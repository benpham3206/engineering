# Rotorcraft and drones

**Type:** lesson

A rotorcraft lifts itself by spinning blades that push air down, so it can hover and fly at low speed. An engineer sizes the rotor from the hover power, which momentum theory predicts, and designs the control system that keeps the craft stable.

**Prerequisites:** [Hydrostatics and Bernoulli](../../physics/10-hydrostatics-and-bernoulli.md), [Particle dynamics](../../physics/02-particle-dynamics.md), [Feedback control](../../physics/14-controls.md)
**Time:** 6-8 h

## Core ideas

### How it works

A rotor is a set of spinning blades, each acting as a rotating wing. The blades turn air, and the air pushes back on them, which is thrust. In hover, thrust equals weight.

Momentum theory treats the rotor as an actuator disk, a flat disk of area $A$ that adds momentum to the air passing through it. Air enters the disk from above at almost zero speed and leaves below it at a higher speed. The disk adds a velocity $v_i$ to the air at the disk. Far below the rotor, the wake speed reaches $2v_i$. Momentum conservation links the thrust to this wake speed. Energy conservation links the power to the same speed. The result is a simple formula for the least power a rotor of a given size can use to make a given thrust.

A rotor with a large disk area moves a large mass of air slowly. A small rotor moves a small mass of air fast. Moving air slowly costs less power for the same thrust, so large rotors are more efficient than small ones. This is the core trade-off in rotorcraft design.

Forward flight changes the picture. At higher speed, the air arrives at the disk from the front, and the induced power falls. Profile and parasite drag rise with speed, so total power has a minimum at some moderate forward speed.

### Main parts

- **Rotor blades.** Airfoil sections that generate thrust. Blade pitch, twist, and tip shape set the thrust and the noise.
- **Hub and swashplate.** The hub holds the blades. On a helicopter, the swashplate changes the blade pitch with each blade's position in its rotation.
- **Mast and transmission.** Carry the engine's torque to the rotor. A gearbox sets the rotor speed.
- **Tail rotor or anti-torque system.** On a single-rotor helicopter, the tail rotor cancels the torque that the main rotor puts on the fuselage.
- **Motors and electronic speed controllers.** On a drone, each rotor has its own brushless motor and an electronic speed controller that sets the motor speed.
- **Flight controller.** Reads the gyroscopes and accelerometers, runs control loops, and sends speed commands to the motors.
- **Battery.** Stores the energy for hover, and its mass adds to the weight the rotors must lift.

### Variants

- **Single-rotor helicopter.** One main rotor and a tail rotor. Collective pitch sets the thrust, and cyclic pitch tilts the thrust to move the craft forward, sideways, or back.
- **Coaxial helicopter.** Two rotors on one mast turn in opposite directions, so the torques cancel without a tail rotor.
- **Tandem helicopter.** Two rotors, one at each end of the fuselage, with opposite torques. The Boeing CH-47 Chinook is a tandem design.
- **Tiltrotor.** Rotors on wing tips that tilt from vertical for hover to horizontal for fast forward flight. The Bell-Boeing V-22 Osprey is an example.
- **Autogyro.** A rotor that spins from the airflow, with a separate propeller for forward thrust. It does not hover.
- **Multirotor drone.** Four, six, or eight rotors with fixed pitch. Speed changes give control. Quadcopters are the most common.

## Key equations

Momentum theory for a rotor in hover. Here $\rho$ is air density, $A$ is the disk area, and $v_i$ is the induced velocity at the disk.

$$
T = 2\rho A v_i^2 \qquad v_h = \sqrt{\frac{T}{2\rho A}} \qquad P_{\text{ideal}} = T v_h = \frac{T^{3/2}}{\sqrt{2\rho A}}
$$

- $T$ is thrust (N), which equals weight in hover. $\rho$ is air density (kg/m$^3$, about 1.225 at sea level on Earth). $A$ is the total rotor disk area (m$^2$). $v_h$ is the hover induced velocity (m/s). $P_{\text{ideal}}$ is the ideal induced power (W), the least power that the rotor can use for this thrust.
- Assumptions: ideal actuator disk, uniform inflow across the disk, hover (no forward or vertical speed), steady and incompressible flow, air at rest far upstream, and no profile drag, swirl, or tip losses. Real rotors need more power than $P_{\text{ideal}}$.

Actual shaft power with a figure of merit $FM$, a measure of how close the rotor comes to the ideal.

