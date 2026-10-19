# Scientific revolution and the measurement of time and place

**Type:** lesson

From about 1600 to 1700, scientists began to describe motion, falling bodies, and the heavens with measurements and mathematics. Engineers gained the tools that made those measurements repeatable: the pendulum clock, the balance spring, and the telescope. The longitude problem at sea forced a precise clock to be built, and that clock is still the model for reliable timing.

**Prerequisites:** [Medieval and renaissance engineering](03-medieval-and-renaissance.md), [Trigonometry](../math/02-trigonometry.md), [Vibrations](../physics/13-vibrations.md)
**Time:** 3-4 h

## Core ideas

Before 1600, most natural philosophers reasoned from authorities such as Aristotle and from careful observation without numbers. The change came when several people began to test ideas with measured quantities. Galileo rolled balls down inclined planes to measure how distance depended on time. He observed that a pendulum's swings seemed to take the same time whatever their size, and he used that idea to propose the pendulum as a timer.

Galileo was born in Pisa in 1564. He taught at Padua for many years, and he published his mechanics in *Dialogues Concerning Two New Sciences* in 1638 in Leiden. The book gave the rule that distance fallen from rest grows with the square of time, and it discussed how beams and columns break. These results gave builders a way to predict loads.

Ibn al-Haytham worked in Cairo in the early 1000s. His *Book of Optics* describes light entering the eye and tests the claims of earlier writers with experiments. Song dynasty scholar Shen Kuo recorded in his *Dream Pool Essays* of 1088 the magnetic needle compass, and he described the difference between magnetic north and true north. Both works show the same method that later European scientists used: measure, compare, and revise.

Christiaan Huygens, a Dutch scientist, built the first pendulum clock in 1656 and patented it in 1657. A pendulum swings with a period set by its length and gravity, so it regulates a clock better than a verge escapement with a foliot. Early pendulum clocks kept time to about 15 seconds per day, which was a large improvement over the quarter hour or more per day of earlier clocks. Huygens and Robert Hooke both worked on balance springs in the 1670s, which made small portable watches possible.

Isaac Newton published the *Principia* in 1687 in Latin. It set out three laws of motion and a law of universal gravitation, and it showed that the motion of planets and the fall of objects follow the same rules. Newton's laws became the basis for the mechanics used in every machine described in later lessons.

Measurement also spread to astronomy. Ole Rømer used the timing of eclipses of Jupiter's moon Io to estimate the speed of light in 1676. Accurate timing of events in the sky was a method that also helped navigation.

## Key inventions

| Year | Invention or result | Who and where | Why it mattered |
|------|---------------------|---------------|-----------------|
| About 1602 | Pendulum swings seem to take equal time | Galileo, Padua | Showed a pendulum could regulate time |
| 1088 | Magnetic needle compass with true-north note | Shen Kuo, Song China | Recorded the compass as a measuring tool |
| 1638 | *Two New Sciences* | Galileo, Leiden | Gave rules for falling bodies and beams |
| 1656 | Pendulum clock | Huygens, The Hague | Kept time far more steadily than earlier clocks |
| 1670s | Balance spring for watches | Huygens and Hooke | Made portable timekeepers possible |
| 1676 | Speed of light from Io eclipses | Ole Rømer, Paris | Used precise timing of astronomical events |
| 1687 | *Principia* | Newton, London | Gave the laws of motion and gravitation |
| 1714 | Longitude Act | Parliament of Great Britain | Offered prizes for a practical method at sea |
| 1761 | H4 marine chronometer | John Harrison, England | Kept time on a voyage well enough for longitude |

## Key equations

The period of a simple pendulum for small swings is

$$T = 2\pi \sqrt{\frac{L}{g}}$$

where $T$ is the period in seconds (s), $L$ is the length from pivot to bob centre in metres (m), and $g$ is gravitational acceleration in metres per second squared (m/s$^2$). The standard value is $g = 9.81\ \text{m/s}^2$, but $g$ changes with latitude, from about 9.78 at the equator to about 9.83 at the poles (typical values). A pendulum of fixed length therefore runs slightly differently at different places.

