# Orbital mechanics reference

**Type:** reference
**Verify:** strict

Lookup sheet for the motion of a spacecraft under the gravity of one central body, the impulsive burns that change that motion, and the propellant those burns cost, for an engineer who needs a formula, a limit, or a check in the middle of mission design.

## Principles

- Gravity is a central force, so two quantities stay fixed on an unperturbed orbit: specific energy and specific angular momentum. Every closed-form orbit result follows from those two.
- Radius means distance from the center of the attracting body, never altitude. Add the body's radius to an altitude before using any formula here.
- Use the gravitational parameter $GM$ of the central body, never $G$ and the mass separately. It is known far more precisely than either.
- Orbital speed depends on position, not on the mass of the spacecraft. The same orbit serves a probe and a station.
- A burn at a point changes the orbit that passes through that point. The point stays on the new orbit, so a burn can never move the spacecraft off its current radius.
- An impulsive burn is the limit of a burn short compared with the orbit. Long burns lose delta-v to gravity and steering; the rocket equation gives the propellant, and the burn model decides the delta-v to ask for.
- Delta-v is the currency. Propellant mass grows exponentially with delta-v, so a small saving in delta-v is a large saving in mass.
- Every result here assumes two point masses (or spherical bodies). Oblateness, drag, a third body, and radiation pressure are perturbations, and each has its own entry or boundary below.
- State the central body, its $GM$, the frame, and the epoch with every state vector or element set. A set of numbers without them cannot be reproduced.
- Angles in every equation are in radians. Degrees appear only as printed inputs and results.

## Frames, epochs, and state vectors

A **frame** is a set of three perpendicular axes, with an origin, in which a position and velocity are written. The orbit equations here hold in an **inertial frame**: one that does not accelerate or rotate, so that Newton's second law holds without fictitious forces. A frame fixed to a rotating planet is not inertial; positions written in it include the planet's rotation.

An **epoch** is the instant to which a state vector or an element set refers. It is part of the data. Because every real orbit is perturbed, the elements that fit the orbit at one epoch are the **osculating** elements: the elements of the two-body orbit that would continue with the position and velocity of that instant. They drift from epoch to epoch.

- A **state vector** is position $\mathbf{r}$ (m) and velocity $\mathbf{v}$ (m/s) of the spacecraft relative to the central body, in a stated frame at a stated epoch. Six numbers fix a two-body orbit, so a state vector and a set of six classical elements carry the same information.
- A frame is fixed by naming its origin, its reference plane, and the direction of its first axis. Any named frame standard, and the time scale that dates an epoch, is a dated convention that a program must cite; this sheet names none and works in a generic inertial frame with its $z$ axis along the reference-plane normal.
- The **perifocal frame** has its $x$ axis toward periapsis and its $z$ axis along the orbit normal. Orbit shape is simplest there; the conversion section rotates to the inertial frame.
- The **local vertical local horizontal (LVLH) frame** rides with a reference spacecraft: $x$ radially outward, $y$ along the direction of motion in the orbit plane, $z$ along the orbit normal. The relative-motion section uses it.
- Convert between frames at one epoch only. A rotating-frame velocity must also remove the frame's rotation before it enters the inertial equations.
- Time-keeping at the level of relativistic clock corrections is outside this sheet; see [Modern physics and quantum mechanics](18-modern-physics-and-quantum.md).

## Two-body invariants

### Energy, angular momentum, and vis-viva

$$\mathcal{E} = \frac{v^2}{2} - \frac{GM}{r} = -\frac{GM}{2a} \qquad \mathbf{h} = \mathbf{r} \times \mathbf{v}, \quad h_{\text{am}} = r v \cos\phi_{\text{fp}} \qquad v^2 = GM\left(\frac{2}{r} - \frac{1}{a}\right)$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\mathcal{E}$ | specific orbital energy (energy per unit spacecraft mass) | $\text{m}^{2}/\text{s}^{2}$ |
| $GM$ | gravitational parameter of the central body | $\text{m}^{3}/\text{s}^{2}$ |
| $r$ | distance from the center of the central body | m |
| $v$ | speed relative to the central body | m/s |
| $a$ | semi-major axis (negative for a hyperbola) | m |
| $\mathbf{h}$ | specific angular momentum vector | $\text{m}^{2}$/s |
| $h_{\text{am}}$ | magnitude of $\mathbf{h}$ | $\text{m}^{2}$/s |
| $\phi_{\text{fp}}$ | flight-path angle, between $\mathbf{v}$ and the local horizontal | rad |

Holds when: the central body is a point mass or a sphere of uniform shells, the spacecraft mass is negligible, and no thrust, drag, or third body acts.
Breaks when: the body is oblate or lumpy, an atmosphere is present, a burn is under way, or a second large body pulls on the spacecraft. The invariants then change slowly; use perturbation methods.
Source and basis: derived from Newton's law of gravitation and the conservation of energy and angular momentum for a central force; taught in [Orbital mechanics and rockets](15-orbital-mechanics-and-rockets.md). Newtonian gravitation itself is in [Fields, waves, and space reference](reference-fields-waves-space.md#gravity-and-orbits).

Circular-orbit speed follows from $a = r$: $v_{\text{c}} = \sqrt{GM/r}$, with period $T = 2\pi\sqrt{r^3/GM}$. Example, Earth, using its $GM$ and its mean radius, a circular orbit 400 km above the surface, so $r = 6771$ km: $v_{\text{c}} = 7.673$ km/s, $T = 92.41$ min, $\mathcal{E} = -29.43$ MJ/kg, and $h_{\text{am}} = 51951$ $\text{km}^{2}$/s.

```verify
GM = q(3.98600435507e14, "m^3/s^2", of="gm_earth")
R = q(6371, "km", of="r_earth_mean")
alt = q(400, "km")
r = R + alt
expect(r, "6771 km")
vc = sqrt(GM / r)
expect(vc, "7.673 km/s")
T = 2 * pi * sqrt(r**3 / GM)
expect(T, "92.41 min")
E = -GM / (2 * r)
expect(E, "-29.43 MJ/kg")
check(abs(vc**2 / 2 - GM / r - E) < q(1, "J/kg"), "energy from speed matches energy from semi-major axis")
h = r * vc
expect(h, "51951 km^2/s")
```

## Conic trajectories

### Orbit equation, conic types, escape, and hyperbolic excess speed

$$r = \frac{p}{1 + e\cos\theta} \quad p = \frac{h_{\text{am}}^2}{GM} = a\left(1 - e^2\right) \qquad v_{\text{esc}} = \sqrt{\frac{2\,GM}{r}} \qquad v^2 = v_\infty^2 + \frac{2\,GM}{r}, \quad a = -\frac{GM}{v_\infty^2}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $r$ | distance from the center of the central body | m |
| $p$ | semi-latus rectum (orbit parameter) | m |
| $e$ | eccentricity | dimensionless |
| $\theta$ | true anomaly, angle from periapsis to the spacecraft | rad |
| $h_{\text{am}}$ | specific angular momentum magnitude | $\text{m}^{2}$/s |
| $GM$ | gravitational parameter of the central body | $\text{m}^{3}/\text{s}^{2}$ |
| $a$ | semi-major axis (negative for a hyperbola) | m |
| $v_{\text{esc}}$ | escape speed at radius $r$ | m/s |
| $v$ | speed at radius $r$ | m/s |
| $v_\infty$ | hyperbolic excess speed, the speed left far from the body | m/s |

