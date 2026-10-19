# Check units and limiting cases

**Type:** lesson

**Checking units and limiting cases** is the practice of testing a formula with dimensional analysis and with an extreme input value. Engineers need it because these two quick tests catch many wrong formulas before anyone trusts them.

The first test is dimensional
analysis. Every term in an equation must have the same units, and the final result must have
the units of the quantity you want. The second is the limiting case. Push one input to an
extreme value (zero, very large, or a special angle) and check whether the answer does what
physics says it should.

**Prerequisites:** [Solve symbolically before plugging in numbers](04-solve-symbolically.md), [Units and dimensional analysis](../measurement/01-units-and-dimensional-analysis.md), [Heat transfer](../physics/12-heat-transfer.md)
**Time:** 3-4 h

## Core ideas

- A **dimension** is the physical kind of a quantity: length ($L$), mass ($M$), time ($T$), and so
  on. Units are a choice of scale within a dimension (meter, foot).
- **Dimensional analysis** means writing the dimensions of every symbol and checking each side
  of an equation.
- Two terms can be added only if they have the same dimensions. You cannot add meters to
  seconds, and you cannot add a force to an energy.
- A **limiting case** is an extreme input where you already know the answer. Examples:
  zero load, zero angle, infinite length, or a very large mass.
- A formula that fails a limiting case is wrong, even if its units are correct. A formula
  that passes both tests is not proven, but it has earned trust.

### Units to know

Use SI (the metric system used in science and most engineering). Base units: meter (m) for
length, kilogram (kg) for mass, second (s) for time, kelvin (K) for temperature, ampere (A) for
electric current. The complete list is on the [NIST SI page](https://www.nist.gov/pml/owm/metric-si/si-units).

Derived units you will meet often:

- Force: newton ($\text{N}$) $= \text{kg} \cdot \text{m/s}^2$
- Energy: joule ($\text{J}$) $= \text{N} \cdot \text{m} = \text{kg} \cdot \text{m}^2/\text{s}^2$
- Power: watt ($\text{W}$) $= \text{J/s}$
- Pressure: pascal ($\text{Pa}$) $= \text{N/m}^2$

### Steps to check a formula

1. Write the dimensions of every symbol. Use the table above.
2. Build the dimensions of each term and of the result.
3. Check that all added terms match and that the final dimensions equal the target quantity.
4. Test one or two limits: set an input to zero, to very large, or to a special angle.
5. Compare the limit to physical intuition.

## Key equations

Heat flow through a flat wall, steady and one-dimensional (typical values for $k$ are given
below):

$$
Q = \frac{k\,A\,\Delta T}{L}
$$

Symbols:

- $Q$ is heat flow rate in watts (W), which is joules per second.
- $k$ is thermal conductivity in W/(m $\cdot$ K). Typical single-pane glass is about 0.8 W/(m $\cdot$ K).
- $A$ is area in square meters (m$^2$).
- $\Delta T$ is the temperature difference in kelvin (K) or degrees Celsius (a difference is the same in both).
- $L$ is thickness in meters (m).

Dimensional check of the group $\dfrac{k A \Delta T}{L}$:

$$
\left[\frac{\text{W}}{\text{m}\cdot\text{K}}\right]\cdot[\text{m}^2]\cdot[\text{K}]\cdot\frac{1}{[\text{m}]} = \text{W}
$$

The result is in watts, as required.

## Worked example

**Problem.** A single-pane window is 1.5 m$^2$ in area and 4.0 mm thick. The inner glass surface is 20 K warmer
than the outer glass surface. Estimate the heat loss through the glass, and check the formula with units and
limits.

**Given:** $A = 1.5\ \text{m}^2$, $L = 4.0\ \text{mm} = 0.0040\ \text{m}$, $\Delta T = 20\ \text{K}$ (across the glass, surface to surface),
$k = 0.8\ \text{W/(m}\cdot\text{K)}$ (typical value for glass).

**Find:** $Q$ in W.

**Assumptions:** steady heat flow, no heat lost through the frame, and a flat pane.

**Solution.**

Step 1, unit check. Done above: the formula gives watts.

Step 2, calculate:

$$
Q = \frac{0.8 \times 1.5 \times 20}{0.0040} = \frac{24}{0.0040} = 6000\ \text{W}
$$

Step 3, limiting case. If the thickness $L$ doubles, $Q$ should halve, because the formula puts
$L$ in the denominator. Check: with $L = 0.0080\ \text{m}$, $Q = 24/0.0080 = 3000\ \text{W}$.
That is half, as expected.

Step 4, limiting case. If $\Delta T = 0$ (no temperature difference), $Q = 0$. A window with no
temperature difference loses no heat, so the formula passes.

**Answer:** $Q \approx 6.0 \times 10^3\ \text{W}$ (6 kW) through the glass.

**Sanity check:** 6 kW is about four small space heaters running at 1.5 kW each. That is large for
one pane, and it is valid only because the two glass surfaces are assumed to be 20 K apart. In a real window
most of the room-to-outdoor temperature difference falls across the air films at the glass surfaces, so the
temperature difference across the glass is much smaller and the real loss is far lower.

## Practice

1. A wall with $k = 0.8\ \text{W/(m}\cdot\text{K)}$, $A = 2.0\ \text{m}^2$,
   $\Delta T = 10\ \text{K}$, and $L = 0.010\ \text{m}$. Find $Q$ in W.
2. A 50 kg sign hangs from two cables at $80^\circ$ to the horizontal, using
   $T = mg/(2\sin\theta)$. Find $T$ in N.
3. The same sign, but the cables are at $5^\circ$ to the horizontal. Find $T$ in N. Then state
   whether the limit makes sense.

<details><summary>Answers</summary>

1. 1600 W
2. 249.0 N
3. 2814 N

</details>

## Common mistakes

- Adding terms with different units, such as a length and a time, without noticing.
- Using centimeters where meters are needed. The window example gives a factor of 10 error if
  the thickness is entered as 4 cm (lesson 08 shows this case).
- Skipping the limit test because the units looked right. Units alone do not prove a formula.
- Using absolute temperature where a difference is needed, or the reverse. A difference
  $\Delta T$ is the same number in Celsius and kelvin, but a single temperature is not.
- Assuming a limit is "physical" when the formula diverges. A divergence at zero angle is a
  real feature of the cable problem, not a bug, but you must say so.

## Go deeper

- [University Physics Volume 1, section 1.2 Units and Standards](https://openstax.org/books/university-physics-volume-1/pages/1-2-units-and-standards) by OpenStax: base and derived SI units and prefixes.
- [SI units](https://www.nist.gov/pml/owm/metric-si/si-units) by NIST: the official SI reference used by U.S. government labs.
- [Engineering LibreTexts](https://eng.libretexts.org/) by LibreTexts: free engineering textbooks, with units and conversion chapters in several shelves.
- [University Physics Volume 1](https://openstax.org/details/books/university-physics-volume-1) by OpenStax: the first chapter on measurement and dimensional analysis.
- [Problem-solving reference](reference.md): the lookup sheet for this topic.
