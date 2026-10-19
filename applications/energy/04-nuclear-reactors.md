# Nuclear reactors

**Type:** lesson

A nuclear reactor turns the energy released when heavy atoms split into heat, and that heat makes steam for a turbine. Engineers need to understand reactors because the design work comes down to two balances: the neutron balance that keeps the chain reaction steady, and the heat balance that keeps the fuel cool in every operating state.

**Prerequisites:** [Atomic structure and bonding](../../materials/01-atomic-structure-bonding.md), [Thermodynamics: properties, work, heat, and the first law](../../physics/08-thermo-first-law.md), [Thermodynamics: entropy, the second law, and cycles](../../physics/09-thermo-second-law-cycles.md), [Heat transfer](../../physics/12-heat-transfer.md)
**Time:** 8-10 h

## Core ideas

### How it works

A neutron strikes a uranium-235 nucleus, which splits into two smaller nuclei, two or three new neutrons, and about 200 MeV of energy. That is about $3.2 \times 10^{-11}\ \text{J}$ per fission. Most of the energy appears as the kinetic energy of the fission fragments. The fragments slow down inside the fuel and heat it.

The new neutrons drive the chain reaction. If, on average, exactly one neutron from each fission causes another fission, the reactor is critical. The power then stays constant. If more than one does, the power rises. If fewer do, the power falls.

Fission neutrons leave the nucleus fast, at about 2 MeV. U-235 is much more likely to fission when the neutron is slow, so the reactor uses a moderator to slow the neutrons to thermal energies near 0.025 eV. In a pressurized water reactor, ordinary water does this job. The same water also carries the heat away.

Step by step, one cycle of heat moves like this:

1. Fission heats the uranium oxide pellets to temperatures above 1000 °C at the center.
2. Heat flows through the pellet and the zirconium alloy cladding into the coolant.
3. Primary coolant at about 15.5 MPa stays liquid at about 320 °C. It is kept under pressure so it does not boil in the core.
4. Hot primary water flows through tubes in a steam generator. Heat passes through the tube walls into secondary water, which boils at a lower pressure.
5. Steam drives the turbine. A condenser cools the steam back to water, and feedwater pumps return it to the steam generator.

The secondary loop never touches the fuel. That keeps radioactive primary water out of the turbine hall. The turbine and condenser follow the Rankine cycle, covered in the [steam power plants lesson](../thermal-fluid/08-steam-power-plants.md).

Control works through neutron absorbers. Control rods made of boron carbide or silver-indium-cadmium alloy slide into the core and capture neutrons. Pulling rods out raises the reactivity. Pressurized water reactors also dissolve boric acid in the coolant, and the operators adjust its concentration to hold the reactivity over a fuel cycle.

The fuel has a negative temperature coefficient. When the fuel or water heats up, the reactivity falls. This self-correction keeps the power from running away after a small disturbance.

### Main parts

- **Fuel assemblies.** Uranium dioxide pellets, enriched to about 3 to 5 percent U-235, stack inside zirconium alloy tubes called fuel rods. A pressurized water reactor assembly holds a square array of rods, commonly 17 by 17.
- **Reactor pressure vessel.** A thick low-alloy steel shell that holds the core and the coolant under pressure.
- **Control rods and drive mechanisms.** Absorber rods that move in and out of the core, driven by motors on the vessel head.
- **Reactor coolant pumps.** Circulate primary water through the core and the steam generators.
- **Steam generators.** Thousands of U-tubes carry hot primary water and transfer its heat to secondary water.
- **Pressurizer.** A vessel with electric heaters and spray nozzles that sets and holds the primary pressure.
- **Containment.** A steel-lined concrete structure around the primary system, built to hold released steam and radioactive material.
- **Emergency systems.** Backup power from diesel generators and batteries, pumps for emergency core cooling, and systems that remove decay heat.

### Variants

- **Pressurized water reactor (PWR).** Primary water at high pressure transfers heat to a separate steam loop. It is the most common type in operation.
- **Boiling water reactor (BWR).** Water boils inside the core at about 7 MPa. The steam goes straight to the turbine, which simplifies the plant but puts radioactive steam in the turbine hall.
- **Pressurized heavy water reactor (CANDU design).** Uses heavy water as moderator and coolant, which allows natural uranium fuel without enrichment.
- **Gas-cooled and fast reactors.** Use helium or liquid metal coolants to reach higher temperatures or to breed fuel. Most are at the demonstration or early commercial stage.
- **Small modular reactors.** PWR and other designs built in factories at smaller sizes, typically below 300 MWe per unit. Most are under development and few are operating.

