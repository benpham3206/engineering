# Couplings and universal joints

**Type:** lesson

A coupling joins two shafts so that torque passes from one to the other. Real shafts never line up exactly, so the coupling must accept some misalignment without binding, wearing out, or pushing side loads into the bearings.

**Prerequisites:** [Axial and torsion](../../physics/04-axial-and-torsion.md), [Rigid body dynamics](../../physics/03-rigid-body-dynamics.md), [Shafts and bearings](../../design/08-shafts-and-bearings.md), [Trigonometry](../../math/02-trigonometry.md)
**Time:** 5-7 h

## Core ideas

- **Torque and speed.** A coupling carries torque $T$ (N m) at a shared angular speed $\omega$ (rad/s). The power through it is $P = T\omega$ (W). For a given power, the torque rises as the speed falls.
- **Misalignment.** Parallel offset moves one shaft sideways from the other. Angular misalignment tilts one shaft against the other. Axial misalignment changes the gap between the shaft ends. Most installations have all three in small amounts, and they grow as the machine heats up and the base settles.
- **Rigid couplings.** A rigid coupling, such as a clamp or flange coupling, has no flexible element. It is stiff and has no backlash, but it needs close alignment. Any misalignment bends each shaft once per revolution and loads the bearings.
- **Flexible couplings.** A flexible coupling adds a compliant element, such as an elastomer spider, a bellows, or a disc pack. The element bends or shears to take up misalignment. The cost is lower torsional stiffness, and the element wears or ages.
- **Universal joints.** A universal joint, also called a Cardan joint, connects two shafts at an angle through a cross-shaped spider between two yokes. It handles much larger angles than a flexible coupling. Its output speed rises and falls twice per revolution when the shafts are at an angle.
- **Constant velocity joints.** A CV joint keeps the output speed equal to the input speed at any angle within its range. Ball-type and tripod designs are common in front-wheel-drive axles. They cost more than a Cardan joint and need a sealed boot to hold grease.

### How it works

A rigid coupling carries torque by friction, keys, or bolts. Torque moves in three steps:

1. The driving shaft turns the first hub.
2. The hub passes torque to the second hub through a clamp, a key, or the bolts of a flange.
3. The second hub turns the driven shaft at the same speed, because the two hubs are locked together.

A flexible coupling works the same way, except that the element between the hubs takes up part of the motion. Torque passes through the element, and the element bends or shears to follow the misalignment.

A Cardan joint works differently. The input yoke turns the cross, and the cross carries torque to the output yoke through two pairs of bearings. When the shafts make an angle $\theta$, each yoke must swing as it turns. The output yoke therefore runs fast in one part of the turn and slow in another, even though the input speed is constant.

### Main parts

- **Hubs and yokes.** The hub clamps or bolts to a shaft. A U-joint yoke forks around the cross.
- **Flexible element.** The part that takes up misalignment, such as the spider, the bellows, or the disc pack.
- **Cross and needle bearings.** In a U-joint, the four journals of the cross ride in needle bearings held by the yokes.
- **Clamps, keys, and bolts.** A key carries torque in a keyway. A clamp carries torque by friction, so its bolts must hold enough preload.
- **Boot and grease.** A CV joint keeps its balls and races in grease inside a flexible boot.

### Variants

- **Rigid.** Sleeve (muff) couplings, clamp couplings, and flange couplings.
- **Flexible.** Jaw couplings with an elastomer spider, bellows, disc packs, grid couplings, and Oldham couplings. An Oldham coupling takes parallel offset but no large angle.
- **Universal.** A single Cardan joint, a double joint with two Cardan joints in one line, and CV joints of ball or tripod type.

## Key equations

Power and torque, with $n$ in rev/min:

$$T = \frac{P}{\omega}, \qquad \omega = \frac{2\pi n}{60}$$

Here $P$ is power in watts (W), $\omega$ is angular speed in rad/s, and $T$ is torque in newton metres (N m).

