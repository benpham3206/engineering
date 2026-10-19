# Measurement reference

**Type:** reference

Measurement is the process of giving a physical quantity a number, a unit, and an uncertainty. Engineers need all three, because a value without them cannot be trusted or compared.

A lookup sheet for units, SI rules, uncertainty, significant figures, sensors, thermocouples, strain gauges, sampling, and experiment design, for an engineer who needs a value or a rule in the middle of a measurement task.

## Principles

- Every number carries a unit and an uncertainty. A value without both is not yet a result.
- The SI base units are fixed by exact constants (2019 revision). Exact conversions stay exact; anything else needs its stated uncertainty.
- Averaging reduces random error only. It does not remove systematic error (bias, zero offset, wrong calibration).
- Independent uncertainties combine by root-sum-square (RSS). Linear addition gives a bound, not an estimate.
- Resolution limits what you can read. Calibration and bias limit how close a value is to the true one. Do not confuse them.
- Sample at more than twice the highest frequency you need. Aliasing cannot be undone after sampling.
- Traceability is an unbroken chain of comparisons, each with a stated uncertainty.
- Check every result for dimensions, sign, limits, and order of magnitude before trusting it.

## 1. Units and dimensional analysis

### 1.1 SI base units (2019 definitions)

| Quantity | Unit (symbol) | Plain words | Fixed exact value |
|---|---|---|---|
| time | second (s) | a fixed number of cycles of the cesium-133 hyperfine transition | $\Delta\nu_{\text{Cs}} = 9\,192\,631\,770$ Hz |
| length | meter (m) | the distance light travels in a fixed fraction of a second | $c = 299\,792\,458$ m/s |
| mass | kilogram (kg) | fixed through the Planck constant | $h = 6.62607015 \times 10^{-34}$ J s |
| electric current | ampere (A) | a fixed number of elementary charges per second | $e = 1.602176634 \times 10^{-19}$ C |
| temperature | kelvin (K) | fixed through the energy per kelvin of thermal motion | $k_B = 1.380649 \times 10^{-23}$ J/K |
| amount of substance | mole (mol) | a fixed count of entities | $N_A = 6.02214076 \times 10^{23}$ mol$^{-1}$ |
| luminous intensity | candela (cd) | light power at 540 THz scaled by a fixed efficacy | $K_{\text{cd}} = 683$ lm/W |

- Standard gravity $g_0 = 9.80665$ m/s$^2$ is a defined constant, not a base unit. Local gravity differs (about 9.78 to 9.83 m/s$^2$ at sea level across Earth; typical).
- Dimension symbols: $L$ (length), $M$ (mass), $T$ (time), $I$ (current), $\Theta$ (temperature), $N$ (amount), $J$ (luminous intensity).

### 1.2 Named SI derived units

| Quantity | Unit | Symbol | Base units | Equivalent |
|---|---|---|---|---|
| frequency | hertz | Hz | s$^{-1}$ | cycles per second |
| force, weight | newton | N | kg m s$^{-2}$ | |
| pressure, stress | pascal | Pa | kg m$^{-1}$ s$^{-2}$ | N/m$^2$ |
| energy, work, heat | joule | J | kg m$^2$ s$^{-2}$ | N m |
| power | watt | W | kg m$^2$ s$^{-3}$ | J/s |
| electric charge | coulomb | C | A s | |
| electric potential | volt | V | kg m$^2$ s$^{-3}$ A$^{-1}$ | W/A |
| resistance | ohm | $\Omega$ | kg m$^2$ s$^{-3}$ A$^{-2}$ | V/A |
| conductance | siemens | S | kg$^{-1}$ m$^{-2}$ s$^3$ A$^2$ | A/V |
| capacitance | farad | F | kg$^{-1}$ m$^{-2}$ s$^4$ A$^2$ | C/V |
| inductance | henry | H | kg m$^2$ s$^{-2}$ A$^{-2}$ | Wb/A |
| magnetic flux | weber | Wb | kg m$^2$ s$^{-2}$ A$^{-1}$ | V s |
| magnetic flux density | tesla | T | kg s$^{-2}$ A$^{-1}$ | Wb/m$^2$ |
| absorbed dose | gray | Gy | m$^2$ s$^{-2}$ | J/kg |
| dose equivalent | sievert | Sv | m$^2$ s$^{-2}$ | J/kg (weighted) |
| activity | becquerel | Bq | s$^{-1}$ | |
| catalytic activity | katal | kat | mol s$^{-1}$ | |
| luminous flux | lumen | lm | cd sr | |
| illuminance | lux | lx | cd sr m$^{-2}$ | lm/m$^2$ |

- Radian (rad) and steradian (sr) are dimensionless (m/m and m$^2$/m$^2$).
- Degree Celsius: $t\ [\text{°C}] = T\ [\text{K}] - 273.15$ exactly. A temperature difference of 1 °C equals 1 K.

### 1.3 SI prefixes (exact powers of ten)

