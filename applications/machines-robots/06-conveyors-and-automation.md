# Conveyors and automation

**Type:** lesson

A conveyor moves material along a fixed path with a belt or rollers, and automation decides when it
starts, stops, and where each item goes. An engineer sizes the drive for speed, throughput, and
power, and designs the control logic so that a fault stops the line safely.

**Prerequisites:** [Mechatronics](../electronics/06-mechatronics.md),
[Sensors in products](../electronics/05-sensors-in-products.md),
[Digital logic and computers](../electronics/07-digital-logic-and-computers.md),
[Gear trains](../power-transmission/01-gear-trains.md),
[Statics](../../physics/01-statics.md)
**Time:** 8-12 h

## Core ideas

- **Belt conveyor**: an endless belt runs over a drive pulley and idler pulleys. Friction between the
  drive pulley and the belt pulls the belt along. The load rides on the belt.
- **Roller conveyor**: rows of rollers carry the load. Powered rollers are driven by a belt, a chain,
  or a motor in each roller. Unpowered rollers let the load slide or are pushed along.
- **Throughput**: the mass of material passing a point each second, in kilograms per second (kg/s).
- **Sensor**: a device that reports a condition to the controller. A photoeye reports that a beam is
  broken, and an encoder reports shaft position. See the [sensors lesson](../electronics/05-sensors-in-products.md).
- **Actuator**: a device that acts on the line. A motor drives the belt, and a pneumatic cylinder
  pushes an item into a diverter lane.
- **Programmable logic controller (PLC)**: an industrial computer that reads inputs, runs a program,
  and sets outputs on a fixed cycle. Its program is usually written in ladder logic.
- **Scan cycle**: the PLC reads every input, runs the program from the first rung to the last, writes
  every output, and repeats. A full scan takes milliseconds in typical small PLCs.

## How it works

A motor drives a gearbox, and the gearbox turns the drive pulley. The belt grips the pulley through
friction, and the belt carries the load along its top surface. The belt returns underneath on the idler
pulleys. A roller conveyor works the same way, except that each roller turns to move the load on top
of it.

Automation adds the control layer. A sensor at the start of the line sees a box. The PLC reads that
input, decides the box is in the right place, and sets an output that switches the motor contactor.
At the end of the line, a second sensor counts the box. If the diverter sensor sees a wrong box, the
PLC sets a solenoid valve, and a pneumatic cylinder pushes the box into a side lane.

## Main parts

- Drive pulley and motor: the drive pulley turns the belt. The motor and gearbox set its speed and
  torque.
- Idler pulleys and tensioner: they guide the belt and keep it tight enough to grip the drive pulley.
- Frame, rollers, and guards: the frame holds the line level and in position. Guards cover pinch
  points.
- Sensors: photoeyes, proximity sensors, and encoders report the state of the line.
- Contactors and drives: a contactor switches motor power. A variable frequency drive sets the speed.
- PLC: reads the inputs and sets the outputs according to its program.
- Actuators: solenoid valves and pneumatic cylinders move items, stoppers, and diverters.
- Emergency stop: a hardwired button that removes power from the motor through a safety circuit, not
  only through the PLC.

## Variants

- Flat belt: the belt is flat across its width. It suits light, uniform loads.
- Troughed belt: the belt sides curl up over idler rollers. It carries bulk material such as grain
  or gravel.
- Powered roller conveyor: each roller or zone has its own drive. Zones start and stop
  independently.
- Chain and slat conveyors: they carry heavy or hot items that a belt cannot take.
- PLC types: a compact PLC suits a small machine. A modular rack suits a large line with many I/O
  points. A safety PLC runs safety functions such as an emergency stop with its own certified logic.

## Key equations

Assumptions for the equations below: the belt does not slip on the drive pulley, the load moves at
the belt speed, and the flow is steady.

Belt speed for a drive pulley of diameter $D$ in metres (m) turning at $N$ revolutions per second
(rev/s), with $v$ in metres per second (m/s):

$$v = \pi D N$$

Mass throughput for a load of linear density $\lambda$ in kilograms per metre (kg/m), moving at
belt speed $v$:

$$\dot{m} = \lambda v$$

Rolling resistance force for total load weight $W = m g$ in newtons (N), with the rolling resistance
coefficient $\mu_r$ (dimensionless, typical value about 0.03 for a belt on steel rollers). The formula
assumes a level section with no slope and a load that rolls, not slides:

$$F = \mu_r\,m\,g$$

Horizontal drive power, with $P$ in watts (W), assuming a level section:

$$P_{\text{horiz}} = F\,v$$

Lift power for a mass flow $\dot{m}$ raised a height $h$ in metres (m), assuming steady flow and that
the load gains only potential energy:

$$P_{\text{lift}} = \dot{m}\,g\,h$$

Input power for drive efficiency $\eta$ (dimensionless, between 0 and 1):

