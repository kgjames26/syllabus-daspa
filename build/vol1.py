"""Assemble le volume 1 : un PDF élève + un PDF enseignant, numérotation continue."""
import sys, os
sys.path.insert(0, '/home/claude/syllabus')
from pypdf import PdfWriter, PdfReader
from lib.base import *
from lib.render import to_pdf
from lib.progression import V1
from build.m1 import build_m1
from build.m2 import build_m2

BUILDERS = [build_m1, build_m2]
import importlib
for k in range(3, 13):
    try:
        mod = importlib.import_module(f"build.m{k}")
        BUILDERS.append(getattr(mod, f"build_m{k}"))
    except ModuleNotFoundError:
        break

TMP = '/home/claude/syllabus/build/tmp'
os.makedirs(TMP, exist_ok=True)
GUIDE = '/home/claude/syllabus/out/00_Guide_general_et_progression.pdf'
gpages = len(PdfReader(GUIDE).pages)

books = []
start, tstart = 1, gpages + 2  # +1 page sommaire prof
for fn in BUILDERS:
    b, T = fn(start=start, tstart=tstart, render=False)
    books.append((b, T))
    start, tstart = b.n + 1, T.n + 1

def sommaire(kind):
    rows = []
    for i, m in enumerate(V1):
        if i < len(books):
            b, T = books[i]
            pg = (b.pages and b.marks) and min(min(v) for v in b.marks.values()) if kind == "e" else min(min(v) for v in T.marks.values())
            last = b.n if kind == "e" else T.n
            rows.append([f'<b style="font-size:13pt">{i+1}</b>', f'<b>{m[0]}</b><div class="xs muted">{m[1]}</div>', f'<span class="sm">{m[8]}</span>', f'<b>p. {pg}–{last}</b>'])
        else:
            rows.append([f'<span class="muted">{i+1}</span>', f'<span class="muted">{m[0]}</span><div class="xs muted">{m[1]}</div>', f'<span class="xs muted">{m[8]}</span>', '<span class="xs muted">à venir</span>'])
    return table(["Module", "Thème", "Tâche finale", "Pages"], rows, ["16mm", "86mm", "52mm", "28mm"])

b1 = books[0][0]
b1.pages = [p.replace("%%SOMMAIRE%%", '<h1>Sommaire</h1><p class="muted mb4">Volume 1 · Premiers pas · parcours ★ Alpha → A1</p>' + sommaire("e")) for p in b1.pages]

el, pr = PdfWriter(), PdfWriter()
for i, (b, T) in enumerate(books):
    fe, fp = f'{TMP}/e{i+1}.pdf', f'{TMP}/p{i+1}.pdf'
    to_pdf(b.html(), fe); to_pdf(T.html(), fp)
# prof : guide + sommaire + livrets
S = Book("V1 · PROF", "Volume 1 · Premiers pas · Livret enseignant", "#E4572E", teacher=True, start=gpages + 1)
S.page('<h1>Volume 1 · Livrets enseignant</h1><p class="muted mb4">Le guide général (pages précédentes) présente la collection. Voici les livrets de chaque module : déroulement, scripts, corrigés, clés QCM et grilles.</p>' + sommaire("p"), "Sommaire")
to_pdf(S.html(), f'{TMP}/psom.pdf')
for f in [GUIDE, f'{TMP}/psom.pdf'] + [f'{TMP}/p{i+1}.pdf' for i in range(len(books))]:
    pr.append(f)
for i in range(len(books)):
    el.append(f'{TMP}/e{i+1}.pdf')
el.write('/home/claude/syllabus/out/VOLUME_1_Premiers_pas_ELEVE.pdf')
pr.write('/home/claude/syllabus/out/VOLUME_1_Premiers_pas_PROF.pdf')
print("modules:", len(books), "élève:", books[-1][0].n, "p · prof:", books[-1][1].n, "p")
