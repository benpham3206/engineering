# AC circuits, phasors, and power

**Type:** lesson
**Verify:** strict

Alternating-current (AC) circuit analysis is the method for finding voltages, currents, and power when the sources are sinusoids, using complex numbers called phasors to turn the calculus of capacitors and inductors into algebra. Motors, pumps, compressors, and shop wiring all run on AC, and a mechanical engineer who reads a motor nameplate, sizes a feeder, or asks why an industrial plant is billed for reactive power is using exactly these ideas.

**Prerequisites:** [Circuit analysis methods](16-circuit-analysis-methods.md), [Electricity and magnetism](06-electricity-and-magnetism.md), [Trigonometry](../math/02-trigonometry.md), [Differential equations](../math/06-differential-equations.md)
**Time:** 10-14 h

## Core ideas

### Sinusoids and complex numbers

- A **sinusoid** is a signal of the form $v(t) = V_m \cos(\omega t + \phi)$. Here $V_m$ is the **amplitude** (V), $\omega$ the **angular frequency** (rad/s), $f = \omega/2\pi$ the **frequency** (Hz), $T = 1/f$ the **period** (s), and $\phi$ the **phase** (rad or degrees). A positive $\phi$ makes the wave **lead** (peak earlier).
- A **complex number** is $z = a + jb$, where $j$ satisfies $j^2 = -1$ (electrical engineering uses $j$ because $i$ means current). It has a **magnitude** $|z| = \sqrt{a^2+b^2}$ and an **angle** $\theta = \operatorname{atan2}(b,a)$, and can be written $z = |z|e^{j\theta}$. Euler's formula $e^{j\theta} = \cos\theta + j\sin\theta$ links the two forms. Multiplying complex numbers multiplies magnitudes and adds angles; dividing divides magnitudes and subtracts angles.
- The **root-mean-square (RMS)** value of a periodic signal is $\sqrt{\text{mean of } v^2}$. It is the constant voltage that would heat a resistor at the same average rate. For a sinusoid, $V_{rms} = V_m/\sqrt{2}$. Meters, nameplates, and wall outlets quote RMS values.

### Phasors

A **phasor** is the complex number $\mathbf{V} = V_m e^{j\phi}$ that records the amplitude and phase of a sinusoid at a known, fixed frequency. The time signal is recovered as $v(t) = \operatorname{Re}\{\mathbf{V}e^{j\omega t}\}$. Because every signal in a linear circuit driven at one frequency has that same frequency, the phasor carries all the information, and derivatives become multiplication by $j\omega$. A phasor is a snapshot of rotating arrows, so adding sinusoids of one frequency is adding arrows.

### Impedance and admittance

- **Impedance** ($Z$) is the ratio of voltage phasor to current phasor, in ohms. It is the AC generalisation of resistance: $\mathbf{V} = Z\mathbf{I}$. A resistor has $Z_R = R$, an inductor $Z_L = j\omega L$, and a capacitor $Z_C = 1/(j\omega C) = -j/(\omega C)$.
- The imaginary part of impedance is the **reactance** ($X$), and the real part is the resistance. Inductive reactance is positive and rises with frequency; capacitive reactance is negative and falls with frequency.
- **Admittance** ($Y = 1/Z$) is the reciprocal, in siemens (S). Its real part is **conductance** and its imaginary part is **susceptance**. Parallel parts add admittances; series parts add impedances.
- The current in an inductor lags its voltage by 90 degrees, and the current in a capacitor leads its voltage by 90 degrees. A mnemonic: the inductor resists change in current, so the current arrives late.

Once every part is replaced by its impedance, every DC method of [Circuit analysis methods](16-circuit-analysis-methods.md) carries over unchanged, now with complex arithmetic: Kirchhoff's laws, node-voltage and mesh-current analysis, superposition (applied one frequency at a time), source transformation, and the Thevenin and Norton equivalents.

