# Thermal-fluids reference

**Type:** reference

Thermodynamics is the study of energy, heat, and work, fluid mechanics is the study of liquids and gases at rest and in motion, and heat transfer is the study of how thermal energy moves. This sheet lists equations, validity limits, typical values, and sanity checks for use during real analysis and design work. It pairs with lessons 07 to 12 in this folder.

## Principles

- Energy is conserved. If your balance creates energy, a term is missing or has the wrong sign.
- Entropy generation is never negative. Friction, mixing, and finite temperature differences only make a process worse.
- Heat flows from hot to cold on its own. Reversing that flow needs work from outside.
- Use absolute temperature (K) and absolute pressure (Pa) in gas laws, radiation, and every ratio.
- Every model is a regime. A formula is only as good as the assumptions it was derived under. Check them each time.
- Mass is conserved. In a control volume, mass in minus mass out equals the rate of accumulation.
- Every term in an equation has the same units. Dimensional mismatch is the cheapest error to catch.
- Dimensionless groups decide which physics dominates. Match them, not the dimensional sizes, when scaling a test.
- Gravity, atmospheric pressure, and fluid properties are inputs, not constants. Write $g$, $p_\text{atm}$, and property values explicitly, with the temperature they apply to.

## Thermodynamics

### Ideal gas

$$
pV = mRT, \qquad pv = RT, \qquad R = \frac{\bar R}{M}, \qquad \bar R = 8.314\,46\ \text{J/(mol K)}
$$

- $p$ is absolute pressure (Pa). $V$ is volume ($\text{m}^3$). $m$ is mass (kg). $T$ is absolute temperature (K).
- $v$ is specific volume ($\text{m}^3$/kg). Density is $\rho = 1/v$ ($\text{kg/m}^3$).
- $M$ is molar mass (kg/mol). $R$ is the specific gas constant (J/(kg K)).

**Holds when:** the gas is far from condensation, $p$ is well below the critical pressure, and $T$ is well above the critical temperature. Dry air and most combustion gases at ambient or moderate conditions qualify.
**Breaks when:** the gas is near saturation (steam at wet conditions, refrigerant vapor), at high pressure, or near the critical point. Use $pv = ZRT$ with the compressibility factor $Z$ from data, or a real-gas property library.

For an ideal gas with constant specific heats:

$$
c_p - c_v = R, \qquad k = \frac{c_p}{c_v}, \qquad \Delta u = c_v \Delta T, \qquad \Delta h = c_p \Delta T
$$

Typical ideal-gas properties near 300 K and 1 atm (typical):

| Gas | $M$ (kg/kmol) | $R$ (J/(kg K)) | $c_p$ (J/(kg K)) | $c_v$ (J/(kg K)) | $k$ |
|---|---|---|---|---|---|
| Air | 28.97 | 287.0 | 1005 | 718 | 1.40 |
| Nitrogen | 28.01 | 296.8 | 1040 | 743 | 1.40 |
| Oxygen | 32.00 | 259.8 | 918 | 658 | 1.40 |
| Carbon dioxide | 44.01 | 188.9 | 844 | 655 | 1.29 |
| Argon | 39.95 | 208.1 | 520 | 312 | 1.67 |
| Helium | 4.003 | 2077 | 5193 | 3116 | 1.67 |
| Hydrogen | 2.016 | 4124 | 14 307 | 10 185 | 1.405 |

- For air, $c_p$ rises with temperature while $k$ falls. For air at 1000 K (typical), $c_p \approx 1140$ J/(kg K) and $k \approx 1.33$. Use temperature-dependent property data for hot gas.
- Monatomic gases have $k = 5/3$. Diatomic gases near room temperature have $k \approx 1.40$. Polyatomic gases are lower.

### Polytropic and isentropic relations

A polytropic process for a gas obeys $pv^n = \text{const}$.

| Exponent $n$ | Process |
|---|---|
| $0$ | Isobaric (constant $p$) |
| $1$ | Isothermal for an ideal gas |
| $k$ | Isentropic (reversible and adiabatic) |
| $\infty$ | Isochoric (constant $v$) |

$$
\frac{T_2}{T_1} = \left(\frac{p_2}{p_1}\right)^{(n-1)/n} = \left(\frac{v_1}{v_2}\right)^{n-1}, \qquad W_{12} = \frac{p_2V_2 - p_1V_1}{1-n}\ \ (n \ne 1)
$$

- For $n = 1$ (ideal gas): $W_{12} = p_1V_1 \ln(V_2/V_1)$.
- Isentropic, constant $k$: $pv^k = \text{const}$, $\;T_2/T_1 = (p_2/p_1)^{(k-1)/k}$, $\;T_2/T_1 = (v_1/v_2)^{k-1}$.

**Holds when:** ideal gas, reversible process, constant specific heats (with $n$ fitted to data if needed).
**Breaks when:** the process is irreversible (adiabatic but not isentropic, so use entropy instead); the temperature range is large and $k$ varies (use variable-property data); the gas is real.

Worked check: air at 300 K compressed isentropically from 100 kPa to 500 kPa gives $T_2 = 300 \times 5^{0.2857} = 475$ K.

### First law

For a closed system:

$$
\Delta U = Q - W
$$

Use one sign convention and state it. A common one counts heat added to the system and work done by the system as positive.

For a steady-flow open system, per unit mass with one inlet and one outlet:

$$
q - w_s = (h_2 - h_1) + \tfrac{1}{2}(V_2^2 - V_1^2) + g(z_2 - z_1)
$$

- $w_s$ is shaft work out of the control volume (J/kg). $h$ is specific enthalpy (J/kg). $V$ is velocity (m/s). $z$ is height (m).
- In rate form, multiply by the mass flow rate $\dot m$ (kg/s) to get powers in W.
- For multiple inlets or outlets, sum every stream.

