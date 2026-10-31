# Module 4. Intentional AI Implementation for Engagement & Feedback

Module id: `m4`
Steps: 2
ID check-in: live review of this module's sections, at the end of the week or sooner

Faculty complete: learning activities for every module, including third-party tools, checked
automatically for RSI, workload and AI risk, and a week-in-your-student's-shoes review of each
module.

Refresh checks for this module: at least two RSI categories of instructor activity per module;
about 10 hours of student work a week; major assessments that AI could complete without student
thinking.

Sources: `src:reading-m4-crafting-part-1`, `src:reading-m4-crafting-part-2`,
`src:assignment-m4-assessment-interaction-plan`, `src:assignment-m4-course-tutor`,
`src:guide-learning-activities`, `src:guide-rubrics`, `src:guide-third-party-tools`,
`src:example-mgmt615-course-map`

Demo data: `demo/mgmt615-activities.json`

## Refresh reflection

Shown once, in the refresh track only, before step 4.1. It asks only about activities and
assessments the course already has. AI and XR, which most courses are adding for the first
time, are left out.

Prompt shown: "Think about the activities and assessments in the last version of this course.
Answer whichever of these apply."

1. Which activities gave you the best evidence of what students could do? Which gave you the
   weakest?
2. Where did grading take more time than it was worth?
3. Have you seen work that looked like a student let AI do the thinking? On which activities?
4. Which activities would you keep exactly as they are?

AI instructions (added to each Review step in this module): same as the Module 1 reflection
instruction.

Demo answers (MGMT 615):

1. "The feedback scripts were the weakest. The team memo was the strongest because students had
   to pick a fix and defend it."
2. "The Management Approach Summary in the last week. Forty reflections, and most said the same
   things."
3. "The feedback scripts again. Several read like they came from the same template."
4. "The cohort roundtables and the delegation memo."

Project file: `reflection.m4`.

---

## 4.1 Activities for every module

Time: about 45 minutes, about 5 minutes a module
Pattern: pick and combine, one module at a time (full build); edit in place (refresh)

### Learn

A learning activity moves students toward an objective and gives you evidence of whether they
got there. At this stage you don't write prompts or rubrics. You decide what students will do in
each module, clearly enough that your ID can see the plan.

A planned activity:

- **Traces to a CLO and matches its verb.** If the CLO says evaluate, the activity has to
  require evaluation. If you can't name the CLO, the activity may not belong.
- **Asks students to do what professionals do**: analyze data, recommend a course of action,
  design a process, run a conversation.
- **Fits the week.** Flex Online courses plan for about 10 hours of student work a week,
  including readings, videos, activities and the 90-minute cohort session. Module 1 is lighter,
  about 4 hours, while students get oriented.
- **Adds variety.** If every module has the same format, the course feels repetitive and the same
  students are always at a disadvantage.

**Your storyline supplies the activities.** Each scenario ends in a decision, and that is where
the module's main activity belongs. One decision can become an assignment where students write a
recommendation, a discussion where they argue what the character should do, or a short quiz that
checks they can find the root cause first. Not every activity has to come from the story. Use it
where it fits.

**Canvas offers three activity types.** Assignments are for producing something, such as an
analysis or a plan. Discussions are for dialogue across professional perspectives. Quizzes are
for low-stakes checks before harder work. Cohort sessions come in Module 7.

**Weight.** Mark each activity high, medium or low. Activities that show mastery of a CLO carry
more weight than the practice that builds toward it. Points and rubrics are finished with your
ID during development.

**Aggie Core Values.** Look for one or two places where an activity asks students to act with
integrity, lead or consider who their decision affects. Your character's decisions are often
the natural spot. You don't need all six values.

**Watch the last module.** Courses often stack a final project on the module's normal work, and
the last week ends up twice as heavy. Start a course-wide synthesis a module early, or let it
replace that module's main assignment.

**Design major assessments for AI.** For each high-weight activity, ask whether a student could
hand the prompt to an AI tool and submit what comes back without doing the thinking the CLO asks
for. Banning AI rarely solves this, and detection tools are unreliable. Design does better. Changes
that make a student's own thinking visible:

- **Their own context.** Students apply the concept to their own team, client or organization,
  which an AI tool doesn't know.
- **Process evidence.** Students submit annotations explaining their choices, a draft
  with revisions, or a short reflection on what they changed and why.
- **A live part.** Students defend, rehearse or present the work in a cohort session.
- **Course-specific material.** The work depends on your storyline, data or earlier submissions.

You can also allow AI on purpose: let students draft with it, then grade their critique and
revision of the draft. Say clearly in the prompt what use is allowed.

Low-weight practice doesn't need this check. The point of practice is the practice.

**Third-party tools.** A tool earns a place when it serves an objective better than a Canvas
activity would. The AI may suggest one where it fits.

