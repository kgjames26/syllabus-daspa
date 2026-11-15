"""Volume 1 · Module 2 « Mon école » — partie A."""
from lib.base import *
from lib.art import *

MC = "#0E9F8E"

OBJ = [("✏️", "un crayon", "m"), ("🖊️", "un stylo", "m"), ("📏", "une latte", "f"), ("✂️", "des ciseaux", "p"), ("📒", "un cahier", "m"), ("📕", "un livre", "m"),
       ("🎒", "un cartable", "m"), ("👝", "un plumier", "m"), ("🧴", "une colle", "f"), ("📄", "une feuille", "f"), ("🧽", "une gomme", "f"), ("🖍️", "des marqueurs", "p"),
       ("🪑", "une chaise", "f"), ("🖥️", "un ordinateur", "m"), ("🗑️", "une poubelle", "f"), ("🕐", "une horloge", "f"), ("🚪", "une porte", "f"), ("🪟", "une fenêtre", "f"),
       ("📐", "une équerre", "f"), ("🧮", "une calculatrice", "f"), ("📓", "un classeur", "m"), ("🗺️", "une carte", "f"), ("💡", "une lampe", "f"), ("🧷", "une agrafeuse", "f")]

LIEUX = [("🏫", "l'entrée"), ("🗂️", "le secrétariat"), ("👩‍💼", "le bureau de la directrice"), ("🩺", "l'infirmerie"), ("🍽️", "le réfectoire"), ("🚻", "les toilettes"),
         ("🏀", "la salle de gym"), ("🌳", "la cour de récréation"), ("📚", "la bibliothèque"), ("💻", "le local informatique"), ("☕", "la salle des profs"), ("🪜", "l'escalier"),
         ("🧑‍🏫", "la classe (le local)"), ("🔬", "le laboratoire"), ("🚲", "le parking vélos"), ("🚶", "le couloir")]


def plan_ecole(width="100%"):
    def room(x, y, w, h, label, n="", fill="#fff"):
        lab = label.split("|")
        t = "".join(f'<text x="{x+w/2}" y="{y+h/2+(i-(len(lab)-1)/2)*4.2+1.4}" font-size="3.4" text-anchor="middle" font-family="Poppins" font-weight="600">{l}</text>' for i, l in enumerate(lab))
        num = f'<circle cx="{x+4}" cy="{y+4}" r="2.6" fill="{MC}"/><text x="{x+4}" y="{y+5.2}" font-size="3" fill="#fff" text-anchor="middle" font-family="Poppins" font-weight="700">{n}</text>' if n else ""
        return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="#1F2A44" stroke-width=".6"/>{t}{num}'
    g = []
    # rez-de-chaussée
    g.append('<text x="2" y="6" font-size="4.6" font-family="Poppins" font-weight="800">REZ-DE-CHAUSSÉE</text>')
    oy = 9
    g += [room(2, oy, 26, 20, "Secrétariat", "1", "#E8F6F2"), room(28, oy, 26, 20, "Bureau de la|directrice", "2", "#E8F6F2"), room(54, oy, 20, 20, "Infirmerie", "3", "#FDECE7"),
          room(74, oy, 14, 20, "Toilettes", "4", "#EEF1F6"), room(2, oy + 20, 52, 10, "couloir", "", "#FAFAFA"), room(54, oy + 20, 34, 10, "escalier ↗", "", "#FAFAFA"),
          room(2, oy + 30, 40, 22, "Réfectoire", "5", "#FFF3C4"), room(42, oy + 30, 46, 22, "Salle de gym", "6", "#E1EAFB")]
    g.append(f'<path d="M20 {oy+52} L28 {oy+52}" stroke="#E4572E" stroke-width="2.2"/><text x="24" y="{oy+57}" font-size="3.2" text-anchor="middle" font-family="Poppins" fill="#E4572E" font-weight="700">ENTRÉE ⬆</text>')
    g.append(f'<rect x="2" y="{oy+61}" width="86" height="16" rx="2" fill="#DDF3EC" stroke="#2BA88F" stroke-width=".5"/><text x="45" y="{oy+71}" font-size="3.6" text-anchor="middle" font-family="Poppins" font-weight="600">🌳 Cour de récréation 🌳 · 🚲 parking vélos</text>')
    # 1er étage
    ox = 96
    g.append(f'<text x="{ox}" y="6" font-size="4.6" font-family="Poppins" font-weight="800">1er ÉTAGE</text>')
    g += [room(ox, oy, 22, 20, "Local 11", "7"), room(ox + 22, oy, 22, 20, "Local 12|DASPA B", "8", "#FFE5DC"), room(ox + 44, oy, 22, 20, "Local 13", "9"),
          room(ox + 66, oy, 16, 20, "Toilettes", "10", "#EEF1F6"), room(ox, oy + 20, 66, 10, "couloir", "", "#FAFAFA"), room(ox + 66, oy + 20, 16, 10, "escalier", "", "#FAFAFA"),
          room(ox, oy + 30, 22, 22, "Local 14", "11"), room(ox + 22, oy + 30, 26, 22, "Bibliothèque", "12", "#EEE3FC"), room(ox + 48, oy + 30, 18, 22, "Labo|sciences", "13", "#E1EAFB"),
          room(ox + 66, oy + 30, 16, 22, "Salle|des profs", "14", "#FFF3C4"), room(ox, oy + 52, 40, 14, "Local informatique", "15", "#E8F6F2")]
    return f'<svg viewBox="0 0 182 88" width="{width}">{"".join(g)}</svg>'


