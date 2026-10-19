# Test and inspection instruments

**Type:** lesson
**Verify:** strict

A **test or inspection instrument** is a handheld or bench device that measures a physical quantity such as force, torque, speed, temperature, sound, hardness, or surface finish, or that lets you see where you cannot look directly. An engineer uses these instruments to check that a part or machine matches its design, and a reading is only as good as the user's knowledge of how the instrument works and the ways it can mislead.

This lesson starts from the first reading: what each instrument measures, the one safe first use, and the normal procedure. Then it covers the judgment that separates a measurement from a number on a display: how the instrument lies. Dimensional tools such as calipers are in [Measurement tools](07-measurement-tools.md), and the sensor principles behind many of these devices are in [Sensors and transducers](../measurement/05-sensors-and-transducers.md).

**Prerequisites:** [Measurement tools](07-measurement-tools.md), [Sensors and transducers](../measurement/05-sensors-and-transducers.md), [Precision, accuracy, and uncertainty](../measurement/02-precision-accuracy-and-uncertainty.md)
**Time:** 5-7 h

## Core ideas

### What every instrument has in common

- An instrument reports a number, but it measures an effect: a resistance change, a light flash, a sound pressure. The number is right only if the effect it senses is the one you think it is.
- **Resolution** is the smallest step the display shows, and **accuracy** is how close the reading is to the true value. A display with many digits is not accurate because of them. See [Precision, accuracy, and uncertainty](../measurement/02-precision-accuracy-and-uncertainty.md).
- **Calibration** is comparing the instrument with a reference of known value and recording the difference. An instrument out of its calibration interval still reads, and the reading is unreliable by an unknown amount.
- A **zero check** is reading the instrument with nothing applied, to see whether it starts at zero. A **check against a known** is reading a reference you trust, such as a known weight, a known torque, or a calibrator, before and after the job.
- The most common way an instrument lies is a mismatch between the conditions it was made for and the conditions you used it in. Each section ends with that failure.

### Force gauges and load cells

A **force gauge** is a handheld device with a hook or tip that reads the push or pull applied to it. A **load cell** is a metal body fitted with strain gauges that changes its electrical output in proportion to the force through it. Strain gauges and the bridge circuit that reads them are taught in [Strain gauges and the Wheatstone bridge](../measurement/06-strain-gauges-and-wheatstone-bridge.md).

A load cell is rated by a **rated output** in millivolts per volt of excitation at its rated capacity. A cell with a typical rated output of 2 mV/V, powered at 10 V, gives 20 mV at full load, and its output at a lower load is proportional.

To use a force gauge, zero it with nothing attached and the attachment fitted, then pull or push along the axis of the gauge and read the peak or steady value. For a load cell, mount it so the load passes through its intended axis and nothing else carries part of the force, zero it in the position it will be used, and read with a stable supply.

How it lies: a force not along the axis adds bending the cell was not made for, so the reading is wrong. Side loads, a bent mount, and a gauge hung from a frame that flexes all do this. Readings above the rated capacity damage a cell without warning, and temperature changes drift the zero. A load cell is only as accurate as its zero and its supply.

### Torque wrenches and torque testers

A **torque wrench** tightens a fastener until the applied torque equals a set value, and then signals by clicking, slipping, or showing the value on a dial. A **torque tester** (or torque analyzer) is a fixed sensor that reads the torque a wrench or screwdriver actually delivers, used to check and calibrate tools.

Set the wrench to the value on the drawing, pull smoothly on the handle at the grip mark, and stop when it signals. Return a click-type wrench to its lowest setting when stored, because a spring left under load loses accuracy. Do not use it to loosen a fastener.

An extension changes the torque on the fastener. If the wrench has effective length $L$ and you add an extension of length $E$ in line with it, the fastener sees more torque than the wrench shows, because the same force now acts through a longer arm. Compute the setting with the equation below.

How it lies: a wrench pulled off its grip mark, jerked rather than pulled steadily, used with an extension and no correction, or left out of calibration gives the wrong torque. The reading also does not say how much of the torque went into friction in the threads and under the head, so a dry, rusty, or oiled thread can give a very different clamping force at the same torque.

### Tachometers and stroboscopes

A **tachometer** measures the rotational speed of a shaft in revolutions per minute (rpm). A **contact tachometer** presses a rubber tip or wheel against the shaft end or surface. An **optical tachometer** points a light beam at a reflective mark stuck on the shaft and counts the returned pulses.

A **stroboscope** is a light that flashes at a set rate. When the flash rate matches the rotation rate, a marked rotating part appears to stand still.

