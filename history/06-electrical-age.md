# The electrical age

**Type:** lesson

**The electrical age** is the period from about 1800 to 1900 when engineers learned to make steady electric current, use it in motors and lamps, and send it along wires. Engineers today should know it because the choice of alternating current for long-distance power still shapes the power grid and the electrical equipment in homes.

**Prerequisites:** [Scientific revolution](04-scientific-revolution.md), [Industrial revolution](05-industrial-revolution.md), [Electricity and magnetism](../physics/06-electricity-and-magnetism.md)
**Time:** 2-3 h

## Core ideas

### A steady current from a battery

Before 1800, electricity came from static charge and from brief sparks. Alessandro Volta, in Italy, built a **voltaic pile** in 1800. The pile stacked discs of zinc and silver or copper with cloth soaked in brine between them. It gave a steady current for the first time, and experimenters could repeat their work with it. Volta announced the pile in a letter to the Royal Society in London that same year.

### Current makes a magnet, and a magnet makes current

In 1820, Hans Christian Ørsted in Copenhagen showed that a current in a wire deflects a compass needle. Within a few years, researchers built electromagnets and simple motors. In 1831, Michael Faraday in London showed that a changing magnetic field induces a voltage in a nearby coil. This is **electromagnetic induction**. Every generator, transformer, and induction motor depends on it.

### Theory and the telegraph

James Clerk Maxwell wrote the field equations of electromagnetism in the 1860s. His theory predicted that electric and magnetic fields travel as waves at the speed of light. Heinrich Hertz produced and detected such waves in Karlsruhe in 1887. Telegraph companies had already used current to send messages over wire. Samuel Morse's system sent its first public long-distance message from Washington to Baltimore in 1844, and cables later crossed the Atlantic. The 1866 cable worked reliably, and that success proved that long lines could carry signals.

### Light and the first power stations

Thomas Edison's team at Menlo Park, New Jersey, made a carbon filament lamp in 1879. A lamp needs a supply, so Edison built a central station. Pearl Street Station in New York began serving customers in 1882. It used **direct current (DC)**, which is hard to change in voltage. Lines of direct current also lose much of their power as heat, so a DC system had to stay close to its customers.

### The contest between direct and alternating current

In the 1880s, companies competed over which system would power cities. Edison's companies promoted direct current, and Westinghouse promoted alternating current. The dispute was partly technical and partly commercial, and it included public arguments about safety. Engineers who compared the two systems focused on distance, cost of copper, and the ability to change voltage. Those points favored AC once transformers and AC motors were available.

### Alternating current wins

**Alternating current (AC)** can change voltage with a **transformer**, which works only with a changing magnetic flux. Transformers let engineers send power at high voltage and use it at low voltage. William Stanley Jr. demonstrated a transformer-based AC lighting system in Great Barrington, Massachusetts, in 1886. Nikola Tesla patented practical polyphase AC motors in 1888, and George Westinghouse's company licensed the system. The Adams Power Plant at Niagara Falls began generating in 1895, and it sent AC power to distant users. The worked example below shows why high voltage reduces line losses.

### Radio

Guglielmo Marconi used the electromagnetic waves that Hertz had detected to send signals across distance without wires. In 1901 he received a transatlantic radio signal at Signal Hill, Newfoundland. Radio became a second communication system that did not need cables.

## Key inventions

| Year | Invention | Who and where | Why it mattered |
|---|---|---|---|
| 1800 | Voltaic pile | Alessandro Volta, Italy | Gave a steady electric current for experiments |
| 1820 | Current deflects a magnet | Hans Christian Ørsted, Copenhagen | Linked electricity and magnetism |
| 1831 | Electromagnetic induction | Michael Faraday, London | Showed that a changing field makes voltage, the basis of generators and transformers |
| 1844 | First public long-distance telegraph message | Samuel Morse, Washington to Baltimore | Started a national message network |
| 1865 | Electromagnetic field theory | James Clerk Maxwell, Britain | Predicted waves that travel at light speed |
| 1866 | Reliable transatlantic telegraph cable | Cyrus Field and partners, Atlantic Ocean | Showed that long submarine lines could carry signals |
| 1879 | Carbon filament lamp | Thomas Edison, Menlo Park, New Jersey | Made an electric light practical |
| 1882 | Pearl Street Station | Thomas Edison, New York | Early central station supplying direct current to nearby customers |
| 1886 | AC transformer lighting system | William Stanley Jr., Great Barrington, Massachusetts | Showed AC distribution with transformers |
| 1887 | Electromagnetic waves detected | Heinrich Hertz, Karlsruhe | Confirmed Maxwell's waves in the laboratory |
| 1888 | Polyphase AC induction motor | Nikola Tesla, patents licensed to Westinghouse | Gave a simple motor that runs on AC |
| 1895 | Adams Power Plant | Westinghouse and Tesla's AC system, Niagara Falls | Large-scale AC generation for distant users |
| 1901 | Transatlantic radio signal | Guglielmo Marconi, Newfoundland | Showed radio could cross an ocean |

## Key equations

Faraday's law of induction gives the voltage around a coil:

$$\mathcal{E} = -N \frac{\Delta \Phi}{\Delta t}$$

Here $\mathcal{E}$ is the induced voltage in volts (V), $N$ is the number of turns, $\Phi$ is the magnetic flux in webers (Wb), and $t$ is time in seconds (s). The minus sign shows that the induced voltage opposes the change.

For an ideal transformer, the voltage ratio follows the turns ratio:

$$\frac{V_s}{V_p} = \frac{N_s}{N_p}$$

