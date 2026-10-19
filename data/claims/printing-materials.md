# Printing materials claims

**Type:** data

Supplier-reported 3D printing material values and document roles. Typical ranges compare the named sheets and are not design allowables.

### tds-and-sds-roles
- Claim: A technical data sheet reports product property values and test methods, while a safety data sheet communicates chemical hazard, composition, handling, and emergency information.
- Values: product properties; test methods; chemical hazards; composition; handling; emergency information
- Layer: durable
- Status: verified-2
- Sources: pm-polylite-pla-tds (Physical properties, mechanical properties, and thermal properties tables, "Density"; "Tensile strength"; "Heat deflection temperature"); ccohs-sds ("What is a safety data sheet (SDS)?": "summary documents that provide information about the hazards of a product and advice about safety precautions"; section list: "3 Composition/Information on ingredients", "7 Handling and storage", "Emergency telephone number")
- Checked: agent, 2026-10-19, read both public sources and matched their stated contents

### pla-orientation
- Claim: PolyLite PLA reports tensile strength at 52.3 MPa in XY and 40.5 MPa in Z; UltiMaker explains that upright Z specimens test interlayer adhesion and typically have the lowest strength in FFF.
- Values: 52.3; 40.5
- Layer: dated
- Status: verified-2
- As of: 2026
- Review by: 2028-10-19
- Sources: pm-polylite-pla-tds (Mechanical properties, "Tensile strength (X-Y)" and "Tensile strength (Z)", "52.3 ± 0.3 MPa" and "40.5 ± 0.5 MPa"); um-pla-tds (Print orientation, "the upright samples (Z direction) give information on the strength of the interlayer adhesion" and "interlayer strength (Z) has the lowest strength in FFF")
- Checked: agent, 2026-10-19, read both TDS texts and matched the values and orientation statement

### impact-methods
- Claim: The supplied PolyLite PETG and UltiMaker PETG sheets both report notched Charpy impact strength, and the UltiMaker sheet describes a printed notched specimen.
- Values: notched Charpy
- Layer: dated
- Status: verified-2
- As of: 2026
- Review by: 2028-10-19
- Sources: pm-polylite-petg-tds (Mechanical properties, "Notched Charpy impact strength (X-Y)", "2.6 ± 0.2 kJ/m2"); um-petg-tds (Mechanical properties, "Charpy impact strength (at 23 °C)", "ISO 179-1 / 1eB (notched)", and Notes, "Charpy: 80 x 10 x 4 mm with printed Notch")
- Checked: agent, 2026-10-19, read both TDS texts and matched the impact method descriptions

### pla-typical-ranges
- Claim: The listed PolyLite PLA and UltiMaker PLA sheets give these typical ranges across the two products: density 1170 to 1240 kg/m^3; XY tensile strength at break 45.5 to 52.3 MPa; XY tensile modulus 3.25 to 3.43 GPa; XY elongation at break 6.3 to 7.8%; HDT near 0.45 MPa 58.8 to 60 °C; and glass transition 59.1 to 61 °C.
- Values: 1170-1240; 45.5-52.3; 3.25-3.43; 6.3-7.8; 58.8-60; 59.1-61
- Layer: dated
- Status: verified-2
- As of: 2026
- Review by: 2028-10-19
- Sources: pm-polylite-pla-tds (Physical properties, "Density", "1.17 g/cm3"; Thermal properties, "Glass transition temperature", "61 °C", and "Heat deflection temperature", "60 °C at 0.45 MPa"; Mechanical properties, XY values "3426.9 ± 64.8 MPa", "52.3 ± 0.3 MPa", and "6.3 ± 0.6 %"); um-pla-tds (Mechanical properties, XY values "3250 ± 119 MPa", "45.5 ± 1.1 MPa", and "7.8 ± 1.2%"; Thermal properties, "58.8 ± 0.4 °C", "59.1 °C", and "1.24 g/cm3")
- Checked: agent, 2026-10-19, read both TDS texts, converted density and modulus units, and bounded each range from the two reported typical values

