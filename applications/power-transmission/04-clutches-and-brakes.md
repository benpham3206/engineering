# Clutches and brakes

**Type:** lesson

A clutch connects and disconnects two rotating shafts, and a brake slows or holds a shaft. Both work
by pressing two surfaces together so that friction transmits torque. Engineers size them for torque
capacity, which sets the largest torque that can pass before the surfaces slip, and for heat, because
every joule of slipping energy turns into temperature rise in the parts.

**Prerequisites:** [Statics](../../physics/01-statics.md), [Rigid body dynamics](../../physics/03-rigid-body-dynamics.md), [Axial and torsion](../../physics/04-axial-and-torsion.md), [Heat transfer](../../physics/12-heat-transfer.md), [Trigonometry](../../math/02-trigonometry.md)
**Time:** 6 to 8 h

## Core ideas

### How it works

Friction between two surfaces resists sliding. The friction force is $F_f = \mu N$, where $N$ is the
normal force pressing the surfaces together in newtons (N), and $\mu$ is the coefficient of friction,
which has no units. A clutch uses a clamp force to press a friction lining against a rotating face.
The friction force acts at a radius, so it produces a torque. The torque is the largest one the clutch
can carry before it slips.

A clutch goes through two phases. While the two sides turn at different speeds, the lining slips, and
friction turns the energy of the speed difference into heat. Once the speeds match, the surfaces stick
and carry the full torque with no slip. The kinetic friction coefficient governs the slipping phase.
The static coefficient is higher and governs the locked phase.

A brake works the same way, except one side is fixed to the frame. The brake takes the kinetic energy
of the moving parts and turns it into heat in the rotor or drum. Stopping a car is a heat transfer
problem as much as a friction problem.

### Main parts

- The friction lining is the material that rubs. Organic, sintered metal, and ceramic linings are common.
- Springs, a diaphragm spring, or hydraulic pressure form the clamp mechanism that pushes the plates together.
- The flywheel or pressure plate is the rigid face that the lining presses against.
- The clutch disc carries the lining on a hub. Torsional springs in the hub soften engagement.
- The release mechanism, a bearing and fork or a hydraulic slave cylinder, pulls the plates apart.
- The brake rotor or drum is the rotating part that absorbs the heat. Its mass and surface area set
  how hot it gets.
- The brake caliper or shoes clamp the pads onto the rotor, or press shoes against the inside of a drum.

### Variants

- A single-plate dry clutch uses one disc with two friction faces. Manual car transmissions use it.
- A multi-plate wet clutch runs several discs in oil. The oil cools the plates, so the clutch fits a
  small diameter. Motorcycles and automatic transmissions use it.
- A centrifugal clutch has shoes that swing out at a set speed and grip a drum. Go-karts and
  chainsaws use it, because the clutch engages by speed alone.
- An electromagnetic clutch uses a coil to pull the plates together. A controller can engage it remotely.
- A disc brake has an exposed rotor that sheds heat well and resists fade. Most car wheels use it.
- A drum brake has an enclosed drum. A leading shoe pulls itself into the drum, which is called
  self-energizing, so it needs less actuating force. The enclosure traps heat.
- A band brake tightens a steel band around a drum. Hoists and older machinery use it.

## Key equations

Friction force, in newtons:

$$F_f = \mu N$$

For a clutch disc with friction faces at outer radius $R_o$ and inner radius $R_i$, both in metres (m),
and clamp force $F$ in newtons, the torque with uniform wear is

$$T = \frac{n\,\mu F\,(R_o + R_i)}{2}$$

With uniform pressure on the faces, the torque is

$$T = \frac{2}{3}\,\frac{n\,\mu F\,(R_o^3 - R_i^3)}{R_o^2 - R_i^2}$$

Here $n$ counts the friction faces (two for a single disc with linings on both sides), $T$ is torque in
newton metres (N m), and $\mu$ is dimensionless. Uniform wear is the usual assumption for a worn-in
clutch. Uniform pressure is the usual assumption for a new one.

Power dissipated while the surfaces slip, in watts, with $\omega_{rel}$ the relative angular speed in
radians per second (rad/s):

$$P = T\,\omega_{rel}$$

