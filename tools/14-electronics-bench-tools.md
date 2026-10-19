# Electronics bench tools

**Type:** lesson
**Verify:** strict

The **electronics bench tools** are the instruments and hand tools used to power, stimulate, observe, and assemble a circuit on a workbench: a bench power supply, an oscilloscope, a function generator, a soldering iron, a breadboard, and a logic analyzer. A circuit on paper obeys equations; a circuit on a bench obeys those equations plus the limits of the tools, and an engineer who knows those limits can tell a real signal from an artifact and can avoid destroying parts, boards, or a hand.

This lesson assumes you have never used any of them. It follows the order of a first session at the bench: power a circuit safely, look at what it does, drive it with a test signal, and build or repair it. The `13-multimeters` lesson covers the multimeter, which is not repeated here.

**Prerequisites:** [Circuit basics](../applications/electronics/01-circuit-basics.md), [RC circuits and op-amps](../applications/electronics/02-rc-circuits-and-op-amps.md), [Printed circuit boards](../applications/electronics/04-printed-circuit-boards.md), [Data acquisition and sampling](../measurement/08-data-acquisition-and-sampling.md)
**Time:** 6-8 h of reading, plus supervised practice at a bench

## Core ideas

### The bench power supply

A **bench power supply** is a source whose output voltage and maximum output current you set with knobs. It works in one of two modes at any instant.

- In **constant-voltage (CV) mode** the supply holds the voltage you set, and the load decides the current by Ohm's law. This is the normal mode.
- In **constant-current (CC) mode** the supply has reached the **current limit** you set. It lowers its output voltage as far as needed to hold the current at that limit, and the load voltage becomes $I_{lim} R$.

The mode changes by itself at the **crossover resistance** $R_x = V_{set}/I_{lim}$. A load resistance above $R_x$ draws less than the limit, so the supply stays in CV. A load below $R_x$ would draw more than the limit, so the supply drops into CC.

The current limit is what protects the circuit. A wiring mistake, a reversed capacitor, or a solder bridge makes a very low resistance, and without a limit the supply would push whatever current the low resistance allows, heating the fault until something burns. With the limit set low, the supply caps the current, and the fault dissipates only $I_{lim}^2 R$, which for a short is tiny.

The safe first use, in order:

1. Turn the output off. Set the voltage to the value the circuit needs.
2. Short the two output leads together, or use the supply's own limit-set function if it has one, and turn the current limit knob until the display shows the limit you want. Remove the short. Choose a limit a little above the current you expect the circuit to draw, so a fault trips it.
3. Connect the leads to the circuit with the output still off, red to the positive input and black to the return, then turn the output on and watch the current reading.
4. If the supply goes into CC mode at once, or the current is far from what you calculated, turn the output off and look for the fault before raising the limit.

Many bench supplies have two or three isolated outputs. A floating output has no connection to earth, which is what allows a positive and a negative rail to be built from two outputs wired in series, and it prevents the supply's return from clashing with an earthed instrument.

### The oscilloscope

An **oscilloscope** plots a voltage against time. The vertical axis is voltage, the horizontal axis is time, and the trace you see is the signal as it repeats or as it happened once. It shows what a multimeter hides: the shape, the noise, the timing between two signals, and glitches too brief for any meter.

The screen is divided into a grid of **divisions**. Two knobs set the scale.

- **Volts per division** sets how many volts one vertical division represents. At 2 V/div, a trace 3 divisions tall is 6 V tall.
- **Time per division** sets how many seconds one horizontal division represents. At 0.5 ms/div, a wave that repeats every 4 divisions has a period of 2 ms.

A reading is the number of divisions you count, times the setting. Count divisions, then multiply; the numbers on the screen are what the scope believes, and the probe setting must match the probe (below) for those numbers to be true.

**Triggering** decides where on the signal each sweep starts. A repeating wave drawn from a different starting point on each sweep appears to slide across the screen. The scope fixes this by starting every sweep at the same event: the signal crossing a chosen voltage, the **trigger level**, in a chosen direction, rising or falling edge. Set the trigger source to the channel you are viewing, put the level inside the signal's swing, and the picture holds still. If the picture will not hold still, the level is outside the signal, or the wrong edge or channel is chosen.

Three more controls matter from the start. The **coupling** switch chooses DC, which shows the whole signal, AC, which blocks the average (DC) part so a small ripple on a large level can be magnified, or ground, which shows where zero volts sits. Vertical **position** moves the trace up or down so you can place that zero line. **Single** mode catches one event and holds it, for a signal that happens once.

