# Compressible flow reference

**Type:** reference
**Verify:** strict

Lookup sheet for the one-dimensional flow of a compressible gas, covering isentropic flow, nozzles, shock waves, expansion fans, and flow with friction or heat addition, for an engineer who needs a relation, a table value, or a check on a nozzle, inlet, or duct.

## Principles

- A gas is compressible when its density changes appreciably along the flow. The Mach number $\mathrm{Ma} = v/a$ decides it. Below about $\mathrm{Ma} = 0.3$ the density change is a few percent and incompressible formulas hold.
- Information in a gas travels at the speed of sound. In supersonic flow a disturbance cannot move upstream, so the flow upstream cannot adjust to what is ahead of it. A shock or an expansion fan appears instead.
- Subsonic and supersonic flow respond in opposite ways to a change of area. A converging passage speeds up subsonic flow and slows supersonic flow. Only a converging-diverging passage can take a flow through $\mathrm{Ma} = 1$ smoothly.
- Stagnation temperature stays constant along an adiabatic flow, shocks included. Stagnation pressure stays constant only when the flow is isentropic. Every shock, every friction effect, and every heat addition lowers it.
- A choked throat sets the mass flow. Once the throat reaches $\mathrm{Ma} = 1$, a lower back pressure cannot raise the flow rate.
- A shock is a thin region where the flow is irreversible. Entropy rises across it, so only compression shocks occur. An expansion shock cannot exist.
- Friction drives any duct flow toward $\mathrm{Ma} = 1$, and heat addition does the same. Past that limit the duct chokes and the upstream flow must change.
- Every formula on this sheet assumes a calorically perfect gas (constant $\gamma$). It fails when temperature changes are large enough to excite molecular vibration, and the last section says how to check.
- State the gas, $\gamma$, and $R_s$ with every result. Air at moderate temperature is only one case.

## Governing conservation equations

For steady one-dimensional flow between a station 1 and a station 2 in a duct of changing area, three conservation laws apply. They hold for any gas, and they are the starting point for every relation below.

$$
\rho_1 v_1 A_1 = \rho_2 v_2 A_2, \qquad
p_1 A_1 + \dot{m}\, v_1 + \int p\, dA = p_2 A_2 + \dot{m}\, v_2, \qquad
h_1 + \frac{v_1^2}{2} = h_2 + \frac{v_2^2}{2}
$$

For a control volume with no area change, such as a shock or a constant-area duct, the momentum equation reduces to $p_1 + \rho_1 v_1^2 = p_2 + \rho_2 v_2^2$.

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\rho$ | gas density | $\text{kg/m}^{3}$ |
| $v$ | flow speed along the duct axis | m/s |
| $A$ | duct cross-section area | $\text{m}^{2}$ |
| $\dot{m}$ | mass flow rate | kg/s |
| $p$ | absolute static pressure | Pa |
| $h$ | specific enthalpy | J/kg |

Holds when: the flow is steady and one-dimensional (properties uniform across each section), the gas is a continuum, and no work or heat crosses the walls in the energy equation (adiabatic).
Breaks when: boundary layers are thick compared with the duct (use an effective area), the flow is unsteady, or the walls transfer heat (add $q$ to the energy equation, see Rayleigh flow).
Source and basis: derived from conservation of mass, linear momentum, and energy for a control volume; taught in [Control volumes and pipe flow](11-control-volumes-pipe-flow.md) and [First law](08-thermo-first-law.md).

## Perfect-gas model used throughout

