# Gas turbines and jet engines

**Type:** lesson

A gas turbine compresses air, burns fuel in it, and expands the hot gas through a turbine. Part of the turbine's work drives the compressor, and the rest either turns a shaft or leaves as a fast jet that pushes the engine forward. Engineers use the Brayton cycle to estimate efficiency and the thrust equation to size engines for aircraft, power plants, and ships.

**Prerequisites:** [Thermodynamics: properties, work, heat, and the first law](../../physics/08-thermo-first-law.md), [Thermodynamics: entropy, the second law, and cycles](../../physics/09-thermo-second-law-cycles.md)
**Time:** 8-12 h

## Core ideas

### How it works

Air flows through five stages in order.

1. Intake. Air enters at the ambient pressure and temperature. At flight speed, the inlet also slows the air and raises its pressure.
2. Compression. The compressor raises the air pressure, often by a factor of 10 to 40 in modern engines (typical values). Compression raises the air temperature as well.
3. Combustion. Fuel burns in the combustor at nearly constant pressure, and the gas temperature rises sharply.
4. Expansion. The hot gas passes through one or more turbine stages. The turbine extracts enough work to drive the compressor, and the remaining energy goes to the shaft or the nozzle.
5. Exhaust. The nozzle expands the remaining gas and accelerates it out of the engine.

The ideal Brayton cycle has four processes: isentropic compression, constant-pressure heat addition, isentropic expansion, and constant-pressure heat rejection. The cycle describes the air as a closed loop, which is an idealization. Real engines take in fresh air, so the cycle is a model of the gas path, not a literal loop.

The engine type sets where the useful work goes. A turbojet sends all of the leftover energy into the exhaust, so it produces thrust only. A turbofan uses the turbine to drive a large fan that moves air around the core, so most of its thrust comes from the fan air. A turboprop or turboshaft uses the turbine to drive a propeller or rotor through a gearbox, and an industrial turbine drives a generator.

### Main parts

- The inlet shapes the air flow and delivers it to the compressor. Its design matters most at high speed.
- The compressor is axial, with many stages of rotor and stator blades, or centrifugal, with a single impeller. Large engines use axial compressors because they move more air for a given diameter.
- The combustor burns the fuel in a steady flame. Modern combustors are annular rings or can-annular arrays, and they mix the fuel and air to keep the flame stable and the emissions low.
- The turbine stages are the high-pressure and low-pressure turbines, each on its own shaft. The high-pressure turbine drives the high-pressure compressor. The turbine blades run in gas hotter than their metal can stand, so they carry internal air cooling and ceramic thermal barrier coatings.
- The nozzle sets the exit velocity. A variable nozzle changes the exit area for different flight conditions.
- The bearings, oil system, and accessory gearbox carry the shafts and drive the fuel pump and generator.

### Variants

- Turbojet: a simple engine with no fan. It is used on early jet aircraft and on some missiles. Its exhaust is fast and noisy, so it is inefficient at low speed.
- Low-bypass turbofan: a small fan with a bypass ratio of about 0.5 to 2 (typical values). It suits fighters, which need high thrust at high speed.
- High-bypass turbofan: a large fan with a bypass ratio of about 9 to 12 on modern large airliners (typical values). Its slower exhaust is quieter and uses less fuel per unit of thrust.
- Turboprop and turboshaft: turbines that drive a propeller or a helicopter rotor through a reduction gearbox.
- Industrial and marine gas turbines: turbines that drive generators or ship propulsion. Power plants also run gas turbines as the top half of a combined cycle, with a steam plant on the exhaust. See [Steam power plants](08-steam-power-plants.md).

## Key equations

Symbols are in SI units unless marked dimensionless.

- Ideal Brayton efficiency: $\eta = 1 - r_p^{-(\gamma-1)/\gamma}$, where $r_p$ is the pressure ratio (dimensionless) and $\gamma = 1.4$ is the ratio of specific heats for air (typical value, dimensionless).
- Compressor work per kilogram of air: $w_c = c_p (T_2 - T_1)$, where $c_p = 1.005\ \text{kJ/(kg K)}$ is the specific heat of air at constant pressure (typical value) and the temperatures are in kelvin.
- Turbine work per kilogram of air: $w_t = c_p (T_3 - T_4)$.
- Net work and heat input: $w_{\mathrm{net}} = w_t - w_c$ and $q_{\mathrm{in}} = c_p (T_3 - T_2)$, both in kilojoules per kilogram.
- Thrust: $F = \dot m (V_e - V_0) + (p_e - p_0) A_e$, where $F$ is in newtons, $\dot m$ is the air mass flow in kilograms per second, $V_e$ is the exit velocity in metres per second, $V_0$ is the flight speed in metres per second, $p_e$ and $p_0$ are the exit and ambient pressures in pascals, and $A_e$ is the exit area in square metres.
- Propulsive efficiency: $\eta_p = \dfrac{2 V_0}{V_e + V_0}$, dimensionless.
- Thrust specific fuel consumption: $\text{TSFC} = \dot m_f / F$, where $\dot m_f$ is the fuel mass flow in kilograms per second, so TSFC is in kilograms per newton second.

