# Hydroelectric power

**Type:** lesson

**Hydroelectric power** is electricity made by letting falling water drive a turbine and generator. Plants are long-lived civil works, so the site's height and water supply decide how much energy they deliver over decades.

Engineers need to understand it because the output depends on two numbers, the head and the flow, and because the same plant can store energy by pumping water back uphill.

**Prerequisites:** [Hydrostatics and Bernoulli](../../physics/10-hydrostatics-and-bernoulli.md), [Control volumes and pipe flow](../../physics/11-control-volumes-pipe-flow.md), [Fluid systems](../thermal-fluid/02-fluid-systems.md)
**Time:** 6-8 h

## Core ideas

### How it works

Water stored high in a reservoir has potential energy. The water flows downhill through a pipe called a **penstock**, and its pressure and speed drive a turbine. The turbine turns a shaft, and the shaft spins a generator. After the turbine, the water flows out through a **tailrace** back to the river.

The steps run in order:

1. A dam or diversion weir holds back water and creates a height difference, called the **head**.
2. An intake with a screen and a gate lets water into the penstock. The screen keeps out debris.
3. The penstock carries the water down the slope. Pressure at the turbine inlet is roughly $\rho g H$, the weight of the water column per square metre.
4. The turbine runner converts the water's energy into rotation. Guide vanes or nozzles control the flow.
5. The generator makes electricity. A transformer raises the voltage for the grid.
6. The water leaves through a draft tube and returns to the river.

The head sets the pressure and the energy per kilogram of water. The flow sets how much water passes each second. The product of head and flow sets the power.

### Main parts

- **Dam or weir.** Creates the head. Gravity dams resist water by their weight, arch dams transfer the load to the valley walls, and embankment dams rely on their earth mass.
- **Intake and gates.** The intake holds trash racks and a gate that can shut off the water. The gate protects the turbine when the plant is off.
- **Penstock.** A steel or concrete pipe that carries the water to the turbine. Its wall thickness depends on pressure, which rises with head.
- **Turbine runner.** The rotating wheel, with buckets or blades shaped to the water flow.
- **Guide vanes or wicket gates.** Adjustable vanes that control the flow into a reaction turbine.
- **Draft tube.** A flared pipe below the runner. It recovers some of the pressure energy and lets the runner sit above the tailwater.
- **Spillway.** An overflow path that releases water when the reservoir is full or in a flood.
- **Generator and transformer.** The generator makes electricity, and the transformer steps up the voltage for transmission.

### Variants

Turbines fall into two groups. Impulse turbines use a high-speed jet of water. Reaction turbines use the pressure difference across the runner. The U.S. Department of Energy gives these main types:

- **Pelton.** An impulse turbine for very high head and low flow. A jet hits a row of buckets on the wheel.
- **Cross-flow.** An impulse turbine for lower head and larger flow than a Pelton.
- **Francis.** A reaction turbine for a wide range of head. The Department of Energy gives a range of about 130 to 2000 feet of head, which is about 40 to 610 m.
- **Kaplan and propeller.** Reaction turbines for low head and high flow. Kaplan blades can pitch to match the flow, which keeps efficiency high across a range of flows.
- **Kinetic.** A free-flow turbine that uses the speed of a river, with little or no dam.

Plants also differ by how they use water. A run-of-river plant has little storage and produces power as water flows past. A storage plant holds water in a reservoir and releases it on demand. A **pumped-storage plant** moves water between two reservoirs to store energy.

## Key equations

**Hydraulic power**, the power available in the flow, in watts:

$$P_{\mathrm{hyd}} = \rho g Q H$$

