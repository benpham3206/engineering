# Differentials and transmissions

**Type:** lesson

A transmission is a set of gears that changes the speed and torque from the engine to the wheels, and a differential is a gear set that lets the
two driven wheels turn at different speeds in a corner. Engineers pick the gear ratios to match the
engine's power band to the vehicle's speed and load, and they set the differential to balance traction
against steering and wear. Both parts follow simple ratio and torque rules, and efficiency decides how
much of the engine's power arrives at the road.

**Prerequisites:** [Rigid body dynamics](../../physics/03-rigid-body-dynamics.md), [Axial and torsion](../../physics/04-axial-and-torsion.md), [Gears, fasteners, and springs](../../design/09-gears-fasteners-and-springs.md)
**Time:** 8 to 10 h

## Core ideas

### How it works

A gear pair changes speed and torque. The gear ratio is $G = N_{\mathrm{out}}/N_{\mathrm{in}}$, where $N$ is the tooth count.
A pair with more teeth on the output side turns the output slower and gives it more torque. Power stays
the same apart from losses, so torque times speed is nearly constant through the gears. A transmission is a
set of gear pairs. A driver picks one pair at a time, or the transmission changes pairs by itself.

The differential sits between the two driven wheels. In a car, the engine turns the ring gear through
the final drive. The ring gear turns a carrier that holds two small bevel gears, the spider gears. Those
gears drive two side gears, one on each axle. When the car goes straight, the wheels turn at the same
speed. In a corner, the outer wheel must turn faster, and the spider gears rotate on the carrier to let it.

Torque in an open differential splits equally between the two wheels. Equal torque is the reason the
differential loses traction. If one wheel spins on ice, the other gets no more torque than the spinning
wheel can carry through its contact with the ground.

### Main parts

A manual transmission has input and output shafts, a set of gear pairs, synchronizers that match the
speeds of a gear before it locks, and a shift linkage. An automatic transmission has a torque converter,
planetary gear sets, and clutches and bands that hold or release each part of the gear set. A continuously
variable transmission, or CVT, has two variable-diameter pulleys and a belt or chain that runs between them.

A differential has a ring gear, a pinion that drives the ring gear, a carrier, spider gears, and side gears.
A limited-slip differential adds clutch plates, a helical gear set, or a viscous coupling that resists
speed difference between the wheels.

### Variants

A manual gearbox has a fixed set of ratios, and the driver chooses one. Its ratios are spaced so that the
engine stays inside a useful speed band at each step.

An automatic transmission uses a torque converter, which is a fluid coupling with a stator. At low speed,
the stator redirects the fluid, so the converter multiplies torque. The converter locks up at higher speed,
so it stops slipping. Planetary gear sets then give several fixed ratios, and hydraulic clutches select them.

A CVT changes its ratio continuously. Moving the belt toward the outside of one pulley and the inside of
the other changes the ratio. The engine can stay near its best speed, but the belt has limits on the torque
it carries.

A differential can be open, limited-slip, or locked. A locked differential forces both wheels to turn
together, which gives full traction off road and makes steering harder on dry pavement.

## Key equations

Gear ratio, with $N$ the tooth count and $\omega$ the angular speed in radians per second (rad/s):

$$G = \frac{N_{\mathrm{out}}}{N_{\mathrm{in}}} = \frac{\omega_{\mathrm{in}}}{\omega_{\mathrm{out}}}$$

Output torque and output speed through a gear train with overall ratio $G$ and efficiency $\eta$ (no units),
with input torque $T_{\mathrm{in}}$ in newton metres (N m):

$$T_{\mathrm{out}} = \eta\, G\, T_{\mathrm{in}}, \qquad \omega_{\mathrm{out}} = \frac{\omega_{\mathrm{in}}}{G}$$

Vehicle speed, with tire radius $r$ in metres (m) and the rotational speed of the wheel $\omega_{\mathrm{wheel}}$ in rad/s,
where the total ratio is the gearbox ratio times the final drive ratio:

$$v = \omega_{\mathrm{wheel}}\, r, \qquad \omega_{\mathrm{wheel}} = \frac{\omega_{\mathrm{engine}}}{G_{\mathrm{gearbox}}\, G_{\mathrm{final}}}$$

