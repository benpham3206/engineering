# Sensors in products: phones, cars, and appliances

**Type:** lesson

A **sensor** is a part that turns a physical quantity, such as acceleration, temperature, or a magnetic field, into an electrical signal that a product can read. Engineers need to understand these sensors because the accuracy a user sees depends on the sensor and on every electronic stage that follows it.

A phone, car, or appliance reads the world through a small set of sensors. Accelerometers, thermistors, Hall-effect sensors, and image sensors cover most of what these products measure. Engineers pick a sensor for its signal, its power draw, and how well it survives the product's environment.

**Prerequisites:** [Sensors and transducers](../../measurement/05-sensors-and-transducers.md), [Circuit basics](01-circuit-basics.md), [RC circuits and op-amp basics](02-rc-circuits-and-op-amps.md), [Semiconductors](03-semiconductors-diodes-and-transistors.md)
**Time:** 6-8 h

## Core ideas

- A product sensor is one stage in a **signal chain**. The chain runs from the physical effect to the sensing element, then to an analog front end that amplifies and filters the signal, then to an analog-to-digital converter (ADC), and finally to firmware that calibrates and acts on the number.
- Each stage adds noise, offset, and power draw. The error a reader sees is the sum of every stage, so the sensing element alone does not set the accuracy.
- Most sensors in consumer products are MEMS parts (micro-electromechanical systems). A **MEMS sensor** is a tiny silicon structure made with the same kind of process used for chips. MEMS parts are cheap, small, and low in power, which is why they appear in phones and cars.
- Four sensing effects cover most products. Capacitance changes in accelerometers and pressure sensors. Resistance changes with temperature in thermistors. The Hall effect responds to magnetic fields. Photons create charge in image sensors.
- The factory usually calibrates each part. It stores offset and gain corrections in memory, and the firmware applies them at run time.

### How it works

**Accelerometer.** A MEMS accelerometer etches a small silicon block, the **proof mass**, on thin silicon springs. The surrounding frame is fixed to the product. When the product accelerates, the proof mass lags behind by Newton's second law and moves relative to the frame. Fixed plates and plates on the proof mass form capacitors. As the gap changes, the capacitance changes, and the readout circuit turns that change into a voltage or a digital number.

An accelerometer measures **specific force**, not acceleration in the everyday sense. A phone lying flat on a table reads about 9.81 m/s$^2$ upward on its vertical axis at Earth's surface, because the table pushes up on it. Only a phone in free fall reads zero. Typical phone accelerometers have ranges of $\pm 2$ g to $\pm 16$ g.

**Thermistor.** A negative-temperature-coefficient (NTC) thermistor is a ceramic made from metal oxides. Its resistance falls as temperature rises, because more charge carriers become free to move. Its resistance follows an exponential curve in $1/T$. In a product, the thermistor forms one leg of a voltage divider with a fixed resistor. The ADC reads the midpoint voltage. Battery packs, chargers, kettles, and engine coolant sensors use this arrangement.

**Hall-effect sensor.** A Hall element is a thin, flat piece of semiconductor with a current flowing through it. A magnetic field perpendicular to the current pushes the moving charges toward one side of the element. That charge buildup creates a small voltage across the width, called the Hall voltage. A linear Hall sensor gives an output voltage that is proportional to the field. A switch-type Hall sensor gives a digital high or low when the field passes a threshold. Products use Hall sensors to detect a closed lid with a magnet, to read wheel speed from a toothed ring, and to find the rotor position in brushless motors in fans, compressors, and power tools.

**Image sensor.** A CMOS image sensor is a grid of pixels, and each pixel holds a photodiode. A photon with energy above the silicon bandgap (about 1.1 eV) frees an electron-hole pair. The charge builds up during the exposure. The readout converts each pixel's charge to a voltage, and the ADC turns that voltage into a number. The number of electrons in a pixel sets the signal, and random electron arrival sets the noise.

### Main parts

