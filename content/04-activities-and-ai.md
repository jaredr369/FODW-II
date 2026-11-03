# Module 4. Intentional AI Implementation for Engagement & Feedback

Module id: `m4`
Steps: 3
ID check-in: live review of this module's sections, at the end of the week or sooner

Faculty complete: learning activities for every module, including third-party tools, checked
automatically for RSI, workload, and AI risk, and a week-in-your-student's-shoes review of each
module.

Refresh checks for this module: at least two RSI categories of instructor activity per module;
close to 10 hours of student work a week; major assessments that AI could complete without student
thinking.

Sources: `src:reading-m4-crafting-part-1`, `src:reading-m4-crafting-part-2`,
`src:assignment-m4-assessment-interaction-plan`, `src:assignment-m4-course-tutor`,
`src:guide-learning-activities`, `src:guide-rubrics`, `src:guide-third-party-tools`,
`src:example-mgmt615-course-map`

Demo data: `demo/mgmt615-activities.json`

## Refresh reflection

> App note: Shown once, in the refresh track only, before step 4.1. It asks only about activities
> and assessments the course already has. AI and XR, which most courses are adding for the first
> time, are left out.

::: purpose
**What you'll do:** Answer a few questions about the activities and assessments in the last version
of your course. Answer whichever apply; short notes are fine.

**Why it matters:** The AI uses your answers when it reviews each section in this module, so its
suggestions reflect what actually happened in your course.
:::

1. Which activities gave you the best evidence of what students could do? Which gave you the
   weakest?
2. Where did grading take more time than it was worth?
3. Have you seen work that looked like a student let AI do the thinking? On which activities?
4. Which activities would you keep exactly as they are?

> App note: AI instructions are the same as the Module 1 reflection instruction.

Demo answers (MGMT 615):

1. "The feedback scripts were the weakest. The team memo was the strongest because students had
   to pick a fix and defend it."
2. "The Management Approach Summary in the last week. Forty reflections, and most said the same
   things."
3. "The feedback scripts again. Several read like they came from the same template."
4. "The cohort roundtables and the delegation memo."

Project file: `reflection.m4`.

---

## 4.1 Choose and build with AI

Time: about 45 minutes
Pattern: choose, then build (both tracks)

### Learn

::: purpose
**What you'll do:** Learn three ways to put AI to work in your course, choose one, and build it: an
AI-integrated assignment, an AI tutor, or a grading assistant.

**Why it matters:** Your students will use AI whether you plan for it or not. Building one thing
yourself shows you what AI does well and where it needs limits, before you plan the activities for
every module.
:::

There are three ways to bring AI into your course on purpose:

| Option | What it is | Who uses it | Where you build it |
|---|---|---|---|
| An AI-integrated assignment | An assignment where students work with an AI assistant you set up, such as role-playing a stakeholder from your scenario or critiquing an AI draft | Students | A Gemini Gem in Canvas |
| An AI tutor | An assistant students use for practice and feedback between assignments. It coaches and asks questions instead of doing graded work | Students | A Gemini Gem in Canvas |
| A grading assistant | An assistant that drafts rubric-based feedback on student work for you to review and edit | You | TAMU AI Chat |

**Why two different tools.** Gemini is built into our Canvas, so a Gem you create there is easy to
share with your students. TAMU AI Chat offers several AI models and the most protected environment
for student records, which matters under FERPA when an assistant reads student work. Both are
university-protected environments.

**A few terms you'll use:**

- **System instructions:** the standing rules that tell the assistant who it is, what to do, and how
  to respond in every conversation.
- **Knowledge files:** documents you attach so its answers fit your course, such as the assignment
  directions, your scenario, or a rubric. Never attach student work or records to a student-facing
  Gem.
- **Guardrails:** what it won't do, such as write a student's graded work for them or assign a
  final grade.
- **Hallucination:** when AI states something false with confidence. It's why you test what you
  build, and why you review anything it gives students.

**Choose what you'll build.** You can build the others later with your ID.

