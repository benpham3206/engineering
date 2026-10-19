# Mechanical properties: strength, stiffness, hardness, toughness, ductility

**Type:** lesson

Mechanical properties describe how a material responds to force. Engineers use them to decide whether a beam will sag, a shaft will snap, or a bracket will bend permanently.
**Prerequisites:** [Atomic structure and bonding](01-atomic-structure-bonding.md), [Crystal structures and defects](02-crystal-structures-defects.md), [Algebra](../math/01-algebra.md)
**Time:** 8-10 h

## Core ideas

- **Stress** is force divided by area. It tells you how hard the material is being pushed or pulled inside. Its unit is the pascal (Pa), or megapascal (MPa, $10^6$ Pa).
- **Strain** is change in length divided by the original length. It is dimensionless, or given as a percent.
- A **stress-strain curve** plots stress against strain during a test. It is the basic picture of mechanical behavior.

### Stiffness

- **Stiffness** is how much a material resists elastic stretching. The measure is **Young's modulus** ($E$), the ratio of stress to strain in the elastic range.
- Stiffness depends mainly on bonding. Strong bonds give a high modulus. Metals are stiff, polymers are not, and most ceramics are stiff but brittle.
- Stiffness is not strength. Steel and glass have similar stiffness, but glass fails at much lower stress.

### Strength

- **Yield strength** ($\sigma_y$) is the stress where permanent (plastic) deformation starts. Engineers usually design so the part never reaches yield.
- **Ultimate tensile strength** is the highest stress on the curve.
- Some materials, such as glass and many ceramics, break without yielding. For these, the fracture strength is the useful number.

### Ductility and toughness

- **Ductility** is how much a material stretches before breaking. Percent elongation at fracture is a common measure. Copper and aluminum are ductile. Cast iron and glass are not.
- **Toughness** is the energy a material absorbs before it breaks. It is the area under the stress-strain curve up to fracture. A tough material can be strong and ductile at the same time.
- **Brittle** materials break with little plastic deformation. They have low toughness.

### Hardness

- **Hardness** is resistance to local indentation or scratching. Common tests are Rockwell, Brinell, and Vickers.
- Hardness correlates roughly with yield strength for metals, which is why hardness tests are fast and useful on the shop floor.

## Key equations

Stress and strain for a uniaxial tensile test:

$$\sigma = \frac{F}{A_0}, \qquad \varepsilon = \frac{\Delta L}{L_0}$$

where:

- $\sigma$ is engineering stress (Pa or MPa)
- $F$ is the applied force (N)
- $A_0$ is the original cross-sectional area (m$^2$)
- $\varepsilon$ is engineering strain (dimensionless)
- $\Delta L$ is the change in gauge length (m)
- $L_0$ is the original gauge length (m)

In the elastic range, Hooke's law links them:

$$\sigma = E\, \varepsilon$$

where $E$ is Young's modulus (Pa or GPa, with $1\ \mathrm{GPa} = 10^9\ \mathrm{Pa}$). In US customary units, $E$ is often given in ksi or Msi ($\mathrm{psi} = \mathrm{lb/in^2}$, $1\ \mathrm{ksi} = 1000\ \mathrm{psi}$).

### Typical property values

These are typical textbook values at room temperature. Real values depend on alloy, heat treatment, grain size, moisture, and processing, so use supplier data for real design work. Yield strength is listed as "n/a" when the material does not yield in a clear, sharp way.

| Material | Density $\rho$ (kg/m$^3$) | Young's modulus $E$ (GPa) | Yield strength $\sigma_y$ (MPa) |
|---|---|---|---|
| 1018 steel (cold drawn) | 7870 | 205 | 370 |
| 6061-T6 aluminum | 2700 | 69 | 276 |
| Ti-6Al-4V titanium (annealed) | 4430 | 114 | 880 |
| ABS plastic | 1050 | 2.3 | 40 |
| Nylon 6/6 (dry) | 1140 | 2.9 | 80 |
| Soda-lime glass | 2500 | 70 | n/a (brittle) |
| Concrete | 2400 | 30 | n/a (brittle; compressive strength about 30 MPa) |
| Wood, Douglas fir (along grain) | 530 | 13 | n/a (strength varies widely with defects and direction) |

