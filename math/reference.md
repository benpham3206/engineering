# Math reference

**Type:** reference

A dense lookup sheet of the algebra, calculus, linear algebra, differential equation, transform, Fourier, probability, and numerical formulas an engineer needs mid-task, with the assumptions under which each one holds.

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

Holds when: real, positive arguments. Breaks when: a log is taken of zero or a negative number (undefined for real results); $\sqrt{ab} = \sqrt{a}\sqrt{b}$ and $(a^m)^n = a^{mn}$ fail for negative bases with fractional exponents on the principal branch.

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

Holds when: plane (Euclidean) geometry. Breaks when: the triangle lies on a curved surface (use spherical trigonometry, where the law of cosines gains correction terms), or when an angle in degrees is fed to a radian function (a common and silent error).

Small-angle approximations, $x$ in radians:

$$\sin x \approx x - \frac{x^3}{6}, \qquad \cos x \approx 1 - \frac{x^2}{2}, \qquad \tan x \approx x + \frac{x^3}{3}$$

- Holds when: $|x| \ll 1$. At $x = 0.1$ rad, $\sin x$ is $0.09983$ and the error of $\sin x \approx x$ is $0.17\%$.
- Breaks when: $x$ is in degrees (a $10^\circ$ angle is $0.1745$ rad, error about $0.5\%$ for $\sin x \approx x$, but the input unit must still be radians).

## Calculus

### Derivatives (typical table)

| $f(x)$ | $f'(x)$ |
|---|---|
| $x^n$ | $n x^{n-1}$ |
| $e^{ax}$ | $a e^{ax}$ |
| $a^x$ | $a^x \ln a$ |
| $\ln x$ ($x > 0$) | $1/x$ |
| $\log_b x$ | $1/(x \ln b)$ |
| $\sin x$ | $\cos x$ |
| $\cos x$ | $-\sin x$ |
| $\tan x$ | $\sec^2 x$ |
| $\arcsin x$ | $1/\sqrt{1 - x^2}$ |
| $\arccos x$ | $-1/\sqrt{1 - x^2}$ |
| $\arctan x$ | $1/(1 + x^2)$ |
| $\sinh x$ | $\cosh x$ |
| $\cosh x$ | $\sinh x$ |
| $\tanh x$ | $\operatorname{sech}^2 x$ |

Rules: sum, product $(fg)' = f'g + fg'$, quotient $(f/g)' = (f'g - fg')/g^2$, chain $\dfrac{d}{dx} f(g(x)) = f'(g(x))\,g'(x)$.

### Integrals (indefinite; add $C$)

| $\int f\,dx$ | Result (conditions) |
|---|---|
| $x^n$ | $\dfrac{x^{n+1}}{n+1}$ ($n \ne -1$) |
| $1/x$ | $\ln \lvert x \rvert$ |
| $e^{ax}$ | $\dfrac{e^{ax}}{a}$ ($a \ne 0$) |
| $\sin ax$ | $-\dfrac{\cos ax}{a}$ |
| $\cos ax$ | $\dfrac{\sin ax}{a}$ |
| $\tan x$ | $-\ln \lvert\cos x\rvert$ |
| $\sec^2 x$ | $\tan x$ |
| $\ln x$ | $x\ln x - x$ |
| $x e^{ax}$ | $e^{ax}\left(\dfrac{x}{a} - \dfrac{1}{a^2}\right)$ |
| $e^{ax}\sin bx$ | $\dfrac{e^{ax}(a\sin bx - b\cos bx)}{a^2 + b^2}$ |
| $e^{ax}\cos bx$ | $\dfrac{e^{ax}(a\cos bx + b\sin bx)}{a^2 + b^2}$ |
| $\dfrac{1}{x^2 + a^2}$ | $\dfrac{1}{a}\arctan\dfrac{x}{a}$ ($a \ne 0$) |
| $\dfrac{1}{\sqrt{a^2 - x^2}}$ | $\arcsin\dfrac{x}{a}$ ($\lvert x\rvert < a$) |
| $\dfrac{1}{\sqrt{x^2 + a^2}}$ | $\ln\left(x + \sqrt{x^2 + a^2}\right)$ |

Integration by parts: $\int u\,dv = uv - \int v\,du$.

Leibniz rule for a variable limit:

$$\frac{d}{dx}\int_{a(x)}^{b(x)} f(x,t)\,dt = f(x,b)\,b' - f(x,a)\,a' + \int_{a(x)}^{b(x)} \frac{\partial f}{\partial x}\,dt$$

Fundamental theorem: $\int_a^b f\,dx = F(b) - F(a)$ with $F' = f$.

Standard limits:

- $\lim_{x\to 0} \dfrac{\sin x}{x} = 1$, $\lim_{x\to 0}\dfrac{1 - \cos x}{x^2} = \tfrac{1}{2}$, $\lim_{x\to 0}\dfrac{e^x - 1}{x} = 1$
- $\lim_{x\to 0^+} x\ln x = 0$, $\lim_{n\to\infty}\left(1 + \dfrac{x}{n}\right)^n = e^x$
- L'Hopital's rule applies only to $0/0$ or $\infty/\infty$ forms.

