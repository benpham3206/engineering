# Brushless and stepper motors

**Type:** lesson

Brushless DC (BLDC) and permanent magnet synchronous (PMSM) motors replace the brushes with electronic switching, which removes the main wear part of a brushed motor. Stepper motors move in fixed angular steps and can hold a position without a sensor. Engineers use these motors in drones, appliances, disk drives, 3D printers, and machine tools, so they need to understand how the drive electronics and the magnets work together.

**Prerequisites:** [Electricity and magnetism](../../physics/06-electricity-and-magnetism.md), [Mechatronics](../electronics/06-mechatronics.md), [DC motors](01-dc-motors.md)
**Time:** 8-10 h

## Core ideas

### How it works

A brushless motor has a permanent magnet rotor and a stator with several coils. The coils carry no brushes, so a controller must switch the current into each coil at the right moment. The controller needs to know the rotor angle, which it gets from Hall sensors or an encoder.

1. The rotor magnets set up a field that rotates with the shaft.
2. The inverter, a three-phase bridge of power transistors, sends current into two of the three stator coils at a time. The pair is chosen from the rotor angle.
3. The stator current creates its own field. The two fields pull on each other, and the rotor turns to line up with the stator field.
4. As the rotor reaches the next position, the controller switches the current to the next pair of coils, so the stator field keeps moving ahead of the rotor.

A BLDC motor with trapezoidal back-EMF uses six switching states per electrical cycle, each lasting 60 electrical degrees. A PMSM with sinusoidal back-EMF is driven with sinusoidal currents, usually by field-oriented control (FOC), which gives smoother torque.

A stepper motor works on a different principle. The stator has several poles, and each pole is energized in a sequence. The rotor, which is a toothed iron core or a magnet, steps to the nearest aligned position each time the energized pole changes. Without an encoder, the controller counts pulses and assumes the rotor has moved one step per pulse.

### Main parts

- **Stator coils**: copper windings around laminated steel. In a BLDC motor, they are usually three-phase. In a stepper, they form two or more independent phases.
- **Rotor magnets**: neodymium-iron-boron magnets are common in high-performance designs. Ferrite magnets are cheaper and weaker.
- **Position sensing**: three Hall sensors, a magnetic encoder, or an optical encoder. A stepper often has none, which is why its open-loop control is simple.
- **Inverter and gate drivers**: power MOSFETs or IGBTs switch the phases. Gate drivers turn them on and off quickly enough to make the switching efficient.
- **Controller**: a microcontroller or motor-control chip reads the sensors, computes the commutation or current, and sets the PWM duty cycles.
- **Stepper driver**: a current-regulated chopper that sets the winding current for each step and each microstep.

### Variants

- **Trapezoidal BLDC**: simple, low cost, and good for fans, pumps, and drones. Torque ripple is higher than with sinusoidal drive.
- **Sinusoidal PMSM with FOC**: smooth torque and high efficiency. Used in electric vehicles, servo drives, and industrial robots. The controller is more complex.
- **Hybrid stepper**: a toothed rotor with a permanent magnet and two phases. This is the most common stepper, with a 1.8 degree full step (typical) and a holding torque that grows with frame size.
- **Permanent magnet stepper**: a magnet rotor with simpler construction and lower torque per volume.
- **Variable reluctance stepper**: a toothed iron rotor with no magnet. It has the lowest torque per volume and is rare in new designs.

## Key equations

For a simplified model of a BLDC motor at steady speed, the terminal voltage balances the resistive drop and the back-EMF:

$$V \approx I R + K_e \omega \qquad T = K_t I$$

In SI, $K_t$ and $K_e$ have the same numerical value (N m/A and V s/rad). The symbols are the same as in the DC motor lesson: $V$ in volts, $I$ in amperes, $R$ in ohms, $\omega$ in rad/s, and $T$ in N m.

The electrical frequency that the drive must produce depends on the number of pole pairs. With $p$ pole pairs (dimensionless) and speed $n$ in rpm, the electrical frequency in hertz is:

$$f_e = \frac{p\, n}{60}$$

A motor with 4 pole pairs at 3000 rpm needs 200 Hz of electrical excitation, even though the shaft turns 50 times per second.

For a stepper, the full step angle is $\theta_s = 360 / N_s$ degrees, where $N_s$ is the number of full steps per revolution (dimensionless). With microstepping at $M$ divisions per full step, the microstep angle is $\theta_m = \theta_s / M$. The pulse rate that the driver needs at speed $n$ rpm is:

$$f_{pulse} = \frac{N_s\, M\, n}{60}$$

where $f_{pulse}$ is in pulses per second (Hz).

Efficiency and losses: $P_{elec} = V I$, $P_{mech} = T \omega$, $P_{cu} = I^2 R$, and $\eta = P_{mech} / P_{elec}$.

## Worked example

**Given:** A BLDC motor has $p = 4$ pole pairs. Its supply is $V = 24\ \text{V}$, its phase resistance in this simplified model is $R = 0.50\ \Omega$, and $K_t = K_e = 0.080$ in SI units. The load torque is $T = 0.30\ \text{N m}$.

**Find:** (a) the current, (b) the shaft speed in rpm, (c) the electrical frequency at that speed, (d) the mechanical output and electrical input power, and (e) the efficiency.

**Solution:**

1. Current: $I = T / K_t = 0.30 / 0.080 = 3.75\ \text{A}$.
2. Speed: $\omega = (V - I R) / K_e = (24 - 3.75 \times 0.50) / 0.080 = 276.6\ \text{rad/s}$. In rpm, $276.6 \times 60 / (2\pi) = 2641\ \text{rpm}$.
3. Electrical frequency: $f_e = 4 \times 2641 / 60 = 176\ \text{Hz}$.
4. Mechanical output: $P_{mech} = 0.30 \times 276.6 = 83.0\ \text{W}$. Electrical input: $P_{elec} = 24 \times 3.75 = 90.0\ \text{W}$.
5. Efficiency: $83.0 / 90.0 = 0.922$, or 92.2 percent.

**Answer:** (a) $I = 3.75\ \text{A}$. (b) $2641\ \text{rpm}$, which is $277\ \text{rad/s}$. (c) $176\ \text{Hz}$. (d) $P_{mech} = 83.0\ \text{W}$ and $P_{elec} = 90.0\ \text{W}$. (e) $92.2$ percent.

**Sanity check:** The losses close the balance: copper loss is $I^2 R = 3.75^2 \times 0.50 = 7.0\ \text{W}$, and $90.0 - 7.0 = 83.0\ \text{W}$. The efficiency of 92 percent is in the range of good BLDC drives (typical). The electrical frequency is four times the mechanical rotation frequency of 44 Hz, which matches $4 \times 2641 / 60$.

## Design trade-offs

- **Efficiency**: BLDC and PMSM motors often reach 85 to 95 percent (typical), higher than brushed motors of the same size, because they lose no power at brushes.
- **Cost**: the electronics, sensors, and magnets cost more than a brushed motor. A stepper is cheaper still, and it needs no sensor for simple positioning.
- **Torque at speed**: stepper torque falls as step rate rises, so a stepper suits low-speed positioning. A BLDC or PMSM keeps useful torque over a wider speed range.
- **Heat**: a stepper draws full holding current when it is still, so it can run hot. A BLDC draws little current at standstill with no load.
- **Precision**: an open-loop stepper is accurate to its step angle only if it does not miss steps. A BLDC with an encoder can track position closely and correct errors.
- **Magnet choice**: neodymium magnets give high torque per volume, but their strength falls at high temperature. Ferrite magnets are cheaper and need more volume for the same torque.
- **Microstepping**: finer steps give smoother motion and less vibration, but the holding torque and step accuracy do not improve in proportion, because the rotor position between full steps is less controlled.

## How it fails

