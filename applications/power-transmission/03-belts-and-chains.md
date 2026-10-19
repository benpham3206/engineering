# Belts and chains

**Type:** lesson

Belts and chains carry power between two shafts that sit some distance apart, so the drive needs no gears on the shafts. Designers pick the belt type, set the tension, and check the wrap and the speed ratio, because those set how much power the drive can carry without slipping. Flat, V, and timing belts and roller chains each suit different loads, speeds, and center distances.

**Prerequisites:** [Statics](../../physics/01-statics.md), [Axial and torsion](../../physics/04-axial-and-torsion.md), [Shafts and bearings](../../design/08-shafts-and-bearings.md), [Trigonometry](../../math/02-trigonometry.md)
**Time:** 4-6 h

## Core ideas

### How it works

A belt wraps around two pulleys. Friction between the belt and the pulley carries the torque from the driver to the driven pulley. The tight side of the belt carries tension $T_1$, and the slack side carries $T_2$. The difference $T_1 - T_2$ is the force that does work, so the power is $P = (T_1 - T_2) v$.

Friction makes the drive work, and it also limits it. If the tension difference exceeds the friction capacity, the belt slips. Slip lowers the speed of the driven pulley below the ideal ratio. A timing belt avoids slip by using teeth that mesh with the pulley.

A roller chain works like a belt wrapped around sprockets, but the chain links hold the load through pins and rollers instead of friction. The teeth of the sprocket engage the rollers, so a chain does not slip. It does change speed slightly within each revolution, which is the polygon effect described below.

### Main parts

- **Flat belt.** A thin band of rubber, leather, or polymer. It runs on crowned pulleys, which keep it centered.
- **V-belt.** A rubber belt with a trapezoid cross section. It wedges into a V-groove in the pulley, so it grips harder than a flat belt at the same tension.
- **Timing belt.** A toothed belt, usually with a steel or aramid cord for strength. The teeth mesh with matching teeth on the pulley.
- **Roller chain.** A chain of inner and outer links with pins and rollers. The rollers ride on the sprocket teeth.
- **Tensioner.** A pulley or slide that keeps the belt or chain tight enough to carry load without slipping or jumping teeth.

### Variants

- **Flat belts** cost little and run over long center distances, and they suit high speeds. They slip more than the other types and need high tension.
- **V-belts** are common in engines, fans, and pumps. The wedge raises the grip, and several belts can run side by side in a multi-groove pulley.
- **Timing belts** give an exact ratio with no slip, which matters for camshafts and positioning axes. They need accurate pulleys and a tension that keeps the teeth engaged.
- **Roller chains** carry high torque at low speed and tolerate heat and dirt better than belts. They need lubrication and a chain guard, and they lengthen as the pins and bushings wear.

## Key equations

Belt speed, with pulley diameter $d$ in m and speed $n$ in rpm, giving $v$ in m/s:

$$
v = \frac{\pi\, d\, n}{60}
$$

Speed ratio for a belt with slip $s$ (dimensionless), where $d_1$ is the driver pulley and $d_2$ is the driven pulley:

$$
\frac{\omega_2}{\omega_1} = \frac{d_1}{d_2}\,(1 - s)
$$

Typical slip for a V-belt is 1 to 2 percent (typical).

Power transmitted, with $T_1$ and $T_2$ in N and $v$ in m/s:

$$
P = (T_1 - T_2)\, v
$$

Open belt length, with center distance $C$ in m, pulley diameters $D$ and $d$ in m:

$$
L = 2C + \frac{\pi (D + d)}{2} + \frac{(D - d)^2}{4C}
$$

Wrap angle on the smaller pulley, in radians:

$$
\theta = \pi - 2 \arcsin\!\left(\frac{D - d}{2C}\right)
$$

Euler's relation for a flat belt on the wrap, with friction coefficient $\mu$ (dimensionless) and wrap angle $\theta$ in radians:

$$
\frac{T_1}{T_2} = e^{\mu \theta}
$$

A V-belt groove with half-angle $\beta/2$ raises the effective friction coefficient by the wedge factor:

$$
\mu_{eff} = \frac{\mu}{\sin(\beta/2)}
$$

