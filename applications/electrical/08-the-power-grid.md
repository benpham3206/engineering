# The power grid

**Type:** lesson

The power grid carries electricity from power plants to homes, factories, and offices across distances of hundreds of kilometres. It runs as one machine that must match supply and demand every second. An engineer who understands the grid can size a transmission line, read a frequency number, and see why a fault in one substation can trip breakers far away.

**Prerequisites:** [Electricity and magnetism](../../physics/06-electricity-and-magnetism.md), [Circuit basics](../electronics/01-circuit-basics.md), [Thermodynamics: entropy, the second law, and cycles](../../physics/09-thermo-second-law-cycles.md), [Trigonometry](../../math/02-trigonometry.md)
**Time:** 8-10 h

## Core ideas

The grid moves energy in alternating current (AC). Power plants generate it, step-up transformers raise its voltage for long-distance transmission, and step-down transformers lower it for distribution to customers. Three facts shape the design.

First, power is the product of voltage, current, and power factor. For a given power, a higher voltage means a lower current. Lower current means less heat loss in the wires, so the grid uses high voltage for long lines.

Second, the frequency is the same everywhere on a synchronous grid. Generators spin in step with each other, and the frequency tells every machine on the grid whether supply matches demand. If demand rises above supply, the generators slow down and the frequency drops.

Third, the grid uses three-phase AC. Three sinusoidal voltages, each offset by 120 degrees, deliver power more smoothly than one phase and let motors start without a separate circuit.

The frequency and the household voltage differ by region. Most of the Americas and parts of Asia use 60 Hz. Most of Europe, Africa, Australia, and much of Asia use 50 Hz. Household voltages range from about 100 V to about 240 V. Engineers must check the local standard before they design any equipment that connects to the grid.

## How it works

### Generation

A power plant turns some form of energy into mechanical rotation, and a synchronous generator turns that rotation into electricity. Steam turbines in coal, gas, nuclear, and some geothermal plants drive generators. Hydropower turbines drive them from falling water. Wind turbines drive them through a gearbox or a direct-drive ring. Solar panels produce DC, so an inverter converts their output to AC before it reaches the grid.

In 2025, U.S. utility-scale generation was about 41 percent natural gas, 18 percent nuclear, 17 percent coal, and 24 percent renewables, according to the U.S. Energy Information Administration. The mix varies by country and by season, so the numbers here describe one grid only.

A generator must spin at a speed that matches the grid frequency. The synchronous speed in revolutions per minute is:

$$n = \frac{120\, f}{p}$$

where $f$ is the frequency in hertz (Hz), $p$ is the number of poles, and $n$ is in rpm. A two-pole steam turbine at 60 Hz spins at 3600 rpm, and at 50 Hz it spins at 3000 rpm.

### Transmission

A step-up transformer raises the generator voltage to a transmission level, often 110 kV to 765 kV in North America and 220 kV to 1000 kV in parts of Asia and Europe. The high voltage keeps the current low. Lines run on towers or underground cables. Long lines also carry reactive power, which must be balanced to keep the voltage steady along the line.

Transmission lines form a meshed network, so power can reach a load through more than one path. If one line trips, the others carry its flow.

### Distribution

A step-down substation lowers the voltage to a medium level, typically 4 kV to 35 kV. Feeders carry the power through neighbourhoods. A distribution transformer on a pole or a pad lowers it again to the customer voltage. A single-phase household supply in North America is $120/240$ V split phase, and most homes in Europe and Australia receive a 230 V single-phase supply.

### Three-phase power

A three-phase generator produces three voltages, each 120 degrees apart. The total power delivered to a balanced load is constant at every instant, while a single-phase supply delivers power that pulses twice per cycle. Industrial motors and large loads use three-phase power because the motor torque stays smooth and the motor starts without help. Line-to-line voltage $V_{\mathrm{LL}}$ and line-to-neutral voltage $V_{\mathrm{LN}}$ differ by $\sqrt{3}$.

### Protection

Protection equipment isolates a fault before it damages equipment or hurts people. Circuit breakers open the circuit when current exceeds a set level. Relays sense the current, voltage, or phase angle and send the trip signal. Surge arresters clamp lightning spikes to the ground. A residual-current device, often called a GFCI or RCD, trips when current leaves a circuit through an unintended path, such as a person.

Under-frequency relays shed load when the frequency falls, so the generators can recover before the grid collapses. A cascading outage starts when one protective device trips and shifts its load onto other lines, which then trip in turn.

## Main parts

