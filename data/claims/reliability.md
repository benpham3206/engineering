# Reliability claims

**Type:** data

Empirical and attributed methods used by the reliability reference sheet. Field rules are in [VERIFICATION.md](../../VERIFICATION.md#claims).

### median-rank-approximation
- Claim: A published reliability handbook gives the median rank approximation for the failure fraction of the i-th failure among n units on test as (i - 0.3)/(n + 0.4), recommended over i/n.
- Values: 0.3; 0.4
- Layer: durable
- Status: verified-1
- Sources: nist-sematech-handbook (section 8.2.2.1, "Probability plotting", "100(i-0.3)/(n+0.4)")
- Checked: agent:sonnet, 2026-10-18, fetched the handbook page and read the formula

### bathtub-curve
- Claim: The bathtub curve of failure rate against age has an early region of high, rapidly decreasing failure rate, a long region of roughly level failure rate, and a wear-out region of rising failure rate.
- Values: bathtub curve
- Layer: durable
- Status: verified-1
- Sources: nist-sematech-handbook (section 8.1.2.4, "Bathtub curve", "high but rapidly decreasing failure rate")
- Checked: agent:sonnet, 2026-10-18, fetched the handbook page and read the description of the three regions

### beta-factor-common-cause
- Claim: In the beta factor model of common cause failure, beta represents the fraction of the failure rate that is common to multiple susceptible components.
- Values: beta factor
- Layer: durable
- Status: verified-1
- Sources: nasa-fault-tree-handbook (section 5.2, page 59, "fraction of the failure rate that is common to multiple susceptible components")
- Checked: agent:sonnet, 2026-10-18, downloaded the handbook PDF and read section 5.2

### rare-event-approximation
- Claim: The probability of a fault tree top event can be approximated as the sum of the minimal cut set probabilities when they are small, typically accurate for basic event probabilities below 0.1, and it errs on the conservative side.
- Values: 0.1
- Layer: durable
- Status: verified-1
- Sources: nasa-fault-tree-handbook (section 7.1, "typically an accurate approximation for basic event probabilities below 0.1")
- Checked: agent:sonnet, 2026-10-18, downloaded the handbook PDF and read section 7.1 and Appendix B equation B.8
