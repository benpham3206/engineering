# Materials reference

**Type:** reference

A lookup sheet for choosing, checking, and failing-analysing engineering materials, for engineers who already know the basics and need a value, a relation, or a checklist in the middle of a job.

## Principles

- Processing sets structure, structure sets properties, and properties set performance. Change the processing and the same composition can behave very differently.
- Stiffness comes from bonding and changes little with microstructure. Strength, toughness, and fatigue life depend strongly on microstructure and flaws.
- Real parts contain flaws. Fracture happens when a crack reaches its critical size, not when the average stress reaches a limit.
- Temperature changes most properties. Above roughly 0.3 to 0.5 of the melting temperature (in kelvin), creep and time-dependent failure matter.
- Corrosion is electrochemistry. No electrolyte, or no electron path between the two sites, means no galvanic corrosion.
- Table values are typical, not guaranteed. Design to specified minimums from the supplier or code, with the actual condition, temperature, and environment.
- Any single property is not a material choice. Rank candidates by a performance index built from the constraints and the objective.
- Use SI units throughout. Check the unit of every number before combining them.

## Bonding and crystal structure (foundations)

| Bond | Character | Typical consequence |
|---|---|---|
| Ionic | Electron transfer, nondirectional attraction | Hard, brittle, high melting point |
| Covalent | Shared electron pairs, directional | Hard, stiff, brittle in ceramics; stiff chains in polymers |
| Metallic | Delocalized electron sea | Conductive, ductile, dense |
| Secondary (van der Waals, hydrogen) | Weak, between molecules | Low melting point, creep, softening in polymers |

Crystal structures of common metals (room temperature):

| Structure | Examples | Atoms per cell | Atomic packing factor | Ductility note |
|---|---|---|---|---|
| BCC | alpha Fe, Cr, W | 2 | 0.68 | Strong, can be brittle at low T |
| FCC | Al, Cu, Ni, austenitic steel | 4 | 0.74 | Usually ductile |
| HCP | Ti (alpha), Mg, Zn | 6 (hcp cell) | 0.74 | Few slip systems, often less ductile |

- Density of a crystal: $\rho = \dfrac{n M}{V_c N_A}$, where $\rho$ is density (kg/m$^3$), $n$ the atoms per cell, $M$ the molar mass (kg/mol), $V_c$ the cell volume (m$^3$), and $N_A = 6.022 \times 10^{23}$ mol$^{-1}$. Check: alpha iron (BCC, $a = 0.2866$ nm) gives about 7880 kg/m$^3$.
- The formula holds for ideal lattices. It breaks when vacancies, precipitates, or porosity change the density, which is why cast and sintered parts differ from the crystal value.
- Hall-Petch: $\sigma_y = \sigma_0 + k_y d^{-1/2}$, where $d$ is grain diameter (m), and $\sigma_0$ and $k_y$ are material constants. The relation holds for grains from micrometres down to about tens of nanometres. It breaks at very fine grains, where grain boundary sliding softens the metal.
- Strengthening mechanisms all work by blocking dislocation motion: grain refinement, solid solution, precipitates, and cold work.

## Typical property table

All values are typical at room temperature, in the stated condition. They are not design minimums. Use "n/a" where the material does not yield in a sharp way. "Not listed" means the value was left out because it is not reliable enough to print. "Code-limited" means the service limit is set by a design code, not by the material alone.

