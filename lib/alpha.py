"""Pages types du parcours ★ Alpha, réutilisables dans tous les modules du volume 1."""
import random
from .base import *
from .art import *

AL = '<div style="background:#FFD166;margin:-17mm -14mm 4mm -14mm;padding:15mm 14mm 3mm 14mm;display:flex;align-items:center;gap:4mm"><span style="font-size:22pt;font-weight:800">★ ALPHA</span><span class="big">{t}</span></div>'


def letter_page(b, E, L, son, words, distract, snd, color="#E4572E"):
    """L : lettre (ex. 'm'), son : '[m]', words : [(emoji, mot)], snd : [(emoji, mot, bool)]"""
    lo, up = L.lower(), L.upper()
    gl = [lo] * 7 + list(distract)
    random.seed(sum(map(ord, lo)) * 7)
    random.shuffle(gl)
    glh = "".join(f'<span style="display:inline-block;width:10mm;text-align:center;font-size:20pt;font-weight:600">{c}</span>' for c in gl)
    wc = "".join(f'<div class="card c"><span class="emo">{e}</span><div class="word" style="font-size:13pt">{w.replace(lo, f"<span style=color:#E4572E>{lo}</span>", 1)}</div></div>' for e, w in words)
    ex1 = E(f"La lettre {lo} — {up}. Elle fait le son {son}. J'écoute, je regarde les mots.", f'<div class="flex"><div style="font-size:{ {1: 72, 2: 46}.get(len(lo), 34)}pt;font-weight:800;color:#E4572E;line-height:1;width:55mm" class="c">{up}{lo}</div><div class="grid4 grow">{wc}</div></div>',
            ["ecoute", "regarde"], 1, "P", alpha=True, script=f"Faire entendre le son {son} longuement (sans dire « èm » : on dit le son). Dire chaque mot en insistant : {', '.join(w for _, w in words)}. Faire chercher des prénoms de la classe avec ce son.",
            sol="Activité orale.")
    ex2 = E(f"J'entoure toutes les lettres {lo}.", f'<div class="card" style="line-height:1.6">{glh}</div>', ["entoure"], 1, "B", alpha=True, sol=f"Il y a 7 lettres « {lo} ».")
    ex3 = E(f"Je trace {lo} et {up}.", trace(lo, 30, 8) + trace(up, 30, 8), ["trace"], 1, "C", alpha=True, sol=f"Observer le point de départ et le sens du tracé de « {lo} ».")
    ex4 = E(f"J'écoute le mot. J'entends {son} ? Je colorie l'image.", '<div class="grid4">' + "".join(f'<div class="card c" style="padding:2mm"><span class="emo s">{e}</span></div>' for e, w, ok in snd) + '</div>',
            ["ecoute", "colorie"], 2, "A", alpha=True, script="Dire chaque mot deux fois : " + ", ".join(w for _, w, _ in snd) + ".",
            sol="Oui : " + ", ".join(w for _, w, ok in snd if ok) + " · Non : " + ", ".join(w for _, w, ok in snd if not ok))
    ex5 = E(f"J'écris {lo} et {up} tout seul.", guide_lines(1, 20), ["ecris"], 2, "C", alpha=True, sol="Écriture autonome.")
    b.page(AL.format(t=f"La lettre {lo}") + ex1 + ex2 + ex3 + ex4 + ex5, "★ Alpha", color=color)


def syll_table(cons, vows="a i o u é"):
    vs = vows.split()
    head = "".join(f'<th style="text-align:center;font-size:16pt">{v}</th>' for v in vs)
    rows = "".join(f'<tr><th style="font-size:16pt;text-align:center">{c}</th>' + "".join(f'<td style="text-align:center;font-size:20pt;font-weight:700">{c}{v}</td>' for v in vs) + '</tr>' for c in cons)
    return f'<table class="t"><tr><th></th>{head}</tr>{rows}</table>'


def slide(c, v):
    """Visuel « la consonne glisse vers la voyelle »."""
    return (f'<div class="card c" style="padding:2mm"><svg viewBox="0 0 80 34" width="100%" height="16mm"><text x="6" y="24" font-size="20" font-family="Poppins" font-weight="700" fill="#4A7BD1">{c}</text>'
            f'<path d="M22 18 Q36 6 50 18" fill="none" stroke="#E4572E" stroke-width="1.6" marker-end="url(#a{c}{v})"/><defs><marker id="a{c}{v}" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto"><path d="M0 0 L5 2.5 L0 5Z" fill="#E4572E"/></marker></defs>'
            f'<text x="54" y="24" font-size="20" font-family="Poppins" font-weight="700" fill="#E4572E">{v}</text></svg><div class="huge">{c}{v}</div></div>')
