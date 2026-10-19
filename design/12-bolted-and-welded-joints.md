# Bolted and welded joints

**Type:** lesson
**Verify:** strict

A joint is the place where one part is held to another so that load passes from one to the other, and a bolted or welded joint is one held by a clamping fastener or by metal fused across the seam. Joints are where most structures and machines actually fail, because load concentrates there and the joint is weaker than the parts it joins. This lesson shows how a preloaded bolt shares load with the clamped parts, why that sharing governs fatigue, how shear joints fail, and how to size a weld.

**Prerequisites:** [Factor of safety and failure](07-factor-of-safety-and-failure.md), [Gears, fasteners, and springs](09-gears-fasteners-and-springs.md) (bolt preload and tightening torque), [Axial and torsion](../physics/04-axial-and-torsion.md), [Fracture and fatigue](../materials/06-fracture-and-fatigue.md)
**Time:** 8-10 h

## Core ideas

Preload, the proof strength, and the torque-tension relation are in [Gears, fasteners, and springs](09-gears-fasteners-and-springs.md) and are not repeated here. This lesson starts from a bolt that already carries preload $F_i$.

### Bolted joints in tension

- **Stiffness** ($k$) is force per unit deflection, in N/m. A bolt and the parts it clamps are springs that carry the same force while the nut is tight.
- **Bolt stiffness** ($k_b$) follows from axial deformation: $k_b = A E / L$ for each length of constant area, and the segments (shank and threaded part) add as springs in series.
- **Member stiffness** ($k_m$) is the stiffness of the clamped parts. Their compression does not stay under the bolt head. It spreads outward in a cone, so the loaded volume is larger than the bolt and the members are much stiffer than the bolt. The common model replaces the cone with frustums.
- **Joint constant** ($C$) is the fraction of an external tensile load that goes into the bolt, $C = k_b/(k_b + k_m)$.
- **External load** ($P$) is the extra tension a joint carries beyond its preload, per bolt.

Before any external load, the bolt is stretched by $F_i$ and the members are squeezed by $F_i$. When $P$ pulls the members apart, the bolt stretches a little more and the members relax a little. The members were holding the bolt back, so the bolt only takes the share $C P$ and the members give up the share $(1 - C) P$ of their squeeze. A stiff member and a soft bolt give a small $C$: the bolt feels only a small part of the load.

**Separation** is the joint opening, which happens when the member force falls to zero. After that the bolt carries all of $P$ and the joint no longer clamps. Design keeps the actual load well below the separation load.

### Fatigue of bolts

**Fatigue** is failure under repeated load at stresses below the static strength (see [Fracture and fatigue](../materials/06-fracture-and-fatigue.md)). Preload helps fatigue. Because the bolt carries only $C P$ of a load that cycles between 0 and $P$, its stress range is small and is superimposed on a large steady stress from preload. A fatigue crack in a bolt starts where stress concentrates, at the thread root and under the head. The alternating stress is small, so the preload carries the mean. Loosen the bolt and the alternating stress rises to $P/A_t$.

### Shear joints

In a **shear joint** the load is perpendicular to the bolt axis. Three failures matter, besides the bolt shear itself.

- **Bearing** is the crushing of plate material against the bolt shank. The stress is taken as $F/(d t)$, force over the projected area of the hole.
- **Shear-out** (also called tear-out) is a plate tearing out along two planes between the hole and the free end. The planes lie parallel to the load, one on each side of the hole.
- **Net-section tension** is the plate fracturing across the hole, where its width is reduced.

A **slip-critical joint** is one designed so the parts never slide. Friction between the clamped faces carries the load, and the bolts only clamp. Slip begins when the load exceeds the friction resistance $\mu\, n\, F_i$, where $\mu$ is the coefficient of friction of the faying surfaces (the touching faces), and $n$ is the number of such faces. The coefficient depends strongly on surface condition, coating, and finish, so it is a measured or code value, not a constant.

### Welded joints

A **weld** is metal fused across a seam, so the joint becomes one piece of metal. Two forms dominate.

- A **butt weld** (groove weld) fills the gap between two parts that meet edge to edge. With full penetration, the weld carries load over the plate thickness: $\sigma = F/(t\, L)$ for tension, with $t$ the plate thickness and $L$ the weld length.
- A **fillet weld** has a roughly triangular cross-section in the corner between two surfaces. Its size is the **leg** $h$. Its weakest plane is the **throat**, the shortest distance from the root of the corner to the face of the weld. For an equal-leg weld with a flat face the throat is the altitude of a right isosceles triangle, $0.707\,h$. The **throat area** is $0.707\,h$ times the weld length. Fillet welds are loaded in shear on the throat, and this lesson treats them that way.

