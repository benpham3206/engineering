# Radio and antennas

**Type:** lesson

**Radio and antennas** are the parts of a link that turn information into electromagnetic waves and recover it at a receiver. A weak received signal can be lost in noise, so an engineer must size the antenna to the wavelength and check the link budget.

**Prerequisites:** [Electricity and magnetism](../../physics/06-electricity-and-magnetism.md), [Oscillations, waves, light, and heat](../../physics/07-waves-light-heat.md)
**Time:** 4-6 h

## Core ideas

### How it works

A transmitter drives alternating current at radio frequency into an antenna. Charges that accelerate in the conductor radiate electromagnetic waves, and those waves travel at the speed of light. A receiving antenna captures a tiny fraction of the wave and converts it back into a small alternating voltage.

The information rides on a **carrier wave**, and this step is called **modulation**. **Amplitude modulation (AM)** changes the strength of the carrier. **Frequency modulation (FM)** changes its frequency. Digital systems change amplitude and phase together. The carrier frequency sets the wavelength, and the wavelength sets the antenna size.

### Main parts

- **Transmitter.** An oscillator produces the carrier, and a modulator puts the signal on it. A power amplifier raises the power.
- **Feed line.** A coaxial cable or a printed line carries the signal to the antenna. Its impedance must match the antenna's, or part of the power reflects back.
- **Antenna.** A conductor, or an arrangement of conductors, sized to the wavelength. It converts the feed signal into a radiated wave, and the reverse on receive.
- **Receiver.** A filter selects the wanted frequency, an amplifier raises the weak signal, and a demodulator recovers the information.

### Variants

- **Dipole.** Two conductors, each a quarter wavelength long, fed at the center. Common for broadcast and for simple links.
- **Monopole.** A quarter-wave element over a ground plane. Car radio and many handheld antennas use this form.
- **Yagi.** A driven element with a reflector behind it and directors in front. It gives directional gain for television and point-to-point links.
- **Patch.** A flat metal plate over a ground plane. Phones and Wi-Fi equipment use patches because they fit in a thin case.
- **Parabolic dish.** A reflector focuses the wave into a narrow beam. Satellite dishes and radio telescopes use dishes.
- **Phased array.** Many small elements, each with its own phase shift. The beam steers without moving parts. Radar and some 5G base stations use phased arrays.

## Key equations

Wavelength, with $c = 2.998 \times 10^8\ \text{m/s}$ and $f$ in hertz:

$$\lambda = \frac{c}{f}$$

Length of a resonant dipole, with $\lambda$ in metres. Real wire dipoles are about 95 percent of the ideal length because the ends shorten the electrical length:

$$L_{\text{dipole}} \approx 0.95\,\frac{\lambda}{2}$$

Friis free-space equation, with received power $P_r$ and transmitted power $P_t$ in watts, linear gains $G_t$ and $G_r$ (dimensionless), and distance $d$ in metres:

$$P_r = P_t\, G_t\, G_r \left(\frac{\lambda}{4\pi d}\right)^2$$

The same link in decibels, with powers in dBm, gains in dBi, and free-space loss $L_{\mathrm{fs}}$ in dB:

$$P_r\,(\text{dBm}) = P_t\,(\text{dBm}) + G_t\,(\text{dBi}) + G_r\,(\text{dBi}) - L_{\mathrm{fs}}\,(\text{dB})$$

$$L_{\mathrm{fs}} = 20\log_{10}\!\left(\frac{d}{\text{km}}\right) + 20\log_{10}\!\left(\frac{f}{\text{MHz}}\right) + 32.44$$

**Shannon capacity**, with bandwidth $B$ in hertz and signal-to-noise ratio $S/N$ as a plain ratio (not decibels):

$$C = B\log_2\!\left(1 + \frac{S}{N}\right)$$

## Worked example

**Given:** A 2.4 GHz Wi-Fi link covers 100 m in free space. The transmitter outputs 20 dBm (100 mW). Each antenna has a gain of 2 dBi.

**Find:** (a) the wavelength, (b) the ideal and practical half-wave dipole lengths, (c) the free-space loss, and (d) the received power in dBm and in watts.

**Solution:**

1. $\lambda = (2.998 \times 10^8) / (2.4 \times 10^9) = 0.1249\ \text{m}$, or 12.5 cm.
2. The ideal half-wave dipole is $\lambda/2 = 6.25\ \text{cm}$. The practical dipole is $0.95 \times 6.25 = 5.9\ \text{cm}$.
3. $L_{\mathrm{fs}} = 20\log_{10}(0.1) + 20\log_{10}(2400) + 32.44 = -20 + 67.60 + 32.44 = 80.04\ \text{dB}$.
4. $P_r = 20 + 2 + 2 - 80.04 = -56.0\ \text{dBm}$. Converting, $10^{-5.6}\ \text{mW} = 2.5\ \text{nW}$.

**Answer:** (a) 12.5 cm. (b) 6.25 cm ideal, 5.9 cm practical. (c) 80 dB. (d) $-56$ dBm, which is 2.5 nW.

