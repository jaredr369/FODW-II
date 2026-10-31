"""Convert .docx to plain text with stdlib only. Keeps paragraphs, table rows, and hyperlink targets."""
import sys, zipfile, re
from xml.etree import ElementTree as ET

W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
R = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'


def rels(z):
    try:
        x = ET.fromstring(z.read('word/_rels/document.xml.rels'))
    except KeyError:
        return {}
    return {e.get('Id'): e.get('Target') for e in x}


def para_text(p, links):
    out = []
    for node in p:
        tag = node.tag
        if tag == W + 'r':
            for t in node.iter():
                if t.tag == W + 't':
                    out.append(t.text or '')
                elif t.tag == W + 'tab':
                    out.append('\t')
                elif t.tag == W + 'br':
                    out.append('\n')
        elif tag == W + 'hyperlink':
            txt = ''.join(t.text or '' for t in node.iter(W + 't'))
            rid = node.get(R + 'id')
            tgt = links.get(rid)
            out.append(f'[{txt}]({tgt})' if tgt else txt)
        elif tag in (W + 'ins', W + 'smartTag', W + 'sdt', W + 'sdtContent', W + 'fldSimple'):
            out.append(para_text(node, links))
    return ''.join(out)


def style(p):
    ppr = p.find(W + 'pPr')
    if ppr is not None:
        s = ppr.find(W + 'pStyle')
        if s is not None:
            return s.get(W + 'val') or ''
    return ''


def walk(body, links, out, depth=0):
    for el in body:
        if el.tag == W + 'p':
            t = para_text(el, links)
            st = style(el)
            m = re.match(r'Heading(\d)', st)
            if m and t.strip():
                t = '#' * int(m.group(1)) + ' ' + t
            elif 'List' in st and t.strip():
                t = '- ' + t
            out.append(t)
        elif el.tag == W + 'tbl':
            out.append('[TABLE]')
            for tr in el.iter(W + 'tr'):
                cells = []
                for tc in tr.findall(W + 'tc'):
                    sub = []
                    walk(tc, links, sub, depth + 1)
                    cells.append(' / '.join(s for s in sub if s.strip()))
                out.append('| ' + ' | '.join(cells) + ' |')
            out.append('[/TABLE]')
        elif el.tag in (W + 'sdt', W + 'sdtContent'):
            walk(el, links, out, depth)


def convert(path):
    with zipfile.ZipFile(path) as z:
        links = rels(z)
        doc = ET.fromstring(z.read('word/document.xml'))
    out = []
    walk(doc.find(W + 'body'), links, out)
    text = '\n'.join(out)
    return re.sub(r'\n{3,}', '\n\n', text)


if __name__ == '__main__':
    for p in sys.argv[1:]:
        if len(sys.argv) > 2:
            print(f'\n\n===== {p} =====\n')
        print(convert(p))
