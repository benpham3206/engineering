# Solid mechanics reference

**Type:** reference
**Verify:** strict

Lookup sheet for the tensor theory of elastic solids, energy methods, indeterminate members, torsion of thin-walled sections, thick-walled cylinders, rotating disks, plates, shells, and their buckling, for an engineer at level 3 who has outgrown the elementary formulas in [physics/reference-mechanics.md](reference-mechanics.md).

## Principles

- Stress at a point is a second-order tensor, not a number. Its components change with the axes, but its principal values and invariants do not. A failure criterion built from invariants does not depend on how the axes were drawn.
- Every elasticity problem needs three sets of equations: equilibrium, the strain-displacement relations with compatibility, and a constitutive law. Closed-form solutions exist only where geometry and loading make these collapse to one ordinary differential equation.
- Energy is the shortcut. For a linear elastic body the strain energy is a quadratic form in loads or displacements, so deflections, redundants, and approximate solutions follow from derivatives and integrals instead of solving the field equations.
- Redundancy is bought with compatibility. Each redundant force adds one equation that says a displacement is zero (or known); the extra stiffness comes from the extra load path.
- Hydrostatic stress changes volume but not shape. Yield of ductile metals follows the shape-changing part, which is why a pressure of any size does not yield a metal by itself.
- Thin and thick are comparisons of thickness with the radius or the span. Each thin-walled theory (membrane, plate, thin-walled torsion) drops the stress component through the thickness and is wrong where that component matters: near supports, load points, and junctions.
- A thin plate or shell carries load by bending and by in-plane stretching. Which one governs sets the formula, and swapping one for the other is a common source of order-of-magnitude errors.
- Linear elastic stress analysis cannot predict buckling. A thin compressed member reaches an instability at a stress far below yield, and real shells reach it below the classical value.
- Check the sign convention first. Tension is positive here, and the engineering shear strain $\gamma$ is twice the tensor shear strain.

## Stress and strain tensors

### Index notation and transformation

The **stress tensor** $\boldsymbol{\sigma}$ collects the nine components $\sigma_{ij}$, where the first index names the face (by its outward normal) and the second names the direction of the force. A repeated index in a product is summed over $x$, $y$, $z$. Moment balance makes the tensor symmetric, $\sigma_{ij} = \sigma_{ji}$, so six components are independent.

$$t_i = \sigma_{ij}\, n_j \qquad \sigma'_{ij} = l_{ik}\, l_{jl}\, \sigma_{kl} \qquad \varepsilon_{ij} = \tfrac{1}{2}\left(u_{i,j} + u_{j,i}\right)$$

- $l_{ik}$ is the cosine of the angle between new axis $i$ and old axis $k$. For a rotation by $\theta$ about $z$, in plane: $\sigma'_{x} = \sigma_x \cos^2\theta + \sigma_y \sin^2\theta + 2\tau_{xy}\sin\theta\cos\theta$ and $\tau'_{xy} = -(\sigma_x - \sigma_y)\sin\theta\cos\theta + \tau_{xy}(\cos^2\theta - \sin^2\theta)$.
- The tensor shear strain is $\varepsilon_{xy} = \gamma_{xy}/2$. Transformation rules apply to $\varepsilon_{ij}$, not to $\gamma$.
- Example: $\sigma_x = 80$ MPa, $\sigma_y = 20$ MPa, $\tau_{xy} = 30$ MPa, rotated by 30 degrees. Then $\sigma'_x = 90.98$ MPa, $\sigma'_y = 9.02$ MPa, $\tau'_{xy} = -10.98$ MPa, and $\sigma'_x + \sigma'_y = 100$ MPa, equal to $\sigma_x + \sigma_y$.

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $t_i$ | traction (force per area) on a face | Pa |
| $\sigma_{ij}$ | stress tensor component | Pa |
| $n_j$ | component of the outward unit normal of the face | dimensionless |
| $l_{ik}$ | direction cosine between new axis $i$ and old axis $k$ | dimensionless |
| $\varepsilon_{ij}$ | strain tensor component | dimensionless |
| $u_i$ | displacement component | m |
| $u_{i,j}$ | derivative of $u_i$ with respect to coordinate $j$ | dimensionless |
| $\theta$ | rotation of the axes about $z$ | rad |
| $\tau_{xy}$ | shear stress | Pa |
| $\gamma_{xy}$ | engineering shear strain | rad |

Holds when: small displacement gradients, so the strain is the symmetric part of the displacement gradient; the axes are right-handed and Cartesian.
Breaks when: strains or rotations are large (finite-strain measures are needed), or the material carries couple stresses (the stress tensor is then not symmetric).
Source and basis: derived from force and moment equilibrium of a tetrahedron cut from the body and from the geometry of small deformation; the plane case is Mohr's circle in [physics/reference-mechanics.md](reference-mechanics.md) ([stress and strain](reference-mechanics.md#stress-and-strain)).

```verify
sx = q(80, "MPa")
sy = q(20, "MPa")
txy = q(30, "MPa")
th = q(30, "deg")
c = cos(th)
s = sin(th)
expect(sx * c**2 + sy * s**2 + 2 * txy * s * c, "90.98 MPa")
expect(sx * s**2 + sy * c**2 - 2 * txy * s * c, "9.02 MPa")
expect(-(sx - sy) * s * c + txy * (c**2 - s**2), "-10.98 MPa")
expect((sx * c**2 + sy * s**2 + 2 * txy * s * c) + (sx * s**2 + sy * c**2 - 2 * txy * s * c), "100 MPa")
```

### Invariants and principal stresses

The principal stresses are the roots of a cubic whose coefficients are the three **stress invariants**, numbers that do not change when the axes rotate.

$$\sigma^3 - I_1 \sigma^2 + I_2 \sigma - I_3 = 0$$

$$I_1 = \sigma_x + \sigma_y + \sigma_z \qquad I_2 = \sigma_x\sigma_y + \sigma_y\sigma_z + \sigma_z\sigma_x - \tau_{xy}^2 - \tau_{yz}^2 - \tau_{zx}^2 \qquad I_3 = \det \boldsymbol{\sigma}$$

- In terms of the ordered principal stresses $\sigma_1 \ge \sigma_2 \ge \sigma_3$: $I_1 = \sigma_1 + \sigma_2 + \sigma_3$, $I_2 = \sigma_1\sigma_2 + \sigma_2\sigma_3 + \sigma_3\sigma_1$, $I_3 = \sigma_1\sigma_2\sigma_3$. The absolute largest shear stress is $(\sigma_1 - \sigma_3)/2$.
- Example: the plane state above with $\sigma_z = 40$ MPa and no other shear. Then $I_1 = 140\ \text{MPa}$, $I_2 = 4700\ \text{MPa}^{2}$, $I_3 = 28000\ \text{MPa}^{3}$. The roots are 92.43, 40, and 7.57 MPa.

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\sigma$ | an eigenvalue of the stress tensor (a principal stress) | Pa |
| $I_1$ | first stress invariant | Pa |
| $I_2$ | second stress invariant | $\text{Pa}^{2}$ |
| $I_3$ | third stress invariant | $\text{Pa}^{3}$ |
| $\sigma_x$, $\sigma_y$, $\sigma_z$ | normal stress components | Pa |
| $\tau_{xy}$, $\tau_{yz}$, $\tau_{zx}$ | shear stress components | Pa |
| $\sigma_1$, $\sigma_2$, $\sigma_3$ | principal stresses, largest first | Pa |

Holds when: the stress tensor is symmetric, which gives three real principal stresses and mutually perpendicular principal directions.
Breaks when: the tensor is not symmetric (couple stresses); a repeated root makes the principal directions non-unique, though the stresses are still correct.
Source and basis: derived from the eigenvalue problem $(\sigma_{ij} - \sigma \delta_{ij}) n_j = 0$, which asks for faces on which the traction is purely normal.

```verify
sx = q(80, "MPa")
sy = q(20, "MPa")
sz = q(40, "MPa")
txy = q(30, "MPa")
expect(sx + sy + sz, "140 MPa")
expect(sx * sy + sy * sz + sz * sx - txy**2, "4700 MPa^2")
expect(sz * (sx * sy - txy**2), "28000 MPa^3")
R = sqrt(((sx - sy) / 2)**2 + txy**2)
expect((sx + sy) / 2 + R, "92.43 MPa")
expect((sx + sy) / 2 - R, "7.57 MPa")
expect(((sx + sy) / 2 + R) + ((sx + sy) / 2 - R) + sz, "140 MPa")
```

### Von Mises invariant

The **deviatoric stress** $s_{ij} = \sigma_{ij} - \tfrac{1}{3}\sigma_{kk}\delta_{ij}$ is the stress that changes shape without changing volume. Its second invariant sets the von Mises equivalent stress.

