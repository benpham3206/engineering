# Fracture and fatigue reference

**Type:** reference
**Verify:** strict

Lookup sheet for how cracks carry load and grow, covering stress intensity, fracture toughness, crack growth under repeated load, and fatigue life from stress and strain, for an engineer who must decide whether a flawed or cyclically loaded part survives. This sheet owns the fracture and fatigue equations; the lessons that teach them are [Failure: fracture and fatigue](06-fracture-and-fatigue.md) and [Mechanical properties](03-mechanical-properties.md).

## Principles

- A crack concentrates stress without limit in the elastic model, so the stress at a crack tip cannot be the design measure. The stress intensity factor $K$ measures the strength of that concentration, and a part fractures when $K$ reaches the toughness of the material.
- Strength and toughness are separate properties. A high-strength alloy can tolerate a smaller flaw than a weaker, tougher one.
- Fracture is set by stress and flaw size together. Doubling the flaw size at a fixed stress multiplies $K$ by $\sqrt{2}$; dividing the stress by $\sqrt{2}$ cancels that rise.
- Fatigue cracks grow in cycles, from flaws that are always present, at stresses well below yield. A part that passes a static check can still fail from a crack that grows a little each cycle.
- Fatigue life depends on stress amplitude to a high power, so a small error in stress is a large error in life. In the Paris model with $n = 3$, reducing the stress range by 10 percent lengthens life by about 1.37 times when geometry stays fixed.
- Fatigue scatters. Life at one stress varies over a factor of ten or more between nominally identical parts, so a computed life is a median to be reduced by a scatter factor, not a promise.
- Notches, surface finish, corrosion, and residual stress change fatigue life more than most changes in the average stress do. Check where the crack will start, not only the nominal section.
- Fracture mechanics and the stress-life approaches answer different questions. Fracture mechanics grows a crack that is assumed to exist, and stress-life or strain-life predicts the cycles to start one.
- Every empirical constant (Paris $C$ and $n$, Basquin $b$, toughness) belongs to one material, condition, temperature, environment, and stress ratio. Use values measured at those conditions.
- Linear elastic fracture mechanics holds only while yielding at the crack tip stays small compared with the crack and the section. Outside that limit, use elastic-plastic methods.

## Crack-tip fields and modes

A **crack** is a sharp, planar flaw in a solid, and its **mode** is the way the two crack faces move relative to each other.

- Mode I (opening): the faces separate normal to the crack plane, driven by tension across the crack.
- Mode II (sliding): the faces slide over each other in the crack plane, normal to the crack front, driven by in-plane shear.
- Mode III (tearing): the faces slide along the crack front, driven by out-of-plane shear.

In the elastic model, directly ahead of a mode I crack (angle $\theta = 0$) the opening stress is

$$\sigma_{yy} = \frac{K_I}{\sqrt{2 \pi r}}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\sigma_{yy}$ | opening stress ahead of the crack, normal to the crack plane | Pa |
| $K_I$ | mode I stress intensity factor | $\text{N}/\text{m}^{3/2}$ |
| $r$ | distance ahead of the crack tip | m |

Holds when: the material is linear elastic, the crack is sharp, and $r$ is small compared with the crack length and the remaining ligament but large compared with the plastic zone.
Breaks when: $r$ is inside the plastic zone, where the real stress is capped near yield, or the load has a large shear component (mix modes II and III in, and the crack may turn).
Source and basis: Irwin's elastic crack-tip mode field [src](../data/claims/fracture-fatigue.md#fracture-crack-tip-field-modes).

Example. A crack has $K_I = 18.8$ MPa times the square root of metre. At $r = 0.1$ mm ahead of the tip, the elastic opening stress is far above any yield strength, which shows why the elastic field must give way to a plastic zone very near the tip.

```verify
rtm = sqrt(q(1, "m"))
K = q(18.8, "MPa") * rtm
r = q(0.1, "mm")
s = K / sqrt(2 * pi * r)
expect(s, "750 MPa")
```

The elastic opening stress is 750 MPa at that point.

## Stress-intensity factors

The **stress intensity factor** $K$ is the single number that sets the size of the crack-tip stress field for a given crack, load, and geometry. For mode I,

$$K_I = Y \sigma \sqrt{\pi a}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $K_I$ | mode I stress intensity factor | $\text{N}/\text{m}^{3/2}$ |
| $Y$ | geometry factor (1 for a center crack in a very wide plate) | dimensionless |
| $\sigma$ | remote stress normal to the crack plane, computed on the uncracked section | Pa |
| $a$ | crack length (half the length for a center crack, depth for an edge or surface crack) | m |

Holds when: the plate is loaded in tension, the crack is a sharp slit of length small compared with the plate width, and yielding at the tip is small.
Breaks when: the crack is a large fraction of the width (use a finite-width factor from the next section), the geometry has a stress gradient across the crack (use the handbook factor for that geometry), or the tip plastic zone is not small (see the plastic-zone entry).
Source and basis: Irwin's stress intensity factor approach for cracks, applied to the Griffith slit problem [src](../data/claims/fracture-fatigue.md#fracture-k-factor-forms).

