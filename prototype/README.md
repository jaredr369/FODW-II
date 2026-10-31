# Course Plan Builder prototype

A clickable prototype of the workshop for the leadership demo. It walks through Getting Started
and Modules 1 to 8 in either track with MGMT 615, a fictional course, and plays back the recorded
AI responses from `content/`, so it never needs a live AI connection.

Open `index.html` in Edge or Chrome. It's one self-contained file with no outside scripts, so it
works opened straight from disk.

## What it shows

- Track choice (Full build or Refresh), switchable at any time from the header.
- Each step's Learn, See it, Decide and Save parts, rendered from the module files.
- **Draft with AI** or **Review with AI** reveals the recorded MGMT 615 response after a short
  pause. "What the AI is asked to do" shows the instructions the real app would send.
- **Save to plan** marks the step done, shows the automatic checks, and fills in that part of the
  planning document.
- **Planning document** opens a preview in the order set by `content/export.md`. "Show the
  finished plan" fills every section for a quick look. **Download (Word)** saves the preview as a
  Word-readable file.
- Progress is kept in this browser; **Reset the demo** on the Welcome screen clears it.

## What it doesn't do yet

No live AI, file upload, folder saving, or real .docx export. Those come with the app build.

## Rebuilding

The page is generated. Edit `src/template.html` or the content files, then run:

```bash
python tools/build_prototype.py
```

Only source ids, titles, citations and public links are bundled; internal file names stay out.