> [!WARNING]
> A contact tip held against a rotating shaft can catch loose clothing, hair, or a glove, and can slip and strike a spinning part. Prefer the optical tachometer on rotating machinery, put the reflective mark on while the machine is stopped, and measure from outside the danger zone.

To use an optical tachometer, stop the machine, stick on a small piece of reflective tape, restart, aim the beam at the tape from the stated distance, and read the rpm. To use a stroboscope, mark the rotating part, start at a high flash rate, and lower it until a single sharp image of the mark stands still. The highest rate that gives one still image is the true speed. Lower rates that also give a still image are fractions of it (half, a third, and so on), and rates above it show two or more images.

How they lie: a contact wheel slips and reads low. An optical tachometer counts the wrong thing if the tape is dirty, if there is more than one mark, or if bright light or a shiny surface returns extra pulses. A stroboscope can show a still image at a fraction of the true speed, so a flash rate that lowers to a still image at half speed reads half the true value if you stop there. Always check the next higher setting.

### Infrared thermometers and thermal cameras

An **infrared (IR) thermometer** measures a surface temperature without touching it, by sensing the thermal radiation the surface emits. A **thermal camera** does the same for many points at once and shows the temperature as a picture. Because they sense radiation, not the temperature itself, two properties of the surface and the geometry control the reading.

**Emissivity** ($\varepsilon$) is the fraction of ideal blackbody radiation a surface actually emits, between 0 and 1. Rough, dark, painted, or oxidized surfaces have a high emissivity. Bare polished metals have a low one, and a low-emissivity surface also reflects the surroundings. The instrument assumes an emissivity (often fixed by the maker); if the real surface differs, the reading is wrong.

The **distance-to-spot ratio (D:S)** gives the nominal spot diameter from distance divided by the ratio. A ratio of 12:1 gives a nominal 1 m spot at 12 m. The spot has no sharp edge, and the ratio applies only under the instrument's stated focus conditions, so check its spot-size definition and focal distance. Keep the target wider than the nominal spot to limit background radiation in the reading.

To use one, aim at a matt surface, stand close enough that the spot fits inside the target, and wait for the reading to settle. When the surface is shiny, cover a small patch with matt tape or paint and measure the patch, or use a contact probe.

> [!WARNING]
> Many IR thermometers use a laser dot only to show where they aim. Do not point it at anyone's eyes, and do not aim it at a reflecting surface where it could bounce into a face.

How they lie: a shiny, low-emissivity surface reads close to the temperature of whatever it reflects. A spot larger than the target averages in the background. Steam, dust, glass, and plastic windows block the radiation, and glass does not transmit the infrared band these instruments use, so you cannot read a temperature through a window. A thermal camera adds one more error: a temperature picture of a shiny object is mostly a picture of reflections.

### Sound level meters

A **sound level meter** measures sound pressure and shows it in decibels (dB). A **decibel** is ten times the base-10 logarithm of a power ratio, or twenty times the logarithm of a pressure ratio, so equal steps in dB are equal ratios of power. A **weighting** filter, such as A-weighting, adjusts the levels at different frequencies to follow how the ear responds.

To use one, check it with a calibrator that produces a known level, hold it at arm's length at the position where a person's ears would be, point the microphone as the manual says, and read with the weighting and response time the task needs. Use hearing protection near loud machines, and read from outside the loudest zone if you can.

Levels from separate sources do not add arithmetically. Their powers add, so two equal sources are 3 dB higher than one, and a source 10 dB below another adds under half a decibel to it.

How it lies: wind across the microphone, a handling noise, a body close to the meter that reflects sound, and a microphone placed in a corner all raise the reading. Background noise adds to the machine you want to measure. A meter set to the wrong weighting or range overloads, and a meter out of calibration reads wrong by an amount you do not know.

### Borescopes

A **borescope** is a thin probe with a light and a camera or an optical path, for looking inside a cavity such as an engine cylinder, a pipe, or a casting. It lets an engineer inspect for cracks, corrosion, and foreign objects without taking the part apart.

> [!WARNING]
> Never put a probe into a machine that is running, hot, or electrically live. Stop, lock out, and let the part cool first. A probe is also a thin tool; pushing it against resistance can kink or break it in the part.

To use one, insert the probe slowly, steering the tip with the control, and withdraw it by the same path. Photograph what you find, with a note of the position.

