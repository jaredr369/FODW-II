# Module 5. Learning Materials and Responsible Use

Module id: `m5`
Steps: 2
ID check-in: live review of this module's sections, at the end of the week or sooner

Faculty complete: the learning materials for each module, with rights status, attribution and
AI-use notes.

Refresh checks for this module: dated sources, missing attribution, unclear rights.

Sources: `src:reading-m5-materials-plan`, `src:assignment-m5-materials-rights-review`,
`src:assignment-m5-writing-attributions`, `src:guide-copyright`, `src:guide-curating-creating`,
`src:guide-instructor-authored-reading`, `src:guide-accessibility`,
`src:example-mgmt615-course-map`

Demo data: `demo/mgmt615-materials.json`

## Refresh reflection

Shown once, in the refresh track only, before step 5.1. It asks only about materials the course
already has.

1. Which readings or videos did students skip, struggle with, or tell you were out of date?
2. Which materials do students still bring up later in the course?
3. Is there anything you've been meaning to replace?
4. Which materials would you keep exactly as they are?

AI instructions: same as the Module 1 reflection instruction.

Demo answers (MGMT 615): (1) "The SBI job aid confuses people; it's a photocopy of a diagram."
(2) "The Marsh chapters." (3) "Nothing specific." (4) "Both Marsh chapters and the Park and Marsh
article."

Project file: `reflection.m5`.

---

## 5.1 Materials for every module

Time: about 40 minutes, about 5 minutes a module
Pattern: pick and combine, one module at a time (full build); edit in place (refresh)

### Learn

Learning materials are everything that isn't an activity: what students read, watch or work with
to get ready for the module's decision. Every item should earn its place by preparing students
for a specific activity.

Choose from least to most effort to produce:

| Type | Effort | Use when |
|---|---|---|
| Curated reading (article, chapter, report, case) | Lowest | A good source exists. This is the default. |
| Curated video | Low | An existing video covers it well. |
| Instructor-authored reading (4 to 10 pages) | Several hours each | Nothing curated fits, or your own experience is the point. |
| Interactive reading (built by your ID) | High | Complex content that benefits from short sections and checks. |
| Instructor-recorded video | Highest | Planned in Module 6, up to 30 minutes a module. |

**Your scenario is a material too.** The narrative, and any exhibits the character works from (an
email from a boss, a dashboard, a complaint), are created content. List them.

**Finding sources with AI.** Perplexity is licensed through the university and cites its sources,
which makes its suggestions easy to check. Describe the CLO, topic, your students and the kind
of source you want. Check every suggestion before you list it: authored by someone credible,
current, stable, and tied to an objective. Start with TAMU Libraries, and link to the library
record instead of uploading a PDF.

**Load.** Aim for roughly 20 pages of required reading a module, adjusted for density. With 4 to
5 hours of activities and a 90-minute cohort session, that keeps the week near 10 hours. Module 1
targets about 4 hours in all, so keep its reading to a few pages.

### See it

MGMT 615 Module 4, after the refresh: an 11-page article on what predicts team performance, the
Team That Couldn't Ship case as a contrast, and a 4-page interactive reading, "Diagnose the Team,
Not the Person." A supplemental article on designing team assignments was removed because it was
about course design. About 21 pages.

### Draft (full build)

The AI can't verify that a specific source exists, so it never names one. It suggests what each
module needs and how to find it; the faculty member enters the actual sources.

AI instructions:

```text
For the given module, using its CLOs, topics, scenario and activities, propose two versions of a
materials list. Each item gives: type (curated reading, curated video, instructor-authored
reading, interactive reading, scenario exhibit), what it must cover, the activity it prepares
students for, and an estimated page count or minutes. Prefer curated types. Always include the
scenario narrative and any exhibits the character works from. Never name a specific article,
book, author or video. For each curated item, write one search prompt the faculty member can
paste into Perplexity or the TAMU Libraries search.

Return: {"versions": [{"items": [{"type": string, "covers": string, "supports": string, "pages": number | null, "minutes": number | null, "searchPrompt": string | null}]}]}
```

