# Infusion pumps and ventilators

**Type:** lesson

An infusion pump delivers a fluid at a set volume rate through tubing, and a ventilator moves gas into and out of a lung model with controlled pressure and flow. Both devices are engineered as closed-loop systems with alarms, because a fault in flow or pressure can reach the user in seconds.

**Prerequisites:** [Hydrostatics and Bernoulli](../../physics/10-hydrostatics-and-bernoulli.md), [Control volumes and pipe flow](../../physics/11-control-volumes-pipe-flow.md), [Feedback control](../../physics/14-controls.md), [Fluid systems](../thermal-fluid/02-fluid-systems.md), [Factor of safety and failure](../../design/07-factor-of-safety-and-failure.md)
**Time:** 6-8 h

## Core ideas

### How it works

An infusion pump moves fluid in small, precise volumes. A motor drives a lead screw that pushes a syringe plunger, or a rotor squeezes a flexible tube in a peristaltic pump. The pump's controller counts motor steps, and each step displaces a known volume. The flow rate is the volume per step multiplied by the step rate. A pressure sensor detects blockage, and an air sensor detects bubbles in the line. The controller stops the pump and sounds an alarm when either sensor reports a fault.

A ventilator moves gas through a patient circuit. A gas source, a blower or valves, and a flow sensor set the inspiratory flow. A pressure transducer measures the pressure in the circuit. An exhalation valve opens to let gas leave, and a positive end-expiratory pressure (PEEP) valve holds a set pressure at the end of exhalation. The controller reads the pressure and flow signals and adjusts the valves to follow a set profile. The engineering problem is to deliver a set volume or pressure with known error and to detect a fault before it harms the user.

### Main parts

- Pump drive: a stepper or DC motor, a lead screw or rotor, and a gear train. Position encoders or step counts confirm the displacement.
- Fluid path: a syringe or tubing set, a check valve, and an anti-free-flow valve that prevents uncontrolled flow when the set is loaded or removed.
- Sensors: an occlusion pressure sensor, an ultrasonic or optical air-in-line detector, and a drop or position sensor for the plunger.
- Controller and software: a microcontroller that sets the flow rate, runs the alarm logic, and stores the programmed dose.
- Ventilator gas path: an oxygen blender, flow valves, a blower or compressed-gas regulator, and a humidifier.
- Ventilator circuit: an inspiratory limb, an expiratory limb, a PEEP valve, an exhalation valve, and a test lung or patient interface.
- Ventilator sensors and alarms: pressure and flow transducers, an oxygen sensor, and a controller that checks for leaks and disconnection.

### Variants

- Syringe pumps deliver small volumes at low rates with high accuracy. They have a plunger and a fixed syringe size.
- Volumetric pumps use a peristaltic or cassette mechanism for larger volumes. They rely on the tube set's geometry.
- Ambulatory pumps are battery-powered and portable. Battery life and size trade against flow accuracy and display size.
- Ventilators come in transport, intensive-care, and portable designs. Each one trades power, size, noise, and gas consumption differently.
- Historically, the iron lung was a negative-pressure ventilator that pulled the chest wall outward, instead of pushing gas into the airway.

## Key equations

- Volume rate and delivered volume: $Q = \dot V$, and $V = Q\,t$. Here $Q$ is the volume flow rate in $\text{m}^3/\text{s}$, $\dot V$ is the same quantity, $t$ is time in seconds, and $V$ is volume in $\text{m}^3$. Assumes a constant flow rate over the interval.
- Hagen-Poiseuille flow in a tube: $Q = \dfrac{\pi \Delta p\, r^4}{8 \mu L}$. Here $\Delta p$ is the pressure drop in pascals, $r$ is the tube radius in metres, $\mu$ is dynamic viscosity in $\text{Pa s}$, and $L$ is the tube length in metres. Assumes laminar, steady, fully developed flow of a Newtonian incompressible fluid in a rigid, straight, circular tube.
- Ventilator equation of motion for a test lung: $p = \dfrac{V}{C} + R\,Q + \text{PEEP}$. Here $p$ is the airway pressure in $\text{cmH}_2\text{O}$, $V$ is the volume in litres, $C$ is compliance in $\text{L/cmH}_2\text{O}$, $R$ is resistance in $\text{cmH}_2\text{O/(L/s)}$, $Q$ is flow in $\text{L/s}$, and PEEP is the set end-expiratory pressure in $\text{cmH}_2\text{O}$. Assumes linear elastic compliance, linear resistance, and constant flow, which is an approximation for a bench test lung.
- Unit conversion: $1\ \text{cmH}_2\text{O} = 98.07\ \text{Pa}$, a standard conversion from the water-column definition at standard gravity.

