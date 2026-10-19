# 3D printers

**Type:** lesson

A 3D printer is a motion system that places a nozzle, a light beam, or a powder layer at each point of a part, one layer at a time. Its accuracy comes from the drive ratio of its axes, the stiffness of its frame, and how well it controls heat. An engineer who designs, buys, or repairs a printer needs the mechanics and the thermal balance, not only the printed shape.

**Prerequisites:** [Additive manufacturing](../../manufacturing/04-additive-manufacturing.md), [Brushless and stepper motors](../electrical/02-brushless-and-stepper-motors.md), [Heat transfer](../../physics/12-heat-transfer.md), [Mechatronics](../electronics/06-mechatronics.md)
**Time:** 8-10 h

## Core ideas

### How it works

The controller reads a file of moves, and it turns each move into step pulses for the stepper motors. Each step moves an axis by a fixed distance set by the drive ratio, so the position is always a count of steps. Heaters run on a separate feedback loop. A temperature sensor reads the nozzle or bed, and the controller adjusts the heater power to hold a set point.

A single move passes through these steps:

1. The controller reads the next move and computes the target position for each axis.
2. It converts the distance into a count of steps for each motor, at a step rate set by the speed.
3. The motor drivers energize the motor coils in sequence, so the rotor steps. Microstepping splits each full step into smaller steps.
4. Belts, lead screws, or rods carry the motion to the toolhead or the bed.
5. A thermistor reads the temperature, and the controller sets heater power from that reading.

### Main parts

- **Frame:** an aluminum or steel frame holds the axes in place. Flex in the frame shows as ringing and as misalignment between layers.
- **Belts and pulleys:** toothed belts, usually with a 2 mm pitch, drive the $\mathrm{XY}$ axes. Each pulley turns a fixed length of belt per revolution.
- **Lead screws:** a threaded rod drives the $Z$ axis, which lifts the bed or the toolhead.
- **Stepper motors and drivers:** steppers are open loop. They count steps without feedback and can lose steps under heavy load or fast acceleration.
- **Toolhead (fused deposition):** an extruder motor drives filament through a gear. A heater cartridge in the hotend melts the filament before it leaves the nozzle.
- **Bed:** a heated plate with its own sensor and heater. It holds the part at a steady temperature during the build.
- **Light path (resin printers):** a galvanometer mirror or a projector directs light onto a resin vat. A $Z$ stage lifts the part out of the vat one layer at a time.
- **Powder system (powder bed printers):** a build piston lowers one layer at a time. A roller spreads powder across the bed, and a chamber heater holds the build area warm.

### Variants

- **Cartesian:** separate motors drive $X$, $Y$, and $Z$. The bed or a gantry carries the motion.
- **CoreXY:** two motors drive two separate belts that cross, and the toolhead moves in $\mathrm{XY}$. The moving mass is lower, so the toolhead accelerates faster.
- **Delta:** three arms hang from a fixed top plate. The moving parts are light, and the build volume is cylindrical.
- **Resin printers:** a $Z$ stage moves in a vat of liquid resin. Light from a laser or a projector cures each layer.
- **Powder bed printers:** an enclosed chamber holds a build piston and powder. These printers suit metal and nylon parts.

## Key equations

Linear travel per microstep on a belt drive, with belt pitch $p$ in metres (m), pulley teeth $z$ (dimensionless), full steps per revolution $n_s$ (dimensionless), and microsteps per full step $m$ (dimensionless):

$$\delta x = \frac{p\, z}{n_s\, m}$$

Assumptions: the belt does not stretch or slip, the pulley meshes on every tooth, and the motor takes exact steps.

Linear travel per microstep on a lead screw of lead $L$ in metres (m), using the same $n_s$ and $m$:

$$\delta z = \frac{L}{n_s\, m}$$

Assumptions: no backlash in the nut, and no lead error along the screw.

Step rate for a commanded speed $v$ in metres per second (m/s):

$$f = \frac{v}{\delta x}$$

Here $f$ is in steps per second (Hz). Assumptions: constant speed, with acceleration ignored.

Steady heat loss from a heated surface of area $A$ in square metres (m$^2$) to air at a temperature difference $\Delta T$ in kelvin (K), with heat transfer coefficient $h$ in watts per square metre kelvin (W/(m$^2$ K)):

