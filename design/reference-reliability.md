# Reliability reference

**Type:** reference
**Verify:** strict

Lookup sheet for reliability, the probability that a part or system performs its function for a stated time under stated conditions, covering lifetime models, system structures, redundancy, availability, fault trees, and life tests, for an engineer who must predict or demonstrate how long something lasts.

## Principles

- Reliability is a probability tied to a mission time and a set of conditions. A reliability number with no time, load, or environment attached has no meaning.
- Every result here assumes a failure definition. Change what counts as a failure and every number changes.
- Series structures multiply reliabilities, so a system is weaker than its weakest part. Redundancy adds reliability only as far as the units fail independently.
- Independence is the assumption that most often fails. One power supply, one maintenance crew, one bad batch, or one design flaw ties units together and can dominate the system result.
- A constant hazard rate means the unit does not age: its chance of failing in the next hour is the same whether it is new or old. Real wear-out and infant mortality break that.
- Few failures means wide uncertainty. A point estimate from two or three failures is a guess; always report a confidence bound.
- A survivor-only sample lies. Units that have not failed yet carry information, and dropping them biases life estimates short.
- Reliability is designed in, then demonstrated. A test can show a requirement is met with stated confidence, but it cannot make a weak design strong.
- Failure data from one population, load, and environment transfers to another only with stated adjustments. Label the source of every rate.
- Models give relative ranking and sensitivity more reliably than absolute probabilities. Use them to find the dominant contributor, not to quote the fourth digit.

## Reliability, survival, density, and hazard

The **lifetime** $t$ of a non-repairable item is the time from start of operation to its first failure; it is a random variable. The **reliability function** $R(t)$ is the probability that the item survives beyond $t$. The **probability density** $f(t)$ and **cumulative distribution** $F(t)$ describe the failure time; the **hazard rate** $h(t)$ is the instantaneous failure rate of items that have survived to $t$. For general distributions see [Probability, statistics, and numerical methods reference](../math/reference-probability-numerical-methods.md).

### Definitions and relations

$$R(t) = 1 - F(t) = \int_t^{\infty} f(u)\,\mathrm{d}u \qquad h(t) = \frac{f(t)}{R(t)} \qquad R(t) = \exp\!\left(-\int_0^t h(u)\,\mathrm{d}u\right)$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $t$ | operating time | s |
| $u$ | dummy variable of integration (time) | s |
| $R(t)$ | reliability, probability of surviving beyond $t$ | dimensionless |
| $F(t)$ | probability of failing by time $t$ | dimensionless |
| $f(t)$ | probability density of the failure time | 1/s |
| $h(t)$ | hazard rate | 1/s |

Holds when: the item is non-repairable (or only the first failure is of interest), the failure time is continuous, and $t$ is measured on one consistent clock such as operating hours.
Breaks when: operating hours and calendar time differ (idle, standby, or duty-cycled units) and the clock is not stated, or when failure modes with different clocks are mixed. Repairable items need a point-process model, not a lifetime distribution.
Source and basis: derived from the definition of conditional probability; taught in [Probability and statistics](../math/07-probability-and-statistics.md).

Example: a unit has $f = 0.00015$ per hour and $R = 0.75$ at the time of interest, so $h = f/R$ is 0.0002 per hour.

```verify
f = q(0.00015, "1/h")
R = q(0.75, "")
expect(f / R, "0.0002 1/h")
```

### The bathtub curve

