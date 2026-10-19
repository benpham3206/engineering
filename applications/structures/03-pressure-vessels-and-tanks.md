# Pressure vessels and tanks

**Type:** lesson

**Pressure vessels and tanks** are closed containers that hold gas or liquid, a pressure vessel at a pressure different from its surroundings.

> [!WARNING]
> An engineer who designs one must size the wall so its stress stays within an allowable limit and test the finished vessel before use, because a vessel that fails under pressure can burst and injure people nearby.

A storage tank holds liquid at close to atmospheric pressure, and the liquid's weight loads its walls.

**Prerequisites:** [Axial and torsion](../../physics/04-axial-and-torsion.md), [Hydrostatics and Bernoulli](../../physics/10-hydrostatics-and-bernoulli.md), [Mechanics reference](../../physics/reference-mechanics.md)
**Time:** 6-10 h

## Core ideas

### How it works

Internal pressure pushes outward on every part of the wall. In a cylinder, that push tries to split the wall along its length, which creates a stress around the circumference called the **hoop stress**. The same pressure also pulls the ends apart, which creates a smaller stress along the length. The wall must resist both. Because the hoop stress is larger, it usually sets the thickness.

A **thin wall** has a thickness small compared with its radius, typically less than about one-tenth of the radius. In a thin wall, the stress is nearly uniform through the thickness, and simple formulas give accurate answers. A thick wall needs a different analysis, because the stress changes from the inner surface to the outer surface.

A storage tank works differently. The liquid pressure is $\rho g h$, and it grows with depth. The bottom ring carries the largest hoop stress, so the wall is thickest at the bottom and thinner toward the top.

### Main parts

- **Shell.** The cylindrical or spherical wall that holds the pressure.
- **Heads.** The ends of a cylindrical vessel. Hemispherical, elliptical, and flat heads each carry the load differently. A hemispherical head carries the same stress as a sphere.
- **Nozzles and openings.** Holes for pipes, manways, and instruments. Each opening weakens the shell, so reinforcement rings or thicker walls compensate.
- **Welds.** The seams where plates join. A weld is often the weakest point, so its quality and inspection set a limit on the design.
- **Supports.** Saddles, legs, or skirts carry the vessel's weight into the foundation.
- **Relief devices.** Safety valves and rupture discs release pressure if the vessel overpressurises. The [piping and valves](../thermal-fluid/12-piping-and-valves.md) lesson covers the valve types.

### Variants

- **Cylindrical vessels.** The most common shape. Their flat sides carry more stress than a sphere, so they usually need thicker walls for the same pressure.
- **Spherical vessels.** A sphere holds pressure with the least wall thickness for a given volume and pressure, because the stress is the same in every direction. Gas storage spheres use this shape.
- **Atmospheric storage tanks.** Open or vented tanks that hold liquid at close to atmospheric pressure. Water towers, fuel tanks, and oil storage tanks are examples.
- **Pressure tanks.** Tanks that hold compressed air or gas, such as scuba cylinders and receivers in compressed-air systems.

## Key equations

For a thin-walled cylinder with inner radius $r$ in m, wall thickness $t$ in m, and internal gauge pressure $p$ in Pa:

- Hoop stress: $\sigma_h = \dfrac{pr}{t}$, in Pa.
- Longitudinal stress: $\sigma_L = \dfrac{pr}{2t}$, in Pa.

For a thin-walled sphere: $\sigma = \dfrac{pr}{2t}$, which equals the longitudinal stress of a cylinder.

For a thick-walled cylinder with inner radius $r_i$ and outer radius $r_o$ in m, under internal pressure only, the largest hoop stress occurs at the inner surface (Lamé):

$$\sigma_{\theta,\mathrm{max}} = p\,\frac{r_o^2 + r_i^2}{r_o^2 - r_i^2}$$

For a storage tank of liquid with density $\rho$ in $\text{kg/m}^3$, depth $h$ in m, and radius $R$ in m, the hoop stress at depth $h$ is:

$$\sigma_h = \frac{\rho g h R}{t}$$

