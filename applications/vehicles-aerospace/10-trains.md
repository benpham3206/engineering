# Trains

**Type:** lesson

A train moves on steel wheels over steel rails, and the only thing that pushes or stops it is the small contact patch under each wheel. Engineers design traction, braking, and signaling around that contact, because a train that cannot grip the rail can neither accelerate nor stop on time. Signaling keeps trains apart, so a train never runs into the one ahead.

**Prerequisites:** [Particle dynamics](../../physics/02-particle-dynamics.md), [Statics](../../physics/01-statics.md)
**Time:** 6-10 h

## Core ideas

### How it works

A wheel rolls on a rail. The wheel and rail touch over a patch only a few millimetres across, so the whole weight of the train passes through a few small contact patches. Friction at these patches provides the force that accelerates and brakes the train. This friction is called adhesion, and its coefficient $\mu$ is typically about 0.25 when the rail is dry and lower when it is wet or contaminated.

A steel wheel has a slightly conical tread. When the axle moves off center, one wheel rolls on a larger radius than the other, and the axle steers back to the middle. This self-centering keeps the train on the track in a straight line.

Traction motors turn the driven axles through gearboxes. The motor torque sets the force the wheel tries to deliver, but the adhesion sets the most force the rail will accept. If the motor asks for more than adhesion allows, the wheel slips and spins. Modern trains detect slip and reduce torque.

Braking uses friction brake blocks or discs, electric regenerative braking that feeds energy back to the line, or both. The same adhesion limit applies. Air brakes, first made practical by George Westinghouse, use compressed air to apply the brakes, and a loss of air pressure applies them automatically. This fail-safe design is why air brakes remain standard.

### Main parts

- **Wheels and axles**: steel wheels with conical treads, pressed or fixed to axles. Axle loads set the force each wheel can carry.
- **Rails**: steel rails on sleepers, with ballast or a concrete slab beneath. Standard gauge is 1435 mm.
- **Bogies**: frames under the car that carry the wheels and steer the axles through curves.
- **Traction system**: a motor, inverter, and gearbox on driven axles. Diesel-electric locomotives use a diesel engine to drive a generator.
- **Brakes**: friction brakes on wheels or discs, electric regenerative braking, and the air or electronic control that operates them.
- **Signaling and train control**: track circuits detect where trains are. Signals and onboard systems tell the driver the safe speed and when to stop.

### Variants

- **Electric trains**: power from an overhead wire, often 25 kV AC at 50 Hz on many lines, or a third rail. They accelerate quickly and suit urban and intercity service.
- **Diesel-electric locomotives**: a diesel engine runs a generator that powers traction motors. They need no overhead wire.
- **High-speed trains**: high power per axle, very smooth track geometry, and advanced braking. Speeds above 300 km/h need careful design of the pantograph and overhead wire.
- **Freight trains**: heavy loads and long lengths. Brakes must act along the whole train, and the air or electronic braking system is tested before each run.
- **Metro and light rail**: short trains with frequent stops. Fast acceleration and short headways drive their design.

## Key equations

Force on a train from adhesion, in newtons (N):

$$F_{\max} = \mu W_d$$

where $\mu$ is the adhesion coefficient (dimensionless) and $W_d$ is the weight on the driven axles in newtons (N). This is the most tractive force the rails will accept. Braking force is limited in the same way.

Newton's second law for a train, with mass $m$ in kilograms and acceleration $a$ in metres per second squared:

$$F = m a$$

The braking distance at constant deceleration $a$ from speed $v$ is:

$$s = \frac{v^2}{2 a}$$

