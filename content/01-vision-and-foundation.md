# Module 1. Creating Vision and Foundation

Module id: `m1`
Steps: 6
ID check-in: live review of this module's sections, at the end of the week or sooner

Faculty complete: catalog description, program outcomes, course vision, CLOs, module titles and
topics.

Refresh checks for this module: CLOs are measurable, with one verb each, and line up with the
catalog description and program outcomes; every CLO appears in at least one module; topics are
current.

Sources: `src:reading-m1-setting-the-foundation`, `src:guide-course-alignment`,
`src:guide-learning-objectives`, `src:assignment-m1-building-the-framework`,
`src:assignment-m1-redesign-and-refine`, `src:template-planning-doc`,
`src:example-mgmt615-course-map`

## Refresh reflection

Shown once, in the refresh track only, before step 1.1. The answers go to the AI in every
Review step of this module, so a suggested revision can point to what the faculty member saw
in class.

Prompt shown: "Think about the last time you taught this course. Answer whichever of these
apply. Short notes are fine."

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

Each answer connects to the demo review. The CLO 2 revision ("states the change expected")
responds to the weak feedback scripts. The Module 4 topic change responds to the thin week. The
new hiring CLO responds to the Module 8 note, and the vision revision keeps the diagnosis-first
approach.

Project file: `reflection.m1`.

> Review note: reflection appears only in modules where an existing course already has
> something to look back on. Proposed: Module 1 (objectives and modules), Module 4 (activities
> and assessments), Module 5 (materials), Module 6 (existing videos), Module 7 (cohort
> sessions) and Module 8 (communication and feedback). Modules 2 and 3 introduce new work
> (character, storyline, scenarios) and have none. Where a module mixes old and new, such as
> AI in Module 4 or XR stages in Modules 4 and 7, the reflection asks only about the parts the
> course already had.

---

## 1.1 The principles behind the plan

Time: about 20 minutes

### Learn

Before you plan what students will do, it helps to know the principles every Flex Online course
is built on. You will apply each of them in later modules. For now you only need to know what
they mean.

**Adult learning.** Your students are working professionals, many of them managers or senior
specialists. Malcolm Knowles described four traits of adult learners that matter for course
design (Knowles, Holton, & Swanson, 2015). They want some control over how they learn. They
connect new ideas to experience, so their experience is material you can use. They want to know
why something matters before they put time into it. And they want to use what they learn soon,
usually on a problem already on their desk.

**Backward Design.** Wiggins and McTighe (2005) start with the end of the course. First decide
what students should be able to do when they finish. Then decide what evidence will show they
can do it. Only then plan the instruction and materials. In this tool that order is literal: you
write CLOs in Module 1, activities in Module 4 and materials in Module 5.

**Active learning.** Students learn more when they work with the material, by analyzing a case,
arguing a position or producing something, than when they only read or watch (Freeman et al.,
2014). For professionals the effect is stronger when the task looks like their work.

**Universal Design for Learning (UDL).** Build flexibility into the course from the start, so
fewer students need an exception later. Offer content in more than one form, give students more
than one way to engage, and let them show what they learned in more than one way (CAST, 2018).

**Accessibility.** Every student, whatever their ability or circumstances, should be able to use
every part of the course. Captions, readable documents and accessible slides are easier to plan
now than to fix during the build. Module 5 and Module 6 cover the details.

### See it

MGMT 615 students are new or soon-to-be managers. Most were promoted because they were good at
their own jobs. Each module gives them a management problem to diagnose before they choose a
fix, which draws on what they have already seen at work. The Module 3 deliverable is a feedback
script for a real conversation, something a student could use the following Monday.

### Draft (full build)

The faculty member answers four questions about their learners. The AI turns the answers into a
short learner profile that later steps use as context.

Questions shown:

1. What jobs do most students hold while they take the course?
2. What do they already know about the subject when they start?
3. What will they do differently at work after the course?
4. Is there anything about their schedules or situations the course should plan around?

AI instructions:

