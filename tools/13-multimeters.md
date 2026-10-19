# Multimeters

**Type:** lesson
**Verify:** strict

A **digital multimeter (DMM)** is a handheld instrument that measures voltage, current, and resistance, and usually continuity, diodes, capacitance, and frequency, and shows the result as a number. It is the first tool an engineer reaches for to ask what a circuit is really doing, and the one that can mislead or hurt you if you use it without knowing how it works.

**Prerequisites:** [Circuit basics](../applications/electronics/01-circuit-basics.md), [Circuit analysis methods](../physics/16-circuit-analysis-methods.md), [AC circuits, phasors, and power](../physics/17-ac-circuits-phasors-and-power.md), [Precision, accuracy, and uncertainty](../measurement/02-precision-accuracy-and-uncertainty.md), [Measurement tools](07-measurement-tools.md)
**Time:** 4-6 h

## Core ideas

### What the meter is

A DMM is a box with a display, a rotary **dial** (selector switch), two or more input **jacks**, and two **test leads**: flexible insulated wires with a probe tip on one end and a plug on the other. The dial chooses what the meter measures. The leads carry the circuit's voltage or current into the jacks.

- The **COM** (common) jack is the return. The black lead almost always lives here.
- The **V** jack, often marked with the ohm and diode symbols as well, takes the red lead for voltage, resistance, continuity, diode test, and usually capacitance and frequency. Its input resistance is high.
- One or two **amps** jacks take the red lead for current. Their input resistance is tiny and sits behind a **fuse**, a thin conductor that melts and opens the path if the current is too high. A small-current jack (milliamps) and a large-current jack (up to about ten amps) are common.

The meter does one thing at a time. The dial and the jack together decide which of two very different circuits the meter connects between your probes: a very high resistance for voltage, or a near-short-circuit for current.

### Reading the display

- A meter's display has a fixed number of **counts**, the number of distinct values it can show from zero to full scale. A "6000-count" meter shows 0 to 5999, so on a range whose top is 6.000 V one count is 0.001 V.
- The **range** is the largest value the meter can show before it must change scale. Resolution is the range divided by the counts, so a lower range gives finer steps.
- An **autoranging** meter picks the range itself. A manual meter makes you pick it. Autoranging is convenient, but it can hunt on a noisy signal, and it hides the range, which you need for the accuracy spec below.
- **OL** (overload) or a lone 1 on the left means the input is above the range or, in resistance mode, that the circuit is open. It is a valid answer, not a fault.
- A reading that never settles is usually real: noise, a slowly charging capacitor, or a meter loading a high-resistance node.

### The one safe first use

Set the dial to DC volts, put the black lead in COM and the red lead in the V jack, and touch the probes to the two ends of a battery, red to the positive end. The display shows the battery voltage. Swap the probes and the sign flips; nothing is damaged. Nothing about this check can harm the meter or you, so it is the habit to build: measure a source whose voltage you already know. Do this before and after every important measurement (see the routine at the end).

### Voltage: in parallel

**Voltage** is a difference between two points, so the meter is connected across the part, in **parallel**, without opening the circuit. The circuit runs as usual and the meter just looks.

- DC volts reads a steady voltage and shows a sign. Reading negative means the red probe is at the lower potential.
- AC volts reads the RMS value of an alternating voltage (see [AC circuits, phasors, and power](../physics/17-ac-circuits-phasors-and-power.md)). Many meters also offer a combined AC plus DC mode, and a millivolt range for small signals.
- A voltmeter has a very large **input impedance**, the resistance the meter presents to the circuit. A typical handheld meter is 10 megaohms on its voltage ranges (typical). The meter draws a tiny current through it, which changes the circuit slightly. This is **loading** and is quantified below.

### Resistance and continuity: power off

A meter measures **resistance** by pushing a small known current through the part and reading the voltage that results. So the circuit must be dead and, ideally, the part isolated.

- Power must be off and any capacitor discharged. A live circuit adds its own voltage to the meter's test, giving a wrong reading and sometimes damaging the meter.
- Other parts in parallel with the part under test lower the reading. Lift one lead of the part, or measure before it is installed.
- **Continuity** is a quick test of whether a low-resistance path exists. The meter beeps below a threshold, typically a few tens of ohms (typical). It finds broken wires, open fuses, and shorts to ground.
- Touching both probes with your fingers adds your body's resistance in parallel, so hold only the insulation for readings of a high-resistance part.

