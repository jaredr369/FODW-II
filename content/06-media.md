# Module 6. Audiovisual Aspects of Storytelling

Module id: `m6`
Steps: 2
ID check-in: live review of this module's sections, at the end of the week or sooner

Faculty complete: the media plan for each module, with each item's connection to the storyline,
and a first script ready for the XR stage.

Refresh checks for this module: dated media; required welcome, overview, and closing videos
present.

Sources: `src:reading-m6-planning-media`, `src:assignment-m6-media-planning`,
`src:template-av-script`, `src:guide-script-writing`, `src:guide-planning-media`,
`src:example-mgmt615-course-map`

Demo data: `demo/mgmt615-media.json`

## Refresh reflection

> App note: Shown once, in the refresh track only, before step 6.1. It asks only about the course's
> existing videos and graphics.

::: purpose
**What you'll do:** Answer a few questions about the videos and graphics in the last version of your
course. Answer whichever apply; short notes are fine.

**Why it matters:** The AI uses your answers when it reviews each section in this module, so its
suggestions reflect what actually happened in your course.
:::

1. Which videos do students mention, and which do they seem to skip?
2. Which videos are out of date: wrong numbers, old examples, a different version of you?
3. Which visuals do students need that the course doesn't have yet?
4. Which videos would you keep exactly as they are?

> App note: AI instructions are the same as the Module 1 reflection instruction.

Demo answers (MGMT 615): (1) "They mention the role-plays. Nobody mentions the discussion
primers." (2) "None, really." (3) "A picture of the shift handoff." (4) "The role-plays and the feedback video."

Project file: `reflection.m6`.

---

## 6.1 Media for every module

Time: about 40 minutes, about 5 minutes a module
Pattern: pick and combine, one module at a time (full build); edit in place (refresh)

### Learn

::: purpose
**What you'll do:** Plan the media to be produced for each module: video, audio, and graphics,
including the videos every course requires.

**Why it matters:** Media takes the longest to produce, so planning it now gives you and the
Learning Media Team time to make it well.
:::

Learning media is the video, audio, and graphics made for your course, by you and the Learning
Media Team. Curated videos from other sources belong in your materials plan
(Module 5), not here.

| Kind | Required? | Typical length | Who makes it |
|---|---|---|---|
| Welcome video | Yes, in Module 1 | About 3 minutes | Learning Media Team records you on an XR stage |
| Module overview video | Yes, in every module | About 2 minutes | Learning Media Team records you on an XR stage |
| Closing video | Yes, in the last module | 2 to 3 minutes | Learning Media Team records you on an XR stage |
| Teaching video (lecture, worked example, demonstration) | No | 6 minutes or less, or split into parts | Learning Media Team records you on an XR stage, or you record in a One-Touch studio |
| Scenario video | No | 2 to 5 minutes | Learning Media Team records you on an XR stage |
| Audio, such as a short podcast | No | A few minutes | Learning Media Team records you in the studio |
| Graphic, such as an infographic | No | None | A graphic designer |

**Why the required videos matter.** The welcome, overview, and closing videos are how students see
and hear you each week. They're part of your presence in the course and support RSI.

**Limits.** Video and audio you script and record should total no more than 30 minutes a module.
Curated videos from other sources (planned in Module 5) have no total limit, but each should run 6
to 10 minutes at most, and their time counts toward the week's roughly 2 hours of readings and
media. Engagement drops sharply after about six minutes of watching (Guo, Kim, & Rubin, 2014), so
split anything longer into short parts.

**What to record.** Beyond the required videos, save recorded media for what text can't do well: a
topic too complex for many students to grasp from reading alone, a process they need to watch, or a
moment of tension from your story. Keep every item concise, and don't repeat what another material
already covers.

**Media for your story.** Go through your scenarios and decide which need production. A scenario
video opens in the character's situation and ends at the decision, before the answer, so the
activity that follows has something to work on. Many scenarios work fine as readings or
discussion cases with no production at all.

**The XR stage.** Most instructor videos are recorded on the XR stage, which places you in a
produced setting without filming on location. Each video starts with an A/V script (you'll draft
your first in step 6.2), and you schedule a practice session on the stage with the Learning Media
Team before recording.

**One-Touch studios.** These small studios let you create screen-recorded videos on your own, to
illustrate a process or teach with your slides. Videos you make there count toward your 30 minutes
of recorded media.

### See it

::: full
Here's the media plan the MGMT 615 instructor settled on for Module 4. Every item connects to the
storyline, and the scripted video comes to 11 minutes, well under the 30-minute limit.
:::

::: refresh
Here's MGMT 615's Module 4 after the review. The course had no module overview videos, so the
review added one to every module, all recorded in a single XR stage session. The scripted video
comes to 11 minutes.
:::

::: plan Learning Media Plan, Module 4
- Overview video (XR stage): Module 4 overview, 2 min. Story: The handoff nobody owns.
- Teaching video (XR stage): Why Some Teams Just Work, 6 min. Story: Diagnoses the two-shift handoff with the framework.
- Graphic (Learning Media Team): The 4:45 p.m. handoff, day shift to night shift. Story: Shows what falls between the shifts.
- Scenario video (Learning Media Team): Structural Fixes vs. Pep Talks, 3 min. Story: Greg's team-building lunch against a handoff owner.
:::

