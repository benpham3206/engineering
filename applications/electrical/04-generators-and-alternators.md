# Generators and alternators

**Type:** lesson

A generator is a machine that converts rotating mechanical power into electrical power by moving conductors through a magnetic field. An engineer should understand it because almost all grid electricity and the charging current in every car come from such machines, and sizing one means matching speed, voltage, and losses.

**Prerequisites:** [Electricity and magnetism](../../physics/06-electricity-and-magnetism.md), [Thermodynamics: properties, work, heat, and the first law](../../physics/08-thermo-first-law.md), [Trigonometry](../../math/02-trigonometry.md), [Single-variable calculus](../../math/03-single-variable-calculus.md)
**Time:** 4-6 h

## Core ideas

### How it works

Faraday's law sets the basic rule. An EMF appears in a conductor when the magnetic flux through a loop changes. For a coil of $N$ turns:

$$\varepsilon = -N \frac{d\Phi}{dt}$$

The minus sign is Lenz's law. The induced EMF drives a current that opposes the change that caused it.

Picture a single coil of $N$ turns, area $A$, in a uniform field $B$. Turn the coil at angular speed $\omega$. The flux through it is $\Phi = BA\cos\omega t$, so the EMF is a sine wave with peak value $NBA\omega$. The rotation is the only thing that changes the flux, so the rotor must keep turning to keep the voltage.

Energy follows the same path in reverse. A current in the coil produces a force that opposes the rotation. The prime mover, such as an engine, turbine, or water wheel, must supply the torque to overcome that force. The shaft torque times the shaft speed is the power that becomes electricity, minus losses.

In a large synchronous generator, a DC field on the rotor produces a magnetic field that spins with the shaft. The stator winding sees that spinning field. Stator and rotor run at a fixed ratio, so the output frequency is fixed by the shaft speed and the number of poles.

### Main parts

The rotor carries the magnetic field. It is either a field coil fed with DC through slip rings, or a set of permanent magnets. The rotor is the part that spins.

The stator, also called the armature, is a fixed iron core with insulated copper windings. The EMF appears in these windings, so their voltage and current are the machine's output.

The field supply provides DC to the rotor winding. In a large generator, a small exciter machine often supplies this current. In a car, the voltage regulator sets the field current from the battery voltage.

The bearings hold the rotor. The stator core is laminated silicon steel, which keeps eddy currents small.

A car alternator adds a diode bridge that turns the three-phase AC from the stator into DC for the battery. A regulator inside the unit adjusts the field current to hold the output near 14 V (typical).

Large machines use fans, water, or hydrogen to carry away heat from the windings and core. Hydrogen cooling is common in large turbogenerators (typical).

### Variants

A synchronous generator runs at a speed tied to the output frequency. A two-pole machine at 3600 rpm gives 60 Hz, and a four-pole machine at 1800 rpm gives 60 Hz. Power stations, diesel generator sets, and hydroelectric plants use this type. Hydroelectric turbines turn slowly, so their generators have many poles.

An alternator is a synchronous generator with a rectifier at its output. Cars, boats, and trucks use alternators because they charge a battery with DC from a machine that runs at varying speed.

A permanent-magnet generator has no field winding and no slip rings. It is common in small wind turbines and in some direct-drive wind turbines (typical).

An induction generator runs slightly faster than synchronous speed and is used in some wind installations. The [induction motors lesson](03-induction-motors.md) covers that machine in detail.

## Key equations

Faraday's law: $\varepsilon = -N\,d\Phi/dt$, where $\varepsilon$ is the EMF in volts, $N$ is the number of turns (dimensionless), $\Phi$ is the magnetic flux in webers (Wb), and $t$ is time in seconds.

Sinusoidal EMF from a rotating coil:

$$e(t) = N B A \omega \sin(\omega t)$$

Here $B$ is the flux density in teslas (T), $A$ is the coil area in square metres (m$^2$), and $\omega$ is the angular speed in radians per second (rad/s).

Peak and root-mean-square (rms) values:

$$E_{\mathrm{max}} = N B A \omega, \qquad E_{\mathrm{rms}} = \frac{E_{\mathrm{max}}}{\sqrt{2}}$$

Synchronous speed and frequency:

$$f = \frac{p\, n}{120}$$

