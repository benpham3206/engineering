# Failure cases and decision frameworks

**Type:** reference

Failure analysis is the study of why engineered things break, and a decision framework is a structured way to choose what to do next. Engineers need both because most failures repeat patterns that a careful check can catch.

A lookup sheet for engineers who need to recall a documented failure, check a design against the patterns that repeat across failures, or decide when to stop, escalate, or refuse a piece of work.

## Principles

- Most failures are system failures. The physical cause is what broke; the root cause is the decision, process, or review that let it happen.
- A design is only as valid as its assumptions. Every assumption that was not tested is a hazard.
- Any change to a design, material, supplier, or operating condition needs a fresh analysis, not just a fresh look.
- Units are part of the interface. A number without a unit is not a value.
- Software and reused parts carry their assumptions with them. Reuse outside the original envelope is a new design.
- Warning signs are data. A concern that is recorded but not acted on is still a latent failure.
- Schedule and cost pressure do not change physics. They change which risks get accepted, so acceptance must be explicit and documented.
- Risk is never zero. The acceptable level is set by people responsible for the public, and the engineer's job is to make that decision informed.

## Failure case index

Dates are the year of the event. Death counts are as stated in the official or widely cited investigation; where counts vary by source, the count is given as approximate.

| Case | Year | What failed | Root cause (one line) | Lesson (one line) |
|---|---|---|---|---|
| Tay Bridge, Scotland | 1879 | Cast iron rail bridge collapsed in a gale under a passing train; 59 to 75 killed (estimates vary) | Design underestimated wind pressure; girder castings were poor quality | Design for the real environmental loads and inspect the material |
| Quebec Bridge, Canada | 1907 | Steel cantilever bridge collapsed during erection, 75 workers killed | Compression member overstressed by underestimated dead load; calculation errors not caught | Check erection and self-weight loads, and get independent verification |
| Boston molasses flood, USA | 1919 | Steel storage tank burst, about 2.3 million gal (8.7 million L) of molasses flooded streets; about 21 killed | Tank built too thin and weakly riveted, filled without proof testing; leaks ignored | Test before service and treat early warning signs as urgent |
| Tacoma Narrows Bridge, USA | 1940 | Suspension deck twisted and broke in moderate wind | Aeroelastic torsional flutter; shallow, flexible deck not analyzed for wind-structure interaction | Dynamic and aerodynamic effects must be analyzed, not only static loads |
| Liberty ships, USA | 1943 onward | Welded hulls cracked; some ships broke in two | Notch-sensitive steel at low service temperature (ductile-to-brittle transition), stress concentrations at corners | Specify and test material toughness at the lowest service temperature |
| de Havilland Comet, UK | 1954 | Two Comet 1 jet airliners broke up in flight | Metal fatigue starting at sharp window corners under repeated pressurization cycles | Full-scale fatigue testing and attention to stress concentrations |
| Ronan Point, UK | 1968 | Corner of a precast concrete tower collapsed after a gas explosion; 4 killed | Panel system lacked robustness; no alternate load path after one connection failed | Design for progressive collapse; a local failure must not remove the whole structure |
| Apollo 13, USA | 1970 | Oxygen tank explosion crippled the service module | Heater thermostats rated for 28 V were damaged by ground-test voltage of 65 V and hidden | Changes to test conditions and ratings must be traced to every component |
| Hyatt Regency walkways, USA | 1981 | Two suspended walkways collapsed onto a crowd; 114 killed | A rod arrangement was changed during construction, roughly doubling the connection load; change not reanalyzed | Re-analyze every change to a structure against the forces it creates |
| Therac-25, Canada and USA | 1985-1987 | Radiation therapy overdoses to patients, several deaths | Safety functions moved from hardware interlocks to software; race condition; dismissed incident reports | Software is part of the safety system and needs independent checks |
| Challenger, USA | 1986 | Shuttle broke apart 73 s after launch; 7 killed | O-ring joint failed in cold; engineers' concerns did not reach or move the launch decision | Technical risk must reach the decision maker, and decisions must weigh it |
| Chernobyl, Ukraine (then USSR) | 1986 | Reactor 4 destroyed in a steam explosion and fire during a test | Test run with safety systems disabled, procedure violations, and a reactor design with positive void reactivity feedback | Safety culture and design margins must hold when operators deviate from plan |
| Ariane 5 flight 501, France | 1996 | Rocket self-destructed about 37 s after launch | 64-bit float converted to 16-bit integer overflowed; inertial reference software reused from Ariane 4 outside its envelope | Reused software must be re-validated for the new operating conditions |
| Mars Climate Orbiter, USA | 1999 | Spacecraft lost on arrival at Mars | Ground software output impulse in pound-force seconds; navigation expected newton-seconds | Interface units must be specified and checked at every handoff |
| Columbia, USA | 2003 | Shuttle broke up on reentry; 7 killed | Foam from the external tank struck the wing leading edge; repeated foam strikes were normalized as not a safety issue | Recorded anomalies require analysis, not acceptance by precedent |
| Deepwater Horizon, USA | 2010 | Well blowout, rig fire and sinking; 11 killed | Negative pressure test misread; blowout preventer failed to seal; barriers defeated together | Treat a surprising test result as a stop signal and verify each barrier |
| Fukushima Daiichi, Japan | 2011 | Loss of cooling and meltdowns at three reactors after earthquake and tsunami | Seawall lower than the tsunami that struck; backup generators at low elevation; inadequate beyond-design-basis planning | Protect against the hazard you have not yet seen, and keep backups independent |
| Boeing 737 MAX, USA and international | 2018-2019 | Two airliners crashed; 346 killed | MCAS flight control relied on one angle-of-attack sensor; behavior poorly disclosed; certification relied on delegated review | Safety-critical functions need redundancy, full disclosure, and independent review |