The orbit type follows from the eccentricity, and equally from the sign of the specific energy $\mathcal{E}$:

| Conic | $e$ | $\mathcal{E}$ | $a$ |
|---|---|---|---|
| Circle | $e = 0$ | negative | $a = r$ |
| Ellipse | $0 < e < 1$ | negative | positive |
| Parabola | $e = 1$ | zero | infinite |
| Hyperbola | $e > 1$ | positive | negative |

- Periapsis radius $r_{\text{p}} = a(1 - e)$ and apoapsis radius $r_{\text{a}} = a(1 + e)$ for an ellipse. For a hyperbola $r_{\text{p}} = a(1 - e)$ is positive because $a$ is negative.
- The escape speed is the speed on the parabola at that radius, $\sqrt{2}$ times the circular speed. A spacecraft at or above it never returns.
- A hyperbola has asymptotes at true anomaly $\pm\theta_\infty$ with $\cos\theta_\infty = -1/e$. Eccentricity from the periapsis radius and excess speed: $e = 1 + r_{\text{p}} v_\infty^2 / GM$.

Holds when: the two-body assumptions of the entry above hold and the orbit is not rectilinear ($h_{\text{am}} \neq 0$).
Breaks when: near the edge of the central body's gravitational dominance, where a third body changes the energy (use the patched-conic section), or when $e$ is within rounding of 1, where $a$ is ill-conditioned (use $p$ and $r_{\text{p}}$ instead of $a$).
Source and basis: derived from solving the two-body equation of motion with conservation of $h_{\text{am}}$ and $\mathcal{E}$; taught in [Orbital mechanics and rockets](15-orbital-mechanics-and-rockets.md).

Example, Earth, from the same 400 km circular orbit: the escape speed at $r = 6771$ km is 10.85 km/s. For an excess speed of 3 km/s the hyperbola has $a = -44289$ km and, with periapsis at that radius, $e = 1.153$.

```verify
GM = q(3.98600435507e14, "m^3/s^2", of="gm_earth")
R = q(6371, "km", of="r_earth_mean")
r = R + q(400, "km")
expect(r, "6771 km")
vesc = sqrt(2 * GM / r)
expect(vesc, "10.85 km/s")
vinf = q(3, "km/s")
a = -GM / vinf**2
expect(a, "-44289 km")
e = 1 + r * vinf**2 / GM
expect(e, "1.153")
check(abs(r - a * (1 - e)) < q(1, "m"), "periapsis radius from a and e matches r")
```

## Classical orbital elements

### The six elements and the shape relations

$$a = \frac{r_{\text{p}} + r_{\text{a}}}{2} \qquad e = \frac{r_{\text{a}} - r_{\text{p}}}{r_{\text{a}} + r_{\text{p}}} \qquad p = a\left(1 - e^2\right)$$

The six **classical orbital elements** fix a two-body orbit and the position on it:

- $a$: semi-major axis, the size of the orbit.
- $e$: eccentricity, its shape.
- $i_{\text{inc}}$: inclination, the angle between the orbit normal and the reference-plane normal. Zero to $\pi$ rad; above $\pi/2$ rad the orbit is retrograde.
- $\Omega_{\text{node}}$: right ascension of the ascending node, the angle in the reference plane from the reference direction to where the orbit crosses it going up.
- $\omega_{\text{p}}$: argument of periapsis, the angle in the orbit plane from the ascending node to periapsis.
- $\theta$: true anomaly at the epoch, the angle from periapsis to the spacecraft. Mean anomaly $M$ (next section) is the usual time-linear choice.

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $a$ | semi-major axis | m |
| $e$ | eccentricity | dimensionless |
| $p$ | semi-latus rectum | m |
| $r_{\text{p}}$, $r_{\text{a}}$ | periapsis and apoapsis radius, from the body's center | m |
| $i_{\text{inc}}$ | inclination | rad |
| $\Omega_{\text{node}}$ | right ascension of the ascending node | rad |
| $\omega_{\text{p}}$ | argument of periapsis | rad |
| $\theta$ | true anomaly | rad |

Holds when: the orbit is a bound ellipse ($0 \le e < 1$) so that both apsides exist.
Breaks when: $e = 0$ (periapsis undefined, so $\omega_{\text{p}}$ and $\theta$ have no meaning separately; use the argument of latitude), $i_{\text{inc}} = 0$ or $\pi$ rad (the node is undefined), or the orbit is open. See the conversion entry for the standard fixes.
Source and basis: derived from the geometry of the ellipse; the elements are the standard parametrization taught in [Orbital mechanics and rockets](15-orbital-mechanics-and-rockets.md).

Example, Earth, perigee altitude 400 km and apogee altitude 20000 km, so $r_{\text{p}} = 6771$ km and $r_{\text{a}} = 26371$ km: $a = 16571$ km, $e = 0.5914$, $p = 10775$ km. The speeds are 9.679 km/s at perigee and 2.485 km/s at apogee, and $r v$ is the same at both, 65537 $\text{km}^{2}$/s, as constant $h_{\text{am}}$ requires.

```verify
GM = q(3.98600435507e14, "m^3/s^2", of="gm_earth")
R = q(6371, "km", of="r_earth_mean")
rp = R + q(400, "km")
ra = R + q(20000, "km")
expect(rp, "6771 km")
expect(ra, "26371 km")
a = (rp + ra) / 2
expect(a, "16571 km")
e = (ra - rp) / (ra + rp)
expect(e, "0.5914")
p = a * (1 - e**2)
expect(p, "10775 km")
vp = sqrt(GM * (2 / rp - 1 / a))
va = sqrt(GM * (2 / ra - 1 / a))
expect(vp, "9.679 km/s")
expect(va, "2.485 km/s")
expect(rp * vp, "65537 km^2/s")
check(abs(rp * vp - ra * va) < q(1, "km^2/s"), "angular momentum equal at both apsides")
```

## Anomalies and time of flight

### Kepler's equation, mean motion, and period

$$M = E - e\sin E = n_{\text{mm}}\,(t - t_{\text{p}}) \qquad n_{\text{mm}} = \sqrt{\frac{GM}{a^3}} \qquad T = \frac{2\pi}{n_{\text{mm}}} \qquad \tan\frac{\theta}{2} = \sqrt{\frac{1 + e}{1 - e}}\tan\frac{E}{2} \qquad r = a(1 - e\cos E)$$

