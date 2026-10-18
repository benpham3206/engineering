# Feedback control

A control system measures an output, compares it with a desired value, and changes an input to close the gap. Engineers use feedback to hold a temperature, keep a drone level, or position a robot arm, even when the plant changes or a disturbance pushes on it.

**Prerequisites:** [13-vibrations.md](13-vibrations.md), [02-particle-dynamics.md](02-particle-dynamics.md)
**Time:** 8-12 h

## Core ideas

- The **plant** is the system being controlled. Its input is $u(t)$ and its output is $y(t)$.
- The **reference** $r(t)$ is the value you want the output to follow. The **error** is $e(t) = r(t) - y(t)$.
- A **controller** turns the error into the plant input. A **proportional (P) controller** sets $u = K_p e$, where $K_p$ is the gain.
- **Unity feedback** means the measured output is fed straight back and subtracted from the reference, with no filter in the loop.
- A **transfer function** $G(s)$ describes a linear system in the Laplace variable $s$. It is the ratio of output to input when all starting conditions are zero. You can read the time response, and the stability, from the poles of $G(s)$.
- A **step response** is the output when the reference jumps from 0 to 1 at $t = 0$. It is the standard test for speed, overshoot and final error.
- **Steady-state error** $e_{ss}$ is the error left after the transient has died out. A P controller often leaves a steady error. An integral term removes it.
- A **PID controller** adds three actions: proportional (now), integral (the past sum of error), and derivative (the rate of change of error). Its standard form is

$$u(t) = K_p e(t) + K_i \int_0^t e(\tau)\,d\tau + K_d \frac{de(t)}{dt}$$

where $K_i$ is the integral gain (1/s times $K_p$) and $K_d$ is the derivative gain (s times $K_p$).

- The **time constant** $\tau$ is the time for a first-order response to reach 63.2 percent of its final value.
- Feedback has a trade-off. Higher gain reduces error, but too much gain can make the loop oscillate or go unstable. Good design balances speed, accuracy and stability.

## Key equations

First-order plant with gain $K$ and time constant $\tau$ (both positive):

$$G(s) = \frac{K}{\tau s + 1}$$

Units: $K$ is dimensionless if input and output share units, $\tau$ is in seconds (s).

Closed loop with proportional gain $K_p$ and unity feedback:

$$T(s) = \frac{Y(s)}{R(s)} = \frac{K_p K}{\tau s + 1 + K_p K}$$

This is still first order. Rewrite it as

$$T(s) = \frac{K_{cl}}{\tau_{cl}s + 1}, \qquad K_{cl} = \frac{K_p K}{1 + K_p K}, \qquad \tau_{cl} = \frac{\tau}{1 + K_p K}$$

Step response to a unit step, $R(s) = 1/s$:

$$y(t) = K_{cl}\left(1 - e^{-t/\tau_{cl}}\right)$$

Steady-state error for a unit step (the error is $1 - y(\infty)$):

$$e_{ss} = \frac{1}{1 + K_p K}$$

Sign conventions: a larger $K_p K$ shrinks both the steady error and the closed-loop time constant. The 2 percent settling time of a first-order response is about $4\tau_{cl}$.

## Worked example

**Problem.** A heater plant has a steady gain $K = 2.0$ (output units per input unit) and a time constant $\tau = 0.50$ s. It is closed with unity feedback and a proportional controller with $K_p = 4.0$. Find the closed-loop gain, the steady-state error to a unit step, the closed-loop time constant, the output at one closed-loop time constant, and the 2 percent settling time.

**Given.** $K = 2.0$, $\tau = 0.50$ s, $K_p = 4.0$, unit step reference.

**Find.** $K_{cl}$, $e_{ss}$, $\tau_{cl}$, $y(\tau_{cl})$, $t_{2\%}$.

**Assumptions.** The plant is linear and first order. The sensor is perfect and has unity gain. The actuator is ideal.

**Solution.**

1. Product of gains: $K_p K = 4.0 \cdot 2.0 = 8.0$.
2. Closed-loop gain: $K_{cl} = 8.0/(1+8.0) = 0.889$.
3. Steady-state error: $e_{ss} = 1/(1+8.0) = 0.111$, which is 11.1 percent of the step.
4. Closed-loop time constant: $\tau_{cl} = 0.50/9.0 = 0.0556$ s.
5. Output at $t = \tau_{cl}$: $y = 0.889(1 - e^{-1}) = 0.889 \cdot 0.632 = 0.562$.
6. 2 percent settling time: about $4\tau_{cl} = 0.222$ s.