## Worked example

**Given:** Ambient air at $T_1 = 288\ \text{K}$ enters the compressor. The pressure ratio is $r_p = 12$, and the turbine inlet temperature is $T_3 = 1400\ \text{K}$. The air mass flow is $\dot m = 25\ \text{kg/s}$. Take $c_p = 1.005\ \text{kJ/(kg K)}$, $\gamma = 1.4$, and a fuel lower heating value of $\mathrm{LHV} = 43\ \text{MJ/kg}$ (typical value for jet fuel). Assume ideal, isentropic compression and expansion.

**Find:** (a) the temperatures $T_2$ and $T_4$, (b) the compressor and turbine work, (c) the net work and the net power, (d) the thermal efficiency, and (e) the fuel flow.

**Solution:**

1. Exponent: $(\gamma - 1)/\gamma = 0.4/1.4 = 0.2857$. Then $12^{0.2857} = 2.034$.
2. Compressor exit: $T_2 = T_1 \cdot 12^{0.2857} = 288 \times 2.034 = 585.8\ \text{K}$.
3. Turbine exit: $T_4 = T_3 / 12^{0.2857} = 1400 / 2.034 = 688.3\ \text{K}$.
4. Compressor work: $w_c = 1.005 \times (585.8 - 288) = 299.3\ \text{kJ/kg}$.
5. Turbine work: $w_t = 1.005 \times (1400 - 688.3) = 715.2\ \text{kJ/kg}$.
6. Net work: $w_{\mathrm{net}} = 715.2 - 299.3 = 416.0\ \text{kJ/kg}$. Net power: $25 \times 416.0 = 10\,400\ \text{kW}$, or 10.4 MW.
7. Heat input: $q_{\mathrm{in}} = 1.005 \times (1400 - 585.8) = 818.3\ \text{kJ/kg}$.
8. Thermal efficiency: $\eta = 416.0 / 818.3 = 0.508$, which matches $1 - 12^{-0.2857} = 0.508$.
9. Fuel flow: $\dot m_f = \dot m \, q_{\mathrm{in}} / \mathrm{LHV} = 25 \times 818.3 \times 10^{3} / (43 \times 10^{6}) = 0.476\ \text{kg/s}$, which is about 1700 kg/h. The fuel-to-air ratio is $q_{\mathrm{in}} / \mathrm{LHV} = 0.019$.

**Answer:** (a) $T_2 = 586\ \text{K}$, $T_4 = 688\ \text{K}$. (b) $w_c = 299\ \text{kJ/kg}$, $w_t = 715\ \text{kJ/kg}$. (c) $w_{\mathrm{net}} = 416\ \text{kJ/kg}$, net power 10.4 MW. (d) $\eta = 0.508$, or 50.8 percent. (e) About 0.48 kg/s of fuel.

**Sanity check:** The heat rejected is $c_p (T_4 - T_1) = 1.005 \times (688.3 - 288) = 402.3\ \text{kJ/kg}$. Then $q_{\mathrm{in}} - q_{\mathrm{out}} = 818.3 - 402.3 = 416.0\ \text{kJ/kg}$, which equals $w_{\mathrm{net}}$, so the energy balance closes. The efficiency of 0.508 is below the Carnot limit between 1400 K and 288 K, which is $1 - 288/1400 = 0.79$.

## Design trade-offs

- Pressure ratio and turbine inlet temperature: higher values raise the cycle efficiency. A higher turbine inlet temperature also needs better blade materials, more cooling air, and more frequent inspection. The cooling air bled from the compressor reduces the work the engine produces.
- Bypass ratio: a higher bypass ratio gives more efficient thrust and lower noise, but the fan is larger, adds drag and weight, and must fit under the wing. Designers balance these against each other for each aircraft.
- Thrust specific fuel consumption: this measures how much fuel an engine burns per unit of thrust. A lower TSFC cuts operating cost and emissions, and it is the main measure of engine efficiency for aircraft.
- Noise: jet noise rises with exhaust velocity, so the high-bypass design and the chevron nozzles reduce noise near airports.
- Life: hot-section parts have a limited life, and manufacturers set inspection and replacement intervals based on cycles and temperature.
- Emissions: nitrogen oxide forms at high flame temperature, so combustors use staged or lean-burn designs to keep the flame cooler.
- Size and weight: a gas turbine has a high power-to-weight ratio, which suits aircraft, but its efficiency drops at part load, which suits base-load power plants.

