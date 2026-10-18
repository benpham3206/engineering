# Problem-solving reference

**Type:** reference

A dense lookup sheet for engineers solving real problems: the working method, dimensional analysis, limiting-case tests, orders of magnitude, Fermi estimates, root-cause tools, decision matrices, debugging checklists, and the cognitive traps that bend answers. Use it mid-task; the lessons in this folder teach the same ideas.

## Principles

- Conservation: mass, energy, momentum, and charge are accounted for. A model that creates or destroys them is wrong until proven otherwise.
- Balance: for a body at rest, the sum of forces and the sum of moments are zero. For a body that accelerates, $\sum F = ma$.
- Dimensional homogeneity: only quantities with the same dimensions can be added, subtracted, or set equal.
- Every answer comes from a model, and the assumptions are part of the model. Write them down with the answer.
- Second law: no cyclic device converts heat fully into work. The Carnot bound is $\eta \le 1 - T_c/T_h$, with temperatures in kelvin.
- Nothing carries matter or information faster than light in vacuum: $c = 299\,792\,458\ \text{m/s}$ (exact).
- Scaling: areas grow as $L^2$ and volumes and masses as $L^3$. Strength and stiffness scale differently, so a larger copy of a part is rarely a safe copy.
- Local conditions matter: $g$, air pressure, and temperature depend on place. State the local value. Earth values are one case.
- A correct formula obeys its limits. Test it at zero, at very large values, and at special angles.
- Failures are chains. Fix the broken link, not the symptom.

## The method on one page

Use these eight steps in order. Each step has one output you can point to.

1. **Given.** List every known with its unit. Mark what you calculated as "derived," not "given."
2. **Find.** Name each unknown with a symbol and unit. Write the goal in one sentence.
3. **Assumptions and constraints.** Each assumption names what it throws away and why that is safe. Constraints are rules the system must obey.
4. **Sketch.** Draw the geometry, supports, and loads. Draw a free-body diagram of one object. Put axes on the drawing and label each force with a symbol and unit.
5. **Principles.** Pick by question: balance (nothing moves), Newton's second law (something accelerates), energy (no losses), mass (flow in equals flow out), heat (flow through a wall). Count independent equations against unknowns. Fewer equations than unknowns means a missing known, assumption, or constraint.
6. **Symbolic solution.** Solve for the unknown in symbols only. Check the units of the result and one limit before going further.
7. **Numbers.** Substitute with units. Carry full precision and round at the end, to two or three significant figures for estimates.
8. **Check.** Run an order-of-magnitude estimate, a sign and direction check, and an intuition check against a known object. If you can, solve by a second method. A failed check sends you back to step 1 or to debugging, not to an explanation.

## Units and limits

### Buckingham pi theorem

Use it to find the form of a relationship before you know the equation.

- Variables: list every quantity that plays a role, $n$ in total.
- Base dimensions: count the independent ones, $k$ (usually mass M, length L, time T, and temperature, electric current, or amount when needed).
- Result: the relationship is equivalent to $n - k$ dimensionless groups, called pi groups. Write it as $f(\Pi_1, \Pi_2, \dots) = 0$.
- Choose $k$ repeating variables that together carry all base dimensions and are independent of each other. Each pi group is one remaining variable multiplied by powers of the repeating variables, with exponents chosen so the group is dimensionless.

**Worked example: simple pendulum.** Period $T$ (s) of a bob of mass $m$ (kg) on a string of length $L$ (m), in local gravity $g$ (m/s$^2$), released from angle $\theta_0$ (rad, dimensionless).

- Variables: $n = 5$ ($T, m, L, g, \theta_0$). Base dimensions: $k = 3$ (M, L, T).
- Pi groups: $n - k = 2$.
- Repeating variables: $m$ (M), $L$ (L), $g$ (LT$^{-2}$). They are independent and cover M, L, and T.
- $\Pi_1 = T\,L^{-1/2}\,g^{1/2} = T\sqrt{g/L}$. Dimensionless, since $T \cdot \sqrt{\text{s}^{-2}} = 1$.
- $\Pi_2 = \theta_0$.
- Result: $T\sqrt{g/L} = f(\theta_0)$, so $T = \sqrt{L/g}\,f(\theta_0)$.
- The mass does not appear. Dimensional analysis alone says so, and an experiment with different bobs confirms it.
- Exact form: $f(\theta_0) = \dfrac{2}{\pi}K\!\left(\sin\tfrac{\theta_0}{2}\right)$, where $K$ is the complete elliptic integral of the first kind (modulus form). Small-angle form: $f \approx 1 + \theta_0^2/16$.

