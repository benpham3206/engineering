# applications reference

**Type:** reference

A lookup sheet for building and checking electrical, mechatronic, robotic, thermal, and fluid systems, for an engineer who needs a formula, a value, a limit, or a checklist in the middle of a build or a review.

## Principles

- Conservation holds in every system: charge (KCL), energy (KVL, and Bernoulli with losses), and mass (continuity). If your numbers create any of them, recheck the work.
- Every model has a regime. Ohm's law assumes linear parts, the ideal op-amp rules assume negative feedback, and Bernoulli assumes no friction and no added energy. Check the regime before you trust the formula.
- Power that is not delivered to the load ends up as heat. Size parts and heat paths for dissipation, not only for voltage and current.
- A rating is a limit, not a target. Design against the worst case of supply, temperature, and tolerance.
- Unit errors are the most common source of wrong answers. Convert to SI (ohm, A, V, m, s, W, Pa, N m) before you compute.
- A prediction counts only after a measurement checks it. Write the predicted number down before the test.
- Change one variable per test, so each result has one cause.
- Gravity, air density, and temperature are not fixed. Use the general form with the local value (for example $W = m g$ with $g$ for the local body), and state Earth values as one case.
- Datasheet min, typ, and max values govern a design. Textbook values are typical and are for orientation only.

## Resistors and preferred values

Four-band code, digits and multiplier in ohms, then tolerance.

| Color | Digit | Multiplier | Tolerance |
|---|---|---|---|
| Black | 0 | $10^0$ | none |
| Brown | 1 | $10^1$ | 1 percent |
| Red | 2 | $10^2$ | 2 percent |
| Orange | 3 | $10^3$ | none |
| Yellow | 4 | $10^4$ | none |
| Green | 5 | $10^5$ | 0.5 percent |
| Blue | 6 | $10^6$ | 0.25 percent |
| Violet | 7 | $10^7$ | 0.1 percent |
| Gray | 8 | $10^8$ | none |
| White | 9 | $10^9$ | none |
| Gold | none | $10^{-1}$ | 5 percent |
| Silver | none | $10^{-2}$ | 10 percent |

- Four band: value = (digit 1 digit 2) times multiplier. Five band: (digits 1 to 3) times multiplier, then tolerance.
- Example: yellow, violet, red, gold = $47 \times 10^2\ \Omega = 4.7\ \text{k}\Omega$, 5 percent.
- Preferred values (IEC 60063). Pick the nearest value on the safe side of the design, then recompute the result with the chosen value.

| Series | Values in one decade | Step ratio | Typical tolerance |
|---|---|---|---|
| E12 | 1.0, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2 | about 1.21 | 10 percent |
| E24 | 1.0, 1.1, 1.2, 1.3, 1.5, 1.6, 1.8, 2.0, 2.2, 2.4, 2.7, 3.0, 3.3, 3.6, 3.9, 4.3, 4.7, 5.1, 5.6, 6.2, 6.8, 7.5, 8.2, 9.1 | about 1.10 | 5 percent |
| E96 | 96 values per decade | about 1.024 | 1 percent |

- Power: $P = I^2 R = V^2 / R$. Standard power ratings are 1/8, 1/4, 1/2, and 1 W.
- Rule of thumb: keep a resistor below about half its rated power at the worst-case ambient. Basis: temperature rise drives drift and failure. Limit: depends on ambient, airflow, and board layout; apply the derating curve in the datasheet.
- Holds when: the value is near nominal and the part is at room temperature. Breaks when: precision work needs low-tolerance or low-temperature-coefficient parts, or when voltage across the part exceeds its voltage rating.

## Series, parallel, and dividers

Series and parallel (linear, ideal wires):

- Series: $R_{eq} = R_1 + R_2 + \cdots$. Same current in each part.
- Parallel: $\dfrac{1}{R_{eq}} = \dfrac{1}{R_1} + \dfrac{1}{R_2} + \cdots$. Same voltage across each part.
- Two in parallel: $R_{eq} = \dfrac{R_1 R_2}{R_1 + R_2}$. N equal in parallel: $R/N$.
- Capacitors: series $\dfrac{1}{C_{eq}} = \sum \dfrac{1}{C_i}$, parallel $C_{eq} = \sum C_i$.
- Inductors: series $L_{eq} = \sum L_i$, parallel $\dfrac{1}{L_{eq}} = \sum \dfrac{1}{L_i}$. Valid only without mutual coupling.

Voltage divider:

- Unloaded: $V_2 = V_s \dfrac{R_2}{R_1 + R_2}$.
- Loaded by $R_L$: $V_{out} = V_s \dfrac{R_2 \| R_L}{R_1 + R_2 \| R_L}$, where $\|$ means parallel.
- Thevenin equivalent seen at the tap: $V_{th} = V_s \dfrac{R_2}{R_1 + R_2}$, $R_{th} = \dfrac{R_1 R_2}{R_1 + R_2}$.
- Rule of thumb: make $R_L$ at least 10 times $R_{th}$ so the load error is about 10 percent or less. Limit: this error is still too large for precision; add a buffer (voltage follower).
- Worked check: 9 V across 10 k and 10 k, loaded by 10 k. $R_2 \| R_L = 5$ k, so $V_{out} = 9 \times 5 / (10 + 5) = 3.0$ V, against 4.5 V unloaded.

