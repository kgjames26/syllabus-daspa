"""Outils communs à tous les modules : plan de travail, livret enseignant, pagination."""
import re
import math
from .base import *


def plan_de_travail(b, E, mnum, lessons, tache):
    cells = ""
    for n, pg, lv, at, al, t in E.all:
        col = {"A": "#E4572E", "B": "#4A7BD1", "C": "#2BA88F", "D": "#9B5DE5", "P": "#1F2A44"}.get(at, "#9aa1b1")
        star = '<span style="color:#d9a400">★</span>' if al else ''
        cells += (f'<div style="border:1.5px solid #dfe3ea;border-left:4px solid {col};border-radius:1.5mm;padding:.8mm 1.5mm;display:flex;align-items:center;justify-content:space-between;font-size:8.5pt">'
                  f'<span><b>{n}</b>{star} <span class="muted">p.{pg}</span></span>{dots(lv)}<span class="chk" style="width:3.6mm;height:3.6mm;margin:0"></span></div>')
    les = "<br>".join(f"☐ Leçon {i} · {t}" for i, t in enumerate(lessons, 1))
    plan = f'''<h2>Mon plan de travail · Module {mnum}</h2>
<p class="sm">Quand j'ai fini un exercice et qu'il est corrigé, je coche la case ☑. Les ★ = parcours Alpha. La couleur = l'atelier :
<span class="atl A">🎧</span> <span class="atl B">📖</span> <span class="atl C">✏️</span> <span class="atl D">🧩</span> <span class="atl P">👩‍🏫</span> · gris = activité de classe.</p>
<div style="display:grid;grid-template-columns:repeat(7,1fr);gap:1.3mm">{cells}</div>
<div class="grid3 mt4">
<div class="card"><b>📌 Mes leçons à étudier</b><p class="sm">{les}</p></div>
<div class="card"><b>🎯 Ma tâche finale</b><p class="sm">{tache}</p><b>📝 Mon test</b><p class="sm">Date : ............ Note : ...... / 40</p></div>
<div class="card"><b>✍️ Signature</b><p class="sm">Élève :<br><br>Prof :<br><br>Parent :</p></div></div>'''
    b.pages = [p.replace("%%PLAN_DE_TRAVAIL%%", plan) for p in b.pages]


def _cost(row, widths):
    c = 0
    for txt, w in zip(row, widths):
        t = re.sub(r"<[^>]+>", "", str(txt))
        c = max(c, math.ceil(len(t) / max(1, w * 0.52)))
    return c * 4.4 + 4.5


def paginate(rows, widths, budget_first, budget):
    pages, cur, used, bud = [], [], 0, budget_first
    for r in rows:
        k = _cost(r, widths)
        if cur and used + k > bud:
            pages.append(cur)
            cur, used, bud = [], 0, budget
        cur.append(r)
        used += k
    if cur:
        pages.append(cur)
    return pages


def helpers(b, E):
    M = b.marks

    def pg(sec):
        p = M.get(sec, [])
        return f"p. {p[0]}–{p[-1]}" if len(p) > 1 else (f"p. {p[0]}" if p else "")

    def exs(sec):
        ps = set(M.get(sec, []))
        ns = [n for n, p, *_ in E.all if p in ps]
        return f"ex. {ns[0]}–{ns[-1]}" if len(ns) > 1 else (f"ex. {ns[0]}" if ns else "")
    return pg, exs


