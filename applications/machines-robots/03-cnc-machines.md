# CNC machines

**Type:** lesson

A CNC machine moves a cutting tool or a workpiece along straight and rotary axes, each driven by a motor under closed-loop or open-loop control. Its accuracy comes from the machine itself: the stiffness of the structure, the lead of the screws, the resolution of the feedback, and how well the controller holds each axis on its path. An engineer who buys, programs, or repairs a machine tool must know which of these limits the result.

**Prerequisites:** [Machining processes](../../manufacturing/03-machining-processes.md), [Mechatronics](../electronics/06-mechatronics.md), [DC motors](../electrical/01-dc-motors.md), [Brushless and stepper motors](../electrical/02-brushless-and-stepper-motors.md)
**Time:** 8-10 h

## Core ideas

### How it works

Each axis has a motor, a drive that sends current to the motor, a transmission that turns rotation into straight-line motion, and a feedback device that reports the position. The controller compares the commanded position with the measured position, computes the error, and corrects the drive. On a modern machine this loop runs thousands of times per second.

Each move in a program passes through these steps:

1. The controller reads the next program block and computes the position of each axis at the next interpolation point.
2. The position loop subtracts the feedback position from the command and outputs a velocity command.
3. The velocity loop and current loop drive the motor current that produces the required torque.
4. The motor turns the ball screw, and the nut moves the table.
5. The encoder reports the motor rotation, or a linear scale reports the table position, back to the controller.

### Main parts

- **Structure:** the bed, column, saddle, and table carry the cutting loads. Stiffness decides how far the tool deflects under cutting force. Cast iron is common for beds because it damps vibration well.
- **Linear guides:** rails and carriages, usually recirculating-ball types, carry each axis with low friction and little play.
- **Ball screw:** a screw and nut with balls between them. It turns rotation into travel with low friction. The lead is the travel per revolution.
- **Drives and motors:** servo motors with encoders on the shaft are the usual choice for production machines. Stepper motors appear on lower-cost machines.
- **Feedback:** a rotary encoder on the motor gives semi-closed-loop control, so screw stretch and pitch error stay outside the loop. A linear glass scale on the table gives closed-loop control, so the scale measures the table directly.
- **Controller:** it reads G-code, interpolates the path between points, and runs the loops for every axis.
- **Spindle:** a separate drive with its own speed control turns the cutter or the workpiece.

### Variants

- **Knee mill or bed mill:** the table moves in X and Y, and the head or knee moves in Z.
- **Gantry mill:** a bridge moves over a fixed bed. It suits large parts.
- **Machining center:** a mill with an automatic tool changer.
- **CNC lathe:** two linear axes, Z along the spindle and X across it. The spindle is the rotary axis.
- **Five-axis machine:** two rotary axes added to the three linear axes. The rotary axes sit on the table (trunnion type) or in the head. They change the tool orientation.

## Key equations

Travel per second for a lead screw turning at $N$ revolutions per second (rev/s), with lead $L$ in metres (m):

$$v = N L$$

Position resolution of a feedback device that gives $n_c$ counts per revolution (dimensionless):

$$\delta x = \frac{L}{n_c}$$

Torque at the motor to push an axial force $F$ in newtons (N) through a ball screw of efficiency $\eta$ (dimensionless, about 0.9 for a ball screw):

$$T = \frac{F L}{2 \pi \eta}$$

Here $T$ is in newton metres (N m). Acceleration torque is extra, and it comes from the inertia of the moving parts.

Mechanical power at the shaft, with angular speed $\omega$ in radians per second (rad/s):

$$P = T \omega, \qquad \omega = 2 \pi N$$

Thermal growth of a steel member of length $L_0$ in metres (m) when its temperature rises by $\Delta T$ in kelvin (K), with linear expansion coefficient $\alpha$ of about $11.7 \times 10^{-6}$ per K for carbon steel (typical):

$$\Delta L = \alpha L_0 \Delta T$$

## Worked example

**Given:** The X axis has a ball screw with lead $L = 0.010\ \text{m}$. A servo encoder gives $n_c = 10\,000$ counts per revolution after quadrature decoding, and the motor drives the screw directly (1:1). The cutting force along X is $F = 1500\ \text{N}$, the screw efficiency is $\eta = 0.90$, and the feed speed is $v = 0.050\ \text{m/s}$ (3000 mm/min).

**Find:** (a) the position resolution, (b) the motor speed, (c) the torque, and (d) the mechanical power.

**Assumptions:** Steady cutting at constant feed. Acceleration torque is ignored here.

**Solution:**

1. Resolution: $\delta x = \dfrac{0.010}{10\,000} = 1.0 \times 10^{-6}\ \text{m} = 1\ \mu\text{m}$.
2. Speed: $N = \dfrac{v}{L} = \dfrac{0.050}{0.010} = 5.0\ \text{rev/s} = 300\ \text{rpm}$. Angular speed $\omega = 2\pi \times 5.0 = 31.4\ \text{rad/s}$.
3. Torque: $T = \dfrac{1500 \times 0.010}{2\pi \times 0.90} = 2.65\ \text{N m}$.
4. Power: $P = T \omega = 2.65 \times 31.4 = 83\ \text{W}$.

**Answer:** (a) $1\ \mu\text{m}$ per count. (b) 300 rpm. (c) 2.65 N m. (d) 83 W at this load.

