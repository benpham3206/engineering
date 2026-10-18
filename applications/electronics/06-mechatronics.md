# Mechatronics: sensors, actuators, and microcontrollers

**Type:** lesson

Mechatronics is the combination of mechanical parts, electronics, and software. A microcontroller
reads sensors, decides what to do, and drives actuators such as motors, valves, and lights. Most
modern machines, from printers to cars, are built this way.

**Prerequisites:** [Circuit basics](01-circuit-basics.md), [RC circuits and op-amps](02-rc-circuits-and-op-amps.md)
**Time:** 10-14 h

## Core ideas

- **Sensor**: a part that turns a physical quantity (temperature, distance, light, position) into
  an electrical signal. Many sensors change resistance or produce a small voltage.
- **Actuator**: a part that turns an electrical signal into motion or force. Motors, solenoids, and
  heaters are common actuators.
- **Microcontroller**: a small computer on one chip, with digital pins, analog input pins, and
  timers. Typical boards run at a few megahertz to a few hundred megahertz.
- **Digital I/O**: a pin is either high (near the supply voltage, often 3.3 V or 5 V) or low (near
  0 V). Digital outputs switch things on and off.
- **Analog input**: an analog-to-digital converter (ADC) measures a voltage and returns a number. A
  10-bit ADC returns integers from 0 to 1023.
- **PWM** (pulse-width modulation): a digital output switches on and off at a set frequency. The fraction of
  time it is on is the duty cycle. The average voltage seen by the load is the supply voltage times
  the duty cycle. PWM is how a microcontroller controls motor speed or LED brightness.
- **Motor driver**: a power circuit that lets a small microcontroller switch a motor that needs
  more current than the pin can supply. The microcontroller sends logic signals, and the driver
  does the switching.
- **Sampling and resolution**: an ADC measures at a fixed rate, and its resolution is the smallest
  voltage step it can see.

## Key equations

- PWM average voltage: $V_{avg} = D \cdot V_{supply}$, where $D$ is duty cycle (0 to 1, dimensionless)
  and $V_{supply}$ is volts (V).
- ADC step size (least significant bit, LSB): $V_{LSB} = \dfrac{V_{ref}}{2^n}$, where $V_{ref}$ is the
  reference voltage (V) and $n$ is the number of bits.
- ADC reading to voltage: $V_{in} = \text{code} \cdot \dfrac{V_{ref}}{2^n}$.
- Voltage divider for a sensor: $V_{out} = V_{s} \dfrac{R_{sensor}}{R_{sensor} + R_{fixed}}$.

## Worked example

**Given:** A microcontroller has a 10-bit ADC with a $5\ \text{V}$ reference. A sensor and a fixed
$10\ \text{k}\Omega$ resistor form a divider across $5\ \text{V}$. The ADC reads the code $512$ for one
measurement.

**Find:** (a) the step size of the ADC, (b) the voltage the ADC measured, and (c) the PWM average
voltage if the same $12\ \text{V}$ motor is driven at a $25$ percent duty cycle.

**Solution:**

1. (a) Step size: $V_{LSB} = 5 / 2^{10} = 5 / 1024 = 4.88\ \text{mV}$ per count.
2. (b) Measured voltage: $V_{in} = 512 \times 4.88\ \text{mV} = 2.50\ \text{V}$.
3. (c) PWM average: $V_{avg} = 0.25 \times 12\ \text{V} = 3.00\ \text{V}$.

**Answer:** (a) $4.88\ \text{mV}$ per count. (b) $2.50\ \text{V}$. (c) $3.00\ \text{V}$.

**Sanity check:** Code 512 is half of 1024, so the measured voltage should be half of the 5 V
reference, or $2.5\ \text{V}$. That matches. A $25$ percent duty cycle should give one quarter of
12 V, which is 3 V.

## How it fails