### AC Thevenin and Norton equivalents

Any linear network at one frequency looks, from two terminals, like a source $\mathbf{V}_{th}$ in series with an impedance $Z_{th}$, or a current $\mathbf{I}_N = \mathbf{V}_{th}/Z_{th}$ in parallel with the same $Z_{th}$. The maximum average power goes to a load $Z_L = Z_{th}^*$, the **complex conjugate** (same resistance, opposite-sign reactance), so the reactances cancel and the circuit is resonant.

### Average, reactive, and complex power

With $v(t) = V_m\cos(\omega t + \phi_v)$ and $i(t) = I_m\cos(\omega t + \phi_i)$, the instantaneous power $p = vi$ has a constant part and a part that oscillates at twice the line frequency. Let $\theta = \phi_v - \phi_i$ be the **power angle**, the angle of the load impedance.

- **Average (real) power** ($P$) is the constant part, in watts: the rate at which energy is converted to heat or work.
- **Reactive power** ($Q$) is the amplitude of the energy that swings in and out of the inductors and capacitors each cycle, with no net conversion. Its unit is the volt-ampere reactive (var). It is positive for an inductive load.
- **Apparent power** ($S$) is $V_{rms}I_{rms}$, in volt-amperes (VA). It sizes the wiring and transformers, which carry the full current whether or not it does useful work.
- **Complex power** is $\mathbf{S} = P + jQ = \mathbf{V}_{rms}\mathbf{I}_{rms}^*$, where the star is the complex conjugate. The three powers form a right triangle: $S^2 = P^2 + Q^2$.
- The **power factor (pf)** is $P/S = \cos\theta$. It is **lagging** for an inductive load (current behind voltage) and **leading** for a capacitive load. Induction motors are inductive, so plants have lagging power factor.

### Power factor correction

A supply delivers $I = P/(V\,\text{pf})$ for a real load $P$. A low power factor raises current, so it raises wire loss and the size of the wiring and transformers, and utilities often bill for it. **Power factor correction** adds a capacitor in parallel with the load to supply the reactive power locally. The capacitor removes reactive power $Q_c = Q_1 - Q_2$ and leaves $P$ unchanged, since a capacitor stores energy and dissipates none.

### Balanced three-phase systems

A **three-phase** source has three sinusoidal voltages of equal amplitude, 120 degrees apart, carried on three line conductors (plus a neutral in some systems). It is **balanced** when the three loads are identical.

- A **wye (Y)** connection joins one end of each phase at a common neutral point. The **line voltage** ($V_L$, between two lines) is $\sqrt{3}$ times the **phase voltage** ($V_p$, across one phase), and the line current equals the phase current.
- A **delta ($\Delta$)** connection joins the phases in a triangle. The line voltage equals the phase voltage, and the line current is $\sqrt{3}$ times the phase current.
- The total real power is $P = 3V_p I_p\cos\theta = \sqrt{3}\,V_L I_L \cos\theta$ in either connection, where $\theta$ is the angle of one phase's impedance. The total apparent power is $\sqrt{3}\,V_L I_L$. Always quote line values for $V_L$ and $I_L$ in the same formula, since nameplates give them.
- A balanced load can be analysed on one phase, then multiplied by three.

Why machines run on three-phase power: the instantaneous power of one phase pulses at twice the line frequency, which in a single-phase motor shows up as a pulsating torque. For three equal phases 120 degrees apart, the three pulsating terms cancel, so the total instantaneous power is constant and equal to $3V_{rms}I_{rms}\cos\theta$. Three-phase currents in three coils spaced 120 degrees around a stator also make a smoothly rotating magnetic field, so an induction motor starts and runs with no starting winding or capacitor, a steady torque, and no moving contacts. For the same power, three-phase also needs less conductor material than single-phase. The motor then converts electrical to shaft power, so a nameplate quotes shaft output and the electrical input is higher by the inverse of efficiency (see [Electricity and magnetism](06-electricity-and-magnetism.md) for the motor principle).

