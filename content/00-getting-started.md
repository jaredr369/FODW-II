# Getting Started

Module id: `gs`
Steps: 2
ID check-in: none (first check-in follows Module 1)

Faculty complete: AI connection, save folder, ID and check-in details, course details, and
track. Refresh track also uploads the current Course Map or syllabus.

Sources: `src:reading-gs-flex-online-process`, `src:guide-course-development-process`,
`src:tool-course-creator`, `src:example-mgmt615-course-map`

---

## GS.1 Set up

Time: about 15 minutes
Pattern: setup (no AI draft)

### Learn

::: purpose
**What you'll do:** Connect the AI, choose where your work is saved, and enter your ID's name and
check-in details.

**Why it matters:** Every step after this one depends on them. The AI drafts and checks each
section, and the files you save are how your ID sees your work.
:::

**How this workshop works.** A Flex Online course is a Mays online business course built on a shared
template and common design standards. In this workshop, you'll build your Course Planning Document,
a working plan that will guide the future development of the entire course. Each module in this
workshop will have you building different sections of your course plan. The expected pace is one
module per week, with a live check-in each week by Zoom or in person with your instructional
designer (ID). Your ID is assigned to you before the workshop begins and works with you through the
development of your course. You can work ahead; if you do, ask your ID to meet more often, so each
module is reviewed before the next one builds on it.

**How each step works.** Throughout the workshop, AI drafts ideas for you to decide on, modify, and
save. Each step opens with **Learn**, a short read on what the section is for, and **See it**, an
example from MGMT 615 (a fictitious course used throughout the workshop). See it shows what the MGMT
615 instructor did in that step and what came out of it, so you can see what you're aiming for
before you start. Then you work on your own course. Doing so has a few quick steps:

- **Draft.** Select Draft with AI, and the AI writes a first version of one section of your plan
  from your course details. If you're updating a course you already teach, Review with AI checks
  your current section instead and flags what may need to change.
- **Decide.** You're the expert on your course. You are free to keep the draft, edit it, ask for
  another version, or write your own. A short checklist shows what a finished section includes.
- **Save.** When you're happy with the section, select Save to plan, and it goes into your Course
  Planning Document. **Checks** then run and flag anything to fix, or to keep with a note for your
  ID.

Some steps end with **Go deeper (supplemental)**: readings and tools that build on the step. Use
them to strengthen that part of your plan.

After the workshop comes a kick-off meeting with your ID to plan the development schedule, then 13
weeks of development, 2 weeks of quality review, and a final week to review the course and train on
grading and communicating in Canvas. Then the course is yours to teach. You are the expert on what
the course teaches; your ID is the expert on how to teach it online.

**The AI.** This tool uses TAMU AI Chat to draft and check each section of the course plan. You
connect it with your own key, a code that works like a password and lets this tool use TAMU AI
Chat for you. The key stays in this browser and never goes into your project file.
Every draft is a starting point: you can edit it, ask for another, or write the section yourself,
and nothing goes into your plan until you select Save.

We strongly recommend connecting TAMU AI Chat. The workshop is built around it. You can continue without
it, but you will write every section yourself, without first drafts, checks on your work, or, if
you're updating a course you already teach, a review of it. You can connect it later with the
Settings button at the top of every page.

How to get your TAMU AI key (about a minute):

1. Open TAMU AI Chat at chat.tamu.ai in a new tab and sign in with your NetID.
2. Select your name or profile picture in the lower-left corner, then Settings.
3. Select Account from the options on the left. Then to the right of API keys, select Show.
4. Select Create new secret key. If a key is already listed, you can use that one.
5. Copy the key. It starts with `sk-`.
6. Paste it below and select Test connection.

Treat the key like a password. If you don't see API keys in your settings, contact your ID.

**Saving and sharing.** This tool is not like Canvas. Your work saves in this browser as you go.
When you select Save, the tool writes two files to a folder you choose: the planning document
(Word), which your ID reads, and a project file, which lets you reopen your work on any computer
and pick up where you left off. If possible, choose a folder your ID can see,
such as a OneDrive or Teams folder you share with them. This works best in Microsoft Edge or Google
Chrome; in other browsers, the files go to Downloads, and you move them yourself.

> Review note: key steps adapted from `src:tool-course-creator`; the key process is confirmed.
> Still open for TAMU IT: what we can say about how TAMU AI Chat handles course content.

### See it

Throughout the workshop, you'll see examples from MGMT 615, a fictitious course. Here's how its
instructor did this step. They connected a key, chose a OneDrive folder shared with their ID, and set a Tuesday
check-in. They finished Modules 1 and 2 in the first week and asked their ID for a second meeting
that week.

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

1. Paste your key and select Test connection, or select Continue without AI.
2. Select Choose save folder and pick a folder your ID can see.
3. Enter your ID's name and your weekly check-in day, time, and format. Any of these can wait.

