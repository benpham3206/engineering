# Calculators

**Type:** lesson

A calculator is a device or app that does arithmetic and other math, such as powers, logarithms, and trigonometry, on numbers you enter. Knowing its strengths and limits matters to an engineer because a wrong keystroke gives a confident-looking wrong answer.

It is the fastest tool for a quick number, an exam, or a check on the shop floor. Knowing when to use one, and when to switch to code or a spreadsheet, saves time and prevents a whole class of silent errors.

**Prerequisites:** [Algebra](../math/01-algebra.md) and [Trigonometry](../math/02-trigonometry.md). [Axial and torsion](../physics/04-axial-and-torsion.md) helps with the worked example.
**Time:** 2-4 h, then practice until it is automatic

## Core ideas

### When to use a calculator

- **Use one** for quick checks, estimates, single formulas, unit conversions, exams, and anywhere a computer is not practical, such as the shop, the field, or a meeting.
- **Switch to a spreadsheet or code** when you repeat the same calculation with different inputs, when there are more than a few steps, when someone else must check your work, or when you need a plot. A calculation in a script can be reread, rerun, and reviewed. Keystrokes cannot.
- **Rule of thumb.** If you will do it twice, or if it matters, write it down where it can be checked. See [Python](02-python.md) and [Spreadsheets](03-spreadsheets.md).

### Kinds of calculators

- **Scientific:** arithmetic, powers, logs, trig, statistics, often fractions and simple equation solving. Enough for most engineering work and the only kind allowed in many licensing exams.
- **Graphing:** adds plots, tables, matrices, and programs. Useful for seeing a function's shape and finding roots or intersections.
- **CAS (computer algebra system):** works with symbols, not just numbers. It can solve, differentiate, integrate, and simplify expressions. Powerful, but you must still be able to check what it gives you.
- **Software calculators and phone apps:** free, often very capable, and fine for practice. Many graphing and CAS calculators have free official emulators. See [Free engineering software](09-free-software.md).

### How to use one well

- **Estimate first.** Before you press anything, guess the answer to within a factor of ten. If the screen disagrees with your estimate, one of them is wrong; find out which.
- **Check the angle mode.** Degrees or radians is the most common calculator error in engineering. $\sin(30)$ in radian mode is about $-0.988$, not $0.5$.
- **Store intermediate results** in memory instead of retyping rounded values. Rounding early changes the final digits. Round once, at the end.
- **Use parentheses generously.** $a/bc$ is read differently by different calculators. Type $a/(b \cdot c)$.
- **Know your entry mode.** Algebraic entry evaluates the expression as written. RPN, or reverse Polish notation, is used on many HP calculators. It puts numbers on a stack and applies operators after them. It needs no parentheses and shows every intermediate result. Both work. Pick one and practice it until you do not think about it.
- **Carry units on paper,** even when the calculator does not. Some calculators can attach units to numbers and convert them; use that if yours does, but check it once by hand.
- **Write down the inputs and the result** with units. A number on a screen is gone the moment you press clear.

### Useful features worth learning

- **Equation solver:** enter an equation once, then solve for any variable.
- **Statistics:** mean, standard deviation, and linear regression on entered data.
- **Complex numbers:** for AC circuits and vibrations.
- **Matrices:** for small systems of equations.
- **Unit conversion and physical constants:** built into many scientific calculators.
- **Number bases:** binary and hexadecimal for electronics and programming.

## Key equations

There are no calculator-specific equations, but two habits are worth writing as rules:

- Percent error of a result against an estimate or a second method: $\text{error} = \dfrac{|x_{\text{calc}} - x_{\text{check}}|}{|x_{\text{check}}|} \times 100\%$
- Degrees to radians: $\theta_{\text{rad}} = \theta_{\text{deg}} \times \dfrac{\pi}{180}$

## Worked example

**Given:** A solid steel shaft transmits $P = 5$ kW at $n = 1500$ rpm. The allowable shear stress is $\tau_{\text{allow}} = 40$ MPa.

**Find:** The minimum shaft diameter, using a calculator, with an estimate first and a check after.

**Assumptions:** Pure torsion, solid circular shaft, steady load.

**Estimate first:** $\omega$ is about $1500 \times 6 / 60 \approx 150$ rad/s, so $T \approx 5000/150 \approx 33$ N m. Then $d^3 \approx 16 \times 33 / (3 \times 4 \times 10^7) \approx 4.4 \times 10^{-6}$ m$^3$, so $d$ is about 16 mm.

**Solution on the calculator:**

1. Angular speed: $\omega = 2\pi n / 60 = 2\pi \times 1500 / 60 = 157.08$ rad/s. Store it.
2. Torque: $T = P/\omega = 5000 / 157.08 = 31.831$ N m. Store it.
3. Diameter from $\tau = 16T/(\pi d^3)$:
   $$d = \left(\frac{16T}{\pi \tau_{\text{allow}}}\right)^{1/3} = \left(\frac{16 \times 31.831}{\pi \times 40 \times 10^6}\right)^{1/3} = 0.015944\ \text{m}$$
   Type the whole expression with parentheses, using the stored $T$, and take the cube root last.

**Answer:** $d_{\min} \approx 15.9$ mm. Choose the next standard size up, for example 16 mm or larger after applying a factor of safety.

**Sanity check:** The estimate was about 16 mm and the result is 15.9 mm, about 2 percent apart. The units work out: N m divided by Pa gives m$^3$, and the cube root gives m.

## Practice

1. Set your calculator to radians and compute $\sin(30)$. Then set it to degrees and compute it again. Write down both.
2. A stone falls from rest for 2.5 s with $g = 9.81$ m/s$^2$ (Earth surface). Find the distance fallen, estimating first.
3. How long does an object take to fall 10 m from rest on Earth?
4. A 120 N force acts at 35 degrees above horizontal. Find its horizontal component.
5. Find the equivalent resistance of 220 ohm and 330 ohm in parallel, using memory for the intermediate values.

<details><summary>Answers</summary>

1. Radians: about $-0.988$. Degrees: $0.5$.
2. About 30.7 m.
3. About 1.43 s.
4. About 98.3 N.
5. 132 ohm.

</details>

## Common mistakes

- Wrong angle mode. Check it before every trig problem, and after anyone else uses your calculator.
- Retyping rounded intermediate values instead of using memory.
- Missing parentheses around a denominator or an exponent.
- Trusting a CAS result you cannot check. Substitute the answer back into the original equation.
- Doing a long, important calculation only on a calculator, so nobody can review it. Move it to a script or spreadsheet.
- Bringing a calculator to an exam without checking the rules. Licensing exams often allow only specific scientific models; for example, the NCEES exams in the United States publish an approved list (as of 2026, certain Casio, HP, and TI scientific models, and no graphing or CAS calculators).

## Go deeper

- [Free engineering software](09-free-software.md) in this folder: free calculator apps, emulators, and the HP calculator Connectivity Kit.
- [Python](02-python.md) in this folder: what to switch to when a calculation outgrows a calculator.
- [Problem-solving](../problem-solving/README.md): estimation and sanity checks, the habits that make calculator results trustworthy.
- [Tools reference](reference.md): the lookup sheet for this topic.
