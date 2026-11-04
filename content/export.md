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
| 11 | Instructor Interaction: syllabus statement, then the communication and feedback plan | 2.1, Module 8 | `rsi.statement`, `communication` | No, added |
| 12 | Change log (refresh track only) | Every Review step | `*.original`, compared with the saved section | No, added |
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
   backstory (step 2.3).

## Change log (refresh track)

One entry per section the faculty member reviewed, in document order: the section name, what it
was, and what it is now. The tool builds it by comparing the saved section with the original from
the Course Map; faculty don't write change notes. Sections kept as they were are listed as "Kept" with no further
detail. Sections that ran as a full build because the original course had none are listed as
"New".

## Check-in summary

Added to working copies only, at the end, so the ID can prepare for a check-in without opening
the tool. Lists the modules finished since the last check-in, new and changed sections (on
the refresh track, what changed from the Course Map), practice and reflection answers, and open items (unchecked checklist items and
AI flags the faculty member chose to keep). The app leaves it out when the faculty member
exports the final version for kick-off.

Two save actions:

- **Save** writes a working copy, with the check-in summary.
- **Save final version** (shown once all eight modules are complete) writes the copy for
  kick-off, without the check-in summary and, if the faculty member chooses, without the
  change log.

## Saving

Nothing is submitted. Faculty share their plan by saving into a folder their ID can see.
Confirmed with Jared on Oct 31.

**Files.** Each save writes two files with fixed names, so later saves replace them:

- `[COURSE NUMBER] Course Planning Document.docx`, for example `MGMT 615 Course Planning Document.docx`
- `[COURSE NUMBER] Course Plan Builder project.json`

**Choosing the folder.** In browsers that support the File System Access API (Edge and Chrome),
Choose save folder opens the system folder picker (`showDirectoryPicker`). The app keeps the
folder handle in IndexedDB under `course-plan-builder:saveFolder`, so Save writes to the same
folder without asking again. The browser may ask the faculty member to allow access again in a
new session; the app requests write permission when Save is selected and explains why.

Any folder the computer can reach works: a local folder, a OneDrive or Teams folder synced to
the computer, or a Google Drive folder through Google Drive for desktop. Sharing the folder with
the ID is how the ID sees the plan.

**Other browsers.** Firefox and Safari have no folder picker. Save downloads both files, which
go to the Downloads folder, and the app reminds the faculty member to move them into the
shared folder.

**Opening a project.** Open project reads a project file (file picker, or drag and drop) and
replaces the work in this browser after a confirmation. This is how faculty move between
computers and how an ID can look at a plan in the tool.

**Browser autosave.** Separately from saving files, the app keeps the current work in
`localStorage` under `course-plan-builder:project` after every change, so closing the tab loses
nothing. Autosave holds one project per browser.

**One place for storage.** All reading and writing goes through two functions, `load()` and
`save()`, with the destination as a setting. A later direct save to Google Drive or OneDrive
is then one more destination. Neither is planned now: both need an app registration that TAMU
administrators approve (a Google Cloud project for Drive, a Microsoft Entra app for OneDrive).
The team currently works in OneDrive and is exploring Google Drive and Docs; revisit once that
choice is made.

**Google Docs.** A saved .docx opens in Google Docs for reading and comments. Keep the .docx as
the official copy, since converting the planning document's tables back and forth can shift
their formatting.

## Downloads

Three steps also offer a Word file to download: the video script (6.2), the run of show for the
first cohort session (7.2) and the Module 1 announcement sequence (8.2). They show faculty what
these documents look like and give them a head start for development. They aren't part of the
planning document, and faculty don't fill them out or submit them.
