# Numerical methods

**Type:** lesson

Many engineering equations cannot be solved by hand. Numerical methods replace an exact answer with a sequence of approximations that you can carry out, check, and stop when the error is small enough. Engineers use them for root finding, integrals without closed forms, and differential equations solved over time.

**Prerequisites:** [Single-variable calculus](03-single-variable-calculus.md), [Differential equations](06-differential-equations.md), [Linear algebra](05-linear-algebra.md)
**Time:** 30-40 h

## Core ideas

- A root is a value $x$ where $f(x) = 0$. Root finding searches for it.
- Bisection is the safest root method. Keep an interval $[a, b]$ where $f(a)$ and $f(b)$ have opposite signs, then halve it. It always converges, but slowly: each step gains about one binary digit of accuracy.
- Newton's method uses the tangent line. Starting from a guess $x_0$, the next guess is $x_{n+1} = x_n - f(x_n)/f'(x_n)$. It converges very fast near the root, but can fail if the starting guess is poor or $f'$ is near zero.
- Numerical integration replaces an integral with a weighted sum. The trapezoidal rule uses straight segments. Simpson's rule uses parabolas and is more accurate for the same number of points.
- Truncation error comes from the method itself, for example from replacing a curve with a straight line. Round-off error comes from storing numbers with finite digits. Both matter, and you should know which one dominates.
- Euler's method solves $y' = f(t, y)$ by stepping forward with $y_{n+1} = y_n + h\,f(t_n, y_n)$. It is simple and first-order accurate: halving the step size roughly halves the error. Higher-order methods such as Runge-Kutta are better in practice.
- Convergence check: refine the step or the grid and see whether the answer changes. If halving $h$ changes the answer by less than your tolerance, you can trust it.

## Key equations

Newton's method for $f(x) = 0$:

$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$

Composite trapezoidal rule on $n$ equal intervals of width $h = (b - a)/n$:

$$\int_a^b f(x)\,dx \approx \frac{h}{2}\left[f(x_0) + 2\sum_{i=1}^{n-1} f(x_i) + f(x_n)\right]$$

Euler's method for $y' = f(t, y)$ with step $h$ (s):

$$y_{n+1} = y_n + h\,f(t_n, y_n)$$

Error rule for a method of order $p$: halving $h$ reduces the error by about $2^p$. The trapezoidal rule is order 2, so halving $h$ should cut its error by about 4.

## Worked example

**Given:** Find the root of $f(x) = x^3 - 2x - 5 = 0$ near $x = 2$.

**Find:** The root to at least six significant figures, and the number of Newton steps needed.

**Assumptions:** $f$ is smooth near the root, and $f'(x) = 3x^2 - 2$ is nonzero there.

**Solution:**

1. Start with $x_0 = 2$. Then $f(2) = 8 - 4 - 5 = -1$ and $f'(2) = 10$.
2. First step: $x_1 = 2 - (-1)/10 = 2.1$.
3. Second step: $f(2.1) = 0.061$, $f'(2.1) = 11.23$, so $x_2 = 2.1 - 0.061/11.23 = 2.094568$.
4. Third step: $x_3 = 2.0945515$. The change from step 2 to step 3 is about $1.7 \times 10^{-5}$.
5. Fourth step: $x_4 = 2.0945515$ to 10 digits. Residual $f(x_4) \approx 10^{-15}$, which is round-off.

**Answer:** $x \approx 2.0945515$. Newton converged in 3 to 4 steps, while bisection on $[2, 3]$ would need about 20 steps for similar accuracy.

**Sanity check:** Substitute back: $2.0945515^3 - 2(2.0945515) - 5 \approx 0$. The error falls from about $5 \times 10^{-3}$ after step 1 to about $2 \times 10^{-5}$ after step 2, then to round-off after step 3. That fast drop is the quadratic convergence Newton's method should show.

A second example, integration error. Estimate $\int_0^1 e^{-x^2}\,dx$, whose exact value is $0.746824$. The trapezoidal rule with $n = 4$ gives $0.742984$, an error of $-0.00384$. With $n = 8$ the error is $-0.00096$. Halving $h$ reduced the error by a factor of about 4, as the order-2 rule predicts.

## Practice

1. Apply one Newton step to $x^2 - 2 = 0$ starting from $x_0 = 1$. Give $x_1$ to six decimal places.
2. Apply the trapezoidal rule with $n = 2$ to $\int_0^1 x^2\,dx$. Give the result and the error against the exact value $1/3$.
3. Apply three bisection steps to $f(x) = x^3 - 2x - 5$ on $[2, 3]$. Give the midpoint after the third step.
4. Take one Euler step for $y' = -y$ with $y(0) = 1$ and $h = 0.1$. Give $y_1$.

<details><summary>Answers</summary>

1. $x_1 = 1.500000$
2. $0.375$, error $+0.0417$
3. Midpoint $2.0625$ (bracket $[2.0, 2.125]$)
4. $y_1 = 0.9$

</details>

## Common mistakes

- Starting Newton's method at a point where $f'$ is close to zero. The next guess shoots far away.
- Stopping when the change in $x$ is small without checking the residual $f(x)$.
- Using too few intervals in a trapezoidal rule and trusting the answer without a refinement check.
- Taking Euler steps that are too large. The method can blow up when $h$ exceeds the stability limit of the problem.
- Confusing round-off error with truncation error. Smaller steps reduce truncation error but can increase round-off.

## Go deeper

- [SciPy Tutorial](https://docs.scipy.org/doc/scipy/tutorial/index.html) by the SciPy project: sections on integration (`scipy.integrate`), optimization and root finding (`scipy.optimize`), and linear algebra.
- [Engineering LibreTexts](https://eng.libretexts.org/) by LibreTexts: free, open-access engineering texts that include numerical methods chapters.
- Next: [Software solvers](09-software-solvers.md).
