# Reverse-engineering reference

**Type:** reference

A lookup sheet for engineers taking a part apart and rebuilding it: thread and fastener identification, material and process clues, typical densities, nominal-size inference, measurement order, and the checks that keep the work lawful and safe.

## Principles

- Measure before you assume. A number you did not measure is a guess, and a guess needs a label.
- Two independent clues that agree beat one clue that looks convincing.
- A worn part shows its present size, not its designed size. Find an unworn surface before you choose a nominal value.
- Units are a source of error. Convert to one system first, then calculate, then convert back only for display.
- Matching appearance is not matching performance. Strength, hardness, and fatigue life need tests.
- Keep the evidence. A photo, a logged measurement, or a mass check outlives memory.
- A rebuilt part that carries a load or protects a person needs engineering verification before anyone relies on it.
- Ownership of a product does not transfer the right to copy its design.

## Thread identification

### ISO metric coarse threads (typical, ISO 261 and ISO 262 coarse series)

Designation $M d \times p$, where $d$ is the nominal major diameter in millimeters and $p$ is the pitch in millimeters. Coarse pitch is the default when only the size is given.

| Size | Pitch $p$ (mm) | Size | Pitch $p$ (mm) |
|------|----------------|------|----------------|
| M2 | 0.40 | M12 | 1.75 |
| M2.5 | 0.45 | M14 | 2.00 |
| M3 | 0.50 | M16 | 2.00 |
| M4 | 0.70 | M18 | 2.50 |
| M5 | 0.80 | M20 | 2.50 |
| M6 | 1.00 | M22 | 2.50 |
| M8 | 1.25 | M24 | 3.00 |
| M10 | 1.50 | | |

- Fine-pitch metric threads (for example M8 x 1.0) exist. Read the designation; a bare "M8" means coarse.
- Holds when: the thread is standard and undamaged. Breaks when: the part has a custom or rolled thread, or the thread is badly worn or mis-chased.

### UNC threads (Unified National Coarse, typical)

Designation $n\text{-}TPI$ for numbered sizes or $f\text{-}TPI$ for fractional sizes, where TPI is threads per inch. Pitch in millimeters is:

$$p_{\text{mm}} = \frac{25.4}{\text{TPI}}$$

| Size | TPI | Pitch (mm) | Major diameter (in) | Major diameter (mm) |
|------|-----|-----------|---------------------|---------------------|
| #4 | 40 | 0.635 | 0.112 | 2.845 |
| #5 | 40 | 0.635 | 0.125 | 3.175 |
| #6 | 32 | 0.794 | 0.138 | 3.505 |
| #8 | 32 | 0.794 | 0.164 | 4.166 |
| #10 | 24 | 1.058 | 0.190 | 4.826 |
| #12 | 24 | 1.058 | 0.216 | 5.486 |
| 1/4 | 20 | 1.270 | 0.250 | 6.350 |
| 5/16 | 18 | 1.411 | 0.3125 | 7.938 |
| 3/8 | 16 | 1.588 | 0.375 | 9.525 |
| 7/16 | 14 | 1.814 | 0.4375 | 11.112 |
| 1/2 | 13 | 1.954 | 0.500 | 12.700 |
| 9/16 | 12 | 2.117 | 0.5625 | 14.288 |
| 5/8 | 11 | 2.309 | 0.625 | 15.875 |
| 3/4 | 10 | 2.540 | 0.750 | 19.050 |
| 7/8 | 9 | 2.822 | 0.875 | 22.225 |
| 1 | 8 | 3.175 | 1.000 | 25.400 |