For larger swings, the period grows with amplitude. For a swing of half-angle $\theta_0$ in radians, the period is approximately

$$T \approx T_0 \left(1 + \frac{\theta_0^2}{16}\right)$$

where $T_0$ is the small-swing period from the first equation. This correction is small for swings under a few degrees, which is why clock makers kept the arc small.

Longitude is the angle east or west of a reference meridian. The Earth turns $360^\circ$ in 24 hours, so an offset in local time corresponds to an angle:

$$\Delta\lambda = 15^\circ \times \Delta t_{\text{h}}$$

where $\Delta t_{\text{h}}$ is the time difference in hours. One degree of longitude equals 4 minutes of time.

## Worked example

**Given:** A pendulum clock uses a bob on a rod of length $L = 0.994\ \text{m}$ at a place on Earth where $g = 9.81\ \text{m/s}^2$. The clock swings with a half-angle of $\theta_0 = 3^\circ$.

**Find:** (a) the small-swing period, (b) the extra time lost per day from the amplitude correction, and (c) why a pendulum clock improved timekeeping.

**Solution:**

1. Small-swing period: $T_0 = 2\pi \sqrt{0.994 / 9.81} = 2.00\ \text{s}$. Each full cycle lasts 2.00 seconds, so the clock ticks once per second with each half swing.
2. Amplitude correction: $\theta_0 = 3^\circ = 0.0524\ \text{rad}$, so $\theta_0^2 / 16 = 0.000171$. The period is $T = 2.00 \times 1.000171$, which is larger by $0.000171$. Over one day of $86\,400\ \text{s}$, the clock runs slow by $86\,400 \times 0.000171 = 14.8\ \text{s}$.
3. Why it improved timekeeping: the period depends only on length and gravity, and it does not depend on the force that drives the clock. A verge and foliot clock swings faster or slower as the driving weight or friction changes. A pendulum holds its period through those changes, so the error comes down to a few seconds per day at small arcs.

**Answer:** The period is 2.00 s. At a 3 degree swing, the clock runs about 15 seconds per day slow.

**Sanity check:** A 1 m pendulum has a period of 2.006 s, so the 0.994 m rod gives a slightly shorter period of 2.000 s, as expected. The 15 seconds per day is about 0.017 percent, which is small compared with the errors of earlier mechanical clocks.

### Longitude from a drifting clock

A navigator needs to know the local time at a known reference place. At sea, the navigator compares local noon, found by the Sun, with the time on a clock set to the home port.

**Given:** A clock set to the home port drifts by $3\ \text{s}$ per day. The ship sails for 30 days before the navigator checks the clock again.

**Find:** the longitude error in degrees and in kilometres at the equator.

**Solution:**

1. Total time error: $3\ \text{s} \times 30 = 90\ \text{s}$.
2. Angle: $\Delta\lambda = 15^\circ/\text{h} \times (90 / 3600)\ \text{h} = 0.375^\circ$.
3. Distance at the equator: one degree of longitude is about $111.32\ \text{km}$, so $0.375 \times 111.32 = 41.7\ \text{km}$.

**Answer:** A drift of 3 s per day gives a position error of about $0.375^\circ$, or about 42 km at the equator, after 30 days.

**Sanity check:** Near the equator, 90 s of time error means 90 s of rotation, which is $90/240 = 0.375$ degrees, since one degree equals 4 minutes. The arithmetic agrees.

## Design trade-offs

A clock designer balanced the period, the accuracy, and the sensitivity to the environment. A long pendulum has a slower, steadier swing, but it is tall and easily disturbed by a moving ship. A short pendulum fits in a case, but it swings faster and the escapement wears more quickly.

Marine chronometers balanced accuracy against heat, motion, and the sea. Harrison's H4 used a bimetallic strip to correct for temperature changes in the balance spring, and it used a balance instead of a pendulum, so a ship's motion disturbed it less. Designers traded bulk and cost for stability at sea.

Instrument makers balanced precision against the cost of skilled labour. A telescope lens or a clock escapement needed a fine finish, and only a few workshops could make them well. The reward for solving the longitude problem reflected that cost.