### petg-typical-ranges
- Claim: The listed PolyLite PETG and UltiMaker PETG sheets give these typical ranges across the two products: density 1250 to 1270 kg/m^3; XY tensile strength at break 38.5 to 50.8 MPa; XY tensile modulus 1.94 to 2.12 GPa; XY elongation at break 7.6 to 8.4%; HDT near 0.45 MPa 76.2 to 78 °C; and glass transition 77.4 to 81 °C.
- Values: 1250-1270; 38.5-50.8; 1.94-2.12; 7.6-8.4; 76.2-78; 77.4-81
- Layer: dated
- Status: verified-2
- As of: 2026
- Review by: 2028-10-19
- Sources: pm-polylite-petg-tds (Physical properties, "Density", "1.25 g/cm3"; Thermal properties, "Glass transition temperature", "81 °C", and "Heat deflection temperature", "78 °C at 0.45 MPa"; Mechanical properties, XY values "2116.8 ± 68.1 MPa", "50.8 ± 0.9 MPa", and "8.4 ± 1.7 %"); um-petg-tds (Mechanical properties, XY values "1939 ± 28 MPa", "38.5 ± 1.4 MPa", and "7.6 ± 0.2%"; Thermal properties, "76.2 ± 0.8 °C", "77.4 °C", and "1.27 g/cm3")
- Checked: agent, 2026-10-19, read both TDS texts, converted density and modulus units, and bounded each range from the two reported typical values

### abs-typical-ranges
- Claim: The listed PolyLite ABS and UltiMaker ABS sheets support density 1100 to 1120 kg/m^3, HDT near 0.45 MPa 86.6 to 100 °C, and glass transition 100.5 to 101 °C; their tensile values are excluded from this comparison.
- Values: 1100-1120; 86.6-100; 100.5-101
- Layer: dated
- Status: verified-2
- As of: 2026
- Review by: 2028-10-19
- Sources: pm-polylite-abs-tds (Physical properties, "Density", "1.12 g/cm3"; Thermal properties, "Glass transition temperature", "101 °C", and "Heat deflection temperature", "100 °C at 0.45 MPa"); um-abs-tds (Mechanical properties, "Tensile stress at break"; Thermal properties, "86.6 ± 0.4 °C", "100.5 °C", and "1.1 g/cm3")
- Checked: agent, 2026-10-19, read both TDS texts and compared density, HDT load, and glass transition values

### abs-repeated-tensile-row
- Claim: The PolyLite ABS sheet prints two XY tensile-strength rows, 33.4 MPa and 29.7 MPa, then reports 29.7 MPa for Z, so its tensile figures are excluded from the comparison.
- Values: 33.4; 29.7
- Layer: dated
- Status: verified-1
- As of: 2026
- Review by: 2028-10-19
- Sources: pm-polylite-abs-tds (Mechanical properties, consecutive "Tensile strength (X-Y)" rows and "Tensile strength (Z)" row, "33.4 ± 0.6 MPa", "29.7 ± 0.3 MPa", and "29.7 ± 0.3 MPa")
- Checked: agent, 2026-10-19, read the mechanical properties table and confirmed the repeated labels and value

### nylon-typical-ranges
- Claim: The listed PolyMide CoPA and UltiMaker Nylon sheets support density 1120 to 1140 kg/m^3; XY tensile strength at break 40.4 to 78.0 MPa; XY tensile modulus 2.33 to 2.70 GPa; HDT near 0.45 MPa 89.2 to 111 °C; and glass transition 55.1 to 66 °C.
- Values: 1120-1140; 40.4-78.0; 2.33-2.70; 89.2-111; 55.1-66
- Layer: dated
- Status: verified-2
- As of: 2026
- Review by: 2028-10-19
- Sources: pm-polymide-copa-tds (Physical properties, "Density", "1.12 g/cm3"; Thermal properties, "Glass transition temperature", "66 °C", and "Heat deflection temperature", "111 °C at 0.45 MPa"; Dry Status mechanical properties, XY values "2703 ± 259 MPa" and "78.0 ± 0.7 MPa"); um-nylon-tds (Mechanical properties, XY values "2331 ± 55 MPa" and "40.4 ± 2.2 MPa"; Thermal properties, "89.2 ± 5.6 °C", "55.1 °C", and "1.14 g/cm3")
- Checked: agent, 2026-10-19, read both TDS texts, converted density and modulus units, and bounded each range from the two reported typical values

### nylon-dry-and-wet
- Claim: PolyMide CoPA reports dry XY tensile strength of 78.0 MPa, wet XY tensile strength of 34.3 MPa, and wet Z tensile strength of 13.7 MPa; wet specimens were annealed and immersed in water and had 6.16% average moisture content.
- Values: 78.0; 34.3; 13.7; 6.16
- Layer: dated
- Status: verified-1
- As of: 2026
- Review by: 2028-10-19
- Sources: pm-polymide-copa-tds (Dry Status and Wet Status mechanical properties, "78.0 ± 0.7 MPa", "34.3 ± 2.5 MPa", and "13.7 ± 1.2 MPa"; specimen notes, annealing, drying, immersion, and "6.16%")
- Checked: agent, 2026-10-19, read the dry and wet tables and specimen notes and matched the reported values

