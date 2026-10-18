# Batteries

**Type:** lesson

A battery stores chemical energy and releases it as electricity through two reactions at its electrodes. Engineers choose a battery by its energy, power, life, and safety, and lithium-ion cells need careful management because a fault can release heat fast enough to start a fire.

**Prerequisites:** [Electricity and magnetism](../../physics/06-electricity-and-magnetism.md), [Circuit basics](../electronics/01-circuit-basics.md), [Atomic structure and bonding](../../materials/01-atomic-structure-bonding.md)
**Time:** 4-6 h

## Core ideas

### How it works

A cell has two electrodes in contact with an electrolyte. At the anode, a material gives up electrons, which is oxidation. The electrons flow through the external circuit to the cathode, where a material takes them up, which is reduction. Ions move through the electrolyte to keep the charge balanced inside the cell. Charging drives current the other way and reverses both reactions.

A lead-acid cell has a lead anode, a lead dioxide cathode, and an electrolyte of sulfuric acid in water. During discharge, both electrodes turn into lead sulfate, and the acid is used up. The overall reaction is $\text{Pb} + \text{PbO}_2 + 2\,\text{H}_2\text{SO}_4 \rightarrow 2\,\text{PbSO}_4 + 2\,\text{H}_2\text{O}$. Each cell gives about 2.0 V (as of 2026, for this chemistry). Six cells in series give a 12 V battery.

A lithium-ion cell has a graphite anode and a lithium metal oxide cathode, with a lithium salt dissolved in an organic solvent. Lithium ions move in and out of the layered electrode materials, a process called intercalation. The electrode structure changes little, so the cell tolerates many cycles. Common cells give 3.6 to 3.7 V (as of 2026, for cobalt and nickel-based cells). Lithium iron phosphate cells give about 3.2 V (as of 2026).

Capacity is measured in amp-hours (Ah), the current a cell delivers for one hour. Energy is capacity times voltage, measured in watt-hours (Wh). A 12 V, 100 Ah battery stores 1200 Wh.

### Main parts

The electrodes hold the active material on a current collector. Lead-acid plates are lead grids pasted with lead oxide. Lithium-ion electrodes are a coating on copper foil at the anode and aluminum foil at the cathode.

The electrolyte carries ions between the electrodes. In lead-acid cells it is sulfuric acid. In lithium-ion cells it is a lithium salt in an organic solvent.

The separator is a porous membrane that keeps the electrodes apart and lets ions pass. Lithium-ion separators are polymer films. Some shut down their pores when the cell overheats, which slows the reaction (typical).

Lead-acid cases have vents that release hydrogen during overcharge. Vented cells need ventilation for that reason.

A battery management system, or BMS, measures each cell's voltage, the pack current, and the temperature. It limits charge and discharge, and it balances the cells in a series pack. Most lithium packs need one. Lead-acid packs usually need a charge controller instead.

Protective devices include fuses, contactors that disconnect the pack, and cell spacers or thermal barriers that slow heat spread between cells.

### Variants

Flooded lead-acid cells have liquid electrolyte and removable caps for adding water. Valve-regulated lead-acid (VRLA) cells are sealed, with the electrolyte held in a gel or a glass mat. Both are used for car starting, backup power, and forklifts (traction).

Lithium iron phosphate, or LFP, has a stable cathode and a long cycle life. It is common in stationary storage and in some electric vehicles (typical).

Lithium nickel manganese cobalt, or NMC, stores more energy per kilogram. It is common in electric vehicles and power tools (typical).

Lithium cobalt oxide cells store the most energy per volume and are common in phones and laptops (typical).

Nickel-metal hydride cells were common in earlier hybrid vehicles (typical). Alkaline cells are primary cells, which cannot be recharged safely.

## Key equations

Stored energy:

$$E = V_{nom}\, C$$

Here $E$ is the energy in watt-hours (Wh), $V_{nom}$ is the nominal voltage in volts, and $C$ is the rated capacity in amp-hours (Ah).

C-rate, the discharge current as a multiple of capacity:

$$I = C_{rate}\, C$$

Here $I$ is the current in amps, and $C_{rate}$ is the C-rate (dimensionless). A 1C current empties the rated capacity in about one hour. A 0.2C current takes about five hours.

Run time at constant load power:

$$t = \frac{E_{usable}}{P}$$

Here $t$ is the run time in hours, $P$ is the load power in watts, and $E_{usable}$ is the usable energy in watt-hours. Usable energy equals the stored energy times the depth of discharge, a fraction between 0 and 1.