### Current: in series, and why the amps jack is dangerous

**Current** flows through a part, so the meter must be part of the path. Turn the power off. Move the red lead to the amps jack and set the dial to amps before you touch the circuit. Check the jack's continuous and time-limited current ratings before connecting. If the current is unknown, start with the high-current jack and range only when the circuit and meter ratings permit. Open the circuit, connect the meter in **series**, then turn the power on. For current in mains circuits, use a clamp meter rated for the circuit's category and voltage. Do not break a mains circuit to insert a handheld meter.

In amps mode the meter is a very small resistance, a **shunt**, across which it reads the voltage, then reports the current. That tiny resistance is the reason for the hazard. Put the meter on its amps jack across a supply or a battery, which is what happens when you carry the leads from a current measurement and touch them to a voltage source, and you have placed a near-short circuit across it. The current is limited only by the supply and the shunt, and the fuse is the only thing that stops it. If the fuse is the wrong rating, or has been replaced with a wire or a lower-rated part, the leads, the meter, and the supply can overheat or burst.

> [!WARNING]
> Never connect a meter set to amps, or with a lead in an amps jack, across a voltage source. The shunt is nearly a short circuit, and only the fuse limits the current. Replace a blown fuse only with the type and ratings printed on the meter, and return the leads to the V jack as soon as the current measurement is done.

- The shunt also adds a small voltage drop to the circuit, the **burden voltage**. In a low-voltage circuit this can change the very current you are measuring.
- A blown fuse reads as an open circuit. A meter with a blown fuse on a live current path reads exactly zero, which looks the same as a circuit with no current. Check the fuse by measuring a known current, or by testing continuity through the fuse as the manual describes.
- A meter that is too far over its current limit for too long can fail even with a good fuse.

### Diode test, capacitance, and frequency

- **Diode test** applies a small current and shows the forward voltage drop. A silicon diode shows about 0.5 to 0.7 V one way and OL the other (typical). A shorted diode reads near zero both ways, an open diode OL both ways. See [Semiconductors, diodes, and transistors](../applications/electronics/03-semiconductors-diodes-and-transistors.md).
- **Capacitance** mode (if the meter has it) charges the part and measures the response, and needs a discharged capacitor out of the circuit. Results are good to a few percent at best and are slow for large capacitors.
- **Frequency** mode counts cycles per second of an AC signal. It needs a signal large enough to trigger the counter, and it works best on clean waves.

### AC: average-responding versus true RMS

An AC meter reports an **RMS** value, but there are two ways to get it.

- An **average-responding** meter rectifies the signal, averages it, and multiplies by a fixed factor, the **form factor** of a sine wave, $\pi/(2\sqrt{2}) \approx 1.11$. This is correct only for a sine wave.
- A **true RMS** meter computes the square root of the mean of the square, as in the definition. It reads correctly for sine, square, triangle, and the distorted currents drawn by motor drives, power supplies, and dimmers, up to its stated **crest factor** (peak divided by RMS) and frequency limits.

On a non-sine wave an average-responding meter is simply wrong. A symmetric square wave is a clear case, worked in Practice. A true RMS meter also has a bandwidth limit, often a few kilohertz, past which AC readings fall.

### Accuracy specifications

A meter's accuracy is quoted for each function and range as $\pm(p\ \text{percent of reading} + n\ \text{counts})$. The percent part is a gain error that grows with the reading. The count part is an offset and rounding term in units of the smallest step on that range. Both add. This is a worst-case (Type B) limit from the manufacturer, valid under stated conditions such as temperature and the time since calibration, and the meter must be in range (see [Precision, accuracy, and uncertainty](../measurement/02-precision-accuracy-and-uncertainty.md)). If the true value is equally likely anywhere inside the limit, the standard uncertainty is the limit divided by $\sqrt{3}$.

### Meter loading

Your meter is a resistor in parallel with the part. Measuring across a resistor $R_2$ with a meter input resistance $R_m$ replaces $R_2$ with $R_2 \| R_m$. When the circuit's resistance is small next to $R_m$, the effect is negligible. At megaohms it is not.

### Measurement categories (CAT)

A mains wiring system can release enormous energy in a fault. A **measurement category** is a rating, given in roman numerals I to IV, that tells where in a power system a meter is safe to use, and at what maximum voltage. Higher numbers mean closer to the source of supply, where more fault current is available and brief voltage spikes (transients) are larger. A rating always has two parts, the category and a voltage, such as a category and a line-to-ground voltage. The category is set by an international standard for electrical test equipment, and a meter is tested to it for its insulation, spacing inside, and fuse performance.

