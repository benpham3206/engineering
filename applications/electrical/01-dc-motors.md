# DC motors

**Type:** lesson

A DC motor is a machine that turns electrical energy into rotation with a simple rule. Engineers choose DC motors when they need simple speed and torque control, and they must understand the brushes and commutator because those set the motor's wear, noise, and limits. Current in a conductor inside a magnetic field feels a force, and a commutator keeps that force pointing the same way as the rotor turns.

**Prerequisites:** [Electricity and magnetism](../../physics/06-electricity-and-magnetism.md), [Circuit basics](../electronics/01-circuit-basics.md), [Mechatronics](../electronics/06-mechatronics.md)
**Time:** 6-8 h

## Core ideas

### How it works

1. The stator sets up a magnetic field. In a permanent magnet motor, this is a fixed magnet. In a wound-field motor, a coil carries current to make the field.
2. The rotor, also called the armature, is a laminated iron core with coils wound in slots. Each coil connects to two segments of the commutator.
3. Current flows through the armature coils from the brushes. A conductor carrying current $I$ in a field $B$ feels a force $F = B I \ell$, where $\ell$ is the length of conductor in the field (m). The forces on the coils make a torque about the shaft.
4. As the rotor turns, the commutator segments pass under the brushes and reverse the current in each coil about every half turn. The torque stays in the same direction.
5. A turning coil also cuts the magnetic flux. That motion generates a voltage called back-EMF, which opposes the supply. The rotor speeds up until the back-EMF plus the resistive drop equals the supply voltage. At that speed, the net driving voltage is small and the current settles at the level the load needs.

The steady-state balance is $V = I R + K_e \omega$. The robot arm lesson states this relation and uses it for speed and stall calculations, so this lesson uses it without repeating that material.

### Main parts

- **Stator (field)**: the part that makes the magnetic field. Permanent magnets are common in small motors, such as those in tools and car window lifts. Large industrial motors use wound field coils.
- **Armature (rotor)**: a laminated steel core with copper coils. Laminations reduce eddy-current losses.
- **Commutator**: a ring of copper segments on the shaft. Each segment is insulated from the others and connected to one coil terminal.
- **Brushes**: blocks of carbon or graphite pressed against the commutator by springs. They carry current into the rotor. Brushes wear and must be replaced.
- **Bearings, shaft, and housing**: they hold the rotor, carry the load, and set the air gap.

### Variants

- **Permanent magnet DC (PMDC)**: the most common small motor. Its torque constant is fixed by the magnet strength, so the motor is simple to control.
- **Shunt-wound**: the field coil is connected in parallel with the armature. Speed stays close to constant as load changes.
- **Series-wound**: the field coil carries the armature current. Torque rises with the square of current at low speed, so the starting torque is high. With no load, the speed can climb dangerously high, so a series motor must always drive a load.
- **Compound**: a series field added to a shunt field. It mixes the starting torque of a series motor with the steadier speed of a shunt motor.
- **Universal motor**: a series-wound motor that runs on AC or DC. Drills, blenders, and vacuum cleaners often use one because a series field works with either polarity.

## Key equations

The armature voltage balance, the torque relation, and the speed formula are the same for every brushed DC motor in this lesson. In SI units:

$$V = I R + K_e \omega \qquad T = K_t I \qquad \omega = \frac{V - I R}{K_e}$$

where $V$ is the armature supply voltage (V), $I$ is the armature current (A), $R$ is the armature resistance ($\Omega$), $\omega$ is the shaft speed (rad/s), $T$ is the electromagnetic torque (N m), $K_e$ is the back-EMF constant (V s/rad), and $K_t$ is the torque constant (N m/A).

The two constants come from the motor's construction:

$$K_t = K_e = \frac{Z\, p\, \Phi}{\pi a}$$

Here $Z$ is the number of armature conductors (dimensionless), $p$ is the number of pole pairs (dimensionless), $\Phi$ is the magnetic flux per pole (Wb, which equals V s), and $a$ is the number of parallel current paths in the armature (dimensionless). The units check: V s divided by rad equals N m/A. Because the two constants share one flux term, a motor with a weaker field has a lower $K_e$ and a lower $K_t$.

Power and losses:

$$P_{\mathrm{elec}} = V I \qquad P_{\mathrm{mech}} = T \omega \qquad P_{\mathrm{cu}} = I^2 R$$

