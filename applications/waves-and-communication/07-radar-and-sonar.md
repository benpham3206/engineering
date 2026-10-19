# Radar and sonar

**Type:** lesson

Radar and sonar are systems that find objects by sending a wave out and listening for its echo. A wrong echo reading can send an aircraft or ship off course, so engineers must get every measurement right.

Engineers use them to measure distance and speed for aircraft, ships, weather, road vehicles, and seabed mapping. Three quantities cover most of the work: the round-trip time gives range, the frequency shift gives radial speed, and the pulse length sets the smallest separation a system can resolve.

**Prerequisites:** [Oscillations, waves, light, and heat](../../physics/07-waves-light-heat.md), [Radio and antennas](02-radio-and-antennas.md), [Trigonometry](../../math/02-trigonometry.md)
**Time:** 6-8 h

## Core ideas

### How it works

Radar (radio detection and ranging) sends a short pulse of electromagnetic waves, usually at microwave frequencies from about 1 GHz to 40 GHz. Sonar (sound navigation and ranging) does the same job with sound in water or air. Sound travels at about 1500 m/s in seawater and 343 m/s in air at 20 C (typical values). Radio waves travel at $c = 3.00 \times 10^8$ m/s, so radar needs much faster electronics than sonar does.

The sequence is the same for both:

1. The transmitter emits a pulse of length $\tau$ (seconds).
2. The pulse travels to the target at range $R$ (metres) and reflects.
3. The receiver detects the echo after a round-trip time $t = 2R/c$.
4. The processor converts the time to range and measures any frequency shift to find the target's speed.

A target moving toward or away from the sensor shifts the echo frequency. This is the Doppler effect. Radar uses the shift to separate moving targets from stationary clutter such as buildings, sea, and rain.

### Main parts

- Transmitter: a power amplifier. Older radars used a magnetron or klystron. Modern systems often use solid-state amplifiers.
- Antenna: a parabolic dish or a phased array. A narrow beam gives angular resolution and gain.
- Duplexer: a switch that lets one antenna transmit and receive. It also shields the receiver from the high transmit power.
- Receiver: a low-noise amplifier, a mixer, and filters that pick out the echo from the noise.
- Signal processor and display: matched filters, Doppler filters, detection thresholds, and target tracking.
- Sonar transducer: a piezoelectric or magnetostrictive element that converts electrical signals to sound and back. Hydrophones listen without transmitting.

### Variants

- Pulsed radar: sends short pulses and times the echoes. This is the most common type for measuring range, such as air traffic control and naval search radar.
- Continuous-wave (CW) radar: transmits without pauses. It measures speed well through Doppler but cannot measure range without modulation.
- FMCW radar: sweeps the frequency up and down. The beat frequency between the sent and received signals gives range. Automotive radar near 77 GHz (a typical band) uses this method.
- Weather radar: uses a wavelength long enough to pass through rain with little loss. Many national networks use S-band near 3 GHz.
- Active sonar: sends pings and listens for echoes. Passive sonar only listens, which keeps the listener hidden.
- Side-scan sonar: sweeps sound sideways across the seabed to make images of the bottom.

## Key equations

Round-trip range, with $R$ in metres, $c$ in m/s, and $t$ in seconds:

$$R = \frac{c\,t}{2}$$

This assumes free-space propagation at a constant $c$, a stationary target during the round trip, and a single reflection.

Range resolution, the smallest separation two targets can have and still show as two echoes, with $\tau$ the pulse length in seconds:

$$\Delta R = \frac{c\,\tau}{2}$$

This assumes a rectangular pulse with no pulse compression, and two targets are resolved only when their echoes do not overlap in time.

Doppler shift for radar, with $v$ the radial speed toward the sensor in m/s and $f_0$ the transmitted frequency in Hz:

$$f_d = \frac{2 v f_0}{c}$$

This assumes a monostatic radar (same antenna sends and receives), non-relativistic speeds with $v \ll c$, and motion along the line of sight only.

Radial speed from a measured Doppler shift $f_d$:

$$v = \frac{c\,f_d}{2 f_0}$$

This is the inverse of the Doppler relation and assumes the same conditions: monostatic radar, $v \ll c$, and radial motion only.

Sonar range uses the speed of sound in the medium, $c_w$ in m/s:

$$R = \frac{c_w t}{2}$$

This assumes a uniform medium with constant sound speed $c_w$ and straight-line sound paths, so refraction from temperature layers is ignored.

Angular resolution of a circular dish, with $\lambda$ the wavelength in m and $D$ the dish diameter in m, in radians:

$$\theta \approx 1.22\,\frac{\lambda}{D}$$

This assumes a circular aperture with uniform illumination, a far-field observer, and $D \gg \lambda$.

## Worked example

A pulsed radar operates at $f_0 = 10$ GHz (X-band), with a pulse length of $\tau = 1\ \mu\text{s}$. A target sits at $R = 30$ km and moves straight toward the radar at $v = 30$ m/s. Find (a) the round-trip time of the echo, (b) the range resolution, and (c) the Doppler shift. Assume $c = 3.00 \times 10^8$ m/s.

Solution for (a): $t = 2R/c = 2 \times 30\,000 / 3.00\times10^8 = 200\ \mu\text{s}$.

Solution for (b): $\Delta R = c\tau/2 = 3.00\times10^8 \times 1\times10^{-6} / 2 = 150$ m.

Solution for (c): $f_d = 2 v f_0 / c = 2 \times 30 \times 10\times10^9 / 3.00\times10^8 = 2000$ Hz, or about 2.0 kHz. The sign is positive because the target approaches.

Answers: (a) about 200 $\mu$s, (b) about 150 m, (c) about 2.0 kHz.

