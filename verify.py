"""Deterministic verifier for this repo. Standard library only, offline, no network.

Run from anywhere:  python verify.py            (full check and coverage report)
                    python verify.py --show-debt (also list findings in files not yet migrated)
                    python verify.py --today 2030-01-01   (date used for the stale-review report)
                    python verify.py --require-strict path/to/new.md   (CI uses this for added files)

What it checks is specified in VERIFICATION.md. Exit status 1 means the build fails.
"""

import argparse
import ast
import datetime
import math
import re
import sys
from decimal import Decimal, InvalidOperation
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
TYPES = {"lesson", "reference", "philosophy", "data", "track"}
ROOT_META = {"README.md", "ROADMAP.md", "AGENTS.md", "CLAUDE.md", "VERIFICATION.md", "LEVELS.md"}
SKIP_DIRS = {"tests"}  # verifier test fixtures, some broken on purpose; tests/ runs them

# Severity: gate fails anywhere; content fails in strict files and is debt elsewhere; advice never fails.
GATE, CONTENT, ADVICE = "gate", "content", "advice"


class Finding:
    def __init__(self, path, line, check, level, msg):
        self.path, self.line, self.check, self.level, self.msg = path, line, check, level, msg

    def __str__(self):
        return f"{self.path}:{self.line}: [{self.check}] {self.msg}"


# ---------------------------------------------------------------- markdown helpers

LINK = re.compile(r"\]\(([^)\s]+(?:\([^)]*\)[^)\s]*)?)\)")
FENCE = re.compile(r"^```")
VERIFY_OPEN = re.compile(r"^```verify\s*$")
HEADING = re.compile(r"^(#{1,6})\s+(.*\S)\s*$")


def rel(path):
    return path.relative_to(ROOT).as_posix()


def slug(text):
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text).strip().lower()
    text = re.sub(r"[^\w\- ]", "", text)
    return text.replace(" ", "-")


class Doc:
    """One markdown file, split into lines with code and verify-block spans marked."""

    def __init__(self, path):
        self.path = path
        self.rel = rel(path)
        self.text = path.read_text(encoding="utf-8")
        self.lines = self.text.split("\n")
        self.code = set()  # line indexes inside any fence, fence lines included
        self.blocks = []  # (start_index, end_index, source) of verify blocks
        i = 0
        while i < len(self.lines):
            if FENCE.match(self.lines[i]):
                start, is_verify = i, bool(VERIFY_OPEN.match(self.lines[i]))
                i += 1
                while i < len(self.lines) and not FENCE.match(self.lines[i]):
                    i += 1
                self.code.update(range(start, min(i, len(self.lines) - 1) + 1))
                if is_verify:
                    self.blocks.append((start, i, "\n".join(self.lines[start + 1:i])))
            i += 1
        self.math = set()  # line indexes inside multi-line $$ display math
        inside = False
        for n, line in enumerate(self.lines):
            if n in self.code:
                continue
            if line.strip() == "$$":
                self.math.add(n)
                inside = not inside
            elif inside:
                self.math.add(n)
        self.headings = []  # (index, level, title)
        for n, line in enumerate(self.lines):
            m = HEADING.match(line)
            if m and n not in self.code:
                self.headings.append((n, len(m.group(1)), m.group(2)))
        m = re.search(r"^\*\*Type:\*\* (\w+)", self.text, re.M)
        self.type = m.group(1) if m else None
        self.strict = bool(re.search(r"^\*\*Verify:\*\* strict\s*$", self.text, re.M))
        self.anchors = set()
        seen = {}
        for _, _, title in self.headings:
            s = slug(title)
            k = seen.get(s, 0)
            self.anchors.add(s if k == 0 else f"{s}-{k}")
            seen[s] = k + 1

    def section_of(self, index, level=6):
        """Line range (start, end) of the innermost heading section at or above `level` holding index."""
        start, slevel = 0, 0
        for n, lv, _ in self.headings:
            if n <= index and lv <= level:
                start, slevel = n, lv
        end = len(self.lines)
        for n, lv, _ in self.headings:
            if n > index and lv <= max(slevel, 1) and lv <= level:
                end = n
                break
        return start, end

    def sections(self, level=2):
        """Yield (title, start, end) for headings of exactly `level`."""
        hs = [(n, lv, t) for n, lv, t in self.headings if lv <= level]
        for k, (n, lv, t) in enumerate(hs):
            if lv == level:
                end = hs[k + 1][0] if k + 1 < len(hs) else len(self.lines)
                yield t, n, end

    def prose(self, start, end):
        """(index, line) pairs in [start, end) that are not code."""
        return [(n, self.lines[n]) for n in range(start, end) if n not in self.code]


# ---------------------------------------------------------------- number handling

GROUPED = re.compile(r"(?<![\d.])(\d{1,3})(?:[ \u00a0\u2009\u202f]|\\,|\\ )(\d{3})(?![\d])")
NUMTOK = re.compile(r"(?<![\w.])-?\d+(?:\.\d+)?(?![\d])")


def join_groups(s):
    prev = None
    while prev != s:
        prev, s = s, GROUPED.sub(r"\1\2", s)
    return s


def norm_numbers(line):
    """Prose line reduced to the numbers a reader sees: no exponents, subscripts, or link targets."""
    s = line.replace("\u2212", "-").replace("\u00d7", "x")
    s = re.sub(r"\]\([^)]*\)", "]", s)
    s = re.sub(r"\\(?:text|mathrm|mathbf|operatorname)\{([^}]*)\}", r"\1", s)
    s = re.sub(r"(?:\\times|\bx)\s*10\^\{?-?\d+\}?", " ", s)
    s = re.sub(r"\^\{[^}]*\}|\^-?\d+(?:\.\d+)?", " ", s)
    s = re.sub(r"_\{[^}]*\}|_[A-Za-z0-9]+", " ", s)
    s = join_groups(s.replace("$", " "))
    return s


def tokens(text):
    out = []
    for m in NUMTOK.finditer(norm_numbers(text)):
        try:
            out.append(Decimal(m.group()))
        except InvalidOperation:
            pass
    return out


def norm_units(line):
    """Prose line with LaTeX unit markup flattened, for constant scans."""
    s = line.replace("\u2212", "-").replace("\u00d7", "x")
    s = re.sub(r"\\(?:text|mathrm)\{([^}]*)\}", r"\1", s)
    s = s.replace("\\ ", " ").replace("\\,", " ").replace("$", "").replace("{", "").replace("}", "")
    return join_groups(s)


def literal_parts(text):
    """'1.216e4' -> (Decimal mantissa, half-unit-in-last-place as float)."""
    m = re.fullmatch(r"\s*(-?\d+(?:\.(\d+))?)(?:[eE]([-+]?\d+))?\s*", text)
    if not m:
        raise ValueError(f"not a number literal: {text!r}")
    decimals = len(m.group(2) or "")
    exp = int(m.group(3) or 0)
    return Decimal(m.group(1)), 0.5 * 10.0 ** (exp - decimals), float(text)


# ---------------------------------------------------------------- units and quantities

DIM0 = (Fraction(0),) * 7
BASE = ["m", "kg", "s", "A", "K", "mol", "cd"]