| Material (condition) | $\rho$ (kg/m$^3$) | $E$ (GPa) | $\sigma_y$ (MPa) | $\sigma_u$ (MPa) | Elongation (%) | $\alpha$ (10$^{-6}$/K) | $k$ (W/m K) | Max service (C) |
|---|---|---|---|---|---|---|---|---|
| Structural steel (A36 type) | 7850 | 200 | 250 | 400-550 | about 20 | about 12 | about 50 | code-limited |
| 1018 steel (cold drawn) | 7870 | 205 | 370 | 440 | about 15 | about 11.5 | about 51 | code-limited |
| 1018 steel (hot rolled) | 7870 | 205 | about 220 | about 400 | about 25 | about 11.5 | about 51 | code-limited |
| 4140 steel (annealed) | 7850 | 205 | about 415 | about 655 | about 25 | about 12 | about 42 | code-limited |
| 304 stainless (annealed) | 8000 | 193 | about 215 | about 515 | 40-60 | 17.2 | about 16 | about 870 (oxidation, approx.) |
| 6061-T6 aluminum | 2700 | 69 | 276 | about 310 | about 12 | 23.6 | about 167 | about 150 (approx.) |
| 7075-T6 aluminum | 2810 | 72 | about 503 | about 572 | about 11 | 23.4 | about 130 | about 120 (approx.) |
| Ti-6Al-4V (annealed) | 4430 | 114 | about 880 | about 950 | about 14 | 8.6 | about 6.7 | about 400 (approx.) |
| Copper (annealed) | 8960 | 117-130 | about 70 | about 220 | about 45 | about 16.5 | about 390 | not listed |
| Brass 70/30 (annealed) | 8530 | 110 | about 75 | about 300 | 60-68 | about 20 | about 120 | not listed |
| Gray cast iron (class 30 type) | about 7200 | about 110 | n/a (brittle) | about 200-300 | under 1 | about 11 | about 45-50 | not listed |
| PLA (3D print grade) | about 1240 | about 3.5 | about 60 | about 60 | about 4 | about 68 | about 0.13 | about 55 (Tg, approx.) |
| ABS | about 1050 | about 2.3 | about 40 | about 40-45 | about 20 | 90-100 | about 0.2 | about 80 (Tg about 105) |
| Nylon 6/6 (dry) | 1140 | 2.9 | about 80 | about 80-85 | about 60 | 80-100 | about 0.25 | about 80-120 |
| PEEK | about 1300 | about 3.6 | about 97 | about 100 | 30-50 | about 47 | about 0.25 | about 250 (Tg 143) |
| Polycarbonate | about 1200 | about 2.4 | about 62 | about 65 | over 50 | about 65 | about 0.2 | about 115 (Tg 147) |
| CFRP quasi-isotropic (epoxy, carbon fiber) | about 1550 | about 50 | n/a | about 600 | about 1.5 | 2-4 | about 5 in plane | about 120 (epoxy-limited) |
| Soda-lime glass | 2500 | 70 | n/a (brittle) | 30-100 (flaw-dependent) | about 0 | about 9 | about 1.0 | about 450 (approx.) |
| Alumina (99.5 percent) | about 3900 | 370 | n/a (brittle) | flexural about 350 | about 0 | about 8 | 25-35 | about 1500 (approx.) |
| Concrete (normal weight) | about 2400 | 25-35 | n/a (brittle) | tension 2-5; compression 20-40 | about 0.01 | 10-12 | 1.4-2.0 | not listed |
| Wood, Douglas fir (parallel to grain) | about 530 | about 13 | n/a | compression about 45 | small | 3-5 | not listed | not listed |

Notes:

- Glass, alumina, concrete, and wood have no yield point. For these, use the fracture data in the fracture section, not $\sigma_y$.
- Wood, concrete, and fiber composites are anisotropic. The values apply only in the stated direction.
- Polymer values depend strongly on temperature, moisture, and fill. Nylon absorbs water and its stiffness drops with humidity.
- Heat-treated steels and aluminum alloys vary widely with temper. Always specify the condition (for example 6061-T6 and not "6061").

## Elastic constants

For an isotropic, linear elastic material, only two independent constants are needed. The others follow.

- Hooke's law, normal: $\sigma = E\,\varepsilon$. Shear: $\tau = G\,\gamma$.
- Lateral strain: $\varepsilon_{\text{lat}} = -\nu\,\varepsilon_{\text{axial}}$, with $\nu$ the Poisson's ratio.
- Shear modulus: $G = \dfrac{E}{2(1+\nu)}$
- Bulk modulus: $K = \dfrac{E}{3(1-2\nu)}$, where $K$ is the ratio of hydrostatic pressure to volumetric strain.
- Equivalent form: $E = 2G(1+\nu) = 3K(1-2\nu)$.
- Stability bounds: $-1 < \nu < 0.5$. Most metals have $\nu$ near 0.3, cork is near 0, and rubber is near 0.5.
- The relations hold for linear elastic, isotropic, small-strain, uniform materials. They break for composites, wood, single crystals, and anything past yield.
- Sanity: steel with $E = 200$ GPa and $\nu = 0.3$ gives $G = 77$ GPa and $K = 167$ GPa.
- Thermal strain: $\varepsilon_{\text{th}} = \alpha\,\Delta T$, with $\alpha$ the coefficient of thermal expansion (1/K). A fully constrained, linear elastic bar carries $\sigma = E\,\alpha\,\Delta T$ in compression on heating. It breaks when the part can move freely or when the material yields.

