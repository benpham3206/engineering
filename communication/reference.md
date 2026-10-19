# Communication reference

**Type:** reference

Engineering communication is the writing, drawing, presenting, and documenting that let others act on engineering work. Engineers need it because work that its readers cannot understand is not finished.

A lookup sheet of templates, conventions, and checks for writing, drawing, presenting, and documenting engineering work, for an engineer who needs a layout, a rule, or a checklist in the middle of a task.

## Principles

- A document works only if the reader can act on it without asking you a question.
- Lead with the result or the decision needed. Put the support after it.
- Every number has a value, a unit, and the condition it applies to. A number without a unit is not a result.
- Separate what you measured, what you calculated, and what you believe. Label each.
- Use one name for each part, signal, and quantity in every document that mentions it.
- Words that define a requirement have fixed meanings: "shall" is mandatory, "should" is a recommendation, "may" is permitted.
- Drawings, graphs, and units follow shared standards so that every reader sees the same thing.
- Record the decision, its reason, and the outcome. Future readers need the why.
- Write for a reader who was not in the room, and who will read the document years later.

## 1. Writing templates

### 1.1 Lab report

| Section | Contents | Length (typical) |
|---|---|---|
| Title | Quantity measured and setup | 1 line |
| Abstract | Purpose, method, main number, one-sentence conclusion | about 100 words |
| Introduction | Question, expected result, theory with reference | 1 page |
| Apparatus and method | Equipment with model and calibration date; repeatable steps; sample rate, load steps, trial count | 1 to 2 pages |
| Data | Tables and figures only; raw data in appendix | varies |
| Analysis | Equations written out; uncertainty and how it was found; comparison with expected value | varies |
| Discussion | Differences between measured and expected; likely error sources; which dominates | varies |
| Conclusion | Answer the introduction question in 2 or 3 sentences | short |
| References | Every text, standard, and data sheet used | list |

Copy-ready skeleton:

```
Title: Measured <quantity> of <specimen or setup> under <condition>

Abstract
<Purpose in one sentence. Method in one sentence. Main result with unit and
uncertainty. Conclusion in one sentence.>

1. Introduction
<Question being answered. Expected result [value, unit] and its source [ref 1].>

2. Apparatus and method
- Equipment: <item, model, serial, calibration date>
- Procedure: <numbered steps a classmate could repeat>
- Settings: sample rate <value unit>; load steps <values unit>; trials <n>

3. Data
Table 1. <Quantity> at each <variable>. <Caption: conditions, source.>
Figure 1. <Caption: what is shown, conditions, n, what the bars mean.>

4. Analysis
<Equation. Inputs with units. Result with unit and uncertainty.
Comparison: measured <v> vs expected <v>, difference <d %>.>

5. Discussion
<Largest error source and why. Other error sources. What would reduce them.>

6. Conclusion
<Two or three sentences that answer the question in Section 1.>

References
[1] <Author, Title, Publisher or Standard number, Year>
```

### 1.2 Technical report

| Part | Purpose |
|---|---|
| Title page | Title, author, date, revision, distribution |
| Abstract | Whole report in one paragraph: purpose, method, result, conclusion |
| Table of contents, list of figures, list of tables | Navigation for long reports |
| Nomenclature | Symbols and abbreviations with units |
| Introduction | Background, problem statement, scope, requirements |
| Method | How the work was done, with assumptions |
| Results | Findings, with figures and tables; no interpretation |
| Discussion | Meaning of results, limits, comparison with requirements |
| Conclusions and recommendations | Numbered; each traceable to a result |
| References | One citation style throughout |
| Appendices | Raw data, long derivations, drawings |

Rules:

- Each section must make sense if the reader starts there.
- Put every term in the nomenclature list on first use.
- Put the answer to "so what" in the abstract and in the conclusions.

### 1.3 Engineering memo

