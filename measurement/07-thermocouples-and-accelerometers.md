# Thermocouples and accelerometers

**Type:** lesson

Thermocouples measure temperature with a voltage produced by a junction of two dissimilar metals. Accelerometers measure acceleration, usually with a small mass on a spring, and output a voltage or digital value proportional to it. Both are common sensors on machines, test rigs, and vehicles.

**Prerequisites:** [Sensors and transducers](05-sensors-and-transducers.md), [Electricity and magnetism](../physics/06-electricity-and-magnetism.md), [Particle dynamics](../physics/02-particle-dynamics.md) (acceleration)
**Time:** 4-6 h

## Core ideas

- **Seebeck effect**: when two different metals are joined at one end and that junction is at a different temperature than the other ends, a small voltage appears. The junction you care about is the **hot junction** (sensing tip). The other end is the **cold junction** (reference).
- A thermocouple measures a **voltage difference**, not an absolute temperature. To find the hot junction temperature, you must know the cold junction temperature and correct for it. This is called **cold junction compensation**.
- **Type K** (chromel and alumel) is a common general-purpose thermocouple. Near room temperature its sensitivity is roughly 41 $\mu$V/°C (a typical value). The relation is not perfectly linear, so accurate work uses standard reference tables or a polynomial.
- Thermocouples are rugged and cover wide temperature ranges, but their voltages are small, so the amplifier and wiring must be clean and well shielded.
- **Accelerometer**: a proof mass on a spring (or a piezoelectric crystal) moves when the housing accelerates. The output is proportional to acceleration. Its unit is often given as mV/g, where $g$ is standard gravity.
- **Piezoelectric** accelerometers produce a charge when a crystal is compressed. They respond well to vibration but cannot measure steady acceleration such as gravity. **MEMS** accelerometers use tiny silicon structures and can measure static tilt.
- **Calibration check.** A MEMS accelerometer at rest should read about 1 g on the axis pointing up, which is $9.80665\ \text{m/s}^2$ by definition of standard gravity.
- **Mounting** matters. A loose mount adds resonance and noise, and a very heavy sensor changes the vibration it measures.

## Key equations

Thermocouple, linear approximation near room temperature, where $S$ is the Seebeck sensitivity in V/K (or V/°C), $V$ is the measured voltage, and $T_{\text{cj}}$ is the cold junction temperature:

$$T_{\text{hot}} = T_{\text{cj}} + \frac{V}{S}$$

For type K, $S \approx 41\ \mu\text{V/°C} = 4.1 \times 10^{-5}\ \text{V/°C}$ near room temperature.

Accelerometer, linear with sensitivity $s$ in mV/g:

$$a\ [\text{g}] = \frac{V_{\text{out}}\ [\text{mV}]}{s\ [\text{mV/g}]} \qquad a\ [\text{m/s}^2] = a\ [\text{g}] \times 9.80665\ \text{m/s}^2$$

## Worked example

**Given:** A type K thermocouple reads 2.05 mV. The cold junction (at the meter terminals) is at 20.0 °C. Separately, a 100 mV/g accelerometer reads 350 mV.

**Find:** (a) the hot junction temperature, and (b) the acceleration in g and in $\mathrm{m/s^2}$.

**Assumptions:** The linear sensitivity of 41 $\mu$V/°C applies over the measured range. For a precise value you would use a reference table, which is noted below. Cold junction temperature is measured accurately.

**Solution (a):**

- Voltage change from the reference: $V / S = 2.05 \times 10^{-3}\ \text{V} / (4.1 \times 10^{-5}\ \text{V/°C}) = 50.0\ \text{°C}$
- Hot junction: $T_{\text{hot}} = 20.0 + 50.0 = 70.0\ \text{°C}$

**Solution (b):**

- In g: $a = 350\ \text{mV} / 100\ \text{mV/g} = 3.50\ \text{g}$
- In SI: $a = 3.50 \times 9.80665 = 34.32\ \text{m/s}^2$

**Answer:** (a) $T_{\text{hot}} \approx 70\ \text{°C}$. (b) $a = 3.50\ \text{g} = 34.3\ \text{m/s}^2$.

**Sanity check:** A 2 mV reading from a type K couple 50 °C above room temperature is in the usual range, since the sensitivity is about 41 $\mu$V/°C. For the accelerometer, 3.5 g is a moderate impact or vibration level. A static tilt test should give about 1 g, which is a good check before trusting larger readings.

## Practice

1. A type K thermocouple reads 3.28 mV with a cold junction at 25 °C, using 41 $\mu$V/°C. Find the hot junction temperature.
2. A 50 mV/g accelerometer reads 127 mV. Find the acceleration in g and in $\mathrm{m/s^2}$.

<details><summary>Answers</summary>

1. 105 °C
2. 2.54 g; 24.9 $\mathrm{m/s^2}$

</details>

## Common mistakes

- Reading the thermocouple voltage as temperature. You must add the cold junction temperature.
- Forgetting cold junction compensation, which shifts the answer by the full reference error.
- Using the linear sensitivity far from room temperature, where the error grows. Use a reference table for wide ranges.
- Mixing up g with $\mathrm{m/s^2}$. $1\ \text{g} = 9.80665\ \text{m/s}^2$ is a unit, not a dimensionless ratio.
- Trusting a piezoelectric accelerometer for steady acceleration. It cannot measure a constant force, such as gravity alone.

## Go deeper

- [University Physics Volume 2, Chapter 1: Introduction](https://openstax.org/books/university-physics-volume-2/pages/1-introduction) by OpenStax: temperature, thermometers, and thermal expansion, the physical background for thermocouples.
- [University Physics Volume 2, Chapter 10: Introduction](https://openstax.org/books/university-physics-volume-2/pages/10-introduction) by OpenStax: resistors and circuits, the electrical background for signal conditioning.

Look up the reference table for your thermocouple type from the manufacturer or a standards body before using values outside room temperature.
- [Measurement reference](reference.md): the lookup sheet for this topic.
