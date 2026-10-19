# Simulation verification and validation reference

**Type:** reference
**Verify:** strict

Lookup sheet for the convergence, error-estimate, and validation formulas that show whether a numerical simulation solves its equations correctly and whether those equations describe the physical system, for an engineer who must put a number on a simulation result before anyone relies on it.

## Principles

- **Verification** is the check that the code and the numerical solution solve the chosen equations correctly. **Validation** is the check that those equations describe the physical system well enough for the intended use. Verification asks whether the equations are solved right; validation asks whether they are the right equations.
- **Calibration** is tuning model inputs so output matches data. It is neither verification nor validation, and a calibrated model still has to be validated against data that were not used to tune it.
- Verification comes first. A validation comparison on a result with unknown numerical error cannot separate a modeling error from a discretization error.
- Code verification tests the software against a known exact solution. Solution verification estimates the numerical error of one particular run, where no exact solution exists.
- Agreement with experiment is never proof of correctness. Two large errors can cancel, and a single case checks one point in the input space.
- A simulation result without an error estimate is a number with unknown meaning. Report the estimate with the result.
- Name every error source: discretization, iteration, round-off, input, model form, and experiment. An error source that was not estimated is unknown, not zero.
- Validation holds only inside the range of conditions tested. Use outside that range is a new claim that needs its own evidence.
- Conservation of mass, momentum, and energy is a free independent check. A solution that violates a conserved balance by more than its estimated numerical error has a defect.
- Convergence of one monitored quantity says nothing about quantities that were not monitored. Pick the monitored quantity from the engineering question.

## Code verification

### Order-of-accuracy test

Code verification measures how the error of the code against a known exact solution falls as the mesh or step is refined, and compares the result to the order the numerical method is designed to have.

$$E = f_h - f_{\text{exact}} \approx C\, h^{p} \qquad p = \frac{\ln\left(E_2 / E_1\right)}{\ln r}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $E$ | discretization error of the monitored quantity | m/s |
| $f_h$ | numerical value on a mesh of size $h$ | m/s |
| $f_{\text{exact}}$ | exact value | m/s |
| $C$ | error constant, independent of $h$ | m/s |
| $h$ | representative mesh size or step | m |
| $p$ | observed order of accuracy | dimensionless |
| $E_1$, $E_2$ | errors on the fine and coarse mesh | m/s |
| $r$ | refinement ratio, $h_2 / h_1$ | dimensionless |

Holds when: an exact solution exists, both meshes are in the asymptotic range (the error is dominated by the leading term $C h^p$), and the meshes are geometrically similar.
Breaks when: the mesh is too coarse for the leading term to dominate, a lower-order boundary treatment hides the interior order, round-off or iterative error is comparable to $E$, or the exact solution is not smooth (shocks and singularities pull the observed order below the design order).
Source and basis: derived from the Taylor-series form of truncation error, taught in [Numerical methods](../math/08-numerical-methods.md); the error orders of common methods are in [math/reference-probability-numerical-methods.md](../math/reference-probability-numerical-methods.md).

Example. A second-order code has a fine-mesh error of 0.0026 m/s and a coarse-mesh error of 0.0100 m/s with $r = 2$. The observed order is 1.943, a shortfall of about 3 percent from the design order of 2.

```verify
E1 = q(0.0026, "m/s")
E2 = q(0.0100, "m/s")
r = q(2, "")
p = log(E2 / E1) / log(r)
expect(p, "1.943")
check(p > q(1.8, ""), "within 10 percent of the design order of 2")
given("3")
```

### Method of manufactured solutions

The **method of manufactured solutions (MMS)** builds a test problem by choosing a smooth function $u_m$, applying the governing operator $L$ to it, and adding the result as a source term, so that $u_m$ becomes the exact solution of the modified problem.

$$L(u) = 0 \quad \longrightarrow \quad L(u) = s, \qquad s := L(u_m)$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $L$ | governing differential operator | dimensionless |
| $u$ | unknown field | dimensionless |
| $u_m$ | chosen manufactured solution | dimensionless |
| $s$ | source term added to the equations | dimensionless |

