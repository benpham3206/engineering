# Semiconductors and computing

**Type:** lesson

Between 1904 and the early 1970s, engineers replaced hot, power-hungry vacuum tubes with the transistor, and then with the integrated circuit, which put many switches on one small chip. Every computer, phone, and controller in use today rests on that shrinking switch, and the scaling trend that followed still sets what engineers can build.

**Prerequisites:** [The electrical age](06-electrical-age.md), [Diodes and transistors](../applications/electronics/03-semiconductors-diodes-and-transistors.md), [Digital logic and computers](../applications/electronics/07-digital-logic-and-computers.md)
**Time:** 3-4 h

## Core ideas

### Vacuum tubes

A vacuum tube is a sealed glass envelope with the air pumped out. A heated filament releases electrons, and a voltage on a control grid sets how many electrons reach the plate. In 1904, John Ambrose Fleming in London built a two-electrode tube that rectified radio signals. In 1906, Lee de Forest added a third electrode, the grid, and the triode could amplify a signal. Radios, telephones, and early radar all depended on tubes.

Tubes set a hard limit on computing. Each tube needed power to heat its filament, ran hot, and wore out after a few thousand hours. ENIAC, completed in 1945 at the University of Pennsylvania, used about 17,000 tubes. With that many parts, failures were frequent, and the machine needed constant attention. Engineers needed a smaller, cooler, and more reliable switch.

### The transistor

At Bell Labs in Murray Hill, New Jersey, John Bardeen and Walter Brattain built the first working point-contact transistor in December 1947. A small signal applied to one contact controlled a larger current between two others, and no hot filament was needed. William Shockley described the junction transistor in 1948, and that design became the standard for manufacturing. Bardeen, Brattain, and Shockley shared the 1956 Nobel Prize in Physics.

The transistor works because of how silicon conducts. Pure silicon is a poor conductor. Adding a few atoms of phosphorus gives extra free electrons, which is called n-type material. Adding a few atoms of boron leaves gaps called holes, which is called p-type material. A junction between p-type and n-type material lets current flow in one direction and block it in the other. A third terminal then controls the flow, so the device works as an amplifier or a switch.

### The integrated circuit

Building many separate transistors and wiring them by hand limited both size and reliability. In 1958, Jack Kilby at Texas Instruments built a circuit with transistors and other components on one piece of germanium. In 1959, Robert Noyce at Fairchild Semiconductor in California built a version on silicon. Noyce's version used the planar process, in which photolithography patterns the wiring and components on a flat surface. Because the process could make many devices at once, it became the basis of nearly all later chips. Kilby shared the 2000 Nobel Prize in Physics for his part in the invention.

### The microprocessor

In 1971, Intel released the 4004, a 4-bit processor on one chip with about 2,300 transistors, made with a 10 micrometre process. Federico Faggin, Ted Hoff, Stanley Mazor, and Masatoshi Shima led its design. Intel first built the chip for a Japanese calculator company, Busicom, and then sold it as a general-purpose part. A processor on one chip let product designers buy the central logic as one part instead of building it from many separate parts.

### Moore's law

In 1965, Gordon Moore wrote in *Electronics* magazine that the number of components on a chip had roughly doubled each year, and he expected that pace to continue for a while. In 1975 he revised the pace to about every two years. Later writers called this observation Moore's law, and chip makers used it to plan research and factories for decades.

Smaller transistors switch faster and use less energy per switch. Robert Dennard and his colleagues described this scaling in 1974. For about three decades, shrinking transistors also kept power density roughly constant. Around 2005, the supply voltage could no longer fall as fast as the size did. Power density then rose, and clock speeds stopped climbing quickly. Designers responded with several processor cores on one chip, and they spent extra transistors on caches and specialized units.

## Key inventions

| Year | Invention | Who and where | Why it mattered |
|---|---|---|---|
| 1904 | Two-electrode vacuum tube | John Ambrose Fleming, London | Rectified radio signals, an early practical electronic valve |
| 1906 | Triode vacuum tube | Lee de Forest, United States | Amplified signals, which made long-distance radio and telephony practical |
| 1945 | ENIAC | J. Presper Eckert and John Mauchly, University of Pennsylvania | A large electronic digital computer built from about 17,000 tubes |
| 1947 | Point-contact transistor | John Bardeen and Walter Brattain, Bell Labs, New Jersey | The first working solid-state amplifier, with no hot filament |
| 1958 | First integrated circuit | Jack Kilby, Texas Instruments, Dallas | Put several components on one piece of germanium |
| 1959 | Planar silicon integrated circuit | Robert Noyce, Fairchild Semiconductor, California | Photolithography made many devices at once, which scaled to modern chips |
| 1971 | Intel 4004 | Federico Faggin, Ted Hoff, Stanley Mazor, and Masatoshi Shima, Intel, California | The first commercial single-chip microprocessor, with about 2,300 transistors |

## Key equations

Dynamic power in a CMOS circuit, which is the power used each time a gate switches:

$$P = \alpha \, C \, V^2 \, f$$

