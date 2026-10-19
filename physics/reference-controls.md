# Controls reference

**Type:** reference
**Verify:** strict

Lookup sheet for modeling, time response, stability tests, loop shaping, PID, state space, and sampled-data control of linear feedback systems, for an engineer who needs a formula, a limit, or a check in the middle of a design.

## Principles

- Feedback trades gain for error. A higher loop gain shrinks error and sensitivity to plant change, and it pushes the loop toward instability.
- A linear time-invariant (LTI) system is fully set by its transfer function, or equivalently by its state matrices. Poles set the modes, zeros shape how much of each mode appears.
- Stability is a property of the closed loop, not of the controller or plant alone. Every stability test below applies to LTI systems with a rational transfer function, unless the entry says how a delay is handled.
- Integrators in the loop remove steady error and cost phase. A pole at the origin is a $-90$ degree lag at every frequency.
- Delay and right-half-plane zeros are limits, not tuning problems. No controller removes them, and they cap the usable crossover frequency.
- Actuators saturate. A linear design says nothing about large signals, so check what the loop does when the actuator hits its limit.
- Sampling adds delay of about half a sample period. Sample fast enough that this lag is small at the crossover frequency.
- Margins measure distance to instability. A loop that is stable on paper with a small margin fails when the plant changes.
- Model the plant before the controller. A controller tuned on the wrong model only looks good in simulation.

## Models and linearization

### Linearization

A **linearization** replaces a nonlinear function by its tangent at an operating point, so the linear tools below can be used for small deviations around that point.

$$f(x) \approx f(x_0) + \left.\frac{df}{dx}\right|_{x_0}(x - x_0)$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $f$ | nonlinear function of the state (here dimensionless) | dimensionless |
| $x$ | state variable (here an angle) | rad |
| $x_0$ | operating point | rad |

Holds when: the deviation $x - x_0$ is small, $f$ is differentiable at $x_0$, and the system stays near that operating point.
Breaks when: the system moves far from $x_0$, $f$ has a corner or a dead zone at $x_0$, or the operating point itself drifts (a gain-scheduled design is then needed).
Source and basis: derived from the first-order Taylor expansion; taught in [Feedback control](14-controls.md).

Example: a pendulum has restoring torque proportional to $\sin\theta$. About $\theta_0 = 0$ the linear model replaces $\sin\theta$ by $\theta$. At $\theta = 0.3$ rad, $\sin\theta = 0.2955$ and the linear value 0.3 is high by a relative error of 0.0152.

<details><summary>Verification</summary>

```verify
th = q(0.3, "rad")
expect(sin(th), "0.2955")
expect((th - sin(th)) / sin(th), "0.0152")
```

</details>

## Transfer functions and block diagrams

### Block algebra

A **transfer function** $G(s)$ is the ratio of the Laplace transform of the output to that of the input, with zero initial conditions. Transform tables are in [Laplace transform tables](../math/reference-linear-algebra-differential-equations.md). For blocks $G_1$ and $G_2$ (and a sensor $H$ in the feedback path):

$$G_{\text{series}} = G_1 G_2 \qquad G_{\text{parallel}} = G_1 + G_2 \qquad T(s) = \frac{G_c G_p}{1 + G_c G_p H} = \frac{L}{1 + L}\ \text{(unity sensor)}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $G_1$, $G_2$ | transfer functions of two blocks | dimensionless |
| $G_c$, $G_p$, $H$ | controller, plant, and sensor transfer functions | dimensionless |
| $L$ | loop transfer function $G_c G_p H$ | dimensionless |
| $T$ | closed-loop transfer function from reference to output | dimensionless |

Holds when: all blocks are LTI and the signals share consistent units, so that each product is dimensionless or carries units that cancel around the loop. For negative feedback the denominator is $1 + L$; for positive feedback it is $1 - L$.
Breaks when: a block is nonlinear (saturation, friction, backlash), a block loads the one before it (then model them together), or a pole and a zero cancel across blocks and hide an unstable mode.
Source and basis: derived from solving the linear algebraic block equations; taught in [Feedback control](14-controls.md).

Example: a loop has $L(0) = 2.5$. The closed-loop DC gain is $L(0)/(1 + L(0)) = 0.714$, so the output settles at 0.714 of the reference.

<details><summary>Verification</summary>

```verify
L0 = q(2.5, "")
expect(L0 / (1 + L0), "0.714")
```

</details>

### Mason's gain rule

**Mason's gain rule** gives the transfer function of a signal-flow graph in one formula. It is useful when a block diagram has nested loops that block algebra handles clumsily.

$$T = \frac{\sum_k P_k \Delta_k}{\Delta}, \qquad \Delta = 1 - \sum L_i + \sum L_i L_j - \cdots$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $P_k$ | gain of the $k\text{th}$ forward path | dimensionless |
| $L_i$ | gain of the $i\text{th}$ feedback loop | dimensionless |
| $\Delta$ | determinant of the graph | dimensionless |
| $\Delta_k$ | $\Delta$ with all loops touching path $k$ removed | dimensionless |

Holds when: the graph is linear. In $\Delta$, the products $L_i L_j$ run over pairs of loops that share no node, the triple products over triples of mutually non-touching loops, and so on.
Breaks when: loops are counted that touch (they must be excluded from the products), or the system is nonlinear.
Source and basis: derived from Cramer's rule applied to the linear signal-flow equations.

## Poles, zeros, and time response

Poles are the roots of the denominator of $G(s)$ and zeros the roots of the numerator. A real pole at $s = -a$ ($a > 0$) gives a decaying exponential with time constant $1/a$. A complex pair at $-\sigma \pm j\omega_d$ gives an oscillation with envelope $e^{-\sigma t}$. A pole in the right half plane gives growth. Poles closest to the imaginary axis dominate the slow part of the response. A zero in the right half plane (non-minimum phase) makes the step response start in the wrong direction and limits the achievable bandwidth; keep the crossover well below the zero frequency.

### First-order step response

A first-order system has one real pole and responds to a step by an exponential approach to its final value.

$$G(s) = \frac{K}{\tau s + 1} \qquad y(t) = K\left(1 - e^{-t/\tau}\right) \qquad t_{2\%} = \tau \ln 50 \approx 4\tau$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $K$ | steady-state (DC) gain | dimensionless |
| $\tau$ | time constant | s |
| $y$ | step response of unit step input | dimensionless |
| $t$ | time | s |
| $t_{2\%}$ | time after which $y$ stays within 2 percent of its final value | s |