where $g$ is the local gravitational acceleration (9.81 $\text{m/s}^2$ at Earth's surface). The bottom ring has the largest value, so $h$ is the full liquid depth.

## Worked example

**Given:** A cylindrical vessel with an inside diameter of $1.2\ \text{m}$ holds gas at an internal gauge pressure of $p = 2.0\ \text{MPa}$. The allowable stress of the steel is $S = 120\ \text{MPa}$. The weld joint efficiency is $E = 0.85$, which reduces the strength at the weld. The corrosion allowance is $2\ \text{mm}$.

**Find:** the required wall thickness, and the hoop stress in the chosen plate.

**Assumptions:** The wall is thin. The pressure is uniform and static. The allowable stress and joint efficiency come from the design code.

**Solution:**

1. Radius: $r = 0.6\ \text{m}$.
2. Thickness from the hoop stress limit with weld efficiency: $t = \dfrac{pr}{SE} = \dfrac{2.0\times10^6 \times 0.6}{120\times10^6 \times 0.85} = 0.01176\ \text{m} = 11.76\ \text{mm}$.
3. Add the corrosion allowance: $t = 11.76 + 2.0 = 13.76\ \text{mm}$. Round up to a $14\ \text{mm}$ plate.
4. Hoop stress in the $14\ \text{mm}$ plate: $\sigma_h = \dfrac{2.0\times10^6 \times 0.6}{0.014} = 85.7\ \text{MPa}$.

**Answer:** The plate must be at least $13.8\ \text{mm}$ thick, so a $14\ \text{mm}$ plate is chosen. The hoop stress is $85.7\ \text{MPa}$.

**Sanity check:** The ratio $t / r = 0.014 / 0.6 = 0.023$ is well under 0.1, so the thin-wall formula is valid. The **corrosion allowance** is metal expected to be lost, so check the end-of-life wall too: $14 - 2 = 12$ mm gives $\sigma_h = 2.0\times10^6 \times 0.6 / 0.012 = 100$ MPa, against a weld-reduced allowable of $SE = 120 \times 0.85 = 102$ MPa. The margin at end of life is about 2 percent, which is what the design intended. The 85.7 MPa on the new wall is not spare margin. The longitudinal stress is half the hoop stress, which is $43\ \text{MPa}$, as expected for a closed cylinder.

## Design trade-offs

- **Thickness against weight and cost.** Wall thickness grows in direct proportion to pressure and radius. A vessel twice as wide needs twice the thickness for the same pressure, so weight and steel cost grow quickly.
- **Shape.** A sphere uses less steel than a cylinder for the same volume and pressure. A cylinder is easier to fabricate and fits more easily in a plant layout, so most process vessels are cylinders.
- **Corrosion allowance.** Extra thickness absorbs corrosion over the design life. Designers balance the allowance against the cost of corrosion-resistant alloys.
- **Joint quality.** Welds that are fully inspected allow a higher joint efficiency. Spot-checked welds force thicker plate or a lower allowable stress.
- **Temperature.** Steel loses strength at high temperature and can become brittle at low temperature. The material choice follows the coldest and hottest service the vessel sees.
- **Testing.** A hydrostatic test checks the vessel with water at a pressure above the design pressure. Pressure tests often use about 1.3 times the design pressure (typical). Water is used because it is nearly incompressible, so a leak or failure releases little stored energy. Pneumatic tests store much more energy and carry more risk.

The design of pressure vessels in the United States follows the ASME Boiler and Pressure Vessel Code. The code sets allowable stresses, joint efficiencies, inspection rules, and test requirements.

## How it fails

- **Overpressure.** A blocked outlet, a runaway reaction, or a failed control can push the pressure above the design limit. Relief valves and rupture discs protect against this. Missing or undersized relief devices caused many historical boiler and vessel explosions.
- **Corrosion thinning.** Liquid can corrode the bottom of a tank or the inside of a vessel. The wall thins slowly until it can no longer hold the stress. Thickness measurements and inspection find the problem before the wall fails.
- **Brittle fracture.** Cold steel can break with little yielding. Many Liberty ships cracked during World War II, and the cold water and low-toughness steel played a part. Material choice and minimum design temperatures now control this risk.
- **Stress corrosion cracking.** Some combinations of metal, chemicals, and stress crack a vessel along a path that is hard to see. Specific alloys and stress relief heat treatment reduce the risk.
- **Fire exposure.** A vessel holding a liquefied gas that is engulfed in fire can weaken and burst. The sudden release of pressure makes the liquid flash into vapor, which causes a boiling liquid expanding vapor explosion, known as a BLEVE. Fire protection and relief valves guard against this.
- **Tank failure from liquid load.** The Boston Molasses Tank failed in January 1919 and released a wave of molasses through the city. It killed 21 people. Tank shells now receive strength checks for the full liquid load and foundation checks for settlement.

Warning signs include leaks at welds or nozzles, bulging in the shell, rust that flakes off in layers, and a relief valve that lifts or leaks during normal operation.

## History

Denis Papin built a steam digester, an early pressure cooker, in 1679, and he showed that sealed steam could do useful work. Steam boilers in the 1800s were often built with poor materials and no code, and explosions killed many people. The American Society of Mechanical Engineers was founded in 1880, and it published the first edition of its boiler and pressure vessel code in 1914. Today, the code sets the rules for design, fabrication, inspection, and testing in many countries.

## Practice

Where a problem needs gravitational acceleration, use $g = 9.81\ \text{m}/\text{s}^2$ (Earth surface).

1. A cylinder has an inside radius of 0.5 m, a wall thickness of 8 mm, and an internal pressure of 1.5 MPa. Find the hoop stress and the longitudinal stress.
2. A tank is filled with water to a depth of 8 m. Find the gauge pressure at the bottom in kPa.
3. A thin spherical vessel has a radius of 1.0 m, a wall thickness of 10 mm, and an internal pressure of 1.0 MPa. Find the stress in the wall.
4. A thick-walled cylinder has an inner radius of 0.3 m, an outer radius of 0.4 m, and an internal pressure of 40 MPa. Find the largest hoop stress. Then find the value the thin-wall formula predicts, using $r = r_i$, and state how far below the true value it falls.
5. Why does a storage tank need a thicker wall at the bottom than at the top?

<details><summary>Answers</summary>

1. $\sigma_h = pr/t = 1.5\times10^6 \times 0.5 / 0.008 = 93.8\ \text{MPa}$. $\sigma_L = \sigma_h / 2 = 46.9\ \text{MPa}$.
2. $p = \rho g h = 1000 \times 9.81 \times 8 = 78.5\ \text{kPa}$.
3. $\sigma = pr/(2t) = 1.0\times10^6 \times 1.0 / (2 \times 0.010) = 50\ \text{MPa}$.
4. $\sigma_{\theta,\mathrm{max}} = 40 \times (0.4^2 + 0.3^2) / (0.4^2 - 0.3^2) = 40 \times 0.25 / 0.07 = 143\ \text{MPa}$. The thin-wall formula gives $pr_i/t = 40 \times 0.3 / 0.1 = 120\ \text{MPa}$, which is 16 percent below the true value.
5. The liquid pressure $\rho g h$ grows with depth. The bottom ring carries the largest hoop stress, so it needs the most thickness.

</details>

## Common mistakes

- Using the diameter in the hoop stress formula instead of the radius. The formula needs $r$, and a diameter doubles the answer.
- Applying the thin-wall formula to a thick wall. Check $t/r$ first. Above about 0.1, use the thick-wall analysis.
- Forgetting the corrosion allowance and the joint efficiency. The nominal plate thickness alone often falls short of the code requirement.
- Using gauge pressure in one place and absolute pressure in another. Stress from internal pressure uses **gauge pressure**, the difference from the surroundings.
- Assuming a hydrostatic test proves the vessel is safe for all time. The test checks the vessel at one moment, and corrosion, fatigue, and cracks develop later.

## Go deeper

- [*University Physics Volume 1*, Chapter 14 (fluid mechanics)](https://openstax.org/books/university-physics-volume-1/pages/14-introduction) by OpenStax: pressure, hydrostatic pressure, and fluid behavior in tanks.
- Related lessons: [Fluid systems](../thermal-fluid/02-fluid-systems.md), [Piping and valves](../thermal-fluid/12-piping-and-valves.md), [Bridges](01-bridges.md), [Buildings and skyscrapers](02-buildings-and-skyscrapers.md), [Dams](05-dams.md).
- Background on stress: [Axial and torsion](../../physics/04-axial-and-torsion.md) and [Hydrostatics and Bernoulli](../../physics/10-hydrostatics-and-bernoulli.md).
