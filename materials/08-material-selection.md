# Material selection

Choosing a material is a design decision with numbers attached. Engineers start with what the part must do, turn that into a simple objective (usually mass or cost), and then rank candidate materials by a performance index. Michael Ashby popularized this method, and it works for almost any structural part.

**Prerequisites:** [Mechanical properties](03-mechanical-properties.md), [Material classes](05-material-classes.md), [Failure: fracture and fatigue](06-fracture-and-fatigue.md), [Creep and corrosion](07-creep-and-corrosion.md)
**Time:** 8-10 h

## Core ideas

- **Function.** What the part does, such as a tie, a beam, a shaft, or a pressure vessel.
- **Constraints.** Conditions the material must meet, such as a minimum stiffness, a yield strength above a design stress, or a service temperature.
- **Objective.** What you want to minimize or maximize, usually mass, cost, or volume.
- **Free variables.** What you are allowed to change, such as the material or the cross-section size.

The procedure is always the same:

1. Write the objective as a function of the free variables and the material properties.
2. Use each constraint to eliminate the free variables that are fixed by the design.
3. What is left is a performance index, a combination of material properties. Rank materials by that index. Higher is better when maximizing.

### Example performance indices

The table below gives indices for common cases. All assume a light part, meaning the objective is mass and the length or load is fixed.

- **Stiff, light tie** (a rod in tension, stiffness limited): maximize $E/\rho$.
- **Stiff, light beam** (bending, stiffness limited, square section): maximize $E^{1/2}/\rho$.
- **Strong, light tie** (strength limited): maximize $\sigma_y/\rho$.
- **Strong, light beam** (bending, strength limited, square section): maximize $\sigma_y^{2/3}/\rho$.

Stiffness-limited means the part must not deflect too much. Strength-limited means the part must not yield. A given part is often limited by one of these, and the choice changes the ranking.

### Why the indices come out this way

- For a tie of length $L$ and required stiffness $S$, the area is $A = SL/E$. Mass is $m = \rho L A = \rho S L^2 / E$, so the index is $E/\rho$.
- For a square beam, stiffness is $S = cEa^4/L^3$, where $a$ is the side and $c$ depends on the load case. The area is $a^2$, so $a^2 \propto (E)^{-1/2}$, and mass is proportional to $\rho / E^{1/2}$. The index is $E^{1/2}/\rho$.
- The same logic gives the strength indices using $\sigma_y$ in place of $E$.

### Property table for ranking

Typical values from [Mechanical properties](03-mechanical-properties.md). The indices are computed with $\rho$ in g/cm$^3$ and $E$ and $\sigma_y$ in GPa and MPa. Only the ranking matters, so the units are shown for reference.

| Material | $\rho$ (g/cm$^3$) | $E$ (GPa) | $\sigma_y$ (MPa) | $E/\rho$ | $E^{1/2}/\rho$ | $\sigma_y/\rho$ |
|---|---|---|---|---|---|---|
| 1018 steel | 7.87 | 205 | 370 | 26.0 | 1.82 | 47.0 |
| 6061-T6 aluminum | 2.70 | 69 | 276 | 25.6 | 3.08 | 102.2 |
| Ti-6Al-4V | 4.43 | 114 | 880 | 25.7 | 2.41 | 198.6 |
| ABS | 1.05 | 2.3 | 40 | 2.2 | 1.44 | 38.1 |
| Nylon 6/6 (dry) | 1.14 | 2.9 | 80 | 2.5 | 1.49 | 70.2 |
| Soda-lime glass | 2.50 | 70 | n/a | 28.0 | 3.35 | n/a |
| Concrete | 2.40 | 30 | n/a | 12.5 | 2.28 | n/a |
| Wood, Douglas fir (along grain) | 0.53 | 13 | n/a | 24.5 | 6.80 | n/a |

Notes on the table:

- Glass has the highest $E/\rho$ and $E^{1/2}/\rho$ in this list, but it is brittle and has no yield. It cannot be chosen on stiffness alone.
- Wood is strongly directional. Its numbers apply only along the grain, and real design uses grade-specific data.
- The $\sigma_y$ indices are not given for brittle materials because they do not have a yield point. Use fracture data for them instead.