Holds when: the function is continuous (or piecewise continuous) on the interval. Breaks when: the integrand is singular inside the interval (an improper integral must be split and each piece checked) or the antiderivative is taken across a branch cut.

### Taylor series (about $a = 0$ unless noted)

| Function | Series | Radius / convergence |
|---|---|---|
| $e^x$ | $\sum_{n\ge 0} \dfrac{x^n}{n!}$ | all $x$ |
| $\sin x$ | $\sum_{n\ge 0} (-1)^n \dfrac{x^{2n+1}}{(2n+1)!}$ | all $x$ |
| $\cos x$ | $\sum_{n\ge 0} (-1)^n \dfrac{x^{2n}}{(2n)!}$ | all $x$ |
| $\sinh x$ | $\sum_{n\ge 0} \dfrac{x^{2n+1}}{(2n+1)!}$ | all $x$ |
| $\cosh x$ | $\sum_{n\ge 0} \dfrac{x^{2n}}{(2n)!}$ | all $x$ |
| $\ln(1+x)$ | $\sum_{n\ge 1} (-1)^{n+1} \dfrac{x^n}{n}$ | $-1 < x \le 1$ |
| $\dfrac{1}{1-x}$ | $\sum_{n\ge 0} x^n$ | $\lvert x\rvert < 1$ |
| $\arctan x$ | $\sum_{n\ge 0} (-1)^n \dfrac{x^{2n+1}}{2n+1}$ | $-1 \le x \le 1$ |
| $(1+x)^p$ | $\sum_{n\ge 0} \binom{p}{n} x^n$ | $\lvert x\rvert < 1$ (general $p$) |

Examples from the binomial row: $\sqrt{1+x} \approx 1 + \tfrac{x}{2} - \tfrac{x^2}{8} + \tfrac{x^3}{16}$; $1/\sqrt{1+x} \approx 1 - \tfrac{x}{2} + \tfrac{3x^2}{8}$.

Lagrange remainder after the term of degree $n$:

$$\lvert R_n(x)\rvert \le \frac{M\,\lvert x - a\rvert^{n+1}}{(n+1)!}, \qquad M \ge \max \lvert f^{(n+1)}\rvert \text{ between } a \text{ and } x$$

- Check: $e^{0.1}$ with terms through $x^2/2$ has error $1.71\times10^{-4}$. The bound with $M = e^{0.1} \approx 1.106$ is $1.84\times10^{-4}$, which holds.
- For an alternating series with decreasing terms, the error is no larger than the first omitted term.

Holds when: $x$ is near the expansion point $a$, and $f$ is smooth there. Breaks when: $x$ lies outside the radius, or the bound's $M$ is taken too small (it must bound the derivative over the whole interval).

## Vector calculus

### Operators in Cartesian coordinates

- $\nabla f = \left(\dfrac{\partial f}{\partial x}, \dfrac{\partial f}{\partial y}, \dfrac{\partial f}{\partial z}\right)$ (gradient, vector)
- $\nabla\cdot\mathbf{F} = \dfrac{\partial F_x}{\partial x} + \dfrac{\partial F_y}{\partial y} + \dfrac{\partial F_z}{\partial z}$ (divergence, scalar)
- $\nabla\times\mathbf{F} = \left(\dfrac{\partial F_z}{\partial y} - \dfrac{\partial F_y}{\partial z},\ \dfrac{\partial F_x}{\partial z} - \dfrac{\partial F_z}{\partial x},\ \dfrac{\partial F_y}{\partial x} - \dfrac{\partial F_x}{\partial y}\right)$ (curl, vector)
- $\nabla^2 f = \nabla\cdot\nabla f = \dfrac{\partial^2 f}{\partial x^2} + \dfrac{\partial^2 f}{\partial y^2} + \dfrac{\partial^2 f}{\partial z^2}$ (Laplacian)
- $\nabla^2\mathbf{F} = \nabla(\nabla\cdot\mathbf{F}) - \nabla\times(\nabla\times\mathbf{F})$ (vector Laplacian)

### Identities (for functions with continuous second derivatives)

- $\nabla\times(\nabla f) = \mathbf{0}$ (a gradient field is curl-free)
- $\nabla\cdot(\nabla\times\mathbf{F}) = 0$ (a curl field is divergence-free)
- $\nabla\cdot(f\mathbf{F}) = f\,\nabla\cdot\mathbf{F} + \mathbf{F}\cdot\nabla f$
- $\nabla\times(f\mathbf{F}) = f\,\nabla\times\mathbf{F} + \nabla f \times \mathbf{F}$
- $\nabla\cdot(\mathbf{F}\times\mathbf{G}) = \mathbf{G}\cdot(\nabla\times\mathbf{F}) - \mathbf{F}\cdot(\nabla\times\mathbf{G})$
- $\nabla\times(\nabla\times\mathbf{F}) = \nabla(\nabla\cdot\mathbf{F}) - \nabla^2\mathbf{F}$

### Integral theorems

