# Module 3. Scenario Planning and the Learner's Journey

Module id: `m3`
Steps: 5
ID check-in: live review of this module's sections, at the end of the week or sooner

Faculty complete: the course storyline premise, one scenario per module, and a scenario plan for
one module.

Refresh checks for this module: each scenario calls for that module's objectives; pressure builds
across modules.

No refresh reflection in this module. Scenarios are new work for nearly every course. In the
refresh track, the AI builds scenarios from cases and examples the course already uses where
they fit.

Sources: `src:assignment-m3-identifying-scenarios`, `src:guide-storytelling`,
`src:example-mgmt615-scenarios`, `src:example-mgmt615-episodes`, `src:example-mgmt615-character`,
`src:example-mgmt615-course-map`

Demo data: `demo/mgmt615-scenarios.json`

---

## 3.1 Your storyline

Time: about 20 minutes

### Learn

In Module 2 you built a character and named the conflict at the center of your course. The
storyline is what happens to that character from the first module to the last.

At the course level, the character has one long-term goal, and it lines up with your CLOs. Each
module then puts a new obstacle or decision in the way. Some decisions move the character
closer to the goal, and some set them back. Because the same person keeps coming back, students
see how a decision in Module 2 shapes what is possible in Module 7, which is how the skills
connect on the job.

A storyline premise keeps it focused. It's one sentence:

"[Course] is a story about [character, role] who struggles to [long-term goal] when [the
conflict]."

A storyline works when:

- **Pressure builds.** Early modules can start small. By the last few, more is at stake and the
  character has fewer easy options.
- **Every CLO gets a turn.** Each CLO should drive at least one module's decision.
- **The details hold.** Names, numbers and relationships stay the same from module to module.
- **The setting changes at least once.** A student who follows one character through one company
  learns to reason about that company. To help students apply the thinking elsewhere, put at
  least one scenario in a different setting, such as a sister site, a client or the character's
  past job (Gick & Holyoak, 1983).

### See it

MGMT 615's storyline premise: "MGMT 615 is a story about Dana Ortiz, a newly promoted operations
manager, who struggles to find and fix the real causes of her site's slipping performance before
peak season, when her director has already decided who to blame."

The arc runs from Dana's first bad week in Module 1, when on-time shipping drops, to Module 8,
when she hires the shift lead who will own the broken handoff for good. The pressure rises as
peak season gets closer. By Module 5 she has to tell her director he's wrong, and by Module 6
peak season has started.

### Draft (full build)

AI instructions:

```text
Draft a storyline for the course from the character profile, the conflict (step 2.4), the CLOs
and the module titles and topics. Return:
1. A storyline premise in the form "[Course] is a story about [character, role] who struggles
   to [long-term goal] when [conflict]."
2. An arc: one line per module giving a working episode title and the decision the character
   faces, in module order. Each decision must call for that module's CLOs. Pressure should rise
   across the modules.
3. A one-sentence note on where pressure peaks.
Use the character profile exactly as written. Do not change names, numbers or relationships.

Return: {"premise": string, "arc": [{"module": int, "title": string, "decision": string, "clos": [string]}], "peak": string}
```

Demo response (MGMT 615): the premise above, and the arc from the episode titles in
`demo/mgmt615-scenarios.json`. Peak note: "Pressure peaks in Module 5, when Dana has to
challenge her director with a week until his deadline."

### Review (refresh)

If the uploaded document has a storyline, the app shows it and checks it. If not, this step runs
as a full build.

AI instructions:

```text
The faculty member's existing storyline is given. Check it against this checklist: a premise
names the character, the long-term goal and the conflict; pressure builds across modules; every
CLO drives at least one module; details stay consistent. Keep what passes. For each gap, quote
the problem and suggest a fix. Then return a premise and arc as in the full build.

Return: {"passes": boolean, "issues": [string], "premise": string, "arc": [...], "peak": string}
```

Demo response (MGMT 615): no storyline in the course map, so this step runs as a full build.

### Decide

The faculty member edits the premise and the arc. Episode titles stay working titles until step
3.2 and 3.3.

Checklist:

- The premise names the character, the goal and the conflict.
- Pressure rises across the modules.
- Every CLO drives at least one module's decision.
- At least one module is in a different setting, if transfer matters for your course.

### Save

Planning document: storyline premise at the start of the Storyline section.
Project file: `story.premise`, `story.arc`.

### Go deeper (optional)

