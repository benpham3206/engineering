# Washing machines and dryers: spin g-force, balance, and drying heat

**Type:** lesson

A washing machine spins a drum fast enough to throw water out of clothes, and a dryer heats air to evaporate the rest. The spin g-force grows with the square of the drum speed and with the drum radius, and an unbalanced load turns that force into shaking. Engineers who size drums, motors, and suspensions need these relations and the safety measures they demand.

**Prerequisites:** [Particle dynamics](../../physics/02-particle-dynamics.md), [Rigid-body dynamics](../../physics/03-rigid-body-dynamics.md), [Vibrations](../../physics/13-vibrations.md), [Heat transfer](../../physics/12-heat-transfer.md)
**Time:** 3-4 h

## Core ideas

### How it works

A front-loading or top-loading washer holds a perforated drum inside an outer tub. A motor turns the drum, first slowly for washing and then quickly for spinning. During a spin, the drum wall pushes the clothes inward toward the axis, and water passes through the perforations because the clothes press against the drum wall and the water cannot. The centripetal force acts on the wet clothes, so the water leaves through the holes and drains.

A dryer tumbles wet clothes in a rotating drum while air moves across them. A heater warms the air, the warm air evaporates the water, and the moist air leaves through a vent or a condenser. Energy goes into evaporating water, so the heat supply sets the drying speed.

### Main parts

- **Drum**: a perforated cylinder that carries the load and sets the spin radius.
- **Tub and suspension**: the outer tub holds water. Springs and dampers hold the tub and drum on their supports.
- **Drive motor**: a brushless or induction motor, driving the drum through a belt or direct drive.
- **Balance sensors and counterweights**: detect an off-centre load and adjust spin speed to keep vibration low.
- **Door interlock**: keeps the door locked while the drum turns.
- **Heater and lint filter** (dryers): the heater supplies heat, and the filter traps fibres before they reach the hot element.

### Variants

- **Top-loader agitator**: the agitator moves the load, and the drum spins only for water removal.
- **Front-loader**: the drum rotates horizontally, which spins faster for the same motor and suits heavier loads.
- **Condenser dryer**: cools the moist air and collects the water. It needs no outside vent.
- **Vented dryer**: exhausts moist air outdoors and uses less energy per cycle in some designs.

## Key equations

Assumptions for all equations below: the drum rotates about a fixed axis at constant speed, the clothes press against the drum wall, and the radius is measured to the inside of the drum wall where the clothes touch.

Angular speed from revolutions per minute:

$$\omega = \frac{2\pi N}{60}$$

where $\omega$ is the angular speed in radians per second (rad/s) and $N$ is the speed in revolutions per minute (rpm).

Centripetal acceleration of the clothes:

$$a = \omega^{2} r$$

where $a$ is the acceleration in metres per second squared (m/s$^2$) and $r$ is the drum radius in metres (m).

Spin g-force, with $g = 9.81\ \text{m/s}^2$ (standard gravity):

$$G = \frac{\omega^{2} r}{g}$$

where $G$ is dimensionless, expressed as multiples of $g$.

Unbalance force from an off-centre mass, assuming a rigid rotor and ignoring damping:

$$F = m\,e\,\omega^{2}$$

where $F$ is the force in newtons (N), $m$ is the unbalanced mass in kilograms (kg), and $e$ is the eccentricity of the mass centre in metres (m).

Energy to evaporate water, assuming all water evaporates and ignoring sensible heat and losses:

$$Q = m_{w}\,h_{fg}$$

where $Q$ is the energy in joules (J), $m_{w}$ is the water mass in kilograms (kg), and $h_{fg} \approx 2.26\ \text{MJ/kg}$ is the latent heat of vaporization of water at 100 °C (typical value).

## Worked example

**Given:** A drum with radius $r = 0.25\ \text{m}$ spins at $N = 1200\ \text{rpm}$.

**Find:** (a) the centripetal acceleration, (b) the spin g-force, and (c) the force from a 2 kg wet load whose centre sits 0.05 m off the drum axis.

**Solution:**

1. Angular speed: $\omega = 2\pi \times 1200 / 60 = 125.7\ \text{rad/s}$.
2. Acceleration: $a = 125.7^2 \times 0.25 = 3948\ \text{m/s}^2$.
3. Spin force: $G = 3948 / 9.81 = 402$, so about 400 times gravity.
4. Unbalance force: $F = 2 \times 0.05 \times 125.7^2 = 1579\ \text{N}$. The load weighs $2 \times 9.81 = 19.6\ \text{N}$, so the force is about 80 times its weight.

**Answer:** (a) About $3.9 \times 10^3\ \text{m/s}^2$. (b) About $402\ \text{g}$. (c) About $1.6 \times 10^3\ \text{N}$.

**Sanity check:** Going from 800 rpm to 1200 rpm multiplies $G$ by $(1200/800)^2 = 2.25$. The computed values are $179\ \text{g}$ and $402\ \text{g}$, and $402/179 = 2.25$, which matches.

