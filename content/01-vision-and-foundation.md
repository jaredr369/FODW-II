# Module 1. Creating Vision and Foundation

Module id: `m1`
Steps: 4
ID check-in: live review of this module's sections, at the end of the week or sooner

Faculty complete: learners, catalog description, program outcomes, course vision, CLOs, module
titles and topics.

Refresh checks for this module: CLOs are measurable, with one verb each, and line up with the
catalog description and program outcomes; every CLO appears in at least one module; topics are
current.

Sources: `src:reading-m1-setting-the-foundation`, `src:guide-course-alignment`,
`src:guide-learning-objectives`, `src:assignment-m1-building-the-framework`,
`src:assignment-m1-redesign-and-refine`, `src:template-planning-doc`,
`src:example-mgmt615-course-map`

## Refresh reflection

> App note: shown once, in the refresh track only, before step 1.1. The answers go to the AI in
> every Review step of this module.

Think about the last time you taught this course. Answer whichever of these questions apply.
Short notes are fine. The AI uses your answers when it reviews each section in this module.

1. Which course objectives did students struggle to meet? What did you see in their work?
2. Were there weeks that felt overloaded or thin, or topics that came too early or too late?
3. Is there a topic you want to add, cut or update?
4. What worked well enough that you want to keep it as it is?

AI instructions (added to each Review step in this module):

```text
The faculty member's reflection on the last time they taught the course is given. When a
problem you find matches something in the reflection, say so in the issue and connect the
revision to it. Do not raise problems only because the reflection mentions them; check them
against the checklist first.
```

Demo answers (MGMT 615):

1. "The feedback script in Module 3 was the weakest work. Students wrote what they'd tell the
   employee and stopped there. Few said what they expected to change."
2. "Module 4 felt thin. We spent a lot of time on team stages and never got to the handoff
   problems students actually face."
3. "Hiring comes up every term in Module 8 and students want more of it."
4. "The diagnosis-first approach. Students tell me it's what they use most at work."

> App note: each answer connects to the demo review: the CLO 2 revision answers the first, the
> Module 4 topic change the second, the new hiring CLO the third, and the vision revision keeps
> the diagnosis-first approach.

Project file: `reflection.m1`.

---

## 1.1 Learners, catalog and program outcomes

Time: about 20 minutes
Pattern: interview, then draft

### Learn

Flex Online courses are planned backward: decide what students should be able to do at the end,
then how you'll see it, then what they'll read and watch (Wiggins & McTighe, 2005). That's the
order of this workshop. Module 1 sets the end point.

Start with who the students are. They're working professionals who connect new ideas to their
own experience, want to know why something matters before they invest time, and want to use it
soon (Knowles, Holton, & Swanson, 2015). Every AI draft from here on uses the learner profile, a
short description of who takes your course, that you write in this step.

Your catalog description is the course's public promise, so your course vision and course-level
objectives (CLOs), which you'll write in steps 1.2 and 1.3, stay within it. Paste the official
text from the TAMU course catalog (catalog.tamu.edu); the AI won't write or change it.

The AI then breaks the description into a list of commitments: each separate thing the catalog
promises students will learn to do. Check that the list is complete and accurate. It matters
later: when you write your CLOs in step 1.3, the tool checks them against this list and flags any
promise your course doesn't cover yet.

Program outcomes describe what students can do after the whole degree; mark the two to four this
course supports. Your ID can find them if you don't have them. Before you start Module 2, confirm
your vision and CLOs with your program director, since the storyline you'll build in Modules 2
and 3 builds on them.

### See it

MGMT 615's students are new or soon-to-be managers, promoted for being good at their own jobs.
Its catalog description makes six commitments, from diagnosing underperformance to hiring well.
Later checks hold the CLOs to that list, which is how the review of the existing course found
that no CLO covered hiring.

### Draft (full build)

The AI asks you four questions, then drafts a learner profile:

1. What jobs do most students hold while they take the course?
2. What do they already know about the subject when they start?
3. What will they do differently at work after the course?
4. Anything about their schedules or situations the course should plan around?

Then you paste the catalog description and program outcomes.

AI instructions:

```text
1. Write a learner profile of 3 or 4 sentences from the faculty member's answers, using only
   what they said, and name one design implication from adult learning (self-directed,
   experience-rich, goal-oriented, practically motivated).
2. List each distinct thing the catalog description commits the course to, in the catalog's own
   words where possible. Do not rewrite the catalog description.
3. For each program outcome, say whether this course likely supports it, with a reason under 20
   words based on the catalog description.

Return: {"profile": string, "implication": string, "commitments": [string], "programOutcomes": [{"outcome": string, "supports": boolean, "reason": string}]}
```

Demo response (MGMT 615):

```json
{
  "profile": "Students are working professionals in a first management role or about to step into one, most promoted after strong work as individual contributors. They arrive with years of workplace experience and plenty of stories about good and bad managers, but little formal training in managing people. They take the course to handle the conversations and decisions their new role puts in front of them. Most work full time and study in the evenings and on weekends.",
  "implication": "Ask students to bring a current problem from their own team into each module's main assignment, so the work pays off at their job the same week.",
  "commitments": ["Diagnose why employees and teams underperform", "Deliver feedback that changes behavior", "Build and repair team dynamics", "Delegate and make decision-rights calls under pressure", "Lead a team through change", "Hire well"],
  "programOutcomes": [
    {"outcome": "PLO 1: Lead individuals and teams to meet organizational goals.", "supports": true, "reason": "The whole course is about managing people toward performance targets."},
    {"outcome": "PLO 2: Analyze business problems using evidence and established frameworks.", "supports": true, "reason": "Diagnosing underperformance with motivation and team frameworks is central."},
    {"outcome": "PLO 3: Communicate decisions clearly to varied audiences.", "supports": true, "reason": "Feedback, change messages and delegation calls are communication tasks."},
    {"outcome": "PLO 4: Apply quantitative methods to financial decisions.", "supports": false, "reason": "The catalog description does not mention financial analysis."}
  ]
}
```


### Review (refresh)

You'll see the learner description, catalog description and program outcomes found in your
Course Map. The AI drafts any missing part from scratch. It also lists the catalog's commitments
and checks that your learner description names students' roles, what they bring and what they
need.

Demo response (MGMT 615): learners and program outcomes are missing, so those run as the full
build; the catalog is found and its commitments match the list above. The app asks the faculty
member to confirm the catalog text is the current official version.

### Decide

Checklist:

- The profile describes the students who actually take your course.
- The catalog text is the current official version.
- The commitment list includes every promise in the catalog description, and nothing extra.
- You've marked the program outcomes this course supports.
- You've planned a meeting with your program director before Module 2.

### Checks

None on save. The commitments and program outcomes feed the checks in steps 1.2 to 1.4.

### Save

Planning document: Catalog Course Description; Program-Level Outcomes (supported only);
Learners (new paragraph, after Course Vision).
Project file: `learners.profile`, `catalog.text`, `catalog.commitments`, `programOutcomes`,
`programDirectorReview.status`.

### Go deeper (optional)

- `src:reading-m1-setting-the-foundation`: the principles behind Flex Online design.
- `src:ext-wiggins-mctighe-2005`, `src:ext-knowles-2015`, `src:ext-cast-2018`

---

## 1.2 Course vision

Time: about 15 minutes
Pattern: interview, then draft

### Learn

Your vision says what students will be able to do, and who they'll become, because they took
your course. Try this: a student runs into you a year after the course. What do you hope they
tell you they now do differently at work? That answer is the core of your vision.

Write 3 or 4 sentences about what students do in their professional setting, within the scope
of your catalog description, and say what sets the course apart. A vision drives every later choice: each topic,
activity and reading has to help students get there.

### See it

