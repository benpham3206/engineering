# Differential equations

**Type:** lesson

A differential equation is a statement that relates a function to its own derivatives. Many physical laws, including cooling, motion, circuits, and vibration, are written this way, so engineers solve them to predict how a system changes over time, and to design it so that it settles at the required value.

**Prerequisites:** [Single-variable calculus](03-single-variable-calculus.md), [Linear algebra](05-linear-algebra.md) for systems
**Time:** 50-70 h

## Core ideas

- An ordinary differential equation (ODE) has one independent variable, usually time $t$. Its order is the highest derivative that appears: $y'$ is first order, $y''$ is second order.
- A solution is a function that makes the equation true. A general solution has arbitrary constants. Initial conditions, such as $y(0) = y_0$, pick out one specific solution.
- First-order linear ODEs model rates that depend on the current state, such as Newton's law of cooling and simple charging of a capacitor. Their solutions are exponentials.
- Second-order ODEs model inertia and restoring forces: a spring-mass-damper, a pendulum for small angles, and an RLC circuit. The behavior depends on the damping ratio $\zeta$. Underdamped systems oscillate, critically damped systems return fastest without overshoot, and overdamped systems creep back slowly.
- Systems of ODEs are several coupled equations, such as two masses on springs. They are written in matrix form and solved with eigenvalues, which links directly to the previous lesson.
- The Laplace transform turns a linear ODE with constant coefficients into an algebra problem in $s$. Solve the algebra, then transform back. It handles sudden inputs well, such as a step load or a switch that turns on at a time.
- Numerical solvers (covered in the numerical methods lesson) handle equations that have no closed-form solution. Always check a numerical answer against a simple analytic case first.

## Key equations

Newton's law of cooling for a body at temperature $T$ (degrees C), ambient temperature $T_a$, and rate constant $k$ (1/min):

$$\frac{dT}{dt} = -k\,(T - T_a) \quad \Rightarrow \quad T(t) = T_a + (T_0 - T_a)\,e^{-kt}$$

Second-order mass-spring-damper, with mass $m$ (kg), damping $c$ (N s/m), stiffness $k$ (N/m):

$$m\,x'' + c\,x' + k\,x = 0$$

Damping ratio and natural frequency:

$$\zeta = \frac{c}{2\sqrt{km}}, \qquad \omega_n = \sqrt{\frac{k}{m}}$$

For $\zeta < 1$, the damped frequency is $\omega_d = \omega_n\sqrt{1 - \zeta^2}$.

Laplace transform of a unit step and of $t$:

$$\mathcal{L}\{1\} = \frac{1}{s}, \qquad \mathcal{L}\{t\} = \frac{1}{s^2}$$

## Worked example

**Given:** A steel part at $180^\circ\mathrm{C}$ is placed in air at $T_a = 25^\circ\mathrm{C}$. After 10 minutes it reads $120^\circ\mathrm{C}$.

**Find:** (a) The cooling constant $k$. (b) The time to reach $40^\circ\mathrm{C}$.

**Assumptions:** Lumped-capacity cooling (the part is at one uniform temperature), Newton's law of cooling holds, the ambient temperature is constant.

**Solution:**

1. Solution form: $T(t) = T_a + (T_0 - T_a)\,e^{-kt}$.
2. Use the 10-minute reading: $120 = 25 + 155\,e^{-10k}$, so $e^{-10k} = 95/155$.
3. Solve for $k$: $k = \dfrac{1}{10}\ln\dfrac{155}{95} = 0.04895\ \mathrm{min^{-1}}$.
4. Solve for the time $t$ at $T = 40^\circ\mathrm{C}$: $t = \dfrac{1}{k}\ln\dfrac{155}{15} = 47.7\ \mathrm{min}$.
5. Check numerically with `scipy.integrate.solve_ivp` integrated to $t = 47.7$ min. It returns $T = 40.00^\circ\mathrm{C}$.

**Answer:** $k \approx 0.0490\ \mathrm{min^{-1}}$, and the part reaches $40^\circ\mathrm{C}$ after about 48 minutes.

**Sanity check:** The first 10 minutes dropped the temperature by 60 degrees. The remaining drop to 40 degrees is 80 degrees, and it takes about 38 more minutes. Cooling slows as the part approaches room temperature, which the exponential shape predicts.

A second-order example: $m = 2\ \mathrm{kg}$, $c = 4\ \mathrm{N\,s/m}$, $k = 50\ \mathrm{N/m}$, released from $x_0 = 0.02\ \mathrm{m}$ at rest. Then $\zeta = 0.2$ (underdamped), $\omega_n = 5$ rad/s, $\omega_d = 4.899$ rad/s, and $x(1\ \mathrm{s}) = -0.000111\ \mathrm{m}$. The analytic and numerical results agree to six decimal places.

## Practice

1. Solve $y' = -2y$ with $y(0) = 5$. Find $y(1)$ to four decimal places.
2. A mass $m = 1\ \mathrm{kg}$ on a spring with $k = 100\ \mathrm{N/m}$ and no damping. Find the period of free oscillation in seconds.
3. For $m = 2\ \mathrm{kg}$ and $k = 50\ \mathrm{N/m}$, find the critical damping $c$ in N s/m.
4. Find $\mathcal{L}\{t\}$ evaluated at $s = 2$.

<details><summary>Answers</summary>

1. $y(1) \approx 0.6767$
2. $\approx 0.6283\ \mathrm{s}$
3. $c = 20\ \mathrm{N\,s/m}$
4. $0.25$

</details>

## Common mistakes

- Forgetting the constant of integration, then applying the initial condition to the wrong constant.
- Using $\ln$ of a negative number. Check the sign of $T - T_a$ or $T_0 - T_a$ first.
- Mixing the time units. A rate in per-minute needs time in minutes.
- Calling a system underdamped without computing $\zeta$. Compute $\zeta$ before deciding.
- Applying the Laplace transform to a nonlinear equation, where it does not apply.

## Go deeper

- [Ordinary Differential Equations (18.03SC)](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/) by MIT OpenCourseWare: full course with lectures on first-order, second-order, and Laplace methods.
- [Differential Equations notes](https://tutorial.math.lamar.edu/classes/de/de.aspx) by Paul Dawkins, Paul's Online Math Notes: chapters on first-order, second-order, and Laplace transforms with worked examples.
- Next: [Probability and statistics](07-probability-and-statistics.md).
- [Math reference](reference.md): the lookup sheet for this topic.
