# Velocity kinematics and Jacobians

**Type:** lesson
**Verify:** strict

A **Jacobian** is the matrix that converts the speeds of a robot's joints into the velocity of its tool, and, by the same matrix transposed, converts a force at the tool into the torques the joints must supply. An engineer needs it to move a tool along a straight line, to size motors for a pushing task, and to know which poses the arm must avoid. This lesson derives it for a planar two-link arm and uses it three ways.

**Prerequisites:** [Robot arms](01-robot-arms.md) (forward and inverse kinematics), [Multivariable calculus](../../math/04-multivariable-calculus.md) (partial derivatives and the chain rule), [Linear algebra](../../math/05-linear-algebra.md) (matrix products, determinants, inverses), [Statics](../../physics/01-statics.md) (moments)
**Time:** 6-8 h

## Core ideas

### How it works

Forward kinematics, covered in [Robot arms](01-robot-arms.md), gives the tool position as a function of the joint angles. Differentiate that function with respect to time and the chain rule gives a relation between rates. Each tip velocity component is a sum of terms, one per joint, and each term is a joint speed multiplied by a coefficient that depends only on the current pose. Collected in a matrix, the coefficients are the Jacobian $J$.

At a fixed pose the relation is linear, so linear algebra applies. If the joint speeds double, the tip speed doubles. If the pose changes, the coefficients change, and so does $J$.

The same matrix answers a second question. A **virtual displacement** is a small imagined motion of the joints that obeys the arm's constraints. In slow motion with no friction, the work the motors do equals the work the tip does on its surroundings. Equating the two powers gives $\boldsymbol{\tau} = J^{T}\mathbf{F}$, with the transpose of the same $J$.

The **inverse velocity problem** asks the reverse question. Given the tip velocity wanted, find the joint speeds. When $J$ is square and invertible, the answer is $\dot{\boldsymbol\theta} = J^{-1}\mathbf{v}$. When $J$ has no inverse, the arm is at a **singularity**, a pose where the tool loses the ability to move in some direction no matter how fast the joints turn.

### Main parts

- Columns of $J$. Column $i$ is the tip velocity produced by joint $i$ turning at 1 rad/s while all other joints stay still. For a revolute joint in a plane, it points perpendicular to the line from that joint to the tip, with length equal to that distance.
- Determinant of $J$. For a square $J$ it measures how much the map stretches area. Zero means the map collapses a direction.
- Inverse of $J$. It exists only away from singularities, and it grows without bound as the arm nears one.
- Transpose of $J$. It carries tip force to joint torque and needs no inversion, so it is safe at every pose, singular or not.
- Manipulability ellipse. The set of tip velocities reachable with joint speeds of unit size is an ellipse. Its axes are the singular values of $J$. A thin ellipse means the arm is near a singularity.

### Variants

- Planar and spatial. A planar arm has a $2 \times 2$ Jacobian for tip position. A spatial arm has a $6 \times n$ Jacobian whose rows cover three linear and three angular velocity components.
- Space and body forms. The same velocity can be written in the base frame or in a frame attached to the tool. The two Jacobians differ by a change of frame.
- Square and non-square. An arm with more joints than task dimensions is **redundant**. Its Jacobian has more columns than rows, so many joint speeds give the same tip velocity, and a pseudoinverse picks one of them.
- Analytic and geometric. The analytic Jacobian differentiates a chosen orientation parameterization. The geometric Jacobian uses angular velocity directly.

The Modern Robotics text listed in Go deeper treats the spatial forms in full. This lesson stays in the plane, where every quantity can be checked by hand.

## Key equations

Symbols: $L_1$, $L_2$ are link lengths (m). $\theta_1$ is the shoulder angle from the base x-axis (rad). $\theta_2$ is the elbow angle relative to link 1 (rad), the same convention as [Robot arms](01-robot-arms.md). $\dot\theta_1$, $\dot\theta_2$ are joint speeds (rad/s). $\mathbf{v} = (v_x, v_y)$ is tip velocity (m/s). $\mathbf{F} = (F_x, F_y)$ is the force the tip applies to its surroundings (N). $\boldsymbol\tau = (\tau_1, \tau_2)$ is the torque each motor applies at its joint (N m). Shorthand: $s_1 = \sin\theta_1$, $c_1 = \cos\theta_1$, $s_{12} = \sin(\theta_1+\theta_2)$, $c_{12} = \cos(\theta_1+\theta_2)$.

Start from the tip coordinates $x(\theta_1,\theta_2)$ and $y(\theta_1,\theta_2)$ of the forward kinematics. The chain rule gives

