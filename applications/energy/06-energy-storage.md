# Energy storage

**Type:** lesson

Energy storage holds energy from one time and returns it at another, so supply can follow demand. Engineers use storage to smooth the output of solar and wind plants, to cover peak demand, and to keep a grid stable within seconds. Each technology stores energy in a different form, and the size of the store depends on both how much energy it holds and how fast it can deliver it.

**Prerequisites:** [Thermodynamics: properties, work, heat, and the first law](../../physics/08-thermo-first-law.md), [Hydrostatics and Bernoulli](../../physics/10-hydrostatics-and-bernoulli.md), [Rigid body dynamics](../../physics/03-rigid-body-dynamics.md)
**Time:** 8-10 h

## Core ideas

### How it works

Every store follows the same cycle. Energy goes in, the store holds it in some form, and energy comes out, with losses at each step. Four numbers describe most stores:

- **Energy capacity** is the total energy the store can hold, in kilowatt-hours or megawatt-hours.
- **Power rating** is the fastest rate the store can deliver, in kilowatts or megawatts.
- **Duration** is the energy capacity divided by the power rating. A 2 MW store holding 4 MWh runs for 2 hours at full power.
- **Round-trip efficiency** is the energy returned divided by the energy put in. A store with 80 percent round-trip efficiency returns 80 percent of what it took.

Grid storage falls into two groups. Short-duration stores, from seconds to about four hours, hold frequency and cover short peaks. Long-duration stores, from about four hours to days, shift solar output from noon into the evening.

Batteries store energy in chemical bonds that change as ions move between electrodes. Pumped hydro stores it as the potential energy of water raised uphill. Compressed air stores it as pressure in a cavern or tank. Thermal storage keeps energy as heat in a material such as molten salt or water. Flywheels store it as the rotational kinetic energy of a spinning mass.

### Main parts

- **Battery cells and management system.** Cells in modules and racks, with a battery management system that limits voltage and temperature and balances the cells.
- **Pumps and turbines.** Reversible pump-turbines move water between reservoirs and generate power on release. Motor-generators connect to the grid.
- **Reservoirs and penstocks.** An upper and lower reservoir, linked by a pipe called a penstock, with a height difference called head.
- **Compressors and expanders.** Compressors drive air into a cavern or tank. Expanders run the air through a turbine as it flows back out.
- **Heat exchangers and tanks.** Hot and cold storage tanks, pumps, and steam generators for thermal stores.
- **Rotor and bearings.** A steel or composite rotor spinning in a vacuum on magnetic or low-friction bearings.
- **Power electronics.** Inverters and converters that match the store to the grid frequency and voltage.

### Variants

| Technology | Typical round-trip efficiency | Typical duration | Notes |
|---|---|---|---|
| Lithium-ion battery | 85 to 95 percent | 1 to 4 hours | Fast response, modular, cost falls with production |
| Pumped hydro | 70 to 85 percent | 6 to 12 hours or more | Most of the storage capacity on the world's grids, needs a site with head |
| Compressed air | 40 to 70 percent | 4 to 12 hours | Needs a cavern or a large tank |
| Molten salt thermal | Set by the steam turbine | 6 to 12 hours | Used with concentrated solar power, stores heat |
| Flywheel | 85 to 90 percent | Seconds to minutes | High power, many cycles, loses energy to friction |

All values are typical, and designs vary widely.

## Key equations

Energy stored by raising mass $m$ in kilograms through height $h$ in metres, with $g = 9.81\ \text{m}/\text{s}^2$ (Earth surface):

$$E = m g h$$

For water with density $\rho = 1000\ \text{kg}/\text{m}^3$ and volume $V$ in cubic metres, the stored energy is $E = \rho g h V$ in joules. Convert to kilowatt-hours by dividing by $3.6 \times 10^{6}$.

Energy returned by a store, with round-trip efficiency $\eta_{\mathrm{rt}}$ (dimensionless):

$$E_{\mathrm{out}} = \eta_{\mathrm{rt}} E_{\mathrm{in}}$$

Rotational kinetic energy of a flywheel, with moment of inertia $I$ in kg m$^2$ and angular speed $\omega$ in rad/s:

$$E = \tfrac{1}{2} I \omega^2$$

