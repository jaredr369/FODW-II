"""Bundle the content files into one self-contained prototype page.

Usage: python tools/build_prototype.py
Reads content/*.md, content/demo/*.json and content/sources.json, fills the
/*DATA*/ placeholder in prototype/src/template.html, and writes
prototype/index.html. Only source ids, titles, citations and public URLs are
bundled; internal file names and folders stay out of the page.
"""
import glob
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(ROOT, 'content')
MODULE_FILES = ['00-getting-started.md', '01-vision-and-foundation.md', '02-ai-and-rsi.md',
                '03-scenario-planning.md', '04-activities-and-ai.md', '05-materials.md',
                '06-media.md', '07-cohort-sessions.md', '08-readiness-and-teaching.md']


def read(path):
    with open(path, encoding='utf-8') as f:
        return f.read()


def main():
    modules = []
    for name in MODULE_FILES:
        raw = read(os.path.join(CONTENT, name))
        mod_id = next(line.split('`')[1] for line in raw.splitlines() if line.startswith('Module id:'))
        modules.append({'id': mod_id, 'file': name, 'raw': raw})

    demo = {os.path.basename(p): json.loads(read(p)) for p in glob.glob(os.path.join(CONTENT, 'demo', '*.json'))}

    sources = {}
    for s in json.loads(read(os.path.join(CONTENT, 'sources.json')))['sources']:
        sources[s['id']] = {k: s[k] for k in ('title', 'citation', 'url', 'path') if k in s}

    # The glossary is a Term | Also matches | Definition table in content/glossary.md.
    glossary = []
    for line in read(os.path.join(CONTENT, 'glossary.md')).splitlines():
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if len(cells) == 3 and cells[0] not in ('Term', '---') and not set(cells[0]) <= set('-'):
            also = [] if cells[1] in ('', '(glossary only)') else [a.strip() for a in cells[1].split(',') if a.strip()]
            glossary.append({'term': cells[0], 'also': also, 'def': cells[2], 'auto': cells[1] != '(glossary only)'})
    data = json.dumps({'modules': modules, 'demo': demo, 'sources': sources, 'glossary': glossary}, ensure_ascii=False)
    data = data.replace('</', '<\\/')
    template = read(os.path.join(ROOT, 'prototype', 'src', 'template.html'))
    assert '/*DATA*/null' in template
    out = template.replace('/*DATA*/null', data)
    with open(os.path.join(ROOT, 'prototype', 'index.html'), 'w', encoding='utf-8', newline='\n') as f:
        f.write(out)
    print('wrote prototype/index.html', len(out) // 1024, 'KB')


if __name__ == '__main__':
    main()
