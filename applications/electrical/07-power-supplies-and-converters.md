# Power supplies and converters

**Type:** lesson

A power supply turns the electricity from a source into the voltage and current that a device needs. Phone chargers, laptop adapters, and the boards inside appliances all convert power, and most of them do it with switches rather than resistors. Engineers need to know which converter fits a job, because the choice sets the efficiency, the heat, and the size.

**Prerequisites:** [Electricity and magnetism](../../physics/06-electricity-and-magnetism.md), [Circuit basics](../electronics/01-circuit-basics.md), [RC circuits and op-amp basics](../electronics/02-rc-circuits-and-op-amps.md), [Semiconductors](../electronics/03-semiconductors-diodes-and-transistors.md)
**Time:** 8-10 h

## Core ideas

A power supply takes electrical energy in at one voltage and delivers it out at another. The ideal supply loses no energy, so input power equals output power. Real supplies lose some energy as heat. The efficiency $\eta$ is the ratio of output power to input power:

$$\eta = \frac{P_{\mathrm{out}}}{P_{\mathrm{in}}}$$

where $P_{\mathrm{out}}$ and $P_{\mathrm{in}}$ are in watts (W), and $\eta$ is dimensionless.

Converters fall into two groups. Linear regulators drop the extra voltage across a transistor that acts like a variable resistor. Switching converters turn a transistor fully on and fully off many times per second, and store energy in an inductor or capacitor between switching cycles. The switch dissipates little power in either state, so switching converters reach efficiencies of 85 to 95 percent in typical designs.

A rectifier turns alternating current (AC) into direct current (DC). An inverter does the reverse: it turns DC into AC at a chosen frequency.

## How it works

### Linear regulator

A linear regulator holds the output voltage by changing the voltage across a pass transistor. A feedback circuit compares the output with a fixed reference and adjusts the transistor until the two match. The transistor carries the full load current, and the voltage it drops turns into heat.

The power lost in the regulator is:

$$P_{\mathrm{loss}} = (V_{\mathrm{in}} - V_{\mathrm{out}})\, I_{\mathrm{out}}$$

The output is clean and has almost no switching noise. The cost is efficiency. The efficiency is:

$$\eta = \frac{V_{\mathrm{out}}}{V_{\mathrm{in}}}$$

when the quiescent current is small. A 12 V input regulated down to 5 V gives at most 42 percent efficiency, no matter how well the regulator is built.

### Buck converter (step down)

A buck converter lowers the voltage. A switch connects the input to an inductor for a fraction of each cycle, called the duty cycle $D$. When the switch opens, a diode or a second switch keeps the inductor current flowing into the output capacitor. The output voltage is set by the duty cycle:

$$V_{\mathrm{out}} = D\, V_{\mathrm{in}}$$

The inductor smooths the current, so the output carries only a small ripple. A capacitor on the output smooths the voltage further.

### Boost converter (step up)

A boost converter raises the voltage. The inductor charges from the input while the switch is closed. When the switch opens, the inductor pushes its stored energy through a diode into the output capacitor. The output voltage for an ideal converter is:

$$V_{\mathrm{out}} = \frac{V_{\mathrm{in}}}{1 - D}$$

A boost converter cannot give a lower output than its input. It also has no direct path from input to output, so a short on the output can draw a large current unless the design limits it.

### Rectifier

A rectifier uses diodes to pass only one direction of current. A half-wave rectifier passes one half of each AC cycle. A full-wave bridge uses four diodes to pass both halves, so its output has twice the ripple frequency of the input. A filter capacitor across the output holds the voltage between peaks. The average output voltage drops by about 0.7 V per conducting silicon diode in the bridge.

### Inverter

An inverter turns DC into AC. A switching bridge of transistors connects the DC input to a transformer or an output filter in alternating directions. Control circuits change the switching pattern to set the output frequency and voltage. Solar inverters, uninterruptible power supplies, and motor drives use this idea.

## Main parts

- **Pass transistor or switch.** It carries the current in a linear regulator, or it switches between on and off in a switching converter. Its losses set the efficiency.
- **Inductor.** It stores energy in its magnetic field and keeps the current from changing too quickly. A typical buck converter in a laptop uses an inductor of 1 to 10 µH.
- **Output capacitor.** It holds the voltage between switching pulses and sets the ripple.
- **Diode or synchronous switch.** It carries the inductor current during the off part of each cycle. A synchronous converter replaces the diode with a transistor to cut the loss.
- **Feedback and control circuit.** It measures the output, compares it with a reference, and sets the duty cycle or the pass transistor voltage.
- **Transformer.** In an isolated supply, a transformer separates the input from the output and changes the voltage. A flyback converter uses a coupled inductor for this job.

## Variants

