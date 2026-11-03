# Module 7. Cohort Session Planning

Module id: `m7`
Steps: 2
ID check-in: live review of this module's sections, at the end of the week or sooner

Faculty complete: a cohort session for each of Modules 2 to 8, planned as a decision point, and the
first session ready to broadcast from the XR stage.

Refresh checks for this module: each cohort session passes the recording test.

Sources: `src:reading-m7-going-live`, `src:reading-m7-active-learning-tools`,
`src:assignment-m7-cohort-planning`, `src:assignment-m7-cohort-materials`,
`src:guide-cohort-sessions`, `src:template-cohort-lesson-plan`, `src:template-run-of-show`, `src:example-mgmt615-course-map`

Demo data: `demo/mgmt615-cohort.json`

## Refresh reflection

> App note: Shown once, in the refresh track only, before step 7.1. It asks only about sessions the
> course has already run.

::: purpose
**What you'll do:** Answer a few questions about the cohort sessions in the last version of your
course. Answer whichever apply; short notes are fine.

**Why it matters:** The AI uses your answers when it reviews each section in this module, so its
suggestions reflect what actually happened in your course.
:::

1. Which sessions drew the most students, and which the fewest?
2. When did the room go quiet, and when was it hard to stop the conversation?
3. What do students say about the sessions?
4. Which sessions would you keep exactly as they are?

> App note: AI instructions are the same as the Module 1 reflection instruction.

Demo answers (MGMT 615): (1) "The role-plays and the mock interview. The roundtables in Modules 2
and 4 were thin." (2) "Quiet when I asked open questions to the whole room." (3) "They like the
breakouts." (4) "The mock interview panel."

Project file: `reflection.m7`.

---

## 7.1 Cohort sessions for Modules 2 to 8

Time: about 40 minutes, about 5 minutes a module
Pattern: pick and combine, one module at a time (full build); edit in place (refresh)

### Learn

::: purpose
**What you'll do:** Plan a cohort session, a 90-minute live class on Zoom, for each of Modules 2 to
8, with at least one part students can only get by being there.

**Why it matters:** Students don't skip sessions because they're recorded; they skip sessions that
offer nothing the recording doesn't (Morris et al., 2019).
:::

Flex Online courses hold one cohort session each week from Module 2 to Module 8; Module 1 has none.
Attendance is optional and every session is recorded, so students decide each week whether to come
or watch later.

**The recording test.** Ask: if a student watched only the recording, what would they have
missed? If the answer is nothing, they'll watch it later. A session passes when at least one
part depends on who's in the room. Students get five things live that a recording can't give
them:

| What students get live | What it looks like |
|---|---|
| Feedback on their own work | Students bring a draft of the next assignment and get responses |
| Applying the concept to their own job | Students map the week's framework onto a problem at work |
| Practice with peers | Students rehearse a conversation, pitch, or negotiation in breakouts |
| Your judgment on a messy case | You work through a case with no clean answer and explain your reasoning |
| A preview of the next assessment | Students work a problem shaped like the next assignment with you there |

**A shape that works.** Most sessions follow the same four steps:

1. **Check understanding (about 10 minutes).** Open with a poll or a few chat questions on the
   week's main concepts. It shows you what students took from the materials, and you can clear up
   a misunderstanding before it spreads. Keep it short; don't re-teach the reading.
2. **Guided practice (about 15 minutes).** Work one example with the class. You lead, students
   supply the next step or the next move, and you coach as they go.
3. **The live part (most of the session).** Students practice or decide in small groups: the part
   a recording can't give them.
4. **Debrief and preview.** Groups share, you add your judgment, and you point to what's due next.

Lecturing on new material belongs in the asynchronous content.

**Your story as a live decision.** Let the week's materials carry the scenario up to the
decision, then stop. The session is where students make the call: vote on the character's
options and argue the split, role-play the hard conversation in threes (one observer gives
hesitant students a way in), or give each group a different piece of evidence so the picture
only comes together in the debrief.

**Quiet rooms.** Over a third of distance learners feel stressed when asked to participate live
(Donelan et al., 2025). The check for understanding eases them in: start with a poll or the chat,
then small groups, then the whole room.

**RSI.** A session built this way is facilitated discussion (category 4) every week, often with
feedback (2) or direct instruction (1) as well.