| Tool | What it does | Fits a story-based course when |
|---|---|---|
| Perusall | Students annotate readings, video or web pages together; grades automatically | Students annotate a scenario and flag what they'd do before the discussion |
| Peerceptiv | Structured peer review; students review the reviews; grades from review quality | Students compare how classmates reasoned through the same decision |
| Poll Everywhere | Polls and open questions, live or on students' own time | Students vote on the character's choice, then argue it in the cohort session |

The checks ask six questions about any tool you choose, from privacy to your time. Automatic
scores from these tools don't count as RSI on their own; plan what you'll add.

**A grading assistant (optional).** You can also set up an AI assistant for yourself that drafts
feedback on student work. In Google Gemini, a Gem holds standing instructions and "knowledge
files": you give it the assignment prompt and your rubric, then paste in one submission at a time
and it drafts rubric-based comments. It can save real time in a large course. Three cautions:
use only a tool the university has approved for student data (TAMU licenses Gemini with
enterprise privacy protection, but confirm with your ID before uploading student work); read and
edit every comment before it goes to a student, which is also what makes it count as RSI; and
the grade is always yours. The build steps are under Go deeper.

### See it

MGMT 615 Module 3 after the refresh:

| Activity | CLO | Weight | Hours |
|---|---|---|---|
| Assignment: Feedback Conversation Script, Dana and Jordan | CLO 2 | High | 3 |
| Perusall: Feedback That Lands (Chapter 4) | CLO 2 | Low | 1.5 |
| Interactive: Coaching or Discipline? Scenario Sort | CLO 2 | Low | 0.5 |

The script sits at the module's decision point: students write the conversation Dana has with
Jordan.

### Draft (full build)

The AI offers two versions of each module's activity set. The faculty member picks one, combines
them, or writes their own.

AI instructions:

```text
For the given module, propose two versions of its activity set, each with 2 to 4
activities, from the module's CLOs met, topics and saved scenario. Make the main activity sit at the scenario's decision point. For each activity
give: type (Assignment, Discussion, Quiz), a short title, the CLOs it assesses with the verb it
uses, weight (high, medium, low), estimated student hours, and one sentence on what students do.
Every module needs exactly one high-weight activity unless the faculty member's notes say
otherwise. Vary types across modules. Do not include cohort session activities.

Where a third-party tool (Perusall, Peerceptiv, Poll Everywhere) would serve an objective better
than a Canvas activity, include it with type set to the tool name. At most one tool per module.

Return: {"versions": [{"activities": [{"type": string, "title": string, "clos": [string], "verb": string, "weight": string, "hours": number, "what": string}]}]}
```

Demo response (MGMT 615, if run as a full build): each module's activities from
`demo/mgmt615-activities.json`.

### Review (refresh)

The app shows each module's current activities from the uploaded course map.

AI instructions:

```text
Each module's current activities are given, with the module's CLOs met, topics and saved
scenario. For each activity check: it traces to a CLO and matches the CLO's verb; students do
something professionals do; the main activity sits at or near the scenario's decision. Keep
what passes. For the rest, quote the problem and suggest one revision. Add estimated hours and
weight to every activity. Note modules where activity types repeat the previous module.

Return: {"modules": [{"module": int, "activities": [{"original": string, "action": "keep" | "revise", "issues": [string], "revision": {...same shape as full build...}}]}]}
```

Demo response (MGMT 615): each module and its `review` notes from
`demo/mgmt615-activities.json`. The main finding: three of the four main assignments used
separate cases or a topic of the student's choice. The review moves each to the module's
scenario decision and keeps the original cases as readings or comparisons.

### Decide

For each module the faculty member edits, adds or removes activities and marks, for each
high-weight activity, the AI use allowed: not allowed, allowed with disclosure, or required as
part of the task.

Checklist (for each module):

- One main activity carries the module's weight.
- Students do something professionals in your field do.
- Each high-weight activity says what AI use is allowed.

### Checks

On save of each module:

- **Alignment:** each activity traces to a CLO the module lists and uses its verb.
- **RSI:** at least two categories of instructor activity, counting the cohort session (4) and
  responsive weekly announcements (3) if the interaction statement promises them.
- **Workload:** activities total about 4 to 5 hours (about 1.5 in Module 1), leaving room for
  readings, media and the 90-minute cohort session. The last module is flagged if it runs much heavier than the others.
- **AI risk:** each high-weight activity rated high, medium or low, with a suggested change for
  high and medium.
- **Tools:** each third-party tool answers the six questions (alignment, feedback quality,
  academic integrity, access, privacy, your time); privacy shows "check with your ID" unless the
  tool is approved.

RSI and workload instructions:

```text
For each module, using its saved activities, the step 2.2 RSI check, the syllabus statement and
whether the module has a cohort session (assume yes for modules 2 to 8 unless told otherwise):
1. Assign each activity an RSI category or null, with a short reason. Auto-graded work and
   student-only activities are null unless the faculty member described instructor involvement.
2. Count the categories the module covers, including the cohort session (4) and responsive
   weekly announcements (3) if the syllabus statement promises them.
3. Total the activity hours.
Flag modules with fewer than two categories, and modules whose activities exceed 5 hours (2 hours in Module 1).
For each flag, suggest one specific change.

Return: {"modules": [{"module": int, "activities": [{"title": string, "rsi": int | null, "reason": string}], "categories": [int], "hours": number, "flags": [string]}]}
```

