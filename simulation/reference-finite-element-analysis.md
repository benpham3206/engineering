# Finite element analysis reference

**Type:** reference
**Verify:** strict

Lookup sheet for the formulation of the finite element method: weak forms, shape functions, element matrices, integration, assembly, boundary conditions, time stepping, error rates, locking, and result recovery, for an engineer who builds, reads, or checks a finite element model.

## Principles

- A finite element model solves an approximate problem exactly. The unknown is restricted to the shapes the elements can represent, and the solver finds the best member of that set in an energy sense.
- For a force-loaded displacement-based model of a linear elastic body with zero prescribed displacements, conforming elements, and exact integration, the computed strain energy never exceeds the exact value, so the model is on average too stiff, never too soft.
- Convergence needs two properties. An element must reproduce rigid-body motion and constant strain (completeness), and displacement must be continuous across element edges (compatibility). The patch test checks both.
- Equilibrium holds in a weighted-average sense, not point by point. Stress is discontinuous between elements, and the size of the jump measures the local error.
- Displacements converge faster than stresses. A displacement that looks right does not prove the stress is right.
- Boundary conditions decide the answer as much as the mesh does. A missing constraint gives a singular matrix; an extra constraint adds false stress.
- A point load, a sharp re-entrant corner, or a crack tip has infinite stress in the mathematical model. Refining the mesh there changes the model's output without converging, so change the model, not the mesh.
- Reactions must balance the applied loads in every direction. This check costs nothing and catches wrong constraints, wrong units, and wrong loads.
- Verification asks whether the equations were solved correctly. Validation asks whether the equations describe the part. Neither replaces the other; see [Verification and validation reference](reference-verification-validation.md).
- A linear solution holds only while displacements are small, strains stay in the elastic range, and contact status does not change.

## Strong and weak forms

The **strong form** is the differential equation that must hold at every point of the body. The **weak form** is the same statement multiplied by an arbitrary test function and integrated once by parts. It needs only first derivatives of the unknown and is the equation that finite elements discretize.

For an axial bar of length $L$ with fixed end at $x = 0$, end load $P$ at $x = L$, and distributed axial load $b$:

$$\frac{d}{dx}\left(E A \frac{du}{dx}\right) + b = 0, \qquad u(0) = 0, \qquad E A \frac{du}{dx}\Big|_{x=L} = P$$

$$\int_0^L E A \frac{du}{dx}\frac{dv}{dx}\,dx = \int_0^L b\,v\,dx + P\,v(L) \quad \text{for every } v \text{ with } v(0) = 0$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $u$ | axial displacement | m |
| $v$ | test function (virtual displacement) | m |
| $x$ | axial coordinate | m |
| $L$ | bar length | m |
| $E$ | Young's modulus | Pa |
| $A$ | cross-section area | $\text{m}^{2}$ |
| $b$ | distributed axial load per unit length | N/m |
| $P$ | end load | N |

Holds when: material is linear elastic, strains are small, and load acts along the axis.
Breaks when: the bar buckles, bends, yields, or has a section that changes abruptly (use a continuum or beam model).
Source and basis: derived from equilibrium of a bar element and integration by parts; taught in [Finite element method](01-finite-element-method.md) and [Axial and torsion](../physics/04-axial-and-torsion.md).

Essential (displacement) conditions are imposed on $u$ and $v$. Natural (force) conditions, such as the end load, appear in the weak form and need no special treatment.

Example. $E = 200\ \text{GPa}$, $A = 100\ \text{mm}^2$, $L = 2\ \text{m}$, $P = 10\ \text{kN}$, $b = 1\ \text{kN/m}$. Integrating the strong form gives a tip displacement $u(L) = P L/(E A) + b L^2/(2 E A)$. The end load contributes 1.000 mm and the distributed load 0.100 mm, so the tip moves 1.100 mm.

```verify
E = q(200, "GPa")
A = q(100, "mm^2")
L = q(2, "m")
P = q(10, "kN")
b = q(1, "kN/m")
u_P = P * L / (E * A)
u_b = b * L**2 / (2 * E * A)
expect(u_P, "1.000 mm")
expect(u_b, "0.100 mm")
expect(u_P + u_b, "1.100 mm")
```

## Virtual work and minimum potential energy

The **principle of virtual work** says a body is in equilibrium if the internal virtual work equals the external virtual work for every admissible virtual displacement. For linear elasticity it is equivalent to the **principle of minimum potential energy**: of all admissible displacements, the true one minimizes the total potential energy $\Pi$. Substituting $u = \sum N_i d_i$ turns that minimization into a matrix equation.

$$\Pi(\mathbf{d}) = \tfrac{1}{2}\,\mathbf{d}^{\mathsf{T}} \mathbf{K}\, \mathbf{d} - \mathbf{d}^{\mathsf{T}} \mathbf{f}, \qquad \frac{\partial \Pi}{\partial \mathbf{d}} = \mathbf{K}\,\mathbf{d} - \mathbf{f} = \mathbf{0}$$

$$\Pi_{\text{min}} = -\tfrac{1}{2}\,\mathbf{d}^{\mathsf{T}} \mathbf{f} = -U$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\Pi$ | total potential energy | J |
| $U$ | strain energy stored at the solution | J |
| $\mathbf{d}$ | vector of nodal displacements | m |
| $\mathbf{K}$ | global stiffness matrix | N/m |
| $\mathbf{f}$ | vector of nodal forces | N |

Holds when: the response is linear, loads do not depend on the deformation, and $\mathbf{K}$ is positive definite after constraints.
Breaks when: the response is nonlinear (follower loads, contact, plasticity), where $\Pi$ is not quadratic, or the constraints leave rigid-body motion so $\mathbf{K}$ is singular.
Source and basis: derived from the principle of virtual work; taught in [Finite element method](01-finite-element-method.md).

Consequence. For force-loaded models with zero prescribed displacements, the strain energy of a conforming model rises toward the exact value as the mesh is refined, so $U$ is a convergence monitor that cannot overshoot. With prescribed nonzero displacements and no applied forces, the model can instead converge from above.

Example. One bar element, $E = 200\ \text{GPa}$, $A = 100\ \text{mm}^2$, $l = 1\ \text{m}$, fixed at one end with a 10 kN end pull. The stiffness is $k = E A/l$ and the tip moves $d = P/k$. The stiffness is 20 MN/m and the tip moves 0.500 mm. Then $U = \tfrac{1}{2} P d = 2.50\ \text{J}$ and $\Pi_{\text{min}} = -2.50\ \text{J}$.

```verify
E = q(200, "GPa")
A = q(100, "mm^2")
l = q(1, "m")
P = q(10, "kN")
k = E * A / l
expect(k, "20 MN/m")
d = P / k
expect(d, "0.500 mm")
U = 0.5 * P * d
expect(U, "2.50 J")
expect(0.5 * k * d**2 - P * d, "-2.50 J")
```

## Shape functions

A **shape function** $N_i$ is the interpolation function of node $i$. It equals 1 at node $i$, 0 at every other node, and the shape functions of an element sum to 1 everywhere (the partition of unity), which makes rigid-body motion exact. The unknown inside the element is $u = \sum N_i u_i$.

### One-dimensional elements

On the natural coordinate $\xi$ with $-1 \le \xi \le 1$, the two-node (linear) and three-node (quadratic, midside node at $\xi = 0$) functions are:

$$N_1 = \frac{1 - \xi}{2}, \quad N_2 = \frac{1 + \xi}{2}$$

$$N_1 = \frac{\xi(\xi - 1)}{2}, \quad N_2 = 1 - \xi^2, \quad N_3 = \frac{\xi(\xi + 1)}{2}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\xi$ | natural coordinate of the element | dimensionless |
| $N_1$, $N_2$, $N_3$ | shape function of node 1, 2, 3 | dimensionless |

