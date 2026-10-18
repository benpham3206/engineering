# Thermodynamics: properties, work, heat, and the first law

**Type:** lesson

Thermodynamics is the study of energy and how it moves between heat and work. Engines, compressors, turbines, refrigerators, and power plants all depend on it.
**Prerequisites:** [07-waves-light-heat.md](07-waves-light-heat.md) (temperature, heat, and specific heat)
**Time:** 8-12 h

## Core ideas

### Systems and properties

- A **system** is the part of the universe you choose to study. Everything else is the **surroundings**.
- A **closed system** has a fixed mass. Energy can cross its boundary, but mass cannot.
- An **open system** (also called a control volume) has mass flowing in and out. A turbine, a compressor, and a nozzle are open systems.
- A **property** describes the state of a system, such as pressure, temperature, volume, or internal energy. A **state** is a set of values for all the properties at one moment.
- **Pressure** $P$ is force per unit area, in pascals (Pa). One standard atmosphere is about $101{,}325$ Pa, or 14.7 psi.
- **Specific volume** $v$ is volume per unit mass, in cubic meters per kilogram (m³/kg). Density is its inverse.
- A property that depends only on the state is called a **state function**. Pressure, temperature, and internal energy are state functions. Work and heat are not.

### The ideal gas model

- An **ideal gas** is a model where molecules do not attract each other and take up almost no space. Air at room temperature and atmospheric pressure behaves close enough to an ideal gas for most engineering work.
- The ideal gas law relates pressure, specific volume, and temperature. For a fixed mass, it links them through the gas constant $R$.
- For dry air, $R = 287$ J/(kg K). This lesson uses this value throughout, so no steam table is needed.
- Two specific heats matter. $c_p$ is the specific heat at constant pressure. $c_v$ is the specific heat at constant volume. For air, $c_p \approx 1005$ J/(kg K) and $c_v \approx 718$ J/(kg K). These are typical values near room temperature.
- The ratio $k = c_p/c_v$ is about $1.4$ for air.

### Internal energy

- **Internal energy** $U$ is the energy stored in the molecules of a substance. For an ideal gas, it depends only on temperature.
- Its change is $\Delta U = m\,c_v\,\Delta T$ for an ideal gas.

### Work

- In thermodynamics, **work** $W$ is energy that crosses the boundary of a system because of a force acting through a distance. A moving piston is the standard example.
- By convention in this lesson, work done *by* the system is positive. Work done *on* the system is negative.
- For a gas at constant pressure in a piston, $W = P\,\Delta V$.

### Heat

- **Heat** $Q$ is energy that crosses the boundary because of a temperature difference.
- By convention in this lesson, heat added *to* the system is positive. Heat removed from the system is negative.
- Heat and work depend on the path a process takes. They are not state functions.

### The first law of thermodynamics

- The **first law** is energy conservation. The change in a system's internal energy equals the heat added minus the work the system does.
- For a closed system, the first law is written in terms of internal energy, heat, and work.
- For an open system at steady flow, the energy balance also includes the energy carried by the flowing mass: enthalpy, kinetic energy, and potential energy.
- **Enthalpy** $h$ is the internal energy plus pressure times specific volume. For an ideal gas, $h = c_p T$ (relative to a reference temperature).

## Key equations

First law for a closed system:

$$
\Delta U = Q - W
$$

- $\Delta U$ is the change in internal energy (J).
- $Q$ is the heat added to the system (J).
- $W$ is the work done by the system (J).

Work at constant pressure for a closed system:

$$
W = P\,\Delta V = m\,R\,\Delta T
$$

- $P$ is the constant pressure (Pa).
- $\Delta V$ is the change in volume (m³).
- The second form uses the ideal gas law for a fixed mass at constant pressure.

Steady-flow energy balance for an open system with one inlet and one outlet, with negligible kinetic and potential energy changes:

$$
\dot{W} = \dot{m}\,c_p\,(T_1 - T_2)
$$

- $\dot{W}$ is the power output (W).
- $\dot{m}$ is the mass flow rate (kg/s).
- $T_1$ and $T_2$ are the inlet and outlet temperatures (K).

Adiabatic (no heat transfer) isentropic relation for an ideal gas:

$$
\frac{T_2}{T_1} = \left(\frac{P_2}{P_1}\right)^{(k-1)/k}
$$

