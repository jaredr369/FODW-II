# Module 6. Audiovisual Aspects of Storytelling

Module id: `m6`
Steps: 2
ID check-in: live review of this module's sections, at the end of the week or sooner

Faculty complete: the media plan for each module, with each item's connection to the storyline,
and a first script ready for the XR stage.

Refresh checks for this module: dated media; required welcome, overview and closing videos
present.

Sources: `src:reading-m6-planning-media`, `src:assignment-m6-media-planning`,
`src:template-av-script`, `src:guide-script-writing`, `src:guide-planning-media`,
`src:example-mgmt615-course-map`

Demo data: `demo/mgmt615-media.json`

## Refresh reflection

Shown once, in the refresh track only, before step 6.1. It asks only about the course's existing
videos and graphics.

1. Which videos do students mention, and which do they seem to skip?
2. Which videos are out of date: wrong numbers, old examples, a different version of you?
3. Which visuals do students need that the course doesn't have yet?
4. Which videos would you keep exactly as they are?

AI instructions: same as the Module 1 reflection instruction.

Demo answers (MGMT 615): (1) "They mention the role-plays. Nobody mentions the discussion
primers." (2) "None, really." (3) "A picture of the shift handoff." (4) "The role-plays and the feedback video."

Project file: `reflection.m6`.

---

## 6.1 Media for every module

Time: about 40 minutes, about 5 minutes a module
Pattern: pick and combine, one module at a time (full build); edit in place (refresh)

### Learn

Your media plan lists what will be produced for your course: video, audio and graphics. Curated
videos from other sources belong in your materials plan.

**Required in every course:** a welcome video, a short overview video for each module, and a
closing video. These are how students see and hear you each week, which is part of your presence
and supports RSI.

**Optional:** teaching videos (lecture, worked example, demonstration), scenario videos that
present a moment from your storyline, audio, and graphics such as an infographic of the data
your character works from.

**Limits.** Recorded video totals no more than 30 minutes a module. Engagement drops sharply
after about six minutes (Guo, Kim, & Rubin, 2014), so split anything longer into short pieces,
one idea each. Every item should add something a reading can't: a process to watch, a voice and
face, a moment of tension.

**Media for your story.** Go through your scenarios and decide which need production. A scenario
video opens in the character's situation and ends at the decision, before the answer, so the
activity that follows has something to work on. Many scenarios work fine as readings or
discussion cases with no production at all.

**The XR stage.** Instructor videos, including the required welcome and overview videos, are
recorded on the XR stage, which places you in a produced setting without filming on location.
For each video you fill out the A/V script template (step 6.2), and you schedule a practice
session on the stage with the Learning Media team before recording.

### See it

MGMT 615 Module 4: a 2-minute overview ("the handoff nobody owns"), a 6-minute teaching video
diagnosing the two-shift handoff, an infographic of the 4:45 p.m. handoff, and a 3-minute
scenario video setting Greg's team-building lunch against a handoff owner. 11 minutes.

### Draft (full build)

AI instructions:

```text
For the given module, using its scenario, activities and materials, propose two versions of its
media list. Always include a module overview video of about 2 minutes; include the welcome video
in Module 1 and the closing video in the last module. For each item give: kind (welcome,
overview, teaching, scenario, closing, graphic, audio), a working title, minutes, where it is
made (xr-stage for instructor videos, media-team for produced scenarios and graphics,
faculty-self for screen recordings), one sentence on what it adds that a reading can't, and its
connection to the storyline. Keep video at or under 30 minutes for the module and each video at
or under 6 minutes unless it is split into parts.

Return: {"versions": [{"items": [{"kind": string, "title": string, "minutes": number, "where": string, "adds": string, "story": string}]}]}
```

Demo response (MGMT 615, if run as a full build): each module's `media` from
`demo/mgmt615-media.json`.

### Review (refresh)

Edit in place. The app lists each module's current produced media from the upload.

AI instructions:

```text
For each current media item in the given module, check: it adds something a reading can't; it
doesn't repeat other content; length (flag over 6 minutes unless split); it connects to the
storyline or could with a small change (say what). Flag the module if it has no overview video,
if Module 1 has no welcome video, or if the last module has no closing video. Suggest keep,
revise (say how) or replace. Use the faculty member's reflection on dated videos.

Return: {"items": [{"original": string, "action": "keep" | "revise" | "replace", "issues": [string], "suggestion": string | null}], "missingRequired": [string]}
```

