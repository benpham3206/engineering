# Computational fluid dynamics reference

**Type:** reference
**Verify:** strict

Computational fluid dynamics (CFD) is the numerical solution of the conservation equations for a moving fluid on a mesh, and this sheet is the lookup for the formulation, discretization, stability limits, and mesh rules an engineer needs to set up and judge a flow simulation.

## Principles

- A flow solver approximates the conservation laws of mass, momentum, and energy. It adds no physics of its own, so every result is only as good as the equations chosen, the boundary conditions, and the mesh.
- Conservation form plus the finite-volume balance makes a scheme conserve its transported quantities exactly, whatever the mesh. A scheme that is not conservative can lose or create mass at shocks and at mesh jumps.
- Every discretization error acts as a physical effect. Low-order upwind schemes add artificial diffusion, central schemes add dispersion and oscillations. Know which one the scheme adds before reading a result.
- Stability and accuracy are different. An implicit method can be stable at any time step and still smear a wave it does not resolve.
- Information travels along characteristics. A scheme that takes data from the wrong side of a wave is unstable or wrong, and boundary conditions must fit the number of characteristics that enter the domain.
- Incompressible flow has no equation of state to give pressure. Pressure is a constraint that enforces zero divergence of velocity, and the solver must couple it to velocity.
- The mesh must resolve the thinnest layer that matters: the boundary layer, the shear layer, the shock. Resolution comes from the physics, not from a cell count.
- Turbulence is the hard part. For homogeneous, isotropic turbulence, resolving all scales costs a number that grows about as the cube of the Reynolds number, so every practical method models some scales.
- A converged run is not a correct run. Small residuals prove that the algebra settled, not that the discretization, the model, or the boundary conditions are right.
- Verification (solving the equations right) and validation (solving the right equations) are separate jobs. Grid convergence, Richardson extrapolation, and the grid convergence index are in the [verification and validation reference](reference-verification-validation.md).

## Conservation equations

The conservation form states that the rate of change of a quantity in a fixed volume equals the flux through its surface plus any source, and it is the form that the finite-volume method discretizes.

$$
\frac{\partial \rho}{\partial t} + \nabla \cdot (\rho \mathbf{v}) = 0
$$

$$
\frac{\partial (\rho \mathbf{v})}{\partial t} + \nabla \cdot (\rho \mathbf{v}\mathbf{v}) = -\nabla p + \nabla \cdot \boldsymbol{\tau} + \rho \mathbf{g}
$$

$$
\frac{\partial (\rho e_t)}{\partial t} + \nabla \cdot \big[(\rho e_t + p)\mathbf{v}\big] = \nabla \cdot (\boldsymbol{\tau}\cdot\mathbf{v}) + \nabla \cdot (k_{\text{th}} \nabla T) + \rho\, \mathbf{g}\cdot\mathbf{v} + \dot{q}_v
$$

For a Newtonian fluid the viscous stress is linear in the rate of strain:

$$
\boldsymbol{\tau} = \mu\left[\nabla\mathbf{v} + (\nabla\mathbf{v})^{\mathsf{T}}\right] - \tfrac{2}{3}\mu\, (\nabla\cdot\mathbf{v})\,\mathbf{I}
$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\rho$ | fluid density | $\text{kg/m}^{3}$ |
| $\mathbf{v}$ | velocity vector | m/s |
| $t$ | time | s |
| $p$ | absolute pressure | Pa |
| $\boldsymbol{\tau}$ | viscous stress tensor | Pa |
| $\mathbf{I}$ | identity tensor | dimensionless |
| $\mathbf{g}$ | local gravitational acceleration vector | $\text{m/s}^{2}$ |
| $e_t$ | total specific energy, internal plus kinetic | J/kg |
| $k_{\text{th}}$ | thermal conductivity | W/(m K) |
| $T$ | absolute temperature | K |
| $\mu$ | dynamic viscosity | Pa s |
| $\dot{q}_v$ | volumetric heat source | $\text{W/m}^{3}$ |

Holds when: the fluid is a continuum (the mean free path is far below the smallest flow scale), Newtonian, and described by a single-phase equation of state; the stress form above also assumes that bulk viscosity is negligible.
Breaks when: the flow is rarefied (high altitude, microchannels), the fluid is non-Newtonian (polymer melts, blood at low shear), or radiation, chemical reaction, or multiple phases add terms that are not written here.
Source and basis: derived from conservation of mass, Newton's second law, and the first law of thermodynamics for a control volume; the integral forms are taught in [Control volumes and pipe flow](../physics/11-control-volumes-pipe-flow.md), and Bernoulli's equation as the inviscid steady special case in [Hydrostatics and Bernoulli](../physics/10-hydrostatics-and-bernoulli.md).

- The momentum and energy equations are written with the product $\rho \mathbf{v}$ inside the divergence. That conservation form lets a shock satisfy the correct jump conditions. The non-conservative form $\rho\, D\mathbf{v}/Dt$ is equivalent for smooth flow only.
- Incompressible flow with constant density and viscosity reduces to $\nabla\cdot\mathbf{v} = 0$ and $\rho\, D\mathbf{v}/Dt = -\nabla p + \mu \nabla^2 \mathbf{v} + \rho\mathbf{g}$. The energy equation then decouples from the flow unless properties depend on temperature.
- Five unknowns in 3D compressible flow ($\rho$, three velocity components, $e_t$) need five equations, plus an equation of state such as the ideal gas law. Pressure is then a thermodynamic variable.

