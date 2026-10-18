# Pick the governing principles

**Type:** lesson

A principle is a law of nature or a rule of the model that ties your knowns to your unknowns.
Most engineering problems use only a few: force balance, Newton's second law, conservation of
energy, and conservation of mass or heat. The skill is picking the right ones, not memorizing
every formula.

**Prerequisites:** [Define the problem](01-define-the-problem.md), [Draw it](02-draw-it.md)
**Time:** 4-6 h

## Core ideas

- A **governing principle** is a statement that is always true for the system you chose, such as
  "the net force on a body at rest is zero."
- A **model** is a set of principles plus assumptions. Changing the assumptions changes which
  principles apply.
- Pick principles by asking what the problem is about:
  - Is anything speeding up or slowing down? Use Newton's second law, $\sum F = ma$.
  - Is nothing moving? Use equilibrium, $\sum F = 0$ and $\sum M = 0$ (moments balance).
  - Is energy moving from one form to another with no losses? Use conservation of energy.
  - Is heat moving through a wall? Use a heat-flow law (lesson 08 uses one).
- Count your equations. You need as many independent equations as unknowns. If you have one
  unknown and two equations, check whether they are the same equation in disguise.

### Equilibrium

An object is in equilibrium when it does not accelerate. Then the net force is zero:

$$
\sum F_x = 0, \qquad \sum F_y = 0
$$

A static problem is one where equilibrium is the principle. The sign from lesson 01 is in
equilibrium, so its forces balance.

### Newton's second law

Newton's second law relates net force to acceleration. It is used when things move:

$$
\sum F = ma
$$

Here $F$ is force in newtons (N), $m$ is mass in kilograms (kg), and $a$ is acceleration in
meters per second squared ($\text{m/s}^2$). One newton is one kilogram times one meter per
second squared.

### Conservation of energy

When no energy is lost to friction or air drag, the total energy stays fixed. For an object
falling from rest:

$$
mgh = \tfrac{1}{2}mv^2
$$

Here $h$ is the drop height in meters (m), $v$ is speed in meters per second (m/s), and $g$ is
gravity at $9.81\ \text{m/s}^2$. The mass cancels, so the speed does not depend on mass. That
is a useful result, and you should check it, not assume it.

### Choosing principles for a falling object

Two principles can describe a falling object with no air drag:

- Kinematics: $v = gt$ and $h = \tfrac{1}{2}gt^2$, which use time as well as height.
- Energy: $v^2 = 2gh$, which uses height only.

Both are valid. Energy is faster when you do not need the time. Kinematics is needed when the
question asks how long the fall takes.

## Key equations

Equilibrium in two directions, from the knot of the sign:

$$
\sum F_y = 2T\sin\theta - W = 0
$$

Newton's second law for a block of mass $m$ pushed by a net force $F_{\text{net}}$:

$$
a = \frac{F_{\text{net}}}{m}
$$

Energy for a body falling a height $h$ from rest, with no losses:

$$
v = \sqrt{2gh}
$$

Each symbol:

- $T$ is tension in one cable (N)
- $\theta$ is the angle of each cable to horizontal (degrees)
- $W = mg$ is weight (N)
- $a$ is acceleration ($\text{m/s}^2$)
- $h$ is height (m), $v$ is speed (m/s), $g = 9.81\ \text{m/s}^2$

## Worked example

**Problem.** A ball is dropped from rest from a height of 20 m. Ignore air drag. Find (a) its
speed just before it hits the ground and (b) the time the fall takes.

**Given:** $h = 20\ \text{m}$, starting speed $v_0 = 0$, $g = 9.81\ \text{m/s}^2$.

**Find:** $v$ in m/s and $t$ in seconds (s).

**Assumptions:** no air drag, the ball is small enough to treat as a point, and gravity is
uniform over 20 m.

**Principles chosen:**

- Energy for (a): no losses, so $mgh = \tfrac{1}{2}mv^2$.
- Kinematics for (b): constant acceleration from rest, $h = \tfrac{1}{2}gt^2$.

**Solution.**

(a) Cancel mass and solve: $v = \sqrt{2gh} = \sqrt{2 \times 9.81 \times 20} = 19.81\ \text{m/s}$.

(b) Solve for time: $t = \sqrt{\dfrac{2h}{g}} = \sqrt{\dfrac{2 \times 20}{9.81}} = 2.019\ \text{s}$.

Cross-check with the other principle: $v = gt = 9.81 \times 2.019 = 19.81\ \text{m/s}$. The two
principles agree.

**Answer:** (a) $v = 19.8\ \text{m/s}$, about 71 km/h. (b) $t = 2.02\ \text{s}$.

**Sanity check:** 20 m is roughly a six-story building (about 3 m per floor). A fall that
long taking about 2 s is plausible. A speed of about 20 m/s is about 70 km/h, which is a fast
city-road speed, so the result is in the right range. Air drag would reduce both numbers, so
the real values would be a little lower.

## Practice

1. A block has forces of 10 N to the right and 4 N to the left, and nothing else. What is the
   net force in newtons?
2. An 8.0 kg block has a net force of 24 N. What is its acceleration in $\text{m/s}^2$?
3. A ball is dropped from rest from 3.0 m, ignoring air drag. What is its speed at the bottom,
   in m/s?

<details><summary>Answers</summary>

1. 6 N
2. 3.0 $\text{m/s}^2$
3. 7.67 m/s

</details>

## Common mistakes

- Using $\sum F = ma$ on an object at rest without checking the forces. At rest, $a=0$, so the
  forces must balance, and a missing force will show up as a mismatch.
- Mixing the principles. Energy gives speed from height directly. The time formula needs
  $g$ and $h$, not the speed, so do not swap a speed from one principle into the other
  without checking which quantities you know.
- Forgetting that energy conservation needs no losses. A real fall with drag loses energy.
- Writing more equations than unknowns and not noticing that some are dependent.
- Ignoring the direction of forces. Assign a positive direction and keep it.

## Go deeper

- [University Physics Volume 1](https://openstax.org/details/books/university-physics-volume-1) by OpenStax: chapters on Newton's laws, work and energy, and equilibrium.
- [Classical Mechanics (8.01SC)](https://ocw.mit.edu/courses/8-01sc-classical-mechanics-fall-2016/) by MIT OpenCourseWare: lectures on Newton's laws and energy conservation with problem sets.
- [Engineering LibreTexts](https://eng.libretexts.org/) by LibreTexts: free engineering textbooks, including statics and dynamics shelves.
- For more practice on these principles, see the [physics](../physics/README.md) folder.
