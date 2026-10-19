# Precision, accuracy, and uncertainty

**Type:** lesson

Every measurement is an estimate. Accuracy tells you how close the estimate is to the true value, precision tells you how well repeated estimates agree, and uncertainty is the size of the doubt that remains.

**Prerequisites:** [Units and dimensional analysis](01-units-and-dimensional-analysis.md), [Probability and statistics](../math/07-probability-and-statistics.md) (mean and standard deviation)
**Time:** 6-8 h

## Core ideas

- **Accuracy** is closeness to the true value. Accuracy is limited by **systematic errors**, which push every reading the same way, such as a miscalibrated scale or a zero that is off by 0.02 mm.
- **Precision** is how tightly repeated readings cluster. Precision is limited by **random errors**, which change from reading to reading, such as hand jitter or electrical noise.
- A measurement can be precise but not accurate (tight cluster, wrong center) or accurate but not precise (centered, but spread out). Good work needs both.
- **Resolution** is the smallest change an instrument can show. A ruler marked in millimeters has a resolution of 1 mm, but you can usually estimate a fraction of that.
- **Uncertainty** is a range you attach to a result, written as $x \pm u$. It says where the true value is likely to lie.
- A **standard uncertainty**, $u$, is one standard deviation of the estimate. A **Type A** evaluation estimates $u$ from repeated readings. A **Type B** evaluation estimates $u$ from other information, such as a calibration certificate or the resolution of the instrument.
- For a reading limited only by resolution $\delta$ (the smallest step), a common Type B estimate is $u = \frac{\delta}{2\sqrt{3}}$, which assumes the true value is equally likely anywhere in the step. The NIST technical note on uncertainty explains this Type B approach.
- **Relative uncertainty** is $u/|x|$, often shown as a percent. It makes it easier to compare a small error on a small number with a small error on a big number.

## Key equations

Sample mean of $N$ readings $x_i$:

$$\bar{x} = \frac{1}{N}\sum_{i=1}^{N} x_i$$

Sample standard deviation, in the same units as the readings:

$$s = \sqrt{\frac{1}{N-1}\sum_{i=1}^{N}(x_i - \bar{x})^2}$$

Standard uncertainty of the mean (Type A), which shrinks as $1/\sqrt{N}$:

$$u(\bar{x}) = \frac{s}{\sqrt{N}}$$

Percent error against a known true value $x_{\text{true}}$:

$$\%\text{ error} = \frac{\bar{x} - x_{\text{true}}}{x_{\text{true}}} \times 100\%$$

## Worked example

**Given:** A machinist measures the same steel block ten times with a digital micrometer. The readings in mm are: 25.08, 25.12, 25.10, 25.07, 25.11, 25.09, 25.13, 25.10, 25.06, 25.11.

**Find:** The mean, the standard uncertainty of the mean, and whether a block certified at 25.10 mm is consistent with the data.

**Assumptions:** Readings are independent, the instrument has no significant bias, and the certified value of 25.10 mm is accurate to about 0.002 mm.

**Solution:**

- Sum of readings is 250.97 mm, so $\bar{x} = 250.97 / 10 = 25.097\ \text{mm}$.
- Sample standard deviation: $s = 0.0221\ \text{mm}$ (computed with Python's `statistics.stdev`).
- Standard uncertainty of the mean: $u(\bar{x}) = 0.0221 / \sqrt{10} = 0.0070\ \text{mm}$.
- Result: $25.097 \pm 0.007\ \text{mm}$.
- Consistency check: the difference from the certified value is $25.097 - 25.10 = -0.003\ \text{mm}$. The combined uncertainty is $\sqrt{0.007^2 + 0.002^2} = 0.0073\ \text{mm}$. The difference, 0.003 mm, is smaller than that, so the data agree with the certificate.

**Answer:** $\bar{x} = 25.097\ \text{mm}$, $u(\bar{x}) = 0.007\ \text{mm}$. The mean agrees with the certified 25.10 mm.

**Sanity check:** The full spread of single readings is $25.13 - 25.06 = 0.07$ mm, and $s = 0.022$ mm. The uncertainty of the mean (0.007 mm) is smaller than the spread of single readings, as expected when averaging ten readings.

## Practice

1. Find the mean and standard deviation of 10.2, 10.4, 10.3, 10.5, 10.1 (mm). Give the standard uncertainty of the mean.
2. A voltmeter reads 9.82 V for a reference of 10.00 V. Find the error and the percent error.
3. A digital meter has a resolution of 0.1 V. Using $u = \delta / (2\sqrt{3})$, find its standard uncertainty.

<details><summary>Answers</summary>

1. Mean 10.3 mm, standard deviation 0.158 mm, standard uncertainty of the mean 0.071 mm.
2. Error -0.18 V, percent error -1.8%.
3. 0.029 V.

</details>

## Common mistakes

- Using $N$ instead of $N-1$ in the standard deviation for a sample. Most calculators and Python use $N-1$ by default for sample statistics.
- Reporting more digits than the uncertainty justifies. If $u = 0.007$ mm, a mean of 25.09712 mm is false precision.
- Averaging readings and then treating the spread of the average as the spread of single readings. Use $s/\sqrt{N}$ for the mean.
- Treating repeated readings as proof of accuracy. Ten precise readings from a bad instrument are still wrong.
- Forgetting that a calibration certificate has its own uncertainty, which you must include.

## Go deeper

- [Guidelines for Evaluating and Expressing the Uncertainty of NIST Measurement Results (TN 1297)](https://www.nist.gov/pml/nist-technical-note-1297) by NIST: the standard reference on Type A and Type B evaluation and standard uncertainty.
- [Introduction to Statistics (chapter 1)](https://openstax.org/books/introductory-statistics/pages/1-introduction) by OpenStax: data, sampling, and the vocabulary of statistics.
- [Introduction to Probability and Statistics (18.05)](https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2014/) by MIT OpenCourseWare: probability, confidence intervals, and hypothesis testing.
- [Measurement reference](reference.md): the lookup sheet for this topic.
