# Lasers

**Type:** lesson

A laser is an optical amplifier inside a resonator. It emits a narrow, nearly parallel beam of light at one wavelength, and the light waves stay in step with each other. An engineer needs stimulated emission and beam behavior to choose a laser for cutting, measuring, or communication, and to handle one without injury.

**Prerequisites:** [Oscillations, waves, light, and heat](../../physics/07-waves-light-heat.md), [Atomic structure and bonding](../../materials/01-atomic-structure-bonding.md)
**Time:** 4-6 h

## Core ideas

### How it works

An atom can sit in an excited energy level. It can drop to a lower level on its own, which is spontaneous emission, and it emits a photon at random. A photon that passes near an excited atom can also trigger it to drop and emit a second photon. The new photon matches the first in direction, frequency, and phase. This is stimulated emission.

Normally most atoms sit in the lower level, and they absorb more light than they emit. A pump, which is electrical or optical energy, must move more atoms into the upper level than the lower one. This condition is called population inversion. In that state, stimulated emission beats absorption, and the medium amplifies light.

Two mirrors form an optical cavity around the gain medium. Light bounces back and forth through the medium and grows with each pass. One mirror transmits a small fraction of the light, and that fraction is the output beam. When the gain exceeds the losses, the laser starts emitting.

### Main parts

- **Gain medium.** A solid, liquid, gas, or semiconductor with energy levels that support population inversion.
- **Pump.** Electrical current, a flash lamp, or another laser that supplies the energy to excite the atoms.
- **Optical cavity.** Two mirrors, one partly transparent, that set the direction and the feedback.
- **Beam delivery.** Lenses, mirrors, or an optical fiber that carry the beam to the work and focus it.
- **Cooling.** Removes the heat the pump and the medium leave behind. Output and wavelength both shift with temperature.

### Variants

- **Solid state.** Ruby lasers emit at 694 nm. Nd:YAG lasers emit at 1064 nm and are common in cutting and marking.
- **Gas.** The helium-neon laser emits at 632.8 nm and is used in alignment and measurement. The carbon dioxide (CO$_2$) laser emits at 10.6 $\mu$m and is used for cutting wood, plastic, and some metals.
- **Semiconductor diodes.** Small and efficient. They power barcode readers, optical storage, and optical fiber links.
- **Fiber lasers.** A doped optical fiber is the gain medium. They emit near 1 $\mu$m and are used for industrial metal cutting.
- **Dye lasers.** A liquid dye is the gain medium, and the wavelength can be tuned across a wide range.

## Key equations

Photon energy, with $h = 6.626 \times 10^{-34}\ \text{J s}$, $c = 2.998 \times 10^8\ \text{m/s}$, and $\lambda$ in metres:

$$E = hf = \frac{hc}{\lambda}$$

Half-angle divergence of a Gaussian beam, with waist radius $w_0$ in metres (the $1/e^2$ radius of the intensity):

$$\theta = \frac{\lambda}{\pi w_0}$$

Rayleigh range, the distance over which the beam radius grows by $\sqrt{2}$:

$$z_R = \frac{\pi w_0^2}{\lambda}$$

Intensity at a focused spot, with power $P$ in watts and spot area $A$ in m$^2$, assuming a uniform disk:

$$I = \frac{P}{A}$$

Coherence length, with bandwidth $\Delta\lambda$ in metres. It sets how far apart two points on the beam can be and still interfere:

$$L_c = \frac{\lambda^2}{\Delta\lambda}$$

## Worked example

**Given:** A 1 kW laser cutter focuses its beam to a spot 0.1 mm in diameter. Assume all the power reaches the spot, and assume the spot is a uniform disk. The wavelength is 1064 nm.

**Find:** (a) the intensity at the spot in W/cm$^2$, (b) the energy of one photon in joules, and (c) the number of photons arriving per second.

**Solution:**

1. The spot radius is $r = 0.05\ \text{mm} = 5.0 \times 10^{-5}\ \text{m}$, so $A = \pi r^2 = 7.85 \times 10^{-9}\ \text{m}^2$.
2. $I = 1000 / (7.85 \times 10^{-9}) = 1.27 \times 10^{11}\ \text{W/m}^2 = 1.27 \times 10^7\ \text{W/cm}^2$.
3. $E = (6.626 \times 10^{-34})(2.998 \times 10^8) / (1064 \times 10^{-9}) = 1.87 \times 10^{-19}\ \text{J}$, which is 1.17 eV.
4. The photon rate is $1000 / (1.87 \times 10^{-19}) = 5.36 \times 10^{21}\ \text{s}^{-1}$.

**Answer:** (a) $1.27 \times 10^7\ \text{W/cm}^2$. (b) $1.87 \times 10^{-19}\ \text{J}$. (c) $5.36 \times 10^{21}$ photons per second.

**Sanity check:** Intensity, not power, decides what the beam does to a material. Halving the spot diameter quadruples the intensity. The photon energy of 1.17 eV is in the near-infrared, which is invisible, so a cutting laser gives no visible warning. The photon rate is huge, but the energy per photon is small, so the total power, not the photon count, sets the heating.