## Repeating patterns

| Pattern | Where it appears | What to check |
|---|---|---|
| Unit errors | Mars Climate Orbiter; Ariane 5 integer overflow (a range error, closely related) | Every interface states units and ranges; conversions are tested at boundaries |
| Untested assumptions | Tay Bridge (wind), Tacoma Narrows (aeroelasticity), Comet (fatigue), Liberty ships (toughness at low temperature) | List assumptions explicitly and map each to a test or analysis |
| Design change without re-analysis | Hyatt Regency; Apollo 13 (test conditions); Boeing 737 MAX (added function) | Every change triggers the same review as an original design |
| Normalization of deviance | Challenger; Columbia; Deepwater Horizon | Repeated anomalies are tracked to a closed cause, not a precedent of acceptance |
| Software reuse outside its envelope | Ariane 5; Therac-25 (legacy assumptions) | Reused code is re-validated against the new environment and inputs |
| Schedule and cost pressure | Challenger; Chernobyl (test schedule); Quebec Bridge (erection schedule) | Acceptance of a reduced margin is written down with its owner and reason |
| Single point of protection | Boeing 737 MAX (single sensor); Fukushima (single backup power); Therac-25 (software-only interlock) | Independent protections for each hazard; no single sensor or path controls a catastrophic outcome |
| Confirmation bias in tests | Deepwater Horizon (negative pressure test) | Define failure criteria before the test; a result that contradicts expectation is investigated |

## Professional ethics canons

Summarized in plain words from common codes of ethics for engineers (for example those of national engineering societies and licensing bodies). Read the full code of your own jurisdiction for binding wording.

- Public safety comes first. When it conflicts with an employer's or client's wishes, schedule, or budget, public safety governs.
- Work only where you are competent. Say so when a question is outside your training, and bring in qualified help.
- Be honest and objective. Reports, estimates, and public statements must not hide known risks or overstate confidence.
- Serve employers and clients faithfully, and keep their confidences, up to the point where that service would endanger the public.
- Avoid conflicts of interest and undisclosed incentives that could bend a judgment.
- Own your signature. A stamp, certification, or sign-off claims that the work is competent and safe, and you answer for that claim.
- Keep the profession's trust. Deceptive or careless conduct harms every engineer's ability to be believed.

## Risk matrix

$\text{Risk score} = \text{likelihood score} \times \text{severity score}$. Choose the scores from the definitions below, then read the band.

Likelihood (over the life of the product or activity):

| Score | Level | Meaning (typical) |
|---|---|---|
| 1 | Rare | Not expected in the life of the system |
| 2 | Unlikely | Could occur once in many systems or lifetimes |
| 3 | Possible | Could occur in some systems during life |
| 4 | Likely | Expected to occur in some systems or operations |
| 5 | Frequent | Expected to occur repeatedly |

