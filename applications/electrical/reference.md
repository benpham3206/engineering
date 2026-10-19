# Electrical power reference

**Type:** reference
**Verify:** strict

Lookup sheet for alternating-current power: phasors, complex power, balanced three-phase systems, per-unit quantities, transformers, rotating machines, transmission lines, voltage drop, symmetrical components, and fault current, for an engineer sizing, checking, or troubleshooting a power circuit.

## Principles

- Power is conserved. Real power into a network equals real power out plus losses, and reactive power balances separately at each bus. A power-flow answer that does not close is wrong.
- Reactive power does no net work but carries current. Current heats conductors and sizes equipment whether or not it does useful work, so apparent power sets the rating.
- State every sinusoidal quantity as root mean square (RMS) or peak. The two differ by $\sqrt{2}$, and every power formula in this sheet uses RMS.
- State every three-phase quantity as line or phase. A line-to-line voltage and a phase voltage differ by $\sqrt{3}$ in a wye connection and are equal in a delta connection.
- A balanced three-phase system reduces to one phase. An unbalanced system does not; split it into symmetrical components first.
- For a fixed delivered power, current falls as voltage rises, and conductor loss falls with the square of the current. This is why power moves at high voltage.
- Per-unit values remove the voltage level and the transformer ratios from a network, so one calculation covers every voltage level.
- A fault current is limited only by the impedance between the source and the fault. The protective device must interrupt more than the largest current that can reach it.
- Grid frequency and nominal voltage are regional conventions, not physics. Every example here uses 50 Hz or 400 V as an example input, and a design must use the local values.
- A rating, a conductor size, or a protection setting is a decision under a jurisdiction's code. This sheet gives the physics and leaves the code tables to the code.

## AC and phasor conventions

### RMS value and the phasor

A sinusoid is described by an RMS magnitude, a phase, and an angular frequency. The phasor $\underline{V}$ carries the first two, using the $e^{j\omega t}$ convention of [notation](../../data/notation.md).

$$V_{\text{rms}} = \frac{V_{\text{pk}}}{\sqrt{2}} \qquad v(t) = \mathrm{Re}\left\{\sqrt{2}\,\underline{V}\,e^{j\omega t}\right\} \qquad \omega = 2\pi f$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $V_{\text{rms}}$ | RMS value of the sinusoid | V |
| $V_{\text{pk}}$ | peak value of the sinusoid | V |
| $\underline{V}$ | phasor; its magnitude is the RMS value | V |
| $v(t)$ | instantaneous voltage | V |
| $\omega$ | angular frequency | rad/s |
| $f$ | frequency | Hz |
| $t$ | time | s |

Holds when: the waveform is a single-frequency sinusoid in steady state.
Breaks when: the waveform is distorted. The RMS value of a non-sinusoidal wave is the square root of the mean of its square, and it is not the peak divided by $\sqrt{2}$.
Source and basis: derived from the definition of RMS value; taught in [AC circuits, phasors, and power](../../physics/17-ac-circuits-phasors-and-power.md). Complex-number arithmetic is in [Foundations reference](../../math/reference-foundations.md).

- Example: a sinusoid of 325 V peak has an RMS value of 229.8 V.

<details><summary>Verification</summary>

```verify
Vpk = q(325, "V")
expect(Vpk / sqrt(2), "229.8 V")
```

</details>

### Impedance of R, L, and C

