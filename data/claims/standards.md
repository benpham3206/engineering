# Standards claims

**Type:** data

Facts about published standards: their numbers, titles, editions, publishers, and what they cover. A standard's edition ages, so these claims use layer `dated`, with `As of` and a `Review by` date about five years ahead. Only facts checkable on a free public page are registered; a paywalled standard is named by title in prose, with no claim about its contents. Field rules are in [VERIFICATION.md](../../VERIFICATION.md#claims).

### nist-fips-203-204-205-2024
- Claim: NIST published its first three finalized post-quantum cryptography standards in 2024: FIPS 203 (ML-KEM, for general encryption), FIPS 204 (ML-DSA, for digital signatures), and FIPS 205 (SLH-DSA, a backup signature method).
- Values: FIPS 203; FIPS 204; FIPS 205; 2024
- Layer: dated
- Status: verified-1
- Sources: nist-pqc-2024 (news release dated August 13, 2024, "NIST Releases First 3 Finalized Post-Quantum Encryption Standards": FIPS 203 is "intended as the primary standard for general encryption", FIPS 204 "intended as the primary standard for protecting digital signatures", FIPS 205 "intended as a backup method in case ML-DSA proves vulnerable")
- Checked: agent:opus, 2026-10-18, fetched the NIST page and matched the title, date, and quoted words
- As of: 2026
- Review by: 2031-10-18
