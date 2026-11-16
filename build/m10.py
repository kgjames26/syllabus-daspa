"""Volume 1 · Module 10 « Ma journée »."""
import sys
sys.path.insert(0, '/home/claude/syllabus')
from lib.base import *
from lib.art import *
from lib.alpha import AL, letter_page, syll_table
from lib.module import *
from lib.render import to_pdf

MC = "#AD1457"
ACT = [("⏰", "se réveiller"), ("🛏️", "se lever"), ("🚿", "se laver / se doucher"), ("🪥", "se brosser les dents"), ("👕", "s'habiller"), ("💇", "se coiffer"),
       ("🥣", "déjeuner (le matin)"), ("🚌", "aller à l'école"), ("✏️", "travailler en classe"), ("🍽️", "dîner (à midi)"), ("⚽", "jouer"), ("🏠", "rentrer à la maison"),
       ("📚", "faire ses devoirs"), ("🧹", "aider à la maison"), ("📱", "regarder son téléphone"), ("🍲", "souper (le soir)"), ("📺", "regarder la télé"), ("😴", "se coucher")]
MOM = [("🌅", "le matin"), ("☀️", "à midi"), ("🌤️", "l'après-midi"), ("🌆", "le soir"), ("🌙", "la nuit")]


def clock(h, m, size="18mm"):
    import math
    ah = math.radians((h % 12 + m / 60) * 30)
    am = math.radians(m * 6)
    ticks = "".join(f'<line x1="{20 + 15 * math.sin(math.radians(k * 30)):.1f}" y1="{20 - 15 * math.cos(math.radians(k * 30)):.1f}" x2="{20 + 17 * math.sin(math.radians(k * 30)):.1f}" y2="{20 - 17 * math.cos(math.radians(k * 30)):.1f}" stroke="#1F2A44" stroke-width="1"/>' for k in range(12))
    return (f'<svg viewBox="0 0 40 40" width="{size}"><circle cx="20" cy="20" r="18" fill="#fff" stroke="#1F2A44" stroke-width="1.5"/>{ticks}'
            f'<line x1="20" y1="20" x2="{20 + 9 * math.sin(ah):.1f}" y2="{20 - 9 * math.cos(ah):.1f}" stroke="#1F2A44" stroke-width="2.2" stroke-linecap="round"/>'
            f'<line x1="20" y1="20" x2="{20 + 14 * math.sin(am):.1f}" y2="{20 - 14 * math.cos(am):.1f}" stroke="#E4572E" stroke-width="1.4" stroke-linecap="round"/><circle cx="20" cy="20" r="1.3" fill="#1F2A44"/></svg>')