For a solid disk of mass $m$ and radius $r$, $I = \tfrac{1}{2} m r^2$.

Battery energy, with nominal voltage $V_{\mathrm{nom}}$ in volts and capacity $Q$ in ampere-hours:

$$E = V_{\mathrm{nom}} Q\ \text{(in watt-hours)}$$

C-rate, the ratio of charge or discharge current $I$ to the nominal capacity $Q$ in ampere-hours. A 1C rate empties a fully charged battery in one hour:

$$C\text{-rate} = \frac{I}{Q}$$

Duration of a store, with energy capacity $E$ in MWh and power rating $P$ in MW:

$$t = \frac{E}{P}\ \text{hours}$$

## Worked example

**Given:** A pumped hydro scheme uses an upper reservoir of $V = 1.0 \times 10^{6}\ \text{m}^3$ of water with 500 m of head above the lower reservoir. The turbine rating is 200 MW. The round-trip efficiency is 0.80. Water density is $1000\ \text{kg}/\text{m}^3$, and $g = 9.81\ \text{m}/\text{s}^2$ (Earth surface).

**Find:** (a) the potential energy the reservoir holds, in GWh, (b) the energy the grid receives on discharge, in GWh, (c) the time the turbine runs at full power on one full reservoir, and (d) the grid energy needed to refill the reservoir.

**Solution:**

1. Potential energy: $E = \rho g h V = 1000 \times 9.81 \times 500 \times 1.0 \times 10^{6} = 4.905 \times 10^{12}\ \text{J}$. In kilowatt-hours, that is $4.905 \times 10^{12} / 3.6 \times 10^{6} = 1.36 \times 10^{6}\ \text{kWh}$, or 1.36 GWh.
2. Energy delivered: $E_{\mathrm{out}} = 0.80 \times 1.36\ \text{GWh} = 1.09\ \text{GWh}$.
3. Run time: $t = 1090\ \text{MWh} / 200\ \text{MW} = 5.45\ \text{h}$.
4. Refill energy: $E_{\mathrm{in}} = 1.36 / 0.80 = 1.70\ \text{GWh}$.

**Answer:** (a) 1.36 GWh. (b) 1.09 GWh. (c) About 5.5 hours at full power. (d) About 1.70 GWh from the grid.

**Sanity check:** Efficiency means the grid must supply more energy to refill the reservoir than the reservoir returns. $1.70 > 1.09$, so the balance holds. A run time of about 5.5 hours at 200 MW fits a daily peak. The reservoir holds $1.0 \times 10^{9}$ kg of water, which is a large body of water but within the scale of existing pumped hydro sites.

## Design trade-offs

- **Energy versus power.** A store sized for short peaks needs high power and little energy. A store sized for overnight shifting needs the reverse. Cost per kilowatt-hour and cost per kilowatt are separate costs, so designers choose the mix for the job.
- **Siting.** Pumped hydro needs two reservoirs with head, a water supply, and permits. It takes years to build. Batteries need little land and can go near load centres.
- **Cycle life.** Lithium-ion cells degrade with each cycle and with heat. Designers limit depth of discharge and temperature to reach thousands of cycles.
- **Storage losses.** Compressed air and some thermal systems lose heat during compression or storage, which lowers efficiency. Adiabatic designs keep and reuse that heat, at extra cost.
- **Self-discharge.** Flywheels lose energy to bearing friction and air drag. Pumped hydro and thermal stores lose very little over days. A flywheel suits minutes, not days.
- **Cost of heat.** Molten salt stores heat cheaply per kilowatt-hour, but the steam turbine that returns it to electricity sets the efficiency.

## How it fails

- **Battery thermal runaway.** A cell overheats, its electrolyte decomposes, and the heat spreads to neighboring cells. Warning signs include rising cell temperature, gas, and voltage drops. Designers use thermal monitoring, cell spacing, fire suppression, and venting.
- **Pumped hydro dam or penstock failure.** A failure releases a large volume of water. Designers monitor seepage, pressure, and seismic loads, and they inspect the dam and penstock on a set schedule.
- **Compressed air cavern leak or collapse.** A leaking or unstable cavern loses air or pressure. Operators monitor pressure and the rock mass around the cavern.
- **Flywheel burst.** A rotor spinning too fast can fail, and the rim stress is the limit. Designers use a vacuum enclosure, a containment ring, speed limits, and rotor balancing.
- **Molten salt freezing.** Solar salt freezes at about 220 °C, so cold spots in pipes can block flow. Trace heating and drain systems prevent it.

