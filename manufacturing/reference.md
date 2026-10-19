# manufacturing reference

**Type:** reference

Lookup sheet for the working engineer who needs a formula, a typical value, a rule with its limit, or a checklist mid-job. It assumes the lessons in this folder are known.

## Principles

- Geometry is made by removing, adding, or deforming material. Every process leaves its own error, and that error is a distribution, not a single number.
- Forces, heat, and deflection follow the cut or the pressure. Fix the physics first, then pick the speed.
- Every material shrinks, springs back, or distorts when it cools, unloads, or is heated. Allow for it in the pattern, die, or program.
- A process has a rate, a fixed cost, and a per-part cost. Choose the process by volume first, then by geometry.
- Capability is designed in and monitored. It cannot be inspected into a part after the fact.
- Sharp corners concentrate stress and flow. Use radii wherever the function allows.
- A measurement has its own uncertainty. A gauge should resolve a fraction of the tolerance it checks (a common rule is about one tenth).
- Hazards are removed by design first, then guarded, then warned about, and only then covered by personal protective equipment.
- Starting values from a tool maker, a handbook, or a supplier are starting points. The sound, the chip, and the finish decide the final value.

## Process selection

| Process | Typical materials | Typical tolerance (typical) | Typical Ra, um (typical) | Economic batch (typical) |
|---|---|---|---|---|
| CNC turning | metals, plastics | $\pm$ 0.025 mm | 0.8 to 3.2 | one-off to medium |
| CNC milling | metals, plastics | $\pm$ 0.025 mm | 0.8 to 3.2 | one-off to medium |
| Precision grinding | hardened steel, carbide, ceramics | $\pm$ 0.005 mm | 0.2 to 0.8 | small to high |
| Sand casting | iron, steel, aluminum, bronze | $\pm$ 0.5 to 1.5 mm on small castings | 6.3 to 25 | small |
| Investment casting | steel, nickel alloys, aluminum, titanium | $\pm$ 0.1 mm on first 25 mm | 1.6 to 3.2 | small to medium |
| Die casting | aluminum, zinc, magnesium | $\pm$ 0.1 mm | not quoted here | high |
| Injection molding | thermoplastics | $\pm$ 0.05 to 0.1 mm on small features | 0.05 to 1.6 (set by mold finish) | high (about 5,000+) |
| Closed-die forging | steel, aluminum, titanium | $\pm$ 0.25 to 0.5 mm | not quoted here | medium to high |
| Sheet metal laser cut | steel, aluminum, stainless | $\pm$ 0.1 mm | not quoted here | one-off to medium |
| Sheet metal stamping | steel, aluminum, copper alloys | $\pm$ 0.1 mm | not quoted here | high |
| Fused deposition (FDM) | thermoplastics | $\pm$ 0.2 to 0.5 mm | not quoted; layer lines visible | one-off to small |

- Batch bands are coarse on purpose. Tooling cost, setup time, and cycle time set the real break-even point.
- **Holds when:** the part is within the process envelope for size and feature. **Breaks when:** the feature is smaller than the process resolves, or the tolerance is tighter than the process holds without a secondary operation.

## Machining: speeds and feeds

### Formulas

Units: $N$ spindle speed (rev/min). $V$ surface speed (ft/min, SFM, in US form; m/min in SI). $D$ tool or workpiece diameter (in US form; mm in SI). $f_z$ feed per tooth (in/tooth or mm/tooth). $z$ number of teeth (flutes). $f_m$ feed rate (ipm or mm/min). $a_p$ axial depth of cut. $a_e$ radial width of cut. The same length unit must be used throughout a calculation.

Spindle speed from surface speed:

$$N = \frac{V_{\text{US}}}{\pi D/12} \approx \frac{3.82\,V_{\text{SFM}}}{D_{\text{in}}}$$

$$N = \frac{1000\,V_{\text{m/min}}}{\pi D_{\text{mm}}}$$

Feed rate and chip load:

$$f_m = f_z\, z\, N \qquad f_z = \frac{f_m}{z\,N}$$

Milling material removal rate:

$$\text{MRR} = a_p\, a_e\, f_m$$