```
To:       <name, role>
From:     <name, role>
Date:     <YYYY-MM-DD>
Subject:  <Verb-led statement of what the reader must do or know>
Action:   <Decision or approval requested, and by when>

Purpose
<One or two sentences: why this memo exists.>

Recommendation
<Decision or result in three or four sentences. Numbers with units.>

Background
<Only what the reader needs to follow the recommendation.>

Options considered
| Option | Main advantage | Main disadvantage | Cost / schedule |
|---|---|---|---|
| A | | | |
| B | | | |

Details
<Short. Link to a longer report rather than copying it.>

Action requested
- <Owner>: <task>, due <YYYY-MM-DD>

Attachments
- <file name, revision>
```

Memo rules: one page if possible, three at most. Put the action in the subject line.

### 1.4 Design review agenda

```
Design review: <product / subsystem>, revision <X>
Date: <YYYY-MM-DD>    Time: <start-end>    Location: <room or link>
Chair: <name>         Note taker: <name>
Pre-read: <document, revision, sent on date>

Decision needed: <approve, approve with changes, or reject, for what>

| Time  | Item                                  | Presenter | Output needed          |
|-------|---------------------------------------|-----------|------------------------|
| 0:00  | Purpose and decision needed           | Chair     | Agreement on the goal  |
| 0:05  | Problem and requirements (IDs)        | <name>    | Requirements accepted  |
| 0:15  | Proposed design and key trade-off     | <name>    | Choice confirmed       |
| 0:30  | Analysis results vs requirements      | <name>    | Pass, fail, or open    |
| 0:45  | Test results and open risks           | <name>    | Risk owners named      |
| 0:55  | Action items and decision             | Chair     | Decision recorded      |

Open questions to be answered by: <name, date>
Actions: <owner, task, due date> (one line each)
```

Rules: send the pre-read a day ahead. Each item names its output. Close with the decision, read aloud, and record it.

### 1.5 Email asking a senior engineer for help

```
Subject: <Specific topic> - question about <one thing>, need by <date>

Hi <name>,

I am working on <project or task, one sentence>.

What I have tried:
- <attempt 1, with result and number>
- <attempt 2, with result and number>

Where I am stuck:
<One specific question, stated so that a yes, no, or one-line answer helps.>

What I think is happening: <your best hypothesis, with the evidence for it>.

Files: <file name, revision, location or attached>.

Would 20 minutes this week work? I can also send a written summary if easier.

Thanks,
<name>
```

Rules: ask one question per email. Show what you already tried so the reader does not repeat it. Keep the email under about 150 words. Put the deadline in the subject line. Attach the data, not a description of it.

## 2. Incident report

Blameless format: describe systems and decisions, not people's failings.

```
Incident report: <short name>          ID: <INC-###>     Revision: <A>
Date and time of event: <YYYY-MM-DD hh:mm, time zone>
Reported by: <name>    Report date: <date>    Status: open / closed

1. What happened
<Plain statement of the event: what failed or went wrong, observed effect.
Use measured values with units. No cause yet.>

2. Impact
| Area | Effect | Quantity and unit | Duration |
|---|---|---|---|
| Safety | | | |
| Function | | | |
| Schedule | | | |
| Cost | | | |
| Customers or users | | | |

3. Timeline
| Time (time zone) | Event | Source (log, witness, data file) |
|---|---|---|
| hh:mm | First abnormal reading | <file> |
| hh:mm | Operator action | <log> |
| hh:mm | Containment applied | <record> |

4. Root cause
- Direct cause: <the physical or technical failure, with evidence>
- Root cause: <the condition or process that allowed it; test: "if this were
  removed, would the failure still happen?">
- Contributing factors: <list; each with evidence>
- Verification: <how the cause was confirmed, for example reproduced at
  <condition>; not only a guess>

5. Corrective actions
| ID | Action | Type (fix / prevent / detect) | Owner | Due | Verified by |
|---|---|---|---|---|---|
| CA-1 | | | | | |

6. Containment and immediate actions taken
<What was done to stop further harm, and when.>

7. Lessons and document updates
<Which drawings, procedures, test plans, or requirements change.
Cross-reference the change requests.>
```

Rules: the root cause must be backed by evidence. A corrective action without an owner and a verification method is not done. Close the report only when every corrective action is verified.

