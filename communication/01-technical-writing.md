# Technical writing: reports, memos, and lab reports

Most engineering work reaches people as writing. A test result that nobody can read has the same value as no test at all. Technical writing is the craft of putting facts in an order a busy reader can use, with enough detail to check them.

**Prerequisites:** none
**Time:** 4-6 h

## Core ideas

- **Know the reader first.** Ask who will read the document, what they already know, and what decision they need to make. A manager wants the answer on page one. A reviewer wants the method so they can check it.
- **Lead with the point.** Engineers call this "bottom line up front" (BLUF). State the result or recommendation in the first paragraph, then give the support.
- **One idea per paragraph.** A paragraph has a topic sentence and then evidence. If you cannot name the topic sentence, split or cut the paragraph.
- **Plain words.** Use "about 2 mm thick" rather than "approximately dimensionally significant." Define any acronym the first time you use it.
- **Separate facts from opinions.** Write "the bracket deflected 1.2 mm under the 50 N load" as a fact. Write "the bracket seems stiff enough" as an opinion, and say what it is based on.
- **Make every claim checkable.** Give the number, the unit, the condition it applies to, and where the data came from.

### Three document types you will write

- **Technical report.** A long, self-contained account of work done, such as a project or a study. It has a title page, abstract, table of contents, body, conclusions, and references. The reader may skip to any section, so each section must stand on its own.
- **Engineering memo.** A short document, usually one to three pages, that asks for a decision or gives a status update. It has a header block (To, From, Date, Subject) and goes straight to the point.
- **Lab report.** A record of an experiment that another engineer could repeat. It follows the scientific order: question, method, data, analysis, and conclusion.

### Writing process

- Make an outline before you write any sentences. Each heading should be a claim or a question, not just a label.
- Write a rough draft fast, without stopping to polish.
- Revise for content first (is the argument complete and in order?), then for clarity (are the sentences short and direct?), then for mechanics (spelling, units, numbering).
- Read the draft out loud or have someone else read it. Mark every sentence the reader would need to ask about.

## Checklist

Use this before you send any technical document.

- [ ] The first paragraph states the purpose and the main result or request.
- [ ] Every number has a unit and, where it matters, an uncertainty or a condition.
- [ ] Every figure and table is referred to in the text by number.
- [ ] Every acronym is defined on first use.
- [ ] Headings are in order and make sense when read alone.
- [ ] The conclusion follows from the evidence shown, with no new data introduced.
- [ ] Sources are listed in one consistent citation style.
- [ ] The file has been spell-checked and the numbering of figures and tables is correct.

## Example

Below are outlines you can copy. Replace the bracketed text with your own content.

### Lab report outline

1. **Title.** Name the quantity measured and the setup, for example "Measured stiffness of a 6061 aluminum cantilever beam."
2. **Abstract (about 100 words).** Purpose, method, the main number, and the one-sentence conclusion.
3. **Introduction.** What is being measured and why. State the expected result and the theory behind it, with a reference.
4. **Apparatus and method.** Equipment with model numbers and calibration dates. Procedure steps written so another student can repeat them. Include the sampling rate, the load steps, and the number of repeat trials.
5. **Data.** Tables and figures only. Raw data goes in an appendix if it is long. No analysis here.
6. **Analysis.** Calculations with the equations written out. Uncertainty estimate and how you got it. Comparison with the expected value.
7. **Discussion.** Explain differences between measured and expected results. Name the likely error sources and say which one you think dominates.
8. **Conclusion.** Answer the question from the introduction in two or three sentences.
9. **References.** Every textbook, standard, and data sheet used.

### Engineering memo outline

- **Header.** To, From, Date, Subject. The subject line should say what the reader must do or know, for example "Subject: Recommend supplier B for the motor mounts."
- **Purpose (one or two sentences).** Why this memo exists.
- **Recommendation or summary.** The decision or result in three or four sentences.
- **Background.** Only what the reader needs to understand the recommendation.
- **Options considered.** Two or three options, each with its main advantage and disadvantage. A short table works well here.
- **Details.** Supporting data, calculations, or schedule. Keep this short and link to a longer report if needed.
- **Action requested.** Who does what, by when.
- **Attachments.** List them by name.

### Design review slide outline

This is a slide-by-slide outline for a design review. The full guidance for slides is in [03-presentations.md](03-presentations.md).

1. Title slide: project, design revision, presenter, date.
2. Problem statement: the need, in one sentence, and the main requirements.
3. Proposed design: one annotated image or drawing.
4. Key trade-off: the two or three options and why this one was picked.
5. Analysis results: the main numbers against the requirements, with uncertainty.
6. Risks and open questions: what could fail and what you still need to learn.
7. Decision needed: what the review board should approve or change.

## Practice

1. Rewrite this sentence so it is specific and checkable: "The new fixture is much better than the old one and holds parts well." Write what a good answer includes.
2. Take a paragraph of your own writing and find its topic sentence. If there is none, write one. Write what a good answer includes.
3. Write a three-sentence memo recommending one of two cable suppliers. Write what a good answer includes.
4. Outline a lab report for measuring the time it takes a ball to roll down a ramp. Write what a good answer includes.
5. Find a sentence in an old document that uses a vague word such as "soon," "large," or "fast." Replace it with a number and a unit. Write what a good answer includes.

<details><summary>Answers</summary>

1. A good answer replaces "much better" and "holds parts well" with measured values, such as the change in positioning error in millimetres and the clamping force in newtons, with the test condition stated.
2. A good answer has one sentence that names the single main point of the paragraph, and the rest of the paragraph supports it with evidence.
3. A good answer opens with the recommendation, gives the one or two criteria that decided it (cost, lead time, or test data), states the main risk, and asks for a yes or no by a named date.
4. A good answer includes a purpose statement, a list of equipment (ruler, timer, ball), a repeatable procedure with the number of trials, a data table, an uncertainty estimate for the timing, and a comparison with a simple energy or kinematics prediction.
5. A good answer swaps the vague word for a number with a unit and a condition, for example a time in seconds at a stated temperature.

</details>

## Common mistakes

- Writing the report in the order you did the work, instead of the order the reader needs. Put the result first and the history later.
- Leaving out units or test conditions. A number without a unit is not a result.
- Mixing data and interpretation in the same figure or table.
- Using a long title that repeats the section heading. Write a short title and a clear first sentence.
- Sending a draft without checking that every figure and table is cited in the text.

## Go deeper

- [Purdue OWL: Professional and Technical Writing](https://owl.purdue.edu/owl/subject_specific_writing/professional_technical_writing/index.html) by Purdue University: memos, technical reports, and other workplace genres.
- [Purdue OWL: Writing Report Abstracts](https://owl.purdue.edu/owl/subject_specific_writing/professional_technical_writing/technical_reports_and_report_abstracts/index.html) by Purdue University: how to write informational and descriptive abstracts.
- [OpenStax Writing Guide with Handbook](https://openstax.org/books/writing-guide/pages/1-introduction) by OpenStax (Rice University): free general writing textbook covering the writing process and revision.
- [Purdue OWL](https://owl.purdue.edu/owl/purdue_owl.html) by Purdue University: the full writing resource index, including general writing and grammar.
