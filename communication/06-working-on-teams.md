# Working on teams

Almost no engineering product is built by one person. Projects succeed or fail on how people divide the work, share information, make decisions, and handle disagreement. This lesson covers the roles teams need, how to run a meeting that produces decisions, how to give and receive feedback, and how to keep work visible to everyone.

**Prerequisites:** [04-documentation.md](04-documentation.md): teams depend on shared records.
**Time:** 3-5 h

## Core ideas

- **Every task has one owner.** A task with two owners has none. Name one person responsible for each deliverable, even if several people help.
- **Write the decision down.** A decision that lives only in a conversation will be remade or forgotten. Record what was decided, by whom, and why.
- **Define the interfaces.** When two people's work must fit together, agree on the shared dimensions, signals, or data format in writing before either one builds.
- **Surface problems early.** A late surprise costs more than an early warning. Say "I am behind" as soon as you know it.
- **Disagree about the idea, not the person.** Engineering decisions improve when people argue about evidence. Ask what would change your mind.

### Roles that often appear

- **Project lead.** Keeps the schedule, runs the meetings, and makes sure decisions get made.
- **Technical lead.** Owns the design direction and the final technical calls.
- **Subsystem owner.** Responsible for one part of the design and its documentation.
- **Test or quality lead.** Plans verification and checks that the requirements are met.
- **Records keeper.** Maintains the decision log, action list, and document versions. On small teams, this is often shared.

On a student team, these roles may rotate. Name who holds each one, and write it down.

### Running a useful meeting

- Send the agenda and any pre-read at least a day before. State the decision the meeting must reach.
- Limit the meeting to the decisions and blockers. Move detailed discussions into a side session with the people who need them.
- Assign an action item with an owner and a date for each open point.
- Send the notes within a day. Include the decisions, the action items, and the open questions.

### Giving and receiving feedback

- Be specific. "The sketch is missing the hole positions" is more useful than "the drawing is bad."
- Separate what you observed from your interpretation. "The test did not record temperature" is an observation. "The team was careless" is a judgment.
- When you receive feedback, ask a clarifying question before you respond to it. Make sure you understand the concern.
- Thank people for raising problems, even when it is uncomfortable.

### Keeping work visible

- Use one shared task list that shows the owner, status, and due date of each item.
- Post status updates on a fixed schedule, such as every week, with three items: done, in progress, and blocked.
- Keep the design, test, and documentation in one repository or folder, so everyone works from the same version.

## Checklist

Use this to check a team's working process.

- [ ] Every deliverable has one named owner.
- [ ] Roles are written down, even if they rotate.
- [ ] Each decision is recorded with the date and the reasons.
- [ ] Interfaces between subsystems are documented and agreed.
- [ ] The task list is current and shared.
- [ ] Meetings have an agenda, a decision goal, and notes sent afterward.
- [ ] Blockers are raised within a day of being found.
- [ ] Each team member knows how to find the current version of every document.

## Example

**Task.** Your three-person team is designing a small drone landing gear. Alex owns the frame, Sam owns the test plan, and you own the drawings. A test shows the gear flexes more than expected. Write the message you send to the team, and the decision you propose.

**Draft message.**

"Test TP-02 on Tuesday showed the landing gear tip deflects 9 mm under the design load, more than the 5 mm limit in REQ-04. The test used the rev B frame. Alex, can you check whether the frame wall thickness in the CAD matches the rev B drawing? Sam, please confirm the load fixture was set to the stated load and attach the raw data. I will check the drawing notes. Proposal: hold the drawing release until we agree whether to thicken the frame or change the leg geometry. We will decide at Thursday's review. Owners and due dates are in the task list."

**Why this works.**

- It states the observation with numbers and the requirement it breaks.
- It names one task and one owner for each check.
- It proposes a decision and a date.
- It points to where the evidence lives.

**Sanity check.** Could anyone on the team act on this message without asking a follow-up question? If not, add the missing owner, date, or file location.

## Practice

1. Write a one-page team charter for a four-person project: goal, roles, meeting time, how decisions are made, and how conflicts are handled.
2. Write the agenda and the action-item list for a 30-minute design review.
3. Describe a time a team you were on missed a deadline. What was the root cause, and what process change would have caught it?
4. Practice giving feedback on a teammate's design using: what works, one specific concern, and a suggested next step.

<details><summary>What a good answer includes</summary>

1. Each role has one named owner, and the charter says what happens when someone misses a commitment.
2. Each action item has an owner and a due date.
3. A good answer names a process cause (no owner, unclear scope, late integration) rather than blaming a person.
4. The concern is about the design, not the person, and comes with evidence or a number.

</details>

## Common mistakes

- Assuming someone else is handling a task that nobody owns.
- Making decisions in a hallway conversation and never writing them down.
- Letting a disagreement continue for weeks without a decision date.
- Hiding a delay until the due date has already passed.
- Making a change to a shared design without telling the owner of the affected subsystem.

## Go deeper

- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) by NASA: free handbook from NASA whose sections include crosscutting technical management.
- [Purdue OWL: Professional and Technical Writing](https://owl.purdue.edu/owl/subject_specific_writing/professional_technical_writing/index.html) by Purdue University: workplace writing genres, including memos, which teams use to communicate decisions.