Holds when: the element is a straight line segment and the unknown is a scalar or one displacement component.
Breaks when: the element is strongly curved or distorted (the mapping becomes singular), or the unknown has a jump inside the element.
Source and basis: derived from the conditions $N_i(\xi_j) = \delta_{ij}$ and $\sum N_i = 1$; taught in [Finite element method](01-finite-element-method.md).

The linear element represents a constant strain. The quadratic element represents a linear strain, so it follows bending of a bar-like field with fewer elements.

Example at $\xi = 0.5$. Linear: $N_1 = 0.25$, $N_2 = 0.75$. Quadratic: $N_1 = -0.125$, $N_2 = 0.75$, $N_3 = 0.375$, which sum to 1.

```verify
xi = q(0.5, "")
expect((1 - xi) / 2, "0.25")
expect((1 + xi) / 2, "0.75")
n1 = xi * (xi - 1) / 2
n2 = 1 - xi**2
n3 = xi * (xi + 1) / 2
expect(n1, "-0.125")
expect(n2, "0.75")
expect(n3, "0.375")
expect(n1 + n2 + n3, "1")
```

### Linear triangle

The three-node triangle has linear shape functions in physical coordinates. With nodes $(x_i, y_i)$ numbered counterclockwise and $i, j, k$ cycling through 1, 2, 3:

$$N_i = \frac{a_i + b_i x + c_i y}{2A_e}, \quad a_i = x_j y_k - x_k y_j, \quad b_i = y_j - y_k, \quad c_i = x_k - x_j$$

$$2 A_e = x_1(y_2 - y_3) + x_2(y_3 - y_1) + x_3(y_1 - y_2)$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $N_i$ | shape function of node $i$ | dimensionless |
| $x$, $y$ | point coordinates | m |
| $x_i$, $y_i$ | nodal coordinates | m |
| $a_i$ | constant term of the numerator | $\text{m}^{2}$ |
| $b_i$, $c_i$ | coordinate-difference coefficients | m |
| $A_e$ | element area | $\text{m}^{2}$ |

Holds when: the nodes are ordered counterclockwise (so $A_e > 0$) and the element is not degenerate.
Breaks when: the triangle is very thin or has an angle near 180 degrees, where accuracy collapses.
Source and basis: derived from solving $N_i(x_j, y_j) = \delta_{ij}$ for a linear polynomial.

The strain in this element is constant, so it is called the constant-strain triangle. Example. Nodes $(0, 0)$, $(4, 0)$, $(0, 3)$ m give $2 A_e = 12\ \text{m}^2$, so $A_e = 6\ \text{m}^2$. At the centroid $(4/3, 1)$ m, each $N_i$ is 0.333.

```verify
x1 = q(0, "m")
y1 = q(0, "m")
x2 = q(4, "m")
y2 = q(0, "m")
x3 = q(0, "m")
y3 = q(3, "m")
twoA = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
expect(twoA, "12 m^2")
xc = (x1 + x2 + x3) / 3
yc = (y1 + y2 + y3) / 3
a1 = x2 * y3 - x3 * y2
b1 = y2 - y3
c1 = x3 - x2
expect((a1 + b1 * xc + c1 * yc) / twoA, "0.333")
```

### Bilinear quadrilateral and isoparametric mapping

An **isoparametric** element uses the same shape functions for the geometry and for the unknown. The four-node quadrilateral lives on the square $-1 \le \xi, \eta \le 1$ with corner coordinates $(-1,-1)$, $(1,-1)$, $(1,1)$, and $(-1,1)$ in counterclockwise order, and maps to the physical element by interpolating its corner coordinates.

$$N_i = \frac{(1 + \xi_i \xi)(1 + \eta_i \eta)}{4}, \qquad x = \sum N_i x_i, \quad y = \sum N_i y_i$$

$$\mathbf{J} = \begin{bmatrix} \partial x/\partial \xi & \partial y/\partial \xi \\ \partial x/\partial \eta & \partial y/\partial \eta \end{bmatrix}, \qquad dA = \det \mathbf{J}\; d\xi\, d\eta, \qquad \begin{bmatrix} \partial N_i/\partial x \\ \partial N_i/\partial y \end{bmatrix} = \mathbf{J}^{-1} \begin{bmatrix} \partial N_i/\partial \xi \\ \partial N_i/\partial \eta \end{bmatrix}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\xi$, $\eta$ | natural coordinates | dimensionless |
| $\xi_i$, $\eta_i$ | natural coordinates of node $i$ | dimensionless |
| $N_i$ | shape function of node $i$ | dimensionless |
| $x_i$, $y_i$ | physical coordinates of node $i$ | m |
| $\mathbf{J}$ | Jacobian matrix of the mapping | m |
| $\det \mathbf{J}$ | area scale factor, physical area per natural area | $\text{m}^{2}$ |

Holds when: the quadrilateral is convex, so $\det \mathbf{J} > 0$ at every integration point.
Breaks when: the element is concave or badly warped, so $\det \mathbf{J} \le 0$ somewhere; the element then inverts and the stiffness is meaningless. A non-parallelogram shape also loses accuracy because the polynomial in $(x, y)$ is no longer complete.
Source and basis: derived from the chain rule applied to the mapping $(\xi, \eta) \to (x, y)$.

For a rectangle with sides $a$ and $c$, $\det \mathbf{J} = a c/4$ everywhere, which is the area divided by 4 (the area of the natural square). Example. Rectangle corners $(0, 0)$, $(4, 0)$, $(4, 2)$, $(0, 2)$ m. At $(\xi, \eta) = (0.5, -0.5)$ the weights are $N_1 = 0.1875$, $N_2 = 0.5625$, $N_3 = 0.1875$, $N_4 = 0.0625$. The point maps to $(3, 0.5)$ m, and $\det \mathbf{J} = 2\ \text{m}^2$.

```verify
xi = q(0.5, "")
eta = q(-0.5, "")
n1 = (1 - xi) * (1 - eta) / 4
n2 = (1 + xi) * (1 - eta) / 4
n3 = (1 + xi) * (1 + eta) / 4
n4 = (1 - xi) * (1 + eta) / 4
expect(n1, "0.1875")
expect(n2, "0.5625")
expect(n3, "0.1875")
expect(n4, "0.0625")
w = q(4, "m")
h = q(2, "m")
expect(w * (n2 + n3), "3 m")
expect(h * (n3 + n4), "0.5 m")
expect(w * h / 4, "2 m^2")
```

## Element matrices and vectors

### Bar element

A bar element with nodes 1 and 2, length $l$, carries axial force only. Its stiffness, consistent mass, lumped mass, and consistent load for a uniform axial load $b$ (force per length) are:

$$\mathbf{k}_e = \frac{E A}{l}\begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix}, \quad \mathbf{m}_e = \frac{\rho A l}{6}\begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}, \quad \mathbf{m}_{e,\text{lump}} = \frac{\rho A l}{2}\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}, \quad \mathbf{f}_e = \frac{b\, l}{2}\begin{bmatrix} 1 \\ 1 \end{bmatrix}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\mathbf{k}_e$ | element stiffness matrix | N/m |
| $\mathbf{m}_e$ | consistent element mass matrix | kg |
| $\mathbf{m}_{e,\text{lump}}$ | lumped element mass matrix | kg |
| $\mathbf{f}_e$ | consistent nodal load vector | N |
| $E$ | Young's modulus | Pa |
| $A$ | cross-section area | $\text{m}^{2}$ |
| $l$ | element length | m |
| $\rho$ | density | $\text{kg/m}^{3}$ |
| $b$ | uniform axial load per unit length | N/m |

Holds when: $E$, $A$, $\rho$ are constant over the element and the load acts along the axis.
Breaks when: properties vary along the element (integrate numerically), or bending or torsion matters (use a beam element).
Source and basis: derived by substituting the linear shape functions into the energy and kinetic energy integrals; taught in [Finite element method](01-finite-element-method.md).

