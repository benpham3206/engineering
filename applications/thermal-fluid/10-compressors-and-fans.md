# Compressors and fans

**Type:** lesson

Compressors and fans are machines that move gas by raising its pressure or pushing it along. Both turn shaft power into flow and pressure, and both waste energy when they are oversized, leaky, or run against the wrong resistance. A fan moves air with a small pressure rise, and a compressor raises the pressure enough to store or drive tools.

**Prerequisites:** [Fluid systems](02-fluid-systems.md), [Thermodynamics: properties, work, heat, and the first law](../../physics/08-thermo-first-law.md), [Thermodynamics: entropy, the second law, and cycles](../../physics/09-thermo-second-law-cycles.md)
**Time:** 6-8 h

## Core ideas

### How it works

A **compressor** raises gas pressure by reducing the volume that holds the gas. There are three main families.

A **reciprocating compressor** draws gas into a cylinder, traps it, and drives a piston to squeeze it. Valves open only when the pressure difference is right. Each stroke moves a fixed volume, so the flow follows the speed and the cylinder size.

A **screw compressor** uses two intermeshing rotors. Gas fills the pockets between the lobes at the inlet. As the rotors turn, the pockets move along the axis and shrink, and the gas pressure rises. The flow is smooth, and there are no valves to wear.

A **dynamic compressor** speeds up the gas, then slows it in a diffuser so that the kinetic energy turns into pressure. A centrifugal compressor accelerates gas outward with an impeller. An axial compressor pushes gas along the axis through many rows of blades, and each row adds a small pressure rise. Jet engines use axial compressors for this reason. See [Gas turbines and jet engines](07-gas-turbines-and-jet-engines.md).

A **fan** is a dynamic machine that moves gas at a pressure rise of a few kilopascals or less. Its blades push air along the axis (axial fan) or outward from the center (centrifugal fan). A **blower** is a centrifugal fan with a higher pressure rise.

### Compression processes

Three idealized paths bracket a real compressor. An **isothermal path** keeps the temperature constant, which needs cooling as the gas compresses. An **isentropic path** has no heat exchange and no friction, so the gas heats the most. A real machine lies between the isothermal limit and the isentropic path, with extra heat from friction.

Compressing air rapidly heats it. Air compressed from 293 K to 700 kPa leaves hot enough to damage oil and seals. Multistage compression with intercooling between stages brings the process close to isothermal and saves energy.

### Fan laws

For one fan with fixed geometry and a fixed gas density, the **fan laws** give the flow, pressure, and power at a new speed. They are the same ratios as the pump affinity laws, with one addition. Pressure and power also scale with gas density, so a hot fan moves less pressure at the same speed.

### Compressed air systems

A compressed air system includes the compressor, a receiver tank, an air dryer, filters, pipes, and the tools at the end. Most of the energy is lost before the tools use any air. Leaks, pressure set too high, and unnecessary runs of the compressor waste the most.

### Main parts

- **Cylinder and valves.** In a reciprocating compressor, the valves open when the pressure difference reaches the right value.
- **Rotors.** In a screw compressor, the male and female rotors carry the gas and seal against each other.
- **Impeller and diffuser.** In a centrifugal compressor, the impeller speeds the gas and the diffuser recovers pressure.
- **Intercooler and aftercooler.** Heat exchangers remove heat between stages and after the last stage.
- **Receiver.** A tank that smooths pressure pulses and stores air.
- **Blades and housing.** In a fan, the blades add energy to the air, and the housing directs the flow and holds the pressure.

### Variants

Reciprocating compressors handle small to medium flow at high pressure, and they suit intermittent use such as workshops. Screw compressors run continuously and suit factory air supply. Centrifugal compressors handle very large flow at moderate pressure, such as process gas and large plants. Axial fans move large volumes at low pressure, as in cooling towers. Centrifugal fans work against higher pressure, as in ducts and furnaces.

## Key equations