### pc-typical-ranges
- Claim: The listed PolyLite PC and UltiMaker PC sheets give these typical ranges across the two products: density 1180 to 1200 kg/m^3; XY tensile strength at break 43.2 to 69.1 MPa; XY tensile modulus 2.39 to 2.50 GPa; XY elongation at break 4.8 to 9.2%; HDT near 0.45 MPa 104.5 to 111 °C; and glass transition 107.7 to 113 °C.
- Values: 1180-1200; 43.2-69.1; 2.39-2.50; 4.8-9.2; 104.5-111; 107.7-113
- Layer: dated
- Status: verified-2
- As of: 2026
- Review by: 2028-10-19
- Sources: pm-polylite-pc-tds (Physical properties, "Density", "1.19 g/cm3"; Thermal properties, "Glass transition temperature", "113 °C", and "Heat deflection temperature", "111 °C at 0.45 MPa"; Mechanical properties, XY values "2497 ± 154 MPa", "69.1 ± 3.0 MPa", and "4.8 ± 0.9 %"); um-pc-tds (Mechanical properties, XY values "2394 ± 98 MPa", "43.2 ± 1.5 MPa", and "9.2 ± 0.9%"; Thermal properties, "104.5 ± 0.7 °C", "107.7 °C", and "1.18-1.20 g/cm3")
- Checked: agent, 2026-10-19, read both TDS texts, converted density and modulus units, and bounded each range from the two reported typical values

### tpu-typical-ranges
- Claim: The listed PolyFlex TPU95 and UltiMaker TPU 95A sheets report density values spanning 1200 to 1240 kg/m^3.
- Values: 1200-1240
- Layer: dated
- Status: verified-2
- As of: 2026
- Review by: 2028-10-19
- Sources: pm-polyflex-tpu95-tds (Physical properties, "Density", "1.20-1.24 g/cm3 at 23 °C"); um-tpu-tds (Other properties, specific gravity "1.22 g / cm3")
- Checked: agent, 2026-10-19, read both TDS texts and converted the supplier values to kg/m^3

### tpu-modulus-flag
- Claim: The PolyFlex TPU95 sheet labels 33.6 MPa as Young's modulus, but this entry is excluded from comparison as directed because it is not suitable for use as a modulus value.
- Values: 33.6 MPa
- Layer: dated
- Status: verified-1
- As of: 2026
- Review by: 2028-10-19
- Sources: pm-polyflex-tpu95-tds (Mechanical properties, "Young's modulus (X-Y)", "33.6 ± 0.9 MPa", and stress rows at 100%, 200%, 300%, and 400% strain)
- Checked: agent, 2026-10-19, read the table and followed the packet's exclusion instruction

### pla-density-range
- Claim: PolyLite PLA and UltiMaker PLA report density values spanning 1170 to 1240 kg/m^3.
- Values: 1170-1240
- Layer: dated
- Status: verified-2
- As of: 2026
- Review by: 2028-10-19
- Sources: pm-polylite-pla-tds (Physical properties, Density, "1.17 g/cm3"); um-pla-tds (Other properties, specific gravity, "1.24 g/cm3")
- Checked: agent, 2026-10-19, read both values and converted to kg/m^3

### pla-tensile-strength-range
- Claim: PolyLite PLA and UltiMaker PLA report XY tensile strength at break spanning 45.5 to 52.3 MPa.
- Values: 45.5-52.3
- Layer: dated
- Status: verified-2
- As of: 2026
- Review by: 2028-10-19
- Sources: pm-polylite-pla-tds (Mechanical properties, XY tensile strength, "52.3 ± 0.3 MPa"); um-pla-tds (Mechanical properties, XY tensile stress at break, "45.5 ± 1.1 MPa")
- Checked: agent, 2026-10-19, read both XY break values and bounded the range