Here $P$ is power in watts, $\alpha$ is the activity factor, a dimensionless number between 0 and 1, $C$ is the switched capacitance in farads, $V$ is the supply voltage in volts, and $f$ is the clock frequency in hertz. Power grows with the square of the voltage, which is why cutting the voltage saves so much energy.

The doubling trend, written as a model fitted to observed chip counts:

$$N(t) = N_0 \cdot 2^{(t - t_0)/T_d}$$

Here $N(t)$ is the number of transistors in year $t$, $N_0$ is the count in the reference year $t_0$, and $T_d$ is the doubling time in years. The model describes past data. It does not follow from any physical law.

## Worked example

**Given:** The Intel 4004 in 1971 had $N_0 = 2300$ transistors. Assume a doubling time of $T_d = 2$ years. The Apple M1 chip, released in 2020, had about $16 \times 10^9$ transistors.

**Find:** (a) the count the trend predicts for 2020, (b) how far the prediction is from the actual M1, and (c) the doubling time that the 4004 and the M1 imply.

**Solution:**

1. Doublings from 1971 to 2020: $(2020 - 1971) / 2 = 24.5$.
2. Predicted count: $N = 2300 \times 2^{24.5} = 5.46 \times 10^{10}$ transistors, about 55 billion.
3. Ratio of prediction to actual: $54.6 / 16 = 3.4$.
4. Doublings needed to go from 2300 to $16 \times 10^9$: $\log_2(16 \times 10^9 / 2300) = 22.7$.
5. Implied doubling time: $T_d = 49 / 22.7 = 2.16$ years.

**Answer:** (a) About $5.5 \times 10^{10}$ transistors. (b) The trend overshoots the M1 by a factor of about 3.4. (c) The implied doubling time is about 2.2 years.

**Sanity check:** Over 49 years, the count rose by a factor of about $7 \times 10^6$, which matches $2^{22.7}$. A doubling time near 2 years is the right order of magnitude, and a 3.4 times gap over five decades is small on a log scale. The result is an observation about one trend, not a proof that the trend holds.

## Lessons for engineers today

The trend mattered because it gave engineers a target. Companies planned lithography, factories, and product schedules around it, and the whole industry moved together. The trend also came with a limit that the physics set. Dynamic power rises with voltage squared, so a chip that runs faster and hotter needs a plan for heat removal. A designer who forgets this gets a chip that throttles itself.

Treat any growth trend as a fit to data. Check whether the fit still holds, and write down the year it was measured. Engineers who planned around Moore's law in the 2000s had to change their designs when clock speeds stopped rising, and the ones who saw the limit early had time to adapt.

## Practice

1. Why did engineers move from vacuum tubes to transistors? Give two reasons.
2. Using $N = N_0 \cdot 2^{(t - t_0)/T_d}$ with $N_0 = 2300$ in 1971 and $T_d = 2$ years, find the predicted count in 1991.
3. A chip has $C = 1.0$ nF of switched capacitance, $\alpha = 0.10$, $V = 1.0$ V, and $f = 3.0$ GHz. Find its dynamic power in watts.
4. The chip in problem 3 raises its supply voltage by 10 percent and keeps the same frequency and capacitance. What is the new power, as a multiple of the old power?
5. Is Moore's law a law of physics? Explain in two or three sentences.

<details><summary>Answers</summary>

1. Transistors need no hot filament, so they use far less power and last longer. They are also much smaller, so more fit on one chip.
2. $2300 \times 2^{10} = 2{,}355{,}200$, about $2.36 \times 10^6$ transistors.
3. $P = 0.10 \times 1.0 \times 10^{-9} \times 1.0^2 \times 3.0 \times 10^{9} = 0.30$ W.
4. Power scales with $V^2$, so the new power is $1.1^2 = 1.21$ times the old power, a 21 percent increase.
5. No. It is an observation about how the chip industry progressed. No physical principle forces a doubling every two years, and the pace depends on lithography, investment, and economics. It also cannot continue forever, because transistors cannot shrink past atomic scales.

</details>

## Common mistakes

- Treating Moore's law as a physical law. It is an empirical trend, and it has changed pace over time.
- Crediting one person with the transistor or the integrated circuit. The transistor came from Bardeen, Brattain, and Shockley at Bell Labs. The integrated circuit came from Kilby at Texas Instruments and Noyce at Fairchild, independently.
- Calling ENIAC the first computer. Konrad Zuse completed the Z3 in Berlin in 1941, and it was an earlier programmable machine built from electromechanical relays.
- Assuming clock speed kept doubling with transistor count. After about 2005, voltage and power limits slowed clock increases, and extra transistors went into multiple cores and caches.
- Forgetting that dynamic power depends on voltage squared. A small voltage change has a large effect on power and heat.

## Go deeper

- [Computation Structures, MIT OpenCourseWare 6.004](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/): free lecture notes and videos on how digital systems, logic, and processors are built.
- [Digital logic and computers](../applications/electronics/07-digital-logic-and-computers.md): gates, flip-flops, and the microcontroller in this repo.
- [Diodes and transistors](../applications/electronics/03-semiconductors-diodes-and-transistors.md): doping, the p-n junction, and the MOSFET switch in detail.
- Next: [The modern era](10-the-modern-era.md).
