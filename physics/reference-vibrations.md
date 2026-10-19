# Vibrations reference

**Type:** reference
**Verify:** strict

Lookup sheet for the free and forced vibration of springs, masses, and dampers, from one degree of freedom to continuous beams, strings, and rotors, for an engineer who needs a natural frequency, a response amplitude, or an isolation check in the middle of a job.

## Principles

- A **vibration** is motion that repeats about an equilibrium. Every elastic body with mass has natural frequencies, and a force near one of them produces a response far larger than the static one.
- Natural frequency comes from the ratio of stiffness to mass. Doubling stiffness raises it by a factor of $\sqrt{2}$, and doubling mass lowers it by the same factor.
- Damping sets the height of the resonance peak and the decay rate of free motion. It barely changes the natural frequency of a lightly damped system.
- A system with $n$ degrees of freedom has $n$ natural frequencies and $n$ mode shapes. A continuous body has infinitely many.
- For a linear system, modes are independent. A response is a sum of modal responses, each behaving as a single-degree-of-freedom oscillator.
- Frequency in the formulas is in rad/s. Convert to Hz or rev/min only to read or report a number.
- Isolation works only when the disturbance frequency is above $\sqrt{2}$ times the natural frequency of the isolated mass. Below that, a soft mount amplifies.
- Adding a mass or a stiffener moves a natural frequency but does not remove it. Check where the new one lands against every excitation.
- Rayleigh's method gives an upper bound on the first natural frequency. A guessed mode shape can only add constraint, never remove it.
- All formulas here are linear and small-motion. Large amplitude, dry friction, clearances, and cracked or loosening joints break them.

## Single-degree-of-freedom free response

### Natural frequency, damping ratio, and damped response

A **single-degree-of-freedom (SDOF)** system is a mass that moves along one coordinate $x$ against a spring and a viscous damper. Its free motion, with no applied force, sets the natural frequency and damping ratio used everywhere else in this sheet.

$$m\ddot{x} + c\dot{x} + kx = 0 \qquad \omega_n = \sqrt{\frac{k}{m}} \qquad \zeta = \frac{c}{2\sqrt{km}} \qquad \omega_d = \omega_n\sqrt{1-\zeta^2}$$

$$x(t) = X e^{-\zeta\omega_n t}\cos(\omega_d t - \phi) \qquad (\zeta < 1)$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $m$ | mass | kg |
| $c$ | viscous damping coefficient | N s/m |
| $k$ | spring stiffness | N/m |
| $x$ | displacement from equilibrium | m |
| $X$ | free-response amplitude, set by the initial displacement and velocity | m |
| $\phi$ | free-response phase | rad |
| $t$ | time | s |
| $\omega_n$, $\omega_d$ | natural and damped angular frequency | rad/s |
| $\zeta$ | damping ratio | dimensionless |

The three regimes depend only on $\zeta$.

| Regime | $\zeta$ | Free motion |
|---|---|---|
| Underdamped | below 1 | decaying oscillation at $\omega_d$, envelope $e^{-\zeta\omega_n t}$ |
| Critically damped | exactly 1 | fastest return to rest with no oscillation, $c_{cr} = 2\sqrt{km}$ |
| Overdamped | above 1 | two real decaying exponentials, roots $s = -\omega_n\left(\zeta \pm \sqrt{\zeta^2 - 1}\right)$ |

Example. A 5 kg mass on a 2000 N/m spring with a 40 N s/m damper has $\omega_n = 20$ rad/s, $f_n = \omega_n/2\pi = 3.183$ Hz, $c_{cr} = 200$ N s/m, $\zeta = 0.2$, and $\omega_d = 19.60$ rad/s. The amplitude envelope decays with time constant $1/(\zeta\omega_n) = 0.25$ s. Overdamped, with $\zeta = 2$ and the same $\omega_n$, the roots are $-74.64$ rad/s and $-5.359$ rad/s, and the slow root sets the return time.

Holds when: the spring and damper are linear, mass is constant, the motion is small, and damping is viscous (force proportional to velocity).
Breaks when: dry friction (the decay is linear, not exponential), a nonlinear or clearance spring (frequency depends on amplitude), or high damping where the system is a lag, not an oscillator.
Source and basis: derived from Newton's second law and the characteristic equation of the linear ordinary differential equation; taught in [Vibrations](13-vibrations.md).

<details><summary>Verification</summary>

```verify
m = q(5, "kg")
k = q(2000, "N/m")
c = q(40, "N s/m")
wn = sqrt(k / m)
expect(wn, "20 rad/s")
expect(wn / (2 * pi), "3.183 Hz")
expect(2 * sqrt(k * m), "200 N s/m")
z = c / (2 * sqrt(k * m))
expect(z, "0.2")
expect(wn * sqrt(1 - z**2), "19.60 rad/s")
expect(1 / (z * wn), "0.25 s")
z2 = q(2, "")
expect(-wn * (z2 + sqrt(z2**2 - 1)), "-74.64 rad/s")
expect(-wn * (z2 - sqrt(z2**2 - 1)), "-5.359 rad/s")
```

</details>

## Equivalent stiffness and mass

### Springs, beams, and shafts as stiffness elements

An **equivalent stiffness** is the single spring constant that replaces a combination of elastic members seen at one point and along one direction. Combine elements first, then use $\omega_n = \sqrt{k/m}$.

$$k_{par} = \sum_i k_i \qquad \frac{1}{k_{ser}} = \sum_i \frac{1}{k_i}$$

Springs that share one displacement (side by side) add. Springs that carry one force (end to end) add as reciprocals, so the series result is always softer than the softest element.

Stiffness at the point of load of common members (the load and the displacement are measured at that point):

| Member and load | Stiffness | Unit |
|---|---|---|
| Axial bar, length $L$ | $EA/L$ | N/m |
| Cantilever, end force | $3EI/L^{3}$ | N/m |
| Simply supported beam, centre force | $48EI/L^{3}$ | N/m |
| Fixed-fixed beam, centre force | $192EI/L^{3}$ | N/m |
| Circular shaft in torsion | $GJ/L$ | N m/rad |

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $k_i$, $k_{par}$, $k_{ser}$ | stiffness of element $i$, and of the parallel and series combinations | N/m |
| $E$, $G$ | Young's modulus, shear modulus | Pa |
| $A$ | cross-section area | $\text{m}^{2}$ |
| $I_A$ | second moment of area of the cross section | $\text{m}^{4}$ |
| $J$ | polar second moment of area | $\text{m}^{4}$ |
| $L$ | length | m |

Example. A steel cantilever 0.5 m long with a rectangular section 40 mm wide and 6 mm thick has $I_A = bh^{3}/12 = 7.2\times10^{-10}$ $\text{m}^{4}$. With $E = 200$ GPa its tip stiffness is $3EI_A/L^{3} = 3456$ N/m. A 2 kg tip mass gives $\omega_n = 41.57$ rad/s, or 6.616 Hz. Springs of 2000 and 3000 N/m give 5000 N/m in parallel and 1200 N/m in series.

Holds when: the members are linear elastic, slender (shear deformation small), and the supports are rigid.
Breaks when: supports are flexible (add their compliance in series), the beam is short and deep (add shear deflection), or the load point differs from the one tabulated.
Source and basis: derived from beam theory and Hooke's law; stiffness of members is taught in [Beam bending](05-bending-and-buckling.md) and [Axial and torsion](04-axial-and-torsion.md).

