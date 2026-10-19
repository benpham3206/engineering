"""Tests for the reference-entry contract in verify.py.

Run from the repo root:  python -m unittest discover -s tests
The fixtures in tests/fixtures are skipped by the repo-wide run, since some are broken on purpose.
"""

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import verify  # noqa: E402

FIXTURES = ROOT / "tests" / "fixtures"


def run(name):
    """All findings for one fixture, as the full per-file check produces them."""
    out = []
    data = verify.Data(out)
    out.clear()
    doc = verify.Doc(FIXTURES / name)
    verify.check_doc(doc, {}, data, out, verify.Stats(), {})
    return doc, out


def contract(findings):
    return [f for f in findings if f.check == "formula-entry"]


class PassingSheet(unittest.TestCase):
    def test_contract_sheet_has_no_findings(self):
        doc, out = run("reference-pass.md")
        self.assertTrue(doc.strict)
        self.assertEqual([str(f) for f in out], [])

    def test_counts_complete_entries(self):
        out, stats = [], verify.Stats()
        data = verify.Data(out)
        verify.check_doc(verify.Doc(FIXTURES / "reference-pass.md"), {}, data, out, stats, {})
        self.assertEqual(stats.c.get("formula-entries"), 2)
        self.assertEqual(stats.c.get("formula-entries-complete"), 2)


class FailingSheets(unittest.TestCase):
    def test_missing_variables(self):
        _, out = run("reference-missing-variables.md")
        msgs = [f.msg for f in contract(out)]
        self.assertEqual(len(msgs), 1)
        self.assertIn("no Variables:", msgs[0])
        self.assertEqual(contract(out)[0].line, 14)  # the equation line

    def test_units(self):
        _, out = run("reference-bad-units.md")
        msgs = "\n".join(f.msg for f in contract(out))
        self.assertIn("'No unit column': Variables: table has no SI unit column", msgs)
        self.assertIn("unit 'deg' is not SI", msgs)
        self.assertIn("unit 'lbf in' is not SI", msgs)
        self.assertIn("unit 'furlong' is not defined", msgs)
        self.assertIn("empty SI unit", msgs)
        self.assertIn("does not end with its SI unit in brackets", msgs)
        self.assertIn("unit 'psi' is not SI", msgs)
        self.assertNotIn("m$^{4}$", msgs)
        self.assertEqual(len(contract(out)), 7)

    def test_limits_and_basis(self):
        _, out = run("reference-missing-limits.md")
        msgs = [f.msg for f in contract(out)]
        self.assertIn("section 'No limits': no Holds when: line", msgs)
        self.assertIn("section 'No limits': no Breaks when: line", msgs)
        self.assertTrue(any("'No basis'" in m and "no link to a derivation" in m for m in msgs))

    def test_fields_must_sit_with_the_equation(self):
        _, out = run("reference-missing-limits.md")
        scoped = [f.msg for f in contract(out) if "'Fields only in a subsection'" in f.msg]
        self.assertEqual(len(scoped), 4)

    def test_strict_findings_are_content_level(self):
        for name in ("reference-missing-variables.md", "reference-bad-units.md", "reference-missing-limits.md"):
            for f in contract(run(name)[1]):
                self.assertEqual(f.level, verify.CONTENT)


class NonStrictSheets(unittest.TestCase):
    def test_reported_as_debt_not_failure(self):
        doc, out = run("reference-debt.md")
        self.assertFalse(doc.strict)
        found = contract(out)
        self.assertEqual(len(found), 1)
        strict = set()
        fails = [f for f in out if f.level == verify.GATE or (f.level == verify.CONTENT and f.path in strict)]
        self.assertEqual(fails, [])


class Units(unittest.TestCase):
    def setUp(self):
        self.units = verify.Data([]).units

    def test_accepts_prefixed_and_latex_units(self):
        for cell in ("Pa", "kN m", "m$^{4}$", "$\\text{m}^4$", "kg/m^3", "N s/m", "rad/s", "1/s", "dimensionless",
                     "um", "µm", "W/m^2 K", "T", "H", "F", "S", "Wb"):
            self.assertIsNone(verify.unit_problem(cell, self.units), cell)

    def test_rejects_non_si(self):
        for cell in ("psi", "deg", "h", "rpm", "in", "lbf"):
            self.assertIsNotNone(verify.unit_problem(cell, self.units), cell)


class RepoScan(unittest.TestCase):
    def test_fixtures_are_not_in_the_repo_run(self):
        self.assertIn("tests", verify.SKIP_DIRS)


if __name__ == "__main__":
    unittest.main()
