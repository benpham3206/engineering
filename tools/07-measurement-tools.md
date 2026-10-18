# Measurement tools

**Type:** lesson

Every design number depends on a measurement, and every measurement has an error. Measurement tools include rules, calipers, micrometers, gauges, and digital readouts. Learn to read them correctly, estimate the uncertainty, and combine errors in a stack of parts.

**Prerequisites:** [Starter kit](01-starter-kit.md). Also [algebra and functions](../math/README.md). The [measurement folder](../measurement/README.md) covers error and uncertainty in depth.
**Time:** 4-8 h for reading tools and stacking tolerances

## Core ideas

- **Resolution** is the smallest step a tool can show. A steel rule with 1 mm marks has about 0.5 mm resolution when you read to the nearest half-mark.
- **Accuracy** is how close the reading is to the true value. A tool can have fine resolution and poor accuracy if it is out of calibration.
- **Repeatability** is how much repeated readings differ.
- A **caliper** measures outside, inside, and depth dimensions. A **micrometer** measures smaller lengths with finer steps, typically 0.01 mm or 0.001 in.
- Always record units with the reading. Convert with 1 in = 25.4 mm.
- A **tolerance** is the allowed variation in a dimension, such as $\pm 0.05$ mm.
- A **stack-up** adds tolerances of parts that line up in one direction. Two methods are common: worst case (add all the errors) and root-sum-square (RSS, the square root of the sum of squares). RSS assumes independent errors.

Read the [NIST SI guide](https://www.nist.gov/pml/special-publication-811) for consistent unit use. Use it when you record and convert readings.

## Key equations

For $n$ parts with tolerances $t_i$ (each $\pm t_i$, in mm):

Worst case:

$$T_{\text{wc}} = \sum_{i=1}^{n} t_i$$

Root-sum-square:

$$T_{\text{rss}} = \sqrt{\sum_{i=1}^{n} t_i^2}$$

Here $T$ is the total tolerance in mm. Worst case is the safe bound. RSS is an estimate that assumes random, independent variation.

## Worked example

**Given:** Three parts stack end to end in one direction. Their tolerances are $\pm 0.10$ mm, $\pm 0.05$ mm, and $\pm 0.08$ mm.

**Find:** The total tolerance by worst case and by RSS.

**Assumptions:** Each tolerance is a symmetric $\pm$ band. Errors are independent for RSS.

**Solution (run in Python):**

```python
import math
tols = [0.10, 0.05, 0.08]   # mm, each +/-
worst = sum(tols)
rss = math.sqrt(sum(t**2 for t in tols))
print("worst =", worst, "mm, rss =", round(rss, 4), "mm")
```

Output:

```
worst = 0.23 mm, rss = 0.1375 mm
```

**Answer:** Worst case is $\pm 0.23$ mm. RSS is $\pm 0.14$ mm (0.1375 mm rounded).

**Sanity check:** RSS must be smaller than the worst case, because the squares of small numbers add to less than the square of their sum. Here $0.1375 < 0.23$. Also, the largest single tolerance, 0.10 mm, is less than either total, which is expected.

## Practice

1. A stack has tolerances $\pm 0.02$ mm, $\pm 0.03$ mm, and $\pm 0.01$ mm. Find the worst-case total in mm.
2. Find the RSS total for the same stack in mm to four decimals.
3. A caliper shows 25.40 mm. Convert the reading to inches to four decimals.
4. A steel rule has marks every 1 mm. You read the midpoint between two marks. What is the resolution of your reading in mm?
5. Which method, worst case or RSS, is safer for a critical fit? Explain in one sentence.

<details><summary>Answers</summary>

1. 0.060 mm
2. 0.0374 mm
3. 1.0000 in
4. 0.5 mm
5. Worst case. It bounds the error even if all parts are at their limits together.

</details>

## Common mistakes

- Mixing units in a single stack, such as adding inches to millimeters.
- Reading a caliper or micrometer without checking zero first.
- Reporting more digits than the tool resolves.
- Using RSS for a safety-critical fit where worst case is required.
- Forgetting that a tool out of calibration gives wrong readings with no warning.

## Go deeper

- [NIST Special Publication 811](https://www.nist.gov/pml/special-publication-811) by NIST: the official SI guide for units and conversion.
- [University Physics Volume 1, Chapter 1: Introduction](https://openstax.org/books/university-physics-volume-1/pages/1-introduction) by OpenStax: units, unit conversion, dimensional analysis, and significant figures. Free to read.
- [Measurement folder](../measurement/README.md): the error and uncertainty lessons for this topic.
- Related: [CAD](06-cad-solidworks.md), [shop tools](08-shop-tools.md), [starter kit](01-starter-kit.md).
