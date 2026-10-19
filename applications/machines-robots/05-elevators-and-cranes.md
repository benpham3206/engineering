# Elevators and cranes

**Type:** lesson

Elevators and cranes lift loads with ropes, drums, and motors, and both depend on one physics: a load must balance around a support point. An elevator must hold its car safely even if the drive fails. A crane must stay upright when it lifts a load on the end of a boom. Both are rated by limits set by ropes, brakes, and stability, and an engineer who sizes or inspects them must check each limit.

**Prerequisites:** [Statics](../../physics/01-statics.md), [Particle dynamics](../../physics/02-particle-dynamics.md), [Factor of safety and failure](../../design/07-factor-of-safety-and-failure.md), [Induction motors](../electrical/03-induction-motors.md)
**Time:** 8-10 h

## Core ideas

### How it works

A traction elevator hangs the car on one end of a set of steel ropes and a counterweight on the other. The ropes run over a traction sheave, a grooved wheel that a motor turns. Friction in the grooves drives the ropes without slipping. The counterweight carries most of the car's weight, so the motor only lifts the difference.

The movement of a traction elevator follows these steps:

1. The motor turns the traction sheave.
2. Friction in the grooves moves the ropes, so the car rises and the counterweight descends.
3. When the car stops, an electrically released brake on the motor shaft holds the sheave.
4. If the car overspeeds, the governor trips the safety gear, which grips the guide rails and stops the car.

A crane lifts a load by winding rope onto or off a drum. The boom sets the radius from the tipping line to the load. The load creates an overturning moment about the tipping line, and the crane's own weight and counterweight create a restoring moment in the opposite direction. The crane stays upright while the restoring moment exceeds the overturning moment by the margin the load chart allows.

### Main parts

- **Traction sheave and ropes:** the sheave drives the ropes by friction. Several ropes share the load, and their grooves wear over time.
- **Counterweight:** a frame loaded with weights. Its mass is chosen to balance the car plus part of the rated load.
- **Brake:** a spring-applied brake that releases only when power is supplied. It fails to the held state.
- **Governor and safety gear:** the governor detects overspeed. The safety gear grips the guide rails and stops the car.
- **Buffers:** springs or hydraulic buffers at the bottom of the hoistway absorb the energy of a car that overruns the lowest landing.
- **Crane outriggers or counterweight:** outriggers widen the base, and a counterweight adds restoring moment.
- **Boom and winch:** the boom sets the radius, and the winch lifts the load. A load-moment indicator warns the operator when the load approaches the rated limit.

### Variants

- **Geared or gearless traction elevator:** the most common type in buildings. A gearless drive suits high speeds.
- **Hydraulic elevator:** a piston under the car pushes it up. These suit low rises.
- **Machine-room-less elevator:** the drive sits in the hoistway instead of a separate room.
- **Mobile crane:** a crane on a truck or crawler base. Outriggers or a crawler base set the stability.
- **Tower crane:** a fixed mast carries a jib, with a counterweight on a counter-jib.
- **Overhead bridge crane:** a trolley runs on rails fixed to the building structure, so the building carries the stability load.

## Key equations

Rope tension ratio on a traction sheave, from the Euler-Eytelwein equation. $T_1$ and $T_2$ are rope tensions in newtons (N) on the heavy side and light side. $\mu$ is the effective friction coefficient in the grooves (dimensionless). $\theta$ is the angle of wrap in radians:

$$\frac{T_1}{T_2} = e^{\mu \theta}$$

Assumptions: the rope is about to slip, the friction is uniform around the wrap, and the rope is inextensible.