class Q:
    __slots__ = ("v", "d")

    def __init__(self, v, d=DIM0):
        self.v, self.d = float(v), d

    def _co(self, o):
        return o if isinstance(o, Q) else Q(o)

    def _same(self, o, op):
        o = self._co(o)
        if o.d != self.d:
            raise VerifyError(f"dimension mismatch in {op}: {dimstr(self.d)} vs {dimstr(o.d)}")
        return o

    def __add__(self, o):
        o = self._same(o, "+")
        return Q(self.v + o.v, self.d)

    __radd__ = __add__

    def __sub__(self, o):
        o = self._same(o, "-")
        return Q(self.v - o.v, self.d)

    def __rsub__(self, o):
        return self._co(o) - self

    def __mul__(self, o):
        o = self._co(o)
        return Q(self.v * o.v, tuple(a + b for a, b in zip(self.d, o.d)))

    __rmul__ = __mul__

    def __truediv__(self, o):
        o = self._co(o)
        return Q(self.v / o.v, tuple(a - b for a, b in zip(self.d, o.d)))

    def __rtruediv__(self, o):
        return self._co(o) / self

    def __pow__(self, o):
        o = self._co(o)
        if o.d != DIM0:
            raise VerifyError("exponent must be dimensionless")
        f = Fraction(o.v).limit_denominator(12)
        return Q(self.v ** o.v, tuple(a * f for a in self.d))

    def __neg__(self):
        return Q(-self.v, self.d)

    def __pos__(self):
        return self

    def cmp(self, o, op):
        o = self._same(o, op)
        return {"<": self.v < o.v, "<=": self.v <= o.v, ">": self.v > o.v, ">=": self.v >= o.v,
                "==": self.v == o.v, "!=": self.v != o.v}[op]


class VerifyError(Exception):
    pass


def dimstr(d):
    parts = [f"{b}^{e}" if e != 1 else b for b, e in zip(BASE, d) if e != 0]
    return " ".join(parts) or "1"


class Units:
    """Unit symbols and SI prefixes, read from data/units.md. Each unit is defined from earlier rows."""

    def __init__(self, rows, prefixes):
        self.u = {}
        self.prefixes = {r["Prefix"]: float(r["Factor"]) for r in prefixes}
        for k, b in enumerate(BASE):
            d = [Fraction(0)] * 7
            d[k] = Fraction(1)
            self.u[b] = Q(1.0, tuple(d))
        for r in rows:
            sym = r["Symbol"]
            if r["Value"] == "base":
                continue
            self.u[sym] = Q(float(r["Value"])) * self.parse(r["In terms of"])

    def one(self, tok):
        m = re.fullmatch(r"([^\s^]+?)(?:\^(-?\d+(?:/\d+)?))?", tok)
        if not m:
            raise VerifyError(f"bad unit token {tok!r}")
        name, power = m.group(1), Fraction(m.group(2) or 1)
        if name in self.u:
            base = self.u[name]
        else:
            for p in sorted(self.prefixes, key=len, reverse=True):
                if name.startswith(p) and name[len(p):] in self.u:
                    base = Q(self.prefixes[p]) * self.u[name[len(p):]]
                    break
            else:
                raise VerifyError(f"unknown unit {name!r}")
        return Q(base.v ** float(power), tuple(a * power for a in base.d))

    def parse(self, text):
        text = (text or "").strip()
        if text in ("", "1"):
            return Q(1.0)
        # The unit's own slash splits numerator from denominator; a slash inside
        # an exponent (Pa m^1/2) belongs to that power and is kept.
        parts = re.split(r"(?<!\^\d)(?<!\^-\d)/|(?<=\^\d)/(?!\d)|(?<=\^-\d)/(?!\d)", text, maxsplit=1)
        num, den = parts[0], parts[1] if len(parts) > 1 else ""
        out = Q(1.0)
        for tok in num.replace("*", " ").replace("\u00b7", " ").split():
            if tok != "1":
                out = out * self.one(tok)
        for tok in den.replace("*", " ").replace("(", " ").replace(")", " ").split():
            out = out / self.one(tok)
        return out


# ---------------------------------------------------------------- data tables

def md_tables(path):
    """All pipe tables in a markdown file, as lists of dicts keyed by header cell."""
    tables, cur, header = [], None, None
    for line in path.read_text(encoding="utf-8").split("\n"):
        if line.startswith("|"):
            raw = line.strip().strip("|").replace(r"\|", "<PIPE>")
            cells = [c.strip().replace("<PIPE>", "|") for c in raw.split("|")]
            if header is None:
                header, cur = cells, []
            elif all(re.fullmatch(r":?-+:?", c) for c in cells):
                continue
            else:
                cur.append(dict(zip(header, cells)))
        elif header is not None:
            tables.append(cur)
            header, cur = None, None
    if header is not None:
        tables.append(cur)
    return tables


def unticks(s):
    s = s.strip()
    return s[1:-1] if s.startswith("`") and s.endswith("`") else s


class Data:
    def __init__(self, findings):
        self.f = findings
        ut = md_tables(DATA / "units.md")
        self.units = Units(ut[0], ut[1])
        self.sources = {r["Key"]: r for r in md_tables(DATA / "sources.md")[0]}
        self.canon = {}  # key -> (Q, half-tolerance Q or None, range (lo, hi) or None, row)
        ct = md_tables(DATA / "constants.md")
        for r in ct[0]:
            self.canon[r["Key"]] = (self.q(r["Value"], r["Unit"]), None, r)
        self.scans = ct[1]
        for r in md_tables(DATA / "properties.md")[0]:
            rng = None
            if r.get("Range"):
                lo, _, hi = r["Range"].partition("..")
                u = self.units.parse(r["Unit"])
                rng = (float(lo) * u.v, float(hi) * u.v)
            self.canon[r["Key"]] = (self.q(r["Value"], r["Unit"]), rng, r)
        for key, (_, _, r) in self.canon.items():
            src = r.get("Source", "")
            for s in [x.strip() for x in src.split(";") if x.strip()]:
                if s not in self.sources:
                    findings.append(Finding("data", 0, "registry", GATE, f"{key}: unknown source {s}"))
        self.claims = load_claims(self, findings)

    def q(self, value, unit):
        return Q(float(value.replace(" ", ""))) * self.units.parse(unit)

    def lookup(self, key):
        if key.startswith("unit:"):
            return self.units.parse(key[5:]), None
        if key not in self.canon:
            raise VerifyError(f"unknown canonical key {key!r}")
        q, rng, _ = self.canon[key]
        return q, rng


def split_top(text, sep=";"):
    """Split on sep outside parentheses and quotes."""
    out, depth, quote, cur = [], 0, False, ""
    for ch in text:
        if ch == '"':
            quote = not quote
        elif not quote and ch == "(":
            depth += 1
        elif not quote and ch == ")":
            depth -= 1
        if ch == sep and depth == 0 and not quote:
            out.append(cur.strip())
            cur = ""
        else:
            cur += ch
    if cur.strip():
        out.append(cur.strip())
    return out


CLAIM_FIELDS = {"Claim", "Values", "Layer", "Status", "Sources", "Checked", "As of", "Review by",
                "Dispute", "Watch", "Require"}
STATUSES = {"unverified", "verified-1", "verified-2", "disputed"}