| Prefix | Symbol | Factor | Prefix | Symbol | Factor |
|---|---|---|---|---|---|
| quetta | Q | $10^{30}$ | quecto | q | $10^{-30}$ |
| ronna | R | $10^{27}$ | ronto | r | $10^{-27}$ |
| yotta | Y | $10^{24}$ | yocto | y | $10^{-24}$ |
| zetta | Z | $10^{21}$ | zepto | z | $10^{-21}$ |
| exa | E | $10^{18}$ | atto | a | $10^{-18}$ |
| peta | P | $10^{15}$ | femto | f | $10^{-15}$ |
| tera | T | $10^{12}$ | pico | p | $10^{-12}$ |
| giga | G | $10^{9}$ | nano | n | $10^{-9}$ |
| mega | M | $10^{6}$ | micro | $\mu$ | $10^{-6}$ |
| kilo | k | $10^{3}$ | milli | m | $10^{-3}$ |
| hecto | h | $10^{2}$ | centi | c | $10^{-2}$ |
| deca | da | $10^{1}$ | deci | d | $10^{-1}$ |

- The kilogram is the base unit, so prefixes attach to the gram (mg, Mg), not to kg.
- Ronna, quetta, ronto, and quecto were added in 2022. Older texts stop at yotta and yocto.

### 1.4 Conversion factors

Exact means set by definition. Derived means computed from exact pieces. Each value below was computed from its definition.

| Quantity | From | To | Factor | Status |
|---|---|---|---|---|
| length | 1 in | mm | 25.4 | exact |
| length | 1 ft | m | 0.3048 | exact |
| length | 1 yd | m | 0.9144 | exact |
| length | 1 statute mile | m | 1609.344 | exact |
| area | 1 in$^2$ | mm$^2$ | 645.16 | exact (25.4$^2$) |
| mass | 1 lb (avoirdupois) | kg | 0.45359237 | exact |
| mass | 1 slug | kg | 14.593903 | derived ($32.174049\ \mathrm{lb} \times 0.45359237\ \mathrm{kg}$) |
| force | 1 lbf | N | 4.4482216152605 | exact ($\mathrm{lb} \times g_0$) |
| pressure | 1 psi (lbf/in$^2$) | Pa | 6894.757 | derived (lbf / in$^2$) |
| pressure | 1 ksi | MPa | 6.894757 | derived |
| pressure | 1 lbf/ft$^2$ | Pa | 47.880259 | derived |
| pressure | 1 atm | Pa | 101325 | exact |
| pressure | 1 bar | Pa | 100000 | exact |
| pressure | 1 torr (mmHg) | Pa | 133.322368 | derived (atm / 760) |
| energy | 1 ft lbf | J | 1.3558179 | derived ($\mathrm{ft} \times \mathrm{lbf}$) |
| energy | 1 BTU (IT) | J | 1055.05585 | exact (international table) |
| energy | 1 BTU (thermochemical) | J | 1054.350264 | exact (thermochemical) |
| energy | 1 kWh | J | $3.6 \times 10^6$ | exact |
| energy | 1 cal (IT) | J | 4.1868 | exact |
| energy | 1 cal (thermochemical) | J | 4.184 | exact |
| power | 1 hp (mechanical, 550 ft lbf/s) | W | 745.69987 | derived |
| power | 1 hp (metric, 75 kgf m/s) | W | 735.49875 | exact (with $g_0$) |
| power | 1 hp (electric) | W | 746 | convention |
| speed | 1 mph | m/s | 0.44704 | exact |
| speed | 1 knot | m/s | 0.5144444 | exact (1852 m per 3600 s) |
| volume | 1 US gallon | L | 3.785411784 | exact |
| volume | 1 imperial gallon | L | 4.54609 | exact |
| density | 1 lbm/ft$^3$ | kg/m$^3$ | 16.018463 | derived |
| acceleration | 1 g (standard gravity) | m/s$^2$ | 9.80665 | exact |
| temperature | $t$ [°F] to $t$ [°C] | | $t_C = (t_F - 32) \times 5/9$ | exact |
| temperature | $t$ [°C] to $T$ [K] | | $T = t_C + 273.15$ | exact |

- Use the factor for the base unit squared or cubed when converting areas and volumes: 1 in$^2$ is $25.4^2$ mm$^2$, not 25.4 mm$^2$.
- rpm to rad/s: $\omega = 2\pi N / 60$.

### 1.5 SI writing style (NIST SP 811, own summary)

