# Hydraulics and pneumatics

**Type:** lesson

Hydraulic and pneumatic systems are ways of moving loads with pressurized liquid or gas sent through pumps, valves, and cylinders. An engineer who designs or services one must size the cylinder for force and the valves for speed, because stored energy and high-pressure jets make these systems dangerous.

**Prerequisites:** [Hydrostatics and Bernoulli](../../physics/10-hydrostatics-and-bernoulli.md), [Control volumes and pipe flow](../../physics/11-control-volumes-pipe-flow.md), [Fluid systems](../thermal-fluid/02-fluid-systems.md)
**Time:** 8-12 h

## Core ideas

- **Pascal's law**: pressure applied to a confined fluid acts equally in every direction and
  reaches every wall. A small piston pushing on oil creates a pressure that acts on a large piston.
- **Pressure** $p$ (pascals, Pa): force per unit area. The formulas here use gauge pressure, which
  is measured above atmospheric pressure.
- **Flow** $Q$ (m$^3$/s): volume of fluid delivered per second. Shop practice uses litres per minute.
  One litre per minute is $1.667 \times 10^{-5}$ m$^3$/s.
- **Force sets pressure, flow sets speed.** A cylinder's force depends on pressure and piston area.
  Its speed depends on flow and piston area. Friction and leakage change both.
- **Stored energy.** Oil under pressure, a held load, and a charged accumulator each store energy
  that is released when a hose, seal, or valve fails.
- **Pneumatics** uses compressed air instead of oil. Air is compressible, so a pneumatic cylinder
  moves in a less controlled way and is less stiff. It is cheap, clean, and fast for light tasks such
  as clamping and sorting.

## How it works

1. A pump draws oil from a reservoir and pushes it into the supply line. An electric motor or an
   engine drives the pump.
2. A relief valve opens to the tank when the pressure reaches its setting. This limits the pressure
   the system can build.
3. A directional control valve routes the oil to one side of the piston. The oil on the other side
   flows back to the reservoir.
4. The pressure acts on the piston and produces force. The oil flow fills the volume behind the
   piston and sets how fast it moves.
5. A flow control valve restricts the flow to slow the cylinder. The energy the restriction removes
   from the flow becomes heat in the oil.

A pneumatic system follows the same path, with a compressor and receiver tank in place of the pump
and reservoir. The exhaust air goes to the atmosphere instead of back to a tank.

## Main parts

- Reservoir: holds the oil, lets it cool, and lets air and debris settle out.
- Pump: converts shaft power into fluid flow and pressure. Gear, vane, and axial piston pumps are the
  common types.
- Relief valve: a spring-loaded valve that protects the system from overpressure.
- Directional control valve: a spool or poppet that routes flow to each port. It sets the direction
  of motion.
- Flow control valve: a variable restriction that sets the speed of a cylinder.
- Cylinder: a barrel, piston, and rod. It turns fluid pressure into a linear force.
- Accumulator: a gas-charged vessel that stores pressurized oil and smooths the pressure.
- Filter: removes particles that wear valves and seals.
- Hoses, pipes, and fittings: carry the fluid. Their pressure rating sets the safe limit.

## Variants

- Single-acting cylinders push in one direction. A spring or the load returns the piston.
- Double-acting cylinders push and pull. Most industrial and mobile machines use them.
- Gear pumps are cheap and simple but limited to low pressure. Axial piston pumps reach high pressure
  and can vary their displacement.
- Industrial hydraulic systems often run at about 10 to 21 MPa. Mobile machines such as excavators
  often run at about 20 to 35 MPa (typical values).
- Pneumatic supply pressure is commonly about 0.6 to 0.8 MPa (typical), far below hydraulic levels.

## Key equations

Assumptions for the equations below: the oil is incompressible except where the bulk modulus
appears, the flow is steady, friction and leakage are zero unless a line says otherwise, and the
pressures are gauge pressures.

Pressure and force, with $p$ in pascals (Pa), $F$ in newtons (N), and $A$ the piston area in square
metres (m$^2$):

$$p = \frac{F}{A}$$

Piston area for a cylinder bore of diameter $D$ in metres (m):

$$A = \frac{\pi D^2}{4}$$