- **Linear regulator.** Use it for low-power circuits that need very low noise, such as sensors, audio, and reference voltages. It is cheap and simple, but it wastes power whenever the input is much higher than the output.
- **Buck.** Use it to step down a battery or a bus voltage to a lower rail for a processor or a memory chip. Most point-of-load regulators are buck converters.
- **Boost.** Use it to raise a low battery voltage to a higher level, such as a white LED driver or the boost stage in a hybrid car.
- **Buck-boost.** Use it when the input may be above or below the output, such as a battery that drains from 4.2 V to 3.0 V while the output stays at 3.3 V.
- **Flyback and forward (isolated).** Use them in chargers and adapters where the output must be isolated from the mains for safety.
- **Full-wave bridge rectifier with a capacitor filter.** Use it for the front end of most mains-powered DC supplies.

## Key equations

- Efficiency: $\eta = P_{\mathrm{out}} / P_{\mathrm{in}}$, dimensionless.
- Buck output voltage: $V_{\mathrm{out}} = D\, V_{\mathrm{in}}$, with $D$ dimensionless and between 0 and 1, and $V$ in volts (V).
- Boost output voltage: $V_{\mathrm{out}} = V_{\mathrm{in}} / (1 - D)$, in V.
- Linear regulator loss: $P_{\mathrm{loss}} = (V_{\mathrm{in}} - V_{\mathrm{out}}) I_{\mathrm{out}}$, in W, with $I_{\mathrm{out}}$ in amperes (A).
- Inductor ripple current in a buck converter: $\Delta I_L = \dfrac{(V_{\mathrm{in}} - V_{\mathrm{out}})\, D}{L\, f_{\mathrm{sw}}}$, where $L$ is the inductance in henries (H) and $f_{\mathrm{sw}}$ is the switching frequency in hertz (Hz). The ripple $\Delta I_L$ is in A peak to peak.
- Output ripple of a full-wave bridge with a capacitor filter: $\Delta V \approx \dfrac{I_{\mathrm{load}}}{2 f_{\mathrm{line}} C}$, where $I_{\mathrm{load}}$ is in A, $f_{\mathrm{line}}$ is the mains frequency in Hz, $C$ is the capacitance in farads (F), and $\Delta V$ is in V peak to peak.

## Worked example

**Given:** A 12 V battery bus must supply a 5 V rail at $I_{\mathrm{out}} = 2.0$ A. The rail can use either a linear regulator or a buck converter. The buck converter switches at $f_{\mathrm{sw}} = 200$ kHz with an inductor of $L = 22\ \mu\text{H}$ and an efficiency of $\eta = 0.90$. Assume ideal components except for the stated efficiency.

**Find:** (a) the duty cycle of the buck converter, (b) its input power and power loss, (c) the peak-to-peak inductor ripple current, and (d) the power lost in a linear regulator for the same job, and its efficiency.

**Solution:**

1. Duty cycle: $D = V_{\mathrm{out}} / V_{\mathrm{in}} = 5.0 / 12.0 = 0.417$.
2. Output power: $P_{\mathrm{out}} = V_{\mathrm{out}} I_{\mathrm{out}} = 5.0 \times 2.0 = 10.0\ \text{W}$.
3. Input power: $P_{\mathrm{in}} = P_{\mathrm{out}} / \eta = 10.0 / 0.90 = 11.1\ \text{W}$. The converter loses $11.1 - 10.0 = 1.1\ \text{W}$.
4. Inductor ripple: $\Delta I_L = (12.0 - 5.0)(0.417) / (22\times10^{-6} \times 200\times10^{3}) = 2.92 / 4.4 = 0.66\ \text{A}$ peak to peak.
5. Linear regulator loss: $P_{\mathrm{loss}} = (12.0 - 5.0) \times 2.0 = 14.0\ \text{W}$. Its input power is $10.0 + 14.0 = 24.0\ \text{W}$, so its efficiency is $10.0 / 24.0 = 42\ \%$.

**Answer:** (a) $D = 0.417$. (b) $P_{\mathrm{in}} = 11.1\ \text{W}$, with a loss of $1.1\ \text{W}$. (c) $\Delta I_L = 0.66\ \text{A}$. (d) The linear regulator loses $14.0\ \text{W}$ and runs at about 42 percent efficiency.

**Sanity check:** The buck converter loses about 1 W, and the linear regulator loses 14 W for the same load. The linear regulator must dissipate 14 W from a small package, so it needs a heat sink. The ripple of 0.66 A is about one third of the 2 A load. Designers often accept this level to keep the inductor small, and the output capacitor must absorb the ripple.

## Practice

