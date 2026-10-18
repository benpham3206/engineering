# Multivariable calculus

**Type:** lesson

Multivariable calculus handles functions of several variables, such as temperature that depends on both $x$ and $y$. Engineers use it for heat flow, fluid flow, stress in plates, the center of mass of irregular parts, and the moments of inertia that govern how a shaft or beam resists bending.

**Prerequisites:** [Single-variable calculus](03-single-variable-calculus.md), [Linear algebra](05-linear-algebra.md) helps for vector work but is not required first
**Time:** 40-60 h

## Core ideas

- A function $f(x, y)$ gives one number for each point in a plane. Its graph is a surface.
- A partial derivative $\partial f / \partial x$ is the derivative with respect to $x$, holding $y$ constant. Partial derivatives are the building block of everything else in this lesson.
- The gradient $\nabla f = \left(\dfrac{\partial f}{\partial x}, \dfrac{\partial f}{\partial y}\right)$ is a vector. It points in the direction of steepest increase, and its length is the rate of increase in that direction.
- A double integral $\iint_R f\,dA$ adds up $f$ over a region $R$ in the plane. Use it for area, mass of a plate with varying density, and the second moment of area of a cross section.
- Changing the order of integration, or switching to polar or other coordinates, often makes an integral easier. Choose coordinates that match the shape of the region.
- A line integral adds up a quantity along a curve. A surface integral adds up a quantity over a surface. Both show up in work done along a path and in flux through a surface.
- Vector calculus adds the divergence and curl operators. You will meet them in fluid and electromagnetic courses. Learn the gradient first.
- The Laplacian, $\nabla^2 T = \dfrac{\partial^2 T}{\partial x^2} + \dfrac{\partial^2 T}{\partial y^2}$, appears in steady heat conduction. A steady temperature field satisfies $\nabla^2 T = 0$ wherever there is no heat source.

## Key equations

Gradient of $f(x, y)$:

$$\nabla f = \frac{\partial f}{\partial x}\,\mathbf{i} + \frac{\partial f}{\partial y}\,\mathbf{j}$$

Fourier's law of heat conduction in a plate, where $\mathbf{q}$ is heat flux (W/m$^2$), $k$ is thermal conductivity (W/(m K)), and $T$ is temperature (K or degrees C, since only differences matter here):

$$\mathbf{q} = -k\,\nabla T$$

Second moment of area of a region $R$ about the $x$-axis, with $y$ measured from the centroid (m$^4$):

$$I_x = \iint_R y^2\,dA$$

For a rectangle of width $b$ and height $h$, this gives $I_x = \dfrac{b h^3}{12}$.

## Worked example

**Given:** A flat plate has temperature $T(x, y) = 200 - 30x - 10y$ (degrees C), with $x$ and $y$ in meters. The plate's thermal conductivity is $k = 50\ \mathrm{W/(m\,K)}$, a typical value for steel.

**Find:** The heat flux vector $\mathbf{q}$ and its magnitude at the point $(0.5, 0.2)$ m.

**Assumptions:** Steady conduction, no internal heat generation, isotropic material.

**Solution:**

1. Partial derivatives of $T$: $\dfrac{\partial T}{\partial x} = -30$, and $\dfrac{\partial T}{\partial y} = -10$. Both are constant, so the point does not matter.
2. Gradient: $\nabla T = (-30, -10)\ \mathrm{C/m}$.
3. Apply Fourier's law: $\mathbf{q} = -k\,\nabla T = -50 \times (-30, -10) = (1500, 500)\ \mathrm{W/m^2}$.
4. Magnitude: $|\mathbf{q}| = \sqrt{1500^2 + 500^2} = 1581.1\ \mathrm{W/m^2}$.

**Answer:** $\mathbf{q} = (1500, 500)\ \mathrm{W/m^2}$, magnitude about $1.58\ \mathrm{kW/m^2}$. Heat flows toward lower temperature, which is the $+x$ and $+y$ direction here.

**Sanity check:** Heat should flow from hot to cold. $T$ decreases in both $+x$ and $+y$, so the flux should point in those directions, and it does. The sign is right.

A double-integral check: for a rectangle of width $b = 0.05\ \mathrm{m}$ and height $h = 0.10\ \mathrm{m}$, centered on its centroid, $\iint y^2\,dA$ evaluated numerically with `scipy.integrate.dblquad` over $y \in [-0.05, 0.05]$, $x \in [0, 0.05]$, gives $4.167 \times 10^{-6}\ \mathrm{m^4}$. This matches $bh^3/12$.

## Practice

1. For $f(x, y) = x^2 y$, find $\nabla f$ at $(1, 2)$.
2. Find $\iint_D 1\,dA$ over the unit disk $x^2 + y^2 \le 1$.
3. Evaluate $\int_0^1 \int_0^2 (x + y)\,dy\,dx$.
4. A plate has $T = 100 - 40x$ (degrees C) with $k = 20\ \mathrm{W/(m\,K)}$. Find the magnitude of $\mathbf{q}$ in W/m$^2$.

<details><summary>Answers</summary>

1. $\nabla f = (4, 1)$
2. $\pi \approx 3.1416$
3. $3$
4. $800\ \mathrm{W/m^2}$

</details>

## Common mistakes

- Holding the wrong variable constant when taking a partial derivative.
- Forgetting the minus sign in Fourier's law, which reverses the flux direction.
- Using $\dfrac{\partial}{\partial x}$ on a term that also depends on $y$ without including the $y$ dependence in the other partials.
- Mixing up the order of limits in a double integral. The inner limits can depend on the outer variable, not the reverse.
- Computing a moment of inertia about the wrong axis. $I_x$ and $I_y$ use different distance measures.

## Go deeper

- [Multivariable Calculus](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/) by MIT OpenCourseWare (18.02SC): full course with lecture videos and problem sets, openly shared.
- [Calculus III notes](https://tutorial.math.lamar.edu/) by Paul Dawkins, Paul's Online Math Notes: partial derivatives, multiple integrals, and vector calculus with worked examples.
- [Active Calculus](https://activecalculus.org/) by Matthew Boelkins and collaborators: free, openly licensed calculus text (CC BY-SA) for a single-variable review.
- Next: [Linear algebra](05-linear-algebra.md).
- [Math reference](reference.md): the lookup sheet for this topic.
