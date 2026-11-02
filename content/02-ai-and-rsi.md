# Module 2. AI & RSI in Strategic Course Design

Module id: `m2`
Steps: 2
ID check-in: live review of this module's sections, at the end of the week or sooner

Faculty complete: the syllabus statement on how and when students hear from the instructor, and
the course character and conflict.

Refresh checks for this module: a throughline exists, or could come from cases the course
already uses; the syllabus says when students hear from the instructor.

No refresh reflection in this module. The character and conflict are new work for nearly every
course. Module 4 checks RSI for every module's activities.

Sources: `src:guide-rsi`, `src:assignment-m2-understanding-rsi`,
`src:assignment-m2-character-conflict`, `src:guide-storytelling`, `src:example-mgmt615-character`,
`src:example-mgmt615-course-map`

---

## 2.1 Your interaction statement

Time: about 20 minutes
Pattern: interview, then draft (full build) or edit in place (refresh)

### Learn

Every Flex Online course has to show that the instructor is actively teaching. The federal term
is regular and substantive interaction (RSI). A course that can't show it is treated as a
correspondence course, and its students lose eligibility for federal financial aid. TLI checks
for it in every course review.

**Substantive** means about teaching, learning or assessment: an announcement explaining the
concept half the class missed counts; a due-date reminder doesn't. **Regular** means
predictable, proactive and responsive to how students are doing. Your syllabus has to say how and
when students will hear from you. That statement is what you write in this step.

For the substantive test, your course needs instructor activity in at least two of these five
categories:

| Category | Counts | Doesn't count on its own |
|---|---|---|
| 1. Direct instruction | Your recorded lectures, worked examples you narrate, case debriefs, guided questions | Third-party videos with no framing or follow-up, reading lists with no instructions, quizzes graded only automatically |
| 2. Assessing or giving feedback | Comments on graded work, audio or video feedback, feedback on drafts, peer review you oversee, AI-drafted feedback you review and edit | Scores only, generic comments such as "good job", peer grading you never see, AI feedback you didn't review |
| 3. Giving information or answering questions | Announcements that clear up a hard concept, content answers by email or in forums, module orientation videos that explain how the content fits together, Q&A sessions about content | Deadline reminders, automated messages, welcome videos with no later engagement, forums where only students answer |
| 4. Facilitating discussion | Follow-up questions, summaries that connect posts to the readings, live sessions about content | Posting a prompt and grading replies with no comment, office hours used only for logistics |
| 5. Other instructional activities | Feedback on journals, simulations you debrief, debriefs after group projects | Reflections nobody reads, simulations nobody discusses |

Most of the right-hand column isn't bad teaching. A good industry video helps students learn.
So does an auto-graded practice quiz. They count as RSI once you add your own engagement, such
as a two-minute introduction on what to watch for and a follow-up on what students noticed. The
fix often takes about ten minutes.

**Where AI fits.** AI can draft feedback, summarize discussion threads or flag students who have
gone quiet. The interaction counts when you review and adjust what goes to students. Feedback an
AI writes and you release unread does not. As AI takes on more of the explaining, what students
need most from you is the judgment it can't supply: framing the problem, weighing evidence,
and telling them where their reasoning went wrong (Maxwell, 2026).

You don't need to sort your activities into these categories now. Module 4 does that
automatically for every module.

### See it

MGMT 615's statement: "Every Monday I'll post an announcement that picks up Dana's story, names
the week's decision and responds to what I saw in your last assignment. You'll get written
feedback on each module's main assignment within five days of the due date. I check activity
every Wednesday, and if you've missed a module's work, I'll contact you that week."

### Draft (full build)

The AI asks three questions, then drafts:

1. In a normal week, when and how will students hear from you?
2. How soon will students get feedback on their main assignment each module?
3. How will you notice a student falling behind, and what will you do?

AI instructions:

```text
Draft a syllabus statement of 2 or 3 sentences from the faculty member's answers. It must name
how students hear from the instructor, on which days or within what time, and how the instructor
notices and responds when a student falls behind. Use only commitments the faculty member
described or that follow directly from them. If something is missing, add it and mark it [check]
so the faculty member confirms it.

Return: {"statement": string, "added": [string]}
```

