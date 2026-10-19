# Electricity and magnetism

**Type:** lesson

**Electricity and magnetism** are the linked forces that act on electric charge and the currents it makes. Motors, generators, sensors, and every electronic circuit depend on them, and engineers use these ideas to size wiring, design power supplies, and predict how a coil or magnet will respond to a changing current.

**Prerequisites:** [Algebra](../math/01-algebra.md), [Trigonometry](../math/02-trigonometry.md), [Single-variable calculus](../math/03-single-variable-calculus.md) (Faraday's law uses a rate of change of flux)
**Time:** 8-10 h

## Core ideas

- **Electric charge** is a property of matter that causes electric forces. Its SI unit is the coulomb (C). Like charges repel and opposite charges attract. The elementary charge, carried by a single electron or proton, is about $1.602 \times 10^{-19}$ C.
- **Electric field** ($\vec{E}$) is the force per unit charge that a test charge would feel at a point. Its units are newtons per coulomb (N/C), which equal volts per meter (V/m).
- **Electric potential** ($V$) is energy per unit charge. Its unit is the volt (V). A voltage is a difference in potential between two points.
- **Current** ($I$) is the rate of charge flow, measured in amperes (A), where $1\ \mathrm{A} = 1\ \mathrm{C/s}$. Conventional current is taken as the direction positive charge would move.
- **Resistance** ($R$) is how strongly a material opposes current. Its unit is the ohm ($\Omega$). Wire and copper have very low resistance. Heaters and some sensors have high resistance by design.
- **Ohm's law** says that for many conductors, voltage equals current times resistance.
- **Series and parallel.** In a series circuit, the same current flows through every element, and resistances add. In a parallel circuit, every element sees the same voltage, and the reciprocals of resistances add.
- **Power** is the rate of energy transfer. In a resistor, $P = VI$, measured in watts (W).
- **Magnetic field** ($\vec{B}$) describes how a magnet or current pushes on moving charges. Its SI unit is the tesla (T). In US customary texts, the gauss is also used, where $1\ \mathrm{T} = 10{,}000\ \mathrm{G}$.
- **Magnetic force on a moving charge** is perpendicular to both the velocity and the field. A charge moving parallel to the field feels no force.
- **Magnetic force on a wire** carrying current in a field is perpendicular to both the wire and the field.
- **Magnetic flux** ($\Phi_B$) is the field passing through a loop, measured in webers (Wb). A changing flux induces a voltage around the loop. This is electromagnetic induction.
- **Lenz's law** says the induced current opposes the change in flux that produced it. The minus sign in Faraday's law carries this idea.

Ideas that tie the topics together:

- **Conductors** such as copper have free charges that move easily. **Insulators** such as rubber or glass hold their charges in place.
- **Voltage sources** such as batteries push charges around a loop. Kirchhoff's voltage law says the sum of voltage rises and drops around any closed loop is zero.
- **Kirchhoff's current law** says the currents entering a junction equal the currents leaving it.
- **Energy and voltage.** A potential difference of 1 V gives a charge of 1 C an energy change of 1 J.
- **Right-hand rule.** For a current in a straight wire, point the thumb along the current and the fingers curl in the direction of the magnetic field around the wire.
- **Power in a circuit** is always the voltage across an element times the current through it. A 60 W bulb on a 120 V circuit draws $60 / 120 = 0.5$ A.
- **Electromagnetic coupling** links electricity and magnetism. A changing magnetic field makes an electric field, and a current makes a magnetic field. Motors use the force side, and generators use the induction side.

Assumptions behind the formulas in this lesson:

- Circuits use ideal wires and lumped resistors. This lesson ignores wire resistance.
- Fields are uniform over the region of interest.
- The magnetic field is steady or changes slowly enough that the quasi-static laws apply.

## Key equations

Symbols and units:

- $F$: force (N, or lbf)
- $q$, $q_1$, $q_2$: electric charges (C)
- $r$: distance between charges, or from a charge to a point (m, or ft)
- $k$: Coulomb constant, $k \approx 8.99 \times 10^{9}$ $\mathrm{N\cdot m^2/C^2}$ (equal to $1/(4\pi\varepsilon_0)$)
- $\vec{E}$: electric field (N/C, or V/m)
- $V$: voltage or potential difference (V)
- $I$: current (A)
- $R$: resistance ($\Omega$)
- $P$: power (W)
- $v$: speed of a charge (m/s, or ft/s)
- $B$: magnetic field magnitude (T, or G)
- $\theta$: angle between two vectors (rad or degrees)
- $\ell$: length of a wire inside the field (m, or ft)
- $A$: area of a loop ($\mathrm{m^2}$, or $\mathrm{ft^2}$)
- $\Phi_B$: magnetic flux (Wb)
- $N$: number of turns in a coil (dimensionless)
- $\mathcal{E}$: induced emf (V)

Coulomb's law (magnitude of the force between two point charges):

$$F = k\,\frac{|q_1 q_2|}{r^2}$$

Electric field from a point charge:

$$E = \frac{F}{q} = k\,\frac{|q|}{r^2}$$

Ohm's law and power:

$$V = IR, \qquad P = VI = I^2 R = \frac{V^2}{R}$$

Resistors in series and in parallel:

$$R_{\text{series}} = R_1 + R_2 + \cdots, \qquad \frac{1}{R_{\text{parallel}}} = \frac{1}{R_1} + \frac{1}{R_2} + \cdots$$

Magnetic force on a moving charge and on a current-carrying wire:

$$F = q v B \sin\theta, \qquad F = B I \ell \sin\theta$$

Magnetic flux through a loop (uniform field, angle $\theta$ between $\vec{B}$ and the area normal):

$$\Phi_B = B A \cos\theta$$

Faraday's law for a coil of $N$ turns:

$$\mathcal{E} = -N\,\frac{d\Phi_B}{dt}$$

## Worked example

**Problem.** A coil has $N = 200$ turns. Each turn has area $A = 0.010$ $\mathrm{m^2}$, and the field is perpendicular to the coil. The magnetic field increases uniformly from 0 to 0.50 T in 0.10 s.

**Find.** The magnitude of the induced emf while the field is changing.

**Assumptions.** The field is uniform over the coil, perpendicular to its plane ($\theta = 0$, so $\cos\theta = 1$), and changes at a constant rate. The coil area stays fixed.

**Solution.**

1. Change in flux per turn. Since $\Phi_B = BA$ for a field perpendicular to the coil:
   $$\Delta \Phi_B = \Delta B \cdot A = (0.50 - 0)\ \text{T} \times 0.010\ \text{m}^2 = 5.0 \times 10^{-3}\ \text{Wb}$$
2. Rate of change of total flux linkage:
   $$\frac{d\Phi_B}{dt} = \frac{\Delta \Phi_B}{\Delta t} = \frac{5.0 \times 10^{-3}\ \text{Wb}}{0.10\ \text{s}} = 5.0 \times 10^{-2}\ \text{Wb/s}$$
3. Induced emf:
   $$|\mathcal{E}| = N \left|\frac{d\Phi_B}{dt}\right| = 200 \times 5.0 \times 10^{-2}\ \text{V} = 10\ \text{V}$$

**Answer.** The induced emf has magnitude 10 V while the field is changing. Lenz's law sets its direction so the induced current opposes the increase in flux.

**Sanity check.**

- The units check out: a weber per second is a volt.
- A 10 V emf from a 200-turn coil in a 0.1 s pulse is a realistic order of magnitude for a small transformer or sensor coil.
- If the field changed in 1.0 s instead, the emf would be 1.0 V. Slower changes give smaller emf, which matches the formula.

## Practice

1. Two point charges, $+2.0\ \mu\text{C}$ and $+5.0\ \mu\text{C}$, sit 0.30 m apart in air. Find the magnitude of the electrostatic force in newtons and state whether it attracts or repels.
2. A 9.0 V battery is connected in series to a 3.0 $\Omega$ resistor and a 6.0 $\Omega$ resistor. Find the current in amperes and the voltage across the 6.0 $\Omega$ resistor.
3. A straight wire 0.40 m long carries 2.0 A and is perpendicular to a uniform 0.15 T magnetic field. Find the magnetic force on the wire in newtons.
4. A coil has 100 turns and area $0.0050$ $\mathrm{m^2}$. The field perpendicular to it changes by 0.20 T in 0.040 s. Find the magnitude of the induced emf in volts.

<details><summary>Answers</summary>

1. 1.0 N, repulsive
2. 1.0 A; 6.0 V
3. 0.12 N
4. 2.5 V

</details>

## Common mistakes

- Forgetting the micro prefix. $1\ \mu\text{C} = 10^{-6}$ C. A factor of a million error is common in charge problems.
- Using degrees in a calculator set to radians, or the reverse, when computing $\sin\theta$ or $\cos\theta$.
- Thinking an emf depends on the flux itself. Faraday's law depends on the rate of change of flux, so a steady flux gives no emf.
- Applying $F = qvB$ when the velocity is parallel to $B$. The sine is zero, so the force is zero.
- Dropping the minus sign in Faraday's law and then mixing up the direction of the induced current. Use Lenz's law to find the direction.
- Treating a battery as a source of constant current. An ideal battery holds voltage constant, and the current depends on the resistance in the loop.
- Forgetting that the magnetic force on a wire is zero when the wire runs parallel to the field.

## Go deeper

- [Physics II: Electricity and Magnetism](https://ocw.mit.edu/courses/8-02-physics-ii-electricity-and-magnetism-spring-2007/) by MIT OpenCourseWare (8.02, Spring 2007): free course materials covering electric fields, Gauss's law, circuits, magnetic fields, and Faraday's law, under a Creative Commons license.
- [Readings](https://ocw.mit.edu/courses/8-02-physics-ii-electricity-and-magnetism-spring-2007/pages/readings/) for the same course by MIT OpenCourseWare: a session-by-session list of topics and textbook chapter references, useful for choosing what to read next.
- Previous lesson: none in this folder. For the circuit and force ideas used here, the algebra in [Statics](01-statics.md) is a useful warm-up on vectors.
- [Fields, waves, and space reference](reference-fields-waves-space.md): the lookup sheet for this topic.
