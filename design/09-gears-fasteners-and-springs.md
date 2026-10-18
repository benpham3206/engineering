# Gears, fasteners, and springs

**Type:** lesson

Gears change speed and torque between shafts. Fasteners clamp parts together, and their job is to hold a preload that does not loosen. Springs store energy and give a force that changes with length. These three machine elements appear in almost every machine, and each has a few formulas that a designer uses over and over. This lesson covers the basic sizing of each.

**Prerequisites:** [07 Factor of safety and failure](07-factor-of-safety-and-failure.md), [08 Shafts and bearings](08-shafts-and-bearings.md)
**Time:** 8-12 h

## Core ideas

**Gears**

- A **gear tooth** is a lever that transfers force from one shaft to another. Gears in mesh must share the same **module** $m$, which is the pitch diameter in mm divided by the number of teeth.
- The **pitch diameter** $d$ is the diameter of the imaginary circle where two teeth roll together.
- The **gear ratio** $i$ is the number of teeth on the driven gear divided by the number on the driver. A ratio of 2 halves the speed and doubles the torque, ignoring losses.
- The **center distance** is the distance between two shaft centers. For gears in mesh, it is the average of the two pitch diameters.
- **Pitch-line velocity** is the speed of a point on the pitch circle. It sets the noise, lubrication, and dynamic load.

**Fasteners**

- A **bolt** is a threaded fastener that stretches when tightened. The stretch creates the **preload**, a tension that clamps the parts together.
- **Preload** is the main job of a bolt. A bolt that is clamped firmly does not slip under shear load, and it resists fatigue better.
- The **tensile stress area** $A_t$ is the effective area of a threaded bolt, between the root and pitch diameters. It is looked up in tables for standard threads.
- The **proof strength** $S_p$ is the stress a bolt can carry without permanent stretch. For grade 8.8 steel bolts, the standard proof strength is 600 MPa (about 87 ksi).
- A typical design preload is 75 percent of the proof load, which leaves margin for relaxation.
- Torque is the usual way to set preload in the shop. The **torque-tension relation** links the two, and the nut factor $K$ depends on friction. A typical value for dry steel is about 0.2.

**Springs**

- A **helical compression spring** is a coil of wire that pushes back when compressed. Its **spring rate** $k$ is the force per unit deflection.
- The spring rate depends on the wire diameter, the coil diameter, the number of active coils, and the shear modulus of the material.
- Springs that are compressed to solid, or stretched past their elastic limit, do not return to their free length. Check the design with a maximum deflection.

## Key equations

**Gears**

Pitch diameter, with $m$ the module (mm) and $N$ the number of teeth:

$$
d = mN
$$

Center distance for two meshing gears with teeth $N_1$ and $N_2$:

$$
C = \frac{m(N_1 + N_2)}{2}
$$

Gear ratio, speed ratio, and ideal torque ratio:

$$
i = \frac{N_2}{N_1} = \frac{n_1}{n_2} = \frac{T_2}{T_1}
$$

Pitch-line velocity with $d$ in mm and $n$ in rpm, giving $v$ in m/s:

$$
v = \frac{\pi d n}{60\,000}
$$

**Fasteners**

Preload from proof strength $S_p$ (MPa) and tensile stress area $A_t$ (mm$^2$), giving $F_i$ in N:

$$
F_i = 0.75\,S_p\,A_t
$$

Tightening torque from the nut factor $K$, preload $F_i$ (N), and nominal diameter $d$ (mm), giving $T$ in N$\cdot$mm:

$$
T = K\,F_i\,d
$$

Divide by 1000 to get N$\cdot$m.

**Springs**

Spring rate for a helical compression spring of wire diameter $d$, mean coil diameter $D$, active coils $N_a$, and shear modulus $G$:

$$
k = \frac{G\,d^4}{8\,D^3\,N_a}
$$

Force and deflection:

$$
F = k\,x
$$

Units: $G$ in MPa (or N/mm$^2$). $d$, $D$ in mm. $k$ in N/mm. $x$ in mm.

Typical shear modulus for steel: $G = 79$ GPa (about 11.5 Msi). This is a typical value.

## Worked example: bolt preload

An M10 coarse-thread steel bolt of grade 8.8 is tightened into a steel plate. Its proof strength is $S_p = 600$ MPa (typical for grade 8.8), its tensile stress area is $A_t = 58.0$ mm$^2$ (standard for M10 by 1.5), and the nut factor is $K = 0.20$ for dry steel. Find the preload and the tightening torque.