AI-risk instructions:

```text
For each high-weight activity, judge how easily a student could complete it with a general AI
tool and no course-specific thinking: high, medium or low. Give a one-sentence reason based on
what the activity asks for. For high and medium, suggest one change that makes the student's own
thinking visible, using their own context, process evidence, a live part or course-specific
material. Keep the activity's CLO and verb. Do not suggest AI detection tools.

Return: {"assessments": [{"module": int, "activity": string, "risk": "high" | "medium" | "low", "why": string, "change": string | null}]}
```

Demo flags (MGMT 615), from `demo/mgmt615-activities.json`: Module 1, "about 4.5 hours of
activities in a 4-hour week; make the sort optional and shorten the case analysis"; Module 5, "Perusall counts for RSI
only with instructor replies; apply the Module 3 fix"; Module 8, "about 6 hours of activities;
move part of the Management Approach Summary earlier"; AI risk high for the Module 3 script, the
Module 7 change message and the Module 8 summary, with the changes in `aiCheck`.

### Save

Planning document: Learning Activities Plan Part 1 (Canvas) and Part 2 (third-party tools) rows
in Tables 1 and 2, one line per activity, for example "Assignment: Feedback Conversation Script
(CLO 2, high, RSI 2; annotated and rehearsed in cohort session)".
Project file: `modules[].activities` (with `rsi`, `hours`, `aiRisk`, `aiPolicy`, `aiChange`),
`modules[].toolActivities`; in refresh, `.original` and `.changeNote`.

### Go deeper (optional)

- `src:reading-m4-crafting-part-1`, `src:reading-m4-crafting-part-2`
- `src:guide-learning-activities`, `src:guide-rubrics`, `src:guide-third-party-tools`
- `src:ext-tamu-ai-guidelines`, `src:ext-terry-2023`
- `src:assignment-m4-course-tutor` and `src:ext-bowen-watson-2025-ch15`: build an AI tutor for
  your students, or a grading assistant for yourself, in Google Gemini, outside this tool.

---

## 4.2 A week in your student's shoes

Time: about 20 minutes, a few minutes a module
Pattern: a week in your student's shoes

### Learn

A plan can pass every check and still feel wrong to a student. In this step the AI walks through
each module's week as one of your students would live it: what they open on Monday, what they
read, do and submit, when they hear from you, and how long it takes. You react to what feels
heavy, thin or silent, and fix it in step 4.1 if you want to.

Readings and media aren't planned yet, so the walk-through uses placeholders for them. You'll
see the full week again in Modules 5 and 6.

### See it

MGMT 615, Module 3, as a student: "Monday, an announcement picks up Dana's story: Greg wants a
formal warning for Jordan. I spend about an hour and a half annotating the feedback chapter in
Perusall; on Thursday the instructor replies to my thread with a question about Jordan. Wednesday
night I do the 30-minute coaching-or-discipline sort. Saturday I draft the feedback script and
annotate why each line is there, about three hours. In Tuesday's cohort session I rehearse it
with a partner. I hear from the instructor three times this week." The instructor's reaction:
"Saturday is the whole assignment. Move the script due date to Sunday and open it Wednesday."

### Draft (full build) and Review (refresh)

AI instructions:

```text
Walk through the given module's week as one of the course's students, in first person and in
time order, using the learner profile, the saved activities, the interaction statement, the
scenario and a 90-minute cohort session. Use [reading] and [video] placeholders where materials
aren't planned yet. Give rough hours for each part and a total. Then list, in one line each:
the heaviest point in the week, any stretch of three or more days with no contact from the
instructor, and anything a student might not understand the purpose of. Under 200 words.

Return: {"walkthrough": string, "hours": number, "heaviest": string, "silent": string | null, "unclear": string | null}
```

Demo response (MGMT 615, Module 3): the walk-through under See it, with hours 5.5, heaviest
"Saturday: the whole script in one sitting", silent null, unclear null.

### Decide

For each module the faculty member selects Looks right, or writes a short note and optionally
returns to step 4.1 to change the module's activities.

Checklist:

- No week has one day carrying most of the work.
- Students hear from you at least twice a week.

### Checks

None beyond step 4.1's, which run again on any activity changes.

### Save

Planning document: nothing new.
Project file: `modules[].weekWalk` (walk-through, hours, reaction).

---

## Check-in prep

Same instructions as Module 1.

Demo response (MGMT 615):

```json
{
  "changed": ["Activities for all eight modules: three main assignments moved onto the storyline", "Module 5 Perusall: instructor replies added", "Module 8: summary draft moved to Module 7", "AI changes for three high-risk assessments"],
  "keptFlags": [],
  "questions": ["Is about 4 to 5 hours of activities a module the right target for this program?", "Should students be allowed to draft with AI on the change message if they critique the draft?"]
}
```

Project file: `checkins.prep.m4`.
