# Suspension and steering: springs, dampers, and Ackermann geometry

**Type:** lesson

A suspension keeps the tires on the road while the body carries the load and absorbs bumps. A steering system turns the front wheels so that the car follows the driver's chosen path. Engineers tune the spring and damper for ride comfort and grip, and they set the steering geometry so that the inner and outer wheels turn through the right angles in a corner.

**Prerequisites:** [Particle dynamics](../../physics/02-particle-dynamics.md), [Vibrations](../../physics/13-vibrations.md), [Rigid body dynamics](../../physics/03-rigid-body-dynamics.md), [Statics](../../physics/01-statics.md), [Trigonometry](../../math/02-trigonometry.md)
**Time:** 5-7 h

## Core ideas

### How it works

A spring stores energy when the wheel moves up over a bump, and it returns that energy as the wheel moves down. A spring alone keeps bouncing. A damper turns the motion of the spring into heat, so each bump dies out after a cycle or two. The tire is a spring too, and it sits between the wheel and the road.

Steering works through a linkage. The driver turns the steering wheel, a rack or a steering box moves a tie rod, and the tie rod turns each front wheel about its steering axis. Ackermann geometry sets the angles of the two front wheels, so the inner wheel turns more sharply than the outer wheel in a corner. Each wheel then rolls in its own circle, and the tires do not scrub sideways.

### Main parts

- **Coil spring:** a steel spring that carries the static weight of the body. Its stiffness $k$ sets the ride frequency.
- **Damper (shock absorber):** a piston moves through oil, and small valves in the piston set the damping force. Its damping coefficient $c$ sets how fast each oscillation dies.
- **Anti-roll bar:** a torsion bar that links the two wheels on one axle. It resists body roll in a corner, and it can stiffen the axle without making the ride harder over single bumps.
- **Control arms and links:** hold the wheel in place while it moves up and down. Their geometry sets camber change and roll center height.
- **Steering rack or steering box:** converts the rotation of the steering wheel into a sideways motion of the tie rods.
- **Tie rods and steering arms:** carry the force to the wheel hubs. The tie rod length sets the toe, which is the angle of the wheel as seen from above.

### Variants

- **MacPherson strut:** a spring and damper form one unit, and the wheel hub hangs from its lower end. It packs into little space and costs less, but it limits how the wheel can lean as it moves.
- **Double wishbone:** two control arms hold the wheel at the top and bottom. It keeps the camber and the track steady as the wheel moves, which suits sports cars.
- **Multi-link:** several separate links set the wheel position. It gives the designer control over each motion, and it costs more to build.
- **Solid axle with leaf springs or coil springs:** both wheels on an axle move together. It is strong and simple, and it is common on trucks and on the rear of some cars.
- **Rack and pinion steering:** a pinion meshes with a rack that moves the tie rods. It is light and direct, and most modern cars use it.
- **Electric power steering:** an electric motor adds torque to the steering shaft. It saves fuel compared with a hydraulic pump, and software can adjust the assist at each speed.

## Key equations

The ride and damping equations assume a linear spring and a linear viscous damper, small deflections, and a quarter-car model with one corner and no coupling to the other wheels. The Ackermann relation assumes rigid links, no tire slip, and small steering angles, so it gives the ideal geometry and not the real angles under load.