| Stage | What it does | Example in a phone |
|---|---|---|
| Sensing element | Turns the measured quantity into a change in capacitance, resistance, voltage, or charge | Proof mass and plates in an accelerometer |
| Analog front end | Biases, amplifies, and filters the small signal | Low-noise amplifier and low-pass filter |
| ADC | Converts the voltage into a number | ADC inside the sensor package or in the processor |
| Firmware | Applies calibration, filters readings, and sets thresholds | Averages gyroscope readings and rejects spikes |

### Variants

- Accelerometers. Capacitive MEMS parts dominate phones and cars because they are stable and low in power. Piezoresistive parts, which change resistance under strain, appear in some pressure and high-shock sensors.
- **Gyroscopes.** A vibrating MEMS structure measures rotation. Coriolis forces shift the vibration when the part turns, and the shift gives the rotation rate.
- Thermistors and RTDs. NTC thermistors are cheap and sensitive, and they suit a limited range such as 0 to 100 °C. Platinum resistance temperature detectors (RTDs) are more linear and stable, and industrial equipment uses them over wider ranges.
- Hall sensors. Linear parts measure field strength. Switch parts give a yes-or-no answer and are simpler to use for lid, position, and speed detection.
- Image sensors. CMOS sensors dominate phones and cameras. CCD sensors, which move charge across the chip to one output, appear in some scientific and astronomy cameras.

## Key equations

Thermistor, beta model:

$$R = R_0 \exp\left[B\left(\frac{1}{T} - \frac{1}{T_0}\right)\right]$$

where $R$ is the thermistor resistance in ohms ($\Omega$), $T$ is its temperature in kelvin (K), $R_0 = 10\ \text{k}\Omega$ is the resistance at the reference temperature $T_0 = 298.15$ K (25 °C), and $B$ is the material constant in kelvin. Typical NTC values of $B$ are 3000 K to 4500 K.

Voltage divider with a thermistor to ground:

$$V_{\mathrm{out}} = V_s \frac{R}{R + R_f}$$

where $V_{\mathrm{out}}$ and $V_s$ are volts (V), and $R_f$ is the fixed resistor in ohms.

ADC code for an $n$-bit converter with reference voltage $V_{\mathrm{ref}}$ in volts:

$$N = \operatorname{round}\left(\frac{V_{\mathrm{out}}}{V_{\mathrm{ref}}} \, 2^n\right)$$

Hall voltage for a current $I$ in amperes through a plate of thickness $t$ in metres, in a field $B$ in tesla (T):

$$V_H = \frac{I B}{n e t}$$

where $n$ is the charge carrier density in m$^{-3}$ and $e = 1.602 \times 10^{-19}$ C is the elementary charge.

Accelerometer displacement at steady acceleration $a$ (m/s$^2$), for proof mass $m$ in kilograms and suspension stiffness $k$ in newtons per metre:

$$x = \frac{m a}{k}$$

For a small displacement $x$ across a gap $d$ in metres, the capacitance changes by $\Delta C / C_0 \approx x / d$, where $C_0$ is the capacitance at rest in farads (F).

Photon energy for wavelength $\lambda$ in metres:

$$E = \frac{h c}{\lambda}$$

where $h = 6.626 \times 10^{-34}$ J s is Planck's constant and $c = 2.998 \times 10^{8}$ m/s is the speed of light. Shot noise in a pixel that collects $N$ electrons gives a signal-to-noise ratio of $\sqrt{N}$.

## Worked example

**Given:** A battery pack uses an NTC thermistor with $R_0 = 10\ \text{k}\Omega$ at 25 °C and $B = 3950$ K. A fixed $10\ \text{k}\Omega$ resistor connects the 3.3 V supply to the midpoint, and the thermistor connects the midpoint to ground. The ADC has 12 bits and a 3.3 V reference.

**Find:** (a) the thermistor resistance at 45 °C, (b) the divider voltage at 45 °C, (c) the ADC code, and (d) the temperature change that one ADC count represents near 45 °C.