How it lies: a wide-angle lens makes small features look different in size and makes straight lines curve, so a borescope picture is not a dimensioned drawing. Light reflecting from wet or shiny surfaces hides a crack or makes a harmless mark look like one, and dirt on the lens can look like a defect. Do not read sizes from the picture unless the instrument is calibrated for measuring at a known distance.

### Hardness testers

A **hardness tester** measures how strongly a material resists permanent indentation by a hard indenter. Hardness is a measure of resistance to local plastic deformation, and for many metals it correlates with strength, but it is not a strength itself.

A **Rockwell** tester presses an indenter into the surface with a small preload and then a large load, and reports the number from the additional depth of the permanent indentation after the large load is removed. A smaller depth means a harder material, so the number rises with hardness. A **Shore** durometer presses a spring-loaded indenter against a rubber or plastic and reads the depth it penetrates; it is for elastomers and soft plastics. The scale letters name the indenter and load used, and numbers on different scales cannot be compared.

To use a tester, clean the surface, support the part so it cannot move or rock, apply the load as the instrument specifies, and read. Take several readings, spaced apart, and average them. Check the instrument on a reference block of known hardness before the job.

How it lies: a thin part, a rounded surface, a surface with a rough finish, or a test too near an edge gives a false value. A hardness number is valid only for the layer under the indenter, so a case-hardened or coated part tests hard on the outside and soft inside. Using the wrong scale or converting between scales gives numbers that are only approximate.

### Surface roughness gauges

A **surface roughness gauge** (or profilometer) drags a fine stylus along a surface and measures the height of the profile. The most common result is **Ra**, the arithmetic mean of the absolute height of the profile from its mean line. It tells you the typical size of the bumps but not their shape.

To use one, clean the surface, set the measuring length the standard for the surface calls for, place the gauge so the stylus travels across the machining marks (not along them), and read. Take readings in several places.

How it lies: Ra averages away the peaks and valleys, so a surface with a few deep scratches and a smooth surface with a fine texture can give the same Ra. A stylus drawn along the lay reads smoother than across it, a worn stylus rounds off fine detail, and a curved or dirty surface gives a wrong profile.

### Data loggers

A **data logger** records readings over time at a set interval from one or more sensors, without anyone watching. It is for slow processes such as a temperature in a room or a vibration over a shift.

To use one, choose the sampling interval, set the clock, check each channel against a known reference, start it, and confirm that it is recording before you leave it. Download the data and look at it before you rely on it. [Data acquisition and sampling](../measurement/08-data-acquisition-and-sampling.md) explains how to choose the rate.

How it lies: a sampling interval that is too long misses fast events and can show a false slower pattern (aliasing). A full memory or a flat battery stops the record, and nothing on the output says so unless you look. A clock that was not set, and a sensor placed where it does not see the real condition, make a clean-looking record that is wrong.

## Key equations

Load cell output voltage at force $F$, with sensitivity $S$ (V/V, quoted in mV/V), excitation $V_{ex}$ (V), and rated capacity $F_{rated}$ (N):

$$
V_{out} = S\,V_{ex}\,\frac{F}{F_{rated}}
$$

Torque wrench setting with an in-line extension. The wrench has effective length $L$ (m), the extension adds $E$ (m), the torque you want on the fastener is $T_{applied}$ (N m), and $T_{set}$ (N m) is the value to dial in:

$$
T_{set} = T_{applied}\,\frac{L}{L+E}
$$

Infrared spot diameter at distance $D$ (m) for a distance-to-spot ratio $r$ (dimensionless, quoted as $r$:1):

$$
d = \frac{D}{r}
$$

Apparent temperature read by an infrared thermometer set to $\varepsilon = 1$, for a surface at $T_s$ (K) with emissivity $\varepsilon$, reflecting surroundings at $T_a$ (K). This holds for a surface that emits like a gray body in the instrument's band and reflects the surroundings diffusely:

$$
T_{app}^4 = \varepsilon\,T_s^4 + (1-\varepsilon)\,T_a^4
$$

Sound pressure level for a rms pressure $p$ and a reference pressure $p_{ref}$ (both Pa), and the level of several sources whose powers add:

$$
L = 20\log_{10}\frac{p}{p_{ref}}, \qquad L_{total} = 10\log_{10}\sum_i 10^{L_i/10}
$$

Arithmetic mean roughness from $n$ equally spaced height readings $z_i$ (m) measured from the mean line:

$$
R_a = \frac{1}{n}\sum_{i=1}^{n}\left|z_i\right|
$$

## Worked example

### Infrared thermometer spot size

An IR thermometer has a distance-to-spot ratio of 12:1. You aim it at a warm bearing housing 80 mm across from a distance of 1.5 m.