Current divider (two branches, total current $I$):

- Current in branch 1: $I_1 = I \dfrac{R_2}{R_1 + R_2}$. Current splits in the opposite ratio to resistance.
- Check: 10 mA into 1 k and 4.7 k in parallel gives 8.25 mA in the 1 k branch and 1.75 mA in the 4.7 k branch.

Holds when: linear parts and a stiff source. Breaks when: the load is not much larger than the divider resistance, the source has its own resistance, or parasitic capacitance matters at high frequency.

## Op-amp configurations

Ideal rules (valid only with negative feedback and the output inside its rails):

- The two inputs are at the same voltage: $V_+ = V_-$.
- The inputs draw no current.

| Configuration | Circuit | Gain or output | Notes |
|---|---|---|---|
| Inverting | $V_{in}$ into $V_-$ through $R_{in}$; $R_f$ from output to $V_-$; $V_+$ at ground | $A_v = -R_f / R_{in}$ | Input resistance equals $R_{in}$. Sign flips. |
| Non-inverting | $V_{in}$ into $V_+$; $R_g$ from $V_-$ to ground; $R_f$ from output to $V_-$ | $A_v = 1 + R_f / R_g$ | Very high input resistance. Gain is at least 1. |
| Voltage follower | Output tied straight to $V_-$ | $A_v = 1$ | Buffer; isolates a high-impedance source. |
| Summing (inverting) | Several inputs $V_i$ through $R_i$ into $V_-$; $R_f$ to output | $V_{out} = -R_f \sum V_i / R_i$ | Equal $R_i$ gives $-(R_f/R)\sum V_i$. |
| Integrator | $R_{in}$ into $V_-$; $C$ in feedback | $V_{out}(t) = -\dfrac{1}{R_{in} C} \int V_{in}\,dt + V_{out}(0)$ | Output drifts from offset and bias. Needs a reset or a leak resistor. |
| Differentiator | $C$ into $V_-$; $R_f$ in feedback | $V_{out} = -R_f C \dfrac{dV_{in}}{dt}$ | Amplifies noise at high frequency. Add a small series resistor. |
| Comparator | No feedback; compare $V_+$ with $V_-$ | Output high if $V_+ > V_-$, else low | Use a comparator part if the output must switch fast. Add positive feedback for hysteresis. |

Worked checks:

- Inverting, $R_{in} = 4.7$ k, $R_f = 47$ k: $A_v = -10$. Non-inverting with the same values: $A_v = 11$.
- Summing, $R_1 = 10$ k, $R_2 = 20$ k, $R_f = 10$ k, $V_1 = 1$ V, $V_2 = 0.5$ V: $V_{out} = -10\text{k}(1/10\text{k} \cdot 1 + 1/20\text{k} \cdot 0.5) = -1.25$ V.
- Integrator, $R = 10$ k, $C = 1\ \mu$F, constant $V_{in} = 1$ V: output ramps at $-100$ V/s.
- Differentiator, $R_f = 10$ k, $C = 1\ \mu$F, $dV_{in}/dt = 1$ V/ms: $V_{out} = -10$ V.

Bandwidth and limits:

- Closed-loop bandwidth is about $f_{GBW} / |A_v|$. Check: GBW of 1 MHz at gain 100 gives about 10 kHz.
- Output cannot exceed the supply. Many general-purpose parts stay about 1 V or more inside the rails; rail-to-rail parts get closer. Check the output swing in the datasheet.
- Typical general-purpose op-amp: GBW around 1 MHz, input offset in the millivolt range. Precision parts reach microvolt offsets. Use datasheet values.
- Slew rate caps how fast the output changes. Large, fast signals can distort even when the small-signal bandwidth looks fine.

Holds when: negative feedback is present, the output is inside its swing, and the signal is well below GBW over gain. Breaks when: there is no feedback (output saturates), the signal is near the rails or the input common-mode range, the load is too heavy for the output stage, or the signal is faster than the slew rate allows.

## RC filters and time response

- Time constant: $\tau = RC$ (s), with R in ohms and C in farads.
- Cutoff frequency: $f_c = \dfrac{1}{2\pi R C}$ (Hz).
- First-order low-pass: $|H| = \dfrac{1}{\sqrt{1 + (f/f_c)^2}}$, phase $= -\arctan(f/f_c)$.
- First-order high-pass: $|H| = \dfrac{f/f_c}{\sqrt{1 + (f/f_c)^2}}$, phase $= \arctan(f_c/f)$.
- Roll-off above cutoff: about $-20$ dB per decade (first order).
- Step response (low-pass): $V(t) = V_s (1 - e^{-t/\tau})$. At $\tau$: 63 percent. At $4.6\tau$: 99 percent. At $5\tau$: 99.3 percent.
- Worked check: $R = 1$ k, $C = 100$ nF gives $f_c = 1592$ Hz. At $f_c/10$: $-0.04$ dB, $-5.7$ deg. At $f_c$: $-3.01$ dB, $-45$ deg. At $10 f_c$: $-20.0$ dB, $-84$ deg.