## Stress-strain curve landmarks

- Engineering stress $\sigma = F/A_0$ and engineering strain $\varepsilon = \Delta L/L_0$. True stress $\sigma_t = \sigma(1+\varepsilon)$ and true strain $\varepsilon_t = \ln(1+\varepsilon)$, valid up to the onset of necking.
- Proportional limit: the end of the straight-line Hooke's law region.
- Elastic limit: the highest stress with no permanent set. Usually close to the proportional limit.
- Yield strength $\sigma_y$: for metals without a sharp yield, the 0.2 percent offset method. Low-carbon steel shows a flat yield plateau (Luders bands) before work hardening.
- Ultimate tensile strength $\sigma_u$: the maximum engineering stress. For ductile metals, necking starts here (Considere criterion).
- Fracture point: the stress and strain where the specimen separates. Engineering values can drop after necking, so true stress is the better measure of local stress.
- Resilience (elastic energy per unit volume to yield): $U_r = \dfrac{\sigma_y^2}{2E}$ (J/m$^3$). Useful for springs.
- Toughness: the area under the stress-strain curve to fracture (J/m$^3$).
- Work hardening (Hollomon form, plastic range): $\sigma_t = K\,\varepsilon_t^{\,n}$, where $K$ is the strength coefficient (MPa) and $n$ the strain hardening exponent (dimensionless). The relation holds for uniform plastic flow before necking.
- Yield-to-tensile ratio: high ratio (near 1) means little work-hardening margin before a load drop; cold-worked and quenched steels often have high ratios.

## Hardness scales

Hardness is resistance to local indentation. No hardness scale is an absolute measure, and scales are not directly comparable. Pick one scale and use it consistently.

| Scale | Indenter and load | What it suits | Notes |
|---|---|---|---|
| Rockwell C (HRC) | Diamond cone, 150 kgf major load | Hardened and tempered steel | Depth-based. Typical for shop checks on heat-treated parts |
| Rockwell B (HRB) | 1/16 in ball, 100 kgf | Annealed steel, aluminum, copper alloys | Soft materials |
| Brinell (HBW) | Tungsten carbide ball, large load | Castings, forgings, coarse structures | Averages over many grains. Good for coarse or non-uniform materials |
| Vickers (HV) | Diamond pyramid, selectable load | Any metal, thin sections, weld zones, microhardness | One scale at all loads. Load-dependent at low loads |
| Knoop (HK) | Elongated diamond pyramid | Thin coatings, brittle materials | Gives an elongated indent for direction-sensitive readings |
| Shore A or D | Spring-loaded indenter | Elastomers and polymers | Durometer, not comparable to metal scales |

- Rule of thumb: for metals, hardness roughly tracks yield and tensile strength. For steel, tensile strength is roughly 3.4 times the Brinell number, in MPa. It holds for plain carbon and low alloy steels in the annealed or tempered state. It breaks for cold worked, case hardened, or highly alloyed steels.
- Test thickness: the sample should be at least about ten times the indent depth thick, or the reading is pulled low by the support.
- Hardness is a surface and local reading. It does not show subsurface properties after case hardening or decarburization.

## Ashby performance indices

Use the index as a ranking tool, not as a design value. Higher is better when maximizing. Index units follow the input units, so compare only within one table. The table below uses $\rho$ in g/cm$^3$, $E$ in GPa, and $\sigma_y$ in MPa.

Common design goals, for a light part with fixed length and load:

| Design goal | Constraint | Index | Notes |
|---|---|---|---|
| Stiff tie | Stiffness | $E/\rho$ | Tie, rod in tension |
| Strong tie | Yield | $\sigma_y/\rho$ | Tie, rod in tension |
| Stiff beam | Stiffness | $E^{1/2}/\rho$ | Square section, bending |
| Strong beam | Yield | $\sigma_y^{2/3}/\rho$ | Square section, bending |
| Stiff panel | Stiffness | $E^{1/3}/\rho$ | Plate in bending |
| Strong panel | Yield | $\sigma_y^{1/2}/\rho$ | Plate in bending |
| Thermal shock resistance | Thermal stress | $\sigma_f/(E\,\alpha)$ | Brittle ceramics and glass |

