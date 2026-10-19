# Simulation verification and validation claims

**Type:** data

Facts about published grid convergence methods and the NASA modeling and simulation standard. Field rules are in [VERIFICATION.md](../../VERIFICATION.md#claims).

### nasa-grc-spatial-convergence
- Claim: The NASA Glenn Research Center verification and validation tutorial gives the observed order of convergence from three grids with constant refinement ratio, and Richardson extrapolation as an estimate of the continuum value.
- Values: NASA Glenn
- Layer: durable
- Status: verified-1
- Sources: nasa-grc-cfd-vv (spatial convergence page, https://www.grc.nasa.gov/www/wind/valid/tutorial/spatconv.html, "estimate of the continuum value")
- Checked: agent:sonnet, 2026-10-18, fetched the page and matched the formulas and the quoted words

### nasa-grc-refinement-ratio
- Claim: The NASA Glenn Research Center verification and validation tutorial states a minimum grid refinement ratio of 1.1 to distinguish discretization error from other error sources, and notes that a ratio of 2 has traditionally been used.
- Values: 1.1; 2
- Layer: durable
- Status: verified-1
- Sources: nasa-grc-cfd-vv (spatial convergence page, https://www.grc.nasa.gov/www/wind/valid/tutorial/spatconv.html, "minimum of r >= 1.1" and "Traditionally, Richardson extrapolation has been used with grid refinement ratios of r = 2")
- Checked: agent:codex, 2026-10-19, fetched the page and matched the ratio guidance and quoted words

### nasa-grc-gci-safety-factors
- Claim: For the grid convergence index, the NASA Glenn tutorial recommends a safety factor of 3.0 for comparisons of two grids and 1.25 for three or more grids.
- Values: 3.0; 1.25
- Layer: durable
- Status: verified-1
- Sources: nasa-grc-cfd-vv (spatial convergence page, https://www.grc.nasa.gov/www/wind/valid/tutorial/spatconv.html, "Fs=1.25 for comparisons over three or more grids")
- Checked: agent:sonnet, 2026-10-18, fetched the page and matched the safety factors and the quoted words

### nasa-std-7009-purpose
- Claim: NASA-STD-7009, Standard for Models and Simulations, Version B, Change 1, establishes uniform practices in modeling and simulation.
- Values: NASA-STD-7009; Version B
- Layer: dated
- Status: verified-1
- Sources: nasa-std-7009 (standard page, https://standards.nasa.gov/standard/nasa/nasa-std-7009, "establishes uniform practices in modeling and simulation")
- Checked: agent:sonnet, 2026-10-18, fetched the page and matched the title, version, and purpose words
- As of: 2026
- Review by: 2031-10-18