## Key equations

Symbols: $\omega$ = angular frequency (rad/s), $f$ = frequency (Hz), $\mathbf{V}$, $\mathbf{I}$ = voltage and current phasors (V, A), $Z$ = impedance ($\Omega$), $R$ = resistance ($\Omega$), $X$ = reactance ($\Omega$), $L$ = inductance (H), $C$ = capacitance (F), $P$ = real power (W), $Q$ = reactive power (var), $S$ = apparent power (VA), $\theta$ = power angle (rad or degrees). Dimensionally, $\text{F} = \text{s}/\Omega$ and $\text{H} = \Omega\,\text{s}$.

Frequency, RMS value of a sinusoid, and impedances, holding for linear parts in sinusoidal steady state:

$$
\omega = 2\pi f, \qquad V_{rms} = \frac{V_m}{\sqrt{2}}, \qquad Z_R = R, \quad Z_L = j\omega L, \quad Z_C = \frac{1}{j\omega C}
$$

Series RL impedance, magnitude and angle:

$$
Z = R + jX, \qquad |Z| = \sqrt{R^2 + X^2}, \qquad \theta = \operatorname{atan2}(X, R)
$$

Single-phase power from RMS values, where $\theta$ is positive for a lagging load:

$$
P = V_{rms}I_{rms}\cos\theta, \qquad Q = V_{rms}I_{rms}\sin\theta, \qquad S = V_{rms}I_{rms}, \qquad S^2 = P^2 + Q^2
$$

Power factor correction from $\text{pf}_1$ to $\text{pf}_2$ for a real load $P$, and the parallel capacitor that does it at RMS voltage $V$ and frequency $\omega$:

$$
Q_c = P\left(\tan\theta_1 - \tan\theta_2\right), \qquad C = \frac{Q_c}{\omega V^2}
$$

Maximum average power to a load $Z_L = Z_{th}^*$ from a source of RMS Thevenin voltage $V_{th}$ and $R_{th} = \operatorname{Re}(Z_{th})$. This holds only for a load whose reactance can be chosen freely:

$$
P_{max} = \frac{V_{th}^2}{4R_{th}}
$$

Balanced three-phase, in either connection (the rest is for wye, and delta with the roles of current and voltage swapped):

$$
P = \sqrt{3}\,V_L I_L\cos\theta, \quad S = \sqrt{3}\,V_L I_L, \quad V_L = \sqrt{3}\,V_p \ (\text{wye}), \quad I_L = \sqrt{3}\,I_p \ (\text{delta})
$$

> [!WARNING]
> Mains and three-phase supplies are lethal. A capacitor bank used for power factor correction can stay charged after the supply is removed, and a motor's neutral or ground can be live. Treat a circuit as live until measured, and follow lockout and tagout before any work.

## Worked example

### Power factor correction of a single-phase motor

A single-phase induction motor load draws 2000 W at a lagging power factor of 0.80 from a 230 V RMS, 50 Hz supply. A parallel capacitor will correct the power factor to 0.95.

**Given:** $P = 2000$ W, $\text{pf}_1 = 0.80$ lagging, $\text{pf}_2 = 0.95$ lagging, $V = 230$ V RMS, $f = 50$ Hz.

**Find:** The apparent and reactive power and line current before correction, the capacitor needed, and the line current after.

**Assumptions:** Sinusoidal steady state, constant load, an ideal capacitor that dissipates no power, the supply voltage unchanged by the added capacitor.

**Solution:**

1. Apparent power: $S_1 = P/\text{pf}_1 = 2500$ VA. Reactive power: $Q_1 = \sqrt{S_1^2 - P^2} = 1500$ var.
2. Line current before correction: $I_1 = S_1/V = 10.87$ A.
3. After correction the reactive power must be $Q_2 = P\tan(\arccos 0.95) = 657.4$ var, so the capacitor supplies $Q_c = Q_1 - Q_2 = 842.6$ var.
4. $\omega = 2\pi f = 314.2$ rad/s, so $C = Q_c/(\omega V^2) = 50.7\ \mu\text{F}$.
5. Line current after correction: $I_2 = P/(V\,\text{pf}_2) = 9.153$ A.