Device forms (steady flow, one stream in and out):

| Device | Simplifications | Energy result | Notes |
|---|---|---|---|
| Nozzle | $q = 0$, $w_s = 0$, $\Delta z$ neglected | $V_2 = \sqrt{V_1^2 + 2(h_1 - h_2)}$; ideal gas: $V_2 = \sqrt{V_1^2 + 2c_p(T_1 - T_2)}$ | Speed rises as enthalpy falls. Check for choking (section on compressible flow). |
| Turbine | $q \approx 0$, KE and PE negligible | $w_t = h_1 - h_2$; ideal gas: $w_t = c_p(T_1 - T_2)$ | Isentropic efficiency $\eta_t = (h_1 - h_2)/(h_1 - h_{2s})$ |
| Compressor (gas) | $q \approx 0$ or known, KE and PE negligible | $w_c = h_2 - h_1$ | $\eta_c = (h_{2s} - h_1)/(h_2 - h_1)$. Isentropic exit: $T_{2s} = T_1(p_2/p_1)^{(k-1)/k}$. |
| Pump (liquid) | Incompressible, adiabatic | $\dot W = \dot V\,\Delta p / \eta_p$ | Ideal: $\dot W = \dot V\,\Delta p$. $\Delta p$ in Pa, $\dot V$ in $\text{m}^3$/s. |
| Heat exchanger | No shaft work, KE and PE negligible | $\dot Q = \dot m_h(h_{h,i} - h_{h,o}) = \dot m_c(h_{c,o} - h_{c,i})$ | Size with LMTD or $\varepsilon$-NTU (see heat transfer). |
| Throttle (valve, orifice) | $q = 0$, $w_s = 0$, KE and PE negligible | $h_1 = h_2$ (isenthalpic) | Ideal gas: $T_2 = T_1$. Real gas can cool or heat (Joule-Thomson). Entropy rises. |

Typical isentropic efficiencies (typical, design-dependent): large steam or gas turbines 0.85 to 0.93; axial compressors 0.80 to 0.90; centrifugal pumps 0.70 to 0.85; fans 0.50 to 0.80.

**Holds when:** steady flow, uniform states at each port, one-dimensional streams.
**Breaks when:** the flow is unsteady (keep the storage term $dE_{\mathrm{cv}}/dt$), a stream is not uniform (average it, or integrate), or KE/PE are not negligible (keep them; check $V^2/2$ against $\Delta h$).

## Second law and entropy

Clausius inequality for a cycle:

$$
\oint \frac{\delta Q}{T} \le 0
$$

with equality only if every part of the cycle is reversible. Entropy balance for a closed system:

$$
\Delta S_{\text{sys}} = \int \frac{\delta Q}{T} + S_{\text{gen}}, \qquad S_{\text{gen}} \ge 0
$$

- $S$ is entropy (J/K). $S_{\text{gen}}$ is entropy generated by irreversibility (J/K).
- Lost work (Gouy-Stodola): $W_{\text{lost}} = T_0\,S_{\text{gen}}$, where $T_0$ is the surroundings temperature (K).

Entropy change of an ideal gas with constant specific heats:

$$
\Delta s = c_p \ln\frac{T_2}{T_1} - R\ln\frac{p_2}{p_1} = c_v \ln\frac{T_2}{T_1} + R\ln\frac{v_2}{v_1}
$$

- For an incompressible liquid or solid: $\Delta s = c \ln(T_2/T_1)$.
- Worked check: air from 300 K and 100 kPa to 400 K and 200 kPa gives $\Delta s = 1005\ln(4/3) - 287\ln 2 = 90.2$ J/(kg K).
- Isentropic (reversible adiabatic) means $\Delta s = 0$. An adiabatic process with friction has $\Delta s > 0$.

Statements of the second law:

- Kelvin-Planck: no cyclic device converts heat from one reservoir entirely into work.
- Clausius: no cyclic device moves heat from cold to hot with no work input.

### Efficiency and COP limits

Heat engine: $\eta = W_\text{net}/Q_H = 1 - Q_C/Q_H$.

Carnot limit (any engine between two reservoirs):

$$
\eta_C = 1 - \frac{T_C}{T_H}
$$

- Temperatures in kelvin. Example: $T_H = 800$ K, $T_C = 300$ K gives $\eta_C = 62.5$ percent.
- No real engine between the same two reservoirs can exceed $\eta_C$.

Refrigerator and heat pump:

$$
\text{COP}_R = \frac{Q_L}{W}, \qquad \text{COP}_{\mathrm{HP}} = \frac{Q_H}{W}, \qquad \text{COP}_{\mathrm{HP}} = \text{COP}_R + 1
$$

- Carnot limits: $\text{COP}_{R,C} = T_L/(T_H - T_L)$ and $\text{COP}_{\text{HP},C} = T_H/(T_H - T_L)$.
- Example: a space at 270 K in surroundings at 300 K has ideal $\text{COP}_R = 9.0$ and $\text{COP}_{\mathrm{HP}} = 10.0$.
- COP above 1 is normal for refrigerators. Efficiency above 1 is impossible.

Typical real values (typical): spark-ignition engine 0.25 to 0.35; diesel engine 0.35 to 0.45; steam power plant 0.35 to 0.45; vapor-compression refrigeration or heat pump COP 2 to 4.

### Ideal cycles (cold air standard, $k = 1.4$)

| Cycle | Efficiency | Depends only on | Worked value | Models |
|---|---|---|---|---|
| Otto | $\eta = 1 - r^{1-k}$ | Compression ratio $r$ | $r = 8$: 56.5 percent | Spark-ignition engine |
| Diesel | $\eta = 1 - \dfrac{1}{r^{k-1}}\,\dfrac{r_c^k - 1}{k(r_c - 1)}$ | $r$ and cutoff ratio $r_c = V_3/V_2$ | $r = 18$, $r_c = 2$: 63.2 percent | Compression-ignition engine |
| Brayton | $\eta = 1 - r_p^{-(k-1)/k}$ | Pressure ratio $r_p$ | $r_p = 10$: 48.2 percent | Gas turbine, jet engine |