- Isentropic outlet temperature: $T_{2s} = T_1 (p_2/p_1)^{(\gamma-1)/\gamma}$, with $T$ in K, $p$ in Pa, and $\gamma$ dimensionless (1.4 for air).
- Isentropic power: $P_{\mathrm{is}} = \dot m\, c_p (T_{2s} - T_1)$, with $\dot m$ in kg/s and $c_p = 1005\ \text{J/(kg K)}$ for air (typical).
- Actual shaft power: $P = P_{\mathrm{is}}/\eta_{\mathrm{is}}$, with $\eta_{\mathrm{is}}$ dimensionless.
- Actual outlet temperature: $T_2 = T_1 + (T_{2s} - T_1)/\eta_{\mathrm{is}}$.
- Isothermal ideal power: $P_{\mathrm{iso}} = \dot m\, R T_1 \ln(p_2/p_1)$, with $R = 287\ \text{J/(kg K)}$ for air (typical).
- Fan laws at fixed geometry: $Q \propto N$, $\Delta p \propto \rho N^2$, $P \propto \rho N^3$, with $N$ in rev/min and $\rho$ in $\text{kg/m}^3$.
- Fan air power: $P_{\mathrm{air}} = Q\, \Delta p$, in W, with $Q$ in $\text{m}^3$/s and $\Delta p$ in Pa. Shaft power is $P_{\mathrm{air}}/\eta$.
- Choked leak through an orifice: $\dot m = C_d A p_0 \sqrt{\gamma/(R T_0)} \left(\dfrac{2}{\gamma+1}\right)^{(\gamma+1)/(2(\gamma-1))}$, with $C_d$ dimensionless (about 0.6 for a sharp hole), $A$ in $\text{m}^2$, $p_0$ in Pa, and $T_0$ in K.

## Worked example

**Given:** A compressor draws air at $p_1 = 101.3\ \text{kPa}$ and $T_1 = 293\ \text{K}$. It delivers $\dot m = 0.05\ \text{kg/s}$ at $p_2 = 700\ \text{kPa}$ absolute. The isentropic efficiency is $\eta_{\mathrm{is}} = 0.80$. Air has $\gamma = 1.4$, $c_p = 1005\ \text{J/(kg K)}$, and $R = 287\ \text{J/(kg K)}$.

**Find:** (a) the isentropic outlet temperature, (b) the actual shaft power, (c) the actual outlet temperature, and (d) the isothermal ideal power for comparison.

**Solution:**

1. Pressure ratio: $r = 700 / 101.3 = 6.91$.
2. Isentropic outlet temperature: $T_{2s} = 293 \times 6.91^{0.286} = 509\ \text{K}$, which is about $236\ \text{C}$.
3. Isentropic power: $P_{\mathrm{is}} = 0.05 \times 1005 \times (509 - 293) = 10\,850\ \text{W}$.
4. Actual shaft power: $P = 10\,850 / 0.80 = 13\,570\ \text{W}$, which is about $13.6\ \text{kW}$.
5. Actual outlet temperature: $T_2 = 293 + (509 - 293)/0.80 = 563\ \text{K}$, which is about $290\ \text{C}$.
6. Isothermal ideal power: $P_{\mathrm{iso}} = 0.05 \times 287 \times 293 \times \ln(6.91) = 8130\ \text{W}$, which is about $8.1\ \text{kW}$.

**Answer:** (a) $509\ \text{K}$. (b) $13.6\ \text{kW}$. (c) $563\ \text{K}$. (d) $8.1\ \text{kW}$.

**Sanity check:** The actual power is larger than the isentropic power, and the isentropic power is larger than the isothermal ideal. The isothermal ideal sets the lower bound on work. The gap between $8.1\ \text{kW}$ and $13.6\ \text{kW}$ is the reason designers add intercooling. The outlet at about $290\ \text{C}$ is hot enough to degrade lubricating oil, which is why the aftercooler is part of the package.

## Design trade-offs

Stages and intercooling trade cost against efficiency. Two or three stages with intercoolers come close to the isothermal limit, but each stage adds a cooler, a valve set, and a control loop.

Lubricated and oil-free compressors trade cost against air quality. Oil-free machines cost more and need more maintenance, but they give air with no oil for food, medical, and paint work. Lubricated machines are cheaper and need filtration.

Load-unload control and variable speed drives match the air output to demand. A load-unload compressor runs at full power or idles, so idle losses add up. A variable speed drive matches output more closely. Most of the input power ends up as heat, and that heat can warm a building or water.

Fan selection depends on blade shape. Backward-curved blades give high efficiency and a steady curve. Forward-curved blades give more flow in a small housing but lower efficiency. Noise rises steeply with tip speed, so a larger, slower fan is quieter than a small fast one for the same flow.

Leaks waste a large share of the air in many compressed air systems. The leak formula below shows how much a small hole passes.

## How it fails

**Surge.** A dynamic compressor at low flow can reverse the flow through the impeller. Pressure swings back and forth, and the machine shakes hard enough to break bearings and blades. A surge control valve that recycles gas keeps the flow above the surge line.