Both mass matrices carry the full element mass $\rho A l$. Consistent mass comes from $\int \rho A N_i N_j\,dx$; lumping puts half of the mass on each node.

Example. $E = 200\ \text{GPa}$, $A = 100\ \text{mm}^2$, $l = 1\ \text{m}$, $b = 1\ \text{kN/m}$. The stiffness is 20 MN/m and each consistent nodal load is 0.5 kN.

```verify
E = q(200, "GPa")
A = q(100, "mm^2")
l = q(1, "m")
b = q(1, "kN/m")
expect(E * A / l, "20 MN/m")
expect(b * l / 2, "0.5 kN")
```

### Beam element

The Euler-Bernoulli beam element has two nodes with a transverse displacement $v$ and a rotation $\theta$ at each, in the order $(v_1, \theta_1, v_2, \theta_2)$. The shape functions are cubic, so the element is exact for end loads. With $I_A$ the second moment of area:

$$\mathbf{k}_e = \frac{E I_A}{l^3}\begin{bmatrix} 12 & 6l & -12 & 6l \\ 6l & 4l^2 & -6l & 2l^2 \\ -12 & -6l & 12 & -6l \\ 6l & 2l^2 & -6l & 4l^2 \end{bmatrix}, \qquad \mathbf{f}_e = \begin{bmatrix} w l/2 \\ w l^2/12 \\ w l/2 \\ -w l^2/12 \end{bmatrix}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\mathbf{k}_e$ | element stiffness matrix (mixed force and moment rows) | N/m |
| $\mathbf{f}_e$ | consistent load vector for uniform load (force and moment entries) | N |
| $E$ | Young's modulus | Pa |
| $I_A$ | second moment of area about the bending axis | $\text{m}^{4}$ |
| $l$ | element length | m |
| $w$ | uniform transverse load per unit length | N/m |

Holds when: the beam is slender (shear deformation negligible), the section is constant, deflections are small, and $w$ acts in the direction of $v$.
Breaks when: the beam is deep (span to depth below about 5 to 10; use a shear-deformable beam), the section tapers sharply, or deflection is large.
Source and basis: derived from cubic Hermite shape functions and the beam strain energy; the beam theory is taught in [Bending and buckling](../physics/05-bending-and-buckling.md).

Consistent mass for this element is $\dfrac{\rho A l}{420}$ times the matrix with rows $(156,\ 22l,\ 54,\ -13l)$, $(22l,\ 4l^2,\ 13l,\ -3l^2)$, $(54,\ 13l,\ 156,\ -22l)$, $(-13l,\ -3l^2,\ -22l,\ 4l^2)$. A lumped mass puts $\rho A l/2$ on each translation and little or nothing on the rotations.

Example. Cantilever, one element, fixed at node 1. $E = 200\ \text{GPa}$, $I_A = 100\ \text{cm}^4$, $l = 0.5\ \text{m}$. The free DOFs $(v_2, \theta_2)$ obey a 2 by 2 system. For a tip load $P = 1\ \text{kN}$ the solution is $v_2 = P l^3/(3 E I_A)$, which equals the exact beam result: $v_2 = 0.208\ \text{mm}$ and $\theta_2 = 0.625\ \text{mrad}$. For a uniform load $w = 2\ \text{kN/m}$ with the consistent vector above, $v_2 = w l^4/(8 E I_A)$, again exact at the node, 0.0781 mm.

```verify
E = q(200, "GPa")
I = q(100, "cm^4")
l = q(0.5, "m")
P = q(1, "kN")
c = E * I / l**3
a11 = 12 * c
a12 = -6 * l * c
a22 = 4 * l**2 * c
det = a11 * a22 - a12**2
v = (a22 * P) / det
th = (-a12 * P) / det
expect(v, "0.208 mm")
expect(P * l**3 / (3 * E * I), "0.208 mm")
expect(th, "0.625 mrad")
w = q(2, "kN/m")
f1 = w * l / 2
f2 = -w * l**2 / 12
vw = (a22 * f1 - a12 * f2) / det
expect(vw, "0.0781 mm")
expect(w * l**4 / (8 * E * I), "0.0781 mm")
```

### Plane stress triangle

The constant-strain triangle has two displacement DOFs per node, ordered $(u_1, v_1, u_2, v_2, u_3, v_3)$. With the strain vector $(\varepsilon_x, \varepsilon_y, \gamma_{xy})$, the strain-displacement matrix is constant and the stiffness follows from the energy:

$$\mathbf{B} = \frac{1}{2 A_e}\begin{bmatrix} b_1 & 0 & b_2 & 0 & b_3 & 0 \\ 0 & c_1 & 0 & c_2 & 0 & c_3 \\ c_1 & b_1 & c_2 & b_2 & c_3 & b_3 \end{bmatrix}, \quad \mathbf{D} = \frac{E}{1 - \nu^2}\begin{bmatrix} 1 & \nu & 0 \\ \nu & 1 & 0 \\ 0 & 0 & \dfrac{1 - \nu}{2} \end{bmatrix}, \quad \mathbf{k}_e = t\, A_e\, \mathbf{B}^{\mathsf{T}} \mathbf{D}\, \mathbf{B}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\mathbf{B}$ | strain-displacement matrix | 1/m |
| $\mathbf{D}$ | plane stress elasticity matrix | Pa |
| $\mathbf{k}_e$ | element stiffness matrix | N/m |
| $b_i$, $c_i$ | triangle coefficients from the shape functions | m |
| $A_e$ | element area | $\text{m}^{2}$ |
| $t$ | element thickness | m |
| $E$ | Young's modulus | Pa |
| $\nu$ | Poisson's ratio | dimensionless |

Holds when: the thickness is small and the stress through the thickness is zero (plane stress), the material is isotropic and linear, and $t$ is constant in the element.
Breaks when: the part is thick (use plane strain or a solid), or the stress varies sharply, because the triangle cannot bend and locks in bending-dominated fields. Use finer meshes or higher-order elements there.
Source and basis: derived from the triangle shape functions and the plane stress law; the stress-strain law is taught in [Axial and torsion](../physics/04-axial-and-torsion.md).

For plane strain the first row of $\mathbf{D}$ becomes $E/\left((1+\nu)(1-2\nu)\right)$ times $(1 - \nu,\ \nu,\ 0)$, the second $(\nu,\ 1-\nu,\ 0)$, and the third $(0,\ 0,\ (1-2\nu)/2)$.

Example. Triangle $(0,0)$, $(1,0)$, $(0,1)$ m, so $A_e = 0.5\ \text{m}^2$, $b = (-1, 1, 0)$ m, $c = (-1, 0, 1)$ m. With $E = 200\ \text{GPa}$, $\nu = 0.3$, $t = 10\ \text{mm}$. The displacement field $u = 10^{-3} x$, $v = 0$ gives $\varepsilon_x = 10^{-3}$, so $\sigma_x = E \varepsilon_x/(1 - \nu^2) = 219.8\ \text{MPa}$ and $\sigma_y = \nu \sigma_x = 65.9\ \text{MPa}$. The stiffness entry for $u_2$ against $u_2$ is $t A_e D_{11}$ times the square of the $u_2$ column of $\mathbf{B}$, which is $(1, 0, 0)^{\mathsf{T}}$ per metre, so it is 1099 MN/m.

```verify
E = q(200, "GPa")
nu = q(0.3, "")
t = q(10, "mm")
Ae = q(0.5, "m^2")
D11 = E / (1 - nu**2)
eps = q(1e-3, "")
sx = D11 * eps
expect(sx, "219.8 MPa")
expect(nu * sx, "65.9 MPa")
Bu = q(1, "1/m")
expect(t * Ae * Bu**2 * D11, "1099 MN/m")
```