$$P_{\text{in}} = \frac{P_{\text{horiz}} + P_{\text{lift}}}{\eta}$$

## Ladder logic basics

Ladder logic draws a control circuit as rungs between two vertical power rails. The PLC scans each
rung from left to right, top to bottom. Four elements make up nearly every rung.

- Normally open contact: it is true when its input is on, and false when its input is off.
- Normally closed contact: it is true when its input is off, and false when its input is on.
- Coil: an output. It turns on when the conditions to its left are true.
- Timer and counter: a timer turns on its output after a set delay, and a counter counts events.

A seal-in circuit keeps a motor running after the start button is released. The motor's own contact
sits in parallel with the start contact, so either one keeps the coil on. The stop contact sits in
series, so pressing stop breaks the path.

```
  Start   Stop (NC)    Motor
--| |----+----|/|------( )--
         |
  Motor  |
--| |----+
```

In this rung, pressing Start turns on the Motor coil, and the Motor contact seals the circuit. Pressing
Stop opens the path and turns the coil off. The stop contact is normally closed, so a broken stop
wire also stops the motor. This fails safe.

A PLC scans the rung once per cycle. An output set in one rung can be read by the next rung on the next
scan, so outputs can lag by one scan. This matters for fast sensor signals.

## Worked example

**Given:** A belt conveyor carries a load of linear density $\lambda = 12\ \text{kg/m}$ at a speed
$v = 0.50\ \text{m/s}$. The belt runs $L = 20\ \text{m}$ horizontally, then lifts the load
$h = 5\ \text{m}$. The rolling resistance coefficient is $\mu_r = 0.03$, and the drive efficiency is
$\eta = 0.80$. Use $g = 9.81\ \text{m/s}^2$.

**Find:** (a) the throughput, (b) the friction force on the horizontal section, (c) the drive pulley
speed in rpm, and (d) the input power.

**Solution:**

1. Throughput: $\dot{m} = \lambda v = 12 \times 0.50 = 6.0\ \text{kg/s}$, which is $21.6\ \text{t/h}$.
2. Mass on the horizontal section: $m = \lambda L = 12 \times 20 = 240\ \text{kg}$.
   Weight: $W = 240 \times 9.81 = 2354\ \text{N}$.
   Friction force: $F = 0.03 \times 2354 = 70.6\ \text{N}$.
   Horizontal power: $P_{\text{horiz}} = 70.6 \times 0.50 = 35.3\ \text{W}$.
3. Lift power: $P_{\text{lift}} = 6.0 \times 9.81 \times 5 = 294\ \text{W}$.
4. Input power: $P_{\text{in}} = (35.3 + 294) / 0.80 = 412\ \text{W}$.
5. Drive pulley diameter: take $D = 0.20\ \text{m}$. The speed is $N = v / (\pi D) = 0.50 / (\pi \times 0.20) = 0.796\ \text{rev/s}$, which is $47.7\ \text{rpm}$.

**Answer:** (a) $6.0\ \text{kg/s}$ ($21.6\ \text{t/h}$). (b) $70.6\ \text{N}$. (c) $47.7\ \text{rpm}$ for a
$0.20\ \text{m}$ drive pulley. (d) $412\ \text{W}$.

**Sanity check:** The lift power is much larger than the friction power, which is typical when a belt
climbs even a short height. The input power is larger than the output power, which is required by
an efficiency below 1. The check $\dot{m} g h = 6.0 \times 9.81 \times 5 = 294\ \text{W}$ matches step 3.

## Design trade-offs

- Speed against belt wear and noise: a faster belt moves more material but wears idlers and bearings
  faster, and it raises noise.
- Belt tension against slip and bearing life: more tension grips the drive pulley better but loads
  the bearings and shortens belt life. Too little tension lets the belt slip.
- Load against motor size: a heavier load or a steeper lift needs a larger motor and gearbox.
- Zone control against cost: a powered roller zone starts and stops independently, which saves
  energy and handles accumulation. It costs more drives and controls than a single belt.
- Control complexity against reliability: a PLC program with many interlocks is hard to test. Keep
  the program simple and hardwire the safety functions.

## How it fails

- Belt slip: the motor turns, but the belt does not move. Low tension, oil, water, or overload cause it.
  A squeal at the drive pulley is an early warning.
- Belt tracking drift: the belt walks sideways off the pulleys and damages its edges. Misaligned
  pulleys and uneven loads cause it.
- Jams and pinch points: a jam can trap a hand between a belt and a pulley or roller. Guards and
  emergency stops protect people at these points.
- Sensor fault: a dirty photoeye reads a false beam break. The PLC may stop the line or send a box to
  the wrong lane.
- Logic error or power loss: a wrong ladder rung can keep a motor running or let a cylinder move
  unexpectedly. A power dip can drop outputs and leave the line in an unknown state.
