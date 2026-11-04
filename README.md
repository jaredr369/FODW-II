# FODW II: Course Plan Builder

The Flex Online Design Workshop II as a web tool. Faculty build a Course Planning Document for a
new Flex Online course (Full build), or review and update the Course Map of a course they already
teach (Refresh), one module a week with their instructional designer.

**Open the tool:** https://jaredr369.github.io/FODW-II/

## How it works

- **Plan my course** uses the faculty member's own answers. Every box is kept in their browser as
  they type, and **Save to plan** writes their project file and planning document to the folder they
  choose (Edge and Chrome) or downloads them. **Open a project file** on the Welcome page picks the
  work back up on any computer.
- **Try the example** walks through the workshop with MGMT 615, a fictional course, using recorded
  AI responses.
- **TAMU AI Chat.** Faculty paste their own TAMU AI key in Getting Started (step GS.1). The key is
  kept in their browser only, never in the project file. Each step sends its AI instructions, the
  shared rules in `content/ai-rules.md`, and what the faculty member has saved so far.
- **Settings**, at the top of every page, shows the AI connection, the model, and the save folder.

## Editing the content

The workshop's text lives in `content/` (one file per module). **Edit** in the header outlines
every piece of text that can be changed in place. It shows when the tool is opened from your own
computer, or online with `?edit` at the end of the address. Click and type; **Save edits**
downloads `fodw-edits-<date>.json`. Then apply it to the content files and rebuild:

```bash
python tools/apply_edits.py
```

With no file named, it uses the newest `fodw-edits-*.json` in Downloads. Edits already in the files
are skipped, and anything it can't place is listed for a person to handle.

## Rebuilding

`index.html` is generated. Edit `src/template.html` or the files in `content/`, then run:

```bash
python tools/build.py
```

Only source ids, titles, citations and public links are bundled; internal file names stay out.
GitHub Pages publishes `index.html` from the main branch.
