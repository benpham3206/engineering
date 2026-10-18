# Implants and pacemakers

**Type:** lesson

An implant is a device placed inside the body for years. Passive implants, such as joint replacements, carry load, and active implants, such as pacemakers, also store and deliver energy. Engineers must design both kinds to survive body fluids, repeated loading, and a sealed environment where a failure cannot be repaired without surgery.

**Prerequisites:** [Electricity and magnetism](../../physics/06-electricity-and-magnetism.md), [Metals, polymers, ceramics, composites](../../materials/05-material-classes.md), [Failure: fracture and fatigue](../../materials/06-fracture-and-fatigue.md), [Failure: creep and corrosion](../../materials/07-creep-and-corrosion.md), [Circuit basics](../electronics/01-circuit-basics.md), [Batteries](../electrical/06-batteries.md)
**Time:** 6-8 h

## Core ideas

### How it works

A pacemaker keeps watch on the heart's own electrical activity. A sensing amplifier listens through the lead electrodes that touch the heart muscle. If the heart does not beat within a set interval, a pulse generator sends a short electrical stimulus through the lead. The stimulus causes the muscle to contract. The circuit lowers its output to the smallest pulse that still works, which saves energy. A rate-responsive design adds an accelerometer or other sensor to change the pacing rate with activity. A telemetry coil lets a clinician read the device and change its settings through the skin.

Joint replacements work on a different principle. A metal or ceramic component replaces the surface of a bone joint. A polymer bearing, such as ultra-high-molecular-weight polyethylene, slides against it. The load passes through the implant into the bone, and bone grows onto or into the fixation surface.

### Main parts

- Hermetic housing: a titanium or other biocompatible metal case, sealed so body fluids cannot reach the electronics.
- Battery: a lithium cell, typically lithium-iodine chemistry in pacemakers. It must hold charge for years at a low self-discharge rate.
- Feedthroughs: ceramic-to-metal seals that carry signals through the housing without leaks.
- Leads: insulated conductor coils, usually silicone or polyurethane insulation. The distal tip contacts the heart muscle.
- Header connector: the interface between the leads and the housing. ISO 5841-3 defines the common low-profile connector.
- Electronics: a microcontroller, sense amplifier, pulse generator, and telemetry radio.
- Joint implants: a stem or cup fixed to bone, a head or liner that bears load, and a polymer or ceramic bearing surface.

### Variants

- Single-chamber pacemakers pace one heart chamber. Dual-chamber devices pace two. Biventricular devices pace both ventricles to coordinate contraction.
- Implantable cardioverter-defibrillators (ICDs) share many parts with pacemakers but deliver high-energy shocks.
- Leadless pacemakers sit entirely inside the heart chamber, with no leads to the chest.
- Hip replacements use metal-on-polyethylene, metal-on-metal, or ceramic-on-ceramic bearings. Each pairing trades friction, wear debris, and cost differently.
- Cochlear implants and retinal prostheses are active implants that stimulate nerves. They use the same battery, feedthrough, and telemetry ideas as pacemakers.

## Key equations

- Pulse energy: $E = V^2 t / R$. Here $V$ is pulse amplitude in volts, $t$ is pulse width in seconds, $R$ is the electrode-tissue resistance in ohms, and $E$ is in joules. Assumes a constant amplitude over the pulse and a purely resistive load.
- Average pacing power: $P_\text{pace} = E\, f_\text{rate}$. Here $f_\text{rate}$ is pulses per second, and $P_\text{pace}$ is in watts. Assumes each pulse has the same energy.
- Quiescent power: $P_q = I_q V_b$. Here $I_q$ is the standby current in amperes and $V_b$ is the battery voltage in volts. Assumes a constant standby current.
- Battery energy: $E_b = C\, V_b \times 3600$. Here $C$ is capacity in ampere-hours, $V_b$ is nominal voltage in volts, and $E_b$ is in joules. Assumes a constant nominal voltage over the discharge, which is a simplification.
- Device life: $t_\text{life} = E_b / P_\text{avg}$. Here $P_\text{avg}$ is the total average power in watts. Assumes a constant average draw, with no self-discharge or end-of-life margin.

