# Gear trains

**Type:** lesson

A gear train passes power from one shaft to another through meshing teeth, and the tooth count sets the speed and torque at the output. Designers pick the tooth form, the number of stages, and the losses, and each choice changes noise, size, and how the drive wears out.

**Prerequisites:** [Gears, fasteners, and springs](../../design/09-gears-fasteners-and-springs.md), [Shafts and bearings](../../design/08-shafts-and-bearings.md), [Rigid body dynamics](../../physics/03-rigid-body-dynamics.md), [Trigonometry](../../math/02-trigonometry.md)
**Time:** 4-6 h

## Core ideas

### How it works

A gear train is a chain of meshing gears. The driver's teeth push on the driven gear's teeth at the pitch circles, and the force they exchange sets the torque on each shaft. The basic speed ratio and the pitch formulas are in the [gears lesson](../../design/09-gears-fasteners-and-springs.md). This lesson adds the tooth forms, the stages, and the losses that the ideal ratio leaves out.

The ratio of a train is the product of the ratios of its stages. A two-stage train with ratios 3 and 3 has a total ratio of 9. The output turns nine times slower than the input and carries nine times the torque, minus the losses. Power is conserved except for losses, so the output power is the input power times the efficiency.

An idler gear placed between two gears reverses the rotation direction without changing the ratio. Designers use idlers when the output must turn the same way as the input and the shafts cannot sit on the same axis.

### Main parts

- **Pinion.** The smaller gear of a pair. It is usually the driver when the train reduces speed.
- **Gear.** The larger gear of a pair. It is usually the driven member.
- **Shafts and bearings.** They hold the gears at the correct center distance. A shaft that deflects under load moves the teeth out of line and concentrates the load on one edge.
- **Housing.** It holds the lubricant, seals the gears from dirt, and keeps the shafts aligned.
- **Idler.** A gear that changes direction without changing the ratio of the train.

### Variants

- **Spur gears.** The teeth run straight across the face, parallel to the shaft. They are simple and cheap to cut. They are louder at high speed because each tooth meets its mate with a sudden load change.
- **Helical gears.** The teeth are cut at a helix angle $\psi$. Several teeth share the load at any moment, so the drive runs smoother and quieter. The angled teeth also push the gear sideways, so helical gears need thrust bearings.
- **Bevel gears.** The shafts meet at an angle, usually 90 degrees. The teeth are cut on cones. Bevel pairs appear in right-angle drives and in differentials.
- **Worm gears.** A screw, called the worm, drives a wheel. One stage gives a large ratio in a small space, but sliding contact lowers the efficiency. A worm can be self-locking, so the wheel cannot turn the worm.

A single spur stage usually gives a ratio of about 3:1 to 6:1 in ordinary machines (typical). Larger ratios use a second or third stage, which adds parts and bearing losses.

## Key equations

Total ratio of a train with stages $k = 1, 2, \ldots$, where $N_{\mathrm{in},k}$ is the number of teeth on the driver of stage $k$ and $N_{\mathrm{out},k}$ is the number on its driven gear:

$$
i = \prod_k i_k = \prod_k \frac{N_{\mathrm{out},k}}{N_{\mathrm{in},k}}
$$

Output speed and output torque, with $n$ in rpm, $T$ in N$\cdot$m, and the overall efficiency $\eta$ dimensionless:

$$
n_{\mathrm{out}} = \frac{n_{\mathrm{in}}}{i}, \qquad T_{\mathrm{out}} = \eta\, i\, T_{\mathrm{in}}
$$

The overall efficiency is the product of the mesh efficiencies, $\eta = \prod_k \eta_k$. A clean spur mesh has $\eta_k$ of about 0.98 (typical).

Power, with $\omega = 2\pi n / 60$ in rad/s and $P$ in W:

$$
P = T\,\omega, \qquad P_{\mathrm{out}} = \eta\, P_{\mathrm{in}}
$$

Helical gears, with normal module $m_n$ in mm, helix angle $\psi$, normal pressure angle $\phi_n$, and tooth count $N$:

$$
m_t = \frac{m_n}{\cos\psi}, \qquad d = m_t N, \qquad F_t = \frac{2T}{d}, \qquad F_a = F_t \tan\psi, \qquad F_r = \frac{F_t \tan\phi_n}{\cos\psi}
$$

