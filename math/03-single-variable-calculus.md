# Single-variable calculus

**Type:** lesson

Calculus is the branch of mathematics that describes change: a derivative gives the rate at which something changes, and an integral adds up many small pieces. Engineers use derivatives for velocity, slope, and heat flow, and integrals for deflection, total work, and total heat.

**Prerequisites:** [Algebra](01-algebra.md), [Trigonometry](02-trigonometry.md)
**Time:** 40-60 h (limits, derivatives, integrals, and series, in that order)

## Core ideas

- A limit describes what a function approaches as its input approaches a value. You do not need the function to be defined at that exact point. Example: $\lim_{x \to 0} \dfrac{\sin x}{x} = 1$.
- The derivative $f'(x)$ is the slope of the tangent line, or the instantaneous rate of change. It is defined as the limit of the average rate of change over a shrinking interval.
- Useful rules: power rule $\frac{d}{dx} x^n = n x^{n-1}$, product rule, quotient rule, and chain rule. The chain rule handles a function inside another function.
- The integral $\int_a^b f(x)\,dx$ is the signed area under $f$ from $a$ to $b$. It is also the limit of a sum of thin slices.
- The fundamental theorem of calculus connects the two ideas. Differentiation and integration are inverse operations. If $F' = f$, then $\int_a^b f\,dx = F(b) - F(a)$.
- A series is a sum of infinitely many terms. A Taylor series approximates a smooth function with polynomials around a point. Keeping only the first few terms gives an approximation with a known error, which engineers rely on for small angles and small strains.
- Engineering rule of thumb: if a quantity is given as a rate, integrate it to get the total. If a quantity is a total, differentiate it to get the rate.

## Key equations

Derivative definition:

$$f'(x) = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}$$

Fundamental theorem of calculus:

$$\int_a^b f(x)\,dx = F(b) - F(a), \quad \text{where } F'(x) = f(x)$$

Taylor series of $\sin x$ about $0$ ($x$ in radians):

$$\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots$$

Euler-Bernoulli beam relation for small deflections $w(x)$ (m), bending moment $M(x)$ (N m), flexural rigidity $EI$ (N m$^2$), where $E$ is Young's modulus (Pa) and $I$ is the second moment of area (m$^4$):

$$\frac{d^2 w}{dx^2} = \frac{M(x)}{EI}$$

Symbols: $f$ is any function, $h$ is a small step, $x$ is position (m) unless stated otherwise.

## Worked example

**Given:** A steel cantilever beam, fixed at $x = 0$ and free at $x = L = 2.0\ \mathrm{m}$, carries a point load $P = 1000\ \mathrm{N}$ at its free end. Width $b = 0.05\ \mathrm{m}$, height $h = 0.10\ \mathrm{m}$, $E = 200\ \mathrm{GPa}$ (typical value for steel).

**Find:** The tip deflection $\delta$.

**Assumptions:** Small deflections, linear elastic material, beam weight neglected.

**Solution:**

1. Second moment of area of the rectangle: $I = \dfrac{b h^3}{12} = \dfrac{0.05 \times 0.10^3}{12} = 4.167 \times 10^{-6}\ \mathrm{m^4}$.
2. Bending moment at distance $x$ from the fixed end, measured from the load: $M(x) = P(L - x)$ in magnitude.
3. Integrate the curvature $M/EI$ twice with the boundary conditions $w(0) = 0$ and $w'(0) = 0$, then evaluate at $x = L$. The result is $\delta = \dfrac{P L^3}{3 E I}$.
4. Check the integral numerically with `scipy.integrate.quad`, using the unit-load form $\delta = \int_0^L \dfrac{P (L-x)^2}{EI}\,dx$. It returns $0.0032\ \mathrm{m}$.
5. Substitute: $\delta = \dfrac{1000 \times 2.0^3}{3 \times 200\times10^9 \times 4.167\times10^{-6}} = 0.0032\ \mathrm{m}$.

**Answer:** $\delta = 3.2\ \mathrm{mm}$ downward.

**Sanity check:** The beam is 2 m long and 100 mm deep. A tip deflection of about $1/600$ of the span is small, so the small-deflection assumption holds. Doubling $L$ would multiply $\delta$ by 8, which is the $L^3$ behavior you expect for a cantilever.

## Practice

1. Find $\dfrac{d}{dx}(x^3)$ at $x = 2$.
2. Evaluate $\int_0^2 3x^2\,dx$.
3. Find $\lim_{x \to 0} \dfrac{\sin x}{x}$.
4. A cantilever carries $P = 500\ \mathrm{N}$ at its tip. $L = 1.5\ \mathrm{m}$, $E = 200\ \mathrm{GPa}$, $I = 4.167 \times 10^{-6}\ \mathrm{m^4}$. Find the tip deflection in millimeters.
5. Use $1 + x + x^2/2$ to approximate $e^{0.1}$. How large is the error?

<details><summary>Answers</summary>

1. $12$
2. $8$
3. $1$
4. $\approx 0.675\ \mathrm{mm}$
5. $\approx 0.00017$ (the approximation is $1.1050$, and the true value is $1.10517$)

</details>

## Common mistakes

- Forgetting the chain rule, for example differentiating $\sin(3x)$ as $\cos(3x)$.
- Dropping the limits of integration, or evaluating $F(a)$ and $F(b)$ in the wrong order.
- Mixing up a rate and a total. Ask which one the problem gives you before choosing derivative or integral.
- Using a Taylor series far from its center point. Approximations are accurate only near the point where they are built.
- Mishandling units: a moment of inertia in cm$^4$ used with SI formulas gives an answer that is off by $10^8$.

## Go deeper

- [Active Calculus](https://activecalculus.org/) by Matthew Boelkins and collaborators: free, openly licensed calculus textbook (CC BY-SA).
- [Calculus Volume 1](https://openstax.org/books/calculus-volume-1/pages/1-introduction) by OpenStax: free online calculus textbook.
- [Calculus I, II, and III notes](https://tutorial.math.lamar.edu/) by Paul Dawkins, Paul's Online Math Notes: worked examples for limits, derivatives, and integrals.
- Next: [Multivariable calculus](04-multivariable-calculus.md).
- [Math reference](reference.md): the lookup sheet for this topic.
