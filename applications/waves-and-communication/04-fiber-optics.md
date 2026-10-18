# Fiber optics: total internal reflection, attenuation, and data transmission

**Type:** lesson

An optical fiber is a thin glass or plastic strand that guides light along its length, often for many kilometres. Engineers need to understand it because fiber carries most long-distance internet and telephone traffic, and its loss and dispersion set how far and how fast a link can run.

**Prerequisites:** [Waves, light, and heat](../../physics/07-waves-light-heat.md), [Trigonometry](../../math/02-trigonometry.md)
**Time:** 6-8 h

## Core ideas

### How it works

A fiber has a core with a high refractive index $n_1$, surrounded by cladding with a lower index $n_2$. The refractive index is the ratio $n = c/v$, where $c$ is the speed of light in vacuum and $v$ is the speed in the material. Silica glass has $n$ near 1.46 to 1.48, so the difference between core and cladding is small.

Light that meets the core-cladding boundary at a shallow angle reflects back into the core. This is total internal reflection. It happens when the angle of incidence is larger than the critical angle $\theta_c$. Light at a steeper angle leaks out of the core and is lost.

The light bounces down the fiber, and each reflection keeps it inside. The fiber can curve, and the light follows the curve because it still meets the wall at a shallow angle.

### Main parts

- **Core.** The glass that carries light. Germanium or phosphorus doping raises its index slightly.
- **Cladding.** Glass with a lower index. The outer diameter is typically 125 micrometres.
- **Coating and jacket.** A polymer coating protects the glass, typically about 250 micrometres in total. The cable jacket protects the coated fibers.
- **Light source.** An LED for short multimode links. A laser diode for long links.
- **Photodetector.** A PIN photodiode or an avalanche photodiode turns light back into current.
- **Connectors and splices.** Each one adds a small loss, and a dirty end face adds more.
- **Optical amplifier.** An erbium-doped fiber amplifier boosts the light near 1550 nm without converting it to an electrical signal.

### Variants

- **Multimode fiber.** The core is about 50 or 62.5 micrometres. Many light paths travel at different speeds, so pulses spread. It suits links of a few hundred metres inside buildings and data centers.
- **Single-mode fiber.** The core is about 9 micrometres. Only one path carries the light, so pulses spread much less. It suits long-haul, metro, and submarine links.
- **Plastic optical fiber.** A thick, cheap polymer fiber for short runs, such as inside a car or a home audio link.

## Key equations

- Snell's law, with angles $\theta$ in radians or degrees and refractive indices $n$ dimensionless: $n_1 \sin\theta_1 = n_2 \sin\theta_2$.
- Critical angle: $\theta_c = \arcsin(n_2 / n_1)$.
- Numerical aperture, dimensionless: $\mathrm{NA} = \sqrt{n_1^2 - n_2^2}$. When light enters from air, with $n_0 = 1$, the acceptance half-angle is $\theta_a = \arcsin(\mathrm{NA})$.
- Attenuation, with $\alpha$ in dB/km and $L$ in km: $P_{out} = P_{in} \cdot 10^{-\alpha L / 10}$.
- Power level, with $P$ in watts: $P\,(\text{dBm}) = 10 \log_{10}(P / 1\ \text{mW})$.
- Link budget margin, in dB: $M = P_{tx} - P_{rx,\min} - L_{total}$, where $P_{rx,\min}$ is the receiver sensitivity.
- Propagation delay, with $t$ in seconds and $L$ in metres: $t = L\,n / c$, where $c = 3.00 \times 10^8\ \text{m/s}$.

## Worked example

**Given:** An 80 km single-mode link at 1550 nm. The fiber loss is $\alpha = 0.2$ dB/km (typical). The link has four connectors at 0.5 dB each and twenty splices at 0.05 dB each. The transmitter sends $P_{tx} = 0$ dBm, which is 1.0 mW. The receiver needs at least $P_{rx,\min} = -30$ dBm. The core index is $n = 1.468$.

**Find:** (a) the total loss, (b) the received power, (c) the link margin, and (d) the propagation delay.

**Solution:**

1. Fiber loss: $0.2 \times 80 = 16$ dB.
2. Connector and splice loss: $4 \times 0.5 + 20 \times 0.05 = 3$ dB.
3. Total loss: $16 + 3 = 19$ dB.
4. Received power: $0 - 19 = -19$ dBm, which is $10^{-1.9}$ mW, or about $12.6\ \mu\text{W}$.
5. Margin: $M = 0 - (-30) - 19 = 11$ dB.
6. Speed in fiber: $v = c/n = 3.00 \times 10^8 / 1.468 = 2.04 \times 10^8$ m/s. Delay: $t = 80\,000 / 2.04 \times 10^8 = 3.91 \times 10^{-4}$ s, which is 0.39 ms.