- `src:guide-storytelling`: Building Your Storyline, and the options for courses where one
  character doesn't fit.
- `src:ext-gick-holyoak-1983`

---

## 3.2 Scenarios for Modules 1 to 4

Time: about 30 minutes

### Learn

A scenario is one specific moment in your storyline: your character has to make a decision that
calls for that module's objectives. It doesn't need to be dramatic. It needs to be specific.

Look for turning points. Reasonable professionals disagree about a decision. A plan looks sound
until reality exposes a weakness. New data, or a stakeholder, forces a change in approach. A
mistake is easy to make and costly to fix.

Each scenario answers five questions:

- **Situation.** What's the setting, and what was supposed to happen?
- **Trigger.** What went wrong or became uncertain, and what new pressure appeared?
- **Stakeholders.** Who is affected, and who else has something at stake?
- **Decision.** What has to be decided, and which options are realistically on the table?
- **Outcome and learning.** What changes at the end, and which idea from this module would have
  improved the outcome?

A good scenario can't be handled well without the module's skills, and its options are ones a
professional could defend. If one option is obviously right, students learn to spot the answer
the course wants instead of making a judgment.

A clear scenario now saves work later. The same moment can anchor a module overview, a
discussion, an assignment and a cohort session.

In this step you choose scenarios for Modules 1 to 4. Step 3.3 covers Modules 5 to 8.

### See it

MGMT 615, Module 4, "The Handoff Nobody Owns":

| | |
|---|---|
| Situation | The two shifts pass work to each other every afternoon, but no one owns the handoff. |
| Trigger | The shift leads now blame each other for the late orders. Greg, the director, suggests a team-building lunch. |
| Stakeholders | Both shift leads and their crews, Dana, Greg, customers. |
| Decision | Host the lunch, hold a joint meeting to air the tension, or change the structure: name a handoff owner and add a shared checklist and an overlap window. |
| Outcome and learning | A team-effectiveness framework shows the problem is unclear roles, so a lunch won't touch it. Dana has to explain to Greg why the structural fix beats his idea. |

### Draft (full build)

The AI proposes two scenarios for each module. The faculty member picks one per module, edits it,
or writes their own.

AI instructions:

```text
Propose two scenario options for each of the given modules, using the storyline arc (step 3.1),
the character profile, the CLOs and each module's title, CLOs met and topics. Each option puts
the character in a moment of decision that calls for that module's CLOs. Use the character
profile exactly as written. For each option give: a short episode title; a premise in the form
"[Character] struggles to [decision] when [complication]."; the CLOs it supports; situation;
trigger; stakeholders; decision with 2 or 3 realistic options a professional could defend;
outcome and learning, naming the module concept that improves the outcome. Keep each element to
one or two sentences. The first option should follow the arc; the second can depart from it.

Return: {"modules": [{"module": int, "options": [{"title": string, "premise": string, "clos": [string], "situation": string, "trigger": string, "stakeholders": string, "decision": string, "outcome": string}]}]}
```

Demo response (MGMT 615): modules 1 to 4 from `demo/mgmt615-scenarios.json`, with `chosen` as
the first option and `alternative` as the second.

### Review (refresh)

If the uploaded document has scenarios for these modules, the app checks them. Either way, the
AI draws on the course's existing cases and examples.

AI instructions:

```text
The faculty member's existing scenarios for these modules are given, if any, along with each
module's current activities and materials. For existing scenarios, check: the decision calls for
that module's CLOs; the options are ones a professional could defend; the stakes are visible;
character details match the profile. Keep what passes and suggest fixes for the rest.
For modules with no scenario, propose two options as in the full build. Where an existing case
or example fits, build an option from it and name the case.

Return: {"modules": [{"module": int, "existing": {"passes": boolean, "issues": [string]} | null, "options": [...]}]}
```

Demo response (MGMT 615): no scenarios in the course map, so the full-build options play, with
one note added to Module 1: "Your existing case, Maria's First Ninety Days, covers the same
moment from another company. Keep it as a contrast: students compare Maria's first quarter with
Dana's first bad week."

### Decide

For each module the faculty member picks an option, edits it, or writes their own. They can ask
for new options for one module without redoing the others.

Checklist (for each scenario):

- The decision can't be made well without this module's skills.
- There are two or three options a professional could defend.
- The stakes are visible.
- Names, numbers and relationships match your character profile.

### Save