$$\dot x = \frac{\partial x}{\partial \theta_1}\dot\theta_1 + \frac{\partial x}{\partial \theta_2}\dot\theta_2, \qquad \dot y = \frac{\partial y}{\partial \theta_1}\dot\theta_1 + \frac{\partial y}{\partial \theta_2}\dot\theta_2$$

Evaluating the four partial derivatives (the derivative of $\sin(\theta_1+\theta_2)$ with respect to either angle is $\cos(\theta_1+\theta_2)$, and the same for cosine with a sign change) gives the velocity map:

$$\begin{bmatrix}\dot x\\ \dot y\end{bmatrix} = J \begin{bmatrix}\dot\theta_1\\ \dot\theta_2\end{bmatrix}, \qquad J = \begin{bmatrix} -L_1 s_1 - L_2 s_{12} & -L_2 s_{12} \\ L_1 c_1 + L_2 c_{12} & L_2 c_{12} \end{bmatrix}$$

The entries of $J$ have units of metres, because a joint angle in radians is dimensionless. The map holds for rigid links, a fixed base, and speeds read at one instant. It says nothing about acceleration.

Determinant:

$$\det J = L_1 L_2 \sin\theta_2$$

It follows by multiplying out the two diagonals, where the $L_2^2$ terms cancel and the product reduces through $\sin(\theta_1+\theta_2)\cos\theta_1 - \cos(\theta_1+\theta_2)\sin\theta_1 = \sin\theta_2$. It does not depend on $\theta_1$, since rotating the whole arm about the base cannot change whether it is singular. Units: m$^2$.

Static force map. Take the arm in slow, frictionless motion with the link weights ignored. Mechanical power from the motors equals power delivered by the tip:

$$\boldsymbol\tau^{T}\dot{\boldsymbol\theta} = \mathbf{F}^{T}\mathbf{v} = \mathbf{F}^{T} J \dot{\boldsymbol\theta} \quad\text{for every } \dot{\boldsymbol\theta} \;\Rightarrow\; \boldsymbol\tau = J^{T}\mathbf{F}$$

The result holds at a fixed pose with no acceleration and no friction. Gravity on the links and payload adds its own torques on top, as in [Robot arms](01-robot-arms.md).

Inverse velocity. When $\det J \neq 0$,

$$\begin{bmatrix}\dot\theta_1\\ \dot\theta_2\end{bmatrix} = \frac{1}{L_1 L_2 \sin\theta_2}\begin{bmatrix} L_2 c_{12} & L_2 s_{12} \\ -L_1 c_1 - L_2 c_{12} & -L_1 s_1 - L_2 s_{12} \end{bmatrix}\begin{bmatrix}v_x\\ v_y\end{bmatrix}$$

The factor $1/\sin\theta_2$ shows how joint speeds grow near the singular poses $\theta_2 = 0$ and $\theta_2 = \pi$. The inverse assumes the joint speeds are free to take any value, with no speed limit.

## Worked example

**Given:** A planar two-link arm with $L_1 = 0.40\ \text{m}$ and $L_2 = 0.30\ \text{m}$, in the pose $\theta_1 = 20^\circ$, $\theta_2 = 60^\circ$. Joint speeds $\dot\theta_1 = 0.50\ \text{rad/s}$ and $\dot\theta_2 = -0.20\ \text{rad/s}$ in part (b). In part (c) the tip pushes straight down on a table with $\mathbf{F} = (0, -10)\ \text{N}$. In part (d) the tool must move at $\mathbf{v} = (0.10, 0.05)\ \text{m/s}$, first in this pose and then with $\theta_2$ lowered to $10^\circ$ and to $2^\circ$, keeping $\theta_1 = 20^\circ$.

**Find:** (a) $J$ and $\det J$. (b) The tip velocity. (c) The joint torques. (d) The joint speeds for the wanted tool velocity at the three elbow angles.

**Assumptions:** rigid links, planar motion, quasi-static loading, no friction, and link weight ignored in part (c) so that only the tip force is counted.

**Solution:**

