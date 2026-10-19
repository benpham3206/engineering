# Fracture and fatigue claims

**Type:** data

Claims about fracture mechanics and fatigue methods in [Materials reference](../../materials/reference-fracture-fatigue.md). Each claim records the supporting passage in an extracted source. The MIT source keys are proposals and must be registered in `data/sources.md` before merge.

### fracture-crack-tip-field-modes
- Claim: Irwin's linear elastic crack-tip field is singular as the distance to a sharp crack tip approaches zero, and crack modes describe opening, sliding, and tearing.
- Values: mode
- Layer: durable
- Status: verified-1
- Sources: nasa-lefm-primer (section 2.1, pages 7-9, "Three fundamental modes of crack-tip deformation" and "The crack-tip stresses of equation 11 are proportional to r -1/2")
- Checked: agent, 2026-10-19, read the extracted NASA primer text and matched the cited section

### fracture-k-factor-forms
- Claim: The NASA primer gives geometry-dependent stress intensity factor solutions, including the edge-cracked plate in tension polynomial for crack depth over width no greater than 0.6.
- Values: crack
- Layer: durable
- Status: verified-1
- Sources: nasa-lefm-primer (section 3, pages 21-22, "Edge cracked plate in tension" and polynomial ending "30.382c_ 4")
- Checked: agent, 2026-10-19, read the extracted NASA primer text and matched the geometry and coefficients

### fracture-griffith-energy
- Claim: For a through crack in a wide plate under fixed remote stress, Griffith's ideal brittle-solid energy release rate is proportional to stress squared times crack half-length, and Irwin relates it to the squared stress intensity factor through the effective elastic modulus.
- Values: energy
- Layer: durable
- Status: verified-1
- Sources: nasa-lefm-primer (section 1, pages 2-3, "GI is also called the crack driving force" and "where E'= E for plane stress and E'= E/(1 - u 2) for plane strain")
- Checked: agent, 2026-10-19, read the extracted NASA primer text and matched the energy and intensity discussion

### fracture-toughness-size-rule
- Claim: Fracture toughness depends on temperature, heat treatment, and constraint, and a plane-strain toughness test requires specimen dimensions large compared with the plastic zone.
- Values: toughness
- Layer: durable
- Status: verified-1
- Sources: nasa-lefm-primer (section 4, pages 27-29, "fracture toughness ... may be strongly affected by operating temperature, heat treatment, and constraint" and "dimensions are large compared to the plastic zone size")
- Checked: agent, 2026-10-19, read the extracted NASA primer text and matched the cited statements

### fracture-irwin-plastic-zone
- Claim: Irwin's first-order plastic-zone estimate is smaller by a factor of three under plane-strain constraint than under plane stress.
- Values: zone
- Layer: durable
- Status: verified-1
- Sources: nasa-lefm-primer (section 2.3, pages 10-11, "For thick plates ... plane strain" and "smaller by a factor of three")
- Checked: agent, 2026-10-19, read the extracted NASA primer text and matched the plane-stress and plane-strain discussion

### fracture-leak-before-burst
- Claim: Leak before burst concerns flaws that grow through a pressure wall without immediate catastrophic failure, with flaw size constrained by fracture conditions before and after breakthrough.
- Values: leak before burst
- Layer: durable
- Status: verified-1
- Sources: nasa-lefm-primer (section 7.2, pages 51-53, "flaws in a pressure vessel safely grow through the pressure wall without causing immediate catastrophic failure")
- Checked: agent, 2026-10-19, read the extracted NASA primer text and matched the cited section

### fatigue-paris-law
- Claim: In region II, Paris' empirical relation models fatigue crack growth rate as a power of the stress intensity factor range; the fitted constants depend on material and test conditions.
- Values: Paris
- Layer: durable
- Status: verified-1
- Sources: nasa-lefm-primer (section 5.1, pages 35-38, "The Paris equation describes crack growth in region II" and "For most materials, the value of n ranges from 2 to 4")
- Checked: agent, 2026-10-19, read the extracted NASA primer text and matched the Paris law, regimes, and conditions

### fatigue-basquin
- Claim: Basquin observed that stress amplitude versus reversals to failure can be linearized on log-log axes, and practical design stress amplitude may be reduced from the curve value by a safety factor.
- Values: stress
- Layer: durable
- Status: verified-1
- Sources: mit-ocw-2002 (section "Basquin's relation", page 19, "observed that the a versus Nf data could be effectively linearized on log-log axes"; section "Stress-Life Properties", page 20, "reduced ... by a safety factor, often in the range of a factor of 2")
- Checked: agent, 2026-10-19, read the extracted MIT 2.002 notes and matched both passages

