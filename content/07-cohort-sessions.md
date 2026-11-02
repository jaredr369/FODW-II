# Module 7. Cohort Session Planning

Module id: `m7`
Steps: 2
ID check-in: live review of this module's sections, at the end of the week or sooner

Faculty complete: a cohort session for each of Modules 2 to 8, planned as a decision point, and the
first session ready to broadcast from the XR stage.

Refresh checks for this module: each cohort session passes the recording test.

Sources: `src:reading-m7-going-live`, `src:reading-m7-active-learning-tools`,
`src:assignment-m7-cohort-planning`, `src:assignment-m7-cohort-materials`,
`src:guide-cohort-sessions`, `src:template-run-of-show`, `src:example-mgmt615-course-map`

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

Flex Online courses hold one each week from Module 2 to Module 8; Module 1 has none. Attendance is
optional and every session is recorded, so students decide each week whether to come or watch later.

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

Reviewing the reading or lecturing on new material belongs in the asynchronous content.

**Your story as a live decision.** Let the week's materials carry the scenario up to the
decision, then stop. The session is where students make the call: vote on the character's
options and argue the split, role-play the hard conversation in threes (one observer gives
hesitant students a way in), or give each group a different piece of evidence so the picture
only comes together in the debrief.

**Quiet rooms.** Over a third of distance learners feel stressed when asked to participate live
(Donelan et al., 2025). Start with a poll or the chat, then small groups, then the whole room.

**RSI.** A session built this way is facilitated discussion (category 4) every week, often with
feedback (2) or direct instruction (1) as well.

**Your Instructional Technologist** runs Zoom, polls, breakouts, captions, and timers, if they know
the plan. Note poll wording, breakout sizes and timing, and anything to drop in the chat.

### See it

MGMT 615 Module 5, "Telling Greg He's Wrong": students voted on Poll Everywhere during the week on
how Dana should answer her director. The session opens with the split, runs 45 minutes of
role-play in threes (Dana, Greg, observer), then two volunteers replay their conversation for the
class and get the instructor's feedback.

### Draft (full build)

AI instructions:

```text
For the given module, using its scenario, activities, and the learner profile, propose two
versions of a 90-minute cohort session. Each gives: a title; the decision it centers on; which
of the five live benefits it offers (feedback on own work, own job, practice with peers,
instructor judgment, assessment preview); 3 to 5 timed segments that start low-stakes (poll or
chat) before small groups; the RSI categories it shows; and setup needs for the Instructional
Technologist (poll wording, breakout sizes and timing, chat links). It must pass the recording
test: name the moment that depends on who is in the room.

Return: {"versions": [{"title": string, "decision": string, "live": string, "segments": [string], "rsi": [int], "setup": [string], "liveMoment": string}]}
```

Demo response (MGMT 615, if run as a full build): each module from `demo/mgmt615-cohort.json`.

### Review (refresh)

Edit in place. The app lists each module's current session from the upload.

AI instructions:

```text
For each current cohort session, apply the recording test: name what a student who watched only
the recording would miss, or say "nothing." Check it connects to the module's scenario or
activities, starts low-stakes, and gives the Instructional Technologist enough to set up. Use
the faculty member's reflection on attendance and quiet moments. Suggest keep or revise; for a
revision, keep the session's purpose and add one live moment.

Return: {"sessions": [{"module": int, "original": string, "missed": string, "action": "keep" | "revise", "issues": [string], "revision": {...same shape as full build...} | null}]}
```

Demo response (MGMT 615): `review` notes in `demo/mgmt615-cohort.json`. The Module 2 and 4
roundtables failed the recording test, matching the reflection that they were thin; both got a
live moment.

### Decide

Checklist (for each module):

- You can name what a student watching the recording would miss.
- The session starts with something low-stakes.
- Setup needs are clear enough for your Instructional Technologist.

### Checks

On save of each module: passes the recording test; ties to the module's scenario or activities;
starts with a poll, chat, or small group; shows at least one RSI category; segments total about 90
minutes. The week-in-your-student's-shoes walk-through refreshes with the session.

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

Time: about 25 minutes
Pattern: interview, then draft

### Learn

::: purpose
**What you'll do:** Draft the run of show for your first cohort session: a minute-by-minute plan for
the people who run the session with you.

**Why it matters:** Sessions are broadcast live from the XR stage. The run of show is how Learning
Delivery and your Instructional Technologist set up polls, breakouts, and slides before you go live.
:::

The run of show is a preparation template. It lists what happens minute by minute: segments, slides,
polls, breakouts, and anything that goes in the chat. You'll have 30 minutes of setup before each
session.

Before your first session, schedule a practice session on the stage with Learning Delivery. It's
the time to try the polls and breakouts, find where to look, and get comfortable with the
setting.

During development you'll do the rest with your ID, along with slides and a student-facing outline.
Keep slides accessible: readable contrast, real text instead of text in images, and nothing
important only on a slide.
### See it

MGMT 615's Module 2 run of show, first rows:

| Time | Segment | What happens | Setup |
|---|---|---|---|
| 0:00 | Welcome | Instructor greets the class and recaps Dana's situation: the bonus, the error rates, and Luis | Slide 1 |
| 0:10 | Split evidence | Breakouts of three. Each group gets one piece of evidence: the bonus data, Luis's record, or the crew's view | Three breakout handouts; 30 minutes, with a timer |
| 0:40 | Recommend | Groups combine their evidence and recommend: keep, adjust, or replace the bonus | Regroup breakouts; 35 minutes |

### Draft (full build) and Review (refresh)

The AI asks which session to prepare (usually Module 2, the first session students attend) and two
questions: "Is there a point where you'll need help from your Instructional Technologist that
isn't obvious?" and "How do you want to end?"

AI instructions:

```text
Turn the saved cohort session for the chosen module into a run of show: rows with start time,
segment, what happens (what the instructor says or asks and what students do) and setup needs
(slides, poll with exact wording and options, breakout size and duration, chat links, timers).
Total 90 minutes. Include a two-minute buffer before the close. Use the faculty member's answers.

Return: {"module": int, "rows": [{"time": string, "segment": string, "happens": string, "setup": string}]}
```

Refresh track: an existing run of show or lesson plan can be uploaded and checked against the
same instructions.

Demo response (MGMT 615): the Module 2 run of show, opening as under See it.

### Decide

Checklist:

- The minutes add up to 90.
- Every poll has its exact wording and options.
- You've asked to schedule a practice session on the XR stage with Learning Delivery.

### Checks

On save: total time is 90 minutes; every poll and breakout has its setup details.

### Save

Planning document: nothing new; the session's line gains "run of show drafted."
Download: the run of show as a Word file, to share with Learning Delivery and your Instructional
Technologist. There's nothing to fill out or submit; it's there to show and share.
Project file: `runOfShow[]`.


---

## Check-in prep

Same instructions as Module 1.

Demo response (MGMT 615):

```json
{
  "changed": ["Cohort sessions for Modules 2 to 8", "Module 2 and 4 roundtables given a live moment", "Module 2 run of show drafted"],
  "keptFlags": [],
  "questions": ["When can I practice on the XR stage before the first session?", "Can the Instructional Technologist show the week's Poll Everywhere results at the start of Module 5?"]
}
```

Project file: `checkins.prep.m7`.
