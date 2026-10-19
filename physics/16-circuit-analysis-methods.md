# Circuit analysis methods

**Type:** lesson
**Verify:** strict

Circuit analysis is the set of methods that find every voltage and current in a network of sources, resistors, capacitors, inductors, and amplifiers from two conservation laws and the behaviour of each part. Sensors, motor drives, instrumentation, and control hardware are all circuits, and a mechanical engineer who can reduce a network to a few equations can size a supply, predict a sensor signal, and read a drive's datasheet.

**Prerequisites:** [Electricity and magnetism](06-electricity-and-magnetism.md), [Circuit basics](../applications/electronics/01-circuit-basics.md), [Differential equations](../math/06-differential-equations.md)
**Time:** 14-18 h

## Core ideas

### Nomenclature and the two laws

- A **node** is a point where two or more parts join. A **branch** is one part, or one series string of parts, between two nodes. A **loop** is any closed path through branches that visits no node twice. A **mesh** is a loop that contains no other loop.
- **Current** ($i$) is charge per unit time through a branch, in amperes (A). **Voltage** ($v$) is the energy per unit charge between two nodes, in volts (V). A voltage is always the difference between two nodes, so its polarity (+ and - marks) must be stated.
- The **passive sign convention** assigns the reference current into the + terminal of a part. Then $p = v i$ is the power absorbed by the part, and a negative $p$ means the part delivers power.
- **Kirchhoff's current law (KCL)**: the currents leaving a node sum to zero, because charge does not accumulate at a node. **Kirchhoff's voltage law (KVL)**: the voltages around any closed loop sum to zero, because the electric field of a lumped circuit is conservative.
- An **ideal voltage source** holds its terminal voltage whatever current it supplies. An **ideal current source** forces its current whatever voltage appears across it. Real sources add a series or parallel resistance.
- A **dependent (controlled) source** is a source whose value is set by a voltage or current elsewhere in the circuit. The four types are the voltage-controlled voltage source (VCVS), the current-controlled voltage source (CCVS), the voltage-controlled current source (VCCS), and the current-controlled current source (CCCS). They model transistors and amplifiers.
- A circuit is **linear** when every part obeys a straight-line law (resistors, capacitors, inductors, and sources that are constant or proportional to a circuit variable). Every method below, except the time-domain solutions of nonlinear parts, relies on linearity.

### Element laws

- A **resistor** obeys Ohm's law, $v = i R$. A **capacitor** stores charge: $i = C\,dv/dt$, so its voltage cannot jump. An **inductor** stores magnetic flux: $v = L\,di/dt$, so its current cannot jump.
- Resistors in series add. Resistors in parallel add as conductances ($G = 1/R$). A **voltage divider** splits a voltage in proportion to resistance, and a **current divider** splits a current in proportion to conductance.

### Node-voltage analysis

The **node-voltage method** chooses one node as ground (0 V), writes KCL at every other node with each branch current expressed through node voltages, and solves the linear equations. It needs one equation per non-ground node, so it is the better choice when nodes are fewer than meshes or when current sources are present. A voltage source between two non-ground nodes joins them into a **supernode**: write one KCL around the pair and add the source's constraint as the second equation.

### Mesh-current analysis

The **mesh-current method** assigns a circulating current to each mesh, writes KVL around each mesh, and solves. It is the better choice when meshes are fewer than nodes or when voltage sources are present. A current source shared by two meshes joins them into a **supermesh**; a current source on the outer edge of one mesh simply fixes that mesh current.

### Superposition and source transformation

- **Superposition** states that in a linear circuit the response to several independent sources equals the sum of the responses to each source acting alone. To find one source's effect, replace every other independent voltage source with a short circuit and every independent current source with an open circuit. Dependent sources stay in. Superposition adds voltages and currents, never power, because power is quadratic.
- **Source transformation** replaces a voltage source $V_s$ in series with $R$ by a current source $V_s/R$ in parallel with $R$, and the reverse. The two have the same terminal behaviour but not the same internal dissipation. It simplifies a network without writing equations.

### Thevenin and Norton equivalents

Any linear two-terminal network is equivalent, as seen from its terminals, to a single voltage source in series with a resistance (**Thevenin equivalent**) or a single current source in parallel with a resistance (**Norton equivalent**). The Thevenin voltage $V_{th}$ is the open-circuit voltage. The Norton current $I_N$ is the short-circuit current. The resistance $R_{th}$ is the same in both.

