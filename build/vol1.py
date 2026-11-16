"""Assemble le volume 1 : un PDF élève + un PDF enseignant, numérotation continue.

Élève : modules 1→12, annexes (mémos), table des matières détaillée + index.
Prof  : guide général, sommaire, table des matières détaillée (pages élève + livret), livrets.
"""
import sys, os, importlib
sys.path.insert(0, '/home/claude/syllabus')
from pypdf import PdfWriter, PdfReader
from lib.base import *
from lib.render import to_pdf
from lib.progression import V1
from lib.toc import build_toc
from build.annexes import build_annexes

BUILDERS = []
for k in range(1, 13):
    try:
        mod = importlib.import_module(f"build.m{k}")
        BUILDERS.append(getattr(mod, f"build_m{k}"))
    except ModuleNotFoundError:
        break

TMP = '/home/claude/syllabus/build/tmp'
os.makedirs(TMP, exist_ok=True)
GUIDE = '/home/claude/syllabus/out/00_Guide_general_et_progression.pdf'
gpages = len(PdfReader(GUIDE).pages)
COL = "#E4572E"


def build_all(toc_pages):
    books = []
    start, tstart = 1, gpages + 2 + toc_pages  # guide + sommaire + table détaillée
    for fn in BUILDERS:
        b, T = fn(start=start, tstart=tstart, render=False)
        books.append((b, T))
        start, tstart = b.n + 1, T.n + 1
    return books


def modlist(books):
    return [(i + 1, V1[i][0], b, T) for i, (b, T) in enumerate(books)]


# itération : le nombre de pages de la table prof décale la numérotation des livrets
k = 6
for _ in range(4):
    books = build_all(k)
    annex = build_annexes(start=books[-1][0].n + 1)
    TP = build_toc(Book, "V1 · PROF", "Volume 1 · Premiers pas · Livret enseignant", COL, modlist(books), annex, prof=True, start=gpages + 2, teacher=True)
    kk = TP.n - (gpages + 1)
    if kk == k:
        break
    k = kk
TE = build_toc(Book, "V1 · Index", "Volume 1 · Premiers pas · Index", COL, modlist(books), annex, prof=False, start=annex.n + 1)


def sommaire(kind):
    rows = []
    for i, m in enumerate(V1):
        if i < len(books):
            b, T = books[i]
            pg = min(min(v) for v in b.marks.values()) if kind == "e" else min(min(v) for v in T.marks.values())
            last = b.n if kind == "e" else T.n
            rows.append([f'<b style="font-size:13pt">{i+1}</b>', f'<b>{m[0]}</b><div class="xs muted">{m[1]}</div>', f'<span class="sm">{m[8]}</span>', f'<b>p. {pg}–{last}</b>'])
        else:
            rows.append([f'<span class="muted">{i+1}</span>', f'<span class="muted">{m[0]}</span><div class="xs muted">{m[1]}</div>', f'<span class="xs muted">{m[8]}</span>', '<span class="xs muted">à venir</span>'])
    if kind == "e":
        rows.append(["📎", "<b>Annexes · Mes mémos</b><div class='xs muted'>conjugaison, grammaire, sons, nombres, consignes en images</div>", "", f"<b>p. {annex.n - len(annex.pages) + 1}–{annex.n}</b>"])
        rows.append(["🔎", "<b>Table des matières détaillée et index</b><div class='xs muted'>trouver une leçon, un document, un son, une activité</div>", "", f"<b>p. {TE.n - len(TE.pages) + 1}–{TE.n}</b>"])
    return table(["Module", "Thème", "Tâche finale", "Pages"], rows, ["16mm", "86mm", "52mm", "28mm"])


b1 = books[0][0]
b1.pages = [p.replace("%%SOMMAIRE%%", '<h1>Sommaire</h1><p class="muted mb4">Volume 1 · Premiers pas · parcours ★ Alpha → A1</p>' + sommaire("e")) for p in b1.pages]

el, pr = PdfWriter(), PdfWriter()
for i, (b, T) in enumerate(books):
    to_pdf(b.html(), f'{TMP}/e{i+1}.pdf'); to_pdf(T.html(), f'{TMP}/p{i+1}.pdf')
to_pdf(annex.html(), f'{TMP}/annex.pdf'); to_pdf(TE.html(), f'{TMP}/etoc.pdf'); to_pdf(TP.html(), f'{TMP}/ptoc.pdf')
S = Book("V1 · PROF", "Volume 1 · Premiers pas · Livret enseignant", COL, teacher=True, start=gpages + 1)
S.page(f'<h1>Volume 1 · Livrets enseignant</h1><p class="muted mb4">Le guide général (pages précédentes) présente la collection. Ensuite : la <b>table des matières détaillée</b> (p. {gpages + 2}–{TP.n}) pour préparer un cours ou retrouver une matière, puis les livrets de chaque module.</p>' + sommaire("p"), "Sommaire")
to_pdf(S.html(), f'{TMP}/psom.pdf')
for f in [GUIDE, f'{TMP}/psom.pdf', f'{TMP}/ptoc.pdf'] + [f'{TMP}/p{i+1}.pdf' for i in range(len(books))]:
    pr.append(f)
for f in [f'{TMP}/e{i+1}.pdf' for i in range(len(books))] + [f'{TMP}/annex.pdf', f'{TMP}/etoc.pdf']:
    el.append(f)
el.write('/home/claude/syllabus/out/VOLUME_1_Premiers_pas_ELEVE.pdf')
pr.write('/home/claude/syllabus/out/VOLUME_1_Premiers_pas_PROF.pdf')
print("modules:", len(books), "· élève:", TE.n, "p (annexes", len(annex.pages), "+ index", len(TE.pages), ") · prof:", books[-1][1].n, "p (table", len(TP.pages), ")")
