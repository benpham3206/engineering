# Crystal structures and defects

**Type:** lesson

A **crystal structure** is the regular, repeating arrangement of atoms in a solid, and a **defect** is a flaw in that arrangement. Engineers need both because the pattern decides how dense the material is, how it deforms, and where it is weak. Most engineering metals and many ceramics are crystalline, and the flaws in real crystals often control strength.

**Prerequisites:** [Atomic structure and bonding](01-atomic-structure-bonding.md), [Algebra](../math/01-algebra.md)
**Time:** 6-8 h

## Core ideas

- A **crystal** is a solid whose atoms are arranged in a repeating 3D pattern.
- A **lattice** is the set of points that the pattern repeats around. Each point is the same relative to its neighbors.
- A **unit cell** is the smallest box that, repeated in all directions, builds the whole crystal. Its edge length is the **lattice parameter**, written $a$.
- A **polycrystal** is many small crystals (grains) packed together. The boundary between grains is a **grain boundary**. Most metal parts are polycrystals.
- An **amorphous** solid, such as ordinary glass, has no long-range repeating pattern.

### The three common metal structures

- **Body-centered cubic (BCC).** Atoms sit at the corners of a cube and one atom in the center. Examples: iron at room temperature, chromium, tungsten. BCC metals are strong but can be brittle at low temperature.
- **Face-centered cubic (FCC).** Atoms sit at the corners and at the center of each face. Examples: aluminum, copper, nickel, austenitic stainless steel. FCC metals are usually ductile, which makes them easy to form.
- **Hexagonal close-packed (HCP).** Atoms form stacked hexagonal layers. Examples: titanium (at room temperature), magnesium, zinc. HCP metals often have fewer slip systems, so they are less ductile.

### Packing and density

**Atomic packing factor (APF)** is the fraction of a unit cell's volume filled by atoms. Atoms are treated as hard spheres. Close packing gives the highest APF possible for spheres, about 0.74. BCC gives about 0.68. Higher packing usually means higher density for a given atomic mass.

### Point defects

- A **vacancy** is a missing atom from a lattice site.
- A **self-interstitial** is an extra atom squeezed into a gap.
- A **substitutional impurity** is a foreign atom sitting on a normal lattice site, such as zinc in brass.
- An **interstitial impurity** is a small foreign atom in a gap, such as carbon in iron. Carbon in iron is what makes steel stronger than pure iron.

### Line and planar defects

- A **dislocation** is a line where the lattice is out of step. Dislocations move under stress, and their motion is how metals deform permanently. Making dislocations hard to move is one of the main ways to strengthen a metal.
- A grain boundary is a planar defect between grains of different orientation. Smaller grains mean more boundaries. More boundaries block dislocation motion, so fine-grained metals are usually stronger. This is the **Hall-Petch effect**.

## Key equations

Density of a crystal follows from its cell contents:

$$\rho = \frac{n\, M}{V_c\, N_A}$$

where:

- $\rho$ is the density ($\text{kg/m}^3$)
- $n$ is the number of atoms in one unit cell (dimensionless)
- $M$ is the molar mass of the element (kg/mol)
- $V_c = a^3$ is the volume of the unit cell ($\text{m}^3$) for a cubic cell
- $N_A = 6.022 \times 10^{23}$ $\text{mol}^{-1}$ is Avogadro's number

Atomic packing factor is

$$\text{APF} = \frac{n\, \tfrac{4}{3}\pi r^3}{V_c}$$

where $r$ is the atomic radius (m). For FCC, $n = 4$ and $a = 2\sqrt{2}\, r$, which gives APF $\approx 0.74$.

Atoms per cell: simple cubic 1, BCC 2, FCC 4.

## Worked example

**Given:** Alpha iron is BCC with lattice parameter $a = 0.2866$ nm. The molar mass of iron is $M = 55.85$ g/mol.

**Find:** The density of iron, in $\text{kg/m}^3$.

**Assumptions:** Pure iron at room temperature, perfect lattice, no vacancies. Typical value for comparison: about 7870 $\text{kg/m}^3$.

**Solution:**

1. Convert units: $a = 0.2866 \times 10^{-9}$ m, so $V_c = a^3 = 2.354 \times 10^{-29}$ $\text{m}^3$. $M = 0.05585$ kg/mol.
2. BCC has $n = 2$ atoms per cell.
3. $\rho = \dfrac{2 \times 0.05585}{(2.354 \times 10^{-29})(6.022 \times 10^{23})} = 7879$ $\text{kg/m}^3$.

**Answer:** $\rho \approx 7.88 \times 10^{3}$ $\text{kg/m}^3$.

**Sanity check:** This is close to the typical value of 7870 $\text{kg/m}^3$. The difference is well under 1 percent, which is expected for a textbook lattice parameter. A density near 2700 or 20000 $\text{kg/m}^3$ would signal an error in the atom count or the unit conversion.

## Practice

1. How many atoms belong to one FCC unit cell? (Count corner and face atoms, with each shared correctly.)
2. What is the APF of a simple cubic lattice, where each cell has one atom? Use $r = a/2$.
3. Copper is FCC with $a = 0.3615$ nm and $M = 63.55$ g/mol. Find its density in $\text{kg/m}^3$.
4. Name two strengthening methods that work by blocking dislocation motion.
5. A metal's grain size drops from 100 $\mu\text{m}$ to 10 $\mu\text{m}$. Does the number of grain boundaries per unit length go up or down?

<details><summary>Answers</summary>

1. 4
2. about 0.52
3. about 8935 $\text{kg/m}^3$
4. Any two of: grain refinement, solid solution alloying, cold work, precipitates
5. Up (ten times more boundaries per unit length)

</details>

## Common mistakes

- Counting a corner atom as fully inside the cell. Each corner atom is shared by eight cells, so it counts as $1/8$.
- Forgetting that a face atom is shared by two cells, so it counts as $1/2$.
- Mixing up nanometres, angstroms, and metres. Convert everything to metres before cubing $a$.
- Assuming all metals are equally ductile because they are all metals. Crystal structure matters a lot.
- Thinking defects are always bad. Carbon in iron and dislocations in metal are the reason steel can be shaped and strengthened.

## Go deeper

- [Introduction to Solid-State Chemistry](https://ocw.mit.edu/courses/3-091-introduction-to-solid-state-chemistry-fall-2018/) by MIT OpenCourseWare: lattices, unit cells, and defects.
- [Fundamentals of Materials Science](https://ocw.mit.edu/courses/3-012-fundamentals-of-materials-science-fall-2005/) by MIT OpenCourseWare: crystal structure, defects, and their effect on properties.
- [Materials Laboratory](https://ocw.mit.edu/courses/3-014-materials-laboratory-fall-2006/) by MIT OpenCourseWare: how structure is measured in the lab, including x-ray scattering.
- [Materials reference](reference.md): the lookup sheet for this topic.
