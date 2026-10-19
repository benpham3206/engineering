# Estimation

**Type:** lesson

**Estimation** is the practice of finding the order of magnitude of an answer from known values when exact data is missing. Engineers need it because a rough answer with its assumptions shows quickly whether a detailed analysis is worth doing.

A Fermi problem asks for a
quantity such as "how much energy heats a bath?" and answers it by breaking the question into
parts, using values you know or can look up, and rounding aggressively. The result is an order
of magnitude with a range, and you write down every assumption so a reader can check or change it.

**Prerequisites:** [Sanity-check the answer](06-sanity-check-the-answer.md), [Thermodynamics: properties, work, heat, and the first law](../physics/08-thermo-first-law.md)
**Time:** 4-6 h

## Core ideas

- A **Fermi problem** is a question where the exact answer is hard to get but a careful
  estimate is easy. The name comes from the physicist Enrico Fermi, who was known for these
  questions.
- The method has five steps:
  1. Decompose the quantity into parts you can estimate, using a formula.
  2. Assume a value for each part, stating the source or the reason.
  3. Round each value to one significant figure to keep the arithmetic simple.
  4. Compute the result, and carry the rounding through.
  5. Bound the answer: give a range from a low and a high set of assumptions.
- An **assumption** is a stated value that you have not measured. Write it down with its unit,
  and say why you chose it. A reader should be able to swap in a better value.
- A **typical value** is a number that is representative of common cases, such as the density of
  water (about 1000 kg/m$^3$). Use these from reliable tables, not from memory alone.
- An **order-of-magnitude answer** is correct to within a factor of about 3 to 10. Do not claim
  more precision than the inputs support.

### Good habits

- Use a formula to build the estimate. A formula keeps the unit bookkeeping honest.
- Round inputs first, then compute. Rounding at the end hides bad assumptions.
- Give a range: "between 10 and 30 kWh." A single number implies more confidence than you have.
- Compare to a known quantity. If your estimate is larger than a whole house's yearly use, look
  for the error (lesson 08).

## Key equations

Energy to heat a mass of water by a temperature rise $\Delta T$:

$$
Q = m\,c\,\Delta T
$$

Symbols:

- $Q$ is energy in joules (J)
- $m$ is mass of water in kilograms (kg)
- $c$ is specific heat of water, typically $4186\ \text{J/(kg}\cdot\text{K)}$
- $\Delta T$ is the temperature rise in kelvin (K), which equals the rise in Celsius

Converting energy: $1\ \text{kWh} = 3.6 \times 10^6\ \text{J}$.

Heating time at a constant power $P$ in watts (W):

$$
t = \frac{Q}{P}
$$

## Worked example

**Problem.** Estimate the energy needed to heat a bath from 10 C to 40 C. Express it in MJ and
in kWh. Then estimate how long a 1.5 kW heater would take.

**Given (typical values and assumptions):**

- Bath water volume is about 150 L. One liter of water has a mass of about 1 kg, so
  $m \approx 150\ \text{kg}$.
- Specific heat of water: $c = 4186\ \text{J/(kg}\cdot\text{K)}$, a typical value.
- Temperature rise: $\Delta T = 40 - 10 = 30\ \text{K}$.
- Heat losses to the room are ignored (an upper-bound estimate would add them).
- Heater power: $P = 1.5\ \text{kW} = 1500\ \text{W}$, a typical small electric heater.

**Find:** $Q$ in MJ and kWh, and heating time $t$ in minutes.

**Solution.**

Energy:

$$
Q = m\,c\,\Delta T = 150 \times 4186 \times 30 = 1.884 \times 10^7\ \text{J} = 18.8\ \text{MJ}
$$

In kWh:

$$
Q = \frac{18.84 \times 10^6}{3.6 \times 10^6}\ \text{kWh} = 5.2\ \text{kWh}
$$

Heating time:

$$
t = \frac{Q}{P} = \frac{1.884 \times 10^7}{1500}\ \text{s} = 12\,560\ \text{s} = 209\ \text{min}
$$

**Answer:** about 19 MJ, or about 5 kWh, which at a 1.5 kW heater takes roughly 3.5 hours.
Real bath heating also loses heat to the tank, pipes, and room, so the energy drawn is somewhat larger
than this, but the order of magnitude is right.

**Sanity check:** a home uses roughly tens of kWh per day for everything. A single bath at 5 kWh
is a reasonable fraction of that. A bath at 500 kWh would be wrong by a factor of 100.

**Range:** if the bath is 100 L and the rise is 20 K, $Q = 8.4$ MJ, about 2.3 kWh. If the
bath is 200 L and the rise is 35 K, $Q = 29$ MJ, about 8.1 kWh. The estimate is between about 2
and 8 kWh for a typical bath.

## Practice

1. Estimate the energy in kWh to warm 30 kg of water by 20 K. Use $c = 4186\ \text{J/(kg}\cdot\text{K)}$.
2. How many seconds are in one day? Use 24 h per day and 60 min per hour.
3. A 40 L bucket of water is heated by 20 K. Find the energy in kWh.

<details><summary>Answers</summary>

1. 0.698 kWh
2. 86400 s
3. 0.93 kWh

</details>

## Common mistakes

- Forgetting that $\Delta T$ must be a temperature difference, so 10 C to 40 C gives 30 K.
- Mixing volume and mass. One liter of water is about one kilogram, but that comes from the
  density of water. Use the density of the actual liquid when it is different.
- Reporting many significant figures. An estimate with three figures claims precision you do
  not have.
- Forgetting to convert joules to kWh before comparing with a utility bill.
- Hiding an assumption. If you ignore heat losses, say so, and say whether the true value is
  higher or lower.

## Go deeper

- [University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) by OpenStax: the thermodynamics chapters cover specific heat and energy balance.
- [Units and standards](https://openstax.org/books/university-physics-volume-1/pages/1-2-units-and-standards) by OpenStax: SI units and prefixes for converting J, kWh, and MJ.
- [SI units](https://www.nist.gov/pml/owm/metric-si/si-units) by NIST: the reference for the base and derived units used here.
- Polya, *How to Solve It* (1945), a printed book with a section on estimating and checking results. No link is given.
- [Problem-solving reference](reference.md): the lookup sheet for this topic.
