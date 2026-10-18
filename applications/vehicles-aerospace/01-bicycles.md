# Bicycles

**Type:** lesson

A bicycle turns the rider's leg power into speed through a chain, gears, and two wheels. Engineers use the same physics to size gears, estimate how much power a rider needs on a hill, and design a frame that steers stably.

**Prerequisites:** [Particle dynamics and energy](../../physics/02-particle-dynamics.md), [Rigid body dynamics](../../physics/03-rigid-body-dynamics.md), [Trigonometry](../../math/02-trigonometry.md)
**Time:** 4-6 h

## Core ideas

### How it works

The rider pushes the pedals, which turn the crank. The chainring pulls the chain, and the chain turns the rear cog. The rear wheel turns, and friction between the tyre and the road pushes the bicycle forward. Without that friction at the contact patch, the wheel would spin in place.

Two numbers set the gear: the ratio of chainring teeth to cog teeth, and the wheel radius. A large chainring or a small cog gives a harder gear. Each pedal turn then moves the bicycle farther, but the rider must push harder.

At steady speed, the rider's power balances three resistances. Rolling resistance comes from the tyre deforming on the road. Air drag comes from pushing air aside. A grade adds a force that pulls the bicycle back. Air drag grows with the square of speed, so it dominates at high speed. Power to overcome it grows with the cube of speed.

Steering depends on the geometry of the fork. Trail is the distance along the ground between the tyre's contact point and the point where the steering axis meets the ground. Positive trail makes the front wheel follow the frame and return to straight when the rider lets go, which is why a rider can ride without hands at speed.

### Main parts

- **Frame:** the front and rear triangles carry the loads. Common materials are steel, aluminium, and carbon fibre.
- **Fork and head tube:** the fork carries the front wheel. The head tube holds the bearings that set the steering axis.
- **Crank, chainring, and pedals:** the crank converts the rider's force into a torque at the chainring.
- **Chain and cassette:** the chain carries the torque to the rear wheel. The cassette is the set of cogs on the rear hub.
- **Derailleurs:** these move the chain from one sprocket to another.
- **Brakes:** rim brakes and disc brakes convert the bicycle's kinetic energy into heat at the rim or the disc.
- **Wheels, hubs, spokes, and tyres:** the hub holds the bearings, the spokes carry tension, and the tyre holds the air pressure that sets its rolling resistance.
- **Saddle, seatpost, and handlebars:** these set the rider's position, which affects comfort, power, and drag.

### Variants

- **Road bike:** light frame, narrow tyres, and drop handlebars. It aims at low rolling resistance and low drag.
- **Mountain bike:** wide, knobby tyres and a strong frame for rough ground. Many have suspension.
- **City or hybrid bike:** upright posture, fenders, and a rack. It favours comfort and simple maintenance over speed.
- **Track bike:** a fixed gear with no freewheel, and often no brakes. Its gear ratio stays the same at every moment.
- **Recumbent:** the rider sits low with the legs in front. The lower frontal area reduces drag, but the bike is heavier and harder to see in traffic.
- **Electric bicycle:** a motor adds power to the rider's pedalling. The same equations for resistance and gearing apply.

## Key equations

The gear ratio compares the number of teeth on the chainring and the cog. $N$ is a tooth count, so $G$ is dimensionless:

$$G = \frac{N_{ring}}{N_{cog}}$$

The crank turns at a cadence measured in revolutions per minute. The crank angular speed in radians per second, and the wheel angular speed, are:

$$\omega_c = \frac{2\pi\,\text{cadence}}{60}, \qquad \omega_w = \omega_c G$$

The bicycle speed in metres per second, with wheel radius $r$ in metres, is:

$$v = \omega_w r$$

Rolling resistance is a force in newtons. Here $C_{rr}$ is the dimensionless rolling resistance coefficient, about 0.004 for a road tyre on smooth asphalt (typical), $m$ is the total mass of rider and bicycle in kilograms, and $g = 9.81\ \text{m/s}^2$:

$$F_{rr} = C_{rr}\, m\, g$$

Air drag in newtons depends on the air density $\rho_a$ in kilograms per cubic metre, the speed $v$ in metres per second, and $C_dA$, the drag coefficient times the frontal area in square metres. A typical road position has $C_dA$ near $0.35\ \text{m}^2$:

$$F_d = \tfrac{1}{2}\rho_a C_d A\, v^2$$

On a grade of angle $\theta$, the gravity force along the slope in newtons is:

$$F_g = m g \sin\theta$$

