# Partial differential equations and Fourier series

**Type:** lesson
**Verify:** strict

A partial differential equation (PDE) is an equation that relates a function of several variables, such as temperature in space and time, to its partial derivatives. Engineers meet PDEs whenever a quantity varies in both place and time: heat spreading through a part, a string or beam vibrating, a field settling around an electrode. Fourier series is the tool that turns many of these problems into a list of ordinary differential equations that can be solved by hand.

**Prerequisites:** [Differential equations](06-differential-equations.md), [Multivariable calculus](04-multivariable-calculus.md) (partial derivatives), [Linear algebra](05-linear-algebra.md) (eigenvalues and orthogonal vectors)
**Time:** 8-12 h

## Core ideas

- A **partial differential equation** involves an unknown function of two or more independent variables, such as $u(x,t)$, and its partial derivatives. An ordinary differential equation has only one independent variable.
- The **order** of a PDE is the highest derivative that appears. A PDE is **linear** when the unknown and its derivatives appear only to the first power and are not multiplied together. Linear PDEs obey **superposition**: a sum of solutions is a solution.
- Three linear second-order PDEs cover a large part of engineering. Each describes a different physical behavior.
  - The **heat equation** $u_t = \alpha u_{xx}$ describes diffusion: temperature in a solid, a dissolved chemical in a liquid, a consolidating soil layer. It smooths things out and only runs forward in time.
  - The **wave equation** $u_{tt} = c^2 u_{xx}$ describes motion that travels or oscillates: a string, a rod in axial vibration, sound in a pipe, a transmission line. It conserves energy and runs equally well backward.
  - The **Laplace equation** $\nabla^2 u = 0$ describes a steady state with no time in it: temperature after everything has settled, the electric potential between conductors, the velocity potential of an ideal flow. Its solutions have no interior peaks or dips.
- An **initial condition** gives the unknown at the starting time, for example the temperature profile at $t = 0$. A **boundary condition** gives it, or its slope, on the edge of the region. Three common kinds:
  - **Dirichlet** fixes the value ($u = 0$ at an end held at a set temperature or a clamped string end).
  - **Neumann** fixes the slope ($u_x = 0$ at an insulated end, because heat flux is proportional to slope).
  - **Robin** fixes a mix of value and slope, such as convection at a surface.
- A problem is **well posed** when a solution exists, is unique, and changes only a little when the data change a little. The heat equation run backward in time is not well posed.
- A **Fourier series** writes a periodic function as a sum of sines and cosines. Each term is a **mode**. For a PDE with simple boundaries, each mode evolves independently, and the full solution is the sum.

### Fourier series

For a function $f(x)$ of period $2L$ (it repeats after $2L$), the Fourier series is a constant plus a sum of sine and cosine modes of frequency $n\pi/L$. The coefficients come from the fact that sines and cosines of different $n$ are **orthogonal**: the integral of their product over one period is zero. Multiplying the series by one mode and integrating isolates that mode's coefficient, in the same way a dot product isolates one component of a vector.

If $f$ is odd (its graph is mirrored through the origin), only sine terms survive. If $f$ is even, only cosines survive. A function given only on $0 \le x \le L$ can be continued as an odd function, which gives a pure sine series that is zero at both ends. This is the right series for Dirichlet boundaries.

**Convergence.** If $f$ is piecewise smooth, the series converges to $f(x)$ at every point where $f$ is continuous. At a jump, it converges to the average of the values on the two sides. Coefficients fall as $1/n$ at a jump, $1/n^2$ when $f$ is continuous with a kink, and faster when $f$ is smoother. A smooth start gives a series that needs few terms.

**Gibbs effect.** Near a jump, the partial sums overshoot the true value by about 9 percent of the jump height. Adding terms squeezes the overshoot toward the jump but does not shrink it. The overshoot is not an error in the coefficients. It is a property of approximating a sharp step with smooth waves, and it also appears in digital filters and in finite element and finite difference results near sharp steps in the solution.

### Separation of variables

**Separation of variables** assumes the solution is a product of a function of space only and a function of time only, $u(x,t) = X(x)\,T(t)$. Substituting into a linear PDE with homogeneous boundary conditions splits it into two ordinary equations joined by a constant $-\lambda$. The space equation $X'' + \lambda X = 0$ with the boundary conditions has solutions only for special values $\lambda_n$, called **eigenvalues**, with shapes $X_n$ called **eigenfunctions**. For both ends fixed at zero on a length $L$:

- $X_n(x) = \sin(n\pi x / L)$ with $\lambda_n = (n\pi/L)^2$, for $n = 1, 2, 3, \dots$
- The time equation then depends on the PDE. For heat it is first order, so each mode decays. For the wave equation it is second order, so each mode oscillates.
- Superposition adds all modes, and the initial condition fixes their coefficients through the Fourier formulas.

