# Rockets

**Type:** lesson

A rocket carries its own oxidizer or oxidizer and fuel, so it works in vacuum. An engineer who designs one must size the engine, the nozzle, the propellant tanks, and the structure that holds them, and each choice trades performance against mass and risk.

**Prerequisites:** [Thermodynamics: properties, work, heat, and the first law](../../physics/08-thermo-first-law.md), [Thermodynamics: entropy, the second law, and cycles](../../physics/09-thermo-second-law-cycles.md), [Particle dynamics](../../physics/02-particle-dynamics.md)
**Time:** 8-10 h

## Core ideas

### How it works

A rocket engine burns propellant in a combustion chamber at high pressure. The hot gas leaves through a nozzle at high speed. The gas pushes the engine forward, and by Newton's third law, the engine pushes the gas backward. The rocket needs no air to push against, so it works in space.

The nozzle does the work of turning heat into speed. Gas leaves the chamber slowly and enters a narrow throat. At the throat, the gas reaches the speed of sound, and the flow is choked. Downstream, the nozzle widens, and the gas expands and speeds up to a supersonic exit velocity. The exit pressure can be above, equal to, or below the outside pressure, and that difference adds a second term to the thrust.

The propellant supply has its own system. In a pressure-fed engine, tank pressure forces propellant into the chamber. In a turbopump engine, pumps driven by turbines raise the pressure, which lets the tanks stay light. Each design balances tank mass, pump mass, and complexity.

### Main parts

- **Injector.** Sprays fuel and oxidizer into the chamber so they mix and burn evenly. Poor mixing causes hot spots and instability.
- **Combustion chamber.** Holds the burning gas at high pressure. Its walls are cooled, often by flowing fuel through channels in the wall.
- **Throat.** The narrowest section of the nozzle. Its area sets the mass flow for a given chamber pressure.
- **Nozzle.** The diverging section that expands the gas. Its exit area sets the thrust and the efficiency at each altitude.
- **Propellant tanks.** Hold the fuel and oxidizer. For a liquid rocket, the tanks are the main structure of the vehicle, and their walls carry internal pressure and flight loads.
- **Turbopumps.** Raise propellant pressure to the chamber level in a turbopump-fed engine.
- **Thrust vector control.** A gimbaled engine or movable vanes that tilt the thrust to steer the vehicle.

### Variants

- **Liquid bipropellant.** Separate fuel and oxidizer, both liquid. They can be throttled, shut down, and restarted. Examples pair liquid oxygen with kerosene (RP-1) or with liquid hydrogen.
- **Storable liquid.** Liquids that stay liquid at room temperature, such as nitrogen tetroxide and a hydrazine-based fuel. They fit in tanks that sit for years, which suits spacecraft and missile use.
- **Solid motor.** The propellant is a solid grain that burns on its surface. The motor is simple and reliable, and it cannot be shut off once lit.
- **Hybrid.** A solid fuel with a liquid or gaseous oxidizer. It can be throttled and shut down, and it avoids the complexity of a liquid pump system.
- **Cold gas thrusters.** Compressed gas leaves through a nozzle with no combustion. The thrust is low, and the system is used for attitude control.

## Key equations

Thrust of a nozzle, from the momentum of the exhaust and the pressure at the exit.

$$
F = \dot m\, v_e + (p_e - p_a)\, A_e
$$

- $F$ is thrust (N). $\dot m$ is propellant mass flow rate (kg/s). $v_e$ is exhaust velocity at the nozzle exit (m/s). $p_e$ is exit pressure (Pa). $p_a$ is ambient pressure (Pa), zero in vacuum and 101 325 Pa at sea level on Earth. $A_e$ is nozzle exit area (m$^2$).
- Assumptions: steady flow, uniform conditions across the exit plane, one-dimensional flow, and no external forces on the gas after it leaves the nozzle.

Specific impulse, a measure of how efficiently a propellant makes thrust.

$$
I_{\mathrm{sp}} = \frac{F}{\dot m\, g_0} \qquad v_e = I_{\mathrm{sp}}\, g_0 \text{ when } p_e = p_a
$$

