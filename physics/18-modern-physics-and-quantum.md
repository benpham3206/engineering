# Modern physics and quantum mechanics

**Type:** lesson
**Verify:** strict

Modern physics is the pair of theories, special relativity and quantum mechanics, that replaced classical mechanics and electromagnetism where speeds approach the speed of light or where sizes shrink to atoms. Classical physics is not wrong in its home range, but transistors, LEDs, lasers, solar cells, MRI scanners, electron microscopes, and flash memory only work because of the rules that replaced it. An engineer who knows where classical physics stops can tell which part of a device needs the new rules and which part is still ordinary mechanics.

**Prerequisites:** [Particle dynamics](02-particle-dynamics.md) (energy and momentum), [Electricity and magnetism](06-electricity-and-magnetism.md), [Waves, light, and heat](07-waves-light-heat.md), [Algebra](../math/01-algebra.md)
**Time:** 8-10 h

## Core ideas

### Where classical physics stops

Classical physics fails in two regimes. It fails when a speed $v$ is a sizeable fraction of the **speed of light** $c$ (the fixed speed of light in vacuum, the same for every observer). It also fails when the **action** (energy times time, or momentum times distance) of a process is comparable to the **Planck constant** $h$, the fixed constant that sets the size of the quantum. Both constants are exact in the SI, listed in [constants](../data/constants.md).

Everyday machines sit far from both limits, so a car, a beam, or a pump needs neither theory. A device that works with single electrons, single photons, or spacings of a few nanometres does need quantum rules, and a clock in orbit needs relativity.

### Special relativity: time and mass-energy

**Special relativity** rests on two statements. The laws of physics are the same in every frame moving at constant velocity, and light in vacuum has the same speed $c$ in every such frame. Two results matter to engineers.

- **Time dilation.** A clock moving at speed $v$ relative to an observer ticks slower, by the factor $\gamma$ (the **Lorentz factor**), as that observer measures it. At everyday speeds the effect is tiny but never zero.
- **Mass-energy equivalence.** A body at rest holds energy $E_0 = m c^2$. Energy released or absorbed in a reaction shows up as a change in mass, which is how nuclear energy is accounted for below.

Gravity also slows clocks: a clock deeper in a gravitational field ticks slower than one higher up. This is a result of general relativity, which this lesson uses only in its weak-field form for the example.

**Engineering case, satellite navigation.** A navigation satellite carries an atomic clock, and a receiver finds its position from signal travel times, so a clock error $\Delta t$ becomes a range error $c\,\Delta t$. The satellite's speed slows its clock, and its height speeds it up relative to a ground clock. The two effects have opposite signs and unequal sizes, and the worked example computes both. The correction is large enough that a system built without it would drift by kilometres per day.

### Photons and the photoelectric effect

A **photon** is one quantum of light, with energy $E = h f$ where $f$ is the light frequency. The **photoelectric effect** is the ejection of electrons from a material by light. Classical wave theory predicts that brighter light should free electrons at any colour, and it does not. Instead no electrons leave if the photon energy is below the **work function** $\phi$ (the energy needed to free one electron), however bright the light. Above that threshold, brighter light frees more electrons, but each leaves with the same maximum kinetic energy $hf - \phi$.

The electron volt (eV) is the natural energy unit here: the energy gained by one electron through one volt, exactly $1.602\,176\,634 \times 10^{-19}$ J.

Photon absorption and emission are the working mechanism of solar cells (a photon lifts an electron to a conducting state), photodiodes and camera sensors (the same, read as a signal), and LEDs (an electron drops and emits a photon).

### Energy levels and spectra

In an isolated atom, an electron can have only certain energies, called **energy levels**. An atom absorbs or emits a photon only when the photon energy equals the gap between two levels. The set of photon energies an element emits or absorbs is its **spectrum**, and it is a fingerprint. Spectrometers use it to identify materials, and atomic clocks lock a signal to one such gap.

