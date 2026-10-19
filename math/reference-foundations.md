# Math foundations reference

**Type:** reference
**Verify:** strict

A lookup sheet for the arithmetic, algebra, geometry, trigonometry, and complex numbers that every other sheet in this repo assumes, written for a reader with no mathematics background who needs a rule, a formula, or a quick check.

## Principles

- A number is a quantity, and an engineering number carries a unit. A result with the wrong unit is wrong even when the arithmetic is right.
- An equation is a balance. Whatever you do to one side, you do to the other, and the balance holds.
- Operations have a fixed order. Everyone who follows the same order gets the same answer from the same expression.
- A formula is a recipe with stated limits. Use it only where its conditions hold.
- Dividing by zero has no meaning. A formula that asks for it is telling you the situation it describes does not exist.
- Rounding happens once, at the end. Rounding in the middle of a calculation adds error that the final digits cannot hide.
- A drawing, a graph, or an estimate catches errors that arithmetic repeats. Look at the answer and ask whether it is the right size.
- Angles in an equation are in radians. Degrees are a way to write an angle for people and are converted before use.
- The same rule often shows up in a new place. Slope, ratio, and percent change are one idea seen from three sides.

## Arithmetic and order of operations

### Order of operations

An **expression** is a group of numbers joined by operations such as add, subtract, multiply, and divide. Work an expression in this order:

1. Brackets first, innermost first.
2. Powers and roots.
3. Multiplication and division, left to right.
4. Addition and subtraction, left to right.

A **negative number** is a number below zero. Multiplying or dividing two numbers with the same sign gives a positive result. Multiplying or dividing two numbers with different signs gives a negative result. The **absolute value** of a number, written $|x|$, is its distance from zero and is never negative.

Examples:

- $3 + 4 \times 2$ gives 11, because the multiplication comes first.
- $(3 + 4) \times 2$ gives 14, because the brackets come first.
- $20 - 2^{3} \div 4$ gives 18, because $2^{3} = 8$, then $8 \div 4 = 2$, then $20 - 2 = 18$.
- $(-6) \times (-3)$ gives 18, and $(-6) \times 3$ gives $-18$.

```verify
expect(3 + 4 * 2, "11")
expect((3 + 4) * 2, "14")
expect(20 - 2**3 / 4, "18")
expect((-6) * (-3), "18")
expect((-6) * 3, "-18")
```

Holds when: the expression is written in the standard notation above.
Breaks when: a calculator or program uses different rules for chained division (check by putting brackets around every step you care about) or when a written fraction bar hides a bracket (the whole top and the whole bottom are each in brackets).
Source and basis: derived from the definition of the operations and the convention that makes expressions unambiguous; taught in [Algebra](01-algebra.md).

### The distributive law

The **distributive law** says that multiplying a sum equals multiplying each part and adding. It lets you expand a bracket or pull a common factor out.

$$a(b + c) = ab + ac$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $a$, $b$, $c$ | any three numbers or quantities with compatible units ($b$ and $c$ share a unit) | dimensionless |

Holds when: the operation inside the bracket is addition or subtraction.
Breaks when: you apply it to a power or root. $(a + b)^{2}$ is not $a^{2} + b^{2}$; the full expansion is in the algebra section below.
Source and basis: derived from the meaning of multiplication as repeated addition.

Example: $7 \times 98$ is easier as $7 \times (100 - 2) = 700 - 14 = 686$.

```verify
n98 = q(98, "")
n100 = q(100, "")
expect(n100 - 2, "98")
expect(7 * n98, "686")
expect(7 * (100 - 2), "686")
expect(7 * 100, "700")
expect(7 * 2, "14")
expect(7 * 100 - 7 * 2, "686")
```

## Fractions, ratios, proportions, and percent

### Fractions

A **fraction** $\frac{a}{b}$ is the number you get by dividing $a$ (the numerator) by $b$ (the denominator, which cannot be zero). Two fractions are equal when they are the same number written differently, such as $\frac{1}{2}$ and $\frac{3}{6}$.

$$\frac{a}{b} + \frac{c}{d} = \frac{ad + bc}{bd} \qquad \frac{a}{b} \cdot \frac{c}{d} = \frac{ac}{bd} \qquad \frac{a}{b} \div \frac{c}{d} = \frac{ad}{bc}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $a$, $c$ | numerators | dimensionless |
| $b$, $d$ | denominators, not zero | dimensionless |

Holds when: all four numbers are ordinary numbers and $b$, $d$, and $c$ (in the division rule) are not zero.
Breaks when: you add the tops and the bottoms separately ($\frac{1}{2} + \frac{1}{3}$ is not $\frac{2}{5}$) or when a zero sits in a denominator.
Source and basis: derived from the definition of division and the rule that multiplying top and bottom by the same number does not change a fraction; taught in [Algebra](01-algebra.md).

Examples:

- $\frac{1}{2} + \frac{1}{3} = \frac{5}{6} = 0.8333$.
- $\frac{3}{4} \times \frac{2}{9} = \frac{6}{36} = \frac{1}{6} = 0.1667$.
- $\frac{3}{4} \div \frac{9}{2} = \frac{6}{36} = 0.1667$. Dividing by a fraction means multiplying by its flip.

```verify
expect(1/2 + 1/3, "0.8333")
expect((1*3 + 1*2) / (2*3), "0.8333")
expect(3/4 * 2/9, "0.1667")
expect((3/4) / (9/2), "0.1667")
```

### Ratios and proportions

A **ratio** compares two quantities of the same kind by division, such as 3 parts cement to 12 parts sand. A **proportion** states that two ratios are equal. Cross-multiplying solves for the one unknown.

$$\frac{a}{b} = \frac{c}{d} \quad\Longrightarrow\quad ad = bc \quad\Longrightarrow\quad d = \frac{bc}{a}$$

