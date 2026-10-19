# Reading calipers and micrometers

**Type:** lesson

Calipers and micrometers are hand tools that measure lengths such as shaft diameters and plate thicknesses, with resolution down to hundredths of a millimetre. Engineers must read them correctly, because most errors come from misreading the scales rather than from the tool itself.

**Prerequisites:** [Units and dimensional analysis](01-units-and-dimensional-analysis.md), [Precision, accuracy, and uncertainty](02-precision-accuracy-and-uncertainty.md)
**Time:** 3-5 h (plus practice on a real tool)

## Core ideas

- A **vernier caliper** has a fixed main scale (the **beam**) and a sliding jaw with a second scale called the **vernier**. Calipers measure outside, inside, and depth dimensions.
- The **vernier principle**: a short scale slides along a long scale, and the line that lines up shows a fraction of the main division. A common caliper has a vernier with 50 divisions that spans 49 mm of main scale. Each vernier division is $49/50 = 0.98$ mm, so the difference between one main division and one vernier division is $1.00 - 0.98 = 0.02$ mm. That is the resolution.
- A **micrometer** (outside micrometer) uses a screw instead of a sliding scale. One full turn of the thimble moves the spindle 0.5 mm. The thimble has 50 divisions, so each division is $0.5/50 = 0.01$ mm.
- The micrometer **sleeve** (barrel) has a main scale in millimeters, and a second row of marks, usually below the main line, shows the half millimeter. A half-line that is visible adds 0.5 mm to the sleeve reading.
- **Zero error** is the reading when the tool is closed. Check it before every series of measurements. If a closed micrometer reads $+0.02$ mm, subtract 0.02 mm from every reading.
- **Gauges** are fixed-size reference parts. A plug gauge or pin gauge checks a hole or shaft. A **go/no-go gauge** checks a tolerance band: the go side must enter, and the no-go side must not.
- Use gentle, consistent force, typically with the ratchet stop on a micrometer. Too much force squeezes the part and the frame.

## Key equations

Vernier caliper reading, where $N$ is the whole millimeters on the main scale just to the left of the vernier zero, and $n$ is the number of the vernier line that aligns best with a main-scale line:

$$L = N + n \times r \qquad r = \text{resolution (for a 50-division vernier, } r = 0.02\ \text{mm)}$$

Micrometer reading, where $S$ is the sleeve value in mm (including 0.5 if the half-line is showing), and $t$ is the thimble division in hundredths of a millimeter:

$$L = S + t \times 0.01\ \text{mm}$$

Standard uncertainty from resolution $\delta$, using the same approach as the precision, accuracy, and uncertainty lesson:

$$u = \frac{\delta}{2\sqrt{3}}$$

For the caliper, $\delta = 0.02$ mm, so $u = 0.0058$ mm. For the micrometer, $\delta = 0.01$ mm, so $u = 0.0029$ mm.

## Worked example

**Given:** A micrometer is used on a steel shaft. The sleeve shows 6 mm with the half-line visible, and the thimble line lines up with division 27. A closed-jaw check reads $+0.02$ mm.

**Find:** The corrected shaft diameter and its standard uncertainty.

**Assumptions:** The micrometer's resolution is 0.01 mm. Its zero error is stable over the measurement. The shaft is round at the measured point.

**Solution, step by step:**

1. Read the sleeve. The number 6 is the whole millimeters, and the half-line is visible, so the sleeve shows $6 + 0.5 = 6.5$ mm.
2. Read the thimble. The line on the thimble that sits on the sleeve reference line is 27, so add $27 \times 0.01 = 0.27$ mm.
3. Raw reading: $6.5 + 0.27 = 6.77$ mm.
4. Apply zero error. The closed reading was $+0.02$ mm, so subtract it: $6.77 - 0.02 = 6.75$ mm.
5. Uncertainty from resolution: $u = 0.01 / (2\sqrt{3}) = 0.0029$ mm, which we round to 0.003 mm.

**Answer:** Diameter $= 6.750 \pm 0.003$ mm.

**Sanity check:** Take the raw reading, 6.77 mm, and the corrected value, 6.75 mm. They differ by the zero error, 0.02 mm, which is correct. The result is about 6.75 mm, which sits between two common shaft sizes, so a go/no-go gauge is the right next check against the drawing tolerance.

## Practice

1. A vernier caliper with 50 divisions on 49 mm. The zero of the vernier sits just past the 41 mm main line, and vernier line 16 aligns best. Find the reading in mm.
2. A micrometer shows the sleeve at 8 mm with no half-line visible, and the thimble at division 36. Find the reading in mm.
3. A micrometer shows the sleeve at 7 mm with the half-line visible, and the thimble at division 12. Find the reading in mm.

<details><summary>Answers</summary>

1. 41.32 mm
2. 8.36 mm
3. 7.62 mm

</details>

## Common mistakes

- Reading the vernier line by the wrong main line. The vernier zero, not the nearest main mark, locates the whole millimeters.
- Forgetting the half-millimeter line on a micrometer sleeve, which causes an error of exactly 0.5 mm.
- Skipping the zero check, or ignoring a zero error that is not zero.
- Over-tightening the micrometer. Use the ratchet stop so every reading applies the same force.
- Reporting the resolution as the accuracy. Resolution limits the smallest reading; calibration and zero error limit accuracy.

## Go deeper

- [*Guidelines for Evaluating and Expressing the Uncertainty of NIST Measurement Results (TN 1297)*](https://www.nist.gov/pml/nist-technical-note-1297) by NIST: the Type B method for resolution-limited readings used above.
- [*University Physics Volume 1*, Chapter 1: Introduction](https://openstax.org/books/university-physics-volume-1/pages/1-introduction) by OpenStax: units, measurement, and estimates in physics context.

Note: no free tutorial specific to calipers and micrometers was confirmed for this lesson. Check the manufacturer's manual for your tool's scale layout, and use a real tool to practice.
- [Measurement reference](reference.md): the lookup sheet for this topic.