- Unit symbols are upright (roman) and never take a plural "s". Quantity symbols ($m$ for mass, $T$ for temperature) are italic.
- Write unit symbols in lowercase unless the unit is named after a person (N, Pa, J, W, A, K, V, Hz, $\Omega$).
- Leave a space between the number and the unit symbol: 25 mm, 20 °C. Plane angles are the exception: 90°.
- Put no space between a prefix and its unit symbol: 5 mm, not 5 m m. Use one prefix only: write nm, not m$\mu$m.
- No period after a unit symbol except at the end of a sentence.
- Mix symbols or names, never both in one expression: "5 kg/m$^3$" or "five kilograms per cubic meter", not "5 kilograms/m$^3$".
- Products use a centered dot or a space (N m or N$\cdot$m). Quotients use one slash (m/s$^2$) or negative exponents (m s$^{-2}$); never two slashes in one unit without parentheses.
- Write a leading zero before the decimal point (0.5, not .5). Group long numbers in threes from the decimal point with a thin space, not a comma.
- Use "kelvin" and K with no degree sign. Use °C for the Celsius scale.
- The liter symbol is L (capital). Use "t" for the metric tonne. Minute, hour, and day (min, h, d) are accepted with SI.
- Use "meter" in US text and "metre" in most other English usage; the symbol is m in both.

### 1.6 Dimensional checks

- Both sides of an equation must have the same dimensions. $E_k = \tfrac{1}{2} m v^2$ has dimensions $M (L T^{-1})^2 = M L^2 T^{-2}$, which is the joule.
- Trig functions, exponentials, and logarithms take dimensionless arguments.
- Adding quantities with different dimensions is always an error.

## 2. Accuracy, precision, and uncertainty

### 2.1 Definitions

| Term | Meaning |
|---|---|
| Accuracy | closeness of a result to the true value; limited by systematic error |
| Precision | closeness of repeated results to each other; limited by random error |
| Resolution | smallest change an instrument can display or read |
| Standard uncertainty $u$ | one standard deviation of the estimate, in the unit of the result |
| Type A evaluation | uncertainty from statistics of repeated observations |
| Type B evaluation | uncertainty from other information (certificate, data sheet, resolution, experience) |
| Combined standard uncertainty $u_c$ | RSS of all standard uncertainty components (section 3) |
| Expanded uncertainty $U$ | $U = k\,u_c$, with coverage factor $k$; state $k$ and the coverage probability |
| Relative uncertainty | $u / \lvert x \rvert$, often as a percent |

### 2.2 Equations

Sample mean and sample standard deviation of $N$ readings $x_i$:

$$\bar{x} = \frac{1}{N}\sum_{i=1}^{N} x_i \qquad s = \sqrt{\frac{1}{N-1}\sum_{i=1}^{N}(x_i - \bar{x})^2}$$

Type A standard uncertainty of the mean (shrinks as $1/\sqrt{N}$):

$$u(\bar{x}) = \frac{s}{\sqrt{N}}$$

Type B from resolution $\delta$ (full width of the step; the true value is assumed equally likely anywhere in it):

$$u = \frac{\delta}{2\sqrt{3}}$$

Percent error against a reference value $x_{\text{ref}}$:

$$\%\text{ error} = \frac{\bar{x} - x_{\text{ref}}}{x_{\text{ref}}} \times 100\%$$

### 2.3 Coverage and distributions

| Assumed distribution | Half-width $a$ | Standard uncertainty |
|---|---|---|
| Rectangular (equal chance anywhere in $\pm a$), default for a hard limit with no other information | $a$ | $u = a/\sqrt{3}$ |
| Triangular (most likely at center) | $a$ | $u = a/\sqrt{6}$ |
| Normal, from a stated 95 % interval | $a$ | $u = a/1.96$ (approx $a/2$) |
| Resolution step $\delta$ (rectangular, full width $\delta$) | $\delta/2$ | $u = \delta/(2\sqrt{3})$ |

| Coverage factor $k$ (normal distribution) | Coverage probability |
|---|---|
| 1 | 68.3 % |
| 1.96 | 95.0 % |
| 2 | 95.4 % (commonly quoted as 95 %) |
| 3 | 99.7 % |

- $k = 2$ gives about 95 % only when the uncertainty has many degrees of freedom. For small $N$, use a Student $t$ factor with the effective degrees of freedom (Welch-Satterthwaite formula). Standard practice in metrology requires stating which $k$ is used.

### 2.4 Typical uncertainty sources (typical)

- Instrument resolution, calibration certificate (value and its uncertainty), repeatability (Type A), temperature effects on the instrument, zero offset, linearity, hysteresis, reference value, and environment (vibration, humidity).

### Holds when / breaks when

- Holds when errors are small relative to the value, the model is linear over the uncertainty range, and components are independent.
- Breaks when $N$ is very small ($N < 5$ makes $s$ unreliable), when bias dominates (averaging does not help), or when the distribution is strongly skewed.

## 3. Propagation of uncertainty and significant figures

### 3.1 Propagation (GUM law)

For $y = f(x_1, \ldots, x_n)$ with uncorrelated inputs, sensitivity coefficients $c_i = \partial f / \partial x_i$:

$$u_c(y) = \sqrt{\sum_{i=1}^{n} c_i^2\, u^2(x_i)}$$

If inputs are correlated, add $2\sum_{i<j} c_i c_j\, u(x_i, x_j)$ inside the root, with $u(x_i, x_j)$ the covariance.