- Otto and Brayton are ideal. Real engines run well below them because of combustion chemistry, heat loss, friction, and component efficiencies.
- Rankine (steam plant) and vapor-compression refrigeration need real-fluid property data. Do not hand-compute them from the air formulas. Get states from steam tables or from [CoolProp](../tools/09-free-software.md) (free, Python). For vapor compression, $\text{COP}_R = (h_1 - h_4)/(h_2 - h_1)$ with $h$ taken from the property data.

**Holds when:** the cold air standard assumptions hold (ideal gas, constant $k$, reversible processes, fixed heat-addition model).
**Breaks when:** the fluid is steam or a refrigerant, combustion changes the mixture, or the process is irreversible. Carnot always gives the upper bound.

## Fluid properties at standard conditions

Water at 20 °C, 1 atm (typical):

| Property | Value |
|---|---|
| Density $\rho$ | 998 $\text{kg/m}^3$ |
| Dynamic viscosity $\mu$ | $1.00 \times 10^{-3}$ Pa s |
| Kinematic viscosity $\nu$ | $1.00 \times 10^{-6}$ $\text{m}^2$/s |
| Specific heat $c_p$ | 4182 J/(kg K) |
| Thermal conductivity $k$ | 0.60 W/(m K) |
| Prandtl number $\mathrm{Pr}$ | 7.0 |
| Saturation pressure | 2.3 kPa |
| Speed of sound | about 1480 m/s |
| Surface tension (against air) | 0.073 N/m |
| Volume expansion $\beta$ | $2.1 \times 10^{-4}$ 1/K |

Air at 20 °C, 1 atm (typical):

| Property | Value |
|---|---|
| Density $\rho$ | 1.20 $\text{kg/m}^3$ |
| Dynamic viscosity $\mu$ | $1.81 \times 10^{-5}$ Pa s |
| Kinematic viscosity $\nu$ | $1.51 \times 10^{-5}$ $\text{m}^2$/s |
| Specific heat $c_p$ | 1005 J/(kg K) |
| Thermal conductivity $k$ | 0.026 W/(m K) |
| Prandtl number $\mathrm{Pr}$ | 0.71 |
| Speed of sound | 343 m/s |
| Volume expansion $\beta$ | $3.4 \times 10^{-3}$ 1/K (ideal gas, $1/T$) |

- ISA sea-level standard air: $p = 101\,325$ Pa, $T = 288.15$ K, $\rho = 1.225$ $\text{kg/m}^3$, speed of sound about 340 m/s.
- Water viscosity falls by about a factor of 3 from 20 °C to 80 °C. Air viscosity rises slowly with temperature. Never reuse a 20 °C value at another temperature.

**Holds when:** liquids are treated as incompressible, air as an ideal gas, and the temperature is near the stated one.
**Breaks when:** water is near freezing or boiling, pressures reach many MPa, or the fluid is a mixture or contaminated.

## Hydrostatics

$$
p = p_\text{atm} + \rho g h, \qquad p_\text{gauge} = \rho g h
$$

- $h$ is depth below the free surface (m). $g$ is local gravitational acceleration ($\text{m/s}^2$). Earth: 9.81. Moon: 1.62. Mars: 3.71 (typical).
- Rule of thumb: fresh water adds about 9.8 kPa per metre of depth on Earth. 10 m of water is about 98 kPa gauge, so about 1 atm.
- Manometer: $p_A - p_B = \sum \rho_i g\,h_i$, with each term signed by whether you move up or down through it.

Force on a submerged plane surface of area $A$ with centroid depth $h_c$:

$$
F = \rho g h_c A, \qquad y_\text{cp} = y_c + \frac{I_{xc}}{y_c A}
$$

- $y_\text{cp}$ and $y_c$ are distances measured down the plane from the free-surface line, so the center of pressure lies below the centroid. $I_{xc}$ is the second moment of area about the centroid ($\text{m}^4$). For vertical depth on a plate inclined at angle $\theta$ from the horizontal, $h_\text{cp} = h_c + \dfrac{I_{xc}\sin^2\theta}{h_c A}$.

Buoyancy:

$$
F_b = \rho_f g V_\text{sub}
$$

A uniform floating body submerges the fraction $\rho_\text{body}/\rho_f$ of its volume.

Gas column (isothermal, ideal gas):

$$
p(z) = p_0 e^{-z/H}, \qquad H = \frac{RT}{g}
$$

- For air at 288 K on Earth, $H = 8.4$ km (scale height).

**Holds when:** the fluid is at rest, $g$ is uniform, and density is constant (liquids) or the column is short (gases).
**Breaks when:** the fluid rotates (add $\rho\omega^2 r^2/2$), the container accelerates (add the acceleration term), or the gas column is tall (use the scale-height form).

## Bernoulli's equation

$$
p_1 + \tfrac{1}{2}\rho V_1^2 + \rho g z_1 = p_2 + \tfrac{1}{2}\rho V_2^2 + \rho g z_2
$$

Head form: $p/(\rho g) + V^2/(2g) + z = \text{const}$ along a streamline.

Four assumptions. All four must hold between the two points:

1. **Steady flow.** Nothing changes with time at the points compared.
2. **Incompressible.** Density is constant. Valid for liquids and for gases at Mach numbers below about 0.3.
3. **Frictionless (inviscid).** No viscous losses between the points.
4. **Along one streamline.** The two points lie on the same streamline (or the flow is irrotational, for the wider form). No shaft work or heat transfer occurs between them.