- $P_1$, $P_2$ are the initial and final pressures (Pa).
- $T_1$, $T_2$ are the initial and final temperatures (K).

Ideal gas density:

$$
\rho = \frac{P}{R\,T}
$$

- $\rho$ is the density (kg/m³).

## Worked example

**Problem.** A piston and cylinder hold $m = 0.50$ kg of air at a constant pressure of $P = 200$ kPa. The air is heated from $T_1 = 300$ K to $T_2 = 400$ K at constant pressure. Find the work done by the air, the heat added, and the change in internal energy.

**Given:**

- $m = 0.50$ kg
- $P = 200$ kPa (constant)
- $T_1 = 300$ K, $T_2 = 400$ K
- $R = 287$ J/(kg K), $c_p = 1005$ J/(kg K), $c_v = 718$ J/(kg K) (note $c_p - R = c_v$)

**Find:** $W$, $Q$, $\Delta U$

**Assumptions:** Air is an ideal gas. The piston moves freely, so the pressure stays at 200 kPa. Kinetic and potential energy changes are zero.

**Solution.**

1. Temperature change: $\Delta T = 400 - 300 = 100$ K.
2. Work done by the air at constant pressure: $W = m\,R\,\Delta T = 0.50(287)(100) = 14{,}350$ J.
3. Change in internal energy: $\Delta U = m\,c_v\,\Delta T = 0.50(718)(100) = 35{,}900$ J.
4. Heat added from the first law: $Q = \Delta U + W = 35{,}900 + 14{,}350 = 50{,}250$ J.
5. Check with the constant-pressure form: $Q = m\,c_p\,\Delta T = 0.50(1005)(100) = 50{,}250$ J. It matches.

**Answer.** The work done by the air is 14.4 kJ. The heat added is 50.3 kJ. The change in internal energy is 35.9 kJ.

**Sanity check.** Most of the heat goes into raising the internal energy, and the rest goes out as expansion work. The ratio $W/Q = 14.35/50.25 = 0.286$, which is close to $(k-1)/k = 0.286$. That is what you expect for a constant-pressure process of an ideal gas.

## Practice

1. Air at constant pressure is heated from $300$ K to $350$ K. The mass is $2.0$ kg. Find the work done by the air, in kilojoules.
2. For the same $2.0$ kg of air and the same temperature change, find the heat added and the change in internal energy, in kilojoules.
3. Find the density of air at $100$ kPa and $300$ K. Use $R = 287$ J/(kg K).
4. An adiabatic air turbine has an inlet temperature of $1200$ K and an outlet temperature of $900$ K. The mass flow rate is $2.0$ kg/s. Neglect kinetic and potential energy. Find the power output in kilowatts.
5. Air at $300$ K is compressed adiabatically and reversibly from $100$ kPa to $500$ kPa. Use $k = 1.4$. Find the final temperature.

<details><summary>Answers</summary>

1. $28.7$ kJ
2. $Q = 100.5$ kJ, $\Delta U = 71.8$ kJ
3. $1.16$ kg/m³
4. $603$ kW
5. $475$ K

</details>

## Common mistakes

- Using $c_v$ for a constant-pressure heat calculation. Use $c_p$ when pressure stays constant.
- Mixing up the sign convention for work. Pick one convention, such as work done by the system is positive, and use it every time.
- Using Celsius in a gas equation. Always convert to kelvin before computing $T$ ratios or using $PV = mRT$.
- Treating heat and work as stored quantities. Both describe energy crossing a boundary, so they depend on the path.
- Forgetting the flow terms in an open system. The steady-flow balance includes enthalpy and, when they matter, kinetic and potential energy.

## Go deeper

- [Introduction to Thermodynamics (Chapter 3), University Physics Volume 2](https://openstax.org/books/university-physics-volume-2/pages/3-introduction) by OpenStax: systems, work, heat, the first law, and processes for an ideal gas, free to read.
- [First Law of Thermodynamics](https://www.grc.nasa.gov/www/k-12/airplane/thermo1.html) by NASA Glenn Research Center: internal energy as a state variable and the relation between heat, work, and energy change.
- [Introduction to the Temperature and Heat chapter, University Physics Volume 2](https://openstax.org/books/university-physics-volume-2/pages/1-introduction) by OpenStax: temperature, specific heat, and calorimetry, useful as background for the heat terms in this lesson.