- With only independent sources, set them to zero (short voltage sources, open current sources) and find the resistance between the terminals.
- With dependent sources, do not zero them. Find $V_{oc}$ and $I_{sc}$ and divide, or attach a test source and compute $v_{test}/i_{test}$.

### Maximum power transfer

A load $R_L$ on a Thevenin source receives the most power when $R_L = R_{th}$. At that match the efficiency of the source is only 50 percent, since half the power is lost in $R_{th}$. Power systems therefore keep $R_L \gg R_{th}$ and accept low-power signals only where efficiency does not matter (sensors, antennas).

### Ideal op amp as a circuit element

An **operational amplifier (op amp)** is a high-gain differential amplifier. The **ideal op amp** has infinite open-loop gain, infinite input resistance, and zero output resistance. With negative feedback this gives two rules for analysis:

1. No current flows into either input.
2. The inverting and non-inverting inputs sit at the same voltage (the **virtual short**).

Apply KCL at the inverting input with those rules and the closed-loop gain follows. The output cannot exceed the supply rails (**saturation**), and a real op amp has a finite gain-bandwidth product, so the ideal model fails when the signal is fast or the output hits a rail. See [RC circuits and op-amp basics](../applications/electronics/02-rc-circuits-and-op-amps.md) for the inverting amplifier in use.

### Natural and complete response

- The **natural response** is the behaviour of a circuit with no sources, driven only by energy stored in capacitors and inductors. The **forced response** is the part that follows the sources. The **complete response** is their sum, and it is the solution of the circuit's differential equation with the stored initial energy.
- A first-order circuit (one energy-storing part) has a **time constant** ($\tau$) with units of seconds: $RC$ for a capacitor, $L/R$ for an inductor, where $R$ is the Thevenin resistance seen by the storage part. After one time constant a response has covered about 63 percent of its change, and after five it is within 1 percent of final.
- A second-order circuit (an inductor and a capacitor) rings or creeps depending on its **damping**. The **neper frequency** ($\alpha$) measures the decay and the **resonant frequency** ($\omega_0$) is the undamped oscillation rate. If $\alpha > \omega_0$ the response is **overdamped** (two real decays); if $\alpha = \omega_0$ it is **critically damped**; if $\alpha < \omega_0$ it is **underdamped** (a decaying sinusoid at the **damped frequency** $\omega_d$).

A series RLC circuit is the electrical twin of a mass-spring-damper from [Vibrations](13-vibrations.md): inductance plays mass, resistance plays the damper, and the inverse of capacitance plays the spring. Everything learned there about damping ratio and overshoot carries over.

## Key equations

Symbols: $v$ = voltage (V), $i$ = current (A), $R$ = resistance ($\Omega$), $G$ = conductance (S, equal to $1/R$), $C$ = capacitance (F), $L$ = inductance (H), $p$ = power (W), $t$ = time (s). Dimensionally, $\text{F} = \text{s}/\Omega$ and $\text{H} = \Omega\,\text{s}$.

Element laws and power, holding for linear parts with the passive sign convention:

$$
v = iR, \qquad i = C\frac{dv}{dt}, \qquad v = L\frac{di}{dt}, \qquad p = vi
$$

KCL and KVL, holding when the circuit is lumped (its size is much smaller than the wavelength of its signals):

$$
\sum i_{\text{leaving node}} = 0, \qquad \sum v_{\text{around loop}} = 0
$$

Node-voltage and mesh-current systems for a resistive network, where $\mathbf{G}$ is the conductance matrix ($S$), $\mathbf{v}$ the node voltages (V), $\mathbf{i}_s$ the source currents into each node (A), $\mathbf{R}$ the resistance matrix ($\Omega$), $\mathbf{i}_m$ the mesh currents (A), and $\mathbf{v}_s$ the source voltages around each mesh (V):

$$
\mathbf{G}\,\mathbf{v} = \mathbf{i}_s, \qquad \mathbf{R}\,\mathbf{i}_m = \mathbf{v}_s
$$

Thevenin and Norton equivalents, holding for any linear two-terminal network:

$$
V_{th} = v_{oc}, \qquad I_N = i_{sc}, \qquad R_{th} = \frac{v_{oc}}{i_{sc}}, \qquad V_{th} = I_N R_{th}
$$

Maximum power to a load of resistance $R_L$, reaching its peak at $R_L = R_{th}$ and breaking when the source is not linear or $R_{th}$ cannot be matched:

$$
P_L = \frac{V_{th}^2 R_L}{(R_{th}+R_L)^2}, \qquad P_{max} = \frac{V_{th}^2}{4R_{th}}
$$

Ideal op amp gains, holding with negative feedback and an output below the rails ($R_{in}$ and $R_f$ are the input and feedback resistances, and $R_g$ is the resistor from the inverting input to ground):

$$
\frac{v_{out}}{v_{in}} = -\frac{R_f}{R_{in}} \ \text{(inverting)}, \qquad \frac{v_{out}}{v_{in}} = 1 + \frac{R_f}{R_g} \ \text{(non-inverting)}
$$

First-order response of any capacitor voltage or inductor current $x$, with initial value $x(0)$, final value $x(\infty)$, and time constant $\tau$ (s):

$$
x(t) = x(\infty) + \bigl[x(0) - x(\infty)\bigr]e^{-t/\tau}, \qquad \tau_{RC} = RC, \qquad \tau_{RL} = \frac{L}{R}
$$

Series RLC, with a step source $V_s$ applied to an initially relaxed circuit. The constants have units of 1/s:

$$
\alpha = \frac{R}{2L}, \qquad \omega_0 = \frac{1}{\sqrt{LC}}, \qquad \omega_d = \sqrt{\omega_0^2 - \alpha^2}, \qquad \zeta = \frac{\alpha}{\omega_0}
$$

The capacitor voltage for $\alpha < \omega_0$, and the overshoot above the final value as a fraction of the step:

$$
v_C(t) = V_s\left[1 - e^{-\alpha t}\left(\cos\omega_d t + \frac{\alpha}{\omega_d}\sin\omega_d t\right)\right], \qquad \text{OS} = e^{-\pi\alpha/\omega_d}
$$

For the overdamped case the roots are $s = -\alpha \pm \sqrt{\alpha^2 - \omega_0^2}$. Critical damping occurs at $R = 2\sqrt{L/C}$. For a parallel RLC, replace $\alpha$ with $1/(2RC)$ and keep $\omega_0$.

> [!NOTE]
> Every closed-form response here assumes constant $R$, $L$, and $C$. An iron-core inductor that saturates, or a capacitor whose value changes with voltage, makes the circuit nonlinear and these formulas wrong.

## Worked example

### Thevenin equivalent and maximum power

A 24 V source drives a 6 $\Omega$ resistor in series, then a 12 $\Omega$ resistor to ground. A load is connected across the 12 $\Omega$ resistor.

**Given:** $V_s = 24$ V, $R_1 = 6\ \Omega$, $R_2 = 12\ \Omega$.

**Find:** The Thevenin equivalent seen by the load, the load that receives the most power, that power, and the power at $R_L = 8\ \Omega$.

**Assumptions:** Ideal source, linear resistors, steady direct current.

**Solution:**

1. Remove the load. The open-circuit voltage is the divider output, $V_{th} = V_s R_2/(R_1+R_2) = 16$ V.
2. Zero the source (short it). The resistance seen is $R_1$ in parallel with $R_2$, so $R_{th} = R_1 R_2/(R_1+R_2) = 4\ \Omega$.
3. Maximum power occurs at $R_L = R_{th} = 4\ \Omega$, with $P_{max} = V_{th}^2/(4R_{th}) = 16$ W.
4. At $R_L = 8\ \Omega$ the current is $I = V_{th}/(R_{th}+R_L) = 1.333$ A, and the load power is $I^2 R_L = 14.22$ W.

**Answer:** $V_{th} = 16$ V and $R_{th} = 4\ \Omega$. The best load is 4 $\Omega$, receiving 16.0 W. An 8 $\Omega$ load receives 14.2 W.

**Sanity check:** The 8 $\Omega$ load is off the match, so it must receive less than $P_{max}$, and 14.2 W is below 16.0 W. The short-circuit current is $V_{th}/R_{th} = 4$ A, which equals $24/6$ because a short across the 12 $\Omega$ resistor leaves only the 6 $\Omega$ resistor, so the two routes agree.