**Breaks when:** friction is significant (add $h_f$, see pipe flow), a pump or turbine sits between the points (add $h_p$ or $h_t$), the flow is compressible, the flow is unsteady, the streamline crosses a shock or a mixing zone, or the flow separates from a surface.

Applications and checks:

- Torricelli (free jet from a tank, ideal): $V = \sqrt{2gh}$. A hole 5.0 m below the surface gives 9.9 m/s. Real sharp-edged orifices have a discharge coefficient near 0.6 (typical), so the real flow is lower.
- Pitot tube (incompressible): $V = \sqrt{2(p_0 - p)/\rho}$, with $p_0$ the stagnation pressure.
- Venturi in a horizontal line with $\dot V = 0.010$ $\text{m}^3$/s, $D_1 = 0.10$ m, $D_2 = 0.05$ m, water: $p_1 - p_2 \approx 12.2$ kPa. Speeds are 1.27 and 5.09 m/s.

## Dimensionless numbers

| Group | Definition | Meaning | Critical or typical values | Main use |
|---|---|---|---|---|
| Reynolds $\mathrm{Re}$ | $\rho V L/\mu$ | Inertia over viscous forces | Pipe: laminar below 2300, turbulent above about 4000. Flat plate: transition near $\mathrm{Re}_x = 5 \times 10^5$ | Friction, transition, drag |
| Prandtl $\mathrm{Pr}$ | $\mu c_p/k = \nu/\alpha$ | Momentum diffusion over thermal diffusion | Gases about 0.7 to 1. Water about 7 at 20 °C (typical). Liquid metals about 0.01 (typical) | Convection |
| Nusselt $\mathrm{Nu}$ | $hL/k$ | Convection over conduction in the fluid | $\mathrm{Nu} = 1$ means pure conduction in the fluid layer | Convection correlations |
| Biot $\mathrm{Bi}$ | $hL_c/k$ | Surface convection over conduction inside a solid | Lumped capacitance valid for $\mathrm{Bi} \le 0.1$ | Transient heating and cooling |
| Froude $\mathrm{Fr}$ | $V/\sqrt{gL}$ | Inertia over gravity | Open channel: $\mathrm{Fr} = 1$ is critical. Below 1 is subcritical | Free-surface flow, waves |
| Mach $\mathrm{Ma}$ | $V/a$ | Flow speed over sound speed | Incompressible approximation usable below about 0.3 (density change about 5 percent). $\mathrm{Ma} = 1$ is sonic | Compressible flow |
| Grashof $\mathrm{Gr}$ | $g\beta\Delta T L^3/\nu^2$ | Buoyancy over viscous forces | Sets natural-convection strength | Natural convection |
| Rayleigh $\mathrm{Ra}$ | $\mathrm{Gr} \cdot \mathrm{Pr} = g\beta\Delta T L^3/(\nu\alpha)$ | Buoyancy over diffusion | Vertical plate: laminar up to about $10^9$, turbulent above (typical) | Natural convection |

- $\alpha = k/(\rho c_p)$ is thermal diffusivity ($\text{m}^2$/s). $\beta$ is volume expansion coefficient (1/K).
- Rules of use: state the reference length $L$ for every group in a correlation. Use the same $L$ for all groups. Hydraulic diameter $D_h = 4A/P$ replaces $D$ for non-circular ducts.
- Similarity: a scaled test matches a full-size flow only if the governing groups match (for example $\mathrm{Re}$ for viscous flow, $\mathrm{Ma}$ for compressible flow, $\mathrm{Fr}$ for free-surface flow).

## Pipe flow

Mass flow:

$$
\dot m = \rho A V = \rho \dot V
$$

Darcy-Weisbach head loss:

$$
h_f = f\,\frac{L}{D}\,\frac{V^2}{2g}, \qquad \Delta p = \rho g h_f \ \ (\text{horizontal})
$$

Friction factor:

- Laminar ($\mathrm{Re} < 2300$): $f = 64/\mathrm{Re}$. Equivalent to Hagen-Poiseuille, $\Delta p = 32\,\mu L V/D^2$.
- Turbulent, implicit (Colebrook):

$$
\frac{1}{\sqrt f} = -2\log_{10}\!\left(\frac{\varepsilon/D}{3.7} + \frac{2.51}{\mathrm{Re}\sqrt f}\right)
$$

- Turbulent, explicit (Swamee-Jain):

$$
f = \frac{0.25}{\left[\log_{10}\!\left(\dfrac{\varepsilon}{3.7D} + \dfrac{5.74}{\mathrm{Re}^{0.9}}\right)\right]^2}
$$

  Valid for $5 \times 10^3 \le \mathrm{Re} \le 10^8$ and $10^{-6} \le \varepsilon/D \le 10^{-2}$. Within about 3 percent of Colebrook over that range (typical; the largest gap is at low $\mathrm{Re}$ with high roughness). Example: $\mathrm{Re} = 10^5$, $\varepsilon/D = 10^{-3}$ gives $f = 0.0223$.

Minor losses and totals:

$$
h_m = K\,\frac{V^2}{2g}, \qquad h_\text{total} = \sum h_f + \sum h_m
$$

Typical absolute roughness $\varepsilon$ (typical, from standard Moody-chart values):

| Pipe | $\varepsilon$ (mm) |
|---|---|
| Drawn tubing, glass, PVC, copper | 0.0015 |
| Commercial steel, welded steel | 0.045 |
| Galvanized iron | 0.15 |
| Cast iron | 0.26 |
| Concrete | 0.3 to 3 |
| Riveted steel | 0.9 to 9 |

Typical minor-loss coefficients $K$ (typical values). Each $K$ uses the downstream velocity for expansions and the velocity in the fitting otherwise. Take exact values for design from a cited handbook:

| Fitting | $K$ |
|---|---|
| Sharp-edged entrance | 0.5 |
| Re-entrant (projecting) entrance | 0.8 |
| Sharp-edged exit | 1.0 |
| 90° elbow, flanged | 0.3 |
| 90° elbow, threaded | 1.5 |
| Tee, flow through run | 0.6 |
| Tee, flow through branch | 1.8 |
| Gate valve, fully open | 0.2 |
| Ball valve, fully open | 0.05 to 0.1 |
| Swing check valve | 2.0 to 2.5 |
| Globe valve, fully open | about 10 |

Limits and notes:

- Non-circular ducts: use $D_h = 4A/P$ in $\mathrm{Re}$ and in $h_f$.
- Entrance length: laminar about $0.05\,\mathrm{Re}\,D$. Turbulent about $10D$ (typical). Inside the entrance length the friction is higher than the fully developed value.
- Typical water-main design velocities: 1 to 3 m/s (typical). Typical friction gradients: 0.2 to 3 percent (typical).
- Hazen-Williams and similar empirical formulas are valid only for their stated fluid, unit system, and range. Do not use them outside that range.

**Holds when:** steady, fully developed, incompressible, Newtonian flow in a constant-section pipe.
**Breaks when:** the pipe is short with many fittings (minor losses dominate), the flow is compressible at high Mach numbers, the fluid is non-Newtonian or two-phase, or the flow is in the transition zone $2300 < \mathrm{Re} < 4000$, which design should avoid.

## External flow: drag and lift

$$
F_D = \tfrac{1}{2}\rho V^2 A\, C_D, \qquad F_L = \tfrac{1}{2}\rho V^2 A\, C_L
$$

- $A$ is the reference area. Use frontal area for bluff bodies and planform area for wings. State which one you used.
- Terminal velocity of a falling body with drag and buoyancy: $V_t = \sqrt{2(m - \rho V_\text{body})g/(\rho C_D A)}$.

Typical drag coefficients (typical, subcritical unless noted, based on the stated area):

| Shape | $C_D$ | Notes |
|---|---|---|
| Sphere | 0.4 to 0.5 | $\mathrm{Re}$ about $10^3$ to $2 \times 10^5$. Falls to about 0.1 to 0.2 after the drag crisis near $\mathrm{Re}$ of $3 \times 10^5$ (typical). |
| Circular cylinder, crossflow | 1.0 to 1.2 | $\mathrm{Re}$ about $10^3$ to $10^5$ |
| Square plate, normal to flow | about 1.2 | Frontal area |
| Cube, face on | about 1.05 | Frontal area |
| Passenger car | 0.25 to 0.35 | Frontal area, typical modern shapes |
| Streamlined body (airfoil at low angle) | about 0.01 | Planform area. Mostly skin friction. |

Flat plate skin friction (parallel flow, typical correlations). Average values over plate length $L$, with $\mathrm{Re}_L = UL/\nu$:

- Laminar: $\bar{C}_f = 1.328/\sqrt{\mathrm{Re}_L}$, for $\mathrm{Re}_L$ up to about $5 \times 10^5$.
- Turbulent: $\bar{C}_f = 0.074\,\mathrm{Re}_L^{-1/5}$, for about $5 \times 10^5$ to $10^7$.

Local values at distance $x$ from the leading edge, with $\mathrm{Re}_x = Ux/\nu$:

- Laminar: $C_{f,x} = 0.664/\sqrt{\mathrm{Re}_x}$, for $\mathrm{Re}_x$ up to about $5 \times 10^5$.
- Turbulent: $C_{f,x} = 0.0592\,\mathrm{Re}_x^{-1/5}$, for about $5 \times 10^5$ to $10^7$.

Lift:

- Thin-airfoil theory, small angle $\alpha$ in radians: $C_L \approx 2\pi(\alpha - \alpha_{L=0})$, where $\alpha_{L=0}$ is the zero-lift angle (zero for a symmetric airfoil, so $C_L \approx 2\pi\alpha$; negative for a cambered airfoil). For a symmetric airfoil at $\alpha = 5°$ this gives $C_L \approx 0.55$.
- Stall: typical airfoils stall near $\alpha = 12°$ to $16°$. Maximum lift coefficient is typically 1.0 to 1.6 (typical).
- Kutta-Joukowski, per unit span: $L' = \rho V \Gamma$, with circulation $\Gamma$ ($\text{m}^2$/s).

**Holds when:** steady flow, uniform far-field velocity, a stated Reynolds number range, and attached flow.
**Breaks when:** the flow is transonic or compressible, the body sheds vortices (vortex-induced vibration), the body is near a wall or the ground, or the flow is unsteady. $C_D$ depends strongly on $\mathrm{Re}$, roughness, and the drag crisis.

## Compressible flow

Speed of sound:

$$
a = \sqrt{kRT} \ \ (\text{ideal gas}), \qquad a = \sqrt{K/\rho} \ \ (\text{liquid})
$$

- $K$ is the bulk modulus (Pa). Water: $K \approx 2.2$ GPa, $a \approx 1480$ m/s.
- Air: 340 m/s at 15 °C, 343 m/s at 20 °C, 331 m/s at 0 °C (all typical).

Stagnation relations (isentropic, ideal gas, constant $k$):

$$
\frac{T_0}{T} = 1 + \frac{k-1}{2}\mathrm{Ma}^2, \qquad \frac{p_0}{p} = \left(\frac{T_0}{T}\right)^{k/(k-1)}, \qquad \frac{\rho_0}{\rho} = \left(\frac{T_0}{T}\right)^{1/(k-1)}
$$

- Stagnation temperature rise for air at 100 m/s: $V^2/(2c_p) \approx 5$ K.
- Worked check: $\mathrm{Ma} = 0.5$ in air gives $T_0/T = 1.05$ and $p_0/p = 1.19$.