Superposition holds within one mode. For separate loads that all open the crack, add their factors, $K_I = K_{I,1} + K_{I,2} + \dots$ Factors of different modes never add, because they act on different crack-face motions. The energy release rates of the modes do add, as shown in the energy entry below [src](../data/claims/fracture-fatigue.md#fracture-crack-tip-field-modes).

Units. $K$ has SI units $\text{Pa}\,\text{m}^{1/2}$, equivalent to $\text{N}/\text{m}^{3/2}$. Convert the crack length to metres before taking the square root. Common converted values are given in Sanity checks.

Example. A wide plate with $Y = 1$ has a center-crack half-length of 4 mm under 100 MPa tension.

```verify
rtm = sqrt(q(1, "m"))
a = q(4, "mm")
sig = q(100, "MPa")
expect(sig * sqrt(pi * a) / rtm, "11.2 MPa")
```

The stress intensity is $11.2\ \text{MPa}\,\text{m}^{1/2}$.

## Geometry factors

A **geometry factor** $Y$ is the dimensionless multiplier that adjusts the wide-plate result for the real crack shape and the finite size of the part. Only factors that can be sourced are listed here, each with its validity range.

Center crack of half-length $a$ in a very wide plate in tension: $Y = 1$.

Edge crack of depth $a$ in a plate of width $W$ in uniform tension, with $\alpha = a/W$:

$$Y = 1.122 - 0.231\,\alpha + 10.55\,\alpha^{2} - 21.71\,\alpha^{3} + 30.382\,\alpha^{4}$$

Embedded circular (penny-shaped) crack of radius $a$ in an infinite body under uniform tension:

$$K_I = \frac{2}{\pi}\,\sigma \sqrt{\pi a}$$

Shallow semi-circular surface crack of depth $a$, free surface treated with the factor 1.12:

$$K_I = 1.12\,\frac{2}{\pi}\,\sigma \sqrt{\pi a}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $Y$ | geometry factor | dimensionless |
| $\alpha$ | crack depth over plate width, $a/W$ | dimensionless |
| $a$ | edge or surface crack depth, or penny crack radius | m |
| $W$ | plate width | m |
| $\sigma$ | remote tensile stress on the uncracked section | Pa |
| $K_I$ | mode I stress intensity factor | $\text{N}/\text{m}^{3/2}$ |

Holds when: the edge-crack polynomial is used for $\alpha \le 0.6$ under uniform tension; the penny crack lies far from any surface and edge; the surface-crack form is used for a semi-circular crack that is shallow compared with the plate thickness.
Breaks when: $\alpha > 0.6$ for the polynomial; the crack is elliptical with a different aspect ratio (use the elliptic-integral solutions in the source); or the surface crack depth exceeds about half the thickness (a back-surface correction is then needed).
Source and basis: handbook stress intensity factor solutions for cracks collected in the NASA primer [src](../data/claims/fracture-fatigue.md#fracture-k-factor-forms).

As $\alpha \to 0$ the polynomial gives $Y \to 1.122$, the familiar 1.12 for an edge crack in a wide plate.

Example. An edge crack 4 mm deep in a plate 20 mm wide carries 100 MPa. The depth ratio is 0.2. A penny crack of radius 2 mm in a large body carries the same 100 MPa for comparison.

```verify
rtm = sqrt(q(1, "m"))
al = q(4, "mm") / q(20, "mm")
expect(al, "0.2")
Y = 1.122 - 0.231 * al + 10.55 * al**2 - 21.71 * al**3 + 30.382 * al**4
expect(Y, "1.373")
sig = q(100, "MPa")
a = q(4, "mm")
K_edge = Y * sig * sqrt(pi * a)
expect(K_edge / rtm, "15.4 MPa")
K_penny = (2 / pi) * sig * sqrt(pi * q(2, "mm"))
expect(K_penny / rtm, "5.05 MPa")
```

The edge crack gives $Y = 1.373$ and $K_I = 15.4\ \text{MPa}\,\text{m}^{1/2}$. The penny crack gives $K_I = 5.05\ \text{MPa}\,\text{m}^{1/2}$.

## Energy release rate

The **energy release rate** $G$ is the elastic energy released per unit of new crack area when the crack extends, and it is the crack driving force in energy terms. For the Griffith slit (center crack of half-length $a$ in a wide plate under remote stress $\sigma$),

$$G = \frac{\pi \sigma^{2} a}{E'} = \frac{K_I^{2}}{E'}, \qquad \sigma_c = \sqrt{\frac{E' G_c}{\pi a}}$$

where $E' = E$ for plane stress and $E' = E/(1 - \nu^{2})$ for plane strain.

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $G$ | energy release rate | $\text{J/m}^2$ |
| $G_c$ | critical energy release rate, the toughness in energy terms | $\text{J/m}^2$ |
| $\sigma$ | remote tensile stress | Pa |
| $\sigma_c$ | remote stress at fracture | Pa |
| $a$ | crack half-length | m |
| $E'$ | effective modulus, $E$ or $E/(1-\nu^{2})$ | Pa |
| $E$ | Young's modulus | Pa |
| $\nu$ | Poisson's ratio | dimensionless |
| $K_I$ | mode I stress intensity factor | $\text{N}/\text{m}^{3/2}$ |

Holds when: the body is linear elastic, the load is held fixed during extension, and the crack is a through crack in a wide plate (the $K$ and $G$ forms are linked for any mode I geometry through $E'$).
Breaks when: plastic work is large, as in tough metals, where $G_c$ is mostly plastic work and the energy balance of an ideally brittle solid underestimates fracture strength.
Source and basis: Griffith energy balance, with the link of $G$ to $K$ from Irwin [src](../data/claims/fracture-fatigue.md#fracture-griffith-energy).

Surface energy gives $G_c = 2\gamma$ for an ideally brittle solid with surface energy $\gamma$ per surface. For metals the plastic work dominates $G_c$ and the surface energy is negligible. Mixed-mode loading adds energy release rates of the three modes, $G = G_I + G_{II} + G_{III}$ [src](../data/claims/fracture-fatigue.md#fracture-crack-tip-field-modes).

Example. A wide plate of an aluminium-like material has $E = 70$ GPa and $G_c = 20\ \text{kJ/m}^2$ (illustrative values; plane stress). A center crack with half-length 10 mm fractures at the remote stress below.

```verify
E = q(70, "GPa")
Gc = q(20, "kJ/m^2")
a = q(10, "mm")
sc = sqrt(E * Gc / (pi * a))
expect(sc, "211 MPa")
```

The remote fracture stress is 211 MPa.

## Fracture toughness and critical crack size

**Fracture toughness** $K_{Ic}$ is the value of $K_I$ at which a crack in a thick section runs unstably, a material property under plane-strain conditions. Setting $K_I = K_{Ic}$ in the stress intensity relation and solving for the crack size gives the **critical crack size**,

$$a_c = \frac{1}{\pi}\left(\frac{K_{Ic}}{Y \sigma}\right)^{2}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $a_c$ | critical crack size | m |
| $K_{Ic}$ | plane-strain fracture toughness | $\text{N}/\text{m}^{3/2}$ |
| $Y$ | geometry factor at the critical size | dimensionless |
| $\sigma$ | remote stress at the instant of failure | Pa |

Holds when: $Y$ is the factor for the actual geometry, evaluated at $a_c$ (iterate if $Y$ depends on $a$); the section is thick enough for plane strain (see the size rule below); the stress is the maximum in service.
Breaks when: the section is thin and plane-stress toughness $K_c$ is higher than $K_{Ic}$ (using $K_{Ic}$ is then conservative); the net-section stress approaches yield, so linear elastic fracture mechanics no longer holds; or temperature, loading rate, or environment differ from the test.
Source and basis: derived from the stress intensity relation, with $K_{Ic}$ as measured fracture toughness data [src](../data/claims/fracture-fatigue.md#fracture-toughness-size-rule).

Toughness falls as temperature falls in many steels. The primer reports one 4340 steel fracture toughness dropping from about 55 $\text{MPa}\sqrt{\text{m}}$ at 24 C to about 33 $\text{MPa}\sqrt{\text{m}}$ at -73 C [src](../data/claims/fracture-fatigue.md#fracture-toughness-size-rule). A toughness taken at room temperature does not cover a cold service.

The **plane-strain size requirement** is a rule for when a test or a design value of $K_{Ic}$ is valid: the thickness and crack length must be at least about 2.5 times the square of $K_{Ic}$ over the yield strength,

$$B,\ a \ge 2.5 \left(\frac{K_{Ic}}{S_y}\right)^{2}$$

where $B$ is the thickness. The test procedure is set by the ASTM standard test method for plane-strain fracture toughness of metallic materials (named by title only). The toughness rule needs $K_{Ic}$ in advance, so an expected value is used to size a specimen first and the result is then checked against it [src](../data/claims/fracture-fatigue.md#fracture-toughness-size-rule).

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $B$ | specimen or section thickness | m |
| $S_y$ | yield strength | Pa |

Holds when: the material yields in a classical way and the test is of a fatigue-precracked specimen.
Breaks when: the yield strength is high and the toughness low (the required size is then small, but scatter in $K_{Ic}$ is large), or the section is thinner than the rule (then only a plane-stress or apparent toughness is available).
Source and basis: ASTM-style fracture-toughness validity rule recorded in the NASA primer [src](../data/claims/fracture-fatigue.md#fracture-toughness-size-rule).

Example. A wide plate with an edge crack ($Y = 1.12$) works at a stress of 200 MPa. The alloy has $K_{Ic} = 38$ $\text{MPa}\sqrt{\text{m}}$ and $S_y = 455$ MPa (illustrative values of an aluminium alloy class).

```verify
rtm = sqrt(q(1, "m"))
K = q(38, "MPa") * rtm
Y = q(1.12, "1")
sig = q(200, "MPa")
ac = (1 / pi) * (K / (Y * sig))**2
expect(ac, "9.16 mm")
Sy = q(455, "MPa")
Bmin = 2.5 * (K / Sy)**2
expect(Bmin, "17.4 mm")
```

The critical crack depth is 9.16 mm, and a valid plane-strain test needs a thickness of 17.4 mm.

The crack that becomes critical is 9.2 mm deep, and a valid plane-strain test of this alloy needs a section about 17.4 mm thick.

## Small-scale yielding and plastic-zone size

**Small-scale yielding** is the condition that the plastic zone at the crack tip is small compared with the crack length and the section, so the elastic field of the crack still controls it. Irwin estimated the zone size by setting the elastic opening stress equal to the yield strength:

$$r_y = \frac{1}{2\pi}\left(\frac{K_I}{S_y}\right)^{2} \quad \text{(plane stress)}, \qquad r_y = \frac{1}{6\pi}\left(\frac{K_I}{S_y}\right)^{2} \quad \text{(plane strain)}$$

The zone extends about $2 r_y$ ahead of the tip once load is redistributed, and the crack acts as if it were longer by $r_y$, so a corrected crack length $a + r_y$ gives a corrected $K_I$.

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $r_y$ | first-order plastic-zone radius ahead of the crack tip | m |
| $K_I$ | mode I stress intensity factor | $\text{N}/\text{m}^{3/2}$ |
| $S_y$ | yield strength | Pa |
| $a$ | crack length | m |

Holds when: the zone is small, so that $r_y$ is a small fraction of $a$ and of the uncracked ligament, and the material is elastic-perfectly plastic.
Breaks when: the plastic zone is not small (the applied stress is a large fraction of yield), the section is thin and the zone spreads through the thickness, or the material work-hardens strongly (the estimate is then rough).
Source and basis: Irwin's plastic zone estimate [src](../data/claims/fracture-fatigue.md#fracture-irwin-plastic-zone).

Plane strain applies in the thick interior and gives the smaller zone by a factor of three. A thin plate is plane stress. A plate of intermediate thickness has a plane-stress zone at the surface and nearly plane strain inside [src](../data/claims/fracture-fatigue.md#fracture-irwin-plastic-zone).

Example. $K_I = 38$ $\text{MPa}\sqrt{\text{m}}$ and $S_y = 455$ MPa.

```verify
rtm = sqrt(q(1, "m"))
K = q(38, "MPa") * rtm
Sy = q(455, "MPa")
r_ps = (1 / (2 * pi)) * (K / Sy)**2
expect(r_ps, "1.11 mm")
r_pe = (1 / (6 * pi)) * (K / Sy)**2
expect(r_pe, "0.370 mm")
```

The plastic-zone radii are 1.11 mm in plane stress and 0.370 mm in plane strain.

## Leak-before-break

**Leak before break** (LBB) is the condition in which a flaw grows through the wall of a pressure vessel and the contents leak, giving warning, before the crack grows long enough to burst the vessel. The check compares the stress intensity of a through crack of the leaking length with the plane-stress toughness $K_c$. For an axial through crack of half-length $c$ in a thin-wall cylinder of radius $R$ and wall $t$ under internal pressure $p$,

$$K_I = \frac{p R}{t}\sqrt{\pi c}\,\sqrt{1 + 1.61\,\frac{c^{2}}{R\,t}}, \qquad K_I < K_c \text{ for leak before break}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $K_I$ | stress intensity of the axial through crack | $\text{N}/\text{m}^{3/2}$ |
| $K_c$ | plane-stress fracture toughness of the wall | $\text{N}/\text{m}^{3/2}$ |
| $p$ | internal gauge pressure | Pa |
| $R$ | mean cylinder radius | m |
| $t$ | wall thickness | m |
| $c$ | through-crack half-length | m |

Holds when: the wall is thin ($R/t$ about 10 or larger), the surface flaw breaks through with a through crack of about the flaw length, and the contents leak where the flaw breaks through and are detected.
Breaks when: leakage cannot be tolerated (design to a safe-life limit instead), the contents or the wall make a leak undetectable, the wall is thick so the crack front stays in plane strain, or the stress is high enough that the crack runs unstably at the surface-flaw stage.
Source and basis: Kanninen's approach to leak before burst, as given in the NASA primer [src](../data/claims/fracture-fatigue.md#fracture-leak-before-burst).

Example. $R = 0.5$ m, $t = 10$ mm, $p = 5$ MPa, and a surface flaw 50 mm long that breaks through with half-length $c = 25$ mm. Take $K_c = 100$ $\text{MPa}\sqrt{\text{m}}$ (illustrative).

```verify
rtm = sqrt(q(1, "m"))
p = q(5, "MPa")
R = q(0.5, "m")
t = q(10, "mm")
flaw_length = q(50, "mm")
c = flaw_length / 2
expect(c, "25 mm")
s = p * R / t
expect(s, "250 MPa")
fac = sqrt(1 + 1.61 * c**2 / (R * t))
expect(fac, "1.096")
K = s * sqrt(pi * c) * fac
expect(K / rtm, "76.8 MPa")
Kc = q(100, "MPa") * rtm
check(K < Kc, "through crack is stable, so the vessel leaks before it bursts")
```

The wall stress is 250 MPa, the geometry factor is 1.096, and the through-crack intensity is $76.8\ \text{MPa}\,\text{m}^{1/2}$, below the assumed toughness.

## Subcritical crack growth and the Paris law

**Subcritical crack growth** is the slow extension of a crack under a load too low to cause fracture, by cyclic load (fatigue), sustained load in a hostile environment, or both. For fatigue, the growth per cycle correlates with the range of the stress intensity factor in the cycle,

$$\frac{da}{dN} = C\left(\frac{\Delta K}{K_0}\right)^{n}, \qquad \Delta K = K_{\max} - K_{\min} = Y\,\Delta\sigma\sqrt{\pi a}$$

Use $K_0 = 1\ \text{MPa}\,\text{m}^{1/2}$ as the reference intensity when tabulating $C$. This equals $1,000,000\ \text{Pa}\,\text{m}^{1/2}$.

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $a$ | crack length | m |
| $N$ | number of load cycles | dimensionless |
| $C$ | Paris coefficient for $K_0 = 1\ \text{MPa}\,\text{m}^{1/2}$ | m |
| $n$ | Paris exponent | dimensionless |
| $K_0$ | reference stress intensity factor | $\text{N}/\text{m}^{3/2}$ |
| $\Delta K$ | stress intensity factor range in a cycle | $\text{N}/\text{m}^{3/2}$ |
| $\Delta\sigma$ | stress range in a cycle, $\sigma_{\max} - \sigma_{\min}$ for $R \ge 0$ | Pa |
| $Y$ | geometry factor | dimensionless |

Holds when: the crack grows in region II of the growth-rate curve (a straight line on log-log axes), the stress ratio, temperature, environment, and frequency match those of the test, the crack is long compared with the grain size and the plastic zone, and loading is constant amplitude.
Breaks when: $\Delta K$ is near the threshold (growth is slower than the line), $K_{\max}$ nears $K_c$ (growth accelerates beyond the Paris line), a high tensile overload retards growth, or the load history changes the stress ratio.
Source and basis: Paris' correlation of crack growth rate with the stress intensity range [src](../data/claims/fracture-fatigue.md#fatigue-paris-law).

Regimes. On the log-log plot the growth rate has three regions. In region I the rate falls steeply as $\Delta K$ falls to a **threshold** $\Delta K_{th}$, below which cracks ideally do not grow. A common test definition of the threshold is the $\Delta K$ at a growth rate of about $10^{-10}$ m per cycle. In region II the Paris line holds, and the exponent $n$ is usually between 2 and 4 for metals. In region III of the Paris curve, the rate rises sharply as $K_{\max}$ approaches the toughness [src](../data/claims/fracture-fatigue.md#fatigue-paris-law).

Paris stress-ratio data show that for $R = \sigma_{\min}/\sigma_{\max}$ below zero, the compressive part of the cycle may or may not be counted in $\Delta K$, and a factor-of-two difference follows. For a Paris curve, use the definition that matches how the $da/dN$ data were measured, commonly the positive part only, $\Delta K = K_{\max}$ when $K_{\min} \le 0$ [src](../data/claims/fracture-fatigue.md#fatigue-paris-law).

Do not design the Paris crack-growth model to $\Delta K$ below the threshold as if infinite life were proven. The Paris threshold is hard to measure, and the source treats such designs with skepticism, the same way as an assumed endurance limit [src](../data/claims/fracture-fatigue.md#fatigue-paris-law).

Example. For $a = 1$ mm, $\Delta\sigma = 100$ MPa, $Y = 1$, $n = 3$, and $C = 0.00000000001$ m per cycle, find the Paris growth rate using $K_0 = 1\ \text{MPa}\,\text{m}^{1/2}$.

```verify
a = q(1, "mm")
ds = q(100, "MPa")
k0 = q(1, "MPa") * sqrt(q(1, "m"))
c = q(0.00000000001, "m")
expect(c * (ds * sqrt(pi * a) / k0)**3, "1.76e-9 m")
```

The Paris growth rate is $1.76 \times 10^{-9}$ m per cycle.

## Paris-law integration to cycles

The **cycles to grow a crack** from an initial length $a_i$ to a final length $a_f$ follow from integrating the Paris law. With a constant geometry factor $Y$ and constant stress range $\Delta\sigma$,

$$N = \frac{a_f^{\,1 - n/2} - a_i^{\,1 - n/2}}{\left(1 - \dfrac{n}{2}\right) C\,\left(Y\,\Delta\sigma\sqrt{\pi}/K_0\right)^{n}} \quad (n \ne 2), \qquad N = \frac{\ln(a_f/a_i)}{C\,\pi\,(Y\,\Delta\sigma/K_0)^{2}} \quad (n = 2)$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $N$ | cycles to grow the crack from $a_i$ to $a_f$ | dimensionless |
| $a_i$ | initial crack length | m |
| $a_f$ | final crack length | m |
| $C$ | Paris coefficient for $K_0 = 1\ \text{MPa}\,\text{m}^{1/2}$ | m |
| $K_0$ | reference stress intensity factor | $\text{N}/\text{m}^{3/2}$ |
| $n$ | Paris exponent | dimensionless |
| $Y$ | geometry factor, held constant | dimensionless |
| $\Delta\sigma$ | stress range, held constant | Pa |

Holds when: $Y$ is nearly constant over the growth (a crack small against the width), the load is constant amplitude with $R \ge 0$, and the crack stays in region II.
Breaks when: $Y$ changes by more than a few percent between $a_i$ and $a_f$ (integrate in steps with $Y$ updated at each step, or numerically), the load spectrum varies (sum over blocks with $\Delta K_j$ for each), or $a_f$ approaches the critical size (final fracture adds almost no further cycles, but the final size itself must be the critical size at maximum stress).
Source and basis: derived from integrating the Paris law [src](../data/claims/fracture-fatigue.md#fatigue-paris-law); the integral and the stepwise treatment for a load spectrum are given in the NASA primer [src](../data/claims/fracture-fatigue.md#fatigue-paris-law).

Set $a_f$ no larger than the critical size $a_c$ at the maximum stress, from the fracture-toughness entry. In the Paris model with $n > 2$, life is dominated by the small crack lengths because the exponent $1 - n/2$ is negative. When the initial flaw dominates the integral, halving its length increases life by about $2^{n/2 - 1}$; for $n = 3$, this is about 1.41. Limiting the initial flaw size through inspection or processing therefore pays more than raising the final size in the Paris model [src](../data/claims/fracture-fatigue.md#fatigue-paris-law).

Example. A wide plate has $n = 3$, $C = 0.00000000001$ m per cycle for $K_0 = 1$ $\text{MPa}\sqrt{\text{m}}$, $\Delta\sigma = 100$ MPa, $R = 0$, and $Y = 1$. Find the cycles from $a_i = 1$ mm to $a_f = 10$ mm, then compare the final size with $K_{Ic} = 38$ $\text{MPa}\sqrt{\text{m}}$.

```verify
n = 3
C = q(0.00000000001, "m")
ds = q(100, "MPa")
K0 = q(1, "MPa") * sqrt(q(1, "m"))
ai = q(1, "mm")
af = q(10, "mm")
k = C * (ds * sqrt(pi) / K0)**n
N = (af**(1 - n / 2) - ai**(1 - n / 2)) / ((1 - n / 2) * k)
expect(N, "776634")
Kic = q(38, "MPa") * sqrt(q(1, "m"))
ac = (1 / pi) * (Kic / ds)**2
expect(ac, "46.0 mm")
check(af < ac, "final size is below the critical size at the maximum stress")
```

Growth from 1 mm to 10 mm takes 776634 cycles, and the critical size at this stress is 46.0 mm.

## Stress-life

**Stress-life** (the S-N approach) predicts cycles to failure from the stress amplitude of a cycle, for lives long enough that the part stays mostly elastic. In the high-cycle range the stress amplitude against reversals to failure $2N_f$ is nearly a straight line on log-log axes (**Basquin's relation**),

$$\sigma_a = \sigma_f'\,(2N_f)^{b}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\sigma_a$ | stress amplitude, half the stress range of a fully reversed cycle | Pa |
| $\sigma_f'$ | fatigue strength coefficient | Pa |
| $b$ | fatigue strength exponent, negative, between about 0 and -0.1 for many metals | dimensionless |
| $N_f$ | cycles to failure | dimensionless |

Holds when: the cycle is fully reversed (zero mean stress), the stress amplitude stays below the cyclic yield strength, and the life is above about $10^{4}$ cycles.
Breaks when: there is a mean stress (use the mean-stress entries), strains are plastic (use strain-life), the part is notched (use $K_f$), or the metal has an endurance limit and the stress is below it (the line then does not describe life).
Source and basis: Basquin's power law for the stress-life line [src](../data/claims/fracture-fatigue.md#fatigue-basquin).

Because $b$ is near -0.1, life varies roughly as the inverse tenth power of stress amplitude [src](../data/claims/fracture-fatigue.md#fatigue-basquin).

**Endurance limit.** Many ferritic and martensitic steels show an **endurance limit** $S_e$, a stress amplitude below which the life appears unlimited. Most non-ferrous alloys, such as aluminium, show none, and a pseudo-endurance limit at a stated long life ($5 \times 10^{6}$ cycles in the source) is used instead [src](../data/claims/fracture-fatigue.md#fatigue-endurance-limit). For wrought steels the endurance limit of a polished specimen is empirically

$$S_e \approx 0.5\,S_u \ \text{ for } S_u \le 1400\ \text{MPa}, \qquad S_e \approx 700\ \text{MPa for } S_u > 1400\ \text{MPa}$$

where $S_u$ is the tensile strength used in the endurance limit correlation [src](../data/claims/fracture-fatigue.md#fatigue-endurance-limit).

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $S_e$ | endurance limit of a polished specimen | Pa |
| $S_u$ | ultimate tensile strength | Pa |

Holds when: the steel is wrought (not cast), and the specimen is small, polished, and tested in air at room temperature.
Breaks when: the steel is cast, the part is large or rough, the environment is corrosive, or the strength is above 1400 MPa. The relation is for the specimen, not the part.
Source and basis: empirical endurance-limit correlation recorded in the MIT 2.002 notes [src](../data/claims/fracture-fatigue.md#fatigue-endurance-limit).

The part endurance limit is lower than the specimen value. The factors that lower it are surface finish, size, load type, temperature, reliability, and corrosion; they are treated in [Mechanical design reference](../design/reference.md#fatigue) and in the machine-element fatigue design of shafts and bolts, which is not repeated here. A design stress amplitude often applies a safety factor of about 2 to the amplitude read from the S-N curve at the required life [src](../data/claims/fracture-fatigue.md#fatigue-basquin).

Example. A steel has $\sigma_f' = 900$ MPa and $b = -0.09$ (illustrative). The stress amplitude is 300 MPa, fully reversed.

```verify
sf = q(900, "MPa")
sa = q(300, "MPa")
b = q(-0.09, "1")
twoN = (sa / sf)**(1 / b)
expect(twoN / 2, "100073")
Su = q(1000, "MPa")
expect(0.5 * Su, "500 MPa")
```

The predicted life is 100,073 cycles, and the specimen endurance limit is 500 MPa.

The predicted life is 100073 cycles (median, before a scatter factor), and a wrought steel of 1000 MPa tensile strength has a specimen endurance limit of about 500 MPa.

## Strain-life

**Strain-life** predicts cycles to crack initiation from the total strain amplitude, and it covers both low-cycle fatigue, where plastic strain dominates, and high-cycle fatigue, where elastic strain dominates. The total strain amplitude is the sum of an elastic part (Basquin) and a plastic part (the **Coffin-Manson relation**),

$$\varepsilon_a = \frac{\sigma_f'}{E}\,(2N_f)^{b} + \varepsilon_f'\,(2N_f)^{c}$$

The two parts are equal at the transition life $2N_t$,

$$2N_t = \left(\frac{\varepsilon_f'\,E}{\sigma_f'}\right)^{1/(b - c)}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\varepsilon_a$ | total strain amplitude | dimensionless |
| $\sigma_f'$ | fatigue strength coefficient | Pa |
| $E$ | Young's modulus | Pa |
| $b$ | fatigue strength exponent | dimensionless |
| $\varepsilon_f'$ | fatigue ductility coefficient | dimensionless |
| $c$ | fatigue ductility exponent, between about -0.5 and -0.7, with -0.6 typical | dimensionless |
| $N_f$ | cycles to failure | dimensionless |
| $N_t$ | cycles at the transition | dimensionless |

Holds when: the loading is fully reversed and strain-controlled, the material has stable cyclic properties, and there is no crack to begin with.
Breaks when: the mean stress is large (use the correction below), cyclic hardening or softening is still changing the properties, the life is dominated by crack growth (use the Paris law), or the temperature is high enough for creep.
Source and basis: Coffin and Manson's power law for plastic strain, combined with Basquin's relation [src](../data/claims/fracture-fatigue.md#fatigue-strain-life).

Below the transition life, ductility controls fatigue life. Above it, strength controls. Raising strength by alloying or heat treatment lowers $\varepsilon_f'$, so it helps high-cycle life and hurts low-cycle strain-life performance [src](../data/claims/fracture-fatigue.md#fatigue-strain-life).

Example. $E = 200$ GPa, $\sigma_f' = 1000$ MPa, $b = -0.09$, $\varepsilon_f' = 0.5$, $c = -0.6$ (illustrative). Find the transition life, then the strain amplitude at one hundred thousand reversals.

```verify
E = q(200, "GPa")
sf = q(1000, "MPa")
b = q(-0.09, "1")
ef = q(0.5, "1")
c = q(-0.6, "1")
tw = (ef * E / sf)**(1 / (b - c))
expect(tw, "8348")
tr = q(100000, "1")
e_el = (sf / E) * tr**b
e_pl = ef * tr**c
expect(e_el, "0.001774")
expect(e_pl, "0.0005000")
expect(e_el + e_pl, "0.002274")
```

At 100,000 reversals, the elastic and plastic strain amplitudes are 0.001774 and 0.0005000, for a total of 0.002274. The elastic part is larger, as expected above the transition life of about 8348 reversals.

## Mean-stress corrections

A **mean stress** $\sigma_m = (\sigma_{\max} + \sigma_{\min})/2$ shifts the cycle, and a tensile mean lowers the allowable stress amplitude. Basquin's relation gives the fully reversed case only, so a mean-stress correction converts a cycle with a mean stress into an equivalent fully reversed amplitude.

Goodman's line joins the endurance limit $S_e$ on the amplitude axis to the tensile strength $S_u$ on the mean-stress axis. A point on or below the line survives, and the factor of safety $n_s$ on both stress components is

$$\frac{1}{n_s} = \frac{\sigma_a}{S_e} + \frac{\sigma_m}{S_u}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $n_s$ | factor of safety against fatigue failure, loading line scaled to the Goodman line | dimensionless |
| $\sigma_a$ | stress amplitude, $(\sigma_{\max} - \sigma_{\min})/2$ | Pa |
| $\sigma_m$ | mean stress | Pa |
| $S_e$ | endurance limit of the part | Pa |
| $S_u$ | ultimate tensile strength | Pa |

Holds when: the mean stress is tensile, the material is a ductile metal with an endurance limit, and the life is long (mean stress matters most at long life, where plastic strain is small).
Breaks when: the mean stress is compressive (the line is then conservative if the benefit is ignored, so set $\sigma_m$ to zero), the material is brittle, the peak stress approaches yield (also check $\sigma_a + \sigma_m < S_y$), or the life is short, where mean stress relaxes.
Source and basis: Goodman's straight-line diagram of alternating stress against mean stress [src](../data/claims/fracture-fatigue.md#fatigue-goodman).

For a fatigue life at a finite number of cycles, a strain-life correction subtracts a tensile mean stress from the fatigue strength coefficient, so that the Basquin term becomes

$$\varepsilon_a = \frac{\sigma_f' - \sigma_m}{E}\,(2N_f)^{b} + \varepsilon_f'\,(2N_f)^{c}$$

with the same variables as the strain-life entry plus $\sigma_m$ (Pa). For compressive mean stress $\sigma_m$ the conservative choice is to ignore the benefit and use the zero-mean form [src](../data/claims/fracture-fatigue.md#fatigue-strain-life-mean-stress).

The Soderberg and Gerber lines and the Smith-Watson-Topper parameter are other mean-stress corrections. Soderberg and Gerber are tabulated in [Mechanical design reference](../design/reference.md#fatigue). They are not repeated here because no registered source states them.

Example. $S_u = 600$ MPa, $S_e = 250$ MPa, $\sigma_a = 100$ MPa, $\sigma_m = 150$ MPa.

```verify
Su = q(600, "MPa")
Se = q(250, "MPa")
sa = q(100, "MPa")
sm = q(150, "MPa")
inv = sa / Se + sm / Su
expect(inv, "0.650")
ns = 1 / inv
expect(ns, "1.54")
```

The Goodman damage ratio is 0.650, giving a fatigue safety factor of 1.54.

## Notch sensitivity and fatigue stress concentration

A **notch** is any hole, fillet, groove, or scratch that concentrates stress. The elastic **stress concentration factor** $K_t$ is the ratio of peak local stress to nominal stress. The **fatigue notch factor** $K_f$ is the ratio of the unnotched to the notched fatigue strength at the same long life, and satisfies $1 \le K_f \le K_t$. For wrought steels, Peterson fitted

$$K_f = 1 + \frac{K_t - 1}{1 + \alpha/\rho}, \qquad \alpha = \alpha_0 \left(\frac{\sigma_{ref}}{S_u}\right)^{1.8}$$

with $\alpha_0 = 25.4\ \mu\text{m}$ (0.001 in) and $\sigma_{ref} = 2070$ MPa (300 ksi) for wrought steels. The **notch sensitivity** is $q = (K_f - 1)/(K_t - 1) = 1/(1 + \alpha/\rho)$.

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $K_f$ | fatigue notch factor | dimensionless |
| $K_t$ | elastic stress concentration factor | dimensionless |
| $q$ | notch sensitivity | dimensionless |
| $\rho$ | notch root radius | m |
| $\alpha$ | material length scale, smaller for stronger steel | m |
| $\alpha_0$ | reference length of the fit | m |
| $\sigma_{ref}$ | reference strength of the fit | Pa |
| $S_u$ | ultimate tensile strength | Pa |

Holds when: the material is a wrought steel, the loading is high-cycle with local response elastic, and $K_t$ comes from a handbook chart or finite element analysis of the same notch.
Breaks when: the material is not wrought steel (the constants are for steel), the root radius is very small or very large compared with $\alpha$ (the fit is least reliable at the extremes), or the notch response is plastic (use the Neuber relation below).
Source and basis: Peterson's empirical fit to notch fatigue data for wrought steels [src](../data/claims/fracture-fatigue.md#fatigue-kf-peterson). The charts of $K_t$ are named, not reproduced: Peterson's *Stress Concentration Factors* is the standard handbook.

For $\rho \gg \alpha$, $K_f \to K_t$ (a blunt notch in strong steel acts at full strength). For $\rho \ll \alpha$, $K_f \to 1$ (a small notch in a weak steel hardly matters). The high-cycle notched amplitude then uses the nominal stress with $K_f$: $K_f\,S_a = \sigma_f'(2N_f)^{b}$. For local plasticity, Neuber's rule links the local stress and strain concentrations to the elastic one,

$$K_\sigma K_\varepsilon = K_f^{2}$$

where $K_\sigma$ and $K_\varepsilon$ are the cyclic stress and strain concentration factors, both dimensionless. Neuber's rule is most appropriate for thin plane-stress sheets with a root radius comparable to thickness, and it is conservative for more triaxial notches [src](../data/claims/fracture-fatigue.md#fatigue-neuber).

Example. $K_t = 2.5$, root radius $\rho = 2$ mm, and a wrought steel with $S_u = 1000$ MPa.

```verify
a0 = q(25.4, "um")
sref = q(2070, "MPa")
Su = q(1000, "MPa")
al = a0 * (sref / Su)**1.8
expect(al, "0.0941 mm")
rho = q(2, "mm")
Kt = q(2.5, "1")
qn = 1 / (1 + al / rho)
expect(qn, "0.955")
Kf = 1 + (Kt - 1) * qn
expect(Kf, "2.43")
```

The notch behaves almost at full theoretical strength ($K_f = 2.43$ against $K_t = 2.5$) because the radius is large compared with $\alpha$. The fitted length scale is 0.0941 mm, and notch sensitivity is 0.955.

## Cumulative damage

**Cumulative damage** is the accounting of fatigue life used up when the stress amplitude changes during service. The Palmgren-Miner rule assigns each block of $n_i$ cycles at one amplitude the fraction $n_i/N_i$ of the life $N_i$ at that amplitude, and predicts failure when the fractions sum to one,

$$D = \sum_i \frac{n_i}{N_i}, \qquad \text{failure predicted at } D = 1$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $D$ | damage sum | dimensionless |
| $n_i$ | cycles applied at amplitude $i$ | dimensionless |
| $N_i$ | cycles to failure at constant amplitude $i$ | dimensionless |

Holds when: damage accumulates at a constant rate within each block, the order of the blocks does not matter, and the amplitudes are of similar kind (all high-cycle, or all low-cycle).
Breaks when: loads of high and low amplitude are mixed in a certain order (a high block first and a low block after differs from the reverse), the damage rate rises late in life as cracks form, or overloads create residual stresses that change later damage. Treat $D = 1$ as a median estimate with scatter, not a threshold of certainty.
Source and basis: the linear damage rule introduced by Palmgren and Miner [src](../data/claims/fracture-fatigue.md#fatigue-miner).

The rule ignores sequence effects, and the source warns that real accumulation is a mixture of mechanisms and the linear assumption should be viewed skeptically. Design to a damage sum below one, and apply a scatter factor to the life [src](../data/claims/fracture-fatigue.md#fatigue-miner).

Example. A part sees three blocks per year: $2 \times 10^{4}$ cycles at an amplitude with life $1 \times 10^{5}$, $5 \times 10^{4}$ cycles at an amplitude with life $4 \times 10^{5}$, and 1000 cycles at an amplitude with life 5000.

```verify
D1 = 20000 / 100000
D2 = 50000 / 400000
D3 = q(1000, "1") / q(5000, "1")
D = D1 + D2 + D3
expect(D, "0.525")
yrs = 1 / D
expect(yrs, "1.90")
```

Each block set uses 0.525 of the life, so the part reaches $D = 1$ after about 1.9 repetitions (median, before the scatter factor).

## Damage-tolerance limits and inspection intervals

**Damage tolerance** is the design approach that assumes a flaw of the largest size inspection could miss, and shows that it cannot grow to the critical size before the next inspection. The no-growth size and the inspection interval follow from the entries above.

The **no-growth size** is the largest crack whose stress intensity range stays at or below the threshold, so a wide-plate crack of that size or smaller does not grow,

$$a_{th} = \frac{1}{\pi}\left(\frac{\Delta K_{th}}{Y\,\Delta\sigma}\right)^{2}$$

The **inspection interval** in cycles is the cycles to grow the assumed flaw from the detectable size $a_d$ to the critical size $a_c$, divided by a scatter factor $f_s$,

$$N_{insp} = \frac{N(a_d \to a_c)}{f_s}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $a_{th}$ | no-growth crack size | m |
| $\Delta K_{th}$ | threshold stress intensity range | $\text{N}/\text{m}^{3/2}$ |
| $Y$ | geometry factor | dimensionless |
| $\Delta\sigma$ | stress range | Pa |
| $N_{insp}$ | inspection interval | dimensionless |
| $N(a_d \to a_c)$ | cycles from detectable to critical size, from the integration entry | dimensionless |
| $a_d$ | smallest crack the inspection method finds reliably | m |
| $a_c$ | critical crack size at the maximum stress | m |
| $f_s$ | scatter factor on life | dimensionless |

Holds when: the inspection method detects $a_d$ with high reliability, the crack growth data match the service conditions, and the inspection occurs at the interval set.
Breaks when: the detection probability is low (then use the larger size at which it is high), the cracks are hidden or cannot be inspected (then a safe-life limit is needed instead), the growth is retarded or accelerated by the load spectrum, or the threshold is not well measured. Designing to $\Delta K < \Delta K_{th}$ in the Paris model rests on a quantity that is hard to measure, so the source calls such designs questionable [src](../data/claims/fracture-fatigue.md#fatigue-paris-law).
Source and basis: derived from the threshold and Paris-integration entries; the primer's worked proof-test example takes a scatter factor of 4 on the required life [src](../data/claims/fracture-fatigue.md#fracture-damage-tolerance-scatter).

The scatter factor is a design choice. The value 4 comes from that example and is not a universal requirement; the governing specification sets it.

Example. A wide plate has $\Delta K_{th} = 3$ $\text{MPa}\sqrt{\text{m}}$, $\Delta\sigma = 150$ MPa, and $Y = 1$. At $R = 0$, take $K_{Ic} = 38$ $\text{MPa}\sqrt{\text{m}}$, an initial flaw $a_d = 1$ mm, $n = 3$, $C = 0.00000000001$ m per cycle for $K_0 = 1$ $\text{MPa}\sqrt{\text{m}}$, and scatter factor $f_s = 4$.

```verify
rtm = sqrt(q(1, "m"))
dKth = q(3, "MPa") * rtm
ds = q(150, "MPa")
ath = (1 / pi) * (dKth / ds)**2
expect(ath, "0.127 mm")
n = 3
C = q(0.00000000001, "m")
K0 = q(1, "MPa") * rtm
Kic = q(38, "MPa") * rtm
ad = q(1, "mm")
ac = (Kic / ds)**2 / pi
expect(ac, "20.4 mm")
k = C * (ds * sqrt(pi) / K0)**n
N = (ac**(1 - n / 2) - ad**(1 - n / 2)) / ((1 - n / 2) * k)
expect(N, "262077")
fs = q(4, "1")
expect(N / fs, "65519")
```

The predicted crack-growth life is 262077 cycles. Cracks smaller than 0.127 mm would not grow at this stress range, and inspection every 65519 cycles keeps a crack just missed at 1 mm from reaching its calculated critical size of 20.4 mm.

## Checklists

Before trusting a fracture check:

- Is there a stated flaw size, the largest that inspection could miss, and where is it placed (surface, corner, embedded, at a hole or weld)?
- Is $Y$ the factor for that geometry and size, with the validity range respected?
- Is the toughness $K_{Ic}$ measured at the service temperature, environment, and thickness, and does the section meet the size requirement?
- Is the stress the maximum in service, including residual and thermal stress, with the net section below yield?
- Is the plastic zone small against the crack and the ligament?
- Is the sensitivity checked: how does $a_c$ change if the stress rises 10 percent?

Before trusting a fatigue life:

- Are the constants ($C$, $n$, $b$, $\sigma_f'$, $c$, $\varepsilon_f'$) from the same material, condition, temperature, environment, and stress ratio?
- Is the stress the local stress at the notch ($K_f$ applied), not the nominal one?
- Is a mean stress present, and has a correction been applied?
- Is the damage sum below one, and is a scatter factor applied to the median life?
- Is the load spectrum known, including overloads, start-up and shutdown cycles, and vibration?
- Is the initial flaw size justified by the inspection method, and are all critical locations on the inspection plan?

## Sanity checks

- $K$ in MPa times the square root of metre for a flaw of a few millimetres at a few hundred MPa is of order 10 to 30; for a toughness near 40, a flaw of about 10 mm is critical at 200 MPa. A result in the thousands means mm were used where m were needed.
- Doubling the stress cuts the critical size by a factor of four; doubling the toughness raises it by a factor of four.
- The plane-strain plastic zone is a third of the plane-stress one. A zone larger than a few percent of the crack length breaks the linear elastic model.
- A tensile mean stress always shortens life against zero mean. A result that lengthens life with a tensile mean has the sign wrong.
- Paris life with $n = 3$ falls by a factor of $2^{3} = 8$ if the stress range doubles. A change of 5 percent in $\Delta\sigma$ changes life by about 14 percent.
- $K_f$ lies between 1 and $K_t$. A value above $K_t$ is an error.
- A Miner sum above one means the life is used up. A sum far below one for a part that has cracked means scatter, overloads, or a notch were not captured.

Conversions. 1 ksi times the square root of inch equals 1.099 $\text{MPa}\sqrt{\text{m}}$, and 1 ksi equals 6.895 MPa.

```verify
rtm = sqrt(q(1, "m"))
kk = q(1, "ksi") * sqrt(q(1, "in"))
expect(kk / rtm, "1.099 MPa")
expect(q(1, "ksi"), "6.895 MPa")
```

Reported values from the primer (one source, for orientation only; use certified data for design). They are not material allowables.

| Item | Yield strength (MPa) | Fracture toughness ($\text{Pa}\,\text{m}^{1/2}$) | Note |
|---|---|---|---|
| 2219-T87 aluminium alloy, room temperature | 455 | $38.5 \times 10^{6}$ | 66 ksi and 35 ksi times the square root of inch in the source |
| One 4340 steel condition, 24 C | not given | $55 \times 10^{6}$ | about 50 ksi times the square root of inch |
| The same 4340 steel, -73 C | not given | $33 \times 10^{6}$ | about 30 ksi times the square root of inch |

The toughness of a metal varies with heat treatment, product form, direction, and temperature, by tens of percent. Do not take a toughness from a table without its test conditions [src](../data/claims/fracture-fatigue.md#fracture-toughness-size-rule).

## Further reference

- Anderson, Fracture Mechanics: Fundamentals and Applications (crack-tip fields, elastic-plastic fracture, and fatigue crack growth; paid, by title only).
- Tada, Paris, and Irwin, The Stress Analysis of Cracks Handbook (geometry factors; paid, by title only).
- Suresh, Fatigue of Materials (stress-life, strain-life, and crack growth; paid, by title only).
- Bannantine, Comer, and Handrock, Fundamentals of Metal Fatigue Analysis (stress-life, strain-life, and notches; paid, by title only).
- Peterson, Stress Concentration Factors (charts of $K_t$; paid, by title only).
- The ASTM standard test method for plane-strain fracture toughness of metallic materials, and the ASTM standard test method for measurement of fatigue crack growth rates (named by title only).
- [Linear Elastic Fracture Mechanics Primer](https://ntrs.nasa.gov/citations/19920021173), NASA Technical Reports Server: the crack-tip field, geometry factors, toughness testing, Paris law, and worked inspection problems.
- [Defect-free fatigue notes](https://ocw.mit.edu/courses/2-002-mechanics-and-materials-ii-spring-2004/), MIT OpenCourseWare 2.002: stress-life, strain-life, mean stress, cumulative damage, and notch effects.
- [Fatigue notes by Roylance](https://ocw.mit.edu/courses/3-11-mechanics-of-materials-fall-1999/), MIT OpenCourseWare 3.11: the S-N curve, the Goodman diagram, Miner's rule, and the Paris law.
- Related sheets: [Materials reference](reference.md) for material properties, and [Mechanical design reference](../design/reference.md) for shaft and bolt fatigue design.