| $\theta_0$ | $f$ exact | $1 + \theta_0^2/16$ | Error of approximation |
|---|---|---|---|
| 5 deg | 1.00048 | 1.00048 | 0.00 % |
| 10 deg | 1.00191 | 1.00190 | 0.00 % |
| 20 deg | 1.00767 | 1.00762 | 0.005 % |
| 30 deg | 1.01741 | 1.01713 | 0.03 % |
| 60 deg | 1.07318 | 1.06854 | 0.43 % |

For $L = 1.00\ \text{m}$ at standard gravity $g = 9.80665\ \text{m/s}^2$: $T_0 = 2\pi\sqrt{L/g} = 2.006\ \text{s}$ at small angle. At $20$ deg the period is $2.022\ \text{s}$; at $60$ deg it is $2.153\ \text{s}$.

**Second example, drag on a body.** Force $F$ (N) on a body of size $D$ (m) moving at speed $v$ (m/s) through fluid of density $\rho$ (kg/m$^3$) and dynamic viscosity $\mu$ (Pa$\cdot$s). Five variables, three base dimensions, so two groups:

$$
C_d = \frac{F}{\tfrac{1}{2}\rho v^2 D^2}, \qquad \text{Re} = \frac{\rho v D}{\mu}, \qquad C_d = f(\text{Re}) \text{ for a fixed shape}
$$

- Holds when: the body shape is geometrically similar between tests, and the only forces are drag and inertia or viscosity. Compressibility enters as $v$ approaches the speed of sound (a common rule-of-thumb threshold is Mach 0.3).
- Breaks when: shape changes, surface roughness matters, or compressibility or free-surface effects are present. Each one adds a missing pi group.
- Typical: a smooth sphere has $C_d \approx 0.47$ over a wide subcritical range of Re (typical, roughly $10^3$ to $10^5$). A car at 30 m/s with $C_d A = 0.66\ \text{m}^2$ in air of density $1.2\ \text{kg/m}^3$ feels about $356\ \text{N}$ of drag, which is about $10.7\ \text{kW}$ of power to overcome (typical).

**Holds when:** the list of variables is complete. Dimensional analysis cannot find a variable you forgot. It only finds the form of the answer from the list you give it.
**Breaks when:** a variable is left out (for example, air resistance missing from a pendulum with a heavy bob at high speed), or the physics has a regime change inside the test range.

**Rule of thumb:** before running an experiment, write the pi groups. Each group is one axis of the plot. Fewer axes means fewer runs.

### Limiting-case checks

Push one input to an extreme and confirm the answer does what physics requires.

| System | Formula | Limit test | Required behavior |
|---|---|---|---|
| Pendulum | $T = \sqrt{L/g}\,f(\theta_0)$ | $\theta_0 \to 0$ | $T \to 2\pi\sqrt{L/g}$, finite |
| Pendulum | same | $g \to 0$ | $T \to \infty$ (no restoring force) |
| Two cables, sign hung | $T = \dfrac{mg}{2\sin\theta}$ | $\theta \to 90^\circ$ | $T \to mg/2$, each cable carries half |
| Two cables, sign hung | same | $\theta \to 0$ | $T \to \infty$ (cables go flat; divergence is real) |
| Cantilever beam, tip load | $\delta = \dfrac{F L^3}{3EI}$ | double $L$ | $\delta$ grows by $2^3 = 8$ |
| Heat through a wall | $Q = \dfrac{kA\,\Delta T}{L}$ | double $L$ | $Q$ halves |
| Heat through a wall | same | $\Delta T \to 0$ | $Q \to 0$ |
| Resistors in parallel | $1/R = \sum 1/R_i$ | one $R_i \to \infty$ | Branch removed; result unchanged |
| Carnot engine | $\eta = 1 - T_c/T_h$ | $T_c \to T_h$ | $\eta \to 0$ |

