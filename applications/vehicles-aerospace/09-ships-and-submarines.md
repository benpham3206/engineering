# Ships and submarines

**Type:** lesson

**Ships and submarines** are vessels that float on water or travel beneath its surface.

> [!WARNING]
> A vessel that is poorly balanced can capsize at sea, which is why its shape must be designed with care.

A ship floats because the water it pushes aside weighs as much as the ship. It stays upright because its shape and weight distribution keep its center of buoyancy in the right place. Naval architects size hulls, check stability, and choose propulsion, and each of these choices changes the others.

**Prerequisites:** [Hydrostatics and Bernoulli](../../physics/10-hydrostatics-and-bernoulli.md), [Statics](../../physics/01-statics.md), [Rigid body dynamics](../../physics/03-rigid-body-dynamics.md)
**Time:** 8-12 h

## Core ideas

### How it works

**Archimedes' principle** says a body in a fluid feels an upward buoyant force equal to the weight of the fluid it displaces. A ship sinks until the displaced water weighs the same as the ship. This is the **displacement**. For a ship in equilibrium, the buoyant force equals the weight, and the two forces act along the same vertical line.

Stability is about rotation, not sinking. Two forces act on the hull. The weight acts at the **center of gravity** $G$. The buoyant force acts at the **center of buoyancy** $B$, which is the centroid of the submerged volume. When the ship heels, the shape of the submerged volume changes, and $B$ moves toward the low side. The buoyant force and the weight then form a couple that rights the ship if $G$ sits below the metacenter $M$. The **metacenter** is the point where the line of action of buoyancy crosses the centerline at small heel angles.

The **metacentric height** $\mathrm{GM}$ is the distance from $G$ up to $M$. A positive $\mathrm{GM}$ means the ship rights itself after a small heel. A negative $\mathrm{GM}$ means it capsizes. Designers aim for a $\mathrm{GM}$ large enough to resist heeling from wind, waves, and cargo, but not so large that the ship snaps back violently and stresses its structure.

Propulsion overcomes the hull resistance. Water resistance grows with speed, so most of the power goes into overcoming drag at high speed. A propeller converts engine torque into thrust by accelerating water backward.

### Main parts

- **Hull**: the watertight shell that carries the displacement. Its shape sets the drag and the waterplane area that controls stability.
- **Ballast**: water or heavy material placed to set the draft, trim, and center of gravity. Submarines use ballast tanks to dive and surface.
- **Propulsion**: engines, gearboxes, shafts, and propellers. Large ships often use slow-speed diesel engines with fixed-pitch propellers.
- **Steering**: the rudder and, on some ships, thrusters that turn the bow at low speed.
- **Compartments and bulkheads**: watertight subdivisions that limit flooding after damage.
- **Submarine pressure hull**: a sealed cylinder that holds the crew at one atmosphere while the outside water pressure rises with depth.

### Variants

- **Cargo ships**: long, wide hulls with large holds. Container ships and bulk carriers differ mainly in their hold layout.
- **Warships**: hulls shaped for speed, sensors, and weapons. Stability and damage control drive their subdivision.
- **Passenger ships and ferries**: stability is strict because passengers and vehicles shift weight quickly.
- **Submarines**: submerged most of the time. Their stability depends on the balance of buoyancy and ballast, and on depth control rather than a waterplane.
- **Small craft**: sailboats and planing boats use keels, ballast, and hull shape to balance sail forces.

## Key equations

Buoyant force on a body in water, in newtons (N):

$$F_B = \rho g V$$