def build_m10(start=1, tstart=1, render=True):
    b = Book("V1 · M10", "Volume 1 · Premiers pas · Module 10 · Ma journée", MC, start=start)
    E = Ex(b)
    vis = '<div class="c" style="font-size:40pt;line-height:1.3">⏰🛏️🚿🪥👕🥣<br>🚌🏫🍽️📚🍲😴</div>'
    opening(b, MC, 10, "Ma journée", vis, [("⏰", "dire ce que je fais le matin, l'après-midi, le soir"), ("🔁", "conjuguer se lever, s'habiller…"), ("➡️", "raconter dans l'ordre : d'abord, ensuite, enfin"),
            ("📊", "dire si je le fais souvent ou jamais"), ("📓", "lire un emploi du temps et un journal de classe"), ("🎬", "raconter ma journée en BD ou en vidéo")],
            ["Tu te lèves à quelle heure ?", "Qu'est-ce que tu fais après l'école ?", "Ta journée dans ton pays était différente ?"],
            ["le matin", "le soir", "se lever", "s'habiller", "d'abord", "ensuite", "enfin", "toujours", "jamais", "l'emploi du temps"], "#FBE7EF")

    # ---------- Découvrir ----------
    bd = '<div class="grid2" style="gap:3mm">' + "".join([
        bd_case(1, f'<div class="c">{clock(7, 0, "20mm")}</div>' + lr("bilal", ["Zzz… Encore 5 minutes…"], ma="neutre")),
        bd_case(2, f'<div class="c">{clock(7, 45, "20mm")}</div>' + lr("bilal", ["Quoi ? Il est déjà 8 heures moins le quart ! Je suis en retard !"], ma="surpris")),
        bd_case(3, lr("bilal", ["Je me lève vite, je m'habille, je ne me lave pas…"], extra='<div class="c" style="font-size:24pt">👕💨🏃</div>', ma="surpris")),
        bd_case(4, lr("bilal", ["Et je ne prends pas mon déjeuner ! J'ai faim…"], extra='<div class="c" style="font-size:24pt">🥣❌🚌</div>', ma="triste")),
        bd_case(5, lr("prof", ["Bilal, tu es encore en retard ! Tu te couches à quelle heure ?"], "bilal", ["Euh… à minuit. Je regarde des vidéos sur mon téléphone…"], "neutre", "triste")),
        bd_case(6, lr("prof", ["Le soir, éteins ton téléphone et couche-toi à 22 heures. Tu verras !"], "bilal", ["D'accord, Madame. Demain, je me lève à l'heure !"], "sourire", "rire")),
    ]) + '</div>'
    e = E("J'écoute et je regarde la BD : Bilal est en retard.", bd, ["ecoute", "regarde"], 1, "A",
          script="Lire deux fois. Mimer : se réveiller, se lever, s'habiller. Faire répéter : « Je suis en retard ! », « Je me lève », « Je me couche à… ».", sol="Activité orale.")
    b.page(f'<h2>Découvrir · Bilal est en retard</h2>{e}', "Découvrir")
    e = E("Je réponds.", f'<p>1. Bilal se réveille à quelle heure ? {blank()}</p><p>2. Il se lève à quelle heure ? {blank()}</p><p>3. Qu\'est-ce qu\'il ne fait pas ? {blank("xl")}</p><p>4. Il se couche à quelle heure ? Pourquoi ? {blank("xl")}</p><p>5. Le conseil de la prof : {blank("xl")}</p>',
          ["lis", "ecris"], 1, "B", sol="1. à 7 heures — 2. à 8 heures moins le quart (7 h 45) — 3. Il ne se lave pas, il ne prend pas son déjeuner. — 4. à minuit ; il regarde des vidéos — 5. éteindre le téléphone, se coucher à 22 heures")
    e2 = E("Vrai ou faux ?", vf(["Bilal se lève tout de suite.", "Bilal a faim en classe.", "Bilal se couche tôt.", "Demain, Bilal veut être à l'heure."]), ["lis", "coche"], 2, "B", sol="Faux · Vrai · Faux (à minuit) · Vrai")
    e3 = E("Défi ! Et moi ? Je me lève à quelle heure ? Je me couche à quelle heure ? Je dors combien d'heures ?", lines(2), ["ecris", "parle"], 3, "C", sol="Ex. : Je me lève à 6 h 30, je me couche à 22 h : je dors 8 heures et demie.")
    b.page(f'{e}{e2}{e3}<div class="astuce">🇧🇪 En Belgique : le <b>déjeuner</b> = le repas du matin, le <b>dîner</b> = à midi, le <b>souper</b> = le soir. Un ado a besoin de <b>8 à 10 heures</b> de sommeil 😴.</div>', "Découvrir")

    # ---------- Lexique ----------
    e = E("Les actions de la journée. J'écoute, je mime et je répète.", emogrid(ACT, 6), ["ecoute", "repete"], 1, "A", script="Dire chaque action en la mimant. Jeu : un élève mime, la classe devine (« Tu te brosses les dents ! »).", sol="Activité orale.")
    e2 = E("Les moments de la journée.", '<div class="grid5">' + "".join(f'<div class="card c"><span class="emo">{em}</span><b>{t}</b></div>' for em, t in MOM) + '</div>', ["ecoute", "repete"], 1, "A", script="Montrer le soleil qui monte et descend. Le matin : de 6 h à 12 h…", sol="Activité orale.")
    b.page(f'<h2>Ma journée</h2>{e}{e2}', "Lexique")
    e = E("Je classe les actions : le matin, l'après-midi ou le soir ?", table(["🌅 Le matin", "🌤️ L'après-midi", "🌆 Le soir"], [["", "", ""]], ["60mm", "60mm", "62mm"]).replace("<td></td>", '<td style="height:36mm"></td>') +
          '<p class="sm mt2">se réveiller · faire ses devoirs · souper · s\'habiller · rentrer à la maison · se coucher · déjeuner · jouer au parc · regarder la télé · se brosser les dents</p>', ["ecris"], 1, "C",
          sol="Matin : se réveiller, s'habiller, déjeuner, se brosser les dents · Après-midi : rentrer, faire ses devoirs, jouer au parc · Soir : souper, regarder la télé, se coucher (se brosser les dents aussi !)")
    e2 = E("Je relie l'heure et le moment.", relie([clock(7, 0, "13mm"), clock(12, 30, "13mm"), clock(16, 0, "13mm"), clock(9, 0, "13mm") + ' 🌙'], ["l'après-midi", "le matin", "la nuit / le soir", "à midi"]), ["regarde", "relie"], 1, "B",
           sol="7 h → le matin · 12 h 30 → à midi · 16 h → l'après-midi · 21 h → le soir")
    b.page(f'{e}{e2}', "Lexique")

    # ---------- Leçon 1 : verbes pronominaux ----------
    l1 = lecon("Les verbes pronominaux : se lever, s'habiller", f'''<div class="grid3"><div class="card" style="background:#fff"><b>SE LEVER</b><p>je <b>me</b> lève<br>tu <b>te</b> lèves<br>il / elle <b>se</b> lève<br>nous <b>nous</b> levons<br>vous <b>vous</b> levez<br>ils / elles <b>se</b> lèvent</p></div>
<div class="card" style="background:#fff"><b>S'HABILLER</b> (voyelle)<p>je <b>m'</b>habille<br>tu <b>t'</b>habilles<br>il / elle <b>s'</b>habille<br>nous <b>nous</b> habillons<br>vous <b>vous</b> habillez<br>ils / elles <b>s'</b>habillent</p></div>
<div class="card" style="background:#fff"><b>Le petit mot</b> 🪞<p>Je fais l'action <b>sur moi</b> : je <b>me</b> lave.</p><p>Je lave le chien 🐕 → pas de « me ».</p><p><b>Négation :</b> je <b>ne</b> me lève <b>pas</b>.</p></div></div>
<p class="mt2">Autres verbes : se réveiller · se laver · se doucher · se brosser les dents · se coiffer · se reposer · se dépêcher · se coucher</p>''')
    e = E("Je complète avec me, te, se, nous, vous (m', t', s').", '<p>1. Je ___ réveille à 6 h 30. 2. Tu ___ habilles vite. 3. Elle ___ coiffe. 4. Nous ___ dépêchons ! 5. Vous ___ couchez tard. 6. Ils ___ lavent les mains.</p>', ["complete"], 1, "C",
          sol="me · t' · se · nous · vous · se")
    b.page(f'{l1}{e}', "Leçon 1")
    e = E("Je conjugue au présent.", '<p>1. Daria (se lever) ______________ à 7 h.</p><p>2. Nous (se brosser) ______________ les dents.</p><p>3. Tu (se doucher) ______________ le matin ?</p><p>4. Les garçons (s\'habiller) ______________.</p><p>5. Je (se coucher) ______________ à 22 h.</p>', ["complete"], 2, "C",
          sol="se lève · nous brossons · te douches · s'habillent · me couche")
    e2 = E("Je transforme à la forme négative.", '<p>1. Je me lave. → ______________________</p><p>2. Il se réveille tôt. → ______________________</p>', ["ecris"], 2, "C", sol="Je ne me lave pas. · Il ne se réveille pas tôt.")
    e3 = E("Interview : « À quelle heure tu te lèves ? Tu te couches ? » Je pose la question à 3 camarades.", table(["Prénom", "se lève à…", "se couche à…"], [["", "", ""] for _ in range(3)], ["60mm", "60mm", "62mm"]).replace("<td></td>", '<td style="height:9mm"></td>'), ["parle", "ecris", "groupe"], 1, "A",
           sol="Phrase bilan : Yonas se lève à… et se couche à…")
    b.page(f'{e}{e2}{e3}', "S'entraîner")

    # ---------- Leçon 2 : raconter dans l'ordre + heure ----------
    l2 = lecon("Raconter dans l'ordre · dire l'heure", f'''<div class="flex" style="justify-content:space-around">{"".join(f'<div class="c"><span class="pill" style="font-size:12pt">{w}</span><div class="xs muted">{n}</div></div>' for w, n in [("D'abord", "1"), ("Ensuite", "2"), ("Puis", "3"), ("Après", "4"), ("Enfin", "5 · la fin")])}</div>
<p class="mt2"><b>D'abord</b>, je me lève. <b>Ensuite</b>, je me douche. <b>Puis</b> je m'habille. <b>Après</b>, je déjeune. <b>Enfin</b>, je pars à l'école.</p>
<div class="flex mt2" style="justify-content:space-around">{"".join(f'<div class="c">{clock(h, m, "15mm")}<div class="xs"><b>{t}</b></div></div>' for h, m, t in [(7, 0, "7 h · sept heures"), (7, 15, "7 h 15 · et quart"), (7, 30, "7 h 30 · et demie"), (7, 45, "8 h moins le quart"), (12, 0, "midi"), (0, 0, "minuit")])}</div>
<p class="sm mt2">⚠️ Révision du module 3. À l'oral, on dit aussi : 19 h = dix-neuf heures = sept heures du soir. <b>À</b> quelle heure ? → <b>À</b> 8 heures.</p>''')
    e = E("J'écoute la journée de Fatou. Je numérote les images dans l'ordre.", '<div class="grid6">' + "".join(f'<div class="card c"><span class="emo">{em}</span><div class="line"></div></div>' for em in ["🚌", "⏰", "🥣", "🚿", "👕", "🪥"]) + '</div>', ["ecoute", "numerote"], 1, "A",
          script="D'abord, je me réveille à 6 h 30. Ensuite, je me douche. Puis je m'habille. Après, je déjeune : du pain et du thé. Je me brosse les dents. Enfin, je prends le bus à 7 h 40.",
          sol="⏰ 1 · 🚿 2 · 👕 3 · 🥣 4 · 🪥 5 · 🚌 6")
    b.page(f'{l2}{e}', "Leçon 2")
    e = E("J'écris l'heure sous l'horloge.", '<div class="grid6">' + "".join(f'<div class="card c">{clock(h, m, "16mm")}<div class="line"></div></div>' for h, m in [(6, 30), (8, 15), (10, 0), (12, 45), (3, 30), (9, 15)]) + '</div>', ["regarde", "ecris"], 2, "C",
          sol="6 h 30 · 8 h 15 · 10 h · 1 h moins le quart (12 h 45) · 3 h 30 (15 h 30) · 9 h 15 (21 h 15)")
    e2 = E("Je remets la phrase dans l'ordre, avec les mots d'ordre.", '<p>mange · ensuite · je · une tartine → ______________________</p><p>enfin · me · je · couche → ______________________</p><p>d\'abord · lève · je · me → ______________________</p>', ["ecris"], 2, "C",
           sol="Ensuite, je mange une tartine. · Enfin, je me couche. · D'abord, je me lève.")
    e3 = E("Je raconte mon matin avec d'abord, ensuite, puis, enfin (4 phrases).", lines(4), ["ecris"], 2, "C", sol="Production personnelle (verbes pronominaux + mots d'ordre).")
    b.page(f'{e}{e2}{e3}', "S'entraîner")

    # ---------- Leçon 3 : fréquence ----------
    freq = [("toujours", "100 %", 7), ("souvent", "", 5), ("parfois", "", 3), ("rarement", "", 1), ("jamais", "0 %", 0)]
    l3 = lecon("Dire la fréquence : toujours, souvent, jamais", '<div class="grid5">' + "".join(f'<div class="card c" style="background:#fff;padding:2mm"><b>{w}</b><div style="font-size:8pt;letter-spacing:.3mm">{"●" * n}{"○" * (7 - n)}</div><div class="xs muted">{p}</div></div>' for w, p, n in freq) + '</div>' +
               '<p class="mt2">Le mot se place <b>après le verbe</b> : Je mange <b>toujours</b> à la cantine. Je me lève <b>souvent</b> tôt.</p><div class="attention">⚠️ <b>jamais</b> = ne… jamais : Je <b>ne</b> bois <b>jamais</b> de café. Il <b>ne</b> se couche <b>jamais</b> tôt.</div>' +
               '<p><b>Et aussi :</b> tous les jours · chaque matin · le lundi (= tous les lundis) · une fois par semaine · deux fois par jour</p>')
    e = E("Je complète avec un mot de fréquence (vrai pour moi).", '<p>1. Je me brosse les dents ________. 2. Je fais ________ mes devoirs. 3. Je vais ________ à la piscine. 4. Je regarde ________ la télé le soir.</p>', ["complete"], 1, "C", sol="Réponses personnelles (toujours, souvent, parfois, rarement, ne… jamais).")
    b.page(f'{l3}{e}', "Leçon 3")
    e = E("Je transforme avec ne… jamais.", '<p>1. Je mange du poisson. → ______________________</p><p>2. Elle se lève tard. → ______________________</p><p>3. Nous prenons le bus. → ______________________</p>', ["ecris"], 2, "C",
          sol="Je ne mange jamais de poisson. · Elle ne se lève jamais tard. · Nous ne prenons jamais le bus.")
    e2 = E("J'écoute Yonas. Il fait ça combien de fois ? Je relie.", relie(["⚽ jouer au foot", "📱 téléphone au lit", "🧹 aider maman", "🥣 déjeuner", "🕌 aller à la mosquée"], ["tous les jours", "le vendredi", "jamais", "souvent", "parfois"]), ["ecoute", "relie"], 2, "A",
           script="Je joue souvent au foot après l'école. Je ne prends jamais mon téléphone au lit : c'est la règle chez moi ! J'aide parfois maman à faire le ménage. Je déjeune tous les jours. Et le vendredi, je vais à la mosquée avec mon père.",
           sol="foot → souvent · téléphone → jamais · aider → parfois · déjeuner → tous les jours · mosquée → le vendredi")
    e3 = E("Sondage de la classe : « Tu fais du sport ? Tu lis ? Tu joues aux jeux vidéo ? » Je fais un petit graphique.", '<div class="card" style="height:36mm"></div>', ["parle", "dessine", "groupe"], 3, "A", sol="Graphique en barres : toujours / souvent / parfois / jamais.")
    b.page(f'{e}{e2}{e3}', "S'entraîner")

    # ---------- FLESco : chronologie ----------
    l4 = lecon("Mettre des événements dans l'ordre (chronologie)", '<p>1️⃣ Je regarde toutes les images. 2️⃣ Je cherche le <b>début</b> (le matin, « d\'abord ») et la <b>fin</b> (le soir, « enfin »). 3️⃣ Je cherche les <b>indices</b> : l\'heure, le soleil, les vêtements. 4️⃣ Je <b>numérote</b>. 5️⃣ Je raconte avec les mots d\'ordre.</p><p class="sm">À l\'école : une expérience en sciences, l\'histoire (une ligne du temps), une recette, une BD, un texte.</p>')
    e = E("Je numérote les images de 1 à 6.", '<div class="grid6">' + "".join(f'<div class="card c"><span class="emo">{em}</span><div class="xs">{t}</div><div class="line"></div></div>' for em, t in [("🍲", "souper"), ("⏰", "se réveiller"), ("🏫", "en classe"), ("😴", "dormir"), ("🚌", "le bus"), ("📚", "les devoirs")]) + '</div>', ["regarde", "numerote"], 1, "B",
          sol="⏰ 1 · 🚌 2 · 🏫 3 · 📚 4 · 🍲 5 · 😴 6")
    tl = '<svg viewBox="0 0 180 22" width="100%"><line x1="5" y1="11" x2="175" y2="11" stroke="#1F2A44" stroke-width="1.2"/><path d="M175 11 l-4 -3 v6z" fill="#1F2A44"/>' + "".join(f'<line x1="{x}" y1="7" x2="{x}" y2="15" stroke="#1F2A44"/><text x="{x}" y="21" font-size="4.5" text-anchor="middle" font-family="Poppins">{t}</text>' for x, t in [(15, "6 h"), (45, "9 h"), (75, "12 h"), (105, "15 h"), (135, "18 h"), (165, "21 h")]) + '</svg>'
    e2 = E("La ligne du temps : je place les actions de ma journée (dessin ou mot).", tl + '<div class="card" style="height:22mm"></div>', ["dessine", "ecris"], 2, "C", sol="Placement cohérent avec les heures.")
    e3 = E("Défi ! Je lis et je remets l'expérience de sciences dans l'ordre (1 à 4).", '<div class="card"><p>☐ Enfin, j\'observe : la plante a grandi ! ☐ D\'abord, je mets de la terre dans le pot. ☐ Ensuite, je mets une graine. ☐ Puis j\'arrose tous les jours.</p></div>', ["lis", "numerote"], 3, "B", sol="Terre 1 · graine 2 · arroser 3 · observer 4")
    b.page(f'<span class="tag-doc">🎒 FRANÇAIS DE L\'ÉCOLE</span>{l4}{e}{e2}{e3}', "Consignes & école")

    # ---------- Documents de la vie ----------
    hrs = ["8 h 25", "9 h 15", "10 h 05", "10 h 20", "11 h 10", "12 h 00", "13 h 00", "13 h 50", "14 h 40"]
    edt = [["Français", "Maths", "Français", "Sciences", "Français"], ["Français", "Maths", "Français", "Sciences", "Maths"], ["Maths", "Éduc. physique", "Maths", "Français", "Néerlandais"],
           ["☕ RÉCRÉ", "☕ RÉCRÉ", "☕ RÉCRÉ", "☕ RÉCRÉ", "☕ RÉCRÉ"], ["Géographie", "Éduc. physique", "Français", "Maths", "Français"], ["Musique", "Français", "—", "Arts", "Histoire"],
           ["🍽️ DÎNER", "🍽️ DÎNER", "", "🍽️ DÎNER", "🍽️ DÎNER"], ["Français", "Sciences", "", "Français", "Religion / CPC"], ["Atelier", "Histoire", "", "Informatique", "Atelier"]]
    rows = [[f'<b>{h}</b>'] + r for h, r in zip(hrs, edt)]
    edth = table(["", "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi"], rows, ["20mm"] + ["32mm"] * 5).replace("<td>☕ RÉCRÉ</td>", '<td style="background:#FFF3C4;text-align:center">☕ RÉCRÉ</td>').replace("<td>🍽️ DÎNER</td>", '<td style="background:#E3F2E1;text-align:center">🍽️ DÎNER</td>')
    e = E("Je lis l'emploi du temps de la classe DASPA. Je réponds.", f'<p>1. Le cours commence à quelle heure ? {blank()} 2. La récré est à quelle heure ? {blank()}</p><p>3. Quel jour il y a éducation physique ? {blank()} 4. Le mercredi, l\'école finit à quelle heure ? {blank()}</p><p>5. Combien d\'heures de maths par semaine ? {blank("s")} 6. Le jeudi à 14 h 40, j\'ai… {blank()}</p>',
          ["lis", "ecris"], 2, "B", sol="1. 8 h 25 — 2. 10 h 05 — 3. le mardi — 4. à 12 h — 5. 7 heures — 6. informatique")
    b.page(f'<span class="tag-doc">📄 DOCUMENT DE LA VIE</span><h2>L\'emploi du temps</h2>{edth}<div class="mt4">{e}</div>', "Document de la vie")
    jc = '''<div class="doc" style="transform:rotate(-.8deg);padding:4mm;background:#fff;border:1px solid #c9ced8"><div class="flex" style="justify-content:space-between"><b>📓 JOURNAL DE CLASSE</b><span class="sm">Semaine du 23 au 27 novembre</span></div>
<table class="t" style="margin-top:2mm"><tr><th style="width:26mm">Jour</th><th>À faire / à apprendre</th><th style="width:30mm">Signature</th></tr>
<tr><td><b>Lundi 23</b></td><td>Français : étudier la leçon « se lever » · Maths : ex. 4 et 5</td><td></td></tr>
<tr><td><b>Mardi 24</b></td><td>Apporter le training et les baskets (éduc. physique) 👟</td><td></td></tr>
<tr><td><b>Mercredi 25</b></td><td>Pas de cours l'après-midi · Rendez-vous CPMS à 9 h 15 (Fatou)</td><td></td></tr>
<tr><td><b>Jeudi 26</b></td><td>Interro de vocabulaire : la journée · Rendre le talon signé (excursion)</td><td></td></tr>
<tr><td><b>Vendredi 27</b></td><td>Bibliothèque : rendre le livre 📚</td><td>Parent : ________</td></tr></table></div>'''
    e = E("Je lis le journal de classe. Je réponds.", f'<p>1. Quand est l\'interro ? {blank()} Sur quoi ? {blank()}</p><p>2. Qu\'est-ce que j\'apporte mardi ? {blank("xl")}</p><p>3. Qu\'est-ce que je rends vendredi ? {blank()} 4. Qui signe le journal ? {blank()}</p>', ["lis", "ecris"], 2, "B",
          sol="1. jeudi 26 ; le vocabulaire de la journée — 2. le training et les baskets — 3. le livre de la bibliothèque — 4. les parents (et la prof)")
    e2 = E("J'écris dans mon journal de classe le devoir dicté par la prof.", lines(2), ["ecoute", "ecris"], 2, "A", script="Dicter : « Pour lundi : apprendre les verbes se lever et s'habiller. Faire l'exercice 5. »", sol="Pour lundi : apprendre les verbes se lever et s'habiller. Faire l'exercice 5.")
    b.page(f'<span class="tag-doc">📄 DOCUMENT DE LA VIE</span><h2>Le journal de classe</h2>{jc}<div class="mt4">{e}{e2}</div><div class="astuce">🇧🇪 En Belgique, chaque élève a un <b>journal de classe</b> : on y note les devoirs, les interros, les messages. Les parents le signent chaque semaine. Le <b>CPMS</b> aide les élèves (santé, orientation, soucis).</div>', "Document de la vie")
    bd2 = '<div class="grid3" style="gap:2mm">' + "".join(f'<div style="border:2px solid #1F2A44;border-radius:2mm;padding:2mm;min-height:34mm;background:#FFFDF8"><div class="c" style="font-size:22pt">{em}</div><p class="xs">{t}</p></div>' for em, t in [
        ("🌅⏰", "Le samedi, Daria ne se réveille pas tôt. Elle se lève à 10 h !"), ("🥞☕", "D'abord, elle prend un grand déjeuner avec sa grand-mère."), ("🛒🧺", "Ensuite, elle aide sa mère : elles vont au marché."),
        ("📞💻", "L'après-midi, elle téléphone à son père en Ukraine. Il lui manque."), ("🎨🖌️", "Puis elle dessine. Elle adore les mangas."), ("📺😴", "Le soir, elle regarde un film en famille. Enfin, elle se couche à 23 h.")]) + '</div>'
    e = E("Je lis la BD « Le samedi de Daria ». Je réponds.", bd2 + f'<p class="mt2">1. Daria se lève à quelle heure ? {blank()} 2. Avec qui elle déjeune ? {blank()}</p><p>3. Elle téléphone à qui ? Pourquoi ? {blank("xl")}</p><p>4. Qu\'est-ce qu\'elle adore ? {blank()}</p>', ["lis", "ecris"], 2, "B",
          sol="1. à 10 h — 2. avec sa grand-mère — 3. à son père, en Ukraine : il lui manque — 4. dessiner, les mangas")
    b.page(f'<span class="tag-doc">📄 DOCUMENT DE LA VIE</span><h2>Une BD : le samedi de Daria</h2>{e}', "Document de la vie")

    # ---------- Sons ----------
    e = E("Les lettres muettes : on les écrit, on ne les dit pas. J'écoute et je barre la lettre muette.", '<div class="card big" style="line-height:2">petit · grand · trois · deux · le lit · ils jouent · un chat · le temps · beaucoup · il fait</div>', ["ecoute", "barre"], 1, "A",
          script="Lire lentement. Souvent muets à la fin : e, s, t, d, x, p. Mais : un bus, un parc (on entend !)", sol="petit · grand · trois · deux · lit · jouent (-ent) · chat · temps (p, s) · beaucoup (p) · fait (t)")
    e2 = E("La lettre x et la lettre z. J'écoute et je répète.", '<div class="grid4"><div class="card c"><div class="huge">x = [ks]</div><p>taxi · texte · boxe</p></div><div class="card c"><div class="huge">x = [gz]</div><p>exercice · exemple · examen</p></div><div class="card c"><div class="huge">x = [s] / [z]</div><p>six · dix · deuxième · sixième</p></div><div class="card c"><div class="huge">z = [z]</div><p>zéro · zoo · onze · douze</p></div></div>', ["ecoute", "repete"], 2, "A",
           script="Faire répéter chaque colonne. x à la fin est souvent muet : deux, les cheveux, je veux.", sol="Activité orale.")
    e3 = E("J'écoute : j'entends [ks] ou [gz] ?", checks(6, ["[ks]", "[gz]"]), ["ecoute", "coche"], 2, "A", script="1. taxi — 2. exercice — 3. texte — 4. examen — 5. boxe — 6. exemple", sol="1. ks — 2. gz — 3. ks — 4. gz — 5. ks — 6. gz")
    b.page(f'<h2>J\'écoute bien</h2>{e}{e2}{e3}', "Sons")
    e = E("🔁 Module 9 · Aller à.", '<p>Le matin, je vais ___ école. Le samedi, nous allons ___ marché.</p>', ["complete"], 1, "C", sol="à l' · au")
    e2 = E("🔁 Module 9 · L'impératif.", '<p>(tu) se lever → ______ ! ⚠️ <span class="sm muted">verbe pronominal : lève-toi !</span> · (tu) prendre le bus → ______ !</p>', ["ecris"], 3, "C", sol="Lève-toi ! · Prends le bus !")
    e3 = E("🔁 Module 8 · La météo et les vêtements.", '<p>Il pleut. Je ______ (mettre) mes bottes.</p>', ["complete"], 1, "C", sol="mets")
    b.page(f'<h2>🔁 Je révise les modules 8 et 9</h2>{e}{e2}{e3}', "Je révise")

    # ---------- Ateliers ----------
    cases = [("⏰", "Je me réveille à…"), ("🚿", "Je me douche le… / le soir"), ("🪥", "Je me brosse les dents… fois par jour"), ("🥣", "Au déjeuner, je mange…"), ("🚌", "Je vais à l'école…"), ("🔙", "Recule de 2 cases"),
             ("🍽️", "À midi, je mange…"), ("📚", "Je fais mes devoirs…"), ("⭐", "Rejoue !"), ("⚽", "Après l'école, je…"), ("📱", "Je regarde mon téléphone…"), ("🍲", "Je soupe à… heures"), ("📺", "Le soir, je…"), ("😴", "Je me couche à… ARRIVÉE !")]
    e = E("Le jeu de l'oie de la journée : je lance le dé, j'avance et je complète la phrase à voix haute. Faux ? Je recule d'une case !", '<div class="grid5" style="grid-template-columns:repeat(7,1fr)">' + "".join(f'<div class="card c" style="padding:1.5mm;min-height:24mm"><b class="xs">{i}</b><div class="emo s">{em}</div><div class="xs">{t}</div></div>' for i, (em, t) in enumerate(cases, 1)) + '</div>', ["joue", "parle", "groupe"], 1, "D",
          sol="Phrases complètes au présent (verbes pronominaux, heure, fréquence).")
    e2 = E("Qui suis-je ? Je lis la carte, je devine le personnage du cahier.", '<div class="grid3">' + "".join(f'<div class="card" style="border-style:dashed"><p class="sm">{t}</p><p class="xs muted">→ ________</p></div>' for t in ["Je me couche à minuit. Je suis souvent en retard. J'ai des lunettes.", "Je me lève à 10 h le samedi. J'adore les mangas.", "Je joue souvent au foot. Le vendredi, je vais à la mosquée."]) + '</div>', ["lis", "joue"], 2, "D", sol="Bilal · Daria · Yonas")
    b.page(f'{atl_head("D", "Atelier · Jouer avec ma journée")}{e}{e2}', "Atelier")
    e = E("Je lis le texte d'Amina. Je réponds.", '<div class="card"><p>« Pendant la semaine, je me lève toujours à 6 h 15. D\'abord, je fais la prière avec ma mère. Ensuite, je m\'habille et je prépare le déjeuner de mes petits frères. Puis nous allons à l\'école à pied. À midi, je mange à la cantine avec Fatou. Après l\'école, je fais mes devoirs à la bibliothèque, parce qu\'à la maison, c\'est bruyant ! Le soir, je regarde parfois une série. Je ne me couche jamais après 22 h. »</p></div>' +
          f'<p>1. Amina se lève à quelle heure ? {blank()} 2. Qu\'est-ce qu\'elle fait d\'abord ? {blank("l")}</p><p>3. Elle aide qui ? {blank()} 4. Où fait-elle ses devoirs ? Pourquoi ? {blank("xl")}</p><p>5. Trouve 2 mots de fréquence : {blank()} {blank()}</p>', ["lis", "ecris"], 2, "B",
          sol="1. à 6 h 15 — 2. la prière avec sa mère — 3. ses petits frères — 4. à la bibliothèque, parce que c'est bruyant à la maison — 5. toujours, parfois, (ne) jamais")
    e2 = E("J'écris le texte de ma journée d'école, comme Amina (6 phrases).", lines(6), ["ecris"], 2, "C", sol="Production : heure, verbes pronominaux, mots d'ordre, 1 mot de fréquence.")
    b.page(f'{atl_head("C", "Atelier · Lire et écrire")}{e}{e2}', "Atelier")

    # ---------- ★ Alpha ----------
    letter_page(b, E, "x", "[ks]", [("🚕", "taxi"), ("🥊", "boxe"), ("6️⃣", "six"), ("🎷", "saxo")], "scksvcsk", [("🚕", "taxi", 1), ("🥊", "boxe", 1), ("🐟", "poisson", 0), ("6️⃣", "six", 1), ("🎷", "saxo", 1), ("🏠", "maison", 0), ("🔟", "dix", 1), ("🚌", "bus", 0)], MC)
    letter_page(b, E, "z", "[z]", [("🦓", "zèbre"), ("0️⃣", "zéro"), ("🦁", "zoo"), ("1️⃣1️⃣", "onze")], "sxsvsxcs", [("🦓", "zèbre", 1), ("0️⃣", "zéro", 1), ("🌞", "soleil", 0), ("🦁", "zoo", 1), ("🍕", "pizza", 1), ("🐍", "serpent", 0), ("1️⃣2️⃣", "douze", 1), ("🚌", "bus", 0)], MC)
    letter_page(b, E, "y", "[i] / [j]", [("🚴", "cycliste"), ("🧘", "yoga"), ("✏️", "crayon"), ("🪀", "yoyo")], "iuivilij", [("🧘", "yoga", 1), ("✏️", "crayon", 1), ("🚌", "bus", 0), ("🪀", "yoyo", 1), ("🦓", "zèbre", 0), ("🦬", "yak", 1), ("👀", "yeux", 1), ("🚕", "taxi", 0)], MC)
    e = E("La lettre w et les lettres muettes. Je lis.", '<div class="grid4">' + "".join(f'<div class="card c"><span class="emo s">{em}</span><div class="huge" style="font-size:16pt">{w}</div></div>' for em, w in [("🥪", "sand·wich"), ("📶", "wi-fi"), ("🚃", "wa·gon"), ("🥝", "ki·wi")]) + '</div>' +
          '<div class="grid4 mt2">' + "".join(f'<div class="card c"><span class="emo s">{em}</span><div class="huge" style="font-size:16pt">{w}<span style="color:#bbb">{m}</span></div></div>' for em, w, m in [("🐭", "sou·ri", "s"), ("🐈", "cha", "t"), ("🛏️", "li", "t"), ("2️⃣", "deu", "x")]) + '</div><p class="sm muted">La lettre grise est muette : je l\'écris, mais je ne la dis pas.</p>',
          ["lis"], 1, "P", alpha=True, sol="Lecture.")
    e2 = E("Je lis les phrases de la journée. Je montre l'image.", '<div class="grid2">' + "".join(f'<div class="card"><p class="big">{t}</p></div>' for t in ["Je me lève. 🛏️", "Je me lave. 🚿", "Je vais à l'école. 🏫", "Je me couche. 😴"]) + '</div>', ["lis", "montre"], 2, "P", alpha=True, sol="Lecture + geste.")
    b.page(AL.format(t="Je lis") + e + e2, "★ Alpha", color=MC)
    e = E("Je numérote les images de ma journée et je lis le mot.", '<div class="grid4">' + "".join(f'<div class="card c"><span class="emo">{em}</span><b>{w}</b><div class="line"></div></div>' for em, w in [("😴", "dodo"), ("⏰", "réveil"), ("🏫", "école"), ("🥣", "bol")]) + '</div>', ["lis", "numerote"], 1, "B", alpha=True, sol="réveil 1 · bol 2 · école 3 · dodo 4")
    e2 = E("Je recopie : je me lève.", trace("je me lève", 24, 2), ["recopie", "trace"], 1, "C", alpha=True, sol="Écriture.")
    e3 = E("Dictée.", guide_lines(2, 20), ["ecoute", "ecris"], 2, "P", alpha=True, script="Dicter : x — z — y — taxi — zéro — je me lève", sol="x z y taxi zéro je me lève")
    b.page(AL.format(t="J'écris") + e + e2 + e3, "★ Alpha", color=MC)

    # ---------- Tâche finale ----------
    e = E("Je raconte ma journée en BD (6 cases) : je dessine et j'écris une phrase sous chaque case. OU je prépare un petit vlog (vidéo de 1 minute) avec ce texte.",
          '<div class="grid3" style="gap:2mm">' + "".join(f'<div style="border:2px solid #1F2A44;border-radius:2mm;min-height:52mm;padding:1.5mm"><b class="xs">{i}</b><div style="height:34mm"></div><div class="line"></div><div class="line"></div></div>' for i in range(1, 7)) + '</div>',
          ["dessine", "ecris", "seul"], 2, "C", sol="Évaluation avec la grille.")
    b.page(tache_head("Ma journée en BD ou en vlog", "Je raconte une journée d'école, du réveil au coucher. Je présente ma BD ou ma vidéo à la classe.") + e +
           table(["Je vérifie :", "✅"], [[x, '<span class="chk"></span>'] for x in ["Il y a 6 moments, du matin au soir.", "J'utilise d'abord, ensuite, puis, enfin.", "J'utilise 3 verbes pronominaux (je me…).", "Je dis 2 heures et 1 mot de fréquence."]], ["160mm", "22mm"]), "Tâche finale", levels=False)
    e = E("Je révise.", '<p>1. Nous ______ (se lever) à 7 h. 2. Tu ______ (s\'habiller). 3. 7 h 30 = sept heures ______ 4. Je bois du café. → (jamais) ______________ 5. ______, je me couche. (la fin)</p>', ["ecris"], 2, "C",
          sol="nous levons · t'habilles · et demie · Je ne bois jamais de café. · Enfin")
    e2 = E("Défi ! Je corrige les 4 erreurs.", '<div class="card big">Le matin, je lève à 7 h. Il se habille. Je mange jamais le soir. Enfin, je me réveille.</div>' + lines(1), ["barre", "ecris"], 3, "C",
           sol="je me lève · Il s'habille · Je ne mange jamais · D'abord, je me réveille (ou : Enfin, je me couche)")
    b.page(f'<h2>🔁 Je révise tout le module</h2>{e}{e2}', "Je révise")

    # ---------- Test ----------
    Q = [("🪥 :", ["se coiffer", "se brosser les dents", "se lever", "se coucher"]), ("😴 :", ["se réveiller", "se coucher", "s'habiller", "se laver"]),
         ("Je ____ lève.", ["te", "me", "se", "nous"]), ("Tu ____ habilles.", ["t'", "m'", "s'", "te"]), ("Ils ____ couchent.", ["se", "nous", "vous", "me"]),
         ("Nous nous ____ .", ["lave", "lavons", "lavez", "lavent"]), ("Négation : Je me lave. →", ["Je ne lave pas me.", "Je ne me lave pas.", "Je me ne lave pas.", "Ne je me lave pas."]),
         ("Le repas du matin en Belgique :", ["le dîner", "le souper", "le déjeuner", "le goûter"]), ("7 h 30 :", ["sept heures et quart", "sept heures et demie", "huit heures moins le quart", "sept heures trente-cinq"]),
         ("7 h 45 :", ["sept heures et quart", "huit heures moins le quart", "sept heures et demie", "huit heures et quart"]), ("Le premier mot pour raconter :", ["Enfin", "Ensuite", "D'abord", "Puis"]),
         ("Le dernier mot pour raconter :", ["D'abord", "Enfin", "Ensuite", "Après"]), ("100 % :", ["souvent", "toujours", "parfois", "jamais"]),
         ("« Je ne bois ____ de café. » (0 %)", ["toujours", "souvent", "jamais", "parfois"]), ("Je mange ____ à la cantine.", ["souvent", "jamais souvent", "ne souvent", "souvent ne"]),
         ("Dans le journal de classe, j'écris :", ["mes devoirs", "mes vêtements", "la météo", "mon adresse"]), ("Sur l'emploi du temps, « récré » =", ["un cours", "une pause", "le repas", "un examen"]),
         ("Dans « petit », la lettre muette est :", ["p", "e", "i", "t"]), ("Dans « exercice », x se dit :", ["[ks]", "[gz]", "[s]", "rien"]), ("🔁 Je vais ____ école.", ["au", "à la", "à l'", "aux"])]
    ans = ["se brosser les dents", "se coucher", "me", "t'", "se", "lavons", "Je ne me lave pas.", "le déjeuner", "sept heures et demie", "huit heures moins le quart", "D'abord", "Enfin", "toujours", "jamais", "souvent", "mes devoirs", "une pause", "t", "[gz]", "à l'"]
    key = key_from(Q, ans)
    test_pages(b, 10, "Ma journée", Q, f'<h3>B1. Je conjugue se lever avec je, tu, nous. (… / 3)</h3>{lines(1, True)}<h3>B2. Je raconte mon matin avec d\'abord, ensuite, enfin. (… / 4)</h3>{lines(2, True)}<h3>B3. J\'écris 3 phrases avec toujours, souvent, ne… jamais. (… / 3)</h3>{lines(2, True)}',
               [["raconter sa journée dans l'ordre", "/ 4", ""], ["dire l'heure (3 horloges)", "/ 3", ""], ["répondre : « Tu fais ça souvent ? »", "/ 3", ""]],
               f'<h3>1. J\'écoute et j\'entoure. (… / 4)</h3><div class="grid4">{"".join(f"<div class=\'card c big\' style=\'font-weight:700\'>{r}</div>" for r in ["x z y", "z y x", "y x z", "x y z"])}</div><h3>2. Je lis et je relie. (… / 4)</h3>{relie([f"<b class=big>{w}</b>" for w in ["taxi", "zéro", "lit", "yoyo"]], ["<span class=\'emo s\'>0️⃣</span>", "<span class=\'emo s\'>🪀</span>", "<span class=\'emo s\'>🚕</span>", "<span class=\'emo s\'>🛏️</span>"])}<h3>3. Dictée. (… / 4)</h3>{guide_lines(1, 22)}<h3>4. Je mime et je dis (oral). (… / 4)</h3><div class="card">☐ je me lève ☐ je me lave ☐ je mange ☐ je me couche</div><h3>5. Je remets 4 images de la journée dans l\'ordre. (… / 4)</h3><div class="card">☐ ⏰ ☐ 🏫 ☐ 🍲 ☐ 😴</div>')
    closing(b, 10, ["Je sais dire les actions de la journée.", "Je connais les moments de la journée.", "Je sais conjuguer se lever, s'habiller.", "Je sais dire je ne me lève pas.", "Je sais dire l'heure.",
                    "Je sais raconter dans l'ordre (d'abord, ensuite, enfin).", "Je sais dire toujours, souvent, ne… jamais.", "Je sais remettre des images dans l'ordre.", "Je sais lire un emploi du temps et un journal de classe.", "Je connais les lettres muettes et le x.", "★ Je sais lire x, z, y, w…"],
            ACT[:16] + [("🌅", "le matin"), ("🌆", "le soir"), ("1️⃣", "d'abord"), ("2️⃣", "ensuite"), ("🔚", "enfin"), ("💯", "toujours"), ("🚫", "jamais"), ("📓", "le journal de classe")])
    plan_de_travail(b, E, 10, ["Les verbes pronominaux", "Raconter dans l'ordre · l'heure", "La fréquence", "Mettre dans l'ordre (chronologie)"], "☐ Ma journée en BD (6 cases)<br>☐ ou mon vlog d'une minute")
    if render:
        to_pdf(b.html(), '/home/claude/syllabus/out/V1_M10_eleve.pdf')

    pg, exs = helpers(b, E)
    A = b.marks["★ Alpha"]
    days = [("1", "Collectif", f"Ouverture · BD ({pg('Découvrir')})", f"Alpha : x (p. {A[0]})"), ("2", "Collectif", f"Actions et moments ({pg('Lexique')})", f"Alpha : z (p. {A[1]})"),
            ("3", "Rotation", f"📌 Leçon 1 verbes pronominaux ({pg('Leçon 1')})", f"Alpha : y (p. {A[2]})"), ("4", "Rotation", f"📌 Leçon 2 ordre + heure ({pg('Leçon 2')})", f"Alpha : w, lettres muettes (p. {A[3]})"),
            ("5", "Collectif", f"📌 Leçon 3 fréquence ({pg('Leçon 3')})", f"Alpha : écriture (p. {A[4]})"), ("6", "Rotation", f"Chronologie ({pg('Consignes & école')}) · sons", "Alpha : images à ordonner"),
            ("7", "Collectif", f"Emploi du temps, journal de classe, BD ({pg('Document de la vie')})", "Alpha : son journal de classe"), ("8", "Ateliers", f"Jeu de l'oie, qui suis-je, texte d'Amina ({pg('Atelier')})", "Alpha : jeu de l'oie (images)"),
            ("9", "Seul", f"Tâche finale ({pg('Tâche finale')})", "Alpha : BD + 1 mot par case"), ("10", "Seul", f"Test ({pg('Test')})", f"Alpha : test ({pg('★ Alpha · Test')})")]
    rot = [["🎧 Écouter-Parler", "Interview « tu te lèves à quelle heure ? »", "20 min", "—"], ["📖 Lire", "Texte d'Amina · BD de Daria", "20 min", "Oui"], ["✏️ Écrire", "Verbes pronominaux · ma journée", "20 min", "● oui"],
           ["🧩 Jouer", "Jeu de l'oie · qui suis-je ?", "20 min", "Entre joueurs"], ["👩‍🏫 Table d'appui", "Alpha : x z y · autres : l'heure, ne… jamais", "20 min", "—"]]
    ev1 = '''<h3>Partie B (10 points)</h3><p class="sm"><b>B1</b> : <span class="sol">je me lève · tu te lèves · nous nous levons</span> · <b>B2</b> : 3 étapes logiques avec mots d'ordre (3) + verbe pronominal juste (1) · <b>B3</b> : 1 pt par phrase (place du mot, ne… jamais).</p>
<h3>Test ★ Alpha</h3><p class="sm"><b>Ex. 1, dire :</b> <span class="sol">z · x · y · z</span> · <b>Ex. 2 :</b> <span class="sol">taxi–🚕, zéro–0️⃣, lit–🛏️, yoyo–🪀</span> · <b>Ex. 3, dicter :</b> <span class="sol">x, z, taxi, zéro</span>.</p>'''
    ev2 = f'''<h2>Grille · tâche finale « Ma journée en BD ou en vlog »</h2>{table(["Critère", "Très bien", "Bien", "À retravailler", "Points"], [["<b>Contenu</b> : 6 moments, du matin au soir", "Complet", "Partiel", "Incomplet", "/ 4"], ["<b>Ordre</b> : mots d'ordre", "4 mots", "2-3", "0-1", "/ 4"], ["<b>Verbes pronominaux</b> justes", "3 justes", "1-2", "0", "/ 4"], ["<b>Heures et fréquence</b>", "Oui", "Partiel", "Non", "/ 4"], ["<b>Présentation</b> (BD lisible ou vlog)", "Soignée", "Correcte", "À revoir", "/ 4"]], ["64mm", "32mm", "32mm", "32mm", "22mm"])}
<h2 class="mt4">Différencier et remédier</h2>{table(["Difficulté", "Remédiation"], [["me / te / se", "Miroir : « je me regarde » ; étiquettes pronoms à manipuler ; tableau affiché."], ["L'heure", "Horloge à aiguilles de la classe ; dominos heure-écrite / horloge."], ["ne… jamais", "Gestes : pouce levé (toujours), main plate (parfois), croix (jamais)."], ["Chronologie", "Bandes BD découpées à remettre en ordre avant d'écrire."], ["Élève rapide", "Comparer sa journée ici et dans son pays (texte de 8 phrases) ; vlog avec sous-titres."]], ["50mm", "132mm"])}
<div class="astuce mt4"><b>Sensibilité :</b> certaines routines révèlent des situations difficiles (fatigue, garde des petits frères, travail, ramadan, centre d'accueil, sommeil perturbé). Laisser le choix d'une journée « imaginaire » pour la tâche finale. Le sommeil et les écrans sont un bon sujet de prévention (CPMS).</div>'''
    T = teacher_book(b, E, "V1 · M10", "", MC, 10, "Ma journée",
                     "<li><b>Communication :</b> raconter sa routine, dire l'heure et la fréquence.</li><li><b>Lexique :</b> actions du quotidien, moments de la journée, école (emploi du temps, journal de classe).</li><li><b>Grammaire :</b> verbes pronominaux ; d'abord / ensuite / puis / enfin ; toujours / souvent / parfois / ne… jamais.</li><li><b>Phonétique :</b> lettres muettes ; x, z.</li><li><b>FLSco :</b> chronologie, ligne du temps.</li><li><b>Documents :</b> emploi du temps, journal de classe, BD.</li><li><b>★ Alpha :</b> x, z, y, w ; lettres muettes.</li>",
                     '<p class="sm"><b style="color:#E4572E">Indispensable</b> : actions de base, je me lève / je me couche, l\'heure, lire son journal de classe.</p><p class="sm"><b style="color:#d9a400">Important</b> : mots d\'ordre, fréquence.</p><p class="sm"><b style="color:#2BA88F">Enrichissement</b> : négation des pronominaux, vlog.</p>',
                     "Horloge à aiguilles · miroir · dés · journal de classe réel · tablettes pour le vlog (facultatif, autorisation des parents).", "<b>Lien école :</b> faire lire le <b>vrai</b> journal de classe et l'emploi du temps de la classe ; vérifier que chacun sait où noter ses devoirs.",
                     days, "Quelle heure est-il ? (horloge) · « Hier soir, tu t'es couché à quelle heure ? » (oral) · un verbe pronominal du jour.", rot, key, (ev1, ev2), start=tstart)
    if render:
        to_pdf(T.html(), '/home/claude/syllabus/out/V1_M10_prof.pdf')
    return b, T


if __name__ == "__main__":
    b, T = build_m10()
    print(b.n, T.n)