<details><summary>Verification</summary>

```verify
b = q(40, "mm")
h = q(6, "mm")
L = q(0.5, "m")
E = q(200, "GPa")
given("12")
Ia = b * h**3 / 12
expect(Ia, "7.2e-10 m^4")
kt = 3 * E * Ia / L**3
expect(kt, "3456 N/m")
expect(sqrt(kt / q(2, "kg")), "41.57 rad/s")
expect(sqrt(kt / q(2, "kg")) / (2 * pi), "6.616 Hz")
ka = q(2000, "N/m")
kb = q(3000, "N/m")
expect(ka + kb, "5000 N/m")
expect(1 / (1 / ka + 1 / kb), "1200 N/m")
```

</details>

### Rayleigh's method and spring mass

**Rayleigh's method** estimates a natural frequency by equating peak kinetic energy to peak strain energy for an assumed mode shape. A shape close to the true mode gives a close frequency, and any shape gives a value at or above the true first frequency.

$$\omega^{2} \approx \frac{\int EI_A\,(y'')^{2}\,dx}{\int \rho A\, y^{2}\,dx} \qquad m_{eff} = m + \frac{m_s}{3} \qquad m_{eff} = m + \frac{33}{140}\,m_b$$

The second form adds a third of the spring mass $m_s$ to a mass $m$ hanging on a helical spring. The third form adds $33/140$ of the beam mass $m_b$ to a tip mass $m$ on a cantilever, using the static deflected shape of the cantilever.

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\omega$ | estimated natural angular frequency | rad/s |
| $y(x)$ | assumed mode shape (displacement along the beam) | m |
| $y''$ | second derivative of the shape with respect to $x$ | 1/m |
| $x$ | position along the beam | m |
| $E$ | Young's modulus | Pa |
| $I_A$ | second moment of area | $\text{m}^{4}$ |
| $\rho A$ | mass per unit length | kg/m |
| $m_{eff}$ | effective mass at the mass point | kg |
| $m$ | lumped (tip or hanging) mass | kg |
| $m_s$, $m_b$ | spring mass, beam mass | kg |

Example. A 5 kg mass hangs on a 2000 N/m spring of mass 0.6 kg. Then $m_{eff} = 5.2$ kg and $\omega = \sqrt{k/m_{eff}} = 19.61$ rad/s, against 20 rad/s with the spring mass ignored.

Holds when: the assumed shape meets the geometric boundary conditions (it need not meet the force conditions), and the member is linear elastic.
Breaks when: the shape is poor (the error is first order in the shape error, but the frequency error is second order), or for higher modes, where the quotient is not a bound.
Source and basis: derived from conservation of energy for a harmonic motion, with a shape function; see [Vibrations](13-vibrations.md) for the lumped model.

<details><summary>Verification</summary>

```verify
k = q(2000, "N/m")
m = q(5, "kg")
ms = q(0.6, "kg")
meff = m + ms / 3
expect(meff, "5.2 kg")
expect(sqrt(k / meff), "19.61 rad/s")
expect(sqrt(k / m), "20 rad/s")
check(sqrt(k / meff) < sqrt(k / m), "spring mass lowers the frequency")
```

</details>

## Harmonic forcing

### Magnification factor, phase, resonance peak, and quality factor

Under a steady harmonic force $F_0\cos\omega t$ an SDOF system settles into motion at the forcing frequency. The **magnification factor** $M$ is the ratio of the steady amplitude to the static deflection $F_0/k$.

$$M = \frac{X}{X_0} = \frac{1}{\sqrt{(1-r^{2})^{2} + (2\zeta r)^{2}}} \qquad \tan\phi = \frac{2\zeta r}{1 - r^{2}} \qquad r = \frac{\omega}{\omega_n}$$

$$r_{pk} = \sqrt{1-2\zeta^{2}} \qquad M_{pk} = \frac{1}{2\zeta\sqrt{1-\zeta^{2}}} \qquad Q = \frac{1}{2\zeta}$$

The **quality factor** $Q$ is the response at $r = 1$ divided by the static response. The response lags the force by $\phi$, which rises from 0 at low $r$ through $\pi/2$ at $r = 1$ toward $\pi$ at high $r$. The peak exists only for $\zeta < 1/\sqrt{2}$.

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $X$ | steady-state amplitude (peak) | m |
| $X_0$ | static deflection $F_0/k$ | m |
| $F_0$ | force amplitude (peak) | N |
| $M$, $M_{pk}$ | magnification factor, and its peak over $r$ | dimensionless |
| $r$, $r_{pk}$ | frequency ratio, and the ratio at the amplitude peak | dimensionless |
| $\phi$ | phase lag of displacement behind force | rad |
| $\omega$ | forcing angular frequency | rad/s |
| $\zeta$ | damping ratio | dimensionless |
| $Q$ | quality factor | dimensionless |

Example. With $\zeta = 0.05$ and $r = 0.9$, $M = 4.757$ and $\phi = 0.4424$ rad. The exact peak is at $r_{pk} = 0.9975$ with $M_{pk} = 10.01$, and $Q = 10$. For $F_0 = 100$ N and $k = 5000$ N/m, $X_0 = 20$ mm and the amplitude at $r = 0.9$ is $4.757 \times 20 = 95.13$ mm.

Holds when: the force is harmonic at one frequency, damping is viscous and linear, and transients have died out.
Breaks when: the force has several frequencies (add the modal responses), damping is hysteretic or dry friction (the peak and phase shapes differ), or the structure is nonlinear and amplitude changes the frequency.
Source and basis: derived from the steady-state solution of the linear ordinary differential equation with a complex amplitude; taught in [Vibrations](13-vibrations.md).

<details><summary>Verification</summary>

```verify
z = q(0.05, "")
r = q(0.9, "")
M = 1 / sqrt((1 - r**2)**2 + (2 * z * r)**2)
expect(M, "4.757")
expect(atan(2 * z * r / (1 - r**2)), "0.4424 rad")
expect(sqrt(1 - 2 * z**2), "0.9975")
expect(1 / (2 * z * sqrt(1 - z**2)), "10.01")
expect(1 / (2 * z), "10")
X0 = q(100, "N") / q(5000, "N/m")
expect(X0, "20 mm")
expect(M * X0, "95.13 mm")
```

</details>

## Base excitation and isolation

### Transmissibility and relative motion

A **base excitation** moves the support of the mass, $y = Y\cos\omega t$, instead of applying a force to the mass. **Transmissibility** $TR$ is the ratio of the absolute amplitude of the mass to the amplitude of the base, and it also equals the ratio of the force transmitted to the support to the force applied to a mass on a fixed support.

$$TR = \frac{X}{Y} = \sqrt{\frac{1 + (2\zeta r)^{2}}{(1 - r^{2})^{2} + (2\zeta r)^{2}}} \qquad \frac{Z}{Y} = \frac{r^{2}}{\sqrt{(1-r^{2})^{2} + (2\zeta r)^{2}}}$$

