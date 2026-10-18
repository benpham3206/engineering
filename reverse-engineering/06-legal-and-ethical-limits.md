# Legal and ethical limits

Taking things apart to learn how they work is a normal and valuable engineering activity. It is also one that can cross lines: into someone else's patent, into their copyrighted drawings, into a safety-critical part, or into a product whose license forbids it. This lesson gives a short set of checks to run before you take apart, measure, copy, or sell a reverse-engineered design. It is general information, not legal advice. Laws and contracts differ by country and by product.

**Prerequisites:** [Teardowns](01-teardowns.md)
**Time:** 2-3 h

## Core ideas

- **Learning from a product you own** is the usual starting point. Studying how a product works is a different act from copying it for sale.
- **Patents** protect an invention for a limited time. A patent is a right you apply for and, if granted, enforce. Reading a published patent to learn how a device works is a normal use of public information. Making, selling, or using a patented design without permission can infringe the patent, even if you rebuilt it yourself.
- **Copyright** protects original creative works, including drawings, CAD files, manuals, and photographs. Copying a copyrighted drawing or a 3D model is different from measuring a physical part and making your own drawing from those measurements. The distinction is a common source of confusion, so check before you publish a copied file.
- **Trade secrets** are confidential information a company protects by keeping it secret, such as a formula or a process. Reverse-engineering a product you bought is generally treated as a fair way to learn what is on the market, but it does not give you permission to use confidential information that someone else took or leaked.
- **Licenses and terms of use** can restrict what you do with software or a device. Some software licenses forbid decompiling it. Read the terms that came with the product you own, and do not assume they allow or forbid anything without reading them.
- **Trademarks** are brand names, logos, and trade dress. Making a copy that uses a brand to pass as the original is a problem even if the part itself is not patented.
- **Safety-critical parts** include brake components, pressure vessels, medical devices, electrical protection, and anything whose failure can injure a person. A reverse-engineered copy of one of these needs engineering verification and testing before anyone relies on it. A guess that looks close is not enough.
- **Defeating a protection** such as a safety interlock, an access lock, or a usage limit may be illegal in some places even when the act is only for personal study. Do not do it on products that are not yours.

### Checklist before you start a reverse-engineering project

- [ ] You own the product, or you have permission from its owner to take it apart.
- [ ] You know whether the product or its software is covered by a license or terms of use, and you have read them.
- [ ] You have searched for patents on the feature you care about, and you know what they claim.
- [ ] You are drawing your own measurements and models, not copying a supplier's drawing or CAD file.
- [ ] You are not using a brand name or logo to suggest the copy is genuine.
- [ ] The part is not safety-critical, or you have a plan for engineering checks before any real use.
- [ ] You are not defeating a lock, an interlock, or a usage limit.
- [ ] You know what you will do with the result: personal learning, a repair, a school project, or sale. Sale raises the most questions.

## Example

A learner wants to rebuild the crank arm of a bicycle they own, and later sell copies online.

1. **Ownership:** The bike is theirs, so taking it apart and measuring it is allowed. Pass.
2. **Patents:** The learner searches public patent records for "crank arm" and finds patents on a specific spider design. The patent claims a particular hollow arm profile. Their plan is to copy that profile for sale. Stop here: copying a patented profile for sale may infringe, so the learner should either design a different profile or get legal advice.
3. **Copyright:** The learner plans to use a manufacturer's published CAD file. Stop: that file is copyrighted, so the learner should model the crank from their own measurements instead.
4. **Safety:** A crank is a load-bearing part whose failure can throw a rider off the bike. The learner needs engineering verification, such as fatigue and load testing, before any sale.
5. **Result:** Personal study and a repair are fine. Sale needs a different profile from the patent, an own-measured model, and testing to a recognized standard.

The example shows the order of checks: ownership, patents, copyright, then safety. Each stop point changes what the learner may do next.

## Practice

1. A learner checks 4 items on the checklist and 3 are done. How many are not done?
2. A patent search returns 6 patents on a feature, and 2 are relevant to the learner's design. How many are not relevant?
3. A bike spider has 5 arms, each with 1 bolt. How many bolts are on the spider in total?
4. A product has 3 safety-critical parts and 5 non-critical parts. How many parts in total need an engineering test plan before sale?
5. A learner has 9 checklist items and must complete all of them. How many more items must they complete if they have done 6?

<details><summary>Answers</summary>

1. 1
2. 4
3. 5
4. 3
5. 3

</details>

## Common mistakes

- Assuming that because a product was bought, anything can be done with its design. Ownership of a thing is not the same as a right to copy its design.
- Believing a patent only matters for the exact part. A patent claim can cover a feature in a different shape, so read the claims.
- Using a manufacturer's drawing to save time. That is copying, and it is a copyright issue even when the part is your own.
- Selling a safety-critical part after only a visual match. Matching appearance is not proof of strength.
- Treating this lesson as legal advice. Ask a qualified patent or IP lawyer before you commercialize a design.

## Go deeper

- [Patent Basics](https://www.uspto.gov/patents/basics) by the U.S. Patent and Trademark Office: the official U.S. government overview of how patents work.
- [Control of Hazardous Energy (Lockout/Tagout)](https://www.osha.gov/control-hazardous-energy) by OSHA: a free U.S. government guide to controlling dangerous energy during work on equipment.
- [Engineering LibreTexts](https://eng.libretexts.org/) by LibreTexts: free engineering books for the design and safety topics behind this lesson.
- See also the [design folder](../design/README.md) for how safety and standards shape design choices.