def classe_scene(width="100%"):
    s = ['<svg viewBox="0 0 180 100">', '<rect x="0" y="0" width="180" height="100" fill="#FDF6E9"/><rect x="0" y="70" width="180" height="30" fill="#E9D8B9"/>',
         '<rect x="50" y="8" width="80" height="34" rx="2" fill="#2F5D50" stroke="#8a6b47" stroke-width="2"/><text x="90" y="28" font-size="7" fill="#fff" text-anchor="middle" font-family="Poppins">Mon école</text>']
    for x in (6, 150):
        s.append(f'<rect x="{x}" y="10" width="24" height="28" fill="#BFE3F7" stroke="#8a6b47" stroke-width="1.6"/><path d="M{x+12} 10 V38 M{x} 24 H{x+24}" stroke="#8a6b47" stroke-width="1.2"/>')
    s.append('<circle cx="140" cy="16" r="5" fill="#fff" stroke="#1F2A44" stroke-width="1"/><path d="M140 16 L140 12.5 M140 16 L142.5 17" stroke="#1F2A44" stroke-width=".8"/>')
    for i in range(4):  # tables
        x = 16 + i * 40
        s.append(f'<rect x="{x}" y="62" width="30" height="5" rx="1" fill="#C68A5E"/><rect x="{x+2}" y="67" width="2" height="14" fill="#8a6b47"/><rect x="{x+26}" y="67" width="2" height="14" fill="#8a6b47"/>')
    for i in range(6):  # chaises
        x = 12 + i * 27
        s.append(f'<rect x="{x}" y="74" width="10" height="2" fill="#4A7BD1"/><rect x="{x}" y="64" width="2" height="12" fill="#4A7BD1"/><rect x="{x}" y="76" width="1.5" height="10" fill="#4A7BD1"/><rect x="{x+8.5}" y="76" width="1.5" height="10" fill="#4A7BD1"/>')
    s.append('<text x="152" y="66" font-size="14">🪴</text><text x="2" y="96" font-size="9">🗑️</text><text x="62" y="60" font-size="9">🖥️</text>')
    for x in (100, 112, 124):
        s.append(f'<text x="{x}" y="97" font-size="9">🎒</text>')
    for x in (24, 30):
        s.append(f'<text x="{x}" y="61" font-size="7">📕</text>')
    s.append('</svg>')
    return "".join(s).replace('<svg viewBox="0 0 180 100">', f'<svg viewBox="0 0 180 100" width="{width}">')