## 3. Change and test documents

### 3.1 Engineering change request (ECR)

```
ECR number: <ECR-####>        Date: <YYYY-MM-DD>     Requested by: <name>
Title: <what changes, in one line>
Priority: <safety / function / cost / cosmetic>

Affected items
| Part or assembly number | Current revision | Proposed revision | Document type |
|---|---|---|---|
| | | | drawing / BOM / spec / test |

Description of change
<What is different, with before and after values and units.>

Reason for change
<Problem or requirement it solves, with reference (incident, REQ-ID, test report).>

Impact assessment
| Area | Assessment |
|---|---|
| Form, fit, function | <same / changed: how> |
| Safety and compliance | <review needed? yes/no> |
| Cost | <change in unit cost, tooling, in currency and amount> |
| Schedule | <change in lead time, in days> |
| Inventory and existing parts | <use-up, scrap, rework> |
| Documents to update | <list> |
| Verification needed | <test plan ID and what it checks> |

Effectivity: <serial number, date, or lot from which the change applies>
Disposition: approved / approved with conditions / rejected
Approvals: <role, name, signature, date> for each required reviewer
```

Rules: list every affected drawing, BOM line, and test. Assign the new revision letter only at approval. An ECR without an effectivity point is incomplete.

### 3.2 Test plan

```
Test plan: <TP-###>      Revision: <A>      Product / item: <part or revision>
Objective: <what question the test answers, in one sentence>
Requirements verified: <REQ-IDs>

Scope
- In scope: <items, conditions>
- Out of scope: <items, and why>

Test article
- Identification: <serial numbers, revision, build date>
- Configuration: <as built, fixtures, software version>

Equipment
| Item | Model / ID | Range and accuracy | Calibration due |
|---|---|---|---|
| | | | |

Environment: <temperature in degC, humidity in %RH, pressure in kPa if relevant>

Procedure
1. <step, with the setting and the value with unit>
2. <step>
3. <record: what, where, how often>

Pass / fail criteria (stated before testing)
| Criterion | Limit | Unit | Measured quantity |
|---|---|---|---|
| | | | |

Sample size and repeats: <n, and why that n>
Data recorded: <channels, sample rate, file name convention>
Deviations and anomalies: recorded in <report section>, with reason

Test report reference: <TR-###>. Prepared by: <name>. Reviewed by: <name>.
```

Rules: write the pass criteria before the first test run. Record each deviation from the plan. A plan that cannot fail is not a test.

## 4. Requirements statement

### 4.1 Template

```
The <system or item> shall <verb> <measurable property> of <value> <unit>
under <condition>, as verified by <method>.
```

Example form: "The bracket shall carry a static load of 2.0 kN applied at the hole centers, with no yielding, as verified by test TP-02."

### 4.2 Word choice

| Word | Meaning in a requirement |
|---|---|
| shall | Mandatory. Verifiable. Use for every requirement. |
| should | Recommended, not mandatory. Use for guidance only. |
| may | Optional. Permitted but not required. |
| will | Statement of fact or future event, not a requirement. |

### 4.3 Good versus bad requirements

Good requirements are testable (a test can pass or fail them) and unambiguous (two readers agree on the meaning).

| Bad (fails) | Why it fails | Good (passes) |
|---|---|---|
| The enclosure should be strong. | "Strong" is not measurable; "should" is not mandatory. | The enclosure shall survive a 1.0 m drop onto concrete with no loss of function, as verified by TP-05. |
| The fan should be quiet. | No number, no condition. | The fan shall not exceed 40 dB(A) at 1 m, at 25 degC, at rated speed, as verified by TP-07. |
| The app will load fast. | "Fast" is vague; "will" is not a requirement. | The page shall display its first content within 2.0 s on a 10 Mbit/s link, as verified by TP-11. |
| The battery must last a long time. | "Long time" has no value. | The battery shall power the device for at least 8 h of continuous operation at 25 degC, as verified by TP-03. |
| The bolts should be tight enough. | No torque, no tolerance, no method. | The bolts shall be tightened to 12 N m $\pm 1$ N m, as verified by torque audit of 10 joints. |
| The part must be small and light. | Two undefined adjectives. | The part shall have a mass of no more than 0.5 kg and fit within a $100\ \mathrm{mm} \times 60\ \mathrm{mm} \times 40\ \mathrm{mm}$ envelope. |
| The system shall be user-friendly. | No measure, no user group. | 90 % of first-time users shall complete setup in under 5 min, as verified by usability test UT-01 with 10 users. |