Here $V_p$ and $V_s$ are the primary and secondary voltages in volts (V), and $N_p$ and $N_s$ are the turns in each coil.

Power lost in a line as heat:

$$P_{\text{loss}} = I^2 R$$

Here $P_{\text{loss}}$ is the loss in watts (W), $I$ is the current in amperes (A), and $R$ is the line resistance in ohms ($\Omega$).

## Worked example: why high voltage reduces line loss

**Given:** A line delivers $P = 1.0\ \text{MW}$ to a load. The total resistance of the line conductors is $R = 10\ \Omega$. The load is resistive, so the power factor is 1.

**Find:** The line current and the power lost in the line at two transmission voltages: $V = 10\ \text{kV}$ and $V = 100\ \text{kV}$.

**Assumptions:**

1. The load draws power at voltage $V$, so $I = P / V$.
2. The line resistance stays the same at both voltages.
3. The model is single phase, so a three-phase line changes the constants but not the trend.

**Solution:**

1. At $10\ \text{kV}$: $I = 1.0 \times 10^6 / 10\,000 = 100\ \text{A}$. The loss is $I^2 R = 100^2 \times 10 = 100\ \text{kW}$, which is 10 percent of the delivered power.
2. At $100\ \text{kV}$: $I = 1.0 \times 10^6 / 100\,000 = 10\ \text{A}$. The loss is $I^2 R = 10^2 \times 10 = 1.0\ \text{kW}$, which is 0.1 percent of the delivered power.

**Answer:** Ten times the voltage cuts the current by ten times and the line loss by one hundred times.

**Sanity check:** The loss scales with $1/V^2$, so the 10-fold voltage increase gives a 100-fold drop in loss, which matches the numbers. The 10 kV line loses 100 kW of the 1 MW delivered, which is a reasonable scale for a long line at low voltage.

## Lessons for engineers today

- Losses in a conductor scale with the square of the current. Reduce the current for the same power, and the losses fall fast.
- A transformer lets one system raise and lower voltage to match its job. The grid, the wall socket, and the phone charger all depend on this step.
- Faraday's law sits inside every motor, generator, and transformer. Learn it once, and the rest of the electrical design follows.
- Insulation, protection devices, and standards matter as much as the physics. Early systems failed from shock and fire, and codes grew from those failures.

## Practice

1. A 2.0 MW load draws power through a line of 4.0 $\Omega$ at 5 kV and at 50 kV. Find the line loss at each voltage, in kilowatts and as a percent of the delivered power.
2. An ideal transformer steps 11 000 V down to 240 V. Find the turns ratio $N_s / N_p$, and the primary current for a 2.4 kW load.
3. A coil with 200 turns sees its flux change by 0.010 Wb in 0.50 s. Find the average induced voltage.
4. In the 1880s, why was it hard to step direct-current voltage up for long-distance transmission? Answer in two or three sentences.
5. Explain in two or three sentences how Hertz's experiments supported Maxwell's theory, and why that mattered for radio.

<details><summary>Answers</summary>

1. At 5 kV: $I = 2.0 \times 10^6 / 5000 = 400\ \text{A}$, and $I^2 R = 400^2 \times 4 = 640\ \text{kW}$, which is 32 percent. At 50 kV: $I = 40\ \text{A}$, and $I^2 R = 40^2 \times 4 = 6.4\ \text{kW}$, which is 0.32 percent.
2. The turns ratio is $240 / 11\,000 = 0.0218$. The primary current is $P / V_p = 2400 / 11\,000 = 0.218\ \text{A}$, and the secondary current is $2400 / 240 = 10\ \text{A}$.
3. $\mathcal{E} = 200 \times 0.010 / 0.50 = 4.0\ \text{V}$.
4. A transformer works only with a changing flux, so it needs alternating current. A direct current has no changing flux, so the simple transformer does not step it up. Engineers used rotary converters, which were costly and less reliable, or ran separate generators at each voltage.
5. Hertz produced and detected electromagnetic waves in 1887, which confirmed Maxwell's prediction that such waves exist. Radio engineers then used those waves to carry signals through the air without wires.

</details>

## Common mistakes

- Edison invented the electric light alone. Earlier arc lamps existed, and Joseph Swan in England also made carbon filament lamps. Edison's contribution was a practical lamp combined with a supply system.
- Higher voltage on a line means higher current in the line. For a fixed power, higher voltage means lower current, and the lower current cuts the losses.
- Line losses grow linearly with distance and current. The loss grows with the square of the current, so doubling the current quadruples the loss.
- Tesla alone chose AC for the grid. The choice came from many engineers and from business contracts, including the licensing of his patents to Westinghouse.

## Go deeper

- [*Experimental Researches in Electricity, Volume 1*](https://www.gutenberg.org/ebooks/14986), Michael Faraday, free on Project Gutenberg. Faraday's own record of his induction experiments.
- [*The inventions, researches and writings of Nikola Tesla*](https://www.gutenberg.org/ebooks/39272), edited by Thomas Commerford Martin, free on Project Gutenberg. Tesla's papers and patents on AC systems.
- [Physics II: Electricity and Magnetism](https://ocw.mit.edu/courses/8-02-physics-ii-electricity-and-magnetism-spring-2007/), MIT OpenCourseWare, free. A university course that covers induction and the field equations.
- Related lessons: [Electricity and magnetism](../physics/06-electricity-and-magnetism.md), [Transformers](../applications/electrical/05-transformers.md), [The power grid](../applications/electrical/08-the-power-grid.md), and [Radio and antennas](../applications/waves-and-communication/02-radio-and-antennas.md).
- [History of engineering reference](reference.md): the lookup sheet for this topic.
