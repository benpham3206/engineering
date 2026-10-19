# Renaissance polymaths

**Type:** lesson

Renaissance polymaths are the Europeans of the 1400s and 1500s who joined mathematics, art, mining, and mechanics into single careers. Engineers today should know them because their work on domes, machines, mining, and the testing of motion and strength still shows up in engineering methods. This lesson profiles five people from that period and shows where their work is found today.

**Prerequisites:** [Ancient and medieval minds](01-ancient-and-medieval-minds.md), [Simple machines](../01-simple-machines.md), [Statics](../../physics/01-statics.md), [Hydrostatics and Bernoulli](../../physics/10-hydrostatics-and-bernoulli.md), [Particle dynamics](../../physics/02-particle-dynamics.md)
**Time:** 6-8 h

## Core ideas

The profiles run in rough time order. Each one gives when and where the person lived, what they built or discovered, and why it still matters.

### Filippo Brunelleschi, 1377 to 1446, Florence, Italy

Brunelleschi was a goldsmith and architect in Florence. Between 1420 and 1436 he built the dome of the Florence Cathedral, Santa Maria del Fiore. The dome has two shells with a space between them, and its brickwork follows a herringbone pattern that locks the courses together. He raised the dome without a full wooden frame under it, which had never been done at that size. Structural engineers still study the dome as an example of a self-supporting masonry shell.

### Leonardo da Vinci, 1452 to 1519, Vinci, Milan, Florence, Rome, and France

Leonardo was a painter, engineer, and anatomist. He worked for patrons in Milan, Florence, and Rome, and he spent his last years in France. His notebooks contain studies of pulleys, gears, screw pumps, bridges, canals, and flying machines, many of them drawn with careful dimensions. Most of his machines were never built in his lifetime. His drawings still teach how to show a mechanism clearly, and his notebooks record the habit of testing ideas on paper before building them.

### Georgius Agricola, 1494 to 1555, Glauchau, Saxony

Agricola was a German physician and scholar who studied mining. His *De re metallica*, published in 1556 after his death, describes how miners find ore, sink shafts, pump water, ventilate tunnels, and smelt metals. The book includes careful woodcut illustrations of pumps, hoists, crushing stamps, and furnaces. It remained a standard reference on mining for generations.

### Simon Stevin, 1548 to 1620, Bruges and The Hague

Stevin was a Flemish mathematician and engineer who worked for the Dutch Republic. In 1585 he published a booklet that explained decimal fractions, which made calculation with numbers less than one as simple as whole numbers. In 1586 he published work on statics that includes the inclined plane. He also studied hydrostatics, and he showed that the pressure at the bottom of a vessel depends on depth, not on the shape of the vessel. Modern engineers use decimal arithmetic for every calculation, and hydrostatic pressure governs the design of dams and tanks.

### Galileo Galilei, 1564 to 1642, Pisa, Padua, and Florence

Galileo taught mathematics at Pisa and Padua before moving to Florence. In 1609 and 1610 he used a telescope to observe the moons of Jupiter and the phases of Venus. In his *Two New Sciences*, published in 1638, he showed that the distance an object falls from rest grows with the square of time, and he studied the strength of beams. He used inclined planes to slow falling motion so that he could measure it with the timing tools of his day. His work set the pattern of testing a claim against measurement, which every engineering test still follows.

## Key inventions

| Year | Person | Contribution | Where it lives today |
|---|---|---|---|
| 1420 to 1436 | Brunelleschi | Double-shell dome of the Florence Cathedral | Florence Cathedral, Florence, Italy |
| 1478 to 1519 | Leonardo da Vinci | Notebooks of machines, pumps, bridges, and flying devices | Codex Atlanticus in Milan; other notebooks in libraries worldwide |
| 1556 | Agricola | *De re metallica*, the standard mining handbook | Copies in university and national libraries |
| 1585 | Stevin | Decimal fractions booklet | Decimal arithmetic in every calculator and spreadsheet |
| 1586 | Stevin | Statics, including the inclined plane | Standard statics texts |
| 1609 to 1610 | Galileo | Telescope observations of Jupiter's moons and Venus | Museo Galileo, Florence, holds his instruments |
| 1638 | Galileo | *Two New Sciences*, falling bodies and beam strength | Copies in libraries; the basis of modern strength of materials |

## Key equations

Stevin's inclined plane describes a load held on a frictionless slope by a force that pulls along the slope. The force needed is the weight times the ratio of height to length:

$$F = W \sin\theta = W \frac{h}{L}$$

where $F$ is the force along the slope in newtons (N), $W$ is the load's weight in N, $h$ is the height the slope rises in metres (m), $L$ is the slope's length in m, and $\theta$ is the angle of the slope. Friction makes the real force larger.

Galileo's law of falling bodies describes motion from rest with uniform acceleration. Near Earth's surface the distance fallen in time $t$ is:

$$d = \tfrac{1}{2} g t^2$$