$$\sigma_{vm} = \sqrt{3 J_2} = \sqrt{\tfrac{1}{2}\left[(\sigma_1 - \sigma_2)^2 + (\sigma_2 - \sigma_3)^2 + (\sigma_3 - \sigma_1)^2\right]}$$

- Adding the same pressure to all three principal stresses leaves $\sigma_{vm}$ unchanged because it does not change the deviatoric stress. For yield checks, including the Tresca criterion and pure-shear limits, see [combined loading and failure criteria](reference-mechanics.md#combined-loading-and-failure-criteria).
- Example: principal stresses 92.43, 40, 7.57 MPa give $\sigma_{vm} = 74.17$ MPa. Adding 100 MPa of hydrostatic stress to all three leaves $\sigma_{vm}$ unchanged.

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\sigma_{vm}$ | von Mises equivalent stress | Pa |
| $J_2$ | second invariant of the deviatoric stress | $\text{Pa}^{2}$ |
| $s_{ij}$ | deviatoric stress component | Pa |
| $\sigma_{kk}$ | trace of the stress tensor, $I_1$ | Pa |
| $\delta_{ij}$ | Kronecker delta (1 if $i = j$, else 0) | dimensionless |
| $\sigma_1$, $\sigma_2$, $\sigma_3$ | principal stresses, largest first | Pa |

Holds when: isotropic ductile metal, yield independent of mean stress, monotonic loading at moderate temperature.
Breaks when: the material is brittle, pressure-sensitive (soils, concrete, many polymers), or anisotropic, under cyclic loading, or the stress state is so triaxial that fracture, not yield, governs.
Source and basis: derived from the distortion energy (the part of strain energy that changes shape); the yield criteria are given in [combined loading and failure criteria](reference-mechanics.md#combined-loading-and-failure-criteria).

```verify
s1 = q(92.43, "MPa")
s2 = q(40, "MPa")
s3 = q(7.57, "MPa")
expect(sqrt(0.5 * ((s1 - s2)**2 + (s2 - s3)**2 + (s3 - s1)**2)), "74.17 MPa")
h = q(100, "MPa")
expect(sqrt(0.5 * (((s1 + h) - (s2 + h))**2 + ((s2 + h) - (s3 + h))**2 + ((s3 + h) - (s1 + h))**2)), "74.17 MPa")
```

### Plane stress and plane strain

**Plane stress** has $\sigma_z = \tau_{xz} = \tau_{yz} = 0$ (thin plate loaded in its plane). **Plane strain** has $\varepsilon_z = \gamma_{xz} = \gamma_{yz} = 0$ (long body with constant cross section, such as a dam or a pipe far from its ends).

$$\text{plane stress: } \varepsilon_z = -\frac{\nu}{E}\left(\sigma_x + \sigma_y\right) \qquad \text{plane strain: } \sigma_z = \nu\left(\sigma_x + \sigma_y\right)$$

- A plane-strain problem has the plane-stress equations with $E \to E/(1 - \nu^2)$ and $\nu \to \nu/(1 - \nu)$.
- Plane strain adds $\sigma_z = \nu(\sigma_x + \sigma_y)$. When both in-plane principal stresses have the same sign and $\sigma_z$ lies between them, this usually lowers von Mises stress and leaves Tresca unchanged. The added triaxial constraint delays ductile yield but can promote brittle fracture.
- Example: $\sigma_x = 80$, $\sigma_y = 20$ MPa, $\tau_{xy} = 30$ MPa, $E = 200$ GPa, $\nu = 0.3$. Plane stress gives $\varepsilon_z = -1.5 \times 10^{-4}$. Plane strain gives $\sigma_z = 30$ MPa, and $\sigma_{vm}$ is 76.16 MPa, compared with 88.9 MPa in plane stress.

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\varepsilon_z$ | out-of-plane normal strain | dimensionless |
| $\sigma_z$ | out-of-plane normal stress | Pa |
| $\sigma_x$, $\sigma_y$ | in-plane normal stresses | Pa |
| $E$ | Young's modulus | Pa |
| $\nu$ | Poisson's ratio | dimensionless |

Holds when: the loading and geometry really are uniform through the thickness (plane stress) or along the axis (plane strain), and the material is isotropic and linear elastic.
Breaks when: the plate is thick enough that $\sigma_z$ is not negligible near holes or edges (a state between the two), or the body ends constrain the axial strain only partly.
Source and basis: derived from the isotropic Hooke's law with the stated component set to zero; taught in [Axial and torsion](04-axial-and-torsion.md) for the uniaxial case.

```verify
E = q(200, "GPa")
nu = q(0.30, "")
sx = q(80, "MPa")
sy = q(20, "MPa")
txy = q(30, "MPa")
expect(-nu * (sx + sy) / E, "-1.5e-4")
sz = nu * (sx + sy)
expect(sz, "30 MPa")
expect(sqrt(0.5 * ((sx - sy)**2 + (sy - sz)**2 + (sz - sx)**2) + 3 * txy**2), "76.16 MPa", rel=0.001)
expect(sqrt(sx**2 - sx * sy + sy**2 + 3 * txy**2), "88.9 MPa")
```

## Three-dimensional constitutive laws

### Isotropic Hooke's law and the elastic constants

An **isotropic** material has the same stiffness in every direction. Two independent constants describe it, and every other constant follows from any two.

$$\varepsilon_{ij} = \frac{1 + \nu}{E}\,\sigma_{ij} - \frac{\nu}{E}\,\sigma_{kk}\,\delta_{ij} \qquad \sigma_{ij} = 2G\,\varepsilon_{ij} + \lambda_L\,\varepsilon_{kk}\,\delta_{ij}$$

$$G = \frac{E}{2(1 + \nu)} \qquad \lambda_L = \frac{E\nu}{(1 + \nu)(1 - 2\nu)} \qquad K_b = \frac{E}{3(1 - 2\nu)} = \lambda_L + \tfrac{2}{3}G \qquad \sigma_{kk} = 3K_b\,\varepsilon_{kk}$$

- The **bulk modulus** $K_b$ is the ratio of mean stress $\sigma_{kk}/3$ to volumetric strain $\varepsilon_{kk}$. It tends to infinity as $\nu \to 0.5$ (incompressible).
- The constrained (one-dimensional strain) modulus is $E(1 - \nu)/[(1 + \nu)(1 - 2\nu)] = \lambda_L + 2G$.
- Example: $E = 200$ GPa, $\nu = 0.30$. Then $G = 76.92$ GPa, $\lambda_L = 115.4$ GPa, $K_b = 166.7$ GPa. A bar held so that only $\varepsilon_x = 0.001$ is nonzero has $\sigma_x = 269.2$ MPa and $\sigma_y = \sigma_z = 115.4$ MPa. For $\nu = 0.45$ the bulk modulus is $K_b = 666.7$ GPa.

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\varepsilon_{ij}$ | strain tensor component | dimensionless |
| $\sigma_{ij}$ | stress tensor component | Pa |
| $\sigma_{kk}$ | trace of the stress tensor (sum of normal components) | Pa |
| $\varepsilon_{kk}$ | trace of the strain tensor (volumetric strain) | dimensionless |
| $E$ | Young's modulus | Pa |
| $\nu$ | Poisson's ratio | dimensionless |
| $G$ | shear modulus | Pa |
| $\lambda_L$ | first Lame parameter | Pa |
| $K_b$ | bulk modulus | Pa |
| $\delta_{ij}$ | Kronecker delta | dimensionless |

Holds when: linear elastic, isotropic, small strain, isothermal (see the next entry for temperature change).
Breaks when: the material is anisotropic (rolled sheet, fibre composites, wood, single crystals), yields, or strains are large. For $\nu$ near $0.5$ numerical models lock, and mixed formulations are needed.
Source and basis: derived from superposing uniaxial responses (stretching along one axis with lateral contraction $\nu$) and from isotropy, which ties $G$ to $E$ and $\nu$; the uniaxial case is in [Axial and torsion](04-axial-and-torsion.md).

```verify
E = q(200, "GPa")
nu = q(0.30, "")
G = E / (2 * (1 + nu))
lam = E * nu / ((1 + nu) * (1 - 2 * nu))
expect(G, "76.92 GPa")
expect(lam, "115.4 GPa")
expect(E / (3 * (1 - 2 * nu)), "166.7 GPa")
expect(lam + 2 * G / 3, "166.7 GPa")
ex = q(0.001, "")
expect((lam + 2 * G) * ex, "269.2 MPa")
expect(lam * ex, "115.4 MPa")
expect(E / (3 * (1 - 2 * q(0.45, ""))), "666.7 GPa")
```

### Thermal strain

A free temperature change $\Delta T$ stretches an isotropic material equally in all directions without shear. Stress appears only when the expansion is constrained.

$$\varepsilon_{ij} = \frac{1 + \nu}{E}\,\sigma_{ij} - \frac{\nu}{E}\,\sigma_{kk}\,\delta_{ij} + \alpha_L\,\Delta T\,\delta_{ij}$$

- Fully constrained bar, one direction: $\sigma = -E\alpha_L\Delta T$. Plate constrained in its plane (equal biaxial): $\sigma = -E\alpha_L\Delta T/(1 - \nu)$. Block constrained in all three directions: $\sigma = -E\alpha_L\Delta T/(1 - 2\nu)$.
- Typical linear expansion coefficient $\alpha_L$ of carbon steel is about $12 \times 10^{-6}\ 1/\text{K}$ (range roughly 11 to 13). Aluminium alloys are about twice that.
- Example: steel, $E = 200$ GPa, $\nu = 0.30$, $\alpha_L = 12 \times 10^{-6}\ 1/\text{K}$ (typical), heated by 50 K. Compressive stress in the constrained bar: 120 MPa. In the constrained plate: 171.4 MPa. In the fully constrained block: 300 MPa.

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\alpha_L$ | coefficient of linear thermal expansion | $1/\text{K}$ |
| $\Delta T$ | temperature change (kelvin and degrees Celsius steps are equal) | K |
| $\sigma$ | constrained thermal stress | Pa |
| $E$ | Young's modulus | Pa |
| $\nu$ | Poisson's ratio | dimensionless |
| $\varepsilon_{ij}$, $\sigma_{ij}$ | strain and stress tensor components | dimensionless |
| $\sigma_{kk}$ | trace of the stress tensor | Pa |
| $\delta_{ij}$ | Kronecker delta | dimensionless |

Holds when: $\alpha_L$ is constant over the temperature range, the material is isotropic and elastic, and the temperature field is uniform or the constraint is as stated.
Breaks when: the stress reaches yield, $\alpha_L$ varies strongly with temperature, the material is anisotropic, or temperature varies through the body (the self-equilibrating gradient stress then needs its own solution).
Source and basis: derived from superposing a free thermal strain onto the elastic strain; $\alpha_L$ is a measured material property, so the value used here is labelled typical.

```verify
E = q(200, "GPa")
nu = q(0.30, "")
al = q(12e-6, "1/K")
dT = q(50, "K")
expect(E * al * dT, "120 MPa")
expect(E * al * dT / (1 - nu), "171.4 MPa")
expect(E * al * dT / (1 - 2 * nu), "300 MPa")
```

## Equilibrium and compatibility equations

### Equilibrium equations

For a body in equilibrium, every infinitesimal element satisfies force balance. In index notation, with body force per volume $b_i$:

$$\sigma_{ij,j} + b_i = 0$$

- Written out for $x$: $\partial\sigma_x/\partial x + \partial\tau_{xy}/\partial y + \partial\tau_{xz}/\partial z + b_x = 0$, with the matching cyclic forms for $y$ and $z$.
- Example: a vertical steel bar hung from its top, length $L$, density $\rho$, in Earth gravity ($g = 9.80665\ \text{m/s}^2$, standard). Balance along $z$ (up from the free end) gives $d\sigma_z/dz = \rho g$, so $\sigma_z = \rho g z$ and the peak is $\rho g L$ at the top. For $\rho = 7850\ \text{kg/m}^3$ (typical steel) and $L = 100$ m, the peak is 7.698 MPa. A yield strength of 250 MPa is reached at 3248 m of length.

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\sigma_{ij,j}$ | divergence of the stress tensor | $\text{Pa/m}$ |
| $b_i$ | body force per unit volume | $\text{N/m}^{3}$ |
| $\sigma_z$ | axial stress in the hanging bar | Pa |
| $\rho$ | density | $\text{kg/m}^{3}$ |
| $g$ | local gravitational acceleration | $\text{m/s}^{2}$ |
| $z$ | height above the free end | m |
| $L$ | bar length | m |

Holds when: static equilibrium with small deformation (the equations are written on the undeformed geometry); a dynamic problem adds $-\rho\,\partial^2 u_i/\partial t^2$ to the left side.
Breaks when: deformations are large enough to change the geometry the load acts on, or the material carries couple stresses.
Source and basis: derived from force balance on an infinitesimal element; moment balance gives $\sigma_{ij} = \sigma_{ji}$.

```verify
rho = q(7850, "kg/m^3")
g = q(9.80665, "m/s^2", of="g_standard")
L = q(100, "m")
expect(rho * g * L, "7.698 MPa")
expect(q(250, "MPa") / (rho * g), "3248 m")
```

### Strain-displacement relations and compatibility

Six strains come from three displacement functions, so the strains cannot be chosen freely. **Compatibility** is the condition that a strain field comes from a continuous displacement field.

$$\frac{\partial^2 \varepsilon_x}{\partial y^2} + \frac{\partial^2 \varepsilon_y}{\partial x^2} = \frac{\partial^2 \gamma_{xy}}{\partial x\,\partial y}$$

- The strain-displacement relations are $\varepsilon_x = \partial u/\partial x$, $\varepsilon_y = \partial v/\partial y$, $\gamma_{xy} = \partial u/\partial y + \partial v/\partial x$.
- In plane problems the stress can be derived from an Airy stress function $\phi$ with $\sigma_x = \partial^2\phi/\partial y^2$, $\sigma_y = \partial^2\phi/\partial x^2$, $\tau_{xy} = -\partial^2\phi/\partial x\,\partial y$. Compatibility then requires $\nabla^4\phi = 0$ with no body force.
- Example: the field $\varepsilon_x = a y^2$, $\varepsilon_y = a x^2$, $\gamma_{xy} = 4 a x y$ with $a = 2 \times 10^{-6}\ 1/\text{m}^2$ gives $2a + 2a = 8 \times 10^{-6}\ 1/\text{m}^2$ on the left and $4a = 8 \times 10^{-6}\ 1/\text{m}^2$ on the right, so it is compatible. Changing $\gamma_{xy}$ to $2axy$ makes the right side $4 \times 10^{-6}\ 1/\text{m}^2$, and no displacement field produces it.

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\varepsilon_x$, $\varepsilon_y$ | normal strains | dimensionless |
| $\gamma_{xy}$ | engineering shear strain | rad |
| $u$, $v$ | displacements along $x$ and $y$ | m |
| $a$ | amplitude of the example strain field | $1/\text{m}^{2}$ |
| $\phi$ | Airy stress function | N |

Holds when: small strain and a simply connected body.
Breaks when: the region has holes (extra conditions on the displacement around each hole are needed), or strains are large.
Source and basis: derived from the strain-displacement relations by eliminating $u$ and $v$ through mixed second derivatives.

```verify
a = q(2e-6, "1/m^2")
expect(2 * a + 2 * a, "8e-6 1/m^2")
expect(4 * a, "8e-6 1/m^2")
check(2 * a + 2 * a != 2 * a, "the altered field with 2axy is incompatible")
```

## Energy methods

### Strain energy

**Strain energy** $U$ is the work stored elastically when a body is loaded, and a linear elastic body returns it on unloading.

$$U = \tfrac{1}{2}\int_V \sigma_{ij}\,\varepsilon_{ij}\,dV \qquad U = \int_0^L \left[\frac{N^2}{2EA} + \frac{M^2}{2EI} + \frac{T^2}{2GJ} + \frac{\kappa V^2}{2GA}\right]dx$$

- The shear form factor $\kappa$ is $6/5$ for a rectangular section and $10/9$ for a solid circle; for an I-beam use $A$ equal to the web area and $\kappa \approx 1$.
- Example: cantilever, tip load $P = 1$ kN, $L = 1$ m, $E = 200$ GPa, $\nu = 0.30$, rectangle 20 mm by 40 mm (depth 40 mm). Bending energy $U = P^2 L^3/(6EI) = 7.8125$ J, so $\delta = 2U/P = 15.625$ mm, equal to $PL^3/(3EI)$. The shear contribution to deflection is $\kappa P L/(GA) = 0.0195$ mm, 0.0012 of the bending deflection.

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $U$ | strain energy | J |
| $V$ (in $dV$) | volume | $\text{m}^{3}$ |
| $N$ | axial force along the member | N |
| $V$ | shear force along the member | N |
| $T$ | torque along the member | N m |
| $M$ | bending moment along the member | N m |
| $E$, $G$ | Young's and shear modulus | Pa |
| $A$ | cross-section area (web area for an I-beam in shear) | $\text{m}^{2}$ |
| $I$ | second moment of area | $\text{m}^{4}$ |
| $J$ | polar second moment of area (circular section) | $\text{m}^{4}$ |
| $\kappa$ | shear form factor | dimensionless |
| $L$ | member length | m |
| $P$ | tip load | N |
| $\delta$ | tip deflection | m |

Holds when: linear elastic, small deflection, prismatic or slowly varying sections, torsion of circular sections (use the torsion constant $J_t$ below otherwise).
Breaks when: the section is thin-walled open (warping energy matters), the member is short and deep (beam theory fails), or the material yields.
Source and basis: derived from the work done by loads that rise in proportion to displacement (one half of load times displacement); beam stress relations in [Bending and buckling](05-bending-and-buckling.md).

```verify
P = q(1, "kN")
L = q(1, "m")
E = q(200, "GPa")
nu = q(0.30, "")
I = q(20, "mm") * q(40, "mm")**3 / 12
A = q(20, "mm") * q(40, "mm")
U = P**2 * L**3 / (6 * E * I)
expect(U, "7.8125 J")
expect(2 * U / P, "15.625 mm")
expect(P * L**3 / (3 * E * I), "15.625 mm")
G = E / (2 * (1 + nu))
expect(1.2 * P * L / (G * A), "0.0195 mm")
expect(1.2 * P * L / (G * A) / (P * L**3 / (3 * E * I)), "0.0012")
```

### Castigliano's theorems

Both theorems turn derivatives of strain energy into loads or displacements.

$$\delta_i = \frac{\partial U}{\partial P_i} \qquad P_i = \frac{\partial U}{\partial \delta_i}$$

- Second theorem (left): write $U$ as a function of the loads $P_i$; the derivative is the displacement at that load, in its direction. For a point where no load acts, add a dummy load $Q$, differentiate, then set $Q = 0$: $\delta = \int (M/EI)(\partial M/\partial Q)\,dx$.
- First theorem (right): write $U$ as a function of the displacements; the derivative is the generalized force.
- Example: cantilever of length $L$ with uniform load $w$ and a dummy tip load $Q$. With $x$ from the free end, $M = -(wx^2/2 + Qx)$ and $\partial M/\partial Q = -x$, so $\delta = wL^4/(8EI)$. For $w = 5$ kN/m, $L = 2$ m, and a 100 mm by 200 mm steel section ($E = 200$ GPa) this is 0.75 mm.

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $U$ | strain energy as a function of the loads (second theorem) or displacements (first theorem) | J |
| $P_i$ | generalized force, force or moment | N |
| $\delta_i$ | generalized displacement in the direction of $P_i$, displacement or rotation | m |
| $Q$ | dummy load placed where the displacement is wanted | N |
| $M$ | bending moment as a function of $x$ and $Q$ | N m |
| $w$ | uniform load per length | N/m |
| $E$ | Young's modulus | Pa |
| $I$ | second moment of area | $\text{m}^{4}$ |

Holds when: linear elastic response, small displacement, unyielding supports (or support energy included), and temperature fixed.
Breaks when: material or geometry is nonlinear (Engesser's extension applies to nonlinear elastic material), the supports settle, or $U$ is written in terms of the wrong variables (using the second theorem on $U(\delta)$ gives wrong answers).
Source and basis: derived from conservation of energy for a conservative elastic system; the unit-load method below is the same result written with virtual loads.

```verify
w = q(5, "kN/m")
L = q(2, "m")
E = q(200, "GPa")
I = q(100, "mm") * q(200, "mm")**3 / 12
expect(w * L**4 / (8 * E * I), "0.75 mm")
```

### Unit-load method and principle of virtual work

The **principle of virtual work** says that for a body in equilibrium, the work of the external loads on any compatible virtual displacement equals the work of the internal stresses on the matching virtual strain. The **unit-load method** applies it with a virtual load of 1 at the point and direction of the wanted displacement.

$$\delta\,(1) = \int_V \bar{\sigma}_{ij}\,\varepsilon_{ij}\,dV \qquad \delta = \int_0^L \frac{M m}{EI}\,dx + \sum_i \frac{N_i n_i L_i}{E_i A_i}$$

- $M$ and $N_i$ come from the real loads; $m$ and $n_i$ come from a unit load applied at the wanted point. Add $\int T t/(GJ)\,dx$ and $\int \kappa V v/(GA)\,dx$ when torsion or shear matters.
- Virtual displacements also find reactions: remove one support, give the structure a rigid-body virtual motion, and balance the work of that reaction against the load. Simply supported span 4 m, load 12 kN at 1 m from the left: a virtual rotation $\theta$ about the left pin gives $12\,\text{kN} \times 1\,\text{m}\ \theta = R_B \times 4\,\text{m}\ \theta$, so $R_B = 3$ kN.
- Example, two-bar truss: horizontal bar of length $L = 1$ m in compression and inclined bar (length $\sqrt{2}L$) in tension, joined at a joint carrying a downward load $P = 10$ kN. Both bars have $A = 200\ \text{mm}^2$ and $E = 200$ GPa. Bar forces are $\sqrt{2}P$ (tension) and $P$ (compression); the unit load gives $\sqrt{2}$ and $-1$. The vertical deflection is $(2\sqrt{2} + 1)PL/(EA) = 0.957$ mm.

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\delta$ | displacement at the unit-load point, along the unit load | m |
| $\bar{\sigma}_{ij}$ | stress from the unit load | Pa |
| $\varepsilon_{ij}$ | real total strain | dimensionless |
| $M$ | bending moment from the real loads | N m |
| $m$ | bending moment from the unit load | dimensionless |
| $N_i$ | axial force in member $i$ from the real loads | N |
| $n_i$ | axial force in member $i$ from the unit load | dimensionless |
| $L_i$ | length of member $i$ | m |
| $A_i$ | cross-section area of member $i$ | $\text{m}^{2}$ |
| $E_i$ | modulus of member $i$ | Pa |
| $R_B$ | reaction found by virtual work | N |
| $P$ | applied joint load | N |

Holds when: the unit-load integral uses the real total strain, including any initial strain; the energy form agrees with it for linear elastic material with no initial strain. Virtual work itself needs equilibrium and compatibility, small displacement, and pin-jointed members for the truss sum.
Breaks when: joints are stiff and carry bending (add the moment terms), or members buckle or yield.
Source and basis: derived from the principle of virtual work (equilibrium of the real system against compatible virtual displacements).

```verify
P = q(10, "kN")
L = q(1, "m")
A = q(200, "mm^2")
E = q(200, "GPa")
d = (sqrt(2) * P * sqrt(2) * sqrt(2) * L + P * L) / (E * A)
expect(d, "0.957 mm")
expect((2 * sqrt(2) + 1) * P * L / (E * A), "0.957 mm")
expect(q(12, "kN") * q(1, "m") / q(4, "m"), "3 kN")
```

## Statically indeterminate members

### Force method

A member is **statically indeterminate** when equilibrium alone cannot find the reactions. The **force method** removes redundant supports until the structure is determinate, then restores each by requiring the displacement at the cut to match what the support allows (usually zero).

$$\sum_j f_{ij}\,X_j + \Delta_{i0} = 0 \qquad f_{ij} = \int \frac{m_i m_j}{EI}\,dx$$

- $X_j$ are the redundants. $\Delta_{i0}$ is the displacement at redundant $i$ in the released structure under the real loads, and $f_{ij}$ is the displacement at $i$ per unit redundant $j$ (the flexibility). For one redundant, $X = -\Delta_{10}/f_{11}$.
- Count redundants as unknown reactions (plus internal releases) minus the independent equilibrium equations.
- Example: propped cantilever of length $L$, uniform load $w$, prop at the free end taken as the redundant $R_B$. Released tip deflection $\Delta_{10} = -wL^4/(8EI)$ (downward, taking up as positive), $f_{11} = L^3/(3EI)$, so $R_B = 3wL/8$. The fixed-end moment is $wL^2/8$. For $w = 10$ kN/m and $L = 4$ m: $R_B = 15$ kN and $M_A = 20$ kN m.

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $X_j$ | redundant force or moment | N |
| $\Delta_{i0}$ | displacement at redundant $i$ in the released structure under the real loads | m |
| $f_{ij}$ | flexibility, displacement at $i$ per unit redundant at $j$ | m/N |
| $m_i$ | bending moment from a unit redundant $i$ | dimensionless |
| $R_B$ | prop reaction | N |
| $M_A$ | fixed-end moment | N m |
| $w$ | uniform load per length | N/m |
| $L$ | span | m |
| $E$ | Young's modulus | Pa |
| $I$ | second moment of area | $\text{m}^{4}$ |

Holds when: linear elastic, small displacement, supports rigid or with known settlement (put it in $\Delta_{i0}$).
Breaks when: members yield (limit analysis or a nonlinear solver is needed), supports are compliant but treated as rigid, or second-order effects matter.
Source and basis: derived from superposition: the real structure is the released structure under the loads plus the redundants, with compatibility restored at each cut; displacements from the unit-load method above.

```verify
w = q(10, "kN/m")
L = q(4, "m")
RB = 3 * w * L / 8
expect(RB, "15 kN")
expect(w * L**2 / 2 - RB * L, "20 kN m")
expect(w * L**2 / 8, "20 kN m")
```

## Noncircular and thin-walled torsion

### Closed thin-walled sections (Bredt-Batho)

For a single closed cell with thin walls, the shear flow $q$ (force per unit length of wall, N/m) is constant around the cell.

$$q = \frac{T}{2A_m} \qquad \tau = \frac{T}{2A_m t} \qquad \phi = \frac{TL}{4A_m^2 G}\oint \frac{ds}{t} \qquad J_t = \frac{4A_m^2}{\oint ds/t}$$

- $A_m$ is the area enclosed by the wall midline. The stress is largest where the wall is thinnest.
- Example: square tube, mean side 50 mm, wall 3 mm, $T = 500$ N m, $L = 1$ m, $G = 80$ GPa. Then $A_m = 2500\ \text{mm}^2$, $\tau = 33.33$ MPa, $J_t = 3.75 \times 10^{-7}\ \text{m}^4$, and $\phi = 0.01667$ rad (0.955 degrees).

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $q$ | shear flow | N/m |
| $T$ | torque | N m |
| $A_m$ | area enclosed by the wall midline | $\text{m}^{2}$ |
| $\tau$ | shear stress in the wall | Pa |
| $t$ | wall thickness | m |
| $\phi$ | angle of twist over length $L$ | rad |
| $L$ | member length | m |
| $G$ | shear modulus | Pa |
| $ds$ | element of midline length | m |
| $J_t$ | torsion constant | $\text{m}^{4}$ |

Holds when: wall thickness is small against the cell size, a single closed cell, linear elastic, and the ends are free to warp (or the member is long).
Breaks when: multiple cells (each needs its own shear flow and a twist-compatibility equation), the walls are thick, ends are restrained against warping (warping torsion adds stiffness), or thin walls buckle in shear.
Source and basis: derived from equilibrium of a wall segment (constant $q$), moment balance about any point ($T = 2A_m q$), and strain energy for the twist; circular shafts are in [Axial and torsion](04-axial-and-torsion.md).

```verify
Am = q(50, "mm")**2
t = q(3, "mm")
T = q(500, "N m")
L = q(1, "m")
G = q(80, "GPa")
expect(Am, "2500 mm^2")
expect(T / (2 * Am * t), "33.33 MPa")
Jt = 4 * Am**2 / (4 * q(50, "mm") / t)
expect(Jt, "3.75e-7 m^4")
expect(T * L / (G * Jt), "0.01667 rad")
expect(T * L / (G * Jt), "0.955 deg")
```

### Open thin-walled sections and the rectangle

An **open section** (a slit tube, an I, a channel, an angle) has no closed loop, so the shear flows around the walls cancel across the thickness and the section is far softer in twist.

$$J_t = \frac{1}{3}\sum_i b_i t_i^3 \qquad \tau_{\max} = \frac{T\,t_{\max}}{J_t} \qquad \phi = \frac{TL}{G J_t}$$

- The rectangle $b \times t$ follows from the Saint-Venant series: $J_t = \dfrac{b t^3}{3}\left[1 - \dfrac{192\,t}{\pi^5 b}\sum_{n=1,3,5,\ldots}\dfrac{1}{n^5}\tanh\dfrac{n\pi b}{2t}\right]$. The bracket tends to 1 for $b/t \gg 1$. It gives $J_t = 0.1406\,t^4$ for a square and $0.3123\,b t^3$ for $b/t = 10$.
- Example: cut the square tube above along its length. The slit tube has $b = 200$ mm (unrolled midline) and $t = 3$ mm, so $J_t = 1.8 \times 10^{-9}\ \text{m}^4$, which is 208 times smaller than the closed tube's $3.75 \times 10^{-7}\ \text{m}^4$.

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $J_t$ | torsion constant | $\text{m}^{4}$ |
| $b_i$ | length of strip $i$ of the section | m |
| $t_i$ | thickness of strip $i$ | m |
| $t_{\max}$ | thickest strip | m |
| $\tau_{\max}$ | peak shear stress, on the surface of the thickest strip | Pa |
| $T$ | torque | N m |
| $\phi$ | angle of twist | rad |
| $L$ | member length | m |
| $G$ | shear modulus | Pa |

Holds when: each strip has $b_i \gg t_i$ (about $b_i/t_i \ge 10$ for the one-third formula), linear elastic, free warping.
Breaks when: strips are not slender, fillets at junctions raise the local stress above $\tau_{\max}$, or warping is restrained (use warping-torsion theory).
Source and basis: derived from the Prandtl stress function for torsion (membrane analogy) with the thin-strip limit; the series is the Saint-Venant solution for a rectangle.

```verify
b = q(200, "mm")
t = q(3, "mm")
Jt = b * t**3 / 3
expect(Jt, "1.8e-9 m^4")
expect(q(3.75e-7, "m^4") / Jt, "208")
bt = 10
x1 = bt * pi / 2
x3 = 3 * x1
x5 = 5 * x1
f = 1 - 192 / pi**5 / bt * ((exp(2 * x1) - 1) / (exp(2 * x1) + 1) + (exp(2 * x3) - 1) / (exp(2 * x3) + 1) / 243 + (exp(2 * x5) - 1) / (exp(2 * x5) + 1) / 3125)
expect(f / 3, "0.3123")
y1 = pi / 2
y3 = 3 * y1
y5 = 5 * y1
sq = 1 - 192 / pi**5 * ((exp(2 * y1) - 1) / (exp(2 * y1) + 1) + (exp(2 * y3) - 1) / (exp(2 * y3) + 1) / 243 + (exp(2 * y5) - 1) / (exp(2 * y5) + 1) / 3125)
expect(sq / 3, "0.1406")
```

## Thick-walled cylinders

### Lame equations

A cylinder is **thick-walled** when the wall thickness is more than about one tenth of the inner radius, so stress varies across the wall.

$$\sigma_r = \frac{p_i a^2 - p_o b^2}{b^2 - a^2} - \frac{(p_i - p_o)\,a^2 b^2}{(b^2 - a^2)\,r^2} \qquad \sigma_\theta = \frac{p_i a^2 - p_o b^2}{b^2 - a^2} + \frac{(p_i - p_o)\,a^2 b^2}{(b^2 - a^2)\,r^2}$$

$$\sigma_z = \frac{p_i a^2 - p_o b^2}{b^2 - a^2} \quad \text{(closed ends)}$$

- Internal pressure only: the hoop stress is largest at the bore, $\sigma_\theta(a) = p_i (b^2 + a^2)/(b^2 - a^2)$, and $\sigma_r(a) = -p_i$. Hoop stress at the outer surface is $2 p_i a^2/(b^2 - a^2)$.
- External pressure only: the largest hoop stress is also at the bore, $\sigma_\theta(a) = -2 p_o b^2/(b^2 - a^2)$.
- Tresca yield at the bore under internal pressure begins at $p_y = S_y (b^2 - a^2)/(2 b^2)$.
- Example: $a = 50$ mm, $b = 75$ mm, $p_i = 60$ MPa, $p_o = 0$. Then $\sigma_\theta(a) = 156$ MPa, $\sigma_\theta(b) = 96$ MPa, $\sigma_r(a) = -60$ MPa, $\sigma_z = 48$ MPa, and $\sigma_{vm}(a) = 187.1$ MPa. The thin-wall formula $p r/t$ at the inner radius would give 120 MPa, an error of 0.23 of the true value. For $S_y = 500$ MPa, $p_y = 138.9$ MPa.

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\sigma_r$, $\sigma_\theta$, $\sigma_z$ | radial, hoop, and axial stress | Pa |
| $p_i$, $p_o$ | internal and external pressure, gauge relative to the same reference | Pa |
| $a$, $b$ | inner and outer radius | m |
| $r$ | radius at the point, $a \le r \le b$ | m |
| $S_y$ | tensile yield strength | Pa |
| $p_y$ | internal pressure at first Tresca yield | Pa |

Holds when: linear elastic, isotropic, uniform wall, long cylinder away from ends and nozzles, axisymmetric loading. The axial stress shown applies to closed ends with the cylinder free to stretch; for open ends $\sigma_z = 0$.
Breaks when: the pressure exceeds first yield (the plastic zone changes the profile; autofrettage and fully plastic analyses are separate), the cylinder is short, there are stress concentrations at cross-bores, or the wall is thin and the thin-wall formula in [thin-walled pressure vessels](reference-mechanics.md#thin-walled-pressure-vessels) is adequate.
Source and basis: derived from the radial equilibrium equation $d(r\sigma_r)/dr = \sigma_\theta$ with plane-strain or plane-stress compatibility, which gives $\sigma_r = A - B/r^2$ and $\sigma_\theta = A + B/r^2$, and from the pressure boundary conditions.

```verify
a = q(50, "mm")
b = q(75, "mm")
p = q(60, "MPa")
Y = q(500, "MPa")
sth = p * (b**2 + a**2) / (b**2 - a**2)
sz = p * a**2 / (b**2 - a**2)
sr = -p
expect(sth, "156 MPa")
expect(2 * p * a**2 / (b**2 - a**2), "96 MPa")
expect(sz, "48 MPa")
expect(sqrt(0.5 * ((sth - sr)**2 + (sr - sz)**2 + (sz - sth)**2)), "187.1 MPa")
expect(p * a / (b - a), "120 MPa")
expect((sth - p * a / (b - a)) / sth, "0.23")
expect(Y * (b**2 - a**2) / (2 * b**2), "138.9 MPa")
```

### Shrink-fit interface pressure

A **shrink fit** joins an inner member (outer radius $c$ before assembly, inner radius $a$, with $a = 0$ for a solid shaft) to an outer member (inner radius $c$, outer radius $b$) with a radial interference $\delta_r$. The outer member stretches and the inner one shrinks until the surfaces meet at the interface pressure $p$.

$$p = \frac{\delta_r}{c\left\{\dfrac{1}{E_o}\left[\dfrac{b^2 + c^2}{b^2 - c^2} + \nu_o\right] + \dfrac{1}{E_i}\left[\dfrac{c^2 + a^2}{c^2 - a^2} - \nu_i\right]\right\}}$$

- For the same material the Poisson terms cancel, and $p = E\,\delta_r \Big/ \left(c\left[\dfrac{b^2 + c^2}{b^2 - c^2} + \dfrac{c^2 + a^2}{c^2 - a^2}\right]\right)$.
- The hoop stress in the outer member at the interface is $p\,(b^2 + c^2)/(b^2 - c^2)$, the highest in that member.
- Example: steel hub on a solid steel shaft, $c = 25$ mm, $b = 50$ mm, $a = 0$, radial interference $\delta_r = 0.020$ mm, $E = 200$ GPa. The bracket is $2.667$, so $p = 60$ MPa, and the hub hoop stress at the bore is 100 MPa.
- The torque the fit can carry (friction at the interface) is a design use; see [design/reference-machine-design.md](../design/reference-machine-design.md).

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $p$ | interface pressure after assembly | Pa |
| $\delta_r$ | radial interference (difference of the interface radii before assembly) | m |
| $a$ | inner radius of the inner member (0 for a solid shaft) | m |
| $c$ | nominal interface radius | m |
| $b$ | outer radius of the outer member | m |
| $E_o$, $E_i$ | modulus of the outer and inner member | Pa |
| $\nu_o$, $\nu_i$ | Poisson's ratio of the outer and inner member | dimensionless |

Holds when: both members elastic, plane stress (or members free to change length), same temperature, no surface roughness flattening, interface remains fully in contact along its length.
Breaks when: members yield at the interface, interference is large against surface roughness (roughness removes part of $\delta_r$), the hub is short (pressure peaks at its ends), or the members are at different temperatures at assembly or in service.
Source and basis: derived from the Lame displacement $u_r = (r/E)(\sigma_\theta - \nu\sigma_r)$ evaluated at the interface for internal pressure on the outer member and external pressure on the inner one.

```verify
E = q(200, "GPa")
c = q(25, "mm")
b = q(50, "mm")
d = q(0.020, "mm")
br = (b**2 + c**2) / (b**2 - c**2) + 1
expect(br, "2.667")
p = E * d / (c * br)
expect(p, "60 MPa")
expect(p * (b**2 + c**2) / (b**2 - c**2), "100 MPa")
```

## Rotating disks

### Constant-thickness disk

A thin disk spinning at angular speed $\omega$ is loaded by its own inertia. Radial acceleration $\omega^2 r$ gives an outward body force $\rho\omega^2 r$.

$$\sigma_r = \frac{3 + \nu}{8}\rho\omega^2\left(a^2 + b^2 - \frac{a^2 b^2}{r^2} - r^2\right) \qquad \sigma_\theta = \frac{3 + \nu}{8}\rho\omega^2\left(a^2 + b^2 + \frac{a^2 b^2}{r^2} - \frac{1 + 3\nu}{3 + \nu}\,r^2\right)$$

- Solid disk: set $a = 0$. The stress is largest at the centre, where $\sigma_r = \sigma_\theta = \dfrac{3 + \nu}{8}\rho\omega^2 b^2$.
- Annular disk: the largest stress is the hoop stress at the bore, $\sigma_\theta(a) = \dfrac{3 + \nu}{4}\rho\omega^2\left(b^2 + \dfrac{1 - \nu}{3 + \nu}a^2\right)$. A small central hole nearly doubles the peak stress.
- Stress scales with $\rho\omega^2 b^2$, the square of rim speed times density.
- Example: steel disk ($\rho = 7850\ \text{kg/m}^3$ typical, $\nu = 0.30$), $b = 0.2$ m, $6000\ \text{rev/min}$ ($\omega = 628.3$ rad/s). Solid: $\sigma = 51.13$ MPa. With a bore $a = 0.05$ m: $\sigma_\theta(a) = 103.6$ MPa.

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\sigma_r$, $\sigma_\theta$ | radial and hoop stress | Pa |
| $\rho$ | density | $\text{kg/m}^{3}$ |
| $\omega$ | angular speed | rad/s |
| $\nu$ | Poisson's ratio | dimensionless |
| $a$, $b$ | bore radius and outer radius | m |
| $r$ | radius at the point | m |

Holds when: the disk is thin and of uniform thickness (plane stress), isotropic, linear elastic, at uniform temperature, with free rim and bore (no shrink-fit pressure or blade load).
Breaks when: thickness varies with radius (numerical or series solutions), the rim carries blade or bolt loads, temperature varies through the disk (add thermal stress), yield is reached (burst speed needs a plastic analysis), or the disk is thick.
Source and basis: derived from the radial equilibrium equation with body force $\rho\omega^2 r$ and plane-stress compatibility, with zero radial stress at both free surfaces. Check that $\sigma_r = 0$ at $r = a$ and $r = b$ by substitution.

```verify
rho = q(7850, "kg/m^3")
nu = q(0.30, "")
b = q(0.2, "m")
a = q(0.05, "m")
w = q(6000, "rev/min")
expect(w, "628.3 rad/s")
k = (3 + nu) / 8 * rho * w**2
expect(k * b**2, "51.13 MPa")
expect(2 * k * (b**2 + (1 - nu) / (3 + nu) * a**2), "103.6 MPa")
sr_a = k * (a**2 + b**2 - a**2 * b**2 / a**2 - a**2)
check(abs(sr_a) < q(1, "Pa"), "radial stress is zero at the bore")
```

## Classical plate bending

### Flexural rigidity and the Kirchhoff plate equation

A **plate** is a flat body whose thickness $h$ is small against its other dimensions, loaded across its face. Its bending stiffness per unit width is the **flexural rigidity** $D$.

$$D = \frac{E h^3}{12\,(1 - \nu^2)} \qquad \nabla^4 w = \frac{q}{D} \qquad \sigma_{\max} = \frac{6 M}{h^2}$$

- $M$ is the bending moment per unit width. Moments follow from the deflection: $M_x = -D\left(\partial^2 w/\partial x^2 + \nu\,\partial^2 w/\partial y^2\right)$.
- The $1 - \nu^2$ factor makes a plate stiffer than a beam strip of the same thickness, because the neighbouring strips resist lateral contraction.
- Deflection scales with $q/D$, so doubling the thickness divides it by eight.
- Example: steel plate $h = 10$ mm, $E = 200$ GPa, $\nu = 0.30$. Then $D = 18\,315\ \text{N m}$.

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $D$ | flexural rigidity | N m |
| $E$ | Young's modulus | Pa |
| $h$ | plate thickness | m |
| $\nu$ | Poisson's ratio | dimensionless |
| $w$ | transverse deflection | m |
| $q$ | transverse pressure load | Pa |
| $\nabla^4 w$ | biharmonic operator applied to $w$ | $1/\text{m}^{3}$ |
| $M$ | bending moment per unit width | N |
| $\sigma_{\max}$ | peak bending stress at the surface | Pa |

Holds when: $h$ is small against the span (about span over thickness 10 or more), deflection is small against $h$ (about half of $h$ or less, a rule of thumb), isotropic and linear elastic.
Breaks when: deflection reaches the order of $h$ (membrane stress stiffens the plate; use large-deflection theory), the plate is thick (shear deformation, use Mindlin theory), or the material is anisotropic.
Source and basis: derived from plane sections remaining plane and normal to the midsurface (Kirchhoff hypotheses) and moment equilibrium of a plate element; the beam analogue is in [Bending and buckling](05-bending-and-buckling.md).

```verify
E = q(200, "GPa")
nu = q(0.30, "")
h = q(10, "mm")
expect(E * h**3 / (12 * (1 - nu**2)), "18315 N m")
```

### Circular plates under uniform pressure

For a circular plate of radius $a$ and uniform pressure $q$:

$$\text{simply supported: } w_{\max} = \frac{5 + \nu}{1 + \nu}\,\frac{q a^4}{64 D},\ \sigma_{\max} = \frac{3(3 + \nu)\,q a^2}{8 h^2} \text{ (centre)}$$

$$\text{clamped: } w_{\max} = \frac{q a^4}{64 D},\ \sigma_{\max} = \frac{3 q a^2}{4 h^2} \text{ (radial, at the edge)},\ \sigma_{\text{centre}} = \frac{3(1 + \nu)\,q a^2}{8 h^2}$$

- Clamping cuts the deflection by the factor $(1 + \nu)/(5 + \nu)$ (about a quarter for steel) and the peak stress by roughly 40 percent.
- Example: steel plate, $a = 250$ mm, $h = 10$ mm, $q = 100$ kPa, $D = 18\,315\ \text{N m}$, $\nu = 0.30$. Simply supported: $w_{\max} = 1.359$ mm and $\sigma_{\max} = 77.34$ MPa. Clamped: $w_{\max} = 0.333$ mm and edge stress 46.88 MPa.

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $w_{\max}$ | deflection at the centre | m |
| $\sigma_{\max}$ | peak bending stress | Pa |
| $q$ | uniform pressure | Pa |
| $a$ | plate radius | m |
| $h$ | plate thickness | m |
| $D$ | flexural rigidity | N m |
| $\nu$ | Poisson's ratio | dimensionless |

Holds when: Kirchhoff conditions above, uniform pressure over the full face, ideal support (simple support free to rotate and slide inward; clamp rigid).
Breaks when: deflection is not small against $h$, the real edge is partly fixed (the answer lies between the two cases, and the clamped value can be far from a bolted flange), or the load is concentrated.
Source and basis: derived from the axisymmetric Kirchhoff equation $\nabla^4 w = q/D$ integrated with the stated edge conditions; the combined formulas are tabulated in Roark's formulas (named under Further reference).

```verify
E = q(200, "GPa")
nu = q(0.30, "")
a = q(250, "mm")
h = q(10, "mm")
P = q(100, "kPa", of="none")
D = E * h**3 / (12 * (1 - nu**2))
expect(D, "18315 N m")
expect((5 + nu) / (1 + nu) * P * a**4 / (64 * D), "1.359 mm")
expect(3 * (3 + nu) * P * a**2 / (8 * h**2), "77.34 MPa")
expect(P * a**4 / (64 * D), "0.333 mm")
expect(3 * P * a**2 / (4 * h**2), "46.88 MPa")
```

## Membrane shells

### Membrane equations and the cone

A **shell of revolution** is a thin curved wall whose midsurface is generated by rotating a curve about an axis. In **membrane theory** the wall carries load only by in-plane stress, with no bending. The principal radii of curvature are $R_\phi$ (meridional) and $R_\theta$ (the distance along the normal to the axis).

$$\frac{\sigma_\phi}{R_\phi} + \frac{\sigma_\theta}{R_\theta} = \frac{p}{t}$$

- The cylinder ($R_\phi \to \infty$, $R_\theta = R$) and the sphere ($R_\phi = R_\theta = R$) are covered in [thin-walled pressure vessels](reference-mechanics.md#thin-walled-pressure-vessels).
- Cone of half-angle $\alpha$ under internal pressure, with $r$ the distance from the axis: $\sigma_\theta = \dfrac{p\,r}{t\cos\alpha}$ and $\sigma_\phi = \dfrac{p\,r}{2\,t\cos\alpha}$. The hoop stress grows linearly with $r$ and is largest at the large end.
- Example: $\alpha = 30$ degrees, $r = 0.5$ m, $p = 1$ MPa, $t = 5$ mm. Then $\sigma_\theta = 115.5$ MPa and $\sigma_\phi = 57.7$ MPa.

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\sigma_\phi$ | meridional stress | Pa |
| $\sigma_\theta$ | hoop stress | Pa |
| $R_\phi$ | radius of curvature of the meridian | m |
| $R_\theta$ | radius of curvature perpendicular to the meridian (length of the normal to the axis) | m |
| $p$ | pressure difference across the wall | Pa |
| $t$ | wall thickness | m |
| $\alpha$ | cone half-angle | rad |
| $r$ | distance from the axis of revolution | m |

Holds when: thin wall (thickness small against both radii), smooth varying curvature, load that varies slowly, and boundaries that let the shell deform as the membrane stresses demand.
Breaks when: there are junctions, supports, flanges, or changes of thickness (bending arises; see the next entry), concentrated loads, or compressive membrane stress (buckling governs).
Source and basis: derived from force balance on a small element of the shell; the cone forms come from $R_\phi \to \infty$, $R_\theta = r/\cos\alpha$, and axial equilibrium of the cut cone.

```verify
al = q(30, "deg")
r = q(0.5, "m")
p = q(1, "MPa")
t = q(5, "mm")
expect(p * r / (t * cos(al)), "115.5 MPa")
expect(p * r / (2 * t * cos(al)), "57.7 MPa")
```

### Where membrane theory fails: the bending boundary layer

At a rigid support, a flange, or a change of shell geometry, the membrane deformation does not fit the boundary, so local bending moments appear. For a cylinder they decay with distance $x$ from the discontinuity as $e^{-\beta x}$ with a wavelength-like length:

$$\beta = \left[\frac{3(1 - \nu^2)}{R^2 t^2}\right]^{1/4} \qquad \ell = \frac{\pi}{\beta} \approx 2.44\sqrt{R t} \quad (\nu = 0.30)$$

- Bending stresses at the junction can exceed the membrane stress several times; they act over a length of order $\sqrt{R t}$ only.
- Example: $R = 0.5$ m, $t = 10$ mm, $\nu = 0.30$. Then $\beta = 18.18\ 1/\text{m}$ and $\ell = 0.1728$ m, which is 2.44 times $\sqrt{Rt} = 0.0707$ m.

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\beta$ | decay constant of the edge-bending solution | $1/\text{m}$ |
| $\ell$ | length over which edge bending acts | m |
| $R$ | mean radius of the cylinder | m |
| $t$ | wall thickness | m |
| $\nu$ | Poisson's ratio | dimensionless |

Holds when: a long thin cylinder, linear elastic, axisymmetric edge loading.
Breaks when: the shell is thick, the edge disturbances from two ends overlap (short cylinder), or the geometry is not a cylinder (the form changes, though the order $\sqrt{Rt}$ remains).
Source and basis: derived from the beam on elastic foundation analogy: hoop stiffness acts as a continuous elastic foundation of stiffness $E t/R^2$ under a strip with bending stiffness $D$, which gives $\beta^4 = Et/(4DR^2) = 3(1 - \nu^2)/(R^2 t^2)$.

```verify
nu = q(0.30, "")
R = q(0.5, "m")
t = q(10, "mm")
beta = (3 * (1 - nu**2) / (R**2 * t**2))**0.25
expect(beta, "18.18 1/m")
expect(pi / beta, "0.1728 m")
expect(sqrt(R * t), "0.0707 m")
expect(pi / beta / sqrt(R * t), "2.44")
```

## Plate and shell buckling

### Plate buckling stress

A **plate** under in-plane compression can buckle into a wave pattern at a stress set by its thickness-to-width ratio, not by yield.

$$\sigma_{cr} = k\,\frac{\pi^2 E}{12\,(1 - \nu^2)}\left(\frac{t}{b}\right)^2$$

- $k$ is the **buckling coefficient**, set by edge conditions and aspect ratio. For a long plate simply supported on all four edges and compressed along its length, $k = 4$ (derived from the sinusoidal mode). Other edge conditions give other $k$; take them from a sourced table (Timoshenko and Gere, below).
- A plate keeps carrying more load after it first buckles, because the stress shifts to the edges (post-buckling reserve); this is the basis of effective-width design.
- Example: steel, $E = 200$ GPa, $\nu = 0.30$, $t = 2$ mm, $b = 200$ mm, $k = 4$: $\sigma_{cr} = 72.3$ MPa. A 5 mm plate of the same width would reach 451.9 MPa, above steel yield.

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\sigma_{cr}$ | critical (first buckling) compressive stress | Pa |
| $k$ | buckling coefficient | dimensionless |
| $E$ | Young's modulus | Pa |
| $\nu$ | Poisson's ratio | dimensionless |
| $t$ | plate thickness | m |
| $b$ | plate width across the loaded direction | m |

Holds when: elastic buckling (the result is below the proportional limit), perfectly flat plate, uniform compression, thin plate.
Breaks when: $\sigma_{cr}$ computed exceeds the proportional limit (inelastic buckling, use a reduced modulus), the plate is initially curved, or edge conditions differ from the assumed.
Source and basis: derived from the plate equation with in-plane load, $D\nabla^4 w + N_x\,\partial^2 w/\partial x^2 = 0$, and a sinusoidal mode; the elementary column case is in [column buckling](reference-mechanics.md#column-buckling).

```verify
E = q(200, "GPa")
nu = q(0.30, "")
k = 4
f = k * pi**2 * E / (12 * (1 - nu**2))
expect(f * (q(2, "mm") / q(200, "mm"))**2, "72.3 MPa")
expect(f * (q(5, "mm") / q(200, "mm"))**2, "451.9 MPa")
```

### Axial buckling of a cylindrical shell

The **classical buckling stress** of a perfect, thin, isotropic cylinder in axial compression is

$$\sigma_{cl} = \frac{E}{\sqrt{3\,(1 - \nu^2)}}\,\frac{t}{R} \approx 0.605\,E\,\frac{t}{R} \quad (\nu = 0.30)$$

- This is an upper bound for real shells. Measured buckling loads of thin cylinders fall well below it, because the post-buckling equilibrium path drops steeply and small geometric imperfections, loading eccentricity, and boundary conditions trigger collapse early. Design uses an empirical knockdown factor from a published design standard, not a value from this sheet.
- Example: steel, $R = 0.5$ m, $t = 2$ mm, $E = 200$ GPa, $\nu = 0.30$: $\sigma_{cl} = 484.2$ MPa, above yield, so a real shell of this proportion fails by yield or local buckling well below this number. Also check long-column Euler buckling for long shells.

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\sigma_{cl}$ | classical axisymmetric buckling stress | Pa |
| $E$ | Young's modulus | Pa |
| $\nu$ | Poisson's ratio | dimensionless |
| $t$ | wall thickness | m |
| $R$ | mean radius | m |

Holds when: the cylinder is perfect, thin ($R/t$ large), moderate length, uniform axial compression, elastic.
Breaks when: always, in practice, as a prediction of the real strength: imperfections reduce the load, internal pressure raises it, external pressure and bending change the mode. It also fails when the result exceeds yield.
Source and basis: derived from the linear stability analysis of the shell equations (axisymmetric mode); the knockdown relation to test data is empirical and is not given here.

```verify
E = q(200, "GPa")
nu = q(0.30, "")
t = q(2, "mm")
R = q(0.5, "m")
expect(E * t / (R * sqrt(3 * (1 - nu**2))), "484.2 MPa")
expect(1 / sqrt(3 * (1 - nu**2)), "0.605")
```

## Regime map

| Situation | Model to use | Check |
|---|---|---|
| Uniaxial bar, shaft, slender beam | Elementary formulas in [physics/reference-mechanics.md](reference-mechanics.md) | Slenderness and stress concentration |
| General 3D stress state, yield of a ductile metal | Principal stresses, von Mises (Tresca for a conservative bound) | Invariants, safety factor |
| Thin plate loaded in its plane | Plane stress | Plate thickness against feature size |
| Long body, constant section, loaded across the section | Plane strain | Ends restrained or free |
| Deflection or redundant of a frame or truss | Unit-load method, Castigliano | Linear elastic, small displacement |
| More supports than equilibrium equations | Force method (or stiffness method, finite elements) | Compatibility at each redundant |
| Closed thin-walled tube in torsion | Bredt-Batho | Single cell, free warping |
| Open thin-walled section in torsion | One-third sum, with warping torsion if restrained | Very low stiffness; avoid |
| Pressure cylinder, $t/r > 0.1$ | Lame equations | Yield at the bore |
| Interference fit | Shrink-fit pressure from Lame | Roughness, hub ends |
| Spinning disk | Rotating-disk formulas | Rim loads, thickness variation |
| Flat plate under pressure, deflection below half the thickness | Kirchhoff plate theory | Edge conditions between simple support and clamp |
| Plate deflection of the order of the thickness | Large-deflection plate theory or finite elements | Membrane action |
| Thin curved shell, smooth load | Membrane theory | Edge bending over $\sqrt{Rt}$ |
| Compressed plate, shell, or tube | Buckling analysis with knockdown from a standard | Imperfections |
| Complex geometry, contact, plasticity | Finite elements; see [simulation/reference-finite-element-analysis.md](../simulation/reference-finite-element-analysis.md) | Mesh convergence |
| Cyclic loading or cracks | Fatigue and fracture; see [materials/reference-fracture-fatigue.md](../materials/reference-fracture-fatigue.md) | Stress range, flaw size |

## Checklists

Tensors and failure:

- Sign convention stated; tension positive; $\gamma$ is twice $\varepsilon_{xy}$.
- All three principal stresses computed, including the zero one in plane stress.
- The invariants are the same before and after rotating the axes.
- Equivalent stress compared with $S_y$ for a ductile metal; brittle material checked with a normal-stress criterion.

Energy and indeterminacy:

- Loads and displacements paired: the unit load points where and the way the displacement is wanted.
- Shear and axial terms included only when they are not negligible.
- Number of redundants counted; compatibility equation written for each.
- Result checked by a second route, such as a standard table value or the sign of the reaction.

Thin-walled and curved bodies:

- Thin or thick decided by the ratio of thickness to radius, and the correct model chosen.
- Torsion section type identified: closed or open, one cell or several.
- Interference fit: roughness loss, temperature at assembly, and yield at the bore checked.
- Plate deflection compared with its thickness before trusting small-deflection theory.
- Shell junctions identified and the edge-bending length $\ell$ compared with the geometry.
- Buckling checked for every compressed thin member, with a knockdown from a published standard for shells.

## Sanity checks

- The sum of the diagonal terms of the stress tensor, $I_1$, does not change when the axes rotate.
- The classical cylinder factor $1/\sqrt{3(1 - \nu^2)}$ is 0.605 for $\nu = 0.30$.
- Von Mises and Tresca agree in uniaxial tension and differ by at most about 15 percent in other states.
- Constraining thermal expansion of steel in one direction costs about 2.4 MPa per kelvin ($E\alpha_L$, typical).
- $K_b$ is $E/3$ at $\nu = 0$ and $E$ at $\nu = 1/3$.
- A thick cylinder's bore hoop stress is always above the thin-wall estimate $pr/t$ for the inner radius, and approaches $p$ as the wall thickens without limit.
- An open thin-walled section in torsion is far softer than the same material closed into a tube.

```verify
E = q(200, "GPa")
al = q(12e-6, "1/K")
expect(E * al, "2.4 MPa/K")
expect(1 / sqrt(3 * (1 - q(0.30, "")**2)), "0.605")
check(E / (3 * (1 - 2 * q(0, ""))) == E / 3, "bulk modulus is E/3 at zero Poisson ratio")
nu13 = q(1, "") / 3
check(abs(E / (3 * (1 - 2 * nu13)) / E - 1) < 1e-12, "bulk modulus is E at Poisson ratio one third")
```

## Further reference

Named books and standards only (no links), except free sources listed with a URL.

- Roark's Formulas for Stress and Strain, Young and Budynas (paid, tables of plate, shell, and torsion cases).
- Theory of Elasticity, Timoshenko and Goodier (paid, classic solutions including thick cylinders and rotating disks).
- Theory of Elastic Stability, Timoshenko and Gere (paid, buckling coefficients for plates and shells).
- Theory of Plates and Shells, Timoshenko and Woinowsky-Krieger (paid, plates and membrane shells).
- Advanced Mechanics of Materials and Applied Elasticity, Ugural and Fenster (paid).
- Mechanics of Materials, Gere and Goodno (paid, energy methods and indeterminate members).
- Peterson's Stress Concentration Factors, Pilkey (paid, local stresses at notches).
- NASA SP-8007, Buckling of Thin-Walled Circular Cylinders (public NASA design guideline for knockdown factors; check the current version).
