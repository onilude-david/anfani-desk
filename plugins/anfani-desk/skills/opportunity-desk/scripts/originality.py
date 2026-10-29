"""Originality check for answer sheets.

Usage: python originality.py <sheet.md> [<sheet.md> ...] [--against <dir-or-file> ...] [--min-words 10] [--all]
       [--sheets <glob>] [--bio <file>]

Defaults: --sheets 'desk/applications/**/*.md' (the user's other sheets), --bio desk/profile.md (their approved bio may repeat).

By default only the ANSWER text is compared: blockquotes (> ...) and the paragraph under an "**Answer" line, which
is what a reviewer will read. --all compares the whole sheet (tables, notes, template lines too).

Reports, for every sheet given:
  1. Runs of words it shares verbatim with any OTHER sheet in desk/applications/ (templated answers look alike to
     reviewers, and some funders share readers).
  2. Runs it shares with any file passed with --against: saved funder pages, sample essays, press articles, other
     people's applications. Anything found there must be rewritten or quoted with attribution.
Text copied on purpose from the user's approved bio (--bio) is listed separately, not counted as a problem.
MIT licence, part of Anfani Desk (anfani.app).
Exit code 1 if any cross-sheet or external overlap is found, so a run can gate on it.
"""
import glob, os, re, sys

MIN = 10
ALL = False

def norm(s):
    return re.sub(r'[^a-z0-9 ]+', ' ', s.lower()).split()

def sentences(text):
    text = re.sub(r'`[^`]*`', ' ', text)
    text = re.sub(r'\[TBC[^\]]*\]', ' ', text)
    for s in re.split(r'(?<=[.!?])\s+|\n', text):
        w = norm(s)
        if len(w) >= 8:
            yield s.strip(), ' '.join(w)

def shingles(words, n):
    return {' '.join(words[i:i + n]) for i in range(len(words) - n + 1)}

def load(path):
    try:
        return open(path, encoding='utf-8', errors='replace').read()
    except OSError:
        return ''

def answers_only(text):
    out, take, quoted = [], False, False
    for ln in text.splitlines():
        if ln.startswith('## '):
            # the programme's own criteria are quoted on purpose; never test them
            quoted = ln.lower().startswith('## scoring criteria'); take = False; continue
        if quoted:
            continue
        if ln.startswith('>'):
            out.append(ln.lstrip('> ')); take = False; continue
        if re.match(r'^\*\*Answer', ln):
            take = True; continue
        if take:
            if not ln.strip() or ln[0] in '#|*':
                take = False
            else:
                out.append(ln)
    return '\n'.join(out)

def body(path):
    t = load(path)
    return t if ALL else answers_only(t)

def main(argv):
    global MIN, ALL
    SHEETS = 'desk/applications/**/*.md'
    BIO = 'desk/profile.md'
    sheets, against = [], []
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == '--against':
            against.append(argv[i + 1]); i += 2
        elif a == '--min-words':
            MIN = int(argv[i + 1]); i += 2
        elif a == '--all':
            ALL = True; i += 1
        elif a == '--sheets':
            SHEETS = argv[i + 1]; i += 2
        elif a == '--bio':
            BIO = argv[i + 1]; i += 2
        else:
            sheets.append(a); i += 1
    if not os.path.isdir('desk') and '--sheets' not in argv:
        sys.exit('error: no desk/ folder here. Run from the project that holds desk/, or pass --sheets and --bio.')
    bio_sh = shingles(norm(load(BIO)), MIN)
    others = {p: body(p) for p in glob.glob(SHEETS, recursive=True)
              if os.path.basename(p).endswith('.md')}
    ext = {}
    for a in against:
        paths = [a] if os.path.isfile(a) else glob.glob(os.path.join(a, '**', '*'), recursive=True)
        for p in paths:
            if os.path.isfile(p):
                ext[p] = load(p)
    problems = 0
    for sheet in sheets:
        text = body(sheet); mine = shingles(norm(text), MIN)
        print(f'\n== {sheet}')
        found = 0
        bio_hits = mine & bio_sh
        if bio_hits:
            print(f'  bio text reused on purpose: {len(bio_hits)} runs of {MIN} words (fine)')
        for p, t in others.items():
            if os.path.abspath(p) == os.path.abspath(sheet):
                continue
            shared = (mine & shingles(norm(t), MIN)) - bio_sh
            if shared:
                sents = [s for s, n in sentences(text) if any(sh in n for sh in shared)]
                print(f'  shares {len(shared)} runs of {MIN} words with {p}:')
                for s in sents[:8]:
                    print(f'    - {s[:150]}')
                found += 1
        for p, t in ext.items():
            shared = (mine & shingles(norm(t), MIN)) - bio_sh
            if shared:
                sents = [s for s, n in sentences(text) if any(sh in n for sh in shared)]
                print(f'  EXTERNAL overlap, {len(shared)} runs of {MIN} words, with {p}:')
                for s in sents[:8]:
                    print(f'    - {s[:150]}')
                found += 1
        if not found:
            print('  clean')
        problems += found
    print(f'\n{problems} overlap(s) to resolve' if problems else '\nclean')
    return 1 if problems else 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