## Worked example

**Given:** A pacemaker delivers pulses of $V = 2.5\ \text{V}$ and $t = 0.4\ \text{ms}$ into an electrode-tissue resistance of $R = 500\ \Omega$, at one pulse per second. Its standby current is $I_q = 10\ \mu\text{A}$. The battery is a $1.2\ \text{Ah}$ cell at a nominal $2.8\ \text{V}$. Assume a constant nominal voltage, a constant average draw, and no self-discharge. These are illustrative figures for the calculation, not data for a specific device.

**Find:** (a) the energy per pulse, (b) the total average power, and (c) the ideal device life.

**Solution:**

1. Pulse energy: $E = (2.5)^2 \times 0.0004 / 500 = 5.0\ \mu\text{J}$.
2. Pacing power: $P_\text{pace} = 5.0\ \mu\text{J} \times 1\ \text{Hz} = 5.0\ \mu\text{W}$.
3. Standby power: $P_q = 10\ \mu\text{A} \times 2.8\ \text{V} = 28\ \mu\text{W}$.
4. Total power: $P_\text{avg} = 5.0 + 28 = 33\ \mu\text{W}$.
5. Battery energy: $E_b = 1.2 \times 2.8 \times 3600 = 12\,096\ \text{J}$.
6. Life: $t_\text{life} = 12\,096 / 33\times10^{-6} = 3.67\times10^{8}\ \text{s}$, or about 11.6 years.

**Answer:** (a) $E = 5.0\ \mu\text{J}$ per pulse. (b) $P_\text{avg} = 33\ \mu\text{W}$. (c) About 11.6 years under the ideal, constant-draw assumptions.

**Sanity check:** Pacing takes about 15 percent of the total power in this example, so standby current dominates. The ideal life is an upper bound. Real devices add sensing, telemetry, and higher pacing outputs, which shorten the life in practice, so a published life is typically shorter than the ideal figure.

## Design trade-offs

- Battery size against device size. The battery is often the largest part of the device, so designers cut standby current and pulse energy to keep the case small.
- Pulse energy against tissue response. A higher amplitude or longer pulse gives a larger margin, but it draws more energy from the battery.
- Lead flexibility against durability. Soft leads are kinder to tissue, but repeated flexing with each heartbeat fatigues the conductor.
- Stiffness against bone health. Titanium alloy Ti-6Al-4V has a Young's modulus of about 110 GPa (typical), and cortical bone has about 17 GPa (typical). A stiff stem carries much of the load that the bone would otherwise carry, and the bone can thin from disuse. This is called stress shielding. Designers tune stem stiffness and fixation to limit it.
- Bearing material against wear. Polyethylene bearings wear and shed debris over years, and the debris can trigger bone loss. Ceramic bearings resist wear better but are brittle.
- MRI compatibility. Leads, housings, and magnetic components respond to strong fields and gradient coils. Designers choose materials and layouts that keep heating and force within labeled limits.

## How it fails

- Lead fracture. Repeated flexing fatigues the conductor, which breaks or creates an intermittent short. Warning signs include sensed noise and changes in measured resistance.
- Electrode tissue response. Scar tissue grows around the electrode and raises the pulse energy needed to make the muscle contract. Warning signs include a change in the measured pacing threshold.
- Battery depletion. The device sends an end-of-life signal through telemetry and changes its mode to a safe, reduced function.
- Electromagnetic interference. Strong external fields can disturb sensing. Shielding, filtering, and a defined interference mode limit the effect.
- Corrosion and wear in joints. Metal ions and polymer debris can cause local inflammation and loosening over time.
- Infection. Bacteria can form a biofilm on a device surface, which is hard to clear without removal.

**Risk management.** ISO 14971 governs these hazards. The manufacturer estimates the risk of each hazard, reduces it with controls, and verifies the residual risk. ISO 10993 governs biological evaluation of the materials. The hierarchy of controls applies as follows.

