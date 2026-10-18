# Bending and buckling

**Type:** lesson

A beam carries loads sideways, such as a floor joist or a shelf. A column carries load along its length, such as a building post or a strut in a truss. Beams fail by bending too far or by overstressing the outer fibers. Columns can fail suddenly by buckling, even when the stress in the material is well below its yield strength.

**Prerequisites:** [Statics](01-statics.md) (reactions and internal forces), [Axial and torsion](04-axial-and-torsion.md) (stress, strain, and Hooke's law)
**Time:** 8-10 h

## Core ideas

- **Beam** is a slender member loaded across its length. Engineers call the axis of the beam the longitudinal axis.
- **Support types.** A simply supported beam rests on a pin at one end and a roller at the other. A cantilever is fixed at one end and free at the other.
- **Internal forces.** At any cut through a beam there is a shear force $V$ and a bending moment $M$. The moment is the internal couple that resists the external loads. Engineers draw shear and moment diagrams to show how these change along the beam.
- **Neutral axis.** When a beam bends, the fibers on one side stretch and the fibers on the other side shorten. The line between them, at the centroid for a symmetric section, has zero bending stress.
- **Second moment of area** ($I$) measures how the cross section resists bending. It depends on the shape and the distribution of area away from the neutral axis. A deep, narrow section has a large $I$ when the depth is in the bending direction.
- **Section modulus** ($S = I/c$) is the second moment of area divided by the distance $c$ to the outermost fiber. It gives the maximum bending stress directly.
- **Deflection** is how far the beam sags under load. Designers check it because a beam can be strong enough and still feel bouncy or crack finishes. A common floor guideline is a deflection limit of $L/360$.
- **Stiffness** is the resistance to deflection, which is $EI$ for a beam. Doubling $E$ or $I$ halves the deflection under the same load.
- **Sign convention.** Engineers often treat sagging (the beam bends into a smile shape) as a positive moment. Check the convention in each textbook before comparing signs.
- **Buckling** is a sudden sideways instability of a slender column under compression. Past a critical load, the column deflects sideways and the load cannot be increased without large deflection.
- **Slenderness ratio** $KL/r$ compares the effective length to the radius of gyration. A large ratio means a long, slender column that will buckle. A small ratio means a short column that is controlled by yielding.
- **End conditions** change the effective length. The effective length factor $K$ is 1.0 for pinned-pinned ends, 0.5 for fixed-fixed ends, and 2.0 for a cantilever column that is fixed at one end and free at the other.
- **Weakest axis buckles first.** A rectangular column buckles about the axis with the smallest $I$.

Common load patterns on beams:

- A point load is a force at one spot, such as a box resting at midspan.
- A uniform load is spread evenly along the length, such as the weight of a floor or a snow load. Its units are force per length.
- A moment load is a couple applied at a point. It causes a jump in the bending moment diagram at that point.
- Superposition lets you add the results of simple load cases. At any point, the deflection from two loads is the sum of the deflections each load causes at that point, as long as the beam stays elastic and the deflections are small.

Shear and moment in a beam:

- The shear force at a section is the sum of the vertical forces on one side of it.
- The bending moment at a section is the sum of moments of those forces about the section.
- Shear is the slope of the moment diagram. Where shear is zero, the moment is at a peak or a valley.
- A bending moment that is largest at midspan is typical for a uniform load on a simply supported beam.
- Shear stress in beams is usually small compared with bending stress for slender sections. It matters more for short, deep beams.

Assumptions behind the formulas in this lesson:

- The material is linear elastic (Hooke's law holds).
- The beam is prismatic and slender, so shear deformation is small.
- The loads act in the plane of symmetry of the section.
- For Euler buckling, the column is straight and perfectly aligned, and the load is centered.

## Key equations

Symbols and units:

- $M$: bending moment (N·m, or lbf·ft)
- $V$: internal shear force (N, or lbf)
- $y$: distance from the neutral axis (m, or in)
- $\sigma$: bending stress (Pa, or psi)
- $I$: second moment of area (m⁴, or in⁴)
- $c$: distance from the neutral axis to the outermost fiber (m, or in)
- $S$: section modulus (m³, or in³)
- $b$, $h$: width and depth of a rectangular section (m, or in)
- $d$: diameter of a solid circular section (m, or in)
- $w$: uniform load per unit length (N/m, or lbf/ft)
- $P$: concentrated load (N, or lbf)
- $L$: span or column length (m, or in)
- $v_{\max}$: maximum deflection (m, or in)
- $E$: Young's modulus (Pa, or psi)
- $P_{cr}$: critical buckling load (N, or lbf)
- $K$: effective length factor (dimensionless)
- $A$: cross-sectional area (m², or in²)
- $r$: radius of gyration (m, or in)

Flexure formula:

$$\sigma = \frac{M y}{I}, \qquad \sigma_{\max} = \frac{M c}{I} = \frac{M}{S}$$

Second moment of area for common shapes:

$$I_{\text{rect}} = \frac{b h^3}{12}, \qquad I_{\text{circle}} = \frac{\pi d^4}{64}$$

Moments for two common loadings on a simply supported span:

$$M_{\max,\,\text{UDL}} = \frac{w L^2}{8}, \qquad M_{\max,\,\text{midspan point}} = \frac{P L}{4}$$

Maximum deflection for the same loadings:

$$v_{\max,\,\text{UDL}} = \frac{5\,w L^4}{384\,E I}, \qquad v_{\max,\,\text{midspan point}} = \frac{P L^3}{48\,E I}$$

Euler's critical load for a column with effective length factor $K$:

$$P_{cr} = \frac{\pi^2 E I}{(K L)^2}$$

Radius of gyration and slenderness:

$$r = \sqrt{\frac{I}{A}}, \qquad \text{slenderness} = \frac{K L}{r}$$

## Worked example

**Problem.** A simply supported steel beam has span $L = 4.0$ m and carries a uniform load of $w = 10$ kN/m (including its own weight). The cross section is a rectangle, 100 mm wide and 200 mm deep. Take $E = 200$ GPa.

**Find.** The maximum bending moment, the maximum bending stress, and the maximum deflection.

**Assumptions.** The beam is prismatic and linear elastic. The load is uniform along the span. The supports are ideal pin and roller.

**Solution.**

1. Second moment of area (the depth is in the bending direction):
   $$I = \frac{b h^3}{12} = \frac{0.100 \times (0.200)^3}{12} = 6.667 \times 10^{-5}\ \text{m}^4$$
2. Maximum moment at midspan:
   $$M_{\max} = \frac{w L^2}{8} = \frac{10\,000 \times 4.0^2}{8} = 2.00 \times 10^{4}\ \text{N·m} = 20.0\ \text{kN·m}$$
3. Maximum bending stress at the outer fiber, where $c = h/2 = 0.100$ m:
   $$\sigma_{\max} = \frac{M_{\max} c}{I} = \frac{2.00 \times 10^{4} \times 0.100}{6.667 \times 10^{-5}} = 3.00 \times 10^{7}\ \text{Pa} = 30.0\ \text{MPa}$$
4. Maximum deflection:
   $$v_{\max} = \frac{5\,w L^4}{384\,E I} = \frac{5 \times 10\,000 \times 4.0^4}{384 \times 200 \times 10^{9} \times 6.667 \times 10^{-5}} = 2.50 \times 10^{-3}\ \text{m} = 2.50\ \text{mm}$$

**Answer.** $M_{\max} = 20.0$ kN·m, $\sigma_{\max} = 30.0$ MPa, and $v_{\max} = 2.50$ mm.

**Sanity check.**

- The bending stress of 30 MPa is well below the typical mild steel yield of about 250 MPa.
- The span-to-deflection ratio is $L / v_{\max} = 4000 / 2.5 = 1600$. That is far stiffer than the common $L/360$ floor guideline, which would allow about 11.1 mm here.
- The moment of 20 kN·m is consistent with the total load of $10 \times 4 = 40$ kN. The moment at midspan is one eighth of $wL^2$, which matches the simply supported shape.

## Practice

1. A simply supported beam of span 3.0 m carries a point load of 5 kN at midspan. It has the same 100 mm by 200 mm rectangular section and $E = 200$ GPa. Find the maximum moment in kN·m, the maximum bending stress in MPa, and the maximum deflection in mm.
2. A rectangular section is 50 mm wide and 100 mm deep. Find its second moment of area in mm⁴ and its section modulus in cm³.
3. A pinned-pinned steel column is a solid circular rod with diameter 25 mm and length 1.8 m. It has $E = 200$ GPa. Find the Euler critical load in kN and the critical stress in MPa.
4. The same rod as problem 3 is fixed at both ends, so $K = 0.5$. Find the new critical load in kN.

<details><summary>Answers</summary>

1. 3.75 kN·m; 5.6 MPa; 0.211 mm
2. 4.17 × 10^6 mm⁴; 83.3 cm³
3. 11.7 kN; 23.8 MPa
4. 46.7 kN

</details>

## Common mistakes

- Swapping $b$ and $h$. The depth is cubed in $I$, so orientation changes the answer by a large factor. Check which direction the load bends the beam.
- Using the centerline distance instead of $c$, the distance to the outermost fiber, when computing bending stress.
- Using $L$ in the Euler formula when the end conditions give a different effective length. Use $KL$.
- Applying Euler's formula to a short, stocky column. If the slenderness ratio is small, the column yields before it buckles and Euler's formula overpredicts the load.
- Checking buckling about the wrong axis. Use the smallest second moment of area in the Euler formula.
- Reading the deflection as a stress check. Deflection and stress are separate limits, and a beam can pass one and fail the other.

## Go deeper

- [Chapter 8: Beam Bending, Buckling, and Torsion](https://eng.libretexts.org/Courses/California_State_Polytechnic_University_Humboldt/Mechanical_Behavior_of_Material/Chapter_8:_Beam_Bending,_Buckling,_and_Torsion) by Cal Poly Humboldt, via Engineering LibreTexts: free notes on Euler-Bernoulli beams, the simply supported deflection formulas, and the pinned column derivation.
- [Stresses in Beams](https://eng.libretexts.org/Bookshelves/Mechanical_Engineering/Mechanics_of_Materials_%28Roylance%29/04:_Bending/4.02:_Stresses_in_Beams) by David Roylance, MIT OpenCourseWare, via Engineering LibreTexts: the flexure formula and the pinned-pinned buckling load, in a free, openly licensed textbook.
- Previous lesson: [Axial and torsion](04-axial-and-torsion.md), which covers the stress and strain basics used here.