- **Generator.** A synchronous machine that makes three-phase AC at the grid frequency. Its rotor speed is fixed by the frequency and the pole count.
- **Step-up transformer.** It raises the voltage at the power plant, which lowers the current in the transmission lines.
- **Transmission line and tower.** It carries high-voltage power over long distances. Conductor size, spacing, and height set the resistance, the inductance, and the capacitance per kilometre.
- **Substation.** It holds the transformers, switchgear, breakers, and protection that switch and step down the voltage.
- **Distribution transformer.** It steps the voltage down to the level used by a building or a block of houses.
- **Protection relays and breakers.** They detect faults and open the circuit within a few cycles, which is about 0.1 seconds at 60 Hz.
- **Control centre.** Operators balance generation against demand in real time and watch the frequency and voltage on each line.

## Variants

- **AC transmission.** The usual choice for a meshed grid. It works with transformers, so it can change voltage easily.
- **HVDC.** High-voltage direct current suits very long lines, undersea cables, and links between two grids that run at different frequencies. A converter station at each end changes AC to DC and back.
- **Radial distribution.** A single feeder serves a set of customers and has one path back to the substation. It is cheap, but a fault cuts off every customer on that feeder.
- **Networked distribution.** Several feeders connect to the same loads, so a fault on one feeder leaves the load supplied from another. Dense city centres often use this design.
- **Microgrid.** A small grid with its own generation, often solar and batteries, that can run separately from the main grid during an outage.

## Key equations

- Three-phase real power: $P = \sqrt{3}\, V_{\mathrm{LL}}\, I_L \cos\phi$, where $P$ is in watts (W), $V_{\mathrm{LL}}$ is the line-to-line voltage in volts (V), $I_L$ is the line current in amperes (A), and $\cos\phi$ is the power factor (dimensionless).
- Line-to-neutral voltage in a balanced system: $V_{\mathrm{LN}} = V_{\mathrm{LL}} / \sqrt{3}$. A 400 V line-to-line supply gives about 231 V line to neutral.
- Resistive loss in a three-phase line: $P_{\mathrm{loss}} = 3 I_L^2 R$, where $R$ is the resistance of one conductor in ohms ($\Omega$).
- Percentage loss: $\%\text{ loss} = 100\, P_{\mathrm{loss}} / P$.
- Synchronous speed: $n = 120 f / p$, where $n$ is in rpm, $f$ is in Hz, and $p$ is the number of poles.
- Transformer voltage ratio: $V_s / V_p = N_s / N_p$, where $V$ is in V and $N$ is the number of turns, which is dimensionless.

## Worked example

**Given:** A plant delivers $P = 500$ MW to a load at a power factor of $\cos\phi = 0.95$ (lagging). The line has a resistance of $R = 2.0\ \Omega$ per conductor. The line-to-line voltage is either $500$ kV or $138$ kV. Assume the same conductor and length in both cases, and assume the resistance is the same for both voltages.

**Find:** (a) the line current at each voltage, and (b) the resistive power loss and its percentage of the delivered power at each voltage.

**Solution:**

1. Line current at 500 kV: $I_L = P / (\sqrt{3}\, V_{\mathrm{LL}} \cos\phi) = 500\times10^6 / (1.732 \times 500\times10^3 \times 0.95) = 608\ \text{A}$.
2. Resistive loss at 500 kV: $P_{\mathrm{loss}} = 3 I_L^2 R = 3 \times 608^2 \times 2.0 = 2.2\times10^6\ \text{W}$, which is 2.2 MW, or $0.44\ \%$ of 500 MW.
3. Line current at 138 kV: $I_L = 500\times10^6 / (1.732 \times 138\times10^3 \times 0.95) = 2202\ \text{A}$.
4. Resistive loss at 138 kV: $P_{\mathrm{loss}} = 3 \times 2202^2 \times 2.0 = 2.9\times10^7\ \text{W}$, which is 29 MW, or $5.8\ \%$ of 500 MW.

**Answer:** (a) $608\ \text{A}$ at 500 kV and $2202\ \text{A}$ at 138 kV. (b) At 500 kV the loss is about 2.2 MW, or 0.44 percent. At 138 kV the loss is about 29 MW, or 5.8 percent.

**Sanity check:** The voltage ratio is $500 / 138 = 3.6$, and the current ratio is $2202 / 608 = 3.6$. The loss ratio is $3.6^2 = 13$, which matches $29 / 2.2 = 13$. Raising the voltage cuts the current by the same factor, and the loss falls with the square of the current. The 138 kV line would need conductors with about 13 times the area to match the loss of the 500 kV line, because resistance falls with area.

## Design trade-offs

Designers balance cost, losses, reliability, land use, and safety. A higher transmission voltage cuts loss but needs taller towers, wider right-of-way, and more expensive insulators and transformers. Underground cable costs several times as much as an overhead line of the same rating, and it is harder to repair, so most transmission is overhead. Undersea links use HVDC because AC cable has large charging current over long distances.

Frequency is a fixed choice for each grid. A 50 Hz grid needs motors and transformers with about 20 percent more core area than a 60 Hz design for the same voltage, because the peak flux in the core scales with the voltage divided by the frequency. Changing a grid's frequency is expensive, so a country keeps its choice for a century.