### pla-tensile-modulus-range
- Claim: PolyLite PLA and UltiMaker PLA report XY tensile modulus spanning 3.25 to 3.43 GPa.
- Values: 3.25-3.43
- Layer: dated
- Status: verified-2
- As of: 2026
- Review by: 2028-10-19
- Sources: pm-polylite-pla-tds (Mechanical properties, XY Young's modulus, "3426.9 ± 64.8 MPa"); um-pla-tds (Mechanical properties, XY tensile modulus, "3250 ± 119 MPa")
- Checked: agent, 2026-10-19, read both values and converted to GPa

### pla-elongation-range
- Claim: PolyLite PLA and UltiMaker PLA report XY elongation at break spanning 6.3 to 7.8%.
- Values: 6.3-7.8
- Layer: dated
- Status: verified-2
- As of: 2026
- Review by: 2028-10-19
- Sources: pm-polylite-pla-tds (Mechanical properties, XY elongation at break, "6.3 ± 0.6 %"); um-pla-tds (Mechanical properties, XY elongation at break, "7.8 ± 1.2%")
- Checked: agent, 2026-10-19, read both XY values and bounded the range

### pla-hdt-range
- Claim: PolyLite PLA and UltiMaker PLA report HDT near 0.45 MPa spanning 58.8 to 60 °C.
- Values: 58.8-60
- Layer: dated
- Status: verified-2
- As of: 2026
- Review by: 2028-10-19
- Sources: pm-polylite-pla-tds (Thermal properties, HDT at 0.45 MPa, "60 °C"); um-pla-tds (Thermal properties, HDT at 0.455 MPa, "58.8 ± 0.4 °C")
- Checked: agent, 2026-10-19, read both values and compared the stated loads

### pla-glass-transition-range
- Claim: PolyLite PLA and UltiMaker PLA report glass transition spanning 59.1 to 61 °C.
- Values: 59.1-61
- Layer: dated
- Status: verified-2
- As of: 2026
- Review by: 2028-10-19
- Sources: pm-polylite-pla-tds (Thermal properties, glass transition, "61 °C"); um-pla-tds (Thermal properties, glass transition, "59.1 °C")
- Checked: agent, 2026-10-19, read both values and bounded the range

### petg-density-range
- Claim: PolyLite PETG and UltiMaker PETG report density spanning 1250 to 1270 kg/m^3.
- Values: 1250-1270
- Layer: dated
- Status: verified-2
- As of: 2026
- Review by: 2028-10-19
- Sources: pm-polylite-petg-tds (Physical properties, density, "1.25 g/cm3"); um-petg-tds (Other properties, specific gravity, "1.27 g/cm3")
- Checked: agent, 2026-10-19, read both values and converted to kg/m^3

### petg-tensile-strength-range
- Claim: PolyLite PETG and UltiMaker PETG report XY tensile strength at break spanning 38.5 to 50.8 MPa.
- Values: 38.5-50.8
- Layer: dated
- Status: verified-2
- As of: 2026
- Review by: 2028-10-19
- Sources: pm-polylite-petg-tds (Mechanical properties, XY tensile strength, "50.8 ± 0.9 MPa"); um-petg-tds (Mechanical properties, XY tensile stress at break, "38.5 ± 1.4 MPa")
- Checked: agent, 2026-10-19, read both XY break values and bounded the range

### petg-tensile-modulus-range
- Claim: PolyLite PETG and UltiMaker PETG report XY tensile modulus spanning 1.94 to 2.12 GPa.
- Values: 1.94-2.12
- Layer: dated
- Status: verified-2
- As of: 2026
- Review by: 2028-10-19
- Sources: pm-polylite-petg-tds (Mechanical properties, XY Young's modulus, "2116.8 ± 68.1 MPa"); um-petg-tds (Mechanical properties, XY tensile modulus, "1939 ± 28 MPa")
- Checked: agent, 2026-10-19, read both values and converted to GPa

### petg-elongation-range
- Claim: PolyLite PETG and UltiMaker PETG report XY elongation at break spanning 7.6 to 8.4%.
- Values: 7.6-8.4
- Layer: dated
- Status: verified-2
- As of: 2026
- Review by: 2028-10-19
- Sources: pm-polylite-petg-tds (Mechanical properties, XY elongation at break, "8.4 ± 1.7 %"); um-petg-tds (Mechanical properties, XY elongation at break, "7.6 ± 0.2%")
- Checked: agent, 2026-10-19, read both XY values and bounded the range

### petg-hdt-range
- Claim: PolyLite PETG and UltiMaker PETG report HDT near 0.45 MPa spanning 76.2 to 78 °C.
- Values: 76.2-78
- Layer: dated
- Status: verified-2
- As of: 2026
- Review by: 2028-10-19
- Sources: pm-polylite-petg-tds (Thermal properties, HDT at 0.45 MPa, "78 °C"); um-petg-tds (Thermal properties, HDT at 0.455 MPa, "76.2 ± 0.8 °C")
- Checked: agent, 2026-10-19, read both values and compared the stated loads

### petg-glass-transition-range
- Claim: PolyLite PETG and UltiMaker PETG report glass transition spanning 77.4 to 81 °C.
- Values: 77.4-81
- Layer: dated
- Status: verified-2
- As of: 2026
- Review by: 2028-10-19
- Sources: pm-polylite-petg-tds (Thermal properties, glass transition, "81 °C"); um-petg-tds (Thermal properties, glass transition, "77.4 °C")
- Checked: agent, 2026-10-19, read both values and bounded the range

### abs-density-range
- Claim: PolyLite ABS and UltiMaker ABS report density spanning 1100 to 1120 kg/m^3.
- Values: 1100-1120
- Layer: dated
- Status: verified-2
- As of: 2026
- Review by: 2028-10-19
- Sources: pm-polylite-abs-tds (Physical properties, density, "1.12 g/cm3"); um-abs-tds (Other properties, specific gravity, "1.1 g/cm3")
- Checked: agent, 2026-10-19, read both values and converted to kg/m^3

### abs-hdt-range
- Claim: PolyLite ABS and UltiMaker ABS report HDT near 0.45 MPa spanning 86.6 to 100 °C.
- Values: 86.6-100
- Layer: dated
- Status: verified-2
- As of: 2026
- Review by: 2028-10-19
- Sources: pm-polylite-abs-tds (Thermal properties, HDT at 0.45 MPa, "100 °C"); um-abs-tds (Thermal properties, HDT at 0.455 MPa, "86.6 ± 0.4 °C")
- Checked: agent, 2026-10-19, read both values and compared the stated loads

### abs-glass-transition-range
- Claim: PolyLite ABS and UltiMaker ABS report glass transition spanning 100.5 to 101 °C.
- Values: 100.5-101
- Layer: dated
- Status: verified-2
- As of: 2026
- Review by: 2028-10-19
- Sources: pm-polylite-abs-tds (Thermal properties, glass transition, "101 °C"); um-abs-tds (Thermal properties, glass transition, "100.5 °C")
- Checked: agent, 2026-10-19, read both values and bounded the range

### nylon-density-range
- Claim: PolyMide CoPA and UltiMaker Nylon report density spanning 1120 to 1140 kg/m^3.
- Values: 1120-1140
- Layer: dated
- Status: verified-2
- As of: 2026
- Review by: 2028-10-19
- Sources: pm-polymide-copa-tds (Physical properties, density, "1.12 g/cm3"); um-nylon-tds (Other properties, specific gravity, "1.14 g/cm3")
- Checked: agent, 2026-10-19, read both values and converted to kg/m^3

### nylon-tensile-strength-range
- Claim: PolyMide CoPA and UltiMaker Nylon report XY tensile strength at break spanning 40.4 to 78.0 MPa.
- Values: 40.4-78
- Layer: dated
- Status: verified-2
- As of: 2026
- Review by: 2028-10-19
- Sources: pm-polymide-copa-tds (Dry Status mechanical properties, XY tensile strength, "78.0 ± 0.7 MPa"); um-nylon-tds (Mechanical properties, XY tensile stress at break, "40.4 ± 2.2 MPa")
- Checked: agent, 2026-10-19, read both XY break values and bounded the range

### nylon-tensile-modulus-range
- Claim: PolyMide CoPA and UltiMaker Nylon report XY tensile modulus spanning 2.33 to 2.70 GPa.
- Values: 2.33-2.70
- Layer: dated
- Status: verified-2
- As of: 2026
- Review by: 2028-10-19
- Sources: pm-polymide-copa-tds (Dry Status mechanical properties, XY Young's modulus, "2703 ± 259 MPa"); um-nylon-tds (Mechanical properties, XY tensile modulus, "2331 ± 55 MPa")
- Checked: agent, 2026-10-19, read both values and converted to GPa

### nylon-hdt-range
- Claim: PolyMide CoPA and UltiMaker Nylon report HDT near 0.45 MPa spanning 89.2 to 111 °C.
- Values: 89.2-111
- Layer: dated
- Status: verified-2
- As of: 2026
- Review by: 2028-10-19
- Sources: pm-polymide-copa-tds (Thermal properties, HDT at 0.45 MPa, "111 °C"); um-nylon-tds (Thermal properties, HDT at 0.455 MPa, "89.2 ± 5.6 °C")
- Checked: agent, 2026-10-19, read both values and compared the stated loads

### nylon-glass-transition-range
- Claim: PolyMide CoPA and UltiMaker Nylon report glass transition spanning 55.1 to 66 °C.
- Values: 55.1-66
- Layer: dated
- Status: verified-2
- As of: 2026
- Review by: 2028-10-19
- Sources: pm-polymide-copa-tds (Thermal properties, glass transition, "66 °C"); um-nylon-tds (Thermal properties, glass transition, "55.1 °C")
- Checked: agent, 2026-10-19, read both values and bounded the range

### pc-density-range
- Claim: PolyLite PC and UltiMaker PC report density spanning 1180 to 1200 kg/m^3.
- Values: 1180-1200
- Layer: dated
- Status: verified-2
- As of: 2026
- Review by: 2028-10-19
- Sources: pm-polylite-pc-tds (Physical properties, density, "1.19 g/cm3"); um-pc-tds (Other properties, specific gravity, "1.18-1.20 g/cm3")
- Checked: agent, 2026-10-19, read both values and converted to kg/m^3

### pc-tensile-strength-range
- Claim: PolyLite PC and UltiMaker PC report XY tensile strength at break spanning 43.2 to 69.1 MPa.
- Values: 43.2-69.1
- Layer: dated
- Status: verified-2
- As of: 2026
- Review by: 2028-10-19
- Sources: pm-polylite-pc-tds (Mechanical properties, XY tensile strength, "69.1 ± 3.0 MPa"); um-pc-tds (Mechanical properties, XY tensile stress at break, "43.2 ± 1.5 MPa")
- Checked: agent, 2026-10-19, read both XY break values and bounded the range

### pc-tensile-modulus-range
- Claim: PolyLite PC and UltiMaker PC report XY tensile modulus spanning 2.39 to 2.50 GPa.
- Values: 2.39-2.50
- Layer: dated
- Status: verified-2
- As of: 2026
- Review by: 2028-10-19
- Sources: pm-polylite-pc-tds (Mechanical properties, XY Young's modulus, "2497 ± 154 MPa"); um-pc-tds (Mechanical properties, XY tensile modulus, "2394 ± 98 MPa")
- Checked: agent, 2026-10-19, read both values and converted to GPa

### pc-elongation-range
- Claim: PolyLite PC and UltiMaker PC report XY elongation at break spanning 4.8 to 9.2%.
- Values: 4.8-9.2
- Layer: dated
- Status: verified-2
- As of: 2026
- Review by: 2028-10-19
- Sources: pm-polylite-pc-tds (Mechanical properties, XY elongation at break, "4.8 ± 0.9 %"); um-pc-tds (Mechanical properties, XY elongation at break, "9.2 ± 0.9%")
- Checked: agent, 2026-10-19, read both XY values and bounded the range

### pc-hdt-range
- Claim: PolyLite PC and UltiMaker PC report HDT near 0.45 MPa spanning 104.5 to 111 °C.
- Values: 104.5-111
- Layer: dated
- Status: verified-2
- As of: 2026
- Review by: 2028-10-19
- Sources: pm-polylite-pc-tds (Thermal properties, HDT at 0.45 MPa, "111 °C"); um-pc-tds (Thermal properties, HDT at 0.455 MPa, "104.5 ± 0.7 °C")
- Checked: agent, 2026-10-19, read both values and compared the stated loads

### pc-glass-transition-range
- Claim: PolyLite PC and UltiMaker PC report glass transition spanning 107.7 to 113 °C.
- Values: 107.7-113
- Layer: dated
- Status: verified-2
- As of: 2026
- Review by: 2028-10-19
- Sources: pm-polylite-pc-tds (Thermal properties, glass transition, "113 °C"); um-pc-tds (Thermal properties, glass transition, "107.7 °C")
- Checked: agent, 2026-10-19, read both values and bounded the range

### tpu-density-range
- Claim: PolyFlex TPU95 and UltiMaker TPU 95A report density spanning 1200 to 1240 kg/m^3.
- Values: 1200-1240
- Layer: dated
- Status: verified-2
- As of: 2026
- Review by: 2028-10-19
- Sources: pm-polyflex-tpu95-tds (Physical properties, density, "1.20-1.24 g/cm3"); um-tpu-tds (Other properties, specific gravity, "1.22 g/cm3")
- Checked: agent, 2026-10-19, read both values and converted to kg/m^3