def load_claims(data, findings):
    claims = {}
    for path in sorted((DATA / "claims").glob("*.md")):
        if path.name == "README.md":
            continue
        doc = Doc(path)
        cur = None
        for n, line in enumerate(doc.lines):
            m = re.match(r"^### (\S+)\s*$", line)
            if m:
                key = m.group(1)
                if key in claims:
                    findings.append(Finding(doc.rel, n + 1, "registry", GATE, f"duplicate claim key {key}"))
                if key != slug(key):
                    findings.append(Finding(doc.rel, n + 1, "registry", GATE, f"claim key not slug-safe: {key}"))
                cur = claims[key] = {"_file": doc.rel, "_line": n + 1}
                continue
            m = re.match(r"^- ([A-Z][a-z]*(?: [a-z]+)?): (.*)$", line)
            if cur is not None and m:
                if m.group(1) not in CLAIM_FIELDS:
                    findings.append(Finding(doc.rel, n + 1, "registry", GATE, f"unknown field {m.group(1)}"))
                if m.group(1) in cur:
                    findings.append(Finding(doc.rel, n + 1, "registry", GATE, f"field {m.group(1)} given twice"))
                cur[m.group(1)] = m.group(2).strip()
    for key, c in claims.items():
        where = (c["_file"], c["_line"])

        def bad(msg):
            findings.append(Finding(*where, "registry", GATE, f"{key}: {msg}"))

        for need in ("Claim", "Values", "Layer", "Status", "Sources"):
            if not c.get(need):
                bad(f"missing {need}")
        if c.get("Layer") not in ("durable", "dated"):
            bad("Layer must be durable or dated (timeless facts are derived, not registered)")
        if c.get("Status") not in STATUSES:
            bad(f"Status must be one of {sorted(STATUSES)}")
        groups, srcs = set(), []
        for item in split_top(c.get("Sources", "")):
            m = re.fullmatch(r"([a-z0-9-]+)\s*\((.+)\)", item)
            if not m:
                bad(f"source needs a locator, as key (locator): {item}")
                continue
            if m.group(1) not in data.sources:
                bad(f"unknown source {m.group(1)}")
                continue
            srcs.append(m.group(1))
            groups.add(data.sources[m.group(1)].get("Group", m.group(1)))
        if not srcs:
            bad("no source: a claim with no checkable public source is left out of the repo")
        st = c.get("Status")
        if st in ("verified-1", "verified-2", "disputed") and not c.get("Checked"):
            bad("verified or disputed claims need Checked (who or what, date, method)")
        if st == "verified-2" and len(groups) < 2:
            bad("verified-2 needs sources from two independent groups")
        if st == "disputed" and not c.get("Dispute"):
            bad("disputed claims need a Dispute line giving the competing values and sources")
        if c.get("Layer") == "dated":
            if not re.fullmatch(r"\d{4}", c.get("As of", "")):
                bad("dated claims need As of: YYYY")
            if not re.fullmatch(r"\d{4}-\d\d-\d\d", c.get("Review by", "")):
                bad("dated claims need Review by: YYYY-MM-DD")
        if bool(c.get("Watch")) != bool(c.get("Require")):
            bad("Watch and Require go together")
        c["_values"] = [v.strip() for v in c.get("Values", "").split(";") if v.strip()]
    return claims


# ---------------------------------------------------------------- verify blocks

FUNCS = {
    "sqrt": lambda x: x ** 0.5, "cbrt": lambda x: x ** Fraction(1, 3),
    "exp": math.exp, "log": math.log, "log10": math.log10, "sin": math.sin, "cos": math.cos,
    "tan": math.tan, "asin": math.asin, "acos": math.acos, "atan": math.atan,
}