**Given:** $r = 12$, $D = 1.5$ m, target width 80 mm.

**Find:** The spot diameter, whether it fits on the target, and the greatest distance at which it would.

**Assumptions:** The nominal spot is a circle of diameter $D/r$. For this example, the target width is at least twice the nominal spot diameter.

**Solution:**

1. Spot diameter: $d = D/r = 0.125$ m, which is 125 mm.
2. 125 mm is larger than the 80 mm target, so part of the reading comes from the background.
3. For a two-to-one target-to-spot margin, require $d \le 0.040$ m, so $D \le r \times 0.040$ m $= 0.48$ m.

**Answer:** The spot is 125 mm across and does not fit. Move to within 0.48 m for a 40 mm nominal spot, half the target width.

**Sanity check:** The spot shrinks in proportion to distance. At 0.75 m the spot is 62.5 mm, which is smaller than the 80 mm target but does not meet the two-to-one margin. At 0.48 m it is 40 mm.

<details><summary>Verification</summary>

```verify
given("10")
r = q(12, "1")
D = q(1.5, "m")
w = q(80, "mm")
d = D / r
expect(d, "0.125 m")
expect(d, "125 mm")
expect(q(0.08, "m"), "80 mm")
check(d > w, "the spot is larger than the target")
Dmax = r * w / 2
expect(w / 2, "0.040 m")
expect(Dmax, "0.48 m")
expect(Dmax / r, "40 mm")
spot075 = q(0.75, "m") / r
expect(spot075, "62.5 mm")
check(spot075 < w and spot075 > w / 2, "0.75 m is smaller than the target but misses the two-to-one margin")
check(Dmax / r == w / 2, "the spot is half the target width at the selected distance")
```

</details>

### Emissivity error on a shiny surface

A polished aluminium bracket is at 100 degrees Celsius in a room at 20 degrees Celsius. Its emissivity is about 0.10. An IR thermometer set to emissivity 1.0 is aimed at it.

**Given:** $T_s = 100$ degrees Celsius, $T_a = 20$ degrees Celsius, $\varepsilon = 0.10$.

**Find:** The apparent temperature the thermometer reports.

**Assumptions:** A gray-body surface that reflects the room diffusely, and a thermometer that attributes all the radiation it receives to the surface.

**Solution:**

1. Convert to kelvin: $T_s = 373.15$ K and $T_a = 293.15$ K.
2. $T_{app}^4 = \varepsilon\,T_s^4 + (1-\varepsilon)\,T_a^4$, so $T_{app} = 304.4$ K.
3. In Celsius that is 31.2 degrees Celsius.

**Answer:** The thermometer shows about 31.2 degrees Celsius for a bracket at 100 degrees Celsius, an error of about 69 kelvin.

**Sanity check:** With $\varepsilon = 1$ the formula gives $T_{app} = T_s$, and with $\varepsilon \to 0$ it gives $T_a$. The reading falls between the room and the surface and is near the room temperature, as expected for a mirror-like surface.

<details><summary>Verification</summary>

```verify
given("10")
t0 = const("t_celsius_zero")
Ts = t0 + q(100, "K")
Ta = t0 + q(20, "K")
expect(Ts, "373.15 K")
expect(Ta, "293.15 K")
e = q(0.10, "1")
T4 = e * Ts**4 + (1 - e) * Ta**4
Tapp = T4**0.25
expect(Tapp, "304.4 K")
expect(Tapp - t0, "31.2 K")
expect(Ts - Tapp, "69 K")
check(Tapp > Ta and Tapp < Ts, "reading lies between room and surface")
```

</details>

### Adding two sound sources

Two machines run in one room. Alone, machine A measures 85 dB and machine B measures 82 dB at the same position.

**Given:** $L_A = 85$ dB, $L_B = 82$ dB.

**Find:** The level with both running.

**Assumptions:** The sources are independent, so their sound powers add.

**Solution:**

1. Convert each level to a power ratio, $10^{L/10}$.
2. Sum and take the logarithm: $L_{total} = 10\log_{10}(10^{L_A/10} + 10^{L_B/10}) = 86.8$ dB.

**Answer:** Both together give about 86.8 dB, only 1.8 dB above the louder machine.

**Sanity check:** Two equal 85 dB machines would give $L_A + 10\log_{10}2 = 88.0$ dB, which is 3.01 dB higher. A quieter second machine adds less than that, so 86.8 dB lies between 85 dB and 88.0 dB.

<details><summary>Verification</summary>

