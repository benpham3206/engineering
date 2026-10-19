# Flywheels

**Type:** lesson

A **flywheel** is a rotating mass that stores energy as rotation. Engineers size the flywheel for the energy it must store and limit its rim speed, because a rotor that bursts throws its pieces outward with lethal energy. It smooths the speed of an engine, press, or pump, and it can hold energy for a short time in a grid or vehicle system.

**Prerequisites:** [Rigid body dynamics](../../physics/03-rigid-body-dynamics.md), [Axial and torsion](../../physics/04-axial-and-torsion.md), [Mechanical properties](../../materials/03-mechanical-properties.md), [Factor of safety and failure](../../design/07-factor-of-safety-and-failure.md)
**Time:** 4-6 h

## Core ideas

### How it works

An engine delivers torque in pulses. During the power stroke, the engine torque is larger than the load torque, so the extra energy speeds up the rotor. During the rest of the cycle, the load torque is larger, so the rotor slows and gives energy back. The flywheel keeps the speed within a narrow band.

The energy follows these steps:

1. The engine torque exceeds the load torque for part of each cycle.
2. The excess energy speeds up the rotor and is stored as **kinetic energy**, $E = \tfrac{1}{2} I\omega^2$.
3. For the rest of the cycle, the load torque exceeds the engine torque, and the rotor slows. It gives its energy back to the load.
4. The speed swings between a maximum and a minimum. A larger inertia $I$ or a higher mean speed shrinks the swing for the same energy swing.

The inertia depends on where the mass sits. A thin rim at radius $R$ has $I = mR^2$, so most of the mass should sit far from the axis.

### Main parts

- **Rotor.** The rim carries most of the mass and most of the inertia. A hub, spokes, or a disc connect the rim to the shaft.
- **Hub and bore.** The hub carries torque to the shaft by a key, a spline, or a shrink fit. The bore and the keyway are stress concentrations.
- **Bearings.** The bearings carry the rotor weight and small loads. Vacuum systems and magnetic bearings have their own design rules.
- **Containment.** A housing catches fragments if the rotor bursts.
- **Speed sensor and overspeed trip.** The sensor watches the speed, and the trip cuts the drive when the speed rises too far.

### Variants

- **Thin ring.** Most of the mass sits at the rim. It is simple to analyze, but the rim carries the full stress for its energy.
- **Solid disc.** The disc carries less stress at its rim for its mass, so it can run at a higher rim speed. It stores more energy per kilogram at the limit.
- **Tapered or stepped disc.** More material sits where the stress is low, and less where it is high. It is a common design for high-speed rotors.
- **Steel and composite.** Steel suits engine and press flywheels. Carbon fibre composite rotors run at much higher rim speeds, and they are used for high-speed energy storage. They need careful containment and cost more.

## Key equations

Kinetic energy, with $I$ in kg m$^2$, $\omega$ in rad/s, and $E$ in joules (J):

$$E = \tfrac{1}{2} I \omega^2$$

**Speed fluctuation coefficient**, with $\omega_{\mathrm{max}}$, $\omega_{\mathrm{min}}$, and the mean speed $\omega_m$ all in rad/s:

$$C_s = \frac{\omega_{\mathrm{max}} - \omega_{\mathrm{min}}}{\omega_m}$$

Energy fluctuation per cycle, in J:

$$\Delta E = I\,\omega_m^2\,C_s$$

Inertia needed for a given energy fluctuation:

$$I = \frac{\Delta E}{\omega_m^2\,C_s}$$

**Hoop stress** in a thin rim, with density $\rho$ in kg/m$^3$ and rim speed $v = \omega R$ in m/s, gives $\sigma$ in pascals (Pa):

$$\sigma = \rho v^2$$

Maximum rim speed of a thin ring for an allowable stress $\sigma_{\mathrm{allow}}$ (Pa):

$$v_{\mathrm{max}} = \sqrt{\frac{\sigma_{\mathrm{allow}}}{\rho}}$$

