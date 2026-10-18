# Python for engineering calculations

**Type:** lesson

Python is a free programming language. Engineers use it to repeat calculations, check hand work, fit data, and build small tools. You need almost no software to start: Python and a text editor or Jupyter notebook.

**Prerequisites:** [Algebra and functions](../math/README.md)
**Time:** 10-15 h to become comfortable with the basics used here

## Core ideas

- A **variable** is a name that stores a value, such as `F = 5000.0`.
- A **float** is a number with a decimal point. Use floats for physical quantities.
- A **function** takes inputs and returns a result. You write one when you repeat a formula.
- A **list** holds several values in order. A **loop** runs the same code for each item.
- A **library** adds tools. NumPy gives fast arrays and linear algebra. SciPy adds solvers and numerical methods. Matplotlib makes plots.
- Keep units in your variable names or in comments. Python will not stop you from mixing millimeters and meters.

Free tools you need:

- Python 3 from [python.org](https://www.python.org/) or your operating system.
- Jupyter Lab for notebooks. The install steps are on [jupyter.org/install](https://jupyter.org/install).
- NumPy and SciPy with `pip install numpy scipy`. Matplotlib with `pip install matplotlib` if you want plots.

Read the [Python Tutorial](https://docs.python.org/3/tutorial/index.html) for the language basics. Read the [NumPy quickstart](https://numpy.org/doc/stable/user/quickstart.html) for arrays.

## Key equations

Simply supported beam with a center point load $F$ (N), span $L$ (m), modulus $E$ (Pa), and second moment of area $I$ (m$^4$):

$$\delta = \frac{F L^3}{48\,E\,I}$$

For a rectangle of width $b$ and height $h$ (both m):

$$I = \frac{b h^3}{12}$$

## Worked example

**Given:** A 2.0 m steel beam, 50 mm wide by 100 mm tall, carries a 5 kN load at mid-span. Take $E = 200$ GPa (typical steel).

**Find:** The mid-span deflection $\delta$.

**Assumptions:** Simply supported, linear elastic, small deflection, no self-weight.

**Solution (run in Python):**

```python
F = 5000.0            # N
L = 2.0               # m
b, h = 0.050, 0.100   # m
E = 200e9             # Pa, typical steel
I = b * h**3 / 12
delta = F * L**3 / (48 * E * I)
print("I =", I, "m^4")
print("delta =", delta, "m =", delta * 1000, "mm")
```

Output:

```
I = 4.166666666666668e-06 m^4
delta = 0.0009999999999999998 m = 0.9999999999999998 mm
```

**Answer:** $\delta \approx 1.0$ mm.

**Sanity check:** The beam is 2 m long, and a 1 mm sag is 1/2000 of the span. That is a plausible service deflection for a stiff steel beam. The span-to-depth ratio is 20, which is a common rule-of-thumb proportion.

## Practice

1. Change the load to 3000 N and rerun the calculation. What is the new $\delta$ in mm?
2. Compute the second moment of area for a 30 mm wide by 60 mm tall section. Give the answer in m$^4$.
3. Write a function `deflection(F, L, E, I)` that returns $\delta$. Test it with the worked example.
4. Use a list of three loads (2, 4, 6 kN) and print the deflection for each.
5. Convert your final answer to inches. Use 1 in = 25.4 mm.

<details><summary>Answers</summary>

1. 0.25 mm
2. 5.4 x 10$^{-7}$ m$^4$ (5.4e-07)
3. Check: 1.0 mm at 5000 N.
4. Check: 0.4, 0.8, 1.2 mm.
5. 0.039 in

</details>

## Common mistakes

- Mixing millimeters and meters in one formula. Convert every input to SI before you calculate.
- Using integer division by accident. Write `10.0` instead of `10` when the result needs decimals.
- Copying a formula without checking its units. Print the units with the number.
- Trusting a result without a sanity check, such as an order-of-magnitude estimate.
- Keeping code in a cell or file you cannot rerun. Save the script or notebook.

## Go deeper

- [The Python Tutorial](https://docs.python.org/3/tutorial/index.html) by the Python Software Foundation: free official language guide.
- [NumPy quickstart](https://numpy.org/doc/stable/user/quickstart.html) by the NumPy project: arrays and vector math.
- [SciPy User Guide](https://docs.scipy.org/doc/scipy/tutorial/index.html) by the SciPy project: solvers, integration, and statistics.
- [MIT 6.0001 Introduction to Computer Science and Programming in Python](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/) by MIT OpenCourseWare: a free full course.
- Related: [GNU Octave and MATLAB](04-matlab.md), [spreadsheets](03-spreadsheets.md), [starter kit](01-starter-kit.md).
