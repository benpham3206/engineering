# Mechanics reference

**Type:** reference

Lookup sheet for statics, rigid-body dynamics, stress and strain, beams, columns, vibration, and second-order control, for an engineer who needs a formula, a value, or a check in the middle of a job.

## Principles

- Equilibrium comes first. A body at rest or at steady velocity has zero net force and zero net moment. If the free-body diagram does not balance, the diagram is wrong.
- Energy is conserved. Work by non-conservative forces (friction, damping, plastic deformation) is the only thing that changes total mechanical energy.
- $F = ma$ holds in an inertial frame at speeds far below light speed. Use fictitious forces in rotating frames.
- Stress is force per area on a specific cut. Strain is dimensionless change in shape. Both depend on location and orientation.
- Linear formulas hold only in the linear range: below yield, for small strains, for small deflections. Past those limits the formulas do not describe the part.
- Stiffness sets deflection. Deflection scales with load times length to a power, divided by $EI$ (beams) or $EA$ (axial). Check the scaling before trusting a number.
- Superposition is valid for linear, small-deflection problems. Add the effects of separate loads.
- Compatibility: displacements must fit together at joints and supports.
- Units and sign conventions must be consistent within one problem. Pick SI, convert once, and state the sign convention.
- A linear second-order system is set by its natural frequency and damping ratio. Those two numbers predict its response shape.

## Statics

### Free-body diagrams and equilibrium

- Draw one body, every external force and moment on it, and the reaction at every support.
- For a rigid body in 2D: $\sum F_x = 0$, $\sum F_y = 0$, $\sum M_O = 0$ (3 equations). For a particle, only the two force equations.
- For 3D rigid bodies: 6 equations, $\sum \mathbf{F} = 0$ and $\sum \mathbf{M} = 0$.
- A 2D body with 3 unknown reactions is statically determinate. More unknowns means statically indeterminate; compatibility is then needed.