Holds when: the system is LTI and first order, the step is applied at $t = 0$ with zero initial state, and $K$ and $\tau$ are positive.
Breaks when: a second pole is within about a decade of $1/\tau$ (the curve is then S-shaped), there is dead time, or the actuator saturates.
Source and basis: derived from the inverse Laplace transform of $K/(s(\tau s + 1))$; taught in [Feedback control](14-controls.md).

Example: $K = 2$, $\tau = 0.5$ s. At $t = 2$ s the output is $y = 1.963$. The 2 percent settling time is $\tau \ln 50 = 1.96$ s, so the estimate $4\tau = 2$ s is slightly conservative.

<details><summary>Verification</summary>

```verify
given("50")
K = q(2, "")
tau = q(0.5, "s")
t = q(2, "s")
expect(K * (1 - exp(-t / tau)), "1.963")
expect(tau * log(50), "1.96 s")
expect(4 * tau, "2 s")
```

</details>

### Second-order step metrics

A standard second-order system with unity DC gain is set by its natural frequency $\omega_n$ and damping ratio $\zeta$. The metrics below are for a unit step and $0 < \zeta < 1$ (underdamped).

$$G(s) = \frac{\omega_n^2}{s^2 + 2\zeta\omega_n s + \omega_n^2}$$

$$\omega_d = \omega_n\sqrt{1 - \zeta^2} \qquad M_p = \exp\!\left(-\frac{\pi\zeta}{\sqrt{1 - \zeta^2}}\right) \qquad t_p = \frac{\pi}{\omega_d}$$

$$t_r = \frac{\pi - \arccos\zeta}{\omega_d} \qquad t_{s,2\%} \approx \frac{4}{\zeta\omega_n} \qquad t_{s,5\%} \approx \frac{3}{\zeta\omega_n}$$

$$\zeta = \frac{-\ln M_p}{\sqrt{\pi^2 + \ln^2 M_p}}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $s$ | Laplace variable | 1/s |
| $\omega_n$, $\omega_d$ | natural and damped angular frequency | rad/s |
| $\zeta$ | damping ratio | dimensionless |
| $M_p$ | peak overshoot as a fraction of the final value | dimensionless |
| $t_p$ | time of the first peak | s |
| $t_r$ | rise time from 0 to 100 percent (first crossing of the final value) | s |
| $t_{s,2\%}$, $t_{s,5\%}$ | settling time into a band of 2 or 5 percent around the final value | s |

Holds when: the closed loop is well approximated by two dominant poles with no nearby zero or third pole, the input is a step, and the system is linear. The settling time is the last time the response leaves the stated band. The estimates use the envelope $e^{-\zeta\omega_n t}$ equal to the band, so $e^{-4} = 0.0183$ for 2 percent. They overestimate the true settling time slightly.
Breaks when: a zero near the poles adds overshoot, a third pole slows the rise, dead time is present, or the loop saturates. The 10 to 90 percent rise time is shorter than $t_r$ above and must be simulated if a specification uses that definition. At $\zeta \ge 1$ there is no overshoot; use the two real-pole time constants instead. Vibration use of the same model is in [Vibrations reference](reference-vibrations.md).
Source and basis: derived from the inverse Laplace transform of the step response; taught in [Feedback control](14-controls.md).

Example: $\zeta = 0.5$, $\omega_n = 10$ rad/s. Then $\omega_d = 8.66$ rad/s, overshoot $M_p = 0.163$, peak time 0.363 s, rise time 0.242 s, and 2 percent settling about 0.80 s (5 percent about 0.60 s). An overshoot spec of 0.2 requires $\zeta \ge 0.456$.

<details><summary>Verification</summary>

```verify
z = q(0.5, "")
wn = q(10, "rad/s")
wd = wn * sqrt(1 - z**2)
expect(wd, "8.66 rad/s")
expect(exp(-pi * z / sqrt(1 - z**2)), "0.163")
expect(pi / wd, "0.363 s")
expect((pi - acos(z)) / wd, "0.242 s")
expect(4 / (z * wn), "0.80 s")
expect(3 / (z * wn), "0.60 s")
expect(exp(-4), "0.0183")
Mp = q(0.2, "")
expect(-log(Mp) / sqrt(pi**2 + log(Mp)**2), "0.456")
```

</details>

## Steady-state error and system type

The **system type** is the number of free integrators (poles at $s = 0$) in the loop transfer function $L(s)$. For unity feedback, the final value theorem gives the steady error for a reference $R(s)$.

$$e_{ss} = \lim_{s \to 0}\frac{s R(s)}{1 + L(s)} \qquad K_p = \lim_{s\to 0} L(s) \quad K_v = \lim_{s\to 0} sL(s) \quad K_a = \lim_{s\to 0} s^2 L(s)$$

| Loop type | Step error | Ramp error | Parabola error |
|---|---|---|---|
| 0 | $1/(1 + K_p)$ | infinite | infinite |
| 1 | 0 | $1/K_v$ | infinite |
| 2 | 0 | 0 | $1/K_a$ |

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $e_{ss}$ | steady-state error for a unit-amplitude reference | dimensionless |
| $R$ | Laplace transform of the reference | dimensionless |
| $L$ | loop transfer function | dimensionless |
| $K_p$ | position error constant | dimensionless |
| $K_v$ | velocity error constant | 1/s |
| $K_a$ | acceleration error constant | $1/\text{s}^{2}$ |

Holds when: the closed loop is stable (the theorem fails otherwise), feedback is unity and negative, and the reference is a unit step, ramp, or parabola as in the table.
Breaks when: the closed loop is unstable or has poles on the imaginary axis, the reference is sinusoidal (use the frequency response), or a nonlinearity such as dead zone or friction leaves a residual error that the linear formula cannot see.
Source and basis: derived from the final value theorem applied to $E(s) = R(s)/(1 + L(s))$; taught in [Feedback control](14-controls.md).

Example: $L(s) = 20/(s(s + 2))$ is type 1 with $K_v = 20/2 = 10$ 1/s, so the unit-ramp error is 0.1. A type 0 loop with $K_p = 4$ leaves a step error of 0.2.

<details><summary>Verification</summary>