**Direct proportion** means $y = kx$: doubling $x$ doubles $y$. **Inverse proportion** means $y = k/x$: doubling $x$ halves $y$. The constant $k$ is found from one known pair.

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $a$, $b$, $c$, $d$ | the four members of the proportion, $a$ and $b$ not zero | dimensionless |
| $k$ | constant of proportionality | dimensionless |

Holds when: the quantities really are proportional, so the graph of $y$ against $x$ is a straight line through the origin (direct) or a curve $y = k/x$ (inverse).
Breaks when: the relationship has an offset (a taxi fare with a starting charge is not proportional to distance) or curves in another way. Check with a second data point.
Source and basis: derived from the definition of equal ratios.

Example: a recipe uses 150 g of flour for 6 portions. For 10 portions the flour is $d = \frac{150 \times 10}{6} = 250$ g. Inverse case: a job takes 4 workers 15 days. With 6 workers the same job takes $k/x$ with $k = 4 \times 15 = 60$ worker-days, so $60/6 = 10$ days.

```verify
flour = q(150, "g") * 10 / 6
expect(flour, "250 g")
workers = q(4, "")
days = q(15, "")
k = workers * days
expect(k, "60")
expect(k / 6, "10")
```

### Percent and percent change

**Percent** means "per hundred". It is a fraction multiplied by 100. **Percent change** compares a new value to the old value it replaces.

$$p = 100\,\frac{\text{part}}{\text{whole}} \qquad \Delta p = 100\,\frac{x_{\text{new}} - x_{\text{old}}}{x_{\text{old}}}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $p$ | the part as a percent of the whole | dimensionless |
| $\Delta p$ | percent change from old to new | dimensionless |
| $x_{\text{old}}$, $x_{\text{new}}$ | the quantity before and after, in one shared unit; $x_{\text{old}}$ not zero | dimensionless |

Holds when: the whole (or the old value) is the correct base for the comparison and is not zero.
Breaks when: percents are added across different bases. A rise of 50 percent followed by a fall of 50 percent does not return to the start, because the second percent is taken of a larger number.
Source and basis: derived from the definition of percent as a fraction of one hundred.

Examples:

- A part is 18 mm of a 240 mm bar, so it is $100 \times 18/240 = 7.5$ percent of the length.
- A force rises from 400 N to 460 N. The change is $100 \times 60/400 = 15$ percent.
- A price of 80 rises 50 percent to 120, then falls 50 percent to 60. The net change is $-25$ percent.

```verify
expect(100 * q(18, "mm") / q(240, "mm"), "7.5")
expect(100 * (q(460, "N") - q(400, "N")) / q(400, "N"), "15")
expect(100 * q(60, "N") / q(400, "N"), "15")
expect(80 * 1.5, "120")
expect(120 * 0.5, "60")
expect(100 * (60 - 80) / 80, "-25")
```

## Powers, roots, and scientific notation

### Laws of powers and roots

A **power** $a^{n}$ means $a$ multiplied by itself $n$ times, where $n$ is the **exponent**. A **square root** $\sqrt{a}$ is the non-negative number whose square is $a$. A **cube root** is the number whose cube is $a$. A root is a power with a fractional exponent.

$$a^{m} a^{n} = a^{m+n} \qquad \frac{a^{m}}{a^{n}} = a^{m-n} \qquad (a^{m})^{n} = a^{mn} \qquad a^{0} = 1 \qquad a^{-n} = \frac{1}{a^{n}} \qquad a^{1/n} = \sqrt[n]{a}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $a$ | the base, not zero when the exponent is zero or negative; not negative when the exponent is a fraction | dimensionless |
| $m$, $n$ | exponents; $n$ in the root rule is a positive whole number | dimensionless |

Holds when: the base is a real number and every power or root named is defined.
Breaks when: bases differ or terms are added. $a^{m} + a^{n}$ does not simplify to $a^{m+n}$, and $\sqrt{a + b}$ is not $\sqrt{a} + \sqrt{b}$. A square root of a negative number is not a real number (see the complex numbers section).
Source and basis: derived from the definition of a power as repeated multiplication; taught in [Algebra](01-algebra.md).

Examples:

- $2^{3} \times 2^{4} = 2^{7} = 128$.
- $2^{-3} = 1/8 = 0.125$.
- $16^{1/2} = 4$ and $27^{1/3} = 3$.
- A square with side 0.3 m has area $0.3^{2} = 0.09$ $\text{m}^{2}$. To get a side from an area of 50 $\text{m}^{2}$, $\sqrt{50} = 7.071$ m.

```verify
expect(2**3 * 2**4, "128")
expect(2**7, "128")
expect(2**(-3), "0.125")
expect(16**0.5, "4")
expect(27**(1/3), "3")
expect(q(0.3, "m")**2, "0.09 m^2")
expect(sqrt(q(50, "m^2")), "7.071 m")
```

### Scientific notation and SI prefixes

**Scientific notation** writes a number as a mantissa between 1 and 10 times a power of ten. It keeps very large and very small numbers readable and shows how many digits are meaningful.

$$x = m \times 10^{n}, \qquad 1 \le |m| < 10$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $x$ | the number | dimensionless |
| $m$ | the mantissa | dimensionless |
| $n$ | the whole-number exponent: how far the decimal point moved | dimensionless |

Holds when: $x$ is not zero.
Breaks when: you multiply or divide numbers with different exponents without combining them. Multiply the mantissas, add the exponents, then fix the mantissa back into the range 1 to 10.
Source and basis: derived from the laws of powers above; the prefix names and symbols are defined by the SI and listed in [Units](../data/units.md) and [the measurement reference](../measurement/reference.md).

Common SI prefixes (a prefix is a name that multiplies a unit by a power of ten):

| Prefix | Symbol | Factor |
|---|---|---|
| tera | T | $10^{12}$ |
| giga | G | $10^{9}$ |
| mega | M | $10^{6}$ |
| kilo | k | $10^{3}$ |
| milli | m | $10^{-3}$ |
| micro | $\mu$ | $10^{-6}$ |
| nano | n | $10^{-9}$ |
| pico | p | $10^{-12}$ |