- $I_{\mathrm{sp}}$ is specific impulse (s). $g_0 = 9.80665$ m/s$^2$ is standard gravity. The second form applies only when the pressure term in the thrust equation is zero.
- Assumptions: the pressure term is zero for the second form, and the flow is steady. For the first form, the thrust and mass flow are both measured over the same period.

Choked mass flow through the throat, with an ideal gas.

$$
\dot m = \frac{A_t\, p_c\, \Gamma}{\sqrt{R\, T_c}} \qquad \Gamma = \sqrt{\gamma}\left(\frac{2}{\gamma+1}\right)^{\frac{\gamma+1}{2(\gamma-1)}}
$$

- $A_t$ is throat area (m$^2$). $p_c$ is chamber pressure (Pa). $R$ is the specific gas constant (J/(kg K)), equal to the universal gas constant 8314.46 J/(kmol K) divided by the molar mass in kg/kmol. $T_c$ is chamber temperature (K). $\gamma$ is the ratio of specific heats (dimensionless).
- Assumptions: ideal gas with constant $\gamma$, isentropic flow from chamber to throat, no friction or heat loss, and the throat flow exactly at Mach 1.

Exit velocity for an ideal nozzle expansion.

$$
v_e = \sqrt{\frac{2\gamma}{\gamma-1}\, R\, T_c \left[1 - \left(\frac{p_e}{p_c}\right)^{\frac{\gamma-1}{\gamma}}\right]}
$$

- Assumptions: ideal gas with constant $\gamma$, isentropic expansion, no friction, and frozen composition (no further reactions in the nozzle). Real engines lose some speed to these effects, so this value is an upper bound.

Area ratio and exit Mach number, from isentropic flow.

$$
\frac{A_e}{A_t} = \frac{1}{M_e}\left[\frac{2}{\gamma+1}\left(1 + \frac{\gamma-1}{2} M_e^2\right)\right]^{\frac{\gamma+1}{2(\gamma-1)}}
$$

- $M_e$ is the Mach number at the exit (dimensionless). The equation applies in the supersonic branch, where $M_e > 1$.
- Assumptions: isentropic, ideal gas with constant $\gamma$, and one-dimensional flow.

Structural mass fraction of a stage, which sets how much of the stage is structure.

$$
\varepsilon = \frac{m_s}{m_s + m_p}
$$

- $m_s$ is the stage's dry structure mass (kg), without propellant. $m_p$ is the propellant mass (kg). $\varepsilon$ is dimensionless.
- Assumptions: the engine mass is included in $m_s$, and the propellant is all usable.

Solid propellant burn rate, an empirical law.

$$
r = a\, p_c^{\,n}
$$

- $r$ is burn rate, the speed at which the grain surface recedes (m/s). $a$ is a constant with units of (m/s)/Pa$^n$ and is set by the propellant. $p_c$ is chamber pressure (Pa). $n$ is the pressure exponent (dimensionless), often between 0.3 and 0.5 for typical propellants.
- Assumptions: the pressure is uniform in the port, the propellant composition is fixed, and $a$ and $n$ hold over the pressure range used.

The rocket equation, which turns exhaust speed into velocity change, is derived in [Orbital mechanics and rockets](../../physics/15-orbital-mechanics-and-rockets.md). This lesson covers the hardware that sets $v_e$.

## Worked example

**Given.** A liquid rocket engine has chamber pressure $p_c = 7.0$ MPa and chamber temperature $T_c = 3500$ K. The propellant has molar mass 22 kg/kmol and $\gamma = 1.2$. The mass flow is $\dot m = 100$ kg/s. The nozzle exit pressure is $p_e = 0.10$ MPa.

**Find.** (a) the throat area, (b) the exhaust velocity, (c) the exit Mach number and exit area, and (d) the thrust and specific impulse in vacuum and at sea level.

**Assumptions.** Ideal gas, constant $\gamma$, isentropic flow in the nozzle, frozen composition, and no friction or heat loss. These assumptions make the result an ideal upper bound.

**Solution.**

