# Measuring existing parts

**Type:** lesson

Measuring an existing part is the job of recording its real dimensions with calipers, micrometers, and other tools. It matters because every rebuild starts from these numbers, and an error in one measurement carries into every part made from it.

Parts that have been used are worn, so a measurement shows the current size, not the size the designer intended. Good reverse engineering means choosing the right tool, reading it correctly, and working backward from the measured size to the likely nominal (intended) size and to a standard fastener or thread where one fits.

**Prerequisites:** [Teardowns](01-teardowns.md), [Trigonometry](../math/02-trigonometry.md), [Reading calipers and micrometers](../measurement/04-reading-calipers-and-micrometers.md)
**Time:** 6-10 h

## Core ideas

- **Nominal size** is the size the designer intended, for example 110 mm. **Actual size** is what you measure. The gap between them comes from manufacturing tolerance and wear.
- **Resolution** is the smallest step a tool can show. **Accuracy** is how close the reading is to the true size. A tool can have fine resolution and still be inaccurate if it is out of calibration.
- Common tools and their typical resolution:
  - Vernier or digital caliper: outside, inside, and depth reading, usually to 0.01 mm (0.0005 in).
  - Outside micrometer: a precise diameter or thickness reading, usually to 0.01 mm (0.0001 in).
  - Thread pitch gauge: a set of blades, each marked with a pitch. You match the blade to the thread teeth.
  - Steel rule: useful for lengths, but limited to about 0.5 mm reliable reading.
- Use two measurements for anything that matters. Measure the same feature twice from different directions, and check that the two readings agree.
- Measure in both units if the part could be metric or inch. A reading of 3.25 in is 82.55 mm ($1\ \text{in} = 25.4\ \text{mm}$ exactly).
- **Wear** shows up as a loss of material on surfaces that rub, such as bearing bores, gear teeth, and threads. Measure the worn surface, then find a surface that was not in contact, such as a shoulder or a hidden face, to estimate the original size.
- **Bolt circle diameter (BCD)** is the diameter of an imaginary circle that passes through the centers of a ring of holes. You cannot measure it directly across the middle, so you measure the distance between two adjacent holes and calculate it.
- **Thread pitch** is the distance from one thread crest to the next. You can measure it by counting turns over a known length.

### Thumb rules for nominal sizes

- Standard fasteners come in sizes you can match against a table. A measured thread diameter of 7.9 mm likely means an M8 thread that has worn a little, not a 7.9 mm design.
- Round numbers are common in design: 25, 30, 50, 100, 110 mm. If a measurement lands within a fraction of a millimeter of one of these, check it as the nominal size first.
- A measured size that fits a standard value like $1/4$ in or M6 is a strong clue. Test that idea before you accept it.

## Key equations

Chord between adjacent holes on a bolt circle, where $c$ is the straight-line distance between two adjacent hole centers in millimeters, $R$ is the bolt circle radius in millimeters, and $n$ is the number of holes:

$$c = 2R\sin\left(\frac{180^\circ}{n}\right)$$

Solving for the bolt circle diameter $D = 2R$ in millimeters:

$$D = \frac{c}{\sin\left(\frac{180^\circ}{n}\right)}$$

Thread pitch from turn counting, where $p$ is the pitch in millimeters, $L$ is the length counted in millimeters, and $N$ is the number of thread crests (or turns) counted over that length:

$$p = \frac{L}{N}$$

Unit conversion, where $x_{\text{mm}}$ is millimeters and $x_{\text{in}}$ is inches:

$$x_{\text{mm}} = 25.4\, x_{\text{in}}$$

## Worked example

**Given:** A five-arm bicycle crank spider has five bolt holes. You measure the straight distance between two adjacent hole centers with a caliper, and it reads $c = 64.7$ mm. You count 8 thread turns over a length of 10.0 mm on a bolt from the same crank.

**Find:** (a) the bolt circle diameter $D$, (b) the thread pitch $p$, and (c) the likely standard for each.

**Assumptions:** The holes are evenly spaced on one circle. The caliper is accurate to about 0.05 mm. The thread is not badly worn.

**Solution:**

(a) For $n = 5$, $180^\circ / 5 = 36^\circ$, and $\sin 36^\circ = 0.587785$.

$$D = \frac{64.7}{0.587785} = 110.07 \text{ mm}$$

(b) Pitch from turn counting:

$$p = \frac{10.0}{8} = 1.25 \text{ mm}$$

(c) A 110 mm bolt circle is a common five-arm crank size. A 1.25 mm pitch matches the coarse pitch of an M8 thread ($\mathrm{M8} \times 1.25$).

**Answer:** The bolt circle diameter is about 110 mm, and the thread is most likely $\mathrm{M8} \times 1.25$.

**Sanity check:** At radius 55 mm, the chord should be $2 \times 55 \times 0.587785 = 64.66$ mm, which matches the reading to within 0.05 mm, the caliper accuracy.

## Practice

1. Convert 3.25 in to millimeters.
2. A ring of 5 holes has an adjacent-hole chord of 64.66 mm. What is the bolt circle diameter in millimeters, rounded to 0.01 mm?
3. A thread shows 14 crests over 17.5 mm. What is the pitch in millimeters?
4. A ring of 6 holes has an adjacent-hole chord of 55.00 mm. What is the bolt circle diameter in millimeters?
5. A caliper reads 25.38 mm on a bar whose nominal size is 25.40 mm. What is the difference in millimeters, sign included as actual minus nominal?

<details><summary>Answers</summary>

1. 82.55
2. 110.00
3. 1.25
4. 110.00
5. -0.02

</details>

## Common mistakes

- Measuring across the middle of a bolt circle instead of between adjacent holes, which gives the wrong number.
- Using the worn bearing surface as the nominal size. Find an unworn reference surface first.
- Assuming a number is a standard size without testing it against a table or a pitch gauge.
- Forgetting to check whether the part is metric or inch before converting. A 1/4-20 thread has a pitch of about 1.27 mm, not 1.25 mm.
- Reading a steel rule to 0.1 mm and reporting it as precise. Match the stated precision to the tool.

## Go deeper

- [*University Physics Volume 1*, Chapter 1: Introduction](https://openstax.org/books/university-physics-volume-1/pages/1-introduction) by OpenStax: covers units, standards, unit conversion, and significant figures.
- [SI units and the metric system](https://www.nist.gov/pml/owm/metric-si) by NIST: the official U.S. government guide to SI units and the seven base units.
- [*e-Handbook of Statistical Methods*, Measurement Process Characterization](https://www.itl.nist.gov/div898/handbook/mpc/mpc.htm) by NIST and SEMATECH: explains measurement error, bias, and variation.
- [Mechanical Engineering bookshelf](https://eng.libretexts.org/Bookshelves/Mechanical_Engineering) by LibreTexts: a free starting point for tolerances and machine elements.
- [Reverse-engineering reference](reference.md): the lookup sheet for this topic.
