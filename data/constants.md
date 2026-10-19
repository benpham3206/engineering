# Constants

**Type:** data

The one place in the repo where a physical constant or conventional value is stated with its source. Lessons and reference sheets round these values freely, and the verifier checks that every rounding agrees with this table.

The first table holds the values. The second holds the prose scans: patterns the verifier runs over every file to catch a stated value that disagrees with the table, and to catch Earth values given without saying Earth.

The seven defining constants of the SI are exact by definition and do not depend on any planet or institution. Standard gravity and the standard atmosphere are conventions tied to Earth; use them only for Earth, and say so.

| Key | Quantity | Value | Unit | Uncertainty | Source | Locator |
|---|---|---|---|---|---|---|
| c | speed of light in vacuum | 299792458 | m/s | exact | bipm-si-9 | Table 1 |
| h_planck | Planck constant | 6.62607015e-34 | J s | exact | bipm-si-9 | Table 1 |
| e_charge | elementary charge | 1.602176634e-19 | C | exact | bipm-si-9 | Table 1 |
| k_boltzmann | Boltzmann constant | 1.380649e-23 | J/K | exact | bipm-si-9 | Table 1 |
| n_avogadro | Avogadro constant | 6.02214076e23 | mol^-1 | exact | bipm-si-9 | Table 1 |
| delta_nu_cs | caesium hyperfine frequency | 9192631770 | Hz | exact | bipm-si-9 | Table 1 |
| r_gas | molar gas constant | 8.314462618 | J/mol K | exact (product of N_A and k) | codata-2022 | value page "r" |
| sigma_sb | Stefan-Boltzmann constant | 5.670374419e-8 | W/m^2 K^4 | exact (derived from exact constants) | codata-2022 | value page "sigma" |
| g_newton | Newtonian constant of gravitation | 6.67430e-11 | m^3/kg s^2 | 0.00015e-11 | codata-2022 | value page "bg" |
| t_celsius_zero | kelvin temperature of 0 degrees Celsius | 273.15 | K | exact (definition of the Celsius scale) | bipm-si-9 | section 2.3.1, Celsius temperature |
| g_standard | standard acceleration of gravity (Earth convention) | 9.80665 | m/s^2 | exact (conventional) | codata-2022 | value page "gn" |
| p_standard | standard atmosphere (Earth convention) | 101325 | Pa | exact (conventional) | codata-2022 | value page "stdatm" |
| m_electron | electron mass | 9.1093837139e-31 | kg | 0.0000000028e-31 | codata-2022 | value page "me" |
| gm_earth | geocentric gravitational parameter GM of Earth (Earth value) | 3.98600435507e14 | m^3/s^2 | as published, 12 digits | jpl-astro-par | Planetary Masses table, row "Earth", 398600.435507 km^3/s^2, from ephemeris DE440 |
| r_earth_mean | volumetric mean radius of Earth (Earth value) | 6371.000 | km | as published, to 1 m | nasa-earth-factsheet | row "Volumetric mean radius (km)" |

Prose scans. `v` is the captured number, in the scan's unit. `Context` must also match the line for the scan to apply, and `Unless` skips the line. `Planet: yes` means the line must also say Earth or standard.

| Key | Pattern | Unit | Equals | Context | Unless | Planet |
|---|---|---|---|---|---|---|
| g_standard | `(?<![\d.])(?P<v>9\.8(?:[01]\d*)?)\s*m/s` | m/s^2 | g_standard | | | yes |
| g_standard | `(?<![\d.])(?P<v>32\.[12]\d*)\s*ft/s` | ft/s^2 | g_standard | | | yes |
| p_standard | `(?<![\d.])(?P<v>101\d{3}(?:\.\d+)?)\s*Pa\b` | Pa | p_standard | `(?i)atm\|sea level` | | yes |
| p_standard | `(?<![\d.])(?P<v>10[01](?:\.\d+)?)\s*kPa\b` | kPa | p_standard | `(?i)atm\|sea level` | `(?i)gauge` | yes |
| p_standard | `(?<![\d.])(?P<v>14\.[67]\d*)\s*psi\b` | psi | p_standard | `(?i)atm\|sea level` | | yes |
| unit:psi | `\b1\s*psi\s*=\s*(?P<v>\d+(?:\.\d+)?)\s*Pa\b` | Pa | unit:psi | | | |
| unit:hp | `\b1\s*hp\s*=[^=]*=\s*(?P<v>\d+(?:\.\d+)?)\s*W\b` | W | unit:hp | | | |
| unit:hp | `\b1\s*hp\s*=\s*(?P<v>\d+(?:\.\d+)?)\s*W\b` | W | unit:hp | | | |
| unit:MPa | `\b1\s*MPa\b[^.]{0,30}?(?P<v>14[45](?:\.\d+)?)\s*psi\b` | psi | unit:MPa | | | |