A **weld group** is several weld segments that together carry one load. Treat each segment as a line with throat thickness $0.707\,h$.

- The direct (primary) shear from a force $F$ through the centroid of the group is $\tau' = F/A$, with $A$ the total throat area.
- A load that acts off the centroid at distance $e$ adds a moment $M = F e$. The moment causes **secondary shear** $\tau'' = M r / J$ at distance $r$ from the centroid, in a direction perpendicular to $r$.
- $J = 0.707\,h\, J_u$ is the polar second moment of the throat area, with $J_u$ the second polar moment of the weld lines about the centroid taken as a unit throat.

At any point the two shears are vectors and add as vectors. The critical point is where they point closest to the same direction, usually the farthest end of the group.

### Weld fatigue and why weld toes crack

The **weld toe** is the line where the weld face meets the base plate. Four things make it the usual place a fatigue crack starts.

- The weld face meets the plate at an angle, which is a sharp change of geometry. Stress concentrates there.
- Welding leaves small flaws at the toe, such as slag intrusions and undercut. A crack therefore starts already present, and most of the life is crack growth, not initiation.
- Cooling leaves residual tensile stress near yield around the weld. The true mean stress is high whatever the applied mean stress, so the applied stress range matters more than the load ratio.
- Heat changes the grain structure and can leave a harder, more brittle zone beside the weld.

Because crack growth under a stress range $\Delta\sigma$ follows a power law, the life $N$ of a welded detail scales as $N \propto \Delta\sigma^{-m}$, with $m$ about 3 for typical structural steel details (a typical value; design codes give detail categories and their own values, which are not reproduced here). The practical consequence is that cutting the stress range is worth far more than raising the strength of the steel. Higher-strength steel does not improve the life of a welded detail by much, because the crack growth law depends little on strength.

> [!NOTE]
> Allowable stresses for welds and bolts come from the code or standard governing the structure. Edition, safety factors, and weld classes differ between codes and change between editions. This lesson gives the mechanics that every code is built on and uses stated example numbers, not code allowables.

## Key equations

Symbols: $A_b$ = bolt cross-section area ($\text{m}^2$), $E$ = elastic modulus (Pa), $L$ = length of a bolt segment (m), $k_b$ and $k_m$ = bolt and member stiffness (N/m), $d$ = bolt nominal diameter (m), $d_w$ = diameter of the washer face or bearing area (m), $l$ = grip length, the total thickness of the clamped parts (m).

Bolt stiffness for a bolt with area $A$ over length $L$:

$$
k_b = \frac{A E}{L}
$$

Member stiffness from the frustum model with a $\alpha = 30^\circ$ half-angle cone, valid for $d_w > d$ and a joint of one material (this is the commonly used cone model, a first estimate; finite element analysis does better):

$$
k_m = \frac{\pi E d \tan\alpha}{\ln \dfrac{(2 l \tan\alpha + d_w - d)(d_w + d)}{(2 l \tan\alpha + d_w + d)(d_w - d)}}
$$

Joint constant and load sharing, with $F_i$ the preload (N), $P$ the external tensile load per bolt (N), $F_b$ the bolt force (N), and $F_m$ the clamping force on the members (N):

$$
C = \frac{k_b}{k_b + k_m}, \qquad F_b = F_i + C P, \qquad F_m = F_i - (1 - C) P
$$

Separation occurs when $F_m = 0$, which gives the separation load $P_0$:

$$
P_0 = \frac{F_i}{1 - C}
$$

Bolt stresses for a load cycling from 0 to $P$, with $A_t$ the tensile stress area ($\text{m}^2$):

$$
\sigma_a = \frac{C P}{2 A_t}, \qquad \sigma_m = \frac{F_i}{A_t} + \frac{C P}{2 A_t}
$$

The Goodman safety factor $n$ follows from $1/n = \sigma_a/S_e + \sigma_m/S_{ut}$, with $S_e$ the corrected endurance limit and $S_{ut}$ the tensile strength (Pa), the same relation as in the [Design reference](reference.md).