A **laser** works because an excited level can be made to release its photon on demand. Light of the right energy passing an excited atom stimulates it to emit a second photon with the same energy, direction, and phase. The device needs more atoms in the upper level than the lower one (a **population inversion**), which an ordinary lamp never has.

### Wave-particle duality and the de Broglie wavelength

**Wave-particle duality** means that light and matter show both wave behaviour (diffraction, interference) and particle behaviour (single detections). Every body with momentum $p$ has a **de Broglie wavelength** $\lambda = h/p$. For a baseball this wavelength is far below anything measurable, so classical mechanics works. For an electron accelerated through a few volts it is comparable to atomic spacings, so electrons diffract from crystals.

An **electron microscope** uses electrons whose de Broglie wavelength is far shorter than the wavelength of visible light, so it can resolve far finer detail. Its practical limit comes from lens aberrations, not from the wavelength.

### The uncertainty principle

The **Heisenberg uncertainty principle** says that position and momentum cannot both be known exactly. The spread $\Delta x$ in position and the spread $\Delta p$ in momentum obey $\Delta x\,\Delta p \ge \hbar/2$, where $\hbar = h/(2\pi)$. This is a property of waves, not a flaw in measuring instruments: a wave squeezed into a small region must contain a wide range of wavelengths. Pinning a particle in a small space forces a large minimum momentum, and so a minimum kinetic energy. That **confinement energy** is why atoms do not collapse and why a smaller box means higher energies.

### Particle in a box and tunneling

A **particle in a box** is a particle confined between two walls a distance $L$ apart. Only waves that fit, with a node at each wall, are allowed, so the energies are quantized: $E_n = n^2 h^2/(8 m L^2)$ for $n = 1, 2, 3, \dots$. A smaller box raises every level and widens the gaps. Semiconductor **quantum dots** use this: a smaller crystal emits a bluer photon.

A real wall is a finite barrier, and the wave leaks into it. **Tunneling** is the passage of a particle through a barrier it classically lacks the energy to cross. The transmission probability falls exponentially with barrier width, so a change of a tenth of a nanometre changes the current by nearly an order of magnitude. Engineers use this in three devices and fight it in a fourth.

- A **scanning tunneling microscope** holds a sharp tip a fraction of a nanometre above a surface and reads the tunnel current, which maps the surface atom by atom.
- **Flash memory** stores a bit as charge pushed through a thin oxide onto an isolated gate by tunneling. The charge stays for years because the oxide is a barrier, and it leaks away slowly when the oxide wears.
- A tunnel diode conducts by tunneling across a very thin junction.
- Modern transistors lose power to unwanted tunneling through gate oxides that are only a few atoms thick.

### Bands and band gaps in solids

When many atoms join into a crystal, their identical energy levels split and merge into nearly continuous **energy bands**, with forbidden gaps between them. The **band gap** $E_g$ is the energy gap between the top filled band (the **valence band**) and the empty band above it (the **conduction band**). A filled band cannot carry current, so the gap decides the material.

- A metal has a partly filled band, so electrons move freely.
- An insulator has a large gap, so almost no electrons reach the conduction band.
- A **semiconductor** has a moderate gap, so a little energy (heat, light, or doping) moves electrons across.

This one picture explains the engineering behaviour in [Semiconductors: diodes and transistors](../applications/electronics/03-semiconductors-diodes-and-transistors.md). Doping adds levels near a band edge, a junction bends the bands to make a diode, and a gate voltage moves the bands in a transistor. An LED emits a photon of energy close to $E_g$, so the gap sets its colour. A solar cell absorbs photons with energy above $E_g$, and the part of the photon energy above the gap becomes heat.

### Radioactive decay and binding energy

Quantum mechanics also governs the nucleus. An unstable nucleus changes into another by emitting radiation, and for one nucleus the moment of decay is random. For a large number of identical nuclei, the decay is exponential, and each species has a fixed **half-life** $t_{1/2}$, the time for half of any sample to decay.