Separation works for linear PDEs on simple shapes (an interval, rectangle, disk) when the boundary conditions are homogeneous. A boundary held at a nonzero value is handled by subtracting a steady solution first. Complicated shapes need numerical methods, taken up in [Finite element method](../simulation/01-finite-element-method.md).

## Key equations

Symbols: $u$ = unknown field (temperature in K for heat, displacement in m for a string); $x$ = position (m); $t$ = time (s); $\alpha$ = thermal diffusivity, $k/(\rho c_p)$ (m$^2$/s); $c$ = wave speed (m/s); $L$ = length of the rod or string (m); $n$ = mode number (1, 2, 3, ...); $F_T$ = string tension (N); $\mu$ = mass per unit length (kg/m).

Heat, wave, and Laplace equations in one or more space dimensions:

$$
u_t = \alpha\, u_{xx} \qquad u_{tt} = c^2 u_{xx} \qquad \nabla^2 u = 0
$$

The heat equation holds for constant $\alpha$, no internal heat source, and conduction only. It breaks when the material properties change strongly with temperature or when convection or radiation moves most of the heat. The wave equation holds for small slopes in a perfectly flexible, uniform string; it breaks for large amplitudes and for stiff strings, where bending adds a term.

Wave speed on a string:

$$
c = \sqrt{F_T / \mu}
$$

Fourier series on $-L \le x \le L$, with coefficients:

$$
f(x) = \frac{a_0}{2} + \sum_{n=1}^{\infty}\left[a_n \cos\frac{n\pi x}{L} + b_n \sin\frac{n\pi x}{L}\right]
$$

$$
a_n = \frac{1}{L}\int_{-L}^{L} f(x)\cos\frac{n\pi x}{L}\,dx \qquad b_n = \frac{1}{L}\int_{-L}^{L} f(x)\sin\frac{n\pi x}{L}\,dx
$$

Sine series for $f(x)$ on $0 \le x \le L$ (Dirichlet ends):

$$
b_n = \frac{2}{L}\int_{0}^{L} f(x)\sin\frac{n\pi x}{L}\,dx
$$

For a constant $f = u_0$, the integral gives $b_n = 4u_0/(n\pi)$ for odd $n$ and zero for even $n$.

Heat in a rod with both ends held at $u = 0$ and initial profile $f(x)$:

$$
u(x,t) = \sum_{n=1}^{\infty} b_n \sin\frac{n\pi x}{L}\, e^{-\alpha (n\pi/L)^2 t}
$$

The decay rate of mode $n$ is $\alpha (n\pi/L)^2$, so high modes die much faster. The slowest mode sets the **time constant** $\tau = L^2/(\alpha\pi^2)$.

Vibrating string, ends fixed, released from rest with initial shape $f(x)$:

$$
u(x,t) = \sum_{n=1}^{\infty} b_n \sin\frac{n\pi x}{L}\cos(\omega_n t), \qquad \omega_n = \frac{n\pi c}{L}, \quad f_n = \frac{n c}{2L}
$$

## Worked example

**Cooling of a rod.** A rod of length $L = 0.50$ m has thermal diffusivity $\alpha = 1.0 \times 10^{-4}$ m$^2$/s (a typical value for a good metal conductor). It starts at a uniform temperature 100 K above the temperature of its two ends, which are held at the lower temperature. The sides are insulated. Find the temperature rise above the ends at the center after 300 s.

**Given:** $L = 0.50$ m, $\alpha = 1.0\times 10^{-4}$ m$^2$/s, $u_0 = 100$ K (excess over the ends), $t = 300$ s, $x = L/2$.

**Find:** $u(L/2, 300\ \text{s})$.

**Assumptions:** one-dimensional conduction, constant $\alpha$, no heat source, ends exactly at the reference temperature for $t > 0$.

**Solution:**

1. Measured above the end temperature, the ends satisfy $u = 0$ and the start is $u = u_0$, so the sine series applies with $b_n = 4u_0/(n\pi)$ for odd $n$. The first coefficient is $b_1 = 4u_0/\pi = 127.3$ K.
2. The first decay rate is $\alpha\pi^2/L^2 = 3.948\times 10^{-3}$ s$^{-1}$. After 300 s the exponent is $1.184$, so the first mode has fallen to $e^{-1.184} = 0.3059$.
3. At the center $\sin(n\pi/2)$ is $+1$ for $n = 1$ and $-1$ for $n = 3$. First term: $127.3 \times 0.3059 = 38.95$ K.
4. The third term has the opposite sign and size 0.001 K. It is negligible, and higher terms are smaller still.

**Answer:** $u(L/2, 300\ \text{s}) \approx 38.95$ K above the end temperature. The center has cooled a great deal but is still well above the ends.

