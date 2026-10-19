# Cars: drivetrain, road load, and braking

**Type:** lesson

A car turns stored energy into motion, and the tires push on the road to move it. Engineers size the engine, the gearbox, and the brakes from one balance: the force at the tires must match the resistance the car meets. This lesson covers the drivetrain layout, the road load that the car must overcome, and the braking distance that friction allows.

**Prerequisites:** [Statics](../../physics/01-statics.md), [Particle dynamics](../../physics/02-particle-dynamics.md), [Rigid body dynamics](../../physics/03-rigid-body-dynamics.md), [Hydrostatics and Bernoulli](../../physics/10-hydrostatics-and-bernoulli.md), [Trigonometry](../../math/02-trigonometry.md)
**Time:** 6-8 h

## Core ideas

### How it works

The engine makes torque at its crankshaft. The gearbox multiplies that torque and changes the speed. A driveshaft or pair of half-shafts carries the torque to the wheels. At each tire, the torque turns the wheel, and friction at the contact patch pushes the road backward. The road pushes the tire forward with the same force, and that force moves the car.

Three forces act on a car moving at steady speed on a level road. The tires supply a forward force, and rolling resistance and aerodynamic drag oppose it. When the tire force equals the sum of the two resistances, the speed stays constant. Any extra force goes into acceleration.

### Main parts

- **Engine or motor:** makes the torque. A gasoline engine has a narrow band of good efficiency, so its gearbox keeps it near that band.
- **Clutch or torque converter:** connects and disconnects the engine from the gearbox, so the car can start from rest.
- **Gearbox:** holds several gear ratios. A low ratio gives high wheel torque for starting. A high ratio gives a lower engine speed at highway speed.
- **Differential:** splits the torque between the two driven wheels and lets them turn at different speeds in a corner. See [Differentials and transmissions](../power-transmission/06-differentials-and-transmissions.md).
- **Half-shafts and driveshaft:** carry torque from the differential to the wheels, and from the gearbox to the differential in rear-drive cars.
- **Brakes:** friction pads or shoes press on a disc or drum and turn kinetic energy into heat.

### Variants

- **Front-wheel drive:** the engine, gearbox, and driven wheels sit at the front. It packs well into a small car and saves weight, but the front tires must steer and drive at the same time.
- **Rear-wheel drive:** the driven wheels sit at the back. Its weight split is closer to even, and steering and driving are separate jobs. It needs a driveshaft tunnel through the cabin floor.
- **All-wheel drive:** a center differential or a clutch splits torque front to rear. It adds grip in rain and snow, at the cost of weight and drag losses.
- **Mid-engine:** the engine sits behind the cabin and ahead of the rear axle. This gives a centered mass, which helps handling in sports cars.

## Key equations

The equations below assume steady speed unless an equation includes acceleration. Tires roll without slip at the contact patch. Rolling resistance and drag coefficients stay constant over the speed range. Air is uniform with no wind. Braking uses one constant friction coefficient, and the stopping distance ignores reaction time.