Shear joint stresses, for a bolt of diameter $d$ in a plate of thickness $t$ and end distance $e_c$ measured from the hole edge to the free end, carrying shear force $F$:

$$
\sigma_{br} = \frac{F}{d t}, \qquad \tau_{so} = \frac{F}{2 e_c t}, \qquad F_{slip} = \mu\, n\, F_i
$$

Fillet weld, with leg $h$, total length $L_w$, force $F$, moment $M$ about the group centroid, distance $r$ from the centroid, and polar moment $J_u$ of the weld lines:

$$
A = 0.707\, h\, L_w, \qquad \tau' = \frac{F}{A}, \qquad \tau'' = \frac{M r}{0.707\, h\, J_u}
$$

For two parallel weld lines of length $a$ separated by $b$, the polar moment of the lines about the centroid is

$$
J_u = \frac{a b^2}{2} + \frac{a^3}{6}
$$

Holds when: loads act on the stated plane, the joint stays elastic, the weld is sound, and the members are the same material for the frustum model. Breaks when: the plates bend or open (prying), the bolt holes are oversize, the weld has defects, or the load is dynamic and the connection is not stiff.

## Worked example

**Bolted joint, external load and fatigue.** A pressure cover is held by M10 grade 8.8 bolts through two steel plates, each 10 mm thick. Each bolt is tightened to a preload of 75 percent of its proof load. In service each bolt sees an external tensile load that cycles between 0 and 10 kN. Find the joint constant, the peak bolt force, the load that would separate the joint, and the fatigue safety factor.

**Given:** $d = 10$ mm, $A_t = 58.0$ $\text{mm}^2$ (M10 coarse thread), $S_p = 580$ MPa, $E = 200$ GPa (a typical value for steel), grip $l = 20$ mm, $d_w = 1.5\,d$, $P = 10$ kN per bolt, $S_e = 129$ MPa (assumed corrected endurance limit for a rolled thread, a stated input for this example), $S_{ut} = 800$ MPa (assumed tensile strength, a stated input).

**Find:** $C$, $F_b$ at peak load, $P_0$, $n$.

**Assumptions:** the whole grip is modelled as threaded at area $A_t$ (which makes the bolt slightly less stiff than it is, so $C$ is a little low); the cone half-angle is $30^\circ$; both plates are the same steel; the load is applied at the bolt centre line.

**Solution:**

1. Bolt stiffness: $k_b = A_t E / l = 58.0 \times 200\,000 / 20 = 580$ kN/mm.
2. Member stiffness from the frustum formula with $d_w = 15$ mm and $\tan 30^\circ = 0.5774$: $k_m = 3384$ kN/mm.
3. Joint constant: $C = 580 / (580 + 3384) = 0.1463$, so the bolt takes about 15 percent of the external load.
4. Preload: $F_i = 0.75 \times 580 \times 58.0 = 25.2$ kN.
5. Peak bolt force: $F_b = 25.2 + 0.1463 \times 10 = 26.7$ kN. Member force at peak: $F_m = 25.2 - 0.8537 \times 10 = 16.7$ kN, still clamped.
6. Separation load: $P_0 = 25.2 / (1 - 0.1463) = 29.6$ kN.
7. Stresses: $\sigma_a = 0.1463 \times 10\,000 / (2 \times 58.0) = 12.6$ MPa, $\sigma_m = 25\,230 / 58.0 + 12.6 = 447.6$ MPa.
8. Goodman: $1/n = 12.6/129 + 447.6/800$, so $n = 1.52$.

**Answer:** $C = 0.146$, peak bolt force 26.7 kN, separation at $P_0 = 29.6$ kN (about three times the working load), fatigue safety factor $n = 1.52$.

**Sanity check:** the bolt force rises by only 1.5 kN while the external load rises by 10 kN, and $C$ is well under 1, as it should be for steel plates clamped by a bolt of this length. The preload is the bulk of the bolt stress.

<details><summary>Verification</summary>