Holds when: $u_m$ is smooth, exercises every term of the operator, stays inside the physical bounds of the model (positive density, for example), and the boundary conditions are set from $u_m$.
Breaks when: $u_m$ is so simple that a term in the operator vanishes (an untested term cannot be verified), the source is coded with the same mistake as the operator, or the code uses a different formulation near boundaries than in the interior.
Source and basis: derived from the definition of the exact solution of a modified problem; choosing the solution first is the same idea as the hand checks in [Finite element method](01-finite-element-method.md).

Example. For $-u'' = s$ on $0 \le x \le 1$ choose $u_m = \sin(\pi x)$. Then $s = \pi^2 \sin(\pi x)$, which at $x = 0.5$ is 9.870 in nondimensional units. The values $u_m(0) = u_m(1) = 0$ are the boundary conditions.

```verify
x = q(0.5, "")
s = pi**2 * sin(pi * x)
expect(s, "9.870")
```

After the source is coded, run the order-of-accuracy test above on a sequence of meshes. A pass is an observed order that matches the design order on all of them.

## Solution verification

### Iterative convergence

**Iterative convergence** is the settling of an iterative solver (a linear solver, a nonlinear loop, or a pseudo-time march) onto the solution of the discrete equations. The residual is the amount by which the current iterate fails to satisfy those equations.

$$\rho = \frac{\Delta_n}{\Delta_{n-1}} \qquad e_n \approx \frac{\rho}{1 - \rho}\, \Delta_n$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\Delta_n$ | change in the monitored quantity over iteration $n$, $\lvert f_n - f_{n-1} \rvert$ | m/s |
| $\rho$ | observed convergence rate, per iteration | dimensionless |
| $e_n$ | estimated remaining iterative error in the monitored quantity | m/s |

Holds when: convergence is linear and monotone, so the changes shrink by a roughly constant factor $\rho < 1$.
Breaks when: the residual stalls or oscillates (a limit cycle or unsteady physics), the rate changes between iterations, or $\rho$ is near 1, where the estimate is very large and unreliable.
Source and basis: derived from the sum of a geometric series of future changes, $\Delta_n (\rho + \rho^2 + \dots) = \Delta_n \rho / (1 - \rho)$.

Example. Successive changes in a monitored velocity are 0.0200 m/s and then 0.0100 m/s, so $\rho = 0.5$ and the remaining iterative error is about 0.0100 m/s. A residual norm that fell from 1.0 to 0.00001 is a drop of 5 orders of magnitude.

```verify
d_prev = q(0.0200, "m/s")
d_now = q(0.0100, "m/s")
rho = d_now / d_prev
expect(rho, "0.5")
e = rho / (1 - rho) * d_now
expect(e, "0.0100 m/s")
drop = log10(q(1.0, "") / q(0.00001, ""))
expect(drop, "5")
```

- Reduce the residual until the iterative error in the monitored quantity is far below the discretization error, a common target being one tenth of it or less.
- Residual reduction alone is not enough. Watch the monitored quantities (a force, a flow rate, a peak temperature) until they stop changing in the digits that will be reported.
- A normalized residual depends on the scaling used, so state the norm and the scaling.
- For unsteady runs, converge the inner iterations at every time step, then judge the time-step error separately.

## Spatial and temporal refinement

### Refinement ratio and observed order from three grids

The **refinement ratio** $r$ is the ratio of the representative mesh size of a coarser mesh to that of the next finer mesh. With three meshes of constant ratio $r$ and solutions $f_1$ (fine), $f_2$ (medium), and $f_3$ (coarse), the observed order of accuracy follows from the solutions alone, with no exact solution needed.

$$r = \frac{h_2}{h_1} = \left(\frac{N_1}{N_2}\right)^{1/d} \qquad p = \frac{\ln\left(\dfrac{f_3 - f_2}{f_2 - f_1}\right)}{\ln r}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $r$ | constant refinement ratio between successive meshes | dimensionless |
| $h_1$, $h_2$ | representative mesh size of the fine and medium mesh | m |
| $N_1$, $N_2$ | number of cells or nodes on the fine and medium mesh | dimensionless |
| $d$ | number of spatial dimensions refined | dimensionless |
| $f_1$, $f_2$, $f_3$ | monitored quantity on the fine, medium, and coarse mesh | m/s |
| $p$ | observed order of accuracy | dimensionless |