Chain pitch diameter for a sprocket with $N$ teeth and pitch $p$ in mm:

$$
d_p = \frac{p}{\sin(180^\circ / N)}
$$

Chain speed, with $p$ in m and $n$ in rpm:

$$
v = \frac{N\, p\, n}{60}
$$

Speed fluctuation within one revolution (the polygon effect), as a fraction of the mean speed:

$$
\frac{\Delta v}{v} = 1 - \cos\!\left(\frac{180^\circ}{N}\right)
$$

Chain length in pitches, with center distance $C_p$ in pitches, sprocket teeth $N_1$ and $N_2$:

$$
L_p = 2 C_p + \frac{N_1 + N_2}{2} + \frac{\left(\frac{N_2 - N_1}{2\pi}\right)^2}{C_p}
$$

Round $L_p$ up to a whole number, then to an even number, because a chain must close on an inner link.

## Worked example

**Given.** A V-belt drive has a driver pulley of $d_1 = 150$ mm running at $n_1 = 1450$ rpm and a driven pulley of $d_2 = 300$ mm. The slip is $s = 0.02$, the center distance is $C = 500$ mm, and the drive transmits $P = 5.0$ kW.

**Find.** The driven speed, the belt speed, the belt length, the wrap angle on the small pulley, and the tension difference.

**Assumptions.** The slip is 2 percent. The belt runs in the straight line between the pulleys. The tension difference is set by the power and the belt speed.

**Solution.**

Step 1. Driven speed: $n_2 = 1450 \times (150 / 300) \times 0.98 = 710.5$ rpm.

Step 2. Belt speed: $v = \pi \times 0.150 \times 1450 / 60 = 11.39$ m/s.

Step 3. Belt length: $L = 2(0.500) + \pi(0.300 + 0.150)/2 + (0.150)^2/(4 \times 0.500) = 1.718$ m.

Step 4. Wrap on the small pulley: $\theta = \pi - 2\arcsin(0.150 / 1.000) = 2.841$ rad, which is $162.8$ degrees.

Step 5. Tension difference: $T_1 - T_2 = P / v = 5000 / 11.39 = 439$ N.

Step 6. Capstan check for a flat belt with $\mu = 0.30$ on that wrap: $T_1 / T_2 = e^{0.30 \times 2.841} = 2.34$. A V-belt in a 38-degree groove has $\mu_{eff} = 0.30 / \sin 19^\circ = 0.92$, which is 3.07 times the flat-belt friction.

**Answer.** Driven speed 710.5 rpm. Belt speed 11.39 m/s. Belt length 1.718 m. Wrap 162.8 degrees. Tension difference 439 N.

**Sanity check.** The driven speed is about half the driver speed, as $150/300 = 0.5$ predicts, minus the 2 percent slip. The belt speed is well below the typical 30 m/s limit of V-belts (typical), so the belt is not at its speed limit.

For a roller chain with $p = 12.7$ mm, $N_1 = 17$ teeth on the driver, $N_2 = 34$ on the driven sprocket, $n_1 = 600$ rpm, and $C = 500$ mm: the driver pitch diameter is 69.12 mm, the chain speed is 2.159 m/s, the polygon fluctuation is 1.70 percent, and the driven speed is 300 rpm. The chain length is $L_p = 104.43$ pitches, which rounds up to 106 links, or 1346 mm. At 3.0 kW the chain carries 1390 N.

## Design trade-offs

- **Slip against cost.** A flat belt costs little and runs at high speed, but it slips and needs high tension, which loads the bearings. A V-belt grips harder at lower tension but has a speed limit of about 30 m/s (typical).
- **Ratio against exactness.** Belts and chains slip or stretch. A timing belt holds an exact ratio, which a camshaft needs. Its pulleys must be accurate, and its cost is higher.
- **Speed against noise.** A chain at high speed is loud and its polygon effect adds vibration. A sprocket with more teeth lowers the fluctuation: about 1.7 percent at 17 teeth, and about 0.4 percent at 34 teeth.
- **Efficiency.** Belts and chains typically pass 95 to 98 percent of the input power (typical). A worm or heavy gearbox loses more.
- **Life against tension.** Too little tension makes a belt slip and wear. Too much tension shortens the belt life and loads the shaft bearings. Set the tension to the manufacturer's value and check it after a run-in period.
- **Heat and dirt.** Chains tolerate heat, dust, and oil better than belts. Belts need a clean, dry drive and a fixed temperature range.

