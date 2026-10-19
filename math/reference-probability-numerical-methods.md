# Probability, statistics, and numerical methods reference

**Type:** reference
**Verify:** strict

Lookup sheet for probability, statistics, and the numerical methods that replace an exact answer with a checkable approximation, for an engineer who needs a formula, an error order, or a sanity check in the middle of a job.

## Principles

- A probability model is an assumption about a process, not a fact about it. Every result is only as good as the independence, stationarity, and distribution shape assumed.
- A statistic computed from a sample is itself random. Report it with its uncertainty, never as a bare number.
- Statistical significance measures how surprising data are under a null model. It says nothing about whether an effect is large enough to matter against a tolerance.
- A numerical answer is an approximation with two error sources, truncation (the method) and round-off (the arithmetic). Know which one dominates before refining.
- The order of a method is the power of the step size in its error. Halving $h$ cuts the error of a method of order $p$ by about $2^p$. Measure the order; do not assume it.
- Refine and compare. A result that does not change when the step or grid is halved is converged; a result that moves is not.
- Stability and conditioning decide whether a correct formula gives a usable number. A small input error can become a large output error with no bug anywhere.
- Consistency plus stability gives convergence. A consistent scheme that is unstable gives garbage that gets worse as the step shrinks.
- Test against a case with a known answer before trusting code on a case without one.

## Probability rules and Bayes' theorem

An **event** is a set of outcomes, and its **probability** $\Pr(A)$ is a number from 0 to 1 that measures how likely the event is. Probabilities of all mutually exclusive outcomes that cover every case add to 1.

$$\Pr(A \cup B) = \Pr(A) + \Pr(B) - \Pr(A \cap B)$$

$$\Pr(A \mid B) = \frac{\Pr(A \cap B)}{\Pr(B)}, \qquad \Pr(B \mid A) = \frac{\Pr(A \mid B)\,\Pr(B)}{\Pr(A)}$$

$$\Pr(A) = \sum_i \Pr(A \mid B_i)\,\Pr(B_i)$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\Pr(A)$ | probability of event $A$ | dimensionless |
| $A \cup B$, $A \cap B$ | $A$ or $B$ occurs; $A$ and $B$ both occur | dimensionless |
| $\Pr(A \mid B)$ | probability of $A$ given that $B$ occurred | dimensionless |
| $B_i$ | events that do not overlap and together cover every outcome | dimensionless |

Holds when: events are well defined and the $B_i$ partition the outcomes. Independence ($\Pr(A \cap B) = \Pr(A)\Pr(B)$) is an extra assumption, used only when it is justified.
Breaks when: independence is assumed for events that share a cause (two sensors on one power supply fail together), or when the prior $\Pr(B)$ is guessed and the result is quoted as if it were measured.
Source and basis: derived from the axioms of probability and the definition of conditional probability; taught in [Probability and statistics](07-probability-and-statistics.md).

Example. A fault occurs with probability 0.01 per unit. A test flags a faulty unit with probability 0.95 and flags a good unit with probability 0.05. Given a flag, the chance the unit is faulty is $\Pr(D \mid +) = 0.95 \times 0.01 / (0.95 \times 0.01 + 0.05 \times (1 - 0.01)) = 0.161$. Most flags are false alarms because faults are rare. Always compute the base-rate term before trusting a test.

```verify
p_d = q(0.01, "")
sens = q(0.95, "")
fp = q(0.05, "")
num = sens * p_d
den = sens * p_d + fp * (1 - p_d)
expect(num / den, "0.161")
```

## Random variables and moments

A **random variable** $X$ assigns a number to each outcome. Its **expected value** $\mathrm{E}[X]$ is the probability-weighted average, and its **variance** $\mathrm{Var}(X)$ is the expected squared distance from that average.

$$\mu_X = \mathrm{E}[X] = \sum_i x_i\, p_i \quad \text{or} \quad \int x f(x)\,dx, \qquad \mathrm{Var}(X) = \mathrm{E}[X^2] - \mu_X^2$$

$$\mathrm{E}[aX + b] = a\mu_X + b, \qquad \mathrm{Var}(aX + b) = a^2\,\mathrm{Var}(X)$$

$$\mathrm{Var}(X + Y) = \mathrm{Var}(X) + \mathrm{Var}(Y) + 2\,\mathrm{Cov}(X, Y)$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $X$, $Y$ | random variables | dimensionless |
| $x_i$, $p_i$ | possible values and their probabilities | dimensionless |
| $f(x)$ | probability density of a continuous variable | dimensionless |
| $\mu_X$ | mean of $X$ | dimensionless |
| $\mathrm{Var}(X)$ | variance of $X$ | dimensionless |
| $a$, $b$ | constants | dimensionless |
| $\mathrm{Cov}(X, Y)$ | covariance of $X$ and $Y$ | dimensionless |

Holds when: the moments exist (the sums or integrals converge). The linearity of $\mathrm{E}$ holds always; the variance sum rule with $\mathrm{Cov} = 0$ needs the variables to be uncorrelated.
Breaks when: the distribution is heavy tailed enough that the variance is infinite (Cauchy), or when variables are correlated and the covariance term is dropped. A tolerance stack of correlated dimensions is not the root-sum-square of the parts.
Source and basis: derived from the definition of expectation; taught in [Probability and statistics](07-probability-and-statistics.md). Propagation of measurement uncertainty is owned by the [Measurement reference](../measurement/reference.md).

Example. A fair die has $\mu = 3.5$ and $\mathrm{E}[X^2] = 91/6$, so $\mathrm{Var}(X) = 91/6 - 3.5^2 = 2.917$. Scaling it to $2X + 1$ gives variance $4 \times 2.917 = 11.67$.

```verify
ex2 = q(91, "") / 6
mu = q(3.5, "")
var = ex2 - mu**2
expect(var, "2.917")
expect(4 * var, "11.67")
```