```verify
d = q(10, "mm")
At = q(58.0, "mm^2")
Sp = q(580, "MPa")
E = q(200, "GPa", of="none")
l = q(20, "mm")
given("1.5", "0.75", "30", "0.5774", "8.8")
dw = 1.5 * d
P = q(10, "kN")
Se = q(129, "MPa")
Sut = q(800, "MPa")
kb = At * E / l
expect(E, "200000 MPa")
expect(dw, "15 mm")
expect(P, "10000 N")
expect(kb, "580 kN/mm")
tn = tan(pi / 6)
expect(tn, "0.5774")
km = pi * E * d * tn / log(((2 * l * tn + dw - d) * (dw + d)) / ((2 * l * tn + dw + d) * (dw - d)))
expect(km, "3384 kN/mm")
C = kb / (kb + km)
expect(C, "0.1463")
expect(C, "0.146")
Fi = 0.75 * Sp * At
expect(Fi, "25.2 kN")
expect(Fi, "25230 N")
Fb = Fi + C * P
expect(Fb, "26.7 kN")
Fm = Fi - (1 - C) * P
expect(Fm, "16.7 kN")
P0 = Fi / (1 - C)
expect(P0, "29.6 kN")
sa = C * P / (2 * At)
sm = Fi / At + sa
expect(sa, "12.6 MPa")
expect(sm, "447.6 MPa")
n = 1 / (sa / Se + sm / Sut)
expect(n, "1.52")
expect(1 - C, "0.8537")
expect(C * P, "1.5 kN")
check(Fm > q(0, "kN"), "joint stays clamped at peak load")
check(P0 > 2 * P, "separation load well above working load")
```

</details>

**Fillet weld group with an offset load.** A bracket is welded to a column with two vertical fillet welds, each 100 mm long, 100 mm apart. A 20 kN force acts in the plane of the welds, 150 mm from the centroid of the group. The leg is 6 mm. Find the largest shear stress on the throat.

**Given:** $a = 100$ mm, $b = 100$ mm, $h = 6$ mm, $F = 20$ kN, $e = 150$ mm.

**Find:** the resultant throat shear stress at the critical end.

**Assumptions:** equal-leg fillet welds loaded in shear on the throat, throat $0.707\,h$, the force is in the plane of the welds, the bracket and column are rigid, no code factor applied.

**Solution:**

1. Throat area: $A = 0.707 \times 6 \times 200 = 848$ $\text{mm}^2$ (two welds of 100 mm).
2. Direct shear: $\tau' = 20\,000 / 848 = 23.6$ MPa.
3. Moment: $M = 20\,000 \times 150 = 3.00 \times 10^6$ N mm.
4. Polar moment of lines: $J_u = 100 \times 100^2 / 2 + 100^3 / 6 = 6.67 \times 10^5$ $\text{mm}^3$. Then $J = 0.707 \times 6 \times 6.67\times10^5 = 2.83 \times 10^6$ $\text{mm}^4$.
5. Farthest end is at $x = 50$ mm, $y = 50$ mm, so $r = 70.7$ mm. Secondary shear: $\tau'' = 3.00 \times 10^6 \times 70.7 / 2.83 \times 10^6 = 75.0$ MPa, perpendicular to $r$.
6. Components. The secondary shear at this end has components $53.0$ MPa along $x$ and $53.0$ MPa along $y$, and the $y$ component adds to the direct shear. Sum along $y$: $23.6 + 53.0 = 76.6$ MPa.
7. Resultant: $\sqrt{53.0^2 + 76.6^2} = 93.2$ MPa.

**Answer:** the largest throat shear stress is about 93 MPa at the two outer ends of the welds. Compare it with the weld allowable that the governing code gives for the filler metal and load type.

**Sanity check:** the moment term dominates (75.0 MPa against 23.6 MPa), as expected for a load 150 mm off a 100 mm weld. The resultant must lie between the larger component, 76.6 MPa, and the sum of the two magnitudes, 98.6 MPa, and 93.2 MPa does.

<details><summary>Verification</summary>

```verify
a = q(100, "mm")
b = q(100, "mm")
h = q(6, "mm")
F = q(20, "kN")
e = q(150, "mm")
given("0.707", "2", "50", "6", "70.7", "3.00", "6.67", "2.83", "53.0")
A = 0.707 * h * 2 * a
expect(F, "20000 N")
expect(A, "848 mm^2")
tp = F / A
expect(tp, "23.6 MPa")
M = F * e
expect(M, "3.00e6 N mm")
Ju = a * b**2 / 2 + a**3 / 6
expect(Ju, "6.67e5 mm^3")
J = 0.707 * h * Ju
expect(J, "2.83e6 mm^4")
r = sqrt((b / 2)**2 + (a / 2)**2)
expect(r, "70.7 mm")
tpp = M * r / J
expect(tpp, "75.0 MPa")
comp = tpp * (b / 2) / r
expect(comp, "53.0 MPa")
y = tp + comp
expect(y, "76.6 MPa")
res = sqrt(comp**2 + y**2)
expect(res, "93.2 MPa")
expect(res, "93 MPa")
expect(tp + tpp, "98.6 MPa")
check(res < tp + tpp, "resultant is below the sum of the magnitudes")
check(res > y, "resultant exceeds the larger component")
```