- Elimination: remove the hazard. For example, design the housing without sharp edges and without exposed metal that could corrode in fluid.
- Substitution: replace the hazard source. For example, use ceramic bearings in place of metal-on-metal pairs, or a more fatigue-resistant lead conductor.
- Engineering controls: build protection into the design. For example, a sealed housing, redundant sensing paths, a safe fallback mode when the battery is low, and fault detection in the firmware.
- Administrative controls: labeling, instructions for use, MRI-conditional labeling, a patient device identification card, and service procedures for clinics.
- Personal protective equipment: worn by surgical staff during implantation, such as sterile gowns and gloves. It protects the staff and the sterile field, not the device.

**Regulation and standards.** The FDA classifies pacemakers as Class III devices, which need a premarket approval (PMA) application. Joint replacements and other implants have their own classifications, which must be checked in the FDA database. ISO 14708-2 covers active implantable medical devices such as pacemakers. ISO 10993 covers biocompatibility, and the test program depends on how the material contacts the body and for how long. ISO 13485 covers the quality management system, and ISO 14971 covers risk management.

## History

In 1958, Åke Senning and Rune Elmqvist implanted an early pacemaker at the Karolinska Institute in Stockholm, and the patient lived for years with the device. Wilson Greatbatch in Buffalo, New York, helped develop the implantable pulse generator, and his work led to reliable battery-powered devices in the early 1960s. John Charnley at Wrightington Hospital in England developed a low-friction total hip replacement in the early 1960s. In Sweden during the 1950s and 1960s, Per-Ingvar Brånemark studied how bone bonds to titanium, a finding that later shaped dental and orthopedic implants.

## Practice

1. A pulse of $V = 3.0\ \text{V}$ and $t = 0.5\ \text{ms}$ is delivered into $R = 600\ \Omega$. Find the energy per pulse in microjoules.
2. Using the energy from problem 1, find the average pacing power at one pulse per second.
3. A battery of $0.5\ \text{Ah}$ has a nominal voltage of $3.0\ \text{V}$. Find its energy in joules.
4. The device draws a constant $20\ \mu\text{W}$. Using the energy from problem 3, find the ideal life in years.
5. Titanium alloy has a Young's modulus of $110\ \text{GPa}$, and cortical bone has $17\ \text{GPa}$. Find the ratio, and state what the ratio means for a stem that is fixed in bone.

<details><summary>Answers</summary>

1. $E = 9 / 600 \times 0.0005 = 7.5\ \mu\text{J}$
2. $P = 7.5\ \mu\text{W}$
3. $E_b = 0.5 \times 3.0 \times 3600 = 5400\ \text{J}$
4. $t = 5400 / 20\times10^{-6} = 2.7\times10^{8}\ \text{s} = 8.6$ years, under ideal constant-draw assumptions
5. $110 / 17 = 6.5$. The stem is about 6.5 times stiffer than the bone, so it carries more of the load than the bone does, which is the origin of stress shielding.

</details>

## Common mistakes

- Using the pulse width in milliseconds without converting to seconds. Energy in joules needs seconds.
- Treating ampere-hours as energy. Energy needs the voltage as well: $E = C V$.
- Assuming the ideal battery life equals the device life. Self-discharge, telemetry, and end-of-life margins all shorten the real life.
- Calling a material biocompatible in general. Biocompatibility depends on the device, the contact, and the time in the body, and ISO 10993 tests it for each use.
- Ignoring stress shielding when choosing a stiff metal stem. A stiffer implant can weaken the surrounding bone over time.

## Go deeper

- [Robotic and Bionic Medical Devices, National Institute of Biomedical Imaging and Bioengineering](https://nibib.nih.gov/science-education/science-topics/robotic-bionic-medical-devices): an NIH overview of implants and bionic devices, including cochlear implants and retinal prostheses.
- [Classify Your Medical Device, U.S. Food and Drug Administration](https://www.fda.gov/medical-devices/overview-device-regulation/classify-your-medical-device): device classes and the PMA pathway for Class III devices.
- [Materials reference](../../materials/reference.md) for the properties of titanium, ceramics, and polymers.
- [Mechanical properties](../../materials/03-mechanical-properties.md) for stiffness, strength, and the modulus values used in the stress shielding example.
- [Batteries](../electrical/06-batteries.md) for capacity, energy density, and the self-discharge of lithium cells.