- Green (plane, counterclockwise boundary $C$): $\oint_C (P\,dx + Q\,dy) = \iint_R \left(\dfrac{\partial Q}{\partial x} - \dfrac{\partial P}{\partial y}\right) dA$
- Gradient theorem: $\int_C \nabla f\cdot d\mathbf{r} = f(\text{end}) - f(\text{start})$. Path independent.
- Divergence theorem (closed surface $\partial V$, outward normal $\hat{\mathbf{n}}$): $\iiint_V \nabla\cdot\mathbf{F}\,dV = \oiint_{\partial V}\mathbf{F}\cdot\hat{\mathbf{n}}\,dS$
- Stokes (surface $S$ with boundary $\partial S$, right-hand orientation): $\iint_S (\nabla\times\mathbf{F})\cdot\hat{\mathbf{n}}\,dS = \oint_{\partial S}\mathbf{F}\cdot d\mathbf{r}$
- Conservative fields: in a simply connected domain, $\nabla\times\mathbf{F} = \mathbf{0}$ if and only if $\mathbf{F} = \nabla f$ for some $f$.

Holds when: $\mathbf{F}$ is continuously differentiable on the region, the boundary is closed and piecewise smooth (for the divergence theorem) or the surface is orientable with a piecewise smooth boundary (for Stokes). Breaks when: there is a point source or singularity inside the region. Example: $\mathbf{F} = \mathbf{r}/r^3$ has $\nabla\cdot\mathbf{F} = 0$ everywhere except the origin, where the flux through any enclosing sphere is $4\pi$ (a Dirac delta in the divergence). Applying the theorem naively gives zero and is wrong.

### Curvilinear forms

Cylindrical $(r, \theta, z)$:

- $\nabla\cdot\mathbf{F} = \dfrac{1}{r}\dfrac{\partial (rF_r)}{\partial r} + \dfrac{1}{r}\dfrac{\partial F_\theta}{\partial\theta} + \dfrac{\partial F_z}{\partial z}$
- $\nabla f = \dfrac{\partial f}{\partial r}\hat{\mathbf{r}} + \dfrac{1}{r}\dfrac{\partial f}{\partial\theta}\hat{\boldsymbol\theta} + \dfrac{\partial f}{\partial z}\hat{\mathbf{z}}$

Spherical $(r, \theta, \phi)$, with $\theta$ the polar angle measured from $+z$:

- $\nabla\cdot\mathbf{F} = \dfrac{1}{r^2}\dfrac{\partial (r^2 F_r)}{\partial r} + \dfrac{1}{r\sin\theta}\dfrac{\partial (\sin\theta\,F_\theta)}{\partial\theta} + \dfrac{1}{r\sin\theta}\dfrac{\partial F_\phi}{\partial\phi}$
- $\nabla f = \dfrac{\partial f}{\partial r}\hat{\mathbf{r}} + \dfrac{1}{r}\dfrac{\partial f}{\partial\theta}\hat{\boldsymbol\theta} + \dfrac{1}{r\sin\theta}\dfrac{\partial f}{\partial\phi}\hat{\boldsymbol\phi}$
- $\nabla^2 f = \dfrac{1}{r^2}\dfrac{\partial}{\partial r}\!\left(r^2\dfrac{\partial f}{\partial r}\right) + \dfrac{1}{r^2\sin\theta}\dfrac{\partial}{\partial\theta}\!\left(\sin\theta\dfrac{\partial f}{\partial\theta}\right) + \dfrac{1}{r^2\sin^2\theta}\dfrac{\partial^2 f}{\partial\phi^2}$

Holds when: the unit vectors are used in the order $(\hat{\mathbf{r}}, \hat{\boldsymbol\theta}, \hat{\boldsymbol\phi})$ or $(\hat{\mathbf{r}}, \hat{\boldsymbol\theta}, \hat{\mathbf{z}})$ as defined. Breaks when: a different angle convention is used (many texts put $\theta$ as the azimuth). Confirm the convention before substituting.

## Linear algebra

### Determinant and inverse

- $2\times 2$: $\det\begin{pmatrix} a & b\\ c & d\end{pmatrix} = ad - bc$
- $3\times 3$: $a(ei - fh) - b(di - fg) + c(dh - eg)$ for rows $(a,b,c)$, $(d,e,f)$, $(g,h,i)$
- Properties: $\det(\mathbf{A}\mathbf{B}) = \det\mathbf{A}\,\det\mathbf{B}$; $\det\mathbf{A}^{\mathsf T} = \det\mathbf{A}$; $\det(c\mathbf{A}) = c^n\det\mathbf{A}$ for $n\times n$; swapping two rows flips the sign; a triangular matrix has determinant equal to the product of its diagonal.
- Inverse, $2\times 2$: $\mathbf{A}^{-1} = \dfrac{1}{ad-bc}\begin{pmatrix} d & -b\\ -c & a\end{pmatrix}$. For larger matrices, do not form $\mathbf{A}^{-1}$ to solve a system. Solve $\mathbf{A}\mathbf{x} = \mathbf{b}$ directly.
- Cramer's rule $x_i = \det\mathbf{A}_i/\det\mathbf{A}$ is fine for $n \le 3$ by hand and poor beyond that.

