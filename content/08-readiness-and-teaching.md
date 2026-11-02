# Module 8. Development Readiness and Sustainable Teaching

Module id: `m8`
Steps: 2
ID check-in: live review of the finished plan; the ID then schedules the kick-off meeting

Faculty complete: a final check of the whole planning document, and the communication and
feedback plan.

Refresh checks for this module: the planning document is complete and aligned; announcement and
feedback routines are in place.

Sources: `src:reading-m8-preparing-for-development`, `src:assignment-m8-course-planning-document`,
`src:guide-online-teaching-practices`, `src:guide-grading-weight`, `src:guide-large-enrollment`,
`src:guide-rsi`, `src:example-mgmt615-course-map`

## Refresh reflection

> App note: Shown once, in the refresh track only, before step 8.1. It asks only about how the
> course was taught last time.

::: purpose
**What you'll do:** Answer a few questions about how you communicated with students and gave
feedback the last time you taught the course. Answer whichever apply; short notes are fine.

**Why it matters:** The AI uses your answers when it reviews each section in this module, so its
suggestions reflect what actually happened in your course.
:::

1. How did students hear from you each week, and did it hold up in the busiest weeks?
2. Where did grading and feedback take the most time?
3. What did students say about feedback?
4. Which routines would you keep exactly as they are?

> App note: AI instructions are the same as the Module 1 reflection instruction.

Demo answers (MGMT 615): (1) "Monday announcements, but they slipped mid-term." (2) "The
Management Approach Summary and the memos." (3) "They wanted it faster." (4) "Monday
announcements, when I kept them up."

Project file: `reflection.m8`.

---

## 8.1 Check the whole plan

Time: about 25 minutes
Pattern: edit in place

### Learn

::: purpose
**What you'll do:** Run every check across your whole planning document and fix what it flags,
module by module.

**Why it matters:** Your ID builds the course from this document, and it's much easier to adjust the
plan now than to rebuild a module in development.
:::

The checks run across the whole document at once and show the results by module.

For each module you should be able to point to the story thread: the scenario and its decision,
the activity where students work through it, the materials that prepare them, the media it needs,
and how the cohort session builds on it. If a piece is missing or doesn't connect, fix it now.

Then look at the whole week. With activities, materials, media, and the cohort session all
planned, the week-in-your-student's-shoes walk-through can now show the full week: about 4 hours in
Module 1 and about 10 in the rest.

### See it

MGMT 615's final check found three things. Module 1 came to about 8 hours against a 4-hour
target; the instructor made the sort optional and moved the book chapter to Module 2. The Module 6 thread had no media tied to the scenario;
the instructor noted that the AI teaching video carries the story through the scheduling tool.
And Module 8 still ran heavy at about 11 hours; the instructor cut one reading to supplemental.

### Draft (full build) and Review (refresh)

Same for both tracks. No drafting; the AI runs the checks.

AI instructions:

```text
Check the whole planning document. For each module, confirm the story thread: scenario and
decision; an activity at the decision; materials that prepare students for it; media tied to the
scenario or a note; a cohort session that builds on it. Total the week's hours (activities,
reading at about 6 pages an hour for dense reading, video minutes, 90-minute cohort session) and
flag Module 1 if it is far from about 4 hours, and any other week under 8 or over 11 hours. List every section that is empty or still a placeholder,
and every earlier flag kept without a note. Then list the three most important fixes across the
course, most important first.

Return: {"modules": [{"module": int, "thread": {"scenario": boolean, "activity": boolean, "materials": boolean, "media": boolean, "cohort": boolean}, "hours": number, "flags": [string]}], "missingSections": [string], "unnotedFlags": [string], "topFixes": [string]}
```

Demo response (MGMT 615):

```json
{
  "modules": [
    {"module": 1, "thread": {"scenario": true, "activity": true, "materials": true, "media": true, "cohort": true}, "hours": 8, "flags": ["About 8 hours against a 4-hour target for the first week."]},
    {"module": 6, "thread": {"scenario": true, "activity": true, "materials": true, "media": false, "cohort": true}, "hours": 9.5, "flags": ["No media tied to the scenario 'Twelve Things on Dana's List'."]},
    {"module": 8, "thread": {"scenario": true, "activity": true, "materials": true, "media": true, "cohort": true}, "hours": 11, "flags": ["About 11 hours, the heaviest week."]}
  ],
  "missingSections": [],
  "unnotedFlags": [],
  "topFixes": ["Lighten Module 1 to about 4 hours: make the sort optional and move the book chapter to Module 2.", "Lighten Module 8: move one reading to supplemental.", "Tie a Module 6 media item to Dana's list, or note why none is needed."]
}
```

Modules not listed passed every check.

### Decide

For each flag, Fix (opens the section) or Keep with a note.

Checklist:

- Every module's story thread is complete, or the gap has a note.
- Module 1 is about 4 hours, and every other week about 10.
- No section is empty.

### Checks

This step is the check. Save final version becomes available when no flag is left without a fix
or note.

### Save

Planning document: no new section. The change log (refresh) and check-in summary are complete.
Project file: `alignment.final`.