Holds when: the source impedance is small against $R$, the next stage draws little current, and the parts are linear. Breaks when: the next stage loads the filter (add a buffer), the source impedance adds to $R$, capacitor tolerance and dielectric change with voltage and temperature, or the signal is so fast that parasitics and the op-amp limit the response.

## Diodes and LEDs

- Series resistor for an LED or a forward-biased diode: $R = \dfrac{V_s - V_f}{I}$. Resistor power $P_R = I^2 R$.
- Typical forward voltage at indicator current (typical, check the datasheet for your part and current):

| Device | Typical $V_f$ |
|---|---|
| Silicon signal or rectifier diode | 0.6 to 0.7 V |
| Red LED | 1.8 to 2.0 V |
| Yellow or green LED | 2.0 to 2.2 V |
| Blue or white LED | 3.0 to 3.4 V |

- Typical indicator LED current: 5 to 20 mA. Check the datasheet for the rated value.
- Worked check: 5 V supply, red LED with $V_f = 2.0$ V, 20 mA target. $R = (5 - 2)/0.020 = 150\ \Omega$ (E12 value, exact). $P_R = 0.02^2 \times 150 = 60$ mW, so a 1/4 W resistor.
- Sensitivity: the same 150 Ω gives 16.7 mA at 4.5 V and 23.3 mA at 5.5 V. A constant-current driver is the fix when the supply varies.
- Forward voltage of a silicon diode falls about 2 mV per kelvin of temperature rise (typical). LED brightness also depends on temperature.
- Inductive loads (relay coils, solenoids, motor windings): place a flyback diode across the coil, reverse-rated at or above the supply voltage and with a current rating at or above the load current. The stored energy $E = \tfrac{1}{2} L I^2$ must go somewhere; without the diode it appears as a voltage spike across the switch.

Holds when: the supply is stiff and the diode is at a steady operating point. Breaks when: the supply varies (use a current source), the part heats up, or the reverse voltage exceeds the rating.

## Transistors as switches

BJT (NPN, low-side switch, emitter to ground):

- Off: base-emitter voltage well below the turn-on value, base current zero, collector current near zero.
- On (saturated): base current must be at least $I_c / h_{FE,min}$ at the worst case. Rule of thumb: design for $I_b \approx I_c / 10$. Basis: $h_{FE}$ falls with collector current and temperature. Limit: check $h_{FE}$ at your actual $I_c$ in the datasheet.
- Base resistor: $R_b = \dfrac{V_{in,high} - V_{be}}{I_b}$, with $V_{be} \approx 0.7$ V (typical when on).
- Worked check: $I_c = 100$ mA, $I_b = 10$ mA, $V_{in,high} = 3.3$ V gives $R_b = 2.6\ \text{V} / 10\ \text{mA} = 260\ \Omega$. Use 220 Ω (next lower E12 value) for more base drive. Confirm the microcontroller can source that current at the output high level.
- Saturation voltage $V_{ce,sat}$ is typically 0.1 to 0.3 V. Loss $P = V_{ce,sat} I_c$.
- Add a pulldown (10 k is a common value, typical) from base to emitter so the transistor stays off while the input floats.

MOSFET (N-channel, low-side switch):

- The gate is voltage controlled. DC gate current is near zero, but the gate is capacitive: charging $Q_g$ each switching cycle draws average current $I_g \approx Q_g f_{sw}$.
- Use a logic-level MOSFET if the gate drive is 3.3 V or 5 V. Check $R_{ds(on)}$ at your actual $V_{gs}$ in the datasheet. A part specified only at 10 V may not fully turn on at 3.3 V.
- On-state loss: $P = I^2 R_{ds(on)}$. Example: 5 A through 20 mΩ gives 0.5 W.
- A series gate resistor (10 to 100 Ω, typical) damps ringing. A gate pulldown (10 k, typical) holds the device off during reset or boot.
- Voltage rating: a common rule is to keep the drain voltage rating at 1.5 to 2 times the supply for transient margin. Limit: depends on the expected transients; check the application.

Holds when: the drive voltage and current exceed the thresholds with margin at worst-case temperature. Breaks when: the input drive is too weak (the device stays in its linear region and overheats), the load is inductive without a flyback path, or the device is switched faster than the drive can support.

## Microcontroller interfacing