Demo response (MGMT 615), from the answers "Weekly announcement and the cohort session," "Within
five days," and "I'm not sure":

```json
{
  "statement": "Every Monday I'll post an announcement that picks up Dana's story, names the week's decision and responds to what I saw in your last assignment. You'll get written feedback on each module's main assignment within five days of the due date. I check activity every Wednesday, and if you've missed a module's work, I'll contact you that week [check].",
  "added": ["Wednesday activity check and outreach to students who miss work, since your answer didn't say how you'd notice a student falling behind."]
}
```

### Review (refresh)

Edit in place. If the upload has a statement about instructor contact, it appears with flags and
one suggested revision that keeps the faculty member's commitments. If not, the full build runs.

Demo response (MGMT 615): no statement in the course map, so the full build runs.

### Decide

Checklist:

- You can keep this up during the busiest week of the term.
- Anything marked [check] is confirmed or removed.

### Checks

On save: names how students hear from you; names days or turnaround times ("regularly" and
"promptly" are flagged); says how you notice and respond when a student falls behind.

### Save

Planning document: Instructor Interaction (near the end; see `export.md`). Module 8 adds the
communication and feedback plan to the same section.
Project file: `rsi.statement`; in refresh, `rsi.original`, `rsi.changeNote`.

### Go deeper (supplemental)

- `src:guide-rsi`: full tables for each category, and the rules behind them.
- `src:article-maxwell-2026`: what students need from a professor once AI can explain the
  content. About 9 minutes.

---

## 2.2 Character and conflict

Time: about 30 minutes
Pattern: interview, then pick and combine, then draft

### Learn

The rest of the workshop builds a story through your course: a character who faces a decision
in each module. A story earns its place when it gives busy professionals a reason to care about
a concept now, and a place to file what they learn (Mayer, 2021).

Start with the performance: one sentence, from a CLO, saying what students should be able to do.
Then the conflict that makes it hard, pushing directly against it: conflicting goals, ambiguous
data, misaligned incentives or time pressure. If more information would settle it, it isn't a
conflict yet.

