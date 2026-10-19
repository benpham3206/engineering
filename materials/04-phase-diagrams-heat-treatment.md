# Phase diagrams and heat treatment

**Type:** lesson

An alloy can have different internal structures at different temperatures and compositions. A phase diagram is the map that shows which structure is stable where. Heat treatment uses that map to set the final structure on purpose, and the structure sets the strength and toughness of the part.

**Prerequisites:** [Crystal structures and defects](02-crystal-structures-defects.md), [Mechanical properties](03-mechanical-properties.md), [Algebra](../math/01-algebra.md)
**Time:** 8-10 h

## Core ideas

- A **phase** is a region of a material with uniform structure and composition, such as liquid, a solid solution, or a compound.
- A **component** is a chemical species that makes up the system, such as copper and nickel in a Cu-Ni alloy.
- A **phase diagram** plots the stable phases against temperature and composition, at a fixed pressure (usually 1 atm).
- A **solid solution** has one crystal structure with two elements mixed in it. A **eutectic** is a composition that melts at a single lowest temperature and freezes into two solid phases together.
- A **microstructure** is the arrangement of phases and grains you see under a microscope. Two alloys with the same composition can have different microstructures if they were cooled differently.

### Reading a phase diagram

- A **single-phase region** has one phase. A **two-phase region** has two phases together, and their compositions are found by drawing a tie line.
- The **liquidus** is the line above which the alloy is fully liquid. The **solidus** is the line below which it is fully solid.
- Between the two lines, the alloy is part solid and part liquid.

### The lever rule

In a two-phase region, the mass fraction of each phase is found by the lever rule. Draw a horizontal tie line through the alloy's composition. The fraction of one phase is the length of the arm on the opposite side, divided by the full tie line length.

### Iron-carbon and steel

- Steel is iron with a small amount of carbon, typically below about 2 wt% C.
- At 0.76 wt% C (the eutectoid composition), slow cooling forms **pearlite**, a layered mix of ferrite and cementite.
- Hypoeutectoid steels (below 0.76 wt% C) form some ferrite before pearlite. Hypereutectoid steels form some cementite first.

### Heat treatment

- **Annealing.** Heat the metal, then cool slowly. This gives a soft, ductile, low-stress structure. Engineers use it before forming or machining.
- **Normalizing.** Heat, then cool in still air. Gives a finer, more uniform structure than annealing.
- **Quenching.** Heat, then cool very fast, usually in water, oil, or a polymer bath. In steel this traps carbon and forms **martensite**, a very hard but brittle phase.
- **Tempering.** Reheat a quenched part to a moderate temperature, then cool. This reduces brittleness at the cost of some hardness. Engineers temper almost every quenched steel part.
- **Precipitation hardening (aging).** Dissolve a second phase at high temperature, quench, then hold at a lower temperature so fine particles form. The particles block dislocations. Engineers use it on aluminum alloys such as 6061-T6 (the "T6" means solution heat treated and artificially aged).

## Key equations

For an alloy of overall composition $C_0$ in a two-phase region with liquid composition $C_L$ and solid composition $C_S$ (all in wt%), the mass fractions are

$$W_L = \frac{C_S - C_0}{C_S - C_L}, \qquad W_S = \frac{C_0 - C_L}{C_S - C_L}$$

where:

- $W_L$ is the mass fraction of liquid (dimensionless, between 0 and 1)
- $W_S$ is the mass fraction of solid (dimensionless)
- $C_0$ is the overall alloy composition (wt%)
- $C_L$ is the composition of the liquid at that temperature (wt%)
- $C_S$ is the composition of the solid at that temperature (wt%)

The two fractions always add to 1.

## Worked example

**Given:** A Cu-Ni alloy with overall composition $C_0 = 35$ wt% Ni is held at a temperature where the liquid has $C_L = 32$ wt% Ni and the solid has $C_S = 43$ wt% Ni. These values are read from the phase diagram at that temperature. The numbers here are for practice, not a published diagram.

**Find:** The mass fraction of solid and of liquid.

**Assumptions:** Equilibrium cooling, so the phases have the compositions shown by the tie line.

**Solution:**

1. Solid fraction: $W_S = \dfrac{C_0 - C_L}{C_S - C_L} = \dfrac{35 - 32}{43 - 32} = \dfrac{3}{11} = 0.273$.
2. Liquid fraction: $W_L = \dfrac{C_S - C_0}{C_S - C_L} = \dfrac{43 - 35}{11} = \dfrac{8}{11} = 0.727$.

**Answer:** About 27.3 percent solid and 72.7 percent liquid by mass.

**Sanity check:** $0.273 + 0.727 = 1.000$. The overall composition 35 is closer to the liquid value 32 than to the solid value 43, and the liquid fraction is the larger one.

## Practice

1. An alloy with $C_0 = 40$, $C_L = 30$, and $C_S = 50$ (wt%) is in a two-phase region. Find $W_S$ and $W_L$.
2. An alloy with $C_0 = 60$, $C_L = 55$, and $C_S = 70$ (wt%) is in a two-phase region. Find $W_S$.
3. What composition of carbon in iron (in wt%) is called the eutectoid composition?
4. Why is a quenched steel part usually tempered before use?
5. Which is harder, martensite or pearlite? Answer with one word.

<details><summary>Answers</summary>

1. $W_S = 0.50$, $W_L = 0.50$
2. $W_S = 0.333$
3. 0.76 wt% C
4. Tempering reduces brittleness from quenching; it lowers hardness somewhat but raises toughness
5. Martensite

</details>

## Common mistakes

- Swapping $C_L$ and $C_S$ in the lever rule. The fraction of solid uses the distance from $C_0$ to the liquid side, so check your numerator carefully.
- Reading the composition from the wrong line (liquidus instead of solidus) at a given temperature.
- Forgetting that heat treatment changes the microstructure, not the chemical composition.
- Assuming a quenched part is ready to use. Quenched martensite is often too brittle, so engineers temper it.
- Confusing annealing (slow cool, soft) with quenching (fast cool, hard).

## Go deeper

- [Fundamentals of Materials Science](https://ocw.mit.edu/courses/3-012-fundamentals-of-materials-science-fall-2005/) by MIT OpenCourseWare: phase equilibria, phase diagrams, and microstructure.
- [Materials Laboratory](https://ocw.mit.edu/courses/3-014-materials-laboratory-fall-2006/) by MIT OpenCourseWare: thermal analysis (DSC) used to find phase transformation temperatures.
- [Crystal structures and defects](02-crystal-structures-defects.md): the lattice ideas behind phases and solid solutions.
- [Materials reference](reference.md): the lookup sheet for this topic.