$$
P = \frac{P_{\text{ideal}}}{FM}
$$

- $FM$ is the figure of merit (dimensionless). Well-designed helicopter rotors reach about 0.7 to 0.8 (typical values). Small drone rotors often reach 0.5 to 0.7 (typical values).
- Assumptions: $FM$ is a single empirical factor, assumed constant over the hover condition, that lumps together the profile drag, swirl, and tip losses that the ideal model omits. Its value must come from measurement or a more detailed model.

Disk loading, the thrust per unit disk area, which sets the hover power.

$$
\frac{T}{A} \quad \text{(N/m}^2\text{)}
$$

- Assumptions: thrust spread uniformly over the disk area $A$. Disk loading is a design ratio, not a measured quantity.

Thrust in a multirotor. Each rotor makes thrust proportional to the square of its speed. Here $k_T$ is a thrust coefficient.

$$
T_{\text{rotor}} = k_T \omega^2
$$

- $\omega$ is rotor angular speed (rad/s). $k_T$ is the thrust coefficient (N s$^2$/rad$^2$), set by blade shape and air density.
- Assumptions: $k_T$ is constant over the operating range, which holds at low forward speed and in hover. Inflow effects, stall, and compressibility at high tip speed break this relation.

## Worked example

**Given.** A 2.0 kg quadcopter has four rotors, each 0.254 m in diameter, so each has radius $R = 0.127$ m. It hovers at sea level on Earth, where $\rho = 1.225$ kg/m$^3$. Assume $FM = 0.70$.

**Find.** (a) the thrust needed, (b) the total disk area and disk loading, (c) the ideal hover power and the shaft power, and (d) the power per rotor.

**Assumptions.** The four rotors act as independent disks with no interference. The air is at rest far above the craft. Electrical losses in the motors and controllers are not included.

**Solution.**

1. Thrust equals weight: $T = mg = 2.0 \times 9.80665 = 19.61$ N.
2. Total disk area: $A = 4\pi R^2 = 4\pi (0.127)^2 = 0.2027$ m$^2$. Disk loading: $T/A = 19.61 / 0.2027 = 96.8$ N/m$^2$.
3. Hover induced velocity:
$$
v_h = \sqrt{\frac{19.61}{2 \times 1.225 \times 0.2027}} = 6.28\ \text{m/s}
$$
4. Ideal power, using either form:
$$
P_{\text{ideal}} = T v_h = 19.61 \times 6.28 = 123\ \text{W}
$$
The shaft power at $FM = 0.70$ is $P = 123 / 0.70 = 176$ W.
5. Power per rotor: $176 / 4 = 44$ W.

**Answer.** (a) $T = 19.6$ N. (b) $A = 0.203$ m$^2$ and $T/A = 96.8$ N/m$^2$. (c) $P_{\text{ideal}} = 123$ W and shaft power $P = 176$ W. (d) About 44 W per rotor.

**Sanity check.** The shaft power of 176 W is in the range of small quadcopters with a few hundred grams of payload. Battery input power is higher, because motor and controller losses add to it. Doubling the mass would multiply the ideal power by $2^{1.5} = 2.83$, so a heavier drone costs much more power, not just proportionally more.

## Design trade-offs

- **Rotor size.** A bigger rotor lowers the disk loading and the hover power for the same weight. A helicopter with a 10 m rotor and 1000 kg mass has an ideal hover power of about 70 kW. Helicopter rotors are large for this reason. Drones with small props are limited by the power they can carry in the battery.
- **Mass and power.** Power scales with $T^{3/2}$, so every kilogram of battery or payload costs more than the last. Drone designers trade battery energy against weight, and the flight time often falls faster than the battery mass grows.
- **Rotor speed.** Tip speed sets noise, and blade stall sets the limit. Helicopters run the rotor at a fixed speed, and drones change the rotor speed for control. Thrust rises with the square of speed, so a 10 percent speed increase gives about 21 percent more thrust.
- **Number of rotors.** More rotors give redundancy and smaller individual props, but each extra rotor adds weight, control complexity, and interference between rotors.
- **Mechanical versus electric control.** A helicopter's swashplate and collective pitch control give fast, strong control and need heavy mechanical parts. A quadcopter's control by speed alone is simpler, but the speed changes are slower and the motors must respond quickly.

## How it fails

