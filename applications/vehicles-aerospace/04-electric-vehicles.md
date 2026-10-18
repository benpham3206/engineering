# Electric vehicles: motors, batteries, regenerative braking, and range

**Type:** lesson

An electric vehicle (EV) drives its wheels with one or more electric motors, and a battery pack stores the energy. An engineer who understands an EV can size the motor for a given speed and grade, choose a pack for a target range, and predict how much energy regenerative braking returns. The range estimate works from the same road load that sets the power of any car.

**Prerequisites:** [Cars](02-cars.md), [Electricity and magnetism](../../physics/06-electricity-and-magnetism.md), [Thermodynamics II](../../physics/09-thermo-second-law-cycles.md), [DC motors](../electrical/01-dc-motors.md), [Batteries](../electrical/06-batteries.md)
**Time:** 6-8 h

## Core ideas

### How it works

The battery pack supplies direct current (DC) to an inverter. The inverter switches the current into a three-phase alternating current, and the motor turns that current into torque. The motor shaft drives a single-speed reduction gear, which turns the wheels. Power flows the other way during regenerative braking: the wheels turn the motor as a generator, and the inverter sends current back into the pack.

The motor produces torque from the magnetic force between a magnetic field in the rotor and a rotating field in the stator. A permanent-magnet synchronous motor (PMSM) gives high efficiency over a wide speed range. An induction motor needs no magnets, and it has lower efficiency at light load but is robust and cheap. An EV controller adjusts the frequency and current so the motor produces the requested torque at each speed.

### Main parts

- **Battery pack:** lithium-ion cells in modules, with a battery management system (BMS) that watches each cell's voltage and temperature. A typical passenger EV pack holds 40 to 100 kWh.
- **Inverter:** power transistors that switch the DC pack voltage into a controlled AC waveform. Its efficiency is typically 95 to 98 percent.
- **Traction motor:** converts electric power into torque at the shaft. Its efficiency is typically 90 to 95 percent across most of its range.
- **Single-speed reduction gear:** a fixed gear ratio, often 8:1 to 12:1, that matches the motor's high speed to the wheel's lower speed.
- **Onboard charger and DC fast-charge port:** convert grid AC power to pack DC power. A fast charger supplies DC directly to the pack.
- **Thermal management loop:** pumps coolant through the pack and the motor so that they stay within a safe temperature range.

### Variants

- **Single motor, rear or front drive:** the simplest and lightest layout, and the one most common in mass-market EVs.
- **Dual motor, all-wheel drive:** one motor per axle gives all-wheel drive with no mechanical center differential. The control software splits torque between the axles.
- **Wheel hub motors:** the motor sits inside the wheel. This saves space in the body, but it adds unsprung mass, which hurts ride and handling.
- **Plug-in hybrid electric vehicle (PHEV):** a small battery and a gasoline engine share the drive. Its range on electricity is shorter, and it has a second drive system to maintain.

Motor torque and power follow a standard shape. Torque is roughly constant from zero speed up to a base speed. Above that speed, the motor works at roughly constant power, so the torque falls as the speed rises. Mechanical power is $P = T\omega$, with the torque $T$ in N m and the angular speed $\omega$ in rad/s.

## Key equations

- **Mechanical power at the shaft:** $P = T \, \omega$, in W, with $T$ in N m and $\omega$ in rad/s.
- **Motor speed from road speed:** $\omega_m = (v / r) \, G$, where $v$ is the car speed in m/s, $r$ is the tire radius in m, and $G$ is the reduction gear ratio, dimensionless.
- **Battery power:** $P_{batt} = P_w / \eta_{dt} + P_{aux}$, in W, where $P_w = F_{road} \, v$ is the wheel power, $\eta_{dt}$ is the battery-to-wheel efficiency (the product of inverter, motor, and gear efficiencies), and $P_{aux}$ is the power for heating, lights, and electronics in W.
- **Drivetrain efficiency:** $\eta_{dt} = \eta_{inv} \, \eta_{mot} \, \eta_{gear}$, dimensionless. Typical values are 0.95, 0.92, and 0.98.
- **Road load:** $F_{road} = C_{rr} \, m \, g + \tfrac{1}{2} \rho \, C_d \, A \, v^2$, in N, with rolling resistance from the tire, $m$ the mass in kg, and $g = 9.81\ \text{m/s}^2$. $C_{rr}$ and $C_d$ are dimensionless, $\rho$ is the air density in kg/m$^3$, and $A$ is the frontal area in m$^2$. See [Cars](02-cars.md) for the derivation.
- **Energy per distance:** $e = P_{batt} / v$, in J/m. To express it in Wh/km, divide the value in J/m by 3.6, because $1\ \text{Wh/km} = 3.6\ \text{J/m}$.
- **Range:** $R = E_{use} / e$, in km, where $E_{use}$ is the usable pack energy in Wh. Usable energy is the nominal pack energy times the fraction the BMS allows you to use.
- **Battery C-rate:** $C = I / Q$, dimensionless, where $I$ is the current in A and $Q$ is the rated capacity in Ah. A discharge at 1C empties the pack in one hour.
- **Regenerative energy:** $E_{regen} = \eta_{regen} \, \tfrac{1}{2} m v_0^2$, in J, where $\eta_{regen}$ is the fraction of kinetic energy returned to the pack and $v_0$ is the speed before braking in m/s. Typical values of $\eta_{regen}$ are 0.5 to 0.7 for the brake energy the motor can recover, and the rest goes to friction brakes and losses.