Examples:

- $45\,300\,000 = 4.53 \times 10^{7}$, which is 45.3 mega.
- $0.00072 = 7.2 \times 10^{-4}$.
- $(3 \times 10^{5}) \times (4 \times 10^{-2}) = 12 \times 10^{3} = 1.2 \times 10^{4}$.
- $2.5\ \text{GPa} = 2.5 \times 10^{9}\ \text{Pa}$, and $350\ \mu\text{m} = 3.5 \times 10^{-4}\ \text{m}$.

```verify
expect(q(4.53, "") * 1e7, "4.53e7")
expect(q(7.2, "") * 1e-4, "0.00072")
expect(3e5 * 4e-2, "1.2e4")
expect(3 * 4, "12")
expect(q(2.5, "GPa"), "2.5e9 Pa")
expect(q(350, "um"), "3.5e-4 m")
```

## Significant figures and rounding

### Significant figures

**Significant figures** are the digits of a number that carry information about how well it is known. Rules for counting them:

- All non-zero digits count.
- Zeros between non-zero digits count.
- Leading zeros never count: 0.004560 has four significant figures (4, 5, 6, and the final 0).
- Trailing zeros after a decimal point count.
- Trailing zeros in a whole number with no decimal point are ambiguous. Write $1.20 \times 10^{3}$ to show three, or $1.2 \times 10^{3}$ to show two.
- Exact numbers, such as a count of 4 bolts or the 2 in $2\pi r$, have unlimited significant figures.

Rules for results:

- Multiply or divide: keep as many significant figures as the input that has the fewest.
- Add or subtract: keep as many decimal places as the input that has the fewest.
- Round only the final answer. Carry at least one extra digit through the steps.

**Rounding** to a place means keeping the digits down to that place and increasing the last kept digit by one when the next digit is 5 or more.

Examples:

- $3.2 \times 1.47 = 4.704$, which rounds to 4.7 because 3.2 has two significant figures.
- $12.1 + 0.256 = 12.356$, which rounds to 12.4 because 12.1 has one decimal place.
- $1234.5678$ rounded to 2 decimal places is 1234.57.

```verify
expect(rnd(q(3.2, "") * q(1.47, ""), 1, ""), "4.7")
expect(rnd(q(12.1, "") + q(0.256, ""), 1, ""), "12.4")
expect(rnd(q(1234.5678, ""), 2, ""), "1234.57")
```

Holds when: the inputs are measured values with the usual uncertainty of plus or minus one in the last digit.
Breaks when: uncertainties are known to be larger or smaller than that. Then state the uncertainty and round to it, as in [Propagating uncertainty and significant figures](../measurement/03-propagating-uncertainty-and-significant-figures.md).
Source and basis: a bookkeeping convention that approximates uncertainty propagation; derived from the rules for combining uncertainties in that lesson.

## Algebra and equation rearrangement

### Solving a linear equation

A **linear equation** in $x$ has $x$ only to the first power. Undo the operations around $x$ in reverse order, doing the same thing to both sides.

$$a x + b = c \quad\Longrightarrow\quad x = \frac{c - b}{a}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $x$ | the unknown | dimensionless |
| $a$ | the coefficient of $x$, not zero | dimensionless |
| $b$, $c$ | constants with the same unit as $a x$ | dimensionless |

Holds when: $a$ is not zero.
Breaks when: $a = 0$ (no solution, or every $x$ works), or when the unknown also appears in a power, a root, or a denominator (those need other methods).
Source and basis: derived from the balance rule for equations; taught in [Algebra](01-algebra.md).

Example: $5x + 7 = 32$ gives $x = (32 - 7)/5 = 5$. Check: $5 \times 5 + 7 = 32$.

To rearrange a formula, treat the symbol you want as the unknown. For the distance under steady acceleration from rest, $s = \tfrac{1}{2} a t^{2}$, the time is $t = \sqrt{2 s / a}$. With $s = 20$ m and $a = 5$ $\text{m/s}^{2}$ the time is 2.828 s. The units check: $\sqrt{\text{m} / (\text{m/s}^{2})} = \sqrt{\text{s}^{2}} = \text{s}$.

```verify
x = (q(32, "") - q(7, "")) / q(5, "")
expect(x, "5")
expect(5 * x + 7, "32")
s = q(20, "m")
a = q(5, "m/s^2")
expect(sqrt(2 * s / a), "2.828 s")
```

### Quadratic equation

A **quadratic equation** has $x$ to the second power as its highest power. It has two real solutions, one repeated solution, or none, depending on the **discriminant** $b^{2} - 4ac$.

$$a x^{2} + b x + c = 0 \quad\Longrightarrow\quad x = \frac{-b \pm \sqrt{b^{2} - 4ac}}{2a}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $x$ | the unknown | dimensionless |
| $a$ | coefficient of $x^{2}$, not zero | dimensionless |
| $b$ | coefficient of $x$ | dimensionless |
| $c$ | constant term | dimensionless |

Holds when: $a \ne 0$. A positive discriminant gives two real solutions, zero gives one, and a negative one gives two complex solutions.
Breaks when: $a$ is very small next to $b$, where subtracting two nearly equal numbers loses digits. Compute the larger-magnitude solution first, then use the product of the solutions $c/a$ for the other.
Source and basis: derived by completing the square; taught in [Algebra](01-algebra.md).

Example: $x^{2} - 5x + 6 = 0$ has $b^{2} - 4ac = 25 - 24 = 1$, so $x = (5 \pm 1)/2$, giving 3 and 2. The solutions sum to $-b/a = 5$ and multiply to $c/a = 6$.