::: choose aiChoice
- assignment | An AI-integrated assignment | Students work with a Gem you set up as part of one assignment.
- tutor | An AI tutor | Students practice with a Gem between assignments.
- grader | A grading assistant | You get draft feedback on student work, built in TAMU AI Chat.
:::

### See it

::: when aiChoice=
Choose an option above to see what the MGMT 615 instructor built with it.
:::

::: when aiChoice=assignment
For Module 7's change message, the MGMT 615 instructor built a Gem that plays a skeptical member of
Dana's crew. Students share their draft announcement that the bonus is ending, read the crew
member's reactions, revise, and submit both drafts with a short note on what they changed and why.
The AI-risk check in Module 4 had rated this assignment high; the Gem makes students' own judgment
visible.
:::

::: when aiChoice=tutor
For Module 5, the MGMT 615 instructor built "Practice with Greg," a Gem that plays Dana's director.
Students rehearse telling Greg he's wrong before they write the assignment. Greg pushes back the way
a busy director would and gives one coaching tip after each exchange, but never writes the graded
work.
:::

::: when aiChoice=grader
The MGMT 615 instructor built a grading assistant in TAMU AI Chat for Module 3's Feedback
Conversation Script. It drafts two or three comments for each rubric criterion and suggests a
rating with a reason, but never a final grade. The instructor pastes in one submission at a time,
with the student's name removed, and edits every comment before posting it in Canvas.
:::

### Draft (full build) and Review (refresh)

::: when aiChoice=
Choose an option in Learn first. The build steps and the AI's draft depend on what you choose.
:::

::: when aiChoice=assignment,tutor
::: fold How to build your Gem and add it to Canvas
**Build the Gem**

1. Go to gemini.google.com and sign in with your TAMU Google account. In the left sidebar, select
   **Gems**, then **Create a new Gem**. Build it under your own account: a Gem belongs to whoever
   creates it, and students lose access if its owner stops sharing it.
2. Name it for students, such as "Crew Reactions" or "Practice with Greg."
3. Paste the system instructions the AI drafts below, edited into your own words. Before you save,
   ask yourself: Have I told it what to do? What *not* to do? Does it send students back to me for
   grades and other high-stakes questions? Is its scope narrow enough to stay on topic?
4. Add knowledge files: your scenario, the assignment directions (so it knows what it must not do
   for students), and any reading it should draw on. Never add student work or records.
5. Save it, then test it the way a student would, including a request it should refuse, such as
   "Can you just write my assignment for me?" Revise the instructions until it behaves.

**Add it to your Canvas course**

1. In your course, select **Modules**, find the module, and select **Add Item** (the plus sign).
2. Choose **External Tool**, then **Google Gemini**. If asked, sign in with your TAMU Google account
   and authorize the connection.
3. Select **Gem**, choose your Gem, set it to open in a new tab if needed, and select **Add Item**.
4. Publish the item when it's ready. Students open the Gem from the module and get view access to
   it.

::: when aiChoice=assignment
In the assignment directions, say what students do with the Gem and what they submit.
:::

::: when aiChoice=tutor
Tell students when to use it and what it's for, in the module overview or an announcement.

Want a study space instead of a conversation partner? The same Canvas tool can add a Gemini
Notebook, grounded in the course materials you choose; students can study with it but can't change
its sources.
:::

Google Gemini is on by default in Canvas courses. If you don't see it, turn it on in **Settings**,
**Navigation**. Full steps: `src:ext-tamu-lms-gemini`. Your ID can walk you through the build.
:::
:::