## Nondimensional form

Scaling the equations by a reference length $L$, speed $U$, and fluid properties shows which dimensionless groups decide the solution, and a simulation is only as hard as those groups make it.

$$
\mathrm{Re} = \frac{\rho U L}{\mu} \qquad \mathrm{Ma} = \frac{U}{a} \qquad \mathrm{Pr} = \frac{\mu c_p}{k_{\text{th}}} \qquad \mathrm{Pe} = \mathrm{Re}\,\mathrm{Pr} = \frac{U L}{\alpha_{\text{th}}}
$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\mathrm{Re}$ | Reynolds number, inertia over viscous force | dimensionless |
| $\mathrm{Ma}$ | Mach number, flow speed over sound speed | dimensionless |
| $\mathrm{Pr}$ | Prandtl number, momentum over thermal diffusivity | dimensionless |
| $\mathrm{Pe}$ | Peclet number, advection over thermal diffusion | dimensionless |
| $U$ | reference speed | m/s |
| $L$ | reference length | m |
| $a$ | speed of sound in the fluid | m/s |
| $c_p$ | specific heat at constant pressure | J/(kg K) |
| $\alpha_{\text{th}}$ | thermal diffusivity, $k_{\text{th}}/(\rho c_p)$ | $\text{m}^{2}$/s |