### fatigue-endurance-limit
- Claim: Most ferritic and martensitic steels exhibit an endurance limit, while most non-ferrous alloys do not show a true endurance limit; for wrought steels the notes give a specimen correlation capped at 700 MPa above 1400 MPa tensile strength.
- Values: limit
- Layer: durable
- Status: verified-1
- Sources: mit-ocw-2002 (section "Endurance Limit", page 19, "Most ferritic and martensitic steels exhibit an endurance limit" and "a pseudo-endurance limit ... 5 x 106 cycles"; equation 14, "if TS > 200 ksi or 1400 MPa")
- Checked: agent, 2026-10-19, read the extracted MIT 2.002 notes and matched the stated alloy classes and correlation

### fatigue-strain-life
- Claim: The Coffin-Manson relation models plastic strain amplitude as a power of reversals to failure, and the ductility exponent for many metals is usually between -0.5 and -0.7, with -0.6 typical.
- Values: strain
- Layer: durable
- Status: verified-1
- Sources: mit-ocw-2002 (section "Low Cycle Fatigue", pages 22-23, "Coffin and Manson independently established a power law correlation" and "usually in the range -.5 ... -.7 ... with c = -.6 as typical")
- Checked: agent, 2026-10-19, read the extracted MIT 2.002 notes and matched the relation and exponent range

### fatigue-goodman
- Claim: The Goodman diagram joins the endurance limit on the alternating-stress axis to the ultimate tensile strength on the mean-stress axis.
- Values: Goodman
- Layer: durable
- Status: verified-1
- Sources: mit-ocw-311 (section "Effect of mean load", page 4, "a straight lifeline is drawn from the endurance limit on the ... axis to the ultimate tensile stress")
- Checked: agent, 2026-10-19, read the extracted MIT 3.11 notes and matched the Goodman diagram description

### fatigue-strain-life-mean-stress
- Claim: In strain-life analysis, a tensile mean stress reduces the effective fatigue strength coefficient, while a conservative treatment of compressive mean stress retains the zero-mean relation.
- Values: mean stress
- Layer: durable
- Status: verified-1
- Sources: mit-ocw-2002 (section "Mean Stress Effects on Fatigue", page 28, "a tensile mean stress, m > 0, will correspondingly reduce the effective fatigue strength coefficient" and "a conservative approach would be to continue to use eq. (18) ... in those cases where m is negative")
- Checked: agent, 2026-10-19, read the extracted MIT 2.002 notes and matched the mean-stress statements

### fatigue-kf-peterson
- Claim: The MIT notes identify Peterson's handbook as a source for elastic stress concentration factors and give reference values of 0.001 in (25.4 micrometres) and 300 ksi (2070 MPa) for the wrought-steel notch-sensitivity fit.
- Values: notch
- Layer: durable
- Status: verified-1
- Sources: mit-ocw-2002 (section "Notch Sensitivity", page 34, "0 = .001 in = 25.4 x 10-6m" and "= 300 ksi = 2070 MPa")
- Checked: agent, 2026-10-19, read the extracted MIT 2.002 notes and matched the fit constants

### fatigue-neuber
- Claim: The MIT notes state Neuber's rule as the product of local stress and strain concentration factors equaling the square of the fatigue notch factor, and describe the rule as most appropriate for planar geometries with root radius comparable to sheet thickness.
- Values: notch
- Layer: durable
- Status: verified-1
- Sources: mit-ocw-2002 (section "Neuber's Rule", pages 35-36, "K · K = (Kf)2" and "most appropriate for planar geometries in generalized plane stress with root radius of comparable size with sheet thickness")
- Checked: agent, 2026-10-19, read the extracted MIT 2.002 notes and matched the rule and limitation

### fatigue-miner
- Claim: Miner's linear cumulative damage model sums the fractions of constant-amplitude life consumed by each loading block, and its linear accumulation assumption can miss fatigue mechanisms.
- Values: damage
- Layer: durable
- Status: verified-1
- Sources: mit-ocw-2002 (section "Cumulative Fatigue Damage", pages 28-29, "fatigue failure occurs when" and "The theory of linear cumulative fatigue damage assumes")
- Checked: agent, 2026-10-19, read the extracted MIT notes and matched the damage rule and caveat

### fracture-damage-tolerance-scatter
- Claim: The NASA primer's proof-test example applies a scatter factor of 4 to a 10,000-cycle service requirement and evaluates the proof-test factor from crack-growth life.
- Values: scatter factor
- Layer: durable
- Status: verified-1
- Sources: nasa-lefm-primer (section 8.1.4, pages 59-60, "10,000 cycles x scatter factor of 4" and "For a proof stress of 20 ksi, the proof factor of 1.33 is calculated")
- Checked: agent, 2026-10-19, read the extracted NASA primer text and matched the worked example