## Worked example

**Given:** A midsize EV with mass $m = 1800\ \text{kg}$, $C_{rr} = 0.010$, $C_d = 0.25$, and frontal area $A = 2.3\ \text{m}^2$. Air density is $\rho = 1.20\ \text{kg/m}^3$. The battery-to-wheel efficiency is $\eta_{dt} = 0.88$, and the auxiliary load is $P_{aux} = 0.5\ \text{kW}$. The usable pack energy is $E_{use} = 75\ \text{kWh}$. The car drives at a steady speed on a level road, with no wind and no regenerative braking included.

**Find:** the energy use per km and the range at 50, 100, and 130 km/h.

**Assumptions:** The values for $C_{rr}$, $C_d$, $A$, and $\eta_{dt}$ are typical for a midsize EV. Real range depends on temperature, cabin heating, wind, and driving style, so this is a steady-speed estimate only.

**Solution at 100 km/h ($v = 27.78\ \text{m/s}$):**

1. Rolling resistance: $F_{rr} = 0.010 \times 1800 \times 9.81 = 176.6\ \text{N}$.
2. Aerodynamic drag: $F_d = 0.5 \times 1.20 \times 0.25 \times 2.3 \times 27.78^2 = 266.2\ \text{N}$.
3. Wheel power: $P_w = (176.6 + 266.2) \times 27.78 = 12.30\ \text{kW}$.
4. Battery power: $P_{batt} = 12.30 / 0.88 + 0.5 = 14.48\ \text{kW}$.
5. Energy per km: at 100 km/h the car covers 100 km in one hour, so $e = 14.48\ \text{kWh}/100\ \text{km} = 144.8\ \text{Wh/km}$.
6. Range: $R = 75\ \text{kWh} / 144.8\ \text{Wh/km} = 518\ \text{km}$.

The same steps at the other speeds give:

| Speed (km/h) | Drag force (N) | Wheel power (kW) | Battery power (kW) | Energy (Wh/km) | Range (km) |
|---|---|---|---|---|---|
| 50 | 67 | 3.38 | 4.34 | 86.7 | 865 |
| 100 | 266 | 12.30 | 14.48 | 144.8 | 518 |
| 130 | 450 | 22.62 | 26.21 | 201.6 | 372 |

**Answer:** At 100 km/h, the car uses 145 Wh/km and reaches about 518 km on 75 kWh. At 50 km/h, the range rises to about 865 km, and at 130 km/h it falls to about 372 km.

**Sanity check:** The energy use at 100 km/h is about 0.145 kWh/km. The drag force at 130 km/h is about 1.7 times the drag at 100 km/h, since drag grows with the square of speed. The auxiliary load matters most at low speed. At 50 km/h, the road load alone gives 977 km of range, and the 0.5 kW auxiliary load cuts that to 865 km, about 11 percent less.

## Design trade-offs

- **Pack size against mass and cost:** a bigger pack gives more range, but it adds mass, and mass raises rolling resistance and brake load. Every 10 kWh of pack adds roughly 60 kg at the cell-to-pack level if the pack holds about 170 Wh/kg.
- **Motor size against efficiency:** a larger motor can cover a higher peak power, but it runs less efficiently at light load. Engineers pick the motor size from the highest load the car must handle, such as a fast highway merge or a long grade.
- **Charging speed against battery life:** fast charging at high C-rates heats the cells and speeds up aging. A charging curve that tapers near full charge protects the pack.
- **Regeneration against brake feel:** strong regeneration recovers more energy, but it can make the pedal feel different from a conventional brake. Blending the friction brake with the motor keeps the pedal consistent.
- **Cold weather against range:** lithium-ion cells lose power at low temperatures, and heating the cabin draws energy from the pack. A heat pump uses less energy for heating, and it is a common cold-weather choice.

