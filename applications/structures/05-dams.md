# Dams

**Type:** lesson

A dam holds back water and turns a river or valley into a reservoir. An engineer must make sure the dam stays in place under the push of the water, its own weight, uplift from water under its base, floods, and earthquakes.

**Prerequisites:** [Statics](../../physics/01-statics.md), [Hydrostatics and Bernoulli](../../physics/10-hydrostatics-and-bernoulli.md), [Factor of safety and failure](../../design/07-factor-of-safety-and-failure.md)
**Time:** 6-8 h

## Core ideas

### How it works

Water pushes on the upstream face of the dam. The pressure grows with depth, so the lower part of the wall takes far more load than the top. The dam resists that push with its own weight, with friction on its base, or with the arch action of its shape.

Engineers check three things. The dam must not slide along its base. It must not overturn. It must not crush or crack the foundation under it. This lesson works through overturning in detail.

The steps run as follows:

1. Water pressure at depth $h$ is $p = \rho g h$. Pressure rises in a straight line from zero at the surface to a maximum at the base.
2. The pressure adds up to one horizontal force per metre of dam length. That force acts at height $H/3$ above the base, which is a depth of $2H/3$ below the free surface.
3. The dam's weight pushes down through its centre of mass. Multiplied by its lever arm about the downstream toe, the weight resists tipping. Uplift from water under the base pushes up and reduces the net resisting force.
4. The base spreads the load into the rock or soil. The stress at the base must stay below what the foundation can carry.

### Main parts

- **Upstream face:** the wet side. It is usually vertical or only slightly sloped.
- **Downstream face:** sloped on a gravity dam, which gives the wall a triangular cross-section.
- **Crest:** the top of the dam. It often carries a road.
- **Foundation and grout curtain:** the contact with rock. Grout injected into cracks in the rock cuts seepage.
- **Drains and galleries:** drain holes and inspection passages inside the concrete. They relieve uplift pressure.
- **Spillway:** the channel that passes floods over or around the dam.
- **Outlet works:** gates and pipes that release water for use or to lower the reservoir.
- **Instruments:** piezometers, which measure water pressure inside the dam and foundation, plus survey points and seepage meters that track movement over years.

### Variants

- **Gravity dam:** a concrete or masonry wall that stands by its weight. Its cross-section is a triangle. It suits wide valleys with solid rock foundations.
- **Arch dam:** a curved wall that pushes against the valley sides. It uses much less concrete than a gravity dam of the same height, but it needs a narrow canyon with strong abutments.
- **Arch-gravity dam:** a hybrid. Hoover Dam on the Colorado River is an example.
- **Embankment dam:** built from compacted earth or rock fill, with an impervious core or face that stops seepage. It suits soft foundations, where concrete would cost too much.

## Key equations

Hydrostatic pressure at depth $h$:

$$p = \rho g h$$

Assumes the water is at rest and incompressible, and that $p$ is gauge pressure above the free surface. Here $p$ is pressure in pascals (Pa), $\rho$ is the water density in kilograms per cubic metre (about $1000\ \text{kg/m}^3$ for fresh water, typical), $g = 9.81\ \text{m/s}^2$, and $h$ is depth in metres.

Resultant water force per metre of dam length, for a vertical face with water depth $H$:

$$F_H = \tfrac{1}{2}\rho g H^2$$

Assumes still water, a vertical upstream face, and a dam that does not move under load. Here $F_H$ is in newtons per metre (N/m), and $H$ is the water depth in metres. The center of pressure acts horizontally at height $H/3$ above the base, which is a depth of $2H/3$ below the free surface.

Weight per metre of dam length for a triangular gravity section:

$$W = \rho_c\, g\, A, \qquad A = \tfrac{1}{2} B H$$

Assumes uniform concrete density and a triangular section with a vertical upstream face. Here $\rho_c$ is the concrete density in kilograms per cubic metre (about $2400\ \text{kg/m}^3$, typical), $A$ is the cross-section area in square metres, and $B$ is the base width in metres.

Moments per metre of dam length, taken about the downstream toe:

$$M_R = W \cdot \tfrac{2}{3} B, \qquad M_O = F_H \cdot \tfrac{H}{3}$$