class Block:
    """Runs one verify block in a closed evaluator: arithmetic, units, and the block API only."""

    def __init__(self, doc, start, source, data):
        self.doc, self.start, self.src, self.data = doc, start, source, data
        self.env = {"pi": Q(math.pi)}
        self.expects = []  # (line, literal_text, ans, ok)
        self.literals = []  # Decimal values of declared inputs and checked outputs
        self.answers = set()
        self.errors = []  # (line, msg)

    def err(self, node, msg):
        self.errors.append((self.start + 1 + getattr(node, "lineno", 1), msg))

    def run(self):
        try:
            tree = ast.parse(self.src)
        except SyntaxError as e:
            self.errors.append((self.start + 1 + (e.lineno or 1), f"syntax error: {e.msg}"))
            return
        for stmt in tree.body:
            try:
                if isinstance(stmt, ast.Assign) and len(stmt.targets) == 1 and isinstance(stmt.targets[0], ast.Name):
                    name = stmt.targets[0].id
                    if name in API or name in FUNCS or name == "pi":
                        raise VerifyError(f"cannot assign to reserved name {name}")
                    self.env[name] = self.ev(stmt.value)
                elif isinstance(stmt, ast.Expr) and isinstance(stmt.value, ast.Call):
                    self.ev(stmt.value, top=True)
                else:
                    raise VerifyError("only assignments and calls to expect, check, given, skip are allowed")
            except VerifyError as e:
                self.err(stmt, str(e))
            except (ArithmeticError, ValueError, TypeError) as e:
                self.err(stmt, f"{type(e).__name__}: {e}")

    def ev(self, node, top=False):
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and not isinstance(node.value, bool):
            return Q(node.value)
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            return node.value
        if isinstance(node, ast.Name):
            if node.id not in self.env:
                raise VerifyError(f"undefined name {node.id}")
            return self.env[node.id]
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.USub, ast.UAdd)):
            v = self.ev(node.operand)
            return -v if isinstance(node.op, ast.USub) else v
        if isinstance(node, ast.BinOp):
            a, b = self.ev(node.left), self.ev(node.right)
            ops = {ast.Add: lambda: a + b, ast.Sub: lambda: a - b, ast.Mult: lambda: a * b,
                   ast.Div: lambda: a / b, ast.Pow: lambda: a ** b}
            if type(node.op) not in ops:
                raise VerifyError("operator not allowed")
            return ops[type(node.op)]()
        if isinstance(node, ast.Compare) and len(node.ops) == 1:
            ops = {ast.Lt: "<", ast.LtE: "<=", ast.Gt: ">", ast.GtE: ">=", ast.Eq: "==", ast.NotEq: "!="}
            return self.ev(node.left).cmp(self.ev(node.comparators[0]), ops[type(node.ops[0])])
        if isinstance(node, ast.BoolOp):
            vals = [self.ev(v) for v in node.values]
            return all(vals) if isinstance(node.op, ast.And) else any(vals)
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            name = node.func.id
            if name in API:
                return API[name](self, node)
            if top:
                raise VerifyError(f"bare call to {name}")
            if name in FUNCS or name in ("abs", "min", "max", "rnd"):
                args = [self.ev(a) for a in node.args]
                return self.func(name, args)
        raise VerifyError(f"expression not allowed: {ast.dump(node)[:60]}")

    def func(self, name, args):
        if name == "sqrt":
            return args[0] ** 0.5
        if name == "cbrt":
            return args[0] ** Q(1 / 3)
        if name == "abs":
            return Q(abs(args[0].v), args[0].d)
        if name in ("min", "max"):
            for a in args[1:]:
                args[0]._same(a, name)
            pick = (min if name == "min" else max)(args, key=lambda q: q.v)
            return pick
        if name == "rnd":  # rnd(x, digits, "unit"): round x as printed in unit
            x, nd = args[0], int(args[1].v)
            u = self.data.units.parse(args[2] if len(args) > 2 else "")
            x._same(u, "rnd")
            return Q(round(x.v / u.v, nd) * u.v, x.d)
        x = args[0]
        if x.d != DIM0:
            raise VerifyError(f"{name}() needs a dimensionless argument, got {dimstr(x.d)}")
        if name == "atan2":
            return Q(math.atan2(x.v, args[1].v))
        return Q(FUNCS[name](x.v))

    # ---- API

    def kw(self, node, name, default=None):
        for k in node.keywords:
            if k.arg == name:
                return self.ev(k.value)
        return default

    def api_q(self, node):
        lit = node.args[0]
        text = ast.get_source_segment(self.src, lit) or ""
        unit = self.ev(node.args[1]) if len(node.args) > 1 else ""
        mant, half, val = literal_parts(text.replace("_", ""))
        self.literals.append(mant)
        u = self.data.units.parse(unit)
        qv = Q(val) * u
        of = self.kw(node, "of")
        relv = self.kw(node, "rel")
        if of and of != "none":
            canon, rng = self.data.lookup(of)
            if canon.d != qv.d:
                raise VerifyError(f"q({text}, {unit!r}) has dimension {dimstr(qv.d)}, {of} is {dimstr(canon.d)}")
            if rng:
                ok = rng[0] <= qv.v <= rng[1]
            else:
                tol = max(half * u.v, (relv.v if relv else 0) * abs(canon.v)) * (1 + 1e-9)
                ok = abs(qv.v - canon.v) <= tol
            if not ok:
                raise VerifyError(f"{text} {unit} disagrees with canonical {of} = {canon.v / u.v:.10g} {unit}")
        elif of is None:
            for key, (cq, _, _) in self.data.canon.items():
                if cq.d == qv.d and cq.d != DIM0 and cq.v and abs(qv.v - cq.v) <= 0.02 * abs(cq.v):
                    raise VerifyError(f"{text} {unit} looks like canonical {key}: declare of={key!r} (or of='none')")
        return qv

    def api_const(self, node):
        return self.data.lookup(self.ev(node.args[0]))[0]

    def api_u(self, node):
        return self.data.units.parse(self.ev(node.args[0]))

    def api_given(self, node):
        for a in node.args:
            text = self.ev(a)
            self.literals.append(literal_parts(text)[0])
        return None

    def api_skip(self, node):
        ans = self.kw(node, "ans")
        if ans is None or not self.kw(node, "why"):
            raise VerifyError("skip needs ans= and why=")
        self.answers.add(int(ans.v))

    def api_check(self, node):
        ok = self.ev(node.args[0])
        if ok is not True:
            msg = self.ev(node.args[1]) if len(node.args) > 1 else ast.get_source_segment(self.src, node.args[0])
            raise VerifyError(f"check failed: {msg}")

    def api_expect(self, node):
        value = self.ev(node.args[0])
        text = self.ev(node.args[1])
        m = re.fullmatch(r"\s*(-?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?)\s*(.*?)\s*", text)
        if not isinstance(value, Q) or not m:
            raise VerifyError(f"expect needs a quantity and a printed value like '12.2 kPa', got {text!r}")
        mant, half, printed = literal_parts(m.group(1))
        u = self.data.units.parse(m.group(2))
        if u.d != value.d:
            raise VerifyError(f"expect {text!r}: computed dimension is {dimstr(value.d)}, printed unit is {dimstr(u.d)}")
        relv = self.kw(node, "rel")
        tol = max(half, (relv.v if relv else 0) * abs(printed)) * (1 + 1e-9)
        computed = value.v / u.v
        ans = self.kw(node, "ans")
        ans = int(ans.v) if ans is not None else None
        line = self.start + 1 + node.lineno
        self.literals.append(mant)
        if ans is not None:
            self.answers.add(ans)
        if abs(computed - printed) > tol:
            raise VerifyError(f"expect {text!r}: computed {computed:.6g} {m.group(2)}".rstrip())
        self.expects.append((line, mant, ans, text))
        return None


API = {"q": Block.api_q, "const": Block.api_const, "u": Block.api_u, "given": Block.api_given,
       "skip": Block.api_skip, "check": Block.api_check, "expect": Block.api_expect}


# ---------------------------------------------------------------- per-file checks

PROCESS = re.compile(r"(?i)\b(this session|computed with python|computed in python|fetched (this|in this)|"
                     r"not fetched|as an ai|language model|todo|tbd|fixme)\b")
DASH = re.compile("[\u2014\u2013]")
CURLY = re.compile("[\u2018\u2019\u201c\u201d]")
EMOJI = re.compile("[\U0001F300-\U0001FAFF\u2600-\u27BF]")
ANSWER_ITEM = re.compile(r"^\s*(\d+)\.\s")
DATE_TRIGGER = re.compile(
    r"\b(1[0-9]{3}|20[0-9]{2})s?\b|\b\d{1,4}\s*(BC|BCE|AD|CE)\b|"
    r"\b(\d{1,2}(st|nd|rd|th)|first|second|third|fourth|fifth|sixth|seventh|eighth|ninth|tenth|eleventh|"
    r"twelfth|thirteenth|fourteenth|fifteenth|sixteenth|seventeenth|eighteenth|nineteenth|twentieth|"
    r"twenty-first)[- ]century\b|\b(killed|died|deaths|fatalities)\b|\b(the|one of the) first\b", re.I)
AS_OF = re.compile(r"\(?as of (\d{4})\)?", re.I)
APPROX = re.compile(r"(?i)\b(about|around|circa|c\.|approximately|roughly)\s")
SENT_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-Z*(\[])")
CONTROL = re.compile("[\x00-\x08\x0b\x0c\x0e-\x1f\t]")
# Long LaTeX command names that are never plain words inside math. A lost
# backslash turns k\Omega into kOmega, which renders as italic letters.
BARE_COMMAND = re.compile(
    r"(alpha|beta|gamma|delta|epsilon|theta|lambda|sigma|omega|varphi"
    r"|Omega|Delta|Sigma|Gamma|Lambda|Theta|frac|sqrt|times|cdot|infty|partial|nabla)$")


def bare_commands(line):
    """LaTeX command names missing their backslash inside $...$ spans.

    Each letter run is a token; a run that starts with a backslash is a command
    and is fine (\\dfrac, \\varepsilon). A run without one that ends in a command
    name (kOmega, arepsilon, frac) lost its backslash.
    """
    s = re.sub(r"`[^`]*`", " ", line)
    out = []
    for m in re.finditer(r"\$\$?([^$]+)\$\$?", s):
        body = re.sub(r"\\(?:text|mathrm|operatorname|mathit|mathbf)\{[^}]*\}", " ", m.group(1))
        for tok in re.finditer(r"(\\?)([A-Za-z]+)", body):
            if not tok.group(1) and (b := BARE_COMMAND.search(tok.group(2))):
                out.append(b.group())
    return out


