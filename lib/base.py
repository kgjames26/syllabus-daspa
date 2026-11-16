"""Gabarit commun aux 3 volumes : CSS, pages, composants d'exercices."""
from .art import picto, avatar, PICTO_LABEL

CSS = r"""
@page { size: A4; margin: 0; }
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; }
body { font-family: 'Poppins', 'Inter', sans-serif; color: #1F2A44; font-size: 11.5pt; line-height: 1.38; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
.page { width: 210mm; height: 297mm; position: relative; overflow: hidden; page-break-after: always; padding: 17mm 14mm 16mm 14mm; background: #fff; }
.page.full { padding: 0; }
.hdr { position: absolute; top: 0; left: 0; right: 0; height: 12mm; display: flex; align-items: stretch; }
.hdr .tab { background: var(--mc); color: #fff; font-weight: 700; padding: 0 6mm; display: flex; align-items: center; font-size: 10pt; border-bottom-right-radius: 5mm; letter-spacing: .3px; }
.hdr .sec { display: flex; align-items: center; padding: 0 5mm; font-size: 10pt; font-weight: 600; color: var(--mc); }
.hdr .lvl { margin-left: auto; display: flex; align-items: center; padding-right: 8mm; gap: 2mm; font-size: 9pt; color: #666; }
.ftr { position: absolute; bottom: 0; left: 0; right: 0; height: 11mm; display: flex; align-items: center; justify-content: space-between; padding: 0 14mm; font-size: 8.5pt; color: #8a8f9c; border-top: 1px solid #eceef2; }
.ftr .pn { background: var(--mc); color: #fff; border-radius: 50%; width: 8mm; height: 8mm; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 9pt; }
h1 { font-size: 26pt; margin: 0 0 3mm 0; line-height: 1.1; }
h2 { font-size: 16pt; margin: 0 0 3mm 0; color: var(--mc); }
h3 { font-size: 12.5pt; margin: 3mm 0 2mm 0; }
p { margin: 0 0 2mm 0; }
.ex { margin: 0 0 5mm 0; break-inside: avoid; }
.ex-h { display: flex; align-items: center; gap: 2.5mm; margin-bottom: 2.5mm; }
.ex-n { background: var(--mc); color: #fff; font-weight: 800; min-width: 9mm; height: 9mm; border-radius: 2.5mm; display: flex; align-items: center; justify-content: center; font-size: 12pt; }
.ex-t { font-weight: 600; font-size: 12pt; flex: 1; line-height: 1.25; }
.ex-p { display: flex; gap: 1mm; }
.dots { display: inline-flex; gap: 1.2mm; }
.dots i { width: 3.2mm; height: 3.2mm; border-radius: 50%; border: 1.5px solid var(--mc); display: inline-block; }
.dots i.on { background: var(--mc); }
.atl { font-size: 8pt; font-weight: 700; padding: .6mm 2.2mm; border-radius: 3mm; color: #fff; white-space: nowrap; }
.atl.A { background: #E4572E; } .atl.B { background: #4A7BD1; } .atl.C { background: #2BA88F; } .atl.D { background: #9B5DE5; } .atl.P { background: #1F2A44; }
.alpha-tag { background: #FFD166; color: #1F2A44; font-size: 8pt; font-weight: 800; padding: .6mm 2.2mm; border-radius: 3mm; white-space: nowrap; }
.lecon { border: 2.5px solid #F2B705; background: #FFF8DB; border-radius: 4mm; padding: 4mm 5mm 4mm 5mm; margin: 2mm 0 5mm 0; position: relative; break-inside: avoid; }
.lecon .lt { position: absolute; top: -4mm; left: 5mm; background: #F2B705; color: #1F2A44; font-weight: 800; font-size: 9.5pt; padding: .8mm 3mm; border-radius: 2mm; letter-spacing: .5px; }
.astuce { border-left: 5px solid #2BA88F; background: #E8F6F2; padding: 3mm 4mm; border-radius: 0 3mm 3mm 0; margin: 2mm 0 4mm; font-size: 10.5pt; break-inside: avoid; }
.attention { border-left: 5px solid #E4572E; background: #FDECE7; padding: 3mm 4mm; border-radius: 0 3mm 3mm 0; margin: 2mm 0 4mm; font-size: 10.5pt; break-inside: avoid; }
.prof-note { border: 1.5px dashed #9aa1b1; color: #555; font-size: 9pt; padding: 2mm 3mm; border-radius: 2mm; margin: 2mm 0; }
.blank { display: inline-block; border-bottom: 1.6px solid #1F2A44; min-width: 28mm; height: 1.1em; vertical-align: bottom; }
.blank.s { min-width: 14mm; } .blank.l { min-width: 50mm; } .blank.xl { min-width: 80mm; }
.line { border-bottom: 1.3px solid #b9bfcc; height: 9mm; }
.line.tall { height: 11mm; }
.grid2 { display: grid; grid-template-columns: 1fr 1fr; gap: 4mm; }
.grid3 { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 4mm; }
.grid4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: 3mm; }
.grid5 { display: grid; grid-template-columns: repeat(5, 1fr); gap: 3mm; }
.grid6 { display: grid; grid-template-columns: repeat(6, 1fr); gap: 2.5mm; }
.card { border: 1.8px solid #dfe3ea; border-radius: 3mm; padding: 3mm; background: #fff; }
.card.c { text-align: center; }
.emo { font-size: 30pt; line-height: 1.1; display: block; }
.emo.xl { font-size: 44pt; } .emo.s { font-size: 22pt; }
.word { font-weight: 600; font-size: 11pt; }
table.t { border-collapse: collapse; width: 100%; font-size: 10.5pt; }
table.t th { background: var(--mc); color: #fff; padding: 2mm; text-align: left; font-weight: 600; }
table.t td { border: 1px solid #d7dbe3; padding: 2mm; vertical-align: top; }
table.t.compact td { padding: 1.3mm 1.6mm; line-height:1.25; }
table.t tr:nth-child(even) td { background: #f7f8fb; }
.chk { display: inline-block; width: 4.5mm; height: 4.5mm; border: 1.6px solid #1F2A44; border-radius: 1mm; vertical-align: middle; margin-right: 1.5mm; }
.circ { display: inline-flex; width: 7mm; height: 7mm; border: 1.6px solid #1F2A44; border-radius: 50%; align-items: center; justify-content: center; font-weight: 700; font-size: 10pt; margin-right: 1.5mm; }
.relie { display: grid; grid-template-columns: 1fr 14mm 14mm 1fr; align-items: center; row-gap: 3mm; }
.relie .l { text-align: right; } .relie .d { width: 3mm; height: 3mm; border-radius: 50%; background: #1F2A44; justify-self: center; }
.av { display: block; }
.avb { display: flex; align-items: flex-start; gap: 2mm; margin-bottom: 2mm; }
.bubble { background: #fff; border: 2px solid #1F2A44; border-radius: 4mm; padding: 2mm 3.5mm; position: relative; font-size: 11pt; margin-top: 3mm; }
.bubble:before { content: ''; position: absolute; left: -3mm; top: 4mm; border: 1.5mm solid transparent; border-right: 2mm solid #1F2A44; }
.big { font-size: 15pt; } .huge { font-size: 22pt; font-weight: 700; }
.c { text-align: center; } .r { text-align: right; }
.muted { color: #7a8193; } .sm { font-size: 9.5pt; } .xs { font-size: 8.5pt; }
.pill { display: inline-block; padding: .8mm 3mm; border-radius: 4mm; background: #eef1f6; font-weight: 600; margin: .8mm; font-size: 10.5pt; }
.flex { display: flex; gap: 4mm; align-items: center; } .flex.top { align-items: flex-start; }
.grow { flex: 1; }
.mb2 { margin-bottom: 2mm; } .mb4 { margin-bottom: 4mm; } .mt4 { margin-top: 4mm; } .mt2 { margin-top: 2mm; }
.doc { box-shadow: 0 1.5mm 4mm rgba(0,0,0,.18); border-radius: 2mm; background: #fff; transform: rotate(-.6deg); }
.tag-doc { display: inline-block; background: #1F2A44; color: #fff; font-size: 8.5pt; font-weight: 700; padding: 1mm 3mm; border-radius: 2mm; margin-bottom: 2mm; letter-spacing: .5px; }
.sol { color: #C0392B; font-weight: 700; font-family: 'Inter'; }
.teacher body, .teacher { font-family: 'Inter', sans-serif; font-size: 10.5pt; }
.qcm-grid { display: grid; grid-template-columns: repeat(2, 1fr); column-gap: 10mm; row-gap: 2.2mm; }
.bub { display: inline-flex; width: 6.5mm; height: 6.5mm; border: 1.5px solid #1F2A44; border-radius: 50%; align-items: center; justify-content: center; font-size: 8.5pt; margin-right: 1.5mm; font-weight: 600; }
.score { border: 2px solid var(--mc); border-radius: 3mm; padding: 2mm 4mm; font-weight: 700; display: inline-block; }
.cut { border-top: 2px dashed #9aa1b1; margin: 4mm 0; position: relative; }
.cut:after { content: '✂'; position: absolute; left: 0; top: -3.6mm; font-size: 12pt; color: #9aa1b1; background: #fff; padding-right: 1mm; }
.stamp { display: inline-block; border: 2.5px solid #E4572E; color: #E4572E; font-weight: 800; padding: 1mm 3mm; border-radius: 2mm; transform: rotate(-6deg); }
"""