**Answer:** (a) 19 dB. (b) $-19$ dBm, about $12.6\ \mu\text{W}$. (c) 11 dB. (d) 0.39 ms.

**Sanity check:** A 19 dB loss divides the power by about 80, because $10^{1.9} \approx 79$. The received power is therefore $1.0\ \text{mW} / 79 \approx 12.6\ \mu\text{W}$, which matches step 4. The margin is positive, so the receiver sees enough light. The delay is longer than the vacuum value of about 0.27 ms, as expected for light in glass.

## Design trade-offs

- **Wavelength.** Loss depends on wavelength. Silica fiber is near 0.2 dB/km at 1550 nm and about 0.35 dB/km at 1310 nm (typical). Multimode links at 850 nm lose a few dB/km, which limits them to short runs.
- **Dispersion.** Pulses spread as they travel. Standard single-mode fiber spreads about 17 ps per nm of source width per km at 1550 nm (typical), so the bit rate times distance product is limited.
- **Amplifiers versus regeneration.** Amplifiers restore power but also add noise. Regenerators convert to electrical signals, retime, and resend, at higher cost and complexity.
- **Cost of the endpoints.** Multimode lasers and LEDs are cheap. Single-mode lasers and receivers cost more, but one fiber carries far more data over far more distance.
- **Bend radius.** Tight bends leak light. Cables have a minimum bend radius, and installers must respect it.

## How it fails

- **Macrobends.** A pinched cable or a sharp bend lets light escape the core. The warning sign is a loss step on an optical time-domain reflectometer trace at the bend.
- **Dirty or damaged connectors.** Dust on an end face scatters light and adds loss and back-reflection. Cleaning with a lint-free wipe and a fiber cleaner fixes most cases.
- **Dispersion.** Pulses overlap at the receiver, and bit errors rise. Single-mode fiber and dispersion-compensating modules limit this.
- **Physical damage.** Digging equipment cuts cables. Buried routes use markers, and cable ducts protect the fiber.
- **Eye damage.** Infrared light at 1550 nm is invisible, and a live fiber end can damage an eye. Laser safety classes and the rule against looking into a fiber end exist for this reason.

## History

Charles K. Kao and George A. Hockham proposed in 1966 that glass fiber with loss below 20 dB/km could carry communication signals. In 1970, researchers at Corning Glass Works made fiber that met that loss target. Commercial fiber links appeared in the late 1970s. The first transatlantic fiber cable, TAT-8, entered service in 1988. Kao shared the 2009 Nobel Prize in Physics for this work.

## Practice

1. A fiber has $n_1 = 1.50$ and $n_2 = 1.45$. Find the critical angle.
2. A 10 km link has loss 0.35 dB/km. The launch power is 1.0 mW. Find the total loss in dB and the received power in mW.
3. Light enters from air into a fiber with $n_1 = 1.50$ and $n_2 = 1.47$. Find the numerical aperture and the acceptance half-angle.
4. Light travels 500 m in a fiber with $n = 1.468$. Find the delay in microseconds.
5. Explain why a single-mode fiber carries more data per second than a multimode fiber over the same distance.

<details><summary>Answers</summary>

1. $\theta_c = \arcsin(1.45 / 1.50) = 75.2^\circ$.
2. Loss $= 0.35 \times 10 = 3.5$ dB. The received power is $10^{-0.35} = 0.447$ mW.
3. $\mathrm{NA} = \sqrt{1.50^2 - 1.47^2} = 0.298$. The half-angle is $\arcsin(0.298) = 17.4^\circ$.
4. $t = 500 \times 1.468 / (3.00 \times 10^8) = 2.45\ \mu\text{s}$.
5. A single-mode fiber has one light path, so pulses do not spread from different path lengths. Less spreading means pulses can follow each other more closely, which allows a higher bit rate.

</details>

## Common mistakes

- Adding losses in linear units, or multiplying dB values. Power ratios multiply, and dB values add.
- Confusing the critical angle, which is inside the fiber, with the acceptance angle, which is outside.
- Leaving connectors and splices out of the link budget. They often cost more than the fiber itself over short runs.
- Using $c$ for the speed of light in fiber. The speed in fiber is $c/n$.
- Bending a cable tighter than its minimum radius, then blaming the fiber for the loss.

## Go deeper

- [University Physics Volume 3, Chapter 1: light, reflection, refraction, and total internal reflection](https://openstax.org/books/university-physics-volume-3/pages/1-introduction) by OpenStax. Free, with a full treatment of the physics used here.
- [Optics, course 2.71](https://ocw.mit.edu/courses/2-71-optics-spring-2009/) by MIT OpenCourseWare. Free lecture materials on optical science with engineering applications.
- Related lessons: [Lasers](03-lasers.md), which covers the light source, and [Radio and antennas](02-radio-and-antennas.md), which covers the other main way to send a signal without a wire.
