# Vibrations

**Type:** lesson

Vibration is motion that repeats around an equilibrium position. Engineers care because almost every structure, machine and vehicle shakes, and a part that is driven near its natural frequency can grow large enough to crack or fail.

**Prerequisites:** [Particle dynamics](02-particle-dynamics.md), [Oscillations, waves, light, and heat](07-waves-light-heat.md), [Differential equations](../math/06-differential-equations.md) (solving $m x'' + c x' + k x = F$)
**Time:** 8-12 h

## Core ideas

- A **spring-mass system** is the simplest model. A mass $m$ sits on a spring of stiffness $k$. When the mass moves a distance $x$ from equilibrium, the spring pushes back with force $-kx$.
- **Free vibration** happens when nothing drives the system after the start. The mass oscillates at its **natural frequency**, which depends only on $m$ and $k$.
- **Damping** removes energy. A **damper** (often a dashpot, a piston in oil) adds a force proportional to velocity, $-c\dot{x}$. Real structures always have some damping, even if it is small.
- **Forced vibration** happens when an outside force drives the system. A steady harmonic force at frequency $\omega$ produces a steady response at the same frequency.
- **Resonance** is the large response that appears when the driving frequency is close to the natural frequency. Damping limits how large the response gets.
- The **damping ratio** $\zeta$ (zeta) is a dimensionless number that tells you how strongly a system is damped.
- A system with $\zeta < 1$ is **underdamped** and rings. $\zeta = 1$ is **critically damped** and returns to rest fastest without overshoot. $\zeta > 1$ is **overdamped** and creeps back slowly.

The equation of motion for a damped, forced spring-mass system is

$$m\ddot{x} + c\dot{x} + kx = F(t)$$

where $x$ is displacement (m), $\dot{x}$ is velocity (m/s), $\ddot{x}$ is acceleration ($\mathrm{m/s^2}$), $m$ is mass (kg), $c$ is damping coefficient ($\mathrm{N\cdot s/m}$), $k$ is stiffness (N/m), and $F(t)$ is the applied force (N).

## Key equations

Natural (undamped) angular frequency and cyclic frequency:

$$\omega_n = \sqrt{\frac{k}{m}} \qquad f_n = \frac{\omega_n}{2\pi}$$

Units: $\omega_n$ in rad/s, $f_n$ in Hz (1/s).

Damping ratio:

$$\zeta = \frac{c}{2\sqrt{km}} = \frac{c}{c_{\mathrm{cr}}}, \qquad c_{\mathrm{cr}} = 2\sqrt{km}$$

Units: $c_{\mathrm{cr}}$ is the critical damping coefficient ($\mathrm{N\cdot s/m}$). $\zeta$ has no units.

Damped natural frequency (only meaningful when $\zeta < 1$):

$$\omega_d = \omega_n\sqrt{1-\zeta^2}$$

Steady-state forced response for harmonic force $F(t) = F_0\cos(\omega t)$, with static deflection $X_0 = F_0/k$ (m):

$$X = \frac{X_0}{\sqrt{\left(1-r^2\right)^2 + \left(2\zeta r\right)^2}}, \qquad r = \frac{\omega}{\omega_n}$$

Here $X$ is the steady amplitude (m) and $r$ is the frequency ratio (dimensionless). The **magnification factor** is $M = X/X_0$.

At resonance ($r = 1$), $M = 1/(2\zeta)$. The exact peak of the amplitude curve for lightly damped systems is at $r = \sqrt{1-2\zeta^2}$, with peak magnification

$$M_{\mathrm{peak}} = \frac{1}{2\zeta\sqrt{1-\zeta^2}}$$

Logarithmic decrement (for free decay of an underdamped system), the natural log of the ratio of successive peak amplitudes:

$$\delta = \frac{2\pi\zeta}{\sqrt{1-\zeta^2}}$$

A lightly damped structure has $\zeta$ much less than 1. The worked example below uses $\zeta = 0.10$.

## Worked example

**Problem.** A machine mount is modeled as a 2.0 kg mass on a spring with $k = 800$ N/m and a damper with $c = 8.0$ $\mathrm{N\cdot s/m}$. A steady harmonic force of amplitude $F_0 = 5.0$ N drives the mass at frequency $\omega = \omega_n$. Find the natural frequency, damping ratio, damped frequency, and the steady amplitude at this driving frequency. Also find the peak amplitude over all driving frequencies.

**Given.** $m = 2.0$ kg, $k = 800$ N/m, $c = 8.0$ $\mathrm{N\cdot s/m}$, $F_0 = 5.0$ N.

**Find.** $\omega_n$, $f_n$, $\zeta$, $\omega_d$, $X$ at $r = 1$, and the peak amplitude.

**Assumptions.** Linear spring and linear viscous damper. Steady state only (transients have died out). Small motions.

**Solution.**

1. Natural angular frequency: $\omega_n = \sqrt{800/2.0} = \sqrt{400} = 20.0$ rad/s.
2. Natural frequency: $f_n = 20.0/(2\pi) = 3.183$ Hz.
3. Critical damping: $c_{\mathrm{cr}} = 2\sqrt{800 \cdot 2.0} = 80$ $\mathrm{N\cdot s/m}$.
4. Damping ratio: $\zeta = 8.0/80 = 0.10$.
5. Damped frequency: $\omega_d = 20.0\sqrt{1-0.1^2} = 19.90$ rad/s.
6. Static deflection: $X_0 = 5.0/800 = 6.25$ mm.
7. At $r = 1$, $M = 1/(2 \cdot 0.10) = 5.0$, so $X = 5.0 \cdot 6.25\ \text{mm} = 31.25$ mm.
8. Exact peak: $M_{\mathrm{peak}} = 1/(2 \cdot 0.10 \cdot \sqrt{0.99}) = 5.025$. Peak amplitude $X_{\mathrm{peak}} = 5.025 \cdot 6.25 = 31.41$ mm, at $r = \sqrt{0.98} = 0.990$.

**Answer.**

- $\omega_n = 20.0$ rad/s, $f_n = 3.18$ Hz
- $\zeta = 0.10$ (underdamped)
- $\omega_d = 19.9$ rad/s
- $X(r=1) = 31.3$ mm
- Peak amplitude about $31.4$ mm, very close to the value at resonance.

**Sanity check.** The static deflection is only 6.25 mm, and the response is about five times larger at resonance. That matches $M \approx 1/(2\zeta)$. A lightly damped system near resonance gives a large response, which is the reason to keep driving frequencies away from $f_n$ or add damping.

## Practice

1. A 4.0 kg mass sits on a spring with $k = 1000$ N/m, with no damping. Find $f_n$ in Hz.
2. The same mass and spring now have $c = 20$ $\mathrm{N\cdot s/m}$. Find $\zeta$.
3. A static force of 50 N is applied to the spring from problem 1. Find the static deflection in mm.
4. For the system in problem 2, find $\omega_d$ in rad/s.
5. Find the exact peak magnification $M_{\mathrm{peak}}$ for a system with $\zeta = 0.05$.

<details><summary>Answers</summary>

1. 2.52 Hz
2. 0.158
3. 50 mm
4. 15.6 rad/s
5. 10.01

</details>

## Common mistakes

- Mixing up $f$ (Hz) and $\omega$ (rad/s). Frequency in the formulas for $\omega_n$ and $r$ must be in rad/s. Divide by $2\pi$ only when you need Hz.
- Forgetting the square root in $\zeta = c/(2\sqrt{km})$. Using $c/(2km)$ gives the wrong units and the wrong value.
- Using $\omega_d$ for an overdamped system. It has no real meaning when $\zeta \ge 1$.
- Treating the resonance peak as exactly $1/(2\zeta)$. That is a good estimate at light damping, but the exact peak, $1/(2\zeta\sqrt{1-\zeta^2})$, is slightly higher and at a slightly different frequency.
- Using the steady-state formula before transients have decayed. Start-up motion includes a free-vibration part that dies out over time.

## Go deeper

- [MIT OpenCourseWare 2.003SC Engineering Dynamics (Fall 2011)](https://ocw.mit.edu/courses/2-003sc-engineering-dynamics-fall-2011/) by MIT: a free course with a unit on mechanical vibration, multi-degree-of-freedom systems and mode superposition. Use it for the next level after this lesson.
- [MIT OpenCourseWare 2.003SC, course pages](https://ocw.mit.edu/courses/2-003sc-engineering-dynamics-fall-2011/pages/) by MIT: lists the vibration units (mechanical vibration, multi-DOF vibration, mode superposition) as a study map.
- [Mechanics reference](reference-mechanics.md): the lookup sheet for this topic.