MGMT 615: "MGMT 615 turns people who are good at their jobs into people who are good at running
a team. Every module asks students to work out what is actually wrong before they choose a fix,
and to defend that call to peers in a live cohort session (a scheduled live class meeting on Zoom;
you'll plan these in Module 7). Students leave with work they can use
on the job: a feedback script, a delegation memo, a change announcement and a structured
interview scorecard. They finish ready to manage a larger team and to explain the reasoning
behind each call."

### Draft (full build)

The AI asks you one question, "What do you hope a student tells you a year after the course?",
then drafts two versions with different emphasis. Pick one, combine them or write your own.

AI instructions:

```text
Draft two course visions of 3 or 4 sentences each from the faculty member's answer, the learner
profile and the catalog commitments. Describe what students will do in their professional
setting, stay inside the catalog commitments, and say what sets the course apart. Make the two
differ in emphasis: one on skills, one on the professional the student becomes.

Return: {"versions": [string, string]}
```

Demo response (MGMT 615), from the answer "That they stopped fixing everything themselves, figured
out what was really wrong with their team before reacting, and had the conversation they were
avoiding":

```json
{
  "versions": [
    "MGMT 615 prepares new managers to figure out why a person or team is struggling before they act. Students practice the work that follows a good diagnosis, from feedback and delegation to change announcements and hiring, and defend each call to peers in live cohort sessions. Every major assignment produces something they can use with their own team. Students finish ready to stop fixing problems themselves and start building a team that can.",
    "Students arrive at MGMT 615 good at their own jobs and leave able to run a team. Module after module, the course asks them to look past the obvious explanation for a performance problem and find the real cause. They rehearse the hard conversations in scripts and cohort sessions, so they're ready to have them at work. A year later they should be the manager their team trusts to diagnose before deciding."
  ]
}
```

### Review (refresh)

You'll see your current vision with flags from the checks below and one suggested revision that
keeps your language.

Demo response (MGMT 615): two flags. "Seven sentences; the planning document asks for 3 or 4."
And "The first two sentences describe the program ('sits at the center of the Flex Online
people-management sequence'). A vision should describe what students will do." Suggested
revision: the four-sentence vision under See it. Demo change note: "Cut to four sentences.
Removed the program description; kept the diagnosis-first approach and the deliverables."

### Decide

Checklist:

- 3 or 4 sentences.
- Describes what students do at work.
- Fits the catalog description.
- You'd be glad to hear a former student describe the course this way.

### Checks

On save: sentence count (3 or 4); every claim fits a catalog commitment; it describes student
actions instead of course coverage.

### Save

Planning document: Course Vision.
Project file: `vision.text`; in refresh, `vision.original`, `vision.changeNote`.

---

## 1.3 Course-Level Objectives (CLOs)

Time: about 25 minutes
Pattern: spot the problem, then pick and combine (full build) or edit in place (refresh)

### Learn

CLOs say what students will be able to do by the end of the course, in a way you can observe and
grade. Everything later traces back to them. Write 3 to 6.

To pitch them at the right level, use Bloom's taxonomy, a widely used framework that sorts
learning by how much thinking it asks of students (Anderson & Krathwohl, 2001). It has six
levels, from least to most demanding:

1. **Remember:** recall facts and terms.
2. **Understand:** explain ideas in your own words.
3. **Apply:** use a method or idea in a new situation.
4. **Analyze:** break a situation into parts and see how they relate.
5. **Evaluate:** judge options against criteria and defend a choice.
6. **Create:** put ideas together into something new, such as a plan, design or proposal.

Start each CLO with one action verb at the apply level or higher, mostly analyze, evaluate or
create. Your students are experienced professionals; they need to use and judge ideas, not just
recall them. Avoid verbs like "understand" or "know." You can't see them happen, so you can't
grade them. Describe something within the student's control.

| Level | Example verbs |
|---|---|
| Apply | apply, implement, solve, calculate |
| Analyze | analyze, diagnose, compare, differentiate |
| Evaluate | evaluate, assess, justify, defend |
| Create | design, develop, construct, draft |

Each CLO should also suggest a decision someone in your students' role would face. In Module 2
you'll create a character, someone in your students' role, whose story runs through the course.
These decisions become that character's story.

**Spot the problem.** Before drafting, you'll see one weak objective. In a sentence, say what
you would change, and why. The AI then confirms what you caught and adds anything you missed.

> Example: "Students will understand how to give feedback that changes an employee's behavior."

> App note: expected points: "understand" can't be observed; "changes an employee's behavior"
> depends on the employee, which the student can't control. A stronger version: "Design a
> feedback conversation that targets a specific behavior and states the change expected." The
> AI confirms what the faculty member caught and adds what they missed, in two sentences.

### See it

MGMT 615's first CLO began as "Apply core theories of motivation and performance to diagnose why
an employee or team is underperforming." Two verbs. The refresh kept the one students are graded
on: "Diagnose why an employee or team is underperforming using core theories of motivation and
performance." It gives MGMT 615's character, Dana Ortiz, a newly promoted manager you'll meet in
Module 2, her first decision: is the shift lead the problem?

### Draft (full build)

AI instructions:

```text
Draft 4 to 6 CLOs from the vision, the catalog commitments, the supported program outcomes and
the learner profile. One measurable verb per CLO, Bloom's apply or higher, mostly analyze,
evaluate or create; describe what the student does, within their control; together cover every
catalog commitment. For each give its verb, level, the commitments and program outcomes it
covers, and one decision a professional in the students' role would face.

Return: {"clos": [{"text": string, "verb": string, "level": string, "commitments": [string], "programOutcomes": [string], "decision": string}]}
```

Demo response (MGMT 615, if run as a full build): the six revised CLOs listed under Review.

### Review (refresh)

Each of your current CLOs shows Keep or a suggested revision, with flags.

AI instructions:

```text
Check each current CLO: exactly one measurable verb; Bloom's apply or higher; within the
student's control; fits the catalog. Keep the wording wherever it passes. For each problem,
quote the words that cause it and suggest one revision. If a catalog commitment is uncovered,
propose one new CLO for it. If there are more than 6, suggest which to merge.

Return: {"clos": [{"original": string, "action": "keep" | "revise", "issues": [string], "revision": string | null}], "newClos": [string]}
```

Demo response (MGMT 615):

| Current | Action | Revision | Change note |
|---|---|---|---|
| CLO 1: Apply core theories of motivation and performance to diagnose why an employee or team is underperforming. | Revise | Diagnose why an employee or team is underperforming using core theories of motivation and performance. | Dropped "apply" so the CLO has one verb. |
| CLO 2: Design a feedback or coaching conversation that changes an employee's behavior, not just documents it. | Revise | Design a feedback or coaching conversation that targets a specific behavior and states the change expected. | Now graded on the conversation the student designs. Matches the reflection: scripts never said what should change. |
| CLO 3: Evaluate team dynamics and organizational context to select a management intervention appropriate to the actual problem. | Keep | | Kept. |
| CLO 4: Make a delegation or decision-rights call and justify the trade-offs involved. | Revise | Justify a delegation or decision-rights call, including the trade-offs involved. | Dropped "make" so the CLO grades the justification. |
| CLO 5: Communicate a management decision in language a direct report can act on immediately. | Revise | Draft a management decision message that states the decision and the next steps a direct report must take. | Changed to a written message with stated next steps so it can be graded. |
| (new) CLO 6 | Add | Evaluate candidates for a role using a structured interview scorecard. | The catalog promises hiring and Module 8 teaches it. Matches the reflection on Module 8. |

### Decide

New course: pick from the AI's drafts, then edit, reorder, remove or add. Updating a course: for
each current CLO, keep it, accept the AI's suggested revision, edit it or rewrite it; accept,
edit or reject each new CLO the AI suggests.

Checklist:

- 3 to 6 CLOs, one measurable verb each, at apply or above.
- Each describes what the student does.
- Each suggests a decision someone in your students' role would face.

### Checks

On save: one verb per CLO; level apply or above; count 3 to 6; every catalog commitment covered
by a CLO; every CLO supports at least one supported program outcome. Demo: all pass after the
revisions; before them, the commitment check flags "Hire well: no CLO covers it."

### Save

Planning document: Course-Level Objectives (CLOs).
Project file: `clos` (text, verb, level, commitments, programOutcomes, decision); in refresh,
`clos[].original`, `clos[].changeNote`.

### Go deeper (optional)

- `src:guide-learning-objectives`: verb tables and the case for higher-order objectives.
- `src:ext-anderson-krathwohl-2001`

---

## 1.4 Module titles and topics

Time: about 25 minutes
Pattern: pick and combine (full build) or edit in place (refresh)

### Learn

Lay out the weekly modules; the planning document has room for eight. Each gets a title a
student would understand on day one, one CLO the module mainly works toward and at most one more
it also supports, and three to five topics. Start from the CLOs: list what students need to know or practice to meet each
one, then cut anything whose removal wouldn't stop anyone from meeting a CLO.

Order matters. In Module 3 each module becomes a scenario, a realistic situation your character
faces that week, so order
the modules the way the decisions would come up at work: diagnosis before treatment, one person
before the whole team.

### See it

| Module | Title | CLOs met |
|---|---|---|
| 1 | What Managers Actually Do | CLO 1, CLO 5 |
| 2 | Motivating People | CLO 1, CLO 5 |
| 3 | Performance Management and Feedback | CLO 2, CLO 5 |
| 4 | Building and Leading Teams | CLO 3, CLO 1 |
| 5 | Managing Conflict and Difficult Conversations | CLO 3, CLO 2 |
| 6 | Delegation and Decision-Making | CLO 4, CLO 5 |
| 7 | Leading Through Change | CLO 5, CLO 3 |
| 8 | Hiring and Building Your Team | CLO 6, CLO 1 |

### Draft (full build)

AI instructions:

```text
Draft a module sequence from the CLOs, catalog commitments and learner profile, using the number
of modules the faculty member chose (default 8). For each module: a plain title, one primary CLO
and at most one supporting CLO, and 3 to 5 topics. Every CLO appears at least once. Order the
modules the way the decisions would come up for a professional in the students' role, with a
one-sentence reason.

Return: {"modules": [{"number": int, "title": string, "closMet": [string], "topics": [string]}], "orderReason": string}
```

Demo response (MGMT 615, if run as a full build): the eight modules above with the topics from
the MGMT 615 course map, including the Module 4 change below.

### Review (refresh)

Each module shows Keep or a suggested revision, with flags. CLO numbers are updated to match
step 1.3.

Demo response (MGMT 615):

- Modules 1, 2, 3, 5, 6 and 7: keep.
- Module 4: revise. The topic "Designing team assignments that are accessible to every learner"
  is a note about designing the course; students wouldn't study it. Replacement: "Role clarity
  and ownership of handoffs." Matches the reflection that Module 4 never reached the handoff
  problems.
- Module 8: CLOs met change from "CLO 4, CLO 1" to "CLO 6, CLO 1".

### Decide

You'll see a table with one column per module. Edit titles, CLOs met and topics, and drag to
reorder. Updating a course: for each module, keep it, accept the AI's suggested revision, edit it
or rewrite it.

Checklist:

- Each module has one or two CLOs.
- Titles make sense to a student on day one.
- The order follows the way the decisions would come up at work.

### Checks

On save: every CLO appears in at least one module; each topic serves a CLO its module lists;
topics are content for students; CLOs appearing in only one module, or in more than five, are
noted. Demo flag (MGMT 615): "CLO 4 and CLO 6 each appear in one module." Demo kept note:
"Delegation and hiring are each a focused skill, practiced and assessed in one module."

### Save

Planning document: Module Titles, CLOs met and Module Topics rows in Tables 1 and 2 (see
`export.md`).
Project file: `modules[].title`, `modules[].closMet`, `modules[].topics`; in refresh,
`.original` and `.changeNote`. Other columns from an uploaded course map stay in
`source.sections` for later modules.

### Go deeper (optional)

- `src:guide-course-alignment`

---

## Check-in prep

> App note: shown after step 1.4.

AI instructions:

```text
From this module's saved sections, change notes and kept flags, list what's new or changed since
the last check-in, the flags kept with their notes, and two questions worth raising with the ID.
Keep it under 150 words.

Return: {"changed": [string], "keptFlags": [string], "questions": [string, string]}
```

Demo response (MGMT 615):

```json
{
  "changed": ["Learners, program outcomes: new", "Vision: cut to four sentences", "CLOs: four revised, CLO 3 kept, CLO 6 added for hiring", "Modules: Module 4 topic replaced, Module 8 mapped to CLO 6"],
  "keptFlags": ["CLO 4 and CLO 6 each appear in one module: focused skills, practiced and assessed in one module"],
  "questions": ["Does adding a sixth CLO for hiring need program director approval?", "Is one module enough practice for delegation (CLO 4)?"]
}
```

Project file: `checkins.prep.m1`.
