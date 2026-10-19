# Fuel cells and hydrogen

**Type:** lesson

Fuel cells and hydrogen are the technologies for making electricity from hydrogen and for storing energy as that gas. Whether such a system works depends on the cell physics, the catalyst, and the pressure of the stored gas, so each must be sized with care.

A fuel cell turns hydrogen and oxygen into electricity and water with no combustion and no moving parts. Hydrogen also stores energy from solar or wind power when an electrolyzer splits water and a fuel cell later turns the gas back into electricity.

**Prerequisites:** [Atomic structure and bonding](../../materials/01-atomic-structure-bonding.md), [Electricity and magnetism](../../physics/06-electricity-and-magnetism.md), [Thermodynamics: properties, work, heat, and the first law](../../physics/08-thermo-first-law.md), [Mechanical properties](../../materials/03-mechanical-properties.md)
**Time:** 8-10 h

## Core ideas

### How it works

A proton exchange membrane (PEM) fuel cell has two electrodes separated by a thin polymer membrane. The membrane conducts protons (hydrogen ions) and blocks electrons. Each electrode carries a catalyst, usually platinum, that speeds up the reaction.

At the anode, each hydrogen molecule splits into two protons and two electrons:

$$\text{H}_2 \rightarrow 2\text{H}^+ + 2\text{e}^-$$

The protons cross the membrane. The electrons cannot cross it, so they travel through an external circuit and do useful work. At the cathode, oxygen from the air combines with the protons and the returning electrons to form water:

$$\tfrac{1}{2}\text{O}_2 + 2\text{H}^+ + 2\text{e}^- \rightarrow \text{H}_2\text{O}$$

The electrons in the external circuit are the current. The chemistry releases energy because water has less chemical energy than hydrogen and oxygen together. The cell turns that energy into electricity and heat directly, without a heat engine. A single PEM cell produces about 0.6 to 0.7 V under load. Engineers stack many cells in series to reach useful voltages.

Each cell runs at about 60 to 80 °C. The membrane must stay wet to conduct protons, so the gas streams are humidified, and the cooling loop keeps the temperature in range.

Electrolysis runs the same reactions in reverse. Electricity drives water into hydrogen at the cathode and oxygen at the anode. A PEM electrolyzer does this with a similar membrane and catalyst layers.

### Main parts

- **Membrane electrode assembly.** The membrane with a catalyst layer on each side. Modern designs use a fraction of a milligram of platinum per square centimetre.
- **Gas diffusion layers.** Porous carbon sheets that spread the gas to the catalyst and carry water and electrons away.
- **Bipolar plates.** Graphite or coated metal plates with flow channels. They separate the cells, carry the current from one cell to the next, and route the gases.
- **Air and hydrogen supply.** A compressor or blower feeds air. A regulator and recirculation pump feed hydrogen from the storage tank.
- **Humidifier and cooling loop.** These keep the membrane wet and the temperature near 70 °C.
- **Power electronics.** A converter steps the stack voltage up or down and matches the load.

### Variants

- **PEM fuel cells.** Low operating temperature, fast start, and high power density. Used in cars, buses, and some forklifts and backup systems.
- **Solid oxide fuel cells.** Operate at 700 to 1000 °C, can run on natural gas after reforming, and suit stationary power plants with heat recovery.
- **Alkaline fuel cells.** Used in the Apollo spacecraft. They need pure hydrogen and oxygen because carbon dioxide ruins the electrolyte.
- **PEM electrolyzers.** Split water with electricity. They respond quickly to changes in renewable power output.
- **Alkaline electrolyzers.** Older and cheaper, with a liquid electrolyte, but they respond more slowly.

## Key equations

Faraday's law gives the hydrogen consumed by a current $I$ in amperes, over time $t$ in seconds. Here $M = 2.016\ \text{g/mol}$ is the molar mass of H$_2$, $n = 2$ is the number of electrons per molecule, and $F = 96\,485\ \text{C/mol}$ is the Faraday constant:

$$m = \frac{I\,t\,M}{n\,F}$$

Cell voltage and electrical power, with $V$ in volts and $I$ in amperes:

$$P_{\mathrm{el}} = V I$$