```text
Write a learner profile of 3 or 4 sentences from the faculty member's answers. Describe who the
students are, what they bring, and what they need from the course. Use only what the answers
say. Then name one design implication for this course, based on the adult learning traits
(self-directed, experience-rich, goal-oriented, practically motivated).

Return: {"profile": string, "implication": string}
```

Demo response (MGMT 615):

```json
{
  "profile": "Students are working professionals in a first management role or about to step into one, most promoted after strong work as individual contributors. They arrive with years of workplace experience and plenty of stories about good and bad managers, but little formal training in managing people. They take the course to handle the conversations and decisions their new role puts in front of them, often while managing a team for the first time. Most work full time and study in the evenings and on weekends.",
  "implication": "Ask students to bring a current problem from their own team into each module's main assignment. Their experience becomes course material, and the work pays off at their job the same week."
}
```

### Review (refresh)

If the uploaded document describes the learners, the app shows that text and runs the
instructions below. If not, this step runs as a full build.

AI instructions:

```text
The faculty member's current description of their learners is given. Check it against this
checklist:
- Names the jobs or roles students hold.
- Says what students already know when they start.
- Says what students need to do at work after the course.
If it passes, suggest keeping it. If not, name what is missing and suggest a revised profile of
3 or 4 sentences using only what the document says, and mark anything you could not find.

Return: {"passes": boolean, "issues": [string], "revision": string | null}
```

Demo response (MGMT 615): the course map has no learner description, so this step runs as a
full build and plays the full-build demo response above.

### Decide

The faculty member edits the profile.

Checklist:

- It describes the students who actually take your course.
- It says what they bring and what they need.

### Save

Planning document: a new "Learners" paragraph directly under Course Vision. The template has
no learner section, so the export adds it.
Project file: `learners.profile`. Every later AI step receives it as context.

### Go deeper (optional)

- `src:ext-knowles-2015`
- `src:ext-wiggins-mctighe-2005`
- `src:ext-cast-2018`
- `src:guide-course-development-process`

---

## 1.2 Catalog description and program outcomes

Time: about 20 minutes

### Learn

Your course already has a boundary: its catalog description. The catalog is the public promise
of what the course covers, and your vision and CLOs have to stay inside it. Paste the official
text. The AI will not write or change a catalog description, because changes go through the
university's curriculum process.

Program-level outcomes describe what students can do when they finish the whole degree. Your
CLOs should show how this course moves students toward some of them. You do not need to touch
every program outcome, and most courses address two to four. Your ID can find your program's
outcomes if you do not have them.

Before you start Module 2, meet with your program director to confirm that your vision and CLOs
fit the catalog description. Your character and scenarios build on your CLOs, so it is easier
to change them now. Programs ask for this check because a course that drifts from its catalog
description can cause problems at program review.

In this step the AI reads your catalog description and lists each thing it commits the course
to. Later steps check your vision, CLOs and modules against that list.

### See it

The MGMT 615 catalog description makes six commitments: diagnosing why employees and teams
underperform, giving feedback that changes behavior, building and repairing team dynamics,
delegating and making decision-rights calls under pressure, leading a team through change, and
hiring well. In step 1.4 that list showed a gap: no CLO covered hiring, even though Module 8 was
about it.

### Draft (full build)

The faculty member pastes the catalog description and the program outcomes. The AI lists the
catalog commitments and suggests which program outcomes the course most likely supports.

AI instructions:

```text
You are given a course catalog description and the program's outcomes.
1. List each distinct thing the catalog description commits the course to cover or teach,
   using the catalog's own words where possible.
2. For each program outcome, say whether this course likely supports it (yes or no), with a
   reason under 20 words based on the catalog description.
Do not rewrite the catalog description.

Return: {"commitments": [string], "programOutcomes": [{"outcome": string, "supports": boolean, "reason": string}]}
```

Demo response (MGMT 615):

