"""Volume 1 · Module 5 « Mon corps, ma santé »."""
import sys
sys.path.insert(0, '/home/claude/syllabus')
from lib.base import *
from lib.art import *
from lib.alpha import AL, letter_page, syll_table, slide
from lib.module import plan_de_travail, teacher_book, helpers
from lib.render import to_pdf

MC = "#D64545"
PARTS = [(1, "la tête", 100, 22), (2, "les cheveux", 100, 8), (3, "l'œil (les yeux)", 92, 22), (4, "l'oreille", 80, 26), (5, "le nez", 100, 28), (6, "la bouche", 100, 35),
         (7, "le cou", 100, 46), (8, "l'épaule", 76, 56), (9, "le bras", 66, 80), (10, "la main", 60, 108), (11, "le doigt", 56, 120), (12, "le ventre", 100, 92),
         (13, "le dos", 136, 76), (14, "la jambe", 88, 150), (15, "le genou", 88, 140), (16, "le pied", 86, 186)]


def body(width="78mm", labels=True):
    s = ['<svg viewBox="0 0 200 200" width="%s">' % width, '<g fill="#E0AC84" stroke="#1F2A44" stroke-width="1.2">',
         '<ellipse cx="100" cy="26" rx="17" ry="20"/><rect x="93" y="44" width="14" height="8"/>', '<path d="M72 54 Q100 48 128 54 L132 110 L68 110Z" fill="#4A7BD1"/>',
         '<path d="M72 56 L58 104 L64 106 L78 64Z" fill="#4A7BD1"/><path d="M128 56 L142 104 L136 106 L122 64Z" fill="#4A7BD1"/>', '<circle cx="60" cy="110" r="6"/><circle cx="140" cy="110" r="6"/>',
         '<path d="M70 110 L130 110 L126 182 L104 182 L100 128 L96 182 L74 182Z" fill="#2E4057"/>', '<ellipse cx="85" cy="187" rx="12" ry="5" fill="#1F2A44"/><ellipse cx="115" cy="187" rx="12" ry="5" fill="#1F2A44"/></g>',
         '<path d="M83 18 Q100 0 117 18 Q110 10 100 11 Q90 10 83 18Z" fill="#3B2516"/><circle cx="93" cy="24" r="2" fill="#222"/><circle cx="107" cy="24" r="2" fill="#222"/>',
         '<path d="M100 26 L98 31 L102 31" stroke="#1F2A44" fill="none" stroke-width="1"/><path d="M94 36 Q100 40 106 36" stroke="#7A2E2E" fill="none" stroke-width="1.4"/>',
         '<ellipse cx="83" cy="27" rx="3" ry="5" fill="#E0AC84" stroke="#1F2A44"/>']
    if labels:
        for n, w, x, y in PARTS:
            side = 1 if n in (4, 8, 9, 10, 11, 14, 15, 16, 3) else -1
            lx = 22 if side == 1 else 178
            s.append(f'<line x1="{x}" y1="{y}" x2="{lx + (6 if side==1 else -6)}" y2="{y}" stroke="#9aa1b1" stroke-width=".5" stroke-dasharray="1.5 1"/>'
                     f'<circle cx="{lx}" cy="{y}" r="5.5" fill="{MC}"/><text x="{lx}" y="{y+2.2}" font-size="6" fill="#fff" text-anchor="middle" font-family="Poppins" font-weight="700">{n}</text>')
    s.append('</svg>')
    return "".join(s)