**Assumptions:** The beta model holds from 25 °C to 45 °C. The ADC draws negligible current. The divider current is about 0.23 mA, so self-heating is small and we ignore it.

**Solution:**

1. (a) The temperatures are $T = 318.15$ K and $T_0 = 298.15$ K. Then $1/T - 1/T_0 = -2.11 \times 10^{-4}$ K$^{-1}$. The exponent is $3950 \times (-2.11 \times 10^{-4}) = -0.833$, and $R = 10\ \text{k}\Omega \times e^{-0.833} = 4.35\ \text{k}\Omega$.
2. (b) $V_{\mathrm{out}} = 3.3\ \text{V} \times \dfrac{4348}{4348 + 10000} = 1.00\ \text{V}$.
3. (c) $N = \dfrac{1.00}{3.3} \times 4096 = 1241$.
4. (d) The ADC step is $3.3\ \text{V} / 4096 = 0.806$ mV. Differentiating the divider with the beta model gives $dV_{\mathrm{out}}/dT \approx -27.2$ mV/K at 45 °C. One count is $0.806 / 27.2 = 0.030$ K.

**Answer:** (a) $R \approx 4.35\ \text{k}\Omega$. (b) $V_{\mathrm{out}} = 1.00\ \text{V}$. (c) $N = 1241$. (d) About $0.03$ K per count.

**Sanity check:** At 25 °C the thermistor equals the fixed resistor, so the output is $3.3 / 2 = 1.65$ V. The output falls to 1.00 V at 45 °C, so the average slope over those 20 K is $0.65\ \text{V} / 20\ \text{K} = 32$ mV/K. That is steeper than the local slope at 45 °C, which fits a curve that flattens as it warms.

## Design trade-offs

- **Power.** Many MEMS accelerometers draw microamps in low-power modes, so a phone can sense motion all day. A sensor that samples at a higher rate uses more power, so designers sample only as fast as the task needs.
- **Noise and bandwidth.** For white noise, halving the bandwidth cuts the RMS noise by a factor of $\sqrt{2}$. A slower filter reads more steadily but responds more slowly, so a step detector and a balance display need different filters.
- **Pixel size.** For the same light per unit area, a pixel with half the pitch collects about one quarter as many photons. That is why small phone pixels are noisy in dim light. Phones combine neighboring pixels ("binning") to recover signal.
- **Self-heating.** The thermistor in the example dissipates $P = I^2 R = (0.23\ \text{mA})^2 \times 4.35\ \text{k}\Omega \approx 0.23$ mW. A higher divider current would warm the thermistor and add error.
- **Environment.** Automotive parts are often rated from $-40$ °C to 125 °C (AEC-Q100 Grade 1). A part that works on a bench can drift or fail under engine heat and road shock.
- **Size and cost.** A MEMS accelerometer package is a few millimetres across. Its small size and low price let designers place several sensors in one product.

## How it fails

- **Accelerometer shock.** A drop that moves the proof mass beyond its travel can break a spring or make the mass stick to a plate. Internal mechanical stops limit the travel. A warning sign is a reading pinned at the full-scale value.
- **Thermistor open or short.** An open thermistor pulls the midpoint up to the supply voltage, so the ADC reads full scale, which looks like a very cold part. A shorted thermistor reads as very hot. Firmware should check for readings at both ends of the range and treat them as faults. Battery packs use this kind of check to cut charging when a cell overheats, which protects against thermal runaway (see [Batteries](../electrical/06-batteries.md)).
- **Hall sensor drift and stray fields.** A nearby steel part or a second magnet shifts the field the sensor sees. Temperature changes the sensitivity. A warning sign is a switch that chatters near its threshold. Designers add hysteresis, so the output switches on at one level and off at a lower one.
- **Image sensor saturation.** A bright area fills each pixel's well and clips to white. Heat raises the dark current and adds hot pixels. Rolling shutter skews fast-moving objects, because the rows are read at different times.