Assumes a rigid dam that rotates about the downstream toe, with no uplift and no tailwater. Both moments are in newton metres per metre (N m/m). $M_R$ resists tipping, and $M_O$ tips the dam. The centroid of the triangle sits $B/3$ from the upstream face, so its arm about the downstream toe is $B - B/3 = 2B/3$. That arm is positive, so the weight resists tipping.

The factor of safety against overturning assumes that the weight is the only restoring force, with no uplift, no tailwater, and no earthquake load.

$$FS_{ot} = \frac{M_R}{M_O}$$

For a triangular section with a vertical upstream face and no uplift, the two equations combine into one:

$$FS_{ot} = 2\,\frac{\rho_c}{\rho_w}\left(\frac{B}{H}\right)^2$$

Here $\rho_w$ is the water density in kilograms per cubic metre. The ratio $B/H$ is dimensionless.

## Worked example

**Given:** A gravity dam with a vertical upstream face holds water 30 m deep. The base is 18 m wide. Concrete density is $\rho_c = 2400\ \text{kg/m}^3$, and water density is $\rho_w = 1000\ \text{kg/m}^3$. Assume $g = 9.81\ \text{m/s}^2$, no uplift, no tailwater, and no earthquake load.

**Find:** the water force per metre of dam length, the overturning factor of safety, and the smallest base width that gives a factor of 1.5.

**Solution:**

1. Water force: $F_H = \tfrac{1}{2}(1000)(9.81)(30)^2 = 4.41 \times 10^6\ \text{N/m}$.
2. Overturning moment: the lever arm is $H/3 = 10\ \text{m}$, so $M_O = 4.41 \times 10^6 \times 10 = 4.41 \times 10^7\ \text{N m/m}$.
3. Dam weight: $W = 2400 \times 9.81 \times \tfrac{1}{2} \times 18 \times 30 = 6.36 \times 10^6\ \text{N/m}$.
4. Resisting moment: the lever arm is $2B/3 = 12\ \text{m}$, so $M_R = 6.36 \times 10^6 \times 12 = 7.63 \times 10^7\ \text{N m/m}$.
5. Factor of safety: $FS_{ot} = 7.63 \times 10^7 / 4.41 \times 10^7 = 1.73$.
6. Minimum base width for a factor of 1.5: $B = H\sqrt{FS\,\rho_w / (2\rho_c)} = 30\sqrt{1.5/4.8} = 16.8\ \text{m}$.

**Answer:** The water force is $4.41\ \text{MN/m}$. The overturning factor of safety is $1.73$, so the 18 m base passes a check at 1.5. The minimum base width for that check is $16.8\ \text{m}$.

**Sanity check:** The combined formula gives $FS = 2(2.4)(18/30)^2 = 1.73$, which matches the step-by-step result. The calculation ignores uplift. Uplift lowers the effective weight, so the real factor is smaller and the real base must be wider than $16.8\ \text{m}$. The water force also scales with the square of depth, so doubling the depth to 60 m raises the force four times.

## Design trade-offs

- **Concrete volume and cost:** a gravity dam's cross-section area is $\tfrac{1}{2}BH$. Base width must grow roughly with height, so the concrete volume per metre of crest grows with the square of height. Concrete is often the largest cost in the project.
- **Shape and site:** an arch dam uses far less concrete, but it needs a narrow valley with strong rock on both sides. A gravity dam tolerates a wider valley. An embankment dam uses local soil and rock, which suits weak foundations.
- **Uplift control:** drains cut the uplift pressure under the base. A grout curtain cuts seepage. Both raise the factor of safety without adding concrete.
- **Flood capacity:** the spillway must pass the design flood safely. A larger design flood lowers the risk of overtopping, but it costs more gates and channel.
- **Earthquake loads:** ground shaking pushes the dam sideways and can shift the water load. Designs in seismic regions add checks for that load.
- **Sediment:** rivers carry sediment into the reservoir for decades. The storage volume shrinks over time, and outlet intakes can clog.

## How it fails

