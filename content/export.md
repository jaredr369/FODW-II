# Planning document export

How the app builds the Word planning document from `src:template-planning-doc` and the project
file. The tables come early, after a short set of foundation sections; everything below them
supports what's in them.

## Order

| # | Section | Filled in | Source in the project file | In the template? |
|---|---|---|---|---|
| 1 | Title: "[Course number] [Course title] Course Planning Document" | GS.4 | `course` | Yes |
| 2 | Planning Document Overview, with program and ID name | GS.2, GS.4 | `course.program`, `course.idName` | Yes (overview text only) |
| 3 | TAMU Catalog Course Description | 1.2 | `catalog.text` | Yes |
| 4 | Program-Level Outcomes (only those the course supports) | 1.2 | `programOutcomes` | Yes |
| 5 | Course Vision | 1.3 | `vision.text` | Yes |
| 6 | Learners | 1.1 | `learners.profile` | No, added |
| 7 | Course-Level Objectives (CLOs) | 1.4 | `clos` | Yes |
| 8 | Table 1, Modules 1 to 4 | Modules 1 to 7 | `modules[0..3]` | Yes, with a new Scenario row |
| 9 | Table 2, Modules 5 to 8 | Modules 1 to 7 | `modules[4..7]` | Yes, with a new Scenario row |
| 10 | Storyline: storyline premise and character profile | 2.5, Module 3 | `story` | No, added |
| 11 | Instructor Interaction: syllabus statement, then the communication and feedback plan | 2.3, Module 8 | `rsi.statement`, `communication` | No, added |
| 12 | Change log (refresh track only) | Every Review step | `*.original`, `*.changeNote` | No, added |
| 13 | Check-in summary (working copies only) | Every module | `checkins`, practice and reflection answers, open checklist items | No, added |

Sections 1 to 7 should fit on about one page, so the tables start on page one or two.

## Table rows

Both tables use the same rows. The left column says which workshop module fills the row. The
template's own labels for this column are off by one or two modules; the export uses the
numbers below, which follow `src:coursemap-v3`.

| Workshop module | Row | Project file |
|---|---|---|
| M1 | Module Titles | `modules[].title` |
| M1 | CLOs met | `modules[].closMet` |
| M1 | Module Topics | `modules[].topics` |
| M3 | Scenario (new row): episode title and premise statement, one per module | `modules[].scenario` |
| M4 | Learning Activities Plan Part 1 (Canvas Assignments) | `modules[].activities` |
| M4 | Learning Activities Plan Part 2 (Third-Party Tool Activities) | `modules[].toolActivities` |
| M5 | Learning Materials Plan | `modules[].materials` |
| M6 | Learning Media Plan | `modules[].media` |
| M7 | Learning Activities Plan Part 3 (Cohort Session Activities) | `modules[].cohort` |

Keep each Scenario cell short: the episode title and its one-sentence premise statement, such
as "The Handoff Nobody Owns. Dana struggles to fix the broken handoff between her two shifts
with a structural change when her director is pushing a team-building lunch." The full scenario
plan stays in the project file.

Empty rows show the template's bracketed placeholder until the faculty member reaches the
module that fills them.

## Storyline section

After the tables:

1. Storyline premise: one sentence for the whole course (Module 3).
2. Character profile: premise statement, position, conflict, peers, values and fears,
   backstory (step 2.5).

## Change log (refresh track)

One entry per section the faculty member reviewed, in document order: the section name, what it
was, what changed and why. Sections kept as they were are listed as "Kept" with no further
detail. Sections that ran as a full build because the original course had none are listed as
"New".

## Check-in summary

Added to working copies only, at the end, so the ID can prepare for a check-in without opening
the tool. Lists the modules finished since the last check-in, new and changed sections with
change notes, practice and reflection answers, and open items (unchecked checklist items and
AI flags the faculty member chose to keep). The app leaves it out when the faculty member
exports the final version for kick-off.

> Review note: the check-in summary assumes faculty share the exported Word document and
> project file with their ID before each check-in, for example in a shared OneDrive or Teams
> folder. That sharing workflow is not yet written into Getting Started.