Here $f$ is the output frequency in hertz (Hz), $p$ is the number of poles (an even integer, dimensionless), and $n$ is the rotor speed in revolutions per minute (rpm).

Winding EMF per phase, for a sinusoidal flux:

$$E = 4.44\, f\, N\, \Phi$$

Here $E$ is the rms EMF per phase in volts, $N$ is the number of turns per phase, and $\Phi$ is the peak flux per pole in webers. The constant 4.44 is $2\pi/\sqrt{2}$, rounded.

Electrical output power, DC form and three-phase form:

$$P_{\mathrm{out}} = V I \qquad P_{\mathrm{out}} = \sqrt{3}\, V_L I_L \cos\phi$$

Here $V$ and $I$ are volts and amps, $V_L$ and $I_L$ are the line voltage and line current, and $\cos\phi$ is the power factor (dimensionless).

Efficiency and shaft torque:

$$\eta = \frac{P_{\mathrm{out}}}{P_{\mathrm{in}}} \qquad T = \frac{P_{\mathrm{in}}}{\omega}$$

Here $\eta$ is efficiency (dimensionless), $P_{\mathrm{in}}$ is the shaft input power in watts, $T$ is torque in newton metres (N m), and $\omega = 2\pi n / 60$ is the shaft speed in rad/s.

## Worked example

**Given:** A car alternator is driven by a belt at a pulley ratio of 2.5, so the alternator turns 2.5 times faster than the engine. The engine runs at 2000 rpm. The rotor has 12 poles. At this operating point the alternator delivers 14.0 V at 70 A, with an efficiency of 0.60. The belt drive is assumed to be 100 percent efficient.

**Find:** (a) the alternator speed in rpm, (b) the output frequency in hertz, (c) the electrical output power, (d) the shaft input power, and (e) the torque the alternator draws from the engine at 2000 rpm.

**Assumptions:** The voltage and current are steady. The efficiency lumps together the copper, iron, friction, field, and rectifier losses.

**Solution:**

1. Alternator speed: $n_{\mathrm{alt}} = 2.5 \times 2000 = 5000\ \text{rpm}$.
2. Output frequency: $f = p\,n/120 = 12 \times 5000 / 120 = 500\ \text{Hz}$.
3. Electrical output: $P_{\mathrm{out}} = V I = 14.0 \times 70 = 980\ \text{W}$.
4. Shaft input: $P_{\mathrm{in}} = P_{\mathrm{out}}/\eta = 980 / 0.60 = 1633\ \text{W}$. This is about 1.63 kW, or about 2.2 hp.
5. Engine speed in rad/s: $\omega = 2\pi \times 2000 / 60 = 209.4\ \text{rad/s}$. Torque: $T = 1633 / 209.4 = 7.80\ \text{N m}$.

**Answer:** (a) 5000 rpm. (b) 500 Hz. (c) 980 W. (d) 1.63 kW. (e) 7.80 N m.

**Sanity check:** The shaft input must exceed the electrical output, and it does: 1633 W is greater than 980 W. An efficiency of 0.60 is in the range typical of car alternators at moderate load (typical). The 500 Hz frequency is high for a machine that makes grid power, but it follows directly from 12 poles at 5000 rpm.

## Design trade-offs

Speed and pole count set the frequency. For a synchronous generator, more poles let the machine run slower at the same frequency. A slower rotor has lower centrifugal stress and less noise, but the rotor is bigger. Hydroelectric generators use many poles because water turns the shaft slowly.

Efficiency matters because losses become heat. Large turbogenerators reach 98 to 99 percent efficiency at rated load (typical). Car alternators run lower, roughly 50 to 65 percent at typical operating points (typical). The losses are copper loss, which scales with the square of current, plus core loss, friction, windage, field loss, and rectifier voltage drop.

Power per kilogram rises with speed for the same torque. This is why a car alternator spins several times faster than the engine. The cost is higher bearing speed, more heat, and a need for a belt drive that stays tight.

Voltage regulation matters for charging. Output voltage depends on speed and field current, and the load changes both. The regulator adjusts field current to hold the battery charging voltage steady, usually near 14 V for a 12 V system (typical).

Noise has several sources. Magnetic hum appears at twice the electrical frequency. A car alternator's whine rises with engine speed because its frequency rises with speed.

Brush and slip-ring wear limits life in wound-rotor machines, because the field current passes through them. Bearings often set the service life before the windings do.