class Book:
    """Accumule les pages, numérote, produit le HTML final."""

    def __init__(self, code, title, color, teacher=False, start=1):
        self.code = code
        self.title = title
        self.color = color
        self.pages = []
        self.teacher = teacher
        self.n = start - 1
        self.exn = 0

    def page(self, body, section="", full=False, levels=True, color=None):
        self.n += 1
        if not hasattr(self, "marks"):
            self.marks = {}
        self.marks.setdefault(section or "_", []).append(self.n)
        if not hasattr(self, "raw"):
            self.raw = []
        self.raw.append((self.n, section, body))
        col = color or self.color
        if full:
            html = f'<section class="page full" style="--mc:{col}">{body}</section>'
        else:
            lv = ('<div class="lvl"><span class="dots"><i class="on"></i></span>découverte '
                  '<span class="dots"><i class="on"></i><i class="on"></i></span>entraînement '
                  '<span class="dots"><i class="on"></i><i class="on"></i><i class="on"></i></span>défi</div>') if levels and not self.teacher else ''
            html = (f'<section class="page{" teacher" if self.teacher else ""}" style="--mc:{col}">'
                    f'<div class="hdr"><div class="tab">{self.code}</div><div class="sec">{section}</div>{lv}</div>'
                    f'{body}'
                    f'<div class="ftr"><span>{self.title}</span><span>{"Livret enseignant" if self.teacher else "Nom : ................................................"}</span><span class="pn">{self.n}</span></div>'
                    f'</section>')
        self.pages.append(html)
        return self.n

    def html(self):
        return ('<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><style>' + CSS +
                '</style></head><body>' + "".join(self.pages) + '</body></html>')


