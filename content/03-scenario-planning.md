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

::: purpose
**What you'll do:** Draft your course's storyline: a one-sentence premise and the arc of decisions
your character faces from the first module to the last.

**Why it matters:** Because the same person keeps coming back, students see how a decision in one
module shapes what's possible later, which is how the skills connect on the job.
:::

In Module 2 you built a character and named the conflict at the center of your course. This module
turns them into a story.

At the course level, the character has one long-term goal, and it lines up with your CLOs. Each
module then puts a new obstacle or decision in the way. Some decisions move the character closer to
the goal, and some set them back.

A storyline premise keeps it focused. It's one sentence:

"[Course] is a story about [character, role] who struggles to [long-term goal] when [the
conflict]."

A storyline works when:

- **Pressure builds.** Early modules can start small. By the last few, more is at stake and the
  character has fewer easy options.
- **Every CLO gets a turn.** Each CLO should drive at least one module's decision.
- **The details hold.** Names, numbers, and relationships stay the same from module to module.
- **The setting changes at least once.** A student who follows one character through one company
  learns to reason about that company. To help students apply the thinking elsewhere, put at
  least one scenario in a different setting, such as a sister site, a client, or the character's
  past job (Gick & Holyoak, 1983).

### See it

::: full
Here's the storyline the MGMT 615 instructor settled on.
:::

::: refresh
MGMT 615's Course Map had no storyline, so the instructor built one, as on the full build. Here's
what they settled on.
:::

::: plan Storyline premise
MGMT 615 is a story about Dana Ortiz, a newly promoted operations manager, who struggles to find
and fix the real causes of her site's slipping performance before peak season, when her director
has already decided who to blame.
:::

::: figure arc | MGMT 615's arc: pressure rises toward peak season
- 1 | The First Bad Week | 1
- 2 | The Bonus That Backfired | 2
- 3 | The Conversation With Jordan | 2
- 4 | The Handoff Nobody Owns | 3
- 5 | Telling Greg He's Wrong | 5 | peak
- 6 | Twelve Things on Dana's List | 4
- 7 | Ending the Bonus | 4
- 8 | Proven vs. Potential | 4
- Note | Pressure peaks in Module 5, when Dana has to tell her director he's wrong. Peak season starts in Module 6, so the stakes stay high to the end.
:::

### Draft (full build) and Review (refresh)

Answer the optional question if you want a say in where the story goes, then select the button
below. The AI drafts a premise and an arc: one line per module with a working episode title and the
decision your character faces, built from your character, conflict, CLOs, and modules. Under the
draft, select **Use this storyline** to copy it into the boxes under Decide.

::: refresh
If your Course Map already has a storyline or a case that runs through several modules, the AI
starts from it instead: it checks it against the Learn section, keeps what works, and suggests
fixes.
:::

::: fields
- What does your character want by the end of the course? (optional) | To get her site running well without fixing everything herself, and to keep her team through peak season.
:::

::: full
AI instructions:

```text
Draft a storyline for the course from the character profile, the conflict (step 2.2), the CLOs,
and the module titles and topics. Include:
1. A storyline premise in the form "[Course] is a story about [character, role] who struggles
   to [long-term goal] when [conflict]."
2. An arc: one line per module giving a working episode title and the decision the character
   faces, in module order. Each decision must call for that module's CLOs. Pressure should rise
   across the modules.
3. A one-sentence note on where pressure peaks.
Use the character profile exactly as written. Do not change names, numbers, or relationships.
If the faculty member described the character's long-term goal, use it.

Return: {"premise": string, "arc": [{"module": int, "title": string, "decision": string, "clos": [string]}], "peak": string}
```
:::

::: refresh
AI instructions:

```text
The faculty member's existing storyline or recurring case, if any, is given. If there is none,
draft a storyline as on the full build. If there is one, check it against this checklist: a
premise names the character, the long-term goal, and the conflict; pressure builds across
modules; every CLO drives at least one module; details stay consistent. Keep what passes. For
each gap, quote the problem and suggest a fix. Then give a premise and arc as on the full build.

Return: {"passes": boolean, "issues": [string], "premise": string, "arc": [...], "peak": string}
```
:::

Demo response (MGMT 615):

::: refresh
MGMT 615's Course Map had no storyline, so the AI drafted one.
:::

**Premise:** MGMT 615 is a story about Dana Ortiz, a newly promoted operations manager, who
struggles to find and fix the real causes of her site's slipping performance before peak season,
when her director has already decided who to blame.

**Arc:**

