# RC circuits and op-amp basics

**Type:** lesson

An **RC circuit** is a resistor and a capacitor working together. Its voltage changes over time along an exponential curve. An op-amp is a small amplifier chip that, with two resistors, sets its
gain. Engineers use RC circuits for timing, filtering, and smoothing, and op-amps for
sensor signal conditioning.

**Prerequisites:** [Circuit basics](01-circuit-basics.md), [Algebra](../../math/01-algebra.md)
**Time:** 8-12 h

## Core ideas

- **Capacitor**: a part that stores charge and voltage. Its voltage cannot change instantly.
  The capacitance $C$ is measured in farads (F). Typical bench values are microfarads ($\mu$F).
- **Charging**: when a voltage is applied through a resistor, current flows into the capacitor
  and its voltage rises gradually.
- **Time constant** $\tau$ (tau): the product $RC$. After one time constant, a charging capacitor
  reaches about 63 percent of its final voltage.
- **Discharging**: a charged capacitor left across a resistor loses its voltage in the same
  exponential shape.
- **Op-amp** (operational amplifier): a three-terminal amplifier with two inputs and one output.
  Its output tries to make the two input voltages equal, which is the basis of its behavior.
- **Ideal op-amp assumptions**: infinite input resistance, zero output resistance, and infinite open
  loop gain. These are good enough for most first designs, as long as there is negative feedback.
- **Inverting amplifier**: the signal goes into the minus input through a resistor $R_{\mathrm{in}}$, and a
  feedback resistor $R_f$ connects the output back to the minus input. The gain is
  $-R_f / R_{\mathrm{in}}$. The minus sign means the output is flipped in polarity.

## Key equations

- Time constant: $\tau = R C$, where $R$ is ohms ($\Omega$), $C$ is farads (F), and $\tau$ is seconds.
- Charging from zero to $V_s$ through $R$: $V_C(t) = V_s \left(1 - e^{-t/\tau}\right)$.
- Time to reach a voltage $V_x$ when charging from zero: $t = -\tau \ln\left(1 - \dfrac{V_x}{V_s}\right)$.
- Inverting amplifier gain: $A_v = -\dfrac{R_f}{R_{\mathrm{in}}}$ (dimensionless).
- Output voltage: $V_{\mathrm{out}} = A_v V_{\mathrm{in}}$.

## Worked example

**Given:** A $10\ \text{k}\Omega$ resistor is in series with a $47\ \mu\text{F}$ capacitor. A $5\ \text{V}$
step is applied at $t = 0$, with the capacitor starting at $0\ \text{V}$.

**Find:** (a) the capacitor voltage at $t = 1\ \text{s}$, and (b) the time to reach $2.5\ \text{V}$.

**Solution:**

1. Time constant: $\tau = RC = 10\,000 \times 47\times10^{-6} = 0.47\ \text{s}$.
2. (a) $V_C(1) = 5\left(1 - e^{-1/0.47}\right) = 5\left(1 - 0.119\right) = 4.40\ \text{V}$.
3. (b) Solve for $t$ when $V_C = 2.5\ \text{V}$, which is half of $V_s$:
   $t = -0.47 \ln(1 - 0.5) = -0.47 \times (-0.693) = 0.326\ \text{s}$.

**Answer:** (a) $4.40\ \text{V}$ at $1\ \text{s}$. (b) $0.326\ \text{s}$.

**Sanity check:** $1\ \text{s}$ is about $2\tau$. At $2\tau$ the capacitor should be about 86 percent of the
way to 5 V, and $0.86 \times 5 = 4.3\ \text{V}$, close to $4.40\ \text{V}$. Half of the final voltage
is reached in roughly $0.7\tau$, and $0.326 / 0.47 = 0.69$, which agrees.

## How it fails