<details><summary>Verification</summary>

```verify
Vs = q(24, "V")
R1 = q(6, "ohm")
R2 = q(12, "ohm")
RL = q(8, "ohm")
Vth = Vs * R2 / (R1 + R2)
Rth = R1 * R2 / (R1 + R2)
expect(Vth, "16 V")
expect(Rth, "4 ohm")
Pmax = Vth**2 / (4 * Rth)
expect(Pmax, "16.0 W")
I = Vth / (Rth + RL)
expect(I, "1.333 A")
expect(I**2 * RL, "14.22 W")
expect(I**2 * RL, "14.2 W")
expect(Vth / Rth, "4 A")
expect(Vs / R1, "4 A")
check(I**2 * RL < Pmax, "off-match power is below the maximum")
```

</details>

### Series RLC step response

A relaxed series RLC circuit has $R = 20\ \Omega$, $L = 0.10$ H, and $C = 100\ \mu\text{F}$, and a 12 V step is applied.

**Given:** $R = 20\ \Omega$, $L = 0.10$ H, $C = 100\ \mu\text{F}$, $V_s = 12$ V.

**Find:** The damping type, $\alpha$, $\omega_0$, $\omega_d$, the damping ratio, the critical resistance, the overshoot, and the time of the first peak.

**Assumptions:** Linear parts, ideal source, zero initial energy.

**Solution:**

1. $\alpha = R/(2L) = 100\ \text{s}^{-1}$.
2. $\omega_0 = 1/\sqrt{LC} = 316.2\ \text{rad/s}$, so $\alpha < \omega_0$ and the response is underdamped.
3. $\omega_d = \sqrt{\omega_0^2 - \alpha^2} = 300.0\ \text{rad/s}$, and $\zeta = \alpha/\omega_0 = 0.316$.
4. Critical resistance: $2\sqrt{L/C} = 63.25\ \Omega$. The circuit's 20 $\Omega$ is below that, which agrees with underdamping.
5. Overshoot: $e^{-\pi\alpha/\omega_d} = 0.351$, so the capacitor peaks at 35.1 percent above 12 V.
6. The first peak is at $t = \pi/\omega_d = 10.47$ ms.

**Answer:** Underdamped with $\alpha = 100\ \text{s}^{-1}$, $\omega_0 = 316.2$ rad/s, $\omega_d = 300.0$ rad/s, $\zeta = 0.316$, overshoot 35.1 percent (the capacitor reaches about 16.2 V), peak at 10.47 ms.

**Sanity check:** A damping ratio well below one makes a mass-spring-damper overshoot by roughly a third, which matches the 35.1 percent. The peak time $\pi/\omega_d$ is half a damped period, and the damped period $2\pi/300 = 20.9$ ms is close to the undamped $2\pi/316.2 = 19.9$ ms.

<details><summary>Verification</summary>

```verify
R = q(20, "ohm")
L = q(0.10, "ohm s")
C = q(100, "us/ohm")
Vs = q(12, "V")
alpha = R / (2 * L)
expect(alpha, "100 1/s")
w0 = 1 / sqrt(L * C)
expect(w0, "316.2 1/s")
wd = sqrt(w0**2 - alpha**2)
expect(wd, "300.0 1/s")
expect(alpha / w0, "0.316")
Rcrit = 2 * sqrt(L / C)
expect(Rcrit, "63.25 ohm")
OS = exp(-pi * alpha / wd)
expect(OS, "0.351")
expect(OS * 100, "35.1")
expect(Vs * (1 + OS), "16.2 V")
tp = pi / wd
expect(tp, "10.47 ms")
expect(2 * pi / wd, "20.9 ms")
expect(2 * pi / w0, "19.9 ms")
check(alpha < w0, "underdamped")
check(R < Rcrit, "below critical resistance")
```

</details>

## Practice