```verify
a = 1
b = -5
c = 6
disc = b**2 - 4*a*c
expect(b**2, "25")
expect(4*a*c, "24")
expect(disc, "1")
x1 = (-b + sqrt(disc)) / (2*a)
x2 = (-b - sqrt(disc)) / (2*a)
expect(x1, "3")
expect(x2, "2")
expect(x1 + x2, "5")
expect(x1 * x2, "6")
```

### Useful expansions

$$(a + b)^{2} = a^{2} + 2ab + b^{2} \qquad (a - b)^{2} = a^{2} - 2ab + b^{2} \qquad a^{2} - b^{2} = (a - b)(a + b)$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $a$, $b$ | any numbers or quantities with the same unit | dimensionless |

Holds when: $a$ and $b$ are ordinary numbers or quantities of one shared unit.
Breaks when: the units of $a$ and $b$ differ, because then the sum has no meaning.
Source and basis: derived from the distributive law applied twice.

Example: $51^{2} = (50 + 1)^{2} = 2500 + 100 + 1 = 2601$, and $99 \times 101 = 100^{2} - 1^{2} = 9999$.

```verify
n = q(51, "")
n50 = q(50, "")
expect(n**2, "2601")
expect((50 + 1)**2, "2601")
expect(50**2, "2500")
expect(2*50*1, "100")
expect(50**2 + 2*50*1 + 1, "2601")
expect(100**2 - 1**2, "9999")
expect(q(99, "") * q(101, ""), "9999")
```

## Logarithms and exponentials (basic rules only)

### Logarithm rules

The **logarithm** of a positive number $x$ to base $b$, written $\log_{b} x$, is the exponent you put on $b$ to get $x$. So $\log_{10} 1000 = 3$ because $10^{3} = 1000$. The **natural logarithm** $\ln x$ uses the base $e = 2.71828$, a constant that appears wherever growth is proportional to size. A logarithm turns multiplication into addition.

$$\log_{b}(xy) = \log_{b} x + \log_{b} y \qquad \log_{b}\frac{x}{y} = \log_{b} x - \log_{b} y \qquad \log_{b}(x^{n}) = n \log_{b} x \qquad \log_{b} x = \frac{\ln x}{\ln b}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $x$, $y$ | positive numbers | dimensionless |
| $b$ | the base, positive and not 1 | dimensionless |
| $n$ | any real exponent | dimensionless |

Holds when: $x$ and $y$ are positive, because the logarithm of zero or a negative number is not a real number.
Breaks when: you apply it to a sum. $\log(x + y)$ does not simplify. Also take the logarithm of a pure number only; a quantity with a unit (a length in metres) must first be divided by a reference of the same unit.
Source and basis: derived from the laws of powers above, since a logarithm is an exponent.

Examples:

- $\log_{10} 2000 = \log_{10} 2 + \log_{10} 1000 = 0.3010 + 3 = 3.301$.
- $\ln 8 = 3 \ln 2 = 2.079$.
- $\log_{2} 1024 = \ln 1024 / \ln 2 = 10$.

```verify
expect(log10(2000), "3.301")
expect(log10(2) + 3, "3.301")
expect(log(8), "2.079")
expect(3 * log(2), "2.079")
expect(log(1024) / log(2), "10")
```

### Exponential growth and decay

**Exponential growth** is a quantity that changes by a fixed fraction in each equal step. A positive $k$ gives growth, and a negative $k$ gives decay.

$$y = y_{0}\, e^{k t} \qquad t = \frac{1}{k} \ln\frac{y}{y_{0}}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $y$ | quantity at time $t$ | dimensionless |
| $y_{0}$ | quantity at $t = 0$ | dimensionless |
| $k$ | rate constant | 1/s |
| $t$ | time | s |

Holds when: the rate of change is proportional to the current value and $k$ is constant.
Breaks when: the growth is limited (a supply runs out) or the rate changes with time. A real cooling or charging process needs its own model.
Source and basis: derived from the definition of $e$ and the logarithm rules above; the calculus behind it is in [Single-variable calculus](03-single-variable-calculus.md).

Example: a quantity that grows 3 percent per step doubles after $\ln 2 / \ln 1.03 = 23.45$ steps. A decaying signal with $k = -0.2\ \text{1/s}$ falls to $e^{-1} = 0.3679$ of its start after $t = 5$ s.

```verify
expect(log(2) / log(q(1.03, "")), "23.45")
k = q(-0.2, "1/s")
t = q(5, "s")
expect(exp(k * t), "0.3679")
```

## Functions and graphs

### Slope, intercept, and the straight line

A **function** is a rule that gives exactly one output for each input. Its **graph** plots output $y$ against input $x$. A straight line has a constant **slope** (how much $y$ changes per unit of $x$) and an **intercept** (the value of $y$ where the line crosses $x = 0$).

$$m = \frac{y_{2} - y_{1}}{x_{2} - x_{1}} \qquad y = m x + c$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $m$ | slope | dimensionless |
| $c$ | $y$-intercept | dimensionless |
| $(x_{1}, y_{1})$, $(x_{2}, y_{2})$ | two points on the line, $x_{2} \ne x_{1}$ | dimensionless |

Holds when: the relationship is truly linear over the range plotted.
Breaks when: the data curves, in which case the slope between two points depends on which two you pick. Between points on a curve the slope is an average; the slope at one point is a derivative (see [math/reference-calculus.md](reference-calculus.md)).
Source and basis: derived from the definition of slope as rise over run; taught in [Algebra](01-algebra.md).

Example: a spring reads 12 N at 10 mm and 30 N at 25 mm. The slope is $(30 - 12)/(25 - 10) = 1.2$ N/mm, which is 1200 N/m. The intercept is $12 - 1.2 \times 10 = 0$ N, so the force is proportional to the stretch.

```verify
m = (q(30, "N") - q(12, "N")) / (q(25, "mm") - q(10, "mm"))
expect(m, "1.2 N/mm")
expect(m, "1200 N/m")
c = q(12, "N") - m * q(10, "mm")
expect(c, "0 N")
```

