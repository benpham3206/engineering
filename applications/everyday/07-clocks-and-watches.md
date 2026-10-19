# Clocks and watches

**Type:** lesson

Clocks and watches are **timekeeping devices** that count equal intervals of time. Each timekeeping device trades accuracy, size, and cost, so an engineer must understand how its oscillator, counter, and display work together.

Every clock needs an oscillator with a steady period, a way to count its cycles, and a way to drive the display. A pendulum clock, a mechanical watch, and a quartz watch solve these three jobs in different ways.

**Prerequisites:** [Particle dynamics](../../physics/02-particle-dynamics.md), [Vibrations](../../physics/13-vibrations.md), [Circuit basics](../electronics/01-circuit-basics.md), [Digital logic and computers](../electronics/07-digital-logic-and-computers.md)
**Time:** 4-6 h

## Core ideas

### How it works

A pendulum clock uses gravity as the restoring force. A bob hangs on a rod and swings. For a small swing, the period depends only on the length of the rod and on gravity. The **escapement** is the part that converts the swing into discrete steps. Each swing lets one tooth of the escape wheel advance, and the escapement gives the pendulum a small push each cycle to replace the energy lost to friction. The gear train reduces the escape wheel's motion to the speed of the hands. A weight or a spring supplies the energy.

A mechanical watch replaces the pendulum with a **balance wheel** and a hairspring. The **hairspring** is a coiled spring that pulls the balance back toward its rest position. The wheel swings back and forth at a fixed rate set by its moment of inertia and the spring stiffness. Many watches run at about 4 Hz, which is 28 800 beats per hour. A mainspring stores the energy, and the lever escapement releases it in small steps.

A quartz watch uses a **quartz crystal** as the oscillator. The crystal is cut into a tuning-fork shape and mounted in a small package. When an electric field is applied, quartz deforms, which is the **piezoelectric effect**. The crystal resonates at a frequency set by its dimensions. A small oscillator circuit drives the crystal at that frequency. A chain of binary divider stages reduces the frequency to 1 Hz. A small stepper motor moves the hands once per second.

### Main parts

- **Pendulum clock:** a bob, a rod, an escapement (anchor or deadbeat), a gear train, and a weight or a mainspring.
- **Mechanical watch:** a balance wheel, a hairspring, a pallet fork, an escape wheel, a mainspring, a gear train, and jewel bearings. Synthetic ruby jewels reduce friction and wear at the pivots.
- **Quartz watch:** a quartz crystal, an oscillator integrated circuit, a binary divider chain, a stepper motor, a gear train, and a coin cell battery.

### Variants

Pendulum clocks come as longcase (grandfather) clocks, mantel clocks, and wall clocks. Marine chronometers are precise mechanical clocks built for ships to find longitude at sea. The chronometer that John Harrison completed in 1761 is the best-known example. Mechanical wristwatches come as manual-wind and automatic (self-winding) watches. Quartz watches come as analog and digital models. Atomic clocks use a microwave transition in cesium or a similar atom, and they serve as national time standards.

## Key equations

Assumptions for the equations below: the pendulum is a point mass on a light, rigid rod, the swing is small (below about 15 degrees) so the sine of the angle is close to the angle, and gravity is uniform at $g = 9.81\ \text{m}/\text{s}^2$ (Earth surface, typical sea-level value; it varies from about 9.78 to 9.83 with latitude). The hairspring is an ideal linear torsion spring, and friction is neglected in the period calculation.

- Pendulum period: $T = 2\pi \sqrt{L / g}$, where $T$ is the period in seconds (s), $L$ is the length from pivot to bob centre in metres (m), and $g$ is gravity in m/s$^2$. The period does not depend on the bob mass.
- Balance wheel period: $T = 2\pi \sqrt{I / \kappa}$, where $I$ is the wheel's moment of inertia in kg m$^2$ and $\kappa$ is the hairspring's torsional stiffness in N m/rad. The assumption is that the spring is linear and the amplitude is small.
- Quartz frequency and division: $f_{\text{out}} = f_{\text{in}} / 2^{n}$, where $f_{\text{in}}$ is the crystal frequency in hertz (Hz), $n$ is the number of binary stages (a dimensionless integer), and $f_{\text{out}}$ is the output frequency. The assumption is that each stage divides exactly by two.
- Rate error: $\varepsilon = \Delta f / f$, expressed in parts per million (ppm) as $\varepsilon \times 10^6$. The clock error in seconds per day is $\varepsilon \times 86\,400\ \text{s}$. The assumption is that the rate error is constant over the day.