Turning material removal rate, where $f$ is feed per revolution (mm/rev) and $V$ is surface speed in mm/min:

$$\text{MRR} = a_p\, f\, V$$

Cutting power from specific cutting energy $k_c$ (J/mm$^3$; note that 1 J/mm$^3$ equals 1000 N/mm$^2$):

$$P_c = k_c\, \text{MRR}$$

Units: $P_c$ in W when MRR is in mm$^3$/s. Motor input power is $P_c/\eta$, with $\eta$ the drive efficiency, typically 0.7 to 0.9 (typical).

### Specific cutting energy (typical, broad)

| Work material | $k_c$ (J/mm$^3$, typical) |
|---|---|
| Aluminum (wrought) | 0.5 to 1.0 |
| Cast iron | 1.0 to 1.5 |
| Mild steel | 1.8 to 3.0 |
| Stainless steel | 2.5 to 3.5 |

- $k_c$ falls as chip thickness rises. Use the value for the actual chip thickness, not the nominal feed alone.
- **Holds when:** the cut is steady and the chip is formed in the normal way. **Breaks when:** the tool is dull, the edge is chipped, or the cut is interrupted and the load swings.

### Surface speed bands (typical, broad)

Starting bands for turning only. Drilling and milling often run lower. Tool supplier data governs. These are not design rules.

| Work material | HSS, m/min (SFM) | Carbide, m/min (SFM) |
|---|---|---|
| Aluminum (e.g. 6061) | 60 to 150 (200 to 490) | 250 to 700 (820 to 2300) |
| Mild steel (e.g. 1018) | 20 to 35 (65 to 115) | 90 to 200 (300 to 650) |
| Stainless (austenitic, e.g. 304, 316) | 12 to 25 (40 to 80) | 60 to 120 (200 to 390) |

- 1 m/min is about 3.28 SFM.
- **Holds when:** the tool is rigid, coolant is adequate, and the work is clamped. **Breaks when:** the machine lacks power or stiffness, or the tool coating is not suited to the material.

### Worked check (from the lesson example, SI)

Full-width slot 10 mm wide, 40 mm long, and 10 mm deep, cut in one pass with a 10 mm, 3-flute end mill in 6061 at $V = 250$ m/min and $f_z = 0.08$ mm/tooth.

- $N = 1000 \times 250 / (\pi \times 10) = 7958$ rpm
- $f_m = 0.08 \times 3 \times 7958 = 1910$ mm/min
- MRR $= 10 \times 10 \times 1910 = 191{,}000$ mm$^3$/min $= 3183$ mm$^3$/s
- $P_c \approx 0.7 \times 3183 \approx 2.2$ kW at $k_c = 0.7$ J/mm$^3$ (typical aluminum), before drive losses

### Rules of thumb

- Start at the supplier value, then reduce feed first if the tool chatters, and reduce speed first if the tool wears fast. Basis: heat wears the edge, and chatter comes from feed-driven load. Limit: the machine's rigidity sets the real ceiling.
- Start the first run at about half the feed and override up only after the first pass looks clean. Basis: a first run exposes program and offset errors. Limit: very low feed rubs and work-hardens some materials, so do not go too far.

### Holds when / breaks when

- **Holds when:** the cutter is sharp, the work and tool are rigid, and coolant or chip evacuation is adequate.
- **Breaks when:** interrupted cuts, long overhang, thin walls, or chip recutting raise the load beyond what the formulas assume.

## Drilling

