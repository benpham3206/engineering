# Solar photovoltaics

**Type:** lesson

A photovoltaic (PV) cell turns sunlight directly into electricity with no moving parts and no heat engine. Engineers size PV arrays by the power a panel makes at a given sunlight level, and they check how much energy a site yields over a day or a year.

**Prerequisites:** [Electricity and magnetism](../../physics/06-electricity-and-magnetism.md), [Oscillations, waves, light, and heat](../../physics/07-waves-light-heat.md), [Heat transfer](../../physics/12-heat-transfer.md)
**Time:** 6-8 h

## Core ideas

### How it works

Light is a stream of photons. A photon with enough energy knocks an electron loose in a semiconductor, which creates an electron and a hole. A cell has two regions with different doping. The p-type side has extra holes, and the n-type side has extra electrons. The junction between them forms a built-in electric field. That field pushes the freed electrons toward the n side and the holes toward the p side. An external circuit connected to the two sides carries the current back through the load.

The steps run in order:

1. Sunlight strikes the cell. Photons with energy above the semiconductor's band gap create electron-hole pairs. For crystalline silicon the band gap is about 1.1 eV (typical value).
2. The junction's electric field separates the charges before they recombine.
3. Metal contacts on the front and back collect the current.
4. The cell delivers a voltage of about 0.6 V under load (typical value for one silicon cell). Cells are wired in series to reach useful voltages.

Photons with less energy than the band gap pass through without producing current. Photons with more energy than the band gap give up the extra energy as heat. Both effects limit efficiency.

### Main parts

- **Cells.** The active part. Most cells are silicon wafers, about 150 to 210 mm on a side, with a thin antireflection coating on the front.
- **Encapsulant.** A layer of ethylene vinyl acetate (EVA) or a similar polymer that bonds the cells and keeps out moisture.
- **Glass and frame.** Tempered glass on the front for impact resistance, and an aluminium frame for mounting.
- **Backsheet.** A polymer film on the back that insulates the electrical parts.
- **Bypass diodes.** Diodes wired across groups of cells. They let current flow around a shaded or broken group, which prevents a hot spot.
- **Junction box and cables.** The electrical connection to the array.
- **Inverter.** Converts the DC output of the array to AC for the grid or a building. It also tracks the maximum power point, which keeps the array at its best operating voltage.

### Variants

- **Monocrystalline silicon.** One large crystal per cell. It has the highest efficiency in mainstream production. As of 2026, commercial silicon modules are typically about 20 to 23 percent efficient.
- **Multicrystalline (polycrystalline) silicon.** Many grains in each cell. It costs less to make and has slightly lower efficiency than monocrystalline.
- **Thin-film.** Cadmium telluride (CdTe), copper indium gallium selenide (CIGS), or amorphous silicon layers a few micrometres thick on glass or flexible sheets. These modules usually have lower efficiency than crystalline silicon, but they use less material and handle heat well.
- **Bifacial modules.** Cells that collect light on both faces. They gain energy from light reflected off the ground or a light roof.
- **Emerging cells.** Perovskite and tandem designs stack two absorbers, one for high-energy photons and one for low-energy photons. Lab results are higher than silicon, but few products are sold at scale as of 2026.

## Key equations

The current-voltage curve of a cell is the basis for all of its sizing. A cell delivers the most power at the point on that curve where the product of current and voltage is largest.

Power at the maximum power point, in watts:

$$P_{max} = V_{mp} \, I_{mp}$$

where $V_{mp}$ is the voltage at maximum power in volts (V) and $I_{mp}$ is the current at maximum power in amperes (A).

Fill factor, a dimensionless measure of how square the curve is:

$$FF = \frac{P_{max}}{V_{oc} \, I_{sc}}$$

where $V_{oc}$ is the open-circuit voltage in volts (V) and $I_{sc}$ is the short-circuit current in amperes (A). A good module has a fill factor near 0.75 to 0.80 (typical value).

Efficiency, a dimensionless ratio:

$$\eta = \frac{P_{max}}{G \, A}$$

where $G$ is the incident irradiance in watts per square metre (W/m$^2$) and $A$ is the module area in square metres (m$^2$). The standard test condition is $G = 1000\ \text{W/m}^2$ at a cell temperature of 25 °C.

Array peak power, in watts peak (Wp):

$$P_{pk} = N \, A \, G_{STC} \, \eta$$

where $N$ is the number of modules (dimensionless), $A$ is the area of one module in m$^2$, $G_{STC} = 1000\ \text{W/m}^2$, and $\eta$ is the module efficiency.

Daily energy yield, in kilowatt-hours per day:

$$E_{day} = P_{pk} \, H_{psh} \, PR$$

where $P_{pk}$ is the peak power in kilowatts (kW), $H_{psh}$ is the peak sun hours per day in hours (h/day), and $PR$ is the performance ratio, a dimensionless factor for losses in wiring, inverter, dust, and temperature (typical value 0.75 to 0.85).

Temperature correction, in watts:

$$P(T_c) = P_{STC} \left[ 1 + \gamma (T_c - 25) \right]$$

where $P_{STC}$ is the rated power in watts (W), $T_c$ is the cell temperature in degrees Celsius (°C), and $\gamma$ is the power temperature coefficient in per degree Celsius (per °C). For crystalline silicon, $\gamma \approx -0.35\ \%/^\circ\text{C}$ (typical value).

## Worked example

**Given:** An array of $N = 20$ modules. Each module has area $A = 1.7\ \text{m}^2$ and efficiency $\eta = 0.21$. The site receives $H_{psh} = 4.5\ \text{h/day}$ of peak sun on average, and the performance ratio is $PR = 0.80$ (assumed, covering inverter, wiring, and soiling losses).

**Find:** (a) the array peak power and (b) the daily energy yield.

**Assumptions:** The modules sit at the standard irradiance of $1000\ \text{W/m}^2$ for the peak rating. The yield uses the average peak sun hours for the site.

**Solution:**

1. Peak power: $P_{pk} = N A G_{STC} \eta = 20 \times 1.7 \times 1000 \times 0.21 = 7140\ \text{W}$, which is $7.14\ \text{kW}$.
2. Daily energy: $E_{day} = 7.14\ \text{kW} \times 4.5\ \text{h/day} \times 0.80 = 25.7\ \text{kWh/day}$.

**Answer:** (a) $P_{pk} = 7.14\ \text{kW}$. (b) $E_{day} = 25.7\ \text{kWh/day}$.

**Sanity check:** Over a year, $25.7 \times 365 = 9380\ \text{kWh}$. Divided by the $7.14\ \text{kW}$ rating, that gives about $1310\ \text{kWh}$ per kilowatt of peak power per year. Sunny sites often reach that range, so the result is plausible. A site with half the sun hours would produce about half the energy.

## Design trade-offs

- **Efficiency and cost.** A higher efficiency module costs more per watt. A roof with little area favours high efficiency. A large ground-mounted field favours low cost per watt.
- **Tilt and orientation.** A fixed array in the Northern Hemisphere usually faces south. Tilting near the site latitude gives the most energy over a year. A single-axis tracker follows the sun across the day and adds energy, but it adds motors, controls, and wind loads.
- **Temperature.** A module at 65 °C loses about 14 percent of its rated power at a $-0.35\ \%/^\circ\text{C}$ coefficient. Mounting with air gaps behind the panel keeps the cells cooler.
- **Degradation.** Most modules lose about 0.5 percent of output per year (typical value). A warranty usually guarantees about 80 to 90 percent of rated power after 25 years.
- **Area and roof loads.** Modules weigh about 10 to 25 kg each (typical value). The roof structure, snow load, and wind uplift set the mounting design.
- **Storage and inverter sizing.** A system sized for midday peak produces most of its energy at midday. Batteries shift that energy to the evening, at added cost.

## How it fails