1. A linear regulator takes 9.0 V in and gives 3.3 V out at 0.50 A. Find the power the regulator dissipates in watts.
2. An ideal buck converter takes 12 V in and gives 3.3 V out. Find the duty cycle $D$.
3. An ideal boost converter takes 3.7 V in and gives 5.0 V out. Find the duty cycle $D$.
4. A buck converter takes 24 V in and gives 12 V out at 3.0 A, with an efficiency of 0.92. Find its input power in watts.
5. A full-wave bridge rectifier runs from a 60 Hz mains supply. The load draws 2.0 A, and the filter capacitor is 10 000 µF. Find the peak-to-peak ripple voltage, using the approximation in the key equations.

<details><summary>Answers</summary>

1. $P_{\mathrm{loss}} = (9.0 - 3.3) \times 0.50 = 2.85\ \text{W}$.
2. $D = 3.3 / 12 = 0.275$.
3. $D = 1 - 3.7 / 5.0 = 0.26$.
4. $P_{\mathrm{in}} = 12 \times 3.0 / 0.92 = 39.1\ \text{W}$.
5. $\Delta V \approx 2.0 / (2 \times 60 \times 0.010) = 1.7\ \text{V}$ peak to peak.

</details>

## Common mistakes

- Using the buck formula for a boost converter, or the reverse. A buck gives $V_{\mathrm{out}} < V_{\mathrm{in}}$, and a boost gives $V_{\mathrm{out}} > V_{\mathrm{in}}$.
- Assuming a linear regulator is efficient because its output is steady. Its efficiency is $V_{\mathrm{out}}/V_{\mathrm{in}}$, which drops when the input is much higher than the output.
- Forgetting that the rectifier output depends on the mains frequency. A 50 Hz supply has a larger ripple than a 60 Hz supply with the same capacitor.
- Sizing the inductor for average current only. The peak current, which is the average plus half the ripple, sets the saturation rating.
- Ignoring light-load efficiency for a battery device, where the converter spends most of its time.

## Design trade-offs

Designers balance efficiency, size, cost, noise, and heat. A linear regulator costs little, has low noise, and needs few parts, but its loss grows with the voltage drop. A buck converter adds an inductor, a switch, and a control chip, which cost more and create switching noise. A higher switching frequency lets the designer use a smaller inductor and capacitor, which shrinks the converter. The cost is more switching loss, which grows in proportion to the switching frequency.

Laptop and phone chargers switch at tens of kilohertz to about 1 MHz. Their small size comes from the high switching frequency and from gallium nitride or silicon carbide switches, which switch fast with low loss. A large data center supply runs at a lower frequency, and its switching loss forms a smaller share of its total loss.

The design also depends on the load. A converter that runs efficiently at full load may lose much of its efficiency at light load, where fixed losses such as the control circuit and gate drive matter more. Battery-powered devices spend most of their time at light load, so the light-load efficiency often matters more than the peak.

## How it fails

- **Overheating.** A linear regulator at a large voltage drop runs hot. A thermal shutdown circuit turns the output off when the chip reaches about 150 degrees Celsius, which protects the chip but interrupts the load.
- **Inductor saturation.** A core that saturates loses its inductance at high current. The current then rises very fast, and the switch can fail. Designers choose an inductor rated above the peak current.
- **Output capacitor failure.** Electrolytic capacitors dry out over time, and their equivalent series resistance rises. The ripple grows, and the output can oscillate. Ceramic capacitors avoid drying but lose capacitance under DC bias.
- **Switch failure from overvoltage.** An inductive spike larger than the switch rating destroys the transistor. Snubbers and careful layout limit the spike.
- **Loss of isolation.** A cracked insulation barrier in an isolated supply lets mains voltage reach the output. Safety standards set minimum creepage distances and test voltages for this reason.
- **Warning signs.** A supply that gets hot at light load, emits a whine at the switching frequency, or resets under load often has a feedback or stability problem.

## History

Early power supplies used vibrating contacts and motor-generator sets, and vacuum tube rectifiers came into radio and television in the 1920s and 1930s. Linear regulators with transistors appeared in the 1950s after the transistor was invented at Bell Labs in 1947. Switching regulators followed in the 1960s and 1970s, as transistors became fast enough to switch at tens of kilohertz. Modern switch-mode supplies in phones and computers use silicon and, more recently, gallium nitride power devices.

## Go deeper

- [OpenStax University Physics Volume 2, Chapter 10](https://openstax.org/books/university-physics-volume-2/pages/10-introduction), free text on electric circuits, resistors, and Kirchhoff's rules.
- [OpenStax University Physics Volume 2, Chapter 14](https://openstax.org/books/university-physics-volume-2/pages/14-introduction), free text on alternating current and RLC circuits.
- Related lessons: [Circuit basics](../electronics/01-circuit-basics.md), [RC circuits and op-amps](../electronics/02-rc-circuits-and-op-amps.md), [Transformers](05-transformers.md), [Batteries](06-batteries.md), and [The power grid](08-the-power-grid.md).
- [Applications reference](../reference.md): the lookup sheet for this topic.