**Sanity check:** A Wi-Fi receiver typically works down to about $-70$ to $-90$ dBm (typical values), so $-56$ dBm leaves a margin. Doubling the distance adds 6 dB of loss, so the link would drop to about $-62$ dBm at 200 m. Walls and furniture add losses that the Friis equation does not count, so indoor links are weaker than this estimate.

## Design trade-offs

- **Size against frequency.** An FM dipole at 100 MHz is about 1.5 m long. A 2.4 GHz antenna fits on a circuit board. The price of a small antenna at high frequency is more path loss for the same gain.
- **Gain against coverage.** A dish with high gain focuses the power into a narrow beam. It works only when both ends point at each other.
- **Bandwidth against efficiency.** A wide-band antenna covers more channels, but it usually has lower gain and more loss.
- **Power against battery and rules.** Higher transmit power extends range, but it drains batteries and must stay within regulated limits.
- **Phone design.** Phone antennas must fit inside a metal and glass case. The hand and the case shift the resonance, so designers tune the antenna with the case in place.

## How it fails

- **Mismatch.** A poor match between the antenna and the feed line reflects power back to the transmitter. The warning sign is a high **standing-wave ratio (SWR)**, and the fix is a matching network or a corrected length.
- **Detuning.** A nearby object, a hand, or a damaged element moves the resonance. The signal weakens without any change in the electronics.
- **Multipath fading.** A signal that arrives by two paths with different delays can cancel itself at some frequencies and places. Receivers use diversity antennas and equalizers to handle it.
- **Interference.** Another transmitter on the same frequency raises the noise. Spectrum licensing and channel plans reduce this.
- **Lightning and mast failure.** Tall antennas attract lightning, and guy wires or bases can fail under wind and ice. Grounding, lightning arrestors, and inspection schedules exist because of these failures.

> [!WARNING]
> **Excess exposure.** Radiation close to a powerful antenna can heat tissue. Regulators limit exposure, and installers keep public access away from high-power antennas.

## History

James Clerk Maxwell predicted electromagnetic waves in the 1860s, and his equations showed that they travel at the speed of light. Heinrich Hertz produced and detected such waves in laboratory experiments starting in 1887. Guglielmo Marconi sent a radio signal across the Atlantic in 1901, from Cornwall to Newfoundland. Edwin Armstrong demonstrated wideband frequency modulation in 1933, and FM reduced static in broadcasting.

## Practice

1. Find the wavelength of an FM signal at 98 MHz, and find the ideal half-wave dipole length.

   <details><summary>Answers</summary>

   $\lambda = (2.998 \times 10^8) / (98 \times 10^6) = 3.06\ \text{m}$. The ideal dipole is $3.06 / 2 = 1.53\ \text{m}$.

   </details>

2. Find the ideal quarter-wave monopole length for a 146 MHz signal.

   <details><summary>Answers</summary>

   $\lambda = 2.054\ \text{m}$. The quarter wavelength is $2.054 / 4 = 0.513\ \text{m}$.

   </details>

3. A channel of 10 MHz has a signal-to-noise ratio of 30 dB, which is a ratio of 1000. Find the Shannon capacity.

   <details><summary>Answers</summary>

   $C = 10 \times 10^6 \times \log_2(1001) = 99.7\ \text{Mb/s}$.

   </details>

4. Doubling the distance of a free-space link with fixed antenna gains changes the loss by how many decibels?

   <details><summary>Answers</summary>

   6 dB. The loss rises with the square of distance, and $20\log_{10}(2) = 6.02$.

   </details>

## Common mistakes

- **Cutting a dipole to a full wavelength.** A dipole is half a wavelength, and a real wire is about 95 percent of that.
- **Mixing dBm, dBi, and dBW.** A gain in dBi is not a power, and a power in dBm is not a gain. Convert everything to dB before adding.
- **Using the free-space equation indoors.** Walls, floors, and furniture add loss, so the real signal is weaker than the Friis estimate.
- **Assuming higher frequency always reaches farther.** With fixed antenna gains, path loss grows with frequency squared. Higher frequencies need more gain or closer spacing to match the range.
- **Treating gain as extra power.** Gain focuses the power that the transmitter already provides. It does not create power.

## Go deeper

- [*University Physics Volume 2*, Chapter 16.1, Maxwell's equations and electromagnetic waves](https://openstax.org/books/university-physics-volume-2/pages/16-1-maxwells-equations-and-electromagnetic-waves) by OpenStax. Maxwell's theory and Hertz's experiments.
- [*University Physics Volume 2*, Chapter 16.5, The electromagnetic spectrum](https://openstax.org/books/university-physics-volume-2/pages/16-5-the-electromagnetic-spectrum) by OpenStax. The radio bands among the other electromagnetic waves.
- Related: [Microwave ovens](01-microwave-ovens.md), which uses the same wave equations at 2.45 GHz, and [Lasers](03-lasers.md), which uses the same wavelength and energy ideas at optical frequencies.
- [Applications reference](../reference.md): the lookup sheet for this topic.
