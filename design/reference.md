# Design reference

**Type:** reference

Mechanical design is the field of choosing the shape, size, material, and tolerances of machine parts so they carry their loads safely and can be made and assembled. Every design choice trades cost, safety, and performance against one another, and a poor choice shows up later as a failed part or an expensive rework. Lookup sheet for mechanical design: process gates, factor of safety, static and fatigue failure, tolerancing and GD&T, fits, fasteners, shafts, bearings, gears, springs, and DFMA. For an engineer who knows the basics and needs a formula, a limit, or a checklist mid-task.

## Principles

- Function drives the design. Choose tolerances, characteristics, and factors of safety from what the part must do and what happens if it fails.
- Loads are forces, stresses are what the material feels. Compute stress from load and area, then compare with a strength.
- Every number needs units. Keep one consistent system (SI here: N, mm, MPa) and convert once, at the start.
- A factor of safety is a statement of what you do not know. State it and its basis.
- Stress concentration, assembly access, and manufacturing process decide more failures than the nominal formula does.
- A tolerance is a design choice with a cost. Tighten only where the function needs it.
- If a result is surprising, check the sanity bounds before checking the algebra.
- Weight is $W = m\,g$, with $g$ the local gravity. Earth value $g = 9.81$ $\text{m/s}^2$ is one case, not the rule.

## Design process

| Stage | Output | Gate question |
|---|---|---|
| Need | One-sentence need | Does the need say what success looks like? |
| Requirements | Measurable list with metric, target, and limit | Can a second engineer test each one without asking? |
| Constraints | Separate list (budget, envelope, rules) | Are limits kept apart from goals? |
| Concepts | At least three distinct options | Were alternatives compared, not just the first idea? |
| Selection | Trade study or decision matrix | Are hard requirements checked before totals? |
| Detail design | Geometry, materials, tolerances, drawings | Does every critical feature have a tolerance and a check? |
| Prototype and test | Measured data with date, setup, and tester | Did the test answer the riskiest assumption? |
| Iteration and review | Recorded change and reason | Is each action owned and dated? |

- Trade study score: sum of (weight times score) over criteria. Weights and scores are usually 1 to 5.
- A concept that fails a hard requirement is out, whatever its total.
- Review outcomes: proceed, proceed with actions, or return to an earlier stage.
- Holds when: the requirements are stable enough to test. Breaks when: requirements drift silently; log every change with its reason.

## Factor of safety

Definition, ductile yield basis:

$$
n = \frac{S_y}{\sigma}
$$

where $S_y$ is yield strength (Pa or MPa) and $\sigma$ is the governing stress (same unit). For brittle materials use $S_{\text{ut}}$ or $S_{\text{uc}}$ in place of $S_y$ and state it.

Choose $n$ from how well the inputs are known. Specific values come from the governing code, client, or industry; the table gives direction only.

| Knowledge of loads | Knowledge of material | Consequence of failure | Direction for $n$ |
|---|---|---|---|
| Measured or certified | Tested, certified stock | Low, easy to inspect | Lowest. Justify it. |
| Calculated, bounded | Handbook typical | Moderate | Moderate |
| Estimated, shock or fatigue likely | Unknown or variable | High, or hard to inspect | Highest |

- Holds when: loads and strengths are each characterized. Breaks when: a load case or a process variation is missing; the margin then means nothing.
- Use the lowest $n$ you can justify. Extra material adds mass, cost, and sometimes new failure modes.
- Stating the basis (yield or ultimate, static or fatigue, which load case) matters as much as the number.

## Static failure theories

Plane stress: $\sigma_x$, $\sigma_y$, $\tau_{xy}$. Principal stresses:

$$
\sigma_{1,2} = \frac{\sigma_x + \sigma_y}{2} \pm \sqrt{\left(\frac{\sigma_x - \sigma_y}{2}\right)^2 + \tau_{xy}^2}
$$

Von Mises equivalent stress in plane stress:

$$
\sigma_{\text{vm}} = \sqrt{\sigma_x^2 - \sigma_x \sigma_y + \sigma_y^2 + 3\tau_{xy}^2}
$$

Sorted principal stresses $\sigma_1 \ge \sigma_2 \ge \sigma_3$. Maximum shear:

$$
\tau_{\max} = \frac{\sigma_1 - \sigma_3}{2}
$$

| Theory | Material class | Failure condition | Use when | Limit |
|---|---|---|---|---|
| Maximum normal stress (Rankine) | Brittle (cast iron, glass, ceramics) | $\sigma_1 \ge S_{\text{ut}}$ or $\sigma_3 \le -S_{\text{uc}}$ | Brittle, tension governs | Ignores shear; no interaction between modes |
| Tresca (maximum shear) | Ductile | $\sigma_1 - \sigma_3 \ge S_y$, so $n = S_y/(\sigma_1 - \sigma_3)$ | Ductile, quick and conservative check | Underpredicts the yield load by up to about 15 percent (conservative) |
| Von Mises (distortion energy) | Ductile | $\sigma_{\text{vm}} \ge S_y$, so $n = S_y/\sigma_{\text{vm}}$ | Ductile metals, general default | Yield only; not for brittle |
| Mohr-Coulomb | Brittle, unequal tension and compression strength | $\sigma_1/S_{\text{ut}} - \sigma_3/S_{\text{uc}} \ge 1$ (compression $\sigma_3$ negative) | Rock, soil, cast iron, concrete-like | Needs both strengths; not for ductile metals |

- Tresca and von Mises differ by up to about 15 percent in plane stress. They agree in uniaxial tension. In pure shear Tresca gives an equivalent stress of $2\tau$ and von Mises gives $\sqrt{3}\,\tau$, about 15 percent apart.
- Worked check (von Mises): $\sigma_x = 120$, $\sigma_y = 40$, $\tau_{xy} = 30$ MPa gives $\sigma_{\text{vm}} = 117.9$ MPa. With $S_y = 350$ MPa, $n = 2.97$.
- Worked check (Mohr-Coulomb): $\sigma_1 = 100$, $\sigma_3 = -200$ MPa, $S_{\text{ut}} = 600$, $S_{\text{uc}} = 800$ MPa gives bracket $= 0.1667 + 0.25 = 0.4167$, so $n = 2.40$.
- Holds when: loading is static and the material behaves as its class. Breaks when: loads cycle (use fatigue), temperature is high (creep), or the part is near a notch and is brittle.

## Fatigue

Stress cycle definitions:

$$
\sigma_a = \frac{\sigma_{\max} - \sigma_{\min}}{2}, \qquad \sigma_m = \frac{\sigma_{\max} + \sigma_{\min}}{2}, \qquad R = \frac{\sigma_{\min}}{\sigma_{\max}}
$$

Rotating-beam endurance limit of the test specimen (steel, typical):

$$
S_e' = \begin{cases} 0.5\,S_{\text{ut}} & S_{\text{ut}} \le 1400\ \text{MPa} \\ 700\ \text{MPa} & S_{\text{ut}} > 1400\ \text{MPa} \end{cases}
$$

Marin factors, applied to the specimen value to get the part endurance limit:

$$
S_e = k_a\,k_b\,k_c\,k_d\,k_e\,k_f\,S_e'
$$

