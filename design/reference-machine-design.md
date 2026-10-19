# Machine design reference

**Type:** reference
**Verify:** strict

Lookup sheet for sizing and checking the standard machine elements (bolts, welds, power screws, shafts, keys, springs, bearings, gears, belts, chains, clutches, and press fits), for an engineer who needs a formula, a limit, or a sanity check in the middle of a design.

## Principles

- A machine element carries load along a path from the point of application to the ground. Find the path, then size each element on it for the load it carries, not the load the whole machine sees.
- The weakest element on the path sets the strength of the machine. Equal strength everywhere is not the goal, but no element should fail first by accident.
- Compare a calculated stress with the strength that matches the failure mode: yield for steady ductile loads, endurance strength for repeated loads, contact strength for rolling and meshing surfaces, wear limits for sliding surfaces.
- Geometry that changes abruptly (keyways, shoulders, thread roots, weld toes) concentrates stress. A nominal-stress formula that ignores it needs a fatigue factor or a margin.
- A preload turns a joint into a pair of springs. The clamped parts, not the bolt, carry most of an external load while the joint stays closed.
- Friction sets what torque a joint, clutch, belt, or press fit can carry, and friction coefficients scatter widely. State the coefficient and design for its range.
- Life of a rolling bearing falls with a power of the load. A small load error becomes a large life error.
- Use the tabulated rating of a bought part (bearing, chain, belt) only at the conditions the maker states.
- A formula in this sheet is the first estimate. Standards and codes add factors for load type, reliability, and temperature, and they govern a real design.
- Write the unit of every input. Convert once, to N, mm, and MPa or to N, m, and Pa, and hold that set for the whole calculation.

## Load paths and design factors

### Design factor

The design factor $n_s$ is the ratio of the strength that governs the failure mode to the calculated stress at the critical point.

$$n_s = \frac{S}{\sigma_{\text{max}}}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $n_s$ | design factor (factor of safety) | dimensionless |
| $S$ | governing strength: yield $S_y$, endurance $S_e$, or another strength matched to the failure mode | Pa |
| $\sigma_{\text{max}}$ | calculated stress at the critical point, including concentration | Pa |

Holds when: the stress is computed in the same state (static or cycling) as the strength, and the loads are known to a stated accuracy.
Breaks when: the load is uncertain by more than the factor (the factor then hides ignorance), the failure is buckling, creep, or fracture (compare loads or intensities, not stresses), or stresses and strengths are scattered widely (use a reliability method).
Source and basis: derived from the definition of margin; taught in [Factor of safety and failure](07-factor-of-safety-and-failure.md).

Example: a part with yield strength 350 MPa and a peak stress of 140 MPa has $n_s = 2.5$.

```verify
Sy = q(350, "MPa")
s = q(140, "MPa")
expect(Sy / s, "2.5")
```