```json
{
  "commitments": [
    "Diagnose why employees and teams underperform",
    "Deliver feedback that changes behavior",
    "Build and repair team dynamics",
    "Delegate and make decision-rights calls under pressure",
    "Lead a team through change",
    "Hire well"
  ],
  "programOutcomes": [
    {"outcome": "PLO 1: Lead individuals and teams to meet organizational goals.", "supports": true, "reason": "The whole course is about managing people toward performance targets."},
    {"outcome": "PLO 2: Analyze business problems using evidence and established frameworks.", "supports": true, "reason": "Diagnosing underperformance with motivation and team frameworks is central."},
    {"outcome": "PLO 3: Communicate decisions clearly to varied audiences.", "supports": true, "reason": "Feedback, change messages and delegation calls are communication tasks."},
    {"outcome": "PLO 4: Apply quantitative methods to financial decisions.", "supports": false, "reason": "The catalog description does not mention financial analysis."}
  ]
}
```

> Review note: MGMT 615 has no program outcomes in the course map. The four PLOs above are
> invented for the demo. Please approve them or give me others.

### Review (refresh)

AI instructions:

```text
The faculty member's current catalog description and program outcomes are given, if found.
- If the catalog description is present, list its commitments as in the full build. Remind
  the faculty member to confirm it matches the current official catalog.
- If program outcomes are missing, say so; the app will run the full build for them.
Do not suggest changes to the catalog description.

Return: {"commitments": [string], "catalogFound": boolean, "programOutcomesFound": boolean, "programOutcomes": [...]}
```

Demo response (MGMT 615): the catalog description is found and the commitments match the
full-build demo response. Program outcomes are missing, so the app asks the faculty member to
paste them, then plays the full-build response for the program outcome list.

### Decide

The faculty member confirms the catalog text is current, edits the commitment list if the AI
split or merged something wrongly, and checks the program outcomes the course supports.

Checklist:

- The catalog description is the current official text.
- The commitment list covers everything the catalog promises.
- You have marked the program outcomes this course supports.
- You have planned a meeting with your program director before Module 2.

Refresh change note: required only if the faculty member changes the commitment list or the
program outcomes. The catalog description itself is kept as is.

### Save

Planning document: TAMU Catalog Course Description; Program-Level Outcomes (only those marked
as supported).
Project file: `catalog.text`, `catalog.commitments`, `programOutcomes`,
`programDirectorReview.status`.

> Review note: `src:template-planning-doc` labels these sections "Covered in FODW Module 2", and the
> Program-Level Outcomes placeholder repeats the catalog description placeholder. The export
> will use "Module 1" and a correct placeholder.

---

## 1.3 Course vision

Time: about 20 minutes

### Learn

Your course vision is a short statement of what students will be able to do, and who they will
become, because they took your course. It comes before the CLOs because it tells you what the
CLOs are for.

Try this. A student finishes your course and runs into you a year later. What do you hope they
tell you they now do differently at work? For professionals, the answer is usually about a
problem in their own organization that they handled better. That answer is the core of your
vision.

A common alternative is to start with a list of everything the course should cover. Courses
built that way tend to feel thorough but aimless, because nothing tells students what the
coverage is for. Starting from the vision gives every later choice a test: does this topic,
activity or reading help students get there?

A good vision for a Flex Online course:

- runs 3 or 4 sentences
- describes what students will do, in their professional setting
- stays inside the catalog description
- says what sets this course apart from others in the program

### See it

MGMT 615's vision, shortened in the refresh: "MGMT 615 turns people who are good at their jobs
into people who are good at running a team. Every module asks students to work out what is
actually wrong before they choose a fix, and to defend that call to peers in a live cohort
session. Students leave with work they can use on the job: a feedback script, a delegation memo,
a change announcement and a structured interview scorecard. They finish ready to manage a larger
team and to explain the reasoning behind each call."

### Draft (full build)

The faculty member answers the "year later" question in a few sentences. The AI drafts two
versions of a vision.

AI instructions:

```text
Draft two versions of a course vision, each 3 or 4 sentences, from the faculty member's answer
to "What do you hope a student tells you a year after the course?", the learner profile and the
catalog commitments. Describe what students will do in their professional setting. Stay inside
the catalog commitments. Make the two versions differ in emphasis, for example one centered on
the skills and one on the kind of professional the student becomes.

Return: {"versions": [string, string]}
```