### Draft (full build) and Review (refresh)

Work through your modules one at a time. Choose a module, then select the button below. The AI
proposes the module's media from its scenario, activities, and materials, including the required
videos, and checks the time. Select **Use this media plan** to copy the list into the box under
Decide.

::: refresh
The AI starts from your Course Map's current media for the module. It checks each item, says what
it would keep, revise, or replace and why, and adds any required video that's missing.
:::

::: module-picker
:::

::: full
AI instructions:

```text
For the given module, using its scenario, activities, and materials, propose its media list.
Always include a module overview video of about 2 minutes; include the welcome video in Module 1
and the closing video in the last module. For each item give: kind (welcome, overview, teaching,
scenario, closing, graphic, audio), a working title, minutes, where it is made (xr-stage for
instructor videos, media-team for produced scenarios and graphics, one-touch for screen
recordings made in a One-Touch studio), one sentence on what it adds that a reading can't, and its connection to the
storyline. Keep scripted video and audio at or under 30 minutes for the module, and each video at
or under 6 minutes unless it is split into parts.

Return: {"items": [{"kind": string, "title": string, "minutes": number, "where": string, "adds": string, "story": string}]}
```
:::

::: refresh
AI instructions:

```text
For each current media item in the given module, check: it adds something a reading can't; it
doesn't repeat other content; its length (flag over 6 minutes unless split into parts); it
connects to the storyline or could with a small change (say what). Flag the module if it has no
overview video, if Module 1 has no welcome video, or if the last module has no closing video.
Suggest keep, revise (say how), or replace. Use the faculty member's reflection on dated videos.

Return: {"items": [{"original": string, "action": "keep" | "revise" | "replace", "issues": [string], "suggestion": string | null}], "missingRequired": [string]}
```
:::

Demo response (MGMT 615):

::: module-options
:::

### Decide

Your final media plan for each module goes in this box. Type in it to change anything, or select
**Redraft with AI** under it to have the AI rewrite it. To work on another module, choose it above;
what you've typed is kept.

For each item, give the kind, who makes it, the title, the minutes, and its connection to your
story. The minutes feed the week check in Module 4.

::: module-fields
:::

Checklist:

- The overview video is there, plus the welcome video in Module 1 and the closing video in the last
  module.
- Each item adds something a reading can't.
- You know which items you'll record on the XR stage.

### Checks

When you save each module, the tool checks that:

- the required videos are there;
- scripted video and audio come to 30 minutes or less;
- each video runs 6 minutes or less, or is split into parts;
- every item names its connection to the storyline.

The week check in Module 4 then uses your real media time instead of an estimate.

### Save

Planning document: Learning Media Plan row in Tables 1 and 2, one line per item, for example
"Scenario video (Learning Media Team): The First Bad Week, 2.5 min. Story: Dana's Monday report and
Greg's email, ending at her decision."
Project file: `modules[].media`; in refresh, `.original`, `.changeNote`.

### Go deeper (supplemental)

- `src:guide-planning-media`
- `src:jobaid-media-selection-matrix`
- `src:ext-guo-2014`

---

## 6.2 Your first script and the XR stage

Time: about 25 minutes
Pattern: interview, then draft

### Learn

::: purpose
**What you'll do:** Draft one A/V script, usually for your welcome video or your Module 1 overview.

**Why it matters:** Writing one script now, with feedback, makes the rest faster during development.
The script is also what you share with the Learning Media Team before your practice session on the
XR stage.
:::

Every instructor video starts with an A/V script in two columns: what you'll say (Dialogue) and what
appears on screen (Graphics). The template runs in five parts:

- **Opening:** the branded intro, with no dialogue.
- **Introduction:** greet students and frame the topic.
- **Content:** the main ideas, in short chunks of two to four sentences.
- **Conclusion:** one clear next step.
- **Closing:** the branded outro.

**Write for the ear.** Use contractions and full sentences, and read it aloud as you write; if a
sentence is awkward spoken, rewrite it. Say anything a student needs to know, so nothing depends
only on what's on screen. Most scripts run 250 to 350 words, about 2 to 2.5 minutes spoken.

Your ID and the Learning Media Team will help with the rest of your scripts during development.

**Getting ready for the stage.** Send the finished script to your ID, who passes it to Learning
Media. Schedule a practice session on the XR stage with the Learning Media Team. Record your
required videos in as few sessions as you can; MGMT 615 recorded all eight module overviews in
one.

### See it

MGMT 615's welcome video, first lines:

| Dialogue | Graphics |
|---|---|
| Howdy, and welcome to MGMT 615. Over the next eight weeks, you'll follow one manager, Dana Ortiz, through the hardest stretch of her first year running a distribution center. | Course title, then the instructor on the XR stage |
| Each module puts you inside one of Dana's decisions: a shift that's falling behind, a bonus nobody wants to lose, a director who's sure he's right. You'll decide before you find out what she did. | Three snapshots from Dana's story |