- Module 1, The First Bad Week: work the floor to recover the number, or step back and find out what is driving the drop.
- Module 2, The Bonus That Backfired: leave the pick-rate bonus alone, add an accuracy threshold, or propose replacing it.
- Module 3, The Conversation With Jordan: issue the warning Greg wants, coach with no record, or coach and document the agreed next steps.
- Module 4, The Handoff Nobody Owns: host Greg's team lunch, hold a joint meeting, or name a handoff owner and change the structure.
- Module 5, Telling Greg He's Wrong: send Greg's replacement plan, or ask for 30 minutes to walk him through the data.
- Module 6, Twelve Things on Dana's List: decide what to keep, what to hand off, and what to hand off with checkpoints.
- Module 7, Ending the Bonus: announce the change in writing, through her leads, or to each shift in person.
- Module 8, Proven vs. Potential: hire the proven candidate, hire Luis, or hire one and develop the other.

**Where pressure peaks:** Module 5, when Dana has to challenge her director with a week until his
deadline.

### Decide

Your final premise and arc go in these boxes. Type in any box to change it, or select **Redraft
with AI** under a box to have the AI rewrite just that part.

Under the AI's draft, select **Use this storyline** to copy it here, then edit it into your own
words. Episode titles are working titles; you can change them in step 3.2.

::: fields
- Your storyline premise (one sentence)
- Your arc, one module per line: episode title and the decision your character faces
:::

Checklist:

- The premise names the character, the goal, and the conflict.
- Pressure rises across the modules.
- Every CLO drives at least one module's decision.
- At least one module is in a different setting, so students practice applying the skills
  somewhere new.

### Checks

When you save, the tool checks that:

- the premise names the character, the goal, and the conflict;
- every CLO drives at least one module in the arc.

### Save

Planning document: Storyline premise, at the start of the Storyline section. Step 3.2 turns each
line of your arc into a full scenario.
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

::: purpose
**What you'll do:** Plan a scenario for each module: a specific moment when your character has to
make a decision that calls for that module's CLOs.

**Why it matters:** A clear scenario now saves work later. The same moment can anchor the module's
overview video, discussion, assignment, and cohort session.
:::

A scenario follows the pattern you practiced in step 2.2: something the character needs to do, and a
conflict that makes it hard. It doesn't need to be dramatic. It needs to be specific.

Look for turning points. Reasonable professionals disagree about a decision. A plan looks sound
until reality exposes a weakness. New data, or a stakeholder, forces a change in approach. A
mistake is easy to make and costly to fix.

Each scenario answers five questions:

::: flow
- Situation | What's the setting, and what was supposed to happen?
- Trigger | What went wrong or became uncertain, and what new pressure appeared?
- Stakeholders | Who is affected, and who else has something at stake?
- Decision | What has to be decided, and which options are realistically on the table?
- Outcome and learning | What changes at the end, and which idea from this module would have improved the outcome?
:::

A good scenario can't be handled well without the module's skills, and its options are ones a
professional could defend. If one option is obviously right, students learn to spot the answer
the course wants instead of making a judgment.

Work one module at a time, in order. The second half is usually where pressure peaks, and earlier
decisions can come back: in MGMT 615, the bonus Dana questions in Module 2 is the change she
announces in Module 7. A scenario that depends on an earlier decision shows students that the
skills build on each other.

One scenario can carry a whole module. Here's how MGMT 615's Module 4 scenario, "The Handoff Nobody
Owns," shows up in the steps ahead:

::: figure trace | One scenario, four uses: MGMT 615, Module 4
- Overview video (Module 6) | Opens on the handoff nobody owns and ends at Dana's decision.
- Scenario video (Module 6) | "Structural Fixes vs. Pep Talks" sets Greg's team-building lunch against naming a handoff owner.
- Main assignment (Module 4) | The team diagnosis memo: students find the cause and make the case to Greg.
- Cohort session (Module 7) | "Fix the Handoff": groups design a fix for a team they know.
:::

### See it

Here's one of the eight scenarios the MGMT 615 instructor planned, for Module 4. Its title and
premise go into the plan; the five parts guide the activities, media, and
cohort session you'll plan in Modules 4 to 7.

::: plan Scenario, Module 4
**The Handoff Nobody Owns.** Dana struggles to fix the broken handoff between her two shifts with a
structural change, when her director is pushing a team-building lunch.
:::

| Part | MGMT 615, Module 4 |
|---|---|
| Situation | The two shifts pass work to each other every afternoon, but no one owns the handoff. |
| Trigger | The shift leads now blame each other for the late orders. Greg, the director, suggests a team-building lunch. |
| Stakeholders | Both shift leads and their crews, Dana, Greg, customers. |
| Decision | Host the lunch, hold a joint meeting to air the tension, or change the structure: name a handoff owner and add a shared checklist and an overlap window. |
| Outcome and learning | A team-effectiveness framework shows the problem is unclear roles, so a lunch won't touch it. Dana has to explain to Greg why the structural fix beats his idea. |

