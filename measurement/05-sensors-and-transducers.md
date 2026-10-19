# Sensors and transducers

**Type:** lesson

A sensor is a device that turns a physical quantity, such as temperature, force, or position, into a signal you can measure. Engineers rely on sensors to tell a machine what is happening in the physical world around it.

A transducer is the broader term for any device that converts energy from one form to another, and most sensors are transducers.

**Prerequisites:** [Units and dimensional analysis](01-units-and-dimensional-analysis.md), [Precision, accuracy, and uncertainty](02-precision-accuracy-and-uncertainty.md)
**Time:** 4-6 h

## Core ideas

- The **measurand** is the quantity being measured, such as pressure, strain, or acceleration.
- A **transducer** converts the measurand into an electrical signal, such as a voltage, current, or resistance. The output is the signal the measurement system reads.
- **Sensitivity** is the slope of the input-output relationship: how much the output changes per unit change of input. Write it as output units per input unit, such as mV/bar.
- **Range** (or full scale) is the span of inputs the sensor can measure. **Span** is the difference between the highest and lowest output.
- **Zero offset** (or bias) is the output when the input is zero. Many industrial sensors use a live zero, where the minimum output is not zero. The common 4-20 mA current loop uses 4 mA for the minimum signal, so a broken wire (0 mA) is easy to spot.
- **Linearity** is how closely the output follows a straight line. A linear sensor has a constant sensitivity over its range. Nonlinearity is usually stated as a percent of full scale.
- **Hysteresis** is a difference in output when the input is rising versus falling. Repeatability is how well the output matches itself on repeated runs with the same input.
- **Calibration** compares the sensor output to known reference inputs and fits the relationship. A calibration certificate gives the uncertainty that must be carried forward.
- Common sensing principles: resistive (strain gauges, thermistors), thermoelectric (thermocouples), piezoelectric and capacitive (accelerometers, pressure sensors), and inductive (position sensors).

## Key equations

Sensitivity, from two calibration points $(x_1, y_1)$ and $(x_2, y_2)$:

$$S = \frac{y_2 - y_1}{x_2 - x_1}$$

Inverting a linear calibration to find the input from a measured output $y$:

$$x = \frac{y - y_0}{S}$$

where $y_0$ is the output at zero input (the zero offset) and $S$ is the sensitivity.

Full-scale accuracy, a common specification for industrial sensors, is a percent of the full-scale range $R$:

$$u_{\text{acc}} = \frac{a\%}{100} \times R$$

## Worked example

**Given:** A pressure transducer has a range of 0 to 10 bar. Its output is 4 mA at 0 bar and 20 mA at 10 bar, and it is linear. The data sheet states an accuracy of $\pm 0.5\%$ of full scale.

**Find:** (a) the sensitivity in mA/bar, (b) the pressure when the loop current reads 12.8 mA, and (c) its uncertainty from the accuracy specification.

**Assumptions:** The current measurement is perfect (we ignore its uncertainty). The sensor has the same sensitivity over the whole range.

**Solution (a):**

$$S = \frac{20\ \text{mA} - 4\ \text{mA}}{10\ \text{bar} - 0\ \text{bar}} = 1.6\ \text{mA/bar}$$

**Solution (b):** Use the zero offset $y_0 = 4$ mA:

$$P = \frac{12.8\ \text{mA} - 4\ \text{mA}}{1.6\ \text{mA/bar}} = 5.5\ \text{bar}$$

**Solution (c):** Full-scale accuracy is $0.5\% \times 10\ \text{bar} = 0.05$ bar. Treat this as the standard uncertainty for this example, which is a simple Type B estimate. The result is $5.50 \pm 0.05$ bar.

**Answer:** $S = 1.6\ \text{mA/bar}$; $P = 5.50 \pm 0.05\ \text{bar}$.

**Sanity check:** The midpoint of the range is 5 bar, which corresponds to $4 + 0.5 \times 16 = 12$ mA. The reading of 12.8 mA is a little above midpoint, and 5.5 bar is a little above 5 bar, which agrees.

## Practice

1. A pressure sensor is rated 0 to 100 psi with a linear output of 0 to 5 V. Find its sensitivity in V/psi, and the output at 64 psi.
2. Using the same sensor, the output reads 2.4 V. Find the pressure.
3. The 0 to 10 bar, 4-20 mA transducer from the worked example reads 20 mA. Find the pressure.

<details><summary>Answers</summary>

1. 0.05 V/psi; 3.2 V
2. 48 psi
3. 10 bar

</details>

## Common mistakes

- Assuming the zero output is zero. Check whether the sensor uses a live zero such as 4 mA.
- Using a two-point sensitivity from points that are not on the linear part of the curve.
- Reporting sensitivity without units, or with the units inverted (bar/mA instead of mA/bar).
- Treating the data-sheet accuracy as a percent of reading when it is stated as a percent of full scale. The difference is large at low readings.
- Forgetting that the measurement chain adds its own uncertainty, such as the resistor or ADC used to read the signal.

## Go deeper

- [Guidelines for Evaluating and Expressing the Uncertainty of NIST Measurement Results (TN 1297)](https://www.nist.gov/pml/nist-technical-note-1297) by NIST: how to carry sensor accuracy specifications into a combined uncertainty.
- [University Physics Volume 2, Chapter 10: Introduction](https://openstax.org/books/university-physics-volume-2/pages/10-introduction) by OpenStax: resistors and circuit basics that underpin resistive sensors.
- [Electronics (Wikibooks)](https://en.wikibooks.org/wiki/Electronics) by Wikibooks contributors: resistors and DC circuits, the basics behind resistive transducers.
- [Measurement reference](reference.md): the lookup sheet for this topic.