| Factor | Name | Typical basis (textbook typical) |
|---|---|---|
| $k_a$ | Surface | $k_a = a\,S_{\text{ut}}^{\,b}$ with $S_{\text{ut}}$ in MPa. Typical $(a, b)$: ground $(1.58, -0.085)$; machined or cold drawn $(4.51, -0.265)$; hot rolled $(57.7, -0.718)$; as forged $(272, -0.995)$ |
| $k_b$ | Size | Rotating round, $d$ in mm: $1.24\,d^{-0.107}$ for $2.79 \le d \le 51$; $1.51\,d^{-0.157}$ for $51 < d \le 254$. Use $1$ for axial. For non-round bending, use an equivalent diameter $d_e$ in the same formulas (rectangle: $d_e = 0.808\sqrt{bh}$) |
| $k_c$ | Load | Bending $1.0$; axial $0.85$; torsion $0.59$ |
| $k_d$ | Temperature | $1.0$ at room temperature; derate at elevated temperature (a common textbook polynomial gives about $0.85$ for steel at 450 C), from a data source |
| $k_e$ | Reliability | 50 %: 1.000; 90 %: 0.897; 95 %: 0.868; 99 %: 0.814; 99.9 %: 0.753; 99.99 %: 0.702 |
| $k_f$ | Miscellaneous | $1.0$ by default; apply for corrosion, plating, residual stress, or cold-work effects, from a source |

- Holds when: steel with $S_{\text{ut}}$ known; Marin factors are multiplicative. Breaks when: non-steel (aluminum has no endurance limit in the same sense; use its life curve), corrosion, or unknown surface.
- Worked example (ground, $d = 25$ mm, $S_{\text{ut}} = 600$ MPa, 95 % reliability): $k_a = 0.917$, $k_b = 0.879$, $S_e = 210$ MPa.

Fatigue failure lines, with mean stress $\sigma_m$, alternating $\sigma_a$, endurance $S_e$, ultimate $S_{\text{ut}}$, yield $S_y$, factor $n$:

| Line | Equation for $n$ | Character |
|---|---|---|
| Goodman | $\dfrac{1}{n} = \dfrac{\sigma_a}{S_e} + \dfrac{\sigma_m}{S_{\text{ut}}}$ | Conservative for ductile metals; simple |
| Soderberg | $\dfrac{1}{n} = \dfrac{\sigma_a}{S_e} + \dfrac{\sigma_m}{S_y}$ | Most conservative; no yield check needed |
| Gerber | $n\,\dfrac{\sigma_a}{S_e} + \left(n\,\dfrac{\sigma_m}{S_{\text{ut}}}\right)^2 = 1$ | Fits ductile data best; can be non-conservative |

- Worked example: $\sigma_a = 100$, $\sigma_m = 50$, $S_e = 209.9$, $S_{\text{ut}} = 600$, $S_y = 400$ MPa. Goodman $n = 1.79$; Soderberg $n = 1.66$; Gerber $n = 2.04$.
- Compressive mean stress is often set to zero in simple checks. State the choice; check the code.
- Yield check: the line $\sigma_a + \sigma_m = S_y$ must also hold for the peak stress when yielding can occur.
- Holds when: the cycle is stable and the stress state is known at the critical point. Breaks when: the surface is damaged, load sequence matters (for example overload or variable amplitude), or the part is non-metallic.

## Stress concentration

Stress concentration is local peak stress at geometry changes: holes, fillets, keyways, shoulders, threads, sharp corners, welds, and cracks.

$$
K_t = \frac{\sigma_{\max}}{\sigma_{\text{nom}}}, \qquad K_f = 1 + q\,(K_t - 1)
$$

