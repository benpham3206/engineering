# Verification

How this repo proves its content, and where proof stops. The runner is [verify.py](verify.py). It uses only the Python standard library, reads only files in this repo, never touches the network, and gives the same result for the same files and the same `--today` date.

```
python verify.py                 # check everything, print coverage, exit 1 on failure
python verify.py --show-debt     # also list findings in files not yet migrated
python verify.py --today 2031-06-01           # date used for the stale-review report
python verify.py --require-strict new-file.md # fail unless these files are strict
```

Nothing merges unless `python verify.py` passes. CI runs the same command on every pull request ([workflow](.github/workflows/verify.yml)) and passes every added markdown file to `--require-strict`, so new content arrives migrated.

## What a machine can prove, and what it cannot

| The verifier proves | The verifier cannot prove |
|---|---|
| Every checked number printed in a worked example or answer equals a recomputation from the stated inputs, within the rounding shown | That the formula in the block is the right physics for the situation. A wrong formula used consistently in prose and block passes |
| Every formula in a block is dimensionally consistent, and every printed unit has the dimension of the computed quantity | That the inputs and assumptions are realistic |
| Every printed number in a strict example or answer is either a declared input or a checked result | That a number outside examples and answers (in core ideas or tables of typical values) is right, unless a prose scan covers it |
| Every rounded constant or property agrees with the one canonical row in `data/` | That the canonical row itself is right. That rests on its source and on the person or agent who checked it |
| Every citation resolves to a registered claim, every claim names a registered source with a locator, every status is backed by the number of independent sources it claims, and the citing sentence states the registered value | That the source says what the claim says. The registry records who checked it, when, and how; a reviewer re-checks a sample |
| Two files that cite one claim cannot state it differently, and watched subjects (such as who designed *Rocket*) are flagged wherever they appear | That every factual claim was detected. Detection keys on years, centuries, BC and CE dates, death counts, and first-of phrasing; a bare name or mechanism slips through |
| Links and heading anchors resolve; types, templates, prerequisites, answer blocks, dashes, and process notes follow the rules | That an external link still loads. Link liveness needs the network and is checked by reviewers, not by the build |
| Each dated claim carries its year, its source, and a review date, and stale claims are listed | That a dated practice is still current. Stale means a person must look |

The design rule follows from this table: make every check that can be deterministic deterministic, record the human or agent judgment that remains, and never let one stand in for the other.

## Severity

- **Gate.** Fails the build in any file: broken links and anchors, missing or unknown `**Type:**`, em or en dashes, prerequisite cycles, any failing verify block, any `expect` whose number is not printed where it claims, any citation to an unknown claim, and any registry error in `data/`.
- **Content.** Fails the build in strict files and is counted as debt elsewhere: template sections, the definition-first rule, answers outside a `<details>` block, process notes, unverified worked examples or answers, uncovered printed numbers, constant mismatches, Earth values without "Earth" or "standard", uncited dated claims, cited values not stated, `as of` without a dated claim, watch conflicts, and reference entries that break the contract below.
- **Advice.** Never fails: stale dated claims and sources without an archive snapshot.

A file opts into the content rules with a line under its type line:

```
**Type:** lesson
**Verify:** strict
```

Migration moves files to strict one at a time. The coverage report shows how far it has gone.

## Verify blocks

A verify block is a fenced code block with the language `verify`, placed in the section whose numbers it checks. In a lesson, put the worked example's block in a `<details><summary>Verification</summary>` block after the sanity check, and put the practice block inside the answers `<details>` block after the last answer. In a reference sheet, put one block after the `Breaks when` line of each section that has an example.

The block uses Python syntax but runs in a closed evaluator, never in Python itself. Only these forms are allowed:

- `name = expression` with numbers, `+ - * / **`, parentheses, comparisons, `and`, `or`.
- Functions: `sqrt cbrt exp log log10 sin cos tan asin acos atan atan2 abs min max`, and `rnd(x, digits, "unit")` to round a value as printed in a unit. `pi` is defined.
- `q(value, "unit")` declares an input. `q(9.81, "m/s^2", of="g_standard")` declares a rounded canonical value; the verifier checks the rounding against the table. Add `rel=0.001` to allow a stated relative tolerance. An input within 2 percent of any canonical value with the same dimension must say `of=` (or `of="none"` when it is a different quantity), so a rounded constant cannot hide.
- `const("key")` gives the full canonical value. `u("kPa")` gives one unit.
- `expect(expression, "12.2 kPa")` checks a printed result. Add `ans=3` when it checks practice answer 3, and `rel=` when chained rounding needs it.
- `check(condition, "message")` asserts a sanity condition.
- `given("0.5", "100")` declares printed numbers that are definitions or inputs written only in prose, such as a factor or a range label. Reviewers treat every `given` as a claim to inspect.
- `skip(ans=3, why="short answer")` marks a practice answer whose digits are not a calculation.

Anything else (imports, attributes, loops, function definitions) fails the block. This keeps CI safe on pull requests from anyone.

Units come from [data/units.md](data/units.md): a unit string is `numerator tokens / denominator tokens`, with `^` powers and SI prefixes, such as `kg/m^3`, `N s/m`, `m^3/kg s^2`, `cm^3/rev`. Angles are dimensionless, so `rev` and `deg` carry their factor of $2 \pi$ or $\pi/180$. Temperatures are in kelvin; write Celsius values as differences from `const("t_celsius_zero")`.

### How a printed value is matched

1. The printed text `"12.2 kPa"` sets the tolerance: half a unit in the last printed digit (0.05 kPa here), or `rel` times the value if larger.
2. The computed quantity must have the dimension of `kPa` and lie within the tolerance.
3. The digits `12.2` must appear in the section (or in answer 3 when `ans=3`). The match reads numbers the way a reader sees them: exponents, subscripts, and link targets are dropped, `1.216 \times 10^4` reads as 1.216, and `101 325` reads as 101325.
4. Every printed number of 10 or more, and every decimal, in a strict worked example, answer, or reference example line must be an input, a checked result, or a `given`. Single-digit integers are skipped, since they are mostly step numbers, exponents, and small counts.

## Canonical data

One fact, one place. Lessons round values freely, and the verifier checks each rounding against the table.

- [data/constants.md](data/constants.md): physical constants and Earth conventions, with source and locator, plus the prose scans.
- [data/properties.md](data/properties.md): material and fluid properties with conditions. A row with a `Range` is a typical value; any rounded value inside the range passes.
- [data/units.md](data/units.md): unit definitions, each built from the SI base units, which rest on fixed constants of nature.
- [data/sources.md](data/sources.md): every source, with publisher, edition, URL, archive snapshot, and independence group.

The scans table in `constants.md` lists regular expressions that find a constant stated in prose anywhere in the repo, with an optional `Context` that must also match and an `Unless` that skips the line. `Planet: yes` means the line must also say Earth or standard, so no Earth value is stated as if it held everywhere. To catch a new constant in prose, add a scan row. Planet context is checked per line, so a second Earth value on a line that already says Earth is not flagged.

## Claims

A claim is a specific fact that is not derived from physics: a date, a name, an attribution, a first-of statement, a count, a standard's number, a price, a company practice. Claims live in [data/claims/](data/claims/README.md), one heading per claim:

```
### rocket-rainhill-1829
- Claim: The locomotive Rocket won the trials held at Rainhill in 1829.
- Values: 1829; Rainhill
- Layer: durable
- Status: verified-2
- Sources: smg-collection (object co26704, "..."); eb1911 (article "Stephenson, George", "...")
- Checked: agent:opus, 2026-10-18, fetched both pages and matched the quoted words
```

Cite a claim by linking to its heading, before the sentence's final period: `won at Rainhill in 1829 [src](../data/claims/history.md#rocket-rainhill-1829).` In a table, put the links in a `Source` column.

Rules the verifier enforces:

- **Grounding.** Every claim names at least one registered source with a locator in parentheses. A claim with no checkable public source is refused, and the content is left out of the repo.
- **Values.** The citing sentence or table row must state every value, ignoring case and link targets. `~1705` also needs an approximation word (about, around, circa, approximately, roughly). `1705..1712` needs both ends.
- **Status.** `unverified` (registered, not yet checked against the source), `verified-1` (one source checked), `verified-2` (sources from two different `Group` values checked), or `disputed` (sources disagree; a `Dispute:` line gives the competing values, and the prose must say what the sources support). Every status above unverified needs `Checked:` with who or what checked it, the date, and the method. Strict files may not cite unverified claims.
- **Layer.** `durable` for facts and methods that hold for decades, `dated` for anything that ages. A dated claim needs `As of: YYYY` and `Review by: YYYY-MM-DD`. Any `as of YEAR` in a strict file must cite a dated claim with that year. The runner lists dated claims past their review date as stale, a warning that never fails the build. Timeless content (physics, mathematics, principles) is derived, not registered.
- **Watch.** `Watch:` (a regular expression) and `Require:` (text) flag every line in the repo that mentions a contested subject without the registered answer.
- **Detection.** In strict history lessons (all sections except key equations, worked examples, practice, and go deeper) and in `## History` sections of strict lessons, every sentence or table row with a year, a century, a BC or CE date, a death count, or "the first" must cite a claim.

## Reference entries

A reference sheet is where an engineer looks up a formula in the middle of a job, so every formula there carries what is needed to use it safely. An **entry** is the text under one heading, up to the next heading of any level. Every entry in a `**Type:** reference` file that holds display math (`$$...$$`) must also hold, in that same entry:

1. A line starting `Variables:`, followed by either a table with an `SI unit` column and one row per symbol, or a bullet list whose items end with the unit in brackets, as `- $F$: spring force [N]`.
2. A line starting `Holds when:` with the assumptions, geometry, material behavior, and regime the formula needs.
3. A line starting `Breaks when:` with the first ways it fails.
4. A line starting `Source and basis:` with a link to a derivation (a lesson or a registered source) or to a registered claim, or the words "derived from" and the principle it comes from. Empirical, attributed, and dated material cites a claim.

```
$$\sigma = \frac{P}{A}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\sigma$ | axial normal stress | Pa |
| $P$ | axial force | N |
| $A$ | cross-section area | m$^{2}$ |

Holds when: the load acts through the centroid of a uniform bar.
Breaks when: holes or fillets raise the local stress.
Source and basis: derived from equilibrium of a cut bar; taught in [Axial and torsion](physics/04-axial-and-torsion.md).
```

Each unit must be `dimensionless`, `1`, or a unit in [data/units.md](data/units.md) whose factor to the SI base units is a power of ten, so `kN m`, `mm`, `m$^{4}$`, and `rad/s` pass and `psi`, `deg`, `h`, and `rpm` fail. LaTeX unit markup (`$\text{N m}$`, `m$^{4}$`) is read as written. Equations use radians; degrees appear only as printed inputs or results with their conversion.

The check proves that each field is present and each unit is SI. It cannot prove that the table names every symbol, that the limits are the right ones, or that the basis supports the formula; the reviewer of every reference sheet checks those, per [AGENTS.md](AGENTS.md#migration-waves). Symbols follow [data/notation.md](data/notation.md). Entry findings are content findings: they fail strict sheets and count as debt in sheets not yet migrated.

## Structure checks

- Relative links and heading anchors resolve.
- Every content file has `**Type:**` with one of lesson, reference, philosophy, data, or track. Root files listed in the runner are exempt.
- Lessons have the sections of their template, the prerequisite and time lines, practice answers inside `<details>`, and a first sentence that says what the topic is.
- Prerequisite links form no cycle.
- Folder READMEs link every file in their folder.
- No em or en dashes anywhere, and no process notes ("this session", "computed with Python", TODO) in content.

## Coverage report

Every run ends with counts: strict files, fully verified worked examples, verified numeric answers, printed numbers covered, verify blocks and expects, complete reference entries, cited dated claims in history scopes, claims by status, sources without an archive snapshot, constant scan hits and mismatches, stale claims, and debt by check in files not yet migrated. Coverage never fails the build; it tells the next wave where to go.

## Changing the verifier

The verifier is shared infrastructure. Only the architect role changes it, in its own pull request. Each change states the check, the class of error it catches, and a mutation test: break a pilot file in the way the check targets, run the verifier, and show it fails; then restore the file. A check that never fails on a deliberate error is removed.

Each check also gets fixtures in `tests/fixtures/`, at least one that passes and one that fails, and unit tests in `tests/` that run them. Run them with `python -m unittest discover -s tests`; CI runs them before the verifier. The repo-wide run skips `tests/`, because failing fixtures are broken on purpose.
