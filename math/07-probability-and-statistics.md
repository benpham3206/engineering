# Probability and statistics

Probability describes uncertainty in a model. Statistics uses measured data to estimate what a process actually does. Engineers use both to set tolerances, judge whether a test result is real or noise, and estimate how often a part will fail.

**Prerequisites:** [Algebra](01-algebra.md), [Single-variable calculus](03-single-variable-calculus.md) for the continuous-distribution parts
**Time:** 30-45 h

## Core ideas

- A probability is a number from 0 to 1 that describes how likely an event is. Probabilities of all possible outcomes add to 1.
- Independent events do not affect each other. For independent events $A$ and $B$, $P(A \text{ and } B) = P(A)\,P(B)$.
- A random variable is a number assigned to each outcome. A discrete variable takes countable values (defective parts in a batch). A continuous variable takes any value in a range (a diameter in mm).
- The mean $\mu$ is the average value of the distribution. The standard deviation $\sigma$ measures spread. The sample standard deviation $s$ estimates $\sigma$ from data and divides by $n - 1$.
- The normal distribution is a bell curve defined by $\mu$ and $\sigma$. Many measurement errors are close to normal, and the Central Limit Theorem explains why averages tend toward it.
- A confidence interval gives a range that is likely to contain the true mean. A 95% interval means that if you repeated the experiment many times, about 95% of the intervals would contain the true value.
- Use the $t$-distribution instead of the normal when $\sigma$ is estimated from a small sample. For large samples, the two are nearly the same.
- Statistical significance is not the same as engineering importance. Always compare the size of an effect with the tolerance or the design margin.

## Key equations

Sample mean and sample standard deviation for $n$ values $x_i$:

$$\bar{x} = \frac{1}{n}\sum_{i=1}^n x_i, \qquad s = \sqrt{\frac{1}{n-1}\sum_{i=1}^n (x_i - \bar{x})^2}$$

Confidence interval for the mean (units of the data), with $t^*$ the critical value of the $t$-distribution with $n - 1$ degrees of freedom:

$$\bar{x} \pm t^*\,\frac{s}{\sqrt{n}}$$

Normal probability, where $Z = (x - \mu)/\sigma$ is the standard score and $\Phi$ is the standard normal cumulative distribution:

$$P(X > x) = 1 - \Phi\!\left(\frac{x - \mu}{\sigma}\right)$$

Binomial probability of exactly $k$ successes in $n$ independent trials with success probability $p$:

$$P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$$

## Worked example

**Given:** Ten measured diameters of a machined shaft (mm), nominally 25.00 mm:

25.02, 24.98, 25.01, 25.03, 24.99, 25.00, 25.02, 24.97, 25.01, 25.00

**Find:** (a) The sample mean and standard deviation. (b) A 95% confidence interval for the true mean diameter. (c) The probability that a single shaft exceeds 25.04 mm, assuming the process is normal with these estimates.

**Assumptions:** Measurements are independent and drawn from one normal process. Measurement error is small compared with the spread.

**Solution:**

1. Mean: $\bar{x} = 25.003\ \mathrm{mm}$.
2. Sample standard deviation with $n - 1 = 9$: $s = 0.01889\ \mathrm{mm}$.
3. Critical value: $t^* = 2.2622$ for 95% with 9 degrees of freedom.
4. Half-width: $2.2622 \times 0.01889 / \sqrt{10} = 0.01351\ \mathrm{mm}$. The interval is $25.003 \pm 0.0135$, so $[24.990, 25.017]\ \mathrm{mm}$.
5. Standard score for 25.04 mm: $Z = (25.04 - 25.003)/0.01889 = 1.96$. Then $P(X > 25.04) = 1 - \Phi(1.96) \approx 0.025$, which is about 2.5%.

**Answer:** Mean $25.003$ mm, $s = 0.0189$ mm. The 95% interval for the true mean is $24.990$ to $25.017$ mm. About 2.5% of shafts are expected above 25.04 mm.

**Sanity check:** The interval is narrow because $n = 10$ and the spread is small. The true mean is inside the nominal 25.00 mm band, so the process is centered. A 2.5% reject rate is a number a process engineer can act on.

## Practice

1. Find the mean and sample standard deviation of 4, 6, 8, and 10.
2. For a one-sided 95% bound on a normal variable, find the critical $z$ value. Give three decimal places.
3. Events $A$ and $B$ are independent with $P(A) = 0.2$ and $P(B) = 0.3$. Find $P(A \text{ and } B)$.
4. A batch has a defect probability $p = 0.1$ per part. Find the probability of exactly 2 defective parts in a sample of 10.

<details><summary>Answers</summary>

1. Mean $7$, sample standard deviation $\approx 2.582$
2. $z \approx 1.645$
3. $0.06$
4. $\approx 0.1937$

</details>

## Common mistakes

- Dividing by $n$ instead of $n - 1$ when computing the sample standard deviation.
- Calling a 95% interval "a 95% chance the true mean is inside." The probability statement applies to the procedure, not to one fixed interval.
- Using the normal distribution for a small sample without thinking about the $t$-distribution.
- Adding probabilities of events that overlap. Subtract the overlap.
- Treating a probability of exceeding a limit as a probability of failure without checking the physics.

## Go deeper

- [Engineering Statistics Handbook, section 1.3.5 Quantitative Techniques](https://www.itl.nist.gov/div898/handbook/eda/section3/eda35.htm) by NIST: confidence intervals, hypothesis tests, and outlier checks for engineering data.
- [Introductory Statistics](https://openstax.org/books/introductory-statistics/pages/1-introduction) by OpenStax: free textbook covering descriptive statistics, probability, and inference.
- Next: [Numerical methods](08-numerical-methods.md).