Open differential, with input torque $T_{\mathrm{in}}$ on the carrier and output torques $T_L$ and $T_R$ on the wheels:

$$T_L = T_R = \frac{T_{\mathrm{in}}}{2}$$

The speed relation is $\omega_L + \omega_R = 2\,\omega_{\mathrm{carrier}}$, where $\omega_L$ and $\omega_R$ are the wheel speeds.

Torque converter stall ratio, the torque multiplication at zero output speed:

$$K_0 = \frac{T_{\mathrm{turbine}}}{T_{\mathrm{pump}}}$$

Typical converters have $K_0$ between about 1.8 and 2.5, and the ratio falls toward 1 as the converter
approaches lock-up (typical values).

## Worked example

**Given:** A car has a manual gearbox with first gear ratio $3.5$ and a final drive ratio of $3.9$. The
engine delivers $T_{\mathrm{engine}} = 150\ \text{N m}$ at $4000\ \text{rpm}$ in first gear. The driveline efficiency
is $\eta = 0.92$, and the tire radius is $r = 0.33\ \text{m}$.

**Find:** (a) the torque at the driven axle, (b) the tire force on the road, and (c) the vehicle speed.

**Solution:**

1. Total ratio: $G = 3.5 \times 3.9 = 13.65$.
2. Axle torque: $T_{\mathrm{axle}} = \eta\, G\, T_{\mathrm{engine}} = 0.92 \times 13.65 \times 150 = 1884\ \text{N m}$.
3. Tire force, total at the two driven wheels: $F = T_{\mathrm{axle}}/r = 1884 / 0.33 = 5708\ \text{N}$.
   With an open differential, each wheel gets half, about $2854\ \text{N}$.
4. Wheel speed: $\omega_{\mathrm{wheel}} = (4000 \times 2\pi/60)/13.65 = 30.7\ \text{rad/s}$, which is $293\ \text{rpm}$.
5. Vehicle speed: $v = 30.7 \times 0.33 = 10.1\ \text{m/s}$, which is $36.5\ \text{km/h}$.

**Answer:** (a) $1884\ \text{N m}$ at the axle. (b) $5.71\ \text{kN}$ total at the two driven wheels. (c) $36.5\ \text{km/h}$ at $4000\ \text{rpm}$ in first gear.

**Sanity check:** Torque rose by $13.65 \times 0.92 = 12.6$ times, and speed fell by $13.65$ times. The product
of torque and speed at the axle is less than the engine's product, because the $0.92$ efficiency removes the
difference as heat. The tire force of $5.7\ \text{kN}$ on a car of about $1500\ \text{kg}$ is roughly $0.39$ times
the weight at $g = 9.81\ \text{m}/\text{s}^2$ (Earth surface), which is a plausible first-gear launch.

## Design trade-offs

- Gear spacing versus engine speed. Close ratios keep the engine near its best power at each step, but
  each extra gear adds cost, weight, and shift points. Manual car gearboxes have typically 5 or 6 forward
  gears, and modern automatics have typically 8 to 10 (typical values).
- Efficiency versus smoothness. A manual gearbox is typically 90 to 95 percent efficient (typical). A
  torque converter gives smooth starts but loses power to slip until it locks up.
- Traction versus steering. An open differential is cheap and gives easy steering, but it loses traction
  when one wheel spins. A limited-slip differential gives traction, but it adds clutches, wear, and some
  handling change in corners.
- Shift quality versus clutch life. Synchronizers and friction elements need firm engagement and must wear
  slowly. Harder engagement shifts faster but wears the parts more.
- Size and weight versus strength. Gears must carry the peak torque of the engine at the lowest gear, which
  often sets the size of the whole box.

## How it fails

- Gear tooth fracture or pitting under shock loads, usually at the lowest gear with a heavy load.
- Differential wear. Spider and side gears wear, and backlash grows. The warning is a clunk on acceleration
  or a whine that rises with speed.
- Synchronizer wear. Grinding on a shift shows the synchronizer cannot match speeds. The gear teeth can
  be damaged if the driver keeps forcing the shift.
- Clutch-pack slip in an automatic. Friction elements wear or overheat, and the fluid darkens and smells burnt.
  The engine speed rises without the car speeding up.