**Sanity check:** The power check agrees with the torque and speed. A servo motor with a continuous torque rating well above 2.65 N m, plus margin for acceleration, is the right size. The 1 $\mu$m resolution is not the accuracy of the axis. Pitch error, backlash, and thermal growth add to it, as the next sections show.

## Design trade-offs

- **Stiffness against mass:** a heavy casting resists deflection and damps vibration. It also needs larger drives and limits acceleration. A frame that deflects 10 $\mu$m under 1500 N has a stiffness of 150 N/$\mu$m, or 150 kN/mm.
- **Screw lead:** torque scales with lead, so a small lead needs less motor torque for the same force. A large lead gives more travel per revolution and more speed at a low motor speed, but it lowers the resolution per count for a given encoder.
- **Stepper against servo:** a stepper is cheaper and holds position without feedback. It loses steps when the load exceeds its torque at that speed. A servo costs more and corrects position errors as they happen.
- **Ball screw against linear motor:** a ball screw is cheap and has high force, but it wears and has limited speed. A linear motor drives the table directly with no screw wear. It needs more magnet material and cooling.
- **Thermal growth:** a 2 m steel axis grows about 0.023 mm for each kelvin of rise. Machines need a warm-up cycle, and compensation tables help where the temperature changes.

## How it fails

- **Backlash:** a gap in the nut or gearing lets the table move before the screw does. The sign is a position error that flips when the direction reverses. Preloaded nuts, linear scales, and backlash compensation in the controller reduce it.
- **Lost steps:** a stepper loses position when the load exceeds its torque at the current speed. The sign is a position shift after a heavy cut. A servo with an encoder detects the error and corrects it, and a stall alarm stops the axis.
- **Thermal drift:** parts and frames grow as the machine warms. The sign is that the first part measures differently from the fifth. A warm-up cycle and temperature sensors on the frame help.
- **Servo oscillation:** loop gains set too high for the structure's resonance make the axis hum or shake at a fixed frequency. Gain tuning and notch filters fix it.
- **Pitch error and screw wear:** the screw's lead varies along its length. The sign is a periodic error along the axis. Laser calibration produces an error map, which the controller uses to correct position.
- **Overtravel:** an axis that runs past its end stops can strike the frame. Limit switches, software travel limits, and an emergency stop protect the machine and operator.

## History

Numerical control grew out of work at the MIT Servomechanisms Laboratory. Around 1952, a team there demonstrated a vertical milling machine that followed a program on punched tape to move along its axes. The project was carried out with Parsons Corporation, which had proposed positioning machine tools from punched cards. Through the 1950s and 1960s, control moved from tape to computers, and feedback on machine axes became standard.

## Practice

1. A ball screw has a 5 mm lead, and the encoder gives 5000 counts per revolution. What is the position resolution?
2. A stepper motor has 200 full steps per revolution and runs at 8 microsteps per full step. The drive turns an 8 mm lead screw. How many microsteps are needed per millimetre of travel?
3. A steel bed 2000 mm long rises by 4 K. How much does it grow? Use $\alpha = 11.7 \times 10^{-6}$ per K.
4. A ball screw with a 10 mm lead and efficiency 0.85 must push an axial force of 3000 N. What torque does the motor need?
5. An axis must move at 6000 mm/min on the 10 mm lead screw. What is the motor speed in rpm?

<details><summary>Answers</summary>

1. $\delta x = 0.005 / 5000 = 1.0 \times 10^{-6}$ m, which is 0.001 mm.
2. $200 \times 8 = 1600$ microsteps per revolution. Over an 8 mm lead, that is 200 microsteps per mm.
3. $\Delta L = 11.7 \times 10^{-6} \times 2.000 \times 4 = 9.36 \times 10^{-5}$ m, which is 0.094 mm.
4. $T = (3000 \times 0.010)/(2\pi \times 0.85) = 5.62$ N m.
5. $6000$ mm/min is $0.100$ m/s, so $N = 0.100/0.010 = 10$ rev/s, which is 600 rpm.

</details>

## Common mistakes

- Equating position resolution with accuracy. A fine encoder does not correct a screw with a 0.02 mm pitch error. The accuracy test uses a laser or a calibrated artefact, under ISO 230-2 (the test code for positioning accuracy of machine tools).
- Sizing the drive for cutting force alone. Accelerating the table and the screw takes torque too, and that can exceed the cutting torque.
- Leaving out thermal growth on a long axis. A 2 m steel axis grows about 0.023 mm for each kelvin.
- Forgetting the microstep setting on a stepper drive. A wrong setting scales every move by the ratio of the two values.
- Placing the measuring scale far from the tool tip. When the table tilts, the error at the tool is the tilt times the offset (the Abbe error).

## Go deeper

- [MIT OpenCourseWare, Design and Manufacturing I (2.007)](https://ocw.mit.edu/courses/2-007-design-and-manufacturing-i-spring-2009/) by MIT: a free course on machine design and manufacturing.
- [NIST: Manufacturing](https://www.nist.gov/manufacturing) by NIST: national work on measurement and machine tool accuracy.
- [Machining speeds and feeds](../../manufacturing/02-machining-speeds-and-feeds.md) and [Tolerances, fits, and finish](../../manufacturing/08-tolerances-fits-finish.md): the process side of accuracy.
- [Lead screws and ball screws](../power-transmission/08-lead-screws-and-ball-screws.md) and [Robot arms](01-robot-arms.md): the same drive and kinematics ideas in other machines.
