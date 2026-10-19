# Argument and persuasion: how engineers make a case

**Type:** lesson
**Verify:** strict

An engineering argument is a claim, the evidence that supports it, and the reasoning that links the two, written for a reader who must decide something. Engineers need it because almost every real decision (which design, which supplier, whether to fix now or later) is made by people who were not in the lab, and they can act only on what the writing shows them.

**Prerequisites:** [Technical writing: reports, memos, lab reports](01-technical-writing.md)
**Time:** 3-5 h

## Core ideas

### The three parts of a case

A **claim** is a statement the reader could reasonably doubt, such as "the bolted joint should replace the bonded joint." A fact everyone accepts is not a claim, and neither is a preference with no stated basis.

**Evidence** is the observation, measurement, calculation, or documented source that the claim rests on. A test result, a datasheet value, a field failure record, and a hand calculation are all evidence. Evidence is only as good as its stated conditions, so give the setup, the sample, and what was not tested.

A **warrant** (also called the reasoning) is the principle that explains why this evidence supports this claim. Most weak engineering arguments have good evidence and an unstated warrant. "The bonded sample cracked under vibration" supports "replace the bonded joint" only through the warrant "the service vibration is at least as severe as the test vibration." If that warrant is false, the argument fails, and the reader can only attack it if you wrote it down.

A short test for any paragraph. Underline the claim, then the evidence, then ask what must be true for the evidence to count. Write that down as the warrant. If you cannot, the argument has a gap.

### Audience and purpose

The **audience** is the set of people who will read the document and act on it. The **purpose** is the specific change you want, such as an approval, a budget line, a design change, or a stop. Both decide what counts as strong evidence.

- A program manager decides on cost, schedule, and risk, so evidence must be translated into those terms.
- A peer reviewer decides on correctness, so evidence must include method, assumptions, and limits.
- A customer decides on fitness for their use, so evidence must tie to their requirements.

Write down one sentence before drafting: "After reading this, [person] should [action] because [reason]." If you cannot fill all three slots, the document is not ready to write.

### Three kinds of appeal

