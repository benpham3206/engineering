# AGENTS.md

The rules for working on this repo, for every agent and every person. This file is the single source of truth; [CLAUDE.md](CLAUDE.md) only points here. Where this file and another doc disagree, this file wins and the other doc gets fixed.

## Purpose and the reliability bar

This repo is a free engineering reference that takes a person with no math or engineering background to a working engineer, and a working engineer to the frontier: the teams that build rockets, cars, and machines far faster and cheaper than precedent. [LEVELS.md](LEVELS.md) defines the ladder from level 0 to level 5.

It must stay right for centuries, for readers on Earth and off it, for beginners and senior engineers. Thousands of agents and people will extend it over decades, and most of its text was first written by AI agents. Reliability is the whole point. A missing fact costs a reader a lookup; a wrong fact can cost a part, a vehicle, or a life.

The bar:

- Every number in an example or answer is recomputed by machine. Every dated or attributed fact traces to a public source. The verifier enforces both.
- State every assumption a result depends on: which planet's gravity, which atmosphere, which temperature, which material condition. Write the general form first (for example $W = m g$ with $g$ for the local body) and give Earth values as one case, labelled Earth or standard.
- Define units and constants from physics, not from institutions that may not last. The SI rests on seven fixed constants of nature; [data/units.md](data/units.md) builds every unit from them, so a reader with no surviving standards body can rebuild every unit.
- First principles over products, brands, and software versions.
- Leave it out rather than guess. A missing entry is far better than a wrong one.

## Accuracy rules

1. **No invented content.** Every claim that is not timeless (not derived from physics, mathematics, or a stated principle) traces to a real, public, checkable source registered in [data/sources.md](data/sources.md) with an exact locator. If no source can be found, the content is left out. The claims registry refuses a claim with no source.
2. **Compute, never guess.** Every number in a worked example and every practice answer carries a verify block that recomputes it. Run the arithmetic; never write a number you did not compute.
3. **One fact, one place.** Constants live in [data/constants.md](data/constants.md), properties in [data/properties.md](data/properties.md), claims in [data/claims/](data/claims/README.md). Lessons round and cite them; they never restate a different value.
4. **Typical values are labelled typical**, with the range they vary over.
5. **Where sources disagree, say so.** Register the claim as disputed, give the competing values, and write only what the sources support.
6. **Read the source before you cite it.** Fetch it, find the words that support the claim, and record the locator and the quoted words in the claim. A claim you have not checked is `unverified`, and strict files cannot cite it.

## How content ages