```verify
given("10")
LA = q(85, "1")
LB = q(82, "1")
Lt = 10 * log10(10**(LA / 10) + 10**(LB / 10))
expect(Lt, "86.8 1")
expect(Lt - LA, "1.8 1")
Leq = 10 * log10(2 * 10**(LA / 10))
expect(Leq, "88.0 1")
expect(Leq - LA, "3.01 1")
check(Lt > LA and Lt < Leq, "between one machine and two equal machines")
```

</details>

## Practice

1. A load cell has a rated output of 2 mV/V at a capacity of 1000 N. It is powered with 10 V. Find the output voltage in mV when it carries 250 N.
2. A click-type torque wrench has an effective length of 0.40 m. You add a straight extension 0.10 m long in line with it and want 80 N m on the fastener. Find the setting in N m.
3. A machine measures 90 dB alone, and a second one adds 80 dB. Find the combined level in dB, and say whether the second machine matters.
4. Eight readings of height from the mean line, in micrometres, are 2, -3, 1, -2, 2, -1, 3, -2. Find Ra in micrometres.
5. An IR thermometer reads 31 degrees Celsius on a polished steel pan that feels too hot to touch. Give two reasons the reading may be wrong and one way to get a better value.

<details><summary>Answers</summary>

1. 5 mV
2. 64 N m
3. 90.4 dB. The second machine adds only 0.4 dB, so it does not matter for the total level.
4. 2.0 micrometres
5. The polished metal has a low emissivity, so the thermometer reads mostly the reflected room. The spot may also include background. Cover a patch with matt tape or paint, and measure the patch, or use a contact probe.

```verify
S = q(2, "mV")
Vex = q(10, "1")
F = q(250, "N")
Fr = q(1000, "N")
expect(S * Vex * F / Fr, "5 mV", ans=1)
L = q(0.40, "m")
E = q(0.10, "m")
Ta = q(80, "N m")
expect(Ta * L / (L + E), "64 N m", ans=2)
L1 = q(90, "1")
L2 = q(80, "1")
Lt = 10 * log10(10**(L1 / 10) + 10**(L2 / 10))
expect(Lt, "90.4 1", ans=3)
expect(Lt - L1, "0.4 1", ans=3)
z1 = q(2, "um")
z2 = q(-3, "um")
z3 = q(1, "um")
z4 = q(-2, "um")
z5 = q(2, "um")
z6 = q(-1, "um")
z7 = q(3, "um")
z8 = q(-2, "um")
zmean = (z1 + z2 + z3 + z4 + z5 + z6 + z7 + z8) / 8
check(abs(zmean) < q(0.001, "um"), "readings are from the mean line")
Ra = (abs(z1) + abs(z2) + abs(z3) + abs(z4) + abs(z5) + abs(z6) + abs(z7) + abs(z8)) / 8
expect(Ra, "2.0 um", ans=4)
skip(ans=5, why="short answer")
```

</details>

## Common mistakes

- Reading a number to its last digit and ignoring the accuracy. A display with many digits is not an accurate one.
- Skipping the zero check and the check against a known before and after the job.
- Pulling a load cell or force gauge off its axis, or loading it past its capacity.
- Using a torque wrench with an extension and no correction, or storing it under load.
- Using a contact tachometer on rotating machinery when an optical one would do, or stopping at the first still image of a stroboscope.
- Pointing an IR thermometer at shiny metal, through glass, or at a target smaller than its spot.
- Adding decibels as ordinary numbers.
- Taking a single hardness or roughness reading, or reading roughness along the machining lay.
- Starting a data logger without checking that it records, and without a note of when it started.

## Go deeper

- [OSHA: Occupational noise exposure](https://www.osha.gov/noise) by the U.S. Department of Labor: how noise damages hearing and what the exposure limits are.
- [OSHA: Machine guarding](https://www.osha.gov/machine-guarding) by the U.S. Department of Labor: why you measure rotating machinery from outside the danger zone.
- [*NIST Special Publication 811*](https://www.nist.gov/pml/special-publication-811) by NIST: unit use for the quantities in this lesson.
- Previous: [Hand and power tools](16-hand-and-power-tools.md) and [Measurement tools](07-measurement-tools.md).
- Related: [Strain gauges and the Wheatstone bridge](../measurement/06-strain-gauges-and-wheatstone-bridge.md), [Thermocouples and accelerometers](../measurement/07-thermocouples-and-accelerometers.md), [Data acquisition and sampling](../measurement/08-data-acquisition-and-sampling.md).
