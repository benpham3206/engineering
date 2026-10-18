# Axial and torsion

Stress and strain describe what happens inside a material when you pull, push, or twist it. Engineers use them to check that a rod, cable, or shaft is strong enough and stiff enough before anything gets built.

**Prerequisites:** [Statics](01-statics.md) (free-body diagrams and equilibrium)
**Time:** 6-8 h

## Core ideas

- **Stress** is force divided by the area it acts on, measured on a cut through the material. Its SI unit is the pascal (Pa), where 1 Pa = 1 N/m². Engineers usually write megapascals (MPa), where 1 MPa = 10^6 Pa. In US customary units, stress is in pounds per square inch (psi) or kips per square inch (ksi).
- **Normal stress** ($\sigma$) acts perpendicular to the cut. Axial loading creates normal stress. Tension is positive and compression is negative.
- **Shear stress** ($\tau$) acts parallel to the cut. Torsion creates shear stress.
- **Strain** is a change in length divided by the original length. It has no units. Normal strain is $\varepsilon = \delta / L$, where $\delta$ is the change in length and $L$ is the original length.
- **Hooke's law** says that inside the elastic range, stress is proportional to strain. For normal stress, $\sigma = E\varepsilon$. The constant $E$ is Young's modulus.
- **Typical values** (approximate, textbook level): structural steel has $E$ about 200 GPa (about 29,000 ksi). Aluminum has $E$ about 70 GPa (about 10,000 ksi). Mild steel yields near 250 MPa (about 36 ksi).
- **Elastic** means the material returns to its original length when the load is removed. Above the yield strength, some deformation stays behind forever. This is called plastic deformation.
- **Torsion** is twisting about the long axis of a shaft. In a solid circular shaft, shear stress is zero at the center and largest at the outer surface.
- **Shear modulus** ($G$) links shear stress to shear strain. Typical steel has $G$ about 80 GPa.
- **Shear strain** ($\gamma$) is the angle a square element distorts, in radians. For a shaft, it grows with distance from the axis and with the angle of twist.
- **Poisson's ratio** ($\nu$) is the ratio of lateral strain to axial strain. Most metals have $\nu$ near 0.3. A bar that stretches also gets thinner.
- **Factor of safety** is the strength of a material divided by the stress it actually sees in use. A factor of 1.4 means the working stress is about 70 percent of the strength.

Reading a stress-strain curve:

- Plot stress on the vertical axis and strain on the horizontal axis, starting from an unloaded bar.
- The first straight part is the elastic region. Its slope is Young's modulus.
- The yield point marks the start of plastic flow. Many metals show a clear yield point. Others, such as aluminum alloys, bend gradually, so engineers use a 0.2 percent offset yield strength.
- Past yield, the curve keeps rising to the ultimate tensile strength, then falls as the bar necks and breaks.
- Ductile materials, like mild steel, show large strain before fracture. Brittle materials, like cast iron, break with little warning.
- The area under the curve up to fracture is related to toughness, which matters for impact and overload.
- Use the elastic slope only for the linear part. Designing with values past yield is a common error.

Assumptions behind the simple formulas:

- The bar is straight and has a constant cross section (prismatic).
- The load acts through the centroid of the section, so the stress is spread evenly across it.
- Deformations are small, and the material stays elastic.
- The part is far from holes, notches, and changes in diameter. Those features concentrate stress.

## Key equations

Symbols and units:

- $\sigma$: normal stress (Pa, or psi)
- $\tau$: shear stress (Pa, or psi)
- $P$: axial force (N, or lbf)
- $A$: cross-sectional area (m², or in²)
- $\delta$: change in length (m, or in)
- $L$: original length (m, or in)
- $\varepsilon$: normal strain (dimensionless)
- $E$: Young's modulus (Pa, or psi)
- $T$: applied torque (N·m, or lbf·ft)
- $r$: distance from the shaft axis (m, or in)
- $J$: polar second moment of area (m⁴, or in⁴)
- $\theta$: angle of twist (rad)
- $G$: shear modulus (Pa, or psi)
- $d$, $D$: solid or outer diameter, and inner diameter for a hollow shaft (m)

Axial loading:

$$\sigma = \frac{P}{A}$$

$$\varepsilon = \frac{\delta}{L}, \qquad \sigma = E\varepsilon$$

Combining the last two gives the elongation of a bar:

$$\delta = \frac{PL}{AE}$$

Torsion of a circular shaft:

$$\tau = \frac{T\,r}{J}, \qquad \tau_{\max} = \frac{T\,(d/2)}{J}$$

For a solid shaft of diameter $d$:

$$J = \frac{\pi d^4}{32}$$

For a hollow shaft with outer diameter $D$ and inner diameter $d$:

$$J = \frac{\pi\,(D^4 - d^4)}{32}$$

Angle of twist for a uniform shaft:

$$\theta = \frac{T L}{G J}$$

Shear modulus for an isotropic material:

$$G = \frac{E}{2(1+\nu)}$$

## Worked example

### Worked example 1: rod in tension

**Problem.** A steel rod has diameter 12 mm and length 2.0 m. It carries an axial tension of 20 kN. Take $E = 200$ GPa.

**Find.** The normal stress, the strain, and the elongation of the rod.

**Assumptions.** The rod is straight and uniform. The load acts through the centroid. The stress stays elastic and is uniform across the section, away from the ends.

**Solution.**

1. Cross-sectional area:
   $$A = \frac{\pi d^2}{4} = \frac{\pi (0.012\ \text{m})^2}{4} = 1.131 \times 10^{-4}\ \text{m}^2 \;(113.1\ \text{mm}^2)$$
