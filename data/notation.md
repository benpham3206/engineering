# Notation

**Type:** data

The canonical symbols, sign conventions, and transform conventions for every formula in this repo. One symbol means one quantity, so a formula copied from one sheet to another keeps its meaning. Units are in [units](units.md); constants and their values are in [constants](constants.md).

## Scope and precedence

- This table governs every new formula entry, lesson, and reference sheet. Existing files keep their symbols until they are migrated; a migration fixes a file's conflicts one file at a time, never by a repo-wide rename.
- The `Variables:` table of an entry is the final word on what a symbol means in that entry. It may use a symbol differently from this table only as listed in [Allowed scoped overloads](#allowed-scoped-overloads).
- Where a field has a long-standing symbol that differs from this table (for example a sourced pump curve that writes volumetric flow as $Q$), reproduce the source's symbol only inside that entry and say so in its variables table.
- When this table is silent, follow ISO 80000 and the SI Brochure, and add the symbol here in the same pull request.

## Typography and operators

| Form | Use | Example |
|---|---|---|
| Italic letter | Scalar quantity or variable | $m$, $T$, $\sigma$ |
| Bold lowercase | Vector | $\mathbf{v}$, $\mathbf{F}$ is the one bold capital allowed for a force vector |
| Bold capital | Matrix or second-order tensor | $\mathbf{A}$, $\mathbf{K}$, $\boldsymbol{\sigma}$ |
| Upright subscript | A word or abbreviation | $T_{\text{max}}$, $p_{\text{atm}}$ |
| Italic subscript | An index or a variable | $x_i$, $\sigma_x$ |
| Upright text in `\text{}` | Units, always after a space | $9.81\ \text{m/s}^2$ |
| Upright two-letter name | Dimensionless group | $\mathrm{Re}$, $\mathrm{Pr}$, $\mathrm{Nu}$, $\mathrm{Ma}$ |
| Dot over a symbol | Rate with respect to time | $\dot{m}$, $\dot{Q}$, $\ddot{x}$ |
| Prime | Derivative with respect to the argument, or a state after an event | $f'(x)$, $v_1'$ |
| Hat | Unit vector, or an estimate in statistics | $\hat{\mathbf{n}}$, $\hat{\mu}$ |
| Bar | Average or centroid | $\bar{x}$, $\bar{y}$ |

- Imaginary unit: $j$, with $j^2 = -1$. Mathematics texts write $i$; this repo uses $j$ everywhere so that $i$ stays free for current and indices.
- Logarithms: $\ln$ for base $e$, $\log_{10}$ and $\log_2$ with the base written. A bare $\log$ is not used.
- Transpose $\mathbf{A}^{\mathsf{T}}$, conjugate transpose $\mathbf{A}^{\mathsf{H}}$, complex conjugate $z^{*}$, inverse $\mathbf{A}^{-1}$.
- Defined as $:=$, approximately equal $\approx$, proportional to $\propto$, of the order of $\sim$.
- Angles in equations are in radians. Degrees appear only as printed inputs or results, with the conversion shown.
- Products of units are written with a space ($\text{N m}$), quotients with a slash and at most one slash ($\text{W/(m}^2\ \text{K)}$).

## Coordinates and signs

- Cartesian axes $x$, $y$, $z$ are right-handed. Every figure or entry states which axis points up; when none is stated, $y$ is up in planar problems and $z$ is up in three-dimensional ones.
- A positive angle or moment turns counterclockwise when viewed from the positive end of its axis (the right-hand rule).
- Normal stress and strain are positive in tension.
- Shear stress $\tau_{xy}$ is positive when it acts in $+y$ on the face whose outward normal is $+x$. Mohr's circle in this repo plots positive shear downward, so that a counterclockwise rotation on the circle matches a counterclockwise rotation of the cut.
- Beam internal moment is positive when it compresses the top fibre (sagging), with $y$ up. Beam tables give magnitudes and say the direction in words.
- Pressure $p$ is absolute. Gauge pressure is written $p_g := p - p_{\text{atm}}$ and named in every entry that uses it.
- Temperature $T$ in a thermodynamic equation is absolute, in kelvin. A temperature difference may be read in kelvin or degrees Celsius, since one step is the same size.
- Heat $Q$ into a system is positive. Work $W$ done by a system on its surroundings is positive, so the first law for a closed system reads $\Delta U = Q - W$.
- Electrical power uses the passive sign convention: power absorbed by an element is positive when current enters its positive voltage terminal.
- A mass flow into a control volume is positive at an inlet; an entry that writes outflows as positive says so.

## Transform conventions

| Transform | Forward | Inverse | Notes |
|---|---|---|---|
| Laplace | $F(s) = \int_{0^-}^{\infty} f(t)\, e^{-st}\, dt$ | Inverse by tables or partial fractions | One-sided; $s$ in $\text{1/s}$; the lower limit $0^-$ keeps an impulse at $t = 0$ |
| Fourier (ordinary frequency) | $X(f) = \int_{-\infty}^{\infty} x(t)\, e^{-j 2\pi f t}\, dt$ | $x(t) = \int_{-\infty}^{\infty} X(f)\, e^{j 2\pi f t}\, df$ | No $2\pi$ factors outside the exponent; $f$ in Hz |
| Fourier series, period $T_0$ | $c_n = \frac{1}{T_0}\int_{T_0} x(t)\, e^{-j n \omega_0 t}\, dt$ | $x(t) = \sum_{n=-\infty}^{\infty} c_n\, e^{j n \omega_0 t}$ | $\omega_0 = 2\pi / T_0$ |
| Discrete Fourier transform, $N$ points | $X_k = \sum_{n=0}^{N-1} x_n\, e^{-j 2\pi k n / N}$ | $x_n = \frac{1}{N}\sum_{k=0}^{N-1} X_k\, e^{j 2\pi k n / N}$ | The $1/N$ sits on the inverse |
| Z-transform | $X(z) = \sum_{n=0}^{\infty} x_n\, z^{-n}$ | Inverse by tables or partial fractions | One-sided; sample period $T_s$ |

- Phasors use $e^{j\omega t}$: $x(t) = \mathrm{Re}\{\underline{X}\, e^{j\omega t}\}$. An underline marks a phasor or other complex amplitude.
- Every sinusoidal amplitude says whether it is root mean square or peak: $V_{\text{rms}}$, $V_{\text{pk}}$. In electrical power entries a phasor's magnitude is the root-mean-square value. In vibration entries an amplitude ($X$, $F_0$) is the peak value. The variables table states which.
- Angular frequency $\omega$ is in $\text{rad/s}$ and frequency $f$ in Hz, with $\omega = 2\pi f$. A formula never mixes them silently.

## Mathematics

| Symbol | Quantity | SI unit | Notes |
|---|---|---|---|
| $x$, $y$, $z$ | Coordinates, or generic unknowns | m, or as stated | |
| $t$ | Time | s | |
| $f(x)$ | A function | as stated | $f$ alone is frequency |
| $\mathbf{x}$, $\mathbf{b}$ | Vectors of unknowns and right-hand sides | as stated | |
| $\mathbf{A}$ | Coefficient or system matrix | as stated | |
| $\lambda$ | Eigenvalue | as stated | |
| $\kappa(\mathbf{A})$ | Condition number | dimensionless | State the norm |
| $\nabla$, $\nabla \cdot$, $\nabla \times$, $\nabla^2$ | Gradient, divergence, curl, Laplacian | 1/m per application | |
| $\delta(t)$ | Dirac delta | 1/s | |
| $H(t)$ | Unit step (Heaviside) | dimensionless | Not $u(t)$, which is a control input |
| $\varepsilon_{\text{tol}}$ | Numerical tolerance | as stated | |
| $h$ | Step size in a numerical method | as stated | Scoped overload, see below |

## Mechanics and materials

| Symbol | Quantity | SI unit | Notes |
|---|---|---|---|
| $\mathbf{F}$, $F$ | Force, and its magnitude | N | |
| $m$ | Mass | kg | |
| $\mathbf{a}$, $a$ | Acceleration | m/s$^{2}$ | |
| $\mathbf{v}$, $v$ | Velocity, and speed | m/s | |
| $g$ | Local gravitational acceleration | m/s$^{2}$ | Name the body; the Earth standard value is a constant in `data/` |
| $\theta$, $\phi$ | Angle, angle of twist | rad | |
| $\omega$, $\alpha$ | Angular velocity, angular acceleration | rad/s, rad/s$^{2}$ | |
| $M$ | Moment, bending moment | N m | |
| $\mathcal{T}$ | Torque, where temperature also appears | N m | $T$ is allowed for torque in mechanics entries with no temperature |
| $\sigma$, $\tau$ | Normal and shear stress | Pa | |
| $\varepsilon$, $\gamma$ | Normal strain, shear strain | dimensionless, rad | $\gamma$ is a scoped overload in thermofluids |
| $E$, $G$ | Young's modulus, shear modulus | Pa | |
| $\nu$ | Poisson's ratio | dimensionless | |
| $S_y$, $S_u$, $S_e$ | Yield strength, ultimate tensile strength, endurance limit | Pa | Not $\sigma_y$, which is the stress on the $y$ face |
| $A$ | Area | m$^{2}$ | |
| $I_A$, $J$ | Second moment of area, polar second moment of area | m$^{4}$ | Plain $I$ is a scoped overload |
| $I_m$ | Mass moment of inertia | kg m$^{2}$ | Plain $I$ is a scoped overload |
| $S$ | Elastic section modulus | m$^{3}$ | |
| $k_s$ | Spring stiffness | N/m | Plain $k$ is a scoped overload |
| $c$ | Viscous damping coefficient | N s/m | Also the distance to the extreme fibre in beam entries |
| $\zeta$ | Damping ratio | dimensionless | |
| $\omega_n$, $\omega_d$ | Natural and damped angular frequency | rad/s | |
| $\delta$ | Deflection or elongation | m | |
| $w$ | Distributed load | N/m | |
| $K_t$ | Stress concentration factor | dimensionless | |
| $K_I$, $K_{Ic}$ | Mode I stress intensity factor, fracture toughness | Pa m$^{1/2}$ | |
| $n_s$ | Factor of safety | dimensionless | |
| $\rho$ | Density | kg/m$^{3}$ | |

## Thermal and fluids

| Symbol | Quantity | SI unit | Notes |
|---|---|---|---|
| $T$ | Absolute temperature | K | |
| $p$, $p_g$ | Absolute pressure, gauge pressure | Pa | |
| $V$, $\dot{V}$ | Volume, volumetric flow rate | m$^{3}$, m$^{3}$/s | Not $Q$ for flow |
| $\dot{m}$ | Mass flow rate | kg/s | |
| $Q$, $\dot{Q}$ | Heat, heat rate | J, W | |
| $q$, $q''$ | Heat per unit mass, heat flux | J/kg, W/m$^{2}$ | |
| $W$, $\dot{W}$ | Work, power | J, W | $P$ is also power |
| $U$, $u$ | Internal energy, specific internal energy | J, J/kg | |
| $H$, $h$ | Enthalpy, specific enthalpy | J, J/kg | |
| $S$, $s$ | Entropy, specific entropy | J/K, J/(kg K) | |
| $c_p$, $c_v$ | Specific heat at constant pressure and volume | J/(kg K) | |
| $\gamma$ | Heat capacity ratio $c_p/c_v$ | dimensionless | Not $k$ |
| $R_u$, $R_s$ | Universal and specific gas constant | J/(mol K), J/(kg K) | Never a bare $R$ |
| $k_{\text{th}}$ | Thermal conductivity | W/(m K) | Plain $k$ is a scoped overload |
| $h_c$ | Convection coefficient | W/(m$^{2}$ K) | Plain $h$ is a scoped overload |
| $\alpha_{\text{th}}$ | Thermal diffusivity | m$^{2}$/s | |
| $\mu$, $\nu_k$ | Dynamic and kinematic viscosity | Pa s, m$^{2}$/s | Plain $\nu$ for kinematic viscosity is a scoped overload |
| $z$ | Elevation | m | |
| $f_D$ | Darcy friction factor | dimensionless | The Fanning factor is $f_D/4$ and is always labelled $f_F$ |
| $\eta$ | Efficiency | dimensionless | |
| $\epsilon_{\text{rad}}$ | Emissivity | dimensionless | |
| $\mathrm{Re}$, $\mathrm{Pr}$, $\mathrm{Nu}$, $\mathrm{Ma}$ | Reynolds, Prandtl, Nusselt, Mach numbers | dimensionless | State the length or diameter that defines each |

## Electrical and controls

| Symbol | Quantity | SI unit | Notes |
|---|---|---|---|
| $I$, $i(t)$ | Current, and its instantaneous value | A | |
| $V$, $v(t)$ | Voltage, and its instantaneous value | V | Scoped overload of volume and speed |
| $R$, $X$, $Z$ | Resistance, reactance, impedance | ohm | |
| $G$, $B$, $Y$ | Conductance, susceptance, admittance | S | |
| $C$ | Capacitance | F | |
| $L$ | Inductance | H | Scoped overload of length |
| $P$, $Q$, $S$ | Real, reactive, and apparent power | W | By convention $Q$ is written in var and $S$ in VA; both are watts dimensionally |
| $\Phi$, $B$ | Magnetic flux, flux density | Wb, T | |
| $\mathbf{E}$, $\mathbf{H}$ | Electric field, magnetic field strength | V/m, A/m | |
| $\omega$, $f$ | Angular frequency, frequency | rad/s, Hz | |
| $G_p(s)$, $G_c(s)$, $H(s)$ | Plant, controller, and sensor transfer functions | as stated | Set apart from other symbols by the argument $s$ |
| $L(s)$ | Loop transfer function $G_c G_p H$ | dimensionless | |
| $r$, $y$, $e$, $u$, $d$ | Reference, output, error $r - y$, control input, disturbance | as stated | |
| $K_p$, $K_i$, $K_d$ | Proportional, integral, and derivative gains | as stated | |
| $\mathbf{x}$, $\mathbf{A}$, $\mathbf{B}$, $\mathbf{C}$, $\mathbf{D}$ | State vector and state-space matrices | as stated | |
| $T_s$ | Sample period | s | |
| $\phi_m$, $g_m$ | Phase margin, gain margin | rad, dimensionless | Margins may be printed in degrees and decibels with the conversion shown |

## Probability and reliability

| Symbol | Quantity | SI unit | Notes |
|---|---|---|---|
| $\Pr(A)$ | Probability of event $A$ | dimensionless | Not $P$, which is power or load |
| $\mathrm{E}[X]$, $\mathrm{Var}(X)$ | Expectation and variance of $X$ | as $X$, as $X$ squared | Upright E |
| $\mu_X$, $\sigma_X$ | Mean and standard deviation of $X$ | as $X$ | The subscript may drop inside a probability entry |
| $\bar{x}$, $s_x$, $n$ | Sample mean, sample standard deviation, sample size | as $x$, as $x$, dimensionless | |
| $f(t)$, $F(t)$ | Probability density and cumulative distribution of life | 1/s, dimensionless | |
| $R(t)$ | Reliability, $1 - F(t)$ | dimensionless | Set apart from resistance by the argument $t$ |
| $h(t)$ | Hazard rate | 1/s | |
| $\lambda$ | Constant failure rate | 1/s | |
| $\beta$, $\eta_W$ | Weibull shape and scale | dimensionless, s | |
| $\mathrm{MTTF}$, $\mathrm{MTBF}$, $\mathrm{MTTR}$ | Mean time to failure, between failures, to repair | s | Hours may be printed with the conversion shown |
| $A_{\text{av}}$ | Availability | dimensionless | |

## Allowed scoped overloads

A symbol may carry the local meaning below only inside an entry whose `Variables:` table defines it, and only when the canonical meaning does not appear in the same entry.

| Symbol | Canonical meaning | Allowed local meaning | Where |
|---|---|---|---|
| $I$ | Current | Second moment of area, or mass moment of inertia | Mechanics entries with no current |
| $k$ | (none; always subscripted) | Spring stiffness, thermal conductivity, or a wave number | Entries with only one of those |
| $h$ | Specific enthalpy | Convection coefficient, height, or step size | Entries with no enthalpy |
| $T$ | Absolute temperature | Torque, or a period | Entries with no temperature |
| $V$ | Volume | Voltage, or shear force in a beam | Electrical entries; beam entries with no volume |
| $v$ | Speed | Specific volume | Thermodynamics entries with no speed |
| $P$ | Power | Axial load, or a probability written $P$ in a quoted source | Mechanics entries with no power |
| $L$ | Length | Inductance | Electrical entries with no length in the same formula |
| $\gamma$ | Heat capacity ratio | Shear strain | Solid-mechanics entries |
| $\varepsilon$ | Normal strain | Emissivity, or a numerical tolerance | Entries with no strain |
| $\mu$ | Dynamic viscosity | Friction coefficient, or a mean | Friction or probability entries with no viscosity |
| $\sigma$ | Normal stress | Standard deviation, or the Stefan-Boltzmann constant written with its key | Probability or radiation entries with no stress |
| $\nu$ | Poisson's ratio | Kinematic viscosity | Fluids entries with no Poisson's ratio |
| $\delta$ | Deflection | Logarithmic decrement, or a boundary-layer thickness | Entries with no deflection |
| $n$ | Sample size | Polytropic exponent, amount of substance, rotational speed, or refractive index | Entries with only one of those |
| $s$ | Specific entropy | Laplace variable | Controls and transform entries |
| $c$ | Damping coefficient | Distance to the extreme fibre, or the speed of light written with its key | Entries with no damping |

## Deprecated forms and redirects

New content does not use the forms on the left. Existing files are corrected as they are migrated.

| Do not write | Write | Why |
|---|---|---|
| $k$ for the heat capacity ratio | $\gamma$ | $k$ is stiffness and conductivity |
| A bare $R$ for a gas constant | $R_u$ or $R_s$ | The two differ by the molar mass |
| $Q$ for volumetric flow | $\dot{V}$ | $Q$ is heat and reactive power |
| $q$ for heat rate | $\dot{Q}$ | $q$ is heat per unit mass |
| $\sigma_y$ for yield strength | $S_y$ | $\sigma_y$ is the normal stress on the $y$ face |
| $i$ for the imaginary unit | $j$ | $i$ is current |
| A bare $\log$ | $\ln$ or $\log_{10}$ | The base changes the answer |
| Degrees inside an equation | Radians | Trigonometric series and derivatives assume radians |
| An unlabelled friction factor | $f_D$ or $f_F$ | The two differ by a factor of four |
| An unlabelled sinusoidal amplitude | A subscript rms or pk | The two differ by a factor of $\sqrt{2}$ |
| Gauge pressure written $p$ | $p_g$ | Gas laws and cavitation need absolute pressure |
| Celsius temperature inside a thermodynamic equation | Kelvin | Ratios and the gas law need absolute temperature |

## Checklist

- Every symbol in the entry appears in its `Variables:` table, with an SI unit.
- Each symbol has its canonical meaning, or an allowed scoped overload whose canonical meaning is absent from the entry.
- Vectors and matrices are bold; words in subscripts are upright.
- Angles are in radians inside equations.
- Pressure and temperature are absolute unless the entry names gauge pressure or a temperature difference.
- Every sinusoidal amplitude says rms or peak.
- The transform and phasor conventions match the table above, or the entry states the difference and converts.
- Constants are named here but valued only in [constants](constants.md).