## Numerical integration

Element integrals are evaluated by **Gauss quadrature**: a rule with $n$ points integrates every polynomial up to degree $2n - 1$ exactly on $[-1, 1]$.

$$\int_{-1}^{1} f(\xi)\,d\xi \approx \sum_{i=1}^{n} w_i\, f(\xi_i)$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $f$ | integrand in natural coordinates | dimensionless |
| $\xi_i$ | location of integration point $i$ | dimensionless |
| $w_i$ | weight of point $i$ | dimensionless |
| $n$ | number of integration points | dimensionless |

Holds when: the integrand is a polynomial of degree at most $2n - 1$, which holds for undistorted isoparametric elements. Points: $n = 1$ at $\xi = 0$ with $w = 2$; $n = 2$ at $\xi = \pm 1/\sqrt{3}$ with $w = 1$; $n = 3$ at $\xi = 0$ with $w = 8/9$ and at $\xi = \pm\sqrt{3/5}$ with $w = 5/9$.
Breaks when: the element is distorted so the integrand is rational (the rule is then only approximate), or the integrand is not smooth.
Source and basis: derived from requiring exactness for monomials up to degree $2n - 1$.

Full integration orders for typical elements (stiffness matrix, undistorted shape):

| Element | Full rule | Reduced rule | Note |
|---|---|---|---|
| 2-node bar | 1 point | none | integrand is constant |
| 3-node bar | 2 points | 1 point | reduced rule makes the matrix singular |
| 3-node triangle | 1 point | none | integrand is constant |
| 6-node triangle | 3 points (edge midpoints) | none | exact to degree 2 |
| 4-node quadrilateral | 2 by 2 | 1 by 1 | reduced rule allows hourglass modes |
| 8-node quadrilateral | 3 by 3 | 2 by 2 | reduced rule often usable |
| 8-node brick | 2 by 2 by 2 | 1 point | reduced rule allows hourglass modes |

**Hourglassing** is a spurious mode that produces no strain at the reduced-rule points, so the stiffness matrix sees no energy in it and the mesh can deform in a zigzag at no cost. A single-point 4-node quadrilateral has 8 DOFs, 3 rigid-body modes and 3 constant-strain modes, so $8 - 3 - 3 = 2$ hourglass modes remain, one per displacement component. Reduced integration also removes locking (see Element limitations and locking), which is why it is used with hourglass control.

Example. The quadratic bar stiffness entry $k_{11} = (2 E A/l)\int_{-1}^{1} (\xi - \tfrac{1}{2})^2\,d\xi$. The integrand has degree 2, so 2 points are exact: the sum is 1.167, giving $k_{11} = 7 E A/(3l)$. With $E A/l = 20\ \text{MN/m}$ that is 46.7 MN/m. One point at $\xi = 0$ gives 0.5 for the integral, which is wrong.

```verify
g = 1 / sqrt(3)
s = (g - 0.5)**2 + (-g - 0.5)**2
expect(s, "1.167")
EAl = q(20, "MN/m")
expect(2 * EAl * s, "46.7 MN/m")
expect(2 * (0 - 0.5)**2, "0.5")
```

## Assembly

**Assembly** adds each element matrix into the global matrix at the rows and columns given by its global DOF numbers. Equivalently, with $\mathbf{L}_e$ a Boolean matrix that picks the element DOFs out of the global vector:

$$\mathbf{K} = \sum_{e} \mathbf{L}_e^{\mathsf{T}}\, \mathbf{k}_e\, \mathbf{L}_e, \qquad \mathbf{f} = \sum_{e} \mathbf{L}_e^{\mathsf{T}}\, \mathbf{f}_e + \mathbf{f}_{\text{nodal}}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\mathbf{K}$ | global stiffness matrix | N/m |
| $\mathbf{k}_e$ | stiffness matrix of element $e$ | N/m |
| $\mathbf{L}_e$ | connectivity (gather) matrix of element $e$ | dimensionless |
| $\mathbf{f}$ | global force vector | N |
| $\mathbf{f}_e$ | consistent load vector of element $e$ | N |
| $\mathbf{f}_{\text{nodal}}$ | loads applied directly at nodes | N |

Holds when: elements share nodes (compatibility) and the element matrices use a common coordinate system and unit set.
Breaks when: elements are mixed with incompatible DOF types without a constraint (for example a solid joined to a beam), or a local coordinate system is not rotated into the global one first.
Source and basis: derived from summing element energies; taught in [Finite element method](01-finite-element-method.md).

The assembled $\mathbf{K}$ is symmetric, banded or sparse (a row has entries only for DOFs sharing an element), and singular until rigid-body motion is removed. Each diagonal entry is positive.

Example. Two bars in series, fixed at node 1. Bar 1: $E = 70\ \text{GPa}$, $A = 300\ \text{mm}^2$, $l = 0.6\ \text{m}$. Bar 2: same $E$, $A = 150\ \text{mm}^2$, $l = 0.4\ \text{m}$. Loads: 3 kN at node 2 and 6 kN at node 3. With $k_1 = 35\ \text{MN/m}$ and $k_2 = 26.25\ \text{MN/m}$, the reduced system is

$$\begin{bmatrix} k_1 + k_2 & -k_2 \\ -k_2 & k_2 \end{bmatrix}\begin{bmatrix} u_2 \\ u_3 \end{bmatrix} = \begin{bmatrix} 3 \\ 6 \end{bmatrix}\ \text{kN}$$

Bar 1 carries the full 9 kN, so $u_2 = 9\ \text{kN}/k_1 = 0.257\ \text{mm}$. Bar 2 carries 6 kN, so it stretches 0.229 mm and $u_3 = 0.486\ \text{mm}$. The reaction is 9 kN against the loads.

```verify
E = q(70, "GPa")
k1 = E * q(300, "mm^2") / q(0.6, "m")
k2 = E * q(150, "mm^2") / q(0.4, "m")
expect(k1, "35 MN/m")
expect(k2, "26.25 MN/m")
f2 = q(3, "kN")
f3 = q(6, "kN")
det = k1 * k2
u2 = (k2 * f2 + k2 * f3) / det
u3 = ((k1 + k2) * f3 + k2 * f2) / det
expect(u2, "0.257 mm")
expect(u3, "0.486 mm")
expect(u3 - u2, "0.229 mm")
expect(k1 * u2, "9 kN")
```

## Boundary conditions

A **Dirichlet** condition fixes a DOF to a prescribed value. A **Neumann** condition prescribes a force or flux and enters the right side as a load. Dirichlet conditions are applied by elimination (delete the row and column, move $\mathbf{K}_{fc}\,\bar{\mathbf{d}}_c$ to the right side) or by a penalty.

$$\mathbf{K}_{ff}\,\mathbf{d}_f = \mathbf{f}_f - \mathbf{K}_{fc}\,\bar{\mathbf{d}}_c, \qquad \mathbf{r}_c = \mathbf{K}_{cf}\,\mathbf{d}_f + \mathbf{K}_{cc}\,\bar{\mathbf{d}}_c - \mathbf{f}_c$$

$$K_{ii} \leftarrow K_{ii} + k_p, \qquad f_i \leftarrow f_i + k_p\,\bar{d}_i, \qquad \text{relative error} \approx \frac{k}{k_p}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\mathbf{d}_f$ | free (unknown) nodal displacements | m |
| $\bar{\mathbf{d}}_c$ | prescribed (constrained) displacements | m |
| $\mathbf{K}_{ff}$ | stiffness block of free DOFs | N/m |
| $\mathbf{K}_{fc}$ | stiffness coupling free and constrained DOFs | N/m |
| $\mathbf{f}_f$ | loads on free DOFs | N |
| $\mathbf{r}_c$ | reactions at constrained DOFs | N |
| $k_p$ | penalty stiffness | N/m |
| $k$ | local structural stiffness at the constrained DOF | N/m |