2. Normal stress:
   $$\sigma = \frac{P}{A} = \frac{20\,000\ \text{N}}{1.131 \times 10^{-4}\ \text{m}^2} = 1.768 \times 10^{8}\ \text{Pa} = 177\ \text{MPa}$$
3. Strain:
   $$\varepsilon = \frac{\sigma}{E} = \frac{1.768 \times 10^{8}\ \text{Pa}}{2.00 \times 10^{11}\ \text{Pa}} = 8.84 \times 10^{-4}$$
4. Elongation:
   $$\delta = \varepsilon L = 8.84 \times 10^{-4} \times 2.0\ \text{m} = 1.77 \times 10^{-3}\ \text{m} = 1.77\ \text{mm}$$

**Answer.** $\sigma \approx 177$ MPa in tension, $\varepsilon \approx 8.84 \times 10^{-4}$, and $\delta \approx 1.77$ mm.

**Sanity check.**

- The stress of 177 MPa is below the typical mild steel yield of about 250 MPa, so the elastic formula is valid.
- The factor of safety against yielding is $250 / 177 = 1.41$. That is a reasonable margin for a static load.
- The elongation is $1.77 / 2000 = 0.09$ percent of the length, which is small. The small-deformation assumption holds.

### Worked example 2: hollow shaft in torsion

**Problem.** A hollow steel drive shaft has outer diameter 50 mm, inner diameter 40 mm, and length 1.5 m. It transmits a torque of 1.2 kN m. Take $G = 80$ GPa.

**Find.** The maximum shear stress and the angle of twist.

**Assumptions.** Circular cross section, linear elastic material, torque applied only at the ends, no stress concentrations from keyways.

**FBD description.** Cut the shaft anywhere along its length. The internal torque on the cut face is 1.2 kN m, equal and opposite to the torque at the free end.

**Solution.**

Polar moment of inertia of a hollow circle:

$$J = \frac{\pi}{32}\left(D_o^4 - D_i^4\right) = \frac{\pi}{32}\left(0.050^4 - 0.040^4\right) = 3.62 \times 10^{-7}\ \text{m}^4$$

Maximum shear stress, at the outer surface ($c = D_o/2 = 0.025$ m):

$$\tau_{max} = \frac{T c}{J} = \frac{1200 \times 0.025}{3.62 \times 10^{-7}} = 82.8\ \text{MPa}$$

Angle of twist:

$$\phi = \frac{T L}{G J} = \frac{1200 \times 1.5}{80 \times 10^9 \times 3.62 \times 10^{-7}} = 0.0621\ \text{rad} = 3.56^\circ$$

**Answer.** $\tau_{max} \approx 82.8$ MPa and $\phi \approx 3.56^\circ$.

**Sanity check.**

- A solid 50 mm shaft would see 48.9 MPa. The hollow shaft is more highly stressed, as expected, but it uses only 36 percent of the material and keeps 59 percent of the torsional stiffness. That is why drive shafts are hollow.
- Shear yield of mild steel is roughly half its tensile yield, about 125 MPa, so 82.8 MPa is elastic with a factor of safety near 1.5.

## Practice

1. A solid steel rod, 20 mm in diameter, carries 10 kN in tension. Find the normal stress in MPa.
2. The same rod is 1.5 m long, with $E = 200$ GPa, and carries 10 kN. Find the elongation in mm.
3. An aluminum rod, 15 mm in diameter, carries 20 kN. Find the normal stress in MPa. Then, with $E = 70$ GPa, find the strain.
4. A solid steel shaft has diameter 50 mm and length 1.0 m. It carries a torque of 800 N·m, with $G = 80$ GPa. Find the maximum shear stress in MPa and the angle of twist in radians.

<details><summary>Answers</summary>

1. 31.8 MPa
2. 0.239 mm
3. 113 MPa; strain 1.62 × 10^-3
4. 32.6 MPa; 0.0163 rad

</details>

## Common mistakes

- Using the radius where the formula needs the diameter, or the reverse. The area uses $d^2$ with $d$ as the diameter. For torsion, $r = d/2$ at the outer surface.
- Mixing millimeters and meters. Convert every length to meters before using SI formulas, then convert the answer to MPa or mm for reporting.
- Using axial formulas for torsion. Torsion uses $J$ and $G$, not $A$ and $E$.
- Forgetting stress concentrations. A hole or sharp groove can raise the peak stress well above $P/A$.
- Applying the elastic formula after the part has yielded. Check the stress against the yield strength first.
- Confusing load with stress. Two rods can carry the same load, but the thinner one has the higher stress.

Units tip: work in SI inside the formulas, then convert at the end. A quick check is to see whether $P/A$ gives newtons per square meter. If it does, the answer is in pascals and dividing by $10^6$ gives MPa.

## Go deeper

- [Mechanics of Materials (Roylance)](https://eng.libretexts.org/Bookshelves/Mechanical_Engineering/Mechanics_of_Materials_%28Roylance%29) by David Roylance, MIT OpenCourseWare, via Engineering LibreTexts: a free, openly licensed textbook. Start with the tensile response and stress and strain chapters.
- [Chapter 8: Beam Bending, Buckling, and Torsion](https://eng.libretexts.org/Courses/California_State_Polytechnic_University_Humboldt/Mechanical_Behavior_of_Material/Chapter_8:_Beam_Bending,_Buckling,_and_Torsion) by Cal Poly Humboldt, via Engineering LibreTexts: a free treatment of the torsion angle of twist, with the same notation used in this lesson.
- Next lesson: [Bending and buckling](05-bending-and-buckling.md), which applies the same ideas to beams and columns.