## Distributions

A **distribution** is the rule that gives the probability of each value (or range of values) of a random variable. The table lists what each common one models, its mean, and its variance. Use the support (the allowed values) to pick a candidate, then check the fit against data.

| Distribution | Models | Mean | Variance |
|---|---|---|---|
| Binomial($n$, $p$) | number of successes in $n$ independent trials, success probability $p$ | $np$ | $np(1-p)$ |
| Poisson($\lambda$) | count of rare independent events in a fixed interval, mean count $\lambda$ | $\lambda$ | $\lambda$ |
| Uniform($a$, $b$) | a value equally likely anywhere in $[a, b]$ | $(a+b)/2$ | $(b-a)^2/12$ |
| Normal($\mu$, $\sigma^2$) | sum of many small independent effects; measurement error | $\mu$ | $\sigma^2$ |
| Lognormal | positive quantity whose logarithm is normal; product of many small factors | $e^{m + s^2/2}$ | $\left(e^{s^2} - 1\right) e^{2m + s^2}$ |
| Exponential($\lambda$) | waiting time between independent events at constant rate $\lambda$ | $1/\lambda$ | $1/\lambda^2$ |
| Student $t$, $\nu$ degrees of freedom | standardized sample mean when $\sigma$ is estimated | $0$ for $\nu > 1$ | $\nu/(\nu - 2)$ for $\nu > 2$ |
| Chi-square, $k$ degrees of freedom | sum of $k$ squared independent standard normals; sample variance scaling | $k$ | $2k$ |

