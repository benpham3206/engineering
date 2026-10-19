# Circuit basics: Ohm's law, KVL, and KCL

**Type:** lesson

Circuit analysis is the bookkeeping that tells you the voltage and current at every part of a
circuit. Almost every electronic device, from a phone charger to a motor controller, is built
from a handful of rules that you can apply with algebra.

**Prerequisites:** [Algebra](../../math/01-algebra.md)
**Time:** 6-10 h

## Core ideas

- **Voltage** ($V$, volts) is the energy per unit charge between two points. It is always measured
  between two points.
- **Current** ($I$, amperes) is the rate of charge flow through a wire, in coulombs per second.
- **Resistance** ($R$, ohms, $\Omega$) is how much a part opposes current. A resistor is the
  simplest part that has resistance.
- **Ideal voltage source**: a part that holds its voltage fixed no matter how much current it has to
  supply. A battery is a good model for this.
- **Node**: a point where two or more wires meet.
- **Loop**: any closed path through the circuit.

### Ohm's law

For a resistor, voltage and current are proportional. This is Ohm's law. Most of the time you
use it in one of three forms.

- Voltage across a resistor is current times resistance.
- Current is voltage divided by resistance.
- Power dissipated as heat is voltage times current.

### Kirchhoff's current law (KCL)

At any node, the total current in equals the total current out. Charge does not pile up at a
node.

### Kirchhoff's voltage law (KVL)

Around any closed loop, the voltage rises add up to the voltage drops. Walking around a loop and
returning to where you started, the net change in potential is zero.

### Series and parallel

- **Series** resistors share the same current. Their resistances add.
- **Parallel** resistors share the same voltage. The reciprocal of the total resistance equals the
  sum of the reciprocals.

Two resistors in parallel: $R_{\mathrm{eq}} = \dfrac{R_1 R_2}{R_1 + R_2}$.

### Voltage divider

Two resistors in series across a source split the voltage in proportion to their resistances.

## Key equations

- Ohm's law: $V = I R$, where $V$ is volts (V), $I$ is amperes (A), and $R$ is ohms ($\Omega$).
- Power: $P = V I = I^2 R = V^2 / R$, where $P$ is watts (W).
- KCL: $\sum I_{\mathrm{in}} = \sum I_{\mathrm{out}}$ at a node.
- KVL: $\sum V_{\mathrm{rises}} = \sum V_{\mathrm{drops}}$ around a loop.
- Series: $R_{\mathrm{eq}} = R_1 + R_2 + \cdots$
- Parallel: $\dfrac{1}{R_{\mathrm{eq}}} = \dfrac{1}{R_1} + \dfrac{1}{R_2} + \cdots$
- Voltage divider: $V_2 = V_s \dfrac{R_2}{R_1 + R_2}$

## Worked example

**Given:** A 9 V battery (ideal) drives a series string of $R_1 = 3.3\ \text{k}\Omega$ and
$R_2 = 6.8\ \text{k}\Omega$. Assume the battery is ideal and the wires have no resistance.

**Find:** The current $I$, the voltage across $R_2$, and the power in $R_2$.

**Solution:**

1. The two resistors are in series, so the total resistance is
   $R_{\mathrm{eq}} = 3300 + 6800 = 10100\ \Omega$.
2. Current from Ohm's law: $I = V_s / R_{\mathrm{eq}} = 9 / 10100 = 8.91 \times 10^{-4}\ \text{A}$,
   which is $0.891\ \text{mA}$.
3. Voltage across $R_2$: $V_2 = I R_2 = 8.91 \times 10^{-4} \times 6800 = 6.06\ \text{V}$.
4. Check with KVL: the drop across $R_1$ is $0.891\ \text{mA} \times 3300\ \Omega = 2.94\ \text{V}$.
   Adding $6.06\ \text{V} + 2.94\ \text{V} = 9.00\ \text{V}$, which matches the source.
5. Power in $R_2$: $P_2 = I^2 R_2 = (8.91\times10^{-4})^2 \times 6800 = 5.40\ \text{mW}$.

**Answer:** $I = 0.891\ \text{mA}$, $V_2 = 6.06\ \text{V}$, $P_2 = 5.40\ \text{mW}$.

**Sanity check:** $R_2$ is about two-thirds of the total resistance, so it should take about two-thirds
of the 9 V. $6.06 / 9 = 0.67$, which fits.