Annulus area on the rod side, with rod diameter $d$ in metres:

$$A_a = \frac{\pi \left(D^2 - d^2\right)}{4}$$

Cylinder force on the bore side (friction ignored):

$$F_{\text{extend}} = p\,A \qquad F_{\text{retract}} = p\,A_a$$

Cylinder speed, with $v$ in metres per second (m/s) and $Q$ in cubic metres per second (m$^3$/s):

$$v = \frac{Q}{A} \qquad\text{or}\qquad v = \frac{Q}{A_a} \text{ on the retract stroke}$$

Hydraulic power, with $P$ in watts (W):

$$P_{\text{hyd}} = p\,Q$$

Pump input power for pump efficiency $\eta$, a dimensionless number between 0 and 1:

$$P_{\text{in}} = \frac{p\,Q}{\eta}$$

Ideal jet speed from a small leak, assuming no friction and no losses at the orifice (so the result
is an upper bound), with pressure drop $\Delta p$ in pascals, oil density $\rho$ in kilograms per
cubic metre (kg/m$^3$), and jet speed $v_j$ in m/s. A typical density for hydraulic oil is 870 kg/m$^3$:

$$v_j = \sqrt{\frac{2\,\Delta p}{\rho}}$$

Energy stored in compressed oil of volume $V$ in cubic metres (m$^3$), with bulk modulus $K$ in
pascals. A typical bulk modulus for mineral oil is about $1.6 \times 10^9$ Pa:

$$E = \frac{\Delta p^2\,V}{2K}$$

Energy stored by a raised load of mass $m$ in kilograms (kg) at height $h$ in metres (m), assuming
the load is held still and the local gravity is $g = 9.81\ \text{m}/\text{s}^2$:

$$E = m\,g\,h$$

## Worked example

**Given:** A double-acting cylinder has bore $D = 0.080\ \text{m}$ and rod diameter $d = 0.040\ \text{m}$.
The pump supplies oil at $p = 10\ \text{MPa}$ and flow $Q = 30\ \text{L/min}$. The pump efficiency is
$\eta = 0.85$. The stroke is $0.50\ \text{m}$.

**Find:** (a) the extend and retract forces, (b) the extend and retract speeds, (c) the stroke time,
and (d) the pump input power.

**Solution:**

1. Convert the flow: $Q = 30 / 60000 = 5.00 \times 10^{-4}\ \text{m}^3/\text{s}$.
2. Bore area: $A = \pi (0.080)^2 / 4 = 5.027 \times 10^{-3}\ \text{m}^2$.
3. Annulus area: $A_a = \pi \left(0.080^2 - 0.040^2\right) / 4 = 3.770 \times 10^{-3}\ \text{m}^2$.
4. (a) Extend force: $F = 10 \times 10^6 \times 5.027 \times 10^{-3} = 50.3\ \text{kN}$.
   Retract force: $F = 10 \times 10^6 \times 3.770 \times 10^{-3} = 37.7\ \text{kN}$.
5. (b) Extend speed: $v = 5.00 \times 10^{-4} / 5.027 \times 10^{-3} = 0.0995\ \text{m/s}$, which is
   $99.5\ \text{mm/s}$.
   Retract speed: $v = 5.00 \times 10^{-4} / 3.770 \times 10^{-3} = 0.133\ \text{m/s}$, which is
   $133\ \text{mm/s}$.
6. (c) Stroke time: $t = 0.50 / 0.0995 = 5.03\ \text{s}$.
7. (d) Hydraulic power: $P_{\text{hyd}} = 10 \times 10^6 \times 5.00 \times 10^{-4} = 5.00\ \text{kW}$.
   Pump input: $P_{\text{in}} = 5.00 / 0.85 = 5.88\ \text{kW}$.

**Answer:** (a) $F_{\text{extend}} = 50.3\ \text{kN}$, $F_{\text{retract}} = 37.7\ \text{kN}$.
(b) $v_{\text{extend}} = 99.5\ \text{mm/s}$, $v_{\text{retract}} = 133\ \text{mm/s}$. (c) $5.03\ \text{s}$.
(d) $P_{\text{in}} = 5.88\ \text{kW}$.