- **Shading and hot spots.** A shaded cell in series with lit cells cannot pass the current of the chain. It becomes a load and heats up. Bypass diodes limit the heat by routing current around the shaded group. A hot spot can still char the backsheet or crack the glass if a diode fails.
- **Cracked cells.** Hail, snow loads, or handling damage break cells. Cracks cut current paths and grow over time with thermal cycling.
- **Encapsulant and backsheet aging.** Heat and ultraviolet light yellow the encapsulant and break down polymers. Moisture then reaches the cells and corrodes the metal contacts.
- **Potential-induced degradation (PID).** High voltage between the cells and the grounded frame drives sodium ions through the glass and into the cells. This lowers output. Grounding the array and choosing suitable modules limit PID.
- **Inverter and wiring faults.** A failed inverter stops the array. A loose connector can create an arc. Arc-fault detection and rapid shutdown devices are required on many rooftop systems.

Safety measures that exist because of these failures include bypass diodes, module certification to IEC 61215 (design qualification) and IEC 61730 (safety), overcurrent protection on each string, grounding, and rapid shutdown for firefighters.

## History

In 1839, Alexandre-Edmond Becquerel observed the photovoltaic effect in France. Charles Fritts built a selenium cell in New York in about 1883, with an efficiency near 1 percent. Engineers at Bell Labs, including Daryl Chapin, Calvin Fuller, and Gerald Pearson, built a silicon cell in 1954 with an efficiency of about 6 percent. Space programs adopted silicon cells soon after, and the U.S. Vanguard 1 satellite launched in 1958 carried solar cells. Cost reductions from the 1970s onward made solar power practical on Earth.

## Practice

1. A module with rated power $300\ \text{W}$ has area $1.6\ \text{m}^2$. Find its efficiency at $G = 1000\ \text{W/m}^2$.
2. A $4\ \text{kW}$ array gets $4.5\ \text{h/day}$ of peak sun. Its performance ratio is $0.80$. Find the daily energy in kWh.
3. A $300\ \text{W}$ module has $\gamma = -0.35\ \%/^\circ\text{C}$. Its cells reach $65\ ^\circ\text{C}$. Find its power at that temperature.
4. A module has $I_{sc} = 10\ \text{A}$, $V_{oc} = 38\ \text{V}$, and fill factor $FF = 0.80$. Find $P_{max}$.

<details><summary>Answers</summary>

1. $\eta = 300 / (1.6 \times 1000) = 0.1875$, or 18.75 percent.
2. $E_{day} = 4 \times 4.5 \times 0.80 = 14.4\ \text{kWh/day}$.
3. $P = 300 \times [1 + (-0.0035)(65 - 25)] = 300 \times 0.86 = 258\ \text{W}$.
4. $P_{max} = FF \times V_{oc} \times I_{sc} = 0.80 \times 38 \times 10 = 304\ \text{W}$.

</details>

## Common mistakes

- Confusing power with energy. A $4\ \text{kW}$ array is a power rating. Multiply by hours to get energy in kWh.
- Using the rated power as the average output. The average over a day is a fraction of the peak, set by sun hours, tilt, and losses.
- Ignoring temperature. A hot roof lowers output, and a cold, clear day can raise it above the rating.
- Assuming a shaded panel loses only its shaded share. One shaded cell in a series string can cut the output of the whole string unless bypass diodes are present.
- Treating peak sun hours as clock hours. One peak sun hour is one hour at $1000\ \text{W/m}^2$, not one hour of daylight.

## Go deeper

- [How does solar work](https://www.energy.gov/eere/solar/how-does-solar-work), U.S. Department of Energy: a short, free explanation of how sunlight becomes electricity in a panel.
- Related lessons: [Wind turbines](02-wind-turbines.md), [Hydroelectric power](03-hydroelectric-power.md), [Energy storage](06-energy-storage.md), [The power grid](../electrical/08-the-power-grid.md), [Semiconductors, diodes, and transistors](../electronics/03-semiconductors-diodes-and-transistors.md).
- [Applications reference](../reference.md): the lookup sheet for this topic.
