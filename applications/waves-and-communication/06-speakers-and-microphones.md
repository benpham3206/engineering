# Speakers and microphones: transduction, voice coils, and sound pressure level

**Type:** lesson

A loudspeaker turns an electrical signal into sound pressure, and a microphone does the reverse. Engineers need the force, motion, and pressure relations to size a speaker driver, pick a microphone, and set a level that is loud enough without distortion or hearing damage.

**Prerequisites:** [Electricity and magnetism](../../physics/06-electricity-and-magnetism.md), [Oscillations, waves, light, and heat](../../physics/07-waves-light-heat.md)
**Time:** 6-8 h

## Core ideas

### How it works

A dynamic loudspeaker has a coil of wire, the voice coil, sitting in the gap of a magnet. A current $I$ in the coil produces a force on it. The force is perpendicular to both the magnetic field and the wire. Because the coil is attached to a cone, the cone moves in and out and pushes the air. The moving air carries the pressure wave away as sound.

A dynamic microphone reverses the process. Sound pressure moves a diaphragm, which moves a coil in a magnet, and the moving coil produces a voltage. Both devices are transducers, because each converts one form of energy into another.

A condenser microphone uses a thin diaphragm close to a fixed plate. The two form a capacitor. Sound changes the gap, which changes the capacitance, and a bias voltage turns that change into a signal.

### Main parts

- **Magnet.** Neodymium or ferrite. It sets the field strength $B$ in the coil gap.
- **Voice coil.** Copper or aluminum wire wound on a former. It carries the signal current.
- **Cone or dome.** The light, stiff surface that moves air. Paper, polymer, and metal domes are common.
- **Surround and spider.** The flexible suspensions that return the cone to rest and keep the coil centered in the gap.
- **Frame and enclosure.** The frame holds the parts. The enclosure controls how the back of the cone radiates, which strongly affects the bass.
- **Microphone diaphragm.** A thin film that moves with sound pressure.
- **Preamplifier.** Raises the small microphone signal to a usable level. A condenser mic needs a bias supply, often 48 V phantom power.

### Variants

- **Speakers.** Woofers for low frequencies with large cones, midrange drivers, and tweeters for high frequencies with small domes. Dynamic, planar magnetic, and piezoelectric drivers each suit different bands.
- **Dynamic microphones.** Rugged, handle high sound pressure, and need no power. Used for vocals and loud sources.
- **Condenser microphones.** More sensitive and flatter in response. They need a bias supply and are used in studios and measurement.
- **Electret microphones.** Condenser designs with a permanently charged film. Inexpensive and common in phones and headsets.

## Key equations

- Lorentz force on the voice coil, with $B$ in tesla, wire length $l$ in metres, current $I$ in amperes, and force $F$ in newtons: $F = B\,l\,I$.
- Newton's second law for the moving assembly, with mass $m$ in kilograms and acceleration $a$ in metres per second squared: $a = F / m$.
- Motional emf in a microphone or in the back-emf of a speaker, with coil velocity $v$ in metres per second: $e = B\,l\,v$.
- Sound pressure level, in decibels, with rms pressure $p$ in pascals and the reference pressure $p_0 = 20\ \mu\text{Pa}$: $L_p = 20 \log_{10}(p / p_0)$.
- Acoustic intensity of a plane wave, in W/m$^2$: $I = p^2 / (\rho c)$, where $\rho = 1.2$ kg/m$^3$ is the density of air and $c = 343$ m/s is the speed of sound in air at about 20 °C (typical). The product $\rho c$ is about $412$ Pa s/m.
- Acoustic efficiency, dimensionless: $\eta = P_{\mathrm{acoustic}} / P_{\mathrm{electrical}}$.

Doubling the pressure raises the level by $20 \log_{10} 2 = 6.0$ dB. Doubling the acoustic power raises it by $10 \log_{10} 2 = 3.0$ dB.

## Worked example

**Given:** A voice coil has 8.0 m of wire in a magnetic field of $B = 1.0$ T. The current is $I = 2.0$ A. The moving mass, including the coil and cone, is 10 g. Ignore the load of the air.

**Find:** (a) the force on the coil, (b) its acceleration, and (c) the sound pressure level of a 0.10 Pa rms wave in air.

**Solution:**

1. Force: $F = B\,l\,I = 1.0 \times 8.0 \times 2.0 = 16$ N.
2. Acceleration: $a = F / m = 16 / 0.010 = 1600$ m/s$^2$. This is about $1600 / 9.81 = 163$ times the acceleration of gravity at Earth's surface.
3. Sound pressure level: $L_p = 20 \log_{10}\!\left(\dfrac{0.10}{20 \times 10^{-6}}\right) = 20 \log_{10}(5000) = 74.0$ dB.

**Answer:** (a) 16 N. (b) 1600 m/s$^2$. (c) 74 dB.

**Sanity check:** A 1.0 Pa rms wave is about 94 dB, and 0.10 Pa is one tenth of that pressure, which is 20 dB lower, giving 74 dB. The intensity is $I = (0.10)^2 / 412 = 2.4 \times 10^{-5}$ W/m$^2$, which is far above the hearing threshold of about $10^{-12}$ W/m$^2$, as expected for a 74 dB sound. An acceleration of 1600 m/s$^2$ is high, so the cone must stay light and stiff.

