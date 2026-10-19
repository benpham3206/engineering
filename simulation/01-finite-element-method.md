# Finite element method

**Type:** lesson
**Verify:** strict

The finite element method (FEM), used in finite element analysis (FEA), is a numerical way to solve the partial differential equations of a real part by cutting it into many small simple pieces and solving a large set of linear equations. Engineers use it because most real shapes, loads, and materials have no closed-form solution, and because it predicts stress, deflection, temperature, and vibration before anything is built. A result is only worth the checks behind it, so this lesson teaches the method by hand on a bar small enough to verify exactly.

**Prerequisites:** [Differential equations](../math/06-differential-equations.md), [Linear algebra](../math/05-linear-algebra.md), [Partial differential equations and Fourier series](../math/10-pdes-and-fourier-series.md), [Axial and torsion](../physics/04-axial-and-torsion.md), [Heat transfer](../physics/12-heat-transfer.md)
**Time:** 8-12 h

## Core ideas

- A **finite element** is a small region of the body, such as a line segment, triangle, or brick, over which the unknown is assumed to follow a simple shape. A **node** is a point where elements meet and where the unknown is stored. A **mesh** is the full set of elements and nodes covering the body.
- The unknowns are the **degrees of freedom (DOF)**: the independent values the solver finds, such as the axial displacement at a node of a bar, or the temperature at a node in a heat problem.
- FEM does not solve the governing equation exactly everywhere. It finds the node values that make the model's total potential energy a minimum among all shapes the elements can represent. For a solid, that energy is the strain energy stored in the material minus the work done by the loads.
- Each element contributes a **stiffness matrix** $\mathbf{k}$ that relates its nodal forces to its nodal displacements. **Assembly** adds all element matrices into one **global stiffness matrix** $\mathbf{K}$, so that $\mathbf{K}\mathbf{d} = \mathbf{F}$ with $\mathbf{d}$ the vector of nodal displacements and $\mathbf{F}$ the vector of nodal loads.
- **Boundary conditions** remove the rigid-body motion. Without them, $\mathbf{K}$ is singular (it has no inverse) because the whole body could slide with no strain. Fixing a DOF removes its row and column from the system.
- The same recipe covers other physics. For heat conduction, the unknown is temperature, the element matrix involves conductivity, and the equation is the heat equation from the [PDE lesson](../math/10-pdes-and-fourier-series.md). Only the matrices change.
- The steps are: define the geometry, material, loads, and constraints; mesh; compute and assemble the element matrices; apply boundary conditions; solve; compute strains and stresses from the displacements; then check.

### Shape functions

A **shape function** $N_i(x)$ is a function that equals 1 at node $i$, equals 0 at every other node, and is used to interpolate the unknown inside the element: $u(x) = \sum N_i(x)\,u_i$. For a two-node bar element of length $l$ the shape functions are straight lines. A three-node element uses parabolas and can follow curvature, at the cost of an extra node. Higher-order elements converge faster per node but cost more to assemble.

### Mesh convergence

As elements get smaller (smaller size $h$), the computed answer approaches the exact solution of the underlying mathematical model, provided the elements can represent constant strain and rigid motion. For linear elements, displacement error typically falls as $h^2$ and stress error as $h$. **Mesh convergence** is the practice of solving on two or more meshes and confirming that the quantity of interest stops changing. If it keeps changing, the mesh is too coarse.

Convergence has limits. Stress at a **singularity**, such as a sharp inside corner or a point load, is infinite in the mathematical model. Refining the mesh makes the computed stress grow without end, so convergence never arrives. The model, not the mesh, must change: add a realistic fillet radius, spread the load over a contact area, or read stress away from the corner.

### Verification against hand calculations

**Verification** asks whether the equations were solved correctly. **Validation** asks whether the equations describe the real thing, and needs test data. These verification checks can be run by hand:

- Reactions sum to the applied loads, in every direction.
- The total strain energy equals half the work of the loads, for a linear problem.
- A simplified hand model (a bar, a beam, a stress concentration factor) agrees within a reasonable margin. When it does not, find out which one is wrong before using either.
- Displacements are the right order of magnitude and the deformed shape moves the right way.
- Refining the mesh changes the answer by less than the accuracy needed.

## Key equations

Symbols: $E$ = Young's modulus (Pa); $A$ = cross-section area ($\text{m}^2$); $l$ = element length (m); $x$ = position along the element (m); $u$ = axial displacement (m); $u_1, u_2$ = nodal displacements (m); $\varepsilon$ = strain (dimensionless); $\sigma$ = stress (Pa); $k$ = element stiffness (N/m); $F_1, F_2$ = nodal forces (N).

Linear shape functions for a two-node bar element, $0 \le x \le l$:

$$
N_1(x) = 1 - \frac{x}{l}, \qquad N_2(x) = \frac{x}{l}, \qquad u(x) = N_1 u_1 + N_2 u_2
$$

Strain is the slope of $u$, constant in the element:

$$
\varepsilon = \frac{du}{dx} = \frac{u_2 - u_1}{l}, \qquad \sigma = E\,\varepsilon
$$

Strain energy of the element is $\tfrac{1}{2} E A l\,\varepsilon^2 = \tfrac{1}{2} \dfrac{EA}{l}(u_2 - u_1)^2$. Setting its derivatives with respect to $u_1$ and $u_2$ equal to the nodal forces gives the element equation:

$$
\frac{EA}{l}\begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix}\begin{bmatrix} u_1 \\ u_2 \end{bmatrix} = \begin{bmatrix} F_1 \\ F_2 \end{bmatrix}, \qquad k = \frac{EA}{l}
$$

The bar element holds for linear elastic material, small strain, and load along the axis. It breaks when the bar buckles under compression, bends, yields, or has a cross section that changes sharply inside one element. Assembly for a chain of elements adds each element's $2 \times 2$ matrix into the rows and columns of its two nodes, so neighbors share a node's stiffness. Solving $\mathbf{K}\mathbf{d} = \mathbf{F}$ after applying the constraints gives the displacements.

## Worked example

**Two-element stepped bar.** A steel bar is fixed at its left end. The first element is 1.0 m long with area 200 $\text{mm}^2$. The second is 1.0 m long with area 100 $\text{mm}^2$. A 10 kN axial load pulls on the free end. Find the nodal displacements, the reaction, and the stress in each element, and compare with the exact answer.

**Given:** $E = 200$ GPa, $l_1 = l_2 = 1.0$ m, $A_1 = 200$ $\text{mm}^2$, $A_2 = 100$ $\text{mm}^2$, $P = 10$ kN. Nodes 1, 2, 3 from left to right.

**Find:** $u_2$, $u_3$, the reaction at node 1, $\sigma_1$, $\sigma_2$.

**Assumptions:** linear elastic, small displacement, load along the axis, no buckling, uniform properties inside each element.

**Solution:**

1. Element stiffnesses: $k_1 = E A_1/l_1 = 40$ MN/m and $k_2 = E A_2/l_2 = 20$ MN/m.
2. Assemble. Element 1 acts on DOF 1 and 2, element 2 on DOF 2 and 3, so the shared node carries both:

$$
\begin{bmatrix} k_1 & -k_1 & 0 \\ -k_1 & k_1 + k_2 & -k_2 \\ 0 & -k_2 & k_2 \end{bmatrix}\begin{bmatrix} u_1 \\ u_2 \\ u_3 \end{bmatrix} = \begin{bmatrix} R_1 \\ 0 \\ P \end{bmatrix}
$$

3. Boundary condition $u_1 = 0$: delete row 1 and column 1. What remains is a $2\times 2$ system:

$$
\begin{bmatrix} k_1 + k_2 & -k_2 \\ -k_2 & k_2 \end{bmatrix}\begin{bmatrix} u_2 \\ u_3 \end{bmatrix} = \begin{bmatrix} 0 \\ P \end{bmatrix}
$$

4. Its determinant is $k_1 k_2$. By Cramer's rule, $u_2 = P/k_1 = 0.250$ mm and $u_3 = P(k_1 + k_2)/(k_1 k_2) = 0.750$ mm.
5. Reaction from the deleted row: $R_1 = -k_1 u_2$, which has magnitude 10 kN and opposes the load.
6. Stresses: $\sigma_1 = E(u_2 - u_1)/l_1 = 50$ MPa and $\sigma_2 = E(u_3 - u_2)/l_2 = 100$ MPa.

**Exact answer:** by statics the force is 10 kN everywhere, so $\sigma_1 = P/A_1 = 50$ MPa and $\sigma_2 = P/A_2 = 100$ MPa. The tip movement is the integral of $P/(EA)$ along the bar, 0.750 mm.

**Answer:** $u_2 = 0.250$ mm, $u_3 = 0.750$ mm, reaction 10 kN toward the wall, $\sigma_1 = 50$ MPa, $\sigma_2 = 100$ MPa. These match the exact values because the true displacement is linear inside each element, which is exactly what the shape functions represent.

**Sanity check:** the work of the load, $\tfrac{1}{2} P u_3 = 3.75$ J, equals the strain energy stored in the two elements, $\tfrac{1}{2} k_1 u_2^2 + \tfrac{1}{2} k_2 (u_3 - u_2)^2 = 3.75$ J. The thinner element has half the area and carries the same force, so it sees twice the stress.