## How it fails

- **Thermal runaway:** an internal short, physical damage, or overcharging can trigger an uncontrolled rise in cell temperature. The BMS limits voltage and current and monitors temperature, and the pack has fire barriers and vents.
- **Cell imbalance:** cells age at different rates, and the weakest cell limits the whole pack. The BMS balances cell voltages to keep the pack usable.
- **Insulation faults:** a damaged high-voltage cable or connector can leak current. Interlocks and insulation monitors cut power when they detect a fault.
- **Overheated motor or inverter:** repeated hill climbs or towing can raise temperatures beyond limits. The controller reduces power to protect the parts, and the driver sees a warning light.
- **Capacity fade:** the usable energy falls over years and many charge cycles. Warning signs are a shorter range and a lower state-of-health reading from the BMS.

## History

Ferdinand Porsche showed a car with electric hub motors in the wheels at the 1900 Paris Exposition, and it was built by the Lohner company in Vienna. Electric cars were common in cities in the early 1900s. Gasoline cars took most of the market by the 1920s, helped by longer range and the electric starter. Toyota launched the Prius hybrid in Japan in 1997, which brought electric drive to mass production. The Tesla Roadster (2008) and the Nissan Leaf (2010) showed that a battery EV could sell in volume with modern lithium-ion cells.

## Practice

1. A 150 kW motor turns at 6000 rpm. Find its torque in N m at that speed.
2. A 60 kWh pack supplies 30 kW to the motor. Find the C-rate and the time to empty the pack at that power, ignoring losses.
3. A 1800 kg car slows from 25 m/s to rest. The regenerative system returns 60 percent of the kinetic energy to the pack. Find the energy returned in kWh.
4. A pack holds 75 kWh and has a pack-level energy density of 180 Wh/kg. Find the pack mass in kg.
5. A drivetrain has a motor efficiency of 0.92, an inverter efficiency of 0.97, and a gear efficiency of 0.98. Find the overall drivetrain efficiency.

<details><summary>Answers</summary>

1. $239\ \text{N m}$, from $T = P / \omega = 150000 / (6000 \times 2\pi / 60) = 239\ \text{N m}$.
2. $C = 0.5\ \text{C}$, and the time is $2.0\ \text{h}$, from $60\ \text{kWh} / 30\ \text{kW} = 2.0\ \text{h}$.
3. $0.094\ \text{kWh}$, from $E = 0.6 \times \tfrac{1}{2} \times 1800 \times 25^2 = 337.5\ \text{kJ}$, which is $0.094\ \text{kWh}$.
4. $417\ \text{kg}$, from $75000\ \text{Wh} / 180\ \text{Wh/kg} = 417\ \text{kg}$.
5. $0.875$, from $0.92 \times 0.97 \times 0.98 = 0.875$.

</details>

## Common mistakes

- Using the nominal pack energy in the range formula. Range uses the usable energy, which is lower because the BMS keeps a reserve.
- Adding regenerative braking to a steady-speed range estimate. Regeneration helps in stop-and-go driving, and it does nothing on a steady highway cruise.
- Forgetting the auxiliary load. At low speed it can be a large share of the total power draw.
- Confusing kWh and kW. Energy is in kWh, and power is in kW. A 75 kWh pack at 15 kW lasts 5 h at constant draw, not 5 kWh.
- Treating efficiency numbers as additive. The drivetrain efficiency is the product of the stage efficiencies. Three stages at 0.95 give 0.86, not 0.95.

## Go deeper

- [Electric vehicles, U.S. Department of Energy](https://www.fueleconomy.gov/feg/evtech.shtml) by the U.S. Department of Energy: how battery electric vehicles work, with their advantages and drawbacks.
- [Where the energy goes in a gasoline car](https://www.fueleconomy.gov/feg/atv.shtml) by the U.S. Department of Energy: energy losses in conventional cars across driving cycles, for comparison with EVs.
- Related lessons: [Batteries](../electrical/06-batteries.md), [Brushless and stepper motors](../electrical/02-brushless-and-stepper-motors.md), [Induction motors](../electrical/03-induction-motors.md), [Suspension and steering](03-suspension-and-steering.md), [Internal combustion engines](../thermal-fluid/06-internal-combustion-engines.md).