## Worked example

**Given:** A seconds pendulum swings with a full period of $T = 2.0\ \text{s}$ at $g = 9.81\ \text{m}/\text{s}^2$ (Earth surface). A quartz watch has a rate error of $\varepsilon = 20$ ppm.

**Find:** (a) the length of the pendulum, (b) the clock error per day, and (c) the error in 30 days.

**Solution:**

1. Pendulum length from $T = 2\pi \sqrt{L/g}$: $L = g (T / 2\pi)^2 = 9.81 \times (2.0 / 6.283)^2 = 0.994\ \text{m}$.
2. Error per day: $\varepsilon \times 86\,400 = 20 \times 10^{-6} \times 86\,400 = 1.73\ \text{s}$.
3. Error in 30 days: $1.73 \times 30 = 51.8\ \text{s}$.

**Answer:** (a) $0.994\ \text{m}$. (b) $1.73\ \text{s}$ per day. (c) $52\ \text{s}$ in 30 days.

**Sanity check:** A pendulum of about one metre has a period close to 2 s, which matches the known length of the seconds pendulum. A quartz error of 20 ppm is about 0.002 percent, and it is a typical value for a watch crystal. The result of 1.73 s per day is consistent with $20 \times 10^{-6} \times 86\,400$.

## Why the number 32,768 Hz

Quartz watches use a crystal that oscillates at $32\,768\ \text{Hz}$. That value equals $2^{15}$, which is $2 \times 2 \times \dots \times 2$ with fifteen factors.

A binary divider chain halves the frequency at each stage. Each stage is a flip-flop, which is a circuit that toggles its output on every second input pulse. After $n$ stages, the output frequency is $32\,768 / 2^{n}$. With $n = 15$, the result is $32\,768 / 32\,768 = 1\ \text{Hz}$. Each stage needs only a simple binary flip-flop, so the chain is small and cheap.

Engineers picked this frequency for three reasons. The divider needs exactly fifteen stages to reach 1 Hz, with no extra logic. A tuning-fork crystal of this frequency is small enough to fit in a watch, and its size balances stiffness and drive power. A crystal at this frequency also has a low power draw, which lets a coin cell last years. The number is not the only frequency that could work, but a power of two makes the division exact and the circuit simple.

## Design trade-offs

- **Accuracy.** A pendulum clock can reach about a second per day or better in a stable room. A quartz crystal in a watch is typically within about 10 to 20 ppm, which is roughly 1 to 2 s per day.
- **Temperature.** A steel pendulum rod of length $L$ with a thermal expansion coefficient of $12 \times 10^{-6}$ per kelvin (typical value) lengthens when it warms. A 10 K rise changes the rod length by $1.2 \times 10^{-4}$, and the period by half that. The clock loses about $5.2$ s per day. Engineers use invar, a nickel-iron alloy with a much lower expansion coefficient, or a compensated pendulum to fix this.
- **Swing amplitude.** The small-angle formula assumes the swing is small. For a swing of amplitude $\theta_0$ in radians, the first-order correction is $T \approx T_0 (1 + \theta_0^2 / 16)$, where $T_0$ is the small-angle period. The assumption is that $\theta_0$ is small enough for this series to converge quickly. At a 15 degree amplitude ($\theta_0 = 0.262$ rad), the period is about 0.4 percent longer than $T_0$. Clocks keep the swing nearly constant with the escapement so that this error stays steady.
- **Power.** A mechanical watch needs a mainspring that must be wound or driven by the wrist. A quartz watch needs a small battery, which is a cost and a waste stream.
- **Size and shock.** A balance wheel with a hairspring is sensitive to shock, so watch makers add shock protection. A quartz crystal resists shock better than a balance.
- **Cost.** Quartz movements are cheap to mass-produce, while a high-grade mechanical movement takes many hours of hand work.

## How it fails