## Design trade-offs

- **Wavelength against absorption.** Metals absorb 1 $\mu$m light well, which suits fiber lasers for metal cutting. Organic materials absorb 10.6 $\mu$m light well, which suits CO$_2$ lasers for wood and plastic.
- **Beam quality against power.** A tight, low-divergence beam focuses to a small spot. Higher power often comes with a poorer beam, so the choice depends on the job.
- **Efficiency.** CO$_2$ lasers convert roughly 10 percent of wall power into light (typical value). Diode and fiber lasers are more efficient, so they need less cooling and less electrical power for the same output.
- **Depth of focus against spot size.** A small spot has a short Rayleigh range. The cutting head must stay within a few millimeters of the work for a clean cut.
- **Cost and size.** Diode lasers are small and cheap. High-power solid-state and gas lasers need larger power supplies and cooling systems.

## How it fails

- **Dirty or damaged optics.** Dust and scratches absorb light and heat up. The optic can crack, and output drops. Warning signs are falling power and scorch marks. Cleaning on a schedule and power monitors catch the problem early.
- **Back reflection into a diode.** Light reflected from the work travels back into a laser diode and can damage it. Optical isolators block the return path.
- **Overheating.** Insufficient cooling raises the medium's temperature. Diode wavelength shifts, and output falls. Temperature sensors and interlocks stop the laser before damage.
- **Eye injury.** Direct and specular reflections can injure the eye. Invisible wavelengths such as 1064 nm and 10.6 $\mu$m give no visible warning. Enclosures, interlocks, and goggles rated for the wavelength exist because of this.
- **Gradual aging.** Diode output falls slowly over thousands of hours. Power monitoring lets operators replace a laser before the job suffers.

## History

Einstein described stimulated emission in 1917. Charles Townes and Arthur Schawlow published the principles of a laser in 1958. Theodore Maiman built the first working laser, a ruby laser, at Hughes Research Laboratories in 1960. Gordon Gould coined the word "laser" in the late 1950s. Townes shared the 1964 Nobel Prize in Physics with Nicolay Basov and Aleksandr Prokhorov for work on masers and lasers.

## Practice

1. Find the photon energy in electronvolts of a helium-neon laser at 632.8 nm. Use $E\ (\text{eV}) = 1239.8 / \lambda\ (\text{nm})$.

   <details><summary>Answers</summary>

   $E = 1239.8 / 632.8 = 1.96\ \text{eV}$.

   </details>

2. A helium-neon beam at 632.8 nm starts with a waist radius of 0.5 mm. Find its half-angle divergence and its radius at 10 m.

   <details><summary>Answers</summary>

   $\theta = \lambda / (\pi w_0) = 0.403\ \text{mrad}$. The radius at 10 m is $\theta \times 10\ \text{m} = 4.0\ \text{mm}$.

   </details>

3. A 2 kW beam focuses to a spot 0.2 mm in diameter. Find the intensity in W/cm$^2$, assuming a uniform disk.

   <details><summary>Answers</summary>

   $A = \pi (0.1\ \text{mm})^2 = 3.14 \times 10^{-8}\ \text{m}^2$, so $I = 2000 / 3.14 \times 10^{-8} = 6.4 \times 10^{10}\ \text{W/m}^2 = 6.4 \times 10^6\ \text{W/cm}^2$.

   </details>

4. Why does a laser need population inversion?

   <details><summary>Answers</summary>

   Without inversion, most atoms sit in the lower level and absorb more light than the stimulated emission returns. The medium then loses light and cannot amplify it.

   </details>

## Common mistakes

- **Treating laser power as the whole story.** The spot size sets the intensity, so the same beam can cut or only mark a surface depending on focus.
- **Assuming a beam stays narrow forever.** The beam radius grows with distance. A 1 mm waist at 1064 nm grows to a beam radius of about 3.4 mm at 10 m, and the spread keeps increasing with distance.
- **Thinking a laser is just bright light.** Laser light is coherent and has a narrow wavelength band. Those properties matter for interference and for measurement.
- **Believing a red laser is safe because it is visible.** The power and wavelength set the hazard, not the color. Invisible infrared beams can cause the most damage because nobody flinches away from them.
- **Forgetting that reflections are hazardous.** A shiny surface can send a beam into the eye or onto a bystander, so the beam path needs enclosures and eye protection.

## Go deeper

- [University Physics Volume 3, Chapter 8.6, Lasers](https://openstax.org/books/university-physics-volume-3/pages/8-6-lasers) by OpenStax. Stimulated emission, population inversion, and laser applications.
- [Frequently Asked Questions About Lasers](https://www.fda.gov/radiation-emitting-products/laser-products-and-instruments/frequently-asked-questions-about-lasers) by the U.S. Food and Drug Administration. Hazard classes and laser safety guidance.
- Related: [Radio and antennas](02-radio-and-antennas.md), which uses the same wavelength and energy ideas at radio frequencies.
- [Applications reference](../reference.md): the lookup sheet for this topic.