A meter with no category marking, or one rated for a lower category than the place you use it, may have no protection against the fault spark or transient in a panel. If an arc forms inside the meter, the result can be an arc blast, with hot gas and molten metal flung at the user. A cheap, unrated meter on a mains panel is a hazard no matter how well it reads. The rule is simple. Match the category and voltage to the work, use a meter that carries a mark from a recognized testing laboratory, use fused high-quality leads of the same category, and do not work on mains if you are not trained and authorized.

### Clamp meters

A **clamp meter** measures current without breaking the circuit. Its jaws open and close around one conductor. For AC, the jaws are a transformer core: the conductor is the primary and a coil in the meter is the secondary. A DC-capable clamp uses a Hall-effect sensor, which measures the magnetic field directly. Because the field depends on the net current through the jaws, clamp around one insulated conductor only. Two conductors of a cable carrying equal and opposite current show zero. Use a clamp meter rated for the circuit's measurement category and voltage. A clamp does not make live mains work safe by itself.

A clamp adds no burden voltage and needs no circuit change. It is less accurate than a series measurement at low current, and external magnetic fields and the conductor's position in the jaws change the reading. Many clamp meters also have voltage and resistance modes with leads, and the same rules apply to those.

### A safe checking routine

1. Look first. Check the case, the leads, and the probe tips for cracks or exposed metal. Do not use a damaged meter or lead.
2. Know the circuit. Decide whether it could be live, how much voltage and current to expect, and whether the meter's category and range fit.
3. Set the dial and the jacks to the function you want, before touching the circuit. Start on the highest range if you do not know the size.
4. Test on a known source (a battery, or a supply whose value you know) to prove the meter and leads work.
5. Measure with one hand where you can, keep fingers behind the guards on the probes, and keep the leads away from other conductors.
6. Test on the known source again. A meter that failed halfway through would have told you the circuit was dead when it was not.
7. When done, set the dial to off or to a voltage range and put the leads back in the voltage jacks.

## Key equations

Symbols: $V_t$ = true voltage across the part with no meter attached (V), $V_m$ = voltage the meter reads (V), $V_{pk}$ = peak voltage (V), $R_1$, $R_2$ = resistances of the divider (ohms), $R_m$ = meter input resistance (ohms), $R_p$ = parallel resistance of $R_2$ and $R_m$ (ohms), $V_s$ = source voltage (V), $p$ = percent-of-reading term (percent), $n$ = count term (counts), $\delta$ = value of one count on the range (same unit as the reading), $x$ = reading, $e$ = worst-case error limit (same unit as the reading), $V_{rms}$ = RMS voltage (V), $V_{avg}$ = mean of the absolute value (V), $I$ = current (A), $R_{sh}$ = shunt resistance (ohms).

Resolution of one count, from the top of the range $x_{max}$ and the number of counts $N$:

$$\delta = \frac{x_{max}}{N}$$

Worst-case error limit and standard uncertainty (rectangular distribution), valid in range and under the stated conditions:

$$e = \frac{p}{100}\,x + n\,\delta, \qquad u = \frac{e}{\sqrt{3}}$$

Loaded divider: the meter replaces $R_2$ with $R_p$.

$$R_p = \frac{R_2 R_m}{R_2 + R_m}, \qquad V_m = V_s\,\frac{R_p}{R_1 + R_p}, \qquad V_t = V_s\,\frac{R_2}{R_1 + R_2}$$

Average-responding meter on a symmetric wave, where the scale is set for a sine (factor $\pi/(2\sqrt{2}) \approx 1.11$):

$$V_{read} = \frac{\pi}{2\sqrt{2}}\,V_{avg}$$

For a sine, $V_{avg} = (2/\pi)V_{pk}$, where $V_{pk}$ is the peak voltage, and $V_{read}$ equals $V_{rms}$. For a symmetric square wave, $V_{avg} = V_{rms}$, so the reading is high by the factor $\pi/(2\sqrt{2})$.

Fault current when the amps jack is placed across a source of voltage $V_s$ through the shunt:

$$I = \frac{V_s}{R_{sh}}$$

Ohm's law applies with the source's own internal resistance also in the loop, so this is an upper bound and the real current is lower. The fuse still has to open it.

