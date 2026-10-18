# Transformers

**Type:** lesson

A transformer changes an alternating voltage up or down by linking two coils through a shared magnetic core. Engineers use transformers at almost every step between a power station and a wall socket, and they design them around the turns ratio, the losses, and the isolation that separates the two windings.

**Prerequisites:** [Electricity and magnetism](../../physics/06-electricity-and-magnetism.md), [Circuit basics](../electronics/01-circuit-basics.md)
**Time:** 4-6 h

## Core ideas

### How it works

An alternating current in the primary winding drives a changing magnetic flux through an iron core. That flux also passes through the secondary winding. Faraday's law then induces an EMF in each winding.

The core carries nearly all the flux, so every turn on either winding sees the same flux change. Each turn therefore has the same EMF, and the total voltage on a winding is proportional to its number of turns.

The secondary current creates its own magnetic field, which opposes the change in core flux. To keep the core flux nearly constant, the primary draws the extra current that balances the secondary. The primary current therefore follows the load.

An ideal transformer has no losses, no leakage flux, and an iron core with infinite permeability. In that case the voltage ratio equals the turns ratio, the current ratio is the inverse, and the power in equals the power out.

A transformer needs a changing flux to work. A steady DC current gives a steady flux, which induces no EMF in the secondary. The primary then behaves like a short circuit and overheats.

The two windings share flux through the core, not a conductor. That gives electrical isolation: the secondary has no direct connection to the primary.

### Main parts

The core is laminated silicon steel. Thin laminations, insulated from each other, reduce eddy-current loss. Grain-oriented steel carries flux better in one direction, which suits power transformers (typical). Amorphous metal cores have lower core loss than silicon steel, but they cost more and are harder to make (typical).

The primary winding connects to the supply. The secondary winding connects to the load. Copper or aluminum conductors carry the current, and paper, enamel, oil, or resin insulate them.

A tap changer switches between taps on a winding, which changes the turns ratio and holds the output voltage steady as the load changes.

Dry-type transformers rely on air for cooling. Oil-filled transformers use mineral oil or ester fluid in a tank, with radiators, fans, or pumps to move heat away.

Bushings bring the windings out of the tank. A conservator and a breather let the oil expand and contract with temperature while keeping moisture out.

### Variants

A power transformer steps voltage up at generating stations and down at substations. A distribution transformer steps voltage down to the level used by homes and small businesses, and it is often mounted on a pole or a pad.

An isolation transformer has a 1:1 turns ratio. It isolates a circuit from its supply, which lowers the risk of shock and reduces noise on the supply line.

An autotransformer uses one winding for both sides. It costs less and is more efficient for small voltage changes, but it gives no isolation.

Instrument transformers scale current or voltage down to safe levels for meters and protective relays.

Three-phase transformers use three legs on one core, or three single-phase units wired together. Both carry power the same way.

## Key equations

Voltage ratio:

$$\frac{V_1}{V_2} = \frac{N_1}{N_2} = a$$

Here $V_1$ and $V_2$ are the primary and secondary voltages in volts, $N_1$ and $N_2$ are the turn counts (dimensionless), and $a$ is the turns ratio.

Current ratio for an ideal transformer:

$$\frac{I_2}{I_1} = \frac{N_1}{N_2}$$

Here $I_1$ and $I_2$ are the primary and secondary currents in amps. The current ratio is the inverse of the voltage ratio.

Ideal power balance:

$$V_1 I_1 = V_2 I_2$$

The product $VI$ is the apparent power in volt-amperes (VA). For a resistive load it equals the real power in watts.

Core flux and primary voltage:

$$V_1 \approx 4.44\, f\, N_1\, \Phi_{max}$$

Here $f$ is the supply frequency in hertz, and $\Phi_{max}$ is the peak core flux in webers (Wb). This shows that a transformer needs AC, and that a lower frequency needs more flux and a bigger core for the same voltage.

Efficiency:

$$\eta = \frac{P_{out}}{P_{out} + P_{core} + P_{cu}}$$

Here $P_{out}$ is the output power in watts, $P_{core}$ is the core loss in watts, and $P_{cu}$ is the copper loss in watts.

Copper loss and core loss:

$$P_{cu} = I^2 R \qquad P_{cu} = x^2 P_{cu,rated}$$

Here $I$ is the winding current in amps, $R$ is the winding resistance in ohms, and $x$ is the load as a fraction of rated current (dimensionless). Core loss depends on voltage and frequency, not on load current, so it stays about constant.

Impedance referred to the primary:

$$Z_1 = a^2 Z_2$$

Here $Z_1$ and $Z_2$ are impedances in ohms.

## Worked example

**Given:** A 25 kVA single-phase distribution transformer with a 7200 V primary and a 240 V secondary. Full-load copper loss is 350 W, and core loss is 120 W. The transformer supplies 75 percent of its rated power at unity power factor.

**Find:** (a) the turns ratio, (b) the rated primary and secondary currents, and (c) the efficiency at 75 percent load.

**Assumptions:** Steady sinusoidal operation. Unity power factor. Core loss stays constant with load. Copper loss scales with the square of current.

**Solution:**

1. Turns ratio: $a = V_1 / V_2 = 7200 / 240 = 30$, so the ratio is 30:1.
2. Rated currents: $I_2 = 25\,000 / 240 = 104.2\ \text{A}$ on the secondary, and $I_1 = 25\,000 / 7200 = 3.47\ \text{A}$ on the primary.
3. Output at 75 percent load: $P_{out} = 0.75 \times 25\,000 = 18\,750\ \text{W}$.
4. Copper loss at 75 percent current: $P_{cu} = 350 \times 0.75^2 = 196.9\ \text{W}$. Core loss stays at 120 W.
5. Efficiency: $\eta = 18\,750 / (18\,750 + 120 + 196.9) = 18\,750 / 19\,066.9 = 0.983$.

