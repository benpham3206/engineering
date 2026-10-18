# GPS

**Type:** lesson

GPS finds a receiver's position by measuring how long radio signals take to arrive from satellites with atomic clocks. Engineers need to understand it because a 1 ns timing error becomes a 0.30 m position error, and clock effects from relativity add about 38 $\mu$s per day that must be corrected. Positioning accuracy depends on clocks, orbits, the atmosphere, and the receiver's geometry.

**Prerequisites:** [Waves, light, and heat](../../physics/07-waves-light-heat.md), [Radio and antennas](02-radio-and-antennas.md), [Orbital mechanics and rockets](../../physics/15-orbital-mechanics-and-rockets.md), [Algebra](../../math/01-algebra.md)
**Time:** 6-8 h

## Core ideas

### How it works

Each GPS satellite broadcasts its position and the exact time the signal left it. The receiver compares that time with its own clock and multiplies the difference by the speed of light. The result is the distance to the satellite, called a pseudorange. The receiver's clock is not perfect, so every pseudorange contains the same unknown clock error.

With four satellites, the receiver solves for four unknowns: its position $x$, $y$, $z$, and its clock error $\delta t$. Each satellite gives one equation. The receiver knows where the satellites are, so the position comes from the intersection of spheres around the satellites. Three satellites fix position if the clock error is known. The fourth satellite removes the clock error.

The steps are:

1. The satellite broadcasts its position and a time stamp on the L1 carrier at 1575.42 MHz.
2. The receiver measures the arrival time of each signal.
3. The receiver forms a pseudorange for each satellite.
4. The receiver solves four equations for position and clock error.

The satellite clocks themselves run at a different rate than clocks on the ground. The satellite is faster in orbit and sits higher in Earth's gravity. Both effects change the clock rate, and the system must correct them.

### Main parts

- Satellites: about 30 operational spacecraft in six orbital planes. Each orbits at an altitude of about 20 200 km (typical) with a period of about 12 hours.
- Atomic clocks: rubidium or cesium clocks on each satellite. The clock stability controls the timing error.
- Ground control: monitor stations track the satellites and upload orbit and clock corrections several times a day.
- Receiver: an antenna, a low-noise amplifier, a correlator that locks onto each code, and a processor that solves the position equations.
- Augmentation systems: ground stations that broadcast corrections for the ionosphere and orbit errors. The United States operates WAAS for aviation, and Europe operates EGNOS.

### Variants

- Single-frequency receivers: use one carrier and a model to correct the ionosphere. Phone and car receivers commonly work this way.
- Dual-frequency receivers: measure the ionospheric delay directly from two carriers, such as L1 and L5, and remove most of it.
- Carrier-phase receivers: measure the phase of the carrier, not just the code. They reach centimetre accuracy and are used in surveying and precision farming.
- Other satellite systems: Galileo (Europe), GLONASS (Russia), and BeiDou (China) use the same basic method.

## Key equations

Pseudorange for satellite $i$, with $t_{rx}$ the receiver time, $t_{tx,i}$ the satellite transmit time in seconds, $c = 2.998 \times 10^8$ m/s, and $\rho_i$ in metres:

$$\rho_i = c\,(t_{rx} - t_{tx,i})$$

Each pseudorange also contains the clock error, so the solved equation is

$$\rho_i = \sqrt{(x - x_i)^2 + (y - y_i)^2 + (z - z_i)^2} + c\,\delta t$$

where $(x_i, y_i, z_i)$ are the satellite coordinates in metres and $\delta t$ is the receiver clock error in seconds.

Distance from a clock error $\delta t$ is

$$d = c\,\delta t$$

Orbital speed of a circular orbit, with $GM = 3.986 \times 10^{14}$ m$^3$/s$^2$ (typical value for Earth) and $r$ the orbit radius in metres:

$$v = \sqrt{\frac{GM}{r}}$$

Special relativity: a moving clock runs slow by a fraction of about $v^2 / (2c^2)$.

$$\frac{\Delta f}{f} \approx -\frac{v^2}{2c^2}$$

General relativity: a clock higher in Earth's gravity runs fast by the gravitational potential difference divided by $c^2$. With $R$ the Earth radius in metres and $r$ the satellite orbit radius in metres:

$$\frac{\Delta f}{f} \approx \frac{GM}{c^2}\left(\frac{1}{R} - \frac{1}{r}\right)$$

Both effects are fractions of the clock rate. Multiply by the number of seconds in a day, $86\,400$ s, to get the time error per day.

## Worked example

**Part A: relativity correction.** A GPS satellite is in a circular orbit with radius $r = 26\,560$ km (typical value). Earth's mean radius is $R = 6371$ km (typical value), $GM = 3.986 \times 10^{14}$ m$^3$/s$^2$, and $c = 2.998 \times 10^8$ m/s. Find the orbital speed, the clock rate change from motion, the clock rate change from gravity, and the net change per day.

Orbital speed: $v = \sqrt{GM/r} = \sqrt{3.986\times10^{14} / 2.656\times10^7} = 3874$ m/s, which is about 3.9 km/s.

Motion effect: $\Delta f/f = -v^2 / (2c^2) = -7.21\ \mu\text{s}$ per day. The satellite clock loses about 7.2 $\mu$s per day.

Gravity effect: $\Delta f/f = (GM/c^2)(1/R - 1/r) = +45.72\ \mu\text{s}$ per day. The satellite clock gains about 45.7 $\mu$s per day.

Net effect: $+45.72 - 7.21 = +38.5\ \mu\text{s}$ per day. The satellite clock runs fast by about 38.5 $\mu$s per day compared with a ground clock.