Linear sum, for comparison (always larger than RSS). It is not a guaranteed error bound, because a standard uncertainty is a standard deviation, not a limit. A true worst-case bound needs hard limits $a_i$ on each input in place of $u(x_i)$:

$$\Delta_{\max} = \sum_{i=1}^{n} |c_i|\, u(x_i)$$

For a product or power law $y = \prod x_i^{p_i}$:

$$\left(\frac{u_y}{|y|}\right)^2 = \sum_i \left(p_i \frac{u(x_i)}{|x_i|}\right)^2$$

| Function | Sensitivity coefficients |
|---|---|
| $y = a + b$ or $a - b$ | $c_a = \pm 1$, $c_b = \pm 1$ |
| $y = a b$ | $c_a = b$, $c_b = a$ |
| $y = a / b$ | $c_a = 1/b$, $c_b = -a/b^2$ |
| $y = a^p$ | $c_a = p\,a^{p-1}$ |
| $y = \sqrt{a}$ | $c_a = 1/(2\sqrt{a})$ |
| $y = \ln a$ | $c_a = 1/a$ |
| $y = \sin a$ | $c_a = \cos a$ (with $a$ in radians) |

- Power example: $P = VI$ gives $(u_P/P)^2 = (u_V/V)^2 + (u_I/I)^2$. Sum of relative terms, then take the root.
- Linear sum of relative uncertainties of two inputs is a bound only; use RSS for independent inputs.

### 3.2 Significant figures

- Nonzero digits are always significant.
- Zeros between nonzero digits are significant (1002 has 4).
- Leading zeros are not significant (0.0042 has 2).
- Trailing zeros after a decimal point are significant (2.50 has 3).
- Trailing zeros in an integer with no decimal point are ambiguous. Write them in scientific notation ($1.2 \times 10^4$).
- Exact numbers (counted items, defined conversions) do not limit significant figures.
- Multiplication and division: keep the fewest significant figures of the inputs.
- Addition and subtraction: keep the fewest decimal places of the inputs.
- Logarithm: digits after the decimal point in $\log_{10} x$ equal the significant figures of $x$.

### 3.3 Reporting procedure

1. Compute with extra digits; round only at the end.
2. Round the uncertainty to 1 or 2 significant figures (2 when the leading digit is 1 or 2, otherwise 1 is usually enough).
3. Round the value to the same decimal place as the rounded uncertainty.
4. Write $x \pm u$ with units, $k$ and coverage if expanded, $N$, and the method.

Example: $\rho = 2.6308$ g/cm$^3$ with $u = 0.0253$ g/cm$^3$ becomes $\rho = 2.631 \pm 0.025$ g/cm$^3$ (2.631 rounded to the thousandths place, matching $u$ rounded to 0.025).

### Holds when / breaks when

- Holds for independent random inputs and a locally linear model. The sensitivity coefficients are taken at the best estimate.
- Breaks for strongly nonlinear functions near a singularity (for example $1/b$ when $b$ is near zero) and for correlated inputs that are treated as independent.

## 4. Calipers and micrometers

- Vernier resolution: $r = S/N$, where $S$ is the main-scale division and $N$ is the number of vernier divisions. For 50 divisions on 49 mm: $r = 0.02$ mm.
- Vernier reading: $L = N_{\text{main}} + n\,r$, where $n$ is the vernier line that aligns best.
- Micrometer resolution: $r = p/N$, where $p$ is the screw pitch (0.5 mm common) and $N$ the thimble divisions (50 common): $r = 0.01$ mm.
- Micrometer reading: $L = S + t \times 0.01$ mm, where $S$ is the sleeve value (add 0.5 mm if the half-line shows) and $t$ the thimble division.
- Zero error: check with the tool closed. Correct every reading by subtracting the closed reading.
- Standard uncertainty from resolution: $u = r/(2\sqrt{3})$. Calibration and zero error add to this; resolution is not accuracy.
- Gauges: a go/no-go gauge checks a tolerance band. The go side must enter, and the no-go side must not.

## 5. Sensors and transducers

### 5.1 Characteristics

- Sensitivity from two calibration points: $S = (y_2 - y_1)/(x_2 - x_1)$ (units of output per unit of input).
- Inverse of a linear calibration: $x = (y - y_0)/S$, with $y_0$ the output at zero input.
- Full-scale accuracy: $u_{\text{acc}} = (a\%/100) \times R$, where $R$ is the full-scale range. Percent of full scale is not percent of reading; at low readings the difference is large.
- Live zero: 4 to 20 mA loops use 4 mA as the minimum. 0 mA signals a broken wire.
- Nonlinearity, hysteresis, and repeatability are separate specifications. Read all three.

### 5.2 Sensor selection (all values typical; confirm against the data sheet)

