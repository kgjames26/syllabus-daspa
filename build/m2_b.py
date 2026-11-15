"""Volume 1 · Module 2 « Mon école » — partie B."""
from lib.base import *
from lib.art import *
from lib.alpha import AL, letter_page, syll_table, slide
from build.m2_a import MC, OBJ, LIEUX, plan_ecole, classe_scene

HEURES = ["8 h 20", "9 h 10", "10 h 15", "11 h 05", "12 h 45", "13 h 35", "14 h 25"]
COL = {"Français": "#FFE5DC", "Maths": "#E1EAFB", "Sciences": "#DDF3EC", "Éduc. physique": "#FFF3C4", "Citoyenneté": "#EEE3FC", "Informatique": "#E8F6F2",
       "Géographie": "#F3E8D8", "Histoire": "#F3E8D8", "Arts": "#FCE4EC", "Musique": "#FCE4EC", "Néerlandais": "#E0F2F1", "Bibliothèque": "#EEE3FC"}
LOC = {"Français": "L12", "Maths": "L14", "Sciences": "Labo", "Éduc. physique": "Gym", "Citoyenneté": "L12", "Informatique": "L15", "Géographie": "L12", "Histoire": "L12",
       "Arts": "L12", "Musique": "L11", "Néerlandais": "L13", "Bibliothèque": "Biblio"}
HOR = {"Lundi": ["Français", "Français", "Maths", "Sciences", "Éduc. physique", "Éduc. physique", "Citoyenneté"],
       "Mardi": ["Maths", "Français", "Français", "Informatique", "Géographie", "Histoire", "Arts"],
       "Mercredi": ["Français", "Maths", "Sciences", "Néerlandais", "", "", ""],
       "Jeudi": ["Français", "Français", "Bibliothèque", "Maths", "Éduc. physique", "Musique", "Français"],
       "Vendredi": ["Maths", "Français", "Sciences", "Informatique", "Français", "Citoyenneté", ""]}


def horaire_html():
    days = list(HOR)
    h = '<table style="border-collapse:collapse;width:100%;font-size:8.6pt;font-family:Inter"><tr><th style="background:#1F2A44;color:#fff;padding:1.5mm">Heure</th>' + "".join(f'<th style="background:#1F2A44;color:#fff;padding:1.5mm">{d}</th>' for d in days) + '</tr>'
    for i, hr in enumerate(HEURES):
        if i == 2:
            h += '<tr><td colspan="6" style="text-align:center;background:#DDF3EC;font-size:8pt;padding:.8mm">☕ récréation 10 h 00 – 10 h 15</td></tr>'
        if i == 4:
            h += '<tr><td colspan="6" style="text-align:center;background:#FFF3C4;font-size:8pt;padding:.8mm">🍽️ temps de midi 11 h 55 – 12 h 45</td></tr>'
        h += f'<tr><td style="border:1px solid #ccd;padding:1.4mm;font-weight:700;white-space:nowrap">{hr}</td>'
        for d in days:
            c = HOR[d][i]
            if c:
                h += f'<td style="border:1px solid #ccd;padding:1.4mm;background:{COL[c]}"><b>{c}</b><br><span style="color:#667">{LOC[c]}</span></td>'
            else:
                h += '<td style="border:1px solid #ccd;background:repeating-linear-gradient(45deg,#f4f4f4,#f4f4f4 2mm,#fff 2mm,#fff 4mm)"></td>'
        h += '</tr>'
    return h + '</table>'


PERS = [("prof", "la professeure (la prof)", "Elle donne cours."), ("educ", "l'éducateur", "Il aide les élèves, il surveille, il note les absences."),
        ("amina", "l'élève", "Il / Elle apprend."), ("bilal", "le délégué de classe", "Il parle pour la classe.")]
PERS2 = [("👩‍💼", "la directrice", "Elle dirige l'école."), ("🧑‍💻", "la secrétaire", "Elle s'occupe des papiers."), ("🧑‍⚕️", "l'infirmière", "Elle soigne les élèves."),
         ("🧑‍🔧", "le technicien", "Il répare et il nettoie."), ("📚", "la bibliothécaire", "Elle prête les livres."), ("🧑‍🍳", "le cuisinier", "Il prépare les repas.")]