**Stall.** Blades in an axial fan or compressor stall when the angle of attack grows too high. A rotating stall spreads from blade to blade. Warning signs are noise, vibration, and a falling pressure rise.

**Overheating and oil carbonization.** High outlet temperatures burn oil into deposits, which block valves and cause fires. Cooling and high-temperature alarms prevent it.

> [!WARNING]
> **Vessel rupture.** A receiver or intercooler can burst if it is overpressured. A relief valve sized for the compressor limits the pressure, and the vessel must meet a pressure code.

> [!WARNING]
> **Air injection injury.** A jet of compressed air can enter the skin and cause serious injury. Never point an air nozzle at a person.

**Fan imbalance.** Dust on the blades or a bent blade shifts the balance, and the vibration grows fast. Bearings then fail. Regular cleaning and balance checks prevent it.

## History

Compressed air powered rock drills in the Mont Cenis tunnel through the Alps in the 1860s, and Germain Sommeiller led the work. Charles Parsons built a steam turbine in 1884, and blade-row machines of that kind later led to dynamic compressors. Frank Whittle proposed a centrifugal jet engine in the 1930s, and jet engines with axial compressors followed in the 1940s. Alf Lysholm developed the rotary screw compressor in the 1930s.

## Practice

1. Air at $100\ \text{kPa}$ and $300\ \text{K}$ is compressed isentropically to $500\ \text{kPa}$. Find the outlet temperature. Use $\gamma = 1.4$.
2. A fan turns at 900 rev/min and delivers $Q = 1.5\ \text{m}^3/\text{s}$. Find the flow at 1350 rev/min.
3. The same fan produces $\Delta p = 200\ \text{Pa}$ at 900 rev/min. Find the pressure rise at 1350 rev/min, and find the ratio of its shaft power at the two speeds.
4. A $2\ \text{mm}$ hole is open in a line at $700\ \text{kPa}$ absolute and $293\ \text{K}$. Use $C_d = 0.6$ and find the leak mass flow. Then state what happens to the flow if the hole doubles in diameter.
5. A compressor needs $4.0\ \text{kW}$ of isentropic power and runs at $\eta_{\mathrm{is}} = 0.75$. Find its actual shaft power.

<details><summary>Answers</summary>

1. $T_2 = 300 \times 5^{0.286} = 475\ \text{K}$, which is about $202\ \text{C}$.
2. $Q_2 = 1.5 \times 1350/900 = 2.25\ \text{m}^3/\text{s}$.
3. $\Delta p_2 = 200 \times (1350/900)^2 = 450\ \text{Pa}$. The power ratio is $(1350/900)^3 = 3.4$, so the shaft power rises by a factor of about 3.4.
4. The flow is $\dot m = 0.00312\ \text{kg/s}$, or $3.1\ \text{g/s}$. Doubling the diameter multiplies the area by four, so the flow becomes $12.5\ \text{g/s}$.
5. $P = 4.0 / 0.75 = 5.3\ \text{kW}$.

</details>

## Common mistakes

- Using gauge pressure in the compressor equations. The pressure ratio needs absolute pressures, so add atmospheric pressure to the gauge reading.
- Assuming a fan's pressure follows the speed law without the density term. Hot air makes less pressure than cold air at the same speed.
- Sizing a compressor only from the tool demand, and forgetting leaks, the receiver size, and the duty cycle.
- Treating the isentropic temperature as the real outlet temperature. Divide the temperature rise by the efficiency.
- Assuming a leak is small because the hole is small. Flow scales with the hole area, so doubling the diameter quadruples the leak.

## Go deeper

- [Compressors, NASA Glenn Research Center K-12 resources](https://www.grc.nasa.gov/www/k-12/airplane/compress.html): axial and centrifugal compressors, and how they raise pressure in jet engines.
- [*Fluid Mechanics*, Wikibooks](https://en.wikibooks.org/wiki/Fluid_Mechanics) by Wikibooks contributors: an open text on fluid statics and control-volume analysis, the method used for the flow balances in this lesson.
- Related: [Pumps](09-pumps.md) for the same affinity logic applied to liquids, and [Gas turbines and jet engines](07-gas-turbines-and-jet-engines.md) for axial compressors in engines.
- Related: [Hydraulics and pneumatics](../machines-robots/07-hydraulics-and-pneumatics.md) for compressed air driving machine actuators, and [Vacuum cleaners](../everyday/04-vacuum-cleaners.md) for fans and suction.
- [Applications reference](../reference.md): the lookup sheet for this topic.
