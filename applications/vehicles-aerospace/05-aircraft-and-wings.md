# Aircraft and wings

**Type:** lesson

An **aircraft** is a flying machine that stays up because its wings make lift. A wing sized wrong can stall too early or cost too much engine power to fly, so engineers must check it first.

An engineer sizes the wing to set the stall speed, the cruise drag, and the power the engine must supply to pay for the drag of the wings and body.

**Prerequisites:** [Hydrostatics and Bernoulli](../../physics/10-hydrostatics-and-bernoulli.md), [Particle dynamics](../../physics/02-particle-dynamics.md), [Rigid body dynamics](../../physics/03-rigid-body-dynamics.md)
**Time:** 8-10 h

## Core ideas

### How it works

A wing sits in moving air and turns the air downward. The wing's shape and its angle to the flow set how much air it turns. The air pushes back on the wing, and that reaction is **lift**. Newton's third law explains the push, and the pressure picture explains where the force comes from. The air above the wing speeds up and its pressure drops, while the air below stays closer to free-stream pressure. The pressure difference acts over the wing area, and its total is the lift.

A common explanation says the air over the top must cover a longer path and so must move faster to meet the air below at the trailing edge. That claim is wrong. The air over the top moves faster than the equal-transit-time story predicts, and nothing forces the two streams to meet at the trailing edge.

Four forces act on an aircraft. Lift acts up, weight acts down, thrust acts forward, and drag acts backward. In steady level flight, lift equals weight and thrust equals drag. Climbing, descending, and turning all change these balances. In a turn, the wing must make more lift than the aircraft's weight.

The **angle of attack** $\alpha$ is the angle between the wing chord line and the oncoming air. Lift rises with angle of attack until the flow separates from the upper surface. Past that point, lift drops quickly. This event is a stall.

### Main parts

- **Wing.** Makes most of the lift. The wing's planform, airfoil section, and span set its lift and drag.
- **Flaps.** Hinged panels on the trailing edge. Flaps raise the maximum lift coefficient, so the aircraft can fly slower on approach. They also add drag.
- **Ailerons.** Hinged panels on the outer trailing edges that roll the aircraft by changing lift on each wing.
- **Horizontal stabilizer and elevator.** The tail surfaces that set pitch and give static pitch stability.
- **Vertical fin and rudder.** Give yaw stability and turn the aircraft about the vertical axis.
- **Fuselage.** Carries the payload and connects the wing and tail. It adds drag and some lift.

### Variants

- **Gliders.** Very high aspect ratio wings, often 25 to 40 or more. The drag is very low, so the glider can travel far for each meter it loses in height.
- **General aviation aircraft.** Light, low-speed aircraft with straight, fairly thick wings and flaps. They fly at stall speeds near 80 to 100 km/h.
- **Airliners.** Swept wings with high aspect ratio, typically around 8 to 11. Sweep delays the drag rise near the speed of sound, and high-lift devices handle takeoff and landing.
- **Fighter jets.** Low aspect ratio, often with delta wings or leading-edge extensions. The high thrust-to-weight ratio, not the wing, gives most of the performance.
- **Flying wings.** No separate tail. The wing carries both lift and stability, which needs careful design of the airfoil and the center of gravity.

## Key equations

Lift and drag. Both depend on **dynamic pressure**, $q = \tfrac{1}{2}\rho V^2$.

$$
L = \tfrac{1}{2}\rho V^2 S\, C_L \qquad D = \tfrac{1}{2}\rho V^2 S\, C_D
$$

- $L$ is lift (N). $D$ is drag (N). $\rho$ is air density ($\text{kg/m}^3$, about 1.225 at sea level on Earth). $V$ is airspeed (m/s). $S$ is wing area ($\text{m}^2$). $C_L$ and $C_D$ are the lift and drag coefficients (dimensionless).
- Assumptions: steady flight, subsonic and incompressible air, and $C_L$ and $C_D$ both referenced to the same wing area $S$.

**Stall speed**, where lift equals weight at the maximum lift coefficient.

$$
V_s = \sqrt{\frac{2W}{\rho\, S\, C_{L,\max}}}
$$

- $V_s$ is stall speed (m/s). $W = mg$ is weight (N), with $m$ in kg and $g = 9.81$ $\text{m/s}^2$ near Earth's surface. $C_{L,\max}$ is the maximum lift coefficient (dimensionless). The stall speed rises with the square root of the load factor $n$ in a turn, because lift must equal $nW$.
- Assumptions: steady, unaccelerated flight at the stall point, a load factor of 1 (level flight) unless the text says otherwise, and $C_{L,\max}$ set for the configuration in use.

**Induced drag**, which comes from the lift itself, and total drag.

$$
C_{D,i} = \frac{C_L^2}{\pi\, e\, \mathrm{AR}} \qquad C_D = C_{D,0} + C_{D,i} \qquad \mathrm{AR} = \frac{b^2}{S}
$$

