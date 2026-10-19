# Fixture reference

**Type:** reference
**Verify:** strict

A sheet whose variables give missing, unknown, or non-SI units.

## Principles

- Fixture.

## No unit column

$$\sigma = \frac{P}{A}$$

Variables:

| Symbol | Meaning |
|---|---|
| $\sigma$ | stress |

Holds when: the load is central.
Breaks when: the bar has holes.
Source and basis: derived from equilibrium.

## Bad unit cells

$$\phi = \frac{T L}{G J}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\phi$ | angle of twist | deg |
| $T$ | torque | lbf in |
| $L$ | length | furlong |
| $G$ | shear modulus | |
| $J$ | polar moment | $\text{m}^{4}$ |

Holds when: the shaft is circular.
Breaks when: the section warps.
Source and basis: derived from plane sections that rotate rigidly.

## Bad list items

$$F = k x$$

Variables:

- $F$: spring force
- $k$: stiffness [psi]

Holds when: the spring is linear.
Breaks when: coils touch.
Source and basis: derived from a measured curve.

## Further reference

- Named books only.
