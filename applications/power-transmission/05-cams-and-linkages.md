# Cams and linkages

**Type:** lesson

**Cams and linkages** are two ways to turn one motion into another, such as spinning into rocking or spinning into sliding: a linkage uses rigid bars joined by pins, and a cam uses a shaped disc or groove to make a follower move in any pattern the designer chooses. Engineers use both to get motion that a plain gear or belt cannot give, and they check the geometry for locking, binding, and excess force before they build anything.

**Prerequisites:** [Trigonometry](../../math/02-trigonometry.md), [Single-variable calculus](../../math/03-single-variable-calculus.md), [Particle dynamics](../../physics/02-particle-dynamics.md), [Rigid body dynamics](../../physics/03-rigid-body-dynamics.md)
**Time:** 8 to 10 h

## Core ideas

### How it works

A **four-bar linkage** has four rigid links joined by four pin joints. One link is fixed to the frame, and
it is called the **ground link**. The two links joined to ground are the **crank** and the **rocker**, and the
link between them is the **coupler**. When one link turns at a constant speed, every point on the
linkage moves in a repeating path. The motion depends only on the link lengths and the starting angle.

A **slider-crank** replaces one rocker with a slider that moves in a straight guide. The engine piston
and crank use this arrangement. The crank turns, the connecting rod pushes and pulls, and the piston
moves back and forth in its bore.

A **cam** is a rotating shape, or a groove cut into a drum. A **follower** rides on the cam and moves up and
down, or side to side, as the cam turns. The follower motion is set directly by the cam profile. The
profile is the path the follower must trace, so the design problem is to shape the cam so that the
follower moves the way the job needs.

### Main parts

The four-bar uses four links and four pin joints. The slider-crank adds a slider block and a guide.
A cam set uses a cam, a follower, and a spring or a positive guide that keeps the follower on the
cam. A roller follower has a small roller at the contact point. A flat-faced follower has a flat
face. A knife-edge follower has a sharp tip, which wears fast and is rarely used.

### Variants

Four-bar linkages come in classes that depend on the link lengths. A crank-rocker has a crank that
turns fully and a rocker that swings back and forth. Windshield wipers use this form. A double-crank,
or drag-link, linkage has two links that turn fully. A triple-rocker has no link that turns fully. Each
form gives a different output motion.

Cams come in disc (plate) cams, cylindrical cams with a groove around a drum, and face cams with a
groove cut into a flat face. Followers come in translating and oscillating forms. The translating
follower moves in a straight line, and the oscillating follower swings on a pivot.

## Key equations

Grashof criterion for a four-bar linkage. Let $s$ be the shortest link, $l$ the longest, and $p$ and $q$
the other two, all in metres (m). The linkage is Grashof when

$$s + l \le p + q$$

A Grashof linkage has at least one link that rotates fully. The shortest link does so when it is the ground link or is adjacent to the ground link. A linkage that is not Grashof has no link that rotates fully.

Slider-crank position. With crank radius $r$ in metres, connecting rod length $L$ in metres, and crank
angle $\theta$ in radians (rad) measured from the cylinder axis, the piston position $x$ in metres from
the crank centre is

$$x = r\cos\theta + \sqrt{L^2 - r^2\sin^2\theta}$$

The stroke is the total travel, $2r$ in metres.

Cam follower displacement for simple harmonic motion (SHM) over a rise of height $h$ in metres during a cam
rotation angle $\beta$ in rad, with the cam turning at angular speed $\omega$ in radians per second (rad/s):

$$s(\theta) = \frac{h}{2}\left(1 - \cos\frac{\pi\theta}{\beta}\right)$$

Peak follower velocity in metres per second (m/s) and peak acceleration in metres per second squared ($\text{m/s}^2$):

$$v_{\mathrm{max}} = \frac{\pi h \omega}{2\beta}, \qquad a_{\mathrm{max}} = \frac{\pi^2 h \omega^2}{2\beta^2}$$

