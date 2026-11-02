# Course Plan Builder content

One file per module. The app reads these files; faculty never see this README.

| File | Module |
|---|---|
| `ai-rules.md` | Instructions shared by every AI call |
| `sources.json` | Every source the content draws on, with a stable id |
| `export.md` | Layout of the Word planning document the app exports |
| `00-getting-started.md` | Getting Started |
| `01-vision-and-foundation.md` | Module 1. Creating Vision and Foundation |
| `02-ai-and-rsi.md` | Module 2. AI & RSI in Strategic Course Design |
| `03-scenario-planning.md` | Module 3. Scenario Planning and the Learner's Journey |
| `04-activities-and-ai.md` | Module 4. Intentional AI Implementation for Engagement & Feedback |
| `05-materials.md` | Module 5. Learning Materials and Responsible Use |
| `06-media.md` | Module 6. Audiovisual Aspects of Storytelling |
| `07-cohort-sessions.md` | Module 7. Cohort Session Planning |
| `08-readiness-and-teaching.md` | Module 8. Development Readiness and Sustainable Teaching |
| `demo/` | Recorded MGMT 615 demo data too long to keep inside a module file |

## The design rule

Every step writes a section of the planning document, or checks one. The workshop's job is to
get faculty to a finished plan quickly. Practice exercises, knowledge checks, discussion posts,
annotated readings and anything built outside the app are left out; anything worth keeping
from them moves into Go deeper or the weekly ID check-in.

## How a step is written

Each step has the same parts, in this order:

- **Pattern**: which activity pattern the step uses (below).
- **Learn**: what faculty need to make this decision, about 2 minutes.
- **See it**: the MGMT 615 example (Dana Ortiz course).
- **Draft** (full build track) and **Review** (refresh track): what the AI does. Each has an
  `AI instructions` block for the app and a `Demo response` block that demo mode plays back.
  Faculty can open the instructions under "What the AI is asked to do." Its last line,
  `Return: {...}`, is the format the software needs back; it is never shown to faculty.
- **Decide**: what the faculty member edits, chooses or rejects, and the checklist shown beside it.
  In a step with an AI draft or review, each Decide box has **Redraft with AI**. It sends the box's
  current text, the faculty member's optional note on what should change, and the step's AI
  instructions, and returns a new version of that box only.
- **Checks**: the automatic checks that run when the section is saved.
- **Save**: where the result goes in the planning document and in the project file.
- **Go deeper (supplemental)**: readings and tools that build on the step.

## Activity patterns

| Pattern | How it works | Use for |
|---|---|---|
| Interview, then draft | The AI asks 3 to 5 short questions, then drafts from the answers. | Sections that need the faculty member's knowledge: learners, vision, character, interaction statement |
| Pick and combine | The AI offers 2 or 3 versions. Faculty choose one, merge parts, or ask for another. | Creative sections: scenarios, activities, storyline |
| Edit in place | Refresh track. The current section appears with flags beside it. Faculty fix each flag or keep it with a short note. | Every Review step |
| Spot the problem | One weak MGMT 615 example. Faculty say in a sentence what's wrong; the AI confirms or adds what they missed. About 2 minutes. | A concept faculty need before drafting, such as a measurable CLO |
| A week in your student's shoes | The AI walks through one module's week as a student: what they read, do and submit, what they hear from the instructor, and the hours. Faculty react to what feels heavy, thin or silent. | Activities, materials, media and cohort sessions (Modules 4 to 7) |

## Automatic checks

Checks run when a section is saved and show as flags beside it. They never get a step of their
own. Each flag offers Fix (back to the section) or Keep, with a short note the ID will see. A
module can't be marked complete while a flag has neither a fix nor a note.

## Check-in prep

Each module ends with a one-minute screen for the next ID check-in: sections new or changed
since the last check-in, flags kept with their notes, and two questions the AI suggests raising
with the ID. The same content goes into the check-in summary in the Word export (see
`export.md`).

Without AI (faculty who chose Continue without AI in GS.1): Learn, See it, Decide and Save
work the same. Draft and Review are replaced by a text box (empty in the full build, holding the
current section in the refresh track) next to the step's checklist. The refresh reflection is
still shown and saved for the ID.

## Sources

Content files never name a source file directly. They use its id from `sources.json`, written
as `` `src:<id>` ``, for example `` `src:guide-rsi` ``. The app turns each id into the citation
and, for public sources, a link. Each module file lists the sources it draws on under its
header, and Go deeper lists are made of ids.

Ids follow `<kind>-<slug>`, such as `guide-storytelling` or `assignment-m2-character-conflict`.
The module a source belongs to is a field in the registry and follows the V3 course map, even
when the source file itself is labeled with a different module. Ids never change once used.

The reference files are internal and read-only. They stay out of this repo; the registry holds
only their names, so a maintainer can find them.

Notes for reviewers are in blocks that start with `> Review note:`. The app ignores them.

## Example course

MGMT 615: Managing People and Performance is a made-up course. Dana Ortiz, the company,
and every other person in the example are fictional. Readings and program outcomes in the
MGMT 615 example are fictional too.