The **binding energy** of a nucleus is the energy needed to pull it apart into separate protons and neutrons. By mass-energy equivalence it shows up as a **mass defect**: the nucleus weighs less than its parts. Binding energy per particle is largest near iron. Fusing light nuclei or splitting heavy ones moves matter toward that peak and releases the difference, which is the source of energy in [Nuclear reactors](../applications/energy/04-nuclear-reactors.md).

### Which technology depends on which idea

| Technology | Idea it depends on |
|---|---|
| Transistor, diode | Band structure, doping, junctions |
| LED | Band gap, photon emission |
| Solar cell, camera sensor | Photon absorption across a band gap, photoelectric effect |
| Laser | Discrete energy levels, stimulated emission |
| MRI | Quantized energy levels of nuclear spin in a magnetic field, absorbed and emitted as radio-frequency photons |
| Electron microscope | de Broglie wavelength of electrons |
| Scanning tunneling microscope | Tunneling |
| Flash memory | Tunneling through a thin oxide |
| Satellite navigation | Time dilation and gravitational clock shift |
| Nuclear reactor, radioisotope source | Binding energy, decay, mass-energy equivalence |

## Key equations

Symbols: $c$ = speed of light in vacuum (m/s), $h$ = Planck constant (J s), $\hbar = h/(2\pi)$ (J s), $v$ = speed (m/s), $m$ = mass (kg), $f$ = frequency (Hz), $\lambda$ = wavelength (m), $p$ = momentum (kg m/s), $\phi$ = work function (J or eV), $L$ = box width or barrier width (m), $U$ = barrier height (J), $E$ = particle energy (J), $N$ = number of undecayed nuclei, $t$ = time (s).

Time dilation, with $\Delta t_0$ the proper time on the moving clock and $\Delta t$ the time an observer measures:

$$
\gamma = \frac{1}{\sqrt{1 - v^2/c^2}}, \qquad \Delta t = \gamma\,\Delta t_0
$$

For $v \ll c$, a moving clock falls behind by the fraction $v^2/(2c^2)$. In a weak gravitational field, a clock at distance $r$ from the centre of a body of gravitational parameter $\mu = G M$ (m$^3$/s$^2$) runs fast relative to one at $R < r$ by the fraction $\mu(1/R - 1/r)/c^2$. Both approximations hold when $v \ll c$ and $\mu/(r c^2) \ll 1$, and break near black holes or for relativistic speeds.

Mass-energy and binding energy, with $\Delta m$ the mass defect (kg):

$$
E_0 = m c^2, \qquad E_b = \Delta m\,c^2
$$

Photon energy and the photoelectric effect, with $K_\text{max}$ the maximum kinetic energy of an ejected electron (J):

$$
E = h f = \frac{h c}{\lambda}, \qquad K_\text{max} = h f - \phi
$$

The relation holds when $hf \ge \phi$. For $hf < \phi$ no electrons are ejected.

de Broglie wavelength, and for an electron of mass $m$ accelerated from rest through a potential difference $V_a$ (V) with charge $e$ (C), at speeds well below $c$:

$$
\lambda = \frac{h}{p}, \qquad \lambda = \frac{h}{\sqrt{2 m e V_a}}
$$

The second form breaks when the electron energy approaches $m c^2$, where the relativistic momentum is needed.

Uncertainty principle, and the particle in a box with infinite walls:

$$
\Delta x\,\Delta p \ge \frac{\hbar}{2}, \qquad E_n = \frac{n^2 h^2}{8 m L^2}
$$

The box formula holds for walls high enough to confine the particle and breaks for shallow wells, where the wave leaks out.

Tunneling through a rectangular barrier of height $U > E$ and width $L$:

$$
T \approx e^{-2\kappa L}, \qquad \kappa = \frac{\sqrt{2 m (U - E)}}{\hbar}
$$

This holds when $\kappa L \gg 1$ (a thick or tall barrier) and breaks for thin barriers, where the prefactor matters.