## Design trade-offs

- **Efficiency.** Most electrical power in a direct-radiating speaker becomes heat in the coil. Typical efficiency is only 1 to 3 percent. A 10 W amplifier driving a 1 percent efficient speaker produces 0.1 W of sound.
- **Bass versus size.** Low frequencies need a large cone area or a long excursion, and both need a larger enclosure. Compact speakers give up low bass.
- **Power handling.** The coil heats as current flows. Thermal limits set the continuous power rating, and wire gauge and cooling set how much power the coil can take.
- **Distortion.** The force $F = B\,l\,I$ depends on the coil staying in the gap. At large excursions, the field weakens and the force becomes nonlinear, which adds distortion.
- **Sensitivity versus noise.** Condenser microphones are more sensitive and flatter, but they need a bias supply and add their own electronic noise. Dynamic microphones are rugged, with lower output.
- **Directionality.** Cardioid microphones reject sound from the rear, which helps in noisy rooms, at the cost of more proximity effect in bass.

## How it fails

- **Voice coil overheating.** Sustained high power burns the insulation, and the coil can short. Clipping in the amplifier, which sends a high-energy square wave, is a common cause.
- **Overexcursion.** The cone moves past its linear range. The surround can tear, or the coil can hit the magnet gap and scrape.
- **Demagnetization.** Heat weakens a magnet. A coil that runs too hot for too long can cut the field permanently.
- **Microphone wind noise and pop.** Moving air hits the diaphragm and creates a low rumble. A foam or mesh windscreen reduces it.
- **Feedback.** A microphone near a speaker picks up the amplified sound, which loops and howls. Placement and gain limits fix it.
- **Hearing damage.** NIOSH recommends a limit of 85 dBA over an eight-hour day as a protection level. Playing sound above that level for long periods risks permanent hearing loss.

## History

Alexander Graham Bell patented the telephone in 1876, and its transmitter and receiver were both magnetic transducers. Thomas Edison built a carbon microphone for telephones about 1877. Edward W. Kellogg and Chester W. Rice of General Electric published the design of the moving-coil loudspeaker in 1925, and it became the basis of modern speakers. Gerhard Sessler and James West of Bell Labs developed the electret condenser microphone in 1962, which is now the most common microphone in phones and headsets.

## Practice

1. A voice coil has 6.0 m of wire in a field of 1.2 T and carries 1.5 A. Find the force.
2. A microphone in air sees a sound wave of 2.0 Pa rms. Find the sound pressure level.
3. A sound must reach 60 dB. Find the required rms pressure in pascals.
4. A cone of mass 15 g experiences a net force of 10 N. Find its acceleration.
5. Explain why doubling the sound pressure adds 6 dB, while doubling the acoustic power adds only 3 dB.

<details><summary>Answers</summary>

1. $F = 1.2 \times 6.0 \times 1.5 = 10.8$ N.
2. $L_p = 20 \log_{10}\!\left(\dfrac{2.0}{20 \times 10^{-6}}\right) = 100$ dB.
3. $p = 20\ \mu\text{Pa} \times 10^{60/20} = 0.020$ Pa.
4. $a = 10 / 0.015 = 667$ m/s$^2$.
5. Sound pressure level uses $20 \log_{10}$ of the pressure ratio. Acoustic power is proportional to the square of the pressure, so the power level uses $10 \log_{10}$. Doubling the pressure gives $20 \log_{10} 2 = 6.0$ dB, and doubling the power gives $10 \log_{10} 2 = 3.0$ dB.

</details>

## Common mistakes

- Using $10 \log_{10}$ for pressure. Sound pressure level uses $20 \log_{10}$.
- Using peak pressure in the level formula. The formula uses rms pressure.
- Forgetting that the reference pressure is $20\ \mu\text{Pa}$, not 1 Pa.
- Reading the amplifier power rating as the sound output. Efficiency is a few percent, so most of the power becomes heat.
- Judging a speaker by its cone size alone. The enclosure and the driver's suspension set much of the bass.

## Go deeper

- [University Physics Volume 1, Chapter 17: sound waves, intensity, and the Doppler effect](https://openstax.org/books/university-physics-volume-1/pages/17-introduction) by OpenStax. Free, with the sound background used here.
- [University Physics Volume 2, Chapter 11: magnetic force on a current-carrying conductor](https://openstax.org/books/university-physics-volume-2/pages/11-introduction) by OpenStax. Free, covering the force behind the voice coil.
- [University Physics Volume 2, Chapter 13: electromagnetic induction](https://openstax.org/books/university-physics-volume-2/pages/13-introduction) by OpenStax. Free, covering the emf that a moving coil produces.
- Related lessons: [Circuit basics](../electronics/01-circuit-basics.md), which covers the amplifier circuits that drive speakers, and [Electricity and magnetism](../../physics/06-electricity-and-magnetism.md).
- [Applications reference](../reference.md): the lookup sheet for this topic.
