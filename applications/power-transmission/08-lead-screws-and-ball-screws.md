# Lead screws and ball screws

**Type:** lesson

Lead screws and ball screws are threaded rods that turn rotary motion into linear motion through a nut, and a ball screw uses steel balls that roll in the thread groove, which cuts friction. Engineers choose these screws for precise positions and large thrust, and they must check efficiency, back-driving, and the speed at which a long screw whirls.

**Prerequisites:** [Statics](../../physics/01-statics.md) (friction and moments), [Gears, fasteners, and springs](../../design/09-gears-fasteners-and-springs.md) (thread geometry and bolt preload), [Bending and buckling](../../physics/05-bending-and-buckling.md), [Mechatronic systems](../../design/11-mechatronic-systems.md) (lead and encoder counts), [Trigonometry](../../math/02-trigonometry.md)
**Time:** 5-7 h

## Core ideas

### How it works

The screw turns in its supports, and the nut moves along it. The nut is usually held against rotation by a carriage or a guide. The thread acts as an inclined plane wrapped around a cylinder. One full turn moves the nut by the lead, which is the distance the nut travels per revolution.

The motion and the force follow these steps:

1. The motor turns the screw.
2. The thread flank pushes on the nut's thread along the helix angle.
3. The nut moves along the axis by the lead for each turn, and it carries the axial load.
4. Friction on the flanks opposes the sliding, so part of the input torque is lost as heat.
5. On a vertical axis, the load pulls the nut back down the screw. Whether the screw turns back depends on friction. A plain lead screw with a shallow lead angle can hold the load, but a steep lead or low friction lets it back-drive. A ball screw has so little friction that the load turns the screw.

### Main parts

- **Screw.** A threaded shaft with a trapezoidal (Acme) or square thread on a lead screw. A ball screw has a ground thread groove, called a raceway.
- **Nut.** A bronze, plastic, or steel nut on a lead screw. A ball nut carries the balls and a return path that moves them back to the start of the raceway.
- **Balls.** Hardened steel balls roll in the raceway and recirculate through the nut.
- **Supports and bearings.** End bearings take the thrust and fix the screw axially. The length between supports sets the critical speed.
- **Lubrication and seals.** Grease or oil keeps the thread surfaces apart. Wipers and covers keep chips and dust out.

### Variants

- **Square thread.** A thread form with the highest efficiency of the plain threads. It is harder to cut and is used where efficiency matters most.
- **Acme (trapezoidal) thread.** The common form in machine tools and presses. It is easier to make and stronger than a square thread, and it is less efficient.
- **Ball screw.** The highest efficiency of the three, with low friction, a backlash-free nut when preloaded, and a tendency to back-drive.
- **Multi-start thread.** A thread with more than one start has a lead equal to the number of starts times the pitch. It gives faster travel at the same rotation speed.

## Key equations

Lead and helix angle, with $n$ starts, pitch $P$, lead $L$, and mean diameter $d_m$, all in the same length unit:

$$L = nP, \qquad \lambda = \arctan\!\left(\frac{L}{\pi d_m}\right)$$

Here $\lambda$ is the helix angle in degrees or radians, and $d_m$ is the mean diameter in metres.

Friction angle, with coefficient of friction $\mu$ (dimensionless):

$$\phi = \arctan\mu$$

Torque to raise an axial load $F$ (N) on a square thread, with $T$ in newton metres (N m):

$$T = \frac{F\,d_m}{2}\tan(\lambda + \phi)$$

Efficiency when raising the load, with $\eta$ dimensionless:

$$\eta = \frac{F L}{2\pi T} = \frac{\tan\lambda}{\tan(\lambda + \phi)}$$

Axial thrust from an input torque $T$:

$$F = \frac{2\pi\,\eta\,T}{L}$$

Self-locking for a square thread, meaning the load cannot turn the screw under static conditions:

$$\tan\lambda \le \mu$$