where $d$ is the distance in metres (m), $t$ is the time in seconds (s), and $g$ is the local gravitational acceleration (9.81 m/s$^2$ at Earth's surface).

## Worked example

### Given

A 600 N crate sits on a frictionless ramp 4.0 m long. The top of the ramp is 1.2 m above the bottom.

### Find

The force needed to hold the crate on the ramp, the mechanical advantage, and the slope angle.

### Assumptions

The ramp is frictionless. The pull is parallel to the slope. The crate is treated as a point at its centre of mass.

### Solution

Use Stevin's relation with $W = 600\ \text{N}$, $h = 1.2\ \text{m}$, and $L = 4.0\ \text{m}$:

$$F = W \frac{h}{L} = 600 \times \frac{1.2}{4.0} = 180\ \text{N}$$

The mechanical advantage is the load divided by the force:

$$\mathrm{MA} = \frac{W}{F} = \frac{600}{180} = 3.33$$

The angle of the slope is:

$$\theta = \sin^{-1}\left(\frac{h}{L}\right) = \sin^{-1}(0.300) = 17.5^\circ$$

### Answer

The force needed is 180 N. The mechanical advantage is 3.33. The slope angle is 17.5 degrees.

### Sanity check

The force is less than the crate's weight, as a ramp should give. Friction on a real ramp adds force, so the real pull will be more than 180 N. Halving the ramp length to 2.0 m would double the force to 360 N.

## Lessons for engineers today

These five people show three habits that still matter. Brunelleschi built a dome that carries its own load, using a two-shell structure and a brick pattern that locks the courses together. Leonardo and Agricola drew mechanisms with dimensions, so that others could build from the drawings. Stevin and Galileo tied claims to numbers, so a result could be checked by anyone with the same measurements. A clear drawing, a stated assumption, and a measured number are still the basis of an engineering record.

## Practice

1. Calculation. A 800 N load sits on a frictionless ramp 5.0 m long that rises 1.5 m. Find the force needed to hold it, using Stevin's relation.

2. Calculation. Find the gauge pressure at 10 m depth in fresh water, in kilopascals. Then add standard atmospheric pressure of 101.3 kPa to find the absolute pressure. Use $g = 9.81\ \text{m/s}^2$ (Earth surface).

3. Calculation. A stone is dropped from rest from a height of 20 m. Using $d = \tfrac{1}{2} g t^2$, find the time to fall. Use Earth's surface $g$, $9.81\ \text{m/s}^2$.

4. Short answer. Stevin showed that pressure at the bottom of a vessel depends on depth, not on vessel shape. Explain why this matters for the design of a dam.

5. Short answer. Galileo used inclined planes to study falling motion. Explain why slowing the motion helped him measure it.

<details>
<summary>Answers</summary>

1. $F = 800 \times 1.5 / 5.0 = 240\ \text{N}$.

2. $p = \rho g h = 1000 \times 9.81 \times 10 = 98\ 100\ \text{Pa} = 98.1\ \text{kPa}$. Absolute pressure is $98.1 + 101.3 = 199.4\ \text{kPa}$.

3. $t = \sqrt{2d/g} = \sqrt{2 \times 20 / 9.81} = 2.02\ \text{s}$.

4. A dam's wall must resist the force from water pressing on it. That force grows with depth, so the wall must be thicker at the bottom. The shape of the reservoir above the wall does not change the force on the wall.

5. A ball on a slope accelerates more slowly than a ball in free fall. Its travel takes longer, so the timing methods of his day could measure it. A ball in free fall falls too quickly to time with those tools.

</details>

## Common mistakes

- The Leaning Tower of Pisa story says Galileo dropped weights from the tower to test falling bodies. The story comes from a biography written after his death, and historians doubt it.
- Brunelleschi did not invent the dome. Domes existed for more than a thousand years before him. His contribution was the method he used to build this one.
- Leonardo's notebooks contain many working ideas, but most of his machines were never built during his lifetime. Drawing a machine does not prove it works.
- Stevin did not invent the modern decimal point. He wrote digits with index marks, and the dot notation came later.
- Galileo did not prove the Earth moves around the Sun. His telescope observations supported that view, and his trial in 1633 ended with house arrest.

## Go deeper

- [MacTutor biography of Galileo](https://mathshistory.st-andrews.ac.uk/Biographies/Galileo/), University of St Andrews
- [MacTutor biography of Simon Stevin](https://mathshistory.st-andrews.ac.uk/Biographies/Stevin/), University of St Andrews
- Related lessons: [Ancient and medieval minds](01-ancient-and-medieval-minds.md), [Medieval and Renaissance](../03-medieval-and-renaissance.md), [Scientific revolution](../04-scientific-revolution.md), [Statics](../../physics/01-statics.md), [Hydrostatics and Bernoulli](../../physics/10-hydrostatics-and-bernoulli.md), [Algebra](../../math/01-algebra.md)
- [People of engineering reference](../reference-people.md): the lookup sheet for this topic.