```verify
Kv = q(20, "") / q(2, "") * q(1, "1/s")
expect(Kv, "10 1/s")
expect(1 / Kv * q(1, "1/s"), "0.1")
Kp = q(4, "")
expect(1 / (1 + Kp), "0.2")
```

</details>

## Stability

A linear system is **bounded-input bounded-output (BIBO) stable** when every bounded input gives a bounded output. For an LTI system with a rational transfer function in lowest terms, this holds exactly when every pole has a negative real part (all poles in the left half plane). A pole on the imaginary axis gives a response that does not decay (marginal), and a repeated imaginary-axis pole gives growth. Internal stability, which also covers hidden modes, needs every eigenvalue of the state matrix $\mathbf{A}$ in the left half plane. Closed-loop stability needs every root of $1 + L(s) = 0$, the characteristic equation, in the left half plane. For a sampled system the condition is every pole inside the unit circle (see the sampled-data entries).

The tests that follow (Routh, root locus, Nyquist, margins) are for LTI systems with rational transfer functions, with the delay treatment noted where it applies.

### Routh criterion

The **Routh criterion** counts the roots of a polynomial in the right half plane from its coefficients, without finding the roots. For a cubic $a_3 s^3 + a_2 s^2 + a_1 s + a_0$ with $a_3 > 0$ the first column of the Routh table is below, and the cubic is stable exactly when every entry is positive.

$$\text{first column: } a_3,\quad a_2,\quad b_1 = \frac{a_2 a_1 - a_3 a_0}{a_2},\quad a_0$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $a_3$, $a_2$, $a_1$, $a_0$ | coefficients of the characteristic polynomial | dimensionless |
| $b_1$ | first entry of the $s^1$ row | dimensionless |

Holds when: the polynomial has real coefficients and comes from a lumped LTI system (rational transfer function). For higher order, each new row is built from the two rows above by the same cross-multiplication, and the number of sign changes in the first column equals the number of right-half-plane roots. A necessary condition is that all coefficients are positive.
Breaks when: a delay is present (the polynomial is not finite; use Nyquist or a Pade model), or a first-column entry is zero or a whole row is zero. For a zero entry with nonzero rest of the row, replace it by a small $\epsilon$ and let $\epsilon \to 0^+$, or test the reversed polynomial. A whole row of zeros means roots symmetric about the origin: form the auxiliary polynomial from the row above, differentiate it to fill the zero row, and continue; the auxiliary polynomial's roots are among the roots of the original and show imaginary-axis pairs.
Source and basis: derived from the Routh-Hurwitz theorem on the argument of the polynomial along the imaginary axis; taught in [Feedback control](14-controls.md).

Example: the closed loop of $L(s) = K/(s(s + 2)(s + 3))$ has characteristic polynomial $s^3 + 5s^2 + 6s + K$. The first column is $1,\ 5,\ (30 - K)/5,\ K$, so the loop is stable for $0 < K < 30$. At $K = 20$, $b_1 = 2$. At $K = 30$ the $s^1$ row is zero, the auxiliary polynomial is $5s^2 + 30$, and the loop oscillates at $\omega = \sqrt{6} = 2.45$ rad/s.

<details><summary>Verification</summary>

```verify
a3 = q(1, "")
a2 = q(5, "")
a1 = q(6, "")
K = q(20, "")
expect((a2 * a1 - a3 * K) / a2, "2")
Kmax = a2 * a1 / a3
expect(Kmax, "30")
expect(sqrt(Kmax / a2) * q(1, "rad/s"), "2.45 rad/s")
```

</details>

## Root locus

The **root locus** is the set of closed-loop pole positions as a gain $K$ goes from 0 to infinity in $1 + K\,N(s)/D(s) = 0$. It lets a designer see how a gain change moves every pole.

$$\angle\frac{N(s)}{D(s)} = \pm 180^\circ (2k + 1) \qquad K = \frac{|D(s)|}{|N(s)|} \qquad \sigma_a = \frac{\sum p_i - \sum z_j}{n - m} \qquad \phi_a = \frac{180^\circ(2k + 1)}{n - m}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $N$, $D$ | numerator (degree $m$) and denominator (degree $n$) of $L$ without the gain | dimensionless |
| $K$ | loop gain | dimensionless |
| $p_i$, $z_j$ | open-loop poles and zeros | 1/s |
| $\sigma_a$ | asymptote centroid on the real axis | 1/s |
| $\phi_a$ | asymptote angle, $k = 0, 1, \ldots, n - m - 1$ | rad |

Holds when: $L$ is rational and LTI, and negative feedback is used with $K > 0$. The rules are

- There are $n$ branches. Each starts at an open-loop pole ($K = 0$) and ends at an open-loop zero or at infinity ($K \to \infty$).
- A point on the real axis is on the locus if the count of poles plus zeros to its right is odd.
- $n - m$ branches go to infinity along the asymptotes with centroid $\sigma_a$ and angles $\phi_a$.
- Breakaway and break-in points are real roots of $dK/ds = 0$ (equivalently $D'N - DN' = 0$) that lie on the locus.
- A point $s_0$ is on the locus if the angle condition holds, and the gain there is given by the magnitude condition.
- Imaginary-axis crossings and the gain there come from the Routh table.

Breaks when: the loop has a delay (the locus then has infinitely many branches; use a Pade model for a few of them), the gain enters nonlinearly, or parameters other than a gain vary (rewrite the characteristic equation in the form $1 + K\,N/D$ first).
Source and basis: derived from the polar form of $1 + K\,N(s)/D(s) = 0$; taught in [Feedback control](14-controls.md).

Example: $L(s) = K/(s(s + 2)(s + 3))$ has three branches. The asymptote centroid is $-5/3 = -1.67$ with angles $60^\circ$, $180^\circ$, and $300^\circ$. The real-axis segments are $(-2, 0)$ and $(-\infty, -3)$. Breakaway satisfies $3s^2 + 10s + 6 = 0$, giving $s = -0.785$ (on the locus) and $s = -2.55$ (not on the locus). The gain at breakaway is $K = 2.11$. The imaginary-axis crossing at $K = 30$ matches the Routh example.

<details><summary>Verification</summary>

```verify
given("180", "300", "10", "30")
sa = (q(0, "") - 2 - 3) / 3
expect(sa, "-1.67")
expect(pi / 3, "60 deg")
sb = (-10 + sqrt(10**2 - 4 * 3 * 6)) / (2 * 3)
expect(sb, "-0.785")
expect((-10 - sqrt(10**2 - 4 * 3 * 6)) / (2 * 3), "-2.55")
expect(-sb * (sb + 2) * (sb + 3), "2.11")
```

