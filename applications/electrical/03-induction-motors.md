# Induction motors

**Type:** lesson

An induction motor makes torque without brushes and without magnets on the rotor. Three-phase currents in the stator make a rotating magnetic field, and that field induces currents in the rotor, which then turn to follow it. Induction motors drive most pumps, fans, compressors, and conveyors in industry, so engineers need to understand slip, the speed-torque curve, and how a variable frequency drive changes speed.

**Prerequisites:** [Electricity and magnetism](../../physics/06-electricity-and-magnetism.md), [Circuit basics](../electronics/01-circuit-basics.md), [DC motors](01-dc-motors.md)
**Time:** 6-8 h

## Core ideas

### How it works

1. Three coils in the stator are spaced 120 degrees apart around the core. Three-phase currents, shifted by a third of a cycle, make a magnetic field that rotates around the stator at a fixed speed, called the synchronous speed.
2. The rotor is a set of conducting bars, usually aluminum or copper, joined at each end by rings. This is the squirrel cage. No current reaches the rotor from outside.
3. The rotating field cuts the rotor bars and induces a voltage in them, as Faraday's law describes. The induced voltage drives current around the shorted bars.
4. The rotor current interacts with the field and produces torque. Lenz's law says the rotor current opposes the change that caused it, so the rotor is pulled along with the field.
5. The rotor cannot quite catch the field. If it reached synchronous speed, the bars would see no relative motion, the induced current would vanish, and the torque would fall to zero. The rotor therefore runs slightly slower than the field. That difference is slip.

### Main parts

- **Stator**: a laminated steel core with copper windings in slots, connected to three-phase supply. The stator sets the number of poles and the synchronous speed.
- **Squirrel-cage rotor**: a laminated core with solid bars and end rings. It has no brushes, no slip rings, and no magnets. Its simplicity makes it rugged and cheap.
- **Wound rotor**: a rotor with coils connected to slip rings. External resistors in the rotor circuit raise starting torque and limit starting current.
- **Bearings, fan, and housing**: bearings carry the shaft load. The fan cools the frame, and the housing protects the windings.
- **Terminal box and protection**: thermal overload relays, fuses, and motor protection devices guard the windings.

### Variants

- **Squirrel-cage induction motor**: the most common motor in industry. Used for pumps, fans, compressors, and conveyors.
- **Wound-rotor induction motor**: used where high starting torque or speed control by rotor resistance is needed, such as older crane hoists. Its slip rings need maintenance.
- **Single-phase induction motor**: used in homes for small appliances. A single-phase supply does not make a rotating field, so a starting winding with a capacitor or a split phase is added to start the motor.
- **Efficiency classes**: IEC 60034-30 defines classes IE1 to IE4 for motor efficiency. Premium classes IE3 and IE4 cost more and reduce losses.
- **NEMA design classes**: North American design letters (A, B, C, D) describe the speed-torque shape, with Design B as the general-purpose choice.

## Key equations

The synchronous speed depends on the supply frequency $f$ in hertz and the number of poles $P$ (an even integer, dimensionless):

$$n_s = \frac{120 f}{P}$$

where $n_s$ is in rpm. A four-pole motor on a 50 Hz supply has $n_s = 1500\ \text{rpm}$.

Slip is the fractional difference between synchronous speed and the rotor speed $n$ (rpm):

$$s = \frac{n_s - n}{n_s}$$

Slip is dimensionless. At full load, a typical induction motor has a slip of 2 to 5 percent (typical).

The rotor frequency is the slip times the supply frequency, in hertz:

$$f_r = s\, f$$

Power flow through the motor: the air-gap power $P_{ag}$ (W) crosses from stator to rotor. Of that, $s P_{ag}$ is lost as rotor copper loss, and the rest, $(1 - s) P_{ag}$, becomes mechanical power:

$$P_{cu,r} = s\, P_{ag} \qquad P_{mech} = (1 - s)\, P_{ag}$$

Torque from air-gap power, with $\omega_s = 2\pi n_s / 60$ in rad/s:

$$T = \frac{P_{ag}}{\omega_s}$$