where $\rho$ is the water density in kilograms per cubic metre (kg/m$^3$), $g$ is the local gravitational acceleration (9.81 m/s$^2$ at Earth's surface), $Q$ is the volume flow rate in cubic metres per second (m$^3$/s), and $H$ is the net head in metres (m).

Turbine output, in watts:

$$P_{\mathrm{out}} = \eta \rho g Q H$$

where $\eta$ is the turbine-generator efficiency (dimensionless). Large modern plants reach $\eta$ of about 0.85 to 0.95 (typical range).

**Net head**, in metres:

$$H = H_{\mathrm{gross}} - h_{\mathrm{loss}}$$

where $H_{\mathrm{gross}}$ is the height difference between the reservoir surface and the tailwater, and $h_{\mathrm{loss}}$ is the head lost to friction and bends in the penstock.

Energy stored in a volume of water $V$ at head $H$, in joules:

$$E = \rho g V H$$

where $V$ is the volume in cubic metres (m$^3$). Dividing by 3.6 million converts joules to kilowatt-hours.

Ideal jet speed from a Pelton nozzle, in metres per second, before nozzle losses:

$$v_{\mathrm{jet}} = \sqrt{2 g H}$$

Friction and bends in the penstock lower this speed in practice.

## Worked example

**Given:** A plant takes water from a reservoir with a gross head of $H_{\mathrm{gross}} = 100\ \text{m}$. Losses in the penstock total $h_{\mathrm{loss}} = 0\ \text{m}$ for this estimate. The flow is $Q = 10\ \text{m}^3/\text{s}$. The turbine-generator efficiency is $\eta = 0.90$. Water density is $\rho = 1000\ \text{kg}/\text{m}^3$. Gravity is $g = 9.81\ \text{m}/\text{s}^2$ (Earth surface).

**Find:** (a) the electrical output, and (b) the annual energy if the plant runs at a capacity factor of 0.5.

**Assumptions:** The flow is steady. The head loss is zero for this estimate, so the net head equals the gross head. The capacity factor of 0.5 is an assumed value for a plant that runs at about half its full output on average.

**Solution:**

1. Output power: $P_{\mathrm{out}} = \eta \rho g Q H = 0.90 \times 1000 \times 9.81 \times 10 \times 100 = 8.83 \times 10^6\ \text{W}$, which is $8.83\ \text{MW}$.
2. Annual energy: $E = P \times 8760\ \text{h} \times \mathrm{CF} = 8.83\ \text{MW} \times 8760\ \text{h} \times 0.5 = 38\,700\ \text{MWh}$, which is $38.7\ \text{GWh}$.

**Answer:** (a) $P_{\mathrm{out}} = 8.83\ \text{MW}$. (b) $E = 38.7\ \text{GWh}$ per year.

**Sanity check:** The power is less than the hydraulic power, $\rho g Q H = 9.81\ \text{MW}$, because the efficiency is 0.90. Each cubic metre of water per second at $100\ \text{m}$ head gives about $9.8\ \text{MW}$ before losses. The energy per year is plausible for a plant of this size. Doubling the head would double the power, while doubling the flow would also double it, so both numbers matter.

## Design trade-offs

- **Head and flow.** High head favours a small flow and a small turbine, which suits a Pelton. Low head needs a large flow, which suits a Kaplan. Civil works set the head, and the river sets the flow.
- **Civil cost.** Dams, tunnels, and penstocks cost much more than the turbine. A plant's cost depends mostly on its civil structures, and those last for many decades.
- **Storage and firm power.** A reservoir lets the plant run when the grid needs power, instead of when the river flows. A reservoir also limits floods, but it floods land and changes ecosystems.
- **Pumped storage efficiency.** Pumped storage gives back about 70 to 85 percent of the energy it uses for pumping (typical range). The losses come from pumps, motors, and turbines.
- **Environment.** Dams block fish migration. Fish passage, minimum flows, and turbine designs that protect fish reduce this harm, at added cost.
- **Cavitation.** Low pressure at the runner can form vapour bubbles that collapse on the metal and erode it. Designers set the runner height and the operating range to avoid cavitation.

## How it fails

- **Water hammer.** A valve that closes fast stops the flow in the penstock. The kinetic energy of the water becomes a pressure spike. Slow gate and vane closing, surge tanks, and pressure relief valves limit the spike.
- **Penstock rupture.** A pressure spike or a corroded wall can burst the penstock. Inspection, thickness design for pressure, and anchor blocks prevent this.
- **Runaway speed.** If the generator load drops suddenly, the turbine speeds up. The governor closes the gates, and a braking system stops the runner.
- **Cavitation erosion.** Vapour bubbles collapse on the runner surface and pit the metal. Warning signs include noise and loss of efficiency.
- **Dam failure.** A dam can fail from overtopping, foundation erosion, or earthquakes. Spillways, inspection, instrumentation, and emergency action plans reduce the risk.
- **Sediment.** Sediment wears the turbine blades and fills the reservoir. Intake design and sediment flushing reduce wear.

The safety measures that exist because of these failures include spillways sized for the largest expected flood, governors and emergency shutdown systems, surge tanks, and regular dam safety reviews.

## History

Lester Pelton developed the impulse wheel that bears his name in California in the 1870s. James B. Francis designed a reaction turbine at Lowell, Massachusetts, in 1849, and the Francis turbine remains a common design. Viktor Kaplan in Austria developed the adjustable-blade propeller turbine in the 1910s. The Vulcan Street Plant in Appleton, Wisconsin, opened in 1882 and was one of the first hydroelectric plants to supply customers. Pumped-storage plants came later, as electric grids grew and needed storage.

## Practice

Where a problem needs gravitational acceleration, use $g = 9.81\ \text{m}/\text{s}^2$ (Earth surface).

1. A plant has a head of $50\ \text{m}$, a flow of $4\ \text{m}^3/\text{s}$, and efficiency $0.85$. Find the output in megawatts.
2. A plant must deliver $2\ \text{MW}$ at a head of $40\ \text{m}$ with efficiency $0.90$. Find the required flow in cubic metres per second.
3. A reservoir holds $1000\ \text{m}^3$ of water at a head of $300\ \text{m}$. Find the energy stored in kilowatt-hours, and the energy recovered after a round trip with efficiency $0.75$.
4. A small plant has flow $2\ \text{m}^3/\text{s}$, head $25\ \text{m}$, and efficiency $0.88$. Find its output in kilowatts.

<details><summary>Answers</summary>

1. $P = 0.85 \times 1000 \times 9.81 \times 4 \times 50 = 1.67\ \text{MW}$.
2. $Q = \dfrac{2 \times 10^6}{0.90 \times 1000 \times 9.81 \times 40} = 5.66\ \text{m}^3/\text{s}$.
3. Stored: $E = \rho g V H = 1000 \times 9.81 \times 1000 \times 300 = 2.94 \times 10^9\ \text{J}$, which is about $818\ \text{kWh}$. Recovered: $0.75 \times 818 = 613\ \text{kWh}$.
4. $P = 0.88 \times 1000 \times 9.81 \times 2 \times 25 = 432\ \text{kW}$.

</details>

## Common mistakes

- Mixing gross and net head. Friction in the penstock and losses at bends lower the net head, and the output depends on the net value.
- Forgetting the efficiency. Output power is always less than hydraulic power.
- Assuming a constant flow. Rivers rise and fall with rain and snowmelt, so the plant output changes with the season.
- Mixing units for flow. One cubic metre per second equals 1000 litres per second. Check units before multiplying.
- Treating pumped storage as a free source. A round trip returns only part of the energy, about 70 to 85 percent (typical range), because pumping costs energy.

## Go deeper

- [Types of hydropower turbines](https://www.energy.gov/eere/water/types-hydropower-turbines), U.S. Department of Energy: the impulse and reaction turbine types, with their typical head and flow ranges.
- [Types of hydropower plants](https://www.energy.gov/eere/water/types-hydropower-plants), U.S. Department of Energy: run-of-river, storage, and pumped-storage plants, with an explanation of how pumped storage works.
- Related lessons: [Fluid systems](../thermal-fluid/02-fluid-systems.md), [Energy storage](06-energy-storage.md), [Solar photovoltaics](01-solar-photovoltaics.md), [Wind turbines](02-wind-turbines.md), [Generators and alternators](../electrical/04-generators-and-alternators.md), [The power grid](../electrical/08-the-power-grid.md).
- [Applications reference](../reference.md): the lookup sheet for this topic.
