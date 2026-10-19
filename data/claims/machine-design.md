# Machine design claims

**Type:** data

Empirical machine-element relations taken from published course notes: the rolling bearing life exponents and the Lewis gear tooth bending equation. Field rules are in [VERIFICATION.md](../../VERIFICATION.md#claims).

### bearing-life-exponents
- Claim: Rolling bearing load-life follows the relation load to the power a times life equals a constant, with a = 3 for ball bearings and a = 10/3 (3.333) for roller bearings.
- Values: 3; 10/3
- Layer: durable
- Status: verified-1
- Sources: mit-ocw-272 (Lecture 07, "Rolling contact bearings", slide 18, "a = 3 for ball bearings", "a = 3.333 for roller bearings")
- Checked: agent:sonnet, 2026-10-18, downloaded the lecture PDF, extracted its text, and matched the quoted words

### lewis-gear-bending
- Claim: The Lewis equation models a gear tooth as a cantilever and gives the root bending stress as the tangential load times the diametral pitch over the face width times the Lewis form factor Y, where Y is a function of the number of teeth.
- Values: Lewis form factor
- Layer: durable
- Status: verified-1
- Sources: mit-ocw-272 (Lecture 13, "Gear failure prevention", slides 14 and 15, "Y: Lewis form factor", "f( # of teeth )")
- Checked: agent:sonnet, 2026-10-18, downloaded the lecture PDF, extracted its text, and matched the quoted words
