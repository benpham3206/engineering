# Semiconductors: diodes and transistors

**Type:** lesson

A diode passes current in one direction, and a transistor uses a small input to control a large current. These two parts sit inside every power supply, motor drive, and processor, so an engineer who knows how they switch can read a datasheet and design a driver that works.

**Prerequisites:** [Circuit basics](01-circuit-basics.md), [Atomic structure and bonding](../../materials/01-atomic-structure-bonding.md), [Electricity and magnetism](../../physics/06-electricity-and-magnetism.md)
**Time:** 10-14 h

## Core ideas

### How it works

A semiconductor conducts better than an insulator and worse than a metal. Pure silicon has few free charge carriers at room temperature. Adding a small amount of another element, called doping, sets the number of carriers. There are two carrier types. Electrons carry negative charge. Holes are the gaps left by missing electrons, and they behave like mobile positive charges.

- **n-type silicon** is doped with a group V element such as phosphorus. Each dopant atom donates one extra electron. Electrons are the majority carriers.
- **p-type silicon** is doped with a group III element such as boron. Each dopant atom accepts an electron, which creates a hole. Holes are the majority carriers.

In any doped sample, the product of the electron and hole densities stays fixed: $n\,p = n_i^2$. In silicon at 300 K, the intrinsic carrier density $n_i$ is about $1.5 \times 10^{10}\ \text{cm}^{-3}$ (typical value).

When a p-type region meets an n-type region, electrons diffuse into the p side and holes diffuse into the n side. They leave behind fixed, charged dopant ions. Those ions create an electric field that opposes further diffusion. The region with no free carriers is the depletion region. Silicon junctions have a built-in voltage of about 0.6 to 0.7 V (typical value).

A **diode** is one p-n junction with two terminals: the anode (p side) and the cathode (n side).

- Forward bias (anode more positive than cathode) shrinks the depletion region. Current rises exponentially once the voltage passes about 0.6 V in silicon.
- Reverse bias widens the depletion region. Only a tiny leakage current flows, until the reverse voltage reaches the breakdown rating.

A **bipolar junction transistor (BJT)** stacks two junctions. An NPN transistor has a thin p-type base between an n-type emitter and an n-type collector. A small base current controls a large collector current. The collector current is about $\beta$ times the base current. The transistor has three operating regions. In cutoff, the base-emitter junction is off and almost no current flows, so the transistor acts as an open switch. In the active region, the collector current follows the base current, so the transistor acts as an amplifier. In saturation, both junctions are forward biased and the collector-emitter voltage drops to about 0.1 to 0.3 V (typical value), so the transistor acts as a closed switch.

A **MOSFET** (metal-oxide-semiconductor field-effect transistor) has a gate electrode on top of a thin insulating oxide layer. The gate sits above the channel between the source and the drain. When the gate-source voltage passes the threshold voltage $V_{th}$, the channel forms and connects the source to the drain. The gate draws almost no DC current, because the oxide insulates it. The MOSFET is voltage controlled. A BJT is current controlled.

### Main parts

| Part | Role |
|---|---|
| Anode and cathode (diode) | The p side and n side of the junction. Current flows anode to cathode in forward bias. |
| Base, emitter, collector (BJT) | Base carries the small control current. Emitter and collector carry the large current. |
| Gate, source, drain (MOSFET) | Gate sets the channel. Source and drain are the two ends of the channel. |
| Oxide layer (MOSFET) | An insulator, usually silicon dioxide, that isolates the gate from the channel. |
| Silicon die and package | The die holds the doped regions. The package conducts heat away and makes the leads. |

### Variants

- **Rectifier diodes** pass mains-frequency current in power supplies.
- **Schottky diodes** use a metal-semiconductor junction. They drop about 0.2 to 0.4 V (typical value) in forward bias and switch faster than silicon p-n diodes, but leak more in reverse.
- **Zener diodes** are used in reverse breakdown as a voltage reference or clamp.
- **LEDs** are diodes that emit light in forward bias. Their forward drop depends on the color, from about 1.8 V for red to above 3 V for blue (typical values).
- **NPN and PNP BJTs** differ in the polarity of their doped regions. NPN is more common.
- **n-channel and p-channel MOSFETs** differ in the carrier type of the channel. Most power switches are n-channel enhancement-mode MOSFETs.
- **IGBTs** combine a MOSFET-style gate with a BJT-style output. They handle high voltage in motor drives.
- **Wide-bandgap devices** made from silicon carbide or gallium nitride switch faster and tolerate higher temperatures than silicon.

## Key equations

