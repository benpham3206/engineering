# Fixture reference

**Type:** reference
**Verify:** strict

A sheet that meets the reference-entry contract, used by the verifier tests.

## Principles

- Every formula names its symbols, its limits, and its basis.

## Axial bar

$$\sigma = \frac{P}{A}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\sigma$ | axial normal stress | Pa |
| $P$ | axial force | kN |
| $A$ | cross-section area | $\text{m}^{2}$ |
| $\varepsilon$ | strain | dimensionless |

Holds when: the load acts through the centroid of a uniform bar.
Breaks when: holes or fillets raise the local stress.
Source and basis: derived from equilibrium of a cut bar; taught in [Axial and torsion](../../physics/04-axial-and-torsion.md).

## Spring

$$
F = k x
$$

Variables:

- $F$: spring force [N]
- $k$: stiffness [N/m]
- $x$: stretch [mm]

Holds when: the spring stays in its linear range.
Breaks when: coils touch or the wire yields.
Source and basis: derived from a measured linear force-stretch curve.

## Further reference

- Named books only.