**Given.** $S_p = 600$ MPa, $A_t = 58.0$ mm$^2$, $K = 0.20$, $d = 10$ mm.

**Find.** Preload $F_i$ and torque $T$.

**Assumptions.** Preload is 75 percent of the proof load. The friction is the dry steel value. The clamped parts are rigid enough that the preload stays put.

**Solution.**

Step 1. Proof load: $S_p A_t = 600 \times 58.0 = 34\,800$ N.

Step 2. Preload: $F_i = 0.75 \times 34\,800 = 26\,100$ N $\approx 26.1$ kN (about 5.9 kip).

Step 3. Torque: $T = K F_i d = 0.20 \times 26\,100 \times 10 = 52\,200$ N$\cdot$mm $= 52.2$ N$\cdot$m (about 38.5 lbf$\cdot$ft).

**Answer.** Preload 26.1 kN. Tighten to about 52 N$\cdot$m with a calibrated wrench.

**Sanity check.** A 26 kN clamp load is large for an M10 bolt, but it matches the idea that most of the bolt's proof load is used for clamping. A torque of 52 N$\cdot$m is a reasonable wrench value for an M10 bolt. The torque is very sensitive to friction: if the nut factor were 0.15 with lubrication, the same torque would give a larger preload, which is why the nut factor must be stated.

## Worked example: gear pair

Two spur gears have module $m = 2$ mm, with $N_1 = 20$ teeth on the driver and $N_2 = 40$ on the driven gear. The driver runs at 1200 rpm.

- Pitch diameters: $d_1 = 2 \times 20 = 40$ mm, $d_2 = 2 \times 40 = 80$ mm.
- Center distance: $C = \dfrac{2 (20 + 40)}{2} = 60$ mm.
- Gear ratio: $i = \dfrac{40}{20} = 2.0$, so the driven gear runs at $600$ rpm and carries twice the torque, ignoring losses.
- Pitch-line velocity: $v = \dfrac{\pi \times 40 \times 1200}{60\,000} = 2.51$ m/s.

**Sanity check.** The center distance equals the average of the pitch diameters, $(40 + 80)/2 = 60$ mm, which confirms the formula.

## Worked example: spring rate

A helical spring has wire diameter $d = 2$ mm, mean coil diameter $D = 16$ mm, and $N_a = 10$ active coils. With $G = 79\,000$ MPa, the spring rate is

$$
k = \frac{79\,000 \times 2^4}{8 \times 16^3 \times 10} = 3.86\ \text{N/mm}.
$$

Under a 20 N load the deflection is $x = 20 / 3.86 = 5.18$ mm.

## Checklist

- Do meshing gears share the same module?
- Is the preload 75 percent of the proof load, and is the stress area the tensile stress area?
- Is the torque in N$\cdot$mm before converting to N$\cdot$m?
- Is the spring rate calculated with the coil diameter $D$ and not the wire diameter?
- Is the deflection checked against solid height and the elastic limit?

## Practice

1. Two gears have module 3 mm, $N_1 = 24$ teeth, and $N_2 = 36$ teeth. Find the center distance in mm.
2. For the gears in question 1, find the gear ratio $N_2 / N_1$. Give the number to one decimal place.
3. An M8 bolt has $S_p = 600$ MPa and $A_t = 36.6$ mm$^2$. Find the preload in kN to one decimal place.
4. A spring has $d = 3$ mm, $D = 24$ mm, $N_a = 8$, and $G = 79\,000$ MPa. Find $k$ in N/mm to two decimals.

<details><summary>Answers</summary>

1. 90
2. 1.5
3. 16.5
4. 7.23

</details>

## Common mistakes

- Mixing up the module and the diameter. The pitch diameter is $m$ times $N$, not $N$ alone.
- Using the nominal bolt area instead of the tensile stress area, which overstates the preload.
- Forgetting the unit conversion in the torque formula: N$\cdot$mm to N$\cdot$m is a factor of 1000.
- Using the wire diameter where the mean coil diameter belongs in the spring rate, which changes $k$ by a large factor.
- Assuming a spring returns to its free length after going past its elastic limit.

## Go deeper

- [Engineering LibreTexts](https://eng.libretexts.org/) by the LibreTexts project: free engineering textbooks, including machine design and mechanics topics.
- [Paul's Online Math Notes](https://tutorial.math.lamar.edu/) by Paul Dawkins: free algebra and exponent review for the cube and fourth-power terms in the spring and shaft formulas.
- Gear and fastener standards (for example the ISO and ASME tables) are the real reference for tooth profiles and thread sizes. Many are paid, so check the library or your employer first.
