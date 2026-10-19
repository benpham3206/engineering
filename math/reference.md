# Math reference

**Type:** reference
**Verify:** strict

Mathematics is the language of quantities, patterns, and change, written in numbers and symbols. This sheet is a dense lookup of the algebra, calculus, linear algebra, differential equation, transform, Fourier, probability, and numerical formulas an engineer needs mid-task, with the assumptions under which each one holds.

## Principles

- Units balance in every term, or the answer is wrong. Check units before checking arithmetic.
- Every model has a regime. Linear, small-angle, small-deflection, steady-state, lumped, and independent-sample assumptions each fail somewhere. Name the one you rely on.
- A numerical answer is a claim that needs evidence: refine the grid, check a residual, or test a known special case.
- Convergence order tells you how error scales with step size. Confirm it with two resolutions before trusting the result.
- Rates integrate to totals and totals differentiate to rates. Identify which one the problem gives you.
- Probability describes a model; statistics estimates the model from data. A confidence level describes the procedure, not one fixed interval.
- Real symmetric matrices have real eigenvalues. Do not assume this for a general matrix.
- Dimensionless groups (damping ratio, Biot number, ratios of frequencies) decide which regime applies and let a result scale.
- Gravity, atmosphere, and temperature are not fixed. Write the general form ($W = m g$ with $g$ the local value) and specialize to Earth only as one case.
- Use the simplest method that meets the tolerance: closed form, then series, then numerical solver.

## Algebra and logarithms

Exponent rules, for $a > 0$ unless noted:

| Rule | Form |
|---|---|
| Product | $a^m a^n = a^{m+n}$ |
| Quotient | $a^m / a^n = a^{m-n}$ |
| Power of a power | $(a^m)^n = a^{mn}$ |
| Zero exponent | $a^0 = 1$ (for $a \ne 0$) |
| Negative exponent | $a^{-n} = 1/a^n$ |
| Fractional exponent | $a^{m/n} = \sqrt[n]{a^m}$ |

Logarithm rules, for $x, y > 0$ and base $b > 0$, $b \ne 1$. $\ln$ is base $e$:

- $\log(xy) = \log x + \log y$
- $\log(x/y) = \log x - \log y$
- $\log(x^n) = n \log x$
- $\log_b x = \dfrac{\ln x}{\ln b}$ (change of base)
- $e^{\ln x} = x$ and $\ln e^{x} = x$

Holds when: logarithms have real, positive arguments.

Breaks when: a log is taken of zero or a negative number (undefined for real results); $\sqrt{ab} = \sqrt{a}\sqrt{b}$ and $(a^m)^n = a^{mn}$ fail for negative bases with fractional exponents on the principal branch.

Decibels, with $P$ power and $A$ amplitude:

$$L = 10 \log_{10}\frac{P_2}{P_1}\ \mathrm{dB}, \qquad L = 20 \log_{10}\frac{A_2}{A_1}\ \mathrm{dB}$$

- A factor of 2 in power is 3.01 dB. A factor of 2 in amplitude is 6.02 dB.

Quadratic $a x^2 + b x + c = 0$, $a \ne 0$, discriminant $\Delta = b^2 - 4ac$:

$$x = \frac{-b \pm \sqrt{\Delta}}{2a}$$

- $\Delta > 0$: two distinct real roots. $\Delta = 0$: one repeated root. $\Delta < 0$: a complex-conjugate pair.
- Vieta: sum of roots $= -b/a$, product $= c/a$.
- Numerical stability: when $b^2 \gg 4|ac|$, subtracting nearly equal numbers loses digits. Compute $q = -\tfrac{1}{2}\left(b + \mathrm{sgn}(b)\sqrt{\Delta}\right)$ (no cancellation). The two roots are $x_1 = q/a$ and $x_2 = c/q$.

Geometric series, for $r \ne 1$:

$$\sum_{k=0}^{n-1} r^k = \frac{1 - r^n}{1 - r}, \qquad \sum_{k=0}^{\infty} r^k = \frac{1}{1-r} \quad (|r| < 1)$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $P_1$, $P_2$ | reference and measured power | W |
| $A_1$, $A_2$ | reference and measured amplitude | dimensionless |
| $L$ | logarithmic level difference | dimensionless |
| $a$, $b$, $c$ | quadratic coefficients | dimensionless |
| $x$ | quadratic unknown | dimensionless |
| $\Delta$ | quadratic discriminant | dimensionless |
| $r$ | geometric-series ratio | dimensionless |
| $n$, $k$ | integer indices | dimensionless |

Source and basis: derived from the definition of a logarithm, completing the square, and subtracting $r$ times the geometric sum from itself.

## Trigonometry

