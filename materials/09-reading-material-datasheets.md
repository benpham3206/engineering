# Reading material datasheets

**Type:** lesson
**Verify:** strict

A **technical data sheet (TDS)** is a supplier's record of measured properties for a named material and stated test conditions. Engineers use it to decide what to test in a real part under its expected load, temperature, and environment.

**Prerequisites:** [Mechanical properties](03-mechanical-properties.md), [Material selection](08-material-selection.md), [Additive manufacturing](../manufacturing/04-additive-manufacturing.md)
**Time:** 3-4 h

## Core ideas

### A TDS and an SDS answer different questions

Technical data sheets report product properties and test methods, while safety data sheets state chemical hazards, composition, handling, and emergency information [src](../data/claims/printing-materials.md#tds-and-sds-roles). Read the SDS before handling a resin or filament, then use the TDS to judge whether the material merits testing for a design.

A value in a TDS describes a test specimen. It does not automatically describe a finished part or set a safe service load. The material name, print process, specimen direction, conditioning, and test method all belong beside the value.

### Mechanical properties

A **test specimen**, or coupon, is a small sample made in a stated shape and orientation for measurement.

**Tensile strength** is the largest tensile stress reached by a specimen in a pull test, or the stress at break when the source reports break strength. Stress is force divided by the original cross-section area, in pascals. A datasheet may also list yield strength, the stress where permanent deformation starts. Keep yield and break values in separate columns.

**Tensile modulus** is the slope of the early, nearly straight part of a tensile stress-strain curve. It measures stiffness, in pascals. A large modulus means more stress is needed for a small elastic strain. It does not say how much stress the material can take before it yields or breaks.

**Elongation at break** is the increase in a tensile specimen's gauge length divided by its original gauge length when it breaks. It is usually reported as a percentage. A high value indicates that the tested specimen stretched far before breaking; it does not by itself measure impact resistance or fatigue life.

**Flexural strength** is the bending stress at a stated failure or deflection point in a beam test. **Flexural modulus** is the slope of the early, nearly straight part of that beam's stress-strain response. Both depend on specimen geometry and support span, so compare them only when the test setup matches.

**Notched impact strength** is the absorbed impact energy divided by a specimen dimension or cross-sectional area, depending on the method. A notch concentrates stress and makes crack initiation easier. Izod holds a notched bar as a cantilever; Charpy supports it as a beam and strikes the opposite face. Keep the method, notch direction, and units with the value. Do not combine Izod values in J/m with Charpy values in kJ/m².

The supplied Polymaker sheets report notched Charpy impact strength. The supplied UltiMaker sheets also identify notched Charpy specimens; other product sheets may use Izod, so read the method named beside each result [src](../data/claims/printing-materials.md#impact-methods).

### Thermal, hardness, and physical properties

**Heat deflection temperature (HDT)** is the temperature at which a loaded specimen bends by a specified amount during heating. The stated load matters: a value measured near 0.45 MPa cannot be swapped with one measured at 1.8 MPa. HDT is a test result, not a recommended continuous-use temperature.

**Glass transition temperature** is the temperature range where amorphous regions of a polymer gain much more molecular mobility. A supplier may measure it with calorimetry or a mechanical test. Glass transition is not melting, and neither value alone gives a safe part temperature.

**Shore hardness** is resistance to indentation measured with a spring-loaded indenter. Shore A suits softer elastomers; Shore D suits harder plastics. The scale and test time matter, so a Shore A number cannot be ranked directly against a Shore D number.

**Density** is mass divided by volume, in kg/m³. A filament TDS may report dense polymer material, while a printed part also contains voids from its infill and print path. Use the part's measured mass and external volume when its actual density matters.

**Water absorption** is the mass gained by a specimen after exposure to water under stated conditions, often expressed as a percentage of its dry mass. The immersion time, temperature, specimen thickness, and drying procedure affect the result. A wet nylon part can have different stiffness and strength from a dry one.

### Test conditions set the meaning

The dimensions, print settings, infill, layer height, test machine, and test speed can change a tensile result. Read the notes after the property tables, because they often state conditions that the table heading leaves out.

For fused filament fabrication (FFF), **print orientation** is the direction of the specimen relative to the build plate and deposited roads. XY means the specimen lies flat; Z means it stands upright so tension crosses layer interfaces. The printed roads bond by heat and contact, so a load across those interfaces can separate layers. Supplier data show lower Z values in examples such as PLA, where tensile strength is 52.3 MPa in XY and 40.5 MPa in Z [src](../data/claims/printing-materials.md#pla-orientation).

The difference depends on the material and print settings. Wall roads, infill direction, layer height, temperature, cooling, and voids change the load path. Use the orientation closest to the finished part, and test the weakest direction that the part will see.

**Conditioning** is the controlled drying, moisture exposure, aging, or temperature treatment applied before testing. **Post-curing** is additional light and heat exposure used to finish a photopolymer resin after printing. Record both when the source reports them. A value for dry, annealed nylon or post-cured resin does not describe a wet or uncured part.

### Compare material rows with care

The table gives reported typical ranges from two independent supplier sheets per nonempty cell. It combines individual product values, not a statistical range for every grade in a polymer family. Different printers, specimens, orientations, and test procedures can explain part of each spread. Treat a blank as missing comparable evidence, not as zero.

Tensile entries below mean XY or flat specimen strength at break. Modulus and elongation use the same direction where both sources report them. HDT is near 0.45 MPa; the source values use 0.45 or 0.455 MPa. Density is converted to SI units. Each populated cell links to the claim that records the two source values and conditions.

| Material (typical) | Density ($\text{kg/m}^3$) | Tensile strength at break, XY (MPa) | Tensile modulus, XY (GPa) | Elongation at break, XY (%) | HDT near 0.45 MPa (°C) | Glass transition (°C) |
|---|---:|---:|---:|---:|---:|---:|
| PLA, typical | 1170-1240 [src](../data/claims/printing-materials.md#pla-density-range) | 45.5-52.3 [src](../data/claims/printing-materials.md#pla-tensile-strength-range) | 3.25-3.43 [src](../data/claims/printing-materials.md#pla-tensile-modulus-range) | 6.3-7.8 [src](../data/claims/printing-materials.md#pla-elongation-range) | 58.8-60 [src](../data/claims/printing-materials.md#pla-hdt-range) | 59.1-61 [src](../data/claims/printing-materials.md#pla-glass-transition-range) |
| PETG, typical | 1250-1270 [src](../data/claims/printing-materials.md#petg-density-range) | 38.5-50.8 [src](../data/claims/printing-materials.md#petg-tensile-strength-range) | 1.94-2.12 [src](../data/claims/printing-materials.md#petg-tensile-modulus-range) | 7.6-8.4 [src](../data/claims/printing-materials.md#petg-elongation-range) | 76.2-78 [src](../data/claims/printing-materials.md#petg-hdt-range) | 77.4-81 [src](../data/claims/printing-materials.md#petg-glass-transition-range) |
| ABS, typical | 1100-1120 [src](../data/claims/printing-materials.md#abs-density-range) |  |  |  | 86.6-100 [src](../data/claims/printing-materials.md#abs-hdt-range) | 100.5-101 [src](../data/claims/printing-materials.md#abs-glass-transition-range) |
| Nylon, typical, PA6/66 and PA6/12 examples | 1120-1140 [src](../data/claims/printing-materials.md#nylon-density-range) | 40.4-78 [src](../data/claims/printing-materials.md#nylon-tensile-strength-range) | 2.33-2.70 [src](../data/claims/printing-materials.md#nylon-tensile-modulus-range) |  | 89.2-111 [src](../data/claims/printing-materials.md#nylon-hdt-range) | 55.1-66 [src](../data/claims/printing-materials.md#nylon-glass-transition-range) |
| Polycarbonate (PC), typical | 1180-1200 [src](../data/claims/printing-materials.md#pc-density-range) | 43.2-69.1 [src](../data/claims/printing-materials.md#pc-tensile-strength-range) | 2.39-2.50 [src](../data/claims/printing-materials.md#pc-tensile-modulus-range) | 4.8-9.2 [src](../data/claims/printing-materials.md#pc-elongation-range) | 104.5-111 [src](../data/claims/printing-materials.md#pc-hdt-range) | 107.7-113 [src](../data/claims/printing-materials.md#pc-glass-transition-range) |
| TPU 95A, typical | 1200-1240 [src](../data/claims/printing-materials.md#tpu-density-range) |  |  |  |  |  |

The PolyLite ABS sheet lists XY tensile strengths of 33.4 MPa and 29.7 MPa, then gives 29.7 MPa for Z, so those rows are excluded from this comparison [src](../data/claims/printing-materials.md#abs-repeated-tensile-row). Nylon grades and conditioning differ, so its range is a screen for which products to test, not a single nylon design property. The PolyFlex TPU95 sheet lists 33.6 MPa as Young's modulus, which this comparison excludes [src](../data/claims/printing-materials.md#tpu-modulus-flag). It has no matching XY values from both suppliers for the other mechanical columns.

Water absorption and HDT at 1.8 MPa are not in the range table because the supplied sheets do not provide two comparable values for these materials. The properties still matter in design. Ask a supplier for the method and conditions or test the part in its actual environment.

## Key equations

Engineering stress divides tensile force by the specimen's original area. Engineering strain divides its change in gauge length by its original gauge length. Their ratio in the initial linear region is Young's modulus:

$$
\sigma = \frac{F}{A_0}, \qquad \epsilon = \frac{\Delta L}{L_0}, \qquad E = \frac{\Delta \sigma}{\Delta \epsilon}
$$

$\sigma$ is stress in Pa, $F$ is tensile force in N, $A_0$ is original cross-section area in m², $\epsilon$ is dimensionless strain, $\Delta L$ is change in gauge length in m, $L_0$ is original gauge length in m, and $E$ is tensile modulus in Pa. The modulus equation applies only over the initial linear response; polymers can be nonlinear, yield, and creep.

## Worked example

### Screen a wet, upright nylon coupon

A PolyMide CoPA data sheet reports dry XY tensile strength of 78.0 MPa, wet XY tensile strength of 34.3 MPa, wet Z tensile strength of 13.7 MPa, and 6.16% average moisture in wet specimens [src](../data/claims/printing-materials.md#nylon-dry-and-wet). The dry samples were annealed and dried; the wet samples were annealed and then immersed in water.

**Given:** Use the wet Z strength after accounting for moisture and orientation. Assume a temperature factor of 0.80, a creep factor of 0.70, and a factor of safety of 2.0. The part has a net load-carrying area of $20\ \text{mm}^2$ and sees a steady 50 N tensile load.

**Find:** The illustrative allowable stress, the applied stress, and whether this simple screen passes.

**Assumptions:** The load is axial and steady. The wet Z specimen is the closest available strength condition. The temperature and creep factors are chosen for this example and are not supplier test results. This screen does not establish a certified design allowable.

**Solution:**

1. Moisture factor: $34.3/78.0 = 0.440$.
2. Orientation factor in the wet condition: $13.7/34.3 = 0.399$.
3. Apply those reductions to the dry XY value, then apply the chosen temperature and creep factors and divide by the factor of safety: $78.0(34.3/78.0)(13.7/34.3)(0.80)(0.70)/2.0 = 3.84$ MPa.
4. Applied stress is $50/20 = 2.50\ \text{N/mm}^2$, equal to 2.50 MPa.
5. Since 2.50 MPa is below 3.84 MPa, this example passes the stated screen. A real part still needs validation with its geometry, print settings, moisture, temperature, and load duration.

**Answer:** The illustrative allowable is 3.84 MPa and the applied stress is 2.50 MPa, so the simple screen passes.

**Sanity check:** The allowable is below the measured wet Z strength of 13.7 MPa because the chosen temperature, creep, and safety reductions all lower it.

<details><summary>Verification</summary>

```verify
given("80", "6", "48", "60", "6.16")
dry_xy = q(78.0, "MPa")
wet_xy = q(34.3, "MPa")
wet_z = q(13.7, "MPa")
temp = q(0.80, "1")
creep = q(0.70, "1")
fs = q(2.0, "1")
area = q(20, "mm^2")
force = q(50, "N")
moisture = wet_xy / dry_xy
expect(moisture, "0.440 1")
orientation = wet_z / wet_xy
expect(orientation, "0.399 1")
allow = dry_xy * moisture * orientation * temp * creep / fs
expect(allow, "3.84 MPa")
stress = force / area
expect(stress, "2.50 MPa")
check(stress < allow, "the stated example load is below the illustrative allowable")
check(allow < wet_z, "additional factors reduce the measured wet Z strength")
```

</details>

## Practice

1. A supplier reports 45 MPa tensile yield strength and 52 MPa tensile strength at break. Which value answers the question "when does permanent deformation begin"?
2. A coupon with 80 mm original gauge length measures 86 mm at break. Find its elongation at break as a percentage.
3. A printed bracket will carry a load that pulls across its layer interfaces. A data sheet gives 48 MPa in XY and 18 MPa in Z. Which direction should guide a first strength screen, and why?
4. A resin TDS reports properties after post-curing. Your part will be used immediately after washing. What evidence is missing before you use the TDS values?

<details><summary>Answers</summary>

1. The 45 MPa yield strength marks the start of permanent deformation.
2. The gauge length increased by 6 mm, so elongation at break is $6/80 \times 100 = 7.5\%$.
3. Use the Z value for the first screen because the load crosses the layer interfaces. The supplier's orientation and specimen conditions still need to match the part.
4. The TDS does not describe the un-post-cured part. Measure or obtain data for the washed, uncured state, or post-cure the part as specified before using those values.

```verify
given("100")
yield_strength = q(45, "MPa")
break_strength = q(52, "MPa")
check(yield_strength < break_strength, "yield precedes the reported break strength")
L0 = q(80, "mm")
Lf = q(86, "mm")
elongation = (Lf - L0) / L0
expect(elongation, "7.5 %", ans=2)
xy = q(48, "MPa")
z = q(18, "MPa")
check(z < xy, "the stated Z value is the weaker direction", ans=3)
skip(ans=1, why="short answer")
skip(ans=4, why="short answer")
```

</details>

## Common mistakes

- Treating tensile modulus as strength. Modulus measures the slope of the early stress-strain curve; strength describes a yield or break point.
- Comparing a flat XY coupon with an upright Z coupon as if print direction did not matter.
- Mixing notched Charpy and Izod impact values, or comparing values with different units.
- Reading HDT as a service temperature without checking its load and specimen conditions.
- Treating a dry, annealed or post-cured specimen as equivalent to a wet, unannealed or uncured part.
- Reusing the 33.6 MPa Polymaker TPU95 entry as a tensile modulus [src](../data/claims/printing-materials.md#tpu-modulus-flag). The sheet labels it Young's modulus, but this lesson excludes it from comparison because the entry is not suitable as a modulus value.

## Go deeper

- [Safety Data Sheet (SDS)](https://www.ccohs.ca/oshanswers/chemicals/whmis_ghs/sds.html) by the Canadian Centre for Occupational Health and Safety: what each section of an SDS tells you.
- [Mechanical properties](03-mechanical-properties.md)
- [Material selection](08-material-selection.md)
- [Additive manufacturing](../manufacturing/04-additive-manufacturing.md)
- [Factor of safety and failure](../design/07-factor-of-safety-and-failure.md)
