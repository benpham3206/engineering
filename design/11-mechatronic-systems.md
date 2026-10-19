# Mechatronic systems

**Type:** lesson

A mechatronic system combines mechanics, electronics, sensors, actuators, and software into one machine that senses what it is doing and corrects itself. A 3D printer, a robotic arm, a camera gimbal, and a car's cruise control are all mechatronic systems. The skill is in the connections. A good mechanical design is wasted if the sensor cannot see the motion, and a good controller cannot fix a loose gear.

**Prerequisites:** [Design process](01-design-process.md), [Shafts and bearings](08-shafts-and-bearings.md), [Sensors and transducers](../measurement/05-sensors-and-transducers.md), [Electricity and magnetism](../physics/06-electricity-and-magnetism.md), [Feedback control](../physics/14-controls.md)
**Time:** 10-15 h

## Core ideas

- **Mechanism.** The moving hardware: links, gears, lead screws, belts, and bearings. It turns actuator motion into the motion the user needs.
- **Actuator.** The part that makes motion happen, such as a DC motor, a stepper motor, a servo, or a solenoid.
- **Sensor.** The part that measures the state of the system. An encoder measures angle or position. A limit switch detects an end of travel. A current sensor measures motor load.
- **Controller.** The processor that reads sensors and decides what the actuator should do. It runs a control law, which is a set of rules or equations.
- **Feedback loop.** The sensor reports the result, the controller compares it with the target, and the actuator corrects the error. A loop with feedback is called closed-loop control. Without a sensor, the system is open-loop, and it cannot correct errors it cannot see.
- **Resolution.** The smallest change a sensor can report. It limits how precisely the controller can position the machine.
- **Interface.** The electrical and software link between parts. Voltage levels, communication protocols, and timing must match.

## Systems thinking

A mechatronic design is a set of trade-offs across disciplines. A few habits help:

- Define the motion first. Ask what position, speed, and force the machine must reach, and how precisely.
- Choose the sensor from the resolution and range the controller needs. A sensor that is too coarse cannot meet the goal, no matter how fast the processor is.
- Keep mechanical backlash, play, and compliance in mind. A gear with play can make a precise sensor look wrong.
- Put the sensor where it measures the result you care about. An encoder on the motor shaft does not see slop in the screw after the coupling.
- Plan for failure. What happens when a sensor disconnects, a motor stalls, or a limit switch sticks?

## Key equations

Angle per count for a quadrature encoder with $P$ pulses per revolution (PPR), read on all four edges, so $N = 4P$ counts per revolution:

$$
\theta_{\text{count}} = \frac{360^\circ}{4P}
$$

Linear travel per count for a lead screw with lead $\ell$ (mm of travel per revolution), giving $\Delta x$ in mm:

$$
\Delta x = \frac{\ell}{4P}
$$

Counts per second at speed $n$ rpm:

$$
f = \frac{4P \, n}{60}
$$

Linear speed of the screw nut at $n$ rpm, giving $v$ in mm/s:

$$
v = \frac{\ell \, n}{60}
$$

Units: $\ell$ and $\Delta x$ in mm (or in). $\theta$ in degrees. $f$ in counts per second. The factor 4 in each formula comes from reading both channels of a quadrature encoder on both edges.

## Worked example

A servo motor drives a lead screw through a direct coupling. The screw has a lead of 5 mm per revolution. The motor has a 1000 PPR quadrature encoder on its shaft. The motor runs at 600 rpm. Find the angle per count, the linear travel per count, the counts per second, and the linear speed of the nut.

**Given.** $P = 1000$ PPR, $\ell = 5$ mm, $n = 600$ rpm.

**Find.** $\theta_{\text{count}}$, $\Delta x$, $f$, and $v$.

**Assumptions.** Direct coupling with no slip or backlash. Encoder reads four edges per pulse.

**Solution.**

Step 1. Counts per revolution: $4P = 4000$.

Step 2. Angle per count: $\theta_{\text{count}} = \dfrac{360}{4000} = 0.09^\circ$.

Step 3. Linear travel per count: $\Delta x = \dfrac{5}{4000} = 0.00125$ mm $= 1.25\ \mu$m.

Step 4. Counts per second: $f = \dfrac{4000 \times 600}{60} = 40\,000$ counts/s.

Step 5. Linear speed: $v = \dfrac{5 \times 600}{60} = 50$ mm/s.

**Answer.** Angle per count 0.09 degrees. Linear travel per count 1.25 micrometres. Counts per second 40 000. Nut speed 50 mm/s.

**Sanity check.** At 600 rpm, the screw turns 10 times per second. Each turn moves 5 mm, so the speed is 50 mm/s, which matches step 5. The 40 000 counts per second equals 4000 counts per turn times 10 turns per second. The resolution of 1.25 micrometres is far smaller than the 5 mm lead. A fine sensor on a coarse screw can still give fine positioning, as long as the screw is stiff and backlash-free.

## Checklist

- Is the encoder count taken as four times the PPR for a quadrature encoder?
- Is the sensor on the element that matters, not only on the motor?
- Is the resolution finer than the smallest move the machine must make?
- Are backlash, play, and compliance in the mechanism measured or estimated?
- Is there a fallback if a sensor fails or a limit is reached?
- Are the voltage levels and timing of the interface checked?

## Practice

1. A 2048 PPR quadrature encoder is used. Find the angle per count in degrees to five decimal places.
2. The same encoder is used. How many counts are there per revolution?
3. A lead screw has a lead of 2 mm and a 4000-count-per-revolution encoder on the screw. Find the travel per count in micrometres.
4. A lead screw with a 5 mm lead runs at 300 rpm. Find the nut speed in mm/s.

<details><summary>Answers</summary>

1. 0.04395
2. 8192
3. 0.5
4. 25

</details>

## Common mistakes

- Using PPR as the count per revolution, which forgets the factor of 4 in quadrature mode.
- Putting the encoder on the motor and assuming the load position matches it, which ignores backlash and coupling slip.
- Choosing a sensor with resolution coarser than the required move.
- Mixing units, such as lead in inches with travel in millimetres.
- Forgetting that a closed loop can only correct errors that the sensor can see.

## Go deeper

- [MIT OpenCourseWare, 2.017J Design of Electromechanical Robotic Systems](https://ocw.mit.edu/courses/2-017j-design-of-electromechanical-robotic-systems-fall-2009/) by MIT: a free course on designing and testing electromechanical robots, covering sensing, actuation, and control in hardware.
- [Engineering LibreTexts](https://eng.libretexts.org/) by the LibreTexts project: free engineering textbooks, including circuits and control background.
- [OpenStax University Physics Volume 1](https://openstax.org/books/university-physics-volume-1/pages/1-introduction) by OpenStax at Rice University: free physics text covering motion and forces that drive actuators.
- [Design reference](reference.md): the lookup sheet for this topic.