- Broken wire on a stop circuit: a normally open stop button fails with the wire, so the machine
  keeps running. A normally closed contact fails safe.

Safety follows the hierarchy of controls, strongest first:

1. Elimination: remove the hazard where possible. Keep people out of the pinch zone by designing the
   line so that no one needs to reach into it while the belt runs.
2. Substitution: use a low-speed drive, a lower-energy actuator, or a slat conveyor where a belt
   would catch fingers.
3. Engineering controls: fixed guards over pinch points, hardwired emergency stops that remove motor
   power directly, pull-cords along the line, safety-rated sensors, and a safety PLC for the stop
   functions.
4. Administrative controls: written procedures, operator training, lockout and tagout rules, and a
   schedule for belt inspection and replacement.
5. Personal protective equipment: gloves and close-fitting clothing for the work area. PPE is the last
   layer, because it does not stop a belt from pulling in a limb.

Lockout and tagout before any service on the line:

- Isolate every energy source: open the motor disconnect, turn off the variable frequency drive, and
  shut the compressed air supply to any pneumatic cylinders on the line.
- Release or restrain the stored energy: let a pneumatic cylinder exhaust its air, block any raised
  or spring-loaded part with a mechanical stop, and let a belt come to rest before work begins.
- Verify a zero-energy state: try to start the line from its normal controls, confirm that nothing
  moves, and only then begin work. Lock and tag every isolation point, and remove the lock only when
  the person who applied it is finished.

## History

Belt conveyors appeared in mining and grain handling in the 19th century. Henry Ford's Highland Park
plant used a moving assembly line in 1913, which made the conveyor a core tool of mass production.
The programmable logic controller grew out of relay control. Engineers wired relays into ladder
diagrams to control machines. In 1969, Richard Morley led the team that built the Modicon 084, an early
PLC that replaced relay panels with a programmable controller. Ladder logic kept the relay-style
drawing, so electricians could read the program.

## Lessons for engineers today

- A conveyor is sized by throughput and lift, and the drive is sized by the power those set.
- Put safety functions in hardwired circuits, not only in the program.
- Design control logic to fail safe: a broken wire or lost power should stop the machine.

## Practice

1. A drive pulley of diameter $0.15\ \text{m}$ turns at $40\ \text{rpm}$. Find the belt speed in m/s.
2. A load of $8\ \text{kg/m}$ moves at $0.40\ \text{m/s}$. Find the throughput in kg/s and in t/h.
3. A horizontal belt is $30\ \text{m}$ long, carries $10\ \text{kg/m}$, moves at $0.50\ \text{m/s}$, and
   has $\mu_r = 0.03$. Find the horizontal power in watts.
4. A throughput of $3.2\ \text{kg/s}$ is lifted $6\ \text{m}$. Find the lift power in watts.
5. A start/stop rung uses a normally open stop button. Explain why this is unsafe, and say what contact
   type to use instead.

<details><summary>Answers</summary>

1. $v = \pi \times 0.15 \times (40 / 60) = 0.314\ \text{m/s}$
2. $\dot{m} = 8 \times 0.40 = 3.2\ \text{kg/s}$, which is $11.5\ \text{t/h}$
3. $m = 300\ \text{kg}$, $W = 2943\ \text{N}$, $F = 88.3\ \text{N}$, and $P = 88.3 \times 0.50 = 44.1\ \text{W}$
4. $P = 3.2 \times 9.81 \times 6 = 188\ \text{W}$
5. A broken stop wire leaves the normally open contact open, so the machine keeps running when someone
   presses stop and the wire is cut. Use a normally closed stop contact, so that a broken wire opens the
   circuit and stops the motor.

</details>

## Common mistakes

- Using rpm directly in the belt speed formula. The formula takes revolutions per second, so divide by 60.
- Applying the horizontal friction formula to a lifting section. A climb adds potential energy, which
  the lift term covers.
- Forgetting the drive efficiency. Motor input power must be larger than the power the belt delivers.
- Wiring a stop button as normally open. A broken wire then leaves the machine running.
- Assuming the PLC runs every rung at once. Each rung runs in order, so outputs can lag by one scan.

## Go deeper

- [Robotics, Wikibooks](https://en.wikibooks.org/wiki/Robotics) by Wikibooks contributors: sensors and
  actuators, which drive the conveyor and the automation layer.
- [Circuits and Electronics (6.002), MIT OpenCourseWare](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/)
  by MIT: circuit fundamentals behind the sensor and control wiring.
- Reference sheets: [Applications reference](../reference.md) and
  [Mechanics reference](../../physics/reference-mechanics.md).
- Related lessons: [Hydraulics and pneumatics](07-hydraulics-and-pneumatics.md),
  [Robot arms](01-robot-arms.md), [Gear trains](../power-transmission/01-gear-trains.md), and
  [DC motors](../electrical/01-dc-motors.md).