### Draft (full build) and Review (refresh)

Answer the questions, then select the button below. The AI drafts the script in the template's two
columns, in your voice and at the planned length. Select **Use this script** to copy it into the
box under Decide.

::: refresh
If you already have a script for this video, paste it into the last box. The AI checks it for
length, spoken style, and the decision ending, and suggests edits instead of starting over.
:::

::: fields
- Which video are you scripting: your welcome video, a module overview, or a scenario video from your media plan? | The Module 1 overview, 2 minutes.
- What should students feel or understand by the end? | That a manager's job is different from the job Dana just left, and that Greg's quick answer deserves a second look.
- Is there a phrase or story you always use when you introduce this? | "Your best player isn't automatically your best coach."
- Your current script for this video, if you have one
:::

AI instructions:

```text
Draft an A/V script for the chosen video in two columns, Dialogue and Graphics, with sections:
opening (branded intro, no dialogue), introduction, content in chunks of 2 to 4 sentences,
conclusion with one next step, closing (branded outro). Write conversational spoken English with
contractions, in the faculty member's voice, using their answers. Keep to the planned minutes at
about 140 spoken words a minute. For an overview or scenario video, open in the character's
situation and end at the decision without resolving it. Put everything a student needs in the
dialogue; graphics only reinforce it. If the faculty member pasted a current script, check it for
length, spoken style, and the decision ending, and suggest edits to it instead of starting over.

Return: {"title": string, "minutes": number, "rows": [{"section": string, "dialogue": string, "graphics": string}]}
```

Demo response (MGMT 615):

**Script:** Module 1 overview: What Managers Actually Do. About 2 minutes.

| Section | Dialogue | Graphics |
|---|---|---|
| Opening | (No dialogue) | Branded intro |
| Introduction | Howdy. This week you meet Dana Ortiz. Eight months ago she was the best shift lead in her distribution center. Now she runs it, and on Monday morning the report says on-time shipping has dropped from 97 to 89 percent. | Dana's Monday report, with 89% highlighted |
| Introduction | Her director already has an answer. Before you agree with him, this module asks you a different question: what is a manager's job, and how is it different from the job Dana just left? | Greg's email: "Jordan's shift is the problem." |
| Content | There's a line I've used with every new manager I've coached: your best player isn't automatically your best coach. Dana got this job because she was great at the work. Now her job is getting the work done through other people, and the habits that made her great won't tell her how. | Two columns: "Shift lead's day" and "Manager's day" |
| Content | Here's what to watch for. When the numbers drop, the fastest answer is usually a person: a slow picker, a weak lead, a bad shift. Sometimes that's right. More often the cause sits between people, in how work gets handed off or who owns a decision. A manager looks there first. | Three words on screen: person, process, handoff |
| Content | This week's reading looks at how managers actually spend their time. Notice how little of it is doing the work yourself. As you read, keep Dana's report in mind. What would you need to know before you decide whose fault it is? | The reading's title and author |
| Conclusion | Start with Dana's Monday report, then the reading on what managers actually do. This week's assignment asks what you'd do with Dana's first week, so hold off on deciding about Jordan until you've read it. I'll see you in the discussion. | This week: the report, the reading, the assignment due Sunday |
| Closing | (No dialogue) | Branded outro |

**Length:** about 260 words, about 2 minutes at 140 words a minute.

### Decide

Read your script aloud, then make it yours in the box below. Type in it to change anything, or
select **Redraft with AI** under it to have the AI rewrite it, for example shorter or closer to how
you talk.

::: fields
- Your script: for each part, the dialogue and the graphics
- What you changed after reading it aloud
:::

Checklist:

- It sounds natural read aloud.
- It fits the planned length.
- Nothing important appears only on screen.
- You've asked your ID to schedule an XR stage practice session.

### Checks

When you save, the tool checks that:

- the spoken length is within 15 percent of the planned minutes, at about 140 words a minute;
- every graphic has matching dialogue, so nothing important appears only on screen.

### Save

Planning document: nothing new; the media line for this video gains "script drafted."
Download: the script as a Word file in the A/V script template format, to share with your ID and
Learning Media. There's nothing to fill out or submit; it's there to show and share.
Project file: `scripts[]` (video, rows, status).

### Go deeper (supplemental)

- `src:guide-script-writing`
- `src:template-av-script`
- `src:tool-scriptwise`: an AI tool for developing scripts. Any AI tool can also help: paste in
  your draft and ask it to tighten the wording for the ear or cut it to length.

---

## Check-in prep

Same instructions as Module 1.

Demo response (MGMT 615):

```json
{
  "changed": ["Media plan for all eight modules, 7.5 to 14 minutes each", "Module overview videos added for every module", "Discussion primers replaced with scenario videos", "Module 1 overview script drafted"],
  "keptFlags": ["Module 3 teaching video at 7 minutes, in two parts"],
  "questions": ["Can all eight overviews be recorded in one XR stage session?", "Which scenario videos can Learning Media produce this term?"]
}
```

Project file: `checkins.prep.m6`.
