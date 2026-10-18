# Prosthetics and orthotics

**Type:** lesson

A prosthesis replaces a missing limb, and an orthosis supports or corrects a limb that remains. Engineers design both to carry body loads, copy the motion of a healthy joint, and stay comfortable against the skin for many hours a day.

**Prerequisites:** [Statics](../../physics/01-statics.md), [Rigid body dynamics](../../physics/03-rigid-body-dynamics.md), [Mechanical properties](../../materials/03-mechanical-properties.md), [Failure: fracture and fatigue](../../materials/06-fracture-and-fatigue.md), [Batteries](../electrical/06-batteries.md)
**Time:** 6-8 h

## Core ideas

### How it works

A prosthesis moves load and motion between the body and the ground. Walking repeats a gait cycle. In normal adult walking at a comfortable speed, the stance phase, when the foot is on the ground, takes about 60 percent of the cycle, and the swing phase takes about 40 percent (typical values). During stance the device holds body weight. During swing it lets the limb move forward with little resistance.

A prosthetic leg carries load through four steps in stance:

1. The heel contacts the ground, and the device takes the body weight.
2. The knee or ankle bends under load, and a damper or spring absorbs energy.
3. The body rolls forward over the foot, and the keel stores elastic energy.
4. The foot pushes off, and the stored energy returns to the gait.

Inside the socket, the residual limb presses against a soft liner. The socket spreads that pressure over the skin, and the pylon carries the rest of the load down to the foot.

### Main parts

- Socket: the cup that holds the residual limb. It transfers pressure into soft tissue and fixes the limb to the device.
- Suspension: a liner, pin lock, or vacuum system that keeps the socket on the limb during swing.
- Pylon or shank: the rigid tube or bar that carries the axial load from the socket to the foot. Aluminum and carbon-fiber composites are common materials.
- Knee unit, for transfemoral devices: a hinge with friction, hydraulic damping, and a stance lock. Microprocessor knees change damping from sensor data during each step.
- Foot or ankle: a keel of carbon-fiber composite that stores and returns elastic energy. A powered ankle adds a motor and a gearbox.
- Sensors and controller, in powered and microprocessor devices: load cells, inertial sensors, and a microcontroller that sets damping or motor torque.

### Variants

- Transtibial (below the knee) and transfemoral (above the knee) prostheses differ mainly in the knee joint.
- Passive devices use springs, friction, and hydraulic dampers only. They need no battery.
- Microprocessor devices adjust damping or stance locking from sensors. Battery life now limits the design.
- Powered devices use motors to add energy at push-off. They are the heaviest of the three and need the most battery energy.
- Orthoses support a limb that remains. An ankle-foot orthosis (AFO) holds the ankle in a set range of motion. A knee-ankle-foot orthosis (KAFO) also controls the knee. Spinal braces support the trunk.

## Key equations

- Body weight: $W = m g$. Here $m$ is body mass in kilograms, $g = 9.81\ \text{m/s}^2$ is standard gravity at sea level, and $W$ is in newtons. Assumes the body accelerates little, so no inertial force adds to the ground force.
- Ankle moment: $M = F d$. Here $F$ is the vertical ground reaction force in newtons, $d$ is the horizontal distance in metres from the ankle joint center to the center of pressure, and $M$ is in newton metres. Assumes a quasi-static sagittal-plane model with negligible limb inertia.
- Normalized moment: $M_n = M / m$, in $\text{N m/kg}$. Assumes $M$ is the net joint moment from inverse dynamics.
- Average socket pressure: $p = F / A$. Here $F$ is in newtons, $A$ is the contact area in square metres, and $p$ is in pascals. Assumes uniform pressure over the contact area. Real sockets only approximate this.
- Stored energy in a linear keel: $U = \tfrac{1}{2} k x^2$. Here $k$ is stiffness in newtons per metre, $x$ is deflection in metres, and $U$ is in joules. Assumes linear elastic behavior with no energy loss.

## Worked example

**Given:** An adult of mass $m = 75\ \text{kg}$ walks at a steady speed. The peak vertical ground reaction force is $1.2 W$, a typical value for walking. The typical peak net ankle plantarflexor moment in late stance is $1.5\ \text{N m/kg}$. Assume the quasi-static, sagittal-plane model above and $g = 9.81\ \text{m/s}^2$.

**Find:** (a) the peak ankle moment, (b) the moment arm that the ground force needs, and (c) a check of (a) using a moment arm of $0.13\ \text{m}$.

**Solution:**

1. Ankle moment: $M = 1.5 \times 75 = 112.5\ \text{N m}$.
2. Body weight: $W = 75 \times 9.81 = 735.8\ \text{N}$, so the peak force is $F = 1.2 \times 735.8 = 882.9\ \text{N}$.
3. Moment arm: $d = M / F = 112.5 / 882.9 = 0.127\ \text{m}$.
4. Check: $M = 882.9 \times 0.13 = 114.8\ \text{N m}$.

**Answer:** (a) $112.5\ \text{N m}$. (b) $d \approx 0.127\ \text{m}$. (c) With $d = 0.13\ \text{m}$, the moment is $114.8\ \text{N m}$, about 2 percent above the normalized value.

**Sanity check:** A moment arm of about 0.13 m is a plausible distance from the ankle to the forward center of pressure at push-off. For the same walker, the typical peak knee extension moment in early stance is about $0.5\ \text{N m/kg}$, or $37.5\ \text{N m}$. That is about one third of the ankle moment, which matches the usual pattern in normal gait. The knee value is a typical figure that varies with walking speed and study.