## Worked example

**Given:** A 10 mm diameter round bar of 1018 steel has a 200 mm gauge length. A tensile load of $F = 20$ kN is applied, and the gauge length grows by $\Delta L = 0.25$ mm. Yield strength of the steel is about 370 MPa.

**Find:** (a) the stress, (b) the strain, (c) Young's modulus, and (d) the load at which yield starts.

**Assumptions:** The load is in the elastic range. The bar is uniform, and the stress is uniform across the cross-section.

**Solution:**

1. Area: $A_0 = \pi (0.005\ \text{m})^2 = 7.854 \times 10^{-5}$ m$^2$.
2. Stress: $\sigma = 20\,000 / 7.854 \times 10^{-5} = 2.546 \times 10^{8}$ Pa $= 254.6$ MPa.
3. Strain: $\varepsilon = 0.25 / 200 = 0.00125$.
4. Modulus: $E = \sigma / \varepsilon = 254.6 \times 10^{6} / 0.00125 = 2.037 \times 10^{11}$ Pa $= 204$ GPa.
5. Load at yield: $F_y = \sigma_y A_0 = (370 \times 10^{6})(7.854 \times 10^{-5}) = 29\,060$ N $\approx 29$ kN.

**Answers:** (a) 254.6 MPa, (b) 0.00125 (0.125 percent), (c) about 204 GPa, (d) about 29 kN.

**Sanity check:** 204 GPa is close to the typical 205 GPa for steel. The 20 kN load is below the 29 kN yield load, so the test stayed elastic, which matches the assumption.

## Practice

1. A 5 mm diameter rod carries 4 kN. What is the stress in MPa? (Area $= 1.963 \times 10^{-5}$ m$^2$.)
2. A 100 mm long aluminum bar stretches 0.10 mm under load. What is its strain?
3. Using the strain from Problem 2 and a stress of 69 MPa, find the modulus in GPa.
4. Which has higher toughness, a material with high strength and low ductility, or one with moderate strength and high ductility? Explain in one sentence.
5. Using the table, which listed metal has the largest yield margin over a 200 MPa design stress, and what is that margin?

<details><summary>Answers</summary>

1. about 204 MPa
2. 0.001
3. 69 GPa
4. Moderate strength with high ductility (it absorbs more energy before breaking; the area under the curve is larger)
5. Ti-6Al-4V, margin 680 MPa (880 minus 200)

</details>

## Common mistakes

- Mixing up stiffness and strength. A stiff material can still yield at a low stress.
- Using the diameter as the radius when computing area. Area uses the radius, $A = \pi r^2$.
- Forgetting to convert millimetres to metres before computing area in SI.
- Treating the table values as guaranteed. They are typical values, not minimums for a specific supplier.
- Reading strain as a percent without converting. A strain of 0.00125 is 0.125 percent.

## Go deeper

- [Mechanics of Materials](https://ocw.mit.edu/courses/3-11-mechanics-of-materials-fall-1999/) by MIT OpenCourseWare: stress, strain, and mechanical behavior of ceramics, metals, and polymers.
- [Fundamentals of Materials Science](https://ocw.mit.edu/courses/3-012-fundamentals-of-materials-science-fall-2005/) by MIT OpenCourseWare: how bonding and structure set stiffness and strength.
- [Materials Laboratory](https://ocw.mit.edu/courses/3-014-materials-laboratory-fall-2006/) by MIT OpenCourseWare: how tests such as tension and hardness are run in practice.
- [Materials reference](reference.md): the lookup sheet for this topic.