Holds when: square matrix, exact arithmetic. Breaks when: $\det\mathbf{A}$ is near zero in floating point. A tiny determinant does not mean a singular matrix, because it depends on scale. Use the condition number (below) instead.

### Eigenvalues and eigenvectors

- $\mathbf{A}\mathbf{v} = \lambda\mathbf{v}$, $\mathbf{v}\ne\mathbf{0}$. Characteristic equation: $\det(\mathbf{A} - \lambda\mathbf{I}) = 0$.
- Trace and determinant: $\sum_i \lambda_i = \operatorname{tr}\mathbf{A}$, $\prod_i\lambda_i = \det\mathbf{A}$.
- $2\times 2$ symmetric $\begin{pmatrix} a & b\\ b & c\end{pmatrix}$: $\lambda = \dfrac{a+c}{2} \pm\sqrt{\left(\dfrac{a-c}{2}\right)^2 + b^2}$. Check: $\begin{pmatrix}2&1\\1&2\end{pmatrix}$ gives $1$ and $3$.
- Spectral theorem: a real symmetric matrix has real eigenvalues and orthogonal eigenvectors.
- Positive definite: all $\lambda > 0$, equivalently $\mathbf{x}^{\mathsf T}\mathbf{A}\mathbf{x} > 0$ for all $\mathbf{x}\ne\mathbf{0}$. Such a matrix has a Cholesky factorization. Stiffness and mass matrices of stable structures are positive definite once rigid-body modes and supports are handled.
- Rayleigh quotient, symmetric $\mathbf{A}$: $\lambda_{\min} \le \dfrac{\mathbf{x}^{\mathsf T}\mathbf{A}\mathbf{x}}{\mathbf{x}^{\mathsf T}\mathbf{x}} \le \lambda_{\max}$.

Vibration: for $\mathbf{K}\mathbf{u} = \mathbf{F}$ with mass $\mathbf{M}$, undamped natural frequencies $\omega$ solve $\det(\mathbf{K} - \omega^2\mathbf{M}) = 0$, that is, $\omega^2$ are eigenvalues of $\mathbf{M}^{-1}\mathbf{K}$.

Holds when: the matrix is symmetric for real eigenvalues and orthogonal eigenvectors. Breaks when: the matrix is nonsymmetric (eigenvalues may be complex and eigenvectors not orthogonal), or defective (not enough independent eigenvectors).

### Conditioning and solving

- Condition number: $\kappa(\mathbf{A}) = \lVert\mathbf{A}\rVert\,\lVert\mathbf{A}^{-1}\rVert$. In the 2-norm, $\kappa = \sigma_{\max}/\sigma_{\min}$ (singular values). For symmetric positive definite $\mathbf{A}$, $\kappa = \lambda_{\max}/\lambda_{\min}$.
- Relative error bound, first order: $\dfrac{\lVert\delta\mathbf{x}\rVert}{\lVert\mathbf{x}\rVert} \lesssim \kappa(\mathbf{A})\,\dfrac{\lVert\delta\mathbf{b}\rVert}{\lVert\mathbf{b}\rVert}$.
- Rule of thumb: you lose about $\log_{10}\kappa$ significant digits. In double precision (about 16 digits), $\kappa = 10^{12}$ leaves about 4 digits.
- Hilbert matrices $H_{ij} = 1/(i+j-1)$ (computed in 2-norm): $\kappa \approx 19$ at $n=2$, $5.2\times10^2$ at $n=3$, $1.6\times10^4$ at $n=4$, $1.5\times10^{10}$ at $n=8$. Use them as a stress test.
- Matrix norms: 1-norm $=$ max column sum of absolute values; $\infty$-norm $=$ max row sum; 2-norm $=$ largest singular value.
- Work: LU with partial pivoting about $\tfrac{2}{3}n^3$ flops; Cholesky about $\tfrac{1}{3}n^3$ flops for symmetric positive definite.

Holds when: the rule of thumb is for first-order perturbation. Breaks when: the problem is nonlinear, or the solver is iterative (its convergence depends on the spectrum, not just $\kappa$). A large $\kappa$ can come from bad scaling of units (mixing mm and m), so nondimensionalize first.

## Ordinary differential equations

Classification: order (highest derivative), linear or nonlinear, homogeneous or forced, constant or variable coefficients.

### First-order linear

$$y' + p(t)\,y = q(t)$$

- Integrating factor $\mu(t) = \exp\!\left(\int p\,dt\right)$. Solution: $y = \dfrac{1}{\mu}\left[\int \mu\,q\,dt + C\right]$.
- Constant $p \ne 0$ and constant $q$: $y = \dfrac{q}{p} + C e^{-pt}$. Time constant $\tau = 1/p$.
- Separable $y' = g(t)h(y)$: $\int \dfrac{dy}{h(y)} = \int g(t)\,dt$.

Newton's law of cooling (lumped capacity), $T_a$ ambient, $k$ in 1/s:

$$T(t) = T_a + (T_0 - T_a)\,e^{-kt}, \qquad k = \frac{h_c A}{\rho V c_p}$$

- Here $h_c$ is the convective coefficient (W/(m$^2$ K)), $A$ area (m$^2$), $\rho$ density (kg/m$^3$), $V$ volume (m$^3$), $c_p$ specific heat (J/(kg K)).
- Holds when: the Biot number $\mathrm{Bi} = h_c L_c/k_{\mathrm{th}} \ll 0.1$, with $L_c = V/A$ and $k_{\mathrm{th}}$ the solid's thermal conductivity. Then the body is nearly uniform in temperature.
- Breaks when: $\mathrm{Bi}$ is not small (temperature gradients inside the body matter), when $h_c$ or $T_a$ varies, or when radiation is significant at high temperature (the law is then not linear in $T$).

Half-life of exponential decay: $t_{1/2} = \ln 2/k = 0.693/k$.

### Second-order linear, constant coefficients

Mass-spring-damper, $m$ (kg), $c$ (N s/m), $k$ (N/m):

$$m x'' + c x' + k x = F(t)$$

- Undamped natural frequency: $\omega_n = \sqrt{k/m}$ (rad/s); $f_n = \omega_n/(2\pi)$ (Hz).
- Damping ratio: $\zeta = \dfrac{c}{2\sqrt{km}} = \dfrac{c}{2m\omega_n}$.
- Characteristic equation: $r^2 + 2\zeta\omega_n r + \omega_n^2 = 0$, roots $r = -\zeta\omega_n \pm \omega_n\sqrt{\zeta^2 - 1}$.

Free response, all three damping cases plus undamped:

| Case | Condition | General solution | Notes |
|---|---|---|---|
| Undamped | $\zeta = 0$ | $x = A\cos\omega_n t + B\sin\omega_n t$ | Period $2\pi/\omega_n$ |
| Underdamped | $0 < \zeta < 1$ | $x = e^{-\zeta\omega_n t}(A\cos\omega_d t + B\sin\omega_d t)$ | $\omega_d = \omega_n\sqrt{1 - \zeta^2}$; oscillates with decaying envelope |
| Critically damped | $\zeta = 1$ | $x = (A + Bt)\,e^{-\omega_n t}$ | Fastest return with no overshoot |
| Overdamped | $\zeta > 1$ | $x = A e^{r_1 t} + B e^{r_2 t}$, $r_{1,2} = -\omega_n\left(\zeta \mp \sqrt{\zeta^2-1}\right)$ | Both roots real and negative; slow creep |

- Underdamped constants from $x(0) = x_0$, $\dot x(0) = v_0$: $A = x_0$, $B = (v_0 + \zeta\omega_n x_0)/\omega_d$.
- Logarithmic decrement between successive peaks: $\delta = \dfrac{2\pi\zeta}{\sqrt{1-\zeta^2}}$, approximately $2\pi\zeta$ for small $\zeta$. Use it to estimate $\zeta$ from a measured decay.
- Worked check: $m = 2$ kg, $c = 4$ N s/m, $k = 50$ N/m give $\zeta = 0.2$, $\omega_n = 5$ rad/s, $\omega_d = 4.899$ rad/s.

Steady forced response, $F = F_0\cos\omega t$, $r = \omega/\omega_n$:

$$X = \frac{F_0/k}{\sqrt{(1 - r^2)^2 + (2\zeta r)^2}}, \qquad \phi = \operatorname{atan2}\!\left(2\zeta r,\ 1 - r^2\right)$$

- Dynamic amplification $X/(F_0/k)$ peaks at $r = \sqrt{1 - 2\zeta^2}$ (for $\zeta < 1/\sqrt{2}$) with peak value $\dfrac{1}{2\zeta\sqrt{1-\zeta^2}}$. At $\zeta = 0.05$ the peak is about 10.

Damping ratios must come from measurement or from the governing standard for the structure type. Do not assume a value; the example above uses $\zeta = 0.2$ only as an illustration.

Holds when: linear stiffness, linear viscous damping, a lumped mass, and small motion. Breaks when: Coulomb (dry) friction (decay becomes linear in time, not exponential), nonlinear springs (large amplitude shifts $\omega_n$, as in Duffing behavior), or time-varying parameters (for example, a rotating unbalance mass that changes the effective stiffness).

### Systems of ODEs

- $\mathbf{M}\ddot{\mathbf{x}} + \mathbf{C}\dot{\mathbf{x}} + \mathbf{K}\mathbf{x} = \mathbf{f}(t)$. For proportional damping, modes decouple. Otherwise solve as a first-order system $\dot{\mathbf{z}} = \mathbf{A}\mathbf{z} + \mathbf{b}(t)$ with $\mathbf{z} = (\mathbf{x}, \dot{\mathbf{x}})$, $\mathbf{A} = \begin{pmatrix} \mathbf{0} & \mathbf{I} \\ -\mathbf{M}^{-1}\mathbf{K} & -\mathbf{M}^{-1}\mathbf{C} \end{pmatrix}$, and $\mathbf{b} = (\mathbf{0}, \mathbf{M}^{-1}\mathbf{f}(t))$.
- Stability of $\dot{\mathbf{z}} = \mathbf{A}\mathbf{z}$: stable (decaying) if every eigenvalue of $\mathbf{A}$ has negative real part.