Impedance $\underline{Z}$ is the phasor ratio of voltage to current. Each ideal element has a fixed impedance at a given frequency. Direct-current laws and Thevenin and Norton equivalents are in [Circuit analysis methods](../../physics/16-circuit-analysis-methods.md) and [Circuit relations](../../physics/reference-fields-waves-space.md#circuit-relations).

$$\underline{Z}_R = R \qquad \underline{Z}_L = j\omega L \qquad \underline{Z}_C = \frac{1}{j\omega C} = -\frac{j}{\omega C}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\underline{Z}_R$ | impedance of a resistor | ohm |
| $\underline{Z}_L$ | impedance of an inductor | ohm |
| $\underline{Z}_C$ | impedance of a capacitor | ohm |
| $R$ | resistance | ohm |
| $L$ | inductance | H |
| $C$ | capacitance | F |
| $\omega$ | angular frequency | rad/s |

Holds when: the element is linear and ideal, and the circuit is in sinusoidal steady state at one frequency. Current is positive into the terminal at the higher voltage (passive sign convention).
Breaks when: the element has parasitics (winding capacitance, lead inductance), the core saturates, or several frequencies are present. Analyze each frequency separately and add the time responses.
Source and basis: derived from $v = L\,di/dt$ and $i = C\,dv/dt$ with $d/dt \to j\omega$; taught in [AC circuits, phasors, and power](../../physics/17-ac-circuits-phasors-and-power.md).

- Example: at 50 Hz (an example input), a 50 mH inductor has a reactance of 15.71 ohm. A $100\ \mu\text{F}$ capacitor has a reactance of magnitude 31.83 ohm. In series the net reactance is -16.12 ohm, which is capacitive.

<details><summary>Verification</summary>

```verify
f = q(50, "Hz")
L = q(50, "mH")
C = q(100, "uF")
w = 2 * pi * f
expect(w * L, "15.71 ohm")
expect(1 / (w * C), "31.83 ohm")
expect(w * L - 1 / (w * C), "-16.12 ohm")
```

</details>

## Single-phase complex power

### Real, reactive, and apparent power

Complex power $\underline{S}$ combines real power $P$ (the rate energy is converted) and reactive power $Q$ (the rate energy is exchanged with fields). With the passive sign convention and the $e^{j\omega t}$ convention, $Q$ is positive for an inductive load, whose current lags its voltage.

$$\underline{S} = \underline{V}\,\underline{I}^{*} = P + jQ \qquad P = V I \cos\theta \qquad Q = V I \sin\theta \qquad S = V I \qquad \mathrm{pf} = \cos\theta$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\underline{S}$ | complex power | VA |
| $S$ | apparent power, $\lvert\underline{S}\rvert$ | VA |
| $P$ | real power | W |
| $Q$ | reactive power, positive for an inductive load | var |
| $V$ | RMS voltage across the load (single-phase) | V |
| $I$ | RMS current into the load (single-phase) | A |
| $\underline{I}^{*}$ | complex conjugate of the current phasor | A |
| $\theta$ | power angle, voltage phase minus current phase | rad |
| $\mathrm{pf}$ | power factor, lagging for $\theta > 0$ | dimensionless |

Holds when: voltage and current are single-frequency sinusoids in steady state and the load is linear. The power factor alone does not say lagging or leading; state which.
Breaks when: the current is distorted (rectifiers, drives). Then $P/S$ includes harmonic content and is not $\cos\theta$ of the fundamental.
Source and basis: derived from the time average of $v(t)\,i(t)$; taught in [AC circuits, phasors, and power](../../physics/17-ac-circuits-phasors-and-power.md).

- Example: a load draws 8 A at 230 V with a lagging power factor of 0.8. Then $S = 1840$ VA, $P = 1472$ W, and $Q = 1104$ var.

<details><summary>Verification</summary>

```verify
V = q(230, "V")
I = q(8, "A")
pf = q(0.8, "1")
S = V * I
expect(S, "1840 VA")
expect(S * pf, "1472 W")
expect(S * sqrt(1 - pf**2), "1104 var")
```

</details>

### Power-factor correction capacitor

A capacitor in parallel with a lagging load supplies reactive power locally and leaves $P$ unchanged. The capacitor must supply the difference between the load's reactive power now and the target.

$$Q_c = P\left(\tan\theta_1 - \tan\theta_2\right) \qquad C_{1\phi} = \frac{Q_c}{\omega V^2} \qquad C_{Y} = \frac{Q_c}{\omega V_{\text{LL}}^2} \qquad C_{\Delta} = \frac{Q_c}{3\,\omega V_{\text{LL}}^2}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $Q_c$ | reactive power supplied by the capacitor (total, all phases) | var |
| $P$ | real power of the load (total) | W |
| $\theta_1$ | power angle before correction | rad |
| $\theta_2$ | power angle after correction | rad |
| $C_{1\phi}$ | capacitance of the single-phase capacitor | F |
| $C_{Y}$ | capacitance of each of three wye-connected capacitors, balanced | F |
| $C_{\Delta}$ | capacitance of each of three delta-connected capacitors, balanced | F |
| $V$ | RMS single-phase voltage across the capacitor | V |
| $V_{\text{LL}}$ | RMS line-to-line voltage | V |
| $\omega$ | angular frequency | rad/s |

Holds when: the load is lagging and steady, the capacitor is ideal, the supply voltage does not change when it is added, and the three-phase case is balanced.
Breaks when: the load is non-linear (a capacitor can resonate with the supply inductance at a harmonic), the load varies widely (fixed correction overcorrects at light load and causes a leading power factor), or the voltage drifts (capacitor reactive power scales with $V^2$).
Source and basis: derived from $Q = \omega C V^2$ across a capacitor and the power triangle; taught in [AC circuits, phasors, and power](../../physics/17-ac-circuits-phasors-and-power.md).

- Example: a 2000 W load at power factor 0.8 lagging on 230 V and 50 Hz (example inputs) corrected to 0.95 needs $Q_c = 842.6$ var, or $C = 50.70\ \mu\text{F}$. The same $Q_c$ on a 400 V line-to-line three-phase supply needs $C_Y = 16.76\ \mu\text{F}$ per phase in wye or $C_\Delta = 5.588\ \mu\text{F}$ per phase in delta.

<details><summary>Verification</summary>

```verify
P = q(2000, "W")
V = q(230, "V")
f = q(50, "Hz")
w = 2 * pi * f
th1 = acos(q(0.8, "1"))
th2 = acos(q(0.95, "1"))
Qc = P * (tan(th1) - tan(th2))
expect(Qc, "842.6 var")
expect(Qc / (w * V**2), "50.70 uF")
VLL = q(400, "V")
expect(Qc / (w * VLL**2), "16.76 uF")
expect(Qc / (3 * w * VLL**2), "5.588 uF")
```

</details>

## Balanced three-phase systems

A three-phase source has three voltages of equal RMS value, 120 degrees apart in phase, in the sequence a, b, c (positive sequence). The system is balanced when the loads are also equal. Unbalanced cases are in [Symmetrical components](#symmetrical-components).

### Wye and delta relations

In a wye connection the three phases join at a neutral point. In a delta connection they form a closed triangle. The relations below are for a balanced load and positive sequence.

$$\text{wye: } V_{\text{LL}} = \sqrt{3}\,V_{\text{ph}},\ I_{\text{L}} = I_{\text{ph}} \qquad \text{delta: } V_{\text{LL}} = V_{\text{ph}},\ I_{\text{L}} = \sqrt{3}\,I_{\text{ph}}$$

$$\underline{V}_{ab} = \sqrt{3}\,\underline{V}_{an}\,e^{j\pi/6} \quad (\text{wye}) \qquad \underline{I}_{a} = \sqrt{3}\,\underline{I}_{ab}\,e^{-j\pi/6} \quad (\text{delta})$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $V_{\text{LL}}$ | RMS line-to-line voltage, between two line conductors | V |
| $V_{\text{ph}}$ | RMS phase voltage, across one source winding or load branch (line-to-neutral in a wye) | V |
| $I_{\text{L}}$ | RMS line current, in one line conductor | A |
| $I_{\text{ph}}$ | RMS phase current, in one winding or load branch | A |
| $\underline{V}_{ab}$ | line-to-line voltage phasor, RMS | V |
| $\underline{V}_{an}$ | phase voltage phasor, line a to neutral, RMS | V |
| $\underline{I}_{a}$ | line current phasor in line a, RMS | A |
| $\underline{I}_{ab}$ | phase current phasor in the branch between lines a and b, RMS | A |

Holds when: the source and load are balanced, the sequence is positive (a, b, c), and the circuit is in sinusoidal steady state.
Breaks when: the load is unbalanced (the neutral then carries current and the ratios differ), the sequence is negative (the phase shifts change sign), or the voltages are distorted.
Source and basis: derived from phasor subtraction of two phase voltages 120 degrees apart; taught in [AC circuits, phasors, and power](../../physics/17-ac-circuits-phasors-and-power.md).

- Example: a 400 V line-to-line supply (an example input) gives a wye phase voltage of 230.9 V. A delta load of 30 ohm per phase on the same supply carries a phase current of 13.33 A and a line current of 23.09 A.

<details><summary>Verification</summary>

```verify
VLL = q(400, "V")
expect(VLL / sqrt(3), "230.9 V")
Zd = q(30, "ohm")
Iph = VLL / Zd
expect(Iph, "13.33 A")
expect(sqrt(3) * Iph, "23.09 A")
```

</details>

### Total three-phase power

For a balanced load, total power depends on line quantities and the angle of one phase's impedance.

$$P = \sqrt{3}\,V_{\text{LL}} I_{\text{L}} \cos\theta \qquad Q = \sqrt{3}\,V_{\text{LL}} I_{\text{L}} \sin\theta \qquad S = \sqrt{3}\,V_{\text{LL}} I_{\text{L}}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $P$ | total real power, all three phases | W |
| $Q$ | total reactive power, all three phases | var |
| $S$ | total apparent power, all three phases | VA |
| $V_{\text{LL}}$ | RMS line-to-line voltage | V |
| $I_{\text{L}}$ | RMS line current | A |
| $\theta$ | angle of one phase's impedance (phase voltage minus phase current), not the angle between a line voltage and a line current | rad |

Holds when: the load is balanced, in either wye or delta. The instantaneous total power is then constant in time.
Breaks when: the load is unbalanced. Then add the complex power of each phase, computed from its own phase voltage and current.
Source and basis: derived from summing three phase powers $3V_{\text{ph}}I_{\text{ph}}\cos\theta$; taught in [AC circuits, phasors, and power](../../physics/17-ac-circuits-phasors-and-power.md).

- Example: a balanced load draws 50 A at 400 V line-to-line and power factor 0.85 lagging. Then $S = 34641$ VA, $P = 29445$ W, and $Q = 18248$ var.

<details><summary>Verification</summary>

```verify
VLL = q(400, "V")
IL = q(50, "A")
pf = q(0.85, "1")
S = sqrt(3) * VLL * IL
expect(S, "34641 VA")
expect(S * pf, "29445 W")
expect(S * sqrt(1 - pf**2), "18248 var")
```

</details>

### Per-phase equivalent and delta-wye conversion

A balanced three-phase circuit is solved on one phase: replace every delta load with its equivalent wye, connect all neutrals with a wire of zero impedance (it carries no current), solve line to neutral, then multiply real and reactive power by three and take line voltages from phase voltages.

$$Z_{Y} = \frac{Z_{\Delta}}{3}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $Z_{Y}$ | impedance of each branch of the equivalent wye load | ohm |
| $Z_{\Delta}$ | impedance of each branch of the delta load | ohm |

Holds when: the three impedances of the delta are equal. The conversion then gives identical terminal currents and power.
Breaks when: the three impedances differ. The general conversion is a different formula that gives unequal wye branches.
Source and basis: derived from equating the terminal behavior of the two connections for a balanced load.

- Example: the 30 ohm delta load on a 400 V line-to-line supply is equivalent to a 10 ohm wye. Each takes 16000 W in total, and the wye line current is 23.09 A.

<details><summary>Verification</summary>

```verify
Zd = q(30, "ohm")
Zy = Zd / 3
expect(Zy, "10 ohm")
VLL = q(400, "V")
Iy = VLL / sqrt(3) / Zy
expect(Iy, "23.09 A")
expect(3 * Iy**2 * Zy, "16000 W")
expect(3 * VLL**2 / Zd, "16000 W")
```

</details>

## Per-unit quantities

A **per-unit (pu)** value is an actual value divided by a chosen base value of the same dimension. Choose the three-phase base power $S_{\text{base}}$ and the line-to-line base voltage $V_{\text{base}}$ for each voltage level; the other bases follow. On the two sides of a transformer, choose base voltages in the ratio of the rated line-to-line voltages, so the ideal transformer disappears from the per-unit network.

### Base quantities

$$I_{\text{base}} = \frac{S_{\text{base}}}{\sqrt{3}\,V_{\text{base}}} \qquad Z_{\text{base}} = \frac{V_{\text{base}}^2}{S_{\text{base}}} \qquad X_{\text{pu}} = \frac{X}{Z_{\text{base}}}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $S_{\text{base}}$ | three-phase base power | VA |
| $V_{\text{base}}$ | base voltage, line-to-line RMS | V |
| $I_{\text{base}}$ | base current, line RMS | A |
| $Z_{\text{base}}$ | base impedance, per phase of the equivalent wye | ohm |
| $X$ | actual reactance, per phase of the equivalent wye | ohm |
| $X_{\text{pu}}$ | per-unit reactance | dimensionless |

Holds when: the system is balanced and every quantity is taken in the per-phase equivalent. For a single-phase circuit use $I_{\text{base}} = S_{\text{base}}/V_{\text{base}}$ with single-phase $S_{\text{base}}$ and $V_{\text{base}}$.
Breaks when: bases at the two sides of a transformer are not in the ratio of the transformer's voltage ratings; the per-unit network then carries a spurious ideal ratio. Phase-shifting connections (delta-wye) also shift angles that per-unit values do not show.
Source and basis: derived from the definitions of power and impedance in the per-phase equivalent: $(V_{\text{LL}}/\sqrt{3})^2 / (S/3) = V_{\text{LL}}^2/S$.

- Example: with $S_{\text{base}} = 100$ MVA and $V_{\text{base}} = 138$ kV, $Z_{\text{base}} = 190.4$ ohm and $I_{\text{base}} = 418.4$ A. A reactance of 47.61 ohm is 0.25 pu.

<details><summary>Verification</summary>

```verify
Sb = q(100, "MVA")
Vb = q(138, "kV")
Zb = Vb**2 / Sb
expect(Zb, "190.4 ohm")
expect(Sb / (sqrt(3) * Vb), "418.4 A")
X = q(47.61, "ohm")
expect(X / Zb, "0.25")
```

</details>

### Change of base

A per-unit impedance given on a nameplate base converts to the system base by this rule.

$$Z_{\text{pu,new}} = Z_{\text{pu,old}}\,\frac{S_{\text{base,new}}}{S_{\text{base,old}}}\left(\frac{V_{\text{base,old}}}{V_{\text{base,new}}}\right)^2$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $Z_{\text{pu,old}}$ | per-unit impedance on the old base | dimensionless |
| $Z_{\text{pu,new}}$ | per-unit impedance on the new base | dimensionless |
| $S_{\text{base,old}}$ | old three-phase base power | VA |
| $S_{\text{base,new}}$ | new three-phase base power | VA |
| $V_{\text{base,old}}$ | old base voltage, line-to-line RMS | V |
| $V_{\text{base,new}}$ | new base voltage, line-to-line RMS | V |

Holds when: both bases refer to the same physical impedance at the same voltage level.
Breaks when: the old and new bases belong to different voltage levels without a transformer between them; convert through the transformer ratio first.
Source and basis: derived from equating the actual ohmic impedance, $Z_{\text{pu,old}} Z_{\text{base,old}} = Z_{\text{pu,new}} Z_{\text{base,new}}$.

- Example: a transformer rated 20 MVA and 13.2 kV with 0.08 pu impedance becomes 0.366 pu on a 100 MVA, 13.8 kV system base.

<details><summary>Verification</summary>

```verify
Zold = q(0.08, "1")
r = (q(100, "MVA") / q(20, "MVA")) * (q(13.2, "kV") / q(13.8, "kV"))**2
expect(Zold * r, "0.366")
```

</details>

## Transformers and equivalent circuits

### Ideal ratios and referred impedance

An ideal transformer has no losses, no leakage flux, and unlimited core permeability. An impedance on one side appears on the other side scaled by the square of the turns ratio.

$$k_{\text{t}} = \frac{N_1}{N_2} = \frac{V_1}{V_2} = \frac{I_2}{I_1} \qquad Z_2' = k_{\text{t}}^2\,Z_2$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $k_{\text{t}}$ | turns ratio, primary to secondary | dimensionless |
| $N_1$ | primary turns | dimensionless |
| $N_2$ | secondary turns | dimensionless |
| $V_1$ | RMS voltage, primary winding (single-phase) | V |
| $V_2$ | RMS voltage, secondary winding (single-phase) | V |
| $I_1$ | RMS current, primary winding | A |
| $I_2$ | RMS current, secondary winding | A |
| $Z_2$ | impedance connected to the secondary | ohm |
| $Z_2'$ | the same impedance referred to the primary | ohm |

Holds when: the operation is sinusoidal steady state and losses and magnetizing current are negligible. For a three-phase bank use the winding (phase) voltages, not the line voltages, in $V_1/V_2$.
Breaks when: the load is heavy enough that winding drops matter, or the frequency is low enough that the core saturates.
Source and basis: derived from Faraday's law with the same flux in both windings; taught in [Transformers](05-transformers.md).

- Example: a 25 kVA transformer rated 7200 V to 240 V has $k_{\text{t}} = 30$, a rated primary current of 3.472 A, and a rated secondary current of 104.2 A. A 2.4 ohm load appears as 2160 ohm at the primary.

<details><summary>Verification</summary>

```verify
V1 = q(7200, "V")
V2 = q(240, "V")
S = q(25, "kVA")
k = V1 / V2
expect(k, "30")
expect(S / V1, "3.472 A")
expect(S / V2, "104.2 A")
expect(k**2 * q(2.4, "ohm"), "2160 ohm")
```

</details>

### Open-circuit and short-circuit tests

The approximate equivalent circuit has a series resistance and leakage reactance and a shunt branch of core-loss resistance and magnetizing reactance. Two tests find them, using per-phase values for a three-phase unit.

$$Q_{\text{oc}} = \sqrt{(V_{\text{oc}} I_{\text{oc}})^2 - P_{\text{oc}}^2} \qquad R_c = \frac{V_{\text{oc}}^2}{P_{\text{oc}}} \qquad X_m = \frac{V_{\text{oc}}^2}{Q_{\text{oc}}}$$

$$R_{\text{eq}} = \frac{P_{\text{sc}}}{I_{\text{sc}}^2} \qquad Z_{\text{eq}} = \frac{V_{\text{sc}}}{I_{\text{sc}}} \qquad X_{\text{eq}} = \sqrt{Z_{\text{eq}}^2 - R_{\text{eq}}^2}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $V_{\text{oc}}$ | open-circuit test voltage, rated, per phase RMS | V |
| $I_{\text{oc}}$ | open-circuit test current, per phase RMS | A |
| $P_{\text{oc}}$ | open-circuit test power, per phase (core loss) | W |
| $Q_{\text{oc}}$ | open-circuit reactive power, per phase | var |
| $R_c$ | core-loss resistance, on the tested side | ohm |
| $X_m$ | magnetizing reactance, on the tested side | ohm |
| $V_{\text{sc}}$ | short-circuit test voltage, reduced, per phase RMS | V |
| $I_{\text{sc}}$ | short-circuit test current, rated, per phase RMS | A |
| $P_{\text{sc}}$ | short-circuit test power, per phase (copper loss) | W |
| $R_{\text{eq}}$ | equivalent series resistance, on the tested side | ohm |
| $Z_{\text{eq}}$ | equivalent series impedance magnitude, on the tested side | ohm |
| $X_{\text{eq}}$ | equivalent leakage reactance, on the tested side | ohm |

Holds when: the open-circuit test is run at rated voltage on one winding with the other open (usually the low-voltage side), the short-circuit test is run at reduced voltage with rated current and the other winding shorted (usually the high-voltage side), and the circuit is linear. Parameters from the two sides are combined only after referring one set with $k_{\text{t}}^2$.
Breaks when: the core saturates (the open-circuit result then depends on voltage), the test frequency differs from service, or the unit is large enough that the shunt branch must be placed between the two series elements.
Source and basis: derived from circuit analysis of the approximate equivalent circuit; taught in [Transformers](05-transformers.md).

- Example: for a 25 kVA, 7200 V to 240 V unit, an open-circuit test at 240 V, 1.5 A, and 120 W gives $Q_{\text{oc}} = 339.4$ var, $R_c = 480$ ohm, and $X_m = 169.7$ ohm on the low side. A short-circuit test at rated current 3.472 A, 220 V, and 350 W gives $R_{\text{eq}} = 29.03$ ohm, $Z_{\text{eq}} = 63.36$ ohm, and $X_{\text{eq}} = 56.32$ ohm on the high side.

<details><summary>Verification</summary>

```verify
Voc = q(240, "V")
Ioc = q(1.5, "A")
Poc = q(120, "W")
Qoc = sqrt((Voc * Ioc)**2 - Poc**2)
expect(Qoc, "339.4 var")
expect(Voc**2 / Poc, "480 ohm")
expect(Voc**2 / Qoc, "169.7 ohm")
Isc = q(25, "kVA") / q(7200, "V")
expect(Isc, "3.472 A")
Req = q(350, "W") / Isc**2
Zeq = q(220, "V") / Isc
expect(Req, "29.03 ohm")
expect(Zeq, "63.36 ohm")
expect(sqrt(Zeq**2 - Req**2), "56.32 ohm")
```

</details>

### Regulation and efficiency

Voltage regulation is the change in secondary voltage from no load to full load at a given power factor, as a fraction of the full-load value. Efficiency is output power over input power.

$$\mathrm{VR} \approx \varepsilon_R \cos\theta + \varepsilon_X \sin\theta \qquad \eta = \frac{x\,S_{\text{rated}}\cos\theta}{x\,S_{\text{rated}}\cos\theta + P_{\text{core}} + x^2 P_{\text{cu,rated}}} \qquad x_{\eta,\max} = \sqrt{\frac{P_{\text{core}}}{P_{\text{cu,rated}}}}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\mathrm{VR}$ | voltage regulation | dimensionless |
| $\varepsilon_R$ | per-unit equivalent resistance, $R_{\text{eq}} I_{\text{rated}} / V_{\text{rated}}$ | dimensionless |
| $\varepsilon_X$ | per-unit equivalent reactance, $X_{\text{eq}} I_{\text{rated}} / V_{\text{rated}}$ | dimensionless |
| $\theta$ | load power angle, positive for a lagging load (use a negative angle for a leading load) | rad |
| $\eta$ | efficiency | dimensionless |
| $x$ | load as a fraction of rated apparent power | dimensionless |
| $S_{\text{rated}}$ | rated apparent power | VA |
| $P_{\text{core}}$ | core loss, taken as constant with load | W |
| $P_{\text{cu,rated}}$ | copper loss at rated current | W |

Holds when: the per-unit impedance is small (a few percent), the load voltage stays near rated, and core loss is constant at rated voltage and frequency.
Breaks when: the impedance is large, the load is highly leading and the secondary voltage rises above no-load, or the supply voltage varies (core loss then changes).
Source and basis: derived from the approximate equivalent circuit, neglecting the quadrature component of the drop; taught in [Transformers](05-transformers.md).

- Example: with $R_{\text{eq}}$ and $X_{\text{eq}}$ from the tests above, $\varepsilon_R = 0.014$ and $\varepsilon_X = 0.02716$. At power factor 0.8 lagging, $\mathrm{VR} = 0.0275$. At $x = 0.75$ and the same power factor, $\eta = 0.9793$. Efficiency peaks at $x = 0.5855$, where copper loss equals core loss.

<details><summary>Verification</summary>

```verify
Isc = q(25, "kVA") / q(7200, "V")
Req = q(350, "W") / Isc**2
Zeq = q(220, "V") / Isc
Xeq = sqrt(Zeq**2 - Req**2)
V = q(7200, "V")
eR = Req * Isc / V
eX = Xeq * Isc / V
expect(eR, "0.014")
expect(eX, "0.02716")
pf = q(0.8, "1")
expect(eR * pf + eX * sqrt(1 - pf**2), "0.0275")
x = q(0.75, "1")
S = q(25, "kVA")
Pc = q(120, "W")
Pcu = q(350, "W")
Po = x * S * pf
expect(Po / (Po + Pc + x**2 * Pcu), "0.9793")
expect(sqrt(Pc / Pcu), "0.5855")
```

</details>

## Rotating machines

### Synchronous speed and slip

The stator of a polyphase machine with $p$ poles produces a magnetic field that rotates at synchronous speed. An induction motor turns slower than that field by the slip.

$$\omega_s = \frac{4\pi f}{p} \qquad s_{\text{sl}} = \frac{\omega_s - \omega_m}{\omega_s} \qquad \omega_m = (1 - s_{\text{sl}})\,\omega_s \qquad f_r = s_{\text{sl}}\,f$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\omega_s$ | synchronous angular speed (mechanical) | rad/s |
| $\omega_m$ | rotor angular speed (mechanical) | rad/s |
| $f$ | stator supply frequency | Hz |
| $p$ | number of poles, an even integer | dimensionless |
| $s_{\text{sl}}$ | slip | dimensionless |
| $f_r$ | rotor current frequency | Hz |

Holds when: the stator carries balanced polyphase currents of a single frequency, in steady state.
Breaks when: the supply is single-phase (no rotating field without extra windings), the voltage is non-sinusoidal (harmonic fields rotate at other speeds), or the machine runs as a generator (slip is negative).
Source and basis: derived from a rotating field of $p/2$ pole pairs crossing the rotor; taught in [Induction motors](03-induction-motors.md).

- Example: a four-pole motor on a 50 Hz supply (example input) has $\omega_s = 157.1$ rad/s, which is 1500 rev/min. At a slip of 0.04 its rotor speed is 1440 rev/min and its rotor frequency is 2 Hz.

<details><summary>Verification</summary>

```verify
f = q(50, "Hz")
p = q(4, "1")
ws = 4 * pi * f / p
expect(ws, "157.1 rad/s")
expect(ws, "1500 rev/min")
s = q(0.04, "1")
expect((1 - s) * ws, "1440 rev/min")
expect(s * f, "2 Hz")
```

</details>

### Induction motor power split

Power crosses the air gap to the rotor. A fraction equal to the slip is lost as rotor copper loss, and the rest becomes mechanical power.

$$P_{\text{ag}} = 3\,I_2'^2\,\frac{R_2'}{s_{\text{sl}}} \qquad P_{\text{cu,r}} = s_{\text{sl}}\,P_{\text{ag}} \qquad P_{\text{mech}} = (1 - s_{\text{sl}})\,P_{\text{ag}} \qquad \mathcal{T} = \frac{P_{\text{ag}}}{\omega_s} = \frac{P_{\text{mech}}}{\omega_m}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $P_{\text{ag}}$ | air-gap power, all three phases | W |
| $P_{\text{cu,r}}$ | rotor copper loss, all three phases | W |
| $P_{\text{mech}}$ | internal mechanical power, before friction and windage | W |
| $I_2'$ | rotor phase current referred to the stator, RMS | A |
| $R_2'$ | rotor resistance per phase referred to the stator | ohm |
| $s_{\text{sl}}$ | slip | dimensionless |
| $\mathcal{T}$ | electromagnetic torque | N m |
| $\omega_s$ | synchronous angular speed | rad/s |
| $\omega_m$ | rotor angular speed | rad/s |

Holds when: the supply is balanced, the machine is in steady state, and the per-phase equivalent circuit (stator impedance, shunt magnetizing branch, rotor branch $R_2'/s_{\text{sl}} + jX_2'$) applies with constant parameters.
Breaks when: the supply is unbalanced (a negative-sequence field opposes torque), the iron saturates, or the rotor's skin effect changes $R_2'$ with slip. Shaft power is $P_{\text{mech}}$ minus friction and windage.
Source and basis: derived from the per-phase equivalent circuit, where the power in $R_2'(1-s_{\text{sl}})/s_{\text{sl}}$ is the mechanical power; taught in [Induction motors](03-induction-motors.md).

- Example: a four-pole, 50 Hz motor develops 7500 W of internal mechanical power at 1450 rev/min. Its slip is 0.0333, $P_{\text{ag}} = 7759$ W, $P_{\text{cu,r}} = 258.6$ W, and $\mathcal{T} = 49.39$ N m.

<details><summary>Verification</summary>

```verify
f = q(50, "Hz")
ws = 4 * pi * f / q(4, "1")
wm = q(1450, "rev/min")
s = (ws - wm) / ws
expect(s, "0.0333")
Pm = q(7500, "W")
Pag = Pm / (1 - s)
expect(Pag, "7759 W")
expect(s * Pag, "258.6 W")
expect(Pm / wm, "49.39 N m")
```

</details>

### DC machine: back EMF and torque

In a DC machine with constant field flux, the voltage induced in the armature is proportional to speed and the torque is proportional to armature current, with the same constant in SI units.

$$E_a = k_\phi\,\omega_m \qquad \mathcal{T} = k_\phi\,I_a \qquad V_t = E_a + I_a R_a \ (\text{motor}) \qquad V_t = E_a - I_a R_a \ (\text{generator})$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $E_a$ | back EMF (generated armature voltage), DC | V |
| $k_\phi$ | machine constant at constant flux (torque constant equals voltage constant) | V s/rad |
| $\omega_m$ | rotor angular speed | rad/s |
| $\mathcal{T}$ | electromagnetic torque | N m |
| $I_a$ | armature current, DC | A |
| $V_t$ | terminal voltage, DC | V |
| $R_a$ | armature circuit resistance | ohm |

Holds when: the field flux is constant (permanent magnet or fixed field current), magnetic behavior is linear, and brush drop and armature reaction are neglected.
Breaks when: the field is weakened or saturated, the armature current is large enough to distort the flux, or the supply is a switched converter with ripple current (average values still hold; the heating does not).
Source and basis: derived from Faraday's law and the Lorentz force on the armature conductors; taught in [DC motors](01-dc-motors.md).

- Example: a motor on 120 V DC with $R_a = 0.5$ ohm and $k_\phi = 0.6$ V s/rad draws 20 A. Then $E_a = 110$ V, the speed is 183.3 rad/s, the torque is 12 N m, and the mechanical power is 2200 W.

<details><summary>Verification</summary>

```verify
Vt = q(120, "V")
Ra = q(0.5, "ohm")
Ia = q(20, "A")
k = q(0.6, "V s/rad")
Ea = Vt - Ia * Ra
expect(Ea, "110 V")
wm = Ea / k
expect(wm, "183.3 rad/s")
expect(k * Ia, "12 N m")
expect(Ea * Ia, "2200 W")
```

</details>

## Transmission-line models

Each model is per phase, line to neutral, for a balanced system. Series impedance $\underline{Z} = R + jX$ and total shunt admittance $\underline{Y}$ are for the whole line length.

### Short line

The short-line model keeps only the series impedance. The sending-end voltage magnitude for a lagging receiving-end load is below, with the receiving-end phase voltage as the reference.

$$\lvert\underline{V}_S\rvert = \sqrt{\left(V_R + R I \cos\theta + X I \sin\theta\right)^2 + \left(X I \cos\theta - R I \sin\theta\right)^2} \qquad \underline{I}_S = \underline{I}_R$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\underline{V}_S$ | sending-end phase voltage (line-to-neutral), RMS | V |
| $V_R$ | receiving-end phase voltage (line-to-neutral), RMS, the reference | V |
| $R$ | total series resistance of one conductor | ohm |
| $X$ | total series reactance of one conductor | ohm |
| $I$ | line current, RMS, equal at both ends | A |
| $\underline{I}_S$ | sending-end line current, RMS | A |
| $\underline{I}_R$ | receiving-end line current, RMS | A |
| $\theta$ | receiving-end power angle, positive for a lagging load (use a negative angle for a leading load) | rad |

Holds when: the shunt capacitance is small enough to ignore, which is true for short overhead lines at moderate voltage, and the system is balanced.
Breaks when: the line is long or a cable (shunt capacitance matters; use the pi model), or the system is unbalanced.
Source and basis: derived from $\underline{V}_S = \underline{V}_R + \underline{Z}\,\underline{I}_R$ with the current at the angle $-\theta$.

- Example: a line with $R = 10$ ohm and $X = 40$ ohm per phase carries 200 A at power factor 0.9 lagging to a receiving end of 132 kV line-to-line. The receiving-end phase voltage is 76.21 kV. The sending-end phase voltage is 81.74 kV, which is 0.0726 of the receiving-end value above it.

<details><summary>Verification</summary>

```verify
VR = q(132, "kV") / sqrt(3)
expect(VR, "76.21 kV")
R = q(10, "ohm")
X = q(40, "ohm")
I = q(200, "A")
c = q(0.9, "1")
sn = sqrt(1 - c**2)
VS = sqrt((VR + R * I * c + X * I * sn)**2 + (X * I * c - R * I * sn)**2)
expect(VS, "81.74 kV")
expect((VS - VR) / VR, "0.0726")
```

</details>

### Medium line, nominal pi

The nominal pi model splits the total shunt admittance into two halves, one at each end, and puts the series impedance between them.

$$\underline{V}_S = \left(1 + \frac{\underline{Z}\,\underline{Y}}{2}\right)\underline{V}_R + \underline{Z}\,\underline{I}_R \qquad \underline{I}_S = \underline{Y}\left(1 + \frac{\underline{Z}\,\underline{Y}}{4}\right)\underline{V}_R + \left(1 + \frac{\underline{Z}\,\underline{Y}}{2}\right)\underline{I}_R$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\underline{V}_S$ | sending-end phase voltage (line-to-neutral), RMS | V |
| $\underline{V}_R$ | receiving-end phase voltage (line-to-neutral), RMS | V |
| $\underline{I}_S$ | sending-end line current, RMS | A |
| $\underline{I}_R$ | receiving-end line current, RMS | A |
| $\underline{Z}$ | total series impedance of one conductor | ohm |
| $\underline{Y}$ | total shunt admittance, line to neutral | S |

Holds when: the line is balanced and of moderate length, so that lumping the shunt admittance in two halves is accurate enough.
Breaks when: the line is long enough that voltage and current vary visibly along its length (use the distributed-parameter model), or the system is unbalanced.
Source and basis: derived from Kirchhoff's laws applied to the pi circuit.

- Example: at no load ($\underline{I}_R = 0$) the factor $1 + \underline{Z}\,\underline{Y}/2$ gives the voltage ratio from sending to receiving end. With $X = 40$ ohm, $R = 10$ ohm, and $B = 4 \times 10^{-4}$ S, its magnitude is 0.9920, so the receiving end rises 0.00806 of its own value above the sending end. This is the Ferranti effect.

<details><summary>Verification</summary>

```verify
R = q(10, "ohm")
X = q(40, "ohm")
B = q(0.0004, "S")
A = sqrt((1 - B * X / 2)**2 + (B * R / 2)**2)
expect(A, "0.9920")
expect(1 / A - 1, "0.00806")
```

</details>

## Voltage drop and losses

### Voltage-drop approximation

When the drop is small compared with the voltage, the magnitude of the drop is close to the component of the impedance drop in phase with the voltage.

$$\Delta V_{1\phi} \approx 2\,I\,\ell\,\left(r'\cos\theta + x'\sin\theta\right) \qquad \Delta V_{\text{LL}} \approx \sqrt{3}\,I\,\ell\,\left(r'\cos\theta + x'\sin\theta\right)$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\Delta V_{1\phi}$ | voltage drop across the out-and-back conductors, single-phase, RMS | V |
| $\Delta V_{\text{LL}}$ | line-to-line voltage drop, balanced three-phase, RMS | V |
| $I$ | line current, RMS | A |
| $\ell$ | one-way length of the circuit | m |
| $r'$ | resistance of one conductor per unit length | ohm/m |
| $x'$ | reactance of one conductor per unit length | ohm/m |
| $\theta$ | load power angle, positive for lagging | rad |

Holds when: the drop is a few percent of the supply voltage, the load is balanced for three-phase, and the load current is fixed.
Breaks when: the drop is large (use the exact short-line formula), the load is a constant-power load whose current rises as voltage falls, or the circuit is long enough to need the pi model.
Source and basis: derived from the phasor drop $\underline{I}(r' + jx')\ell$ projected on the voltage axis, with a factor of two for the return conductor (single-phase) or $\sqrt{3}$ (balanced three-phase, line to line).

- Example: a three-phase circuit of 100 m carries 32 A at power factor 0.9 lagging, with $r' = 2.0$ mohm/m and $x' = 0.08$ mohm/m (example inputs, not table values). The line-to-line drop is 10.17 V, which is 0.0254 of a 400 V supply.

<details><summary>Verification</summary>

```verify
I = q(32, "A")
l = q(100, "m")
rp = q(2.0, "mohm/m")
xp = q(0.08, "mohm/m")
c = q(0.9, "1")
dV = sqrt(3) * I * l * (rp * c + xp * sqrt(1 - c**2))
expect(dV, "10.17 V")
expect(dV / q(400, "V"), "0.0254")
```

</details>

### Conductor loss and voltage level

Resistive loss heats the conductors. At fixed delivered power, raising the voltage lowers the current and with it the loss.

$$P_{\text{loss}} = 3\,I_{\text{L}}^2 R \qquad P_{\text{loss}} = \frac{P^2 R}{V_{\text{LL}}^2 \cos^2\theta}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $P_{\text{loss}}$ | total conductor loss in three phases | W |
| $I_{\text{L}}$ | RMS line current | A |
| $R$ | resistance of one conductor | ohm |
| $P$ | real power delivered, all three phases | W |
| $V_{\text{LL}}$ | RMS line-to-line voltage | V |
| $\theta$ | load power angle | rad |

Holds when: the load is balanced three-phase, the conductor resistance is the AC resistance at operating temperature, and the delivered power and power factor are fixed. For single-phase out-and-back wiring use $2 I^2 R$.
Breaks when: the load is unbalanced (add each phase's $I^2 R$), the current is distorted (harmonics raise the RMS current), or the power is delivered at constant current instead of constant power.
Source and basis: derived from $P = \sqrt{3}\,V_{\text{LL}} I_{\text{L}} \cos\theta$ and the heating $I^2 R$ in each conductor.

- Example: 10 MW at power factor 0.95 over conductors of 4 ohm each loses 407.0 kW at 33 kV and 25.44 kW at 132 kV, a ratio of 16.

<details><summary>Verification</summary>

```verify
P = q(10, "MW")
R = q(4, "ohm")
c = q(0.95, "1")
L1 = P**2 * R / (q(33, "kV")**2 * c**2)
L2 = P**2 * R / (q(132, "kV")**2 * c**2)
expect(L1, "407.0 kW")
expect(L2, "25.44 kW")
expect(L1 / L2, "16")
```

</details>

## Symmetrical components

Any set of three phasors, balanced or not, is the sum of three balanced sets: positive sequence (same order as the source), negative sequence (opposite order), and zero sequence (three equal phasors). For a network with symmetrical elements the three sequence networks do not couple, so each is solved alone.

### The transform

$$\begin{bmatrix}\underline{I}_0 \\ \underline{I}_1 \\ \underline{I}_2\end{bmatrix} = \frac{1}{3}\begin{bmatrix}1 & 1 & 1 \\ 1 & \underline{a} & \underline{a}^2 \\ 1 & \underline{a}^2 & \underline{a}\end{bmatrix}\begin{bmatrix}\underline{I}_a \\ \underline{I}_b \\ \underline{I}_c\end{bmatrix} \qquad \underline{a} = e^{j2\pi/3}$$

$$\underline{I}_n = 3\,\underline{I}_0$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\underline{I}_0$ | zero-sequence current phasor, RMS | A |
| $\underline{I}_1$ | positive-sequence current phasor, RMS | A |
| $\underline{I}_2$ | negative-sequence current phasor, RMS | A |
| $\underline{I}_a$ | phase a line current phasor, RMS | A |
| $\underline{I}_b$ | phase b line current phasor, RMS | A |
| $\underline{I}_c$ | phase c line current phasor, RMS | A |
| $\underline{I}_n$ | neutral current phasor, RMS | A |
| $\underline{a}$ | rotation operator, 120 degrees | dimensionless |

Holds when: the system is linear and at one frequency. The transform holds for any three phasors. The sequence networks decouple only when the network elements are symmetrical.
Breaks when: network elements are unequal in the three phases (an open conductor, an unbalanced load). The sequence networks then couple and must be connected at the unbalance. The same transform applies to voltages with the same matrix.
Source and basis: derived from linear algebra; the matrix is the three-point discrete Fourier transform. For matrix operations see [Foundations reference](../../math/reference-foundations.md).

- Example: only phase a carries 30 A (b and c open). Then $I_0 = I_1 = I_2$ each have magnitude 10 A, and the neutral current is 30 A.

<details><summary>Verification</summary>

```verify
Ia = q(30, "A")
Ib = q(0, "A")
Ic = q(0, "A")
I0 = (Ia + Ib + Ic) / 3
expect(I0, "10 A")
expect(3 * I0, "30 A")
```

</details>

### Sequence networks, in words

The positive-sequence network is the usual balanced per-phase network, with the source. The negative-sequence network has no source and, for static elements, the same impedances as positive sequence. The zero-sequence network has no source and depends on how windings are connected and grounded: a delta winding blocks zero-sequence current from flowing out of it, and a wye winding passes it only if the neutral is grounded. Unbalanced faults connect the three sequence networks at the fault point in a way set by the fault type.

## Fault-current basics

### Three-phase bolted fault

A bolted fault has zero impedance at the fault. The balanced three-phase fault current is the prefault voltage divided by the Thevenin impedance seen from the fault point.

$$I_{f,\text{pu}} = \frac{V_{\text{pre,pu}}}{Z_{\text{th,pu}}} \qquad I_f = I_{f,\text{pu}}\,I_{\text{base}} \qquad S_{\text{sc}} = \frac{S_{\text{base}}}{Z_{\text{th,pu}}}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $I_{f,\text{pu}}$ | per-unit fault current, line current | dimensionless |
| $V_{\text{pre,pu}}$ | per-unit prefault line-to-neutral voltage at the fault point | dimensionless |
| $Z_{\text{th,pu}}$ | per-unit Thevenin impedance magnitude to the fault point | dimensionless |
| $I_f$ | fault current, RMS line current | A |
| $I_{\text{base}}$ | base current at the fault's voltage level | A |
| $S_{\text{sc}}$ | short-circuit apparent power | VA |
| $S_{\text{base}}$ | three-phase base power | VA |

Holds when: the fault is balanced and bolted, the network is linear, the prefault voltage is near 1 pu, load current is neglected, and machines are represented by their subtransient reactance for the first cycle.
Breaks when: the fault has impedance (arc, ground), the fault is unbalanced (use sequence networks), or motors and generators feed the fault with decaying current (the current changes over the first cycles).
Source and basis: derived from Thevenin's theorem applied to the network and Ohm's law; taught in [The power grid](08-the-power-grid.md).

- Example: on a 100 MVA, 13.8 kV base, a source reactance of 0.05 pu in series with a transformer of 0.10 pu gives a Thevenin impedance of 0.15 pu. The fault current is 6.667 pu, or 27.89 kA, and the short-circuit power is 666.7 MVA.

<details><summary>Verification</summary>

```verify
Sb = q(100, "MVA")
Vb = q(13.8, "kV")
Ib = Sb / (sqrt(3) * Vb)
Zth = q(0.05, "1") + q(0.10, "1")
expect(Zth, "0.15")
If = q(1, "1") / Zth
expect(If, "6.667")
expect(If * Ib, "27.89 kA")
expect(Sb / Zth, "666.7 MVA")
```

</details>

### Unbalanced bolted faults

Two common unbalanced faults connect the sequence networks at the fault point. The magnitudes below are for a bolted fault on phase a (single line to ground) and between phases b and c (line to line).

$$I_{f,\text{SLG}} = \frac{3\,V_f}{Z_0 + Z_1 + Z_2} \qquad I_{f,\text{LL}} = \frac{\sqrt{3}\,V_f}{Z_1 + Z_2}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $I_{f,\text{SLG}}$ | fault current magnitude in the faulted phase, single line to ground | dimensionless |
| $I_{f,\text{LL}}$ | fault current magnitude in each faulted phase, line to line | dimensionless |
| $V_f$ | prefault phase voltage at the fault point, per unit | dimensionless |
| $Z_0$ | zero-sequence Thevenin impedance, per unit | dimensionless |
| $Z_1$ | positive-sequence Thevenin impedance, per unit | dimensionless |
| $Z_2$ | negative-sequence Thevenin impedance, per unit | dimensionless |

Holds when: the faults are bolted, the network is linear, and the impedances are all reactive or all have the same angle, so they add as magnitudes. Otherwise add them as complex numbers.
Breaks when: fault impedance is present (it adds to the sum in the SLG case, and is different in the LL case), or load current is large compared with the fault current.
Source and basis: derived from interconnecting the sequence networks for each fault type, with $\underline{I}_0 = \underline{I}_1 = \underline{I}_2$ for single line to ground and $\underline{I}_0 = 0$, $\underline{I}_2 = -\underline{I}_1$ for line to line.

- Example: with $Z_1 = Z_2 = 0.10$ pu and $Z_0 = 0.05$ pu, the single-line-to-ground current is 12 pu, the line-to-line current is 8.660 pu, and the three-phase current is 10 pu. The ground fault is the largest because $Z_0$ is smaller than $Z_1$.

<details><summary>Verification</summary>

```verify
Z1 = q(0.10, "1")
Z2 = q(0.10, "1")
Z0 = q(0.05, "1")
Vf = q(1, "1")
expect(3 * Vf / (Z0 + Z1 + Z2), "12")
expect(sqrt(3) * Vf / (Z1 + Z2), "8.660")
expect(Vf / Z1, "10")
```

</details>

### X/R ratio and DC offset

A fault current starts with a decaying DC component whose size depends on the instant the fault occurs. The ratio of reactance to resistance sets how long it lasts and how much it adds to the first peak.

$$\tau_{dc} = \frac{X}{\omega R} \qquad I_{\text{pk}} \approx \sqrt{2}\,I_{\text{sym}}\left(1 + e^{-\pi R/X}\right)$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\tau_{dc}$ | time constant of the DC component | s |
| $X$ | Thevenin reactance to the fault | ohm |
| $R$ | Thevenin resistance to the fault | ohm |
| $\omega$ | angular frequency of the system | rad/s |
| $I_{\text{pk}}$ | first peak of the fault current in the worst case | A |
| $I_{\text{sym}}$ | RMS value of the symmetrical (AC) fault current | A |

Holds when: the fault occurs at the instant that gives the largest offset (voltage zero crossing), the network is a series resistance and inductance, and the AC component does not decay.
Breaks when: the network has several time constants, or machines feed the fault so the AC component decays. At the example ratio below, the estimate is about 0.4 percent below the exact maximum.
Source and basis: derived from the solution of $L\,di/dt + Ri = \sqrt{2}\,V\sin(\omega t + \alpha)$; the exact peak is found by setting the derivative to zero.

- Example: at $X/R = 10$ and 50 Hz (example input), $\tau_{dc} = 31.83$ ms and the peak factor is 1.730. A symmetrical fault current of 20 kA RMS has a first peak of 48.94 kA.

<details><summary>Verification</summary>

```verify
XR = q(10, "1")
f = q(50, "Hz")
expect(XR / (2 * pi * f), "31.83 ms")
k = 1 + exp(-pi / XR)
expect(k, "1.730")
exact = q(1.7368, "1", of="none")
expect(100 * (exact - k) / exact, "0.4")
expect(sqrt(2) * q(20, "kA") * k, "48.94 kA")
```

</details>

## Protection boundary

A protective device senses a condition and opens a circuit. This sheet states what the devices do and leaves settings and selection to the standard, the manufacturer's curves, and a coordination study.

- A **fuse** has an element that melts when the heat $\int i^2\,dt$ in it reaches a set value. It opens faster at higher current.
- A **circuit breaker** opens a mechanical contact, either by a thermal element, a magnetic element, or a relay that senses current, voltage, or angle.
- A device must have an interrupting rating above the largest fault current that can reach it. Use the bolted fault calculation as the starting point and the standard's rules for the exact duty.
- A residual-current device or ground-fault interrupter trips when the current in the line conductors differs from the return current, which means current leaves through an unintended path.
- Devices in series are coordinated so that the one nearest the fault opens first. Coordination uses published time-current curves and is a study, not a formula.
- This sheet gives no trip settings, no rating tables, and no code requirements.

## Conductor and thermal boundary

### Resistance from resistivity and temperature

$$R = \frac{\rho_{\text{e}}\,\ell}{A} \qquad R(T_2) = R(T_1)\left[1 + \alpha_R\,(T_2 - T_1)\right]$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $R$ | conductor DC resistance | ohm |
| $\rho_{\text{e}}$ | electrical resistivity of the conductor material | ohm m |
| $\ell$ | conductor length | m |
| $A$ | conductor cross-section area | $\text{m}^2$ |
| $R(T_1)$ | resistance at temperature $T_1$ | ohm |
| $R(T_2)$ | resistance at temperature $T_2$ | ohm |
| $\alpha_R$ | temperature coefficient of resistance, a material property | 1/K |
| $T_1$ | reference temperature | K |
| $T_2$ | operating temperature | K |

Holds when: the current is uniform over the cross section (DC or low frequency), the material is uniform, and the temperature change is moderate so the coefficient is constant. Take $\rho_{\text{e}}$ and $\alpha_R$ for the actual material and condition from a registered property source.
Breaks when: the frequency or conductor size is large enough for skin and proximity effects to raise the resistance, the temperature range is wide, or the conductor is stranded (a lay factor lengthens the path).
Source and basis: derived from the definition of resistivity, $\rho_{\text{e}} = R A / \ell$; the temperature coefficient is a measured material property.

- Example: with example inputs (not table values) $\rho_{\text{e}} = 1.7 \times 10^{-8}$ ohm m, $A = 10\ \text{mm}^2$, and $\ell = 100$ m, $R = 0.17$ ohm. With $\alpha_R = 0.004$ per kelvin, heating by 50 K raises it to 0.204 ohm.

<details><summary>Verification</summary>

```verify
rho = q(1.7e-8, "ohm m")
A = q(10, "mm^2")
l = q(100, "m")
R1 = rho * l / A
expect(R1, "0.17 ohm")
a = q(0.004, "1/K")
dT = q(50, "K")
expect(R1 * (1 + a * dT), "0.204 ohm")
```

</details>

### Ampacity is a code question

Ampacity is the largest current a conductor can carry continuously without exceeding its insulation temperature rating. It depends on the insulation type, the ambient temperature, how many conductors share a raceway, the installation method, and the terminations. The adopted electrical code of the jurisdiction sets the allowed values, and codes differ by country and change by edition. This sheet gives no ampacity table. Use the code in force at the site.

## Checklists

- Voltage: is each value RMS or peak, line-to-line or phase?
- Current: is each value a line or a phase current? Does the load connection (wye or delta) match the formula?
- Is the system balanced? If not, use symmetrical components or per-phase calculation, not the balanced formulas.
- Sign convention: is reactive power positive for an inductive load, and is the power factor labelled lagging or leading?
- Per-unit: are all quantities on one base, and are the transformer base voltages in the ratio of the voltage ratings?
- Frequency and voltage: are the regional values the site's own, not an example's?
- Fault duty: is the interrupting rating of each device above the maximum fault current at its location, including the DC offset?
- Conductors: are resistance, ampacity, and voltage drop all checked, and is the ampacity from the code in force?
- Units: does every product of volt and ampere carry the right name (W, var, or VA)?

## Sanity checks

- A balanced three-phase line current is the apparent power over $\sqrt{3}$ times the line-to-line voltage. If the answer is off by about 1.73, a phase quantity was used as a line quantity.
- Real power cannot exceed apparent power. Power factor lies between 0 and 1.
- Doubling the voltage at fixed delivered power quarters the conductor loss.
- Per-unit impedances on a common base add like ohms; a per-unit value on the wrong base is off by the ratio of the base powers.
- Induction motor slip at rated load is a few percent (typical). A slip near 0 or near 1 at rated load points to an input error.
- The fault current in per unit is the reciprocal of the Thevenin impedance in per unit. A fault current below the rated current points to an error.
- A transformer's referred impedance changes by the square of the turns ratio. A factor off by the ratio, not its square, is a common error.
- Capacitor reactive power rises with the square of voltage. A capacitor at a lower voltage gives less than its rating.

## Further reference

- *Power System Analysis*, Grainger and Stevenson. Per-unit, fault, and line models.
- *Power System Analysis and Design*, Glover, Overbye, and Sarma. Fault and line models.
- *Electric Machinery Fundamentals*, Chapman. Transformers, induction, and DC machines.
- *Short-circuit currents in three-phase a.c. systems*, IEC 60909. The standard method for fault current.
- [Introduction to Electric Power Systems (6.061), MIT OpenCourseWare](https://ocw.mit.edu/courses/6-061-introduction-to-electric-power-systems-spring-2011/): free lectures and notes on three-phase systems, transformers, and machines.
- [*University Physics Volume 2*, Chapter 15 (Alternating-Current Circuits), OpenStax](https://openstax.org/books/university-physics-volume-2/pages/15-introduction): free textbook chapter on AC circuits and power.
- Related sheets: [Circuit relations](../../physics/reference-fields-waves-space.md#circuit-relations) for direct-current laws, and [Foundations reference](../../math/reference-foundations.md) for complex numbers.
