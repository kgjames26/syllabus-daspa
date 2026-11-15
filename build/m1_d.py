"""Volume 1 · Module 1 — partie D : tâche finale, révision, test, autoévaluation, lexique."""
from lib.base import *
from lib.art import *

QCM_KEY = "1-D, 2-A, 3-C, 4-B, 5-C, 6-B, 7-A, 8-B, 9-C, 10-D, 11-A, 12-A, 13-B, 14-B, 15-D, 16-C, 17-A, 18-C, 19-B, 20-D"


def bubbles_row(n, filled=None, cross=None):
    out = f'<div class="flex" style="gap:2mm;margin-bottom:1.6mm"><b style="width:7mm">{n}</b>'
    for L in "ABCD":
        st = ""
        inner = L
        if filled == L:
            st = "background:#1F2A44;color:#1F2A44;"
        if cross == L:
            inner = "✗"
        out += f'<span class="bub" style="{st}">{inner}</span>'
    return out + '</div>'


def build_d(b, E):
    # ================= TÂCHE FINALE =================
    steps = [("1", "🎤", "J'interviewe un camarade. Je note ses réponses."), ("2", "✏️", "J'écris sa présentation avec « il » ou « elle »."),
             ("3", "🎨", "Je dessine son portrait."), ("4", "🗣️", "Je le présente à la classe."), ("5", "📌", "On colle les affiches au mur : « Les élèves de notre classe ».")]
    st = "".join(f'<div class="card c"><div style="font-size:18pt;font-weight:800;color:#E4572E">{n}</div><span class="emo s">{e}</span><p class="sm">{t}</p></div>' for n, e, t in steps)
    itw = table(["Ma question", "Sa réponse"], [[q, ""] for q in ["Comment tu t'appelles ?", "Comment tu écris ton prénom ? (il épelle)", "Tu as quel âge ?", "Tu viens d'où ?", "Tu parles quelles langues ?", "Tu habites où ?", "Tu aimes… ? (ma question libre)"]], ["80mm", "102mm"]).replace("<td></td>", '<td style="height:10mm"></td>')
    e1 = E("Étape 1 : l'interview.", itw, ["parle", "ecris", "duo"], 2, "A", sol="Réponses personnelles.")
    b.page(f'''<div style="background:#1F2A44;color:#fff;margin:-17mm -14mm 5mm -14mm;padding:15mm 14mm 5mm 14mm"><div style="font-size:11pt;font-weight:700;opacity:.8">🎯 TÂCHE FINALE</div><div style="font-size:26pt;font-weight:800">Le mur de notre classe</div>
<div class="sm" style="opacity:.9">Je présente un camarade à toute la classe. Ensemble, nous faisons l'affiche « Les élèves de notre classe ».</div></div>
<div class="grid5">{st}</div><div class="mt4">{e1}</div>''', "Tâche finale", levels=False)

    poster = f'''<div style="border:4px solid #E4572E;border-radius:6mm;padding:5mm;background:#FFFDF8">
<div class="flex top"><div style="width:58mm;height:70mm;border:2.5px dashed #9aa1b1;border-radius:4mm;display:flex;align-items:center;justify-content:center" class="muted sm c">le portrait<br>de mon camarade</div>
<div class="grow" style="line-height:2.4;font-size:12.5pt">Voici {blank("l")} !<br>Il / Elle a {blank("s")} ans.<br>Il / Elle vient {blank("l")}.<br>Il / Elle parle {blank("l")}.<br>Il / Elle habite à {blank("l")}.<br>Il / Elle aime {blank("l")}.</div></div></div>'''
    e2 = E("Étapes 2 et 3 : l'affiche de mon camarade.", poster, ["ecris", "dessine"], 2, "C", sol="Production évaluée avec la grille de la tâche finale (livret enseignant).")
    chk = table(["Avant de présenter, je vérifie :", "✅"], [[x, '<span class="chk"></span>'] for x in ["J'ai écrit 5 phrases ou plus.", "J'ai mis une majuscule au début et un point à la fin.", "J'ai utilisé « il » ou « elle ».", "J'ai écrit « Il/Elle a … ans » (avec AVOIR).", "Je sais lire mon affiche à voix haute."]], ["160mm", "22mm"])
    peer = table(["Mon camarade…", "😀", "🙂", "😕"], [[x, '<span class="chk"></span>', '<span class="chk"></span>', '<span class="chk"></span>'] for x in ["parle fort et lentement.", "regarde la classe.", "donne 5 informations.", "dit « il » ou « elle »."]], ["120mm", "20mm", "20mm", "22mm"])
    e2b = E("J'écoute la présentation d'un camarade et je donne mon avis.", '<p class="sm">J\'écoute : ' + blank("l") + ' présente ' + blank("l") + '.</p>' + peer, ["ecoute", "coche"], 2, "A", sol="Co-évaluation : encourager des remarques positives et un conseil précis.")
    b.page(f'{e2}{chk}{e2b}<div class="astuce mt2"><b>Étape 4 · Pour présenter :</b> je me lève, je regarde la classe, je parle fort et lentement. Je commence par « Je vous présente… » et je termine par « Merci ! »</div>', "Tâche finale", levels=False)

    # ================= JE RÉVISE =================
    e3 = E("Je complète la conversation.", f'''<div class="card"><p>— {blank()} ! Je m'appelle Ana. Et toi, comment tu {blank()} ?</p><p>— Je m'appelle Ion. Tu as quel {blank("s")} ?</p>
<p>— J'{blank("s")} 15 ans. Tu viens {blank("s")} ?</p><p>— Je viens {blank("s")} Roumanie. Et toi ?</p><p>— Je viens {blank("s")} Brésil. Au {blank()} !</p></div>''', ["complete"], 2, "C",
           sol="Bonjour (Salut) · t'appelles · âge · ai · d'où · de · du · revoir")
    e4 = E("J'écris les nombres en chiffres.", '<p class="big">quatorze : ___ &nbsp; neuf : ___ &nbsp; dix-sept : ___ &nbsp; onze : ___ &nbsp; vingt : ___ &nbsp; six : ___</p>', ["ecris"], 1, "C",
           sol="14 · 9 · 17 · 11 · 20 · 6")
    e5 = E("Je classe les mots dans le tableau.", '<p class="c">Bonjour · douze · Syrie · Au revoir · seize · Guinée · Salut · trois · Ukraine · Bonsoir · vingt · Maroc</p>' +
           table(["👋 Saluer / dire au revoir", "🔢 Nombres", "🌍 Pays"], [["", "", ""]]).replace("<td></td>", '<td style="height:22mm"></td>'), ["lis", "ecris"], 1, "C",
           sol="Saluer : Bonjour, Au revoir, Salut, Bonsoir · Nombres : douze, seize, trois, vingt · Pays : Syrie, Guinée, Ukraine, Maroc")
    e6 = E("Je mets les lettres dans l'ordre de l'alphabet.", '<p class="big">D · A · C · B → ______ &nbsp;&nbsp; M · O · L · N → ______ &nbsp;&nbsp; T · R · U · S → ______</p>', ["ecris"], 2, "C",
           sol="A B C D · L M N O · R S T U")
    e7 = E("Défi ! Je lis et je trouve les 4 erreurs. Je corrige.", '<div class="card"><p class="big">bonjour ! je m\'appelle Sami. Je suis 13 ans. Je viens du Maroc. J\'ai parle arabe.</p></div>' + lines(2), ["lis", "barre", "ecris"], 3, "C",
           sol="Bonjour (majuscule) · Je (majuscule après le point d'exclamation) · J'ai 13 ans · Je parle arabe")
    b.page(f'<h2>🔁 Je révise tout le module</h2>{e3}{e4}{e5}{e6}{e7}', "Je révise")

    # ================= ENTRAÎNEMENT FEUILLE-RÉPONSE =================
    demo = f'''<div class="grid3">
<div class="card c"><b style="color:#2BA88F">✅ Bien</b><div style="margin-top:2mm">{bubbles_row("1", filled="B")}</div><p class="xs">Je noircis bien le rond.</p></div>
<div class="card c"><b style="color:#E4572E">❌ Pas bien</b><div style="margin-top:2mm">{bubbles_row("1", cross="B")}</div><p class="xs">Une croix : la machine ne lit pas !</p></div>
<div class="card c"><b style="color:#E4572E">❌ Pas bien</b><div style="margin-top:2mm"><div class="flex" style="gap:2mm"><b style="width:7mm">1</b><span class="bub" style="background:#1F2A44"></span><span class="bub" style="background:#1F2A44"></span><span class="bub">C</span><span class="bub">D</span></div></div><p class="xs">Deux réponses : c'est faux.</p></div></div>'''
    e8 = E("Je m'entraîne à remplir une feuille de réponses.", demo + '''<div class="grid2 mt4"><div>
<p><b>1.</b> 2 + 2 = ? &nbsp; A 3 &nbsp; B 4 &nbsp; C 5 &nbsp; D 6</p><p><b>2.</b> 🐱 = ? &nbsp; A un chien &nbsp; B un poisson &nbsp; C un chat &nbsp; D un oiseau</p>
<p><b>3.</b> Le matin, je dis : &nbsp; A Bonjour &nbsp; B Bonne nuit &nbsp; C Bonsoir &nbsp; D Merci</p><p><b>4.</b> La lettre après A : &nbsp; A C &nbsp; B D &nbsp; C Z &nbsp; D B</p><p><b>5.</b> dix = ? &nbsp; A 2 &nbsp; B 6 &nbsp; C 10 &nbsp; D 12</p></div>
<div class="card">''' + "".join(bubbles_row(str(i)) for i in range(1, 6)) + '''</div></div>''', ["lis", "colorie"], 1, "P", sol="1-B, 2-C, 3-A, 4-D, 5-C. Montrer comment effacer (gomme) et vérifier qu'il y a un seul rond noirci par ligne.")
    b.page(f'<span class="tag-doc">🎒 FRANÇAIS DE L\'ÉCOLE</span><h2>Répondre sur une feuille de réponses</h2>{e8}<div class="astuce">Au test, je reçois une feuille spéciale. Je noircis <b>un seul rond</b> par question, avec un crayon ou un stylo noir. Je peux d\'abord entourer la réponse dans le test, puis noircir le rond.</div>', "Consignes & école", levels=False)

    # ================= TEST =================
    head = f'''<div style="background:#1F2A44;color:#fff;margin:-17mm -14mm 4mm -14mm;padding:14mm 14mm 4mm 14mm;display:flex;justify-content:space-between;align-items:flex-end">
<div><div style="font-size:11pt;font-weight:700;opacity:.8">📝 TEST · MODULE 1</div><div style="font-size:24pt;font-weight:800">Bonjour !</div></div>
<div class="sm" style="text-align:right">Prénom : ......................................<br>Date : ........ / ........ / ............</div></div>'''
    Q = [
        ("Le matin, je dis :", ["Bonsoir !", "Bonne nuit !", "Merci !", "Bonjour !"]),
        ("Je pars de l'école. Je dis à la prof :", ["Au revoir, Madame !", "Salut, ça va ?", "Bonjour, Madame !", "Bonne nuit !"]),
        ("« Comment tu t'appelles ? »", ["J'ai 14 ans.", "Je viens du Maroc.", "Je m'appelle Bilal.", "Ça va bien."]),
        ("« Tu as quel âge ? »", ["Je suis 15 ans.", "J'ai 15 ans.", "J'ai Syrie.", "Je m'appelle 15."]),
        ("« Tu viens d'où ? »", ["Je parle peul.", "J'habite à Namur.", "Je viens de Guinée.", "Ça va."]),
        ("Je ____ Daria.", ["ai", "suis", "es", "a"]),
        ("Tu ____ 13 ans.", ["as", "es", "est", "ai"]),
        ("Elle ____ professeure.", ["a", "est", "as", "ai"]),
        ("douze =", ["2", "20", "12", "11"]),
        ("16 =", ["six", "soixante", "dix-six", "seize"]),
        ("8 + 7 =", ["quinze", "quatorze", "dix-sept", "treize"]),
        (f'{picto("ecoute", 28)} =', ["J'écoute.", "J'écris.", "Je lis.", "Je coche."]),
        (f'{picto("entoure", 28)} =', ["Je souligne.", "J'entoure.", "Je relie.", "Je colorie."]),
        (f'{picto("relie", 28)} =', ["Je barre.", "Je relie.", "Je découpe.", "Je regarde."]),
        ("Sur la carte, le <b>prénom</b> de l'élève est :", ["MBALA", "DASPA", "Namur", "Grace"]),
        ("Sur la carte, le <b>NOM</b> de l'élève est :", ["Grace", "Tilleuls", "MBALA", "Athénée"]),
        ("Sur la carte, la <b>classe</b> de l'élève est :", ["DASPA A", "DASPA B", "2013", "Namur"]),
        ("Quelle lettre vient après F ?", ["E", "H", "G", "J"]),
        ("Tu ne comprends pas. Tu dis :", ["Au revoir !", "Vous pouvez répéter, s'il vous plaît ?", "J'ai fini !", "Bonne nuit !"]),
        ("Quelle lettre est une voyelle ?", ["B", "M", "T", "O"]),
    ]
    mini = f'''<div class="doc" style="width:105mm;border-radius:3mm;overflow:hidden;border:1px solid #ccc;font-size:9.5pt;transform:none;margin-bottom:3mm"><div style="background:#1F4E79;color:#fff;padding:1.5mm 3mm;font-weight:700">ATHÉNÉE DES TILLEULS · CARTE D'ÉLÈVE</div>
<div class="flex" style="padding:2mm 3mm;gap:3mm">{avatar("fatou", 50)}<div style="line-height:1.5">NOM : <b>MBALA</b><br>Prénom : <b>Grace</b><br>Née le : <b>21/09/2013</b><br>Classe : <b>DASPA A</b></div></div></div>'''

    def qblock(i, q, o):
        return qcm_line(i, q, o)
    p1 = "".join(qblock(i + 1, q, o) for i, (q, o) in enumerate(Q[:11]))
    p2 = "".join(qblock(i + 12, q, o) for i, (q, o) in enumerate(Q[11:14]))
    p3 = "".join(qblock(i + 15, q, o) for i, (q, o) in enumerate(Q[14:]))
    b.page(f'{head}<div class="flex" style="justify-content:space-between"><h2 style="margin:0">Partie A · Je choisis la bonne réponse</h2><span class="score">…… / 20</span></div><p class="sm muted">J\'entoure la lettre, puis je noircis le rond sur la feuille de réponses.</p>{p1}', "Test", levels=False)
    b.page(f'{p2}{mini}{p3}<div class="cut"></div><p class="sm"><b>Pour la prof :</b> clé QCM dans le livret enseignant.</p>', "Test", levels=False)

    partB = f'''<div class="flex" style="justify-content:space-between"><h2 style="margin:0">Partie B · J'écris</h2><span class="score">…… / 10</span></div>
<h3>B1. J'écris les nombres en lettres. (… / 5)</h3><div class="grid5">{"".join(f'<div class="card c"><b class="big">{n}</b><div class="line"></div></div>' for n in [5, 11, 14, 18, 20])}</div>
<h3 class="mt4">B2. Je me présente en 5 phrases. (… / 5)</h3>{lines(5, True)}
<div class="flex mt4" style="justify-content:space-between"><h2 style="margin:0">Partie C · Je parle avec la prof</h2><span class="score">…… / 10</span></div>
<p class="sm muted">La prof coche pendant que tu parles.</p>
{table(["Je sais…", "Points", "✅"], [["saluer et dire au revoir", "/ 2", ""], ["répondre : nom, âge, pays, langues (4 questions)", "/ 4", ""], ["épeler mon prénom", "/ 2", ""], ["compter de 0 à 20", "/ 2", ""]], ["120mm", "30mm", "32mm"])}
<div class="card mt4 c"><span class="huge">TOTAL : …… / 40</span></div>'''
    b.page(partB, "Test", levels=False)

    # ================= TEST ALPHA =================
    ta = f'''<div style="background:#FFD166;margin:-17mm -14mm 4mm -14mm;padding:14mm 14mm 4mm 14mm;display:flex;justify-content:space-between;align-items:flex-end">
<div><div style="font-size:11pt;font-weight:800">★ ALPHA · 📝 TEST · MODULE 1</div><div style="font-size:22pt;font-weight:800">Bonjour !</div></div><div class="sm">Date : ...... / ...... / ..........</div></div>
<h3>1. J'écris mon prénom. (… / 4)</h3>{guide_lines(1, 24)}
<h3>2. J'écoute et j'entoure la lettre. (… / 4)</h3><div class="grid4">{"".join(f'<div class="card c" style="font-size:20pt;letter-spacing:3mm;font-weight:700">{r}</div>' for r in ["a o i", "u é a", "i u o", "o a é"])}</div>
<h3>3. Je relie. (… / 4)</h3>{relie([f'<b style="font-size:20pt">{x}</b>' for x in "AOUI"], [f'<b style="font-size:20pt">{x}</b>' for x in "iauo"])}
<h3>4. Je compte et j'entoure. (… / 4)</h3><div class="grid4">{"".join(f'<div class="card c"><div style="font-size:16pt">{e*n}</div><p class="big" style="letter-spacing:2mm">{o}</p></div>' for e, n, o in [("🍎", 3, "2 3 6"), ("⭐", 6, "6 9 4"), ("🐟", 8, "3 5 8"), ("🌸", 10, "10 7 1")])}</div>
<h3>5. Je parle avec la prof. (… / 4)</h3>{table(["", "✅"], [["Je dis bonjour / au revoir.", ""], ["Je dis mon prénom.", ""], ["Je dis mon âge.", ""], ["Je dis mon pays.", ""]], ["150mm", "32mm"])}
<div class="card c mt2"><span class="huge">TOTAL : …… / 20</span></div>'''
    b.page(ta, "★ Alpha · Test", levels=False)

    # ================= JE SAIS FAIRE =================
    items = ["Je sais dire bonjour et au revoir.", "Je sais dire mon nom et mon prénom.", "Je sais dire mon âge.", "Je sais dire mon pays et mes langues.",
             "Je sais poser des questions à un camarade.", "Je sais compter de 0 à 20.", "Je sais dire l'alphabet.", "Je sais épeler mon prénom.",
             "Je comprends les consignes (les pictogrammes).", "Je sais remplir une fiche d'inscription.", "Je sais dire : « Je ne comprends pas. »", "★ Je sais écrire mon prénom et les voyelles."]
    tb = table(["", "😀 Oui !", "🙂 Un peu", "😕 Pas encore", "La prof"], [[x, '<span class="chk"></span>', '<span class="chk"></span>', '<span class="chk"></span>', ""] for x in items], ["92mm", "20mm", "20mm", "24mm", "26mm"])
    b.page(f'<h2>✅ Je sais faire</h2><p>Je colorie ou je coche. Je suis honnête : c\'est pour apprendre !</p>{tb}<div class="grid2 mt4"><div class="card"><b>Ce que j\'aime dans ce module :</b>{lines(2)}</div><div class="card"><b>C\'est difficile pour moi :</b>{lines(2)}</div></div>', "Je sais faire", levels=False)

    # ================= MES MOTS =================
    mots = [("👋", "bonjour"), ("👋", "au revoir"), ("😊", "salut"), ("🌆", "bonsoir"), ("🌙", "bonne nuit"), ("🙏", "merci"), ("🙋", "le prénom"), ("👪", "le nom"), ("🎂", "l'âge"), ("🌍", "le pays"),
            ("🗣️", "la langue"), ("🏠", "l'adresse"), ("📞", "le téléphone"), ("👩‍🏫", "la prof"), ("🧑‍🎓", "l'élève"), ("🏫", "l'école"), ("✏️", "un crayon"), ("📒", "un cahier"),
            ("📏", "une latte"), ("👂", "écouter"), ("📖", "lire"), ("✍️", "écrire"), ("🔤", "l'alphabet"), ("🔢", "un nombre"),
            ("🎒", "un cartable"), ("✂️", "des ciseaux"), ("🧽", "une gomme"), ("❓", "une question"), ("💬", "une réponse"), ("🔁", "répéter"),
            ("⭕", "entourer"), ("🔗", "relier"), ("✅", "cocher"), ("🎨", "colorier"), ("🙋", "se présenter"), ("🤷", "je ne comprends pas")]
    half = len(mots) // 2

    def mt(lst):
        return table(["", "Français", "Dans ma langue"], [[f'<span style="font-size:13pt">{e}</span>', f"<b>{w}</b>", ""] for e, w in lst], ["12mm", "40mm", "36mm"]).replace("<td>", '<td style="padding:1.6mm 2mm">')
    b.page(f'<h2>📒 Mes mots du module 1</h2><p class="sm">J\'écris le mot dans ma langue (ou je demande de l\'aide à ma famille).</p><div class="grid2">{mt(mots[:half])}{mt(mots[half:])}</div>', "Mes mots", levels=False)

    return QCM_KEY
