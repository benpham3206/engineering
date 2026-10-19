# Heat transfer reference

**Type:** reference
**Verify:** strict

Lookup sheet for conduction, thermal resistance networks, fins, transient conduction, convection groups, radiation exchange, and heat exchangers, for an engineer who needs a formula, a limit, or a check in the middle of a job.

Thermodynamics and the ideal gas live in [Thermal-fluids reference](reference-thermofluids.md#thermodynamics). Device-level exchanger design is in [Heat exchangers](../applications/thermal-fluid/05-heat-exchangers.md). The lesson behind this sheet is [Heat transfer](12-heat-transfer.md).

## Principles

- Heat flows from hot to cold, and the rate is set by a temperature difference divided by a resistance. Every result in this sheet is a version of that statement.
- Energy is conserved. A steady problem has heat in equal to heat out at every surface and every interface. If the interface balance fails, a resistance is missing.
- Conduction is linear in temperature, convection is linear in temperature for a given $h_c$, and radiation goes as the fourth power of absolute temperature. Use kelvin in every radiation term.
- Conduction rate scales with thermal conductivity and inversely with thickness [src](../data/claims/heat-transfer.md#openstax-conduction-form). Doubling thickness halves the rate; doubling area doubles it. Check the scaling before trusting a number.
- A convection coefficient is not a material property. It depends on the fluid, the speed, the geometry, and the temperatures, so it is always attached to a correlation or a measurement.
- Dimensionless groups carry the physics. $\mathrm{Re}$, $\mathrm{Pr}$, $\mathrm{Gr}$, $\mathrm{Bi}$, and $\mathrm{Fo}$ say which regime applies before any formula is chosen.
- A thin solid layer or a small body can be treated as one temperature only when its internal resistance is small against the surface resistance ($\mathrm{Bi}$ small).
- Radiation needs no medium and does not add like conduction. The net exchange depends on emissivity, geometry through the view factor, and both temperatures.
- Adding insulation lowers heat loss only when the outer surface of the insulation sits beyond the critical radius.
- Net radiation between a gray surface and large surroundings is proportional to emissivity and to the difference of fourth powers of absolute temperature [src](../data/claims/heat-transfer.md#openstax-radiation-form).

## Governing energy equation

### Heat equation and thermal diffusivity

Energy balance on a small solid element with constant properties gives how its temperature changes with time and position.

$$
\frac{\partial T}{\partial t} = \alpha_{\text{th}}\,\nabla^{2}T + \frac{\dot{q}_{\text{gen}}}{\rho c_p}, \qquad \alpha_{\text{th}} = \frac{k_{\text{th}}}{\rho c_p}
$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $T$ | temperature | K |
| $t$ | time | s |
| $\alpha_{\text{th}}$ | thermal diffusivity | $\text{m}^{2}\text{/s}$ |
| $k_{\text{th}}$ | thermal conductivity | W/m K |
| $\rho$ | density | $\text{kg/m}^{3}$ |
| $c_p$ | specific heat (solid: $c_p \approx c$) | J/kg K |
| $\dot{q}_{\text{gen}}$ | volumetric heat generation | $\text{W/m}^{3}$ |

Holds when: the medium is a solid or a stationary fluid, properties are uniform and constant, and conduction obeys Fourier's law.
Breaks when: properties vary strongly with temperature, the material is anisotropic (use a conductivity tensor), the medium moves (add the convective term), or lengths approach the mean free path of the carriers.
Source and basis: derived from energy conservation on a control volume plus Fourier's law, taught in [Heat transfer](12-heat-transfer.md).

Example. Aluminium with $k_{\text{th}} = 237$ W/(m K), $\rho = 2700$ $\text{kg/m}^3$, and $c_p = 900$ J/(kg K) has $\alpha_{\text{th}}$ below. The time for a change to diffuse across $L = 0.05$ m scales as $L^2/\alpha_{\text{th}}$. Result: $\alpha_{\text{th}} = 9.75 \times 10^{-5}$ $\text{m}^2\text{/s}$ and $L^2/\alpha_{\text{th}} = 25.6$ s.

```verify
k = q(237, "W/m K")
rho = q(2700, "kg/m^3")
cp = q(900, "J/kg K")
L = q(0.05, "m")
alpha = k / (rho * cp)
expect(alpha, "9.75e-5 m^2/s")
expect(L**2 / alpha, "25.6 s")
```

## Steady conduction

### Plane wall, cylinder, and sphere

Steady one-dimensional heat rate through a wall, a hollow cylinder of length $L$, and a hollow sphere, with surface temperatures $T_1$ (inner) and $T_2$ (outer).

$$
\dot{Q}_{\text{wall}} = \frac{k_{\text{th}} A (T_1 - T_2)}{L}, \qquad \dot{Q}_{\text{cyl}} = \frac{2\pi k_{\text{th}} L (T_1 - T_2)}{\ln(r_2/r_1)}, \qquad \dot{Q}_{\text{sph}} = \frac{4\pi k_{\text{th}} (T_1 - T_2)}{1/r_1 - 1/r_2}
$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\dot{Q}$ | heat rate | W |
| $k_{\text{th}}$ | thermal conductivity | W/m K |
| $A$ | wall area normal to the heat flow | $\text{m}^{2}$ |
| $L$ | wall thickness, or cylinder length | m |
| $T_1$, $T_2$ | inner and outer surface temperatures | K |
| $r_1$, $r_2$ | inner and outer radius | m |

Holds when: steady state, no internal generation, constant $k_{\text{th}}$, heat flow in one direction only (radial for the cylinder and sphere), and isothermal surfaces.
Breaks when: the end effects of a short cylinder matter, $k_{\text{th}}$ changes strongly across the temperature range (use a mean value over the range), or heat generation exists inside the wall.
Source and basis: the conduction rate is proportional to thermal conductivity and inversely proportional to thickness [src](../data/claims/heat-transfer.md#openstax-conduction-form); derived from integrating Fourier's law with the steady heat equation in each geometry; taught in [Heat transfer](12-heat-transfer.md).

Examples. A 10 m long pipe with $k_{\text{th}} = 0.04$ W/(m K) insulation, $r_1 = 0.025$ m, $r_2 = 0.045$ m, and a 80 K difference loses 342 W. A hollow sphere with the same $k_{\text{th}}$, $r_1 = 0.1$ m, $r_2 = 0.15$ m, and 50 K difference loses 7.54 W. A concrete wall with $k_{\text{th}} = 1.0$ W/(m K), 10 $\text{m}^2$, 0.20 m thick, and a 15 K difference carries 750 W.

```verify
k = q(0.04, "W/m K")
dT = q(80, "K")
Lc = q(10, "m")
r1 = q(0.025, "m")
r2 = q(0.045, "m")
expect(2 * pi * k * Lc * dT / log(r2 / r1), "342 W")
s1 = q(0.1, "m")
s2 = q(0.15, "m")
dTs = q(50, "K")
expect(4 * pi * k * dTs / (1 / s1 - 1 / s2), "7.54 W")
kc = q(1.0, "W/m K")
A = q(10, "m^2")
Lw = q(0.2, "m")
dTw = q(15, "K")
expect(kc * A * dTw / Lw, "750 W")
```

## Thermal resistance networks

### Resistances, series and parallel paths, and the overall coefficient

A thermal resistance $R$ is the temperature difference that drives one watt along a path. Elements in series add, paths in parallel add their conductances, and the overall coefficient $U$ is set by the sum.

$$
R_{\text{cond}} = \frac{L}{k_{\text{th}}A}, \quad R_{\text{conv}} = \frac{1}{h_c A}, \quad R_{\text{rad}} = \frac{1}{h_r A}, \quad R_{\text{contact}} = \frac{R''_c}{A}
$$

$$
\dot{Q} = \frac{\Delta T}{\sum R} = U A\,\Delta T, \qquad \frac{1}{UA} = \sum R, \qquad \frac{1}{R_{\text{par}}} = \sum \frac{1}{R_i}, \qquad h_r = \epsilon_{\text{rad}}\,\sigma\,(T_s + T_{\text{sur}})(T_s^{2} + T_{\text{sur}}^{2})
$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $R$ | thermal resistance of an element | K/W |
| $R''_c$ | contact resistance per unit area | $\text{m}^{2}\text{ K/W}$ |
| $L$ | layer thickness | m |
| $k_{\text{th}}$ | thermal conductivity of the layer | W/m K |
| $A$ | area normal to the flow | $\text{m}^{2}$ |
| $h_c$ | convection coefficient | $\text{W/m}^{2}\text{ K}$ |
| $h_r$ | linearized radiation coefficient | $\text{W/m}^{2}\text{ K}$ |
| $\epsilon_{\text{rad}}$ | surface emissivity | dimensionless |
| $\sigma$ | Stefan-Boltzmann constant | $\text{W/m}^{2}\text{ K}^{4}$ |
| $T_s$, $T_{\text{sur}}$ | surface and surroundings absolute temperature | K |
| $U$ | overall heat transfer coefficient | $\text{W/m}^{2}\text{ K}$ |
| $\Delta T$ | overall temperature difference between the two fluids | K |
| $\dot{Q}$ | heat rate | W |

Holds when: steady state, one-dimensional flow, uniform properties in each layer, constant $h_c$ over each surface, and a linearized $h_r$ evaluated near the operating temperatures.
Breaks when: heat spreads sideways (thin high-conductivity layers, fins, corners), $h_c$ varies along the surface, or the surface and surroundings temperatures differ so much that $h_r$ changes appreciably over the range.
Source and basis: derived from the electrical analogy for steady conduction, convection, and the factored form of the radiation difference; taught in [Heat transfer](12-heat-transfer.md).

Example. Wall of 1.0 $\text{m}^2$: inside film $h_c = 8$ $\text{W/(m}^2\text{ K)}$, brick 0.10 m with $k_{\text{th}} = 0.72$ W/(m K), a contact resistance $R''_c = 0.01$ $\text{m}^2\text{ K/W}$, insulation 0.05 m with $k_{\text{th}} = 0.04$ W/(m K), outside film $h_c = 25$ $\text{W/(m}^2\text{ K)}$. Air differs by 26 K between inside and outside. Radiation coefficient for $\epsilon_{\text{rad}} = 0.9$, $T_s = 350$ K, $T_{\text{sur}} = 300$ K. Result: total resistance 1.56 K/W, overall coefficient 0.639 $\text{W/(m}^2\text{ K)}$, heat rate 16.6 W, and $h_r = 7.05$ $\text{W/(m}^2\text{ K)}$.

```verify
A = q(1.0, "m^2")
Ri = 1 / (q(8, "W/m^2 K") * A)
Rb = q(0.10, "m") / (q(0.72, "W/m K") * A)
Rc = q(0.01, "m^2 K/W") / A
Rins = q(0.05, "m") / (q(0.04, "W/m K") * A)
Ro = 1 / (q(25, "W/m^2 K") * A)
Rt = Ri + Rb + Rc + Rins + Ro
expect(Rt, "1.56 K/W")
expect(1 / (Rt * A), "0.639 W/m^2 K")
expect(q(26, "K") / Rt, "16.6 W")
sg = q(5.670374419e-8, "W/m^2 K^4", of="sigma_sb")
hr = q(0.9, "") * sg * q(650, "K") * (q(350, "K")**2 + q(300, "K")**2)
expect(hr, "7.05 W/m^2 K")
```

## Critical radius of insulation

### Insulation on a cylinder or sphere

Adding insulation to a small cylinder or sphere raises the outer area faster than it raises the conduction resistance, so heat loss first rises, peaks at the critical radius, then falls.

$$
r_{\text{cr,cyl}} = \frac{k_{\text{th}}}{h_c}, \qquad r_{\text{cr,sph}} = \frac{2k_{\text{th}}}{h_c}
$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $r_{\text{cr,cyl}}$ | critical outer radius, cylinder | m |
| $r_{\text{cr,sph}}$ | critical outer radius, sphere | m |
| $k_{\text{th}}$ | insulation conductivity | W/m K |
| $h_c$ | outer convection coefficient | $\text{W/m}^{2}\text{ K}$ |

Holds when: steady radial conduction in the insulation, a constant outer $h_c$ that does not change with radius, and negligible radiation change.
Breaks when: the bare pipe radius already exceeds $r_{\text{cr}}$ (every added layer then helps, which is the usual case for steam pipes), or $h_c$ falls with radius as natural convection does (the true peak shifts).
Source and basis: derived from setting the derivative of the total resistance with respect to the outer radius to zero; taught in [Heat transfer](12-heat-transfer.md).

Example. Insulation with $k_{\text{th}} = 0.05$ W/(m K) in still air with $h_c = 10$ $\text{W/(m}^2\text{ K)}$ has the radii below. Results: 5.0 mm for the cylinder and 10 mm for the sphere. A wire or small tube below that radius loses more heat when insulated.

```verify
k = q(0.05, "W/m K")
h = q(10, "W/m^2 K")
expect(k / h, "5.0 mm")
expect(2 * k / h, "10 mm")
```

## Fins

### Straight fin of uniform cross section

A fin extends a surface into a fluid. Its performance is set by the fin parameter $m$ and the tip condition.

$$
m = \sqrt{\frac{h_c P}{k_{\text{th}} A_c}}, \qquad \dot{Q}_{\text{long}} = \sqrt{h_c P k_{\text{th}} A_c}\,\theta_b, \qquad \dot{Q}_{\text{adiab}} = \sqrt{h_c P k_{\text{th}} A_c}\,\theta_b \tanh(mL)
$$

$$
\eta_f = \frac{\tanh(mL)}{mL}, \qquad \varepsilon_{\text{fin}} = \frac{\dot{Q}_f}{h_c A_c \theta_b}, \qquad L_c = L + \frac{A_c}{P}
$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $m$ | fin parameter | 1/m |
| $h_c$ | convection coefficient on the fin | $\text{W/m}^{2}\text{ K}$ |
| $P$ | fin perimeter | m |
| $A_c$ | cross-section area of the fin | $\text{m}^{2}$ |
| $k_{\text{th}}$ | fin conductivity | W/m K |
| $\theta_b$ | base excess temperature $T_b - T_\infty$ | K |
| $L$ | fin length | m |
| $L_c$ | corrected length for a convecting tip | m |
| $\dot{Q}_{\text{long}}$, $\dot{Q}_{\text{adiab}}$, $\dot{Q}_f$ | fin heat rate: infinitely long, adiabatic tip, general | W |
| $\eta_f$ | fin efficiency | dimensionless |
| $\varepsilon_{\text{fin}}$ | fin effectiveness | dimensionless |

Holds when: steady state, constant $k_{\text{th}}$ and $h_c$, a thin fin so temperature varies only along its length, and an adiabatic tip (or $L_c$ substituted for $L$ for a convecting tip). The long fin form needs $mL$ large (about 3 or more, where $\tanh(mL)$ is near 1).
Breaks when: the fin is thick (Biot number across the fin not small), $h_c$ varies along the fin, radiation from the fin is significant, or contact resistance at the base is ignored.
Source and basis: derived from the steady energy balance on a fin element, giving $d^2\theta/dx^2 = m^2\theta$; taught in [Heat transfer](12-heat-transfer.md).

Example. A pin fin of diameter 5 mm and length 50 mm with $k_{\text{th}} = 200$ W/(m K), $h_c = 25$ $\text{W/(m}^2\text{ K)}$, and $\theta_b = 60$ K. Results: $m = 10$ 1/m, $mL = 0.50$, heat rate 1.09 W, efficiency 0.924, effectiveness 37.0. Effectiveness well above 2 means the fin is worth adding.

```verify
d = q(5, "mm")
L = q(50, "mm")
k = q(200, "W/m K")
h = q(25, "W/m^2 K")
tb = q(60, "K")
P = pi * d
Ac = pi * d**2 / 4
m = sqrt(h * P / (k * Ac))
expect(m, "10 1/m")
expect(m * L, "0.50")
Mq = sqrt(h * P * k * Ac)
th = (exp(2 * m * L) - 1) / (exp(2 * m * L) + 1)
Qf = Mq * tb * th
expect(Qf, "1.09 W")
expect(th / (m * L), "0.924")
expect(Qf / (h * Ac * tb), "37.0")
```

## Transient conduction

### Biot number, lumped capacitance, and Fourier number

When a body's internal resistance is small against its surface resistance, it cools as one lump with a single time constant.

$$
\mathrm{Bi} = \frac{h_c L_c}{k_{\text{th}}}, \quad L_c = \frac{V}{A_s}, \qquad \frac{T - T_\infty}{T_i - T_\infty} = e^{-t/\tau}, \quad \tau = \frac{\rho V c}{h_c A_s}, \qquad \mathrm{Fo} = \frac{\alpha_{\text{th}} t}{L^{2}}
$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\mathrm{Bi}$ | Biot number | dimensionless |
| $\mathrm{Fo}$ | Fourier number | dimensionless |
| $h_c$ | convection coefficient | $\text{W/m}^{2}\text{ K}$ |
| $L_c$ | characteristic length, volume over surface area | m |
| $V$ | body volume | $\text{m}^{3}$ |
| $A_s$ | surface area exposed to the fluid | $\text{m}^{2}$ |
| $k_{\text{th}}$ | solid conductivity | W/m K |
| $T$, $T_i$, $T_\infty$ | body temperature now, initially, and of the fluid | K |
| $t$ | time | s |
| $\tau$ | thermal time constant | s |
| $\rho$ | solid density | $\text{kg/m}^{3}$ |
| $c$ | solid specific heat | J/kg K |
| $\alpha_{\text{th}}$ | thermal diffusivity | $\text{m}^{2}\text{/s}$ |
| $L$ | length scale for diffusion | m |

Holds when: $\mathrm{Bi}$ is below about 0.1 (a common rule, with a temperature error across the body of a few percent), constant $h_c$ and properties, and no internal generation.
Breaks when: $\mathrm{Bi}$ exceeds 0.1 (use the one-dimensional transient solutions and the Fourier number), $h_c$ changes during the transient (radiation, natural convection), or the body is large and its edges cool faster than its core.
Source and basis: derived from the energy balance $\rho V c\,dT/dt = -h_c A_s (T - T_\infty)$; taught in [Heat transfer](12-heat-transfer.md).

Example. An aluminium cube of side 50 mm ($k_{\text{th}} = 237$ W/(m K), $\rho = 2700$ $\text{kg/m}^3$, $c = 900$ J/(kg K)) in air with $h_c = 20$ $\text{W/(m}^2\text{ K)}$. Time to fall to one tenth of the initial excess temperature is $\tau$ times the natural logarithm of ten. Results: $L_c = 8.33$ mm, $\mathrm{Bi} = 7.03 \times 10^{-4}$, $\tau = 1.01 \times 10^{3}$ s, and $2.33 \times 10^{3}$ s to a tenth.

```verify
a = q(50, "mm")
Lc = a**3 / (6 * a**2)
expect(Lc, "8.33 mm")
h = q(20, "W/m^2 K")
Bi = h * Lc / q(237, "W/m K")
expect(Bi, "7.03e-4")
tau = q(2700, "kg/m^3") * q(900, "J/kg K") * Lc / h
expect(tau, "1.01e3 s")
expect(tau * log(10), "2.33e3 s")
```

### Semi-infinite solid

Conduction into a body so thick that the far side is never reached during the time of interest, after a step change of surface temperature to $T_s$.

$$
\frac{T(x,t) - T_s}{T_i - T_s} = \operatorname{erf}\!\left(\frac{x}{2\sqrt{\alpha_{\text{th}}t}}\right), \qquad q''_s = \frac{k_{\text{th}}\,(T_s - T_i)}{\sqrt{\pi\,\alpha_{\text{th}}\,t}}
$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $T(x,t)$ | temperature at depth $x$ and time $t$ | K |
| $T_s$ | imposed surface temperature | K |
| $T_i$ | initial uniform temperature | K |
| $x$ | depth below the surface | m |
| $t$ | time since the step | s |
| $\alpha_{\text{th}}$ | thermal diffusivity | $\text{m}^{2}\text{/s}$ |
| $k_{\text{th}}$ | thermal conductivity | W/m K |
| $q''_s$ | surface heat flux | $\text{W/m}^{2}$ |

Holds when: constant properties, one-dimensional conduction, uniform initial temperature, and a body thick compared with the penetration depth $2\sqrt{\alpha_{\text{th}}t}$.
Breaks when: the penetration depth reaches the body thickness (use the finite-slab solution), the surface has a contact or film resistance (use the convective-boundary solution), or properties vary with temperature.
Source and basis: derived from the heat equation by the similarity variable $x/\sqrt{\alpha_{\text{th}}t}$.

Example. Soil-like solid with $k_{\text{th}} = 1.0$ W/(m K), $\alpha_{\text{th}} = 5 \times 10^{-7}$ $\text{m}^2\text{/s}$, surface 20 K above the initial temperature, for 3600 s. Results: surface flux 266 $\text{W/m}^2$ and penetration depth 0.0849 m.

```verify
k = q(1.0, "W/m K")
al = q(5e-7, "m^2/s")
t = q(3600, "s")
dT = q(20, "K")
expect(k * dT / sqrt(pi * al * t), "266 W/m^2")
expect(2 * sqrt(al * t), "0.0849 m")
```

## Convection groups and laminar internal flow

### Dimensionless groups

The groups below define the regime and the form of every convection correlation.

$$
\mathrm{Re} = \frac{\rho V D}{\mu}, \qquad \mathrm{Pr} = \frac{\nu_k}{\alpha_{\text{th}}} = \frac{\mu c_p}{k_{\text{th}}}, \qquad \mathrm{Nu} = \frac{h_c D}{k_{\text{th}}}, \qquad \mathrm{St} = \frac{\mathrm{Nu}}{\mathrm{Re}\,\mathrm{Pr}}
$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\mathrm{Re}$ | Reynolds number, inertia over viscous force | dimensionless |
| $\mathrm{Pr}$ | Prandtl number, momentum over thermal diffusivity | dimensionless |
| $\mathrm{Nu}$ | Nusselt number, convective over conductive transfer in the fluid | dimensionless |
| $\mathrm{St}$ | Stanton number | dimensionless |
| $\rho$ | fluid density | $\text{kg/m}^{3}$ |
| $V$ | characteristic velocity | m/s |
| $D$ | characteristic length (diameter, plate length) | m |
| $\mu$ | dynamic viscosity | Pa s |
| $\nu_k$ | kinematic viscosity | $\text{m}^{2}\text{/s}$ |
| $c_p$ | fluid specific heat | J/kg K |
| $k_{\text{th}}$ | fluid conductivity | W/m K |
| $\alpha_{\text{th}}$ | fluid thermal diffusivity | $\text{m}^{2}\text{/s}$ |
| $h_c$ | convection coefficient | $\text{W/m}^{2}\text{ K}$ |

Holds when: the length used in $\mathrm{Re}$ and $\mathrm{Nu}$ is the same one stated by the correlation, and $k_{\text{th}}$ in $\mathrm{Nu}$ is the fluid's.
Breaks when: the length is mismatched (diameter in one place, hydraulic diameter in another), or fluid properties are taken at the wrong reference temperature (film temperature for external flow, bulk mean for internal flow, as each correlation states).
Source and basis: definitions; the groups arise from nondimensionalizing the momentum and energy equations, see [Heat transfer](12-heat-transfer.md) and [Thermal-fluids reference](reference-thermofluids.md#dimensionless-numbers).

### Fully developed laminar flow in a circular tube

After the entry region, laminar flow in a circular tube has a constant Nusselt number set only by the wall condition.

$$
\mathrm{Nu}_D = 3.66 \ (\text{constant wall temperature}), \qquad \mathrm{Nu}_D = 4.36 \ (\text{constant wall heat flux}), \qquad h_c = \frac{\mathrm{Nu}_D\,k_{\text{th}}}{D}
$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\mathrm{Nu}_D$ | Nusselt number based on tube diameter | dimensionless |
| $h_c$ | convection coefficient | $\text{W/m}^{2}\text{ K}$ |
| $k_{\text{th}}$ | fluid conductivity at the bulk mean temperature | W/m K |
| $D$ | tube inner diameter | m |

Holds when: the flow is laminar ($\mathrm{Re}_D$ below about 2300), thermally and hydrodynamically fully developed, in a circular tube with constant properties, and the wall condition is uniform temperature or uniform flux. The values do not depend on $\mathrm{Re}$ or $\mathrm{Pr}$ once the flow is developed.
Breaks when: the flow is in the entry region (local and average $\mathrm{Nu}$ are higher), the tube is not circular (the constant changes with shape), properties vary strongly across the tube, or the flow is turbulent.
Source and basis: Lienhard, Chapter 7, eqns. (7.22) and (7.23) [src](../data/claims/heat-transfer.md#lienhard-laminar-pipe-nu): the constant is 4.364 for uniform wall heat flux and 3.657 for uniform wall temperature; derived from the exact solution of the energy equation with the parabolic velocity profile, taught in [Heat transfer](12-heat-transfer.md).

Example. A 20 mm tube with a fluid of $k_{\text{th}} = 0.6$ W/(m K) in fully developed laminar flow. Results: 110 $\text{W/(m}^2\text{ K)}$ at constant wall temperature and 131 $\text{W/(m}^2\text{ K)}$ at constant flux.

```verify
k = q(0.6, "W/m K")
D = q(20, "mm")
expect(q(3.66, "") * k / D, "110 W/m^2 K")
expect(q(4.36, "") * k / D, "131 W/m^2 K")
```

### Turbulent flow in a smooth circular pipe

Nusselt number for fully developed turbulent flow. The Colburn and Dittus-Boelter power laws are the simple forms; Gnielinski's equation covers the wider range and uses the smooth-pipe friction factor $f$ from Filonenko's equation.

$$
\mathrm{Nu}_D = 0.023\,\mathrm{Re}_D^{0.8}\,\mathrm{Pr}^{1/3} \quad (\text{Colburn}), \qquad \mathrm{Nu}_D = 0.0243\,\mathrm{Re}_D^{0.8}\,\mathrm{Pr}^{0.4} \quad (\text{Dittus-Boelter, heating})
$$

$$
\mathrm{Nu}_D = \frac{(f/8)\,(\mathrm{Re}_D - 1000)\,\mathrm{Pr}}{1 + 12.7\sqrt{f/8}\,\left(\mathrm{Pr}^{2/3} - 1\right)}, \qquad f = \frac{1}{\left(1.82\,\log_{10}\mathrm{Re}_D - 1.64\right)^{2}}
$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\mathrm{Nu}_D$ | Nusselt number $h_c D/k_{\text{th}}$ | dimensionless |
| $\mathrm{Re}_D$ | Reynolds number based on pipe diameter and mean velocity | dimensionless |
| $\mathrm{Pr}$ | Prandtl number | dimensionless |
| $f$ | Darcy-Weisbach friction factor, smooth pipe | dimensionless |

Holds when: smooth circular pipe, fully developed turbulent flow, uniform wall temperature or uniform wall heat flux, and all properties evaluated at the local bulk temperature. The power laws need a Reynolds number of at least 10000, and the source reports errors up to +25 percent and -40 percent for Prandtl numbers from 0.67 to 100. Gnielinski's equation holds for $2300 \le \mathrm{Re}_D \le 5 \times 10^{6}$ and $0.6 \le \mathrm{Pr} \le 10^{5}$ and reproduces more than 90 percent of the liquid data within 20 percent.
Breaks when: the wall is rough (the friction factor and the sublayer term change), the wall-to-bulk temperature difference is large enough to change properties across the pipe, the pipe is short (entry region), or the flow is laminar or in early transition for the power laws. Dittus-Boelter eqn. (7.39b) is for heating. For a cooled wall or other large temperature difference, use Gnielinski's eqn. (7.41) with properties at the bulk temperature, then apply the source's correction: for liquids multiply by $(\mu_b/\mu_w)^n$, with $n = 0.11$ when $T_w < T_b$ and $n = 0.25$ when $T_w > T_b$, over $0.025 \le \mu_b/\mu_w \le 12.5$; for gases multiply by $(T_b/T_w)^n$, with $n = 0.47$ when $T_w < T_b$ and $n = 0$ when $T_w > T_b$, over $0.27 \le T_b/T_w \le 2.7$ [src](../data/claims/heat-transfer.md#lienhard-turbulent-pipe-property-correction).
Source and basis: Lienhard, Chapter 7, section 7.3, eqns. (7.38), (7.39a), (7.39b), (7.41), and (7.42), pp. 368 to 369 [src](../data/claims/heat-transfer.md#lienhard-turbulent-pipe): the Colburn constant 0.023 and the Dittus-Boelter constant 0.0243 with exponent 0.4. Gnielinski's constants 12.7 and 1000 and Filonenko's 1.82 and 1.64 [src](../data/claims/heat-transfer.md#lienhard-gnielinski), valid from 2300 upward.

Example. $\mathrm{Re}_D = 5 \times 10^{4}$, $\mathrm{Pr} = 7$, fluid conductivity 0.6 W/(m K), 20 mm pipe. Results: Colburn $\mathrm{Nu}_D = 253$; Gnielinski $f = 0.0209$, $\mathrm{Nu}_D = 329$, and $h_c = 9870$ $\text{W/(m}^2\text{ K)}$.

```verify
Re = q(5e4, "")
Pr = q(7, "")
k = q(0.6, "W/m K")
D = q(20, "mm")
expect(0.023 * Re**0.8 * Pr**(1 / 3), "253")
f = 1 / (1.82 * log10(Re) - 1.64)**2
expect(f, "0.0209")
Nu = (f / 8) * (Re - 1000) * Pr / (1 + 12.7 * sqrt(f / 8) * (Pr**(2 / 3) - 1))
expect(Nu, "329")
expect(Nu * k / D, "9870 W/m^2 K")
```

## Forced convection over external surfaces

### Flat plate, laminar boundary layer

Average Nusselt number over a plate of length $L$ with an isothermal wall and a laminar boundary layer from the leading edge.

$$
\mathrm{Nu}_L = \frac{h_c L}{k_{\text{th}}} = 0.664\,\mathrm{Re}_L^{1/2}\,\mathrm{Pr}^{1/3}
$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\mathrm{Nu}_L$ | average Nusselt number over the plate | dimensionless |
| $h_c$ | average convection coefficient | $\text{W/m}^{2}\text{ K}$ |
| $L$ | plate length in the flow direction | m |
| $k_{\text{th}}$ | fluid conductivity | W/m K |
| $\mathrm{Re}_L$ | Reynolds number at the plate end, $uL/\nu_k$ | dimensionless |
| $\mathrm{Pr}$ | Prandtl number | dimensionless |

Holds when: two-dimensional incompressible laminar flow on a flat isothermal wall from the leading edge, $\mathrm{Pr} \ge 0.6$, $\mathrm{Re}_L$ below the transition value (typically over about $10^{5}$), Mach number below about 0.3, small viscous heating, and properties at the film temperature $(T_w + T_\infty)/2$.
Breaks when: the boundary layer is tripped or turbulent, there is a strong pressure gradient, the wall is not isothermal near the leading edge, or the plate has an unheated starting length. For liquid metals ($\mathrm{Pr}$ much below 0.6) the source gives a different relation, $\mathrm{Nu}_L = 1.13\,\mathrm{Pe}_L^{1/2}$.
Source and basis: Lienhard, Chapter 6, eqn. (6.68) and the film-temperature rule after eqn. (6.43) [src](../data/claims/heat-transfer.md#lienhard-plate-laminar): the constant 0.664 follows from integrating the local 0.332 over the plate, and the average is twice the end value.

Example. $\mathrm{Re}_L = 1 \times 10^{5}$ and $\mathrm{Pr} = 0.71$ give $\mathrm{Nu}_L = 187$.

```verify
expect(0.664 * sqrt(q(1e5, "")) * q(0.71, "")**(1 / 3), "187")
```

### Flat plate, turbulent boundary layer

Local Nusselt number $\mathrm{Nu}_x = h_c(x)\,x/k_{\text{th}}$ in a fully turbulent boundary layer from the Reynolds-Colburn analogy, with the skin friction coefficient $C_f$ of White, and two simpler power laws.

$$
\mathrm{St}_x = \frac{\mathrm{Nu}_x}{\mathrm{Re}_x\,\mathrm{Pr}} = \frac{C_f/2}{1 + 12.7\sqrt{C_f/2}\,\left(\mathrm{Pr}^{2/3} - 1\right)}, \qquad C_f = \frac{0.455}{\left[\ln(0.06\,\mathrm{Re}_x)\right]^{2}}
$$

$$
\mathrm{Nu}_x = 0.0296\,\mathrm{Re}_x^{0.8}\,\mathrm{Pr}^{0.6} \ (\text{gases}), \qquad \mathrm{Nu}_x = 0.032\,\mathrm{Re}_x^{0.8}\,\mathrm{Pr}^{0.43} \ (\text{nonmetallic liquids})
$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\mathrm{St}_x$ | local Stanton number | dimensionless |
| $\mathrm{Nu}_x$ | local Nusselt number | dimensionless |
| $\mathrm{Re}_x$ | Reynolds number at distance $x$ from the leading edge | dimensionless |
| $\mathrm{Pr}$ | Prandtl number | dimensionless |
| $C_f$ | local skin friction coefficient | dimensionless |

Holds when: smooth wall, zero or mild pressure gradient, and either uniform wall temperature or uniform wall heat flux. The analogy needs a Prandtl number of at least 0.5 and its air data scatter has a standard deviation of 5.5 percent. Properties are taken at the film temperature $(T_w + T_\infty)/2$ unless the variable-property correction below is used. The gas power law was fitted to air. The liquid power law fitted water and an oil up to $\mathrm{Pr}$ of 85 within about 15 percent and overpredicts air by 15 to 25 percent.
Breaks when: the boundary layer is still laminar or in transition (use the transition methods of the source section 6.9), the wall is rough, a large wall-to-stream temperature difference changes the properties, or the gas power law is used on a liquid. For a large temperature difference, evaluate the other properties at the free-stream temperature $T_\infty$ and apply the source's correction instead of using film-temperature properties: multiply by $(\mathrm{Pr}/\mathrm{Pr}_w)^{1/4}$ for liquids or $(T_\infty/T_w)^{0.4}$ for gases.
Source and basis: Lienhard, Chapter 6, eqns. (6.102), (6.111), (6.112), and (6.113) [src](../data/claims/heat-transfer.md#lienhard-plate-turbulent): White's constants 0.455 and 0.06, the sublayer constant 12.7, and the power-law constants 0.0296 with exponent 0.6 and 0.032 with exponent 0.43.

Example. Water at $\mathrm{Re}_x = 2.371 \times 10^{6}$, $\mathrm{Pr} = 7.66$, conductivity 0.5927 W/(m K), at $x = 1.0$ m. Results: $C_f = 0.00323$, $h_c = 7033$ $\text{W/(m}^2\text{ K)}$ from the analogy and 5730 $\text{W/(m}^2\text{ K)}$ from the liquid power law. A gas at $\mathrm{Re}_x = 1 \times 10^{6}$ and $\mathrm{Pr} = 0.71$ gives $\mathrm{Nu}_x = 1521$ from the gas power law.

```verify
Re = q(2.371e6, "")
Pr = q(7.66, "")
k = q(0.5927, "W/m K")
x = q(1.0, "m")
Cf = 0.455 / log(0.06 * Re)**2
expect(Cf, "0.00323")
St = (Cf / 2) / (1 + 12.7 * sqrt(Cf / 2) * (Pr**(2 / 3) - 1))
expect(St * Re * Pr * k / x, "7033 W/m^2 K")
expect(0.032 * Re**0.8 * Pr**0.43 * k / x, "5730 W/m^2 K")
expect(0.0296 * q(1e6, "")**0.8 * q(0.71, "")**0.6, "1521")
```

### Cylinder in crossflow

Average Nusselt number for a cylinder of diameter $D$ in a normal stream, from Churchill and Bernstein, covering the whole range of the available data.

$$
\mathrm{Nu}_D = 0.3 + \frac{0.62\,\mathrm{Re}_D^{1/2}\,\mathrm{Pr}^{1/3}}{\left[1 + (0.4/\mathrm{Pr})^{2/3}\right]^{1/4}}\left[1 + \left(\frac{\mathrm{Re}_D}{282\,000}\right)^{5/8}\right]^{4/5}
$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\mathrm{Nu}_D$ | average Nusselt number based on cylinder diameter | dimensionless |
| $\mathrm{Re}_D$ | Reynolds number from free-stream velocity and diameter | dimensionless |
| $\mathrm{Pr}$ | Prandtl number | dimensionless |

Holds when: a single smooth cylinder in a steady normal stream, the product $\mathrm{Pe}_D = \mathrm{Re}_D\,\mathrm{Pr}$ above 0.2, and all properties at the film temperature $(T_w + T_\infty)/2$.
Breaks when: $\mathrm{Pe}_D$ is 0.2 or below (the source gives a separate relation), the stream is turbulent or the cylinder is in a tube bank, or the flow is inclined. The equation underpredicts most data by about 20 percent for $40\,000 < \mathrm{Re}_D < 400\,000$, where the source recommends the same form with the exponent $1/2$ in place of $5/8$ and $4/5$ removed.
Source and basis: Lienhard, Chapter 7, section 7.6, eqns. (7.65) to (7.68), pp. 390 to 391 [src](../data/claims/heat-transfer.md#lienhard-churchill-bernstein): the constants 0.3, 0.62, 0.4, and 282000, with the exponents 1/2, 1/3, 5/8, and 4/5.

Example. $\mathrm{Re}_D = 5 \times 10^{3}$ and $\mathrm{Pr} = 0.71$ give $\mathrm{Nu}_D = 36.8$.

```verify
Re = q(5e3, "")
Pr = q(0.71, "")
Nu = 0.3 + 0.62 * sqrt(Re) * Pr**(1 / 3) / (1 + (0.4 / Pr)**(2 / 3))**0.25 * (1 + (Re / 282000)**(5 / 8))**0.8
expect(Nu, "36.8")
```

## Natural convection

### Grashof and Rayleigh numbers

Natural convection is driven by buoyancy from density differences caused by temperature. $\mathrm{Gr}$ measures buoyancy against viscous force, and $\mathrm{Ra}$ sets the regime of the boundary layer.

$$
\mathrm{Gr}_L = \frac{g\,\beta\,\Delta T\,L^{3}}{\nu_k^{2}}, \qquad \mathrm{Ra}_L = \mathrm{Gr}_L\,\mathrm{Pr} = \frac{g\,\beta\,\Delta T\,L^{3}}{\nu_k\,\alpha_{\text{th}}}, \qquad \beta_{\text{ideal gas}} = \frac{1}{T}
$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\mathrm{Gr}_L$ | Grashof number | dimensionless |
| $\mathrm{Ra}_L$ | Rayleigh number | dimensionless |
| $g$ | local gravitational acceleration | $\text{m/s^2}$ |
| $\beta$ | volumetric thermal expansion coefficient | 1/K |
| $\Delta T$ | surface to fluid temperature difference | K |
| $L$ | characteristic length (plate height) | m |
| $\nu_k$ | kinematic viscosity | $\text{m}^{2}\text{/s}$ |
| $\alpha_{\text{th}}$ | thermal diffusivity | $\text{m}^{2}\text{/s}$ |
| $T$ | absolute fluid temperature | K |
| $\mathrm{Pr}$ | Prandtl number | dimensionless |

Holds when: the density change is small enough that the Boussinesq approximation applies, properties are evaluated at the film temperature, and $\beta = 1/T$ is used only for an ideal gas.
Breaks when: temperature differences are large against the absolute temperature, the fluid is near its critical point or a density maximum (water near 4 degrees Celsius), or gravity is near zero, where there is no buoyancy-driven flow.
Source and basis: derived from the Boussinesq momentum equation; taught in [Heat transfer](12-heat-transfer.md).

Example (Earth). A vertical plate 0.3 m high, 30 K warmer than air at a 300 K film temperature, with assumed air values $\nu_k = 1.6 \times 10^{-5}$ $\text{m}^2\text{/s}$ and $\alpha_{\text{th}} = 2.2 \times 10^{-5}$ $\text{m}^2\text{/s}$, on Earth with standard gravity. Results: $\mathrm{Ra}_L = 7.52 \times 10^{7}$ and $\mathrm{Pr} = 0.727$.

```verify
g = q(9.80665, "m/s^2", of="g_standard")
beta = 1 / q(300, "K")
dT = q(30, "K")
L = q(0.3, "m")
nu = q(1.6e-5, "m^2/s")
al = q(2.2e-5, "m^2/s")
Ra = g * beta * dT * L**3 / (nu * al)
expect(Ra, "7.52e7")
expect(nu / al, "0.727")
```

### Vertical isothermal plate

Average Nusselt number for natural convection on a vertical plate of height $L$, from Churchill and Chu. The first form is the more accurate for laminar flow; the second covers all conditions.

$$
\mathrm{Nu}_L = 0.68 + \frac{0.670\,\mathrm{Ra}_L^{1/4}}{\left[1 + (0.492/\mathrm{Pr})^{9/16}\right]^{4/9}}, \qquad \mathrm{Nu}_L = \left\{0.825 + \frac{0.387\,\mathrm{Ra}_L^{1/6}}{\left[1 + (0.492/\mathrm{Pr})^{9/16}\right]^{8/27}}\right\}^{2}
$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\mathrm{Nu}_L$ | average Nusselt number $h_c L/k_{\text{th}}$ | dimensionless |
| $\mathrm{Ra}_L$ | Rayleigh number based on plate height | dimensionless |
| $\mathrm{Pr}$ | Prandtl number | dimensionless |

Holds when: a vertical isothermal plate (or uniform heat flux) in an extensive quiescent fluid, properties at the film temperature $(T_w + T_\infty)/2$. The first form is for $\mathrm{Ra}_L \le 10^{9}$ (laminar). The second holds for all $\mathrm{Ra}_L$ and $\mathrm{Pr}$.
Breaks when: the plate is inclined or short against its boundary-layer thickness, the surroundings are confined, or the temperature difference is large enough that the film-temperature property rule fails. Above $\mathrm{Ra}_L$ of about $10^{9}$ the first form lies on the low side of the data. Measured $\mathrm{Nu}_L$ scatters substantially once the boundary layer is turbulent.
Source and basis: Lienhard, Chapter 8, section 8.3, eqns. (8.13a) and (8.13b), pp. 419 to 420 [src](../data/claims/heat-transfer.md#lienhard-churchill-chu): the constants 0.68, 0.670, 0.492 in the laminar form, and 0.825 and 0.387 in the all-range form, fitted to data from 13 independent studies.

Example. $\mathrm{Ra}_L = 6.78 \times 10^{7}$ and $\mathrm{Pr} = 0.710$ give $\mathrm{Nu}_L = 47.3$ from the laminar form and $54.4$ from the all-range form.

```verify
Ra = q(6.78e7, "")
Pr = q(0.710, "")
expect(0.68 + 0.670 * Ra**0.25 / (1 + (0.492 / Pr)**(9 / 16))**(4 / 9), "47.3")
expect((0.825 + 0.387 * Ra**(1 / 6) / (1 + (0.492 / Pr)**(9 / 16))**(8 / 27))**2, "54.4")
```

## Boiling and condensation

Boiling heat flux rises steeply with the excess of wall temperature over saturation temperature through four regimes. Natural convection boiling comes first at small excess temperature. Nucleate boiling follows, where bubbles form at the wall and give very high $h_c$. The critical heat flux is the peak of nucleate boiling; past it, a vapor film starts to blanket the wall, flux drops through transition boiling, and film boiling gives low $h_c$ and a wall temperature far above saturation.

- In a heat-flux-controlled device (an electric heater, a nuclear fuel rod) the wall temperature jumps from the nucleate range to the film range once the critical heat flux is exceeded, and the surface can burn out. Design with a margin below the critical heat flux.
- Condensation is filmwise when the liquid wets the surface and forms a continuous film whose thickness is the main resistance. It is dropwise when the surface is not wetted; $h_c$ is then much higher.
- Both processes occur at nearly constant fluid temperature (the saturation temperature at the local pressure), so a boiling or condensing stream has an effective heat capacity rate that is very large, which sets $C_r \to 0$ in exchanger calculations.
- Correlations for nucleate boiling and condensation depend on fluid and surface and are not given here; the peak heat flux is below.

### Peak pool boiling heat flux

The peak (critical) heat flux on a large horizontal flat plate in saturated pool boiling, where the vapor columns become unstable and a vapor film starts to cover the heater.

$$
q''_{\max} = 0.149\,\rho_g^{1/2}\,h_{fg}\,\left[\sigma\,g\,(\rho_f - \rho_g)\right]^{1/4}
$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $q''_{\max}$ | peak heat flux | $\text{W/m}^{2}$ |
| $\rho_g$ | saturated vapor density | $\text{kg/m}^{3}$ |
| $\rho_f$ | saturated liquid density | $\text{kg/m}^{3}$ |
| $h_{fg}$ | latent heat of vaporization | J/kg |
| $\sigma$ | liquid-vapor surface tension | N/m |
| $g$ | local gravitational acceleration | $\text{m/s}^{2}$ |

Holds when: a horizontal flat well-wetted heater large enough for a few vapor-jet wavelengths (the source gives a width of about three times the jet spacing $d_1$ or more), with side walls so that no side flow is entrained, in a saturated pool, with properties at the saturation temperature.
Breaks when: the heater is narrower than about $3d_1$, where the actual peak first falls below this prediction as the heater shrinks, then rises once a single vapor column serves a sufficiently small area [src](../data/claims/heat-transfer.md#lienhard-chf-small-heater); the correlation also changes for a partly wetted heater, one without side walls, or forced or subcooled boiling. The source's Zuber-Kutateladze form with constant 0.131 is lower by 14 percent and cannot be applied directly to any actual configuration.
Source and basis: Lienhard, Chapter 9, section 9.3, eqn. (9.11), p. 493, and eqn. (9.12) [src](../data/claims/heat-transfer.md#lienhard-chf): the constant 0.149 for the hydrodynamic peak and 0.131 for the Zuber-Kutateladze value. Wall temperature rise past the peak under controlled heat flux is derived from the energy balance; the source's nucleate boiling and film condensation correlations are not reproduced here.

Example (Earth, standard gravity). Water at saturation at 1 atm: $\rho_f = 958.2$ $\text{kg/m}^3$, $\rho_g = 0.597$ $\text{kg/m}^3$, $h_{fg} = 2257$ kJ/kg, $\sigma = 0.0589$ N/m. Results: $q''_{\max} = 1.26$ $\text{MW/m}^2$ and, with the constant 0.131, 1.11 $\text{MW/m}^2$.

```verify
rf = q(958.2, "kg/m^3")
rg = q(0.597, "kg/m^3")
hfg = q(2257, "kJ/kg")
sg = q(0.0589, "N/m")
g = q(9.80665, "m/s^2", of="g_standard")
expect(0.149 * sqrt(rg) * hfg * (sg * g * (rf - rg))**0.25, "1.26 MW/m^2")
expect(q(0.131, "") * sqrt(rg) * hfg * (sg * g * (rf - rg))**0.25, "1.11 MW/m^2")
```


## Radiation exchange

### Blackbody emission and gray surfaces

A blackbody absorbs all incident radiation and emits the maximum possible at its temperature. A real surface emits a fraction $\epsilon_{\text{rad}}$ of that.

$$
E_b = \sigma T^{4}, \qquad E = \epsilon_{\text{rad}}\,\sigma T^{4}, \qquad \dot{Q}_{\text{net}} = \epsilon_{\text{rad}}\,\sigma A\,(T_s^{4} - T_{\text{sur}}^{4})
$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $E_b$ | blackbody emissive power | $\text{W/m}^{2}$ |
| $E$ | emissive power of a gray surface | $\text{W/m}^{2}$ |
| $\sigma$ | Stefan-Boltzmann constant | $\text{W/m}^{2}\text{ K}^{4}$ |
| $T$, $T_s$, $T_{\text{sur}}$ | absolute temperature of the surface, and of its surroundings | K |
| $\epsilon_{\text{rad}}$ | emissivity | dimensionless |
| $A$ | surface area | $\text{m}^{2}$ |
| $\dot{Q}_{\text{net}}$ | net radiative heat rate from the surface | W |

Holds when: the surface is gray and diffuse (emissivity and absorptivity equal and independent of wavelength and direction), the surroundings are much larger than the surface and isothermal, and temperatures are absolute.
Breaks when: the surface is selective (solar absorptivity differs from low-temperature emissivity, as on many coatings), the medium between surfaces absorbs or scatters (combustion gases, water vapor, dust), or the surroundings are not large against the surface (use the enclosure equation).
Source and basis: Stefan-Boltzmann law, derived from Planck's law integrated over wavelength; the net exchange is proportional to emissivity and the difference of fourth powers of absolute temperature [src](../data/claims/heat-transfer.md#openstax-radiation-form).

Example. A surface of 2.0 $\text{m}^2$ with $\epsilon_{\text{rad}} = 0.8$ at 350 K facing surroundings at 300 K. Results: 627 W, a flux of 313 $\text{W/m}^2$.

```verify
sg = q(5.670374419e-8, "W/m^2 K^4", of="sigma_sb")
A = q(2.0, "m^2")
Qn = q(0.8, "") * sg * A * (q(350, "K")**4 - q(300, "K")**4)
expect(Qn, "627 W")
expect(Qn / A, "313 W/m^2")
```

### View factors and the two-surface enclosure

The **view factor** $F_{12}$ is the fraction of radiation leaving surface 1 that strikes surface 2. For two gray diffuse isothermal surfaces forming a closed enclosure, the net exchange follows from a surface and a space resistance network.

$$
A_1 F_{12} = A_2 F_{21}, \qquad \sum_j F_{ij} = 1
$$

$$
\dot{Q}_{12} = \frac{\sigma\,(T_1^{4} - T_2^{4})}{\dfrac{1 - \epsilon_1}{\epsilon_1 A_1} + \dfrac{1}{A_1 F_{12}} + \dfrac{1 - \epsilon_2}{\epsilon_2 A_2}}
$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $F_{12}$, $F_{21}$ | view factor from 1 to 2 and from 2 to 1 | dimensionless |
| $F_{ij}$ | view factor from surface $i$ to surface $j$ | dimensionless |
| $A_1$, $A_2$ | areas of the two surfaces | $\text{m}^{2}$ |
| $\epsilon_1$, $\epsilon_2$ | emissivities of the two surfaces | dimensionless |
| $T_1$, $T_2$ | absolute temperatures | K |
| $\sigma$ | Stefan-Boltzmann constant | $\text{W/m}^{2}\text{ K}^{4}$ |
| $\dot{Q}_{12}$ | net radiative heat rate from 1 to 2 | W |

Holds when: both surfaces are gray, diffuse, and isothermal, they form a closed enclosure (the two surfaces see only each other), and the medium is transparent. A convex inner body enclosed by a larger surface has $F_{12} = 1$. Two large parallel plates have $A_1 = A_2$ and $F_{12} = 1$.
Breaks when: more than two surfaces take part (solve the full radiosity network), a surface is not isothermal, or the medium participates in radiation.
Source and basis: reciprocity and summation derived from the geometry of the definition of $F$ and conservation of radiant energy; the network from the radiosity-irradiation balance.

Example. Inner sphere of radius 0.1 m at 400 K with $\epsilon_1 = 0.5$ enclosed by a sphere of radius 0.3 m at 300 K with $\epsilon_2 = 0.8$. Result: 61.5 W.

```verify
sg = q(5.670374419e-8, "W/m^2 K^4", of="sigma_sb")
A1 = 4 * pi * q(0.1, "m")**2
A2 = 4 * pi * q(0.3, "m")**2
e1 = q(0.5, "")
e2 = q(0.8, "")
R = (1 - e1) / (e1 * A1) + 1 / A1 + (1 - e2) / (e2 * A2)
Q = sg * (q(400, "K")**4 - q(300, "K")**4) / R
expect(Q, "61.5 W")
```

### Radiation shield between parallel plates

A thin shield of low emissivity placed between two parallel plates adds two surface resistances and one more space resistance in series.

$$
\frac{\dot{Q}}{A} = \frac{\sigma\,(T_1^{4} - T_2^{4})}{\left(\dfrac{1}{\epsilon_1} + \dfrac{1}{\epsilon_2} - 1\right) + \left(\dfrac{1}{\epsilon_{3,1}} + \dfrac{1}{\epsilon_{3,2}} - 1\right)}
$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\dot{Q}/A$ | net radiative flux between the plates | $\text{W/m}^{2}$ |
| $T_1$, $T_2$ | absolute temperatures of the outer plates | K |
| $\epsilon_1$, $\epsilon_2$ | emissivities of the outer plates | dimensionless |
| $\epsilon_{3,1}$, $\epsilon_{3,2}$ | emissivities of the two faces of the shield | dimensionless |
| $\sigma$ | Stefan-Boltzmann constant | $\text{W/m}^{2}\text{ K}^{4}$ |

Holds when: large parallel gray diffuse plates, a thin shield with no conduction through it, and no convection or conduction in the gap.
Breaks when: the gap is not evacuated or has convection (the shield then also blocks gas flow, which changes the result), the shield touches a plate, or edge losses matter.
Source and basis: derived from series radiation resistances; each added shield adds the second bracket.

Example. Plates at 600 K and 300 K with $\epsilon = 0.8$, with and without a shield of $\epsilon = 0.1$ on both faces. Results: 4593 $\text{W/m}^2$ bare and 336 $\text{W/m}^2$ shielded.

```verify
sg = q(5.670374419e-8, "W/m^2 K^4", of="sigma_sb")
dT4 = q(600, "K")**4 - q(300, "K")**4
e = q(0.8, "")
s = q(0.1, "")
base = 1 / e + 1 / e - 1
expect(sg * dT4 / base, "4593 W/m^2")
expect(sg * dT4 / (base + 1 / s + 1 / s - 1), "336 W/m^2")
```

## Heat exchangers

### Log mean temperature difference

For a heat exchanger with a nearly constant $U$, the duty is the product of $U$, the area, a mean temperature difference, and a correction for the flow arrangement.

$$
\dot{Q} = U A\,F\,\Delta T_{\text{lm}}, \qquad \Delta T_{\text{lm}} = \frac{\Delta T_1 - \Delta T_2}{\ln(\Delta T_1/\Delta T_2)}
$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\dot{Q}$ | heat transfer rate | W |
| $U$ | overall heat transfer coefficient | $\text{W/m}^{2}\text{ K}$ |
| $A$ | heat transfer area the $U$ is based on | $\text{m}^{2}$ |
| $F$ | correction factor for the flow arrangement | dimensionless |
| $\Delta T_{\text{lm}}$ | log mean temperature difference | K |
| $\Delta T_1$, $\Delta T_2$ | temperature differences between the streams at the two ends | K |

Holds when: steady flow, constant $U$ and specific heats, no heat loss to the surroundings, and negligible axial conduction. The factor $F$ is exactly 1 for pure counterflow, pure parallel flow, and a phase-change stream. For counterflow the two ends are (hot in, cold out) and (hot out, cold in); for parallel flow, (hot in, cold in) and (hot out, cold out).
Breaks when: $\Delta T_1 = \Delta T_2$ (the expression is then undefined, so use $\Delta T_1$), $U$ varies strongly along the exchanger, or outlet temperatures are unknown (use effectiveness-NTU). For shell-and-tube and crossflow units $F$ is below 1 and is read from a chart or formula for that arrangement.
Source and basis: derived from integrating the local energy balance along the exchanger with a constant $U$; taught in [Heat exchangers](../applications/thermal-fluid/05-heat-exchangers.md).

Example. Counterflow with end differences 80 K and 30 K and $UA = 4$ kW/K. Results: $\Delta T_{\text{lm}} = 51.0$ K and a duty of 204 kW.

```verify
d1 = q(80, "K")
d2 = q(30, "K")
lm = (d1 - d2) / log(d1 / d2)
expect(lm, "51.0 K")
expect(q(4000, "W/K") * lm, "204 kW")
```

### Effectiveness-NTU

Effectiveness is the actual heat transfer over the maximum possible, which is set by the smaller heat capacity rate.

$$
C_r = \frac{C_{\min}}{C_{\max}}, \qquad \mathrm{NTU} = \frac{UA}{C_{\min}}, \qquad \varepsilon_{\text{hx}} = \frac{\dot{Q}}{C_{\min}(T_{h,i} - T_{c,i})}
$$

$$
\varepsilon_{\text{counter}} = \frac{1 - e^{-\mathrm{NTU}(1 - C_r)}}{1 - C_r\,e^{-\mathrm{NTU}(1 - C_r)}}, \qquad \varepsilon_{\text{parallel}} = \frac{1 - e^{-\mathrm{NTU}(1 + C_r)}}{1 + C_r}
$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $C_{\min}$, $C_{\max}$ | smaller and larger capacity rate $\dot{m}c_p$ of the two streams | W/K |
| $C_r$ | capacity rate ratio | dimensionless |
| $\mathrm{NTU}$ | number of transfer units | dimensionless |
| $\varepsilon_{\text{hx}}$ | heat exchanger effectiveness | dimensionless |
| $UA$ | overall conductance | W/K |
| $T_{h,i}$, $T_{c,i}$ | hot and cold inlet temperatures | K |
| $\dot{Q}$ | heat transfer rate | W |

Holds when: the same assumptions as the log mean method. Special cases: $C_r = 1$ counterflow gives $\varepsilon_{\text{hx}} = \mathrm{NTU}/(1 + \mathrm{NTU})$; a boiling or condensing stream gives $C_r = 0$ and $\varepsilon_{\text{hx}} = 1 - e^{-\mathrm{NTU}}$ for every arrangement.
Breaks when: $C_r = 1$ in the counterflow expression as written (it is 0/0, use the special case), $U$ varies strongly, or the flow arrangement is not counterflow or parallel (use the relation for that arrangement).
Source and basis: derived from the energy balance and the same integration as the log mean method; taught in [Heat exchangers](../applications/thermal-fluid/05-heat-exchangers.md).

Example. $\mathrm{NTU} = 2$ and $C_r = 0.5$ with $C_{\min} = 2000$ W/K and a 60 K inlet difference. For the same $\mathrm{NTU}$, counterflow always gives the higher effectiveness. Results: counterflow 0.775, parallel 0.633, heat rate 93.0 kW for counterflow, 0.865 for a phase-change stream, and 0.667 for $C_r = 1$ counterflow.

```verify
N = q(2, "")
Cr = q(0.5, "")
ec = (1 - exp(-N * (1 - Cr))) / (1 - Cr * exp(-N * (1 - Cr)))
ep = (1 - exp(-N * (1 + Cr))) / (1 + Cr)
expect(ec, "0.775")
expect(ep, "0.633")
expect(ec * q(2000, "W/K") * q(60, "K"), "93.0 kW")
expect(1 - exp(-N), "0.865")
expect(N / (1 + N), "0.667")
```

## Mass-transfer analogies

### Schmidt and Sherwood numbers

Convective mass transfer from a surface follows the same equations as convective heat transfer, with concentration in place of temperature and the mass diffusivity in place of the thermal diffusivity.

$$
\mathrm{Sc} = \frac{\nu_k}{D_{AB}}, \qquad \mathrm{Sh} = \frac{h_m L}{D_{AB}}, \qquad \mathrm{Le} = \frac{\alpha_{\text{th}}}{D_{AB}} = \frac{\mathrm{Sc}}{\mathrm{Pr}}
$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\mathrm{Sc}$ | Schmidt number | dimensionless |
| $\mathrm{Sh}$ | Sherwood number, mass-transfer analogue of $\mathrm{Nu}$ | dimensionless |
| $\mathrm{Le}$ | Lewis number | dimensionless |
| $\nu_k$ | kinematic viscosity | $\text{m}^{2}\text{/s}$ |
| $D_{AB}$ | binary mass diffusivity of species A in B | $\text{m}^{2}\text{/s}$ |
| $h_m$ | convective mass-transfer coefficient | m/s |
| $L$ | characteristic length | m |
| $\alpha_{\text{th}}$ | thermal diffusivity | $\text{m}^{2}\text{/s}$ |
| $\mathrm{Pr}$ | Prandtl number | dimensionless |

Holds when: mass-transfer rates are low enough not to distort the flow, the geometry and boundary conditions match those of the heat transfer correlation, and there is no chemical reaction. Then a correlation $\mathrm{Nu} = f(\mathrm{Re}, \mathrm{Pr})$ becomes $\mathrm{Sh} = f(\mathrm{Re}, \mathrm{Sc})$ with the same function.
Breaks when: transfer rates are high (blowing or suction changes the boundary layer), buoyancy from composition differences matters, or the species reacts at or near the surface.
Source and basis: derived from the identical form of the energy and species equations; the diffusivity of a particular gas pair is a measured property.

Example. $\nu_k = 1.6 \times 10^{-5}$ $\text{m}^2\text{/s}$ and $D_{AB} = 2.4 \times 10^{-5}$ $\text{m}^2\text{/s}$ (water vapor in air at room temperature, assumed round values) give $\mathrm{Sc}$ below; with $\alpha_{\text{th}} = 2.2 \times 10^{-5}$ $\text{m}^2\text{/s}$ the Lewis number is near 1, so heat and mass transfer coefficients scale together. Results: $\mathrm{Sc} = 0.667$ and $\mathrm{Le} = 0.917$.

```verify
nu = q(1.6e-5, "m^2/s")
D = q(2.4e-5, "m^2/s")
al = q(2.2e-5, "m^2/s")
expect(nu / D, "0.667")
expect(al / D, "0.917")
```

### Heat and mass transfer analogy at low rates

When mass transfer is slow, the ratio of the heat transfer coefficient to the mass transfer conductance depends only on the Lewis number and the specific heat, not on the flow or the shape.

$$
\frac{h_c}{g_m\,c_p} = \mathrm{Le}^{2/3}
$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $h_c$ | convection coefficient | $\text{W/m}^{2}\text{ K}$ |
| $g_m$ | mass transfer conductance (mass flux per unit mass-fraction difference) | $\text{kg/m}^{2}\text{ s}$ |
| $c_p$ | specific heat of the gas mixture | J/kg K |
| $\mathrm{Le}$ | Lewis number $\alpha_{\text{th}}/D_{AB}$ | dimensionless |

Holds when: low-rate mass transfer, so the flow is not distorted, the Nusselt number follows $\mathrm{Re}^{a}\,\mathrm{Pr}^{b}$ with $b$ near $1/3$ (so the exponent on $\mathrm{Le}$ is $1 - b$), and the geometry is the same for heat and mass transfer.
Breaks when: transfer rates are high, the Prandtl exponent differs from $1/3$, or the species react at the surface.
Source and basis: Lienhard, Chapter 11, section 11.7, eqn. (11.73) [src](../data/claims/heat-transfer.md#lienhard-lewis-analogy): the Lewis relation, in the general form with the 2/3 exponent, as proposed by Chilton and Colburn, with a Lewis number of about 0.847 for air and water.

Example. For $\mathrm{Le} = 0.847$ the ratio is 0.895.

```verify
expect(q(0.847, "")**(2 / 3), "0.895")
```

## Checklists

Before trusting a heat-transfer result:

- Absolute temperature used in every radiation term and in $\beta = 1/T$.
- Every resistance included: each film, each layer, each contact, and the fouling layers.
- Bi computed before using the lumped method; Bi above 0.1 means a gradient inside the body.
- Heat balance closed at every interface: heat in equals heat out.
- For a convection correlation: geometry, characteristic length, property reference temperature, and the $\mathrm{Re}$, $\mathrm{Pr}$, or $\mathrm{Ra}$ range checked against what the source states.
- Radiation compared with convection ($h_r$ against $h_c$) before dropping it.
- For fins: base temperature drop and contact resistance considered; effectiveness above 2 before adding fins.
- For insulation on small pipes or wires: critical radius checked.
- Heat exchanger: stream with $C_{\min}$ identified, end differences paired for the actual arrangement, $F$ at most 1.
- Local gravity used for natural convection and a stated planet for any Earth property.

## Sanity checks

- A heat rate through any resistance equals the temperature difference over that resistance. If it exceeds the largest difference over the smallest resistance, a number is wrong.
- The temperature drop across a series element is proportional to its resistance; the largest drop is across the largest resistance, usually the insulation or the gas film.
- Effectiveness is between 0 and 1, and at the same NTU and $C_r$ counterflow is at least as high as parallel flow.
- The log mean difference lies between the two end differences (here 80 K and 30 K give 51 K).
- $\mathrm{Nu}$ near 1 means conduction in the fluid dominates; large $\mathrm{Nu}$ means convection dominates.
- Radiation to surroundings at similar temperature behaves like a convection coefficient of about $4\epsilon_{\text{rad}}\sigma T^3$; near 300 K and $\epsilon_{\text{rad}} = 1$ this is near 6 $\text{W/(m}^2\text{ K)}$.
- A fin of efficiency near 1 is too short to use its tip; one near 0.5 or below carries little at its end.
- A conductivity ratio of metal to insulation is about 3 to 4 orders of magnitude, so a thin insulating layer dominates any metal wall.
- For typical $h_c$ ranges by fluid and regime, see the table in [Thermal-fluids reference](reference-thermofluids.md#heat-transfer).

## Further reference

Free sources:

- Lienhard IV and Lienhard V, [*A Heat Transfer Textbook*](https://ahtt.mit.edu/): the full text, free to download.
- [MIT OpenCourseWare 2.51, Intermediate Heat and Mass Transfer](https://ocw.mit.edu/courses/2-51-intermediate-heat-and-mass-transfer-fall-2008/).
- [OpenStax University Physics Volume 2](https://openstax.org/books/university-physics-volume-2/pages/1-6-mechanisms-of-heat-transfer): the mechanisms of heat transfer, section 1.6.

Paid books and handbooks (by name only): *Fundamentals of Heat and Mass Transfer* (Incropera and DeWitt), *Heat Transfer* (Holman), *Heat and Mass Transfer* (Cengel and Ghajar), *Handbook of Heat Transfer* (Rohsenow, Hartnett, and Cho), and *Heat Exchanger Design Handbook*.