- Spindle speed uses the same surface speed formula, with $D$ the drill diameter.
- Feed per revolution $f_r$ (mm/rev) gives feed rate $f_m = f_r N$.
- Point angle: 118 degrees is the general-purpose standard for steel. A 135 degree split point needs less thrust and resists walking, and is common for harder work. A 140 degree point is common for stainless (typical practice).
- Point depth (cone contribution to hole depth): $h_{\text{cone}} = \dfrac{D/2}{\tan(\theta/2)}$. For 118 degrees, $h_{\text{cone}} \approx 0.30\,D$. For 135 degrees, $h_{\text{cone}} \approx 0.21\,D$.
- Peck depth (rule of thumb): start with a first peck near one diameter in steel, then shorten the pecks as the hole deepens. Retract fully to clear chips at each peck. Basis: chip evacuation limits depth before the flutes pack. Limit: material, coolant, and machine rigidity set the real value. Use supplier peck tables for the job.
- Deep holes (rule of thumb): above about 3 to 5 diameters, expect pecking, through-coolant, or a special tool. Basis: chips must clear the flutes.
- **Holds when:** the drill is sharp, centered, and the hole is through or fully clear of chips. **Breaks when:** the drill walks on a sloped or curved surface (use a spot drill or center drill first), or the hole is blind and the cone is ignored in depth.
- Drilled holes are rough and oversize compared with a reamed hole. A bore or a reamer is needed for tight fits (see tolerances section).

## Turning and milling notes

### Turning

- Surface finish from feed and nose radius (ideal peak height): $R_{\max} = \dfrac{f^2}{8r}$ with $f$ and $r$ in mm, and $R_{\max}$ in mm. Multiply by 1000 for micrometers. Real surfaces are rougher from wear, vibration, and built-up edge.
- Larger nose radius gives a smoother ideal finish but raises the risk of chatter. Basis: the same formula holds up to the point where the contact length shortens the chip.
- Constant surface speed (CSS) mode raises RPM as diameter falls. Use it on facing and taper work. Basis: keeps $V$ constant in the formulas above. Limit: the spindle's maximum RPM caps it at small diameters.
- **Holds when:** the workpiece is well supported and the tool is rigid. **Breaks when:** long slender parts deflect under cut, which is a geometry problem, not a speed problem.

### Milling

- Full slot (radial engagement equal to diameter): chip thickness equals feed per tooth. Full-width cuts load the cutter hardest.
- Partial radial engagement thins the chip, so feed per tooth can be raised for the same chip thickness. Basis: chip thickness, not nominal feed, drives the load. Limit: a thin chip can rub and wear the edge, so keep the chip above the minimum the tool supplier lists.
- Climb milling (cutter teeth move with the feed) usually gives a better finish and lower heat. It needs a rigid machine and a backlash-free table. Conventional milling (teeth move against the feed) suits older or loose machines.
- **Holds when:** the cutter is sharp, the engagement is steady, and the work is clamped. **Breaks when:** the cut is interrupted or the cutter overhang is long, which causes chatter.

## Casting, forming, and molding

### Shrinkage allowance

$$L_{\text{pattern}} = L_{\text{part}}\,(1 + s)$$

Units: lengths in the same unit. $s$ is the linear shrink fraction (dimensionless). For aluminum castings, $s \approx 0.013$ is a typical starting value (1.3 percent). Use the alloy supplier's or casting handbook's value for the actual job.

- **Holds when:** the solidification is uniform and the part is not machined in the same step. **Breaks when:** thick and thin sections cool at different rates, or the gating causes distortion. Use a pattern with separate allowances or a trial casting.

### Injection molding design rules (typical)

| Feature | Rule | Basis and limit |
|---|---|---|
| Nominal wall | uniform, about 1.5 to 3.5 mm for common thermoplastics (typical) | Keep variation within about 20 to 25 percent. Thick sections sink and warp. |
| Draft | about 1 degree per side is common; 0.5 degree minimum on polished surfaces | Textured surfaces need more. Limit: draft adds material and can conflict with tight fits. |
| Ribs | thickness 50 to 60 percent of nominal wall; height up to about 3 times the wall | Basis: thick rib base causes sink marks on the cosmetic face. Limit: deep ribs need draft and can trap the part. |
| Rib base fillet | radius about 0.25 to 0.5 times the wall | Reduces stress at the root. |
| Boss | outside diameter about 2 times the hole diameter; tie to the wall with ribs | Basis: thick boss sinks. Limit: depends on resin and screw-boss strength needed. |
| Inside corner | radius at least 0.5 times the wall | Reduces stress and improves flow. |
| Outside corner | inside radius plus the wall thickness | Keeps the wall uniform around the corner. |

- The parting line sets draft direction. Undercuts need side action or a slide, which raises tooling cost.
- **Holds when:** the resin flows through the cavity at the designed pressure and the mold is cooled uniformly. **Breaks when:** wall variation is large, or thick sections are used for strength instead of ribs.

