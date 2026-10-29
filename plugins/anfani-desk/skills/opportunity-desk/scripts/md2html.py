"""Convert an answer sheet (Markdown) to the HTML that Google Drive converts into a Google Doc.

Usage: python md2html.py <answers.md> <out.html> [--title "Doc title"]
Handles headings, paragraphs, bold, italics, inline code, links, bullet and numbered lists, tables,
blockquotes and horizontal rules. Everything else is left as text. [TBC: ...] markers are highlighted
so the user sees what only they can answer.
"""
import html, re, sys

def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    s = re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])', r'<i>\1</i>', s)
    s = re.sub(r'\[([^\]]+)\]\((https?://[^)\s]+)\)', r'<a href="\2">\1</a>', s)
    s = re.sub(r'(\[TBC[^\]]*\])', r'<span style="background-color:#fff2a8"><b>\1</b></span>', s)
    return s

def convert(md, title=None):
    out, i, lines = [], 0, md.splitlines()
    if title: out.append(f'<h1>{html.escape(title)}</h1>')
    para = []
    def flush():
        if para:
            out.append('<p>' + inline(' '.join(para)) + '</p>'); para.clear()
    while i < len(lines):
        ln = lines[i]
        if not ln.strip():
            flush(); i += 1; continue
        m = re.match(r'^(#{1,6})\s+(.*)$', ln)
        if m:
            flush(); lvl = min(len(m.group(1)) + (1 if title else 0), 6)
            out.append(f'<h{lvl}>{inline(m.group(2))}</h{lvl}>'); i += 1; continue
        if re.match(r'^\s*(-{3,}|\*{3,})\s*$', ln):
            flush(); out.append('<hr>'); i += 1; continue
        if ln.startswith('|'):
            flush(); rows = []
            while i < len(lines) and lines[i].startswith('|'):
                cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
                if not all(re.match(r'^:?-+:?$', c) for c in cells if c): rows.append(cells)
                i += 1
            out.append('<table border="1" cellpadding="4" style="border-collapse:collapse">')
            for r, cells in enumerate(rows):
                tag = 'th' if r == 0 else 'td'
                out.append('<tr>' + ''.join(f'<{tag}>{inline(c)}</{tag}>' for c in cells) + '</tr>')
            out.append('</table>'); continue
        if ln.startswith('>'):
            flush(); q = []
            while i < len(lines) and lines[i].startswith('>'):
                q.append(lines[i].lstrip('> ').rstrip()); i += 1
            out.append('<blockquote><p>' + inline(' '.join(q)) + '</p></blockquote>'); continue
        m = re.match(r'^(\s*)([-*]|\d+[.)])\s+(.*)$', ln)
        if m:
            flush(); ordered = m.group(2)[0].isdigit(); items = []
            while i < len(lines):
                m2 = re.match(r'^(\s*)([-*]|\d+[.)])\s+(.*)$', lines[i])
                if m2 and (m2.group(2)[0].isdigit() == ordered):
                    items.append(m2.group(3)); i += 1
                elif lines[i].startswith('  ') and items and lines[i].strip():
                    items[-1] += ' ' + lines[i].strip(); i += 1
                else: break
            tag = 'ol' if ordered else 'ul'
            out.append(f'<{tag}>' + ''.join(f'<li>{inline(x)}</li>' for x in items) + f'</{tag}>'); continue
        para.append(ln.strip()); i += 1
    flush()
    body = '\n'.join(out)
    return ('<html><head><meta charset="utf-8"></head><body style="font-family:Arial;font-size:11pt">'
            + body + '</body></html>')

if __name__ == '__main__':
    args = sys.argv[1:]; title = None
    if '--title' in args:
        k = args.index('--title'); title = args[k + 1]; del args[k:k + 2]
    src, dst = args
    open(dst, 'w', encoding='utf-8').write(convert(open(src, encoding='utf-8').read(), title))
    print(dst)
