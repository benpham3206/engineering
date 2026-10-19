# Identifying materials and manufacturing processes

**Type:** lesson

Identifying materials and manufacturing processes is the work of finding out what a part is made from and how it was shaped, using clues on its surface and a few simple tests. Engineers need this step, because a rebuild in the wrong material can look right and still fail under load.

Every part is made from a material and shaped by a process. The material affects strength, weight, and cost, and the process affects the shape the designer could make. Careful observation and a few simple tests can tell you a lot.
**Prerequisites:** [Teardowns](01-teardowns.md), [Measuring existing parts](02-measuring-existing-parts.md), [Mechanical properties](../materials/03-mechanical-properties.md), [Metals, polymers, ceramics, composites](../materials/05-material-classes.md)
**Time:** 8-12 h

## Core ideas

- Start with a guess, then test it. Most identifications come from two or three clues that agree, not from one clue alone.
- **Ferromagnetic** metals, such as iron and most carbon steels, are attracted to a magnet. Aluminum, copper, brass, and most plastics are not. This is a quick sort, not a grade test. Some stainless steels are only weakly magnetic.
- A **spark test** holds a sample against a grinding wheel and watches the sparks. Carbon steel gives long streams with small bursts called forks. Stainless steel and cast iron give different patterns.

> [!WARNING]
> Treat this as a rough guide, and always wear eye protection and a guard.

- **Density** is mass per unit volume. Measure the mass on a scale and the volume by displacement in water (Archimedes' principle). Density separates materials that look alike, such as aluminum and zinc, or plastics with different fillers.
- Process clues come from how the surface was formed:
  - **Parting line:** a thin seam where two mold halves met. It points to molding (injection molding, die casting, or sand casting).
  - **Draft angle:** a slight taper on walls so the part releases from a mold. Molded plastic parts often have a draft of about 1 to 3 degrees. A wall with no draft on a molded part is unusual.
  - **Ejector pin marks:** small round witness marks where pins pushed the part out of a mold. They are a strong clue for injection molding.
  - **Gate marks:** a small stub or scar where plastic or metal entered the mold.
  - **Machining marks:** straight parallel lines suggest milling or planing. Concentric circular rings suggest turning on a lathe. Fine random scratches with a uniform sheen suggest grinding.
  - **Weld beads:** raised or ripple-patterned lines where metal was joined by melting.
  - **Sheet metal:** uniform wall thickness, bend radii at the corners, and small relief notches where the metal was bent.
  - **Porosity:** small holes or bubbles inside a cast part, visible on a cut section.
- A material and a process go together. Cast iron is usually sand cast. Thin aluminum housings are often die cast. Most molded plastic parts are injection molded.

## Key equations

Density, where $\rho$ is density in grams per cubic centimeter ($\text{g/cm}^3$), $m$ is mass in grams, and $V$ is volume in cubic centimeters:

$$\rho = \frac{m}{V}$$

Volume by water displacement, where $V$ is the volume of the sample in cubic centimeters, $V_2$ is the water level after the sample is added, and $V_1$ is the water level before, both read in milliliters ($1\ \text{mL} = 1\ \text{cm}^3$):

$$V = V_2 - V_1$$

Typical densities (standard textbook values, which vary by alloy and filler):

- Low-carbon steel: about 7.85 $\text{g/cm}^3$
- Aluminum alloy (such as 6061): about 2.70 $\text{g/cm}^3$
- Zinc alloy (die cast): about 6.6 $\text{g/cm}^3$
- Polypropylene (PP): about 0.90 $\text{g/cm}^3$
- Acrylonitrile butadiene styrene (ABS): about 1.04 $\text{g/cm}^3$

## Worked example

**Given:** A small bracket has a mass of $m = 53.4$ g. Placed in a graduated cylinder, its water level rises from 40.0 mL to 46.8 mL. A magnet sticks firmly to the bracket.

**Find:** (a) the density, and (b) the most likely material.

**Assumptions:** The bracket is solid with no internal voids. Water displacement is accurate to about 0.1 mL. Density values are typical.

**Solution:**

(a) Volume from displacement:

$$V = 46.8 - 40.0 = 6.8 \text{ mL} = 6.8 \text{ cm}^3$$

Density:

$$\rho = \frac{53.4}{6.8} = 7.85 \text{ g/cm}^3$$

(b) The density matches low-carbon steel (about 7.85 $\text{g/cm}^3$). The magnet sticks, which fits a ferromagnetic steel. Aluminum would give about 2.70 $\text{g/cm}^3$, which does not match.

**Answer:** The density is 7.85 $\text{g/cm}^3$, and the bracket is most likely low-carbon steel.

**Sanity check:** A 6.8 $\text{cm}^3$ block of steel should weigh $6.8 \times 7.85 = 53.4$ g. That is exactly the measured mass, so the two agree.

## Practice

1. A sample has a mass of 26.8 g and a volume of 9.9 $\text{cm}^3$. What is its density in $\text{g/cm}^3$, rounded to 2 decimal places?
2. Water rises from 50.0 mL to 58.4 mL when a part is dropped in. What is the part's volume in $\text{cm}^3$?
3. A part of 8.4 $\text{cm}^3$ has a density of 2.70 $\text{g/cm}^3$. What is its mass in grams, rounded to 1 decimal place?
4. A steel part has a volume of 12.0 $\text{cm}^3$. What is its mass in grams, using 7.85 $\text{g/cm}^3$?
5. A part has a mass of 6.6 g and a volume of 1.0 $\text{cm}^3$. What is its density in $\text{g/cm}^3$?

<details><summary>Answers</summary>

1. 2.71
2. 8.4
3. 22.7
4. 94.2
5. 6.6

</details>

## Common mistakes

- Using the magnet test to pick a grade. It only separates magnetic from non-magnetic materials.
- Forgetting that the volume from water displacement is the change in level, not the final level.
- Reading a parting line on a machined part and calling it a mold seam. Look for other clues before deciding.
- Assuming a surface finish tells you the material. Painted, plated, or anodized parts hide the base metal, so test a cut edge or a hidden face.
- Trusting one clue alone. Confirm with a second test, such as density or a section cut.

## Go deeper

- [Materials Science bookshelf](https://eng.libretexts.org/Bookshelves/Materials_Science) by LibreTexts: a free starting point for material properties and polymers.
- [Mechanical Engineering bookshelf](https://eng.libretexts.org/Bookshelves/Mechanical_Engineering) by LibreTexts: free material on machining and design for manufacture.
- [*University Physics Volume 1*](https://openstax.org/books/university-physics-volume-1/pages/1-introduction) by OpenStax: free units and measurement material to support density calculations.
- [SI units and the metric system](https://www.nist.gov/pml/owm/metric-si) by NIST: the official guide to the units used in density.
- [Reverse-engineering reference](reference.md): the lookup sheet for this topic.
