# Mobile robots

**Type:** lesson

A mobile robot moves itself across floors, yards, or warehouses. It must know where it is, decide where to go, and drive its wheels to get there. This lesson covers the kinematics of the common wheeled base, how wheel encoders give odometry, the sensors that correct odometry, and the basic steps of navigation.

**Prerequisites:** [Trigonometry](../../math/02-trigonometry.md), [Particle dynamics](../../physics/02-particle-dynamics.md), [Probability and statistics](../../math/07-probability-and-statistics.md), [Mechatronics](../electronics/06-mechatronics.md), [Sensors in products](../electronics/05-sensors-in-products.md)
**Time:** 10-14 h

## Core ideas

### How it works

A differential-drive robot has two driven wheels on a common axle and, usually, one or two passive casters. Each wheel turns at its own speed. When both wheels turn at the same speed, the robot drives straight. When one wheel is faster, the robot turns about a point on the axle line. The turning point sits on the axle, so the robot can also spin in place when the wheels turn in opposite directions.

Odometry estimates the robot's pose, which is its position and heading, from wheel motion. Each encoder counts wheel rotation. Those counts become wheel arc lengths, and the arc lengths become a change in pose. Odometry is accurate over short distances. Its errors add up with every step, because nothing in the sum corrects them.

Navigation adds three questions to odometry. Where am I? That is localization. What path leads to the goal? That is path planning. How do I drive the path while avoiding obstacles? That is control and obstacle avoidance. Localization usually fuses odometry with absolute measurements, such as a map match from a lidar scan.

### Main parts

- Drive wheels with motors and gearboxes. The motor torque must overcome rolling resistance, acceleration, and slopes. See [DC motors](../electrical/01-dc-motors.md) for torque and speed.
- Encoders on each wheel or each motor shaft. A quadrature encoder reports both the count and the direction of rotation.
- An inertial measurement unit (IMU) with a gyroscope and an accelerometer. The gyroscope measures turn rate, which helps heading estimates.
- Range sensors: ultrasonic sensors, infrared distance sensors, bump switches, and cliff sensors.
- Lidar, which scans a plane with a rotating laser and returns distances to nearby surfaces.
- A camera, which gives images for recognition and visual landmarks.
- A controller that runs the odometry, the navigation software, and the motor loops.

### Variants

- Differential drive: two independent driven wheels. Simple, cheap, and able to turn in place. Used in robot vacuums and warehouse carts.
- Car-like (Ackermann) steering: one or two driven wheels and a steered front axle. Stable at speed and efficient on roads, but it cannot turn in place.
- Omnidirectional drives, using mecanum or omni wheels: the robot moves sideways without turning. They suit tight indoor spaces, but the rollers wear faster and add cost.
- Tracked or skid-steer bases: wide contact patches for rough ground. They turn by skidding, which makes odometry less accurate.

## Key equations

Symbols: $r$ is wheel radius (m). $b$ is wheel separation, the distance between the two contact points (m). $v_L$, $v_R$ are the left and right wheel rim speeds (m/s). $v$ is forward speed of the robot centre (m/s). $\omega$ is turn rate (rad/s), positive counterclockwise. $\theta$ is heading (rad). $(x, y)$ is position (m). $\varphi_L$, $\varphi_R$ are wheel angles (rad). $N$ is the encoder count in one sample (counts), and $\mathrm{CPR}$ is the encoder counts per wheel revolution (counts/rev). $R$ is the turning radius (m).

Forward kinematics of a differential drive. Assumes no wheel slip, equal wheel radii, a rigid axle, and a flat floor:

$$v = \frac{v_R + v_L}{2}, \qquad \omega = \frac{v_R - v_L}{b}, \qquad R = \frac{b}{2}\,\frac{v_R + v_L}{v_R - v_L}$$

Inverse kinematics, for a commanded forward speed $v$ and turn rate $\omega$. Assumes the same no-slip, rigid-axle conditions as the forward model:

$$v_L = v - \frac{\omega b}{2}, \qquad v_R = v + \frac{\omega b}{2}$$

Each wheel angular speed is $\omega_w = v_w / r$, in rad/s.

