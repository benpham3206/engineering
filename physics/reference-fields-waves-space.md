# Fields, waves, and space reference

**Type:** reference

Electromagnetism is the study of electric and magnetic fields, circuits are closed paths that carry electric current, waves are disturbances that carry energy through space or a material, optics is the study of light, and orbital mechanics is the study of how objects move under gravity in space. This sheet is a lookup for all five, for an engineer who already knows the lessons in this folder and needs a formula, a constant, a limit, or a check in seconds.

## Principles

- Energy is conserved. If your answer creates energy, it is wrong.
- Charge is conserved. The net current into any node is zero.
- Every formula has a regime. Write down the assumption (steady, linear, small amplitude, point mass, geometric optics, impulsive burn) before you trust the number.
- Units first. Carry SI through the calculation and convert prefixes ($\mu$, m, k, M) only at the end.
- A changing magnetic field makes an electric field, and a changing electric field makes a magnetic field. Maxwell's equations are the only source of electromagnetic waves.
- The source sets the frequency of a wave. The medium sets its speed and wavelength.
- Outside a spherically symmetric body, its gravity acts as if all its mass were at the center.
- Decibels add only for incoherent power. Two equal incoherent sources add 3 dB, not double the level.
- Newton's laws, Maxwell's equations, and the conservation laws do not expire. Constants and tables do, so date them.

## Physical constants

Exact SI defining constants (2019 redefinition; exact by definition, so no uncertainty):

| Symbol | Quantity | Exact value | Unit |
|---|---|---|---|
| $\Delta\nu_{\text{Cs}}$ | Hyperfine transition frequency of Cs-133 | 9 192 631 770 | Hz |
| $c$ | Speed of light in vacuum | 299 792 458 | m/s |
| $h$ | Planck constant | $6.62607015 \times 10^{-34}$ | J s |
| $e$ | Elementary charge | $1.602176634 \times 10^{-19}$ | C |
| $k_B$ | Boltzmann constant | $1.380649 \times 10^{-23}$ | J/K |
| $N_A$ | Avogadro constant | $6.02214076 \times 10^{23}$ | mol$^{-1}$ |
| $K_{\mathrm{cd}}$ | Luminous efficacy at 540 THz | 683 | lm/W |

Other constants used in this sheet:

| Symbol | Quantity | Value | Unit | Status |
|---|---|---|---|---|
| $g_0$ | Standard gravity | 9.80665 | m/s$^2$ | Exact (defined) |
| $G$ | Newtonian gravitational constant | $6.67430 \times 10^{-11}$ | m$^3$ kg$^{-1}$ s$^{-2}$ | Measured, relative uncertainty about $2 \times 10^{-5}$ (CODATA 2018) |
| $\varepsilon_0$ | Vacuum permittivity | $8.8541878 \times 10^{-12}$ | F/m | Derived from $c$ and $\mu_0$ (CODATA) |
| $\mu_0$ | Vacuum permeability | $1.2566371 \times 10^{-6}$ | N/A$^2$ | Relation: $\mu_0 = 1/(\varepsilon_0 c^2)$. Not exactly $4\pi \times 10^{-7}$ (the pre-2019 defined value), which differs by about $5 \times 10^{-10}$ relative |
| $\sigma$ | Stefan-Boltzmann constant | $5.670374 \times 10^{-8}$ | W m$^{-2}$ K$^{-4}$ | Derived from $h$, $k_B$, $c$: $\sigma = 2\pi^5 k_B^4 / (15 h^3 c^2)$ |
| $k_e$ | Coulomb constant | $8.98755 \times 10^{9}$ | N m$^2$/C$^2$ | $k_e = 1/(4\pi\varepsilon_0)$ |

- Quote $\varepsilon_0$ and $\mu_0$ to 5 significant figures unless the work needs more. Later CODATA adjustments move the last digits by about $10^{-9}$ relative.
- Use $\mu_0 = 4\pi \times 10^{-7}$ N/A$^2$ only as a rounded value; it is accurate to about $10^{-9}$ relative after 2019 (the old definition was exact).

## Electricity and magnetism

### Electrostatics

$$F = k_e \frac{|q_1 q_2|}{r^2}, \qquad \vec{E} = \frac{\vec{F}}{q}$$