**Your Instructional Technologist** runs Zoom, polls, breakouts, captions, and timers, if they know
the plan. Note poll wording, breakout sizes and timing, and anything to drop in the chat.

### See it

::: full
Here's the session the MGMT 615 instructor planned for Module 5. It passes the recording test:
students who only watch the recording miss the role-play itself.
:::

::: refresh
Here's MGMT 615's Module 5 session, which passed the review as it was. The Module 2 and 4
roundtables didn't: nothing in them depended on who was in the room, so each got a live moment.
:::

::: plan Cohort Session, Module 5
- Telling Greg He's Wrong. Decision: how Dana answers her director.
- What students get live: practice with peers.
- 10 min: check understanding: the week's Poll Everywhere results, plus one question on the root causes of disagreement
- 15 min: guided practice: the instructor and a volunteer play the opening exchange, and the class coaches Dana's next line
- 40 min: role-play in threes (Dana, Greg, and an observer), three rounds
- 20 min: two volunteers replay their conversation for the class; instructor feedback
- 5 min: preview of the memo to Greg
- Setup: show the poll results; breakouts of three; observer checklist in the chat.
:::

### Draft (full build) and Review (refresh)

Work through Modules 2 to 8 one at a time. Choose a module, then select the button below. The AI
proposes a session built on the module's scenario and activities, with what the checks will find.
Select **Use this session** to copy it into the box under Decide.

::: refresh
The AI starts from your Course Map's current session for the module. It applies the recording test,
says what it would keep or revise and why, and adds a live moment where one is missing.
:::

::: module-picker
:::

::: full
AI instructions:

```text
For the given module, using its scenario, activities, and the learner profile, propose a 90-minute
cohort session. Give: a title; the decision it centers on; which of the five live benefits it
offers (feedback on own work, own job, practice with peers, instructor judgment, assessment
preview); 4 or 5 timed segments that open with a quick check for understanding of the week's main
concepts (a poll or the chat), then guided practice the instructor leads, then small groups;
the RSI categories it shows; and setup needs for the Instructional Technologist (poll wording,
breakout sizes and timing, chat links). It must pass the recording test: name the moment that
depends on who is in the room.

Return: {"title": string, "decision": string, "live": string, "segments": [string], "rsi": [int], "setup": [string], "liveMoment": string}
```
:::

::: refresh
AI instructions:

```text
For the module's current cohort session, apply the recording test: name what a student who watched
only the recording would miss, or say "nothing." Check it connects to the module's scenario or
activities, opens with a check for understanding and guided practice before small groups, and
gives the Instructional Technologist enough to set up. Use the
faculty member's reflection on attendance and quiet moments. Suggest keep or revise; for a
revision, keep the session's purpose and add one live moment.

Return: {"original": string, "missed": string, "action": "keep" | "revise", "issues": [string], "revision": {...same shape as full build...} | null}
```
:::

Demo response (MGMT 615):

::: module-options
:::

### Decide

Your final session for each module goes in this box. Type in it to change anything, or select
**Redraft with AI** under it to have the AI rewrite it. To work on another module, choose it above;
what you've typed is kept.

Give the title and the decision, what students get live, each segment with its minutes, and the
setup your Instructional Technologist needs. The minutes should add up to 90.

::: module-fields
:::

Checklist:

- You can name what a student watching the recording would miss.
- The session opens with a check for understanding, then guided practice.
- Setup needs are clear enough for your Instructional Technologist.

### Checks

When you save each module, the tool checks that:

- the session passes the recording test;
- it ties to the module's scenario or activities;
- it opens with a check for understanding (a poll or the chat), then guided practice;
- it shows at least one RSI category;
- the segments add up to about 90 minutes.

The week walk-through in step 4.3 then includes the session.

### Save

Planning document: Learning Activities Plan Part 3 (Cohort Session Activities) row in Tables 1
and 2, for example "Telling Greg He's Wrong: role-play in threes after a week-long poll."
Project file: `modules[].cohort`; in refresh, `.original`, `.changeNote`.

### Go deeper (supplemental)

- `src:reading-m7-going-live`: the research behind the recording test, and eight ways to use
  your story live.
- `src:reading-m7-active-learning-tools`
- `src:guide-cohort-sessions`

---

## 7.2 Ready for the stage