### Reading a log scale

On a **logarithmic axis** equal distances mean equal ratios, not equal differences. Each step from one power of ten to the next is a **decade**, and the numbers 1, 10, 100, 1000 are evenly spaced. On a **log-log plot** both axes are logarithmic, and a power law $y = a x^{n}$ plots as a straight line whose slope is the exponent $n$. On a **semi-log plot** only one axis is logarithmic, and an exponential $y = y_{0} e^{k t}$ plots as a straight line.

$$n = \frac{\log_{10} y_{2} - \log_{10} y_{1}}{\log_{10} x_{2} - \log_{10} x_{1}} \qquad a = \frac{y_{1}}{x_{1}^{\,n}}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $n$ | power-law exponent, the slope on a log-log plot | dimensionless |
| $a$ | power-law coefficient | dimensionless |
| $(x_{1}, y_{1})$, $(x_{2}, y_{2})$ | two points on the line, all values positive | dimensionless |

Holds when: the data follow a power law over the range read and all values are positive.
Breaks when: the points do not fall on a straight line (the law does not fit) or a value is zero or negative (it cannot be plotted). Read the slope in axis units of decades, not centimetres of paper, unless both axes use the same decade length.
Source and basis: derived from the logarithm rules above, since $\log y = \log a + n \log x$.

Examples:

- Points (10, 4) and (100, 400) give $n = (\log_{10} 400 - \log_{10} 4)/(\log_{10} 100 - \log_{10} 10) = 2$ and $a = 4/10^{2} = 0.04$.
- The point halfway along a decade between 1 and 10 is $\sqrt{10} = 3.162$, not 5.5.

```verify
n = (log10(400) - log10(4)) / (log10(100) - log10(10))
expect(n, "2")
expect(4 / 10**2, "0.04")
expect(sqrt(10), "3.162")
```

## Geometry

### Areas and perimeters

**Area** is the amount of flat surface inside a shape, measured in square units. **Perimeter** is the length around the edge.

$$A_{\text{rect}} = b h \qquad A_{\text{tri}} = \tfrac{1}{2} b h \qquad A_{\text{trap}} = \tfrac{1}{2}(b_{1} + b_{2}) h \qquad A_{\text{circle}} = \pi r^{2} \qquad C = 2 \pi r$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $A$ | area | $\text{m}^{2}$ |
| $C$ | circumference (the perimeter of a circle) | m |
| $b$, $b_{1}$, $b_{2}$ | base, or the two parallel sides of a trapezoid | m |
| $h$ | height, measured at right angles to the base | m |
| $r$ | radius of the circle | m |

Holds when: the shape is flat and the lengths are measured in one unit. The height $h$ is the perpendicular distance, not the slanted side.
Breaks when: units are mixed (convert first) or the shape is curved in three dimensions, such as the surface of a sphere (see the volumes entry).
Source and basis: derived from the definition of area as counting unit squares; $\pi$ is the ratio of a circle's circumference to its diameter.

Examples:

- A plate 0.40 m by 0.25 m has area 0.1 $\text{m}^{2}$.
- A circle with $r = 0.05$ m has area $\pi r^{2} = 0.007854$ $\text{m}^{2}$ and circumference 0.3142 m.
- A trapezoid with parallel sides 6 m and 10 m, 4 m apart, has area 32 $\text{m}^{2}$.
- Doubling the radius multiplies the area by 4, not 2.

```verify
expect(q(0.40, "m") * q(0.25, "m"), "0.1 m^2")
r = q(0.05, "m")
expect(pi * r**2, "0.007854 m^2")
expect(2 * pi * r, "0.3142 m")
expect(0.5 * (q(6, "m") + q(10, "m")) * q(4, "m"), "32 m^2")
expect(pi * (2*r)**2 / (pi * r**2), "4")
```

### Volumes and surface areas

**Volume** is the amount of space inside a solid, measured in cubic units.

