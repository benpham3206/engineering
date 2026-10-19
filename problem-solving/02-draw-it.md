# Draw it

**Type:** lesson

A sketch turns a sentence into a picture you can check. Engineers draw before they calculate
because a picture shows which forces exist, which way they point, and where the system ends.
A free-body diagram is the most useful sketch in mechanics. It shows one object and every
force acting on it.

**Prerequisites:** [Define the problem](01-define-the-problem.md), [Statics](../physics/01-statics.md), [Trigonometry](../math/02-trigonometry.md)
**Time:** 2-4 h

## Core ideas

- A **sketch** is a quick drawing with the key geometry: lengths, angles, supports, and loads.
  Label every dimension with its value and unit.
- A **free-body diagram (FBD)** is a sketch of one object, cut away from everything touching
  it. Draw the object as a simple box or dot, and replace each contact or field with a force
  arrow.
- A **force arrow** shows direction and, roughly, magnitude. Label each arrow with a symbol
  such as $W$, $N$, $T$, or $f$.
- A **reaction force** is the push or pull a support exerts on the object. A wall, floor, or
  cable pushes or pulls back. Draw these where the object touches the support.
- A **coordinate frame** is a pair of axes you choose, usually $x$ to the right and $y$ up.
  Write it on the sketch so every component has a sign.

### Steps to draw a free-body diagram

1. Name the object you are studying. Draw it as a simple shape.
2. Find every point where something touches it. Each touch point gets a force arrow.
3. Add the weight. Always draw weight as a single arrow from the center of mass, pointing
   down, labeled $W = mg$.
4. Pick axes. Put $x$ and $y$ on the sketch.
5. Label each force with a symbol and a unit. Do not decide the magnitudes yet.
6. Check that every arrow touches the object (or acts through it) and that you did not draw an
   internal force.

### Common ways to go wrong

- Drawing a force the object exerts on something else. An FBD shows forces on the object only.
- Forgetting weight, or drawing it on the wrong side of the object.
- Drawing a normal force perpendicular to a surface that is not level without tilting it
  correctly.
- Leaving out a support that is actually holding the object.

### Sketch for the sign problem

Here is a rough picture of the sign from lesson 01. The sign hangs from two cables that meet a
bar at angle $\theta$ to the horizontal.

```
        cable 1          cable 2
           \   theta   θ   /
            \  \       /  /
             \  \     /  /
    ----------\--+---+--/----------  horizontal bar
                 |   |
              [ sign ]
                 |
                 v  W = m g
```

In the simplified drawing the two cable forces $T$ are along each cable. Each cable has a
vertical part $T\sin\theta$ and a horizontal part $T\cos\theta$. The horizontal parts cancel by
symmetry.

### The free-body diagram for the knot

The knot where the cables meet is the object that carries the load. Its FBD has three forces:

- $T$ along cable 1, pointing up and out at angle $\theta$
- $T$ along cable 2, pointing up and out at the same angle
- $W$ straight down from the sign

The knot is in equilibrium, so the arrows must balance. The lesson Pick the governing principles writes this balance as
equations.

## Key equations

A sketch is not an equation, but it sets up the components you will need:

$$
T_{\text{vertical}} = T\sin\theta, \qquad T_{\text{horizontal}} = T\cos\theta
$$

Each cable's vertical component is $T\sin\theta$ when $\theta$ is measured from the horizontal.

## Worked example

**Problem.** A box of mass $m = 5.0\ \text{kg}$ sits on a flat floor. Draw its free-body diagram
and list the forces.

**Given:** mass $m = 5.0\ \text{kg}$, gravity $g = 9.81\ \text{m/s}^2$ (Earth surface), flat horizontal floor,
no push or pull applied sideways.

**Find:** the forces acting on the box, and their directions.

**Assumptions:** the box does not slide (friction is not needed to explain it), and the floor is
level.

**Solution.**

1. Draw the box as a square.
2. Weight: a downward arrow from the center, $W = mg = 5.0 \times 9.81 = 49.05\ \text{N}$.
3. Floor: an upward arrow from the bottom face, called the normal force $N$.
4. No other contacts, so no other arrows.
5. Axes: $y$ up, $x$ to the right.

**Answer:** Two forces. $W = 49.05\ \text{N}$ down, and $N$ up with $N$ still unknown until we
apply equilibrium in lesson 03.

**Sanity check:** a 5 kg box is about the mass of a bag of sugar. Its weight of about 50 N is
about the force you feel holding a bag like that. The arrows must be two, opposite, and the same
length if the box is at rest.

## Practice

1. A 5.0 kg box hangs straight from a rope. What is the tension $T$ in the rope, in newtons?
2. The same 5.0 kg box sits on a level floor. What is the normal force $N$ in newtons?
3. The same 5.0 kg box hangs from two ropes, each at 45 degrees to the horizontal, and the
   two ropes share the load equally. What is the tension in each rope, in newtons?

<details><summary>Answers</summary>

1. 49.05 N
2. 49.05 N
3. 34.68 N

</details>

## Common mistakes

- Drawing a force on the wrong object. Every arrow on an FBD acts on the object in the box.
- Forgetting weight. It acts on every object with mass, even one that is standing still.
- Labeling a force with a symbol but no unit, or reusing one symbol for two different forces.
- Making the sketch so small that arrows overlap and cannot be read.
- Choosing axes after writing equations. Pick them first and write them on the picture.

## Go deeper

- [University Physics Volume 1](https://openstax.org/details/books/university-physics-volume-1) by OpenStax: the chapters on forces and Newton's laws include free-body diagrams.
- [Classical Mechanics (8.01SC)](https://ocw.mit.edu/courses/8-01sc-classical-mechanics-fall-2016/) by MIT OpenCourseWare: lecture materials on forces and free-body diagrams.
- [Engineering LibreTexts](https://eng.libretexts.org/) by LibreTexts: a free library of engineering textbooks; search its mechanics and statics shelves for free-body diagram practice.
- [Problem-solving reference](reference.md): the lookup sheet for this topic.