## Worked example

**Given:** Two bench problems, both using engineering test setups and not patient settings.

*Part A.* An infusion pump delivers water at $5\ \text{mL/h}$ through a tube of inner diameter $1.6\ \text{mm}$ and length $1.5\ \text{m}$. Water has dynamic viscosity $\mu = 1.0\ \text{mPa s}$ at about $20\ \text{C}$ (typical). Assume laminar, steady flow in a rigid tube.

*Part B.* A ventilator is tested on a bench test lung with compliance $C = 0.050\ \text{L/cmH}_2\text{O}$ and resistance $R = 5\ \text{cmH}_2\text{O/(L/s)}$. The test delivers a volume $V = 0.5\ \text{L}$ at a flow $Q = 0.5\ \text{L/s}$, with PEEP of $0$.

**Find:** (a) the flow in $\text{m}^3/\text{s}$, (b) the pressure drop along the tube, and (c) the peak airway pressure on the test lung, in both $\text{cmH}_2\text{O}$ and kPa.

**Solution:**

1. Flow: $Q = 5\times10^{-6}\ \text{m}^3 / 3600\ \text{s} = 1.389\times10^{-9}\ \text{m}^3/\text{s}$.
2. Pressure drop: $\Delta p = 8\mu L Q / (\pi r^4)$, with $r = 0.8\times10^{-3}\ \text{m}$, gives $\Delta p = 8(1.0\times10^{-3})(1.5)(1.389\times10^{-9}) / [\pi (0.8\times10^{-3})^4] = 13.0\ \text{Pa}$.
3. Peak pressure: $p = V/C + RQ = 0.5/0.050 + 5 \times 0.5 = 10 + 2.5 = 12.5\ \text{cmH}_2\text{O}$.
4. Convert: $12.5 \times 98.07 = 1226\ \text{Pa}$, or $1.23\ \text{kPa}$.

**Answer:** (a) $Q = 1.39\times10^{-9}\ \text{m}^3/\text{s}$. (b) $\Delta p = 13.0\ \text{Pa}$. (c) $p = 12.5\ \text{cmH}_2\text{O} = 1.23\ \text{kPa}$.

**Sanity check:** The tube pressure drop of 13 Pa is small, so a long, narrow tube does not limit flow at this rate. The pump's occlusion sensor must detect a rise from that small baseline, which is why sensor resolution matters. In part B, $V/C = 10\ \text{cmH}_2\text{O}$ is the elastic term and $RQ = 2.5\ \text{cmH}_2\text{O}$ is the resistive term, so the elastic term dominates in this test.

## Design trade-offs

- Flow accuracy against cost. A high-accuracy pump needs a finer drive, better sensors, and calibration. Each step adds cost and power draw.
- Occlusion sensitivity against false alarms. A sensitive pressure threshold catches blockages early, but it also trips on normal events such as tube kinks or changes in height.
- Pump size against battery life. A portable pump has a small battery, so the motor and display draw must stay low.
- Dead volume against response time. Tubing and valves hold fluid that is not delivered, and the volume matters when rates are small.
- Ventilator noise against power. A quiet blower draws less power, but it may be slower to follow a pressure profile.
- Gas consumption against portability. Oxygen blending and humidification add plumbing and weight.
- Response time against stability. A fast valve reacts quickly, but it may overshoot. The control loop must balance the two.

## How it fails

- Free flow. Gravity or pressure drives fluid uncontrolled when the set is loaded or the door is open. A check valve or anti-free-flow valve prevents it.
- Occlusion. A kinked or blocked line raises pressure. The sensor must alarm before the pressure reaches a damaging level.
- Air in the line. A bubble passes into the line when a container runs empty or a connection leaks. An air sensor stops the pump.
- Dosing errors. Wrong programming causes an incorrect rate. A drug library with limits on the programmed value reduces this risk.
- Leaks and disconnection in the ventilator circuit. A leak lowers the delivered volume, and a disconnection drops the pressure. The controller must alarm on both.
- Valve sticking and sensor drift. A stuck valve or a drifted sensor gives the wrong pressure or flow reading.
- Power loss or low battery. The device must alarm and fall back to a safe state.
- Lead screw wear. A worn screw gives uneven displacement and erratic flow.