where $s$ is the distance in metres, $v$ is the speed in metres per second (m/s), and $a$ is the deceleration in m/s$^2$. Adhesion limits the deceleration. The required adhesion coefficient is $\mu_{\text{req}} = a / g$, where $g$ is the local gravitational acceleration (9.81 m/s$^2$ at Earth's surface).

During brake build-up, the train travels at constant speed before braking takes full effect. That distance is $s_d = v t_d$, where $t_d$ is the delay in seconds.

## Worked example

**Given:** A 400 t train runs at 120 km/h on dry rail. It brakes at a service deceleration of $a = 0.9\ \text{m}/\text{s}^2$, which is an assumed design value. The brake build-up delay is $t_d = 3\ \text{s}$, also an assumed value. The adhesion coefficient for dry rail is $\mu = 0.25$, a typical value.

**Find:** (a) the braking force, (b) the adhesion needed to hold that deceleration, and (c) the total stopping distance from the moment the driver applies the brakes.

**Assumptions:** Level track. Constant deceleration after brake build-up. Mass constant during braking. Gravity is $g = 9.81\ \text{m}/\text{s}^2$ (Earth surface).

**Solution:**

1. Speed: $v = 120 / 3.6 = 33.3\ \text{m/s}$.
2. Braking force: $F = m a = 400\,000 \times 0.9 = 360\ \text{kN}$.
3. Adhesion needed: $\mu_{\text{req}} = a / g = 0.9 / 9.81 = 0.092$.
4. Adhesion available: $\mu_{\max} g = 0.25 \times 9.81 = 2.45\ \text{m}/\text{s}^2$, which is well above $0.9\ \text{m}/\text{s}^2$.
5. Braking distance: $s = v^2 / (2a) = 33.3^2 / (2 \times 0.9) = 617\ \text{m}$.
6. Build-up distance: $s_d = 33.3 \times 3 = 100\ \text{m}$.
7. Total stopping distance: $617 + 100 = 717\ \text{m}$.

**Answer:** (a) 360 kN. (b) About 0.092, which is well within the available adhesion. (c) About 717 m.

**Sanity check:** A stopping distance of about 700 m for a fast heavy train is consistent with the long braking distances that trains need. The required adhesion of 0.092 is far below the 0.25 available, so the wheels will not slide at this deceleration. A large braking force needs a high adhesion coefficient, so the check matters more on wet rail.

## Design trade-offs

- **Axle load against track damage**: heavier axles carry more freight, but they strain the rail, sleepers, and bridges. Limits on axle load protect the track.
- **Braking power against wheel and rail wear**: friction brakes heat the wheel and wear the tread. Regenerative braking reduces wear but needs a line that can use the energy.
- **Speed against curvature and cant**: higher speed needs gentler curves and a banked track, called cant, which tilts the track to balance the forces on a curve.
- **Signaling density against cost**: closer spacing of trains needs more signals and faster communication. Automatic train protection systems add safety and cost.
- **Train length against platform and signal limits**: long trains carry more people or freight, but they need longer platforms and sidings.

## How it fails

- **Wheel slip**: too much torque or wet rail drops adhesion, and the wheel slides. Slip control and sanding reduce the risk.
- **Wheel slide under braking**: locked wheels flatten a spot on the tread, which causes vibration and damage. Anti-skid brake systems release the brakes before a wheel locks.
- **Derailment**: a worn wheel profile, a broken rail, a track fault, or excessive speed in a curve can cause a derailment. Inspection, rail testing, and speed limits protect against it.
- **Signal passed at danger**: a driver can miss a signal, or a fault can display the wrong aspect. Automatic train protection applies the brakes when the train passes a stop signal.
- **Brake failure**: a leak in the air brake line drops the pressure, and the brakes apply automatically. This is the fail-safe that makes air brakes the standard.
- **Fatigue cracks in wheels and axles**: repeated loading grows cracks. Ultrasonic inspection and scheduled wheelset replacement find cracks before they fail.

## History

George and Robert Stephenson's locomotive Rocket won the Rainhill Trials in 1829 for the Liverpool and Manchester Railway. Stephenson's early lines used a track width of 1435 mm, which became the standard gauge. George Westinghouse patented an air brake in 1869 and the automatic, fail-safe version in the early 1870s, and it made stopping long trains safe. Werner von Siemens built an electric locomotive that ran at the Berlin Trades Exhibition in 1879, which showed that electric traction could work on a railway.

## Practice

Where a problem needs gravitational acceleration, use $g = 9.81\ \text{m}/\text{s}^2$ (Earth surface).

1. A 200 t train runs at 25 m/s. Find its kinetic energy in megajoules. Use $E = \tfrac{1}{2} m v^2$.
2. A train has 1.5 MN on its driven axles, and $\mu = 0.30$. Find the maximum tractive force in kilonewtons.
3. A train at 160 km/h brakes at $0.8\ \text{m}/\text{s}^2$ with no delay. Find the braking distance in metres.
4. A train of mass 400 t brakes at $0.9\ \text{m}/\text{s}^2$ on wet rail with $\mu = 0.10$. Is the deceleration within the adhesion limit? Show your check.
5. Explain why a derailment on a curve depends on speed, cant, and wheel profile together, and name one measure that reduces each risk.

<details><summary>Answers</summary>

1. $E = 0.5 \times 200\,000 \times 25^2 = 62.5\ \text{MJ}$
2. $F_{\max} = 0.30 \times 1.5\ \text{MN} = 450\ \text{kN}$
3. $s = (160/3.6)^2 / (2 \times 0.8) = 1235\ \text{m}$
4. $\mu_{\text{req}} = 0.9 / 9.81 = 0.092$, and $\mu = 0.10$ is greater than $0.092$. The deceleration is just within the adhesion limit, with little margin.
5. Speed, cant, and wheel profile set the lateral force on the wheel. Lower speed or more cant reduces that force, and a well-maintained wheel profile keeps the wheel on the rail.

</details>

## Common mistakes

- Using speed in km/h in the braking distance formula. Convert to m/s first.
- Treating adhesion as a fixed number. Wet, oily, or leaf-covered rail can drop it by half or more.
- Ignoring the brake build-up delay. Stopping distances in signaling design must include it.
- Assuming a train can brake at any deceleration the driver asks for. The adhesion limit caps it.
- Calling the steel wheel and rail a simple rolling contact with no friction. Traction and braking depend on the friction at the contact patch.

## Go deeper

- [University Physics Volume 1](https://openstax.org/books/university-physics-volume-1/pages/1-introduction) by OpenStax: a free introductory textbook on Newton's laws, friction, work, and energy. It is licensed CC BY-NC-SA.
- [MIT OpenCourseWare](https://ocw.mit.edu/): free lecture notes, exams, and videos from MIT, with no registration required. Search for courses on dynamics and transportation systems.
- Related: [Cars](02-cars.md), [Electric vehicles](04-electric-vehicles.md), [Gear trains](../power-transmission/01-gear-trains.md), [Brakes and clutches](../power-transmission/04-clutches-and-brakes.md), [Factor of safety and failure](../../design/07-factor-of-safety-and-failure.md), [Mechanical properties](../../materials/03-mechanical-properties.md).
- [Applications reference](../reference.md): the lookup sheet for this topic.