Ranking table (computed; ranking only, not design values):

| Material | $E/\rho$ | $E^{1/2}/\rho$ | $E^{1/3}/\rho$ | $\sigma_y/\rho$ | $\sigma_y^{2/3}/\rho$ | $\sigma_y^{1/2}/\rho$ |
|---|---|---|---|---|---|---|
| 1018 steel | 26.0 | 1.82 | 0.75 | 47.0 | 6.55 | 2.44 |
| 304 stainless | 24.1 | 1.74 | 0.72 | 26.9 | 4.49 | 1.83 |
| 6061-T6 aluminum | 25.6 | 3.08 | 1.52 | 102.2 | 15.7 | 6.15 |
| 7075-T6 aluminum | 25.6 | 3.02 | 1.48 | 179.0 | 22.5 | 7.98 |
| Ti-6Al-4V | 25.7 | 2.41 | 1.09 | 198.6 | 20.7 | 6.70 |
| Copper (annealed) | 13.1 | 1.21 | 0.55 | 7.8 | 1.90 | 0.93 |
| PLA | 2.8 | 1.51 | 1.22 | 48.4 | 12.4 | 6.25 |
| ABS | 2.2 | 1.44 | 1.26 | 38.1 | 11.1 | 6.02 |
| Nylon 6/6 (dry) | 2.5 | 1.49 | 1.25 | 70.2 | 16.3 | 7.85 |
| PEEK | 2.8 | 1.46 | 1.18 | 74.6 | 16.2 | 7.58 |
| Polycarbonate | 2.0 | 1.29 | 1.12 | 51.7 | 13.1 | 6.56 |
| Soda-lime glass | 28.0 | 3.35 | 1.65 | n/a | n/a | n/a |
| Alumina | 94.9 | 4.93 | 1.84 | n/a | n/a | n/a |

The indices hold when the constraint and objective match the index, the section shape matches the load case, and no other constraint (for example fatigue, creep, or fracture) limits the part. They break when fracture toughness (brittle materials), temperature, or cost and manufacturability limit the part. Glass and alumina score high on stiffness indices but cannot be chosen on that basis alone.

## Failure modes and the governing property

| Failure mode | Governing property | Typical check |
|---|---|---|
| Yielding (permanent set) | $\sigma_y$ | $\sigma_{\max} \le \sigma_y / N$, with $N$ the design factor |
| Ductile overload | $\sigma_u$, ductility | Net section stress below $\sigma_u$ with margin |
| Brittle fracture | $K_{IC}$, flaw size | Largest flaw below $a_c$ (see fracture section) |
| Fatigue | Endurance limit or S-N curve, notch factor, surface | Stress amplitude under the fatigue limit, or life from S-N |
| Creep rupture | Creep rate, activation energy, rupture time | Temperature below creep regime, or rupture life above design life |
| Buckling | $E$ and section stiffness $I$, not $\sigma_y$ | $P_{\text{cr}} = \dfrac{\pi^2 E I}{(K_e L)^2}$, with $K_e$ the effective length factor |
| Wear | Hardness, lubrication, surface contact stress | Contact pressure against hardness and lubrication regime |
| Stress corrosion cracking | $K_{ISCC}$, environment, tensile stress | Stress and environment both present, below yield |
| Galvanic, pitting, crevice corrosion | Electrode potential, chloride, geometry | See corrosion section |
| Thermal shock | $\sigma_f/(E\,\alpha)$ | Thermal stress against fracture strength |
| Low temperature brittleness (BCC steel) | Notch toughness vs temperature | Impact toughness at the lowest service temperature |
| Fretting | Contact stress, slip amplitude | Surface damage at contacts with small oscillation |

Notes: buckling depends on stiffness and geometry, not strength. A stiff, strong, slender column can still buckle at a load far below its yield load.

## Fracture toughness and critical crack size

