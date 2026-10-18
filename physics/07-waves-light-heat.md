# Oscillations, waves, light, and heat

**Type:** lesson

Oscillations, waves, and light show up in almost every machine: springs and suspensions, sound and vibration in structures, sensors that use light, and the temperature and heat that decide how a part behaves.
**Prerequisites:** [02-particle-dynamics.md](02-particle-dynamics.md) (forces and Newton's second law)
**Time:** 8-12 h

## Core ideas

### Oscillation

- An **oscillation** is a motion that repeats back and forth around an equilibrium position.
- The **period** $T$ is the time for one full cycle, in seconds (s).
- The **frequency** $f$ is the number of cycles per second, in hertz (Hz). The two are linked by $f = 1/T$.
- The **amplitude** $A$ is the largest displacement from equilibrium, in the same units as the displacement (meters, m, for a spring).
- In **simple harmonic motion** (SHM), the restoring force is proportional to the displacement. A mass on an ideal spring is the standard example.
- The **angular frequency** $\omega$ is in radians per second (rad/s). It is linked to the frequency by $\omega = 2\pi f$.

### Waves

- A **wave** carries energy from one place to another without carrying the material along with it.
- A **transverse wave** moves the medium at right angles to the direction of travel. A wave on a stretched string is an example.
- A **longitudinal wave** moves the medium along the direction of travel. Sound in air is an example.
- The **wavelength** $\lambda$ is the distance over which the wave pattern repeats, in meters.
- The **wave speed** $v$ is how fast the pattern moves. It is linked to the others by $v = f\lambda$.
- Wave speed depends on the medium. The source sets the frequency, which stays the same when the wave enters a new medium.

### Standing waves and resonance

- A **standing wave** forms when two waves of the same frequency travel in opposite directions and interfere.
- A string fixed at both ends has standing waves when its length is a whole number of half-wavelengths.
- **Resonance** happens when a driving frequency matches a natural frequency. The response becomes large. Bridges, engines, and musical instruments all need to avoid or use it on purpose.

### Light

- Light is an electromagnetic wave. In vacuum it travels at $c \approx 3.00 \times 10^{8}$ m/s (metres per second, the speed of light).
- The **index of refraction** $n$ of a material is $n = c/v$, where $v$ is the speed of light in that material. Water has $n \approx 1.33$. Common glass has $n \approx 1.5$.
- When light crosses a boundary between two materials, it bends. This is **refraction**. The bending follows Snell's law.
- Frequency stays the same when light enters a new medium. The wavelength gets shorter by the factor $n$.

### Temperature and heat

- **Temperature** measures how hot or cold something is. It tells you the direction heat will flow. Heat flows from higher to lower temperature.
- **Heat** $Q$ is energy that moves across a boundary because of a temperature difference. It is measured in joules (J). Heat is not stored in a body. Work and heat are both ways of moving energy.
- The **Kelvin** scale starts at absolute zero, the lowest possible temperature. Use kelvin (K) in any physics equation that involves a ratio of temperatures.
- To convert Celsius to kelvin, add 273.15. A temperature of 25 °C is 298.15 K. The Fahrenheit value is 77 °F.
- The **specific heat capacity** $c$ of a material is the heat needed to raise 1 kg of it by 1 K. Water is about 4186 J/(kg K). Aluminium is about 900 J/(kg K). These are typical values at room temperature.

## Key equations

Spring-mass oscillator (typical SHM):

$$
\omega = \sqrt{\frac{k}{m}}, \qquad f = \frac{\omega}{2\pi}, \qquad T = \frac{1}{f}, \qquad v_{\max} = A\,\omega
$$

- $k$ is the spring constant (newtons per meter, N/m).
- $m$ is the mass (kilograms, kg).
- $A$ is the amplitude (m).
- $v_{\max}$ is the largest speed of the mass (m/s).

Wave on a stretched string:

$$
v = \sqrt{\frac{T_s}{\mu}}, \qquad v = f\lambda
$$

- $T_s$ is the tension in the string (N).
- $\mu$ is the mass per unit length of the string (kg/m).

Fundamental standing wave on a string fixed at both ends of length $L$:

$$
\lambda_1 = 2L, \qquad f_1 = \frac{v}{2L}
$$

Refraction (Snell's law):

$$
n_1 \sin\theta_1 = n_2 \sin\theta_2
$$

- $n_1$ and $n_2$ are the indices of refraction of the two media.
- $\theta_1$ and $\theta_2$ are the angles from the normal to the surface, in degrees.

Heat added to a substance with no phase change:

$$
Q = m\,c\,\Delta T
$$

- $m$ is the mass (kg).
- $c$ is the specific heat capacity (J/(kg K)).
- $\Delta T$ is the temperature change (K). A change of 1 K equals a change of 1 °C.

## Worked example

**Problem.** A string is fixed at both ends. Its length is $L = 1.2$ m. Its tension is $T_s = 50$ N, and its mass per unit length is $\mu = 0.010$ kg/m. Find the speed of waves on the string, the fundamental frequency, and the fundamental wavelength.

**Given:**

- $L = 1.2$ m
- $T_s = 50$ N
- $\mu = 0.010$ kg/m

**Find:** $v$, $f_1$, $\lambda_1$

**Assumptions:** The string is ideal (uniform, with no stiffness). Air damping is ignored.

**Solution.**

1. Wave speed: $v = \sqrt{T_s/\mu} = \sqrt{50/0.010} = \sqrt{5000} = 70.71$ m/s.
2. Fundamental wavelength: $\lambda_1 = 2L = 2(1.2) = 2.4$ m.
3. Fundamental frequency: $f_1 = v/\lambda_1 = 70.71/2.4 = 29.46$ Hz.

**Answer.** The wave speed is 70.7 m/s. The fundamental wavelength is 2.4 m. The fundamental frequency is 29.5 Hz.

**Sanity check.** The units check: $\sqrt{\text{N}/(\text{kg/m})} = \sqrt{\text{kg m/s}^2 / (\text{kg/m})} = \sqrt{\text{m}^2/\text{s}^2} = \text{m/s}$. Also $f_1 \lambda_1 = 29.46 \times 2.4 = 70.7$ m/s, which matches $v$.

## Practice

1. A spring has $k = 200$ N/m and a mass of $m = 0.50$ kg attached. Find $\omega$, $f$, and $T$.
2. A string has tension $50$ N and mass per unit length $0.010$ kg/m. Find the wave speed.
3. Light with a wavelength of $500$ nm in vacuum enters water with $n = 1.33$. Find its wavelength in water.
4. Light travels from air ($n = 1.00$) into glass ($n = 1.50$) at an incidence angle of $30^\circ$. Find the refraction angle.
5. A $2.0$ kg mass of water is heated from $20\,^\circ$C to $80\,^\circ$C. Find the heat added, in kilojoules.

<details><summary>Answers</summary>

1. $\omega = 20$ rad/s, $f = 3.18$ Hz, $T = 0.314$ s
2. $70.7$ m/s
3. $376$ nm
4. $19.5^\circ$
5. $502$ kJ

</details>

## Common mistakes

- Mixing up frequency and angular frequency. Use $\omega = 2\pi f$ when you need radians per second.
- Using degrees in a temperature equation. Thermodynamic ratios need kelvin, so convert from Celsius first.
- Assuming the wavelength stays the same when light enters water. The frequency stays the same, and the wavelength gets shorter.
- Forgetting that $\mu$ is mass per unit length, not total mass. Divide the mass by the length first.
- Treating heat as something an object contains. Heat is energy moving across a boundary because of a temperature difference.

## Go deeper

- [Introduction to Oscillations, University Physics Volume 1](https://openstax.org/books/university-physics-volume-1/pages/15-introduction) by OpenStax: simple harmonic motion, damping, and forced oscillations, free to read.
- [Introduction to Waves, University Physics Volume 1](https://openstax.org/books/university-physics-volume-1/pages/16-introduction) by OpenStax: traveling waves, wave speed on a string, interference, and standing waves, free to read.
- [Introduction to Temperature and Heat, University Physics Volume 2](https://openstax.org/books/university-physics-volume-2/pages/1-introduction) by OpenStax: temperature scales, thermal expansion, specific heat, and calorimetry, free to read.
- [Fields, waves, and space reference](reference-fields-waves-space.md): the lookup sheet for this topic.