$$V_{\text{box}} = l w h \qquad V_{\text{cyl}} = \pi r^{2} h \qquad V_{\text{cone}} = \tfrac{1}{3} \pi r^{2} h \qquad V_{\text{sphere}} = \tfrac{4}{3} \pi r^{3} \qquad A_{\text{sphere}} = 4 \pi r^{2}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $V$ | volume | $\text{m}^{3}$ |
| $A_{\text{sphere}}$ | surface area of a sphere | $\text{m}^{2}$ |
| $l$, $w$ | length and width of the box | m |
| $h$ | height (the cone's height is along its axis) | m |
| $r$ | radius | m |

Holds when: the solid has the exact shape named (a straight cylinder, a right circular cone, a true sphere).
Breaks when: the shape is tapered, hollow, or irregular. Split it into simple shapes, subtract holes, or measure by displacement.
Source and basis: derived from stacking cross-sections (box and cylinder) and from integration for the cone and sphere; the integration is in [Single-variable calculus](03-single-variable-calculus.md).

Examples:

- A cylinder with $r = 0.05$ m and $h = 0.20$ m holds $1.571 \times 10^{-3}$ $\text{m}^{3}$, which is 1.571 litres (1 litre is $10^{-3}$ $\text{m}^{3}$).
- A sphere with $r = 0.10$ m has $V = 4.189 \times 10^{-3}$ $\text{m}^{3}$ and surface area 0.1257 $\text{m}^{2}$.
- A cone is exactly one third of the cylinder with the same base and height.

```verify
r = q(0.05, "m")
h = q(0.20, "m")
Vc = pi * r**2 * h
expect(Vc, "1.571e-3 m^3")
expect(Vc, "1.571 L")
R = q(0.10, "m")
expect(4/3 * pi * R**3, "4.189e-3 m^3")
expect(4 * pi * R**2, "0.1257 m^2")
check(abs((pi * r**2 * h / 3) / Vc - 1/3) < 1e-9, "one third of the cylinder")
```

### Pythagoras and right triangles

A **right triangle** has one angle of exactly 90 degrees. The side opposite that angle is the **hypotenuse** and is the longest side. The **Pythagorean theorem** relates the three sides.

$$a^{2} + b^{2} = c^{2} \qquad c = \sqrt{a^{2} + b^{2}} \qquad a = \sqrt{c^{2} - b^{2}}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $a$, $b$ | the two shorter sides (legs) | m |
| $c$ | the hypotenuse | m |

Holds when: the triangle has a right angle and lies on a flat plane.
Breaks when: the triangle has no right angle (use the law of cosines in [the trigonometry reference](reference.md#trigonometry)) or lies on a curved surface such as a globe.
Source and basis: derived from comparing the areas of squares built on the sides; taught in [Trigonometry](02-trigonometry.md).

Examples:

- The 3-4-5 triangle: $\sqrt{9 + 16} = 5$, a handy right-angle check for a layout.
- A 5 m ladder with its foot 1.5 m from a wall reaches $\sqrt{25 - 2.25} = 4.770$ m up the wall.
- The diagonal of a 0.30 m by 0.40 m panel is 0.5 m.

```verify
expect(sqrt(3**2 + 4**2), "5")
L = q(5, "m")
foot = q(1.5, "m")
expect(sqrt(L**2 - foot**2), "4.770 m")
expect(sqrt(q(0.30, "m")**2 + q(0.40, "m")**2), "0.5 m")
```

### Similar triangles and scaling

Two shapes are **similar** when one is an exact enlargement of the other: all angles match and all lengths are in the same ratio $k$, the **scale factor**.

$$\frac{a'}{a} = \frac{b'}{b} = \frac{c'}{c} = k \qquad \frac{A'}{A} = k^{2} \qquad \frac{V'}{V} = k^{3}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $a$, $b$, $c$ | sides of the first shape | m |
| $a'$, $b'$, $c'$ | matching sides of the second shape | m |
| $k$ | scale factor | dimensionless |
| $A$, $A'$ | areas of the two shapes | $\text{m}^{2}$ |
| $V$, $V'$ | volumes of the two solids | $\text{m}^{3}$ |

Holds when: all angles match, so the shapes are true copies at different sizes.
Breaks when: only one dimension is scaled (a stretched shape is not similar) or when the material changes with size. Strength, weight, and heat loss do not scale the same way: weight goes as $k^{3}$ but cross-section as $k^{2}$.
Source and basis: derived from the definition of similarity and from counting unit squares and cubes.

Examples:

- A 2 m pole casts a 1.5 m shadow while a tree casts a 12 m shadow at the same moment. The sun angle is the same, so $k = 12/1.5 = 8$ and the tree is $2 \times 8 = 16$ m tall.
- A model at scale 1:10 ($k = 10$ from model to full size) has 100 times the area and 1000 times the volume.

```verify
k = q(12, "m") / q(1.5, "m")
expect(k, "8")
expect(q(2, "m") * k, "16 m")
kk = 10
expect(kk**2, "100")
expect(kk**3, "1000")
```

## Right-triangle trigonometry and radians

### Sine, cosine, and tangent

**Trigonometry** relates the angles of a right triangle to the ratios of its sides. For an angle $\theta$ other than the right angle, call the side across from it the **opposite**, the side touching it (not the hypotenuse) the **adjacent**, and the longest side the **hypotenuse**.

$$\sin\theta = \frac{\text{opp}}{\text{hyp}} \qquad \cos\theta = \frac{\text{adj}}{\text{hyp}} \qquad \tan\theta = \frac{\text{opp}}{\text{adj}} \qquad \theta = \arcsin\frac{\text{opp}}{\text{hyp}}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\theta$ | the angle, in radians in equations | rad |
| opp, adj, hyp | lengths of the opposite, adjacent, and hypotenuse sides | m |

Holds when: the triangle has a right angle and $0 < \theta < \pi/2$ for the side-ratio definitions. For other angles the functions are defined on the unit circle, with $\sin\theta$ and $\cos\theta$ the vertical and horizontal coordinates of the point at angle $\theta$.
Breaks when: your calculator is in degree mode while the formula expects radians, or the other way round (check with $\sin 90^{\circ} = 1$). $\tan\theta$ grows without limit as $\theta$ approaches $\pi/2$.
Source and basis: derived from the similarity of right triangles that share an angle (the ratios do not depend on size); taught in [Trigonometry](02-trigonometry.md). For identities and the laws of sines and cosines see [the trigonometry reference](reference.md#trigonometry).

Special angles (exact values):

| Angle | Radians | $\sin$ | $\cos$ | $\tan$ |
|---|---|---|---|---|
| $30^{\circ}$ | $\pi/6$ | $1/2$ | $\sqrt{3}/2$ | $1/\sqrt{3}$ |
| $45^{\circ}$ | $\pi/4$ | $\sqrt{2}/2$ | $\sqrt{2}/2$ | $1$ |
| $60^{\circ}$ | $\pi/3$ | $\sqrt{3}/2$ | $1/2$ | $\sqrt{3}$ |

Examples:

- A 5 m ladder at $70^{\circ}$ to the ground reaches $5 \sin 70^{\circ} = 4.698$ m up the wall and its foot is $5 \cos 70^{\circ} = 1.710$ m from the wall.
- A ramp rises 0.4 m over a horizontal run of 2.0 m. Its angle is $\arctan(0.4/2.0) = 0.1974$ rad, which is $11.31^{\circ}$.
- $\sin 30^{\circ} = 0.5$ and $\cos 45^{\circ} = 0.7071$.

```verify
L = q(5, "m")
th = q(70, "deg")
expect(L * sin(th), "4.698 m")
expect(L * cos(th), "1.710 m")
ang = atan(q(0.4, "m") / q(2.0, "m"))
expect(ang, "0.1974")
expect(ang * 180 / pi, "11.31")
expect(sin(q(30, "deg")), "0.5")
expect(cos(q(45, "deg")), "0.7071")
```

### Radians and arc length

A **radian** is the angle at the centre of a circle that cuts off an arc equal in length to the radius. A full turn is $2\pi$ rad, which is $360^{\circ}$. Equations in this repo use radians because the formulas for arc length, angular speed, and small angles are simplest in them.

$$\theta_{\text{rad}} = \theta_{\text{deg}} \cdot \frac{\pi}{180} \qquad s = r \theta$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\theta_{\text{rad}}$ | the angle in radians | rad |
| $\theta_{\text{deg}}$ | the same angle written in degrees (a pure number) | dimensionless |
| $s$ | arc length along the circle | m |
| $r$ | radius | m |
| $\theta$ | the angle in radians | rad |

Holds when: $\theta$ is in radians in the formula $s = r\theta$.
Breaks when: you put degrees into $s = r\theta$, which gives an answer about 57 times too large. For small angles (about $0.1$ rad or less) $\sin\theta \approx \theta$ and $\tan\theta \approx \theta$ to within about 1 percent; beyond that use the full function.
Source and basis: derived from the definition of the radian as arc length divided by radius.

Examples:

- $1\ \text{rad} = 180/\pi = 57.30^{\circ}$, and $90^{\circ} = 1.571$ rad.
- An arc of angle $40^{\circ}$ on a circle of radius 0.5 m has length $0.5 \times 0.6981 = 0.3491$ m.
- For $\theta = 0.1$ rad, $\sin\theta = 0.09983$, which differs from $\theta$ by 0.17 percent.

```verify
expect(180 / pi, "57.30")
expect(q(90, "deg"), "1.571 rad")
th = q(40, "deg")
expect(th, "0.6981 rad")
expect(q(0.5, "m") * th, "0.3491 m")
x = 0.1
expect(sin(x), "0.09983")
expect(100 * (x - sin(x)) / sin(x), "0.17")
```

## Complex numbers

### Rectangular and polar form

An **imaginary number** is a multiple of $j$, where $j$ is defined by $j^{2} = -1$. A **complex number** adds a real part and an imaginary part. It describes a point on a plane, with the real part along the horizontal axis and the imaginary part along the vertical axis. The **magnitude** $r$ is its distance from the origin and the **angle** $\varphi$ is measured counterclockwise from the positive real axis. This repo writes $j$ rather than $i$, as set in [Notation](../data/notation.md).

$$z = a + j b = r\,e^{j\varphi} \qquad r = \sqrt{a^{2} + b^{2}} \qquad \varphi = \operatorname{atan2}(b, a) \qquad a = r\cos\varphi \qquad b = r\sin\varphi$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $z$ | the complex number | dimensionless |
| $a$ | real part | dimensionless |
| $b$ | imaginary part | dimensionless |
| $r$ | magnitude, never negative | dimensionless |
| $\varphi$ | angle (argument) | rad |

Holds when: $z$ is a single complex number. The angle is defined for $r > 0$ and is unique up to adding $2\pi$.
Breaks when: you use $\arctan(b/a)$ alone, which cannot tell $(a, b)$ from $(-a, -b)$. Use $\operatorname{atan2}(b, a)$ or place the point in the correct quadrant yourself. The angle of $z = 0$ is undefined.
Source and basis: derived from plotting $a + jb$ as a point and applying right-triangle trigonometry; taught in [Algebra](01-algebra.md) and [Trigonometry](02-trigonometry.md).

Example: $z = 3 + 4j$ has $r = \sqrt{9 + 16} = 5$ and $\varphi = \arctan(4/3) = 0.9273$ rad ($53.13^{\circ}$). Converting back gives $5\cos 0.9273 = 3$ and $5\sin 0.9273 = 4$. The point $-3 - 4j$ has the same magnitude but angle $-2.214$ rad, not $0.9273$ rad.

```verify
a = 3
b = 4
r = sqrt(a**2 + b**2)
expect(b**2, "16")
expect(r, "5")
phi = atan(b / a)
expect(phi, "0.9273")
expect(phi * 180 / pi, "53.13")
expect(r * cos(phi), "3")
expect(r * sin(phi), "4")
expect(atan(4 / 3) - pi, "-2.214")
```

### Euler's formula

**Euler's formula** connects the exponential to sine and cosine. It is why a rotating arrow of length 1 can be written $e^{j\varphi}$.

$$e^{j\varphi} = \cos\varphi + j\sin\varphi \qquad e^{j\pi} = -1 \qquad \left|e^{j\varphi}\right| = 1$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\varphi$ | angle | rad |
| $j$ | the imaginary unit, $j^{2} = -1$ | dimensionless |

Holds when: $\varphi$ is in radians. It holds for every real $\varphi$.
Breaks when: $\varphi$ is entered in degrees. Convert first.
Source and basis: derived from the series expansions of $e^{x}$, $\cos x$, and $\sin x$; the series are in [math/reference-calculus.md](reference-calculus.md) and the sheet [Mathematics reference](reference.md).

Example: $e^{j\pi/2} = \cos(\pi/2) + j\sin(\pi/2) = 0 + j$, so multiplying by $e^{j\pi/2}$ turns a number a quarter turn counterclockwise. At $\varphi = 1$ rad the real part is $0.5403$ and the imaginary part $0.8415$, and $0.5403^{2} + 0.8415^{2} = 1$.

```verify
expect(cos(pi/2) + 0, "0")
expect(sin(pi/2), "1")
expect(cos(1), "0.5403")
expect(sin(1), "0.8415")
expect(cos(1)**2 + sin(1)**2, "1")
```

### Multiplication, division, and the conjugate

In rectangular form, multiply as with brackets and use $j^{2} = -1$. In polar form, multiply the magnitudes and add the angles; divide the magnitudes and subtract the angles. The **complex conjugate** $z^{*}$ flips the sign of the imaginary part, and $z z^{*} = r^{2}$ is real.

$$z_{1} z_{2} = r_{1} r_{2}\, e^{j(\varphi_{1} + \varphi_{2})} \qquad \frac{z_{1}}{z_{2}} = \frac{r_{1}}{r_{2}}\, e^{j(\varphi_{1} - \varphi_{2})} \qquad z^{*} = a - j b \qquad \frac{1}{z} = \frac{z^{*}}{r^{2}}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $z_{1}$, $z_{2}$ | complex numbers, $z_{2} \ne 0$ in the quotient | dimensionless |
| $r_{1}$, $r_{2}$ | their magnitudes | dimensionless |
| $\varphi_{1}$, $\varphi_{2}$ | their angles | rad |
| $z^{*}$ | complex conjugate of $z$ | dimensionless |

Holds when: all quantities are complex numbers and the divisor is not zero.
Breaks when: you add or subtract in polar form (convert to rectangular first) or when the summed angle leaves the range you report (add or subtract $2\pi$ to bring it back).
Source and basis: derived from Euler's formula and the laws of powers. For how a sinusoidal signal becomes a phasor, and for impedance, see [applications/electrical/reference.md](../applications/electrical/reference.md).

Example with $z_{1} = 3 + 4j$ and $z_{2} = 1 + j$ (magnitudes 5 and 1.414, angles 0.9273 rad and 0.7854 rad):

- Product in rectangular form: $(3 + 4j)(1 + j) = 3 + 3j + 4j + 4j^{2} = -1 + 7j$.
- Product in polar form: magnitude $5 \times 1.414 = 7.071$ and angle $0.9273 + 0.7854 = 1.7127$ rad. The rectangular result agrees, since $\sqrt{1 + 49} = 7.071$ and $\pi + \arctan(7/(-1)) = 1.7127$ rad.
- Quotient: multiply top and bottom by the conjugate of $z_{2}$, giving $(3 + 4j)(1 - j)/2 = (7 + j)/2 = 3.5 + 0.5j$. Polar form gives magnitude $5/1.414 = 3.536$ and angle $0.9273 - 0.7854 = 0.1419$ rad.

```verify
a1 = 3
b1 = 4
a2 = 1
b2 = 1
re = a1*a2 - b1*b2
im = a1*b2 + b1*a2
expect(re, "-1")
expect(im, "7")
r1 = sqrt(a1**2 + b1**2)
r2 = sqrt(a2**2 + b2**2)
p1 = atan(b1 / a1)
p2 = atan(b2 / a2)
expect(r2, "1.414")
expect(p1, "0.9273")
expect(p2, "0.7854")
expect(r1 * r2, "7.071")
expect(p1 + p2, "1.7127")
expect(sqrt(re**2 + im**2), "7.071")
check(re**2 + im**2 == 50, "sum of squares")
expect(im**2, "49")
expect(pi + atan(im / re), "1.7127")
qre = (a1*a2 + b1*b2) / (a2**2 + b2**2)
qim = (b1*a2 - a1*b2) / (a2**2 + b2**2)
expect(qre, "3.5")
expect(qim, "0.5")
expect(r1 / r2, "3.536")
expect(p1 - p2, "0.1419")
expect(sqrt(qre**2 + qim**2), "3.536")
expect(atan(qim / qre), "0.1419")
```

## Checklists

Before you trust a calculation:

- Every quantity has a unit, and every unit is in one system (convert once, at the start).
- Brackets enclose every numerator and denominator that is more than one term.
- No division by zero, no logarithm or square root of a number outside its domain.
- Angles are in radians, or the calculator mode matches the angle you typed.
- Rounding was done once, at the end, and the answer shows no more significant figures than the inputs support.
- You solved for the right unknown and put the answer back into the original equation.
- The answer has the right unit and the right size (see the sanity checks).

When rearranging a formula:

1. Write the formula and circle the symbol you want.
2. Undo the operations touching it in reverse order of the order of operations, doing the same to both sides.
3. Check the units of the result with a dimensional check.
4. Substitute a simple test value to confirm the rearranged formula gives back the original.

## Sanity checks

- A square root of a number between 1 and 100 lies between 1 and 10. A square root of a number below 1 is larger than the number.
- Multiplying by a number above 1 makes a result larger; dividing by it makes a result smaller. If your answer moved the wrong way, an operation was inverted.
- $\sin$ and $\cos$ are between $-1$ and $1$. A hypotenuse is longer than either leg.
- The area of a circle is a little over 3 times the square on its radius ($\pi \approx 3.14$), and its circumference a little over 3 times its diameter.
- A percent change from a small base can be huge, and a change of 100 percent is a doubling.
- A log-log slope of 1 is proportional, 2 is squared, and $-1$ is inverse.
- Estimate before you calculate: round each input to one digit, compute in your head, and compare. Estimating is taught in [Estimation](../problem-solving/07-estimation.md).

```verify
given("3.14", "100")
expect(pi, "3.14")
```

## Further reference

- *Prealgebra 2e* (OpenStax), free at [openstax.org](https://openstax.org/details/books/prealgebra-2e), covers arithmetic, fractions, percent, and powers from the start.
- *Algebra and Trigonometry 2e* (OpenStax), free at [openstax.org](https://openstax.org/details/books/algebra-and-trigonometry-2e), covers algebra, logarithms, functions, trigonometry, and complex numbers.
- *Mathematics reference* in this repo, [math/reference.md](reference.md), holds the identities, calculus, linear algebra, and statistics that build on this sheet. Calculus alone is in [math/reference-calculus.md](reference-calculus.md).
- Units and prefixes: [Units](../data/units.md) and [the measurement reference](../measurement/reference.md). The method of checking units is in [Units and dimensional analysis](../measurement/01-units-and-dimensional-analysis.md).
- *Schaum's Outline of Beginning Algebra* and *Schaum's Outline of Trigonometry* are classic worked-problem books, named here by title only.