## Design trade-offs

- Mass against strength. Carbon-fiber pylons and keels cut mass, but a thin laminate fatigues faster. Designers set the layup and thickness from a fatigue life target.
- Energy return against stability. A stiff keel returns more energy at push-off, but it can feel harsh on uneven ground.
- Battery life against features. Microprocessor and powered devices must run a full day of walking on one charge. A powered ankle adds a motor and gearbox, which add mass and energy use.
- Socket fit against skin health. A tight socket gives control, but it raises pressure on the skin. A loose socket slips and changes the gait.
- Cost against function. Microprocessor and powered devices cost much more than passive ones, so the choice depends on the user's activity and the payer's rules.

## How it fails

- Fatigue cracks in pylons and keels. Repeated loading makes cracks grow each cycle until the part breaks. Warning signs include new cracks, creaking, and a change in stiffness. See [Failure: fracture and fatigue](../../materials/06-fracture-and-fatigue.md).
- Skin breakdown under the socket. High or uneven pressure causes blisters and sores. Redness that does not fade is a warning sign.
- Loose suspension. A worn liner or pin lock lets the limb move inside the socket, so the device no longer matches the gait.
- Battery depletion or electronic faults in powered and microprocessor devices. A low-battery alarm or a sensor fault code signals the problem.
- Corrosion of metal connectors. Sweat and salt speed galvanic corrosion where dissimilar metals touch.

**Risk management.** ISO 14971 sets the process for these hazards. The manufacturer identifies each hazard, estimates the risk from severity and probability, reduces the risk with controls, and verifies the residual risk. The controls follow the hierarchy below, from most to least effective.

- Elimination: remove the hazard. For example, round and deburr every edge that touches skin.
- Substitution: replace the hazard source. For example, use a more fatigue-resistant laminate or a corrosion-resistant alloy.
- Engineering controls: build protection into the device. For example, a stance lock that holds when the controller fails, and a proof load test on each pylon.
- Administrative controls: written procedures and information. For example, fitting protocols, instructions for use, inspection schedules, and warning labels.
- Personal protective equipment: worn by staff who fabricate or adjust devices, such as eye protection and gloves when grinding composites. It protects workers, not the wearer.

**Regulation and standards.** The FDA classifies medical devices by risk into Class I, II, and III. Class I or II devices that are not exempt need a 510(k) premarket notification. Class III devices need a premarket approval (PMA) application. Many prosthetic components fall in Class I or II, but the product's classification must be checked in the FDA database. ISO 22523 sets requirements and test methods for external limb prostheses and orthoses. ISO 10993 covers biological evaluation of materials that touch the body. ISO 13485 covers the quality management system, and ISO 14971 covers risk management.

## History

Some of the oldest known prostheses are simple wood and leather devices. A wooden toe found in Egypt dates to roughly the first millennium BC. In the sixteenth century, the French surgeon Ambroise Paré designed articulated iron hands that used springs and catches. War wounds drove many improvements in socket design and artificial limbs through the nineteenth and twentieth centuries. Lightweight carbon-fiber keels appeared in the late twentieth century. Microprocessor-controlled knees and powered ankles are more recent developments.

## Practice

1. A person of mass $60\ \text{kg}$ has a peak net ankle moment of $1.5\ \text{N m/kg}$. Find the moment in newton metres.
2. Find the body weight in newtons of a person of mass $75\ \text{kg}$. Use $g = 9.81\ \text{m/s}^2$.
3. A ground force of $800\ \text{N}$ acts $0.12\ \text{m}$ forward of the ankle joint center. Find the moment.
4. A socket applies $500\ \text{N}$ over a uniform contact area of $0.0025\ \text{m}^2$. Find the average pressure in kilopascals.
5. A linear keel has stiffness $20\ \text{kN/m}$ and compresses $10\ \text{mm}$. Find the stored energy in joules, assuming linear elastic behavior.

<details><summary>Answers</summary>

1. $90\ \text{N m}$
2. $736\ \text{N}$ (735.8 N)
3. $96\ \text{N m}$
4. $200\ \text{kPa}$
5. $1.0\ \text{J}$

</details>

## Common mistakes

- Using mass where force is needed. The ground force is $mg$ in newtons, not kilograms.
- Measuring the moment arm from the wrong point. The arm runs from the joint center to the line of action of the force.
- Treating a static estimate as the peak. Dynamic loads at faster walking speeds exceed quasi-static estimates.
- Assuming uniform socket pressure. Real pressure varies over bone and soft tissue.
- Designing for static strength alone. Walking repeats thousands of cycles each day, so fatigue usually limits the life of pylons and keels.

## Go deeper

- [Robotic and Bionic Medical Devices, National Institute of Biomedical Imaging and Bioengineering](https://nibib.nih.gov/science-education/science-topics/robotic-bionic-medical-devices): an NIH overview of bionic limbs and related devices.
- [Classify Your Medical Device, U.S. Food and Drug Administration](https://www.fda.gov/medical-devices/overview-device-regulation/classify-your-medical-device): device classes and premarket pathways.
- [Mechanics reference](../../physics/reference-mechanics.md) and [Materials reference](../../materials/reference.md).
- [Factor of safety and failure](../../design/07-factor-of-safety-and-failure.md) for how designers set safety margins.
- [Statics](../../physics/01-statics.md) for the moment and force balance used in the worked example.