- Probability mass and density functions: binomial $\Pr(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$; Poisson $\Pr(X = k) = \lambda^k e^{-\lambda}/k!$; exponential $\Pr(T > t) = e^{-\lambda t}$ for $t \ge 0$; normal density $\frac{1}{\sigma\sqrt{2\pi}}\exp[-(x-\mu)^2/(2\sigma^2)]$.
- For the lognormal, $m$ and $s$ are the mean and standard deviation of $\ln X$. Its median is $e^m$, below its mean.
- Poisson approximates Binomial($n$, $p$) when $n$ is large, $p$ is small, and $\lambda = np$.
- The sum of independent normals is normal, with means added and variances added.
- Central limit theorem: the mean of many independent draws with finite variance is close to normal, whatever the parent shape. The closeness depends on skewness and $n$.
- Normal coverage, two-sided, typical rounded values: $\pm 1\sigma$ holds 68.27 percent, $\pm 2\sigma$ holds 95.45 percent, $\pm 3\sigma$ holds 99.73 percent.
- Lifetime and failure-rate models (exponential in the reliability setting, Weibull) are owned by the reliability reference [design/reference-reliability.md](../design/reference-reliability.md).

Holds when: the process matches the stated model: independent trials for the binomial, a constant rate with no memory for the Poisson and exponential, a log-scale sum of small effects for the lognormal.
Breaks when: trials are dependent (overdispersed counts), the rate changes with time or load (wear-out is not exponential), or the tails are heavier than normal. A normal tail beyond $4\sigma$ is a model prediction and is often orders of magnitude optimistic.
Source and basis: derived from the definitions of the distributions; the moments follow by summation or integration. Taught in [Probability and statistics](07-probability-and-statistics.md).

Examples. Binomial with $n = 10$ and $p = 0.1$ gives $\Pr(X = 2) = 45 \times 0.1^2 \times 0.9^8 = 0.1937$. Poisson with $\lambda = 3$ gives $\Pr(X = 2) = 9 e^{-3} / 2 = 0.2240$. Exponential with $\lambda = 0.5$ per hour gives $\Pr(T > 2\ \text{h}) = e^{-1} = 0.3679$. A lognormal with $m = 0$ and $s = 0.5$ has mean $1.133$, variance $0.3647$, and median $1$. A uniform on $[0, 12]$ mm has variance $12$ $\text{mm}^{2}$.

```verify
p = q(0.1, "")
expect(q(45, "") * p**2 * (1 - p)**8, "0.1937")
lam = q(3, "")
expect(lam**2 * exp(-lam) / 2, "0.2240")
r = q(0.5, "1/h")
t = q(2, "h")
expect(exp(-r * t), "0.3679")
s = q(0.5, "")
expect(exp(s**2 / 2), "1.133")
expect((exp(s**2) - 1) * exp(s**2), "0.3647")
a = q(0, "mm")
b = q(12, "mm")
expect((b - a)**2 / 12, "12 mm^2")
```

## Sampling and estimation

A **sample** is $n$ measurements drawn from a process. The **sample mean** $\bar{x}$ and **sample standard deviation** $s$ estimate the process mean and spread. The **standard error** is the standard deviation of $\bar{x}$ itself.

$$\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i, \qquad s = \sqrt{\frac{1}{n-1}\sum_{i=1}^{n}(x_i - \bar{x})^2}, \qquad \text{SE} = \frac{s}{\sqrt{n}}$$

$$\bar{x} \pm t^{*}\,\frac{s}{\sqrt{n}}, \qquad n \ge \left(\frac{z\,\sigma}{E}\right)^2$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $x_i$ | measured values | mm |
| $n$ | sample size | dimensionless |
| $\bar{x}$ | sample mean | mm |
| $s$ | sample standard deviation | mm |
| $\sigma$ | process standard deviation, known or planning value | mm |
| $\text{SE}$ | standard error of the mean | mm |
| $t^{*}$ | two-sided critical value of the $t$ distribution with $n-1$ degrees of freedom | dimensionless |
| $z$ | two-sided critical value of the standard normal | dimensionless |
| $E$ | required half-width of the interval | mm |

Holds when: observations are independent draws from one stable process that is close to normal (or $n$ is large enough for the central limit theorem). The sample-size form needs a planning value of $\sigma$ and uses the normal critical value.
Breaks when: observations are autocorrelated (consecutive readings from one drifting instrument), the process changes during sampling, or the sample is small and the data are skewed. Then the interval is too narrow and its stated confidence is false. The interval describes the mean, not where individual parts fall; a prediction interval for one new part is wider, $\bar{x} \pm t^{*} s \sqrt{1 + 1/n}$.
Source and basis: derived from the variance of a mean of independent variables, $\mathrm{Var}(\bar{X}) = \sigma^2/n$; taught in [Probability and statistics](07-probability-and-statistics.md).

A 95 percent confidence interval means the procedure captures the true mean in 95 percent of repeated experiments. It is not a 95 percent chance for this one interval.

Typical two-sided critical values, rounded:

| Confidence | $z$ | $t^{*}$ at 4 df | $t^{*}$ at 9 df | $t^{*}$ at 29 df |
|---|---|---|---|---|
| 90 percent | 1.645 | 2.132 | 1.833 | 1.699 |
| 95 percent | 1.960 | 2.776 | 2.262 | 2.045 |
| 99 percent | 2.576 | 4.604 | 3.250 | 2.756 |

Example. Ten shaft diameters have $\bar{x} = 25.003$ mm and $s = 0.01889$ mm. With $t^{*} = 2.262$ at 9 df, the half-width is $2.262 \times 0.01889 / \sqrt{10} = 0.01351$ mm, so the interval is $25.003 \pm 0.01351$ mm. To pin the mean within $E = 0.01$ mm at the confidence level that gives $z = 1.96$, with a planning $\sigma = 0.02$ mm and $z = 1.96$, $n \ge (1.96 \times 0.02 / 0.01)^2 = 15.37$, so take $n = 16$.

```verify
xbar = q(25.003, "mm")
s = q(0.01889, "mm")
n = q(10, "")
tstar = given("2.262")
tc = q(2.262, "")
expect(tc * s / sqrt(n), "0.01351 mm")
sig = q(0.02, "mm")
E = q(0.01, "mm")
z = q(1.96, "")
expect((z * sig / E)**2, "15.37")
given("16")
```

## Hypothesis tests

A **hypothesis test** asks whether data are too surprising to be explained by a stated null model. The **p value** is the probability, if the null model were true, of a result at least as extreme as the one observed.

$$t = \frac{\bar{x} - \mu_0}{s/\sqrt{n}}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $t$ | test statistic, with $n-1$ degrees of freedom under the null model | dimensionless |
| $\bar{x}$ | sample mean | mm |
| $\mu_0$ | mean claimed by the null hypothesis | mm |
| $s$ | sample standard deviation | mm |
| $n$ | sample size | dimensionless |

Holds when: the data are independent and close to normal, and the claimed mean $\mu_0$ and the test direction (one-sided or two-sided) were fixed before looking at the data.
Breaks when: many tests are run and only the significant one is reported (the chance of a false positive grows with the number of looks), when the data are paired but treated as independent, or when $n$ is so large that a trivial difference gives a tiny p value.
Source and basis: derived from the distribution of $(\bar{X} - \mu)/(s/\sqrt{n})$ for normal data; taught in [Probability and statistics](07-probability-and-statistics.md). Handbook treatment: NIST/SEMATECH e-Handbook of Statistical Methods, which the further reference lists.

Decision rule: reject the null model at significance level $\alpha$ when $|t|$ exceeds the two-sided critical value $t^{*}$ for $n - 1$ degrees of freedom.

What a p value is not:

- It is not the probability that the null model is true.
- It is not the probability that the result came from chance alone.
- It does not measure the size of an effect. Compare the estimated difference and its interval with the tolerance or design margin.
- A large p value does not show that no effect exists. It shows the data were too few or too noisy to see one. Report the interval.

Example. Test whether the process mean differs from $\mu_0 = 25.000$ mm using the data above. The statistic is $t = (25.003 - 25.000)/(0.01889/\sqrt{10}) = 0.502$. The critical value is $2.262$, so the data do not reject the null model. The offset of the sample mean from $\mu_0$ is well inside the noise.

```verify
xbar = q(25.003, "mm")
mu0 = q(25.000, "mm")
s = q(0.01889, "mm")
n = q(10, "")
expect((xbar - mu0) / (s / sqrt(n)), "0.502")
check(abs((xbar - mu0) / (s / sqrt(n))) < q(2.262, ""), "below the critical value")
```

## Regression

**Linear least squares** fits a line $\hat{y} = a + b x$ by choosing $a$ and $b$ to minimize the sum of squared residuals, where a **residual** is the measured $y$ minus the fitted value. $R^2$ is the fraction of the variation in $y$ that the line accounts for.

$$b = \frac{S_{xy}}{S_{xx}}, \qquad a = \bar{y} - b\,\bar{x}, \qquad R^2 = 1 - \frac{\text{SS}_{\text{res}}}{\text{SS}_{\text{tot}}}$$

$$S_{xx} = \sum (x_i - \bar{x})^2, \quad S_{xy} = \sum (x_i - \bar{x})(y_i - \bar{y}), \quad \text{SS}_{\text{res}} = \sum (y_i - a - b x_i)^2, \quad \text{SS}_{\text{tot}} = \sum (y_i - \bar{y})^2$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $x_i$, $y_i$ | paired observations (dimensionless in the example) | dimensionless |
| $a$ | intercept, the fitted $y$ at $x = 0$ | dimensionless |
| $b$ | slope | dimensionless |
| $\bar{x}$, $\bar{y}$ | means of $x$ and $y$ | dimensionless |
| $S_{xx}$, $S_{xy}$ | sums of squares and cross-products about the means | dimensionless |
| $\text{SS}_{\text{res}}$, $\text{SS}_{\text{tot}}$ | residual and total sums of squares | dimensionless |
| $R^2$ | coefficient of determination | dimensionless |

Holds when: the relation is linear in $a$ and $b$, the $x$ values are known far better than the $y$ values, and the scatter in $y$ has constant spread and is independent between points.
Breaks when: the true relation is curved, the scatter grows with $x$ (use weights), $x$ also has noise (the slope is biased toward zero), or a few points have large leverage. A high $R^2$ does not prove the model is right, and a low $R^2$ with a clear slope can still be useful. Never extrapolate far outside the fitted $x$ range.
Source and basis: derived from setting the derivatives of $\text{SS}_{\text{res}}$ with respect to $a$ and $b$ to zero (the normal equations); taught in [Probability and statistics](07-probability-and-statistics.md). The matrix form $\mathbf{A}^{\mathsf{T}}\mathbf{A}\,\mathbf{c} = \mathbf{A}^{\mathsf{T}}\mathbf{y}$ and its stable solution by orthogonal factorization are in the linear algebra and differential equations reference [math/reference-linear-algebra-differential-equations.md](reference-linear-algebra-differential-equations.md).

Residual checks, run before trusting the fit:

- Plot residuals against $x$ and against fitted value. A curve means the model form is wrong; a funnel means the spread is not constant.
- The residuals should average to zero and show no runs of the same sign.
- Look for one point that moves the line when removed.
- Check that residual scale is comparable to the known measurement noise. A fit much better than the noise allows is overfitting.

Example. Fit $x = 1, \dots, 5$ to $y = 2.1, 3.9, 6.2, 7.8, 10.1$. Then $\bar{x} = 3$, $\bar{y} = 6.02$, $S_{xx} = 10$, $S_{xy} = 19.9$, so $b = 1.99$ and $a = 0.05$. The residual sum of squares is $0.107$ against a total of $39.708$, so $R^2 = 0.9973$.

```verify
y1 = q(2.1, "")
y2 = q(3.9, "")
y3 = q(6.2, "")
y4 = q(7.8, "")
y5 = q(10.1, "")
ybar = (y1 + y2 + y3 + y4 + y5) / 5
expect(ybar, "6.02")
sxy = -2 * (y1 - ybar) - (y2 - ybar) + (y4 - ybar) + 2 * (y5 - ybar)
expect(sxy, "19.9")
sxx = q(10, "")
b = sxy / sxx
a = ybar - b * 3
expect(b, "1.99")
expect(a, "0.05")
ssres = (y1 - a - b)**2 + (y2 - a - 2 * b)**2 + (y3 - a - 3 * b)**2 + (y4 - a - 4 * b)**2 + (y5 - a - 5 * b)**2
sstot = (y1 - ybar)**2 + (y2 - ybar)**2 + (y3 - ybar)**2 + (y4 - ybar)**2 + (y5 - ybar)**2
expect(ssres, "0.107")
expect(sstot, "39.708")
expect(1 - ssres / sstot, "0.9973")
```

## Roots and nonlinear systems

A **root** of $f$ is a value $r$ with $f(r) = 0$. Root finders generate a sequence of guesses. Its **order of convergence** $p$ is the exponent in $e_{n+1} \approx C\,e_n^{\,p}$, where $e_n$ is the error after $n$ steps.

$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)} \qquad \text{(Newton)}$$