::: when aiChoice=grader
::: fold How to build a grading assistant in TAMU AI Chat
1. Open TAMU AI Chat at chat.tamu.ai and sign in with your NetID.
2. Create a custom assistant (in TAMU AI Chat's workspace, add a new model) and choose the AI model
   it runs on.
3. Paste the grading instructions the AI drafts below into the assistant's system prompt, edited
   into your own words.
4. Add knowledge files: the assignment prompt and your rubric.
5. Test it on a sample submission with the student's name removed, and compare its comments with
   your own.
6. Use it one submission at a time, with names removed. Read and edit every comment before you
   post it in Canvas. The grade is always yours, and your reviewed feedback is what counts as RSI.

Menu names in TAMU AI Chat can change. Your ID can walk you through the build.
:::
:::

Answer two questions, then select the button below. The AI drafts the system instructions for what
you chose, with guardrails built in. Select **Use these instructions** to copy them into the boxes
under Decide, then paste your final version into your Gem or assistant.

::: fields
- Which module and activity is this for? | Module 5, Telling Greg He's Wrong.
- What should it do for students, or for you? | Let students rehearse pushing back on their director before they write the assignment.
:::

AI instructions:

```text
Draft system instructions for the faculty member's chosen build (an AI-integrated assignment Gem,
an AI tutor Gem, or a grading assistant), from their answers and the module's CLOs, scenario, and
activity. Give it a role, the task, how to respond, and a length limit. Build in guardrails: a
student-facing Gem never writes graded work for a student and says so if asked; a grading
assistant never assigns a final grade, quotes the student's own words, flags anything it is
unsure of, and never refers to a student by name. For an AI-integrated assignment, also draft one
sentence of student directions. Under 200 words.

Return: {"where": string, "instructions": string, "directions": string | null}
```

Demo response (MGMT 615):

::: when aiChoice=assignment
**Where it's used:** Module 7, Ending the Bonus: the change-message assignment. Students use it.

**System instructions:** You are a member of Dana Ortiz's crew at a distribution center, hearing that
the pick-rate bonus is ending. React to the student's draft announcement as a skeptical but fair
crew member: say what worries you and what you still don't understand. Stay in role. Don't rewrite
the message; react to it. If asked to write it, say that's the student's job. Keep replies under
120 words.

**Student directions:** Share your draft announcement with the Crew Reactions Gem, revise it after
reading the crew's reactions, and submit both drafts with a short note on what you changed and why.
:::

::: when aiChoice=tutor
**Where it's used:** Module 5, Telling Greg He's Wrong: practice before the assignment. Students
use it.

**System instructions:** You are Greg Halvorsen, regional director for a distribution center. You
believe Jordan's shift is the problem. When the student, speaking as Dana, presents evidence, push
back the way a busy director would: ask for the data and question the timeline. Concede only to
specific evidence and a clear plan. After each exchange, give one coaching tip in brackets. Never
write the student's graded assignment; if asked, say practice is the point. Keep replies under 120
words.
:::

::: when aiChoice=grader
**Where it's used:** Module 3, Feedback Conversation Script: grading. You use it.

**System instructions:** You help the instructor grade the Feedback Conversation Script, using the
attached assignment prompt and rubric. For each submission, draft two or three comments for each
rubric criterion: what works, what to improve, and one suggestion, quoting the student's own words.
Suggest a rating for each criterion with a one-line reason, but never a final grade. Flag anything
you're unsure of for the instructor. Never refer to the student by name.
:::

### Decide

Your final version goes in these boxes. Type in any box to change it, or select **Redraft with AI**
under a box to have the AI rewrite just that part. Paste the final instructions into your Gem or
assistant, test it, and note what you changed.

::: fields
- Where it's used: the module, the activity, and who uses it
- Its system instructions, as you'll paste them into your Gem or assistant
- How you tested it, and what you changed
:::

Checklist:

- It has guardrails: what it won't do.
- No student names or records are in a student-facing Gem's knowledge files.
- For a grading assistant: you remove names and review every comment before it reaches a student.
- Students will know how they may use it, from the assignment directions or the syllabus.

### Checks

When you save, the tool checks that:

- the instructions give a role, a task, and at least one guardrail;
- a grading assistant never assigns final grades or names a student;
- the module and activity match ones in your plan.

### Save

Planning document: an "AI in this course" line in the Learning Activities Plan row for the module
where it's used, naming what you built.
Project file: `ai.choice`, `ai.where`, `ai.instructions`, `ai.testing`.

### Go deeper (supplemental)

- `src:assignment-m4-course-tutor`: the full lesson on building a course tutor and a grading
  assistant, with key terms and tool comparisons.
- `src:ext-bowen-watson-2025-ch15`: custom bots and how to design them for teaching.
- `src:ext-tamu-lms-gemini`: adding Gemini Gems and Notebooks to Canvas courses.

---

## 4.2 Activities for every module

Time: about 45 minutes, about 5 minutes a module
Pattern: pick and combine, one module at a time (full build); edit in place (refresh)

### Learn

::: purpose
**What you'll do:** Plan the learning activities for each module: what students will do, which CLO
each activity serves, how much it weighs, and how long it takes.

**Why it matters:** Activities are where students practice and show what they've learned. They give
you the evidence of whether students met your CLOs.
:::

At this stage you don't write prompts or rubrics. Plan clearly enough that your ID can see what
students will do.

A planned activity:

- **Traces to a CLO and matches its verb.** If the CLO says evaluate, the activity has to
  require evaluation. If you can't name the CLO, the activity may not belong.
- **Asks students to do what professionals do**: analyze data, recommend a course of action,
  design a process, run a conversation.
- **Fits the week.** Activities are one part of a student's week, so they need room for the rest.
- **Adds variety.** If every module has the same format, the course feels repetitive and the same
  students are always at a disadvantage.

::: figure budget | A typical week in Modules 2 to 8: close to 10 hours
- Activities | roughly 6 hours | 63
- Readings and media | roughly 2 hours | 21
- Cohort session | 90 minutes, live or recorded | 16
- Note | Module 1 is different: about 4 hours in all, with no cohort session, while students get oriented.
:::

::: fold How the time estimates work
The AI estimates each activity's time, and you can change any estimate: it's the number of hours in
parentheses on each line of your activities box. Due dates follow the Flex Online pattern, so you
don't need to add them; to use a different day for one activity, add it to its line, such as "due
Thu." Everything else uses these rates:

- **Reading:** about 8 pages an hour (6 for dense material such as research articles, 10 for
  lighter reading such as trade articles and cases).
- **Video and audio:** playback time plus about a quarter, for pausing and notes.
- **Cohort session:** 90 minutes, in Modules 2 to 8.

Until you plan materials in Module 5 and media in Module 6, the checker assumes about 2 hours for
readings and media (about 1 in Module 1). If your program director sets a different weekly target,
enter it in your course details (step GS.2). For a fuller method, see Rice University's Course
Workload Estimator: `src:ext-rice-workload`.
:::

**Your storyline supplies the activities.** Each scenario ends in a decision, and that is where
the module's main activity belongs. One decision can become an assignment where students write a
recommendation, a discussion where they argue what the character should do, or a short quiz that
checks they can find the root cause first. Not every activity has to come from the story. Use it
where it fits.

**Canvas offers three activity types.** Assignments are for producing something, such as an
analysis or a plan. Discussions are for dialogue across professional perspectives. Quizzes are
for low-stakes checks before harder work. Cohort sessions come in Module 7.

**Weight.** Mark each activity high, medium, or low. Activities that show mastery of a CLO carry
more weight than the practice that builds toward it. As a guide, finished work such as analyses,
plans, and projects makes up 70 to 90 percent of the grade, and practice and participation 10 to 30
percent. Points and rubrics are finished with your ID during development.

**Watch the last module.** Courses often stack a final project on the module's normal work, and
the last week ends up twice as heavy. Start a course-wide synthesis a module early, or let it
replace that module's main assignment.

**Design major assessments for AI.** For each high-weight activity, ask whether a student could
hand the prompt to an AI tool and submit what comes back without doing the thinking the CLO asks
for. Banning AI rarely solves this, and detection tools are unreliable. Design does better. Changes
that make a student's own thinking visible:

- **Their own context.** Students apply the concept to their own team, client, or organization,
  which an AI tool doesn't know.
- **Process evidence.** Students submit annotations explaining their choices, a draft
  with revisions, or a short reflection on what they changed and why.
- **A live part.** Students defend, rehearse, or present the work in a cohort session.
- **Course-specific material.** The work depends on your storyline, data, or earlier submissions.

You can also allow AI on purpose: let students draft with it, then grade their critique and
revision of the draft. Say clearly in the prompt what use is allowed. Low-weight practice doesn't
need this check. The point of practice is the practice.

**Aggie Core Values.** Look for one or two places where an activity asks students to act with
integrity, lead, or consider who their decision affects. Your character's decisions are often
the natural spot. You don't need all six values.

::: fold Third-party tools: Perusall, Peerceptiv, and Poll Everywhere
A tool earns a place when it serves an objective better than a Canvas activity would. The AI may
suggest one where it fits.

| Tool | What it does | Fits a story-based course when |
|---|---|---|
| Perusall | Students annotate readings, video, or web pages together; grades automatically | Students annotate a scenario and flag what they'd do before the discussion |
| Peerceptiv | Structured peer review; students review the reviews; grades from review quality | Students compare how classmates reasoned through the same decision |
| Poll Everywhere | Polls and open questions, live or on students' own time | Students vote on the character's choice, then argue it in the cohort session |

The checks ask six questions about any tool you choose, from privacy to your time. Automatic
scores from these tools don't count as RSI on their own; plan what you'll add, such as replies in
the tool's threads.
:::

**AI in your activities.** In step 4.1 you built an AI-integrated assignment, a tutor, or a grading
assistant. Place it in the module you chose, and plan AI use for each high-weight activity below.

### See it

::: full
Here are the activities the MGMT 615 instructor planned for Module 3. The script sits at the
module's decision point: students write the conversation Dana has with Jordan.
:::

::: refresh
Here are MGMT 615's Module 3 activities after the review. The script sits at the module's decision
point: students write the conversation Dana has with Jordan. The Perusall reading now counts for RSI
because the instructor replies in its threads each Thursday.
:::

| Activity | CLO | Weight | Hours |
|---|---|---|---|
| Assignment: Feedback Conversation Script, Dana and Jordan | CLO 2 | High | 4 |
| Perusall: Feedback That Lands (Chapter 4) | CLO 2 | Low | 1.5 |
| Interactive: Coaching or Discipline? Scenario Sort | CLO 2 | Low | 0.5 |

### Draft (full build) and Review (refresh)

Work through your modules one at a time. Choose a module, then select the button below. The AI
drafts the module's activities from its CLOs, topics, and scenario, and shows what the checks will
find: the hours, the RSI categories, and the AI risk of each high-weight activity. Select **Use
these activities** to copy them into the boxes under Decide.

::: refresh
The AI starts from your Course Map's current activities for the module. It keeps what works, says
what it would change and why, and adds hours and weight to each activity.
:::

::: module-picker
:::

::: full
AI instructions:

```text
For the given module, propose an activity set of 2 to 4 activities from the module's CLOs met,
topics, and saved scenario. Make the main activity sit at the scenario's decision point. For each
activity give: type (Assignment, Discussion, Quiz), a short title, the CLOs it assesses with the
verb it uses, weight (high, medium, low), estimated student hours, and one sentence on what
students do. Every module needs exactly one high-weight activity unless the faculty member's notes
say otherwise. Vary types across modules. Do not include cohort session activities. Where a
third-party tool (Perusall, Peerceptiv, Poll Everywhere) would serve an objective better than a
Canvas activity, include it with type set to the tool name. At most one tool per module.

Return: {"activities": [{"type": string, "title": string, "clos": [string], "verb": string, "weight": string, "hours": number, "what": string}]}
```
:::

::: refresh
AI instructions:

```text
The module's current activities are given, with its CLOs met, topics, and saved scenario. For each
activity check: it traces to a CLO and matches the CLO's verb; students do something
professionals do; the main activity sits at or near the scenario's decision. Keep what passes.
For the rest, quote the problem and suggest one revision. Add estimated hours and weight to every
activity. Note when activity types repeat the previous module.

Return: {"module": int, "activities": [{"original": string, "action": "keep" | "revise", "issues": [string], "revision": {...same shape as full build...}}]}
```
:::

Demo response (MGMT 615):

::: module-options
:::

### Decide

Your final activities for each module go in these boxes. Type in any box to change it, or select
**Redraft with AI** under a box to have the AI rewrite just that part. To work on another module,
choose it above; what you've typed is kept.

For each high-weight activity, decide what AI use is allowed and say so in the second box. The week
check below adds up the whole week as you type: your activities, readings and media, and the cohort
session. If you've entered your course start date, you'll also see each activity's due date.

::: module-fields
:::

::: due-dates
:::


::: week-check
:::

::: workload-chart
:::

Checklist (for each module):

- One main activity carries the module's weight.
- Students do something professionals in your field do.
- Each high-weight activity says what AI use is allowed.

### Checks

When you save each module, the tool checks:

- **Alignment:** each activity traces to a CLO the module lists and uses its verb.
- **RSI:** at least two categories of instructor activity, counting the cohort session and
  responsive weekly announcements if your interaction statement promises them.
- **Workload:** the whole week comes close to your weekly target, counting activities, readings and
  media, and the cohort session (about 4 hours in Module 1). A week more than about 1 hour over or
  1.5 hours under is flagged, and so is a module with two major assignments due the same day or one
  activity over about 4 hours.
- **AI risk:** each high-weight activity is rated high, medium, or low, with a suggested change for
  high and medium.
- **Tools:** each third-party tool answers six questions: alignment, feedback quality, academic
  integrity, access, privacy, and your time. Privacy shows "check with your ID" unless the tool is
  approved.

In MGMT 615, the checks flagged Module 1's workload (the sort became optional practice), the
Module 5 Perusall reading for RSI (the instructor added Thursday replies), and Module 8's workload
(the summary's first draft moved to Module 7). They rated three assessments high for AI risk and
suggested the changes shown with each module's draft.

AI instructions (RSI and workload):

```text
For each module, using its saved activities, the syllabus statement (step 2.1), and whether the
module has a cohort session (assume yes for modules 2 to 8 unless told otherwise):
1. Assign each activity an RSI category or null, with a short reason. Auto-graded work and
   student-only activities are null unless the faculty member described instructor involvement.
2. Count the categories the module covers, including the cohort session (4) and responsive weekly
   announcements (3) if the syllabus statement promises them.
3. Total the activity hours.
Flag modules with fewer than two categories, modules with two high-weight activities due the same
day, and any activity over about 4 hours.
For each flag, suggest one specific change. The tool adds readings, media, and the cohort session to
the activity hours and checks the week against the weekly target.

Return: {"modules": [{"module": int, "activities": [{"title": string, "rsi": int | null, "reason": string}], "categories": [int], "hours": number, "flags": [string]}]}
```

AI instructions (AI risk):

```text
For each high-weight activity, judge how easily a student could complete it with a general AI
tool and no course-specific thinking: high, medium, or low. Give a one-sentence reason based on
what the activity asks for. For high and medium, suggest one change that makes the student's own
thinking visible, using their own context, process evidence, a live part, or course-specific
material. Keep the activity's CLO and verb. Do not suggest AI detection tools.

Return: {"assessments": [{"module": int, "activity": string, "risk": "high" | "medium" | "low", "why": string, "change": string | null}]}
```

### Save

Planning document: Learning Activities Plan Part 1 (Canvas) and Part 2 (third-party tools) rows
in Tables 1 and 2, one line per activity, for example "Assignment: Feedback Conversation Script
(CLO 2, high, RSI 2; annotated and rehearsed in cohort session)".
Project file: `modules[].activities` (with `rsi`, `hours`, `aiRisk`, `aiPolicy`, `aiChange`),
`modules[].toolActivities`; in refresh, `.original` and `.changeNote`.

### Go deeper (supplemental)

- `src:reading-m4-crafting-part-1`, `src:reading-m4-crafting-part-2`
- `src:guide-learning-activities`, `src:guide-rubrics`, `src:guide-third-party-tools`
- `src:ext-tamu-ai-guidelines`, `src:ext-terry-2023`
- `src:ext-rice-workload`: estimate student time by reading difficulty and writing type.

---

## 4.3 A week in your student's shoes

Time: about 20 minutes, a few minutes a module
Pattern: a week in your student's shoes

### Learn

::: purpose
**What you'll do:** Read an AI walk-through of each module's week from a student's point of view,
and note what feels heavy, thin, or silent.

**Why it matters:** A plan can pass every check and still feel wrong to a student. Seeing the week
as they'll live it shows problems that numbers miss.
:::

The walk-through follows one of your students through the week: what they open on Monday, what they
read, do, and submit, when they hear from you, and how long it takes. If something needs fixing, go
back to step 4.2.

Readings and media aren't planned yet, so the walk-through uses placeholders for them. It updates
as you plan materials in Module 5 and media in Module 6, and Module 8 shows the full week.

### See it

Here's MGMT 615's Module 3 week as a student would live it, and what the instructor changed.

::: figure week | MGMT 615, Module 3: a student's week
- Mon | **Announcement:** Greg wants a formal warning for Jordan. **Perusall reading:** start annotating the feedback chapter (about 1.5 hours over two days).
- Tue | **Perusall reading:** finish the annotations.
- Wed | **Interactive:** coaching-or-discipline sort (30 minutes).
- Thu | **Instructor reply:** a question in the student's Perusall thread. **Cohort session:** rehearse the opening of the conversation with a partner (90 minutes).
- Fri |
- Sat | **Assignment:** draft the whole feedback script and annotate each line (about 4 hours).
- Sun |
- Note | The heaviest point is Saturday: the whole script in one sitting. The instructor's fix: open the script on Wednesday and make it due Sunday, so students can start it after the cohort session.
:::

### Draft (full build) and Review (refresh)

Select the button below. The AI walks through each module's week as one of your students, then
names the heaviest point, any stretch of three or more days without hearing from you, and anything
a student might not understand the purpose of.

AI instructions:

```text
Walk through the given module's week as one of the course's students, in first person and in
time order, using the learner description, the saved activities, the interaction statement, the
scenario, and a 90-minute cohort session. Use [reading] and [video] placeholders where materials
aren't planned yet. Give rough hours for each part and a total. Then list, in one line each:
the heaviest point in the week, any stretch of three or more days with no contact from the
instructor, and anything a student might not understand the purpose of. Under 200 words.

Return: {"walkthrough": string, "hours": number, "heaviest": string, "silent": string | null, "unclear": string | null}
```

Demo response (MGMT 615):

**Module 3: Performance Management and Feedback**

"Monday, an announcement picks up Dana's story: Greg wants a formal warning for Jordan. Monday and
Tuesday I spend about an hour and a half annotating the feedback chapter in Perusall. Wednesday
night I do the 30-minute coaching-or-discipline sort. Thursday the instructor replies to my
Perusall thread with a question about Jordan, and in the cohort session I rehearse the opening of
the conversation with a partner. Saturday I draft the whole feedback script and annotate why each
line is there, about four hours. I hear from the instructor three times this week."

- **Total:** about 6 hours of activities, plus the 90-minute cohort session.
- **Heaviest point:** Saturday, the whole script in one sitting.
- **Days without contact:** none.
- **Unclear purpose:** none.

### Decide

Note anything you want to change, module by module. These are your own notes, so there's no AI
redraft here. To make a change, go back to step 4.2 and edit that module's activities.

::: fields notes
- Your notes on any week that feels heavy, thin, or silent, one module per line | Module 3: Saturday is the whole assignment. Open the script Wednesday and make it due Sunday.
:::

Checklist:

- No week has one day carrying most of the work.
- Students hear from you at least twice a week.

### Checks

None beyond step 4.2's, which run again when you change any activities.

### Save

Saved with your project. Your notes stay with each module's plan for your ID to see at your
check-in.
Project file: `modules[].weekWalk` (walk-through, hours, reaction).

---

## Check-in prep

Same instructions as Module 1.

Demo response (MGMT 615):

```json
{
  "changed": ["Activities for all eight modules: three main assignments moved onto the storyline", "Module 5 Perusall: instructor replies added", "Module 8: summary draft moved to Module 7", "AI changes for three high-risk assessments"],
  "keptFlags": [],
  "questions": ["Is roughly 6 hours of activities a module the right target for this program?", "Should students be allowed to draft with AI on the change message if they critique the draft?"]
}
```

Project file: `checkins.prep.m4`.