1. Entries of $J$ at the pose: $J_{11} = -0.40\sin 20^\circ - 0.30\sin 80^\circ = -0.432\ \text{m}$. $J_{12} = -0.30\sin 80^\circ = -0.295\ \text{m}$. $J_{21} = 0.40\cos 20^\circ + 0.30\cos 80^\circ = 0.428\ \text{m}$. $J_{22} = 0.30\cos 80^\circ = 0.052\ \text{m}$.
2. The determinant from the entries is $J_{11}J_{22} - J_{12}J_{21} = 0.1039\ \text{m}^2$. The closed form gives $0.40 \times 0.30 \times \sin 60^\circ = 0.1039\ \text{m}^2$, the same value.
3. Tip velocity: $v_x = -0.432 \times 0.50 + (-0.295)(-0.20) = -0.157\ \text{m/s}$ and $v_y = 0.428 \times 0.50 + 0.052 \times (-0.20) = 0.204\ \text{m/s}$.
4. Joint torques from $\boldsymbol\tau = J^{T}\mathbf{F}$: $\tau_1 = J_{11}F_x + J_{21}F_y = 0.428 \times (-10) = -4.28\ \text{N m}$ and $\tau_2 = J_{12}F_x + J_{22}F_y = 0.052 \times (-10) = -0.52\ \text{N m}$. Negative means the motors push clockwise, which matches a downward push at a tip to the right of the base.
5. Power check: $\boldsymbol\tau^{T}\dot{\boldsymbol\theta} = (-4.28)(0.50) + (-0.52)(-0.20) = -2.04\ \text{W}$, and $\mathbf{F}^{T}\mathbf{v} = (-10)(0.204) = -2.04\ \text{W}$.
6. Inverse velocity at $\theta_2 = 60^\circ$ gives $\dot\theta_1 = 0.192\ \text{rad/s}$ and $\dot\theta_2 = -0.620\ \text{rad/s}$. At $\theta_2 = 10^\circ$ the same tool velocity needs $\dot\theta_1 = 1.61\ \text{rad/s}$ and $\dot\theta_2 = -3.74\ \text{rad/s}$. At $\theta_2 = 2^\circ$ it needs $\dot\theta_1 = 7.98\ \text{rad/s}$ and $\dot\theta_2 = -18.6\ \text{rad/s}$.

**Answer:** (a) $J = \begin{bmatrix}-0.432 & -0.295\\ 0.428 & 0.052\end{bmatrix}\ \text{m}$ and $\det J = 0.104\ \text{m}^2$. (b) $\mathbf{v} = (-0.157, 0.204)\ \text{m/s}$. (c) $\boldsymbol\tau = (-4.28, -0.52)\ \text{N m}$. (d) The joint speeds are $(0.192, -0.620)$, $(1.61, -3.74)$, and $(7.98, -18.6)\ \text{rad/s}$ at the three elbow angles.

**Sanity check:** The torque result agrees with moments. The tip sits at $x = 0.428\ \text{m}$ from the base, so a 10 N downward force has a moment of $4.28\ \text{N m}$ about the shoulder. The elbow sits at $x = 0.376\ \text{m}$ and the tip is $0.052\ \text{m}$ to its right, giving $0.52\ \text{N m}$ about the elbow. Both match step 4. The speeds in step 6 grow as the elbow straightens, as the factor $1/\sin\theta_2$ predicts.

<details><summary>Verification</summary>

```verify
L1 = q(0.40, "m")
L2 = q(0.30, "m")
th1 = q(20, "deg")
th2 = q(60, "deg")
w1 = q(0.50, "rad/s")
w2 = q(-0.20, "rad/s")
Fy = q(-10, "N")
J11 = -L1 * sin(th1) - L2 * sin(th1 + th2)
J12 = -L2 * sin(th1 + th2)
J21 = L1 * cos(th1) + L2 * cos(th1 + th2)
J22 = L2 * cos(th1 + th2)
expect(J11, "-0.432 m")
expect(J12, "-0.295 m")
expect(J21, "0.428 m")
expect(J22, "0.052 m")
det = J11 * J22 - J12 * J21
expect(det, "0.1039 m^2")
expect(L1 * L2 * sin(th2), "0.1039 m^2")
expect(det, "0.104 m^2")
vx = J11 * w1 + J12 * w2
vy = J21 * w1 + J22 * w2
expect(vx, "-0.157 m/s")
expect(vy, "0.204 m/s")
tau1 = J21 * Fy
tau2 = J22 * Fy
expect(tau1, "-4.28 N m")
expect(tau2, "-0.52 N m")
expect(tau1 * w1 + tau2 * w2, "-2.04 W")
expect(Fy * vy, "-2.04 W")
expect(L1 * cos(th1) + L2 * cos(th1 + th2), "0.428 m")
expect(L1 * cos(th1), "0.376 m")
given("80")
vdx = q(0.10, "m/s")
vdy = q(0.05, "m/s")
a1 = (J22 * vdx - J12 * vdy) / det
a2 = (-J21 * vdx + J11 * vdy) / det
expect(a1, "0.192 rad/s")
expect(a2, "-0.620 rad/s")
t2b = q(10, "deg")
D2 = L1 * L2 * sin(t2b)
K11 = -L1 * sin(th1) - L2 * sin(th1 + t2b)
K12 = -L2 * sin(th1 + t2b)
K21 = L1 * cos(th1) + L2 * cos(th1 + t2b)
K22 = L2 * cos(th1 + t2b)
expect((K22 * vdx - K12 * vdy) / D2, "1.61 rad/s")
expect((-K21 * vdx + K11 * vdy) / D2, "-3.74 rad/s")
t2c = q(2, "deg")
D3 = L1 * L2 * sin(t2c)
M11 = -L1 * sin(th1) - L2 * sin(th1 + t2c)
M12 = -L2 * sin(th1 + t2c)
M21 = L1 * cos(th1) + L2 * cos(th1 + t2c)
M22 = L2 * cos(th1 + t2c)
expect((M22 * vdx - M12 * vdy) / D3, "7.98 rad/s")
expect((-M21 * vdx + M11 * vdy) / D3, "-18.6 rad/s")
check(D3 < D2 and D2 < det, "the determinant shrinks as the elbow straightens")
```

