# Experiment design

**Type:** lesson

An experiment tests a question under controlled conditions. Good design decides what you change, what you hold still, how many times you repeat, and how you guard against bias. A well-designed experiment can answer a question with a modest number of runs. A poorly designed one wastes time even when the measurements are precise.

**Prerequisites:** [02 - Precision, accuracy, and uncertainty](02-precision-accuracy-and-uncertainty.md), [03 - Propagating uncertainty and significant figures](03-propagating-uncertainty-and-significant-figures.md)
**Time:** 6-8 h

## Core ideas

- **Factor** (or independent variable): a quantity you deliberately change, such as motor speed or material type.
- **Level**: a specific setting of a factor, such as 1000 rpm or 2000 rpm.
- **Response** (or dependent variable): the quantity you measure, such as vibration amplitude or temperature rise.
- **Control**: a run or group that does not receive the change, used as a baseline. A control shows what happens when the factor is absent.
- **Confounding variable**: something else that changes with the factor and can produce the same effect. Hold constants fixed, or record them, so you can separate effects.
- **Replication**: repeating a run under the same settings. It estimates random error and is what gives a standard deviation and a standard uncertainty of the mean.
- **Randomization**: running the trials in random order so that drift in equipment or room temperature does not line up with a factor.
- **Blocking**: grouping runs that share a known source of variation, such as one test day or one batch of material, so that the comparison is made within each block.
- **Full factorial design**: test every combination of levels. With $k$ factors at 2 levels each, you need $2^k$ runs.
- **Pilot study**: a small run to estimate the spread of the response, which you then use to choose the number of replicates.
- Write down the hypothesis, the response, the acceptance criterion, and the uncertainty budget before you start. Changing them after seeing data is a common source of false conclusions.

## Key equations

Required number of replicates $N$ to achieve a target standard uncertainty $u_{\text{target}}$ of the mean, given a pilot standard deviation $s$ (from lesson 02, $u(\bar{x}) = s / \sqrt{N}$):

$$N = \left(\frac{s}{u_{\text{target}}}\right)^2$$

Round $N$ up to the next whole number.

Number of runs in a full factorial design with $k$ factors at 2 levels each:

$$N_{\text{runs}} = 2^k$$

## Worked example

**Given:** A bench test measures the temperature rise of a motor winding. A pilot study of repeated runs at one setting gives a sample standard deviation of $s = 0.20$ °C. The goal is a mean temperature rise known to a standard uncertainty of 0.05 °C.

**Find:** (a) the number of replicates per setting, and (b) the number of runs needed if the test has three factors (load, speed, and ambient temperature) each at two levels, in a full factorial.

**Assumptions:** The pilot standard deviation is representative. The runs are independent and randomized. The factors are chosen to cover the expected operating range.

**Solution (a):**

$$N = \left(\frac{0.20}{0.05}\right)^2 = 4^2 = 16$$

Sixteen replicates per setting give $u(\bar{x}) = 0.20 / \sqrt{16} = 0.05$ °C.

**Solution (b):** With $k = 3$ factors at 2 levels, the full factorial has $2^3 = 8$ settings. If each setting needs 16 replicates, the total is $8 \times 16 = 128$ runs. That may be too many for a single test day, so a fractional design or blocking by day should be considered.

**Answer:** (a) 16 replicates per setting. (b) 8 settings, 128 runs total in a full factorial with 16 replicates each.

**Sanity check:** Halving the target uncertainty to 0.025 °C would require four times as many replicates (64).

## Practice

1. A pilot standard deviation is $s = 0.5$ units. The target uncertainty of the mean is 0.1 units. Find $N$.
2. An experiment has three factors at two levels each, with no replicates. How many runs are needed?
3. A pilot standard deviation is $s = 1.2$ units. The target uncertainty of the mean is 0.3 units. Find $N$.

<details><summary>Answers</summary>

1. 25
2. 8
3. 16

</details>

## Common mistakes

- Running all the trials of one setting in a row, so that time drift looks like a factor effect. Randomize the order.
- Using one replicate and reporting its value as the answer. A single run gives no estimate of random error.
- Changing the hypothesis or the response after seeing the data.
- Forgetting the square law. Halving the uncertainty costs four times as many replicates.
- Leaving out a control, which makes it hard to tell the factor's effect from background change.

## Go deeper

- [Introduction to Statistics (chapter 1)](https://openstax.org/books/introductory-statistics/pages/1-introduction) by OpenStax: sampling methods, data collection, and what separates good data from bad.
- [Introduction to Probability and Statistics (18.05)](https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2014/) by MIT OpenCourseWare: confidence intervals and hypothesis testing for comparing settings.
- [Guidelines for Evaluating and Expressing the Uncertainty of NIST Measurement Results (TN 1297)](https://www.nist.gov/pml/nist-technical-note-1297) by NIST: how to build an uncertainty budget from replicates and other components.
- [Measurement reference](reference.md): the lookup sheet for this topic.
