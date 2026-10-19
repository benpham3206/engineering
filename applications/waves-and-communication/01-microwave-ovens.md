# Microwave ovens

**Type:** lesson

A **microwave oven** is a kitchen appliance that heats food with a 2.45 GHz electromagnetic wave. An engineer who designs or repairs one must get the heating pattern right, because uneven heating leaves cold spots in food.

Water molecules in the food absorb energy from that wave and turn it into heat. An engineer needs the physics of the magnetron, the metal cavity, and the standing wave pattern, because those set how evenly food heats and how well the oven keeps the energy inside.

**Prerequisites:** [Electricity and magnetism](../../physics/06-electricity-and-magnetism.md), [Oscillations, waves, light, and heat](../../physics/07-waves-light-heat.md)
**Time:** 4-6 h

## Core ideas

### How it works

The oven moves energy through a chain of steps. A transformer and a high-voltage capacitor raise the mains voltage to a few kilovolts. The magnetron converts that electrical power into a microwave field at 2.45 GHz. A waveguide carries the field into the metal cavity, where the walls reflect it until the field fills the box as a standing wave pattern. Food in the cavity absorbs part of the field.

Heating happens by **dielectric loss**. A water molecule has a permanent electric dipole, so the field pulls on it and tries to turn it. The field reverses about 2.45 billion times per second. The molecule cannot keep up, and its motion is damped by its neighbors. That damping turns energy into heat. Dissolved salt adds a second effect: ions drift back and forth in the field and heat the liquid.

The field loses strength as it enters food. Most of the heating happens in the outer one to two centimeters. The center warms afterward, by conduction from the outside.

### Main parts

- **Magnetron.** A vacuum tube with a cathode, a ring of resonant cavities, and a permanent magnet. It produces the microwave power, typically about 1 kW in a home oven.
- **High-voltage supply.** A transformer and a diode feed a high-voltage capacitor. The capacitor can hold a dangerous charge after the oven is unplugged.
- **Waveguide.** A metal channel sized for 2.45 GHz. It carries the wave from the magnetron to the cavity.
- **Cavity.** A metal box whose walls reflect microwaves. Its dimensions set the standing wave pattern.
- **Stirrer and turntable.** A rotating metal blade changes the field pattern, and the turntable moves food through it. Both average out the hot spots.
- **Door screen and interlock.** The screen is a metal mesh with holes much smaller than the 12 cm wavelength. Light passes through it, but microwaves do not. Switches cut power when the door opens.

### Variants

- **Countertop ovens.** The common home type at 2.45 GHz. Typical microwave output is 700 W to 1200 W.
- **Combination ovens.** Add heating elements or a convection fan to the microwave function.
- **Industrial microwave systems.** Often use 915 MHz, which penetrates deeper into thick loads. They dry, heat, and process bulk material. A lower frequency needs a larger cavity.

## Key equations

Free-space wavelength, with $c = 2.998 \times 10^8\ \text{m/s}$ and $f$ in hertz:

$$\lambda_0 = \frac{c}{f}$$

Wavelength inside a material, with relative permittivity $\varepsilon_r = \varepsilon' - j\varepsilon''$ (both dimensionless):

$$\lambda_m = \frac{\lambda_0}{\operatorname{Re}\sqrt{\varepsilon_r}}$$

Power absorbed per unit volume, in W/m$^3$, with $\varepsilon_0 = 8.85 \times 10^{-12}\ \text{F/m}$ and $E$ the rms electric field in V/m:

$$p = 2\pi f\, \varepsilon_0\, \varepsilon''\, E^2$$

**Penetration depth**, the distance over which the power falls to $1/e$:

$$d_p = \frac{\lambda_0}{2\pi\sqrt{2\varepsilon'}}\left[\sqrt{1+\left(\frac{\varepsilon''}{\varepsilon'}\right)^2}-1\right]^{-1/2}$$

Heat needed to warm food, with mass $m$ in kg, specific heat $c_p$ in J/(kg K), and $\Delta T$ in K. Water has $c_p \approx 4186\ \text{J/(kg K)}$ (typical value):

$$Q = m\, c_p\, \Delta T$$

**Relaxation frequency** of water, with relaxation time $\tau$ in seconds:

$$f_r = \frac{1}{2\pi\tau}$$

## Worked example

**Given:** $f = 2.45\ \text{GHz}$. Water at 20 to 25 C has $\varepsilon' \approx 78$ and $\varepsilon'' \approx 10$ at this frequency (typical values).

**Find:** (a) the free-space wavelength, (b) the wavelength inside water, (c) the spacing of standing-wave maxima in the empty cavity, and (d) the penetration depth in water.

**Solution:**

1. $\lambda_0 = (2.998 \times 10^8) / (2.45 \times 10^9) = 0.1224\ \text{m}$, or 12.2 cm.
2. $\sqrt{78 - 10j} = 8.85 - 0.56j$, so $\operatorname{Re}\sqrt{\varepsilon_r} = 8.85$. Then $\lambda_m = 0.1224 / 8.85 = 0.01383\ \text{m}$, or 1.38 cm.
3. Adjacent maxima of a standing wave are half a wavelength apart. In air, that spacing is $\lambda_0 / 2 = 6.12\ \text{cm}$.
4. $d_p = \dfrac{0.1224}{2\pi\sqrt{156}}\left[\sqrt{1+0.0164}-1\right]^{-1/2} = 0.01725\ \text{m}$, or 1.7 cm.