$$x_{n+1} = x_n - f(x_n)\,\frac{x_n - x_{n-1}}{f(x_n) - f(x_{n-1})} \qquad \text{(secant)}$$

$$|x_n - r| \le \frac{b - a}{2^{\,n}} \qquad \text{(bisection, } n \text{ halvings of } [a, b])$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $f$ | function whose root is sought | dimensionless |
| $x_n$ | the $n$-th guess | dimensionless |
| $f'$ | derivative of $f$ | dimensionless |
| $r$ | the root | dimensionless |
| $a$, $b$ | ends of the bracket, with $f(a)$ and $f(b)$ of opposite sign | dimensionless |
| $n$ | iteration count | dimensionless |

Holds when: for bisection, $f$ is continuous and the bracket changes sign. For Newton, $f$ is smooth, $f'(r) \ne 0$, and the start is close enough to $r$. For secant, the same smoothness without needing $f'$.
Breaks when: Newton starts near a zero of $f'$ (the step flies away), cycles, or meets a repeated root (then the order drops to 1). Secant can divide by a near-zero difference. Bisection cannot find a root where $f$ touches zero without changing sign.
Source and basis: derived from the tangent line (Newton), the secant line, and interval halving; taught in [Numerical methods](08-numerical-methods.md).

| Method | Order $p$ | Cost per step | Needs |
|---|---|---|---|
| Bisection | 1 (error halves each step) | 1 evaluation of $f$ | a sign-change bracket |
| Secant | $(1 + \sqrt{5})/2 = 1.618$ | 1 evaluation of $f$ | two starting points |
| Newton | 2 (correct digits roughly double) | $f$ and $f'$ | a derivative and a good start |

A robust code brackets first, then switches to a fast method inside the bracket and falls back to bisection when a step leaves it. Stop on both a small step and a small residual $|f(x)|$; either alone can mislead.

Example. For $f(x) = x^2 - 2$ from $x_0 = 1$, Newton gives $x_1 = 1.5$, $x_2 = 1.416667$, $x_3 = 1.414216$, against $\sqrt{2} = 1.414214$. The correct digits go roughly 0, 1, 3, 6, the signature of order 2. Bisection on $[1, 2]$ needs $n \ge \log_2(1000000) = 19.93$, so 20 halvings, to bring the bracket below one millionth of its start.