- Stress intensity factor for a crack of length $a$ under stress $\sigma$: $K = Y\,\sigma\,\sqrt{\pi a}$. Units: MPa $\sqrt{\text{m}}$ with $\sigma$ in MPa and $a$ in m.
- Geometry factor $Y$: about 1.12 for an edge crack in a wide plate. Use 1.0 for a through crack in an infinite plate.
- Fracture occurs when $K = K_{IC}$. Critical crack length: $a_c = \dfrac{1}{\pi}\left(\dfrac{K_{IC}}{Y\sigma}\right)^2$.
- The formula holds for linear elastic behavior, plane strain, and a crack small compared with the part. It breaks for ductile metals with large plastic zones (use J-integral or COD methods) and for very thin sections.
- Plane strain validity (ASTM E399 criterion): crack length and thickness both at least $2.5\,(K_{IC}/\sigma_y)^2$. Thinner sections need a different test or fail the validity check.
- Example (6061-T6, $K_{IC} \approx 30$ MPa $\sqrt{\text{m}}$, $\sigma_y = 276$ MPa): minimum valid thickness is about 30 mm. Critical edge crack at $\sigma = 138$ MPa (half yield) and $Y = 1.12$ is about 12 mm.
- Example (soda-lime glass, $K_{IC} \approx 0.75$ MPa $\sqrt{\text{m}}$, $\sigma = 50$ MPa, $Y = 1.12$): critical edge crack is about 0.06 mm, which shows how little flaw glass tolerates.

Typical fracture toughness (MPa $\sqrt{\text{m}}$, typical):

| Material | $K_{IC}$ |
|---|---|
| Soda-lime glass | about 0.75 |
| Alumina | about 4 |
| 6061-T6 aluminum | about 30 |
| Ti-6Al-4V | about 50-100 |

- Strength and toughness are separate. High yield strength does not mean high $K_{IC}$.
- Crack growth under cyclic load follows the Paris law form $da/dN = C\,(\Delta K)^m$, with $C$ and $m$ material constants. The law holds only in the stable growth region.

## Fatigue basics

- Stress amplitude $\sigma_a = \dfrac{\sigma_{\max} - \sigma_{\min}}{2}$. Stress ratio $R = \sigma_{\min}/\sigma_{\max}$.
- Fatigue occurs in three stages: crack initiation (usually at a surface or inclusion), slow propagation, and final fracture.
- Steels (wrought, rotating beam test rule of thumb): endurance limit $S_e' \approx 0.5\,S_{ut}$ for $S_{ut} \le 1400$ MPa, and $S_e' \approx 700$ MPa for higher strength. It holds for smooth, polished specimens in air at room temperature. It breaks for notched, corroded, large, or hot parts.
- Marin factors reduce the endurance limit for the real part: surface finish, size, loading mode, temperature, reliability, and miscellaneous effects. Apply them multiplicatively to $S_e'$.
- Aluminum alloys and most non-ferrous metals have no clear endurance limit. Design to a stated finite life, commonly $10^8$ or $5 \times 10^8$ cycles.
- Mean stress: modified Goodman relation $\dfrac{\sigma_a}{S_e} + \dfrac{\sigma_m}{S_{ut}} = 1$. It holds for ductile metals. It breaks for brittle materials and for compressive mean stress, which is usually kinder.
- Stress concentration: $\sigma_{\max} = K_t\,\sigma_{\text{nominal}}$. Fatigue notch factor $K_f$ is lower than $K_t$ for notch-sensitive materials. Use $K_f$ for fatigue.
- Surface finish, corrosion, residual stress (shot peening helps), and notches can each cut fatigue life a lot.

## Creep

- Creep is time-dependent deformation under constant stress. Three stages: primary (decelerating), secondary (steady-state), and tertiary (accelerating to rupture).
- Regime rule: creep matters when the absolute temperature is above about 0.3 to 0.5 of the absolute melting temperature $T_m$ (in kelvin). It holds for metals and many ceramics. Polymers creep at much lower temperature, so use the glass transition temperature $T_g$ as the reference.
- Worked check: aluminum ($T_m \approx 933$ K) creeps at about 280 K to 470 K, which is about 7 C to 195 C. Lead ($T_m \approx 601$ K) is at about 0.49 $T_m$ at room temperature, so lead creeps at room temperature.
- Steady-state creep rate: $\dot{\varepsilon} = A\,\sigma^{n}\exp\!\left(-\dfrac{Q}{RT}\right)$, with $\dot{\varepsilon}$ in 1/s, $\sigma$ in MPa, $n$ the stress exponent (often 3 to 8 for metals), $Q$ the activation energy (J/mol), $R = 8.314$ J/(mol K), and $T$ in kelvin.
- Temperature ratio at the same stress: $\dfrac{\dot{\varepsilon}_2}{\dot{\varepsilon}_1} = \exp\!\left[\dfrac{Q}{R}\left(\dfrac{1}{T_1} - \dfrac{1}{T_2}\right)\right]$. Example: with $Q = 200$ kJ/mol, raising T from 900 K to 1000 K increases the creep rate by about 14.5 times.
- It breaks when the model is applied with Celsius instead of kelvin, when the microstructure changes (overaging, phase transformation), or when multiaxial stress or oxidation dominate.
- Design responses: higher melting point material, precipitate-strengthened alloys, lower stress, lower temperature, and wall thickness allowance for creep life.