## Key equations

Energy per fission, with $E_f$ in joules:

$$E_f \approx 200\ \text{MeV} = 200 \times 10^{6} \times 1.602 \times 10^{-19}\ \text{J} = 3.20 \times 10^{-11}\ \text{J}$$

Energy from fully fissioning one kilogram of U-235, with $N_A = 6.022 \times 10^{23}\ \text{mol}^{-1}$ (Avogadro's number), $M = 0.23504\ \text{kg/mol}$ (molar mass of U-235), and $m = 1\ \text{kg}$:

$$E_m = \frac{m}{M} N_A E_f = \frac{1}{0.23504} \times 6.022 \times 10^{23} \times 3.20 \times 10^{-11}\ \text{J/kg} \approx 8.2 \times 10^{13}\ \text{J/kg}$$

Thermal power, with $\dot{N}_f$ the fission rate in fissions per second:

$$P_{\mathrm{th}} = \dot{N}_f E_f$$

Electric power, with $\eta$ the thermal efficiency (dimensionless):

$$P_e = \eta P_{\mathrm{th}}$$

Heat rejected to the environment, in watts:

$$Q_{\mathrm{rej}} = P_{\mathrm{th}} - P_e$$

Reactivity, with $k$ the effective neutron multiplication factor (dimensionless):

$$\rho_r = \frac{k - 1}{k}$$

Here $k = 1$ means critical, $k > 1$ means the power rises, and $k < 1$ means the power falls. After shutdown, decay heat from fission products still adds roughly 6 percent of full thermal power in the first seconds. That fraction falls over hours and days.

## Worked example

**Given:** A 1 GWe pressurized water reactor with thermal efficiency $\eta = 0.33$ runs at a capacity factor of 0.90. Assume every fission releases 200 MeV, all of it from U-235. Ignore neutron capture in U-238 and any plutonium fissions. One year is $365.25\ \text{days} = 3.156 \times 10^{7}\ \text{s}$.

**Find:** (a) the thermal power, (b) the heat rejected at full electric output, and (c) the mass of U-235 fissioned in one year.

**Solution:**

1. Thermal power: $P_{\mathrm{th}} = P_e / \eta = 1.00 \times 10^{9} / 0.33 = 3.03 \times 10^{9}\ \text{W}$.
2. Heat rejected: $Q_{\mathrm{rej}} = 3.03\ \text{GW} - 1.00\ \text{GW} = 2.03\ \text{GW}$.
3. Energy in one year at 90 percent capacity: $E_{\mathrm{yr}} = 0.90 \times 3.03 \times 10^{9} \times 3.156 \times 10^{7} = 8.61 \times 10^{16}\ \text{J}$.
4. Mass fissioned: $m = E_{\mathrm{yr}} / E_m = 8.61 \times 10^{16} / 8.21 \times 10^{13} = 1.05 \times 10^{3}\ \text{kg}$.

**Answer:** (a) 3.03 GW. (b) 2.03 GW. (c) About 1.05 tonnes of U-235 per year.

**Sanity check:** Heat rejected is larger than electric output, as the efficiency below 1 requires. A plant of this size loads about 20 to 30 tonnes of fuel a year at 3 to 5 percent enrichment. That fuel holds roughly 1 tonne of U-235, which matches the mass found here.

## Design trade-offs

- **Enrichment.** Higher U-235 content lets the core run longer between refuelings or hold less fuel. The cost of enrichment rises, and high-enrichment fuel raises proliferation concerns, so commercial reactors stay below about 5 percent.
- **Operating pressure and temperature.** Water at 15.5 MPa stays liquid at about 320 °C. Higher pressure allows hotter water but needs thicker vessel walls and piping, which raises cost and weight.
- **Efficiency.** Light water reactors reach about 33 percent thermal efficiency because the steam temperature is limited. Gas-cooled and supercritical designs can reach higher temperatures and efficiencies, at the cost of new materials.
- **Power density.** A PWR core produces about 100 MW of heat per cubic metre, which keeps the vessel compact but makes cooling demanding.
- **Redundancy.** Multiple pumps, diesel generators, and trains of safety systems add cost. Operators accept that cost because one failure must not lead to core damage.
- **Refueling and outages.** Plants typically refuel every 18 to 24 months. Long outages cost money, so designers aim for fuel that lasts and components that need little maintenance.
- **Waste.** Spent fuel stays radioactive for thousands of years. It is stored in water pools and then in dry casks, which adds long-term cost.

## How it fails

- **Loss of coolant.** A break in primary piping drains water from the core. Without cooling, the fuel overheats and the cladding can fail. Emergency core cooling systems inject water, and the containment holds the released steam and fission products.
- **Loss of power.** When offsite power stops, the pumps stop. Diesel generators and batteries drive the emergency pumps, and the plant removes decay heat through separate paths.
- **Zirconium-steam reaction.** Above about 1200 °C, zirconium cladding reacts with steam and releases hydrogen and heat. Containment hydrogen recombiners and vents limit the buildup. The hydrogen explosions at Fukushima Daiichi in March 2011 came from this reaction after the cooling failed.
- **Stuck valve.** At Three Mile Island Unit 2 in Pennsylvania in March 1979, a relief valve stuck open. Operators misread the instruments, and part of the core melted.
- **Unsafe design and test.** The Chernobyl Unit 4 reactor in April 1986 had a positive void coefficient and a design that let operators run it unsafely during a test. The accident released radioactive material over a wide area. Western PWRs have a negative temperature coefficient, which is one reason they do not share this failure.

Warning signs include falling coolant level, rising primary pressure, high temperature at the core outlet, and rising radiation readings. The safety measures that exist because of these failures include defense in depth, independent cooling paths, backup power, containment, and operator training on simulators.

## History

In December 1938, Otto Hahn and Fritz Strassmann in Berlin found barium among the products when they bombarded uranium with neutrons. Lise Meitner and Otto Frisch explained early in 1939 that the nucleus had split, and they named the process fission. Enrico Fermi and his team at the University of Chicago started Chicago Pile-1 on 2 December 1942, the first self-sustaining chain reaction. The first full-scale pressurized water reactor for commercial power in the United States began operating at Shippingport, Pennsylvania, in 1957.

## Practice

1. A 1 GWe plant has thermal efficiency 0.33. Find the heat rejected per second, in gigawatts.
2. Find the mass of coal, at 30 MJ/kg, that releases the same energy as 1 kg of U-235 fully fissioned.
3. A reactor produces 1 MW of thermal power. Find the number of fissions per second.
4. A reactor produces 1 MW of thermal power for one full day. Find the mass of U-235 fissioned, in grams.
5. Explain in two or three sentences why a pressurized water reactor uses light water both as moderator and as coolant.

<details><summary>Answers</summary>

1. $Q_{\mathrm{rej}} = 1.00/0.33 - 1.00 = 2.03\ \text{GW}$.
2. $8.21 \times 10^{13} / 3.0 \times 10^{7} = 2.74 \times 10^{6}\ \text{kg}$, about 2.7 million kilograms of coal.
3. $1 \times 10^{6} / 3.20 \times 10^{-11} = 3.12 \times 10^{16}$ fissions per second.
4. Energy per day is $1 \times 10^{6} \times 86\,400 = 8.64 \times 10^{10}\ \text{J}$. Mass is $8.64 \times 10^{10} / 8.21 \times 10^{13} = 1.05 \times 10^{-3}\ \text{kg}$, which is about 1.05 g.
5. Water slows the fast fission neutrons so that U-235 captures them more readily, which sustains the chain reaction. The same water carries the heat from the core. Its high density and heat capacity make it a good coolant, and its pressure keeps it liquid at high temperature.

</details>

## Common mistakes

- Treating reactor fuel as pure U-235. Commercial fuel is 3 to 5 percent U-235 by mass, and the rest is mostly U-238.
- Using electric power where the energy balance needs thermal power. Divide the electric output by the efficiency to get the heat input.
- Assuming a reactor can explode like a nuclear weapon. Reactor fuel is not enriched enough, and the geometry does not allow an uncontrolled chain reaction of that kind.
- Confusing criticality with high power. Critical means the neutron population is steady, and the power level depends on how the operators set it.
- Forgetting decay heat after shutdown. About 6 percent of full power remains right after shutdown, so cooling must continue for days.

## Go deeper

- [University Physics Volume 3, Chapter 10 introduction](https://openstax.org/books/university-physics-volume-3/pages/10-introduction), free from OpenStax. It covers the atomic nucleus and introduces fission.
- [Steam power plants](../thermal-fluid/08-steam-power-plants.md): the Rankine cycle that turns reactor heat into electricity.
- [The power grid](../electrical/08-the-power-grid.md): how generated power reaches the load.
- [Heat transfer](../../physics/12-heat-transfer.md): conduction through fuel and cladding, and convection to the coolant.
- [Applications reference](../reference.md): the lookup sheet for this topic.