Demo response (MGMT 615):

Faculty answer: "That they stopped fixing everything themselves. That they figured out what was
really wrong with their team before reacting, and that they had the conversation they were
avoiding."

```json
{
  "versions": [
    "MGMT 615 prepares new managers to figure out why a person or team is struggling before they act. Students practice the work that follows a good diagnosis, from feedback and delegation to change announcements and hiring, and defend each call to peers in live cohort sessions. Every major assignment produces something they can use with their own team, such as a feedback script or a delegation memo. Students finish ready to stop fixing problems themselves and start building a team that can.",
    "Students arrive at MGMT 615 good at their own jobs and leave able to run a team. The course asks them, module after module, to look past the obvious explanation for a performance problem and find the real cause. They have the hard conversations in rehearsal first, in scripts and in cohort sessions, so they are ready to have them at work. A year later they should be the manager their team trusts to diagnose before deciding."
  ]
}
```

### Review (refresh)

AI instructions:

```text
The faculty member's current course vision is given. Check it against this checklist:
- 3 or 4 sentences.
- Describes what students will do, in their professional setting.
- Stays inside the catalog commitments.
- Says what sets the course apart.
If it passes, suggest keeping it. Otherwise list each issue, quoting the words that cause it,
and suggest one revision that keeps the faculty member's own language where possible.

Return: {"passes": boolean, "issues": [string], "revision": string | null}
```

Demo response (MGMT 615):

```json
{
  "passes": false,
  "issues": [
    "Seven sentences, longer than the 3 or 4 the planning document asks for.",
    "The first two sentences, \"sits at the center of the Flex Online people-management sequence\" and \"Other Flex Online courses build a student's functional expertise\", describe the program. A vision should describe what students will do."
  ],
  "revision": "MGMT 615 turns people who are good at their jobs into people who are good at running a team. Every module asks students to work out what is actually wrong before they choose a fix, and to defend that call to peers in a live cohort session. Students leave with work they can use on the job: a feedback script, a delegation memo, a change announcement and a structured interview scorecard. They finish ready to manage a larger team and to explain the reasoning behind each call."
}
```

### Decide

Full build: the faculty member picks one version, combines them, or writes their own, then
edits. Refresh: keep, accept the revision, edit it, or rewrite.

Checklist:

- 3 or 4 sentences.
- Describes what students do at work.
- Fits the catalog description.
- You would be glad to hear a former student describe the course this way.

Refresh change note, demo example: "Cut from seven sentences to four. Removed the program
description and kept the diagnosis-first approach and the list of deliverables."

### Save

Planning document: Course Vision.
Project file: `vision.text`; in refresh, `vision.original` and `vision.changeNote`.

---

## 1.4 Course-Level Objectives (CLOs)

Time: about 30 minutes

### Learn

CLOs are specific, measurable statements of what students will be able to do by the end of the
course. In Backward Design they come first: every module, activity and reading later has to trace
back to at least one CLO.

Write between 3 and 6. Each one starts with a single action verb that names something you can
see a student do. "Understand", "appreciate" and "be familiar with" fail that test, because you
cannot observe them. A useful pattern is: students will be able to [verb] [what] by [how you will
see it]. You can state "students will be able to" once and start each CLO with the verb.

Use one verb per CLO. "Apply theories to diagnose a problem" has two verbs, and an assignment
has to decide which one it is grading. Pick the one that names what students actually produce.

Bloom's Taxonomy sorts thinking into six levels: remember, understand, apply, analyze, evaluate
and create (Anderson & Krathwohl, 2001). Your students are experienced professionals, so CLOs
should start at apply and mostly sit at analyze, evaluate or create.

| Level | Example verbs |
|---|---|
| Apply | apply, implement, solve, calculate |
| Analyze | analyze, diagnose, compare, differentiate |
| Evaluate | evaluate, assess, justify, defend |
| Create | design, develop, construct, draft |