**Dryer energy.** Removing 2 kg of water needs $Q = 2 \times 2.26 = 4.52\ \text{MJ}$, which is about $1.26\ \text{kWh}$ before losses. That is the latent part only, so a real cycle uses more.

## Design trade-offs

- **Spin speed versus energy**: a faster spin removes more water and saves drying energy, but it needs a stronger drum, a stronger motor, and better balance.
- **Drum radius**: a larger radius raises $G$ for the same rpm, but a fixed cabinet limits how large the drum can be.
- **Balance and noise**: stiff suspensions transmit more vibration to the floor. Soft suspensions with dampers let the tub move, which reduces transmitted force and noise.
- **Dryer heat**: higher air temperature dries faster but risks fabric damage and fire. Heat pump dryers use less energy but dry more slowly.
- **Life**: bearings and seals fail first. Drums that are not balanced wear bearings much faster.

## How it fails

- **Unbalance**: a heavy wet load on one side makes the drum shake violently. Warning signs are loud banging, walking across the floor, and fault codes.
- **Bearing wear**: unbalance overloads the drum bearings. Grinding noise and leaks past the seal are warning signs.
- **Door opening during spin**: a missing or failed interlock lets the door open while the drum still turns. This is a severe injury hazard.
- **Dryer fire**: lint collects on the heater and filter. Blocked airflow overheats the element, which can ignite lint.
- **Overheating motor**: a failed cooling fan or a jammed drum overloads the motor, and it can burn out.

## Hierarchy of controls for spin and fire hazards

- **Elimination**: a machine that cannot spin does not spin. Designers remove spin from the washing stage where it is not needed, but this is not an option for spinning machines.
- **Substitution**: a lower spin speed or a gentler cycle reduces $G$ and the unbalance force. Heat pump dryers replace electric resistance heating with lower-temperature heat transfer.
- **Engineering controls**: the door interlock locks the door until the drum stops. Balance sensors stop or slow spin when a load is off centre. A thermal cutoff on the heater shuts it off if the air temperature rises too far. A lint filter and sensor stop the dryer when airflow drops.
- **Administrative controls**: follow the rated load and never run a machine with a damaged door or interlock. Clean the lint filter after every dryer cycle.
- **Personal protective equipment**: not applicable for normal home use. Service technicians wear eye protection and gloves when working on drums and springs.

## History

Early washing machines used hand-cranked drums and wringer rollers before electric motors took over. Spin-dry drums came into common use in the early twentieth century, when the centrifugal principle was applied to water removal. Clothes dryers followed the same path, and both appliances spread widely in homes after electric power reached most households. Exact dates and inventors vary by country, so treat any single date as approximate.

## Practice

1. A drum with radius 0.22 m spins at 1100 rpm. What is the spin g-force?
2. What is the maximum rpm for 500 g on a drum with radius 0.25 m?
3. A 3 kg load has its centre 0.03 m from the axis and spins at 1000 rpm. What is the unbalance force?
4. How much energy, in MJ, is needed to evaporate 1.5 kg of water, using latent heat only?

<details><summary>Answers</summary>

1. $\omega = 115.2\ \text{rad/s}$, $G = 115.2^2 \times 0.22 / 9.81 = 298\ \text{g}$, which is about $298\ \text{g}$.
2. $N = (60 / 2\pi)\sqrt{500 \times 9.81 / 0.25} = 1338\ \text{rpm}$, which is about $1340\ \text{rpm}$.
3. $F = 3 \times 0.03 \times 104.7^2 = 987\ \text{N}$, which is about $990\ \text{N}$.
4. $1.5 \times 2.26 = 3.39\ \text{MJ}$.

</details>

## Common mistakes

- Using the drum diameter as the radius. The formula needs the radius to the drum wall.
- Using rpm directly in $\omega^2 r$ without converting to rad/s. Divide by 60 and multiply by $2\pi$ first.
- Assuming the spin force acts on the water only. It acts on the whole load, and the water leaves because the drum holes let it pass.
- Treating dryer energy as only the latent heat. Real cycles also heat the fabric, the drum, and the air, and they lose heat through the vent.
- Ignoring the door interlock and balance sensors. They are safety controls, not optional features.

## Go deeper

- [OpenStax University Physics Volume 1, fixed-axis rotation](https://openstax.org/books/university-physics-volume-1/pages/10-introduction): angular speed and centripetal acceleration for a rotating body.
- [Vibrations](../../physics/13-vibrations.md): unbalance and resonance in rotating machines.
- [Mechanics reference sheet](../../physics/reference-mechanics.md): centripetal and rotational relations.
- [Thermofluids reference sheet](../../physics/reference-thermofluids.md): heat and latent heat relations for drying.
- Related lessons: [Vacuum cleaners](04-vacuum-cleaners.md), [Heat transfer](../../physics/12-heat-transfer.md).