## Worked example

### Accuracy of a reading, then the error from loading

A 6000-count handheld DMM on its 6.000 V DC range is specified as $\pm(0.5\ \text{percent of reading} + 3\ \text{counts})$. It reads 5.000 V.

**Given:** range top 6.000 V, 6000 counts, reading 5.000 V, $p = 0.5$, $n = 3$.

**Find:** The resolution, the worst-case error limit, the interval that contains the true value, and the standard uncertainty.

**Assumptions:** Conditions are those the spec states, the meter is in range, and the error is equally likely anywhere in the limit.

**Solution:**

1. Resolution: $\delta = 6.000/6000 = 0.001$ V.
2. Percent term: $0.5\ \text{percent} \times 5.000 = 0.025$ V. Count term: $3 \times 0.001 = 0.003$ V.
3. Worst-case limit: $e = 0.028$ V, which is $0.56$ percent of the reading.
4. The true voltage lies between $4.972$ V and $5.028$ V.
5. Standard uncertainty: $u = 0.028/\sqrt{3} = 0.016$ V.

**Answer:** $5.000 \pm 0.028$ V, with a standard uncertainty of about 0.016 V.

**Sanity check:** The count term alone (0.003 V) is only a tenth of the total, so on a mid-scale reading the percent term dominates. On a small reading, such as a tenth of a volt on the same range, the count term (0.003 V) would be 3 percent of the reading, which is why a small reading on a large range is poor.

<details><summary>Verification</summary>

```verify
xmax = q(6.000, "V")
N = q(6000, "1")
x = q(5.000, "V")
p = q(0.5, "1")
n = q(3, "1")
d = xmax / N
expect(d, "0.001 V")
e1 = p / 100 * x
expect(e1, "0.025 V")
e2 = n * d
expect(e2, "0.003 V")
e = e1 + e2
expect(e, "0.028 V")
expect(e / x * 100, "0.56 1")
expect(x - e, "4.972 V")
expect(x + e, "5.028 V")
unc = e / sqrt(3)
expect(unc, "0.016 V")
check(e2 < e1, "the percent term dominates mid scale")
```

</details>

### Loading a high-resistance divider

A 10 V source feeds a divider of two equal resistors, 1 megaohm each. A meter with an input resistance of 10 megaohms measures across the lower resistor.

**Given:** $V_s = 10$ V, $R_1 = R_2 = 1\ \text{M}\Omega$, $R_m = 10\ \text{M}\Omega$.

**Find:** The true voltage, the meter's reading, and the error.

**Assumptions:** An ideal source and a perfectly accurate meter whose only effect is its input resistance.

**Solution:**

1. True voltage with no meter: $V_t = 10 \times 1/(1+1) = 5.000$ V.
2. The meter in parallel with $R_2$ gives $R_p = (1 \times 10)/(1 + 10) = 0.9091\ \text{M}\Omega$.
3. The meter reads $V_m = 10 \times 0.9091/(1 + 0.9091) = 4.762$ V.
4. The error is $0.238$ V, or $4.76$ percent of the true value.

**Answer:** The meter reads 4.762 V instead of 5.000 V, low by almost 5 percent, even though the meter is perfect.

**Sanity check:** The reading must be below the true value, because adding a parallel path lowers the resistance of the lower leg. The error is large because the meter's resistance is only ten times the circuit's. Its accuracy spec (about 0.5 percent) is far smaller than this error, which shows that the spec says nothing about loading.

<details><summary>Verification</summary>

```verify
Vs = q(10, "V")
R1 = q(1, "Mohm")
R2 = q(1, "Mohm")
Rm = q(10, "Mohm")
Vt = Vs * R2 / (R1 + R2)
expect(Vt, "5.000 V")
Rp = R2 * Rm / (R2 + Rm)
expect(Rp, "0.9091 Mohm")
Vm = Vs * Rp / (R1 + Rp)
expect(Vm, "4.762 V")
expect(Vt - Vm, "0.238 V")
expect((Vt - Vm) / Vt * 100, "4.76 1")
check(Vm < Vt, "loading lowers the reading")
```

</details>

## Practice

