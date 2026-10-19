# Algebra

**Type:** lesson

Algebra is the branch of mathematics that uses letters for unknown numbers and rules for solving equations. Engineers use it to rearrange formulas, solve for a required size or load, and check units before they trust a result.

**Prerequisites:** none. High-school arithmetic and basic fractions are assumed.
**Time:** 8-12 h

## Core ideas

- A variable is a symbol for a number you do not know yet, or a number that can change.
- An equation says two expressions are equal. Solving it means finding the values that make it true.
- Algebra works because whatever you do to one side, you do to the other. Add, subtract, multiply, or divide both sides by the same thing (except zero).
- A function is a rule that takes an input and gives exactly one output. In engineering, the input is often a load, time, or temperature and the output is a stress, a deflection, or a temperature.
- Units are algebra too. If you multiply newtons by meters, the result is joules. A formula that does not balance its units is wrong, even if the arithmetic is right.
- Rearranging a formula is a skill of its own. A formula like $S = \frac{bh^2}{6}$ can be solved for $h$ once you isolate the squared term and take a square root.
- A linear equation has the form $y = mx + c$. Its graph is a straight line, and $m$ is the slope (rate of change).
- A quadratic equation has the form $ax^2 + bx + c = 0$. It can have two, one, or no real roots.

## Key equations

Quadratic formula, for $ax^2 + bx + c = 0$ with $a \ne 0$:

$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

Slope between two points $(x_1, y_1)$ and $(x_2, y_2)$:

$$m = \frac{y_2 - y_1}{x_2 - x_1}$$

Section modulus of a solid rectangle of width $b$ (m) and height $h$ (m), used in bending stress:

$$S = \frac{b\,h^2}{6} \quad [\mathrm{m^3}]$$

Symbols: $S$ is the section modulus in cubic meters (in$^3$ in US customary units), $b$ is width, $h$ is height.

## Worked example

**Given:** A rectangular steel strip must have a section modulus of $S = 2.0 \times 10^{-5}\ \mathrm{m^3}$. Its width is fixed at $b = 0.05\ \mathrm{m}$.

**Find:** The required height $h$.

**Assumptions:** The strip is a solid rectangle. The formula $S = bh^2/6$ applies.

**Solution:**

1. Start from $S = \dfrac{b h^2}{6}$.
2. Multiply both sides by 6: $6S = b h^2$.
3. Divide by $b$: $h^2 = \dfrac{6S}{b}$.
4. Take the positive square root: $h = \sqrt{\dfrac{6S}{b}}$.
5. Substitute: $h = \sqrt{\dfrac{6 \times 2.0 \times 10^{-5}}{0.05}} = \sqrt{0.0024} \approx 0.04899\ \mathrm{m}$.

**Answer:** $h \approx 0.0490\ \mathrm{m}$, or about 49 mm.

**Sanity check:** Put it back in: $0.05 \times 0.04899^2 / 6 = 2.0 \times 10^{-5}\ \mathrm{m^3}$. The units are $\mathrm{m} \cdot \mathrm{m^2} / 1 = \mathrm{m^3}$, which matches $S$. A 49 mm strip is a reasonable size for this kind of part.

A second, linear example: a spring reads 12 N at 10 mm of stretch and 30 N at 25 mm. The slope is $k = \dfrac{30 - 12}{0.025 - 0.010} = 1200\ \mathrm{N/m}$. Predicted force at 18 mm is $12 + 1200(0.018 - 0.010) = 21.6\ \mathrm{N}$.

## Practice

1. Solve $3x - 7 = 11$.
2. Solve $x^2 - 5x + 6 = 0$. Give both roots.
3. A spring stretches 4 mm under an 8 N load. Find its stiffness $k$ in N/m.
4. A rectangular section must have $S = 1.0 \times 10^{-5}\ \mathrm{m^3}$ with $b = 0.04\ \mathrm{m}$. Find $h$ in meters.

<details><summary>Answers</summary>

1. $x = 6$
2. $x = 2$ and $x = 3$
3. $k = 2000\ \mathrm{N/m}$
4. $h \approx 0.0387\ \mathrm{m}$

</details>

## Common mistakes

- Dropping a negative sign when moving a term across the equals sign.
- Taking the square root of only one side of an equation, or forgetting the $\pm$ sign when solving $x^2 = c$.
- Mixing units, such as millimeters in one term and meters in another. Convert first.
- Canceling a common factor that is zero. Divide only by quantities you know are nonzero.
- Writing $\sqrt{a + b}$ as $\sqrt{a} + \sqrt{b}$. This is not true in general.

## Go deeper

- [College Algebra 2e](https://openstax.org/books/college-algebra-2e/pages/1-introduction-to-prerequisites) by OpenStax: free textbook, chapter 1 reviews the prerequisites.
- [Algebra notes](https://tutorial.math.lamar.edu/classes/alg/alg.aspx) by Paul Dawkins, Paul's Online Math Notes: worked examples on equations, inequalities, and functions.
- Next: [Trigonometry](02-trigonometry.md), which needs these skills for angles and right triangles.
- [Math reference](reference.md): the lookup sheet for this topic.
