# Robotics: forward kinematics and DC motor torque and speed

**Type:** lesson

A robot arm is a chain of links connected by joints. Forward kinematics answers one question. Given
the joint angles, where is the tip of the arm? A DC motor is the actuator that turns the joints,
and its torque and speed set how strong and how fast the arm can move.

**Prerequisites:** [Mechatronics](03-mechatronics.md), [Circuit basics](01-circuit-basics.md)
**Time:** 10-14 h

## Core ideas

- **Link**: a rigid bar between two joints. Its length is fixed.
- **Joint**: a point where two links meet and can rotate. A revolute joint rotates about one axis.
- **Degrees of freedom**: the number of independent joint variables. A two-link planar arm has two.
- **Forward kinematics**: the map from joint angles to the tip position. It is pure geometry, with
  no forces or motors involved.
- **Angle convention.** In a planar arm, the second joint angle is usually measured relative to the
  first link. The absolute angle of the second link is then $\theta_1 + \theta_2$.
- **DC motor**: a motor whose speed is set by its voltage and whose output torque is set by its
  current. Two constants link them: torque constant $K_t$ and back-EMF constant $K_e$.
- **Back-EMF**: a motor spinning produces a voltage opposing its supply. This is why a motor draws
  less current as it speeds up.
- **Stall**: the condition where the motor is held still. The current is at its largest and so is
  the torque.
- **Gear ratio**: a gearbox trades speed for torque. Ideal gears multiply torque and divide speed
  by the same ratio.

## Key equations

Two-link planar arm, with link lengths $L_1$ and $L_2$ in metres (m), joint angles $\theta_1$ and
$\theta_2$ in radians:

- Tip position: $x = L_1 \cos\theta_1 + L_2 \cos(\theta_1 + \theta_2)$
- Tip position: $y = L_1 \sin\theta_1 + L_2 \sin(\theta_1 + \theta_2)$

DC motor, with supply voltage $V$ in volts (V), armature resistance $R$ in ohms ($\Omega$), current $I$
in amperes (A), speed $\omega$ in radians per second (rad/s), torque $T$ in newton metres (N m):

- Voltage balance: $V = I R + K_e \omega$
- Torque: $T = K_t I$, where $K_t$ is N m/A
- Speed: $\omega = (V - I R) / K_e$, where $K_e$ is V s/rad
- Stall current: $I_{stall} = V / R$; stall torque: $T_{stall} = K_t V / R$
- Mechanical power: $P_{mech} = T \omega$, electrical input $P_{elec} = V I$

Typical values for a small motor are $K_t = K_e$ in SI units, so the two constants share one number.

## Worked example

**Given:** A two-link planar arm has $L_1 = 0.30\ \text{m}$ and $L_2 = 0.20\ \text{m}$. The joints are set
at $\theta_1 = 30^\circ$ and $\theta_2 = 45^\circ$ (relative). A DC motor drives the first joint with
$V = 12\ \text{V}$, $R = 1.5\ \Omega$, $K_t = K_e = 0.02$ (SI), and carries a load of $T = 0.05\ \text{N m}$.

**Find:** (a) the tip position $(x, y)$, (b) the motor current, speed, and mechanical output power,
and (c) the efficiency of the motor.

**Solution:**

1. Convert angles: $\theta_1 = 0.5236\ \text{rad}$, $\theta_1 + \theta_2 = 75^\circ = 1.309\ \text{rad}$.
2. (a) $x = 0.30 \cos 30^\circ + 0.20 \cos 75^\circ = 0.2598 + 0.0518 = 0.3116\ \text{m}$.
   $y = 0.30 \sin 30^\circ + 0.20 \sin 75^\circ = 0.1500 + 0.1932 = 0.3432\ \text{m}$.
   The tip is $0.4635\ \text{m}$ from the base.
3. (b) Current from torque: $I = T / K_t = 0.05 / 0.02 = 2.50\ \text{A}$.
   Speed: $\omega = (12 - 2.5 \times 1.5) / 0.02 = 8.25 / 0.02 = 412.5\ \text{rad/s}$, which is
   $3939\ \text{rpm}$.
   Mechanical output: $P_{mech} = 0.05 \times 412.5 = 20.6\ \text{W}$.
4. (c) Electrical input: $P_{elec} = 12 \times 2.5 = 30.0\ \text{W}$.
   Efficiency: $20.6 / 30.0 = 0.69$, or $69$ percent. The remaining $9.4\ \text{W}$ is $I^2 R$ heat.

**Answer:** (a) tip at $(0.312, 0.343)\ \text{m}$, distance $0.464\ \text{m}$. (b) $I = 2.50\ \text{A}$,
$\omega = 412\ \text{rad/s}$ ($3939\ \text{rpm}$), $P_{mech} = 20.6\ \text{W}$. (c) $69$ percent.

**Sanity check:** Both link lengths sum to $0.50\ \text{m}$, so the tip must lie within a $0.50\ \text{m}$
radius of the base. $0.464\ \text{m}$ is inside that limit. The efficiency loss $I^2 R = 2.5^2 \times 1.5 =
9.4\ \text{W}$ matches $30.0 - 20.6$.

## Practice

1. Two links of $0.5\ \text{m}$ each, $\theta_1 = 0$ and $\theta_2 = 90^\circ$. Find the tip $x$ and $y$.
2. The same arm with $\theta_1 = 90^\circ$ and $\theta_2 = 0$. Find the tip $x$ and $y$.
3. A $24\ \text{V}$ motor has $R = 2\ \Omega$ and $K_t = 0.05$. Find the stall torque.
4. The $12\ \text{V}$ motor of the worked example runs with no load. Find its no-load speed in rpm,
   ignoring friction.
5. The motor of the worked example draws $4.0\ \text{A}$. Find its torque.

<details><summary>Answers</summary>

1. $x = 0.500\ \text{m}$, $y = 0.500\ \text{m}$
2. $x = 0.000\ \text{m}$, $y = 1.000\ \text{m}$
3. $0.60\ \text{N m}$
4. $5730\ \text{rpm}$
5. $0.080\ \text{N m}$

</details>

## Common mistakes

- Using degrees inside a sine or cosine that expects radians. Check the calculator mode before you
  compute.
- Adding $\theta_2$ to $\theta_1$ when the joint angle is defined as absolute. Read the convention for
  your arm first.
- Forgetting back-EMF. Using $V / R$ for the running current gives a stall-level current, which is far
  too high.
- Mixing up $K_t$ and $K_e$. Torque uses $K_t$ with current, and speed uses $K_e$ with voltage.
- Assuming a motor's full rated torque is available at full speed. Torque falls as speed rises, so the
  usable operating point is a trade-off.

## Go deeper

- [Robotics, Wikibooks](https://en.wikibooks.org/wiki/Robotics) by Wikibooks contributors: an open
  introduction to robot structure, sensing, and control.
- [Circuits and Electronics (6.002), MIT OpenCourseWare](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/)
  by MIT: the circuit model behind motor drive and power electronics.
- For trigonometry and vectors, which the arm geometry uses, see the [math folder](../math/README.md).
- Previous: [Lesson 03, mechatronics](03-mechatronics.md).
- Next: [Lesson 05, thermal systems](05-thermal-systems.md).