</details>

## Design trade-offs

- Pose planning against joint speed limits. For a tool path at a fixed speed, the needed joint speed varies with $1/\sin\theta_2$. The example shows $0.65\ \text{rad/s}$ at $60^\circ$ and $20\ \text{rad/s}$ at $2^\circ$ for the same tool velocity. A planner keeps the elbow bent away from straight so the motors stay inside their speed limits.
- Reach against dexterity. Fully extended gives the longest reach but zero velocity capability along the arm. Mounting the workpiece so the task sits at a bent elbow gives up a little reach for speed in every direction.
- Torque capability against speed capability. A pose where a small joint speed produces a large tip speed is a pose where a small tip force needs a large joint torque, and the reverse. The two ellipses of the same $J$ are stretched in perpendicular ways, so no pose gives both.
- Redundant joints against cost. An extra joint adds a free choice of joint speeds for the same tip velocity, which lets a controller steer around singularities and joint limits. It adds a motor, a gearbox, and an encoder.
- Pseudoinverse and damping against exactness. Near a singularity a damped inverse limits joint speeds, at the price of a tip velocity that no longer matches the command in the poorly conditioned direction.

## How it fails

- Singular pose reached on a commanded path. The inverse asks for unbounded joint speeds, a drive saturates, and the tip departs from the path. Controllers detect a small determinant or a large condition number and slow down or switch to a damped solution.
- Kinematic model out of date. A link length, joint zero, or tool offset in the controller that differs from the real arm gives a $J$ that predicts the wrong tip velocity. Signs: the tool drifts off a straight line during a Cartesian jog. Calibration repairs it.
- Force estimates from motor current. $\boldsymbol\tau = J^{T}\mathbf{F}$ run backward estimates tip force from torque. Friction in the gearbox and the weight of the links add torque that does not come from the tip, so the estimate is wrong without compensation.
- Unexpected tip force near a singularity. A force along the arm's length at $\theta_2 = 0$ needs no joint torque, so a motor-current limit does not protect against it. The structure carries the load, and only the link strength limits it. A tool pushing outward on a stiff fixture with a straight arm can load the links and bearings far beyond what the motors would predict.
- Numerical inversion with a bad condition number. A tiny determinant makes the computed inverse dominated by rounding error. Use a solver that checks conditioning, not a raw matrix inverse.

> [!WARNING]
> A robot jogged in Cartesian mode at a fixed tool speed can command very large joint speeds as it approaches a singular pose. Keep people out of the reach envelope, and set joint speed limits in the controller rather than relying on the operator to avoid the pose.

## History

The Jacobian is the matrix of first partial derivatives from multivariable calculus, and robotics borrowed it because the tool velocity of a serial arm is a linear map of the joint velocities at each pose. Controllers use the inverse of that map to drive the tool along a commanded path, and use damped or pseudoinverse forms where the inverse fails. The Modern Robotics text and the MIT OpenCourseWare robotics notes listed below teach the topic in its current form.

## Practice

Use the arm of the worked example, $L_1 = 0.40\ \text{m}$ and $L_2 = 0.30\ \text{m}$, unless stated.