### Probes, and the 10x setting

A **probe** is the lead that carries the signal from the circuit to the scope. A plain wire would load a circuit and pick up noise, so a real probe is built to do neither. A **10x probe** holds a series resistor about nine times the scope's input resistance, so together they divide the signal by 10. The scope input would otherwise load the circuit with its own resistance and with the cable capacitance, and the divider cuts that load. The price is a signal one tenth as large at the input, which the scope restores when you set the channel's probe setting to 10x. Set the setting to match the probe, or every voltage reading will be wrong by a factor of 10.

Because the probe is a resistive divider with cable capacitance after it, it needs a small trimmer capacitor to make the divider equal at all frequencies. The condition is that the product of the upper resistance and its capacitance equals the product of the lower resistance and its capacitance, which makes the attenuation the same at every frequency. **Probe compensation** is adjusting that trimmer. Connect the probe to the scope's square-wave test output and adjust the trimmer with a small screwdriver until the top of the square wave is flat. Rounded corners mean undercompensated; a spike on the corner and a sloping top mean overcompensated. Do this each time you move a probe to a different channel.

Most probes have a switch for 1x and 10x. Use 10x for general work. Use 1x only for tiny signals, and remember that 1x loads the circuit more and has far less bandwidth.

### Bandwidth and rise time

The **bandwidth** of a scope is the frequency at which a sine wave appears about 30 percent smaller than it really is (the $-3\ \text{dB}$ point). A scope also has a **rise time**, the time its own response needs to go from 10 percent to 90 percent of a step. For an instrument that behaves like a single RC low-pass filter, the two are linked. A step through an RC filter has a 10 to 90 percent rise time of $t_r = 2.2\,RC$, and the filter's $-3\ \text{dB}$ bandwidth is $BW = 1/(2\pi RC)$, so

$$
t_r \, BW = \frac{2.2}{2\pi} = 0.35
$$

Many scopes behave close to this model, which is why the rule works well. It is only the model for a simple low-pass response. A scope with a sharp, flat-top response has a somewhat different constant, so treat 0.35 as the usual figure for scopes of moderate bandwidth and read the manual for the exact one.

What matters at the bench is that the scope and the signal's edge add in quadrature. The rise time you see is $t_{meas} = \sqrt{t_{sig}^2 + t_{scope}^2}$. If the scope is as fast as the edge, the picture is wrong by more than 40 percent. A common rule of thumb is to choose a scope with a bandwidth at least five times the highest frequency content of the signal, which keeps the rise-time error near 2 percent. The frequency content of a fast edge is about $0.35/t_r$, not just the repetition rate of the wave: a 1 MHz square wave with a 5 ns edge needs far more than 5 MHz.

The probe's bandwidth counts too. The bandwidth of the whole system is set by the slower of the probe and the scope.

> [!WARNING]
> A scope's probe ground clip is connected to the mains safety earth through the scope's power cord. Clipping it onto a circuit that is referenced to the mains, such as the primary side of a switching power supply or any circuit plugged into the wall without an isolating transformer, connects that circuit to earth through the clip and the cord. The result is a short, a flash, burned parts, or a shock. Never defeat the earth pin on a scope's plug to get around this. Measure mains-referenced circuits only with an isolation transformer feeding the circuit, a differential probe, or a battery-powered scope, and only if you have been trained to work on mains circuits. A probe's tip and ground clip are both at the scope's earth, so never clip the ground lead to a point that is not at earth potential unless you know why.

### Reading amplitude, period, frequency, and duty cycle

Four numbers describe most repeating waves. Read them from the screen by counting divisions.

- **Peak-to-peak voltage** ($V_{pp}$) is the vertical distance from the lowest to the highest point of the wave, times volts per division. **Amplitude** is half of it for a sine wave about zero.
- **Period** ($T$) is the horizontal distance of one full cycle, times time per division. **Frequency** is $f = 1/T$.
- **Duty cycle** ($D$) is the fraction of each period that a wave spends high, $D = t_{high}/T$. A symmetric square wave has $D = 0.5$.
- For a signal that is only high or low, the average (DC) value is $V_{low} + D\,V_{pp}$.