def unrendered_math(line):
    """Inline $...$ spans that GitHub shows as raw text.

    GitHub renders inline math only when the opening $ follows whitespace, the
    line start, "(" or "**", and the closing $ is not followed by a letter or
    digit. So kg/m$^3$ and $F$s stay raw; write $\\text{kg/m}^3$ and $F\\text{s}$.
    """
    s = re.sub(r"`[^`]*`", lambda m: " " * len(m.group()), line)
    bad, i = [], 0
    while (a := s.find("$", i)) >= 0:
        if a and s[a - 1] == "\\":
            i = a + 1
            continue
        if s.startswith("$$", a):
            b = s.find("$$", a + 2)
            if b < 0:
                break
            i = b + 2
            continue
        b = a + 1
        while (b := s.find("$", b)) > 0 and s[b - 1] == "\\":
            b += 1
        if b < 0:
            break
        pre, post = s[:a], s[b + 1:b + 2]
        if (pre and not (pre[-1].isspace() or pre[-1] == "(" or pre.endswith("**"))) or post.isalnum():
            bad.append(line[max(0, a - 12):b + 3])
        i = b + 1
    return bad


PLAIN_MATH = re.compile(r"[A-Za-z0-9)\]]\^-?[A-Za-z0-9({]|\bsqrt\(|[\u0391-\u03a9\u03b1-\u03c9\u2264\u2265\u2248\u00b1\u00f7\u221a\u221e\u222b\u2211\u2202\u00d7\u2260]")
LABEL_LINE = re.compile(r"^\*\*[A-Za-z][A-Za-z ,()-]*:\*\*")
DEFINITION = re.compile(r"\b(is|are|was|were|means|refers to|describes)\b")
EXAMPLE_LINE = re.compile(r"\b(Example|Worked check|Worked result)\b|\(computed\)")

LESSON_SECTIONS = ["Core ideas", "Practice", "Common mistakes", "Go deeper"]
DEVICE_SECTIONS = ["Design trade-offs", "How it fails", "History"]
HISTORY_SECTIONS = ["Key inventions", "Key equations", "Worked example", "Lessons for engineers today"]
REFERENCE_SECTIONS = ["Principles", "Further reference"]
HISTORY_EXEMPT = ("Key equations", "Worked example", "Practice", "Go deeper")


class Stats:
    def __init__(self):
        self.c = {}

    def add(self, k, n=1):
        self.c[k] = self.c.get(k, 0) + n


def is_meta(doc):
    return doc.path.parent == ROOT and doc.path.name in ROOT_META


def kind(doc):
    parts = doc.rel.split("/")
    if doc.type != "lesson" or not re.match(r"\d\d-", parts[-1]):
        return doc.type
    if parts[0] == "applications" and len(parts) == 3 and parts[1] != "projects":
        return "device"
    if parts[0] == "history" and len(parts) == 2:
        return "history"
    return "lesson"


def check_doc(doc, docs, data, out, stats, prereqs):
    def add(n, check, level, msg):
        out.append(Finding(doc.rel, n + 1, check, level, msg))

    # links and anchors
    for n, line in enumerate(doc.lines):
        if n in doc.code:
            continue
        for target in LINK.findall(re.sub(r"`[^`]*`", "", line)):
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            path, _, anchor = target.partition("#")
            dest = (doc.path.parent / path).resolve() if path else doc.path
            if not dest.exists():
                add(n, "link", GATE, f"broken link {target}")
                continue
            if anchor and dest.suffix == ".md":
                other = docs.get(dest) or Doc(dest)
                if anchor not in other.anchors:
                    add(n, "anchor", GATE, f"no heading #{anchor} in {rel(dest)}")
        if DASH.search(line):
            add(n, "dash", GATE, "em or en dash")
        if CONTROL.search(line) and n not in doc.code:
            add(n, "control", GATE, "control character (often a collapsed escape: \\t in \\text, \\a in \\arctan, "
                                    "\\v in \\varepsilon, \\f in \\frac, \\b in \\beta)")
        if n not in doc.code:
            for name in bare_commands(line):
                add(n, "math-render", GATE, f"LaTeX command without its backslash in math: {name!r}")
        if n not in doc.math:
            for span in unrendered_math(line):
                add(n, "math-render", GATE, f"inline math GitHub will not render: {span!r}")
        if not is_meta(doc) and doc.path.parent != DATA and doc.path.parent.parent != DATA:
            if PROCESS.search(line):
                add(n, "process-note", CONTENT, f"process note: {PROCESS.search(line).group()}")
            if CURLY.search(line) or EMOJI.search(line):
                add(n, "characters", CONTENT, "curly quote or emoji")
            bare = re.sub(r"\$\$.*?\$\$|\$[^$]*\$|`[^`]*`|\]\([^)]*\)", " ", line)
            if n not in doc.math and "$$" not in bare and PLAIN_MATH.search(bare):
                add(n, "plain-math", CONTENT, f"math outside $...$: {PLAIN_MATH.search(bare).group()!r}")
        if line.startswith("**Prerequisites:**"):
            for target in LINK.findall(line):
                if target.endswith(".md") and not target.startswith("http"):
                    dest = (doc.path.parent / target).resolve()
                    if dest.exists() and dest.name != "README.md":
                        prereqs.setdefault(doc.path, set()).add(dest)

    if is_meta(doc) or doc.path.name == "README.md":
        return
    if doc.type not in TYPES:
        add(0, "type", GATE, "missing or unknown **Type:** line")
        return
    k = kind(doc)
    stats.add(f"type:{doc.type}")
    if doc.strict:
        stats.add("strict")

    # template
    h2 = [t for _, lv, t in doc.headings if lv == 2]
    need = []
    if k in ("lesson", "device", "history"):
        need = list(LESSON_SECTIONS)
        if k == "device":
            need += DEVICE_SECTIONS
        if k == "history":
            need += HISTORY_SECTIONS
        for line_start in ("**Prerequisites:**", "**Time:**"):
            if line_start not in doc.text:
                add(0, "template", CONTENT, f"missing {line_start} line")
    elif k == "reference" and doc.path.name.startswith("reference"):
        need = REFERENCE_SECTIONS
    for s in need:
        if not any(t == s or t.startswith(s + ":") or t.startswith(s + " ") for t in h2):
            add(0, "template", CONTENT, f"missing section ## {s}")
    if k in ("lesson", "device", "history", "philosophy"):
        first = next((l for n, l in enumerate(doc.lines[1:], 1) if l.strip() and n not in doc.code
                      and not LABEL_LINE.match(l) and not l.startswith(("#", "<", "|", "-", ">"))), "")
        if not DEFINITION.search(SENT_SPLIT.split(first)[0] if first else ""):
            add(0, "definition", CONTENT, "first sentence after the title must say what the topic is")

    # practice answers
    for title, a, b in doc.sections(2):
        if title == "Practice":
            body = "\n".join(doc.lines[a:b])
            if "<details>" not in body:
                add(a, "practice", CONTENT, "practice answers are not in a <details> block")
            else:
                d0 = next(n for n in range(a, b) if "<details>" in doc.lines[n])
                d1 = next((n for n in range(d0, b) if "</details>" in doc.lines[n]), b)
                items = answer_items(doc, d0, d1)
                numeric = {i for i, (s, e) in items.items()
                           if tokens(ANSWER_ITEM.sub("", text_of(doc, s, e), count=1))}
                stats.add("answers", len(numeric))
                doc_answers = (d0, d1, items, numeric)
                check_answers(doc, doc_answers, data, add, stats)
        if title.startswith("Worked example"):
            stats.add("worked")
            check_worked(doc, a, b, data, add, stats)

    if k == "reference":
        check_reference_examples(doc, data, add, stats)
        check_formula_entries(doc, data, add, stats)

    # blocks outside the places above still run
    for start, end, src in doc.blocks:
        if not any(start == s for s, _, _ in getattr(doc, "_ran", [])):
            blk = run_block(doc, start, src, data, add)
            stats.add("blocks")
            stats.add("expects", len(blk.expects))

    check_scans(doc, data, add, stats)
    check_claims(doc, data, add, stats)