The torque-speed curve is often approximated by the Kloss formula, where $T_{max}$ is the peak torque (N m) and $s_m$ is the slip at peak torque (dimensionless):

$$T \approx \frac{2 T_{max}}{s / s_m + s_m / s}$$

The Kloss formula is an approximation. Manufacturers publish the exact curve, and the approximation is useful for a first estimate.

Variable frequency drives keep the ratio of voltage to frequency fixed, so the air-gap flux stays near its rated value:

$$\frac{V}{f} = \text{constant}$$

## Worked example

**Given:** A four-pole induction motor runs on a $50\ \text{Hz}$ supply. Its rated output is $P_{mech} = 7.5\ \text{kW}$ at full load, its efficiency at that point is $\eta = 0.90$, and its full-load speed is $n = 1450\ \text{rpm}$.

**Find:** (a) the synchronous speed, (b) the slip, (c) the shaft torque, (d) the air-gap power and rotor copper loss, and (e) the speed on a drive at $25\ \text{Hz}$, if the slip stays the same.

**Solution:**

1. Synchronous speed: $n_s = 120 \times 50 / 4 = 1500\ \text{rpm}$.
2. Slip: $s = (1500 - 1450) / 1500 = 0.0333$, or 3.3 percent.
3. Shaft speed in rad/s: $\omega_m = 1450 \times 2\pi / 60 = 151.8\ \text{rad/s}$. Shaft torque: $T = P_{mech} / \omega_m = 7500 / 151.8 = 49.4\ \text{N m}$.
4. Air-gap power: $P_{ag} = P_{mech} / (1 - s) = 7500 / (1 - 0.0333) = 7759\ \text{W}$. Rotor copper loss: $P_{cu,r} = s P_{ag} = 0.0333 \times 7759 = 259\ \text{W}$.
5. Electrical input: $P_{in} = P_{mech} / \eta = 7500 / 0.90 = 8333\ \text{W}$. The stator copper, iron, and windage losses are $8333 - 7500 - 259 = 575\ \text{W}$.
6. Drive at 25 Hz: $n_s = 120 \times 25 / 4 = 750\ \text{rpm}$. With slip held at 0.0333, the speed is $750 \times (1 - 0.0333) = 725\ \text{rpm}$. This assumes the load torque, and so the slip, stays the same. Real slip changes with torque and with the voltage setting, so this is an estimate.

**Answer:** (a) $n_s = 1500\ \text{rpm}$. (b) $s = 0.033$, or 3.3 percent. (c) $T = 49.4\ \text{N m}$. (d) $P_{ag} = 7.76\ \text{kW}$ and $P_{cu,r} = 259\ \text{W}$. (e) about $725\ \text{rpm}$ at $25\ \text{Hz}$.

**Sanity check:** The rotor frequency at full load is $f_r = 0.0333 \times 50 = 1.67\ \text{Hz}$, which is small, as expected for a motor that runs close to synchronous speed. The power flow closes: $P_{ag} = P_{mech} + P_{cu,r} = 7500 + 259 = 7759\ \text{W}$. A 7.5 kW motor at 90 percent efficiency sits in the usual range for premium motors (typical).

## Design trade-offs

- **Efficiency versus cost**: an IE3 motor costs more than an IE1 motor, but it saves energy over its life. A motor that runs most of the day usually repays the extra cost within a few years (typical).
- **Slip versus losses**: a lower slip at full load reduces rotor copper loss but makes the rotor bars and rings bigger and more costly. Designers balance slip against cost and starting torque.
- **Starting current**: a squirrel-cage motor started directly across the line draws about 5 to 8 times its rated current (typical). That dip can disturb the supply, so large motors use soft starters, star-delta starting, or drives.
- **Speed control**: a fixed-speed motor on a pump wastes energy when flow falls. A variable frequency drive matches speed to demand, but it adds harmonics and costs more than a direct connection.
- **Power factor**: an induction motor draws reactive current, so its power factor is lowest at light load. Capacitors or drive electronics correct it.
- **Cooling and size**: a totally enclosed motor runs hotter than an open motor of the same size, so its insulation class or frame size must be larger.