Each CLO should also describe something within the student's control. "Write a feedback plan
that changes an employee's behavior" depends on the employee. "Design a feedback conversation
that targets a specific behavior" depends on the student.

**CLOs and your storyline.** In Module 2 you will build a central character who faces decisions
at work. Each decision should come from a CLO. If a CLO suggests no decision that someone in
your students' role would face, check its Bloom's level. It may be aimed too low.

### See it

MGMT 615's first CLO began as "Apply core theories of motivation and performance to diagnose why
an employee or team is underperforming." It has two verbs. The refresh kept the one students
are graded on: "Diagnose why an employee or team is underperforming using core theories of
motivation and performance." That CLO gives Dana Ortiz her first decision. Her director says one
shift lead is the problem, and she has to work out whether he is right.

### Draft (full build)

AI instructions:

```text
Draft 4 to 6 CLOs from the course vision, the catalog commitments, the program outcomes the
course supports and the learner profile. Rules:
- One measurable action verb per CLO, at Bloom's apply level or higher, mostly analyze,
  evaluate or create.
- Describe what the student does, within the student's control.
- Together the CLOs cover every catalog commitment.
For each CLO give its Bloom's level, the catalog commitments it covers, the program outcomes it
supports, and one decision a professional in the students' role would face that the CLO
prepares them for.

Return: {"clos": [{"text": string, "verb": string, "level": string, "commitments": [string], "programOutcomes": [string], "decision": string}], "uncoveredCommitments": [string]}
```

Demo response (MGMT 615, if run as a full build):

```json
{
  "clos": [
    {"text": "Diagnose why an employee or team is underperforming using core theories of motivation and performance.", "verb": "Diagnose", "level": "Analyze", "commitments": ["Diagnose why employees and teams underperform"], "programOutcomes": ["PLO 2"], "decision": "Is the missed target one person's fault or a process problem?"},
    {"text": "Design a feedback or coaching conversation that targets a specific behavior and states the change expected.", "verb": "Design", "level": "Create", "commitments": ["Deliver feedback that changes behavior"], "programOutcomes": ["PLO 1", "PLO 3"], "decision": "What do I say to a capable lead who avoids hard calls with his crew?"},
    {"text": "Evaluate team dynamics and organizational context to select a management intervention that fits the problem.", "verb": "Evaluate", "level": "Evaluate", "commitments": ["Build and repair team dynamics", "Lead a team through change"], "programOutcomes": ["PLO 1", "PLO 2"], "decision": "Do I fix the shift handoff or the people on each shift?"},
    {"text": "Justify a delegation or decision-rights call, including the trade-offs involved.", "verb": "Justify", "level": "Evaluate", "commitments": ["Delegate and make decision-rights calls under pressure"], "programOutcomes": ["PLO 1"], "decision": "Which peak-season decisions do I keep, and which do I hand to my shift leads?"},
    {"text": "Draft a management decision message that states the decision and the next steps a direct report must take.", "verb": "Draft", "level": "Create", "commitments": ["Lead a team through change"], "programOutcomes": ["PLO 3"], "decision": "How do I announce the end of a bonus the crew likes?"},
    {"text": "Evaluate candidates for a role using a structured interview scorecard.", "verb": "Evaluate", "level": "Evaluate", "commitments": ["Hire well"], "programOutcomes": ["PLO 1", "PLO 2"], "decision": "Do I promote the proven associate or hire the outside candidate with more potential?"}
  ],
  "uncoveredCommitments": []
}
```

### Review (refresh)

AI instructions:

```text
The faculty member's current CLOs are given. Check each against this checklist:
- Starts with exactly one measurable action verb.
- Bloom's apply level or higher.
- Describes something within the student's control.
- Fits the catalog description.
Then check the set: 3 to 6 CLOs; together they cover every catalog commitment; each supports
at least one program outcome the course supports.
For each CLO return keep or revise, the issues (quoting the words that cause them) and a
revision if needed. Keep the faculty member's wording wherever it passes. If a catalog
commitment is uncovered, suggest one new CLO for it. If there are more than 6, suggest which to
merge.

Return: {"clos": [{"original": string, "action": "keep" | "revise", "issues": [string], "revision": string | null}], "setIssues": [string], "newClos": [string]}
```