## How it fails

- **Overheated resistors.** A resistor dissipates $P = I^2 R$. If that exceeds its rating, the body darkens, smells, and the value drifts or the part opens. Choose a power rating at least twice the calculated dissipation (derating).
- **Overcurrent in wires and traces.** A short circuit or an overload heats conductors until the insulation melts. The warning sign is a warm cable or a discolored board. Fuses and circuit breakers open the circuit before the wire overheats, so the fuse rating must sit below the current limit of the wire.
- **Shorted and open parts.** A solder bridge, a pinched wire, or a failed component can short a supply. A short draws very high current, so a supply needs current limiting or a fuse. An open joint gives zero current and a floating, unpredictable voltage.
- **Solder joint and connector fatigue.** Vibration and repeated heating and cooling crack solder joints and wear connector contacts. The sign is a circuit that works only when tapped or flexed. Strain relief, locking connectors, and clean crimps reduce it.
- **Contact resistance.** A corroded or loose terminal adds resistance, and $I^2 R$ heating at that spot grows until the connector burns. A discolored terminal is the warning. Torque terminals to specification and inspect them.
- **Voltage divider loading.** A load connected to a divider output lowers the voltage below the unloaded value. The sign is a reading that sags when the load connects. Keep the load resistance much larger than the divider resistors, or buffer the output.
- **Electric shock.** Current through the body can stop the heart at levels far below what trips a fuse, so a fuse protects the wire and not the person. Controls in order of strength are: eliminate the hazard by working on de-energized circuits, substitute low voltage (batteries or a limited supply), add engineering controls such as enclosures, insulation, ground-fault protection, and interlocks, apply administrative controls such as procedures and training, and wear PPE such as insulated gloves and eye protection last. For maintenance, apply lockout/tagout: isolate the supply, lock and tag the disconnect, discharge stored energy, then prove zero energy with a tested meter before touching conductors.

## Practice

1. Find the current through a $220\ \Omega$ resistor across a $5\ \text{V}$ source.
2. Find the equivalent resistance of $100\ \Omega$ in parallel with $220\ \Omega$.
3. Three resistors, $1\ \text{k}\Omega$, $2.2\ \text{k}\Omega$, and $4.7\ \text{k}\Omega$, are in series
   across $12\ \text{V}$. Find the current.
4. A $100\ \Omega$ resistor carries $50\ \text{mA}$. Find the power it dissipates.
5. A voltage divider uses $R_1 = 10\ \text{k}\Omega$ and $R_2 = 10\ \text{k}\Omega$ across $9\ \text{V}$.
   Find $V_2$.

<details><summary>Answers</summary>

1. $22.7\ \text{mA}$
2. $68.75\ \Omega$
3. $1.52\ \text{mA}$
4. $0.25\ \text{W}$
5. $4.5\ \text{V}$

</details>

## Common mistakes

- Mixing up series and parallel. Series resistors share current, and parallel resistors share
  voltage. Check which quantity is shared before you add anything.
- Forgetting that voltage is always measured between two points. Name the two points before
  you write a number.
- Using kilo-ohms with amperes and getting an answer off by a factor of 1000. Convert to ohms and
  amperes first.
- Ignoring power. A resistor that dissipates more than its rating will overheat even when the
  voltage and current look reasonable.
- Assuming a battery is an ideal source. Real batteries have internal resistance, and it matters
  under heavy load.

## Go deeper

- [Circuits and Electronics (6.002), MIT OpenCourseWare](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/)
  by MIT: a full course on circuit analysis with lecture notes and problem sets.
- [University Physics Volume 2, Chapter 10 (DC circuits)](https://openstax.org/books/university-physics-volume-2/pages/10-introduction)
  by OpenStax: resistance, series and parallel rules, and Kirchhoff's rules with worked examples.
- [Engineering LibreTexts](https://eng.libretexts.org/) by LibreTexts: a free library of engineering
  textbooks, including electrical circuits.
- [Electronics, Wikibooks](https://en.wikibooks.org/wiki/Electronics) by Wikibooks contributors:
  a free open text on electronics fundamentals.
- Next step: [Lesson 02, RC circuits and op-amps](02-rc-circuits-and-op-amps.md).
- [Applications reference](../reference.md): the lookup sheet for this topic.