- Stress formulas for axial, bending, and torsion loads are in [Mechanics reference](../physics/reference-mechanics.md#stress-and-strain).
- Fatigue strength, mean-stress corrections, and $K_f$ belong to [materials/reference-fracture-fatigue.md](../materials/reference-fracture-fatigue.md).
- Fit classes and tolerances are in [Design reference](reference.md#tolerancing-and-stack-up).

## Bolted joints

### Thread tensile stress area

The tensile stress area $A_t$ is the area of an unthreaded rod that carries the same tensile load as the threaded bolt, so it is the area to use in bolt stress and preload.

$$A_t = \frac{\pi}{4}\left(d - \frac{13}{12}H\right)^{2}, \qquad H = \frac{\sqrt{3}}{2}\,p$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $A_t$ | tensile stress area | $\text{m}^2$ |
| $d$ | nominal (major) diameter of the thread | m |
| $p$ | thread pitch | m |
| $H$ | height of the sharp-V thread triangle | m |

Holds when: the thread is a 60 degree metric thread of the basic profile, so the effective diameter is the mean of the pitch diameter $d - \tfrac{3}{4}H$ and the minor diameter $d - \tfrac{17}{12}H$.
Breaks when: the thread form differs (Acme, buttress, rolled threads with a different root), or the thread is damaged or undersize.
Source and basis: derived from the basic thread profile geometry, in which the sum of the two diameters halved gives $d - \tfrac{13}{12}H$, so $A_t \approx \tfrac{\pi}{4}(d - 0.9382\,p)^2$. For standard sizes use the table value.

Example: an M10 coarse thread has $d = 10$ mm and $p = 1.5$ mm, so the factor on the pitch is $0.9382$ and $A_t = 58.0\ \text{mm}^2$.

```verify
d = q(10, "mm")
p = q(1.5, "mm")
expect(q(13, "") / 12 * sqrt(3) / 2, "0.9382")
At = pi / 4 * (d - 13 / 12 * sqrt(3) / 2 * p)**2
expect(At, "58.0 mm^2")
```

### Preload and tightening torque

Preload $F_i$ is the tension a bolt carries before any external load, set by stretching the bolt until the clamped parts are squeezed together.

$$F_i = \phi\, S_p\, A_t, \qquad T = K\, F_i\, d$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $F_i$ | bolt preload | N |
| $\phi$ | preload fraction of the proof load | dimensionless |
| $S_p$ | proof strength of the bolt, from its specification | Pa |
| $A_t$ | tensile stress area | $\text{m}^2$ |
| $T$ | tightening torque | N m |
| $K$ | nut factor (torque coefficient) | dimensionless |
| $d$ | nominal bolt diameter | m |

Holds when: the bolt stays elastic, the nut factor matches the actual surfaces and lubricant, and the clamped parts do not relax. Typical fastener practice uses $\phi$ from 0.7 to 0.9, chosen for the joint and its service conditions; this is not a universal limit.
Breaks when: friction differs from the assumed $K$ (the preload scatters widely with torque control alone), the joint embeds or relaxes, or the thread galls. Use bolt stretch or turn-of-nut methods where preload must be accurate.
Source and basis: $F_i$ is a design rule of thumb on the proof load; $T = K F_i d$ lumps thread and collar friction into $K$, which is a measured value. Typical fastener practice uses $K$ from about 0.15 to 0.25 for steel fasteners, with the value depending on surface and lubricant. These are practice ranges, not universal limits. Taught in [Gears, fasteners, and springs](09-gears-fasteners-and-springs.md).

Example: a bolt of proof strength 580 MPa with $A_t = 58.0\ \text{mm}^2$, $d = 10$ mm, $K = 0.20$ gives $F_i = 25.2$ kN and $T = 50.5\ \text{N m}$. With lubricated threads of $K = 0.15$, the same torque gives $33.6$ kN, the proof load; tightening torsion can bring the bolt to yield.

```verify
Sp = q(580, "MPa")
At = q(58.0, "mm^2")
d = q(10, "mm")
K = q(0.20, "")
Fi = 0.75 * Sp * At
expect(Fi, "25.2 kN")
T = K * Fi * d
expect(T, "50.5 N m")
K2 = q(0.15, "")
F2 = T / (K2 * d)
expect(F2, "33.6 kN")
expect(Sp * At, "33.6 kN")
```

### Joint stiffness and load sharing

The joint constant $C$ is the fraction of an external tensile load that goes into the bolt while the clamped members stay in contact.

$$C = \frac{k_b}{k_b + k_m}, \qquad F_b = F_i + C\,P, \qquad F_m = F_i - (1 - C)\,P, \qquad P_0 = \frac{F_i}{1 - C}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $C$ | joint constant | dimensionless |
| $k_b$ | bolt stiffness, $A E / L$ summed in series over its segments | N/m |
| $k_m$ | stiffness of the clamped members | N/m |
| $F_b$ | bolt force under external load | N |
| $F_m$ | clamping force left on the members | N |
| $F_i$ | preload | N |
| $P$ | external tensile load per bolt | N |
| $P_0$ | external load at which the members separate | N |

Holds when: the external load acts at the bolt axis, the members stay in contact ($F_m > 0$), and everything is elastic. The member stiffness $k_m$ comes from a frustum (cone) model; see [Bolted and welded joints](12-bolted-and-welded-joints.md).
Breaks when: the joint opens ($P > P_0$, then the bolt carries all of $P$), the plates bend or pry, or the load acts off the bolt axis.
Source and basis: derived from the compatibility of two springs that share one deflection, taught in [Bolted and welded joints](12-bolted-and-welded-joints.md).

Example: an M10 bolt with $A_t = 58.0\ \text{mm}^2$, $E = 200$ GPa, and grip 20 mm has $k_b = 580$ kN/mm. The two half-grip frustums for 10 mm steel plates each have stiffness 4440 kN/mm, so their series stiffness is $k_m = 2220$ kN/mm. Then $C = 0.207$. With $F_i = 25.2$ kN and $P = 10$ kN, $F_b = 27.3$ kN, $F_m = 17.3$ kN, and $P_0 = 31.8$ kN.

```verify
At = q(58.0, "mm^2")
E = q(200, "GPa", of="none")
l = q(20, "mm")
d = q(10, "mm")
dw = 1.5 * d
kb = At * E / l
expect(kb, "580 kN/mm")
tn = tan(pi / 6)
t = l / 2
kf = pi * E * d * tn / log(((2 * t * tn + dw - d) * (dw + d)) / ((2 * t * tn + dw + d) * (dw - d)))
expect(kf, "4440 kN/mm")
km = kf / 2
C = kb / (kb + km)
expect(km, "2220 kN/mm")
expect(C, "0.207")
Fi = 0.75 * q(580, "MPa") * At
P = q(10, "kN")
expect(Fi, "25.2 kN")
expect(Fi + C * P, "27.3 kN")
expect(Fi - (1 - C) * P, "17.3 kN")
expect(Fi / (1 - C), "31.8 kN")
```

### Bolt stress under cycling load

When the external load cycles between zero and $P$, the bolt sees a small alternating stress on top of a large mean stress from the preload.

$$\sigma_a = \frac{C\,P}{2 A_t}, \qquad \sigma_m = \frac{F_i}{A_t} + \frac{C\,P}{2 A_t}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\sigma_a$ | alternating stress amplitude in the bolt | Pa |
| $\sigma_m$ | mean stress in the bolt | Pa |
| $C$ | joint constant | dimensionless |
| $P$ | peak external load per bolt | N |
| $A_t$ | tensile stress area | $\text{m}^2$ |
| $F_i$ | preload | N |

Holds when: the joint stays closed through the cycle and the load runs from zero to $P$.
Breaks when: the joint separates (then the bolt sees the whole of $P$), or the load is fully reversing.
Source and basis: derived from $F_b = F_i + C P$ at the peak and $F_i$ at zero load. Compare $\sigma_a$ and $\sigma_m$ with the endurance and tensile strength using the mean-stress rules in [materials/reference-fracture-fatigue.md](../materials/reference-fracture-fatigue.md).

Example: the bolt above has $\sigma_a = 17.9$ MPa and $\sigma_m = 452.9$ MPa. A fatigue crack starts at the thread root or under the head, so the strength compared with these stresses is the corrected endurance strength of the threaded bolt.

```verify
At = q(58.0, "mm^2")
C = q(0.2071463, "")
P = q(10, "kN")
Fi = q(25.23, "kN")
sa = C * P / (2 * At)
expect(sa, "17.9 MPa")
expect(Fi / At + sa, "452.9 MPa")
```

## Welded joints

### Fillet weld throat stress

A fillet weld fails on its throat, the shortest section from the root of the corner to the face of the weld, so the weld stress is the load over the throat area.

$$t_e = \frac{h}{\sqrt{2}}, \qquad \tau = \frac{F}{t_e\, L_w}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $t_e$ | throat thickness of an equal-leg fillet | m |
| $h$ | leg length of the fillet | m |
| $\tau$ | average shear stress on the throat | Pa |
| $F$ | load carried by the weld, through its centroid | N |
| $L_w$ | total weld length | m |

Holds when: the weld has two equal legs at a right angle with a flat face, the weld is sound, and the load acts through the centroid of the weld group.
Breaks when: the load is off the centroid (add the secondary shear from the moment, in [Bolted and welded joints](12-bolted-and-welded-joints.md)), the face is convex or concave, the weld has defects, or the load is cyclic (weld toes crack, so use a fatigue detail category).
Source and basis: derived from the geometry of a right isosceles triangle, where the altitude to the hypotenuse is $h/\sqrt{2}$, so $t_e \approx 0.707\,h$. Allowable stresses and filler-metal strengths come from the governing code and are not given here.

Example: fillet welds of leg 6 mm and total length 200 mm carry 20 kN through the centroid. The throat is $t_e = 4.24$ mm, the throat area is $849\ \text{mm}^2$, and $\tau = 23.6$ MPa.

```verify
h = q(6, "mm")
Lw = q(200, "mm")
F = q(20, "kN")
te = h / sqrt(2)
expect(te, "4.24 mm")
expect(te * Lw, "849 mm^2")
expect(F / (te * Lw), "23.6 MPa")
```

## Power screws

### Torque, self-locking, and efficiency

A power screw turns rotation into thrust through a thread acting as an inclined plane wound round a cylinder.

$$T_R = \frac{F d_m}{2}\,\frac{l + \pi \mu d_m}{\pi d_m - \mu l}, \qquad T_L = \frac{F d_m}{2}\,\frac{\pi \mu d_m - l}{\pi d_m + \mu l}, \qquad e = \frac{F\, l}{2\pi\, T_R}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $T_R$ | torque to raise the load (or push against it) | N m |
| $T_L$ | torque to lower the load | N m |
| $F$ | axial load on the screw | N |
| $d_m$ | mean thread diameter | m |
| $l$ | lead, the axial advance per turn | m |
| $\mu$ | thread friction coefficient | dimensionless |
| $e$ | efficiency, work out over work in | dimensionless |

Holds when: the thread is square (or the Acme angle effect is small), the load is axial, the screw turns slowly, and collar or bearing friction is added separately.
Breaks when: the thread has a large flank angle (replace $\mu$ by $\mu / \cos\alpha$ for a flank half-angle $\alpha$ measured in the axial plane), the speed is high, or a thrust collar adds friction torque.
Source and basis: derived from force balance on a block on an inclined plane of lead angle $\tan\lambda = l / (\pi d_m)$, with Coulomb friction (see [Friction](../physics/reference-mechanics.md#friction)). The screw is self-locking when $T_L > 0$, which means $\pi \mu d_m > l$, or $\mu > \tan\lambda$. Then $e < 0.5$.

Example: a single-start screw with $d_m = 20$ mm, lead 4 mm, $\mu = 0.15$ carries 5 kN. Here $\pi \mu d_m = 9.42$ mm exceeds the lead, so the screw is self-locking. $T_R = 10.8\ \text{N m}$, $T_L = 4.28\ \text{N m}$, and $e = 0.295$.

```verify
F = q(5, "kN")
dm = q(20, "mm")
l = q(4, "mm")
mu = q(0.15, "")
expect(pi * mu * dm, "9.42 mm")
TR = F * dm / 2 * (l + pi * mu * dm) / (pi * dm - mu * l)
TL = F * dm / 2 * (pi * mu * dm - l) / (pi * dm + mu * l)
expect(TR, "10.8 N m")
expect(TL, "4.28 N m")
expect(F * l / (2 * pi * TR), "0.295")
check(pi * mu * dm > l, "self-locking")
```

## Shafts

### Combined bending and torsion sizing

For a solid round shaft under steady bending moment $M$ and torque $T$, the von Mises stress at the surface sets the smallest diameter for a design factor.

$$d = \left(\frac{16\, n_s}{\pi\, S_y}\sqrt{4M^2 + 3T^2}\right)^{1/3}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $d$ | shaft diameter | m |
| $n_s$ | design factor | dimensionless |
| $S_y$ | tensile yield strength | Pa |
| $M$ | bending moment at the section | N m |
| $T$ | torque at the section | N m |

Holds when: the shaft is solid, round, ductile, and loaded steadily, with no stress concentration at the section.
Breaks when: the load cycles (size for fatigue instead, with $K_f$ at keyways, shoulders, and grooves), the shaft is hollow with a thin wall, or axial load is large.
Source and basis: derived by setting the von Mises stress $\sqrt{\sigma^2 + 3\tau^2}$, with $\sigma = 32M/(\pi d^3)$ and $\tau = 16T/(\pi d^3)$ from [Mechanics reference](../physics/reference-mechanics.md#stress-and-strain), equal to $S_y / n_s$. Taught in [Shafts and bearings](08-shafts-and-bearings.md).

Example: $M = 150\ \text{N m}$, $T = 200\ \text{N m}$, $S_y = 350$ MPa, and $n_s = 2.5$ give $d = 25.55$ mm. Use the next standard size above it.

```verify
M = q(150, "N m")
T = q(200, "N m")
Sy = q(350, "MPa")
n = q(2.5, "")
d = (16 * n / (pi * Sy) * sqrt(4 * M**2 + 3 * T**2))**(1 / 3)
expect(d, "25.55 mm")
```

### Deflection, slope, and twist

Bearings, seals, and gear meshes need small shaft deflection, slope, and twist, so a shaft that is strong enough may still be too flexible.

$$\delta = \frac{F L^3}{48 E I}, \qquad \theta_s = \frac{F L^2}{16 E I}, \qquad \phi = \frac{T L}{G J}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\delta$ | midspan deflection | m |
| $\theta_s$ | slope at each support | rad |
| $\phi$ | angle of twist | rad |
| $F$ | load at midspan | N |
| $L$ | span between supports, or length under torque | m |
| $E$ | Young's modulus | Pa |
| $G$ | shear modulus | Pa |
| $I$ | second moment of area, $\pi d^4 / 64$ for a solid round shaft | $\text{m}^4$ |
| $J$ | polar second moment of area, $\pi d^4 / 32$ for a solid round shaft | $\text{m}^4$ |
| $T$ | torque | N m |

Holds when: the shaft is uniform, simply supported with one central load (for $\delta$ and $\theta_s$), and elastic.
Breaks when: the shaft is stepped (use an equivalent diameter or integrate), the supports are not simple, or the loads are several.
Source and basis: derived from beam and torsion theory; see [Mechanics reference](../physics/reference-mechanics.md). Limits on deflection, slope, and twist depend on the bearing, seal, or gear and come from its maker or the governing standard, so none is given here. First critical speed is in [Vibrations reference](../physics/reference-vibrations.md#rotor-critical-speed).

Example: a 30 mm steel shaft of span 0.4 m carries 1 kN at midspan. With $E = 200$ GPa, $\delta = 0.168$ mm and $\theta_s = 0.00126$ rad. A 200 N m torque over 0.4 m with $G = 79$ GPa twists it $0.0127$ rad.

```verify
d = q(30, "mm")
L = q(0.4, "m")
F = q(1, "kN")
E = q(200, "GPa", of="none")
G = q(79, "GPa", of="none")
I = pi * d**4 / 64
J = pi * d**4 / 32
expect(F * L**3 / (48 * E * I), "0.168 mm")
expect(F * L**2 / (16 * E * I), "0.00126")
expect(q(200, "N m") * L / (G * J), "0.0127")
```

## Keys and splines

### Key shear and bearing stress

A key transmits torque from a shaft to a hub by shear across its length and by bearing on its side face.

$$F = \frac{2T}{d}, \qquad \tau = \frac{F}{b\, L_k}, \qquad \sigma_b = \frac{F}{(h/2)\, L_k}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $F$ | tangential force at the shaft surface | N |
| $T$ | torque | N m |
| $d$ | shaft diameter | m |
| $\tau$ | shear stress on the key's mid-plane | Pa |
| $\sigma_b$ | bearing stress on the key side | Pa |
| $b$ | key width | m |
| $h$ | key height | m |
| $L_k$ | key length | m |

Holds when: the force is spread evenly along the key, and the key is a rectangular parallel key that carries half its height in each of the shaft and hub.
Breaks when: the fit is loose (load concentrates at one end), the load cycles or reverses (stress concentration at the keyway and wear), or two keys share load (take the share at about one half, not one half exactly).
Source and basis: derived from moment balance about the shaft axis and the contact areas of the key.

Splines share load among teeth. Use the same two checks with the contact area summed over the teeth, and reduce it by a load-sharing fraction below 1 because not every tooth touches at once. A key or spline gives no axial location and is not a substitute for a press fit where that is needed.

Example: $T = 200\ \text{N m}$ on a 25 mm shaft with a key $b = 8$ mm, $h = 7$ mm, $L_k = 30$ mm gives $F = 16.0$ kN, $\tau = 66.7$ MPa, and $\sigma_b = 152$ MPa.

```verify
T = q(200, "N m")
d = q(25, "mm")
b = q(8, "mm")
h = q(7, "mm")
Lk = q(30, "mm")
F = 2 * T / d
expect(F, "16.0 kN")
expect(F / (b * Lk), "66.7 MPa")
expect(F / (h / 2 * Lk), "152 MPa")
```

## Springs

### Helical compression spring rate and stress

A helical compression spring is a coil of round wire that stores energy by twisting its wire, so its rate follows from torsion of the wire.

$$k = \frac{G\, d^4}{8\, D^3 N_a}, \qquad \tau = K_s\,\frac{8\, F\, D}{\pi\, d^3}, \qquad K_s = 1 + \frac{d}{2D}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $k$ | spring rate | N/m |
| $G$ | shear modulus of the wire | Pa |
| $d$ | wire diameter | m |
| $D$ | mean coil diameter | m |
| $N_a$ | number of active coils | dimensionless |
| $\tau$ | direct plus torsional shear stress used for static yield checks | Pa |
| $K_s$ | direct-shear factor | dimensionless |
| $F$ | axial force on the spring | N |

Holds when: the coil is helical with a small pitch angle, the wire is round, the deflection is well below solid, and the spring index $D/d$ is moderate (about 4 to 12, typical).
Breaks when: curvature raises the local stress above this direct-plus-torsional value, the spring is loaded to solid or past its elastic limit, or the load cycles without a curvature correction for fatigue.
Source and basis: derived from torsion of a straight wire of length $\pi D N_a$ (see [Axial and torsion](../physics/04-axial-and-torsion.md)); $K_s$ adds direct shear to torsional shear, but does not include curvature. A curvature correction is needed for fatigue checks at every spring index. Taught in [Gears, fasteners, and springs](09-gears-fasteners-and-springs.md).

Example: $d = 2$ mm, $D = 16$ mm, $N_a = 10$, and $G = 79$ GPa give $k = 3.86\ \text{N/mm}$. A 20 N load deflects it $5.18$ mm and gives $K_s = 1.06$ and $\tau = 108$ MPa.

```verify
G = q(79, "GPa", of="none")
d = q(2, "mm")
D = q(16, "mm")
Na = q(10, "")
k = G * d**4 / (8 * D**3 * Na)
expect(k, "3.86 N/mm")
F = q(20, "N")
expect(F / k, "5.18 mm")
Ks = 1 + d / (2 * D)
expect(Ks, "1.06")
expect(Ks * 8 * F * D / (pi * d**3), "108 MPa")
```

### Solid height and surge

A spring must not close to solid in service, and its coils must not resonate with the load cycle.

$$H_s = d\, N_t, \qquad f_1 = \frac{d}{2\pi D^2 N_a}\sqrt{\frac{G}{2\rho}}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $H_s$ | solid height | m |
| $N_t$ | total coils, active plus end coils | dimensionless |
| $f_1$ | first natural frequency of the coil (surge), both ends fixed | Hz |
| $\rho$ | wire density | $\text{kg/m}^3$ |
| $d$ | wire diameter | m |
| $D$ | mean coil diameter | m |
| $N_a$ | number of active coils | dimensionless |
| $G$ | shear modulus | Pa |

Holds when: the end coils are closed and ground, so $N_t = N_a + 2$, and both ends are held fixed.
Breaks when: one end is free (the frequency halves), or the spring is lightly loaded and its coils vibrate freely in a way the lumped model misses.
Source and basis: $H_s$ is a definition. The frequency is derived by setting the spring's mass $\rho (\pi d^2/4)(\pi D N_a)$ and rate $k$ into $f = \tfrac{1}{2}\sqrt{k/m}$, the first mode of a fixed-fixed spring; see [Vibrations reference](../physics/reference-vibrations.md).

A long compression spring can also buckle, and the limit depends on the free length, the coil diameter, and how the ends are supported, so check it with the maker's data or a column check. Keep the highest forcing frequency well below $f_1$ (and its multiples).

Example: the spring above has $N_t = 12$, so $H_s = 24$ mm. With steel density $7850\ \text{kg/m}^3$ (typical), $f_1 = 279$ Hz.

```verify
d = q(2, "mm")
expect(d * q(12, ""), "24 mm")
D = q(16, "mm")
Na = q(10, "")
G = q(79, "GPa", of="none")
rho = q(7850, "kg/m^3", of="none")
f1 = d / (2 * pi * D**2 * Na) * sqrt(G / (2 * rho))
expect(f1, "279 Hz")
```

## Rolling bearings

### Rating life

The basic rating life $L_{10}$ is the number of revolutions that 90 percent of a group of identical bearings reach or exceed, and it falls as a power of the equivalent load.

$$L_{10} = \left(\frac{C}{P}\right)^{a}, \qquad t_{10} = \frac{10^{6}\, L_{10}}{f_r}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $L_{10}$ | basic rating life in millions of revolutions | dimensionless |
| $C$ | basic dynamic load rating of the bearing | N |
| $P$ | equivalent dynamic load | N |
| $a$ | life exponent, 3 for ball bearings and 10/3 for roller bearings | dimensionless |
| $t_{10}$ | rating life as a running time | s |
| $f_r$ | rotational speed in revolutions per second | Hz |

Holds when: the load is steady, the lubrication is clean and adequate, and the bearing is aligned and mounted per its maker. The load rating $C$ is the value the maker gives for the stated rating basis.
Breaks when: the load is light or heavy beyond the catalogue range, the speed is very low or very high, the bearing is contaminated, misaligned, or run with poor lubrication (life is far shorter), or a reliability above 90 percent is required (apply a life adjustment factor).
Source and basis: the exponents 3 and 10/3 are registered in [bearing-life-exponents](../data/claims/machine-design.md#bearing-life-exponents), from a fit to test data, not derived. The units of $C$ and $P$ must match.

The equivalent load $P$ is the single steady radial load that would give the same life as the real mix of radial force $F_r$ and axial force $F_a$. It is written $P = X F_r + Y F_a$, where the factors $X$ and $Y$ depend on the bearing type and the ratio $F_a / F_r$, and come from the bearing maker's catalogue.

Example: with $C = 20$ kN and $P = 5$ kN, a ball bearing has $L_{10} = 64$ million revolutions. A roller bearing at the same ratio has $L_{10} = 102$ million revolutions. At 25 Hz (1500 rpm) the ball bearing life is 711 h, or $t_{10} = 2.56 \times 10^{6}$ s.

```verify
C = q(20, "kN")
P = q(5, "kN")
ball = (C / P)**3
roller = (C / P)**(q(10, "") / 3)
expect(ball, "64")
expect(roller, "102")
f = q(25, "Hz")
t = 1e6 * ball / f
expect(t, "711 h")
expect(t, "2.56e6 s")
given("1500", "10", "6")
```

## Sliding bearings

### Petroff friction, Sommerfeld number, and PV

A sliding (journal) bearing carries load on a film of oil or on a solid lining, and its friction and wear are set by the film and by the pressure-velocity product.

$$S = \frac{\mu N}{p}\left(\frac{r}{c}\right)^{2}, \qquad f = 2\pi^{2}\,\frac{\mu N}{p}\,\frac{r}{c}, \qquad PV = p\, v$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $S$ | Sommerfeld number | dimensionless |
| $f$ | coefficient of friction of the bearing (Petroff) | dimensionless |
| $\mu$ | dynamic viscosity of the oil | Pa s |
| $N$ | journal speed in revolutions per second | 1/s |
| $p$ | projected pressure, load over $L D$ | Pa |
| $r$ | journal radius | m |
| $c$ | radial clearance | m |
| $PV$ | pressure-velocity product | $\text{W/m}^2$ |
| $v$ | surface speed of the journal | m/s |

Holds when: for $S$ and $f$, a full oil film, Newtonian oil at one temperature, and a lightly loaded shaft that runs nearly concentric (Petroff). For $PV$, a dry or boundary-lubricated lining running steadily.
Breaks when: the shaft is heavily loaded and runs eccentric (use charts or the Reynolds equation), the bearing starts or stops (no film), or the oil heats noticeably. The $PV$ limit is a property of the lining material and comes from its supplier; none is given here.
Source and basis: Petroff's relation is derived from Couette shear of the oil in the clearance; the lesson [Lubrication and tribology](13-lubrication-and-tribology.md) derives it and treats regimes, viscosity, and film thickness.

Example: a 50 mm journal at 1800 rpm with $L = 50$ mm, $c = 0.050$ mm, load 2.00 kN, and $\mu = 0.040$ Pa s has $p = 0.80$ MPa, $S = 0.375$, and $f = 0.0148$. The surface speed is $v = 4.71$ m/s, so $PV = 3.77\ \text{MW/m}^2$.

```verify
D = q(50, "mm")
L = q(50, "mm")
c = q(0.050, "mm")
N = q(1800, "") / q(60, "s")
mu = q(0.040, "Pa s")
p = q(2.00, "kN") / (L * D)
expect(p, "0.80 MPa")
r = D / 2
S = mu * N / p * (r / c)**2
expect(S, "0.375")
expect(2 * pi**2 * mu * N / p * r / c, "0.0148")
v = pi * D * N
expect(v, "4.71 m/s")
expect(p * v, "3.77 MW/m^2")
```

## Gears

### Gear ratio, pitch-line velocity, and tangential load

Meshing gears share a module, and their speeds and torques follow from the tooth counts.

$$i = \frac{N_2}{N_1} = \frac{\omega_1}{\omega_2} = \frac{T_2}{T_1}, \qquad v = \frac{\omega\, d}{2}, \qquad W_t = \frac{2T}{d} = \frac{\dot{W}}{v}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $i$ | gear ratio, driven over driver | dimensionless |
| $N_1$, $N_2$ | tooth counts of driver and driven gear | dimensionless |
| $\omega_1$, $\omega_2$ | angular speeds of driver and driven gear | rad/s |
| $T_1$, $T_2$ | torques on driver and driven shaft, ideal | N m |
| $v$ | pitch-line velocity | m/s |
| $d$ | pitch diameter, $m_g N$ | m |
| $\omega$ | angular speed of the gear whose pitch diameter is $d$ | rad/s |
| $W_t$ | tangential tooth load at the pitch circle | N |
| $T$ | torque on the gear | N m |
| $\dot{W}$ | transmitted power | W |

Holds when: the gears are involute spur gears with a common module $m_g$ and no slip, and losses are small (a good spur pair loses a few percent).
Breaks when: the mesh has large friction losses (worm gears), the teeth are helical or bevel (the load has axial and radial parts), or speeds are high (dynamic loads add to $W_t$).
Source and basis: derived from rolling contact of the pitch circles ($v$ equal on both) and torque balance; taught in [Gears, fasteners, and springs](09-gears-fasteners-and-springs.md). Contact ratio of involute spur gears is in [Design reference](reference.md#gears).

Example: a pinion of module 2 mm with 20 teeth, driving a 40-tooth gear, runs at 20 Hz (1200 rpm) and transmits 5 kW. The ratio is 2.0, the pitch diameter is 40 mm, $v = 2.51$ m/s, and $W_t = 1989$ N.

```verify
m = q(2, "mm")
N1 = q(20, "")
N2 = q(40, "")
expect(N2 / N1, "2.0")
d = m * N1
expect(d, "40 mm")
w = 2 * pi * q(20, "Hz")
v = w * d / 2
expect(v, "2.51 m/s")
Pw = q(5, "kW")
expect(Pw / v, "1989 N")
expect(2 * (Pw / w) / d, "1989 N")
given("1200")
```

### Lewis tooth bending stress

The Lewis equation treats a gear tooth as a cantilever loaded by the tangential force at its tip, which gives the bending stress at the root.

$$\sigma = \frac{W_t}{F\, m_g\, Y}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\sigma$ | bending stress at the tooth root | Pa |
| $W_t$ | tangential load | N |
| $F$ | face width of the gear | m |
| $m_g$ | module | m |
| $Y$ | Lewis form factor, a function of tooth count and pressure angle | dimensionless |

Holds when: one tooth carries the whole load at its tip (a conservative case), the load is steady, and $Y$ is taken for the same tooth count and pressure angle.
Breaks when: the speed is high (multiply the load by a dynamic factor), more than one tooth pair shares the load, the fillet geometry is not standard, or the gear must also be checked for surface contact. Standards for gear rating add factors for overload, size, reliability, and geometry; this sheet does not reproduce them.
Source and basis: the form $\sigma = W_t P / (F Y)$ with $P$ the diametral pitch and $Y$ the Lewis form factor, a function of tooth count, is registered in [lewis-gear-bending](../data/claims/machine-design.md#lewis-gear-bending); the metric form follows with $P = 1/m_g$. The cantilever model is derived from [bending stress](../physics/reference-mechanics.md#stress-and-strain). Values of $Y$ come from tables for the tooth form.

Surface (contact) stress at the pitch line is the Hertz stress between two curved bodies, and it grows with the square root of the load per unit width; see [physics/reference-solid-mechanics.md](../physics/reference-solid-mechanics.md). Pitting and wear depend on it.

Example: the 20-tooth pinion above has face width 20 mm. With $Y = 0.32$ (an assumed form factor for this example), the root stress is $\sigma = 155$ MPa.

```verify
Wt = q(1989.4, "N")
F = q(20, "mm")
m = q(2, "mm")
Y = q(0.32, "")
expect(Wt / (F * m * Y), "155 MPa")
```

## Belts and chains

### Belt tensions and power

A flat or V belt transmits power through the difference between its tight-side and slack-side tensions, and friction on the wrap limits that ratio.

$$P_b = (F_1 - F_2)\, v, \qquad \frac{F_1}{F_2} = e^{\mu\theta}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $P_b$ | power transmitted | W |
| $F_1$ | tight-side tension | N |
| $F_2$ | slack-side tension | N |
| $v$ | belt speed | m/s |
| $\mu$ | friction coefficient of the belt on the pulley | dimensionless |
| $\theta$ | wrap angle on the smaller pulley | rad |

Holds when: the belt is on the point of slipping on the smaller pulley, the speed is low enough that centrifugal tension is small, and the belt is inextensible.
Breaks when: the speed is high (subtract the centrifugal tension $\dot{m}' v^2$ from both tensions, with $\dot{m}'$ the belt mass per metre, before applying the ratio), the belt is a V belt (the groove raises the effective $\mu$), or the belt creeps (the speed ratio is not exact).
Source and basis: the ratio is derived by the capstan relation in [Friction](../physics/reference-mechanics.md#friction); the power follows from force times speed.

Example: a 100 mm pulley at 25 Hz (1500 rpm) has $v = 7.85$ m/s. For $\mu = 0.3$ and a wrap of $\pi$ rad, $e^{\mu\theta} = 2.566$. To carry 2 kW, $F_1 - F_2 = 255$ N, so $F_2 = 163$ N and $F_1 = 417$ N.

```verify
d = q(100, "mm")
v = pi * d * q(25, "Hz")
given("1500")
expect(v, "7.85 m/s")
r = exp(q(0.3, "") * pi)
expect(r, "2.566")
dF = q(2, "kW") / v
expect(dF, "255 N")
F2 = dF / (r - 1)
expect(F2, "163 N")
expect(F2 + dF, "417 N")
```

### Chain speed and polygon effect

A roller chain wraps a sprocket as a polygon, so the chain speed varies a little with every tooth that engages.

$$v = z\, p_c\, f_r, \qquad \frac{v_{\text{min}}}{v_{\text{max}}} = \cos\frac{\pi}{z}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $v$ | mean chain speed | m/s |
| $z$ | number of teeth on the sprocket | dimensionless |
| $p_c$ | chain pitch | m |
| $f_r$ | sprocket speed in revolutions per second | Hz |
| $v_{\text{min}}$, $v_{\text{max}}$ | lowest and highest instantaneous chain speed | m/s |

Holds when: the chain is on a sprocket of $z$ teeth and the sprocket turns at constant speed.
Breaks when: the sprocket has few teeth (the variation grows fast, and wear and noise rise), the speed is high, or the chain is long and lightly tensioned (it whips).
Source and basis: derived from the geometry of a polygon of $z$ sides, in which the chain line moves between a radius to the pitch point and the apothem $\cos(\pi/z)$ times it.

Example: a 17-tooth sprocket with a 12.7 mm pitch chain at 10 Hz (600 rpm) gives a chain speed of $v = 2.16$ m/s. The speed varies by $1.70$ percent between its highest and lowest values.

```verify
z = q(17, "")
pc = q(12.7, "mm")
expect(z * pc * q(10, "Hz"), "2.16 m/s")
given("600")
expect((1 - cos(pi / z)) * 100, "1.70")
```

## Clutches and brakes

### Disk clutch torque

A disk clutch transmits torque by friction on an annular face, and the torque depends on whether the pressure is uniform or the wear is uniform.

$$T_p = \frac{2}{3}\,\mu\, F_a\, N_f\,\frac{r_o^3 - r_i^3}{r_o^2 - r_i^2}, \qquad T_w = \mu\, F_a\, N_f\,\frac{r_o + r_i}{2}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $T_p$ | torque for uniform pressure | N m |
| $T_w$ | torque for uniform wear | N m |
| $\mu$ | friction coefficient of the lining | dimensionless |
| $F_a$ | axial clamping force | N |
| $N_f$ | number of friction faces | dimensionless |
| $r_o$ | outer radius of the friction face | m |
| $r_i$ | inner radius of the friction face | m |

Holds when: the lining is flat and rigid, the coefficient is constant, and the force is steady. A new clutch follows the uniform-pressure case; after it wears in, the wear is uniform.
Breaks when: the lining overheats (friction falls at high temperature), the face is not flat, or slip is long and the heat is not carried away.
Source and basis: derived from integrating the friction moment $\mu\, p\, r\, dA$ over the annulus, with $p$ constant for $T_p$ and with $p\,r$ constant (equal wear rate) for $T_w$; the force is $F_a = \int p\, dA$ in both. The uniform-wear value is the lower, so it is the safer basis for the torque a clutch can carry.

Example: $\mu = 0.3$, $F_a = 2$ kN, $r_o = 100$ mm, and $r_i = 60$ mm on a single face give $T_p = 49.0\ \text{N m}$ and $T_w = 48.0\ \text{N m}$.

```verify
mu = q(0.3, "")
Fa = q(2, "kN")
ro = q(100, "mm")
ri = q(60, "mm")
expect(q(2, "") / 3 * mu * Fa * (ro**3 - ri**3) / (ro**2 - ri**2), "49.0 N m")
expect(mu * Fa * (ro + ri) / 2, "48.0 N m")
```

## Fits, preload, and alignment

### Torque capacity of a press fit

An interference fit holds a hub on a shaft by the contact pressure between them, and friction on that pressure carries torque and axial force.

$$T_{\text{cap}} = \frac{\mu\, p_c\,\pi\, d^2 L}{2}, \qquad F_{\text{cap}} = \mu\, p_c\,\pi\, d L$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $T_{\text{cap}}$ | torque the fit can carry before slipping | N m |
| $F_{\text{cap}}$ | axial force the fit can carry before slipping | N |
| $\mu$ | friction coefficient at the fit | dimensionless |
| $p_c$ | contact pressure at the interface | Pa |
| $d$ | nominal diameter of the fit | m |
| $L$ | length of the fit | m |

Holds when: the contact pressure is uniform over the fit, the friction coefficient is known, and both parts stay elastic. The pressure $p_c$ comes from the interference through the thick-wall (Lame) equations in [physics/reference-solid-mechanics.md](../physics/reference-solid-mechanics.md).
Breaks when: the parts yield, the hub is thin or the fit is short (end effects), the temperature changes the interference (differing expansion), or the load cycles (fretting at the ends of the fit). The fit classes themselves are in [Design reference](reference.md#tolerancing-and-stack-up).
Source and basis: derived from Coulomb friction on the cylinder of area $\pi d L$ with moment arm $d/2$.

Example: a pressure of 40 MPa on a 40 mm diameter fit of length 50 mm with $\mu = 0.15$ carries $T_{\text{cap}} = 754\ \text{N m}$ or $F_{\text{cap}} = 37.7$ kN axially. Apply the design factor to both.

```verify
mu = q(0.15, "")
pc = q(40, "MPa")
d = q(40, "mm")
L = q(50, "mm")
expect(mu * pc * pi * d**2 * L / 2, "754 N m")
expect(mu * pc * pi * d * L, "37.7 kN")
```

Alignment and preload are linked. A rolling bearing, a gear shaft, or a seal needs the shaft seat and the housing bore aligned within the maker's limit, set with the runout and position tolerances in [Design reference](reference.md#tolerancing-and-stack-up). Misalignment shortens bearing life far below the rating, and an overtightened bearing preload raises friction and heat.

## Checklists

Before sizing a joint:

- Preload uses the tensile stress area, not the nominal area, and a stated nut factor with its scatter.
- External load, preload, and member stiffness are checked: the joint stays closed, and the bolt stress range is compared with a fatigue strength.
- A fillet weld is checked on its throat, not its leg, and the weld group is checked for moment about its centroid.
- Torque capacity of a friction joint (press fit, clamp, clutch) is checked at the lowest friction coefficient.

Before releasing a shaft, bearing, or gear design:

- Shaft sized for combined bending and torsion, then checked for fatigue at every shoulder, keyway, and groove.
- Deflection, slope, and twist are within the limits of the bearings, seals, and gears they serve.
- Bearing life computed at the real equivalent load and speed, with the right exponent for the bearing type.
- Gears share a module and have a contact ratio above 1; bending and contact stresses both checked; lubrication matched to the pitch-line speed.
- Critical speed and the spring surge frequency are well away from the operating and forcing frequencies.

## Sanity checks

- A bolt preload is a large fraction of the proof load, so the preload of an M10 bolt of 8.8 class is in the tens of kN, not hundreds of N.
- Steel threads with the same torque at a lower nut factor give a higher preload, in proportion to $1/K$.
- A steel joint's constant $C$ is well under 1 (about 0.1 to 0.3), so most external load goes into the members.
- The throat of a fillet weld is about 0.7 times the leg, so the weld area is smaller than the leg times the length.
- A self-locking screw has an efficiency below one half.
- Halving a shaft's diameter cuts its torsion strength by a factor of 8 and its torsional stiffness by 16.
- Doubling the load on a ball bearing cuts its life by a factor of 8.
- Doubling the wire diameter multiplies a spring's rate by 16, and doubling the coil diameter divides it by 8.
- Gear ratio times speed out equals speed in; pitch-line velocity of steel gears in common machinery is a few metres per second to a few tens of metres per second.
- A belt's tight-side tension is at most about $e^{\mu\theta}$ times the slack side, which is about 2.5 for a half wrap on a smooth belt.

## Further reference

Named references only. None has a URL in this sheet. Look up the current edition.

- *Shigley's Mechanical Engineering Design* (paid): shafts, bearings, gears, springs, bolts, welds, clutches.
- *Machinery's Handbook* (paid): thread data, keys, splines, and standard sizes.
- *Roark's Formulas for Stress and Strain* (paid): beams, shafts, and contact stresses.
- Rating standards for rolling bearings and gears (paid): the governing methods for life, reliability, and tooth stress.
- Bearing and chain manufacturers' catalogues: load ratings, equivalent-load factors, and speed limits for the product you buy.
- [Elements of Mechanical Design (2.72, Spring 2009)](https://ocw.mit.edu/courses/2-72-elements-of-mechanical-design-spring-2009/) by MIT OpenCourseWare: free lecture notes on bearings, bolted joints, screws, gears, and clutches.