- Holds when: the thread is coarse and standard. Breaks when: the thread is fine (UNF), or the part uses a non-standard form.
- Same-pitch pairs (for example #4-40 and #5-40) are told apart only by major diameter.

### Metric or inch: how to tell

- Measure the outside major diameter across the crests with a caliper or micrometer, at a clean, unworn section.
- Compare with the tables above. Metric major diameters are close to whole millimeters (6.00, 8.00). Inch major diameters are close to 0.0625 in steps and convert to 6.35, 7.94, 9.53 mm and so on.
- Use a pitch gauge with blades marked in TPI and in mm. Match the blade to the crests with no visible gap. The blade is the better test for pitch; the diameter is the better test for system.
- Watch for conflicts. M8 x 1.25 and 1/4-20 UNC both have a pitch near 1.25 to 1.27 mm. The major diameter (8.00 mm against 6.35 mm) separates them easily.
- Holds when: the thread is not plated, stripped, or heavily corroded. Breaks when: the thread is damaged, or the measured major diameter is near a size where wear could mislead you. Use two readings from different crests.
- Lead for multi-start threads: $L = n_s \, p$, where $L$ is lead in millimeters, $n_s$ is the number of starts, and $p$ is pitch in millimeters. Pitch counting on a multi-start thread gives the wrong pitch unless you use lead.

Thread form: ISO metric and UN threads both use a 60 degree flank angle, so the angle alone does not identify the system.

### Thread pitch by turn counting

$$p = \frac{L}{N}$$

where $p$ is pitch in millimeters, $L$ is the measured length in millimeters, and $N$ is the number of crest intervals counted within $L$.

- Holds when: the measured length is at least several pitches long and the thread is single-start. Breaks when: the length is only one or two pitches (counting error dominates).

## Fastener heads and drives

### Head types

| Head | Typical use | Identification |
|------|-------------|----------------|
| Pan | General assembly, rounded low profile | Domed top, straight vertical sides, flat underside |
| Round | Similar to pan, slightly higher | Fully rounded top |
| Truss | Low, wide head to cover large holes | Very shallow dome, wide flat bearing |
| Flat (countersunk) | Flush mount in a countersink | Conical underside; included angle is typically 82 degrees (inch) or 90 degrees (metric) |
| Button | Low profile, rounded edges | Short, wide dome |
| Hex (external) | High torque, wrench drive | Six flats outside |
| Socket cap | Recessed in counterbore | Cylindrical head with hex socket |
| Set screw (grub) | Locks one part onto a shaft | No head; hex or slot in the end |
| Flange | Built-in washer face | Wide annular flange under head |
| Carriage bolt | Square neck resists turning | Dome head, square shoulder under head |

### Drive types

| Drive | Identification | Notes |
|-------|----------------|-------|
| Slotted | Single straight slot | Prone to cam-out; common in older equipment |
| Phillips (PH) | Cross with conical center | Cams out by design under high torque |
| Pozidriv (PZ) | Cross with four small radial marks at 45 degrees | Less cam-out than Phillips; the two are not interchangeable |
| Hex socket (Allen) | Hexagonal recess | Use a hex key of matching size |
| Torx (T) | Six-lobed star | Common in automotive and electronics; sizes T5 to T60 are typical |
| Torx Plus (IP) | Star with rounded lobes | Not interchangeable with Torx |
| Square (Robertson, R) | Square recess with taper | Common in some North American trades |
| Security Torx | Torx recess with center pin | Needs a pinned driver |
| Tri-wing | Three-point recess | Common in consumer electronics |

- Holds when: the drive is undamaged. Breaks when: a previous user has damaged the recess; the recess then looks like a different drive.
- Test by trying the smallest candidate drive first. Forcing a driver into a damaged recess destroys evidence.

## Material identification

### Quick bench tests

| Test | Result | What it suggests |
|------|--------|------------------|
| Magnet | Strong pull | Ferromagnetic: carbon and low-alloy steel, most cast iron, many 400-series stainless |
| Magnet | Weak or no pull | Non-ferromagnetic: aluminum, copper, brass, bronze, most 300-series stainless, most plastics |
| Magnet | Slight pull on stainless | Cold-worked 300-series stainless can show weak attraction; not proof of carbon steel |
| Density (water displacement) | Matches a row in the density table | Narrows the family; see density table |
| Spark test (grinder, eye protection and guard) | Long straight streams with small forked bursts | Carbon or low-alloy steel |
| Spark test | Short, dull-red sparks with few forks | Cast iron (high carbon, graphite) |
| Spark test | Short sparks, little or no fork | Stainless steel, depending on grade |
| Spark test | No useful spark stream | Aluminum, copper, brass, bronze |
| File test | File bites easily and leaves bright metal | Soft material: aluminum, brass, copper, lead, zinc alloy |
| File test | File skates or will not cut | Hard material: hardened steel, hard stainless |
| Scratch test on a hidden face | Bright silver, gray, or colored core | Shows base metal under paint, plating, or anodizing |
| Appearance of a cut edge | Dark gray with graphite flecks | Cast iron |
| Appearance of a cut edge | Bright, even grain, light color | Aluminum or zinc alloy |
| Appearance of a cut edge | Bright red-gold | Copper or brass |

- Holds when: the sample is a clean, uncoated, hidden face or a cut edge. Breaks when: plating, paint, anodizing, or heat tint hides the base metal.
- Spark and magnet tests sort families only. They cannot give a grade, a temper, or a heat treatment.

### Plastics: flame and float (typical, use a fume hood or open air, small sample, no PVC nearby)

| Plastic | Flame behavior | Smell | Density (g/cm$^3$, typical) | Floats in water? |
|---------|----------------|-------|------------------------------|------------------|
| PE (HDPE, LDPE) | Melts, drips, keeps burning, blue base | Candle or paraffin | 0.92 to 0.97 | Yes |
| PP | Melts, drips, blue base | Candle or paraffin | 0.90 | Yes |
| PS | Sooty yellow flame | Sweet styrene | 1.04 to 1.05 | No |
| ABS | Sooty, black smoke | Styrene | 1.04 to 1.06 | No |
| PC | Yellow, sooty, slow, bubbles | Sweetish | 1.20 | No |
| PMMA (acrylic) | Clear blue flame, crackles | Fruity or acrid | 1.18 | No |
| PA (nylon) | Drips, self-extinguishes slowly | Burnt hair or feathers | 1.13 to 1.15 | No |
| POM (acetal) | Blue flame, little soot, drips | Formaldehyde, sharp | 1.41 | No |
| PVC | Hard to ignite, green-edged flame, self-extinguishes | Sharp acid; releases hydrogen chloride | 1.30 to 1.45 | No |
| Thermoset (phenolic, epoxy) | Chars; does not melt | Varies | 1.2 to 1.9 | Varies |

- Caution: PVC and some filled plastics release toxic gas. Stop the test at the first sign of pungent acid smoke. Do not burn PTFE.
- Holds when: the sample is pure and unfilled. Breaks when: fillers (glass, mineral, flame retardant) or colorants change the result.

### Material family from the test results

- Magnetic plus density near 7.85 g/cm$^3$ suggests steel. Density near 7.2 g/cm$^3$ with dark cut edge suggests cast iron.
- Non-magnetic plus density near 2.7 g/cm$^3$ suggests aluminum. Near 8.9 g/cm$^3$ suggests copper or bronze. Near 8.5 g/cm$^3$ suggests brass.
- Non-magnetic plus density near 4.4 g/cm$^3$ suggests titanium alloy.
- Density below 1 g/cm$^3$ and floats suggests PE, PP, or some foamed plastics.

## Process identification

| Clue on the part | Likely process | Notes |
|------------------|----------------|-------|
| Thin seam where two mold halves met | Injection molding, die casting, sand casting | Seam position shows the mold split |
| Small round witness marks on a molded wall | Injection molding | Ejector pins |
| Small stub or scar at one point | Molding or casting | Gate (molding) or riser (casting) |
| Branched runner stub connected to several parts | Injection molding, die casting | Runner system |
| Taper of about 1 to 3 degrees on walls | Molding or casting | Draft for release from the mold |
| Thin fin or flash along the parting line | Molding, forging, die casting | Excess material at the split |
| Sink marks or voids on thick plastic sections | Injection molding | Uneven cooling |
| Gas holes or porosity on a cut section | Casting | Trapped gas or shrinkage |
| Stair-step layer lines along a fixed direction | Additive (fused filament, FDM/FFF) | Layer lines follow the build direction |
| Raised, ripple-patterned bead along a joint | Welding (arc, MIG, TIG) | Melting joins the metal |
| Straight parallel lines on a flat face | Milling, planing, shaping | Cutter path |
| Concentric rings around a round part | Turning on a lathe | Feed marks |
| Fine uniform sheen with random scratches | Grinding | Abrasive finish |
| Regular diamond pattern of ridges | Knurling | Pressed or cut pattern |
| Bright sheared band with rollover on one face | Blanking or punching (sheet) | Burr sits on the die exit side |
| Uniform wall thickness, bend radii, relief notches | Sheet metal forming | Bending and forming |
| Fibrous grain lines in a cut or etched section that follow the shape | Forging | Grain flow |
| Threads with rounded crests and no cut marks | Rolled thread | Stronger than cut thread |
| Recast layer or small craters on a hard surface | EDM (electrical discharge machining) | Spark erosion |
| Ripple or chatter marks at regular spacing | Turning or milling with poor rigidity | Tool vibration |

- Holds when: the surface is unfinished. Breaks when: secondary operations (painting, plating, heat treatment, polishing) remove the clue.
- Two or more clues must agree. One clue alone (for example a parting line on a machined part) is not enough.

## Density of common materials (typical)

Density is $\rho = m / V$ in g/cm$^3$. Values are standard textbook typical values; alloy, filler, and porosity shift them.

| Material | Density (g/cm$^3$) |
|----------|--------------------|
| Lead | 11.3 |
| Copper (pure) | 8.96 |
| Bronze (tin bronze) | 8.8 |
| Brass (typical) | 8.5 |
| Stainless steel (austenitic, e.g. 304) | 8.0 |
| Low-carbon steel | 7.85 |
| Cast iron (gray) | 7.2 |
| Zinc alloy (die cast) | 6.6 |
| Titanium alloy (Ti-6Al-4V) | 4.43 |
| Aluminum (pure) | 2.70 |
| Aluminum alloy (e.g. 6061) | 2.70 |
| Magnesium alloy | 1.74 |
| Glass (soda-lime) | 2.5 |
| Concrete | 2.4 |
| Polytetrafluoroethylene (PTFE) | 2.2 |
| Polyoxymethylene (POM) | 1.41 |
| Polyvinyl chloride, rigid (PVC) | 1.30 to 1.45 |
| Polyamide 6 (PA6, nylon) | 1.13 to 1.15 |
| Polymethyl methacrylate (PMMA) | 1.18 |
| Polycarbonate (PC) | 1.20 |
| Acrylonitrile butadiene styrene (ABS) | 1.04 to 1.06 |
| Polystyrene (PS) | 1.04 to 1.05 |
| Polypropylene (PP) | 0.90 |
| Polyethylene, high density (HDPE) | 0.95 |
| Polyethylene, low density (LDPE) | 0.92 |
| Oak (dry) | 0.75 |

Weight check: $m = \rho V$, with $V$ in cm$^3$ and $\rho$ in g/cm$^3$. Convert mm$^3$ to cm$^3$ by dividing by 1000.

Holds when: the part is solid and homogeneous. Breaks when: the part is porous (castings, sintered parts), hollow, foamed, or contains an inserted part.

## Inferring nominal dimensions from worn parts

### Method

1. Measure the worn feature at several points and directions.
2. Find an unworn reference: a shoulder, a hidden face, a bore that was not in contact, or a mating part.
3. Measure the reference and record the difference from the worn feature.
4. Choose the nominal value from the reference, then round to a standard value.

### Direction of wear

- A worn shaft is smaller than its nominal size. The nominal is at or above the measured diameter.
- A worn bore is larger than its nominal size. The nominal is at or below the measured diameter.
- External thread wear flattens crests and reduces the major diameter. Read the unworn root or the mating nut.
- Holds when: the wear is from rubbing and the reference surface was never in contact. Breaks when: the part was damaged by impact, corrosion, or plating removal.

### Rounding to standard values

- Metric fastener sizes: M1.6, M2, M2.5, M3, M4, M5, M6, M8, M10, M12, M14, M16, M20, M24.
- Common round design numbers: 10, 12, 15, 20, 25, 30, 40, 50, 60, 80, 100 mm.
- Preferred numbers (ISO 3, R10 series, rounded values): 1.00, 1.25, 1.60, 2.00, 2.50, 3.15, 4.00, 5.00, 6.30, 8.00, 10.0. Each step is about 25 percent larger than the one before. Use the rounded table; the raw formula $10^{n/10}$ gives approximate values only.
- Inch sizes: fractions in 1/64 in steps are common in older US drawings; decimal inch is common in some industries.
- Rule of thumb: if the measured value is within about 0.1 mm of a standard value and the wear direction agrees, treat the standard value as the first candidate. Test it against a second feature.

Holds when: the design uses standard fasteners and preferred sizes. Breaks when: the designer chose a custom size for a fit, or the part was made to a non-metric standard.

### Sanity checks on the inference

- The fit should still work with the mating part at the inferred nominal size.
- The inferred clearance should match a standard fit class from the drawing system used.
- A standard fastener should thread into the part at the inferred size.

## Measurement strategy for complex parts

Measure in datum order, not in the order features appear on the part.

1. Choose a primary datum: the most stable, most functional face, usually one that mates with another part or sits on a surface plate.
2. Choose secondary and tertiary datums perpendicular to the primary and to each other. Together they fix the part in space.
3. Support the part on the primary datum at three points, locate it against the second, and clamp it against the third (the 3-2-1 principle).
4. Measure each feature relative to the datums, not to the edge of the part. Record the datum reference with every dimension.
5. Measure in one setup where possible. Each re-setup adds error.
6. Take three readings for any dimension that matters, and report the spread.
7. Check the datums themselves for flatness or squareness before trusting the rest.

Tools by task:

- Plane and height: surface plate, height gauge, indicator.
- Diameter and length: caliper, micrometer, bore gauge, pin gauge.
- Angles: protractor, sine bar, angle block.
- Position of holes: coordinate measuring machine (CMM), or a surface plate with a height gauge and a known reference.
- Thread: pitch gauge, thread gauge, go and no-go gauge.

Holds when: the part is rigid enough to stay in place. Breaks when: the part flexes under its own weight or clamping force, or a datum is itself worn.

## Teardown documentation template

Use a new log for each product. Keep the photos in the same folder and name each photo with its step number.

```
PRODUCT RECORD
Make and model:
Serial or date code:
Date and operator:
Power or stored-energy hazards found, and how each was controlled:

PHOTO LIST
Photo name | Step | Angle or view | Subject

STEP RECORD
Step | Action | Fastener type, size and count | Parts moved | Photo name | Notes

PART LIST
Item | Name | Qty | Material guess and basis | How held and removed | Dimensions measured | Notes

INTENT NOTES
Feature | Likely function | Evidence | Alternative | Confidence (low, medium, high)

OPEN QUESTIONS
-

REASSEMBLY CHECK
Parts in order, fastener map, and the test that proves the product works after reassembly
```

## Legal and ethical checklist

This is general information, not legal advice. Laws differ by country and by product.

- Ownership: you own the product, or the owner has given permission.
- Licenses and terms: you have read the terms that came with the product, including any restriction on decompiling software or reverse-engineering hardware.
- Patents: you have searched patent records for the feature, and you have read the claims, not just the title. A claim can cover a feature in a different shape.
- Copyright: you are measuring the physical part and drawing your own model. You are not copying a supplier's drawing, CAD file, manual, or photograph.
- Trade secrets: you have not received confidential information from anyone who was not entitled to share it.
- Trademarks: you are not using a brand name, logo, or trade dress to suggest the copy is genuine.
- Protection measures: you are not defeating a lock, interlock, usage limit, or access control. Some jurisdictions treat circumventing such measures as unlawful even for personal study (for example, anti-circumvention provisions in copyright law).
- Safety-critical parts: brake parts, pressure vessels, load-bearing parts, medical devices, and electrical protection need engineering verification and testing before any real use. A visual match is not evidence of strength.
- Use: personal study, repair, school work, and sale each carry different obligations. Sale raises the most questions and usually needs a qualified IP lawyer.

## Checklists

### Before trusting an identification

- [ ] At least two independent clues agree.
- [ ] Measurements are taken on an unworn, unplated surface.
- [ ] Units are consistent before any calculation.
- [ ] The result is checked against a standard size or table.
- [ ] Alternatives are written down with the evidence for each.

### Before trusting a rebuilt model

- [ ] Overall volume and mass match the measured part within the error of the measurement.
- [ ] Key distances match the datums.
- [ ] Standard fasteners thread into the model at the inferred size.
- [ ] Fillets and chamfers that the process would produce are included.
- [ ] Every dimension has a stated source: measured, inferred, or assumed.

### Before releasing or selling a reverse-engineered design

- [ ] Legal and ethical checklist completed.
- [ ] Safety-critical features verified by test to a recognized standard.
- [ ] Design differs from any patent claim, or a lawyer has reviewed it.
- [ ] No copied files, drawings, or brand marks are used.

## Sanity checks

- One cubic centimeter of steel weighs about 7.85 g. One cubic centimeter of aluminum weighs about 2.7 g.
- A 10 mm diameter steel sphere has volume $\frac{4}{3}\pi (5)^3 \approx 524$ mm$^3$ and mass about 4.1 g.
- One liter of water is one kilogram, so water density is 1 g/cm$^3$. Plastics that float are below 1.
- One inch is exactly 25.4 mm. A 1 inch bolt has a major diameter of 25.4 mm.
- The M8 coarse pitch (1.25 mm) and the 1/4-20 UNC pitch (1.27 mm) are close. Use the diameter to choose.
- For a bolt circle of radius $R$ with $n$ holes, the adjacent-hole chord is $2R\sin(180^\circ/n)$. For $R = 55$ mm and $n = 5$, the chord is about 64.66 mm. For $n = 6$, it is 55.00 mm (the chord equals the radius).
- A mass estimate off by more than about 10 percent from the density table points to a wrong material, a hidden void, or a wrong volume.
- A worn shaft measures smaller than nominal. A worn bore measures larger than nominal. If the wrong direction appears, suspect a different cause.

## Further reference

Named books and standards. Paid items are named only, with no link.

- Machinery's Handbook (Industrial Press). Standard reference for threads, tolerances, and machining data. Paid.
- Shigley's Mechanical Engineering Design (McGraw-Hill). Standard textbook on machine elements and fastener design. Paid.
- ASME Y14.5, Dimensioning and Tolerancing. Standard for geometric tolerances and datum reference frames. Paid.
- ASME B1.1, Unified Inch Screw Threads. Standard for UN and UNC thread forms. Paid.
- ISO 261 and ISO 262, ISO metric screw threads (general plan and selected sizes). Paid.
- ISO 286, ISO system of limits and fits. Paid.
- ISO 2768, General tolerances for linear and angular dimensions. Paid.
- ISO 3, Preferred numbers. Paid.
- ASM Handbook, Volume 1: Properties and Selection (ASM International). Material property reference. Paid.

No free links are included here. None were fetched in this session, and the rule is to link only sources confirmed to load free content.