Demo response (MGMT 615):

```json
{
  "clos": [
    {"original": "CLO 1: Apply core theories of motivation and performance to diagnose why an employee or team is underperforming.", "action": "revise", "issues": ["Two verbs, \"apply\" and \"diagnose\"."], "revision": "Diagnose why an employee or team is underperforming using core theories of motivation and performance."},
    {"original": "CLO 2: Design a feedback or coaching conversation that changes an employee's behavior, not just documents it.", "action": "revise", "issues": ["\"changes an employee's behavior\" depends on the employee, so the student cannot be graded on it."], "revision": "Design a feedback or coaching conversation that targets a specific behavior and states the change expected."},
    {"original": "CLO 3: Evaluate team dynamics and organizational context to select a management intervention appropriate to the actual problem.", "action": "keep", "issues": [], "revision": null},
    {"original": "CLO 4: Make a delegation or decision-rights call and justify the trade-offs involved.", "action": "revise", "issues": ["Two verbs, \"make\" and \"justify\". The justification is what an assignment can grade."], "revision": "Justify a delegation or decision-rights call, including the trade-offs involved."},
    {"original": "CLO 5: Communicate a management decision in language a direct report can act on immediately.", "action": "revise", "issues": ["\"Communicate\" does not say what students produce.", "\"can act on immediately\" is hard to grade."], "revision": "Draft a management decision message that states the decision and the next steps a direct report must take."}
  ],
  "setIssues": ["The catalog description commits the course to \"hire well\", but no CLO covers hiring. Module 8 is about hiring and currently maps to CLO 4 and CLO 1."],
  "newClos": ["Evaluate candidates for a role using a structured interview scorecard."]
}
```

### Decide

Full build: the faculty member edits, reorders, removes or adds CLOs. Refresh: for each CLO,
keep, accept the revision, edit it, or rewrite it; then accept, edit or reject any new CLO.

Checklist (shown beside the list):

- 3 to 6 CLOs.
- One measurable verb each, at apply or above.
- Each describes what the student does.
- Every catalog commitment is covered.
- Each CLO suggests a decision someone in your students' role would face.

Refresh change notes, demo examples:

- CLO 1: "Dropped 'apply' so the CLO has one verb."
- CLO 2: "Now graded on the conversation the student designs."
- CLO 3: Kept.
- CLO 4: "Dropped 'make' so the CLO grades the justification."
- CLO 5: "Changed to a written message with stated next steps so it can be graded."
- CLO 6 (new): "Added because the catalog promises hiring and Module 8 teaches it."

### Save

Planning document: Course-Level Objectives (CLOs).
Project file: `clos` (text, verb, level, commitments, programOutcomes, decision); in refresh,
`clos[].original`, `clos[].changeNote`.

### Go deeper (optional)

- `src:guide-learning-objectives`
- `src:ext-anderson-krathwohl-2001`

> Review note: sources disagree on how many CLOs to write: 3 to 7 in
> `src:reading-m1-setting-the-foundation`, 3 to 6 in `src:guide-learning-objectives` and
> `src:assignment-m1-building-the-framework`, 3 to 5 in `src:template-planning-doc`. Jared
> confirmed 3 to 6.

---

## 1.5 Module titles and topics

Time: about 30 minutes

### Learn

With CLOs set, you can lay out the modules. Flex Online courses run in weekly modules, and the
planning document has room for eight. Each module gets a title, the CLOs it works toward and a
short list of topics.

Start from the CLOs. For each one, ask what a student needs to know or practice to meet it.
Those are your candidate topics. Then cut. Students need the parts of a topic that serve the
CLO. If removing a topic would not stop anyone from meeting a
CLO, it is a candidate for cutting.

Map one or two CLOs to each module. In the MGMT 615 plan, the first CLO listed for a module is
its primary CLO and the second is supporting. Every CLO should appear in at least one module.
A CLO that appears in only one module gets little practice; one that appears in six may be
too broad.

