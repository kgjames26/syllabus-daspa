"""Volume 3 · Module 13 « Corps et santé » (sciences · B1 + français de scolarisation).

Expliquer un phénomène du corps humain : les organes et leurs fonctions (digestion, respiration, circulation),
le sommeil, l'hygiène et la prévention.
Langue : le texte explicatif ; exprimer la cause, la conséquence (approfondissement du module 3 : tellement… que,
si bien que, cela s'explique par…) et le but (pour, afin de + infinitif ; pour que, afin que + subjonctif).
FLSco : lire une infographie. Fil rouge : Yonas fait un malaise au cours d'éducation physique (il n'a pas déjeuné) ;
la classe prépare des capsules explicatives pour la semaine de la santé de l'Athénée de Hautrive.
Visuels : corps() (silhouette et organes, légendés ou numérotés), digestion() (le trajet des aliments),
circulation() (le cœur, les poumons et les muscles), info_sommeil() (infographie), etiquette() (valeurs nutritionnelles).
Faits scientifiques courants vérifiés (novembre 2026) : sommeil des 13-18 ans (8 à 10 h), activité physique des
5-17 ans (OMS : 60 minutes par jour en moyenne), sucres libres (OMS : moins de 10 % de l'énergie), numéros belges
112 et Centre Antipoisons 070 245 245.
"""
import sys
sys.path.insert(0, '/home/claude/syllabus')
from lib.base import *
from lib.art import *
from lib.module import *
from lib.v3 import CP, CPCOL, EPR, disc_tag
from lib.render import to_pdf

import os
BUMP = int(os.environ.get("BUMP", "60"))
SCR = int(os.environ.get("SCR", "120"))
MC = "#C0392B"
TINT = "#FBEAE8"
S = disc_tag("sciences")


def chk3(items, w=128):
    return table(["", "😀", "🙂", "😕"], [[x, '<span class="chk"></span>', '<span class="chk"></span>', '<span class="chk"></span>'] for x in items], [f"{w}mm", "18mm", "18mm", "18mm"])


def tall(html, h):
    return html.replace("<td></td>", f'<td style="height:{h}mm"></td>')


def compact(html):
    return html.replace('class="t"', 'class="t compact"')


def card(t, lh=2):
    return f'<div class="card" style="line-height:{lh}">{t}</div>'


ORG = [("le cerveau", 60, 22, "#E8A0BF"), ("les poumons", 48, 72, "#F4B6A6"), ("le cœur", 66, 80, "#C0392B"), ("le foie", 50, 100, "#8E5A3C"),
       ("l'estomac", 70, 104, "#E59866"), ("l'intestin grêle", 60, 126, "#F5CBA7"), ("le gros intestin", 60, 140, "#D4A373")]


def corps(labels=True, w=70):
    """Silhouette simplifiée avec 7 organes ; labels=False : numéros ①-⑦ à légender."""
    g = ('<circle cx="60" cy="24" r="16" fill="#F6E3D4" stroke="#9aa1b1" stroke-width="1"/>'
         '<rect x="54" y="39" width="12" height="8" fill="#F6E3D4" stroke="#9aa1b1" stroke-width="1"/>'
         '<path d="M32 50 Q60 42 88 50 L92 150 Q60 162 28 150 Z" fill="#F6E3D4" stroke="#9aa1b1" stroke-width="1"/>'
         '<path d="M32 52 L16 112 L22 114 L36 70" fill="#F6E3D4" stroke="#9aa1b1" stroke-width="1"/><path d="M88 52 L104 112 L98 114 L84 70" fill="#F6E3D4" stroke="#9aa1b1" stroke-width="1"/>'
         '<ellipse cx="60" cy="21" rx="11" ry="8" fill="#E8A0BF"/>'
         '<rect x="58" y="44" width="4" height="56" fill="#E59866" opacity=".55"/>'
         '<ellipse cx="47" cy="74" rx="9" ry="15" fill="#F4B6A6"/><ellipse cx="73" cy="74" rx="9" ry="15" fill="#F4B6A6"/>'
         '<path d="M62 76 q4 -6 8 0 q2 6 -6 12 q-8 -6 -6 -12 q2 -4 4 0" fill="#C0392B"/>'
         '<path d="M40 96 Q52 90 62 98 Q54 108 40 104 Z" fill="#8E5A3C"/>'
         '<ellipse cx="72" cy="102" rx="9" ry="6" fill="#E59866"/>'
         '<rect x="44" y="114" width="32" height="30" rx="7" fill="none" stroke="#D4A373" stroke-width="4"/>'
         '<path d="M50 120 q5 4 10 0 q5 -4 10 0 M50 128 q5 4 10 0 q5 -4 10 0 M50 136 q5 4 10 0 q5 -4 10 0" stroke="#F5CBA7" stroke-width="3" fill="none"/>')
    pts = [(60, 21), (47, 74), (66, 80), (48, 100), (74, 102), (60, 128), (78, 140)]
    side = ["r", "l", "r", "l", "r", "l", "r"]
    ys = [22, 60, 82, 98, 112, 126, 146]
    for k, ((x, y), sd, ly) in enumerate(zip(pts, side, ys)):
        lx = 118 if sd == "r" else 2
        tx = 120 if sd == "r" else 0
        anc = "start" if sd == "r" else "end"
        g += f'<line x1="{x}" y1="{y}" x2="{lx if sd == "r" else 30}" y2="{ly}" stroke="#1F2A44" stroke-width=".5"/>'
        t = ORG[k][0] if labels else "①②③④⑤⑥⑦"[k]
        if sd == "r":
            g += f'<text x="{tx}" y="{ly + 2}" font-size="{8 if labels else 10}" font-family="Poppins" fill="#1F2A44" text-anchor="start">{t}</text>'
        else:
            g += f'<text x="28" y="{ly + 2}" font-size="{8 if labels else 10}" font-family="Poppins" fill="#1F2A44" text-anchor="end">{t}</text>'
    vb = "-50 0 240 165"
    return f'<svg viewBox="{vb}" width="{w}mm" style="max-width:100%">{g}</svg>'


DIG = [("👄", "La bouche", "Les dents broient les aliments ; la salive les mouille."), ("⬇️", "L'œsophage", "Un tube qui conduit les aliments jusqu'à l'estomac."), ("🫙", "L'estomac", "Les aliments sont brassés avec les sucs gastriques pendant plusieurs heures."),
       ("〰️", "L'intestin grêle", "Environ 6 à 7 m de long : les nutriments passent dans le sang."), ("🔁", "Le gros intestin", "L'eau est absorbée ; les restes forment les selles."), ("🚽", "L'anus", "Les déchets non digérés sont évacués.")]


def digestion(quiz=False):
    """Le trajet des aliments (quiz=True : rôles à compléter)."""
    out = ""
    for i, (ic, t, d) in enumerate(DIG):
        dd = '<div class="line" style="margin:2.5mm 0 0"></div>' if quiz else f'<span class="xs">{d}</span>'
        out += f'<div class="card" style="padding:1.3mm 2mm;background:#fff;border-top:4px solid {MC}"><b class="sm">{ic} {i + 1}. {t}</b><br>{dd}</div>'
    return f'<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:1.5mm">{out}</div>'


def circulation():
    """La circulation du sang : un trajet en boucle (schéma simplifié)."""
    box = lambda t, c: f'<div class="card c sm" style="padding:1.5mm;background:#fff;border:2px solid {c}">{t}</div>'
    return ('<div style="display:grid;grid-template-columns:1fr 14mm 1fr 14mm 1fr;gap:1mm;align-items:center">'
            + box("🫁 <b>Les poumons</b><br><span class='xs'>le sang prend l'oxygène et rejette le dioxyde de carbone</span>", "#4A7BD1")
            + '<div class="c" style="color:#C0392B;font-weight:800">⇄</div>'
            + box("❤️ <b>Le cœur</b><br><span class='xs'>une pompe : il envoie le sang dans tout le corps (environ 60 à 100 battements par minute au repos)</span>", "#C0392B")
            + '<div class="c" style="color:#C0392B;font-weight:800">⇄</div>'
            + box("💪 <b>Les muscles et les organes</b><br><span class='xs'>le sang apporte l'oxygène et les nutriments ; il repart avec les déchets</span>", "#2BA88F")
            + '</div><p class="xs c muted" style="margin:1mm 0 0">Les <b>artères</b> partent du cœur · les <b>veines</b> reviennent au cœur · un adulte a environ 5 litres de sang.</p>')


def info_sommeil(w="100%"):
    """Infographie fictive « Le sommeil des ados » (chiffres courants)."""
    tile = lambda big, t, c: f'<div class="card c" style="padding:2mm;background:#fff;border-top:5px solid {c}"><div style="font-size:19pt;font-weight:800;color:{c};line-height:1">{big}</div><div class="xs" style="margin-top:1mm">{t}</div></div>'
    cyc = "".join(f'<div style="flex:{f};background:{c};color:#fff;font-size:7pt;text-align:center;padding:.8mm 0">{t}</div>' for f, c, t in [(1, "#9DB4E8", "endormissement"), (2, "#4A7BD1", "sommeil lent léger"), (2, "#1F2A44", "sommeil lent profond"), (1.4, "#9B5DE5", "sommeil paradoxal (rêves)")])
    return (f'<div class="doc" style="transform:none;background:#F4F7FD;border:1.5px solid #9aa1b1;padding:3mm 4mm;width:{w}">'
            f'<div class="flex" style="justify-content:space-between;align-items:center"><b style="font-size:13pt;color:#1F2A44">😴 Le sommeil des ados</b><span class="xs muted">Service PSE de Hautrive (document fictif) · chiffres d\'organismes de santé</span></div>'
            '<div class="grid4" style="gap:2mm;margin:2mm 0">' + tile("8-10 h", "de sommeil par nuit recommandées entre 13 et 18 ans", "#4A7BD1") + tile("4 à 6", "cycles de sommeil par nuit", "#9B5DE5") + tile("± 90 min", "durée moyenne d'un cycle", "#1F2A44") + tile("1 h", "sans écran avant de dormir : c'est le conseil", "#E4572E") + '</div>'
            f'<div class="xs" style="margin-bottom:1mm"><b>Un cycle de sommeil</b></div><div style="display:flex;border-radius:2mm;overflow:hidden">{cyc}</div>'
            '<div class="grid2" style="gap:2mm;margin-top:2mm"><div class="xs"><b>Pendant le sommeil,</b> le corps récupère, la mémoire trie et enregistre ce qu\'on a appris, la croissance continue.</div>'
            '<div class="xs"><b>Le manque de sommeil</b> provoque de la fatigue, des difficultés de concentration, de l\'irritabilité ; il augmente aussi le risque d\'accident.</div></div></div>')


def etiquette(fs=8.6):
    """Étiquette de boisson fictive avec tableau des valeurs nutritionnelles et Nutri-Score."""
    rows = [("Énergie", "176 kJ / 42 kcal"), ("Matières grasses", "0 g"), ("Glucides", "10,6 g"), ("dont sucres", "10,6 g"), ("Protéines", "0 g"), ("Sel", "0,02 g")]
    ns = "".join(f'<span style="display:inline-block;width:6mm;text-align:center;color:#fff;font-weight:800;background:{c};{"transform:scale(1.25);border-radius:1mm;" if l == "E" else ""}">{l}</span>' for l, c in [("A", "#1E8F4E"), ("B", "#7AC547"), ("C", "#FFC734"), ("D", "#FF7D29"), ("E", "#E63E11")])
    t = "".join(f'<tr><td style="padding:.4mm 1.5mm">{a}</td><td style="padding:.4mm 1.5mm;text-align:right">{b}</td></tr>' for a, b in rows)
    return (f'<div class="doc" style="transform:none;background:#fff;border:1.5px solid #9aa1b1;padding:2.5mm 3.5mm;font-size:{fs}pt;max-width:96mm">'
            f'<b style="font-size:11pt;color:#E4572E">FIZZ ORANGE</b> <span class="xs muted">boisson gazeuse aux fruits · canette de 33 cl (marque fictive)</span>'
            f'<div style="margin:1.5mm 0">{ns}</div>'
            f'<div class="xs"><b>Ingrédients :</b> eau gazéifiée, sucre, jus d\'orange à base de concentré (5 %), acidifiant (acide citrique), arômes, colorant.</div>'
            f'<table style="width:100%;border-collapse:collapse;margin-top:1mm;border:1px solid #1F2A44" class="xs"><tr style="background:#1F2A44;color:#fff"><td style="padding:.4mm 1.5mm"><b>Valeurs nutritionnelles</b></td><td style="padding:.4mm 1.5mm;text-align:right"><b>pour 100 ml</b></td></tr>{t}</table></div>')