Energy absorbed by a brake that stops a vehicle of mass $m$ in kilograms (kg) at speed $v$ in metres per
second (m/s):

$$E = \tfrac{1}{2}\,m\,v^2$$

Temperature rise of a lumped heat sink with mass $m$ in kilograms and specific heat $c$ in joules per
kilogram kelvin (J/(kg K)), with no heat lost to the air:

$$\Delta T = \frac{E}{m\,c}$$

Typical values: $\mu \approx 0.3$ to $0.4$ for dry organic linings on steel, and $c \approx 500\ \text{J/(kg K)}$
for cast iron (typical).

## Worked example

**Given:** A dry single-disc clutch has outer radius $R_o = 0.120\ \text{m}$, inner radius
$R_i = 0.070\ \text{m}$, and $\mu = 0.35$ (typical organic lining). The clamp force is $F = 2000\ \text{N}$.
The disc has two friction faces. At the start of a launch, the engine side turns $100\ \text{rad/s}$
faster than the driven plate, and the relative speed falls linearly to zero in $2.0\ \text{s}$.

**Find:** (a) the torque capacity with uniform wear, and (b) the energy the clutch dissipates in the launch.

**Solution:**

1. Torque capacity: $T = \dfrac{2 \times 0.35 \times 2000 \times (0.120 + 0.070)}{2} = 133\ \text{N m}$.
2. Average relative speed: the speed falls from $100$ to $0\ \text{rad/s}$, so the average is $50\ \text{rad/s}$.
   While the clutch carries its full torque, the average power is $P = 133 \times 50 = 6650\ \text{W}$.
3. Energy: $E = P \times t = 6650 \times 2.0 = 13\,300\ \text{J}$.

**Answer:** (a) $T = 133\ \text{N m}$. (b) $E = 13.3\ \text{kJ}$.

**Sanity check:** The capacity of 133 N m must exceed the engine torque at launch, or the clutch keeps slipping. The 6.65 kW average power is the rate the lining heats up during the launch, which is
consistent with a few kilowatts for a car launch.

**Worked example, brake:** A car of mass $1500\ \text{kg}$ brakes from $27\ \text{m/s}$ (about $97\ \text{km/h}$)
to rest on level ground. Four discs, each of mass $8\ \text{kg}$ with $c = 500\ \text{J/(kg K)}$, absorb all the energy.

Energy: $E = \tfrac{1}{2} \times 1500 \times 27^2 = 546\,750\ \text{J} \approx 547\ \text{kJ}$.
Temperature rise: $\Delta T = \dfrac{546\,750}{4 \times 8 \times 500} = 34\ \text{K}$.

This is an upper bound for one stop. The discs lose heat to the air while they cool, so a single stop
heats them less. Repeated stops add up, and the discs can keep climbing in temperature without enough
cooling.

## Design trade-offs

- Torque versus size. The torque grows with the mean radius and with the number of friction faces.
  A wet multi-plate clutch gets high torque in a small diameter, but it needs oil and seals.
- Clamp force versus effort. A stiff diaphragm spring or a strong hydraulic actuator gives a firm
  grip. A pedal must still be easy to press, so designers balance clamp force against pedal force
  through lever ratios.
- Friction material versus life. Organic linings are smooth and quiet, but their friction falls as
  they heat up. Sintered metal keeps more friction when hot, and it wears the mating face faster and
  makes more noise.
- Heat versus mass. A big rotor stores more heat and cools faster per unit of area exposed to air.
  A heavy rotor adds unsprung mass on a car, which hurts ride and handling.
- Smooth engagement versus response. Torsional springs in the clutch disc soften the jerk of
  engagement. Too much spring adds noise and wear.

## How it fails

- Slipping under load. Worn linings, low clamp force, or oil on the lining reduce the torque
  capacity. Warning signs are a burning smell, and engine speed that rises without the car speeding up.
- Glazing. The lining surface shines smooth when it overheats. The friction coefficient drops, and
  the clutch chatters or squeals.
- Brake fade. As pads and rotors get hot, the friction coefficient falls. The pedal goes lower, and
  stopping distance grows. Ventilated discs and good pad compounds reduce it.