Holds when: the body is rigid and at rest or moving at constant velocity, and the loads are known.
Breaks when: the body deforms significantly (use compatibility and stiffness), or it is accelerating (use Newton's second law).

### Support types and reactions

| Support | Symbol | Unknown reactions (2D) | Notes |
|---|---|---|---|
| Roller or smooth surface | | 1 (normal to surface) | Cannot resist motion along the surface |
| Link or cable (tension only) | | 1 (along the member) | Force acts along member axis |
| Pin or hinge | | 2 ($F_x$, $F_y$) | No moment resistance |
| Fixed (built-in) | | 3 ($F_x$, $F_y$, $M$) | Full restraint |
| Slider or collar on smooth rod | | 2 (normal force and moment) | Free along the rod |

- Reaction directions are assumed; a negative answer means the actual direction is opposite.

### Distributed loads

Replace a distributed load by its resultant (one force) placed at the centroid of the load diagram for the moment calculation.

| Load shape | Resultant | Location (from reference) |
|---|---|---|
| Uniform, intensity $w$ (N/m) over length $L$ | $wL$ (N) | $L/2$ from either end |
| Triangular, peak $w_0$ at one end, zero at other | $\tfrac{1}{2}w_0 L$ | $\tfrac{1}{3}L$ from the peak end; $\tfrac{2}{3}L$ from the zero end |
| Trapezoidal | Split into rectangle and triangle | Sum the parts |

Holds when: the load is in one plane and the body is rigid for equilibrium.
Breaks when: the resultant is used for internal forces in a member. Internal shear and moment need the actual load intensity.

### Trusses

Assumptions: members are straight, joints are frictionless pins, loads act only at joints, members carry axial force only.

Method of joints:

- Start at a joint with at most two unknown member forces.
- Sum forces in $x$ and $y$ at that joint. Tension is positive when the member pulls the joint.
- Move to the next joint with two unknowns.

Method of sections:

- Cut through no more than three members with unknown forces.
- Take moments about the intersection of two cut members to isolate the third force.

Zero-force member rules (for a joint with no external load):

- Two non-collinear members at a joint: both are zero force.
- Three members at a joint where two are collinear: the third is zero force.

Worked check. A triangle truss has a pin at A $(0, 0)$, a roller at B $(4, 0)$ m, and an apex C $(2, 3)$ m, with a 10 kN load down at C. By symmetry each reaction is 5 kN up.

- Member AC has length $\sqrt{13} \approx 3.606$ m. Joint A: $F_{AC} = -\tfrac{5\sqrt{13}}{3} = -6.009$ kN (compression).
- Horizontal balance at A: $F_{AB} = 10/3 = 3.333$ kN (tension).
- Method of sections check, moment about C of the left part: $5(2) - 3.333(3) = 0$. Consistent.

Holds when: the truss is statically determinate ($m + r = 2j$ for a planar pin-jointed truss, with $m$ members, $j$ joints, and $r$ support reactions; $r = 3$ for a pin plus a roller) and loads are at joints.
Breaks when: members are welded or bolted with rigidity (secondary bending), loads act between joints, or compression members buckle (check the column table below).

### Friction

Coulomb model:

$$F_f \le \mu_s N \qquad F_k = \mu_k N$$

Here $N$ is normal force (N), $\mu_s$ and $\mu_k$ are dimensionless static and kinetic coefficients. $F_k$ acts opposite to sliding.

Typical coefficients (dry, approximate, vary widely; measure for design):

| Pair | $\mu_s$ (typical) | $\mu_k$ (typical) |
|---|---|---|
| Steel on steel, dry | 0.5 to 0.8 | 0.4 to 0.6 |
| Rubber on dry concrete | 0.6 to 0.9 | 0.5 to 0.8 |
| PTFE on steel | 0.04 to 0.1 | 0.03 to 0.1 |

Belt (capstan) friction, impending slip over wrap angle $\theta$ (rad):

$$T_{\text{high}} = T_{\text{low}}\, e^{\mu\theta}$$

- Example: $\mu = 0.3$, half wrap $\theta = \pi$ gives $e^{0.3\pi} = 2.566$. Full wrap with $\mu = 0.2$ gives $e^{0.4\pi} = 3.514$ at $\theta = 2\pi$.
- At high belt speed, subtract centrifugal tension $mv^2$ (per unit belt length, $m$ in kg/m, $v$ in m/s) from both tensions before applying the formula.

Holds when: dry sliding with a single $\mu$, impending or full slip, and no lubrication.
Breaks when: lubricated, at microscopic adhesion (very clean or very flat surfaces), at high speed (friction varies with velocity), or when temperature or wear changes $\mu$.

## Section properties

Area $A$ (m^2), centroid, and second moments of area $I$ (m^4) about the centroidal axis. Polar moment $J$ (m^4) is about the centroid for circular shafts.

| Section | $A$ | $I$ about centroid | $S = I/c$ (m^3) | Other |
|---|---|---|---|---|
| Rectangle, width $b$, depth $h$ (bending about axis parallel to $b$) | $bh$ | $\dfrac{bh^3}{12}$ | $\dfrac{bh^2}{6}$ | Centroid at $h/2$ from base |
| Rectangle about its base edge | $bh$ | $\dfrac{bh^3}{3}$ | | Parallel axis at base |
| Solid circle, diameter $d$ | $\dfrac{\pi d^2}{4}$ | $\dfrac{\pi d^4}{64}$ | $\dfrac{\pi d^3}{32}$ | $J = \dfrac{\pi d^4}{32}$ |
| Hollow circle, outer $D$, inner $d_i$ | $\dfrac{\pi(D^2 - d_i^2)}{4}$ | $\dfrac{\pi(D^4 - d_i^4)}{64}$ | $\dfrac{\pi(D^4 - d_i^4)}{32D}$ | $J = \dfrac{\pi(D^4 - d_i^4)}{32}$ |

Centroid of a composite: $\bar{y} = \dfrac{\sum A_i y_i}{\sum A_i}$.

Parallel axis theorem:

$$I = I_c + A d^2$$

Here $d$ (m) is the distance between the centroidal axis and the parallel axis. Use it for each part of a composite, then add.

I-beam approximation (idealized section: two rectangular flanges of width $b$ and thickness $t_f$, one web of thickness $t_w$, overall depth $H$, clear web depth $h = H - 2t_f$):

$$I_x = \frac{bH^3 - (b - t_w)h^3}{12} \qquad A \approx 2bt_f + t_w h$$

- Example: $H = 200$ mm, $b = 100$ mm, $t_f = 10$ mm, $t_w = 6$ mm. Then $h = 180$ mm, $I_x = 2.10 \times 10^7$ mm^4 ($2098$ cm^4), $A = 3080$ mm^2.
- Root fillets and rolled tolerances are ignored. Use catalog values for a real rolled shape.

Holds when: the shape is idealized and the flanges are rectangular.
Breaks when: the section is thin-walled and open (use shear flow and torsion constant), or the real shape has fillets and tapers that are not small.

## Dynamics

### Kinematics

Constant acceleration in one direction:

$$v = v_0 + at \qquad x = x_0 + v_0 t + \tfrac{1}{2}at^2 \qquad v^2 = v_0^2 + 2a(x - x_0)$$

Here $x$ (m), $v$ (m/s), $a$ (m/s^2), $t$ (s).

Holds when: acceleration is constant along the path.
Breaks when: acceleration varies (integrate), or motion is curved (use normal and tangential components).

### Newton's second law

$$\sum \mathbf{F} = m\mathbf{a} \qquad \sum M_G = I_G \alpha \quad (\text{rotation about the centre of mass})$$

Holds when: inertial frame, $v \ll c$, and the body mass is constant.
Breaks when: mass changes (rockets: use $F = \dot{m}v$ terms), relativistic speeds, or non-inertial frames without fictitious forces.

### Work and energy

$$W_{\text{net}} = \Delta K \qquad K = \tfrac{1}{2}mv^2$$

With non-conservative work (friction, damping):

$$K_1 + U_1 + W_{\text{nc}} = K_2 + U_2$$

- Gravity near a surface: $U = mgh$, with $g$ the local gravitational acceleration. Earth: $g = 9.81$ m/s^2 (typical).
- Spring: $U = \tfrac{1}{2}kx^2$.

Holds when: forces are known and the work of each force is computable.
Breaks when: forces depend on time in a way that is not a potential (use the impulse form), or there is internal energy loss that you have not accounted for.

### Impulse and momentum

$$\int_{t_1}^{t_2} \sum \mathbf{F}\,dt = m\mathbf{v}_2 - m\mathbf{v}_1 \qquad \sum \mathbf{p} \text{ conserved if } \sum \mathbf{F}_{\text{ext}} = 0$$

Units: impulse and momentum in N s = kg m/s.

Holds when: the impulse is over a finite time and the system is clearly defined.
Breaks when: the force is internal to the system (it does not change total momentum), or the collision is between a body and a field that is not part of the system.

Coefficient of restitution (1-D collision, velocities after $v'$, before $v$): $e = \dfrac{v_2' - v_1'}{v_1 - v_2}$. $e = 1$ for a perfectly elastic collision, $e = 0$ for perfectly plastic (bodies stick).

### Rotation

- Angular position $\theta$ (rad), velocity $\omega$ (rad/s), acceleration $\alpha$ (rad/s^2).
- Rolling without slip on a surface: $v_G = \omega r$, $a_G = \alpha r$.
- Rotational kinetic energy about the centre: $K_{\text{rot}} = \tfrac{1}{2}I_G \omega^2$.
- Total planar kinetic energy: $K = \tfrac{1}{2}m v_G^2 + \tfrac{1}{2}I_G \omega^2$.
- For a fixed axis $O$ in 2D: $\sum M_O = I_O \alpha$, with $I_O$ about the same axis.

Holds when: planar motion, rigid body, rolling without slip where stated.
Breaks when: 3D rotation (inertia becomes a tensor and $\omega$ and angular momentum may not align), or slipping (friction work changes the rolling relation).

Worked result. A 10 kg solid disk of radius 0.3 m, pulled with a horizontal 50 N force at its centre and rolling without slip, has $a_G = F / (\tfrac{3}{2}m) = 3.33$ m/s^2. It needs friction of 16.7 N, so $\mu_s \ge 0.17$ on a dry floor with $N = 98.1$ N.

### Mass moments of inertia (typical formulas, body mass $m$)

| Body | Axis | $I$ (kg m^2) |
|---|---|---|
| Thin rod, length $L$ | Through centre, perpendicular to rod | $\dfrac{mL^2}{12}$ |
| Thin rod, length $L$ | Through one end, perpendicular to rod | $\dfrac{mL^2}{3}$ |
| Solid disk or solid cylinder, radius $r$ | Central axis of symmetry | $\dfrac{mr^2}{2}$ |
| Solid disk, radius $r$ | Diameter (in its plane) | $\dfrac{mr^2}{4}$ |
| Ring or thin hoop, radius $r$ | Central axis (perpendicular to plane) | $mr^2$ |
| Ring or thin hoop, radius $r$ | Diameter (in its plane) | $\dfrac{mr^2}{2}$ |
| Solid sphere, radius $r$ | Any diameter | $\dfrac{2mr^2}{5}$ |
| Thin spherical shell, radius $r$ | Any diameter | $\dfrac{2mr^2}{3}$ |

- Parallel axis: $I = I_G + md^2$ with $d$ in metres.
- Radius of gyration $k = \sqrt{I/m}$ (m). A body behaves as if all its mass were at distance $k$ from the axis.

Holds when: uniform density and the axis passes through the stated location.
Breaks when: density varies, the body has holes or cutouts (subtract), or the body is not one of the listed shapes (integrate).

## Stress and strain

Definitions:

$$\sigma = \frac{F}{A} \quad (\text{Pa}) \qquad \tau = \frac{V}{A} \quad (\text{Pa}) \qquad \varepsilon = \frac{\delta}{L} \quad (\text{dimensionless}) \qquad \gamma = \frac{\Delta x}{h} \quad (\text{rad})$$

Typical elastic properties (metals, room temperature; standard textbook values):

| Material | $E$ (GPa, typical) | $\nu$ (typical) | $\sigma_y$ (MPa, typical, structural) |
|---|---|---|---|
| Structural steel | 200 | 0.30 | 250 |
| Aluminum alloy | 70 | 0.33 | 100 to 300 (alloy-dependent) |
| Titanium alloy (Ti-6Al-4V) | 110 | 0.34 | 880 |

- Shear modulus: $G = \dfrac{E}{2(1 + \nu)}$. Steel $G \approx 77$ GPa.
- Hooke's law (linear elastic): $\sigma = E\varepsilon$, $\tau = G\gamma$.

Holds when: linear elastic (stress below yield; yield is near 0.2 percent strain for most structural metals), small strain, uniform material.
Breaks when: stress exceeds yield, the material is anisotropic (composites, wood, rolled sheets), the part is above its creep temperature, or the strain is large.

### Axial loading

$$\sigma = \frac{P}{A} \qquad \delta = \frac{PL}{AE}$$

- $P$ is axial force (N). Tension positive.
- For a stepped bar, sum $PL/(AE)$ over segments.

Holds when: the load acts through the centroid and the section is uniform away from ends.
Breaks when: holes, fillets, and grooves raise the peak stress (use $K_t$, stress concentration factor), or the bar is short and fat (end effects).

### Torsion of circular shafts

$$\tau = \frac{Tr}{J} \qquad \tau_{\max} = \frac{Tc}{J} \qquad \phi = \frac{TL}{GJ}$$

- $T$ torque (N m), $r$ distance from the axis (m), $c$ outer radius (m), $\phi$ angle of twist (rad).
- Example: hollow shaft $D = 50$ mm, $d_i = 40$ mm, $T = 1.2$ kN m, $L = 1.5$ m, $G = 80$ GPa gives $\tau_{\max} = 82.8$ MPa and $\phi = 3.56$ degrees.

Holds when: circular cross section, linear elastic, torque applied at ends.
Breaks when: non-circular sections (warping, use torsion constant $J_t$ and different formulas), thin-walled open sections, or yielding.

### Bending and transverse shear

Flexure (normal stress):

$$\sigma = \frac{My}{I} \qquad \sigma_{\max} = \frac{Mc}{I} = \frac{M}{S}$$

- $M$ moment (N m), $y$ distance from neutral axis (m), $c$ distance to extreme fibre (m).

Transverse shear stress (beams):

$$\tau = \frac{VQ}{Ib}$$

- $V$ shear force (N), $Q = \int y\, dA$ first moment of area above the cut (m^3), $b$ width at the cut (m).
- Rectangle: $\tau_{\max} = \dfrac{3V}{2A}$ at the neutral axis.
- Circle: $\tau_{\max} = \dfrac{4V}{3A}$.

Holds when: slender beam (span over depth roughly 10 or more), prismatic, plane sections stay plane, linear elastic.
Breaks when: deep or short beams (shear is significant; use shear deformation or Timoshenko theory), thin-walled sections (shear flow), or stress concentrations at supports and load points.

### Thin-walled pressure vessels

Rule of thumb: thin wall when $t/r \le 0.1$ (inner radius $r$, wall thickness $t$). Use the stresses below only in that range.

Cylinder with internal pressure $p$ (Pa):

$$\sigma_{\text{hoop}} = \frac{pr}{t} \qquad \sigma_{\text{long}} = \frac{pr}{2t}$$

Sphere:

$$\sigma = \frac{pr}{2t}$$

- Example: $p = 2$ MPa, $r = 500$ mm, $t = 10$ mm. Hoop stress 100 MPa; longitudinal and sphere stress 50 MPa.
- The hoop stress is the design-governing stress for cylinders.

Holds when: $t/r \le 0.1$, internal pressure only, no end-cap or nozzle effects.
Breaks when: thick walls (use Lame equations), local stresses at nozzles, supports, and head-to-shell joints, and external pressure (buckling governs).

### Mohr's circle and principal stresses

Plane stress with normal stresses $\sigma_x$, $\sigma_y$ and shear $\tau_{xy}$:

$$\sigma_{\text{avg}} = \frac{\sigma_x + \sigma_y}{2} \qquad R = \sqrt{\left(\frac{\sigma_x - \sigma_y}{2}\right)^2 + \tau_{xy}^2}$$

$$\sigma_1 = \sigma_{\text{avg}} + R \qquad \sigma_2 = \sigma_{\text{avg}} - R \qquad \tau_{\max} = R$$

Principal angle (measured from $x$):

$$\tan 2\theta_p = \frac{2\tau_{xy}}{\sigma_x - \sigma_y}$$

- Example: $\sigma_x = 80$, $\sigma_y = 20$, $\tau_{xy} = 30$ MPa. $\sigma_{\text{avg}} = 50$, $R = 42.43$ MPa, $\sigma_1 = 92.43$ MPa, $\sigma_2 = 7.57$ MPa, $\tau_{\max} = 42.43$ MPa, $\theta_p = 22.5$ degrees. Substitution at $\theta = 22.5$ degrees reproduces $\sigma_1$.
- Sign convention for $\tau$ must match the text you use. Check by substitution.

Holds when: plane stress (one principal stress is zero or negligible).
Breaks when: 3D stress (use all three principal stresses), or when the Mohr circle is drawn with the wrong $\tau$ sign convention.

### Combined loading and failure criteria

- Superpose normal stresses from axial, bending, and pressure at each point: $\sigma = \dfrac{P}{A} \pm \dfrac{Mc}{I}$.
- Superpose shear from torsion and transverse load, then find principal stresses.
- Ductile yield, plane stress (von Mises, distortion energy):

$$\sigma_{vm} = \sqrt{\sigma_x^2 - \sigma_x\sigma_y + \sigma_y^2 + 3\tau_{xy}^2}$$

- Example above: $\sigma_{vm} = 88.9$ MPa. Factor of safety against yield is $\sigma_y / \sigma_{vm}$.
- Tresca (maximum shear): $\tau_{\max} = (\sigma_1 - \sigma_2)/2$, more conservative than von Mises.

Holds when: ductile material, static load, yield is the failure mode.
Breaks when: brittle materials (use maximum normal stress or Mohr-Coulomb), fatigue (use a fatigue criterion such as Goodman or Soderberg), or buckling and fracture-mechanics failures.

## Beams

Deflection and moment formulas for prismatic beams, linear elastic, small slope. $E$ in Pa, $I$ in m^4, $L$ in m.

| Case | Max moment | Location | Max deflection | Location |
|---|---|---|---|---|
| Cantilever, end load $P$ | $PL$ | Fixed end | $\dfrac{PL^3}{3EI}$ | Free end |
| Cantilever, uniform load $w$ | $\dfrac{wL^2}{2}$ | Fixed end | $\dfrac{wL^4}{8EI}$ | Free end |
| Simply supported, centre load $P$ | $\dfrac{PL}{4}$ | Centre | $\dfrac{PL^3}{48EI}$ | Centre |
| Simply supported, uniform load $w$ | $\dfrac{wL^2}{8}$ | Centre | $\dfrac{5wL^4}{384EI}$ | Centre |
| Fixed-fixed, uniform load $w$ | $\dfrac{wL^2}{12}$ hogging at supports, $\dfrac{wL^2}{24}$ sagging at centre | Supports and centre | $\dfrac{wL^4}{384EI}$ | Centre |

- Superposition: add the deflection and moment from each load at the same point.
- Sanity: fixed-fixed deflection under uniform load is one fifth of the simply supported value, because $1/384$ versus $5/384$.
- Example: simply supported 4 m span, $w = 10$ kN/m, rectangle $100 \times 200$ mm, $E = 200$ GPa gives $M_{\max} = 20$ kN m, $\sigma_{\max} = 30$ MPa, $\delta_{\max} = 2.50$ mm.

Holds when: linear elastic, small deflections, slender beams, and the support conditions match the table.
Breaks when: the beam is short (add shear deflection), the support is not ideal (a real pin or fixed support may partly rotate), or the deflection is large (geometric nonlinearity).

## Column buckling

Euler critical load for a straight, slender, elastic column with effective length $KL$:

$$P_{cr} = \frac{\pi^2 EI}{(KL)^2} \qquad \sigma_{cr} = \frac{\pi^2 E}{(KL/r)^2} \qquad r = \sqrt{\frac{I}{A}}$$

Here $P_{cr}$ is in N, $E$ in Pa, $I$ the smallest second moment of area in m^4, $L$ in m, $r$ the radius of gyration in m.

| End condition | $K$ (ideal) | Shape of buckled column |
|---|---|---|
| Pinned-pinned | 1.0 | Half sine wave |
| Fixed-fixed | 0.5 | Inflection points at quarter lengths |
| Fixed-pinned | 0.7 (0.699) | One inflection point |
| Fixed-free (cantilever column) | 2.0 | Quarter sine wave |

- Example: solid rod, $d = 25$ mm, $L = 1.8$ m, $E = 200$ GPa. $P_{cr}$ = 11.7 kN (pinned), 23.8 kN (fixed-pinned), 46.7 kN (fixed-fixed), 2.92 kN (cantilever). The critical stress for the pinned case is 23.8 MPa.
- Transition slenderness below which Euler does not apply (column yields first): $(KL/r)_t = \pi\sqrt{E/\sigma_y}$. Steel ($E = 200$ GPa, $\sigma_y = 250$ MPa) gives about 89. The example rod has $KL/r = 288$, so Euler applies.

Holds when: the column is straight, centrally loaded, slender ($KL/r$ above the transition value), elastic, with ideal end conditions.
Breaks when: stocky columns (use inelastic or empirical column curves), eccentric loading (secant formula), imperfections, or real end conditions that are partly restrained (use a $K$ between the ideal values, and be conservative).

## Vibrations

Single-degree-of-freedom spring-mass-damper:

$$m\ddot{x} + c\dot{x} + kx = F(t)$$

Units: $m$ kg, $c$ N s/m, $k$ N/m, $F$ N.

Natural frequency and damping ratio:

$$\omega_n = \sqrt{\frac{k}{m}} \quad (\text{rad/s}) \qquad f_n = \frac{\omega_n}{2\pi} \quad (\text{Hz}) \qquad \zeta = \frac{c}{c_{cr}} = \frac{c}{2\sqrt{km}}$$

- $\zeta < 1$ underdamped (rings), $\zeta = 1$ critically damped, $\zeta > 1$ overdamped.
- Damped frequency (underdamped): $\omega_d = \omega_n\sqrt{1 - \zeta^2}$.
- Example: $m = 2$ kg, $k = 800$ N/m, $c = 8$ N s/m gives $\omega_n = 20$ rad/s, $\zeta = 0.10$, $\omega_d = 19.9$ rad/s.

Logarithmic decrement (free decay, underdamped; $x_n$ and $x_{n+1}$ successive peaks):

$$\delta = \ln\frac{x_n}{x_{n+1}} = \frac{2\pi\zeta}{\sqrt{1 - \zeta^2}} \qquad \zeta = \frac{\delta}{\sqrt{4\pi^2 + \delta^2}}$$

- Example: $\zeta = 0.10$ gives $\delta = 0.6315$.

Steady harmonic response, $F = F_0\cos\omega t$, $X_0 = F_0/k$, $r = \omega/\omega_n$:

$$\frac{X}{X_0} = \frac{1}{\sqrt{(1 - r^2)^2 + (2\zeta r)^2}}$$

- At $r = 1$: $X/X_0 = 1/(2\zeta)$. Exact peak at $r = \sqrt{1 - 2\zeta^2}$ with magnification $\dfrac{1}{2\zeta\sqrt{1 - \zeta^2}}$.

Transmissibility (force transmitted to the support, or displacement transmitted from a moving base; same expression):

$$TR = \sqrt{\frac{1 + (2\zeta r)^2}{(1 - r^2)^2 + (2\zeta r)^2}}$$

- Example: $\zeta = 0.10$, $r = 2$: $TR = 0.356$ (isolation works). $r = 0.5$: $TR = 1.328$ (amplified).
- Isolation is effective only for $r > \sqrt{2}$. Lower damping helps isolation at high $r$ and hurts it near resonance.

Holds when: linear spring and viscous damper, single degree of freedom, small motion, steady state (transients gone).
Breaks when: nonlinear stiffness or damping (amplitude-dependent frequency), dry (Coulomb) friction, multiple modes near each other, or time-varying mass or stiffness.

## Second-order step metrics

Standard second-order system with unity DC gain:

$$G(s) = \frac{\omega_n^2}{s^2 + 2\zeta\omega_n s + \omega_n^2}$$

Step-response metrics for underdamped ($0 < \zeta < 1$):

| Metric | Formula | Notes |
|---|---|---|
| Overshoot | $M_p = \exp\!\left(-\dfrac{\zeta\pi}{\sqrt{1 - \zeta^2}}\right)$ | As a fraction of final value; multiply by 100 for percent |
| Peak time | $t_p = \dfrac{\pi}{\omega_d}$ | First peak |
| Rise time, 0 to 100 percent | $t_r = \dfrac{\pi - \arccos\zeta}{\omega_d}$ | The 10 to 90 percent rise time is shorter; simulate it if the spec uses that definition |
| Settling time, 2 percent | $t_s \approx \dfrac{4}{\zeta\omega_n}$ | Envelope estimate |
| Settling time, 5 percent | $t_s \approx \dfrac{3}{\zeta\omega_n}$ | Envelope estimate |

Overshoot for common damping ratios (computed):

| $\zeta$ | $M_p$ (percent) | $\omega_n t_p$ | $\omega_n t_r$ (0 to 100 percent) |
|---|---|---|---|
| 0.1 | 72.9 | 3.16 | 1.68 |
| 0.3 | 37.2 | 3.29 | 1.97 |
| 0.5 | 16.3 | 3.63 | 2.42 |
| 0.707 | 4.3 | 4.44 | 3.33 |

- Example: $\zeta = 0.3$, $\omega_n = 10$ rad/s. $M_p = 37.2$ percent, $t_p = 0.329$ s, $t_r = 0.197$ s (0 to 100 percent). Simulated 10 to 90 percent rise time is 0.132 s. The envelope estimate $4/(\zeta\omega_n) = 1.33$ s for 2 percent settling is conservative; a simulation gives 1.12 s. The 5 percent estimate $3/(\zeta\omega_n) = 1.0$ s agrees with a simulated 1.01 s.
- $\zeta \approx 0.707$ is a common design target: low overshoot with reasonable speed.
- At $\zeta = 1$ or more, there is no overshoot; use the real-root time constants instead.

Holds when: the closed loop is well approximated by a second-order system (dominant poles, no zeros nearby, linear).
Breaks when: a zero is near the poles (it adds overshoot), there is dead time or a third pole nearby, or the system is nonlinear (saturation, friction). The overshoot formula is only for a step input.

## PID effects

Ideal PID: $u(t) = K_p e + K_i \int e\,dt + K_d\,\dfrac{de}{dt}$, error $e = r - y$.

Qualitative effects of increasing each gain alone (typical; interactions exist):

| Gain | Rise time | Overshoot | Settling | Steady error | Stability margin | Noise sensitivity |
|---|---|---|---|---|---|---|
| $K_p$ up | Faster | Up | Usually faster, then oscillatory | Down (not removed for a type-0 plant) | Down | Slight |
| $K_i$ up | Slightly faster | Up | Slower (slow tail) | Removed for step input | Down | Slight |
| $K_d$ up | Slightly slower | Down | Faster if well damped | No direct effect | Up | Up (amplifies noise) |

Holds when: the plant is linear and roughly second-order or first-order, the measurement is clean, and the loop has modest delay.
Breaks when: derivative acts on noisy measurement (filter it), integral windup occurs at actuator saturation (clamp or back-calculate), or the loop has significant dead time (the PID gains that work on paper will oscillate in the real plant).

Example (first-order plant, $K = 2$, $\tau = 0.5$ s, P-only, unity feedback, $K_p = 4$): closed-loop gain $K_{cl} = 0.889$, steady error $e_{ss} = 1/(1 + K_pK) = 0.111$, closed-loop time constant $\tau/(1 + K_pK) = 0.0556$ s. A P-only loop leaves steady error for a step; adding $K_i$ removes it.

## Checklists

Statics and equilibrium:

- Free-body diagram drawn for each body, all external forces and reactions.
- Support types match the reactions drawn (roller 1, pin 2, fixed 3).
- Distributed loads replaced by resultants at the correct location.
- Equations count equals unknowns; determinacy checked.
- Units consistent (N or lbf, not a mix); sign convention stated.
- Friction direction opposes slip; static friction solved from equilibrium, then compared with $\mu_s N$.

Truss analysis:

- Joints checked for zero-force members.
- Sum of joint forces and reactions closes at a second joint or by a section.
- Compression members checked for buckling with the correct $K$.

Stress and deflection:

- Stress computed at the critical point, not just the average.
- Peak stress checked against $K_t$ at holes, fillets, and grooves.
- Elastic formulas used only below yield; factor of safety reported.
- Deflection checked against the serviceability limit separately from stress.
- Moment of inertia about the correct axis (the weakest axis for buckling).

Vibration and control:

- Natural frequency computed in rad/s and converted to Hz only when needed.
- Damping ratio uses the square root in $c_{cr} = 2\sqrt{km}$.
- Excitation frequency checked against $\omega_n$ (resonance band).
- Step response reported with overshoot, rise time, and settling time under the stated criterion.
- Stability checked before adding integral or derivative gain.

## Sanity checks

- Earth gravity is about 9.81 m/s^2 (typical, varies from about 9.78 to 9.83 with latitude and altitude). Use $g$ local for other bodies.
- $1$ MPa $= 10^6$ N/m^2. In US units, 1 MPa is about 145 psi.
- Steel at 200 MPa carries strain $200 \times 10^6 / 200 \times 10^9 = 1 \times 10^{-3}$. That is 1 mm per metre.
- Kinetic energy of 1 kg at 1 m/s is 0.5 J. A 1 kg object at 10 m/s carries 50 J.
- Stress on a 1 cm^2 area of 1 MPa corresponds to 100 N of force.
- Shear yield of a ductile metal is about 0.58 times its tensile yield (von Mises, $\sigma_y/\sqrt{3}$). Tresca gives 0.5.
- For steel, a column with $KL/r$ above about 89 (the transition value) is Euler-governed; below it, Euler overpredicts the load.
- Damping ratio of most structures is roughly 0.01 to 0.05 (typical), so resonance peaks are large unless damping is added.
- An overshoot above 50 percent corresponds to $\zeta$ below about 0.2 for a second-order loop.
- A deflection that scales as $L^4$ doubles by a factor 16 if the span doubles. Check whether your answer does.

## Further reference

Named books and standards only (no links). Check current editions before relying on a value.

- Roark's Formulas for Stress and Strain, Young and Budynas (paid, classic beam and plate tables).
- Shigley's Mechanical Engineering Design, Budynas and Nisbett (paid, machine design with failure criteria).
- Mechanics of Materials, Hibbeler (paid, stress, strain, beams, columns).
- Vector Mechanics for Engineers: Statics and Dynamics, Beer and Johnston (paid).
- Engineering Mechanics: Statics and Dynamics, Hibbeler (paid).
- Mechanics of Materials, Timoshenko and Gere (paid, classic derivations of buckling and beams).
- Mechanical Vibrations, Den Hartog (paid, Dover reprint available, vibration and transmissibility).
- Modern Control Engineering, Ogata (paid, step response, PID).
- Feedback Control of Dynamic Systems, Franklin, Powell, and Emami-Naeini (paid, feedback and step metrics).
- Machinery's Handbook (paid, values and reference tables for design work).
- AISC 360, Specification for Structural Steel Buildings (standard, check the current edition for column and beam design).