Here $d$ is in metres when $T$ is in N$\cdot$m and $F_t$ is in N. The forces are tangential $F_t$, axial $F_a$, and radial $F_r$, all in N.

Bevel pair with shaft angle $\Sigma$ and ratio $u = N_2 / N_1$, giving pitch cone angles $\gamma_1$ and $\gamma_2$ in radians or degrees:

$$
\tan\gamma_1 = \frac{\sin\Sigma}{u + \cos\Sigma}, \qquad \gamma_2 = \Sigma - \gamma_1
$$

Worm drive with $z$ starts, axial pitch $p_x$ in mm, worm pitch diameter $d_w$ in mm, and friction coefficient $\mu$:

$$
i = \frac{N_{\mathrm{wheel}}}{z}, \qquad \tan\lambda = \frac{z\,p_x}{\pi\, d_w}, \qquad \eta = \frac{\tan\lambda}{\tan(\lambda + \varphi)}, \qquad \tan\varphi = \mu
$$

The lead angle is $\lambda$, and the friction angle is $\varphi$. The drive is self-locking when $\lambda < \varphi$, which is a common rule.

## Worked example

**Given.** A motor turns at $n_{\mathrm{in}} = 1800$ rpm and delivers $T_{\mathrm{in}} = 2.0$ N$\cdot$m. The train has two spur stages. Stage 1 has a pinion of 18 teeth and a gear of 54 teeth. Stage 2 has a pinion of 20 teeth and a gear of 60 teeth. Each mesh has $\eta_k = 0.98$.

**Find.** The total ratio, the output speed, the output torque, and the output power when the input power is $P_{\mathrm{in}}$.

**Assumptions.** The mesh efficiency is 0.98 for each stage. The shafts are rigid, and the losses are only the mesh losses.

**Solution.**

Step 1. Total ratio: $i = \dfrac{54}{18} \times \dfrac{60}{20} = 3.0 \times 3.0 = 9.000$.

Step 2. Output speed: $n_{\mathrm{out}} = 1800 / 9.000 = 200.0$ rpm.

Step 3. Overall efficiency: $\eta = 0.98^2 = 0.9604$.

Step 4. Output torque: $T_{\mathrm{out}} = 0.9604 \times 9.000 \times 2.0 = 17.29$ N$\cdot$m.

Step 5. Input power: $\omega_{\mathrm{in}} = 1800 \times 2\pi / 60 = 188.5$ rad/s, so $P_{\mathrm{in}} = 2.0 \times 188.5 = 377.0$ W.

Step 6. Output power: $\omega_{\mathrm{out}} = 200.0 \times 2\pi / 60 = 20.94$ rad/s, so $P_{\mathrm{out}} = 17.29 \times 20.94 = 362.1$ W.

**Answer.** Ratio 9.000. Output speed 200 rpm. Output torque 17.29 N$\cdot$m. Output power 362.1 W, which is $0.9604$ of the 377.0 W input.

**Sanity check.** The output torque is below the ideal $9 \times 2.0 = 18.0$ N$\cdot$m because of the losses, and the output power is $0.9604 \times 377.0 = 362.1$ W, so the energy balance holds.

For the helical case, take a pinion with $m_n = 2.0$ mm, $\psi = 20$ degrees, $\phi_n = 20$ degrees, $N = 24$ teeth, and a torque of 30 N$\cdot$m. The transverse module is $m_t = 2.128$ mm, the pitch diameter is 51.08 mm, the tangential force is 1174.6 N, the axial thrust is 427.5 N, and the radial force is 455.0 N. The axial thrust is large, so the shaft needs a bearing that carries thrust.

For a worm with two starts, $p_x = 2\pi$ mm, and a 40 mm worm pitch diameter, the lead angle is $\lambda = 5.71$ degrees. A wheel of 40 teeth gives a ratio of 20. With $\mu = 0.05$, the efficiency is 0.663. With $\mu = 0.10$, the efficiency falls to 0.495, and the lead angle equals the friction angle, which marks the edge of self-locking.

## Design trade-offs