Reliability costs money. Redundant lines, spare transformers, and extra generation capacity reduce outages but add capital cost. Utilities trade these costs against the cost of lost load, which can be measured in dollars per kilowatt-hour for industrial customers.

## How it fails

- **Cascading outage.** One overloaded line trips, its power moves to the lines next to it, and they overload and trip in turn. The 2003 blackout in northeastern North America spread this way across several states and Canada.
- **Frequency collapse.** If generation falls below demand, the frequency drops. Under-frequency relays shed load to recover, but a fast fall can trip generators, which lowers generation further.
- **Voltage collapse.** A heavily loaded line draws more reactive power, and the voltage sags. Reactive power sources such as capacitor banks, static compensators, and generator excitation hold the voltage up.
- **Lightning and faults.** Lightning strikes a line and sends a surge through it. Surge arresters and insulators limit the damage, and protection relays clear the fault in a few cycles.
- **Equipment ageing.** Transformer oil degrades, insulation cracks, and breakers wear out. Utilities test transformers for dissolved gases to find faults before they fail.
- **Warning signs.** Warm transformers, frequent breaker trips, flickering lights during peak demand, and frequency that drifts from its set value all point to a system near its limits.

## History

Thomas Edison's Pearl Street Station in New York began supplying direct current to customers in September 1882. Direct current could not be transformed, so the station needed a generator close to each load. George Westinghouse and Nikola Tesla championed alternating current, which can be transformed. The first large AC hydro plant at Niagara Falls began generating in 1895, and it sent power to Buffalo in 1896. Around the turn of the twentieth century, North American systems settled on 60 Hz, and many European systems chose 50 Hz. Those choices remain in use. Interconnected grids grew through the twentieth century, and HVDC links were built from the 1950s onward.

## Practice

1. A three-phase supply has a line-to-line voltage of 400 V. Find the line-to-neutral voltage in volts.
2. A four-pole generator runs at 50 Hz. Find its speed in rpm.
3. A three-phase motor draws 15 kW from a 400 V line at a power factor of 0.85. Find the line current in amperes.
4. A 100 MW load at 230 kV and a power factor of 0.98 draws power through a line with 1.0 $\Omega$ per conductor. Find the line current and the resistive loss in kilowatts.
5. A distribution transformer has 1000 turns on its primary and 40 turns on its secondary. The primary sees 11 kV. Find the secondary voltage in volts, and say whether the transformer steps up or down.

<details><summary>Answers</summary>

1. $V_{\mathrm{LN}} = 400 / \sqrt{3} = 231\ \text{V}$.
2. $n = 120 \times 50 / 4 = 1500\ \text{rpm}$.
3. $I_L = 15\,000 / (\sqrt{3} \times 400 \times 0.85) = 25.5\ \text{A}$.
4. $I_L = 100\times10^6 / (\sqrt{3} \times 230\times10^3 \times 0.98) = 256\ \text{A}$. The loss is $3 \times 256^2 \times 1.0 = 197\ \text{kW}$, which is about 0.2 percent of the load.
5. $V_s = 11\,000 \times 40 / 1000 = 440\ \text{V}$. The transformer steps down, because the secondary has fewer turns.

</details>

## Common mistakes

- Using the phase voltage in the three-phase power formula. The formula $\sqrt{3}\, V_{\mathrm{LL}} I_L \cos\phi$ needs the line-to-line voltage.
- Assuming the grid frequency is the same in every country. Europe uses 50 Hz, and North America uses 60 Hz. A motor rated for one frequency runs at the wrong speed on the other.
- Thinking that the household voltage is the same everywhere. Households in North America get 120 V single phase, and most of Europe gets 230 V.
- Comparing loss at two voltages without holding the conductor fixed. The loss falls with the square of the current, so a small change in voltage gives a large change in loss.
- Believing the grid stores energy. Generation must match demand at every moment, and storage is used only to smooth short gaps.

## Go deeper

- [U.S. Energy Information Administration, Electricity explained: delivering electricity to consumers](https://www.eia.gov/energyexplained/electricity/delivery-to-consumers.php), a free, plain account of the path from plant to customer.
- [U.S. Energy Information Administration, Electricity in the U.S.](https://www.eia.gov/energyexplained/electricity/electricity-in-the-us.php), a free summary of how the U.S. generates electricity.
- [OpenStax University Physics Volume 2, Chapter 14](https://openstax.org/books/university-physics-volume-2/pages/14-introduction), free text on alternating current, RLC circuits, and power in AC circuits.
- Related lessons: [Transformers](05-transformers.md), [Generators and alternators](04-generators-and-alternators.md), [Induction motors](03-induction-motors.md), [Batteries](06-batteries.md), and [Power supplies and converters](07-power-supplies-and-converters.md).
- [Applications reference](../reference.md): the lookup sheet for this topic.