- $K_t$ is the geometric factor. Read it from charts or tables for the geometry (for example Peterson's Stress Concentration Factors; not reproduced here).
- $q$ is notch sensitivity, from $0$ (no notch effect) to $1$ (full effect). It depends on material and notch radius.
- $K_f \le K_t$ always.
- Where it matters: fatigue (almost always), brittle materials, and any cyclic or impact load. Ductile static yield often redistributes stress, so $K_t$ is usually not applied for static yield, but check the code.
- Where it does not matter much: smooth, uniform members under static loads of ductile material.
- Holds when: the feature is a local notch in a member with a stress gradient. Breaks when: the notch is sharp relative to its size, or the effect is combined with corrosion or temperature.

## Tolerancing and stack-up

Limits from nominal $N$ and plus-minus tolerance $t$:

$$
L_{\max} = N + t, \qquad L_{\min} = N - t, \qquad T = 2t
$$

Linear stack, gap $g = L - \sum a_i$ (sign of each term follows its direction in the chain):

- Worst case: $T_{\text{wc}} = \sum_i \lvert t_i \rvert$. Guarantees the fit; conservative.
- RSS: $T_{\text{rss}} = \sqrt{\sum_i t_i^2}$. A statistical estimate. Valid only for independent, stable, centered processes. Mean shift adds to it and is not in this formula.
- Clearance: $C_{\min} = H_{\min} - S_{\max}$, $C_{\max} = H_{\max} - S_{\min}$ for hole $H$ and shaft $S$. Negative clearance is interference.

- Worked: $L = 60.00 \pm 0.15$, $a = 25.00 \pm 0.05$, $b = 30.00 \pm 0.08$ mm gives nominal gap $5.00$ mm, worst case $\pm 0.28$ mm, RSS $\pm 0.177$ mm.
- Holds when: the chain is linear and every contributor is included. Breaks when: parts are not in one line (use vector or 3D stack), contributors are not independent, or a hidden contributor (fixture, thermal growth, deflection) is missing.
- Rule of thumb: use worst case where failure is costly or the assembly cannot be adjusted; use RSS only with measured process data.

## GD&T: characteristic symbols

Fourteen geometric characteristic symbols, from the ASME Y14.5 set (ISO 1101 uses the same family with different names and conventions).

| # | Characteristic | Category | Datum required? |
|---|---|---|---|
| 1 | Straightness | Form | No |
| 2 | Flatness | Form | No |
| 3 | Circularity | Form | No |
| 4 | Cylindricity | Form | No |
| 5 | Profile of a line | Profile | No, unless it controls orientation or location |
| 6 | Profile of a surface | Profile | No, unless it controls orientation or location |
| 7 | Angularity | Orientation | Yes |
| 8 | Perpendicularity | Orientation | Yes |
| 9 | Parallelism | Orientation | Yes |
| 10 | Position | Location | Yes |
| 11 | Concentricity | Location | Yes; removed from ASME Y14.5-2018 (use position or profile instead), still used in ISO GPS (ISO 1101) |
| 12 | Symmetry | Location | Yes; removed from ASME Y14.5-2018 (use position or profile instead), still used in ISO GPS (ISO 1101) |
| 13 | Circular runout | Runout | Yes |
| 14 | Total runout | Runout | Yes |

- Form controls shape only. Orientation, location, and runout need a datum or datums.
- Circularity controls one cross section; cylindricity controls the whole surface.
- Runout is measured while rotating about a datum axis; form is not.
- One characteristic per feature control frame. Read left to right: symbol, tolerance (full zone width), modifier, datums.

## GD&T: material conditions

| Modifier | Meaning | Hole | Shaft or pin |
|---|---|---|---|
| MMC (circled M) | Maximum material condition | Smallest allowed size | Largest allowed size |
| LMC (circled L) | Least material condition | Largest allowed size | Smallest allowed size |
| RFS | Regardless of feature size (no bonus) | Zone fixed | Zone fixed |

- RFS is the default in current practice when no modifier is shown.
- Bonus only applies with MMC or LMC. Check the modifier before you use bonus.

Bonus tolerance (never negative):

$$
B_{\text{hole}} = A - \text{MMC}_{\text{hole}}, \qquad B_{\text{shaft}} = \text{MMC}_{\text{shaft}} - A
$$

where $A$ is the actual size. Total allowed position at MMC:

$$
t_{\text{total}} = t_{\text{pos}} + B
$$

Virtual condition (gauge design):

$$
V_{\text{hole}} = \text{MMC}_{\text{hole}} - t_{\text{pos}}, \qquad V_{\text{shaft}} = \text{MMC}_{\text{shaft}} + t_{\text{pos}}
$$

## Position of holes

Position deviation as a diameter from radial offsets $x$, $y$ in the datum frame:

$$
d = 2\sqrt{x^2 + y^2}
$$

Pass when $d \le t_{\text{total}}$.

- Worked: hole $\varnothing 10.00 \pm 0.10$, position $\varnothing 0.25$ at MMC, actual $A = 9.95$, offsets $x = 0.11$, $y = 0.09$ mm. MMC $= 9.90$, bonus $= 0.05$, total $= 0.30$, deviation $= 0.284$. Passes at MMC; would fail at RFS ($0.284 > 0.25$).
- Holds when: datums are set as the drawing says and the offsets are in the datum frame. Breaks when: the measurement uses the wrong datum order, or the gauge is not at virtual condition.

## Datum reference frames

- A datum is a theoretical reference. A datum feature is the real surface that establishes it.
- Datum letters run A to Z, skipping I, O, and Q.
- A datum reference frame (DRF) is set in order: primary, secondary, tertiary.
- 3-2-1 idea: primary restricts 3 degrees of freedom (plane), secondary 2 (line), tertiary 1 (point). Together they fix the part.
- Datum order in the frame is the order of setup. Reversing it changes the result.
- Choose datums from how the part mounts or mates. Use the surfaces the mate touches.
- Form controls take no datum. Do not add one.

## Fits (ISO hole basis)

Hole basis uses H (lower deviation zero) with a shaft letter. Limits come from ISO 286 tables; the qualitative behavior is:

| Fit | Type | Qualitative behavior | Typical use |
|---|---|---|---|
| H7/g6 | Clearance | Shaft slides or turns freely by hand; smallest clearance | Precision sliding, close-running |
| H7/h6 | Clearance (locational) | Slides by hand; near zero clearance at the largest shaft | Location with easy assembly |
| H7/k6 | Transition | Snug; can have a slight gap or slight interference | Locating, held by light tapping |
| H7/p6 | Interference | Light press; needs a press or thermal assembly | Permanent location, no key |

- Shaft letters: $a$ to $h$ give clearance with $H$; $j$ to $n$ give transition; $p$ to $\text{zc}$ give interference.
- Holds when: the fit is between features of the same nominal size, at room temperature, with the tolerance grades stated. Breaks when: materials have different thermal expansion or the press force is not checked.

## Fasteners

Preload and bolt sizing:

$$
F_i = 0.75\,S_p\,A_t \qquad \text{(reused joint; }0.9\,S_p A_t\text{ is often used for a permanent joint)}
$$

where $S_p$ is proof strength (MPa) and $A_t$ is tensile stress area ($\text{mm}^2$). Use $A_t$, not the nominal area.

Torque-tension (nut factor $K$, typical dry steel about $0.20$; lubricated values are lower):

$$
T = K\,F_i\,d
$$

with $T$ in $\text{N}\cdot\text{mm}$, $F_i$ in N, $d$ in mm. Divide by 1000 for $\text{N}\cdot\text{m}$.

Joint stiffness split under external load $P$, with bolt stiffness $k_b$ and member stiffness $k_m$:

$$
C = \frac{k_b}{k_b + k_m}, \qquad F_b = F_i + C\,P, \qquad F_m = F_i - (1 - C)\,P
$$

- A stiff member and a soft bolt give small $C$: most external load goes into the clamped parts, and fatigue life of the bolt improves.
- Example: $k_b = 1$, $k_m = 4$ gives $C = 0.2$.
- Thread engagement rule of thumb: steel nut into steel, about one nominal diameter. Softer materials (aluminum, cast iron, plastics) need longer engagement, commonly 1.5 times the diameter or more. Check thread stripping in softer parts.
- Holds when: the joint is rigid-body, preload stays (no embedding or relaxation), and the bolt stays in the elastic range. Breaks when: the joint is compliant, vibration causes loosening, or torque is the only control (scatter is large because friction varies).
- Worked: M10 grade 8.8, $S_p = 580$ MPa, $A_t = 58.0$ $\text{mm}^2$, $K = 0.20$. $F_i = 25.2$ kN, $T = 50.5$ $\text{N}\cdot\text{m}$.

## Shafts

Solid round shaft, bending $\sigma$ and torsion $\tau$:

$$
\sigma = \frac{32\,M}{\pi d^3}, \qquad \tau = \frac{16\,T}{\pi d^3}
$$

Hollow shaft torsion, outside diameter $d_o$, inside $d_i$:

$$
\tau = \frac{16\,T\,d_o}{\pi\,(d_o^4 - d_i^4)}
$$

Angle of twist over length $L$ with shear modulus $G$ and polar moment $J = \pi d^4/32$ (solid):

$$
\theta = \frac{T\,L}{G\,J}
$$

Static sizing for combined bending and torsion, ductile, ASME elliptic form (use $M$ and $T$ in $\text{N}\cdot\text{mm}$, $S_y$ in MPa):

$$
d = \left(\frac{16\,n}{\pi\,S_y}\sqrt{4M^2 + 3T^2}\right)^{1/3}
$$

- Worked: $M = 150$ $\text{N}\cdot\text{m}$, $T = 200$ $\text{N}\cdot\text{m}$, $S_y = 350$ MPa, $n = 2.5$ gives $d = 25.6$ mm (use a standard size at or above).
- Tresca alternative for torsion only: $\tau_{\text{allow}} = 0.5\,S_y/n$, $d_{\min} = (16\,T/(\pi\,\tau_{\text{allow}}))^{1/3}$.
- Stress concentration (keyway, shoulder, fillet, retaining ring groove) is not in these formulas. Apply $K_f$ for fatigue or check the code.
- Holds when: the shaft is solid, round, loaded steadily, and uniform. Breaks when: the shaft cycles (use fatigue), has notches, or is hollow with a thin wall.

Critical speed (lateral, first mode, single mass $m$ on a stiffness $k$ at the midspan of a simply supported shaft):

$$
\omega_n = \sqrt{\frac{k}{m}}, \qquad k = \frac{48\,E\,I}{L^3}
$$

with $\omega_n$ in rad/s, $E$ in Pa, $I$ in $\text{m}^4$, $L$ in m, $m$ in kg. Operate away from it with margin set by the code or the designer; include shaft mass for better accuracy.

- Holds when: the shaft is uniform and the mass is lumped at midspan. Breaks when: the shaft is stepped, the mass is spread, bearings are soft, or the load is off center.

## Bearings

Basic rating life of a rolling bearing, in millions of revolutions, with dynamic rating $C$ and equivalent load $P$ (same units):

$$
L_{10} = \left(\frac{C}{P}\right)^p, \qquad p = 3 \text{ (ball)}, \qquad p = \frac{10}{3} \text{ (roller)}
$$

Life in hours at speed $n$ (rpm):

$$
L_h = \frac{10^6\,L_{10}}{60\,n}
$$

- $L_{10}$ is the life that 90 percent of a group survives.
- Doubling the load cuts life by $2^3 = 8$ for ball bearings.
- Worked: $C = 20$ kN, $P = 5$ kN, $n = 1500$ rpm gives $L_{10} = 64$ million revolutions, $L_h = 711$ h.
- Holds when: loads are steady and clean lubrication is maintained. Breaks when: misalignment, contamination, shock, low speed with high load, or poor lubrication shortens life far below the rating.
- Shaft seat fit and runout (see GD&T and fits) keep the bearing rings round and supported.

## Gears

Spur gear relations, metric module $m$ (mm) and teeth $N$:

$$
d = m\,N, \qquad C = \frac{m\,(N_1 + N_2)}{2}, \qquad i = \frac{N_2}{N_1} = \frac{n_1}{n_2} = \frac{T_2}{T_1}
$$

- Meshing gears share the same module.
- $d$ is the pitch diameter; $C$ is center distance (average of pitch diameters).
- Ratio $i > 1$ reduces speed and raises torque (ideal; losses ignored).
- Pitch-line velocity with $d$ in mm, $n$ in rpm, $v$ in m/s: $v = \pi\,d\,n / 60\,000$.
- Worked: $m = 2$ mm, $N_1 = 20$, $N_2 = 40$, $n_1 = 1200$ rpm gives $d_1 = 40$ mm, $C = 60$ mm, $i = 2.0$, $v = 2.51$ m/s.

Contact ratio, involute spur gears, pressure angle $\phi$ (typical $20$ degrees), base radius $r_b = r\cos\phi$, addendum radius $r_a$:

$$
m_c = \frac{\sqrt{r_{a1}^2 - r_{b1}^2} + \sqrt{r_{a2}^2 - r_{b2}^2} - C\sin\phi}{\pi\,m\cos\phi}
$$

- The contact ratio must exceed 1 so that one tooth pair is always in contact. Spur gears commonly run from about 1.4 to 2.0 (typical).
- Worked: $m = 2$, $N_1 = 20$, $N_2 = 40$, $\phi = 20$ degrees gives $m_c = 1.64$.
- Holds when: involute profile, standard addendum, no backlash, ideal alignment. Breaks when: profile errors, misalignment, shock, high speed (dynamic loads), or poor lubrication. Failure modes: bending fatigue at the tooth root, pitting, scuffing, wear, noise.

## Springs

Helical compression spring, wire diameter $d$, mean coil diameter $D$, active coils $N_a$, shear modulus $G$ (typical steel about 79 GPa):

$$
k = \frac{G\,d^4}{8\,D^3\,N_a}, \qquad F = k\,x
$$

- Spring index $C_s = D/d$. Typical range 4 to 12 (typical).
- Wahl factor for shear stress from force $F$ and mean coil diameter $D$:

$$
K_w = \frac{4C_s - 1}{4C_s - 4} + \frac{0.615}{C_s}, \qquad \tau = K_w\,\frac{8\,F\,D}{\pi\,d^3}
$$

- Example: $C_s = 8$ gives $K_w = 1.184$.
- Series springs (same force): $\dfrac{1}{k_{\text{eq}}} = \sum \dfrac{1}{k_i}$. For $n$ identical springs in series, $k_{\text{eq}} = k/n$.
- Parallel springs (same deflection): $k_{\text{eq}} = \sum k_i$. For $n$ identical springs in parallel, $k_{\text{eq}} = n\,k$.
- Worked: $d = 2$ mm, $D = 16$ mm, $N_a = 10$, $G = 79$ GPa gives $k = 3.86$ N/mm.
- Holds when: linear, helical, round wire, deflection well below solid height and below the elastic limit. Breaks when: the spring is compressed to solid, stressed past its elastic limit (set and loss of free length), or near resonance.
- Check the deflection against solid height and the elastic limit, not only the rate.

## Design for manufacturing and assembly (DFMA)

- Reduce part count. For each part, ask whether it can be merged with another without hurting function.
- Count fasteners. Replace them with snap, press, or molded features where the load allows.
- One assembly direction, from the top or a single side, is easier than parts that need flipping.
- Self-locating features (pins, chamfers, tapers, slots) remove measurement.
- Access: every fastener and tool must reach its location. The last step must be reachable.
- Process fit: choose the process early. Casting and molding need draft, uniform walls, and radii. Machining prefers standard tool sizes and avoids deep thin holes. Sheet metal needs bend radius and hole-to-bend spacing from the shop.
- Standard parts and sizes (fasteners, bearings, stock) cut cost and risk.
- Tolerance only the features that need it.
- Test: build a mockup and time the assembly. Count the parts and operations before and after.

Part-count reduction is $\dfrac{N_0 - N_1}{N_0}$, with $N_0$ the starting count.

- Example: 12 parts to 7 gives $41.7$ percent reduction.

## Checklists

Before trusting a stress result:

- Stress from load and correct area, with units consistent (N and $\text{mm}^2$ give MPa).
- Strength matches the failure mode (yield for ductile static, ultimate for brittle, endurance for cyclic).
- Failure theory matches the material class.
- Factor of safety stated with its basis.
- Stress concentration considered, and $K_f$ applied for fatigue.

Before releasing a dimensioned design:

- Every requirement has a metric and a pass value.
- Every critical feature has a tolerance, and the stack-up is checked (worst case or RSS, with the choice stated).
- Each GD&T frame has one characteristic; datums are on real surfaces; datum order matches setup.
- Modifiers (MMC, LMC, RFS) are set on purpose; bonus is used only with them.
- Fits are the intended ISO class; interference parts have a press or thermal plan.
- Fasteners: $A_t$ used; preload and torque stated; engagement checked; joint stiffness considered for fatigue.
- Shafts and bearings: critical speed, fits, and runout checked; bearing life at the real load and speed.
- Gears: same module, contact ratio above 1, mesh checked.
- Springs: deflection below solid and below elastic limit; Wahl factor used for stress.
- Assembly: each part locates before fastening; every fastener is reachable; sequence walked through.

## Sanity checks

- Stress from $F/A$ for a 1 kN axial load on a 10 mm round bar: $A = 78.5$ $\text{mm}^2$, so $\sigma = 12.7$ MPa. Expect results of this order for light loads.
- Steel modulus $E \approx 200$ GPa (typical); $G \approx 79$ GPa (typical); Poisson ratio about 0.3 (typical). Aluminum $E \approx 70$ GPa (typical).
- Steel yield strength is a few hundred MPa for common grades (typical). A computed stress above yield in a ductile part means yielding or a unit error.
- Unit check: $1\ \text{MPa} = 1\ \text{N/mm}^2$; $1\ \text{in} = 25.4\ \text{mm}$ exactly; 1 ksi $\approx$ 6.9 MPa; 1 MPa $\approx$ 145 psi.
- Shaft torque units: entering $T$ in $\text{N}\cdot\text{m}$ where $\text{N}\cdot\text{mm}$ is required makes $d$ about ten times too small, because $d \propto T^{1/3}$ and a factor 1000 in $T$ is a factor 10 in $d$.
- Bearing life: doubling the load gives one eighth the life (ball).
- Stack-up: the RSS value is always below the worst-case value for the same tolerances.
- Position: the deviation is always the diameter (twice the radial offset), never the radius.
- Gear ratio times speed equals input speed; module times teeth equals pitch diameter.
- Spring rate scales with $d^4$ and inversely with $D^3$: doubling $d$ multiplies $k$ by 16.
- Gravity: a 1 kg mass weighs about 9.8 N on Earth. Other bodies scale with their local $g$.

## Further reference

Named references only. None has a URL in this sheet. Look up the current edition.

- Shigley's Mechanical Engineering Design (paid): static and fatigue failure, shafts, gears, springs, fasteners, bearings.
- Roark's Formulas for Stress and Strain (paid): beam and plate formulas.
- Peterson's Stress Concentration Factors (paid): $K_t$ charts by geometry.
- Machinery's Handbook (paid): tolerances, threads, fits, and standard sizes.
- ASME Y14.5, Dimensioning and Tolerancing (paid): GD&T symbols, datums, modifiers.
- ISO 1101, Geometrical product specifications (GPS): geometric tolerancing (paid).
- ISO 286, ISO code system for tolerances on linear sizes (paid): fit grades and limits.
- ISO 898-1, Mechanical properties of fasteners, carbon steel and alloy steel (paid): bolt grades and proof strength.
- Boothroyd, Dewhurst, and Knight, Product Design for Manufacture and Assembly (paid): DFMA method.
- NIST SP 811, Guide for the Use of the International System of Units (name only; check the NIST publication list for the current copy).