**Answer:** Before: 2500 VA, 1500 var, 10.87 A. A capacitor of about 50.7 $\mu\text{F}$ supplies 842.6 var, and the line current falls to 9.15 A, a drop of about 16 percent.

**Sanity check:** The real power stays 2000 W, and 9.153 A is less than 10.87 A as it must be when the power factor rises. The current ratio $I_2/I_1 = \text{pf}_1/\text{pf}_2 = 0.842$, so the drop is 16 percent.

<details><summary>Verification</summary>

```verify
P = q(2000, "W")
V = q(230, "V")
f = q(50, "Hz")
pf1 = q(0.80, "1")
pf2 = q(0.95, "1")
S1 = P / pf1
expect(S1, "2500 V A")
Q1 = sqrt(S1**2 - P**2)
expect(Q1, "1500 V A")
I1 = S1 / V
expect(I1, "10.87 A")
Q2 = P * tan(acos(pf2))
expect(Q2, "657.4 V A")
Qc = Q1 - Q2
expect(Qc, "842.6 V A")
w = 2 * pi * f
expect(w, "314.2 1/s")
C = Qc / (w * V**2)
expect(C, "50.7 us/ohm")
I2 = P / (V * pf2)
expect(I2, "9.153 A")
expect(I2, "9.15 A")
expect(I2 / I1, "0.842")
expect((1 - I2 / I1) * 100, "16 1")
check(I2 < I1, "current falls when the power factor rises")
```

</details>

### Three-phase motor feeder

A three-phase induction motor delivers 15 kW of shaft power at an efficiency of 0.90 and a lagging power factor of 0.85, on a 400 V line-to-line, balanced supply.

**Given:** $P_{shaft} = 15$ kW, efficiency $\eta = 0.90$, $\text{pf} = 0.85$, $V_L = 400$ V.

**Find:** The electrical input power, the apparent power, the line current, the phase voltage, and the phase current if the stator is wound in delta.

**Assumptions:** Balanced supply and load, sinusoidal steady state, rated operating point.

**Solution:**

1. Input real power: $P = P_{shaft}/\eta = 16.67$ kW.
2. Apparent power: $S = P/\text{pf} = 19.61$ kVA.
3. Line current: $I_L = S/(\sqrt{3}V_L) = 28.30$ A.
4. For a wye connection the phase voltage is $V_L/\sqrt{3} = 230.9$ V.
5. For a delta winding the phase voltage is 400 V and the phase current is $I_L/\sqrt{3} = 16.34$ A.

**Answer:** The motor draws 16.67 kW, 19.61 kVA, and 28.30 A from each line. A delta winding carries 16.34 A per phase.

**Sanity check:** Powers recompute as $\sqrt{3} \times 400 \times 28.30 \times 0.85 = 16.67$ kW. A single-phase supply at 230 V carrying the same real power at the same power factor would need $P/(230 \times 0.85) = 85.3$ A in one conductor, which is why the three-phase feeder is smaller.

<details><summary>Verification</summary>

```verify
Pshaft = q(15, "kW")
eta = q(0.90, "1")
pf = q(0.85, "1")
VL = q(400, "V")
P = Pshaft / eta
expect(P, "16.67 kW")
S = P / pf
expect(S, "19.61 kV A")
IL = S / (sqrt(3) * VL)
expect(IL, "28.30 A")
expect(VL / sqrt(3), "230.9 V")
expect(IL / sqrt(3), "16.34 A")
expect(sqrt(3) * VL * IL * pf, "16.67 kW")
Vphase = q(230, "V")
expect(P / (Vphase * pf), "85.3 A")
check(IL / sqrt(3) < IL, "delta phase current is below line current")
```