- **Wheel speed:** $\omega_w = v / r$, where $\omega_w$ is the wheel angular speed in radians per second, $v$ is the car speed in m/s, and $r$ is the loaded tire radius in m.
- **Engine speed:** $\omega_e = \omega_w \, G$, where $G$ is the overall ratio (gearbox times final drive), dimensionless.
- **Wheel torque:** $T_w = F_{tire} \, r$, where $T_w$ is in N m and $F_{tire}$ is the tire force in N.
- **Engine torque:** $T_e = T_w / (G \, \eta_{dt})$, where $\eta_{dt}$ is the drivetrain efficiency, typically 0.90 to 0.95 for a manual or automatic gearbox with a final drive.
- **Power:** $P = T \, \omega$, in W, with torque in N m and angular speed in rad/s. At the wheels, $P_w = F_{road} \, v$.
- **Rolling resistance:** $F_{rr} = C_{rr} \, m \, g$, where $C_{rr}$ is the rolling resistance coefficient (dimensionless, typically 0.008 to 0.012 on asphalt), $m$ is mass in kg, and $g$ is the local gravitational acceleration (9.81 m/s$^2$ at Earth's surface).
- **Aerodynamic drag:** $F_d = \tfrac{1}{2} \rho \, C_d \, A \, v^2$, where $\rho$ is the air density in kg/m$^3$ (typically 1.20 at 20 C at sea level), $C_d$ is the drag coefficient (dimensionless, typically 0.25 to 0.35 for production cars), and $A$ is the frontal area in m$^2$.
- **Road grade:** $F_g = m \, g \sin\theta$, where $\theta$ is the road angle. A 6 percent grade means $\tan\theta = 0.06$.
- **Total road load:** $F_{road} = F_{rr} + F_d + F_g + m a$, where $a$ is the acceleration in m/s$^2$.
- **Braking deceleration limit:** $a_{max} = \mu g$, where $\mu$ is the tire-road friction coefficient (dimensionless, about 0.8 to 1.0 on dry asphalt).
- **Stopping distance:** $d = v^2 / (2 \mu g)$, in m, with the speed $v$ in m/s. This ignores the driver's reaction time.
- **Braking weight transfer:** $\Delta N = m \, a \, h / L$, where $\Delta N$ is the load moved to the front axle in N, $h$ is the height of the center of mass in m, and $L$ is the wheelbase in m.

## Worked example

**Given:** A 1500 kg car with $C_{rr} = 0.012$, $C_d = 0.30$, $A = 2.2\ \text{m}^2$, and $\rho = 1.20\ \text{kg/m}^3$. The tire radius is $r = 0.33\ \text{m}$. The overall ratio is $G = 3.5$, and the drivetrain efficiency is $\eta_{dt} = 0.92$. The car cruises at 100 km/h, which is $v = 27.78\ \text{m/s}$, on a level road with no wind. Gravity is $g = 9.81\ \text{m/s}^2$ (Earth surface).

**Find:** (a) the road load force, (b) the wheel power, (c) the engine speed and engine torque, and (d) the braking distance from 100 km/h with $\mu = 0.9$.

**Solution:**

1. Rolling resistance: $F_{rr} = 0.012 \times 1500 \times 9.81 = 176.6\ \text{N}$.
2. Aerodynamic drag: $F_d = 0.5 \times 1.20 \times 0.30 \times 2.2 \times 27.78^2 = 305.6\ \text{N}$.
3. Road load: $F_{road} = 176.6 + 305.6 = 482.1\ \text{N}$.
4. Wheel power: $P_w = 482.1 \times 27.78 = 13.39\ \text{kW}$.
5. Engine power: $P_e = 13.39 / 0.92 = 14.6\ \text{kW}$.
6. Wheel speed: $\omega_w = 27.78 / 0.33 = 84.2\ \text{rad/s}$, which is 804 rpm.
7. Engine speed: $\omega_e = 84.2 \times 3.5 = 294.6\ \text{rad/s}$, which is 2813 rpm.
8. Wheel torque: $T_w = 482.1 \times 0.33 = 159.1\ \text{N m}$.
9. Engine torque: $T_e = 159.1 / (3.5 \times 0.92) = 49.4\ \text{N m}$. Check: $49.4 \times 294.6 = 14.6\ \text{kW}$.
10. Braking distance: $d = 27.78^2 / (2 \times 0.9 \times 9.81) = 43.7\ \text{m}$.

**Answer:** (a) 482 N. (b) 13.4 kW at the wheels. (c) Engine speed 2813 rpm and engine torque 49.4 N m, with 14.6 kW at the crankshaft. (d) 43.7 m.

**Sanity check:** The engine power is larger than the wheel power, as efficiency requires, and the power check of step 9 matches step 5. The wheel torque equals the tire force times the radius, $482 \times 0.33 = 159\ \text{N m}$. The stopping distance is the friction-limited value only, so a real stop from 100 km/h is longer by the reaction distance.

## Design trade-offs

- **Drag against interior space:** a lower drag coefficient often needs a longer, lower body. At highway speed, drag can exceed rolling resistance by a wide margin, as the worked example shows (306 N against 177 N at 100 km/h). Drag grows with the square of speed, so the effect is small at 30 km/h and large at 130 km/h.
- **Mass against safety:** heavier cars need larger brakes and tires, but they carry crash loads better. Each 100 kg adds about 12 N of rolling resistance on a flat road with $C_{rr} = 0.012$.
- **Gearing against efficiency and drivability:** more gears let the engine run near its best efficiency band. Each added gear adds parts, weight, and friction losses.
- **Tire grip against rolling resistance:** a softer tread grips more but rolls with more loss. Low rolling resistance tires can cost some wet grip.
- **Brake size against heat:** a brake must absorb the kinetic energy of a stop. Repeated stops on a long downhill raise disc temperature, which lowers friction.

## How it fails

- **Brake fade:** the pads or the disc overheat, and the friction coefficient drops. Warning signs are a soft pedal and longer stops after repeated hard braking. Ventilated discs, larger pads, and brake fluid with a high boiling point reduce the risk.
- **Loss of traction:** a wet or icy surface drops $\mu$ well below 0.8, so stopping distances grow. Anti-lock braking systems (ABS) keep each wheel near the peak friction point, so the driver keeps steering control during a hard stop.
- **Tire failure:** underinflation raises heat and can cause a tread separation. Tire pressure monitoring and the correct load rating prevent most of these failures.
- **Driveline wear:** worn CV joints, universal joints, or differential gears make clunks and vibrations. These parts see high torque at large steering angles.
- **Overheating:** a blocked radiator or failed water pump raises coolant temperature. Temperature gauges and warning lights give the first warning.

### Controlling brake failure risk

Brake failure is controlled by the hierarchy of controls, from the most effective to the least. Elimination removes the hazard, for example by avoiding a need for high-speed stops. Substitution replaces a weak part with a better one, such as a brake fluid with a higher boiling point. Engineering controls sit inside the car, and they include dual-circuit hydraulics, ABS, and a parking brake that acts on a separate mechanism. Administrative controls are maintenance intervals, inspection checklists, and driver training. Personal protective equipment is the last layer, and mechanics wear eye protection and gloves when they service brakes.

Servicing a brake system uses lockout and tagout. Isolate every energy source by stopping the engine and removing the key. Release or restrain stored energy by chocking the wheels and releasing the parking brake only after the car is supported. In a conventional hydraulic system, the fluid holds pressure only while the pedal or the booster is loaded, so keep the pedal released while bleeding. Verify a zero-energy state by checking that the car is held on the stands, that the stands are on firm ground, and that the wheels cannot roll, before anyone works under the car.

## History

Karl Benz built a three-wheeled Motorwagen in Mannheim, Germany, and received a German patent for it in 1886. Gottlieb Daimler and Wilhelm Maybach developed a fast, lightweight engine in Cannstatt about the same time. Henry Ford introduced the Model T in 1908, and his Highland Park plant began a moving assembly line in 1913. The line cut the time to build a car and made the car affordable for many families.

## Practice

Where a problem needs gravitational acceleration, use $g = 9.81\ \text{m/s}^2$ (Earth surface).

1. A car has a wheel radius of 0.30 m and travels at 20 m/s. Find the wheel speed in rpm.
2. A 1200 kg car rolls on asphalt with $C_{rr} = 0.010$ on a level road. Find the rolling resistance force in N.
3. A car at 30 m/s has $C_d = 0.28$ and frontal area $A = 2.0\ \text{m}^2$. Find the aerodynamic drag force in N, using $\rho = 1.20\ \text{kg/m}^3$.
4. A car brakes from 25 m/s on a wet road with $\mu = 0.7$. Find the stopping distance in m, ignoring reaction time.
5. A 1500 kg car climbs a 6 percent grade at constant speed, so $\tan\theta = 0.06$. Find the grade force in N.

<details><summary>Answers</summary>

1. $637$ rpm, from $20 / 0.30 = 66.7\ \text{rad/s}$, which is $66.7 \times 60 / (2\pi) = 637$ rpm.
2. $118\ \text{N}$, from $0.010 \times 1200 \times 9.81 = 117.7\ \text{N}$.
3. $302\ \text{N}$, from $0.5 \times 1.20 \times 0.28 \times 2.0 \times 30^2 = 302.4\ \text{N}$.
4. $45.5\ \text{m}$, from $25^2 / (2 \times 0.7 \times 9.81) = 45.5\ \text{m}$.
5. $881\ \text{N}$, from $\theta = \arctan(0.06) = 3.43^\circ$, so $1500 \times 9.81 \times \sin(3.43^\circ) = 881\ \text{N}$.

</details>

## Common mistakes

- Using the wheel radius in the engine speed calculation without the overall ratio. Engine speed is wheel speed times $G$, not wheel speed alone.
- Treating $C_d$ as the drag force. Drag is $\tfrac{1}{2}\rho C_d A v^2$, and $C_d$ alone has no force units.
- Forgetting that drag grows with the square of speed. Doubling the speed raises drag by four times and raises drag power by eight times.
- Using a stopping distance formula that omits the driver's reaction time. Real stops add the distance covered during reaction. At 100 km/h, a one-second reaction adds $27.78\ \text{m/s} \times 1\ \text{s} = 27.8\ \text{m}$.
- Ignoring weight transfer when sizing brakes. Under hard braking the front axle carries more load, so the front brakes do most of the work.

## Go deeper

- [Where the energy goes in a gasoline car](https://www.fueleconomy.gov/feg/atv.shtml) by the U.S. Department of Energy: where energy is lost in conventional cars across driving cycles.
- [University Physics Volume 1, Chapter 5 (Newton's laws of motion)](https://openstax.org/books/university-physics-volume-1/pages/5-introduction) by OpenStax: forces, free-body diagrams, and the basis for the road load balance.
- Reference sheets: [Mechanics reference](../../physics/reference-mechanics.md) for the force and power relations, and [Design reference](../../design/reference.md) for the design vocabulary used in the trade-offs.
- Related lessons: [Differentials and transmissions](../power-transmission/06-differentials-and-transmissions.md), [Internal combustion engines](../thermal-fluid/06-internal-combustion-engines.md), [Suspension and steering](03-suspension-and-steering.md), [Electric vehicles](04-electric-vehicles.md).