| Quantity | Sensor types | Typical range | Typical accuracy | Main error sources |
|---|---|---|---|---|
| Temperature | thermocouple (section 7.1) | -200 to 1800 °C, by type | about 1.5 to 2.5 °C, or 0.4 to 0.75 %, near room temperature (standard tolerance) | cold junction, extension wire mismatch, inhomogeneity, oxidation drift |
| Temperature | platinum RTD (Pt100) | -200 to 850 °C | about 0.15 °C near 0 °C (class A; class B is 0.3 °C) | self-heating, lead resistance, strain on element |
| Temperature | NTC thermistor | -50 to 150 °C | 0.1 to 1 °C over a narrow span | nonlinearity, self-heating, aging |
| Pressure | strain-gauge diaphragm, piezoresistive, capacitive | mbar to 1000 bar | 0.1 to 0.5 % of full scale | zero and span temperature shift, hysteresis, overpressure, mounting stress |
| Force, load | strain-gauge load cell | 1 N to 1 MN | about 0.02 to 0.1 % of full scale | creep, off-axis and eccentric loading, temperature, hysteresis |
| Strain | foil gauge in a bridge (section 6) | 1 to 10 000 $\mu\varepsilon$ | about 1 % of reading plus bridge offset | temperature, lead resistance, transverse sensitivity, creep |
| Linear displacement | LVDT | 1 mm to 500 mm | 0.1 to 0.5 % of full scale | core misalignment, temperature, end-of-range nonlinearity |
| Angle | incremental optical encoder | $10^2$ to $10^5$ counts per revolution | arcseconds to a few arcminutes | eccentricity, mounting, counting errors |
| Acceleration | piezoelectric | 0.5 Hz to 10 kHz (no DC); $\pm 1$ to $\pm 10^5$ g | about 1 to 5 % | mount resonance, transverse sensitivity, temperature, base strain, cable noise |
| Acceleration | MEMS capacitive | DC to about 1 kHz; $\pm 2$ to $\pm 200$ g | about 1 to 3 % | offset drift, temperature, bias instability, noise floor |
| Flow | orifice or venturi with differential pressure | depends on bore and fluid | 0.5 to 2 % of reading (ISO 5167 class) | discharge coefficient, upstream conditions, fluid density |
| Humidity | capacitive polymer | 0 to 100 %RH | $\pm 1$ to $\pm 3$ %RH | contamination, hysteresis, temperature |

### 5.3 Holds when / breaks when

- Holds for sensors used inside their range, at the calibrated temperature, and after warm-up.
- Breaks when the sensor is loaded beyond range, when mounting changes the measured quantity, or when temperature moves the zero or span.

## 6. Strain gauges and the Wheatstone bridge

### 6.1 Equations

Strain (dimensionless): $\varepsilon = \Delta L / L$, with $1\ \mu\varepsilon = 10^{-6}$.

Gauge resistance change: $\dfrac{\Delta R}{R} = \mathrm{GF}\,\varepsilon$, with $\mathrm{GF}$ dimensionless (about 2 for metal foil; semiconductor gauges are much higher, typically 50 to 150).