## Additive manufacturing

### Layer count

$$n = \frac{h}{t}$$

Units: $h$ and $t$ in the same unit (mm). $n$ is a count. Halving $t$ doubles $n$, and layer-driven build time rises roughly in step.

- Typical polymer layer heights are 0.05 to 0.3 mm. Finer layers look smoother and take longer.

### Design rules (typical, process dependent)

| Feature | Rule | Basis and limit |
|---|---|---|
| Overhang (FDM) | self-supporting up to about 45 degrees from vertical | Beyond 45 degrees, add support or reorient. Limit: material and cooling change the real angle. |
| Minimum wall (FDM) | at least two perimeters, about 0.8 to 1.2 mm with a 0.4 mm nozzle | Thinner walls may not print or may break in handling. Confirm with the service bureau. |
| Holes | vertical holes are round; horizontal holes need a teardrop or diamond profile | Basis: horizontal round holes sag at the roof. Limit: check with a test print. |
| Clearance (moving parts) | add clearance per side and verify with a test print | Printed size differs from the model. Limit: depends on printer, resin or filament, and orientation. |
| Orientation | load along the layers, not across them | Layer bonds are the weak path in most processes. |

- Anisotropy: strength across layers is often materially lower than along layers. Do not assume isotropic strength. Test coupons in the actual build direction.
- Support and powder removal: leave access for both. A trapped support or powder is a rework or scrap risk.
- **Holds when:** the part is oriented, supported, and designed for the process. **Breaks when:** the load crosses layers, or thin features are used at the process limit.

## Joining: welding

### Joint types

- Butt, lap, T, corner, and edge joints. The fillet weld is used on lap, T, and corner joints. Groove welds are used for butt and T joints when full penetration is required.
- Positions: flat, horizontal, vertical, overhead. Position changes process settings and skill needs.

### Weld symbol anatomy (in words, AWS A2.4 style)

- The reference line is horizontal. Everything else hangs from it.
- The arrow runs from one end of the reference line to the joint. The arrow side is the side of the joint the arrow points to.
- The weld symbol sits on the reference line. Its position above or below the line says which side of the joint gets the weld (arrow side or other side).
- Dimensions go next to the symbol: size to its left, length to its right, pitch after the length.
- A flag at the arrow end of the reference line means field weld. A circle at the arrow and reference junction means all-around.
- Tail (optional): process, notes, or a reference.

### Fillet weld throat and strength

Throat of a 45 degree fillet with leg length $a$:

$$t = 0.707\,a$$

Units: $a$ and $t$ in the same unit. $0.707 = \sqrt{2}/2$.

Shear capacity of a fillet weld of length $L$ with allowable shear stress $\tau_{\text{allow}}$ on the throat:

$$F = \tau_{\text{allow}}\; 0.707\,a\, L$$

Units: $F$ in N when $\tau_{\text{allow}}$ is in N/mm$^2$ and $a$, $L$ in mm. Take $\tau_{\text{allow}}$ from the governing code (for example AWS D1.1 for steel structures, or AISC 360) for the electrode and base metal. Do not use a value from memory for a load-bearing joint.

- **Holds when:** the load is static, fusion is complete, and the weld is sized by its throat. **Breaks when:** the joint sees fatigue, the heat-affected zone is weakened, or there is undercut, porosity, or lack of fusion.
- Sanity: throat is always less than the leg. A leg of 6 mm gives a throat of about 4.24 mm.

### Process overview (typical)

- MIG (GMAW): wire fed, fast, good for production. TIG (GTAW): tungsten electrode, clean, slow, for thin or critical work. Stick (SMAW): simple, portable, rougher. Heat-affected zone exists for all of them.

## Sheet metal

### Bend allowance

$$\text{BA} = \theta\,\frac{\pi}{180}\,(R + K\,T)$$

Units: $\theta$ in degrees. $R$ and $T$ in the same unit. $K$ dimensionless, between 0 and 1. Typical air-bending $K$ is about 0.3 to 0.5 (typical); use the shop or die chart.

### Bend deduction and flat length