**Sanity check:** The extend force times the extend speed must equal the hydraulic power, because
$F v = p A (Q / A) = p Q$. Here $50\,265\ \text{N} \times 0.0995\ \text{m/s} = 5000\ \text{W}$, which
matches. The retract speed is higher because the rod side has less area, so the same flow moves the
piston faster but with less force.

**Injection and stored energy in the same system.** A pinhole leak at $\Delta p = 20\ \text{MPa}$ gives
an ideal jet speed of $\sqrt{2 \times 20 \times 10^6 / 870} = 214\ \text{m/s}$. The real jet is slower
because of losses, but it still penetrates skin. One litre of oil at $10\ \text{MPa}$ stores
$\Delta p^2 V / (2K) = (10^7)^2 \times 10^{-3} / (2 \times 1.6 \times 10^9) = 31\ \text{J}$. A
$2000\ \text{kg}$ load held $2\ \text{m}$ high stores $m g h = 2000 \times 9.81 \times 2 = 39\ \text{kJ}$ (with $g = 9.81\ \text{m}/\text{s}^2$ at Earth's surface).
A held load is a larger hazard than the oil in the line.

## Design trade-offs

- Force against size: a higher pressure gives the same force from a smaller bore. This saves
  space and weight, but it raises the hose rating, seal cost, and injury risk.
- Speed against pump size: a cylinder's speed is set by flow. A bigger cylinder needs a bigger pump
  for the same speed.
- Throttling loses power: a flow control valve drops pressure across an orifice, and the loss is
  $\Delta p\,Q$ as heat. Variable displacement pumps waste less power than constant displacement pumps
  with a throttle.
- Stiffness against compressibility: oil is nearly incompressible, so hydraulic cylinders hold
  position well. Air compresses, so pneumatic cylinders bounce and cannot hold a position under load.
- Cleanliness against cost: filters and sealed reservoirs protect valves and seals. A contaminated
  system wears out quickly.
- Noise and heat: pumps and valves are the main noise sources. Heat rises when flow is throttled, and
  the oil must be cooled.

## How it fails

- Hose or fitting burst: a worn hose or an overpressure spike splits the line. The oil sprays out at
  high speed.
- Injection injury: a pinhole leak at high pressure forces oil into the skin. The oil looks like a
  small cut or bruise, but it damages tissue and can cause infection. Treat every high-pressure
  injection as a surgical emergency and get medical care at once.
- Dropped load: a leaking directional valve lets a raised cylinder sink.
- Stored energy after shutdown: an accumulator stays charged after the pump stops, and a cylinder
  holds pressure on one side after the pump is off.

Safety follows the hierarchy of controls, strongest first:

1. Elimination: design the load so it does not need to be held in the air, or remove the hazard
   entirely, for example by using a mechanical stop.
2. Substitution: use a lower operating pressure, a lower-energy actuator such as an electric drive
   for light loads, or a fire-resistant fluid where that suits the task.
3. Engineering controls: relief valves, pressure-rated hoses with guards, counterbalance and
   load-holding valves, flow restrictors, check valves, and hardwired emergency stops that cut pump
   power directly rather than through a program.
4. Administrative controls: written procedures, training, a maintenance schedule for hoses and
   relief valves, and a rule that no one checks for leaks with a bare hand.
5. Personal protective equipment: safety glasses, a face shield, and gloves. PPE is the last layer,
   because a jet at high pressure can pass through ordinary clothing.

Lockout and tagout before any service:

- Isolate every energy source: shut off the pump motor at its disconnect, close the supply valve,
  and disconnect the electrical and pneumatic supply where applicable.
- Release or restrain the stored hydraulic and pneumatic pressure: open the bleed valves, let the
  accumulator discharge through its bleed port, and block any raised load with mechanical stops or
  safety blocks before work begins.
- Verify a zero-energy state: attempt to start the machine from its normal control, confirm the
  pressure gauge reads zero, and only then begin work. Lock and tag every isolation point, and remove
  the lock only when the person who applied it is finished.
- Contamination: particles score the spool and the bore, and the valve sticks. Filters and regular oil
  changes prevent it.
- Overheating: throttling and internal leakage heat the oil, which thins it and reduces its
  lubrication. A cooler and a sized reservoir limit the heat.
- Relief valve stuck closed: the pressure rises until a hose or seal fails. Relief valves are tested
  regularly for this reason.

## History

Blaise Pascal described the principle of fluid pressure in the 1650s, and it became known as Pascal's
law. Joseph Bramah, an English engineer, patented a hydraulic press in 1795. The press used a small
pump and a large ram to produce large forces. Hydraulic systems spread through industry in the 19th
century for presses, cranes, and dock machinery. Hydraulics then grew into mobile machines such as
excavators and aircraft flight controls in the 20th century, and pneumatic tools and automation
followed the same pattern.

## Lessons for engineers today

- Pressure multiplies force, so the cylinder and the pump must be sized together.
- Stored energy is as dangerous as the moving parts. Design the system to hold, bleed, or dump it
  on purpose.
- A hydraulic leak can be lethal even when it looks small.

## Practice

Where a problem needs gravitational acceleration, use $g = 9.81\ \text{m}/\text{s}^2$ (Earth surface).

1. A cylinder has bore $D = 0.100\ \text{m}$ and runs at $p = 15\ \text{MPa}$. Find the extend force.
2. The same cylinder with bore $0.063\ \text{m}$ receives $Q = 20\ \text{L/min}$. Find the extend
   speed in mm/s.
3. A pump delivers $25\ \text{L/min}$ at $15\ \text{MPa}$ with efficiency $\eta = 0.90$. Find the
   hydraulic power and the input power.
4. A pinhole leak is at $\Delta p = 25\ \text{MPa}$ in oil of density $870\ \text{kg}/\text{m}^3$. Find the
   ideal jet speed.
5. A cylinder with bore $0.080\ \text{m}$ lifts a $2000\ \text{kg}$ load with no friction. Find the
   pressure needed, in MPa.

<details><summary>Answers</summary>

1. $F = 15 \times 10^6 \times \pi (0.100)^2 / 4 = 118\ \text{kN}$
2. $v = (20 / 60000) / (\pi (0.063)^2 / 4) = 0.107\ \text{m/s}$, which is $107\ \text{mm/s}$
3. $P_{\text{hyd}} = 15 \times 10^6 \times 25 / 60000 = 6.25\ \text{kW}$. $P_{\text{in}} = 6.25 / 0.90 = 6.94\ \text{kW}$
4. $v_j = \sqrt{2 \times 25 \times 10^6 / 870} = 240\ \text{m/s}$
5. $F = 2000 \times 9.81 = 19.6\ \text{kN}$, and $p = F / A = 19\,620 / 5.027 \times 10^{-3} = 3.90\ \text{MPa}$

</details>

## Common mistakes

- Using the bore area for the retract stroke. The retract force uses the annulus area, which is
  smaller because the rod takes up part of the bore.
- Treating litres per minute as cubic metres per second without converting. One litre per minute is
  $1.667 \times 10^{-5}$ m$^3$/s.
- Calling a small injection leak harmless. The jet at high pressure is fast enough to penetrate skin.
- Assuming a raised load stays up when the pump stops. A leaking valve lets it drop, unless a
  load-holding valve prevents that.
- Mixing gauge pressure and absolute pressure in the same calculation. The formulas here use gauge
  pressure.

## Go deeper

- [University Physics Volume 1, Chapter 14 (fluid mechanics)](https://openstax.org/books/university-physics-volume-1/pages/14-introduction)
  by OpenStax: Pascal's principle, hydraulic systems, and fluid pressure.
- [Robotics, Wikibooks](https://en.wikibooks.org/wiki/Robotics) by Wikibooks contributors: actuators,
  including pneumatic drives, and how they connect to robot joints.
- Reference sheets: [Applications reference](../reference.md) and
  [Thermofluids reference](../../physics/reference-thermofluids.md).
- Related lessons: [Fluid systems](../thermal-fluid/02-fluid-systems.md),
  [Pumps](../thermal-fluid/09-pumps.md),
  [Piping and valves](../thermal-fluid/12-piping-and-valves.md),
  [Robot arms](01-robot-arms.md), and
  [Conveyors and automation](06-conveyors-and-automation.md).