def teacher_book(b, E, code, title, color, mnum, mtitle, objectifs, priorites, materiel, accueil, days, rituels, rotation, key, eval_html, extra_pages=(), start=1):
    T = Book(code, f"Volume 1 · Module {mnum} · {mtitle} · Livret enseignant", color, teacher=True, start=start)
    T.page(f'''<div style="background:{color};color:#fff;margin:-17mm -14mm 6mm -14mm;padding:20mm 14mm 10mm 14mm">
<div style="font-size:12pt;font-weight:700;opacity:.9">LIVRET ENSEIGNANT · VOLUME 1 · MODULE {mnum}</div><div style="font-size:40pt;font-weight:800;line-height:1.05">{mtitle}</div>
<div style="font-size:13pt;margin-top:3mm">Déroulement · scripts · corrigés · clé QCM · grilles d'évaluation</div></div>
<div class="grid2">
<div class="card"><h3 style="margin-top:0">Objectifs du module</h3><ul class="sm" style="padding-left:5mm;margin:0">{objectifs}</ul></div>
<div class="card"><h3 style="margin-top:0">Les priorités</h3>{priorites}
<h3>Matériel</h3><p class="sm">{materiel}</p>
<h3>Durée</h3><p class="sm">± 10 jours de cours (± 20 périodes). Élève {b.n - min(min(v) for v in b.marks.values()) + 1} pages · {E.n} exercices.</p></div></div>
<div class="attention mt4">{accueil}</div>''', "Vue d'ensemble")
    T.page(f'''<h2>Déroulement conseillé</h2>
{table(["Jour", "Organisation", "Contenu (cahier élève)", "Groupe ★ Alpha"], [[f"<b>{d}</b>", o, c, a] for d, o, c, a in days], ["12mm", "30mm", "95mm", "45mm"])}
<h3 class="mt4">Rituels quotidiens (10 premières minutes)</h3><p class="sm">{rituels}</p>
<h3>Rotation des ateliers</h3>
{table(["Pôle", "Fiches", "Durée", "Autocorrection"], rotation, ["38mm", "70mm", "20mm", "54mm"])}''', "Déroulement")
    srows = [[f"p. {p}", f"<b>{n}</b>", t, s] for p, n, t, s in E.scripts]
    W = [14, 10, 48, 110]
    for i, chunk in enumerate(paginate(srows, W, 190, 215)):
        T.page(("<h2>Scripts à lire à voix haute</h2><p class='sm muted'>Lire lentement, deux fois, à voix naturelle. Un élève avancé peut aussi lire les scripts.</p>" if i == 0 else "") +
               table(["Page", "Ex.", "Activité", "Script et conduite"], chunk, [f"{w}mm" for w in W]), "Scripts")
    crow = [[f"p. {p}", f"<b>{n}</b>", f'<span class="sm">{t}</span>', f'<span class="sol">{s}</span>'] for p, n, t, s in E.sols]
    W = [14, 10, 56, 102]
    for i, chunk in enumerate(paginate(crow, W, 200, 212)):
        T.page(("<h2>Corrigés</h2>" if i == 0 else "") + table(["Page", "Ex.", "Consigne", "Corrigé"], chunk, [f"{w}mm" for w in W]), "Corrigés")
    for html, sec in extra_pages:
        T.page(html, sec)
    kk = key.split(", ")
    krows = "".join(f'<div class="card c" style="padding:2mm"><b>{k.split("-")[0]}</b> → <span class="sol" style="font-size:14pt">{k.split("-")[1]}</span></div>' for k in kk)
    T.page(f'''<h2>Test du module · clé et barème</h2><h3>Partie A · QCM (20 points, 1 point par question)</h3>
<div style="display:grid;grid-template-columns:repeat(10,1fr);gap:2mm">{krows}</div>
<div class="card mt2" style="font-family:monospace;font-size:11pt"><b>Clé à encoder dans l'application :</b> {key}</div>{eval_html[0]}''', "Évaluation")
    T.page(eval_html[1], "Évaluation")
    return T


# ---------- gabarits de pages réutilisables ----------
from .art import avatar, picto


def opening(b, mc, num, title, visual, obj, talk, keys, tint):
    objs = "".join(f'<div class="flex mb2"><span class="emo s">{e}</span><span class="big">{t}</span></div>' for e, t in obj)
    b.page(f'''<div style="background:{mc};color:#fff;margin:-17mm -14mm 6mm -14mm;padding:16mm 14mm 6mm 14mm"><div style="font-size:13pt;font-weight:700;opacity:.9">MODULE {num}</div><div style="font-size:44pt;font-weight:800;line-height:1">{title}</div></div>
<div style="background:{tint};border-radius:4mm;padding:4mm">{visual}</div>
<div class="grid2 mt4"><div><h2>Je vais apprendre à…</h2>{objs}</div><div><div class="card" style="background:{tint}"><h3 style="margin-top:0">🗣️ On parle ensemble</h3>{"".join(f"<p>{t}</p>" for t in talk)}</div>
<div class="card mt4"><h3 style="margin-top:0">🔑 Les mots-clés</h3>{"".join(f'<span class="pill">{w}</span>' for w in keys)}</div></div></div>''', "Ouverture", levels=False)
    b.page("%%PLAN_DE_TRAVAIL%%", "Mon plan de travail", levels=False)


def bd_case(n, inner):
    return f'<div style="border:2.5px solid #1F2A44;border-radius:3mm;min-height:62mm;position:relative;padding:3mm;background:#FFFDF8"><div style="position:absolute;top:2mm;left:2mm;background:#1F2A44;color:#fff;width:6mm;height:6mm;border-radius:50%;font-size:9pt;font-weight:700;display:flex;align-items:center;justify-content:center">{n}</div>{inner}</div>'


def bub(t):
    return f'<div class="bubble" style="margin:0 0 2mm 0;font-size:11pt">{t}</div>'


def lr(a, ta, bb=None, tb=(), ma="sourire", mb="sourire", extra=""):
    h = f'<div class="flex top" style="margin-top:5mm">{avatar(a, 72, ma)}<div>{"".join(bub(x) for x in ta)}</div></div>'
    if bb:
        h += f'<div class="flex top" style="justify-content:flex-end">{"".join(bub(x) for x in tb)}{avatar(bb, 72, mb, flip=True)}</div>'
    return h + extra