- **Demagnetization of rotor magnets**: heat or a large reverse current can weaken the magnets. The motor then makes less torque for the same current, and the controller must draw more current to compensate.
- **Hall sensor misalignment**: if the sensors are placed or wired wrong, the controller switches at the wrong moment. The result is high torque ripple, noise, and loss of efficiency.
- **Missed steps in a stepper**: when the load torque exceeds what the rotor can hold at that step rate, the rotor loses step. The position is then wrong, and no sensor reports it.
- **Overheating from holding current**: a stepper held in position for a long time keeps its holding current on. Drivers reduce the current when the motor stops, which limits this heat.
- **Phase wiring errors**: swapping two phases reverses rotation or causes the motor to vibrate and fail to start.
- **Inverter failure**: a shoot-through fault, where both transistors in one leg conduct, shorts the supply. Dead-time settings and gate protection prevent it.
- **Back-EMF and regeneration**: when a braking load drives the motor, it can return energy to the supply. The bus voltage can rise, and a braking resistor or regeneration path protects the drive.

## History

Brushless motors became practical in the 1960s, when transistors could switch the phase currents electronically. Permanent magnet materials then improved, and neodymium-iron-boron magnets were developed by Sumitomo Special Metals in Japan in the early 1980s. Stepper motors spread in the 1970s and 1980s through floppy disk drives, printers, and early numerically controlled machines, where a pulse sent to the motor moved it one step. Modern servo drives combine these ideas with encoders and FOC.

## Practice

1. A stepper has 200 full steps per revolution and runs at 1 rev/s with 16 microsteps per full step. Find the pulse rate in microsteps per second.
2. A BLDC motor has 6 pole pairs and runs at 1000 rpm. Find its electrical frequency.
3. A 1.8 degree stepper runs at 1/8 microstepping. Find the microstep angle.
4. A BLDC motor with 4 pole pairs runs at 1500 rpm. Find its electrical frequency and the number of electrical cycles per shaft revolution.
5. A 0.9 degree stepper runs at 1/16 microstepping. Find the microstep angle.

<details><summary>Answers</summary>

1. $N_s M n / 60 = 200 \times 16 \times 60 / 60 = 3200$ microsteps per second.
2. $f_e = 6 \times 1000 / 60 = 100\ \text{Hz}$.
3. $\theta_m = 1.8 / 8 = 0.225$ degrees.
4. $f_e = 4 \times 1500 / 60 = 100\ \text{Hz}$. The shaft turns 25 times per second, so each shaft revolution contains $100 / 25 = 4$ electrical cycles, which equals the pole pair count.
5. $\theta_m = 0.9 / 16 = 0.05625$ degrees.

</details>

## Common mistakes

- Confusing electrical frequency with mechanical frequency. The drive works at $p$ times the shaft frequency, so the electrical frequency is $p n / 60$, not $n / 60$.
- Treating a stepper's microstep as a precise position. Microsteps set a current ratio, and friction and load can shift the rotor away from the commanded position, so accuracy depends on the motor and load, not on the microstep count alone.
- Choosing a stepper for high speed or high torque without checking the torque-speed curve. Torque falls steeply once the step rate rises.
- Forgetting that holding current heats the motor at standstill. A driver with current reduction at rest prevents overheating.
- Wiring Hall sensors or phases without a test at low speed. Wrong order produces noise and wrong direction.

## Go deeper

- [Circuits and Electronics (6.002), MIT OpenCourseWare](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/) by MIT: the switching circuits behind motor drives.
- [University Physics Volume 2, Chapter 13 (Electromagnetic Induction)](https://openstax.org/books/university-physics-volume-2/pages/13-introduction) by OpenStax: Faraday's law, the basis for back-EMF in every motor here.
- [Electric Motors](https://www.energy.gov/eere/buildings/electric-motors) by the U.S. Department of Energy: standards that set efficiency limits for motors and drives.
- Related lessons: [Mechatronics](../electronics/06-mechatronics.md) covers PWM, sensors, and motor drivers. [Feedback control](../../physics/14-controls.md) explains the position and speed loops that servo drives use. Next: [Induction motors](03-induction-motors.md).