def text_of(doc, s, e):
    return "\n".join(l for n, l in doc.prose(s, e))


def answer_items(doc, d0, d1):
    items, cur = {}, None
    for n in range(d0, d1):
        if n in doc.code:
            continue
        m = ANSWER_ITEM.match(doc.lines[n])
        if m:
            cur = int(m.group(1))
            items[cur] = [n, n + 1]
        elif cur is not None and doc.lines[n].strip() and not doc.lines[n].startswith("<"):
            items[cur][1] = n + 1
    return {k: tuple(v) for k, v in items.items()}


def run_block(doc, start, src, data, add):
    if not hasattr(doc, "_ran"):
        doc._ran = []
    for s, blk, _ in doc._ran:
        if s == start:
            return blk
    blk = Block(doc, start, src, data)
    blk.run()
    for line, msg in blk.errors:
        add(line - 1, "verify", GATE, msg)
    doc._ran.append((start, blk, None))
    return blk


def presence(doc, blk, scope_tokens, add, item_tokens=None):
    for line, mant, ans, text in blk.expects:
        pool = item_tokens.get(ans, []) if (ans is not None and item_tokens is not None) else scope_tokens
        if mant not in pool:
            where = f"answer {ans}" if ans is not None else "this section"
            add(line - 1, "prose-match", GATE, f"expect {text!r}: {mant} is not printed in {where}")


def coverage(doc, s, e, literals, add, label, stats, level=CONTENT):
    missing = []
    for n, line in doc.prose(s, e):
        if line.startswith("**Prerequisites") or ANSWER_ITEM.match(line) and False:
            continue
        body = ANSWER_ITEM.sub("", line, count=1)
        for t in tokens(body):
            if abs(t) < 10 and t == t.to_integral_value():
                continue
            stats.add("numbers")
            if t in literals or -t in literals:
                stats.add("numbers-checked")
                continue
            missing.append((n, t))
    for n, t in missing:
        add(n, "number-coverage", level, f"{label}: printed number {t} is not an input or a checked result")
    return not missing


def check_worked(doc, a, b, data, add, stats):
    blocks = [(s, src) for s, e, src in doc.blocks if a <= s < b]
    if not blocks:
        add(a, "worked-unverified", CONTENT, "worked example has no verify block")
        return
    lits, ok_all = set(), True
    scope = [t for n, l in doc.prose(a, b) for t in tokens(l)]
    for s, src in blocks:
        blk = run_block(doc, s, src, data, add)
        stats.add("blocks")
        stats.add("expects", len(blk.expects))
        ok_all &= not blk.errors and bool(blk.expects)
        lits.update(blk.literals)
        presence(doc, blk, scope, add)
    covered = coverage(doc, a, b, lits, add, "worked example", stats)
    if ok_all and covered:
        stats.add("worked-verified")


def check_answers(doc, info, data, add, stats):
    d0, d1, items, numeric = info
    blocks = [(s, src) for s, e, src in doc.blocks if d0 <= s < d1]
    covered_items, lits = set(), set()
    item_tokens = {i: [t for n, l in doc.prose(s, e) for t in tokens(l)] for i, (s, e) in items.items()}
    for s, src in blocks:
        blk = run_block(doc, s, src, data, add)
        stats.add("blocks")
        stats.add("expects", len(blk.expects))
        if not blk.errors:
            covered_items |= blk.answers
        lits.update(blk.literals)
        presence(doc, blk, [], add, item_tokens)
    for i in sorted(numeric):
        if i not in covered_items:
            add(items[i][0], "answer-unverified", CONTENT, f"practice answer {i} has no expect(ans={i}) or skip")
            continue
        s, e = items[i]
        if coverage(doc, s, e, lits, add, f"answer {i}", stats):
            stats.add("answers-verified")


def check_reference_examples(doc, data, add, stats):
    n = 0
    lines = doc.lines
    spans = []
    while n < len(lines):
        if n not in doc.code and EXAMPLE_LINE.search(lines[n]) and not lines[n].startswith("#"):
            s = n
            n += 1
            while n < len(lines) and n not in doc.code and (not lines[n].strip() or lines[n].startswith(("- ", "|", "  "))) \
                    and not lines[n].startswith("Holds when"):
                if not lines[n].strip() and n + 1 < len(lines) and not lines[n + 1].startswith(("- ", "|")):
                    break
                n += 1
            spans.append((s, n))
        else:
            n += 1
    for s, e in spans:
        stats.add("worked")
        a, b = doc.section_of(s)
        blocks = [(bs, src) for bs, be, src in doc.blocks if a <= bs < b]
        if not blocks:
            add(s, "worked-unverified", CONTENT, "example line in a section with no verify block")
            continue
        lits, ok = set(), True
        scope = [t for m, l in doc.prose(a, b) for t in tokens(l)]
        for bs, src in blocks:
            blk = run_block(doc, bs, src, data, add)
            ok &= not blk.errors
            lits.update(blk.literals)
        if coverage(doc, s, e, lits, add, "example", stats) and ok:
            stats.add("worked-verified")
    seen = set()
    for bs, be, src in doc.blocks:
        a, b = doc.section_of(bs)
        blk = run_block(doc, bs, src, data, add)
        if bs not in seen:
            seen.add(bs)
            stats.add("blocks")
            stats.add("expects", len(blk.expects))
        scope = [t for m, l in doc.prose(a, b) for t in tokens(l)]
        presence(doc, blk, scope, add)


FIELD_LABELS = ("Holds when:", "Breaks when:", "Source and basis:")
VARIABLES_LABEL = "Variables:"
UNIT_HEADER = re.compile(r"(?i)^si units?$")
LIST_UNIT = re.compile(r"\[([^\[\]]+)\]\s*$")
DIMENSIONLESS = {"dimensionless", "1"}
DERIVED = re.compile(r"(?i)\bderived from\b")


def unit_text(cell):
    """A unit as written in a variables table ($\\text{N m}$, m$^{4}$, kg/m^3) in verifier syntax."""
    s = cell.strip().replace("$", "")
    s = re.sub(r"\\(?:text|mathrm)\{([^}]*)\}", r"\1", s)
    for a, b in (("\\,", " "), ("\\ ", " "), ("\\cdot", " "), ("\u00b7", " "), ("\u00b5", "u"), ("\u03bc", "u"),
                 ("\u2212", "-")):
        s = s.replace(a, b)
    s = re.sub(r"\^\{([^}]*)\}", r"^\1", s).replace("{", "").replace("}", "")
    return " ".join(s.split())