- **Ride frequency (quarter-car model):** $f_n = \dfrac{1}{2\pi} \sqrt{\dfrac{k}{m_s}}$, in Hz, where $k$ is the spring rate of one corner in N/m and $m_s$ is the sprung mass of that corner in kg. Typical passenger cars have $f_n$ from 1.0 to 1.5 Hz.
- **Critical damping:** $c_{crit} = 2\sqrt{k \, m_s}$, in N s/m.
- **Damping ratio:** $\zeta = c / c_{crit}$, dimensionless. Most road cars use $\zeta$ from 0.2 to 0.4, which gives a few bounces after a bump.
- **Wheel hop frequency:** $f_w = \dfrac{1}{2\pi} \sqrt{\dfrac{k_t}{m_u}}$, in Hz, where $k_t$ is the tire stiffness in N/m and $m_u$ is the unsprung mass (wheel, hub, brake, and part of the links) in kg. Typical values are 10 to 15 Hz.
- **Static deflection:** $\delta = m_s \, g / k$, in m, where $g$ is the local gravitational acceleration (9.81 m/s$^2$ at Earth's surface). The spring compresses by this much under the static load.
- **Ideal Ackermann relation:** $\cot\delta_{out} - \cot\delta_{in} = t / L$, where $\delta_{in}$ and $\delta_{out}$ are the inner and outer wheel angles in radians, $t$ is the track width in m, and $L$ is the wheelbase in m. The inner wheel has the larger angle.
- **Steering ratio:** $R_s = \theta_{wheel} / \delta_{road}$, dimensionless, where $\theta_{wheel}$ is the steering wheel angle and $\delta_{road}$ is the road wheel angle, both in the same unit. A ratio of 15:1 means that a 15 degree turn of the steering wheel turns the road wheels 1 degree.

## Worked example

**Given:** A quarter-car model of one front corner has a sprung mass $m_s = 400\ \text{kg}$, a spring rate $k = 30\ \text{kN/m}$, and a damping coefficient $c = 2078\ \text{N s/m}$. The unsprung mass is $m_u = 40\ \text{kg}$, and the tire stiffness is $k_t = 200\ \text{kN/m}$. The car has a wheelbase $L = 2.7\ \text{m}$ and a track $t = 1.5\ \text{m}$. The inner front wheel turns to $\delta_{in} = 25^\circ$. Gravity is $g = 9.81\ \text{m/s}^2$ (Earth surface).

**Find:** (a) the ride frequency, (b) the damping ratio, (c) the wheel hop frequency, (d) the static deflection of the spring, and (e) the outer wheel angle.

**Solution:**

1. Ride frequency: $f_n = \dfrac{1}{2\pi}\sqrt{30000 / 400} = 1.38\ \text{Hz}$.
2. Critical damping: $c_{crit} = 2\sqrt{30000 \times 400} = 6928\ \text{N s/m}$. Damping ratio: $\zeta = 2078 / 6928 = 0.30$.
3. Wheel hop: $f_w = \dfrac{1}{2\pi}\sqrt{200000 / 40} = 11.25\ \text{Hz}$.
4. Static deflection: $\delta = 400 \times 9.81 / 30000 = 0.131\ \text{m}$, which is 131 mm.
5. Outer wheel angle: $\cot\delta_{out} = \cot 25^\circ + 1.5 / 2.7 = 2.1445 + 0.5556 = 2.7001$, so $\delta_{out} = \arctan(1 / 2.7001) = 20.3^\circ$.

**Answer:** (a) 1.38 Hz. (b) $\zeta = 0.30$. (c) 11.3 Hz. (d) 131 mm. (e) 20.3 degrees.

**Sanity check:** The ride frequency of 1.38 Hz falls in the typical 1.0 to 1.5 Hz band, and $\zeta = 0.30$ sits inside the 0.2 to 0.4 band. The wheel hop frequency is about eight times the ride frequency, which keeps the two modes separate. The outer angle is smaller than the inner angle, as the geometry requires, and the difference of about 5 degrees is what a 2.7 m wheelbase with a 1.5 m track gives.

## Design trade-offs

- **Ride against handling:** a soft spring and a low damping ratio give a smooth ride over bumps. A stiffer setup keeps the body flatter in corners and reduces wheel travel, but it jars the occupants over small bumps.
- **Damping against comfort:** heavy damping keeps the tire on the road over rough surfaces. Too much damping makes the spring act like a rigid link, so the ride feels harsh.
- **Unsprung mass against bump control:** lighter wheels and brakes let the tire follow the road more closely. Heavier wheels move more and cost grip on rough roads.
- **Steering feel against effort:** a low steering ratio gives a quick response, and a high ratio gives a light, stable feel. Power steering reduces effort at parking speeds without making highway steering too light.
- **Packaging against geometry:** a MacPherson strut saves space in the engine bay, and a double wishbone gives better camber control. The designer picks the one that fits the car's mission and its cost.

## How it fails

- **Worn dampers:** the oil leaks past the seals, the damping drops, and the car bounces after each bump. Warning signs are oil on the shock body, a nose-dive under braking, and tires that wear in cups.
- **Broken springs:** a fatigue crack grows from a surface flaw, and the spring sags or breaks. A sagging spring lowers one corner of the car and changes the steering geometry.
- **Worn ball joints or tie rod ends:** play in the joints lets the wheel move under load. The driver feels wander and vague steering, and the tires wear unevenly.
- **Steering rack leaks or a failed pump:** hydraulic power steering loses assist. The driver must turn the wheel with far more effort.
- **Misalignment:** a wrong toe or camber setting wears the tires quickly and pulls the car to one side. Alignment checks and tolerance limits on the tie rods guard against it.

### Spring service hazard

A compressed coil spring stores energy. Removing a strut without compressing the spring first can release that energy suddenly and throw parts or injure a hand. The hierarchy of controls applies here. Elimination means not removing the spring when a complete strut assembly can be swapped instead. Substitution means using a pre-assembled strut with a factory-compressed spring. Engineering controls are a spring compressor with a guard and a safety catch, and a bench vise that holds the strut. Administrative controls are a written procedure, a second person in the room, and training. Personal protective equipment is safety glasses and gloves.

Lockout and tagout for suspension work means the following. Isolate the car by removing the key and disconnecting the battery if the work involves electronic dampers or active suspension. Release or restrain stored energy by compressing each spring with a rated compressor and holding it before any bolt is removed. Verify a zero-energy state by confirming that the spring tension is off the strut before the final bolt comes out, and by checking that the car is supported on stands before work begins.

## History

Ackermann steering geometry takes its name from Rudolph Ackermann, who held an English patent for it in about 1818. The geometry is also credited to Georg Lankensperger, a carriage maker in Munich, who used it in horse-drawn carriages. Robert William Thomson patented a pneumatic tire in 1845, and John Boyd Dunlop patented a pneumatic bicycle tire in Belfast in 1888. The coil spring and the leaf spring carried carriages long before the car, and the damper followed as cars grew faster.

## Practice

Where a problem needs gravitational acceleration, use $g = 9.81\ \text{m/s}^2$ (Earth surface).

1. A corner has a spring rate $k = 25\ \text{kN/m}$ and a sprung mass of 350 kg. Find the ride frequency in Hz.
2. For the corner in problem 1, find the critical damping coefficient in N s/m.
3. A car has a wheelbase of 2.5 m and a track of 1.4 m. The inner wheel turns to 30 degrees. Find the outer wheel angle in degrees, using the ideal Ackermann relation.
4. A 400 kg sprung mass sits on a spring of rate $k = 30\ \text{kN/m}$. Find the static deflection in mm.
5. A steering wheel turns 720 degrees, and the steering ratio is 15:1. Find the road wheel angle in degrees.

<details><summary>Answers</summary>

1. $1.35\ \text{Hz}$, from $\dfrac{1}{2\pi}\sqrt{25000 / 350} = 1.345\ \text{Hz}$.
2. $5916\ \text{N s/m}$, from $2\sqrt{25000 \times 350} = 5916\ \text{N s/m}$.
3. $23.6^\circ$, from $\cot\delta_{out} = \cot 30^\circ + 1.4 / 2.5 = 1.7321 + 0.5600 = 2.2921$, so $\delta_{out} = \arctan(1 / 2.2921) = 23.6^\circ$.
4. $131\ \text{mm}$, from $400 \times 9.81 / 30000 = 0.131\ \text{m}$.
5. $48^\circ$, from $720 / 15 = 48^\circ$.

</details>

## Common mistakes

- Using the sprung mass as the total car mass in the ride frequency. The formula uses the mass that the spring carries at one corner.
- Mixing up the inner and outer angles in the Ackermann relation. The inner wheel has the larger angle, so the outer angle is smaller.
- Treating the damping ratio as the damping coefficient. $\zeta$ is dimensionless, and $c$ has units of N s/m.
- Assuming that a stiffer spring always gives better handling. Stiffness also raises the ride frequency and can make the tire lose contact on rough roads.
- Forgetting that the steering ratio applies to the wheel angle, not to the rack travel. The rack travel depends on the steering arm length as well.

## Go deeper

- [University Physics Volume 1, Chapter 15 (oscillations)](https://openstax.org/books/university-physics-volume-1/pages/15-introduction) by OpenStax: simple harmonic motion and damped oscillations, the basis for the ride frequency and damping ratio.
- Reference sheets: [Mechanics reference](../../physics/reference-mechanics.md) for the vibration and force relations, and [Design reference](../../design/reference.md) for the design vocabulary.
- Related lessons: [Vibrations](../../physics/13-vibrations.md), [Cars](02-cars.md), [Electric vehicles](04-electric-vehicles.md), [Differentials and transmissions](../power-transmission/06-differentials-and-transmissions.md).