## Galvanic series and galvanic corrosion

Qualitative ordering in seawater, from most anodic (least noble, corrodes first) to most cathodic (most noble):

- Magnesium and magnesium alloys
- Zinc
- Aluminum alloys
- Cadmium
- Mild steel and cast iron
- Lead and tin solder
- Brass, bronze, copper
- Nickel-copper alloys and stainless steel in the active (non-passive) state
- Passive stainless steel, titanium, nickel alloys
- Graphite
- Silver, gold, platinum

- Anode (the less noble metal) dissolves; cathode (the more noble) is protected. This holds when the two metals are electrically connected and share one electrolyte.
- Area ratio: a small anode touching a large cathode corrodes fast. A large anode with a small cathode corrodes slowly.
- Order within the noble group depends on alloy, condition (active or passive), flow, and temperature. Use ASTM G82 data for measured positions.

Corrosion rate (uniform attack, Faraday's law): mass loss rate $= \dfrac{i\,M}{n\,F}$, where $i$ is the current density (A/cm$^2$), $M$ the molar mass (g/mol), $n$ the valence, and $F = 96\,485$ C/mol. Penetration rate $= \dfrac{\text{mass loss rate}}{\rho}$. Example: iron ($M = 55.85$ g/mol, $n = 2$, $\rho = 7.87$ g/cm$^3$) at $i = 10$ $\mu$A/cm$^2$ corrodes at about 0.12 mm/year. For iron, each 1 $\mu$A/cm$^2$ is about 0.012 mm/year. The rule holds for uniform attack only. Pitting and crevice attack can perforate thin walls long before the average loss looks serious.

## Corrosion protection options

- Material choice: stainless steel (passive film), titanium, nickel alloys, or a more noble alloy in the same couple.
- Coatings: paint and powder coat, zinc (galvanizing), anodizing for aluminum, metallic plating. Holds while the coating is intact. A damaged coating over a large area can accelerate attack of exposed metal.
- Cathodic protection: sacrificial anodes (zinc, aluminum, or magnesium, chosen for the potential difference) or impressed current.
- Inhibitors in closed systems (for example in cooling water).
- Design: avoid dissimilar metal contact, or insulate it with a gasket or sleeve. Avoid crevices and lap joints, or seal them. Drain water. Keep the anode large relative to the cathode. Avoid stagnant areas.
- Stress corrosion cracking: use a material with a high threshold for the specific environment, reduce tensile residual stress (stress relief or peening), and control the environment (chlorides for stainless steel, for example).

## Heat treatment terms for steel

Plain carbon steel key temperatures: eutectoid (0.76 wt% C) transforms at about 727 C (A1). Hypoeutectoid steels need heating above the A3 line to fully austenitize. Hypereutectoid steels are heated above A1 (or above Acm). Exact A3 and Acm values depend on composition.

- Austenitizing: heating to the single-phase austenite region before cooling.
- Annealing (full): heat into austenite, cool slowly in the furnace. Soft, low stress, fine for forming and machining.
- Process annealing: heat below A1, cool in air. Relieves cold work between forming steps.
- Spheroidize annealing: long hold just below A1, makes carbides round. Improves machinability of high-carbon steel.
- Normalizing: heat into austenite, cool in still air. Finer, more uniform grains than full annealing.
- Quenching: rapid cooling from austenite (water, brine, oil, polymer). Forms martensite, very hard and brittle.
- Hardenability: the depth to which a steel hardens on quenching, measured with the Jominy end-quench test. Different from maximum hardness, which depends on carbon.
- Martempering: quench to just above the martensite start temperature, hold, then air cool. Reduces distortion.
- Austempering: quench to a temperature that forms bainite (a tough, fine mix of ferrite and carbide), hold until transformation finishes. Reduces distortion and cracking.
- Tempering: reheat martensite below A1 to trade hardness for toughness. Lower temperature keeps more hardness. Watch for temper embrittlement in some alloys.
- Stress relief: heat below A1 to reduce residual stress from welding or machining, with little change in microstructure.
- Case hardening: surface hardening with a tough core. Carburizing adds carbon at high temperature, then quench. Carbonitriding adds carbon and nitrogen. Nitriding adds nitrogen below A1 with no quench, so distortion is low. Induction hardening heats the surface only.
- Cryogenic treatment: cooling below room temperature to convert retained austenite. Used on tool steels, with limited effect.
- Precipitation hardening (aging): solution treat, quench, then age at moderate temperature so fine precipitates form. Example: 6061-T6 (solution treated and artificially aged). Work hardening (strain hardening) by cold work is a separate route. Recrystallization softens cold-worked metal.

## Checklists

Before trusting a material value:

- Confirm the source, the exact condition (alloy, temper, heat treat, and processing), and the test temperature.
- Check the direction: wood, composites, rolled plate, and extruded aluminum are anisotropic.
- Use the design minimum (specified or code value), not the typical value, for sizing.
- Check the environment: moisture (nylon, wood), chlorides, oxidation, and humidity.
- Confirm the value is in the right units before combining it with other numbers.

Before releasing a design:

- Check static stress against yield and ultimate with the design factor on the real load path.
- Check buckling for slender members, separately from strength.
- Check fatigue with the notch factor, surface finish, and Marin factors, and confirm the life target.
- Check the largest credible flaw against the critical crack size, and confirm the inspection can find flaws of that size.
- Check service temperature against the creep regime and the polymer glass transition.
- Check every metal-to-metal contact for galvanic pairing, and every crevice for drainage and seal.
- Check thermal strain at the highest and lowest service temperatures for constrained parts.
- Check that the heat treatment, condition, and temper are specified on the drawing.

## Sanity checks

- Stiffness: steel about 200 GPa, aluminum about 70 GPa, titanium about 110 GPa, most polymers 1 to 4 GPa. A polymer reading of 200 GPa is a unit error.
- Density: most metals 2000 to 9000 kg/m$^3$, polymers about 900 to 1600 kg/m$^3$. A value near 1000 for steel means a missing or wrong unit.
- Poisson's ratio: 0 to 0.5 for isotropic materials. Above 0.5 means an error.
- Yield strain for metals: $\sigma_y / E$, usually about 0.001 to 0.005. Steel at 370 MPa gives about 0.0018.
- Yield below ultimate: for ductile materials $\sigma_y < \sigma_u$. Equal values mean brittle or a bad entry.
- Fracture toughness: metals 20 to 200 MPa $\sqrt{\text{m}}$, ceramics and glass about 1 to 5. A ceramic at 50 is suspect.
- Critical crack length: a few mm to a few cm for metals at half yield. A critical crack of 1 m for an ordinary part is suspect.
- Creep: with absolute temperature (kelvin), creep is significant above about 0.4 $T_m$. A room-temperature creep failure of aluminum is not plausible. Lead creeping at room temperature is plausible.
- Galvanic corrosion: rates of 0.1 mm/year are typical for mild steel in mild water. Rates above 1 mm/year are a strong warning, not a normal value.
- Hall-Petch: halving grain diameter raises the $k_y d^{-1/2}$ term by about 41 percent ($\sqrt{2}$). The total yield change is smaller because $\sigma_0$ does not change.

## Further reference

- Callister and Rethwisch, Materials Science and Engineering: An Introduction (classic textbook; paid, by name only).
- Shigley's Mechanical Engineering Design (fatigue and design factors; paid, by name only).
- Ashby, Materials Selection in Mechanical Design (performance indices; paid, by name only).
- Roark's Formulas for Stress and Strain (beam and plate formulas; paid, by name only).
- Hertzberg, Deformation and Fracture Mechanics of Engineering Materials (fatigue and fracture; by name only).
- Dieter, Mechanical Metallurgy (plasticity and strengthening; by name only).
- ASM Handbook (volumes on properties, heat treating, and corrosion; by name only).
- Machinery's Handbook (tolerances and material data; by name only).
- ASTM E8 (tension testing of metals), ASTM E10 (Brinell hardness), ASTM E18 (Rockwell hardness), ASTM E399 (plane-strain fracture toughness), ASTM G82 (galvanic series development). Standards by name only.