Radioactive decay:

$$
N = N_0\,2^{-t/t_{1/2}}
$$

## Worked example

**Clock offset of a navigation satellite.** A satellite in a circular orbit of radius 26 560 km (about a twelve-hour orbit) carries a clock. Find the net daily offset of the satellite clock relative to a clock at the surface of Earth, and the range error it would cause in one day if uncorrected.

**Given:** orbit radius $r = 2.656 \times 10^{7}$ m, Earth mean radius $R = 6.371 \times 10^{6}$ m, Earth's gravitational parameter $\mu = 3.986004 \times 10^{14}$ m$^3$/s$^2$, $c$ from the constants table, one day $= 1$ d.

**Find:** the speed effect, the gravity effect, the net offset in $\mu$s per day, and the range error in km.

**Assumptions:** circular orbit, weak-field and low-speed approximations, a spherical non-rotating Earth with the ground clock at rest. Earth's rotation moves the ground clock slowly and shifts the result by a small fraction of a microsecond per day, which this example ignores.

**Solution:**

1. Orbital speed: $v = \sqrt{\mu/r} = 3874$ m/s. The period $2\pi\sqrt{r^3/\mu}$ is 11.97 h, which checks the twelve-hour description.
2. Speed effect: the fraction $-v^2/(2c^2) = -8.349 \times 10^{-11}$. Over one day this is $-7.21\ \mu$s.
3. Gravity effect: the fraction $+\mu(1/R - 1/r)/c^2 = 5.291 \times 10^{-10}$. Over one day this is $+45.72\ \mu$s.
4. Net: $45.72 - 7.21 = +38.50\ \mu$s per day. The satellite clock runs fast.
5. Range error in one day: $c \times 38.50\ \mu\text{s} = 11.54$ km.

**Answer:** the satellite clock gains about 38.5 $\mu$s per day, which would grow into a range error of about 11.5 km per day if left uncorrected.

**Sanity check:** the gravity term dominates because the satellite is high above the surface, and its sign is opposite to the speed term. The speed effect is the fractional size $v^2/(2c^2)$, a few parts in ten billion, so a day (86 400 s) gives microseconds, not milliseconds.

<details><summary>Verification</summary>

```verify
r = q(2.656e7, "m")
R = q(6.371e6, "m", of="r_earth_mean")
mu = q(3.986004e14, "m^3/s^2", of="gm_earth")
c = const("c")
given("86400", "26560")
v = sqrt(mu / r)
expect(v, "3874 m/s")
T = 2 * pi * sqrt(r**3 / mu)
expect(T, "11.97 h")
speed_frac = -v**2 / (2 * c**2)
expect(speed_frac * 1e11, "-8.349")
speed_day = speed_frac * q(1, "d")
expect(speed_day, "-7.21 us")
grav_frac = mu * (1 / R - 1 / r) / c**2
expect(grav_frac * 1e10, "5.291")
grav_day = grav_frac * q(1, "d")
expect(grav_day, "45.72 us")
net = speed_day + grav_day
expect(net, "38.50 us")
expect(c * net, "11.54 km")
expect(c * net, "11.5 km")
check(grav_day > -speed_day, "gravity effect dominates and the signs oppose")
check(net > q(0, "s"), "satellite clock runs fast")
```

</details>

## Practice

1. Light of wavelength 300 nm falls on a metal with work function 2.30 eV. Find the photon energy and the maximum kinetic energy of the ejected electrons, in eV.
2. An electron is accelerated from rest through 100 V. Find its de Broglie wavelength in nm, using the non-relativistic form. Take the electron mass as $9.1093837 \times 10^{-31}$ kg.
3. An electron is confined in a box of width 1.00 nm with infinite walls. Find the ground-state energy $E_1$ in eV, and the wavelength in $\mu$m of the photon emitted when the electron drops from $n = 2$ to $n = 1$.
4. An electron meets a barrier 0.50 nm wide whose top is 4.00 eV above the electron energy. Estimate the transmission probability. Then find the factor by which the tunnel current falls when the gap widens by 0.10 nm.
5. A radioactive sample has half-life 10.0 h. (a) Find the fraction left after 36.0 h. (b) A nuclear reaction has a mass defect of $3.0 \times 10^{-29}$ kg. Find the energy released in MeV. Explain which method you used for each part.

