# History claims

**Type:** data

Dated and attributed facts about the history of engineering. Each heading is a claim key; lessons cite a claim by linking to its heading. The verifier checks that the citing sentence states every value in `Values`, that each source exists in [sources](../sources.md), and that the status matches the evidence. Field rules are in [VERIFICATION.md](../../VERIFICATION.md).

### newcomen-engine-1705
- Claim: Thomas Newcomen built an atmospheric steam engine in about 1705.
- Values: ~1705
- Layer: durable
- Status: verified-1
- Sources: eb1911 (article "Newcomen, Thomas": "he constructed in 1705 a fire-engine, now known as the atmospheric steam-engine")
- Checked: agent:opus, 2026-10-18, fetched the article and matched the quoted words

### newcomen-mine-pumping-1711
- Claim: Engines of Newcomen's design began pumping water from mines in about 1711.
- Values: ~1711
- Layer: durable
- Status: verified-1
- Sources: eb1911 (article "Steam Engine", section 10: "About 1711 Newcomen's engine began to be introduced for pumping mines")
- Checked: agent:opus, 2026-10-18, fetched the article and matched the quoted words

### watt-model-repair-1760s
- Claim: James Watt, instrument maker to the University of Glasgow, repaired the university's model Newcomen engine in the 1760s.
- Values: 1760s
- Layer: durable
- Status: verified-1
- Sources: eb1911 (article "Watt, James": instrument maker to the university from 1757; the model of Newcomen's engine was "given him to repair" in 1764)
- Checked: agent:opus, 2026-10-18, fetched the article and matched the quoted words

### watt-condenser-patent-1769
- Claim: Watt's patent covering the separate condenser was granted in 1769.
- Values: 1769
- Layer: durable
- Status: verified-1
- Sources: eb1911 (article "Watt, James": the patent "was not obtained till January 1769"); eb1911 (article "Steam Engine", section 11: gives 1769 for Watt's patent of his improvements)
- Checked: agent:opus, 2026-10-18, fetched both articles and matched the quoted words; both are one source group

### boulton-watt-partnership-1775
- Claim: Matthew Boulton and James Watt formally entered into partnership in 1775, the year an act of parliament extended Watt's 1769 patent to 1799.
- Values: 1775
- Layer: durable
- Status: verified-1
- Sources: eb1911 (article "Boulton, Matthew": "Three years later Boulton and Watt formally entered into partnership", counted from the 1772 settlement; same paragraph: the act "extending the term of Watt's 1769 patent to 1799")
- Checked: agent:opus, 2026-10-18, fetched the article; the year is counted from the article's own dates, not printed as 1775

### watt-sun-and-planet-1781
- Claim: Watt's second steam engine patent, for rotary motion by sun and planet wheels, is dated 1781.
- Values: 1781
- Layer: durable
- Status: verified-1
- Sources: eb1911 (article "Watt, James": "Watt's second steam-engine patent is dated 1781")
- Checked: agent:opus, 2026-10-18, fetched the article and matched the quoted words

### watt-double-acting-1782
- Claim: Watt's third patent, in 1782, included the double-acting engine.
- Values: 1782
- Layer: durable
- Status: verified-1
- Sources: eb1911 (article "Watt, James": "A third patent, in 1782, contained two new inventions of the first importance")
- Checked: agent:opus, 2026-10-18, fetched the article and matched the quoted words

### iron-bridge-1779
- Claim: The Iron Bridge over the Severn at Coalbrookdale, overseen by Abraham Darby III, was completed in 1779 and opened to traffic in 1781.
- Values: 1779; Abraham Darby III
- Layer: durable
- Status: verified-1
- Sources: eh-iron-bridge (history page: "completed in 1779 and opened to traffic in 1781"; "Overseen by Darby's grandson Abraham Darby III"); eb1911 (article "Coalbrookdale": "The third Abraham Darby built the famous Coalbrookdale iron bridge over the Severn")
- Checked: agent:opus, 2026-10-18, fetched both pages; the year rests on one source, the builder on two

### iron-bridge-first
- Claim: The Iron Bridge was the first iron bridge.
- Values: first iron bridge
- Layer: durable
- Status: verified-1
- Sources: eh-iron-bridge (history page: "the world's first iron bridge")
- Checked: agent:opus, 2026-10-18, fetched the page and matched the quoted words

### maudslay-screw-lathe-1800
- Claim: Henry Maudslay built a screw-cutting lathe in about 1800; his firm worked in London.
- Values: ~1800
- Layer: durable
- Status: verified-1
- Sources: smg-collection (object co46284, "Henry Maudslay's original screw-cutting lathe, c.1800"; object co46317, "Triangular Bar Lathe by H. Maudslay & Co., London")
- Checked: agent:opus, 2026-10-18, fetched the collection search and matched the object titles

### rocket-rainhill-1829
- Claim: The locomotive Rocket won the trials held at Rainhill in 1829.
- Values: 1829; Rainhill
- Layer: durable
- Status: verified-2
- Sources: smg-collection (object co26704, Rocket: "the clear winner in the locomotive trials held at Rainhill in 1829"); eb1911 (article "Stephenson, George": "the competition held at Rainhill in October 1829")
- Checked: agent:opus, 2026-10-18, fetched both pages and matched the quoted words

### rocket-design
- Claim: Rocket was designed by Robert Stephenson and built by Robert Stephenson and Company in Newcastle upon Tyne.
- Values: designed by Robert Stephenson
- Layer: durable
- Status: disputed
- Sources: smg-collection (object co26704: "designed by Robert Stephenson and made by Robert Stephenson & Co., Newcastle upon Tyne, England, 1829"); eb1911 (article "Stephenson, George": calls Rocket "his engine", crediting George Stephenson)
- Dispute: the museum that holds the engine credits the design to Robert Stephenson; the 1911 encyclopedia credits George Stephenson. State Robert as designer, name George as his partner, and cite this claim.
- Checked: agent:opus, 2026-10-18, fetched both pages and matched the quoted words
- Watch: Stephenson.{0,60}\bRocket\b|\bRocket\b.{0,60}Stephenson
- Require: Robert Stephenson

### lmr-opened-1830
- Claim: The Liverpool and Manchester Railway opened on 15 September 1830; George Stephenson worked on its construction.
- Values: 1830; George Stephenson
- Layer: durable
- Status: verified-1
- Sources: eb1911 (article "Stephenson, George": "his employment in the construction of the Liverpool & Manchester railway"; "On the 15th of September in the following year the railway was formally opened", the year after the 1829 trials)
- Checked: agent:opus, 2026-10-18, fetched the article; the year is counted from the article's own dates

### bessemer-process-1856
- Claim: Henry Bessemer first announced his process of blowing air through molten pig iron in 1856.
- Values: 1856
- Layer: durable
- Status: verified-1
- Sources: eb1911 (article "Bessemer, Sir Henry": "The first public announcement of the process was made at the Cheltenham meeting of the British Association in 1856")
- Checked: agent:opus, 2026-10-18, fetched the article and matched the quoted words

### whitney-firearms-1798
- Claim: Eli Whitney began making firearms near New Haven in 1798 under government contracts.
- Values: 1798
- Layer: durable
- Status: verified-1
- Sources: eb1911 (article "Whitney, Eli": "began the manufacture of fire-arms near New Haven (1798) and secured profitable government contracts")
- Checked: agent:opus, 2026-10-18, fetched the article and matched the quoted words

### archimedes-water-screw
- Claim: Archimedes, who lived from about 287 to 212 BC, invented the water screw.
- Values: ~287; 212 BC
- Layer: durable
- Status: verified-1
- Sources: eb1911 (article "Archimedes": "(c. 287-212 B.C.)"; "The water-screw which he invented")
- Checked: agent:opus, 2026-10-18, fetched the article and matched the quoted words
