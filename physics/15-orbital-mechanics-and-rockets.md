# Orbital mechanics and rockets

**Type:** lesson

Orbital mechanics predicts how a spacecraft moves under gravity, and rocket equations predict how much propellant it takes to change that motion. Together they tell an engineer whether a mission is possible and how large the rocket must be.

**Prerequisites:** [Particle dynamics](02-particle-dynamics.md), [Thermodynamics: properties, work, heat, and the first law](08-thermo-first-law.md), [Trigonometry](../math/02-trigonometry.md)
**Time:** 10-14 h

## Core ideas

- **Newton's law of gravitation** says two point masses attract each other with force $F = G m_1 m_2 / r^2$. Here $G = 6.674 \times 10^{-11}$ $\mathrm{N\,m^2/kg^2}$ is the gravitational constant (a standard measured value), masses are in kilograms (kg), and $r$ is the distance between the centers of the bodies, in meters (m).
- Engineers combine $G$ and a planet's mass $M$ into one number, the gravitational parameter $\mu = GM$. Earth's value is $\mu_\oplus = 3.986004418 \times 10^{14}$ $\mathrm{m^3/s^2}$. Using $\mu$ means you rarely need $G$ and $M$ separately.
- **Radius means distance from the planet's center**, not from its surface. For an orbit at altitude $h$ above a planet of radius $R$, the radius is $r = R + h$. Mixing these up is the most common error in this topic.
- **Circular orbit.** Gravity supplies the centripetal force that keeps the object turning. Setting $m v^2 / r = m \mu / r^2$ gives $v = \sqrt{\mu / r}$. The speed depends only on radius, not on the object's mass.
- **Escape velocity** is the speed an object needs to climb from radius $r$ to infinitely far away with zero speed left over. It equals $\sqrt{2}$ times the circular speed at the same radius.
- **Kepler's laws** describe planetary and satellite orbits:
  - First law: orbits are ellipses, with the central body at one focus.
  - Second law: a line from the central body to the orbiting object sweeps out equal areas in equal times. The object moves fastest at its closest point (perigee) and slowest at its farthest point (apogee).
  - Third law: the square of the orbital period is proportional to the cube of the semimajor axis, $T^2 \propto a^3$. The exact form is in the equations below.
- **Semimajor axis** $a$ is half the longest diameter of an ellipse. For a circle, $a$ equals the radius.
- **Vis-viva equation** gives the speed at any point on any orbit from energy conservation: $v^2 = \mu(2/r - 1/a)$. For a circle, $a = r$ and the formula reduces to the circular speed.
- **Orbital energy** per unit mass is $\varepsilon = v^2/2 - \mu/r$. For any orbit, this equals $-\mu / (2a)$. Bound orbits have negative energy. A burn that adds speed at one point raises the energy and enlarges the orbit.
- **Delta-v** ($\Delta v$) is the change in velocity that a burn produces. Mission planners set a delta-v budget for each mission. Burns are usually modeled as instantaneous (impulsive), which is accurate when the burn is short compared with the orbit.
- **Hohmann transfer** is a low-cost two-burn transfer between two circular, coplanar orbits. The first burn at perigee of the transfer ellipse raises the apogee to the target radius. The second burn at apogee circularizes the orbit. The transfer ellipse has semimajor axis $a_t = (r_1 + r_2)/2$.
- **Rocket equation (Tsiolkovsky).** A rocket pushes by throwing mass backward. Conservation of momentum gives $\Delta v = v_e \ln(m_0 / m_f)$. Here $v_e$ is the exhaust speed relative to the rocket, $m_0$ is the starting mass including propellant, and $m_f$ is the mass left after the burn. Because the mass ratio sits inside a logarithm, each extra unit of delta-v costs more propellant as the rocket gets heavier.
- **Specific impulse** $I_{\mathrm{sp}}$ is a measure of engine efficiency, given in seconds (s). It equals $v_e / g_0$, where $g_0 = 9.80665$ $\mathrm{m/s^2}$ is standard gravity. A higher $I_{\mathrm{sp}}$ means less propellant for the same delta-v. Typical values are roughly 300-320 s for storable bipropellant engines and roughly 450 s for hydrogen-oxygen engines in vacuum.
- **Staging** means dropping empty tanks and engines during flight. Each stage then accelerates a smaller mass, so the total delta-v is the sum of the stage delta-vs. Staging helps because a single stage would need a very large mass ratio. The cost is extra hardware, more separation events, and more things that can fail.
- **Gravity on other bodies.** The surface gravity of any body is $g = GM/R^2 = \mu_{\text{body}}/R^2$. Use that body's own $\mu$ and $R$, never Earth's $g = 9.81$ $\mathrm{m/s^2}$. At altitude $h$ above the surface, the local gravity is $g(h) = \mu / (R + h)^2$. For Mars, with $\mu_{\text{Mars}} = 4.282837 \times 10^{13}$ $\mathrm{m^3/s^2}$ and $R = 3389.5$ km (typical published values), the surface gravity is about 3.73 $\mathrm{m/s^2}$.