Demo response (MGMT 615): `review` notes in `demo/mgmt615-media.json`. Main findings: no module
overview videos (added, all recorded in one XR session); the discussion primers didn't connect to
the story and, per the reflection, nobody mentioned them (replaced by scenario videos); one
teaching video at 8 minutes (kept at 7, in two parts).

### Decide

Checklist (for each module):

- The overview video is there.
- Each item adds something a reading can't.
- You know which items you'll record on the XR stage.

### Checks

On save of each module: required videos present (welcome in Module 1, overview in every module,
closing in the last); total video at or under 30 minutes; each video at or under 6 minutes or
split; every item has a storyline connection or a note. The week-in-your-student's-shoes
walk-through refreshes with video time.

### Save

Planning document: Learning Media Plan row in Tables 1 and 2, one line per item, for example
"Video (XR stage): Module 4 overview, 2 min. Story: the handoff nobody owns."
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

Every instructor video starts with an A/V script: two columns, what you'll say (Dialogue) and
what appears on screen (Graphics). The template has four parts: a branded opening, an
introduction where you greet students and frame the topic, the content in short chunks, and a
conclusion with a clear next step, then a branded close. The script is what you share with the
Learning Media team before your practice session on the XR stage.

Write for the ear. Use contractions and full sentences, and read it aloud as you write; if a
sentence is awkward spoken, rewrite it. Say anything a student needs to know, so nothing depends
only on what's on screen. A 2-minute overview is about 250 to 300 spoken words.

In this step you draft one script, usually your welcome video or your Module 1 overview. Your ID
and the Learning Media team will help with the rest during development.

**Getting ready for the stage.** Send the finished script to your ID, who passes it to Learning
Media. Schedule a practice session on the XR stage with the Learning Media team. Record your
required videos in as few sessions as you can; MGMT 615 recorded all eight module overviews in
one.

### See it

MGMT 615's Module 1 overview, first lines:

| Dialogue | Graphics |
|---|---|
| Howdy. This week you meet Dana Ortiz. Eight months ago she was the best shift lead in her distribution center. Now she runs it, and on Monday morning the report says on-time shipping has dropped from 97 to 89 percent. | Dana's Monday report, with 89% highlighted |
| Her director already has an answer. Before you agree with him, this module asks you a different question: what is a manager's job, and how is it different from the job Dana just left? | Greg's email: "Jordan's shift is the problem." |

### Draft (full build) and Review (refresh)

The AI asks which video to script (welcome, a module overview, or a scenario video from the media
plan) and two questions: "What should students feel or understand by the end?" and "Is there a
phrase or story you always use when you introduce this?" Then it drafts.

AI instructions:

```text
Draft an A/V script for the chosen video in two columns, Dialogue and Graphics, with sections:
opening (branded intro, no dialogue), introduction, content in chunks of 2 to 4 sentences,
conclusion with one next step, closing (branded outro). Write conversational spoken English with
contractions, in the faculty member's voice, using their answers. Keep to the planned minutes at
about 140 spoken words a minute. For an overview or scenario video, open in the character's
situation and end at the decision without resolving it. Put everything a student needs in the
dialogue; graphics only reinforce it.

Return: {"title": string, "minutes": number, "rows": [{"section": string, "dialogue": string, "graphics": string}]}
```

Refresh track: if an existing script is uploaded, the same instructions check it for length,
spoken style and the decision ending, and suggest edits in place.

Demo response (MGMT 615): the Module 1 overview, 2 minutes, opening as under See it and closing
with "Start with Dana's Monday report, then the reading on what managers actually do. Thursday's
assignment asks what you'd do with her first week."

### Decide

The faculty member reads the script aloud, edits it, and marks it ready for Learning Media.

Checklist:

- It sounds natural read aloud.
- It fits the planned length.
- Nothing important appears only on screen.
- You've asked your ID to schedule an XR stage practice session.

### Checks

On save: spoken length within 15 percent of the planned minutes; every graphic has matching
dialogue.

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
  "changed": ["Media plan for all eight modules, 9.5 to 14 minutes each", "Module overview videos added for every module", "Discussion primers replaced with scenario videos", "Module 1 overview script drafted"],
  "keptFlags": ["Module 3 teaching video at 7 minutes, in two parts"],
  "questions": ["Can all eight overviews be recorded in one XR stage session?", "Which scenario videos can Learning Media produce this term?"]
}
```

Project file: `checkins.prep.m6`.