Area-Mach relation (isentropic, for designing converging-diverging nozzles):

$$
\frac{A}{A^*} = \frac{1}{\mathrm{Ma}}\left[\frac{2}{k+1}\left(1 + \frac{k-1}{2}\mathrm{Ma}^2\right)\right]^{(k+1)/(2(k-1))}
$$

Check: $\mathrm{Ma} = 2$, $k = 1.4$ gives $A/A^* = 1.69$. $A^*$ is the throat area at $\mathrm{Ma} = 1$.

Choked flow (converging nozzle, ideal gas):

- Choking occurs when the back pressure ratio satisfies $p_b/p_0 \le (2/(k+1))^{k/(k-1)}$. For air ($k = 1.4$) this is 0.528.
- At choke, $\mathrm{Ma} = 1$ at the throat. Values for air ($k = 1.4$): $T^*/T_0 = 0.833$, $\rho^*/\rho_0 = 0.634$.
- Maximum mass flow: $\dot m_\text{max} = A^* p_0 \sqrt{k/(RT_0)}\,(2/(k+1))^{(k+1)/(2(k-1))}$.
- Downstream of a choked throat, pressure changes cannot travel upstream. The mass flow does not rise with a lower back pressure.

Normal shock (ideal gas, air, upstream $\mathrm{Ma} = 2$): $p_2/p_1 = 4.5$, downstream $\mathrm{Ma} = 0.577$. Stagnation pressure drops across the shock, and entropy rises.

**Holds when:** isentropic flow, ideal gas, constant $k$, steady, one-dimensional.
**Breaks when:** shocks are present (use shock relations and total-pressure loss), the gas is hot enough for $k$ to vary, friction or heat addition is significant (use Fanno or Rayleigh flow), or the gas is real.

## Heat transfer

Governing rates:

$$
q = -kA\frac{dT}{dx}, \qquad q = hA(T_s - T_\infty), \qquad q = \varepsilon\sigma A\left(T_s^4 - T_\text{sur}^4\right)
$$

- $q$ is heat rate (W). $k$ is thermal conductivity (W/(m K)). $h$ is convection coefficient (W/($\text{m}^2$ K)). $\varepsilon$ is emissivity (dimensionless). $\sigma = 5.670\,37 \times 10^{-8}$ W/($\text{m}^2$ $\text{K}^4$). Temperatures in kelvin.

Thermal resistances (steady, one-dimensional, $R$ in K/W):

| Element | Plane wall | Cylinder (length $L$) | Sphere |
|---|---|---|---|
| Conduction | $L/(kA)$ | $\ln(r_2/r_1)/(2\pi k L)$ | $(1/r_1 - 1/r_2)/(4\pi k)$ |
| Convection | $1/(hA)$ | $1/(h\,2\pi r L)$ | $1/(h\,4\pi r^2)$ |

- Series elements add. Parallel paths add their conductances.
- Critical radius of insulation on a cylinder: $r_\text{cr} = k/h$. On a sphere: $r_\text{cr} = 2k/h$. Below the critical radius, adding insulation increases heat loss.

Radiation:

- Linearized radiation coefficient, valid for a modest temperature difference: $h_r = \varepsilon\sigma(T_s + T_\text{sur})(T_s^2 + T_\text{sur}^2)$. Example: $\varepsilon = 0.9$, $T_s = 350$ K, $T_\text{sur} = 300$ K gives $h_r = 7.0$ W/($\text{m}^2$ K) and a flux of 352 $\text{W/m}^2$.
- Two large parallel gray plates: $q/A = \sigma(T_1^4 - T_2^4)/(1/\varepsilon_1 + 1/\varepsilon_2 - 1)$.

Typical emissivities (typical, near room temperature):

| Surface | $\varepsilon$ |
|---|---|
| Polished copper | 0.02 to 0.05 |
| Polished aluminum | 0.04 to 0.06 |
| Polished stainless steel | 0.1 to 0.3 |
| Oxidized steel or cast iron | 0.6 to 0.8 |
| Concrete | 0.85 to 0.95 |
| Water | 0.95 to 0.96 |
| Human skin | 0.95 to 0.98 |
| Black matte paint | 0.9 to 0.98 |

Typical convection coefficients (typical):

| Situation | $h$ (W/($\text{m}^2$ K)) |
|---|---|
| Free convection, air | 2 to 25 |
| Forced convection, air | 25 to 250 |
| Free convection, water | 100 to 1000 |
| Forced convection, water | 500 to 10 000 |
| Boiling water | 2500 to 35 000 |
| Condensing steam | 5000 to 100 000 |

Fins (straight fin, uniform $h$ and $k$, thin fin):

$$
m = \sqrt{\frac{hP}{kA_c}}, \qquad q_f = \sqrt{hPkA_c}\,\theta_b \tanh(mL), \qquad \eta_f = \frac{\tanh(mL)}{mL}
$$

- $P$ is perimeter (m). $A_c$ is cross-section area ($\text{m}^2$). $\theta_b = T_b - T_\infty$ is base excess temperature (K).
- For a convective tip, use the corrected length $L_c = L + t/2$ in place of $L$ (rectangular fin, typical approximation).
- Fin effectiveness $\varepsilon_f = q_f/(hA_c\theta_b)$. A fin is worth adding as a rule of thumb only when $\varepsilon_f$ is above about 2 (typical rule).

Lumped capacitance (transient, uniform temperature inside a solid):

$$
\mathrm{Bi} = \frac{hL_c}{k}, \qquad L_c = \frac{V}{A_s}, \qquad \frac{\theta}{\theta_i} = e^{-t/\tau}, \qquad \tau = \frac{\rho V c}{hA_s}
$$