Efficiency on the lower heating value (LHV) basis. The constant 1.25 V equals the LHV energy of one mole of hydrogen, 241.8 kJ/mol, divided by $2F$:

$$\eta_{\mathrm{LHV}} = \frac{V_{\mathrm{cell}}}{1.25\ \text{V}}$$

Hydrogen energy content on the LHV basis is about 120 MJ/kg, or 33.3 kWh/kg. The higher heating value (HHV) is about 142 MJ/kg, or 39.4 kWh/kg. Both are typical values.

Electrolyzer hydrogen output, with $\eta_{\mathrm{LHV}}$ the electrolyzer efficiency on the LHV basis and $E_{\mathrm{in}}$ the electric energy input in kilowatt-hours:

$$m_{H_2} = \frac{\eta_{\mathrm{LHV}}\,E_{\mathrm{in}}}{33.3\ \text{kWh/kg}}$$

Gas storage, with $\rho$ the gas density in kg/m$^3$ and $m$ the mass in kg:

$$V = \frac{m}{\rho}$$

## Worked example

**Given:** A 1 MW PEM electrolyzer runs for one hour at full power with an LHV efficiency of 0.65. The hydrogen goes into a tank at 700 bar. Hydrogen at 700 bar has a typical density of $40\ \text{kg}/\text{m}^3$.

**Find:** (a) the mass of hydrogen produced in one hour, and (b) the tank volume needed to store it.

**Solution:**

1. Electric energy input: $E_{\mathrm{in}} = 1000\ \text{kW} \times 1\ \text{h} = 1000\ \text{kWh}$.
2. Hydrogen mass: $m = 0.65 \times 1000 / 33.3 = 19.5\ \text{kg}$.
3. Tank volume: $V = 19.5 / 40 = 0.49\ \text{m}^3$, which is 490 litres.

**Answer:** (a) 19.5 kg of hydrogen. (b) About 0.49 m$^3$ of storage at 700 bar.

**Sanity check:** The stored energy is $19.5 \times 33.3 = 650\ \text{kWh}$, which is 65 percent of the 1000 kWh input. That matches the efficiency. A fuel cell running on this hydrogen would return less electricity than went in. Hydrogen is a store with losses, not a source.

Second check, using Faraday's law for a single stack current: a current of 100 A consumes $m = 100 \times 3600 \times 2.016 / (2 \times 96\,485) = 3.76\ \text{g/h}$ of hydrogen. At 0.7 V per cell, the cell produces $P = 70\ \text{W}$. The hydrogen carries $3.76\ \text{g/h} \times 33.3\ \text{kWh/kg} = 125\ \text{W}$, so the efficiency is $70 / 125 = 0.56$, which matches $0.7 / 1.25$.

## Design trade-offs

- **Platinum loading.** Platinum catalyst is expensive and scarce. Thinner catalyst layers lower the cost but can lose performance, and designers balance the two.
- **Operating voltage.** Higher cell voltage means higher efficiency but lower current for the same power, which changes the stack size and cost. A PEM cell at 0.6 V gives 48 percent LHV efficiency, and at 0.7 V it gives 56 percent.
- **Carbon monoxide tolerance.** Platinum catalysts poison in the presence of carbon monoxide, which a hydrogen stream from reformed natural gas can contain. Those systems need a clean-up reactor.
- **Storage pressure.** Hydrogen has a low density. At atmospheric pressure it holds about 0.09 kg/m$^3$, or about 10.8 MJ/m$^3$. At 700 bar it holds about 40 kg/m$^3$, or about 4.8 GJ/m$^3$. Gasoline holds about 32.6 GJ/m$^3$, so 700 bar hydrogen stores about one seventh of the energy per volume of gasoline. Higher pressure needs thicker tanks, which add weight and cost.
- **Liquid hydrogen.** Liquefying hydrogen at about 20 K raises the density, but cooling the gas consumes a large share of its energy and the boil-off losses are significant.
- **Metal hydrides and carriers.** Store hydrogen in solids or chemical carriers. These are safer and compact, but they are heavy and need heat to release the gas.
- **Stack life.** Membranes dry out, catalysts degrade, and start-stop cycles stress the cell. Automotive stacks are designed for several thousand hours of operation.

## How it fails

