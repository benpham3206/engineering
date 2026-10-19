# Shafts and bearings

**Type:** lesson

A **shaft** is a rotating rod that carries torque from a motor or handle to the parts that do work, such as gears, pulleys, or wheels, and a bearing is a support that holds the shaft in place while letting it turn. Engineers size both carefully because an undersized shaft can twist, bend, or break, and a poor bearing wears out long before the rest of the machine. Shaft sizing is a classic design problem: pick a diameter so the shear stress from the torque stays below a safe limit. Bearing selection asks how long the bearing will last under load.
**Prerequisites:** [Factor of safety and failure](07-factor-of-safety-and-failure.md), [GD&T symbols and frames](05-gdt-symbols-and-frames.md) (for runout on shaft seats), [Axial and torsion](../physics/04-axial-and-torsion.md), [Bending and buckling](../physics/05-bending-and-buckling.md), [Rigid body dynamics](../physics/03-rigid-body-dynamics.md) (torque and rotation)
**Time:** 8-12 h

## Core ideas

- **Torque** $T$ is the twisting effort on the shaft. It is force times the distance from the axis, in $\text{N}\cdot\text{m}$ (or $\text{lbf}\cdot\text{in}$).
- **Power and speed.** A motor delivers power $P$ at speed $n$. The torque is $T = P / \omega$, where $\omega$ is the angular speed in rad/s.
- **Torsional shear stress** $\tau$ is the stress a torque creates across a shaft's cross section. It is highest at the outer surface.
- **Shaft sizing** chooses a diameter so that the shear stress stays below an allowable value found from the material and the factor of safety.
- **Stress concentration.** Keyways, shoulders, and small fillets raise the local stress. This lesson ignores them, so real shafts need extra margin or a formal stress concentration factor.
- **Bearings** carry radial load (perpendicular to the shaft) and sometimes thrust load (along the shaft). Ball and roller bearings are the common types.
- **Bearing life** is the number of revolutions (or hours) a bearing runs before a set fraction fails, usually 10 percent. It is called the $L_{10}$ life.
- **Runout and fits.** The shaft seat for a bearing needs low runout. Select fits by which ring sees rotating load (that ring gets the interference fit), load magnitude, temperature, internal clearance, and which ring must float axially. This ties to [04 Tolerancing and stack-up](04-tolerancing-and-stack-up.md) and [05 GD&T symbols and frames](05-gdt-symbols-and-frames.md).

## Key equations

Shear stress in a solid round shaft of diameter $d$ under torque $T$:

$$
\tau = \frac{16\,T}{\pi d^3}
$$

Allowable shear stress from the yield strength $S_y$ and the factor of safety $n$, using the Tresca criterion (shear yield taken as half the tensile yield):

$$
\tau_{\text{allow}} = \frac{0.5\,S_y}{n}
$$

Minimum diameter for a given torque:

$$
d_{\min} = \left(\frac{16\,T}{\pi\,\tau_{\text{allow}}}\right)^{1/3}
$$

Factor of safety for a chosen diameter:

$$
n = \frac{0.5\,S_y}{\tau}
$$

Basic $L_{10}$ life of a ball bearing with dynamic load rating $C$ and equivalent load $P$, in millions of revolutions:

$$
L_{10} = \left(\frac{C}{P}\right)^3
$$

Life in hours at speed $n_{\text{rpm}}$:

$$
L_{h} = \frac{10^6\,L_{10}}{60\,n_{\text{rpm}}}
$$

For roller bearings, replace the exponent 3 with $10/3$.

Units: $T$ in $\text{N}\cdot\text{mm}$ (multiply $\text{N}\cdot\text{m}$ by 1000) so that $d$ comes out in mm. $\tau$ and $S_y$ in MPa. $C$ and $P$ in N (or kN, as long as both match). Speed in rpm.

## Worked example

A solid steel shaft must carry a torque of 200 $\text{N}\cdot\text{m}$ (about 1770 $\text{lbf}\cdot\text{in}$). The steel has yield strength $S_y = 350$ MPa (typical value). Use a factor of safety of 2.5. Find the minimum diameter, choose a standard size, and check the factor of safety.

**Given.** $T = 200$ $\text{N}\cdot\text{m}$ $= 200\,000$ $\text{N}\cdot\text{mm}$, $S_y = 350$ MPa, $n = 2.5$.

**Find.** $d_{\min}$, a standard diameter, and the actual $n$.