where $\rho$ is the water density in kilograms per cubic metre ($\text{kg/m}^3$), $g$ is the local gravitational acceleration (9.81 $\text{m/s}^2$ at Earth's surface), and $V$ is the displaced volume in cubic metres ($\text{m}^3$). Typical seawater density is $\rho \approx 1025\ \text{kg}/\text{m}^3$, and fresh water is about $1000\ \text{kg}/\text{m}^3$.

For a ship in equilibrium, $F_B = \Delta g$, where $\Delta$ is the displacement mass in kilograms.

The metacentric height is:

$$\mathrm{GM} = \mathrm{KB} + \mathrm{BM} - \mathrm{KG}$$

where $\mathrm{KB}$ is the height of the center of buoyancy above the keel in metres (m), $\mathrm{KG}$ is the height of the center of gravity above the keel in metres, and $\mathrm{BM}$ is the distance from $B$ up to the metacenter in metres. For a ship with a rectangular waterplane of length $L$ and breadth $B_w$, $\mathrm{BM}$ is:

$$\mathrm{BM} = \frac{I}{V} = \frac{L B_w^3}{12 V}$$

where $I = L B_w^3 / 12$ is the second moment of the waterplane area about the centerline, in metres to the fourth power ($\text{m}^4$). For a box-shaped hull of draft $T$, the center of buoyancy sits at $\mathrm{KB} = T / 2$.

For a small transverse weight shift $w$ moved a distance $d$ across the deck, the heel angle $\theta$ in radians is approximately:

$$\theta \approx \frac{w \, d}{\Delta \, \mathrm{GM}}$$

where $w$ is the moved weight in newtons, $d$ is the transverse distance in metres, $\Delta$ is the displacement in newtons, and $\mathrm{GM}$ is in metres. This is valid for small angles, roughly up to 10 degrees.

## Worked example

**Given:** A box-shaped barge is 60 m long, 12 m wide, and has a draft of 3 m in seawater with $\rho = 1025\ \text{kg}/\text{m}^3$. Its center of gravity sits at $\mathrm{KG} = 3.2\ \text{m}$ above the keel. A 20 t cargo load is shifted 4 m across the deck.

**Find:** (a) the metacentric height $\mathrm{GM}$, and (b) the heel angle caused by the shifted cargo.

**Assumptions:** Rectangular hull with a flat keel. Constant water density. Shifted cargo is a point weight. No free-surface effect. Small angles, so the linear heel formula applies. Gravity is $g = 9.81\ \text{m}/\text{s}^2$ (Earth surface).

**Solution:**

1. Displaced volume: $V = L B_w T = 60 \times 12 \times 3 = 2160\ \text{m}^3$.
2. Displacement: $\Delta = \rho V = 1025 \times 2160 = 2.214 \times 10^{6}\ \text{kg}$, which is a weight of $21.7\ \text{MN}$.
3. Center of buoyancy: $\mathrm{KB} = T / 2 = 1.5\ \text{m}$.
4. Second moment of waterplane area: $I = L B_w^3 / 12 = 60 \times 12^3 / 12 = 8640\ \text{m}^4$.
5. Metacentric radius: $\mathrm{BM} = I / V = 8640 / 2160 = 4.0\ \text{m}$.
6. Metacentric height: $\mathrm{GM} = \mathrm{KB} + \mathrm{BM} - \mathrm{KG} = 1.5 + 4.0 - 3.2 = 2.3\ \text{m}$.
7. Weight shifted: $w = 20\,000 \times 9.81 = 196\ \text{kN}$. Heel: $\theta \approx \dfrac{196\,000 \times 4}{21.7\ \text{MN} \times 2.3\ \text{m}} = 0.0157\ \text{rad}$, which is $0.9^\circ$.

**Answer:** (a) $\mathrm{GM} = 2.3\ \text{m}$. (b) The heel angle is about $0.9^\circ$.

**Sanity check:** $\mathrm{GM}$ is positive, so the barge is stable. A heel of under one degree is small, which fits a $2.3$ m metacentric height on a $12$ m beam. If $\mathrm{KG}$ rose by $0.5$ m, $\mathrm{GM}$ would fall to $1.8$ m, and the same cargo would heel the barge by about $1.1^\circ$. Stability falls as $\mathrm{KG}$ rises, so high loads cost margin.

## Design trade-offs

- **Stability against comfort**: a large $\mathrm{GM}$ resists heeling, but it gives a short, stiff roll that throws cargo and passengers around. Passenger ships aim for a moderate value.
- **Beam against resistance**: a wide hull has a large waterplane and high stability, but it adds wetted surface and drag. Long, narrow hulls are fast but less stable.
- **Draft against port access**: a deep draft increases displacement and carrying capacity, but it limits harbors and channels.
- **Propeller size against noise and vibration**: a large, slow propeller is efficient, but a small, fast one causes cavitation, noise, and hull vibration.
- **Submarine depth against hull weight**: deeper dives need a thicker pressure hull. Its weight, and the ballast needed to balance it, grows fast with depth.
- **Subdivision against usable space**: more watertight bulkheads save the ship after a breach, but they take space that could carry cargo or passengers.

## How it fails

- **Capsize from low stability**: a high $\mathrm{KG}$, free water in a tank, or cargo that shifts reduces $\mathrm{GM}$. Free-surface effect is a common cause, because liquid moving in a partly full tank shifts the center of gravity.
- **Flooding**: a breach in the hull admits water. Bulkheads, watertight doors, and pumps limit the flooding. Ships need enough margin that a damaged compartment still leaves them afloat and stable.
- **Overloading**: exceeding the design draft or load line reduces freeboard and margin. Load line marks and loading computers prevent it.
- **Cavitation**: low pressure at a propeller blade forms vapor bubbles that collapse on the blade. This erodes the blade surface, causes noise, and lowers thrust.
- **Hull fatigue**: waves bend the hull over its life. Cracks grow at welds and hatch corners. Inspection schedules and design details at stress points reduce the risk.
- **Submarine implosion**: the pressure hull fails if the outside water pressure exceeds its strength. Designers set a test depth well above the operating depth, and depth limits protect the crew.

## History

Archimedes described the principle of buoyancy in the third century BC. Pierre Bouguer studied ship stability in the 18th century and developed the metacenter as the key stability point. David Bushnell built the *Turtle* in 1775, an early one-person submarine, and used it against a British warship in New York Harbor in 1776. Ships grew from wood to iron and then steel during the 19th century, which allowed larger, stronger hulls and watertight compartments.

## Practice

Where a problem needs gravitational acceleration, use $g = 9.81\ \text{m}/\text{s}^2$ (Earth surface).

1. A box-shaped hull has length 40 m, breadth 10 m, and draft 2 m in seawater with $\rho = 1025\ \text{kg}/\text{m}^3$. Find its displaced volume in cubic metres.
2. The same hull has $\mathrm{KG} = 1.8\ \text{m}$. Find $\mathrm{KB}$, $\mathrm{BM}$, and $\mathrm{GM}$.
3. A submarine has a displaced volume of $3000\ \text{m}^3$ in seawater. Find the buoyant force in meganewtons (MN).
4. The barge in the worked example has $\mathrm{GM} = 2.3\ \text{m}$ and a displacement of $21.7\ \text{MN}$. A 10 t weight moves 3 m across the deck. Find the heel angle in degrees.
5. Explain why a ship with $\mathrm{GM}$ slightly above zero can still feel stiff in rough seas, and why a very large $\mathrm{GM}$ is not always better.

<details><summary>Answers</summary>

1. $V = 40 \times 10 \times 2 = 800\ \text{m}^3$
2. $\mathrm{KB} = 1.0\ \text{m}$, $\mathrm{BM} = I / V = (40 \times 10^3 / 12) / 800 = 4.17\ \text{m}$, and $\mathrm{GM} = 1.0 + 4.17 - 1.8 = 3.37\ \text{m}$
3. $F_B = 1025 \times 9.81 \times 3000 = 30.2\ \text{MN}$
4. $w = 10\,000 \times 9.81 = 98.1\ \text{kN}$. Then $\theta \approx 98\,100 \times 3 / (2.172 \times 10^{7} \times 2.3) = 0.0059\ \text{rad}$, which is about $0.3^\circ$.
5. A small positive $\mathrm{GM}$ keeps the ship upright but gives a slow, soft roll. A very large $\mathrm{GM}$ gives a fast, stiff roll that loads the hull and cargo harder and throws passengers around.

</details>

## Common mistakes

- Forgetting the cube on the breadth in the waterplane inertia. For a rectangle, $I = L B_w^3 / 12$.
- Measuring $\mathrm{KG}$ from the waterline instead of the keel. The metacentric formula needs all heights from the same datum.
- Ignoring free-surface effect when a tank is partly full. Liquid moving in a tank lowers the effective $\mathrm{GM}$.
- Assuming a larger $\mathrm{GM}$ is always safer. Excess $\mathrm{GM}$ makes a ship roll stiffly and can overstress the structure and its fittings.
- Using the hull's freshwater draft in seawater. Seawater is denser, so the same ship floats higher.

## Go deeper

- [*University Physics Volume 1*](https://openstax.org/books/university-physics-volume-1/pages/1-introduction) by OpenStax: a free introductory textbook covering fluid statics and buoyancy. It is licensed CC BY-NC-SA.
- [MIT OpenCourseWare](https://ocw.mit.edu/): free lecture notes, exams, and videos from MIT, with no registration required. Search for courses on ship hydrostatics and naval architecture.
- Related: [Hydrostatics and Bernoulli](../../physics/10-hydrostatics-and-bernoulli.md), [Hydraulics and pneumatics](../machines-robots/07-hydraulics-and-pneumatics.md), [Pumps](../thermal-fluid/09-pumps.md), [Pressure vessels and tanks](../structures/03-pressure-vessels-and-tanks.md), [Factor of safety and failure](../../design/07-factor-of-safety-and-failure.md).
- [Applications reference](../reference.md): the lookup sheet for this topic.