- **Membrane dry-out.** A dry membrane stops conducting protons, and the cell voltage drops. Warning signs include a rising stack resistance and a falling voltage at constant current. Designers add humidifiers and current limits.
- **Hydrogen leaks.** Hydrogen is light, burns over a wide range of mixtures in air, and needs only a small spark to ignite. Sensors detect leaks, and ventilation and automatic shutoff valves limit the risk.
- **Hydrogen embrittlement.** Some metals absorb hydrogen and lose ductility, which can cause cracks at stress levels that would be safe in air. Tank and piping materials are chosen and tested for this effect.
- **Fuel starvation.** A blocked flow channel or low hydrogen pressure starves part of the cell. The cell can reverse and damage its catalyst. Stack monitoring of individual cell voltages catches this early.
- **Water flooding.** Too much liquid water blocks the gas diffusion layer and cuts performance at high current. Gas flow rates and cell temperature are controlled to prevent it.

Safety measures come from these failure modes: sensors and shutoff valves for leaks, pressure relief devices on storage tanks, grounding and ventilation, and certified tank standards.

## History

William Grove described a gas voltaic battery in 1839, which is generally regarded as the first fuel cell. The technology stayed mostly in the laboratory for more than a century. General Electric developed a PEM cell for NASA's Gemini program in the early 1960s. The Apollo spacecraft used alkaline fuel cells built by Pratt and Whitney to supply electricity and drinking water. Later decades brought PEM stacks for vehicles and stationary power.

## Practice

1. A stack has a cell voltage of 0.65 V and a current of 50 A. Find its electric power in watts.
2. A fuel cell draws 50 A continuously. Find the hydrogen mass consumed per hour, in grams.
3. A 2 MW electrolyzer runs at 60 percent LHV efficiency for one hour. Find the hydrogen mass produced, in kilograms.
4. Explain in two or three sentences why PEM fuel cells use platinum and why they need pure hydrogen.
5. A PEM cell runs at 0.80 V on the LHV basis. Find its efficiency.

<details><summary>Answers</summary>

1. $P = 0.65 \times 50 = 32.5\ \text{W}$.
2. $m = 50 \times 3600 \times 2.016 / (2 \times 96\,485) = 1.88\ \text{g/h}$.
3. $m = 0.60 \times 2000 / 33.3 = 36.0\ \text{kg}$ per hour.
4. Platinum speeds up the oxygen reduction and the hydrogen oxidation at low temperature, where other materials react too slowly. Carbon monoxide blocks the platinum surface, so the hydrogen must be clean.
5. $\eta = 0.80 / 1.25 = 0.64$, or 64 percent.

</details>

## Common mistakes

- Using the higher heating value where the lower heating value is needed, or the reverse. Fuel cell and electrolyzer efficiencies are usually quoted on the LHV basis.
- Treating a fuel cell as a battery that stores energy. It converts fuel that must be supplied from a tank.
- Forgetting that a cell voltage is about 0.7 V under load, not the 1.23 V ideal reversible voltage.
- Comparing hydrogen by mass without considering volume. At 700 bar, hydrogen holds about one seventh of the energy per volume of gasoline.
- Assuming a round trip from electricity to hydrogen and back returns most of the energy. An electrolyzer at 65 percent and a fuel cell at 56 percent return about one third of the input.

## Go deeper

- [Fuel cells, U.S. Department of Energy](https://www.energy.gov/eere/fuelcells/fuel-cells): a general overview of how fuel cells produce electricity from hydrogen.
- [Types of fuel cells, U.S. Department of Energy](https://www.energy.gov/eere/fuelcells/types-fuel-cells): the PEM, solid oxide, and other cell types, with their operating ranges.
- [Hydrogen production by electrolysis, U.S. Department of Energy](https://www.energy.gov/eere/fuelcells/hydrogen-production-electrolysis): how PEM and other electrolyzers work.
- [Hydrogen storage, U.S. Department of Energy](https://www.energy.gov/eere/fuelcells/hydrogen-storage): compressed, liquid, and materials-based storage.
- [Batteries](../electrical/06-batteries.md): the other way to store electrical energy, for comparison.
- [Energy storage](06-energy-storage.md): where hydrogen fits among grid storage options.
- [Applications reference](../reference.md): the lookup sheet for this topic.