Planning document: the Scenario row in Table 1 (episode title and premise for each module).
Project file: `modules[0..3].scenario` (all five elements, title, premise and CLOs).

---

## 3.3 Scenarios for Modules 5 to 8

Time: about 30 minutes

### Learn

Same process as step 3.2, for the second half of your course.

The second half is usually where pressure peaks. By now your character has made decisions that
have consequences, and earlier choices can come back. In MGMT 615, the bonus Dana questions in
Module 2 is the change she has to announce in Module 7, and the handoff she diagnoses in Module 4
is the role she hires for in Module 8.

Look for those callbacks. A scenario that depends on an earlier decision shows students that the
skills build on each other.

### See it

MGMT 615, Module 8, "Proven vs. Potential": Dana has approval for a new shift-lead role that will
own the handoff, the permanent fix for the gap that started the story. The finalists are an
outside candidate who has run shift operations elsewhere and Luis, a highly accurate associate
who has never supervised anyone. The night-shift lead backs the outside hire, and the crew is
watching to see whether Luis gets a shot. A structured interview scorecard keeps Dana from
deciding on experience or loyalty alone.

### Draft (full build) and Review (refresh)

Same instructions as step 3.2, for modules 5 to 8. The AI also receives the scenarios saved in
step 3.2, so it can build callbacks.

Additional instruction:

```text
Where it fits, connect a scenario to a decision the character made in an earlier module, and
say which one.
```

Demo response (MGMT 615): modules 5 to 8 from `demo/mgmt615-scenarios.json`.

### Decide

Same as step 3.2.

### Save

Planning document: the Scenario row in Table 2.
Project file: `modules[4..7].scenario`.

> Review note: the MGMT 615 scenarios now use the revised CLO numbers from step 1.4. Module 8
> maps to CLO 6 (hiring) instead of CLO 4. Module 2's alternative ("Luis Checks Out"), Module 4's
> ("Two Shifts, Two Rulebooks") and Module 7's ("The Overlap Window") are new, written to give the
> AI two options in every module. The other alternatives are the side plots from
> `src:example-mgmt615-character`.

---

## 3.4 Check the storyline

Time: about 20 minutes

### Learn

Read your eight scenarios in order, as a student would meet them. Scenarios that each work alone
can still fail as a story.

Look for:

- **Flat pressure.** If Module 7 feels no harder than Module 2, raise the stakes or tighten the
  time.
- **A missing CLO.** Every CLO should drive at least one scenario's decision.
- **Drift.** A name, number or relationship that changed along the way.
- **Repeats.** Two scenarios with the same decision in different clothes.
- **One setting throughout.** If transfer matters for your course, put one scenario somewhere
  else.

This step runs one check across all eight. Fix what you can; anything you keep gets a short note.

### See it

MGMT 615's check passed with one note: every scenario takes place at Dana's site. The instructor
kept it, with the note "Module 5 uses data from a sister site, and the existing cases in Modules
1, 2, 4 and 7 give students other companies to compare."

### Draft (full build) and Review (refresh)

Same instructions for both tracks.

AI instructions:

```text
Check the eight saved scenarios as one storyline against the character profile and the CLOs:
1. Pressure rises across the modules.
2. Every CLO drives at least one scenario's decision.
3. Names, numbers and relationships match the profile and each other.
4. No two scenarios turn on the same decision.
5. At least one scenario uses a different setting.
Return one result per check: pass, or issue with the module(s) involved and a one-sentence fix.

Return: {"checks": [{"check": string, "result": "pass" | "issue", "modules": [int], "detail": string | null}]}
```

Demo response (MGMT 615):

```json
{
  "checks": [
    {"check": "Pressure rises", "result": "pass", "modules": [], "detail": null},
    {"check": "Every CLO drives a decision", "result": "pass", "modules": [], "detail": null},
    {"check": "Details are consistent", "result": "pass", "modules": [], "detail": null},
    {"check": "No repeated decisions", "result": "pass", "modules": [], "detail": null},
    {"check": "A different setting", "result": "issue", "modules": [1, 2, 3, 4, 5, 6, 7, 8], "detail": "Every scenario takes place at Dana's site. Consider setting one, such as Module 6, at the sister site Alicia runs."}
  ]
}
```

### Decide

For each issue, Fix (opens the scenario) or Keep with a note.

Checklist:

- Every issue is fixed or has a note.

### Save

Planning document: nothing new. In refresh, the change log covers any scenario changes.
Project file: `alignment.m3` (checks and notes).

