# Trigonometry

**Type:** lesson

Trigonometry turns angles into lengths and back again. Engineers use it to split a force into horizontal and vertical parts, find the length of a brace, and describe anything that repeats, such as vibration and AC power.

**Prerequisites:** [Algebra](01-algebra.md)
**Time:** 8-10 h

## Core ideas

- An angle can be measured in degrees (360 per full turn) or radians ($2\pi$ per full turn). Calculators and Python's math functions use radians by default. Convert with $\theta_{\text{rad}} = \theta_{\text{deg}} \cdot \pi / 180$.
- In a right triangle, the three sides have names relative to an angle $\theta$: the opposite side, the adjacent side, and the hypotenuse (the longest side, opposite the right angle).
- SOH-CAH-TOA is the memory aid: $\sin\theta = \text{opposite}/\text{hypotenuse}$, $\cos\theta = \text{adjacent}/\text{hypotenuse}$, $\tan\theta = \text{opposite}/\text{adjacent}$.
- A force $F$ at an angle $\theta$ from the horizontal has components $F_x = F\cos\theta$ and $F_y = F\sin\theta$. This is the most common use in statics.
- For triangles that are not right triangles, use the law of cosines and the law of sines. They connect sides and angles in any triangle.
- Sine and cosine are periodic. They repeat every $2\pi$ radians. That makes them the natural description of vibration, rotation, and AC current.
- Identities such as $\sin^2\theta + \cos^2\theta = 1$ let you simplify expressions. Use them when a formula has both sine and cosine.

## Key equations

Right-triangle definitions:

$$\sin\theta = \frac{\text{opp}}{\text{hyp}}, \quad \cos\theta = \frac{\text{adj}}{\text{hyp}}, \quad \tan\theta = \frac{\text{opp}}{\text{adj}}$$

Force components, where $F$ is the force magnitude (N or lbf) and $\theta$ is measured from the $x$-axis:

$$F_x = F\cos\theta, \qquad F_y = F\sin\theta$$

Law of cosines, for a triangle with sides $a$, $b$, $c$ (m or ft) and angle $\gamma$ opposite $c$:

$$c^2 = a^2 + b^2 - 2ab\cos\gamma$$

Symmetric two-cable support of a vertical load $W$ (N or lbf), with each cable at angle $\alpha$ to the horizontal:

$$T = \frac{W}{2\sin\alpha}$$

## Worked example

**Given:** A cable pulls on a bracket with a force of $F = 1200\ \mathrm{N}$ at $35^\circ$ above the horizontal.

**Find:** The horizontal and vertical components.

**Assumptions:** The angle is measured from the positive $x$-axis. The force acts at one point.

**Solution:**

1. Convert the angle if needed. Here we keep degrees, so the calculator must be in degree mode. Or convert first: $35^\circ = 35 \times \pi/180 = 0.6109\ \mathrm{rad}$.
2. Horizontal component: $F_x = 1200 \cos 35^\circ = 1200 \times 0.8192 = 982.98\ \mathrm{N}$.
3. Vertical component: $F_y = 1200 \sin 35^\circ = 1200 \times 0.5736 = 688.29\ \mathrm{N}$.

**Answer:** $F_x \approx 983\ \mathrm{N}$ and $F_y \approx 688\ \mathrm{N}$.

**Sanity check:** Pythagoras gives $\sqrt{982.98^2 + 688.29^2} = 1200.0\ \mathrm{N}$, which matches the original force. Since the angle is below $45^\circ$, the horizontal part should be larger, and it is.

A second example, a symmetric two-cable hanger at $30^\circ$ to the horizontal carrying $W = 5000\ \mathrm{N}$: $T = \dfrac{5000}{2 \sin 30^\circ} = 5000\ \mathrm{N}$ in each cable.

## Practice

1. A force of 800 N acts at $60^\circ$ above the horizontal. Find $F_x$ and $F_y$ in newtons.
2. A right triangle has opposite side 3 m and hypotenuse 5 m. Find the angle $\theta$ in degrees.
3. Two cables at $45^\circ$ each support a load $W = 2000\ \mathrm{N}$. Find the tension in each cable in newtons.
4. Two sides of a triangle are 4 m and 5 m, with a $60^\circ$ angle between them. Find the third side in meters.

<details><summary>Answers</summary>

1. $F_x \approx 400.0\ \mathrm{N}$, $F_y \approx 692.8\ \mathrm{N}$
2. $\theta \approx 36.87^\circ$
3. $T \approx 1414.2\ \mathrm{N}$
4. $\approx 4.583\ \mathrm{m}$

</details>

## Common mistakes

- Calculator set to radians when you meant degrees (or the reverse). Check the mode before every calculation.
- Using $\sin$ where $\cos$ belongs in $F_x$. Ask which component the angle is measured from.
- Forgetting that $\sin$ and $\cos$ of an angle outside $0$ to $90^\circ$ can be negative, which flips the direction of a component.
- Applying the Pythagorean formula to a triangle that has no right angle. Use the law of cosines instead.
- Rounding too early. Keep at least four significant figures until the final answer.

## Go deeper

- [Engineering LibreTexts](https://eng.libretexts.org/) by LibreTexts: free, open-access engineering textbooks. Search for statics or trigonometry.
- [Algebra notes](https://tutorial.math.lamar.edu/classes/alg/alg.aspx) by Paul Dawkins, Paul's Online Math Notes: review of the algebra used when rearranging trig formulas.
- Next: [Single-variable calculus](03-single-variable-calculus.md).
- [Math reference](reference.md): the lookup sheet for this topic.