</details>

## Frequency response and Bode plots

The **frequency response** of a stable LTI system is $G(j\omega)$, the steady-state gain and phase shift for a sinusoidal input at angular frequency $\omega$. A **Bode plot** shows $20\log_{10}|G(j\omega)|$ in decibels and $\angle G(j\omega)$ against $\log\omega$. Factors multiply, so their decibel magnitudes and phases add.

### First-order Bode factor

$$|G(j\omega)| = \frac{K}{\sqrt{1 + (\omega\tau)^2}} \qquad \angle G(j\omega) = -\arctan(\omega\tau) \qquad \omega_c = \frac{1}{\tau}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $K$ | DC gain | dimensionless |
| $\tau$ | time constant | s |
| $\omega$ | angular frequency | rad/s |
| $\omega_c$ | corner frequency | rad/s |

Holds when: the factor is a stable real pole $1/(\tau s + 1)$. The asymptotes are a flat line at $20\log_{10} K$ below the corner and a line falling at 20 dB per decade above it. The true curve is 3.01 dB below the asymptote intersection at the corner, where the phase is $-45^\circ$. The phase goes from $0$ to $-90^\circ$, reaching about $-6^\circ$ one decade below and $-84^\circ$ one decade above the corner. A pole at the origin is a line of slope $-20$ dB per decade with phase $-90^\circ$. A real zero reverses the signs of slope and phase. A complex pair at damping ratio $\zeta$ falls at 40 dB per decade above $\omega_n$ with phase from $0$ to $-180^\circ$, and its resonant peak is in [Vibrations reference](reference-vibrations.md).
Breaks when: the factor is unstable or non-minimum phase (a right-half-plane zero has the magnitude of a left-half-plane zero but the phase of a pole, so magnitude alone no longer fixes phase), a delay is present (phase falls without limit and magnitude stays flat), or poles lie within about a decade of each other so the asymptote picture is rough.
Source and basis: derived from substituting $s = j\omega$ in the transfer function; taught in [Feedback control](14-controls.md).

Example: $\tau = 0.1$ s, so the corner is 10 rad/s. At $\omega = 100$ rad/s the magnitude is 0.0995, which is $-20.04$ dB, against $-20$ dB on the asymptote. At the corner the magnitude is $-3.01$ dB and the phase is $-45^\circ$.

<details><summary>Verification</summary>

```verify
tau = q(0.1, "s")
w = q(100, "rad/s")
expect(1 / tau, "10 rad/s")
expect(1 / sqrt(1 + (w * tau)**2), "0.0995")
expect(20 * log10(1 / sqrt(1 + (w * tau)**2)), "-20.04")
expect(20 * log10(1 / sqrt(2)), "-3.01")
expect(20 * log10(1 / (w * tau)), "-20")
expect(-atan(1), "-45 deg")
```

</details>

## Nyquist criterion

The **Nyquist criterion** decides closed-loop stability from the plot of the open-loop frequency response $L(j\omega)$ for $\omega$ from $-\infty$ to $\infty$, closed by a large semicircle at infinity. It is the test to use when the loop has a delay or is open-loop unstable.

$$Z = N + P$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $Z$ | number of closed-loop poles in the right half plane | dimensionless |
| $N$ | net clockwise encirclements of the point $-1$ by the plot | dimensionless |
| $P$ | number of open-loop poles in the right half plane | dimensionless |

Holds when: $L$ is LTI and its poles on the imaginary axis (an integrator, for example) are bypassed by small indentations into the right half plane, which adds the corresponding large arcs to the plot. The closed loop is stable exactly when $Z = 0$. A delay $e^{-sT}$ is allowed, since it only rotates the plot. Counterclockwise encirclements count as negative $N$.
Breaks when: the plot passes through $-1$ (marginal), the sign convention for feedback differs from negative unity feedback (shift the critical point), or the model is wrong near crossover, where the plot comes closest to $-1$.
Source and basis: derived from the argument principle applied to $1 + L(s)$; taught in [Feedback control](14-controls.md).

Example: an open-loop unstable plant has $P = 1$. The closed loop is stable only if the plot encircles $-1$ once counterclockwise ($N = -1$), since then $Z = 0$. With no encirclement, $Z = 1$.

<details><summary>Verification</summary>

```verify
N = q(-1, "")
P = q(1, "")
expect(N + P, "0")
expect(q(0, "") + P, "1")
```

</details>

## Gain and phase margins

The **phase margin** $\phi_m$ is the extra phase lag that would bring the loop to instability, measured at the gain crossover frequency $\omega_c$ where $|L(j\omega_c)| = 1$. The **gain margin** $g_m$ is the factor by which the gain could rise before instability, measured at the phase crossover frequency $\omega_{pc}$ where $\angle L = -180^\circ$.

$$\phi_m = \pi + \angle L(j\omega_c) \qquad g_m = \frac{1}{|L(j\omega_{pc})|} \qquad \zeta \approx \frac{\phi_m}{100^\circ}$$

For the standard second-order loop $L(s) = \omega_n^2/(s(s + 2\zeta\omega_n))$ the margin is exact:

$$\phi_m = \arctan\frac{2\zeta}{\sqrt{\sqrt{1 + 4\zeta^4} - 2\zeta^2}}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\phi_m$ | phase margin | rad |
| $g_m$ | gain margin (a pure ratio; $20\log_{10} g_m$ in dB) | dimensionless |
| $L$ | open-loop frequency response | dimensionless |
| $\omega_c$ | gain crossover frequency | rad/s |
| $\omega_{pc}$ | phase crossover frequency | rad/s |
| $\zeta$ | damping ratio of the closed loop | dimensionless |

Holds when: the open loop is stable with a single crossover, and the loop is LTI. The rule $\zeta \approx \phi_m/100$ with $\phi_m$ in degrees is approximate. It is a straight-line fit to the exact second-order curve, good to a few percent for $\zeta$ up to about 0.6, and it overestimates beyond that. It does not hold for loops that are not close to second order. A margin of about $45^\circ$ and a gain margin of 2 or more are common design floors; the right value depends on how much the plant varies.
Breaks when: there are several crossover frequencies (read the Nyquist plot instead), the open loop is unstable (margins alone do not decide stability), or a delay is present (it lowers $\phi_m$ without changing the magnitude). Large margins can coexist with a high peak of the sensitivity function if the plot passes close to $-1$ at another frequency.
Source and basis: derived from the definitions and the Nyquist criterion; the exact second-order formula is derived from $|L(j\omega_c)| = 1$. Taught in [Feedback control](14-controls.md).