Most scopes also compute these for you as **measurements** or **cursors**. Use them, but check one by hand at least once: a measurement of the wrong channel or a trace that is clipped off the top of the screen will be computed confidently and be wrong.

### The function generator

A **function generator** produces a chosen waveform at a chosen frequency, so you can test a circuit with a known input. The usual waveforms are the sine, the square (with an adjustable duty cycle), and the triangle. The controls are frequency, **amplitude**, and **offset**, a constant voltage added to the wave. A wave of amplitude $A$ (peak-to-peak $2A$) and offset $V_{os}$ swings from $V_{os} - A$ to $V_{os} + A$, so check that offset plus peak does not drive the circuit input past its supply or its safe range.

A function generator has an internal **output resistance** of $R_s = 50\ \Omega$ in nearly all cases. The output is the wave behind this resistance. When it drives a load $R_L$, the load sees the divider

$$
V_{out} = V_{oc}\,\frac{R_L}{R_L + R_s}
$$

where $V_{oc}$ is the open-circuit voltage, the voltage with nothing connected. Generators are usually calibrated to assume a $50\ \Omega$ load: the amplitude you set is what appears across $50\ \Omega$, which is half of $V_{oc}$. If the generator instead drives a high-impedance load, such as a scope input or a circuit input of $1\ \text{M}\Omega$, almost none of the voltage divides away, and the load sees $V_{oc}$, which is twice the number on the display. This is the **doubling surprise**: you set 2 V and the scope shows 4 V. Many generators have an output setting that tells them the load is high impedance, so the display tells the truth. Check which one yours is using.

Never connect a generator output to a powered circuit's output, or to a supply rail. The output can be damaged by current forced back into it.

### The logic analyzer

A **logic analyzer** records many digital signals at once, each only as high or low, and shows them as timing diagrams. It is a variant of the scope for digital work. A scope shows the analog shape of one to four signals; a logic analyzer shows the ones and zeros of eight to dozens of signals, and can decode them into bus data such as the bytes on an SPI or I2C link.

It samples each line at a fixed **sample rate** and compares each sample with a threshold voltage. The sample rate sets the resolution of when an edge occurred: one sample period. Sampling a 1 MHz signal at 10 million samples per second places each edge to within 100 ns, one tenth of the period, which is usually enough to see the data and not enough to see a glitch narrower than 100 ns. Set the threshold for the logic family under test (the voltage that separates low from high in the circuit you are probing), connect a ground lead, trigger on a pattern or an edge, and capture. Because the analyzer reduces each line to high or low, it cannot show ringing, slow edges, or noise. Use the scope for those.

### Soldering

**Soldering** joins metal parts by melting a filler metal, the **solder**, into the joint so it wets both surfaces and solidifies as an electrical and mechanical connection. It is how components are fixed to a board, and the quality of the joint decides whether a circuit works for years or fails when it is bumped.

The parts of a bench kit:

- A **soldering iron** is a heater with a replaceable metal **tip**. A station holds the tip at a set temperature with a feedback sensor. Set the temperature from the data sheet of the solder you are using: the tip must be well above the solder's melting point, because the tip cools as it gives heat to the pad and lead, but not so hot that it lifts pads or damages parts. Leaded solder melts at a lower temperature than lead-free solder, so lead-free work uses a hotter setting. Use the lowest temperature that makes a good joint in a second or two, and read the solder maker's guidance for the actual figure.
- **Solder** for electronics is usually a wire with a core of **flux**. Flux is a chemical that cleans the metal surfaces of oxide as the solder melts, so the solder can wet them. Without flux, the solder beads up and does not bond.
- A **sponge or brass wool** cleans the tip. A clean tip is shiny and silver. A black, oxidised tip does not transfer heat.

**Tinning** is coating the tip with a thin layer of fresh solder before and after use. A tinned tip passes heat to the joint through a thin film of liquid metal instead of through a dry point of contact, and the coating protects the tip from oxidising when idle.

To make a through-hole joint, place the component lead in its hole, touch the tip so it contacts both the pad and the lead at the same time, and after about a second feed the solder to the joint, not to the tip. When the solder has flowed around the lead, remove the solder and then the iron, and hold the part still until the solder freezes. A good joint is shiny and smooth, shaped like a small cone that rises from the pad to the lead (a concave fillet), and fully wets both the pad and the lead. A **cold joint** is one where the solder never fully melted or wetted, because the joint was too cool, was moved while it froze, or was dirty. It looks dull, grainy, or lumpy, may sit as a ball on top of the pad, and conducts badly or intermittently. It is the most common cause of a circuit that works until it is touched. Reheat it, add a little fresh solder with flux, and let it cool undisturbed.