def tache_head(title, desc):
    return f'<div style="background:#1F2A44;color:#fff;margin:-17mm -14mm 5mm -14mm;padding:15mm 14mm 5mm 14mm"><div style="font-size:11pt;font-weight:700;opacity:.8">🎯 TÂCHE FINALE</div><div style="font-size:26pt;font-weight:800">{title}</div><div class="sm" style="opacity:.9">{desc}</div></div>'


def test_pages(b, num, title, Q, partB, oral, alpha_html):
    head = f'''<div style="background:#1F2A44;color:#fff;margin:-17mm -14mm 4mm -14mm;padding:14mm 14mm 4mm 14mm;display:flex;justify-content:space-between;align-items:flex-end"><div><div style="font-size:11pt;font-weight:700;opacity:.8">📝 TEST · MODULE {num}</div><div style="font-size:24pt;font-weight:800">{title}</div></div><div class="sm" style="text-align:right">Prénom : ......................................<br>Date : ........ / ........ / ............</div></div>'''
    p1 = "".join(qcm_line(i + 1, q, o) for i, (q, o) in enumerate(Q[:10]))
    p2 = "".join(qcm_line(i + 11, q, o) for i, (q, o) in enumerate(Q[10:]))
    b.page(f'{head}<div class="flex" style="justify-content:space-between"><h2 style="margin:0">Partie A · Je choisis la bonne réponse</h2><span class="score">…… / 20</span></div><p class="sm muted">J\'entoure la lettre, puis je noircis le rond sur la feuille de réponses.</p>{p1}', "Test", levels=False)
    b.page(p2, "Test", levels=False)
    b.page(f'''<div class="flex" style="justify-content:space-between"><h2 style="margin:0">Partie B · J'écris</h2><span class="score">…… / 10</span></div>{partB}
<div class="flex mt4" style="justify-content:space-between"><h2 style="margin:0">Partie C · Je parle avec la prof</h2><span class="score">…… / 10</span></div>
{table(["Je sais…", "Points", "✅"], oral, ["120mm", "30mm", "32mm"])}<div class="card mt2 c"><span class="huge">TOTAL : …… / 40</span></div>''', "Test", levels=False)
    b.page(f'<div style="background:#FFD166;margin:-17mm -14mm 4mm -14mm;padding:14mm 14mm 4mm 14mm"><div style="font-size:11pt;font-weight:800">★ ALPHA · 📝 TEST · MODULE {num}</div><div style="font-size:22pt;font-weight:800">{title}</div></div>{alpha_html}<div class="card c mt2"><span class="huge">TOTAL : …… / 20</span></div>', "★ Alpha · Test", levels=False)


def key_from(Q, answers):
    """answers : liste des bonnes réponses (texte) → clé « 1-B, … » vérifiée."""
    out = []
    for i, ((q, opts), a) in enumerate(zip(Q, answers), 1):
        out.append(f"{i}-{'ABCD'[opts.index(a)]}")
    return ", ".join(out)


def closing(b, num, items, mots):
    tb = table(["", "😀 Oui !", "🙂 Un peu", "😕 Pas encore", "La prof"], [[x, '<span class="chk"></span>', '<span class="chk"></span>', '<span class="chk"></span>', ""] for x in items], ["92mm", "20mm", "20mm", "24mm", "26mm"])
    b.page(f'<h2>✅ Je sais faire</h2>{tb}<div class="grid2 mt4"><div class="card"><b>Ce que j\'aime :</b>{lines(2)}</div><div class="card"><b>C\'est difficile :</b>{lines(2)}</div></div>', "Je sais faire", levels=False)
    half = (len(mots) + 1) // 2
    mt = lambda lst: table(["", "Français", "Dans ma langue"], [[f'<span style="font-size:12pt">{e}</span>', f"<b>{w}</b>", ""] for e, w in lst], ["12mm", "40mm", "36mm"]).replace("<td>", '<td style="padding:1.4mm 2mm">')
    b.page(f'<h2>📒 Mes mots du module {num}</h2><div class="grid2">{mt(mots[:half])}{mt(mots[half:])}</div>', "Mes mots", levels=False)


def atl_head(k, title):
    return f'<span class="atl {k}" style="font-size:12pt;padding:1.5mm 4mm">{ATELIERS[k]}</span><h2 class="mt2">{title}</h2>'


def vf(items):
    return table(["", "Vrai", "Faux"], [[x, '<span class="chk"></span>', '<span class="chk"></span>'] for x in items], ["130mm", "25mm", "25mm"])


def checks(n, rows):
    head = [""] + [str(i) for i in range(1, n + 1)]
    return table(head, [[r] + ['<span class="chk"></span>'] * n for r in rows], ["26mm"] + [f"{int(150/n)}mm"] * n)


def emogrid(items, cols=6, line=True):
    return f'<div class="grid{cols}">' + "".join(f'<div class="card c"><span class="emo">{e}</span>' + (f'<div class="word" style="font-size:10pt">{w}</div>' if w else "") + ('<div class="line"></div>' if line and not w else "") + '</div>' for e, w in items) + '</div>'