def build_m5(start=1, tstart=1, render=True):
    b = Book("V1 · M5", "Volume 1 · Premiers pas · Module 5 · Mon corps, ma santé", MC, start=start)
    E = Ex(b)
    obj = [("🧍", "nommer les parties du corps"), ("🤒", "dire où j'ai mal et comment je me sens"), ("🩺", "parler avec le médecin, le pharmacien, l'infirmière"),
           ("🚑", "appeler les urgences (112)"), ("👉", "comprendre les ordres : Ouvre la bouche ! Respirez !"), ("⚠️", "comprendre une consigne de sécurité")]
    objs = "".join(f'<div class="flex mb2"><span class="emo s">{e}</span><span class="big">{t}</span></div>' for e, t in obj)
    b.page(f'''<div style="background:{MC};color:#fff;margin:-17mm -14mm 6mm -14mm;padding:16mm 14mm 6mm 14mm"><div style="font-size:13pt;font-weight:700;opacity:.9">MODULE 5</div><div style="font-size:44pt;font-weight:800;line-height:1">Mon corps, ma santé</div></div>
<div class="flex" style="justify-content:space-around;background:#FBEAEA;border-radius:4mm;padding:4mm">{body("58mm", False)}<div class="c" style="font-size:34pt;line-height:1.5">🤒 🤧 🩺<br>💊 🏥 🚑</div></div>
<div class="grid2 mt4"><div><h2>Je vais apprendre à…</h2>{objs}</div><div><div class="card" style="background:#FBEAEA;border-color:#F2C2C2"><h3 style="margin-top:0">🗣️ On parle ensemble</h3>
<p>Quand tu es malade, qu'est-ce que tu fais ?</p><p>Dans ton pays, on va chez le médecin ou à l'hôpital ?</p><p>Tu connais le numéro des urgences en Belgique ?</p></div>
<div class="card mt4"><h3 style="margin-top:0">🔑 Les mots-clés</h3>{"".join(f'<span class="pill">{w}</span>' for w in ["le corps", "j'ai mal", "la tête", "le ventre", "la fièvre", "le médecin", "la pharmacie", "les urgences", "le rendez-vous", "malade"])}</div></div></div>''', "Ouverture", levels=False)
    b.page("%%PLAN_DE_TRAVAIL%%", "Mon plan de travail", levels=False)

    def case(n, inner):
        return f'<div style="border:2.5px solid #1F2A44;border-radius:3mm;min-height:62mm;position:relative;padding:3mm;background:#FFFDF8"><div style="position:absolute;top:2mm;left:2mm;background:#1F2A44;color:#fff;width:6mm;height:6mm;border-radius:50%;font-size:9pt;font-weight:700;display:flex;align-items:center;justify-content:center">{n}</div>{inner}</div>'

    def bub(t):
        return f'<div class="bubble" style="margin:0 0 2mm 0;font-size:11pt">{t}</div>'

    def lr(a, ta, bb, tb, ma="sourire", mb="sourire"):
        return (f'<div class="flex top" style="margin-top:5mm">{avatar(a, 72, ma)}<div>{"".join(bub(x) for x in ta)}</div></div>'
                f'<div class="flex top" style="justify-content:flex-end">{"".join(bub(x) for x in tb)}{avatar(bb, 72, mb, flip=True)}</div>')
    doc = dict(skin="fonce", hair="#111", style="court", glasses=True, shirt="#fff")
    bd = '<div class="grid2" style="gap:3mm">' + "".join([
        case(1, lr("prof", ["Yonas, ça va ? Tu es tout pâle…"], "yonas", ["Non, Madame… J'ai mal à la tête et j'ai froid."], "pense", "triste")),
        case(2, lr("prof", ["Va à l'infirmerie avec Bilal, s'il te plaît."], "bilal", ["Viens, Yonas, je t'accompagne."], "sourire", "sourire")),
        case(3, f'<div class="flex top" style="margin-top:5mm">{face(size=72, skin="clair", hair="#B5651D", style="long", shirt="#fff")}<div>{bub("Bonjour Yonas. Qu&#39;est-ce qui ne va pas ?")}{bub("Ouvre la bouche… Tu as mal à la gorge ?")}</div></div><div class="c" style="font-size:24pt">🌡️</div>'),
        case(4, f'<div class="flex top" style="margin-top:5mm">{face(size=72, skin="clair", hair="#B5651D", style="long", shirt="#fff")}<div>{bub("Tu as 38,5 de fièvre. Tu es malade.")}{bub("Je téléphone à ton oncle.")}</div></div>'),
        case(5, f'<div class="flex top" style="margin-top:5mm">{face(size=72, **doc)}<div>{bub("Le lendemain, chez le médecin : Respire bien fort… Tousse !")}</div></div><div class="flex top" style="justify-content:flex-end">{bub("Kof ! Kof !")}{avatar("yonas", 66, "triste", flip=True)}</div>'),
        case(6, f'<div class="flex top" style="margin-top:5mm">{face(size=72, **doc)}<div>{bub("C&#39;est une grippe. Il faut rester au lit trois jours et boire beaucoup d&#39;eau.")}{bub("Voici l&#39;ordonnance pour la pharmacie.")}</div></div><div class="c" style="font-size:22pt">📄💊🛏️💧</div>'),
    ]) + '</div>'
    e = E("J'écoute et je regarde la BD : Yonas est malade.", bd, ["ecoute", "regarde"], 1, "A",
          script="Lire la BD deux fois en mimant (main sur le front, frissons, toux). Montrer les objets : thermomètre, ordonnance. Faire répéter « J'ai mal à la tête », « J'ai froid », « Ouvre la bouche ! ».", sol="Activité orale.")
    b.page(f'<h2>Découvrir · Yonas est malade</h2>{e}', "Découvrir")
    e = E("Je réponds.", f'''<p>1. Où Yonas a mal ? {blank("l")}</p><p>2. Qui accompagne Yonas à l'infirmerie ? {blank()}</p><p>3. Yonas a combien de fièvre ? {blank()}</p><p>4. Qu'est-ce qu'il a ? (la maladie) {blank()}</p><p>5. Qu'est-ce qu'il faut faire ? {blank("xl")}</p>''',
          ["lis", "ecris"], 1, "B", sol="1. à la tête (et à la gorge) — 2. Bilal — 3. 38,5 — 4. une grippe — 5. rester au lit trois jours et boire beaucoup d'eau")
    e2 = E("Je remets les étapes dans l'ordre (1 à 5).", '<div class="card">' + "".join(f'<p><span class="circ"></span>{t}</p>' for t in ["Le médecin donne une ordonnance.", "Yonas a mal à la tête en classe.", "L'infirmière prend la température.", "Yonas va à la pharmacie.", "Yonas va à l'infirmerie avec Bilal."]) + '</div>',
           ["lis", "numerote"], 2, "B", sol="Ordre affiché : 4 – 1 – 3 – 5 – 2")
    e3 = E("Défi ! Je joue la scène de l'infirmerie avec un camarade (je change le problème).", '', ["parle", "duo"], 3, "A", sol="Production orale.")
    b.page(f'{e}{e2}{e3}', "Découvrir")

    # Leçon 1 corps
    leg = "".join(f'<div class="flex" style="gap:1.5mm;margin-bottom:1mm"><span class="circ" style="background:{MC};color:#fff;border-color:{MC}">{n}</span><span class="sm">{w}</span></div>' for n, w, *_ in PARTS)
    l1 = lecon("Le corps", f'<div class="flex top">{body("100mm")}<div class="grid2 grow" style="gap:0 3mm">{leg}</div></div><p class="sm mt2">⚠️ Pluriels spéciaux : un œil → des <b>yeux</b> · un genou → des genou<b>x</b>. On dit <b>les</b> cheveux (pluriel).</p>')
    e = E("J'écoute et je montre la partie du corps (« Jacques a dit »).", '', ["ecoute", "montre"], 1, "P", script="« Jacques a dit : touchez votre tête ! … votre nez ! … votre genou ! » Puis chanson « Tête, épaules, genoux, pieds ». Un élève devient le meneur.", sol="Activité gestuelle.")
    b.page(f'{l1}{e}', "Leçon 1")
    e = E("J'écris le nom de la partie du corps.", '<div class="grid4">' + "".join(f'<div class="card c"><span class="emo">{em}</span><div class="line"></div></div>' for em in ["👃", "👂", "🦶", "✋", "🦷", "👁️", "🦵", "💪"]) + '</div>', ["regarde", "ecris"], 1, "C",
          sol="le nez · l'oreille · le pied · la main · la dent · l'œil · la jambe · le bras")
    e2 = E("Combien ? J'écris le nombre.", '<p>J\'ai ___ yeux, ___ oreilles, ___ nez, ___ mains, ___ doigts, ___ dents (environ !), ___ pieds.</p>', ["ecris"], 1, "C", sol="2 · 2 · 1 · 2 · 10 · 32 (adulte ; 28 à 32) · 2")
    e3 = E("Avec quoi ? Je relie.", relie(["je regarde", "j'écoute", "je mange", "je marche", "j'écris", "je sens une fleur"], ["avec les jambes", "avec la main", "avec le nez", "avec les yeux", "avec la bouche", "avec les oreilles"]), ["relie"], 2, "B",
           sol="regarde → yeux · écoute → oreilles · mange → bouche · marche → jambes · écris → main · sens → nez")
    e4 = E("Défi ! Je dessine un monstre (3 yeux, 4 bras…) et je le décris en 4 phrases. Mon camarade le dessine sans le voir !", '<div class="card" style="height:40mm"></div>' + lines(3), ["dessine", "ecris", "duo"], 3, "C", sol="Production libre : Il a trois yeux…")
    b.page(f'{e}{e2}{e3}{e4}', "S'entraîner")

    # Leçon 2 avoir mal
    l2 = lecon("J'ai mal… · Comment je me sens ?", f'''{table(["", "avoir mal…", "Exemple"], [["le ventre (masc.)", "<b>au</b> (à + le)", "J'ai mal <b>au</b> ventre. 🤢"], ["la tête (fém.)", "<b>à la</b>", "J'ai mal <b>à la</b> tête. 🤕"], ["l'oreille (voyelle)", "<b>à l'</b>", "J'ai mal <b>à l'</b>oreille."], ["les dents (pluriel)", "<b>aux</b> (à + les)", "J'ai mal <b>aux</b> dents. 🦷"]], ["50mm", "48mm", "84mm"])}
<div class="grid4 mt2">{"".join(f'<div class="card c" style="background:#fff;padding:1.5mm"><span class="emo s">{e}</span><div class="xs">{w}</div></div>' for e, w in [("🤒", "J'ai de la fièvre."), ("🤧", "J'ai un rhume."), ("😷", "Je tousse."), ("🤮", "J'ai envie de vomir."), ("🥶", "J'ai froid."), ("🥵", "J'ai chaud."), ("😴", "Je suis fatigué(e)."), ("🤕", "Je me suis blessé(e).")])}</div>
<p class="mt2"><b>Qu'est-ce qui ne va pas ?</b> / <b>Tu as mal où ?</b> / <b>Ça fait mal ?</b> — Oui, ça fait mal ! / Non, ça va mieux.</p>''')
    e = E("J'écoute : où ont-ils mal ? Je relie la personne et la partie du corps.", relie(["1. Amina", "2. Bilal", "3. Fatou", "4. Mateo"], ["aux dents", "au dos", "à la tête", "au pied"]), ["ecoute", "relie"], 1, "A",
          script="1. Amina : « J'ai mal à la tête, je ne dors pas bien. » — 2. Bilal : « Aïe ! J'ai mal au pied, j'ai joué au foot. » — 3. Fatou : « J'ai mal aux dents, je mange trop de bonbons ! » — 4. Mateo : « Mon sac est lourd, j'ai mal au dos. »",
          sol="Amina → à la tête · Bilal → au pied · Fatou → aux dents · Mateo → au dos")
    b.page(f'{l2}{e}', "Leçon 2")
    e = E("Au, à la, à l' ou aux ? Je complète.", '<div class="grid2">' + "".join(f'<p>J\'ai mal {blank("s")} {w}.</p>' for w in ["ventre", "gorge", "yeux", "dos", "oreille", "jambes", "bras", "main"]) + '</div>', ["complete"], 1, "C",
          sol="au ventre · à la gorge · aux yeux · au dos · à l'oreille · aux jambes · au bras · à la main")
    e2 = E("Je regarde et j'écris la phrase.", '<div class="grid4">' + "".join(f'<div class="card c"><span class="emo">{em}</span><div class="line"></div></div>' for em in ["🤒", "🥶", "🤧", "😴"]) + '</div>', ["regarde", "ecris"], 2, "C",
           sol="J'ai de la fièvre. · J'ai froid. · J'ai un rhume. · Je suis fatigué(e).")
    e3 = E("Le jeu du mime : je mime un problème. Mon camarade devine : « Tu as mal à la tête ? »", '', ["joue", "parle", "groupe"], 1, "D", sol="Jeu oral.")
    e4 = E("Défi ! J'écris un message à la prof : je suis malade, je ne viens pas à l'école.", lines(4), ["ecris"], 3, "C", sol="Exemple : Bonjour Madame, je suis malade. J'ai de la fièvre et j'ai mal à la gorge. Je ne viens pas à l'école aujourd'hui. Mon père va téléphoner à l'école. Merci. Yonas")
    b.page(f'{e}{e2}{e3}{e4}', "S'entraîner")

    # Leçon 3 impératif + il faut
    l3 = lecon("Donner un ordre ou un conseil : l'impératif · il faut", f'''<div class="grid2"><div class="card" style="background:#fff"><b>L'impératif</b> (sans « tu », sans « vous »)
<p>tu ouvres → <b>Ouvre</b> la bouche !<br>vous ouvrez → <b>Ouvrez</b> la bouche !<br>tu respires → <b>Respire</b> !<br>vous toussez → <b>Toussez</b> !</p><p class="sm muted">Verbes en -er avec tu : pas de -s ! (tu ouvres → ouvre)</p></div>
<div class="card" style="background:#fff"><b>Il faut</b> + verbe (infinitif)<p>Il faut <b>rester</b> au lit.<br>Il faut <b>boire</b> de l'eau.<br>Il faut <b>prendre</b> le médicament.<br>Il <b>ne</b> faut <b>pas</b> aller à l'école.</p></div></div>
<div class="card mt2" style="background:#fff"><b>Le médecin dit :</b> Asseyez-vous. · Ouvrez la bouche. · Tirez la langue. · Respirez fort. · Toussez. · Allongez-vous. · Montrez-moi où vous avez mal.</div>''')
    e = E("J'écoute le médecin et je fais le geste.", '', ["ecoute", "montre"], 1, "P", script="Donner les ordres du médecin (vous puis tu) : Asseyez-vous ! Ouvre la bouche ! Tire la langue ! Respire fort ! Tousse ! Lève le bras ! Montre-moi ton pied !", sol="Activité gestuelle.")
    b.page(f'{l3}{e}', "Leçon 3")
    e = E("J'écris l'ordre à l'impératif (tu, puis vous).", table(["Verbe", "tu", "vous"], [[v, "", ""] for v in ["ouvrir → ouvre", "respirer", "tousser", "regarder", "écouter", "rester"]], ["50mm", "66mm", "66mm"]).replace("<td></td>", '<td style="height:8mm"></td>'),
          ["ecris"], 2, "C", sol="Ouvre / Ouvrez · Respire / Respirez · Tousse / Toussez · Regarde / Regardez · Écoute / Écoutez · Reste / Restez")
    e2 = E("Des conseils : il faut / il ne faut pas. Je relie le problème et le conseil.", relie(["J'ai de la fièvre.", "J'ai mal aux dents.", "Je suis fatigué.", "J'ai mal au ventre.", "Je me suis coupé le doigt."], ["Il faut dormir.", "Il faut aller chez le dentiste.", "Il faut mettre un pansement.", "Il faut rester au lit.", "Il ne faut pas manger de frites."]),
           ["relie"], 2, "B", sol="fièvre → rester au lit · dents → dentiste · fatigué → dormir · ventre → pas de frites · coupé → pansement")
    e3 = E("Défi ! J'écris 4 conseils pour être en bonne santé (il faut / il ne faut pas).", lines(4), ["ecris"], 3, "C", sol="Il faut dormir 9 heures. Il faut manger des fruits. Il faut faire du sport. Il ne faut pas passer trop de temps sur l'écran.")
    b.page(f'{e}{e2}{e3}', "S'entraîner")

    # Personnes & lieux santé
    pl = [("🩺", "le médecin (le docteur)", "Il examine. Il donne une ordonnance."), ("💊", "le pharmacien / la pharmacie", "Il donne les médicaments."), ("🦷", "le dentiste", "Il soigne les dents."),
          ("🏥", "l'hôpital", "Pour les problèmes graves."), ("🚑", "les urgences / l'ambulance", "C'est urgent ! On appelle le 112."), ("🧑‍⚕️", "l'infirmière (à l'école)", "Elle soigne les petits problèmes.")]
    e = E("Les personnes et les lieux de la santé. J'écoute et je répète.", '<div class="grid3">' + "".join(f'<div class="card c"><span class="emo">{e}</span><div class="word">{w}</div><div class="xs muted">{d}</div></div>' for e, w, d in pl) + '</div>', ["ecoute", "repete"], 1, "A", script="Présenter chaque image. Expliquer : en Belgique, on va d'abord chez son médecin généraliste ; les urgences de l'hôpital, c'est pour les problèmes graves.", sol="Activité orale.")
    e2 = E("Où je vais ? Médecin, pharmacie, dentiste, ou j'appelle le 112 ?", '<div class="grid2">' + "".join(f'<div class="card"><p class="sm">{t}</p><p>→ {blank("l")}</p></div>' for t in ["J'ai une ordonnance, je veux les médicaments.", "J'ai mal aux dents depuis 3 jours.", "Mon ami est tombé, il ne bouge plus, il ne répond pas.", "J'ai de la toux et de la fièvre depuis 2 jours.", "Il y a un incendie dans la maison !", "J'ai besoin d'un certificat pour l'école."]) + '</div>',
           ["lis", "ecris"], 2, "C", sol="pharmacie · dentiste · 112 · médecin · 112 · médecin")
    b.page(f'<h2>Se soigner en Belgique</h2>{e}{e2}', "Lexique")

    # Doc 1 urgence
    urg = f'''<div class="doc" style="transform:none;padding:4mm;border:3px solid #D64545"><div class="c" style="font-weight:800;font-size:16pt;color:#D64545">🚨 NUMÉROS D'URGENCE EN BELGIQUE</div>
<div class="grid3 mt2"><div class="card c" style="border-color:#D64545"><div class="huge" style="color:#D64545;font-size:30pt">112</div><b>Ambulance · Pompiers</b><p class="xs">Accident, malaise grave, incendie. Gratuit, même sans crédit.</p></div>
<div class="card c" style="border-color:#1F4E79"><div class="huge" style="color:#1F4E79;font-size:30pt">101</div><b>Police</b><p class="xs">Vol, agression, danger.</p></div>
<div class="card c" style="border-color:#2BA88F"><div class="huge" style="color:#2BA88F;font-size:20pt">070 245 245</div><b>Centre Antipoisons</b><p class="xs">Quelqu'un a avalé un produit dangereux.</p></div></div>
<div class="card mt2" style="background:#FFF6F6"><b>Quand j'appelle le 112, je dis :</b><p>1️⃣ <b>Qui</b> je suis · 2️⃣ <b>Où</b> je suis (l'adresse !) · 3️⃣ <b>Ce qui se passe</b> · 4️⃣ Je ne raccroche pas : je réponds aux questions.</p></div></div>'''
    e = E("Je lis l'affiche. Quel numéro j'appelle ?", '<div class="grid2">' + "".join(f'<p>{t} → {blank("s")}</p>' for t in ["Mon petit frère a bu un produit pour nettoyer.", "Une voiture renverse un vélo, le cycliste saigne.", "Quelqu'un vole mon sac.", "La cuisine est en feu !"]) + '</div>', ["lis", "ecris"], 1, "B",
          sol="070 245 245 · 112 · 101 · 112")
    e2 = E("Je joue l'appel au 112 avec un camarade (l'un appelle, l'autre est l'opérateur).", '<div class="card"><p class="sm">— 112, j\'écoute. — Bonjour, je m\'appelle… Je suis à (adresse)… Mon ami est tombé, il a mal à la jambe, il ne peut pas marcher. — …</p></div>', ["parle", "duo"], 2, "A", sol="Vérifier : qui, où (adresse complète), quoi.")
    b.page(f'<span class="tag-doc">📄 DOCUMENT DE LA VIE</span><h2>Les urgences</h2>{urg}<div class="mt4">{e}{e2}</div>', "Document de la vie")

    # Doc 2 rendez-vous + notice
    rdv = f'''<div class="doc" style="transform:rotate(-1deg);padding:4mm;width:110mm;border:1px solid #ccc"><b style="color:#1F4E79">Dr Sophie MARTIN · Médecin généraliste</b><div class="xs muted">Rue de Fer 15 · 5000 Namur · ☎ 081 11 22 33</div>
<div style="border-top:1px solid #ddd;margin:2mm 0"></div><p><b>Rendez-vous</b> pour : <span style="font-family:'TeX Gyre Chorus';font-size:15pt;color:#1a3a8a">Yonas Tesfaye</span></p>
<p>le <span style="font-family:'TeX Gyre Chorus';font-size:15pt;color:#1a3a8a">mardi 13 octobre</span> à <span style="font-family:'TeX Gyre Chorus';font-size:15pt;color:#1a3a8a">16 h 40</span></p><p class="xs">Consultations : lundi au vendredi, 9 h – 12 h et 15 h – 18 h. En cas d'empêchement, prévenez 24 heures à l'avance. N'oubliez pas votre carte d'identité.</p></div>'''
    notice = '''<div class="doc" style="transform:rotate(1deg);padding:4mm;border:1px solid #ccc;background:#FAFAFA"><b>SIROP POUR LA TOUX · notice (extrait simplifié)</b>
<p class="sm">• <b>Pour qui ?</b> Adultes et enfants à partir de 12 ans.<br>• <b>Quand ?</b> Le matin, le midi et le soir, après le repas.<br>• <b>Combien ?</b> La quantité indiquée par le médecin ou le pharmacien.<br>• <b>Attention :</b> ne pas donner aux enfants de moins de 12 ans. Ne pas dépasser 5 jours. Garder hors de portée des enfants.<br>• En cas de problème : appelez votre médecin ou le Centre Antipoisons.</p></div>'''
    e = E("Je lis la carte de rendez-vous. Je réponds.", f'<p>1. Le rendez-vous est pour qui ? {blank()} 2. Quel jour ? {blank()} 3. À quelle heure ? {blank()}</p><p>4. Le médecin travaille le samedi ? {blank("s")} 5. Qu\'est-ce qu\'il faut apporter ? {blank("l")}</p>',
          ["lis", "ecris"], 2, "B", sol="1. Yonas Tesfaye — 2. le mardi 13 octobre — 3. 16 h 40 — 4. non — 5. la carte d'identité")
    e2 = E("Je lis la notice. Vrai ou faux ?", table(["", "V", "F"], [[x, '<span class="chk"></span>', '<span class="chk"></span>'] for x in ["On prend le sirop avant le repas.", "Un enfant de 8 ans peut prendre ce sirop.", "On prend le sirop trois fois par jour.", "On peut le prendre pendant un mois."]], ["140mm", "20mm", "20mm"]), ["lis", "coche"], 2, "B",
           sol="1. Faux (après) — 2. Faux (à partir de 12 ans) — 3. Vrai — 4. Faux (5 jours maximum)")
    b.page(f'<span class="tag-doc">📄 DOCUMENT DE LA VIE</span><h2>Le rendez-vous et la notice</h2><div class="grid2">{rdv}{notice}</div><div class="mt4">{e}{e2}</div><div class="attention">⚠️ Un médicament, c\'est sérieux : je demande toujours à un adulte, au médecin ou au pharmacien.</div>', "Document de la vie")

    # FLSco sécurité
    pict = [("🟩🏃🚪", "Sortie de secours", "#2BA88F"), ("🧯", "Extincteur", "#D64545"), ("🔔", "Alarme incendie", "#D64545"), ("🚫🛗", "Ne pas utiliser l'ascenseur", "#D64545"), ("📍👥", "Point de rassemblement", "#2BA88F"), ("➕", "Premiers secours", "#2BA88F")]
    l4 = lecon("Une consigne de sécurité : l'exercice d'évacuation", f'''<div class="grid3">{"".join(f'<div class="card c" style="background:#fff;border-color:{c}"><span class="emo s">{e}</span><div class="xs"><b>{t}</b></div></div>' for e, t, c in pict)}</div>
<div class="card mt2" style="background:#fff"><b>Quand l'alarme sonne :</b><p>1. J'arrête mon travail. 2. Je laisse mes affaires. 3. Je sors calmement avec la prof, en rang. 4. Je ne cours pas. Je ne prends pas l'ascenseur. 5. Je vais au point de rassemblement (la cour). 6. La prof compte les élèves.</p></div>''')
    e = E("Je lis la consigne et je numérote les images dans l'ordre.", '<div class="grid5">' + "".join(f'<div class="card c"><span class="emo s">{e}</span><div class="xs">{t}</div><span class="circ"></span></div>' for e, t in [("🚶‍♂️🚶‍♀️", "on sort en rang"), ("🔔", "l'alarme sonne"), ("👩‍🏫✅", "la prof compte"), ("✋📚", "j'arrête mon travail"), ("📍", "je vais dans la cour")]) + '</div>',
          ["lis", "numerote"], 2, "B", sol="Ordre affiché : 3 – 1 – 5 – 2 – 4")
    b.page(f'<span class="tag-doc">🎒 FRANÇAIS DE L\'ÉCOLE</span>{l4}{e}', "Consignes & école")

    # Sons
    e = E("Le son [k] et le son [g]. J'écoute et je répète.", '''<div class="grid2"><div class="card c"><div class="huge">[k]</div><p><b>c</b>a, <b>c</b>o, <b>c</b>u · <b>qu</b> · <b>k</b></p><p>cou · corps · cœur · qui · kilo · école</p></div><div class="card c"><div class="huge">[g]</div><p><b>g</b>a, <b>g</b>o, <b>g</b>u · <b>gu</b>e, <b>gu</b>i</p><p>gorge · genou… non ! → gare · goût · guitare · langue</p></div></div>
<div class="astuce" style="margin-bottom:0"><b>c + e, i</b> = [s] : ceci, cinq · <b>g + e, i</b> = [ʒ] : genou, gilet. <b>Mais</b> ga, go, gu = [g] et ca, co, cu = [k].</div>'''.replace("gorge · genou… non ! → gare", "gorge · gare"), ["ecoute", "repete"], 1, "A",
          script="Faire sentir que [g] vibre et [k] ne vibre pas. Paires : cou/goût, car/gare, classe/glace. Puis : cinq, ceci, genou, gilet (c et g doux).", sol="Activité orale.")
    e2 = E("J'écoute. [k] ou [g] ? Je coche.", table(["", "1", "2", "3", "4", "5", "6", "7", "8"], [["[k]"] + ['<span class="chk"></span>'] * 8, ["[g]"] + ['<span class="chk"></span>'] * 8], ["20mm"] + ["20mm"] * 8),
           ["ecoute", "coche"], 2, "A", script="1. gorge — 2. cou — 3. qui — 4. langue — 5. coude — 6. guérir — 7. corps — 8. gare", sol="1. [g] — 2. [k] — 3. [k] — 4. [g] — 5. [k] — 6. [g] — 7. [k] — 8. [g]")
    e3 = E("C doux ou c dur ? J'entoure en bleu [k], en rouge [s].", '<p class="big">un cou · cinq · la colle · ceci · un cœur · la cuisine · merci · un cahier</p>', ["entoure"], 3, "B", sol="[k] : cou, colle, cœur, cuisine, cahier · [s] : cinq, ceci, merci")
    b.page(f'<h2>J\'écoute bien · [k] / [g]</h2>{e}{e2}{e3}', "Sons")

    # Révise
    e = E("🔁 Module 4 · Je décris une personne de la classe (3 phrases).", lines(3), ["ecris"], 1, "C", sol="Production : Il / Elle a les cheveux… Il / Elle est…")
    e2 = E("🔁 Module 4 · Mon, ma, mes.", '<p>___ tête · ___ yeux · ___ main · ___ oreille · ___ dos</p>', ["complete"], 2, "C", sol="ma · mes · ma · mon (voyelle) · mon")
    e3 = E("🔁 Module 3 · Le rendez-vous chez le médecin : j'écris la date et l'heure en lettres.", '<p>12/11 à 15 h 30 → ______________________</p><p>03/12 à 9 h 15 → ______________________</p>', ["ecris"], 2, "C", sol="le 12 novembre à quinze heures trente · le 3 décembre à neuf heures quinze")
    e4 = E("🔁 Module 2 · Où je vais dans l'école quand j'ai mal ?", '<p>→ ___________</p>', ["ecris"], 1, "C", sol="à l'infirmerie")
    b.page(f'<h2>🔁 Je révise les modules 2 à 4</h2>{e}{e2}{e3}{e4}', "Je révise")

    # Ateliers
    e = E("Chez le médecin : je joue la scène (patient / médecin) avec les cartes.", '<div class="grid3">' + "".join(f'<div class="card" style="border-style:dashed"><span class="emo s">{em}</span><p class="sm">{t}</p></div>' for em, t in [("🤕", "Tu es tombé dans la cour. Mal au genou."), ("🤧", "Rhume, nez qui coule, fatigué."), ("🤢", "Mal au ventre depuis hier soir."), ("🦷", "Mal aux dents, tu ne dors pas."), ("🤒", "Fièvre 39, mal à la gorge."), ("👁️", "Les yeux qui piquent, tu lis mal au tableau.")]) + '</div>',
          ["parle", "duo", "decoupe"], 2, "A", sol="Médecin : Bonjour, qu'est-ce qui ne va pas ? Depuis quand ? Ouvrez la bouche… Il faut… Patient : J'ai mal…")
    e2 = E("Le loto du corps : la prof dit une partie du corps, je pose un jeton sur l'image.", '<div class="grid4">' + "".join(f'<div class="card c" style="font-size:26pt">{x}</div>' for x in ["👃", "👂", "🦶", "✋", "🦷", "👁️", "🦵", "💪"]) + '</div>', ["ecoute", "joue"], 1, "D", script="Dire au hasard : le pied, la main, l'oreille, le bras, le nez, la jambe, l'œil, la dent.", sol="Jeu.")
    b.page(f'<span class="atl A" style="font-size:12pt;padding:1.5mm 4mm">{ATELIERS["A"]}</span><h2 class="mt2">Ateliers · Parler et jouer</h2>{e}{e2}', "Atelier")
    txt = '''<div class="card" style="background:#FFFDF8;line-height:1.6">📧 <b>De :</b> Lucía Ramírez · <b>À :</b> Mme Lambert · <b>Objet :</b> Absence de Mateo<br><br>Bonjour Madame,<br>Mateo est malade depuis hier. Il a de la fièvre et il tousse beaucoup. Ce matin, nous sommes allés chez le médecin : c'est une bronchite. Le médecin dit qu'il faut rester à la maison jusqu'à vendredi. Je vous envoie le certificat médical demain. Est-ce que Mateo peut recevoir les devoirs par son cousin Pablo ?<br>Merci beaucoup et bonne journée.<br>Lucía Ramírez (maman de Mateo)</div>'''
    e = E("Je lis le courriel de la maman de Mateo.", txt, ["lis"], 1, "B")
    e2 = E("Je réponds.", f'<p>1. Mateo est malade depuis quand ? {blank()} 2. Quels sont ses symptômes ? {blank("l")}</p><p>3. Quelle est la maladie ? {blank()} 4. Jusqu\'à quand il reste à la maison ? {blank()}</p><p>5. ●●● Qu\'est-ce que la maman demande à la prof ? {blank("xl")}</p>',
           ["lis", "ecris"], 2, "B", sol="1. depuis hier — 2. fièvre, toux — 3. une bronchite — 4. jusqu'à vendredi — 5. si Mateo peut recevoir les devoirs par son cousin Pablo")
    e3 = E("Défi ! J'écris la réponse de la prof (3 phrases).", lines(3), ["ecris"], 3, "C", sol="Exemple : Bonjour Madame, merci pour votre message. Je donne les devoirs à Pablo. Bon rétablissement à Mateo !")
    b.page(f'<span class="atl B" style="font-size:12pt;padding:1.5mm 4mm">{ATELIERS["B"]}</span><h2 class="mt2">Atelier · Lire et écrire</h2>{e}{e2}{e3}', "Atelier")

    # Alpha
    letter_page(b, E, "c", "[k]", [("🥕", "carotte"), ("🍬", "caramel"), ("🦒", "cou"), ("🎁", "cadeau")], "eoaeoeao", [("🎁", "cadeau", 1), ("🦒", "cou", 1), ("🐟", "poisson", 0), ("🥕", "carotte", 1), ("🍫", "chocolat", 1), ("🌙", "lune", 0), ("🛏️", "lit", 0), ("☕", "café", 1)], MC)
    letter_page(b, E, "qu", "[k]", [("4️⃣", "quatre"), ("🐟", "queue de poisson"), ("❓", "question"), ("🎳", "quille")], "qgpdqgpd", [("4️⃣", "quatre", 1), ("❓", "question", 1), ("🚲", "vélo", 0), ("🎳", "quille", 1), ("🍓", "fraise", 0), ("🧃", "jus", 0), ("5️⃣", "cinq", 1), ("🦒", "cou", 1)], MC)
    letter_page(b, E, "g", "[g]", [("🎂", "gâteau"), ("🚉", "gare"), ("🎸", "guitare"), ("🦍", "gorille")], "qpjqpjyq", [("🎂", "gâteau", 1), ("🎸", "guitare", 1), ("🦍", "gorille", 1), ("🐱", "chat", 0), ("🚉", "gare", 1), ("🧃", "jus", 0), ("🍅", "tomate", 0), ("👅", "langue", 1)], MC)
    e = E("Je lis les syllabes.", syll_table(["c", "qu", "g"], "a o u é i") + '<div class="attention mt2" style="margin-bottom:0">⚠️ <b>ci</b> se lit [si] et <b>gi</b> se lit [ʒi] ! Pour [k] avec i et é, on écrit <b>qui, qué</b>. Pour [g] : <b>gui, gué</b>.</div>', ["lis"], 1, "P", alpha=True,
          script="Lire en lignes. Signaler les pièges ci/gi.", sol="ca co cu cé ci[si] / qua quo qu… / ga go gu gé[ʒé] gi[ʒi]")
    e2 = E("Je lis les mots du corps et de la santé.", '<div class="grid4">' + "".join(f'<div class="card c"><span class="emo s">{e}</span><div class="huge" style="font-size:16pt">{w.replace("-", "<span style=color:#E4572E>·</span>")}</div></div>' for e, w in [("🦒", "cou"), ("🦶", "pied"), ("👃", "nez"), ("💊", "ca-chet"), ("🦵", "ge-nou"), ("🤒", "ma-la-de"), ("🦷", "dent"), ("🎂", "gâ-teau")]) + '</div>',
           ["lis"], 1, "P", alpha=True, script="Lire avec l'élève ; « pied », « dent », « gâteau » se lisent globalement (sons pas encore vus).", sol="cou · pied · nez · cachet · genou · malade · dent · gâteau")
    b.page(AL.format(t="Je lis") + e + e2, "★ Alpha", color=MC)
    e = E("Je lis les phrases et je montre sur mon corps.", '<div class="grid2">' + "".join(f'<div class="card"><p class="big">{t}</p></div>' for t in ["J'ai mal au cou.", "Il a mal au pied.", "Sami a mal au nez.", "Ma mère est malade."]) + '</div>', ["lis", "montre"], 2, "B", alpha=True, sol="Lecture + geste.")
    e2 = E("Dictée.", guide_lines(2, 20), ["ecoute", "ecris"], 2, "P", alpha=True, script="Dicter : ca — co — gu — ga — cou — malade — moto", sol="ca co gu ga cou malade moto")
    e3 = E("Je recopie : « J'ai mal. »", trace("J'ai mal.", 26, 2) + guide_lines(1, 20), ["recopie"], 1, "C", alpha=True, sol="Copie.")
    b.page(AL.format(t="Je lis des phrases, j'écris") + e + e2 + e3, "★ Alpha", color=MC)

    # Tâche finale
    fiche = f'''<div style="border:4px solid {MC};border-radius:5mm;padding:5mm;background:#FFF6F6"><div class="c" style="font-weight:800;font-size:15pt;color:{MC}">🚑 MA FICHE URGENCE</div>
<div style="line-height:2.3">Prénom et NOM : {blank("xl")}<br>Date de naissance : {blank("l")}<br>Mon adresse : {blank("xl")}<br>Personne à contacter : {blank("l")} ☎ {blank()}<br>Mon médecin : {blank("l")} ☎ {blank()}<br>Allergies / maladie : {blank("xl")}<br>Numéros : 🚑 112 · 👮 101 · ☠️ 070 245 245</div></div>'''
    e = E("Partie 1 : je remplis ma fiche urgence (je la garde dans mon cartable).", fiche, ["ecris"], 2, "C", sol="Fiche personnelle (vérifier avec les parents ; informations confidentielles).")
    b.page(f'''<div style="background:#1F2A44;color:#fff;margin:-17mm -14mm 5mm -14mm;padding:15mm 14mm 5mm 14mm"><div style="font-size:11pt;font-weight:700;opacity:.8">🎯 TÂCHE FINALE</div><div style="font-size:26pt;font-weight:800">Chez le médecin + ma fiche urgence</div>
<div class="sm" style="opacity:.9">Je prépare ma fiche urgence. Puis je joue une consultation chez le médecin avec un camarade, devant la classe.</div></div>{e}''', "Tâche finale", levels=False)
    sc = table(["Étape", "Le patient dit…", "Le médecin dit…"], [["1. Saluer", "Bonjour docteur.", "Bonjour. Asseyez-vous."], ["2. Le problème", "J'ai mal…", "Depuis quand ?"], ["3. L'examen", "…", "Ouvrez la bouche. Respirez…"], ["4. Le conseil", "D'accord.", "Il faut… Voici l'ordonnance."], ["5. Prendre congé", "Merci, au revoir.", "Au revoir, bon rétablissement !"]], ["34mm", "74mm", "74mm"])
    e = E("Partie 2 : j'écris le dialogue avec mon camarade, puis on le joue.", sc + lines(5), ["ecris", "parle", "duo"], 2, "A", sol="Dialogue évalué avec la grille.")
    b.page(e, "Tâche finale", levels=False)

    e = E("Au, à la, à l', aux.", '<p>J\'ai mal ___ dos, ___ yeux, ___ gorge, ___ oreille.</p>', ["complete"], 1, "C", sol="au · aux · à la · à l'")
    e2 = E("J'écris l'ordre à l'impératif (vous).", '<p>ouvrir la bouche → ______ · respirer → ______ · s\'asseoir → ______</p>', ["ecris"], 2, "C", sol="Ouvrez la bouche · Respirez · Asseyez-vous")
    e3 = E("Quel numéro ?", '<p>Incendie : ___ · Police : ___ · Poison : ___</p>', ["ecris"], 1, "C", sol="112 · 101 · 070 245 245")
    e4 = E("Défi ! Je corrige les 4 erreurs.", '<div class="card big">J\'ai mal à le ventre et à les dents. Il faut reste au lit. Ouvres la bouche !</div>' + lines(2), ["barre", "ecris"], 3, "C", sol="au ventre · aux dents · Il faut rester · Ouvre la bouche")
    b.page(f'<h2>🔁 Je révise tout le module</h2>{e}{e2}{e3}{e4}', "Je révise")

    head = f'''<div style="background:#1F2A44;color:#fff;margin:-17mm -14mm 4mm -14mm;padding:14mm 14mm 4mm 14mm;display:flex;justify-content:space-between;align-items:flex-end"><div><div style="font-size:11pt;font-weight:700;opacity:.8">📝 TEST · MODULE 5</div><div style="font-size:24pt;font-weight:800">Mon corps, ma santé</div></div><div class="sm" style="text-align:right">Prénom : ......................................<br>Date : ........ / ........ / ............</div></div>'''
    Q = [("👃 =", ["l'oreille", "le nez", "la bouche", "l'œil"]), ("🦶 =", ["la main", "le genou", "le pied", "le bras"]), ("Le pluriel de « un œil » :", ["des œils", "des yeux", "des oeuils", "des yeuxs"]),
         ("J'ai mal ____ tête.", ["au", "aux", "à la", "à l'"]), ("J'ai mal ____ ventre.", ["à la", "au", "aux", "à l'"]), ("J'ai mal ____ dents.", ["au", "à la", "à l'", "aux"]),
         ("🤒 =", ["J'ai de la fièvre.", "J'ai faim.", "Je suis content.", "J'ai froid aux pieds."]), ("🥶 =", ["J'ai chaud.", "J'ai sommeil.", "J'ai froid.", "J'ai mal au dos."]),
         ("Le médecin dit : « ____ la bouche ! »", ["Ouvres", "Ouvrez", "Ouvrir", "Ouvert"]), ("Il faut ____ au lit.", ["reste", "restez", "rester", "restes"]),
         ("Pour les médicaments, je vais :", ["à la gare", "à la pharmacie", "à la poste", "à la banque"]), ("Mal aux dents ? Je vais chez :", ["le dentiste", "le boulanger", "le coiffeur", "le pharmacien"]),
         ("Ambulance et pompiers en Belgique :", ["101", "070 245 245", "112", "100 000"]), ("Police en Belgique :", ["112", "101", "18", "911"]),
         ("Quand j'appelle le 112, je dis d'abord :", ["qui je suis et où je suis", "mon âge", "ma couleur préférée", "rien"]), ("L'alarme sonne. Je :", ["prends l'ascenseur", "sors calmement avec la prof", "cours dans l'escalier", "reste en classe"]),
         ("J'entends [g] comme dans « gare » :", ["genou", "gorge", "girafe", "gilet"]), ("Sur la notice : « à partir de 12 ans ». Un enfant de 8 ans :", ["peut le prendre", "ne peut pas le prendre", "prend deux fois plus", "prend la moitié"]),
         ("🔁 ____ mère est gentille.", ["Mon", "Ma", "Mes", "Son"]), ("🔁 Ma sœur est ____.", ["grand", "grande", "grands", "grandes"])]
    key = "1-B, 2-C, 3-B, 4-C, 5-B, 6-D, 7-A, 8-C, 9-B, 10-C, 11-B, 12-A, 13-C, 14-B, 15-A, 16-B, 17-B, 18-B, 19-B, 20-B"
    Q[16] = (Q[16][0], ["genou", "girafe", "gilet", "gorge"])
    Q[17] = (Q[17][0], ["peut le prendre", "prend deux fois plus", "ne peut pas le prendre", "prend la moitié"])
    Q[18] = (Q[18][0], ["Mon", "Mes", "Son", "Ma"])
    Q[19] = (Q[19][0], ["grande", "grand", "grands", "grandes"])
    key = "1-B, 2-C, 3-B, 4-C, 5-B, 6-D, 7-A, 8-C, 9-B, 10-C, 11-B, 12-A, 13-C, 14-B, 15-A, 16-B, 17-D, 18-C, 19-D, 20-A"
    p1 = "".join(qcm_line(i + 1, q, o) for i, (q, o) in enumerate(Q[:10]))
    p2 = "".join(qcm_line(i + 11, q, o) for i, (q, o) in enumerate(Q[10:]))
    b.page(f'{head}<div class="flex" style="justify-content:space-between"><h2 style="margin:0">Partie A · Je choisis la bonne réponse</h2><span class="score">…… / 20</span></div>{p1}', "Test", levels=False)
    b.page(p2, "Test", levels=False)
    b.page(f'''<div class="flex" style="justify-content:space-between"><h2 style="margin:0">Partie B · J'écris</h2><span class="score">…… / 10</span></div>
<h3>B1. J'écris 4 parties du corps (le, la, l', les). (… / 4)</h3><div class="flex top">{body("60mm", False)}<div class="grow">{lines(4, True)}</div></div>
<h3>B2. J'écris un message à la prof : je suis malade (problème, conseil du médecin, absence). (… / 6)</h3>{lines(5, True)}
<div class="flex mt2" style="justify-content:space-between"><h2 style="margin:0">Partie C · Je parle avec la prof</h2><span class="score">…… / 10</span></div>
{table(["Je sais…", "Points", "✅"], [["montrer et nommer 6 parties du corps", "/ 3", ""], ["jouer une consultation (patient)", "/ 4", ""], ["simuler un appel au 112 (qui, où, quoi)", "/ 3", ""]], ["120mm", "30mm", "32mm"])}<div class="card mt2 c"><span class="huge">TOTAL : …… / 40</span></div>''', "Test", levels=False)
    ta = f'''<div style="background:#FFD166;margin:-17mm -14mm 4mm -14mm;padding:14mm 14mm 4mm 14mm"><div style="font-size:11pt;font-weight:800">★ ALPHA · 📝 TEST · MODULE 5</div><div style="font-size:22pt;font-weight:800">Mon corps, ma santé</div></div>
<h3>1. J'écoute et j'entoure. (… / 4)</h3><div class="grid4">{"".join(f'<div class="card c big" style="font-weight:700;white-space:nowrap">{r}</div>' for r in ["ca co cu", "ga go gu", "qua qui quo", "co cou cu"])}</div>
<h3>2. Je lis et je relie. (… / 4)</h3>{relie([f'<b class="big">{w}</b>' for w in ["cou", "nez", "malade", "gâteau"]], ['<span class="emo s">🤒</span>', '<span class="emo s">🎂</span>', '<span class="emo s">🦒</span>', '<span class="emo s">👃</span>'])}
<h3>3. Dictée. (… / 4)</h3>{guide_lines(1, 22)}<h3>4. Je montre sur mon corps (oral) : la tête, la main, le pied, le ventre. (… / 4)</h3><div class="card">☐ ☐ ☐ ☐</div>
<h3>5. Je dis (oral) : « J'ai mal à… » avec les images. (… / 4)</h3><div class="grid4">{"".join(f'<div class="card c" style="font-size:26pt">{x}</div>' for x in ["🤕", "🦷", "🤢", "🦶"])}</div><div class="card c mt2"><span class="huge">TOTAL : …… / 20</span></div>'''
    b.page(ta, "★ Alpha · Test", levels=False)
    items = ["Je sais nommer les parties du corps.", "Je sais dire où j'ai mal (au, à la, aux).", "Je sais dire comment je me sens.", "Je comprends les ordres du médecin (impératif).", "Je sais donner un conseil (il faut).",
             "Je connais les numéros d'urgence.", "Je sais appeler le 112.", "Je sais lire un rendez-vous et une notice simple.", "Je connais les consignes d'évacuation.", "★ Je sais lire ca, co, gu, qui, cou, malade…"]
    tb = table(["", "😀 Oui !", "🙂 Un peu", "😕 Pas encore", "La prof"], [[x, '<span class="chk"></span>', '<span class="chk"></span>', '<span class="chk"></span>', ""] for x in items], ["92mm", "20mm", "20mm", "24mm", "26mm"])
    b.page(f'<h2>✅ Je sais faire</h2>{tb}<div class="grid2 mt4"><div class="card"><b>Ce que j\'aime :</b>{lines(2)}</div><div class="card"><b>C\'est difficile :</b>{lines(2)}</div></div>', "Je sais faire", levels=False)
    mots = [(e, w) for (_, w, *_), e in zip(PARTS, ["🙂", "💇", "👁️", "👂", "👃", "👄", "🦒", "🤷", "💪", "✋", "☝️", "🫃", "🔙", "🦵", "🦵", "🦶"])] + [("🤕", "avoir mal"), ("🤒", "la fièvre"), ("🤧", "le rhume"), ("😷", "tousser"), ("🩺", "le médecin"), ("💊", "le médicament"), ("🏥", "l'hôpital"), ("🚑", "les urgences"), ("📄", "l'ordonnance"), ("🏪", "la pharmacie"), ("🦷", "le dentiste"), ("🛏️", "se reposer"), ("🚨", "l'alarme"), ("🚪", "la sortie de secours")]
    half = len(mots) // 2
    mt = lambda lst: table(["", "Français", "Dans ma langue"], [[f'<span style="font-size:12pt">{e}</span>', f"<b>{w}</b>", ""] for e, w in lst], ["12mm", "40mm", "36mm"]).replace("<td>", '<td style="padding:1.2mm 2mm">')
    b.page(f'<h2>📒 Mes mots du module 5</h2><div class="grid2">{mt(mots[:half])}{mt(mots[half:])}</div>', "Mes mots", levels=False)

    plan_de_travail(b, E, 5, ["Le corps", "J'ai mal… Comment je me sens", "L'impératif · il faut", "Consigne de sécurité : l'évacuation"], "☐ Fiche urgence<br>☐ Consultation jouée")
    if render:
        to_pdf(b.html(), '/home/claude/syllabus/out/V1_M5_eleve.pdf')
    pg, exs = helpers(b, E)
    A = b.marks["★ Alpha"]
    days = [("1", "Collectif", f"Ouverture · BD ({pg('Découvrir')})", f"Alpha : c (p. {A[0]})"), ("2", "Collectif + jeux", f"📌 Leçon 1 le corps ({pg('Leçon 1')})", f"Alpha : qu (p. {A[1]})"),
            ("3", "Rotation", f"📌 Leçon 2 j'ai mal ({pg('Leçon 2')})", f"Alpha : g (p. {A[2]})"), ("4", "Collectif", f"📌 Leçon 3 impératif, il faut ({pg('Leçon 3')})", f"Alpha : syllabes (p. {A[3]})"),
            ("5", "Rotation", f"Se soigner en Belgique ({pg('Lexique')}) · urgences ({pg('Document de la vie')})", f"Alpha : phrases (p. {A[4]})"), ("6", "Collectif", "Rendez-vous et notice · exercice d'évacuation réel si possible", "Alpha : révision"),
            ("7", "Rotation", f"Sons ({pg('Sons')}) · 🔁 révision", "Alpha : lecture"), ("8", "Ateliers", f"Ateliers ({pg('Atelier')})", "Alpha : loto du corps"), ("9", "Duo", f"Tâche finale ({pg('Tâche finale')})", "Alpha : fiche urgence avec aide"),
            ("10", "Seul", f"Test ({pg('Test')}) · je sais faire · mes mots", f"Alpha : test ({pg('★ Alpha · Test')})")]
    rot = [["🎧 Écouter-Parler", "Jeux de rôle chez le médecin", "20 min", "—"], ["📖 Lire", "Courriel de la maman de Mateo", "20 min", "Oui"], ["✏️ Écrire", "Message d'absence · réponse de la prof", "20 min", "● oui"],
           ["🧩 Jouer", "Loto du corps · mime", "20 min", "Entre joueurs"], ["👩‍🏫 Table d'appui", "Alpha : c qu g · autres : au/à la/aux, impératif", "20 min", "—"]]
    ev1 = '''<h3>Partie B · Écrit (10 points)</h3><p class="sm"><b>B1</b> : 1 pt par partie avec article correct · <b>B2</b> : salutation (1), problème avec « j'ai mal à » (2), conseil « il faut » (1), absence (1), formule finale (1).</p>
<h3>Partie C · Oral (10 points)</h3><p class="sm">6 parties (½ pt chacune) · consultation : saluer, dire le problème, répondre, remercier (4) · 112 : qui (1), où avec adresse (1), quoi (1).</p>
<h3>Test ★ Alpha</h3><p class="sm"><b>Ex. 1, dire :</b> <span class="sol">co · gu · qui · cou</span> · <b>Ex. 2 :</b> <span class="sol">cou–🦒, nez–👃, malade–🤒, gâteau–🎂</span> · <b>Ex. 3, dicter :</b> <span class="sol">ca, go, cou, malade</span>.</p>'''
    ev2 = f'''<h2>Grille · tâche finale « Chez le médecin »</h2>{table(["Critère", "Très bien", "Bien", "À retravailler", "Points"], [["<b>Fiche urgence</b> complète et lisible", "Complète", "Partielle", "Incomplète", "/ 4"], ["<b>Dialogue</b> : 5 étapes", "5 étapes", "3-4", "0-2", "/ 6"], ["<b>Langue</b> : j'ai mal à, impératif, il faut", "Correct", "Quelques erreurs", "Beaucoup", "/ 6"], ["<b>Oral</b> : prononciation, gestes", "Clair", "Hésitant", "Bloqué", "/ 4"]], ["64mm", "32mm", "32mm", "32mm", "22mm"])}
<div class="attention mt4"><b>Confidentialité :</b> la fiche urgence contient des données personnelles et de santé. Elle reste dans le cartable de l'élève ; ne pas l'afficher ni la ramasser. Certains élèves ont vécu des situations médicales traumatisantes : rester attentif.</div>
<h2 class="mt4">Différencier et remédier</h2>{table(["Difficulté", "Remédiation"], [["au / à la / aux", "Tableau mural avec code couleur ; jeu « Aïe ! » (l'élève touche, la classe dit la phrase)."], ["Impératif", "Jeu du robot (module 2) avec les ordres du médecin."], ["Numéros d'urgence", "Rituel : chaque lundi, « Quel numéro pour… ? » ; affiche dans la classe."], ["Élève rapide", "Écrire une fiche « premiers secours » illustrée pour la classe ; dialogue à la pharmacie."]], ["50mm", "132mm"])}'''
    T = teacher_book(b, E, "V1 · M5", "", MC, 5, "Mon corps, ma santé",
                     "<li><b>Communication :</b> nommer le corps, dire où on a mal, comprendre le médecin, appeler à l'aide.</li><li><b>Lexique :</b> corps, symptômes, professionnels et lieux de santé, sécurité.</li><li><b>Grammaire :</b> avoir mal au/à la/à l'/aux (articles contractés), impératif (tu/vous), il faut + infinitif.</li><li><b>Phonétique :</b> [k]/[g], c et g durs/doux.</li><li><b>FLSco :</b> consignes de sécurité, évacuation, notice.</li><li><b>★ Alpha :</b> c, qu, g ; phrases « J'ai mal au… ».</li>",
                     '<p class="sm"><b style="color:#E4572E">Indispensable</b> : 112, « J\'ai mal à… », parties principales du corps, évacuation.</p><p class="sm"><b style="color:#d9a400">Important</b> : impératif, il faut, pharmacie/médecin.</p><p class="sm"><b style="color:#2BA88F">Enrichissement</b> : notice, courriel d\'absence, c/g doux.</p>',
                     "Thermomètre et boîte de pansements (montrer) · ciseaux · jetons · plan d'évacuation réel de l'école.",
                     "<b>Lien école :</b> profiter du module pour faire visiter l'infirmerie et montrer le plan d'évacuation réel. Vérifier avec la direction le point de rassemblement.",
                     days, "« Comment ça va aujourd'hui ? » avec l'échelle des visages · un élève dit un conseil santé · rappel du 112.", rot, key, (ev1, ev2), start=tstart)
    if render:
        to_pdf(T.html(), '/home/claude/syllabus/out/V1_M5_prof.pdf')
    return b, T


if __name__ == "__main__":
    b, T = build_m5()
    print(b.n, T.n)
