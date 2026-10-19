# Robot arms

**Type:** lesson

A robot arm is a chain of links and joints that moves a tool to a point in space. Engineers use its kinematics to find where the tool goes, and its statics and dynamics to size the motors, gears, and structure that move it.

**Prerequisites:** [Trigonometry](../../math/02-trigonometry.md), [Linear algebra](../../math/05-linear-algebra.md), [Rigid body dynamics](../../physics/03-rigid-body-dynamics.md), [Mechatronics](../electronics/06-mechatronics.md), [Single-variable calculus](../../math/03-single-variable-calculus.md)
**Time:** 12-16 h

## Core ideas

### How it works

A serial manipulator is a chain of rigid links joined by joints. One end, the base, is fixed. The other end carries the tool. Each joint adds one degree of freedom. A tool that must reach any position and orientation in space needs six degrees of freedom.

Forward kinematics turns joint values into a tool pose. It is pure geometry, with no forces. Inverse kinematics runs the other way. Given a target pose, it finds joint values that reach it. A planar arm with two links has at most two solutions for a reachable point. The two solutions are called elbow-up and elbow-down.

The Jacobian links joint speeds to tool speed. Controllers use it to move the tool in a straight line. It also links joint torques to the force at the tool. A tool force $\mathbf{F}$ needs joint torques $\boldsymbol{\tau} = J^{T}\mathbf{F}$ to hold it still. Gravity and the payload create these static torques at every joint, and the motors must supply them.

### Main parts

- Links are rigid bars. Their stiffness decides how much the tip sags under load.
- Revolute joints (R) rotate about one axis. Prismatic joints (P) slide along one axis. Most industrial arms use revolute joints.
- Actuators are usually servo motors with an encoder, followed by a gearbox. Planetary gearboxes, harmonic drives, and cycloidal drives are common at the joints.
- Encoders on the motor side and often on the output side measure each joint angle.
- The end effector is the tool at the tip: a gripper, a vacuum cup, a welding torch, or a spindle.

### Variants

- Cartesian (gantry) arms use three prismatic joints in a rectangular frame. They are rigid and simple to model, but they fill a box-shaped workspace.
- Cylindrical arms use one rotation and two linear motions.
- SCARA arms use two parallel revolute joints and one vertical prismatic joint. They are stiff in the vertical direction, which suits pick-and-place assembly.
- Articulated arms use three or more revolute joints. They have the largest workspace for their footprint and are the most common industrial type.
- Parallel (delta) robots drive one platform through several arms that share a base. Their moving mass is small, so they are fast for light parts.

## Key equations

