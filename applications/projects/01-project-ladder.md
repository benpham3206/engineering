# Projects: a ladder of build projects

**Type:** lesson

Projects turn the theory into hardware that you can measure and test. The ladder below starts with a
first-year bench exercise and ends with a capstone. Each rung uses the skills from the rungs below it,
and each one has a clear goal and a check you can run yourself.

**Prerequisites:** [Circuit basics](../electronics/01-circuit-basics.md), [RC circuits and op-amps](../electronics/02-rc-circuits-and-op-amps.md),
[Mechatronics](../electronics/06-mechatronics.md), [Robotics](../machines-robots/01-robot-arms.md), [Thermal systems](../thermal-fluid/01-thermal-systems.md),
[Fluid systems](../thermal-fluid/02-fluid-systems.md)
**Time:** 40-80 h across all rungs (each project 4-12 h)

## Core ideas

- **Build, measure, compare.** A project is done when you can measure what you built and compare it with
  the number your theory predicted. A gap between the two is useful information, not a failure.
- **Write the goal first.** A goal that a stranger could check is a good goal. "The bridge holds 2 kg"
  works. "A good bridge" does not.
- **Keep a log.** Record the date, the design change, the measured result, and the predicted result.
  Engineers reuse logs more than they reuse their memory.
- **Safety first.** Check current limits, keep batteries and motors away from loose hair and clothing,
  and wear eye protection for cutting, catapults, and fans.
- **One change at a time.** Change one variable per test, so you know what caused the result.

## The ladder

Each entry lists the goal, the skills used, and the theory to read first. Read the theory before
building.

1. **LED with a current-limiting resistor (first year)**
   - Goal: light an LED at a set current and measure the current with a multimeter.
   - Skills used: Ohm's law, series resistance, meter use.
   - Theory: [Circuit basics](../electronics/01-circuit-basics.md); [measurement folder](../../measurement/README.md).

2. **Voltage divider sensor logger**
   - Goal: read a potentiometer or light-dependent resistor with a microcontroller ADC and print the value.
   - Skills used: voltage dividers, ADC step size, reading code from a microcontroller.
   - Theory: [Mechatronics](../electronics/06-mechatronics.md); [RC circuits and op-amps](../electronics/02-rc-circuits-and-op-amps.md).

3. **Truss bridge**
   - Goal: build a balsa or card truss that holds a set load, and report the failure load.
   - Skills used: statics, tension and compression, joint loads, material strength.
   - Theory: [materials folder](../../materials/README.md); [physics folder](../../physics/README.md).

4. **Heat sink test**
   - Goal: measure the thermal resistance of a heat sink on a resistive heater, and compare it with a bare
     surface.
   - Skills used: thermal resistance, convection, temperature logging, unit checks.
   - Theory: [Thermal systems](../thermal-fluid/01-thermal-systems.md).

5. **Catapult**
   - Goal: launch a ball to a target distance, and show how the launch arm's length and stop angle change
     the range.
   - Skills used: energy balance, torque, repeatable testing, measurement error.
   - Theory: [physics folder](../../physics/README.md).

6. **Line-following robot**
   - Goal: follow a black line on white at a set speed, with a reflectance sensor and a motor driver.
   - Skills used: sensor reading, PWM, motor driver wiring, simple feedback control.
   - Theory: [Mechatronics](../electronics/06-mechatronics.md); [Robotics](../machines-robots/01-robot-arms.md).

7. **Wind tunnel**
   - Goal: build a small duct with a fan and measure the speed at the test section with a pitot tube or an
     anemometer.
   - Skills used: continuity, duct sizing, fan power, flow measurement.
   - Theory: [Fluid systems](../thermal-fluid/02-fluid-systems.md).

8. **Pump and pipe rig**
   - Goal: pump water through a loop, measure flow rate and head, and compare the pump power with the
     motor input.
   - Skills used: continuity, head loss, pump efficiency, Reynolds number.
   - Theory: [Fluid systems](../thermal-fluid/02-fluid-systems.md).

9. **Two-link robot arm**
   - Goal: drive a two-link arm to a set point from forward kinematics, and check the tip position by
     measurement.
   - Skills used: forward kinematics, DC motor torque and speed, gear ratio.
   - Theory: [Robotics](../machines-robots/01-robot-arms.md).

10. **3D-printed gearbox**
    - Goal: design and print a two-stage gearbox for the robot arm, and measure its output torque and
      efficiency.
    - Skills used: gear ratio, torque transfer, CAD, print tolerance, losses.
    - Theory: [manufacturing folder](../../manufacturing/README.md); [Robotics](../machines-robots/01-robot-arms.md).

11. **Capstone: a complete sized system**
    - Goal: pick one system (for example a cooling loop for an electronics box, or an arm that sorts
      objects), size it with the equations from every earlier lesson, build a prototype, and test it
      against the specification you wrote at the start.
    - Skills used: all earlier skills, plus design reviews and a written test report.
    - Theory: [design folder](../../design/README.md); [tools folder](../../tools/README.md).

## Practice

1. An LED drops $2.0\ \text{V}$ and needs $20\ \text{mA}$ from a $5\ \text{V}$ supply. Find the series resistor.
2. A heat sink must carry $50\ \text{W}$ across a $30\ \text{K}$ temperature difference. Find the required
   thermal resistance.
3. A small motor has $K_e = 0.01$ and $R = 1\ \Omega$ on a $6\ \text{V}$ supply. Find its no-load speed in rpm,
   ignoring friction.
4. A $0.025\ \text{m}$ diameter pipe carries $0.0020\ \text{m}^3/\text{s}$ of water. Find the velocity.
5. A $24\ \text{V}$ fan runs at a $40$ percent PWM duty cycle. Find the average voltage.

<details><summary>Answers</summary>

1. $150\ \Omega$
2. $0.60\ \text{K/W}$
3. $5730\ \text{rpm}$
4. $4.07\ \text{m/s}$
5. $9.6\ \text{V}$

</details>

## Checklist before you start any project

- [ ] Goal is written and checkable.
- [ ] Prediction for the key number is written before the build.
- [ ] Current, voltage, and temperature limits are known for every part.
- [ ] Test plan changes one variable at a time.
- [ ] Log file is open, with the date and the design version.

## Common mistakes

- Skipping the prediction. Without a number written beforehand, you cannot tell whether the result is good.
- Building the capstone first. Every rung teaches a skill the capstone needs, so climb the ladder in order.
- Trusting a single measurement. Repeat each test at least three times and report the spread.
- Ignoring the power rating of a motor driver, resistor, or battery. Parts that run hot fail early.
- Changing two things at once. You will not know which change caused the result.

## Go deeper

- [Circuits and Electronics (6.002), MIT OpenCourseWare](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/)
  by MIT: a full course that supports the electronics projects.
- [Robotics, Wikibooks](https://en.wikibooks.org/wiki/Robotics) by Wikibooks contributors: background for
  the line-following robot and the arm.
- [NIST, SI prefixes](https://www.nist.gov/pml/owm/metric-si-prefixes) by NIST: keep units consistent in
  every log.
- Previous: [Lesson 06, fluid systems](../thermal-fluid/02-fluid-systems.md).