Holds when: all three solutions are in the asymptotic range, the refinement ratio is constant, the solutions converge monotonically ($f_3 - f_2$ and $f_2 - f_1$ have the same sign), and the meshes are geometrically similar.
Breaks when: the change in the monitored quantity reverses sign between meshes (oscillatory convergence gives a negative argument of the logarithm), the ratio $r$ is small so that discretization error is lost in iteration and round-off noise, or the refinement is not uniform in all directions.
Source and basis: [NASA Glenn spatial convergence page](https://www.grc.nasa.gov/www/wind/valid/tutorial/spatconv.html), registered in [claims](../data/claims/simulation-vv.md#nasa-grc-spatial-convergence); derived from the error model $f_k = f_{\text{exact}} + C h_k^p$.

Example. Take $r = 2$ and $f_1 = 1.0100$, $f_2 = 1.0400$, $f_3 = 1.1500$ m/s. The change ratio is $0.1100 / 0.0300$ and $p$ is 1.874. A mesh of 2000000 cells in $d = 3$ against 250000 cells on the next coarser mesh has $r = 2$, because $8^{1/3} = 2$.

```verify
f1 = q(1.0100, "m/s")
f2 = q(1.0400, "m/s")
f3 = q(1.1500, "m/s")
r = q(2, "")
p = log((f3 - f2) / (f2 - f1)) / log(r)
expect(p, "1.874")
N1 = q(2000000, "")
N2 = q(250000, "")
expect((N1 / N2)**(q(1, "") / 3), "2")
given("0.1100", "0.0300")
```

- Use a refinement ratio of at least about 1.3, and prefer 2 when the cost allows.
- Refine in every direction by the same ratio, and keep the mesh quality metrics (skewness, aspect ratio, smoothness) the same across the sequence.
- Refine the time step on the same ratio when time accuracy matters, and refine space and time together so that neither hides the other.
- For a non-integer ratio or unequal ratios, the order is the root of a fixed-point equation instead of the closed form above; see [simulation/reference-finite-element-analysis.md](reference-finite-element-analysis.md) and [simulation/reference-computational-fluid-dynamics.md](reference-computational-fluid-dynamics.md) for their mesh practice.

### Richardson extrapolation

**Richardson extrapolation** estimates the exact (zero mesh size) value of a quantity from two solutions on meshes of different size, by removing the leading error term.

$$f_{h \to 0} \approx f_1 + \frac{f_1 - f_2}{r^{p} - 1}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $f_{h \to 0}$ | extrapolated estimate of the exact value | m/s |
| $f_1$ | fine-mesh solution | m/s |
| $f_2$ | medium-mesh solution | m/s |
| $r$ | refinement ratio | dimensionless |
| $p$ | order of accuracy, observed or formal | dimensionless |

Holds when: both solutions are in the asymptotic range, the order $p$ is the true leading order, and convergence is monotone.
Breaks when: the order is unknown or wrong (use the three-grid observed order, or report only a bound), the solution has shocks, singularities, or model switches that change the order, or the extrapolated value is presented as a prediction without saying it is an estimate with its own uncertainty.
Source and basis: [NASA Glenn spatial convergence page](https://www.grc.nasa.gov/www/wind/valid/tutorial/spatconv.html), registered in [claims](../data/claims/simulation-vv.md#nasa-grc-spatial-convergence); derived from eliminating $C$ between $f_1 = f_{\text{exact}} + C h_1^p$ and $f_2 = f_{\text{exact}} + C (r h_1)^p$.

Example. With the three-grid values above, $r^p = 3.667$ and the extrapolated value is 0.9987 m/s. The fine-mesh value is 0.0113 m/s above it.

```verify
f1 = q(1.0100, "m/s")
f2 = q(1.0400, "m/s")
f3 = q(1.1500, "m/s")
r = q(2, "")
p = log((f3 - f2) / (f2 - f1)) / log(r)
rp = r**p
expect(rp, "3.667")
fx = f1 + (f1 - f2) / (rp - 1)
expect(fx, "0.9987 m/s")
expect(f1 - fx, "0.0113 m/s")
```

### Grid convergence index and asymptotic range

The **grid convergence index (GCI)** converts the difference between two mesh solutions into a stated relative error band on the finer solution, with a safety factor because the estimate comes from only a few meshes.

$$\mathrm{GCI}_{12} = \frac{F_s \left\lvert \dfrac{f_1 - f_2}{f_1} \right\rvert}{r^{p} - 1} \qquad \mathrm{GCI}_{23} = \frac{F_s \left\lvert \dfrac{f_2 - f_3}{f_2} \right\rvert}{r^{p} - 1} \qquad \frac{\mathrm{GCI}_{23}}{r^{p}\, \mathrm{GCI}_{12}} \approx 1$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\mathrm{GCI}_{12}$ | relative error band on the fine-mesh solution | dimensionless |
| $\mathrm{GCI}_{23}$ | relative error band on the medium-mesh solution | dimensionless |
| $F_s$ | safety factor, 1.25 for three or more meshes and 3.0 for two | dimensionless |
| $f_1$, $f_2$, $f_3$ | solutions on the fine, medium, and coarse mesh | m/s |
| $r$ | refinement ratio | dimensionless |
| $p$ | observed order of accuracy | dimensionless |

Holds when: the three solutions converge monotonically, the error follows $C h^p$, and the last ratio is close to 1, which shows the meshes are in the asymptotic range.
Breaks when: the ratio is far from 1 (the meshes are not asymptotic, so the band is unreliable and the mesh needs further refinement), convergence is oscillatory, the observed order is far above the formal order (a very large $p$ makes the band too small to trust, so cap $p$ at the formal order), or the monitored quantity is near zero (use an absolute difference in place of the relative one).
Source and basis: the formulas and the safety factors 1.25 and 3.0 are from the [NASA Glenn spatial convergence page](https://www.grc.nasa.gov/www/wind/valid/tutorial/spatconv.html), registered in [claims](../data/claims/simulation-vv.md#nasa-grc-gci-safety-factors); the asymptotic check follows from the scaling of the two bands by $r^p$.

Example. With $F_s = 1.25$, $r = 2$ and the three-grid values above, $\mathrm{GCI}_{12}$ is 1.39 percent and $\mathrm{GCI}_{23}$ is 4.96 percent. The ratio $\mathrm{GCI}_{23} / (r^p \mathrm{GCI}_{12})$ is 0.971, so the meshes are close to the asymptotic range. The fine-mesh result is stated as 1.0100 m/s with an error band of 0.0141 m/s.

```verify
Fs = q(1.25, "")
f1 = q(1.0100, "m/s")
f2 = q(1.0400, "m/s")
f3 = q(1.1500, "m/s")
r = q(2, "")
p = log((f3 - f2) / (f2 - f1)) / log(r)
rp = r**p
g12 = Fs * abs((f1 - f2) / f1) / (rp - 1)
g23 = Fs * abs((f2 - f3) / f2) / (rp - 1)
expect(g12 * 100, "1.39")
expect(g23 * 100, "4.96")
expect(g23 / (rp * g12), "0.971")
expect(g12 * f1, "0.0141 m/s")
```

- Report the fine-mesh value, its GCI, the observed order, and the asymptotic check together.
- A band from two meshes uses the factor 3.0 and the formal order. It cannot test the asymptotic range, so it is a weaker statement than the three-mesh band.

## Conservation checks

A **conservation check** compares what a solution carries into a control volume with what it carries out. A converged solution of a conservative scheme balances to within the iterative error, so a larger imbalance points to a defect.

$$\epsilon_m = \frac{\dot{m}_{\text{in}} - \dot{m}_{\text{out}}}{\dot{m}_{\text{in}}}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\epsilon_m$ | relative mass imbalance | dimensionless |
| $\dot{m}_{\text{in}}$ | mass flow rate into the control volume | kg/s |
| $\dot{m}_{\text{out}}$ | mass flow rate out of the control volume | kg/s |

Holds when: the flow is steady and no mass is stored or produced inside the volume, and inflow and outflow are both counted positive.
Breaks when: the flow is unsteady (include the storage rate), mass is added by a source, or the balance is computed from rounded boundary values.
Source and basis: derived from conservation of mass; the same form applies to energy, using the net heat and work rates, and to force, using the sum of reactions and applied loads.

Example. A steady run has an inflow of 2.500 kg/s and an outflow of 2.462 kg/s. The imbalance is 1.52 percent, far above a converged residual, so the solution is not finished or has a boundary defect.

```verify
mi = q(2.500, "kg/s")
mo = q(2.462, "kg/s")
eps = (mi - mo) / mi
expect(eps * 100, "1.52")
```

- Mass: net flow through every closed surface, and through each inlet and outlet.
- Energy: heat in minus heat out minus net work equals the change in stored energy.
- Force and moment: the sum of the support reactions equals the applied load in a structural model. A mismatch larger than the equation-solver tolerance is a bug in the loads or the constraints.
- Check the conserved quantity on subregions too. A global balance can hide a local source and sink that cancel.

## Uncertainty and validation comparison

A **validation comparison** sets the simulation result $S$ against an experimental result $D$ and asks whether their difference is explained by the uncertainties of the simulation and the experiment. The **comparison error** is the difference, and the **validation uncertainty** is the combined uncertainty of everything that makes the two values differ other than model-form error.

$$E = S - D \qquad u_{\text{val}} = \sqrt{u_{\text{num}}^{2} + u_{\text{input}}^{2} + u_{D}^{2}}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $E$ | comparison error | N |
| $S$ | simulation result | N |
| $D$ | experimental result | N |
| $u_{\text{val}}$ | validation standard uncertainty | N |
| $u_{\text{num}}$ | numerical standard uncertainty (discretization, iteration, round-off) | N |
| $u_{\text{input}}$ | standard uncertainty of the result caused by uncertain model inputs | N |
| $u_{D}$ | standard uncertainty of the experimental result | N |

Holds when: the three parts are independent (the root-sum-square assumption), each is a standard uncertainty with the same coverage, and the experiment measures the same quantity under the same conditions as the simulation.
Breaks when: the parts are correlated (for example one measured boundary condition feeds both the experiment and the simulation, so add the covariance), the numerical error is a one-sided bias and not a symmetric uncertainty, or the experiment does not measure what the simulation computes.
Source and basis: derived from the propagation of independent uncertainties in [Propagating uncertainty and significant figures](../measurement/03-propagating-uncertainty-and-significant-figures.md); the measurement background is in [Measurement reference](../measurement/reference.md).

Example. A simulation predicts a load of 101.2 N and the test measured 98.0 N. The numerical, input, and experimental uncertainties are 1.0 N, 1.5 N, and 1.2 N. The comparison error is 3.2 N and the validation uncertainty is 2.17 N. Because $\lvert E \rvert$ exceeds $u_{\text{val}}$, the stated uncertainties do not explain the difference, and the remainder is attributed to model-form error.

```verify
S = q(101.2, "N")
D = q(98.0, "N")
un = q(1.0, "N")
ui = q(1.5, "N")
ud = q(1.2, "N")
E = S - D
expect(E, "3.2 N")
uv = sqrt(un**2 + ui**2 + ud**2)
expect(uv, "2.17 N")
check(abs(E) > uv, "difference is larger than the validation uncertainty")
```

- If $\lvert E \rvert$ is within $u_{\text{val}}$ (or within the chosen coverage multiple of it), the model is not shown wrong at that level. That is not proof that it is right.
- If $\lvert E \rvert$ is well above $u_{\text{val}}$, the remainder estimates the model-form error at that condition.
- Take $u_{\text{num}}$ from the GCI band, converted to a standard uncertainty with the coverage stated, and $u_{\text{input}}$ from propagating the input uncertainties through the model by sampling or by sensitivity.

## Validation hierarchy

Validation proceeds from simple cases to the full system, so that a discrepancy can be traced to one cause. Each tier uses data that are better controlled than the one above it.

| Tier | What is compared | What a discrepancy points to |
|---|---|---|
| Unit problem | One physical effect with an analytical or very precise reference (flat-plate boundary layer, beam deflection, steady conduction) | The model of that effect, or the code |
| Benchmark case | A documented experiment of a few coupled effects, with measured boundary conditions | Coupling of effects, or a missing effect |
| Subsystem | A real component with realistic geometry and loads, measured on a test rig | Geometry, boundary conditions, or scaling |
| Full system | The complete product at operating conditions | Interactions between subsystems; data are scarce and experimental uncertainty is large |

- Lower tiers cost less and attribute error more cleanly. Higher tiers carry more of the real conditions but mix causes.
- Match the tier to the intended use. A model used to rank design variants needs the tiers that exercise the differences between the variants.
- Document the validation domain, the range of parameters covered. Use outside it is extrapolation.

## Credibility and reporting

A credible simulation report states enough that a reader who was not present can judge the result and repeat it. At minimum it states:

1. The question the simulation answers and the decision it supports.
2. The governing equations and models, and their known limits for this use.
3. The software, its version, the solver settings, and the mesh or step sequence.
4. The inputs and their uncertainties, with sources.
5. The verification evidence: code verification, iterative convergence, and the grid convergence results with the observed order and the GCI.
6. The conservation checks and their results.
7. The validation evidence and domain, with the comparison error and $u_{\text{val}}$.
8. The assumptions, the limitations, and the cases for which the result is not valid.
9. The conclusion with its uncertainty, and how far the result may be relied upon.

NASA-STD-7009, the Standard for Models and Simulations, establishes uniform practices in modeling and simulation, as of 2026 in Version B [src](../data/claims/simulation-vv.md#nasa-std-7009-purpose). A paid standard from another body is named by title only.

## Checklists

Before trusting a result:

- The code passed an order-of-accuracy test for the options in use, or a comparable test is cited.
- The residual dropped by the target number of orders and the monitored quantities stopped changing.
- Three meshes with a constant refinement ratio were run, and the observed order was computed.
- Convergence was monotone and the asymptotic check is close to 1.
- The GCI or other error band is stated with its safety factor.
- Mass, energy, and force balances close to within the iterative error.
- For unsteady runs, the time step was refined as well as the mesh.
- Inputs and their uncertainties are listed, and their effect on the result is estimated.
- The comparison error and the validation uncertainty are computed, with the independence assumption stated.
- The validation domain covers the conditions of the intended use.

## Sanity checks

- Halving $h$ for a second-order method should cut the error by a factor of about 4, and for a first-order method by about 2.
- The observed order should be close to the formal order. A value near 0.5 or near 5 for a second-order scheme means the meshes are not asymptotic, another error dominates, or there is a bug.
- The extrapolated value should lie beyond the fine-mesh value, in the direction of the trend. If it lies on the other side, convergence is not monotone.
- A GCI of a few percent of the monitored quantity is normal for engineering work. A band of 0.0001 percent from three coarse meshes is suspicious.
- Halving the cell size in three dimensions multiplies the cell count by 8 and the cost by more, because the time step usually shrinks as well.
- Reporting six digits from a result with a 2 percent error band overstates what is known. Round to the band.

## Further reference

- [NASA Glenn Research Center, spatial convergence page of the verification and validation tutorial](https://www.grc.nasa.gov/www/wind/valid/tutorial/spatconv.html), the free source for the Richardson and GCI formulas above.
- [NASA technical standards page for NASA-STD-7009](https://standards.nasa.gov/standard/nasa/nasa-std-7009).
- *Guide for the Verification and Validation of Computational Fluid Dynamics Simulations*, AIAA G-077-1998.
- *Verification and Validation in Scientific Computing*, W. L. Oberkampf and C. J. Roy.
- ASME V&V 20, *Standard for Verification and Validation in Computational Fluid Dynamics and Heat Transfer*.
- [Finite element method](01-finite-element-method.md), [Numerical methods](../math/08-numerical-methods.md), [Precision, accuracy, and uncertainty](../measurement/02-precision-accuracy-and-uncertainty.md).