Test each requirement with these questions:

- Can a test be written that passes for a good design and fails for a bad one?
- Does each unit and condition appear?
- Would two engineers draw the same pass or fail line?
- Does each requirement have a unique ID and a verification method?

## 5. Drawing conventions

### 5.1 Line types

| Line | Appearance | Use |
|---|---|---|
| Visible edge (object line) | Thick, continuous | Outline of the part as seen in this view |
| Hidden edge | Medium, short dashes | Edges behind the surface |
| Center line | Thin, long dash and short dash | Axis of a hole, shaft, or symmetric feature |
| Dimension line | Thin, continuous, arrowhead at each end | Shows the extent of a dimension |
| Extension line | Thin, continuous, starts a small gap from the object | Connects the dimension to the feature |
| Leader | Thin, with arrowhead at the feature end | Points a note or callout at a feature |
| Section (cutting plane) line | Thick, long dash with arrows at the ends | Shows where a section is cut and the direction of view |
| Section hatching | Thin, evenly spaced diagonal lines | Shows cut material in a section view |
| Phantom line | Thin, long dash and two short dashes | Alternate position, moving part, adjacent part |
| Break line | Thin, freehand or zigzag | Shows that part of a view is removed |

Rules: keep line weights consistent across the sheet, with thick for visible edges and thin for everything else. Do not use hidden lines for visible edges. Do not use center lines as object outlines.

### 5.2 Views and projection symbols

| Item | Rule |
|---|---|
| Third-angle projection | Standard in the United States (ASME Y14.3). Top view above the front view; right-side view to the right of the front view. |
| First-angle projection | Common in Europe and ISO drawings. Top view below the front view; right-side view to the left of the front view. |
| Projection symbol | A truncated cone drawn in the title block. Its position relative to the circle shows which angle is used. Always check it. |
| Number of views | The fewest that define every feature completely. |
| Isometric view | Aids understanding; does not replace the orthographic views. |

### 5.3 Title block fields

| Field | Content |
|---|---|
| Part name and number | Unique identifier, as in the BOM |
| Drawing number and revision | Revision letter changes with any change to the part |
| Material and finish | Specification, grade, and treatment |
| Units | Millimeters or inches, stated once |
| Default tolerance | For example, `±0.1 mm UNLESS NOTED` |
| Scale | For example 1:2, or "NTS" (not to scale) |
| Projection symbol | First-angle or third-angle |
| Drawn by, checked by, date | Names and dates for each |
| Sheet | "1 of 2", and so on |
| Notes | Finish, heat treatment, and specifications not shown by geometry |

### 5.4 Dimensioning rules