Holds when: constraints remove all rigid-body motion and the penalty stiffness is much larger than the local stiffness, yet small enough not to ruin the conditioning of $\mathbf{K}$ (a ratio near $10^6$ to $10^8$ works in double precision).
Breaks when: the penalty is too small (the constraint leaks) or too large (round-off errors dominate), or constraints conflict with each other. A reaction from a penalty is $k_p (d_i - \bar{d}_i)$ and needs the same care.
Source and basis: derived from partitioning the system and from the energy of a stiff spring; taught in [Finite element method](01-finite-element-method.md).

Natural conditions. A distributed traction $t$ over an edge of length $L_s$ becomes nodal forces $\int \mathbf{N}^{\mathsf{T}} t\,ds$: for a linear edge $t L_s/2$ at each node; for a quadratic edge $t L_s$ times $(1/6,\ 2/3,\ 1/6)$. A force on a quadratic edge is not equal at the three nodes, and a model that splits it equally gives a wrong stress near the edge.

Symmetry. Cut the model on the plane of symmetry and fix the displacement normal to the plane. For beam and shell elements, also fix the two rotations about axes in the plane; leave the in-plane translations free. For an antisymmetric load, fix the in-plane displacements and the rotation about the plane normal instead. A model with more than one symmetry plane needs a constraint on each.

Example. The one-bar problem ($k = 20\ \text{MN/m}$, $P = 10\ \text{kN}$) with node 1 held by a penalty $k_p = 1000\,k$. Then $u_2 = (P/k)(1 + k/k_p)$, which is 0.5005 mm against the exact 0.5 mm, an error of 0.1 percent equal to $k/k_p$.

```verify
k = q(20, "MN/m")
P = q(10, "kN")
ratio = q(1000, "")
kp = ratio * k
u2 = (P / k) * (1 + k / kp)
expect(P / k, "0.500 mm")
expect(u2, "0.5005 mm")
expect(k / kp * 100, "0.1")
```

## Static, thermal, eigenvalue, and transient systems

### Static systems

$$\mathbf{K}\,\mathbf{d} = \mathbf{f}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\mathbf{K}$ | stiffness matrix after constraints | N/m |
| $\mathbf{d}$ | nodal displacements | m |
| $\mathbf{f}$ | nodal loads | N |

Holds when: the problem is linear and static, and $\mathbf{K}$ is positive definite after constraints.
Breaks when: loads grow with deformation, contact opens or closes, or the structure is a mechanism or near a buckling load, where $\mathbf{K}$ is singular or nearly so.
Source and basis: derived from stationarity of $\Pi$; see [Virtual work and minimum potential energy](#virtual-work-and-minimum-potential-energy) and the linear algebra background in [Linear algebra and differential equations reference](../math/reference-linear-algebra-differential-equations.md).

A very large ratio of largest to smallest stiffness (long thin elements next to short stiff ones, or a stiff spring beside a soft one) raises the condition number of $\mathbf{K}$ and degrades the digits of the solution. A zero or tiny pivot signals a missing constraint.

### Thermal conduction

Steady and transient conduction use the same element recipe. For a rod element with conductivity $k_{\text{th}}$, area $A$, length $l$, density $\rho$, and specific heat $c_p$:

$$\mathbf{C}\,\dot{\mathbf{T}} + \mathbf{K}_T\,\mathbf{T} = \mathbf{q}, \qquad \mathbf{k}_{T,e} = \frac{k_{\text{th}} A}{l}\begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix}, \qquad \mathbf{c}_e = \frac{\rho c_p A l}{6}\begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\mathbf{T}$ | nodal temperatures | K |
| $\dot{\mathbf{T}}$ | nodal temperature rates | K/s |
| $\mathbf{K}_T$ | conduction matrix | W/K |
| $\mathbf{C}$ | heat capacity matrix | J/K |
| $\mathbf{q}$ | nodal heat input | W |
| $k_{\text{th}}$ | thermal conductivity | W/(m K) |
| $\rho$ | density | $\text{kg/m}^{3}$ |
| $c_p$ | specific heat | J/(kg K) |
| $A$ | cross-section area | $\text{m}^{2}$ |
| $l$ | element length | m |

Holds when: properties are constant, heat flows along the element, and the loss at the sides is modeled separately (or the sides are insulated).
Breaks when: conductivity depends on temperature, radiation or phase change matters (the system becomes nonlinear), or the transient time step is shorter than the thermal response of one element, which gives oscillating nodal temperatures with consistent capacity.
Source and basis: derived from the weak form of the heat equation; the equation is taught in [Heat transfer](../physics/12-heat-transfer.md).

Example. A rod with $k_{\text{th}} = 50\ \text{W/(m K)}$, $A = 100\ \text{mm}^2$, length 1 m, in 2 elements, with the ends held at 400 K and 300 K. Each element has $k_T = 0.01\ \text{W/K}$. The middle node is at 350 K by symmetry of the two equal elements, and the heat rate is $k_{\text{th}} A\,\Delta T/L = 0.5\ \text{W}$.

```verify
kth = q(50, "W/(m K)")
A = q(100, "mm^2")
l = q(0.5, "m")
kT = kth * A / l
expect(kT, "0.01 W/K")
Tm = (q(400, "K") + q(300, "K")) / 2
expect(Tm, "350 K")
expect(kT * (q(400, "K") - Tm), "0.5 W")
```

### Generalized eigenproblem

Natural frequencies and mode shapes of an undamped structure solve:

$$\left(\mathbf{K} - \omega^2\,\mathbf{M}\right)\boldsymbol{\phi} = \mathbf{0}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\mathbf{K}$ | stiffness matrix | N/m |
| $\mathbf{M}$ | mass matrix | kg |
| $\omega$ | natural angular frequency | rad/s |
| $\boldsymbol{\phi}$ | mode shape vector | dimensionless |

Holds when: the structure is linear, damping is light, and the constraints are fixed. Modes are orthogonal with respect to $\mathbf{M}$ and $\mathbf{K}$.
Breaks when: damping is large (use a complex eigenproblem), the system is nonlinear, or the preload changes the stiffness (include the geometric stiffness).
Source and basis: derived from assuming harmonic motion in $\mathbf{M}\ddot{\mathbf{d}} + \mathbf{K}\mathbf{d} = \mathbf{0}$; vibration theory is in [Vibrations reference](../physics/reference-vibrations.md).

Frequencies from a conforming mesh with consistent mass are upper bounds on the exact values and approach them from above as the mesh is refined. Lumped mass tends to give lower frequencies, so the pair brackets the answer. A rigid-body mode appears as $\omega = 0$.

Example. A fixed-free uniform bar of length $l$, with wave speed $c = \sqrt{E/\rho}$. The exact fundamental frequency is $\omega_1 = (\pi/2)\,c/l = 1.571\,c/l$. One consistent element has $\omega^2 = 3E/(\rho l^2)$, which is $1.732\,c/l$ and is 10.3 percent high. Two consistent elements give the smaller root of a quadratic in $\omega^2$, which is $1.611\,c/l$ and 2.59 percent high.

```verify
exact = pi / 2
one = sqrt(3)
two = sqrt(24 * (10 - sqrt(72)) / 14)
expect(exact, "1.571")
expect(one, "1.732")
expect(two, "1.611")
expect((one / exact - 1) * 100, "10.3")
expect((two / exact - 1) * 100, "2.59")
```

### Transient implicit integration

The structural equation of motion is $\mathbf{M}\ddot{\mathbf{d}} + \mathbf{C}\dot{\mathbf{d}} + \mathbf{K}\mathbf{d} = \mathbf{f}(t)$. The **average acceleration** method treats the acceleration over a step as the mean of its start and end values. It is implicit: each step solves one linear system with the effective stiffness.