def unit_problem(cell, units):
    """None if cell names an SI unit (optionally prefixed) or says dimensionless; else the reason."""
    s = unit_text(cell)
    if not s:
        return "empty SI unit"
    if s.lower() in DIMENSIONLESS:
        return None
    try:
        qv = units.parse(s)
    except VerifyError:
        return f"unit {cell.strip()!r} is not defined in data/units.md"
    exp = math.log10(qv.v) if qv.v > 0 else 0.5
    if abs(exp - round(exp)) > 1e-9:
        return f"unit {cell.strip()!r} is not SI (it is {qv.v:.6g} times the SI unit)"
    return None


def entries(doc):
    """(start, end) of each heading's own text, up to the next heading of any level, plus the preamble."""
    starts = [0] + [n for n, _, _ in doc.headings]
    ends = [n for n, _, _ in doc.headings] + [len(doc.lines)]
    return [(a, b) for a, b in zip(starts, ends) if a < b]


def variables_problems(doc, a, b, units):
    lines = [(n, l) for n, l in doc.prose(a, b)]
    label = next((k for k, (n, l) in enumerate(lines) if l.startswith(VARIABLES_LABEL)), None)
    if label is None:
        return ["no Variables: table or list naming each symbol with its SI unit"]
    rest = [(n, l) for n, l in lines[label + 1:]]
    while rest and not rest[0][1].strip():
        rest.pop(0)
    out = []
    if rest and rest[0][1].startswith("|"):
        rows = []
        for n, l in rest:
            if not l.startswith("|"):
                break
            rows.append((n, [c.strip() for c in l.strip().strip("|").replace(r"\|", "\x00").split("|")]))
        header = rows[0][1]
        col = next((k for k, c in enumerate(header) if UNIT_HEADER.match(c)), None)
        body = [(n, cells) for n, cells in rows[1:] if not all(re.fullmatch(r":?-+:?", c) for c in cells)]
        if col is None:
            return ["Variables: table has no SI unit column"]
        if not body:
            return ["Variables: table has no rows"]
        for n, cells in body:
            if not cells[0].strip():
                out.append(f"line {n + 1}: variables row has no symbol")
            p = unit_problem(cells[col] if col < len(cells) else "", units)
            if p:
                out.append(f"line {n + 1}: {p}")
        return out
    items = []
    for n, l in rest:
        if not l.startswith("- "):
            break
        items.append((n, l))
    if not items:
        return ["Variables: must be followed by a table or a bullet list"]
    for n, l in items:
        m = LIST_UNIT.search(l)
        if not m:
            out.append(f"line {n + 1}: variables item does not end with its SI unit in brackets, as [Pa]")
            continue
        p = unit_problem(m.group(1), units)
        if p:
            out.append(f"line {n + 1}: {p}")
    return out


def check_formula_entries(doc, data, add, stats):
    """Each heading's text that holds display math must carry the reference-entry contract fields."""
    for a, b in entries(doc):
        eqs = [n for n, l in doc.prose(a, b) if n in doc.math or "$$" in l]
        if not eqs:
            continue
        stats.add("formula-entries")
        problems = variables_problems(doc, a, b, data.units)
        prose = doc.prose(a, b)
        for label in FIELD_LABELS:
            hit = next((l for n, l in prose if l.startswith(label)), None)
            if hit is None or not hit[len(label):].strip():
                problems.append(f"no {label} line")
            elif label == "Source and basis:" and not (LINK.search(hit) or DERIVED.search(hit)):
                problems.append("Source and basis: gives no link to a derivation or claim and no 'derived from'")
        title = next((t for n, _, t in doc.headings if n == a), "preamble")
        for p in problems:
            add(eqs[0], "formula-entry", CONTENT, f"section {title!r}: {p}")
        if not problems:
            stats.add("formula-entries-complete")


def check_scans(doc, data, add, stats):
    if doc.path.parent == DATA or doc.path.parent.parent == DATA:
        return
    for n, line in enumerate(doc.lines):
        if n in doc.code or line.startswith("#"):
            continue
        s = norm_units(line)
        for row in data.scans:
            pat = unticks(row["Pattern"])
            for m in re.finditer(pat, s):
                ctx, unless = unticks(row.get("Context", "")), unticks(row.get("Unless", ""))
                if ctx and not re.search(ctx, s):
                    continue
                if unless and re.search(unless, s):
                    continue
                stats.add("scan-hits")
                mant, half, val = literal_parts(m.group("v").replace(" ", ""))
                u = data.units.parse(row["Unit"])
                eq = row["Equals"]
                canon = data.lookup(eq)[0] if not re.match(r"-?\d", eq) else data.q(*eq.split(" ", 1))
                if abs(val * u.v - canon.v) > half * u.v * (1 + 1e-9):
                    add(n, "constant", CONTENT, f"{m.group('v')} {row['Unit']} disagrees with {eq} "
                                                f"= {canon.v / u.v:.8g} {row['Unit']}")
                    stats.add("scan-mismatch")
                if row.get("Planet") == "yes" and not re.search(r"(?i)earth|standard|terrestrial", s):
                    add(n, "planet", CONTENT, f"{m.group('v')} {row['Unit']} is an Earth value; say Earth or standard")
                    stats.add("scan-planet")


def claim_units(doc, a, b):
    """Sentences, bullets, and table rows in [a, b) as (index, text)."""
    out = []
    for n, line in doc.prose(a, b):
        if not line.strip() or line.startswith("#") or re.match(r"^\|[\s:|-]+\|$", line.strip()):
            continue
        if line.startswith("**") and re.match(r"^\*\*(Type|Prerequisites|Time|Verify):\*\*", line):
            continue
        if line.startswith("|"):
            out.append((n, line))
        else:
            out.extend((n, s) for s in SENT_SPLIT.split(line))
    return out


def citations(text, doc):
    keys = []
    for target in LINK.findall(text):
        path, _, anchor = target.partition("#")
        if not path or not anchor:
            continue
        dest = (doc.path.parent / path).resolve()
        if dest.parent == DATA / "claims":
            keys.append(anchor)
    return keys