**Answer:** (a) 12.2 cm. (b) 1.38 cm. (c) 6.12 cm. (d) 1.7 cm.

**Sanity check:** The wavelength in water is about nine times shorter than in air, which matches $\sqrt{78} \approx 8.8$. The penetration depth is about one wavelength in water, so the wave dies out within a couple of centimeters of the surface. The 6.12 cm spacing describes the empty cavity. Food changes the pattern, and the turntable averages the result.

## Design trade-offs

- **Frequency.** 2.45 GHz magnetrons are cheap and produced in large numbers. The frequency sits in the **industrial, scientific, and medical (ISM) band** from 2.400 to 2.500 GHz. A lower frequency such as 915 MHz penetrates deeper but needs a bigger cavity.
- **Power and efficiency.** A typical home oven draws about 1.7 kW from the wall to make 1.0 kW of microwave output. That is about 59 percent overall, and the rest becomes waste heat in the magnetron and power supply.
- **Even heating.** A stirrer, a turntable, or both spread the field. Mechanical parts add cost and wear, so some ovens use only one.
- **Leakage and shielding.** The door screen must block microwaves while letting people see food. Gaps in the seal add cost and leak energy, so the design keeps every gap far smaller than the wavelength.

## How it fails

- **Damaged door or seal.** Bent hinges, cracked glass, or a worn gasket open a path for microwaves. The US Food and Drug Administration limits leakage over an oven's life to 5 mW/cm$^2$ at about 5 cm from the surface. Warning signs are a door that does not seal flush and visible damage. Interlock switches and the leakage standard exist because of this failure.
- **Running empty.** With no food to absorb the power, most of it reflects back to the magnetron. Repeated reflection can damage the magnetron.
- **Metal in the cavity.** Sharp metal edges concentrate the field and cause arcing. The warning sign is sparking.
- **Superheated liquid.** Water heated in a smooth cup can rise above its boiling point and erupt when disturbed. The FDA reports serious scalds from this. Stirring the liquid partway through heating and heating in short bursts reduce the risk.

> [!WARNING]
> **Stored high voltage.** The high-voltage capacitor stays charged after unplugging. Only a trained technician should open the case.

## History

Randall and Boot at the University of Birmingham developed the cavity magnetron in 1940 for radar. It made high-power microwaves practical for the first time. In 1945 Percy Spencer at Raytheon noticed that a candy bar near an active magnetron had melted. Raytheon sold the first commercial microwave oven, the Radarange, in 1947, and it was large and costly. Amana introduced a countertop model in 1967, and that made microwave cooking practical in homes.

## Practice

1. Find the free-space wavelength of a 2.45 GHz wave.

   <details><summary>Answers</summary>

   $\lambda_0 = (2.998 \times 10^8) / (2.45 \times 10^9) = 0.122\ \text{m}$, or 12.2 cm.

   </details>

2. A 600 W absorbed power heats 250 g of water from 20 C to 100 C. Find the time. Use $c_p = 4186\ \text{J/(kg K)}$.

   <details><summary>Answers</summary>

   $Q = 0.25 \times 4186 \times 80 = 83\,720\ \text{J}$, so $t = 83\,720 / 600 = 140\ \text{s}$, or about 2.3 min.

   </details>

3. Water's relaxation time is about 8.3 ps at 25 C. Find its relaxation frequency, and find the ratio of 2.45 GHz to that frequency.

   <details><summary>Answers</summary>

   $f_r = 1 / (2\pi \times 8.3 \times 10^{-12}) = 19.2\ \text{GHz}$. The ratio is $2.45 / 19.2 = 0.13$. The oven frequency sits far below the relaxation peak.

   </details>

4. An oven draws 1.7 kW from the wall and produces 1.0 kW of microwave output. Find the efficiency.

   <details><summary>Answers</summary>

   $1.0 / 1.7 = 0.59$, or 59 percent.

   </details>

## Common mistakes

- **Saying microwaves resonate with water molecules.** They do not. The oven frequency is far below the water relaxation frequency of about 19 GHz. Heating comes from molecules lagging a field that reverses too fast for them to follow, which is a broad loss and not a resonance.
- **Saying microwaves heat food from the inside out.** The outer one to two centimeters heat first, and the center warms by conduction.
- **Expecting frozen food to heat quickly.** Ice holds its water molecules in a fixed lattice, so it absorbs much less energy at 2.45 GHz than liquid water does.
- **Assuming the turntable makes heating perfectly even.** It averages the pattern, but thick food still heats unevenly.
- **Running the oven empty or using metal in it.** Both can damage the oven, and metal can start arcing.

## Go deeper

- [*University Physics Volume 2*, Chapter 16.5, The electromagnetic spectrum](https://openstax.org/books/university-physics-volume-2/pages/16-5-the-electromagnetic-spectrum) by OpenStax. Where microwaves sit among the other electromagnetic waves.
- [Microwave Ovens](https://www.fda.gov/radiation-emitting-products/resources-you-radiation-emitting-products/microwave-ovens) by the U.S. Food and Drug Administration. Leakage limits and consumer safety guidance.
- Next: [Radio and antennas](02-radio-and-antennas.md), which uses the same wave equations at lower frequencies.
- [Applications reference](../reference.md): the lookup sheet for this topic.