def build_b(b, E):
    # ================= PERSONNES =================
    pc = "".join(f'<div class="card c">{avatar(k, 60)}<div class="word">{n}</div><div class="xs muted">{d}</div></div>' for k, n, d in PERS)
    pc2 = "".join(f'<div class="card c"><span class="emo">{e}</span><div class="word">{n}</div><div class="xs muted">{d}</div></div>' for e, n, d in PERS2)
    e1 = E("Les personnes de l'école. J'écoute et je répète.", f'<div class="grid4">{pc}</div><div class="grid3 mt2">{pc2}</div>', ["ecoute", "repete"], 1, "A",
           script="Présenter chaque personne : « Voici la directrice. Elle dirige l'école. » Faire répéter. Donner les vrais noms des personnes de l'école et les afficher avec leur photo si possible.",
           sol="Activité orale. Compléter avec les vrais noms du personnel de l'école.")
    e2 = E("Qui est-ce ? Je relie la personne et le lieu.", relie(["l'infirmière", "la bibliothécaire", "la secrétaire", "le cuisinier", "la prof de sport"], ["le secrétariat", "la salle de gym", "l'infirmerie", "le réfectoire", "la bibliothèque"]),
           ["relie"], 1, "B", sol="infirmière → infirmerie · bibliothécaire → bibliothèque · secrétaire → secrétariat · cuisinier → réfectoire · prof de sport → salle de gym")
    b.page(f'<h2>Les personnes de l\'école</h2>{e1}{e2}', "Lexique")

    e3 = E("J'ai un problème. À qui je parle ? J'écris.", '<div class="grid2">' + "".join(f'<div class="card"><p class="sm">{t}</p><p>→ {blank("l")}</p></div>' for t in ["Je suis malade.", "J'ai perdu mon cartable.", "Je ne comprends pas l'exercice.", "Je veux un livre en arabe ou en ukrainien.", "J'arrive en retard le matin.", "Je dois donner un papier de ma maman."]) + '</div>',
           ["lis", "ecris"], 2, "C", sol="l'infirmière · l'éducateur · la prof · la bibliothécaire · l'éducateur (ou le secrétariat) · le secrétariat (ou l'éducateur)")
    e4 = E("Défi ! Je présente une personne de mon école (son nom, son travail, son lieu).", f'<div class="flex top"><div class="card" style="width:40mm;height:40mm" ></div><div class="grow">{lines(4)}</div></div>', ["ecris", "dessine"], 3, "C",
           sol="Exemple : Voici Monsieur Diallo. C'est l'éducateur. Il aide les élèves. Son bureau est au rez-de-chaussée.")
    e4b = E("Qui dit quoi ? Je relie la phrase et la personne.", relie(["« Ouvrez vos livres à la page 12. »", "« Tu étais absent hier ? Tu as un papier ? »", "« Tu rends le livre dans deux semaines. »", "« Tu as de la fièvre. Tu te couches ici. »"],
             ["l'infirmière", "la prof", "la bibliothécaire", "l'éducateur"]), ["lis", "relie"], 2, "B",
             sol="page 12 → la prof · absent → l'éducateur · rendre le livre → la bibliothécaire · fièvre → l'infirmière")
    b.page(f'{e3}{e4}{e4b}', "S'entraîner")

    # ================= MATIÈRES + HORAIRE =================
    mat = [("📖", "le français"), ("➗", "les mathématiques (les maths)"), ("🔬", "les sciences"), ("🌍", "la géographie"), ("🏛️", "l'histoire"), ("⚽", "l'éducation physique (la gym)"),
           ("🎵", "la musique"), ("🎨", "les arts"), ("💻", "l'informatique"), ("🗣️", "le néerlandais"), ("🤝", "la citoyenneté"), ("📚", "la bibliothèque")]
    mc = "".join(f'<div class="card c" style="padding:2mm"><span class="emo s">{e}</span><div class="word" style="font-size:10pt">{w}</div></div>' for e, w in mat)
    e5 = E("Les cours à l'école. J'écoute et je répète.", f'<div class="grid6">{mc}</div>', ["ecoute", "repete"], 1, "A",
           script="Dire chaque matière avec l'article. Mimer : maths (compter sur les doigts), gym (courir sur place), musique (chanter)… Demander : « Tu aimes les maths ? »",
           sol="Activité orale.")
    jours = '<div class="flex" style="gap:2mm;flex-wrap:wrap">' + "".join(f'<span class="pill" style="background:{c}">{d}</span>' for d, c in [("lundi", "#FFE5DC"), ("mardi", "#E1EAFB"), ("mercredi", "#DDF3EC"), ("jeudi", "#FFF3C4"), ("vendredi", "#EEE3FC")]) + '<span class="pill">samedi 🏠</span><span class="pill">dimanche 🏠</span></div>'
    e5b = E("Mes cours préférés. Je colorie mon visage pour chaque cours, puis je compare avec un camarade : « J'aime les maths. Et toi ? »", '<div class="grid4">' + "".join(f'<div class="card c"><span class="emo s">{e}</span><div class="xs">{w}</div><div>😀 🙂 🙁</div></div>' for e, w in mat[:8]) + '</div>',
             ["colorie", "parle", "duo"], 1, "A", sol="Réponses personnelles (introduction de « j'aime » — repris au module 6).")
    b.page(f'<h2>Les cours</h2>{e5}{e5b}<div class="card"><b>Les jours d\'école</b> (on les apprend bien au module 3) :{jours}<p class="sm mt2">🇧🇪 En Belgique, le <b>mercredi après-midi</b>, il n\'y a pas cours au secondaire.</p></div>', "Lexique")

    e6 = E("Je lis l'horaire de la classe DASPA B. Je réponds.", f'''<div class="grid2"><p>1. Le lundi, la 1re heure, c'est {blank()}.</p><p>2. Le mardi à 12 h 45, c'est {blank()}.</p>
<p>3. La gym, c'est quels jours ? {blank()}</p><p>4. Le cours de maths est au local {blank("s")}.</p><p>5. Le mercredi après-midi, il y a cours ? {blank("s")}</p><p>6. Combien d'heures de français le lundi ? {blank("s")}</p></div>''',
           ["lis", "ecris"], 2, "B", sol="1. français — 2. géographie — 3. lundi et jeudi — 4. 14 — 5. non — 6. deux")
    b.page(f'<span class="tag-doc">📄 DOCUMENT DE LA VIE</span><h2>L\'horaire de la classe</h2><div class="doc" style="padding:3mm;transform:none"><div class="flex" style="justify-content:space-between;margin-bottom:2mm"><b>ATHÉNÉE DES TILLEULS · Horaire 2026–2027</b><span class="pill" style="background:#FFE5DC">DASPA B · titulaire : Mme Lambert</span></div>{horaire_html()}</div><div class="mt4">{e6}</div>', "Document de la vie")

    e7 = E("Vrai ou faux ? Je coche.", table(["", "Vrai", "Faux"], [[x, '<span class="chk"></span>', '<span class="chk"></span>'] for x in ["Il y a cours le samedi.", "La récréation commence à 10 h 00.", "Le jeudi, la classe va à la bibliothèque.", "Le cours de sciences est au laboratoire.", "Le vendredi, il y a 7 heures de cours."]], ["130mm", "25mm", "25mm"]),
           ["lis", "coche"], 1, "B", sol="1. Faux — 2. Vrai — 3. Vrai — 4. Vrai — 5. Faux (6 heures)")
    e8 = E("Mon horaire à moi. Je recopie mon horaire du lundi.", table(["Heure", "Cours", "Local", "Prof"], [[h, "", "", ""] for h in HEURES], ["30mm", "60mm", "40mm", "52mm"]), ["recopie", "ecris"], 2, "C",
           sol="Réponses personnelles (horaire réel de l'élève).")
    e9 = E("Défi ! J'écris 3 phrases sur mon horaire. Exemple : « Le lundi, j'ai deux heures de français. »", lines(3), ["ecris"], 3, "C", sol="Production libre.")
    b.page(f'{e7}{e8}{e9}', "Document de la vie")

    # ================= LEÇON 4 AIDE / EXCUSES =================
    l4 = lecon("Demander de l'aide · S'excuser · Être poli", '''
<table class="t" style="background:#fff"><tr><th>Je veux…</th><th>À un camarade (tu)</th><th>À un adulte (vous)</th></tr>
<tr><td>🙏 demander poliment</td><td>… s'il <b>te</b> plaît.</td><td>… s'il <b>vous</b> plaît.</td></tr>
<tr><td>✏️ emprunter un objet</td><td>Tu peux me prêter ta gomme ?</td><td>Vous pouvez me prêter un stylo ?</td></tr>
<tr><td>📍 demander un lieu</td><td>Où est la bibliothèque ?</td><td>Excusez-moi, où est le secrétariat ?</td></tr>
<tr><td>🤝 demander de l'aide</td><td>Tu peux m'aider ?</td><td>Vous pouvez m'aider, s'il vous plaît ?</td></tr>
<tr><td>😕 m'excuser</td><td>Pardon ! / Excuse-moi !</td><td>Excusez-moi ! / Je suis désolé(e).</td></tr>
<tr><td>⏰ arriver en retard</td><td colspan="2">Excusez-moi pour le retard.</td></tr>
<tr><td>😊 remercier / répondre</td><td colspan="2">Merci ! — De rien ! / Avec plaisir !</td></tr></table>''')
    e10 = E("J'écoute les petits dialogues. Poli ou pas poli ? Je coche 😊 ou 😠.", table(["", "1", "2", "3", "4", "5", "6"], [["😊 poli"] + ['<span class="chk"></span>'] * 6, ["😠 pas poli"] + ['<span class="chk"></span>'] * 6], ["30mm"] + ["25mm"] * 6),
            ["ecoute", "coche"], 1, "A", script="1. « Donne ta gomme ! » — 2. « Tu peux me prêter ta gomme, s'il te plaît ? » — 3. « Excusez-moi pour le retard, Madame. » — 4. (entre en classe sans rien dire, en claquant la porte) « Bon. » — 5. « Merci beaucoup ! — De rien ! » — 6. « Hé ! Où sont les toilettes ? » (à la directrice)",
            sol="1. pas poli — 2. poli — 3. poli — 4. pas poli — 5. poli — 6. pas poli (on dit « Excusez-moi, Madame, où sont les toilettes ? »)")
    b.page(f'{l4}{e10}', "Leçon 4")

    e11 = E("Je transforme : je rends la phrase polie.", f'''<p>1. Donne ton stylo ! → {blank("xl")}</p><p>2. Où sont les toilettes ? (à la prof) → {blank("xl")}</p><p>3. Aide-moi ! (à la prof) → {blank("xl")}</p>''', ["ecris"], 2, "C",
            sol="1. Tu peux me prêter ton stylo, s'il te plaît ? — 2. Excusez-moi, Madame, où sont les toilettes, s'il vous plaît ? — 3. Vous pouvez m'aider, s'il vous plaît ?")
    sit = [("⏰", "Tu arrives en retard en classe."), ("✏️", "Tu n'as pas de crayon."), ("🦶", "Tu marches sur le pied d'un élève."), ("🗺️", "Tu cherches le local 14."), ("🎁", "Un camarade te donne un bonbon."), ("❓", "Tu ne comprends pas l'exercice.")]
    e12 = E("Jeux de rôle. Je tire une carte et je joue la scène avec un camarade.", '<div class="grid3">' + "".join(f'<div class="card c" style="border-style:dashed"><span class="emo s">{e}</span><p class="sm">{t}</p></div>' for e, t in sit) + '</div>',
            ["parle", "duo", "decoupe"], 2, "A", sol="1. Excusez-moi pour le retard. — 2. Tu peux me prêter un crayon, s'il te plaît ? — 3. Pardon ! Excuse-moi ! — 4. Excusez-moi, où est le local 14 ? — 5. Merci ! — 6. Vous pouvez répéter / m'aider, s'il vous plaît ?")
    e13 = E("Défi ! J'écris un petit dialogue (4 répliques) : je demande mon chemin dans l'école.", lines(4), ["ecris"], 3, "C", sol="Production libre : salutation + « Excusez-moi, où est… ? » + réponse avec un lieu + remerciement.")
    b.page(f'{e11}{e12}{e13}', "S'entraîner")

    # ================= RÈGLEMENT =================
    regles = [("✅", "#2BA88F", "J'arrive à l'heure.", "⏰"), ("✅", "#2BA88F", "Je salue les adultes.", "👋"), ("✅", "#2BA88F", "J'ai mon journal de classe et mon matériel.", "🎒"),
              ("✅", "#2BA88F", "Je respecte les autres et le matériel.", "🤝"), ("🚫", "#E4572E", "Pas de GSM en classe.", "📱"), ("🚫", "#E4572E", "Pas de casquette en classe.", "🧢"),
              ("🚫", "#E4572E", "On ne mange pas en classe.", "🍔"), ("⚠️", "#F2B705", "Absent ? Les parents préviennent l'école.", "📞")]
    rc = "".join(f'<div class="card flex" style="border-left:6px solid {c};padding:2.5mm"><span class="emo s">{i}{e}</span><span class="word">{t}</span></div>' for i, c, t, e in regles)
    e14 = E("Je lis le règlement. Vrai ou faux ?", table(["", "Vrai", "Faux"], [[x, '<span class="chk"></span>', '<span class="chk"></span>'] for x in ["Je peux utiliser mon GSM en classe.", "Je dois arriver à l'heure.", "Je peux manger un sandwich en classe.", "Si je suis absent, mes parents téléphonent à l'école."]], ["130mm", "25mm", "25mm"]),
            ["lis", "coche"], 2, "B", sol="1. Faux — 2. Vrai — 3. Faux — 4. Vrai")
    e15 = E("Défi ! Dans mon école d'avant, c'était pareil ? J'explique une différence.", lines(2), ["ecris", "parle"], 3, "C", sol="Production libre ; discussion interculturelle.")
    b.page(f'<span class="tag-doc">📄 DOCUMENT DE LA VIE</span><h2>Le règlement de l\'école (extrait)</h2><div class="doc" style="padding:4mm;transform:none"><div class="c" style="font-weight:800;color:{MC};margin-bottom:2mm">ATHÉNÉE DES TILLEULS · LES RÈGLES DE VIE</div><div class="grid2">{rc}</div></div><div class="mt4">{e14}{e15}</div><div class="astuce">🇧🇪 En Belgique, on dit <b>un GSM</b> pour un téléphone portable.</div>', "Document de la vie")

    # ================= CONSIGNES À 2 ACTIONS =================
    l5 = lecon("Les consignes à deux actions", f'''<p>Une consigne peut avoir <b>deux</b> actions. Je fais l'action 1, <b>puis</b> l'action 2.</p>
<div class="grid2"><div class="card" style="background:#fff"><p>{picto("lis", 26)} + {picto("souligne", 26)}</p><p><b>Lis</b> le texte <b>et souligne</b> les noms.</p><p class="sm muted">1. je lis → 2. je souligne</p></div>
<div class="card" style="background:#fff"><p>{picto("decoupe", 26)} + {picto("colle", 26)}</p><p><b>Découpe</b> les images, <b>puis colle</b>-les.</p><p class="sm muted">1. je découpe → 2. je colle</p></div></div>
<p class="mt2 sm">Les petits mots : <b>et</b> · <b>puis</b> · <b>ensuite</b> · <b>avant de</b> (attention : l'ordre change !)</p>''')
    e16 = E("Je fais les consignes dans l'ordre.", f'''<div class="grid2">
<div class="card"><p class="sm"><b>a.</b> Entoure les objets bleus et barre les objets rouges.</p><div class="c" style="font-size:24pt">📕 📘 🎒 🧢 🍎</div></div>
<div class="card"><p class="sm"><b>b.</b> Lis les mots et souligne les mots féminins.</p><p class="c">une gomme · un livre · une chaise · un stylo · une porte</p></div>
<div class="card"><p class="sm"><b>c.</b> Compte les crayons, puis écris le nombre en lettres.</p><div class="c" style="font-size:16pt">✏️✏️✏️✏️✏️✏️✏️✏️✏️✏️✏️</div><p>{blank()}</p></div>
<div class="card"><p class="sm"><b>d.</b> Colorie le carré en vert, ensuite dessine un rond à côté.</p><svg viewBox="0 0 60 24" width="60%" height="16mm"><rect x="4" y="2" width="20" height="20" fill="none" stroke="#1F2A44" stroke-width="1.2"/></svg></div></div>''',
            ["lis"], 2, "C", sol="a. entourer 📘 et 🧢 (bleus) ; barrer 📕, 🎒 et 🍎 (rouges) — b. souligner gomme, chaise, porte — c. onze — d. carré vert + un rond dessiné à côté")
    e16b = E("Je lis la consigne. Je numérote les actions dans l'ordre : 1 puis 2.", table(["Consigne", "Action", "Ordre"], [
        ["Découpe les images, puis colle-les.", "coller · découper", "___ ___"], ["Lis la question avant de répondre.", "répondre · lire", "___ ___"],
        ["Écoute la prof et répète.", "répéter · écouter", "___ ___"], ["Avant de colorier, écris ton nom.", "colorier · écrire", "___ ___"]], ["88mm", "56mm", "38mm"]),
        ["lis", "numerote"], 3, "B", sol="coller 2, découper 1 · répondre 2, lire 1 · répéter 2, écouter 1 · colorier 2, écrire 1 (« avant de » inverse l'ordre !)")
    b.page(f'<span class="tag-doc">🎒 FRANÇAIS DE L\'ÉCOLE</span>{l5}{e16}{e16b}', "Consignes & école")

    # ================= SONS =================
    e17 = E("Les sons [y] et [u]. J'écoute et je répète.", '''<div class="grid2"><div class="card c" style="border-color:#4A7BD1"><div class="huge" style="color:#4A7BD1">[y] = u</div><p>tu · rue 🛣️ · bus 🚌 · lune 🌙 · mur 🧱</p><p class="sm muted">la bouche fait « i » et les lèvres sont rondes 😗</p></div>
<div class="card c" style="border-color:#9B5DE5"><div class="huge" style="color:#9B5DE5">[u] = ou</div><p>tout · roue 🛞 · loup 🐺 · cour 🌳 · bonjour</p><p class="sm muted">la bouche est très ronde, la langue en arrière</p></div></div>''',
            ["ecoute", "repete"], 1, "A", script="Faire sentir la différence avec la main sous le menton. Paires : tu / tout — rue / roue — dessus / dessous — vu / vous — bu / bout. Faire répéter en exagérant.", sol="Activité orale.")
    e18 = E("J'écoute. J'entends [y] ou [u] ? Je coche.", table(["", "1", "2", "3", "4", "5", "6", "7", "8"], [["[y] u"] + ['<span class="chk"></span>'] * 8, ["[u] ou"] + ['<span class="chk"></span>'] * 8], ["22mm"] + ["20mm"] * 8),
            ["ecoute", "coche"], 2, "A", script="Lire deux fois : 1. rue — 2. roue — 3. vous — 4. tu — 5. cour — 6. mur — 7. bonjour — 8. bus", sol="1. [y] — 2. [u] — 3. [u] — 4. [y] — 5. [u] — 6. [y] — 7. [u] — 8. [y]")
    e19 = E("Le son [s] et le son [z]. Ils sont / ils ont. J'écoute et je répète.", '''<div class="grid2"><div class="card c"><div class="huge">[s] 🐍</div><p>ils <b>s</b>ont · poi<b>ss</b>on 🐟 · <b>s</b>alut · dix</p></div><div class="card c"><div class="huge">[z] 🐝</div><p>il<b>s_o</b>nt · poi<b>s</b>on ☠️ · dou<b>z</b>e · les_élèves</p></div></div>
<div class="astuce" style="margin-bottom:0"><b>ils sont</b> [ilsɔ̃] (être) ≠ <b>ils ont</b> [ilzɔ̃] (avoir). Un seul son change le sens ! Entre deux voyelles, <b>s</b> fait [z] : rose, maison, musique.</div>''',
            ["ecoute", "repete"], 2, "A", script="Faire sentir la vibration [z] (main sur la gorge) et le sifflement [s]. Paires : ils sont / ils ont — poisson / poison — dessert / désert — les sacs / les élèves.",
            sol="Activité orale.")
    b.page(f'<h2>J\'écoute bien · [y] / [u] · [s] / [z]</h2>{e17}{e18}{e19}', "Sons")

    # ================= JE RÉVISE M1 (spirale) =================
    e20 = E("🔁 Module 1 · Je réponds aux questions.", f'<p>Comment tu t\'appelles ? {blank("xl")}</p><p>Tu as quel âge ? {blank("xl")}</p><p>Tu viens d\'où ? {blank("xl")}</p>', ["ecris"], 1, "C", sol="Réponses personnelles (J'ai … ans).")
    e21 = E("🔁 Module 1 · Je calcule et j'écris en lettres.", '<p class="big">7 + 8 = ______ &nbsp; 20 − 3 = ______ &nbsp; 6 + 6 = ______ &nbsp; 10 + 9 = ______</p>', ["ecris"], 2, "C", sol="quinze · dix-sept · douze · dix-neuf")
    e22 = E("🔁 Module 1 · Je lis le pictogramme et j'écris la consigne.", '<div class="grid6">' + "".join(f'<div class="card c">{picto(k, 40)}<div class="line" style="height:7mm"></div></div>' for k in ["souligne", "barre", "relie", "numerote", "colorie", "recopie"]) + '</div>', ["ecris"], 1, "C",
            sol="Souligne · Barre · Relie · Numérote · Colorie · Recopie")
    e23 = E("🔁 Module 1 · Être ou avoir ? Je complète.", '<p>Je ___ élève. J\'___ un cahier. Tu ___ 14 ans. Elle ___ gentille. Il ___ un GSM.</p>', ["complete"], 2, "C", sol="suis · ai · as · est · a")
    e23b = E("🔁 Module 1 · J'épelle et j'écoute : la prof épelle 3 mots de l'école. J'écris.", '<div class="grid3">' + '<div class="card"><div class="line"></div></div>' * 3 + '</div>', ["ecoute", "ecris"], 2, "A",
              script="Épeler deux fois : C-O-U-R · L-I-V-R-E · É-C-O-L-E", sol="cour · livre · école")
    b.page(f'<h2>🔁 Je révise le module 1</h2><p class="sm muted">Ce que j\'ai appris avant revient souvent. C\'est comme ça qu\'on n\'oublie pas !</p>{e20}{e21}{e22}{e23}{e23b}', "Je révise")

    # ================= ATELIERS =================
    devin = [("On mange ici à midi.", "le réfectoire"), ("Il y a beaucoup de livres.", "la bibliothèque"), ("On court, on joue au basket.", "la salle de gym"), ("Les profs boivent un café ici.", "la salle des profs"),
             ("J'ai mal au ventre, je vais ici.", "l'infirmerie"), ("On joue dehors à la récréation.", "la cour")]
    e24 = E("Devinettes : « Où suis-je ? » Je lis la carte à mon camarade. Il devine le lieu.", '<div class="grid3">' + "".join(f'<div class="card" style="border-style:dashed;background:#FFF6EE"><b>Où suis-je ?</b><p class="sm">{q}</p><p class="xs muted" style="transform:rotate(180deg)">{r}</p></div>' for q, r in devin) + '</div>',
            ["decoupe", "parle", "duo"], 1, "A", sol="La réponse est écrite à l'envers sur chaque carte.")
    e25 = E("Je décris ma classe à un camarade (5 phrases avec « il y a »). Il dessine. On compare !", '', ["parle", "duo", "dessine"], 3, "A", sol="Production orale libre ; vérification par le dessin.")
    e25b = E("Le robot : je donne des ordres à mon camarade « robot ». Il fait l'action dans la classe.", '<div class="card"><p class="sm">Va à la porte ! · Ouvre la fenêtre ! · Prends le livre ! · Montre l\'horloge ! · Mets la gomme sur la chaise ! · Assieds-toi !</p></div>', ["parle", "duo"], 2, "A",
              sol="Jeu oral (impératif). Inverser les rôles.")
    b.page(f'<span class="atl A" style="font-size:12pt;padding:1.5mm 4mm">{ATELIERS["A"]}</span><h2 class="mt2">Atelier · Écouter et parler</h2>{e24}{e25}{e25b}', "Atelier")

    web = f'''<div class="doc" style="transform:none;border:1px solid #ccc;border-radius:3mm;overflow:hidden">
<div style="background:#eef1f6;padding:1.5mm 3mm;font-size:8.5pt;color:#555">🔒 www.athenee-des-tilleuls.be/bienvenue</div>
<div style="background:{MC};color:#fff;padding:3mm 4mm;font-weight:800;font-size:13pt">Bienvenue à l'Athénée des Tilleuls ! 🌳</div>
<div style="padding:3mm 4mm;font-size:10.5pt;line-height:1.5">Notre école accueille 620 élèves. Il y a 32 classes, une grande bibliothèque, deux laboratoires de sciences et une salle de gym.
Le réfectoire est ouvert de 11 h 55 à 12 h 45. Le repas chaud coûte 4 €.<br><br><b>La classe DASPA</b> accueille les élèves qui arrivent en Belgique. Ils apprennent le français avec Madame Lambert. Monsieur Diallo, l'éducateur, aide les nouveaux élèves.<br><br>
📞 Secrétariat : 081 00 00 00 · ouvert de 8 h 00 à 16 h 00 (le mercredi : jusqu'à 12 h 30).</div></div>'''
    e26 = E("Je lis la page internet de l'école.", web, ["lis"], 1, "B")
    e27 = E("Je réponds aux questions.", f'''<div class="grid2"><p>1. Combien d'élèves ? {blank()}</p><p>2. Combien de classes ? {blank()}</p><p>3. Le repas chaud coûte combien ? {blank()}</p><p>4. Qui aide les nouveaux élèves ? {blank()}</p></div>
<p>5. Le mercredi, le secrétariat ferme à quelle heure ? {blank()}</p><p>6. ●●● Qu'est-ce qu'il y a dans l'école ? (3 choses) {blank("xl")}</p>''', ["lis", "ecris"], 2, "B",
            sol="1. 620 — 2. 32 — 3. 4 € — 4. M. Diallo, l'éducateur — 5. à 12 h 30 — 6. une bibliothèque, deux laboratoires, une salle de gym (un réfectoire)")
    b.page(f'<span class="atl B" style="font-size:12pt;padding:1.5mm 4mm">{ATELIERS["B"]}</span><h2 class="mt2">Atelier · Lire</h2>{e26}{e27}', "Atelier")

    e28 = E("Je recopie la liste de matériel de la rentrée.", '<div class="card" style="background:#F7F8FB"><b>Liste de matériel · DASPA</b><p>un cartable · un plumier · deux stylos bleus · un crayon · une gomme · une latte · des crayons de couleur · une paire de ciseaux · un bâton de colle · un classeur · des feuilles</p></div>' + lines(3, True),
            ["recopie"], 1, "C", sol="Copie sans erreur.")
    e29 = E("J'écris un message à un nouvel élève pour présenter l'école (complète).", f'''<div class="card"><p style="line-height:2.2">Salut ! Bienvenue à l'école ! Dans notre école, il y a {blank("l")} et {blank("l")}.<br>Notre classe est le local {blank("s")}. Le prof de maths s'appelle {blank()}.<br>À midi, on mange {blank("l")}. Si tu as mal, va {blank("l")}. À bientôt !</p></div>''',
            ["ecris", "complete"], 2, "C", sol="Réponses personnelles et cohérentes (au réfectoire, à l'infirmerie).")
    e30 = E("Défi ! J'écris un texte de 6 phrases : « Mon école ici et mon école dans mon pays ».", lines(6), ["ecris"], 3, "C", sol="Production libre : il y a / il n'y a pas de, comparaisons simples.")
    b.page(f'<span class="atl C" style="font-size:12pt;padding:1.5mm 4mm">{ATELIERS["C"]}</span><h2 class="mt2">Atelier · Écrire</h2>{e28}{e29}{e30}', "Atelier")

    # memory à découper
    mem = OBJ[:12]
    mcards = "".join(f'<div style="border:1.5px dashed #9aa1b1;height:30mm;display:flex;align-items:center;justify-content:center;font-size:34pt">{e}</div>' for e, w, g in mem) + \
        "".join(f'<div style="border:1.5px dashed #9aa1b1;height:30mm;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:12pt;text-align:center">{w}</div>' for e, w, g in mem)
    e31 = E("Le memory de la classe. Je découpe les 24 cartes. Je retourne 2 cartes : l'image et le mot = je gagne la paire ! Je dis le mot à voix haute.", f'<div style="display:grid;grid-template-columns:repeat(6,1fr);gap:0">{mcards}</div>',
            ["decoupe", "joue", "groupe"], 1, "D", sol="Jeu : exiger l'article (« C'est un crayon ! »).")
    b.page(f'<span class="atl D" style="font-size:12pt;padding:1.5mm 4mm">{ATELIERS["D"]}</span><h2 class="mt2">Atelier · Jouer</h2>{e31}', "Atelier")

    # mots en cases
    def cases(w):
        return '<div class="flex" style="gap:0;justify-content:center">' + "".join('<div style="width:9mm;height:10mm;border:1.4px solid #1F2A44;margin-left:-1.4px"></div>' for _ in w) + '</div>'
    mw = [("✏️", "CRAYON"), ("📒", "CAHIER"), ("📕", "LIVRE"), ("🧽", "GOMME"), ("📏", "LATTE"), ("🎒", "CARTABLE"), ("🪑", "CHAISE"), ("🚪", "PORTE")]
    e32 = E("Les mots en cases : j'écris une lettre par case. Le nombre de cases m'aide !", '<div class="grid2">' + "".join(f'<div class="card flex"><span class="emo s">{e}</span><div class="grow">{cases(w)}</div></div>' for e, w in mw) + '</div>',
            ["ecris"], 2, "D", sol=" · ".join(w for _, w in mw))
    b.page(f'{e32}', "Atelier")

    # ================= ALPHA =================
    letter_page(b, E, "m", "[m]", [("👩", "maman"), ("🧱", "mur"), ("🏍️", "moto"), ("🏠", "maison")], "nnuwavno",
                [("👩", "maman", 1), ("🧱", "mur", 1), ("🐱", "chat", 0), ("🏠", "maison", 1), ("🛏️", "lit", 0), ("🏍️", "moto", 1), ("🚌", "bus", 0), ("🍎", "pomme", 1)])
    letter_page(b, E, "l", "[l]", [("🛏️", "lit"), ("🌙", "lune"), ("🦙", "lama"), ("📕", "livre")], "itkfhbtd",
                [("🛏️", "lit", 1), ("🌙", "lune", 1), ("🐟", "poisson", 0), ("🦙", "lama", 1), ("🚲", "vélo", 1), ("🍊", "orange", 0), ("📕", "livre", 1), ("🎒", "cartable", 1)])
    letter_page(b, E, "s", "[s]", [("👜", "sac"), ("☀️", "soleil"), ("🐭", "souris"), ("🧂", "sel")], "zcoeaxzc",
                [("👜", "sac", 1), ("☀️", "soleil", 1), ("🐭", "souris", 1), ("🛏️", "lit", 0), ("🧱", "mur", 0), ("🐍", "serpent", 1), ("🌙", "lune", 0), ("6️⃣", "six", 1)])
    letter_page(b, E, "r", "[r]", [("🤖", "robot"), ("🛞", "roue"), ("😂", "rire"), ("🌹", "rose")], "nvmnuvwn",
                [("🤖", "robot", 1), ("🛞", "roue", 1), ("🌙", "lune", 0), ("🌹", "rose", 1), ("👜", "sac", 0), ("🧱", "mur", 1), ("🍊", "orange", 1), ("🐱", "chat", 0)])

    e33 = E("Je lis les syllabes. La consonne glisse vers la voyelle.", '<div class="grid4">' + slide("m", "a") + slide("l", "i") + slide("s", "o") + slide("r", "u") + '</div>' + '<div class="mt2">' + syll_table(["m", "l", "s", "r"]) + '</div>',
            ["lis", "repete"], 1, "P", alpha=True, script="Montrer la glisse avec le doigt : « mmmmm… a → ma ». Lire chaque ligne du tableau, puis en colonne, puis au hasard (la prof montre, l'élève lit).",
            sol="Lecture : ma mi mo mu mé / la li lo lu lé / sa si so su sé / ra ri ro ru ré.")
    e34 = E("J'écoute la syllabe. Je l'entoure.", '<div class="grid2">' + "".join(f'<p class="big"><b>{i}.</b> &nbsp; ' + " &nbsp; ".join(r) + '</p>' for i, r in enumerate([["ma", "mi", "mo"], ["li", "lu", "la"], ["so", "sa", "su"], ["ri", "ra", "ré"], ["mu", "lu", "su"], ["lé", "mé", "ré"]], 1)) + '</div>',
            ["ecoute", "entoure"], 2, "A", alpha=True, script="Dire deux fois : 1. mo — 2. la — 3. su — 4. ri — 5. lu — 6. ré", sol="1. mo — 2. la — 3. su — 4. ri — 5. lu — 6. ré")
    b.page(AL.format(t="Je lis des syllabes") + e33 + e34, "★ Alpha", color=MC)

    words = [("🙋", "a-mi", "ami"), ("🦙", "la-ma", "lama"), ("🧱", "mur", "mur"), ("😂", "ri-re", "rire"), ("📖", "li-re", "lire"), ("👦", "Sa-mi", "Sami"), ("👧", "Mi-la", "Mila"), ("👦🏽", "Ré-mi", "Rémi")]
    e35 = E("Je lis les mots. Je fais glisser mon doigt sous les syllabes.", '<div class="grid4">' + "".join(f'<div class="card c"><span class="emo s">{e}</span><div class="huge">{s.replace("-", "<span style=color:#E4572E>·</span>")}</div></div>' for e, s, w in words) + '</div>',
            ["lis"], 1, "P", alpha=True, script="Lire avec l'élève : d'abord syllabe par syllabe, puis le mot entier. Vérifier la compréhension avec l'image.", sol="ami · lama · mur · rire · lire · Sami · Mila · Rémi")
    e36 = E("Je relie le mot et l'image.", relie([f'<b class="big">{w}</b>' for w in ["mur", "lama", "rire", "lire"]], ['<span class="emo s">📖</span>', '<span class="emo s">🧱</span>', '<span class="emo s">😂</span>', '<span class="emo s">🦙</span>']),
            ["lis", "relie"], 1, "B", alpha=True, sol="mur–🧱 · lama–🦙 · rire–😂 · lire–📖")
    e37 = E("J'écris la syllabe qui manque.", '<div class="grid4">' + "".join(f'<div class="card c"><span class="emo s">{e}</span><p class="huge">{t}</p></div>' for e, t in [("🦙", "la ___"), ("📖", "___ re"), ("🙋", "a ___"), ("😂", "ri ___")]) + '</div>',
            ["complete", "ecris"], 2, "C", alpha=True, sol="lama (ma) · lire (li) · ami (mi) · rire (re)")
    b.page(AL.format(t="Je lis mes premiers mots") + e35 + e36 + e37, "★ Alpha", color=MC)

    e38 = E("Dictée de syllabes : j'écoute et j'écris.", guide_lines(3, 20), ["ecoute", "ecris"], 2, "P", alpha=True, script="Dicter : ma — lu — so — ri — mé — la — su — ro", sol="ma lu so ri mé la su ro")
    e39 = E("Je recopie les mots.", trace("ami", 28, 3) + trace("lire", 28, 3) + trace("Sami", 28, 2), ["recopie", "trace"], 1, "C", alpha=True, sol="Copie.")
    e40 = E("Défi ★ : j'écris 2 mots avec m, l, s, r (avec l'aide de la prof).", guide_lines(1, 20), ["ecris"], 3, "C", alpha=True, sol="Ex. : mur, lama, rire…")
    e40b = E("Je relie les deux syllabes pour faire un mot. J'écris le mot.", '<div class="grid4">' + "".join(f'<div class="card c"><p class="huge">{a} + {c}</p><div class="line"></div></div>' for a, c in [("la", "ma"), ("a", "mi"), ("ri", "re"), ("Sa", "mi")]) + '</div>',
              ["lis", "ecris"], 2, "C", alpha=True, sol="lama · ami · rire · Sami")
    b.page(AL.format(t="J'écris des syllabes et des mots") + e38 + e39 + e40 + e40b, "★ Alpha", color=MC)