Continuous motion model. Assumes no slip and a flat floor, with pose $(x, y, \theta)$ as the full state:

$$\dot x = v\cos\theta, \qquad \dot y = v\sin\theta, \qquad \dot\theta = \omega$$

Odometry from encoder counts over one sample. The encoder gives $\Delta\varphi = 2\pi N / \mathrm{CPR}$ for each wheel. Then:

$$\Delta s = \frac{r(\Delta\varphi_R + \Delta\varphi_L)}{2}, \qquad \Delta\theta = \frac{r(\Delta\varphi_R - \Delta\varphi_L)}{b}$$

$$x_{k+1} = x_k + \Delta s\cos\!\big(\theta_k + \tfrac{\Delta\theta}{2}\big), \qquad y_{k+1} = y_k + \Delta s\sin\!\big(\theta_k + \tfrac{\Delta\theta}{2}\big), \qquad \theta_{k+1} = \theta_k + \Delta\theta$$

The midpoint heading in the position update reduces error compared with using the start heading. Assumes each wheel count is exact, the wheels roll without slip, and the heading changes steadily within one sample.

Encoder resolution, the smallest distance one count can represent: $\delta = 2\pi r / \mathrm{CPR}$ (m). Assumes the wheel rolls without slip and the encoder counts every step.

Go-to-goal control, with goal $(x_g, y_g)$, distance $\rho = \sqrt{(x_g - x)^2 + (y_g - y)^2}$ (m), and heading error $\alpha = \operatorname{atan2}(y_g - y, x_g - x) - \theta$ (rad):

$$v = k_\rho\,\rho, \qquad \omega = k_\alpha\,\alpha$$

The gains $k_\rho$ (1/s) and $k_\alpha$ (1/s) set how fast the robot closes distance and turns. Assumes the pose is known exactly, the path is free of obstacles, the gains are positive, $k_\alpha > k_\rho$, and the goal stays in front of the robot ($|\alpha| < \pi/2$). Outside these conditions the robot can circle or diverge.

Ultrasonic range from echo time $t$ (s), with sound speed $c \approx 343\ \text{m/s}$ in air at 20 °C: $d = c\,t / 2$. Assumes the sound travels a straight path to the target and back, with no wind and no multipath echoes.

## Worked example

**Given:** A differential-drive robot with wheel radius $r = 0.050\ \text{m}$ and wheel separation $b = 0.250\ \text{m}$. The encoders give $\mathrm{CPR} = 500$. In one sample of $\Delta t = 0.100\ \text{s}$, the left wheel counts $N_L = 30$ and the right wheel counts $N_R = 34$. The robot starts at $(0, 0)$ with heading $\theta = 0$. Assumptions: no wheel slip, flat floor, and a sample small enough that the midpoint method is accurate.

**Find:** (a) the wheel arc lengths and the change in pose after the sample, (b) the forward speed and turn rate, and (c) the wheel speeds for a commanded path of radius $1.0\ \text{m}$ at $0.5\ \text{m/s}$.

**Solution:**

1. Wheel angles: $\Delta\varphi_L = 2\pi \times 30 / 500 = 0.3770\ \text{rad}$ and $\Delta\varphi_R = 2\pi \times 34 / 500 = 0.4273\ \text{rad}$.
2. Arc lengths: $s_L = 0.050 \times 0.3770 = 0.01885\ \text{m}$ and $s_R = 0.050 \times 0.4273 = 0.02136\ \text{m}$.
3. Change in pose: $\Delta s = (0.01885 + 0.02136)/2 = 0.02011\ \text{m}$ and $\Delta\theta = (0.02136 - 0.01885)/0.250 = 0.01005\ \text{rad}$, which is $0.576^\circ$.
4. New pose: $x = 0.02011\cos(0.00503) = 0.0201\ \text{m}$, $y = 0.02011\sin(0.00503) = 0.0001\ \text{m}$, and $\theta = 0.0101\ \text{rad}$.
5. Speeds over $0.100\ \text{s}$: $v_L = 0.1885\ \text{m/s}$, $v_R = 0.2136\ \text{m/s}$, so $v = 0.2011\ \text{m/s}$ and $\omega = 0.1005\ \text{rad/s}$. The turning radius is $R = 0.2011 / 0.1005 = 2.00\ \text{m}$.
6. Commanded path: $\omega = v / R = 0.5 / 1.0 = 0.500\ \text{rad/s}$. Then $v_L = 0.5 - 0.500 \times 0.125 = 0.4375\ \text{m/s}$ and $v_R = 0.5625\ \text{m/s}$. The wheel speeds are $\omega_L = 0.4375 / 0.050 = 8.75\ \text{rad/s}$ and $\omega_R = 11.25\ \text{rad/s}$. In rpm, that is $84\ \text{rpm}$ on the left and $107\ \text{rpm}$ on the right.

