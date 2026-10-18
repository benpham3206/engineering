# Rigid body dynamics

**Type:** lesson

Rigid body dynamics extends particle dynamics to bodies that have size and shape, so they can rotate as well as move. Engineers use it for wheels, gears, flywheels, rotating shafts, and any part that spins up or slows down. This lesson covers planar motion, where the body moves and rotates in a single plane.

**Prerequisites:** [Particle dynamics](02-particle-dynamics.md) and [Statics](01-statics.md) (moments and free-body diagrams).
**Time:** 10-14 h

## Core ideas

- A **rigid body** keeps its shape while it moves. Every point on it moves in a way that is linked to every other point.
- **Planar motion** means all points move in parallel planes. For this lesson, the body moves in the x-y plane and rotates about an axis perpendicular to it, the z axis.
- **Angular position** $\theta$ is measured in radians (rad). **Angular velocity** $\omega = d\theta/dt$ is in rad/s, and **angular acceleration** $\alpha = d\omega/dt$ is in rad/s^2.
- **Mass moment of inertia** $I$ measures how hard it is to change a body's rotation. It depends on the mass and how far that mass sits from the axis. Its SI unit is kilogram meter squared (kg m^2), and its US customary unit is slug foot squared (slug ft^2).
- **Center of mass** $G$ is the average position of the body's mass. For many bodies, you can treat the whole mass as acting at $G$ when you write the translation equation.
- **Rolling without slipping** means the contact point on a wheel has zero velocity relative to the surface. For a wheel of radius $r$ rolling on a flat surface, the center speed and angular speed are linked by $v = \omega r$, and $a = \alpha r$.
- **Kinetic energy** of a rigid body in planar motion has two parts: translation of the center of mass and rotation about it.

Common inertia values for a body of mass $m$ are typical textbook results:

- Thin hoop of radius $r$ about its center: $I = mr^2$
- Solid disk or cylinder of radius $r$ about its center: $I = \tfrac{1}{2}mr^2$
- Thin rod of length $L$ about its center: $I = \tfrac{1}{12}mL^2$
- Thin rod of length $L$ about one end: $I = \tfrac{1}{3}mL^2$

## Key equations

Translation of the center of mass, with $G$ as the center:

$$\sum F_x = m\,a_{Gx} \qquad \sum F_y = m\,a_{Gy}$$

Rotation about the center of mass, for a rigid body rotating about the z axis through $G$:

$$\sum M_G = I_G\,\alpha$$

Here $F$ is force in newtons (N), $m$ is mass in kilograms (kg), $a_G$ is acceleration of the center of mass in m/s^2, $M_G$ is moment about $G$ in newton meters (N m), $I_G$ is the moment of inertia about $G$ in kg m^2, and $\alpha$ is angular acceleration in rad/s^2.

Rotational kinetic energy about the center of mass:

$$K_{\text{rot}} = \tfrac{1}{2}I_G\,\omega^2$$

Total planar kinetic energy:

$$K = \tfrac{1}{2}m v_G^2 + \tfrac{1}{2}I_G\,\omega^2$$

For rolling without slipping on a surface, with the contact point $P$ as the reference point:

$$v_G = \omega r \qquad a_G = \alpha r$$

## Worked example

**Given:** A uniform solid disk has mass $m = 10$ kg and radius $r = 0.3$ m. It rests on a horizontal floor. A horizontal force $F = 50$ N pulls on its center, so the disk rolls without slipping. Take $g = 9.81$ m/s^2.

**Find:** The acceleration $a_G$ of the center, the friction force at the contact point, and the smallest coefficient of static friction $\mu_s$ that prevents slipping.

**Assumptions:** The disk is uniform and rigid. It starts from rest. It rolls without slipping, so $a_G = \alpha r$. The force acts horizontally through the center.

**FBD description:** Draw the disk as a circle. Draw the 50 N force as an arrow to the right through the center. Draw the weight down through the center and the normal force up at the contact point. Draw the friction force as a horizontal arrow at the bottom of the disk. Friction points to the left, opposite to the motion. Pulling the center forward makes the bottom of the disk tend to slide forward relative to the floor.