1. A 2 k$\Omega$ resistor charges a 100 $\mu$F capacitor from a 12 V source, starting at 0 V. Find the time for the capacitor to reach 9 V, in s.
2. A 50 mH inductor with 25 $\Omega$ in series is connected to a 10 V source at $t = 0$, starting with no current. Find the current at $t = 3$ ms, in A.
3. A 10 V source in series with 2 $\Omega$ feeds a node. From that node a 4 $\Omega$ resistor goes to ground, and a 3 A current source pushes current into the node. Find the node voltage in V by any method, then check it a second way.
4. An ideal inverting amplifier has $R_{in} = 10\ \text{k}\Omega$ and $R_f = 47\ \text{k}\Omega$. Find the output voltage for a 0.50 V input, in V, and the output for a non-inverting amplifier with the same two resistors ($R_f$ the feedback, 10 k$\Omega$ to ground) and the same input.
5. Two meshes share a 3 $\Omega$ resistor. Mesh 1 holds a 10 V source and a 5 $\Omega$ resistor. Mesh 2 holds a 2 $\Omega$ resistor and a dependent voltage source that drops $2 i_x$ volts in the direction of $i_2$, where $i_x = i_1$ is the current in the 5 $\Omega$ resistor. Find $i_2$ in A.

<details><summary>Answers</summary>

1. 0.277 s
2. 0.311 A
3. 10.67 V (superposition: 6.667 V from the voltage source plus 4.000 V from the current source)
4. -2.35 V, and +2.85 V
5. 0.270 A (mesh 1 gives $8i_1 - 3i_2 = 10$; mesh 2 gives $-i_1 + 5i_2 = 0$)

```verify
tau = q(2, "kohm") * q(100, "us/ohm")
expect(-tau * log(1 - q(9, "V") / q(12, "V")), "0.277 s", ans=1)
Itot = q(10, "V") / q(25, "ohm")
tau2 = q(50, "mohm s") / q(25, "ohm")
expect(Itot * (1 - exp(-q(3, "ms") / tau2)), "0.311 A", ans=2)
Va = q(10, "V")
R1 = q(2, "ohm")
R2 = q(4, "ohm")
Is = q(3, "A")
v = (Va / R1 + Is) / (1 / R1 + 1 / R2)
expect(v, "10.67 V", ans=3)
v_from_vs = Va * R2 / (R1 + R2)
v_from_is = Is * R1 * R2 / (R1 + R2)
expect(v_from_vs, "6.667 V", ans=3)
expect(v_from_is, "4.000 V", ans=3)
vin = q(0.50, "V")
Rf = q(47, "kohm")
Rg = q(10, "kohm")
expect(-Rf / Rg * vin, "-2.35 V", ans=4)
expect((1 + Rf / Rg) * vin, "2.85 V", ans=4)
r1 = q(5, "ohm")
r12 = q(3, "ohm")
r2 = q(2, "ohm")
rm = q(2, "ohm")
k = (r12 - rm) / (r12 + r2)
i1 = q(10, "V") / ((r1 + r12) - r12 * k)
expect(i1 * k, "0.270 A", ans=5)
```

</details>

## Common mistakes

- Writing a voltage without a polarity, or mixing the passive sign convention, so a source that delivers power is counted as absorbing it.
- Setting a source to zero wrongly in superposition or a Thevenin resistance: a voltage source becomes a short circuit, a current source becomes an open circuit, and a dependent source is never zeroed.
- Adding powers from superposition. Voltages and currents add; powers do not.
- Assuming maximum power transfer means maximum efficiency. At the matched load, half the power is lost in the source resistance.
- Applying the ideal op amp rules with the output at a rail, or without negative feedback. The virtual short holds only when feedback keeps the amplifier in its linear range.
- Using the wrong time constant for a first-order circuit with more than one resistor: $R$ must be the Thevenin resistance seen by the capacitor or inductor.

## Go deeper

- [Circuits and Electronics (6.002)](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/) by MIT OpenCourseWare: a free course covering resistive circuits, Thevenin and Norton equivalents, op amps, and first- and second-order transients.
- [University Physics Volume 2, chapter 10 (Direct-current circuits)](https://openstax.org/books/university-physics-volume-2/pages/10-introduction) by OpenStax: free chapters on Kirchhoff's rules and RC circuits.
- Next: [AC circuits, phasors, and power](17-ac-circuits-phasors-and-power.md) extends these methods to sinusoidal sources.
- Related: [Electricity and magnetism](06-electricity-and-magnetism.md), [Vibrations](13-vibrations.md), [Controls](14-controls.md).
- [Fields, waves, and space reference](reference-fields-waves-space.md): the lookup sheet that includes circuit laws and electromagnetism.
