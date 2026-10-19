# Towers and cables

**Type:** lesson

A tower and its cables carry wind, ice, and their own weight into the ground with very little material. An engineer must predict how far a cable sags and how much tension it carries, because the sag sets clearances and the tension sets the size of every anchor.

**Prerequisites:** [Statics](../../physics/01-statics.md), [Trigonometry](../../math/02-trigonometry.md), [Single-variable calculus](../../math/03-single-variable-calculus.md), [Factor of safety and failure](../../design/07-factor-of-safety-and-failure.md)
**Time:** 6-8 h

## Core ideas

### How it works

A cable carries tension only. It cannot push, and it resists bending only through its shape. Under load, the cable takes whatever shape balances the load with tension. The sag depends on three things: the load per unit length, the span, and the horizontal tension.

More horizontal tension means less sag. Less sag means higher tension in the cable and larger forces on the anchors. Engineers pick the tension to balance clearance against the strength of the anchors and the tower.

A guyed mast stands because its guy cables pull sideways. Wind pushes the mast over, and the guys on the windward side pull back on the mast through their horizontal parts. Each guy also has a vertical part, which the mast base or the guy anchors must carry.

Wind pushes on every tower and cable through drag. The drag force grows with the square of wind speed. A 20 percent rise in wind speed raises the force by 44 percent, because $1.2^2 = 1.44$.

### Main parts

- **Mast or tower:** the vertical member. It may be a steel lattice, a steel tube, or concrete.
- **Guy cables:** steel strands that run from the mast to anchors in the ground.
- **Anchors:** concrete blocks or rock anchors that carry the guy forces into the ground.
- **Pretension device:** a turnbuckle or hydraulic jack that sets the guy tension during erection.
- **Main cable and hangers:** on a suspension bridge, the main cable carries the deck through vertical hangers.
- **Stay cables:** straight cables that run from a tower to the deck of a cable-stayed bridge.
- **Conductors and insulators:** the wires of a power line and the insulators that hold them to the towers.

### Variants

- **Guyed mast:** tall and slender, held by guys at several heights. Radio and television masts often use this form.
- **Free-standing lattice tower:** no guys. The base takes all the bending moment, so the foundation is large. Many power line towers use this form.
- **Suspension bridge:** main cables run from tower to tower and carry the deck through hangers.
- **Cable-stayed bridge:** many straight stay cables run from the towers to the deck. The stays carry the deck directly.
- **Power line:** conductors hang between towers. Their sag changes with temperature, load, and ice.

## Key equations

The parabolic approximation applies when the load is spread evenly along the horizontal projection of the cable. It assumes level supports, a cable that does not stretch, and a sag small compared with the span. Here $q$ is the load per metre of horizontal span in N/m, $L$ is the span in metres, $T_H$ is the horizontal tension in newtons, and $d$ is the sag in metres, measured at midspan with level supports.

$$d = \frac{q L^2}{8 T_H}$$

The parabola has the shape $y(x) = \dfrac{q\,x\,(L - x)}{2 T_H}$, measured from one support. The parabolic length assumes the same conditions, with $d/L$ well below 1. The cable length is approximately:

$$S \approx L + \frac{8 d^2}{3 L}$$

The catenary applies when the cable's own weight is the load. It assumes level supports, a cable that does not stretch, and a uniform weight per metre of cable with no other load. Here $w$ is the weight per metre of cable in N/m. The sag, length, and support tension are:

$$d = \frac{T_H}{w}\left(\cosh\frac{wL}{2T_H} - 1\right), \qquad S = \frac{2T_H}{w}\sinh\frac{wL}{2T_H}, \qquad T_{\mathrm{max}} = T_H \cosh\frac{wL}{2T_H}$$

Here $\cosh$ and $\sinh$ are the hyperbolic cosine and sine, which are dimensionless. The shape formula for the catenary is $y(x) = \dfrac{T_H}{w}\left(\cosh\dfrac{wx}{T_H} - 1\right)$, measured from the lowest point.

Wind drag on a tower or cable assumes steady wind, uniform flow over the member, and a drag coefficient that stays constant over the speed range. The drag is:

$$F = \tfrac{1}{2}\rho_a v^2 C_d A$$

Here $F$ is in newtons, $\rho_a$ is the air density in kilograms per cubic metre (about $1.2\ \text{kg}/\text{m}^3$ at sea level, typical), $v$ is wind speed in metres per second, $C_d$ is the dimensionless drag coefficient, and $A$ is the projected area in square metres.

## Worked example

**Given:** A cable spans $L = 300\ \text{m}$ between level supports. Its weight is $w = 20\ \text{N/m}$, which is about 2 kg per metre. Treat the cable's own weight as the only load, and set $q = w$ for the parabolic method. Two cases use the same cable with different horizontal tensions: case A with $T_H = 10\ \text{kN}$, and case B with $T_H = 3\ \text{kN}$.

**Find:** the sag and length by each method, the percent error of the parabola, and the support tension in case B.

**Solution:**

Case A:

1. Parabolic sag: $d = 20 \times 300^2 / (8 \times 10\,000) = 22.50\ \text{m}$.
2. Catenary sag: $d = 500\,(\cosh 0.3 - 1) = 22.67\ \text{m}$.
3. Error: $(22.50 - 22.67)/22.67 = -0.75$ percent. The sag-to-span ratio is $d/L = 0.075$.
4. Length: parabola $304.50\ \text{m}$, catenary $304.52\ \text{m}$.

Case B:

5. Parabolic sag: $d = 20 \times 300^2 / (8 \times 3000) = 75.0\ \text{m}$.
6. Catenary sag: $d = 150\,(\cosh 1.0 - 1) = 81.46\ \text{m}$.
7. Error: $(75.0 - 81.46)/81.46 = -7.9$ percent. The sag-to-span ratio is $d/L = 0.25$.
8. Length: parabola $350.0\ \text{m}$, catenary $352.56\ \text{m}$.
9. Support tension: the catenary gives $3000\cosh 1.0 = 4.63\ \text{kN}$. The common shortcut $\sqrt{T_H^2 + (wL/2)^2} = 4.24\ \text{kN}$ is 8.3 percent low.

**Answer:** At $d/L = 0.075$, the parabola is within 1 percent of the catenary. At $d/L = 0.25$, the parabola underpredicts the sag by 7.9 percent, the length by $2.56\ \text{m}$, and the support tension by 8.3 percent.

**Sanity check:** The parabolic sag scales with $1/T_H$. Case B has one-third the tension of case A, so its sag should be 3.33 times as large. The parabolic sags give $75.0/22.50 = 3.33$, which matches. Both lengths are a little longer than the span, as expected for any sagging cable.

## Design trade-offs

- **Sag against tension:** a tight cable has little sag and high tension. Anchors and towers must carry that tension, so they grow larger and costlier. A slack cable sags into clearance limits, especially on a power line.
- **Temperature and ice:** a steel cable grows longer when warm and shorter when cold. A power line that is tight in winter sags in summer. Ice adds weight and can double the load on a conductor in a severe storm.
- **Guy spacing:** more guy levels reduce the bending in a mast, but they need more ground area for the anchors.
- **Lattice against tube:** a lattice tower uses less steel for the same strength, but it catches more wind. A tube sheds wind more smoothly but uses more material.
- **Corrosion protection:** galvanized wire and corrosion-resistant coatings extend the life of a cable in damp or salty air. They add cost but cut replacement.

## How it fails

- **Broken wires:** repeated bending at the anchor or socket fatigues the wires. Warning signs include broken wire ends and fretting dust at the socket.
- **Vibration:** wind can set a cable vibrating at its natural frequency. Ice on a conductor can make it gallop with large motions. Dampers and spacers reduce these motions.
- **Corrosion:** water and salt attack steel strands from the outside in. Rust and reduced diameter are the warning signs.
- **Tower buckling:** a tall slender mast can buckle under the compression from its own weight and from guy pretension.
- **Anchor pullout:** the ground gives way under a guy's pull. Load tests and soil checks guard against it.
- **Wind-induced oscillation of a deck:** the Tacoma Narrows Bridge in Washington State collapsed in November 1940 when wind set its deck into a violent twisting motion. The failure changed how engineers design deck stiffness and wind response.

The safety measures include a factor of safety on every cable and anchor, galvanizing or other corrosion protection, dampers on conductors, pretension checks during erection, and regular inspection of wires and sockets.

## History

Galileo studied hanging chains in his 1638 book *Two New Sciences* and wrongly concluded that the shape was a parabola. In 1690 and 1691, Huygens, Leibniz, and Johann Bernoulli worked out the correct curve, which is the catenary. The Brooklyn Bridge in New York opened in 1883. John Roebling designed it, and Washington Roebling finished it after his father died in 1869 from an accident during the survey.

## Practice

1. A cable spans 200 m and carries a load of 50 N/m with a horizontal tension of 20 kN. Find the parabolic sag, then the cable length.
2. A tower face of 30 m$^2$ is exposed to wind at 25 m/s. Its drag coefficient is 1.2. Find the wind force.
3. A cable spans 100 m with a self-weight of 20 N/m and a horizontal tension of 10 kN. Find the catenary support tension.
4. A guy cable at 45 degrees carries 10 kN of tension. Find its horizontal and vertical components.

<details><summary>Answers</summary>

1. $d = 50 \times 200^2 / (8 \times 20\,000) = 12.5\ \text{m}$. The length is $S \approx 200 + 8(12.5)^2/(3 \times 200) = 202.08\ \text{m}$.
2. $F = \tfrac{1}{2}(1.2)(25)^2(1.2)(30) = 1.35 \times 10^4\ \text{N}$, which is $13.5\ \text{kN}$.
3. $T_{\mathrm{max}} = 10\,000\cosh(0.1) = 1.005 \times 10^4\ \text{N}$, which is $10.05\ \text{kN}$.
4. Horizontal component: $10 \cos 45^\circ = 7.07\ \text{kN}$. Vertical component: $10 \sin 45^\circ = 7.07\ \text{kN}$.

</details>

## Common mistakes

- **Using the parabola for a deep sag.** The parabola is accurate only when the sag is small compared with the span. Check $d/L$ before trusting it.
- **Mixing up the two loads.** A load spread evenly along the horizontal projection gives a parabola. The cable's own weight per metre of cable gives a catenary. The two differ when the sag is large.
- **Forgetting that drag grows with the square of speed.** Doubling the wind speed multiplies the force by four.
- **Treating the anchor load as only the tension.** An anchor takes the full cable force at its angle, so both components matter.
- **Ignoring temperature and ice.** Both change the sag and the tension. A design that works in mild weather can fail in winter.

## Go deeper

- [Reference sheet: mechanics](../../physics/reference-mechanics.md): statics, tension, and buckling in one place.
- [Axial and torsion](../../physics/04-axial-and-torsion.md): stress and strain in a rod or cable under pure tension.
- [Bending and buckling](../../physics/05-bending-and-buckling.md): why a slender tower can buckle under compression.
- [Bridges](01-bridges.md): suspension and cable-stayed bridges in more detail.
- [Dams](05-dams.md): another structure that resists forces at its foundation.
- [Trigonometry](../../math/02-trigonometry.md): splitting a cable force into horizontal and vertical parts.
