"""Volume 1 · Module 2 « Mon école » — partie C : tâche finale, révision, test."""
from lib.base import *
from lib.art import *
from lib.alpha import AL
from build.m2_a import MC, plan_ecole

KEY = "1-D, 2-A, 3-B, 4-C, 5-D, 6-C, 7-A, 8-B, 9-A, 10-C, 11-B, 12-A, 13-C, 14-A, 15-D, 16-C, 17-A, 18-B, 19-D, 20-D"


def build_c(b, E):
    steps = [("1", "🚶", "Avec mon groupe, je visite l'école. Je choisis 4 lieux."), ("2", "🎨", "Je dessine chaque lieu (ou je prends une photo)."), ("3", "✏️", "J'écris 3 phrases par lieu."),
             ("4", "📒", "On assemble le guide."), ("5", "🎤", "On présente le guide aux nouveaux élèves.")]
    st = "".join(f'<div class="card c"><div style="font-size:18pt;font-weight:800;color:{MC}">{n}</div><span class="emo s">{e}</span><p class="sm">{t}</p></div>' for n, e, t in steps)
    fiche = lambda: f'''<div style="border:3px solid {MC};border-radius:5mm;padding:4mm;background:#FFFDF8;margin-bottom:4mm"><div class="flex top"><div style="width:55mm;height:42mm;border:2px dashed #9aa1b1;border-radius:3mm" class="c muted sm">dessin / photo</div>
<div class="grow" style="line-height:2.2">Ici, c'est {blank("l")}.<br>C'est au {blank("l")}.<br>Il y a {blank("xl")}.<br>On vient ici pour {blank("l")}.</div></div></div>'''
    e1 = E("Le guide : les pages de mes lieux.", fiche() + fiche(), ["ecris", "dessine", "groupe"], 2, "C", sol="Production évaluée avec la grille de la tâche finale.")
    b.page(f'''<div style="background:#1F2A44;color:#fff;margin:-17mm -14mm 5mm -14mm;padding:15mm 14mm 5mm 14mm"><div style="font-size:11pt;font-weight:700;opacity:.8">🎯 TÂCHE FINALE</div><div style="font-size:26pt;font-weight:800">Le guide de notre école</div>
<div class="sm" style="opacity:.9">Nous faisons un guide illustré pour aider les nouveaux élèves qui arrivent dans l'école.</div></div><div class="grid5">{st}</div><div class="mt4">{e1}</div>''', "Tâche finale", levels=False)
    chk = table(["Avant de présenter, je vérifie :", "✅"], [[x, '<span class="chk"></span>'] for x in ["J'ai 4 lieux avec un dessin.", "Chaque lieu a 3 phrases ou plus.", "J'utilise « il y a ».", "J'utilise bien un / une / le / la / les.", "Je sais présenter un lieu à voix haute."]], ["160mm", "22mm"])
    e2 = E("Encore deux lieux pour le guide.", fiche() + fiche(), ["ecris", "dessine"], 2, "C", sol="Production.")
    b.page(f'{e2}{chk}', "Tâche finale", levels=False)

    e3 = E("Je mets un, une ou des. Puis le, la, l' ou les.", '<div class="grid2">' + "".join(f'<p>{blank("s")} {w} → {blank("s")} {w}</p>' for w in ["tableau", "cour", "élèves", "horloge", "cahiers", "infirmerie"]) + '</div>', ["complete"], 1, "C",
           sol="un/le tableau · une/la cour · des/les élèves · une/l' horloge · des/les cahiers · une/l' infirmerie")
    e4 = E("J'écris le lieu.", '<div class="grid3">' + "".join(f'<div class="card c"><span class="emo s">{e}</span><div class="line"></div></div>' for e in ["🍽️", "📚", "🩺", "🏀", "🗂️", "🌳"]) + '</div>', ["ecris"], 1, "C",
           sol="le réfectoire · la bibliothèque · l'infirmerie · la salle de gym · le secrétariat · la cour")
    e5 = E("Je remets les mots dans l'ordre.", '<p>1. y a / il / chaises / des → __________________</p><p>2. est / où / la bibliothèque / ? → __________________</p><p>3. me prêter / tu peux / ta gomme / ? → __________________</p>', ["ecris"], 2, "C",
           sol="1. Il y a des chaises. — 2. Où est la bibliothèque ? — 3. Tu peux me prêter ta gomme ?")
    e6 = E("Défi ! Je trouve et je corrige les 4 erreurs.", '<div class="card"><p class="big">Dans la classe, il y a un chaise et des livre. Où sont la bibliothèque ? Donne ta gomme !</p></div>' + lines(2), ["lis", "barre", "ecris"], 3, "C",
           sol="une chaise · des livres · Où est la bibliothèque ? · Tu peux me prêter ta gomme, s'il te plaît ?")
    b.page(f'<h2>🔁 Je révise tout le module</h2>{e3}{e4}{e5}{e6}', "Je révise")

    head = f'''<div style="background:#1F2A44;color:#fff;margin:-17mm -14mm 4mm -14mm;padding:14mm 14mm 4mm 14mm;display:flex;justify-content:space-between;align-items:flex-end">
<div><div style="font-size:11pt;font-weight:700;opacity:.8">📝 TEST · MODULE 2</div><div style="font-size:24pt;font-weight:800">Mon école</div></div><div class="sm" style="text-align:right">Prénom : ......................................<br>Date : ........ / ........ / ............</div></div>'''
    Q = [("📏 =", ["un crayon", "une gomme", "un livre", "une latte"]), ("✂️ =", ["des ciseaux", "un cahier", "une colle", "un stylo"]),
         ("____ cahier", ["une", "un", "des", "la"]), ("____ gomme", ["un", "des", "une", "le"]), ("____ livres", ["un", "une", "la", "des"]),
         ("Le pluriel de « la chaise » :", ["le chaises", "les chaise", "les chaises", "la chaises"]), ("Dans la classe, ____ un tableau.", ["il y a", "il est", "c'est des", "il a"]),
         ("J'ai mal. Je vais :", ["à la bibliothèque", "à l'infirmerie", "au réfectoire", "au secrétariat"]), ("Je mange à midi :", ["au réfectoire", "à la salle de gym", "aux toilettes", "au secrétariat"]),
         ("Pour emprunter un livre, je vais :", ["à l'infirmerie", "dans la cour", "à la bibliothèque", "à la salle des profs"]),
         ("Je suis en retard. Je dis :", ["Merci !", "Excusez-moi pour le retard.", "Bonne nuit !", "Il y a un retard."]),
         ("Je n'ai pas de crayon. Je dis à mon voisin :", ["Tu peux me prêter un crayon, s'il te plaît ?", "Donne crayon !", "J'ai un crayon.", "C'est un crayon."]),
         ("Sur le plan, la bibliothèque est :", ["au rez-de-chaussée", "dans la cour", "au 1er étage", "au 2e étage"]),
         ("Sur l'horaire, le lundi, la 1re heure, c'est :", ["le français", "les maths", "la gym", "les sciences"]),
         ("Sur l'horaire, la gym est :", ["dans la cour", "au local 12", "à la bibliothèque", "à la salle de gym"]),
         ("Ce sont ____ élèves.", ["un", "une", "des", "la"]), ("« Lis et souligne. » Je fais :", ["je lis, puis je souligne", "je souligne, puis je découpe", "j'écoute", "je dessine"]),
         ("J'entends le son [y] comme dans « tu » :", ["loup", "rue", "roue", "bonjour"]), ("🔁 15 + 5 =", ["dix-neuf", "quinze", "seize", "vingt"]),
         ("🔁 « Tu as quel âge ? »", ["Je suis 14 ans.", "Il a 14 ans.", "Ça va.", "J'ai 14 ans."])]
    mini = f'<div class="flex top" style="gap:3mm;margin-bottom:2mm"><div class="doc" style="width:128mm;padding:2mm;transform:none">{plan_ecole()}</div><div class="doc" style="padding:2mm;transform:none;font-size:8.5pt;font-family:Inter"><b>Horaire DASPA B · lundi</b><br>8 h 20 Français · L12<br>9 h 10 Français · L12<br>10 h 15 Maths · L14<br>11 h 05 Sciences · Labo<br>12 h 45 Éduc. physique · Gym<br>13 h 35 Éduc. physique · Gym<br>14 h 25 Citoyenneté · L12</div></div>'
    p1 = "".join(qcm_line(i + 1, q, o) for i, (q, o) in enumerate(Q[:12]))
    p2 = "".join(qcm_line(i + 13, q, o) for i, (q, o) in enumerate(Q[12:]))
    b.page(f'{head}<div class="flex" style="justify-content:space-between"><h2 style="margin:0">Partie A · Je choisis la bonne réponse</h2><span class="score">…… / 20</span></div><p class="sm muted">J\'entoure la lettre, puis je noircis le rond sur la feuille de réponses.</p>{p1}', "Test", levels=False)
    b.page(f'{mini}{p2}', "Test", levels=False)
    b.page(f'''<div class="flex" style="justify-content:space-between"><h2 style="margin:0">Partie B · J'écris</h2><span class="score">…… / 10</span></div>
<h3>B1. J'écris un ou une + le mot. (… / 4)</h3><div class="grid4">{"".join(f'<div class="card c"><span class="emo s">{e}</span><div class="line"></div></div>' for e in ["📒", "🧽", "🪑", "🖥️"])}</div>
<h3 class="mt4">B2. Je décris ma classe : 3 phrases avec « il y a ». (… / 3)</h3>{lines(3, True)}
<h3>B3. Je demande poliment un objet à la prof. (… / 3)</h3>{lines(1, True)}
<div class="flex mt4" style="justify-content:space-between"><h2 style="margin:0">Partie C · Je parle avec la prof</h2><span class="score">…… / 10</span></div>
{table(["Je sais…", "Points", "✅"], [["nommer 6 objets de la classe avec un / une", "/ 3", ""], ["dire où sont 3 lieux sur le plan", "/ 3", ""], ["demander mon chemin poliment (jeu de rôle)", "/ 2", ""], ["m'excuser d'être en retard", "/ 2", ""]], ["120mm", "30mm", "32mm"])}
<div class="card mt4 c"><span class="huge">TOTAL : …… / 40</span></div>''', "Test", levels=False)

    ta = f'''<div style="background:#FFD166;margin:-17mm -14mm 4mm -14mm;padding:14mm 14mm 4mm 14mm"><div style="font-size:11pt;font-weight:800">★ ALPHA · 📝 TEST · MODULE 2</div><div style="font-size:22pt;font-weight:800">Mon école</div></div>
<h3>1. J'écoute et j'entoure la syllabe. (… / 4)</h3><div class="grid4">{"".join(f'<div class="card c big" style="font-weight:700;white-space:nowrap">{r}</div>' for r in ["ma mo mi", "la lu li", "sa so su", "ra ri ré"])}</div>
<h3>2. Je lis et je relie. (… / 4)</h3>{relie([f'<b class="big">{w}</b>' for w in ["lama", "mur", "lire", "ami"]], ['<span class="emo s">🙋</span>', '<span class="emo s">🦙</span>', '<span class="emo s">📖</span>', '<span class="emo s">🧱</span>'])}
<h3>3. J'écris la syllabe que la prof dit. (… / 4)</h3>{guide_lines(1, 22)}
<h3>4. Je montre et je nomme (oral). (… / 4)</h3><div class="grid4">{"".join(f'<div class="card c"><span class="emo">{e}</span></div>' for e in ["✏️", "🧽", "📕", "🎒"])}</div>
<h3>5. La prof montre une image : je dis le lieu (oral). (… / 4)</h3><div class="grid4">{"".join(f'<div class="card c"><span class="emo">{e}</span></div>' for e in ["🍽️", "🩺", "📚", "🌳"])}</div>
<div class="card c mt2"><span class="huge">TOTAL : …… / 20</span></div>'''
    b.page(ta, "★ Alpha · Test", levels=False)

    items = ["Je sais nommer 10 objets de la classe.", "Je sais dire un, une, des.", "Je sais dire le, la, l', les.", "Je sais écrire un mot au pluriel (-s).", "Je sais nommer les lieux de l'école.",
             "Je sais lire le plan de l'école.", "Je sais lire mon horaire.", "Je sais dire « il y a ».", "Je sais demander de l'aide poliment.", "Je sais m'excuser.", "Je comprends une consigne à 2 actions.", "★ Je sais lire ma, li, so, ru…"]
    tb = table(["", "😀 Oui !", "🙂 Un peu", "😕 Pas encore", "La prof"], [[x, '<span class="chk"></span>', '<span class="chk"></span>', '<span class="chk"></span>', ""] for x in items], ["92mm", "20mm", "20mm", "24mm", "26mm"])
    b.page(f'<h2>✅ Je sais faire</h2>{tb}<div class="grid2 mt4"><div class="card"><b>Ce que j\'aime dans ce module :</b>{lines(2)}</div><div class="card"><b>C\'est difficile pour moi :</b>{lines(2)}</div></div>', "Je sais faire", levels=False)

    mots = [("✏️", "un crayon"), ("🖊️", "un stylo"), ("📏", "une latte"), ("✂️", "des ciseaux"), ("📒", "un cahier"), ("📕", "un livre"), ("🎒", "un cartable"), ("👝", "un plumier"), ("🧽", "une gomme"),
            ("🪑", "une chaise"), ("🚪", "une porte"), ("🪟", "une fenêtre"), ("🗂️", "le secrétariat"), ("🩺", "l'infirmerie"), ("🍽️", "le réfectoire"), ("🚻", "les toilettes"), ("📚", "la bibliothèque"),
            ("🌳", "la cour"), ("🏀", "la salle de gym"), ("👩‍💼", "la directrice"), ("🧑‍🏫", "l'éducateur"), ("📅", "l'horaire"), ("➗", "les maths"), ("🔬", "les sciences"),
            ("🙏", "s'il vous plaît"), ("😕", "excusez-moi"), ("🤝", "aider"), ("🔁", "prêter"), ("⬅️", "à gauche"), ("➡️", "à droite")]
    half = len(mots) // 2
    mt = lambda lst: table(["", "Français", "Dans ma langue"], [[f'<span style="font-size:13pt">{e}</span>', f"<b>{w}</b>", ""] for e, w in lst], ["12mm", "40mm", "36mm"]).replace("<td>", '<td style="padding:1.6mm 2mm">')
    b.page(f'<h2>📒 Mes mots du module 2</h2><p class="sm">J\'écris le mot dans ma langue.</p><div class="grid2">{mt(mots[:half])}{mt(mots[half:])}</div>', "Mes mots", levels=False)
    return KEY
