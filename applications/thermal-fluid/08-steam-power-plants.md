# Steam power plants

**Type:** lesson

A steam power plant heats water into steam, expands the steam through a turbine that turns a generator, and condenses the steam back into water to repeat the loop. Steam plants generate much of the world's electricity, so their efficiency, water use, and reliability shape the cost of power. The ideal loop is the Rankine cycle, and engineers use it to size boilers, turbines, condensers, and cooling systems.

**Prerequisites:** [Thermodynamics: properties, work, heat, and the first law](../../physics/08-thermo-first-law.md), [Thermodynamics: entropy, the second law, and cycles](../../physics/09-thermo-second-law-cycles.md), [Thermal systems](01-thermal-systems.md)
**Time:** 8-12 h

## Core ideas

### How it works

The Rankine cycle has four steps that repeat in a closed loop.

1. Pumping. A feedwater pump raises the pressure of the liquid water from the condenser pressure to the boiler pressure. Liquid water barely changes volume, so the pump needs very little work.
2. Heating. The boiler adds heat to the water at nearly constant pressure. The water warms, boils, and then the steam is superheated above the boiling temperature.
3. Expansion. The steam expands through the turbine and does work on the blades. Its pressure and temperature fall, and some of the steam may condense into droplets before it leaves.
4. Condensing. The condenser removes heat from the exhaust steam at nearly constant pressure, so the steam turns back into liquid water at low pressure.

Heat enters the water at a range of temperatures, not at one fixed temperature. For that reason, the Rankine cycle stays below the Carnot limit for the same top and bottom temperatures.

Two changes to the basic loop raise efficiency. Reheat sends partly expanded steam back to the boiler to be heated again before it enters a later turbine stage, which reduces the moisture in the low-pressure stages. Regeneration takes some steam from the turbine and uses it to heat the feedwater, so less heat must come from the boiler.

### Main parts

- The boiler, or steam generator, has an economizer that warms the feedwater, an evaporator that boils it, a superheater that raises the steam temperature, and sometimes a reheater.
- The fuel burner or nuclear core supplies the heat. Coal and gas burners in the boiler mix fuel with air. A pressurized water reactor heats water in a primary loop, and a separate steam generator makes the steam.
- The steam turbine has high-pressure, intermediate-pressure, and low-pressure sections on one or more shafts. Each section has rows of fixed nozzles and moving blades.
- The condenser is a large shell that holds bundles of tubes. Cooling water flows through the tubes, and the steam condenses on the outside.
- The cooling system removes heat from the condenser water. Wet cooling towers evaporate some of the water into the air. Dry cooling towers use air alone.
- The feedwater pumps, feedwater heaters, and deaerator prepare the water for the boiler.
- The generator converts the turbine's rotation into electricity.

### Variants

- Coal-fired, oil-fired, and gas-fired plants burn fuel in a boiler. Supercritical plants run at pressures above 22.1 MPa, the critical pressure of water, where the liquid and vapor phases do not separate.
- Nuclear plants use pressurized water reactors, where the primary water stays liquid under pressure, or boiling water reactors, where the steam forms in the reactor itself.
- Geothermal flash plants take hot water from underground and let it flash to steam at lower pressure.
- Combined-cycle plants run a gas turbine first and send its hot exhaust to a steam boiler. They reach higher efficiency than either cycle alone. See [Gas turbines and jet engines](07-gas-turbines-and-jet-engines.md).

## Key equations

Enthalpy $h$ and entropy $s$ are in kilojoules per kilogram and kilojoules per kilogram kelvin. Symbols are otherwise in SI units.

- Pump work: $w_p = v_f (P_2 - P_1)$, where $v_f$ is the specific volume of the liquid in cubic metres per kilogram and $P$ is in kilopascals. The result is in kilojoules per kilogram.
- Turbine work: $w_t = h_3 - h_4$, where $h_3$ is the steam enthalpy at the turbine inlet and $h_4$ is the enthalpy at the exit.
- Turbine isentropic efficiency: $\eta_T = \dfrac{h_3 - h_4}{h_3 - h_{4s}}$, dimensionless, where $h_{4s}$ is the exit enthalpy for an ideal, isentropic expansion.
- Steam quality for a wet mixture: $x = \dfrac{s - s_f}{s_{\mathrm{fg}}}$, dimensionless, where $s_f$ and $s_{\mathrm{fg}}$ are the entropy of saturated liquid and the entropy change on vaporization.
- Rankine efficiency: $\eta = \dfrac{w_t - w_p}{q_{\mathrm{in}}}$, dimensionless, where $q_{\mathrm{in}} = h_3 - h_2$ is the heat added in the boiler, with $h_2$ the enthalpy of the feedwater entering the boiler.
- Net power: $\dot W = \dot m \, w_{\mathrm{net}}$, where $\dot m$ is the steam mass flow in kilograms per second and $w_{\mathrm{net}}$ is in kilojoules per kilogram. The power is in kilowatts.
- Heat rate: $\mathrm{HR} = 3600 / \eta$, in kilojoules per kilowatt hour.
- Carnot limit: $\eta_C = 1 - T_C / T_H$, dimensionless, where $T_H$ and $T_C$ are the hot and cold temperatures in kelvin.

