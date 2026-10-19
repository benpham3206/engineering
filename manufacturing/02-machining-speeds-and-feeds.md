# Machining speeds and feeds

**Type:** lesson

Speeds and feeds are the cutting settings that decide how fast a tool turns, how fast it moves into the material, and how much material it removes in a given time. A machinist must set them correctly because wrong values break tools and make parts that miss their size. Machining removes material from a block of stock with a cutting tool, so you can shape it into a part. Three numbers control how fast that happens: spindle speed (how fast the tool or part turns), feed rate (how fast the tool moves into the material), and material removal rate (how much material comes out per minute).

**Prerequisites:** [Shop safety](01-shop-safety.md), [Algebra](../math/01-algebra.md)
**Time:** 6-8 h

## Core ideas

- **Surface speed (cutting speed)**: how fast the cutting edge moves past the work, measured at the outside of the tool or part. Common units are surface feet per minute (SFM, ft/min) in the US and meters per minute (m/min) in SI.
- **Spindle speed (RPM)**: revolutions per minute of the tool or workpiece. Surface speed and diameter set RPM. A small tool must spin faster than a large one to reach the same surface speed.
- **Feed per tooth ($f_z$)**: how far the tool advances per tooth per revolution, in inches per tooth (ipt) or millimeters per tooth (mm/tooth). Large feed per tooth cuts faster but loads each tooth harder.
- **Feed rate ($f_m$)**: how fast the table or tool moves, in inches per minute (ipm) or mm/min. It is the feed per tooth times the number of teeth (flutes) times RPM.
- **Depth of cut ($a_p$)**: how far the tool goes into the material, in the direction of the tool axis.
- **Width of cut ($a_e$)**: how far the tool reaches across the material, sideways.
- **Material removal rate (MRR)**: the volume of metal removed per minute. For milling it is depth times width times feed rate.

Speeds depend on the material, the tool coating and material, the machine's power and rigidity, and whether you use coolant. Tool makers publish starting values for each tool. Treat those as the starting point and adjust from there while you watch chips and sound.

You are running too fast when the tool turns blue or glows, the edge chips quickly, and the surface finish gets worse. You are running too slow when the chips are thin and powdery, the tool rubs instead of cutting, and heat built up by rubbing wears the tool.

## Key equations

Units: $N$ is spindle speed in rev/min (rpm). $V$ is surface speed in ft/min (SFM) for US form or m/min for SI form. $D$ is tool or workpiece diameter in inches (US) or millimeters (SI).

US customary:

$$N = \frac{3.82\,V}{D}$$

SI:

$$N = \frac{1000\,V}{\pi D}$$

Feed rate, where $f_m$ is feed rate (ipm or mm/min), $f_z$ is feed per tooth (ipt or mm/tooth), $z$ is the number of teeth (flutes), and $N$ is spindle speed (rpm):

$$f_m = f_z \, z \, N$$

Material removal rate for milling, where $a_p$ is depth of cut, $a_e$ is width of cut, and $f_m$ is feed rate (same units as the length units above):

$$\text{MRR} = a_p \, a_e \, f_m$$

The factor 3.82 comes from $12/\pi \approx 3.82$, which converts surface feet per minute and inches into revolutions per minute.

## Worked example

**Given:** A $1/2$ in (0.5 in) diameter, 4-flute end mill cutting a steel block at $V = 300$ SFM. Feed is $f_z = 0.002$ in/tooth. Depth $a_p = 0.25$ in, width $a_e = 0.5$ in (full slot).

**Find:** Spindle speed $N$, feed rate $f_m$, and MRR.

**Assumptions:** The machine can deliver these speeds and feeds, and the tool is rated for them.

**Solution:**

1. Spindle speed:
$$N = \frac{3.82 \times 300}{0.5} = 2292 \text{ rpm}$$
2. Feed rate:
$$f_m = 0.002 \times 4 \times 2292 = 18.34 \text{ ipm}$$
3. Material removal rate:
$$\text{MRR} = 0.25 \times 0.5 \times 18.34 = 2.29 \text{ in}^3/\text{min}$$

**Answer:** $N \approx 2290$ rpm (about 2292 rpm), $f_m \approx 18.3$ ipm, MRR $\approx 2.29$ in$^3$/min.

**Sanity check:** Put the same numbers into SI. Convert $V = 300$ SFM to about $91.4$ m/min and $D = 0.5$ in to $12.7$ mm. Then $N = 1000 \times 91.4 / (\pi \times 12.7) \approx 2292$ rpm, which matches.

**SI version of the same idea:** A 12 mm, 4-flute end mill at $V = 90$ m/min with $f_z = 0.1$ mm/tooth gives $N = 1000 \times 90 / (\pi \times 12) \approx 2387$ rpm and $f_m = 0.1 \times 4 \times 2387 \approx 955$ mm/min.

## Practice

1. A $1/2$ in end mill runs at $V = 400$ SFM. What is the spindle speed in rpm?
2. A 10 mm drill runs at $V = 25$ m/min. What is the spindle speed in rpm? Give one decimal place.
3. A 4-flute cutter has $f_z = 0.003$ in/tooth and runs at 2000 rpm. What is the feed rate in ipm?
4. A milling pass has $a_p = 0.2$ in, $a_e = 0.4$ in, and $f_m = 20$ ipm. What is the MRR in in$^3$/min?
5. A $1/4$ in drill is run at 100 SFM. What is the spindle speed in rpm? Round to the nearest whole rpm.

<details><summary>Answers</summary>

1. 3056 rpm
2. 795.8 rpm
3. 24.0 ipm
4. 1.6 in$^3$/min
5. 1528 rpm

</details>

## Common mistakes

- Mixing units. Using a diameter in mm with the US form of the equation gives an answer that is wildly wrong. Check units before you calculate.
- Using the radius instead of the diameter. The equation needs the full diameter.
- Forgetting the number of flutes. Feed per tooth tells you how much each tooth takes, so feed rate depends on tooth count.
- Setting feed rate from RPM alone and ignoring depth and width. MRR and tool load depend on all three cutting parameters.
- Treating a chart value as a rule. Charts give starting points. Adjust by sound, chip shape, and finish.

## Go deeper

- [Paul's Online Math Notes: Algebra](https://tutorial.math.lamar.edu/classes/alg/alg.aspx) by Paul Dawkins, Lamar University: solving equations and rearranging formulas, which you need to move between US and SI.
- [OpenStax University Physics Volume 1, Chapter 1](https://openstax.org/books/university-physics-volume-1/pages/1-introduction) by OpenStax (Rice University): units, unit conversion, and the habit of checking dimensions.
- [NIST: SI units](https://www.nist.gov/pml/weights-and-measures/si-units) by NIST: the official SI base units and how they are used, including the meter and millimeter.
- [Manufacturing reference](reference.md): the lookup sheet for this topic.
