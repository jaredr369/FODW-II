# Module 5. Learning Materials and Responsible Use

Module id: `m5`
Steps: 2
ID check-in: live review of this module's sections, at the end of the week or sooner

Faculty complete: the learning materials for each module, with rights status, attribution, and
AI-use notes.

Refresh checks for this module: dated sources, missing attribution, unclear rights.

Sources: `src:reading-m5-materials-plan`, `src:assignment-m5-materials-rights-review`,
`src:assignment-m5-writing-attributions`, `src:guide-copyright`, `src:guide-curating-creating`,
`src:guide-instructor-authored-reading`, `src:guide-accessibility`,
`src:example-mgmt615-course-map`

Demo data: `demo/mgmt615-materials.json`

## Refresh reflection

> App note: Shown once, in the refresh track only, before step 5.1. It asks only about materials the
> course already has.

::: purpose
**What you'll do:** Answer a few questions about the materials in the last version of your course.
Answer whichever apply; short notes are fine.

**Why it matters:** The AI uses your answers when it reviews each section in this module, so its
suggestions reflect what actually happened in your course.
:::

1. Which readings or videos did students skip, struggle with, or tell you were out of date?
2. Which materials do students still bring up later in the course?
3. Is there anything you've been meaning to replace?
4. Which materials would you keep exactly as they are?

> App note: AI instructions are the same as the Module 1 reflection instruction.

Demo answers (MGMT 615): (1) "The SBI job aid confuses people; it's a photocopy of a diagram."
(2) "The Marsh chapters." (3) "Nothing specific." (4) "Both Marsh chapters and the Park and Marsh
article."

Project file: `reflection.m5`.

---

## 5.1 Materials for every module

Time: about 40 minutes, about 5 minutes a module
Pattern: pick and combine, one module at a time (full build); edit in place (refresh)

### Learn

::: purpose
::: full
**What you'll do:** Plan the learning materials for each module: what students will read, watch, or
work with to get ready for the module's decision.
:::

::: refresh
**What you'll do:** Review and update the learning materials for each module: what students read,
watch, or work with to get ready for the module's decision.
:::

**Why it matters:** Materials fill much of a student's week, so each item should earn its place by
preparing students for a specific activity.
:::

::: refresh
You planned your materials in your first workshop. As you review, check that each item still
prepares students for a named activity, that sources are current, and that each module's required
reading stays between 5 and 25 pages. Below is what's new since then: your scenario as a material, and
finding sources with AI.

**Too much, not too weak.** Sometimes every material is good but a module simply has more than a
week can hold. You don't have to cut anything: move some items to **Supplemental**. Supplemental items stay in
the module for students who want more, but they're optional, no activity depends on them, and they
don't count toward the week.
:::

::: refresher
Learning materials are everything in a module that isn't an activity. The types below run from
least to most effort to produce:

| Type | Effort | Use when |
|---|---|---|
| Curated reading (article, chapter, report, case) | Lowest | A good source exists. This is the default. |
| Curated video | Low | An existing video covers it well, in 6 to 10 minutes or less. |
| Instructor-authored reading (4 to 10 pages) | Several hours each | Nothing curated fits, or your own experience is the point. |
| Interactive reading (built by your ID) | High | Complex content that benefits from short sections and knowledge checks. |
| Instructor-recorded video | Highest | Planned in Module 6, up to 30 minutes of scripted video and audio a module. |
:::

**Your scenario is a material too.** The narrative, and any exhibits the character works from (an
email from a boss, a dashboard, a complaint), are created content. List them with your other
materials.

**Finding sources with AI.** TAMU AI Chat allows you to sign in with your university credentials and
offers several AI models to choose from. In your request, describe the CLO, the topic, your
students, and the kind of source you want. Check every suggestion before you list it. Each source should have a credible
author, be current and stable, and tie to an objective. You can also search TAMU Libraries. Link to
the library record instead of uploading a PDF, so there's no file to manage in Canvas.

::: refresher
**Load.** Plan 5 to 25 pages of required reading per module, adjusted for how dense the reading
is. At 6 to 10 pages
an hour, that's about 1 to 3 hours. With up to 30 minutes of scripted video and audio, a few short
curated videos, roughly 6 hours of activities, and the 90-minute cohort session, the week comes to
close to 10 hours. Module 1 targets about 4 hours in all, so keep any reading in it light.
:::

### See it

::: full
Here's the materials plan the MGMT 615 instructor settled on for Module 4. Every item prepares
students for the team diagnosis memo, and the reading comes to about 21 pages.
:::

::: refresh
Here's MGMT 615's Module 4 after the review. A supplemental article on designing team assignments
was removed because it was about course design, not content for students. The reading comes to
about 21 pages.
:::

::: plan Learning Materials Plan, Module 4
- Article: Park & Marsh (2024), What actually predicts team performance (11 pp.)
- Case: The Team That Couldn't Ship, a contrast case (6 pp.)
- Interactive reading: Diagnose the Team, Not the Person (4 pp.)
:::

### Draft (full build) and Review (refresh)