Then the character: someone in a role your students could hold within a few years, with enough
authority to feel the decision, facing the constraints your students face. The profile has a
premise statement ("A story about [name, role] who struggles to [performance] when
[conflict]."), position, conflict, two to four peers who see the problem differently, values and
fears, and a short backstory.

If one character doesn't fit your course, you can rotate characters within one setting, keep one
recurring problem, or use a narrator. Your ID reviews the character at this module's check-in,
before Module 3 builds scenarios on it.

### See it

MGMT 615's performance: "Diagnose why a team is underperforming before choosing a fix" (CLO 1).
The conflict: the quick fix against the right fix. Six weeks before peak season, a director has
already blamed one shift lead, while the evidence points to a speed bonus and a shift handoff
nobody owns.

MGMT 615's premise statement: "A story about Dana Ortiz, a newly promoted operations manager at a
regional distribution center, who struggles to find the real causes of her site's slipping
performance and coach, delegate, communicate and hire her way to a fix when leadership has
already decided who to blame."

Dana leads three shift leads and about 45 associates. She was promoted eight months ago from
top-performing day-shift lead, and this is her first time managing managers. Her peers each see
the problem differently. Her night-shift lead agrees with the director, partly because the
broken handoff makes night shift look good. Her day-shift lead, Jordan, is capable but avoids
hard calls and is getting defensive. A manager at a sister site has the data that shows the
handoff problem but thinks Dana should replace Jordan anyway. Dana values fairness and remembers
what it was like to be managed badly. She fears pushing back on her director and being wrong.

### Draft (full build)

Two AI calls. First the AI asks "Which CLO names the decision your students will face most
often?" and "Describe a moment from your field where a capable professional got this decision
wrong, or nearly did," then offers performance and conflict pairs to pick from. Then it drafts
the profile from the chosen pair.

Performance and conflict, AI instructions and demo:

AI instructions:

```text
From the CLOs, the learner profile and the faculty member's answers, propose two or three
performance and conflict pairs for a course storyline. Each performance is one sentence tied to
a named CLO. Each conflict pushes directly against that performance and is a judgment problem,
not missing information. Prefer pairs that can recur across most modules. For each pair, list
the CLOs the conflict would put pressure on.

Return: {"pairs": [{"performance": string, "clo": string, "conflict": string, "closTouched": [string]}]}
```

Demo response (MGMT 615, if run as a full build):

```json
{
  "pairs": [
    {"performance": "Diagnose why a team is underperforming before choosing a fix.", "clo": "CLO 1", "conflict": "Six weeks before peak season, the director has already blamed one shift lead. The evidence points to a speed bonus and an unowned shift handoff, which take longer to fix and mean questioning the director.", "closTouched": ["CLO 1", "CLO 2", "CLO 3", "CLO 4", "CLO 5", "CLO 6"]},
    {"performance": "Justify a delegation call under time pressure.", "clo": "CLO 4", "conflict": "A new manager who was promoted for fixing problems personally is now the bottleneck, and handing work off risks a visible failure in her first year.", "closTouched": ["CLO 3", "CLO 4", "CLO 6"]}
  ]
}
```

Character profile, AI instructions and demo:

Both tracks draft the character from scratch unless the uploaded document already has one. If
it does, the refresh track checks it with the instructions under Review.

AI instructions (draft):

```text
Draft a character profile from the chosen performance and conflict , the CLOs and the
learner profile. Include: premise statement in the form "A story about [name, role] who
struggles to [performance] when [conflict].", position (title, organization type, team size,
experience), conflict (specific to this person), 2 to 4 peers with contrasting views of the
problem, 2 or 3 values, 2 or 3 fears, and 3 or 4 backstory points. The role must be one the
students could hold within a few years. The conflict must force the character to use the skills
in the CLOs. Avoid real company names. Keep the whole profile under 400 words.

Return: {"premise": string, "position": [string], "conflict": string, "peers": [{"name": string, "role": string, "view": string}], "values": [string], "fears": [string], "backstory": [string]}
```

AI instructions (refresh, when a character exists):

```text
The faculty member's existing character or recurring case is given. Check it against this
checklist: realistic role students could hold soon; enough authority to feel the decision;
faces constraints students will face; conflict pushes against a CLO-based performance; stakes
are visible; more than one reasonable option. Keep what passes. For each gap, quote the
problem and suggest a specific addition. Then fill any missing profile parts.

Return: {"passes": boolean, "issues": [string], "profile": {...same shape as draft...}}
```

Demo response (MGMT 615): the course map has no character, so this step runs as a full build.

```json
{
  "premise": "A story about Dana Ortiz, a newly promoted operations manager at a regional distribution center, who struggles to find the real causes of her site's slipping performance and coach, delegate, communicate and hire her way to a fix when leadership has already decided who to blame.",
  "position": [
    "Operations manager, regional distribution center for a mid-size home-goods retailer",
    "Leads 3 shift leads and about 45 hourly associates across two shifts; reports to a regional director",
    "9 years in operations; promoted 8 months ago from top-performing day-shift lead; first time managing managers"
  ],
  "conflict": "Six weeks before peak season, on-time shipping has dropped from 97% to 89%. Her director, Greg Halvorsen, has named the cause: \"Jordan's shift is the problem. Fix him or replace him.\" Dana sees more. A pick-rate bonus rewards speed over accuracy, the handoff between shifts has no owner, and Jordan avoids hard calls with his crew. Blaming Jordan would satisfy Greg quickly. Fixing the causes takes longer, means questioning her boss and requires changes the crew won't like.",
  "peers": [
    {"name": "Ray Kowalski", "role": "Night-shift lead, 22 years on the floor", "view": "Agrees it's Jordan's fault, partly because the handoff problems make night shift look good."},
    {"name": "Jordan Pike", "role": "Day-shift lead, promoted 14 months ago under Dana", "view": "Capable and well liked, but avoids hard conversations with his crew. Senses he's being blamed."},
    {"name": "Alicia Grant", "role": "Operations manager at a sister site", "view": "Has the dashboards that show the handoff problem, but thinks Dana should replace Jordan and move on."},
    {"name": "Luis Ferreira", "role": "Associate, six years at the site", "view": "One of the most accurate pickers. Keeps missing the speed bonus because he won't cut corners."}
  ],
  "values": ["Reliability: the trucks leave on time", "Fairness: decisions based on evidence, not on who's easiest to blame", "Loyalty to the floor: she remembers being managed badly"],
  "fears": ["Pushing back on Greg and being wrong", "Losing the crew's trust when she changes a bonus they like", "Missing peak season in her first year and confirming doubts about her promotion"],
  "backstory": [
    "Started as a seasonal picker while finishing her degree and stayed because she liked solving floor problems",
    "Known as the lead who \"just fixes it,\" which got her promoted and now tempts her to fix symptoms",
    "Her first review as manager called her a bottleneck who wasn't growing her leads, which led her to the graduate program",
    "Early in her career she watched a coworker get blamed and let go for a problem that turned out to be a broken process"
  ]
}
```

### Review (refresh)

Edit in place. The AI first looks for a throughline in the uploaded course map. If a character
exists it is checked; if not, the full build runs.

AI instructions:

```text
The faculty member's existing modules, activities and materials are given. Look for a
throughline: a company, person, case or project that appears in more than one module. Report
what you found and in which modules. Then say whether one of the existing cases could become
the course's central story, or whether the course needs a new character, and why. Finally
propose one or two performance and conflict pairs, as in the full build, that fit what the
course already teaches.

Return: {"throughline": {"found": boolean, "items": [{"name": string, "modules": [int]}]}, "recommendation": string, "pairs": [...]}
```

Demo response (MGMT 615):

```json
{
  "throughline": {
    "found": false,
    "items": [
      {"name": "Maria's First Ninety Days (case)", "modules": [1]},
      {"name": "The Sales Contest That Backfired (case)", "modules": [2]},
      {"name": "The Team That Couldn't Ship (case)", "modules": [4]},
      {"name": "The Reorg Nobody Saw Coming (case)", "modules": [7]}
    ]
  },
  "recommendation": "Each case appears in one module, with a different company each time. None can carry eight modules, but they share a situation: a new manager under pressure whose first answer is wrong. Build one new character in that situation. The existing cases can stay as contrasts in their modules.",
  "pairs": [
    {"performance": "Diagnose why a team is underperforming before choosing a fix.", "clo": "CLO 1", "conflict": "Leadership has already decided who to blame, and the real causes take longer to fix and mean questioning the boss.", "closTouched": ["CLO 1", "CLO 2", "CLO 3", "CLO 4", "CLO 5", "CLO 6"]}
  ]
}
```

### Decide

The faculty member picks a pair, then edits each part of the profile. Any one part can be
redrafted without the rest.

Checklist:

- Your students could hold this role within a few years.
- There's more than one reasonable choice, so students ask "What would I do?"
- All characters, companies and places are fictional.

### Checks

On save: the performance comes from a CLO; the conflict pushes against it and isn't resolved by
more information; stakes are visible; the profile has all six parts; no real company names. In
refresh, the throughline finding is shown beside the character.

### Save

Planning document: Character Profile in the Storyline section, after Tables 1 and 2 (see
`export.md`). Module 3 adds the storyline premise and the Scenario rows.
Project file: `story.performance`, `story.conflict`, `story.character`; in refresh,
`story.throughline`.

### Go deeper (supplemental)

- `src:guide-storytelling`
- `src:jobaid-media-selection-matrix`
- `src:ext-greene-2020`

---

## Check-in prep

Same instructions as Module 1.

Demo response (MGMT 615):

```json
{
  "changed": ["Interaction statement: new, with a Wednesday activity check added", "Character and conflict: Dana Ortiz, new"],
  "keptFlags": [],
  "questions": ["Is the Wednesday check on inactive students realistic during heavy grading weeks?", "Does Dana's disagreement with her director need any care in how it's framed for students?"]
}
```

Project file: `checkins.prep.m2`.