Radians: $\theta_{\mathrm{rad}} = \theta_{\mathrm{deg}}\,\pi/180$. One radian is $57.30^\circ$. Python `math` and NumPy trig functions take radians.

Exact values (typical; memorize these):

| Angle | $0^\circ$ | $30^\circ$ | $45^\circ$ | $60^\circ$ | $90^\circ$ |
|---|---|---|---|---|---|
| $\sin$ | 0 | $1/2$ | $\sqrt{2}/2$ | $\sqrt{3}/2$ | 1 |
| $\cos$ | 1 | $\sqrt{3}/2$ | $\sqrt{2}/2$ | $1/2$ | 0 |
| $\tan$ | 0 | $1/\sqrt{3}$ | 1 | $\sqrt{3}$ | undefined |

Identities:

- $\sin^2\theta + \cos^2\theta = 1$, $\tan\theta = \sin\theta/\cos\theta$
- $\sin(a \pm b) = \sin a \cos b \pm \cos a \sin b$
- $\cos(a \pm b) = \cos a \cos b \mp \sin a \sin b$
- $\sin 2a = 2\sin a \cos a$, $\cos 2a = \cos^2 a - \sin^2 a = 1 - 2\sin^2 a = 2\cos^2 a - 1$
- $\sin^2(a/2) = (1 - \cos a)/2$, $\cos^2(a/2) = (1 + \cos a)/2$
- $\sin a \cos b = \tfrac{1}{2}[\sin(a+b) + \sin(a-b)]$
- $\sin a \sin b = \tfrac{1}{2}[\cos(a-b) - \cos(a+b)]$
- Euler: $e^{i\theta} = \cos\theta + i\sin\theta$

Triangles, sides $a, b, c$ (m), opposite angles $A, B, C$, circumradius $R$ (m):

$$\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C} = 2R, \qquad c^2 = a^2 + b^2 - 2ab\cos C, \qquad \text{Area} = \tfrac{1}{2} a b \sin C$$

Holds when: the triangle lies in a Euclidean plane.

Breaks when: the triangle lies on a curved surface (use spherical trigonometry, where the law of cosines gains correction terms), or when an angle in degrees is fed to a radian function (a common and silent error).

Small-angle approximations, $x$ in radians:

$$\sin x \approx x - \frac{x^3}{6}, \qquad \cos x \approx 1 - \frac{x^2}{2}, \qquad \tan x \approx x + \frac{x^3}{3}$$

- Holds when: $|x| \ll 1$. At $x = 0.1$ rad, $\sin x$ is $0.09983$ and the error of $\sin x \approx x$ is $0.17\%$.
- Breaks when: $x$ is in degrees (a $10^\circ$ angle is $0.1745$ rad, error about $0.5\%$ for $\sin x \approx x$, but the input unit must still be radians).

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\theta$, $a$, $b$, $A$, $B$, $C$ | angles | rad |
| $\theta_{\mathrm{deg}}$ | angle expressed in degrees | dimensionless |
| $a$, $b$, $c$ in a triangle | side lengths | m |
| $R$ | circumradius | m |
| $x$ | small angle in the approximation | rad |

Source and basis: derived from the unit circle and angle addition; the triangle relations follow from right-triangle geometry and projection.

## Calculus