1. A 6000-count meter on its 60.00 V range is specified as $\pm(1.0\ \text{percent of reading} + 5\ \text{counts})$. One count on this range is 0.01 V. It reads 12.00 V. Find the worst-case error limit in V and the interval for the true voltage.
2. A 12 V source feeds a divider of two 470 kilohm resistors. A meter with 10 megohms input resistance measures across the lower resistor. Find the meter's reading in V and the loading error as a percent of the true voltage.
3. An average-responding meter, scaled for sine waves with a factor of $\pi/(2\sqrt{2})$, measures a symmetric square wave of amplitude 10 V. Find the reading in V and the error as a percent of the true RMS value.
4. A meter's amps jack has a shunt of 0.05 ohm. A technician with the leads still in the amps jack touches the probes across a 12 V supply. Find the largest current the shunt could carry, ignoring the supply's own resistance and the fuse, in A.
5. A technician measures an apparently dead motor circuit and the meter reads 0.000 V. Give three different reasons the reading could be zero while the circuit is live, and say what to do before trusting it.

<details><summary>Answers</summary>

1. The limit is 0.17 V (0.12 V from the percent term plus 0.05 V from the counts). The true voltage lies between 11.83 V and 12.17 V.
2. The meter reads 5.862 V instead of 6.000 V. The error is about 2.3 percent low.
3. The reading is 11.1 V against a true 10 V, so the error is about 11 percent high. A true RMS meter reads 10 V.
4. The shunt could pass up to 240 A. This is an upper bound. The fuse must open far below it, and a wrong fuse or a missing one turns the meter into a hazard.
5. The red lead may be in the wrong jack for the dial setting; the dial may be on a current range with a blown fuse, so the meter is open and shows zero; the meter's battery may be dead, or the probe tips may not touch bare metal. The probes may also be across two points at the same potential, such as two points on one side of an open switch. Before trusting a zero, test the meter and leads on a known live source, then check the connection, and treat the circuit as live until proved otherwise by an independent step such as lockout and tagout.

```verify
res = q(0.01, "V")
x = q(12.00, "V")
e = q(1.0, "1") / 100 * x + q(5, "1") * res
expect(q(1.0, "1") / 100 * x, "0.12 V", ans=1)
expect(q(5, "1") * res, "0.05 V", ans=1)
expect(e, "0.17 V", ans=1)
expect(x - e, "11.83 V", ans=1)
expect(x + e, "12.17 V", ans=1)
Vs = q(12, "V")
R = q(470, "kohm")
Rm = q(10000, "kohm")
Rp = R * Rm / (R + Rm)
Vm = Vs * Rp / (R + Rp)
Vt = Vs * R / (R + R)
expect(Vm, "5.862 V", ans=2)
expect(Vt, "6.000 V", ans=2)
expect((Vt - Vm) / Vt * 100, "2.3 1", ans=2)
Vamp = q(10, "V")
factor = pi / (2 * sqrt(2))
reading = factor * Vamp
expect(reading, "11.1 V", ans=3)
expect((reading - Vamp) / Vamp * 100, "11 1", ans=3)
expect(Vamp, "10 V", ans=3)
Rsh = q(0.05, "ohm")
expect(q(12, "V") / Rsh, "240 A", ans=4)
skip(ans=5, why="judgment answer, no calculation")
```

</details>

## Common mistakes

- Leaving a lead in the amps jack and then measuring voltage, which shorts the source through the shunt. Return the red lead to the V jack after every current measurement.
- Measuring resistance in a powered circuit, or with other parts in parallel, and trusting the number.
- Trusting the accuracy spec as the whole error. It does not include loading, which can be much larger on megaohm circuits.
- Using an average-responding meter on a non-sine wave, such as the output of a variable-speed drive, and believing the reading.
- Using a meter with no category rating, or a lower one than the location needs, on a mains panel.
- Reading zero as proof that a circuit is dead without testing the meter on a known source first.
- Clamping around both conductors of a cable and reading about zero.

## Go deeper

- [University Physics Volume 2, section 10.4 (Electrical measuring instruments)](https://openstax.org/books/university-physics-volume-2/pages/10-4-electrical-measuring-instruments) by OpenStax: how voltmeters and ammeters are built, and why a voltmeter needs a high resistance and an ammeter a low one.
- Previous: [Measurement tools](07-measurement-tools.md) for calipers, gauges, and resolution.
- Related: [Precision, accuracy, and uncertainty](../measurement/02-precision-accuracy-and-uncertainty.md), [AC circuits, phasors, and power](../physics/17-ac-circuits-phasors-and-power.md), [Circuit analysis methods](../physics/16-circuit-analysis-methods.md).