def dots(n):
    return '<span class="dots">' + "".join('<i class="on"></i>' if i < n else '<i></i>' for i in range(3)) + '</span>'


ATELIERS = {"A": "🎧 Écouter-Parler", "B": "📖 Lire", "C": "✏️ Écrire", "D": "🧩 Jouer", "P": "👩‍🏫 Avec la prof"}


class Ex:
    """Numérotation des exercices par module + collecte automatique des corrigés et scripts."""

    def __init__(self, book=None):
        self.n = 0
        self.book = book
        self.sols = []      # (page, n, titre, corrigé)
        self.scripts = []   # (page, n, titre, script)
        self.all = []       # (n, page, level, atelier, alpha, titre)

    def __call__(self, title, body, pictos=(), level=1, atelier=None, alpha=False, num=True, sol=None, script=None):
        self.n += 1
        pg = self.book.n + 1 if self.book else 0
        if sol:
            self.sols.append((pg, self.n, title, sol))
        if script:
            self.scripts.append((pg, self.n, title, script))
        self.all.append((self.n, pg, level, atelier, alpha, title))
        p = "".join(picto(x, 30) for x in pictos)
        tags = ""
        if alpha:
            tags += f'<span class="alpha-tag">{getattr(type(self), "TAG", "★ ALPHA")}</span>'
        if atelier:
            tags += f'<span class="atl {atelier}">{ATELIERS[atelier]}</span>'
        n = f'<div class="ex-n">{self.n}</div>' if num else ''
        return (f'<div class="ex"><div class="ex-h">{n}<div class="ex-p">{p}</div>'
                f'<div class="ex-t">{title}</div>{tags}{dots(level)}</div>{body}</div>')


def lecon(title, body, label="À ÉTUDIER"):
    return f'<div class="lecon"><div class="lt">📌 {label}</div><h3 style="margin-top:1mm">{title}</h3>{body}</div>'