Sanity check: a 30 m/s target has $v/c = 10^{-7}$. Twice that, times the 10 GHz carrier, gives about 2 kHz, which matches the result.

For sonar, a sonar in seawater at 1500 m/s, looking at a wall 200 m away, hears the echo after $2 \times 200 / 1500 = 0.267$ s. Radar must time the same kind of echo in microseconds or less, because radio waves cover the same distance far faster.

## Design trade-offs

- Pulse length against range resolution: a shorter pulse gives finer resolution, but it carries less energy for the same peak power, since energy is power times time. Pulse compression uses a long chirped pulse and then compresses it in the receiver, which gives both energy and resolution.
- Frequency against size and weather: a higher frequency gives a narrower beam from a smaller antenna and a larger Doppler shift. It also loses more energy in rain. Weather radar accepts a larger antenna at S-band for that reason.
- Dish size against beamwidth: for an X-band wavelength of 0.03 m and a 1 m dish, $\theta \approx 1.22 \times 0.03 / 1 = 0.037$ rad, which is about 2.1 degrees. Doubling the dish halves the beamwidth.
- Mechanical scanning against electronic scanning: a rotating dish is cheap. A phased array steers the beam with no moving parts and scans faster, but it costs more.
- Echo strength against distance: for a point target, echo power falls with the fourth power of range. Doubling the range cuts the echo to one-sixteenth of its strength.
- Sonar update rate against range: sound is slow, so a sonar must wait for each echo before sending the next ping. Far targets cut the ping rate.

## How it fails

- Clutter: echoes from land, sea, or rain can hide real targets. Designers use Doppler filters to remove stationary returns and constant false alarm rate (CFAR) detection to set thresholds that track background noise.
- Range ambiguity: if the pulse repetition frequency (PRF) is too high, an echo from one pulse can arrive after the next pulse is sent and appear at the wrong range. The unambiguous range is $c / (2 \cdot \text{PRF})$. At a PRF of 1 kHz, that limit is 150 km.
- Blind speeds: a moving-target filter cancels targets whose Doppler shift is a multiple of the PRF. Those targets vanish from the display at certain speeds. Operators change the PRF to break up the pattern.
- Sonar multipath and shadow zones: sound bends in water with temperature layers, and reflections from the surface and bottom make false echoes. Some areas receive no sound at all.
- Radiation and safety: high-power radar beams can heat tissue. Systems use interlocks that cut power when a person enters the beam, and they set exclusion zones around antennas.
- Marine life: high-power sonar can harm marine mammals. Navies and survey operators use power limits, ramp-up procedures, and monitoring before they transmit.

## History

Christian Hülsmeyer showed a radio-echo device for detecting ships in Germany in 1904. Robert Watson-Watt led British work on radar for aircraft detection from about 1935, and the Chain Home stations used it during the Battle of Britain in 1940. At Birmingham in 1940, John Randall and Harry Boot built a cavity magnetron that made short, high-power radar pulses practical. In France during the First World War, Paul Langevin and Constantin Chilowsky developed ultrasonic echo ranging for detecting submarines. Dates for the early work are approximate, and the sources do not always agree on credit.

## Practice

1. A radar receives an echo 80 $\mu$s after the pulse is sent. Find the target range in km. Use $c = 3.00\times10^8$ m/s.
2. A radar uses a 0.5 $\mu$s pulse. Find its range resolution in metres.
3. A sonar in seawater hears an echo 0.8 s after the ping. Find the distance to the reflector in metres. Use 1500 m/s.
4. A 10 GHz radar sees a target moving toward it at 50 m/s. Find the Doppler shift in hertz.
5. A 1 $\mu$s pulse radar cannot separate two targets that are 100 m apart. Explain why, and state the smallest separation it can resolve.

<details><summary>Answers</summary>

1. $R = ct/2 = 3.00\times10^8 \times 80\times10^{-6} / 2 = 12\,000$ m, or 12.0 km.
2. $\Delta R = c\tau/2 = 3.00\times10^8 \times 0.5\times10^{-6} / 2 = 75$ m.
3. $R = c_w t / 2 = 1500 \times 0.8 / 2 = 600$ m.
4. $f_d = 2 v f_0 / c = 2 \times 50 \times 10\times10^9 / 3.00\times10^8 \approx 3300$ Hz, or about 3.3 kHz.
5. The 1 $\mu$s pulse gives $\Delta R = 150$ m. Two targets 100 m apart fall inside one range cell, so their echoes merge into one. The smallest resolvable separation is about 150 m.

</details>

## Common mistakes

- Using $R = ct$ instead of $R = ct/2$. The pulse travels to the target and back, so the time covers twice the range.
- Confusing pulse length with range resolution. Resolution is $c\tau/2$, not $c\tau$.
- Using the speed of sound in air for sonar in water. Sound in seawater is about 4.4 times faster.
- Reading Doppler as total speed. A Doppler radar measures only the radial component of velocity, the part that points toward or away from the sensor.
- Assuming a stronger echo always means a bigger target. Echo strength depends on range, angle, shape, and material as well as size.

## Go deeper

- [Radio and antennas](02-radio-and-antennas.md): the wave and antenna basics that radar uses.
- [Speakers and microphones](06-speakers-and-microphones.md): the transducers that sonar uses, in a different form.
- [GPS](08-gps.md): another time-of-flight system, which turns travel time into position.
- [History, war, nuclear, and space](../../history/08-war-nuclear-and-space.md): the wartime development of radar and jet engines.
- [Waves, light, and heat](../../physics/07-waves-light-heat.md): the wave and Doppler background used in this lesson.
- [Reference: fields, waves, and space](../../physics/reference-fields-waves-space.md): equation sheet for wave speed, Doppler, and related quantities.
</content>
