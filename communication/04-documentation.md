# Documentation

**Type:** lesson

A design is only as useful as the record of why it looks the way it does. Documentation covers the specifications, test records, change history, and user instructions that let someone else build, operate, maintain, or fix a product years later.

**Prerequisites:** [01-technical-writing.md](01-technical-writing.md) and [02-engineering-drawings.md](02-engineering-drawings.md).
**Time:** 4-6 h

## Core ideas

- **Document the decisions behind the result.** The drawing says what the part is. The record says why the wall is 4 mm thick and what was rejected. Future engineers need the reasons to change the design safely.
- **Each document has one owner and one purpose.** A spec defines requirements. A test report records what was measured. A user manual tells an operator what to do. Do not mix them.
- **Requirements are testable.** "The enclosure should be strong" cannot be verified. "The enclosure shall survive a 1 m drop onto concrete without loss of function" can be.
- **Versions and revisions matter.** Every document needs a revision letter or number, a date, and a change note. Readers must be able to tell which version they are reading.
- **Documentation goes out of date.** A document that disagrees with the current design is worse than none. Update it in the same change that changes the design.

### Common types of engineering documentation

- **Requirements specification.** The list of what the product must do, with a unique ID for each requirement and a way to verify it.
- **Design description.** How the design meets the requirements, including the main trade-offs and assumptions.
- **Calculation record.** The equations, inputs, and results for each analysis. Include the source of each input value.
- **Test plan and test report.** The plan states what will be tested, how, and the pass criteria. The report states what was done, the results, and any deviations.
- **Bill of materials (BOM).** A list of every part with its part number, quantity, and supplier.
- **Change log.** A dated list of changes with the reason and the revision affected.
- **User or maintenance manual.** Step-by-step instructions for use, safety, and routine care.

### Writing for maintainers

- Start with the purpose of the document and who should use it.
- Use the same names for parts and signals across all documents. Do not call the same part "bracket" in one place and "mount" in another.
- Define every abbreviation in a glossary or at first use.
- Include the assumptions behind any number. A stress value is only meaningful with the load and geometry that produced it.
- Put a table of contents and an index in any document longer than a few pages.
- Link to the source file, drawing, or data set rather than copying its contents, so there is one place to update.

### Keeping it current

- Store documents in one version-controlled location. Each change should be traceable to a person and a date.
- Review documents at each design milestone and at the end of the project.
- When a design changes, list every document that refers to it and update them together.

## Checklist

Use this to review a document before release.

- [ ] Document title, number, revision, date, and author are present.
- [ ] Purpose and scope are stated in the first section.
- [ ] Every requirement has a unique ID and a verification method.
- [ ] Every number has a unit and a stated condition.
- [ ] Assumptions and their sources are listed.
- [ ] Terms match those used in the drawings and other documents.
- [ ] A change log records what changed and why.
- [ ] Cross-references to drawings, test reports, and other documents are current.
- [ ] The document has been read by someone who did not write it.

## Example

**Task.** You are documenting the decision to use a 4 mm wall in a plastic enclosure. Write the calculation record entry and the change log entry.

**Calculation record entry (outline).**

- **Document ID and revision.** "CALC-012, rev A."
- **Purpose.** Check whether a 4 mm wall meets the stiffness requirement REQ-07.
- **Inputs.** Load of 50 N applied at the center of the lid. Material: a polycarbonate with its stated modulus from the supplier data sheet. Wall dimensions from drawing ENC-001 rev C.
- **Method.** Use a simple beam deflection formula for a clamped plate. State the formula and the boundary condition assumed.
- **Result.** Predicted deflection, with units, and comparison with the limit in REQ-07.
- **Assumptions.** Linear elastic behavior at room temperature. Load applied at a single point.
- **Conclusion.** The design meets REQ-07 under the stated assumptions. The assumption about a single load point is verified in test plan TP-03.

**Change log entry.**

- "rev C, 2026-10-01: Wall thickness changed from 3 mm to 4 mm to meet REQ-07. See CALC-012 rev A. Affects drawing ENC-001 and BOM item 4."

**Sanity check.** Could a new engineer, reading only these two entries, explain what changed, why, and what would need to be re-checked if the material changed? If not, add the missing input or assumption.

## Practice

1. Write a README for a project of yours: what it is, how to build or run it, what it needs, and its known limits.
2. Start an engineering notebook entry for today's work, with date, goal, what you did, results, and next steps.
3. Write a revision history table for a drawing that has changed twice, with revision letter, date, description, and author.
4. Hand your README to someone else and watch them follow it without help. Write down every place they got stuck.

<details><summary>What a good answer includes</summary>

1. A stranger could set it up from the README alone, and the limits section is honest.
2. The entry is dated, says what you expected and what happened, and records raw numbers and conclusions.
3. Revisions run A, B, C in order, and each description says what changed and why.
4. Every sticking point becomes an edit to the README.

</details>

## Common mistakes

- Writing a description of the design that goes out of date the day after release.
- Leaving out assumptions, so the next engineer cannot tell whether a result still applies.
- Copying the same data into several documents, so that one copy gets updated and the others do not.
- Using vague requirements such as "robust," "easy to use," or "fast" without a number or test.
- Skipping the change log because the change "was small."

## Go deeper

- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) by NASA, a free handbook on requirements, documentation, and technical management. Section 6.0 covers crosscutting technical management.
- [Purdue OWL: Professional and Technical Writing](https://owl.purdue.edu/owl/subject_specific_writing/professional_technical_writing/index.html) by Purdue University, covering workplace document types, including memos and technical reports.
- [NIST e-Handbook of Statistical Methods](https://www.itl.nist.gov/div898/handbook/eda/section3/eda3.htm) by NIST, a free government handbook that is useful when you record statistical results and need to describe them correctly.
- [Communication reference](reference.md): the lookup sheet for this topic.
