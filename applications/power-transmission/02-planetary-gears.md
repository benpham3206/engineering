# Planetary gears

**Type:** lesson

A planetary gear train puts a sun gear, planet gears, and a ring gear in one compact set, so three members can turn at once. It gives high ratios in a small space and forms the core of automatic transmissions, hub gears, and gearmotors. The Willis equation ties the speeds of the three members together, and an engineer uses it to pick the input, output, and fixed member.

**Prerequisites:** [Gear trains](01-gear-trains.md), [Gears, fasteners, and springs](../../design/09-gears-fasteners-and-springs.md), [Rigid body dynamics](../../physics/03-rigid-body-dynamics.md)
**Time:** 4-6 h

## Core ideas

### How it works

The sun gear sits at the center. Several planet gears mesh with the sun and turn around it. A carrier arm holds the planets at fixed spacing and turns with them. A ring gear has its teeth on the inside and meshes with the outside of the planets. The planets therefore link all three members.

The planet teeth mesh with the sun on the inside and the ring on the outside. The ring pitch radius equals the sun pitch radius plus two planet pitch radii. With the same module, the tooth counts follow the same rule: $N_r = N_s + 2 N_p$. A sun of 24 teeth and planets of 12 teeth give a ring of 48 teeth.

Any member can be fixed. Two of the three members are then input and output, and the third is the reference that does not move. Changing which member is fixed gives a different ratio, and the Willis equation gives the speed of each case.

### Main parts

- **Sun gear.** The central external gear. In most reduction units it is the input.
- **Planet gears.** Usually three to five gears on the carrier. They share the load, so more planets carry more torque for the same tooth size.
- **Carrier.** The arm that holds the planets on pins, often through needle or ball bearings. The carrier often delivers the output.
- **Ring gear.** The internal gear that the planets mesh with on the outside. It is often fixed to the housing.

### Variants

- **Ring fixed, sun input, carrier output.** This is the common reduction layout. The ratio is $1 + N_r / N_s$, and the output turns in the same direction as the input.
- **Carrier fixed, sun input, ring output.** The ring turns opposite to the sun. This gives a simple reverse ratio.
- **Sun fixed, ring input, carrier output.** The carrier turns in the same direction as the ring, with a ratio of $1 + N_s / N_r$ when the ring is the input.
- **Compound planetary.** Two or more planetary sets in series give very high total ratios. An automatic transmission uses several sets with clutches and brakes to fix each member in turn.

## Key equations

The Willis equation gives the carrier speed $\omega_c$ for sun speed $\omega_s$ and ring speed $\omega_r$, each in rad/s, with tooth counts $N_s$ and $N_r$:

$$
\omega_c = \frac{N_s \,\omega_s + N_r \,\omega_r}{N_s + N_r}
$$

An equivalent form is the relative speed relation, which shows the sign of the ring:

$$
\frac{\omega_s - \omega_c}{\omega_r - \omega_c} = -\frac{N_r}{N_s}
$$

Robert Willis described this relation for epicyclic trains in his book *Principles of Mechanism*, published in 1841.

Ring tooth count, with $N_p$ the teeth on each planet:

$$
N_r = N_s + 2 N_p
$$

Ring fixed, sun input, carrier output, with $\omega_r = 0$ and the ratio of sun speed to carrier speed:

$$
\frac{\omega_s}{\omega_c} = 1 + \frac{N_r}{N_s}
$$

Output torque, with $\eta$ dimensionless and $T$ in N$\cdot$m, for the ring-fixed layout:

$$
T_c = \eta\, \frac{\omega_s}{\omega_c}\, T_s
$$

Power is $P = T\omega$ with $P$ in W, so $P_{out} = \eta P_{in}$ for the same two-member power flow.

Three fixed-member cases, with $N_s = 24$, $N_p = 12$, $N_r = 48$, and sun input $\omega_s = 1$ (or ring input $\omega_r = 1$ in case C). Each case satisfies the relative speed relation with the ring ratio $-N_r / N_s = -2$.

| Fixed member | Input | Output | Output over input speed | Direction |
|---|---|---|---|---|
| Ring | Sun | Carrier | $\omega_c / \omega_s = 1/3$ | Same as sun |
| Carrier | Sun | Ring | $\omega_r / \omega_s = -1/2$ | Opposite to sun |
| Sun | Ring | Carrier | $\omega_c / \omega_r = 2/3$ | Same as ring |

## Worked example

**Given.** A gearmotor drives a planetary reduction with a ring fixed to the housing. The sun has $N_s = 24$ teeth, each planet has $N_p = 12$ teeth, and the ring has $N_r = 48$ teeth. The motor turns the sun at 1500 rpm and delivers $T_s = 10$ N$\cdot$m. The mesh efficiency is $\eta = 0.97$ for the whole set.

**Find.** The carrier speed, the output torque, and the output power.

**Assumptions.** The ring is fixed. The efficiency $\eta = 0.97$ applies to the whole reduction. The planets share the load evenly.

**Solution.**

Step 1. Check the ring: $N_r = N_s + 2 N_p = 24 + 24 = 48$. The ring is consistent with the planets.

Step 2. Speed ratio: $\omega_s / \omega_c = 1 + N_r / N_s = 1 + 48/24 = 3.0$.

Step 3. Carrier speed: $n_c = 1500 / 3.0 = 500$ rpm, which is $\omega_c = 52.36$ rad/s.