Example: $L(s) = 4/(s(s + 2))$ has $\omega_n = 2$ rad/s and $\zeta = 0.5$. The crossover is where $\omega\sqrt{\omega^2 + 4} = 4$, so $\omega_c = 1.572$ rad/s. The phase margin is $90^\circ - \arctan(\omega_c/2) = 51.8^\circ$, against the approximate rule 50 degrees. For the cubic loop $L(s) = 10/(s(s + 2)(s + 3))$ the phase crossover is at $\omega_{pc} = \sqrt{6}$ rad/s where $|L| = 0.333$, so $g_m = 3.00$, or 9.54 dB. This agrees with the Routh limit $K = 30$.

<details><summary>Verification</summary>

```verify
given("50", "10", "30")
wc = sqrt(-2 + sqrt(4 + 4 * 4))
expect(wc, "1.572")
expect(pi / 2, "90 deg")
pm = pi / 2 - atan(wc / 2)
expect(pm, "51.8 deg")
z = q(0.5, "")
expect(atan(2 * z / sqrt(sqrt(1 + 4 * z**4) - 2 * z**2)), "51.8 deg")
w = sqrt(6)
mag = 10 / (w * sqrt(w**2 + 4) * sqrt(w**2 + 9))
expect(mag, "0.333")
expect(1 / mag, "3.00")
expect(20 * log10(1 / mag), "9.54")
```

</details>

## PID control

A **PID controller** forms the control input from the error $e = r - y$ by three terms, proportional (present error), integral (accumulated error), and derivative (rate of change). Two common forms are the parallel form and the standard (ideal) form, related by $K_i = K_p/T_i$ and $K_d = K_p T_d$.

$$u = K_p e + K_i\int e\,dt + K_d \frac{de}{dt} \qquad C(s) = K_p\left(1 + \frac{1}{T_i s} + T_d s\right) \qquad D(s) = \frac{K_d s}{T_f s + 1}, \quad T_f = \frac{T_d}{N}$$

For anti-windup by back-calculation the integrator state $I$ obeys

$$\dot I = K_i e + \frac{u_{\text{sat}} - u}{T_t}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $K_p$ | proportional gain | dimensionless |
| $K_i$ | integral gain | 1/s |
| $K_d$ | derivative gain | s |
| $T_i$, $T_d$ | integral time and derivative time | s |
| $T_f$ | time constant of the derivative filter | s |
| $N$ | filter ratio $T_d/T_f$, a design choice | dimensionless |
| $u$, $u_{\text{sat}}$ | commanded and actually applied control input | dimensionless |
| $T_t$ | tracking time constant of the anti-windup loop | s |
| $e$ | error | dimensionless |

Holds when: controller output and error are in the same units (so the gains reduce to the units listed), the plant is linear and well described by a first- or second-order model with modest delay, the measurement is acceptably clean, and the actuator operates within its limits.
Breaks when: the derivative acts on a noisy measurement without a filter (the term amplifies noise by up to $K_p N$ at high frequency), the integrator winds up while the actuator saturates (the output overshoots badly as it unwinds), or the plant has long dead time (the gain that works on paper then oscillates). A derivative on the reference creates a spike at every step; apply it to the measurement only.
Source and basis: derived from the Laplace transform of the control law; effects below follow from the loop shape. Tuning rules such as Ziegler-Nichols are empirical, are not registered in this sheet, and are left out.

| Increase alone | Rise time | Overshoot | Steady error | Stability margin | Noise sensitivity |
|---|---|---|---|---|---|
| $K_p$ | shorter | larger | smaller, not removed for type 0 | smaller | slight rise |
| $K_i$ | slightly shorter | larger | removed for a step | smaller | slight rise |
| $K_d$ | slightly longer | smaller | no direct effect | larger when well filtered | larger |

The table gives typical trends only; interactions between the terms can reverse an entry.

Example: $K_p = 2$, $T_i = 0.5$ s, $T_d = 0.1$ s gives $K_i = 4$ 1/s and $K_d = 0.2$ s. With $N = 10$ the filter time constant is $T_f = 0.01$ s, so the filter pole is at 100 rad/s.

<details><summary>Verification</summary>

```verify
Kp = q(2, "")
Ti = q(0.5, "s")
Td = q(0.1, "s")
N = q(10, "")
expect(Kp / Ti, "4 1/s")
expect(Kp * Td, "0.2 s")
Tf = Td / N
expect(Tf, "0.01 s")
expect(1 / Tf, "100 rad/s")
```

</details>

## Lead and lag compensation

A **lead compensator** adds phase near the crossover frequency to raise the phase margin. A **lag compensator** raises the low-frequency gain, and so shrinks steady error, with little change in phase near crossover.

$$C_{\text{lead}}(s) = K_c\,\frac{1 + aTs}{1 + Ts},\ a > 1 \qquad \sin\phi_{\max} = \frac{a - 1}{a + 1} \qquad \omega_m = \frac{1}{T\sqrt{a}}$$

$$C_{\text{lag}}(s) = \frac{1 + Ts}{1 + bTs},\ b > 1$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $K_c$ | compensator gain | dimensionless |
| $a$, $b$ | lead and lag ratios | dimensionless |
| $T$ | time constant | s |
| $\phi_{\max}$ | maximum phase added by the lead | rad |
| $\omega_m$ | frequency of maximum phase, the geometric mean of the corners $1/(aT)$ and $1/T$ | rad/s |

Holds when: the plant is LTI and the compensator is a minimum-phase first-order lead or lag. For the lead, the gain at $\omega_m$ is $K_c\sqrt{a}$, so $K_c$ is chosen to place the new crossover at $\omega_m$. For the lag, the corner frequencies are placed at least a decade below the crossover so its phase lag there stays small, and the DC gain is raised by the factor $b$ relative to the high-frequency gain.
Breaks when: the plant has dead time or a right-half-plane zero (extra phase is then useless because the crossover cannot rise), noise limits the high-frequency gain (a lead raises gain by $a$ at high frequency), or more than about $65^\circ$ of lead is wanted from one stage (use two stages, since $a$ grows steeply).
Source and basis: derived from the phase and magnitude of the first-order factors; taught in [Feedback control](14-controls.md).