$$P = h A \Delta T$$

Assumptions: the surface is at a uniform temperature, the air is still, and $h$ is a typical value of about 10 W/(m$^2$ K) for natural convection. Radiation and conduction into the frame are ignored, so real losses are higher.

## Worked example

**Given:** A Cartesian printer has GT2 pulleys with 20 teeth at a pitch of $p = 0.002\ \text{m}$. Its motors have 200 full steps per revolution, run at 16 microsteps per step. The $Z$ lead screw has a lead of $L = 0.008\ \text{m}$. The toolhead moves $0.200\ \text{m}$ at $v = 0.100\ \text{m/s}$. The bed is $0.20\ \text{m}$ by $0.20\ \text{m}$ and must hold $\Delta T = 60\ \text{K}$ above room air, with $h = 10\ \text{W/(m}^2\text{K)}$.

**Find:** (a) the $\mathrm{XY}$ and $Z$ step sizes, (b) the step count and step rate for the move, and (c) the steady heat loss from the bed.

**Assumptions:** The belt does not stretch, the motor takes exact steps, acceleration is ignored, and $h$ is the typical natural-convection value above.

**Solution:**

1. Pulley circumference: $p z = 0.002 \times 20 = 0.040\ \text{m}$. Steps per revolution: $n_s m = 200 \times 16 = 3200$.
2. $\mathrm{XY}$ step: $\delta x = 0.040 / 3200 = 1.25 \times 10^{-5}\ \text{m} = 0.0125\ \text{mm}$.
3. $Z$ step: $\delta z = 0.008 / 3200 = 2.5 \times 10^{-6}\ \text{m} = 0.0025\ \text{mm}$.
4. Move: $0.200 / 1.25 \times 10^{-5} = 16\,000$ steps. Step rate: $f = 0.100 / 1.25 \times 10^{-5} = 8000\ \text{Hz}$. Move time: $0.200 / 0.100 = 2.0\ \text{s}$.
5. Bed loss: $A = 0.20 \times 0.20 = 0.040\ \text{m}^2$, so $P = 10 \times 0.040 \times 60 = 24\ \text{W}$.

**Answer:** (a) 0.0125 mm in $\mathrm{XY}$ and 0.0025 mm in $Z$. (b) 16 000 steps at 8000 Hz, taking 2.0 s. (c) 24 W at steady state.

**Sanity check:** The move takes 2.0 s and covers 16 000 steps, so the step rate is 16 000 divided by 2.0, which is 8000 Hz. The $Z$ step of 0.0025 mm is far finer than a typical layer height of 0.1 to 0.2 mm, so the mechanics of $Z$ are not the limit. The bed loss is a floor, because real heat loss to the frame and to the air is larger.

## Design trade-offs

- **Speed against ringing:** higher acceleration shakes the frame. A stiffer frame and a lighter toolhead raise the speed a printer can reach before the surface shows ripples.
- **Belt tension against backlash:** a loose belt skips and adds backlash. A tight belt loads the bearings and the motor. Belts stretch and relax after setup, so tension needs checking.
- **Frame mass against cost:** a heavy frame damps vibration, but it costs more and moves more slowly.
- **Open loop against closed loop:** a stepper with no encoder costs less. An encoder adds cost, but it catches lost steps.
- **Heater power against warm-up time:** a larger bed heater reaches temperature faster, but it draws more current and needs more protection, as the failure section explains.
- **Enclosure against access:** an enclosure holds heat for powder and resin machines, and it limits access for clearing jams and changing material.

## How it fails

- **Lost steps:** a stepper loses position when acceleration or load exceeds its torque at that speed. The sign is a shift in the part after a sharp move. Lower acceleration, correct driver current, or an encoder on the axis prevents it.
- **Belt slip or stretch:** the sign is a size error along one axis that grows with distance. Belt tension checks and a rigid belt path reduce it.
- **Frame flex and ringing:** the sign is ripples on vertical walls at regular spacing. A stiffer frame, damping, and input shaping reduce it.
- **Heater runaway:** a failed or disconnected sensor reads low, so the controller keeps the heater on. Firmware thermal runaway detection, a thermal fuse, and a hard limit on heater power stop it.
- **Warped bed:** uneven heating bends the bed. The sign is a first layer that is not level across the plate. Insulation and a flat, stiff bed reduce it.
- **Hot and dusty chambers:** powder bed printers run hot and throw fine dust. An enclosure, interlocks on the lid, and extraction protect the operator.