**Answer.**

- $K_{cl} = 0.889$
- $e_{ss} = 0.111$ (about 11 percent)
- $\tau_{cl} = 0.0556$ s
- $y(0.0556\ \text{s}) = 0.562$
- Settling to within 2 percent takes about 0.22 s.

**Verification with Python.** The model was simulated with `scipy.signal`. This is the exact code that was run, with the output printed under it.

```python
import numpy as np
from scipy import signal
K, tau, Kp = 2.0, 0.5, 4.0
# plant G = K/(tau s + 1), P controller, unity feedback
num = [Kp*K]
den = [tau, 1 + Kp*K]
T = signal.TransferFunction(num, den)
t, y = signal.step(T, T=np.linspace(0, 1.0, 2001))
ess = 1 - y[-1]
print("steady-state output", round(y[-1],4), "error", round(ess,4))
print("formula error", round(1/(1+Kp*K),4))
print("closed-loop tau", round(tau/(1+Kp*K),4))
print("10-90 rise approx", round(t[np.argmax(y>=0.9*y[-1])] - t[np.argmax(y>=0.1*y[-1])],4))
print("y at t=0.0556", round(np.interp(tau/(1+Kp*K), t, y),4))
```

Output:

```
steady-state output 0.8889 error 0.1111
formula error 0.1111
closed-loop tau 0.0556
10-90 rise approx 0.122
y at t=0.0556 0.5619
```

The 10-90 rise time, $0.122$ s, matches $2.197\,\tau_{cl} = 0.122$ s.

**Sanity check.** The output stops at 0.889, not 1.0, so a P-only loop leaves a steady error. Raising $K_p$ to 19 (so $K_p K = 38$) would cut the error to about 2.6 percent, and the closed-loop time constant would drop again. The price in a real system is that a plant with dead time or resonance would become unstable first. This first-order model does not show that, so treat its gain limits with care.

## Practice

1. A plant has $K = 1.0$ and $\tau = 2.0$ s. It is closed with unity feedback and $K_p = 9.0$. Find $e_{ss}$ for a unit step.
2. For the same loop as problem 1, find $\tau_{cl}$ in seconds.
3. Using the same loop, find $y$ at $t = \tau_{cl}$.
4. The same plant now has $K_p = 19.0$. Find $e_{ss}$.
5. Give the 2 percent settling time for the loop in problem 1, in seconds.

<details><summary>Answers</summary>

1. 0.100
2. 0.2
3. 0.569
4. 0.050
5. 0.8

</details>

## Common mistakes

- Forgetting the feedback. The closed-loop gain is $K_p K/(1+K_p K)$, not $K_p K$. The $1+$ is the feedback term.
- Using the open-loop time constant $\tau$ for the closed loop. Feedback changes the time constant to $\tau/(1+K_p K)$.
- Reading steady-state error from a transient. Check the final value after the response has settled.
- Expecting a P controller to remove error completely. For a first-order plant with a step input it cannot, because the output only reaches $K_{cl}$.
- Adding integral or derivative gain without checking stability. Each term changes the closed-loop poles.

## Go deeper

- [Feedback Systems: An Introduction for Scientists and Engineers](https://www.cds.caltech.edu/~murray/books/AM08/pdf/am08-complete_22Feb09.pdf) by Karl Johan Åström and Richard M. Murray: the complete first edition as a free PDF from Caltech. A full controls textbook, from modeling through PID and frequency response.
- [MIT OpenCourseWare 2.14 Analysis and Design of Feedback Control Systems (Spring 2014)](https://ocw.mit.edu/courses/2-14-analysis-and-design-of-feedback-control-systems-spring-2014/) by MIT: a free undergraduate course on transfer functions, time response, root locus and loop shaping.
- [MIT OpenCourseWare 2.14, calendar](https://ocw.mit.edu/courses/2-14-analysis-and-design-of-feedback-control-systems-spring-2014/pages/calendar/) by MIT: lists the lecture on PID control and the lecture on first- and second-order time response, which match this lesson.
- [MIT OpenCourseWare 2.14, syllabus](https://ocw.mit.edu/courses/2-14-analysis-and-design-of-feedback-control-systems-spring-2014/pages/syllabus) by MIT: states that the course uses linear transfer function models and analysis in the time and frequency domains.
