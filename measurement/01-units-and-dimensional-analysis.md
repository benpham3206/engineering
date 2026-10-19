# Units and dimensional analysis

**Type:** lesson

A unit is an agreed-upon amount of a quantity, such as one metre of length, that every measurement is counted in. Every number in engineering means nothing without its unit, and mixing units has destroyed a spacecraft.

A measurement is a number with a unit. Engineers use units to check that equations make sense, convert between systems, and catch mistakes before they become expensive.

**Prerequisites:** none (high-school algebra helps)
**Time:** 4-6 h

## Core ideas

- A **physical quantity** is something you can measure, such as length, mass, or time. A **unit** is the reference size you compare against.
- A **base dimension** is a kind of physical quantity that is not built from others. The usual set is length ($L$), mass ($M$), time ($T$), electric current ($I$), temperature ($\Theta$), amount of substance ($N$), and luminous intensity ($J$).
- A **derived dimension** combines base dimensions. Speed is $L T^{-1}$. Force is $M L T^{-2}$.
- The **SI system** (International System of Units) uses meter, kilogram, second, ampere, kelvin, mole, and candela as its seven base units. The NIST SI guide describes the rules for writing them. US customary units (inch, pound, second, and so on) are still common in US industry, so you will convert between them often.
- A **prefix** scales a unit by a power of ten. Examples: milli (m, $10^{-3}$), kilo (k, $10^{3}$), mega (M, $10^{6}$). Write the prefix in front of the unit with no space: 5 mm, not 5 m m.
- A **conversion factor** is a ratio equal to 1, such as $\frac{25.4\ \text{mm}}{1\ \text{in}}$. Multiply by it so the old unit cancels. The inch-to-millimeter factor is exact by definition.
- **Dimensional analysis** is the habit of checking that both sides of an equation have the same dimensions. If they do not, the equation is wrong, even if the numbers look plausible.
- **Dimensionless quantities** have no net unit, such as a strain ratio or a ratio of two lengths. Trig functions and exponentials take dimensionless arguments.

## Key equations

Unit conversion works by multiplying by a factor equal to 1:

$$x_{\text{new}} = x_{\text{old}} \times \frac{\text{new unit}}{\text{old unit}}$$

Angular speed converts from revolutions per minute (rpm) to radians per second (rad/s):

$$\omega\ [\text{rad/s}] = N\ [\text{rev/min}] \times \frac{2\pi\ \text{rad}}{1\ \text{rev}} \times \frac{1\ \text{min}}{60\ \text{s}}$$

Kinetic energy, $E_k$, in joules (J), with mass $m$ in kilograms (kg) and speed $v$ in meters per second (m/s):

$$E_k = \tfrac{1}{2} m v^2 \qquad [M L^2 T^{-2}] = [\text{kg}\cdot\text{m}^2/\text{s}^2] = [\text{J}]$$

Dimension check: $\tfrac{1}{2}$ is dimensionless, so $E_k$ has the dimensions of $m v^2$, which are $M (L T^{-1})^2 = M L^2 T^{-2}$. A joule is a newton-meter, and a newton is a kilogram-meter per second squared, so the units agree.

## Worked example

**Given:** A steel plate measures 3.50 in by 2.25 in. A shop drawing needs the area in $\mathrm{mm^2}$ and $\mathrm{m^2}$, and a motor runs at 1800 rpm.

**Find:** (a) the plate area in $\mathrm{mm^2}$ and $\mathrm{m^2}$, (b) the motor speed in rad/s.

**Assumptions:** $1\ \mathrm{in} = 25.4\ \mathrm{mm}$ exactly (the international inch).

**Solution (a):**

- Length in mm: $L = 3.50\ \text{in} \times 25.4\ \text{mm/in} = 88.9\ \text{mm}$
- Width in mm: $W = 2.25\ \text{in} \times 25.4\ \text{mm/in} = 57.15\ \text{mm}$
- Area in $\mathrm{mm^2}$: $A = 88.9 \times 57.15 = 5080.6\ \text{mm}^2$
- Area in $\mathrm{m^2}$: $5080.6\ \text{mm}^2 \times (10^{-3}\ \text{m/mm})^2 = 5.081 \times 10^{-3}\ \text{m}^2$

**Solution (b):**

$$\omega = 1800\ \frac{\text{rev}}{\text{min}} \times \frac{2\pi\ \text{rad}}{\text{rev}} \times \frac{\text{min}}{60\ \text{s}} = 188.5\ \text{rad/s}$$

**Answer:** $A = 5081\ \text{mm}^2 = 5.081 \times 10^{-3}\ \text{m}^2$. $\omega = 188.5\ \text{rad/s}$.

**Sanity check:** 1 $\mathrm{in^2}$ is about 645 $\mathrm{mm^2}$, and $7.875\ \mathrm{in^2} \times 645.16\ \mathrm{mm^2/in^2} = 5081\ \mathrm{mm^2}$, which agrees. 1800 rpm is 30 rev/s, and each revolution is about 6.28 rad, so $30 \times 6.28 \approx 188$ rad/s.

## Practice

1. Convert 2.50 in to mm.
2. Convert 60 mph to m/s. ($1\ \mathrm{mph} = 0.44704\ \mathrm{m/s}$ exactly.)
3. Convert the density 7850 $\mathrm{kg/m^3}$ to $\mathrm{lb/ft^3}$. ($1\ \mathrm{kg/m^3} = 0.062428\ \mathrm{lb/ft^3}$.)
4. Convert a torque of 25 $\mathrm{N\cdot m}$ to $\mathrm{lbf\cdot ft}$. ($1\ \mathrm{lbf\cdot ft} = 1.3558\ \mathrm{N\cdot m}$.)
5. A student writes $v = a t^2$ for speed $v$ (m/s), acceleration $a$ ($\mathrm{m/s^2}$), and time $t$ (s). Is this dimensionally consistent? Explain in one sentence.

<details><summary>Answers</summary>

1. 63.5 mm
2. 26.82 m/s
3. 490.1 $\mathrm{lb/ft^3}$
4. 18.44 $\mathrm{lbf\cdot ft}$
5. No. $a t^2$ has dimensions $L T^{-2} \cdot T^2 = L$, not $L T^{-1}$.

</details>

## Common mistakes

- Multiplying when you should divide. Check that the old unit cancels before you trust the result.
- Forgetting that squared units square the conversion factor. Converting $\mathrm{mm^2}$ to $\mathrm{m^2}$ uses $(10^{-3})^2 = 10^{-6}$, not $10^{-3}$.
- Mixing rpm with rad/s without the $2\pi/60$ factor.
- Writing units with a space before a prefix or dropping the unit from the final answer.
- Adding quantities with different dimensions, such as meters plus seconds, which is always an error.

## Go deeper

- [University Physics Volume 1, Chapter 1: Introduction](https://openstax.org/books/university-physics-volume-1/pages/1-introduction) by OpenStax: units, standards, and significant figures in physics context.
- [Unit Conversion (section 1.3)](https://openstax.org/books/university-physics-volume-1/pages/1-3-unit-conversion) by OpenStax: worked conversions between unit systems.
- [Dimensional Analysis (section 1.4)](https://openstax.org/books/university-physics-volume-1/pages/1-4-dimensional-analysis) by OpenStax: base dimensions and dimensional consistency.
- [NIST SP 811, Guide for the Use of the International System of Units](https://www.nist.gov/pml/special-publication-811) by NIST: the official SI rules for writing units and prefixes.
- [Measurement reference](reference.md): the lookup sheet for this topic.