<details><summary>Answers</summary>

1. Photon energy 4.13 eV; maximum kinetic energy 1.83 eV.
2. 0.123 nm.
3. $E_1 = 0.376$ eV; the photon wavelength is 1.10 $\mu$m, in the infrared.
4. $T \approx 3.5 \times 10^{-5}$; the current falls by a factor of 7.8.
5. (a) 0.0825, using the half-life form $2^{-t/t_{1/2}}$ directly. (b) 16.8 MeV, using $E_b = \Delta m\,c^2$ and converting joules to MeV.

```verify
h = const("h_planck")
c = const("c")
e = const("e_charge")
m = q(9.1093837e-31, "kg", of="m_electron")
hbar = h / (2 * pi)
Eph = h * c / q(300, "nm")
expect(Eph, "4.13 eV", ans=1)
expect(Eph - q(2.30, "eV"), "1.83 eV", ans=1)
expect(h / sqrt(2 * m * e * q(100, "V")), "0.123 nm", ans=2, rel=0.005)
E1 = h**2 / (8 * m * q(1.00, "nm")**2)
expect(E1, "0.376 eV", ans=3)
expect(h * c / (3 * E1), "1.10 um", ans=3)
kappa = sqrt(2 * m * q(4.00, "eV")) / hbar
T = exp(-2 * kappa * q(0.50, "nm"))
expect(T * 1e5, "3.5", ans=4)
expect(exp(2 * kappa * q(0.10, "nm")), "7.8", ans=4)
expect(2 ** (-q(36.0, "h") / q(10.0, "h")), "0.0825", ans=5)
expect(q(3.0e-29, "kg") * c**2, "16.8 MeV", ans=5)
```

</details>

## Common mistakes

- Treating light intensity as the cause of photoelectron energy. Intensity sets how many electrons leave, and frequency sets how much energy each carries.
- Applying the non-relativistic de Broglie form $h/\sqrt{2meV_a}$ to electrons accelerated through tens of kilovolts or more, where relativistic momentum changes the result noticeably.
- Reading the uncertainty principle as measurement disturbance. It is a limit on how sharply a wave can be both localized and of one wavelength, even for an ideal measurement.
- Forgetting that tunneling is exponential in barrier width, so a small change in a gap or oxide thickness changes a current by a large factor.
- Treating a band gap as a single sharp threshold at all temperatures. The gap shifts with temperature, and thermal energy moves some electrons across even below it.

## Go deeper

- [University Physics Volume 3](https://openstax.org/details/books/university-physics-volume-3) by OpenStax: free textbook chapters on relativity, photons and matter waves, quantum mechanics, atomic structure, condensed matter, and nuclear physics.
- [Quantum Physics I (8.04)](https://ocw.mit.edu/courses/8-04-quantum-physics-i-spring-2016/) by MIT OpenCourseWare: free lectures and problem sets on waves, the uncertainty principle, and tunneling.
- [Fundamental Physical Constants](https://physics.nist.gov/cuu/Constants/) by NIST: the values of $h$, $c$, and $e$ used here.
- Related lessons: [Semiconductors: diodes and transistors](../applications/electronics/03-semiconductors-diodes-and-transistors.md), [Nuclear reactors](../applications/energy/04-nuclear-reactors.md), [Quantum technologies](../applications/electronics/08-quantum-technologies.md), [Orbital mechanics and rockets](15-orbital-mechanics-and-rockets.md).
- [Fields, waves, and space reference](reference-fields-waves-space.md): the lookup sheet for this area.