- $F$: force (N). $q_1, q_2$: charges (C). $r$: separation (m). $\vec{E}$: field (V/m).
- Point charge: $E = k_e |q| / r^2$.
- Infinite line charge of linear density $\lambda$ (C/m): $E = \lambda / (2\pi\varepsilon_0 r)$.
- Infinite plane of surface density $\sigma_s$ (C/m$^2$): $E = \sigma_s / (2\varepsilon_0)$.
- Potential of a point charge: $V = k_e q / r$ (V).

**Holds when:** charges are at rest, or move slowly, and the field is static. Point charge formulas need the charge to be small compared with $r$, or the distribution to be spherical.

**Breaks when:** charges move fast (use the full Maxwell equations), or the geometry is not symmetric (integrate Coulomb's law over the charge distribution).

### Gauss's law

$$\oint_S \vec{E} \cdot d\vec{A} = \frac{Q_{\text{enc}}}{\varepsilon_0}$$

- $Q_{\text{enc}}$: charge enclosed by the surface $S$ (C).
- Use it when the field has the symmetry of the problem: spherical, cylindrical, or planar.

**Holds when:** always true for static fields. It is useful only when symmetry lets you pull $E$ out of the integral.

**Breaks when:** the symmetry is absent. Gauss's law is still true, but it does not give $E$ directly.

### Magnetostatics: Ampere's law

$$\oint_C \vec{B} \cdot d\vec{\ell} = \mu_0 I_{\text{enc}}$$

- $\vec{B}$: magnetic flux density (T). $I_{\text{enc}}$: current through the loop (A).
- Long straight wire: $B = \mu_0 I / (2\pi r)$.
- Ideal long solenoid with $n$ turns per meter: $B = \mu_0 n I$ (inside), near zero outside.
- Toroid with $N$ turns, mean radius $r$: $B = \mu_0 N I / (2\pi r)$ (inside the core).
- Magnetic field of a current loop at its center: $B = \mu_0 I / (2R)$.

**Holds when:** steady currents, no changing electric field (the displacement current term is zero).

**Breaks when:** fields change in time (add Maxwell's displacement term, $\mu_0 \varepsilon_0 \, d\Phi_E/dt$), or the material is magnetic (use $\mu = \mu_r \mu_0$ and $\vec{H}$).

### Faraday's law and induction

$$\mathcal{E} = -N \frac{d\Phi_B}{dt}, \qquad \Phi_B = \int \vec{B} \cdot d\vec{A}$$

- $\mathcal{E}$: induced emf (V). $\Phi_B$: flux (Wb $=$ T m$^2$). $N$: number of turns.
- Motional emf of a rod of length $\ell$ moving at $v$ across a field $B$: $\mathcal{E} = B \ell v$ (for $\vec{v}$, $\vec{B}$, and the rod mutually perpendicular; in general $\mathcal{E} = (\vec{v} \times \vec{B}) \cdot \vec{\ell}$).
- Lenz's law sets the sign: the induced current opposes the change in flux.

**Holds when:** the circuit is a closed loop and the field is quasi-static.

**Breaks when:** the flux through the circuit is ambiguous (sliding contacts or a path that changes with the motion), where you should use the Lorentz force on the moving charges instead; or the radiation wavelength is comparable to the loop size.

### Lorentz force

$$\vec{F} = q(\vec{E} + \vec{v} \times \vec{B}), \qquad \vec{F}_{\text{wire}} = I \vec{\ell} \times \vec{B}$$

- $\vec{v}$: velocity (m/s). $\vec{\ell}$: wire vector (m).
- Magnitude for $\vec{v} \perp \vec{B}$: $F = qvB$. Zero for $\vec{v} \parallel \vec{B}$.
- Cyclotron radius of a charge moving perpendicular to $\vec{B}$: $r = mv / (|q| B)$.
- Cyclotron frequency: $f = |q| B / (2\pi m)$, independent of speed (non-relativistic).
- Velocity selector: $E = vB$ passes charges with speed $v = E/B$ undeflected.

**Holds when:** speeds are much less than $c$ for the cyclotron formula.

**Breaks when:** speeds approach $c$ (use relativistic mass, $\gamma m$), or fields vary across the orbit.

### Capacitance of standard geometries

| Geometry | Capacitance | Symbols |
|---|---|---|
| Parallel plates (fringing neglected) | $C = \varepsilon A / d$ | $A$ plate area (m$^2$), $d$ gap (m) |
| Coaxial cylinders, length $L$ | $C = 2\pi\varepsilon L / \ln(b/a)$ | $a$, $b$ inner and outer radii (m) |
| Isolated sphere, radius $R$ | $C = 4\pi\varepsilon R$ | $R$ (m) |
| Two spheres, radii $a$, $b$ (center to center $d \gg a, b$) | $C \approx 4\pi\varepsilon / (1/a + 1/b)$ | |

- Series: $1/C = \sum 1/C_i$. Parallel: $C = \sum C_i$.
- Dielectric filling: multiply $\varepsilon_0$ by $\varepsilon_r$ (relative permittivity, dimensionless).

Example: parallel plates with $A = 0.010$ m$^2$ and $d = 1.0$ mm in air give $C = 88.5$ pF.

**Holds when:** the gap is small compared with the plate size (parallel plates) and the field is confined.

**Breaks when:** the gap is comparable to the plate size (fringing field matters); at high frequency, the capacitor has lead inductance.

### Inductance of standard geometries

| Geometry | Inductance | Symbols |
|---|---|---|
| Long solenoid, cross-section $A$, length $\ell$ | $L = \mu N^2 A / \ell$ | $N$ turns, $\mu = \mu_r \mu_0$ |
| Coaxial cable, length $L$ | $L = (\mu L / 2\pi) \ln(b/a)$ | $a$, $b$ inner and outer radii |
| Toroid, rectangular section, height $h$ | $L = (\mu N^2 h / 2\pi) \ln(b/a)$ | $a$, $b$ inner and outer radii |
| Long straight wire, per unit length | $L' \approx (\mu_0 / 2\pi) \ln(d/a)$ | $d$ return distance, $a$ wire radius |

Example: a solenoid with $n = 1000$ turns per meter and $I = 2.0$ A has $B = \mu_0 n I = 2.51$ mT inside.

**Holds when:** the solenoid is long compared with its diameter (end effects neglected); the core is linear.

**Breaks when:** the core saturates (ferromagnetic cores), or the frequency is high enough that the winding capacitance matters.

### Energy stored

$$U_C = \frac{1}{2} C V^2 = \frac{Q^2}{2C}, \qquad U_L = \frac{1}{2} L I^2$$

$$u_E = \frac{1}{2} \varepsilon E^2 \ \text{(J/m}^3\text{)}, \qquad u_B = \frac{B^2}{2\mu} \ \text{(J/m}^3\text{)}$$

- $U$: energy (J). $u_E$, $u_B$: energy densities. $\mu = \mu_r\mu_0$ is the permeability of the material ($\mu_0$ in vacuum).
- Total energy stored in a field: $U = \int u \, dV$.

**Holds when:** linear dielectrics and magnetic materials.

**Breaks when:** the material is nonlinear or lossy (hysteresis, dielectric absorption, eddy currents).

## Circuit relations

### Ohm's law, power, resistance

$$V = IR, \qquad P = VI = I^2 R = \frac{V^2}{R}$$

- $P$: power (W). $R$: resistance ($\Omega$).
- Resistors in series add. Resistors in parallel: $1/R = \sum 1/R_i$.
- Resistance of a wire: $R = \rho L / A$, with $\rho$ resistivity ($\Omega$ m).

**Holds when:** the element is ohmic (linear and at constant temperature).

**Breaks when:** diodes, arcs, thermistors, and superconductors are present; at high frequency, skin effect raises the effective resistance. Ohm's law is an approximation for most conductors.

### RC and RL time constants

For a step input $V_0$ at $t = 0$:

$$\tau_{\mathrm{RC}} = RC, \qquad v_C(t) = V_0 \left(1 - e^{-t/\tau_{\mathrm{RC}}}\right)$$

$$\tau_{\mathrm{RL}} = \frac{L}{R}, \qquad i_L(t) = \frac{V_0}{R} \left(1 - e^{-t/\tau_{\mathrm{RL}}}\right)$$

- $\tau$: time constant (s). After $5\tau$ the response is within 1 percent of its final value.
- Discharge: $v_C = V_0 e^{-t/\tau}$ and $i_L = (V_0 / R) e^{-t/\tau}$ once the source is removed.

Example: $R = 1.0$ k$\Omega$ and $C = 1.0$ $\mu$F give $\tau = 1.0$ ms. $L = 10$ mH with $R = 100$ $\Omega$ gives $\tau = 0.10$ ms.

**Holds when:** the element is linear and lumped; the source is an ideal step.

**Breaks when:** parasitic inductance or capacitance dominates; the source has finite rise time; the element saturates.

### Impedance of $R$, $L$, $C$ (phasor form, $e^{j\omega t}$)

| Element | Impedance | Magnitude | Phase of $V$ relative to $I$ |
|---|---|---|---|
| Resistor | $Z_R = R$ | $R$ | 0 |
| Inductor | $Z_L = j\omega L$ | $\omega L$ | $+90^\circ$ |
| Capacitor | $Z_C = 1/(j\omega C)$ | $1/(\omega C)$ | $-90^\circ$ |

- $\omega = 2\pi f$ (rad/s). $j = \sqrt{-1}$ (engineers write $j$ to avoid confusion with current $i$).
- Series RLC: $Z = R + j(\omega L - 1/(\omega C))$. Resonance at $\omega_0 = 1/\sqrt{LC}$ (where the reactance is zero).
- Series RLC quality factor: $Q = \omega_0 L / R$. Bandwidth $\Delta\omega \approx \omega_0 / Q$.
- Average AC power: $P = V_{\text{rms}} I_{\text{rms}} \cos\varphi$, where $\varphi$ is the phase angle of $Z$ and $\cos\varphi$ is the power factor.

**Holds when:** steady-state sinusoidal excitation at a single frequency; linear elements.

**Breaks when:** the circuit is nonlinear, or wavelength is not much larger than the circuit size (a rule of thumb: keep the largest dimension under $\lambda / 10$ to use lumped models).

## Waves

### Wave equation and speed

$$\frac{\partial^2 y}{\partial x^2} = \frac{1}{v^2} \frac{\partial^2 y}{\partial t^2}$$

- $y$: displacement (m, or the field quantity). $x$: position (m). $t$: time (s). $v$: wave speed (m/s).
- General solution in one dimension: $y = f(x - vt) + g(x + vt)$.
- Harmonic wave: $y = A \cos(kx - \omega t)$, with wavenumber $k = 2\pi / \lambda$ (rad/m) and $\omega = 2\pi f$.
- Dispersion relation: $\omega = v k$ holds only if $v$ does not depend on frequency.

Speed in common media (typical):

| Medium | Speed (m/s) | Basis |
|---|---|---|
| Air, 20 $^\circ$C | 343 | Ideal gas, $v = \sqrt{\gamma R T / M}$ |
| Fresh water, 20 $^\circ$C | about 1480 | Typical |
| Steel bar, longitudinal | about 5000 to 6000 | Depends on mode and geometry; $\sqrt{E/\rho}$ for a thin bar |
| Light in vacuum | 299 792 458 | Exact |

- Sound in an ideal gas: $v = \sqrt{\gamma R T / M}$ with $\gamma$ the heat capacity ratio (1.4 for air), $R$ the gas constant, $T$ in kelvin, and $M$ the molar mass (kg/mol).
- Wave on a string: $v = \sqrt{T_s / \mu}$, with $T_s$ tension (N) and $\mu$ mass per unit length (kg/m).
- Bar: $v = \sqrt{E / \rho}$, with $E$ Young's modulus (Pa) and $\rho$ density (kg/m$^3$).

**Holds when:** linear, non-dispersive, small amplitude.

**Breaks when:** amplitude is large (nonlinear steepening, shocks), the medium is dispersive (wave packets spread), or the wavelength is comparable to the medium's structure.

### Standing waves and natural frequencies

| Boundary condition | Harmonics | Wavelength | Frequency |
|---|---|---|---|
| String fixed at both ends, length $L$ | $f_n = n v / (2L)$, $n = 1, 2, 3, \ldots$ | $\lambda_n = 2L / n$ | same form |
| Pipe open at both ends, length $L$ | $f_n = n v / (2L)$ | | |
| Pipe closed at one end, open at the other | $f_n = (2n - 1) v / (4L)$, odd harmonics | | |

- Standing waves form from two traveling waves of equal frequency going opposite ways.
- Nodes are points of zero displacement; antinodes are points of maximum displacement.

**Holds when:** the boundaries are ideal (rigid or free), and damping is small.

**Breaks when:** end corrections matter (open pipe: effective length is slightly longer, about $0.6$ times the radius at each open end); the boundary is compliant; damping is large.

### Resonance and forced response

- A driven oscillator peaks near its natural frequency. The peak height is set by damping; $Q = \omega_0 / \Delta\omega$.
- Avoid driving a structure at a natural frequency within a band of about $\pm 10$ percent, or add damping, when the response is large.

### Doppler effect (sound, moving source and observer)

$$f' = f \, \frac{v + v_o}{v - v_s}$$

- $f'$: observed frequency (Hz). $f$: source frequency (Hz). $v$: wave speed in the medium (m/s).
- $v_o$: observer speed toward the source (positive if approaching). $v_s$: source speed toward the observer (positive if approaching).

Example: a 440 Hz source approaching a stationary listener at 30 m/s in 343 m/s air is heard at 482 Hz.

**Holds when:** motion is along the line joining source and observer; speeds are much less than $v$ for the simple form.

**Breaks when:** the source crosses or circles the observer (use the component along the line of sight); speed approaches $v$ (shock wave, Mach cone); for light, use the relativistic form $f' = f \sqrt{(1 + \beta)/(1 - \beta)}$ with $\beta = v/c$ and $v$ the approach speed.

### Intensity and decibels

- Intensity (power per unit area, W/m$^2$) from a point source of power $P$ (W) at distance $r$ (m): $I = P / (4\pi r^2)$ (free field, no reflection).
- Sound intensity level: $L_I = 10 \log_{10}(I / I_0)$ dB, with $I_0 = 10^{-12}$ W/m$^2$.
- Sound pressure level: $L_p = 20 \log_{10}(p / p_0)$ dB, with $p_0 = 20\ \mu$Pa (rms).
- Doubling intensity: $+3$ dB. Doubling pressure: $+6$ dB. Halving distance from a point source: $+6$ dB.
- Adding incoherent sources: add intensities, then convert to dB. Two 80 dB sources give 83 dB, not 160 dB.

| Level (dB) | Typical sound |
|---|---|
| 0 | Threshold of hearing (at 1 kHz, reference) |
| 60 | Normal conversation at 1 m (typical) |
| 85 | Long-term hearing damage threshold used in many standards (typical) |
| 120 | Pain threshold (typical, approximate) |

**Holds when:** free-field spreading (no reflections); incoherent sources.

**Breaks when:** reflections or enclosures (a room gives a reverberant field); coherent sources (interference); frequency weighting is needed (A-weighting for human loudness).

## Optics

### Refraction and total internal reflection

$$n_1 \sin\theta_1 = n_2 \sin\theta_2, \qquad \sin\theta_c = \frac{n_2}{n_1} \ (n_1 > n_2)$$

- $n$: refractive index (dimensionless), $n = c/v$. $\theta$: angle from the surface normal.
- Critical angle $\theta_c$: above it, light is totally internally reflected.
- Example: air ($n = 1.00$) to glass ($n = 1.50$) at $30^\circ$ incidence gives a refraction angle of $19.5^\circ$.
- Wavelength in a medium: $\lambda_n = \lambda_0 / n$. Frequency does not change.

Typical refractive indices (visible light): air 1.00, water 1.33, common crown glass about 1.5, diamond about 2.42.

**Holds when:** geometric optics (wavelength much smaller than the feature size); isotropic, non-absorbing media.

**Breaks when:** the material is dispersive (index depends on wavelength, so white light separates); the medium is anisotropic (birefringence); the surface is smaller than a wavelength.

### Thin lens

$$\frac{1}{f} = \frac{1}{d_o} + \frac{1}{d_i}, \qquad m = -\frac{d_i}{d_o}$$

- $f$: focal length (m). $d_o$: object distance (m). $d_i$: image distance (m, positive for real images on the far side). $m$: lateral magnification.
- Lensmaker's equation: $1/f = (n - 1)(1/R_1 - 1/R_2)$, with radii $R_1$, $R_2$ (m), positive when the center of curvature is on the far side.
- Example: $f = 0.10$ m and $d_o = 0.30$ m give $d_i = 0.15$ m and $m = -0.5$ (real, inverted, half size).

**Holds when:** paraxial rays (small angles), thin lens (thickness much less than $f$).

**Breaks when:** the lens is thick (use principal planes), rays are steep (spherical and chromatic aberration), or the sign convention is ignored: an object inside the focal length gives a negative $d_i$ (virtual image), which the equation handles correctly.

### Diffraction limit

$$\theta_{\min} = 1.22 \frac{\lambda}{D} \qquad \text{(Rayleigh criterion, circular aperture)}$$

- $\theta_{\min}$: smallest resolvable angle (rad). $\lambda$: wavelength (m). $D$: aperture diameter (m).
- Microscope (Abbe): smallest resolvable distance $d = \lambda / (2\,\text{NA})$, with $\text{NA} = n \sin\theta$.

Example: $\lambda = 550$ nm and $D = 0.10$ m give $\theta_{\min} = 6.7\ \mu$rad. A microscope with NA 0.95 at 550 nm resolves about 290 nm.

**Holds when:** the aperture is circular, the source is incoherent, and the object is in the far field.

**Breaks when:** the image is not in focus, the aperture is not circular (change the constant), or the detector is smaller than the Airy disk (the sampling limit then matters).

## Gravity and orbits

### Newton's law of gravitation

$$F = G \frac{m_1 m_2}{r^2}, \qquad g = \frac{GM}{r^2}$$

- $F$: force (N). $m_1$, $m_2$: masses (kg). $r$: distance between centers (m). $M$: mass of the attracting body (kg). $g$: gravitational acceleration at distance $r$ (m/s$^2$).
- Weight at a location: $W = m g_{\text{local}}$. Use the local $g$, not 9.80665.
- Above a body of radius $R$ at altitude $h$: $g(h) = g_{\text{surface}} \, (R / (R + h))^2$.
- Standard gravity $g_0 = 9.80665$ m/s$^2$ is a defined reference for converting mass and force, not a value at any place.

Standard gravitational parameter $\mu = GM$ (m$^3$/s$^2$) is usually known more precisely than $G$ or $M$ separately. Use $\mu$ in every orbit formula.

**Holds when:** point masses, or spherically symmetric bodies seen from outside; no relativistic effects.

**Breaks when:** the body is oblate or irregular (add $J_2$ and higher harmonics); you are inside a mass distribution; speeds or fields are strong (general relativity; GPS needs its correction).

### Orbital relations (two-body, central force)

| Quantity | Formula | Notes |
|---|---|---|
| Circular speed | $v_c = \sqrt{\mu / r}$ | At radius $r$ from the center |
| Escape speed | $v_e = \sqrt{2\mu / r}$ | $= \sqrt{2} v_c$ at the same radius |
| Vis-viva | $v^2 = \mu (2/r - 1/a)$ | $a$: semi-major axis (m). Works for ellipses, parabolas ($a \to \infty$), hyperbolas ($a < 0$) |
| Specific orbital energy | $\varepsilon = -\mu / (2a)$ (J/kg) | Negative for bound orbits |
| Kepler's third law | $T^2 = 4\pi^2 a^3 / \mu$ | $T$: period (s). Constant $T^2/a^3$ for a given central body |
| Orbital period, circular | $T = 2\pi r / v_c = 2\pi \sqrt{r^3/\mu}$ | Same as Kepler for $a = r$ |

Example: a circular orbit 300 km above Earth's mean radius has $v_c = 7.73$ km/s and period 90.4 min. A geostationary orbit has $a = 42\,164$ km and period 23.93 h (one sidereal day).

**Holds when:** two bodies, the smaller of negligible mass, no drag, no thrust.

**Breaks when:** atmosphere (drag lowers $a$); third bodies (Moon and Sun perturb Earth orbits); thrust (use the rocket equation); $J_2$ oblateness precesses the orbit; very close to a massive body (relativistic precession).

### Hohmann transfer (coplanar, circular, two-impulse)

$$\Delta v_1 = \sqrt{\frac{\mu}{r_1}} \left( \sqrt{\frac{2 r_2}{r_1 + r_2}} - 1 \right), \qquad \Delta v_2 = \sqrt{\frac{\mu}{r_2}} \left( 1 - \sqrt{\frac{2 r_1}{r_1 + r_2}} \right)$$

- $r_1$, $r_2$: starting and target orbit radii (m, from the center, not altitude). $\Delta v_1$, $\Delta v_2$: burns at periapsis and apoapsis (m/s).
- Transfer time (half the ellipse period): $t = \pi \sqrt{a_t^3 / \mu}$, with $a_t = (r_1 + r_2)/2$.

Example: from a 300 km circular orbit to geostationary altitude, $\Delta v_1 = 2.43$ km/s, $\Delta v_2 = 1.47$ km/s, total 3.90 km/s, transfer time 5.27 h.

**Holds when:** burns are impulsive (instantaneous), the orbits are coplanar and nearly circular, and the transfer is between two-body orbits.

**Breaks when:** burns take a significant fraction of the orbit (use finite-burn or gravity-loss estimates); the plane must change (add an inclination change, which is expensive); the transfer uses a third body (gravity assist, low-energy transfers); the target is not circular.

### Rocket equation and specific impulse

$$\Delta v = v_e \ln\frac{m_0}{m_f} = I_{\mathrm{sp}} g_0 \ln\frac{m_0}{m_f}$$

$$I_{\mathrm{sp}} = \frac{v_e}{g_0} \qquad \text{(s)}$$

- $\Delta v$: change in velocity (m/s). $v_e$: effective exhaust velocity (m/s). $m_0$, $m_f$: initial and final mass, including propellant (kg).
- $I_{\mathrm{sp}}$: specific impulse (s). Thrust per unit propellant weight flow. Higher is more efficient.
- Mass ratio $m_0/m_f$ grows exponentially with $\Delta v$. Doubling $\Delta v$ squares the mass ratio.

Typical specific impulse (vacuum, approximate):

| Propulsion | $I_{\mathrm{sp}}$ (s, typical) |
|---|---|
| Cold gas thruster | 50 to 80 for nitrogen; up to about 165 for helium |
| Monopropellant hydrazine | 200 to 230 |
| Liquid bipropellant (LOX/kerosene, LOX/LH$_2$) | about 300 to 360 (kerosene); about 390 to 460 (LH$_2$) |
| Solid rocket motor | 240 to 280 |
| Electric (Hall thruster, ion) | 1500 to 4000 |

Example: $I_{\mathrm{sp}} = 450$ s and a mass ratio of 3 give $\Delta v = 4.85$ km/s.

**Holds when:** the exhaust velocity is constant, thrust acts along the velocity, and the burn is short compared with the orbit.

**Breaks when:** gravity losses (launch needs roughly 1 to 2 km/s beyond the orbital speed), drag losses, steering losses, thrust that varies with time or atmosphere; the exhaust velocity is not uniform across the nozzle.

## Radiation and heat in space

- Stefan-Boltzmann law: $P = \varepsilon \sigma A T^4$, with $\varepsilon$ emissivity (0 to 1, dimensionless), $A$ area (m$^2$), $T$ absolute temperature (K).
- Example: an ideal black body at 300 K emits $\sigma T^4 = 459$ W/m$^2$.
- Equilibrium temperature of a body with absorptance $\alpha$ facing sunlight flux $S$ (about 1361 W/m$^2$ at 1 au): $\alpha S = \varepsilon \sigma T^4$ (for a flat plate radiating from one side, no internal heat).

**Holds when:** blackbody or grey-body emission, uniform temperature.

**Breaks when:** the surface is spectrally selective (use absorptance and emissivity by wavelength); the body rotates or spins unevenly; internal heat dominates.

## Planetary and solar reference values

Typical values using mean radii. Surface gravity is $g = GM / R_{\text{mean}}^2$ (point mass, no rotation, no oblateness). Escape speed is $\sqrt{2GM / R_{\text{mean}}}$. Gas giants and the Sun have no solid surface, so these are reference values at the mean radius.

| Body | Mean radius (km) | $GM$ (m$^3$/s$^2$, typical) | Surface $g$ (m/s$^2$, typical) | Escape speed (km/s, typical) |
|---|---|---|---|---|
| Sun (photosphere, nominal) | 695 700 | $1.3271 \times 10^{20}$ | 274.2 | 617.7 |
| Mercury | 2439.7 | $2.2032 \times 10^{13}$ | 3.70 | 4.25 |
| Venus | 6051.8 | $3.2486 \times 10^{14}$ | 8.87 | 10.36 |
| Earth | 6371.0 | $3.9860 \times 10^{14}$ | 9.82 | 11.19 |
| Moon | 1737.4 | $4.9028 \times 10^{12}$ | 1.62 | 2.38 |
| Mars | 3389.5 | $4.2828 \times 10^{13}$ | 3.73 | 5.03 |
| Jupiter | 69 911 | $1.2669 \times 10^{17}$ | 25.92 | 60.20 |
| Saturn | 58 232 | $3.7931 \times 10^{16}$ | 11.19 | 36.09 |
| Titan | 2574.7 | $8.978 \times 10^{12}$ | 1.35 | 2.64 |
| Europa | 1560.8 | $3.2027 \times 10^{12}$ | 1.31 | 2.03 |

- Earth's computed $g = 9.82$ m/s$^2$ at the mean radius differs from the defined 9.80665 m/s$^2$ because the real Earth is oblate and rotates. Use a local measured value or a geodetic model for real work.
- All $g$ values here are $GM/R^2$ at the mean radius, with no rotation. For Jupiter and Saturn the radius is measured at the 1 bar pressure level, because they have no solid surface.
- Gas giants are strongly oblate, so the equatorial radius gives a lower value: $GM/R_{\mathrm{eq}}^2$ is about 24.79 m/s$^2$ on Jupiter ($R_{\mathrm{eq}}$ $=$ 71 492 km) and 10.44 m/s$^2$ on Saturn (60 268 km). Their fast rotation lowers the effective value at the equator further, to about 22.6 and 8.8 m/s$^2$.
- Titan and Europa values are typical published mean-radius values, not exact.

## Checklists

Before trusting an electrical result:

- [ ] Every quantity has SI units, and prefixes are converted ($\mu$, m, k, M).
- [ ] Signs are set: current direction, voltage polarity, and the sign in Faraday's law (use Lenz to check).
- [ ] Circuit size is small compared with the wavelength, or the answer is labeled "lumped model".
- [ ] DC, steady-state AC, and transient responses are not mixed up (use $\tau$ for transients, $Z$ for sinusoidal steady state).
- [ ] KCL and KVL are satisfied on the final numbers.

Before trusting a wave or optics result:

- [ ] $f$, $\lambda$, and $v$ satisfy $v = f\lambda$ in the same medium.
- [ ] Frequency is not changed when the wave enters a new medium.
- [ ] Decibel sums use intensities (for incoherent sources), not levels.
- [ ] Paraxial and geometric-optics assumptions are stated, and feature sizes are much larger than the wavelength.
- [ ] Doppler uses the component of velocity along the line of sight.

Before trusting an orbit or propulsion result:

- [ ] All distances are from the center of the body, not altitude (add the mean radius).
- [ ] $\mu = GM$ is used, with the body's value (not $G$ times an assumed mass).
- [ ] The burn is impulsive, or gravity losses are added.
- [ ] Drag, third bodies, and oblateness are named as ignored.
- [ ] $\Delta v$ is positive; the mass ratio is greater than 1.

Before releasing a design that uses fields or magnets:

- [ ] Peak field and flux density are checked against material saturation and temperature limits.
- [ ] Eddy and skin-depth effects are estimated at the operating frequency.
- [ ] Insulation and creepage distances meet the voltage class for the project.

## Sanity checks

Orders of magnitude to catch wrong answers:

| Quantity | Expected order of magnitude |
|---|---|
| Force between two electrons 1 m apart | $2.3 \times 10^{-28}$ N electric; gravity is about $5 \times 10^{-71}$ N |
| Earth surface $g$ | about 10 m/s$^2$ |
| Speed of sound in air | about 340 m/s |
| Speed of light | $3 \times 10^8$ m/s |
| LEO period | about 90 min |
| GEO period | about 24 h |
| Earth escape speed | about 11 km/s |
| Mass ratio for a 4 km/s $\Delta v$ with $I_{\mathrm{sp}} = 350$ s | about 3.2 (so propellant is about 70 percent of initial mass) |
| Doubling sound intensity | $+3$ dB |
| Wall outlet current for a 1 kW load at 120 V | about 8.3 A |

Quick tests:

- If a result for a capacitor or inductor is in ohms with no frequency, it is wrong.
- If a rocket $\Delta v$ comes out larger than $I_{\mathrm{sp}} g_0 \ln(\text{mass ratio})$, you added terms that do not belong.
- If a wavelength in water is longer than in air for the same frequency, the index was inverted ($n = c/v$, so higher $n$ means shorter $\lambda$).
- If the circular speed at a given radius is larger than the escape speed, the formula was typed wrong ($v_e = \sqrt{2} v_c$).
- Energy stored in a capacitor should be $\frac{1}{2} C V^2$, which is a few microjoules for a 1 $\mu$F capacitor at 3 V.

## Further reference

Classic works by name:

- Griffiths, *Introduction to Electrodynamics* (undergraduate electromagnetism).
- Jackson, *Classical Electrodynamics* (graduate electromagnetism).
- Purcell and Morin, *Electricity and Magnetism*, Berkeley Physics Course, vol. 2.
- Hecht, *Optics*. Born and Wolf, *Principles of Optics* (advanced optics).
- Kinsler, Frey, Coppens, and Sanders, *Fundamentals of Acoustics*.
- Vallado, *Fundamentals of Astrodynamics and Applications*.
- Sutton and Biblarz, *Rocket Propulsion Elements*.
- Halliday, Resnick, and Walker, *Fundamentals of Physics* (general reference).
- NIST Special Publication 330, *The International System of Units (SI)*.
- NIST Special Publication 811, *Guide for the Use of the International System of Units (SI)*.
- CODATA recommended values of the fundamental physical constants (NIST), for the latest adjustment of $G$, $\varepsilon_0$, and $\mu_0$.