Severity (consequence to people and the mission):

| Score | Level | Meaning (typical) |
|---|---|---|
| 1 | Negligible | No injury; minor cost or delay |
| 2 | Minor | First aid injury; limited damage |
| 3 | Serious | Lost-time injury; significant damage or mission loss |
| 4 | Severe | Permanent injury or multiple injuries; major loss |
| 5 | Catastrophic | Death or multiple deaths; loss of the system |

Matrix ($\text{score} = L \times S$):

| Likelihood \ Severity | 1 Negligible | 2 Minor | 3 Serious | 4 Severe | 5 Catastrophic |
|---|---|---|---|---|---|
| 5 Frequent | 5 | 10 | 15 | 20 | 25 |
| 4 Likely | 4 | 8 | 12 | 16 | 20 |
| 3 Possible | 3 | 6 | 9 | 12 | 15 |
| 2 Unlikely | 2 | 4 | 6 | 8 | 10 |
| 1 Rare | 1 | 2 | 3 | 4 | 5 |

Bands and required action:

| Score | Band | Required action |
|---|---|---|
| 1-4 | Low | Accept with monitoring; record the decision |
| 5-9 | Moderate | Mitigate where practical; record the owner and the residual risk |
| 10-15 | High | Reduce before proceeding; sign-off by a responsible authority |
| 16-25 | Extreme | Stop the activity until the hazard is eliminated or the risk is reduced to High or below |

Holds when: the scores reflect honest estimates and the hazard list is complete. Breaks when: likelihood is estimated from a small sample, when common-cause failures make independent events not independent (for example two sensors on the same bracket), or when a rare severe event has no data. A matrix does not replace analysis for a catastrophic hazard; it only ranks what the analysis must address.

## Hazard control hierarchy

Strongest to weakest. Use the highest level that is practical, and combine levels for catastrophic hazards.

| Level | Control | Example | Weakness |
|---|---|---|---|
| 1 | Eliminate | Remove the stored energy, the toxic material, or the function that is not needed | Often not possible for the core function |
| 2 | Substitute | Use a lower-voltage supply, a less toxic solvent, or a tougher material | Substitute can introduce its own hazard |
| 3 | Engineering controls | Interlocks, guards, relief valves, redundant sensors, independent hardware trips | Can be bypassed, degraded, or defeated by common cause |
| 4 | Administrative controls | Procedures, permits, training, checklists, labels, alarms | Depends on people following them under pressure |
| 5 | Personal protective equipment | Gloves, respirators, hearing protection, helmets | Last line; does nothing for the others and fails when worn wrong |

Rules that follow from the hierarchy:

- A warning label is never the only control for a catastrophic hazard.
- A procedure that requires a person to notice a problem and act within seconds is an engineering weakness, not a safe design.
- Independence matters. Two controls that share a sensor, power source, software, or maintenance error are one control.

## Decision frameworks

### When to stop work

Stop, or do not start, when any of these hold:

- A hazard is identified that is not in the analysis, and its severity is unknown.
- A requirement, change, or test result contradicts the analysis that approved the design.
- A safety-related value is outside its validated range, or a test result is unexplained.
- A change was made without the review it requires.
- The work needs competence the team does not have and cannot get in time.
- The risk score is Extreme (16-25) and no control is in place.
- Records or evidence are missing for a safety claim you are being asked to sign.

Stop means: make the activity safe (shut down, isolate, or hold), write down the reason, and report it to the person who can decide to resume.

### How to escalate a safety concern

Work up the chain, one step at a time, and keep a written record at each step.

1. State the concern in writing: the hazard, the evidence, the people exposed, and the requirement it violates.
2. Raise it with the person responsible for the work, and ask for a written response with the reasoning.
3. If unresolved, raise it with the technical authority or safety, quality, or review function that is independent of the schedule.
4. If still unresolved, raise it with the senior technical leader or the executive responsible for safety.
5. If the hazard is to the public and internal channels fail, use the external route: the regulator, the licensing board, or the authority that has jurisdiction. Know your organization's protections for reporting in good faith before you use them.
6. Keep your own copy of the record, and keep the facts separate from opinions.

Escalation is not a personal attack. It is the process that lets the people who own the decision see the evidence.