```verify
x0 = q(1, "")
x1 = x0 - (x0**2 - 2) / (2 * x0)
x2 = x1 - (x1**2 - 2) / (2 * x1)
x3 = x2 - (x2**2 - 2) / (2 * x2)
expect(x1, "1.5")
expect(x2, "1.416667")
expect(x3, "1.414216")
expect(sqrt(q(2, "")), "1.414214")
expect(log(q(1000000, "")) / log(q(2, "")), "19.93")
given("20")
expect((1 + sqrt(q(5, ""))) / 2, "1.618")
```

Newton for a system $\mathbf{F}(\mathbf{x}) = \mathbf{0}$ solves $\mathbf{J}\,\Delta\mathbf{x} = -\mathbf{F}$ at each step and updates $\mathbf{x} \leftarrow \mathbf{x} + \Delta\mathbf{x}$, where $\mathbf{J}$ is the matrix of partial derivatives. The linear solve is the cost; factorizations are in the linear algebra and differential equations reference [math/reference-linear-algebra-differential-equations.md](reference-linear-algebra-differential-equations.md). Use a line search or damping when the start is far from the solution.

## Interpolation

**Interpolation** builds a function that passes exactly through given data points, to estimate values between them.

$$P(x) = \sum_{k=0}^{n} y_k\,L_k(x), \qquad L_k(x) = \prod_{j \ne k}\frac{x - x_j}{x_k - x_j}$$

$$|f(x) - P_1(x)| \le \frac{h^2}{8}\,\max|f''|$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $P(x)$ | interpolating polynomial through $n + 1$ points | dimensionless |
| $x_k$, $y_k$ | data points ($y_k = f(x_k)$) | dimensionless |
| $L_k(x)$ | Lagrange basis polynomial, 1 at $x_k$ and 0 at the other nodes | dimensionless |
| $P_1$ | piecewise linear interpolant | dimensionless |
| $h$ | spacing between the two nodes bracketing $x$ | dimensionless |
| $f''$ | second derivative of the underlying function | dimensionless |

Holds when: the data are exact (or noise is negligible) and the underlying function is smooth between nodes. The error bound for $P_1$ needs a bounded second derivative.
Breaks when: data are noisy (interpolation reproduces the noise; fit a model instead), the function has a kink or jump between nodes, or a single high-degree polynomial is used on equally spaced nodes (Runge phenomenon below). Do not extrapolate with a polynomial.
Source and basis: derived from the uniqueness of the polynomial of degree $n$ through $n + 1$ points and the remainder term of polynomial interpolation; taught in [Numerical methods](08-numerical-methods.md).

- Linear interpolation is order 2 in the spacing $h$.
- A **cubic spline** joins cubic pieces with continuous value, slope, and curvature at every node. It needs two extra end conditions (natural: zero curvature at the ends; clamped: given end slopes; not-a-knot: a continuous third derivative at the second and second-last nodes), and it oscillates much less than one high-degree polynomial. Its error is order 4 in $h$ for smooth data only when the end conditions match the function (clamped with the true slopes, or not-a-knot). A natural spline drops to order 2 near the ends when the true $f''$ is not zero there.
- **Runge phenomenon**: interpolating $1/(1 + 25x^2)$ on $[-1, 1]$ with a single polynomial through equally spaced nodes gives errors that grow near the ends as the degree rises. The fix is lower degree on short pieces (a spline), or Chebyshev nodes $x_k = \cos\!\left(\frac{(2k+1)\pi}{2n+2}\right)$, which crowd toward the ends.

Example. Interpolate $\sin x$ linearly between $x = 0.4$ and $x = 0.5$ at $x = 0.45$. The interpolant is $(\sin 0.4 + \sin 0.5)/2 = 0.434422$ against the exact $0.434966$. The error is $5.44 \times 10^{-4}$, inside the bound $0.1^2 \sin(0.5)/8 = 6.0 \times 10^{-4}$.

```verify
x = q(0.45, "")
lin = (sin(q(0.4, "")) + sin(q(0.5, ""))) / 2
expect(lin, "0.434422")
expect(sin(x), "0.434966")
err = sin(x) - lin
expect(err * 10000, "5.44")
bound = q(0.1, "")**2 * sin(q(0.5, "")) / 8
expect(bound * 10000, "6.0")
check(err < bound, "error inside bound")
```

## Numerical differentiation and integration

A **finite difference** replaces a derivative by a difference of function values a step $h$ apart. **Quadrature** replaces an integral by a weighted sum of function values.

$$f'(x) \approx \frac{f(x+h) - f(x)}{h}, \qquad f'(x) \approx \frac{f(x+h) - f(x-h)}{2h}$$

$$\int_a^b f\,dx \approx \frac{h}{3}\left[f_0 + 4f_1 + 2f_2 + 4f_3 + \dots + 4f_{n-1} + f_n\right]$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $f$ | function sampled at the nodes | dimensionless |
| $h$ | spacing between equally spaced nodes | dimensionless |
| $f_i$ | $f$ at node $x_i = a + i h$ | dimensionless |
| $n$ | number of intervals, even for Simpson's rule | dimensionless |
| $a$, $b$ | limits of integration | dimensionless |

Holds when: $f$ has the several continuous derivatives that the error terms assume, and $h$ is small enough that truncation error dominates round-off.
Breaks when: $f$ has a jump, kink, or singularity inside the range (the stated orders are lost; split the range at the feature), the data are noisy (differencing amplifies noise by roughly $1/h$), or $h$ is so small that subtraction cancels digits.
Source and basis: derived from Taylor expansion of $f$ about the node, with the error terms from the first neglected term; taught in [Numerical methods](08-numerical-methods.md) and [Software solvers](09-software-solvers.md).

Error orders (leading term, smooth $f$). Every error in the table is approximation minus exact, with the derivative taken at some point $\xi$ in the range.