Speed and power, with $v$ in m/s and $\omega$ in rad/s:

$$v = \frac{\omega L}{2\pi}, \qquad P = T\omega$$

First critical speed of a solid steel screw of root diameter $d_r$ (m), supported at both ends with a span $l$ (m), modulus $E$ (Pa), and density $\rho$ (kg/m$^3$):

$$\omega_c = \frac{\pi^2}{l^2}\sqrt{\frac{EI}{\rho A}} = \frac{\pi^2 d_r}{4 l^2}\sqrt{\frac{E}{\rho}}$$

Here $I = \pi d_r^4/64$ (m$^4$) and $A = \pi d_r^2/4$ (m$^2$). Steel has $E = 200$ GPa and $\rho = 7850$ kg/m$^3$ (typical). The formula assumes simple supports, so the critical speed is lower than for a screw with fixed ends.

## Worked example

**Given:** A square-thread lead screw has a mean diameter $d_m = 20$ mm and a single-start lead $L = 4$ mm. It raises an axial load $F = 2.0$ kN. The steel-on-bronze friction coefficient is $\mu = 0.15$ (typical).

**Find:** (a) the helix angle, (b) the torque to raise the load, (c) the efficiency, and (d) whether the screw is self-locking.

**Assumptions:** The thread is square, so the tangent formulas apply. The thrust bearing friction is ignored. The speed is steady.

**Solution:**

1. Helix angle: $\lambda = \arctan(4/(\pi \times 20)) = \arctan(0.06366) = 3.64^\circ$.
2. Friction angle: $\phi = \arctan(0.15) = 8.53^\circ$.
3. Raising torque: $T = (2000)(0.020)/2 \times \tan(3.64^\circ + 8.53^\circ) = 20 \times \tan 12.17^\circ = 20 \times 0.2155 = 4.31$ N m.
4. Efficiency: $\eta = \tan 3.64^\circ / \tan 12.17^\circ = 0.06366/0.2155 = 0.295$.
5. Self-locking: $\tan\lambda = 0.0637$, which is less than $\mu = 0.15$, so the screw is self-locking.

**Answer:** (a) $3.64^\circ$. (b) $4.31$ N m. (c) $0.295$, or about 30 percent. (d) Yes, the screw is self-locking.

**Sanity check:** The ideal torque with no friction is $F L/(2\pi) = 2000 \times 0.004/(2\pi) = 1.27$ N m. The real torque is $4.31/1.27 = 3.4$ times that, which equals $1/\eta$. The efficiency of 30 percent is typical for a plain lead screw, so the motor must be sized for the friction torque, not the ideal one.

## Design trade-offs

- **Efficiency against holding.** A low-efficiency lead screw holds its position with no brake, and a ball screw needs a brake on any vertical axis. A ball screw wastes less input power, so the motor runs cooler.
- **Lead choice.** For a given torque, a small lead gives more thrust and finer resolution, but slower travel. A large lead gives fast travel and less thrust. The thrust formula $F = 2\pi\eta T/L$ shows the direct trade.
- **Length and critical speed.** The critical speed scales with root diameter over length squared. Doubling the unsupported length cuts the critical speed to a quarter. Long screws need larger diameter, closer supports, or a lower top speed.
- **Backlash.** A plain nut has some backlash. A preloaded ball nut removes most of it, at the cost of higher friction and shorter life.
- **Wear and heat.** A bronze nut wears slowly under load. A plastic nut adds friction and can strip when overtorqued. A ball screw needs seals, because dust in the raceway shortens its life.
- **Cost and accuracy.** Ball screws with tight lead error cost more than plain lead screws. Pick the accuracy grade the position need calls for.

## How it fails