### How to say no

A clear refusal has four parts:

- The fact: what the analysis or test shows.
- The consequence: what hazard follows if the work proceeds as asked.
- The requirement: the code, standard, procedure, or specification that applies.
- The alternative: what you can do now (add a check, reduce scope, delay, or use a different method) and what you need to do it.

Put it in writing. Do not sign, stamp, or release work you believe is unsafe. Do not comply silently and hope the problem resolves itself. Do not overstate your certainty; say what you know, what you do not, and who can resolve the gap.

## Checklists

Before trusting a result:

- [ ] Units checked at every interface and conversion, with a boundary test
- [ ] Assumptions listed, and each one tied to a test, analysis, or stated limit
- [ ] Operating envelope stated, and the design checked against its edges
- [ ] Reused parts or code validated for this envelope, not just the earlier one
- [ ] Failure criteria defined before testing
- [ ] Independent check or peer review done for safety-critical results

Before releasing a design or change:

- [ ] Every change since the last approved analysis is listed and re-analyzed
- [ ] Hazard list is complete and each hazard has a control at the highest practical level
- [ ] No catastrophic hazard depends on a single sensor, path, person, or label
- [ ] Known anomalies are closed with a cause and a corrective action, not just accepted
- [ ] Risk scores are recorded, with the owner of each accepted risk
- [ ] Training, procedures, and maintenance instructions match the design as built

When a concern is raised:

- [ ] Concern written in one sentence with the supporting evidence
- [ ] People exposed identified
- [ ] Qualification to judge checked, with a second expert if needed
- [ ] Recipient of the concern named and the reply recorded
- [ ] Decision and reasons written down

## Sanity checks

- Unit conversions: $1\ \mathrm{lbf} = 4.4482216152605\ \mathrm{N}$ (exact by definition); so $1\ \mathrm{lbf}\,\mathrm{s} = 4.448\ \mathrm{N}\,\mathrm{s}$. $1\ \mathrm{in} = 25.4\ \mathrm{mm}$ exactly. A result off by a factor near 4.45 or 25.4 is likely a units mismatch.
- Integer range: a signed 16-bit integer holds at most 32767. Any physical quantity converted into it must be checked against that limit before conversion.
- Safety factor: a value below 1 means the load exceeds the strength ($\text{strength} / \text{load} = 0.8$ means failure). A value near 1 with an uncertain load is not margin.
- Redundancy: if two "independent" sensors read the same wrong value, ask whether they share a mount, a power source, or the same software.
- Test result: if a test passes exactly on the first try, ask whether the pass criteria were set after seeing the data.
- Recorded anomalies: if the same anomaly has appeared in three or more flights, tests, or shifts without a closed cause, it is a trend, not noise.

## Further reference

- Henry Petroski, *To Engineer Is Human: The Role of Failure in Successful Design* (St. Martin's Press, 1985): essays on how failures drive design.
- Nancy G. Leveson, *Engineering a Safer World: Systems Thinking Applied to Safety* (MIT Press, 2011): systems-based safety analysis, including the Therac-25 and other cases.
- Charles Perrow, *Normal Accidents: Living with High-Risk Technologies* (Basic Books, 1984): accidents in tightly coupled, complex systems.
- Diane Vaughan, *The Challenger Launch Decision: Risky Technology, Culture, and Deviance at NASA* (University of Chicago Press, 1996): normalization of deviance.
- National Transportation Safety Board and Accident Investigation Board reports for aviation accidents (free public record; search by accident name or date).
- National Commission on the BP Deepwater Horizon Oil Spill and Offshore Drilling, *Report to the President* (2011): official findings on barriers and well control.
- International Atomic Energy Agency, INSAG-7, *The Chernobyl Accident: Updating of INSAG-1* (1992): official safety culture findings.
- Ariane 501 Inquiry Board report (Lions report, 1996): official findings on the software reuse failure.
- MIL-STD-882E, *System Safety* (U.S. Department of Defense): hazard analysis and risk matrix method.
- ISO 31000, *Risk management: Guidelines*: general risk management principles.
- ISO 12100, *Safety of machinery: General principles for design: Risk assessment and risk reduction*: hazard control hierarchy for machinery.
- ANSI/AIHA Z10, *Occupational Health and Safety Management Systems*: management system framework.