def check_claims(doc, data, add, stats):
    if doc.path.parent == DATA or doc.path.parent.parent == DATA or is_meta(doc):
        return
    k = kind(doc)
    scopes = []
    if doc.rel.startswith("history/"):
        first = doc.headings[1][0] if len(doc.headings) > 1 else len(doc.lines)
        scopes.append((0, first))
        for title, a, b in doc.sections(2):
            if not title.startswith(HISTORY_EXEMPT):
                scopes.append((a + 1, b))
    else:
        scopes = [(a + 1, b) for title, a, b in doc.sections(2) if title == "History"]
    in_scope = set()
    for a, b in scopes:
        for n, text in claim_units(doc, a, b):
            in_scope.add((n, text))
    units = claim_units(doc, 0, len(doc.lines))
    for n, text in units:
        for key in citations(text, doc):
            stats.add("citations")
            c = data.claims.get(key)
            if not c:
                add(n, "claim", GATE, f"cites unknown claim {key}")
                continue
            if c.get("Status") == "unverified":
                add(n, "claim-status", CONTENT, f"cites {key}, which is unverified")
            else:
                stats.add("citations-verified")
            said = re.sub(r"\]\([^)]*\)", "]", text).lower()
            for v in c["_values"]:
                miss = []
                lv = v.lower()
                if ".." in lv:
                    miss = [x for x in lv.split("..") if x.strip() not in said]
                elif lv.startswith("~"):
                    if lv[1:] not in said or not APPROX.search(said):
                        miss = [v]
                elif lv not in said:
                    miss = [v]
                if miss:
                    add(n, "claim-value", CONTENT, f"cites {key} but does not state {v!r}")
        cited = citations(text, doc)
        if (n, text) in in_scope:
            prose = re.sub(r"\[[^\]]*\]\([^)]*\)", "", text)
            if DATE_TRIGGER.search(prose):
                stats.add("claims-found")
                if cited:
                    stats.add("claims-cited")
                else:
                    add(n, "uncited", CONTENT, f"dated or first-of claim without a citation: {prose.strip()[:80]}")
        for m in AS_OF.finditer(text):
            ok = any(data.claims.get(key, {}).get("Layer") == "dated" and data.claims[key].get("As of") == m.group(1)
                     for key in cited)
            stats.add("dated")
            if not ok:
                add(n, "dated", CONTENT, f"'as of {m.group(1)}' needs a citation to a dated claim with that year")
    for key, c in data.claims.items():
        if not c.get("Watch"):
            continue
        for n, line in enumerate(doc.lines):
            said = re.sub(r"\]\([^)]*\)", "]", line)
            if n not in doc.code and re.search(c["Watch"], said) and c["Require"].lower() not in said.lower():
                add(n, "watch", CONTENT, f"mentions {c['Watch']} without {c['Require']!r} (claim {key})")


def find_cycles(prereqs):
    out, state = [], {}

    def visit(node, stack):
        state[node] = 1
        for nxt in sorted(prereqs.get(node, ())):
            if state.get(nxt) == 1:
                out.append(stack[stack.index(nxt):] + [nxt] if nxt in stack else [node, nxt])
            elif not state.get(nxt):
                visit(nxt, stack + [nxt])
        state[node] = 2

    for node in sorted(prereqs):
        if not state.get(node):
            visit(node, [node])
    return out


def check_readmes(docs, out):
    for path, doc in docs.items():
        if path.name != "README.md" or path.parent == ROOT:
            continue
        for sib in sorted(path.parent.glob("*.md")):
            if sib.name != "README.md" and f"({sib.name})" not in doc.text and f"({sib.name}#" not in doc.text:
                out.append(Finding(doc.rel, 1, "readme", CONTENT, f"does not link {sib.name}"))


# ---------------------------------------------------------------- main

def main(argv=None):
    ap = argparse.ArgumentParser(description="Verify the engineering reference.")
    ap.add_argument("--today", default=datetime.date.today().isoformat(), help="date for stale-review report")
    ap.add_argument("--show-debt", action="store_true", help="list findings in files not yet migrated")
    ap.add_argument("--require-strict", nargs="*", default=[], help="files that must carry **Verify:** strict")
    args = ap.parse_args(argv)

    out = []
    data = Data(out)
    files = sorted(p for p in ROOT.rglob("*.md")
                   if ".git" not in p.parts and p.relative_to(ROOT).parts[0] not in SKIP_DIRS)
    docs = {p.resolve(): Doc(p) for p in files}
    stats, prereqs = Stats(), {}
    for p, doc in docs.items():
        check_doc(doc, docs, data, out, stats, prereqs)
    for cyc in find_cycles(prereqs):
        out.append(Finding(rel(cyc[0]), 1, "prereq-cycle", GATE, " -> ".join(rel(c) for c in cyc)))
    check_readmes(docs, out)
    for f in args.require_strict:
        p = (Path.cwd() / f).resolve()
        if p.suffix == ".md" and p in docs and not docs[p].strict and not is_meta(docs[p]) and p.name != "README.md" \
                and DATA not in p.parents:
            out.append(Finding(rel(p), 1, "require-strict", GATE, "new content files must carry **Verify:** strict"))
    today = args.today
    for key, c in data.claims.items():
        if c.get("Review by") and c["Review by"] < today:
            out.append(Finding(c["_file"], c["_line"], "stale", ADVICE, f"{key}: review by {c['Review by']} has passed"))
    for key, s in data.sources.items():
        if not s.get("Archive") or s["Archive"] == "pending":
            out.append(Finding("data/sources.md", 0, "archive", ADVICE, f"{key}: no archive snapshot yet"))

    strict = {d.rel for d in docs.values() if d.strict}
    fails = [f for f in out if f.level == GATE or (f.level == CONTENT and f.path in strict)]
    debt = [f for f in out if f.level == CONTENT and f.path not in strict]
    advice = [f for f in out if f.level == ADVICE]

    for f in fails:
        print("FAIL", f)
    if args.show_debt:
        for f in debt:
            print("debt", f)
    for f in advice:
        if f.check == "stale":
            print("stale", f)

    c = stats.c
    content = sum(v for k, v in c.items() if k.startswith("type:"))
    statuses = {}
    for cl in data.claims.values():
        statuses[cl.get("Status")] = statuses.get(cl.get("Status"), 0) + 1
    by_check = {}
    for f in debt:
        by_check[f.check] = by_check.get(f.check, 0) + 1

    def pct(a, b):
        return f"{a} / {b} ({100.0 * a / b:.1f}%)" if b else f"{a} / 0"

    print()
    print(f"Coverage ({len(files)} markdown files, {content} content files, today {today})")
    print(f"  strict files            {pct(c.get('strict', 0), content)}")
    print(f"  worked examples         {pct(c.get('worked-verified', 0), c.get('worked', 0))} fully verified")
    print(f"  practice answers        {pct(c.get('answers-verified', 0), c.get('answers', 0))} numeric answers verified")
    print(f"  printed numbers         {pct(c.get('numbers-checked', 0), c.get('numbers', 0))} in examples and answers")
    print(f"  verify blocks           {c.get('blocks', 0)} blocks, {c.get('expects', 0)} expects passing")
    print(f"  formula entries         {pct(c.get('formula-entries-complete', 0), c.get('formula-entries', 0))} "
          f"complete (reference sections with display math)")
    print(f"  dated or first-of claims {pct(c.get('claims-cited', 0), c.get('claims-found', 0))} cited (history scopes)")
    print(f"  citations               {c.get('citations', 0)} ({c.get('citations-verified', 0)} to checked claims)")
    print(f"  claims registry         {len(data.claims)} claims: " +
          ", ".join(f"{k} {v}" for k, v in sorted(statuses.items(), key=lambda x: str(x[0]))))
    print(f"  sources registry        {len(data.sources)} sources, {sum(1 for f in advice if f.check == 'archive')} without archive snapshot")
    print(f"  constant scans          {c.get('scan-hits', 0)} hits, {c.get('scan-mismatch', 0)} disagree, "
          f"{c.get('scan-planet', 0)} without Earth or standard")
    print(f"  stale dated claims      {sum(1 for f in advice if f.check == 'stale')}")
    print(f"  debt in unmigrated files {len(debt)}: " + ", ".join(f"{k} {v}" for k, v in sorted(by_check.items())))
    print()
    print(f"Result: {'FAIL' if fails else 'PASS'} ({len(fails)} failing finding(s))")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