## How it fails

A pendulum clock fails when the length changes with temperature, which causes the period to drift. Early clocks used brass rods, and the brass expanded in summer and contracted in winter. Later clocks used invar or a compensated pendulum. A pendulum also fails when the arc grows, since the period then depends on amplitude, as the worked example shows.

Marine clocks failed when the balance spring lost its springiness in cold, or when a ship's motion disturbed the escapement. Harrison's earlier clocks, H1 to H3, were large and heavy. The Board of Longitude tested H4 on a long sea voyage before it judged the prize.

Clock errors also fail a navigator silently. A clock that drifts 3 s per day can put a ship 40 km off course after a month, and the navigator may not notice until land appears in the wrong place. Navigators cross-checked the clock against celestial observations.

## History

Galileo's work in Padua and Pisa set the pattern for measurement-based physics. Huygens built the first pendulum clock in 1656 and published on the pendulum in the years after. Newton's *Principia* in 1687 gave the laws that later engineers used to design machines. The longitude problem drew in clockmakers, astronomers, and governments: the British Parliament passed the Longitude Act in 1714, and John Harrison built the H4 chronometer that won a large part of the prize. Earlier work in Islamic optics and astronomy, and in Song China's instruments, used many of the same methods of measurement.

## Practice

1. A pendulum has length $L = 0.25\ \text{m}$. Find its small-swing period in seconds. Use $g = 9.81\ \text{m/s}^2$ (Earth surface).
2. If the length of a pendulum is multiplied by 4, what happens to the period?
3. A ship's clock drifts 5 s per day. After 20 days, find the longitude error in degrees and in kilometres at the equator.
4. Explain why a pendulum clock keeps its arc to a few degrees, using the amplitude correction.

<details><summary>Answers</summary>

1. $T = 2\pi \sqrt{0.25 / 9.81} = 1.00\ \text{s}$.
2. The period doubles, because $T$ is proportional to the square root of $L$, and $\sqrt{4} = 2$.
3. Time error: $5 \times 20 = 100\ \text{s}$. Angle: $100 \times 15 / 3600 = 0.42^\circ$. Distance: $0.42 \times 111.32 = 46\ \text{km}$.
4. The period grows with the square of the swing angle. At 3 degrees the extra period loses about 15 s per day. At 2 degrees the loss is about 7 s per day, so a smaller arc keeps the error lower.

</details>

## Common mistakes

- **Myth: Galileo invented the pendulum clock.** Galileo noticed the constant period of a pendulum and proposed a clock. Huygens built the first working pendulum clock in 1656.
- **Mistake: using Earth's $g = 9.81\ \text{m/s}^2$ everywhere.** Gravity varies with latitude by about half a percent. A precise clock must be calibrated at its location.
- **Mistake: treating a clock error as a time error only.** A clock error in time becomes a position error at sea, at 15 degrees per hour of longitude.
- **Mistake: assuming Newton worked alone.** The *Principia* built on Kepler, Galileo, Huygens, Hooke, and others, and Newton's debts to them are well documented.
- **Mistake: assuming the pendulum period depends on the mass of the bob.** For an ideal simple pendulum, the period depends only on length and $g$.

## Go deeper

- [NIST Time and Frequency Division](https://www.nist.gov/pml/time-and-frequency-division). The U.S. standards laboratory for time, which defines and keeps the second.
- [MIT OpenCourseWare](https://ocw.mit.edu/). Free lecture notes on classical mechanics, including the pendulum and gravitation.
- [Library of Congress](https://www.loc.gov/). Digitized historical books and prints on clocks, astronomy, and navigation.

Related lessons: [Medieval and renaissance engineering](03-medieval-and-renaissance.md), [Scientific revolution people](people/03-scientists-and-mathematicians.md), [Clocks and watches](../applications/everyday/07-clocks-and-watches.md), [Industrial revolution](05-industrial-revolution.md), [Mathematics folder](../math/README.md).
- [History of engineering reference](reference.md): the lookup sheet for this topic.