- $C_{D,i}$ is induced drag coefficient. $C_{D,0}$ is zero-lift drag coefficient, which covers form drag and skin friction. $e$ is the **Oswald efficiency factor**, typically 0.7 to 0.85 (typical value). $\mathrm{AR}$ is **aspect ratio** (dimensionless). $b$ is wingspan (m).
- Assumptions: subsonic, steady flow. The factor $e$ folds the real lift distribution into one number, and $e = 1$ would be the elliptical lift distribution, which is the lowest induced drag for a given span and lift.

Thin-airfoil lift slope, valid below the stall.

$$
C_L \approx 2\pi(\alpha - \alpha_{L=0})
$$

- $\alpha$ is angle of attack in radians. $\alpha_{L=0}$ is the zero-lift angle, which is zero for a symmetric airfoil (then $C_L \approx 2\pi\alpha$) and negative for a cambered airfoil. A real wing gives a little less lift than this ideal value.
- Assumptions: thin airfoil (symmetric or cambered, through $\alpha_{L=0}$), inviscid and incompressible flow, small angle of attack, and flow attached below the stall.

Power required in level flight.

$$
P = D\, V
$$

- $P$ is power (W) at the propeller or engine shaft. This value ignores propeller losses and uses the drag at the given speed.
- Assumptions: steady, level, unaccelerated flight, so thrust equals drag, and the drag used is the total drag at that speed.

## Worked example

**Given.** A 1000 kg light aircraft flies at sea level on Earth, where $\rho = 1.225$ $\text{kg/m}^3$. Its maximum lift coefficient is $C_{L,\max} = 1.5$. The design target is a stall speed of 25 m/s. In cruise, the aircraft flies at 50 m/s with $C_{D,0} = 0.030$, aspect ratio $\mathrm{AR} = 8$, and $e = 0.80$.

**Find.** (a) the wing area, (b) the span, (c) the cruise drag and the power required, and (d) the lift-to-drag ratio.

**Assumptions.** Sea-level air, steady level flight, no flaps in cruise, and no propeller losses.

**Solution.**

1. Weight: $W = mg = 1000 \times 9.80665 = 9807$ N.
2. Wing area from the stall speed:
$$
S = \frac{2W}{\rho V_s^2 C_{L,\max}} = \frac{2 \times 9807}{1.225 \times 25^2 \times 1.5} = 17.08\ \text{m}^2
$$
3. Span: $b = \sqrt{\mathrm{AR}\, S} = \sqrt{8 \times 17.08} = 11.69$ m.
4. Cruise lift coefficient, so that lift equals weight at 50 m/s:
$$
C_L = \frac{2W}{\rho V^2 S} = \frac{2 \times 9807}{1.225 \times 50^2 \times 17.08} = 0.375
$$
5. Induced drag coefficient and total drag coefficient:
$$
C_{D,i} = \frac{0.375^2}{\pi \times 0.80 \times 8} = 0.00699 \qquad C_D = 0.03 + 0.00699 = 0.03699
$$
6. Drag and power:
$$
D = \tfrac{1}{2}\times 1.225 \times 50^2 \times 17.08 \times 0.03699 = 967\ \text{N} \qquad P = 967 \times 50 = 48.4\ \text{kW}
$$
7. Lift-to-drag ratio: $L/D = C_L / C_D = 0.375 / 0.03699 = 10.1$.

**Answer.** (a) $S = 17.1$ $\text{m}^2$. (b) $b = 11.7$ m. (c) $D = 967$ N, and the power required is $48.4$ kW (about 65 hp). (d) $L/D = 10.1$.

**Sanity check.** The cruise lift coefficient of 0.375 sits well below the maximum of 1.5, so the wing has margin before it stalls. A stall speed of 90 km/h is typical for a light aircraft. Lift to drag near 10 is a reasonable value for a light aircraft in cruise. Using the sea-level density at altitude would overstate the lift, so the design must check the density at the cruise altitude too.

## Design trade-offs

- **Aspect ratio.** A high aspect ratio cuts induced drag, which is why gliders and airliners use long, narrow wings. A long wing is heavier, needs more root bending strength, and does not fit in a hangar or at a gate. Fighter jets use low aspect ratio for agility and strength.
- **Wing loading.** Weight divided by wing area sets the stall speed. A smaller wing gives a higher stall speed and less drag. A larger wing gives a lower stall speed, more drag, and more weight. Designers pick a wing loading that matches the mission.
- **Flaps.** Flaps raise $C_{L,\max}$, which lowers the landing stall speed. They also add drag and mechanical complexity.
- **Sweep.** Swept wings delay the drag rise near the speed of sound, which matters for airliners at cruise Mach numbers near 0.8. Sweep also lowers $C_{L,\max}$ and adds weight, so airliners use flaps and slats for takeoff and landing.
- **Center of gravity.** The center of gravity must sit ahead of the neutral point for static stability. Too far forward costs performance, because the tail must push down harder. Too far aft makes the aircraft hard or impossible to control.