Twist of a uniform shaft of length $L$ (m) with shear modulus $G$ (Pa) and polar second moment of area $J$ (m$^4$):

$$\theta = \frac{T L}{G J}, \qquad k_t = \frac{G J}{L}$$

Here $\theta$ is the angle of twist in radians and $k_t$ is torsional stiffness in N m/rad. Steel has a shear modulus of about $79$ GPa (typical).

Single Cardan joint with joint angle $\theta$ between the shaft axes, input angle $\varphi$, and output angle $\psi$:

$$\tan\psi = \cos\theta\,\tan\varphi$$

$$\frac{\omega_{out}}{\omega_{in}} = \frac{\cos\theta}{1 - \sin^2\theta\,\sin^2\varphi}$$

With a constant input speed, the output speed reaches its maximum at $\varphi = 90^\circ$ and its minimum at $\varphi = 0^\circ$:

$$\omega_{max} = \frac{\omega_{in}}{\cos\theta}, \qquad \omega_{min} = \omega_{in}\cos\theta, \qquad \frac{\omega_{max}}{\omega_{min}} = \frac{1}{\cos^2\theta}$$

Two equal joints, with the yokes on the middle shaft lying in one plane, cancel the output speed fluctuation. The middle shaft still fluctuates, but the output does not.

## Worked example

**Given:** A 5 kW motor drives a driveshaft at $n = 1500$ rev/min through a single Cardan joint set at $\theta = 20^\circ$.

**Find:** (a) the torque on the driveshaft, (b) the maximum and minimum output speed, and (c) the ratio of the maximum to the minimum output speed.

**Assumptions:** The power is steady. The shafts are rigid. The input speed is constant, the joint angle is constant, and friction losses are ignored.

**Solution:**

1. Input angular speed: $\omega_{in} = 2\pi(1500)/60 = 157.08$ rad/s.
2. Torque: $T = P/\omega_{in} = 5000/157.08 = 31.83$ N m.
3. Cosine of the joint angle: $\cos 20^\circ = 0.9397$.
4. Minimum output speed: $\omega_{min} = 1500 \times 0.9397 = 1409.5$ rev/min.
5. Maximum output speed: $\omega_{max} = 1500 / 0.9397 = 1596.3$ rev/min.
6. Ratio: $\omega_{max}/\omega_{min} = 1/\cos^2 20^\circ = 1.1325$.

**Answer:** (a) $31.8$ N m. (b) The output speed swings between $1410$ and $1596$ rev/min. (c) The ratio is $1.13$.

**Sanity check:** The torque times the angular speed gives back the power: $31.83 \times 157.08 = 5000$ W. The swing is about 6 percent above and below the mean speed, which matches $\cos 20^\circ$ and $1/\cos 20^\circ$. A bigger joint angle makes the swing larger. At 45 degrees, the output reaches $1/\cos 45^\circ = 1.41$ times the input speed at its peak and $\cos 45^\circ = 0.71$ times at its lowest.

## Design trade-offs

- **Rigid against flexible.** A rigid coupling is cheap and stiff, so it suits a servo drive that needs exact position. It demands tight alignment, which costs setup time. A flexible coupling tolerates misalignment and damps vibration, but its element has less stiffness and limits speed and temperature.
- **Bellows against elastomer.** A bellows has no backlash and runs at high speed, but it has a fixed angle limit and can crack from fatigue. An elastomer spider is cheap and damps vibration, but it ages and generates heat.
- **Cardan against CV.** A Cardan joint is cheap and tolerates large angles, but its speed fluctuation causes vibration. A CV joint runs smooth at any angle in its range, but it costs more, needs a boot, and has a lower maximum angle.
- **Rating against shock.** Rated torque is the steady value. Starts, stops, and shocks can exceed it several times over. Use the maker's service factors for the duty, and check the peak torque, not only the average.
- **Balance and speed.** A driveshaft that runs fast must be balanced. An unbalanced shaft whirls, and the whirl can reach a critical speed.

## How it fails