- **Sensor drift and bias.** Sensors change with temperature, age, and supply voltage, so a reading creeps with no change in the physical input. The sign is a slow disagreement with a reference. Calibrate against a known standard, and compensate or use a reference signal.
- **Noise and ground loops.** Motor switching and long cables inject electromagnetic interference into sensor lines, and multiple ground paths add hum. The sign is jitter or spikes that follow motor activity. Use shielded twisted cable, a single-point ground, filters, and routing that keeps signal wires away from motor wires.
- **Inductive kickback.** Switching off a motor, relay, or solenoid makes a voltage spike that destroys the transistor or the microcontroller pin. The sign is a driver that fails after some switching. A flyback diode across the coil prevents it.
- **Motor stall and overheating.** A blocked motor draws stall current and the windings heat quickly. The sign is a hot motor and a sagging supply. Current limiting, a thermal cutoff in the winding, and a controller that detects stall protect it.
- **Driver and supply overload.** A pin that supplies more than its rated current fails, and a supply with too little margin browns out the controller. The sign is random resets. Drive loads through a transistor or driver rated for the current, and use a separate or well-decoupled supply.
- **Software hang and brownout.** A stuck program or a low supply voltage leaves outputs in an unknown state. A watchdog timer resets the controller, a brownout detector holds it in reset, and outputs should default to a safe state.
- **Connector and cable fatigue.** Cables that flex at a moving joint break their conductors inside the insulation. The sign is an intermittent fault that follows motion. Use flex-rated cable, strain relief, and locking connectors.
- **Moving and stored energy hazards.** A machine can start, trap, or crush, and springs, raised loads, and batteries hold energy. Eliminate the hazard by designing it out, substitute lower force and voltage, add guards and interlocks, an emergency stop and a safe-torque-off function, then administrative controls and PPE. For maintenance, apply lockout/tagout: isolate and lock each energy source, release or block stored energy, and verify zero energy by trying to start the machine and by measuring.

## Practice

1. A 10-bit ADC has a $3.3\ \text{V}$ reference. Find the step size in millivolts.
2. The 10-bit ADC from the worked example (5 V reference) reads code $800$. Find the voltage.
3. A $12\ \text{V}$ fan runs at $50$ percent duty cycle. Find the average voltage.
4. A $5\ \text{V}$ supply feeds a $10\ \text{k}\Omega$ potentiometer. The wiper is at the middle. Find the
   wiper voltage.
5. An 8-bit ADC has a $5\ \text{V}$ reference. Find the step size in millivolts.

<details><summary>Answers</summary>

1. $3.22\ \text{mV}$
2. $3.91\ \text{V}$
3. $6.00\ \text{V}$
4. $2.50\ \text{V}$
5. $19.5\ \text{mV}$

</details>

## Common mistakes

- Treating PWM as an analog voltage. The load sees pulses, and the average is only correct if the
  load filters or averages the pulses, as a motor winding does.
- Using the wrong reference voltage in the ADC formula. Check the datasheet for the reference you
  configured.
- Connecting a motor directly to a microcontroller pin. Pins can supply only a few milliamps, and
  motors often need hundreds of milliamps. Use a motor driver.
- Forgetting that a 10-bit ADC has $2^{10} = 1024$ codes, not 1000. Divide by 1024.
- Ignoring the sensor tolerance. A resistor and sensor can each vary by a few percent, which adds to
  the measurement error.

## Go deeper

- [Circuits and Electronics (6.002), MIT OpenCourseWare](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/)
  by MIT: circuit design for sensors and digital logic.
- [Electronics, Wikibooks](https://en.wikibooks.org/wiki/Electronics) by Wikibooks contributors:
  background on digital logic and amplifiers that sensor interfaces use.
- [NIST, SI prefixes](https://www.nist.gov/pml/owm/metric-si-prefixes) by NIST: standard unit prefixes
  for millivolts, microfarads, and kilohms.
- Previous: [Sensors in products](05-sensors-in-products.md).
- Next: [Robot arms](../machines-robots/01-robot-arms.md).
- [Applications reference](../reference.md): the lookup sheet for this topic.