## History

Edwin Hall discovered the Hall effect in 1879 while he was a graduate student at Johns Hopkins University in Baltimore. Willard Boyle and George Smith at Bell Labs invented the charge-coupled device (CCD) in 1969. Analog Devices introduced an early commercial surface-micromachined accelerometer in the early 1990s, and MEMS accelerometers spread into consumer products after that. Eric Fossum and colleagues at NASA's Jet Propulsion Laboratory developed the CMOS active-pixel image sensor in the early 1990s. The first iPhone, in 2007, used an accelerometer to rotate the screen.

## Practice

1. A MEMS accelerometer has a proof mass $m = 0.5$ mg and a suspension stiffness $k = 5\ \text{N/m}$. Find the displacement at 1 g (Earth surface, $9.81\ \text{m}/\text{s}^2$).
2. The thermistor in the worked example has $R_0 = 10\ \text{k}\Omega$ at 25 °C and $B = 3950$ K. Find its resistance at 85 °C.
3. A Hall element carries 5 mA and has a carrier density of $10^{22}$ m$^{-3}$ and a thickness of 0.2 mm. Find the Hall voltage at 10 mT. Then find it at 20 mT, and say how the output changes with the field.
4. Find the energy of a 500 nm photon in electronvolts. Can silicon, with a bandgap of about 1.1 eV, detect it?
5. A 12-bit ADC reads the thermistor divider from the worked example, but the thermistor has an open circuit. What code does the ADC read, and what should the firmware conclude?

<details><summary>Answers</summary>

1. $x = m a / k = (5 \times 10^{-7}\ \text{kg})(9.81\ \text{m}/\text{s}^2) / (5\ \text{N/m}) = 9.8 \times 10^{-7}$ m, which is $0.98\ \mu\text{m}$.
2. $R \approx 1.09\ \text{k}\Omega$.
3. At 10 mT, $V_H = 0.156$ mV. At 20 mT, $V_H = 0.31$ mV. The output doubles because $V_H$ is proportional to $B$.
4. $E = 2.48$ eV. Yes, silicon detects it, because the photon energy is well above the 1.1 eV bandgap.
5. The node is pulled up to 3.3 V, so the ADC reads full scale, $N = 4095$. Firmware should flag this as a sensor fault, not as a very cold reading.

</details>

## Common mistakes

- Treating an NTC thermistor as linear. Its resistance changes exponentially with $1/T$, so a straight-line fit over a wide range gives large errors.
- Reading an accelerometer at rest as zero acceleration. At rest it reads 1 g upward, and the tilt of the product decides which axis carries that reading.
- Forgetting self-heating. Current through a thermistor warms it, and the warming adds error. Keep the divider current low.
- Assuming more megapixels means better low-light images. The area of each pixel sets how many electrons it collects, and that sets the noise.
- Mounting a Hall sensor with the magnet at the wrong angle or distance. The sensor responds to the field component perpendicular to its face, so the output depends on the layout.

## Go deeper

- [Circuits and Electronics (6.002), MIT OpenCourseWare](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/) by MIT: circuit design for sensor front ends and amplifiers.
- [*University Physics Volume 2*, Chapter 11](https://openstax.org/books/university-physics-volume-2/pages/11-introduction) by OpenStax: magnetic forces on charges, including the Hall effect in section 11.6.
- Related lessons: [Mechatronics](06-mechatronics.md), [Electricity and magnetism](../../physics/06-electricity-and-magnetism.md), [Accelerometers and thermocouples](../../measurement/07-thermocouples-and-accelerometers.md), [Data acquisition and sampling](../../measurement/08-data-acquisition-and-sampling.md), [Brushless and stepper motors](../electrical/02-brushless-and-stepper-motors.md), [Cars](../vehicles-aerospace/02-cars.md), and [Cameras and lenses](../waves-and-communication/05-cameras-and-lenses.md).
- [Applications reference](../reference.md): the lookup sheet for this topic.
