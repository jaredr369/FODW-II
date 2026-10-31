# Getting Started

Module id: `gs`
Steps: 2
ID check-in: none (first check-in follows Module 1)

Faculty complete: AI connection, save folder, ID and check-in details, course details and
track. Refresh track also uploads the current course map or syllabus.

Sources: `src:reading-gs-flex-online-process`, `src:guide-course-development-process`,
`src:tool-course-creator`, `src:example-mgmt615-course-map`

---

## GS.1 Set up

Time: about 15 minutes
Pattern: setup (no AI draft)

### Learn

**How this workshop works.** You'll build your Course Planning Document, the plan your
instructional designer (ID) builds your course from. Getting Started and eight modules each add
sections to it. The expected pace is one module a week, with a live check-in with your ID each
week, by Zoom or in person. You can work ahead; if you do, ask your ID to meet more often, so
each module is reviewed before the next one builds on it.

After the workshop come a kick-off meeting with your ID, 13 weeks of content development, 2 weeks
of quality review, and a final week to review the course and train on grading and communicating
in Canvas. Then the course is yours to teach. You are the expert on what the course teaches; your
ID is the expert on how to teach it online.

**The AI.** This tool uses TAMU AI Chat to draft and check each section. You connect it with your
own key, which stays in this browser and never goes into your project file. Every draft is a
starting point: you can edit it, ask for another, or write the section yourself, and nothing goes
into your plan until you select Save.

We strongly recommend connecting the AI. The workshop is built around it. You can continue
without it, but then you write every section yourself, without first drafts, checks on your
work, or, in the refresh track, a review of your existing course. You can connect it later from
Settings.

How to get your key (about a minute):

1. Open TAMU AI Chat at chat.tamu.ai in a new tab and sign in with your NetID.
2. Select your name or profile picture in the lower-left corner, then Settings.
3. Select Account. Next to API keys, select Show.
4. Select Create new secret key. If a key is already listed, you can use that one.
5. Copy the key. It starts with `sk-`.
6. Paste it below and select Test connection.

Treat the key like a password. If you don't see API keys in your settings, contact your ID.

**Saving and sharing.** There is nothing to submit. Your work saves in this browser as you go.
When you select Save, the tool writes two files to a folder you choose: the planning document
(Word), which your ID reads, and a project file, which holds everything and lets you keep working
on another computer. Choose a folder your ID can see, such as a OneDrive or Teams folder you share
with them, and saving is sharing. This works best in Microsoft Edge or Google Chrome; in other
browsers the files go to Downloads and you move them yourself.

> Review note: key steps adapted from `src:tool-course-creator`; the key process is confirmed.
> Still open for TAMU IT: what we can say about how TAMU AI Chat handles course content.

### See it

The MGMT 615 instructor connected a key, chose a OneDrive folder shared with their ID, and set a
Tuesday check-in. They finished Modules 1 and 2 in the first week and asked their ID for a second
meeting that week.

### Draft (full build) and Review (refresh)

No AI draft. Test connection sends one short request.

AI instructions:

```text
Reply with {"ok": true}.
```

Demo response: `{"ok": true}`. Demo mode skips the key and plays recorded responses.

App notes (from `src:tool-course-creator`, reference only): TAMU AI Chat is OpenAI-compatible.
Course Creator calls `https://chat.tamu.ai/api`, falls back to `https://chat-api.tamu.ai/openai`,
sends the key as a Bearer token, lists models from `/models`, posts to `/chat/completions`, and
prefers Claude Sonnet, then other Claude models, then GPT models.

### Decide

The faculty member:

1. Pastes the key and selects Test connection, or selects Continue without AI (a smaller link),
   which asks for confirmation: "Without the AI you'll write every section of your plan yourself.
   You won't get first drafts, checks on your work, or a review of your existing course. You can
   connect the AI later from Settings." Buttons: Connect the AI (default), Continue without AI.
2. Selects Choose save folder.
3. Enters their ID's name and the weekly check-in day, time and format. Any of these can wait.

If the test fails, the app shows the cause and offers Try again:

| Problem | Message shown |
|---|---|
| Key not accepted (401 or 403) | TAMU AI Chat didn't accept the key. Check that you copied all of it and that it hasn't been deleted. |
| Can't reach the service | Couldn't reach TAMU AI Chat. Check your internet connection. Off campus, you may need the university VPN. |
| Too many requests (429) | TAMU AI Chat is busy right now. Wait a moment and try again. |

Until a key is connected, each module shows a banner, "Your AI guide is off. Connect it to get
drafts and checks for this step.", with a Connect button.

Checklist:

- The AI is connected, or you chose to continue without it.
- Your files save to a folder your ID can see.
- You have a weekly check-in time, or know who to ask.

### Checks

None.

### Save

Planning document: ID name on the cover section.
Browser only: `course-plan-builder:apiKey`, `course-plan-builder:aiSkipped`,
`course-plan-builder:saveFolder` (folder handle).
Project file: `course.idName`, `checkins.day`, `checkins.time`, `checkins.format`,
`checkins.log[]`.

### Go deeper (optional)

- `src:guide-course-development-process`: roles, phases and the full development process.

---

## GS.2 Your course and your track

Time: about 20 minutes
Pattern: setup; edit in place for the refresh upload

### Learn

Choose a track:

- **Full build** if the course is new or you're rebuilding it from the beginning. Each module
  drafts its sections from your course details.
- **Refresh** if the course already runs online and you have a course planning document or
  syllabus. Upload it now. In each module you'll see your current section with flags beside it,
  and you keep it, accept or edit a suggested revision, or rewrite it. Each change gets a short
  note so your ID can see what changed and why.

Both tracks go through every module. Most existing courses have no character or scenarios; in
the refresh track, a section your document doesn't have runs as a full build. A course map in
the Flex Online format gives the best results; a syllabus works, with more sections missing.

### See it

The MGMT 615 instructor chose Refresh and uploaded the course map. The tool found the catalog
description, the vision, five CLOs and all eight modules with their activities, materials and
media. It found no program outcomes, character, storyline, scenarios or communication plan. Those
ran as full builds later.

### Draft (full build)

The faculty member fills in a form. No AI call.

| Field | Required | Example (MGMT 615) |
|---|---|---|
| Course number | Yes | MGMT 615 |
| Course title | Yes | Managing People and Performance |
| Credit hours | Yes | 3 |
| Program | Yes | [Program name] |
| First term taught online | No | [Term] |
| Track | Yes | Refresh |

### Review (refresh)

The same form, then the faculty member uploads a .docx or pastes text. The AI sorts it into the
planning document's sections. Without AI, the upload is skipped and the faculty member pastes
each current section when they reach it.

AI instructions:

```text
You are given the text of a faculty member's existing course planning document or syllabus.
Find the content for each section below. Copy text exactly as written. Do not rewrite, fix or
summarize. If a section is not in the document, return null for it. If you are unsure where
something belongs, put it in "unsorted".

Sections:
- catalogDescription
- programOutcomes (list)
- courseVision
- clos (list)
- modules (list of {number, title, closMet, topics, objectives, activities, materials, media,
  cohortSession, overview})
- character (any recurring person or case that runs across modules)
- storyline
- scenarios (list, one per module)
- communicationPlan (announcements, feedback turnaround, instructor contact)
- learners (who takes the course)

Return: {"sections": {...}, "unsorted": [string], "found": [section names], "missing": [section names]}
```

Demo response (MGMT 615, from `src:example-mgmt615-course-map`):

| Section | Result |
|---|---|
| Catalog description, course vision | Found |
| CLOs | Found, 5 |
| Modules | Found, 8, with titles, CLOs met, topics, objectives, activities, materials, media, cohort sessions and overviews |
| Program outcomes, learners, character, storyline and scenarios, communication plan | Missing |

> Review note: the recorded JSON for this response will be generated from the MGMT 615 course map
> when demo mode is built.

### Decide

The tool shows each found section next to its label. The faculty member confirms each, moves
misplaced text, or marks a section as not in the document.

Checklist:

- Course number, title and program are correct.
- Each found section is under the right label.
- You know which sections will run as a full build.

### Checks

None.

### Save

Planning document: course number and title in the document title; program on the cover
section.
Project file: `course`, `track`, `source.sections`, `source.missing`, `source.fileName`.

Getting Started ends without check-in prep; the first check-in follows Module 1.