**Part B: timing error as distance.** A timing error of 1 ns in a pseudorange gives a range error of $d = c\,\delta t = 2.998\times10^8 \times 1\times10^{-9} = 0.30$ m. Without correction, the 38.5 $\mu$s daily drift gives a range error of $2.998\times10^8 \times 38.5\times10^{-6} = 11\,542$ m, which is about 11.5 km per day of drift.

**Answers:** (A) orbital speed about 3874 m/s; the motion effect is $-7.2\ \mu$s per day, the gravity effect is $+45.7\ \mu$s per day, and the net effect is $+38.5\ \mu$s per day. (B) 1 ns is 0.30 m, and an uncorrected 38.5 $\mu$s per day drift is about 11.5 km of position error per day.

**Sanity check:** The orbital speed of 3.9 km/s and the gravity effect matching the known order of tens of microseconds per day both fit the expected values. A 1 ns error being about 30 cm also matches the familiar rule of thumb that light covers 30 cm in a nanosecond.

## Design trade-offs

- Clock quality against cost and mass: atomic clocks give the timing that positioning needs, but they are heavy and costly. Rubidium clocks are smaller and cheaper, while cesium clocks are more stable over long periods.
- Orbit altitude against coverage and radiation: a higher orbit covers more of Earth from each satellite, but it needs a larger launch and receives more radiation, which shortens clock and electronics life.
- Number of satellites against accuracy: more visible satellites improve the geometry and reduce the position error. Receivers in cities or canyons often see only a few satellites, and their accuracy drops.
- Single against dual frequency: a second frequency removes most ionospheric delay, but it needs a more complex receiver and antenna.
- Accuracy against power and cost: carrier-phase receivers reach centimetre accuracy but need longer observation times and more processing.

## How it fails

- Ionospheric delay: the ionosphere slows the signal and adds several metres of error, more at low elevation angles and during solar storms.
- Multipath: signals reflect off buildings, water, and terrain before they reach the antenna. The reflected path is longer, so it adds error. Careful antenna design and choke rings reduce it.
- Clock drift and orbit error: the satellite clock drifts between corrections, and the orbit model is imperfect. Ground corrections keep these errors small, but they grow between uploads.
- Uncorrected relativity: the 38.5 $\mu$s daily offset would grow to about 11.5 km per day. The system corrects it before launch and in software.
- Jamming and spoofing: a weak GPS signal is easy to block or fake. Warning signs include sudden jumps in position, a clock that disagrees with time servers, and a sudden loss of satellites.
- Geometry: satellites clustered in one part of the sky spread out the error. Receivers report a dilution of precision (DOP) value to show the geometry quality.

Safety measures include receiver autonomous integrity monitoring (RAIM), which checks whether the satellites agree, and augmentation systems such as WAAS and EGNOS, which broadcast correction and integrity messages for aircraft.

## History

The United States Department of Defense developed GPS, called NAVSTAR GPS, from the 1970s. The first Block I satellite launched in February 1978. The system reached full operational capability in about 1995. Its predecessor, the Transit system, was a US Navy navigation system from the 1960s that used Doppler shifts from passing satellites. In 1971, Joseph Hafele and Richard Keating flew atomic clocks around the world on airliners and measured time effects that matched relativity predictions, which supported the clock corrections GPS later used. Dates for the early programme are approximate, and sources differ on some of the early milestones.

## Practice

1. A timing error of 1 ns occurs in a receiver. Find the position error in metres.
2. A receiver clock is 50 ns off. Find the range error in metres.
3. A receiver measures a signal transit time of 0.075 s. Find the pseudorange in km, using $c = 2.998 \times 10^8$ m/s.
4. The special relativity effect alone on a satellite moving at 3874 m/s changes the clock rate by $-v^2/(2c^2)$. Find the change per day in $\mu$s.
5. Explain why a receiver needs four satellites, not three, to find a position in three dimensions.

<details><summary>Answers</summary>

1. $d = c\,\delta t = 2.998\times10^8 \times 1\times10^{-9} = 0.30$ m.
2. $d = 2.998\times10^8 \times 50\times10^{-9} = 14.99$ m, or about 15.0 m.
3. $\rho = c\,t = 2.998\times10^8 \times 0.075 = 2.248\times10^7$ m, or about 22 480 km.
4. $-v^2/(2c^2) \times 86\,400$ s $= -7.2\ \mu$s per day.
5. The receiver has four unknowns: three position coordinates and its clock error. Three satellites give three equations, which cannot solve for four unknowns. The fourth satellite supplies the missing equation, so the receiver can solve for the clock error and the position together.

</details>

## Common mistakes

- Treating the clock error as zero. Every pseudorange includes the receiver clock error, so position needs four satellites.
- Using seconds where the formula needs metres. Multiply a time by $c$ before comparing it with a distance.
- Applying only the gravity effect or only the motion effect. GPS needs the net of both.
- Forgetting the sign. The satellite clock runs fast on net, while a moving clock alone runs slow.
- Assuming a GPS fix is always accurate to a few metres. Phones, cities, and jamming can push the error far higher, and the receiver should report its estimated accuracy.

## Go deeper

- [GPS.gov](https://www.gps.gov/): the official US government information on GPS, timing, and accuracy.
- [Radar and sonar](07-radar-and-sonar.md): the same time-of-flight idea used for ranging.
- [Radio and antennas](02-radio-and-antennas.md): the signal and antenna basics that GPS uses.
- [The modern era](../../history/10-the-modern-era.md): the history of GPS and other modern systems.
- [Orbital mechanics and rockets](../../physics/15-orbital-mechanics-and-rockets.md): the orbit and velocity background used here.
</content>