::: full
Work through your modules one at a time. Choose a module, then select the button below. The AI
suggests what the module's materials should cover, from its CLOs, topics, scenario, and activities.
It can't check that a specific source exists, so it never names one: for each curated reading it
gives a search prompt you can paste into TAMU AI Chat or the TAMU Libraries search. Select **Use
these materials** to copy the list into the boxes under Decide, then replace each suggestion with
the source you choose.
:::

::: refresh
Work through your modules one at a time. Choose a module, then select the button below. The AI
starts from your Course Map's current materials for the module. It checks each one, says what it
would keep, replace, move to Supplemental, or remove and why, and adds any scenario exhibits that
are missing. It never
names a new source; for a replacement it gives a search prompt instead. Select **Use these
materials** to copy the reviewed list into the boxes under Decide.
:::

::: module-picker
:::

::: current materials
:::

::: full
AI instructions:

```text
For the given module, using its CLOs, topics, scenario, and activities, propose a materials list.
Each item gives: type (curated reading, curated video, instructor-authored reading, interactive
reading, scenario exhibit), what it must cover, the activity it prepares students for, and an
estimated page count or minutes. Prefer curated types. Always include the scenario narrative and any
exhibits the character works from. Never name a specific article, book, author, or video. For each
curated item, write one search prompt the faculty member can paste into TAMU AI Chat or the TAMU
Libraries search.

Return: {"items": [{"type": string, "covers": string, "supports": string, "pages": number | null, "minutes": number | null, "searchPrompt": string | null}]}
```
:::

::: refresh
AI instructions:

```text
For each current material in the given module, check: it prepares students for a named activity;
it is content for students; its date (flag anything older than 5 years unless it is a classic in
the field, and say so); the scenario narrative and exhibits are listed. Suggest keep, replace (say
what a replacement should cover, never a specific source), supplemental, or remove, with a reason.
If required reading is over 25 pages (about 8 in Module 1) and the items are sound, suggest moving
the ones that least directly prepare students for the main activity to supplemental instead of
removing them, until the module is back in range. Supplemental items don't count toward the load.
Add missing scenario exhibits.

Return: {"items": [{"original": string, "action": "keep" | "replace" | "supplemental" | "remove", "issues": [string], "replacementCovers": string | null}], "add": [string]}
```
:::

Demo response (MGMT 615):

::: module-options
:::

### Decide

Your final materials for each module go in this box. Type in it to change anything, or select
**Redraft with AI** under it to have the AI rewrite it. To work on another module, choose it above;
what you've typed is kept.

For each item, give the type, the title, the author and year if it has them, the pages or minutes,
and the activity it prepares students for. Start a line with "Supplemental:" for an optional item;
it stays in the module but isn't counted. The required reading pages feed the week check in Module
4.

::: module-fields
:::

Checklist:

- Every item prepares students for a named activity.
- The scenario and its exhibits are listed.
- You've checked each curated source yourself.

### Checks

When you save each module, the tool checks that:

- every required item is tied to an activity;
- required reading comes to 5 to 25 pages (about 8 or fewer in Module 1), adjusted for how dense it
  is;
- items older than 5 years are flagged unless they're classics;
- the scenario and its exhibits are listed.

The week check in Module 4 then uses your real reading load instead of an estimate.

### Save

Planning document: Learning Materials Plan row in Tables 1 and 2, one line per item, for example
"Article: Park & Marsh (2024), What actually predicts team performance (11 pp.)". Supplemental items
are listed last, marked "Supplemental".
Project file: `modules[].materials`; in refresh, `.original`, `.changeNote`.

### Go deeper (supplemental)

- `src:guide-curating-creating`
- `src:guide-instructor-authored-reading`
- `src:guide-accessibility`

---

## 5.2 Rights, attribution, and AI notes

Time: about 25 minutes
Pattern: spot the problem, then edit in place

### Learn

::: purpose
::: full
**What you'll do:** For each material, record its rights status, an attribution line, and a note if
AI helped make it.
:::

::: refresh
**What you'll do:** Review the rights status, attribution line, and AI note for each material, and
update any that are missing or out of date.
:::

**Why it matters:** Using material without the right permission puts you and the university at legal
risk. Clear attributions and AI notes also show students the integrity you ask of them.
:::

::: refresh
You covered copyright and attribution in your first workshop. As you review, check that every
material still has a library link, an open license, a public link, or permission, plus an
attribution line. Below is what's new since then: a note for anything made with AI.
:::

::: refresher
Everything you use is protected by copyright unless it says otherwise, and the lack of a notice
doesn't make it free. For each material, you need one of four things. Check for them in this
order:

::: figure trace | Can I use it? Check in this order
- 1. Is it in TAMU Libraries? | Link to the library record. Students sign in with their NetID.
- 2. Does it have an open license, such as Creative Commons? | Use it, and name the license in your attribution.
- 3. Is it a public page or video? | Link to it. Never download it and re-upload it.
- 4. None of these? | Ask the owner for permission, or choose something else.
- Credit | Based on the Mays Teaching & Learning Innovation guide to copyright and fair use.
:::