$$\mathbf{d}_{n+1} = \mathbf{d}_n + \Delta t\,\mathbf{v}_n + \frac{\Delta t^2}{4}\left(\mathbf{a}_n + \mathbf{a}_{n+1}\right), \qquad \mathbf{v}_{n+1} = \mathbf{v}_n + \frac{\Delta t}{2}\left(\mathbf{a}_n + \mathbf{a}_{n+1}\right)$$

$$\left(\mathbf{K} + \frac{2}{\Delta t}\mathbf{C} + \frac{4}{\Delta t^2}\mathbf{M}\right)\mathbf{d}_{n+1} = \mathbf{f}_{n+1} + \mathbf{M}\left(\frac{4}{\Delta t^2}\mathbf{d}_n + \frac{4}{\Delta t}\mathbf{v}_n + \mathbf{a}_n\right) + \mathbf{C}\left(\frac{2}{\Delta t}\mathbf{d}_n + \mathbf{v}_n\right), \qquad \tan\frac{\bar\omega\,\Delta t}{2} = \frac{\omega\,\Delta t}{2}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\Delta t$ | time step | s |
| $\mathbf{d}_n$ | displacement vector at step $n$ | m |
| $\mathbf{v}_n$ | velocity vector at step $n$ | m/s |
| $\mathbf{a}_n$, $\mathbf{a}_{n+1}$ | acceleration vector at step $n$ and $n+1$ | $\text{m/s}^{2}$ |
| $\mathbf{M}$ | mass matrix | kg |
| $\mathbf{C}$ | damping matrix | N s/m |
| $\mathbf{K}$ | stiffness matrix | N/m |
| $\mathbf{f}_{n+1}$ | load at the end of the step | N |
| $\omega$ | exact angular frequency of a mode | rad/s |
| $\bar\omega$ | frequency computed by the integrator | rad/s |

Holds when: the system is linear and the step resolves the highest mode that carries the response. The method is unconditionally stable for linear systems, so $\Delta t$ is set by accuracy, not stability.
Breaks when: the response contains modes with $\omega \Delta t \gg 1$ (they are retained without numerical damping and can pollute the result), or the problem is nonlinear (stability is no longer guaranteed; iterate each step).
Source and basis: derived from integrating the acceleration with its mean value over the step; the amplification matrix has unit-magnitude eigenvalues, so there is no amplitude decay.

The period is stretched, not the amplitude. The relative period elongation is about $(\omega \Delta t)^2/12$ for small $\omega \Delta t$. Rule of thumb: use at least 20 steps per period of the highest mode of interest; the period error falls from 3.21 percent at ten steps to 0.82 percent at twenty.

Example. A mode at $\omega = 100\ \text{rad/s}$ with $\Delta t = 5\ \text{ms}$ has $\omega \Delta t = 0.5$ and 12.6 steps per period. The integrator frequency satisfies $\bar\omega \Delta t = 2 \arctan(\omega \Delta t/2) = 0.490$, so the computed period is 2.05 percent too long.

```verify
w = q(100, "rad/s")
dt = q(5, "ms")
x = w * dt
expect(x, "0.5")
expect(2 * pi / x, "12.6")
th = 2 * atan(x / 2)
expect(th, "0.490")
expect((x / th - 1) * 100, "2.05")
n10 = q(10, "")
x10 = 2 * pi / n10
th10 = 2 * atan(x10 / 2)
expect((x10 / th10 - 1) * 100, "3.21")
n20 = q(20, "")
x20 = 2 * pi / n20
th20 = 2 * atan(x20 / 2)
expect((x20 / th20 - 1) * 100, "0.82")
```

### Transient explicit integration

The **central difference** method uses the acceleration at the current step, so it needs no matrix solve when the mass matrix is diagonal.

$$\mathbf{a}_n = \mathbf{M}^{-1}\left(\mathbf{f}_n - \mathbf{K}\mathbf{d}_n\right), \qquad \mathbf{d}_{n+1} = 2\mathbf{d}_n - \mathbf{d}_{n-1} + \Delta t^2\,\mathbf{a}_n, \qquad \Delta t \le \frac{2}{\omega_{\max}}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\mathbf{a}_n$ | acceleration at step $n$ | $\text{m/s}^{2}$ |
| $\mathbf{d}_n$ | displacement at step $n$ | m |
| $\mathbf{M}$ | diagonal (lumped) mass matrix | kg |
| $\mathbf{K}$ | stiffness matrix | N/m |
| $\mathbf{f}_n$ | external load at step $n$ | N |
| $\Delta t$ | time step | s |
| $\omega_{\max}$ | highest natural angular frequency of the mesh | rad/s |

Holds when: the step is below the stability limit, the mass is lumped, and the response is wave-like or impact-like, where short steps are needed anyway for accuracy.
Breaks when: the step exceeds $2/\omega_{\max}$ (the solution grows without bound), damping is large (damping lowers the limit), or the loading is slow, where the tiny step makes the run cost far more than an implicit analysis.
Source and basis: derived from the stability analysis of the difference equation for one mode.

For a lumped-mass bar element, $\omega_{\max} = 2c/l$, so $\Delta t_{\text{crit}} = l/c$, the time a stress wave takes to cross the element. The limit for a mesh is set by its smallest element, and refining one region lowers the step for the whole model. Consistent mass has $\omega_{\max} = \sqrt{12}\,c/l$, a limit of $0.577\,l/c$.

Example. Steel bar elements 10 mm long with $E = 200\ \text{GPa}$ and $\rho = 7850\ \text{kg/m}^3$. The wave speed is 5048 m/s, so $\omega_{\max} = 1.010 \times 10^{6}\ \text{rad/s}$ and the critical step is 1.98 microseconds.

```verify
E = q(200, "GPa")
rho = q(7850, "kg/m^3")
l = q(10, "mm")
c = sqrt(E / rho)
expect(c, "5048 m/s")
wmax = 2 * c / l
expect(wmax, "1.010e6 rad/s")
expect(2 / wmax, "1.98 us")
expect(l / c, "1.98 us")
```

## Error and convergence

Convergence of a finite element solution depends on the mesh size $h$ and the degree $p$ of the complete polynomial in each element. For a smooth solution, a conforming mesh, and exact integration, the error scales as a power of $h$.

$$\lVert \mathbf{e} \rVert_{E} \propto h^{p}, \qquad \lVert e_u \rVert_{L_2} \propto h^{p+1}, \qquad \lVert e_\sigma \rVert \propto h^{p}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\lVert \mathbf{e} \rVert_{E}$ | error in the energy norm | $\text{kg}^{1/2}\,\text{m/s}$ |
| $\lVert e_u \rVert_{L_2}$ | root-mean-square error in displacement | m |
| $\lVert e_\sigma \rVert$ | root-mean-square error in stress | Pa |
| $h$ | characteristic element size | m |
| $p$ | degree of the complete polynomial in each element | dimensionless |

Holds when: the proportionality constant depends on the solution and mesh shape but not on $h$, the exact solution is smooth (no singularity), elements are not badly distorted, and the mesh is fine enough to be in the asymptotic range.
Breaks when: the solution has a singularity (the rate falls, see below), elements are very distorted, or the mesh is too coarse to see the asymptotic rate.
Source and basis: derived from the best-approximation property of the energy-norm solution and polynomial interpolation error. The strain-energy error, which is proportional to the squared energy norm, falls as $h^{2p}$. The study of observed order, Richardson extrapolation, and the grid convergence index is in [Verification and validation reference](reference-verification-validation.md).

Typical rates, for smooth solutions:

| Element | Displacement error | Stress error |
|---|---|---|
| Linear (3-node triangle, 4-node quad) | $h^2$ | $h$ |
| Quadratic (6-node triangle, 8-node quad) | $h^3$ | $h^2$ |