Content ages at three speeds, defined in [LEVELS.md](LEVELS.md#how-the-content-ages). Principles stay fixed; practices adapt.

| Layer | Examples | Rule |
|---|---|---|
| Timeless | Physics, mathematics, conservation laws, failure mechanisms, principles of judgment | No dates. Derived from first principles, so it holds anywhere and in any century |
| Durable | Methods that have held for decades: fatigue design, tolerancing, test practice; historical facts | Cited to a registered source (claim layer `durable`) |
| Dated | Tools, software, standard editions, company practices, prices, links, case studies | Written "as of YEAR", cited to a claim with layer `dated`, `As of`, and `Review by`. The verifier lists stale claims |

When a dated practice changes, update the claim and the text, and check that the timeless principle it served still explains why.

## Repo map

| Path | What it holds |
|---|---|
| [README.md](README.md) | Front door: what this is, how to start, the folder table |
| [LEVELS.md](LEVELS.md) | The level 0 to 5 ladder, exit tests, and the time layers |
| [ROADMAP.md](ROADMAP.md) | The general learning track |
| [FORMULAS.md](FORMULAS.md) | The formula spine: routes by level and the one owner sheet of each formula family |
| [tracks/](tracks/) | School-specific tracks over the same lessons |
| [courses](courses) | The owner's course sequence, the input to the SJSU track |
| `math/`, `physics/`, `materials/`, `design/`, `manufacturing/`, `measurement/` | Fundamentals |
| `communication/`, `philosophy/`, `problem-solving/` | How engineers think, decide, and explain |
| `applications/<domain>/` | How engineered things work, in 12 domains |
| `history/`, `history/people/`, `history/projects/` | Eras, people, and great projects |
| `reverse-engineering/`, `tools/` | Taking things apart; the tools of the trade |
| [data/](data/README.md) | Canonical units, notation, constants, properties, sources, and claims |
| [verify.py](verify.py), [VERIFICATION.md](VERIFICATION.md), `tests/` | The verifier, its specification, and its tests and fixtures |

### Two learning tracks, one set of lessons

- The **general track** is [ROADMAP.md](ROADMAP.md): what engineers everywhere learn, in degree order, with no school attached.
- The **SJSU mechanical engineering track** is [tracks/sjsu-mechanical-engineering.md](tracks/sjsu-mechanical-engineering.md). It follows the owner's actual course sequence in [courses](courses) and maps each course to the shared lessons.

Lessons are shared and track-neutral. Course codes, semesters, and school-specific sequencing live only in track files, never in lessons or folder READMEs. A new track is a new file in `tracks/` with `**Type:** track`.

### File types

Every content file starts with a `**Type:**` line under its title.

- **lesson.** Numbered `NN-kebab-name.md` files that teach one topic from scratch.
- **reference.** `reference*.md` sheets: dense lookup for working engineers.
- **philosophy.** Principles behind good engineering.
- **data.** Canonical tables in `data/`, read by the verifier.
- **track.** A path through the lessons for one program.

Folder READMEs are maps, not lessons, and carry no type line.

## Templates

### Define before you explain

Every lesson's first sentence says what the topic is and why an engineer cares, before anything about what it does or how it works. The units lesson first says what a unit is. Every new concept inside a lesson gets the same treatment: one line of definition, then the explanation. The verifier checks the first sentence (it must say what something is); reviewers check every concept after it.

### Lesson

```
# <Topic>

**Type:** lesson
**Verify:** strict

<What it is, in one sentence. Why an engineer cares, in one or two more.>

**Prerequisites:** <relative links to earlier lessons, including the math it uses, or "none">
**Time:** <rough hours, for example 6-8 h>

## Core ideas
<Plain explanation. Short paragraphs and bullets. Define every term the first time.>

## Key equations
<GitHub math only: $inline$ and $$display$$. Name every symbol with SI units.>

## Worked example
<Given, find, assumptions, solution, answer with units, sanity check.>
<details><summary>Verification</summary> verify block </details>

## Practice
<3 to 5 problems, easiest first. At least one that needs a choice of method, not just new numbers.>
<details><summary>Answers</summary> answers, then the verify block </details>

## Common mistakes
<3 to 5 bullets.>

## Go deeper
<2 to 5 free public sources, then related lessons.>
```

A non-quantitative lesson may replace Key equations and Worked example with Checklist and Example.

### Device lesson (`applications/<domain>/`)

The lesson template, with Core ideas split into `### How it works`, `### Main parts`, and `### Variants`, and three more sections after the worked example: `## Design trade-offs` (what designers balance, with numbers), `## How it fails` (failure modes, causes, warning signs, and the safety measures that exist because of them), and `## History` (3 to 6 sentences; every dated or first-of sentence cites a claim).

### History lesson (`history/`)

```
# <Era or topic>
**Type:** lesson
<What changed in this era and why it matters to engineers now.>
**Prerequisites:** / **Time:**
## Core ideas          the story in order: the problem, what people built, how it worked
## Key inventions      table: Year | Invention | Who and where | Why it mattered | Source
## Key equations       the physics behind one or two inventions
## Worked example      a calculation tied to a real invention
## Lessons for engineers today
## Practice            calculation and short answer, answers in details
## Common mistakes     myths, corrected, with citations
## Go deeper
```

Every sentence or table row with a year, century, date, death count, or first-of claim cites a registered claim.

### Reference sheet (`reference*.md`)

```
# <Folder> reference
**Type:** reference
**Verify:** strict
<One sentence: what this covers and who it is for.>
## Principles          5 to 10 truths of the field that never expire
## <Topic sections>    in lesson order. Each heading that holds a display equation
                       is one formula entry (below); typical values in tables
                       labelled typical; rules of thumb with basis and limit;
                       a verify block for every example
## Checklists          what a practitioner runs before trusting a result
## Sanity checks       orders of magnitude and quick tests
## Further reference   classic books and standards by name; free ones with a URL
```

A formula entry is the text under one heading, up to the next heading. It holds, in this order:

```
<What the formula gives, in one sentence.>
$$<the equation>$$
Variables:
| Symbol | Meaning | SI unit |      one row per symbol; unit is SI (prefixes allowed) or "dimensionless"
Holds when: <assumptions, geometry, material behavior, regime>
Breaks when: <the first ways it fails, and what to use instead>
Source and basis: <link to the derivation or a registered claim, or "derived from" the principle>
<example lines, then the verify block>
```

The verifier enforces the four labelled fields and the SI units in strict sheets ([VERIFICATION.md](VERIFICATION.md#reference-entries)). Use the symbols in [data/notation.md](data/notation.md) in new entries. Physical constants and reusable properties live in `data/`, never inside an entry; an empirical coefficient lives with its one correlation. [FORMULAS.md](FORMULAS.md) names the one sheet that owns each formula family; check it before adding a formula, and link the owner rather than restating it.

The sheet goes further than the lessons. Where a handbook table cannot be reproduced, give its generating formula (for example the ISO 286 tolerance unit, the thread tensile-area formula, or a saturation-pressure correlation), with its source and range of validity.

### Philosophy

`**Type:** philosophy`, a first sentence that says what the principle is, the principle stated in full in this repo (never only at a link), concrete engineering examples, Practice with answers in details, Common mistakes, and Go deeper.

## Writing rules

- Your own words. Never copy text or tables from any source.
- Plain words, short sentences, active voice where the actor matters, one idea per sentence. Standard technical passive ("is measured in", "is defined as") is fine.
- Sentence-case headings. `-` for bullets. No em or en dashes. No curly quotes. No emoji.
- All math in `$...$` or `$$...$$`. No bare carets, `sqrt(`, or raw Greek and math symbols in prose; the verifier flags them.
- No filler: no "In this lesson we will", "It is important to note", "In summary". Delete any sentence that restates the heading or the sentence before it.
- No AI vocabulary when a concrete word works: not crucial, delve, robust, comprehensive, seamless, leverage, utilize, ensure, landscape.
- No bold-label lists (`- **Label:** text` where the label names what the text says). Bold only defined terms.

### Formatting

Formatting is a reading aid, not decoration. Use each device for one job, consistently:

- **Bold** a technical term once, where it is defined, with its abbreviation if it has one: "**Ideal mechanical advantage (IMA)** is the force ratio a frictionless machine would give." Do not bold it again, and never bold whole sentences for emphasis.
- *Italics* for titles of books, papers, and reports, for the names of individual ships, locomotives, aircraft, and spacecraft (*Rocket*, *Friendship 7*, *Columbia*), and for a word used as a word. Model and type names stay upright (Model T, Saturn V, SR-71, ENIAC). Variables go in math, never in italics.
- History lessons carry no hazard alerts. They describe past events, not hazards to the reader.
- Alerts sit at the top level of the document, never indented inside a list item, where they do not render.
- `Code` for file names, commands, function names, and literal input.
- Numbered lists for steps that happen in order. Bullets for unordered items. A table when three or more items are compared on two or more attributes.
- Math in `$...$`. Units upright with `\text{}`: $9.81\ \text{m/s}^2$.
- A GitHub alert for the few things a reader must not miss. Use `> [!WARNING]` for a hazard to people or equipment, and `> [!NOTE]` for a limit of validity that changes the answer. At most two per lesson.
- Short paragraphs, three to five sentences. One idea per paragraph.
- Link text names the target ("see [Statics](physics/01-statics.md)"), never "click here".
- No colons as mid-sentence connectors. No vague sources ("experts say", "studies show").
- Name a mechanism or a number, never a feeling.
- No notes about your own process ("computed with Python", "fetched this session", TODO). The reader sees only the engineering.
- SI units first, US customary in parentheses where still common.
- Never credit any person as an author of repo content.

## Link rules

- External links only to free, public, well-known sources a reader can open with no paywall, login, or trial: OpenStax, MIT OpenCourseWare, LibreTexts, Khan Academy, NASA, NIST, BIPM, Project Gutenberg, Wikisource, the Smithsonian, the Science Museum Group, the Library of Congress, government agencies, and university pages. No blogs, SEO tutorial sites, or paid textbooks; name a paid book or standard by title with no link.
- Include a URL only after you fetched it and it loaded the expected free content.
- Every source a claim rests on goes in [data/sources.md](data/sources.md) with an independence group and, when you can record one, an archive snapshot.
- Internal links are relative paths and must resolve, anchors included.

## Verification

The full specification is [VERIFICATION.md](VERIFICATION.md). The command, from the repo root:

```
python verify.py
```

Nothing merges unless it passes. CI runs the same command on every pull request and requires every added markdown file to be strict.

- **Mark a file strict** with `**Verify:** strict` under its type line once it meets every rule. Strict files fail the build on any content finding; other files report it as debt.
- **Add a verify block** after each worked example, inside each answers block, and after each reference example. Declare inputs with `q(value, "unit")`, round canonical values with `of="key"`, and check every printed result with `expect(expr, "printed value unit")`, adding `ans=N` for answer N. Every printed number of 10 or more and every decimal in those places must be an input or a checked result.
- **Write reference entries to the contract.** Every display equation in a reference sheet sits in an entry with `Variables:` (SI units), `Holds when:`, `Breaks when:`, and `Source and basis:` lines, as in the reference template above.
- **Test verifier changes.** `python -m unittest discover -s tests` runs the verifier's own tests and fixtures; CI runs them too.
- **Use canonical data.** If a value is a constant or property, add or find its row in `data/` and declare it with `of=`. Never type a new value for a fact the table holds.
- **Cite claims.** Register the claim in `data/claims/<area>.md` with its values, layer, status, sources with locators, and who checked it. Link to it before the sentence's final period: `[src](../data/claims/history.md#key)`.
- **Read the report.** The coverage section shows what is migrated and the debt by check.

## How work is done

The method is the one in [The engineering method](philosophy/08-the-engineering-method.md), applied to this repo.

- **Gate.** Is the change low consequence, low uncertainty, and easy to reverse, all three? A typo fix or a link fix is: build, verify, done. A new lesson, a changed value, a verifier change, or anything a reader may rely on is not: plan first.
- **Plan.** State the intent, the definition of done, how it will be measured (usually the verifier plus a review), the constraints, the assumptions, and what could go wrong if the content is wrong.
- **Build.** Question each requirement. Delete what does not need to exist. Use the existing lesson, table, or claim before writing a new one. Make the smallest change that meets the definition of done.
- **Verify.** Run `python verify.py`. Check every surface the change reaches: the lesson, its folder README, the root README and catalogs, the prerequisite lines that point to it, the track files, and the data rows it uses.
- **Refine.** When a check or a review finds an error, find the root cause, fix the class of error, and turn it into a check or a rule here when it can recur.
- **Complete** means the content exists, the verifier passes, a review found no material issue, and the repo still describes reality.

Judge work by verified outcome, not activity. Lines written, files created, and sources read are not progress by themselves. Deleting a wrong paragraph is progress.

## Roles and routing by model capability

Capability decides what work a model gets; it never grants more authority. Anything not granted in a packet is denied.

| Tier | Models | Suited to |
|---|---|---|
| Small and fast | Haiku | Mechanical sweeps with an exact rule: adding verify blocks to arithmetic already in prose, adding `[src]` links to registered claims, the Earth-gravity wording fix, link and anchor fixes, README link lists, template headings. Runs the verifier after each file |
| Mid | Sonnet | One lesson or one reference section written or rewritten; a bounded fix from a review; registering claims after fetching their sources; adding canonical data rows with sources |
| Large | Opus, Fable | Architecture, new domains and folders, verifier changes, reviews, disputed claims, the coverage map and backlog, final judgment on anything a reader may rely on |

Roles:

- **Architect** (large tier). Owns the structure, this file, the verifier, and the data schema. Splits work into packets, routes them, and integrates the results. Does not absorb worker tasks.
- **Worker** (any tier). Owns one packet. Makes the smallest correct change inside its file scope. Does not change the verifier, the data schema, or this file, and does not widen its scope. If the task cannot be done inside the boundary, stops and reports why.
- **Reviewer** (a different model from the author). Returns material findings only: wrong physics, wrong or unsupported facts, unrealistic assumptions, missing definitions, scope creep. Does not edit. A clean review is a valid result.
- **Researcher.** Answers one question with sources and stated uncertainty, and proposes; the architect reviews, and the owner decides.

### Packet format

Every packet states:

```
Objective:        what must be true when done
File scope:       the exact files the worker may write
Non-goals:        what not to touch or change
Acceptance check: the command and the result that proves done (usually python verify.py
                  passing, the file strict, and named numbers checked)
Return format:    what to report, and its length
```

A failed packet is reported as component, root cause, and failure type, so the next packet fixes the cause.

## Coordination

- **One writer per file.** Two agents never write the same file at once. Packets that touch the same file run in sequence.
- **Claim before you write.** Before writing, open a draft pull request (or an issue) whose description lists every file you will write. Check open pull requests first (`gh pr list`); a file already listed is taken.
- **Hand off in the pull request.** State what is done, what remains, the verifier's coverage lines before and after, and any fact you left out and why.
- **Review by an independent model.** A model other than the author reviews every content change. The reviewer re-derives a sample of the numbers by hand, re-reads the source behind a sample of the claims, and checks the physics of each verify block. The author fixes; the reviewer re-checks; the architect decides on disputes.
- **Data files are shared.** Add rows to `data/` in the same pull request as the content that uses them. Never change an existing row's value without checking every file that rounds it; the verifier lists them.

## Adding content

### A lesson

1. Check the folder README and open pull requests; the topic may exist or be claimed.
2. Write the file at `<folder>/NN-kebab-name.md` from its template, with `**Verify:** strict`.
3. Add its verify blocks, data rows, and claims. Run `python verify.py` until it passes.
4. Link it from the folder README in study order, from the parent catalog (`applications/README.md` for a device lesson), and from the prerequisite lines of the lessons that build on it.
5. Map it into each track that covers it.

### A domain or folder

1. The architect decides, with the coverage map below.
2. Create the folder with a README: title, one-line purpose, a prerequisite line, `## Lessons` in study order, `## Reference`, and see-also links. No course codes.
3. Add the folder to the root README table and to the levels it serves in [LEVELS.md](LEVELS.md) (owner approval needed for LEVELS.md).

### A reference sheet

Write `reference.md` (or `reference-<topic>.md` when a folder needs more than one) from its template, read every lesson in the folder first, and link it from the folder README and the root README table.

## Coverage map and backlog

What exists (lessons, then reference sheets): math 9 and 1, physics 15 and 3, materials 8 and 1, design 11 and 1, manufacturing 9 and 1, measurement 10 and 1, communication 7 and 1, philosophy 9 and 1, problem-solving 8 and 1, reverse-engineering 6 and 1, tools 12 and 1, history 21 and 3, applications 86 lessons over 12 domains and 1 sheet. Levels 1 and 2 are mostly covered; levels 0, 3, 4, and 5 are mostly not.

Backlog in priority order, keyed to [LEVELS.md](LEVELS.md). Each item is a folder or lesson set unless marked.

| Priority | Item | Level | Why |
|---|---|---|---|
| P0 | Migrate existing content to strict, in waves (below) | all | Reliability is the point; today almost nothing is machine-checked |
| P0 | Fix the known errors from review (column limit, Tresca wording, corroded-wall check, cosine error, weld size, aluminium creep, Stephenson attributions, integration signs) | 2, 3 | Wrong statements that can fail a part |
| P0 | Remove course codes from folder READMEs into the tracks | all | Track rule |
| P1 | Foundations: arithmetic, fractions, powers of ten, units, reading a formula and a graph, estimation | 0 | No entry point for a reader with no background |
| P1 | Controls design: stability, Routh, root locus, Bode and margins, tuning rules, discrete-time control | 3 | The largest analysis gap for mechatronics and aerospace |
| P1 | Systems engineering and reliability: requirements, interfaces, failure rates, Weibull, redundancy, FMEA, fault trees, maintainability | 3, 4 | No reliability statistics anywhere |
| P1 | Chemistry: stoichiometry, enthalpy of formation, combustion and flame temperature, equilibrium, electrochemistry and Nernst | 2 | Engines, rockets, batteries, corrosion, and life support rest on it |
| P1 | Statics depth: trusses, frames, centroids, distributed loads, shear and moment diagrams | 1, 2 | The lesson does not teach what the folder promises |
| P2 | Generating formulas for standard tables: ISO 286 fits, thread pitch and tensile area, bolt grades, stress concentration fits, water and steam saturation, ISA atmosphere, wire ampacity | 3 | Removes dependence on handbooks and software |
| P2 | Quantum and solid-state: photons, energy levels, band theory, doping, how a wafer is made | 2 | The semiconductor chain cannot be rebuilt without it |
| P2 | Electrical power: three-phase, per-unit, fault current, protection, conductor sizing; power electronics: converters, switching devices, magnetics, thermal design | 2, 3 | Lives only in lessons, with no reference sheet |
| P2 | Simulation verification and validation: FEA and CFD practice, mesh convergence, validation against test | 3 | Level 3 exit test needs it |
| P2 | Battery packs: cells to packs, thermal runaway, management systems | 3 | Electric vehicles and storage |
| P3 | Frontier engineering: first-principles cost and limit analysis, requirement deletion, rapid hardware iteration, test to failure, manufacturing at scale, cited case studies | 5 | Level 5 has no lessons |
| P3 | Space and isolated systems: life support, radiation dose and shielding, vacuum and cryogenics, thermal vacuum, re-entry heating, orbital operations beyond Hohmann, in-situ resources, repair far from supply | beyond 5 | The off-Earth reader |
| P3 | Metrology from constants: realizing the kilogram, kelvin, ampere, and second from the defining constants | beyond 5 | Rebuilding units with no surviving standards body |
| P3 | Fatigue and fracture depth: notch sensitivity, Miner's rule, weld fatigue classes; plates, shells, and Lamé thick-wall stresses | 3 | Common desk lookups not answered |
| P4 | Geotechnics and tunneling; microfabrication; computing infrastructure (data centers, networks, power and cooling); signal processing; acoustics; chemical process engineering; water and wastewater; mining and mineral processing; human factors; tribology; composites; engineering economics and cost estimation | 3 to 5 | Fields of engineering not yet present |

### Migration waves

| Wave | Scope | Tier | Acceptance |
|---|---|---|---|
| 1 | Physics and math lessons: verify blocks for worked examples and answers, Earth wording, definition-first sentence | Small model per file, mid model for files with judgment calls, large-model review | Each file strict; verifier passes |
| 2 | Applications device lessons by domain, and their History sections with claims | Mid model per domain; claims fetched and checked | Each file strict |
| 3 | Reference sheets, one section at a time | Mid model; large-model review of every Holds when and Breaks when | Each sheet strict |
| 4 | History lessons, people, and projects: register and check every claim, two sources where possible | Mid model; large model for disputed claims | Each file strict; no unverified citation |
| 5 | Dated content: every "as of" gets a dated claim and a review date; archive snapshots for every source | Small model with a fetched-source rule | No dated debt; no archive pending |

## Git rules

- Work on a branch. Open a pull request. Never push to `main` without the owner's yes.
- One coherent change per commit, verified before it is committed.
- No AI attribution anywhere: no `Co-Authored-By` lines, no "Generated with" footers, no model names in commit messages or pull request text.
- Never credit any person as an author in content.
- Never commit secrets, binaries without a documented purpose, or generated files that the verifier could produce.