| Formula | Order in $h$ | Leading error (approximation minus exact) |
|---|---|---|
| Forward difference | 1 | $+\tfrac{h}{2} f''$ |
| Backward difference | 1 | $-\tfrac{h}{2} f''$ |
| Central difference | 2 | $+\tfrac{h^2}{6} f'''$ |
| Composite trapezoid | 2 | $+\tfrac{(b-a)h^2}{12} f''(\xi)$ |
| Composite Simpson | 4 | $+\tfrac{(b-a)h^4}{180} f^{(4)}(\xi)$ |
| $m$-point Gauss-Legendre | exact for polynomials up to degree $2m - 1$ | depends on $f^{(2m)}$ |

- Trapezoid and Simpson use equally spaced nodes and work on tabulated data. Gauss-Legendre picks the nodes and weights to get the highest polynomial degree for a given count of evaluations, so it suits functions you can evaluate anywhere.
- Two-point Gauss-Legendre on $[-1, 1]$ uses nodes $\pm 1/\sqrt{3}$ and weights 1 each. It integrates cubics exactly.
- Round-off and truncation trade off. For a central difference the best $h$ is roughly the cube root of machine epsilon times the scale of $x$, near $10^{-5}$ for double precision. For a forward difference it is the square root, near $10^{-8}$.
- Richardson extrapolation and grid-convergence indices that use these orders are owned by the simulation verification and validation reference [simulation/reference-verification-validation.md](../simulation/reference-verification-validation.md).

Example. For $f = e^x$ at $x = 1$ with $h = 0.1$, the central difference is $2.72281$ against the exact $2.71828$, an error of $0.00453$, and the predicted leading error $h^2 e/6$ is $0.00453$. The forward difference gives $2.85884$, an error of $0.1406$, about 31 times larger. Integrating $\sin x$ over $[0, \pi]$ (exact value 2) with 4 intervals, $h = \pi/4$, Simpson gives $2.00456$ and the trapezoid rule gives $1.89612$. The signs match the table, since $f'' = -\sin x \le 0$ makes the trapezoid low and $f^{(4)} = \sin x \ge 0$ makes Simpson high. Two-point Gauss gives $1.93582$ with 2 evaluations.

```verify
h = q(0.1, "")
x = q(1, "")
fd = (exp(x + h) - exp(x)) / h
cd = (exp(x + h) - exp(x - h)) / (2 * h)
expect(cd, "2.72281")
expect(exp(x), "2.71828")
expect(cd - exp(x), "0.00453")
expect(h**2 * exp(x) / 6, "0.00453")
expect(fd, "2.85884")
expect(fd - exp(x), "0.1406")
expect((fd - exp(x)) / (cd - exp(x)), "31")
hh = pi / 4
simp = hh / 3 * (4 * sin(hh) + 2 * sin(2 * hh) + 4 * sin(3 * hh))
trap = hh * (sin(hh) + sin(2 * hh) + sin(3 * hh))
expect(simp, "2.00456")
expect(trap, "1.89612")
check(trap - 2 < 0, "trapezoid low when f'' <= 0")
check(simp - 2 > 0, "Simpson high when f'''' >= 0")
gauss = pi * sin(pi / 2 * (1 - 1 / sqrt(q(3, ""))))
expect(gauss, "1.93582")
```

## Initial-value solvers

An **initial-value problem** is $y' = f(t, y)$ with $y(0)$ given. A solver advances from $t_n$ to $t_n + h$ in steps. A method has **global error order** $p$ when the error at a fixed end time scales as $h^p$.

$$y_{n+1} = y_n + h\,f(t_n, y_n) \qquad \text{(Euler)}$$

$$y_{n+1} = y_n + \frac{h}{6}\left(k_1 + 2k_2 + 2k_3 + k_4\right)$$

$$k_1 = f(t_n, y_n),\quad k_2 = f\!\left(t_n + \tfrac{h}{2},\, y_n + \tfrac{h}{2}k_1\right),\quad k_3 = f\!\left(t_n + \tfrac{h}{2},\, y_n + \tfrac{h}{2}k_2\right),\quad k_4 = f(t_n + h,\, y_n + h\,k_3)$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $t_n$ | time at step $n$ | s |
| $h$ | step size | s |
| $y_n$ | numerical solution at $t_n$ (dimensionless in the example) | dimensionless |
| $f(t, y)$ | right-hand side, the rate of change of $y$ | 1/s |
| $k_1, \dots, k_4$ | slope estimates within one step | 1/s |

Holds when: $f$ is smooth, and $h$ is small compared with the fastest time scale in the solution (stable range below).
Breaks when: the problem is stiff, so the step is limited by stability rather than accuracy; the solution has discontinuities (events, switching, impact) inside a step; or $f$ is not smooth. Restart the solver at a discontinuity.
Source and basis: derived from matching the Taylor series of the exact step to order $p$ (Euler is order 1, RK4 is order 4 with four evaluations of $f$ per step); taught in [Numerical methods](08-numerical-methods.md) and [Software solvers](09-software-solvers.md).

**Stability** is whether errors decay or grow from step to step. For the test problem $y' = -\lambda y$ with $\lambda > 0$ ($\text{s}^{-1}$), explicit Euler stays bounded only when $h\lambda < 2$, and RK4 only when $h\lambda < 2.785$. A problem is **stiff** when it has a fast decaying component, large $\lambda$, that dies out quickly but still limits $h$ of an explicit method for the whole run. Implicit methods, such as backward Euler $y_{n+1} = y_n/(1 + h\lambda)$, remain stable for any $h$ on this problem and are chosen for stiff systems.

Step-size practice:

- Pick $h$ for accuracy from the order and a refinement test, and confirm that $h\lambda$ is inside the stability limit for the fastest mode.
- Adaptive solvers estimate local error from two methods of different order and adjust $h$ to meet a tolerance. A tolerance sets local error, not global error; check the answer by tightening the tolerance.
- Energy-conserving systems (orbits, oscillators) drift under non-symplectic methods over long runs even at small $h$. Check the invariant.

Example. For $y' = -y$, $y(0) = 1$, $h = 0.1$ s, one Euler step gives $0.9$ and one RK4 step gives the Taylor sum of the first five terms of $e^{-h}$, which is $0.904837$, matching $e^{-0.1} = 0.904837$. With $\lambda = 1000$ $\text{s}^{-1}$ and $h = 0.01$ s, $h\lambda = 10$ is far past the Euler limit; each step multiplies $y$ by $1 - 10 = -9$ and the solution explodes, while backward Euler multiplies by $1/(1 + h\lambda) = 0.0909$ and decays.

```verify
h = q(0.1, "s")
lam = q(1, "1/s")
expect(1 - h * lam, "0.9")
rk = 1 - h * lam + (h * lam)**2 / 2 - (h * lam)**3 / 6 + (h * lam)**4 / 24
expect(rk, "0.904837")
expect(exp(-h * lam), "0.904837")
lam2 = q(1000, "1/s")
h2 = q(0.01, "s")
expect(h2 * lam2, "10")
expect(1 - h2 * lam2, "-9")
expect(1 / (1 + h2 * lam2), "0.0909")
```

## Finite differences for boundary-value problems

A **boundary-value problem** fixes the solution at both ends of an interval, for example $-u'' = g(x)$ with $u(0) = u(L) = 0$. The finite-difference method puts nodes $x_i = i h$ on the interval, replaces $u''$ by a difference, and solves the resulting linear system for the node values.

$$u''(x_i) \approx \frac{u_{i-1} - 2u_i + u_{i+1}}{h^2}, \qquad \text{error} = \frac{h^2}{12}\,u^{(4)}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $u$ | unknown field (a deflection, temperature, or potential) | m |
| $u_i$ | value of $u$ at node $x_i$ | m |
| $h$ | node spacing, $L/N$ for $N$ intervals | m |
| $g$ | source term, with $-u'' = g$ | 1/m |
| $u^{(4)}$ | fourth derivative of $u$ | $1/\text{m}^{3}$ |

Holds when: $u$ is smooth with continuous fourth derivative, the grid is uniform, and the boundary conditions are imposed exactly at the end nodes.
Breaks when: the coefficients or source jump (use a finite-volume or element form that conserves flux), the solution has a boundary layer thinner than $h$, or the grid is stretched without using the variable-spacing formula. Derivative (Neumann) boundary conditions need a one-sided or ghost-node formula of matching order, or the global order falls.
Source and basis: derived from the Taylor expansions of $u_{i \pm 1}$ about $x_i$, which also give the error term; taught in [Numerical methods](08-numerical-methods.md) and [Software solvers](09-software-solvers.md).

The interior equations give a tridiagonal system, solved in a number of operations proportional to the node count (Thomas algorithm). The method is second order, so halving $h$ should cut the error by about 4; if it does not, there is a bug or a boundary condition of lower order. Two- and three-dimensional grids give banded or sparse systems; see the linear algebra and differential equations reference [math/reference-linear-algebra-differential-equations.md](reference-linear-algebra-differential-equations.md) for direct and iterative solvers.

Example. Solve $-u'' = 1$ on $[0, 1]$ m with $u(0) = u(1) = 0$ using $h = 0.25$ m. The unknowns $u_1, u_2, u_3$ satisfy $2u_1 - u_2 = h^2$, $-u_1 + 2u_2 - u_3 = h^2$, and $-u_2 + 2u_3 = h^2$. By symmetry $u_1 = u_3$, so $u_2 = 2u_1 - h^2$ and $-2u_1 + 2u_2 = h^2$ give $u_1 = 0.09375$ and $u_2 = 0.125$. The exact solution $u = x(1-x)/2$ gives $0.09375$ and $0.125$. The fourth derivative of this quadratic is zero, so the scheme is exact here.

```verify
h = q(0.25, "")
u1 = 3 * h**2 / 2
u2 = 2 * u1 - h**2
expect(u1, "0.09375")
expect(u2, "0.125")
check(abs(2 * u1 - u2 - h**2) < q(1e-12, ""), "first equation closes")
check(abs(-u1 + 2 * u2 - u1 - h**2) < q(1e-12, ""), "second equation closes")
expect(q(0.5, "") * (1 - q(0.5, "")) / 2, "0.125")
```

## Error, stability, conditioning, and convergence

**Round-off error** comes from storing numbers with finitely many bits. **Machine epsilon**, $\varepsilon_{\text{mach}}$, is the gap between 1 and the next larger representable number. The **condition number** of a problem measures how much a relative input error is amplified in the output, independent of the algorithm.

$$\varepsilon_{\text{mach}} = 2^{-52}, \qquad u = \tfrac{1}{2}\varepsilon_{\text{mach}} = 2^{-53}$$

$$\kappa_f(x) = \left|\frac{x\,f'(x)}{f(x)}\right|, \qquad \frac{\|\delta\mathbf{x}\|}{\|\mathbf{x}\|} \le \kappa(\mathbf{A})\,\frac{\|\delta\mathbf{b}\|}{\|\mathbf{b}\|}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\varepsilon_{\text{mach}}$ | machine epsilon of binary64 (IEEE double) arithmetic | dimensionless |
| $u$ | unit round-off, the largest relative error of one rounded operation | dimensionless |
| $\kappa_f(x)$ | relative condition number of evaluating $f$ at $x$ | dimensionless |
| $\kappa(\mathbf{A})$ | condition number of the matrix, in a stated norm | dimensionless |
| $\delta\mathbf{x}$, $\delta\mathbf{b}$ | error in the solution and in the right-hand side of $\mathbf{A}\mathbf{x} = \mathbf{b}$ | dimensionless |

Holds when: for $\varepsilon_{\text{mach}}$, the arithmetic is binary64 with a 52-bit stored fraction and round-to-nearest; for $\kappa$, the perturbations are small enough for a first-order bound.
Breaks when: single precision (24-bit significand, epsilon near $10^{-7}$) or an unusual arithmetic is in use; intermediate results overflow or underflow; or $f(x)$ or the matrix is so close to singular that the first-order bound is useless.
Source and basis: derived from the binary64 layout (an implicit leading 1 plus 52 stored fraction bits), where the spacing of numbers just above 1 is $2^{-52}$; the condition formulas follow from a first-order Taylor expansion and from $\mathbf{A}\,\delta\mathbf{x} = \delta\mathbf{b}$. Matrix conditioning in depth is in the linear algebra and differential equations reference [math/reference-linear-algebra-differential-equations.md](reference-linear-algebra-differential-equations.md).

- Double precision carries about 16 significant decimal digits ($53\log_{10}2 = 15.95$). A computed result cannot be more accurate than the conditioning allows: lose about $\log_{10}\kappa$ digits.
- **Cancellation**: subtracting nearly equal numbers leaves few correct digits. Rewrite the formula instead of using more precision, for example $\sqrt{x+1} - \sqrt{x} = 1/(\sqrt{x+1} + \sqrt{x})$.
- Do not compare floating-point numbers for equality. Test $|a - b|$ against a tolerance scaled to the size of $a$ and $b$.
- Add small numbers before large ones, or use compensated summation, when summing many terms of mixed size.
- **Convergence** of a numerical scheme means the error goes to zero as $h \to 0$. For linear problems, consistency (the scheme matches the equation as $h \to 0$) plus stability gives convergence (Lax equivalence).
- Observed order from three grids with ratio 2: $p \approx \log_2\!\left[(y_{h} - y_{h/2})/(y_{h/2} - y_{h/4})\right]$. Use it to check that the code reaches its stated order; the extrapolation and error-band method built on it is in the simulation verification and validation reference [simulation/reference-verification-validation.md](../simulation/reference-verification-validation.md).

Typical tolerances (a choice, not a law): a relative tolerance of $10^{-6}$ is a common engineering default; going below about $10^{-10}$ in double precision rarely helps unless the problem is very well conditioned.

Example. $\varepsilon_{\text{mach}} = 1/2^{52} = 2.220 \times 10^{-16}$. Evaluating $f(x) = x - 1$ at $x = 1.000001$ has $\kappa_f = x/(x - 1) = 1000001$, so a relative input error of $\varepsilon_{\text{mach}}$ can grow to $\kappa_f\,\varepsilon_{\text{mach}} = 2.220 \times 10^{-10}$ in the output. The cancellation costs about 6 decimal digits.

```verify
eps = 1 / q(2, "")**52
expect(eps * 10**16, "2.220")
x = q(1.000001, "")
kap = abs(x * 1 / (x - 1))
expect(kap, "1000001")
expect(kap * eps * 10**10, "2.220")
expect(53 * log10(q(2, "")), "15.95")
```

## Checklists

Before trusting a statistical result:

- State the population and how the sample was drawn. Are the observations independent?
- Plot the data. Look at the distribution, outliers, drift, and clusters before computing a summary.
- Report the estimate with its interval, and the sample size.
- Check the assumptions behind the test or the interval, such as near-normality and constant spread.
- Compare any effect with the tolerance or margin that matters, not only with zero.
- Count how many comparisons were made.

Before trusting a numerical result:

- Run a case with a known exact answer through the same code.
- Halve $h$ (or double the grid) and compare. Estimate the observed order and check it against the method's stated order.
- Check the residual of the original equation, not only the change between iterations.
- Check stability: compare $h$ with the fastest time scale, and confirm the answer does not change when the tolerance tightens.
- Check conditioning of the linear solves; confirm that inputs have as many correct digits as the output claims.
- Check conserved quantities and boundary conditions in the output.

## Sanity checks

- A probability outside 0 to 1, a negative variance, or a probability that fails to sum to 1 is an error.
- The standard error falls as $1/\sqrt{n}$: four times the data halves the interval width. Ten times the precision needs 100 times the data.
- A normal sample lies within $\pm 3\sigma$ of the mean about 997 times in 1000 (99.73 percent).
- A Poisson count with mean $\lambda$ has spread $\sqrt{\lambda}$.
- $R^2$ between 0 and 1 for a fit with an intercept; the residuals sum to zero.
- Newton near a simple root roughly squares the error each step. Bisection gains about 3 digits per 10 steps ($2^{10} \approx 1000$), or one digit per 3.3 steps.
- Halving $h$ should cut a second-order error by about 4 and a fourth-order error by about 16. A ratio near 2 for a method claimed to be second order points to a first-order boundary condition or a bug.
- The exact solution of a decaying system must not grow. If a numerical solution grows, check $h\lambda$ first.
- Double precision gives about 16 digits at best. A claimed result with 20 digits from double-precision code is wrong.

## Further reference

- OpenStax, *Introductory Statistics*, and OpenStax, *Introductory Business Statistics*: free textbooks on probability, intervals, tests, and regression, at openstax.org.
- MIT OpenCourseWare, 18.05 *Introduction to Probability and Statistics*, and 18.335J *Introduction to Numerical Methods*: free course notes and problem sets at ocw.mit.edu.
- NIST/SEMATECH e-Handbook of Statistical Methods: a free handbook of statistical practice, hosted by NIST.
- *Numerical Analysis*, Burden and Faires; *Numerical Recipes*, Press and others; *Numerical Linear Algebra*, Trefethen and Bau; *Applied Numerical Linear Algebra*, Demmel (print references, no link).
- IEEE Standard 754 for floating-point arithmetic (paid standard; cite by title).
- Related lessons: [Probability and statistics](07-probability-and-statistics.md), [Numerical methods](08-numerical-methods.md), [Software solvers](09-software-solvers.md), and the [Math reference](reference.md).