- Thermal voltage: $V_T = \dfrac{kT}{q}$, where $k = 1.380649 \times 10^{-23}\ \text{J/K}$ is the Boltzmann constant, $q = 1.602176634 \times 10^{-19}\ \text{C}$ is the elementary charge, and $T$ is the absolute temperature in kelvin. At 300 K, $V_T \approx 25.9\ \text{mV}$.
- Diode (Shockley) equation: $I_D = I_S \left(e^{V_D / (n V_T)} - 1\right)$, where $I_D$ is the diode current in amperes, $V_D$ is the diode voltage in volts, $I_S$ is the saturation current in amperes (a device constant), and $n$ is the ideality factor (dimensionless, typically 1 to 2).
- Mass action: $n\,p = n_i^2$, where $n$ and $p$ are the electron and hole densities in $\text{cm}^{-3}$, and $n_i$ is the intrinsic density in $\text{cm}^{-3}$.
- BJT current gain: $I_C = \beta I_B$ and $I_E = I_C + I_B$, where $I_C$, $I_B$, and $I_E$ are the collector, base, and emitter currents in amperes, and $\beta$ is the dimensionless current gain.
- MOSFET saturation current: $I_D = \tfrac{1}{2} k_n' \dfrac{W}{L} \left(V_{GS} - V_{th}\right)^2$, where $k_n'$ is the process transconductance parameter in $\text{A/V}^2$, $W/L$ is the width-to-length ratio (dimensionless), $V_{GS}$ is the gate-source voltage in volts, and $V_{th}$ is the threshold voltage in volts.

## Worked example

**Given:** An NPN transistor switches a load. A $12\ \text{V}$ supply feeds a $120\ \Omega$ load connected to the collector. A $5\ \text{V}$ logic signal drives the base through a resistor $R_B$. Assume $V_{BE} = 0.7\ \text{V}$ when on, $V_{CE(sat)} = 0.2\ \text{V}$ (typical value), and a minimum current gain $\beta_{min} = 100$ from the datasheet. The base current is set to $10\ \text{mA}$.

**Find:** (a) the collector current, (b) the base resistor, (c) whether the transistor saturates, and (d) the power dissipated in the transistor.

**Solution:**

1. Collector current when fully on: $I_C = \dfrac{12 - 0.2}{120} = 0.0983\ \text{A} = 98.3\ \text{mA}$.
2. Base resistor: $R_B = \dfrac{5 - 0.7}{0.010} = 430\ \Omega$.
3. Minimum base current for saturation: $I_{B,min} = \dfrac{I_C}{\beta_{min}} = \dfrac{0.0983}{100} = 0.98\ \text{mA}$. The actual base current of $10\ \text{mA}$ is about ten times that value, so the transistor saturates.
4. Power in the transistor: $P = V_{CE} I_C = 0.2 \times 0.0983 = 19.7\ \text{mW}$.
5. Power in the base resistor, for comparison: $P_{R_B} = (4.3)^2 / 430 = 43\ \text{mW}$.

**Answer:** (a) $98.3\ \text{mA}$. (b) $430\ \Omega$. (c) Yes, the transistor saturates, with about ten times the base current needed. (d) $19.7\ \text{mW}$ in the transistor.

**Sanity check:** With $\beta = 100$, the same $10\ \text{mA}$ base current would try to drive $1\ \text{A}$ through the collector. The load limits the collector to $98.3\ \text{mA}$, so the transistor is in saturation and the load sets the current. A small transistor dissipating $20\ \text{mW}$ runs cool. A diode check gives the same kind of result: each $59.5\ \text{mV}$ of forward voltage at 300 K multiplies the diode current by about 10, since $\ln(10) \times V_T = 59.5\ \text{mV}$.

## Design trade-offs

- **Speed against drive power.** A MOSFET needs charge to move its gate capacitance, but it draws no steady current. A BJT needs continuous base current. A BJT in saturation stores charge in the base, so it turns off slower than a MOSFET.
- **Voltage rating against on-resistance.** For a given die size, a MOSFET rated for higher voltage has a larger on-resistance $R_{DS(on)}$. More conduction loss is the price of more voltage margin.
- **Forward drop against leakage.** A Schottky diode loses less power in forward bias than a silicon p-n diode, but it leaks more in reverse and has a lower maximum reverse voltage.
- **Heat against size.** A device must stay below its junction temperature rating. Leakage current in silicon grows quickly with temperature. A roughly doubling every 10 K is a common rule of thumb.
- **Cost against robustness.** Silicon parts are cheap and well understood. Wide-bandgap parts switch faster and run hotter, but they cost more and need careful layout and gate drive.

## How it fails