Here $Z$ is the amplitude of the relative motion $x - y$ across the spring and damper. All curves of $TR$ pass through $TR = 1$ at $r = \sqrt{2}$. For $r > \sqrt{2}$ the mass moves less than the base, and more damping raises $TR$ there. Below $\sqrt{2}$ more damping lowers $TR$.

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $TR$ | transmissibility | dimensionless |
| $X$ | amplitude of the absolute motion of the mass | m |
| $Y$ | amplitude of the base motion | m |
| $Z$ | amplitude of the relative motion $x - y$ | m |
| $r$ | frequency ratio $\omega/\omega_n$ | dimensionless |
| $\zeta$ | damping ratio | dimensionless |

Example. With $\zeta = 0.1$ the amplitude ratio is $TR = 0.3559$ at $r = 2$, so a 1 mm base motion moves the mass 0.3559 mm. At $r = 1.5$ the relative motion is $Z/Y = 1.750$.

Holds when: the base motion is harmonic and the isolator is a linear spring and viscous damper, with a rigid base and mass.
Breaks when: the mount has internal resonances (surge in springs at high frequency stiffens the path), the mass is flexible, the base is not rigid (the effective $TR$ is higher), or motion is rocking and coupled.
Source and basis: derived from Newton's second law for a mass on a moving base, solved for harmonic motion; taught in [Vibrations](13-vibrations.md).

<details><summary>Verification</summary>

```verify
z = q(0.1, "")
r = q(2, "")
expect(sqrt((1 + (2 * z * r)**2) / ((1 - r**2)**2 + (2 * z * r)**2)), "0.3559")
r2 = q(1.5, "")
expect(r2**2 / sqrt((1 - r2**2)**2 + (2 * z * r2)**2), "1.750")
rs = sqrt(q(2, ""))
expect(sqrt((1 + (2 * z * rs)**2) / ((1 - rs**2)**2 + (2 * z * rs)**2)), "1")
```

</details>

## Rotating imbalance

### Response to an unbalanced rotor

An **imbalance** is a mass $m_e$ at radius $e$ from the rotation axis on a machine of total mass $M_T$ that can move along one line. The centrifugal force on the support grows with $\omega^{2}$.

$$F_0 = m_e e\,\omega^{2} \qquad \frac{M_T X}{m_e e} = \frac{r^{2}}{\sqrt{(1-r^{2})^{2} + (2\zeta r)^{2}}} \qquad F_T = m_e e\,\omega^{2}\,TR$$

The right-hand ratio tends to 1 at high $r$, so the machine mass moves by $m_e e/M_T$ (it spins about its centre of mass). It is zero at $r = 0$ and peaks near $r = 1$ at about $1/(2\zeta)$.

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $m_e$ | unbalance mass | kg |
| $e$ | radius (eccentricity) of the unbalance | m |
| $m_e e$ | unbalance | kg m |
| $M_T$ | total mass of the machine, including the unbalance | kg |
| $F_0$ | amplitude of the rotating force along the line of motion | N |
| $X$ | steady vibration amplitude | m |
| $F_T$ | amplitude of the force transmitted to the support | N |
| $TR$ | transmissibility of the mount | dimensionless |
| $\omega$ | rotation rate | rad/s |
| $r$, $\zeta$ | frequency ratio and damping ratio of the mounted machine | dimensionless |

Example. A 50 kg machine with unbalance $m_e e = 0.02$ kg m and $\zeta = 0.1$ runs at $r = 2$. The ratio is 1.322, so $X = 0.02/50 \times 1.322 = 0.5287$ mm.

Holds when: the rotor speed is steady, the unbalance is a point mass, and the support allows one translation.
Breaks when: the rotor is flexible (add the rotor critical speed), the support is anisotropic (two directions with different frequencies), or the machine speeds up through resonance in less than the time the response needs to build.
Source and basis: derived from the harmonic-force solution with force $m_e e\,\omega^{2}$; taught in [Vibrations](13-vibrations.md).

<details><summary>Verification</summary>

```verify
z = q(0.1, "")
r = q(2, "")
ratio = r**2 / sqrt((1 - r**2)**2 + (2 * z * r)**2)
expect(ratio, "1.322")
me = q(0.02, "kg m")
MT = q(50, "kg")
expect(me / MT * ratio, "0.5287 mm")
```

</details>

## Transmissibility and isolator selection

### Choosing a natural frequency for a required isolation

**Isolator selection** sets the mount stiffness so that the natural frequency sits well below the disturbance frequency. For an undamped mount the transmissibility reduces to $TR = 1/(r^{2}-1)$, which inverts to the frequency ratio needed for a target $TR$. The static deflection of the mount under weight fixes the natural frequency.

$$r = \sqrt{1 + \frac{1}{TR}} \qquad f_n = \frac{f_d}{r} \qquad k = m\,(2\pi f_n)^{2} \qquad \delta_{st} = \frac{m g}{k} = \frac{g}{\omega_n^{2}}$$

The isolation efficiency is $1 - TR$. Damping raises transmissibility above the undamped target. At the example's $r = 3.317$, damping ratios $\zeta = 0.05$, $0.10$, and $0.15$ give $TR = 0.105$, $0.120$, and $0.140$, respectively; at $\zeta = 0.15$, the target is missed by 40 percent.

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $TR$ | target transmissibility, undamped | dimensionless |
| $r$ | required frequency ratio $f_d/f_n$ | dimensionless |
| $f_d$ | disturbance frequency | Hz |
| $f_n$ | natural frequency of the mounted mass | Hz |
| $k$ | total stiffness of the mounts, in the direction of isolation | N/m |
| $m$ | supported mass | kg |
| $g$ | local gravitational acceleration | $\text{m/s}^{2}$ |
| $\delta_{st}$ | static deflection of the mount under weight | m |
| $\omega_n$ | natural angular frequency | rad/s |

Example. A 200 kg machine with a 25 Hz disturbance needs $TR = 0.1$. Then $r = 3.317$, $f_n = 7.538$ Hz, and $k = 448.6$ kN/m. The static deflection on Earth (standard gravity, $g = 9.80665$ $\text{m/s}^{2}$) is 4.372 mm.