Outside setback $\mathrm{OSSB} = (R + T)\tan(\theta/2)$ for each bend, so

$$\text{BD} = 2\,(R + T)\tan\!\left(\frac{\theta}{2}\right) - \text{BA}$$

$$L_{\text{flat}} = \sum L_{\text{outside flanges}} - \text{BD}$$

- Worked check ($R = 3$ mm, $T = 2$ mm, $\theta = 90$ degrees, $K = 0.33$): $\text{BA} = 5.749$ mm, $\text{BD} = 4.251$ mm.
- **Holds when:** air bending with consistent tooling and material. **Breaks when:** bottom bending, coining, or a different grain direction changes $K$. Use a measured sample.

### Minimum bend radius (rule of thumb)

- Keep the inside radius at about one material thickness or more for ductile sheet, and larger for harder tempers. Basis: the outside fibers stretch and crack when strain exceeds ductility. Limit: temper, grain direction, and alloy set the real value. Confirm with the supplier's bend table.
- Bend across the grain where practical. Bending along the grain is more likely to crack on many alloys.
- Springback: the part opens after the load is released. Overbend to compensate. The amount depends on material and radius.

### Hole and cut distances (common shop guidelines)

- Hole edge to sheet edge: at least about 2 times the thickness. Basis: keeps the edge from tearing or distorting during forming and punching.
- Hole edge to bend tangent line: at least about $2.5\,T + R$. Basis: keeps the hole from distorting in the bend zone. Limit: a fabricator's capability may be tighter or looser; use its guidelines.
- Keep bends the same direction and radius where practical to cut setups. Changing tools costs time.

## Tolerances, fits, and finish

### Limits and fits

- Clearance (hole upper limit minus shaft lower limit, maximum): $C_{\max} = D_{\max} - d_{\min}$.
- Minimum clearance (hole lower limit minus shaft upper limit): $C_{\min} = D_{\min} - d_{\max}$. Negative means interference.
- Worked check (from the lesson): hole 25.000 to 25.021 mm, shaft 24.980 to 24.993 mm. $C_{\max} = 0.041$ mm, $C_{\min} = 0.007$ mm. Clearance fit.
- Specify the fit type with the sizes, not the sizes alone. Name the fit class (ISO hole and shaft letters and numbers) and check the full table.

### Stack-up

- Worst case: $T_{\text{worst}} = \sum t_i$. Holds when every part must fit regardless of luck.
- Root-sum-square: $T_{\text{RSS}} = \sqrt{\sum t_i^2}$. Holds when the errors are independent, random, and centered. Breaks when the process is biased or drifting.
- Worked check: three tolerances of 0.05, 0.05, and 0.10 mm give worst case 0.20 mm and RSS 0.122 mm.

### General tolerances (ISO 2768-m, typical linear limits, plus or minus)

| Nominal range (mm) | Limit (mm) |
|---|---|
| 0.5 to 3 | 0.1 |
| 3 to 6 | 0.1 |
| 6 to 30 | 0.2 |
| 30 to 120 | 0.3 |
| 120 to 400 | 0.5 |
| 400 to 1000 | 0.8 |

- Use general tolerances on non-critical features. Tighter tolerances cost inspection and process time.

### Surface roughness

- Ra is the arithmetic average deviation from the mean line, in um. Rz is the average of the largest peaks and valleys over a sample length. Both are maximum limits on the drawing. A surface rougher than the specified maximum Ra or Rz is nonconforming. Rougher surfaces come from worse process or tool wear, so check against the limit.
- Typical Ra by process: see the process selection table.
- **Holds when:** the surface is measured over the sample length the standard requires. **Breaks when:** the reading is taken parallel to the lay (which understates roughness; measure across the lay) or on a damaged area.

## Statistical process control

- Process capability (short-term, when $\sigma$ is estimated from within-subgroup variation):

$$C_p = \frac{\text{USL} - \text{LSL}}{6\sigma} \qquad C_{\text{pk}} = \frac{\min(\text{USL} - \mu,\; \mu - \text{LSL})}{3\sigma}$$