Example: $a = 10$, $T = 0.1$ s. The maximum phase added is $54.9^\circ$ at $\omega_m = 3.16$ rad/s, where the gain is $\sqrt{10} = 3.16$ times $K_c$.

<details><summary>Verification</summary>

```verify
a = q(10, "")
T = q(0.1, "s")
expect(asin((a - 1) / (a + 1)), "54.9 deg")
expect(1 / (T * sqrt(a)), "3.16 rad/s")
expect(sqrt(a), "3.16")
```

</details>

## State space

A **state-space model** describes a system by first-order equations in a state vector, which handles several inputs and outputs and internal variables directly.

$$\dot{\mathbf{x}} = \mathbf{A}\mathbf{x} + \mathbf{B}u \qquad y = \mathbf{C}\mathbf{x} + \mathbf{D}u \qquad G(s) = \mathbf{C}(s\mathbf{I} - \mathbf{A})^{-1}\mathbf{B} + \mathbf{D}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\mathbf{x}$ | state vector (units set by each state) | dimensionless |
| $u$, $y$ | input and output (scalar here) | dimensionless |
| $\mathbf{A}$, $\mathbf{B}$, $\mathbf{C}$, $\mathbf{D}$ | state, input, output, and feedthrough matrices | dimensionless |
| $\mathbf{I}$ | identity matrix | dimensionless |
| $s$ | Laplace variable | 1/s |

Holds when: the system is LTI and finite dimensional. The poles of $G(s)$ are eigenvalues of $\mathbf{A}$, and $\det(s\mathbf{I} - \mathbf{A})$ is the denominator. A realization is not unique; any invertible change of state $\mathbf{x} = \mathbf{T}\mathbf{z}$ gives another with the same $G(s)$. The controllable canonical form for $s^2 + a_1 s + a_0$ is $\mathbf{A} = \begin{bmatrix}0 & 1\\ -a_0 & -a_1\end{bmatrix}$, $\mathbf{B} = \begin{bmatrix}0\\ 1\end{bmatrix}$, $\mathbf{C} = \begin{bmatrix}1 & 0\end{bmatrix}$.
Breaks when: the system is nonlinear (linearize first), has a delay (infinite states), or the model is not minimal (a pole-zero cancellation then hides an uncontrollable or unobservable mode that $G(s)$ does not show).
Source and basis: derived from the Laplace transform of the state equations; taught in [Feedback control](14-controls.md).

Example: $\mathbf{A} = \begin{bmatrix}0 & 1\\ -4 & -2\end{bmatrix}$ has $\det(s\mathbf{I} - \mathbf{A}) = s^2 + 2s + 4$, since the coefficient of $s$ is minus the trace (2) and the constant is the determinant (4). This is $\omega_n = 2$ rad/s and $\zeta = 0.5$, the same system as in the margin example.

<details><summary>Verification</summary>

```verify
a11 = q(0, "")
a12 = q(1, "")
a21 = q(-4, "")
a22 = q(-2, "")
expect(-(a11 + a22), "2")
expect(a11 * a22 - a12 * a21, "4")
expect(sqrt(a11 * a22 - a12 * a21), "2")
expect(-(a11 + a22) / (2 * sqrt(a11 * a22 - a12 * a21)), "0.5")
```

</details>

### Pole placement by state feedback

State feedback $u = -\mathbf{K}\mathbf{x} + r$ moves the closed-loop poles to the roots of $\det(s\mathbf{I} - \mathbf{A} + \mathbf{B}\mathbf{K})$. In controllable canonical form of order two the gains read off directly.

$$s^2 + (a_1 + k_2)s + (a_0 + k_1) = s^2 + 2\zeta_d\omega_d s + \omega_d^2$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $a_1$ | open-loop coefficient of $s$ | 1/s |
| $a_0$ | open-loop constant coefficient | $1/\text{s}^{2}$ |
| $k_1$ | state-feedback gain on the first state | $1/\text{s}^{2}$ |
| $k_2$ | state-feedback gain on the second state | 1/s |
| $\zeta_d$ | desired damping ratio | dimensionless |
| $\omega_d$ | desired natural frequency | rad/s |