where $P_{\mathrm{elec}}$ is the electrical input power (W), $P_{\mathrm{mech}}$ is the mechanical power (W), and $P_{\mathrm{cu}}$ is the copper loss (W). The efficiency is $\eta = P_{\mathrm{mech}} / P_{\mathrm{elec}}$, dimensionless.

Field weakening changes the flux. When $\Phi$ falls, $K_e$ falls in proportion, and the ideal no-load speed $V / K_e$ rises. The same current then produces less torque.

## Worked example

**Given:** A permanent magnet DC motor runs from $V = 24\ \text{V}$. Its armature resistance is $R = 0.80\ \Omega$, and its constants are $K_t = K_e = 0.030$ in SI units (N m/A and V s/rad). Friction and windage take $T_f = 0.010\ \text{N m}$. The load is $T_L = 0.120\ \text{N m}$.

**Find:** (a) the stall current and stall torque, (b) the running speed at the load in rad/s and rpm, (c) the efficiency at the load, and (d) the average PWM duty cycle that holds the speed at $300\ \text{rad/s}$ with the same load.

**Solution:**

1. Stall current: $I_{\mathrm{stall}} = V / R = 24 / 0.80 = 30.0\ \text{A}$. Stall torque: $T_{\mathrm{stall}} = K_t I_{\mathrm{stall}} = 0.030 \times 30.0 = 0.90\ \text{N m}$.
2. Total torque the motor must make: $T = T_L + T_f = 0.120 + 0.010 = 0.130\ \text{N m}$. Current: $I = T / K_t = 0.130 / 0.030 = 4.33\ \text{A}$. Speed: $\omega = (V - I R) / K_e = (24 - 4.33 \times 0.80) / 0.030 = (24 - 3.47) / 0.030 = 684\ \text{rad/s}$. In rpm, $684 \times 60 / (2\pi) = 6536\ \text{rpm}$.
3. Electrical input: $P_{\mathrm{elec}} = 24 \times 4.33 = 104.0\ \text{W}$. Copper loss: $I^2 R = 4.33^2 \times 0.80 = 15.0\ \text{W}$. Friction loss: $T_f \omega = 0.010 \times 684 = 6.8\ \text{W}$. Output power at the load: $T_L \omega = 0.120 \times 684 = 82.1\ \text{W}$. Efficiency: $82.1 / 104.0 = 0.79$, or 79 percent.
4. PWM target: at $\omega = 300\ \text{rad/s}$, the current is still $I = 4.33\ \text{A}$ because the torque is unchanged. Back-EMF: $K_e \omega = 0.030 \times 300 = 9.00\ \text{V}$. Required average voltage: $V_{\mathrm{avg}} = I R + K_e \omega = 4.33 \times 0.80 + 9.00 = 3.47 + 9.00 = 12.47\ \text{V}$. Duty cycle: $D = V_{\mathrm{avg}} / V = 12.47 / 24 = 0.52$, or 52 percent.

**Answer:** (a) $I_{\mathrm{stall}} = 30.0\ \text{A}$ and $T_{\mathrm{stall}} = 0.90\ \text{N m}$. (b) $\omega = 684\ \text{rad/s}$, which is $6536\ \text{rpm}$. (c) $79$ percent. (d) $D \approx 0.52$.

**Sanity check:** The losses close the power balance: $104.0 - 15.0 - 6.8 = 82.2\ \text{W}$, which matches $82.1\ \text{W}$ within rounding. The stall current of 30 A is about 7 times the running current of 4.3 A, which is why a motor driver must limit current at start-up. A duty cycle of 52 percent gives a 12.5 V average, and the motor sees that average only if its winding inductance smooths the switching pulses, as the mechatronics lesson describes.

## Design trade-offs

- **Brushes versus life**: brushes wear with every revolution. Carbon brushes in small motors often last from a few hundred to a few thousand hours (typical), and the commutator surface must stay smooth to keep the brush contact steady.
- **Efficiency**: small brushed motors are often 60 to 80 percent efficient (typical). Brush contact drop, copper loss, and friction all reduce it. Brushless motors reach higher efficiency because they have no brush loss.
- **Noise and EMI**: sparking at the brushes produces electrical noise. Suppression capacitors and diodes reduce it, and sparking limits the usable brush current.
- **Size and torque**: torque per volume depends on flux density and winding fill. Strong permanent magnets such as neodymium improve it.
- **Speed range**: a PMDC motor's torque constant is fixed, so speed control uses voltage. Field weakening extends the top speed at the cost of torque.
- **Starting current**: a 24 V motor with 0.8 ohm armature resistance draws 30 A at stall. The driver, wiring, and supply must handle that peak or limit it.