1. Specific gas constant: $R = 8314.46 / 22 = 377.9$ J/(kg K).
2. Throat area from the choked mass flow. With $\Gamma = \sqrt{1.2}\,(2/2.2)^{2.2/0.4} = 0.6485$:
$$
A_t = \frac{\dot m \sqrt{R T_c}}{p_c \Gamma} = \frac{100 \times \sqrt{377.9 \times 3500}}{7.0\times10^6 \times 0.6485} = 2.53\times10^{-2}\ \text{m}^2
$$
3. Exhaust velocity:
$$
v_e = \sqrt{\frac{2 \times 1.2}{0.2}\times 377.9 \times 3500 \times \left[1 - (0.10/7.0)^{1/6}\right]} = 2838\ \text{m/s}
$$
4. Exit Mach number from the pressure ratio. The isentropic relation gives $M_e = 3.21$. The area ratio is then
$$
\frac{A_e}{A_t} = 9.06 \qquad A_e = 9.06 \times 2.53\times10^{-2} = 0.230\ \text{m}^2
$$
5. Thrust in vacuum, with $p_a = 0$:
$$
F_{\text{vac}} = 100 \times 2838 + (0.10\times10^6)(0.230) = 306.8\ \text{kN}
$$
$I_{\mathrm{sp},\text{vac}} = 306\,800 / (100 \times 9.80665) = 313$ s.
6. Thrust at sea level, with $p_a = 101\,325$ Pa:
$$
F_{\text{sl}} = 100 \times 2838 + (0.10\times10^6 - 101\,325)(0.230) = 283.5\ \text{kN}
$$
$I_{\mathrm{sp},\text{sl}} = 283\,500 / 980.665 = 289$ s.

**Answer.** (a) $A_t = 0.0253$ m$^2$, a throat diameter of about 0.18 m. (b) $v_e = 2838$ m/s. (c) $M_e = 3.21$ and $A_e = 0.230$ m$^2$, an exit diameter of about 0.54 m. (d) Vacuum: $F = 307$ kN and $I_{\mathrm{sp}} = 313$ s. Sea level: $F = 283$ kN and $I_{\mathrm{sp}} = 289$ s.

**Sanity check.** Vacuum specific impulse of 313 s is in the range of kerosene and oxygen engines. The sea-level value is lower because the exit pressure sits slightly below ambient, so the engine is overexpanded there and loses thrust. Real engines run below these ideal values because of friction, heat loss, and incomplete mixing.

## Design trade-offs

- **Expansion ratio.** A large exit area gives higher vacuum specific impulse. A large nozzle is heavy and cannot run at sea level without flow separation. Upper stages use large nozzles, and first stages use smaller ones. The ideal expansion ratio is the one that makes the exit pressure equal to ambient pressure at the design altitude.
- **Chamber pressure.** Higher chamber pressure makes the engine smaller for the same thrust, but the turbopumps, chamber walls, and injector must handle more load.
- **Propellant choice.** Liquid hydrogen with oxygen gives the highest specific impulse, near 450 s in vacuum (typical value). Its low density forces large, heavy tanks. Kerosene with oxygen gives a lower specific impulse but a denser fuel, which yields smaller tanks. Solid propellants have the lowest specific impulse, near 250 to 270 s in vacuum (typical value), and are the simplest.
- **Structure.** A stage with a structural mass fraction of 0.05 has structure equal to 5.3 percent of its propellant mass, because $\varepsilon = 0.05$ means $m_s = 0.0526\, m_p$. Tanks, engines, and thrust structure all add to this mass. Lighter tanks mean more propellant per stage, but they need stronger design checks.
- **Cooling.** Regenerative cooling uses the cold propellant to carry heat from the chamber wall. It lets the engine run at high pressure, at the cost of pumps and plumbing.

## How it fails

- **Seal failure.** On 28 January 1986, a rubber O-ring in a solid rocket booster joint failed in cold launch conditions, and hot gas escaped. The Space Shuttle Challenger broke up in flight. Cold tests, joint redesign, and independent review became required.
- **Combustion instability.** Pressure waves in the chamber can grow and tear an engine apart within seconds. Designers use injector patterns, baffles, and acoustic damping to prevent this.
- **Turbopump failure.** Cavitation, bearing failure, or a turbine blade fault can cut propellant flow. Engines use health monitoring and shutdown logic to stop before damage spreads.
- **Nozzle erosion or burn-through.** Hot gas and high heat flux can burn the throat. Ablative linings and regenerative cooling keep the wall below its limit.
- **Tank failure.** Overpressure can burst a tank, and low internal pressure can cause a thin wall to buckle under external loads. Relief valves, burst disks, and stiffened structures protect the tank.
- **Pogo oscillation.** Coupling between propellant feed and engine thrust can cause large vibrations along the vehicle axis. Accumulators and feed-line damping reduce it.