def build_a(b, E):
    # ================= OUVERTURE =================
    obj = [("🎒", "nommer les objets de la classe"), ("🏫", "nommer les lieux de l'école"), ("🧑‍🏫", "connaître les personnes de l'école"),
           ("🗺️", "lire le plan de l'école et mon horaire"), ("🙏", "demander de l'aide, m'excuser"), ("📝", "dire un, une, des, le, la, les")]
    objs = "".join(f'<div class="flex mb2"><span class="emo s">{e}</span><span class="big">{t}</span></div>' for e, t in obj)
    b.page(f'''
<div style="background:{MC};color:#fff;margin:-17mm -14mm 6mm -14mm;padding:16mm 14mm 6mm 14mm">
 <div style="font-size:13pt;font-weight:700;opacity:.9">MODULE 2</div><div style="font-size:44pt;font-weight:800;line-height:1">Mon école</div></div>
<div class="card" style="padding:2mm">{classe_scene()}</div>
<div class="grid2 mt4"><div><h2>Je vais apprendre à…</h2>{objs}</div>
<div><div class="card" style="background:#E8F6F2;border-color:#A8DED3"><h3 style="margin-top:0">🗣️ On parle ensemble</h3>
<p>Regarde l'image. Qu'est-ce qu'il y a dans la classe ?</p><p>Ton école dans ton pays, c'était comment ?</p><p>Qu'est-ce qui est différent ici ?</p></div>
<div class="card mt4"><h3 style="margin-top:0">🔑 Les mots-clés</h3>{"".join(f'<span class="pill">{w}</span>' for w in ["la classe", "le cartable", "la cour", "l'infirmerie", "le réfectoire", "la bibliothèque", "l'horaire", "il y a", "excusez-moi", "s'il vous plaît"])}</div></div></div>''', "Ouverture", levels=False)
    b.page("%%PLAN_DE_TRAVAIL%%", "Mon plan de travail", levels=False)

    # ================= BD : VISITE =================
    def case(n, inner):
        return f'<div style="border:2.5px solid #1F2A44;border-radius:3mm;min-height:66mm;position:relative;padding:3mm;background:#FFFDF8"><div style="position:absolute;top:2mm;left:2mm;background:#1F2A44;color:#fff;width:6mm;height:6mm;border-radius:50%;font-size:9pt;font-weight:700;display:flex;align-items:center;justify-content:center">{n}</div>{inner}</div>'

    def bub(t):
        return f'<div class="bubble" style="margin:0 0 2mm 0;font-size:11pt">{t}</div>'

    def lr(a, ta, bb, tb, ma="sourire", mb="sourire"):
        return (f'<div class="flex top" style="margin-top:5mm">{avatar(a, 76, ma)}<div>{"".join(bub(x) for x in ta)}</div></div>'
                f'<div class="flex top" style="justify-content:flex-end">{"".join(bub(x) for x in tb)}{avatar(bb, 76, mb, flip=True)}</div>')
    bd = '<div class="grid2" style="gap:3mm">' + "".join([
        case(1, lr("educ", ["Bonjour Daria ! Je suis Monsieur Diallo, l'éducateur.", "Je te fais visiter l'école."], "daria", ["Merci, Monsieur !"], "rire")),
        case(2, f'<div class="flex top" style="margin-top:5mm">{avatar("educ", 76)}<div>{bub("Ici, c&#39;est le secrétariat.")}{bub("Et là, c&#39;est l&#39;infirmerie. Si tu as mal, tu viens ici.")}</div></div><div class="c" style="font-size:30pt">🗂️ 🩺</div>'),
        case(3, lr("daria", ["Excusez-moi, où sont les toilettes ?"], "educ", ["Les toilettes sont à droite, à côté de l'escalier."], "pense")),
        case(4, f'<div class="flex top" style="margin-top:5mm">{avatar("educ", 76, "rire")}<div>{bub("Voici le réfectoire. On mange ici à midi.")}{bub("Et là, il y a la cour de récréation.")}</div></div><div class="c" style="font-size:30pt">🍽️ 🌳</div>'),
        case(5, lr("daria", ["Et la bibliothèque, elle est où ?"], "educ", ["Au premier étage, à côté du local 12. C'est ta classe !"])),
        case(6, lr("amina", ["Salut Daria ! Bienvenue dans la classe !", "Tu as besoin d'un crayon ?"], "daria", ["Oui, merci ! Tu es gentille !"], "rire", "rire")),
    ]) + '</div>'
    e1 = E("J'écoute et je regarde la BD : Daria visite l'école.", bd, ["ecoute", "regarde"], 1, "A",
           script="Lire la BD deux fois en changeant de voix. 1re écoute : suivre du doigt. 2e écoute : pause après chaque bulle, montrer le lieu sur le plan de l'école (p. suivante du document). Faire répéter « Excusez-moi, où sont les toilettes ? ».",
           sol="Activité orale.")
    b.page(f'<h2>Découvrir · La visite de l\'école</h2>{e1}', "Découvrir")

    e2 = E("Où est-ce ? Je relie la phrase et le lieu.", relie(["Si tu as mal, tu viens ici.", "On mange ici à midi.", "C'est au premier étage, à côté du local 12.", "C'est à droite, à côté de l'escalier."],
           ["les toilettes", "la bibliothèque", "l'infirmerie", "le réfectoire"]), ["lis", "relie"], 1, "B",
           sol="mal → l'infirmerie · manger → le réfectoire · 1er étage → la bibliothèque · à droite de l'escalier → les toilettes")
    e3 = E("Vrai ou faux ? Je coche.", table(["", "Vrai", "Faux"], [[x, '<span class="chk"></span>', '<span class="chk"></span>'] for x in ["M. Diallo est le directeur.", "Daria visite l'école.", "La classe de Daria est le local 12.", "La bibliothèque est au rez-de-chaussée.", "Amina prête un crayon à Daria."]], ["130mm", "25mm", "25mm"]),
           ["lis", "coche"], 2, "B", sol="1. Faux (l'éducateur) — 2. Vrai — 3. Vrai — 4. Faux (1er étage) — 5. Vrai")
    e4 = E("Je complète avec les mots de la BD.", f'''<p>1. Daria demande : « {blank("l")}, où sont les toilettes ? »</p><p>2. M. Diallo est l'{blank()}.</p><p>3. Amina dit : « {blank()} dans la classe ! »</p><p>4. Daria répond : « Oui, {blank()} ! »</p>''',
           ["complete", "ecris"], 2, "C", sol="1. Excusez-moi — 2. éducateur — 3. Bienvenue — 4. merci")
    e5 = E("Défi ! Je joue la scène 3 avec un camarade. Puis je demande un autre lieu.", '<p class="sm">« Excusez-moi, où est … ? » — « … est à droite / à gauche / au premier étage. »</p>', ["parle", "duo"], 3, "A",
           sol="Production orale libre ; vérifier « où est » (singulier) / « où sont » (pluriel : les toilettes).")
    b.page(f'{e2}{e3}{e4}{e5}', "Découvrir")

    # ================= OBJETS =================
    oc = "".join(f'<div class="card c" style="padding:2mm"><span class="emo">{e}</span><div class="word" style="font-size:10.5pt">{w}</div></div>' for e, w, g in OBJ)
    e6 = E("Les objets de la classe. J'écoute et je répète.", f'<div class="grid6">{oc}</div>', ["ecoute", "repete"], 1, "A",
           script="Montrer l'objet réel ou l'image, dire le mot avec l'article, faire répéter. Jeu « Kim » : cacher un objet, les élèves disent ce qui manque. Insister sur l'article : UN crayon, UNE gomme.",
           sol="Activité orale.")
    e7 = E("Je montre et je demande à mon voisin : « Qu'est-ce que c'est ? » Il répond : « C'est un… / C'est une… ».", '', ["parle", "duo"], 1, "A", sol="Production orale ; vérifier l'article.")
    e7b = E("J'écris le mot sous l'image (sans regarder !). Puis je vérifie.", '<div class="grid6">' + "".join(f'<div class="card c"><span class="emo">{e}</span><div class="line"></div></div>' for e in ["🧮", "🗑️", "🕐", "📐", "📓", "🗺️"]) + '</div>',
              ["ecris"], 2, "C", sol="une calculatrice · une poubelle · une horloge · une équerre · un classeur · une carte")
    e7c = E("Jacques a dit… La prof donne un ordre : je montre l'objet dans la classe.", '<p class="sm">« Montrez la porte ! » « Levez votre cahier ! » « Touchez la fenêtre ! » « Prenez un crayon ! »</p>', ["ecoute", "montre"], 1, "P",
              script="Donner des ordres rapides : Montrez la porte ! Levez votre cahier ! Touchez la fenêtre ! Prenez un crayon ! Montrez l'horloge ! Ouvrez votre plumier ! Variante « Jacques a dit » : on ne bouge que si l'ordre commence par « Jacques a dit ».",
              sol="Activité gestuelle.")
    b.page(f'<h2>Les objets de la classe</h2>{e6}{e7}{e7b}{e7c}', "Lexique")

    # ================= LEÇON 1 un/une/des =================
    l1 = lecon("Un, une, des", f'''
<div class="grid3">
<div class="card c" style="background:#fff;border-color:#4A7BD1"><b style="color:#4A7BD1;font-size:16pt">un</b><p class="sm">masculin · 1</p><p>un crayon ✏️<br>un livre 📕<br>un cahier 📒</p></div>
<div class="card c" style="background:#fff;border-color:#C94F7C"><b style="color:#C94F7C;font-size:16pt">une</b><p class="sm">féminin · 1</p><p>une gomme 🧽<br>une latte 📏<br>une chaise 🪑</p></div>
<div class="card c" style="background:#fff;border-color:#2BA88F"><b style="color:#2BA88F;font-size:16pt">des</b><p class="sm">pluriel · 2, 3, 4…</p><p>des crayons ✏️✏️<br>des gommes 🧽🧽<br>des ciseaux ✂️</p></div></div>
<p class="mt2"><b>C'est</b> un crayon. <b>C'est</b> une gomme. → 1 objet<br><b>Ce sont</b> des crayons. → 2, 3, 4… objets</p>
<div class="astuce" style="margin-bottom:0"><b>Astuce :</b> j'apprends toujours le mot <b>avec</b> son petit mot : <i>une</i> gomme, <i>un</i> cahier. Dans mon cahier, j'écris les mots masculins en <span style="color:#4A7BD1;font-weight:700">bleu</span> et les mots féminins en <span style="color:#C94F7C;font-weight:700">rose</span>.</div>''')
    e8 = E("J'écoute : un ou une ? Je coche.", table(["", "1", "2", "3", "4", "5", "6", "7", "8"], [["un"] + ['<span class="chk"></span>'] * 8, ["une"] + ['<span class="chk"></span>'] * 8], ["20mm"] + ["20mm"] * 8),
           ["ecoute", "coche"], 1, "A", script="Lire deux fois : 1. une chaise — 2. un stylo — 3. une porte — 4. un cartable — 5. une fenêtre — 6. un livre — 7. une calculatrice — 8. un ordinateur",
           sol="1. une — 2. un — 3. une — 4. un — 5. une — 6. un — 7. une — 8. un")
    b.page(f'{l1}{e8}', "Leçon 1")

    sel = [("✏️", "crayon"), ("🧽", "gomme"), ("📕", "livre"), ("🪑", "chaise"), ("🚪", "porte"), ("📒", "cahier"), ("🗑️", "poubelle"), ("🎒", "cartable")]
    e9 = E("Je classe les mots : un ou une ?", '<p class="c big">' + " · ".join(w for _, w in sel) + '</p>' + table(["un (masculin)", "une (féminin)"], [["", ""]], ["91mm", "91mm"]).replace("<td></td>", '<td style="height:22mm"></td>'),
           ["lis", "ecris"], 1, "C", sol="un : crayon, livre, cahier, cartable · une : gomme, chaise, porte, poubelle")
    e10 = E("J'écris un, une ou des.", '<div class="grid4">' + "".join(f'<div class="card c"><span class="emo s">{e}</span><p>{blank("s")} {w}</p></div>' for e, w in [("📏", "latte"), ("✂️", "ciseaux"), ("📒", "cahier"), ("🖍️", "marqueurs"), ("🕐", "horloge"), ("🖥️", "ordinateur"), ("📄📄📄", "feuilles"), ("🪟", "fenêtre")]) + '</div>',
            ["complete"], 2, "C", sol="une latte · des ciseaux · un cahier · des marqueurs · une horloge · un ordinateur · des feuilles · une fenêtre")
    e11 = E("C'est ou ce sont ? Je complète.", f'''<div class="grid2"><p>1. {blank()} un stylo.</p><p>2. {blank()} des livres.</p><p>3. {blank()} une chaise.</p><p>4. {blank()} des ciseaux.</p></div>''', ["complete"], 2, "C",
            sol="1. C'est — 2. Ce sont — 3. C'est — 4. Ce sont")
    e12 = E("Défi ! Je dessine 4 objets de mon cartable et j'écris : « C'est un… / Ce sont des… ».", '<div class="grid4">' + '<div class="card" style="height:30mm"></div>' * 4 + '</div>' + lines(2), ["dessine", "ecris"], 3, "C",
            sol="Réponses personnelles.")
    b.page(f'{e9}{e10}{e11}{e12}', "S'entraîner")

    # ================= LEÇON 2 le/la/les =================
    l2 = lecon("Le, la, l', les · le pluriel", f'''
<table class="t" style="background:#fff"><tr><th></th><th>Un objet (on ne sait pas lequel)</th><th>L'objet précis</th></tr>
<tr><td><b style="color:#4A7BD1">masculin</b></td><td>un cahier</td><td><b>le</b> cahier de Mateo</td></tr>
<tr><td><b style="color:#C94F7C">féminin</b></td><td>une gomme</td><td><b>la</b> gomme d'Amina</td></tr>
<tr><td>devant a, e, i, o, u, h</td><td>un ordinateur · une horloge</td><td><b>l'</b>ordinateur · <b>l'</b>horloge</td></tr>
<tr><td><b style="color:#2BA88F">pluriel</b></td><td>des livres</td><td><b>les</b> livres de la classe</td></tr></table>
<div class="grid2 mt2"><div class="card" style="background:#fff"><b>Le pluriel : j'ajoute -s</b><p>un livre → des livre<b style="color:#E4572E">s</b><br>la chaise → les chaise<b style="color:#E4572E">s</b></p><p class="sm muted">Le -s ne se prononce pas ! 🤫</p></div>
<div class="card" style="background:#fff"><b>Attention</b><p class="sm">un ciseau → des ciseau<b>x</b> (avec -x)<br>un bureau → des bureau<b>x</b></p></div></div>''')
    e13 = E("J'écris le, la ou l'.", '<div class="grid3">' + "".join(f'<p class="big">{blank("s")} {w}</p>' for w in ["tableau", "porte", "école", "cartable", "infirmerie", "classe", "horloge", "bureau", "cour"]) + '</div>', ["complete"], 1, "C",
            sol="le tableau · la porte · l'école · le cartable · l'infirmerie · la classe · l'horloge · le bureau · la cour")
    e13b = E("J'écoute : un objet ou plusieurs objets ? Je coche.", table(["", "1", "2", "3", "4", "5", "6"], [["1 objet (le, la)"] + ['<span class="chk"></span>'] * 6, ["plusieurs (les)"] + ['<span class="chk"></span>'] * 6], ["40mm"] + ["22mm"] * 6),
              ["ecoute", "coche"], 2, "A", script="Lire deux fois : 1. les cahiers — 2. le livre — 3. la porte — 4. les fenêtres — 5. les élèves — 6. l'horloge. Faire remarquer : on n'entend pas le -s, c'est le petit mot (le / les) qui donne l'information.",
              sol="1. plusieurs — 2. 1 — 3. 1 — 4. plusieurs — 5. plusieurs — 6. 1")
    b.page(f'{l2}{e13}{e13b}', "Leçon 2")

    e14 = E("J'écris au pluriel.", '<div class="grid2">' + "".join(f'<p>{a} → {blank("l")}</p>' for a in ["un crayon", "une gomme", "le livre", "la chaise", "l'élève", "le bureau"]) + '</div>', ["ecris"], 2, "C",
            sol="des crayons · des gommes · les livres · les chaises · les élèves · les bureaux")
    e15 = E("Un ou le ? J'entoure.", '''<p>1. Dans mon cartable, il y a <b>un / le</b> livre.</p><p>2. <b>Un / Le</b> livre de Mateo est rouge.</p><p>3. J'ai <b>une / la</b> gomme.</p><p>4. <b>Une / La</b> gomme d'Amina est blanche.</p>''',
            ["entoure"], 3, "C", sol="1. un — 2. Le — 3. une — 4. La (objet précis : « de Mateo », « d'Amina »)")
    e16 = E("Le jeu de Kim. La prof met 8 objets sur la table. Je regarde 30 secondes. La prof cache un objet. Qu'est-ce qui manque ?", '<p>Il manque {} !</p>'.format(blank("l")), ["regarde", "parle", "groupe"], 1, "D",
            sol="Jeu oral : « Il manque la gomme ! » — accepter un/une au départ, puis exiger le/la.")
    e16b = E("Défi ! Je regarde dans la classe et j'écris 4 phrases : « Le tableau est vert. Les chaises sont bleues… »", lines(4), ["regarde", "ecris"], 3, "C",
              sol="Production libre ; vérifier le/la/les et le pluriel (sont).")
    b.page(f'{e14}{e15}{e16}{e16b}', "S'entraîner")

    # ================= LIEUX =================
    lc = "".join(f'<div class="card c" style="padding:2mm"><span class="emo">{e}</span><div class="word" style="font-size:10pt">{w}</div></div>' for e, w in LIEUX)
    e17 = E("Les lieux de l'école. J'écoute et je répète.", f'<div class="grid4">{lc}</div>', ["ecoute", "repete"], 1, "A",
            script="Montrer chaque image, dire le mot avec l'article, faire répéter. Si possible, faire la visite réelle de l'école avec le livre : les élèves montrent la bonne image devant chaque lieu.",
            sol="Activité orale (visite de l'école recommandée).")
    e17b = E("Je relie le lieu et l'action.", relie(["la bibliothèque", "la cour", "le réfectoire", "la salle de gym", "l'infirmerie"], ["on joue dehors", "on se soigne", "on mange", "on lit", "on fait du sport"]), ["relie"], 1, "B",
              sol="bibliothèque → on lit · cour → on joue dehors · réfectoire → on mange · salle de gym → on fait du sport · infirmerie → on se soigne")
    b.page(f'<h2>Les lieux de l\'école</h2>{e17}{e17b}<div class="astuce">🇧🇪 En Belgique, on dit souvent <b>le local</b> pour la salle de classe : « On a cours au local 12. » On dit aussi <b>le réfectoire</b> pour la cantine.</div>', "Lexique")

    # ================= DOCUMENT : PLAN =================
    e18 = E("Je regarde le plan. Je trouve le numéro.", f'''<div class="grid2"><p>la bibliothèque : n° {blank("s")}</p><p>l'infirmerie : n° {blank("s")}</p><p>le réfectoire : n° {blank("s")}</p><p>la classe DASPA B : n° {blank("s")}</p><p>la salle des profs : n° {blank("s")}</p><p>le secrétariat : n° {blank("s")}</p></div>''',
            ["regarde", "ecris"], 1, "B", sol="bibliothèque 12 · infirmerie 3 · réfectoire 5 · DASPA B 8 · salle des profs 14 · secrétariat 1")
    b.page(f'<span class="tag-doc">📄 DOCUMENT DE LA VIE</span><h2>Le plan de l\'école</h2><div class="doc" style="padding:4mm;transform:none">{plan_ecole()}</div><div class="mt4">{e18}</div>', "Document de la vie")

    e19 = E("Rez-de-chaussée ou 1er étage ? Je coche.", table(["", "Rez-de-chaussée", "1er étage"], [[x, '<span class="chk"></span>', '<span class="chk"></span>'] for x in ["la salle de gym", "le laboratoire", "l'infirmerie", "le local informatique", "le bureau de la directrice", "la bibliothèque"]], ["90mm", "45mm", "45mm"]),
            ["lis", "coche"], 1, "B", sol="RDC : salle de gym, infirmerie, bureau de la directrice · 1er : laboratoire, local informatique, bibliothèque")
    e20 = E("Où vais-je ? Je lis la situation et j'écris le lieu.", '<div class="grid2">' + "".join(f'<div class="card"><p class="sm">{t}</p><p>→ {blank("l")}</p></div>' for t in ["J'ai mal à la tête.", "C'est midi, j'ai faim.", "Je veux emprunter un livre.", "J'ai cours de sport.", "Je dois donner un papier à l'école.", "C'est la récréation."]) + '</div>',
            ["lis", "ecris"], 2, "C", sol="l'infirmerie · le réfectoire · la bibliothèque · la salle de gym · le secrétariat · la cour de récréation")
    e21 = E("Défi ! Je dessine le plan de MON école (ou de ma classe) et j'écris le nom des lieux.", '<div class="card" style="height:50mm"></div>', ["dessine", "ecris"], 3, "C", sol="Production personnelle.")
    b.page(f'{e19}{e20}{e21}', "Document de la vie")

    # ================= LEÇON 3 il y a =================
    l3 = lecon("Il y a… · Où est… ? Où sont… ?", f'''
<div class="grid2"><div>
<p><b>Il y a</b> + un / une / des…</p><p>Dans la classe, <b>il y a</b> un tableau.</p><p><b>Il y a</b> des chaises.</p>
<p class="mt2"><b>Il n'y a pas de</b> …</p><p>Il n'y a pas <b>de</b> piscine. 🚫🏊</p></div>
<div><p><b>Où est</b> la bibliothèque ? → 1 lieu</p><p><b>Où sont</b> les toilettes ? → pluriel</p>
<p class="mt2">— Elle est <b>au premier étage</b>.<br>— Ils sont <b>au rez-de-chaussée</b>.<br>— C'est <b>à gauche</b> ⬅️ / <b>à droite</b> ➡️.</p></div></div>
<div class="attention" style="margin-bottom:0">« Il y a » ne change pas : <b>il y a</b> un livre, <b>il y a</b> des livres ✅ (jamais « ils y ont »).</div>''')
    e22 = E("Je regarde la classe. Je compte et je complète.", f'''<div class="grid2"><p>Il y a {blank("s")} tableau.</p><p>Il y a {blank("s")} fenêtres.</p><p>Il y a {blank("s")} tables.</p><p>Il y a {blank("s")} chaises.</p><p>Il y a {blank("s")} cartables.</p><p>Il y a {blank("s")} ordinateur.</p></div>''',
            ["regarde", "complete"], 1, "B", sol="un (1) tableau · deux fenêtres · quatre tables · six chaises · trois cartables · un ordinateur")
    b.page(f'{l3}<div class="card" style="padding:2mm;width:120mm;margin:0 auto 4mm auto">{classe_scene()}</div>{e22}', "Leçon 3")

    e23 = E("Dans notre école, il y a… / il n'y a pas de… Je coche et j'écris 3 phrases.", '<div class="grid4">' + "".join(f'<div class="card c"><span class="emo s">{e}</span><div class="xs">{w}</div><span class="chk"></span>oui <span class="chk"></span>non</div>' for e, w in [("🏊", "une piscine"), ("📚", "une bibliothèque"), ("🍽️", "un réfectoire"), ("⚽", "un terrain de foot"), ("💻", "des ordinateurs"), ("🛗", "un ascenseur"), ("🌳", "des arbres"), ("🎭", "un théâtre")]) + '</div>' + lines(3),
            ["coche", "ecris"], 2, "C", sol="Réponses selon l'école. Modèle : Il y a une bibliothèque. Il n'y a pas de piscine.")
    e24 = E("Où est… ? Où sont… ? Je complète.", f'''<p>1. {blank()} le secrétariat ? — Il est au rez-de-chaussée.</p><p>2. {blank()} les toilettes ? — Elles sont à droite.</p><p>3. {blank()} la classe DASPA B ? — C'est le local 12.</p><p>4. {blank()} les élèves ? — Ils sont dans la cour.</p>''',
            ["complete"], 2, "C", sol="1. Où est — 2. Où sont — 3. Où est — 4. Où sont")
    e25 = E("Défi ! Le jeu du guide : je choisis un lieu sur le plan. Mon camarade pose des questions pour trouver (« C'est au premier étage ? Il y a des livres ? »). Je réponds oui ou non.", '', ["joue", "parle", "duo"], 3, "D",
            sol="Jeu oral de devinettes.")
    b.page(f'{e23}{e24}{e25}', "S'entraîner")