The **mean anomaly** $M$ is the angle a point on the circle of radius $a$ would sweep at the steady mean motion; it grows in proportion to time. The **eccentric anomaly** $E$ is the auxiliary angle that links $M$ to the true anomaly. The unperturbed period depends only on $a$ and $GM$ (Kepler's third law).

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $M$ | mean anomaly | rad |
| $E$ | eccentric anomaly | rad |
| $e$ | eccentricity | dimensionless |
| $n_{\text{mm}}$ | mean motion | rad/s |
| $t$, $t_{\text{p}}$ | time and time of periapsis passage | s |
| $T$ | orbital period | s |
| $a$ | semi-major axis | m |
| $GM$ | gravitational parameter of the central body | $\text{m}^{3}/\text{s}^{2}$ |
| $\theta$ | true anomaly | rad |
| $r$ | distance from the center of the central body | m |

Solving $M \to E$ has no closed form. Newton's iteration $E_{k+1} = E_k - (E_k - e\sin E_k - M)/(1 - e\cos E_k)$ started at $E_0 = M$ converges for moderate $e$; for $e$ above about one half start at $E_0 = \pi$ rad. For a hyperbola use $M = e\sinh F - F$ with hyperbolic anomaly $F$ and $r = a(1 - e\cosh F)$, and for a parabola use Barker's equation or a universal-variable form.

Holds when: the orbit is a bound two-body ellipse. Only $M$ is linear in time.
Breaks when: $e$ is close to 1 (the iteration converges slowly and $a$ is ill-conditioned), the orbit is open (use the hyperbolic form), or perturbations make $n_{\text{mm}}$ differ from the osculating value over many revolutions. Radar-style time requirements can also need relativistic corrections.
Source and basis: derived from conservation of angular momentum (equal areas in equal times) and the geometry of the ellipse; taught in [Orbital mechanics and rockets](15-orbital-mechanics-and-rockets.md).

Example, Earth, the 400 km by 20000 km orbit above: at $E = 60$ deg, $M = 0.5350$ rad. The mean motion is $n_{\text{mm}} = 0.2960$ mrad/s, so the time since periapsis is 30.13 min, the true anomaly is 97.46 deg, and $r = 11671$ km. Three Newton steps from $E_0 = M$ land close to $E$.

```verify
GM = q(3.98600435507e14, "m^3/s^2", of="gm_earth")
R = q(6371, "km", of="r_earth_mean")
rp = R + q(400, "km")
ra = R + q(20000, "km")
a = (rp + ra) / 2
e = (ra - rp) / (ra + rp)
n = sqrt(GM / a**3)
expect(n, "0.2960 mrad/s")
E = q(60, "deg")
M = E - e * sin(E)
expect(M, "0.5350 rad")
t = M / n
expect(t, "30.13 min")
theta = 2 * atan(sqrt((1 + e) / (1 - e)) * tan(E / 2))
expect(theta, "97.46 deg")
r = a * (1 - e * cos(E))
expect(r, "11671 km")
p = a * (1 - e**2)
check(abs(r - p / (1 + e * cos(theta))) < q(1, "m"), "orbit equation agrees with eccentric-anomaly radius")
E1 = M - (M - e * sin(M) - M) / (1 - e * cos(M))
E2 = E1 - (E1 - e * sin(E1) - M) / (1 - e * cos(E1))
E3 = E2 - (E2 - e * sin(E2) - M) / (1 - e * cos(E2))
check(abs(E3 - E) < 1e-2, "three Newton steps land near E")
```

## State-vector and element conversion

### Elements to inertial position, and state to elements

Position in the inertial frame from the elements, with the argument of latitude $u = \omega_{\text{p}} + \theta$:

$$x = r\left(\cos\Omega_{\text{node}}\cos u - \sin\Omega_{\text{node}}\sin u\cos i_{\text{inc}}\right) \qquad y = r\left(\sin\Omega_{\text{node}}\cos u + \cos\Omega_{\text{node}}\sin u\cos i_{\text{inc}}\right) \qquad z = r\sin u\sin i_{\text{inc}}$$

State to elements, in the order a solver works through them:

$$\mathbf{h} = \mathbf{r}\times\mathbf{v} \qquad \mathbf{e} = \frac{1}{GM}\left[\left(v^2 - \frac{GM}{r}\right)\mathbf{r} - (\mathbf{r}\cdot\mathbf{v})\,\mathbf{v}\right] \qquad a = \frac{GM}{\dfrac{2\,GM}{r} - v^2} \qquad \cos i_{\text{inc}} = \frac{h_z}{h_{\text{am}}}$$

The node vector is $\mathbf{N} = \hat{\mathbf{z}}\times\mathbf{h}$. Then $\Omega_{\text{node}} = \operatorname{atan2}(N_y, N_x)$, $\omega_{\text{p}}$ is the angle from $\mathbf{N}$ to $\mathbf{e}$ (negative $e_z$ puts it in $(\pi, 2\pi)$), and $\theta$ is the angle from $\mathbf{e}$ to $\mathbf{r}$ (negative $\mathbf{r}\cdot\mathbf{v}$ puts it in $(\pi, 2\pi)$). The magnitude $e = |\mathbf{e}|$ and $\mathbf{e}$ points at periapsis.

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $x$, $y$, $z$ | inertial position components | m |
| $r$ | distance from the center of the central body | m |
| $\Omega_{\text{node}}$ | right ascension of the ascending node | rad |
| $i_{\text{inc}}$ | inclination | rad |
| $u$ | argument of latitude, $\omega_{\text{p}} + \theta$ | rad |
| $\omega_{\text{p}}$ | argument of periapsis | rad |
| $\theta$ | true anomaly | rad |
| $\mathbf{r}$ | position vector | m |
| $\mathbf{v}$ | velocity vector | m/s |
| $\mathbf{h}$, $h_{\text{am}}$, $h_z$ | angular momentum vector, magnitude, and $z$ component | $\text{m}^{2}$/s |
| $\mathbf{e}$ | eccentricity vector, dimensionless, pointing at periapsis | dimensionless |
| $\mathbf{N}$ | node vector | $\text{m}^{2}$/s |
| $GM$ | gravitational parameter of the central body | $\text{m}^{3}/\text{s}^{2}$ |
| $v$ | speed | m/s |
| $a$ | semi-major axis | m |

Holds when: the orbit is a two-body conic and the state is expressed in one inertial frame at one epoch.
Breaks when: the elements are singular. At $e$ near 0 the line of apsides is undefined, so use the argument of latitude or $\mathbf{e}$ components. At $i_{\text{inc}}$ near 0 or $\pi$ rad the node vector vanishes, so use the longitude of periapsis. Equinoctial or Cartesian state propagation avoids both singularities. Quadrant errors in the inverse trigonometric steps are the usual bug.
Source and basis: derived from rotating the perifocal frame to the inertial frame through $\omega_{\text{p}}$, $i_{\text{inc}}$, and $\Omega_{\text{node}}$; the vector form follows from the two-body equation of motion.

Example, Earth. A spacecraft with $r = 7000$ km, $\Omega_{\text{node}} = 40$ deg, $i_{\text{inc}} = 30$ deg, $u = 75$ deg has $x = -2376$ km, $y = 5650$ km, $z = 3381$ km, and the magnitude returns 7000 km. For the inverse, a spacecraft at $r = 7000$ km moving at 8 km/s tangentially has $h_{\text{am}} = 56000$ $\text{km}^{2}$/s, $\mathcal{E} = -24.94$ MJ/kg, $a = 7990$ km, and $e = 0.1239$.

```verify
GM = q(3.98600435507e14, "m^3/s^2", of="gm_earth")
r = q(7000, "km")
Om = q(40, "deg")
inc = q(30, "deg")
ul = q(75, "deg")
x = r * (cos(Om) * cos(ul) - sin(Om) * sin(ul) * cos(inc))
y = r * (sin(Om) * cos(ul) + cos(Om) * sin(ul) * cos(inc))
z = r * sin(ul) * sin(inc)
expect(x, "-2376 km")
expect(y, "5650 km")
expect(z, "3381 km")
expect(sqrt(x**2 + y**2 + z**2), "7000 km")
v = q(8, "km/s")
h = r * v
expect(h, "56000 km^2/s")
E = v**2 / 2 - GM / r
expect(E, "-24.94 MJ/kg")
a = -GM / (2 * E)
expect(a, "7990 km")
e = r * v**2 / GM - 1
expect(e, "0.1239")
```

## Impulsive maneuvers

### Delta-v of a tangential burn from vis-viva

$$\Delta v = \left|\,v_{\text{after}} - v_{\text{before}}\,\right| \qquad v_{\text{after}} = \sqrt{GM\left(\frac{2}{r} - \frac{1}{a_{\text{new}}}\right)}$$

An **impulsive maneuver** changes the velocity vector in zero time, so the position is unchanged and only the velocity differs. The vector change is $\Delta\mathbf{v} = \mathbf{v}_{\text{after}} - \mathbf{v}_{\text{before}}$ and its magnitude is the delta-v charged to the propellant budget. A burn along the velocity at periapsis or apoapsis changes the opposite apsis radius most efficiently, because the new orbit's speed at the burn point is set by the new $a$.

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\Delta v$ | magnitude of the velocity change | m/s |
| $v_{\text{before}}$, $v_{\text{after}}$ | speed just before and just after the burn | m/s |
| $GM$ | gravitational parameter of the central body | $\text{m}^{3}/\text{s}^{2}$ |
| $r$ | radius at the burn point | m |
| $a_{\text{new}}$ | semi-major axis of the orbit after the burn | m |

Holds when: the burn is short compared with the orbital period, thrust is along the velocity at the burn point, and the orbit stays in its plane.
Breaks when: the burn lasts a noticeable fraction of the orbit (gravity loss grows; integrate the burn or split it into several perigee burns), the thrust has a radial or out-of-plane part, or the burn point is deep in an atmosphere.
Source and basis: derived from vis-viva and the definition of an impulsive burn; taught in [Orbital mechanics and rockets](15-orbital-mechanics-and-rockets.md).

Example, Earth, from a circular orbit at 400 km altitude, raise the apoapsis to 2000 km altitude, then circularize there. The new orbit has $a_{\text{new}} = 7571$ km. The first burn at $r = 6771$ km is 395.2 m/s; the second, at $r = 8371$ km, takes the speed from 6.526 km/s to the circular 6.900 km/s, for 374.8 m/s. The total is 769.9 m/s.

```verify
GM = q(3.98600435507e14, "m^3/s^2", of="gm_earth")
R = q(6371, "km", of="r_earth_mean")
r1 = R + q(400, "km")
expect(r1, "6771 km")
r2 = R + q(2000, "km")
expect(r2, "8371 km")
a = (r1 + r2) / 2
expect(a, "7571 km")
v1 = sqrt(GM / r1)
vt1 = sqrt(GM * (2 / r1 - 1 / a))
d1 = vt1 - v1
expect(d1, "395.2 m/s")
vt2 = sqrt(GM * (2 / r2 - 1 / a))
v2 = sqrt(GM / r2)
expect(vt2, "6.526 km/s")
expect(v2, "6.900 km/s")
d2 = v2 - vt2
expect(d2, "374.8 m/s")
expect(d1 + d2, "769.9 m/s")
```

## Plane changes

### Delta-v to rotate the orbit plane

$$\Delta v = 2\,v\sin\frac{\Delta i}{2} \qquad \Delta v = \sqrt{v_1^2 + v_2^2 - 2\,v_1 v_2\cos\Delta i}$$

The first form is a pure plane change at constant speed $v$ through the angle $\Delta i$. The second is a plane change combined with a speed change from $v_1$ to $v_2$ in the same burn; it is the law of cosines on the two velocity vectors, and it is always smaller than doing the two changes separately. The burn point must be on the line where the old and new planes intersect (a node).

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\Delta v$ | magnitude of the velocity change | m/s |
| $v$, $v_1$, $v_2$ | speed at the burn point, before and after in the combined form | m/s |
| $\Delta i$ | angle between the old and new orbit planes | rad |

Holds when: the burn is impulsive, applied at a node, and the plane angle is the angle between the two velocity vectors.
Breaks when: the burn is not at a node (then it also changes $\Omega_{\text{node}}$ and $\omega_{\text{p}}$ in a coupled way), or the burn is long, or the change is large enough that combining it with other maneuvers needs a full trajectory optimization.
Source and basis: derived from the vector triangle of the two velocity vectors; taught in [Orbital mechanics and rockets](15-orbital-mechanics-and-rockets.md).

A plane change costs the most where the speed is highest, so combine it with a burn at apoapsis of a transfer orbit where the speed is lowest. Example, Earth, a circular orbit of radius 7000 km, rotated through 10 deg: $v = 7.546$ km/s and $\Delta v = 1.315$ km/s from either form.

```verify
GM = q(3.98600435507e14, "m^3/s^2", of="gm_earth")
r = q(7000, "km")
v = sqrt(GM / r)
expect(v, "7.546 km/s")
di = q(10, "deg")
d1 = 2 * v * sin(di / 2)
expect(d1, "1.315 km/s")
d2 = sqrt(v**2 + v**2 - 2 * v * v * cos(di))
expect(d2, "1.315 km/s")
```

## Hohmann and bi-elliptic transfers

### Hohmann transfer

$$\Delta v_1 = \sqrt{\frac{GM}{r_1}}\left(\sqrt{\frac{2 r_2}{r_1 + r_2}} - 1\right) \qquad \Delta v_2 = \sqrt{\frac{GM}{r_2}}\left(1 - \sqrt{\frac{2 r_1}{r_1 + r_2}}\right) \qquad t_{\text{tr}} = \pi\sqrt{\frac{a_{\text{t}}^3}{GM}}, \quad a_{\text{t}} = \frac{r_1 + r_2}{2}$$

A **Hohmann transfer** is the two-burn transfer between coplanar circular orbits along an ellipse tangent to both. It is the minimum-delta-v two-impulse transfer between them. The same formulas serve a downward transfer; the burns then retard the spacecraft and the signs of both flip.

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\Delta v_1$, $\Delta v_2$ | burn at the inner and at the outer orbit | m/s |
| $GM$ | gravitational parameter of the central body | $\text{m}^{3}/\text{s}^{2}$ |
| $r_1$, $r_2$ | radius of the inner and outer circular orbits | m |
| $t_{\text{tr}}$ | transfer time, half the transfer-ellipse period | s |
| $a_{\text{t}}$ | semi-major axis of the transfer ellipse | m |

Holds when: both orbits are circular and coplanar, burns are impulsive, and only one body attracts the spacecraft.
Breaks when: the orbits are inclined (add the plane change in the outer burn), the target is not circular, the phasing at arrival matters (the target must be at the right place when the spacecraft arrives, so a launch window exists), or the radius ratio is large (see the bi-elliptic entry below).
Source and basis: derived from vis-viva applied at the two tangent points; taught in [Orbital mechanics and rockets](15-orbital-mechanics-and-rockets.md) and summarized in [Fields, waves, and space reference](reference-fields-waves-space.md#gravity-and-orbits).

Example, Earth, from a 400 km circular orbit ($r_1 = 6771$ km) to a circular orbit of radius $r_2 = 42164$ km: $a_{\text{t}} = 24467.5$ km, $\Delta v_1 = 2.399$ km/s, $\Delta v_2 = 1.457$ km/s, total 3.857 km/s, transfer time 5.290 h.

```verify
GM = q(3.98600435507e14, "m^3/s^2", of="gm_earth")
R = q(6371, "km", of="r_earth_mean")
r1 = R + q(400, "km")
expect(r1, "6771 km")
r2 = q(42164, "km")
at = (r1 + r2) / 2
expect(at, "24467.5 km")
d1 = sqrt(GM / r1) * (sqrt(2 * r2 / (r1 + r2)) - 1)
d2 = sqrt(GM / r2) * (1 - sqrt(2 * r1 / (r1 + r2)))
expect(d1, "2.399 km/s")
expect(d2, "1.457 km/s")
expect(d1 + d2, "3.857 km/s")
t = pi * sqrt(at**3 / GM)
expect(t, "5.290 h")
```

### Bi-elliptic transfer

$$\frac{\Delta v_1}{v_{\text{c}1}} = \sqrt{\frac{2\beta}{1 + \beta}} - 1 \qquad \frac{\Delta v_2}{v_{\text{c}1}} = \frac{1}{\sqrt{\beta}}\left(\sqrt{\frac{2\rho}{\beta + \rho}} - \sqrt{\frac{2}{1 + \beta}}\right) \qquad \frac{\Delta v_3}{v_{\text{c}1}} = \frac{1}{\sqrt{\rho}}\left(\sqrt{\frac{2\beta}{\beta + \rho}} - 1\right)$$

A **bi-elliptic transfer** uses three burns: raise the apoapsis to an intermediate radius $r_{\text{b}}$ beyond the target, raise the periapsis there to the target radius, and circularize at the target. It trades extra time for lower delta-v when the radius ratio is large.

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\Delta v_1$, $\Delta v_2$, $\Delta v_3$ | the three burns, at $r_1$, $r_{\text{b}}$, and $r_2$ | m/s |
| $v_{\text{c}1}$ | circular speed at $r_1$ | m/s |
| $\beta$ | intermediate radius ratio $r_{\text{b}}/r_1$ | dimensionless |
| $\rho$ | target radius ratio $r_2/r_1$ | dimensionless |

Holds when: $r_{\text{b}} > r_2$, both end orbits are circular and coplanar, and burns are impulsive.
Breaks when: the radius ratio is below the crossover (Hohmann is cheaper at every $r_{\text{b}}$), the long coast time is unacceptable, or the far apoapsis lies outside the sphere of influence of the central body.
Source and basis: derived from vis-viva at the three burn points; the crossover is the radius ratio at which the limiting bi-elliptic transfer ($r_{\text{b}} \to \infty$) matches Hohmann, found numerically from these equations.

Example, in units of $v_{\text{c}1}$: for $\rho = 20$ and $\beta = 60$ the Hohmann total is 0.5347 and the bi-elliptic total is 0.5207, about 2.6 percent less delta-v for a much longer transfer. At the crossover $\rho = 11.94$ the two totals agree.

```verify
rho = q(20, "")
beta = q(60, "")
H = (sqrt(2 * rho / (1 + rho)) - 1) + (1 / sqrt(rho)) * (1 - sqrt(2 / (1 + rho)))
expect(H, "0.5347")
d1 = sqrt(2 * beta / (1 + beta)) - 1
d2 = (1 / sqrt(beta)) * (sqrt(2 * rho / (beta + rho)) - sqrt(2 / (1 + beta)))
d3 = (1 / sqrt(rho)) * (sqrt(2 * beta / (beta + rho)) - 1)
B = d1 + d2 + d3
expect(B, "0.5207")
given("2.6")
check(B < H, "bi-elliptic cheaper at this ratio")
rc = q(11.94, "")
Hc = (sqrt(2 * rc / (1 + rc)) - 1) + (1 / sqrt(rc)) * (1 - sqrt(2 / (1 + rc)))
Bc = (sqrt(2) - 1) * (1 + 1 / sqrt(rc))
check(abs(Hc - Bc) < 0.0001, "totals agree at the crossover ratio")
```

## Relative motion and rendezvous

### Clohessy-Wiltshire equations

$$\ddot{x} - 3n_{\text{mm}}^2 x - 2n_{\text{mm}}\dot{y} = 0 \qquad \ddot{y} + 2n_{\text{mm}}\dot{x} = 0 \qquad \ddot{z} + n_{\text{mm}}^2 z = 0$$

Closed form for initial offset $(x_0, y_0, z_0)$ and initial relative velocity $(\dot{x}_0, \dot{y}_0, \dot{z}_0)$, with $\tau = n_{\text{mm}} t$:

$$x = (4 - 3\cos\tau)\,x_0 + \frac{\sin\tau}{n_{\text{mm}}}\dot{x}_0 + \frac{2}{n_{\text{mm}}}(1 - \cos\tau)\,\dot{y}_0$$

$$y = 6(\sin\tau - \tau)\,x_0 + y_0 - \frac{2}{n_{\text{mm}}}(1 - \cos\tau)\,\dot{x}_0 + \frac{4\sin\tau - 3\tau}{n_{\text{mm}}}\dot{y}_0$$

$$z = z_0\cos\tau + \frac{\dot{z}_0}{n_{\text{mm}}}\sin\tau$$

The **Clohessy-Wiltshire equations** describe the motion of a chaser relative to a target in a circular orbit, written in the LVLH frame riding with the target: $x$ radially outward, $y$ along the direction of motion, $z$ along the orbit normal. They linearize the two-body equation about the target.

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $x$, $y$, $z$ | chaser position relative to the target: radial, along-track, cross-track | m |
| $x_0$, $y_0$, $z_0$ | initial values of $x$, $y$, $z$ | m |
| $\dot{x}$, $\dot{y}$, $\dot{z}$ | relative velocity components | m/s |
| $\ddot{x}$, $\ddot{y}$, $\ddot{z}$ | relative acceleration components | $\text{m/s}^{2}$ |
| $\dot{x}_0$, $\dot{y}_0$, $\dot{z}_0$ | initial relative velocity components | m/s |
| $n_{\text{mm}}$ | mean motion of the target's circular orbit | rad/s |
| $\tau$ | dimensionless time $n_{\text{mm}} t$ | rad |
| $t$ | time from the initial instant | s |

Holds when: the target is on a circular orbit, the separation is small compared with the orbit radius, there is no thrust or perturbation during the interval, and both spacecraft see the same central body.
Breaks when: the target orbit is eccentric (use the Tschauner-Hempel form or full propagation), the separation grows to a few percent of the orbit radius (curvature errors grow), drag differs between the two (differential drag drifts the chaser), or $J_2$ matters over many orbits.
Source and basis: derived from linearizing the two-body equation of motion in the rotating LVLH frame about a circular orbit.

Two consequences hold for any start. A bounded relative orbit with no secular along-track drift needs $\dot{y}_0 = -2n_{\text{mm}} x_0$. With any other $\dot{y}_0$ the along-track position drifts, because a different radius means a different period. Example, Earth, target at 400 km altitude ($n_{\text{mm}} = 1.133$ mrad/s, period 92.41 min), chaser 100 m above it with no relative velocity: after one orbit it has drifted -3770 m along-track. With $\dot{y}_0 = -0.2266$ m/s instead, the along-track excursion at a quarter period is -200 m and the motion stays bounded.

```verify
GM = q(3.98600435507e14, "m^3/s^2", of="gm_earth")
R = q(6371, "km", of="r_earth_mean")
r = R + q(400, "km")
n = sqrt(GM / r**3)
expect(n, "1.133 mrad/s")
expect(2 * pi / n, "92.41 min")
x0 = q(100, "m")
tau = 2 * pi
y = 6 * (sin(tau) - tau) * x0
expect(y, "-3770 m")
yd0 = -2 * n * x0
expect(yd0, "-0.2266 m/s")
tq = pi / 2
yq = 6 * (sin(tq) - tq) * x0 - (2 / n) * (1 - cos(tq)) * q(0, "m/s") + (4 * sin(tq) - 3 * tq) / n * yd0
expect(yq, "-200 m")
xq = (4 - 3 * cos(tq)) * x0 + (2 / n) * (1 - cos(tq)) * yd0
check(abs(xq) < q(1e-6, "m"), "radial offset passes through zero at a quarter period")
```

## Lambert boundary-value problem

The **Lambert problem** gives two position vectors $\mathbf{r}_1$ and $\mathbf{r}_2$, the time of flight $t_{\text{f}}$, the gravitational parameter $GM$, and the direction of travel (prograde or retrograde), and asks for the two-body orbit that joins them. Its output is the velocity $\mathbf{v}_1$ at the start and $\mathbf{v}_2$ at the end; the burns follow by subtracting the velocities on the departure and arrival orbits.

- Lambert's theorem: for a given $GM$ the time of flight depends only on the semi-major axis, the sum $r_1 + r_2$, and the chord length between the two points. The orbit plane is fixed by the two vectors unless they are collinear.
- There is no closed-form solution. Solvers reduce the problem to a single scalar equation (in the semi-major axis, or in a universal variable that spans ellipse, parabola, and hyperbola) and root-find it.
- For $N$ full revolutions before arrival there are two solutions for each feasible $N$; a solver asks for $N$ and a branch.
- The transfer angle of 180 deg makes the plane undefined, and a solver must be given a plane or fall back to a planar transfer.
- Use Lambert solvers for interplanetary and rendezvous targeting, lunar transfers, and preliminary design of arrival and departure burns. A porkchop plot is a grid of such solves over departure and arrival dates.

Holds when: the time of flight is long enough for a two-body orbit to connect the points and the central body is the only force.
Breaks when: a third body matters over the arc (use patched conics or numerical targeting), the transfer passes through the central body, or the endpoints are nearly collinear with the center. The result then seeds a numerical correction rather than ending the design.

## Perturbations

### J2 nodal regression, apsidal rotation, and the sun-synchronous condition

$$\dot{\Omega}_{\text{node}} = -\frac{3}{2}J_2\left(\frac{R_{\text{b}}}{p}\right)^{2}n_{\text{mm}}\cos i_{\text{inc}} \qquad \dot{\omega}_{\text{p}} = \frac{3}{4}J_2\left(\frac{R_{\text{b}}}{p}\right)^{2}n_{\text{mm}}\left(5\cos^2 i_{\text{inc}} - 1\right)$$

$J_2$ is the dimensionless coefficient of the body's equatorial bulge, the leading departure of the gravity field from a sphere. It makes the orbit plane rotate about the body's polar axis (**nodal regression**) and the line of apsides rotate within the plane. A **sun-synchronous orbit** has $\dot{\Omega}_{\text{node}}$ equal to the central body's mean motion about the Sun, one revolution per year, so the orbit keeps a fixed angle to the Sun; it needs $\cos i_{\text{inc}} < 0$ (retrograde), and for a given $a$ and $e$ the inclination follows from setting the first equation equal to the required rate.

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\dot{\Omega}_{\text{node}}$ | secular rate of the right ascension of the node | rad/s |
| $\dot{\omega}_{\text{p}}$ | secular rate of the argument of periapsis | rad/s |
| $J_2$ | second zonal harmonic of the central body (body-specific) | dimensionless |
| $R_{\text{b}}$ | equatorial radius of the central body | m |
| $p$ | semi-latus rectum, $a(1 - e^2)$ | m |
| $n_{\text{mm}}$ | mean motion | rad/s |
| $i_{\text{inc}}$ | inclination | rad |

Holds when: the orbit is bound and the $J_2$ term alone is dominant, averaged over one orbit.
Breaks when: drag or third-body forces are larger than the $J_2$ effect (high altitude, or very low), the orbit is near the critical inclination (where apsides stay fixed), or higher harmonics matter for precise ephemeris work. $J_2$ is body-specific; for Earth its value must come from a registered source, not this sheet.
Source and basis: derived from orbit-averaging the $J_2$ perturbing acceleration (Lagrange planetary equations). The rates scale with $a^{-7/2}$ at fixed $e$ and $i_{\text{inc}}$, because $p^{-2}$ and $n_{\text{mm}}$ each contribute.

Critical inclination: $\dot{\omega}_{\text{p}} = 0$ when $5\cos^2 i_{\text{inc}} = 1$, so $i_{\text{inc}} = 63.43$ deg (or its supplement) for any $J_2$ and any size. Example of scaling, with no value of $J_2$ needed: a circular orbit of radius 7000 km regresses at 0.7855 times the rate at radius 7500 km, same inclination. A retrograde inclination of 98 deg has $\cos i_{\text{inc}} < 0$, so $\dot{\Omega}_{\text{node}} > 0$ (eastward).

```verify
a1 = q(7000, "km")
a2 = q(7500, "km")
expect((a1 / a2)**3.5, "0.7855")
expect(acos(1 / sqrt(5)), "63.43 deg")
inc = q(98, "deg")
check(cos(inc) < 0, "retrograde inclination gives eastward regression")
```

### Atmospheric drag as a model boundary

$$a_{\text{drag}} = -\frac{1}{2}\,\frac{\rho_{\text{atm}}\,v_{\text{rel}}^2}{B}\,\hat{\mathbf{v}}_{\text{rel}} \qquad B = \frac{m}{C_D A}$$

Drag lowers the semi-major axis, so it circularizes the orbit and shortens the period until reentry. The force law above is physics; the atmospheric density $\rho_{\text{atm}}$ is not. Density varies with altitude, solar and geomagnetic activity, local time, and season, and each density model is a dated empirical model with its own error. Quote the model, its version, and the assumed activity level beside any lifetime estimate, and treat the result as an estimate to a factor of two or worse.

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $a_{\text{drag}}$ | drag acceleration | $\text{m/s}^{2}$ |
| $\rho_{\text{atm}}$ | atmospheric density at the spacecraft | $\text{kg/m}^{3}$ |
| $v_{\text{rel}}$ | speed relative to the rotating atmosphere | m/s |
| $\hat{\mathbf{v}}_{\text{rel}}$ | unit vector along the relative velocity | dimensionless |
| $B$ | ballistic coefficient | $\text{kg/m}^{2}$ |
| $m$ | spacecraft mass | kg |
| $C_D$ | drag coefficient (shape and surface dependent) | dimensionless |
| $A$ | cross-section area presented to the flow | $\text{m}^{2}$ |

Holds when: the flow is free molecular or continuum with a known $C_D$, and the density and relative velocity are known along the track.
Breaks when: the attitude changes the area, the density model is out of its range or its activity inputs are wrong, or the spacecraft spans enough altitude that density differs along it. Above all, no single density value applies for more than a short arc.
Source and basis: derived from the dynamic-pressure drag law; $C_D$ and density are empirical inputs that must be cited or measured. Drag in continuum flow is treated in [Fluid mechanics reference sheets](reference-thermofluids.md).

Example with illustrative inputs, not model output: a spacecraft of 500 kg, $C_D = 2.2$, $A = 2$ $\text{m}^{2}$ has $B = 113.6$ $\text{kg/m}^{2}$. At an illustrative density of $1 \times 10^{-12}$ $\text{kg/m}^{3}$ and a relative speed of 7.67 km/s, the drag acceleration is 0.2588 $\text{um/s}^{2}$ (a deceleration).

```verify
m = q(500, "kg")
cd = q(2.2, "")
A = q(2, "m^2")
B = m / (cd * A)
expect(B, "113.6 kg/m^2")
rho = q(1e-12, "kg/m^3")
v = q(7.67, "km/s")
a = rho * v**2 / (2 * B)
expect(a, "0.2588 um/s^2")
```

## Sphere of influence and patched conics

### Sphere of influence and the departure burn

$$r_{\text{SOI}} \approx a_{\text{p}}\left(\frac{m_{\text{s}}}{M_{\text{c}}}\right)^{2/5} \qquad \Delta v_{\text{dep}} = \sqrt{v_\infty^2 + \frac{2\,GM}{r_{\text{p}}}} - \sqrt{\frac{GM}{r_{\text{p}}}}$$

The **sphere of influence (SOI)** of a body of mass $m_{\text{s}}$ orbiting a larger body of mass $M_{\text{c}}$ at distance $a_{\text{p}}$ is the region inside which the smaller body's gravity is treated as the dominant force. A **patched-conic** trajectory uses one two-body conic inside each SOI and joins them at the boundary, matching position and velocity (after changing the origin between bodies). It gives interplanetary delta-v to a few percent and is a design tool, not a flight trajectory.

The second equation gives the burn from a circular parking orbit of radius $r_{\text{p}}$ to leave on a hyperbola of excess speed $v_\infty$, where $v_\infty$ is the vector difference between the required heliocentric velocity and the departure body's velocity, taken as a magnitude.

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $r_{\text{SOI}}$ | radius of the sphere of influence | m |
| $a_{\text{p}}$ | distance between the small body and its primary | m |
| $m_{\text{s}}$ | mass of the smaller body | kg |
| $M_{\text{c}}$ | mass of the larger (primary) body | kg |
| $\Delta v_{\text{dep}}$ | departure burn from a circular parking orbit | m/s |
| $v_\infty$ | hyperbolic excess speed | m/s |
| $GM$ | gravitational parameter of the departure body | $\text{m}^{3}/\text{s}^{2}$ |
| $r_{\text{p}}$ | parking-orbit radius, equal to the hyperbola periapsis | m |

Holds when: the mass ratio is small, the primary orbit is nearly circular, and the SOI is large compared with the departure orbit.
Breaks when: the mass ratio is not small (use three-body methods; the SOI boundary is an approximation, not a place where gravity switches), when the transfer is long enough that the arrival body moves a lot during the hyperbolic leg, or when low-energy or gravity-assist trajectories depend on both bodies' gravity at once.
Source and basis: derived from comparing the perturbing and the central accelerations of two bodies (Laplace sphere of influence); patched-conic joining is a standard approximation taught in [Orbital mechanics and rockets](15-orbital-mechanics-and-rockets.md).

Example. For a generic mass ratio $m_{\text{s}}/M_{\text{c}} = 0.01$, the SOI is 0.1585 of the orbit distance. For Earth, a parking orbit at 400 km ($r_{\text{p}} = 6771$ km) and $v_\infty = 3$ km/s (illustrative), the periapsis speed on the hyperbola is 11.26 km/s, against the circular 7.673 km/s, so the burn is 3.585 km/s.

```verify
GM = q(3.98600435507e14, "m^3/s^2", of="gm_earth")
R = q(6371, "km", of="r_earth_mean")
ratio = q(0.01, "")
expect(ratio**0.4, "0.1585")
rp = R + q(400, "km")
expect(rp, "6771 km")
vinf = q(3, "km/s")
vh = sqrt(vinf**2 + 2 * GM / rp)
vc = sqrt(GM / rp)
expect(vh, "11.26 km/s")
expect(vc, "7.673 km/s")
expect(vh - vc, "3.585 km/s")
```

## Propulsion and mass ratio

### Rocket equation and staging

$$\Delta v = v_{\text{e}} \ln\frac{m_0}{m_{\text{f}}} \qquad \Delta v_{\text{total}} = \sum_{k} v_{\text{e},k}\ln\frac{m_{0,k}}{m_{\text{f},k}}$$

The **Tsiolkovsky rocket equation** gives the velocity change of a rocket that expels propellant at constant effective exhaust speed $v_{\text{e}}$ relative to the vehicle, with no outside force. Solving for the mass ratio gives $m_0/m_{\text{f}} = e^{\Delta v / v_{\text{e}}}$, and the propellant mass is $m_0 - m_{\text{f}}$. **Staging** discards empty structure between burns; the second form adds the stage contributions, where $m_{0,k}$ is the mass at ignition of stage $k$ and $m_{\text{f},k}$ its mass at burnout before the next separation.

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\Delta v$ | velocity change from propulsion | m/s |
| $v_{\text{e}}$ | effective exhaust speed relative to the vehicle | m/s |
| $m_0$ | mass at ignition, including propellant | kg |
| $m_{\text{f}}$ | mass at burnout | kg |
| $v_{\text{e},k}$ | effective exhaust speed of stage $k$ | m/s |
| $m_{0,k}$, $m_{\text{f},k}$ | ignition and burnout mass of stage $k$ | kg |

Holds when: $v_{\text{e}}$ is constant, thrust acts along the velocity, and no gravity, drag, or other external force acts during the burn.
Breaks when: the burn is within a gravity field or atmosphere (add gravity, drag, and steering losses to the delta-v the equation must supply), the exhaust speed changes with altitude or throttle, or the burn is long enough that thrust direction rotates relative to the velocity.
Source and basis: derived from conservation of momentum for a body that sheds mass; taught in [Orbital mechanics and rockets](15-orbital-mechanics-and-rockets.md).

Example, with the standard acceleration $g_0$ converting specific impulse to speed. Required $\Delta v = 3500$ m/s with $I_{\text{sp}} = 300$ s: $v_{\text{e}} = 2942$ m/s, mass ratio 3.286. A two-stage case: stage 1 with $I_{\text{sp}} = 280$ s ignites at 100000 kg and burns out at 40000 kg, giving 2516 m/s from $v_{\text{e}} = 2746$ m/s. After jettisoning 6000 kg, stage 2 starts at 34000 kg with $I_{\text{sp}} = 340$ s, burns out at 10000 kg, and gives 4080 m/s from $v_{\text{e}} = 3334$ m/s. The total is 6596 m/s.

```verify
g0 = q(9.80665, "m/s^2", of="g_standard")
dv = q(3500, "m/s")
isp = q(300, "s")
ve = isp * g0
expect(ve, "2942 m/s")
expect(exp(dv / ve), "3.286")
ve1 = q(280, "s") * g0
expect(ve1, "2746 m/s")
dv1 = ve1 * log(q(100000, "kg") / q(40000, "kg"))
expect(dv1, "2516 m/s")
ve2 = q(340, "s") * g0
expect(ve2, "3334 m/s")
jet = q(6000, "kg")
m2 = q(40000, "kg") - jet
expect(m2, "34000 kg")
dv2 = ve2 * log(m2 / q(10000, "kg"))
expect(dv2, "4080 m/s")
expect(dv1 + dv2, "6596 m/s")
```

### Specific impulse

$$I_{\text{sp}} = \frac{F}{\dot{m}\,g_0} = \frac{v_{\text{e}}}{g_0}$$

**Specific impulse** is the thrust per unit weight flow of propellant, measured in seconds when $g_0$ is the standard acceleration 9.80665 $\text{m/s}^{2}$. The constant $g_0$ is a fixed unit-conversion factor, not the local gravity of any body, so $I_{\text{sp}}$ in seconds means the same on every planet. The effective exhaust speed $v_{\text{e}}$ includes the pressure term of a nozzle that is not perfectly expanded; the nozzle thrust equation is in [Compressible flow reference](reference-compressible-flow.md).

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $I_{\text{sp}}$ | specific impulse | s |
| $F$ | thrust | N |
| $\dot{m}$ | propellant mass flow rate | kg/s |
| $g_0$ | standard acceleration used in the definition | $\text{m/s}^{2}$ |
| $v_{\text{e}}$ | effective exhaust speed | m/s |

Holds when: thrust and flow are steady and measured under stated conditions (vacuum, or a stated back pressure).
Breaks when: quoting a sea-level value for an upper-stage mission (vacuum values are higher), mixing a thrust-over-mass-flow value with a per-weight value in another unit system, or comparing engines at different mixture ratios.
Source and basis: definition of specific impulse using the standard acceleration $g_0$; see [Orbital mechanics and rockets](15-orbital-mechanics-and-rockets.md).

Example: a thrust of 20 kN at a mass flow of 6.0 kg/s has $v_{\text{e}} = 3333$ m/s and $I_{\text{sp}} = 339.9$ s.

```verify
g0 = q(9.80665, "m/s^2", of="g_standard")
F = q(20, "kN")
md = q(6.0, "kg/s")
ve = F / md
expect(ve, "3333 m/s")
expect(ve / g0, "339.9 s")
```

## Model boundaries

The formulas above hold inside these limits. Past them a correction or a different method is required.

| Assumption | Fails when | Use instead |
|---|---|---|
| Point-mass or spherical central body | Low orbits around an oblate body | Add $J_2$ and higher zonal terms |
| Only one attracting body | Near the edge of the central body's gravitational dominance; Earth-Moon and Sun-Earth regions | Patched conics, then three-body or full numerical propagation |
| No atmosphere | Altitudes where drag decays the orbit in days to years | Cite a density model and propagate |
| Impulsive burn | Burn time is a large fraction of the orbit | Integrate the finite burn |
| Circular reference orbit (relative motion) | Eccentric target, or separation near the orbit radius | Tschauner-Hempel or nonlinear propagation |
| Constant exhaust speed | Throttled or altitude-dependent engines | Integrate with the real thrust and mass-flow histories |
| Newtonian gravity | Strong fields or high precision timing | General relativity corrections |
| Radiation pressure and tides ignored | Large area-to-mass ratio, very high orbits | Add the force models |

## Checklists

- Name the central body, its $GM$, the frame, and the epoch before using any number.
- Convert altitude to radius from the body's center. Use the correct body radius (equatorial for $J_2$, mean elsewhere) and say which.
- Check the energy sign: negative for ellipses, zero for parabolas, positive for hyperbolas. A burn that crosses zero changes the orbit type.
- Check angular momentum is the same at every point on a coasting orbit, and that vis-viva at periapsis and apoapsis recovers the same $a$.
- Confirm every angle is in radians inside the equation and that the quadrant of each inverse trigonometric result is right.
- For each burn, state where it happens, in which direction, and what plane it lives in.
- Add gravity, drag, and steering losses to the delta-v the rocket equation must supply, or state that they are excluded.
- For every perturbation result, state the density or $J_2$ source and the model version.

## Sanity checks

- A low Earth orbit has a speed near 7.7 km/s and a period near 90 minutes. A speed far outside that range at low altitude means a radius or unit error.
- Escape speed is $\sqrt{2}$ times circular speed at the same radius. Anything else is an arithmetic slip.
- The period grows as $a^{3/2}$: doubling $a$ multiplies the period by about 2.83.
- Specific energy depends on $a$ alone. Two orbits with equal $a$ have equal energy, however eccentric.
- A Hohmann transfer costs less than a bi-elliptic one at small radius ratio. If the bi-elliptic answer wins at a small ratio, recheck the inputs.
- The mass ratio $e^{\Delta v / v_{\text{e}}}$ is at least 1 and grows quickly. A delta-v about equal to the exhaust speed already needs a mass ratio of 2.7.
- Over one orbit an unperturbed spacecraft returns to the same radius and speed. A clearly different result means drag, a burn, or an error.

## Further reference

- *Fundamentals of Astrodynamics and Applications* by Vallado: algorithms for propagation, conversion, and Lambert solvers. Paid book; named by title only.
- *Fundamentals of Astrodynamics* by Bate, Mueller, and White: the classical textbook for two-body motion and orbit determination. Paid book; named by title only.
- *Orbital Mechanics for Engineering Students* by Curtis: a textbook with worked examples for this sheet's topics. Paid book; named by title only.
- [Astrodynamics (16.346), Fall 2008](https://ocw.mit.edu/courses/16-346-astrodynamics-fall-2008/) by MIT OpenCourseWare: lecture notes and problem sets on two-body orbits, transfers, and perturbations.
- [Orbital mechanics and rockets](15-orbital-mechanics-and-rockets.md): the lesson this sheet extends.
- [Fields, waves, and space reference](reference-fields-waves-space.md#gravity-and-orbits): Newtonian gravitation and a short orbit summary.
- [Compressible flow reference](reference-compressible-flow.md): nozzle thrust and exhaust speed.
- [Modern physics and quantum mechanics](18-modern-physics-and-quantum.md): relativistic clock corrections.