Uniaxial linear-elastic stress (Hooke's law): $\sigma = E\,\varepsilon$, with $E$ the modulus in Pa (steel about 200 GPa, typical; aluminum about 70 GPa, typical).

Quarter bridge, one active arm $R + \Delta R$, three fixed arms $R$, excitation $V_{\text{ex}}$ (V):

$$V_{\text{out}} = V_{\text{ex}}\left[\frac{R+\Delta R}{2R+\Delta R} - \frac{1}{2}\right] = V_{\text{ex}}\,\frac{\Delta R}{4R + 2\Delta R}$$

Small-strain quarter bridge: $V_{\text{out}} \approx V_{\text{ex}}\,\mathrm{GF}\,\varepsilon / 4$. Invert: $\varepsilon \approx 4 V_{\text{out}} / (\mathrm{GF}\, V_{\text{ex}})$.

Half bridge with two active arms carrying opposite strain sense (for example bending): $V_{\text{out}} \approx V_{\text{ex}}\,\mathrm{GF}\,\varepsilon / 2$.

Full bridge with four active arms in the same bending pattern: $V_{\text{out}} \approx V_{\text{ex}}\,\mathrm{GF}\,\varepsilon$.

Balance condition: $R_1 / R_2 = R_3 / R_4$ gives $V_{\text{out}} = 0$ at zero strain. Balance is an output condition, not an excitation-free state.

Quarter-bridge approximation error: $\text{exact} / \text{approximate} = 1/(1 + \Delta R / 2R)$, so the error of the approximation is about $-\mathrm{GF}\,\varepsilon/2$. At $\mathrm{GF}\,\varepsilon = 10^{-3}$ this is -0.05 %.

Thermal apparent strain (approximate, sign convention varies by gauge): $\varepsilon_{\text{app}} \approx (\alpha_{\text{specimen}} - \alpha_{\text{gauge}})\,\Delta T$, with $\alpha$ in 1/K. Cancel it with a dummy gauge on an unstrained piece of the same material, or with a gauge whose $\alpha$ matches the specimen.

Transverse sensitivity: a gauge responds a little to strain across its grid, so the uniaxial reading carries a small error. Under uniaxial stress the transverse strain is $-\nu\,\varepsilon$, with $\nu$ Poisson's ratio (about 0.3 for steel, typical).

### 6.2 Practical values (typical)

| Item | Typical value |
|---|---|
| Gauge resistance | 120, 350, or 1000 $\Omega$ |
| Metal foil $\mathrm{GF}$ | about 2 |
| Excitation | 2 to 10 V |
| Output at 1000 $\mu\varepsilon$, quarter bridge, 5 V excitation, $\mathrm{GF} = 2$ | 2.5 mV |
| Output resolution needed for 10 $\mu\varepsilon$ on the same setup | about 25 $\mu$V |

### 6.3 Wiring

- Three-wire or four-wire connection cancels lead resistance in the bridge arm. Two-wire connection adds lead resistance to the active arm and reduces sensitivity.
- Lead resistance in the active arm reduces apparent strain. Measure or compensate it when leads are long.

### Holds when / breaks when

- Holds for $\mathrm{GF}\,\varepsilon \ll 1$, uniform strain over the grid, linear elastic material, stable excitation, negligible self-heating, and matched fixed resistors.
- Breaks when the gauge yields or creeps, when temperature gradients are large, when the grid is partly on a free edge or a weld, or when gauge $\mathrm{GF}$ does not match the batch used for calibration.

## 7. Thermocouples and accelerometers

### 7.1 Thermocouple types (IEC 60584-1 nominal limits, approximate; check the standard before design)

| Type | Pair (+ / -) | Nominal range | Notes |
|---|---|---|---|
| J | iron / constantan | -210 to 1200 °C | reducing atmospheres; iron rusts |
| K | chromel / alumel | -200 to 1350 °C | general purpose; about 41 $\mu$V/°C near room temperature |
| T | copper / constantan | -200 to 400 °C | low-temperature and moisture-tolerant |
| E | chromel / constantan | -200 to 900 °C | highest output of the common base-metal types |
| N | Nicrosil / Nisil | -270 to 1300 °C | better oxidation resistance than K |
| R | Pt-13 % Rh / Pt | 0 to 1768 °C | noble metal; low output, about 10 $\mu$V/°C (typical) |
| S | Pt-10 % Rh / Pt | 0 to 1768 °C | noble metal; historical reference type |
| B | Pt-30 % Rh / Pt-6 % Rh | 0 to 1820 °C | very low output below about 600 °C; needs care at low temperature |

- Cold junction compensation is required for every type. The junction at the meter terminals is the reference.
- Use extension wire of the matching type. A mismatched extension wire adds an error at each connection.
- Linear sensitivity is only a rough guide; use the standard table or polynomial for accurate work.

### 7.2 Thermocouple equations

Linear approximation near room temperature: $T_{\text{hot}} = T_{\text{cj}} + V / S$, with $S$ the Seebeck sensitivity (type K about $4.1 \times 10^{-5}$ V/K) and $T_{\text{cj}}$ the cold junction temperature.

At 41 $\mu$V/°C, 1 mV of signal is about 24 °C of temperature difference (typical).

### 7.3 Accelerometers

Calibrated linear output: $a\ [\text{g}] = V_{\text{out}}\ [\text{mV}] / s\ [\text{mV/g}]$, and $a\ [\text{m/s}^2] = a\ [\text{g}] \times 9.80665$.

Undamped second-order response: the output-to-input ratio is $1/(1 - r^2)$, with $r = f / f_n$ and $f_n$ the mounted resonant frequency.

| Ratio $r = f/f_n$ | Amplitude error (undamped) |
|---|---|
| 0.2 | +4.2 % |
| $1/3$ | +12.5 % |
| 0.5 | +33 % |

- Rule of thumb: use the sensor only up to about one fifth of the mounted resonance for an error near 4 % (basis: the undamped response above; the real error depends on damping).

### Holds when / breaks when

- Thermocouple linear sensitivity holds only near room temperature and for a narrow span; use tables or polynomials outside that.
- Piezoelectric accelerometers cannot measure steady acceleration (no DC). MEMS sensors can measure static tilt, where gravity gives about 1 g on the sensitive axis.

## 8. Data acquisition and sampling

### 8.1 Sampling

- Nyquist frequency: $f_N = f_s / 2$. Content above $f_N$ is not recoverable.
- Aliased frequency of a tone at $f$ sampled at $f_s$: $f_{\text{alias}} = |f - n\,f_s|$, where $n$ is the integer nearest $f/f_s$. For $f$ between $f_N$ and $f_s$, this is $|f - f_s|$.
- Practical sample rate: 5 to 10 times the highest frequency of interest; the strict minimum is twice.
- Anti-alias filter: a low-pass filter before the ADC, with the cutoff below $f_N$ and enough attenuation at $f_N$ and above for the dynamic range you need. Rule of thumb (basis: an $n$-bit ADC has about $6n$ dB of dynamic range): the attenuation at $f_s - f_{\text{passband}}$ should be at least about $6n$ dB.
- Oversampling then digital decimation reduces the analog filter demand, but the anti-alias filter must still come before the sampling step.

### 8.2 ADC

- Codes: $2^n$ (12 bit gives 4096).
- LSB: $\text{LSB} = V_{\text{span}} / 2^n$. Span is the full range (a $\pm 5$ V range has $V_{\text{span}} = 10$ V).
- Quantization error: uniform within $\pm \text{LSB}/2$. RMS value: $\text{LSB}/\sqrt{12}$.
- Ideal SNR for a full-scale sine: $\text{SNR} \approx 6.02\,n + 1.76$ dB. Real converters give fewer effective bits than their nominal $n$.
- Settling of a full-span step to within 1 LSB through a first-order RC input: $t \approx n\,\tau\ln 2$. For 12 bits, $t \approx 8.3\,\tau$. To within half an LSB: $t \approx \tau\ln(2^{n+1})$, which is $9.0\,\tau$ for 12 bits.

| Bits $n$ | Codes | LSB at 10 V span | RMS quantization error | Ideal SNR |
|---|---|---|---|---|
| 8 | 256 | 39.1 mV | 11.3 mV | 50 dB |
| 10 | 1024 | 9.77 mV | 2.82 mV | 62 dB |
| 12 | 4096 | 2.44 mV | 0.705 mV | 74 dB |
| 16 | 65 536 | 0.153 mV | 0.044 mV | 98 dB |

### Holds when / breaks when

- Holds for a single-tone or band-limited signal sampled with a proper anti-alias filter and clock, and a signal that fills the ADC range.
- Breaks when the signal is smaller than a few LSB (quantization error stops being uniform and noise-like), when the anti-alias filter is after the ADC, when channels are multiplexed faster than they settle, and when clock jitter limits the real SNR.

## 9. Experiment design

- Factor: a quantity you change deliberately. Level: a chosen setting of a factor. Response: the quantity you measure. Control: a run without the change, as a baseline.
- Confounder: a quantity that changes with the factor and can mimic its effect. Hold it fixed or record it.
- Replication estimates random error. A single run gives no uncertainty.
- Randomize run order to keep equipment drift off the factor effects.
- Block runs that share a known source of variation (test day, material batch).
- Full factorial with $k$ factors at 2 levels: $2^k$ settings. Fractional factorials cut the count when interactions are negligible.
- Replicates needed for a target standard uncertainty of the mean, from a pilot standard deviation $s$:

$$N = \left(\frac{s}{u_{\text{target}}}\right)^2 \quad \text{(round up)}$$

Halving the target uncertainty needs four times the replicates.

- Before data: write the hypothesis, the response, the acceptance criterion, and the uncertainty budget. Changing these after seeing data creates false conclusions.

### 9.1 Calibration chain and traceability

- Chain: SI realization (the defined constants above) to national metrology institute (for example NIST) to accredited calibration lab (ISO/IEC 17025) to working standard to the instrument under test.
- Each link adds uncertainty. Record the uncertainty of each link; the combined uncertainty of the instrument includes the whole chain.
- Traceability is an unbroken chain of comparisons, each with a stated uncertainty (VIM definition, JCGM 200).
- Test uncertainty ratio: the tolerance of the item under test divided by the uncertainty of the reference. A 4:1 ratio is a common practice (typical) and gives a clear decision with small guard band.
- Calibration interval: set from drift history. Recalibrate after shock, overload, or repair.

## 10. Data analysis and least squares

For $N$ points $(x_i, y_i)$ fit $y = a + bx$:

$$b = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} \qquad a = \bar{y} - b\,\bar{x}$$