A **calorically perfect gas** obeys $p = \rho R_s T$ with constant specific heats, so $h = c_p T$. The heat capacity ratio is $\gamma = c_p / c_v$ and $R_s = c_p - c_v$. For the ideal-gas law and the first law see [Ideal gas](reference-thermofluids.md#ideal-gas).

$$
R_s = \frac{R_u}{M}, \qquad c_p = \frac{\gamma}{\gamma - 1} R_s
$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $R_s$ | specific gas constant | J/(kg K) |
| $R_u$ | universal gas constant | J/(mol K) |
| $M$ | molar mass of the gas | kg/mol |
| $c_p$ | specific heat at constant pressure | J/(kg K) |
| $\gamma$ | heat capacity ratio | dimensionless |

Holds when: the gas is far from condensation and the temperature range is small enough that $c_p$ is constant.
Breaks when: the temperature changes by several hundred kelvin (vibration raises $c_p$ and lowers $\gamma$), or the gas is near saturation.
Source and basis: derived from the ideal-gas law and $c_p - c_v = R_s$.

Example, dry air (typical for air: $M = 28.97\ \text{g/mol}$ and $\gamma = 1.4$ near ambient temperature). The air values are inputs here, not canonical data.

<details><summary>Verification</summary>

```verify
M = q(28.97, "g/mol", of="none")
gam = q(1.4, "", of="none")
Rs = const("r_gas") / M
expect(Rs, "287.0 J/kg K")
cp = gam / (gam - 1) * Rs
expect(cp, "1005 J/kg K")
```

</details>

With these air values $c_p = 1005\ \text{J/(kg K)}$. Every worked example below uses them and $R_s = 287.0\ \text{J/(kg K)}$.

## Speed of sound and Mach number

The **speed of sound** $a$ is the speed at which a small pressure disturbance travels through a gas. The **Mach number** is the flow speed divided by it.

$$
a = \sqrt{\gamma R_s T}, \qquad \mathrm{Ma} = \frac{v}{a}
$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $a$ | local speed of sound | m/s |
| $\gamma$ | heat capacity ratio | dimensionless |
| $R_s$ | specific gas constant | J/(kg K) |
| $T$ | absolute static temperature | K |
| $\mathrm{Ma}$ | Mach number, local speed over local sound speed | dimensionless |
| $v$ | flow speed | m/s |

Holds when: the gas is a perfect gas and the disturbance is small and isentropic.
Breaks when: the gas is a liquid or a two-phase mixture (use $a = \sqrt{K/\rho}$ with bulk modulus $K$), or the frequency is so high that the gas cannot relax thermally. A wave of finite strength travels faster than $a$; that is a shock.
Source and basis: derived from mass and momentum conservation across a small acoustic wave plus the isentropic perfect-gas relation.

Example. Air at $T = 300\ \text{K}$ has $a = \sqrt{\gamma R_s T} = 347.2\ \text{m/s}$. A vehicle at $v = 600\ \text{m/s}$ in that air is at $\mathrm{Ma} = 1.728$. The sound speed depends on temperature only, not on pressure.

<details><summary>Verification</summary>

```verify
gam = q(1.4, "", of="none")
Rs = q(287.0, "J/kg K", of="none")
T = q(300, "K")
a = sqrt(gam * Rs * T)
expect(a, "347.2 m/s")
v = q(600, "m/s")
expect(v / a, "1.728")
```

</details>

Flow regimes by Mach number (conventional boundaries, typical, not sharp):

| Regime | $\mathrm{Ma}$ range | Main feature |
|---|---|---|
| Incompressible | below 0.3 | density change under about 5 percent |
| Subsonic compressible | 0.3 to 0.8 | density varies; no shocks |
| Transonic | 0.8 to 1.2 | mixed subsonic and supersonic regions, local shocks |
| Supersonic | 1.2 to 5 | shocks and expansion fans |
| Hypersonic | above 5 | high-temperature gas effects dominate |

## Stagnation states

The **stagnation state** is the state a flow reaches if brought to rest isentropically. It is a property of the flow, not of the gas at rest, and it does not change along an isentropic flow.

$$
\frac{T_0}{T} = 1 + \frac{\gamma - 1}{2}\mathrm{Ma}^2, \qquad
\frac{p_0}{p} = \left(\frac{T_0}{T}\right)^{\gamma/(\gamma-1)}, \qquad
\frac{\rho_0}{\rho} = \left(\frac{T_0}{T}\right)^{1/(\gamma-1)}
$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $T_0$ | stagnation temperature | K |
| $p_0$ | stagnation pressure | Pa |
| $\rho_0$ | stagnation density | $\text{kg/m}^{3}$ |
| $T$ | static temperature at the point | K |
| $p$ | static pressure at the point | Pa |
| $\rho$ | static density at the point | $\text{kg/m}^{3}$ |
| $\gamma$ | heat capacity ratio | dimensionless |
| $\mathrm{Ma}$ | local Mach number | dimensionless |

Holds when: the flow is steady, adiabatic for $T_0$, and isentropic (reversible and adiabatic) for $p_0$ and $\rho_0$, for a perfect gas.
Breaks when: a shock, friction, or heat transfer lies between the point and the reference. Then $T_0$ may still hold (adiabatic) but $p_0$ drops. A pitot tube behind a shock reads the post-shock $p_0$, not the free-stream value.
Source and basis: derived from the energy equation $h + v^2/2 = h_0$ and the isentropic relation $p \propto \rho^{\gamma}$; see [First law](08-thermo-first-law.md) and [Second law and cycles](09-thermo-second-law-cycles.md).

Example. At $\mathrm{Ma} = 2$ in air ($\gamma = 1.4$), the static temperature is $T_0/1.8$, the static pressure is $p_0/7.824$, and the static density is $\rho_0/4.347$. The critical (sonic) ratios, where $\mathrm{Ma} = 1$, are $T^*/T_0 = 2/(\gamma+1) = 0.8333$ and $p^*/p_0 = 0.5283$.

<details><summary>Verification</summary>

```verify
gam = q(1.4, "", of="none")
Ma = q(2, "")
tr = 1 + (gam - 1) / 2 * Ma**2
expect(tr, "1.800")
expect(tr**(gam / (gam - 1)), "7.824")
expect(tr**(1 / (gam - 1)), "4.347")
expect(2 / (gam + 1), "0.8333")
expect((2 / (gam + 1))**(gam / (gam - 1)), "0.5283")
```

</details>

## Quasi-one-dimensional flow and the area-velocity relation

In a duct whose area changes slowly, treat each section as uniform. Differentiating mass, momentum, and the isentropic relation gives the effect of area change on speed.

$$
\frac{dv}{v} = -\frac{1}{1 - \mathrm{Ma}^2}\,\frac{dA}{A}, \qquad
\frac{dp}{p} = \frac{\gamma\,\mathrm{Ma}^2}{1 - \mathrm{Ma}^2}\,\frac{dA}{A}
$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $v$ | flow speed | m/s |
| $p$ | static pressure | Pa |
| $A$ | duct area | $\text{m}^{2}$ |
| $\gamma$ | heat capacity ratio | dimensionless |
| $\mathrm{Ma}$ | local Mach number | dimensionless |

Holds when: the flow is steady, isentropic, and quasi-one-dimensional with a small wall slope, for a perfect gas.
Breaks when: the flow separates, the wall angle is large (use a two- or three-dimensional method), or a shock sits in the duct.
Source and basis: derived from differential mass conservation, the Euler momentum equation $dp = -\rho v\, dv$, and $a^2 = dp/d\rho$ for isentropic change.

Reading the relation:

| Flow | $dA > 0$ (diverging) | $dA < 0$ (converging) |
|---|---|---|
| Subsonic, $\mathrm{Ma} < 1$ | $v$ falls, $p$ rises | $v$ rises, $p$ falls |
| Supersonic, $\mathrm{Ma} > 1$ | $v$ rises, $p$ falls | $v$ falls, $p$ rises |

At $\mathrm{Ma} = 1$ the factor $1 - \mathrm{Ma}^2$ is zero, so $dA = 0$: a sonic point can occur only at a minimum area (a throat). A smooth subsonic-to-supersonic transition therefore needs a converging-diverging nozzle.

## Area-Mach relation and choking

The **sonic area** $A^*$ is the area the flow would have if brought isentropically to $\mathrm{Ma} = 1$. The ratio $A/A^*$ is fixed by the local Mach number alone.

$$
\frac{A}{A^*} = \frac{1}{\mathrm{Ma}}\left[\frac{2}{\gamma+1}\left(1 + \frac{\gamma-1}{2}\mathrm{Ma}^2\right)\right]^{\frac{\gamma+1}{2(\gamma-1)}}
$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $A$ | duct area at the section | $\text{m}^{2}$ |
| $A^*$ | sonic (critical) area of the same isentropic flow | $\text{m}^{2}$ |
| $\gamma$ | heat capacity ratio | dimensionless |
| $\mathrm{Ma}$ | Mach number at the section | dimensionless |

Holds when: the flow is steady, isentropic, quasi-one-dimensional, and the gas is perfect. $A^*$ is a reference area; it equals the real throat area only if the throat is sonic.
Breaks when: a shock lies upstream of the section (the shock changes $A^*$; use the post-shock value), or friction and heat addition act.
Source and basis: derived from mass conservation with the isentropic stagnation relations; the area-velocity relation above gives its minimum at $\mathrm{Ma} = 1$.

For a given $A/A^* > 1$ there are two solutions, one subsonic and one supersonic. Which one occurs is set by the back pressure. The relation has no closed-form inverse, so solve it by iteration or from a table.

Example. At $\mathrm{Ma} = 2$ in air, $A/A^* = 1.688$. A nozzle with throat area $A^*$ must have an exit 1.688 times larger to expand a sonic flow to $\mathrm{Ma} = 2$. At $\mathrm{Ma} = 0.5$ the area ratio is 1.340 and at $\mathrm{Ma} = 3$ it is 4.235.

<details><summary>Verification</summary>

```verify
gam = q(1.4, "", of="none")
def_exp = (gam + 1) / (2 * (gam - 1))
Ma2 = q(2, "")
t2 = 2 / (gam + 1) * (1 + (gam - 1) / 2 * Ma2**2)
expect(t2**def_exp / Ma2, "1.688")
Ma5 = q(0.5, "")
t5 = 2 / (gam + 1) * (1 + (gam - 1) / 2 * Ma5**2)
expect(t5**def_exp / Ma5, "1.340")
Ma3 = q(3, "")
t3 = 2 / (gam + 1) * (1 + (gam - 1) / 2 * Ma3**2)
expect(t3**def_exp / Ma3, "4.235")
```

</details>

## Nozzles and mass flow

### Choked mass flow rate

A throat is **choked** when its Mach number reaches 1. The mass flow then depends only on upstream stagnation conditions and the throat area.

$$
\dot{m}_{\max} = A^* p_0 \sqrt{\frac{\gamma}{R_s T_0}}\left(\frac{2}{\gamma+1}\right)^{\frac{\gamma+1}{2(\gamma-1)}}
$$

For a converging nozzle, choking occurs when the back pressure satisfies $p_b / p_0 \le \left(2/(\gamma+1)\right)^{\gamma/(\gamma-1)}$. A converging-diverging nozzle has a geometry-dependent threshold set by its area ratio.

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\dot{m}_{\max}$ | choked mass flow rate | kg/s |
| $A^*$ | throat area (sonic area) | $\text{m}^{2}$ |
| $p_0$ | upstream stagnation pressure | Pa |
| $T_0$ | upstream stagnation temperature | K |
| $\gamma$ | heat capacity ratio | dimensionless |
| $R_s$ | specific gas constant | J/(kg K) |
| $p_b$ | back pressure downstream of the nozzle | Pa |

Holds when: the flow upstream of the throat is isentropic, the gas is perfect, and the throat is sonic. Real nozzles carry a discharge coefficient below 1 from boundary-layer blockage.
Breaks when: the throat is subsonic because the back pressure is above the geometry-dependent choking threshold, the gas has strong real-gas effects, or the stagnation conditions are unsteady.
Source and basis: derived from $\dot{m} = \rho^* a^* A^*$ with the sonic stagnation ratios; see [Control volumes and pipe flow](11-control-volumes-pipe-flow.md).

Example. Air with $p_0 = 500\ \text{kPa}$ and $T_0 = 300\ \text{K}$ through a throat of $A^* = 10\ \text{cm}^2$ gives $\dot{m}_{\max} = 1.167\ \text{kg/s}$. For a converging nozzle the critical back-pressure ratio is 0.5283, so it is choked for any $p_b$ below 264.1 kPa. For a converging-diverging nozzle with $A_e/A^* = 1.688$, the subsonic exit root is $\mathrm{Ma}_e = 0.3722$, giving $p_e/p_0 = 0.9088$; it is choked for any $p_b$ below 454.4 kPa. Doubling $p_0$ doubles $\dot{m}_{\max}$ and raising $T_0$ lowers it as $1/\sqrt{T_0}$.

<details><summary>Verification</summary>

```verify
gam = q(1.4, "", of="none")
Rs = q(287.0, "J/kg K", of="none")
p0 = q(500, "kPa")
T0 = q(300, "K")
As = q(10, "cm^2")
mdot = As * p0 * sqrt(gam / (Rs * T0)) * (2 / (gam + 1))**((gam + 1) / (2 * (gam - 1)))
expect(mdot, "1.167 kg/s")
pcrit = (2 / (gam + 1))**(gam / (gam - 1))
expect(pcrit, "0.5283")
expect(pcrit * p0, "264.1 kPa")
gam = q(1.4, "", of="none")
Mae = q(0.3722, "", of="none")
ar = (1 / Mae) * (2 / (gam + 1) * (1 + (gam - 1) / 2 * Mae**2))**((gam + 1) / (2 * (gam - 1)))
expect(ar, "1.688")
pr = (1 + (gam - 1) / 2 * Mae**2)**(-gam / (gam - 1))
expect(pr, "0.9088")
expect(pr * p0, "454.4 kPa")
```

</details>

### Exit conditions

For a nozzle expanding from stagnation conditions $p_0$, $T_0$ to an exit at Mach number $\mathrm{Ma}_e$, the exit state follows from the stagnation relations, and the exit speed is the Mach number times the exit sound speed.

$$
v_e = \mathrm{Ma}_e\, a_e = \sqrt{\frac{2\gamma}{\gamma-1} R_s T_0\left[1 - \left(\frac{p_e}{p_0}\right)^{(\gamma-1)/\gamma}\right]}
$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $v_e$ | nozzle exit speed | m/s |
| $a_e$ | speed of sound at the exit static temperature | m/s |
| $\mathrm{Ma}_e$ | exit Mach number | dimensionless |
| $p_e$ | exit static pressure | Pa |
| $p_0$ | stagnation pressure | Pa |
| $T_0$ | stagnation temperature | K |
| $\gamma$ | heat capacity ratio | dimensionless |
| $R_s$ | specific gas constant | J/(kg K) |

Holds when: the flow in the nozzle is isentropic, steady, and in equilibrium with constant $\gamma$.
Breaks when: boundary layers, friction, or heat loss reduce exit speed (apply a velocity coefficient), a shock is inside the nozzle, or the hot gas changes composition on expansion (frozen versus equilibrium flow in rocket nozzles).
Source and basis: derived from the energy equation $c_p T_0 = c_p T_e + v_e^2/2$ and the isentropic relation.

Example. With the same air supply as above and a design exit Mach number of 2, the exit area is 1.688 times the throat area. The exit static pressure is $p_0/7.824 = 63.90\ \text{kPa}$, the exit temperature is 166.7 K, and the exit speed is 517.6 m/s.

<details><summary>Verification</summary>

```verify
gam = q(1.4, "", of="none")
Rs = q(287.0, "J/kg K", of="none")
p0 = q(500, "kPa")
T0 = q(300, "K")
Mae = q(2, "")
tr = 1 + (gam - 1) / 2 * Mae**2
pe = p0 / tr**(gam / (gam - 1))
expect(pe, "63.90 kPa")
Te = T0 / tr
expect(Te, "166.7 K")
ve = Mae * sqrt(gam * Rs * Te)
expect(ve, "517.6 m/s")
ve2 = sqrt(2 * gam / (gam - 1) * Rs * T0 * (1 - (pe / p0)**((gam - 1) / gam)))
expect(ve2, "517.6 m/s")
expect(tr**(gam / (gam - 1)), "7.824")
expect(((2 / (gam + 1)) * tr)**((gam + 1) / (2 * (gam - 1))) / Mae, "1.688")
```

</details>

### Under-expanded and over-expanded flow

Whether a nozzle runs at its design pressure ratio depends on the back (ambient) pressure $p_a$ compared with the exit pressure $p_e$.

| Condition | Exit flow | What happens |
|---|---|---|
| $p_e = p_a$ | Design (matched) | Parallel jet, no shocks in the plume |
| $p_e > p_a$ | Under-expanded | The jet expands further outside the nozzle through expansion fans, then recompresses in a shock-cell pattern |
| $p_e < p_a$ | Over-expanded | Oblique shocks form at the lip to raise pressure to ambient |
| $p_e$ far below $p_a$ | Strongly over-expanded | The shock moves inside, the boundary layer separates, and the flow becomes unsteady with side loads |

Mass flow is the same in all four cases once the throat is choked. Only the thrust and the plume change.

### Thrust and thrust coefficient

Thrust is the net axial force on the nozzle and its gas. Use the momentum equation on a control volume around it.

$$
F = \dot{m}\, v_e + (p_e - p_a) A_e, \qquad C_F = \frac{F}{p_0 A^*}
$$

For a matched ideal nozzle, $p_e = p_a$, and
$C_F = \sqrt{\dfrac{2\gamma^2}{\gamma-1}\left(\dfrac{2}{\gamma+1}\right)^{\frac{\gamma+1}{\gamma-1}}\left[1 - \left(\dfrac{p_e}{p_0}\right)^{\frac{\gamma-1}{\gamma}}\right]}$.

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $F$ | thrust | N |
| $\dot{m}$ | mass flow rate through the nozzle | kg/s |
| $v_e$ | exit speed | m/s |
| $p_e$ | exit static pressure | Pa |
| $p_a$ | ambient (back) pressure | Pa |
| $A_e$ | exit area | $\text{m}^{2}$ |
| $C_F$ | thrust coefficient, thrust over $p_0 A^*$ | dimensionless |
| $p_0$ | chamber stagnation pressure | Pa |
| $A^*$ | throat area | $\text{m}^{2}$ |
| $\gamma$ | heat capacity ratio | dimensionless |

Holds when: the flow is steady, the exit plane flow is uniform and axial, and the gas is perfect. The second form needs a matched, isentropic, choked nozzle.
Breaks when: the exit flow is not parallel (a conical nozzle loses a factor close to $(1 + \cos\alpha)/2$ for half-angle $\alpha$), friction is significant, the plume is strongly over-expanded and separated, or the nozzle moves at high speed (use the net thrust with momentum drag of the incoming air).
Source and basis: derived from the linear-momentum equation on a control volume; the rocket equation and mass ratio are on [physics/reference-orbital-mechanics.md](reference-orbital-mechanics.md) and taught in [Orbital mechanics and rockets](15-orbital-mechanics-and-rockets.md).

Example. For the same nozzle (matched, $\mathrm{Ma}_e = 2$, $p_0 = 500\ \text{kPa}$, $A^* = 10\ \text{cm}^2$), thrust is $F = \dot{m} v_e = 603.9\ \text{N}$ and $C_F = 1.208$. The two forms of $C_F$ agree.

<details><summary>Verification</summary>

```verify
gam = q(1.4, "", of="none")
Rs = q(287.0, "J/kg K", of="none")
p0 = q(500, "kPa")
T0 = q(300, "K")
As = q(10, "cm^2")
mdot = As * p0 * sqrt(gam / (Rs * T0)) * (2 / (gam + 1))**((gam + 1) / (2 * (gam - 1)))
ve = q(517.56, "m/s")
F = mdot * ve
expect(F, "603.9 N")
CF = F / (p0 * As)
expect(CF, "1.208")
pr = q(1, "") / 7.824449
CF2 = sqrt(2 * gam**2 / (gam - 1) * (2 / (gam + 1))**((gam + 1) / (gam - 1)) * (1 - pr**((gam - 1) / gam)))
expect(CF2, "1.208")
```

</details>

## Normal shocks

A **normal shock** is a thin surface perpendicular to the flow across which a supersonic flow drops abruptly to subsonic, with a jump in pressure, density, and temperature. Entropy rises, so the process is irreversible. The relations use station 1 upstream and station 2 downstream.

$$
\frac{p_2}{p_1} = 1 + \frac{2\gamma}{\gamma+1}\left(\mathrm{Ma}_1^2 - 1\right), \qquad
\frac{\rho_2}{\rho_1} = \frac{(\gamma+1)\mathrm{Ma}_1^2}{(\gamma-1)\mathrm{Ma}_1^2 + 2}
$$

$$
\frac{T_2}{T_1} = \frac{p_2/p_1}{\rho_2/\rho_1}, \qquad
\mathrm{Ma}_2^2 = \frac{(\gamma-1)\mathrm{Ma}_1^2 + 2}{2\gamma\,\mathrm{Ma}_1^2 - (\gamma-1)}
$$

$$
\frac{p_{02}}{p_{01}} = \left(\frac{\rho_2}{\rho_1}\right)^{\gamma/(\gamma-1)}\left[\frac{\gamma+1}{2\gamma\,\mathrm{Ma}_1^2 - (\gamma-1)}\right]^{1/(\gamma-1)}
$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $p_1$, $p_2$ | static pressure upstream and downstream | Pa |
| $\rho_1$, $\rho_2$ | density upstream and downstream | $\text{kg/m}^{3}$ |
| $T_1$, $T_2$ | static temperature upstream and downstream | K |
| $\mathrm{Ma}_1$, $\mathrm{Ma}_2$ | Mach number upstream and downstream | dimensionless |
| $p_{01}$, $p_{02}$ | stagnation pressure upstream and downstream | Pa |
| $\gamma$ | heat capacity ratio | dimensionless |

Holds when: the shock is normal to a steady flow, the gas is perfect, and $\mathrm{Ma}_1 > 1$. Stagnation temperature is the same on both sides.
Breaks when: the shock is oblique (use the oblique relations with the normal Mach component), the temperature behind the shock is high enough for vibration or dissociation (real-gas shock), or the shock is unsteady or interacts with a boundary layer.
Source and basis: derived from the conservation equations across the shock with the perfect-gas model; see [Control volumes and pipe flow](11-control-volumes-pipe-flow.md).

Example. A normal shock at $\mathrm{Ma}_1 = 2$ in air gives $p_2/p_1 = 4.500$, $\rho_2/\rho_1 = 2.667$, $T_2/T_1 = 1.688$, and $\mathrm{Ma}_2 = 0.5774$. Stagnation pressure falls to 0.7209 of the upstream value, a loss of 0.279 of the upstream value, or 27.9 percent. As $\mathrm{Ma}_1$ approaches 1 the shock weakens and the loss goes to zero; it grows quickly above $\mathrm{Ma}_1 = 2$. The density ratio cannot exceed $(\gamma+1)/(\gamma-1) = 6$ for any strength.

<details><summary>Verification</summary>

```verify
gam = q(1.4, "", of="none")
M1 = q(2, "")
pr = 1 + 2 * gam / (gam + 1) * (M1**2 - 1)
expect(pr, "4.500")
rr = (gam + 1) * M1**2 / ((gam - 1) * M1**2 + 2)
expect(rr, "2.667")
expect(pr / rr, "1.688")
M2 = sqrt(((gam - 1) * M1**2 + 2) / (2 * gam * M1**2 - (gam - 1)))
expect(M2, "0.5774")
p0r = rr**(gam / (gam - 1)) * ((gam + 1) / (2 * gam * M1**2 - (gam - 1)))**(1 / (gam - 1))
expect(p0r, "0.7209")
expect(1 - p0r, "0.279")
expect(100 * (1 - p0r), "27.9")
expect((gam + 1) / (gam - 1), "6")
```

</details>

## Oblique shocks

An **oblique shock** is a straight shock inclined to the flow, formed when supersonic flow turns into itself, as at a wedge or a compression corner. Only the flow component normal to the shock changes as in a normal shock; the tangential component is unchanged.

$$
\tan\theta = 2\cot\beta\;\frac{\mathrm{Ma}_1^2\sin^2\beta - 1}{\mathrm{Ma}_1^2(\gamma + \cos 2\beta) + 2}
$$

With $\mathrm{Ma}_{n1} = \mathrm{Ma}_1 \sin\beta$, the property ratios $p_2/p_1$, $\rho_2/\rho_1$, $T_2/T_1$, and $p_{02}/p_{01}$ are the normal-shock formulas with $\mathrm{Ma}_{n1}$ in place of $\mathrm{Ma}_1$. The downstream Mach number is
$\mathrm{Ma}_2 = \mathrm{Ma}_{n2} / \sin(\beta - \theta)$, with $\mathrm{Ma}_{n2}$ from the normal-shock formula.

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\theta$ | flow deflection angle (wedge or wall turn) | rad |
| $\beta$ | shock wave angle measured from the upstream flow direction | rad |
| $\mathrm{Ma}_1$ | upstream Mach number | dimensionless |
| $\mathrm{Ma}_{n1}$, $\mathrm{Ma}_{n2}$ | Mach number component normal to the shock, upstream and downstream | dimensionless |
| $\mathrm{Ma}_2$ | downstream Mach number | dimensionless |
| $\gamma$ | heat capacity ratio | dimensionless |

Holds when: the shock is straight and attached, the flow is steady and two-dimensional (or conical, for a cone, which has different charts), and the gas is perfect.
Breaks when: the deflection exceeds the maximum for the given Mach number (the shock detaches and becomes curved), the shock meets a boundary layer or another shock, or the flow is three-dimensional.
Source and basis: derived from the normal-shock conservation equations applied to the normal velocity component, with tangential velocity continuous across the shock.

The cubic in $\sin^2\beta$ can have three mathematical roots for a given $\mathrm{Ma}_1$ and $\theta$. Only the weak and strong roots are physical; the third root would decrease entropy across the shock.

| Branch | Wave angle | Downstream flow | Occurs when |
|---|---|---|---|
| Weak | smaller $\beta$ | Supersonic (except for deflections near the maximum) | Almost always, with a free exit to ambient pressure |
| Strong | larger $\beta$ | Subsonic | A high downstream back pressure forces it |

There is a **maximum deflection** $\theta_{\max}$ for each $\mathrm{Ma}_1$. At $\theta_{\max}$ the weak and strong solutions merge. It rises with $\mathrm{Ma}_1$ toward a limit set by $\gamma$. For $\theta$ above $\theta_{\max}$ no attached solution exists and a curved, detached bow shock stands off the body. As $\mathrm{Ma}_1$ approaches 1 the weak-branch wave angle approaches the Mach angle, $\sin\mu = 1/\mathrm{Ma}_1$, for an infinitesimal turn.

Example. At $\mathrm{Ma}_1 = 2$ a shock at $\beta = 40$ degrees deflects air by $\theta = 10.62$ degrees. The normal component is $\mathrm{Ma}_{n1} = 1.286$, so the pressure ratio is $p_2/p_1 = 1.761$ (from the normal-shock formula at that Mach number, a much weaker jump than the 4.500 of a normal shock at $\mathrm{Ma}_1 = 2$). The Mach angle at $\mathrm{Ma}_1 = 2$ is 30 degrees, below $\beta$, as it must be.

<details><summary>Verification</summary>

```verify
gam = q(1.4, "", of="none")
M1 = q(2, "")
beta = q(40, "deg")
theta = atan(2 / tan(beta) * (M1**2 * sin(beta)**2 - 1) / (M1**2 * (gam + cos(2 * beta)) + 2))
expect(theta, "10.62 deg")
Mn1 = M1 * sin(beta)
expect(Mn1, "1.286")
pr = 1 + 2 * gam / (gam + 1) * (Mn1**2 - 1)
expect(pr, "1.761")
expect(1 + 2 * gam / (gam + 1) * (M1**2 - 1), "4.500")
mu = asin(1 / M1)
expect(mu, "30 deg")
check(mu < beta, "wave angle exceeds the Mach angle")
```

</details>

## Prandtl-Meyer expansion

A **Prandtl-Meyer expansion** is the smooth, isentropic turning of a supersonic flow around a convex corner through a fan of Mach waves. The flow accelerates and its pressure falls. The **Prandtl-Meyer function** $\nu$ is the angle through which a flow at $\mathrm{Ma} = 1$ must turn to reach a given Mach number.

$$
\nu(\mathrm{Ma}) = \sqrt{\frac{\gamma+1}{\gamma-1}}\,\arctan\sqrt{\frac{\gamma-1}{\gamma+1}\left(\mathrm{Ma}^2 - 1\right)} - \arctan\sqrt{\mathrm{Ma}^2 - 1}, \qquad
\theta = \nu(\mathrm{Ma}_2) - \nu(\mathrm{Ma}_1)
$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\nu$ | Prandtl-Meyer function | rad |
| $\mathrm{Ma}$ | Mach number | dimensionless |
| $\gamma$ | heat capacity ratio | dimensionless |
| $\theta$ | total turning angle of the expansion | rad |
| $\mathrm{Ma}_1$, $\mathrm{Ma}_2$ | Mach number before and after the fan | dimensionless |

Holds when: the flow is supersonic, steady, two-dimensional, and isentropic through the fan, with a perfect gas. Stagnation conditions are unchanged, so find $p_2$ and $T_2$ from the stagnation relations at $\mathrm{Ma}_2$.
Breaks when: the turn is so large that the pressure would fall below vacuum (the flow turns by at most $\nu_{\max} = \left(\sqrt{(\gamma+1)/(\gamma-1)} - 1\right)\pi/2$), the flow is axisymmetric or three-dimensional, or the boundary layer separates at the corner.
Source and basis: derived from the Mach-wave relation $d\theta = \sqrt{\mathrm{Ma}^2 - 1}\; dv/v$ integrated with the isentropic relations.

Example. At $\mathrm{Ma} = 2$ in air, $\nu = 26.38$ degrees. To expand a flow from $\mathrm{Ma} = 2$ to $\mathrm{Ma} = 3$ around a convex corner, with $\nu(3) = 49.76$ degrees, the wall must turn by $\theta = 23.38$ degrees. The Mach angle at $\mathrm{Ma} = 2$ is 30 degrees, and the fan lies between the Mach angles of the two states.

<details><summary>Verification</summary>

```verify
gam = q(1.4, "", of="none")
r = sqrt((gam + 1) / (gam - 1))
nu2 = r * atan(sqrt((gam - 1) / (gam + 1) * (q(2, "")**2 - 1))) - atan(sqrt(q(2, "")**2 - 1))
expect(nu2, "26.38 deg")
nu3 = r * atan(sqrt((gam - 1) / (gam + 1) * (q(3, "")**2 - 1))) - atan(sqrt(q(3, "")**2 - 1))
expect(nu3, "49.76 deg")
expect(nu3 - nu2, "23.38 deg")
expect(asin(1 / q(2, "")), "30 deg")
```

</details>

## Fanno flow

**Fanno flow** is steady, adiabatic, one-dimensional flow of a perfect gas in a constant-area duct with wall friction. Friction drives the flow toward $\mathrm{Ma} = 1$ from either side, with stagnation temperature constant and stagnation pressure falling.

$$
\frac{4 f_F L^*}{D} = \frac{1 - \mathrm{Ma}^2}{\gamma\,\mathrm{Ma}^2} + \frac{\gamma+1}{2\gamma}\ln\frac{(\gamma+1)\mathrm{Ma}^2}{2 + (\gamma-1)\mathrm{Ma}^2}
$$

$$
\frac{T}{T^*} = \frac{\gamma+1}{2 + (\gamma-1)\mathrm{Ma}^2}, \qquad
\frac{p}{p^*} = \frac{1}{\mathrm{Ma}}\sqrt{\frac{\gamma+1}{2 + (\gamma-1)\mathrm{Ma}^2}}
$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $f_F$ | Fanning friction factor, mean over the length | dimensionless |
| $L^*$ | duct length from the section to the sonic section | m |
| $D$ | hydraulic diameter of the duct | m |
| $\mathrm{Ma}$ | Mach number at the section | dimensionless |
| $T$ | static temperature at the section | K |
| $p$ | static pressure at the section | Pa |
| $T^*$ | static temperature at the sonic state of the same flow | K |
| $p^*$ | static pressure at the sonic state of the same flow | Pa |
| $\gamma$ | heat capacity ratio | dimensionless |

Holds when: the duct has constant area, the walls are adiabatic, the friction factor is constant, and the gas is perfect. The sonic state is a reference even if the duct ends before it. Use the Fanning factor $f_F = f_D/4$ and label which you use.
Breaks when: the friction factor changes strongly along the duct, the walls exchange heat (use Rayleigh flow or a combined model), or the duct is longer than $L^*$. A longer duct chokes: a subsonic inlet flow reduces its mass flow, and a supersonic inlet flow develops a shock in the duct.
Source and basis: derived from the conservation equations with a wall shear term $\tau_w = f_F \rho v^2 / 2$; the friction factor is an empirical input (see [Control volumes and pipe flow](11-control-volumes-pipe-flow.md)).

Example. For air entering at $\mathrm{Ma} = 2$, $4 f_F L^* / D = 0.3050$. With $f_F = 0.003$ and $D = 0.1\ \text{m}$ the duct can run $L^* = 2.54\ \text{m}$ before the flow reaches $\mathrm{Ma} = 1$. At $\mathrm{Ma} = 2$ the ratios are $T/T^* = 0.6667$ and $p/p^* = 0.4082$. A longer duct would shock.

<details><summary>Verification</summary>

```verify
gam = q(1.4, "", of="none")
M = q(2, "")
fl = (1 - M**2) / (gam * M**2) + (gam + 1) / (2 * gam) * log((gam + 1) * M**2 / (2 + (gam - 1) * M**2))
expect(fl, "0.3050")
expect((gam + 1) / (2 + (gam - 1) * M**2), "0.6667")
expect(1 / M * sqrt((gam + 1) / (2 + (gam - 1) * M**2)), "0.4082")
f = q(0.003, "", of="none")
D = q(0.1, "m")
Ls = rnd(fl, 4, "") * D / (4 * f)
expect(Ls, "2.54 m")
```

</details>

## Rayleigh flow

**Rayleigh flow** is steady, frictionless, one-dimensional flow of a perfect gas in a constant-area duct with heat addition or removal. Heating drives the flow toward $\mathrm{Ma} = 1$ from either side. The maximum heat that a flow can absorb without changing its inlet state is the amount that brings it to $\mathrm{Ma} = 1$.

$$
\frac{p}{p^*} = \frac{\gamma+1}{1 + \gamma\,\mathrm{Ma}^2}, \qquad
\frac{T}{T^*} = \mathrm{Ma}^2\left(\frac{\gamma+1}{1 + \gamma\,\mathrm{Ma}^2}\right)^{2}, \qquad
\frac{T_0}{T_0^*} = \frac{(\gamma+1)\,\mathrm{Ma}^2\left[2 + (\gamma-1)\mathrm{Ma}^2\right]}{\left(1 + \gamma\,\mathrm{Ma}^2\right)^2}
$$

The heat added per unit mass between two sections is $q = c_p (T_{02} - T_{01})$.

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $p$ | static pressure at the section | Pa |
| $T$ | static temperature at the section | K |
| $p^*$ | static pressure at the sonic state of the same flow | Pa |
| $T^*$ | static temperature at the sonic state of the same flow | K |
| $T_0$, $T_0^*$ | stagnation temperature at the section and at the sonic state | K |
| $\mathrm{Ma}$ | Mach number at the section | dimensionless |
| $\gamma$ | heat capacity ratio | dimensionless |
| $q$ | heat added per unit mass of gas | J/kg |
| $c_p$ | specific heat at constant pressure | J/(kg K) |

Holds when: the duct has constant area, friction is negligible, and the gas is perfect with constant $c_p$. Heat addition by combustion is modeled as a stagnation-temperature rise only; the molar mass and $\gamma$ of the products are taken as unchanged.
Breaks when: friction is not small (combine Fanno and Rayleigh effects numerically), combustion changes the gas composition (use the products' $\gamma$ and $R_s$ on each side), or the heat added exceeds the choking limit, which makes the inlet flow adjust.
Source and basis: derived from mass, momentum, and energy with a heat term $q = c_p\,\Delta T_0$ and no wall shear.

Example. At $\mathrm{Ma} = 2$ in air the sonic ratios are $p/p^* = 0.3636$, $T/T^* = 0.5289$, and $T_0/T_0^* = 0.7934$. Air entering a duct at $\mathrm{Ma} = 2$ with $T_{01} = 500\ \text{K}$ reaches $\mathrm{Ma} = 1$ when $T_0$ rises to $T_{01}/0.7934 = 630.2\ \text{K}$. The heat added is 130.85 kJ/kg, using $c_p = 1005\ \text{J/(kg K)}$.

<details><summary>Verification</summary>

```verify
gam = q(1.4, "", of="none")
M = q(2, "")
expect((gam + 1) / (1 + gam * M**2), "0.3636")
expect(M**2 * ((gam + 1) / (1 + gam * M**2))**2, "0.5289")
t0r = (gam + 1) * M**2 * (2 + (gam - 1) * M**2) / (1 + gam * M**2)**2
expect(t0r, "0.7934")
T01 = q(500, "K")
T0s = T01 / rnd(t0r, 4, "")
expect(T0s, "630.2 K")
cp = q(1005, "J/kg K", of="none")
expect(cp * (T0s - T01), "130.85 kJ/kg")
```

</details>

## Variable-property and real-gas limits

A perfect gas has constant $c_p$ and $\gamma$. Real gases depart from that, and the departure sets the limit of every relation above.

Typical values for air (typical, near 1 atm):

| Temperature | $\gamma$ (typical) | Note |
|---|---|---|
| 300 K | 1.40 | Translation and rotation only |
| 1000 K | about 1.33 | Vibration of $\text{N}_2$ and $\text{O}_2$ partly excited |
| 2000 K | about 1.29 | Vibration strongly excited |
| above about 2500 K | falls further | Oxygen dissociates, then nitrogen near 4000 K |

These values come from the temperature dependence of molecular heat capacity, which follows from quantum energy levels (see [Modern physics and quantum](18-modern-physics-and-quantum.md)). Use tabulated or computed properties for any gas that reaches such temperatures.

- Where the temperature stays below about 800 K, calorically perfect air with $\gamma = 1.4$ is accurate to a few percent in the isentropic and shock relations.
- Stagnation temperature in a hypersonic flow can far exceed that limit. A flow at $\mathrm{Ma} = 7$ in air at 220 K has $T_0 = 220 \times (1 + 0.2 \times 49) = 2376\ \text{K}$ for perfect gas, where the real value is lower because internal modes absorb energy.
- Cryogenic and high-pressure gases need a real-gas equation of state. At a reduced pressure above about 0.1 the compressibility factor departs from 1 and the perfect-gas relations lose accuracy.
- Condensation. Fast expansion of humid air or a vapor can supercool it below saturation and then condense suddenly, a **condensation shock**. The release of latent heat acts as heat addition (Rayleigh flow) and can choke a wind tunnel or nozzle. Dry the air or heat it before expanding.
- Different gases change the numbers directly. Monatomic gases have $\gamma = 5/3$, diatomic gases near room temperature have $\gamma = 7/5$, and complex molecules fall toward 1.1 to 1.3 (typical).

<details><summary>Verification</summary>

```verify
gam = q(1.4, "", of="none")
Ma = q(7, "")
T = q(220, "K", of="none")
expect(T * (1 + (gam - 1) / 2 * Ma**2), "2376 K")
```

</details>

Source and basis: derived from the kinetic theory of gas heat capacity; the high-temperature values need a property library and are not reproduced here.

## Checklists

- State the gas, $\gamma$, $R_s$, the stagnation conditions, and the sign conventions before any calculation.
- Find the Mach number first. It decides which relations apply and whether density changes matter.
- Check subsonic or supersonic at every station. The same area ratio gives two Mach numbers.
- Check for choking at every throat and in every long duct. A choked throat fixes the mass flow.
- Use stagnation quantities across isentropic stretches and the shock relations across shocks. Stagnation temperature is conserved across a shock; stagnation pressure is not.
- Use static pressure for force and thrust, stagnation pressure for pitot readings, and know which one a gauge shows.
- Confirm the shock is physically allowed. Entropy must rise, so the upstream flow must be supersonic.
- For an oblique shock, check that the deflection is below the maximum for the Mach number, and say whether the weak or strong branch applies.
- For a duct with friction or heat, compare the actual length or heat added with the choking limit before using the Fanno or Rayleigh ratios.
- Check the temperature range against the perfect-gas limit before trusting $\gamma = 1.4$.
- Recompute one result by a second route (for example exit speed from energy and from Mach number).

## Sanity checks

- Air at ambient temperature has a speed of sound near 340 m/s; a jet at 340 m/s is at $\mathrm{Ma} = 1$.
- Isentropic flow at $\mathrm{Ma} = 1$ has $T/T_0 = 0.833$ and $p/p_0 = 0.528$ for $\gamma = 1.4$. A converging nozzle chokes at a pressure ratio $p_0/p_b$ of at least 1.893; a converging-diverging nozzle can choke at a higher back pressure set by its area ratio.
- Across a normal shock, pressure, density, and temperature all rise and $\mathrm{Ma}$ falls below 1. If any property falls, the shock is wrong.
- The stagnation pressure ratio across a normal shock is below 1 for every $\mathrm{Ma}_1 > 1$ and equals 1 only at $\mathrm{Ma}_1 = 1$.
- Choked flow for air is about $0.0404\, A^* p_0 / \sqrt{T_0}$ in kg/s with $A^*$ in $\text{m}^{2}$, $p_0$ in Pa and $T_0$ in K. For $\gamma = 1.4$ and $R_s = 287\ \text{J/(kg K)}$, a throat of $1\ \text{m}^{2}$ at $100\ \text{kPa}$ and $400\ \text{K}$ passes 202.1 kg/s.
- Thrust of a matched nozzle is of the order of $C_F p_0 A^*$ with $C_F$ between about 1.2 and 1.9 for $\gamma$ near 1.2 to 1.4 and large expansion ratios (typical).
- A Prandtl-Meyer expansion raises the Mach number and lowers the pressure; an oblique shock does the opposite.
- Friction pushes both subsonic and supersonic flow toward $\mathrm{Ma} = 1$; heating does the same, and cooling pushes away from it.

<details><summary>Verification</summary>

```verify
gam = q(1.4, "", of="none")
Rs = q(287.0, "J/kg K", of="none")
pcr = (2 / (gam + 1))**(gam / (gam - 1))
expect(1 / pcr, "1.893")
mdot = q(1, "m^2") * q(100, "kPa", of="none") * sqrt(gam / (Rs * q(400, "K"))) * (2 / (gam + 1))**((gam + 1) / (2 * (gam - 1)))
expect(mdot, "202.1 kg/s")
given("0.0404")
```

</details>

## Further reference

- Anderson, *Modern Compressible Flow with Historical Perspective*. A full derivation of every relation on this sheet, with tables.
- Shapiro, *The Dynamics and Thermodynamics of Compressible Fluid Flow*. The classic treatment of Fanno and Rayleigh flow.
- Liepmann and Roshko, *Elements of Gasdynamics*.
- Ames Research Staff, *Equations, Tables, and Charts for Compressible Flow*, NACA Report 1135, hosted by NASA, for the isentropic, shock, Fanno, and Rayleigh tables.
- [NASA Glenn Beginner's Guide to Aeronautics](https://www.grc.nasa.gov/www/k-12/airplane/shortc.html) for short derivations and calculators of the isentropic and shock relations.
- Fluid mechanics and compressible flow notes in MIT OpenCourseWare 16.120 for the aerospace treatment.
- Related sheets and lessons. [Thermofluids reference](reference-thermofluids.md), [Control volumes and pipe flow](11-control-volumes-pipe-flow.md), [Orbital mechanics and rockets](15-orbital-mechanics-and-rockets.md).