- CVT belt slip or chain wear. The belt can crack or stretch, and high torque causes slip.
- Torque converter overheating. Holding a car on a hill with the brakes off forces the converter to slip
  for a long time, and the fluid overheats.
- Safety measures. A park pawl locks the output in an automatic, an interlock prevents starting in gear,
  and fluid temperature sensors warn the driver before the converter fails.

## History

General Motors introduced the Hydra-Matic fluid automatic transmission in 1939, in Oldsmobile cars.
Hermann Föttinger developed hydrodynamic couplings in Germany in the early twentieth century, and his work
led to the torque converter. The Ford Model T used a planetary transmission in 1908. DAF in the
Netherlands introduced a belt-driven CVT, the Variomatic, in 1958.

## Practice

1. A gear pair has $20$ teeth on the input gear and $50$ on the output gear. The input runs at $3000\ \text{rpm}$
   with $40\ \text{N m}$ of torque. Assume $\eta = 1$. Find the output speed and torque.
2. A car has a direct gear (ratio $1.0$) and a final drive of $4.0$. The engine runs at $3000\ \text{rpm}$,
   and the tire radius is $0.30\ \text{m}$. Find the vehicle speed in km/h.
3. An open differential receives $600\ \text{N m}$ from the ring gear. One wheel on ice can carry only
   $30\ \text{N m}$ through its contact. Find the maximum total torque that reaches the ground.
4. A torque converter has a stall ratio of $K_0 = 2.0$. The pump torque is $200\ \text{N m}$. Find the
   turbine torque at stall.
5. A transmission receives $80\ \text{kW}$ and has an efficiency of $\eta = 0.90$. Find the output power and
   the power lost as heat.

<details><summary>Answers</summary>

1. $G = 50/20 = 2.5$. Output speed $= 3000/2.5 = 1200\ \text{rpm}$. Output torque $= 2.5 \times 40 = 100\ \text{N m}$.
2. $\omega_{\mathrm{engine}} = 3000 \times 2\pi/60 = 314.2\ \text{rad/s}$. $\omega_{\mathrm{wheel}} = 314.2/4.0 = 78.5\ \text{rad/s}$.
   $v = 78.5 \times 0.30 = 23.6\ \text{m/s} = 84.8\ \text{km/h}$.
3. The slipping wheel limits both wheels to $30\ \text{N m}$, because an open differential forces equal torque
   on both sides. The total is $2 \times 30 = 60\ \text{N m}$.
4. $T_{\mathrm{turbine}} = K_0 \times T_{\mathrm{pump}} = 2.0 \times 200 = 400\ \text{N m}$.
5. Output power $= 0.90 \times 80 = 72\ \text{kW}$. Power lost $= 80 - 72 = 8\ \text{kW}$.

</details>

## Common mistakes

- Multiplying the speed when the gear reduces it. A higher ratio lowers the output speed and raises the torque.
- Assuming an open differential sends more torque to the wheel with grip. It sends equal torque to both wheels,
  and the slipping wheel sets the limit.
- Forgetting the final drive. The total ratio is the gearbox ratio times the final drive ratio.
- Leaving out efficiency. Output torque and power fall short of the ideal values by the efficiency factor.
- Treating a CVT as having no torque limit. The belt or chain still sets a maximum torque, and the ratio does
  not change the torque limit.

## Go deeper

- [Design and Manufacturing I, lecture notes](https://ocw.mit.edu/courses/2-007-design-and-manufacturing-i-spring-2009/pages/lecture-notes/)
  by MIT OpenCourseWare: session notes on gear basics, involute teeth, and gear train strength, which underlie
  every ratio in a transmission.
- [Design and Manufacturing I, course page](https://ocw.mit.edu/courses/2-007-design-and-manufacturing-i-spring-2009/)
  by MIT OpenCourseWare: the full course with its lecture and assignment materials.
- Related lessons. [Clutches and brakes](04-clutches-and-brakes.md) for the friction elements that engage gears
  in a transmission, and [Cams and linkages](05-cams-and-linkages.md) for other ways to turn motion into motion.
- [Applications reference](../reference.md): the lookup sheet for this topic.