- **Elastomer element wear.** The spider softens, cracks, or tears. Warning signs are rubber dust, heat at the hub, and rising vibration. The usual cause is misalignment beyond the rating or high temperature. Check alignment and replace the element on a schedule.
- **Bellows fatigue.** Repeated flexing beyond the angle rating cracks a convolution. A visible crack or a sudden rise in vibration is the warning. Stay within the rated angle and axial travel.
- **Needle bearing failure in a U-joint.** Lost grease, dirt, or running beyond the rated angle wears the needle bearings. A clunk or a vibration that rises with speed is the warning. Grease the joint on schedule and keep the angle inside the rating.
- **Fretting at keys and hubs.** A loose clamp or shock torque lets the hub move on the shaft. A fine powder around the key and a wobble at the hub are the warnings. Keep the clamp preload and key fit to the drawing.
- **Driveshaft whirl.** Unbalance or a speed near a critical speed makes the shaft bend and vibrate. The vibration grows at one speed range. See [Vibrations](../../physics/13-vibrations.md) for the critical speed idea.
- **Overload breakage.** A shear pin or coupling element breaks under a jam. Safety measures include a torque limiter, a guard over every rotating coupling, and lockout before service.

## History

The name honors Gerolamo Cardano, an Italian mathematician who described the joint in the 1500s. Robert Hooke studied the same joint in the 1600s, so it is also called a Hooke's joint. Alfred Rzeppa patented a ball-type constant velocity joint in the 1920s, and that design still carries his name.

## Practice

1. A motor delivers 2 kW at 1000 rev/min through a coupling. Find the torque in newton metres.
2. A single Cardan joint at $\theta = 15^\circ$ connects shafts. The input runs at 1200 rev/min. Find the maximum output speed.
3. A single Cardan joint runs at $\theta = 25^\circ$. Find the ratio of the maximum to the minimum output speed.
4. A solid steel shaft is 0.50 m long and 25 mm in diameter, with $G = 79$ GPa (typical). It carries 50 N m. Find the angle of twist in degrees.

<details><summary>Answers</summary>

1. $\omega = 2\pi(1000)/60 = 104.72$ rad/s, so $T = 2000/104.72 = 19.1$ N m.
2. $\omega_{max} = 1200/\cos 15^\circ = 1242$ rev/min.
3. $1/\cos^2 25^\circ = 1.217$.
4. $J = \pi(0.025)^4/32 = 3.83 \times 10^{-8}$ m$^4$, so $\theta = (50)(0.50)/(79\times10^9 \times 3.83\times10^{-8}) = 0.00825$ rad, which is $0.47^\circ$.

</details>

## Common mistakes

- Putting rev/min into the power formula. $T = P/\omega$ needs $\omega$ in rad/s.
- Assuming a single Cardan joint gives a constant output speed. Only a double-joint arrangement with coplanar yokes cancels the fluctuation.
- Treating alignment as done after the first setup. Misalignment changes as the machine heats up and as the base settles.
- Choosing a coupling by bore size alone. Check the torque, speed, angle, and misalignment ratings.
- Using the shaft twist formula for an elastomer element. The element has its own stiffness, from the maker's data.

## Go deeper

- [University Physics Volume 1, Chapter 10 introduction](https://openstax.org/books/university-physics-volume-1/pages/10-introduction) by OpenStax: fixed-axis rotation, torque, and rotational motion.
- [2.003SC Engineering Dynamics](https://ocw.mit.edu/courses/2-003sc-engineering-dynamics-fall-2011/) by MIT OpenCourseWare: rigid-body rotation in planar motion.
- [Lead screws and ball screws](08-lead-screws-and-ball-screws.md): the next lesson, on linear motion from rotation.
- [Mechatronic systems](../../design/11-mechatronic-systems.md): why the coupling sits between the motor encoder and the load.
- [Vibrations](../../physics/13-vibrations.md): natural frequency and critical speed.
- [Applications reference](../reference.md): the lookup sheet for this topic.
