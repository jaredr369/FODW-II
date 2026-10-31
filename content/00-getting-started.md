# Getting Started

Module id: `gs`
Steps: 4
Gate: none

Faculty complete: AI key setup, course details, the Flex Online process. Refresh track also
uploads the current course map or syllabus.

---

## GS.1 Connect your AI key

Time: about 15 minutes

### Learn

This tool uses TAMU AI Chat to draft and check sections of your course plan. You connect it
with your own API key, which you create once at chat.tamu.ai.

Your key is stored in this browser on this computer. It is never written into your project
file, so you can send that file to your instructional designer (ID) without sending the key. If
you move to another computer, you paste the key again there.

The AI works only from what you give it: the course details you enter, the sections you have
already saved and, in the refresh track, the course map or syllabus you upload. It does not see
other faculty members' plans.

Treat every draft as a starting point. In each step you can edit what the AI wrote, ask for
another version, or write the section yourself. Nothing goes into your planning document until
you select Save, and you can change a saved section later.

How to create a key:

1. [Steps for chat.tamu.ai, to be written once TAMU IT confirms the process.]
2. Copy the key.
3. Paste it below and select Test connection.

> Review note: the key steps, the endpoint and the model list wait on TAMU IT. Also confirm
> with IT what we can say about how TAMU AI Chat handles course content, and add one plain
> sentence here once we know.

### See it

The MGMT 615 instructor connected a key before starting Module 1. When they reached the CLO
step, the AI had their catalog description, course vision and learner description to work
from, so its first draft of CLOs already used their course's language about diagnosis and
feedback.

### Draft (full build) and Review (refresh)

No AI draft in this step. The app sends one short test request.

AI instructions:

```text
Reply with {"ok": true}.
```

Demo response:

```json
{"ok": true}
```

### Decide

The faculty member pastes the key and selects Test connection. If the test fails, the app shows
the error in plain words (wrong key, no network, service unavailable) and offers Try again.

Checklist:

- The connection test passed.
- You know where to create a new key if you change computers or the key stops working.

Demo mode skips this step and uses recorded AI responses for MGMT 615.

### Save

Planning document: nothing.
Browser only: the API key, under `course-plan-builder:apiKey`.
Project file: nothing.

---

## GS.2 How a Flex Online course gets built

Time: about 20 minutes

### Learn

A Flex Online course is planned first, then built, then reviewed, and then taught. This tool
covers the planning.

**Planning (this workshop).** You work through Getting Started and eight modules at your own
pace. Each module adds sections to your Course Planning Document, the plan your ID will build
from. You meet with your ID three times, by Zoom or in person. Each meeting is a gate: you
move on once your ID has reviewed that part of the plan with you.

| Meeting | After | What you bring |
|---|---|---|
| Gate 1 | Module 2 | Course vision, CLOs, module titles and topics, your character and conflict, and your syllabus statement on when students hear from you |
| Gate 2 | Module 4 | Your storyline, one scenario per module, and the learning activities for each module |
| Gate 3 | Module 8 | The finished planning document and your communication and feedback plan |

**Kick-off.** After the workshop your ID schedules a kick-off meeting. Together you go through
the planning document, confirm what is ready to build, and set milestone dates.

**Content development.** Over about 13 weeks you write the course materials and your ID builds
the course in a Canvas development shell. Shortly after kick-off you meet with your ID and the
Director of Learning Media to confirm which videos and graphics will be produced. If a scenario
needs filming, bring your scenario plan to that meeting.

**Quality review.** A peer review checks that objectives, activities and materials line up. A
technical review checks accessibility, links, the gradebook and due dates. In the week before
launch you look over the finished course and make small fixes.

**Teaching.** You and your ID meet for facilitation training, and then the course is yours to
run. The Learning Delivery team supports your live cohort sessions and contacts you once the
term begins.

**Your ID's role.** You are the expert on what the course teaches. Your ID is the expert on how
to teach it online. Expect your ID to question choices, point out accessibility and copyright
issues, and keep the project on schedule. Your ID will not make content decisions for you.

> Review note: the source reading says 13 weeks for content development in one place and a
> 16-week timeline in a knowledge check answer. I used 13. The three-week timeline for this
> tool is still open, so no workshop length is stated here.