## How it fails

- **Belt slip.** Slip shows as glazing on the belt face, a shrill squeal at start-up, and a driven speed that drops under load. The cause is low tension or a worn, oily pulley.
- **Belt stretch and creep.** The belt lengthens over time, and the tension falls. The warning sign is a belt that slips under the same load it used to carry.
- **Cord fatigue.** A belt bends each time it wraps a small pulley. Repeated bending cracks the cord and the rubber. Keep the smallest pulley above the minimum diameter for the belt.
- **Chain elongation.** The pins and bushings wear, and the chain pitch grows. A worn chain rides high on the sprocket, skips teeth, and jumps under load.
- **Sprocket tooth wear.** A worn chain wears the teeth into a hooked shape. The warning sign is a chain that jumps on the sprocket.
- **Timing belt tooth failure.** Low tension lets the belt jump teeth, and a misaligned pulley shears the teeth.

Safety measures include belt and chain guards, tensioners, and a rated power check for each drive. A chain guard keeps fingers and loose clothing out of the drive, and a tensioner keeps the slack side from whipping.

## History

Leather flat belts drove factory machinery through overhead line shafts across the 19th century. Hans Renold, working in Manchester, developed the bush roller chain in about 1880, and it became a standard chain for power transmission. Timing belts came later, and their teeth let them replace chains where an exact ratio and quiet running matter.

## Practice

1. A V-belt drive has a driver pulley of 100 mm at 1800 rpm and a driven pulley of 250 mm. The slip is 1.5 percent. Find the driven speed in rpm.
2. A pulley of 0.200 m diameter turns at 1200 rpm. Find the belt speed in m/s.
3. A roller chain sprocket has 15 teeth and a pitch of 12.7 mm. Find its pitch diameter in mm.
4. A chain with 15 teeth on a sprocket of pitch 12.7 mm turns at 300 rpm. Find the chain speed in m/s.
5. A flat belt wraps a pulley through $\pi$ radians with friction coefficient $\mu = 0.25$. Find $T_1 / T_2$.

<details><summary>Answers</summary>

1. $n_2 = 1800 \times (100/250) \times 0.985 = 709.2$ rpm.
2. $v = \pi \times 0.200 \times 1200 / 60 = 12.57$ m/s.
3. $d_p = 12.7 / \sin(12^\circ) = 61.08$ mm.
4. $v = 15 \times 12.7 \times 300 / 60000 = 0.9525$ m/s.
5. $T_1 / T_2 = e^{0.25\pi} = 2.193$.

</details>

## Common mistakes

- Using the nominal pulley diameter for the speed ratio of a V-belt when slip is 1 to 2 percent. The slip lowers the driven speed.
- Using the outside diameter of a sprocket instead of the pitch diameter from $p / \sin(180^\circ/N)$.
- Assuming the chain speed is constant. The polygon effect makes the speed rise and fall within each tooth.
- Using a flat-belt friction value for a V-belt. The wedge raises the effective friction, so a V-belt grips harder at the same tension.
- Writing a chain length that is odd. A roller chain must close on an inner link, so the link count is even.

## Go deeper

- [University Physics Volume 1, Chapter 10 (rotational motion)](https://openstax.org/books/university-physics-volume-1/pages/10-introduction) by OpenStax: torque, rotational speed, and the power carried by a rotating shaft, the physics behind every pulley and sprocket.
- [Gear trains](01-gear-trains.md): the positive-engagement alternative to friction and chain drives, with exact ratios and higher efficiency.
- [Planetary gears](02-planetary-gears.md): compact speed and torque changes that use meshing teeth in place of belts.
- [Shafts and bearings](../../design/08-shafts-and-bearings.md): how belt and chain loads reach the shaft and its bearings.
- [Applications reference](../reference.md): the lookup sheet for this topic.