Holds when: $L$ and $U$ are stated for the problem (pipe diameter and mean speed, chord and free-stream speed); state them whenever a group is quoted.
Breaks when: more than one length matters (a long thin plate has a thickness and a length, each with its own Reynolds number), or buoyancy, rotation, or free surfaces add groups such as Rayleigh, Rossby, or Froude.
Source and basis: derived from scaling the conservation equations; the table of groups is in the [thermal-fluids reference](../physics/reference-thermofluids.md#dimensionless-numbers).

What each group controls in a simulation:

| Group | Small value | Large value |
|---|---|---|
| $\mathrm{Re}$ | Viscous, smooth, steady flow; coarse mesh is enough | Thin boundary layers, turbulence; mesh and model cost climb sharply |
| $\mathrm{Ma}$ | Below about 0.3 the density change is small and an incompressible solver is usable | Compressible solver needed; shocks and expansion waves appear near and above 1 |
| $\mathrm{Pr}$ | Thermal layer thicker than the velocity layer | Thermal layer thinner than the velocity layer, so the thermal mesh must be finer |
| $\mathrm{Pe}$ | Diffusion dominates over the reference length; central differencing is non-oscillatory only when the cell Peclet number $\mathrm{Pe}_{\Delta}$ is at most 2 | Advection dominates over the reference length; central differencing can still be non-oscillatory when $\mathrm{Pe}_{\Delta}$ is at most 2, while an upwind scheme smears |

Example. A flow with $U = 2$ m/s, $L = 0.5$ m, and $\nu_k = 1.5 \times 10^{-5}$ $\text{m}^{2}$/s (air, typical) has $\mathrm{Re} = UL/\nu_k = 66667$, well into turbulent flow for most geometries.

<details><summary>Verification</summary>

```verify
U = q(2, "m/s")
L = q(0.5, "m")
nu = q(1.5e-5, "m^2/s")
Re = U * L / nu
expect(Re, "66667")
```

</details>

## PDE classification and its numerical consequences

A second-order partial differential equation is hyperbolic, parabolic, or elliptic, and the class says which way information moves and what boundary data the problem needs.

$$
A\,\phi_{xx} + B\,\phi_{xy} + C\,\phi_{yy} + \dots = 0, \qquad B^2 - 4AC \;\begin{cases} > 0 & \text{hyperbolic} \\ = 0 & \text{parabolic} \\ < 0 & \text{elliptic} \end{cases}
$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\phi$ | the unknown field, in nondimensional form | dimensionless |
| $A$ | coefficient of $\phi_{xx}$ | dimensionless |
| $B$ | coefficient of $\phi_{xy}$ | dimensionless |
| $C$ | coefficient of $\phi_{yy}$ | dimensionless |
| $x$, $y$ | the two independent variables (space and space, or space and time), nondimensional | dimensionless |

Holds when: the equation is written in nondimensional variables, is second order, and linear (or locally linearized), with the coefficients frozen at a point.
Breaks when: the system is mixed (transonic flow is elliptic where subsonic and hyperbolic where supersonic), nonlinear shocks form, or the equation system has higher order.
Source and basis: derived from the characteristic curves of the second-order operator; taught in [PDEs and Fourier series](../math/10-pdes-and-fourier-series.md).

| Class | Flow example | Information moves | Numerical consequence |
|---|---|---|---|
| Hyperbolic | Unsteady inviscid compressible flow, wave propagation, supersonic steady flow | Along characteristics, at finite speed | Marching in time or in the flow direction; upwind-biased fluxes; a time step limit from the wave speed; boundary conditions set only where characteristics enter |
| Parabolic | Unsteady diffusion, boundary-layer equations | Forward in time (or along the flow), spreading by diffusion | Marching; implicit methods remove the diffusion time step limit |
| Elliptic | Steady diffusion, the pressure equation for incompressible flow, subsonic steady potential flow | Both ways at once; every point depends on all boundaries | One global system solved iteratively; boundary conditions on the whole boundary; no marching |

- Steady incompressible Navier-Stokes is elliptic, unsteady incompressible Navier-Stokes is a mix, and unsteady Euler is hyperbolic.
- At high $\mathrm{Re}$ or $\mathrm{Pe}$ the viscous or diffusive terms are small, and the equations behave in practice as hyperbolic away from walls. The numerical scheme should respect that.

## Finite-volume balance

The finite-volume method divides the domain into cells and enforces the integral conservation law on each cell, which makes the discrete scheme conserve every transported quantity by construction.

$$
\frac{d}{dt}\int_{V_c} \phi\, dV + \oint_{\partial V_c} \mathbf{f}\cdot\hat{\mathbf{n}}\, dS = \int_{V_c} s_\phi\, dV
\quad\Longrightarrow\quad
V_c \frac{d\bar{\phi}_c}{dt} = -\sum_{f} \mathbf{f}_f\cdot\mathbf{S}_f + V_c\, \bar{s}_c
$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\phi$ | conserved quantity per unit volume, shown for mass so that $\phi = \rho$ | $\text{kg/m}^{3}$ |
| $V_c$ | cell volume | $\text{m}^{3}$ |
| $\bar{\phi}_c$ | cell-average value of $\phi$ | $\text{kg/m}^{3}$ |
| $\mathbf{f}$ | flux density of $\phi$ (convective plus diffusive) | $\text{kg/(m}^{2}\ \text{s)}$ |
| $\hat{\mathbf{n}}$ | outward unit normal | dimensionless |
| $\mathbf{S}_f$ | face area vector, outward, magnitude equal to the face area | $\text{m}^{2}$ |
| $s_\phi$ | source of $\phi$ per unit volume | $\text{kg/(m}^{3}\ \text{s)}$ |
| $\bar{s}_c$ | cell average of the source | $\text{kg/(m}^{3}\ \text{s)}$ |

Holds when: the units shown are for mass (momentum and energy carry their own units in the same pattern); each interior face is shared by exactly two cells and both use the same face flux, with opposite sign; the cell is fixed in space (moving meshes add the mesh velocity to the flux).
Breaks when: a face flux is computed differently for the two cells that share it (non-conservative interpolation across a mesh interface), or the source term is evaluated inconsistently with the fluxes.
Source and basis: derived from the Reynolds transport theorem and the divergence theorem; the control-volume balance is taught in [Control volumes and pipe flow](../physics/11-control-volumes-pipe-flow.md).

- Conservation by construction means the sum over all cells of $V_c \bar{\phi}_c$ changes only by the boundary fluxes and sources. Interior face fluxes cancel in pairs.
- Cell-centered schemes store $\bar{\phi}_c$ at the cell centroid, so the face value must be reconstructed from the neighbors. Every scheme in the next section is a way to do that.
- Mesh quality enters through the face geometry. Skewed or highly stretched cells make the face-value reconstruction less accurate, though conservation still holds.

## Spatial fluxes and diffusion

The face value of a convected quantity comes from its neighbors, and the way the neighbors are weighted fixes the accuracy, the stability, and the numerical diffusion of the scheme.

$$
\mathrm{Pe}_{\Delta} = \frac{\rho u\, \Delta x}{\Gamma}
\qquad
\phi_f^{\text{central}} = \tfrac{1}{2}(\phi_C + \phi_D)
\qquad
\phi_f^{\text{upwind}} = \phi_C
\qquad
\Gamma_{\text{num}} = \tfrac{1}{2}\,\rho u\, \Delta x
$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\mathrm{Pe}_{\Delta}$ | cell Peclet number, convection over diffusion across one cell | dimensionless |
| $\rho$ | density | $\text{kg/m}^{3}$ |
| $u$ | velocity component normal to the face | m/s |
| $\Delta x$ | cell size along the flow | m |
| $\Gamma$ | diffusion coefficient of $\phi$ (for example $\mu$ for momentum) | kg/(m s) |
| $\phi_C$ | normalized cell-center value of the upwind cell | dimensionless |
| $\phi_D$ | normalized cell-center value of the downwind cell | dimensionless |
| $\phi_U$ | normalized value one cell further upwind | dimensionless |
| $\phi_f$ | normalized face value of the convected quantity | dimensionless |
| $r$ | ratio of successive gradients | dimensionless |
| $\psi$ | limiter function of $r$ | dimensionless |
| $\Gamma_{\text{num}}$ | numerical diffusion coefficient added by first-order upwind | kg/(m s) |

Holds when: steady 1D convection and diffusion with constant coefficients on a uniform mesh; the flow carries $\phi$ from cell $C$ toward cell $D$.
Breaks when: the flow is not aligned with the mesh (upwind then diffuses across the flow, called false diffusion), the mesh is strongly non-uniform, or the problem is unsteady (the numerical diffusion then depends on the time step also).
Source and basis: derived from the discrete 1D convection-diffusion balance, whose neighbor coefficients stay positive only when the cell Peclet number is at most 2, and from the Taylor expansion of the upwind difference, whose leading error is a diffusion term; taught in [Numerical methods](../math/08-numerical-methods.md).

- Central differencing is second-order accurate. For $\mathrm{Pe}_\Delta$ above 2 it gives non-physical oscillations (wiggles) around sharp gradients, because a neighbor coefficient turns negative. The fix is a finer mesh so that $\Delta x \le 2\Gamma/(\rho u)$, or a different scheme.
- First-order upwind is bounded and stable at any $\mathrm{Pe}_\Delta$, but its truncation error acts as an extra diffusion $\Gamma_{\text{num}}$. When $\Gamma_{\text{num}}$ exceeds the physical $\Gamma$ the solution is dominated by the scheme, not the physics. Their ratio is $\Gamma_{\text{num}}/\Gamma = \mathrm{Pe}_\Delta/2$.
- Higher-order upwind-biased schemes cut numerical diffusion but can overshoot at steep gradients.

Total-variation-diminishing (TVD) limiters blend the two. The face value is the upwind value plus a limited share of the central correction:

$$
\phi_f = \phi_C + \tfrac{1}{2}\,\psi(r)\,(\phi_D - \phi_C), \qquad r = \frac{\phi_C - \phi_U}{\phi_D - \phi_C}
$$

Here $\phi_U$ is the value one cell further upwind and $\psi(r)$ is the limiter function. With $\psi = 0$ the face value is the upwind value, and with $\psi = 1$ it is the central value. A limiter chooses $\psi$ from the local ratio $r$ of successive gradients so that no new maximum or minimum is created. The simplest example, minmod, takes $\psi = \max(0, \min(1, r))$.

Example. Air-like flow with $u = 2$ m/s, $\rho = 1$ $\text{kg/m}^{3}$, $\Gamma = 0.001$ kg/(m s), and $\Delta x = 0.01$ m has $\mathrm{Pe}_\Delta = 20$. Central differencing would oscillate. Its limit is $\Delta x \le 1$ mm. First-order upwind on the 10 mm mesh adds $\Gamma_{\text{num}} = 0.01$ kg/(m s), ten times the physical value.

<details><summary>Verification</summary>

```verify
rho = q(1, "kg/m^3")
vel = q(2, "m/s")
G = q(0.001, "kg/m s")
dx = q(0.01, "m")
Pe = rho * vel * dx / G
expect(Pe, "20")
dx_max = 2 * G / (rho * vel)
expect(dx_max, "1 mm")
Gnum = rho * vel * dx / 2
expect(Gnum, "0.01 kg/m s")
expect(Gnum / G, "10")
```

</details>

## Time advancement and CFL limits

An explicit time step is stable only if information moves less than about one cell per step, which sets a maximum time step from the Courant-Friedrichs-Lewy (CFL) number.

$$
\mathrm{CFL} = \frac{|u|\,\Delta t}{\Delta x} \le \mathrm{CFL}_{\max}
\qquad
\Delta t_{\text{diff}} \le \frac{\Delta x^{2}}{2\, n_d\, D}, \qquad
\Delta t \lesssim \frac{1}{|u|/\Delta x + 2 n_d D/\Delta x^{2}}
$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\mathrm{CFL}$ | Courant number, cells crossed per time step | dimensionless |
| $\mathrm{CFL}_{\max}$ | scheme-dependent stability limit, about 1 for simple explicit upwind | dimensionless |
| $u$ | local signal speed (flow speed, or flow speed plus sound speed for compressible flow) | m/s |
| $\Delta t$ | time step | s |
| $\Delta x$ | cell size in the direction of $u$ | m |
| $D$ | diffusivity (kinematic viscosity or thermal diffusivity) | $\text{m}^{2}$/s |
| $n_d$ | number of space dimensions | dimensionless |

Holds when: a uniform mesh, an explicit forward-Euler step, and constant coefficients; the advection CFL bound is for an upwind scheme, and the combined advection-diffusion estimate applies when both terms act together on a uniform mesh. Other explicit schemes (multi-stage Runge-Kutta) have their own $\mathrm{CFL}_{\max}$ from their stability region.
Breaks when: the mesh has unequal spacing (use $\Delta t_{\text{diff}} \le 1/(2D\sum_i \Delta x_i^{-2})$ instead of the equal-spacing diffusion bound), the equation has stiff source terms such as chemistry, or an implicit scheme is used (the limit is then an accuracy limit, not a stability limit). Forward Euler with central advection is unstable at every time step, so use an upwind or another stable advection discretization.
Source and basis: derived from the von Neumann stability analysis of the upwind advection and forward-Euler diffusion schemes; the stability limits and the behavior of explicit steps are taught in [Numerical methods](../math/08-numerical-methods.md).

- The CFL limit applies to the fastest signal. In compressible flow that is the flow speed plus the sound speed, $|u| + a$. An incompressible flow has no sound-speed limit. When advection and diffusion both act, the explicit step must satisfy the combined estimate above, which is tighter than either separate limit.
- The diffusion limit scales with $\Delta x^2$, so halving the mesh size cuts the allowed explicit step by four. At fine meshes (near walls) an explicit diffusion step becomes tiny, which is why viscous terms are often treated implicitly.
- Backward-Euler and other implicit steps are stable for any $\Delta t$ in a linear problem. The price is a global linear system per step, and the step must still be small enough to resolve the time scale of interest. An implicit step with $\mathrm{CFL}$ far above 1 damps waves instead of propagating them.
- Time-accurate runs of vortex shedding or acoustics need $\mathrm{CFL}$ of order 1 even with an implicit method. Steady-state runs may use a large pseudo-time step.

Example. For the compressible limit, take $u = 100$ m/s, $a = 340$ m/s, $\Delta x = 10$ mm, and $\mathrm{CFL} = 0.5$. Then $\Delta t = 0.0114$ ms. For the diffusion limit, take $\nu_k = 1.5 \times 10^{-5}$ $\text{m}^{2}$/s, $\Delta x = 1$ mm, and one space dimension, which gives $\Delta t_{\text{diff}} = 0.0333$ s.

<details><summary>Verification</summary>

```verify
vel = q(100, "m/s")
a = q(340, "m/s")
dx = q(10, "mm")
cfl = q(0.5, "")
dt = cfl * dx / (vel + a)
expect(dt, "0.0114 ms")
nu = q(1.5e-5, "m^2/s")
dx2 = q(0.001, "m")
dtd = dx2**2 / (2 * nu)
expect(dtd, "0.0333 s")
```

</details>

## Pressure-velocity coupling

Incompressible flow has no equation that gives the pressure, so the solver finds the pressure that makes the velocity field divergence-free, and this coupling is the central difficulty of the method.

$$
\nabla^{2} p' = \frac{\rho}{\Delta t}\, \nabla\cdot\mathbf{v}^{*}, \qquad \mathbf{v}^{n+1} = \mathbf{v}^{*} - \frac{\Delta t}{\rho}\,\nabla p'
$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $p'$ | pressure correction (the pressure change that removes the divergence) | Pa |
| $\rho$ | constant density | $\text{kg/m}^{3}$ |
| $\Delta t$ | time step | s |
| $\mathbf{v}^{*}$ | intermediate velocity from the momentum equation with the old pressure | m/s |
| $\mathbf{v}^{n+1}$ | corrected velocity at the new time level | m/s |

Holds when: constant-density flow, and the intermediate velocity comes from a momentum step that omits the new pressure gradient (the projection method).
Breaks when: density varies strongly (use a variable-density or compressible solver), the pressure boundary condition is inconsistent with the velocity boundary condition (the equation then has no consistent solution), or the pressure and velocity are stored at the same points without a coupling term (pressure checkerboarding).
Source and basis: derived by taking the divergence of the momentum update and requiring $\nabla\cdot\mathbf{v}^{n+1} = 0$; the incompressible equations are in [Control volumes and pipe flow](../physics/11-control-volumes-pipe-flow.md).

- The pressure equation is elliptic, so it is solved on the whole domain at once. It usually takes most of the run time.
- The projection method solves it once per step: predict $\mathbf{v}^{*}$, solve for $p'$, correct the velocity. Pressure-correction methods for steady flow, of the SIMPLE family, repeat this cycle with under-relaxation on the pressure and the velocity until the corrections vanish.
- A collocated mesh (all variables at the cell center) needs a face-flux interpolation that couples neighboring pressures. A staggered mesh stores pressure at cell centers and velocity at faces, which couples them naturally.
- In a closed domain with only wall or velocity boundaries the pressure is fixed only up to a constant, so one reference pressure must be set.

## Compressible-flow discretization

Compressible flow is solved in conservation form with fluxes computed at each face from the states on its two sides, so that shocks are captured as part of the solution without being tracked.

$$
\frac{\partial \mathbf{U}}{\partial t} + \frac{\partial \mathbf{F}}{\partial x} = 0, \qquad
\mathbf{U} = \begin{bmatrix} \rho \\ \rho u \\ \rho e_t \end{bmatrix}, \quad
\mathbf{F} = \begin{bmatrix} \rho u \\ \rho u^{2} + p \\ (\rho e_t + p)\,u \end{bmatrix}
$$

$$
\mathbf{U}_i^{n+1} = \mathbf{U}_i^{n} - \frac{\Delta t}{\Delta x}\left(\mathbf{F}_{i+1/2} - \mathbf{F}_{i-1/2}\right), \qquad
\mathbf{F}_{i+1/2} = \tfrac{1}{2}(\mathbf{F}_L + \mathbf{F}_R) - \tfrac{1}{2}\,s_{\max}(\mathbf{U}_R - \mathbf{U}_L)
$$

Variables: the vectors $\mathbf{U}$, $\mathbf{F}$ (flux), $\mathbf{U}_L$, $\mathbf{U}_R$ (states left and right of a face), and $\mathbf{F}_{i+1/2}$ (face flux between cells $i$ and $i+1$) have the units of their components, listed below.

| Symbol | Meaning | SI unit |
|---|---|---|
| $\rho$ | density | $\text{kg/m}^{3}$ |
| $u$ | velocity | m/s |
| $p$ | pressure | Pa |
| $\rho u$ | momentum density, second component of $\mathbf{U}$ | $\text{kg/(m}^{2}\ \text{s)}$ |
| $\rho e_t$ | total energy density, third component of $\mathbf{U}$ | $\text{J/m}^{3}$ |
| $a$ | speed of sound | m/s |
| $e_t$ | total specific energy | J/kg |
| $i$, $n$ | cell index and time level | dimensionless |
| $s_{\max}$ | largest signal speed at the face, $\max(\lvert u \rvert + a)$ over the two states | m/s |

Holds when: one space dimension (multi-dimensional flow applies the same flux in the normal direction to each face), and an explicit step that satisfies the CFL limit with the speed $|u| + a$.
Breaks when: the flux is not consistent (the physical flux for equal left and right states), the scheme is not conservative (shocks then move at the wrong speed), or the first-order dissipation smears features that the mesh should resolve (use a higher-order reconstruction with limiting).
Source and basis: derived from the integral conservation laws applied cell by cell; the Euler flux is derived from mass, momentum, and energy balances, and the compressible relations are in the [compressible flow reference](../physics/reference-compressible-flow.md).

- A Riemann solver computes the face flux from the exact or approximate solution of the initial-value problem with the left state on one side of the face and the right state on the other. It treats each face as a small shock tube, which puts the right upwind direction for every wave into the flux.
- The flux shown is the simplest approximate choice: the central average plus a dissipation term proportional to the largest signal speed. It is robust but smears shocks over several cells. More detailed solvers use the separate wave speeds and give sharper shocks.
- Conservation form fixes the shock speed. For a scalar law the discrete shock speed is $s = (F_R - F_L)/(U_R - U_L)$ (the Rankine-Hugoniot relation), and only conservative schemes converge to the correct one.
- Shock capturing spreads a shock over a few cells. The thickness is set by the mesh, not by physical viscosity.
- Higher-order reconstruction (limited to keep it monotone) is combined with the Riemann flux to get second-order accuracy away from shocks.

## Boundary conditions

A boundary condition supplies the information that the outside of the domain provides, and the wrong choice or a boundary too close to the body corrupts the solution everywhere.

| Boundary | Typical specification | Notes |
|---|---|---|
| Inlet (incompressible) | Velocity profile, plus turbulence quantities if a turbulence model is used | A uniform inlet is only valid if the real flow is nearly uniform; for a pipe, use a developed profile or a long enough inlet section |
| Inlet (compressible, subsonic) | Total pressure and total temperature and flow direction | One characteristic leaves the domain, so one quantity comes from the interior |
| Outlet (subsonic) | Static pressure, or zero normal gradient with a fixed reference pressure | Reflects waves if badly placed; keep it where the flow is nearly parallel and no vortex crosses it |
| Supersonic outlet | Extrapolate everything from the interior | All characteristics leave the domain, so nothing is imposed |
| No-slip wall | Velocity equals wall velocity, and either a fixed temperature or a heat flux | The velocity gradient there sets the wall shear |
| Slip or symmetry plane | Zero normal velocity, zero normal gradient of everything else | Symmetry only applies if both the geometry and the flow are symmetric; a symmetric geometry can still have an asymmetric flow |
| Far field | Free-stream state or characteristic-based condition | Must sit far enough from the body that disturbances have decayed |

- Give a boundary the number of conditions equal to the characteristics that enter the domain. Too few makes the problem ill-posed and too many over-constrain it.
- Place inlet and outlet far enough that moving them does not change the result. Run the same case with the boundary moved outward; the quantity of interest must not change by more than the accuracy needed.
- Do not put an outlet inside a recirculation zone. Back-flow through the outlet carries unknown information into the domain.
- Prescribe the total mass flow that crosses the domain consistently: inflow, outflow, and any compressible accumulation must balance (see the global check below).

## Near-wall resolution

The wall distance in wall units, written y plus, says whether the first mesh cell sits in the viscous sublayer or in the log layer, and it sets the first-cell height for a wall-resolved or wall-function mesh.

$$
y^{+} = \frac{y\, u_\tau}{\nu_k}, \qquad u_\tau = \sqrt{\frac{\tau_w}{\rho}} = U\sqrt{\frac{C_f}{2}}
$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $y^{+}$ | wall distance in wall units | dimensionless |
| $y$ | distance from the wall to the first cell center | m |
| $u_\tau$ | friction velocity | m/s |
| $\nu_k$ | kinematic viscosity | $\text{m}^{2}$/s |
| $\tau_w$ | wall shear stress | Pa |
| $\rho$ | fluid density | $\text{kg/m}^{3}$ |
| $U$ | free-stream speed | m/s |
| $C_f$ | local skin-friction coefficient, $\tau_w/(\tfrac{1}{2}\rho U^2)$ | dimensionless |
| $\mathrm{Re}_x$ | Reynolds number based on distance $x$ from the leading edge | dimensionless |

Holds when: attached turbulent boundary layer from the leading edge on a smooth flat plate with zero pressure gradient, for $\mathrm{Re}_x$ from about $5 \times 10^5$ to $10^7$; there is no laminar run before the point where $\mathrm{Re}_x$ is evaluated.
Breaks when: the flow has a pressure gradient, separation, roughness, or strong curvature, in which case the estimate of $C_f$ is only a first guess and the true $y^{+}$ must be read from the solution and the mesh adjusted.
Source and basis: $y^{+}$, $u_\tau$, and $C_f$ are definitions derived from the wall shear; use the correlation and its range in [External flow drag and lift](../physics/reference-thermofluids.md#external-flow-drag-and-lift).

- A wall-resolved mesh puts the first cell center at $y^{+}$ near 1, with several cells below 5, so the viscous sublayer is in the mesh. The wall shear is then computed from the velocity gradient.
- A wall-function mesh puts the first center in the log layer, which is roughly $y^{+}$ between 30 and 300 for most models (typical; consult the model's documentation). The wall shear then comes from a profile law and not from the mesh.
- The region between about 5 and 30 is the buffer layer. A mesh with first-cell $y^{+}$ there is the worst of both and should be avoided.
- The estimate is made before the run, since the wall shear is not known yet. After the run, read the actual $y^{+}$ from the solution, because $C_f$ depends on the real flow and the first value is only a guide.
- Grow the cells away from the wall at a modest ratio, so that the cell size changes smoothly through the boundary layer.

Example. Air with $U = 30$ m/s and $\nu_k = 1.5 \times 10^{-5}$ $\text{m}^{2}$/s over a plate, at $x = 1$ m. The correlation in [External flow drag and lift](../physics/reference-thermofluids.md#external-flow-drag-and-lift) gives $C_f = 0.00325$ at $\mathrm{Re}_x = 2000000$, so $u_\tau = 1.21$ m/s. For $y^{+} = 1$ the first cell center is at $y = 0.0124$ mm from the wall.

<details><summary>Verification</summary>

```verify
U = q(30, "m/s")
x = q(1, "m")
nu = q(1.5e-5, "m^2/s")
Rex = U * x / nu
expect(Rex, "2000000")
Cf = q(0.00325, "", of="none")
utau = U * sqrt(Cf / 2)
expect(utau, "1.21 m/s")
yp = q(1, "")
y = yp * nu / utau
expect(y, "0.0124 mm")
```

</details>

## Turbulence-model boundary

Turbulent flow contains eddies from the size of the geometry down to a viscous cutoff, and the three modeling levels differ in how much of that range the mesh resolves and how much a model supplies.

| Approach | What is resolved | What is modeled | Cost and use |
|---|---|---|---|
| Direct numerical simulation (DNS) | All scales down to the Kolmogorov scale | Nothing | Cost grows about as the cube of $\mathrm{Re}$ for homogeneous, isotropic turbulence; limited to low $\mathrm{Re}$ and simple geometry; used to study the physics and build models |
| Large-eddy simulation (LES) | The large, energy-containing eddies | Eddies smaller than the filter, by a subgrid model | Far cheaper than DNS in the free flow but still costly near walls; time-accurate, three-dimensional |
| Reynolds-averaged Navier-Stokes (RANS) | Only the mean flow | All turbulent fluctuations, through a closure for the Reynolds stresses | Cheapest; steady or slowly varying; the accuracy depends on the closure and the flow |

The cost of DNS follows from the smallest eddy size. In the energy cascade, energy enters at the large scale $L$ with speed $U$ and is dissipated at the Kolmogorov length $\eta$ by viscosity:

$$
\eta = \left(\frac{\nu_k^{3}}{\varepsilon}\right)^{1/4}, \quad \varepsilon \sim \frac{U^{3}}{L}
\;\Longrightarrow\;
\frac{L}{\eta} \sim \mathrm{Re}_L^{3/4}, \quad N_{\text{points}} \sim \left(\frac{L}{\eta}\right)^{3} \sim \mathrm{Re}_L^{9/4}, \quad \text{cost} \sim \mathrm{Re}_L^{3}
$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\eta$ | Kolmogorov length scale | m |
| $\nu_k$ | kinematic viscosity | $\text{m}^{2}$/s |
| $\varepsilon$ | turbulent dissipation rate per unit mass | $\text{m}^{2}/\text{s}^{3}$ |
| $U$ | velocity of the energy-containing eddies | m/s |
| $L$ | length of the energy-containing eddies | m |
| $\mathrm{Re}_L$ | Reynolds number $UL/\nu_k$ | dimensionless |
| $N_{\text{points}}$ | number of grid points for a three-dimensional DNS | dimensionless |

Holds when: homogeneous, isotropic turbulence at high $\mathrm{Re}$, with the dissipation rate balancing the energy supplied at the large scale; the scaling gives orders of magnitude, with a constant prefactor that depends on the flow.
Breaks when: the Reynolds number is low (no clear scale separation), the flow is wall-bounded (near-wall layers need extra resolution), or the geometry is complex; the prefactor then changes by large factors, so use the scaling for ratios, not absolute counts.
Source and basis: derived from dimensional analysis: the only length from $\nu_k$ and $\varepsilon$ is $\eta$ above, and the energy-cascade assumption that the dissipation rate equals the large-scale rate $U^{3}/L$. The time step scales as the CFL limit $\Delta t \sim \eta/U$, so the number of steps over a fixed number of large-eddy turnover times grows as $\mathrm{Re}_L^{3/4}$, and the cost is points times steps.

Example. Raising the Reynolds number from $10^4$ to $10^5$ multiplies the number of DNS grid points by $10^{9/4} = 177.8$ and the total cost by $10^{3} = 1000$.

<details><summary>Verification</summary>

```verify
ratio = q(10, "")
expect(ratio**(9/4), "177.8")
expect(ratio**3, "1000")
```

</details>

## Residuals and conservation checks

A residual measures how far the current iterate is from satisfying the discrete equations, and conservation checks measure whether the converged result obeys the physical balances.

$$
r = \frac{\lVert \mathbf{b} - \mathbf{A}\boldsymbol{\phi} \rVert}{\lVert \mathbf{b} \rVert}, \qquad
\epsilon_{\dot{m}} = \frac{\left|\dot{m}_{\text{in}} - \dot{m}_{\text{out}}\right|}{\dot{m}_{\text{in}}}
$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $r$ | scaled residual of one equation | dimensionless |
| $\mathbf{A}$ | coefficient matrix of the scaled discrete equation | dimensionless |
| $\boldsymbol{\phi}$ | current iterate of the scaled unknown field | dimensionless |
| $\mathbf{b}$ | right-hand side of the scaled discrete equation | dimensionless |
| $\epsilon_{\dot{m}}$ | relative mass-flow imbalance across the domain | dimensionless |
| $\dot{m}_{\text{in}}$, $\dot{m}_{\text{out}}$ | total mass flow rate into and out of the domain | kg/s |

Holds when: the flow is steady and incompressible, or compressible with no accumulation, and the norm and the scaling are stated.
Breaks when: the residual is scaled so that a large initial value hides a poor fit, the run is unsteady (mass can accumulate, so compare against the change in stored mass), or the residual stalls while a monitored quantity still drifts.
Source and basis: derived from the definition of the residual of a linear system, in [Numerical methods](../math/08-numerical-methods.md), and from conservation of mass for a fixed domain.

- A residual drop of a few orders of magnitude means the iteration settled. It does not show that the answer is accurate.
- Monitor a quantity of interest (drag, pressure drop, outlet temperature) together with the residual. Declare convergence only when both are flat.
- A residual that oscillates at a fixed level often means a real unsteady flow, such as vortex shedding, which a steady solver cannot settle.
- A non-conservative scheme, a poor mesh interface, or a wrong boundary condition shows up as a mass or energy imbalance that does not shrink with the residual.

Example. Inflow 2.0 kg/s and outflow 1.97 kg/s gives a 1.5 percent imbalance, which is a flag: check the boundaries and the convergence, not a number to accept.

<details><summary>Verification</summary>

```verify
mi = q(2.0, "kg/s")
mo = q(1.97, "kg/s")
expect(abs(mi - mo) / mi * 100, "1.5")
```

</details>

## Checklists

Before a run:

- State the equations being solved, the fluid properties and their sources, and the reference length and speed for every dimensionless group.
- Compute $\mathrm{Re}$, $\mathrm{Ma}$, and $\mathrm{Pe}$ and pick the solver family and turbulence approach from them.
- Estimate the first-cell height from the target $y^{+}$ and check the boundary-layer thickness is covered by enough cells.
- Check the cell Peclet number of each convective scheme and the CFL number of each explicit step.
- Put the boundaries far enough away, with the right number of conditions at each.

After a run:

- Residuals dropped by the planned amount and the monitored quantities are flat.
- Global mass, momentum, and energy balances close to the tolerance set before the run.
- The actual $y^{+}$ field lies in the intended range everywhere that matters.
- The result does not change when the mesh, the boundaries, and the time step are changed in turn; see the [verification and validation reference](reference-verification-validation.md).
- The result is compared against an independent measurement or a trusted benchmark before use.

## Sanity checks

- A flow with $\mathrm{Re}$ below about 2000 in a pipe should come out laminar. A turbulent pipe flow has a friction factor that follows the pipe correlations in the [thermal-fluids reference](../physics/reference-thermofluids.md#pipe-flow).
- Mass in equals mass out for steady flow, whatever the geometry. If not, the run is wrong or unconverged.
- Pressure drop and wall shear must agree with a hand estimate to within the accuracy of the estimate (a factor of two is a warning).
- A free stream far from the body should have the inlet speed and pressure. If not, the domain is too small.
- The numerical diffusion of an upwind scheme is $\mathrm{Pe}_\Delta/2$ times the physical diffusion; if that ratio is above 1 the physical diffusion is being overwhelmed.
- A time step far above the CFL limit with an explicit scheme gives growing oscillations and then overflow within a few steps.
- Doubling the mesh resolution should change a second-order result by about a quarter of the previous change.

## Further reference

- Versteeg and Malalasekera, *An Introduction to Computational Fluid Dynamics: The Finite Volume Method*. A standard text for the finite-volume method and pressure-velocity coupling.
- Ferziger, Peric, and Street, *Computational Methods for Fluid Dynamics*. Discretization, stability, and turbulence modeling in depth.
- Toro, *Riemann Solvers and Numerical Methods for Fluid Dynamics*. Compressible flow, shocks, and approximate Riemann solvers.
- Pope, *Turbulent Flows*. The energy cascade, Kolmogorov scales, and the modeling hierarchy.
- MIT OpenCourseWare, the numerical fluid mechanics course 2.29, for lecture notes on finite-volume methods and stability.
- Related sheets in this repo: [verification and validation](reference-verification-validation.md), [thermal-fluids](../physics/reference-thermofluids.md), heat transfer ([physics/reference-heat-transfer.md](../physics/reference-heat-transfer.md)), [compressible flow](../physics/reference-compressible-flow.md).