Order matters for the storyline. In Module 3 each module becomes one scenario in your
character's story, so modules ordered the way the decisions would arrive at work make that story
easier to build. Diagnosis usually comes before treatment, and individual problems before team
or organization-wide ones.

Write titles a student would understand on day one. "Performance Management and Feedback" works.
"Unit 3" does not.

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

The sequence follows Dana Ortiz's first months on the job: she diagnoses before she coaches,
deals with one shift lead before the whole team, and hires last, once she knows what the role
needs.

### Draft (full build)

AI instructions:

```text
Draft a module sequence from the CLOs, the catalog commitments and the learner profile. Use
the number of modules the faculty member chose (default 8). For each module give a plain title,
one primary CLO and at most one supporting CLO, and 3 to 5 topics. Every CLO must appear in at
least one module. Order the modules the way the decisions would come up for a professional in
the students' role, and give a one-sentence reason for the order.

Return: {"modules": [{"number": int, "title": string, "closMet": [string], "topics": [string]}], "orderReason": string}
```

Demo response (MGMT 615, if run as a full build): the app plays back the eight modules in the
"See it" table, with the topics from the MGMT 615 course map and the Module 4 topic change
described under Review.

### Review (refresh)

AI instructions:

```text
The faculty member's current module titles, CLOs met and topics are given, along with the CLOs
saved in step 1.4 (with any renumbering). Check:
- Every saved CLO appears in at least one module. Update CLO numbers to match step 1.4.
- Each module lists one or two CLOs.
- Each topic serves a CLO the module lists.
- Topics are current for the field and are content for students, not notes about course design.
- Titles are clear to a student on day one.
- The order builds from earlier skills to later ones.
For each module return keep or revise, the issues and the revision. Report CLOs that appear in
only one module or in more than five.

Return: {"modules": [{"number": int, "action": "keep" | "revise", "issues": [string], "revision": {"title": string, "closMet": [string], "topics": [string]} | null}], "coverage": {"CLO 1": int, ...}, "coverageNotes": [string]}
```

Demo response (MGMT 615), summarized:

- Modules 1, 2, 3, 5, 6 and 7: keep.
- Module 4: revise. The topic "Designing team assignments that are accessible to every learner"
  is a note about designing the course. Suggested replacement: "Role clarity
  and ownership of handoffs."
- Module 8: revise. CLOs met changes from "CLO 4, CLO 1" to "CLO 6, CLO 1" to use the new
  hiring CLO.
- Coverage note: CLO 5 appears in five modules and CLO 2 in two. No change needed, but watch in
  Module 4 whether CLO 2 gets enough practice.

```json
{
  "modules": [
    {"number": 1, "action": "keep", "issues": [], "revision": null},
    {"number": 2, "action": "keep", "issues": [], "revision": null},
    {"number": 3, "action": "keep", "issues": [], "revision": null},
    {"number": 4, "action": "revise", "issues": ["\"Designing team assignments that are accessible to every learner\" is a note about designing the course. Students would not study it."], "revision": {"title": "Building and Leading Teams", "closMet": ["CLO 3", "CLO 1"], "topics": ["What actually predicts team performance (psychological safety, clear roles)", "The stages teams pass through when they form", "Structural fixes vs. motivational fixes", "Role clarity and ownership of handoffs"]}},
    {"number": 5, "action": "keep", "issues": [], "revision": null},
    {"number": 6, "action": "keep", "issues": [], "revision": null},
    {"number": 7, "action": "keep", "issues": [], "revision": null},
    {"number": 8, "action": "revise", "issues": ["Module 8 teaches hiring, which now has its own CLO (CLO 6)."], "revision": {"title": "Hiring and Building Your Team", "closMet": ["CLO 6", "CLO 1"], "topics": ["Why gut-feel hiring fails", "Structured interviewing and scorecards", "Proven experience vs. potential: the trade-off", "Onboarding as the first delegation and motivation test", "Course wrap-up: your management approach going forward"]}}
  ],
  "coverage": {"CLO 1": 4, "CLO 2": 2, "CLO 3": 3, "CLO 4": 1, "CLO 5": 5, "CLO 6": 1},
  "coverageNotes": ["CLO 5 appears in five modules and CLO 2 in two. Consider whether CLO 2 needs more practice.", "CLO 4 and CLO 6 each appear in one module. That can work for a focused skill, but check that the module's main assignment assesses it."]
}
```