**Through-hole** parts have leads that pass through holes and are soldered on the opposite side. They are strong and easy to hand solder, so they suit learning and prototypes. **Surface-mount** parts sit on pads on the board's surface, are far smaller, and are usually soldered with a fine tip, flux, and often a hot air tool or reflow oven, as described in [Printed circuit boards](../applications/electronics/04-printed-circuit-boards.md). Use less solder, more flux, and a finer tip, and work in good light with magnification.

**Desoldering** removes solder to take a part off. A **desoldering pump** (a spring-loaded suction tool) or **desoldering braid** (woven copper wick) pulls molten solder away from the joint. Heat the joint, apply the pump or braid, and remove the solder until the lead moves freely. Do not pull a part that is still held, since pads and their traces peel off the board with it.

> [!WARNING]
> A hot iron burns skin and ignites materials, so rest it in its stand, never on the bench, and unplug it or turn it off when you leave. Soldering also produces fumes from the flux that irritate lungs, so work with a fume extractor or good ventilation that draws fumes away from your face. Leaded solder contains lead, which harms the nervous system and is absorbed from contaminated hands. Wash your hands with soap after soldering and before you eat, drink, or touch your face, and do not eat at the bench. Dispose of solder waste as hazardous waste under your workplace rules. Lead-free solder avoids lead, but flux fumes and heat hazards remain. See OSHA's [overview of lead](https://www.osha.gov/lead).

### Breadboards and their limits

A **solderless breadboard** is a plastic board of spring contacts into which you push component leads and jumper wires to build a circuit with no soldering. Rows of holes are connected internally in strips, usually five holes in a row on each side of a central gap, and long **power rails** run along the edges. It is the fastest way to try an idea.

The strips explain the limits. The spring contact has resistance and loses grip with wear, so connections can be intermittent. A thin spring contact is not meant for high current, so it heats and fails when a load draws amperes. Each strip sits next to others, which adds stray capacitance between neighbours, and long jumper wires add inductance. Fast signals, sensitive analog circuits, and anything at high frequency misbehave on a breadboard because of these effects, and ringing or oscillation you see there may not be in the real circuit. Keep wires short, keep rails and signals tidy, and move a working design to a soldered board or a printed circuit board for anything that must be reliable or fast. Some rails are split in the middle, so check that a rail runs the whole length before relying on it.

### Electrostatic discharge

**Electrostatic discharge (ESD)** is the sudden flow of charge between two objects at different electric potentials, such as a charged person and a chip. A person who walks across a carpet or takes off a sweater accumulates charge, and the discharge when they touch a part can pass through the part's tiny internal structures and damage them. You often feel nothing and see nothing, and the part may keep working but fail early.

The precautions are cheap. Keep parts in their antistatic bags until you use them. Work at a surface that is connected to earth through a resistor, and wear a **wrist strap** that connects you to that earth through a resistor, which drains the charge from your body slowly and limits the current if you touch something live. Touch the grounded surface before you pick up a part. Do not wear a wrist strap near a live mains circuit: the strap's resistor limits current but it is not a safety device. Handle boards by their edges and avoid touching pins.

## Key equations

Symbols: $V_{set}$ = set voltage (V), $I_{lim}$ = current limit (A), $R_x$ = crossover resistance ($\Omega$), $N$ = divisions counted, $s_V$ = volts per division (V), $s_t$ = time per division (s), $T$ = period (s), $f$ = frequency (Hz), $t_{high}$ = time high in one period (s), $D$ = duty cycle (dimensionless), $t_r$ = 10 to 90 percent rise time (s), $BW$ = bandwidth (Hz), $t_{sig}$ and $t_{scope}$ = rise times of signal and scope (s), $V_{oc}$ = generator open-circuit voltage (V), $R_s$ = source resistance ($\Omega$), $R_L$ = load resistance ($\Omega$), $V_{out}$ = voltage across the load (V).

Supply crossover between constant-voltage and constant-current mode, for a resistive load:

$$
R_x = \frac{V_{set}}{I_{lim}}, \qquad V_{load} = I_{lim} R_L \ \text{ for } R_L < R_x
$$

Reading a scope screen, where $N$ is the count of divisions:

$$
V_{pp} = N_V\, s_V, \qquad T = N_T\, s_t, \qquad f = \frac{1}{T}, \qquad D = \frac{t_{high}}{T}
$$

Rise time and bandwidth of a single-pole response, and how rise times combine:

$$
t_r = \frac{0.35}{BW}, \qquad t_{meas} = \sqrt{t_{sig}^2 + t_{scope}^2}
$$

Generator output into a load:

$$
V_{out} = V_{oc}\,\frac{R_L}{R_L + R_s}
$$

## Worked example

### Setting a current limit

A bench supply is set to 5.0 V with a current limit of 50 mA. A circuit on it should draw about 20 mA. A solder bridge makes a fault of $0.5\ \Omega$.

**Given:** $V_{set} = 5.0$ V, $I_{lim} = 0.050$ A, fault resistance $R_f = 0.5\ \Omega$.

**Find:** The crossover resistance, the fault current and voltage with the limit set, and the fault current with no limit.

**Assumptions:** A resistive fault, an ideal supply that reaches its limit exactly, and a supply with enough rating to deliver the unlimited current.

**Solution:**

1. Crossover: $R_x = V_{set}/I_{lim} = 100\ \Omega$. A load above this stays in CV mode.
2. The fault of $0.5\ \Omega$ is below $R_x$, so the supply is in CC mode and holds 50 mA.
3. The voltage across the fault is $I_{lim} R_f = 0.025$ V, and the power in it is $I_{lim}^2 R_f = 1.25$ mW.
4. With no limit the fault would draw $V_{set}/R_f = 10$ A and dissipate 50 W.

**Answer:** The limit holds the fault to 50 mA, 0.025 V, and 1.25 mW. Without it the fault would draw 10 A and dissipate 50 W.

**Sanity check:** The 20 mA the circuit should draw is below 50 mA, so the limit does not disturb normal operation. The limit-to-expected ratio is 2.5, a margin that still trips a hard fault.

<details><summary>Verification</summary>

```verify
V = q(5.0, "V")
Ilim = q(0.050, "A")
Rf = q(0.5, "ohm")
Rx = V / Ilim
expect(Rx, "100 ohm")
Vf = Ilim * Rf
expect(Vf, "0.025 V")
Pf = Ilim**2 * Rf
expect(Pf, "1.25 mW")
Iun = V / Rf
expect(Iun, "10 A")
Pun = V**2 / Rf
expect(Pun, "50 W")
Iexp = q(20, "mA")
expect(Ilim / Iexp, "2.5 1")
check(Rf < Rx, "the fault is below the crossover resistance")
```

</details>

### Reading a scope screen

A 10x probe is connected to a signal, and the channel is set to 10x. The scope is at 2 V/div and 0.5 ms/div. The wave is a square wave that sits 1 division below the center line when low and 3 divisions above it when high. One full cycle spans 4.0 divisions, and the high part lasts 1.0 division.

**Given:** $s_V = 2$ V/div, $s_t = 0.5$ ms/div, low level $-1$ div, high level $+3$ div, $N_T = 4.0$, high time $1.0$ div.

**Find:** The peak-to-peak voltage, the low and high levels, the period, the frequency, the duty cycle, and the average value.

**Assumptions:** The probe is compensated, the channel setting matches the probe, and the trace is not clipped.

**Solution:**

1. Peak-to-peak: $(3 - (-1))\ \text{div} \times 2$ V/div = 8 V. The levels are $-2$ V and $+6$ V.
2. Period: $4.0 \times 0.5$ ms = 2.0 ms, so $f = 1/T = 500$ Hz.
3. High time: $1.0 \times 0.5$ ms = 0.5 ms, so $D = 0.5/2.0 = 0.25$, which is 25 percent.
4. Average: $V_{low} + D\,V_{pp} = -2 + 0.25 \times 8 = 0$ V.

**Answer:** The wave is 8 V peak-to-peak from $-2$ V to $+6$ V, with a 2.0 ms period (500 Hz) and a 25 percent duty cycle. Its average is 0 V.

**Sanity check:** The trace is 4 divisions tall and 4 divisions wide, so the numbers should match: 8 V is 4 divisions at 2 V/div, and a 25 percent duty cycle is a pulse one quarter of the width.

<details><summary>Verification</summary>