---

## 3.5 Plan one scenario

Time: about 30 minutes

### Learn

A scenario tells you what happens. A scenario plan tells someone how to build it. Pick one
module's scenario and lay it out row by row, in a table with four columns:

| What happens | Students see | Students read or hear | Students do |
|---|---|---|---|

Break the scenario into two to four rows, one for each moment. Keep the last column busy:
every row should give students something to decide, answer or produce, tied to the decision at
the center of the scenario.

Check each row against three of Mayer's principles (Mayer, 2021):

- **Coherence.** Cut details that don't help with the decision.
- **Signaling.** Mark what matters with a heading, a highlight or an arrow.
- **Segmenting.** Split a dense moment into two shorter ones.

Then choose how to deliver it. The decision stays the same whatever the medium.

| Medium | Best for | Needs the media team? |
|---|---|---|
| Module overview page | Introducing the week's story and decision | No |
| Interactive reading | A self-paced walk-through with short checks between moments | No |
| Interactive case | Using a course tool mid-story, such as an analysis or a calculation | No |
| Branching simulation | Practicing a decision and seeing its consequences | No, but the heaviest lift |
| Discussion case | Students argue what the character should do | No |
| Narrated slide deck | A paced visual story you record yourself | No |
| Short video | Setting tone and stakes fast, or modeling an expert's reasoning | Yes |
| Audio narrative | Tone and tension through voice, for listening on the go | Yes |

You'll plan all your media in Module 6. Choosing now tells your ID which scenarios might need
production.

### See it

MGMT 615 planned Module 4, "The Handoff Nobody Owns," as an interactive case:

| What happens | Students see | Students read or hear | Students do |
|---|---|---|---|
| 4:45 p.m. handoff: day shift leaves, night shift finds 60 orders with no notes | Photo of the dock; the handoff sheet, half blank | Ray's message to Dana: "Same as every day." | List what's missing from the handoff sheet |
| Ray and Jordan each blame the other | Two short messages side by side | Both leads' accounts | Use the team-effectiveness framework to name the real problem |
| Greg suggests a team-building lunch | Greg's email | "Let's get everyone on the same page." | Choose an intervention and justify it in 150 words |
| Debrief | Dana's handoff checklist and overlap window | What happened two weeks later | Compare your choice with Dana's |

### Draft (full build) and Review (refresh)

The faculty member picks a module. The AI drafts the plan from that module's saved scenario.

AI instructions:

```text
Turn the saved scenario for the chosen module into a scenario plan: 2 to 4 rows, one per moment,
with four columns: what happens, students see, students read or hear, students do. Write any
narration in natural spoken language. Every "students do" cell must point to the scenario's
decision or a concept from the module, never to decorative detail. Apply coherence, signaling
and segmenting. Then recommend one medium from: module overview page, interactive reading,
interactive case, branching simulation, discussion case, narrated slide deck, short video, audio
narrative. Give a one-sentence reason and say whether it needs the media team.

Return: {"module": int, "rows": [{"happens": string, "see": string, "readHear": string, "do": string}], "medium": string, "reason": string, "needsMediaTeam": boolean}
```

Demo response (MGMT 615): the Module 4 plan above, with medium "interactive case" and reason
"Students apply the team-effectiveness framework mid-story, which a case supports without
filming."

Refresh track: the same step. If the uploaded document already has a scenario plan or a case
write-up for a module, the faculty member can start from it.

### Decide

The faculty member edits the rows and the medium.

Checklist:

- Each row has something for students to do.
- Every "do" ties back to the decision or a module concept.
- Nothing on screen or in the narration is there only for color.
- You know whether this scenario needs the media team.

### Save

Planning document: nothing yet. Module 6 adds the medium to the Learning Media Plan row.
Project file: `modules[n].scenarioPlan` (rows, medium, reason, needsMediaTeam).

> Review note: the V3 course map plans XR stage recordings in Module 4 and XR cohort sessions in
> Module 7. An XR-stage video is a production option that belongs in the medium table above, but
> no source file describes what the XR stage offers or when to use it. Can you share a
> description, or should XR wait for Module 6?

### Go deeper (optional)

- `src:guide-storytelling`: Turning Your Storyline into Scenarios, and Scenario Planning.
- `src:jobaid-media-selection-matrix`
- `src:guide-active-learning`
- `src:guide-adult-learners`
- `src:ext-mayer-2021`
