# Sheet metal

**Type:** lesson

Sheet metal is thin, flat metal that is cut, bent, punched, and sometimes welded into 3D parts such as enclosures, brackets, ducts, and panels. Engineers use it because it is a common, low-cost way to make light parts in quantity, and a designer must plan the bends to get them right. The key challenge is that a bend changes the length of the material. If you add up the flat outside dimensions, the flat blank is wrong, so you need a rule for how much material the bend uses. That rule is bend allowance.

**Prerequisites:** [Shop safety](01-shop-safety.md), [Machining speeds and feeds](02-machining-speeds-and-feeds.md) (for the unit habits), [Algebra](../math/01-algebra.md)
**Time:** 4-6 h

## Core ideas

- **Sheet thickness ($T$)**: the material thickness. Gauge numbers are common in the US, but the actual thickness depends on the metal type, so always check a thickness chart.
- **Bend radius ($R$)**: the inside radius of the bend. A sharp bend can crack the metal, so most metals need a minimum radius. A common rule of thumb is a radius around one times the thickness or more, depending on the material and temper.
- **Neutral axis**: an imaginary layer inside the sheet that does not stretch or compress during a bend. Material on the inside of the bend is squeezed, and material on the outside is stretched.
- **K-factor ($K$)**: the location of the neutral axis as a fraction of the thickness, measured from the inside of the bend. It is between 0 and 1. Typical values for air bending are often in the range of about 0.3 to 0.5, and the exact value depends on the material, tooling, and process. Use the shop's data or the die maker's chart.
- **Bend angle ($\theta$)**: how far the sheet is bent, in degrees. A 90 degree bend is a right-angle bend.
- **Bend allowance (BA)**: the length of the neutral axis through the bend. It is the amount added to the flat length for each bend.
- **Flat blank**: the flat shape cut before bending. Its length equals the sum of the flange lengths, plus the bend allowance for each bend, minus any setback adjustments.

Common sheet metal processes include shearing (straight cuts), punching (holes and shapes in a press), laser or waterjet cutting (profiles), and press braking (bends). Each process leaves its own edge quality. Laser cuts can have a heat-affected edge. Punched holes can be slightly tapered.

Design tips:

- Keep holes and slots at least about one material thickness away from a bend line, so they do not distort.
- Use the same bend radius throughout a part when possible. Changing tools costs time.
- Keep bends the same direction when you can, so the part can be formed in fewer setups.
- Check the rolling direction (grain) of the sheet. A bend line parallel to the rolling direction is more likely to crack, so orient bend lines across (perpendicular to) the rolling direction where possible.

## Key equations

The bend allowance for a bend of angle $\theta$ with inside radius $R$, thickness $T$, and K-factor $K$ is:

$$\text{BA} = \theta \cdot \frac{\pi}{180} \cdot (R + K\,T)$$

Units: $\theta$ is in degrees. $R$ and $T$ must be in the same length unit (mm in SI, inches in US form), and $\text{BA}$ comes out in that same unit. $K$ is a dimensionless fraction. The factor $\pi/180$ converts degrees to radians, so the result is an arc length.

## Worked example

**Given:** A 90 degree bend in 2 mm thick aluminum sheet with an inside radius $R = 3$ mm. Use a K-factor of $K = 0.33$ from the shop's chart.

**Find:** The bend allowance for this bend.

**Assumptions:** Air bending with a single bend, and the K-factor is correct for this tooling.

**Solution:**

1. Neutral axis distance from the inside of the bend:
$$K\,T = 0.33 \times 2 = 0.66 \text{ mm}$$
2. Radius to the neutral axis:
$$R + K\,T = 3 + 0.66 = 3.66 \text{ mm}$$
3. Angle in radians:
$$90 \times \frac{\pi}{180} = \frac{\pi}{2} = 1.5708$$
4. Bend allowance:
$$\text{BA} = 1.5708 \times 3.66 = 5.749 \text{ mm}$$

**Answer:** The bend allowance is about 5.75 mm.

**Sanity check:** The arc length of a 90 degree bend on a circle of radius 3.66 mm is one quarter of the circumference, $\frac{1}{4} \times 2\pi \times 3.66 = 5.75$ mm. That matches. The allowance is also a little less than the full outside arc, which is what the neutral axis predicts.

## Practice

1. A 90 degree bend has $R = 5$ mm, $T = 3$ mm, and $K = 0.4$. What is the bend allowance in mm? Round to two decimal places.
2. A 90 degree bend in $1/8$ in (0.125 in) sheet has $R = 0.25$ in and $K = 0.33$. What is the bend allowance in inches? Round to three decimal places.
3. Why is a sharp bend radius risky for a brittle metal?
4. Which way does the material inside the bend go during forming: squeezed or stretched?
5. Name one reason to keep holes away from bend lines.

<details><summary>Answers</summary>

1. 9.74 mm
2. 0.457 in
3. It can crack on the outside of the bend, because the outside is stretched.
4. Squeezed.
5. Holes near a bend can distort, get out of round, or tear.

</details>

## Common mistakes

- Adding the flange lengths alone and forgetting the bend allowance, which makes the part too short or too long.
- Using the outside dimensions for the flat blank without subtracting the material used by the bend.
- Assuming one K-factor fits all materials and tooling. Use the shop's chart and test a sample.
- Ignoring the rolling direction, which causes cracks when the bend line runs parallel to the grain on some alloys.
- Specifying a bend radius smaller than the material can take.

## Go deeper

- [OpenStax University Physics Volume 1, Chapter 1](https://openstax.org/books/university-physics-volume-1/pages/1-introduction) by OpenStax (Rice University): units and dimensional checks, useful for converting between mm and inches.
- [NIST: SI units](https://www.nist.gov/pml/weights-and-measures/si-units) by NIST: the SI base units and how to express lengths consistently.
- [Paul's Online Math Notes: Algebra](https://tutorial.math.lamar.edu/classes/alg/alg.aspx) by Paul Dawkins, Lamar University: solving and rearranging simple formulas.
- [Manufacturing reference](reference.md): the lookup sheet for this topic.