## How it fails

- Compressor stall and surge: when the airflow separates from the blades, the pressure falls and the flow reverses through the compressor. The result is a loud bang, a loss of thrust, and a rise in exhaust temperature. Causes include inlet distortion, ingestion of ice or debris, and a fuel schedule that runs too rich. Engines use variable stator vanes and bleed valves to keep a margin from surge.
- Turbine blade creep and overtemperature: at high temperature, blade metal stretches slowly until it fails. Warning signs are a rising exhaust gas temperature at the same power. Designers add cooling, coatings, and temperature limits, and they track blade life by operating hours and cycles.
- Foreign object damage: birds, ice, or stones in the inlet can strike fan or compressor blades. Fan cases and inlet screens reduce the risk.
- High-cycle fatigue: blades that vibrate at a resonant frequency crack from the cyclic stress. Designers tune blade frequencies away from the running speeds, and inspection finds cracks early.
- Uncontained rotor failure: a broken disk or blade can break through the casing. Certification rules require a containment ring around the fan and turbine, and aircraft carry fire and overspeed protection.
- Bearing or oil failure: chip detectors in the oil system catch metal debris before a bearing seizes, and oil system warnings alert the crew.

## History

Frank Whittle in England patented a jet engine design in 1930, and his first engine ran in 1937. In Germany, Hans von Ohain built a jet engine that ran in 1937, and the Heinkel He 178 made the first jet-powered flight in 1939. The Gloster E.28/39 flew in Britain in 1941 with a Whittle-type engine. The name Brayton cycle comes from George Brayton, an American engineer who built a reciprocating engine that burned liquid fuel in the 1870s. The same ideal cycle later became the standard model for the gas turbine.

## Practice

1. A turbofan takes in 40 kg/s of air at a flight speed of $V_0 = 200\ \text{m/s}$ and exhausts it at $V_e = 400\ \text{m/s}$. Ignore the pressure term. Find the thrust.
2. An engine has $V_e = 450\ \text{m/s}$ and flies at $V_0 = 250\ \text{m/s}$. Find its propulsive efficiency.
3. An ideal Brayton cycle has a pressure ratio of $r_p = 8$ and $\gamma = 1.4$. Find its thermal efficiency.
4. An engine burns 1.2 kg/s of fuel and produces a thrust of 10 kN. Find its TSFC in kilograms per newton hour.

<details><summary>Answers</summary>

1. $F = \dot m (V_e - V_0) = 40 \times (400 - 200) = 8000\ \text{N}$, or 8.0 kN.
2. $\eta_p = 2 \times 250 / (450 + 250) = 0.714$, or 71.4 percent.
3. $\eta = 1 - 8^{-0.2857} = 1 - 0.552 = 0.448$, or 44.8 percent.
4. $\text{TSFC} = 1.2 / 10\,000 = 1.2 \times 10^{-4}\ \text{kg/(N s)}$, which is $0.432\ \text{kg/(N h)}$.

</details>

## Common mistakes

- Using the flight speed as the exit velocity, or the reverse. The thrust equation uses the difference $V_e - V_0$.
- Reading the turbine work as the engine's output. The compressor takes a large share of the turbine work. In the worked example, the compressor takes 42 percent of the turbine work.
- Assuming a higher bypass ratio always wins. The fan adds drag and weight, so the best ratio depends on the aircraft and its mission.
- Judging an engine by thrust alone. TSFC and weight matter just as much for cost and range.
- Forgetting that thrust falls with air density. A jet produces less thrust at high altitude than at sea level, all else equal.

## Go deeper

- [Turbine Engine Thermodynamic Cycle, Brayton Cycle](https://www.grc.nasa.gov/www/k-12/airplane/brayton.html) by NASA Glenn Research Center: the gas turbine cycle, with T-s and p-V diagrams.
- [University Physics Volume 2, chapter 4 introduction, The Second Law of Thermodynamics](https://openstax.org/books/university-physics-volume-2/pages/4-introduction) by OpenStax: why the efficiency of any engine has a limit.
- Related lessons: [Internal combustion engines](06-internal-combustion-engines.md), [Steam power plants](08-steam-power-plants.md), [Aircraft and wings](../vehicles-aerospace/05-aircraft-and-wings.md), [Rockets](../vehicles-aerospace/07-rockets.md).
- [Applications reference](../reference.md): the lookup sheet for this topic.