Pressure angle $\phi$ for a radial roller follower with prime circle radius $r_p$ in metres. The prime circle is the base circle radius plus the roller radius, $r_p = r_{\mathrm{base}} + r_{\mathrm{roller}}$:

$$\tan\phi = \frac{ds/d\theta}{r_p + s}$$

The pressure angle is the angle between the follower force and the follower motion. A larger angle means
more side load on the follower, and more friction and binding.

## Worked example

**Given:** A cam drives a radial roller follower through a rise of $h = 20\ \text{mm}$ during a cam
rotation of $\beta = 120^\circ$, with simple harmonic motion. The cam turns at $300\ \text{rpm}$, and its
prime circle radius (base circle plus roller radius) is $r_p = 30\ \text{mm}$.

**Find:** (a) the peak follower velocity, (b) the peak follower acceleration, and (c) the peak pressure angle.

**Solution:**

1. Angular speed: $\omega = 300 \times 2\pi / 60 = 31.4\ \text{rad/s}$.
2. Convert the rise and the angle: $h = 0.020\ \text{m}$ and $\beta = 2.094\ \text{rad}$.
3. Peak velocity: $v_{\mathrm{max}} = \dfrac{\pi \times 0.020 \times 31.4}{2 \times 2.094} = 0.471\ \text{m/s}$.
4. Peak acceleration: $a_{\mathrm{max}} = \dfrac{\pi^2 \times 0.020 \times 31.4^2}{2 \times 2.094^2} = 22.2\ \text{m}/\text{s}^2$.
5. Pressure angle: the slope $ds/d\theta$ peaks at $h\pi/(2\beta) = 0.0150\ \text{m/rad}$, and the
   pressure angle is largest where the ratio of slope to radius peaks. Evaluating the expression over
   the rise gives a peak of $\phi = 21.2^\circ$ at about $50^\circ$ of cam rotation.

**Answer:** (a) $v_{\mathrm{max}} = 0.471\ \text{m/s}$. (b) $a_{\mathrm{max}} = 22.2\ \text{m}/\text{s}^2$. (c) $\phi_{\mathrm{max}} = 21.2^\circ$.

**Sanity check:** The peak velocity equals $h\omega$ times $\pi/(2\beta)$. Here $h\omega = 0.628\ \text{m/s}$
and $\pi/(2\beta) = 0.75$, so the product is $0.471\ \text{m/s}$. A pressure angle of about $21^\circ$ sits
under the common design guideline of about $30^\circ$ for translating followers (typical value).

## Design trade-offs

- Linkage versus cam. A linkage has few parts, low cost, and pins that wear slowly. A cam gives any
  motion the designer wants, but the profile is machined to tight tolerance and the contact wears.
- Speed versus acceleration. Higher cam speed raises the acceleration as the square of $\omega$. Peak
  acceleration sets the force on the follower and the spring, so a high-speed cam uses a gentler curve
  than SHM, such as a modified sine or cycloidal curve.
- Pressure angle versus size. A larger base circle lowers the pressure angle. A larger cam takes more
  space and mass.
- Link lengths versus range. Longer links give larger motion but also larger swept volume and more
  inertia. Short links reach a locking position more easily.
- Spring force versus follower motion. A spring must hold the follower on the cam at the highest
  acceleration. Too little force lets the follower jump off the cam. Too much force raises wear and torque.

## How it fails

- Follower jump. At high speed, the follower leaves the cam because the spring cannot supply enough force
  to match the deceleration. The warning is a rattle or a sharp impact at the valve or follower.
- Binding. A high pressure angle pushes the follower sideways against its guide. The follower sticks,
  and the cam wears unevenly.
- Dead points. A linkage can reach a position where the transmission angle is near zero or where the
  output cannot be driven. The machine stalls at that angle, so the designer checks the full cycle.
- Wear. Contact stress on the cam surface pits and grinds it. Pin joints gain play, which adds error to
  the motion.
- Fatigue of links. Each link carries alternating loads, and cracks start at holes and fillets.