- Holds when: the limit is inside the formula's domain. A small-angle formula is not tested at 90 degrees.
- Breaks when: the limit is outside the regime (for example, $\theta_0 \to 0$ with friction present, where the period has no clean limit). Name the regime before you trust the limit.
- Passing a limit is evidence, not proof. Failing one is strong evidence of an error.

Dimensional check: write the dimensions of each term. Terms that add must match. The result must have the units of the target quantity. Example: cantilever $FL^3/(EI)$ has $\text{N}\cdot\text{m}^3/(\text{N/m}^2 \cdot \text{m}^4) = \text{m}$, a length.

### SI prefixes and conversions

- Prefixes: k $10^3$, M $10^6$, G $10^9$, m $10^{-3}$, $\mu$ $10^{-6}$, n $10^{-9}$.
- Energy: $1\ \text{kWh} = 3.6\ \text{MJ}$; $1\ \text{MJ} = 0.2778\ \text{kWh}$; $1\ \text{kcal} = 4.184\ \text{kJ}$.
- Power: $1\ \text{hp} \approx 746\ \text{W}$ (mechanical horsepower; other horsepower definitions differ).
- Speed: $1\ \text{m/s} = 3.6\ \text{km/h}$.
- Pressure: $1\ \text{atm} = 101\,325\ \text{Pa}$ (exact by definition).
- Mistake to watch: a factor of 10 usually means a prefix error, a factor of 2 usually a missing or extra factor.

## Orders of magnitude

Use these to catch wrong answers in seconds. All values are typical, not exact.

### Quick rules

- 1 kg weighs about 10 N on Earth ($9.81$ rounded to $10$; within 2 %).
- 1 L of water is about 1 kg.
- 1 kWh is 3.6 MJ. A 100 W device running for 1 h uses 0.1 kWh.
- Air at sea level: about $10^5\ \text{Pa}$ (1 atm is $1.013 \times 10^5\ \text{Pa}$).
- 1 m/s is about 3.6 km/h, so 10 m/s is about 36 km/h.

### Energy density

Specific energy is per kilogram. Energy density is per liter. Fuel values are lower heating values (LHV) unless stated.

| Material | Specific energy (MJ/kg) | Energy density (MJ/L) | Basis and notes |
|---|---|---|---|
| Gasoline | about 44 (typical 43 to 46) | about 32 | Density about 0.74 kg/L. LHV. Combustion needs oxygen from air. |
| Lithium-ion cell | about 0.5 to 0.9 (150 to 250 Wh/kg) | about 1.4 to 2.5 (400 to 700 Wh/L) | Stored chemical energy, not combusted. Cell chemistry varies widely. |
| TNT | 4.184 (conventional) | about 6.8 (density about 1.6 kg/L) | 1 kg TNT is defined as 4.184 MJ, which is 1 kcal/g. A convention, not a measured release. |
| Hydrogen | about 120 (LHV); about 142 (HHV) | about 8.5 as liquid at 20 K; about 4.5 to 5 as compressed gas at 700 bar (typical) | 0.011 MJ/L at 1 atm, 0 C (gas is very light). |

Computed: $1\ \text{kg}$ gasoline $\approx 44\ \text{MJ}$ is about $12\ \text{kWh}$. $1\ \text{kg}$ lithium-ion cell at $200\ \text{Wh/kg}$ is $0.72\ \text{MJ}$ and holds about $1/60$ of gasoline by mass.

- Holds when: the energy figure is the one that matters (stored chemical energy available for conversion). Real engines convert only part of it (a typical car engine converts about 20 to 30 % to shaft work).
- Breaks when: you compare masses for a vehicle that carries the energy source as a tank, or you forget that conversion efficiency applies.
- Rule of thumb: a typical combustion engine turns about 20 to 30 % of fuel energy into shaft work (typical), so divide fuel energy by about 3 to 4 for usable output. A typical battery-electric drive chain is far more efficient, around 80 to 90 % (typical). Use measured data when it exists.