Symbols: $L_1$, $L_2$ are link lengths (m). $\theta_1$, $\theta_2$ are joint angles (rad). $(x, y)$ is the tip position (m). $m_1$, $m_2$ are link masses (kg). $m_p$ is the payload mass (kg). $g$ is the local gravitational acceleration ($9.81\ \text{m}/\text{s}^2$ at Earth's surface). $\tau$ is joint torque (N m). $N$ is the gear ratio (dimensionless). $\eta$ is gearbox efficiency (dimensionless). $\omega$ is angular speed (rad/s).

Forward kinematics for a planar two-link arm. Assumes rigid links of fixed length, two revolute joints, and a base at the origin:

$$x = L_1 \cos\theta_1 + L_2 \cos(\theta_1 + \theta_2), \qquad y = L_1 \sin\theta_1 + L_2 \sin(\theta_1 + \theta_2)$$

Inverse kinematics, with $r^2 = x^2 + y^2$:

$$\cos\theta_2 = \frac{x^2 + y^2 - L_1^2 - L_2^2}{2 L_1 L_2}, \qquad \theta_1 = \operatorname{atan2}(y, x) - \operatorname{atan2}\big(L_2 \sin\theta_2,\; L_1 + L_2 \cos\theta_2\big)$$

A positive $\theta_2$ and a negative $\theta_2$ give the elbow-down and elbow-up solutions. A reachable point needs $|L_1 - L_2| \le r \le L_1 + L_2$. Assumes the same planar model as above, with $\operatorname{atan2}$ taking the quadrant of $(x, y)$ into account.

Jacobian, which maps $\dot\theta$ (rad/s) to tip velocity (m/s):

$$J = \begin{bmatrix} -L_1 \sin\theta_1 - L_2 \sin(\theta_1+\theta_2) & -L_2 \sin(\theta_1+\theta_2) \\ L_1 \cos\theta_1 + L_2 \cos(\theta_1+\theta_2) & L_2 \cos(\theta_1+\theta_2) \end{bmatrix}, \qquad \det J = L_1 L_2 \sin\theta_2$$

The arm is singular where $\det J = 0$, which means $\theta_2 = 0$ or $\pi$. Near a singularity, a small tip speed needs very large joint speeds. Assumes the planar model above, with joint speeds as the only inputs and no joint limits applied.

Gravity torque for the arm in a vertical plane, with a horizontal shoulder axis:

$$\tau_1 = g\Big[m_1 \tfrac{L_1}{2}\cos\theta_1 + m_2\big(L_1\cos\theta_1 + \tfrac{L_2}{2}\cos(\theta_1+\theta_2)\big) + m_p\big(L_1\cos\theta_1 + L_2\cos(\theta_1+\theta_2)\big)\Big]$$

$$\tau_2 = g\Big[m_2 \tfrac{L_2}{2}\cos(\theta_1+\theta_2) + m_p L_2 \cos(\theta_1+\theta_2)\Big]$$

Each term is a mass times $g$ times its horizontal distance from the joint, in N m. Assumes static equilibrium (no acceleration, no friction), uniform links with centres at their midpoints, a point payload at the tip, and a horizontal shoulder axis so gravity acts in the arm's plane.

Motor and gearbox, for a joint with output torque $\tau_{\mathrm{joint}}$ (N m) and output speed $\omega_{\mathrm{joint}}$ (rad/s). Assumes a constant efficiency $\eta$ over the operating range and ignores gearbox inertia, backlash, and motor back-EMF losses:

$$\tau_{\mathrm{motor}} = \frac{\tau_{\mathrm{joint}}}{N\,\eta}, \qquad \omega_{\mathrm{motor}} = N\,\omega_{\mathrm{joint}}$$

Backlash of angle $\Delta\theta$ (rad) at a joint with link length $L$ (m) moves the tip by about $e \approx L\,\Delta\theta$. Assumes the link is rigid and the small-angle approximation holds, so $\Delta\theta$ is well below 1 rad.

Denavit-Hartenberg (DH) transform between frame $i-1$ and frame $i$, with four parameters per joint: link length $a_i$ (m), link twist $\alpha_i$ (rad), link offset $d_i$ (m), and joint angle $\theta_i$ (rad):

$${}^{i-1}T_i = \begin{bmatrix} \cos\theta_i & -\sin\theta_i\cos\alpha_i & \sin\theta_i\sin\alpha_i & a_i\cos\theta_i \\ \sin\theta_i & \cos\theta_i\cos\alpha_i & -\cos\theta_i\sin\alpha_i & a_i\sin\theta_i \\ 0 & \sin\alpha_i & \cos\alpha_i & d_i \\ 0 & 0 & 0 & 1 \end{bmatrix}$$

Assumes each joint frame is set by the standard DH convention, with all four parameters defined for that joint. Multiplying the transforms from base to tip gives the tool pose. Each revolute joint varies $\theta_i$, and each prismatic joint varies $d_i$.

## Worked example

**Given:** A two-link arm in a vertical plane. $L_1 = 0.40\ \text{m}$, $L_2 = 0.30\ \text{m}$. Link masses $m_1 = 2.0\ \text{kg}$ (uniform, centre at the midpoint) and $m_2 = 1.0\ \text{kg}$. Payload $m_p = 1.5\ \text{kg}$ at the tip. The target tip point is $(0.45, 0.35)\ \text{m}$. Assumptions: static loads only, no friction, Earth surface gravity ($g = 9.81\ \text{m}/\text{s}^2$), and a horizontal shoulder axis. The gearbox ratio and efficiency are chosen in step 6.

**Find:** (a) both inverse kinematics solutions and which is elbow-up, (b) the shoulder torque at the target and in the worst pose, and (c) the motor and gearbox for the shoulder.

**Solution:**

1. Reach: $r^2 = 0.45^2 + 0.35^2 = 0.325\ \text{m}^2$, so $r = 0.5701\ \text{m}$. The limits are $0.10$ m and $0.70$ m, so the point is reachable.
2. $\cos\theta_2 = (0.325 - 0.160 - 0.090) / (2 \times 0.40 \times 0.30) = 0.3125$, so $\theta_2 = \pm 71.79^\circ$.
3. Elbow-up: $\theta_2 = -71.79^\circ$ and $\theta_1 = 67.87^\circ$. The elbow sits at $(0.151, 0.371)\ \text{m}$, above the line from base to tip.
   Elbow-down: $\theta_2 = +71.79^\circ$ and $\theta_1 = 7.88^\circ$. The elbow sits at $(0.396, 0.055)\ \text{m}$, below that line.
   Both solutions return the tip to $(0.450, 0.350)\ \text{m}$.
4. At the target, the shoulder torque is $11.05\ \text{N m}$ in elbow-up and $14.66\ \text{N m}$ in elbow-down. The elbow torque is $5.87\ \text{N m}$ in elbow-up and $1.06\ \text{N m}$ in elbow-down.
5. Worst pose: the arm is fully horizontal, so $\theta_1 = \theta_2 = 0$. The shoulder torque is $g(m_1 L_1/2 + m_2(L_1 + L_2/2) + m_p(L_1 + L_2)) = 9.81(0.40 + 0.55 + 1.05) = 9.81 \times 2.00 = 19.62\ \text{N m}$. The elbow torque there is $9.81(0.15 + 0.45) = 5.89\ \text{N m}$.
6. Sizing with a safety factor $\mathrm{SF} = 1.5$, a gear ratio $N = 50$, and efficiency $\eta = 0.80$:
   Joint torque $= 1.5 \times 19.62 = 29.43\ \text{N m}$.
   Motor torque $= 29.43 / (50 \times 0.80) = 0.736\ \text{N m}$.
   A joint speed of $60^\circ/\text{s} = 1.047\ \text{rad/s}$ needs a motor speed of $50 \times 1.047 = 52.4\ \text{rad/s}$, which is $500\ \text{rpm}$.

The Python used for steps 2 to 6:

```python
import math
g, L1, L2, m1, m2, mp = 9.81, 0.40, 0.30, 2.0, 1.0, 1.5  # g is Earth surface gravity
x, y = 0.45, 0.35
c2 = (x*x + y*y - L1**2 - L2**2) / (2*L1*L2)
t2 = math.acos(c2)
for t2s in (t2, -t2):                     # +: elbow-down, -: elbow-up
    k1, k2 = L1 + L2*math.cos(t2s), L2*math.sin(t2s)
    t1 = math.atan2(y, x) - math.atan2(k2, k1)
    tau_sh = g*(m1*L1/2*math.cos(t1) + m2*(L1*math.cos(t1) + L2/2*math.cos(t1+t2s))
                + mp*(L1*math.cos(t1) + L2*math.cos(t1+t2s)))
    print(math.degrees(t1), math.degrees(t2s), tau_sh)
tau_worst = g*(m1*L1/2 + m2*(L1 + L2/2) + mp*(L1 + L2))
print(tau_worst, tau_worst*1.5/(50*0.80))
```

**Answer:** (a) Elbow-up: $\theta_1 = 67.9^\circ$, $\theta_2 = -71.8^\circ$. Elbow-down: $\theta_1 = 7.9^\circ$, $\theta_2 = 71.8^\circ$. (b) Shoulder torque is $19.6\ \text{N m}$ in the worst pose, and $14.7\ \text{N m}$ or $11.0\ \text{N m}$ at the target depending on the solution. (c) The shoulder needs a motor delivering $0.74\ \text{N m}$ at $500\ \text{rpm}$ through a $50{:}1$ gearbox at $\eta = 0.80$.

**Sanity check:** The total mass is $4.5\ \text{kg}$, so the weight is $44.1\ \text{N}$. The mass-weighted horizontal distance is $2.00\ \text{kg m} / 4.5\ \text{kg} = 0.444\ \text{m}$. Multiplying gives $44.1 \times 0.444 = 19.6\ \text{N m}$, which matches step 5. The tip check in step 3 confirms both IK solutions.

## Design trade-offs

- Reach against stiffness and payload: the gravity torque grows with reach, and the tip sags more under load. Manufacturers quote payload at a stated reach, and the rating falls as reach grows.
- Gear ratio against speed and backlash: a higher ratio multiplies torque and lets a smaller motor work, but it slows the joint and adds gear backlash. Planetary gearboxes are stiff with high torque per volume. Harmonic drives are compact with very little backlash but are less stiff.
- Link material: steel has a stiffness of about 200 GPa and aluminium about 69 GPa. Aluminium links are lighter and cheaper but sag about three times as much for the same section.
- Backlash: a joint with $0.2^\circ$ of backlash and a $0.40$ m link moves the tip about $0.40 \times 0.0035 = 1.40\ \text{mm}$.
- Speed against accuracy: fast motions create dynamic torques and vibration that static sizing misses. Slower paths keep the error small.

## How it fails

- Singularities: near $\det J = 0$, a small tip command demands huge joint speeds and torques. Controllers limit speed and avoid singular paths.
- Overload: a payload above the rating or a reach beyond the chart raises motor current, slows the response, and increases position error. Overload torque limits and force sensing protect the arm.
- Joint brake failure: when power is cut, gravity pulls the arm down. Holding brakes on the joints prevent it.
- Gear wear: backlash grows over thousands of hours, and accuracy drops. Periodic checks and calibration catch it early.
- Link deflection: a stiff controller that assumes rigid links will miss the tip by the amount the links sag. Calibration or sensing on the output side corrects the error.
- Encoder or cable faults: a lost joint angle sends the arm to the wrong pose. Dual encoders and emergency-stop circuits limit the damage.

### Robot cell safety

Industrial robot cells follow the hierarchy of controls, in this order. Elimination removes the hazard, for example by loading parts from a conveyor outside the arm's reach so no one enters the cell. Substitution uses a lower-energy design, such as a smaller payload or a speed limit set low enough for a safe stop. Engineering controls are built into the cell: fixed guards around the envelope, interlocked gates that remove motor power when opened, light curtains or laser scanners, and safety-rated stops. Stop category 0 removes power at once, stop category 1 stops under control and then removes power, and stop category 2 stops under control and keeps power on. Administrative controls are lockout-tagout before entry, training, and written procedures. Personal protective equipment is the last layer and does not replace the others. This follows the stop-category definitions of IEC 60204-1 and the industrial robot safety requirements of ISO 10218.

## History

George Devol filed a patent for a programmable article transfer machine in 1954. The first industrial robot arm, Unimate, was installed at a General Motors plant in Ewing Township, New Jersey, in 1961. Jacques Denavit and Richard Hartenberg published their linkage notation in 1955. Victor Scheinman's Stanford arm, built around 1969, was an electric arm with six degrees of freedom that made computer control practical. Modern arms still use DH parameters or a close variant.

## Practice

Where a problem needs gravitational acceleration, use $g = 9.81\ \text{m}/\text{s}^2$ (Earth surface).

1. Two links with $L_1 = L_2 = 0.50\ \text{m}$. Find both inverse kinematics solutions for the tip at $(0.50, 0.50)\ \text{m}$.
2. A horizontal two-link arm has $L_1 = 0.30\ \text{m}$, $L_2 = 0.20\ \text{m}$, $m_1 = 1.0\ \text{kg}$, $m_2 = 0.5\ \text{kg}$, and no payload. Find the shoulder torque in the fully extended pose.
3. A joint must deliver $8.0\ \text{N m}$ at the output through a $30{:}1$ gearbox with $\eta = 0.75$. Find the motor torque.
4. A robot returns to a point within $\pm 0.05\ \text{mm}$ every time, but the average position is $0.30\ \text{mm}$ from the commanded point. Which figure is repeatability, and which is accuracy?
5. An arm has $L_1 = 0.40\ \text{m}$ and $L_2 = 0.30\ \text{m}$. Can it reach a point $0.80\ \text{m}$ from its base?

<details><summary>Answers</summary>

1. Elbow-down: $\theta_1 = 0^\circ$, $\theta_2 = 90^\circ$. Elbow-up: $\theta_1 = 90^\circ$, $\theta_2 = -90^\circ$.
2. $3.43\ \text{N m}$. The calculation is $9.81(0.15 + 0.50 \times 0.40) = 9.81 \times 0.35$.
3. $0.356\ \text{N m}$, from $8.0 / (30 \times 0.75) = 8.0 / 22.5$.
4. Repeatability is $\pm 0.05\ \text{mm}$. Accuracy is the $0.30\ \text{mm}$ offset from the command.
5. No. The maximum reach is $L_1 + L_2 = 0.70\ \text{m}$.

</details>

## Common mistakes

- Reading $\theta_2$ as an absolute angle when the arm uses the relative convention, or the reverse. Check the convention before solving.
- Sizing the shoulder for the target pose. The worst pose is usually the fully extended one.
- Using the payload mass without its lever arm. Torque is force times distance from the joint.
- Ignoring acceleration. Static torque misses the inertia torque, which can be larger than gravity during fast moves.
- Calling a tight spread of repeated points "accurate." Repeatability and accuracy are different specifications.

## Go deeper

- [Modern Robotics](https://hades.mech.northwestern.edu/index.php/Modern_Robotics) by Kevin Lynch and Frank Park. The site links free preprint PDFs of the updated first edition. It covers kinematics, Jacobians, and dynamics in depth.
- [Introduction to Robotics (2.12)](https://ocw.mit.edu/courses/2-12-introduction-to-robotics-fall-2005/), MIT OpenCourseWare. Free lectures and notes on planar and spatial kinematics and control.
- [DC motors](../electrical/01-dc-motors.md) for the torque-speed curve of the joint motor.
- [Planetary gears](../power-transmission/02-planetary-gears.md) for the gearbox ratio and efficiency used in step 6.
- [Gear trains](../power-transmission/01-gear-trains.md) for ratio and backlash basics.
- [Mobile robots](02-mobile-robots.md) for the next robot type in this folder.
- [Reference sheets](../reference.md) for the applications index and quick-look tables.
- [Mechanics reference](../../physics/reference-mechanics.md) for the statics and dynamics formulas used in the torque sizing.
