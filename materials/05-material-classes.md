# Metals, polymers, ceramics, composites

**Type:** lesson

Engineering materials fall into four broad classes. Each class has a typical bonding type, a typical range of properties, and typical uses. Knowing the class tells you what to expect before you test a single sample.

**Prerequisites:** [Atomic structure and bonding](01-atomic-structure-bonding.md), [Crystal structures and defects](02-crystal-structures-defects.md), [Mechanical properties](03-mechanical-properties.md), [Algebra](../math/01-algebra.md)
**Time:** 6-8 h

## Core ideas

- **Metals** have metallic bonds. They are conductive, usually ductile, and dense. Most are crystalline polycrystals. Examples: steel, aluminum, copper, titanium.
- **Polymers** are long chains of repeating units (monomers) held together by covalent bonds. Weak secondary bonds tie the chains to each other. Examples: polyethylene, nylon, ABS, epoxy.
- **Ceramics** are compounds of metals or semimetals with oxygen, nitrogen, or carbon, held together by ionic and covalent bonds. They are hard, stiff, heat resistant, and brittle. Examples: alumina, silicon carbide, glass, concrete.
- **Composites** combine two or more materials with different properties so the result is better than either alone. Usually a strong, stiff fiber or particle sits inside a tougher matrix. Examples: carbon fiber reinforced polymer, fiberglass, reinforced concrete.

### Typical behavior by class

- **Metals.** High stiffness and strength for their density, good toughness, and conduct heat and electricity. They yield before they break, which gives warning before failure.
- **Polymers.** Low stiffness, low density, low melting point, and good chemical resistance. They creep under load at room temperature more than metals do. Many are excellent electrical insulators.
- **Ceramics.** Very high stiffness and hardness, high melting point, and good corrosion and wear resistance. They fail suddenly by brittle fracture, and tensile strength is much lower than compressive strength.
- **Composites.** Properties depend on fiber, matrix, and layout. Fibers aligned with the load give high stiffness and strength in that direction. The matrix holds the fibers and spreads the load. Composite properties are often anisotropic, meaning they change with direction.

### Why the classes behave differently

- Metals have free electrons and non-directional bonds, so atoms slide and the material yields.
- Polymer chains slip past each other, and secondary bonds let them stretch and creep. Their glass transition temperature sets where they soften.
- Ceramics have rigid, directional bonds and few slip systems, so cracks grow fast once they start.
- Composites use the stiff, strong fiber to carry load and the matrix to hold the fibers and resist cracks.

## Key equations

For a fiber-reinforced composite loaded along the fiber direction, the **rule of mixtures** gives a simple estimate of stiffness:

$$E_c = V_f\, E_f + (1 - V_f)\, E_m$$

where:

- $E_c$ is the composite modulus along the fiber direction (GPa)
- $E_f$ is the fiber modulus (GPa)
- $E_m$ is the matrix modulus (GPa)
- $V_f$ is the volume fraction of fiber (dimensionless, between 0 and 1)

This assumes perfect bonding and fibers all aligned with the load. Real composites are a little weaker.

## Worked example

**Given:** A glass fiber composite has a fiber modulus $E_f = 72$ GPa, an epoxy matrix modulus $E_m = 3$ GPa, and a fiber volume fraction $V_f = 0.50$. The fibers are aligned with the load.

**Find:** The composite modulus $E_c$ along the fiber direction.

**Assumptions:** Perfect bonding between fiber and matrix, aligned fibers, linear elastic behavior. Typical textbook values.

**Solution:**

1. Fiber part: $V_f E_f = 0.50 \times 72 = 36.0$ GPa.
2. Matrix part: $(1 - V_f) E_m = 0.50 \times 3 = 1.5$ GPa.
3. Add: $E_c = 36.0 + 1.5 = 37.5$ GPa.

**Answer:** $E_c = 37.5$ GPa along the fiber direction.

**Sanity check:** The result lies between the matrix modulus (3 GPa) and the fiber modulus (72 GPa), as it must. It is closer to the fiber value because the fiber fraction is large. Stiffness across the fibers would be much lower, which is why the answer applies only along the fiber direction.

## Practice

1. Use the rule of mixtures with $E_f = 72$ GPa, $E_m = 3$ GPa, and $V_f = 0.30$. Find $E_c$.
2. Which class, metal, polymer, ceramic, or composite, usually has the highest melting temperature in this list: nylon, aluminum, alumina?
3. Why does a ceramic plate crack suddenly instead of bending first?
4. A composite has $E_c = 37.5$ GPa at $V_f = 0.50$. What would the fiber fraction need to be for $E_c = 23.7$ GPa, using the same $E_f$ and $E_m$?
5. Give one reason an engineer might choose a metal over a polymer for a bracket that will carry a constant load for ten years.

<details><summary>Answers</summary>

1. $E_c = 23.7$ GPa
2. Alumina (a ceramic)
3. Ceramic bonds are rigid and directional, and there are few slip systems, so a crack grows quickly without plastic yielding first.
4. $V_f = 0.30$ (since $23.7 = 72 V_f + 3(1 - V_f)$ gives $V_f = 0.30$)
5. Metals resist creep at room temperature much better than most polymers, so the bracket keeps its shape over time.

</details>

## Common mistakes

- Using the rule of mixtures for loads across the fibers. It only applies along the fiber direction.
- Mixing up the volume fraction of fiber with the mass fraction. The rule of mixtures uses volume fractions.
- Calling a material "ceramic" because it is hard. Glass is a ceramic, but many hard materials, such as tool steel, are metals.
- Assuming polymers always fail gently. Some polymers are brittle at low temperature.
- Ignoring temperature. A polymer that is stiff at room temperature may soften near its glass transition.

## Go deeper

- [Mechanics of Materials](https://ocw.mit.edu/courses/3-11-mechanics-of-materials-fall-1999/) by MIT OpenCourseWare: mechanical properties of ceramics, metals, and polymers.
- [Fundamentals of Materials Science](https://ocw.mit.edu/courses/3-012-fundamentals-of-materials-science-fall-2005/) by MIT OpenCourseWare: how bonding determines the four material classes.
- [Introduction to Solid-State Chemistry](https://ocw.mit.edu/courses/3-091-introduction-to-solid-state-chemistry-fall-2018/) by MIT OpenCourseWare: why solids of different bonding types behave differently.
- [Materials reference](reference.md): the lookup sheet for this topic.