1. Find $\det J$ for $\theta_1 = 20^\circ$ and $\theta_2 = 90^\circ$.
2. The arm is fully extended along the x-axis, $\theta_1 = \theta_2 = 0$. Find the joint torques needed for a tip force of $20\ \text{N}$ straight up ($\mathbf{F} = (0, 20)\ \text{N}$), and then for a tip force of $20\ \text{N}$ along the arm ($\mathbf{F} = (20, 0)\ \text{N}$).
3. Each joint is limited to $3.0\ \text{rad/s}$. Can the tip move at $\mathbf{v} = (0.10, 0.05)\ \text{m/s}$ with $\theta_1 = 20^\circ$ and $\theta_2 = 10^\circ$? Find the larger of the two joint speeds the motion needs.
4. For which elbow angle between $0^\circ$ and $90^\circ$ is $\det J$ equal to half its maximum value?
5. Explain why a fully extended arm cannot move its tip along its own length, and say what the motors feel if the tip pushes along that direction.

<details><summary>Answers</summary>

1. $0.12\ \text{m}^2$, from $0.40 \times 0.30 \times \sin 90^\circ$.
2. For the upward force, $\tau_1 = 14\ \text{N m}$ and $\tau_2 = 6.0\ \text{N m}$. For the force along the arm, both torques are $0\ \text{N m}$.
3. No. The elbow joint needs $3.74\ \text{rad/s}$, above the $3.0\ \text{rad/s}$ limit. The shoulder needs $1.61\ \text{rad/s}$. The numbers come from the worked example's step 6.
4. $30^\circ$, from $\sin\theta_2 = 0.5$.
5. Both columns of $J$ are perpendicular to the arm at $\theta_2 = 0$, so every joint motion moves the tip sideways only. With the tip pushing along the arm, $J^{T}\mathbf{F}$ is zero. The links carry the load in compression or tension, and the motors feel no torque.

```verify
L1 = q(0.40, "m")
L2 = q(0.30, "m")
expect(L1 * L2 * sin(q(90, "deg")), "0.12 m^2", ans=1)
Fup = q(20, "N")
tq1 = (L1 + L2) * Fup
tq2 = L2 * Fup
expect(tq1, "14 N m", ans=2)
expect(tq2, "6.0 N m", ans=2)
expect(q(0, "N") * (L1 + L2), "0 N m", ans=2)
th1 = q(20, "deg")
t2 = q(10, "deg")
vdx = q(0.10, "m/s")
vdy = q(0.05, "m/s")
D = L1 * L2 * sin(t2)
K11 = -L1 * sin(th1) - L2 * sin(th1 + t2)
K12 = -L2 * sin(th1 + t2)
K21 = L1 * cos(th1) + L2 * cos(th1 + t2)
K22 = L2 * cos(th1 + t2)
r1 = (K22 * vdx - K12 * vdy) / D
r2 = (-K21 * vdx + K11 * vdy) / D
expect(r1, "1.61 rad/s", ans=3)
expect(abs(r2), "3.74 rad/s", ans=3)
check(abs(r2) > q(3.0, "rad/s"), "the elbow exceeds its speed limit")
given("0.5")
expect(asin(0.5) / u("deg"), "30", ans=4)
skip(ans=5, why="explanation")
```

</details>

## Common mistakes

- Mixing the angle conventions. The Jacobian here uses $\theta_2$ relative to link 1. With an absolute second angle the second column changes. Check the convention in [Robot arms](01-robot-arms.md) first.
- Using degrees per second inside $J$. The entries assume joint speeds in rad/s. A speed in deg/s needs a factor of $\pi/180$ before the product.
- Taking $J^{-1}$ as the way to get torque. Joint torque from tip force uses the transpose $J^{T}$, not the inverse. The inverse belongs to velocity.
- Forgetting that $J$ depends on the pose. A Jacobian computed at one pose is wrong a moment later when the joints have moved.
- Reading $\boldsymbol\tau = J^{T}\mathbf{F}$ as the whole torque. It covers only the tip force. Gravity, friction, and acceleration add torque at the joints.

## Go deeper

- [Modern Robotics](https://hades.mech.northwestern.edu/index.php/Modern_Robotics) by Kevin Lynch and Frank Park. The site links the free preprint. See the chapter on velocity kinematics and statics for the spatial Jacobian, the force map, and manipulability ellipsoids, and the inverse kinematics chapter for numerical resolved-rate methods.
- [Introduction to Robotics (2.12)](https://ocw.mit.edu/courses/2-12-introduction-to-robotics-fall-2005/), MIT OpenCourseWare. Free lecture notes on kinematics, Jacobians, and control of arms.
- [Robot arms](01-robot-arms.md) for forward and inverse kinematics, gravity torque, and motor sizing.
- [Mobile robots](02-mobile-robots.md) for the next robot type in this folder.
- [Feedback control](../../physics/14-controls.md) for the loop that follows a Cartesian velocity command.
- [Applications reference](../reference.md) for the index and quick-look tables.
- [Mechanics reference](../../physics/reference-mechanics.md) for moments and virtual work.