### See it

At Gate 1, the MGMT 615 instructor brought five CLOs, eight module titles and a character,
Dana Ortiz, a new operations manager whose director has already decided who to blame for a
drop in on-time shipping. The ID's first question was which CLO each of Dana's decisions came
from. Two decisions in the draft had no CLO behind them, so the instructor cut one and tied the
other to the hiring CLO before moving on to scenarios.

### Draft (full build) and Review (refresh)

No AI draft. The faculty member answers a short knowledge check and records meeting plans.

Knowledge check (feedback shown after each answer, not scored):

1. What does your ID use to build your course?
   - a) Your Canvas course from a previous term
   - **b) Your Course Planning Document**
   - c) A recording of your first meeting
   - d) The program's course catalog

   Feedback: The planning document is what the workshop produces and what content development
   starts from. A complete, specific plan shortens the build.

2. When is your first gate meeting?
   - a) Before Module 1
   - **b) After Module 2**
   - c) After Module 4
   - d) At kick-off

   Feedback: Gate 1 comes after Module 2, once your CLOs, modules, character and conflict are
   drafted. Your ID checks them before you plan scenarios, because every scenario depends on
   them.

3. Who decides what topics your course covers?
   - **a) You**
   - b) Your ID
   - c) The Director of Learning Media
   - d) The AI in this tool

   Feedback: You are the subject matter expert. Your ID advises on how to teach the content
   online, and the AI drafts options, but the content decisions are yours.

### Decide

The faculty member enters their ID's name and, if known, a date for each gate meeting. Dates
can stay blank and be added later.

Checklist:

- You know which modules come before each gate.
- You have your ID's name, or you know who to ask for it.

### Save

Planning document: ID name on the cover section.
Project file: `course.idName`, `gates[1..3].date`.

---

## GS.3 What students need from you online

Time: about 20 minutes

### Learn

Online students judge a course by whether the instructor is there. Federal rules say the same
thing in their own terms.

**Regular and substantive interaction (RSI).** The U.S. Department of Education requires
online courses to include regular, substantive interaction that the instructor starts.
Posting materials and holding optional office hours does not meet the standard. Feedback on
student work, announcements that teach, and questions you pose in discussions or cohort
sessions do. Courses that fall short can be treated as correspondence courses, which affects
federal financial aid. Module 2 covers RSI in detail.

**Instructor presence.** Students notice whether you show up. Regular announcements, replies
to questions within 24 to 48 hours, and feedback that refers to what a student actually wrote
are the habits that research ties most closely to satisfaction and learning online (Garrison,
Anderson, & Archer, 2000).

**Connection between students.** Online students can go weeks without hearing from a
classmate. A good introduction discussion, peer review and live cohort sessions give them
reasons to talk to one another, and courses with that kind of contact see higher satisfaction
(Richardson & Swan, 2003).

**Your voice and face.** Short videos you record, a conversational writing tone and a few
moments where students hear how you think about the field make the course feel like a class
with you in it (Pacansky-Brock, 2020).

In a Flex Online course these habits run through every module. Cohort sessions are where
students apply and argue about what they have studied, and the storyline you build in Module 3
gives them shared problems to argue about.

### See it

In MGMT 615, students hear from the instructor every Monday in an announcement that picks up
Dana Ortiz's story where it left off and names the week's decision. Each week's cohort session
is a roundtable on that decision. The instructor returns written feedback on the module's main
assignment within five days and records one short video per module responding to common
mistakes.

### Draft (full build) and Review (refresh)

The faculty member writes a few sentences. The AI reads them and suggests one specific
addition.

Prompt shown to the faculty member: "In a normal week of your course, when and how will
students hear from you? Include anything you already do in your face-to-face classes that you
want to keep."

AI instructions:

```text
The faculty member described how students will hear from them in a typical week. Name the
interactions that are instructor-initiated and substantive. If none are scheduled on a fixed
day or within a stated time, suggest one specific, schedulable interaction that fits what they
wrote. Keep the reply under 80 words.

Return: {"interactions": [string], "suggestion": string}
```

Refresh track: if the uploaded document contains a communication plan or syllabus statement
about instructor contact, the app shows it in the text box as the starting answer.