**Risk management.** ISO 14971 governs these hazards. The manufacturer estimates the severity and probability of each hazard, reduces the risk with controls, and verifies the residual risk. IEC 60601-1-8 governs the design and testing of alarm systems. The hierarchy of controls applies as follows.

- Elimination: remove the hazard. For example, an anti-free-flow mechanism removes the free-flow path at the set.
- Substitution: replace the hazard source. For example, use a drug library in place of free-text rate entry, which removes many manual typing errors.
- Engineering controls: build protection into the device. For example, an occlusion sensor, an air-in-line detector, redundant pressure sensors on the ventilator circuit, a safe-state valve position on power loss, and a battery backup.
- Administrative controls: labeling, instructions for use, alarm response procedures, and scheduled maintenance and calibration.
- Personal protective equipment: gloves and eye protection for staff who handle fluids, tubing, or gas connections during set-up or cleaning.

**Regulation and standards.** The FDA classifies infusion pumps and ventilators in Class II, which needs special controls and typically a 510(k) premarket notification. The product's classification must be confirmed in the FDA database. IEC 60601-2-24 covers infusion pumps and controllers. IEC 60601-2-12 covers lung ventilators, and ISO 80601-2-12 is the newer form of that standard. IEC 60601-1 covers basic safety, and IEC 60601-1-8 covers alarm systems. ISO 14971 governs risk management.

## History

Thomas Latta in Britain described intravenous saline infusion during a cholera epidemic in about 1832. Gravity drip sets remained the standard method for more than a century. Philip Drinker and Louis Agassiz Shaw at the Harvard School of Public Health built a negative-pressure ventilator in 1928, which became known as the iron lung. Positive-pressure ventilators replaced the iron lung in many settings in the following decades. Electronic infusion pumps with alarms and dose limits became common in hospitals in the late twentieth century.

## Practice

1. A ventilator test lung has $C = 0.040\ \text{L/cmH}_2\text{O}$, the bench test delivers $V = 0.4\ \text{L}$ at $Q = 0.4\ \text{L/s}$, with $R = 4\ \text{cmH}_2\text{O/(L/s)}$ and PEEP of $0$. Find the peak pressure in $\text{cmH}_2\text{O}$ and in kPa.
2. An infusion pump delivers water at $10\ \text{mL/h}$ through a tube of inner diameter $1.6\ \text{mm}$ and length $1.0\ \text{m}$. Water has $\mu = 1.0\ \text{mPa s}$. Find the pressure drop in pascals, assuming laminar flow.
3. A pump runs at $25\ \text{mL/h}$ for $90$ minutes. Find the volume delivered in millilitres.
4. Convert $1.0\ \text{cmH}_2\text{O}$ to pascals, using the standard conversion of $98.07\ \text{Pa}$.

<details><summary>Answers</summary>

1. $p = 0.4/0.040 + 4 \times 0.4 = 11.6\ \text{cmH}_2\text{O} = 1.14\ \text{kPa}$
2. $\Delta p = 17.3\ \text{Pa}$
3. $V = 25 \times 1.5 = 37.5\ \text{mL}$
4. $98.07\ \text{Pa}$

</details>

## Common mistakes

- Mixing up hourly and per-minute rates. A rate of $25\ \text{mL/h}$ is about $0.42\ \text{mL/min}$.
- Ignoring compliance in the tubing and the circuit. Compliance stores volume, so the delivered volume can differ from the displaced volume.
- Using Hagen-Poiseuille flow for turbulent or non-Newtonian fluids. Its assumptions require laminar, Newtonian flow in a rigid tube.
- Mixing $\text{cmH}_2\text{O}$ and kPa in one equation. Convert to one unit before you combine terms.
- Treating a sensor alarm as optional. Each alarm exists because a specific hazard in the failure analysis requires it.

## Go deeper

- [Medical Devices, U.S. Food and Drug Administration](https://www.fda.gov/medical-devices): the FDA hub for device regulation, classification, and recalls.
- [Classify Your Medical Device, U.S. Food and Drug Administration](https://www.fda.gov/medical-devices/overview-device-regulation/classify-your-medical-device): device classes and the 510(k) pathway for Class II devices.
- [Control volumes and pipe flow](../../physics/11-control-volumes-pipe-flow.md) for the flow equations used in the tube example.
- [Feedback control](../../physics/14-controls.md) for the control loops that regulate pump flow and ventilator pressure.
- [Thermal-fluid reference](../../physics/reference-thermofluids.md) for pressure, flow, and viscosity background.