For derivatives, integrals, and series, see the [calculus reference](reference-calculus.md#derivatives).

The Leibniz rule for a variable limit is $\frac{d}{dx}\int_{a(x)}^{b(x)} f(x,t)\,dt = f(x,b)\,b' - f(x,a)\,a' + \int_{a(x)}^{b(x)} \frac{\partial f}{\partial x}\,dt$.

## Vector calculus

See the calculus reference sections on [vector calculus](reference-calculus.md#vector-calculus), [integral theorems](reference-calculus.md#integral-theorems), and [curvilinear forms](reference-calculus.md#curvilinear-forms).

The product identities not listed there are $\nabla\times(f\mathbf{F}) = f\,\nabla\times\mathbf{F} + \nabla f \times \mathbf{F}$ and $\nabla\cdot(\mathbf{F}\times\mathbf{G}) = \mathbf{G}\cdot(\nabla\times\mathbf{F}) - \mathbf{F}\cdot(\nabla\times\mathbf{G})$.

## Linear algebra

For vectors, matrices, linear systems, eigenvalues, and conditioning, see the [linear algebra and differential equations reference](reference-linear-algebra-differential-equations.md#vectors-and-matrices).

The Hilbert matrix family is $H_{ij} = 1/(i+j-1)$.

## Ordinary differential equations

See [first-order ODEs](reference-linear-algebra-differential-equations.md#first-order-odes), [second-order linear ODEs](reference-linear-algebra-differential-equations.md#second-order-linear-odes), and [systems and state space](reference-linear-algebra-differential-equations.md#systems-and-state-space).

The lumped-capacity cooling solution is $T(t) = T_a + (T_0 - T_a)e^{-kt}$, with $k = h_c A/(\rho V c_p)$.

For a mass-spring-damper system, $m x'' + c x' + k x = F(t)$, $\omega_n = \sqrt{k/m}$, $f_n = \omega_n/(2\pi)$, and $\zeta = c/(2\sqrt{km}) = c/(2m\omega_n)$. Its characteristic equation is $r^2 + 2\zeta\omega_n r + \omega_n^2 = 0$, with roots $r = -\zeta\omega_n \pm \omega_n\sqrt{\zeta^2 - 1}$.

The free responses are $x = A\cos\omega_n t + B\sin\omega_n t$ when $\zeta=0$; $x = e^{-\zeta\omega_n t}(A\cos\omega_d t + B\sin\omega_d t)$ when $0 < \zeta < 1$, where $\omega_d = \omega_n\sqrt{1-\zeta^2}$; $x = (A+Bt)e^{-\omega_n t}$ when $\zeta=1$; and $x = A e^{r_1t}+B e^{r_2t}$ when $\zeta>1$, with $r_{1,2}=-\omega_n(\zeta\mp\sqrt{\zeta^2-1})$. For an underdamped response, $A=x_0$ and $B=(v_0+\zeta\omega_nx_0)/\omega_d$; the logarithmic decrement is $\delta=2\pi\zeta/\sqrt{1-\zeta^2}$.

For a harmonic force $F_0\cos\omega t$, $r=\omega/\omega_n$, $X=(F_0/k)/\sqrt{(1-r^2)^2+(2\zeta r)^2}$, and $\phi=\operatorname{atan2}(2\zeta r,1-r^2)$. When $\zeta<1/\sqrt{2}$, the dynamic amplification peaks at $r=\sqrt{1-2\zeta^2}$ with value $1/(2\zeta\sqrt{1-\zeta^2})$.

For a system of masses and springs, $\mathbf{M}\ddot{\mathbf{x}}+\mathbf{C}\dot{\mathbf{x}}+\mathbf{K}\mathbf{x}=\mathbf{f}(t)$. With $\mathbf{z}=(\mathbf{x},\dot{\mathbf{x}})$, the equivalent first-order form is $\dot{\mathbf{z}}=\mathbf{A}\mathbf{z}+\mathbf{b}(t)$, where $\mathbf{A}=\begin{pmatrix}\mathbf{0}&\mathbf{I}\\-\mathbf{M}^{-1}\mathbf{K}&-\mathbf{M}^{-1}\mathbf{C}\end{pmatrix}$ and $\mathbf{b}=(\mathbf{0},\mathbf{M}^{-1}\mathbf{f}(t))$. The unforced system decays when every eigenvalue of $\mathbf{A}$ has negative real part.

## Laplace transform

For the one-sided transform convention, transform pairs, rules, and theorems, see the [Laplace transform reference](reference-linear-algebra-differential-equations.md#laplace-transform).

The hyperbolic pairs are $\mathcal{L}\{\sinh at\} = a/(s^2-a^2)$ and $\mathcal{L}\{\cosh at\} = s/(s^2-a^2)$.

## Fourier series

For the Fourier series convention and coefficient definitions, see the [Fourier series section](reference-linear-algebra-differential-equations.md#fourier-series-and-transform).

## Probability and statistics

See the [distributions](reference-probability-numerical-methods.md#distributions), [sampling and estimation](reference-probability-numerical-methods.md#sampling-and-estimation), and [hypothesis tests](reference-probability-numerical-methods.md#hypothesis-tests) sections of the probability and numerical methods reference.

## Numerical methods

For root finding, quadrature, ODE solvers, and numerical error, see the [probability and numerical methods reference](reference-probability-numerical-methods.md#roots-and-nonlinear-systems).

## Checklists

Before trusting a formula result:

- [ ] Units balance in every term, in SI, after conversion.
- [ ] Angle mode is radians in code. Degrees are converted for display only.
- [ ] Assumptions named: linear, small deflection, steady, lumped, periodic, independent, and so on.
- [ ] The dimensionless group (for example $\zeta$ or $\mathrm{Bi}$) is inside the validity range.
- [ ] Sign checked: the physical direction of flux, displacement, or force matches intuition.
- [ ] A limiting case reduces correctly (zero load, very large stiffness, $t \to \infty$, $r \to 0$).

Before trusting a numerical result:

- [ ] Refinement: halve $h$ or double $n$. The change is below tolerance.
- [ ] Observed order matches the theoretical order.
- [ ] Residual: substitute the answer back ($f(x)\approx 0$, or $\mathbf{A}\mathbf{x} - \mathbf{b}\approx\mathbf{0}$).
- [ ] Stability: $h$ is below the limit for the fastest mode.
- [ ] Conditioning: estimate $\kappa$; digits lost is about $\log_{10}\kappa$.
- [ ] Round-off: $h$ is not below about $\sqrt{\varepsilon}$ (forward difference) or $\varepsilon^{1/3}$ (central difference).
- [ ] Tolerances and stopping criteria recorded with the result.

Before trusting a statistical result:

- [ ] Samples independent, with no drift, batch effect, or time trend.
- [ ] Distribution assumption checked (plot, residuals, tail behavior).
- [ ] $n$ stated. $t$ used when $\sigma$ is estimated.
- [ ] Effect size compared with tolerance, not only significance.
- [ ] Any tail probability beyond the data range is flagged as model-dependent.

Before releasing a design that depends on dynamics:

- [ ] Natural frequency checked against every forcing frequency.
- [ ] Forced response computed, not only the free response.
- [ ] Damping ratio taken from measurement or a stated typical value, with its source.
- [ ] Rule of thumb: keep forcing more than about 20% away from a natural frequency (basis: the half-power band near resonance is about $\pm\zeta$ and stiffness and mass tolerances shift $\omega_n$ by several percent). Limit: this margin does not replace a forced-response analysis, and it does not hold for strongly nonlinear systems.

## Sanity checks

- Powers: $2^{10} \approx 10^3$, $2^{20} \approx 10^6$, $2^{30} \approx 10^9$.
- Logs: $\ln 10 \approx 2.303$, $\log_{10} 2 \approx 0.301$, $\ln 2 \approx 0.693$.
- Constants: $e \approx 2.718$, $\pi \approx 3.142$, $\sqrt{2} \approx 1.414$, $\sqrt{\pi} \approx 1.772$ (also $\int_{-\infty}^{\infty} e^{-x^2}\,dx$).
- Angles: $1\ \mathrm{rad} \approx 57.3^\circ$; $1^\circ \approx 0.01745$ rad, so $\sin 1^\circ \approx 0.01745$.
- Trig: $\sin^2 + \cos^2 = 1$ at any angle you test. Components of a vector never exceed its magnitude.
- Eigenvalues: their sum equals the trace and their product equals the determinant. If not, you have an arithmetic error.
- Scaling: doubling $k$ in a spring-mass system raises $\omega_n$ by $\sqrt{2}$. Doubling cantilever length multiplies tip deflection by $2^3 = 8$.
- Time constant: an exponential decay with rate $k$ falls to $1/e \approx 0.368$ at $t = 1/k$ and to $1/2$ at $t = 0.693/k$.
- Probability: every probability lies in $[0, 1]$, and the outcomes of a complete set sum to 1.
- Normal: about 68% of values lie within $1\sigma$, about 95% within $2\sigma$, about 99.7% within $3\sigma$.
- Newton: the number of correct digits roughly doubles per step near a simple root. If it does not, the root is multiple or the guess is poor.
- Trapezoid: if halving $h$ does not cut the error by about 4, the integrand or the code is wrong.
- Conditioning: if the answer changes in the fourth digit when an input changes in the tenth digit, expect $\kappa \approx 10^6$.
- Convexity: a convex function's chord lies above the curve, so a trapezoid estimate is high.

## Further reference

Classic books by name. Paid titles are named only; no links.

- Stewart, *Calculus* (paid, multiple editions): single and multivariable calculus.
- Boyce and DiPrima, *Elementary Differential Equations and Boundary Value Problems* (paid): ODEs, Laplace transforms, Fourier series.
- Spiegel, *Schaum's Outline of Laplace Transforms* (paid): transform tables and worked inversion.
- Strang, *Introduction to Linear Algebra* (paid): matrices, eigenvalues, and conditioning.
- Golub and Van Loan, *Matrix Computations* (paid): numerical linear algebra, LU, Cholesky, conditioning.
- Burden and Faires, *Numerical Analysis* (paid): root finding, quadrature, and ODE solvers with error analysis.
- Montgomery, *Design and Analysis of Experiments* (paid): confidence intervals, design, and inference for engineers.
- [NIST/SEMATECH e-Handbook of Statistical Methods](https://www.itl.nist.gov/div898/handbook/) by the U.S. National Institute of Standards and Technology: free. Distributions, intervals, and hypothesis tests.
- [NIST Digital Library of Mathematical Functions](https://dlmf.nist.gov/) by NIST: free. Special functions and identities.
- Hamming, *Numerical Methods for Scientists and Engineers* (paid): round-off, stability, and practical error control.