## How it fails

- **Stall.** When the flow separates from the upper surface, lift drops. A stall at low altitude is dangerous, and a stall in a turn can start a spin. Warning systems, such as stall warnings and stick shakers, alert the pilot before the stall. Stall speed margins and certification rules set limits on operations.
- **Tip stall.** A wing stalls first at the tips if the lift distribution is not designed well. A tip stall causes a roll-off that is hard to correct. Twist and taper move the stall inboard.
- **Icing.** Ice changes the wing shape, lowers $C_{L,\max}$, and raises drag. Warning signs include a higher stall speed and buffeting. Heated leading edges and de-icing boots are the safety measures.
- **Flutter.** A wing that bends and twists in phase with the air loads at high speed can oscillate and break. Designers check the flutter speed with analysis and ground vibration tests, and they keep a margin above the top operating speed.
- **Loss of control.** An aft center of gravity or a control surface failure can make an aircraft unstable or unresponsive. Redundant control paths and load limits on the tail reduce this risk.

## History

Otto Lilienthal made hundreds of glider flights in Germany in the 1890s. The Wright brothers made the first controlled, powered, sustained flight by a heavier-than-air machine on 17 December 1903 at Kill Devil Hills, North Carolina. Ludwig Prandtl described the boundary layer in 1904, which explained how friction shapes drag. In the early 1900s, Martin Kutta in Germany and Nikolai Zhukovsky in Russia developed the circulation theory of lift, which still underlies thin-airfoil analysis.

## Practice

1. A 1200 kg aircraft has a wing area of 18 $\text{m}^2$ and $C_{L,\max} = 1.6$ at sea level on Earth, where $\rho = 1.225$ $\text{kg/m}^3$. Find the stall speed in m/s.
2. An aircraft with $S = 18$ $\text{m}^2$ flies at 60 m/s at sea level with $C_L = 0.40$. Find the lift in kN.
3. Using thin-airfoil theory, find $C_L$ at $\alpha = 4^\circ$.
4. A wing has $C_L = 0.50$, $\mathrm{AR} = 9$, and $e = 0.80$. Find the induced drag coefficient.
5. An aircraft in level flight at 40 m/s has a drag of 800 N. Find the power required in kW.

<details><summary>Answers</summary>

1. $V_s = \sqrt{2 \times 1200 \times 9.80665 / (1.225 \times 18 \times 1.6)} = 25.8$ m/s
2. $L = \tfrac{1}{2} \times 1.225 \times 60^2 \times 18 \times 0.40 = 15\,900$ N, which is 15.9 kN
3. $C_L = 2\pi \times 0.0698 = 0.439$
4. $C_{D,i} = 0.50^2 / (\pi \times 0.80 \times 9) = 0.0111$
5. $P = 800 \times 40 = 32\,000$ W, which is 32 kW

</details>

## Common mistakes

- Using the equal-transit-time story to explain lift. The air over the top speeds up more than that story predicts, and the lift comes from the whole flow pattern and the turning of the air.
- Setting lift equal to weight in every flight phase. Lift equals weight only in steady level flight. In a climb, a descent, or a turn, the balance changes.
- Forgetting that stall speed rises with load factor. In a 60 degree bank, the load factor is 2 and the stall speed rises by a factor of $\sqrt{2}$, or about 41 percent.
- Treating $C_{L,\max}$ as fixed. Flaps, ice, dirt, and sweep all change it, so the stall speed in a design calculation must use the configuration that applies.
- Assuming a higher aspect ratio is always better. Induced drag falls, but the wing gets heavier, and the structure must carry the extra root bending moment.

## Go deeper

- [What is lift?](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/what-is-lift/) by NASA Glenn Research Center: how lift arises on a wing, from a plain-language starting point.
- [What is drag?](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/what-is-drag/) by NASA Glenn Research Center: form drag, skin friction, and induced drag.
- [Bernoulli's equation](https://www.grc.nasa.gov/www/k-12/airplane/bern.html) by NASA Glenn Research Center: the pressure and speed relation for airfoils and pitot tubes.
- Reference sheets: [Mechanics reference](../../physics/reference-mechanics.md) and [Thermofluids reference](../../physics/reference-thermofluids.md).
- [*University Physics Volume 1*, Chapter 14 (fluid dynamics)](https://openstax.org/books/university-physics-volume-1/pages/14-introduction) by OpenStax: fluids, pressure, and Bernoulli's equation.
- Related lessons: [Rotorcraft and drones](06-rotorcraft-and-drones.md), [Rockets](07-rockets.md), and [Gas turbines and jet engines](../thermal-fluid/07-gas-turbines-and-jet-engines.md).
