# Particle dynamics

**Type:** lesson

Particle dynamics is the study of how forces change the motion of a body. Engineers use it to predict how a car stops, how a projectile lands, and how a machine part speeds up. This lesson treats the body as a particle, a point with mass, and uses three tools: Newton's second law, work and energy, and impulse and momentum.

**Prerequisites:** [Statics](01-statics.md) (free-body diagrams and force components), [Single-variable calculus](../math/03-single-variable-calculus.md) (velocity and acceleration as rates, impulse and work as integrals)
**Time:** 10-14 h

## Core ideas

- **Position** $x$ is where the particle is. **Velocity** $v = dx/dt$ is how fast position changes. **Acceleration** $a = dv/dt$ is how fast velocity changes. Use meters (m), meters per second (m/s), and meters per second squared ($\mathrm{m/s^2}$), or feet, feet per second, and feet per second squared in US customary units.
- **Kinematics** describes motion without asking what causes it. For constant acceleration, the three standard equations connect position, velocity, acceleration, and time.
- **Kinetics** connects force to motion. Newton's second law says the net force on a particle equals its mass times its acceleration. Mass is in kilograms (kg) in SI units or slugs in US customary units.
- **Work** is the energy transferred by a force along a displacement. For a constant force, work equals the force component along the motion times the distance.
- **Kinetic energy** $K = \tfrac{1}{2}mv^2$ is the energy of motion. Work done by the net force equals the change in kinetic energy.
- **Potential energy** stores energy that depends on position. For gravity near Earth's surface, $U = mgh$.
- **Impulse** is the force integrated over time. It equals the change in momentum.
- **Momentum** $p = mv$ is mass times velocity. Momentum is conserved when the net external force on a system is zero, which is useful in collisions.
- **Friction** is a force that opposes sliding. Kinetic friction has the form $F_k = \mu_k N$, where $\mu_k$ is the coefficient of kinetic friction. It is usually smaller than the static value.

## Key equations

Newton's second law for a particle in one direction:

$$\sum F = ma$$

Constant-acceleration relations, with $x_0$ and $v_0$ as starting position and velocity:

$$v = v_0 + at \qquad x = x_0 + v_0 t + \tfrac{1}{2}at^2 \qquad v^2 = v_0^2 + 2a(x - x_0)$$

Work-energy theorem:

$$W_{\text{net}} = \Delta K = \tfrac{1}{2}m v_2^2 - \tfrac{1}{2}m v_1^2$$

Impulse-momentum theorem:

$$\int_{t_1}^{t_2} \sum F\, dt = m v_2 - m v_1$$

Here $F$ is force in newtons (N), $m$ is mass in kilograms (kg), $a$ is acceleration in $\mathrm{m/s^2}$, $t$ is time in seconds (s), $W$ is work in joules (J), and $K$ is kinetic energy in J. One newton equals one kilogram meter per second squared, and one joule equals one newton meter.

## Worked example

**Given:** A 1500 kg car moves along a straight, level road at $v_1 = 15$ m/s. The driver applies a constant forward force from the engine over a distance of 200 m. The car's speed becomes $v_2 = 25$ m/s at the end. Ignore air resistance and rolling resistance.

**Find:** The average net forward force $F$ on the car over the 200 m, and the car's acceleration.

**Assumptions:** The road is level, so gravity does no work. The force is constant. The car is a particle moving in a straight line.

**FBD description:** Draw the car as a dot. Draw one arrow forward for the net engine force. Draw one arrow down for weight and one arrow up for the normal force from the road. The vertical arrows cancel, so the net force is the forward arrow only.

**Solution, using work and energy:**

$$\Delta K = \tfrac{1}{2}(1500)(25^2 - 15^2) = \tfrac{1}{2}(1500)(625 - 225) = 300\,000\ \text{J}$$

The net work equals the force times the distance:

$$F = \frac{W}{d} = \frac{300\,000\ \text{J}}{200\ \text{m}} = 1500\ \text{N}$$

**Solution, using kinematics as a check:**

From $v^2 = v_0^2 + 2a\,\Delta x$:

$$a = \frac{25^2 - 15^2}{2(200)} = \frac{400}{400} = 1.0\ \text{m/s}^2$$

Then Newton's second law gives $F = ma = (1500)(1.0) = 1500$ N, which matches.

**Answer:** The net forward force is $F = 1500$ N, and the acceleration is $a = 1.0$ $\mathrm{m/s^2}$.

**Sanity check:** An acceleration of 1.0 $\mathrm{m/s^2}$ is about a tenth of gravity, a plausible value for a car. The two methods agree. The speed goes from 15 to 25 m/s, which is an increase of 10 m/s over 200 m, and an average speed of 20 m/s would take 10 s. A constant acceleration of 1.0 $\mathrm{m/s^2}$ for 10 s gives a change of 10 m/s, so the numbers are consistent.

## Practice

1. A 1200 kg car moves at 20 m/s. Find its kinetic energy, in kilojoules.
2. A 4 kg object starts from rest and is pushed by a constant net force of 12 N. How long, in seconds, does it take to reach 9 m/s?
3. A 0.5 kg ball is dropped from rest from a height of 5 m. Ignoring air resistance, find its speed just before it hits the ground, in m/s. Use $g = 9.81\ \text{m/s}^2$ (Earth surface).
4. A 0.2 kg ball moving at +20 m/s bounces straight back at -20 m/s. Find the impulse delivered to the ball, in N s. Take the positive direction as the direction of the initial velocity.

<details><summary>Answers</summary>

1. 240 kJ
2. 3 s
3. About 9.9 m/s
4. -8 N s (magnitude 8 N s)

</details>

## Common mistakes

- Using $K = \tfrac{1}{2}mv^2$ with $v$ in km/h or mph instead of m/s. Convert first.
- Forgetting that work needs the force component along the displacement. A force perpendicular to motion does no work, such as the normal force on a level surface.
- Using the net force in Newton's second law but a single force in the work term, or the reverse. Use the net force for $\sum F = ma$ and the work-energy theorem with net work.
- Dropping the sign on velocity in momentum or impulse problems. A reversed direction changes the sign of the impulse.
- Treating friction as always equal to $\mu N$. Kinetic friction uses $\mu_k N$ only while the body slides, and its direction opposes the sliding.

## Go deeper

- [MIT OpenCourseWare 8.01SC Classical Mechanics, Fall 2016](https://ocw.mit.edu/courses/8-01sc-classical-mechanics-fall-2016/) by MIT: free lecture notes and problem sets on kinematics, Newton's laws, work, energy, and momentum, CC BY-NC-SA 4.0.
- [University Physics Volume 1, Chapter 1, Introduction](https://openstax.org/books/university-physics-volume-1/pages/1-introduction) by OpenStax: units, unit conversion, and problem-solving habits, free online. Read it before the chapters on motion, which cover this lesson's topics in more depth.
- Next: [Rigid body dynamics](03-rigid-body-dynamics.md), which adds rotation to the particle model.
- [Mechanics reference](reference-mechanics.md): the lookup sheet for this topic.