- Brake fluid boiling. Very hot discs heat the fluid in the caliper. Vapor bubbles compress, and the
  pedal feels soft. Dual hydraulic circuits and high-boiling-point fluid are the safety measures.
- Disc warping and judder. Uneven heating distorts the rotor. The pedal pulses at speed.
- Safety measures. Pad wear indicators, dual circuits so one leak does not remove all braking,
  and anti-lock systems that stop wheel lockup while the pads still do the work.

## History

Friction brakes are old. Wagons used wooden shoes pressing on wheels long before cars existed.
Frederick Lanchester, in England, patented a disc brake in 1902, and the idea reappeared in racing
cars decades later. The Ford Model T of 1908 used a planetary transmission whose bands tightened on
drums to hold or release the gears. Friction clutches became standard with manual gearboxes in the
early twentieth century.

## Practice

1. A single disc with two friction faces has $R_o = 0.10\ \text{m}$, $R_i = 0.06\ \text{m}$,
   $\mu = 0.30$, and a clamp force of $F = 1500\ \text{N}$. Find the torque capacity with uniform wear.
2. A car of mass $1200\ \text{kg}$ slows from $20\ \text{m/s}$ to rest. The energy goes into two discs
   of mass $6\ \text{kg}$ each, with $c = 500\ \text{J/(kg K)}$. Find the energy absorbed by the discs
   and their temperature rise.
3. A disc brake pad has a friction coefficient of $\mu = 0.40$ and a normal force of $N = 3000\ \text{N}$.
   Find the friction force at the pad.
4. A clutch disc with inner radius $0.05\ \text{m}$ and outer radius $0.15\ \text{m}$ has
   $\mu = 0.25$ and $n = 2$ faces. Find the clamp force needed for a torque of $150\ \text{N m}$ with
   uniform wear.
5. A brake disc of mass $5\ \text{kg}$ and specific heat $500\ \text{J/(kg K)}$ absorbs $60\ \text{kJ}$.
   Find the temperature rise, assuming no heat is lost.

<details><summary>Answers</summary>

1. $T = \dfrac{2 \times 0.30 \times 1500 \times (0.10 + 0.06)}{2} = 72\ \text{N m}$.
2. $E = \tfrac{1}{2} \times 1200 \times 20^2 = 240\ \text{kJ}$. Temperature rise: $240\,000 / (2 \times 6 \times 500) = 40\ \text{K}$.
3. $F_f = \mu N = 0.40 \times 3000 = 1200\ \text{N}$.
4. Solve $T = n\mu F (R_o + R_i)/2$ for $F$: $F = \dfrac{2T}{n\mu(R_o + R_i)} = \dfrac{2 \times 150}{2 \times 0.25 \times 0.20} = 3000\ \text{N}$.
5. $\Delta T = 60\,000 / (5 \times 500) = 24\ \text{K}$.

</details>

## Common mistakes

- Using the diameter where the formula needs the radius. The torque formulas use $R_o$ and $R_i$ in metres.
- Counting one friction face per disc. A single disc with linings on both sides has two faces.
- Using the static friction coefficient for a slipping clutch. The kinetic coefficient governs slip.
- Assuming friction is constant. The coefficient falls as the lining heats, so a brake that works when
  cold may fade on a long descent.
- Ignoring heat when sizing a brake. The torque may be fine, while the rotor overheats on repeated stops.

## Go deeper

- [Design and Manufacturing I, lecture notes](https://ocw.mit.edu/courses/2-007-design-and-manufacturing-i-spring-2009/pages/lecture-notes/)
  by MIT OpenCourseWare: session notes on mechanisms, gears, and power transmission in machine design.
- [Design and Manufacturing I, course page](https://ocw.mit.edu/courses/2-007-design-and-manufacturing-i-spring-2009/)
  by MIT OpenCourseWare: the full course with its lecture and assignment materials.
- Related lessons: [Thermal systems](../thermal-fluid/01-thermal-systems.md) for heat flow from the
  rotor to the air, and [Shafts and bearings](../../design/08-shafts-and-bearings.md) for the shafts
  that carry the torque.
- [Applications reference](../reference.md): the lookup sheet for this topic.