## Key equations

Newton's law of gravitation:

$$
F = \frac{G\, m_1 m_2}{r^2}
$$

- $F$ is the attractive force (N). $G$ is the gravitational constant ($\mathrm{N\,m^2/kg^2}$). $m_1, m_2$ are masses (kg). $r$ is center-to-center distance (m).

Circular orbit speed and escape speed:

$$
v_{\text{circ}} = \sqrt{\frac{\mu}{r}} \qquad v_{\text{esc}} = \sqrt{\frac{2\mu}{r}}
$$

- $v$ is speed (m/s). $\mu$ is the gravitational parameter ($\mathrm{m^3/s^2}$). $r$ is radius from the planet's center (m).
- In US customary units, speeds are in feet per second (ft/s), with $1\ \mathrm{ft/s} = 0.3048\ \mathrm{m/s}$.

Kepler's third law:

$$
T = 2\pi \sqrt{\frac{a^3}{\mu}}
$$

- $T$ is the orbital period (s). $a$ is the semimajor axis (m).

Vis-viva equation and specific orbital energy:

$$
v^2 = \mu\left(\frac{2}{r} - \frac{1}{a}\right) \qquad \varepsilon = \frac{v^2}{2} - \frac{\mu}{r} = -\frac{\mu}{2a}
$$

- $\varepsilon$ is orbital energy per unit mass (J/kg, which equals $\mathrm{m^2/s^2}$).

Hohmann transfer semimajor axis:

$$
a_t = \frac{r_1 + r_2}{2}
$$

- $r_1$ is the starting (perigee) radius (m). $r_2$ is the target (apogee) radius (m).

Tsiolkovsky rocket equation, specific impulse, and propellant mass fraction:

$$
\Delta v = v_e \ln\frac{m_0}{m_f} \qquad v_e = I_{\mathrm{sp}}\, g_0 \qquad \text{propellant fraction} = 1 - \frac{m_f}{m_0}
$$

- $v_e$ is exhaust speed relative to the rocket (m/s). $I_{\mathrm{sp}}$ is specific impulse (s). $g_0 = 9.80665$ $\mathrm{m/s^2}$ is standard gravity, a fixed constant in the $I_{\mathrm{sp}}$ definition. The propellant fraction is a unitless share of the starting mass.

## Worked example

**Problem.** Find the total delta-v and the propellant mass fraction for a Hohmann transfer from a 400 km circular low Earth orbit (LEO) to geostationary orbit (GEO). The engine has a specific impulse of 300 s.

**Given:**

- $\mu_\oplus = 3.986004418 \times 10^{14}$ $\mathrm{m^3/s^2}$
- $R_\oplus = 6378$ km (equatorial radius; the mean radius is 6371 km)
- Starting altitude $h_1 = 400$ km, so $r_1 = 6378 + 400 = 6778$ km
- GEO radius $r_2 = 42\,164$ km (a standard value, about 35 786 km altitude)
- $I_{\mathrm{sp}} = 300$ s, $g_0 = 9.80665$ $\mathrm{m/s^2}$ (standard gravity)

**Find:** the total delta-v $\Delta v$, the mass ratio $m_0/m_f$, and the propellant mass fraction.

**Assumptions:**

- Both orbits are circular and coplanar, so no plane change is needed.
- Burns are instantaneous (impulsive).
- Gravity losses and atmospheric drag are ignored.
- The engine's $I_{\mathrm{sp}}$ stays constant during the burns.

**Solution.**

1. Convert radii to meters: $r_1 = 6.778 \times 10^6$ m and $r_2 = 4.2164 \times 10^7$ m.

2. Speeds on the two circular orbits:

$$
v_1 = \sqrt{\frac{\mu}{r_1}} = 7668.6 \text{ m/s} \qquad v_2 = \sqrt{\frac{\mu}{r_2}} = 3074.7 \text{ m/s}
$$

3. Semimajor axis of the transfer ellipse:

$$
a_t = \frac{6778 + 42164}{2} = 24\,471 \text{ km}
$$

4. Transfer speeds at perigee and apogee, from vis-viva:

$$
v_p = \sqrt{\mu\left(\frac{2}{r_1} - \frac{1}{a_t}\right)} = 10\,066.1 \text{ m/s} \qquad v_a = \sqrt{\mu\left(\frac{2}{r_2} - \frac{1}{a_t}\right)} = 1618.2 \text{ m/s}
$$

5. The two burns:

$$
\Delta v_1 = v_p - v_1 = 10\,066.1 - 7668.6 = 2397.5 \text{ m/s}
$$

$$
\Delta v_2 = v_2 - v_a = 3074.7 - 1618.2 = 1456.5 \text{ m/s}
$$

$$
\Delta v_{\text{total}} = 2397.5 + 1456.5 = 3854.0 \text{ m/s}
$$

6. Exhaust speed and mass ratio:

$$
v_e = I_{\mathrm{sp}} g_0 = 300 \times 9.80665 = 2942.0 \text{ m/s}
$$

$$
\frac{m_0}{m_f} = e^{\Delta v / v_e} = e^{3854.0 / 2942.0} = e^{1.3100} = 3.706
$$

7. Propellant mass fraction:

$$
1 - \frac{m_f}{m_0} = 1 - \frac{1}{3.706} = 0.730
$$

8. Transfer time (half the transfer ellipse period): $\pi\sqrt{a_t^3/\mu} = 5.29$ h.

**Answer.** The total delta-v is 3854 m/s, about 3.85 km/s. The mass ratio is 3.71. About 73 percent of the starting mass must be propellant. The transfer takes about 5.3 h.

**Sanity check.**

- Delta-v to GEO from a low orbit is typically a few km/s, and 3.85 km/s is in that range.
- The first burn (2.40 km/s) is larger than the second (1.46 km/s), which is typical because the perigee burn does most of the work of raising the orbit.
- The transfer time of 5.3 h is well under the 23.9 h GEO period, as expected for a half-ellipse that ends at a higher orbit.
- If $I_{\mathrm{sp}}$ rises to 450 s, $v_e = 4413$ m/s, the mass ratio falls to 2.39, and the propellant fraction drops to 0.58. Engine efficiency matters a great deal.

## Practice

1. Find the circular orbit speed at 800 km altitude above Earth. Use $\mu_\oplus$ and $R_\oplus = 6378$ km (equatorial). Give the answer in km/s.
2. A rocket has $\Delta v = 2000$ m/s and exhaust speed $v_e = 3000$ m/s. Find the propellant mass fraction.
3. Find the period of a circular orbit at 400 km altitude. Give the answer in minutes.
4. Find the specific orbital energy of the 400 km circular orbit. Give the answer in MJ/kg.
5. Find the surface gravity of Mars using $\mu_{\text{Mars}} = 4.282837 \times 10^{13}$ $\mathrm{m^3/s^2}$ and $R = 3389.5$ km. Give the answer in $\mathrm{m/s^2}$.

<details><summary>Answers</summary>

1. 7.45 km/s
2. 0.487
3. 92.6 min
4. -29.4 MJ/kg
5. 3.73 $\mathrm{m/s^2}$

</details>

## Common mistakes

- Using altitude where the radius from the planet's center is needed. Add the planet's radius first.
- Using Earth's $g = 9.81$ $\mathrm{m/s^2}$ for another body, or for an orbit at altitude. Use $\mu/r^2$ for the body and radius in question.
- Putting $I_{\mathrm{sp}}$ directly into the rocket equation. Multiply by $g_0$ first to get $v_e$ in m/s.
- Writing $\Delta v = v_e \times (m_0/m_f)$ instead of the natural logarithm. The mass ratio is exponential, not linear.
- Placing the Hohmann burns in the wrong spots. The first burn happens at perigee of the transfer ellipse, and the second at apogee.

## Go deeper

- [Astrodynamics (16.346), Fall 2008](https://ocw.mit.edu/courses/16-346-astrodynamics-fall-2008/) by MIT OpenCourseWare: two-body orbits, Kepler's problem, and mission planning, with lecture notes and problem sets under CC BY-NC-SA 4.0.
- [First Law of Thermodynamics](https://www.grc.nasa.gov/www/k-12/airplane/thermo1.html) by NASA Glenn Research Center: a plain statement of energy balance, useful background for the exhaust energy in a rocket.
- [Rocket thrust](https://www.grc.nasa.gov/www/k-12/airplane/rocket.html) by NASA Glenn Research Center: how thrust comes from accelerating expelled mass, as a conceptual introduction before the rocket equation.
- [Fields, waves, and space reference](reference-fields-waves-space.md): the lookup sheet for this topic.