### Human power output

| Quantity | Typical value | Basis |
|---|---|---|
| Basal metabolic rate | about 80 to 100 W | Resting adult, about 1.1 to 1.4 W/kg |
| Sustained labor, hour-long | about 75 to 100 W | Typical working output, not peak |
| Trained cyclist, one hour | about 300 to 400 W | Elite cyclists exceed this; typical athletes are lower |
| Short sprint peak | about 1 to 2 kW for seconds | Burst only |

Computed: a person at $100\ \text{W}$ for $8\ \text{h}$ gives $0.8\ \text{kWh}$, or $2.9\ \text{MJ}$. Typical daily food energy (about 2000 kcal, about $8.4\ \text{MJ}$) is close to what a steady $100\ \text{W}$ would spend over a full day ($8.6\ \text{MJ}$), which is why the figure is sensible.

### Typical speeds

| Motion | Typical speed | In km/h |
|---|---|---|
| Walking | 1.4 m/s | 5 |
| Running, jog | 3 m/s | 11 |
| Cycling | 6 to 8 m/s | 22 to 29 |
| Car in town | 14 m/s | 50 |
| Car on highway | 30 m/s | 108 |
| Airliner cruise | about 250 m/s | about 900 |
| Sound in air at 20 C | 343 m/s | 1235 |
| Low Earth orbit (400 km) | about 7.7 km/s | about 27 700 |
| Earth escape from surface | 11.2 km/s | about 40 000 |

- Speed of sound: $v \approx 331.3\sqrt{1 + T/273.15}\ \text{m/s}$, with $T$ in C. Holds for air as an ideal gas near room conditions. Breaks in other gases (use $\sqrt{\gamma R T/M}$) and in dense media.
- Orbital speed: $v = \sqrt{GM/r}$ for a circular orbit at radius $r$ from center of mass. Earth values: $GM \approx 3.986 \times 10^{14}\ \text{m}^3/\text{s}^2$, $R \approx 6.37 \times 10^6\ \text{m}$. Other bodies use their own $GM$.

### Typical forces

| Force | Typical value | Basis |
|---|---|---|
| Weight of 1 kg | about 9.8 N (local $g$) | $W = mg$ |
| Adult human body weight | about 700 N (about 70 kg) | $mg$ with Earth $g$ |
| Adult maximal hand grip | about 300 to 500 N | Typical, varies widely |
| Car tire static load | about 3.7 kN | 1500 kg car, four tires, equal share |
| Car drag at 30 m/s | about 0.36 kN | $\tfrac{1}{2}\rho v^2 C_d A$ with $C_d A = 0.66\ \text{m}^2$ |

- Holds when: the quoted force is the one in question. A tire's static load is not its braking limit.
- Breaks when: loads are dynamic. Impacts and shocks can multiply static loads several times.

### Typical power of devices and systems

Electrical power in watts. Energy in kWh for one hour of use is the same number divided by 1000.