Residuals: $r_i = y_i - (a + b x_i)$. Residual standard deviation with $N - 2$ degrees of freedom:

$$s_r = \sqrt{\frac{\sum r_i^2}{N-2}}$$

Standard uncertainties of slope and intercept:

$$u(b) = \frac{s_r}{\sqrt{\sum (x_i - \bar{x})^2}} \qquad u(a) = s_r\sqrt{\frac{1}{N} + \frac{\bar{x}^2}{\sum (x_i - \bar{x})^2}}$$

- $R^2 = 1 - \sum r_i^2 / \sum (y_i - \bar{y})^2$. A high $R^2$ does not prove linearity; plot the residuals.
- Report: $b \pm u(b)$, $a \pm u(a)$, units, $N$, and the fit method.
- Do not extrapolate far beyond the calibrated range.

### Holds when / breaks when

- Holds when $x$ is known far better than $y$, $y$ has independent random scatter, and the model is linear.
- Breaks when $y$ errors are heteroscedastic (use weighted least squares), when $x$ has comparable error (use errors-in-variables fits), and when residuals show a trend.

## Checklists

**Before trusting a measurement**

- [ ] Every number has a unit.
- [ ] Zero or offset checked (closed reading, blank, or tare).
- [ ] Instrument calibration in date, with its uncertainty recorded.
- [ ] Resolution and accuracy both noted; resolution not reported as accuracy.
- [ ] Environment stated (temperature, humidity, vibration) and within specification.
- [ ] Repeated readings taken; $N$ stated.
- [ ] Sample rate meets Nyquist with the anti-alias filter before the ADC.
- [ ] Signal fills most of the ADC span without clipping.

