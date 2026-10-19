# Data analysis and reporting

**Type:** lesson

Raw readings become useful only after you summarize them, fit a model to them, and report the result with its uncertainty. This lesson covers the core tools: the mean and standard deviation, a straight-line fit by least squares, residuals to check the fit, and a reporting format that another engineer can check.

**Prerequisites:** [Precision, accuracy, and uncertainty](02-precision-accuracy-and-uncertainty.md), [Propagating uncertainty and significant figures](03-propagating-uncertainty-and-significant-figures.md), [Experiment design](09-experiment-design.md), [Probability and statistics](../math/07-probability-and-statistics.md) (least-squares fits)
**Time:** 8-10 h

## Core ideas

- **Summary statistics** describe a set of readings: the mean (center), the sample standard deviation (spread), and the number of readings $N$. Always report the number of readings with the mean.
- A **least-squares fit** finds the straight line $y = a + b x$ that minimizes the sum of squared differences between the data and the line. It is the standard method when $y$ has random error and $x$ is known well.
- A **residual** is the difference between a data point and the fitted line: $r_i = y_i - (a + b x_i)$. Plot residuals to check the fit. Random scatter around zero is good. A curve or trend in the residuals means the straight line is the wrong model.
- The **coefficient of determination** $R^2$ is the fraction of the variation in $y$ explained by the line. It is useful, but a high $R^2$ does not prove the model is right. Look at the residuals too.
- The **standard uncertainties** of the slope and intercept come from the scatter of the residuals and the spread of the $x$ values. Report them alongside $a$ and $b$.
- A **result** is reported as value $\pm$ standard uncertainty, with units, the number of readings, and a short statement of the method. Use the sig figs rules from the propagating uncertainty and significant figures lesson.
- Keep the raw data. Anyone should be able to reproduce your fit from the table.

## Key equations

Least-squares slope and intercept, for $N$ points $(x_i, y_i)$, with $\bar{x}$ and $\bar{y}$ the means:

$$b = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} \qquad a = \bar{y} - b\,\bar{x}$$

Standard deviation of the residuals (with $N - 2$ degrees of freedom, because two parameters were fitted):

$$s_r = \sqrt{\frac{\sum r_i^2}{N - 2}}$$

Standard uncertainties of the slope and intercept:

$$u(b) = \frac{s_r}{\sqrt{\sum (x_i - \bar{x})^2}} \qquad u(a) = s_r \sqrt{\frac{1}{N} + \frac{\bar{x}^2}{\sum (x_i - \bar{x})^2}}$$

## Worked example

**Given:** A sensor is calibrated against six known inputs $x$ (in some unit), giving the readings $y$ in the same unit, plus a noise term:

| $x$ | 1.0 | 2.0 | 3.0 | 4.0 | 5.0 | 6.0 |
|---|---|---|---|---|---|---|
| $y$ | 2.1 | 3.9 | 6.2 | 7.8 | 10.1 | 12.2 |

**Find:** (a) the slope and intercept with their standard uncertainties, (b) $R^2$, and (c) a report line.

**Assumptions:** The relationship is linear. Errors in $y$ are random and independent, and $x$ is known much more accurately than $y$.

**Solution (a):**

- Means: $\bar{x} = 3.5$, $\bar{y} = 7.05$
- $\sum (x_i - \bar{x})^2 = 17.5$, and $\sum (x_i - \bar{x})(y_i - \bar{y}) = 35.35$
- Slope: $b = 35.35 / 17.5 = 2.020$
- Intercept: $a = 7.05 - 2.020 \times 3.5 = -0.020$
- Residuals: $r_i = y_i - (a + bx_i)$ give a sum of squares near 0.128, so $s_r = \sqrt{0.128/4} = 0.179$
- $u(b) = 0.179 / \sqrt{17.5} = 0.043$
- $u(a) = 0.179 \times \sqrt{1/6 + 3.5^2/17.5} = 0.167$

**Solution (b):** $R^2 = 1 - \sum r_i^2 / \sum (y_i - \bar{y})^2 = 1 - 0.128 / 71.5 = 0.998$

**Solution (c):** Report in the usual format: $b = 2.02 \pm 0.04$ (units per unit of $x$), $a = -0.02 \pm 0.17$, from $N = 6$ points. Fit $y = a + bx$, $R^2 = 0.998$.

**Answer:** Slope $2.02 \pm 0.04$; intercept $-0.02 \pm 0.17$; $R^2 = 0.998$.

**Sanity check:** The data are close to $y \approx 2x$, which matches the slope of 2.02. The intercept is near zero and its uncertainty (0.17) is larger than its value, which is what you expect when the true intercept is zero. The residuals are small compared with the readings, so the straight line is a reasonable model.

## Practice

1. Six repeated readings are 5.02, 4.98, 5.05, 4.97, 5.01, 5.03. Find the mean, the sample standard deviation, and the standard uncertainty of the mean, and report the result to the correct sig figs.
2. Report the value 0.0456789 kg with a standard uncertainty of 0.0003 kg.
3. Using the fit from the worked example, predict $y$ at $x = 7.0$.

<details><summary>Answers</summary>

1. Mean 5.01; standard deviation 0.0303; standard uncertainty of the mean 0.012. Report $5.010 \pm 0.012$.
2. $0.0457 \pm 0.0003$ kg
3. 14.12

</details>

## Common mistakes

- Reporting the fit without the number of points, the units, or the uncertainty of the slope and intercept.
- Trusting $R^2$ alone. Plot the residuals, because a curved trend can still give a high $R^2$.
- Dividing by $N$ instead of $N - 2$ for the residual standard deviation. The two extra degrees of freedom are used by the fitted line.
- Extrapolating far beyond the calibrated range, where the straight line may no longer hold.
- Rounding intermediate values too early. Keep extra digits until the end, then round the result.

## Go deeper

- [Introduction to Statistics (chapter 1)](https://openstax.org/books/introductory-statistics/pages/1-introduction) by OpenStax: descriptive statistics, data collection, and the vocabulary of analysis.
- [Introduction to Probability and Statistics (18.05)](https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2014/) by MIT OpenCourseWare: linear regression and confidence intervals.
- [Guidelines for Evaluating and Expressing the Uncertainty of NIST Measurement Results (TN 1297)](https://www.nist.gov/pml/nist-technical-note-1297) by NIST: how to combine uncertainty components and report a final result.
- [Measurement reference](reference.md): the lookup sheet for this topic.