The Python used for steps 1 to 5:

```python
import math
r, b, cpr, dt = 0.05, 0.25, 500, 0.1
x = y = th = 0.0
sL = r*2*math.pi*30/cpr
sR = r*2*math.pi*34/cpr
ds, dth = (sL+sR)/2, (sR-sL)/b
x += ds*math.cos(th + dth/2)
y += ds*math.sin(th + dth/2)
th += dth
print(x, y, th, ds/dt, dth/dt, ds/dth)   # 0.0201, 0.0001, 0.0101, 0.2011, 0.1005, 2.00
```

**Answer:** (a) $s_L = 0.0189\ \text{m}$, $s_R = 0.0214\ \text{m}$, and the pose becomes $(0.0201, 0.0001)\ \text{m}$ with $\theta = 0.0101\ \text{rad}$. (b) $v = 0.201\ \text{m/s}$, $\omega = 0.1005\ \text{rad/s}$, and $R = 2.00\ \text{m}$. (c) $v_L = 0.4375\ \text{m/s}$ and $v_R = 0.5625\ \text{m/s}$, which are $8.75$ and $11.25\ \text{rad/s}$ at the wheels.

**Sanity check:** The turning radius from the encoders, $2.00\ \text{m}$, matches the ratio $\Delta s / \Delta\theta = 0.02011 / 0.01005 = 2.00\ \text{m}$. The commanded speeds average back to $0.5\ \text{m/s}$, because $(0.4375 + 0.5625)/2 = 0.500$. The encoder resolution is $2\pi \times 0.050 / 500 = 0.628\ \text{mm}$ per count, so the $30$ and $34$ counts are consistent with a $2\ \text{cm}$ motion over $0.1\ \text{s}$.

**Drift check:** If the true wheel radius is 1 percent smaller than the value in the code, every odometry distance is 1 percent too long. After $20\ \text{m}$ of travel, the robot's estimate is off by $0.20\ \text{m}$.

## Design trade-offs

- Wheel size against obstacles: larger wheels roll over small bumps and thresholds. They also raise the axle height, which moves the centre of mass and can reduce stability on slopes.
- Wheel separation against stability and turning: a wider base resists tipping and turns with a larger turning radius for the same wheel speed difference. A narrower base turns more tightly but tips more easily.
- Sensor cost against accuracy: wheel encoders are cheap and give fast updates, but they drift. Lidar costs more and gives accurate maps. Camera systems cost little hardware but need more processing.
- Speed against stopping distance: at $1\ \text{m/s}$ a robot needs a larger safe margin to stop than at $0.2\ \text{m/s}$. Speed limits near people set the maximum speed.
- Battery against runtime: battery mass reduces payload and raises motor load. Motor efficiency and the drive ratio also set runtime.
- Floor type: encoders work well on hard floors and overcount travel on carpet or sand, where driven wheels slip.

## How it fails

- Wheel slip: the encoder counts a rotation that moved the robot less. Odometry overestimates distance on slick floors, and the heading error grows with each turn.
- Wheel wear and tyre pressure: a change in wheel radius scales every distance. Calibration against a measured distance corrects a constant error.
- Gyroscope drift: the heading from the gyroscope drifts slowly over time. Fusing it with a magnetometer or a map match limits the drift.
- Lidar and sonar failures: glass, black surfaces, and mirrors return weak or false echoes. Ultrasonic sensors can miss angled walls, which reflect sound away from the sensor.
- Localization loss: after a collision or a lift, the robot does not know its pose. Recovery needs a map match or a human reset.
- Low battery: as voltage drops, motors stall under load and the robot stops on a slope or in a doorway.
- Cliff and bump events: a robot without cliff sensors drives off stairs. Bumpers and cliff sensors stop the drive, and speed limits and emergency-stop circuits reduce the harm to people.

