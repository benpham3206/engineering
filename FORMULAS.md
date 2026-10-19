# Formulas

**Type:** reference
**Verify:** strict

The map of every formula in this repo: which sheet owns each family of formulas, and the order to learn them in from level 0 to level 5. It holds no equations, constants, or property values itself. Each formula lives in exactly one owner sheet, and every other page links to that owner instead of restating it, so a correction made once reaches every reader.

## How to use this spine

1. Find the family you need in the [ownership map](#formula-ownership-map) and open its owner sheet.
2. Read the entry's variables table, its "Holds when" and "Breaks when" lines, and its source before using the formula. The [reference-entry contract](VERIFICATION.md#reference-entries) says what every entry carries.
3. Take symbols from [the notation table](data/notation.md), units from [units](data/units.md), and constants from [constants](data/constants.md) and [properties](data/properties.md). A sheet never restates a constant's value as its own.
4. Follow the route for your level below when learning a field for the first time. Each route lists the lesson folders first and the owner sheets after.
5. A sheet marked planned does not exist yet. It is named in plain text, not linked, until it does.

The levels are defined in [LEVELS.md](LEVELS.md).

## Level 0 foundations

For a reader with no background. The goal is to read a formula, put numbers with units into it, and judge whether the answer is the right size.

- Lessons: [Algebra](math/01-algebra.md), [Units and dimensional analysis](measurement/01-units-and-dimensional-analysis.md), and [Estimation](problem-solving/07-estimation.md).
- Owner sheets: the [math foundations sheet](math/reference-foundations.md) (arithmetic, fractions, ratios, percent, powers of ten, rearranging an equation, reading a graph), and the [units and limits](problem-solving/reference.md#units-and-limits) section of the problem-solving sheet.
- Habits to build: write the unit beside every number, convert to SI once, and check the size of every answer against something you know.

## Level 1 mathematics and physics

For a maker who builds working things and wants to know why they work.

- Lessons: [Trigonometry](math/02-trigonometry.md), [Statics](physics/01-statics.md), [Particle dynamics](physics/02-particle-dynamics.md), and [Circuit basics](applications/electronics/01-circuit-basics.md).
- Owner sheets: [trigonometry](math/reference.md#trigonometry); [statics](physics/reference-mechanics.md#statics), [section properties](physics/reference-mechanics.md#section-properties), and [dynamics](physics/reference-mechanics.md#dynamics) in the mechanics sheet; [circuit relations](physics/reference-fields-waves-space.md#circuit-relations) in the fields sheet.

## Level 2 engineering core

The fundamentals of a four-year engineering degree.

- Mathematics: [calculus](math/reference.md#calculus), [vector calculus](math/reference.md#vector-calculus), [linear algebra](math/reference.md#linear-algebra), [ordinary differential equations](math/reference.md#ordinary-differential-equations), [Laplace transform](math/reference.md#laplace-transform), [Fourier series](math/reference.md#fourier-series), [probability and statistics](math/reference.md#probability-and-statistics), and [numerical methods](math/reference.md#numerical-methods). These now live in their own sheets: [calculus](math/reference-calculus.md), [linear algebra and differential equations](math/reference-linear-algebra-differential-equations.md), and [probability and numerical methods](math/reference-probability-numerical-methods.md); the combined math sheet keeps its sections until they become redirects.
- Solid mechanics: [stress and strain](physics/reference-mechanics.md#stress-and-strain), [beams](physics/reference-mechanics.md#beams), and [column buckling](physics/reference-mechanics.md#column-buckling).
- Thermal and fluids: [thermodynamics](physics/reference-thermofluids.md#thermodynamics), [second law and entropy](physics/reference-thermofluids.md#second-law-and-entropy), [hydrostatics](physics/reference-thermofluids.md#hydrostatics), [Bernoulli's equation](physics/reference-thermofluids.md#bernoullis-equation), [dimensionless numbers](physics/reference-thermofluids.md#dimensionless-numbers), [pipe flow](physics/reference-thermofluids.md#pipe-flow), and [external flow](physics/reference-thermofluids.md#external-flow-drag-and-lift).
- Fields and waves: [electricity and magnetism](physics/reference-fields-waves-space.md#electricity-and-magnetism), [waves](physics/reference-fields-waves-space.md#waves), and [optics](physics/reference-fields-waves-space.md#optics).
- Materials and measurement: [elastic constants](materials/reference.md#elastic-constants), [Ashby performance indices](materials/reference.md#ashby-performance-indices), and the [measurement sheet](measurement/reference.md) for uncertainty and sensors.
- Design: [factor of safety](design/reference.md#factor-of-safety), [static failure theories](design/reference.md#static-failure-theories), and [tolerancing and stack-up](design/reference.md#tolerancing-and-stack-up).

## Level 3 analysis and design

Trusted to own a component that ships: deeper analysis, design data, and the limits of every model.

- Heat transfer and compressible flow: the [heat transfer sheet](physics/reference-heat-transfer.md) and the [compressible flow sheet](physics/reference-compressible-flow.md).
- Vibration and control: the [vibrations sheet](physics/reference-vibrations.md) and the [controls sheet](physics/reference-controls.md) (modes, stability tests, root locus, frequency response, margins, sampled control).
- Advanced solid mechanics: the [solid mechanics sheet](physics/reference-solid-mechanics.md) (tensors, energy methods, thick cylinders, plates, shells).
- Fracture and fatigue: the [fracture and fatigue sheet](materials/reference-fracture-fatigue.md).
- Machine elements: the [machine design sheet](design/reference-machine-design.md).
- Electrical power: the [electrical power sheet](applications/electrical/reference.md) (phasors, three-phase, per-unit, faults).
- Manufacturing: the [manufacturing sheet](manufacturing/reference.md) for machining, joining, forming, fits, and process statistics.
- Simulation: the [finite element](simulation/reference-finite-element-analysis.md), [computational fluid dynamics](simulation/reference-computational-fluid-dynamics.md), and [verification and validation](simulation/reference-verification-validation.md) sheets.
- Applications: the [applications sheet](applications/reference.md) for motors, pumps, heat exchangers, electronics cooling, and robot arms, until those move to domain sheets.

## Levels 4 and 5 systems and limits

Owning a subsystem, then working from physical limits rather than precedent.

- Reliability: the [reliability sheet](design/reference-reliability.md) (hazard rates, Weibull, series and parallel systems, availability, fault trees), with the [root cause tools](problem-solving/reference.md#root-cause-tools) in the problem-solving sheet.
- Orbits and propulsion: the [orbital mechanics sheet](physics/reference-orbital-mechanics.md).
- Limit analysis: [orders of magnitude](problem-solving/reference.md#orders-of-magnitude) and [Fermi estimation](problem-solving/reference.md#fermi-estimation) in the problem-solving sheet. A level 5 reader starts every design from the governing limit in its owner sheet (conservation, strength, heat flux, or the rocket equation), then measures how far the design sits from it.
- Judgment: the [philosophy sheet](philosophy/reference.md) for failure cases and decision frameworks. It owns no formulas.

## Formula ownership map

One owner per family. Where a new owner sheet replaced a section of an older sheet, the old section keeps its text until it is turned into a one-line link to the new owner.

| Family | Owner | Status |
|---|---|---|
| Arithmetic, fractions, ratios, powers of ten, graphs, complex numbers | [math foundations sheet](math/reference-foundations.md) | owner |
| Algebra, logarithms, trigonometry | [math sheet](math/reference.md#algebra-and-logarithms) | today |
| Calculus, series, vector calculus | [calculus sheet](math/reference-calculus.md) | owner |
| Linear algebra, ordinary differential equations, Laplace and Fourier, PDE types | [linear algebra and differential equations sheet](math/reference-linear-algebra-differential-equations.md) | owner |
| Probability, statistics, numerical methods | [probability and numerical methods sheet](math/reference-probability-numerical-methods.md) | owner |
| Units, dimensional analysis, uncertainty, sensors | [measurement sheet](measurement/reference.md) | today |
| Statics, friction, section properties | [mechanics sheet](physics/reference-mechanics.md#statics) | today |
| Kinematics, Newton's laws, energy, momentum | [mechanics sheet](physics/reference-mechanics.md#dynamics) | today |
| Stress, strain, axial, torsion, bending, Mohr's circle, yield criteria | [mechanics sheet](physics/reference-mechanics.md#stress-and-strain) | today |
| Beam deflection, column buckling | [mechanics sheet](physics/reference-mechanics.md#beams) | today |
| Tensors, energy methods, thick cylinders, plates, shells | [solid mechanics sheet](physics/reference-solid-mechanics.md) | owner |
| Vibration | [vibrations sheet](physics/reference-vibrations.md) | owner |
| Control | [controls sheet](physics/reference-controls.md) | owner |
| Thermodynamics, cycles | [thermofluids sheet](physics/reference-thermofluids.md#thermodynamics) | today |
| Fluid statics, Bernoulli, pipe and external flow | [thermofluids sheet](physics/reference-thermofluids.md#hydrostatics) | today |
| Heat transfer | [heat transfer sheet](physics/reference-heat-transfer.md) | owner |
| Compressible flow | [compressible flow sheet](physics/reference-compressible-flow.md) | owner |
| Electrostatics, magnetism, induction, circuits | [fields sheet](physics/reference-fields-waves-space.md#electricity-and-magnetism) | today |
| Waves, optics | [fields sheet](physics/reference-fields-waves-space.md#waves) | today |
| Gravitation, orbits, rocket equation | [orbital mechanics sheet](physics/reference-orbital-mechanics.md) | owner |
| Three-phase power, per-unit, transformers, faults | [electrical power sheet](applications/electrical/reference.md) | owner |
| Material properties, elastic constants, selection indices | [materials sheet](materials/reference.md) | today |
| Fracture mechanics, fatigue | [fracture and fatigue sheet](materials/reference-fracture-fatigue.md) | owner |
| Creep | [materials sheet](materials/reference.md) | today |
| Safety factors, failure theories, tolerancing, fits | [design sheet](design/reference.md) | today |
| Fasteners, shafts, bearings, gears, springs | [machine design sheet](design/reference-machine-design.md) | owner |
| Reliability, availability, fault trees | [reliability sheet](design/reference-reliability.md) | owner |
| Machining, welding, forming, process statistics | [manufacturing sheet](manufacturing/reference.md) | today |
| Finite elements, computational fluid dynamics, verification and validation | [FEA](simulation/reference-finite-element-analysis.md), [CFD](simulation/reference-computational-fluid-dynamics.md), and [V&V](simulation/reference-verification-validation.md) sheets | owner |
| Dimensional analysis, estimation, decision methods | [problem-solving sheet](problem-solving/reference.md) | today |
| Motors, pumps and fans, heat exchangers, electronics cooling, robot kinematics | [applications sheet](applications/reference.md) | today, until moved to domain sheets |
| Thread identification, material identification | [reverse-engineering sheet](reverse-engineering/reference.md) | today |

## Symbols and units

- Symbols: [notation](data/notation.md) gives one meaning per symbol, the sign and transform conventions, and the few local reuses a variables table may declare.
- Units: [units](data/units.md) builds every unit from the SI base units. Variables tables give SI units only.
- Constants and properties: [constants](data/constants.md) and [properties](data/properties.md). Sheets round these values and the verifier checks each rounding.
- Facts that are not physics, such as a standard's number or a method's origin: [claims](data/claims/README.md).

## Assumption and failure-regime index

Every entry states where its formula holds and how it breaks. The assumptions that recur across sheets, and the owner that states each limit:

- Rigid body versus deformable body: [statics](physics/reference-mechanics.md#free-body-diagrams-and-equilibrium).
- Linear elastic, small strain, small deflection: [stress and strain](physics/reference-mechanics.md#stress-and-strain) and [beams](physics/reference-mechanics.md#beams).
- Slender versus stocky columns: [column buckling](physics/reference-mechanics.md#column-buckling).
- Thin wall versus thick wall: [thin-walled pressure vessels](physics/reference-mechanics.md#thin-walled-pressure-vessels).
- Linear, single-mode, steady-state vibration: [vibrations](physics/reference-mechanics.md#vibrations).
- Ideal gas and constant specific heats: [ideal gas](physics/reference-thermofluids.md#ideal-gas).
- Incompressible, steady, frictionless flow along a streamline: [Bernoulli's equation](physics/reference-thermofluids.md#bernoullis-equation).
- Laminar versus turbulent flow: [pipe flow](physics/reference-thermofluids.md#pipe-flow).
- Static versus cyclic load: [static failure theories](design/reference.md#static-failure-theories) and [fatigue](design/reference.md#fatigue).

## Sanity-check index

Each owner sheet ends with a sanity-check section of orders of magnitude and quick tests. Run the one for the field of the answer:

- [Mechanics](physics/reference-mechanics.md#sanity-checks), [thermofluids](physics/reference-thermofluids.md#sanity-checks), and [fields, waves, and space](physics/reference-fields-waves-space.md#sanity-checks).
- [Mathematics](math/reference.md#sanity-checks), [materials](materials/reference.md#sanity-checks), and [design](design/reference.md#sanity-checks).
- [Problem solving](problem-solving/reference.md#sanity-checks) for estimation and limiting cases across every field.

## Further reference

- [VERIFICATION.md](VERIFICATION.md): what the verifier proves about each entry, and what it cannot.
- [AGENTS.md](AGENTS.md#reference-sheet-referencemd): the reference sheet template and the rule for adding a formula to its owner.
- [ROADMAP.md](ROADMAP.md): the general study order that the level routes follow.