Step 4. Output torque: $T_c = 0.97 \times 3.0 \times 10 = 29.1$ N$\cdot$m.

Step 5. Input power: $\omega_s = 1500 \times 2\pi / 60 = 157.1$ rad/s, so $P_{in} = 10 \times 157.1 = 1571$ W.

Step 6. Output power: $P_{out} = 29.1 \times 52.36 = 1524$ W, which is $0.97 \times 1571$ W.

**Answer.** Carrier speed 500 rpm. Output torque 29.1 N$\cdot$m. Output power about 1524 W.

**Sanity check.** The output speed is one third of the input, and the output torque is about three times the input, less the 3 percent loss. The output power equals $0.97$ times the input power, so the energy balance holds.

## Design trade-offs

- **Ratio against size.** A ring-fixed set gives a ratio of $1 + N_r / N_s$ in one stage. A small sun with a large ring gives a high ratio. Very small suns are hard to cut and have weak roots, so a single planetary stage stays moderate.
- **Load against planet count.** Three planets share the torque, and five planets share it more finely. More planets raise the torque capacity, but each planet needs tighter spacing and more accurate pins.
- **Efficiency.** A planetary stage often loses about 3 percent per stage (typical). The sliding is small, so the efficiency stays high at large ratios compared with a worm drive.
- **Coaxial layout.** The input and output sit on one axis, which saves space in a wheel hub and a gearmotor. The ring and carrier bearings take the radial loads.
- **Cost and tolerance.** Planetary sets need accurate planet spacing and matched tooth profiles. Poor spacing puts most of the load on one planet.

## How it fails

- **Planet bearing fatigue.** The planets run on pins or bearings that see cyclic load on every revolution. The warning sign is noise that grows with speed. Bearings are chosen for life, as in the [shafts and bearings lesson](../../design/08-shafts-and-bearings.md).
- **Tooth fatigue on the sun.** The sun turns fastest and has the fewest teeth, so its root stress and pitch-line velocity are highest. Check the sun first when a set fails early.
- **Uneven load sharing.** If one planet carries more load than the rest, its teeth pit or crack first. The warning sign is a rough, noisy set with one worn planet.
- **Ring gear cracking.** Shock loads on the ring can crack its thin rim, especially in a housing that flexes.
- **Carrier pin wear.** Pins that wear loosen the planets and open the spacing. The gear then runs with extra backlash and noise.

Safety measures include torque limiters on the output, lubrication sized for the planet bearings, and a rated life check on every bearing. A gearmotor with a hub brake keeps a load from back-driving the set when power is off.

## History

The Antikythera mechanism, found in 1901 in a shipwreck off the Greek island of Antikythera, is the earliest known machine that some researchers argue used epicyclic gearing. The Greek astronomers who used epicycles to model planetary motion inspired the name of the gear type. Robert Willis gave the speed relation for epicyclic trains in 1841. The Ford Model T, introduced in 1908, used planetary gears in its transmission, and planetary sets have been standard in automatic transmissions since.

## Practice

1. A sun of 30 teeth and a ring of 90 teeth are used with the ring fixed. The sun is the input at 1200 rpm. Find the carrier speed.
2. The same set has the carrier fixed and the sun input at 1200 rpm. Find the ring speed, and give its sign relative to the sun.
3. The same set has the sun fixed and the ring input at 600 rpm. Find the carrier speed.
4. A ring of 90 teeth meshes with a sun of 30 teeth. How many teeth does each planet have?

<details><summary>Answers</summary>

1. $\omega_c = \omega_s N_s / (N_s + N_r) = 1200 \times 30 / 120 = 300$ rpm.
2. $\omega_r = -\omega_s N_s / N_r = -1200 \times 30 / 90 = -400$ rpm. The ring turns opposite to the sun.
3. $\omega_c = \omega_r N_r / (N_s + N_r) = 600 \times 90 / 120 = 450$ rpm.
4. $N_p = (N_r - N_s) / 2 = (90 - 30) / 2 = 30$ teeth.

</details>

## Common mistakes

- Using $N_s + N_p$ for the ring instead of $N_s + 2N_p$. The ring must be larger than the sun by two planet diameters.
- Forgetting the sign of the ring speed. In the carrier-fixed case, the ring turns opposite to the sun.
- Treating the carrier speed as the planet speed. The planets spin on their own axes while the carrier turns around the sun.
- Assuming the ring-fixed ratio is 1 to 1 because the ring looks stationary. With the ring fixed, the carrier output is $1 + N_r / N_s$ times slower than the sun.
- Assigning the wrong member as fixed. Write down the fixed member first, then apply the Willis equation.

## Go deeper

- [University Physics Volume 1, Chapter 10 (rotational motion)](https://openstax.org/books/university-physics-volume-1/pages/10-introduction) by OpenStax: angular speed, torque, and rotational power, the physics behind each member of an epicyclic set.
- [Gear trains](01-gear-trains.md): the spur, helical, bevel, and worm forms that a planetary set can combine with.
- [Gears, fasteners, and springs](../../design/09-gears-fasteners-and-springs.md): the pitch-diameter and center-distance formulas that set each planet's place between the sun and ring.
- [Belts and chains](03-belts-and-chains.md): another way to transmit speed and torque between shafts, with no tooth meshing.
