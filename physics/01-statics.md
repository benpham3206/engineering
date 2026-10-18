# Statics

**Type:** lesson

Statics is the study of bodies that do not move. Engineers use it to find the forces in cables, trusses, frames, and supports before they size anything, because a part that carries too much load fails. Every later topic in this folder builds on the free-body diagram and the equilibrium equations below.

**Prerequisites:** none in this folder. You should be comfortable with high-school algebra and basic trigonometry (sine, cosine, tangent).
**Time:** 8-12 h

## Core ideas

- A **force** is a push or pull with a size (magnitude), a direction, and a point where it acts. Forces are measured in newtons (N) in SI units or pounds-force (lbf) in US customary units.
- A **vector** has a magnitude and a direction. You add forces as vectors, usually by splitting each force into x and y components.
- A **particle** is a body small enough that all forces act at one point. Cables and pins are often modeled this way.
- A **rigid body** is a body that does not change shape. Forces can act at different points on it, so you also track moments.
- **Equilibrium** means the body is not accelerating. A body at rest is in equilibrium, and so is a body moving at a steady velocity.
- A **free-body diagram (FBD)** is a sketch of one body with every force on it drawn as an arrow. Forces from other bodies, such as a support or a rope, are included. Forces the body exerts on other bodies are not.
- A **moment** (or torque) is the turning effect of a force about a point. It equals the force times the perpendicular distance from the point to the line of action of the force.
- A **reaction** is a force that a support applies to hold the body in place. Common supports are rollers (one reaction component), pins (two components), and fixed supports (two force components and one moment).
- **Friction** resists sliding. Static friction can take any value up to a limit, $F_f \le \mu_s N$, where $\mu_s$ is the coefficient of static friction and $N$ is the normal force. The real value depends on the pair of surfaces and must come from a table or a test.

## Key equations

For a particle in two dimensions, equilibrium requires that the net force is zero:

$$\sum F_x = 0 \qquad \sum F_y = 0$$

For a rigid body in two dimensions, you also need the moments to balance:

$$\sum F_x = 0 \qquad \sum F_y = 0 \qquad \sum M_O = 0$$

Here $F_x$ and $F_y$ are force components in newtons (N), and $M_O$ is the moment about a chosen point $O$ in newton-meters (N m) or pound-feet (lb ft).

For a force $F$ at angle $\theta$ measured from the positive x axis:

$$F_x = F\cos\theta \qquad F_y = F\sin\theta$$

For a cable or rope that pulls on a joint, the magnitude of the tension $T$ in newtons is the unknown to solve for. Choose each cable's direction from the geometry of the joint, not from guesses.

## Worked example

**Given:** An 800 N load hangs from a joint. Two cables support it. Cable 1 goes up and to the left at 40 degrees above horizontal. Cable 2 goes up and to the right at 60 degrees above horizontal. The joint is in equilibrium.

**Find:** The tensions $T_1$ and $T_2$ in the two cables.

**Assumptions:** The cables are light and carry only tension. The joint is a particle. Weight acts straight down.

**FBD description:** Draw a dot for the joint. Draw $T_1$ from the dot up and to the left at 40 degrees above the horizontal. Draw $T_2$ from the dot up and to the right at 60 degrees above the horizontal. Draw the 800 N weight straight down from the dot.

**Solution:**

Horizontal balance, with left as negative:

$$-T_1\cos 40^\circ + T_2\cos 60^\circ = 0$$

so

$$T_1 = T_2\frac{\cos 60^\circ}{\cos 40^\circ}$$

Vertical balance:

$$T_1\sin 40^\circ + T_2\sin 60^\circ - 800\ \text{N} = 0$$

Substitute the first result into the second and solve for $T_2$:

$$T_2 = \frac{800}{\dfrac{\cos 60^\circ}{\cos 40^\circ}\sin 40^\circ + \sin 60^\circ} \approx 622.3\ \text{N}$$

Then

$$T_1 = 622.3 \times \frac{\cos 60^\circ}{\cos 40^\circ} \approx 406.2\ \text{N}$$

**Answer:** $T_1 \approx 406.2$ N and $T_2 \approx 622.3$ N.

**Sanity check:** The cable at the steeper angle, 60 degrees, is the one that carries more of the vertical load, so $T_2$ should be larger. It is. Substituting back, the horizontal sum is $-406.2\cos 40^\circ + 622.3\cos 60^\circ = 0$ (both terms about 311 N), and the vertical sum is $406.2\sin 40^\circ + 622.3\sin 60^\circ = 800$ N. Both checks pass.

## Practice

1. A 50 kg block sits on a horizontal floor with $\mu_s = 0.4$. Find the largest horizontal pull P, in newtons, before the block starts to slide. Use $g = 9.81\ \text{m/s}^2$.
2. A 500 N load hangs from two symmetric cables. Each cable makes 45 degrees with the horizontal. Find the tension in each cable, in newtons.
3. A simply supported beam 10 m long carries a 12 kN point load at its midspan. Find the magnitude of each support reaction, in newtons. Neglect the beam's own weight.

<details><summary>Answers</summary>

1. About 196.2 N
2. About 353.6 N each
3. 6000 N each

</details>

## Common mistakes

- Drawing forces that the body exerts on other bodies. Only forces acting on the body go on its FBD.
- Mixing up sine and cosine for an angle. Measure every angle from the same axis, and check that the components of a force with a 90-degree angle are $F\cos 90^\circ = 0$ and $F\sin 90^\circ = F$.
- Writing only the force equations for a rigid body. A body that can rotate also needs $\sum M = 0$.
- Using $\mu_s N$ as the actual friction force. Static friction is only the maximum value. Find the actual friction from equilibrium first.
- Forgetting the units. Keep every force in N or every force in lbf, not a mix.

## Go deeper

- [Engineering Statics: Open and Interactive, Chapter 3, Equilibrium of Particles](https://eng.libretexts.org/Bookshelves/Mechanical_Engineering/Engineering_Statics:_Open_and_Interactive_(Baker_and_Haynes)/03:_Equilibrium_of_Particles) by Daniel W. Baker and William Haynes, LibreTexts: particle equilibrium in 2D and 3D with worked problems, CC BY-NC-SA 4.0.
- [Engineering Statics: Open and Interactive, Chapter 5, Rigid Body Equilibrium](https://eng.libretexts.org/Bookshelves/Mechanical_Engineering/Engineering_Statics:_Open_and_Interactive_(Baker_and_Haynes)/05:_Rigid_Body_Equilibrium) by Daniel W. Baker and William Haynes, LibreTexts: moments, support reactions, and the three rigid-body equilibrium equations.
- Next: [Particle dynamics](02-particle-dynamics.md), once you can draw an FBD and solve a 2D equilibrium problem.
- [Mechanics reference](reference-mechanics.md): the lookup sheet for this topic.