Units: all in the same unit. $\mu$ is the process mean and $\sigma$ the process standard deviation. $\text{USL}$ and $\text{LSL}$ are the upper and lower spec limits.

- $C_p$ ignores centering. $C_{\text{pk}}$ includes centering and is the one to report with the process mean.
- Worked check: $\text{USL} = 10.5$, $\text{LSL} = 9.5$, $\mu = 10.1$, $\sigma = 0.1$ gives $C_p = 1.67$, $C_{\text{pk}} = 1.33$.
- Typical acceptance thresholds: $C_{\text{pk}} \ge 1.33$ for an existing process; $\ge 1.67$ for critical characteristics; $\ge 2.0$ for six sigma-level performance. These are commonly used industry targets, not universal law.
- **Holds when:** the process is stable (in control) and the data are close to normal. **Breaks when:** the process drifts, has a bimodal distribution, or the $\sigma$ estimate is from too few samples.

### Control charts

- X-bar chart center line: $\bar{\bar{X}}$, the grand mean of subgroup means. Limits: $\bar{\bar{X}} \pm 3\,\sigma/\sqrt{n}$, where $n$ is subgroup size.
- Worked check: $\sigma = 0.1$, $n = 5$ gives limits of $\pm 0.134$ about the center line.
- Typical subgroup size: 3 to 5. Typical number of subgroups to set limits: about 20 to 25 (typical practice).
- Points beyond the limits, or runs of 7 on one side of the center line, signal special cause (common rule set; check the rule set your standard uses).
- **Holds when:** samples are rational subgroups taken in order. **Breaks when:** subgroups mix shifts or lots, or the process is non-normal.

### Six sigma (meaning)

- Six sigma is a process whose spec limits sit six standard deviations from the mean. The commonly quoted 3.4 defects per million opportunities (DPMO) assumes a 1.5 sigma long-term drift in the mean, which leaves 4.5 sigma on the near side.
- Check: $\text{DPMO} = 10^6 \times P(Z > 4.5) \approx 3.4$.
- Breaks when: the defect rate is measured without counting every opportunity, or the drift assumption is not valid for the process.

## Lean and automation

### OEE

$$\text{OEE} = A \times P \times Q$$

- $A = \dfrac{\text{run time}}{\text{planned time}}$, $P = \dfrac{\text{actual output}}{\text{ideal output}}$, $Q = \dfrac{\text{good parts}}{\text{total parts}}$. Each ratio is between 0 and 1.
- Worked check (lesson): $A = 0.90$, $P = 0.85$, $Q = 0.98$ gives OEE $= 0.750$.
- A commonly quoted benchmark for discrete manufacturing is 85 percent (typical, not a law).
- **Holds when:** the ideal rate is a proven best speed, and time is measured the same way. **Breaks when:** the ideal rate is a theoretical number, which makes $P$ look artificially low.

### Takt time and cycle time

$$\text{Takt} = \frac{\text{available time}}{\text{customer demand}}$$

- Worked check: 7.2 h of available time (25,920 s) and 240 parts per day gives takt $= 108$ s.
- A line is balanced when every station's cycle time is at or below takt.
- Little's Law (any stable system): $\text{WIP} = \text{throughput} \times \text{lead time}$. Use it to check inventory and lead-time claims.

### Automation

- Accuracy is closeness to target. Repeatability is closeness across repeats. A robot can repeat well and still be off target (lesson worked case: 0.02 mm repeatability, 0.3 mm offset).
- Payload is the mass at the tool flange, and it includes the tool and the part.
- Safety: a cobot's speed and force limits reduce risk but do not remove the need for a risk assessment. Fixed guards and light curtains are the usual tools for other cells.
- **Holds when:** the task is repeatable and the sensors confirm each step. **Breaks when:** the part presentation changes, or there is no fault state for jams and missing parts.

## Checklists

Before trusting a machining program:

- Tool diameter, length, and flute count match the program.
- Work offset is set and checked on each axis.
- Dry run done with the spindle off or in a simulator, with the tool path watched.
- Feed override starts low and is raised only after a clean first pass.
- First part measured before a batch.

Before releasing a sheet metal part:

- Flat length includes bend deduction or allowance for every bend.
- Hole positions respect the edge and bend-tangent guidelines.
- Bend radius is at or above the supplier's minimum for the material and temper.

Before releasing a molded part:

- Wall is uniform, and draft is on every vertical face.
- Ribs and bosses are at the wall-ratio rules.
- Parting line does not cross a cosmetic or sealing face.

Before releasing a welded joint:

- Weld symbol shows type, size (the fillet leg; strength is checked on the throat, 0.707 times the leg), length, pitch, and side.
- Fillet strength is checked against the governing code value.
- Heat-affected zone is considered in the load path.
- Inspection method is named (visual, dye penetrant, ultrasonic).

Before trusting a capability claim:

- Process is in control on a control chart.
- Compute $C_{\text{pk}}$ with the process mean. $C_p$ alone does not show centering.
- Sample size and subgrouping are stated.

## Sanity checks

- Spindle speed: at 300 SFM, a $1/2$ in cutter should run near 2300 rpm. A 10 mm tool at 90 m/min runs near 2900 rpm.
- Feed rate: feed rate is $f_z \times z \times N$. Double the flutes doubles the feed rate at the same chip load.
- MRR: a 10 mm by 10 mm pass at 1900 mm/min removes about 190,000 mm$^3$/min. If the answer is off by 1000, check the units.
- Cutting power: MRR in mm$^3$/s times $k_c$ in J/mm$^3$ gives W. A few kW for a modest slot in aluminum is plausible; tens of kW for a small end mill is not.
- Drill cone: depth of a 118 degree point is about 0.3 times the diameter. A 10 mm drill's point adds about 3 mm.
- Bend allowance: the arc length of a 90 degree bend is about 1.57 times the radius to the neutral axis. Check that $\text{BA}$ is less than the outside arc.
- Fillet throat: must be less than the leg. $0.707 \times$ leg is the right order of magnitude.
- Shrink: a 200 mm casting length adds about 2.6 mm to the pattern at 1.3 percent. A tolerance smaller than the shrink is a red flag.
- $C_{\text{pk}}$: $C_{\text{pk}} \le C_p$ always. Equality holds only when the mean sits exactly at the spec center. A $C_{\text{pk}}$ above $C_p$ means a calculation error.
- Stack-up: RSS total is always less than or equal to the worst-case total for the same tolerances.
- Layer count: a 40 mm part at 0.2 mm has 200 layers. At 0.1 mm it has 400.
- OEE: the product must be smaller than the smallest of its three factors.
- Takt: if cycle time is above takt, the line falls behind demand.

## Further reference

- Machinery's Handbook (Industrial Press). Machining data, tolerances, fits, and formulas. Paid, by name only.
- Kalpakjian and Schmid, Manufacturing Engineering and Technology (Pearson). Broad process and design textbook. Paid, by name only.
- DeGarmo, Black, and Kohser, Materials and Processes in Manufacturing (Wiley). Process selection and material behavior. Paid, by name only.
- Groover, Fundamentals of Modern Manufacturing (Wiley). Processes and automation. Paid, by name only.
- ASME Y14.5, Dimensioning and Tolerancing (geometric dimensioning and tolerancing). Standard, paid, by name only.
- ISO 286, ISO code system for tolerances on linear sizes (limits and fits). Standard, paid, by name only.
- ISO 2768, General tolerances for linear and angular dimensions. Standard, paid, by name only.
- ISO 1302, Indication of surface texture in technical product documentation. Standard, paid, by name only.
- ISO 2553, Welded, brazed and soldered joints, symbolic representation on drawings. Standard, paid, by name only.
- AWS A2.4, Standard Symbols for Welding, Brazing, and Nondestructive Examination. Standard, paid, by name only.
- AWS D1.1, Structural Welding Code, Steel. Standard, paid, by name only.
- AISC 360, Specification for Structural Steel Buildings. Standard, paid, by name only.
- Montgomery, Introduction to Statistical Quality Control (Wiley). SPC and capability. Paid, by name only.
- Womack and Jones, Lean Thinking (Free Press). Lean principles. Paid, by name only.
- Shingo, A Study of the Toyota Production System (Productivity Press). Lean and setup reduction. Paid, by name only.
