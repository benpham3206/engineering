# Tolerances, fits, and surface finish

**Type:** lesson

No part is made exactly to its drawing dimension. Tolerances state how far a size may vary, fits describe how two mating parts fit together given those variations, and surface finish describes the texture of the surface. An engineer who writes tolerances that are too tight adds cost, and one who writes them too loose gets parts that do not assemble or do not work. Full standard tables are in the handbooks that the shop uses.

**Prerequisites:** [Machining speeds and feeds](02-machining-speeds-and-feeds.md), [Machining processes](03-machining-processes.md)
**Time:** 6-8 h

## Core ideas

- **Nominal size**: the design size on the drawing, such as 25 mm.
- **Limits**: the largest and smallest allowed sizes, such as 25.000 mm and 25.021 mm.
- **Tolerance**: the difference between the upper limit and the lower limit. For the example above, the tolerance is 0.021 mm.
- **Hole basis system**: a common approach where the hole is the fixed reference. The hole's lower limit equals the nominal size, and the shaft is varied to get the fit you want. The ISO letters and numbers (for example H7 for the hole, and g6 or p6 for the shaft) describe how big the tolerance band is and where it sits.
- **Clearance fit**: the shaft is always smaller than the hole, so the parts move freely. A sliding or running fit is an example.
- **Interference fit**: the shaft is always bigger than the hole, so the parts must be pressed or shrunk together. A press fit is an example.
- **Transition fit**: the fit can be either clearance or interference, depending on the actual sizes. Locating pins often use this.
- **Stack-up**: the total variation of a chain of dimensions. Worst case adds all the tolerances, which is safe but pessimistic. Statistical (root-sum-square) stack-up assumes the errors are random and combines them as a square root of the sum of squares.
- **Surface roughness (Ra and Rz)**: a measure of the small height variations on a surface. Ra is the average roughness height. Rz is the average of the largest peaks and valleys over a sample length. Both are measured in micrometers or microinches.
- **Ideal roughness from turning**: the cutting tool leaves a regular pattern of peaks whose height depends on the feed and the tool nose radius.

Simple rules that help:

- Put tight tolerances only where the function needs them. Loose tolerance elsewhere saves money.
- Specify the fit type, not only the sizes, when two parts mate.
- Measure with the right instrument. A caliper is not a substitute for a gauge on a tight fit.
- Remember that cost rises fast as tolerances get tighter. Tighter tolerance often needs slower machining, better tools, and more inspection.

## Key equations

Maximum clearance for a hole with upper limit $D_{\max}$ and a shaft with lower limit $d_{\min}$:

$$C_{\max} = D_{\max} - d_{\min}$$

Minimum clearance for a hole with lower limit $D_{\min}$ and a shaft with upper limit $d_{\max}$:

$$C_{\min} = D_{\min} - d_{\max}$$

If $C_{\min}$ is negative, the fit has some interference. Units: all values in mm (SI) or inches (US form), and both must match.

Worst-case stack-up of $n$ dimensions with tolerances $t_i$ (plus or minus):

$$T_{\text{worst}} = \sum_{i=1}^{n} t_i$$

Root-sum-square stack-up:

$$T_{\text{RSS}} = \sqrt{\sum_{i=1}^{n} t_i^2}$$

Ideal peak height (roughness) from a turning feed $f$ (mm per revolution) and tool nose radius $r$ (mm):

$$R_{\max} = \frac{f^2}{8\,r}$$

Units: $R_{\max}$ comes out in mm. Multiply by 1000 to get micrometers. This is the ideal value. Real surfaces are rougher because of tool wear, vibration, and built-up edge.

## Worked example

**Given:** A hole has limits 25.000 mm and 25.021 mm. A shaft has limits 24.980 mm and 24.993 mm. (These are example values, not standard ISO table values.)

**Find:** The maximum and minimum clearance, and the fit type.

**Assumptions:** The sizes are measured and within limits, and the parts are at room temperature.

**Solution:**

1. Maximum clearance:
$$C_{\max} = 25.021 - 24.980 = 0.041 \text{ mm}$$
2. Minimum clearance:
$$C_{\min} = 25.000 - 24.993 = 0.007 \text{ mm}$$
3. Both values are positive, so the shaft is always smaller than the hole.

**Answer:** Clearance fit, with clearance from 0.007 mm to 0.041 mm.

**Sanity check:** The hole's tolerance is 0.021 mm and the shaft's tolerance is 0.013 mm. The total clearance range should be about the sum of those tolerances, which is 0.034 mm. The computed range is 0.041 - 0.007 = 0.034 mm.
**Stack-up example:** Three parts are 10.00 mm (tolerance $\pm 0.05$), 15.00 mm ($\pm 0.05$), and 20.00 mm ($\pm 0.10$), in a line. The nominal total is 45.00 mm. Worst case is $\pm 0.20$ mm. The RSS value is $\sqrt{0.05^2 + 0.05^2 + 0.10^2} = \sqrt{0.0025 + 0.0025 + 0.01} = \sqrt{0.015} = 0.1225$ mm, about $\pm 0.12$ mm. The RSS value is smaller, which is why statistical stack-up is used when the risk allows it.

**Surface roughness example:** A turning feed of $f = 0.2$ mm/rev with a tool nose radius of $r = 0.8$ mm gives an ideal peak height of $R_{\max} = 0.2^2 / (8 \times 0.8) = 0.00625$ mm, which is 6.25 micrometers.

## Practice

1. A hole has limits 25.000 mm and 25.021 mm. A shaft has limits 25.010 mm and 25.000 mm. What is the minimum clearance in mm? A negative number means interference.
2. Using the same hole and shaft as Problem 1, what is the maximum clearance in mm?
3. Three parts of 25 mm each have tolerance $\pm 0.1$ mm. What is the worst-case total length, in mm and tolerance?
4. A turning feed of $f = 0.1$ mm/rev with a tool nose radius $r = 0.4$ mm gives an ideal peak height. What is it in micrometers?
5. Name one reason to specify a fit type, not only the sizes.

<details><summary>Answers</summary>

1. -0.010 mm (interference of 0.010 mm)
2. 0.021 mm
3. 75 mm plus or minus 0.3 mm
4. 3.125 micrometers
5. It tells the machinist and inspector how the parts are meant to assemble, not just whether each part is in size.

</details>

## Common mistakes

- Treating tolerance as the same as the nominal size. Tolerance is a band, not a single value.
- Calculating clearance with the wrong pairing, such as the hole's upper limit with the shaft's upper limit. Clearance uses the hole's upper limit with the shaft's lower limit for the maximum.
- Specifying tighter tolerances than the function needs, which raises cost without benefit.
- Using worst-case stack-up everywhere, or using RSS when the risk is high and the parts must always fit.
- Forgetting that surface roughness on the drawing is a limit, and the real surface can be rougher.

## Go deeper

- [NIST: SI units](https://www.nist.gov/pml/weights-and-measures/si-units) by NIST: SI base units and the prefixes used for micrometers and millimeters.
- [NIST: Weights and measures](https://www.nist.gov/pml/weights-and-measures) by NIST: the measurement standards office, including metric (SI) programs.
- [Paul's Online Math Notes: Algebra](https://tutorial.math.lamar.edu/classes/alg/alg.aspx) by Paul Dawkins, Lamar University: subtracting limits and solving simple formulas.