> [!WARNING]
> Safety measures include guards around pinch points, lubrication at the cam contact, hardened cam
> surfaces, and a check of the whole motion cycle for locking before the mechanism runs.

## History

Al-Jazari described cam-driven mechanisms in his book on ingenious mechanical devices, completed in
1206 in Diyarbakir. Engineers used cams in clocks, mills, and automata for centuries before motion
analysis was written down. James Watt used a linkage in his steam engine around 1784 to convert the
rocking beam into straight-line motion. Franz Grashof published the criterion for four-bar linkages in
1883, and it is still the standard test.

## Practice

1. A four-bar linkage has links of $20$, $50$, $40$, and $60\ \text{mm}$, with the $60\ \text{mm}$ link
   fixed to the frame. Is the linkage Grashof, and which link can rotate fully?
2. A slider-crank has a crank radius of $50\ \text{mm}$. Find the stroke of the piston.
3. A slider-crank has $r = 0.040\ \text{m}$ and $L = 0.160\ \text{m}$. Find the piston position from the crank
   centre when $\theta = 90^\circ$.
4. A cam with SHM rises $15\ \text{mm}$ over $90^\circ$ and turns at $600\ \text{rpm}$. Find the peak follower
   velocity and peak acceleration.
5. A four-bar linkage has links of $40$, $50$, $60$, and $100\ \text{mm}$, with the $100\ \text{mm}$ link fixed.
   Is the linkage Grashof? Can any link rotate fully?

<details><summary>Answers</summary>

1. The shortest link is $s = 20$ and the longest is $l = 60$. Then $s + l = 80$ and $p + q = 40 + 50 = 90$.
   Since $80 \le 90$, the linkage is Grashof. The shortest link is adjacent to the ground link, so it is a
   crank that rotates fully.
2. Stroke $= 2r = 100\ \text{mm}$.
3. $x = 0.040\cos 90^\circ + \sqrt{0.160^2 - (0.040\sin 90^\circ)^2} = \sqrt{0.0240} = 0.155\ \text{m}$, or $155\ \text{mm}$.
4. $\omega = 600 \times 2\pi/60 = 62.8\ \text{rad/s}$. With $\beta = \pi/2$, $v_{\mathrm{max}} = h\omega = 0.015 \times 62.8 = 0.942\ \text{m/s}$.
   $a_{\mathrm{max}} = 2h\omega^2 = 2 \times 0.015 \times 62.8^2 = 118\ \text{m}/\text{s}^2$.
5. The shortest link is $s = 40$ and the longest is $l = 100$. Then $s + l = 140$ and $p + q = 50 + 60 = 110$.
   Since $140 > 110$, the linkage is not Grashof. No link can rotate fully, so it is a triple-rocker.

</details>

## Common mistakes

- Applying the Grashof test with the wrong pairs. The test always adds the shortest and longest links, and
  compares the sum with the other two.
- Taking the stroke as the crank radius. The stroke is twice the radius.
- Assuming the slider's peak speed happens at $90^\circ$. For a slider-crank, the peak speed occurs at a
  crank angle that depends on the rod ratio $L/r$.
- Using SHM for a fast cam without checking $a_{\mathrm{max}}$. Acceleration grows with the square of the speed, and
  it sets the spring force and the follower load.
- Forgetting that the pressure angle is measured from the follower motion, not from the cam surface.

## Go deeper

- [Design and Manufacturing I, lecture notes](https://ocw.mit.edu/courses/2-007-design-and-manufacturing-i-spring-2009/pages/lecture-notes/)
  by MIT OpenCourseWare: session notes on two-dimensional mechanism analysis, four-bar synthesis, and belts,
  chains, and cams.
- [Design and Manufacturing I, course page](https://ocw.mit.edu/courses/2-007-design-and-manufacturing-i-spring-2009/)
  by MIT OpenCourseWare: the full course with its lecture and assignment materials.
- Related lesson. [Clutches and brakes](04-clutches-and-brakes.md) for the friction parts that stop a
  cam-driven mechanism or hold it in place.
- [Applications reference](../reference.md): the lookup sheet for this topic.
