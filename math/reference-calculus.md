# Calculus reference

**Type:** reference
**Verify:** strict

Lookup sheet for limits, derivatives, integrals, series, multivariable calculus, vector calculus, and optimization, for an engineer who needs a rule, a table entry, or a check in the middle of a job.

In the variables tables, a symbol for a generic function or coordinate is listed as dimensionless. The equation is dimensionally homogeneous, so any unit the application gives $f$ or $x$ carries through, and the meaning column says where a result gains a unit.

## Principles

- A derivative is a local linear model. A function near a point behaves like its tangent line, and every derivative rule is a rule for combining linear models.
- An integral is a limit of sums. Anything that can be cut into small pieces whose sizes add (area, mass, work, charge) is an integral.
- Differentiation and integration undo each other (the fundamental theorem), but differentiation is mechanical and integration is not. A derivative of an elementary function is always elementary; many integrals are not.
- Units carry through. A derivative divides the units of $f$ by the units of $x$; an integral multiplies them. A result with the wrong unit is wrong before any arithmetic is checked.
- Every limit, series, and integral theorem has conditions: continuity, convergence, smoothness, a closed boundary. Check the condition before using the result.
- Series approximate only near the expansion point. The remainder bound says how near.
- Coordinates are a choice. Choose the system that makes the boundary a constant coordinate, and include the Jacobian factor.
- A sign or factor error shows up in a limiting case. Test with a shape whose answer is known (a square, a circle, a constant function).
- Angles are in radians inside every derivative, integral, and series on this sheet.