- **Vortex ring state.** A rotor that descends fast at low forward speed sinks into its own downwash. The thrust drops, and the craft can descend faster as the pilot adds power. Warning signs include high sink rate and buffeting. Pilots avoid this by moving forward or descending slowly.
- **Retreating blade stall.** At high forward speed and high gross weight, the blade on the retreating side meets the air at a low speed and high angle, so it stalls. Helicopters limit the speed and weight to keep the margin.
- **Loss of tail rotor effectiveness.** In some conditions, the tail rotor loses thrust, and the fuselage starts to yaw. Pilots respond by changing the power and the heading.
- **Autorotation.** After an engine failure, the rotor keeps turning from the upward airflow through the disk. The pilot trades rotor speed and altitude for a landing. Autorotation is a safety measure, and training practices it often.
- **Drone motor or controller failure.** A motor or electronic speed controller fault drops one rotor's thrust, and the craft flips unless it has redundancy. Hexacopters and octocopters can often land after one motor fails. Flight controllers use failsafe modes such as return-to-home and emergency landing.
- **Battery sag.** A battery under heavy current drops in voltage, so the motors cannot reach the commanded speed. Battery monitoring and low-voltage cutoffs protect against this.

## History

Juan de la Cierva developed the autogiro in Spain, and its first successful flight came in 1923. Momentum theory for propellers was worked out in the nineteenth century by William Rankine and Robert Froude. Igor Sikorsky flew the VS-300 in 1939, a single-rotor helicopter with a tail rotor that became the model for practical helicopters. Multirotor drones became common in the 2010s, after small brushless motors, lithium polymer batteries, and cheap flight controllers spread.

## Practice

1. A quadcopter has a mass of 1.5 kg and is in hover at sea level. Find the thrust needed in N.
2. The same 1.5 kg quadcopter has four rotors of 0.254 m diameter. Find the hover induced velocity in m/s, using $\rho = 1.225$ kg/m$^3$.
3. Find the ideal hover power for the 1.5 kg quadcopter in W.
4. A rotor's thrust doubles at the same disk area. Find the factor by which the ideal hover power increases.
5. A rotor speeds up by 10 percent, and thrust rises with $\omega^2$. Find the percentage increase in thrust.

<details><summary>Answers</summary>

1. $T = 1.5 \times 9.80665 = 14.7$ N
2. $v_h = \sqrt{14.71 / (2 \times 1.225 \times 0.2027)} = 5.44$ m/s
3. $P_{\text{ideal}} = 14.71 \times 5.44 = 80.1$ W
4. $2^{1.5} = 2.83$
5. $1.10^2 = 1.21$, so thrust rises by 21 percent

</details>

## Common mistakes

- Using momentum theory with the disk diameter where the radius is needed. The disk area is $\pi R^2$ per rotor, so a diameter in the formula must be halved first.
- Forgetting that the figure of merit must divide the ideal power to get the shaft power. The ideal value is always a lower bound.
- Treating the hover power as proportional to weight. Power scales with weight to the 1.5 power, so a heavier craft needs disproportionately more power.
- Assuming a drone's motors can run at full speed for the whole flight. The battery voltage sag and the thermal limits of the motors cut the available power.
- Confusing a helicopter's collective and cyclic controls. Collective changes thrust for all blades together, and cyclic tilts the thrust by changing each blade's pitch as it turns.

## Go deeper

- [What is thrust?](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/what-is-thrust/) by NASA Glenn Research Center: how a rotor or engine produces force by pushing air or gas backward.
- [Unified Engineering I, II, III, and IV (16.01)](https://ocw.mit.edu/courses/16-01-unified-engineering-i-ii-iii-iv-fall-2005-spring-2006/) by MIT OpenCourseWare: fluid mechanics and propulsion, with lecture notes.
- [Bernoulli's equation](https://www.grc.nasa.gov/www/k-12/airplane/bern.html) by NASA Glenn Research Center: the pressure and speed relation that underlies blade lift.
- Reference sheets: [Mechanics reference](../../physics/reference-mechanics.md) and [Thermofluids reference](../../physics/reference-thermofluids.md).
- Related lessons: [Aircraft and wings](05-aircraft-and-wings.md), [Rockets](07-rockets.md), [Batteries](../electrical/06-batteries.md), [Brushless and stepper motors](../electrical/02-brushless-and-stepper-motors.md), and [Controls](../../physics/14-controls.md).