- **Nut wear.** The thread wears, so backlash and lead error grow. Warning signs are loose position and a play that grows over time. The usual causes are abrasion and poor lubrication. Measure the backlash on a schedule.
- **Raceway spalling.** Overload, contamination, or misalignment pits the balls and the raceway. The warnings are noise, rough motion, and play. Keep dust seals in place and follow the lubrication schedule.
- **Load falling on a vertical axis.** Power loss lets a ball screw back-drive, and the load drops. Safety measures include a holding brake, a self-locking drive, or a counterbalance.
- **Whirling at critical speed.** A screw that runs near its critical speed bends and vibrates, with rising noise. Keep the operating speed well below the critical speed, with margin.
- **Buckling under compression.** A long, slender screw in compression can fail suddenly by lateral deflection. See [Bending and buckling](../../physics/05-bending-and-buckling.md). Support the screw and limit its stroke.
- **Stripped plastic nut.** An overtorqued nut strips its thread. Set a torque limit on the drive and check the nut thread at service.
- **Pinch points.** Exposed screws and moving carriages pinch fingers. Guard the screw and keep clear of the travel.

## History

Screw threads on machines were hard to make accurately for centuries, and a lead screw was only as good as its cutting tool. Henry Maudslay built a screw-cutting lathe around 1800 that cut accurate lead screws from a master screw, which made precise machine tools possible. Joseph Whitworth proposed a standard screw thread in 1841, which gave engineers common sizes. Ball screws came later, and they spread through machine tools and aircraft actuators because they cut friction and give precise, low-backlash motion.

## Practice

1. A lead screw has a lead of 5 mm. How far does the nut travel in 3 turns?
2. A single-start screw has a mean diameter of 30 mm and a lead of 5 mm. Find the helix angle.
3. A ball screw with an 8 mm lead and efficiency $\eta = 0.90$ receives 10 N m of input torque. Find the axial thrust in newtons.
4. A square-thread screw has a mean diameter of 20 mm and a lead of 2 mm. The friction coefficient is $\mu = 0.10$. Is the screw self-locking?
5. A solid steel screw has a root diameter of 16 mm and is supported at both ends over a span of 1.0 m. Use $E = 200$ GPa and $\rho = 7850$ kg/m$^3$ (typical). Find the first critical speed in rev/min.

<details><summary>Answers</summary>

1. $3 \times 5 = 15$ mm.
2. $\lambda = \arctan(5/(\pi \times 30)) = \arctan(0.05305) = 3.04^\circ$.
3. $F = 2\pi(0.90)(10)/0.008 = 7069$ N, which is about 7.07 kN.
4. $\tan\lambda = 2/(\pi \times 20) = 0.0318$, which is less than $\mu = 0.10$. Yes, it is self-locking.
5. $\omega_c = \pi^2(0.016)/(4 \times 1.0^2) \times \sqrt{200\times10^9/7850} = 199.3$ rad/s, which is $1903$ rev/min.

</details>

## Common mistakes

- Using the pitch as the lead on a multi-start screw. The lead equals the number of starts times the pitch.
- Using the major or minor diameter for the helix angle or the torque. Use the mean diameter.
- Forgetting that the efficiency applies to the input torque. The raising torque from the formula is the input torque, and it is larger than the ideal torque by $1/\eta$.
- Assuming a ball screw holds a vertical load. It back-drives unless a brake or a self-locking drive holds it.
- Skipping the critical speed check on a long screw. The check takes one line of arithmetic, and it prevents a whirl failure.

## Go deeper

- [Gears, fasteners, and springs](../../design/09-gears-fasteners-and-springs.md): thread geometry, tensile stress area, and preload.
- [Mechatronic systems](../../design/11-mechatronic-systems.md): how a lead screw sets the travel per encoder count.
- [CNC machines](../machines-robots/03-cnc-machines.md): ball screws move the axes of a machine tool.
- [Gear trains](01-gear-trains.md): the rotary side of the drive, when a gear reduces the speed before the screw.
- [Flywheels](09-flywheels.md): how rotating inertia smooths the torque of an engine that drives the screw.
- [Applications reference](../reference.md): the lookup sheet for this topic.