Motor power for an elevator at steady speed. $m_c$ is the car mass, $m_L$ the rated load, and $m_{cw}$ the counterweight, all in kilograms (kg). $g$ is the local gravitational acceleration ($9.81\ \text{m/s}^2$ at Earth's surface). $v$ is the car speed in metres per second (m/s), and $\eta$ is the drive efficiency (dimensionless):

$$P = \frac{(m_c + m_L - m_{cw})\, g\, v}{\eta}$$

Assumptions: steady speed (acceleration ignored), uniform efficiency, and a counterweight that stays in place. The result is in watts (W).

Rope tension in a hoist with $n$ rope parts supporting the load (dimensionless). $W$ is the load weight in newtons (N), and $\eta$ is the reeving efficiency (dimensionless):

$$T = \frac{W}{n\, \eta}$$

Assumptions: all parts carry equal tension, and the sheave efficiency is the same for each part.

Crane load capacity from stability. $f$ is the margin fraction set by the load chart standard (dimensionless, less than 1). $W_i$ are the weights of the restoring masses in newtons (N), and $d_i$ their distances behind the tipping line in metres (m). $R$ is the radius from the tipping line to the load in metres (m). The capacity $W_{\text{cap}}$ is in newtons (N):

$$W_{\text{cap}} = \frac{f \sum_i W_i d_i}{R}$$

Assumptions: the crane tips about one line, the restoring masses act at their stated distances, and the boom and hook weights are included in the $W_i$ terms.

## Worked example

**Given:** A mobile crane tips about its front outrigger line. Its body weighs $W_b = 40\ \text{kN}$, with its centre of gravity $2.0\ \text{m}$ behind the tipping line. A counterweight of $W_{cw} = 10\ \text{kN}$ sits $4.0\ \text{m}$ behind the line. The load chart margin is $f = 0.75$, an assumed value for this example.

**Find:** (a) the restoring moment, and (b) the rated capacity at radii of 6 m, 9 m, and 12 m.

**Assumptions:** The crane tips about one line, the restoring masses act at their stated distances, and the boom and hook weights are included in the body weight.

**Solution:**

1. Restoring moment: $M_r = \sum W_i d_i = 40 \times 2.0 + 10 \times 4.0 = 120\ \text{kN m}$.
2. Capacity at each radius, from $W_{\text{cap}} = f M_r / R = 0.75 \times 120 / R = 90 / R$ kN:
   - $R = 6\ \text{m}$: $W_{\text{cap}} = 90 / 6 = 15.0\ \text{kN}$.
   - $R = 9\ \text{m}$: $W_{\text{cap}} = 90 / 9 = 10.0\ \text{kN}$.
   - $R = 12\ \text{m}$: $W_{\text{cap}} = 90 / 12 = 7.5\ \text{kN}$.

**Answer:** (a) $M_r = 120\ \text{kN m}$. (b) 15.0 kN at 6 m, 10.0 kN at 9 m, and 7.5 kN at 12 m.

**Sanity check:** The product of capacity and radius is 90 kN m at each radius, which equals $f M_r$. That is the load-chart logic: capacity falls as $1/R$ while stability controls. Real charts also cap the capacity at short radii, where the boom's strength controls instead. A load-chart value should never be exceeded for any reason, including wind on the boom.

## Design trade-offs

- **Counterweight size against motor size:** a heavier counterweight lowers the motor power for a given load, but it adds mass to the building and to the shaft and rope loads.
- **Rope count against sheave diameter:** more ropes share the load and reduce wear, but a larger sheave is needed for each rope's bending life.
- **Outrigger span against footprint:** a wider span raises the restoring moment and the capacity, but it needs more space on site.
- **Boom length against capacity:** a longer boom reaches farther, but the same load sits at a larger radius, so the capacity falls.
- **Braking distance against comfort:** a stronger brake stops the car in a shorter distance, but it gives a harder stop for passengers.
- **Speed against cost:** higher speeds need a gearless drive and better buffers, which cost more.

## How it fails

- **Rope wear and broken wires:** the sign is broken wires and a loss of rope diameter. Inspection and retirement criteria catch it before the rope fails.
- **Brake failure:** the sign is a car that drifts when stopped. Brake tests and dual brakes limit the risk.
- **Overspeed:** the governor trips the safety gear, and buffers absorb the rest of the energy.
- **Overload or overturning:** the sign is a load-moment alarm. A crane that exceeds its chart can tip, and a load-moment indicator with an automatic cutoff prevents it.
- **Soft ground:** a crane sinks under an outrigger. Spreader pads and ground checks prevent it.
- **Wind on the boom:** wind adds overturning moment. Wind limits on the load chart set the safe operating range.
- **Low traction:** wet or worn grooves lower $\mu$, so the sheave slips. Groove inspection and rope tension checks catch it early.

**Safety controls, in order of preference:**

1. Elimination: keep loads and people apart with exclusion zones, and avoid lifting over occupied areas.
2. Substitution: use a rope or chain grade and a brake with a higher rating than the chart needs.
3. Engineering controls: safety gear, a governor, buffers, load-moment indicators with automatic cutoffs, and outrigger position sensors.
4. Administrative controls: a signed lift plan, a rule against lifting above the chart, and a schedule of rope and brake inspection.
5. Personal protective equipment: hard hats, high-visibility clothing, and gloves for rigging. PPE protects people, and it does not replace the controls above.

**Lockout and tagout for service:** before a technician works in the hoistway, machine room, or on a crane drive, the technician isolates the supply at the main disconnect and locks it with a personal lock. The technician attaches a tag with the name and date, tests the controls to confirm the drive does not run, and discharges stored energy. Where the car or boom could move under gravity, the technician blocks it with a mechanical stop before work starts. The lock comes off only by the person who fitted it, after the work and the checks are complete.

## History

Elisha Otis demonstrated a safety brake for a hoist at the New York Crystal Palace in 1854. In the demonstration, he cut the rope of a raised platform, and a brake stopped it. His first passenger elevator went into the E. V. Haughwout store in New York in 1857. The safety principle still governs elevators today, and the governor and safety gear are its direct descendants.

## Practice

Where a problem needs gravitational acceleration, use $g = 9.81\ \text{m/s}^2$ (Earth surface).

1. An elevator car has a mass of 1000 kg, the counterweight is 1400 kg, the rated load is 1000 kg, and the car travels at 2.5 m/s. The drive efficiency is 0.75. Find the motor power at full load.
2. A traction sheave has a wrap angle of $\pi$ rad and an effective friction coefficient $\mu = 0.15$. The heavy-side tension is 2000 N. Find the light-side tension at the point of slip.
3. A hoist with four rope parts lifts a 20 kN load at a reeving efficiency of 0.95. Find the tension in each rope part.
4. A crane has a restoring moment of 120 kN m and a margin fraction of $f = 0.85$. Find its rated capacity at a radius of 10 m.
5. Short answer: why does a traction elevator need a counterweight?

<details><summary>Answers</summary>

1. $P = (1000 + 1000 - 1400) \times 9.81 \times 2.5 / 0.75 = 19\,620$ W, which is 19.6 kW.
2. $e^{0.15\pi} = 1.602$, so $T_2 = 2000 / 1.602 = 1248$ N.
3. $T = 20\,000 / (4 \times 0.95) = 5263$ N, which is 5.26 kN.
4. $W_{\text{cap}} = 0.85 \times 120 / 10 = 10.2$ kN.
5. The counterweight carries most of the car weight, so the motor only lifts the unbalance. A smaller motor, with less torque, does the job, and the brake holds less load.

</details>

## Common mistakes

- Sizing an elevator motor from the car and the full load alone. The counterweight changes the unbalance, and that sets the power.
- Using the load at the tip and leaving out the boom and hook block. Those parts move the centre of gravity and the restoring moment.
- Reading a load chart's rated capacity as the total weight lifted. The hook block and rigging count as part of the load.
- Relying on a brake alone for overspeed. The brake holds the car, and the governor and safety gear protect against overspeed.
- Ignoring wind on the boom. A large boom presents a large sail area, and wind adds overturning moment.

## Go deeper

- [OpenStax, University Physics Volume 1, Conditions for Static Equilibrium](https://openstax.org/books/university-physics-volume-1/pages/12-1-conditions-for-static-equilibrium) by OpenStax: a free text on torque balance, the basis of tipping analysis.
- [MIT OpenCourseWare, Design and Manufacturing I (2.007)](https://ocw.mit.edu/courses/2-007-design-and-manufacturing-i-spring-2009/) by MIT: a free course on machine design.
- Reference sheets: [Mechanics reference](../../physics/reference-mechanics.md) and [Design reference](../../design/reference.md).
- Related lessons: [Statics](../../physics/01-statics.md), [Clutches and brakes](../power-transmission/04-clutches-and-brakes.md), [Towers and cables](../structures/06-towers-and-cables.md), and [Robot arms](01-robot-arms.md).