Rhetoric names three ways a writer moves a reader (the three appeals are described in [Purdue OWL: Rhetorical Strategies](https://owl.purdue.edu/owl/general_writing/academic_writing/establishing_arguments/rhetorical_strategies.html)). Engineers rely on three working versions.

- An **appeal to evidence** shows the data, the method, and the calculation, so the reader can check the claim. It carries most of the weight in engineering and must come first.
- An **appeal to credibility** shows the reader why the source can be trusted. In writing this means a stated method, named standards, disclosed limits, and a record of being right or of correcting errors. Admitting what you did not test raises credibility rather than lowering it.
- An **appeal to consequence** states what happens if the reader acts or does not act, in terms they care about, such as a failure mode, a cost, a delay, or a hazard. It is legitimate when the consequence is real and sized honestly. It becomes manipulation when a rare outcome is made to look likely.

Use all three, in that weight. A memo with only consequence reads as alarm. A memo with only credibility reads as "trust me."

### Rhetorical analysis of a technical document

A **rhetorical analysis** is a structured reading that asks how a document tries to move its reader, and whether it earns the move. Run it on other people's documents to learn from them, and on your own draft to find weak spots. Work through these questions in order.

1. Who is the stated audience, and who will really read it?
2. What exactly is the claim, and where does the document state it?
3. What evidence is offered, under what conditions, and what is missing?
4. What is the warrant that connects them, and is it written or hidden?
5. Which appeals carry the argument, and is the balance honest?
6. What would a skeptical reader object to, and does the document answer it?
7. Does the conclusion go further than the evidence?

The seventh question catches the most errors. A recommendation can be right while the document overstates it, and the overstatement is what a reviewer will remember.

### Anticipating objections

An **objection** is the strongest reason a reader could have to reject the claim. Collect them before you write by asking a colleague to argue against you, and by listing the questions the reviewer asked on the last similar decision.

Then handle each one in one of three honest ways.

- Answer it with evidence you already have.
- Concede it and say how the recommendation still holds, or how the risk is managed.
- State that it is open, say how it will be closed, and say by when.

Put the strongest objection near the recommendation, not buried in an appendix. A reader who finds the objection themselves, and sees you did not mention it, discounts everything else you wrote.

### Common fallacies in engineering arguments

A **fallacy** is a pattern of reasoning that looks like support but does not establish the claim. The general catalogue is in [Purdue OWL: Logical Fallacies](https://owl.purdue.edu/owl/general_writing/academic_writing/logic_in_argumentative_writing/fallacies.html). These four appear most often in engineering.

| Fallacy | What it looks like | Why it fails | Honest repair |
|---|---|---|---|
| Appeal to precedent | "We have always used this alloy" or "the last program did it this way" | A past choice shows what was done, not that it was right, and conditions may have changed | State what made it right then and check those conditions still hold |
| Sunk cost | "We have already spent so much on this design that we must finish it" | Money already spent cannot be recovered by either choice, so it cannot favour either | Compare only future cost and benefit of each option |
| False precision | A result quoted to six digits from a model whose inputs are known to two | The digits imply a certainty the inputs cannot support | Round to what the least certain input supports and state the uncertainty |
| Cherry-picked data | Showing the three good runs and omitting the failures, or choosing a plot range that hides scatter | The reader sees a sample chosen to fit the claim | Report all runs, say how any were excluded and why, and show the scatter |

Two more are worth watching. An **appeal to authority** offers "the vendor says so" in place of data, and a **false dichotomy** offers two options when a third exists. Both are fixed the same way, by adding the missing evidence or the missing option.

### Writing a recommendation memo that persuades without overstating

A **recommendation memo** is a short document that asks a named reader to choose one option among several, and supports the choice. Its structure follows from the ideas above.

1. A subject line that states the decision requested.
2. A first paragraph with the recommendation, the one or two reasons that decided it, and the action and date requested.
3. The options considered, including the do-nothing option, with the main advantage and disadvantage of each.
4. The evidence for the recommended option, with conditions, sample, and what the data cannot show.
5. The strongest objections and how each is answered, conceded, or left open.
6. Risks that remain, with an owner and a way to detect them.
7. The action requested, by whom, by when.

To persuade without overstating, match the strength of each verb to the strength of the evidence.

- "The tests show" is for measured results under stated conditions.
- "The analysis predicts" is for a model, with its assumptions named.
- "We expect" or "we believe" is for judgment, with its basis named.
- "We do not know" is for gaps. Say it plainly.

Avoid words that carry no measurement, such as "clearly," "obviously," and "significant" (unless a statistical test is named). Name a mechanism or a number, never a feeling.

## Checklist

Run this on any argument before you send it.

- [ ] The claim is stated in the first paragraph, in one sentence the reader could disagree with.
- [ ] Each piece of evidence states its conditions, its sample, and its source.
- [ ] Each warrant is written down, not left for the reader to guess.
- [ ] The document names the reader, the action requested, and the date.
- [ ] Evidence leads, credibility is shown by method and disclosed limits, and consequence is sized honestly.
- [ ] The strongest objection is stated and answered, conceded, or marked open.
- [ ] No precedent, sunk cost, false precision, or cherry-picked data is carrying the weight.
- [ ] Every verb is as strong as its evidence, and gaps are labelled as gaps.
- [ ] The conclusion does not go beyond what the evidence supports.

## Example

The scenario. A team is deciding how to attach a sensor bracket to a vibrating machine frame. Two options are on the table, a bonded (adhesive) joint and a bolted joint. A test engineer drafts a memo to the project lead.

### Draft memo, as first written

> Subject: Joint selection
>
> We have always bonded brackets on this machine and it has worked well. The bonded joint is obviously better because it is lighter and cheaper, and we have already spent a large part of the budget on the bonding fixtures. One bonded sample was vibration tested and it passed. The bolted joint is a worse idea because bolts can loosen. We should continue with bonding. Please approve.

### Analysis

Run the seven rhetorical questions on the draft.

1. Audience. The project lead decides on cost, schedule, and risk, but the draft never names the decision or the date.
2. Claim. "We should continue with bonding" is the claim, but it appears last and the subject line does not state it.
3. Evidence. The only test is "one bonded sample ... passed." There are no conditions (vibration level, duration, temperature), no sample of more than one, and no result for the bolted option at all.
4. Warrant. Unwritten. Passing one test supports the claim only if the test matched service conditions and one sample represents the batch. The draft states neither.
5. Appeals. Credibility rests on "we have always done it," and the closing push is consequence with no size ("bolts can loosen").
6. Objections. None answered. The obvious ones are that bonds can degrade with heat and moisture, that a bond cannot be inspected or taken apart, and that one sample says little about scatter.
7. Overreach. "Obviously better" and "worse idea" claim far more than one passing sample supports.

The fallacies are visible by name. "We have always bonded" is appeal to precedent. The spent budget on fixtures is sunk cost, because the fixtures' cost is the same whichever joint is chosen. One passing sample out of an untested option is a cherry-picked comparison, since only one side was tested. "Obviously" does the work that evidence should do.

### Improved memo

> Subject: Decision requested: joint type for the sensor bracket, by Friday
>
> Recommendation. Approve a short comparison test of both joints before committing to either. Based on current evidence we lean toward bonding for weight and cost, but the evidence is too thin to commit. The test needs about a week of bench time.
>
> Options. (A) bonded joint, lighter and cheaper, cannot be inspected or disassembled. (B) bolted joint, heavier and costlier, can be inspected and retorqued. (C) do nothing, which leaves the bracket undefined and blocks the frame release.
>
> Evidence so far. One bonded sample survived the bench vibration profile in Table 1 at room temperature. The bolted joint has not been tested. The test does not cover heat, moisture, or more than one sample, so it shows the bonded joint can survive these conditions, not that it will in service.
>
> Warrant. This test supports the bonding option only if the bench profile is at least as severe as service vibration. The service profile has been estimated from the frame drawings, not measured on the machine.
>
> Objections. Bonds can weaken with heat and moisture, which we have not tested and will add to the plan. Bolts can loosen under vibration, which the bolted test will measure with a torque check before and after. We are not counting the money already spent on bonding fixtures, since it is the same for both options.
>
> Action. Approve the comparison test by Friday. We will report all runs, including any failures, in the following week.

Why this version works. The subject line and first paragraph state the decision and date. The claim is scaled to the evidence ("lean toward," "too thin to commit"). The warrant is written, so the lead can challenge it. Both options get a test, and the do-nothing option is shown. The sunk cost is named and set aside. The verbs match the evidence ("survived," "has not been tested," "we have not tested"). The strongest objections appear in the body, not an appendix, each with a handling. The consequence appeal is present (blocks the frame release) and is sized to a schedule fact.

Note what the improved memo gives up. It no longer asks for approval of bonding, so it is weaker as a plea and stronger as a case. In engineering the second is what persuades a reader who knows the stakes.

## Practice

1. For the claim "we should buy the cheaper pump because it passed the supplier's test," name the evidence and write the warrant that must hold for the evidence to count.
2. A teammate argues, "We should keep the old controller design because we invested heavily in its code." Name the fallacy and write the comparison that should replace it.
3. A report states a computed natural frequency to six significant digits, but the stiffness input is known to about two. Name the fallacy and write what the report should say instead.
4. A recommendation memo you must review opens with three paragraphs of background, then asks for a decision on the last line. List the changes you would ask the author to make, in order of importance.
5. A test series of eight runs includes two that failed. Choose between reporting only the six successes with a note, or reporting all eight. Say which is honest, and what the report must also state.

<details><summary>Answers</summary>

1. The evidence is the supplier's test result. The warrant is that the supplier's test conditions (fluid, flow range, duty cycle, temperature) match the intended service and that the supplier is not the only source. Without a named independent check or matching conditions, the evidence supports only "the pump worked in the supplier's test."
2. Sunk cost. The spent effort is the same whether the design is kept or replaced, so it cannot favour either. The comparison to make is the future cost, schedule, and risk of keeping the old design against replacing it, including the effort to maintain the code.
3. False precision. The result cannot be more certain than its least certain input. The report should round to about two significant figures, state the uncertainty from the stiffness input, and say how the frequency changes across that range.
4. First, move the recommendation and the requested action to the first paragraph and put the decision in the subject line. Second, cut the background to what the reader needs to understand the recommendation. Third, add the options considered and the strongest objection, with the handling for each. Fourth, check that the verbs match the evidence strength and that gaps are labelled.
5. Reporting all eight is the honest choice. The report must also state why any run could be excluded, which here would need a documented cause such as a fixture fault, and should show the two failures and their conditions, because they are evidence about reliability and not noise.

</details>

## Common mistakes

- Burying the claim at the end, so the reader has to guess what the evidence is for. State it first.
- Leaving the warrant unwritten. If the reader must supply it, they will supply their own, and it may differ from yours.
- Treating consequence as proof. A large possible loss makes the decision matter more, but it does not make the loss likely.
- Hiding the strongest objection, which the reader then finds and holds against you.
- Matching confidence to the audience's hopes rather than to the evidence, and then correcting later with a worse loss of trust.

## Go deeper

- [Purdue OWL: Rhetorical Strategies](https://owl.purdue.edu/owl/general_writing/academic_writing/establishing_arguments/rhetorical_strategies.html) by Purdue University, covering the three appeals and how to use each responsibly.
- [Purdue OWL: Logical Fallacies](https://owl.purdue.edu/owl/general_writing/academic_writing/logic_in_argumentative_writing/fallacies.html) by Purdue University, a catalogue of common reasoning errors with examples.
- [OpenStax Writing Guide with Handbook, chapter 9](https://openstax.org/books/writing-guide/pages/9-introduction) by OpenStax (Rice University), on rhetoric and analyzing how writers persuade.
- [Technical writing](01-technical-writing.md) and [Communication reference](reference.md), for memo structure and templates.
- [Presentations](03-presentations.md), for making a case aloud to a review board.
