# Heat transfer claims

**Type:** data

Standard textbook statements about conduction and radiation that the heat transfer reference sheet cites. Field rules are in [VERIFICATION.md](../../VERIFICATION.md#claims).

### openstax-conduction-form
- Claim: OpenStax University Physics Volume 2, section 1.6, gives the conduction rate as proportional to thermal conductivity, area, and temperature difference, and inversely proportional to thickness.
- Values: thermal conductivity; thickness
- Layer: durable
- Status: verified-1
- Sources: openstax-up-2 (section 1.6 "Mechanisms of Heat Transfer", conduction formula "P = dQ/dt = kA(Th − Tc)/d")
- Checked: agent:sonnet, 2026-10-19, fetched the OpenStax section page and read the conduction formula

### openstax-radiation-form
- Claim: OpenStax University Physics Volume 2, section 1.6, gives net radiative heat transfer as the Stefan-Boltzmann constant times emissivity, area, and the difference of the fourth powers of absolute temperature.
- Values: emissivity; fourth powers
- Layer: durable
- Status: verified-1
- Sources: openstax-up-2 (section 1.6 "Mechanisms of Heat Transfer", net radiation formula "Pnet = σeA(T2⁴ − T1⁴)")
- Checked: agent:sonnet, 2026-10-19, fetched the OpenStax section page and read the net radiation formula

### lienhard-laminar-pipe-nu
- Claim: For fully developed laminar flow in a circular pipe, the Nusselt number based on diameter is 4.364 for uniform wall heat flux and 3.657 for uniform wall temperature.
- Values: 4.364; 3.657
- Layer: durable
- Status: verified-1
- Sources: lienhard-ahtt (6th edition, Chapter 7, section 7.2, eqn. (7.22) "= 4.364 (qw = constant)" and eqn. (7.23) "NuD = 3.657 for Tw = constant")
- Checked: agent:sonnet, 2026-10-19, fetched the official PDF and read both equations in the extracted text

### lienhard-turbulent-pipe
- Claim: Colburn's turbulent pipe correlation is Nu = 0.023 Re^0.8 Pr^(1/3) and Dittus and Boelter's heating form is Nu = 0.0243 Re^0.8 Pr^0.4, for smooth pipes with Re at least 10000, with errors up to +25% and -40% for Pr from 0.67 to 100.
- Values: 0.023; 0.0243
- Layer: durable
- Status: verified-1
- Sources: lienhard-ahtt (6th edition, Chapter 7, section 7.3, eqns. (7.38), (7.39a), (7.39b), pp. 368-369, "This equation is called the Colburn equation")
- Checked: agent:sonnet, 2026-10-19, fetched the official PDF and read the equations and the stated error range in the extracted text

### lienhard-gnielinski
- Claim: Gnielinski's equation Nu = (f/8)(Re - 1000)Pr / [1 + 12.7 sqrt(f/8)(Pr^(2/3) - 1)], with f from Filonenko's 1/(1.82 log10 Re - 1.64)^2, holds for 2300 <= Re <= 5e6 and 0.6 <= Pr <= 1e5 in smooth pipes.
- Values: 12.7; 1000; 1.82; 1.64; 2300
- Layer: durable
- Status: verified-1
- Sources: lienhard-ahtt (6th edition, Chapter 7, section 7.3, eqns. (7.41) and (7.42), p. 369, "Gnielinski proposed the following modification of eqn. (7.35)")
- Checked: agent:sonnet, 2026-10-19, fetched the official PDF and read both equations and the validity range

### lienhard-turbulent-pipe-property-correction
- Claim: Lienhard corrects the Gnielinski Nusselt number for large property changes using (mu_b/mu_w)^n for liquids and (Tb/Tw)^n for gases. For a cooled wall, Tw < Tb, n is 0.11 for liquids and 0.47 for gases; the corrections cover 0.025 <= mu_b/mu_w <= 12.5 and 0.27 <= Tb/Tw <= 2.7, respectively.
- Values: 0.11; 0.47; 0.025; 12.5; 0.27; 2.7
- Layer: durable
- Status: verified-1
- Sources: lienhard-ahtt (6th edition, Chapter 7, section 7.3, eqns. (7.44) and (7.45), p. 370, "all properties evaluated at Tb using eqn. (7.41)"; for gases, "0.47 for Tw < Tb")
- Checked: agent:sonnet, 2026-10-19, fetched the official PDF and read both correction equations and their ranges

### lienhard-plate-laminar
- Claim: For a laminar boundary layer on an isothermal flat plate with Pr at least 0.6, the average Nusselt number is NuL = 0.664 ReL^(1/2) Pr^(1/3), with properties at the film temperature.
- Values: 0.664; 0.6
- Layer: durable
- Status: verified-1
- Sources: lienhard-ahtt (6th edition, Chapter 6, section 6.5, eqn. (6.68) "NuL = 0.664 ReL^1/2 Pr^1/3, Pr >= 0.6"; film temperature statement after eqn. (6.43))
- Checked: agent:sonnet, 2026-10-19, fetched the official PDF and read the equation and the property rule

### lienhard-plate-turbulent
- Claim: For a turbulent flat-plate boundary layer, Stx = (Cf/2) / [1 + 12.7 sqrt(Cf/2)(Pr^(2/3) - 1)] for Pr at least 0.5 with Cf = 0.455/[ln(0.06 Rex)]^2, and the power laws are Nux = 0.0296 Rex^0.8 Pr^0.6 for gases and Nux = 0.032 Rex^0.8 Pr^0.43 for nonmetallic liquids.
- Values: 0.455; 0.06; 12.7; 0.0296; 0.032; 0.43
- Layer: durable
- Status: verified-1
- Sources: lienhard-ahtt (6th edition, Chapter 6, sections 6.7 and 6.8, eqns. (6.102), (6.111), (6.112), (6.113), "valid for smooth walls with zero or mild pressure gradients")
- Checked: agent:sonnet, 2026-10-19, fetched the official PDF; Cf form checked against the book's worked value 0.003232 at Rex = 2.371e6

### lienhard-churchill-bernstein
- Claim: Churchill and Bernstein's correlation for the average Nusselt number of a cylinder in crossflow is Nu = 0.3 + 0.62 Re^(1/2) Pr^(1/3) / [1 + (0.4/Pr)^(2/3)]^(1/4) times [1 + (Re/282000)^(5/8)]^(4/5), for Re Pr above 0.2 with properties at the film temperature.
- Values: 0.3; 0.62; 0.4; 282000
- Layer: durable
- Status: verified-1
- Sources: lienhard-ahtt (6th edition, Chapter 7, section 7.6, eqn. (7.65), pp. 390-391, "All properties in eqns. (7.65) to (7.68) are to be evaluated at a film temperature")
- Checked: agent:sonnet, 2026-10-19, fetched the official PDF and read the equation and its stated limits

### lienhard-churchill-chu
- Claim: For natural convection on a vertical isothermal plate, Churchill and Chu give NuL = 0.68 + 0.670 RaL^(1/4) / [1 + (0.492/Pr)^(9/16)]^(4/9) for laminar flow (RaL up to 1e9) and NuL = {0.825 + 0.387 RaL^(1/6) / [1 + (0.492/Pr)^(9/16)]^(8/27)}^2 for all RaL and Pr, with properties at the film temperature.
- Values: 0.68; 0.670; 0.492; 0.825; 0.387
- Layer: durable
- Status: verified-1
- Sources: lienhard-ahtt (6th edition, Chapter 8, section 8.3, eqns. (8.13a) and (8.13b), pp. 419-420, "This result can be used for all RaL and Pr")
- Checked: agent:sonnet, 2026-10-19, fetched the official PDF; (8.13a) reproduces the book's Example 8.1 value 47.33 at RaL = 6.78e7

### lienhard-chf
- Claim: The peak pool-boiling heat flux on a large horizontal flat plate is qmax = 0.149 rho_g^(1/2) h_fg [sigma g (rho_f - rho_g)]^(1/4), while the Zuber-Kutateladze form uses the constant 0.131.
- Values: 0.149; 0.131
- Layer: durable
- Status: verified-1
- Sources: lienhard-ahtt (6th edition, Chapter 9, section 9.3, eqns. (9.11) and (9.12), pp. 493-495, "actual qmax falls below that predicted by eqn. (9.11)" and "it then becomes greater")
- Checked: agent:sonnet, 2026-10-19, fetched the official PDF; the size trend was read in the text accompanying Fig. 9.12 and (9.11) reproduces Example 9.5

### lienhard-chf-small-heater
- Claim: For a side-walled heater narrower than about 3d1, actual peak pool-boiling heat flux first falls below the large-plate prediction as size decreases, then rises when one vapor column serves a sufficiently small area.
- Values: 3
- Layer: durable
- Status: verified-1
- Sources: lienhard-ahtt (6th edition, Chapter 9, section 9.3, text accompanying Fig. 9.12, p. 494, "actual qmax falls below that predicted by eqn. (9.11)" and "it then becomes greater")
- Checked: agent:sonnet, 2026-10-19, fetched the official PDF and read the size-trend discussion after equation (9.11)

### lienhard-lewis-analogy
- Claim: For low-rate mass transfer, the ratio of the heat transfer coefficient to the mass transfer conductance times specific heat is h/(g cp) = Le^(1-b), which is about Le^(2/3), and the Lewis number of air and water is about 0.847.
- Values: 2/3; 0.847
- Layer: durable
- Status: verified-1
- Sources: lienhard-ahtt (6th edition, Chapter 11, section 11.7, eqn. (11.73) and the text after it, "The Lewis number for air-water systems is about 0.847")
- Checked: agent:sonnet, 2026-10-19, fetched the official PDF and read the equation and the stated value