<details><summary>Verification</summary>

```verify
E = q(200, "GPa")
l = q(1.0, "m")
A1 = q(200, "mm^2")
A2 = q(100, "mm^2")
P = q(10, "kN")
k1 = E * A1 / l
k2 = E * A2 / l
expect(k1, "40 MN/m")
expect(k2, "20 MN/m")
det = k1 * k2
u2 = (k2 * P) / det
u3 = ((k1 + k2) * P) / det
expect(u2, "0.250 mm")
expect(u3, "0.750 mm")
expect(k1 * u2, "10 kN")
s1 = E * u2 / l
s2 = E * (u3 - u2) / l
expect(s1, "50 MPa")
expect(s2, "100 MPa")
expect(P / A1, "50 MPa")
expect(P / A2, "100 MPa")
expect(0.5 * P * u3, "3.75 J")
expect(0.5 * k1 * u2**2 + 0.5 * k2 * (u3 - u2)**2, "3.75 J")
```

</details>

## Practice

1. Find the stiffness $k = EA/l$ of one bar element with $E = 70$ GPa, $A = 300$ $\text{mm}^2$, and $l = 0.50$ m, in MN/m.
2. A single bar element of length 1.5 m, area 100 $\text{mm}^2$, and $E = 200$ GPa carries a 20 kN end pull, fixed at the other end. Find the tip displacement in mm.
3. A bar of length $L$, fixed at one end, carries a uniform axial load along its length. It is modeled with 2 equal linear elements and consistent nodal loads. The stress in the element at the fixed end is constant. As a fraction of the exact stress at the fixed end, what does the model report? (The exact stress there is the highest in the bar.)
4. For problem 3, the stress error at the fixed end, as a fraction of the exact value, is $1/(2n)$ for $n$ equal elements. How many elements give an error of at most 0.02?
5. An analyst's bracket model predicts a tip deflection of 12.0 mm. A hand beam calculation gives 10.0 mm. Decide where to look first, and find the percentage difference relative to the hand value.

<details><summary>Answers</summary>

1. 42 MN/m
2. 1.5 mm
3. 0.75 of the exact value (an error of 25 percent).
4. 25 elements.
5. 20 percent. The difference is too large to blame on mesh error alone. Check units, boundary conditions, and loads first, then refine the mesh and see whether the answer moves toward the hand value.

```verify
k = q(70, "GPa") * q(300, "mm^2") / q(0.50, "m")
expect(k, "42 MN/m", ans=1)
utip = q(20, "kN") * q(1.5, "m") / (q(200, "GPa") * q(100, "mm^2"))
expect(utip, "1.5 mm", ans=2)
n = 2
expect(1 - 1 / (2 * n), "0.75", ans=3)
expect(1 / (2 * 0.02), "25", ans=4)
expect((q(12.0, "mm") - q(10.0, "mm")) / q(10.0, "mm") * 100, "20", ans=5)
```

</details>

## Common mistakes

- Wrong or missing boundary conditions. Too few constraints leave a singular matrix or a body that drifts. Too many, such as fixing a face that is free to expand, add false stress. Check the reactions against the applied loads.
- Trusting a stress at a sharp corner or under a point load. The mathematical value is infinite, so the number shown depends on the element size and carries no meaning. Read stress away from the singularity, or model the real fillet or contact patch.
- Trusting a color plot. Contours are smoothed across elements, their scale is chosen by the software, and the deformed shape is usually magnified. Look at the legend limits, the unaveraged element stress, and the real deflection.
- Skipping the mesh check. One mesh gives one answer and no way to know whether it is converged.
- Mixing units, for example millimeters for length and meters for area, or MPa with N and m. State one consistent set before building the model.

## Go deeper

- [Finite Element Analysis of Solids and Fluids I (2.092)](https://ocw.mit.edu/courses/2-092-finite-element-analysis-of-solids-and-fluids-i-fall-2009/) by MIT OpenCourseWare: a full undergraduate course on the method.
- [Linear Partial Differential Equations: Analysis and Numerics (18.303)](https://ocw.mit.edu/courses/18-303-linear-partial-differential-equations-analysis-and-numerics-fall-2014/) by MIT OpenCourseWare: the mathematics behind approximating PDEs.
- [Differential Equations (18.03SC)](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/) by MIT OpenCourseWare: the ordinary-equation background.
- [Mechanics reference](../physics/reference-mechanics.md) and [Math reference](../math/reference.md): the hand-calculation formulas to check a model against.
- Related: [Axial and torsion](../physics/04-axial-and-torsion.md), [Heat transfer](../physics/12-heat-transfer.md).
- Reference sheets for FEA, CFD, and verification and validation are planned.