def lines(n, tall=False):
    return "".join(f'<div class="line{" tall" if tall else ""}"></div>' for _ in range(n))


def guide_lines(n=1, h=22, label=""):
    """Lignes d'écriture à 4 interlignes (alpha) en SVG, hauteur h mm."""
    out = []
    for _ in range(n):
        out.append(f'<svg viewBox="0 0 182 {h}" width="100%" style="display:block;margin-bottom:1mm">'
                   f'<rect x="0" y="{h*0.25}" width="182" height="{h*0.25}" fill="#EAF4FF"/>'
                   f'<line x1="0" y1="{h*0.08}" x2="182" y2="{h*0.08}" stroke="#d2d7e0" stroke-width=".3"/>'
                   f'<line x1="0" y1="{h*0.25}" x2="182" y2="{h*0.25}" stroke="#9fb6d6" stroke-width=".35"/>'
                   f'<line x1="0" y1="{h*0.5}" x2="182" y2="{h*0.5}" stroke="#E4572E" stroke-width=".45"/>'
                   f'<line x1="0" y1="{h*0.75}" x2="182" y2="{h*0.75}" stroke="#d2d7e0" stroke-width=".3"/>'
                   f'</svg>')
    return "".join(out)


def trace(text, h=22, reps=1, model=True, fill_ratio=0.0):
    """Ligne de traçage : modèle plein + lettres en pointillés sur lignes guides."""
    fs = h * 0.42
    base = h * 0.5
    items = []
    x = 2
    if model:
        items.append(f'<text x="{x}" y="{base}" font-family="Poppins" font-size="{fs}" fill="#1F2A44" font-weight="500">{text}</text>')
    step = len(text) * fs * 0.72 + 8
    x = 2 + (step if model else 0)
    k = 0
    while x + step * 0.8 < 182 and k < reps:
        items.append(f'<text x="{x}" y="{base}" font-family="Poppins" font-size="{fs}" fill="none" stroke="#7d8597" stroke-width=".35" stroke-dasharray="1 .8">{text}</text>')
        x += step
        k += 1
    return (f'<svg viewBox="0 {base - fs*0.95} 182 {fs*1.45}" width="100%" style="display:block;margin-bottom:1.5mm">'
            f'<rect x="0" y="{base - fs*0.52}" width="182" height="{fs*0.52}" fill="#EAF4FF"/>'
            f'<line x1="0" y1="{base - fs*0.76}" x2="182" y2="{base - fs*0.76}" stroke="#d2d7e0" stroke-width=".3"/>'
            f'<line x1="0" y1="{base - fs*0.52}" x2="182" y2="{base - fs*0.52}" stroke="#9fb6d6" stroke-width=".3"/>'
            f'<line x1="0" y1="{base}" x2="182" y2="{base}" stroke="#E4572E" stroke-width=".45"/>'
            f'<line x1="0" y1="{base + fs*0.35}" x2="182" y2="{base + fs*0.35}" stroke="#d2d7e0" stroke-width=".3"/>'
            + "".join(items) + '</svg>')


def blank(size=""):
    return f'<span class="blank {size}"></span>'


def relie(left, right):
    rows = []
    for a, b in zip(left, right):
        rows.append(f'<div class="l">{a}</div><div class="d"></div><div class="d"></div><div>{b}</div>')
    return '<div class="relie">' + "".join(rows) + '</div>'


def table(head, rows, widths=None):
    cg = ""
    if widths:
        cg = "<colgroup>" + "".join(f'<col style="width:{w}">' for w in widths) + "</colgroup>"
    h = "<tr>" + "".join(f"<th>{x}</th>" for x in head) + "</tr>" if head else ""
    r = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f'<table class="t">{cg}{h}{r}</table>'


def qcm_line(n, q, opts, cols=None):
    o = "".join(f'<span style="margin-right:5mm"><span class="bub">{"ABCDE"[i]}</span>{x}</span>' for i, x in enumerate(opts))
    return f'<div class="mb2"><b>{n}.</b> {q}<div style="margin:1.2mm 0 0 5mm">{o}</div></div>'


def picto_legend(keys):
    return '<div class="flex" style="flex-wrap:wrap;gap:3mm">' + "".join(
        f'<div class="flex" style="gap:1.5mm">{picto(k, 30)}<span class="sm">{PICTO_LABEL[k]}</span></div>' for k in keys) + '</div>'