## How it fails

- **Bearing failure**: bearings are a common end of life. Misalignment, too much grease, too little grease, and contamination all shorten life. Vibration analysis gives early warning.
- **Overheating**: overload, poor ventilation, high ambient temperature, or frequent starts all heat the windings. Insulation breaks down when it runs hot, and repeated heating ages it.
- **Broken rotor bars**: cracked bars or a broken end ring increase the slip under load, and the motor runs slow with large current swings. The motor current shows sidebands around the supply frequency.
- **Single phasing**: if one supply phase is lost, the motor keeps running on two phases, draws high current, and overheats. Phase-loss relays protect against it.
- **Drive-related stress**: a variable frequency drive can produce voltage spikes at the motor terminals, which stress the winding insulation. Filters and motor-rated cable reduce that stress.
- **Running below rated frequency at full voltage**: this raises flux, which saturates the core and overheats the motor. A drive keeps the voltage-to-frequency ratio fixed to prevent it.

## History

Galileo Ferraris in Turin demonstrated the rotating magnetic field in 1885, and he published the principle in 1888. Nikola Tesla developed a practical induction motor, patented in 1888, and George Westinghouse licensed those patents. Mikhail Dolivo-Dobrovolsky developed a three-phase squirrel-cage motor in Germany about 1889. Those three-phase motors became the workhorse of industry through the 20th century, and variable frequency drives became common once power electronics could switch the supply efficiently.

## Practice

1. A six-pole motor runs on a 60 Hz supply. Find its synchronous speed.
2. A two-pole motor on a 50 Hz supply runs at 2880 rpm. Find its slip.
3. A four-pole motor on a 50 Hz supply has a slip of 0.040. Find its rotor frequency.
4. A four-pole motor on a 60 Hz supply runs at 1750 rpm. Find its slip.
5. A four-pole variable frequency drive must set the synchronous speed to 900 rpm. Find the supply frequency.

<details><summary>Answers</summary>

1. $n_s = 120 \times 60 / 6 = 1200\ \text{rpm}$.
2. $n_s = 120 \times 50 / 2 = 3000\ \text{rpm}$, so $s = (3000 - 2880) / 3000 = 0.040$, or 4.0 percent.
3. $f_r = 0.040 \times 50 = 2.0\ \text{Hz}$.
4. $n_s = 120 \times 60 / 4 = 1800\ \text{rpm}$, so $s = (1800 - 1750) / 1800 = 0.028$, or 2.8 percent.
5. $f = 900 \times 4 / 120 = 30\ \text{Hz}$.

</details>

## Common mistakes

- Using the rotor speed where the formula needs synchronous speed. Slip uses $n_s$ in the denominator, and the rotor speed $n$ in the numerator.
- Mixing up supply frequency and rotor frequency. The rotor frequency is $s f$, which is small at normal load.
- Expecting full torque at standstill from every induction motor. Starting torque depends on the rotor design, and a standard squirrel cage gives modest starting torque.
- Running a drive below rated frequency with rated voltage. This saturates the core. Keep the voltage-to-frequency ratio fixed.
- Treating the Kloss approximation as exact. It gives the shape of the curve, but the manufacturer's curve is the one to use for design.

## Go deeper

- [University Physics Volume 2, Chapter 13 (Electromagnetic Induction)](https://openstax.org/books/university-physics-volume-2/pages/13-introduction) by OpenStax: Faraday's law and induced currents, the principle behind the squirrel-cage rotor.
- [Electric Motors](https://www.energy.gov/eere/buildings/electric-motors) by the U.S. Department of Energy: efficiency standards and test rules for induction motors.
- [Circuits and Electronics (6.002), MIT OpenCourseWare](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/) by MIT: circuit models and power electronics used in variable frequency drives.
- Related lessons: [DC motors](01-dc-motors.md) and [Brushless and stepper motors](02-brushless-and-stepper-motors.md) cover the other motor families. [Circuit basics](../electronics/01-circuit-basics.md) covers the resistance and voltage relations used in the equivalent circuit.
- [Applications reference](../reference.md): the lookup sheet for this topic.