## History

Gaston Planté in France built the first practical rechargeable lead-acid battery in 1859. Sony began selling lithium-ion batteries in 1991. Pumped hydro grew through the twentieth century and remains the largest form of grid storage worldwide. The Huntorf plant in Germany began operating as a compressed air store in 1978, and it is one of the early large examples of this technology. Flywheels have smoothed machine speeds for centuries, and modern flywheels use composite rotors and magnetic bearings.

## Practice

Where a problem needs gravitational acceleration, use $g = 9.81\ \text{m}/\text{s}^2$ (Earth surface).

1. A battery stores 50 MWh. With a round-trip efficiency of 0.90, find the energy returned, in MWh.
2. A 2 MW battery stores 4 MWh. Find its duration in hours.
3. A reservoir holds $2.0 \times 10^{5}\ \text{m}^3$ of water with 300 m of head. Find the potential energy in MWh.
4. A solid steel disk of mass 500 kg and radius 0.5 m spins at 10 000 rpm. Find its kinetic energy in kilowatt-hours.
5. Explain in two or three sentences why pumped hydro needs a site with two reservoirs, and why a flat site with one tank would not work.

<details><summary>Answers</summary>

1. $E_{\mathrm{out}} = 0.90 \times 50 = 45\ \text{MWh}$.
2. $t = 4\ \text{MWh} / 2\ \text{MW} = 2\ \text{h}$.
3. $E = 1000 \times 9.81 \times 300 \times 2.0 \times 10^{5} = 5.89 \times 10^{11}\ \text{J}$, which is $163.5\ \text{MWh}$.
4. $I = \tfrac{1}{2} \times 500 \times 0.5^2 = 62.5\ \text{kg m}^2$ and $\omega = 2\pi \times 10\,000 / 60 = 1047\ \text{rad/s}$. Then $E = \tfrac{1}{2} \times 62.5 \times 1047^2 = 3.43 \times 10^{7}\ \text{J}$, which is 9.5 kWh.
5. Pumped hydro stores energy as the potential energy of water raised through a height difference. The energy depends on the head, so the water must move between two levels, and the lower reservoir receives the water on discharge and returns it on recharge. One tank cannot provide a head or a cycle.

</details>

## Common mistakes

- Using power rating where the energy capacity is needed. A 100 MW battery with 1 hour of storage holds 100 MWh, not 100 MW of energy.
- Applying round-trip efficiency to one direction only. The efficiency covers the full cycle, so the return is smaller than the input.
- Forgetting the pumping energy in a pumped hydro cycle. The grid must refill the upper reservoir, and that energy is larger than the energy returned.
- Assuming a flywheel stores energy for hours. Friction and drag drain it in minutes to hours, so flywheels suit short-duration work.
- Mixing watt-hours and ampere-hours. A battery's energy requires the nominal voltage times the ampere-hour rating.

## Go deeper

- [Pumped storage hydropower, U.S. Department of Energy](https://www.energy.gov/eere/water/pumped-storage-hydropower): how two reservoirs at different heights store and return energy.
- [Energy storage, U.S. Department of Energy](https://www.energy.gov/oe/energy-storage): an overview of grid storage technologies and roles.
- [Work and energy, OpenStax University Physics Volume 1, Chapter 7](https://openstax.org/books/university-physics-volume-1/pages/7-introduction): the kinetic energy and work concepts behind the flywheel equation.
- [Batteries](../electrical/06-batteries.md): cell chemistry, C-rate, and thermal runaway in more depth.
- [Solar photovoltaics](01-solar-photovoltaics.md) and [wind turbines](02-wind-turbines.md): the variable sources that storage smooths.
- [Hydroelectric power](03-hydroelectric-power.md): turbines and head in more detail.
- [Fuel cells and hydrogen](05-fuel-cells-and-hydrogen.md): hydrogen as a long-duration store.
- [Applications reference](../reference.md): the lookup sheet for this topic.