- **Overturning:** the dam rotates about its downstream toe. Warning signs include cracks that open at the upstream heel. The base width and the position of the resultant force guard against it.
- **Sliding:** the water force overcomes the friction on the base. Shear keys cut into the rock and drained foundations resist sliding.
- **Foundation failure:** weak or fractured rock gives way under the load. The St. Francis Dam in California failed in March 1928 after problems in the rock beneath and beside it. The flood killed hundreds of people.
- **Uplift and abutment failure:** water under pressure forces its way into rock joints and lifts the structure. The Malpasset Dam in France, an arch dam, failed in December 1959 when its rock abutment gave way. More than 400 people died.
- **Overtopping and erosion:** water flowing over the crest of an embankment dam cuts away its downstream face. The South Fork Dam, an earth dam above Johnstown, Pennsylvania, failed in May 1889 after heavy rain overtopped it. More than 2000 people died in the flood.
- **Piping:** seepage through an embankment carves a channel through the fill. The Teton Dam in Idaho failed in June 1976 this way.

The safety measures that exist because of these failures include filters and drains in embankments, grout curtains, spillway capacity checks, instrumentation that tracks seepage and movement, regular inspections, and emergency action plans for the people downstream.

## History

Egyptian builders constructed the Sadd el-Kafara dam, one of the oldest known large dams. A flood damaged it soon after it was built. Roman engineers built masonry dams with a gravity profile, including the Proserpina dam at Merida in Spain. Concrete gravity and arch dams became common in the 1800s and early 1900s. Hoover Dam was built across the Colorado River from 1931 to 1936, and its scale made it a landmark of concrete construction.

## Practice

1. Find the gauge pressure at 12 m depth in fresh water.
2. Find the water force per metre of dam length on a vertical face with water 8 m deep.
3. A dam is 20 m high with a 14 m base and concrete density $2400\ \text{kg/m}^3$. Find its overturning factor of safety, with no uplift.
4. The same 20 m dam must reach a factor of safety of 2.0. Find the minimum base width.
5. Find the water force per metre of dam length for water 40 m deep, and the height above the base where it acts.

<details><summary>Answers</summary>

1. $p = 1000 \times 9.81 \times 12 = 1.18 \times 10^5\ \text{Pa}$, which is $118\ \text{kPa}$.
2. $F_H = \tfrac{1}{2}(1000)(9.81)(8)^2 = 3.14 \times 10^5\ \text{N/m}$, which is $314\ \text{kN/m}$.
3. $FS = 2(2400/1000)(14/20)^2 = 2.35$.
4. $B = 20\sqrt{2.0 \times 1000 / (2 \times 2400)} = 20\sqrt{0.4167} = 12.9\ \text{m}$.
5. $F_H = \tfrac{1}{2}(1000)(9.81)(40)^2 = 7.85 \times 10^6\ \text{N/m}$, which is $7.85\ \text{MN/m}$. It acts at $H/3 = 13.3\ \text{m}$ above the base.

</details>

## Common mistakes

- **Putting the water force at mid-depth.** On a vertical face of height $H$, the center of pressure sits $2H/3$ below the free surface, which is $H/3$ above the base. It is not at mid-depth.
- **Leaving out uplift.** Uplift can cut the effective weight a great deal. A design that passes without uplift can fail with it.
- **Treating the overturning factor as the only check.** A dam can overturn safely and still slide or crush its foundation. Check all three.
- **Mixing units in the moments.** Force per metre and lever arm give moment per metre, in N m/m. Pressure in pascals is force per square metre, which is a different quantity.

## Go deeper

- [Reference sheet: thermofluids](../../physics/reference-thermofluids.md): pressure, hydrostatics, and fluid forces in one place.
- [Reference sheet: mechanics](../../physics/reference-mechanics.md): statics, moments, and factor of safety in one place.
- [Hydrostatics and Bernoulli](../../physics/10-hydrostatics-and-bernoulli.md): pressure with depth, and the basis of the water force.
- [Mechanical properties](../../materials/03-mechanical-properties.md): compressive strength and stiffness of concrete and rock.
- [Bridges](01-bridges.md): another structure that carries load to the ground through a foundation.
- [Hydroelectric power](../energy/03-hydroelectric-power.md): how dams produce power from head and flow.
- [Fluid systems](../thermal-fluid/02-fluid-systems.md): flow, head, and pressure in pipes and channels.