- **Efficiency against ratio.** A spur or helical pair loses about 2 percent per mesh (typical). A worm stage can lose half its power or more at a large ratio. A worm is a poor choice for a drive that must pass power efficiently.
- **Noise against cost.** Helical gears run quieter than spur gears at the same speed, but they cost more to cut and carry thrust loads. The pitch-line velocity from the [gears lesson](../../design/09-gears-fasteners-and-springs.md) sets how loud a pair will run.
- **Size against stage count.** A large ratio in one stage needs a large gear. Two smaller stages fit in less space but add bearings, housings, and losses.
- **Backlash against positioning.** Backlash is the clearance between mating teeth. A gear train needs some backlash for lubricant films and for thermal growth. Too much backlash makes a positioning drive jump and overshoot. Precision drives control the center distance tightly and sometimes preload the pair, which adds friction.
- **Life against load.** Doubling the tooth face width or the module lowers the stress on each tooth, but it adds weight and cost.

## How it fails

- **Tooth bending fatigue.** A cracked tooth root starts from a stress concentration at the fillet. The warning signs are a sudden change in noise and a broken tooth on inspection. Designers use a factor of safety on tooth bending stress, as described in the [factor of safety lesson](../../design/07-factor-of-safety-and-failure.md).
- **Pitting.** Repeated contact stress on the flank makes small pits. Pitting grows when lubrication is thin or the teeth are misaligned. The warning sign is a grey, rough tooth surface.
- **Scuffing.** Heavy sliding at high temperature tears the oil film and welds small areas of the tooth surface together. Scuffing appears after a lubricant failure.
- **Wear and backlash growth.** Wear opens the clearance between teeth over time. The warning sign is a rattle or a rising play in a positioning axis.
- **Misalignment.** A shaft that deflects or a housing that flexes puts the load on one edge of each tooth. Check the shaft deflection, as described in the [shafts lesson](../../design/08-shafts-and-bearings.md).

Safety measures include oil or grease lubrication, sealed housings, guards around exposed gears, and torque limiters that slip before a gear breaks. A worm wheel of bronze is often specified because the bronze wears gently against steel and resists scuffing.

## History

The Antikythera mechanism, a bronze device recovered from a shipwreck off the Greek island of Antikythera in 1901, used a set of gears to track astronomical cycles. It dates to about the 2nd or 1st century BCE. Gear trains then spread into mills, clocks, and cranes over the following centuries. The involute tooth shape, which keeps the speed ratio constant as the teeth mesh, is the form used on almost all modern gears.

## Practice

1. A pinion of 20 teeth drives a gear of 60 teeth. The input speed is 900 rpm. Find the output speed.
2. A gear mesh has a ratio of 5 and a mesh efficiency of 0.98. The input torque is 4 N$\cdot$m. Find the output torque.
3. A helical pinion has a normal module of 2.5 mm and a helix angle of 25 degrees. Find the transverse module to three decimal places.
4. A worm lead angle is $\lambda = 4.57$ degrees, and the friction angle is $\varphi = 5.71$ degrees. Is the drive self-locking?

<details><summary>Answers</summary>

1. $n_{\mathrm{out}} = 900 \times 20 / 60 = 300$ rpm.
2. $T_{\mathrm{out}} = 0.98 \times 5 \times 4 = 19.6$ N$\cdot$m.
3. $m_t = 2.5 / \cos 25^\circ = 2.758$ mm.
4. Yes. $\lambda < \varphi$ means the wheel cannot drive the worm.

</details>

## Common mistakes

- Multiplying the ratios of the stages but forgetting that each stage loses power. The output torque is always below the ideal ratio times the input torque.
- Using the normal module as the module in the pitch diameter formula of a helical gear. The transverse module $m_t = m_n / \cos\psi$ is the one that sets the pitch diameter.
- Ignoring the axial thrust on a helical gear. The thrust must go to a thrust bearing, or the shaft walks sideways.
- Treating a worm drive as efficient because its ratio is large. At a lead angle near the friction angle, the efficiency is low.
- Forgetting that an idler changes the direction of rotation but not the ratio of the train.

## Go deeper

- [University Physics Volume 1, Chapter 10 (rotational motion)](https://openstax.org/books/university-physics-volume-1/pages/10-introduction) by OpenStax: moment of inertia, torque, and power for rotating shafts, the physics behind every gear train.
- [Gears, fasteners, and springs](../../design/09-gears-fasteners-and-springs.md): the module, pitch diameter, and center distance formulas that this lesson builds on.
- [Planetary gears](02-planetary-gears.md): the same ratio idea with three moving members and the Willis equation.
- [Belts and chains](03-belts-and-chains.md): the other way to pass power between shafts, with no teeth meshing.
- [Applications reference](../reference.md): the lookup sheet for this topic.