</details>

## Practice

1. A bolt has $k_b = 1.0$ MN/mm and the clamped members have $k_m = 3.0$ MN/mm. Find the joint constant $C$.
2. For the joint in question 1, the preload is 20 kN. Find the external load at which the members separate, in kN.
3. A single 12 mm bolt joins an 8 mm plate and carries 30 kN in shear. The plate end distance from the hole edge to the free end is 18 mm. Find the bearing stress and the shear-out stress, in MPa.
4. Two plates are clamped by a bolt with preload 25.2 kN. The faying surfaces have $\mu = 0.30$ (an assumed value for this exercise) and there are two such faces. Find the slip load of the joint in kN, and say whether a design load of 18 kN slips.
5. A welded detail has a stress range of 60 MPa. A redesign raises the range to 120 MPa with the same detail. With life $N \propto \Delta\sigma^{-3}$, find the life ratio $N_{120}/N_{60}$, and say which has the longer life. Which would you change to extend life: a higher-strength steel, or a smoother weld toe at the same range?

<details><summary>Answers</summary>

1. $C = 0.25$
2. 26.7 kN
3. Bearing stress 312.5 MPa. Shear-out stress 104.2 MPa.
4. Slip load 15.1 kN. An 18 kN load exceeds it, so the joint slips.
5. The life ratio is 0.125, so the 120 MPa range lives one eighth as long. The smoother toe, because it removes the stress concentration and the flaws that set the life, while the steel strength barely changes the crack growth.

```verify
kb = q(1.0, "MN/mm")
km = q(3.0, "MN/mm")
C = kb / (kb + km)
expect(C, "0.25", ans=1)
Fi = q(20, "kN")
expect(Fi / (1 - C), "26.7 kN", ans=2)
F = q(30, "kN")
d = q(12, "mm")
t = q(8, "mm")
ec = q(18, "mm")
expect(F / (d * t), "312.5 MPa", ans=3)
expect(F / (2 * ec * t), "104.2 MPa", ans=3)
mu = q(0.30, "")
Fs = mu * 2 * q(25.2, "kN")
expect(Fs, "15.1 kN", ans=4)
check(q(18, "kN") > Fs, "18 kN exceeds the slip load")
expect((q(120, "MPa") / q(60, "MPa"))**(-3), "0.125", ans=5)
```

</details>

## Common mistakes

- Treating the full external load as added to the bolt. The bolt takes only $C P$ while the joint stays clamped, and once it separates it takes all of $P$.
- Using the nominal bolt area $\pi d^2/4$ instead of the tensile stress area $A_t$ in stress and stiffness. The thread root is smaller.
- Using the leg $h$ as the weld thickness in shear. The throat is $0.707\,h$.
- Taking the force at the centre of a weld group when the load is offset, and so leaving out the secondary shear. The two shears add as vectors, not as magnitudes.
- Judging weld fatigue by static strength or by mean stress. The stress range at the toe and the detail geometry govern, and the base metal strength helps little.

## Go deeper

- [Elements of Mechanical Design (2.72, Spring 2009)](https://ocw.mit.edu/courses/2-72-elements-of-mechanical-design-spring-2009/) by MIT OpenCourseWare: free course notes on machine elements, including fasteners and joints.
- [Tribology (2.800, Fall 2004)](https://ocw.mit.edu/courses/2-800-tribology-fall-2004/) by MIT OpenCourseWare: friction and wear at the faying surfaces that slip-critical joints rely on.
- Name a paid book: *Shigley's Mechanical Engineering Design* covers the frustum model and bolt fatigue in depth.
- Next: [Lubrication and tribology](13-lubrication-and-tribology.md) explains the friction and wear that act inside joints and bearings.
- [Gears, fasteners, and springs](09-gears-fasteners-and-springs.md), [Design reference](reference.md): preload, torque, the fatigue lines, and the joint constant in short form.