</details>

## Practice

1. A sinusoid has an amplitude of 170 V. Find its RMS value in V.
2. A coil of 0.10 H in series with 30 $\Omega$ is driven at 60 Hz. Find the magnitude of its impedance in $\Omega$.
3. A 5 kW load at a lagging power factor of 0.70 is corrected to 0.95 with a parallel capacitor. Find the reactive power the capacitor must supply, in kvar.
4. A source has a Thevenin voltage of 19.2 V RMS and a Thevenin impedance of $1.92 - j1.44\ \Omega$. Find the maximum average power it can deliver to any load, in W.
5. A balanced three-phase resistive load of 12 $\Omega$ per phase is on a 400 V line-to-line supply. Find the total power if the load is wye connected, then if it is delta connected, in kW.

<details><summary>Answers</summary>

1. 120.2 V
2. 48.2 $\Omega$ (reactance 37.70 $\Omega$)
3. 3.46 kvar
4. 48.0 W
5. 13.3 kW wye, 40.0 kW delta (delta draws 3 times as much)

```verify
expect(q(170, "V") / sqrt(2), "120.2 V", ans=1)
X = 2 * pi * q(60, "Hz") * q(0.10, "ohm s")
expect(X, "37.70 ohm", ans=2)
expect(sqrt(q(30, "ohm")**2 + X**2), "48.2 ohm", ans=2)
P = q(5, "kW")
Qc = P * (tan(acos(q(0.70, "1"))) - tan(acos(q(0.95, "1"))))
expect(Qc, "3.46 kV A", ans=3)
Rth = q(1.92, "ohm")
Vth = q(19.2, "V")
expect(Vth**2 / (4 * Rth), "48.0 W", ans=4)
R = q(12, "ohm")
VL = q(400, "V")
Pwye = 3 * (VL / sqrt(3))**2 / R
Pdelta = 3 * VL**2 / R
expect(Pwye, "13.3 kW", ans=5)
expect(Pdelta, "40.0 kW", ans=5)
expect(Pdelta / Pwye, "3 1", ans=5)
```

</details>

## Common mistakes

- Adding AC magnitudes instead of phasors. A resistor and an inductor in series have $|Z| = \sqrt{R^2+X^2}$, not $R + X$.
- Mixing amplitude and RMS values. Powers use RMS, and a 170 V amplitude is only about 120 V RMS.
- Reading the wrong sign for reactive power: an inductive load has positive $Q$ and a lagging power factor, and a capacitor supplies reactive power to cancel it. A capacitor sized for the wrong frequency does not correct the factor.
- Using $\sqrt{3}\,V_L I_L$ with a phase voltage or phase current, or forgetting that the power-factor angle is the angle of one phase's impedance, not the angle between two line voltages.
- Applying maximum power transfer to a load that cannot match both resistance and reactance, or treating the conjugate match as a way to raise efficiency.
- Applying phasors to a circuit driven at more than one frequency without solving each frequency separately and adding the time-domain results.

## Go deeper

- [Circuits and Electronics (6.002)](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/) by MIT OpenCourseWare: a free course covering sinusoidal steady state, impedance, and power.
- [University Physics Volume 2, chapter 15 (Alternating-current circuits)](https://openstax.org/books/university-physics-volume-2/pages/15-introduction) by OpenStax: free chapters on phasors, reactance, resonance, and power in AC circuits.
- Previous: [Circuit analysis methods](16-circuit-analysis-methods.md) sets up the node, mesh, Thevenin, and transient tools used here.
- Related: [Electricity and magnetism](06-electricity-and-magnetism.md), [Vibrations](13-vibrations.md).
- [Fields, waves, and space reference](reference-fields-waves-space.md): the lookup sheet that includes circuit laws and electromagnetism.