### Draft (full build) and Review (refresh)

Work through your modules one at a time. Choose a module, then select the button below. The AI
proposes two scenarios for that module from your storyline arc (step 3.1), your character, and the
module's CLOs and topics. The first follows your arc; the second takes a different angle. Under the
one you like better, select **Use this scenario** to copy it into the boxes under Decide.

::: refresh
The AI also looks at your Course Map's existing cases and examples for each module. Where one
fits, it builds an option from it and names the case.
:::

::: module-picker
:::

::: full
AI instructions:

```text
Propose two scenario options for the given module, using the storyline arc (step 3.1), the
character profile, the CLOs, and the module's title, CLOs met, and topics. Each option puts the
character in a moment of decision that calls for that module's CLOs. Use the character profile
exactly as written. For each option give: a short episode title; a premise in the form
"[Character] struggles to [decision] when [complication]."; the CLOs it supports; situation;
trigger; stakeholders; decision with 2 or 3 realistic options a professional could defend;
outcome and learning, naming the module concept that improves the outcome. Keep each element to
one or two sentences. The first option should follow the arc; the second can depart from it. For
modules after the first, where it fits, connect a scenario to a decision the character made in an
earlier module, and say which one.

Return: {"module": int, "options": [{"title": string, "premise": string, "clos": [string], "situation": string, "trigger": string, "stakeholders": string, "decision": string, "outcome": string}]}
```
:::

::: refresh
AI instructions:

```text
The faculty member's existing scenario for the given module is given, if any, along with the
module's current activities and materials. For an existing scenario, check: the decision calls for
that module's CLOs; the options are ones a professional could defend; the stakes are visible;
character details match the profile. Keep what passes and suggest fixes for the rest. If there is
no scenario, propose two options as on the full build. Where an existing case or example fits,
build an option from it and name the case.

Return: {"module": int, "existing": {"passes": boolean, "issues": [string]} | null, "options": [...]}
```
:::

Demo response (MGMT 615):

::: module-options
- 1 | refresh | Your Course Map's existing case, Maria's First Ninety Days, covers the same moment at another company. Keep it as a contrast: students compare Maria's first quarter with Dana's first bad week.
:::

### Decide

Your final scenario for each module goes in these boxes. Type in any box to change it, or select
**Redraft with AI** under a box to have the AI rewrite just that part. To work on another module,
choose it above; what you've typed is kept.

::: module-fields
:::

Checklist (for each scenario):

- The decision can't be made well without this module's skills.
- There are two or three options a professional could defend.
- The stakes are visible.
- Names, numbers, and relationships match your character profile.

### Checks

When you save each scenario, the tool checks that:

- the decision calls for the module's CLOs;
- there are two or three defensible options;
- character details match your profile.

When all your scenarios are saved, a storyline check looks across them: pressure rises, every
CLO drives a decision, details stay consistent, no two scenarios turn on the same decision, and at
least one uses a different setting. Flags appear on the modules involved.

In MGMT 615, the storyline check passed four checks and flagged one: every scenario takes place at
Dana's site. The instructor kept it with a note: "Module 5 uses data from a sister site, and the
existing cases in Modules 1, 2, 4, and 7 give students other companies to compare."

AI instructions:

```text
Check the saved scenarios as one storyline against the character profile and the CLOs:
1. Pressure rises across the modules.
2. Every CLO drives at least one scenario's decision.
3. Names, numbers, and relationships match the profile and each other.
4. No two scenarios turn on the same decision.
5. At least one scenario uses a different setting.
Give one result per check: pass, or issue with the module(s) involved and a one-sentence fix.

Return: {"checks": [{"check": string, "result": "pass" | "issue", "modules": [int], "detail": string | null}]}
```

### Save

Planning document: the Scenario row in Tables 1 and 2 (episode title and premise).
Project file: `modules[].scenario` (all five elements, title, premise, and CLOs); `alignment.m3`.

> Review note: the MGMT 615 scenarios now use the revised CLO numbers from step 1.3. Module 8
> maps to CLO 6 (hiring) instead of CLO 4. Module 2's alternative ("Luis Checks Out"), Module 4's
> ("Two Shifts, Two Rulebooks") and Module 7's ("The Overlap Window") are new, written to give the
> AI two options in every module. The other alternatives are the side plots from
> `src:example-mgmt615-character`. Demo data: `demo/mgmt615-scenarios.json` gives each module's
> `chosen` option in full and the `alternative` as title and premise only.

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