**h-refinement** halves $h$ at fixed $p$ and gives the algebraic rates above. **p-refinement** raises $p$ at fixed mesh and, for smooth solutions, converges faster than any power of $h$. Use $p$-refinement when the solution is smooth and $h$-refinement near singularities.

The **patch test** applies displacements of a constant strain field to the boundary of an arbitrary patch of elements. The interior nodes must then take exactly the field values and every element must show the same constant stress. An element that fails does not converge.

Example. Halving $h$ for linear elements divides the displacement error by 4 and the stress error by 2. A displacement error of 0.80 percent becomes 0.20 percent; a stress error of 8.0 percent becomes 4.0 percent. Patch test in one dimension. Two bar elements of length 0.3 m and 0.7 m, end displacement 1.000 mm over 1 m. The interior node must sit at 0.300 mm.

```verify
h1 = q(0.3, "m")
h2 = q(0.7, "m")
ka = 1 / h1
kb = 1 / h2
u3 = q(1.000, "mm")
u2 = kb / (ka + kb) * u3
expect(u2, "0.300 mm")
ed = q(0.80, "")
es = q(8.0, "")
expect(ed / 2**2, "0.20")
expect(es / 2, "4.0")
```

## Element limitations and locking

### Shear locking

**Shear locking** is spurious stiffness in a bending-dominated field because the element cannot bend without also shearing. A full-integrated 4-node quadrilateral in a pure bending field produces a spurious shear strain $\gamma_{xy} = \kappa x$ for curvature $\kappa$, where $x$ is measured from the element center.

$$\frac{U_{\text{shear}}}{U_{\text{bend}}} \approx \frac{1 - \nu}{2}\left(\frac{a}{h_t}\right)^2$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $U_{\text{shear}}$ | spurious shear energy of a bending mode | J |
| $U_{\text{bend}}$ | bending energy of the same mode | J |
| $\nu$ | Poisson's ratio | dimensionless |
| $a$ | element length along the span | m |
| $h_t$ | element height across the bending direction | m |

Holds when: the element is a rectangle under a pure bending mode with plane stress and full 2 by 2 integration. Read the ratio as a scale of the added stiffness, not an exact factor.
Breaks when: the element is high-order, uses reduced or selective integration, or is a bending-capable element (incompatible modes and mixed formulations remove the effect).
Source and basis: derived from averaging $G\gamma^2/2$ and $E\varepsilon^2/(2(1-\nu^2))$ over the element for the bending mode $u = -\kappa x y$.

Remedies: use a mesh with element length close to its height across the bending direction (aspect ratio near 1), several elements through the thickness, higher-order elements, or an element formulated to avoid the effect.

Example. $\nu = 0.3$ and an aspect ratio $a/h_t = 4$: the ratio is 5.6, so the element is stiffer in bending by a factor of the order of 6.6.

```verify
nu = q(0.3, "")
r = (1 - nu) / 2 * 4**2
expect(r, "5.6")
expect(1 + r, "6.6")
```

### Volumetric locking

**Volumetric locking** occurs in nearly incompressible materials ($\nu$ near 0.5): the bulk modulus $K_b$ tends to infinity, so any volume change costs enormous energy, and an element with too many volume constraints cannot deform at all.

$$K_b = \frac{E}{3\,(1 - 2\nu)}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $K_b$ | bulk modulus | Pa |
| $E$ | Young's modulus | Pa |
| $\nu$ | Poisson's ratio | dimensionless |

Holds when: the material is isotropic and linear elastic.
Breaks when: the material is nonlinear or anisotropic, where the bulk response comes from a different relation.
Source and basis: derived from the isotropic elasticity relations between $E$, $\nu$, and the pressure-volume response.

Example. $K_b/E$ equals 0.833 at $\nu = 0.3$, 16.7 at $\nu = 0.49$, and 167 at $\nu = 0.499$. A 4-node plane strain quadrilateral with 2 by 2 integration imposes 4 volume constraints on 5 free DOFs (8 minus 3 rigid-body modes), which is too many; one constraint at a single point (reduced integration on the volumetric term) or a mixed displacement and pressure element avoids locking. The ratio of free DOFs to constraints for a fine mesh in plane strain is near 2, and an element with a lower ratio tends to lock.

```verify
n1 = q(0.3, "")
n2 = q(0.49, "")
n3 = q(0.499, "")
expect(1 / (3 * (1 - 2 * n1)), "0.833")
expect(1 / (3 * (1 - 2 * n2)), "16.7")
expect(1 / (3 * (1 - 2 * n3)), "167")
```

### Stress singularities

A **stress singularity** is a point where the stress of the mathematical model is infinite. Near a re-entrant corner or a crack tip, the stress varies as $r^{\lambda - 1}$ with $r$ the distance from the tip and $\lambda$ between 0.5 and 1 for an interior angle between 360 and 180 degrees. A crack has $\lambda = 0.5$ and the $1/\sqrt{r}$ field of fracture mechanics. Near a point load on an elastic body in plane problems, the stress grows as $1/r$.

$$\sigma \propto r^{\lambda - 1}, \qquad \sigma_{\text{FE}} \propto h^{\lambda - 1}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\sigma$ | stress of the exact model at distance $r$ | Pa |
| $\sigma_{\text{FE}}$ | stress computed in the element at the singular point | Pa |
| $r$ | distance from the singular point | m |
| $h$ | element size at the singular point | m |
| $\lambda$ | strength exponent of the singularity | dimensionless |

Holds when: the geometry has a sharp re-entrant corner or crack in a linear elastic model; the value of $\lambda$ comes from the elasticity solution for that geometry. Elasticity background is in [physics/reference-solid-mechanics.md](../physics/reference-solid-mechanics.md).
Breaks when: the real part has a radius or a plastic zone (the true peak stress is finite and set by the radius), in which case model the radius with enough elements and the stress converges.
Source and basis: derived from the asymptotic solution of the elasticity equations near the singular point.

The strain energy still converges, but at a reduced rate: the energy-norm error falls as $h^{\lambda}$, so the strain-energy error falls as $h^{2\lambda}$. Reading the peak stress at the singular point therefore gives a number that depends on the element size and carries no design meaning. Take the stress a few element sizes away, model the real fillet, spread the point load over a contact patch, or use a fracture parameter instead of a stress.

Example. For $\lambda = 0.5$ (a crack), halving $h$ raises the computed tip stress by a factor $2^{1 - \lambda} = 1.414$, and the energy-norm error falls only by $2^{0.5} = 1.414$ per halving instead of 2.

```verify
lam = q(0.5, "")
expect(2**(1 - lam), "1.414")
expect(2**lam, "1.414")
```

## Nonlinear-analysis boundary

A linear analysis is valid only when the stiffness does not change during loading. Three sources of nonlinearity break that: **geometric** (large displacement or rotation, stress stiffening, buckling), **material** (plasticity, creep, hyperelasticity), and **contact** (gaps that open or close, friction). Contact makes the response piecewise linear in the load and the contact status unknown in advance.

$$\mathbf{K}_T\,\Delta\mathbf{d} = \mathbf{f}_{\text{ext}} - \mathbf{f}_{\text{int}}(\mathbf{d}), \qquad \mathbf{d} \leftarrow \mathbf{d} + \Delta\mathbf{d}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\mathbf{K}_T$ | tangent stiffness matrix, $\partial \mathbf{f}_{\text{int}}/\partial \mathbf{d}$ | N/m |
| $\Delta\mathbf{d}$ | displacement correction | m |
| $\mathbf{f}_{\text{ext}}$ | external load vector | N |
| $\mathbf{f}_{\text{int}}$ | internal force vector at the current displacement | N |
| $\mathbf{d}$ | nodal displacements | m |