The power the rider delivers at the wheel, in watts, is the total resistance force times the speed. The input power at the pedals is larger because the drivetrain loses some energy. Here $\eta$ is the drivetrain efficiency, which is about 0.97 for a clean chain (typical):

$$P_{wheel} = (F_{rr} + F_d + F_g)\, v, \qquad P_{in} = \frac{P_{wheel}}{\eta}$$

## Worked example

**Given:** The rider pedals at 90 rpm, the chainring has 50 teeth, and the cog has 11 teeth. The wheel radius is $r = 0.335\ \text{m}$. The total mass is $m = 85\ \text{kg}$, with $C_{rr} = 0.004$, $\rho_a = 1.2\ \text{kg/m}^3$, and $C_dA = 0.35\ \text{m}^2$. The drivetrain efficiency is $\eta = 0.97$.

**Find:** the speed at 90 rpm, the rider power needed at 10 m/s on a flat road, and the rider power needed at 5 m/s up a 5 percent grade.

**Solution:**

Speed:

1. Crank speed: $\omega_c = 2\pi(90)/60 = 9.42\ \text{rad/s}$.
2. Gear ratio: $G = 50/11 = 4.55$.
3. Wheel speed: $\omega_w = 9.42 \times 4.55 = 42.84\ \text{rad/s}$.
4. Speed: $v = 42.84 \times 0.335 = 14.35\ \text{m/s}$, which is $51.7\ \text{km/h}$.

Flat road at 10 m/s:

5. Rolling resistance: $F_{rr} = 0.004 \times 85 \times 9.81 = 3.34\ \text{N}$.
6. Air drag: $F_d = \tfrac{1}{2}(1.2)(0.35)(10)^2 = 21.0\ \text{N}$.
7. Wheel power: $P = (3.34 + 21.0)(10) = 243\ \text{W}$. Input power: $243/0.97 = 251\ \text{W}$.

Grade at 5 m/s:

8. The 5 percent grade gives $\tan\theta = 0.05$, so $\sin\theta = 0.0499$. Gravity force: $F_g = 85 \times 9.81 \times 0.0499 = 41.6\ \text{N}$.
9. Resistance at 5 m/s: $F_{rr} = 3.34\ \text{N}$ and $F_d = \tfrac{1}{2}(1.2)(0.35)(5)^2 = 5.25\ \text{N}$.
10. Wheel power: $P = (41.6 + 3.34 + 5.25)(5) = 251\ \text{W}$. Input power: $251/0.97 = 259\ \text{W}$.

**Answer:** The speed is $14.4\ \text{m/s}$, or $51.7\ \text{km/h}$. On a flat road at $10\ \text{m/s}$, the rider supplies $243\ \text{W}$ at the wheel and $251\ \text{W}$ at the pedals. Climbing a 5 percent grade at $5\ \text{m/s}$ needs $251\ \text{W}$ at the wheel and $259\ \text{W}$ at the pedals.

**Sanity check:** Climbing at half the speed takes about the same power as riding twice as fast on the flat, which shows why grades cost so much. The flat-road drag at $10\ \text{m/s}$ is six times the rolling resistance, so air drag dominates at speed, as the theory predicts.

## Design trade-offs

- **Weight against stiffness:** steel is durable but heavy. Aluminium and carbon fibre are lighter and can be made stiff, but they cost more and can crack under impact.
- **Gear range against complexity:** a wide range needs more sprockets and more derailleur travel. Cross-chaining, which runs the chain on a large ring and a large cog, wears the chain and adds friction.
- **Tyre width and pressure:** on smooth roads, narrow tyres at high pressure roll with less resistance. Wider tyres grip better and absorb bumps, which lowers the rider's fatigue on rough ground.
- **Aerodynamics against comfort:** a low tuck cuts drag and raises power efficiency, but it limits breathing and visibility, and it strains the back and neck.
- **Stability against agility:** a longer wheelbase and more trail steer more stably at speed. A shorter wheelbase turns more quickly at low speed.
- **Brake type:** rim brakes heat the rim, which can overheat on a long descent. Disc brakes cope with heat better and work in the wet.

## How it fails

- **Chain drop or chain breakage:** a worn chain or worn sprockets let the chain skip off. Warning signs include skipping under load and a chain that is stretched.
- **Spoke fatigue or loosening:** a loose spoke makes the wheel go out of true. Warning signs include a tick or a wobble that changes with the speed.
- **Frame cracks:** repeated bending fatigues welds and joints, especially at the bottom bracket and the head tube. Warning signs include creaks and hairline cracks around joints.
- **Brake fade:** long descents heat the brake pads and rims. The lever travels farther before the brakes bite.
- **Tyre failure:** low pressure leads to pinch flats, where the tube is caught between the rim and an impact. Debris causes punctures, and a worn sidewall can bulge and burst.
- **Handlebar or seatpost slip:** a clamp that is not tightened to its torque slips under load. Torque checks before a ride catch it.