```verify
sV = q(2, "V")
st = q(0.5, "ms")
low = q(-1, "1")
high = q(3, "1")
NT = q(4.0, "1")
Nh = q(1.0, "1")
Vpp = (high - low) * sV
expect(Vpp, "8 V")
expect(low * sV, "-2 V")
expect(high * sV, "6 V")
T = NT * st
expect(T, "2.0 ms")
expect(1 / T, "500 Hz")
th = Nh * st
expect(th, "0.5 ms")
D = th / T
expect(D, "0.25")
expect(D * 100, "25 1")
expect(low * sV + D * Vpp, "0 V")
check(Vpp / sV == high - low, "height in divisions matches the volts")
```

</details>

### Bandwidth for a fast edge

A digital signal has a rise time of 5 ns. You have a 100 MHz scope.

**Given:** $t_{sig} = 5$ ns, scope bandwidth 100 MHz, $t_r\,BW = 0.35$.

**Find:** The signal's bandwidth, the scope's rise time, the rise time you will see, and the scope bandwidth the five-times rule asks for.

**Assumptions:** A single-pole scope response, and a probe fast enough not to matter.

**Solution:**

1. Signal bandwidth: $0.35/5\ \text{ns} = 70$ MHz.
2. Scope rise time: $0.35/100\ \text{MHz} = 3.5$ ns.
3. Displayed rise time: $\sqrt{5^2 + 3.5^2} = 6.10$ ns, which is 22 percent too long.
4. The five-times rule asks for $5 \times 70 = 350$ MHz.

**Answer:** The 100 MHz scope shows 6.10 ns for a true 5 ns edge, 22 percent too slow. A scope of about 350 MHz or more is needed to see the edge within a few percent.

**Sanity check:** The scope bandwidth is close to the signal bandwidth, so a large error is expected. A 350 MHz scope has a rise time of 1.0 ns and shows $\sqrt{25+1} = 5.10$ ns, a 2 percent error.

<details><summary>Verification</summary>

```verify
k = q(0.35, "1")
tsig = q(5, "ns")
BW = q(100, "MHz")
BWsig = k / tsig
expect(BWsig, "70 MHz")
tscope = k / BW
expect(tscope, "3.5 ns")
tmeas = sqrt(tsig**2 + tscope**2)
expect(tmeas, "6.10 ns")
expect((tmeas / tsig - 1) * 100, "22 1")
BWneed = q(5, "1") * BWsig
expect(BWneed, "350 MHz")
tfast = k / BWneed
expect(tfast, "1.0 ns")
tmeas2 = sqrt(tsig**2 + tfast**2)
expect(tmeas2, "5.10 ns")
expect((tmeas2 / tsig - 1) * 100, "2 1")
check(tmeas > tsig, "a slow scope makes the edge look slower")
```

</details>

### The doubling surprise

A function generator with a $50\ \Omega$ source resistance shows 2.0 V peak-to-peak and is calibrated for a $50\ \Omega$ load. You connect it to a scope input of $1\ \text{M}\Omega$ and then to a $1\ \text{k}\Omega$ load.

**Given:** display 2.0 V into $50\ \Omega$, $R_s = 50\ \Omega$, loads of $50\ \Omega$, $1\ \text{k}\Omega$, and $1\ \text{M}\Omega$.

**Find:** The open-circuit voltage and the voltage on each load.

**Assumptions:** A purely resistive source and load, and a display that assumes a $50\ \Omega$ load.

**Solution:**

1. The display is the voltage across $50\ \Omega$: $V_{out} = V_{oc}\times 50/100 = V_{oc}/2$. So $V_{oc} = 4.0$ V.
2. Into $50\ \Omega$: 2.0 V.
3. Into $1\ \text{k}\Omega$: $V_{oc} R_L/(R_L + R_s) = 3.81$ V.
4. Into $1\ \text{M}\Omega$: $4.0 \times 10^6/(10^6 + 50) = 4.00$ V.

**Answer:** The scope on a high-impedance input shows about 4.0 V, twice the 2.0 V display. A $1\ \text{k}\Omega$ load sees 3.81 V.

**Sanity check:** A load much larger than $R_s$ gets nearly all of $V_{oc}$, and a load equal to $R_s$ gets half. Every result lies between 2.0 V and 4.0 V.

<details><summary>Verification</summary>