- **Pendulum clock.** A change in temperature changes the rod length. Dust and oil thicken in the escapement, and the clock stops or slows. A clock that is not level swings unevenly.
- **Mechanical watch.** Old lubricant thickens and the watch slows. A magnetic field can magnetize the hairspring, which then pulls the balance off its true rate. A hard knock can break a pivot or bend the balance staff.
- **Quartz watch.** The crystal ages slowly, and its frequency drifts over years. Moisture or a leaking battery can corrode the circuit. A cold temperature changes the crystal's rate, and a watch sitting in a freezer loses time.

## History

Christiaan Huygens built the first pendulum clock in 1656, and he patented the design in 1657. The pendulum made clocks far more accurate than the older verge-and-foliot movements.

John Harrison completed his H4 marine chronometer in 1761. It kept time accurately enough at sea to find longitude, which was a central navigation problem of the eighteenth century.

Pierre and Jacques Curie discovered piezoelectricity in 1880. The effect later made quartz oscillators possible. Seiko released the Astron in December 1969, the first quartz wristwatch, and quartz watches then spread through the world market in the 1970s and 1980s.

## Practice

1. Find the length of a pendulum with a full period of $1.0\ \text{s}$ at $g = 9.81\ \text{m}/\text{s}^2$ (Earth surface).
2. A crystal of $32\,768\ \text{Hz}$ feeds a binary divider. How many stages reach $2\ \text{Hz}$?
3. A clock gains 3 s per day. Find its rate error in ppm.
4. A steel pendulum rod warms by 10 K, with $\alpha = 12 \times 10^{-6}$ per kelvin. Find the change in period and the clock error per day, assuming the rod lengthens and the period rises by half the fractional change in length.
5. A pendulum has a small-angle period of $1.00\ \text{s}$. It swings with an amplitude of $15^\circ$. Find its actual period, using the first-order correction.

<details><summary>Answers</summary>

1. $L = g (T / 2\pi)^2 = 9.81 \times (1.0 / 6.283)^2 = 0.249\ \text{m}$.
2. $32\,768 / 2^{n} = 2$ requires $2^{n} = 16\,384 = 2^{14}$, so $n = 14$ stages.
3. $\varepsilon = 3 / 86\,400 = 3.47 \times 10^{-5}$, which is $34.7\ \text{ppm}$.
4. $\Delta L / L = 12 \times 10^{-6} \times 10 = 1.2 \times 10^{-4}$. The period rises by half of that, $6.0 \times 10^{-5}$, which is 60 ppm. The clock loses $60 \times 10^{-6} \times 86\,400 = 5.2\ \text{s}$ per day.
5. $\theta_0 = 15^\circ = 0.2618\ \text{rad}$, so $T = 1.00 \times (1 + 0.2618^2 / 16) = 1.00 \times 1.0043 = 1.004\ \text{s}$.

</details>

## Common mistakes

- Thinking the pendulum period depends on the bob mass. It depends on length and gravity only, for small swings.
- Assuming a large swing keeps the same period. The small-angle result is accurate only for small swings.
- Believing the crystal's 1 Hz comes from the crystal directly. The crystal runs at 32 768 Hz, and the divider makes the 1 Hz.
- Using $g = 9.8\ \text{m}/\text{s}^2$ everywhere. Latitude and altitude change $g$ enough to matter for precision clocks.
- Forgetting that a clock's error is a rate, not a fixed time. A rate error of 20 ppm builds up every day.
- Treating a real pendulum as ideal. The rod's own mass and air drag shift the period a little, so the formula gives a close estimate, not an exact value.
- Assuming a quartz watch needs no service. The coin cell runs down, and the seal needs replacement to keep moisture out of the circuit.

## Go deeper

- [*OpenStax University Physics Volume 1*, Chapter 15](https://openstax.org/books/university-physics-volume-1/pages/15-introduction): free textbook on oscillations, including the simple pendulum.
- [NIST Time and Frequency Division](https://www.nist.gov/pml/time-and-frequency-division): the U.S. standards body for time and frequency, which maintains the national time standard.
- [Reference: mechanics](../../physics/reference-mechanics.md): the rotational and oscillation equations used in the balance wheel and pendulum.
- [Vibrations](../../physics/13-vibrations.md) for natural frequency and damping in mechanical oscillators.
- [Circuit basics](../electronics/01-circuit-basics.md) for the oscillator and battery circuit in a quartz watch.