Demo response (MGMT 615, refresh, no statement found in the course map, faculty typed an
answer):

Faculty answer: "I'll post an announcement each week and hold the cohort session. I grade
the main assignment and leave comments."

```json
{
  "interactions": [
    "Weekly announcement",
    "Weekly cohort session",
    "Comments on the main assignment"
  ],
  "suggestion": "Give the comments a turnaround time, such as feedback within five days of the due date, and say which day the announcement goes out. Students plan around both."
}
```

### Decide

The faculty member edits their answer and keeps or ignores the suggestion.

Checklist:

- At least one interaction happens every week on a set day.
- Feedback on work has a stated turnaround time.

### Save

Planning document: nothing yet.
Project file: `notes.weeklyContact`. Module 2 starts the syllabus RSI statement from this
answer.

### Go deeper (optional)

- Pacansky-Brock, M. (2020). How to humanize your online course.
- Richardson, J. C., & Swan, K. (2003). Examining social presence in online courses in relation
  to students' perceived learning and satisfaction. *Journal of Asynchronous Learning
  Networks, 7*(1), 68–88.
- Garrison, D. R., Anderson, T., & Archer, W. (2000). Critical inquiry in a text-based
  environment: Computer conferencing in higher education. *The Internet and Higher Education,
  2*(2–3), 87–105.

---

## GS.4 Your course and your track

Time: about 25 minutes

### Learn

The rest of the tool works from what you enter here, so it is worth getting right.

Choose a track:

- **Full build** if the course is new or you plan to rebuild it from the beginning. Each module
  drafts its sections from your course details.
- **Refresh** if the course already runs online and you have a course planning document or a
  syllabus. You upload it now. In each module the tool shows your current section, checks it
  against that module's checklist, and you keep it, accept or edit a suggested revision, or
  rewrite it. Each change gets a short note so your ID can see what changed and why.

Both tracks go through every module in order. Most existing courses have no character or
scenarios. In the refresh track, any section your document does not have runs as a full build.

You can upload a Word file (.docx) or paste text. A course map in the Flex Online planning
document format gives the best results. A syllabus works, but expect more sections to show as
missing.

### See it

The MGMT 615 instructor chose the refresh track and uploaded the course's existing course map.
The tool found the catalog description, the course vision, five CLOs and all eight modules
with their titles, topics, activities, materials and media. It found no program outcomes, no
character, no storyline or scenarios, and no communication plan. Those sections ran as full
builds when the instructor reached them.

### Draft (full build)

The faculty member fills in a form. No AI call.

Fields:

| Field | Required | Example (MGMT 615) |
|---|---|---|
| Course number | Yes | MGMT 615 |
| Course title | Yes | Managing People and Performance |
| Credit hours | Yes | 3 |
| Program | Yes | [Program name] |
| First term taught online | No | [Term] |
| New course or existing course | Yes | Existing |
| Who takes the course (a few sentences) | Yes | Working professionals, most in a first management role or about to step into one |

### Review (refresh)

The faculty member fills in the same form, then uploads or pastes their course document. The AI
sorts its contents into the planning document's sections.

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

Demo response (MGMT 615, from `Course Map_MGMT 615.docx`): the app plays back the recorded
extraction, summarized here.

| Section | Result |
|---|---|
| Catalog description | Found |
| Program outcomes | Missing |
| Course vision | Found |
| CLOs | Found, 5 |
| Modules | Found, 8, with titles, CLOs met, topics, objectives, activities, materials, media, cohort sessions and overviews |
| Character | Missing |
| Storyline and scenarios | Missing |
| Communication plan | Missing |
| Learners | Missing (faculty entered it in the form) |

> Review note: the recorded JSON for this response will be generated from the MGMT 615 course
> map when we build demo mode. Its full text is not repeated here.

### Decide

The tool shows each found section next to the label it was sorted under. The faculty member
confirms each one, moves misplaced text, or marks a section as not in the document.

Checklist:

- Course number, title and program are correct.
- Each found section is under the right label.
- You know which sections will run as a full build.

### Save

Planning document: course number and title in the document title; program on the cover
section.
Project file: `course`, `track`, `source.sections`, `source.missing`, `source.fileName`.