## How it fails

A failed rectifier diode in a car alternator produces ripple, whine, and lower output. A shorted diode can drain the battery through the stator. Warning signs are a dim battery light, dimming lights at idle, and a whine that rises with engine speed.

A failed voltage regulator either overcharges or undercharges the battery. Overcharging boils electrolyte in a flooded battery and can swell the case. Undercharging leaves the battery flat. Warning signs are a battery voltage well above 15 V or below about 13 V with the engine running (typical limits).

Brush and slip-ring wear causes sparking, carbon dust, and eventually loss of field. The field is the rotor's magnetic source, so losing it means losing output.

Bearing failure causes rumbling, heat, and seizure. A seized bearing can snap the drive belt, which stops the alternator and can overheat the engine's cooling fan.

Connecting a synchronous generator to a live grid at the wrong phase, voltage, or frequency causes a large current surge and a torque shock on the shaft. Synchronizing check relays and breakers exist to prevent this.

Loss of field in a synchronous generator makes it draw reactive power from the grid and overheat the stator. A loss-of-field relay trips the machine for this reason.

Overspeed happens when a turbine-driven generator loses its load. A governor and an overspeed trip protect the rotor from the stress that can burst it.

Overheating from overload or blocked airflow ages the insulation. Temperature sensors in the windings raise alarms and trip the machine before insulation fails.

## History

Michael Faraday demonstrated electromagnetic induction in 1831 in England. Hippolyte Pixii built a hand-cranked magneto-electric generator in France in 1832. Zénobe Gramme's ring dynamo, a practical DC generator, appeared about 1871. Alternating-current machines were built in quantity during the 1880s and powered the first large AC systems in the late 1880s and 1890s. Automotive alternators with silicon diode rectifiers replaced the older DC dynamos on cars during the 1960s.

## Practice

1. A four-pole generator runs at 1800 rpm. Find its output frequency in hertz.
2. A coil with 300 turns and an area of 0.010 m$^2$ turns at 50 rad/s in a uniform field of 0.50 T. Find the peak EMF and the rms EMF.
3. A 12-pole generator must produce 50 Hz. Find the speed in rpm.
4. A three-phase synchronous generator at 50 Hz has 400 turns per phase and a peak flux per pole of 0.030 Wb. Use $E = 4.44\,f\,N\,\Phi$ to find the rms EMF per phase.
5. An alternator delivers 13.8 V at 90 A with an efficiency of 0.55. Find its shaft input power in watts.

<details><summary>Answers</summary>

1. 60 Hz, from $f = 4 \times 1800 / 120$.
2. Peak EMF 75 V, rms EMF 53.0 V.
3. 500 rpm, from $n = 120 f / p = 120 \times 50 / 12$.
4. 2664 V rms per phase, about 2.66 kV.
5. 2258 W, from $P_{\mathrm{out}} = 13.8 \times 90 = 1242\ \text{W}$ and $P_{\mathrm{in}} = 1242 / 0.55$.

</details>

## Common mistakes

- Dividing by the number of pole pairs when the formula needs the number of poles. Use $f = pn/120$ with $p$ the total poles.
- Treating peak and rms EMF as the same value. The rms value is the peak value divided by $\sqrt{2}$ for a sine wave.
- Forgetting that efficiency applies to the shaft side. Input power equals output power divided by efficiency, not multiplied by it.
- Assuming output voltage stays fixed as load changes. The EMF depends on speed and field current, so a regulator or an operator must control it.
- Assuming a generator makes power without shaft torque. Every watt of electrical output needs torque from the prime mover, plus the losses.

## Go deeper

- [University Physics Volume 2, Chapter 13: Electromagnetic Induction](https://openstax.org/books/university-physics-volume-2/pages/13-introduction), OpenStax. Free text covering Faraday's law, Lenz's law, and electric generators.
- [University Physics Volume 2, Chapter 15: AC Circuits](https://openstax.org/books/university-physics-volume-2/pages/15-introduction), OpenStax. Free text covering alternating current, phase, and transformers.
- Related lessons: [DC motors](01-dc-motors.md), [induction motors](03-induction-motors.md), [transformers](05-transformers.md), [the power grid](08-the-power-grid.md).
- [Applications reference](../reference.md): the lookup sheet for this topic.
