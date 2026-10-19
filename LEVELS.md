# Levels

**Type:** reference

This repo takes a person from no math or engineering background to a working engineer, and a working engineer to the level of the teams that build rockets, cars, and machines faster and cheaper than anyone thought possible. The ladder below says what each level can do, what proves it, and where to study.

A level is defined by what you can do without help, not by what you have read. Each level ends with an exit test: a build and an exam you can check yourself, with answers.

## How the content ages

Engineering knowledge ages at three speeds, and the repo keeps them apart.

| Layer | What it holds | How it is written |
|---|---|---|
| Timeless | Physics, mathematics, conservation laws, failure mechanisms, principles of judgment and ethics | No dates. Stated from first principles, so it holds anywhere and in any century. |
| Durable | Methods that have held for decades: fatigue design, tolerancing, design for manufacture, test practice | Cited to a source. Reviewed rarely. |
| Dated | Tools, software, standard editions, company practices, prices, links, case studies | Marked "as of" a year, cited, and given a review date. Updated as the world changes. |

Principles stay fixed. Practices adapt. When a practice changes, the principle it served should still explain why.

## The ladder

### Level 0: start here

For anyone, with no background assumed.

- Can do: arithmetic with fractions, ratios, percentages, powers of ten, and units; read a formula and a graph; estimate a quantity to within a factor of ten; use hand tools safely; follow a procedure and record what happened.
- Study: the foundations folder (planned), then [Algebra](math/01-algebra.md), [Units and dimensional analysis](measurement/01-units-and-dimensional-analysis.md), [Estimation](problem-solving/07-estimation.md), [Shop safety](manufacturing/01-shop-safety.md), and [Starter kit](tools/01-starter-kit.md).
- Exit test: build a simple machine from scrap (a lever, pulley, or ramp), predict its mechanical advantage, measure it, and explain the difference in writing.

### Level 1: maker

Builds working things and understands why they work.

- Can do: algebra and trigonometry; free-body diagrams; basic circuits; read and make a dimensioned drawing; measure to 0.02 mm; make parts on a drill press, mill, lathe, or 3D printer; write a one-page test report.
- Study: [Trigonometry](math/02-trigonometry.md), [Statics](physics/01-statics.md), [Circuit basics](applications/electronics/01-circuit-basics.md), [Engineering graphics](design/02-engineering-graphics.md), [Reading calipers and micrometers](measurement/04-reading-calipers-and-micrometers.md), the [manufacturing](manufacturing/README.md) lessons, and [Technical writing](communication/01-technical-writing.md).
- Exit test: design, draw, make, and test a bracket that carries a stated load with a stated deflection limit. Predict both, then measure both.

### Level 2: engineer

The level of a graduate of a four-year engineering degree.

- Can do: calculus through differential equations; the full mechanics, thermal-fluid, materials, and electrical fundamentals; model a system, choose assumptions, solve it, and check the answer three ways; design a part for strength, stiffness, fatigue, and manufacture; plan an experiment with stated uncertainty.
- Study: everything in [math](math/README.md), [physics](physics/README.md), [materials](materials/README.md), [design](design/README.md), [measurement](measurement/README.md), and [problem-solving](problem-solving/README.md), in the order of the [roadmap](ROADMAP.md).
- Exit test: a capstone. Take a real need from requirements to a tested prototype, with a design report that another engineer could check line by line.

### Level 3: practicing engineer

Trusted to own a component in a product that ships.

- Can do: look up and apply design data, codes, and standards correctly; design to a reliability target; tune and verify a control loop; verify and validate a simulation against test; design for production volumes; review someone else's analysis and find the error.
- Study: the reference sheets in every folder, the [applications](applications/README.md) lessons for your domain, and the planned controls, reliability, and simulation lessons.
- Exit test: a component that passes a design review, a qualification test, and a first production run, with every number in the review traceable to a source or a test.

### Level 4: lead engineer

Owns a subsystem or a product across disciplines.

- Can do: write and defend requirements; split a system into interfaces and own the interfaces; make cost, schedule, and risk trade-offs with numbers; run design reviews and failure investigations; lead people through a hard problem.
- Study: the planned systems engineering lessons, [The engineering method](philosophy/08-the-engineering-method.md), [A way of working](philosophy/09-a-way-of-working.md), [Working on teams](communication/06-working-on-teams.md), [Safety and risk](philosophy/03-safety-and-risk.md), and the failure cases in [philosophy](philosophy/reference.md).
- Exit test: lead a multi-discipline project to a working system, with a requirements trace, a risk register, and a failure investigation report for at least one real failure.

### Level 5: frontier engineer

The level of the small teams that do what the industry said was impossible, at a fraction of the expected cost and time.

- Can do: reason from physical limits rather than from precedent, and find how far a design sits from the limit; treat every requirement as a hypothesis with an owner; delete parts and steps before optimizing them; build, test, break, and learn in short loops; design the factory along with the product; work across mechanical, electrical, software, and manufacturing without handing off understanding; take responsibility for the outcome, not the task.
- Study: the planned frontier engineering lessons (first-principles cost and limit analysis, requirement deletion, rapid hardware iteration, test to failure, manufacturing at scale, and public case studies), the history of the [great projects](history/projects/README.md), and the [principles that last](philosophy/07-principles-that-last.md).
- Exit test: take a product or process that already exists and make it cheaper, lighter, or faster by a large factor. Show the physics limit, the old design's distance from it, what you deleted, the test campaign, and the measured result.

## Beyond level 5

The repo is also written for engineers far from any supply chain: on ships, on other planets, or centuries from now. Every assumption about gravity, atmosphere, and supply is stated, so the knowledge can be rebuilt from first principles where none of today's institutions exist. The planned space and isolated-systems lessons cover life support, radiation, vacuum and cryogenics, closed-loop resources, and reliability far from repair.

## Further reference

- [Roadmap](ROADMAP.md): the general four-year path through levels 0 to 2.
- [SJSU mechanical engineering track](tracks/sjsu-mechanical-engineering.md): one real program's sequence over the same lessons.
- [README](README.md): the map of every folder.