- **Capacitor overvoltage and reversed polarity.** A capacitor driven above its voltage rating breaks down and shorts, and a polarized electrolytic connected backward heats and can vent or burst. The signs are bulging or leaking cases. Derate to about 50 to 80 percent of the rated voltage, and check polarity before power-up.
- **Electrolytic aging.** The electrolyte dries out with heat and time, so capacitance falls and equivalent series resistance rises. The sign is ripple, a timing circuit running off its design value, or a capacitor that runs warm. Keep capacitors away from heat and use parts rated for the temperature.
- **Shorted capacitor.** A shorted capacitor passes the full supply current. A fuse or current limit stops the failure from spreading, and a series resistor limits inrush current into a discharged capacitor.
- **Component tolerance and drift.** Resistor and capacitor values vary with tolerance, temperature, and age, so the time constant $\tau = RC$ drifts. Use tighter tolerance or stable dielectrics (film or C0G) where timing matters.
- **Op-amp saturation.** The output cannot go beyond the supply rails. When the gain times the input exceeds the rails, the output clips. The sign is a flat-topped waveform. Reduce the gain, check the input range, and pick an amplifier whose output reaches the rails you need.
- **Op-amp oscillation.** Capacitive loads, long input leads, and high gain can add phase lag so the feedback turns positive and the circuit rings or oscillates. The sign is a high-frequency buzz on the output. A small series resistor at the output, a small feedback capacitor, and a decoupling capacitor close to each supply pin prevent it.
- **Input offset and bias current.** A tiny input offset voltage or bias current times a large gain gives a large output error. The sign is a nonzero output with zero input. Use low-offset amplifiers or a trim.
- **Noise pickup and ground loops.** Two ground connections at different potentials drive current through a shared path and inject hum into small signals, and long high-impedance inputs pick up electromagnetic interference. Shielded twisted cable, a single-point ground, and short input leads reduce both.

> [!WARNING]
> **Charged capacitor shock.** A large capacitor stays charged after power-off. Eliminate the hazard by discharging it, add a bleeder resistor as an engineering control, and use procedures and PPE after that. Under lockout/tagout, isolate and lock the supply, discharge stored energy, and prove zero voltage with a meter before touching the circuit.

## Practice

1. Find $\tau$ for $R = 1\ \text{k}\Omega$ and $C = 100\ \mu\text{F}$.
2. An RC circuit with $\tau = 0.1\ \text{s}$ is charged from a $5\ \text{V}$ source. Find the voltage
   after one time constant.
3. An inverting amplifier has $R_{\mathrm{in}} = 4.7\ \text{k}\Omega$ and $R_f = 47\ \text{k}\Omega$. Find the gain.
4. Using the amplifier from problem 3, find $V_{\mathrm{out}}$ for $V_{\mathrm{in}} = 0.5\ \text{V}$.
5. How long does it take to reach $3\ \text{V}$ from zero in the RC circuit of problem 2, with a
   $5\ \text{V}$ source?

<details><summary>Answers</summary>

1. $0.1\ \text{s}$
2. $3.16\ \text{V}$
3. $-10$
4. $-5\ \text{V}$
5. $0.1 \times -\ln(1 - 0.6) = 0.092\ \text{s}$

</details>

## Common mistakes

- Using the time constant in the wrong units. Convert microfarads and kilo-ohms before you multiply.
- Forgetting the minus sign in an inverting amplifier. The output is flipped in polarity.
- Using the 63 percent rule for any voltage. It only applies to one time constant.
- Assuming the op-amp output can go beyond its supply rails. Real output swings are limited, often
  to within about a volt of the supply.
- Building an op-amp circuit without negative feedback. Without feedback, the output saturates.

## Go deeper

- [Circuits and Electronics (6.002), MIT OpenCourseWare](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/)
  by MIT: transient response and op-amp lectures with problem sets.
- [*Electronics*, Wikibooks](https://en.wikibooks.org/wiki/Electronics) by Wikibooks contributors: the
  transient analysis chapter covers RC circuits, and the chapter on operational amplifiers covers
  inverting amplifiers.
- [*University Physics Volume 2*, Chapter 10](https://openstax.org/books/university-physics-volume-2/pages/10-introduction)
  by OpenStax: resistors and circuit analysis, a good base before RC circuits.
- Previous: [Lesson 01, circuit basics](01-circuit-basics.md).
- Next: [Lesson 03, mechatronics](06-mechatronics.md).
- [Applications reference](../reference.md): the lookup sheet for this topic.