> App note: Continue without AI is a smaller link and asks for confirmation: "Without the AI
> you'll write every section of your plan yourself. You won't get first drafts, checks on your
> work, or a review of your existing course. You can connect the AI later from Settings."
> Buttons: Connect the AI (default), Continue without AI.

If the test fails, you'll see what went wrong and a Try again button.

> App note: failure messages and the AI-off banner.
>
> | Problem | Message shown |
> |---|---|
> | Key not accepted (401 or 403) | TAMU AI Chat didn't accept the key. Check that you copied all of it and that it hasn't been deleted. |
> | Can't reach the service | Couldn't reach TAMU AI Chat. Check your internet connection. Off campus, you may need the university VPN. |
> | Too many requests (429) | TAMU AI Chat is busy right now. Wait a moment and try again. |
>
> Until a key is connected, each module shows a banner, "Your AI guide is off. Connect it to get
> drafts and checks for this step.", with a Connect button.

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

### Go deeper (supplemental)

- `src:guide-course-development-process`: roles, phases, and the full development process.

---

## GS.2 Your course and your track

Time: about 20 minutes
Pattern: setup; edit in place for the refresh upload

### Learn

::: purpose
**What you'll do:** Enter your course's details and choose a track: Full build or Refresh.

**Why it matters:** Every later step uses your choices. Your course details go into each AI draft,
and your track decides whether each step drafts a new section or reviews the one you already have.
:::

Choose a track:

- **Full build** if the course is new or you're rebuilding it from the beginning.
- **Refresh** if your course has already been developed and taught in the Flex Online program.
  Upload its Course Map as a Word file, or paste the text. Your ID can help you get the latest version. In each module you'll see the matching section of your Course Map with flags beside it that note what may need
  attention. You keep the section, accept or edit a suggested revision,
  or rewrite it. Each change gets a short note so your ID can see what changed and why.

A Course Map is not the same as your Course Planning Document. The Course Map is the finished,
detailed record of everything in a course, complete enough to rebuild the course in another
learning management system if it were ever lost from Canvas. The Course Planning Document is the
working plan you build in this workshop, a section at a time.

Both tracks go through every module, and both add a storyline to your course: a recurring
character and a realistic scenario in each module, which you'll plan in Modules 2 and 3. Most
existing courses don't have a storyline yet, so refresh courses build one too.

### See it

Here's how the MGMT 615 instructor did this step. The course had already been developed and taught
in the Flex Online program, so they chose Refresh and uploaded their Course Map. The tool sorted it
into the sections of the Course Planning Document and found most of them: the catalog description,
the course vision, five course-level objectives (CLOs) and all eight modules. A few sections weren't
in the Course Map. The instructor wrote the learner description and added the program outcomes
themselves in Module 1. For the storyline, the tool drafts a first version in Modules 2 and 3,
just as it would in a full build.

### Draft (full build)

Fill in a few details about your course. There's no AI draft in this step.

| Field | Required | Example (MGMT 615) |
|---|---|---|
| Course number | Yes | MGMT 615 |
| Course title | Yes | Managing People and Performance |
| Credit hours | Yes | 3 |
| Degree or certificate program | Yes | MS in Management |
| First term taught online | No | Fall 2027 |
| Track | Yes | Refresh |

### Review (refresh)

Next, upload your Course Map as a Word file or paste its text. Select Sort with AI, and the AI
sorts it into the sections of your Course Planning Document. Without the AI, you skip the upload
and paste each current section when you reach it.

AI instructions:

```text
You are given the text of a faculty member's existing Course Map or syllabus.
Find the content for each section below. Copy text exactly as written. Do not rewrite, fix, or
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

Demo response (MGMT 615):

| Section | Result |
|---|---|
| Catalog description, course vision | Found |
| CLOs | Found, 5 |
| Modules | Found, 8, with titles, CLOs met, topics, objectives, activities, materials, media, cohort sessions, and overviews |
| Program outcomes, learners, character, storyline and scenarios, communication plan | Missing |

> Review note: the recorded JSON for this response will be generated from the MGMT 615 course map
> when demo mode is built.

### Decide

Check that your course details are correct. If you uploaded a Course Map, you'll also see each
section the AI found next to its label. Confirm each one, move any text that landed in the wrong
place, or mark a section as not in your document.

Checklist:

- Course number, title, and program are correct.
- If you uploaded a Course Map: each found section is under the right label.
- If you uploaded a Course Map: you know which sections are missing from it. You'll fill them in
  when you reach them.

### Checks

None.

### Save

Planning document: course number and title in the document title; program on the cover
section.
Project file: `course`, `track`, `source.sections`, `source.missing`, `source.fileName`.

Next is Module 1. Your first check-in with your ID comes after it.