```verify
Rs = q(50, "ohm")
Vdisp = q(2.0, "V")
Voc = Vdisp * (Rs + Rs) / Rs
expect(Voc, "4.0 V")
R1 = q(1000, "ohm")
R2 = q(1000000, "ohm")
expect(Voc * Rs / (Rs + Rs), "2.0 V")
expect(Voc * R1 / (R1 + Rs), "3.81 V")
expect(Voc * R2 / (R2 + Rs), "4.00 V")
check(Voc * R1 / (R1 + Rs) < Voc, "no load sees more than the open-circuit voltage")
```

</details>

## Practice

1. A scope with a 10x probe set correctly shows a sine wave at 5 V/div and 20 $\mu\text{s}$/div. The wave runs from 1.6 divisions below the center to 1.6 divisions above, and one cycle spans 5.0 divisions. Find the peak-to-peak voltage and the frequency.
2. A signal edge has a rise time of 2 ns. Find the signal bandwidth and the scope bandwidth the five-times rule asks for.
3. A function generator with a $50\ \Omega$ source shows 5.0 V peak-to-peak for a $50\ \Omega$ load. Find the voltage across a $100\ \Omega$ load.
4. A supply is set to 12.0 V with a current limit of 0.200 A. Find the crossover resistance, then the output voltage when it drives $30\ \Omega$.
5. You must look at a waveform on the primary side of a mains-powered power supply with a bench scope that has a grounded probe clip. State what you must not do, and what you may do.

<details><summary>Answers</summary>

1. 16 V peak-to-peak, 10 kHz (period 100 $\mu\text{s}$)
2. 175 MHz signal bandwidth, 875 MHz scope
3. 6.67 V
4. $60\ \Omega$; 6.00 V, in constant-current mode, since 30 is below 60
5. Do not clip the ground to the mains-referenced circuit, and do not remove the scope's earth. Use an isolation transformer, a differential probe, or a battery-powered scope, and only if trained for mains work.

```verify
sV5 = q(5, "V")
N = q(1.6, "1")
Vpp = 2 * N * sV5
expect(Vpp, "16 V", ans=1)
T = q(5.0, "1") * q(20, "us")
expect(T, "100 us", ans=1)
expect(1 / T, "10 kHz", ans=1)
k = q(0.35, "1")
BWs = k / q(2, "ns")
expect(BWs, "175 MHz", ans=2)
expect(q(5, "1") * BWs, "875 MHz", ans=2)
Voc = q(5.0, "V") * 2
expect(Voc * q(100, "ohm") / (q(100, "ohm") + q(50, "ohm")), "6.67 V", ans=3)
Rx = q(12.0, "V") / q(0.200, "A")
expect(Rx, "60 ohm", ans=4)
expect(q(0.200, "A") * q(30, "ohm"), "6.00 V", ans=4)
skip(ans=5, why="a judgment answer in words")
```

</details>

## Common mistakes

- Setting the current limit after connecting the circuit, or leaving it at the maximum. The limit is the only thing between a fault and a fire.
- Leaving the probe setting at 1x with a 10x probe, so every voltage reads wrong by a factor of 10.
- Skipping probe compensation, so square-wave corners are rounded or spiked and rise-time and amplitude readings are false.
- Using a scope with too little bandwidth and then trusting the rise time it shows. The edge looks slower than it is.
- Clipping the probe ground to a mains-referenced node, or lifting the scope's earth to avoid the problem.
- Reading the generator display as the voltage into a high-impedance load, when it is the voltage into $50\ \Omega$.
- Judging a joint by whether it holds, instead of by how it looks. A dull, grainy joint is a cold joint, and a part that holds in the hand can still fail the first time the board flexes.
- Trusting a breadboard for fast or high-current circuits. Its contacts, stray capacitance, and long wires change what the circuit does.

## Go deeper

- [Circuits and Electronics (6.002)](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/) by MIT OpenCourseWare: a free course on the circuit analysis behind every measurement here.
- [Overview of lead](https://www.osha.gov/lead) by the Occupational Safety and Health Administration: the hazards of lead and the rules for workers exposed to it.
- Related: [Circuit basics](../applications/electronics/01-circuit-basics.md), [RC circuits and op-amps](../applications/electronics/02-rc-circuits-and-op-amps.md), [Printed circuit boards](../applications/electronics/04-printed-circuit-boards.md), [Data acquisition and sampling](../measurement/08-data-acquisition-and-sampling.md), [Measurement tools](07-measurement-tools.md), [Shop tools](08-shop-tools.md).