### Go deeper (supplemental)

- `src:guide-grading-weight`
- `src:guide-large-enrollment`

---

## 8.2 Communication and feedback plan

Time: about 30 minutes
Pattern: interview, then draft (full build) or edit in place (refresh)

### Learn

::: purpose
**What you'll do:** Plan how you'll communicate with students each week: announcements, feedback,
and answers to questions.

**Why it matters:** In a Flex Online course the content does the presenting; your weekly job is to
guide, respond, and give feedback. That's also how you meet RSI week after week.
:::

Plan it now, so it holds up in week ten, not just week one.

**Announcements.** Plan a sequence for each module:

- **Opening:** welcome to the module, where the story stands, the first thing to do.
- **Midpoint:** what you're seeing in student work, and the concept people are missing.
- **Before the cohort session:** what to prepare or bring.
- **Closing:** what the module added up to and the next decision.

The opening and closing can be drafted ahead. The midpoint can't, because it responds to what
students actually did; that's what makes it count as RSI. AI can draft any of them quickly. Edit
each one so it sounds like you and reflects what's happening in your course.

**Feedback.** Students want to know what they did well, what fell short, and what to change, along
with the grade. SpeedGrader's comment library, markup, clickable rubrics, and short audio or video
comments all save time without thinning feedback. If AI drafts comments, read and edit each one
before release. Keep the turnaround your interaction statement promises.

**Questions.** Answer common questions once, in an announcement or the General Q&A discussion, so
everyone sees the answer.

### See it

MGMT 615's plan: Monday opening announcements carry Dana's story; Wednesday midpoints respond to
what the instructor sees in the week's drafts and polls; a short Monday note before each Tuesday
cohort session says what to bring. Feedback on main assignments is within five days: clickable
rubric plus a 2-minute video comment, with a comment library built from the first term's most
common notes. The instructor's reflection said Monday announcements slipped mid-term, so all
opening and closing announcements are drafted before the term and scheduled.

### Draft (full build)

The AI asks three questions, then drafts the plan and the Module 1 announcement sequence:

1. Which format of feedback suits you best: written, audio, or video?
2. Which weeks of the term are your busiest outside the course?
3. Is there anything you already do in announcements that you want to keep?

AI instructions:

```text
From the answers, the interaction statement, the activities, and the scenarios, draft:
1. A communication and feedback plan of 5 to 8 short lines: announcement days, feedback format and
   turnaround for main assignments, how AI drafting will be reviewed, how common questions are
   answered, and how the plan holds in the faculty member's busiest weeks.
2. The Module 1 announcement sequence: opening, midpoint (as a template with [what I'm seeing]
   placeholders, since it must respond to real work), before-session note, closing. Each under
   120 words, in the faculty member's voice, carrying the story forward.
Keep every commitment consistent with the interaction statement.

Return: {"plan": [string], "announcements": [{"type": string, "day": string, "text": string}]}
```

Demo response (MGMT 615): the plan under See it, and a Module 1 opening announcement:
"Welcome to MGMT 615. This week you meet Dana Ortiz, eight months into running a distribution
center, with on-time shipping down eight points and a director who's already decided whose fault
it is. Start with her Monday report and the Whitfield chapter, then join us Tuesday at 6:00,
where you'll decide what Dana should do with her first week."

### Review (refresh)

Edit in place. Existing announcements, feedback practices, and communication notes from the upload
are checked against the interaction statement and the Learn section; the reflection points the
AI at what slipped.

Demo response (MGMT 615): the course map has no communication plan, so the full build runs. The
reflection note about announcements slipping mid-term adds the line "Opening and closing
announcements drafted before the term and scheduled."

### Decide

Checklist:

- The plan matches your interaction statement.
- Midpoint announcements respond to real student work.
- You can keep it up in your busiest weeks.

### Checks

On save: every commitment matches the interaction statement (days and turnaround); each module
has an opening and a closing announcement planned; AI-drafted feedback has a review step.

### Save

Planning document: the communication and feedback plan, added to the Instructor Interaction
section under the syllabus statement.
Download: the Module 1 announcement sequence as a Word file. There's nothing to fill out or submit; it's there to show and share.
Project file: `communication.plan`, `communication.announcements`.

### Go deeper (supplemental)

- `src:reading-m8-preparing-for-development`
- `src:guide-online-teaching-practices`
- `src:guide-rsi`

---

## Check-in prep and finish

Same instructions as Module 1, with one addition: the app offers Save final version once step 8.1
has no open flags. The final version leaves out the check-in summary and, if the faculty member
chooses, the change log. The faculty member saves it to the shared folder, and the ID schedules
the kick-off meeting.

Demo response (MGMT 615):

```json
{
  "changed": ["Final check: Modules 1 and 8 lightened, Module 6 media noted", "Communication and feedback plan", "Module 1 announcement sequence"],
  "keptFlags": ["Module 6 has no scenario media: the AI teaching video carries the story"],
  "questions": ["Which scenario videos should be produced first?", "Can the comment library be set up in the development shell before the term?"]
}
```

Project file: `checkins.prep.m8`.
