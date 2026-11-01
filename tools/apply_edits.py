"""Apply edits saved from the prototype's Edit mode to the content files, then rebuild.

Usage: python tools/apply_edits.py [edits.json]
With no file named, uses the newest fodw-edits-*.json in the Downloads folder. Each edit names
a content file and the exact source text it replaces. An edit whose text is already in place is
skipped; one whose source text can't be found once is reported and left for a person.
"""
import glob
import json
import os
import subprocess
import sys
import textwrap

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(ROOT, 'content')
WIDTH = 100


def wrap(edit):
    """Rewrap a paragraph or list item to the content files' line width."""
    new = edit['new']
    if edit['kind'] == 'p':
        return textwrap.fill(new, WIDTH, break_long_words=False, break_on_hyphens=False)
    if edit['kind'] == 'li':
        marker = edit.get('marker') or '- '
        old_lines = edit['old'].split('\n')
        cont = old_lines[1][:len(old_lines[1]) - len(old_lines[1].lstrip())] if len(old_lines) > 1 else ' ' * len(marker)
        text = textwrap.fill(new, WIDTH, initial_indent=marker, subsequent_indent=cont,
                             break_long_words=False, break_on_hyphens=False)
        return text[len(marker):]
    return new


def norm(s):
    return ' '.join(s.split())


def newest_download():
    found = glob.glob(os.path.join(os.path.expanduser('~'), 'Downloads', 'fodw-edits-*.json'))
    return max(found, key=os.path.getmtime) if found else None


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else newest_download()
    if not path:
        sys.exit('No fodw-edits-*.json file found in Downloads.')
    with open(path, encoding='utf-8') as f:
        edits = json.load(f)['edits']
    print('Applying', len(edits), 'edits from', os.path.basename(path))

    applied, already, problems = 0, 0, []
    for e in edits:
        target = os.path.join(CONTENT, e['file'].replace('/', os.sep))
        with open(target, encoding='utf-8', newline='') as f:
            text = f.read()
        if e['kind'] == 'json':
            old, new = json.dumps(e['old'], ensure_ascii=False), json.dumps(e['new'], ensure_ascii=False)
        else:
            old, new = e['old'], wrap(e)
        if '\r\n' in text:
            old, new = old.replace('\n', '\r\n'), new.replace('\n', '\r\n')
        n = text.count(old)
        if norm(new) in norm(text) and (n == 0 or norm(old) in norm(new)):
            already += 1
        elif n == 1:
            with open(target, 'w', encoding='utf-8', newline='') as f:
                f.write(text.replace(old, new))
            applied += 1
        else:
            problems.append((e, 'source text found %d times' % n))

    print('Applied:', applied, ' Already in place:', already, ' Need a person:', len(problems))
    for e, why in problems:
        print('-', e['file'], e.get('step', ''), '(' + why + '):', e['new'][:80])
    if applied:
        subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'build_prototype.py')], check=True)


if __name__ == '__main__':
    main()