**Answer:** (a) 30:1. (b) 104 A on the secondary and 3.47 A on the primary. (c) About 98.3 percent.

**Sanity check:** The input power is 19 067 W, which is larger than the output of 18 750 W, so the losses are positive. At full load the primary product $3.47 \times 7200 = 25\,000\ \text{VA}$ matches the rating. The full-load copper loss of 350 W is 1.4 percent of 25 kW, which is a reasonable size for a distribution unit.

## Design trade-offs

Core material sets the core loss. Grain-oriented steel and amorphous metal reduce it. Core loss is paid all day, even at light load, so low no-load loss matters most for distribution transformers that spend much of their life lightly loaded.

Copper and iron split the losses. More copper lowers copper loss and raises cost and size. Designers pick the split that gives the lowest total cost over the life of the unit. Large power transformers reach efficiencies above 99 percent at rated load (typical).

Frequency sets the core size. Flux density is limited by core saturation, so a higher frequency needs a smaller core for the same voltage. Aircraft often use 400 Hz for this reason (typical). Higher frequency also raises core loss, so the saving is not free.

Cooling sets the rating. Oil-filled units carry heat away well and insulate the windings, but they carry a fire risk. Dry-type units avoid oil, but they give less rating per unit volume (typical).

Noise comes from magnetostriction. The core changes length slightly with flux, so it hums at twice the supply frequency: 120 Hz on a 60 Hz grid, and 100 Hz on a 50 Hz grid.

Insulation life sets the thermal limit. A common rule of thumb says that every rise of about 6 to 8 degrees Celsius above the rated temperature roughly halves the insulation life.

## How it fails

Insulation breaks down from lightning or switching surges, or from aging. Warning signs are partial discharge, tracking marks on bushings, and dissolved gases in the oil. Surge arresters and insulation coordination protect the windings.

Overload or blocked cooling overheats the windings. Oil temperature rises, and the unit may smell of burnt insulation. Temperature sensors raise an alarm, and overload relays trip the unit.

Energizing a transformer at the wrong point of the voltage wave, or with residual core flux, draws a large inrush current, often many times rated current. Differential relays use harmonic restraint so they do not trip on inrush.

A winding short circuit produces large magnetic forces that can deform the windings. Fuses and breakers limit the fault current, and the windings are designed to withstand it.

Moisture in the oil or paper lowers the dielectric strength. Sealed tanks and breathers with desiccant keep moisture out.

Internal arcing in an oil-filled unit releases gas. A Buchholz relay, which senses gas in the pipe to the conservator, detects this and trips the unit.

## History

Michael Faraday's induction experiments in 1831 established the principle. In the early 1880s, Lucien Gaulard and John Dixon Gibbs developed transformers that were presented in Europe, and they helped make the case for AC distribution. In 1886, William Stanley, working for Westinghouse, powered an AC lighting system in Great Barrington, Massachusetts, using transformers. Transformers let engineers raise the voltage for long-distance transmission and lower it again for users, which cut the loss in the lines.

## Practice

1. A transformer has 1000 primary turns and 50 secondary turns. The primary voltage is 1200 V. Find the secondary voltage.
2. A 50 kVA transformer has a 7200 V primary and a 240 V secondary. Find the rated secondary current.
3. A transformer is 92 percent efficient and delivers 9.2 kW to its load. Find the input power.
4. A 20 kW transformer at rated load and unity power factor has 150 W of core loss and 400 W of copper loss. Find its efficiency.
5. A transformer with a turns ratio of 10:1 feeds a 4 ohm load. Find the load impedance as seen from the primary.

<details><summary>Answers</summary>

1. 60 V, from $V_2 = V_1 N_2 / N_1 = 1200 \times 50 / 1000$.
2. 208 A, from $I_2 = 50\,000 / 240$.
3. 10.0 kW, from $P_{in} = 9200 / 0.92$.
4. 97.3 percent, from $\eta = 20\,000 / (20\,000 + 150 + 400)$.
5. 400 ohms, from $Z_1 = a^2 Z_2 = 10^2 \times 4$.

</details>

## Common mistakes

- Applying the turns ratio to currents in the same direction. Current scales inversely with the voltage ratio.
- Assuming a transformer works on DC. A steady current gives a steady flux, so the secondary gets no EMF and the primary can overheat.
- Treating kVA and kW as the same unit. Real power in kW equals apparent power in kVA times the power factor.
- Using the full-load efficiency for every load. Copper loss falls with the square of current, and core loss stays the same.
- Assuming an autotransformer isolates its two sides. Its windings share a conductor, so there is no isolation.

## Go deeper

- [University Physics Volume 2, Chapter 15: AC Circuits](https://openstax.org/books/university-physics-volume-2/pages/15-introduction), OpenStax. Free text covering AC circuits and transformers.
- [University Physics Volume 2, Chapter 13: Electromagnetic Induction](https://openstax.org/books/university-physics-volume-2/pages/13-introduction), OpenStax. Free text covering the induction that drives a transformer.
- Related lessons: [generators and alternators](04-generators-and-alternators.md), [power supplies and converters](07-power-supplies-and-converters.md), [the power grid](08-the-power-grid.md).
