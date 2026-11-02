# Module 3. Scenario Planning and the Learner's Journey

Module id: `m3`
Steps: 2
ID check-in: live review of this module's sections, at the end of the week or sooner

Faculty complete: the course storyline premise and one scenario per module.

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

Time: about 15 minutes
Pattern: interview, then draft (full build) or edit in place (refresh)

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
Draft a storyline for the course from the character profile, the conflict (step 2.2), the CLOs
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
3.2.

Checklist:

- The premise names the character, the goal and the conflict.
- Pressure rises across the modules.
- Every CLO drives at least one module's decision.
- At least one module is in a different setting, if transfer matters for your course.

### Checks

On save: the premise names the character, the goal and the conflict; every CLO drives at least
one module in the arc.

### Save

Planning document: storyline premise at the start of the Storyline section.
Project file: `story.premise`, `story.arc`.

### Go deeper (supplemental)

- `src:guide-storytelling`: Building Your Storyline, and the options for courses where one
  character doesn't fit.
- `src:ext-gick-holyoak-1983`

---

## 3.2 Scenarios for every module

Time: about 45 minutes, about 5 minutes a module
Pattern: pick and combine, one module at a time (full build); edit in place (refresh)

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

Work one module at a time, in order. The second half is usually where pressure peaks, and earlier
decisions can come back: in MGMT 615, the bonus Dana questions in Module 2 is the change she
announces in Module 7. A scenario that depends on an earlier decision shows students that the
skills build on each other.

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

For modules after the first, add:

```text
Where it fits, connect a scenario to a decision the character made in an earlier module, and
say which one.
```

Demo response (MGMT 615): each module from `demo/mgmt615-scenarios.json`, with `chosen` as the
first option and `alternative` as the second.

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

### Checks

On save of each scenario: the decision calls for the module's CLOs; two or three defensible
options; character details match the profile.

When all scenarios are saved, a storyline check runs across them and shows flags on the modules
involved.

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

Demo kept note: MGMT 615's check passed with one note: every scenario takes place at Dana's site. The instructor
kept it, with the note "Module 5 uses data from a sister site, and the existing cases in Modules
1, 2, 4 and 7 give students other companies to compare."

### Save

Planning document: the Scenario row in Tables 1 and 2 (episode title and premise).
Project file: `modules[].scenario` (all five elements, title, premise and CLOs); `alignment.m3`.

> Review note: the MGMT 615 scenarios now use the revised CLO numbers from step 1.3. Module 8
> maps to CLO 6 (hiring) instead of CLO 4. Module 2's alternative ("Luis Checks Out"), Module 4's
> ("Two Shifts, Two Rulebooks") and Module 7's ("The Overlap Window") are new, written to give the
> AI two options in every module. The other alternatives are the side plots from
> `src:example-mgmt615-character`.

### Go deeper (supplemental)

- `src:guide-storytelling`: includes scenario planning, which you'll do with your ID during
  development for scenarios that need production.
- `src:jobaid-media-selection-matrix`
- `src:guide-active-learning`
- `src:guide-adult-learners`
- `src:ext-mayer-2021`

---

## Check-in prep

Same instructions as Module 1.

Demo response (MGMT 615):

```json
{
  "changed": ["Storyline premise: new", "Scenarios for all eight modules: new"],
  "keptFlags": ["Every scenario is at Dana's site: Module 5 uses sister-site data, and existing cases give other companies to compare"],
  "questions": ["Which scenarios are worth producing as video, and which work as readings or discussion cases?", "Does the Module 5 scenario, where Dana challenges her director, need framing for students?"]
}
```

Project file: `checkins.prep.m3`.