- Logic levels: for every connection, compare the driver's $V_{OH}$ and $V_{OL}$ with the receiver's $V_{IH}$ and $V_{IL}$. The link works when $V_{OH} \ge V_{IH}$ and $V_{OL} \le V_{IL}$ at the actual currents.
- A 3.3 V output into a 5 V CMOS input can fail if $V_{IH}$ is about 0.7 times 5 V (3.5 V). Check the datasheet, and use a level shifter when it does not meet $V_{IH}$.
- A 5 V output into a 3.3 V input may damage a pin that is not 5 V tolerant. Check the "5 V tolerant" entry and use a divider or level shifter if needed.
- Pull-ups for open-drain or open-collector lines: low-state current $I = V_{cc} / R$; rise time about $2.2\,R C_{bus}$ (10 to 90 percent for an RC rise). Worked check: 4.7 k at 3.3 V gives 0.70 mA when low, and $\tau = 4.7\text{k} \times 50\ \text{pF} = 235$ ns for a 50 pF bus. Pick R from the bus protocol's rise-time and current limits.
- Floating inputs: tie unused inputs to a rail or to ground through a resistor. Floating CMOS inputs draw extra current and pick up noise.
- Pin current: check the absolute maximum per pin and per port in the datasheet. Typical per-pin limits are in the 10 to 25 mA range (check your part). Drive LEDs within that limit and use a transistor for anything larger.
- Never drive motors from GPIO. A pin supplies a few to tens of milliamps, and a motor at stall can draw many amps. Use a transistor, MOSFET, or motor driver, and connect the motor's flyback path.
- Ground and decoupling: share one ground reference for signals. Put a ceramic capacitor (100 nF, typical) at each IC supply pin, and bulk capacitance (10 to 100 µF, typical) at the regulator or motor supply.
- Analog inputs: the ADC needs a low source impedance during sampling. Check the maximum source resistance in the datasheet, and buffer high-impedance sensors with a follower.
- ADC: LSB size $V_{LSB} = V_{ref} / 2^n$. Effective resolution is usually below $n$ bits because of noise. Measure the noise floor before you claim a resolution.
- PWM: average voltage $V_{avg} = D V_{supply}$ holds only for a load that averages the pulses, such as a motor winding. Choose a PWM frequency high enough that the load's current ripple is small; for many motors 10 to 20 kHz is common (typical).

Holds when: the datasheet values are used at the actual currents and temperatures. Breaks when: a pin is used beyond its current or voltage limits, a long wire adds noise or ground bounce, or the load is inductive without protection.

## DC motors

Symbols: $V$ supply volts (V), $R$ armature resistance ($\Omega$), $I$ current (A), $\omega$ speed (rad/s), $T$ torque (N m), $K_t$ torque constant (N m/A), $K_e$ back-EMF constant (V s/rad).

- Voltage balance: $V = I R + K_e \omega$.
- Torque: $T = K_t I$.
- Speed at a torque: $\omega = \dfrac{V - R T / K_t}{K_e}$.
- No-load speed (friction ignored): $\omega_0 = V / K_e$. In rpm: $n_0 = 60 \omega_0 / (2\pi)$, which is $9.549\,\omega_0$.
- Stall: $\omega = 0$. Stall current $I_s = V/R$, stall torque $T_s = K_t V / R$.
- Speed-torque line (ideal permanent-magnet DC): $\omega = \omega_0 (1 - T / T_s)$.
- Mechanical power: $P_{mech} = T \omega$. Maximum at $T = T_s/2$ and $\omega = \omega_0/2$, with $P_{max} = T_s \omega_0 / 4$.
- Electrical input $P_{elec} = V I$. Efficiency $\eta = T\omega / (V I)$. Copper loss $I^2 R$.
- Worked check: $V = 12$ V, $R = 1.5\ \Omega$, $K_t = K_e = 0.02$ SI. $\omega_0 = 600$ rad/s (5730 rpm), $I_s = 8$ A, $T_s = 0.16$ N m, $P_{max} = 24$ W at $T = 0.08$ N m, $\omega = 300$ rad/s, where $I = 4$ A.
- Unit conversion: if $K_e$ is given in V per rpm, multiply by 9.549 to get V s/rad. If $K_t$ is given in oz in/A, multiply by 0.00706 for N m/A. In SI, $K_t$ and $K_e$ have the same numerical value for an ideal motor.
- Time constants: electrical $\tau_e = L/R$; mechanical $\tau_m = J R / (K_t K_e)$, with $J$ the rotor inertia in kg m$^2$.

Holds when: the motor is brushed or brushless DC with a steady supply, at steady speed, away from the stall region. Breaks when: transients matter (use $\tau_e$ and $\tau_m$), friction and cogging are large at low speed, brush drop matters at low voltage, the winding overheats, or PWM ripple changes the average.

## Gearboxes and reflected inertia

- Ratio $N = \omega_{in} / \omega_{out}$. A ratio above 1 reduces speed and multiplies torque.
- Output torque: $T_{out} = N T_{in} \eta$. Output speed: $\omega_{out} = \omega_{in} / N$.
- Stage efficiency (typical): spur and helical gears 0.90 to 0.98 per stage. Worm gears are lower and may not back-drive. Check the maker's data.
- Reflected inertia at the motor shaft: $J_{load} / N^2$. Total motor-side inertia is $J_m + J_{load} / N^2$.
- Worked check: a 10:1 gearbox at 90 percent efficiency turns 0.05 N m input into 0.45 N m output at 60 rad/s (573 rpm) from 600 rad/s input.
- Backlash adds position error, which is worst at reversals. A sensor on the motor side cannot see it.

Selection procedure:

1. Find the required output torque and speed, including friction and gravity.
2. Choose $N$ so that $\omega_{in} = N \omega_{out,req}$ stays below the motor's no-load speed with margin.
3. Compute motor torque $T_{in} = T_{out,req} / (N \eta)$ and confirm it is inside the continuous and peak torque ratings.
4. Recompute with the reflected inertia and check acceleration time.

Holds when: the gear train is rigid and efficiency is roughly constant over the load range. Breaks when: efficiency falls at light load, the gearbox is worn or loose, or backlash matters for positioning.

## Motor sizing

1. Define the duty cycle: torque and speed for each phase (acceleration, steady run, deceleration, idle).
2. Compute the output-side torque for each phase: friction $T_f$, gravity $T_g = m g r$ for a lifted load (use $g$ for the local body; Earth: 9.81 m/s$^2$), and inertial $T_a = J_{total}\,\alpha$.
3. Reflect the output torque to the motor: $T_{motor} = T_{out} / (N \eta)$, and reflect inertia as above.
4. Compute the RMS torque over the cycle: $T_{rms} = \sqrt{\sum T_i^2 t_i / \sum t_i}$. Basis: winding heating goes as current squared. Limit: valid when $K_t$ is constant and speed-dependent losses are small.
5. Compare $T_{rms}$ with the continuous torque rating, the peak torque with the peak rating, and the operating speed with no-load speed at the available voltage.
6. Check the voltage budget at the peak point: $V \ge K_e \omega + I R$.
7. Check winding temperature with the datasheet thermal resistance and the worst ambient.
8. Apply a torque safety factor (1.5 to 2 is common practice). Increase it when the load or friction is uncertain.

Worked check: a 2 kg mass lifted by a 0.10 m radius drum needs $T = 2 \times 9.81 \times 0.10 = 1.96$ N m at the drum. Through a 20:1 gearbox at 85 percent, the motor needs $1.96 / (20 \times 0.85) = 0.115$ N m, before inertia and friction are added.

Holds when: the duty profile is known and the motor data is at the operating temperature. Breaks when: loads are unknown, the duty is continuous at high torque with poor cooling, or the motor is oversized so it runs at very low efficiency.

## Stepper motors and servos

Stepper:

- Step angle: $360° / (\text{full steps per revolution})$. Typical hybrid stepper: 200 full steps, so 1.8 deg per step.
- Microstepping by factor $M$: steps per revolution $= 200 M$. At $M = 16$, that is 3200 per revolution, and speed $n = 60 \times \text{step rate} / (\text{steps per revolution})$. Check: 1000 steps/s at 3200 per revolution is 18.75 rpm.
- Holding torque at standstill is the highest. Torque falls as speed rises, because inductance and back-EMF limit the phase current.
- The driver must regulate phase current (chopping). Applying voltage alone sets the wrong current.
- Resonance can occur at certain low step rates. Damp it or step past the band.
- Open loop: missed steps are not detected. Keep a torque margin (30 to 50 percent is a common rule) and check the pull-in and pull-out curves in the datasheet.

Servo:

- Hobby (RC) servo: control pulse width 1.0 to 2.0 ms in a 20 ms frame (50 Hz). Neutral at about 1.5 ms. Duty cycle 5 to 10 percent (typical).
- Position is set by pulse width; the servo has no speed or torque feedback in the simple form, and cheap units have deadband.
- Industrial servo: closed loop with an encoder and a tuned controller. Holds when the load is inside its rated range and the encoder is on the output, not the motor, if backlash matters.

Holds when: the drive and load are inside the rated torque and speed envelope. Breaks when: the load inertia or acceleration exceeds the pull-out torque (stepper) or the control loop is poorly tuned (servo).

## Pump and fan affinity laws

For geometrically similar machines at the same fluid density, with efficiency unchanged, flow $Q$, head $H$ (or pressure rise), and power $P$ scale as:

- $Q \propto N D^3$, $H \propto N^2 D^2$, $P \propto \rho N^3 D^5$, where $N$ is speed and $D$ is impeller diameter.
- Same impeller, speed change only: $Q_2/Q_1 = N_2/N_1$, $H_2/H_1 = (N_2/N_1)^2$, $P_2/P_1 = (N_2/N_1)^3$.
- Pump example, 1450 to 1160 rpm (ratio 0.80): flow $\times 0.80$, head $\times 0.64$, power $\times 0.51$.
- Fan example, 1000 to 1200 rpm (ratio 1.20): flow $\times 1.20$, pressure $\times 1.44$, power $\times 1.73$.
- Sanity check: halving speed cuts power to one eighth.

