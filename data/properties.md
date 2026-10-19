# Properties

**Type:** data

Material and fluid properties that more than one file uses, each with its conditions and source. A row with a `Range` is a typical engineering value that varies between grades or samples; the verifier accepts any rounded value inside the range. A row without a range is a measured or formulated value; the verifier accepts it only at the precision it is printed.

| Key | Property | Value | Unit | Range | Conditions | Source | Locator |
|---|---|---|---|---|---|---|---|
| water.density.20C | density of liquid water | 998.21 | kg/m^3 | | 20 C, 101.325 kPa (IAPWS-95) | nist-webbook | water, isothermal properties at 20 C |
| water.density.nominal | density of liquid water, rounded for hand calculation | 1000 | kg/m^3 | 995..1000 | 0 C to 30 C, near 1 atm | nist-webbook | water, isothermal properties from 0 C to 30 C |
| water.psat.20C | vapour (saturation) pressure of water | 2.3393 | kPa | | 20 C (IAPWS-95) | nist-webbook | water, saturation properties at 20 C |