**Assumptions.** Constant steady torque. No keyway or shoulder. Solid round shaft. Tresca criterion for shear yield.

**Solution.**

Step 1. Allowable shear: $\tau_{\text{allow}} = \dfrac{0.5 \times 350}{2.5} = 70$ MPa.

Step 2. Minimum diameter: $d_{\min} = \left(\dfrac{16 \times 200\,000}{\pi \times 70}\right)^{1/3} = (14\,547)^{1/3} = 24.41$ mm.

Step 3. Choose the next standard size: 25 mm (about 0.98 in).

Step 4. Actual shear at 25 mm: $\tau = \dfrac{16 \times 200\,000}{\pi \times 25^3} = 65.2$ MPa.

Step 5. Actual factor of safety: $n = \dfrac{0.5 \times 350}{65.2} = 2.68$.

**Answer.** Minimum diameter 24.41 mm. Use a 25 mm shaft. The actual factor of safety is 2.68, above the target of 2.5.

**Sanity check.** A 25 mm shaft is about 0.98 in, and the 200 $\text{N}\cdot\text{m}$ torque is a fixed input from the example. The shear of 65 MPa is well below the 175 MPa shear yield (half of 350 MPa). The keyway and shoulder were ignored, so a real design would either choose a larger diameter or run a stress concentration check.

## Worked example: bearing life

A ball bearing has a dynamic load rating $C = 20$ kN. Its equivalent load is $P = 5$ kN, and it runs at 1500 rpm. Find the $L_{10}$ life in millions of revolutions and in hours.

**Solution.**

$L_{10} = \left(\dfrac{20}{5}\right)^3 = 4^3 = 64$ million revolutions.

$L_h = \dfrac{10^6 \times 64}{60 \times 1500} = \dfrac{64 \times 10^6}{90\,000} = 711$ h.

**Answer.** $L_{10}$ life is 64 million revolutions, about 711 hours at 1500 rpm.

**Sanity check.** If the load doubles, the life falls by a factor of $2^3 = 8$. That is why load estimates matter so much in bearing selection.

## Checklist

- Is the torque in $\text{N}\cdot\text{mm}$ before using the sizing formula?
- Is the allowable shear found from $0.5\,S_y$ divided by $n$?
- Is the chosen diameter a standard size at or above $d_{\min}$?
- Are keyways, shoulders, and fillets checked, or at least noted as ignored?
- Is the bearing life exponent 3 for balls and $10/3$ for rollers?
- Are the bearing load and rating in the same units?

## Practice

1. A solid shaft carries 150 $\text{N}\cdot\text{m}$ with allowable shear 60 MPa. Find the minimum diameter in mm to two decimals.
2. A ball bearing has $C = 12$ kN and $P = 4$ kN. It runs at 1200 rpm. Find the $L_{10}$ life in hours.
3. A solid shaft of diameter 30 mm carries 150 $\text{N}\cdot\text{m}$. Find the torsional shear stress in MPa to two decimals.
4. A roller bearing has $C/P = 3$ and runs at 600 rpm. Find L10 in million revolutions, to two decimals.

<details><summary>Answers</summary>

1. 23.35
2. 375
3. 28.29
4. 38.94

</details>

## Common mistakes

- Plugging torque in $\text{N}\cdot\text{m}$ into a formula that needs $\text{N}\cdot\text{mm}$. The result is about ten times too small, because the factor of 1000 becomes a factor of 10 after the cube root.
- Using $S_y$ directly as the shear limit instead of half of it.
- Forgetting the cube in the diameter formula, so the answer is much too small or large.
- Ignoring the keyway or shoulder, which can be the real point of failure.
- Using the bearing exponent 3 for a roller bearing, which changes the life estimate. The roller exponent is $10/3$. For $C/P > 1$, using 3 predicts a life that is too low (at $C/P = 3$: 27 versus 38.9).

## Go deeper

- [*OpenStax University Physics Volume 1*](https://openstax.org/books/university-physics-volume-1/pages/1-introduction) by OpenStax at Rice University: free physics text covering rotation, torque, and angular motion.
- [Engineering LibreTexts](https://eng.libretexts.org/) by the LibreTexts project: free engineering textbooks, including mechanics of materials and machine design topics.
- [Paul's Online Math Notes](https://tutorial.math.lamar.edu/) by Paul Dawkins: free algebra review for exponents, roots, and unit conversions used in the sizing and life formulas.
- [Design reference](reference.md): the lookup sheet for this topic.