Holds when: the fluid is the same, the flow is turbulent enough that efficiency is steady, and the machine is geometrically similar. Breaks when: efficiency falls at low speed, cavitation starts (check net positive suction head available against the pump's required value, with margin set by the pump maker), the impeller is trimmed far from the original, or the fluid is viscous or two-phase.

## System curve and operating point

- System head: $H_{sys}(Q) = H_{static} + K Q^2$, where $H_{static}$ is the elevation and pressure difference in metres of fluid, and $K Q^2$ is friction and minor loss head.
- Friction and minor loss in pipe form: $K = \dfrac{1}{2 g A^2} \left( f \dfrac{L}{D} + \sum K_m \right)$, with $A$ the pipe area (m$^2$) and $K_m$ the minor loss coefficients (dimensionless).
- Operating point: solve $H_{pump}(Q) = H_{sys}(Q)$. The pump runs there, not at its best-efficiency point unless the design put it there.
- Worked check: $H_{static} = 5$ m. Friction is 10 m at $Q = 0.010$ m$^3$/s, so $K = 10 / (0.010)^2 = 1 \times 10^5$ m per (m$^3$/s)$^2$. Pump curve $H_{pump} = 30 - 4 \times 10^5 Q^2$ m. Setting them equal gives $Q^2 = 5 \times 10^{-5}$, so $Q = 7.07 \times 10^{-3}$ m$^3$/s (7.1 L/s) and $H = 10$ m. Check: $30 - 4\times10^5 \times 5\times10^{-5} = 10$ m.
- A throttling valve adds loss, which raises $K$ and moves the operating point to lower flow and higher head.
- Parallel pumps add flows at the same head. Series pumps add heads at the same flow.

Holds when: the flow is steady, friction is quadratic in $Q$ (fully turbulent), and the fluid is the same. Breaks when: flow is laminar (friction is linear in $Q$), the system includes control valves that change with setting, the pump curve is not fitted from data, or two-phase flow occurs.

## Heat exchangers (LMTD)

- Heat balance: $\dot{Q} = \dot m_h c_{p,h} (T_{h,in} - T_{h,out}) = \dot m_c c_{p,c} (T_{c,out} - T_{c,in})$. Units: W, with $\dot m$ in kg/s and $c_p$ in J/(kg K).
- Overall heat transfer coefficient, per area, plane wall: $\dfrac{1}{U} = \dfrac{1}{h_i} + \dfrac{t}{k} + \dfrac{1}{h_o} + R_{foul}$, with $U$ in W/(m$^2$ K).
- Rate equation: $\dot{Q} = U A \, \Delta T_{lm}$.
- Log mean temperature difference: $\Delta T_{lm} = \dfrac{\Delta T_1 - \Delta T_2}{\ln(\Delta T_1 / \Delta T_2)}$, where $\Delta T_1$ and $\Delta T_2$ are the temperature differences at the two ends. If $\Delta T_1 = \Delta T_2$, then $\Delta T_{lm} = \Delta T$.
- Counterflow gives a larger LMTD than parallel flow for the same ends, so it needs less area.
- Worked check: hot 90 to 60 C, cold 20 to 40 C. Counterflow: $\Delta T_1 = 50$, $\Delta T_2 = 40$, $\Delta T_{lm} = 44.8$ K. Parallel: $\Delta T_1 = 70$, $\Delta T_2 = 20$, $\Delta T_{lm} = 39.9$ K. For $\dot Q = 10$ kW and $U = 500$ W/(m$^2$ K), counterflow needs $A = 10\,000 / (500 \times 44.8) = 0.45$ m$^2$.
- Crossflow or multipass: multiply $\Delta T_{lm}$ by a correction factor $F \le 1$ from the standard charts or formulas. Rule of thumb: avoid designs with $F$ below about 0.75. Basis: the temperature cross becomes severe. Limit: depends on the arrangement.
- Effectiveness-NTU method when outlet temperatures are unknown: $NTU = UA / C_{min}$, $C = \dot m c_p$, $\varepsilon = \dot Q / \dot Q_{max}$, $\dot Q_{max} = C_{min}(T_{h,in} - T_{c,in})$. Counterflow with $C_r = C_{min}/C_{max} < 1$: $\varepsilon = \dfrac{1 - e^{-NTU(1-C_r)}}{1 - C_r e^{-NTU(1-C_r)}}$. With $C_r = 1$: $\varepsilon = NTU / (1 + NTU)$.
- Typical overall $U$ (rough, typical, check the design data): liquid to liquid 300 to 3000 W/(m$^2$ K); air to liquid with fins 30 to 100 W/(m$^2$ K), set by the air side; gas to gas 10 to 50 W/(m$^2$ K).

Holds when: steady flow, constant $c_p$ and $U$, and no heat loss to surroundings. Breaks when: $U$ changes with temperature or flow, fouling grows over time, phase change occurs (use $\varepsilon = 1 - e^{-NTU}$ for a fully condensing or boiling side with $C_r \to 0$), or the cold outlet would cross above the hot outlet (in counterflow this makes the design invalid).

## Thermal resistance and electronics cooling

- Analogy: $\Delta T = \dot Q R_{th}$, with $R_{th}$ in K/W. Thermal resistances in series add.
- Junction temperature: $T_j = T_a + P\,\theta_{JA}$, where $P$ is device power dissipation (W), $\theta_{JA}$ is junction-to-ambient resistance from the datasheet (K/W, board-dependent), and $T_a$ is ambient.
- Stacked path: $\theta_{JA} = \theta_{JC} + \theta_{CS} + \theta_{SA}$ (junction to case, case to sink through the interface, sink to ambient).
- Required sink resistance: $\theta_{SA} \le \dfrac{T_{j,max} - T_a}{P} - \theta_{JC} - \theta_{CS}$.
- Worked check: $P = 5$ W, $\theta_{JA} = 20$ K/W, $T_a = 40$ C. $T_j = 40 + 100 = 140$ C. With an example limit $T_{j,max} = 125$ C, $\theta_{JA}$ must be at most $(125 - 40)/5 = 17$ K/W. With $\theta_{JC} = 3$ K/W and $\theta_{CS} = 0.5$ K/W, the sink must have $\theta_{SA} \le 13.5$ K/W. Use the actual $T_{j,max}$ from the datasheet.
- Margin: keep $T_j$ at least 10 K below the absolute maximum as a rule of thumb. Basis: reliability and parameter drift. Limit: the reliability target sets the real margin.
- Convection check: a natural-convection surface with $h = 10$ W/(m$^2$ K) and $A = 0.01$ m$^2$ has $R_{conv} = 1/(hA) = 10$ K/W. Use lesson-level $h$ values only as orders of magnitude: about 5 to 25 W/(m$^2$ K) for natural air, higher for forced air.
- Transients: a pulse shorter than the thermal time constant sees the transient thermal impedance, not $\theta_{JA}$. Use the datasheet's transient thermal curves.

Holds when: the heat path is a single dominant path, steady state is reached, and the datasheet $\theta$ matches the board. Breaks when: most heat leaves through the board copper, the datasheet was measured on a different board, the load is pulsed, or radiation is large at high temperature.

## Two-link planar arm kinematics

Joint variables $\theta_1$ and $\theta_2$ (rad). Here $\theta_2$ is measured relative to link 1, so link 2 has absolute angle $\theta_1 + \theta_2$. Link lengths $L_1$, $L_2$ (m).

Forward kinematics:

- $x = L_1 \cos\theta_1 + L_2 \cos(\theta_1 + \theta_2)$
- $y = L_1 \sin\theta_1 + L_2 \sin(\theta_1 + \theta_2)$
- Worked check: $L_1 = 0.30$, $L_2 = 0.20$, $\theta_1 = 30$ deg, $\theta_2 = 45$ deg gives $(0.3116, 0.3432)$ m, a distance of $0.4635$ m from the base.

Inverse kinematics (two solutions, elbow up and elbow down):

- Let $r^2 = x^2 + y^2$. The target is reachable when $|L_1 - L_2| \le r \le L_1 + L_2$.
- $c_2 = \dfrac{r^2 - L_1^2 - L_2^2}{2 L_1 L_2}$, then $\theta_2 = \pm \arccos(c_2)$. The plus sign is one elbow solution and the minus sign is the other.
- $\theta_1 = \operatorname{atan2}(y, x) - \operatorname{atan2}(L_2 \sin\theta_2, \; L_1 + L_2 \cos\theta_2)$.
- Check: the forward-kinematics tip above returns $\theta_1 = 30.0$ deg and $\theta_2 = 45.0$ deg on the positive branch.
- If $|c_2| > 1$, the target is outside the workspace. Report it, or clamp it, and do not guess.

Jacobian and singularities:

- $J = \begin{bmatrix} -L_1 \sin\theta_1 - L_2 \sin(\theta_1 + \theta_2) & -L_2 \sin(\theta_1 + \theta_2) \\ L_1 \cos\theta_1 + L_2 \cos(\theta_1 + \theta_2) & L_2 \cos(\theta_1 + \theta_2) \end{bmatrix}$
- $\det J = L_1 L_2 \sin\theta_2$. Singular at $\theta_2 = 0$ (arm straight, maximum reach) and at $\theta_2 = \pi$ (arm folded, minimum reach). The worked check gives $\det J = 0.04243$ m$^2$ from both forms.
- Velocity: $\dot{\mathbf{x}} = J \dot{\boldsymbol\theta}$. Static joint torque from tip force $\mathbf F$: $\boldsymbol\tau = J^T \mathbf F$, in N m.

Holds when: links are rigid, the arm is planar, and joint offsets are zero. Breaks when: the motion leaves the plane, joints hit limits, backlash or link flex matter, or the path crosses a singularity (joint speeds blow up near $\det J = 0$).

## DH parameters in words

- Each link in a serial chain is described by four numbers. The link length $a$ is the distance along the common normal between consecutive joint axes. The link twist $\alpha$ is the angle between those axes about the common normal. The link offset $d$ is the distance along the joint axis. The joint angle $\theta$ is the rotation about the joint axis.
- For a revolute joint, $\theta$ is the variable and $d$ is constant. For a prismatic joint, $d$ is the variable and $\theta$ is constant.
- Frame-to-frame transform, in this order: rotate about z by $\theta$, translate along z by $d$, translate along x by $a$, rotate about x by $\alpha$. Multiply the transforms from base to tip to get the tip pose.
- Convention matters. Standard and modified (Craig) DH order the steps differently. State which one the table uses, and use the same one everywhere.
- Check on the planar arm: $a_1 = L_1$, $a_2 = L_2$, $\alpha = 0$, $d = 0$, with $\theta_1$ and $\theta_2$ as the joint angles. The tip position from the product of the two transforms matches the forward kinematics above.
- Holds for serial chains. Breaks for closed loops (parallel mechanisms), flexible links, and joint axes that are parallel or coincident, where the common normal is not unique.

## Checklists

Electrical bring-up:

- [ ] Bench supply has a current limit set before the first power-up.
- [ ] Power dissipation computed for every resistor, transistor, and regulator at worst-case supply, and each is below half its rating (rule of thumb).
- [ ] Logic levels checked on every connection, including 5 V tolerance.
- [ ] Flyback diode on every inductive load.
- [ ] Decoupling on every IC supply pin; common ground planned.
- [ ] Measured voltages at test points compared with the prediction written before the test.

Motor and drive:

- [ ] Stall current and stall torque computed; driver current limit below stall.
- [ ] Continuous and peak torque covered by the duty cycle (RMS check).
- [ ] Gear ratio and efficiency included in the output torque and speed.
- [ ] Supply fused or current-limited.
- [ ] Voltage budget at peak speed and torque checked.

Thermal:

- [ ] $T_j$ predicted with datasheet $\theta$ values and the worst ambient, below the absolute maximum with margin.
- [ ] Interface material between device and sink specified.
- [ ] Heat path drawn as a resistor network.
- [ ] Transient case checked when the load is pulsed.

Fluid:

- [ ] Pump curve and system curve both sourced; operating point found.
- [ ] Reynolds number checked for each pipe, and the right friction model used.
- [ ] Net positive suction head available exceeds required, with the margin the pump maker specifies.
- [ ] Velocity limits from the applicable code checked.

Robot kinematics:

- [ ] Joint angle convention (relative or absolute) and units (rad or deg) written down.
- [ ] Target reachability checked before the solve.
- [ ] Singular configurations ($\theta_2 = 0$ or $\pi$) avoided in the motion plan.

Project risk:

- [ ] Hazards listed: electrical shock, battery fire, pinch points, rotating parts, hot surfaces, pressurized fluid, falling loads.
- [ ] Stored energy identified (capacitors, inductors, springs, pressurized lines) and discharged or locked out before work.
- [ ] Emergency stop path tested.
- [ ] Single points of failure listed, with protection (fuse, current limit, thermal cutoff).
- [ ] Requirements are measurable, with pass and fail numbers.
- [ ] Margin defined for each key number: power, torque, temperature, pressure.
- [ ] Tolerances stacked for the worst case, not only the typical case.
- [ ] Longest-lead part identified, with its lead time.
- [ ] Calculations checked by a second person who did not write them.
- [ ] Datasheet revisions and instrument calibration dates recorded in the log.

## Sanity checks

- Ohm's law: 1 V across 1 k gives 1 mA. If the power is wrong by a factor of 1000, a unit was missed.
- Series resistance exceeds the largest part. Parallel resistance is below the smallest part. Two equal parallel parts give half.
- Divider output lies between 0 and $V_s$, and loading always lowers it.
- Op-amp output lies inside the supply. Inverting gain is negative; non-inverting gain is at least 1.
- RC: 63 percent at $\tau$, 99 percent at about $4.6\tau$.
- Filter: at $f_c$, $-3$ dB and $-45$ deg. Above $f_c$, each tenfold frequency adds about $-20$ dB.
- LED current: $(V_s - V_f)/R$ should land in the typical 5 to 20 mA band. A value far outside means a unit or value error.
- Motor: $\omega_0 = V/K_e$ should be near the rated speed at rated voltage. Stall current is many times the running current, so a stall-level running current means back-EMF was dropped.
- Motor maximum power $= T_s \omega_0 / 4$. Efficiency lies between 0 and 1.
- Pump: input power is above hydraulic power $\rho g Q H$ by the efficiency.
- Fan and pump laws: halving speed gives one eighth of the power.
- Thermal: a $P$ of 1 W through $\theta = 10$ K/W raises the temperature by 10 K.
- Heat balance: hot-side and cold-side heat rates agree within the heat loss you expected.
- Reynolds number in a pipe: below about 2300 is laminar, above about 4000 is turbulent, and between is transitional (typical values).
- Pressure: 1 atm is about 101 kPa. A water column of 10 m is about 98 kPa.
- Arm: the tip is always within $L_1 + L_2$ of the base.
- Sign check: in any feedback loop with a sign error, the output runs to a rail. If the output saturates, check the feedback sign first.

## Further reference

Books (paid, named only):

- Horowitz and Hill, *The Art of Electronics*.
- Sedra and Smith, *Microelectronic Circuits*.
- Craig, *Introduction to Robotics: Mechanics and Control*.
- Spong, Hutchinson, and Vidyasagar, *Robot Modeling and Control*.
- Incropera et al., *Fundamentals of Heat and Mass Transfer*.
- Kays and London, *Compact Heat Exchangers*.
- White, *Fluid Mechanics*.
- Karassik et al., *Pump Handbook*.
- Hughes and Drury, *Electric Motors and Drives*.
- Shigley's *Mechanical Engineering Design*, and the Hydraulic Institute pump standards (by name).

No free online sources are listed. No URL was fetched and confirmed in this session.