| Device or system | Typical power | Notes |
|---|---|---|
| Phone charger | 5 to 30 W | USB-C fast charging at the top of this range |
| LED bulb | 5 to 12 W | Replaces incandescent bulbs at 40 to 60 W |
| Laptop, in use | 30 to 60 W | Charger rated higher than average draw |
| Desktop PC | 150 to 400 W | Depends on graphics card and load |
| Microwave oven | about 1 kW output, about 1.5 kW input | Rated output is the cooking power |
| Electric kettle | 1.5 to 2 kW | Short bursts |
| Home EV charger (Level 2) | about 7 kW | Typical installed unit |
| Car engine | about 100 kW | About 130 hp |
| DC fast charger for EV | 50 to 350 kW | Varies by charger class |
| Average household (typical, one country's scale) | about 1 to 1.5 kW average | Average, not peak |
| Large power station | 0.5 to 1 GW | One 1 GW plant for one year is 8.76 TWh (computed) |
| Sunlight on a surface at noon | about 1 kW/m$^2$ | Peak clear sky, typical |

- Holds when: values are used for scale. Devices vary by model.
- Breaks when: you multiply peak by time and forget duty cycle. Use average power for energy.
- Rule of thumb: to estimate energy, multiply average power by time, then convert with $1\ \text{kWh} = 3.6\ \text{MJ}$.

## Fermi estimation

A Fermi estimate gives an order of magnitude with a range. Five steps:

1. **Decompose.** Write the quantity as a formula of parts you can estimate.
2. **Assume.** Give each part a value with its unit and a reason.
3. **Round.** Use one significant figure for each input.
4. **Compute.** Carry the rounded values through the formula.
5. **Bound.** Compute a low and a high case by changing the most uncertain inputs. Report the range.

**Worked example: heartbeats in a lifetime.** Decompose: beats per minute $\times$ minutes per year $\times$ years.

- Beat rate: $70$ per minute (typical resting adult). Range $60$ to $100$.
- Minutes per year: $60 \times 24 \times 365 = 525\,600$.
- Lifetime: $80$ years. Range $70$ to $90$.
- Central estimate: $70 \times 525\,600 \times 80 = 2.9 \times 10^9$ beats.
- Bounds: low $60 \times 525\,600 \times 70 = 2.2 \times 10^9$; high $100 \times 525\,600 \times 90 = 4.7 \times 10^9$.
- Answer: about $3 \times 10^9$ beats, range $2 \times 10^9$ to $5 \times 10^9$.

- Holds when: the decomposition is a real formula and each input has a source or reason.
- Breaks when: a part is ignored that dominates (for example, estimating a city's energy use without transport or industry).
- Rule of thumb: an order-of-magnitude estimate is right within a factor of about 3 to 10. Claim no more precision than the inputs support.
- Cross-check: compare to a known total (a household's annual energy, a city's population). A result larger than the whole known total is an error.

## Root cause tools

### Five whys

- Ask "why" five times, or until the answer is a process or design choice you can change. Each answer must be a fact, not a blame.
- Example: a pump bearing overheated. Why? Lubricant was low. Why? A seal leaked. Why? The seal was past its service life. Why? The replacement interval was not in the maintenance system. Why? Intervals are set by memory, not by a schedule. Root cause: intervals not recorded, which is actionable.
- Holds when: the cause is a single chain. Breaks when: several causes act together. Use a fishbone or a fault tree then.

### Fishbone (Ishikawa) diagram

Lay the problem at the head. Draw one bone per category. Brainstorm causes on each bone.

- Manufacturing categories (6M): Methods, Machines, Materials, Manpower (people), Measurement, Mother nature (environment).
- Process and software categories: Methods, Tools, Inputs, People, Measurements, Environment.
- Holds when: the team has enough knowledge to list causes. Breaks when the list grows long without data. Test each cause with an experiment, or rank by data.

### Fault tree basics

A fault tree works from the top event (the failure) down to basic events (component failures) with logic gates.

- OR gate: the output occurs if any input occurs.
- AND gate: the output occurs only if all inputs occur.
- Minimal cut set: the smallest set of basic events that causes the top event. Fewer members means a more critical path.
- For independent basic events with probabilities $p_i$ over a fixed period or demand:

$$
P_{\text{AND}} = \prod_i p_i, \qquad P_{\text{OR}} = 1 - \prod_i (1 - p_i) \approx \sum_i p_i \text{ when each } p_i \ll 1
$$

- Worked example: two redundant pumps, each failing on demand with $p = 10^{-3}$, both fail with $P_{\text{AND}} = 10^{-6}$. That redundant pair is in series with a sensor of $p = 5 \times 10^{-4}$, so the top event is an OR: $P \approx 5.0 \times 10^{-4}$ (the pair adds only $10^{-6}$). The sensor dominates, so improving the pumps alone changes nothing.
- Holds when: the events are independent. Breaks when: a common cause (one power supply, one maintenance crew, one bad batch) makes them dependent. Then the AND result is far too optimistic. Common-cause analysis is needed. Screening studies often use a beta factor (the fraction of failures shared by common cause), typically 0.01 to 0.1, until data says otherwise.

### FMEA (failure mode and effects analysis)

For each function, list failure modes. Rate each on three scales, each from 1 (best) to 10 (worst):

- Severity S: how bad the effect is on the user or system.
- Occurrence O: how likely the cause is.
- Detection D: how unlikely the failure is to be caught before it reaches the user. High number means hard to detect.

$$
\text{RPN} = S \times O \times D \qquad (1 \le \text{RPN} \le 1000)
$$

- Worked example: a solder joint cracks, causing intermittent field failure. $S = 7$, $O = 4$, $D = 5$, so $\text{RPN} = 140$.
- Holds when: scales are defined before rating and used consistently across the whole analysis.
- Breaks when: RPN is used alone. Two items with the same product can differ widely in risk. Common practice is to act on any high severity (for example $S \ge 9$) regardless of RPN, and to check occurrence and detection separately.

## Decision matrices

Use a weighted matrix to compare options against several criteria.

Steps:

1. List criteria. Set must-have criteria as pass or fail first, and drop options that fail.
2. Set weights $w_i$ that sum to 1.
3. Score each option on each criterion, using the same scale (for example 1 to 5), with a definition for each score point.
4. Compute the weighted score for each option:

$$
S_j = \sum_i w_i \, s_{ij}
$$

5. Check sensitivity: change each weight by a plausible amount and see whether the ranking changes.

Worked example: three options scored 1 to 5 on cost (weight 0.30), performance (0.45), and risk (0.25).

| Option | Cost | Performance | Risk | Score |
|---|---|---|---|---|
| A | 4 | 3 | 5 | 3.8 |
| B | 3 | 5 | 3 | 3.9 |
| C | 5 | 2 | 4 | 3.4 |

With weights cost 0.40, performance 0.35, risk 0.25, A scores 3.9 and B scores 3.7. The top rank flips with the weight change, so the decision rests on the weights. Say so in the write-up, and get the weights agreed before scoring.

- Holds when: criteria are independent and the scale is linear across its range. Breaks when criteria overlap (the same concern counted twice) or when a single criterion is a hard limit that a weighted sum can hide (use a gate).
- Rule of thumb: if the top two options are within about 5 % of each other, the matrix has not decided the question. Use the sensitivity check, or collect data on the criterion that separates them.

## Cognitive traps

- Anchoring: the first number you see (a quote, a reference value, a classmate's answer) pulls your estimate toward it. Counter: write your own estimate and range before looking at any reference.
- Confirmation bias: you look for evidence that the design works and under-weight tests that could break it. Counter: write down the test that would prove you wrong, then run it.
- Sunk cost: effort already spent makes you keep an approach that is failing. Counter: ask what you would do if you were starting today with the same data.
- Normalization of deviance: a warning sign appears, nothing bad happens, and the sign becomes "acceptable." The 1986 Space Shuttle Challenger accident is the standard case, where O-ring erosion seen on earlier flights was treated as normal. Counter: set numeric limits, log every deviation, and require a closure action when a limit is exceeded.
- Planning fallacy: schedules and budgets assume ideal progress. Counter: use past project data, and add a margin scaled to the uncertainty.
- Availability bias: a recent or vivid failure feels more likely than a statistically common one. Counter: check the frequency data before you change the design.

## Checklists

### Before trusting a calculated result

- [ ] Problem stated: knowns, unknowns, assumptions, constraints, goal.
- [ ] Every number has a unit, and unit conversions were applied.
- [ ] Symbolic solution written before numbers. Units checked on the symbolic form.
- [ ] Limiting case tested (zero, large, special angle).
- [ ] Order-of-magnitude estimate done. Result within a factor of about 3 of it, or the gap explained.
- [ ] Signs and directions checked against the sketch.
- [ ] Rounding: full precision carried, two or three significant figures reported.
- [ ] Assumptions listed with the direction of error each one causes (conservative or not).

### Debugging a calculation

- [ ] Reproduce the bad answer from exact inputs.
- [ ] Run a known case through the same chain. Pass means input error; fail means formula or code error.
- [ ] Check units at every step. A factor of 10 suggests a prefix; a factor of 2 suggests a missing factor.
- [ ] Print intermediate values and compare each to expectation.
- [ ] Change one thing at a time.
- [ ] Fix the cause. Do not multiply the result by a constant to match a reference.
- [ ] Confirm on a second, independent input.

### Debugging hardware

- [ ] Power first. Measure voltage at the load while it is connected, not at the source only. Check polarity.
- [ ] Current draw against the expected value. Compare inrush (startup) and steady-state separately.
- [ ] With power off: check continuity and look for shorts between supply and ground.
- [ ] Ground: verify a single low-impedance return path and that all grounds are bonded where the design says.
- [ ] Measure the signal at each stage of the chain, from input to output. The first stage that is wrong is the suspect.
- [ ] Compare each measurement to the schematic and the datasheet value, with its tolerance.
- [ ] Reseat connectors and check cable strain relief. Flex or vibration can make an intermittent fault look like a logic fault.
- [ ] Check temperature. A part that runs hot is often the first failure, and a thermal fault changes with time.
- [ ] Swap in a known-good part or module, one at a time, and log each swap.
- [ ] Reproduce the fault on the bench before and after the fix.

### Before releasing a design

- [ ] Every failure mode has a severity, occurrence, and detection rating (FMEA), with high-severity items acted on.
- [ ] Safety factor stated with its basis (code, test data, or analysis), and the load case that governs.
- [ ] Assumed operating conditions (temperature, humidity, altitude, load range) written next to the design.
- [ ] Tested at or beyond the limits of the operating envelope, not only at nominal values.

## Sanity checks

- A 50 kg mass weighs about 500 N; a force of 50 kN (about 5 t of mass) is the weight of a small truck, not a person.
- A 100 W lamp running for 10 h uses 1 kWh (3.6 MJ). Convert to cost with your local tariff, not a remembered one.
- A kilogram of fuel holds about 40 to 50 MJ; a kilogram of battery holds about 1 MJ. Gasoline is roughly 50 times the battery by mass.
- Air at sea level is about $10^5$ Pa. Water at 10 m depth adds about $10^5$ Pa, so pressure doubles at about 10 m of water.
- A stress or pressure of $10^6$ Pa (1 MPa) is about 10 atm, a common pneumatic pressure.
- A speed of 200 m/s is the speed of a jet, not a car. A speed of 2000 m/s is about 7000 km/h.
- A 1 GW power station delivers about $8.6 \times 10^{13}$ J per day (computed). A quantity that comes out near that figure for one city needs a careful check.

## Further reference

These are classic, named works. Paid works are listed by name only.

- George Polya, *How to Solve It* (1945): the problem-solving steps used in the method above.
- Edward Buckingham, "On Physically Similar Systems" (1914), the original pi theorem paper. Also Grigory Barenblatt, *Scaling* (Cambridge University Press, 2003), for scaling and dimensional analysis.
- Ralph Langhaar, *Dimensional Analysis and Theory of Models* (1951), a standard reference for pi groups.
- Enrico Fermi and the Fermi-problem tradition; Lawrence Weinstein and John Adam, *Guesstimation* (Princeton University Press, 2008) for worked estimation problems.
- Kaoru Ishikawa, *Guide to Quality Control* (Asian Productivity Organization), the origin of the fishbone diagram.
- IEC 60812, *Failure modes and effects analysis (FMEA and FMECA)*: the international standard for FMEA method.
- IEC 61025, *Fault tree analysis (FTA)*: the international standard for fault trees.
- Diane Vaughan, *The Challenger Launch Decision* (University of Chicago Press, 1996), the study that gave the term normalization of deviance its common use in engineering.
- Daniel Kahneman, *Thinking, Fast and Slow* (2011), the standard reference for anchoring, confirmation bias, and other judgment traps.
- James Reason, *Human Error* (Cambridge University Press, 1990), on error chains and organizational causes.
- Lessons in this folder: [01 Define the problem](01-define-the-problem.md) through [08 Debugging](08-debugging.md).