Specific energy:

$$e_m = \frac{E}{m}$$

Here $e_m$ is specific energy in watt-hours per kilogram (Wh/kg), and $m$ is the mass in kilograms.

Round-trip energy efficiency:

$$\eta = \frac{E_{out}}{E_{in}}$$

Here $E_{out}$ is the energy delivered by the battery and $E_{in}$ is the energy put in during charging, both in watt-hours.

## Worked example

**Given:** A 12 V, 100 Ah flooded lead-acid battery with a mass of 30 kg. It powers a 240 W load, such as an inverter, at constant power. The design limits discharge to 50 percent depth of discharge to protect cycle life.

**Find:** (a) the stored energy, (b) the C-rate of the discharge current, (c) the run time from full charge down to 50 percent depth, (d) the specific energy of the battery, and (e) the run time if the full capacity is used.

**Assumptions:** The load power is constant. The inverter and internal resistance losses are ignored. The rated capacity applies at this discharge rate. Lead-acid cells deliver less capacity at higher rates, which this example ignores.

**Solution:**

1. Stored energy: $E = 12 \times 100 = 1200\ \text{Wh}$, which is 1.2 kWh.
2. Discharge current: $I = P / V = 240 / 12 = 20\ \text{A}$. The C-rate is $20 / 100 = 0.2\text{C}$.
3. Usable energy at 50 percent depth: $E_{usable} = 0.5 \times 1200 = 600\ \text{Wh}$. Run time: $t = 600 / 240 = 2.5\ \text{h}$.
4. Specific energy: $e_m = 1200 / 30 = 40\ \text{Wh/kg}$.
5. Full-depth run time: $t = 1200 / 240 = 5.0\ \text{h}$.

**Answer:** (a) 1.2 kWh. (b) 0.2C, which is 20 A. (c) 2.5 h. (d) 40 Wh/kg. (e) 5.0 h.

**Sanity check:** At 40 Wh/kg, this battery is at the low end of the typical lead-acid range (as of 2026). Gasoline stores about 46 MJ/kg, or about 12 800 Wh/kg (typical value), which is about 320 times more per kilogram than this battery. That gap is why fuel dominates where mass matters most.

## Design trade-offs

Specific energy sets how heavy a pack must be for a given run time. The typical ranges are below.

| Chemistry | Typical specific energy, Wh/kg (as of 2026) | Typical cycle life |
|---|---|---|
| Lead-acid, flooded or VRLA | about 30 to 50 | several hundred cycles at moderate depth of discharge |
| Lithium iron phosphate | about 120 to 180 | several thousand cycles |
| Lithium nickel manganese cobalt | about 200 to 270 | about 1000 to 2000 cycles |
| Gasoline, for comparison (not a battery) | about 12 800 | not applicable |

Energy and power pull against each other. Thick electrodes store more energy but deliver less current. Thin electrodes deliver high current for short bursts. Power tool packs favor power, and electric vehicle packs favor energy.

Cycle life depends on depth of discharge. A lead-acid battery lasts far more cycles at 50 percent depth than at 100 percent. Lithium iron phosphate tolerates deeper discharge than most other lithium chemistries (typical).

Cost has several parts. Lead-acid cells are cheap per unit of starting power, and lead-acid batteries are among the most recycled consumer products (typical). Lithium packs need a BMS, sensors, and often cooling, which add cost but allow higher energy per kilogram.

Temperature changes capacity. Lead-acid cells lose capacity in the cold. Lithium cells must not be charged below about 0 degrees Celsius, because lithium plates onto the anode and damages the cell (as of 2026, for typical graphite anodes).

Charge rate trades time for life. Fast charging raises heat and speeds aging, so packs limit the charge current when cold or hot.

The lightest chemistry is not always the safest. A design must weigh energy density against thermal stability, cost, and the risk to the people who use the pack.

## How it fails

Overcharging a flooded lead-acid cell splits water into hydrogen and oxygen. The electrolyte level falls, and the gas can ignite. Warning signs are a need to top up water often and a swollen or hot case. A charge controller limits the voltage, and the battery needs ventilation.

Sulfation happens when a lead-acid battery sits discharged for a long time. Large lead sulfate crystals form and reduce the capacity. Warning signs are falling capacity and slow charge acceptance. Keeping the battery charged and limiting depth of discharge prevent it.

Overcharging a lithium cell plates metal and can oxidize the cathode, which generates gas and can cause an internal short. A BMS cuts charge at a set voltage to prevent this.