**Safety controls, in order of preference:**

1. Elimination: avoid the hazard. For example, use a sealed printer so no operator contacts the hot bed.
2. Substitution: use a lower-temperature material or a lower-power heater where the process allows.
3. Engineering controls: thermal runaway detection, thermal fuses, enclosure interlocks, and filtered extraction.
4. Administrative controls: a written start-up check, a rule against leaving a heater unattended, and a dust-cleaning schedule.
5. Personal protective equipment: gloves for handling hot parts, and a respirator or filter where the process releases fine particles.

**Lockout and tagout for service:** before any work on the axes, heaters, or powder chamber, turn off the printer at its supply. Lock the switch with a personal lock, attach a tag with the name of the person working, and confirm the machine does not start by trying the controls. Discharge stored energy, such as a raised $Z$ stage or a hot heater, and wait for the bed to cool. Remove the lock only after the person who placed it is finished.

## History

Chuck Hull received a patent in 1986 for stereolithography, a process that cures liquid resin layer by layer, and he co-founded 3D Systems. S. Scott Crump invented fused deposition modeling and co-founded Stratasys around 1989. Carl Deckard developed selective laser sintering at the University of Texas at Austin in the late 1980s. In 2005, Adrian Bowyer at the University of Bath began the RepRap project, which made low-cost, open-source printers that could print many of their own parts.

## Practice

1. A GT2 pulley has 20 teeth at a 2 mm pitch. The motor has 200 full steps per revolution and runs at 16 microsteps. How many steps per revolution does the motor take, and how far does the belt move per microstep?
2. The same printer's $Z$ lead screw has an 8 mm lead. How far does the $Z$ axis move per microstep?
3. A bed of $0.30\ \text{m} \times 0.30\ \text{m}$ holds $70\ \text{K}$ above room air, with $h = 10\ \text{W/(m}^2\text{K)}$. What is the steady heat loss in watts?
4. The toolhead moves at $0.050\ \text{m/s}$ on the $\mathrm{XY}$ axes that step $0.0125\ \text{mm}$. What is the step rate in hertz?
5. Short answer: the $Z$ step is far finer than the layer height. What limits the accuracy of the part instead?

<details><summary>Answers</summary>

1. $200 \times 16 = 3200$ steps per revolution. The belt moves $0.040 / 3200 = 0.0125$ mm per microstep.
2. $0.008 / 3200 = 0.0025$ mm per microstep.
3. $A = 0.09\ \text{m}^2$, so $P = 10 \times 0.09 \times 70 = 63$ W.
4. $0.050 / 1.25 \times 10^{-5} = 4000$ Hz.
5. Frame flex, belt stretch, backlash, and vibration at speed limit the accuracy. Each of these adds error that a finer step cannot remove.

</details>

## Common mistakes

- Reading steps per millimetre as accuracy. The step count is cheap to improve. Flex, backlash, and belt stretch set the accuracy of the part.
- Leaving the microstep setting in firmware different from the driver setting. The mismatch scales every move by the ratio of the two values.
- Trusting a heater set point without a runaway limit. A failed sensor turns a set point into a fire risk.
- Setting high acceleration on a light frame, then blaming the material for ripples.
- Assuming a belt tensioned at setup stays tensioned. Belts stretch and relax, so tension needs checking.

## Go deeper

- [NIST: Manufacturing](https://www.nist.gov/manufacturing) by NIST: national research on additive manufacturing, measurement, and machine accuracy.
- [MIT OpenCourseWare, Design and Manufacturing I (2.007)](https://ocw.mit.edu/courses/2-007-design-and-manufacturing-i-spring-2009/) by MIT: a free course on machine design and manufacturing.
- Reference sheets: [Manufacturing reference](../../manufacturing/reference.md) and [Mechanics reference](../../physics/reference-mechanics.md).
- Related lessons: [Additive manufacturing](../../manufacturing/04-additive-manufacturing.md), [Vibrations](../../physics/13-vibrations.md), and [Cutting-machine lesson: CNC machines](03-cnc-machines.md).
