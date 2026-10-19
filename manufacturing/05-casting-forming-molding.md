# Casting, forming, and molding

**Type:** lesson

Casting, forming, and molding are the three main ways to shape material without cutting it away. Engineers need to know them because each process sets the cost, size, and finish of the part it makes. Casting pours molten metal into a mold. Forming pushes solid metal into shape with force, as in forging, stamping, and rolling. Molding shapes plastic or other materials in a cavity, as in injection molding. Each process is best at a certain volume and part size. Each also leaves its own shrinkage, grain, or parting-line features that a designer must account for.

**Prerequisites:** [Shop safety](01-shop-safety.md)
**Time:** 5-7 h

## Core ideas

- **Casting**: a liquid metal fills a mold cavity and solidifies. Sand casting is cheap and flexible for large, low-volume parts. Die casting forces metal into steel dies under pressure and is fast for high volume. Investment casting uses wax patterns and gives fine detail.
- **Shrinkage**: most metals and plastics get smaller as they cool. Make the pattern or mold larger than the final part by the shrink allowance.
- **Draft**: a slight taper on vertical walls so the part can be pulled from the mold or die without tearing. Designers usually add a few degrees of draft.
- **Parting line**: the joint where two halves of a mold or die meet. It leaves a thin line or flash on the part that may need removing.
- **Forging**: a hammer or press squeezes hot or cold metal into shape. The grain flows with the shape, which often gives strong parts.
- **Stamping**: a press forces sheet metal into a die in one or more strokes. It is fast and repeatable, and it is a common route for sheet metal parts (lesson 07).
- **Extrusion**: metal or plastic is pushed through a shaped opening to make a long constant cross-section, such as aluminum window frames.
- **Injection molding**: molten plastic is forced into a closed steel mold under pressure, cooled, and ejected as a part. Tooling is expensive, but each part is cheap once the mold exists.

Each process has a rough volume where it makes economic sense. Injection molding tooling can cost thousands of dollars, so it pays off only for large runs. Sand casting needs a pattern but no hard tooling, so it suits small runs of big parts.

## Key equations

When a part shrinks as it cools, the pattern (or mold cavity) must be larger than the finished dimension. For a linear shrinkage fraction $s$ (a typical value for aluminum castings is about 1.3 percent, and it depends on the alloy and the process):

$$L_{\text{pattern}} = L_{\text{part}} \,(1 + s)$$

Units: $L_{\text{part}}$ and $L_{\text{pattern}}$ are lengths in the same unit (mm in SI, inches in US form). $s$ is a dimensionless fraction. Use the value from the alloy supplier or a casting handbook for your real job.

## Worked example

**Given:** A cast aluminum housing has a finished length of $L_{\text{part}} = 200$ mm. Use a typical shrink allowance of $s = 0.013$ (1.3 percent).

**Find:** The length the pattern must be.

**Assumptions:** The shrinkage is uniform and the part is not machined after casting in this step.

**Solution:**

$$L_{\text{pattern}} = 200 \times (1 + 0.013) = 200 \times 1.013 = 202.6 \text{ mm}$$

**Answer:** The pattern must be about 202.6 mm long.

**Sanity check:** The allowance is 2.6 mm, which is about 1.3 percent of 200 mm. That is small but enough to matter on a tight fit. Doubling the part length would double the allowance, so long parts need proportionally bigger allowances.

## Practice

1. A finished part is 300 mm long and $s = 0.013$. What is the pattern length in mm? Round to one decimal place.
2. A finished part is 150 mm long and $s = 0.010$. What is the pattern length in mm?
3. Name one reason designers add draft to a mold wall.
4. Which process is best for a high-volume, small plastic cap: sand casting or injection molding?
5. A forging is stronger along the grain flow. Why does that matter for a crank that bends under load?

<details><summary>Answers</summary>

1. 303.9 mm
2. 151.5 mm
3. To let the part release from the mold or die without tearing or scraping.
4. Injection molding
5. The grain runs along the shape, so the strongest direction matches the bending load.

</details>

## Common mistakes

- Making the pattern the same size as the part. The shrink allowance must be added first.
- Ignoring draft, so the part sticks or gets damaged on release.
- Putting the parting line across a critical surface, where the flash will show.
- Choosing injection molding for a small run, which makes tooling cost dominate.
- Using a shrink value from the wrong alloy or process.

## Go deeper

- [NASA Glenn Research Center](https://www.nasa.gov/glenn/) by NASA: government materials and manufacturing research, useful for real-world context on processing.
- [NIST: Manufacturing](https://www.nist.gov/manufacturing) by NIST: an overview of manufacturing processes and standards.
- [Paul's Online Math Notes: Algebra](https://tutorial.math.lamar.edu/classes/alg/alg.aspx) by Paul Dawkins, Lamar University: rearranging and solving simple percent and proportion formulas.
- [Manufacturing reference](reference.md): the lookup sheet for this topic.