| Rule | Detail |
|---|---|
| Size and location | Each feature needs a size and a position. A hole needs diameter, position, and depth if not through. |
| Dimension once | A distance dimensioned twice can create conflicting values. |
| Datums | Location dimensions are measured from a labeled datum or reference edge. |
| No arithmetic for the reader | Give the size directly. Do not require the reader to add or subtract to get it. |
| Reference dimensions | Mark as reference (the lesson's convention is "(REF)"; ASME Y14.5 shows the value in parentheses). Reference dimensions do not control manufacturing. |
| Placement | Put each dimension on the view that shows the feature most clearly, outside the outline. |
| Units | Stated in the title block; not repeated on every dimension unless the drawing mixes units. |
| Tolerances | Required where fit or function depends on them. The default tolerance note is always present. |
| Scale | Dimensions govern. Do not measure the drawing to get a size. |

## 6. Number and unit formatting

### 6.1 Core rules (SI, after NIST SP 811 and ISO 80000-1)

| Rule | Correct | Incorrect |
|---|---|---|
| Space between number and unit symbol | 25 mm, 2.0 kN | 25mm, 2.0kN |
| Exception: plane angles | 30°, $15^{\prime}$ | 30 °, 30 deg |
| Exception: percent | 40 % (SI style) | 40% (informal, accepted in many documents) |
| Temperature | 25 °C (space before the symbol) | 25C, 25 degC in formal documents |
| No plural unit symbols | 10 kg, 3 m | 10 kgs, 3 ms |
| No period after a symbol, unless at sentence end | 5 mm | 5 mm. |
| Unit symbols are case-sensitive | kg, N, Pa, mm, MPa | Kg, n, mpa, Mm for millimeter |
| Compound units with a product | N m, or $\mathrm{N}\cdot\mathrm{m}$ | Nm (can be read as nanometers in some fonts or contexts) |
| Compound units with a quotient | $\mathrm{m/s}$, or $\mathrm{m}\,\mathrm{s}^{-1}$ | m per s |
| Symbols are not abbreviations | 2 h, not 2 hrs or 2 hours | |
| Names are lowercase in text | newton, pascal | Newton in running text |

Note: "Nm" is ambiguous and should not be used for newton-meters. Write "N m" to be safe.

### 6.2 Prefixes

Use prefixes in steps of 1000 for engineering values.

| Prefix | Symbol | Factor | Typical use |
|---|---|---|---|
| giga | G | $10^9$ | GPa (elastic modulus of stiff materials, typical) |
| mega | M | $10^6$ | MPa (stress), MW (power) |
| kilo | k | $10^3$ | kN, km, kg (kg is the base unit with a prefix) |
| milli | m | $10^{-3}$ | mm, mA, ms |
| micro | $\mu$ | $10^{-6}$ | µm (surface roughness, typical) |
| nano | n | $10^{-9}$ | nm |

Rules:

- Use capital M for mega and lowercase m for milli. Confusing these gives errors of a factor of one billion (mega is $10^6$, milli is $10^{-3}$).
- Avoid hecto, deka, deci, and centi in engineering text, except cm for specific cases where it is the accepted unit.
- Choose the prefix so the number falls between 0.1 and 1000 (for example 0.25 kN rather than 250 N, or 250 N if that is clearer; be consistent within a table).
- Do not combine two prefixes (write 1 µm, not 1 mµm).

### 6.3 Decimal marker and digit groups

- Use one decimal marker across a document: the period (US and most engineering documents) or the comma (ISO 80000-1 permits it), stated at the top.
- Group digits in threes separated by a thin space when a number has five or more digits (for example 12 345 kg). Do not use commas for grouping in SI-style documents.
- Write a leading zero before a decimal point: 0.25, not .25.

### 6.4 Significant figures

| Situation | Rule |
|---|---|
| Reporting a measured value | Report to the precision of the measurement. A 0.1 mm gauge gives 12.3 mm, not 12.345 mm. |
| Uncertainty | Give it to one or two significant figures; match the decimal place of the value. Write $12.34 \pm 0.05$ mm. |
| Calculations | Carry extra digits through the calculation. Round only the final result. |
| Trailing zeros | Significant only if a decimal point is written: 1200 has 2 significant figures; 1200. has 4; $1.200 \times 10^3$ has 4. Use scientific notation to remove doubt. |
| Exact counts and defined values | Have unlimited significant figures (for example 12 holes, or the defined value of the speed of light). |
| Percent | Give to the precision of the underlying data. "Yield 92 %" not "92.0348 %". |

Sanity check on the mass of a bar: $10\ \mathrm{mm} \times 10\ \mathrm{mm} \times 1\ \mathrm{m}$ of aluminum (density about $2700\ \mathrm{kg/m^3}$, typical) has a volume of $1 \times 10^{-4}\ \mathrm{m}^3$ and a mass of about 0.27 kg. Two significant figures are the most this estimate supports.

## 7. Figures, tables, and plots

### 7.1 Choosing the form

| Question | Use |
|---|---|
| How does a value change over time or position? | Line plot |
| How do two measured quantities relate? | Scatter plot, one point per measurement |
| How do a few categories compare? | Bar chart (bars must start at zero) |
| Exact values needed for lookup? | Table |
| Spread or distribution of many samples? | Box plot, histogram, or scatter with all points shown |
| A sequence of steps or a system? | Diagram (not a plot) |

### 7.2 Figure and table layout rules

| Element | Rule |
|---|---|
| Numbering | Figures numbered in order of first citation in the text: Figure 1, Figure 2. Tables numbered separately: Table 1, Table 2. |
| Caption position (common engineering convention) | Figure captions below the figure; table titles above the table. Follow the venue's style if it differs. |
| Caption content | What is shown, conditions, n (number of trials), what error bars mean, source. |
| Citation | Every figure and table is referred to in the text by number before it appears. |
| Axis labels | Quantity and unit: "Tip deflection (mm)". Not "Deflection". |
| Axis start | Linear axes do not have to start at zero, but say so if they do not. Bar charts start at zero. |
| Tick marks | Evenly spaced, using multiples of 1, 2, or 5. |
| Scale comparison | Same scale for plots compared side by side. |
| Legend | Label lines directly where possible. Use a legend only when direct labels do not fit. |
| Color | Do not rely on color alone. Add markers or line styles. Check the figure in grayscale. |
| Uncertainty | Show it; define it in the caption (standard deviation, standard error, or confidence interval). |
| Data points | Show individual points when there are few. State the number of points or trials. |
| Smoothing | Say so if a curve is smoothed. Do not present a smoothed fit as data. |
| Dual axes | Avoid. Two scales can make any two lines appear to cross. |
| 3D effects, shadows, gradients | Do not use. |

### 7.3 Table rules

- Column header: quantity and unit, for example "Deflection (mm)". Do not repeat the unit in every cell.
- Align numbers on the decimal point.
- Use the same precision within each column, matching the measurement.
- Give a caption or title that says what the table contains.
- Use a dash or "n/a" consistently for missing entries, and define it in a note.

## 8. Plain-language word list

Replace the word on the left with the one on the right. Delete the word if the sentence works without it.

| Replace | With |
|---|---|
| utilize | use |
| approximately | about |
| in order to | to |
| prior to | before |
| subsequent to | after |
| facilitate | help, or enable |
| commence | start |
| terminate | end, or stop |
| numerous | many |
| demonstrate | show |
| endeavor | try |
| ascertain | find out, or determine |
| methodology | method |
| sufficient number of | enough |
| in the event that | if |
| at this point in time | now |
| due to the fact that | because |
| with regard to | about, or on |
| a majority of | most |
| is able to | can |
| leverage | use |
| impact (as a verb) | affect |
| it should be noted that | (delete) |
| very unique | unique |
| in close proximity to | near |
| a large number of | many, or give the number |
| at a later date | later, or give the date |
| for the purpose of | for |
| in the process of | (delete, and use the verb) |
| e.g. (in running text) | for example |
| i.e. (in running text) | that is |
| soon, large, fast, small | give a number with a unit and a condition |

Word-level rules:

- Use "shall" only for requirements. Do not use it as a general future tense.
- Use "will" for facts or planned events.
- Use "about" with a number only when the value is an estimate. Use a value with its uncertainty when it is measured.
- Use "optimal" only if you can say what it is optimal for. Otherwise write "best" with a criterion, or give the value.

## Checklists

### Before sending any technical document

- [ ] The first paragraph states the purpose and the result or request.
- [ ] Every number has a unit, a condition, and, where it matters, an uncertainty.
- [ ] Every figure and table is numbered and cited in the text.
- [ ] Every acronym is defined on first use.
- [ ] Headings make sense when read alone.
- [ ] The conclusion follows from the evidence shown, with no new data.
- [ ] Citations use one style.
- [ ] Symbols and units follow Section 6.

### Before releasing a drawing

- [ ] Title block complete: name, number, revision, material, units, scale, default tolerance, projection symbol.
- [ ] Views are the fewest that define every feature; aligned by the projection rule.
- [ ] Line types and weights follow Section 5.1.
- [ ] Every feature has a size and a location.
- [ ] No feature is dimensioned twice.
- [ ] Every location dimension has a labeled datum.
- [ ] Notes cover finish and any process not shown by geometry.
- [ ] A second person has checked the drawing against the model.

### Before a presentation or review

- [ ] The goal sentence is written: "After this talk, the audience should ___."
- [ ] The first slide states the purpose and the decision needed.
- [ ] Each content slide has a headline sentence that states its message.
- [ ] Every number has a unit, a condition, and a source.
- [ ] Every chart labels its axes with quantity and unit.
- [ ] Risks and open questions are shown.
- [ ] The final slide states the decision or next step.
- [ ] The talk has been timed aloud.

### Before releasing a requirement, test plan, or ECR

- [ ] Each requirement has a unique ID, "shall", a measurable value with unit, a condition, and a verification method.
- [ ] Pass and fail criteria are written before testing.
- [ ] Equipment is listed with calibration status.
- [ ] Every affected drawing, BOM line, and document is listed in the ECR.
- [ ] Effectivity is stated.
- [ ] The document has a revision, a date, and an author.

### Before closing an incident report

- [ ] Impact is quantified with units.
- [ ] The timeline has sources for each entry.
- [ ] The root cause is backed by evidence and not only by opinion.
- [ ] Each corrective action has an owner, a due date, and a verification method.
- [ ] Affected documents are listed for update.

### Before sending an email asking for help

- [ ] One specific question is stated.
- [ ] What has been tried is listed, with results.
- [ ] Files or data are attached or linked by location.
- [ ] The deadline is in the subject line.
- [ ] Under about 150 words.

## Sanity checks

| Check | Catches |
|---|---|
| Read only the headlines in order. Do they tell the story and end at a decision? | Topic headings, buried conclusions |
| Could a machinist build the part from the drawing alone, without a question? | Missing sizes, locations, or notes |
| Could a reader who never saw the experiment say what varied, what was measured, and how sure we are? | Missing axis labels, units, or uncertainty |
| Does each side of an equation carry the same units? | Unit mismatch in calculations |
| Does a percentage fall between 0 and 100 unless it is a defined gain or change? | Mistyped or misread values |
| Does a bar chart start at zero? | Exaggerated differences |
| Does the same quantity have the same name and unit in every document? | Conflicting records |
| Can a new engineer explain what changed, why, and what to recheck, from the change log alone? | Incomplete change records |
| Does each requirement have a test that could fail? | Untestable requirements |
| Does the estimated number have the right order of magnitude (the 0.27 kg bar in Section 6.4)? | Factor-of-1000 slips from prefixes |

## Further reference

Named standards and books. Paid items are listed by name only. No free links are included in this sheet.

- ASME Y14.5, Dimensioning and Tolerancing (geometric dimensioning and tolerancing). Paid.
- ASME Y14.3, Multiview and Sectional View Drawings (projection and views). Paid.
- ASME Y14.2, Line Conventions and Lettering. Paid.
- ISO 128 (series), Technical drawings: general principles of presentation (line types and views). Paid.
- ISO 129-1, Technical drawings: indication of dimensions and tolerances. Paid.
- ISO 80000-1, Quantities and units: general (SI quantities, unit symbols, number formatting). Paid.
- NIST Special Publication 811, Guide for the Use of the International System of Units (SI). Free from NIST; locate the current edition by name.
- Strunk and White, The Elements of Style. Paid, widely available.
- Edward R. Tufte, The Visual Display of Quantitative Information. Paid; classic on honest graphics.
- Bryan A. Garner, Garner's Modern English Usage. Paid; usage and plain-word guidance.
- Chicago Manual of Style. Paid; citation and style conventions.
- Plain Writing Act of 2010 (United States) and the Plain Language Action and Information Network (PLAIN) guidance. Free; locate by name.