## History

Konstantin Tsiolkovsky published the basis of rocket theory in 1903. Robert Goddard launched the first liquid-fueled rocket on 16 March 1926 at Auburn, Massachusetts. Engineers at Peenemunde in Germany, led by Wernher von Braun's team, achieved the first successful flight of the V-2 missile in October 1942. The Saturn V and the Space Shuttle main engines of the 1960s and 1970s pushed large liquid rockets and solid boosters to their limits.

## Practice

1. An engine has $I_{\mathrm{sp}} = 300$ s. Find the effective exhaust velocity $I_{\mathrm{sp}} g_0$ in m/s. This equals the physical exit velocity only when $p_e = p_a$.
2. An engine has $\dot m = 50$ kg/s and an effective exhaust velocity $I_{\mathrm{sp}} g_0 = 2900$ m/s, which already includes any exit-pressure thrust. Find the thrust in kN.
3. A throat carries $\dot m = 20$ kg/s at $p_c = 5.0$ MPa and $T_c = 3300$ K, with $R = 350$ J/(kg K) and $\gamma = 1.2$. Find the throat area in cm$^2$.
4. An engine makes 100 kN of thrust at $I_{\mathrm{sp}} = 280$ s. Find the mass flow rate in kg/s.
5. A nozzle has an area ratio of 16 and $\gamma = 1.2$. Find the exit Mach number.

<details><summary>Answers</summary>

1. $I_{\mathrm{sp}} g_0 = 300 \times 9.80665 = 2942$ m/s (effective exhaust velocity)
2. $F = \dot m \times I_{\mathrm{sp}} g_0 = 50 \times 2900 = 145\,000$ N, which is 145 kN
3. $\Gamma = 0.6485$, so $A_t = 20 \times \sqrt{350 \times 3300} / (5.0\times10^6 \times 0.6485) = 6.63\times10^{-3}$ m$^2$, which is 66.3 cm$^2$
4. $\dot m = 100\,000 / (280 \times 9.80665) = 36.4$ kg/s
5. $M_e = 3.60$

</details>

## Common mistakes

- Using specific impulse in the thrust equation without multiplying by $g_0$. Specific impulse is in seconds, and the exhaust velocity is in m/s.
- Using the vacuum value of specific impulse for a sea-level launch. The exit pressure term cuts the sea-level thrust and specific impulse.
- Assuming the rocket pushes against the air. Thrust comes from the exhaust momentum. The rocket works just as well in vacuum.
- Treating the solid motor as throttleable. Once lit, a solid grain burns until it is spent, unless the motor has a special design.
- Ignoring the structure in performance estimates. Tanks, engines, and thrust structure often make up a large share of a stage's dry mass, and their mass lowers the stage's velocity change.

## Go deeper

- [Rocket thrust](https://www.grc.nasa.gov/www/k-12/airplane/rocket.html) by NASA Glenn Research Center: how thrust comes from accelerating expelled mass.
- [Thrust equation](https://www.grc.nasa.gov/www/k-12/airplane/rockth.html) by NASA Glenn Research Center: the thrust equation with the exit-pressure term.
- [Nozzles](https://www.grc.nasa.gov/www/k-12/airplane/nozzle.html) by NASA Glenn Research Center: converging and diverging nozzles and the throat.
- [16.522 Space Propulsion, Spring 2015](https://ocw.mit.edu/courses/16-522-space-propulsion-spring-2015/) by MIT OpenCourseWare: rocket propulsion fundamentals and solid rocket motors, with openly licensed course materials.
- Reference sheets: [Thermofluids reference](../../physics/reference-thermofluids.md) and [Mechanics reference](../../physics/reference-mechanics.md).
- Related lessons: [Orbital mechanics and rockets](../../physics/15-orbital-mechanics-and-rockets.md), [Gas turbines and jet engines](../thermal-fluid/07-gas-turbines-and-jet-engines.md), [Pressure vessels and tanks](../structures/03-pressure-vessels-and-tanks.md), and [Spacecraft and satellites](08-spacecraft-and-satellites.md).