## Worked example

**Given:** A boiler delivers steam at 4.0 MPa and 400 °C ($T_H = 673.15\ \text{K}$). The condenser holds the steam at 10 kPa. The turbine and pump are isentropic, and the plant produces 50 MW of net power. Typical steam table values are:

- At 4.0 MPa and 400 °C: $h_3 = 3213.6\ \text{kJ/kg}$, $s_3 = 6.7690\ \text{kJ/(kg K)}$.
- Saturated liquid at 10 kPa: $h_f = 191.83\ \text{kJ/kg}$, $v_f = 0.00101\ \text{m}^3/\text{kg}$, $s_f = 0.6492\ \text{kJ/(kg K)}$, $h_{\mathrm{fg}} = 2392.8\ \text{kJ/kg}$, $s_{\mathrm{fg}} = 7.5009\ \text{kJ/(kg K)}$.

**Find:** (a) the pump work, (b) the turbine work, (c) the thermal efficiency, (d) the steam flow rate, and (e) the heat rate.

**Solution:**

1. Pump work: $w_p = 0.00101 \times (4000 - 10) = 4.03\ \text{kJ/kg}$. The feedwater enthalpy is $h_2 = 191.83 + 4.03 = 195.86\ \text{kJ/kg}$.
2. Exit quality for the isentropic expansion: $x = (6.7690 - 0.6492) / 7.5009 = 0.816$.
3. Exit enthalpy: $h_{4s} = 191.83 + 0.816 \times 2392.8 = 2144.1\ \text{kJ/kg}$.
4. Turbine work: $w_t = 3213.6 - 2144.1 = 1069.5\ \text{kJ/kg}$.
5. Heat input: $q_{\mathrm{in}} = 3213.6 - 195.86 = 3017.7\ \text{kJ/kg}$.
6. Net work: $w_{\mathrm{net}} = 1069.5 - 4.03 = 1065.5\ \text{kJ/kg}$.
7. Thermal efficiency: $\eta = 1065.5 / 3017.7 = 0.353$.
8. Steam flow: $\dot m = 50\,000\ \text{kW} / 1065.5\ \text{kJ/kg} = 46.9\ \text{kg/s}$.
9. Heat rate: $\mathrm{HR} = 3600 / 0.353 = 10\,200\ \text{kJ/kWh}$.

**Answer:** (a) 4.03 kJ/kg. (b) 1070 kJ/kg. (c) 35.3 percent. (d) 46.9 kg/s. (e) About 10 200 kJ/kWh.

**Sanity check:** The Carnot limit between 673.15 K and the condenser saturation temperature of about 319 K (45.8 °C at 10 kPa, typical value) is $1 - 318.96/673.15 = 0.526$. The Rankine efficiency of 0.353 lies below it, as expected. The pump work is 0.4 percent of the turbine work, which matches the small volume of liquid water. A real turbine with an isentropic efficiency of 0.88 (typical value) would give about 31 percent, so the ideal result is an upper bound for this plant.

## Design trade-offs

- Boiler pressure and temperature: higher values raise efficiency, but the boiler tubes and turbine casings must resist creep at high temperature and high pressure, which adds cost and weight. Supercritical coal plants reach efficiencies of about 40 percent (typical value).
- Condenser pressure: a lower exit pressure gives more turbine work. The lowest practical pressure is set by the cooling water temperature, because the condensing temperature cannot fall below the cooling water temperature.
- Cooling method: once-through cooling with river or sea water gives the best efficiency, but it heats the water and affects aquatic life. Wet cooling towers use less water than once-through cooling but lose water by evaporation. Dry cooling uses almost no water, but it costs more and gives a higher condensing temperature.
- Reheat and regeneration: reheat adds a second boiler section and piping. Regeneration adds feedwater heaters. Both raise efficiency by a few percentage points, and designers choose the number of stages that pays back the added cost.
- Emissions: sulfur dioxide, nitrogen oxides, and particulates from coal are removed by scrubbers, low-NOx burners, and electrostatic precipitators or fabric filters. Carbon dioxide capture is costly.
- Size and load following: large units of 500 MW to 1000 MW run best at steady load. Steam plants have high thermal inertia, so they start slowly and follow load changes slowly.

## How it fails