**Before releasing a result**

- [ ] Uncertainty budget complete: Type A and Type B components, calibration, resolution, environment.
- [ ] Components combined by RSS when independent; correlations checked.
- [ ] Coverage factor $k$ and coverage probability stated if expanded.
- [ ] Significant figures match the uncertainty.
- [ ] Traceability chain documented.
- [ ] Residuals plotted for any fit; no trend remains.
- [ ] Result compared with the reference or tolerance using its uncertainty, not the bare value.

**Strain bridge setup**

- [ ] Bridge balanced at zero load; output drift with time checked.
- [ ] Excitation stable and known.
- [ ] Gauge $\mathrm{GF}$ and resistance match the calibration.
- [ ] Lead configuration chosen (three or four wire where possible).
- [ ] Dummy gauge or temperature plan in place for thermal apparent strain.

**Thermocouple reading**

- [ ] Type identified; extension wire of the same type.
- [ ] Cold junction temperature measured and compensated.
- [ ] Standard table or polynomial used outside room temperature.

**Experiment**

- [ ] Hypothesis, response, and acceptance criterion written before data.
- [ ] Control included.
- [ ] Replicates sized from a pilot standard deviation.
- [ ] Run order randomized; blocks defined.
- [ ] Confounders held fixed or recorded.

## Sanity checks

- Dimensions: both sides of every equation match.
- 1 in $\approx$ 25.4 mm; 1 ft $\approx$ 0.305 m; 1 in$^2$ $\approx$ 645 mm$^2$.
- 1 lbf $\approx$ 4.45 N; 1 psi $\approx$ 6.9 kPa; 1 atm $\approx$ 101 kPa.
- 1 hp $\approx$ 746 W; $1\ \mathrm{kWh} = 3.6\ \mathrm{MJ}$; 1 BTU $\approx$ 1055 J.
- Standard gravity: $1\ \mathrm{g} = 9.81\ \mathrm{m/s^2}$ (9.80665 exact). A static MEMS axis should read about 1 g.
- Strain: 1000 $\mu\varepsilon$ with $\mathrm{GF} = 2$ gives $\Delta R/R = 0.2$ %, and a quarter bridge at 5 V gives about 2.5 mV.
- Thermocouple: about 41 $\mu$V/°C for type K; 1 mV is about 24 °C.
- Averaging: $N$ readings reduce $u$ by $\sqrt{N}$. Quadrupling $N$ halves $u$.
- Sampling: a 12-bit ADC on 10 V has an LSB of about 2.44 mV.
- Settling: 12 bits to 1 LSB needs about 8.3 time constants (9.0 for half an LSB).
- Uncertainty larger than the value means the result is not useful at that level.
- A result that is outside the stated range or in the wrong sign is an error until shown otherwise.

## Further reference

- JCGM 100:2008, *Guide to the Expression of Uncertainty in Measurement* (GUM). Free from the BIPM; the basis of all uncertainty rules above.
- JCGM 200:2012, *International Vocabulary of Metrology* (VIM). Definitions of traceability and related terms.
- NIST SP 811, *Guide for the Use of the International System of Units*. Official SI writing rules.
- NIST SP 330, *The International System of Units*. Background to SI.
- NIST Technical Note 1297, *Guidelines for Evaluating and Expressing the Uncertainty of NIST Measurement Results*. Type A and Type B methods.
- NIST Monograph 175, the ITS-90 thermocouple database and polynomials.
- IEC 60584-1, thermocouple tables and tolerances. IEC 60751, platinum resistance thermometers.
- ASTM E230, thermocouple tables for US practice.
- ISO 5167, measurement of fluid flow by differential devices (orifice, venturi).
- ISO/IEC 17025, general requirements for testing and calibration laboratories.
- Taylor, J. R., *An Introduction to Error Analysis*. Paid; clear treatment of propagation.
- Figliola, R. S., and Beasley, D. E., *Theory and Design for Mechanical Measurements*. Paid; instruments and dynamic response.
- Doebelin, E. O., and Manik, D. N., *Measurement Systems: Application and Design*. Paid; sensor and signal chain.
- Holman, J. P., *Experimental Methods for Engineers*. Paid; experiment design and uncertainty.
- Roark's Formulas for Stress and Strain, for strain-to-stress models beyond uniaxial. Paid.
- Machinery's Handbook, for gauge tolerances and metrology tables. Paid.
- Vishay Measurements Group strain gauge technical notes, for gauge installation and bridge practice. Free from the manufacturer.