- Valid when $\mathrm{Bi} \le 0.1$.
- Example: a 50 mm aluminum cube ($k = 237$ W/(m K), $\rho = 2700$ $\text{kg/m}^3$, $c = 900$ J/(kg K)) in air at $h = 20$ W/($\text{m}^2$ K) has $\mathrm{Bi} = 7 \times 10^{-4}$ and $\tau = 1.0 \times 10^3$ s (about 17 min).

Correlations (smooth surfaces, state the validity):

- Laminar, fully developed, circular tube: $\mathrm{Nu}_D = 3.66$ (constant wall temperature), $\mathrm{Nu}_D = 4.36$ (constant heat flux). Valid for $\mathrm{Re}_D < 2300$.
- Dittus-Boelter, turbulent internal flow:

$$
\mathrm{Nu}_D = 0.023\,\mathrm{Re}_D^{0.8}\mathrm{Pr}^n, \qquad n = 0.4 \ (\text{fluid heated}), \quad n = 0.3 \ (\text{fluid cooled})
$$

  Valid for $\mathrm{Re}_D \ge 10^4$, $0.6 \le \mathrm{Pr} \le 160$, $L/D \ge 10$, smooth tube, moderate temperature difference, properties at bulk mean temperature. Example: $\mathrm{Re} = 5 \times 10^4$, $\mathrm{Pr} = 7$, heated water in a 20 mm tube gives $\mathrm{Nu} = 288$ and $h = 8600$ W/($\text{m}^2$ K).
- Flat plate, laminar, average over length $L$: $\mathrm{Nu}_L = 0.664\,\mathrm{Re}_L^{1/2}\mathrm{Pr}^{1/3}$, for $\mathrm{Pr} \ge 0.6$ and $\mathrm{Re}_L < 5 \times 10^5$.
- Flat plate, turbulent from the leading edge, average over length: $\mathrm{Nu}_L = 0.037\,\mathrm{Re}_L^{4/5}\mathrm{Pr}^{1/3}$, for $0.6 \le \mathrm{Pr} \le 60$ and $5 \times 10^5 \le \mathrm{Re}_L \le 10^7$ (typical range).
- Vertical plate, natural convection, Churchill-Chu, for all $\mathrm{Ra}_L \le 10^{12}$:

$$
\mathrm{Nu}_L = \left\{0.825 + \frac{0.387\,\mathrm{Ra}_L^{1/6}}{\left[1 + (0.492/\mathrm{Pr})^{9/16}\right]^{8/27}}\right\}^2
$$

  Example: $\mathrm{Ra}_L = 10^9$, $\mathrm{Pr} = 0.71$ gives $\mathrm{Nu}_L = 123$.
- Cylinder in crossflow, Churchill-Bernstein, valid for $\mathrm{Re}\,\mathrm{Pr} > 0.2$:

$$
\mathrm{Nu}_D = 0.3 + \frac{0.62\,\mathrm{Re}^{1/2}\mathrm{Pr}^{1/3}}{\left[1 + (0.4/\mathrm{Pr})^{2/3}\right]^{1/4}}\left[1 + \left(\frac{\mathrm{Re}}{282\,000}\right)^{5/8}\right]^{4/5}
$$

Rules of thumb:

- Turbulent forced convection: $h \propto V^{0.8}$. Doubling velocity raises $h$ by about 1.7 times. Basis: Dittus-Boelter. Limit: turbulent internal or external flow with the same geometry.
- Compare $h_r$ with $h$ before neglecting radiation. Radiation matters when $h_r$ is comparable to $h$. Near 350 K, $h_r \approx 7$ W/($\text{m}^2$ K) is already comparable to free convection in air.
- Insulation performance depends on the thermal resistance of the convection films as well as the insulation. A thin film of still air is a large resistance.

Heat exchangers:

$$
\dot Q = UA\,F\,\Delta T_{\mathrm{lm}}, \qquad \Delta T_{\mathrm{lm}} = \frac{\Delta T_1 - \Delta T_2}{\ln(\Delta T_1/\Delta T_2)}
$$

- Counterflow: $\Delta T_1 = T_{h,i} - T_{c,o}$, $\Delta T_2 = T_{h,o} - T_{c,i}$. Parallel flow: $\Delta T_1 = T_{h,i} - T_{c,i}$, $\Delta T_2 = T_{h,o} - T_{c,o}$.
- Example: $\Delta T_1 = 80$ K, $\Delta T_2 = 30$ K gives $\Delta T_{\mathrm{lm}} = 51.0$ K.
- Correction factor $F \le 1$ for shell-and-tube or crossflow units, taken from charts or correlations. For counterflow and parallel flow, $F = 1$.
- Overall coefficient: $1/(UA) = 1/(h_i A_i) + R_\text{wall} + 1/(h_o A_o) + R_f$, where $R_f$ is fouling resistance (K/W).

$\varepsilon$-NTU method (use when outlet temperatures are unknown):

$$
C_r = \frac{C_\min}{C_\max}, \qquad \mathrm{NTU} = \frac{UA}{C_\min}, \qquad \varepsilon = \frac{\dot Q}{\dot Q_\max}, \qquad \dot Q_\max = C_\min(T_{h,i} - T_{c,i})
$$

- Counterflow: $\varepsilon = \dfrac{1 - e^{-\mathrm{NTU}(1 - C_r)}}{1 - C_r e^{-\mathrm{NTU}(1 - C_r)}}$ for $C_r < 1$. For $C_r = 1$: $\varepsilon = \mathrm{NTU}/(1 + \mathrm{NTU})$.
- Parallel flow: $\varepsilon = \dfrac{1 - e^{-\mathrm{NTU}(1 + C_r)}}{1 + C_r}$.
- Condenser or evaporator (phase change, $C_r = 0$): $\varepsilon = 1 - e^{-\mathrm{NTU}}$.
- Example: $\mathrm{NTU} = 2$, $C_r = 0.5$. Counterflow gives $\varepsilon = 0.775$ and parallel gives 0.633. For the same $\mathrm{NTU}$, counterflow always gives the higher effectiveness.

