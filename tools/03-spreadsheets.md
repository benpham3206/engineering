# Spreadsheets for engineering

**Type:** lesson

A **spreadsheet** is a grid of cells where formulas update when inputs change. Engineers use it for tables, quick sweeps, unit checks, and records. It is the fastest tool for "what if" questions, and the easiest to get wrong without labels.

**Prerequisites:** [Algebra](../math/01-algebra.md) and [Axial and torsion](../physics/04-axial-and-torsion.md) (for the stress example). [Python](02-python.md) is useful but not required.
**Time:** 6-10 h to learn the parts used here

## Core ideas

- A **cell** has an address such as `B3`. A **formula** starts with `=`, for example `=B2*C2`.
- Use **absolute references** (`$B$2`) for constants that must not shift when you copy a formula.
- Keep **inputs** in one labeled block and **outputs** in another. Never type a number inside a formula.
- Put units in the header, for example `Stress (MPa)`. The sheet will not check them for you.
- Use **named cells** for key constants such as density or yield strength. A formula with a name is easier to audit.
- Use a **table** or a **data sweep** to vary one input and see the result in a column.

Free options: LibreOffice Calc, Google Sheets, or the spreadsheet in any free office suite. The same formulas work in each.

For the same job in code, see the [Python lesson](02-python.md).

## Key equations

Axial stress in a round rod under tensile force $F$ (N) with diameter $d$ (m):

$$\sigma = \frac{F}{A}, \qquad A = \frac{\pi d^2}{4}$$

Here $\sigma$ is stress in pascals (Pa), and $A$ is cross-sectional area in m$^2$. In a sheet, write the diameter in mm and convert in the formula with a units cell.

## Worked example

**Given:** A 12 kN tensile load on round steel rods. Candidate diameters are 8, 10, 12, and 14 mm.

**Find:** The axial stress for each diameter, in MPa.

**Assumptions:** Uniform stress over the cross-section, no bending, no stress concentrations.

**Layout:**

| | A | B | C |
|---|---|---|---|
| 1 | Diameter (mm) | Area (mm$^2$) | Stress (MPa) |
| 2 | 8 | `=PI()*A2^2/4` | `=12000/B2` |
| 3 | 10 | `=PI()*A3^2/4` | `=12000/B3` |
| 4 | 12 | `=PI()*A4^2/4` | `=12000/B4` |
| 5 | 14 | `=PI()*A5^2/4` | `=12000/B5` |

Because the area is in mm$^2$ and the force is in N, the result of $F/A$ is in MPa. This matches what the cell formulas compute.

Running the same formula in Python gives these stresses:

```
d = 8 mm   sigma = 238.73 MPa
d = 10 mm  sigma = 152.79 MPa
d = 12 mm  sigma = 106.10 MPa
d = 14 mm  sigma = 77.95 MPa
```

**Answer:** 239, 153, 106, and 78 MPa for 8, 10, 12, and 14 mm.

**Sanity check:** Doubling the diameter quadruples the area. Going from 8 mm to 12 mm multiplies area by $(12/8)^2 = 2.25$, and $238.7 / 2.25 = 106.1$ MPa, which matches.

## Practice

1. Add a row for 16 mm. Estimate its stress with the same formula. Then check your value by hand.
2. Change the load to 15 kN. Which cell do you edit, and which outputs change?
3. Make a column that divides each stress by a yield strength of 250 MPa. Label the column clearly.
4. Sort the table by stress. Does the sort move the formulas correctly? Check one row.
5. Which diameter first gives a stress below 150 MPa?

<details><summary>Answers</summary>

1. About 59.7 MPa at 16 mm (area 201.1 mm$^2$).
2. The load cell. Every stress cell changes.
3. Values: 0.95, 0.61, 0.42, 0.31 (ratios for 8 to 14 mm).
4. Answers will vary. Check that the formulas still point to the same row.
5. 12 mm (106.1 MPa). The 10 mm rod gives 152.8 MPa, which is just above 150.

</details>

## Common mistakes

- Typing numbers into formulas. Put every constant in a labeled cell.
- Forgetting to lock a constant with `$`. Copying a formula then moves the reference.
- Mixing mm and m in one column. Choose one unit per column and say so in the header.
- Sorting only one column. This breaks the row link between inputs and outputs.
- Treating a spreadsheet result as checked because it looks neat. Check at least one row by hand.

## Go deeper

- [SciPy User Guide](https://docs.scipy.org/doc/scipy/tutorial/index.html) by the SciPy project: the code route for the same table-style calculations.
- [Paul's Online Math Notes, Algebra](https://tutorial.math.lamar.edu/Classes/Alg/Alg.aspx) by Paul Dawkins, Lamar University: the rules for solving formulas that your sheet computes.
- Related: [Python](02-python.md), [GNU Octave and MATLAB](04-matlab.md), [starter kit](01-starter-kit.md).
- [Tools reference](reference.md): the lookup sheet for this topic.
