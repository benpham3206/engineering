# Define the problem

**Type:** lesson

Most wrong engineering answers start with a problem that was never fully stated. Before you
write an equation, you need to know what you have, what you want, and what you are assuming.
Engineers call this step scoping, and it takes less time than the mistakes it prevents.

**Prerequisites:** none, but [Algebra](../math/01-algebra.md) helps.
**Time:** 2-3 h

## Core ideas

- A **known** is a number or fact you are given. Write it with its unit.
- An **unknown** is what you must find. Name it with a symbol and a unit.
- An **assumption** is a simplifying choice you make on purpose, such as "ignore air resistance"
  or "the cable is massless." Assumptions are not hidden. You write them down so a reader can
  check them.
- A **constraint** is a rule the system must obey, such as "the sign does not move" or "the
  box stays on the ramp."
- Write a **goal statement** in one sentence: "Find the tension in each cable."

Good problem definitions share three habits:

- Every number has a unit. A bare "50" is not a known.
- Every symbol is defined once. If you use $W$ for weight, say so.
- Every assumption names what it throws away and why it is safe to throw it away.

A useful test: could a classmate solve the problem from your list alone, without asking you
a single question? If not, the list is incomplete.

### Why this matters

Problems in engineering are often vague on purpose. A client says "the shelf must hold my
books." An engineer has to decide how many books, how far the shelf spans, what material it is
made of, and whether a safety factor applies. Each choice becomes a known, an assumption, or a
constraint. Skipping this step does not remove the choices. It only hides them.

### Common forms of a clear problem

- A **sketch-first** problem: the picture is given, and the list of knowns is read from it.
- A **text-only** problem: you must draw the picture yourself (lesson 02).
- A **design** problem: some quantities are free to choose, and the goal is to pick them so a
  requirement is met. Write the free choices as unknowns and the requirement as a constraint.

## Key equations

No equations yet. This lesson is about the list that comes before equations. The list is
complete when it has:

$$
\text{knowns} + \text{unknowns} + \text{assumptions} + \text{constraints} + \text{goal} = \text{problem statement}
$$

Count the unknowns against the number of independent equations you expect. If you have fewer
equations than unknowns, the problem is either under-specified (you need another known or
assumption) or you need a constraint you have not yet written down.

## Worked example

**Problem.** A sign with mass $m$ hangs from the middle of a horizontal bar by two cables.
Each cable makes an angle $\theta$ with the horizontal bar. Find the tension $T$ in each cable.

**Given (knowns):**

- Mass of the sign: $m = 50\ \text{kg}$
- Angle of each cable: $\theta = 60^\circ$ to the horizontal
- Gravity: $g = 9.81\ \text{m/s}^2$ (standard value at Earth's surface)

**Find (unknowns):**

- Tension in each cable, $T$ in newtons (N)

**Assumptions:**

- The cables are massless and do not stretch.
- The sign is hung at the center, so the two cables share the load equally.
- The sign does not swing. It is at rest.

**Constraints:**

- The sign is in equilibrium. Nothing accelerates.

**Goal:** Find $T$ for each cable at $\theta = 60^\circ$.

**Solution step (scoping only):** The weight on Earth is $W = mg = 50 \times 9.81 = 490.5\ \text{N}$.
Two cables share it, so each cable supplies roughly half the vertical support. The next lessons
turn this list into an answer.

**Answer (from the list so far):** Unknown $T$ in N. Expected size: a few hundred newtons.

**Sanity check:** The sign weighs about 490 N, so the cables together must hold about 490 N
upward. Each cable must carry some share of that. A value near 250 N to 300 N per cable is the
right order of magnitude. The lesson Sanity-check the answer covers this habit in detail.

## Practice

1. A bag has mass 12 kg. Write its weight in newtons using $g = 9.81\ \text{m/s}^2$ (Earth surface).
2. Convert a length of 2.5 ft to meters. Use $1\ \text{ft} = 0.3048\ \text{m}$.
3. Convert a speed of 30 m/s to km/h.

<details><summary>Answers</summary>

1. 117.7 N
2. 0.762 m
3. 108 km/h

</details>

## Common mistakes

- Writing a number without its unit, then mixing units later (kg with N, cm with m).
- Hiding an assumption. If you ignored friction, write "frictionless" in the list.
- Forgetting the goal. A solution that finds the wrong quantity is still wrong.
- Listing as "known" something you actually calculated. Keep knowns to given data.
- Stopping before counting unknowns against equations, which hides an under-specified problem.

## Go deeper

- [OpenStax University Physics Volume 1](https://openstax.org/details/books/university-physics-volume-1) by OpenStax: a free, peer-reviewed physics textbook. Read the first chapter on units and measurement.
- [Units and standards, section 1.2](https://openstax.org/books/university-physics-volume-1/pages/1-2-units-and-standards) by OpenStax: the base units, SI prefixes, and how units are written.
- [SI units](https://www.nist.gov/pml/owm/metric-si/si-units) by NIST: the official list of SI base units from the U.S. National Institute of Standards and Technology.
- [Classical Mechanics (8.01SC)](https://ocw.mit.edu/courses/8-01sc-classical-mechanics-fall-2016/) by MIT OpenCourseWare: free lecture notes and problem sets on forces and motion.
- George Polya, *How to Solve It* (1945): the classic book on problem-solving steps, starting with "understand the problem." Read the first part. It is a printed book, so no link is given.
- [Problem-solving reference](reference.md): the lookup sheet for this topic.