Maximum stress at the centre of a solid disc, with Poisson's ratio $\nu$ (dimensionless, about 0.3 for steel, typical):

$$\sigma_{\mathrm{max}} = \frac{3+\nu}{8}\,\rho v^2$$

Because $(3+\nu)/8$ is about 0.41 for steel, a solid disc can run at about 1.6 times the rim speed of a thin ring at the same stress.

Power of an energy exchange over a time $\Delta t$ (s), in watts (W):

$$P = \frac{\Delta E}{\Delta t}$$

## Worked example

**Given:** A flywheel on an engine runs at a mean speed of $n_m = 600$ rev/min. The energy fluctuation per cycle is $\Delta E = 4.0$ kJ, and the speed fluctuation coefficient is $C_s = 0.02$. The flywheel is a thin steel ring with mean radius $R = 0.50$ m. Steel has a density of $7850$ kg/m$^3$ (typical) and a yield strength of $370$ MPa (typical for cold-drawn 1018 steel).

**Find:** (a) the required inertia $I$, (b) the rim mass $m$, (c) the rim speed $v$ and the hoop stress $\sigma$, and (d) the safety factor against yield.

**Assumptions:** All the mass sits in the rim at radius $R$. The hub and spokes add no inertia. The rim is thin, so the hoop stress formula applies.

**Solution:**

1. Mean angular speed: $\omega_m = 2\pi(600)/60 = 62.83$ rad/s.
2. Inertia: $I = \Delta E/(\omega_m^2 C_s) = 4000/(62.83^2 \times 0.02) = 4000/78.96 = 50.7$ kg m$^2$.
3. Rim mass: $m = I/R^2 = 50.7/0.25 = 203$ kg.
4. Rim speed: $v = \omega_m R = 62.83 \times 0.50 = 31.4$ m/s.
5. Hoop stress: $\sigma = \rho v^2 = 7850 \times 31.4^2 = 7.75$ MPa.
6. Safety factor: $n = 370/7.75 = 47.8$.

**Answer:** (a) $50.7$ kg m$^2$. (b) $203$ kg. (c) $31.4$ m/s and $7.75$ MPa. (d) About $48$.

**Sanity check:** The stored energy is $E = \tfrac{1}{2} I\omega_m^2 = 0.5 \times 50.7 \times 62.83^2 = 100$ kJ. The fluctuation $\Delta E = 4$ kJ is 4 percent of that, which equals $2C_s$, as the formulas predict. The rim stress is far below yield, so the rim is not the limit here. The bore, the keyway, and the spoke joints still need their own stress check, because each revolution cycles those parts.

## Design trade-offs

- **Mass against speed.** Stored energy scales with $I\omega^2$, so speed buys energy more cheaply than mass does. Stress grows with $v^2$, so the rim speed sets the limit.
- **Smoothness against response.** A heavier flywheel holds speed more steadily, but it responds slowly and adds inertia to every start.
- **Ring against disc.** A ring stores the most energy for its rim speed. A disc runs faster at the same stress, so it stores more energy per kilogram at the limit.
- **Usable energy.** Only the energy between $\omega_{\mathrm{min}}$ and $\omega_{\mathrm{max}}$ can be used, which is $\tfrac{1}{2}I(\omega_{\mathrm{max}}^2 - \omega_{\mathrm{min}}^2)$. The rest stays in the rotor.
- **Losses.** Windage and bearing friction drain energy when the rotor spins idle. A vacuum housing or magnetic bearings cut the losses, at extra cost.
- **Balance.** An unbalanced rotor shakes its mounts and its bearings. A high-speed rotor must be balanced to a stated grade.
- **Gyroscopic loads.** A large flywheel in a vehicle or ship resists a change in the direction of its axis. The mount must carry that torque.

## How it fails

