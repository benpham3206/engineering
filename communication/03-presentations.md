# Presentations

Engineers present to reviewers, customers, managers, and sometimes to the public. A good talk gets a decision or an understanding in a few minutes, and a bad one buries the point under charts. This lesson covers how to plan a technical presentation, build slides that support the talk, and run a design review.

**Prerequisites:** [01-technical-writing.md](01-technical-writing.md): the same reader-first habits apply to slides.
**Time:** 4-6 h

## Core ideas

- **Decide the goal before the slides.** Finish this sentence: "After this talk, the audience should ___." If you cannot finish it, you are not ready to build slides.
- **Slides support the talk.** The speaker explains. The slide shows the one thing the audience needs to see. Do not put a paragraph on a slide and then read it aloud.
- **One message per slide.** Give the slide a headline that states the message as a full sentence, such as "The redesigned bracket meets the 2 kN load requirement." A title like "Results" does not tell the audience anything.
- **Show the evidence.** A claim without data is an opinion. Put the key number on the slide with its unit and condition.
- **Plan for questions.** Reviewers ask about assumptions, failure modes, and cost. Keep backup slides for the details you think they will ask about.

### Structure of a technical talk

A common structure, which works for most engineering reviews:

1. **Purpose.** Why you are here and what you need from the audience.
2. **Problem.** The need, the requirements, and the constraints.
3. **Approach.** The options considered and why you chose this path.
4. **Results.** The evidence that the approach works, with uncertainty.
5. **Risks and open items.** What could still go wrong and what you need to learn.
6. **Ask.** The decision, approval, or feedback you want.

Keep the whole talk to the time you are given, with room for questions. A rule of thumb is one main slide per minute for a standard review, but use the time you were actually assigned.

### Building slides

- Use a plain template with a large, readable font. Text should be readable from the back of the room.
- Keep text to a few short lines per slide. Put long detail in notes or a handout.
- Label every chart axis with the quantity and unit. Use the same units across slides.
- Use one color to highlight the key point and gray for the rest.
- Put the source of each number at the bottom of the slide if it is not your own result.
- Use drawings and photos of real hardware when you can. Annotate them with arrows and short labels.

### Delivering the talk

- Practice out loud with a timer. A talk you have not said aloud will run long.
- Look at the audience, not the screen. Use the slides as a reference for yourself.
- When you do not know an answer, say so, and say how you will find out. Write it down and follow up.
- Repeat or restate each question before you answer it, so everyone hears it.

## Checklist

Use this for a design review or project update.

- [ ] The goal sentence is written and tested against the talk.
- [ ] The first slide states the purpose and the ask.
- [ ] Each content slide has a full-sentence headline that states its message.
- [ ] Every number has a unit, a condition, and a source.
- [ ] Every chart labels its axes and uses the same units as the rest of the deck.
- [ ] Risks and open questions are shown, not hidden.
- [ ] The final slide states the decision or next step.
- [ ] Backup slides exist for likely questions.
- [ ] The talk has been timed out loud.

## Example

**Task.** You are presenting a design review for a redesigned motor mount. The mount must hold a 2 kN load with a deflection below a set limit. Write a six-slide outline with the headline and content of each slide.

**Outline.**

1. **Title.** "Motor mount revision B design review." Presenter, date, and the decision requested: approval to build a prototype.
2. **Problem.** "The motor mount must carry 2 kN with less than the specified deflection." Show the requirements in a short table.
3. **Approach.** "Redesign with a thicker web was the best trade-off between weight and stiffness." Show two or three options, each with its main pro and con.
4. **Analysis.** "The revised mount meets the load requirement with margin." Show a bar chart of predicted deflection for the three designs against the limit. Label the axis "Deflection (mm)" and show the limit as a line.
5. **Risks.** "Fatigue at the bolt holes is the open question." State the plan to test it.
6. **Decision.** "We request approval to build and test two prototypes by a named date."

**Sanity check.** Read only the headlines in order. Do they tell the story, with a decision at the end? If not, rewrite the headlines before touching the rest of the slides.

## Practice

1. Write a one-sentence takeaway for a project you have done. It should be a claim, not a topic.
2. Turn a five-paragraph lab report of yours into a 5-slide outline: problem, approach, key result, what it means, next step.
3. Remake one cluttered slide (from your own work or a free online deck) so it has one message, a headline sentence, and one figure.
4. Record yourself giving a 3-minute version of the talk. Note every filler word and every slide you had to read from.

<details><summary>What a good answer includes</summary>

1. Good: "The aluminum bracket meets the load with a factor of safety of 2.4 at 40 percent less mass." Weak: "Bracket analysis."
2. Each slide has a headline that states its point, and the result slide shows a number with units.
3. The new slide has under about 20 words of body text and the figure has labeled axes with units.
4. Under 3:15, no slide read word for word, and the takeaway said at the start and the end.

</details>

## Common mistakes

- Starting with background and history. The audience needs the point first.
- Using a headline that is only a topic, such as "Results" or "Overview."
- Putting raw data in the main deck instead of a summary chart, with the detail in backup.
- Animations and transitions that slow the talk without adding information.
- Presenting a chart with no units, no axis labels, or a truncated scale that exaggerates a small difference.
- Running out of time before reaching the decision slide.

## Go deeper

- [Purdue OWL: Professional and Technical Writing](https://owl.purdue.edu/owl/subject_specific_writing/professional_technical_writing/index.html) by Purdue University: includes workplace writing genres, including white papers and presentation-related guidance.
- [OpenStax Writing Guide with Handbook](https://openstax.org/books/writing-guide/pages/1-introduction) by OpenStax (Rice University): free general writing guide covering the writing process and revision, which applies to slides and speaking notes.