Related sheets: ordinary differential equations, Laplace, and Fourier methods are in [Linear algebra and differential equations reference](reference-linear-algebra-differential-equations.md); numerical integration and differentiation are in [Probability and numerical methods reference](reference-probability-numerical-methods.md); area, centroid, and second moments of standard sections are in [Section properties](../physics/reference-mechanics.md#section-properties).

## Limits and continuity

### Standard limits

A limit gives the value a function approaches as its input approaches a point, without requiring the function to be defined there.

$$\lim_{x\to 0}\frac{\sin x}{x}=1 \qquad \lim_{x\to 0}\frac{1-\cos x}{x^{2}}=\frac12 \qquad \lim_{x\to 0}\frac{e^{x}-1}{x}=1 \qquad \lim_{n\to\infty}\left(1+\frac{x}{n}\right)^{n}=e^{x}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $x$ | argument, in radians where a trigonometric function appears | dimensionless |
| $n$ | positive integer that grows without bound | dimensionless |

Holds when: $x$ is in radians and the limit is taken as stated (a two-sided limit at $0$).
Breaks when: $x$ is in degrees (the first limit becomes $\pi/180$), or the limit is one-sided and the function differs on the two sides.
Source and basis: derived from the squeeze theorem on $\sin x < x < \tan x$; taught in [Single-variable calculus](03-single-variable-calculus.md).

- Also useful: $\lim_{x\to 0^{+}} x\ln x = 0$; $\lim_{x\to\infty} x^{k}e^{-x}=0$ for any $k$; a polynomial of degree $m$ over one of degree $n$ tends to the ratio of leading coefficients when $m=n$, to $0$ when $m<n$.
- Example: the second quotient at $x=0.1$ is $0.4996$. At $x=0.01$ the first quotient is $\sin(0.01)/0.01 = 0.99998$, and the fourth with $x=1$, $n=1000$ gives $2.7169$ against $e = 2.7183$.

```verify
x = q(0.01, "")
expect(sin(x) / x, "0.99998")
n = q(1000, "")
expect((1 + 1 / n) ** n, "2.7169")
expect(exp(1), "2.7183")
y = q(0.1, "")
expect((1 - cos(y)) / y**2, "0.4996")
```

### Continuity and the intermediate value theorem

A function is **continuous** at a point when its limit there equals its value. A function continuous on a closed interval takes every value between its end values.

$$\lim_{x\to a} f(x)=f(a)$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $f$ | function | dimensionless |
| $a$ | point of the domain | dimensionless |
| $x$ | argument | dimensionless |

Holds when: $f(a)$ is defined, the limit exists, and the two are equal. On a closed interval $[a,b]$ the function then attains a maximum and a minimum (extreme value theorem) and, if $f(a)$ and $f(b)$ differ in sign, has a root between (intermediate value theorem).
Breaks when: the function has a jump, a pole, or an oscillation without limit inside the interval; the root guarantee then fails.
Source and basis: derived from the definition of the limit; taught in [Single-variable calculus](03-single-variable-calculus.md).

- Example: $f(x)=x^{3}-x-1$ has $f(1)=-1$ and $f(2)=5$, so a root lies in $[1,2]$. At $x=1.3247$ the value is $f=-0.00008$, so the root is near that point.

```verify
x = q(1.3247, "")
expect(x**3 - x - 1, "-0.00008")
check(1 - 1 - 1 < 0, "f(1) is negative")
check(2**3 - 2 - 1 > 0, "f(2) is positive")
```

### L'Hopital's rule

When a quotient of limits has the form $0/0$ or $\infty/\infty$, the limit of the quotient equals the limit of the quotient of derivatives.

$$\lim_{x\to a}\frac{f(x)}{g(x)}=\lim_{x\to a}\frac{f'(x)}{g'(x)}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $f$, $g$ | differentiable functions with $f,g\to 0$ or both $\to\infty$ | dimensionless |
| $f'$, $g'$ | their derivatives | dimensionless |
| $a$ | the point (or $\pm\infty$) | dimensionless |

Holds when: the original form is $0/0$ or $\infty/\infty$, $g'\neq 0$ near $a$, and the limit on the right exists.
Breaks when: the form is not indeterminate (the rule gives a wrong number), or the derivative quotient oscillates. Forms $0\cdot\infty$, $\infty-\infty$, $1^{\infty}$, $0^{0}$ must be rewritten as a quotient or through $\ln$ first.
Source and basis: derived from the Cauchy mean value theorem; taught in [Single-variable calculus](03-single-variable-calculus.md).

- Example: $\lim_{x\to 0}(e^{x}-1-x)/x^{2}$ is $0/0$; two applications give $\lim e^{x}/2=\tfrac12$. Numerically at $x=0.01$ the quotient is $0.5017$.

```verify
x = q(0.01, "")
expect((exp(x) - 1 - x) / x**2, "0.5017")
```

## Derivatives

### Definition and rules

The **derivative** is the instantaneous rate of change of a function, the limit of the slope of secant lines.

$$f'(x)=\lim_{h\to 0}\frac{f(x+h)-f(x)}{h} \qquad (fg)'=f'g+fg' \qquad \left(\frac{f}{g}\right)'=\frac{f'g-fg'}{g^{2}} \qquad \frac{d}{dx}f(g(x))=f'(g(x))\,g'(x)$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $f$, $g$ | differentiable functions; $f'$ carries the unit of $f$ per unit of $x$ | dimensionless |
| $x$ | independent variable | dimensionless |
| $h$ | step toward zero | dimensionless |

Holds when: the functions are differentiable at $x$ (and $g\neq 0$ in the quotient rule).
Breaks when: there is a corner, cusp, vertical tangent, or discontinuity at $x$; a function can be continuous and still have no derivative there.
Source and basis: derived from the limit definition; taught in [Single-variable calculus](03-single-variable-calculus.md) and OpenStax [Calculus Volume 1](https://openstax.org/books/calculus-volume-1/pages/1-introduction).

- Linearity: $(af+bg)'=af'+bg'$. Power of a function: $(f^{n})'=nf^{n-1}f'$. Higher derivatives: $f''=(f')'$, written $f^{(n)}$.
- Mean value theorem: if $f$ is continuous on $[a,b]$ and differentiable inside, some point has $f'(c)=\dfrac{f(b)-f(a)}{b-a}$.
- Example: $f=x^{2}\sin x$ gives $f'=2x\sin x+x^{2}\cos x$, which is $2.2232$ at $x=1$. A central difference with a very small step gives the same digits.

```verify
x = q(1, "")
fp = 2 * x * sin(x) + x**2 * cos(x)
expect(fp, "2.2232")
h = q(0.00001, "")
d = ((x + h) ** 2 * sin(x + h) - (x - h) ** 2 * sin(x - h)) / (2 * h)
expect(d, "2.2232")
```

### Table of standard derivatives

Valid on the domain where each function is defined; $a$ and $b$ are constants and $u$ is a function of $x$ (apply the chain rule by multiplying by $u'$).

| $f(x)$ | $f'(x)$ | Condition |
|---|---|---|
| $x^{n}$ | $n x^{n-1}$ | $n$ real, $x>0$ if $n$ is not an integer |
| $e^{ax}$ | $a e^{ax}$ | |
| $b^{x}$ | $b^{x}\ln b$ | $b>0$ |
| $\ln \lvert x\rvert$ | $1/x$ | $x\neq 0$ |
| $\log_{b} x$ | $1/(x\ln b)$ | $x>0$, $b>0$, $b\neq 1$ |
| $\sin x$, $\cos x$ | $\cos x$, $-\sin x$ | |
| $\tan x$, $\cot x$ | $\sec^{2}x$, $-\csc^{2}x$ | |
| $\sec x$, $\csc x$ | $\sec x\tan x$, $-\csc x\cot x$ | |
| $\arcsin x$, $\arccos x$ | $1/\sqrt{1-x^{2}}$, $-1/\sqrt{1-x^{2}}$ | $\lvert x\rvert<1$ |
| $\arctan x$ | $1/(1+x^{2})$ | |
| $\sinh x$, $\cosh x$ | $\cosh x$, $\sinh x$ | |
| $\tanh x$ | $1-\tanh^{2}x=\mathrm{sech}^{2}x$ | |
| $\operatorname{arsinh} x$ | $1/\sqrt{x^{2}+1}$ | |
| $\operatorname{arcosh} x$ | $1/\sqrt{x^{2}-1}$ | $x>1$ |
| $\operatorname{artanh} x$ | $1/(1-x^{2})$ | $\lvert x\rvert<1$ |

### Implicit and logarithmic differentiation

When $y$ is defined by $F(x,y)=0$, differentiate both sides and solve for $y'$; when a function is a product or power of many factors, differentiate its logarithm.

$$\frac{dy}{dx}=-\frac{F_{x}}{F_{y}} \qquad \frac{d}{dx}\ln f=\frac{f'}{f}\ \Rightarrow\ f'=f\,\frac{d}{dx}\ln f$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $F$ | function whose zero set defines the curve | dimensionless |
| $F_{x}$, $F_{y}$ | partial derivatives of $F$ | dimensionless |
| $y$ | dependent variable | dimensionless |
| $f$ | positive function being differentiated | dimensionless |

Holds when: $F_{y}\neq 0$ at the point (implicit form); $f>0$ (logarithmic form; use $\lvert f\rvert$ otherwise).
Breaks when: $F_{y}=0$, where the tangent is vertical and $y$ is not a function of $x$ locally.
Source and basis: derived from the chain rule applied to $F(x,y(x))=0$; taught in [Single-variable calculus](03-single-variable-calculus.md).

- Example: the circle $x^{2}+y^{2}=25$ at $(3,4)$ has $dy/dx=-3/4=-0.75$. For $y=x^{x}$, $y'=x^{x}(\ln x+1)$, which is $6.7726$ at $x=2$. The circle check is $x^{2}+y^{2}=25$ with $x=3$ and $y=4$.

```verify
x = q(3, "")
y = q(4, "")
expect(x**2 + y**2, "25")
expect(-(2 * x) / (2 * y), "-0.75")
t = q(2, "")
expect(t**t * (log(t) + 1), "6.7726")
```

### Linear approximation and differentials

Near a point $a$, a function is approximated by its tangent line, and a small change in $x$ produces a change in $f$ of about $f'\,dx$.

$$f(x)\approx f(a)+f'(a)(x-a) \qquad \Delta f\approx f'(a)\,\Delta x$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $f$ | function | dimensionless |
| $a$ | expansion point | dimensionless |
| $x$ | evaluation point near $a$ | dimensionless |
| $\Delta x$ | small change in $x$ | dimensionless |

Holds when: $\lvert x-a\rvert$ is small and $f''$ is not large; the error is about $\tfrac12 f''(a)(x-a)^{2}$.
Breaks when: the curvature is large or $x$ is far from $a$; the Taylor remainder below bounds the error.
Source and basis: derived from the definition of the derivative; the error term is the second Taylor term (see Taylor remainder below).

- Example: $\sqrt{a+\Delta x}$ with $a=4$ and $\Delta x=0.1$ (so the argument is $4.1$) gives $2+\Delta x/4=2.025$ against the true $2.0248$, an error of $0.00015$.

```verify
a = q(4, "")
dx = q(0.1, "")
approx = sqrt(a) + dx / (2 * sqrt(a))
expect(a + dx, "4.1")
expect(approx, "2.025")
expect(sqrt(a + dx), "2.0248")
expect(approx - sqrt(a + dx), "0.00015", rel=0.1)
```

## Integrals

### Table of standard integrals

Add a constant $C$ to every indefinite integral. $a\neq 0$ unless stated, and each result is valid on intervals where the integrand is defined.

| $\int f\,dx$ for $f=$ | Result |
|---|---|
| $x^{n}$, $n\neq -1$ | $\dfrac{x^{n+1}}{n+1}$ |
| $1/x$ | $\ln\lvert x\rvert$ |
| $e^{ax}$ | $e^{ax}/a$ |
| $b^{x}$, $b>0$, $b\neq 1$ | $b^{x}/\ln b$ |
| $\sin ax$, $\cos ax$ | $-\dfrac{\cos ax}{a}$, $\dfrac{\sin ax}{a}$ |
| $\tan x$, $\cot x$ | $-\ln\lvert\cos x\rvert$, $\ln\lvert\sin x\rvert$ |
| $\sec x$, $\csc x$ | $\ln\lvert\sec x+\tan x\rvert$, $-\ln\lvert\csc x+\cot x\rvert$ |
| $\sec^{2}x$, $\csc^{2}x$ | $\tan x$, $-\cot x$ |
| $\sin^{2}ax$, $\cos^{2}ax$ | $\dfrac{x}{2}\mp\dfrac{\sin 2ax}{4a}$ (upper sign for $\sin^{2}$) |
| $\ln x$ | $x\ln x-x$ |
| $xe^{ax}$ | $e^{ax}\left(\dfrac{x}{a}-\dfrac{1}{a^{2}}\right)$ |
| $x\sin ax$, $x\cos ax$ | $\dfrac{\sin ax}{a^{2}}-\dfrac{x\cos ax}{a}$, $\dfrac{\cos ax}{a^{2}}+\dfrac{x\sin ax}{a}$ |
| $e^{ax}\sin bx$ | $\dfrac{e^{ax}(a\sin bx-b\cos bx)}{a^{2}+b^{2}}$ |
| $e^{ax}\cos bx$ | $\dfrac{e^{ax}(a\cos bx+b\sin bx)}{a^{2}+b^{2}}$ |
| $\dfrac{1}{x^{2}+a^{2}}$ | $\dfrac{1}{a}\arctan\dfrac{x}{a}$ |
| $\dfrac{1}{x^{2}-a^{2}}$ | $\dfrac{1}{2a}\ln\left\lvert\dfrac{x-a}{x+a}\right\rvert$ |
| $\dfrac{1}{\sqrt{a^{2}-x^{2}}}$ | $\arcsin\dfrac{x}{a}$ for $\lvert x\rvert<a$, $a>0$ |
| $\dfrac{1}{\sqrt{x^{2}+a^{2}}}$ | $\ln\left(x+\sqrt{x^{2}+a^{2}}\right)$ |
| $\dfrac{1}{\sqrt{x^{2}-a^{2}}}$ | $\ln\left\lvert x+\sqrt{x^{2}-a^{2}}\right\rvert$ |
| $\sqrt{a^{2}-x^{2}}$ | $\dfrac{x}{2}\sqrt{a^{2}-x^{2}}+\dfrac{a^{2}}{2}\arcsin\dfrac{x}{a}$, $a>0$ |
| $\arctan x$ | $x\arctan x-\tfrac12\ln(1+x^{2})$ |
| $\sinh x$, $\cosh x$ | $\cosh x$, $\sinh x$ |

- Check any entry by differentiating the result. Example: $\int_{0}^{1}\sqrt{1-x^{2}}\,dx$ uses the $\sqrt{a^{2}-x^{2}}$ row with $a=1$ and equals $\pi/4=0.7854$ (a quarter of the unit disk).

```verify
a = q(1, "")
F1 = (1 / 2) * sqrt(a**2 - 1) + (a**2 / 2) * asin(1 / a)
expect(F1, "0.7854")
expect(pi / 4, "0.7854")
```

### Substitution

Substitution replaces an inner function by a new variable so that the integrand becomes a table form. For a definite integral, change the limits with the variable.

$$\int_{a}^{b} f(g(x))\,g'(x)\,dx=\int_{g(a)}^{g(b)} f(u)\,du \qquad u=g(x)$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $f$ | outer function | dimensionless |
| $g$ | inner differentiable function | dimensionless |
| $u$ | new variable | dimensionless |
| $a$, $b$ | original limits | dimensionless |

Holds when: $g'$ is continuous on $[a,b]$ and $f$ is continuous on the range of $g$.
Breaks when: $g$ is not one-to-one and the integral is treated as indefinite without returning to $x$; or the substitution crosses a point where $f(g(x))$ is singular.
Source and basis: derived from the chain rule read backward; taught in [Single-variable calculus](03-single-variable-calculus.md).

- Trigonometric substitutions: $\sqrt{a^{2}-x^{2}}$ with $x=a\sin\theta$; $\sqrt{a^{2}+x^{2}}$ with $x=a\tan\theta$; $\sqrt{x^{2}-a^{2}}$ with $x=a\sec\theta$.
- Example: $\int_{0}^{1}2x\,e^{x^{2}}\,dx$ with $u=x^{2}$ becomes $\int_{0}^{1}e^{u}\,du=e-1=1.7183$.

```verify
expect(exp(1) - 1, "1.7183")
```

### Integration by parts

Integration by parts trades an integral of a product for another integral that is simpler, from the product rule.

$$\int u\,dv=uv-\int v\,du \qquad \int_{a}^{b} u\,v'\,dx=\Big[uv\Big]_{a}^{b}-\int_{a}^{b} u'v\,dx$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $u$ | factor chosen to simplify when differentiated | dimensionless |
| $v$ | antiderivative of the remaining factor | dimensionless |
| $a$, $b$ | limits | dimensionless |

Holds when: $u$ and $v$ are continuously differentiable on the interval.
Breaks when: the new integral is harder than the old one (swap the choice of $u$), or boundary terms are dropped from a definite integral.
Source and basis: derived from the product rule; taught in [Single-variable calculus](03-single-variable-calculus.md) and OpenStax [Calculus Volume 2](https://openstax.org/books/calculus-volume-2/pages/1-introduction).

- Choose $u$ in the order logarithm, inverse trigonometric, algebraic, trigonometric, exponential. Repeated parts (a polynomial times $e^{x}$) can be done in a table. A cycle (for example $e^{x}\sin x$) returns the original integral; solve for it.
- Example: $\int_{0}^{\pi}x\sin x\,dx=\big[-x\cos x\big]_{0}^{\pi}+\int_{0}^{\pi}\cos x\,dx=\pi=3.1416$. And $\int_{0}^{1}xe^{x}\,dx=1$.

```verify
expect(-pi * cos(pi) + sin(pi), "3.1416")
expect(exp(1) - (exp(1) - 1), "1")
```

### Partial fractions

A proper rational function is split into terms that each integrate by the table, using one term per factor of the denominator.

$$\frac{P(x)}{Q(x)}=\sum\frac{A_{k}}{(x-r)^{k}}+\sum\frac{B_{k}x+C_{k}}{(x^{2}+px+q)^{k}}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $P$, $Q$ | polynomials with the degree of $P$ below that of $Q$ | dimensionless |
| $r$ | real root of $Q$ | dimensionless |
| $p$, $q$ | coefficients of an irreducible quadratic factor | dimensionless |
| $A_{k}$, $B_{k}$, $C_{k}$ | constants found by matching coefficients or cover-up | dimensionless |

Holds when: the degree of $P$ is less than that of $Q$ (otherwise divide first) and $Q$ is factored over the reals.
Breaks when: the factorization of $Q$ is wrong, or a repeated factor is given only one term (it needs a term for each power up to its multiplicity).
Source and basis: derived from the algebra of rational functions.

- Cover-up rule for a simple root $r$: $A=\dfrac{P(r)}{Q'(r)}$.
- Example: $\dfrac{1}{(x-1)(x+2)}=\dfrac13\left(\dfrac{1}{x-1}-\dfrac{1}{x+2}\right)$, so $\int_{2}^{3}=\tfrac13\ln\tfrac85=0.1567$. At $x=2.5$ the integrand is $0.1481$.

```verify
x = q(2.5, "")
expect(1 / ((x - 1) * (x + 2)), "0.1481")
expect((1 / 3) * (1 / (x - 1) - 1 / (x + 2)), "0.1481")
expect((1 / 3) * log(8 / 5), "0.1567")
```

### Improper integrals

An **improper integral** has an infinite limit or an integrand that is unbounded at an endpoint. It is defined as a limit of proper integrals.

$$\int_{1}^{\infty}x^{-p}\,dx=\frac{1}{p-1}\ (p>1) \qquad \int_{0}^{1}x^{-p}\,dx=\frac{1}{1-p}\ (p<1) \qquad \int_{0}^{\infty}t^{n}e^{-t}\,dt=n!$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $p$ | exponent | dimensionless |
| $n$ | non-negative integer | dimensionless |
| $t$ | integration variable | dimensionless |

Holds when: $p$ is on the stated side of $1$ (the first integral diverges for $p\le 1$, the second for $p\ge 1$).
Breaks when: a singularity sits inside the interval (split there and test each piece), or the integral is evaluated by the antiderivative across the singularity.
Source and basis: derived from the limit definition of the integral; the factorial integral follows from repeated integration by parts; see OpenStax [Calculus Volume 2](https://openstax.org/books/calculus-volume-2/pages/1-introduction).

- Comparison: if $0\le f\le g$ and $\int g$ converges, so does $\int f$; if $\int f$ diverges, so does $\int g$.
- Example: $\int_{1}^{\infty}x^{-2}dx=1$; $\int_{0}^{1}x^{-1/2}dx=2$; $\int_{-\infty}^{\infty}e^{-x^{2}}dx=\sqrt{\pi}=1.7725$; $4!=24$.

```verify
p = q(2, "")
expect(1 / (p - 1), "1")
p2 = q(0.5, "")
expect(1 / (1 - p2), "2")
expect(sqrt(pi), "1.7725")
expect(4 * 3 * 2 * 1, "24")
```

## Applications of integrals

### Area between curves

$$A=\int_{a}^{b}\big[f_{\text{top}}(x)-f_{\text{bottom}}(x)\big]\,dx$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $A$ | enclosed area | $\text{m}^2$ |
| $f_{\text{top}}$, $f_{\text{bottom}}$ | upper and lower boundary curves | m |
| $x$ | coordinate | m |
| $a$, $b$ | limits where the curves meet | m |

Holds when: $f_{\text{top}}\ge f_{\text{bottom}}$ on $[a,b]$; split the interval where the curves cross.
Breaks when: the curves cross inside the interval (the integral then gives a signed area, not the enclosed area).
Source and basis: derived from the definition of the integral as a sum of thin strips; see OpenStax [Calculus Volume 2](https://openstax.org/books/calculus-volume-2/pages/1-introduction).

- Example: between $y=x$ and $y=x^{2}/L$ on $0\le x\le L$ with $L=1\ \text{m}$ the area is $L^{2}/2-L^{2}/3=0.1667\ \text{m}^2$.

```verify
L = q(1, "m")
expect(L**2 / 2 - L**2 / 3, "0.1667 m^2")
```

### Volume of revolution

$$V=\pi\int_{a}^{b}\big[R(x)^{2}-r(x)^{2}\big]\,dx \qquad V=2\pi\int_{a}^{b}\rho\,h(\rho)\,d\rho$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $V$ | volume | $\text{m}^3$ |
| $R$, $r$ | outer and inner radius of the washer | m |
| $\rho$ | distance of the strip from the axis (shells) | m |
| $h$ | height of the shell | m |
| $a$, $b$ | limits along the axis (washers) or the radius (shells) | m |

Holds when: the region does not cross the axis of revolution; disks and washers slice perpendicular to the axis, shells parallel to it.
Breaks when: the region straddles the axis (the two halves overlap), or the radius is measured from the wrong axis.
Source and basis: derived from summing cross-sectional areas $\pi R^{2}$ or cylindrical shell areas; see OpenStax [Calculus Volume 2](https://openstax.org/books/calculus-volume-2/pages/1-introduction).

- Example: a cone from $y=(R/H)x$ rotated about the $x$-axis with $R=0.3\ \text{m}$ and $H=0.9\ \text{m}$ has $V=\pi R^{2}H/3=0.0848\ \text{m}^3$.

```verify
R = q(0.3, "m")
H = q(0.9, "m")
expect(pi * (R / H) ** 2 * H**3 / 3, "0.0848 m^3")
expect(pi * R**2 * H / 3, "0.0848 m^3")
```

### Arc length and surface of revolution

$$s=\int_{a}^{b}\sqrt{1+\big(f'(x)\big)^{2}}\,dx \qquad S=2\pi\int_{a}^{b}f(x)\sqrt{1+\big(f'(x)\big)^{2}}\,dx$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $s$ | arc length | m |
| $S$ | lateral surface area of revolution about the $x$-axis | $\text{m}^2$ |
| $f$ | curve height, non-negative for $S$ | m |
| $f'$ | slope of the curve | dimensionless |
| $a$, $b$ | limits | m |

Holds when: $f'$ is continuous on $[a,b]$ and $f\ge 0$ for the surface formula.
Breaks when: the curve has a vertical tangent (use a parametric form $s=\int\sqrt{x'^{2}+y'^{2}}\,dt$).
Source and basis: derived from the Pythagorean length of a small segment; see OpenStax [Calculus Volume 2](https://openstax.org/books/calculus-volume-2/pages/1-introduction).

- Example: $y=\tfrac23x^{3/2}/\sqrt{L}$ with $L=1\ \text{m}$ has $y'=\sqrt{x/L}$, so over $0\le x\le 3\ \text{m}$ the length is $\tfrac{2L}{3}(4^{3/2}-1)=4.6667\ \text{m}$. The cone $y=x$ on $0\le x\le 1\ \text{m}$ has $S=\pi\sqrt{2}=4.4429\ \text{m}^2$.

```verify
L = q(1, "m")
x = q(3, "m")
expect((2 * L / 3) * ((1 + x / L) ** 1.5 - 1), "4.6667 m")
expect(pi * sqrt(2) * q(1, "m^2"), "4.4429 m^2")
```

### Average value and root-mean-square value

$$\bar f=\frac{1}{b-a}\int_{a}^{b}f(x)\,dx \qquad f_{\text{rms}}=\sqrt{\frac{1}{b-a}\int_{a}^{b}f(x)^{2}\,dx}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\bar f$ | average value of $f$ | dimensionless |
| $f_{\text{rms}}$ | root-mean-square value | dimensionless |
| $f$ | integrable function (the result has the unit of $f$) | dimensionless |
| $a$, $b$ | ends of the averaging interval | dimensionless |

Holds when: $f$ is integrable on $[a,b]$; the rms value of a periodic signal uses a whole number of periods.
Breaks when: the averaging window is not a whole number of periods for a periodic signal (the value then depends on the phase).
Source and basis: derived from the definition of the mean of a continuous quantity; see OpenStax [Calculus Volume 2](https://openstax.org/books/calculus-volume-2/pages/1-introduction).

- Example: $\sin x$ averages $2/\pi=0.6366$ over a half period and has $f_{\text{rms}}=1/\sqrt{2}=0.7071$ over a full period.

```verify
expect((1 / pi) * (cos(0) - cos(pi)), "0.6366")
expect(sqrt((1 / (2 * pi)) * pi), "0.7071")
```

### Centroid of a plane region

$$\bar x=\frac{\int_{a}^{b}x\,f(x)\,dx}{\int_{a}^{b}f(x)\,dx} \qquad \bar y=\frac{\tfrac12\int_{a}^{b}f(x)^{2}\,dx}{\int_{a}^{b}f(x)\,dx}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\bar x$, $\bar y$ | centroid coordinates | m |
| $f$ | height of the region above the $x$-axis | m |
| $x$ | coordinate along the axis | m |
| $a$, $b$ | limits | m |

Holds when: the region lies between the $x$-axis and $f\ge 0$, with uniform density.
Breaks when: the region lies on both sides of the axis (split it), or the density varies (weight each term by density).
Source and basis: derived from the first moment of area divided by the area; see [Section properties](../physics/reference-mechanics.md#section-properties) for standard shapes.

- Example: under $y=x^{2}/L$ on $0\le x\le L$ with $L=1\ \text{m}$, $\bar x=0.75L=0.75\ \text{m}$ and $\bar y=0.3L=0.3\ \text{m}$. A semicircle of radius $R=0.5\ \text{m}$ has $\bar y=4R/(3\pi)=0.2122\ \text{m}$.

```verify
L = q(1, "m")
A = L**2 / 3
expect((L**3 / 4) / A, "0.75 m")
expect((0.5 * L**3 / 5) / A, "0.3 m")
R = q(0.5, "m")
expect(4 * R / (3 * pi), "0.2122 m")
```

### Work

$$W=\int_{x_{1}}^{x_{2}}F(x)\,dx \qquad W_{\text{spring}}=\tfrac12k_s\big(x_{2}^{2}-x_{1}^{2}\big) \qquad W_{\text{lift}}=\rho g\int_{0}^{H}A(y)\,(y_{\text{out}}-y)\,dy$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $W$ | work done by the applied force on the object | J |
| $F$ | force along the path | N |
| $x_{1}$, $x_{2}$ | initial and final positions (spring: stretch from rest length) | m |
| $k_s$ | spring stiffness | N/m |
| $\rho$ | density of the lifted fluid | $\text{kg/m}^3$ |
| $g$ | local gravitational acceleration | $\text{m/s}^2$ |
| $A$ | horizontal cross-section area at height $y$ | $\text{m}^2$ |
| $y$, $y_{\text{out}}$ | height of a slice and of the outlet | m |
| $H$ | depth of the fluid | m |

Holds when: the force is along the displacement and depends only on position; for lifting, the fluid rises vertically and is incompressible. For a spring, positive work means work done on the spring by the applied force $F=k_sx$.
Breaks when: the force has a component across the path (use the line integral), or the force depends on velocity or history.
Source and basis: the definite integral sums force times displacement along a path; the physics of work and energy is covered in [Mechanics reference, Work and energy](../physics/reference-mechanics.md#work-and-energy).

- Example of a definite integral: stretching a spring with $k_s=200\ \text{N/m}$ from $0.1\ \text{m}$ to $0.3\ \text{m}$ requires $W=\int_{x_1}^{x_2}k_sx\,dx=8\ \text{J}$ of work done on the spring by the applied force. A full cylindrical tank of radius $1\ \text{m}$ and height $2\ \text{m}$ pumped to its top rim needs $\rho g\pi r^{2}H^{2}/2$; with $\rho=1000\ \text{kg/m}^3$ and standard Earth gravity $g$ this is $61.6\ \text{kJ}$.

```verify
ks = q(200, "N/m")
expect(0.5 * ks * (q(0.3, "m") ** 2 - q(0.1, "m") ** 2), "8 J")
rho = q(1000, "kg/m^3", of="water.density.nominal")
g = q(9.80665, "m/s^2", of="g_standard")
r = q(1, "m")
H2 = q(2, "m")
expect(rho * g * pi * r**2 * H2**2 / 2, "61.6 kJ")
```

## Sequences and series

### Geometric and p-series

$$\sum_{n=0}^{\infty}r^{n}=\frac{1}{1-r}\ (\lvert r\rvert<1) \qquad \sum_{n=0}^{N}r^{n}=\frac{1-r^{N+1}}{1-r} \qquad \sum_{n=1}^{\infty}\frac{1}{n^{p}}\ \text{converges iff}\ p>1$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $r$ | common ratio | dimensionless |
| $n$ | term index | dimensionless |
| $N$ | last index of a partial sum | dimensionless |
| $p$ | exponent of the p-series | dimensionless |

Holds when: $\lvert r\rvert<1$ for the infinite geometric sum (the finite sum holds for any $r\neq 1$).
Breaks when: $\lvert r\rvert\ge 1$ (the infinite sum diverges); the harmonic series ($p=1$) diverges though its terms tend to zero.
Source and basis: derived from subtracting $r$ times the sum from the sum; the p-series test follows from the integral test; see OpenStax [Calculus Volume 2](https://openstax.org/books/calculus-volume-2/pages/1-introduction).

- Integral-test tail bound: $\sum_{n>N}n^{-2}<1/N$. For $N=100$ the tail is below $0.0100$.
- Example: $r=\tfrac12$ gives a sum of $2$, and ten terms give $1.99805$. And $\sum n^{-2}=\pi^{2}/6=1.6449$.

```verify
r = q(0.5, "")
expect(1 / (1 - r), "2")
expect((1 - r**10) / (1 - r), "1.99805")
expect(pi**2 / 6, "1.6449")
N = q(100, "")
expect(1 / N, "0.0100")
```

### Convergence tests

| Test | Statement | Use when |
|---|---|---|
| Divergence (n-th term) | If $a_{n}\not\to 0$, $\sum a_{n}$ diverges | First check; never proves convergence |
| Comparison | $0\le a_{n}\le b_{n}$: $\sum b_{n}$ converges implies $\sum a_{n}$ converges | Terms resemble a known series |
| Limit comparison | $a_{n}/b_{n}\to c$ with $0<c<\infty$: both converge or both diverge | Same growth as a known series |
| Integral | $a_{n}=f(n)$ with $f$ positive, decreasing: sum and $\int^{\infty}f$ share convergence | $f$ is easy to integrate |
| Ratio | See the ratio test entry | Factorials, powers |
| Root | $\lim\lvert a_{n}\rvert^{1/n}<1$ converges, $>1$ diverges | $n$-th powers |
| Alternating | See the entry below | Signs alternate |
| Absolute | $\sum\lvert a_{n}\rvert$ converges implies $\sum a_{n}$ converges | Mixed signs |

A series that converges but not absolutely is **conditionally convergent**; its terms can be reordered to change the sum, so never reorder it.

### Ratio test and radius of convergence

$$L=\lim_{n\to\infty}\left\lvert\frac{a_{n+1}}{a_{n}}\right\rvert \qquad \sum c_{n}(x-a)^{n}:\ \ R=\frac{1}{\lim\lvert c_{n+1}/c_{n}\rvert}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $a_{n}$ | $n$-th term of the series | dimensionless |
| $L$ | limiting ratio | dimensionless |
| $c_{n}$ | coefficient of a power series | dimensionless |
| $x$ | variable of the power series | dimensionless |
| $a$ | center of the power series | dimensionless |
| $R$ | radius of convergence | dimensionless |

Holds when: the limit exists (or is infinite). The series converges absolutely for $L<1$ and diverges for $L>1$; a power series converges for $\lvert x-a\rvert<R$ and diverges for $\lvert x-a\rvert>R$.
Breaks when: $L=1$ (the test is silent; use another test), and at the endpoints $\lvert x-a\rvert=R$, which must be tested one by one.
Source and basis: derived from comparison with a geometric series; see OpenStax [Calculus Volume 2](https://openstax.org/books/calculus-volume-2/pages/1-introduction).

- Example: for $a_{n}=n/2^{n}$ the ratio is $(n+1)/(2n)$, which is $0.5005$ at $n=1000$, so $L=\tfrac12$ and the series converges. For $e^{x}$, $c_{n}=1/n!$, the ratio $1/(n+1)\to 0$ gives $R=\infty$.

```verify
n = q(1000, "")
expect((n + 1) / (2 * n), "0.5005")
```

### Alternating series test and error bound

$$S=\sum_{n=1}^{\infty}(-1)^{n+1}a_{n},\qquad \lvert S-S_{N}\rvert\le a_{N+1}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $a_{n}$ | positive terms | dimensionless |
| $S$ | sum of the series | dimensionless |
| $S_{N}$ | partial sum of the first $N$ terms | dimensionless |
| $N$ | number of terms kept | dimensionless |

Holds when: $a_{n}$ decreases monotonically to $0$; then the series converges and the error is no larger than the first omitted term, with the same sign as it.
Breaks when: the terms do not decrease monotonically, or do not tend to zero.
Source and basis: derived from bracketing the sum between consecutive partial sums; see OpenStax [Calculus Volume 2](https://openstax.org/books/calculus-volume-2/pages/1-introduction).

- Example: $\sum(-1)^{n+1}/n=\ln 2=0.6931$. With $N=5$, $S_{5}=0.7833$ and the bound is $1/6=0.1667$; the true error is $0.0902$.

```verify
S5 = 1 - 1 / 2 + 1 / 3 - 1 / 4 + 1 / 5
expect(S5, "0.7833")
expect(1 / 6, "0.1667")
expect(S5 - log(2), "0.0902")
expect(log(2), "0.6931")
```

### Finite sums

$$\sum_{n=1}^{N}n=\frac{N(N+1)}{2} \qquad \sum_{n=1}^{N}n^{2}=\frac{N(N+1)(2N+1)}{6} \qquad \sum_{n=1}^{N}n^{3}=\left[\frac{N(N+1)}{2}\right]^{2}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $n$ | summation index | dimensionless |
| $N$ | number of terms | dimensionless |

Holds when: $N$ is a non-negative integer.
Breaks when: the summation starts at an index other than $1$ (subtract the missing terms).
Source and basis: derived from mathematical induction.

- Example with $N=100$: $5050$, $338350$, $25502500$.

```verify
N = q(100, "")
expect(N * (N + 1) / 2, "5050")
expect(N * (N + 1) * (2 * N + 1) / 6, "338350")
expect((N * (N + 1) / 2) ** 2, "25502500")
```

### Taylor and Maclaurin series

A **Taylor series** writes a smooth function as a power series in $x-a$; with $a=0$ it is a **Maclaurin series**.

$$f(x)=\sum_{n=0}^{\infty}\frac{f^{(n)}(a)}{n!}(x-a)^{n}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $f^{(n)}$ | $n$-th derivative of $f$ | dimensionless |
| $a$ | expansion point | dimensionless |
| $x$ | evaluation point, in radians for trigonometric functions | dimensionless |
| $n$ | term index | dimensionless |

Holds when: $f$ has derivatives of all orders at $a$ and $\lvert x-a\rvert$ is inside the radius of convergence, and the remainder tends to zero.
Breaks when: $x$ is outside the radius; or $f$ is smooth but not analytic (for example $e^{-1/x^{2}}$ at $0$, whose series is zero).
Source and basis: derived from repeated integration by parts of the fundamental theorem; taught in [Single-variable calculus](03-single-variable-calculus.md).

| Function | Series (about $0$) | Converges for |
|---|---|---|
| $e^{x}$ | $\sum x^{n}/n!$ | all $x$ |
| $\sin x$ | $\sum(-1)^{n}x^{2n+1}/(2n+1)!$ | all $x$ |
| $\cos x$ | $\sum(-1)^{n}x^{2n}/(2n)!$ | all $x$ |
| $\sinh x$, $\cosh x$ | $\sum x^{2n+1}/(2n+1)!$, $\sum x^{2n}/(2n)!$ | all $x$ |
| $\ln(1+x)$ | $\sum_{n\ge1}(-1)^{n+1}x^{n}/n$ | $-1<x\le 1$ |
| $1/(1-x)$ | $\sum x^{n}$ | $\lvert x\rvert<1$ |
| $\arctan x$ | $\sum(-1)^{n}x^{2n+1}/(2n+1)$ | $\lvert x\rvert\le 1$ |
| $\tan x$ | $x+x^{3}/3+2x^{5}/15+\cdots$ | $\lvert x\rvert<\pi/2$ |
| $\arcsin x$ | $x+x^{3}/6+3x^{5}/40+\cdots$ | $\lvert x\rvert\le 1$ |
| $(1+x)^{p}$ | $\sum\binom{p}{n}x^{n}$, with $\binom{p}{n}=\dfrac{p(p-1)\cdots(p-n+1)}{n!}$ | $\lvert x\rvert<1$ |

- Small-argument forms: $\sin x\approx x$, $\cos x\approx 1-x^{2}/2$, $\sqrt{1+x}\approx 1+x/2$, $1/(1+x)\approx 1-x$, $\ln(1+x)\approx x$.
- Example: $\cos 0.2$ through the $x^{4}$ term is $0.98007$, and $\sqrt{1.1}$ through the $x^{2}$ term is $1.04875$ against the true $1.04881$.

```verify
x = q(0.2, "")
expect(1 - x**2 / 2 + x**4 / 24, "0.98007")
y = q(0.1, "")
expect(1 + y, "1.1")
expect(1 + y / 2 - y**2 / 8, "1.04875")
expect(sqrt(1 + y), "1.04881")
```

### Taylor remainder

$$\lvert R_{n}(x)\rvert\le\frac{M\,\lvert x-a\rvert^{n+1}}{(n+1)!},\qquad M\ge\max\big\lvert f^{(n+1)}\big\rvert\ \text{between}\ a\ \text{and}\ x$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $R_{n}$ | error after the degree $n$ term | dimensionless |
| $M$ | bound on the $(n+1)$-th derivative over the interval | dimensionless |
| $x$, $a$ | evaluation and expansion points | dimensionless |
| $n$ | degree of the polynomial kept | dimensionless |

Holds when: $f^{(n+1)}$ exists on the interval between $a$ and $x$ and $M$ bounds it over the whole interval.
Breaks when: $M$ is taken at one point instead of the maximum over the interval, or $x$ is outside the radius of convergence.
Source and basis: derived from the Lagrange form of the remainder (the mean value theorem applied $n+1$ times); see OpenStax [Calculus Volume 2](https://openstax.org/books/calculus-volume-2/pages/1-introduction).

- Example: $\sin 0.5\approx 0.5-0.5^{3}/6=0.47917$. The bound with $n=3$ and $M=1$ is $0.0026$; the actual error is $0.00026$.

```verify
x = q(0.5, "")
approx = x - x**3 / 6
expect(approx, "0.47917")
expect(x**4 / 24, "0.0026")
expect(sin(x) - approx, "0.00026")
```

## Multivariable derivatives

### Partial derivatives and the gradient

A **partial derivative** differentiates with respect to one variable while the others are held fixed. The **gradient** collects them into a vector that points in the direction of steepest increase.

$$\frac{\partial f}{\partial x}=\lim_{h\to 0}\frac{f(x+h,y)-f(x,y)}{h} \qquad \nabla f=\left(\frac{\partial f}{\partial x},\frac{\partial f}{\partial y},\frac{\partial f}{\partial z}\right)$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $f$ | scalar function of position | dimensionless |
| $x$, $y$, $z$ | Cartesian coordinates | m |
| $\nabla f$ | gradient (carries the unit of $f$ per metre) | 1/m |
| $h$ | step toward zero | m |

Holds when: $f$ has continuous second partials (then $f_{xy}=f_{yx}$, Clairaut's theorem) and the gradient points to steepest ascent, perpendicular to level curves.
Breaks when: partials exist but are discontinuous, so the function need not be differentiable (it may lack a tangent plane).
Source and basis: derived from the single-variable derivative applied one coordinate at a time; taught in [Multivariable calculus](04-multivariable-calculus.md) and OpenStax [Calculus Volume 3](https://openstax.org/books/calculus-volume-3/pages/1-introduction).

- Example: $f=x^{2}y+z$ has $\nabla f=(2xy,\,x^{2},\,1)$, which is $(4,1,1)$ at $(1,2,3)$.

```verify
x = q(1, "")
y = q(2, "")
expect(2 * x * y, "4")
expect(x**2, "1")
```

### Tangent plane and total differential

$$z=f(a,b)+f_{x}(a,b)(x-a)+f_{y}(a,b)(y-b) \qquad df=f_{x}\,dx+f_{y}\,dy$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $f_{x}$, $f_{y}$ | partial derivatives at $(a,b)$ | dimensionless |
| $a$, $b$ | point of tangency | dimensionless |
| $dx$, $dy$ | small changes in the inputs | dimensionless |
| $df$ | resulting first-order change in $f$ | dimensionless |

Holds when: $f$ is differentiable at $(a,b)$ and the changes are small.
Breaks when: the surface is strongly curved over the step (the neglected terms are second order).
Source and basis: derived from the linear approximation of a function of two variables; see OpenStax [Calculus Volume 3](https://openstax.org/books/calculus-volume-3/pages/1-introduction).

- Example: $f=x^{2}y$ at $(1,2)$ with $dx=0.1$, $dy=-0.05$ gives $df=4(0.1)+1(-0.05)=0.35$; the exact change is $0.3595$.

```verify
dx = q(0.1, "")
dy = q(-0.05, "")
expect(4 * dx + 1 * dy, "0.35")
expect((1 + dx) ** 2 * (2 + dy) - 2, "0.3595")
```

### Directional derivative

$$D_{\hat{\mathbf{u}}}f=\nabla f\cdot\hat{\mathbf{u}} \qquad \max_{\hat{\mathbf{u}}}D_{\hat{\mathbf{u}}}f=\lvert\nabla f\rvert$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $D_{\hat{\mathbf{u}}}f$ | rate of change of $f$ per metre along $\hat{\mathbf{u}}$ | 1/m |
| $\nabla f$ | gradient | 1/m |
| $\hat{\mathbf{u}}$ | unit vector giving the direction | dimensionless |

Holds when: $f$ is differentiable and $\hat{\mathbf{u}}$ has length $1$ (normalize first).
Breaks when: the direction vector is not normalized, which scales the answer by its length.
Source and basis: derived from the chain rule along a straight line; see OpenStax [Calculus Volume 3](https://openstax.org/books/calculus-volume-3/pages/1-introduction).

- Example: $f=x^{2}y$ at $(1,2)$ with $\nabla f=(4,1)$ along $(3,4)/5$ gives $3.2$; the steepest rate is $\sqrt{17}=4.1231$, where $17=4^{2}+1^{2}$.

```verify
expect(4 * 3 / 5 + 1 * 4 / 5, "3.2")
expect(4**2 + 1**2, "17")
expect(sqrt(4**2 + 1**2), "4.1231")
```

### Multivariable chain rule

$$\frac{dz}{dt}=\frac{\partial f}{\partial x}\frac{dx}{dt}+\frac{\partial f}{\partial y}\frac{dy}{dt} \qquad \mathbf{J}_{f\circ g}=\mathbf{J}_{f}\,\mathbf{J}_{g}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $z$ | $f(x(t),y(t))$ | dimensionless |
| $t$ | parameter (time) | s |
| $\mathbf{J}_{f}$, $\mathbf{J}_{g}$ | Jacobian matrices of the outer and inner maps | dimensionless |

Holds when: $f$ is differentiable and $x(t)$, $y(t)$ are differentiable.
Breaks when: any link of the chain is not differentiable at the point.
Source and basis: derived from the linear approximation of $f$ composed with the linear approximation of the path; see OpenStax [Calculus Volume 3](https://openstax.org/books/calculus-volume-3/pages/1-introduction).

- Example: $z=x^{2}y$ with $x=t^{2}$, $y=t^{3}$ is $t^{7}$. At $t=2$: $x=4$, $y=8$ and $2xy\cdot 2t+x^{2}\cdot 3t^{2}=448=7\cdot 2^{6}$.

```verify
t = q(2, "")
x = t**2
y = t**3
expect(2 * x * y * 2 * t + x**2 * 3 * t**2, "448")
expect(7 * t**6, "448")
```

### Jacobian and Hessian

The **Jacobian** $\mathbf{J}$ is the matrix of first partials of a vector function; the **Hessian** $\mathbf{H}$ is the matrix of second partials of a scalar function.

$$J_{ij}=\frac{\partial f_{i}}{\partial x_{j}} \qquad H_{ij}=\frac{\partial^{2}f}{\partial x_{i}\,\partial x_{j}}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $J_{ij}$ | entry of the Jacobian matrix $\mathbf{J}$ | dimensionless |
| $H_{ij}$ | entry of the Hessian matrix $\mathbf{H}$ | dimensionless |
| $f_{i}$ | $i$-th component of a vector function | dimensionless |
| $x_{j}$ | $j$-th variable | dimensionless |

Holds when: the functions have continuous first partials ($\mathbf{J}$) or second partials ($\mathbf{H}$, which is then symmetric).
Breaks when: second partials are discontinuous, so $\mathbf{H}$ may be non-symmetric or undefined.
Source and basis: derived from the multivariable linear and quadratic approximations; see OpenStax [Calculus Volume 3](https://openstax.org/books/calculus-volume-3/pages/1-introduction).

- Polar map $(r,\theta)\mapsto(r\cos\theta,\,r\sin\theta)$: $\det\mathbf{J}=r$. With $r=2$ and $\theta=0.7$: $\det\mathbf{J}=2\cos^{2}\theta+2\sin^{2}\theta=2$.
- Linear algebra for $\mathbf{J}$ and $\mathbf{H}$ (determinant, eigenvalues) is in [Linear algebra and differential equations reference](reference-linear-algebra-differential-equations.md).

```verify
r = q(2, "")
th = q(0.7, "")
expect(cos(th) * r * cos(th) + r * sin(th) * sin(th), "2")
```

## Multiple integrals

### Double and triple integrals

$$\iint_{R}f\,dA=\int_{a}^{b}\int_{g_{1}(x)}^{g_{2}(x)}f(x,y)\,dy\,dx \qquad \iiint_{V}f\,dV=\int\!\!\int\!\!\int f\,dz\,dy\,dx$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $R$ | plane region of integration | $\text{m}^2$ |
| $V$ | solid region of integration | $\text{m}^3$ |
| $f$ | integrand (the result carries the unit of $f$ times area or volume) | dimensionless |
| $g_{1}$, $g_{2}$ | lower and upper bounding curves | m |
| $a$, $b$ | limits of the outer variable | m |

Holds when: $f$ is continuous on the region (Fubini's theorem allows either order of integration).
Breaks when: the integrand is unbounded on the region, or the limits are written in the wrong order (the inner limits may depend on the outer variable, never the reverse).
Source and basis: derived from summing over small area and volume elements; taught in [Multivariable calculus](04-multivariable-calculus.md).

- Order swap: sketch the region and read the limits again from the other direction.
- Example: $\int_{0}^{1}\int_{0}^{x}xy\,dy\,dx=\int_{0}^{1}x^{3}/2\,dx=\tfrac18=0.125$. A rectangle of $b=0.05\ \text{m}$ and $h=0.1\ \text{m}$ has $\iint y^{2}\,dA=bh^{3}/12$, which is $4.167\times 10^{-6}\ \text{m}^4$.

```verify
expect(1 / 8, "0.125")
b = q(0.05, "m")
h = q(0.1, "m")
given("12")
expect(b * h**3 / 12, "4.167e-6 m^4")
```

### Polar, cylindrical, and spherical coordinates

$$dA=r\,dr\,d\theta \qquad dV=r\,dr\,d\theta\,dz \qquad dV=r^{2}\sin\theta\,dr\,d\theta\,d\varphi$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $r$ | distance from the axis (polar, cylindrical) or from the origin (spherical) | m |
| $\theta$ | polar angle from $+z$ in spherical form; azimuth in polar and cylindrical form | rad |
| $\varphi$ | azimuth in spherical form | rad |
| $z$ | height | m |

Holds when: the angle convention is as stated (in spherical form $\theta$ is measured from the $+z$ axis, the same convention as the curvilinear forms below).
Breaks when: a source uses the other angle convention (many texts swap $\theta$ and $\varphi$); the factor $\sin\theta$ then moves. The factor $r$ or $r^{2}\sin\theta$ is dropped when the Jacobian is forgotten.
Source and basis: derived from the Jacobian of the coordinate change; see OpenStax [Calculus Volume 3](https://openstax.org/books/calculus-volume-3/pages/1-introduction).

| Conversion | Formulas |
|---|---|
| Polar to Cartesian | $x=r\cos\theta$, $y=r\sin\theta$ |
| Cylindrical to Cartesian | $x=r\cos\theta$, $y=r\sin\theta$, $z=z$ |
| Spherical to Cartesian | $x=r\sin\theta\cos\varphi$, $y=r\sin\theta\sin\varphi$, $z=r\cos\theta$ |

- Example: a disk of radius $R=0.5\ \text{m}$ has polar moment $J=\int_{0}^{2\pi}\int_{0}^{R}r^{3}\,dr\,d\theta=\pi R^{4}/2=0.0982\ \text{m}^4$. A sphere of radius $0.5\ \text{m}$ has $V=4\pi R^{3}/3=0.5236\ \text{m}^3$. And $\iint e^{-(x^{2}+y^{2})}dA=\pi=3.1416$ in polar form.

```verify
R = q(0.5, "m")
expect(pi * R**4 / 2, "0.0982 m^4")
expect(4 * pi * R**3 / 3, "0.5236 m^3")
expect(2 * pi * (1 / 2), "3.1416")
```

### Change of variables

$$\iint_{R}f(x,y)\,dx\,dy=\iint_{S}f\big(x(u,v),y(u,v)\big)\,\left\lvert\det\frac{\partial(x,y)}{\partial(u,v)}\right\rvert\,du\,dv$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $u$, $v$ | new coordinates | dimensionless |
| $x$, $y$ | original coordinates | m |
| $R$, $S$ | region in the old and new coordinates | $\text{m}^2$ |
| $\partial(x,y)/\partial(u,v)$ | Jacobian matrix of the map | m |

Holds when: the map is one-to-one and continuously differentiable with a nonzero Jacobian determinant on the region.
Breaks when: the map folds the region over itself, or the absolute value of the determinant is omitted (area and volume elements are positive).
Source and basis: derived from the area scaling of a linear map by its determinant; see OpenStax [Calculus Volume 3](https://openstax.org/books/calculus-volume-3/pages/1-introduction).

- Example: with $x=au$, $y=bv$ the Jacobian determinant is $ab$, so the ellipse with $a=3\ \text{m}$ and $b=2\ \text{m}$ has area $\pi ab=18.85\ \text{m}^2$.

```verify
a = q(3, "m")
b = q(2, "m")
expect(pi * a * b, "18.85 m^2")
```

### Surface area, mass, and center of mass

$$S=\iint_{R}\sqrt{1+f_{x}^{2}+f_{y}^{2}}\,dA \qquad M=\iiint_{V}\rho\,dV \qquad \bar{x}=\frac{1}{M}\iiint_{V}x\,\rho\,dV$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $S$ | area of the graph $z=f(x,y)$ over $R$ | $\text{m}^2$ |
| $f_{x}$, $f_{y}$ | slopes of the surface | dimensionless |
| $M$ | mass | kg |
| $\rho$ | density, possibly varying with position | $\text{kg/m}^3$ |
| $\bar{x}$ | $x$-coordinate of the center of mass | m |
| $x$ | position of a volume element | m |

Holds when: the surface is a smooth graph over $R$ and the density is integrable.
Breaks when: the surface folds over itself (use a parametric surface); for a uniform body the density cancels and $\bar{x}$ is the centroid.
Source and basis: derived from the area of a tilted plane element and the definition of the center of mass; see OpenStax [Calculus Volume 3](https://openstax.org/books/calculus-volume-3/pages/1-introduction).

- Example: the plane $z=x+y$ over the unit square has $S=\sqrt{3}=1.7321$. A uniform solid hemisphere of radius $R=0.2\ \text{m}$ has $\int z\,dV=\pi R^{4}/4$ and $V=2\pi R^{3}/3$, so $\bar{z}=3R/8=0.075\ \text{m}$.

```verify
expect(sqrt(1 + 1 + 1), "1.7321")
R = q(0.2, "m")
expect((pi * R**4 / 4) / (2 * pi * R**3 / 3), "0.075 m")
```

## Vector calculus

### Gradient, divergence, curl, and Laplacian

The **divergence** measures net outflow per unit volume; the **curl** measures local rotation; the **Laplacian** is the divergence of the gradient.

$$\nabla\cdot\mathbf{F}=\frac{\partial F_{x}}{\partial x}+\frac{\partial F_{y}}{\partial y}+\frac{\partial F_{z}}{\partial z} \qquad \nabla\times\mathbf{F}=\left(\frac{\partial F_{z}}{\partial y}-\frac{\partial F_{y}}{\partial z},\ \frac{\partial F_{x}}{\partial z}-\frac{\partial F_{z}}{\partial x},\ \frac{\partial F_{y}}{\partial x}-\frac{\partial F_{x}}{\partial y}\right) \qquad \nabla^{2}f=\frac{\partial^{2}f}{\partial x^{2}}+\frac{\partial^{2}f}{\partial y^{2}}+\frac{\partial^{2}f}{\partial z^{2}}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\mathbf{F}$ | vector field (a velocity field is used for the units) | m/s |
| $F_{x}$, $F_{y}$, $F_{z}$ | Cartesian components of $\mathbf{F}$ | m/s |
| $f$ | scalar field | dimensionless |
| $x$, $y$, $z$ | Cartesian coordinates | m |

Holds when: the components are differentiable (twice for the Laplacian) in right-handed Cartesian coordinates. The divergence carries $1/\text{s}$ for a velocity field, the curl $1/\text{s}$ as well, and the Laplacian the unit of $f$ per $\text{m}^2$.
Breaks when: the field has a singularity or the coordinates are curvilinear (use the forms in the next entry).
Source and basis: derived from the flux and circulation per unit volume and area in the limit of a small region; taught in [Multivariable calculus](04-multivariable-calculus.md).

- Example: $\mathbf{F}=(x^{2}y,\,yz,\,xz)$ has $\nabla\cdot\mathbf{F}=2xy+z+x$, which is $8$ at $(1,2,3)$, and $\nabla\times\mathbf{F}=(-y,\,-z,\,-x^{2})$, which is $(-2,-3,-1)$. The Laplacian of $x^{2}+y^{2}+z^{2}$ is $6$.

```verify
x = q(1, "")
y = q(2, "")
z = q(3, "")
expect(2 * x * y + z + x, "8")
expect(-y, "-2")
expect(-z, "-3")
expect(2 + 2 + 2, "6")
```

### Curvilinear forms

Cylindrical coordinates $(r,\theta,z)$ and spherical coordinates $(r,\theta,\varphi)$ with $\theta$ the polar angle from $+z$:

$$\nabla\cdot\mathbf{F}=\frac{1}{r}\frac{\partial(rF_{r})}{\partial r}+\frac{1}{r}\frac{\partial F_{\theta}}{\partial\theta}+\frac{\partial F_{z}}{\partial z} \qquad \nabla^{2}f=\frac{1}{r}\frac{\partial}{\partial r}\!\left(r\frac{\partial f}{\partial r}\right)+\frac{1}{r^{2}}\frac{\partial^{2}f}{\partial\theta^{2}}+\frac{\partial^{2}f}{\partial z^{2}}$$

$$(\nabla\times\mathbf{F})_{z}=\frac{1}{r}\left(\frac{\partial(rF_{\theta})}{\partial r}-\frac{\partial F_{r}}{\partial\theta}\right) \qquad \nabla\cdot\mathbf{F}=\frac{1}{r^{2}}\frac{\partial(r^{2}F_{r})}{\partial r}+\frac{1}{r\sin\theta}\frac{\partial(\sin\theta\,F_{\theta})}{\partial\theta}+\frac{1}{r\sin\theta}\frac{\partial F_{\varphi}}{\partial\varphi}$$

$$\nabla^{2}f=\frac{1}{r^{2}}\frac{\partial}{\partial r}\!\left(r^{2}\frac{\partial f}{\partial r}\right)+\frac{1}{r^{2}\sin\theta}\frac{\partial}{\partial\theta}\!\left(\sin\theta\frac{\partial f}{\partial\theta}\right)+\frac{1}{r^{2}\sin^{2}\theta}\frac{\partial^{2}f}{\partial\varphi^{2}}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $r$ | radial distance from the axis (cylindrical) or origin (spherical) | m |
| $\theta$ | azimuth (cylindrical) or polar angle from $+z$ (spherical) | rad |
| $\varphi$ | azimuth (spherical) | rad |
| $z$ | axial coordinate | m |
| $F_{r}$, $F_{\theta}$, $F_{z}$, $F_{\varphi}$ | field components along the local unit vectors | m/s |
| $f$ | scalar field | dimensionless |

Holds when: the unit vectors are taken in the order $(\hat{\mathbf{r}},\hat{\boldsymbol{\theta}},\hat{\mathbf{z}})$ for cylindrical and $(\hat{\mathbf{r}},\hat{\boldsymbol{\theta}},\hat{\boldsymbol{\varphi}})$ for spherical, each right-handed.
Breaks when: a source swaps the meaning of $\theta$ and $\varphi$; the factors $\sin\theta$ then appear in the wrong place. The unit vectors also vary with position, so do not differentiate components as if they were Cartesian.
Source and basis: derived from the scale factors of the coordinate system; see OpenStax [Calculus Volume 3](https://openstax.org/books/calculus-volume-3/pages/1-introduction).

- Gradient: cylindrical $\nabla f=\partial_{r}f\,\hat{\mathbf{r}}+\tfrac1r\partial_{\theta}f\,\hat{\boldsymbol{\theta}}+\partial_{z}f\,\hat{\mathbf{z}}$; spherical $\nabla f=\partial_{r}f\,\hat{\mathbf{r}}+\tfrac1r\partial_{\theta}f\,\hat{\boldsymbol{\theta}}+\tfrac{1}{r\sin\theta}\partial_{\varphi}f\,\hat{\boldsymbol{\varphi}}$.
- Example: a radial field $F_{r}=r^{2}$ has spherical divergence $4r=8$ at $r=2$. Rigid rotation $F_{\theta}=\omega r$ with $\omega=3\ \text{rad/s}$ has $(\nabla\times\mathbf{F})_{z}=2\omega=6\ \text{rad/s}$. And $\ln r$ is harmonic in cylindrical coordinates: $\tfrac1r\tfrac{d}{dr}(r\cdot\tfrac1r)=0$.

```verify
r = q(2, "")
expect((1 / r**2) * 4 * r**3, "8")
w = q(3, "rad/s")
expect(2 * w, "6 rad/s")
```

### Vector identities

$$\nabla\times(\nabla f)=\mathbf{0} \qquad \nabla\cdot(\nabla\times\mathbf{F})=0 \qquad \nabla\cdot(f\mathbf{F})=f\,\nabla\cdot\mathbf{F}+\mathbf{F}\cdot\nabla f \qquad \nabla\times(\nabla\times\mathbf{F})=\nabla(\nabla\cdot\mathbf{F})-\nabla^{2}\mathbf{F}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $f$ | scalar field | dimensionless |
| $\mathbf{F}$ | vector field | dimensionless |
| $\mathbf{0}$ | zero vector | dimensionless |

Holds when: $f$ and $\mathbf{F}$ have continuous second partials (so mixed partials commute).
Breaks when: the fields are not smooth at a point or along a line (a line vortex has zero curl away from the axis but not on it).
Source and basis: derived from the equality of mixed partial derivatives and the product rule.

- Also: $\nabla\times(f\mathbf{F})=f\,\nabla\times\mathbf{F}+\nabla f\times\mathbf{F}$ and $\nabla\cdot(\mathbf{F}\times\mathbf{G})=\mathbf{G}\cdot(\nabla\times\mathbf{F})-\mathbf{F}\cdot(\nabla\times\mathbf{G})$.
- Example: $f=x$, $\mathbf{F}=(x,y,z)$ gives $f\mathbf{F}=(x^{2},xy,xz)$ with divergence $4x$, which is $8$ at $x=2$. The right side is $3x+x=8$.

```verify
x = q(2, "")
expect(2 * x + x + x, "8")
expect(x * 3 + x * 1, "8")
```

## Integral theorems

### Line integrals

$$\int_{C}\mathbf{F}\cdot d\mathbf{r}=\int_{a}^{b}\mathbf{F}(\mathbf{r}(t))\cdot\mathbf{r}'(t)\,dt \qquad \int_{C}f\,ds=\int_{a}^{b}f(\mathbf{r}(t))\,\lvert\mathbf{r}'(t)\rvert\,dt$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\mathbf{F}$ | force field | N |
| $\mathbf{r}(t)$ | parametrization of the curve $C$ | m |
| $\mathbf{r}'(t)$ | tangent vector, derivative with respect to the parameter | m |
| $f$ | scalar density along the curve | dimensionless |
| $ds$ | element of arc length | m |
| $t$ | parameter | dimensionless |

Holds when: the curve is piecewise smooth and the integrand is continuous along it. The first integral is the work done by $\mathbf{F}$ along $C$ and changes sign when the direction is reversed; the second does not.
Breaks when: the parametrization stops (or reverses) partway along, or the direction of travel is not tracked.
Source and basis: derived from summing $\mathbf{F}\cdot\Delta\mathbf{r}$ over small steps; see OpenStax [Calculus Volume 3](https://openstax.org/books/calculus-volume-3/pages/1-introduction).

- Example: $\mathbf{F}=(-y,x)$ counterclockwise round a circle of radius $2$ with $\mathbf{r}=(2\cos t,\,2\sin t)$ has $\mathbf{F}\cdot\mathbf{r}'=4$, so the circulation is $8\pi=25.13$.

```verify
R = q(2, "")
expect(2 * pi * R**2, "25.13")
```

### Conservative fields and the gradient theorem

A field is **conservative** when its line integral between two points does not depend on the path.

$$\int_{C}\nabla\phi\cdot d\mathbf{r}=\phi(B)-\phi(A) \qquad \nabla\times\mathbf{F}=\mathbf{0}\ \Leftrightarrow\ \mathbf{F}=\nabla\phi$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\phi$ | scalar potential | dimensionless |
| $A$, $B$ | start and end points of $C$ | m |
| $\mathbf{F}$ | vector field | dimensionless |

Holds when: $\mathbf{F}$ is continuously differentiable on a simply connected region; then zero curl implies a potential exists.
Breaks when: the region has a hole (the field $\mathbf{F}=(-y,x)/(x^{2}+y^{2})$ has zero curl but circulation $2\pi$ around the origin).
Source and basis: derived from the fundamental theorem of calculus along the curve; see OpenStax [Calculus Volume 3](https://openstax.org/books/calculus-volume-3/pages/1-introduction).

- Example: $\mathbf{F}=(2xy,\,x^{2})=\nabla(x^{2}y)$, so from $(0,0)$ to $(1,2)$ the integral is $x^{2}y=2$ along any path.

```verify
expect(1**2 * 2 - 0, "2")
```

### Green's theorem

$$\oint_{C}\big(P\,dx+Q\,dy\big)=\iint_{R}\left(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\right)dA \qquad A=\tfrac12\oint_{C}\big(x\,dy-y\,dx\big)$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $P$, $Q$ | components of a plane field | dimensionless |
| $C$ | closed boundary of $R$, traversed counterclockwise | m |
| $R$ | plane region | $\text{m}^2$ |
| $A$ | area of $R$ | $\text{m}^2$ |

Holds when: $C$ is a simple closed piecewise smooth curve, counterclockwise, and $P$, $Q$ have continuous partials on $R$ and its boundary.
Breaks when: the field is singular inside $R$, or the region has a hole (add a boundary term for the hole, traversed clockwise).
Source and basis: derived from the fundamental theorem of calculus applied to strips of $R$; see OpenStax [Calculus Volume 3](https://openstax.org/books/calculus-volume-3/pages/1-introduction).

- Example: for $\mathbf{F}=(-y,x)$, $Q_{x}-P_{y}=2$, so the circulation round a disk of radius $2$ is $2\cdot\pi\cdot 2^{2}=25.13$, which matches the line integral above. The area formula for an ellipse gives $\pi ab$.

```verify
R = q(2, "")
expect(2 * pi * R**2, "25.13")
```

### Divergence theorem

$$\iiint_{V}\nabla\cdot\mathbf{F}\,dV=\iint_{\partial V}\mathbf{F}\cdot\hat{\mathbf{n}}\,dS$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\mathbf{F}$ | vector field | m/s |
| $V$ | solid region | $\text{m}^3$ |
| $\partial V$ | closed boundary surface of $V$ | $\text{m}^2$ |
| $\hat{\mathbf{n}}$ | outward unit normal | dimensionless |
| $dS$ | surface area element | $\text{m}^2$ |

Holds when: $V$ is bounded by a closed piecewise smooth surface and $\mathbf{F}$ is continuously differentiable throughout $V$. The right side is the net outward flux (here in $\text{m}^3/\text{s}$).
Breaks when: the field has a singularity inside $V$. The field $\hat{\mathbf{r}}/r^{2}$ has zero divergence away from the origin, yet its flux through every enclosing sphere is $4\pi$; applying the theorem naively gives zero and is wrong.
Source and basis: derived from the net flux through a small box equalling divergence times volume; see OpenStax [Calculus Volume 3](https://openstax.org/books/calculus-volume-3/pages/1-introduction).

- Example: $\mathbf{F}=(x,y,z)$ on a sphere of radius $2$: the flux is $4\pi R^{2}\cdot R=100.53$, and the volume integral of the divergence $3$ is $3\cdot 4\pi R^{3}/3$, the same number. The field $\hat{\mathbf{r}}/r^{2}$ on a sphere of radius $3$ has flux $\tfrac{1}{9}\cdot 4\pi\cdot 9=12.566$.

```verify
R = q(2, "")
expect(4 * pi * R**2 * R, "100.53")
expect(3 * 4 * pi * R**3 / 3, "100.53")
R2 = q(3, "")
expect((1 / R2**2) * 4 * pi * R2**2, "12.566")
```

### Stokes' theorem

$$\iint_{S}(\nabla\times\mathbf{F})\cdot\hat{\mathbf{n}}\,dS=\oint_{\partial S}\mathbf{F}\cdot d\mathbf{r}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\mathbf{F}$ | vector field | m/s |
| $S$ | orientable surface | $\text{m}^2$ |
| $\partial S$ | boundary curve, oriented by the right-hand rule with $\hat{\mathbf{n}}$ | m |
| $\hat{\mathbf{n}}$ | unit normal of the surface | dimensionless |

Holds when: $S$ is piecewise smooth and orientable, $\partial S$ is a piecewise smooth closed curve, and $\mathbf{F}$ is continuously differentiable on $S$ and its boundary.
Breaks when: the normal and the direction of travel round the boundary do not obey the right-hand rule (the sign flips), or the surface is not orientable (a Mobius strip).
Source and basis: derived from summing Green's theorem over small patches whose interior edges cancel; see OpenStax [Calculus Volume 3](https://openstax.org/books/calculus-volume-3/pages/1-introduction).

- Example: $\mathbf{F}=(-y,x,0)$ has curl $(0,0,2)$. Over a disk of radius $2$ the surface integral is $2\cdot\pi\cdot 2^{2}=25.13$, the same as the circulation round its edge. Any surface with the same boundary gives the same value.

```verify
R = q(2, "")
expect(2 * pi * R**2, "25.13")
```

## Optimization and constraints

### Critical points of a single variable

$$f'(x^{*})=0 \qquad f''(x^{*})>0\Rightarrow\text{local minimum},\quad f''(x^{*})<0\Rightarrow\text{local maximum}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $x^{*}$ | critical point | dimensionless |
| $f'$, $f''$ | first and second derivatives | dimensionless |

Holds when: $f$ is twice differentiable at $x^{*}$ and the point is interior to the domain.
Breaks when: $f''(x^{*})=0$ (inconclusive; test the sign of $f'$ on both sides), or the extreme value is at an endpoint or a corner of the domain, where $f'$ need not vanish. Compare all critical points and endpoints.
Source and basis: derived from the sign of the second-order Taylor term; taught in [Single-variable calculus](03-single-variable-calculus.md).

- Example: a closed cylindrical can of volume $V=0.001\ \text{m}^3$ has least surface for $h=2r$, with $r=(V/2\pi)^{1/3}=0.0542\ \text{m}$.

```verify
V = q(0.001, "m^3")
expect(cbrt(V / (2 * pi)), "0.0542 m")
```

### Second-derivative test for two variables

$$D=f_{xx}f_{yy}-f_{xy}^{2}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $D$ | determinant of the Hessian | dimensionless |
| $f_{xx}$, $f_{yy}$, $f_{xy}$ | second partial derivatives at the critical point | dimensionless |

Holds when: $\nabla f=\mathbf{0}$ at the point and the second partials are continuous. Then $D>0$ with $f_{xx}>0$ is a local minimum, $D>0$ with $f_{xx}<0$ a local maximum, and $D<0$ a saddle. In more variables, a minimum has all Hessian eigenvalues positive and a maximum all negative.
Breaks when: $D=0$ (inconclusive), or the extreme lies on the boundary of the domain.
Source and basis: derived from the sign of the quadratic form in the Taylor expansion; see OpenStax [Calculus Volume 3](https://openstax.org/books/calculus-volume-3/pages/1-introduction).

- Example: $f=x^{3}-3x+y^{2}$ has critical points $(\pm 1,0)$ and $D=12x$. At $(1,0)$, $D=12>0$ and $f_{xx}=6>0$, a minimum; at $(-1,0)$, $D=-12<0$, a saddle.

```verify
x = q(1, "")
expect(6 * x * 2 - 0, "12")
x2 = q(-1, "")
expect(6 * x2 * 2 - 0, "-12")
```

### Lagrange multipliers

Lagrange multipliers find extremes of a function on a constraint curve or surface by requiring the gradients to be parallel.

$$\nabla f=\lambda\,\nabla g,\qquad g(\mathbf{x})=c \qquad \nabla f=\sum_{k}\lambda_{k}\nabla g_{k}\ \text{(several constraints)}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $f$ | function to be extremized | dimensionless |
| $g$ | constraint function | dimensionless |
| $c$ | constraint value | dimensionless |
| $\lambda$ | multiplier, the rate of change of the optimum with $c$ | dimensionless |

Holds when: $f$ and $g$ are continuously differentiable and $\nabla g\neq\mathbf{0}$ on the constraint. The multiplier equals $df^{*}/dc$, the sensitivity of the best value to the constraint.
Breaks when: the constraint is an inequality (check each boundary and the interior; see the Karush-Kuhn-Tucker conditions), or the constraint set is unbounded so no extreme exists. The conditions are necessary, not sufficient; compare the candidates.
Source and basis: derived from requiring that no direction along the constraint changes $f$ to first order; see OpenStax [Calculus Volume 3](https://openstax.org/books/calculus-volume-3/pages/1-introduction).

- Example 1: maximize $xy$ with $x+y=10$. Then $y=\lambda$, $x=\lambda$, so $x=y=5$ and $xy=25$ (the sum $5+5=10$ meets the constraint).
- Example 2: the point of the plane $x+2y+3z=14$ nearest the origin has $2(x,y,z)=\lambda(1,2,3)$, so $\lambda=2$ and the point is $(1,2,3)$, where $1+4+9=14$, at distance $\sqrt{14}=3.7417$.

```verify
expect(5 + 5, "10")
expect(5 * 5, "25")
lam = q(2, "")
check(lam / 2 + 2 * lam + 3 * lam * 3 / 2 == 14, "plane constraint satisfied")
expect(1 * 1 + 2 * 2 + 3 * 3, "14")
expect(sqrt(1**2 + 2**2 + 3**2), "3.7417")
```

## Checklists

Before trusting a derivative or integral:

- [ ] The function is differentiable (or integrable) on the whole interval; no pole, corner, or jump hides inside.
- [ ] Angles are in radians in every trigonometric derivative, integral, and series.
- [ ] The result has the expected unit: derivative is unit of $f$ per unit of $x$; integral is unit of $f$ times unit of $x$.
- [ ] A differentiated antiderivative returns the integrand.
- [ ] A definite integral's limits changed with the substitution, and the order of limits is upper minus lower.
- [ ] An improper integral was tested for convergence before it was evaluated.

Before trusting a series:

- [ ] The point lies inside the radius of convergence.
- [ ] The remainder bound uses the maximum of the next derivative over the whole interval.
- [ ] Endpoints of the interval of convergence were tested separately.

Before trusting a multiple or vector integral:

- [ ] The region is sketched and the limits are read from the sketch.
- [ ] The Jacobian factor ($r$, or $r^{2}\sin\theta$) is present for non-Cartesian coordinates.
- [ ] The angle convention (which angle is the polar one) is stated and used consistently.
- [ ] For a theorem, the field is smooth inside the region (no point source), the boundary is closed, and the orientation obeys the right-hand rule.
- [ ] A limiting case (constant field, a circle, a unit square) gives the known answer.

Before trusting an optimum:

- [ ] Critical points and boundary points were all compared.
- [ ] The second-derivative test was applied, or the value was compared with neighbours.
- [ ] A constrained answer satisfies the constraint.

## Sanity checks

- Derivative of a constant is $0$; derivative of $x^{n}$ drops the power by $1$; integral raises it by $1$.
- The integral of a positive function over a positive interval is positive and lies between (minimum value) times (interval length) and (maximum value) times (interval length).
- An even function integrates to twice the half-interval value over a symmetric interval; an odd function integrates to $0$.
- $\sin x\approx x$ and $\cos x\approx 1-x^{2}/2$ for small $x$ in radians; at $x=0.1$ the errors are about $1.7\times 10^{-4}$ and $4\times 10^{-6}$.
- Divergence of a gradient field is the Laplacian; curl of a gradient is zero; divergence of a curl is zero.
- The area of a unit circle is $\pi$; its circumference is $2\pi$; a unit sphere has surface $4\pi$ and volume $4\pi/3$.
- Differentiating under an integral or summing a series term by term needs a justification (uniform convergence); if the result looks wrong, this is a first suspect.
- A numerical integral that changes in the second digit when the step is halved has not converged; see [Probability and numerical methods reference](reference-probability-numerical-methods.md).

## Further reference

- [*Calculus Volume 1*](https://openstax.org/books/calculus-volume-1/pages/1-introduction), [*Calculus Volume 2*](https://openstax.org/books/calculus-volume-2/pages/1-introduction), and [*Calculus Volume 3*](https://openstax.org/books/calculus-volume-3/pages/1-introduction) by OpenStax: free, openly licensed texts for single-variable, series and integration techniques, and multivariable and vector calculus.
- [Single Variable Calculus](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/) and [Multivariable Calculus](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/) by MIT OpenCourseWare: free courses with lecture videos and problem sets.
- [Paul's Online Math Notes](https://tutorial.math.lamar.edu/) by Paul Dawkins, Lamar University: free worked examples and tables.
- [NIST Digital Library of Mathematical Functions](https://dlmf.nist.gov/) by NIST: free. Integrals, series, and special functions.
- Stewart, *Calculus* (paid): single and multivariable calculus.
- Thomas, *Thomas' Calculus* (paid): calculus with engineering applications.
- Marsden and Tromba, *Vector Calculus* (paid): the integral theorems in depth.
- Gradshteyn and Ryzhik, *Table of Integrals, Series, and Products* (paid): large integral and series tables.
- Spivak, *Calculus* (paid): the rigorous treatment of limits and continuity.