def build_v3m13(start=1, tstart=1, render=True):
    b = Book("V3 · M13", "Volume 3 · Je réussis à l'école · Module 13 · Corps et santé", MC, start=start)
    E = Ex(b)
    P = {}
    vis = ('<div class="flex" style="justify-content:space-around;align-items:flex-end">' + avatar("yonas", 80, "triste") + '<div style="font-size:32pt">❤️ 🫁</div>' + avatar("amina", 80, "sourire")
           + '<div style="font-size:32pt">🍎 😴</div>' + avatar("educ", 80, "sourire") + avatar("mateo", 80, "pense") + '</div>')
    opening(b, MC, 13, "Corps et santé", vis, [("🫀", "nommer les organes et expliquer leur rôle"), ("🍽️", "expliquer la digestion, la respiration et la circulation"), ("🔗", "exprimer la cause, la conséquence et le but"),
            ("📊", "lire une infographie et une étiquette alimentaire"), ("📝", "écrire un texte explicatif"), ("🎬", "réaliser une capsule explicative")],
            ["Que se passe-t-il dans ton corps quand tu cours ?", "Combien d'heures dors-tu ? Est-ce assez ?", "Que fais-tu pour rester en bonne santé ?"],
            ["un organe", "une fonction", "la digestion", "la respiration", "le cœur", "le sang", "le sommeil", "la prévention", "parce que", "c'est pourquoi", "afin de"], TINT)

    # ---------- Découvrir ----------
    P["bd"] = b.n + 1
    bd = '<div class="grid2" style="gap:3mm">' + "".join([
        bd_case(1, lr("yonas", ["Monsieur… J'ai la tête qui tourne… Je vois des étoiles !"], "educ", ["Assieds-toi, Yonas. Respire calmement. Tu as mangé ce matin ?"], "triste", "surpris")),
        bd_case(2, lr("yonas", ["Non, je n'avais pas faim. Et j'ai dormi seulement cinq heures : j'ai joué sur mon GSM."], "educ", ["Voilà l'explication ! Ton corps manque d'énergie, c'est pourquoi tu as eu un malaise."], "triste", "sourire")),
        bd_case(3, lr("amina", ["Pourquoi est-ce qu'on a besoin de manger pour courir ?"], "prof", ["Les aliments sont digérés, puis le sang transporte les nutriments et l'oxygène jusqu'aux muscles, afin qu'ils produisent de l'énergie."], "pense", "sourire")),
        bd_case(4, lr("mateo", ["Et pourquoi le cœur bat plus vite quand on fait du sport ?"], "prof", ["Parce que les muscles ont besoin de plus d'oxygène. Le cœur pompe plus vite pour leur en apporter."], "pense", "sourire")),
        bd_case(5, lr("fatou", ["C'est passionnant ! On pourrait expliquer tout ça aux autres classes."], "prof", ["Bonne idée ! Pour la semaine de la santé, chaque groupe réalisera une capsule explicative."], "rire", "rire")),
        bd_case(6, lr("yonas", ["Moi, je ferai la capsule sur le sommeil… quand j'aurai dormi !"], "educ", ["Et demain, un vrai petit-déjeuner, d'accord ?"], "rire", "sourire")),
    ]) + '</div>'
    e = E("J'écoute et je lis la BD : Yonas fait un malaise.", bd, ["ecoute", "lis"], 1, "A",
          script="Lire deux fois en changeant de voix. ", sol="Activité orale.")
    b.page(f'<h2>Découvrir · Le malaise de Yonas</h2>{e}', "Découvrir")
    e = E("Je réponds par une phrase complète.", f'<p>1. Que ressent Yonas pendant le cours ? {blank("xl")}</p><p>2. Quelles sont les deux causes de son malaise ? {blank("xl")}</p><p>3. Selon Mme Lambert, à quoi sert le sang pendant l\'effort ? {blank("xl")}</p><p>4. Pourquoi le cœur bat-il plus vite pendant le sport ? {blank("xl")}</p><p>5. Quel projet la classe va-t-elle réaliser ? {blank("xl")}</p>', ["lis", "ecris"], 1, "B",
          sol="1. Il a la tête qui tourne et il voit des étoiles. — 2. Il n'a pas mangé le matin et il a dormi seulement cinq heures. — 3. Il transporte les nutriments et l'oxygène jusqu'aux muscles. — 4. Parce que les muscles ont besoin de plus d'oxygène : le cœur pompe plus vite pour leur en apporter. — 5. Des capsules explicatives pour la semaine de la santé.")
    e2 = E("Cause, conséquence ou but ? Je relis la BD et je classe les mots en gras.", card("1. Ton corps manque d'énergie, <b>c'est pourquoi</b> tu as eu un malaise. 2. Le sang transporte l'oxygène <b>afin qu'</b>ils produisent de l'énergie. 3. <b>Parce que</b> les muscles ont besoin de plus d'oxygène. 4. Le cœur pompe plus vite <b>pour</b> leur en apporter.", 1.9) +
           tall(compact(table(["🔍 cause", "➡️ conséquence", "🎯 but"], [["", "", ""]], ["60mm", "61mm", "61mm"])), 8), ["lis", "ecris"], 2, "C",
           sol="cause : parce que (3) · conséquence : c'est pourquoi (1) · but : afin qu' (2), pour (4)")
    e3 = E("Vrai ou faux ? Je coche et je corrige les phrases fausses.", vf(["Yonas a bien dormi la nuit dernière.", "Yonas n'a rien mangé le matin.", "M. Diallo pense que le malaise vient d'un manque d'énergie.", "Mateo fera la capsule sur le sommeil."]), ["lis", "coche"], 1, "B",
           sol="Faux (cinq heures seulement) · Vrai · Vrai · Faux (c'est Yonas)")
    e4 = E("Et toi ? Que manges-tu le matin ? Combien d'heures dors-tu ? Je réponds en 3 phrases.", lines(3), ["ecris", "duo"], 1, "C",
           sol="Ex. : Le matin, je bois un thé et je mange du pain. Je dors environ huit heures. Le week-end, je me couche plus tard.")
    b.page(f'{e}{e2}{e3}{e4}', "Découvrir")
    e = E(S + " J'observe le corps humain et ses principaux organes. Je lis les noms à voix haute.", '<div class="grid2" style="grid-template-columns:1fr 1fr;gap:3mm;align-items:center"><div class="c">' + corps(True, 78) + '</div>' +
          compact(table(["Organe", "Il sert à…"], [["le cerveau", "commander le corps, penser, ressentir"], ["les poumons", "respirer : prendre l'oxygène de l'air"], ["le cœur", "pomper le sang dans tout le corps"], ["le foie", "filtrer le sang, aider la digestion"], ["l'estomac", "brasser et digérer les aliments"], ["l'intestin grêle", "faire passer les nutriments dans le sang"], ["le gros intestin", "absorber l'eau, former les selles"]], ["34mm", "56mm"])) + '</div>', ["lis", "regarde"], 1, "B",
          sol="Lecture ; faire montrer chaque organe sur son propre corps.")
    e2 = E("J'écoute la devinette et j'écris le nom de l'organe.", card("1. ______________ 2. ______________ 3. ______________ 4. ______________ 5. ______________"), ["ecoute", "ecris"], 1, "A",
           script="1. Je bats jour et nuit, sans jamais m'arrêter. 2. Nous sommes deux, nous nous gonflons d'air. 3. Je suis dans la tête et je commande tout. 4. Je suis une poche qui brasse les aliments. 5. Je suis très long et replié dans le ventre.",
           sol="1. le cœur — 2. les poumons — 3. le cerveau — 4. l'estomac — 5. l'intestin (grêle)")
    e3 = E("Je cache le tableau et je légende le schéma : j'écris le nom de chaque organe à côté de son numéro.", '<div style="display:grid;grid-template-columns:52mm 1fr;gap:3mm;align-items:center"><div class="c">' + corps(False, 50) + '</div><div class="sm" style="line-height:1.65">① ______________ &nbsp; ② ______________<br>③ ______________ &nbsp; ④ ______________<br>⑤ ______________ &nbsp; ⑥ ______________<br>⑦ ______________</div></div>', ["regarde", "ecris"], 2, "C",
           sol="① le cerveau · ② les poumons · ③ le cœur · ④ le foie · ⑤ l'estomac · ⑥ l'intestin grêle · ⑦ le gros intestin")
    e4 = E("Défi ! Je choisis un organe et j'écris une devinette pour la classe (2 phrases, « Je… »).", lines(2), ["ecris"], 3, "C",
           sol="Ex. : Je suis le plus gros organe à l'intérieur du ventre. Je filtre le sang. → le foie")
    b.page(f'<h2>Découvrir · Le corps humain</h2>{e}{e2}{e3}{e4}', "Découvrir")

    # ---------- Lexique ----------
    e = E("Les mots du corps et de la santé. Je lis l'encadré.", '<div class="grid2">' + "".join(f'<div class="card" style="background:#fff"><b>{t}</b><p class="sm" style="margin:1mm 0 0">{d}</p></div>' for t, d in [
        ("🫀 Le corps", "un <b>organe</b> · le <b>squelette</b>, les <b>os</b> · les <b>muscles</b> · la <b>peau</b> · le <b>sang</b> · les <b>vaisseaux sanguins</b> (<b>artères</b>, <b>veines</b>) · les <b>nerfs</b> · une <b>cellule</b>"),
        ("⚙️ Les fonctions", "la <b>digestion</b> (digérer) · la <b>respiration</b> (respirer, <b>inspirer</b> / <b>expirer</b>) · la <b>circulation</b> sanguine · l'<b>oxygène</b> · le <b>dioxyde de carbone</b> · les <b>nutriments</b> · l'<b>énergie</b>"),
        ("🤒 Être malade", "un <b>symptôme</b> (la fièvre, la toux) · une <b>maladie</b> · un <b>microbe</b> (virus, bactérie) · une <b>infection</b> · <b>contagieux</b> · un <b>malaise</b> · un <b>traitement</b> · <b>guérir</b>"),
        ("🛡️ Prévenir", "la <b>prévention</b> · l'<b>hygiène</b> · un <b>vaccin</b> · une <b>alimentation équilibrée</b> · l'<b>activité physique</b> · le <b>sommeil</b> · un <b>dépistage</b> · le <b>médecin généraliste</b> · la <b>mutuelle</b> 🇧🇪")]) + '</div>', ["lis"], 1, "B", sol="Lecture de l'encadré.")
    e2 = E("Je complète avec : symptôme · contagieux · vaccin · microbes · guérir · hygiène.", card("1. La fièvre est un ______________ de la grippe. 2. Se laver les mains fait partie de l'______________ . 3. Un rhume est ______________ : il se transmet facilement. 4. Le ______________ protège contre certaines maladies. 5. Les virus et les bactéries sont des ______________ . 6. Avec du repos, on peut ______________ plus vite."), ["complete"], 1, "C",
           sol="1. symptôme — 2. hygiène — 3. contagieux — 4. vaccin — 5. microbes — 6. guérir")
    e3 = E("Les familles de mots. Je complète.", tall(compact(table(["Verbe", "Nom", "Adjectif"], [["digérer", "la digestion", "digestif"], ["respirer", "", ""], ["circuler", "", ""], ["infecter", "", ""], ["muscler", "", ""]], ["60mm", "61mm", "61mm"])), 6.5), ["complete"], 2, "C",
           sol="la respiration, respiratoire · la circulation, circulatoire · l'infection, infectieux · le muscle (la musculation), musclé (musculaire)")
    e4 = E("Le langage courant et le langage scientifique. Je relie.", relie(["avoir mal au ventre", "le battement du cœur", "attraper un microbe", "les poumons se remplissent d'air", ], ["l'inspiration", "des douleurs abdominales", "le pouls, la fréquence cardiaque", "être infecté, contracter une infection"]), ["lis", "relie"], 2, "B",
           sol="mal au ventre → douleurs abdominales · battement du cœur → pouls · attraper un microbe → contracter une infection · les poumons se remplissent → l'inspiration")
    b.page(f'<h2>Les mots du corps et de la santé</h2>{e}{e2}{e3}{e4}', "Lexique")
    e = E("Les préfixes et suffixes scientifiques. Je lis, puis je trouve le sens du mot.", '<div class="card sm" style="background:#fff"><b>cardio-</b> = le cœur · <b>gastro-</b> = l\'estomac · <b>pneumo-</b> = le poumon · <b>dermato-</b> = la peau · <b>-logue</b> = le spécialiste · <b>-ite</b> = une inflammation, une maladie</div>' +
          card("1. un cardiologue : ______________________ 2. une gastro-entérite : ______________________ 3. un dermatologue : ______________________ 4. un pneumologue : ______________________ 5. une bronchite : ______________________"), ["lis", "ecris"], 2, "C",
          sol="1. le médecin spécialiste du cœur — 2. une inflammation de l'estomac et des intestins (souvent virale) — 3. le médecin spécialiste de la peau — 4. le médecin spécialiste des poumons — 5. une inflammation des bronches")
    e2 = E("Bon pour la santé ou mauvais ? Je coche.", compact(table(["", "👍", "👎"], [[x, '<span class="chk"></span>', '<span class="chk"></span>'] for x in ["dormir 9 heures par nuit", "boire une canette de soda à chaque repas", "marcher ou faire du vélo chaque jour", "jouer sur son GSM jusqu'à minuit", "se laver les mains avant de manger", "sauter le petit-déjeuner"]], ["140mm", "21mm", "21mm"])), ["lis", "coche"], 1, "B",
           sol="👍 : 1, 3, 5 · 👎 : 2, 4, 6")
    e3 = E("Chez le médecin. Je complète le dialogue avec : ausculter · ordonnance · symptômes · fièvre · pharmacie.", card("— Bonjour docteur. J'ai mal à la gorge et je tousse. — Quels autres ______________ avez-vous ? — J'ai chaud : je crois que j'ai de la ______________ . — Je vais vous ______________ . Respirez profondément… Voici une ______________ : vous irez chercher le sirop à la ______________ ."), ["complete"], 1, "C",
           sol="symptômes · fièvre · ausculter · ordonnance · pharmacie")
    e4 = E("Défi ! J'explique en 3 phrases la différence entre un symptôme, une maladie et un traitement, avec un exemple.", lines(3), ["ecris"], 3, "C",
           sol="Ex. : Une maladie, c'est un problème de santé, comme la grippe. Un symptôme, c'est un signe de la maladie, comme la fièvre ou la toux. Un traitement, c'est ce qu'on fait pour guérir : du repos, des médicaments.")
    b.page(f'<h2>Les mots des médecins</h2>{e}{e2}{e3}{e4}', "Lexique")

    # ---------- Leçon 1 : digestion, respiration, circulation ----------
    P["fonctions"] = b.n + 1
    l1 = lecon(S + " Trois fonctions vitales : digérer, respirer, faire circuler le sang", '<p class="sm" style="margin-bottom:1.5mm">Pour vivre, chaque <b>cellule</b> du corps a besoin de <b>nutriments</b> (venus des aliments) et d\'<b>oxygène</b> (venu de l\'air). Trois fonctions travaillent ensemble pour les lui apporter.</p>' +
        '<p class="sm" style="margin:0 0 1mm"><b>① La digestion</b> transforme les aliments en nutriments.</p>' + digestion() +
        '<p class="sm" style="margin:2mm 0 1mm"><b>② La respiration</b> : quand on <b>inspire</b>, l\'air entre par le nez et la bouche, descend dans la trachée et les bronches, puis arrive dans les <b>alvéoles</b> des poumons, où l\'oxygène passe dans le sang. Quand on <b>expire</b>, on rejette le <b>dioxyde de carbone</b>, un déchet.</p>'
        '<p class="sm" style="margin:0 0 1mm"><b>③ La circulation</b> : le sang transporte l\'oxygène et les nutriments jusqu\'aux cellules, et il en ramène les déchets.</p>' + circulation() +
        '<div class="astuce" style="margin:1.5mm 0 0">🔁 <b>Rappel du module 3</b> : pour expliquer un phénomène scientifique, j\'utilise le <b>présent de vérité générale</b> : « Le cœur <b>pompe</b> le sang. » « L\'air <b>entre</b> par le nez. »</div>')
    e0 = E("Je remets le trajet de l'air dans l'ordre (1 à 5).", card("___ les bronches &nbsp; ___ le nez ou la bouche &nbsp; ___ les alvéoles des poumons &nbsp; ___ la trachée &nbsp; ___ le sang"), ["lis", "numerote"], 1, "C",
          sol="le nez ou la bouche (1) · la trachée (2) · les bronches (3) · les alvéoles (4) · le sang (5)")
    b.page(f'{l1}{e0}', "Leçon 1")
    e = E(f"Je complète le trajet d'une pomme dans le corps (aide : p. {P['fonctions']}).", digestion(True), ["ecris"], 2, "C",
           sol="La bouche : les dents broient, la salive mouille · l'œsophage : conduit à l'estomac · l'estomac : brasse avec les sucs gastriques · l'intestin grêle : les nutriments passent dans le sang · le gros intestin : absorbe l'eau, forme les selles · l'anus : évacue les déchets")
    e2 = E("Vrai ou faux ? Je coche et je corrige les phrases fausses.", vf(["Le cœur est un muscle qui pompe le sang.", "Quand on expire, on rejette de l'oxygène.", "Les nutriments passent dans le sang au niveau de l'intestin grêle.", "Les veines partent du cœur.", "Pendant le sport, le cœur bat moins vite."]), ["lis", "coche"], 1, "B",
           sol="Vrai · Faux (on rejette du dioxyde de carbone) · Vrai · Faux (les artères partent du cœur ; les veines y reviennent) · Faux (il bat plus vite)")
    e3 = E(disc_tag("maths") + " Je prends mon pouls pendant 15 secondes, au repos puis après 30 sauts. Je multiplie par 4 pour obtenir les battements par minute.", tall(compact(table(["", "Battements en 15 s", "× 4 = battements par minute"], [["Au repos", "", ""], ["Après 30 sauts", "", ""]], ["40mm", "70mm", "72mm"])), 8) + f'<p class="sm mt2">J\'explique la différence avec « parce que » : {blank("xl")}</p>', ["ecris", "duo"], 2, "C",
           sol="Ex. : 18 × 4 = 72 battements par minute au repos ; 30 × 4 = 120 après l'effort. Le cœur bat plus vite parce que les muscles ont besoin de plus d'oxygène.")
    b.page(f'{e}{e2}{e3}', "S'entraîner")

    # ---------- Leçon 2 : la cause et la conséquence ----------
    l2 = lecon("Expliquer : la cause et la conséquence", '<p class="sm" style="margin-bottom:1.5mm">🔁 <b>Rappel du module 3</b> : parce que, car, comme, grâce à, à cause de / donc, c\'est pourquoi, provoquer, entraîner. Pour expliquer avec précision, j\'ajoute de <b>nouveaux outils</b> :</p>' +
        compact(table(["", "La CAUSE (pourquoi ?)", "La CONSÉQUENCE (quel résultat ?)"], [
            ["phrases", "<b>puisque</b> (cause connue de tous) : Puisque tu as de la fièvre, reste au lit. · <b>étant donné que</b>, <b>vu que</b>", "<b>si bien que</b>, <b>de sorte que</b> : Il a couru, si bien qu'il est essoufflé. · <b>tellement</b> / <b>si</b> + adjectif + <b>que</b> : Il était si fatigué qu'il s'est endormi."],
            ["mots", "<b>en raison de</b>, <b>à la suite de</b>, <b>faute de</b> (= par manque de) : Faute de sommeil, il ne se concentre pas.", "<b>par conséquent</b>, <b>ainsi</b>, <b>c'est pour cela que</b> · <b>d'où</b> + nom : Il a mal dormi, d'où sa fatigue."],
            ["verbes", "<b>être dû à</b>, <b>s'expliquer par</b>, <b>venir de</b>, <b>résulter de</b> : Le malaise est dû au manque de sucre.", "<b>provoquer</b>, <b>entraîner</b>, <b>causer</b>, <b>favoriser</b>, <b>permettre</b> : Le tabac favorise le cancer."]], ["20mm", "81mm", "81mm"])) +
        '<div class="astuce" style="margin:2mm 0 0">🔀 La même idée, trois constructions : Yonas a eu un malaise <b>parce qu\'</b>il n\'avait pas mangé. → Le malaise de Yonas <b>est dû au</b> manque de nourriture. → Yonas n\'avait pas mangé, <b>c\'est pourquoi</b> il a eu un malaise. ⚠️ Avec un nom : <b>à cause du</b> froid · <b>grâce au</b> vaccin · <b>dû à la</b> fatigue (de + le = du).</div>')
    e = E("Je souligne la cause en bleu et la conséquence en rouge, puis j'entoure le mot qui les relie.", card("1. Puisque les microbes passent par les mains, il faut les laver souvent. 2. Il avait tellement couru qu'il avait un point de côté. 3. Faute d'eau, le corps se déshydrate. 4. La fatigue de Daria s'explique par un manque de fer. 5. L'effort augmente la température du corps, si bien qu'on transpire.", 1.9), ["souligne", "entoure"], 1, "B",
          sol="Cause / conséquence (mot) : 1. les microbes passent par les mains / il faut les laver (puisque) — 2. il avait tellement couru / un point de côté (tellement… que) — 3. faute d'eau / le corps se déshydrate (faute de) — 4. un manque de fer / la fatigue (s'explique par) — 5. l'effort augmente la température / on transpire (si bien que)")
    e2 = E("Je complète avec : puisque · faute de · si bien que · est due à · d'où.", card("1. ______________ tu tousses, mets la main devant la bouche. 2. Il n'a pas bu pendant le match, ______________ il a eu mal à la tête. 3. Sa toux ______________ une allergie au pollen. 4. ______________ sommeil, on retient moins bien ses leçons. 5. Il a mangé trop vite, ______________ son mal de ventre."), ["complete"], 2, "C",
           sol="1. Puisque — 2. si bien que — 3. est due à — 4. Faute de — 5. d'où")
    b.page(f'{l2}{e}{e2}', "Leçon 2")
    e = E("Une idée, trois phrases. Je réécris comme dans l'astuce.", '<div class="card sm" style="background:#fff">Idée : Mateo s\'est cassé le bras. Il est tombé de vélo.</div>' + f'<p>1. avec « parce que » : {blank("xl")}</p><p>2. avec « être dû à » : {blank("xl")}</p><p>3. avec « c\'est pourquoi » : {blank("xl")}</p>', ["ecris"], 2, "C",
          sol="1. Mateo s'est cassé le bras parce qu'il est tombé de vélo. — 2. La fracture de Mateo est due à une chute de vélo. — 3. Mateo est tombé de vélo, c'est pourquoi il s'est cassé le bras.")
    e2 = E("Tellement… que / si… que. Je termine les phrases.", card("1. Le soleil était si fort que ______________________ . 2. Elle avait tellement faim que ______________________ . 3. L'eau de la piscine était si froide que ______________________ ."), ["complete"], 2, "C",
           sol="Ex. : 1. … nous avons attrapé un coup de soleil. — 2. … elle a mangé deux assiettes. — 3. … nous avions la chair de poule.")
    e3 = E("J'écoute l'explication : pourquoi transpire-t-on ? Je complète le schéma des causes et des conséquences.", '<div class="flex" style="justify-content:space-between;gap:2mm;font-size:10pt">' + "".join(f'<div class="card c" style="flex:1;background:{TINT};min-height:17mm">{t}<br>______________</div>' + ('<b>➜</b>' if i < 3 else '') for i, t in enumerate(["🏃 L'effort ou la chaleur", "🌡️ La température du corps", "💧 La peau", "🌬️ La sueur s'évapore"])) + '</div>', ["ecoute", "complete"], 2, "A",
           script="« Quand on fait un effort ou qu'il fait chaud, la température du corps augmente. Or, le corps doit rester autour de 37 °C. C'est pourquoi la peau produit de la sueur. En s'évaporant, la sueur refroidit la peau. La transpiration permet donc de garder une température stable. »",
           sol="L'effort ou la chaleur : fait monter la température · la température du corps : augmente (doit rester à 37 °C) · la peau : produit de la sueur · la sueur s'évapore : refroidit la peau")
    e4 = E("Le texte de Fatou est trop répétitif (« parce que » partout). Je le réécris avec trois outils différents.", '<div class="card" style="font-family:\'Comic Sans MS\',cursive;background:#fff;font-size:10pt">« On a des caries parce qu\'on mange trop de sucre. Les dents se cassent parce que les bactéries attaquent l\'émail. On a mal parce que le nerf est touché. »</div>' + lines(3), ["lis", "ecris"], 3, "C",
           sol="Ex. : Les caries sont dues à une consommation excessive de sucre. En effet, les bactéries attaquent l'émail, si bien que la dent s'abîme. Quand le nerf est touché, la carie provoque une forte douleur.")
    e5 = E("Défi ! Le manque de sommeil : j'écris 4 phrases avec 4 conséquences différentes (provoquer, si bien que, d'où, tellement… que).", lines(3), ["ecris"], 3, "C",
           sol="Ex. : Le manque de sommeil provoque de la fatigue. Yonas s'est couché tard, si bien qu'il s'est endormi en classe. Il a mal dormi, d'où sa mauvaise humeur. Il était tellement fatigué qu'il a oublié son interro.")
    b.page(f'{e}{e2}{e3}{e4}{e5}', "S'entraîner")

    # ---------- Leçon 3 : le but ----------
    l3 = lecon("Exprimer le but (pour quoi faire ?)", compact(table(["Construction", "Quand ?", "Exemples"], [
        ["<b>pour</b>, <b>afin de</b> + infinitif", "même sujet dans les deux parties", "Je me lave les mains <b>pour éviter</b> les microbes. · On se vaccine <b>afin de se protéger</b>."],
        ["<b>pour que</b>, <b>afin que</b> + <b>subjonctif</b>", "deux sujets différents", "Le cœur bat plus vite <b>pour que</b> les muscles <b>reçoivent</b> plus d'oxygène."],
        ["<b>pour ne pas</b> + infinitif · <b>pour que… ne… pas</b>", "un but négatif", "Il tousse dans son coude <b>pour ne pas contaminer</b> les autres. · Couvre ton petit frère <b>pour qu\'</b>il <b>ne</b> tombe <b>pas</b> malade."],
        ["<b>servir à</b>, <b>permettre de</b> + infinitif · <b>avoir pour rôle de</b>", "pour dire la fonction d'un organe ou d'un objet", "Les poumons <b>servent à</b> respirer. · La salive <b>permet de</b> mouiller les aliments."]], ["52mm", "40mm", "90mm"])) +
        '<div class="astuce" style="margin:2mm 0 0">🔁 <b>Rappel du module 11</b> : après « pour que » et « afin que », le verbe est au <b>subjonctif</b> (que je sois, qu\'il ait, qu\'il puisse, qu\'il reçoive…). ⚠️ Ne confonds pas le <b>but</b> (pour que + subjonctif : ce que je veux obtenir) et la <b>conséquence</b> (si bien que + indicatif : ce qui se passe réellement).</div>')
    e = E("But ou conséquence ? J'entoure, puis je justifie avec le mode du verbe.", card("1. Il boit beaucoup d'eau <b>pour que</b> son corps soit bien hydraté. (but / conséquence) 2. Il a bu beaucoup d'eau, <b>si bien qu'</b>il n'a plus soif. (but / conséquence) 3. Elle dort tôt <b>afin d'</b>être en forme. (but / conséquence) 4. Il a dormi tard, <b>de sorte qu'</b>il a raté le bus. (but / conséquence)", 1.9), ["lis", "entoure"], 1, "C",
          sol="1. but (subjonctif « soit ») — 2. conséquence (indicatif « n'a plus ») — 3. but (infinitif) — 4. conséquence (indicatif « a raté »)")
    e2 = E("Pour + infinitif ou pour que + subjonctif ? Je complète.", card("1. Je mange des fruits pour (avoir) ______________ des vitamines. 2. La maman donne des fruits à son fils pour qu'il (avoir) ______________ des vitamines. 3. Le médecin ausculte le patient afin de (comprendre) ______________ le problème. 4. L'infirmière explique le traitement afin que le patient le (prendre) ______________ correctement. 5. Ouvre la fenêtre pour que l'air (être) ______________ renouvelé."), ["complete"], 2, "C",
           sol="1. avoir — 2. ait — 3. comprendre — 4. prenne — 5. soit")
    b.page(f'{l3}{e}{e2}', "Leçon 3")
    e = E(S + " À quoi ça sert ? J'écris la fonction de chaque partie du corps avec « servir à », « permettre de » ou « avoir pour rôle de ».", f'<p>1. Les dents → {blank("xl")}</p><p>2. Les poumons → {blank("xl")}</p><p>3. Le squelette → {blank("xl")}</p><p>4. La peau → {blank("xl")}</p>', ["ecris"], 2, "C",
          sol="Ex. : 1. Les dents servent à couper et à broyer les aliments. — 2. Les poumons permettent de faire entrer l'oxygène dans le sang. — 3. Le squelette a pour rôle de soutenir et de protéger le corps. — 4. La peau sert à protéger le corps contre les microbes et à garder la bonne température.")
    e2 = E("Les gestes barrières. Je relie le geste et son but, puis j'écris deux phrases avec « pour » ou « afin de ».", relie(["Je me lave les mains.", "Je tousse dans mon coude.", "J'aère la classe.", "Je me fais vacciner.", "Je reste à la maison quand j'ai de la fièvre."], ["renouveler l'air", "ne pas contaminer mes camarades", "éliminer les microbes", "ne pas projeter de gouttelettes sur les autres", "me protéger contre une maladie"]) + lines(2), ["relie", "ecris"], 1, "B",
           sol="mains → éliminer les microbes · coude → ne pas projeter de gouttelettes · aérer → renouveler l'air · vaccin → me protéger · rester à la maison → ne pas contaminer. Ex. : Je me lave les mains pour éliminer les microbes.")
    e3 = E("J'écoute les conseils de l'infirmière scolaire. Je complète avec le verbe au subjonctif.", card("« Mangez un vrai petit-déjeuner pour que votre cerveau ______________ (avoir) de l'énergie. Buvez de l'eau afin que votre corps ______________ (être) bien hydraté. Éteignez les écrans une heure avant de dormir pour que le sommeil ______________ (venir) plus facilement. Et bougez chaque jour, pour que vos muscles et votre cœur ______________ (rester) en forme ! »", 1.95), ["ecoute", "complete"], 2, "A",
           script="Lire le texte avec les verbes au subjonctif.", sol="ait · soit · vienne · restent")
    e4 = E("Défi ! J'écris 4 conseils pour un camarade qui prépare ses examens, avec quatre constructions du but (pour, afin de, pour que, pour ne pas).", lines(4), ["ecris"], 3, "C",
           sol="Ex. : Dors huit heures pour être concentré. Fais des pauses afin de reposer ton cerveau. Range ton GSM pour que tes notifications ne te dérangent pas. Mange un fruit pour ne pas avoir de coup de fatigue.")
    b.page(f'{e}{e2}{e3}{e4}', "S'entraîner")

    # ---------- Leçon 4 (FLSco) : lire une infographie ----------
    P["info"] = b.n + 1
    l4 = lecon("Lire une infographie", '<p class="sm" style="margin-bottom:1.5mm">Une <b>infographie</b> présente des informations avec peu de texte : des <b>chiffres</b> mis en valeur, des <b>pictogrammes</b>, des <b>graphiques</b>, des couleurs. On la trouve dans les manuels, les journaux, les affiches de prévention.</p>' +
        compact(table(["Étape", "Je me demande…"], [["① Le titre et la source", "De quoi parle-t-on ? Qui a fait le document ? Est-ce fiable ?"], ["② Le parcours de lecture", "Par où commencer ? (souvent de haut en bas, de gauche à droite, du plus grand au plus petit)"], ["③ Les chiffres et les unités", "Que mesure chaque chiffre ? (heures, %, minutes…) Pour qui ? (âge, pays…)"], ["④ Les graphiques et la légende", "Que représentent les couleurs, les barres, les parts ?"], ["⑤ Le message", "Qu'est-ce que le document veut que je comprenne ou que je fasse ?"]], ["48mm", "134mm"])) +
        '<div class="mt2">' + info_sommeil() + '</div>' +
        '<div class="astuce" style="margin:2mm 0 0">✍️ <b>Pour rédiger ce que dit une infographie</b>, je fais des phrases complètes : « Selon le service PSE, les jeunes de 13 à 18 ans <b>ont besoin de</b> 8 à 10 heures de sommeil. » « Une nuit <b>compte</b> 4 à 6 cycles <b>d\'environ</b> 90 minutes. » Je cite la <b>source</b> et je garde les <b>unités</b>.</div>')
    b.page(f'<span class="tag-doc">🎒 FRANÇAIS DE L\'ÉCOLE</span>{l4}', "Consignes & école")
    e = E(f"Je relis l'infographie « Le sommeil des ados » (p. {P['info']}). Je réponds par des phrases complètes.", f'<p class="sm">1. Qui a réalisé cette infographie ? Pour quel public ? {blank("xl")}</p><p class="sm">2. Combien d\'heures un ado de 15 ans devrait-il dormir ? {blank("l")}</p><p class="sm">3. Combien de temps dure environ un cycle ? Combien de cycles y a-t-il dans une nuit ? {blank("xl")}</p><p class="sm">4. Dans quelle phase du sommeil rêve-t-on ? {blank("l")}</p><p class="sm">5. Cite deux conséquences du manque de sommeil. {blank("xl")}</p><p class="sm">6. Quel est le message principal du document ? {blank("xl")}</p>', ["lis", "ecris"], 2, "B",
          sol="1. Le service PSE de Hautrive (fictif), pour les adolescents (et leurs parents). — 2. Entre 8 et 10 heures par nuit. — 3. Environ 90 minutes ; 4 à 6 cycles. — 4. Pendant le sommeil paradoxal. — 5. Fatigue, difficultés de concentration, irritabilité, risque d'accident (deux au choix). — 6. Les ados doivent dormir assez (8 à 10 h) et éteindre les écrans avant de dormir.")
    e2 = E(disc_tag("maths") + " Yonas se couche à 0 h 30 et se lève à 6 h 45. Combien de temps dort-il ? Combien d'heures lui manque-t-il au minimum ? Combien de cycles complets de 90 minutes a-t-il pu faire ?", f'<p>{blank("xl")}</p><p>{blank("xl")}</p>', ["ecris"], 2, "C",
           sol="De 0 h 30 à 6 h 45 : 6 h 15 de sommeil · il lui manque au minimum 8 h − 6 h 15 = 1 h 45 · 6 h 15 = 375 min ; 375 ÷ 90 ≈ 4,2 → 4 cycles complets.")
    e3 = E("Je crée une petite infographie pour la classe : « Bien commencer la journée ». Je choisis un titre, une source, trois chiffres ou conseils avec un pictogramme, et un message final.", '<div style="height:62mm;border:1.5px dashed #9aa1b1;border-radius:3mm;background:#fff"></div>', ["dessine", "ecris"], 3, "C",
           sol="Infographie avec titre, source (ex. : « d'après l'infirmerie de l'école »), trois informations courtes avec pictogrammes (ex. : 1 vrai petit-déjeuner, 1 verre d'eau, 8 à 10 h de sommeil la veille), un message clair.")
    b.page(f'{e}{e2}{e3}', "Consignes & école")
    act = [("Marche ou vélo pour aller à l'école", 34), ("Sport en club", 28), ("Éducation physique à l'école", 21), ("Moins de 30 minutes par jour", 17)]
    bars = "".join(f'<div style="display:grid;grid-template-columns:58mm 1fr 12mm;gap:2mm;align-items:center;margin-bottom:1.2mm"><span class="xs">{t}</span><div style="height:5mm;width:{v * 2.4}%;background:{MC};border-radius:1mm"></div><b class="xs">{v} %</b></div>' for t, v in act)
    e = E("Je lis le graphique (sondage fictif réalisé dans l'Athénée) et je réponds.", f'<div class="card" style="background:#fff"><b class="sm">Comment les 300 élèves de l\'Athénée bougent-ils le plus ? (une réponse par élève)</b><div style="margin-top:2mm">{bars}</div><span class="xs muted">Recommandation de l\'OMS pour les 5-17 ans : au moins 60 minutes d\'activité physique par jour en moyenne.</span></div>' +
          f'<p class="sm mt2">1. Quelle est la façon de bouger la plus fréquente ? {blank("xl")}</p><p class="sm">2. Combien d\'élèves (sur 300) bougent moins de 30 minutes par jour ? {blank("l")}</p><p class="sm">3. Ces élèves respectent-ils la recommandation de l\'OMS ? Explique. {blank("xl")}</p>', ["lis", "ecris"], 2, "B",
          sol="1. Aller à l'école à pied ou à vélo (34 %). — 2. 17 % de 300 = 51 élèves. — 3. Non : l'OMS recommande au moins 60 minutes par jour en moyenne ; ils en font moins de 30.")
    e2 = E("Les consignes pour lire un document. Je relie la consigne et ce qu'il faut faire.", relie(["Identifiez la source.", "Relevez les données chiffrées.", "Interprétez le graphique.", "Dégagez le message.", "Comparez avec la norme."], ["Je dis ce que le graphique montre et ce que j'en conclus.", "Je dis qui a produit le document.", "Je regarde si les chiffres sont au-dessus ou en dessous de la recommandation.", "Je recopie les nombres avec leur unité.", "Je dis ce que le document veut faire comprendre."]), ["lis", "relie"], 1, "B",
           sol="source → qui a produit · données chiffrées → nombres et unités · interprétez → ce que montre le graphique et la conclusion · message → ce que le document veut faire comprendre · norme → au-dessus ou en dessous")
    e3 = E("Défi ! Je rédige en 3 phrases ce que montre le graphique, comme dans l'astuce de la leçon (source, chiffres avec unités, conclusion).", lines(3), ["ecris"], 3, "C",
           sol="Ex. : Selon un sondage réalisé à l'Athénée, 34 % des élèves bougent surtout en allant à l'école à pied ou à vélo. Cependant, 17 % d'entre eux bougent moins de 30 minutes par jour. Ces élèves n'atteignent donc pas les 60 minutes recommandées par l'OMS.")
    b.page(f'{e}{e2}{e3}', "Consignes & école")

    # ---------- Leçon 5 : le texte explicatif ----------
    P["expl"] = b.n + 1
    modele = [("① Le titre-question", "Pourquoi a-t-on des courbatures ?"),
              ("② L'introduction", "Après une longue randonnée ou une première séance de sport, on a souvent mal aux muscles le lendemain : ce sont des <b>courbatures</b>. D'où viennent-elles ?"),
              ("③ L'explication, étape par étape", "<b>D'abord</b>, pendant un effort inhabituel, les fibres des muscles subissent de <b>minuscules déchirures</b>. <b>Ensuite</b>, le corps répare ces fibres : il se produit une petite <b>inflammation</b>, <b>c'est-à-dire</b> une réaction de défense. <b>C'est pourquoi</b> le muscle devient sensible et douloureux, en général 24 à 72 heures après l'effort. <b>Enfin</b>, une fois réparées, les fibres sont un peu plus solides."),
              ("④ La conclusion (et un conseil)", "Les courbatures ne sont donc pas graves : elles montrent que le muscle s'adapte. <b>Pour les éviter</b>, il vaut mieux reprendre le sport progressivement.")]
    l5 = lecon("Le texte explicatif", '<p class="sm" style="margin-bottom:1.5mm">Un <b>texte explicatif</b> répond à une question <b>pourquoi ?</b> ou <b>comment ?</b>. Il ne donne pas d\'opinion : il fait <b>comprendre</b> un phénomène. On le trouve dans les manuels, les magazines de vulgarisation, les capsules vidéo.</p>' +
        '<div class="card" style="background:#fff;padding:2mm 3mm">' + "".join(f'<p class="sm" style="margin:0 0 1.2mm"><b style="color:{MC}">{t}</b><br>{x}</p>' for t, x in modele) + '</div>' +
        compact(table(["Les outils du texte explicatif", "Exemples"], [["le <b>présent de vérité générale</b>", "Le muscle <b>se répare</b>."], ["les <b>connecteurs</b> d'étapes", "d'abord, ensuite, puis, enfin · quand, lorsque"], ["la <b>cause</b>, la <b>conséquence</b>, le <b>but</b>", "parce que, c'est pourquoi, pour + infinitif"], ["les <b>définitions</b> et <b>reformulations</b>", "c'est-à-dire · on appelle… · ce qu'on nomme… · autrement dit"], ["le vocabulaire <b>précis</b>, le <b>pronom « on »</b>", "les fibres, une inflammation · on a mal"]], ["70mm", "112mm"])))
    e = E("Je relis le texte sur les courbatures et je réponds.", f'<p class="sm">1. À quelle question le texte répond-il ? {blank("xl")}</p><p class="sm">2. Relève les trois connecteurs d\'étapes. {blank("l")}</p><p class="sm">3. Quel mot est défini avec « c\'est-à-dire » ? Recopie la définition. {blank("xl")}</p>', ["lis", "ecris"], 1, "B",
          sol="1. Pourquoi a-t-on des courbatures ? — 2. D'abord, Ensuite, Enfin (« c'est pourquoi » exprime la conséquence). — 3. L'inflammation : « une réaction de défense ».")
    b.page(f'{l5}{e}', "Leçon 5")
    e = E("Explicatif ou argumentatif ? Je coche et je justifie avec un indice.", compact(table(["", "explicatif", "argumentatif", "Indice"], [["« Le cœur est un muscle creux qui se contracte environ 70 fois par minute. »", '<span class="chk"></span>', '<span class="chk"></span>', ""], ["« Je pense qu'on devrait interdire les sodas à l'école. »", '<span class="chk"></span>', '<span class="chk"></span>', ""], ["« Lorsqu'on a froid, les poils se dressent : c'est la chair de poule. »", '<span class="chk"></span>', '<span class="chk"></span>', ""], ["« Il est scandaleux que les cantines servent si peu de légumes ! »", '<span class="chk"></span>', '<span class="chk"></span>', ""]], ["92mm", "20mm", "24mm", "46mm"])), ["lis", "coche"], 1, "B",
          sol="explicatif (faits, présent de vérité générale) · argumentatif (« je pense », « on devrait ») · explicatif (lorsque…, définition) · argumentatif (« il est scandaleux », point d'exclamation)")
    e2 = E("Je remets dans l'ordre l'explication « Comment se forme un bleu ? » (1 à 5), puis je souligne les connecteurs.", '<div class="card sm" style="line-height:1.8">___ Ensuite, le sang s\'échappe et se répand sous la peau, c\'est pourquoi la peau devient bleue ou violette.<br>___ Un bleu, ou <i>hématome</i>, apparaît souvent après un choc. Comment se forme-t-il ?<br>___ Enfin, après une à deux semaines, le corps a éliminé le sang : le bleu disparaît.<br>___ D\'abord, le choc abîme de petits vaisseaux sanguins sous la peau.<br>___ Puis, en quelques jours, le corps « nettoie » ce sang : la tache devient verte, puis jaune.</div>', ["lis", "numerote", "souligne"], 2, "C",
           sol="Un bleu, ou hématome… (1) · D'abord… (2) · Ensuite… (3) · Puis… (4) · Enfin… (5) ; connecteurs : d'abord, ensuite, c'est pourquoi, puis, enfin")
    e3 = E("Je définis chaque mot avec « c'est-à-dire », « on appelle… » ou « autrement dit ».", f'<p class="sm">1. la déshydratation → {blank("xl")}</p><p class="sm">2. un vaccin → {blank("xl")}</p><p class="sm">3. le pouls → {blank("xl")}</p>', ["ecris"], 2, "C",
           sol="Ex. : 1. Le corps se déshydrate, c'est-à-dire qu'il manque d'eau. — 2. On appelle vaccin un produit qui apprend au corps à se défendre contre une maladie. — 3. Le pouls, autrement dit le nombre de battements du cœur par minute, augmente pendant l'effort.")
    e4 = E("Défi ! J'écris l'introduction (2 phrases) d'un texte explicatif sur la question « Pourquoi a-t-on la chair de poule ? » : je présente le phénomène, puis je pose la question.", lines(2), ["ecris"], 3, "C",
           sol="Ex. : Quand on a froid ou qu'on a peur, de petites bosses apparaissent sur la peau et les poils se dressent : c'est la chair de poule. Mais pourquoi notre corps réagit-il ainsi ?")
    b.page(f'{e}{e2}{e3}{e4}', "S'entraîner")

    # ---------- Documents de la vie ----------
    e = E("Je lis l'étiquette de la boisson et je réponds.", '<div class="grid2" style="grid-template-columns:auto 1fr;gap:3mm;align-items:start">' + etiquette() +
          '<div class="card sm" style="background:' + TINT + '"><b>Le saviez-vous ?</b> L\'OMS recommande de limiter les <b>sucres libres</b> (sucres ajoutés, miel, sirops, jus de fruits) à <b>moins de 10 %</b> de l\'énergie que l\'on consomme chaque jour, et si possible à moins de 5 %, soit environ <b>25 g</b> (6 cuillères à café) pour un adulte. Un morceau de sucre pèse environ 5 g. <br>Le <b>Nutri-Score</b> (de A, vert, à E, rouge) est utilisé en Belgique depuis 2019 pour comparer les aliments d\'une même catégorie.</div></div>' +
          f'<p class="sm mt2">1. Combien de sucres y a-t-il dans 100 ml ? Dans la canette entière (33 cl = 330 ml) ? {blank("xl")}</p><p class="sm">2. Cela fait combien de morceaux de sucre (5 g) ? {blank("l")}</p><p class="sm">3. Compare avec les 25 g conseillés par jour : que remarques-tu ? {blank("xl")}</p><p class="sm">4. Quel est le Nutri-Score de cette boisson ? Que signifie-t-il ? {blank("xl")}</p><p class="sm">5. Que pourrait-on boire à la place ? Pourquoi ? {blank("xl")}</p>', ["lis", "ecris"], 2, "B",
          sol="1. 10,6 g pour 100 ml ; 10,6 × 3,3 ≈ 35 g pour la canette. — 2. 35 ÷ 5 = 7 morceaux de sucre. — 3. Une seule canette dépasse les 25 g conseillés pour toute la journée. — 4. E (rouge) : la boisson est peu favorable à la santé par rapport aux autres boissons. — 5. De l'eau (pas de sucre, elle hydrate), éventuellement aromatisée avec un fruit.")
    e2 = E("Je lis la liste des ingrédients. Dans quel ordre sont-ils classés, à ton avis ? Quel est l'ingrédient principal ? Le deuxième ?", lines(2), ["lis", "ecris"], 2, "B",
           sol="Du plus important au moins important (par quantité décroissante). L'ingrédient principal est l'eau gazéifiée ; le deuxième est le sucre.")
    b.page(f'<span class="tag-doc">📄 DOCUMENT DE LA VIE</span><h2>L\'étiquette d\'une boisson</h2>{e}{e2}', "Document de la vie")
    urg = f'''<div class="doc" style="transform:none;border:2px solid {MC};background:#fff;padding:3mm 4mm;font-size:9.2pt;line-height:1.38">
<div class="flex" style="justify-content:space-between;align-items:center"><b style="font-size:13pt;color:{MC}">🚑 Santé : qui appeler ?</b><span class="xs muted">Affiche de l'infirmerie · Athénée de Hautrive (document fictif ; numéros réels en Belgique)</span></div>
<div class="grid2" style="gap:3mm;margin-top:1.5mm">
<div><b style="color:{MC}">112</b> · <b>Urgence vitale</b> (ambulance, pompiers) : quelqu'un est inconscient, ne respire plus, saigne beaucoup, a été gravement blessé. Appel gratuit, même sans crédit, dans toute l'Union européenne.<br><b style="color:{MC}">070 245 245</b> · <b>Centre Antipoisons</b>, 24 h sur 24 : un enfant a avalé un produit ménager, un médicament, une plante…<br><b style="color:{MC}">1733</b> · <b>Médecin de garde</b> : la nuit, le week-end et les jours fériés, quand votre médecin généraliste n'est pas disponible et que ce n'est pas une urgence vitale.</div>
<div><b>💡 Au téléphone, je dis :</b><br>① qui je suis et d'où j'appelle (adresse précise) ;<br>② ce qui s'est passé ;<br>③ l'état de la personne (consciente ? elle respire ?) ;<br>④ je réponds aux questions et je ne raccroche pas le premier.<br><b>À l'école :</b> je préviens tout de suite un adulte (professeur, éducateur, infirmerie).</div></div></div>'''
    e = E("Je lis l'affiche de l'infirmerie. Quel numéro faut-il appeler ? Je complète le tableau.", urg + tall(compact(table(["Situation", "Numéro", "Pourquoi ?"], [["Samedi soir, ton petit frère a 39 °C de fièvre depuis deux jours ; il parle et boit normalement.", "", ""], ["Ta petite sœur a bu du produit pour le lave-vaisselle.", "", ""], ["Dans la rue, un homme tombe et ne répond plus.", "", ""]], ["92mm", "26mm", "64mm"])), 6), ["lis", "ecris"], 2, "B",
          sol="1733 (médecin de garde : pas une urgence vitale, le week-end) · 070 245 245 (Centre Antipoisons ; si elle est inconsciente ou respire mal : 112) · 112 (urgence vitale : il est inconscient)")
    e2 = E("J'écris ce que je dis au 112 pour l'homme tombé dans la rue (4 phrases, en suivant les conseils de l'affiche).", lines(3), ["ecris", "parle"], 2, "A",
           sol="Ex. : Bonjour, je m'appelle Fatou Camara, j'appelle de la rue des Tilleuls 14 à Hautrive. Un homme est tombé sur le trottoir. Il ne répond plus, mais il respire. Que dois-je faire ?")
    e3 = E("Belgicismes de la santé. Je relie le mot belge et son équivalent en France.", relie(["la mutuelle", "un médecin généraliste", "une maison médicale", "la garde (du médecin)"], ["un centre de santé avec plusieurs soignants", "la caisse d'assurance maladie obligatoire (+ complémentaire)", "la permanence de soins la nuit et le week-end", "un médecin traitant"]), ["lis", "relie"], 1, "B",
           sol="mutuelle → assurance maladie obligatoire (en Belgique, la mutuelle rembourse les soins de l'assurance obligatoire ; en France, la « mutuelle » est surtout complémentaire) · médecin généraliste → médecin traitant · maison médicale → centre de santé · garde → permanence de soins")
    b.page(f'<span class="tag-doc">📄 DOCUMENT DE LA VIE</span><h2>En cas d\'urgence</h2>{e}{e2}{e3}', "Document de la vie")

    # ---------- Vers les épreuves ----------
    TXT = ["« Hic ! » Tout le monde a déjà eu le hoquet. Ce petit bruit, gênant mais le plus souvent inoffensif, intrigue les scientifiques depuis longtemps. Que se passe-t-il exactement dans notre corps ?",
           "Le hoquet est provoqué par une contraction brusque et involontaire du diaphragme, le grand muscle situé sous les poumons qui nous permet de respirer. Lorsqu'il se contracte de cette façon, l'air entre très vite dans la gorge. Aussitôt, la glotte, c'est-à-dire l'ouverture située entre les cordes vocales, se ferme d'un coup. C'est cette fermeture brutale qui produit le fameux « hic ».",
           "Plusieurs situations peuvent déclencher le hoquet : manger trop vite ou trop, boire une boisson gazeuse, rire aux éclats, ou encore vivre une émotion forte. Dans la plupart des cas, il disparaît tout seul après quelques minutes. Les « remèdes » de grand-mère, comme retenir sa respiration ou boire un verre d'eau la tête en bas, n'ont pas toujours été prouvés scientifiquement, même si certains semblent aider.",
           "Pourquoi avons-nous le hoquet ? Les chercheurs n'ont pas encore de réponse définitive. Une hypothèse est qu'il s'agirait d'un réflexe hérité de notre développement avant la naissance. Une chose est sûre : si le hoquet dure plus de deux jours, il faut consulter un médecin, car il peut alors être le signe d'un autre problème de santé."]
    P["epr"] = b.n + 1
    texte = '<div class="card" style="background:#fff;font-size:9.5pt;line-height:1.44;padding:2.5mm 4mm"><b style="color:' + MC + '">Le hoquet : un mystère qui fait « hic »</b> <span class="xs muted">(article de vulgarisation écrit pour le cahier)</span>' + "".join(f'<p style="margin:1.1mm 0"><b class="xs" style="color:{MC}">§{i}</b> {t}</p>' for i, t in enumerate(TXT, 1)) + '</div>'
    e = E("Entraînement de type CE1D : je lis l'article et je réponds en justifiant.", texte +
          f'<p class="sm mt2" style="margin-bottom:1mm">a) À quelle question principale le texte répond-il ? {blank("xl")}</p><p class="sm" style="margin-bottom:1mm">b) Explique avec tes mots comment se produit le « hic » (§ 2). Utilise deux connecteurs. {blank("xl")}{blank("xl")}</p><p class="sm" style="margin-bottom:1mm">c) Recopie la définition de la glotte. Quel outil introduit cette définition ? {blank("xl")}</p><p class="sm" style="margin-bottom:1mm">d) Cite trois causes possibles du hoquet (§ 3). {blank("xl")}</p><p class="sm" style="margin-bottom:1mm">e) Vrai ou faux ? Justifie par une citation : « Boire un verre d\'eau la tête en bas arrête toujours le hoquet. » {blank("xl")}</p><p class="sm" style="margin-bottom:1mm">f) « il <b>s\'agirait</b> d\'un réflexe » (§ 4) : à quel mode est ce verbe ? Pourquoi l\'auteur l\'utilise-t-il ? {blank("xl")}</p>', ["lis", "ecris"], 3, "C",
          sol="a) Que se passe-t-il dans notre corps quand on a le hoquet ? (pourquoi / comment a-t-on le hoquet ?) — b) D'abord, le diaphragme se contracte brusquement ; ensuite, l'air entre vite dans la gorge ; enfin, la glotte se ferme d'un coup, ce qui produit le « hic ». — c) « l'ouverture située entre les cordes vocales » ; « c'est-à-dire ». — d) Manger trop vite ou trop, boire une boisson gazeuse, rire aux éclats, une émotion forte (trois au choix). — e) Faux : les remèdes « n'ont pas toujours été prouvés scientifiquement ». — f) Conditionnel présent : l'information n'est pas confirmée, c'est une hypothèse (module 8).")
    b.page(EPR.format(k="CE1D", t="Lire un article de vulgarisation") + e, "Vers les épreuves")
    e = E("Suite de l'épreuve.", f'<p class="sm">g) Dans quel cas faut-il consulter un médecin ? Relève le mot qui introduit la cause de ce conseil. {blank("xl")}</p><p class="sm">h) Ce texte est-il explicatif ou argumentatif ? Donne deux indices. {blank("xl")}</p>', ["lis", "ecris"], 3, "C",
          sol="g) Si le hoquet dure plus de deux jours ; « car ». — h) Explicatif : il répond à une question (que se passe-t-il ?), il présente des faits au présent de vérité générale, des définitions, des causes ; il ne donne pas d'opinion.")
    e2 = E("Entraînement DELF B1 · compréhension des écrits. Je lis le texte et je réponds.", f'<div class="card" style="background:{TINT};font-size:9.4pt"><b>L\'eau, le carburant du corps</b><br>Notre corps est composé en grande partie d\'eau : environ 60 % chez un adulte. Chaque jour, nous en perdons par la respiration, la transpiration et les urines. Il faut donc la remplacer, en buvant (on conseille généralement environ 1,5 litre de boissons par jour) et en mangeant des aliments riches en eau, comme les fruits et les légumes. La soif est un signal d\'alarme : quand on la ressent, le corps a déjà commencé à manquer d\'eau. Une légère déshydratation suffit à provoquer de la fatigue, des maux de tête et une baisse de concentration. Pendant le sport ou les fortes chaleurs, il faut boire davantage. <span class="xs muted">(texte écrit pour le cahier)</span></div>' +
           f'<p class="sm mt2">1. Quelle proportion du corps d\'un adulte est faite d\'eau ? {blank("l")}</p><p class="sm">2. Cite deux façons dont le corps perd de l\'eau. {blank("xl")}</p><p class="sm">3. Pourquoi ne faut-il pas attendre d\'avoir soif pour boire ? {blank("xl")}</p><p class="sm">4. Vrai ou faux ? « Les fruits ne participent pas à l\'hydratation. » Justifie. {blank("xl")}</p><p class="sm">5. Cite deux conséquences d\'une légère déshydratation. {blank("xl")}</p><p class="sm">6. Dans quelles situations faut-il boire davantage ? {blank("xl")}</p><p class="sm">7. Résume le texte en deux phrases, avec un connecteur de conséquence.</p>{lines(2)}<div class="astuce">🎓 Au DELF B1, la compréhension des écrits compte deux textes et dure environ 45 minutes. Lis d\'abord les questions, puis cherche la réponse dans le texte : souvent, il faut <b>justifier</b> en recopiant une phrase.</div>', ["lis", "ecris"], 3, "B",
           sol="1. Environ 60 %. — 2. La respiration, la transpiration, les urines (deux au choix). — 3. Parce que la soif est un signal d'alarme : le corps a déjà commencé à manquer d'eau. — 4. Faux : on remplace l'eau « en mangeant des aliments riches en eau, comme les fruits et les légumes ». — 5. Fatigue, maux de tête, baisse de concentration (deux au choix). — 6. Pendant le sport et les fortes chaleurs. — 7. Ex. : Notre corps perd de l'eau chaque jour ; il faut donc boire régulièrement, sans attendre d'avoir soif.")
    b.page(f'{e}{e2}', "Vers les épreuves")

    # ---------- Sons ----------
    e = E("[y] ou [u] ? J'écoute et je répète.", '<div class="grid2"><div class="card c"><div class="big"><b>[y]</b> u</div><p class="big" style="margin:1mm 0 0">le m<b>u</b>scle · le s<b>u</b>cre · le t<b>u</b>be · les n<b>u</b>triments · il a p<b>u</b></p></div><div class="card c"><div class="big"><b>[u]</b> ou</div><p class="big" style="margin:1mm 0 0">la b<b>ou</b>che · le p<b>ou</b>mon · la t<b>ou</b>x · le c<b>ou</b>de · le p<b>ou</b>ls</p></div></div><p class="sm" style="margin:2mm 0 0">✏️ [y] : je dis [i] et j\'arrondis les lèvres en avant, la langue reste en avant. [u] : les lèvres sont arrondies et la langue recule. ⚠️ Dans <b>le pouls</b>, on ne prononce ni le <b>l</b> ni le <b>s</b> : [pu].</p>', ["ecoute", "repete"], 1, "A",
          script="Lire chaque mot deux fois ; faire sentir la position de la langue.", sol="Activité orale.")
    e2 = E("J'écoute : [y] ou [u] ? Je coche.", checks(8, ["[y]", "[u]"]), ["ecoute", "coche"], 2, "A", script="1. tousser 2. le jus 3. la roue 4. la rue 5. dessous 6. dessus 7. une moule 8. une mule",
           sol="[y] : 2, 4, 6, 8 · [u] : 1, 3, 5, 7")
    e3 = E("Un os, des os ; un œuf, des œufs. J'écoute et je répète : la prononciation change au pluriel !", '<div class="card big c" style="line-height:1.9">un <b>os</b> [ɔs] → des <b>os</b> [o] · un <b>œuf</b> [œf] → des <b>œufs</b> [ø] · un <b>bœuf</b> [bœf] → des <b>bœufs</b> [bø]<br>le <b>cœur</b> [kœʁ] · la <b>sœur</b> · la <b>peur</b> ≠ <b>deux</b> [dø] · <b>nerveux</b> · <b>heureux</b></div>', ["ecoute", "repete"], 1, "A",
           script="Lire chaque paire en exagérant la différence [œ] ouvert / [ø] fermé.", sol="Activité orale.")
    e4 = E("Dictée : j'écoute deux fois et j'écris.", lines(3), ["ecoute", "ecris"], 2, "A",
           script="« Pendant l'effort, le cœur bat plus vite afin que les muscles reçoivent davantage d'oxygène. C'est pourquoi on est essoufflé. »",
           sol="Pendant l'effort, le cœur bat plus vite afin que les muscles reçoivent davantage d'oxygène. C'est pourquoi on est essoufflé.")
    b.page(f'<h2>J\'écoute bien · [y] / [u] · [œ] / [ø]</h2>{e}{e2}{e3}{e4}', "Sons")
    e = E("Les liaisons du corps humain. Je marque les liaisons (‿) puis je lis.", '<div class="card big" style="line-height:2">1. les‿os · les‿yeux · les‿oreilles 2. un‿organe · un‿estomac 3. les‿intestins · les‿artères 4. Ils‿ont mal. 5. C\'est‿un‿effort. 6. deux‿heures de sport</div>', ["lis", "repete"], 1, "A",
          sol="Liaisons en [z] : les‿os, les‿yeux, les‿oreilles, les‿intestins, les‿artères, ils‿ont, deux‿heures · en [n] : un‿organe, un‿estomac, un‿effort · en [t] : c'est‿un")
    e2 = E("Parler pour expliquer. J'écoute la prof, puis je lis le début de capsule en marquant les pauses (|) et en insistant sur les mots en gras.", '<div class="card big" style="line-height:1.9;background:#fff">Vous êtes-vous déjà demandé | <b>pourquoi</b> on bâille ? ↗ | <b>D\'abord</b>, | on bâille quand on est <b>fatigué</b>. | <b>Ensuite</b>, | on bâille aussi quand on <b>s\'ennuie</b>… | et même quand <b>quelqu\'un d\'autre</b> bâille ! ↘</div>', ["ecoute", "repete"], 2, "A",
           script="Voix claire et lente ; montée sur la question ; pause après chaque connecteur.", sol="Activité orale ; l'élève respecte les pauses et l'intonation.")
    e3 = E("J'écoute la capsule de Daria « Pourquoi faut-il se laver les mains ? ». Je note les étapes de son explication.", tall(compact(table(["La question", "Étape 1", "Étape 2", "Le conseil final"], [["", "", "", ""]], ["44mm", "46mm", "46mm", "46mm"])), 15), ["ecoute", "ecris"], 2, "A",
           script="« Pourquoi faut-il se laver les mains ? D'abord, nos mains touchent tout : poignées, GSM, argent… Elles transportent donc des microbes. Ensuite, quand on se touche le visage, ces microbes entrent dans le corps et peuvent nous rendre malades. Lavez-vous les mains au savon, au moins trente secondes, pour éliminer les microbes ! »",
           sol="Question : pourquoi se laver les mains ? · Étape 1 : les mains touchent tout, elles transportent des microbes · Étape 2 : en touchant le visage, les microbes entrent dans le corps et rendent malade · Conseil : se laver les mains au savon au moins trente secondes")
    e4 = E("Je lis vite et bien.", '<div class="card big c" style="line-height:1.8">Le pouls du loup roux tout doux bat sous sa joue.<br>Su-su-sucre sur la pu-pu-purée : du sucre, j\'en ai su trop !</div>', ["lis", "repete"], 2, "A", sol="Activité orale (virelangues écrits pour la classe).")
    b.page(f'<h2>J\'écoute bien · expliquer à l\'oral</h2>{e}{e2}{e3}{e4}', "Sons")

    # ---------- Révision spirale ----------
    e = E("🔁 V3 · Module 11 · Le subjonctif. Je complète : Il faut que tu (boire) ______________ de l'eau et que tu (faire) ______________ du sport.", "", ["complete"], 1, "C", sol="boives · fasses")
    e2 = E("🔁 V3 · Module 12 · Le conditionnel. À ta place, je (aller) ______________ chez le médecin et je (prendre) ______________ du repos.", "", ["complete"], 1, "C", sol="irais · prendrais")
    e3 = E("🔁 V3 · Module 3 · Le présent de vérité générale. Je conjugue : Le sang (circuler) ______________ dans les veines. Les poumons (contenir) ______________ des alvéoles.", "", ["complete"], 1, "C", sol="circule · contiennent")
    e4 = E("🔁 V3 · Module 8 · Le passif. « Le cœur pompe le sang. » → Le sang ______________________________ .", "", ["ecris"], 2, "C", sol="Le sang est pompé par le cœur.")
    e5 = E("🔁 V3 · Module 7 · Donner son avis. Faut-il interdire les distributeurs de sodas à l'école ? Mon avis en 2 phrases, avec un argument.", lines(2), ["ecris"], 2, "C", sol="Ex. : Je pense qu'il faudrait les remplacer par des fontaines à eau. En effet, une canette contient environ sept morceaux de sucre.")
    e6 = E("🔁 V3 · Module 5 · Lire un graphique. Sur un graphique en barres, que représente la longueur de chaque barre ?", '<p>' + blank("xl") + '</p>', ["ecris"], 1, "C", sol="La valeur (la quantité, le pourcentage) de chaque catégorie : plus la barre est longue, plus la valeur est grande.")
    e7 = E("🔁 V2 · Module 5 · La santé. Je complète le dialogue : — Qu'est-ce qui ne va pas ? — J'ai ______________ à la tête et j'ai de la ______________ (38,5 °C).", "", ["complete"], 1, "C", sol="mal · fièvre")
    e8 = E("🔁 V3 · Module 10 · Les figures de style. « Le cœur est le moteur du corps. » C'est une ______________ . « Il a un appétit d'ogre. » C'est une ______________ .", "", ["complete"], 2, "C", sol="métaphore · hyperbole (exagération ; accepter « comparaison implicite »)")
    b.page(f'<h2>🔁 Je révise les modules précédents</h2>{e}{e2}{e3}{e4}{e5}{e6}{e7}{e8}', "Je révise")

    # ---------- Ateliers ----------
    qs = [("🥱", "Pourquoi bâille-t-on ?"), ("🤧", "Pourquoi éternue-t-on ?"), ("🍽️", "Pourquoi a-t-on faim ?"), ("🌡️", "Pourquoi a-t-on de la fièvre ?"), ("🦷", "Comment se forme une carie ?"), ("🩸", "Pourquoi le sang est-il rouge ?")]
    e = E("Les experts (groupes de 3) : nous tirons une carte « question ». Nous cherchons la réponse (manuel, documentaire, site fiable avec la prof), puis nous l'expliquons oralement à la classe en 1 minute.", '<div class="grid3" style="gap:1.5mm">' + "".join(f'<div class="card c sm" style="border:1.5px dashed {MC};padding:2mm 1mm"><span style="font-size:15pt">{ic}</span><br>{t}</div>' for ic, t in qs) + '</div>' +
          compact(table(["Notre explication", ""], [["La question", ""], ["La réponse en une phrase (avec parce que / car)", ""], ["Deux étapes (d'abord, ensuite)", ""], ["Un mot scientifique et sa définition (c'est-à-dire)", ""]], ["80mm", "102mm"])).replace("<td></td>", '<td style="height:9mm"></td>'), ["parle", "groupe", "ecris"], 2, "A",
          script="Préparer des documents simples ; pour chaque groupe, vérifier les sources avant l'oral.",
          sol="Ex. (éternuement) : On éternue parce que le nez veut expulser une poussière ou un microbe. D'abord, l'intérieur du nez est irrité ; ensuite, le cerveau déclenche une expulsion d'air très rapide. Le réflexe, c'est-à-dire une réaction automatique du corps, protège nos voies respiratoires.")
    e2 = E("Pendant les explications des autres groupes, je note une chose que j'ai apprise et une question que je me pose encore.", lines(2), ["ecoute", "ecris"], 1, "A",
           sol="Ex. : J'ai appris que la fièvre aide le corps à combattre les microbes. Je me demande pourquoi on frissonne quand on a de la fièvre.")
    b.page(f'{atl_head("A", "Atelier · Les experts du corps")}{e}{e2}', "Atelier")
    art = '<div class="card" style="background:#fff;font-size:9.6pt;line-height:1.45"><b style="color:' + MC + '">Pourquoi les ados ont-ils du mal à se lever le matin ?</b> <span class="xs muted">(texte écrit pour le cahier)</span><p style="margin:1mm 0 0">Beaucoup de parents pensent que leurs ados sont paresseux. Pourtant, la science donne une autre explication. À l\'adolescence, l\'horloge biologique se décale : la <b>mélatonine</b>, c\'est-à-dire l\'hormone qui prépare au sommeil, est produite plus tard le soir. Les jeunes ont donc naturellement sommeil plus tard. Comme ils doivent se lever tôt pour aller à l\'école, ils dorment souvent moins que les 8 à 10 heures nécessaires. De plus, la lumière des écrans le soir peut retarder encore l\'endormissement. Résultat : une fatigue qui s\'accumule pendant la semaine, et des grasses matinées le week-end pour « rattraper ».</p></div>'
    e = E("Je lis le texte explicatif et je réponds.", art + f'<p class="sm mt2">1. Quelle idée reçue le texte veut-il corriger ? {blank("xl")}</p><p class="sm">2. Qu\'est-ce que la mélatonine ? {blank("xl")}</p><p class="sm">3. Complète la chaîne : la mélatonine est produite plus tard → {blank("m")} → {blank("m")} → fatigue.</p><p class="sm">4. Relève un connecteur de cause, un de conséquence et un d\'addition. {blank("xl")}</p>', ["lis", "ecris"], 2, "B",
          sol="1. Que les ados sont paresseux. — 2. L'hormone qui prépare au sommeil. — 3. Les jeunes ont sommeil plus tard → ils dorment moins que nécessaire (car ils se lèvent tôt) → fatigue. — 4. Cause : comme ; conséquence : donc (résultat) ; addition : de plus.")
    e2 = E("Je fais un schéma « cause → conséquence » qui résume le texte (4 cases).", '<div class="flex" style="gap:2mm">' + "".join(f'<div class="card" style="flex:1;min-height:20mm;background:{TINT}"></div>' + ('<b style="align-self:center">➜</b>' if i < 3 else '') for i in range(4)) + '</div>', ["ecris", "dessine"], 2, "C",
           sol="Horloge biologique décalée (mélatonine plus tard) → sommeil plus tard → lever tôt pour l'école : manque de sommeil → fatigue (+ écrans qui retardent l'endormissement)")
    e3 = E("Je donne un titre à chaque phrase-clé du texte : idée reçue · explication scientifique · conséquence · solution des ados le week-end.", lines(2), ["lis", "ecris"], 3, "B",
           sol="Idée reçue : les ados sont paresseux · Explication : la mélatonine est produite plus tard · Conséquence : manque de sommeil et fatigue · Solution des ados : les grasses matinées du week-end.")
    b.page(f'{atl_head("B", "Atelier · Lire un texte explicatif")}{e}{e2}{e3}', "Atelier")
    e = E("J'écris un texte explicatif (12 à 15 lignes) qui répond à une de ces questions : Pourquoi faut-il manger le matin ? · Pourquoi transpire-t-on ? · Comment se forme un bleu ? · Pourquoi a-t-on besoin de dormir ?", '<div class="card sm" style="background:' + TINT + '">Mon plan : ① titre-question · ② introduction (le phénomène + la question) · ③ explication en étapes (d\'abord, ensuite, enfin) avec la cause et la conséquence · ④ conclusion et conseil (pour + infinitif). Je définis au moins un mot avec « c\'est-à-dire ».</div>' + lines(14), ["ecris"], 3, "C",
          sol="Texte explicatif complet : titre-question, introduction, étapes avec connecteurs, au moins deux expressions de la cause / conséquence, une du but, une définition, présent de vérité générale, pas d'opinion.")
    e2 = E("Je relis mon texte avec la grille.", chk3(["Mon titre est une question (pourquoi ? comment ?).", "J'explique en étapes, avec des connecteurs.", "J'utilise la cause, la conséquence et le but.", "J'écris au présent de vérité générale, sans donner mon avis."]), ["lis", "coche"], 1, "C", sol="Grille complétée ; corriger avant de mettre au propre.")
    b.page(f'{atl_head("C", "Atelier · J\'écris un texte explicatif")}{e}{e2}', "Atelier")
    cases = ["Départ : tu te réveilles après 9 h de sommeil. Avance d'une case !", "Nomme trois organes du ventre.", "Tu as sauté le petit-déjeuner : recule de 2 cases.", "Complète : On transpire … (but) refroidir le corps.", "Explique avec « parce que » : pourquoi le cœur bat vite pendant le sport ?", "Tu bois de l'eau pendant le match : avance de 2 cases.",
             "Que veut dire « cardiologue » ?", "Cite deux gestes barrières.", "Tu joues sur ton GSM jusqu'à 1 h : passe un tour.", "Quel numéro appelle-t-on en cas d'urgence vitale ?", "Dans quel organe les nutriments passent-ils dans le sang ?", "Arrivée : tu es en pleine forme ! BRAVO !"]
    plateau = '<div class="grid4" style="gap:1.4mm">' + "".join(f'<div class="card sm" style="padding:2mm;min-height:22mm;background:{"#FFE8D6" if i == 11 else "#fff"}"><b style="color:{MC}">{i + 1}</b> {t}</div>' for i, t in enumerate(cases)) + '</div>'
    e = E("Le jeu « En pleine forme ! » (2 à 4 joueurs, un dé, un pion par joueur).", '<p class="sm" style="margin:0 0 1.5mm">On lance le dé et on avance. Sur une case « question », on répond : si la réponse est juste (les autres vérifient dans le cahier), on reste ; sinon, on recule d\'une case. Le premier qui arrive à la case 12 a gagné !</p>' + plateau, ["joue", "groupe"], 2, "D",
          sol="Réponses : 2. Ex. : l'estomac, le foie, l'intestin grêle, le gros intestin · 4. pour (afin de) · 5. parce que les muscles ont besoin de plus d'oxygène · 7. le médecin spécialiste du cœur · 8. Ex. : se laver les mains, tousser dans son coude · 10. le 112 · 11. l'intestin grêle.")
    e2 = E("Le jeu « Pourquoi ? Parce que ! » (en duo). L'un tire une carte « conséquence » (j'ai des courbatures, j'ai le hoquet, je suis essoufflé, j'ai une carie…), l'autre trouve la cause avec trois constructions différentes (parce que, être dû à, à cause de).", '<div class="card sm" style="background:#fff">Exemple : « Je suis essoufflé. » → « Tu es essoufflé parce que tu as couru. » · « Ton essoufflement est dû à l\'effort. » · « Tu es essoufflé à cause de la course. »</div>', ["joue", "parle", "duo"], 1, "D",
           sol="Jeu oral ; vérifier les constructions (dû à + nom, à cause du / de la).")
    e3 = E("Après le jeu : j'invente deux nouvelles cases (une question sur le corps, une situation de santé avec sa conséquence).", lines(2), ["ecris"], 2, "C",
           sol="Ex. : « Combien d'heures un ado doit-il dormir ? » (8 à 10 h) · « Tu as oublié ta gourde : recule d'une case. »")
    b.page(f'{atl_head("D", "Atelier · En pleine forme !")}{e}{e2}{e3}', "Atelier")

    # ---------- ★ Coup de pouce ----------
    e = E("Je relie la partie du corps et le dessin.", relie(["le cœur", "les poumons", "le cerveau", "les dents", "le ventre"], ["🧠", "🫁", "🦷", "❤️", "🫃"]), ["relie"], 1, "B", alpha=True, sol="cœur → ❤️ · poumons → 🫁 · cerveau → 🧠 · dents → 🦷 · ventre → 🫃")
    e2 = E("Je complète avec : respirer · manger · dormir · bouger.", '<p class="big" style="line-height:2.1">1. Avec les poumons, je peux ______________ .<br>2. La nuit, je dois ______________ 9 heures.<br>3. Le matin, je dois ______________ un petit-déjeuner.<br>4. Le sport m\'aide à ______________ .</p>', ["complete"], 1, "C", alpha=True, sol="1. respirer — 2. dormir — 3. manger — 4. bouger")
    e3 = E("Bon ou pas bon pour la santé ? J'entoure 👍 ou 👎.", '<div class="card big" style="line-height:2">boire de l\'eau 👍 👎 · fumer 👍 👎 · se laver les mains 👍 👎 · dormir 4 heures 👍 👎</div>', ["entoure"], 1, "C", alpha=True, sol="👍 · 👎 · 👍 · 👎")
    b.page(CP.format(t="Mon corps") + e + e2 + e3, "★ Coup de pouce")
    e = E("Je lis le modèle. Je complète avec parce que ou c'est pourquoi.", '<div class="card" style="background:#F2F6FD"><p class="big" style="margin:0">Modèle : J\'ai froid <b>parce que</b> la fenêtre est ouverte. · La fenêtre est ouverte, <b>c\'est pourquoi</b> j\'ai froid.</p></div><p class="big" style="line-height:2.1;margin:2mm 0 0">1. Je suis fatigué ______________ j\'ai mal dormi.<br>2. J\'ai mal dormi, ______________ je suis fatigué.<br>3. J\'ai soif ______________ j\'ai couru.<br>4. J\'ai couru, ______________ j\'ai soif.</p>', ["lis", "complete"], 1, "C", alpha=True, sol="1. parce que — 2. c'est pourquoi — 3. parce que — 4. c'est pourquoi")
    e2 = E("Je relie la question et la réponse.", relie(["Pourquoi tu bois ?", "Pourquoi tu dors ?", "Pourquoi tu manges ?"], ["Parce que j'ai faim.", "Parce que j'ai soif.", "Parce que je suis fatigué."]), ["relie"], 1, "B", alpha=True, sol="bois → soif · dors → fatigué · manges → faim")
    e3 = E("Je recopie la phrase.", '<div class="card" style="background:#F2F6FD"><p class="big" style="margin:0">Je me lave les mains pour éliminer les microbes.</p></div>' + lines(2), ["recopie"], 1, "C", alpha=True, sol="Copie lisible et exacte.")
    e4 = E("J'entoure la cause (pourquoi ?).", '<p class="big" style="line-height:2.1">1. J\'ai froid parce que <b>je n\'ai pas de pull</b> / <b>je mets un pull</b>.<br>2. Il tousse parce qu\'il est <b>malade</b> / <b>content</b>.<br>3. Elle a faim parce qu\'elle n\'a pas <b>mangé</b> / <b>dormi</b>.</p>', ["lis", "entoure"], 1, "C", alpha=True, sol="1. je n'ai pas de pull — 2. malade — 3. mangé")
    b.page(CP.format(t="Pourquoi ? Parce que…") + e + e2 + e3 + e4, "★ Coup de pouce")
    e = E("Je complète avec pour : je fais… pour…", '<p class="big" style="line-height:2.1">1. Je mange des fruits pour ______________ (être en forme).<br>2. Je bois de l\'eau pour ______________ (ne pas avoir soif).<br>3. Je fais du sport pour ______________ (avoir un cœur solide).</p>', ["complete"], 1, "C", alpha=True, sol="1. être en forme — 2. ne pas avoir soif — 3. avoir un cœur solide")
    e2 = E("Ma mini-capsule. Je complète, puis je la dis à la prof.", '<p class="big" style="line-height:2.1">Pourquoi faut-il dormir ? Il faut dormir parce que ______________ . Si on ne dort pas assez, on est ______________ . Alors, il faut dormir ______________ heures !</p>', ["complete", "parle"], 1, "A", alpha=True, sol="Ex. : … le corps se repose / … fatigué / … 8 à 10 heures.")
    e3 = E("Je lis l'affiche et j'entoure le bon numéro : urgence vitale ?", '<div class="card big c" style="line-height:2">🚑 &nbsp; 112 &nbsp; · &nbsp; 070 245 245 &nbsp; · &nbsp; 1733</div>', ["lis", "entoure"], 1, "C", alpha=True, sol="112")
    e4 = E("Je relie l'action et son but.", relie(["Je me brosse les dents", "Je mets un bonnet", "Je bois de l'eau"], ["pour ne pas avoir froid.", "pour ne pas avoir de caries.", "pour ne pas avoir soif."]), ["relie"], 1, "B", alpha=True, sol="dents → caries · bonnet → froid · eau → soif")
    b.page(CP.format(t="Pour… et ma mini-capsule") + e + e2 + e3 + e4, "★ Coup de pouce")

    # ---------- Tâche finale ----------
    e = E("Nous choisissons une question et nous préparons notre capsule (2 minutes, en groupe de 3).", tall(compact(table(["Notre capsule", "Ce que nous écrivons / préparons", "✅"], [["La question (pourquoi ? comment ?)", "", '<span class="chk"></span>'], ["Nos sources (manuel, documentaire, site d'un organisme de santé)", "", '<span class="chk"></span>'], ["Les étapes de l'explication (3 ou 4)", "", '<span class="chk"></span>'], ["Un schéma ou un dessin à montrer", "", '<span class="chk"></span>'], ["Un conseil de prévention (pour + infinitif)", "", '<span class="chk"></span>'], ["Qui dit quoi ? (rôles dans le groupe)", "", '<span class="chk"></span>']], ["62mm", "104mm", "16mm"])), 22), ["lis", "ecris"], 2, "C",
          sol="Fiche complète : question précise, sources fiables, étapes, schéma, conseil, répartition des rôles.")
    b.page(tache_head("Ma capsule explicative", "Pour la semaine de la santé de l'Athénée, chaque groupe réalise une capsule de 2 minutes (vidéo ou exposé filmé, avec un schéma) qui explique un phénomène du corps humain et donne un conseil de prévention. Les capsules sont présentées aux autres classes.") + e, "Tâche finale", levels=False)
    e = E("J'écris le script de notre capsule (brouillon) : introduction avec la question, explication en étapes, conclusion et conseil.", lines(15), ["ecris"], 3, "C",
          sol="Script complet : accroche (question), étapes avec connecteurs, cause / conséquence / but, une définition, présent de vérité générale, conclusion avec un conseil ; environ 250 mots pour 2 minutes.")
    e2 = E("Je dessine le schéma que nous montrerons (avec un titre et des légendes).", '<div style="height:48mm;border:1.5px dashed #9aa1b1;border-radius:3mm;background:#fff"></div>', ["dessine"], 2, "C",
           sol="Schéma titré, légendé, lisible de loin, avec des flèches pour les étapes.")
    b.page(e + e2, "Tâche finale", levels=False)
    e = E("Le jour de la présentation : j'évalue la capsule d'un autre groupe.", chk3(["La question est claire dès le début.", "L'explication suit des étapes logiques.", "Le vocabulaire scientifique est expliqué.", "Le schéma aide à comprendre.", "Le conseil final est utile."]) + f'<p class="sm mt2">Ce que j\'ai appris grâce à cette capsule : {blank("xl")}</p>', ["ecoute", "coche"], 1, "A",
          sol="Grille remplie ; une information nouvelle formulée en phrase complète.")
    e2 = E("Après la présentation : je m'auto-évalue et j'écris ce que nous ferions mieux la prochaine fois (au conditionnel).", chk3(["J'ai participé à la recherche et à l'écriture.", "J'ai parlé clairement, en regardant le public.", "J'ai utilisé la cause, la conséquence et le but."]) + lines(2), ["ecris", "coche"], 1, "C",
           sol="Auto-évaluation ; objectif au conditionnel (ex. : La prochaine fois, nous parlerions plus lentement et nous ferions un schéma plus grand.).")
    b.page(compact(table(["Je vérifie avant de filmer :", "✅"], [[x, '<span class="chk"></span>'] for x in ["Notre capsule dure environ 2 minutes.", "Nos informations viennent de sources fiables.", "Chaque membre du groupe parle.", "Nous expliquons au moins un mot scientifique.", "Nous terminons par un conseil de prévention."]], ["160mm", "22mm"])) + e + e2, "Tâche finale", levels=False)
    e = E("Je révise.", '<p>1. L\'organe qui pompe le sang : le ______________ . 2. Les nutriments passent dans le sang au niveau de l\'______________ . 3. Quand on inspire, on fait entrer de l\'______________ . 4. « Faute de sommeil » exprime la ______________ . 5. Après « pour que », le verbe est au ______________ . 6. Un texte qui répond à « pourquoi ? » est un texte ______________ . 7. En cas d\'urgence vitale, j\'appelle le ______________ .</p>', ["complete"], 1, "C",
          sol="1. cœur — 2. intestin grêle — 3. oxygène (air) — 4. cause — 5. subjonctif — 6. explicatif — 7. 112")
    e2 = E("Je corrige le texte explicatif de Mateo : 5 erreurs (opinion, but, cause, temps, connecteur).", '<div class="card" style="font-family:\'Comic Sans MS\',cursive;background:#fff;font-size:10.3pt">« Pourquoi transpire-t-on ? Je trouve que la transpiration, c\'est dégoûtant. Le corps transpirait pour que la température baisser. On transpire grâce à la chaleur. Ensuite, la sueur s\'évapore. D\'abord, la peau refroidit. »</div>' + lines(4), ["lis", "ecris"], 2, "C",
           sol="Supprimer l'opinion « Je trouve que… c'est dégoûtant » · présent de vérité générale : « Le corps transpire » · but : « pour que la température baisse » (subjonctif, pas l'infinitif) · cause : « à cause de la chaleur » ou « sous l'effet de la chaleur » (pas « grâce à ») · connecteurs : « D'abord, la sueur s'évapore. Ensuite, la peau refroidit. »")
    e3 = E("Défi ! Je complète la carte mentale du module : un mot ou un exemple par branche.", tall(compact(table(["Branche", "Mes mots / mes exemples"], [["les organes et leurs fonctions", ""], ["digestion, respiration, circulation", ""], ["la cause et la conséquence", ""], ["le but (pour, afin que + subjonctif)", ""], ["l'infographie", ""], ["le texte explicatif et la prévention", ""]], ["66mm", "116mm"])), 11), ["lis", "ecris"], 3, "C",
           sol="Productions variées ; vérifier un exemple juste par branche (ex. : but : je bois pour être hydraté ; afin que les muscles reçoivent de l'oxygène).")
    b.page(f'<h2>🔁 Je révise tout le module</h2>{e}{e2}{e3}', "Je révise")

    # ---------- Test ----------
    Q = [("L'organe qui pompe le sang est…", ["le cœur", "le foie", "l'estomac", "le cerveau"]), ("Les nutriments passent dans le sang au niveau…", ["de l'intestin grêle", "de l'œsophage", "de la bouche", "des poumons"]),
         ("Quand on expire, on rejette…", ["du dioxyde de carbone", "de l'oxygène", "des nutriments", "du sang"]), ("Les vaisseaux qui partent du cœur sont…", ["les artères", "les veines", "les nerfs", "les muscles"]),
         ("Un « cardiologue » soigne…", ["le cœur", "la peau", "les dents", "les poumons"]), ("La fièvre est…", ["un symptôme", "un vaccin", "un organe", "un traitement"]),
         ("« … tu tousses, mets la main devant la bouche. » (cause connue)", ["Puisque", "Donc", "Pour que", "Si bien que"]), ("« Faute de sommeil » exprime…", ["la cause", "le but", "la conséquence", "l'opposition"]),
         ("Il a couru, … il est essoufflé.", ["si bien qu'", "afin qu'", "puisqu'", "pour qu'"]), ("Son malaise est … au manque de sucre.", ["dû", "grâce", "cause", "pour"]),
         ("Je me lave les mains … éliminer les microbes.", ["pour", "pour que", "parce que", "si bien que"]), ("Le cœur bat vite pour que les muscles … plus d'oxygène.", ["reçoivent", "reçoivent-ils", "recevront", "recevoir"]),
         ("Les poumons … respirer.", ["servent à", "sont dus à", "à cause de", "puisque"]), ("Un texte explicatif répond surtout à la question…", ["pourquoi ? / comment ?", "qu'en penses-tu ?", "qui a gagné ?", "quand partons-nous ?"]),
         ("Dans un texte explicatif, on utilise surtout…", ["le présent de vérité générale", "le passé simple", "le futur", "l'impératif"]), ("« c'est-à-dire » sert à…", ["définir ou reformuler", "donner son avis", "exprimer le but", "raconter"]),
         ("Dans une infographie, la « source » indique…", ["qui a produit les informations", "le titre", "la couleur", "la date de naissance"]), ("En cas d'urgence vitale en Belgique, on appelle le…", ["112", "1733", "070 245 245", "100 100"]),
         ("Le mot « muscle » contient le son…", ["[y]", "[u]", "[o]", "[i]"]), ("🔁 Subjonctif : « Il faut que tu … de l'eau. »", ["boives", "bois", "boiras", "boire"])]
    ans = [q[1][0] for q in Q]
    qrot = [1, 3, 0, 2, 2, 1, 3, 0, 1, 2, 3, 0, 2, 1, 0, 3, 1, 2, 3, 0]
    Q = [(q, o[r:] + o[:r]) for (q, o), r in zip(Q, qrot)]
    key = key_from(Q, ans)
    test_pages(b, 13, "Corps et santé", Q, f'<h3>B1. Relie les deux phrases de trois façons : « Il n\'a pas déjeuné. Il a eu un malaise. » (… / 3)</h3><p>avec parce que : {blank("xl")}</p><p>avec c\'est pourquoi : {blank("xl")}</p><p>avec être dû à : {blank("xl")}</p><h3>B2. Complète : Je dors tôt pour (être) ______ en forme. Le médecin parle lentement pour que le patient (comprendre) ______ . (… / 2)</h3><h3>B3. Écris un court texte explicatif (6 lignes) : « Pourquoi faut-il boire de l\'eau ? » (introduction, deux étapes avec connecteurs, une cause ou une conséquence, un conseil). (… / 5)</h3>{lines(6, True)}',
               [["nommer quatre organes et dire leur rôle", "/ 3", ""], ["expliquer oralement un phénomène (digestion ou circulation) en étapes", "/ 4", ""], ["donner deux conseils de santé avec « pour » ou « afin de »", "/ 3", ""]],
               '<h3>1. Je relie la partie du corps et le dessin. (… / 4)</h3>' + relie(["le cœur", "le cerveau", "les poumons", "les dents"], ["🫁", "🦷", "❤️", "🧠"]) + '<h3>2. J\'entoure ce qui est bon pour la santé. (… / 4)</h3><div class="card big">dormir 9 heures · fumer · boire de l\'eau · se laver les mains · sauter le repas</div><h3>3. Je complète avec parce que ou c\'est pourquoi : J\'ai soif ______ j\'ai couru. J\'ai mal dormi, ______ je suis fatigué. (… / 4)</h3><h3>4. Je complète : Je me lave les mains ______ éliminer les microbes. Urgence : j\'appelle le ______ . (… / 3)</h3><h3>5. Oral : je dis deux conseils pour être en forme. (… / 5)</h3>')
    closing(b, 13, ["Je nomme les principaux organes et leur fonction.", "J'explique le trajet des aliments (la digestion).", "J'explique la respiration et la circulation du sang.", "J'exprime la cause avec des outils variés (puisque, faute de, être dû à…).", "J'exprime la conséquence (si bien que, tellement… que, d'où…).", "J'exprime le but (pour, afin de + infinitif ; pour que + subjonctif).",
                    "Je lis une infographie et un graphique.", "Je lis une étiquette alimentaire.", "J'écris un texte explicatif en étapes.", "Je sais qui appeler en cas de problème de santé.", "Je présente une capsule explicative."],
            [("🫀", "un organe"), ("⚙️", "une fonction"), ("❤️", "le cœur, le pouls"), ("🩸", "le sang, une artère, une veine"), ("🫁", "les poumons, respirer"), ("🌬️", "l'oxygène"), ("🍽️", "la digestion, digérer"), ("🥗", "les nutriments"), ("🫙", "l'estomac"), ("〰️", "l'intestin"), ("🦴", "le squelette, un os"), ("💪", "un muscle"),
             ("🦠", "un microbe, un virus"), ("🤒", "un symptôme, la fièvre"), ("💉", "un vaccin"), ("🧼", "l'hygiène"), ("🛡️", "la prévention"), ("😴", "le sommeil"), ("🏃", "l'activité physique"), ("📊", "une infographie"), ("🔍", "la cause, être dû à"), ("➡️", "la conséquence"), ("🎯", "le but, afin de"), ("🎬", "une capsule explicative")])
    plan_de_travail(b, E, 13, ["Digérer, respirer, circuler", "La cause et la conséquence", "Le but", "Lire une infographie", "Le texte explicatif"], "☐ Question et sources<br>☐ Script<br>☐ Schéma<br>☐ Présentation")
    b.pages = [x.replace("padding:.8mm 1.5mm;display:flex", "padding:.3mm 1.5mm;display:flex").replace("repeat(7,1fr);gap:1.3mm", "repeat(7,1fr);gap:.7mm").replace("align-items:center;justify-content:space-between;font-size:8.5pt", "align-items:center;justify-content:space-between;font-size:8pt") for x in b.pages]  # plan compact
    if render:
        to_pdf(b.html(), '/home/claude/syllabus/out/V3_M13_eleve.pdf')

    pg, exs = helpers(b, E)
    CPp = b.marks["★ Coup de pouce"]
    days = [("1", "Collectif", f"Ouverture · BD · le corps humain ({pg('Découvrir')})", f"CP mon corps (p. {CPp[0]})"), ("2", "Collectif + duo", f"Lexique : corps, santé, médecins ({pg('Lexique')})", "CP mon corps"),
            ("3", "Rotation", f"📌 Leçon 1 digestion, respiration, circulation ({pg('Leçon 1')}) · prise du pouls", "Schéma colorié du trajet des aliments"), ("4", "Collectif", f"📌 Leçon 2 cause et conséquence ({pg('Leçon 2')}) · sons ({pg('Sons')})", f"CP parce que (p. {CPp[1]})"),
            ("5", "Rotation", f"📌 Leçon 3 le but ({pg('Leçon 3')})", f"CP pour… (p. {CPp[2]})"), ("6", "Collectif", f"📌 Leçon 4 infographie ({pg('Consignes & école')}) · étiquette ({pg('Document de la vie')})", "Lecture guidée de l'infographie"),
            ("7", "Rotation", f"📌 Leçon 5 texte explicatif ({pg('Leçon 5')}) · urgences", "Texte à trous avec connecteurs"), ("8", "Ateliers", f"Ateliers ({pg('Atelier')}) · CE1D, DELF ({pg('Vers les épreuves')})", "CP mini-capsule"),
            ("9", "Groupes", f"Tâche finale : capsules explicatives ({pg('Tâche finale')})", "Rôle de dessinateur du schéma"), ("10", "Seul", f"Test ({pg('Test')})", f"CP test ({pg('★ Coup de pouce · Test')})")]
    rot = [["🎧 Écouter-Parler", "Les experts du corps (cartes « question »)", "30 min", "Prise de notes croisée"], ["📖 Lire", "Pourquoi les ados ont-ils du mal à se lever ?", "20 min", "Oui"], ["✏️ Écrire", "Mon texte explicatif", "30 min", "Grille de relecture"],
           ["🧩 Jouer", "« En pleine forme ! » + « Pourquoi ? Parce que ! »", "20 min", "Les joueurs vérifient"], ["👩‍🏫 Table d'appui", "Coup de pouce · corps, parce que, pour", "20 min", "—"]]
    ev1 = f'''<h3>Partie B (10 points)</h3><p class="sm"><b>B1</b> : <span class="sol">Il a eu un malaise parce qu'il n'avait pas déjeuné. · Il n'a pas déjeuné, c'est pourquoi il a eu un malaise. · Son malaise est dû à l'absence de petit-déjeuner (au manque de nourriture).</span> (1 pt chacune). · <b>B2</b> : <span class="sol">être · comprenne</span> (1 pt chacun). · <b>B3</b> : introduction et étapes (2), cause ou conséquence (1), conseil avec but (1), langue (1).</p>
<h3>Partie C · oral (10 points)</h3><p class="sm">L'élève nomme quatre organes et leur rôle (3) · il explique en étapes la digestion ou la circulation, avec des connecteurs (4) · il donne deux conseils de santé avec « pour » ou « afin de » (3).</p>
<h3>Test ★ Coup de pouce (20 points)</h3><p class="sm"><b>1 :</b> <span class="sol">cœur → ❤️ · cerveau → 🧠 · poumons → 🫁 · dents → 🦷</span> (4) · <b>2 :</b> <span class="sol">dormir 9 heures · boire de l'eau · se laver les mains</span> (4) · <b>3 :</b> <span class="sol">parce que · c'est pourquoi</span> (4) · <b>4 :</b> <span class="sol">pour · 112</span> (3) · <b>5 :</b> deux conseils compréhensibles (5).</p>
<h3>Lire les résultats du QCM : quelle remédiation ?</h3>{table(["Questions", "Compétence", "Si moins de la moitié est juste…"], [["1 à 6", "le corps, les fonctions, le lexique médical", f"leçon 1 ({pg('Leçon 1')}) + lexique ({pg('Lexique')}) + coup de pouce p. {CPp[0]}"], ["7 à 10", "la cause et la conséquence", f"leçon 2 ({pg('Leçon 2')}) + coup de pouce p. {CPp[1]}"], ["11 à 13", "le but (infinitif, subjonctif, servir à)", f"leçon 3 ({pg('Leçon 3')}) + coup de pouce p. {CPp[2]}"], ["14 à 16", "le texte explicatif", f"leçon 5 ({pg('Leçon 5')})"], ["17 et 18", "infographie, urgences", f"leçon 4 ({pg('Consignes & école')}) + documents ({pg('Document de la vie')})"], ["19", "[y] / [u]", f"sons ({pg('Sons')})"], ["20", "révision (subjonctif)", "module 11"]], ["24mm", "62mm", "96mm"])}'''
    ev2 = f'''<h2>Grille · tâche finale « Ma capsule explicative »</h2>{table(["Critère", "Très bien", "Bien", "À retravailler", "Points"], [["<b>Contenu scientifique</b> juste, sources fiables", "Exact", "Quelques imprécisions", "Erroné", "/ 4"], ["<b>Structure</b> : question, étapes, conclusion et conseil", "Claire", "Partielle", "Confuse", "/ 4"], ["<b>Langue</b> : cause, conséquence, but, présent de vérité générale, définitions", "Maîtrisée", "Quelques erreurs", "Fragile", "/ 4"], ["<b>Oral</b> : voix, débit, regard, durée (2 min)", "Aisé", "Correct", "Difficile", "/ 4"], ["<b>Schéma</b> : titre, légendes, lisibilité", "Réussi", "Correct", "Absent", "/ 2"], ["<b>Travail de groupe</b> : chacun participe", "Équilibré", "Inégal", "Un seul travaille", "/ 2"]], ["66mm", "30mm", "30mm", "34mm", "22mm"])}
<h2 class="mt4">Différencier et remédier</h2>{table(["Difficulté", "Remédiation"], [["Vocabulaire du corps", "Silhouette affichée en classe, organes en carton aimantés à replacer ; mimer les fonctions ; imagier bilingue dans « Mes mots »."], ["Cause / conséquence", "Flèches de couleur au tableau (cause → conséquence) ; transformer une même idée avec trois outils ; dominos cause / conséquence."], ["But : infinitif ou subjonctif", "Rappel du module 11 : un sujet = pour + infinitif ; deux sujets = pour que + subjonctif ; tableau des subjonctifs irréguliers affiché."], ["Lire une infographie", "Lecture guidée en 5 étapes ; surligner chiffres et unités ; reformuler chaque chiffre en phrase complète."], ["Élève rapide", "Comparer deux infographies sur le même sujet ; écrire un article de vulgarisation pour le journal de l'école ; préparer la compréhension écrite du DELF B1."]], ["50mm", "132mm"])}'''
    rep = f'''<h2>Corps et santé : repères</h2>
<div class="attention"><b>Points d'attention.</b> Les questions de santé touchent à l'intime : ne jamais demander à un élève de parler de ses maladies, de son poids, de ses traitements ou de ceux de sa famille. Certains élèves ont vécu des situations de manque (nourriture, soins) ou des traumatismes : présenter l'alimentation et le sommeil sans jugement ni culpabilisation (pas de « bons » et de « mauvais » élèves). Respecter les pratiques alimentaires religieuses ou culturelles (jeûne, interdits). Pour toute inquiétude, s'adresser au service PSE ou au centre PMS de l'école.</div>
{table(["Repère", "Ce qu'il faut savoir (vérifié en novembre 2026)"], [["Le corps", "Digestion : bouche, œsophage, estomac, intestin grêle (environ 6 à 7 m ; absorption des nutriments), gros intestin (absorption de l'eau), anus. Respiration : échanges gazeux dans les alvéoles pulmonaires. Circulation : le cœur, une pompe musculaire (60 à 100 battements par minute au repos chez l'adulte) ; artères (du cœur vers les organes), veines (retour au cœur) ; environ 5 litres de sang chez l'adulte. Température du corps : environ 37 °C."], ["Recommandations", "Sommeil : 8 à 10 heures par nuit pour les 13-18 ans (recommandations des sociétés savantes de médecine du sommeil). Activité physique : au moins 60 minutes par jour en moyenne, d'intensité modérée à soutenue, pour les 5-17 ans (OMS). Sucres libres : moins de 10 % de l'apport énergétique, idéalement moins de 5 % (OMS). Boissons : environ 1,5 litre par jour (recommandation courante). Nutri-Score : adopté en Belgique en 2019 (logo facultatif)."], ["Numéros et services belges", "112 : urgence vitale (ambulance, pompiers), gratuit · Centre Antipoisons : 070 245 245, 24 h sur 24 · 1733 : médecin de garde (nuit, week-end, jours fériés) · le service PSE (Promotion de la santé à l'école) assure les bilans de santé et la prévention dans les écoles de la FWB · la mutuelle rembourse une partie des soins (assurance obligatoire)."]], ["40mm", "142mm"])}
<div class="attention mt2"><b>Fictif :</b> l'Athénée de Hautrive, son infirmerie et sa semaine de la santé, le service PSE de Hautrive et son infographie (les chiffres, eux, sont ceux des recommandations courantes), le sondage sur l'activité physique, la boisson « Fizz Orange » (valeurs proches des sodas réels), les capsules des élèves. Les numéros d'urgence, l'OMS, le Nutri-Score et les connaissances scientifiques sont réels.</div>
<h3>Belgicismes du module</h3><p class="sm">la <b>mutuelle</b> (en Belgique, l'organisme de l'assurance maladie obligatoire) · le <b>médecin généraliste</b> (France : médecin traitant) · une <b>maison médicale</b> · la <b>garde</b> · le <b>GSM</b> (France : portable) · <b>déjeuner</b> = prendre le repas du matin (France : petit-déjeuner ; en Belgique, le repas de midi est le <b>dîner</b> et celui du soir le <b>souper</b>) · une <b>interro</b>.</p>'''
    import re as _re
    def _court(t, n=90):
        t2 = _re.sub(r"<[^>]+>", "", t)
        return t if len(t2) <= n else t2[:n].rsplit(" ", 1)[0] + "…"
    E.sols = [(p, n, _court(t), s) for p, n, t, s in E.sols]
    E.scripts = [(p, n, _court(t, 50), s) for p, n, t, s in E.scripts]
    import lib.module as _LM
    _pg = _LM.paginate
    _LM.paginate = lambda rows, w, bf, bb: _pg(rows, w, bf + (SCR if bf == 190 else BUMP), bb + BUMP)
    _tb = _LM.table
    _LM.table = lambda *a, **k: compact(_tb(*a, **k))
    T = teacher_book(b, E, "V3 · M13", "", MC, 13, "Corps et santé",
                     "<li><b>Communication :</b> nommer les organes et leurs fonctions ; expliquer un phénomène du corps humain (oralement et par écrit) ; lire une infographie, un graphique et une étiquette alimentaire ; savoir qui appeler en cas de problème de santé.</li><li><b>Lexique :</b> le corps (organes, sang, os, muscles), les fonctions (digestion, respiration, circulation), la maladie (symptôme, microbe, infection), la prévention (hygiène, vaccin, sommeil, alimentation) ; préfixes et suffixes médicaux (cardio-, gastro-, -logue, -ite).</li><li><b>Langue :</b> la cause (puisque, faute de, être dû à, s'expliquer par), la conséquence (si bien que, tellement… que, d'où), le but (pour, afin de + infinitif ; pour que, afin que + subjonctif ; servir à) ; le texte explicatif (présent de vérité générale, connecteurs d'étapes, définitions).</li><li><b>Oral :</b> [y] / [u] ; [œ] / [ø] (un os / des os) ; liaisons ; expliquer à l'oral (pauses, intonation).</li><li><b>FLSco :</b> lire une infographie (5 étapes) ; consignes identifiez la source, relevez les données, interprétez, dégagez le message ; sciences (fonctions de nutrition).</li><li><b>Épreuves :</b> CE1D (article de vulgarisation : le hoquet) ; DELF B1 compréhension des écrits (l'eau).</li><li><b>Documents :</b> infographie sur le sommeil, sondage, étiquette de boisson avec Nutri-Score, affiche des numéros d'urgence.</li>",
                     '<p class="sm"><b style="color:#E4572E">Indispensable</b> : organes et fonctions, parce que / c\'est pourquoi, pour + infinitif, les numéros d\'urgence.</p><p class="sm"><b style="color:#d9a400">Important</b> : outils variés de la cause et de la conséquence, pour que + subjonctif, lire une infographie, structure du texte explicatif.</p><p class="sm"><b style="color:#2BA88F">Enrichissement</b> : vocabulaire médical savant, CE1D, DELF B1, capsule filmée.</p>',
                     "Un exemplaire du cahier par élève · une silhouette du corps humain (affiche ou torse anatomique de l'école) · chronomètre pour la prise du pouls · quelques emballages et étiquettes réels (boissons, céréales) · tablettes ou GSM de l'école pour filmer les capsules · dés et pions pour « En pleine forme ! » · cartes « question » découpées.", "<b>Avant de commencer :</b> se coordonner avec le professeur de sciences (le module peut accompagner son chapitre sur la nutrition) et, si possible, avec l'infirmière ou le service PSE (intervention, matériel de prévention). Prévoir où et comment les capsules seront présentées (semaine de la santé, valves, site de l'école) et demander les autorisations de filmer.",
                     days, "« L'organe du jour » : la prof montre un organe sur la silhouette, la classe dit son nom et sa fonction · « Pourquoi ? » : une question sur le corps au tableau, réponse en une phrase avec parce que · « Une idée, trois phrases » : transformer une cause avec trois outils.", rot, key, (ev1, ev2), extra_pages=[(rep, "Repères")], start=tstart)
    _LM.paginate = _pg
    _LM.table = _tb
    if render:
        to_pdf(T.html(), '/home/claude/syllabus/out/V3_M13_prof.pdf')
    return b, T


if __name__ == "__main__":
    b, T = build_v3m13()
    print(b.n, T.n)