## How it fails

- **Brush wear and dust**: worn brushes reduce contact, raise resistance, and leave carbon dust that can short the commutator. Warning signs are rising noise, sparking, and intermittent output.
- **Commutator flashover**: when segments see too much voltage between them, an arc can run across the commutator and damage it. Overvoltage and dirt both raise the risk.
- **Overheating at stall**: a stalled rotor draws stall current, and $I^2 R$ heat builds in seconds. Thermal cutouts, current limits, and stall detection protect the winding.
- **Demagnetization**: permanent magnets lose strength above their rated temperature, which lowers $K_t$ and $K_e$ together and changes the speed-torque curve.
- **Series motor runaway**: without a load, a series motor can accelerate until it is destroyed. Designs use a minimum load or a speed limit.
- **Bearing failure**: bearings are a common end of life for every rotating machine. Misalignment and lack of lubrication shorten their life.

## History

Michael Faraday showed continuous rotation from electromagnetic force in London in 1821, which is the first step toward a motor. In the early 1830s, William Sturgeon in England built a motor with a commutator. Thomas Davenport in the United States received a patent for a DC motor in 1837. In the 1830s, Moritz von Jacobi in Russia built motors, and in 1838 he drove a boat with one on the Neva River in St. Petersburg. Practical DC motors then spread with the growth of electric power distribution in the late 19th century.

## Practice

1. A motor has $K_t = K_e = 0.020$ in SI units. The load torque is $0.050\ \text{N m}$, and friction is ignored. Find the armature current.
2. A 12 V motor has $K_e = 0.020\ \text{V s/rad}$, and friction is ignored. Find its ideal no-load speed in rad/s and in rpm.
3. A 24 V motor has $R = 2.0\ \Omega$ and $K_t = 0.050\ \text{N m/A}$. Find its stall current and stall torque.
4. A 6 V motor has $R = 1.0\ \Omega$ and $K_e = 0.010\ \text{V s/rad}$. It runs at $300\ \text{rad/s}$. Find its armature current.
5. A motor at 12 V runs at an ideal no-load speed of $1000\ \text{rad/s}$. Field weakening halves the flux. Find the new ideal no-load speed at 12 V.

<details><summary>Answers</summary>

1. $I = T / K_t = 0.050 / 0.020 = 2.5\ \text{A}$.
2. $\omega = V / K_e = 12 / 0.020 = 600\ \text{rad/s}$, which is $5730\ \text{rpm}$.
3. $I_{\mathrm{stall}} = 24 / 2.0 = 12\ \text{A}$, and $T_{\mathrm{stall}} = 0.050 \times 12 = 0.60\ \text{N m}$.
4. $I = (6 - 0.010 \times 300) / 1.0 = 3\ \text{A}$.
5. Flux halves, so $K_e$ halves to $0.0060\ \text{V s/rad}$. The ideal no-load speed is $\omega = 12 / 0.0060 = 2000\ \text{rad/s}$.

</details>

## Common mistakes

- Using $V / R$ as the running current. That gives the stall current, which is far too high once the rotor turns. Subtract back-EMF first.
- Mixing up $K_t$ and $K_e$. Torque uses $K_t$ with current, and speed uses $K_e$ with voltage. In SI, the numbers match only because both come from the same flux.
- Ignoring the brush voltage drop. Carbon brushes often drop about 1 to 2 V (typical), which matters for a 6 V or 12 V motor.
- Treating a PWM average as a steady supply. The motor sees the average only if its inductance smooths the pulses. High-frequency switching keeps that smoothing close to ideal.
- Driving a series motor with no load. It can overspeed and fail.

## Go deeper

- [Circuits and Electronics (6.002), MIT OpenCourseWare](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/) by MIT: circuit models and power electronics for motor drives.
- [University Physics Volume 2, Chapter 13 (Electromagnetic Induction)](https://openstax.org/books/university-physics-volume-2/pages/13-introduction) by OpenStax: Faraday's law and the back-EMF that opposes a motor's supply.
- [Electric Motors](https://www.energy.gov/eere/buildings/electric-motors) by the U.S. Department of Energy: the federal efficiency standards and test rules for motors.
- Related lessons: [Robot arms](../machines-robots/01-robot-arms.md) uses the same DC motor torque and speed relations to drive joints. Next: [Brushless and stepper motors](02-brushless-and-stepper-motors.md).
- [Applications reference](../reference.md): the lookup sheet for this topic.