Demo response (MGMT 615, Module 8, if run as a full build): a curated research article on
structured interviews against unstructured ones (about 10 pages; search prompt "peer-reviewed
meta-analysis structured versus unstructured interviews predictive validity, written for
practicing managers"), two candidate files as scenario exhibits, and an interactive reading on
weighing proven experience against potential.

### Review (refresh)

Edit in place. The app lists each module's current materials from the upload. The faculty member
adds anything missing.

AI instructions:

```text
For each current material in the given module, check: it prepares students for a named activity;
it is content for students; its date (flag anything older than 5 years unless it is a classic in
the field, and say so); the scenario narrative and exhibits are listed. Suggest keep, replace
(say what a replacement should cover, never a specific source), or remove, with a reason. Add
missing scenario exhibits.

Return: {"items": [{"original": string, "action": "keep" | "replace" | "remove", "issues": [string], "replacementCovers": string | null}], "add": [string]}
```

Demo response (MGMT 615): `review` notes in `demo/mgmt615-materials.json`. Main findings: the
Module 4 course-design article removed; scenario exhibits added in four modules; the 2019 book
chapters flagged as dated and kept after the instructor confirmed no newer edition.

### Decide

For each item the faculty member enters or confirms the source (title, author, year, link).

Checklist:

- Every item prepares students for a named activity.
- The scenario and its exhibits are listed.
- You've checked each curated source yourself.

### Checks

On save of each module: every item tied to an activity; required pages and minutes total (flag
over about 25 pages, or about 8 in Module 1, adjusted for type); items older than 5 years flagged; scenario listed. After
saving, the week-in-your-student's-shoes walk-through for the module refreshes with the real
reading load.

### Save

Planning document: Learning Materials Plan row in Tables 1 and 2, one line per item, for example
"Article: Park & Marsh (2024), What actually predicts team performance (11 pp.)".
Project file: `modules[].materials`; in refresh, `.original`, `.changeNote`.

### Go deeper (optional)

- `src:guide-curating-creating`
- `src:guide-instructor-authored-reading`
- `src:guide-accessibility`

---

## 5.2 Rights, attribution and AI notes

Time: about 25 minutes
Pattern: spot the problem, then edit in place

### Learn

Everything you use is protected by copyright unless it says otherwise, and the lack of a notice
doesn't make it free. For each material, you need one of four things: a library link, an open
license, a public page or video you link to (never download and re-upload), or permission. When
you're unsure, link instead of uploading.

**Fair use** can cover limited educational use, but it's a judgment on four factors: purpose,
the nature of the work, how much you use, and the effect on the market. It's never blanket
permission, and paywalled content can't be uploaded for students.

**Attribution** credits the creator: name, title, source and license. Use it even when the
license doesn't require it.

**AI-assisted content.** If you used AI to draft a scenario, an exhibit, an image or part of a
reading, tell students. Check it for accuracy and for anything that closely reproduces someone
else's work, and ask your ID before treating it as your own original work. The U.S.
Copyright Office has said that purely AI-generated material isn't protected by copyright.

**Spot the problem.** The app shows one item and asks what's wrong with it:

> "Image: diagram of the SBI feedback model, found through a web image search. Used on slide 3
> and in the job aid."

Expected points: no creator or license, so the rights are unclear; it's reused in two places.
Fix: find a licensed version, or redraw it as your own content and attribute the model.

### See it

MGMT 615's SBI job aid was a photocopied diagram with no attribution, and the instructor's
reflection said students found it confusing. The instructor redrew it as a one-page created job
aid, with the line "Based on the Situation-Behavior-Impact model (Center for Creative
Leadership)." Two AI-drafted items, the Module 2 bonus sheet and the Module 6 AI job aid, got a
disclosure note: "Drafted with AI assistance and reviewed by the instructor."

### Draft (full build) and Review (refresh)

Same for both tracks. The app shows every material in one table with its rights status. The
faculty member answers, for each item, where it came from and whether AI helped make it. The AI
proposes the rights status, an attribution line and any AI-disclosure note.

AI instructions:

```text
For each material, from the faculty member's answers (source, link, license if known, whether AI
helped create it), set rights to one of: library, open (name the license), public (linked, not
uploaded), created, ai-assisted, unclear. Write an attribution line with creator, title, source
and license where known; do not invent missing details, use [check] instead. For ai-assisted
items, write a one-sentence disclosure note. For unclear items, suggest the safest fix: link
instead of upload, find a licensed alternative, or recreate it.

Return: {"items": [{"title": string, "rights": string, "attribution": string, "aiNote": string | null, "fix": string | null}]}
```

Demo response (MGMT 615): the `rights` values in `demo/mgmt615-materials.json`, with fixes for the
two unclear items (Maria's case marked created after the instructor confirmed writing it; the SBI
job aid redrawn) and disclosure notes on the two AI-assisted items.

### Decide

Checklist:

- Every item has a rights status other than unclear, or a fix you'll make.
- Nothing paywalled is uploaded.
- Every AI-assisted item has a disclosure note.

### Checks

On save: no item left unclear without a fix; every item has an attribution or is the faculty
member's own created work; every ai-assisted item has a note; any "upload" of a library or
paywalled item is flagged.

### Save

Planning document: each material line in the Learning Materials Plan row gains its rights status
and, for AI-assisted items, "(AI-assisted, disclosed)". Full attribution lines go to the project
file and the check-in summary.
Project file: `modules[].materials[].rights`, `.attribution`, `.aiNote`.

### Go deeper (optional)

- `src:guide-copyright`
- `src:assignment-m5-writing-attributions`
- `src:ext-copyright-office-ai`

---

## Check-in prep

Same instructions as Module 1.

Demo response (MGMT 615):

```json
{
  "changed": ["Materials for all eight modules, about 17 to 24 pages each", "Scenario exhibits added in four modules", "SBI job aid redrawn and attributed", "AI disclosure on two items"],
  "keptFlags": ["Whitfield (2019) chapters kept: no newer edition"],
  "questions": ["Can the Learning Media team redraw the SBI job aid, or should I?", "Do the created cases from earlier terms need any review before reuse?"]
}
```

Project file: `checkins.prep.m5`.