Holds when: the mount is linear, loaded in its design direction, and the disturbance is a single dominant frequency well above $f_n$; the design equation assumes an undamped mount, so with damping $\zeta$ check $TR$ with the damped formula in [Transmissibility and relative motion](#transmissibility-and-relative-motion) and raise $r$ if needed.
Breaks when: the disturbance lies below $\sqrt{2}\,f_n$ or sweeps through resonance (a soft mount amplifies), the base is flexible, the mount has internal resonance, or rocking modes couple with the vertical mode.
Source and basis: derived from the undamped limit of transmissibility and static equilibrium of the mount; the gravity value is a standard convention in [constants](../data/constants.md).

<details><summary>Verification</summary>

```verify
TR = q(0.1, "")
r = sqrt(1 + 1 / TR)
expect(r, "3.317")
fd = q(25, "Hz")
fn = fd / r
expect(fn, "7.538 Hz")
m = q(200, "kg")
wn = 2 * pi * fn
k = m * wn**2
expect(k, "448.6 kN/m")
g = q(9.80665, "m/s^2", of="g_standard")
expect(g / wn**2, "4.372 mm")
z05 = q(0.05, "")
z10 = q(0.10, "")
z15 = q(0.15, "")
expect(sqrt((1 + (2 * z05 * r)**2) / ((1 - r**2)**2 + (2 * z05 * r)**2)), "0.105")
expect(sqrt((1 + (2 * z10 * r)**2) / ((1 - r**2)**2 + (2 * z10 * r)**2)), "0.120")
tr15 = sqrt((1 + (2 * z15 * r)**2) / ((1 - r**2)**2 + (2 * z15 * r)**2))
expect(tr15, "0.140")
expect((tr15 / TR - 1) * 100, "40")
check(abs(1 / (r**2 - 1) - TR) < 1e-9, "undamped transmissibility closes")
```

</details>

## Multi-degree-of-freedom equations

### Mass, damping, and stiffness matrices

A **multi-degree-of-freedom (MDOF)** model uses $n$ coordinates collected in a vector, with one equation of motion per coordinate. The mass, damping, and stiffness matrices hold the inertia and the elastic and dissipative coupling.

$$\mathbf{M}\ddot{\mathbf{x}} + \mathbf{C}\dot{\mathbf{x}} + \mathbf{K}\mathbf{x} = \mathbf{f}(t)$$

For a chain of two masses joined wall to $m_1$ by $k_1$ and $m_1$ to $m_2$ by $k_2$:

$$\mathbf{M} = \begin{bmatrix} m_1 & 0 \\ 0 & m_2 \end{bmatrix} \qquad \mathbf{K} = \begin{bmatrix} k_1 + k_2 & -k_2 \\ -k_2 & k_2 \end{bmatrix}$$

Both matrices are symmetric. $\mathbf{M}$ is positive definite, and $\mathbf{K}$ is positive definite when the body is fully restrained. A free, unrestrained body has a singular $\mathbf{K}$ and rigid-body modes of zero frequency.

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\mathbf{M}$ | mass matrix | kg |
| $\mathbf{C}$ | viscous damping matrix | N s/m |
| $\mathbf{K}$ | stiffness matrix | N/m |
| $\mathbf{x}$ | vector of displacements | m |
| $\mathbf{f}$ | vector of applied forces | N |
| $m_1$, $m_2$ | masses | kg |
| $k_1$, $k_2$ | spring stiffnesses | N/m |

Example. With $k_1 = 2000$ N/m and $k_2 = 1000$ N/m, $K_{11} = 3000$ N/m, $K_{12} = -1000$ N/m, $K_{22} = 1000$ N/m, and $\det\mathbf{K} = 2\times10^{6}$ $\text{N}^{2}/\text{m}^{2}$, which is positive, so the chain is restrained.

Holds when: the system is linear, the coordinates are small motions about equilibrium, and gyroscopic and follower forces are absent.
Breaks when: the system has gyroscopic or circulatory terms (the matrices are not symmetric, and the modes are complex), or when large rotations make the matrices depend on $\mathbf{x}$.
Source and basis: derived from Newton's second law written for each coordinate; matrix methods are treated in [Linear algebra and differential equations](../math/reference-linear-algebra-differential-equations.md).

<details><summary>Verification</summary>

```verify
k1 = q(2000, "N/m")
k2 = q(1000, "N/m")
K11 = k1 + k2
K12 = -k2
K22 = k2
expect(K11, "3000 N/m")
expect(K12, "-1000 N/m")
expect(K22, "1000 N/m")
expect(K11 * K22 - K12**2, "2e6 N^2/m^2")
```

</details>

## Eigenproblems and mode shapes

### Two-degree-of-freedom closed form, mass normalization, and orthogonality

A **natural mode** is a pattern of motion in which every coordinate moves in phase at one frequency. The frequencies and shapes come from the **eigenproblem** of free, undamped motion, $\mathbf{x} = \boldsymbol{\phi}\cos\omega t$.

$$\left(\mathbf{K} - \omega^{2}\mathbf{M}\right)\boldsymbol{\phi} = \mathbf{0} \qquad \det\left(\mathbf{K} - \omega^{2}\mathbf{M}\right) = 0$$

For two degrees of freedom with a diagonal $\mathbf{M}$ the determinant is a quadratic in $\omega^{2}$.

$$m_1 m_2\,\omega^{4} - \left(m_1 K_{22} + m_2 K_{11}\right)\omega^{2} + \det\mathbf{K} = 0 \qquad \omega^{2} = \frac{B \pm \sqrt{B^{2} - 4 m_1 m_2 \det\mathbf{K}}}{2 m_1 m_2}$$

Here $B = m_1 K_{22} + m_2 K_{11}$. The shape ratio follows from row 1: $\phi_2/\phi_1 = (K_{11} - \omega^{2} m_1)/(-K_{12})$.

Mode shapes of different frequencies are orthogonal through both matrices, and a shape is **mass normalized** when its modal mass is 1 kg.

$$\boldsymbol{\phi}_i^{\mathsf{T}}\mathbf{M}\boldsymbol{\phi}_j = \delta_{ij} \qquad \boldsymbol{\phi}_i^{\mathsf{T}}\mathbf{K}\boldsymbol{\phi}_j = \omega_i^{2}\,\delta_{ij}$$

Here $\delta_{ij}$ is 1 when $i = j$ and 0 otherwise. A shape is only a direction, so any multiple of it is a valid shape until it is normalized.

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\omega$, $\omega_i$ | natural angular frequency, and that of mode $i$ | rad/s |
| $\boldsymbol{\phi}$, $\boldsymbol{\phi}_i$ | mode shape vector (modal vector), scaled to the stated normalization | dimensionless |
| $\phi_1$, $\phi_2$ | components of the shape on coordinates 1 and 2 | dimensionless |
| $\mathbf{M}$ | mass matrix | kg |
| $\mathbf{K}$ | stiffness matrix | N/m |
| $m_1$, $m_2$ | diagonal entries of $\mathbf{M}$ | kg |
| $K_{11}$, $K_{12}$, $K_{22}$ | entries of $\mathbf{K}$ | N/m |
| $B$ | coefficient $m_1 K_{22} + m_2 K_{11}$ | kg N/m |
| $\delta_{ij}$ | Kronecker delta | dimensionless |

Example. Take $m_1 = 2$ kg, $m_2 = 1$ kg, $k_1 = 2000$ N/m, and $k_2 = 1000$ N/m, so $K_{11} = 3000$ N/m and $K_{22} = 1000$ N/m. Then $B = 5000$ kg N/m, $\det\mathbf{K} = 2\times10^{6}$ $\text{N}^{2}/\text{m}^{2}$, and the discriminant has root $3000$. The two roots are $\omega^{2} = 500$ and $2000$ $\text{rad}^{2}/\text{s}^{2}$, so $\omega_1 = 22.36$ rad/s and $\omega_2 = 44.72$ rad/s. The shapes are $(1, 2)$ and $(1, -1)$. Mode 1 has both masses moving together with mass 2 moving twice as far; in mode 2 they move oppositely. The modal mass of $(1, 2)$ is $2 + 4 = 6$ kg, so the mass-normalized shape is $(0.4082, 0.8165)$. Orthogonality: $\boldsymbol{\phi}_1^{\mathsf{T}}\mathbf{M}\boldsymbol{\phi}_2 = 0$ kg.

Holds when: $\mathbf{M}$ and $\mathbf{K}$ are symmetric and positive definite, motion is undamped, and eigenvalues are distinct (repeated roots allow any combination of the shapes in their subspace).
Breaks when: damping is not proportional (the modes are then complex and do not decouple), the matrices are not symmetric, or the model has rigid-body modes ($\omega = 0$ roots).
Source and basis: derived from the symmetric generalized eigenproblem; the underlying mathematics is in [Linear algebra and differential equations](../math/reference-linear-algebra-differential-equations.md).

<details><summary>Verification</summary>

```verify
m1 = q(2, "kg")
m2 = q(1, "kg")
K11 = q(3000, "N/m")
K12 = q(-1000, "N/m")
K22 = q(1000, "N/m")
dK = K11 * K22 - K12**2
B = m1 * K22 + m2 * K11
expect(B, "5000 kg N/m")
disc = sqrt(B**2 - 4 * m1 * m2 * dK)
expect(disc, "3000 kg N/m")
w1sq = (B - disc) / (2 * m1 * m2)
w2sq = (B + disc) / (2 * m1 * m2)
expect(w1sq, "500 rad^2/s^2")
expect(w2sq, "2000 rad^2/s^2")
expect(sqrt(w1sq), "22.36 rad/s")
expect(sqrt(w2sq), "44.72 rad/s")
s1 = (K11 - w1sq * m1) / (-K12)
s2 = (K11 - w2sq * m1) / (-K12)
expect(s1, "2")
expect(s2, "-1")
modal_mass = m1 + m2 * s1**2
expect(modal_mass, "6 kg")
expect(1 / sqrt(modal_mass / q(1, "kg")), "0.4082")
expect(s1 / sqrt(modal_mass / q(1, "kg")), "0.8165")
expect(m1 * 1 * 1 + m2 * s1 * s2, "0 kg")
```

</details>

## Modal superposition and modal damping

### Decoupling the equations of motion

**Modal superposition** writes the response as a sum of mode shapes times modal coordinates, $\mathbf{x} = \sum_i \boldsymbol{\phi}_i q_i$. With proportional damping, each modal coordinate obeys an SDOF equation.

$$\ddot{q}_i + 2\zeta_i\omega_i\dot{q}_i + \omega_i^{2}q_i = \frac{\boldsymbol{\phi}_i^{\mathsf{T}}\mathbf{f}(t)}{m_i} \qquad m_i = \boldsymbol{\phi}_i^{\mathsf{T}}\mathbf{M}\boldsymbol{\phi}_i \qquad \zeta_i = \frac{\alpha}{2\omega_i} + \frac{\beta_R\,\omega_i}{2}$$

The second relation is **Rayleigh damping**, $\mathbf{C} = \alpha\mathbf{M} + \beta_R\mathbf{K}$. To give damping ratio $\zeta$ at two frequencies $\omega_a$ and $\omega_b$:

$$\alpha = \frac{2\zeta\,\omega_a\omega_b}{\omega_a + \omega_b} \qquad \beta_R = \frac{2\zeta}{\omega_a + \omega_b}$$

The mass term damps low modes most, the stiffness term damps high modes most, and between the two anchor frequencies the damping ratio dips below $\zeta$. In practice an engineer often assigns $\zeta_i$ to each mode directly from test data and skips the matrix $\mathbf{C}$.

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $q_i$ | modal coordinate of mode $i$ | m |
| $\boldsymbol{\phi}_i$ | dimensionless mode shape vector | dimensionless |
| $m_i$ | modal mass, $\boldsymbol{\phi}_i^{\mathsf{T}}\mathbf{M}\boldsymbol{\phi}_i$ | kg |
| $\mathbf{M}$ | mass matrix | kg |
| $\omega_i$ | natural angular frequency of mode $i$ | rad/s |
| $\zeta_i$ | modal damping ratio | dimensionless |
| $\mathbf{f}$ | applied force vector | N |
| $\alpha$ | mass-proportional damping coefficient | 1/s |
| $\beta_R$ | stiffness-proportional damping coefficient | s |
| $\omega_a$, $\omega_b$ | two frequencies where the damping ratio is set | rad/s |
| $\zeta$ | target damping ratio at those frequencies | dimensionless |

Example. For the two-mass chain above, a force of 10 N on mass 1 gives the first modal force $\boldsymbol{\phi}_1^{\mathsf{T}}\mathbf{f} = 0.4082 \times 10 = 4.082$ N. With modal mass $m_1 = 1$ kg, the right-hand side for mode 1 is 4.082 $\text{m/s}^{2}$. To set $\zeta = 0.02$ at $\omega_a = 22.36$ and $\omega_b = 44.72$ rad/s, $\alpha = 0.5963$ 1/s and $\beta_R = 5.963\times10^{-4}$ s.

Holds when: the damping matrix is diagonalized by the undamped modes (proportional damping, or light damping where the off-diagonal terms are small).
Breaks when: damping is concentrated in a few joints or dampers (non-proportional, so use complex modes), or when too few modes are kept to represent the load (add residual static flexibility).
Source and basis: derived from the orthogonality of mode shapes in the previous entry; Rayleigh damping is the standard proportional model.

<details><summary>Verification</summary>

```verify
wa = sqrt(q(500, "rad^2/s^2"))
wb = sqrt(q(2000, "rad^2/s^2"))
expect(wa, "22.36 rad/s")
expect(wb, "44.72 rad/s")
z = q(0.02, "")
phi = q(0.4082, "")
force = q(10, "N")
mi = q(1, "kg")
expect(phi * force, "4.082 N")
expect(phi * force / mi, "4.082 m/s^2")
al = 2 * z * wa * wb / (wa + wb)
be = 2 * z / (wa + wb)
expect(al, "0.5963 1/s")
expect(be, "5.963e-4 s")
expect(al / (2 * wa) + be * wa / 2, "0.02")
expect(al / (2 * wb) + be * wb / 2, "0.02")
phi1 = 1 / sqrt(q(6, ""))
expect(phi1, "0.4082")
expect(wa, "22.36 rad/s")
expect(wb, "44.72 rad/s")
expect(phi1 * q(10, "N"), "4.082 N")
expect(phi1 * q(10, "N") / q(1, "kg"), "4.082 m/s^2")
```

</details>

## Continuous systems

### Taut string, axial bar, and torsional shaft

A **continuous system** has mass and stiffness spread along its length, so it has infinitely many modes. The string, the axial bar, and the torsional shaft all obey the same wave equation with a wave speed $c_w$, and their frequencies follow from the end conditions.

$$f_n = \frac{n\,c_w}{2L}\quad\text{(string fixed at both ends; bar or shaft with both ends fixed or both free)}$$

$$f_n = \frac{(2n-1)\,c_w}{4L}\quad\text{(bar or shaft fixed at one end and free at the other)} \qquad c_w = \sqrt{\frac{T}{\rho_\ell}},\ \sqrt{\frac{E}{\rho}},\ \sqrt{\frac{G}{\rho}}$$

The wave speed is the first form for the string, the second for the bar in axial motion, and the third for a circular shaft in torsion. The mode number is $n = 1, 2, 3, \dots$.

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $f_n$ | natural frequency of mode $n$ | Hz |
| $n$ | mode number | dimensionless |
| $c_w$ | wave speed | m/s |
| $L$ | length | m |
| $T$ | string tension | N |
| $\rho_\ell$ | string mass per unit length | kg/m |
| $E$, $G$ | Young's modulus, shear modulus | Pa |
| $\rho$ | material density | $\text{kg/m}^{3}$ |

Example. A string with $T = 100$ N, $\rho_\ell = 0.005$ kg/m, and $L = 0.65$ m has $c_w = 141.4$ m/s and $f_1 = 108.8$ Hz. A steel rod with $E = 200$ GPa and $\rho = 7850$ $\text{kg/m}^{3}$ has $c_w = 5048$ m/s, so fixed-free with $L = 1$ m it has $f_1 = 1262$ Hz. A steel shaft with $G = 80$ GPa and the same density has $c_w = 3192$ m/s; fixed at one end and free at the other with $L = 0.5$ m, it has $f_1 = 1596$ Hz.

Holds when: the string is flexible with a small slope, the bar or circular shaft is uniform with a cross section small against the wavelength, and the ends are ideal (fixed or free); for torsion the section must be circular, solid or hollow, so its torsion constant equals its polar moment.
Breaks when: the string has bending stiffness (the overtones go sharp), the bar is thick (lateral inertia lowers the frequencies), a shaft carries end disks (use the disk inertia as a boundary condition), or the ends are springs.
Source and basis: derived from the one-dimensional wave equation by separation of variables; the wave relations are in [Oscillations, waves, light, and heat](07-waves-light-heat.md).

<details><summary>Verification</summary>

```verify
T = q(100, "N")
rl = q(0.005, "kg/m")
L = q(0.65, "m")
cs = sqrt(T / rl)
expect(cs, "141.4 m/s")
expect(cs / (2 * L), "108.8 Hz")
E = q(200, "GPa")
rho = q(7850, "kg/m^3")
cb = sqrt(E / rho)
expect(cb, "5048 m/s")
expect(cb / (4 * q(1, "m")), "1262 Hz")
G = q(80, "GPa")
ct = sqrt(G / rho)
expect(ct, "3192 m/s")
expect(ct / (4 * q(0.5, "m")), "1596 Hz")
```

</details>

### Euler-Bernoulli beam

An **Euler-Bernoulli beam** is a slender beam whose cross sections stay plane and perpendicular to the neutral axis in bending. Its natural frequencies depend on one dimensionless root $\beta_n L$ set by the end conditions.

$$\omega_n = \left(\beta_n L\right)^{2}\sqrt{\frac{E I_A}{\rho A\,L^{4}}} \qquad f_n = \frac{\omega_n}{2\pi}$$

Values of $\beta_n L$ for the first three bending modes:

| Ends | Frequency equation | $\beta_1 L$ | $\beta_2 L$ | $\beta_3 L$ |
|---|---|---|---|---|
| Simply supported at both ends | $\sin\beta L = 0$ | 3.1416 | 6.2832 | 9.4248 |
| Fixed-free (cantilever) | $\cos\beta L\,\cosh\beta L = -1$ | 1.8751 | 4.6941 | 7.8548 |
| Free-free | $\cos\beta L\,\cosh\beta L = 1$ | 4.7300 | 7.8532 | 10.9956 |
| Fixed-fixed | $\cos\beta L\,\cosh\beta L = 1$ | 4.7300 | 7.8532 | 10.9956 |
| Fixed-pinned | $\tan\beta L = \tanh\beta L$ | 3.9266 | 7.0686 | 10.2102 |

The free-free row omits the two rigid-body modes at zero frequency. For a simply supported beam $\beta_n L = n\pi$. Above the first few modes of the other rows, $\beta_n L$ approaches $(n - 1/2)\pi$ for fixed-free, $(n + 1/2)\pi$ for free-free and fixed-fixed, and $(n + 1/4)\pi$ for fixed-pinned.

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\omega_n$ | natural angular frequency of mode $n$ | rad/s |
| $f_n$ | natural frequency of mode $n$ | Hz |
| $\beta_n L$ | dimensionless root from the frequency equation | dimensionless |
| $E$ | Young's modulus | Pa |
| $I_A$ | second moment of area about the bending axis | $\text{m}^{4}$ |
| $\rho A$ | mass per unit length | kg/m |
| $L$ | length | m |

Example. The steel cantilever from the stiffness entry ($E = 200$ GPa, $I_A = 7.2\times10^{-10}$ $\text{m}^{4}$, $\rho A = 1.884$ kg/m, $L = 0.5$ m) has $EI_A = 144$ N $\text{m}^{2}$ and $\omega_1 = 122.96$ rad/s, or 19.57 Hz. The Rayleigh estimate with $m_{eff} = 33\rho A L/140$ gives 124.76 rad/s, a relative excess of 0.015, as an upper bound should be.

Holds when: the beam is uniform and slender (length well over ten times the depth), motion is small, and rotary inertia and shear deformation are negligible.
Breaks when: the beam is short or deep (Timoshenko theory gives lower frequencies, and the error grows with mode number), carries axial load (compression lowers, tension raises the frequencies), has added masses or varying section, or has flexible supports.
Source and basis: derived from the Euler-Bernoulli beam equation by separation of variables, with the boundary conditions of each row giving the frequency equation; the roots are solutions of that equation.

<details><summary>Verification</summary>

```verify
E = q(200, "GPa")
Ia = q(7.2e-10, "m^4")
rA = q(1.884, "kg/m")
L = q(0.5, "m")
given("33", "140")
expect(E * Ia, "144 N m^2")
w1 = 1.8751**2 * sqrt(E * Ia / (rA * L**4))
expect(w1, "122.96 rad/s")
expect(w1 / (2 * pi), "19.57 Hz")
k = 3 * E * Ia / L**3
wr = sqrt(k / (33 / 140 * rA * L))
expect(wr, "124.76 rad/s")
expect(wr / w1 - 1, "0.015")
check(wr > w1, "Rayleigh is an upper bound")
x = q(1.8751, "")
check(abs(cos(x) + 2 / (exp(x) + exp(-x))) < 1e-3, "cantilever root 1")
x = q(4.6941, "")
check(abs(cos(x) + 2 / (exp(x) + exp(-x))) < 1e-3, "cantilever root 2")
x = q(7.8548, "")
check(abs(cos(x) + 2 / (exp(x) + exp(-x))) < 1e-3, "cantilever root 3")
x = q(4.7300, "")
check(abs(cos(x) - 2 / (exp(x) + exp(-x))) < 1e-3, "free-free root 1")
x = q(7.8532, "")
check(abs(cos(x) - 2 / (exp(x) + exp(-x))) < 1e-3, "free-free root 2")
x = q(10.9956, "")
check(abs(cos(x) - 2 / (exp(x) + exp(-x))) < 1e-3, "free-free root 3")
x = q(3.9266, "")
check(abs(tan(x) - (exp(x) - exp(-x)) / (exp(x) + exp(-x))) < 1e-3, "fixed-pinned root 1")
x = q(7.0686, "")
check(abs(tan(x) - (exp(x) - exp(-x)) / (exp(x) + exp(-x))) < 1e-3, "fixed-pinned root 2")
x = q(10.2102, "")
check(abs(tan(x) - (exp(x) - exp(-x)) / (exp(x) + exp(-x))) < 1e-3, "fixed-pinned root 3")
```

</details>

## Vibration absorber

### Tuned absorber

A **tuned vibration absorber** is a small mass $m_a$ on a spring $k_a$ attached to a machine of mass $M$ and stiffness $k$ that is driven at nearly one frequency. Tuned to that frequency, it makes the machine stand still there, and the absorber carries the motion instead.

$$\frac{X_1}{X_0} = \frac{1 - r_a^{2}}{\left(1 + \kappa - r^{2}\right)\left(1 - r_a^{2}\right) - \kappa} \qquad r = \frac{\omega}{\omega_n},\quad r_a = \frac{\omega}{\omega_a},\quad \kappa = \frac{k_a}{k}$$

Tuned so that $\omega_a = \omega_n$, with mass ratio $\mu_a = m_a/M$, the two new natural frequencies satisfy

$$r^{2} = 1 + \frac{\mu_a}{2} \pm \sqrt{\mu_a + \frac{\mu_a^{2}}{4}} \qquad X_a = -\frac{F_0}{k_a} \quad (\text{absorber amplitude at the tuned frequency})$$

At the tuned frequency the machine amplitude $X_1$ is zero, the absorber amplitude is set only by $F_0/k_a$, and the absorber force on the machine cancels the applied force. A larger $\mu_a$ widens the useful band, because the two new peaks move further apart.

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $X_1$, $X_a$ | steady amplitude of the machine and of the absorber mass | m |
| $X_0$ | static deflection $F_0/k$ of the machine | m |
| $F_0$ | force amplitude on the machine | N |
| $M$, $m_a$ | machine mass and absorber mass | kg |
| $k$, $k_a$ | machine stiffness and absorber stiffness | N/m |
| $\omega_n$, $\omega_a$ | natural frequency of the machine alone and of the absorber alone | rad/s |
| $\omega$ | forcing angular frequency | rad/s |
| $r$, $r_a$ | frequency ratios $\omega/\omega_n$ and $\omega/\omega_a$ | dimensionless |
| $\kappa$ | stiffness ratio $k_a/k$ | dimensionless |
| $\mu_a$ | mass ratio $m_a/M$ | dimensionless |

Example. For $\mu_a = 0.1$, the new natural frequency ratios are $r = 0.8543$ and $r = 1.1705$, so a machine that ran at $r = 1$ now sits between two peaks and must not drift to either. For $M = 100$ kg, $k = 4\times10^{5}$ N/m, $m_a = 10$ kg, so $\omega_n = 63.25$ rad/s, tuning needs $k_a = m_a\omega_n^{2} = 40$ kN/m, and with $F_0 = 50$ N, $X_a = -1.25$ mm.

Holds when: the machine is linear, the forcing has one frequency that does not drift, and damping is negligible (the machine amplitude is zero only without damping).
Breaks when: the forcing frequency varies (the two shifted peaks then fall in the band, so add damping to the absorber), the absorber is detuned by temperature or wear, or the machine has a second mode near the forcing.
Source and basis: derived from the two coupled equations of motion at harmonic frequency; the undamped tuned absorber is a standard textbook result in the vibration text cited below.

<details><summary>Verification</summary>

```verify
mu = q(0.1, "")
root = sqrt(mu + mu**2 / 4)
expect(sqrt(1 + mu / 2 - root), "0.8543")
expect(sqrt(1 + mu / 2 + root), "1.1705")
M = q(100, "kg")
k = q(4e5, "N/m")
ma = mu * M
wn = sqrt(k / M)
expect(wn, "63.25 rad/s")
ka = ma * wn**2
expect(ma, "10 kg")
expect(ka, "40 kN/m")
expect(-q(50, "N") / ka, "-1.25 mm")
r = q(1, "")
ra = r
kap = ka / k
den = (1 + kap - r**2) * (1 - ra**2) - kap
check(abs(1 - ra**2) < 1e-12 and abs(den + kap) < 1e-12, "numerator zero at the tuned frequency")
```

</details>

## Measured response and damping

### Logarithmic decrement and half-power bandwidth

**Damping** is found from tests by two routes. The **logarithmic decrement** $\delta$ is the natural log of the ratio of successive free-decay peaks. The **half-power bandwidth** is the width of the frequency-response peak between the two points at $1/\sqrt{2}$ of the peak amplitude.

$$\delta = \frac{1}{N}\ln\frac{x_0}{x_N} = \frac{2\pi\zeta}{\sqrt{1-\zeta^{2}}} \qquad \zeta = \frac{\delta}{\sqrt{4\pi^{2} + \delta^{2}}}$$

$$\zeta \approx \frac{f_2 - f_1}{2 f_n} \qquad Q \approx \frac{f_n}{f_2 - f_1}$$

The first pair is exact for a linear viscous system and uses peaks $N$ cycles apart, which reduces reading error. The second pair holds for light damping, below about $\zeta = 0.1$.

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\delta$ | logarithmic decrement (not a deflection here) | dimensionless |
| $x_0$, $x_N$ | peak displacement at the start and after $N$ cycles | m |
| $N$ | number of cycles between the two peaks | dimensionless |
| $\zeta$ | damping ratio | dimensionless |
| $f_1$, $f_2$ | frequencies either side of the peak at $1/\sqrt{2}$ of the peak amplitude | Hz |
| $f_n$ | frequency at the peak | Hz |
| $Q$ | quality factor | dimensionless |

Example. A free decay falls from 8.0 mm to 2.0 mm over $N = 5$ cycles. Then $\delta = 0.2773$ and $\zeta = 0.04408$. A response peak at $f_n = 120$ Hz has half-power points at 117 and 123 Hz, so the bandwidth is 6 Hz, $\zeta = 0.025$, and $Q = 20$.

Holds when: free decay is exponential (linear viscous damping), the system is a single mode, and the half-power points are read from an amplitude response with no neighbouring mode.
Breaks when: damping is dry friction (the decay is linear in amplitude), neighbouring modes overlap in the bandwidth, the system is heavily damped (use the exact $\zeta$ from $\delta$), or the sensor is poorly resolved in frequency.
Source and basis: derived from the envelope $e^{-\zeta\omega_n t}$ of the free response and from the amplitude formula for harmonic forcing; taught in [Vibrations](13-vibrations.md).

<details><summary>Verification</summary>

```verify
x0 = q(8, "mm")
xN = q(2, "mm")
d = log(x0 / xN) / 5
expect(d, "0.2773")
expect(d / sqrt(4 * pi**2 + d**2), "0.04408")
fn = q(120, "Hz")
f1 = q(117, "Hz")
f2 = q(123, "Hz")
expect(f2 - f1, "6 Hz")
expect((f2 - f1) / (2 * fn), "0.025")
expect(fn / (f2 - f1), "20")
```

</details>

## Rotor critical speed

### Jeffcott rotor

A **critical speed** is a shaft rotation rate at which the shaft whirls with large amplitude because the rotation frequency matches a bending natural frequency. The **Jeffcott rotor** is the basic model, a point mass (a disk) of mass $m$ with eccentricity $e$ at mid-span of a light elastic shaft on rigid supports.

$$\omega_{cr} = \sqrt{\frac{k_{sh}}{m}} \qquad k_{sh} = \frac{48 E I_A}{L^{3}} \qquad \frac{R_w}{e} = \frac{r^{2}}{\sqrt{(1-r^{2})^{2} + (2\zeta r)^{2}}} \qquad r = \frac{\Omega}{\omega_{cr}}$$

Here $R_w$ is the radius of whirl of the disk centre. Above the critical speed the whirl radius tends to $e$, so the disk spins about its own mass centre (**self-centring**). The speed in rev/min is $60\,\omega_{cr}/(2\pi)$.

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\omega_{cr}$ | critical angular speed | rad/s |
| $k_{sh}$ | shaft bending stiffness at the disk (simply supported, centre disk) | N/m |
| $m$ | disk mass | kg |
| $E$ | Young's modulus of the shaft | Pa |
| $I_A$ | second moment of area of the shaft, $\pi d^{4}/64$ for a solid round shaft | $\text{m}^{4}$ |
| $L$ | span between supports | m |
| $R_w$ | steady whirl radius of the disk centre | m |
| $e$ | eccentricity of the mass centre from the shaft axis | m |
| $\Omega$ | shaft rotation rate | rad/s |
| $r$ | speed ratio $\Omega/\omega_{cr}$ | dimensionless |
| $\zeta$ | damping ratio | dimensionless |

Example. A 20 mm steel shaft ($E = 200$ GPa), 0.6 m between supports, carries an 8 kg disk at mid-span. Then $I_A = 7.854\times10^{-9}$ $\text{m}^{4}$, $k_{sh} = 349.1$ kN/m, $\omega_{cr} = 208.9$ rad/s, which is 33.25 Hz or 1995 rev/min. With $e = 0.1$ mm and $\zeta = 0.05$, the whirl radius at $r = 2$ is 0.1330 mm, close to $e$.

Holds when: the shaft mass is small against the disk, supports are rigid, and the disk sits near mid-span with no gyroscopic effect.
Breaks when: the shaft mass is not negligible (add Rayleigh mass), the supports are flexible (add bearing stiffness in series, which lowers the speed), the disk is off-centre or thick (gyroscopic terms split forward and backward whirl), or fluid-film bearings add cross-coupled stiffness (instability).
Source and basis: derived from the equation of motion of the disk centre in a rotating eccentric frame, which has the form of the rotating-imbalance entry; the shaft stiffness is that of a simply supported beam.

<details><summary>Verification</summary>

```verify
d = q(20, "mm")
E = q(200, "GPa")
L = q(0.6, "m")
m = q(8, "kg")
Ia = pi * d**4 / 64
expect(Ia, "7.854e-9 m^4")
ksh = 48 * E * Ia / L**3
expect(ksh, "349.1 kN/m")
wcr = sqrt(ksh / m)
expect(wcr, "208.9 rad/s")
expect(wcr / (2 * pi), "33.25 Hz")
expect(wcr, "1995 rev/min")
e = q(0.1, "mm")
z = q(0.05, "")
r = q(2, "")
expect(e * r**2 / sqrt((1 - r**2)**2 + (2 * z * r)**2), "0.1330 mm")
```

</details>

## Checklists

Natural frequencies:

- Frequencies computed in rad/s and converted to Hz or rev/min only to report.
- Stiffness taken at the load point and direction, with support and joint compliance added in series.
- Effective mass includes the distributed mass of springs, beams, and fluids that move with the system.
- At least the first modes found, and every mode whose frequency lies in the excitation range.
- Mode shapes checked against the expected motion (number of nodes and signs).

Forced response:

- Every excitation frequency listed: running speed and its multiples, blade-passing, gear mesh, line frequency, vortex shedding.
- Each excitation compared with each natural frequency, with a stated margin (a separation of 15 to 20 percent is a common guide, typical).
- Damping value stated with its source (test, handbook, assumed), and not borrowed from another structure.
- Peak response compared with the allowable stress, displacement, or acceleration.

Isolation:

- Disturbance frequency above $\sqrt{2}$ times the natural frequency of the mount, with a margin.
- Start-up and shut-down pass through resonance. Damping or a fast pass checked.
- Rocking and horizontal modes checked as well as the vertical one.
- Static deflection of the mounts matches the design and the mounts are not overloaded.

Measurement:

- Log decrement taken over several cycles, not one.
- Half-power points read on a response with fine frequency resolution.
- Sensor mass small against the structure mass.

## Sanity checks

- Doubling stiffness raises $\omega_n$ by $\sqrt{2}$, which is a factor 1.41. Doubling mass lowers it by the same factor.
- A static deflection of $\delta_{st}$ on Earth gives $f_n \approx 15.8/\sqrt{\delta_{st}}$ Hz with $\delta_{st}$ in mm.
- Damping ratios of most built structures are about 0.01 to 0.05 (typical), so $Q$ is 10 to 50. Resonance is large unless damping is added.
- Welded steel frames sit near the low end of that range, and bolted, riveted, or jointed structures at the high end. A damper or a viscoelastic layer can reach 0.1 or more.
- The first bending frequency of a steel cantilever of length $L$ and depth $h$ scales as $h/L^{2}$. Doubling the length divides it by 4.
- The bar and string frequencies scale as $1/L$. Halving the length doubles the frequency.
- A mass-normalized mode shape squared and summed over all modes reproduces the inverse of the mass matrix. A mismatch means a normalization slip.
- $TR$ at $r = \sqrt{2}$ is 1 for every damping ratio. A computed curve that misses this point has an error.

<details><summary>Verification</summary>

```verify
expect(sqrt(q(2, "")), "1.41")
g = q(9.80665, "m/s^2", of="g_standard")
dst = q(1, "mm")
expect(sqrt(g / dst) / (2 * pi), "15.8 Hz")
expect(q(2, "")**2, "4")
```

</details>

## Further reference

Named books and standards only for paid items (no links); free items carry a link.

- Mechanical Vibrations, Rao (paid, SDOF through continuous systems, many worked examples).
- Theory of Vibration with Applications, Thomson and Dahleh (paid, SDOF, MDOF, and modal analysis).
- Mechanical Vibrations, Den Hartog (paid, Dover reprint, classical treatment of absorbers and isolation).
- Formulas for Natural Frequency and Mode Shape, Blevins (paid, the largest lookup table of natural frequencies for common structures).
- Roark's Formulas for Stress and Strain, Young and Budynas (paid, stiffness of beams and plates for equivalent springs).
- Rotordynamics of Turbomachinery, Vance (paid, rotors, bearings, and critical speeds beyond the Jeffcott model).
- ISO 20816 series, Mechanical vibration, Measurement and evaluation of machine vibration (standard, vibration severity limits; check the current edition).
- [MIT OpenCourseWare 2.003SC Engineering Dynamics](https://ocw.mit.edu/courses/2-003sc-engineering-dynamics-fall-2011/) by MIT: free lecture notes and problems on free and forced vibration, multi-degree-of-freedom systems, and modal superposition.
- For second-order step metrics and control of vibrating systems, see [Controls reference](reference-controls.md).
- For structural fatigue caused by vibration, see [materials/reference-fracture-fatigue.md](../materials/reference-fracture-fatigue.md).
- For the lookup sheet that covers statics, strength, and the shorter vibration section, see [Mechanics reference](reference-mechanics.md).
