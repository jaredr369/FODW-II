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
| `demo/` | Recorded MGMT 615 demo data too long to keep inside a module file |

## How a step is written

Each step has the same parts, in this order:

- **Learn**: required reading shown to everyone, about 3 to 5 minutes.
- **See it**: the MGMT 615 example (Dana Ortiz course).
- **Draft** (full build track) and **Review** (refresh track): what the AI does. Each has an
  `AI instructions` block for the app and a `Demo response` block that demo mode plays back.
- **Decide**: what the faculty member edits, chooses or rejects, and the checklist shown beside it.
- **Save**: where the result goes in the planning document and in the project file.
- **Go deeper**: optional supplemental material.

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
and every other person in the example are fictional. Readings cited in the MGMT 615 example
are fictional too.