The **bathtub curve** is the hazard rate of a large population plotted against age. It is a concept for organizing causes, not a law that every product follows. Three regions of the bathtub curve are drawn: early life with a high but rapidly decreasing hazard (infant mortality, from defects and weak units), a long useful-life region with a roughly level hazard (random failures), and wear-out with a rising hazard (fatigue, corrosion, depletion) [src](../data/claims/reliability.md#bathtub-curve).

- Screening (burn-in, proof test) removes the early region before shipment.
- Preventive replacement before the wear-out region keeps a fleet in the level region.
- A part with no early or wear-out region on the time scale of its mission can be modelled as constant hazard.

## Exponential model

The **exponential distribution** has a constant hazard rate. It describes failures that arrive at random with no ageing, and it is the only lifetime distribution with no memory.

### Constant hazard, MTTF, and failures in time

$$h(t) = \lambda \qquad R(t) = e^{-\lambda t} \qquad \mathrm{MTTF} = \frac{1}{\lambda}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\lambda$ | constant failure rate | 1/s |
| $t$ | operating time | s |
| $R(t)$ | reliability | dimensionless |
| $\mathrm{MTTF}$ | mean time to failure | s |

Holds when: the hazard is constant over the mission, which means no ageing and no early defects.
Breaks when: any wear-out or infant mortality is present, because the model then overstates reliability early and understates late. Note that $R$ at $t = \mathrm{MTTF}$ is $e^{-1}$, so only about 37 percent of units survive to the mean life.
Source and basis: derived from $R(t) = \exp(-\int h\,\mathrm{d}t)$ with constant $h$; the mean is $\int_0^\infty R\,\mathrm{d}t$. See [Probability and statistics](../math/07-probability-and-statistics.md).

A **FIT** (failure in time) is one failure per $10^9$ device-hours, a convention used for electronic parts. A rate of $\lambda$ per hour equals $\lambda \times 10^9$ FIT.

Example: $\lambda = 2\times 10^{-5}$ per hour. Over $t = 5000$ h, $\lambda t = 0.1$ and $R = 0.9048$. The mean life is 50000 h. The rate is 20000 FIT.

```verify
lam = q(2e-5, "1/h")
t = q(5000, "h")
expect(exp(-lam * t), "0.9048")
expect(1 / lam, "50000 h")
given("1e9", "20000")
expect(lam * t, "0.1")
expect(lam * q(1e9, "h"), "20000")
```

## Weibull model

The **Weibull distribution** has a power-law hazard and is the standard model for mechanical life, since one shape parameter covers early failures, random failures, and wear-out. Its hazard is decreasing for $\beta < 1$, constant for $\beta = 1$ (the exponential case), and increasing for $\beta > 1$.

### Reliability, hazard, and B life

$$R(t) = \exp\!\left[-\left(\frac{t}{\eta_W}\right)^{\beta}\right] \qquad h(t) = \frac{\beta}{\eta_W}\left(\frac{t}{\eta_W}\right)^{\beta-1} \qquad t_{Bp} = \eta_W\left[-\ln(1-p)\right]^{1/\beta}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\beta$ | shape parameter | dimensionless |
| $\eta_W$ | scale parameter, the characteristic life | s |
| $t$ | operating time | s |
| $p$ | cumulative failure fraction defining the B life | dimensionless |
| $t_{Bp}$ | time by which a fraction $p$ has failed | s |

Holds when: the failure mechanism is a single one, there is no failure-free period, and $\beta$ is stable over the range used.
Breaks when: the plot of failures is curved (mixed failure modes or a minimum life, which needs a three-parameter form with a location shift), or when extrapolating far beyond the tested times.
Source and basis: derived from the cumulative hazard $(t/\eta_W)^\beta$; the exponential case is $\beta = 1$ with $\eta_W = 1/\lambda$.

- Shape $\beta < 1$: hazard decreases, early-life failures dominate.
- Shape $\beta = 1$: hazard is constant, equal to $1/\eta_W$.
- Shape $\beta > 1$: hazard increases, wear-out. Fatigue of metals commonly shows $\beta$ well above 1; a larger $\beta$ means a narrower spread of lives.
- At $t = \eta_W$ the reliability is $e^{-1}$ for every $\beta$, which is why $\eta_W$ is the **characteristic life**.
- **B10 life** is $t_{Bp}$ with $p = 0.10$: the time by which 10 percent of units have failed. It is the usual life rating for bearings.

Example: $\beta = 2$, $\eta_W = 1000$ h. At $t = 500$ h, $R = 0.7788$. The B10 life, with $p = 0.1$, is 324.6 h. The hazard at 500 h is 0.0010 per hour.

```verify
beta = q(2, "")
eta = q(1000, "h")
t = q(500, "h")
expect(exp(-(t / eta)**beta), "0.7788")
p = q(0.1, "")
expect(eta * (-log(1 - p))**(1 / beta), "324.6 h")
expect((beta / eta) * (t / eta)**(beta - 1), "0.0010 1/h")
```

## Lognormal model

The **lognormal distribution** applies when the logarithm of life is normally distributed, as in many fatigue-crack growth and degradation processes. Its hazard is neither constant nor monotonic: it rises from zero to a peak and then falls.

### Reliability from the standard normal

$$R(t) = 1 - \Phi\!\left(\frac{\ln t - \mu_{\ln}}{\sigma_{\ln}}\right) \qquad t_{50} = e^{\mu_{\ln}}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\Phi$ | standard normal cumulative distribution function | dimensionless |
| $t$ | operating time, expressed in one fixed unit inside the logarithm | s |
| $\mu_{\ln}$ | mean of $\ln t$ | dimensionless |
| $\sigma_{\ln}$ | standard deviation of $\ln t$ | dimensionless |
| $t_{50}$ | median life | s |

Holds when: life is the product of many small independent multiplicative effects, and $\mu_{\ln}$, $\sigma_{\ln}$ were fitted with $t$ in the same unit used in the formula.
Breaks when: the hazard is truly increasing without a late decline (use Weibull), or when the tail far below the median matters, since the two models differ most there and the data rarely discriminate between them.
Source and basis: derived from the definition of the lognormal distribution; see [Probability, statistics, and numerical methods reference](../math/reference-probability-numerical-methods.md).

Example: $t_{50} = 1000$ h and $\sigma_{\ln} = 0.5$. At $t = t_{50}\,e^{\sigma_{\ln}} = 1649$ h the argument of $\Phi$ is $1$ and $\Phi(1) = 0.8413$, so $R = 0.1587$.

```verify
t50 = q(1000, "h")
s = q(0.5, "")
expect(t50 * exp(s), "1649 h")
expect(log(exp(s)) / s, "1")
phi = q(0.8413, "")
expect(1 - phi, "0.1587")
```

## Parameter estimation and censoring

A life test rarely runs until every unit fails. **Right censoring** means a unit is known only to have survived to some time without failing, because the test stopped or the unit was removed for another reason. A censored unit is not a failure, but it is not discardable: dropping it biases the estimated life short.

### Median ranks and the Weibull plot

The median rank approximation for the failure fraction of the $i$-th ordered failure among $n$ units is $F_i \approx (i - 0.3)/(n + 0.4)$ [src](../data/claims/reliability.md#median-rank-approximation). Taking logarithms twice of the Weibull $F(t)$ gives a straight line:

$$F_i \approx \frac{i - 0.3}{n + 0.4} \qquad \ln\!\bigl[-\ln(1-F)\bigr] = \beta \ln t - \beta \ln \eta_W$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $F_i$ | estimated failure fraction at the $i$-th failure | dimensionless |
| $i$ | rank of the failure, 1 for the earliest | dimensionless |
| $n$ | number of units on test | dimensionless |
| $F$ | failure fraction on the plot | dimensionless |
| $t$ | failure time | s |
| $\beta$ | Weibull shape, the slope of the line | dimensionless |
| $\eta_W$ | Weibull scale, where the line crosses $F = 1 - e^{-1}$ | s |

Holds when: the units are identical in population, the failures are complete (no censored units) or the ranks are adjusted for them, and a single failure mode acts.
Breaks when: censored units are ranked as failures, when points curve (mixed modes), or when $n$ is very small, where the fitted slope has a wide confidence interval.
Source and basis: the rank formula is the empirical approximation $(i - 0.3)/(n + 0.4)$ in [src](../data/claims/reliability.md#median-rank-approximation); the line is derived by taking $\ln$ twice of $F = 1 - \exp[-(t/\eta_W)^\beta]$.

- With censoring, adjust the rank increments for the unit's position among the survivors; a hand plot is only a first look.
- For the exponential model with $r$ failures and total time on test $T_{\text{tot}}$ (failed units' times plus censored units' times), the maximum-likelihood rate is $\hat{\lambda} = r/T_{\text{tot}}$.

Example: $n = 5$ units, first failure at 300 h and third failure at 800 h. The ranks are $F_1 = 0.1296$ and $F_3 = 0.5000$. The line through those two points has slope $\beta = 1.64$ and crosses $\eta_W = 1000$ h.

```verify
n = q(5, "")
F1 = (1 - 0.3) / (n + 0.4)
F3 = (3 - 0.3) / (n + 0.4)
expect(F1, "0.1296")
expect(F3, "0.5000")
y1 = log(-log(1 - F1))
y3 = log(-log(1 - F3))
t1 = q(300, "h")
t3 = q(800, "h")
b = (y3 - y1) / log(t3 / t1)
expect(b, "1.64")
expect(t3 * exp(-y3 / b), "1000 h")
```

## Series systems

A **series system** fails when any one of its units fails, as with links in a chain.

### Series reliability

$$R_s = \prod_{i=1}^{n} R_i \qquad \lambda_s = \sum_{i=1}^{n} \lambda_i \;\text{(exponential units)}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $R_s$ | system reliability | dimensionless |
| $R_i$ | reliability of unit $i$ over the same mission | dimensionless |
| $n$ | number of units in series | dimensionless |
| $\lambda_s$ | system failure rate | 1/s |
| $\lambda_i$ | failure rate of unit $i$ | 1/s |

Holds when: units fail independently, and every unit must work for the system to work.
Breaks when: failures are dependent (shared load or environment), or when the system has any redundancy, graceful degradation, or a unit that is not needed. The sum of rates also needs every unit to be exponential.
Source and basis: derived from the product rule for independent events; taught in [Probability and statistics](../math/07-probability-and-statistics.md).

Example: three units with $R = 0.90$, $0.80$, and $0.95$ in series give $R_s = 0.684$, lower than the weakest unit.

```verify
R1 = q(0.9, "")
R2 = q(0.8, "")
R3 = q(0.95, "")
expect(R1 * R2 * R3, "0.684")
check(R1 * R2 * R3 < R2, "series system is weaker than its weakest unit")
```

## Parallel and k-out-of-n systems

A **parallel system** works if at least one unit works. A **k-out-of-n system** works if at least $k$ of its $n$ units work; parallel is the case $k = 1$ and series is $k = n$.

### Active redundancy

$$R_p = 1 - \prod_{i=1}^{n}(1 - R_i) \qquad R_{k/n} = \sum_{j=k}^{n}\binom{n}{j} R^{j}(1-R)^{n-j}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $R_p$ | reliability of the parallel system | dimensionless |
| $R_i$ | reliability of unit $i$ | dimensionless |
| $R_{k/n}$ | reliability of a k-out-of-n system of identical units | dimensionless |
| $R$ | reliability of one identical unit | dimensionless |
| $k$ | minimum number of working units | dimensionless |
| $n$ | total number of units | dimensionless |
| $j$ | count of working units in the sum | dimensionless |

Holds when: units fail independently, all units run (active redundancy), switching and voting are perfect, and the surviving units can carry the full load.
Breaks when: a failed unit shifts load onto the survivors, the voter or switch itself fails, or the units share a cause of failure. Then the formulas are optimistic.
Source and basis: derived from the binomial distribution for identical independent units and from the product rule for the parallel case; taught in [Probability and statistics](../math/07-probability-and-statistics.md).

Example: two units with $R = 0.9$ in parallel give $0.99$. A 2-out-of-3 system of the same units gives $R^3 + 3R^2(1-R) = 0.972$.

```verify
R = q(0.9, "")
expect(1 - (1 - R)**2, "0.990")
expect(R**3 + 3 * R**2 * (1 - R), "0.972")
```

## Standby redundancy

In **standby redundancy** a spare is switched in only when the active unit fails, so the spare does not age while waiting.

### Perfect switching, identical exponential units

$$R_{\text{sb}}(t) = e^{-\lambda t}\sum_{j=0}^{n-1}\frac{(\lambda t)^j}{j!} \qquad \mathrm{MTTF}_{\text{sb}} = \frac{n}{\lambda}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $R_{\text{sb}}$ | system reliability with $n$ units, one active at a time | dimensionless |
| $\lambda$ | failure rate of an active unit | 1/s |
| $t$ | mission time | s |
| $n$ | total number of units including spares | dimensionless |
| $j$ | index of the sum, the number of failures survived | dimensionless |
| $\mathrm{MTTF}_{\text{sb}}$ | mean time to failure of the standby system | s |

Holds when: the units are identical and exponential, spares cannot fail while idle, and the switch works every time with no delay.
Breaks when: spares degrade in storage (warm or hot standby), the switch has its own failure probability, or the units are not exponential. Include the switch reliability as a series factor.
Source and basis: derived from the Poisson distribution of the number of failures of an exponential unit that is replaced at once.

Example: two units with $\lambda = 2\times 10^{-5}$ per hour over $t = 5000$ h have $\lambda t = 0.1$ and $R_{\text{sb}} = 0.9953$, against 0.9048 for one unit. The mean life is 100000 h.

```verify
lam = q(2e-5, "1/h")
t = q(5000, "h")
x = lam * t
expect(x, "0.1")
expect(exp(-x), "0.9048")
expect(exp(-x) * (1 + x), "0.9953")
expect(2 / lam, "100000 h")
```

## Dependencies and common cause

A **common cause failure (CCF)** is the failure of several units from one shared cause, such as a manufacturing flaw, a maintenance error, or one power supply. It defeats redundancy because the units are not independent.

### Beta-factor model

In the beta factor model, $\beta$ represents the fraction of the failure rate that is common to multiple susceptible components [src](../data/claims/reliability.md#beta-factor-common-cause). Each unit has an independent part $(1 - \beta)\lambda$ and a common part $\beta\lambda$ that fails all units together. For two redundant units that each fail on demand with probability $Q$:

$$Q_s \approx \bigl[(1-\beta)Q\bigr]^2 + \beta Q$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $Q_s$ | probability that both units fail | dimensionless |
| $Q$ | failure probability of one unit | dimensionless |
| $\beta$ | beta factor, the fraction of failures that are common cause | dimensionless |

Holds when: the units are identical, and the independent and common parts add as rare events ($Q \ll 1$).
Breaks when: the system has three or more units and partial common-cause failures matter (use a model that distinguishes the number of units failed), or when $\beta$ is chosen with no data behind it. The result then looks like a calculation but is an assumption.
Source and basis: the beta factor model is cited at [src](../data/claims/reliability.md#beta-factor-common-cause); the two-unit expression is derived by splitting each unit's failure into an independent event and a shared event.

Example: $Q = 0.001$ per demand. Treating the units as independent gives $Q^2 = 1.000$ per million. With $\beta = 0.05$ the pair fails with probability 50.90 per million, about fifty times greater, and the common term $\beta Q$ dominates.

```verify
Q = q(0.001, "")
b = q(0.05, "")
expect(Q**2 * 1e6, "1.000")
Qs = ((1 - b) * Q)**2 + b * Q
expect(Qs * 1e6, "50.90")
check(b * Q > ((1 - b) * Q)**2, "common cause term dominates")
```

## Repairable systems and availability

A **repairable** system returns to service after a failure, so the question is how much of the time it works. **Availability** $A_{\text{av}}$ is the long-run fraction of time the system is up. $\mathrm{MTBF}$ is the mean operating time between failures (for a repairable item with exponential up times it equals $1/\lambda$), and $\mathrm{MTTR}$ is the mean time to repair.

### Inherent and steady-state availability

$$A_{\text{inh}} = \frac{\mathrm{MTBF}}{\mathrm{MTBF} + \mathrm{MTTR}} \qquad A_{\text{ss}} = \frac{\mathrm{MTBF}}{\mathrm{MTBF} + \mathrm{MDT}}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $A_{\text{inh}}$ | inherent availability, counting active repair time only | dimensionless |
| $A_{\text{ss}}$ | steady-state availability, counting all downtime | dimensionless |
| $\mathrm{MTBF}$ | mean operating time between failures | s |
| $\mathrm{MTTR}$ | mean active repair time | s |
| $\mathrm{MDT}$ | mean downtime per failure, including waiting for parts, staff, and access | s |

Holds when: the process is long-run and stationary, and failure and repair times are independent with fixed means.
Breaks when: the mission is short (use the time-dependent availability), preventive maintenance is scheduled downtime that the formulas leave out, or the system has several repair crews and states (use a Markov model). MTBF is a mean, not a promised life: a 50000 h MTBF does not mean a unit lasts 50000 h.
Source and basis: derived from the ratio of mean up time to mean cycle time in a renewal process; see [Probability, statistics, and numerical methods reference](../math/reference-probability-numerical-methods.md).

Example: $\mathrm{MTBF} = 2000$ h, $\mathrm{MTTR} = 8$ h. Then $A_{\text{inh}} = 0.9960$. If waiting for parts and access adds up to a mean downtime of 24 h, $A_{\text{ss}} = 0.9881$.

```verify
MTBF = q(2000, "h")
MTTR = q(8, "h")
MDT = q(24, "h")
expect(MTBF / (MTBF + MTTR), "0.9960")
expect(MTBF / (MTBF + MDT), "0.9881")
```

## Fault trees and event trees

A **fault tree** works backward from one undesired top event through AND and OR gates to basic events. An AND gate occurs only if all inputs occur; an OR gate occurs if any input occurs. A **cut set** is a set of basic events that together cause the top event, and a **minimal cut set** is a cut set that fails if any one event is removed from it; a minimal cut set with one event is a single-point failure. The procedure for building a tree is in [problem-solving reference](../problem-solving/reference.md#root-cause-tools).

An **event tree** works forward from an initiating event through the success or failure of each safety function and gives the frequency of each outcome as the initiator frequency times the branch probabilities along the path.

### Gate and cut-set probabilities

$$P_{\text{AND}} = \prod_i p_i \qquad P_{\text{OR}} = 1 - \prod_i (1 - p_i) \qquad P_{\text{top}} \approx \sum_k P(C_k)$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $p_i$ | probability of basic event $i$ | dimensionless |
| $P_{\text{AND}}$ | probability of an AND gate output | dimensionless |
| $P_{\text{OR}}$ | probability of an OR gate output | dimensionless |
| $P_{\text{top}}$ | probability of the top event | dimensionless |
| $P(C_k)$ | probability of minimal cut set $k$, the product of its event probabilities | dimensionless |

Holds when: basic events are independent. The sum over minimal cut sets is the rare-event approximation, typically accurate for event probabilities below 0.1 [src](../data/claims/reliability.md#rare-event-approximation).
Breaks when: events are dependent (shared causes make AND gates far too optimistic), probabilities are not small (the sum then overestimates, although it errs on the conservative side), or the events are time-ordered, where a static tree misses the order.
Source and basis: gate formulas are derived from the product and complement rules; the rare-event sum is cited. See also [Probability and statistics](../math/07-probability-and-statistics.md).

Example: cut sets $\{A, B\}$ and $\{C\}$ with $p_A = 0.01$, $p_B = 0.02$, $p_C = 0.001$. The exact top probability is $1 - (1 - p_A p_B)(1 - p_C) = 0.00120$, and the rare-event sum is $0.00120$. The single-point failure $C$ contributes most of it.

```verify
pA = q(0.01, "")
pB = q(0.02, "")
pC = q(0.001, "")
exact = 1 - (1 - pA * pB) * (1 - pC)
expect(exact, "0.00120")
expect(pA * pB + pC, "0.00120")
check(pC > pA * pB, "single failure dominates the cut set pair")
```

## Reliability demonstration tests

A **demonstration test** shows with stated confidence that a reliability requirement is met. Confidence $C$ is the probability, over repeated tests, that the claim is true when the test is passed.

### Zero-failure success-run test

$$R^{n} = 1 - C \quad\Longrightarrow\quad n = \frac{\ln(1 - C)}{\ln R}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $R$ | reliability to be demonstrated over the test mission | dimensionless |
| $C$ | confidence level | dimensionless |
| $n$ | number of units that must all survive the mission | dimensionless |

Holds when: the units are identical samples of the production population, each is tested for the full mission, and a single failure fails the test.
Breaks when: the test conditions are milder than service (the result does not carry over), or when failures are allowed, which needs a binomial bound with a larger sample. Round $n$ up.
Source and basis: derived from the binomial probability that all $n$ units survive, which is $R^n$, set equal to $1 - C$.

Example: to demonstrate $R = 0.95$ with $C = 0.9$ confidence, $n = \ln(1-C) / \ln R = 44.89$, so 45 units must pass with no failure.

```verify
R = q(0.95, "")
C = q(0.9, "")
expect(log(1 - C) / log(R), "44.89")
given("45")
```

### Exponential test with the chi-square bound

For a test of exponential units with $r$ failures and total time on test $T_{\text{tot}}$, the lower one-sided confidence bound on the mean life is, for a time-terminated test,

$$\mathrm{MTBF}_{\text{L}} = \frac{2\,T_{\text{tot}}}{\chi^2_{C,\,2r+2}}$$

For a failure-terminated test replace the degrees of freedom $2r+2$ by $2r$.

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\mathrm{MTBF}_{\text{L}}$ | lower confidence bound on the mean life | s |
| $T_{\text{tot}}$ | total time on test of all units, failed and surviving | s |
| $r$ | number of failures | dimensionless |
| $C$ | one-sided confidence level | dimensionless |
| $\chi^2_{p,\nu}$ | chi-square quantile with cumulative probability $p$ and $\nu$ degrees of freedom | dimensionless |

Holds when: the units are exponential (constant hazard), test conditions equal service conditions, and all units run the same clock.
Breaks when: the hazard is not constant (an increasing hazard makes the bound optimistic for early times), or when the test stopped for a reason related to the results. Read the quantile from a table or a numerical routine; do not interpolate by eye.
Source and basis: derived from the fact that $2\lambda T_{\text{tot}}$ follows a chi-square distribution when the units are exponential; see [Probability, statistics, and numerical methods reference](../math/reference-probability-numerical-methods.md).

Example: $r = 2$ failures in $T_{\text{tot}} = 10000$ h, time-terminated, $C = 0.9$. With 6 degrees of freedom the quantile is $\chi^2_{0.9,6} = 10.645$, so $\mathrm{MTBF}_{\text{L}} = 1879$ h. With zero failures the quantile for 2 degrees of freedom is $4.605$, and the bound is 4343 h.

```verify
T = q(10000, "h")
C = q(0.9, "")
given("10.645", "4.605")
expect(2 * T / 10.645, "1879 h")
expect(2 * T / 4.605, "4343 h")
```

## Confidence bounds

A point estimate of a life is a single value from one sample; a **confidence interval** states the range that a repeated procedure would capture the true value in a stated fraction of tests. Bounds are wide when failures are few.

### Two-sided bound on exponential mean life

$$\frac{2\,T_{\text{tot}}}{\chi^2_{1-\alpha/2,\,2r}} \;\le\; \mathrm{MTBF} \;\le\; \frac{2\,T_{\text{tot}}}{\chi^2_{\alpha/2,\,2r}}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\alpha$ | total probability outside the interval | dimensionless |
| $T_{\text{tot}}$ | total time on test | s |
| $r$ | number of failures, failure-terminated test | dimensionless |
| $\mathrm{MTBF}$ | true mean life | s |
| $\chi^2_{p,\nu}$ | chi-square quantile with cumulative probability $p$ and $\nu$ degrees of freedom | dimensionless |

Holds when: units are exponential and the test is stopped at the $r$-th failure.
Breaks when: the test is stopped at a fixed time (use $2r+2$ degrees of freedom in the lower bound and $2r$ in the upper), when $r = 0$ (only a lower bound exists), or when the hazard is not constant.
Source and basis: derived from the chi-square distribution of $2\lambda T_{\text{tot}}$, as in the previous entry.

Example: $r = 2$ failures at $T_{\text{tot}} = 10000$ h, $\alpha = 0.10$. With $\chi^2_{0.95,4} = 9.488$ and $\chi^2_{0.05,4} = 0.7107$, the 90 percent interval is 2108 h to 28141 h, a spread by a factor of more than thirteen.

```verify
T = q(10000, "h")
given("9.488", "0.7107", "0.10", "90")
lo = 2 * T / 9.488
hi = 2 * T / 0.7107
expect(lo, "2108 h")
expect(hi, "28141 h")
check(hi / lo > 13, "interval spans more than a factor of thirteen")
```

For Weibull and lognormal fits, bounds come from the fitted parameters' covariance or from likelihood ratios; use a statistics routine and report the interval, not the point value alone.

## FMEA and FMECA boundary

**Failure modes and effects analysis (FMEA)** lists each failure mode of each function, its effect, its cause, and the controls that exist. **FMECA** adds a criticality ranking. The procedure and the rating scales are in [problem-solving reference](../problem-solving/reference.md#root-cause-tools); this sheet covers only what the number is.

### The risk priority number

$$\mathrm{RPN} = S \times O \times D$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $S$ | severity rating of the effect | dimensionless |
| $O$ | occurrence rating of the cause | dimensionless |
| $D$ | detection rating, higher when the failure is harder to catch | dimensionless |
| $\mathrm{RPN}$ | risk priority number | dimensionless |

Holds when: the three ratings use scales defined before the analysis and the same scales are used on every row.
Breaks when: the RPN is used alone to rank risk. The ratings are ordinal labels, not measurements, so their product has no physical unit and ranks arbitrarily. Different combinations give the same product: severity 9 with occurrence and detection 1 gives the same RPN as severity 3 with occurrence 3 and detection 1, although a failure that harms people is not equal to a nuisance. Act on high severity regardless of RPN, and rank by criticality (severity with occurrence) as a second view.
Source and basis: the RPN is a defined convention in [problem-solving reference](../problem-solving/reference.md#root-cause-tools); the weakness is derived from the arithmetic of multiplying ordinal scales.

Example: severity 7, occurrence 4, detection 5 gives RPN 140. Severity 9 with occurrence and detection 1 gives 9, far below, although the severe effect may deserve action first.

```verify
S = q(7, "")
O = q(4, "")
D = q(5, "")
expect(S * O * D, "140")
expect(9 * 1 * 1, "9")
expect(3 * 3 * 1, "9")
```

## Checklists

Before trusting a reliability result:

- State the failure definition, mission time, load, and environment the number applies to.
- Name the model of each unit (exponential, Weibull, lognormal, or a stated probability on demand) and whether the hazard is constant, increasing, or decreasing.
- Check that the data and model share one clock: operating hours, cycles, or calendar time.
- Treat censored units as censored, not as failures and not as discarded.
- Report a confidence bound, and the number of failures behind it.
- Check each independence assumption against shared power, software, maintenance, environment, and manufacturing lot; add common cause where it applies.
- Check that the system diagram matches the real function: which units must work, and what carries the load after a failure.
- Include switches, voters, sensors, and software as units in the structure.
- Find the dominant contributor (the highest cut set or the weakest series unit) before spending effort elsewhere.

## Sanity checks

- A series system is never more reliable than its least reliable unit. A parallel system is never less reliable than its most reliable unit.
- An exponential unit run for exactly one mean life survives with $R = e^{-1} = 0.368$, not 0.5.
- A Weibull unit run for exactly its characteristic life survives with $R = e^{-1}$ whatever its shape.
- Availability is below one and rises as MTTR falls; an MTTR longer than the MTBF gives availability below 0.5.
- A 2-out-of-3 system of identical units beats a single unit only when each unit has reliability above 0.5.
- A common-cause term of $\beta Q$ in a redundant pair caps its failure probability at about $\beta$ times the single-unit value; redundancy cannot beat that.
- An interval for a mean life from two failures spans an order of magnitude. If a report quotes tight bounds from a few failures, look for the assumption doing the work.
- Zero failures in $n$ trials at confidence $C$ proves only $R \ge (1 - C)^{1/n}$; it never proves perfect reliability.

## Further reference

Named books and standards only for the paid ones. Check current editions before relying on a value.

- NIST/SEMATECH e-Handbook of Statistical Methods, Chapter 8, Assessing Product Reliability (free, [NIST](https://www.itl.nist.gov/div898/handbook/)).
- Fault Tree Handbook with Aerospace Applications, NASA Office of Safety and Mission Assurance, version 1.1 (free, search the title on the NASA site).
- Fault Tree Handbook, NUREG-0492, U.S. Nuclear Regulatory Commission (free, search the title on the NRC site).
- Reliability Engineering, Kececioglu (paid).
- Statistical Methods for Reliability Data, Meeker and Escobar (paid, censored data and confidence bounds).
- Practical Reliability Engineering, O'Connor and Kleyner (paid, systems and testing).
- MIL-HDBK-217 and IEC 61709 for electronic part failure rates (standards, paid or restricted; check scope and age).
- IEC 60812, Failure modes and effects analysis (standard, paid).
- Related sheets: [Factor of safety and failure](07-factor-of-safety-and-failure.md), [Philosophy reference](../philosophy/reference.md).