Over-discharging a lithium cell dissolves copper from the anode current collector. The copper can later deposit and short the cell. An undervoltage cutoff in the BMS prevents this.

Thermal runaway starts with a short, heat, or damage. The protective film inside the anode breaks down and releases heat. The electrolyte decomposes, and the cathode can release oxygen, which feeds the fire. Warning signs are a swollen cell, rising temperature, hissing, and smoke. Measures include BMS cutoffs, temperature sensors, thermal barriers between cells, vents, separators that shut down, and fire-resistant enclosures.

Crushing or piercing a cell can short its electrodes through the separator. Pack enclosures and crash protection reduce this risk.

Cell imbalance in a series pack lets the weakest cell overcharge or over-discharge. A balancing circuit in the BMS evens out the charge across the cells.

Capacity fades with cycling, age, and high temperature. The first sign is a shorter range or run time, and a battery test shows how far it has faded.

## History

Alessandro Volta described his voltaic pile, the first electrochemical cell, in a letter to the Royal Society in London in 1800. Gaston Planté invented the lead-acid battery in France in 1859. M. Stanley Whittingham developed a titanium disulfide cathode at Exxon in the 1970s. John Goodenough identified lithium cobalt oxide as a cathode in 1980, and Akira Yoshino built a working cell with a carbon anode in 1985. Sony sold the first commercial lithium-ion cells in 1991. Goodenough, Whittingham, and Yoshino shared the 2019 Nobel Prize in Chemistry for the lithium-ion battery.

## Practice

1. A 12 V, 100 Ah battery is fully charged. Find its stored energy in watt-hours.
2. A lithium-ion cell has a nominal voltage of 3.7 V and a capacity of 3.0 Ah. Find its stored energy in watt-hours.
3. A 50 Ah battery discharges at 10 A. Find the C-rate and the time to empty the battery at this current.
4. A 48 V, 100 Ah lithium pack has a mass of 25 kg. Find its specific energy in Wh/kg.
5. A 12 V, 100 Ah lead-acid battery must run a 240 W load for 2 hours. The design limits discharge to 50 percent depth. Is the battery large enough? Show the energy needed and the usable energy.

<details><summary>Answers</summary>

1. 1200 Wh, from $E = 12 \times 100$.
2. 11.1 Wh, from $E = 3.7 \times 3.0$.
3. 0.2C, and 5 h, from $C_{rate} = 10 / 50$ and $t = 50 / 10$.
4. 192 Wh/kg, from $e_m = 4800 / 25$. This is a pack-level figure, which is lower than the cell-level value.
5. Yes. The load needs $240 \times 2 = 480\ \text{Wh}$. The usable energy is $0.5 \times 1200 = 600\ \text{Wh}$, which is larger than 480 Wh.

</details>

## Common mistakes

- Treating amp-hours as watt-hours. Energy needs the voltage: $\text{Wh} = V \times \text{Ah}$.
- Using nominal capacity as usable capacity. Depth of discharge, temperature, and discharge rate all reduce the usable energy.
- Confusing C-rate with the current in amps. A 0.5C rate on a 100 Ah battery is 50 A.
- Charging a lithium cell below freezing. This plates lithium metal onto the anode and damages the cell.
- Mixing lead-acid and lithium batteries in one system, or using one charger for both. The two chemistries need different charge profiles and voltage limits.

## Go deeper

- [Vehicle Technologies Office, Batteries](https://energy.gov/eere/vehicles/batteries), U.S. Department of Energy. Free overview of lithium-ion research, cost and performance targets, and durability.
- [10.626 Electrochemical Energy Systems, Spring 2014](https://ocw.mit.edu/courses/10-626-electrochemical-energy-systems-spring-2014/), MIT OpenCourseWare. Free graduate course on battery thermodynamics, kinetics, and transport, with lithium-ion lecture notes.
- [Batteries and Fuel Cells](https://chem.libretexts.org/Courses/University_of_Toronto/UTSC%3A_First-Year_Chemistry_Textbook_%28Fall_2025%29/18%3A_Electrochemistry/18.06%3A_Batteries_and_Fuel_Cells), LibreTexts. Free introduction to primary and secondary cells, including lead-acid and lithium-ion.
- Related lessons: [power supplies and converters](07-power-supplies-and-converters.md), [energy storage](../energy/06-energy-storage.md), [electric vehicles](../vehicles-aerospace/04-electric-vehicles.md).
