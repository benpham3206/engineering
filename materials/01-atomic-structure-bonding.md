# Atomic structure and bonding

**Type:** lesson

Every material property you will meet later comes from how atoms hold on to their electrons and to each other. An engineer who knows why steel is stiff and rubber is soft can predict how a part will behave before building it.

**Prerequisites:** none
**Time:** 6-8 h

## Core ideas

- An atom has a small, dense nucleus of protons and neutrons, surrounded by electrons.
- The number of protons is the atomic number (Z). It sets which element you have.
- Electrons sit in shells and subshells. Only the outermost ones, the valence electrons, take part in bonding.
- The periodic table groups elements by valence electron count. Elements in the same column tend to behave alike.
- Electronegativity is a number that describes how strongly an atom pulls shared electrons toward itself. Fluorine and oxygen have high values. Sodium and magnesium have low values.

Atoms bond because the combined system has lower energy than the separate atoms. Atoms reach a stable arrangement by sharing, giving up, or pooling their valence electrons. The bond type decides most of the material's basic character.

### The main bond types

- **Ionic bond.** One atom gives electrons to another. Both become charged ions (for example Na+ and Cl-), and they attract each other. Ionic solids such as table salt are hard and brittle, and they melt at high temperature.
- **Covalent bond.** Two atoms share a pair of electrons. Silicon, carbon, and many polymers form covalent bonds. Covalent bonds are strong and directional, which gives diamond its hardness and polymer chains their stiffness along the chain.
- **Metallic bond.** Metal atoms release their valence electrons into a shared "sea" that moves freely. The positive ion cores sit in the sea and are held together by it. This explains why metals conduct electricity and heat well, and why they bend without breaking.
- **Secondary bonds.** Van der Waals forces and hydrogen bonds are weak attractions between molecules. They are much weaker than the bonds above, and they explain why many polymers soften at low temperature.

### Why bond type matters for engineers

- Bond strength sets the melting point. Stronger bonds need more heat to break.
- Covalent bonds are directional, so covalent solids tend to be brittle. Ionic bonds are nondirectional, but ionic solids are also brittle because slip moves like charges next to each other and they repel. Metallic bonds are nondirectional and let atoms slide, so metals are ductile.
- Secondary bonds let polymer chains slip, so plastics creep and soften more than metals or ceramics do.

## Key equations

The attraction between two opposite charges is given by Coulomb's law. For an ion pair, the potential energy is

$$U = -\frac{k\, e^2}{r}$$

where:

- $U$ is the potential energy of the pair (joules, J, or electron volts, eV, with 1 eV = $1.602 \times 10^{-19}$ J)
- $k = 8.988 \times 10^{9}$ N m$^2$/C$^2$ is Coulomb's constant
- $e = 1.602 \times 10^{-19}$ C is the elementary charge (one proton or electron)
- $r$ is the distance between the two ion centers (metres, m)

The minus sign means the pair is bound. Energy must be added to pull the ions apart. The energy magnitude falls as $1/r$, so a larger separation gives a weaker bond.

Electronegativity difference is a rough guide to bond character. A large difference between two atoms means the bond is more ionic. A small difference means it is more covalent or metallic.

## Worked example

**Given:** A sodium ion (Na+, charge +e) and a chloride ion (Cl-, charge -e) have their centers 0.25 nm apart.

**Find:** The Coulomb energy of this isolated ion pair, in eV.

**Assumptions:** The ions are point charges in vacuum. We ignore the crystal around them, which changes the real bond energy. This gives a first estimate only.

**Solution:**

1. Convert the distance: $r = 0.25 \times 10^{-9}$ m.
2. Substitute: $U = -\dfrac{(8.988 \times 10^{9})(1.602 \times 10^{-19})^2}{0.25 \times 10^{-9}}$.
3. The numerator is $2.307 \times 10^{-28}$ J m, so $U = -9.23 \times 10^{-19}$ J.
4. Divide by $1.602 \times 10^{-19}$ J/eV: $U = -5.76$ eV.

**Answer:** $U \approx -5.8$ eV for this isolated pair.

**Sanity check:** Bond energies in solids are typically a few eV per bond, so $-5.8$ eV is the right order of magnitude. If we double the distance to 0.50 nm, the energy halves to $-2.88$ eV, which matches the $1/r$ rule.

## Practice

1. How many valence electrons do aluminum (Al, group 13), silicon (Si, group 14), and oxygen (O, group 16) have?
2. Two ions of charge +e and -e are 0.30 nm apart. Find the Coulomb energy in eV. Use the same method as the worked example.
3. If the separation in Problem 2 doubles, what is the new energy in eV?
4. Pauling electronegativity values are Mg 1.31, Si 1.90, and O 3.44. Which bond, Mg-O or Si-O, is more ionic? Give the difference for each.
5. Explain in two sentences why copper can be bent into a wire but a glass rod cannot.

<details><summary>Answers</summary>

1. Al 3, Si 4, O 6
2. about -4.80 eV
3. about -2.40 eV
4. Mg-O (difference 2.13) is more ionic than Si-O (difference 1.54)
5. Answer in your own words. Copper has metallic bonds that let atoms slide. Glass has directional covalent bonds (with some ionic character) that resist sliding.

</details>

## Common mistakes

- Mixing up the number of protons (atomic number) with atomic mass. Protons set the element, but neutrons change the mass.
- Forgetting the sign of bond energy. A bound pair has negative energy relative to separated ions.
- Using the single-pair Coulomb energy as the energy of a whole crystal. Real solids have many neighbors, so the total energy is different.
- Assuming "ionic" or "covalent" is a sharp category. Most real bonds are a mix, and the electronegativity difference only gives a guide.
- Calling a metal "strong because it is stiff." Stiffness and strength are different properties. Lesson 03 explains the difference.

## Go deeper

- [Chemistry 2e](https://openstax.org/books/chemistry-2e/pages/1-introduction) by OpenStax: free college chemistry textbook. Chapters 6 to 8 cover electron structure, periodic trends, and chemical bonding.
- [Introduction to Solid-State Chemistry](https://ocw.mit.edu/courses/3-091-introduction-to-solid-state-chemistry-fall-2018/) by MIT OpenCourseWare: how bonding and structure explain why solids behave as they do.
- [Fundamentals of Materials Science](https://ocw.mit.edu/courses/3-012-fundamentals-of-materials-science-fall-2005/) by MIT OpenCourseWare: structure, energetics, and bonding in engineering materials.
- [Physics folder](../physics/README.md): forces and energy background that helps with Coulomb's law.
- [Materials reference](reference.md): the lookup sheet for this topic.