### Decide

The faculty member edits titles, CLOs met and topics in a table, one column per module, and can
drag modules to reorder them. Refresh: keep, accept, edit or rewrite each module.

Checklist:

- Every CLO appears in at least one module.
- Each module has one or two CLOs.
- Each topic serves a CLO its module lists.
- Titles make sense to a student on day one.
- The order follows the way the decisions would come up at work.

Refresh change notes, demo examples:

- Module 4: "Replaced a course design note with a topic students study."
- Module 8: "Mapped to the new hiring CLO."

### Save

Planning document: Module Titles, CLOs met and Module Topics rows in Tables 1 and 2. See
`export.md` for the full table layout.
Project file: `modules[].title`, `modules[].closMet`, `modules[].topics`; in refresh,
`modules[].original`, `modules[].changeNote`. Module objectives and other columns found in an
uploaded course map stay in `source.sections` for later modules.

### Go deeper (optional)

- `src:guide-course-alignment`

---

## 1.6 Check alignment

Time: about 20 minutes

### Learn

Alignment means the parts of your plan point at the same goals. At this stage that means four
links: the vision fits the catalog description, the CLOs cover the catalog's commitments, the
CLOs support program outcomes, and every CLO shows up in a module. A course that is aligned feels
coherent to students, because each week's work clearly leads somewhere.

This step runs one check across everything you have saved in Module 1. Fix what you can now.
Anything you want to leave as it is gets a short note, so your ID can see you chose it.

Your ID reviews these sections with you at your Module 1 check-in. Before you start Module 2,
take the vision and CLOs to your program director and confirm they fit the catalog description
and the program's plans for the course. Record the outcome here.

### See it

After the refresh, MGMT 615's check passed with one note: CLO 4 and CLO 6 each appear in only
one module. The instructor kept that, with the note "Delegation and hiring are each a focused
skill, practiced and assessed in one module." The program director confirmed the six CLOs
before the instructor started Module 2.

### Draft (full build) and Review (refresh)

Same instructions for both tracks.

AI instructions:

```text
Check the Module 1 sections for alignment:
1. Vision fits the catalog commitments.
2. Every catalog commitment is covered by at least one CLO.
3. Every CLO supports at least one program outcome the course supports.
4. Every CLO appears in at least one module; note CLOs in only one module or in more than five.
5. Every module topic serves a CLO its module lists.
Return one result per check: pass, or issue with a sentence describing it and the section to
fix. Do not repeat checks that pass in detail.

Return: {"checks": [{"check": string, "result": "pass" | "issue", "detail": string | null, "section": string | null}]}
```

Demo response (MGMT 615, after the refresh changes above):

```json
{
  "checks": [
    {"check": "Vision fits the catalog", "result": "pass", "detail": null, "section": null},
    {"check": "Catalog commitments covered by CLOs", "result": "pass", "detail": null, "section": null},
    {"check": "CLOs support program outcomes", "result": "pass", "detail": null, "section": null},
    {"check": "CLOs appear in modules", "result": "issue", "detail": "CLO 4 and CLO 6 each appear in only one module.", "section": "1.5 Module titles and topics"},
    {"check": "Topics serve their module's CLOs", "result": "pass", "detail": null, "section": null}
  ]
}
```

### Decide

For each issue the faculty member selects Fix (which opens that step) or Keep with a note.
They also record the program director review: not yet scheduled, scheduled (with date) or done.

Checklist:

- Every issue is fixed or has a note.
- The program director review is scheduled or done.

### Save

Planning document: nothing new. In refresh, the change log for Module 1 sections is complete.
Project file: `alignment.m1` (checks and notes), `programDirectorReview`.