**Sanity check:** the time constant is $\tau = 1/(3.948\times 10^{-3}) = 253.3$ s. After 300 s, slightly more than one time constant, the profile is nearly a single half-sine whose peak has decayed by about $e^{-1.2}$, which matches a bit over a third of the start. Heat can only leave through the ends, so the temperature never falls below the end value.

<details><summary>Verification</summary>

```verify
L = q(0.50, "m")
alpha = q(1.0e-4, "m^2/s")
u0 = q(100, "K")
t = q(300, "s")
b1 = 4 * u0 / pi
expect(b1, "127.3 K")
lam1 = alpha * pi**2 / L**2
expect(lam1, "3.948e-3 1/s")
expect(lam1 * t, "1.184")
f1 = exp(-lam1 * t)
expect(f1, "0.3059")
expect(b1 * f1, "38.95 K")
expect(b1 / 3 * exp(-9 * lam1 * t), "0.001 K", rel=0.1)
expect(b1 * f1 - b1 / 3 * exp(-9 * lam1 * t), "38.95 K")
expect(1 / lam1, "253.3 s")
check(b1 * f1 < u0, "the center is cooler than the start and warmer than the ends")
```

</details>

## Practice

1. A square wave of height $\pm 1$ has the sine series $\sum b_n \sin(n\pi x/L)$ with $b_n = 4/(n\pi)$ for odd $n$. Find $b_1$.
2. A rod of length 0.20 m has $\alpha = 1.0\times 10^{-4}$ m$^2$/s and both ends held at the reference temperature. Find the time constant $\tau = L^2/(\alpha\pi^2)$ in seconds.
3. A string of length 0.65 m has tension 70 N and mass per length $4.0\times 10^{-4}$ kg/m. Find its fundamental frequency $f_1$ in Hz.
4. For the string in problem 3, find the wave speed $c$ in m/s and the frequency of the second harmonic in Hz.
5. In the worked example, how long does the first mode need to fall to 1 percent of its initial size? Use the first decay rate only, because higher modes have already decayed faster. Give the answer in seconds. Decide first which of the three equations models the problem.

<details><summary>Answers</summary>

1. 1.273
2. 40.53 s
3. 321.8 Hz
4. $c = 418.3$ m/s; second harmonic 643.6 Hz
5. The heat equation applies (diffusion). The time is the inverse of the decay rate times the natural log of the ratio of start to end, which is 1166.5 s.

```verify
b1 = 4 / pi
expect(b1, "1.273", ans=1)
alpha = q(1.0e-4, "m^2/s")
tau = q(0.20, "m")**2 / (alpha * pi**2)
expect(tau, "40.53 s", ans=2)
Ft = q(70, "N")
mu = q(4.0e-4, "kg/m")
Ls = q(0.65, "m")
c = sqrt(Ft / mu)
expect(c / (2 * Ls), "321.8 Hz", ans=3)
expect(c, "418.3 m/s", ans=4)
expect(2 * c / (2 * Ls), "643.6 Hz", ans=4)
lam1 = alpha * pi**2 / q(0.50, "m")**2
expect(log(100) / lam1, "1166.5 s", ans=5)
```

</details>

## Common mistakes

- Using the wrong boundary condition. A fixed end gives sines, an insulated end gives cosines. Swapping them gives a solution that satisfies the equation and the wrong problem.
- Treating the Gibbs overshoot as a bug in the code or the coefficients and adding more terms to remove it. It stays near 9 percent of the jump.
- Applying separation of variables with a nonzero boundary value. Subtract a steady solution first so the remaining problem has zero boundaries.
- Keeping too few terms near $t = 0$. High modes decay quickly, so late-time results need one or two terms, but the start needs many.
- Running the heat equation backward in time to find an earlier state. Small noise in the data grows without bound, so the problem is not well posed.

## Go deeper

- [Differential Equations (18.03SC)](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/) by MIT OpenCourseWare: Fourier series and the heat and wave equations are covered in its later units.
- [Linear Partial Differential Equations: Analysis and Numerics (18.303)](https://ocw.mit.edu/courses/18-303-linear-partial-differential-equations-analysis-and-numerics-fall-2014/) by MIT OpenCourseWare: eigenfunctions, Green's functions, and numerical solution.
- [Finite Element Analysis of Solids and Fluids I (2.092)](https://ocw.mit.edu/courses/2-092-finite-element-analysis-of-solids-and-fluids-i-fall-2009/) by MIT OpenCourseWare: how PDEs on real shapes are solved numerically.
- [Heat transfer](../physics/12-heat-transfer.md) and [Vibrations](../physics/13-vibrations.md): where these equations come from physically.
- Next: [Finite element method](../simulation/01-finite-element-method.md).
- [Math reference](reference.md): the lookup sheet for this folder.