Holds when: the internal force is smooth and the tangent is nonsingular, with a starting guess close enough to the root. Convergence is quadratic near the solution.
Breaks when: the tangent is singular (buckling, snap-through, or a rigid-body contact mode), the step is too large for the iteration to stay in its basin (apply the load in increments), or the model has sudden contact changes. Check both the residual and the displacement correction before accepting a step.
Source and basis: derived from a Taylor expansion of $\mathbf{f}_{\text{int}}$ to first order.

When to leave the linear model: displacements above about a tenth of the thickness for plates and shells, strains beyond yield, or any gap that closes under load. Linear buckling solves $(\mathbf{K} + \lambda_b \mathbf{K}_G)\boldsymbol{\phi} = \mathbf{0}$ for the load factor $\lambda_b$, where $\mathbf{K}_G$ is the geometric stiffness; it is an upper bound on the real buckling load of an imperfect part.

Example. One DOF with $f_{\text{int}} = k_1 u + k_3 u^3$, $k_1 = 1\ \text{MN/m}$, $k_3 = 1000\ \text{N/mm}^3$, and load 2 kN. Starting from $u = 0$: iteration 1 gives 2.000 mm, iteration 2 gives 1.385 mm, iteration 3 gives 1.083 mm, and the root is exactly 1.000 mm.

```verify
k1 = q(1, "MN/m")
k3 = q(1000, "N/mm^3")
f = q(2, "kN")
y = q(0, "mm")
fi = k1 * y + k3 * y**3
K = k1 + 3 * k3 * y**2
y1 = y + (f - fi) / K
expect(y1, "2.000 mm")
fi = k1 * y1 + k3 * y1**3
K = k1 + 3 * k3 * y1**2
y2 = y1 + (f - fi) / K
expect(y2, "1.385 mm")
fi = k1 * y2 + k3 * y2**3
K = k1 + 3 * k3 * y2**2
y3 = y2 + (f - fi) / K
expect(y3, "1.083 mm")
expect(k1 * q(1, "mm") + k3 * q(1, "mm")**3, "2 kN")
```

## Result recovery

Displacements are the primary result. Strains and stresses are computed from derivatives of the interpolation, so they are less accurate and are discontinuous between elements. **Nodal averaging** replaces the several element values at a node by their mean, and the **jump** between them is a local error indicator.

$$\bar\sigma_{\text{node}} = \frac{1}{m}\sum_{e=1}^{m} \sigma_e, \qquad \Delta\sigma = \sigma_{e_1} - \sigma_{e_2}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\bar\sigma_{\text{node}}$ | averaged nodal stress | Pa |
| $\sigma_e$ | stress in element $e$ extrapolated to the node | Pa |
| $m$ | number of elements sharing the node | dimensionless |
| $\Delta\sigma$ | stress jump between two elements at a node | Pa |

Holds when: the stress field is smooth across the node and the elements share the same material and thickness.
Breaks when: the node lies on a real discontinuity (a material interface, a thickness change, a point load), where the true stress jumps and averaging hides it. Compute and plot unaveraged stress there.
Source and basis: derived from the definition of the mean; the jump as an indicator follows from the continuity of exact stress where properties are smooth.

A jump that does not shrink on a finer mesh marks a real feature or a modeling fault. A jump that shrinks marks discretization error. Also check:

- Sum of reactions equals the sum of applied loads, in every direction.
- Moments about a point balance as well.
- Strain energy $U = \tfrac{1}{2}\mathbf{d}^{\mathsf{T}}\mathbf{f}$ equals half the work of the loads.
- A hand calculation of the same loaded part agrees to the accuracy the model is claimed to have.

Example. A uniform bar fixed at one end, $L = 2\ \text{m}$, $A = 100\ \text{mm}^2$, $E = 200\ \text{GPa}$, load $b = 1\ \text{kN/m}$ along the length, 2 equal elements with consistent loads (500 N, 1000 N, 500 N). The element stresses are 15 MPa near the support and 5 MPa at the free end, a jump of 10 MPa at the middle node. The average, 10 MPa, equals the exact stress at midspan. The force at the far end of the first element is 1.5 kN and the reaction is 2 kN, equal to the applied load.

```verify
E = q(200, "GPa")
A = q(100, "mm^2")
h = q(1, "m")
k = E * A / h
f2 = q(1000, "N")
f3 = q(500, "N")
u2 = (f2 + f3) / k
u3 = u2 + f3 / k
s1 = E * u2 / h
s2 = E * (u3 - u2) / h
expect(s1, "15 MPa")
expect(s2, "5 MPa")
expect(s1 - s2, "10 MPa")
expect((s1 + s2) / 2, "10 MPa")
expect(k * u2, "1.5 kN")
expect(q(1, "kN/m") * q(2, "m"), "2 kN")
```

## Checklists

Before solving:

- Units are one consistent set, written down. Check that a load of 1 N on a 1 mm bar gives the displacement you expect.
- The geometry, material, and load case describe the part, with the source of each value known.
- Constraints remove every rigid-body mode and are no stiffer than the real support.
- The element type suits the field: no 3-node triangle or 4-node quadrilateral in a bending-dominated region without refinement; no reduced-integration element without hourglass control.
- Mesh quality: no inverted elements ($\det \mathbf{J} > 0$ at every integration point), no extreme aspect ratios or angles, refinement where stress changes quickly.

After solving:

- Reactions balance the applied loads in every direction.
- Deformed shape moves the right way and has the right magnitude on an undistorted scale.
- Strain energy is positive and equals half the work of the loads.
- Stress is read away from singularities and away from the constraint edges, in unaveraged form, and compared with a hand calculation.
- Mesh convergence of the quantity that drives the decision is shown; see [Verification and validation reference](reference-verification-validation.md).
- For dynamics: the time step resolves the highest mode of interest (implicit) or is below the critical step (explicit).
- For nonlinear runs: the load was applied in increments, the residual and the correction both converged, and contact status is plausible.

## Sanity checks

- A fixed-free bar of stiffness $E A/l$ loaded at the tip moves $P l/(E A)$. Any bar model should reproduce this to its numerical precision.
- A cantilever with a tip load deflects $P L^3/(3 E I_A)$; one cubic beam element reproduces this exactly.
- A mesh that is too coarse overestimates stiffness (displacements low) for conforming elements. A result far more flexible than the hand value suggests a missing load path, a wrong material, or wrong units.
- Natural frequency of a mass on a spring is $\sqrt{k/m}$; if the lowest nonzero frequency of a model is far from the hand estimate of its main mode, check mass and stiffness units first.
- Total mass from the mass matrix equals density times volume. A fraction means a missing part or wrong density.
- Peak stress that keeps rising by a steady factor when the element size halves signals a singularity, not a converged result. The factor is at most about 1.4 at a corner or crack and 2 at a point load.
- Mesh convergence plot: the answer should settle, and the error should fall at the rate given in the error table. If it does not, the mesh is not in the asymptotic range or the solution is singular.

## Further reference

- [Finite Element Analysis of Solids and Fluids I (2.092)](https://ocw.mit.edu/courses/2-092-finite-element-analysis-of-solids-and-fluids-i-fall-2009/) by MIT OpenCourseWare: a full undergraduate course on the method.
- [Finite element method](01-finite-element-method.md): the hand-worked introduction that this sheet extends.
- [Verification and validation reference](reference-verification-validation.md): mesh convergence studies, Richardson extrapolation, the grid convergence index, and validation against test.
- [Mechanics reference](../physics/reference-mechanics.md) and [Vibrations reference](../physics/reference-vibrations.md): hand formulas to check a model against.
- [Linear algebra and differential equations reference](../math/reference-linear-algebra-differential-equations.md): matrix solution and eigenproblems.
- Books by title: *Finite Element Procedures*; *Concepts and Applications of Finite Element Analysis*; *The Finite Element Method: Its Basis and Fundamentals*; *Nonlinear Finite Elements for Continua and Structures*.