When you're unsure, link instead of uploading.

**Fair use** can cover limited educational use, but it's a judgment on four factors: purpose,
the nature of the work, how much you use, and the effect on the market. It's never blanket
permission, and paywalled content can't be uploaded for students.

**Attribution** credits the creator: title, author, source, and license. Include an attribution
even when the license doesn't require one.
:::

**AI-assisted content.** If you used AI to draft a scenario, an exhibit, an image, or part of a
reading, tell students. Check it for accuracy and for anything that closely reproduces someone
else's work, and ask your ID before treating it as your own original work. The [U.S.
Copyright Office](src:ext-copyright-office-ai) has said that purely AI-generated material isn't protected by copyright.

**Spot the problem.** Before you check your own materials, practice on one. Read the item below,
say in a sentence or two what's wrong with it and how you'd fix it, then select **Check my
answer**.

> Item: "Image: diagram of the SBI feedback model, found through a web image search. Used on
> slide 3 and in the job aid."

::: check
- What's wrong with this item, and how would you fix it?
Feedback: You're right if you spotted that the rights are unclear: there's no creator or license, so
you can't tell whether you may use it. It's also reused in two places, so the problem doubles. Fix
it by finding a licensed version, or by redrawing it as your own content with an attribution line
for the model: "Based on the Situation-Behavior-Impact model (Center for Creative Leadership)."
:::

### See it

MGMT 615's SBI job aid was a photocopied diagram with no attribution, and the instructor's
reflection said students found it confusing. The instructor redrew it as a one-page job aid of their
own. Two items were drafted with AI, so each got a disclosure note.

::: plan Learning Materials Plan, Module 3 (rights)
- Book chapter: Marsh (2021), Ch. 4: Feedback That Lands (library)
- Job aid: The SBI Feedback Model, One Page (created). Based on the Situation-Behavior-Impact model (Center for Creative Leadership).
- Interactive reading: Script Your Feedback Conversation (created)
:::

### Draft (full build) and Review (refresh)

::: full
Work through your modules one at a time. Choose a module, then select the button below. The AI
proposes each material's rights status, an attribution line, and, for anything made with AI help,
a disclosure note. It never invents missing details: anything you need to confirm is marked
[check]. Select **Use these notes** to copy them into the boxes under Decide.
:::

::: refresh
Work through your modules one at a time. Choose a module, then select the button below. The AI
starts from the rights notes and attributions in your Course Map. It flags any rights status that's
unclear, any attribution that's missing or incomplete, and any AI-assisted item without a note, and
suggests a fix for each. It never invents missing details: anything you need to confirm is marked
[check]. Select **Use these notes** to copy them into the boxes under Decide.
:::

::: module-picker
:::

AI instructions:

```text
For each material, from the faculty member's answers (source, link, license if known, whether AI
helped create it), set rights to one of: library, open (name the license), public (linked, not
uploaded), created, ai-assisted, unclear. Write an attribution line with creator, title, source,
and license where known; do not invent missing details, use [check] instead. For ai-assisted
items, write a one-sentence disclosure note. For unclear items, suggest the safest fix: link
instead of upload, find a licensed alternative, or recreate it. If the Course Map already has rights
notes or attributions, start from them and flag what's unclear, missing, or out of date.

Return: {"items": [{"title": string, "rights": string, "attribution": string, "aiNote": string | null, "fix": string | null}]}
```

Demo response (MGMT 615):

::: module-options
:::

### Decide

Your final rights notes for each module go in these boxes. Type in any box to change it, or select
**Redraft with AI** under a box to have the AI rewrite just that part. Confirm or replace anything
marked [check].

::: module-fields
:::

Checklist:

- Every item has a rights status other than unclear, or a fix you plan to make.
- Nothing paywalled is uploaded.
- Every AI-assisted item has a disclosure note.

### Checks

When you save each module, the tool confirms that:

- no item is left unclear without a fix;
- every item has an attribution or is your own created work;
- every AI-assisted item has a disclosure note;
- no library or paywalled item is marked for upload.

### Save

Planning document: each material line in the Learning Materials Plan row gains its rights status
and, for AI-assisted items, "(AI-assisted, disclosed)". Full attribution lines go to the project
file and the check-in summary.
Project file: `modules[].materials[].rights`, `.attribution`, `.aiNote`.

### Go deeper (supplemental)

- `src:guide-copyright`
- `src:ext-copyright-office-ai`

---

## Check-in prep

Same instructions as Module 1.

Demo response (MGMT 615):

```json
{
  "changed": ["Materials for all eight modules, about 17 to 24 pages each", "Scenario exhibits added in four modules", "SBI job aid redrawn and attributed", "AI disclosure on two items"],
  "keptFlags": ["Whitfield (2019) chapters kept: no newer edition"],
  "questions": ["Can the Learning Media Team redraw the SBI job aid, or should I?", "Do the created cases from earlier terms need any review before reuse?"]
}
```

Project file: `checkins.prep.m5`.