## Laplace transform

Definition: $F(s) = \displaystyle\int_0^\infty e^{-st} f(t)\,dt$ (for $f$ piecewise continuous and of exponential order).

Properties:

- Linearity: $\mathcal{L}\{af + bg\} = aF + bG$
- Derivatives: $\mathcal{L}\{f'\} = sF - f(0)$; $\mathcal{L}\{f''\} = s^2F - s f(0) - f'(0)$
- First shift: $\mathcal{L}\{e^{at}f(t)\} = F(s - a)$
- Time shift: $\mathcal{L}\{f(t-a)u(t-a)\} = e^{-as}F(s)$
- Convolution: $\mathcal{L}\{(f\ast g)(t)\} = F(s)G(s)$, with $(f\ast g)(t) = \int_0^t f(\tau)g(t-\tau)\,d\tau$
- Initial value: $f(0^+) = \lim_{s\to\infty} sF(s)$. Final value: $\lim_{t\to\infty} f(t) = \lim_{s\to 0} sF(s)$, only if that limit exists (all poles in the left half-plane, except a simple pole at 0).

Table (typical; $u(t)$ unit step, $\delta$ Dirac delta):

| $f(t)$ | $F(s)$ |
|---|---|
| $u(t)$ | $1/s$ |
| $t^n$ ($n$ a nonnegative integer) | $n!/s^{n+1}$ |
| $e^{at}$ | $1/(s-a)$ |
| $t\,e^{at}$ | $1/(s-a)^2$ |
| $t^n e^{at}$ | $n!/(s-a)^{n+1}$ |
| $\sin\omega t$ | $\omega/(s^2+\omega^2)$ |
| $\cos\omega t$ | $s/(s^2+\omega^2)$ |
| $e^{at}\sin\omega t$ | $\omega/((s-a)^2+\omega^2)$ |
| $e^{at}\cos\omega t$ | $(s-a)/((s-a)^2+\omega^2)$ |
| $\sinh at$ | $a/(s^2-a^2)$ |
| $\cosh at$ | $s/(s^2-a^2)$ |
| $u(t-a)$ | $e^{-as}/s$ |
| $\delta(t-a)$ | $e^{-as}$ |

Inversion: use partial fractions (cover-up rule for simple poles, then match the table). Holds when: the ODE is linear with constant coefficients, and the transform is taken with the initial conditions included as above. Breaks when: coefficients vary with $t$ or the equation is nonlinear.

## Fourier series

Period $T$, fundamental $\omega_0 = 2\pi/T$ (rad/s), piecewise smooth and periodic:

$$f(t) = \frac{a_0}{2} + \sum_{n=1}^{\infty}\left[a_n\cos n\omega_0 t + b_n\sin n\omega_0 t\right]$$

$$a_n = \frac{2}{T}\int_{T} f(t)\cos n\omega_0 t\,dt, \qquad b_n = \frac{2}{T}\int_{T} f(t)\sin n\omega_0 t\,dt$$

- Over $(-\pi, \pi)$ with period $2\pi$: $a_n = \dfrac{1}{\pi}\int_{-\pi}^{\pi} f\cos nt\,dt$, $b_n = \dfrac{1}{\pi}\int_{-\pi}^{\pi} f\sin nt\,dt$.
- Complex form: $f = \sum_n c_n e^{in\omega_0 t}$, $c_n = \dfrac{1}{T}\int_T f\,e^{-in\omega_0 t}\,dt$.
- Parseval (mean square): $\dfrac{1}{T}\int_T f^2\,dt = \dfrac{a_0^2}{4} + \tfrac{1}{2}\sum_{n\ge1}(a_n^2 + b_n^2)$.

Standard results (period $2\pi$):

- Square wave, $f = +1$ on $(0,\pi)$, $-1$ on $(-\pi,0)$: $b_n = \dfrac{4}{n\pi}$ for odd $n$, all other coefficients zero. So $f = \dfrac{4}{\pi}\sum_{n\ \text{odd}}\dfrac{\sin nt}{n}$.
- Ramp, $f = t$ on $(-\pi,\pi)$: $b_n = \dfrac{2(-1)^{n+1}}{n}$, all $a_n = 0$.
- Gibbs phenomenon: at a jump, partial sums overshoot by about 8.95% of the jump height. For the $\pm 1$ square wave the peak tends to about $1.179$, not $1$.

Convergence and coefficient decay:

- Piecewise smooth, periodic, with jumps: series converges to the midpoint of a jump; coefficients decay like $1/n$.
- Continuous with a kink (continuous $f$, discontinuous $f'$): coefficients decay like $1/n^2$.
- Holds when: $f$ is periodic (or extended periodically) and piecewise smooth. Breaks when: the signal is not periodic over the window (use the Fourier transform, or window the data and accept leakage), or the data are sampled. Sampling at rate $f_s$ aliases any content above the Nyquist frequency $f_s/2$.

## Probability and statistics

### Distributions

- Mean and variance, discrete: $\mu = \sum x\,p(x)$, $\sigma^2 = \sum (x-\mu)^2 p(x)$.
- Binomial: $P(X = k) = \binom{n}{k}p^k(1-p)^{n-k}$; mean $np$, variance $np(1-p)$. Check: $n=10$, $p=0.1$, $P(X=2) = 0.1937$.
- Poisson (rare events, rate $\lambda$ per interval): $P(X = k) = \dfrac{\lambda^k e^{-\lambda}}{k!}$; mean and variance both $\lambda$.
- Normal: $f(x) = \dfrac{1}{\sigma\sqrt{2\pi}}\exp\!\left[-\dfrac{(x-\mu)^2}{2\sigma^2}\right]$. Standard score $z = (x-\mu)/\sigma$.
- Normal coverage (typical; two-sided):

| Interval | Probability inside | Probability outside |
|---|---|---|
| $\pm 1\sigma$ | 68.27% | 31.73% |
| $\pm 2\sigma$ | 95.45% | 4.55% |
| $\pm 3\sigma$ | 99.73% | 0.27% |
| $\pm 4\sigma$ | 99.9937% | $6.3\times10^{-5}$ |
| $\pm 5\sigma$ | 99.99994% | $5.7\times10^{-7}$ |
| $\pm 6\sigma$ | 99.9999998% | $2.0\times10^{-9}$ |

- One-sided tail beyond $z$: $1 - \Phi(z)$. Beyond $3\sigma$ it is $1.35\times10^{-3}$; beyond $4\sigma$ it is $3.2\times10^{-5}$.

Holds when: the process is stable and the variable is close to symmetric and light-tailed. Breaks when: the tail is heavy (fatigue life, wind gusts, failure of rare events), where $z$-based tails underestimate risk by orders of magnitude. A $6\sigma$ normal tail is a model prediction, not a measured frequency.

### $Z$ and $t$ critical values (typical)

Two-sided, normal ($z$):

| Confidence | 80% | 90% | 95% | 99% | 99.73% |
|---|---|---|---|---|---|
| $z$ | 1.2816 | 1.6449 | 1.9600 | 2.5758 | 3.0000 |

One-sided, normal ($z$):

| Confidence | 90% | 95% | 97.5% | 99% | 99.9% |
|---|---|---|---|---|---|
| $z$ | 1.2816 | 1.6449 | 1.9600 | 2.3263 | 3.0902 |

Two-sided, Student $t$ at 95% and 99% ($\mathrm{df}$ $=$ degrees of freedom $n-1$):

| df | 1 | 2 | 4 | 9 | 29 | $\infty$ |
|---|---|---|---|---|---|---|
| $t_{0.95}$ | 12.706 | 4.303 | 2.776 | 2.262 | 2.045 | 1.960 |
| $t_{0.99}$ | 63.657 | 9.925 | 4.604 | 3.250 | 2.756 | 2.576 |

### Estimation and intervals

- Sample mean $\bar{x} = \tfrac{1}{n}\sum x_i$; sample standard deviation $s = \sqrt{\tfrac{1}{n-1}\sum(x_i - \bar{x})^2}$ (divide by $n-1$).
- Standard error of the mean: $\sigma/\sqrt{n}$ (known $\sigma$) or $s/\sqrt{n}$ (estimated).
- Confidence interval for the mean, $\sigma$ known: $\bar{x} \pm z\,\sigma/\sqrt{n}$.
- Confidence interval for the mean, $\sigma$ estimated: $\bar{x} \pm t^*\,s/\sqrt{n}$, with $t^*$ at $n-1$ df.
- Prediction interval for one new observation: $\bar{x} \pm t^*\,s\sqrt{1 + 1/n}$. Wider than the mean interval, and the one to use for "where will the next part land".
- Sample size for half-width $E$ (known $\sigma$): $n \ge (z\sigma/E)^2$, rounded up.
- Proportion, Wald interval: $\hat p \pm z\sqrt{\hat p(1-\hat p)/n}$. Use only when $n\hat p$ and $n(1-\hat p)$ are both at least about 10. For small $n$ or extreme $\hat p$, use the Wilson interval.
- Confidence interval meaning: a 95% procedure captures the true value in 95% of repeated experiments. It does not say the true value has a 95% chance of being in this interval.

Hypothesis testing and effect size:

- Type I error $\alpha$ (false alarm rate), type II error $\beta$, power $1-\beta$.
- Statistical significance measures whether an effect is distinguishable from noise. It does not measure whether the effect is large. Compare the effect size with the tolerance or design margin.

Holds when: samples are independent, drawn from one process, and the distribution is near normal for $t$-based intervals (or $n$ is large enough for the central limit theorem). Breaks when: data are autocorrelated (time series, batches), heavy-tailed, or a process drifts during the test. Rule of thumb: for many distributions, the sample mean is close to normal once $n \gtrsim 30$; for skewed or heavy-tailed data, use more or switch to a nonparametric method.

Uncertainty propagation (combining measurement errors through a formula) is covered in [measurement](../measurement/README.md). Do not reuse the normal-coverage table for combined errors without checking that the inputs are normal and independent.

## Numerical methods

### Root finding

| Method | Order | Needs | Notes |
|---|---|---|---|
| Bisection | linear: error halves each step | sign change on $[a,b]$ | Always converges. Error $\le (b-a)/2^n$ after $n$ steps |
| Secant | about 1.618 | two starting points | No derivative needed |
| Newton | 2 (quadratic) at a simple root | $f'(x)$ | Fails near $f' = 0$ or with a poor start. $e_{n+1}\approx \dfrac{f''}{2f'}e_n^2$ |
| Newton for root of multiplicity $m$ | linear (order 1) as written | $f'$ | Use $x_{n+1} = x_n - m\,f/f'$ to restore order 2 |

- Bisection steps for tolerance $\varepsilon$: $n \ge \log_2\!\left((b-a)/\varepsilon\right)$. For $[2,3]$ to $10^{-6}$, $n \ge 20$.
- Newton check from the worked lesson example: $f = x^3 - 2x - 5$ from $x_0 = 2$ reaches $2.0945515$ in about three steps.

### Numerical integration

| Rule | Global error order | Error $=$ exact minus approximation (composite, step $h$) |
|---|---|---|
| Midpoint | 2 | $\dfrac{(b-a)h^2}{24}f''(\xi)$ |
| Trapezoid | 2 | $-\dfrac{(b-a)h^2}{12}f''(\xi)$ |
| Simpson | 4 | $-\dfrac{(b-a)h^4}{180}f^{(4)}(\xi)$ |
| Gauss-Legendre, $n$ points | $2n$ (exact for polynomials of degree $\le 2n-1$) | Nodes are not equally spaced |

- Check: $\int_0^1 e^{-x^2}\,dx = 0.7468241$. Trapezoid errors are $+3.84\times10^{-3}$ at $n=4$ and $+9.59\times10^{-4}$ at $n=8$ (ratio 4, order 2). Simpson errors are $-3.1\times10^{-5}$ at $n=4$ and $-2.0\times10^{-6}$ at $n=8$ (ratio about 16, order 4).
- Trapezoid overestimates when $f'' > 0$ (convex) and underestimates when $f'' < 0$.

Holds when: $f$ is smooth enough for the error term's derivative to exist and be bounded. Breaks when: $f$ has a kink or singularity inside the interval (refine locally or use a method for singular integrands).

### ODE solvers

| Method | Global order | Stability (test $y' = \lambda y$, $z = h\lambda$) |
|---|---|---|
| Forward Euler | 1 | Stable for $\lvert 1 + z\rvert \le 1$: $-2 \le z \le 0$ for real $\lambda$. Unstable for every $h$ if $\lambda$ is imaginary |
| Midpoint (RK2) and Heun | 2 | Real-axis limit $-2 \le z \le 0$ (conditionally stable) |
| Backward Euler | 1 | A-stable: stable for all $\operatorname{Re} z \le 0$ |
| Trapezoidal (Crank-Nicolson) | 2 | A-stable. Can ring on stiff problems with large steps |
| RK4 | 4 (local error $O(h^5)$) | Real-axis limit $-2.785 \le z \le 0$. Imaginary-axis limit $\lvert\omega h\rvert \le 2\sqrt{2} \approx 2.83$ |

- Explicit stiffness limit: for an explicit method, $h \le z_{\max}/\lvert\lambda_{\max}\rvert$, where $z_{\max}$ is the stability limit above (2 for Euler, 2.785 for RK4). The fastest mode sets the step, not the slowest.
- Order check: halving $h$ reduces the global error by about $2^p$. Observed order $p = \log_2\!\left(E(h)/E(h/2)\right)$.

Holds when: the solution is smooth on the step scale and the step is small compared with the fastest timescale. Breaks when: the problem is stiff (use an implicit or stiff solver), forcing is discontinuous (use event detection), or the system is chaotic (error grows exponentially regardless of method).

### Error sources and round-off

- Truncation error: from the method (replacing a curve with a line or polynomial).
- Round-off error: from finite precision. Machine epsilon: double precision $2.22\times10^{-16}$; single precision (binary32) $1.19\times10^{-7}$.
- Forward-difference derivative: total error is about $\sqrt{\varepsilon} \approx 1.5\times10^{-8}$ at the best step $h \approx \sqrt{\varepsilon}$ in double precision.
- Central-difference derivative: total error is about $\varepsilon^{2/3} \approx 4\times10^{-11}$ at $h \approx \varepsilon^{1/3} \approx 6\times10^{-6}$ in double precision.
- Smaller $h$ reduces truncation error but eventually increases round-off. Find the minimum by refinement, not by pushing $h$ to zero.

Stopping criteria: stop when the change in $x$ is below a tolerance and the residual $\lvert f(x)\rvert$ is also small. Check both; a small step with a large residual means you are stuck.

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
