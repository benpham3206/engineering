# Strain gauges and the Wheatstone bridge

**Type:** lesson

A **strain gauge** is a thin resistive wire or foil bonded to a part to measure how much the part stretches or squeezes, and a Wheatstone bridge is a resistor circuit that turns the gauge's small resistance change into a voltage an instrument can read. Engineers use the pair to find how hard a part is loaded without breaking it.

When the part stretches or squeezes, the gauge's resistance changes by a tiny, measurable amount.

**Prerequisites:** [Sensors and transducers](05-sensors-and-transducers.md), [Units and dimensional analysis](01-units-and-dimensional-analysis.md), [Electricity and magnetism](../physics/06-electricity-and-magnetism.md) (resistors and voltage dividers)
**Time:** 6-8 h

## Core ideas

- **Strain** $\varepsilon$ is the fractional change in length, $\varepsilon = \Delta L / L$. It is dimensionless. Strain in engineering is tiny, so it is often written in microstrain ($\mu\varepsilon$), where $1\ \mu\varepsilon = 10^{-6}$.
- A **gauge factor** $\mathrm{GF}$ relates the fractional resistance change to strain. For metal foil gauges, $\mathrm{GF}$ is typically near 2.
- A **Wheatstone bridge** has four resistive arms in a diamond shape. Excitation voltage $V_{\text{ex}}$ is applied across two opposite corners, and the output voltage $V_{\text{out}}$ is measured across the other two corners.
- The bridge is **balanced** when $R_1 / R_2 = R_3 / R_4$. Then $V_{\text{out}} = 0$, even with excitation applied. Balancing lets a small change show up as a clean voltage.
- A **quarter bridge** has one active gauge and three fixed resistors. A **half bridge** uses two active gauges, and a **full bridge** uses four. More active arms give more output and better temperature compensation.
- A **dummy gauge** on an unstressed piece of the same material cancels temperature effects, because both gauges change together while only the active one sees strain.
- Gauge resistance is often 120, 350, or 1000 ohms. Lead wires add resistance and can cause errors if they are long; a three-wire or four-wire connection helps.

## Key equations

Gauge resistance change from strain:

$$\frac{\Delta R}{R} = \mathrm{GF} \cdot \varepsilon$$

Quarter-bridge output, with one active arm $R + \Delta R$ and three fixed arms $R$, excitation $V_{\text{ex}}$ in volts (V):

$$V_{\text{out}} = V_{\text{ex}} \left[\frac{R + \Delta R}{2R + \Delta R} - \frac{1}{2}\right]$$

For small strain, where $\Delta R \ll R$, the output simplifies to

$$V_{\text{out}} \approx \frac{V_{\text{ex}} \cdot \mathrm{GF} \cdot \varepsilon}{4}$$

Balance condition: $\quad R_1 / R_2 = R_3 / R_4$

## Worked example

**Given:** A steel bar has a foil gauge with $R = 350\ \Omega$ and $\mathrm{GF} = 2.0$. The bar sees a strain of $500\ \mu\varepsilon$. The bridge is a quarter bridge with $V_{\text{ex}} = 5.0$ V.

**Find:** (a) the resistance change $\Delta R$, (b) the bridge output using the exact formula, (c) the output using the small-strain approximation, and (d) the difference between the two.

**Assumptions:** The three fixed resistors are exactly 350 $\Omega$, the gauge is not heated, and the strain is uniform over the gauge.

**Solution:**

- Strain: $\varepsilon = 500 \times 10^{-6} = 5.00 \times 10^{-4}$
- (a) Fractional change: $\Delta R / R = \mathrm{GF} \cdot \varepsilon = 2.0 \times 5.00 \times 10^{-4} = 1.00 \times 10^{-3}$. So $\Delta R = 350 \times 1.00 \times 10^{-3} = 0.350\ \Omega$.
- (b) Exact: $V_{\text{out}} = 5.0 \times \left[\frac{350.35}{700.35} - \frac{1}{2}\right] = 1.2494 \times 10^{-3}\ \text{V} = 1.2494\ \text{mV}$
- (c) Approximation: $V_{\text{out}} \approx 5.0 \times 2.0 \times 5.00 \times 10^{-4} / 4 = 1.250\ \text{mV}$
- (d) Difference: $(1.2494 - 1.250) / 1.250 = -0.05\%$

**Answer:** $\Delta R = 0.350\ \Omega$. $V_{\text{out}} = 1.25\ \text{mV}$ (exact 1.2494 mV, a difference of 0.05%).

**Sanity check:** The output is in the millivolt range, which is typical for a bridge with a few volts of excitation and microstrain-level strain. The exact and approximate answers agree to within a tenth of a percent, so the small-strain form is safe at this level.

## Practice

1. A gauge has $\mathrm{GF} = 2.1$ and sees $800\ \mu\varepsilon$. Find $\Delta R/R$ and, for a $120\ \Omega$ gauge, $\Delta R$ in ohms.
2. The same quarter bridge as question 1, with $R = 120\ \Omega$ and $V_{\text{ex}} = 10.0$ V. Find the exact $V_{\text{out}}$ in mV.
3. A gauge with $\mathrm{GF} = 2.0$ shows $\Delta R/R = 0.00042$. Find the strain in $\mu\varepsilon$.

<details><summary>Answers</summary>

1. $\Delta R/R = 0.00168$; $\Delta R = 0.2016\ \Omega$
2. 4.196 mV
3. 210 $\mu\varepsilon$

</details>

## Common mistakes

- Mixing microstrain and strain. $500\ \mu\varepsilon$ is $5 \times 10^{-4}$, not $500$.
- Forgetting the factor of 4 when using the small-strain approximation for a quarter bridge.
- Using the gauge factor from a different gauge or material. $\mathrm{GF}$ is a property of the gauge.
- Ignoring temperature effects. Without a dummy gauge or compensation, temperature can cause a larger apparent strain than the load does.
- Assuming a balanced bridge means no excitation. A balanced bridge has zero output, not zero excitation.

## Go deeper

- [*University Physics Volume 2*, Chapter 10: Introduction](https://openstax.org/books/university-physics-volume-2/pages/10-introduction) by OpenStax: Kirchhoff's rules and resistors in series and parallel, needed for bridge analysis.
- [6.002 Circuits and Electronics (Spring 2007)](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/) by MIT OpenCourseWare: resistive networks and sources, the circuit foundation for bridges.
- [*Electronics* (Wikibooks)](https://en.wikibooks.org/wiki/Electronics) by Wikibooks contributors: resistors and DC circuits.

The bridge equations above follow from Kirchhoff's rules.
- [Measurement reference](reference.md): the lookup sheet for this topic.
