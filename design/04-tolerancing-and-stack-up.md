# Tolerancing and stack-up

**Type:** lesson

Tolerancing is the practice of setting the allowed variation in each dimension so a part keeps working, and stack-up is the adding up of that variation across several parts that must fit together. Every part varies a little, so a design that ignores tolerances can look correct on paper and still fail to assemble. Geometric tolerances (GD&T) are covered in the next two lessons.

**Prerequisites:** [Engineering graphics](02-engineering-graphics.md), [Design process](01-design-process.md), [Algebra](../math/01-algebra.md), [Probability and statistics](../math/07-probability-and-statistics.md) (for the RSS method)
**Time:** 5-8 h

## Core ideas

- **Nominal size.** The target dimension written on the drawing, such as 25.00 mm (0.984 in).
- **Tolerance.** The allowed variation from nominal. A bilateral tolerance is written as plus and minus the same amount, such as $25.00 \pm 0.05$ mm.
- **Unilateral tolerance.** The variation is on one side only, such as $25.00^{+0.05}_{\;\;0}$ mm.
- **Upper and lower limits.** The largest and smallest size allowed. They are the nominal plus the upper deviation and the nominal plus the lower deviation.
- **Tolerance band.** The range between the limits. Its width is the total tolerance.
- **Fit.** The relationship between two mating parts, such as a shaft in a hole. Fits are described as clearance, interference, or transition.
- **Stack-up.** The sum of tolerances along a chain of dimensions that together set one final gap or position.

A tolerance is not a mistake. It is a design choice. Tighter tolerances cost more because they need more care in making and checking. Use the widest tolerance that still meets the function.

## Limits and fits

For a shaft in a hole:

- Clearance fit: the shaft is always smaller than the hole, so it can slide or turn freely.
- Interference fit: the shaft is always larger, so the parts must be pressed or heated together.
- Transition fit: sometimes clearance, sometimes interference.

A fit is checked with the smallest hole and largest shaft (for the tightest fit) and the largest hole and smallest shaft (for the loosest fit).

## Key equations

Limits from nominal and tolerance:

$$
L_{\max} = N + t, \qquad L_{\min} = N - t
$$

where $N$ is the nominal size (mm or in), $t$ is the plus-minus tolerance (mm or in), and $L_{\max}$ and $L_{\min}$ are the upper and lower limits.

Tolerance band width:

$$
T = L_{\max} - L_{\min} = 2t
$$

Worst-case stack-up for a linear chain of $n$ dimensions with tolerances $t_i$:

$$
T_{\text{wc}} = \sum_{i=1}^{n} |t_i|
$$

Root-sum-square (RSS) stack-up, which assumes independent random variation and is usually a statistical estimate:

$$
T_{\text{rss}} = \sqrt{\sum_{i=1}^{n} t_i^2}
$$

Clearance between a hole of size $H$ and a shaft of size $S$:

$$
C_{\min} = H_{\min} - S_{\max}, \qquad C_{\max} = H_{\max} - S_{\min}
$$

Units: all quantities in the same length unit (mm or in). Clearance $C$ is positive for a gap and negative for an interference.

## Worst-case and RSS

- **Worst-case** assumes every part is at its limit at the same time in the worst direction. It guarantees the fit but is conservative and can cost too much.
- **RSS** assumes the variations are independent and random. It gives a smaller total tolerance, but it is only a probability estimate. Use it when you have data showing the process is stable and when a small risk of out-of-tolerance parts is acceptable.

For safety-critical or hard-to-adjust assemblies, use worst-case. Use RSS when you can measure the process and accept a small statistical risk.

## Worked example

A housing has an inside length of 60.00 mm (2.362 in). Two parts sit inside it, a spacer of 25.00 mm (0.984 in) and a block of 30.00 mm (1.181 in). The gap left between them must be found. Tolerances are: housing $\pm 0.15$ mm, spacer $\pm 0.05$ mm, block $\pm 0.08$ mm.

**Given.** $L = 60.00 \pm 0.15$, $a = 25.00 \pm 0.05$, $b = 30.00 \pm 0.08$ (mm).

**Find.** The nominal gap $g$, the worst-case range of $g$, and the RSS range of $g$.

**Assumptions.** Parts sit flat in a single line. Tolerances are plus-minus and independent.

**Solution.**

The gap is $g = L - (a + b)$.

Nominal gap: $g = 60.00 - (25.00 + 30.00) = 5.00$ mm.

Worst-case tolerance: $T_{\text{wc}} = 0.15 + 0.05 + 0.08 = 0.28$ mm.

So $g$ is between $5.00 - 0.28 = 4.72$ mm and $5.00 + 0.28 = 5.28$ mm.

RSS tolerance: $T_{\text{rss}} = \sqrt{0.15^2 + 0.05^2 + 0.08^2} = \sqrt{0.0314} = 0.177$ mm.

So with RSS, $g$ is between $4.82$ mm and $5.18$ mm.

**Answer.** Nominal gap 5.00 mm (0.197 in). Worst-case range 4.72 to 5.28 mm (0.186 to 0.208 in). RSS range about 4.82 to 5.18 mm (0.190 to 0.204 in).

**Sanity check.** The RSS range is narrower than the worst case, as expected. Both are centered on 5.00 mm. A gap of 4.72 mm is the worst-case low end. If the design needs at least 4.8 mm, worst-case fails and RSS passes with some risk. Whether that risk is acceptable is the designer's decision.

## Checklist

- Are the limits calculated, not guessed, from nominal and tolerance?
- Is every dimension in the chain included in the stack-up?
- Are the signs correct? A dimension that subtracts in the gap calculation must subtract in the tolerance chain.
- Is worst-case used where a failure would be costly?
- Are the units the same across the whole calculation?

## Practice

1. Find the upper and lower limits of $25.00 \pm 0.05$ mm. Give both numbers in mm.
2. Find the worst-case total tolerance for three dimensions with tolerances $\pm 0.1$, $\pm 0.2$, and $\pm 0.05$ mm. Give the number in mm.
3. Find the RSS total tolerance for the same three dimensions. Give the number in mm to two decimals.
4. A shaft is $30.00^{-0.02}_{-0.04}$ mm and a hole is $30.00^{+0.05}_{\;\;0}$ mm. Find the minimum and maximum clearance. Give both in mm.

<details><summary>Answers</summary>

1. 24.95 and 25.05
2. 0.35
3. 0.23
4. 0.02 and 0.09

</details>

## Common mistakes

- Adding nominal sizes without checking the sign of each dimension in the gap.
- Using RSS for a critical fit without saying that it is a statistical estimate.
- Forgetting one dimension in the chain, which hides a large part of the variation.
- Mixing mm and inch values in one calculation.
- Calling a tolerance an allowed error. It is a design range, not a tolerance on a measurement.

## Go deeper

- [Paul's Online Math Notes](https://tutorial.math.lamar.edu/) by Paul Dawkins: free algebra review for signs, inequalities, and absolute value.
- [NIST, Metric (SI) program](https://www.nist.gov/pml/owm/metric-si) by the National Institute of Standards and Technology: official guidance on SI units, useful when mixing metric and inch dimensions.
- [Engineering LibreTexts](https://eng.libretexts.org/) by the LibreTexts project: free engineering texts that cover measurement and statistics background.
- [Design reference](reference.md): the lookup sheet for this topic.