## Key equations

Mass of a stiffness-limited tie of length $L$ (m) and stiffness $S$ (N/m):

$$m = \frac{\rho\, S\, L^2}{E}$$

Mass of a square beam of length $L$ with a stiffness requirement, using $c$ as the load-case constant:

$$m \propto \frac{\rho}{E^{1/2}}$$

Mass ratio between two materials for the same stiffness and length in bending:

$$\frac{m_1}{m_2} = \frac{\rho_1 / E_1^{1/2}}{\rho_2 / E_2^{1/2}}$$

## Worked example

**Given:** A square-section beam of length $L$ must have a fixed bending stiffness. Two candidates are 6061-T6 aluminum ($\rho = 2.70$ g/cm$^3$, $E = 69$ GPa) and 1018 steel ($\rho = 7.87$ g/cm$^3$, $E = 205$ GPa).

**Find:** The mass of the aluminum beam as a fraction of the steel beam, at the same stiffness and length.

**Assumptions:** The beam is stiffness limited, not strength limited. Both beams have the same length and load case. The cross-section is square, and only the side length changes.

**Solution:**

1. Aluminum index: $\rho_{Al} / E_{Al}^{1/2} = 2.70 / \sqrt{69} = 2.70 / 8.307 = 0.3250$.
2. Steel index: $\rho_{s} / E_{s}^{1/2} = 7.87 / \sqrt{205} = 7.87 / 14.318 = 0.5496$.
3. Ratio: $m_{Al}/m_{s} = 0.3250 / 0.5496 = 0.591$.

**Answer:** The aluminum beam has about 59 percent of the steel beam's mass. It needs a larger cross-section to match stiffness, but the lower density more than makes up for it.

**Sanity check:** The ratio of the two indices is $1.82 / 3.08 \approx 0.59$, which matches the mass ratio. Also, the same stiffness with a tie instead of a beam gives a mass ratio near 1.0 (since $E/\rho$ is nearly equal for steel and aluminum). That shows why the choice of index matters.

## Practice

1. Compute $E/\rho$ for ABS. Use the values in the table.
2. For a stiffness-limited tie, which is higher, $E/\rho$ for 1018 steel or for Ti-6Al-4V?
3. For a stiffness-limited square beam, find the mass ratio of Ti-6Al-4V to 1018 steel at the same stiffness and length. Use $\rho/E^{1/2}$.
4. For a strength-limited tie, which has the higher $\sigma_y/\rho$, 6061-T6 aluminum or 1018 steel?
5. Glass has the highest stiff-beam index in the table. Give one reason it may still be a poor choice for a beam.

<details><summary>Answers</summary>

1. about 2.2 (GPa per g/cm$^3$)
2. 1018 steel (26.0, against 25.7 for Ti-6Al-4V)
3. about 0.75
4. 6061-T6 aluminum (102.2, against 47.0 for steel)
5. Glass is brittle with no yield point, so it fails suddenly under flaws and cannot carry impact or bending loads safely.

</details>

## Common mistakes

- Choosing by one property alone. Stiffness, strength, toughness, cost, and corrosion all matter.
- Using the wrong index for the constraint. A stiffness-limited part and a strength-limited part can rank materials differently.
- Forgetting the square-section assumption. The beam index $E^{1/2}/\rho$ changes for round tubes and I-beams.
- Treating table values as design values. Use supplier data, and check temperature and environment.
- Ignoring the brittle materials' fracture data. A high index means nothing if the part can crack under the design load.

## Go deeper

- [Mechanics of Materials](https://ocw.mit.edu/courses/3-11-mechanics-of-materials-fall-1999/) by MIT OpenCourseWare: the mechanical properties that feed the performance indices.
- [Fundamentals of Materials Science](https://ocw.mit.edu/courses/3-012-fundamentals-of-materials-science-fall-2005/) by MIT OpenCourseWare: how structure and bonding set the properties in the table.
- [Materials Laboratory](https://ocw.mit.edu/courses/3-014-materials-laboratory-fall-2006/) by MIT OpenCourseWare: how the property data in a selection study are measured.