Holds when: the pair $(\mathbf{A}, \mathbf{B})$ is controllable, the model is accurate, all states are available (or estimated), and the form is the canonical one above (for other forms use a transform or Ackermann's formula).
Breaks when: the pair is not controllable (some poles cannot move), the poles are placed far faster than the plant (the actuator saturates and noise is amplified), or the model error moves the true poles. An observer that estimates the states has its own poles, usually placed faster than the regulator poles so estimation error dies out first; the limit is measurement noise.
Source and basis: derived from the characteristic polynomial of $\mathbf{A} - \mathbf{B}\mathbf{K}$; taught in [Feedback control](14-controls.md).

Example: for $s^2 + 2s + 4$ ($a_1 = 2$, $a_0 = 4$), the target $\zeta_d = 0.7$, $\omega_d = 5$ rad/s gives $s^2 + 7s + 25$. So $k_2 = 5$ 1/s and $k_1 = 21$ $1/\text{s}^2$.

<details><summary>Verification</summary>

```verify
zd = q(0.7, "")
wd = q(5, "rad/s")
a1 = q(2, "1/s")
a0 = q(4, "1/s^2")
expect(2 * zd * wd, "7 rad/s")
expect(wd**2, "25 1/s^2")
expect(2 * zd * wd - a1, "5 1/s")
expect(wd**2 - a0, "21 1/s^2")
```

</details>

### Controllability and observability

A system is **controllable** when some input can move the state from any value to any other in finite time, and **observable** when the state can be found from the output history.

$$\operatorname{rank}\begin{bmatrix}\mathbf{B} & \mathbf{A}\mathbf{B} & \cdots & \mathbf{A}^{n-1}\mathbf{B}\end{bmatrix} = n \qquad \operatorname{rank}\begin{bmatrix}\mathbf{C}\\ \mathbf{C}\mathbf{A}\\ \vdots \\ \mathbf{C}\mathbf{A}^{n-1}\end{bmatrix} = n$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $n$ | number of states | dimensionless |
| $\mathbf{A}$, $\mathbf{B}$, $\mathbf{C}$ | state, input, and output matrices | dimensionless |

Holds when: the system is LTI with $n$ states. Full rank of the first matrix is controllability and of the second is observability. Controllability is needed for arbitrary pole placement, and observability for an observer.
Breaks when: the matrices are nearly rank deficient (the rank test passes but the system is practically uncontrollable, because the entries differ by many orders of magnitude; check the singular values), or the system is nonlinear.
Source and basis: derived from the Cayley-Hamilton theorem applied to the state solution; taught in [Feedback control](14-controls.md).

Example: for the system above with $\mathbf{B} = [0\ \ 1]^T$, $\mathbf{A}\mathbf{B} = [1\ \ {-2}]^T$, so $\det[\mathbf{B}\ \mathbf{A}\mathbf{B}] = -1$ and the system is controllable. With $\mathbf{C} = [1\ \ 0]$, $\mathbf{C}\mathbf{A} = [0\ \ 1]$ and the observability matrix has determinant 1.

<details><summary>Verification</summary>

```verify
b1 = q(0, "")
b2 = q(1, "")
ab1 = q(0, "") * b1 + q(1, "") * b2
ab2 = q(-4, "") * b1 + q(-2, "") * b2
expect(b1 * ab2 - ab1 * b2, "-1")
c1 = q(1, "")
c2 = q(0, "")
ca1 = c1 * q(0, "") + c2 * q(-4, "")
ca2 = c1 * q(1, "") + c2 * q(-2, "")
expect(c1 * ca2 - c2 * ca1, "1")
```

</details>

## Sampled-data control

A **sampled-data** (digital) controller reads the output at instants $kT_s$, computes the input in a processor, and holds it constant between samples with a **zero-order hold (ZOH)**. The Laplace variable maps to the z variable by $z = e^{sT_s}$.

### Zero-order hold and the z map

$$z = e^{sT_s} \qquad G_{\text{zoh}}(s) = \frac{1 - e^{-sT_s}}{s} \qquad a = e^{-T_s/\tau}$$

For $G(s) = K/(\tau s + 1)$ preceded by a ZOH, the sampled plant is $G(z) = K(1 - a)/(z - a)$.

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $T_s$ | sample period | s |
| $z$ | z-transform variable | dimensionless |
| $s$ | Laplace variable | 1/s |
| $a$ | discrete pole of the sampled first-order plant | dimensionless |
| $K$ | DC gain of the plant | dimensionless |
| $\tau$ | time constant of the plant | s |

Holds when: the plant is LTI, the sampling is uniform, and the input is held constant between samples. A pole $s_p$ maps to $z_p = e^{s_pT_s}$, so the left half plane maps to the inside of the unit circle and the sampled system is stable exactly when every pole has $|z| < 1$. The ZOH adds an average delay of $T_s/2$.
Breaks when: the sampling is irregular or jittery, a signal has content above half the sampling rate (it aliases onto lower frequencies; an anti-aliasing filter ahead of the sampler is needed), or the plant has delay not a multiple of $T_s$ (use a modified z transform).
Source and basis: derived from the exact solution of the plant over one hold interval.

Example: $\tau = 0.5$ s and $T_s = 0.1$ s give $a = e^{-0.2} = 0.819$. The DC gain of the sampled plant is $K(1 - a)/(1 - a) = K$, as it should be.

<details><summary>Verification</summary>

```verify
tau = q(0.5, "s")
Ts = q(0.1, "s")
a = exp(-Ts / tau)
expect(a, "0.819")
expect((1 - a) / (1 - a), "1")
```

</details>

### Tustin transformation

The **Tustin (bilinear) transformation** converts a continuous controller to a discrete one by approximating $e^{sT_s}$ with a ratio of first-order terms.

$$s \to \frac{2}{T_s}\,\frac{z - 1}{z + 1} \qquad \omega_a = \frac{2}{T_s}\tan\frac{\omega_d T_s}{2}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $T_s$ | sample period | s |
| $\omega_a$ | analog frequency | rad/s |
| $\omega_d$ | digital frequency that the transformation places there | rad/s |

Holds when: the controller is LTI and stable (the map takes the left half plane exactly onto the unit disk, so stability is preserved). The frequency axis is warped, so $\omega_d$ and $\omega_a$ agree closely only when $\omega_d T_s$ is small. To match a critical frequency exactly, prewarp: pick the analog design frequency $\omega_a$ so that the digital filter has its feature at $\omega_d$.
Breaks when: the critical frequency approaches half the sampling rate (the warping becomes large), or the controller must match a continuous design in the time domain rather than the frequency domain.
Source and basis: derived from the trapezoidal-rule approximation of integration.

Example: $T_s = 0.02$ s and $\omega_d = 10$ rad/s. The analog frequency that maps there is $\omega_a = 10.03$ rad/s, a warp of 0.33 percent.

<details><summary>Verification</summary>

```verify
Ts = q(0.02, "s")
wd = q(10, "rad/s")
wa = 2 / Ts * tan(wd * Ts / 2)
expect(wa, "10.03 rad/s")
expect(100 * (wa / wd - 1), "0.33")
```

</details>

### Sampling-rate rule of thumb

The ZOH delays the signal by about $T_s/2$, so the phase lag at the crossover frequency $\omega_c$ is about $\omega_c T_s/2$. Limiting this lag to a budget $\phi_b$ sets a maximum sample period and a minimum sampling rate.

$$\frac{\omega_c T_s}{2} \le \phi_b \qquad \Rightarrow \qquad T_s \le \frac{2\phi_b}{\omega_c} \qquad \omega_s = \frac{2\pi}{T_s} \ge \frac{\pi\,\omega_c}{\phi_b}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\omega_c$ | gain crossover frequency | rad/s |
| $T_s$ | sample period | s |
| $\phi_b$ | phase-lag budget from sampling | rad |
| $\omega_s$ | sampling angular frequency | rad/s |

Holds when: the lag from sampling is small, so that $T_s/2$ is a good model of the hold, and the budget is a fraction of the phase margin. The basis is the delay estimate above. A budget of 0.1 rad (about $5.7^\circ$) gives $\omega_s \ge 31\,\omega_c$, so the usual advice to sample at 20 to 30 times the closed-loop bandwidth follows from a lag of roughly 0.1 to 0.16 rad. This is a rule of thumb, not a bound.
Breaks when: the margin is small (a smaller budget is needed), the controller is computed with a delay of its own (add it to the budget), or the sampling theorem is the constraint instead (any signal content above $\omega_s/2$ aliases, so $\omega_s$ must exceed twice the highest frequency present after filtering).
Source and basis: derived from the half-sample delay of the zero-order hold.

Example: $\omega_c = 10$ rad/s with a budget of 0.1 rad gives $T_s \le 0.02$ s, a rate of at least 50 Hz. At $T_s = 0.02$ s the lag at crossover is $5.73^\circ$.

<details><summary>Verification</summary>

```verify
wc = q(10, "rad/s")
pb = q(0.1, "rad")
Ts = 2 * pb / wc
expect(Ts, "0.02 s")
expect(1 / Ts, "50 Hz")
expect(wc * Ts / 2, "5.73 deg")
expect(pi / pb, "31")
```

</details>

## Saturation, delay, and nonlinear limits

Real actuators saturate, have rate limits, dead zones, and backlash, and real loops carry delay. A saturated loop is effectively open: loop gain falls as the signal grows, an integrator keeps accumulating (windup), and a loop that is stable for small signals can settle into a limit cycle or lose control for large ones. Anti-windup (see the PID entry) and a command-rate limiter address the first, but no linear margin guarantees large-signal stability. Test saturated step responses in simulation and on hardware.

### Delay and Pade approximation

A **pure delay** of $T_d$ seconds has transfer function $e^{-sT_d}$, which has unit magnitude and a phase lag that grows linearly with frequency. A first-order **Pade approximation** replaces it by a rational function so that the Routh test and the root locus can be used.

$$e^{-sT_d} \approx \frac{1 - sT_d/2}{1 + sT_d/2} \qquad \angle e^{-j\omega T_d} = -\omega T_d \qquad T_{\text{margin}} = \frac{\phi_m}{\omega_c}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $T_d$ | delay | s |
| $\omega$ | angular frequency | rad/s |
| $\phi_m$ | phase margin | rad |
| $\omega_c$ | gain crossover frequency | rad/s |
| $T_{\text{margin}}$ | delay margin, the extra delay that brings the loop to instability | s |

Holds when: the approximation is used for $\omega T_d \lesssim 1$. Its phase is $-2\arctan(\omega T_d/2)$, which tracks $-\omega T_d$ to within a few percent there. The delay margin holds when the loop has one crossover and is stable without the delay.
Breaks when: $\omega T_d$ is near or above 1 (use a higher-order Pade or the exact frequency response), or the loop has several crossovers (the delay margin is then the smallest over all of them). The approximation puts a right-half-plane zero at $2/T_d$, which is why a delay limits the crossover to well below $1/T_d$.
Source and basis: derived from the first-order [2/2] Pade expansion of the exponential and from the phase definition of the margin.

Example: $T_d = 0.05$ s at $\omega = 10$ rad/s loses 0.5 rad ($28.6^\circ$) exactly, and the Pade model gives 0.490 rad. The loop $L = 4/(s(s + 2))$ with $\phi_m = 0.905$ rad and $\omega_c = 1.572$ rad/s tolerates an extra delay of $0.575$ s before instability.

<details><summary>Verification</summary>

```verify
Td = q(0.05, "s")
w = q(10, "rad/s")
expect(w * Td, "0.5 rad")
expect(w * Td, "28.6 deg")
expect(2 * atan(w * Td / 2), "0.490 rad")
wc = sqrt(-2 + sqrt(4 + 4 * 4)) * q(1, "rad/s")
pm = pi / 2 - atan(wc / (2 * q(1, "rad/s")))
expect(pm, "0.905 rad")
expect(wc, "1.572 rad/s")
expect(pm / wc, "0.575 s")
```

</details>

## Checklists

Before trusting a model:

- Operating point, units, and sign of every gain stated.
- Linearization range stated and checked against the largest expected signal.
- Actuator limits, rate limits, and sensor noise and delay included or bounded.

Before trusting a stability result:

- Test applies to this system class (LTI, rational, or a delay handled explicitly).
- Open-loop right-half-plane poles counted for Nyquist.
- Routh special cases (zero entry, zero row) handled.
- Both gain margin and phase margin read, and the delay margin checked against the real delay.
- Margins checked at the plant extremes, not only at the nominal model.

Before building the controller:

- Integrator has anti-windup, derivative has a filter, and derivative acts on the measurement.
- Sampling rate set from the phase-lag budget and the sampling theorem.
- Saturated step and large-signal response simulated.
- Controllability and observability checked before pole placement or an observer.

## Sanity checks

- A first-order step reaches 0.632 of its final value at one time constant and 0.982 at four.
- A factor of 2 in magnitude is 6.02 dB and a factor of 10 is 20 dB.
- At a first-order corner frequency the magnitude is 3.01 dB below its low-frequency value and the phase is $-45^\circ$.
- An overshoot of 5 percent is a damping ratio of about 0.69; a phase margin of $60^\circ$ goes with about 0.6.
- Each integrator in the loop adds $-90^\circ$ and each pole above its corner frequency steepens the slope by 20 dB per decade.
- A loop with $n - m$ above 2 always goes unstable at high enough gain, since the asymptotes enter the right half plane.
- A sampled closed loop has poles inside the unit circle; a pole at $|z| = 1$ is marginal.

<details><summary>Verification</summary>

```verify
expect(1 - exp(-1), "0.632")
expect(1 - exp(-4), "0.982")
expect(20 * log10(2), "6.02")
expect(20 * log10(sqrt(2)), "3.01")
z = -log(0.05) / sqrt(pi**2 + log(0.05)**2)
expect(z, "0.69")
```

</details>

## Further reference

Named books and standards only (no links). Check current editions before relying on a value.

- Feedback Control of Dynamic Systems, Franklin, Powell, and Emami-Naeini (paid, classical and digital control in one text).
- Modern Control Engineering, Ogata (paid, root locus, frequency response, and state space).
- Control Systems Engineering, Nise (paid, a gentler route through the same topics).
- Feedback Systems: An Introduction for Scientists and Engineers, Astrom and Murray (the authors have made a free edition available from Caltech; see [Feedback control](14-controls.md) for the link).
- Digital Control of Dynamic Systems, Franklin, Powell, and Workman (paid, sampled-data design).
- Mechatronic systems in practice are covered in [Mechatronics](../applications/electronics/06-mechatronics.md) and [Mechatronic systems](../design/11-mechatronic-systems.md).
