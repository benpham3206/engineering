# Propagating uncertainty and significant figures

**Type:** lesson

Most results are calculated from several measured quantities, and each one carries its own uncertainty. Propagation of uncertainty is the method for finding the uncertainty of the result. Significant figures are the simpler rule for writing the result so it does not claim more precision than you have.

**Prerequisites:** [02 - Precision, accuracy, and uncertainty](02-precision-accuracy-and-uncertainty.md)
**Time:** 6-8 h

## Core ideas

- An **input** is a measured quantity such as length $L$ or voltage $V$. Each input has a standard uncertainty $u(x)$.
- A **result** is a function of the inputs, such as area $A = L \times W$. Its uncertainty comes from how the input uncertainties feed through the function.
- If the inputs are **uncorrelated** (their errors do not depend on each other), their effects add in quadrature, which means the square root of the sum of squares. This is the root-sum-square (RSS) rule. NIST TN 1297 calls it the law of propagation of uncertainty and gives it as the standard way to combine uncertainty components.
- RSS is smaller than a worst-case sum, which adds all errors in the same direction. The worst case is useful as a bound but usually too pessimistic for a best estimate.
- **Significant figures** (sig figs) are the digits you actually know. For a result, keep digits that the uncertainty supports. A common rule: round the uncertainty to one or two significant figures, then round the value to the same decimal place.
- For multiplication and division, the result keeps the same number of sig figs as the input with the fewest. For addition and subtraction, the result keeps the same number of decimal places as the input with the fewest.
- Exact numbers, such as counting 4 holes or the definition 1 in = 25.4 mm, do not limit sig figs.

## Key equations

For a result $f(x_1, x_2, \ldots, x_n)$ with uncorrelated inputs, the combined standard uncertainty is

$$u_c(f) = \sqrt{\sum_{i=1}^{n} \left(\frac{\partial f}{\partial x_i}\right)^2 u^2(x_i)}$$

where $\partial f / \partial x_i$ is the sensitivity of $f$ to input $x_i$, in the units of $f$ per unit of $x_i$.

Useful special cases:

- Sum or difference, $f = a \pm b$: $\quad u_f = \sqrt{u_a^2 + u_b^2}$
- Product or quotient, $f = a b$ or $f = a/b$: $\quad \left(\dfrac{u_f}{|f|}\right)^2 = \left(\dfrac{u_a}{a}\right)^2 + \left(\dfrac{u_b}{b}\right)^2$

Worst-case bound for a product, for comparison: $\quad \Delta_{\text{max}} = |b|\,u_a + |a|\,u_b$

## Worked example

**Given:** A rectangular plate measures $L = 120.0 \pm 0.2\ \text{mm}$ and $W = 45.0 \pm 0.1\ \text{mm}$ (standard uncertainties). Also a block has mass $m = 2.736 \pm 0.001\ \text{g}$ and volume $V = 1.04 \pm 0.01\ \text{cm}^3$.

**Find:** (a) the area and its uncertainty, (b) the density with its uncertainty and correct sig figs.

**Assumptions:** $L$ and $W$ are independent, and $m$ and $V$ are independent.

**Solution (a):**

- Area: $A = L W = 120.0 \times 45.0 = 5400\ \text{mm}^2$
- Relative uncertainties: $u_L / L = 0.2/120 = 0.00167$ and $u_W / W = 0.1/45 = 0.00222$
- RSS of relative terms: $\sqrt{0.00167^2 + 0.00222^2} = 0.00278$, which is 0.278%
- Absolute uncertainty: $u_A = 0.00278 \times 5400 = 15.0\ \text{mm}^2$
- Worst-case bound for comparison: $W u_L + L u_W = 45.0 \times 0.2 + 120.0 \times 0.1 = 21\ \text{mm}^2$. The RSS value (15 mm²) is smaller, as expected.

**Solution (b):**

- Density: $\rho = m / V = 2.736 / 1.04 = 2.6308\ \text{g/cm}^3$
- Relative uncertainties: $u_m / m = 0.001/2.736 = 0.000366$ and $u_V / V = 0.01/1.04 = 0.00962$
- RSS: $\sqrt{0.000366^2 + 0.00962^2} = 0.00962$, which is 0.962%
- Absolute uncertainty: $u_\rho = 0.00962 \times 2.6308 = 0.0253\ \text{g/cm}^3$
- Sig figs: the volume $1.04$ has 3 significant figures, so the value must not carry more than about 3. The uncertainty rounds to two significant figures, 0.025. The value is then rounded to the thousandths place to match.

**Answer:** (a) $A = 5400 \pm 15\ \text{mm}^2$. (b) $\rho = 2.631 \pm 0.025\ \text{g/cm}^3$.

**Sanity check:** The density uncertainty is dominated by the volume, which has the larger relative uncertainty (0.96% against 0.04%). Without the mass term the relative uncertainty is still 0.962%, so the mass barely matters and the volume is the weak link. Water is 1.00 g/cm³, so 2.63 is a plausible metal-like density.

## Practice

1. Two lengths are $a = 4.20 \pm 0.03\ \text{mm}$ and $b = 1.50 \pm 0.04\ \text{mm}$. Find $a + b$ and its uncertainty.
2. Power $P = V I$ with $V = 12.0 \pm 0.1\ \text{V}$ and $I = 2.00 \pm 0.02\ \text{A}$. Find $P$ and $u_P$.
3. Compute $0.00305 \times 4.0$ and round to the correct number of significant figures. (Hint: the factor 4.0 has two significant figures.)

<details><summary>Answers</summary>

1. 5.70 mm, uncertainty 0.05 mm.
2. 24.0 W, uncertainty 0.31 W.
3. 0.012

</details>

## Common mistakes

- Adding uncertainties linearly for independent inputs. Use RSS unless the errors are known to be fully correlated.
- Forgetting to square the sensitivity in the RSS formula. For $f = a^2$, the sensitivity is $2a$, not $1$.
- Carrying every calculator digit into the final answer. Round the uncertainty first, then the value.
- Applying the addition rule for decimal places to a multiplication, or the multiplication rule to an addition.
- Treating exact conversion factors or counted numbers as limiting the sig figs.

## Go deeper

- [Guidelines for Evaluating and Expressing the Uncertainty of NIST Measurement Results (TN 1297)](https://www.nist.gov/pml/nist-technical-note-1297) by NIST: section 5 and Appendix A give the RSS propagation law.
- [University Physics Volume 1, Chapter 1: Introduction](https://openstax.org/books/university-physics-volume-1/pages/1-introduction) by OpenStax: significant figures and estimates in a physics context.
- [Introduction to Probability and Statistics (18.05)](https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2014/) by MIT OpenCourseWare: variance and the algebra behind independent-error addition.
- [Measurement reference](reference.md): the lookup sheet for this topic.