- **Overspeed burst.** A governor fault or a sudden load drop raises the speed past the rim's limit. Warning signs are a speed trace that climbs and rising noise. Safety measures include overspeed trips, speed sensors, containment, and a rotor rated above the maximum overspeed.
- **Fatigue at the bore, keyway, or spoke joints.** Each revolution cycles these parts, and sharp corners raise the local stress. A crack at the bore or a growing wobble is the warning. Use fillets, stress analysis with a factor of safety, and scheduled inspection.
- **Imbalance.** A lost bolt, a crack, or an uneven casting shifts the centre of mass. Vibration that rises with speed and worn bearings are the warnings. Balance the rotor to a stated grade, and check it after any repair.
- **Bearing or seal failure.** Poor lubrication or dirt heats the bearing and makes it noisy. Monitor the bearing temperature, and follow the service schedule.
- **Gyroscopic damage to the mount.** A rotor turned about an axis other than its spin axis loads the mount. Loose or cracked mounts are the warnings. Design the mount for the gyroscopic torque.

## History

Rotating masses that keep turning between pushes are very old. Potters' wheels use the same idea, and they store rotation to keep the wheel turning. James Watt added a flywheel to his rotary steam engine in the 1780s, which smoothed the motion of the engine and made it useful for driving machinery. Flywheels then became standard in steam and internal combustion engines.

## Practice

1. A rotor has $I = 2$ kg m$^2$ and spins at $\omega = 300$ rad/s. How much kinetic energy does it store?
2. The same rotor slows from 300 rad/s to 240 rad/s. How much energy does it give back?
3. A flywheel runs at a mean speed of 500 rev/min, with $\Delta E = 2$ kJ per cycle and $C_s = 0.01$. Find the required inertia in kg m$^2$.
4. A thin steel ring has an allowable stress of 200 MPa and a density of 7850 kg/m$^3$. Find its maximum rim speed.
5. A solid steel disc has the same allowable stress of 200 MPa, and $\nu = 0.3$. Find its maximum rim speed.

<details><summary>Answers</summary>

1. $E = \tfrac{1}{2}(2)(300)^2 = 90\,000$ J, which is 90 kJ.
2. $\Delta E = \tfrac{1}{2}(2)(300^2 - 240^2) = 32\,400$ J, which is 32.4 kJ.
3. $\omega_m = 2\pi(500)/60 = 52.36$ rad/s, so $I = 2000/(52.36^2 \times 0.01) = 73.0$ kg m$^2$.
4. $v_{\mathrm{max}} = \sqrt{200\times10^6/7850} = 159.6$ m/s.
5. $v_{\mathrm{max}} = \sqrt{8 \times 200\times10^6/((3.3)(7850))} = 248.5$ m/s.

</details>

## Common mistakes

- Putting rev/min into $\tfrac{1}{2}I\omega^2$. Convert to rad/s first.
- Taking $C_s$ as the difference between the maximum and minimum speed. It is that difference divided by the mean speed.
- Assuming a solid disc and a thin ring have the same rim speed limit. The disc factor $(3+\nu)/8$ lets the disc run faster at the same stress.
- Treating all the stored energy as usable. The speed cannot fall to zero, so only the energy between $\omega_{\mathrm{min}}$ and $\omega_{\mathrm{max}}$ can be delivered.
- Checking the rim and skipping the bore and the spoke joints. The cyclic stress at those parts often governs the design.

## Go deeper

- [*University Physics Volume 1*, Chapter 10 introduction](https://openstax.org/books/university-physics-volume-1/pages/10-introduction) by OpenStax: rotational motion and the energy of a spinning body.
- [2.003SC Engineering Dynamics](https://ocw.mit.edu/courses/2-003sc-engineering-dynamics-fall-2011/) by MIT OpenCourseWare: rigid-body rotation and angular momentum.
- [Shafts and bearings](../../design/08-shafts-and-bearings.md): how the shaft and the bearings carry the rotor.
- [Energy storage](../energy/06-energy-storage.md): flywheels next to batteries, pumped hydro, and compressed air at grid scale.
- [Clutches and brakes](04-clutches-and-brakes.md): flywheels in clutch and brake assemblies.
- [Applications reference](../reference.md): the lookup sheet for this topic.