- Tube failure in the boiler: deposits and scale on the inside of the tubes block heat transfer, so the metal overheats, swells, and bursts. Warning signs include rising tube temperatures and leaks in the furnace. Plants control the water chemistry and monitor tube metal temperatures.
- Low water in the boiler drum: if the water level drops too low, the tubes can overheat and fail within seconds. Boilers carry low-water cutoffs that trip the burner before damage occurs.
- Overpressure: a stuck control valve or a fire can raise the pressure past the design limit. Code-sized safety relief valves open to protect the boiler, as the ASME Boiler and Pressure Vessel Code requires.
- Turbine blade erosion: water droplets in the low-pressure stages strike the blade edges at high speed and erode them. Moisture separators and reheat reduce the moisture.
- Overspeed: if the generator load drops suddenly, the turbine can speed up dangerously. Overspeed trip valves close the steam supply within a fraction of a second.
- Condenser leaks: seawater or cooling water that leaks into the steam contaminates the boiler water and corrodes the tubes. Condensers carry leak detection and a vacuum system that removes air that leaks in.
- Water hammer: a slug of liquid water in a steam line can strike a valve or bend at high speed when the steam flow starts. Steam lines need drains, slow warm-up, and proper pipe supports.
- Burns: the steam and hot piping can cause severe burns, so the plant uses insulation, guards, and lockout procedures for maintenance.

## History

Thomas Newcomen built an atmospheric steam engine in England about 1712, and it pumped water from mines. James Watt, working in Scotland, patented a separate condenser in 1769, which kept the cylinder hot and saved fuel. Sadi Carnot published his analysis of the limits on heat engines in France in 1824. William John Macquorn Rankine described the cycle that bears his name in the 1850s. Charles Parsons in England patented a practical steam turbine in 1884, and steam turbines then replaced reciprocating engines in large power stations.

## Practice

1. A heat engine runs between 600 K and 300 K. Find its Carnot efficiency.
2. A feedwater pump handles liquid water with $v_f = 0.001\ \text{m}^3/\text{kg}$ and raises the pressure from 10 kPa to 5000 kPa. Find the pump work in kilojoules per kilogram.
3. A plant produces 200 MW of net power, and the net work per kilogram of steam is 1000 kJ/kg. Find the steam flow in kilograms per second.
4. A plant has a thermal efficiency of 0.40. Find its heat rate in kilojoules per kilowatt hour.
5. Short answer: name two reasons a real Rankine plant falls below its Carnot limit.

<details><summary>Answers</summary>

1. $\eta_C = 1 - 300/600 = 0.50$, or 50 percent.
2. $w_p = 0.001 \times (5000 - 10) = 4.99\ \text{kJ/kg}$, or about 5.0 kJ/kg.
3. $\dot m = 200\,000\ \text{kW} / 1000\ \text{kJ/kg} = 200\ \text{kg/s}$.
4. $\mathrm{HR} = 3600 / 0.40 = 9000\ \text{kJ/kWh}$.
5. Any two of these: heat enters the water over a range of temperatures, so the average heat-addition temperature is below the top temperature. The pump and turbine lose energy to irreversibility. Wet steam at the turbine exit lowers the turbine's isentropic efficiency.

</details>

## Common mistakes

- Using the Carnot limit as the efficiency target for a real plant. Real plants reach well below it, and the gap reflects material limits and the shape of the heat-addition curve.
- Forgetting the unit conversion in the pump work. The formula $v (P_2 - P_1)$ gives kilojoules per kilogram only when the pressure is in kilopascals.
- Reading the turbine exit state from the wrong table. A saturated mixture uses the saturation table and quality $x$, and superheated steam uses the superheated table.
- Leaving out the pump work or counting the condenser as an energy producer. The condenser only rejects heat.
- Taking the white plume from a cooling tower for steam from the boiler. The plume is mostly water vapor from the cooling tower, and the boiler steam stays inside closed pipes.

## Go deeper

- [University Physics Volume 2, section 4.2, Heat Engines](https://openstax.org/books/university-physics-volume-2/pages/4-2-heat-engines) by OpenStax: how a heat engine converts heat to work and how efficiency is defined.
- [University Physics Volume 2, chapter 4 introduction, The Second Law of Thermodynamics](https://openstax.org/books/university-physics-volume-2/pages/4-introduction) by OpenStax: the limits that the Carnot and Rankine cycles describe.
- Related lessons: [Internal combustion engines](06-internal-combustion-engines.md), [Gas turbines and jet engines](07-gas-turbines-and-jet-engines.md), [Heat exchangers](05-heat-exchangers.md), [Pumps](09-pumps.md), [Piping and valves](12-piping-and-valves.md).
- [Applications reference](../reference.md): the lookup sheet for this topic.