**Solution:**

Moment of inertia of a solid disk about its center:

$$I_G = \tfrac{1}{2}mr^2 = \tfrac{1}{2}(10)(0.3)^2 = 0.45\ \text{kg m}^2$$

Let $f$ be the friction force, positive to the right. Translation gives:

$$F + f = m\,a_G$$

Rotation about the center, with clockwise as positive for a disk rolling to the right, gives the friction moment:

$$-f\,r = I_G\,\alpha \qquad \text{with } \alpha = a_G / r$$

so

$$f = -\frac{I_G\,a_G}{r^2} = -\tfrac{1}{2}m\,a_G$$

Substitute into the translation equation:

$$F - \tfrac{1}{2}m\,a_G = m\,a_G \quad\Rightarrow\quad a_G = \frac{F}{\tfrac{3}{2}m} = \frac{50}{15} = 3.333\ \text{m/s}^2$$

Friction is then

$$f = -\tfrac{1}{2}(10)(3.333) = -16.67\ \text{N}$$

The minus sign means friction acts to the left, with magnitude 16.67 N.

Smallest coefficient to prevent slipping, with normal force $N = mg = (10)(9.81) = 98.1$ N:

$$\mu_s \ge \frac{16.67}{98.1} = 0.170$$

**Answer:** $a_G \approx 3.33$ m/s^2 to the right. The friction force is about 16.7 N to the left. The floor must provide $\mu_s \ge 0.17$.

**Sanity check:** The disk accelerates at about one third of $F/m = 5$ m/s^2, because the disk's rotational inertia takes part of the force. For a hollow hoop, the result would be $F/(2m)$, a smaller acceleration, which fits because more of the mass sits far from the axis. The friction force of 16.7 N is well under the 98.1 N normal force, so a floor with a moderate coefficient of friction can keep the disk from slipping. A floor with a much smaller coefficient would let it slip.

## Practice

1. A thin hoop of mass 2 kg and radius 0.5 m rotates about its center. Find its moment of inertia about its center, in kg m^2.
2. A uniform rod of mass 3 kg and length 2 m rotates about one end. Find its moment of inertia about that end, in kg m^2.
3. A net moment of 6 N m acts on a body with $I_G = 0.5$ kg m^2 about its center. Find the angular acceleration, in rad/s^2.
4. A uniform solid disk with $I_G = 0.45$ kg m^2 spins at 10 rad/s about its center. Find its rotational kinetic energy, in joules.

<details><summary>Answers</summary>

1. 0.5 kg m^2
2. 4 kg m^2
3. 12 rad/s^2
4. 22.5 J

</details>

## Common mistakes

- Using the moment of inertia of a point mass when the body has size. Use the table value for the shape, or integrate if no table fits.
- Taking moments about a point that is not the center of mass and using $I_G$ with it. Either use $\sum M_G = I_G\alpha$ with $I_G$, or use $\sum M_P = I_P\alpha$ with $I_P$ for a fixed point $P$, and never mix them.
- Forgetting that rolling without slipping links $a_G$ and $\alpha$ only through the radius. Writing $a = \alpha$ without $r$ gives the wrong units.
- Choosing the wrong sign for friction. Friction opposes the tendency to slip, which is not always the direction of motion. Solve for it and check the sign at the end.
- Forgetting to convert the angle in $\omega$ and $\alpha$ to radians. A 360 degree turn is $2\pi$ rad.

## Go deeper

- [MIT OpenCourseWare 2.003SC Engineering Dynamics, Fall 2011](https://ocw.mit.edu/courses/2-003sc-engineering-dynamics-fall-2011/) by MIT: free notes and course materials covering force-momentum methods for planar rigid bodies, CC BY-NC-SA 4.0.
- [MIT OpenCourseWare 8.01SC Classical Mechanics, Fall 2016](https://ocw.mit.edu/courses/8-01sc-classical-mechanics-fall-2016/) by MIT: free course covering rotation, rolling, and collisions, CC BY-NC-SA 4.0. Use it for extra practice with rolling problems.
- Previous: [Particle dynamics](02-particle-dynamics.md), for the translation half of this lesson.