Time: about 30 minutes
Pattern: interview, then draft

### Learn

::: purpose
**What you'll do:** Turn your first cohort session, usually Module 2, into a lesson plan, and list
the background and assets the production team needs to broadcast it from the XR stage.

**Why it matters:** Cohort sessions are broadcast live from the XR stage. Your lesson plan keeps you
on time, and the team uses your background and assets to set up the stage, Zoom, polls, and
breakouts before you go live.
:::

Two documents get a session ready:

- **Cohort Session Lesson Plan:** your plan. Each section has its minutes and its talking points,
  activities, and setup details, followed by the materials, handouts, and room setup you need. You
  write it.
- **XR Run of Show:** the production team's plan for the day: call times, who's on the crew, a
  pre-show checklist, and a backup plan. It sets the order of the session but leaves your teaching
  unscripted. You give the team two things for it: your **background environment** and your
  **session assets**, such as slides, polls, and handouts, in the order you'll use them.

**Keep it simple.** Choose one background with the Learning Media Team; the one you chose for your
videos works well. Teach with slides, and post handouts in Canvas so a link can go in the chat.

**On the day.** Arrive at the call time the team gives you for a mic check and a walkthrough. Look
at the camera lens when you speak to students; a confidence monitor shows your slides and notes.
The team gives you time signals, and your Instructional Technologist runs Zoom, so you can focus on
teaching.

Before your first session, schedule a practice session on the stage with Learning Delivery. It's
the time to try the polls and breakouts, find where to look, and get comfortable with the setting.

Keep slides accessible: readable contrast, real text instead of text in images, and nothing
important only on a slide. During development you'll plan the rest of your sessions with your ID,
along with a student-facing outline for each.

### See it

Here's MGMT 615's Module 5 session as a lesson plan, with what the instructor gave the production
team.

| Duration | Section | Subtopics, Talking Points, and Other Details |
|---|---|---|
| 10 | Introduction | Check understanding: show the week's Poll Everywhere results (how should Dana answer Greg?), then one poll question on the root causes of disagreement. Clear up any mix-ups. |
| 15 | Topic 1: Guided practice | The instructor plays Greg and a volunteer plays Dana for the opening exchange. The class coaches Dana's next line in the chat. |
| 40 | Topic 2: Role-play in threes | Breakouts of three: Dana, Greg, and an observer. Three rounds of about 13 minutes, so everyone plays each role. The observer notes the strongest line they hear. |
| 20 | Topic 3: Replay | Two volunteers replay their conversation for the class. Instructor feedback on what moved Greg, and what didn't. |
| 3 | Conclusion | Preview the memo to Greg due Sunday: put the strongest line from today in writing. |
| 2 | Buffer | Questions from the room, then close. |

**Background environment:** Virtual podcast studio, the same one as the course videos.

| Order | Name | Asset Type | Link (Slides in Canvas) |
|---|---|---|---|
| 1 | Module 5 cohort session slides | Slides | Module 5 cohort session page in Canvas |
| 2 | How should Dana answer Greg? | Poll results (Poll Everywhere) | Shown from the week's poll |
| 3 | Root causes of disagreement | Poll (Zoom) | Loaded by the Instructional Technologist |
| 4 | Observer checklist | Handout | Module 5 page in Canvas, linked in the chat |

### Draft (full build) and Review (refresh)

Answer the questions, then select the button below. The AI turns your saved session into a lesson
plan and a list of session assets. Select **Use this plan** to copy them into the forms under
Decide.

::: refresh
If you already have a lesson plan or run of show for this session, paste it into the last box. The
AI checks it against the same instructions and suggests edits instead of starting over.
:::

::: fields
- Which session are you preparing? | Module 2, the first session students attend.
- Is there a point where you'll need help from your Instructional Technologist that isn't obvious? | Regrouping the breakouts halfway through, so each new group has all three pieces of evidence.
- How do you want to end? | With my own call on the bonus, after two groups share theirs.
- Your current lesson plan or run of show for this session, if you have one
:::

AI instructions:

```text
Turn the saved cohort session for the chosen module into a Cohort Session Lesson Plan: rows with
the duration in minutes, the section (Introduction, Topic 1, Topic 2, and so on, then Conclusion),
and the subtopics, talking points, and other details (what the instructor says or asks, what
students do, and setup such as poll wording and options, breakout size and length, and chat
links). Durations total 90 minutes and include a two-minute buffer before the close. Then list the
materials, handouts, and room setup. Then list the session assets for the XR Run of Show, in the
order they're used, each with a name, an asset type (slides, poll, handout, video), and where it
lives. Use the faculty member's answers. If they pasted a current plan, check it against these
instructions and suggest edits instead of starting over.

Return: {"module": int, "rows": [{"minutes": number, "section": string, "details": string}], "preparation": string, "assets": [{"name": string, "type": string, "link": string}]}
```

Demo response (MGMT 615):

| Duration | Section | Subtopics, Talking Points, and Other Details |
|---|---|---|
| 10 | Introduction | Welcome. Check understanding with a poll: which link in expectancy theory does the pick-rate bonus break? Clear up any mix-ups, then recap Dana's situation. |
| 15 | Topic 1: Guided practice | Diagnose Luis together. The instructor walks through his record; students name the motivation problem in the chat, and the instructor coaches toward the evidence. |
| 25 | Topic 2: Split evidence | Breakouts of three. Each group gets one piece of evidence: the bonus data, Luis's record, or the crew's view. Timer on screen. |
| 25 | Topic 3: Recommend | Regroup so each new group holds all three pieces of evidence. Groups recommend keeping, adjusting, or replacing the bonus, with one reason from each piece. |
| 13 | Conclusion | Two groups share their recommendation, then the instructor's own call and why. Preview the motivation diagnosis due Sunday. |
| 2 | Buffer | Last questions, then close. |

**Materials, handouts, and room setup:** Slides; a concept-check poll; three evidence handouts, one
per group. Breakouts of three for 25 minutes, then regrouped breakouts of three for 25 minutes, with
a timer for each round.

| Order | Name | Asset Type | Link (Slides in Canvas) |
|---|---|---|---|
| 1 | Module 2 cohort session slides | Slides | Module 2 cohort session page in Canvas |
| 2 | Which link does the bonus break? | Poll (Zoom) | Loaded by the Instructional Technologist |
| 3 | Evidence A: the bonus data | Handout | Module 2 page in Canvas, linked in the chat |
| 4 | Evidence B: Luis's record | Handout | Module 2 page in Canvas, linked in the chat |
| 5 | Evidence C: the crew's view | Handout | Module 2 page in Canvas, linked in the chat |

### Decide

Make the plan yours in the forms below. They follow the team's Cohort Session Lesson Plan and the
faculty part of the XR Run of Show. Type in any box to change it, add a row when you need one, or
select **Redraft with AI** under a form to have the AI rewrite it. The total under the lesson plan
shows whether the minutes add up to 90.

::: grid lesson
:::

::: fields
- Materials, handouts, and room setup
- Background environment, chosen with the Learning Media Team
:::

::: grid assets
:::

Checklist:

- The minutes add up to 90, with a short buffer before the close.
- Every poll has its exact wording and options.
- You've chosen a background with the Learning Media Team.
- You've asked to schedule a practice session on the XR stage with Learning Delivery.

### Checks

When you save, the tool checks that:

- the lesson plan totals 90 minutes;
- every poll and breakout has its setup details;
- a background is named, and the slides are listed as an asset.

### Save

Planning document: nothing new; the session's line gains "lesson plan drafted."
Download: the lesson plan as a Word file in the Cohort Session Lesson Plan template, and your
background and session assets for the XR Run of Show, to share with your ID, the Learning Media
Team, and Learning Delivery. There's nothing to fill out or submit; it's there to show and share.
Project file: `lessonPlans[]` (module, rows, preparation, background, assets).

### Go deeper (supplemental)

- `src:guide-cohort-sessions`
- `src:template-cohort-lesson-plan`
- `src:template-run-of-show`

---

## Check-in prep

Same instructions as Module 1.

Demo response (MGMT 615):

```json
{
  "changed": ["Cohort sessions for Modules 2 to 8", "Module 2 and 4 roundtables given a live moment", "Module 2 lesson plan, background, and session assets drafted"],
  "keptFlags": [],
  "questions": ["When can I practice on the XR stage before the first session?", "Can the Instructional Technologist show the week's Poll Everywhere results at the start of Module 5?"]
}
```

Project file: `checkins.prep.m7`.