Bicycle standards set safety requirements for brakes, frame strength, and fasteners. Regular checks of brakes, tyres, and bolts catch most failures early.

## History

Karl Drais built the draisine in Mannheim in 1817. It had two wheels and a steering handlebar, but no pedals, and the rider pushed it along with the feet. In the 1860s, Pierre Michaux and his sons in Paris added pedals and cranks to the front wheel. Large-front-wheel machines, often called high-wheelers, were popular in the 1870s and 1880s. John Kemp Starley's Rover safety bicycle of 1885 used a chain drive to the rear wheel and two wheels of equal size. In 1888, John Boyd Dunlop developed a practical pneumatic tyre in Belfast, which made rides far more comfortable on rough roads.

## Practice

1. A chainring has 52 teeth and the cog has 13 teeth. Find the gear ratio.
2. The rider pedals at 80 rpm in a 50/16 gear, and the wheel radius is 0.335 m. Find the speed.
3. An 80 kg rider on a bicycle with $C_{rr} = 0.005$ and $C_dA = 0.40\ \text{m}^2$ rides on the flat at 8 m/s. Find the wheel power and the input power, with $\eta = 0.97$ and $\rho_a = 1.2\ \text{kg/m}^3$.
4. How much average power does an 80 kg rider need to climb 300 m vertically in one hour, ignoring drag and drivetrain losses?
5. At what cadence in a 50/11 gear does the rider reach $14.35\ \text{m/s}$ with a 0.335 m wheel radius?

<details><summary>Answers</summary>

1. $G = 52/13 = 4.0$.
2. $\omega_c = 2\pi(80)/60 = 8.38\ \text{rad/s}$, $\omega_w = 8.38 \times 50/16 = 26.2\ \text{rad/s}$, and $v = 26.2 \times 0.335 = 8.77\ \text{m/s}$.
3. $F_{rr} = 0.005 \times 80 \times 9.81 = 3.92\ \text{N}$ and $F_d = \tfrac{1}{2}(1.2)(0.40)(8)^2 = 15.4\ \text{N}$. The wheel power is $(3.92 + 15.4)(8) = 154\ \text{W}$, and the input power is $154/0.97 = 159\ \text{W}$.
4. The energy is $mgh = 80 \times 9.81 \times 300 = 2.35 \times 10^5\ \text{J}$. Over 3600 s, the average power is $65.4\ \text{W}$.
5. $\omega_w = 14.35/0.335 = 42.8\ \text{rad/s}$, $\omega_c = 42.8 \times 11/50 = 9.42\ \text{rad/s}$, and the cadence is $9.42 \times 60/(2\pi) = 90\ \text{rpm}$.

</details>

## Common mistakes

- **Reading the gear ratio upside down.** A bigger chainring or a smaller cog makes a harder gear. Check the ratio against the number of teeth before using it.
- **Treating air drag as linear.** Air drag grows with the square of speed, so doubling the speed quadruples the drag force and multiplies the drag power by eight.
- **Leaving out drivetrain losses.** The rider's pedal power is larger than the power at the wheel. Divide by $\eta$ to get the input.
- **Using rim diameter as the wheel radius.** The speed equation needs the radius to the road, which includes the tyre.
- **Forgetting grades and wind.** A flat-road estimate misses the extra power that a hill or a headwind demands.

## Go deeper

- [OpenStax University Physics Volume 1, chapter 6, applications of Newton's laws](https://openstax.org/books/university-physics-volume-1/pages/6-introduction): friction, drag, and terminal speed.
- [OpenStax University Physics Volume 1, chapter 7, work, energy, and power](https://openstax.org/books/university-physics-volume-1/pages/7-introduction): the work-energy theorem and power.
- [OpenStax University Physics Volume 1, chapter 10, rotational motion](https://openstax.org/books/university-physics-volume-1/pages/10-introduction): angular speed and moment of inertia for wheels and cranks.
- [Gear trains](../power-transmission/01-gear-trains.md): tooth ratios and efficiency.
- [Belts and chains](../power-transmission/03-belts-and-chains.md): chain tension, wrap, and speed ratio.
- [Clutches and brakes](../power-transmission/04-clutches-and-brakes.md): brake heat and torque capacity.
- [Cars](02-cars.md): the same resistance and power equations applied to a road vehicle.