- **Thermal runaway in a BJT.** The base-emitter voltage falls as the temperature rises, so the current rises and heats the device further. Emitter resistors, heat sinks, and derating limit the risk.
- **Reverse breakdown.** A diode or MOSFET fails when its reverse voltage passes its rating. Clamp diodes, snubbers, and voltage margin protect against voltage spikes.
- **Gate oxide damage.** The gate oxide is thin, so static discharge or an overvoltage on the gate can puncture it. Gate resistors, Zener clamps, and ESD handling protect it.
- **Inductive kickback.** A relay coil or motor winding produces a large voltage spike when current stops. A flyback diode across the coil gives the current a safe path.
- **Overheating in the active region.** A transistor that sits between fully on and fully off carries current at a high collector-emitter voltage, so it dissipates much more power. Weak base drive or slow switching edges cause this.

Warning signs include a warm package at idle, a device that reads as a short or open with a meter, and a circuit whose output does not reach its expected level.

## History

In December 1947, John Bardeen and Walter Brattain at Bell Labs in New Jersey built the first working point-contact transistor. William Shockley developed the theory of the junction transistor in 1948, and the first practical junction transistors followed in the early 1950s. The three shared the 1956 Nobel Prize in Physics. Mohamed Atalla and Dawon Kahng at Bell Labs demonstrated the MOSFET in 1959. The MOSFET became the main transistor for digital logic and power switching.

## Practice

1. Silicon at 300 K has $n_i = 1.5 \times 10^{10}\ \text{cm}^{-3}$. It is doped with $N_D = 10^{15}\ \text{cm}^{-3}$ donors. Find the hole density $p$.
2. The NPN switch in the worked example has $R_L = 60\ \Omega$ instead of $120\ \Omega$. Find the collector current and the minimum base current for saturation at $\beta_{min} = 100$.
3. At 300 K, the forward voltage of a diode rises by $0.1\ \text{V}$. Assume $n = 1$. By what factor does the diode current rise?
4. A MOSFET has $k_n' = 200\ \mu\text{A/V}^2$, $W/L = 10$, $V_{th} = 1.5\ \text{V}$, and $V_{GS} = 3.5\ \text{V}$. It operates in saturation. Find $I_D$.
5. An NPN transistor carries $I_C = 0.5\ \text{A}$ with $V_{CE} = 0.3\ \text{V}$. Find the power it dissipates.

<details><summary>Answers</summary>

1. $p = n_i^2 / N_D = (1.5 \times 10^{10})^2 / 10^{15} = 2.25 \times 10^{5}\ \text{cm}^{-3}$.
2. $I_C = (12 - 0.2)/60 = 0.197\ \text{A}$, or $196.7\ \text{mA}$. The minimum base current is $0.197 / 100 = 1.97\ \text{mA}$. A base current of $10\ \text{mA}$ still saturates the transistor.
3. The factor is $e^{0.1 / V_T} = e^{0.1 / 0.02585} \approx 48$.
4. $I_D = \tfrac{1}{2} (200 \times 10^{-6})(10)(3.5 - 1.5)^2 = 4.0\ \text{mA}$.
5. $P = 0.3 \times 0.5 = 0.15\ \text{W}$.

</details>

## Common mistakes

- Using a 0.7 V forward drop for every diode. Schottky diodes drop about 0.3 V, and LEDs drop 1.8 V or more (typical values).
- Driving a BJT base from a voltage source with no base resistor. The base current is set by the source and the base-emitter voltage, so the current can grow until the transistor overheats.
- Assuming a transistor with $\beta = 100$ will saturate at any base current. Check the saturation condition with the minimum $\beta$ from the datasheet, not the typical value.
- Treating a MOSFET gate as an open circuit at high frequency. Switching the gate needs charge, so a fast switch needs a gate driver that can supply the peak current.
- Forgetting a flyback diode across an inductive load. The load's voltage spike can destroy the switch.

## Go deeper

- [MIT OpenCourseWare 6.012, Microelectronic Devices and Circuits](https://ocw.mit.edu/courses/6-012-microelectronic-devices-and-circuits-fall-2005/): free lectures and notes on junctions, BJTs, and MOSFETs.
- [Semiconductor Devices: Theory and Application (Fiore), LibreTexts](https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_%28Fiore%29): a free textbook covering diodes, BJTs, and FETs.
- [Transistors, HyperPhysics, Georgia State University](https://hyperphysics.gsu.edu/hbase/Electronic/transis.html): a short overview of the junction transistor.
- Related lessons: [RC circuits and op-amps](02-rc-circuits-and-op-amps.md), [Printed circuit boards](04-printed-circuit-boards.md), [Digital logic and computers](07-digital-logic-and-computers.md).
- Previous: [Circuit basics](01-circuit-basics.md).
- [Applications reference](../reference.md): the lookup sheet for this topic.