**Holds when:** steady, one-dimensional, uniform properties in each element, constant $h$ and $U$ over each surface.
**Breaks when:** $h$ varies strongly (natural convection on long surfaces, boundary-layer development), there is significant radiation at high temperature, the fluid properties change strongly with temperature, or the problem is transient and not lumped.

## Checklists

Before trusting a thermodynamic result:

- Absolute $T$ and $p$ used in every ratio and gas law.
- Sign convention for $Q$ and $W$ written down and used throughout.
- Energy balance closes for each device (in equals out plus storage).
- Efficiency is below the Carnot value between the same two temperatures.
- Entropy generation is zero or positive.
- Ideal-gas assumption checked against pressure and temperature.

Before trusting a fluid result:

- Regime identified first: laminar or turbulent ($\mathrm{Re}$), incompressible or compressible ($\mathrm{Ma}$), free surface or closed conduit ($\mathrm{Fr}$).
- Bernoulli: all four assumptions checked. Friction, pump or turbine work, and heat added between the points listed.
- Gauge and absolute pressure not mixed in one balance.
- Roughness and $K$ values taken from a cited table, not guessed.
- Velocity and length in $\mathrm{Re}$ are the right ones (hydraulic diameter for non-circular ducts).

Before trusting a heat-transfer result:

- Biot number computed before using the lumped method.
- Correlation range ($\mathrm{Re}$, $\mathrm{Pr}$, $L/D$, $\mathrm{Ra}$) checked and stated.
- Properties evaluated at the temperature the correlation calls for (film or bulk).
- Radiation included or justified as negligible, using $h_r$ against $h$.
- Every convection film and every layer included in the resistance network.
- Heat exchanger: $C_r$, $\mathrm{NTU}$, and the correct $\Delta T$ pairs for the flow arrangement. $F \le 1$.

Before releasing a design:

- Margins on temperature, pressure, and velocity stated.
- Worst-case inputs run (lowest flow, highest ambient, highest load).
- Units on every number and every plot axis.
- Local $g$ and local atmospheric pressure used for the site.
- Material and fluid property data taken at the operating temperature.

## Sanity checks

- Efficiency is between 0 and 1, and below $1 - T_C/T_H$. An answer above Carnot means a temperature was in Celsius, or a sign is wrong.
- Gas temperatures: a Celsius temperature in a gas or radiation equation gives a wrong answer by a large factor. Confirm kelvin.
- Air speed of sound: about 340 to 345 m/s near room temperature. If you get a value far from this, check $T$ and $R$.
- Air density at 300 K and 100 kPa: about 1.16 $\text{kg/m}^3$. Water density: about 1000 $\text{kg/m}^3$. A factor of 10 off means a unit error.
- Water column: about 9.8 kPa per metre of depth on Earth. Atmospheric pressure is about 10.3 m of water.
- Water heat capacity: about 4.2 kJ/(kg K). Warming 1 kg of water by 10 K takes about 42 kJ.
- Convection: the $h$ for water is roughly 25 to 50 times the $h$ for air at the same flow. A water film is much less of a resistance than an air film.
- Conduction: 10 $\text{m}^2$ of 0.20 m concrete at $k = 1.0$ W/(m K) with a 15 K difference carries 750 W.
- Friction: head loss scales with $V^2$. Doubling the flow multiplies the head loss by about 4 for the same pipe.
- Compressibility: if $\mathrm{Ma} > 0.3$, expect density changes of several percent and check whether the incompressible formulas still hold.
- Dimensionless groups: $\mathrm{Nu}$ close to 1 means conduction dominates in the fluid. $\mathrm{Bi}$ much below 0.1 means the solid is nearly uniform in temperature.
- Radiation: at 350 K against 300 K, $h_r \approx 7$ W/($\text{m}^2$ K) is the same order as natural convection in air. Do not drop it on a hot surface.
- Lift: $C_L \approx 1$ is a common order of magnitude for a wing near takeoff or landing conditions (typical).

## Further reference

Paid books and handbooks (by name only):

- Çengel and Boles, *Thermodynamics: An Engineering Approach*.
- Moran, Shapiro, Boettner, and Bailey, *Fundamentals of Engineering Thermodynamics*.
- Incropera, DeWitt, Bergman, and Lavine, *Fundamentals of Heat and Mass Transfer*.
- Kays, Crawford, and Weigand, *Convective Heat and Mass Transfer*.
- White, *Fluid Mechanics*.
- Çengel and Cimbala, *Fluid Mechanics: Fundamentals and Applications*.
- Idelchik, *Handbook of Hydraulic Resistance*.
- Crane Co., *Flow of Fluids Through Valves, Fittings, and Pipe* (Technical Paper 410).
- Anderson, *Modern Compressible Flow*.
- Shapiro, *The Dynamics and Thermodynamics of Compressible Fluid Flow*.
- Perry's Chemical Engineers' Handbook.
- Moody, L. F., "Friction Factors for Pipe Flow," *Transactions of the ASME*, 1944 (source of the Moody chart).

Standards:

- ISO 80000-5, quantities and units, part 5: thermodynamics.
- NIST SP 811, *Guide for the Use of the International System of Units (SI)*.
- ASME PTC 19.1, test uncertainty.

Property data:

- CoolProp (free, open source, Python): steam, water, air, and many refrigerants. See [Free engineering software](../tools/09-free-software.md).
- IAPWS-95, the international formulation for water and steam properties, underlies most steam tables and CoolProp water data.

Free textbooks and course notes are linked in the "Go deeper" sections of lessons 08 to 12.