## History

William Grey Walter built small light-seeking tortoise robots in Bristol, England, around 1948 and 1949. They used simple analog circuits, and they were among the first autonomous wheeled robots. The Stanford Research Institute built Shakey between about 1966 and 1972. Shakey used a camera, range sensors, and a planner to act in a room, and it is often cited as an early complete sense-plan-act system. The DARPA Grand Challenge in 2004 and 2005 drove a wave of outdoor autonomous vehicles, and the 2005 race was won by Stanford's Stanley. The consumer robot vacuum appeared in the early 2000s, and it brought wheeled odometry and bump sensing to millions of homes.

## Practice

1. A robot has a wheel radius of $0.040\ \text{m}$ and an encoder with $360$ counts per revolution. In one sample, the left wheel counts $90$. Find the left wheel arc length.
2. A differential-drive robot has $b = 0.30\ \text{m}$, $v_L = 0.20\ \text{m/s}$, and $v_R = 0.30\ \text{m/s}$. Find $v$, $\omega$, and the turning radius.
3. The robot in problem 2 must follow a path of radius $2.0\ \text{m}$ at $0.40\ \text{m/s}$ with $b = 0.25\ \text{m}$. Find $v_L$ and $v_R$.
4. An ultrasonic sensor receives its echo $5.0\ \text{ms}$ after the pulse. Sound travels at $343\ \text{m/s}$. Find the distance to the wall.
5. A robot with a $1$ percent error in its wheel radius estimate drives $20\ \text{m}$ by odometry. Find the size of the distance error.

<details><summary>Answers</summary>

1. $s_L = 0.040 \times 2\pi \times 90/360 = 0.0628\ \text{m}$.
2. $v = 0.25\ \text{m/s}$, $\omega = (0.30 - 0.20)/0.30 = 0.333\ \text{rad/s}$, and $R = v/\omega = 0.75\ \text{m}$.
3. $\omega = 0.40 / 2.0 = 0.200\ \text{rad/s}$. Then $v_L = 0.40 - 0.200 \times 0.125 = 0.375\ \text{m/s}$ and $v_R = 0.425\ \text{m/s}$.
4. $d = 343 \times 0.0050 / 2 = 0.858\ \text{m}$.
5. $0.01 \times 20\ \text{m} = 0.20\ \text{m}$.

</details>

## Common mistakes

- Treating encoder counts as true position. Counts measure wheel rotation, and slip makes the two differ.
- Forgetting that $\Delta\theta$ comes from the difference of the two wheel arcs. Using the sum gives a wrong heading.
- Mixing sign conventions for $\omega$. Pick counterclockwise as positive and use it on every line.
- Expecting GPS to work indoors. Satellite signals do not reach most indoor spaces, so indoor robots rely on odometry, lidar, and maps.
- Trusting one sensor. A robot that uses only encoders or only a gyroscope drifts. Fusing two or more sensors keeps the estimate bounded.

## Go deeper

- [Robotics](https://en.wikibooks.org/wiki/Robotics), Wikibooks. Open text on robot sensors, localization, mapping, and trajectory planning, under a Creative Commons licence.
- [Introduction to Robotics (2.12)](https://ocw.mit.edu/courses/2-12-introduction-to-robotics-fall-2005/), MIT OpenCourseWare. Free lectures on planar kinematics and motion planning.
- [Sensors in products](../electronics/05-sensors-in-products.md) for how encoders, IMUs, and range sensors work.
- [Robot arms](01-robot-arms.md) for the kinematics of the manipulator arm, which shares the same ideas of frames and Jacobians.
- [Mechatronics](../electronics/06-mechatronics.md) for the sensor, actuator, and controller loop that every mobile robot runs.
- [Reference sheets](../reference.md) for the applications index and quick-look tables.
- [Mechanics reference](../../physics/reference-mechanics.md) for the kinematics and dynamics formulas behind wheel motion.
