"""Volume 2 · Module 3 « Souvenirs d'enfance » (A2)."""
import sys
sys.path.insert(0, '/home/claude/syllabus')
from lib.base import *
from lib.art import *
from lib.module import *
from lib.v2 import CP, CPCOL
from lib.render import to_pdf

MC = "#6A5ACD"
JEUX = [("🪢", "la corde à sauter"), ("🔢", "la marelle"), ("🔵", "les billes"), ("🙈", "cache-cache"), ("🏃", "le chat (on court)"), ("🪆", "la poupée"), ("🪁", "le cerf-volant"), ("🪀", "le yoyo"),
        ("🌀", "la toupie"), ("⚽", "le ballon"), ("🚲", "le vélo"), ("📺", "les dessins animés")]
AUTREFOIS = [("⬛", "le tableau noir et la craie"), ("🖋️", "la plume et l'encrier"), ("✏️", "le plumier"), ("🎒", "le cartable en cuir"), ("👘", "le tablier"), ("🔥", "le poêle à charbon"), ("📻", "la radio"), ("☎️", "le téléphone fixe")]
AUJ = [("🖥️", "le tableau interactif"), ("🖊️", "le bic, le stylo"), ("🧮", "la trousse"), ("🎒", "le sac à dos"), ("👕", "les vêtements de tous les jours"), ("🌡️", "le chauffage central"), ("🎧", "le smartphone et la musique"), ("📱", "le GSM")]


def photo(em, cap, rot=0):
    return (f'<div style="background:#fff;padding:2mm 2mm 1mm;box-shadow:0 1mm 3mm rgba(0,0,0,.25);transform:rotate({rot}deg);border-radius:1mm">'
            f'<div style="background:#E9E4F7;height:30mm;display:flex;align-items:center;justify-content:center;font-size:28pt">{em}</div><p class="xs" style="margin:1mm 0 0;font-family:\'DejaVu Serif\';font-style:italic">{cap}</p></div>')


def frise_ecole():
    ev = [(1914, "Loi : l'école est obligatoire (6 à 14 ans)"), (1958, "Pacte scolaire (paix entre réseaux)"), (1983, "École obligatoire jusqu'à 18 ans"), (1989, "L'enseignement passe aux Communautés"), (2012, "Décret : création des DASPA"), (2020, "École obligatoire dès 5 ans")]
    x0, x1, a, z = 8, 192, 1900, 2030
    X = lambda y: x0 + (y - a) / (z - a) * (x1 - x0)
    ticks = "".join(f'<line x1="{X(y):.1f}" y1="38" x2="{X(y):.1f}" y2="44" stroke="#1F2A44" stroke-width=".6"/><text x="{X(y):.1f}" y="50" font-size="4" text-anchor="middle" font-family="Poppins">{y}</text>' for y in range(1900, 2031, 20))
    sec = (f'<rect x="{x0}" y="30" width="{X(2000) - x0:.1f}" height="6" fill="#C9C2EE"/><text x="{(x0 + X(2000)) / 2:.1f}" y="34.6" font-size="4" text-anchor="middle" font-family="Poppins" font-weight="800">XXᵉ siècle (1901-2000)</text>'
           f'<rect x="{X(2000):.1f}" y="30" width="{x1 - X(2000):.1f}" height="6" fill="#FFD166"/><text x="{(X(2000) + x1) / 2:.1f}" y="34.6" font-size="4" text-anchor="middle" font-family="Poppins" font-weight="800">XXIᵉ s.</text>')
    evs = ""
    for i, (y, t) in enumerate(ev):
        evs += (f'<circle cx="{X(y):.1f}" cy="41" r="3.2" fill="{MC}"/><text x="{X(y):.1f}" y="42.6" font-size="4.2" text-anchor="middle" font-family="Poppins" font-weight="800" fill="#fff">{i + 1}</text>'
                f'<text x="{X(y):.1f}" y="{24 if i % 2 == 0 else 60}" font-size="4.2" text-anchor="middle" font-family="Poppins" font-weight="800">{y}</text>')
    leg = "".join(f'<div class="xs"><b style="color:{MC}">{i + 1}</b> · <b>{y}</b> · {t}</div>' for i, (y, t) in enumerate(ev))
    return f'<svg viewBox="0 10 204 58" width="100%" style="max-height:70mm"><line x1="{x0}" y1="41" x2="{x1}" y2="41" stroke="#1F2A44" stroke-width="1.2"/><path d="M{x1 + 4} 41 l-4 -3 v6z" fill="#1F2A44"/>{sec}{ticks}{evs}</svg><div class="grid2 card" style="padding:2mm;gap:1mm">{leg}</div>'


def build_v2m3(start=1, tstart=1, render=True):
    b = Book("V2 · M3", "Volume 2 · Je me débrouille · Module 3 · Souvenirs d'enfance", MC, start=start)
    E = Ex(b)
    vis = '<div class="c" style="font-size:38pt;line-height:1.3">👶📸🪁🔢🪢<br>🖋️⬛📻🕰️💭</div>'
    opening(b, MC, 3, "Souvenirs d'enfance", vis, [("💭", "raconter un souvenir et décrire le passé"), ("🔁", "dire ce que je faisais avant (les habitudes)"), ("⚖️", "choisir entre imparfait et passé composé"),
            ("😮", "réagir quand quelqu'un raconte"), ("🕰️", "lire une frise chronologique (siècles, dates)"), ("📸", "lire un album photo et un témoignage")],
            ["À quoi tu jouais quand tu étais petit(e) ?", "Comment était ton école avant ?", "Tu as un souvenir drôle ?"],
            ["l'enfance", "le souvenir", "autrefois", "avant", "quand j'étais petit(e)", "d'habitude", "un jour", "tout à coup", "l'imparfait", "la frise"], "#ECE9FA")

    # ---------- Découvrir ----------
    bd = '<div class="grid2" style="gap:3mm">' + "".join([
        bd_case(1, lr("prof", ["Aujourd'hui, jeu des photos de bébé ! Qui est ce bébé avec un chapeau rouge ?"], extra='<div class="c" style="font-size:24pt">👶🎩📸</div>')),
        bd_case(2, lr("bilal", ["C'est moi ! J'avais deux ans. J'habitais à Casablanca, chez ma grand-mère."], "fatou", ["Tu étais trop mignon ! 😍"], "rire", "rire")),
        bd_case(3, lr("amina", ["Quand j'étais petite, je jouais tous les jours à la marelle avec mes cousines. On dessinait les cases avec une pierre."], extra='<div class="c" style="font-size:20pt">🔢🪨👧👧</div>', ma="sourire")),
        bd_case(4, lr("mateo", ["Moi, un jour, je suis tombé d'un arbre ! J'avais six ans. Je me suis cassé le bras."], "nour", ["Aïe ! Ça devait faire mal !"], "pense", "surpris")),
        bd_case(5, lr("prof", ["Et voici ma classe en 1988. Il n'y avait pas d'ordinateur. On écrivait au tableau noir avec une craie."], extra='<div class="c" style="font-size:22pt">⬛🧑‍🏫📼</div>')),
        bd_case(6, lr("yonas", ["Et vous aviez un GSM, Madame ?"], "prof", ["Non ! Nous téléphonions avec le téléphone de la maison. C'était une autre époque !"], "pense", "rire")),
    ]) + '</div>'
    e = E("J'écoute et je lis la BD : le jeu des photos.", bd, ["ecoute", "lis"], 1, "A",
          script="Lire deux fois. Faire repérer les verbes : j'avais, j'habitais, je jouais (habitudes, description) et je suis tombé, je me suis cassé (événement). Proposer d'apporter une photo d'enfance (facultatif !) ou de dessiner.", sol="Activité orale.")
    b.page(f'<h2>Découvrir · Le jeu des photos</h2>{e}', "Découvrir")
    e = E("Je réponds par une phrase complète.", f'<p>1. Bilal avait quel âge sur la photo ? Où habitait-il ? {blank("xl")}</p><p>2. À quoi jouait Amina ? Avec qui ? Comment ? {blank("xl")}</p><p>3. Qu\'est-ce qui est arrivé à Mateo ? {blank("xl")}</p><p>4. Comment était la classe de la prof en 1988 ? {blank("xl")}</p><p>5. Comment est-ce qu\'on téléphonait avant ? {blank("xl")}</p>',
          ["lis", "ecris"], 1, "B", sol="1. Il avait deux ans ; il habitait à Casablanca, chez sa grand-mère. — 2. à la marelle, avec ses cousines ; elles dessinaient les cases avec une pierre. — 3. Il est tombé d'un arbre et il s'est cassé le bras. — 4. Il n'y avait pas d'ordinateur ; on écrivait au tableau noir avec une craie. — 5. avec le téléphone de la maison (fixe)")
    e2 = E("Je classe les verbes de la BD : habitude / description ou événement d'un jour ?", table(["🔁 Habitude, description (imparfait)", "⚡ Événement (passé composé)"], [["", ""]], ["91mm", "91mm"]).replace("<td></td>", '<td style="height:28mm"></td>') + '<p class="sm mt2">j\'avais · j\'habitais · je jouais · on dessinait · je suis tombé · je me suis cassé · il n\'y avait pas · on écrivait · nous téléphonions · c\'était</p>', ["lis", "ecris"], 2, "B",
           sol="Imparfait : j'avais, j'habitais, je jouais, on dessinait, il n'y avait pas, on écrivait, nous téléphonions, c'était · Passé composé : je suis tombé, je me suis cassé")
    b.page(f'{e}{e2}', "Découvrir")
    tem = '''<div class="card" style="background:#FBFAFF"><p style="line-height:1.65"><b>🎙️ Témoignage · Mme Dubois, 78 ans, raconte son école</b><br>
« Je suis née en 1948 à Charleroi. Quand j'étais petite, j'allais à l'école des filles de mon quartier. Les garçons avaient leur école à eux ! Nous portions toutes un tablier gris. Le matin, nous marchions trente minutes, même sous la neige, parce qu'il n'y avait pas de bus.<br>
En classe, il y avait un grand poêle à charbon. En hiver, l'élève de service apportait le charbon. Nous écrivions avec une plume qu'on trempait dans l'encrier. Il ne fallait pas faire de taches ! La maîtresse était très sévère : quand on parlait, on allait au coin.<br>
Un jour, en 1955, ma meilleure amie a renversé l'encrier sur son cahier. Toute la classe a ri… et nous sommes restées après l'école pour tout nettoyer ! Aujourd'hui, ça me fait sourire. C'était une autre vie : pas de télé à la maison, pas de vacances à l'étranger… mais nous jouions dehors tout le temps. »</p></div>'''
    e = E("Je lis le témoignage. Je réponds.", tem + f'<p>1. Mme Dubois est née quand ? Où ? {blank("xl")}</p><p>2. Trouve 3 différences entre son école et ton école. {blank("xl")}</p><p>3. Que faisait l\'élève de service ? {blank("xl")}</p><p>4. Raconte l\'événement de 1955 avec tes mots. {blank("xl")}</p>', ["lis", "ecris"], 2, "B",
          sol="1. en 1948, à Charleroi — 2. école des filles séparée, tablier, poêle à charbon, plume et encrier, pas de bus, punition au coin… — 3. Il apportait le charbon. — 4. Son amie a renversé l'encrier ; la classe a ri ; elles sont restées pour nettoyer.")
    b.page(f'<h2>Découvrir · L\'école d\'autrefois</h2>{e}', "Découvrir")

    # ---------- Lexique ----------
    e = E("Les jeux d'enfance. J'écoute et je répète.", emogrid(JEUX, 6), ["ecoute", "repete"], 1, "A", script="Dire chaque jeu. Demander : « À quoi on jouait dans ton pays ? Comment s'appelle ce jeu dans ta langue ? » Noter les jeux du monde au tableau.", sol="Activité orale.")
    e2 = E("Autrefois et aujourd'hui. Je relie l'objet d'autrefois et l'objet d'aujourd'hui.", relie([f"{e} {t}" for e, t in AUTREFOIS[:6]], [f"{e} {t}" for e, t in [AUJ[3], AUJ[0], AUJ[5], AUJ[1], AUJ[2], AUJ[4]]]), ["relie"], 2, "B",
           sol="tableau noir → tableau interactif · plume/encrier → bic · plumier → trousse · cartable → sac à dos · tablier → vêtements de tous les jours · poêle → chauffage central")
    b.page(f'<h2>Les mots de l\'enfance et d\'autrefois</h2>{e}{e2}', "Lexique")
    sent = [("😨", "avoir peur"), ("😊", "être content(e)"), ("😳", "avoir honte"), ("🥹", "être ému(e)"), ("😤", "être fâché(e)"), ("😌", "être fier / fière"), ("🥲", "avoir de la nostalgie"), ("😂", "rire aux éclats")]
    e = E("Les sentiments dans un souvenir. J'écoute et je répète.", '<div class="grid4">' + "".join(f'<div class="card c" style="padding:2mm"><span class="emo s">{em}</span><b class="sm">{t}</b></div>' for em, t in sent) + '</div>', ["ecoute", "repete"], 1, "A", script="Lire et mimer. Au passé : j'avais peur, j'étais content(e)…", sol="Activité orale.")
    e2 = E("Les mots du temps passé. Je classe : une habitude (souvent) ou un moment précis (une fois) ?", table(["🔁 Habitude", "⚡ Une fois"], [["", ""]], ["91mm", "91mm"]).replace("<td></td>", '<td style="height:24mm"></td>') + '<p class="sm mt2">d\'habitude · un jour · tous les étés · soudain · autrefois · ce jour-là · chaque matin · tout à coup · le dimanche · en 2015 · souvent · une fois</p>', ["ecris"], 2, "C",
           sol="Habitude : d'habitude, tous les étés, autrefois, chaque matin, le dimanche, souvent · Une fois : un jour, soudain, ce jour-là, tout à coup, en 2015, une fois")
    b.page(f'{e}{e2}', "Lexique")

    # ---------- Leçon 1 : formation de l'imparfait ----------
    l1 = lecon("L'imparfait : comment on le forme", '''<div class="grid2"><div class="card" style="background:#fff"><b>La recette</b> 🧑‍🍳<p>1️⃣ Je prends le verbe au présent avec <b>nous</b> : nous <b>jou</b>ons · nous <b>finiss</b>ons · nous <b>fais</b>ons · nous <b>pren</b>ons<br>2️⃣ J'enlève <b>-ons</b>.<br>3️⃣ J'ajoute les terminaisons :</p>
<p style="font-size:13pt"><b>-ais · -ais · -ait · -ions · -iez · -aient</b></p></div>
<div class="card" style="background:#fff"><b>JOUER</b> (nous jouons)<p>je jou<b>ais</b><br>tu jou<b>ais</b><br>il / elle / on jou<b>ait</b><br>nous jou<b>ions</b><br>vous jou<b>iez</b><br>ils / elles jou<b>aient</b></p></div></div>
<div class="attention" style="margin-top:2mm">⚠️ Une seule exception : <b>être</b> → j'<b>ét</b>ais, tu étais, il était, nous étions, vous étiez, ils étaient.<br>Attention à l'orthographe : manger → je mang<b>e</b>ais · commencer → je commen<b>ç</b>ais · il y a → il y <b>avait</b> · il pleut → il <b>pleuvait</b> · il faut → il <b>fallait</b></div>
<p class="sm">À l'oral, <b>-ais, -ait, -aient</b> se prononcent pareil : [ɛ].</p>''')
    e = E("Je trouve le radical avec nous, puis je conjugue à l'imparfait.", table(["Verbe", "nous (présent)", "je (imparfait)", "ils (imparfait)"], [["habiter", "nous habitons", "j'habitais", ""], ["finir", "", "", ""], ["faire", "", "", ""], ["avoir", "", "", ""], ["prendre", "", "", ""], ["aller", "", "", ""], ["boire", "", "", ""]], ["36mm", "50mm", "48mm", "48mm"]).replace("<td></td>", '<td style="height:7mm"></td>'), ["ecris"], 1, "C",
          sol="habitaient · finissons, finissais, finissaient · faisons, faisais, faisaient · avons, avais, avaient · prenons, prenais, prenaient · allons, allais, allaient · buvons, buvais, buvaient")
    b.page(f'{l1}{e}', "Leçon 1")
    e = E("Je conjugue à l'imparfait.", '<p>1. Quand j\'(être) ______ petite, j\'(habiter) ______ à Kaboul. 2. Mon grand-père (raconter) ______ des histoires. 3. Nous (aller) ______ à l\'école à pied. 4. Tu (avoir) ______ un chat ? 5. Mes cousins (jouer) ______ au foot dans la rue. 6. Vous (manger) ______ ensemble le soir ? 7. Il (faire) ______ très chaud en été. 8. Il y (avoir) ______ beaucoup d\'enfants.</p>', ["complete"], 2, "C",
          sol="étais, habitais · racontait · allions · avais · jouaient · mangiez · faisait · avait")
    e2 = E("J'écoute : présent ou imparfait ? Je coche.", checks(8, ["présent", "imparfait"]), ["ecoute", "coche"], 2, "A", script="1. je joue — 2. je jouais — 3. nous allions — 4. nous allons — 5. il était — 6. il est — 7. vous faisiez — 8. vous faites", sol="1. P — 2. I — 3. I — 4. P — 5. I — 6. P — 7. I — 8. P")
    e3 = E("Défi ! Je trouve et je corrige les 4 erreurs.", '<div class="card big">Avant, nous jouions au parc. Je mangais beaucoup de bonbons. Mes parents travaillait le soir. J\'avait un vélo rouge. Vous étiez contents ? Je commencais l\'école à 8 h.</div>' + lines(1), ["barre", "ecris"], 3, "C",
           sol="je mangeais · travaillaient · j'avais · je commençais")
    b.page(f'{e}{e2}{e3}', "S'entraîner")

    # ---------- Leçon 2 : emplois ----------
    l2 = lecon("L'imparfait : quand je l'utilise", table(["Pour…", "Exemple"], [["🖼️ <b>décrire</b> un lieu, une personne, le temps qu'il faisait", "Ma maison <b>était</b> petite. Il <b>faisait</b> froid. Ma grand-mère <b>avait</b> les cheveux blancs."], ["🔁 dire une <b>habitude</b> passée", "Le dimanche, nous <b>allions</b> chez mon oncle. Je <b>jouais</b> tous les jours dehors."], ["💭 dire un <b>sentiment</b>, un état", "J'<b>avais</b> peur du noir. J'<b>étais</b> heureux."], ["🕰️ comparer <b>avant</b> / <b>maintenant</b>", "Avant, je ne <b>parlais</b> pas français. Maintenant, je parle bien !"]], ["70mm", "112mm"]) +
               '<p class="mt2"><b>Mots utiles :</b> quand j\'étais petit(e) · à cette époque · autrefois · avant · d\'habitude · tous les jours · le samedi · souvent · toujours</p>')
    e = E("Je décris la photo de classe d'autrefois à l'imparfait (5 phrases).", f'<div class="grid2"><div>{photo("🧑‍🏫👧👧👧<br>⬛🔥🪑", "Classe de Mme Dubois · Charleroi · 1956", -2)}</div><div class="sm">Il y avait… · La maîtresse portait… · Les élèves étaient… · Au mur, il y avait… · Il faisait…</div></div>' + lines(5), ["regarde", "ecris"], 2, "C",
          sol="Ex. : Il y avait une maîtresse et des filles. Elles portaient un tablier. Il y avait un tableau noir et un poêle…")
    b.page(f'{l2}{e}', "Leçon 2")
    e = E("Avant / maintenant : je compare ma vie (4 phrases).", table(["Avant (imparfait)", "Maintenant (présent)"], [["J'habitais…", "J'habite…"], ["", ""], ["", ""], ["", ""]], ["91mm", "91mm"]).replace("<td></td>", '<td style="height:10mm"></td>'), ["ecris"], 2, "C", sol="Comparaisons personnelles.")
    e2 = E("J'écoute Nour parler de son enfance. Je coche ce qui est vrai.", table(["", "Vrai", "Faux"], [[x, '<span class="chk"></span>', '<span class="chk"></span>'] for x in ["Elle habitait dans une grande maison.", "Il y avait un citronnier dans la cour.", "Elle allait à l'école en bus.", "Le vendredi, toute la famille mangeait chez la grand-mère.", "Elle avait peur des chats."]], ["130mm", "26mm", "26mm"]), ["ecoute", "coche"], 2, "A",
           script="« Quand j'étais petite, nous habitions dans une maison avec une cour. Au milieu de la cour, il y avait un citronnier : ça sentait bon ! J'allais à l'école à pied avec ma sœur. Le vendredi, toute la famille mangeait chez ma grand-mère. Elle faisait le meilleur houmous du monde. Et j'adorais les chats du quartier ! »",
           sol="Faux (une maison avec une cour, pas dit « grande ») · Vrai · Faux (à pied) · Vrai · Faux (elle les adorait)")
    e3 = E("Jeu « Quand j'étais petit(e)… » : chacun dit une phrase vraie ou fausse. La classe devine.", '', ["parle", "groupe", "joue"], 1, "A", sol="Phrases à l'imparfait.")
    b.page(f'{e}{e2}{e3}', "S'entraîner")

    # ---------- Leçon 3 : imparfait ou passé composé ----------
    l3 = lecon("Imparfait ou passé composé ?", '''<div class="grid2"><div class="card" style="background:#ECE9FA"><b>IMPARFAIT 🖼️ = le décor</b><p class="sm">la description, la situation, l'habitude, ce qui <b>durait</b><br>Il <b>pleuvait</b>. J'<b>avais</b> 8 ans. Nous <b>étions</b> dans la cour.</p><p class="xs">d'habitude · souvent · tous les jours · pendant que</p></div>
<div class="card" style="background:#FFF3C4"><b>PASSÉ COMPOSÉ ⚡ = l'action</b><p class="sm">un événement précis, une action <b>finie</b>, ce qui <b>arrive</b> dans l'histoire<br>Soudain, mon frère <b>est tombé</b>. J'<b>ai crié</b>.</p><p class="xs">un jour · soudain · tout à coup · ce jour-là · à 10 h · trois fois</p></div></div>
<svg viewBox="0 0 180 26" width="100%" style="margin-top:2mm"><rect x="5" y="9" width="170" height="8" rx="4" fill="#C9C2EE"/><text x="90" y="15" font-size="5" text-anchor="middle" font-family="Poppins" font-weight="700">imparfait : je lisais… (ça dure)</text><path d="M118 2 L122 22 L126 2 Z" fill="#E4572E"/><text x="128" y="25" font-size="4.4" font-family="Poppins" font-weight="800" fill="#E4572E">⚡ le téléphone a sonné !</text></svg>
<p class="mt2">Une action longue (imparfait) est <b>interrompue</b> par une action courte (passé composé) : Je <b>dormais</b> quand mon père <b>est rentré</b>.</p>''')
    e = E("Je souligne le décor (imparfait) en violet et l'action (passé composé) en jaune.", '<div class="card big" style="line-height:1.8">C\'était un samedi. Il faisait beau. Nous étions au parc avec mon cousin. Tout à coup, un chien a pris notre ballon. Nous avons couru derrière lui. Le propriétaire riait. Finalement, il nous a rendu le ballon.</div>', ["lis", "souligne"], 1, "B",
          sol="Imparfait : c'était, faisait, étions, riait · Passé composé : a pris, avons couru, a rendu")
    b.page(f'{l3}{e}', "Leçon 3")
    e = E("Je choisis : imparfait ou passé composé ?", '<p>1. Quand j\'(avoir) ______ 10 ans, je (aller) ______ en Turquie pour la première fois. 2. Il (pleuvoir) ______ quand nous (arriver) ______. 3. Je (regarder) ______ la télé quand ma mère (appeler) ______. 4. D\'habitude, je (prendre) ______ le bus, mais ce jour-là, je (marcher) ______. 5. Nous (être) ______ fatigués, alors nous (rentrer) ______.</p>', ["complete"], 2, "C",
          sol="avais, suis allé(e) · pleuvait, sommes arrivés · regardais, a appelé · prenais, ai marché · étions, sommes rentrés")
    e2 = E("J'écoute l'histoire et je remplis le tableau : décor / actions.", table(["🖼️ Le décor (imparfait)", "⚡ Les actions (passé composé)"], [["", ""]], ["91mm", "91mm"]).replace("<td></td>", '<td style="height:30mm"></td>'), ["ecoute", "ecris"], 2, "A",
           script="« C'était l'hiver. Il neigeait beaucoup et il faisait très froid. Avec mes sœurs, nous étions dans le jardin. Soudain, ma petite sœur a lancé une boule de neige sur la fenêtre du voisin. La fenêtre s'est ouverte ! Nous avons couru dans la maison. Nous avions peur… mais le voisin a ri. »",
           sol="Décor : c'était l'hiver, il neigeait, il faisait froid, nous étions dans le jardin, nous avions peur · Actions : a lancé, s'est ouverte, avons couru, a ri")
    e3 = E("Je continue l'histoire (4 phrases) : « J'étais seul(e) à la maison. Il faisait nuit. Tout à coup… »", lines(4), ["ecris"], 3, "C", sol="Production : alternance décor / actions.")
    b.page(f'{e}{e2}{e3}', "S'entraîner")

    # ---------- Leçon 4 : raconter, réagir ----------
    l4 = lecon("Raconter un souvenir · réagir", table(["Pour…", "Je dis…"], [["commencer", "Je me souviens de… · Quand j'avais … ans, … · Il y a longtemps, …"], ["organiser", "D'abord… Ensuite… Tout à coup… Finalement / À la fin…"], ["dire ce que je ressentais", "J'avais peur. · J'étais très fier / fière. · J'avais honte !"], ["réagir (écouter)", "Ah bon ? · Vraiment ? · C'est drôle ! · Ça devait être difficile. · Moi aussi ! · Ça me rappelle…"], ["poser une question", "Tu avais quel âge ? · Qu'est-ce qui s'est passé ensuite ? · Comment tu te sentais ?"]], ["48mm", "134mm"]) +
               '<div class="astuce">Un souvenir, c\'est personnel : tu peux choisir un souvenir heureux, drôle… ou imaginaire. Tu racontes seulement ce que tu veux. 💜</div>')
    e = E("Je complète le dialogue avec des réactions.", '<p>— Quand j\'avais 7 ans, je me suis perdu au marché ! — ______________________</p><p>— Oui, j\'ai pleuré pendant une heure. — ______________________</p><p>— Finalement, un policier m\'a ramené chez moi. — ______________________</p>', ["ecris"], 2, "C",
          sol="Vraiment ? Tu avais peur ? · Ça devait être difficile ! · Ouf ! Heureusement !")
    b.page(f'{l4}{e}', "Leçon 4")
    e = E("Raconte-moi ! En duo : je raconte un souvenir (1 minute). Mon voisin réagit et pose 2 questions. Puis on change.", '<div class="card"><p class="sm">Idées : un anniversaire · un premier jour d\'école · une bêtise · un voyage · un animal · un jeu · une fête</p></div>', ["parle", "duo"], 2, "A",
          sol="Grille : imparfait pour le décor, passé composé pour les actions, réactions.")
    e2 = E("Je lis le souvenir de Yonas. Je trouve : quand ? où ? qui ? ce qui s'est passé ? les sentiments ?", '<div class="card"><p>« Je me souviens de mon premier match de foot. J\'avais 9 ans. Nous jouions sur un terrain plein de poussière, à Asmara. Il faisait très chaud. J\'étais le plus petit de l\'équipe et j\'étais nerveux. Tout à coup, le ballon est arrivé devant moi. J\'ai tiré… et j\'ai marqué ! Tous mes amis ont crié mon nom. J\'étais tellement fier ! »</p></div>' +
           table(["Quand ?", "Où ?", "Qui ?", "Ce qui s'est passé", "Sentiments"], [["", "", "", "", ""]], ["30mm", "34mm", "30mm", "52mm", "36mm"]).replace("<td></td>", '<td style="height:16mm"></td>'), ["lis", "ecris"], 2, "B",
           sol="à 9 ans · sur un terrain à Asmara · Yonas et son équipe · il a tiré et marqué, ses amis ont crié son nom · nerveux puis fier")
    b.page(f'{e}{e2}', "S'entraîner")

    # ---------- FLESco : frise ----------
    l5 = lecon("Lire une frise chronologique (méthode)", '''<p>1️⃣ Je repère le <b>sens</b> (de gauche = passé à droite = plus récent). 2️⃣ Je lis l'<b>échelle</b> (un trait = 1 an, 10 ans, 100 ans ?). 3️⃣ Je place les <b>dates</b> et les <b>périodes</b>. 4️⃣ Je compare : <b>avant</b>, <b>après</b>, <b>pendant</b>, combien d'années <b>entre</b> deux dates.</p>
<p><b>Les siècles</b> : le XIXᵉ siècle = 1801 → 1900 · le XXᵉ siècle = 1901 → 2000 · le XXIᵉ siècle = depuis 2001. <b>Une décennie</b> = 10 ans (les années 1950 = 1950 → 1959).<br><b>Chiffres romains</b> : I = 1 · V = 5 · X = 10 · L = 50 · C = 100 → XIX = 19 · XXI = 21</p>''')
    e = E("Je lis la frise de l'école en Belgique. Je réponds.", frise_ecole() + f'<p>1. En quelle année l\'école est devenue obligatoire jusqu\'à 18 ans ? {blank()} Dans quel siècle ? {blank()}</p><p>2. Combien d\'années entre la loi de 1914 et la création des DASPA ? {blank()}</p><p>3. Mme Dubois est née en 1948 : jusqu\'à quel âge l\'école était obligatoire pour elle ? {blank()}</p><p>4. Quel événement est le plus récent ? {blank("xl")}</p>',
          ["lis", "ecris"], 2, "B", sol="1. 1983 ; le XXe siècle — 2. 2012 − 1914 = 98 ans — 3. jusqu'à 14 ans (la loi de 1914) — 4. 2020 : l'école est obligatoire dès 5 ans")
    b.page(f'<span class="tag-doc">🎒 FRANÇAIS DE L\'ÉCOLE</span>{l5}{e}', "Consignes & école")
    e = E("J'écris en chiffres romains ou en chiffres arabes.", '<p>XVIIIᵉ siècle = ___ᵉ · XXᵉ = ___ᵉ · 21ᵉ siècle = ______ · 19ᵉ = ______ · Louis XIV = Louis ___ · le chapitre IX = chapitre ___</p>', ["ecris"], 2, "C", sol="18e · 20e · XXIe · XIXe · 14 · 9")
    e2 = E("Dans quel siècle ? Je relie.", relie(["1830 (indépendance de la Belgique)", "1953 (premières émissions de télévision belge)", "2007 (premiers smartphones à écran tactile)", "1914 (Première Guerre mondiale)"], ["XXIᵉ siècle", "XIXᵉ siècle", "XXᵉ siècle", "XXᵉ siècle"]), ["lis", "relie"], 2, "B",
           sol="1830 → XIXe · 1953 → XXe · 2007 → XXIe · 1914 → XXe")
    e3 = E("Ma frise : je place 5 événements de ma vie (naissance, école, une fête, un déménagement…) sur une frise avec une échelle.", '<svg viewBox="0 0 180 14" width="100%"><line x1="5" y1="7" x2="175" y2="7" stroke="#1F2A44" stroke-width="1.2"/><path d="M175 7 l-4 -3 v6z" fill="#1F2A44"/></svg><div class="card" style="height:30mm"></div>', ["dessine", "ecris"], 3, "C", sol="Frise orientée, échelle régulière, 5 dates.")
    b.page(f'{e}{e2}{e3}', "Consignes & école")

    # ---------- Documents de la vie ----------
    alb = '<div class="doc" style="transform:none;padding:4mm;background:#3B2F2F;border-radius:2mm"><div class="c" style="color:#F5E6C8;font-family:\'DejaVu Serif\';font-size:14pt;margin-bottom:3mm">📖 L\'album de Fatou</div><div class="grid3" style="gap:4mm">' + "".join([
        photo("👶🎂", "Mon premier anniversaire. J'avais un an et je pleurais devant le gâteau !", -3), photo("🏫👧", "Mon école à Conakry. L'uniforme était bleu et blanc.", 2), photo("🌊👨‍👧", "À la mer avec papa. On y allait chaque dimanche.", -1),
        photo("🥁💃", "La fête du quartier. Ma tante a dansé toute la nuit.", 1), photo("✈️🧳", "Le jour où nous sommes partis. J'étais triste et curieuse.", -2), photo("❄️😮", "Ma première neige en Belgique ! J'ai touché la neige… c'était froid !", 3)]) + '</div></div>'
    e = E("Je lis les légendes de l'album. Je réponds.", f'<p>1. Que faisait Fatou à son premier anniversaire ? {blank("xl")}</p><p>2. Comment était son uniforme ? {blank()}</p><p>3. Quelle photo montre une habitude ? Comment je le sais ? {blank("xl")}</p><p>4. Quels sentiments le jour du départ ? {blank()}</p><p>5. Je souligne dans les légendes 3 verbes à l\'imparfait et 3 au passé composé.</p>', ["lis", "ecris", "souligne"], 2, "B",
          sol="1. Elle pleurait devant le gâteau. — 2. bleu et blanc — 3. la mer : « chaque dimanche », « on y allait » (imparfait) — 4. triste et curieuse — 5. Imparfait : avais, pleurais, était, allait, étais · PC : a dansé, sommes partis, ai touché")
    b.page(f'<span class="tag-doc">📄 DOCUMENT DE LA VIE</span><h2>Un album photo</h2>{alb}<div class="mt4">{e}</div>', "Document de la vie")
    e = E("J'écris les légendes de 3 photos (ou dessins) de mon enfance ou de ma vie : 1 phrase à l'imparfait + 1 au passé composé pour chaque photo.", '<div class="grid3">' + ('<div><div class="card" style="height:40mm"></div>' + lines(2) + '</div>') * 3 + '</div>', ["dessine", "ecris"], 2, "C", sol="Légendes au passé.")
    e2 = E("Je prépare une interview d'un adulte de ma famille ou de l'école : « Comment était votre enfance ? » J'écris 6 questions à l'imparfait.", lines(6), ["ecris"], 2, "C",
           sol="Ex. : Où habitiez-vous ? À quoi jouiez-vous ? Comment était votre école ? Qu'est-ce que vous mangiez ? Aviez-vous la télé ? Quel était votre meilleur souvenir ?")
    b.page(f'<span class="tag-doc">📄 DOCUMENT DE LA VIE</span><h2>Mon album · une interview</h2>{e}{e2}', "Document de la vie")

    # ---------- Sons : [e] / [ɛ] ----------
    e = E("Passé composé [e] ou imparfait [ɛ] ? J'écoute et je répète.", '<div class="grid2"><div class="card c"><div class="huge">j\'ai joué [e]</div><p>la bouche sourit 😁<br>j\'ai mangé · j\'ai parlé · j\'ai dansé</p></div><div class="card c"><div class="huge">je jouais [ɛ]</div><p>la bouche s\'ouvre 😮<br>je mangeais · je parlais · je dansais</p></div></div>', ["ecoute", "repete"], 1, "A",
          script="Opposer : j'ai joué / je jouais ; j'ai chanté / je chantais ; il a parlé / il parlait. Attention : « je » ≠ « j'ai » aussi !", sol="Activité orale.")
    e2 = E("J'écoute et je coche : passé composé ou imparfait ?", checks(8, ["passé composé", "imparfait"]), ["ecoute", "coche"], 2, "A", script="1. j'ai mangé — 2. je mangeais — 3. il parlait — 4. il a parlé — 5. nous jouions — 6. j'ai dansé — 7. tu chantais — 8. elle a écouté",
           sol="1. PC — 2. I — 3. I — 4. PC — 5. I — 6. PC — 7. I — 8. PC")
    e3 = E("Je lis à voix haute en faisant bien la différence.", '<div class="card big" style="line-height:1.9">Je regardais la télé quand j\'ai entendu un bruit. Je chantais, et j\'ai chanté encore plus fort ! Il pleuvait, alors j\'ai pris mon parapluie.</div>', ["lis", "parle"], 2, "B", sol="Lecture expressive.")
    b.page(f'<h2>J\'écoute bien · j\'ai joué / je jouais</h2>{e}{e2}{e3}', "Sons")
    e = E("🔁 Module 2 · y et en.", '<p>Tu allais souvent au parc ? — Oui, j\'___ allais tous les jours. Tu reviens de chez ta grand-mère ? — Oui, j\'___ reviens.</p>', ["complete"], 2, "C", sol="y · en")
    e2 = E("🔁 Module 2 · Les prépositions.", '<p>Dans ma chambre, il y avait un lit ______ la fenêtre et une étagère ______ le lit (plus haut).</p>', ["complete"], 1, "C", sol="sous / devant / à côté de · au-dessus du")
    e3 = E("🔁 Module 1 · Passé composé avec être.", '<p>Ma sœur (naître) ______________ en 2015. Nous (partir) ______________ en été.</p>', ["complete"], 2, "C", sol="est née · sommes partis")
    b.page(f'<h2>🔁 Je révise les modules 1 et 2</h2>{e}{e2}{e3}', "Je révise")

    # ---------- Ateliers ----------
    e = E("Les jeux de cour du monde : en groupe, je présente un jeu de mon pays à l'imparfait (« On jouait à… On était… On devait… Le gagnant… »). Puis la classe y joue à la récré !", table(["Nom du jeu (et pays)", "Matériel", "Règles (imparfait)", "Le gagnant"], [["", "", "", ""]], ["40mm", "34mm", "70mm", "38mm"]).replace("<td></td>", '<td style="height:42mm"></td>'), ["parle", "ecris", "groupe"], 2, "A",
          sol="Règles à l'imparfait (habitude).")
    cards = [("Avant, on écrivait des lettres.", "Maintenant, on envoie des messages."), ("Avant, on regardait la télé en noir et blanc.", "Maintenant, on regarde des séries sur une tablette."), ("Avant, on lavait le linge à la main.", "Maintenant, on a une machine à laver."), ("Avant, on cherchait dans un dictionnaire.", "Maintenant, on cherche sur internet.")]
    e2 = E("Le mémory Avant / Maintenant : je découpe les cartes. Je retourne 2 cartes : si elles vont ensemble, je lis les 2 phrases et je garde la paire.", '<div class="grid4">' + "".join(f'<div class="card c" style="border-style:dashed;min-height:24mm;padding:2mm"><span class="xs">🕰️</span><p class="sm">{a}</p></div>' for a, _ in cards) + "".join(f'<div class="card c" style="border-style:dashed;min-height:24mm;padding:2mm"><span class="xs">📱</span><p class="sm">{m}</p></div>' for _, m in cards) + '</div>', ["decoupe", "lis", "joue"], 1, "D",
           sol="Paires : lettres / messages · télé noir et blanc / séries · linge à la main / machine · dictionnaire / internet")
    b.page(f'{atl_head("A", "Atelier · Jeux d autrefois et d ailleurs")}{e}{e2}'.replace("d autrefois et d ailleurs", "d'autrefois et d'ailleurs"), "Atelier")
    e = E("Le dé des histoires : je lance le dé 3 fois (lieu, personnage, événement) et j'invente une histoire au passé (6 phrases).", table(["🎲", "Lieu (décor)", "Personnage", "Événement"], [[str(i)] + r for i, r in enumerate([["à la plage", "mon grand-père", "un orage a éclaté"], ["dans la forêt", "un chat noir", "j'ai trouvé une clé"], ["à l'école", "la directrice", "la lumière s'est éteinte"], ["au marché", "un clown", "j'ai perdu mon sac"], ["dans le train", "un footballeur", "le train s'est arrêté"], ["chez moi", "mon meilleur ami", "quelqu'un a sonné"]], 1)], ["12mm", "56mm", "56mm", "58mm"]) + lines(5), ["joue", "ecris"], 2, "C",
          sol="Récit : décor à l'imparfait, événements au passé composé.")
    b.page(f'{atl_head("C", "Atelier · Inventer une histoire")}{e}', "Atelier")

    # ---------- ★ Coup de pouce ----------
    e = E("Je lis le souvenir. Je souligne les verbes.", '<div class="card" style="background:#F2FBF7"><p class="big" style="line-height:1.9">Quand j\'étais petit, j\'habitais au Maroc.<br>Il faisait chaud.<br>Je jouais au ballon avec mes amis.<br>Un jour, j\'ai cassé une fenêtre ! 🪟💥<br>J\'avais très peur.</p></div>', ["lis", "souligne"], 1, "P", alpha=True,
          sol="étais · habitais · faisait · jouais · ai cassé · avais")
    e2 = E("Je complète la recette de l'imparfait.", '<div class="card"><p class="big">jouer → nous jou<b>ons</b> → je jou____ · tu jou____ · il jou____</p><p class="big">finir → nous finiss<b>ons</b> → je finiss____</p><p class="big">être → j\'ét____</p></div>', ["complete"], 1, "C", alpha=True, sol="jouais, jouais, jouait · finissais · étais")
    b.page(CP.format(t="Je lis un souvenir") + e + e2, "★ Coup de pouce")
    e = E("Décor 🖼️ ou action ⚡ ? Je relie.", relie(["Il pleuvait.", "J'ai ouvert la porte.", "J'avais 8 ans.", "Le chien est entré."], ["⚡ action", "🖼️ décor", "🖼️ décor", "⚡ action"]), ["lis", "relie"], 1, "B", alpha=True, sol="pleuvait → décor · ai ouvert → action · avais → décor · est entré → action")
    e2 = E("J'écris mon souvenir avec le modèle.", '<div class="card" style="background:#F2FBF7"><p class="big" style="line-height:2.2">Quand j\'étais petit(e), j\'habitais à ____________.<br>Je jouais à / au ____________ avec ____________.<br>Un jour, ____________________________.<br>J\'étais ____________ (content(e) / triste / fier, fière).</p></div>', ["ecris"], 1, "C", alpha=True, sol="Texte personnel sur le modèle.")
    b.page(CP.format(t="J'écris avec un modèle") + e + e2, "★ Coup de pouce")

    # ---------- Tâche finale ----------
    e = E("Je prépare mon récit : je choisis un souvenir (heureux, drôle, ou imaginaire) et je remplis le plan.", table(["Étape", "Mes idées"], [["🖼️ La situation (imparfait) : quand ? où ? qui ? quel temps ?", ""], ["🔁 Une habitude (imparfait)", ""], ["⚡ L'événement (passé composé) : un jour, tout à coup…", ""], ["⚡ La suite (passé composé)", ""], ["💭 Les sentiments (imparfait)", ""], ["🔚 La fin : finalement… aujourd'hui, quand j'y pense…", ""]], ["70mm", "112mm"]).replace("<td></td>", '<td style="height:15mm"></td>'), ["ecris"], 1, "C",
          sol="Plan complet.")
    b.page(tache_head("Le récit d'un souvenir", "J'écris le récit d'un souvenir (12 lignes), je l'illustre, puis je le raconte à la classe sans lire. On fait un recueil « Nos souvenirs ».") + e, "Tâche finale", levels=False)
    e = E("J'écris mon récit (12 lignes) avec un titre. J'ajoute un dessin ou une photo.", '<p>Titre : ________________________________</p>' + lines(11), ["ecris", "dessine"], 2, "C", sol="Évaluation avec la grille du livret.")
    b.page(e + table(["Je vérifie :", "✅"], [[x, '<span class="chk"></span>'] for x in ["La situation est décrite à l'imparfait.", "Les événements sont au passé composé.", "J'utilise 3 mots du temps (un jour, tout à coup, finalement…).", "Je dis ce que je ressentais.", "Je raconte à l'oral sans lire et je réponds aux questions."]], ["160mm", "22mm"]), "Tâche finale", levels=False)
    e = E("Je révise.", '<p>1. nous (faire) → imparfait : ______ 2. Quand j\'(être) ______ petit… 3. Il (pleuvoir) ______ quand je (sortir) ______. 4. 1990 = ___ᵉ siècle. 5. Pour réagir : « Ça ______ être difficile ! »</p>', ["ecris"], 2, "C",
          sol="faisions · étais · pleuvait, suis sorti(e) · XXe · devait")
    e2 = E("Défi ! Je corrige les 5 erreurs.", '<div class="card big">Quand j\'ai été petit, je jouait au foot. Un jour, il pleuvait et je tombais. Mes amis étaient rire. J\'avais mal mais j\'étais fier.</div>' + lines(2), ["barre", "ecris"], 3, "C",
           sol="Quand j'étais petit · je jouais · je suis tombé · mes amis ont ri / riaient · (avais mal, étais fier : justes)")
    b.page(f'<h2>🔁 Je révise tout le module</h2>{e}{e2}', "Je révise")

    # ---------- Test ----------
    Q = [("🪢 C'est…", ["la marelle", "la corde à sauter", "les billes", "la toupie"]), ("Autrefois, on écrivait avec…", ["un smartphone", "une plume et de l'encre", "un tableau interactif", "un ordinateur"]),
         ("jouer → imparfait (je) :", ["je jouai", "je jouais", "je jouait", "je joué"]), ("finir → imparfait (nous) :", ["nous finions", "nous finissions", "nous finissons", "nous finirons"]), ("être → imparfait (je) :", ["j'étais", "j'êtais", "je suis été", "j'été"]),
         ("Ils ____ au parc. (aller, imparfait)", ["allaient", "allait", "allions", "vont"]), ("manger → imparfait (je) :", ["je mangais", "je mangeais", "je mangé", "je mangeait"]), ("il y a → imparfait :", ["il y avait", "il y a eu", "il y était", "il avait"]),
         ("Pour une habitude passée :", ["Un jour, j'ai joué.", "Tous les jours, je jouais.", "Soudain, j'ai joué.", "Je vais jouer."]), ("Pour décrire le temps passé :", ["Il a fait beau.", "Il faisait beau.", "Il fait beau.", "Il fera beau."]),
         ("Je dormais quand le téléphone ____.", ["sonnait", "a sonné", "sonne", "sonnera"]), ("Tout à coup, un chien ____ dans la classe.", ["entrait", "est entré", "entre", "entrera"]), ("Quand j'____ 6 ans, je suis allé à l'école.", ["ai eu", "avais", "ai", "aurai"]),
         ("Mot pour une action soudaine :", ["d'habitude", "souvent", "tout à coup", "tous les jours"]), ("Réagir à un souvenir triste :", ["C'est nul.", "Ça devait être difficile.", "Et alors ?", "Bof."]),
         ("Le XXᵉ siècle :", ["1801-1900", "1901-2000", "2001-2100", "1900-1999"]), ("XIX =", ["9", "14", "19", "21"]), ("Sur une frise, le plus récent est…", ["à gauche", "à droite", "en haut", "au milieu"]),
         ("« je jouais » : on entend…", ["[e] comme « été »", "[ɛ] comme « mère »", "[a]", "[ø]"]), ("🔁 Tu allais au parc ? — Oui, j'____ allais.", ["en", "y", "le", "lui"])]
    ans = ["la corde à sauter", "une plume et de l'encre", "je jouais", "nous finissions", "j'étais", "allaient", "je mangeais", "il y avait", "Tous les jours, je jouais.", "Il faisait beau.", "a sonné", "est entré", "avais", "tout à coup", "Ça devait être difficile.", "1901-2000", "19", "à droite", "[ɛ] comme « mère »", "y"]
    key = key_from(Q, ans)
    test_pages(b, 3, "Souvenirs d'enfance", Q, f'<h3>B1. Je décris mon école d\'avant ou mon quartier d\'enfance (3 phrases à l\'imparfait). (… / 3)</h3>{lines(2, True)}<h3>B2. Je complète : « Je lisais dans ma chambre quand… » + 2 phrases. (… / 3)</h3>{lines(2, True)}<h3>B3. Je raconte un souvenir (5 phrases : décor + événement + sentiment). (… / 4)</h3>{lines(3, True)}',
               [["raconter un souvenir (1 minute)", "/ 4", ""], ["dire 3 habitudes de mon enfance", "/ 3", ""], ["réagir au souvenir de la prof", "/ 3", ""]],
               f'<h3>1. Je lis et je réponds. (… / 6)</h3><div class="card big" style="line-height:1.7">Quand j\'étais petite, j\'habitais en Ukraine. Il neigeait beaucoup. Je faisais du patin. Un jour, je suis tombée sur la glace.</div><p>Pays : ______ Météo : ______ Activité : ______ Événement : ______</p><h3>2. Décor ou action ? J\'entoure. (… / 4)</h3><div class="card big">Il faisait froid. 🖼️ ⚡ · Je suis tombée. 🖼️ ⚡ · J\'avais 7 ans. 🖼️ ⚡ · Ma mère a crié. 🖼️ ⚡</div><h3>3. Je complète : Quand j\'étais petit(e), je jouais… (… / 6)</h3>{lines(1, True)}<h3>4. Je dis un souvenir à la prof (oral). (… / 4)</h3><div class="card">☐ je comprends ☐ « quand j\'étais petit(e) » ☐ 1 verbe à l\'imparfait ☐ phrase complète</div>')
    closing(b, 3, ["Je sais nommer des jeux d'enfance et des objets d'autrefois.", "Je sais former l'imparfait (nous -ons → -ais…).", "Je sais utiliser l'imparfait pour décrire.", "Je sais utiliser l'imparfait pour les habitudes passées.", "Je sais choisir imparfait ou passé composé.",
                   "Je sais organiser un récit (un jour, tout à coup, finalement).", "Je sais dire ce que je ressentais.", "Je sais réagir quand quelqu'un raconte.", "Je sais lire une frise (siècles, chiffres romains).", "Je sais lire un album photo et un témoignage.", "Je sais écrire le récit d'un souvenir."],
            JEUX[:8] + AUTREFOIS[:6] + [("💭", "le souvenir"), ("🕰️", "autrefois"), ("🔁", "d'habitude"), ("⚡", "tout à coup"), ("🔚", "finalement"), ("😨", "avoir peur"), ("😌", "être fier / fière"), ("📜", "le siècle"), ("📏", "la frise"), ("🎙️", "le témoignage")])
    plan_de_travail(b, E, 3, ["L'imparfait : formation", "L'imparfait : emplois", "Imparfait ou passé composé ?", "Raconter un souvenir, réagir", "Lire une frise chronologique"], "☐ Le plan de mon souvenir<br>☐ Mon récit illustré<br>☐ Je raconte à la classe")
    if render:
        to_pdf(b.html(), '/home/claude/syllabus/out/V2_M3_eleve.pdf')

    pg, exs = helpers(b, E)
    CPp = b.marks["★ Coup de pouce"]
    days = [("1", "Collectif", f"Ouverture · BD ({pg('Découvrir')})", f"Coup de pouce : souvenir court (p. {CPp[0]})"), ("2", "Collectif", f"Témoignage · jeux et autrefois ({pg('Lexique')})", "Coup de pouce : lexique en images"),
            ("3", "Rotation", f"📌 Leçon 1 formation ({pg('Leçon 1')})", "Coup de pouce : recette de l'imparfait"), ("4", "Rotation", f"📌 Leçon 2 emplois ({pg('Leçon 2')})", "Coup de pouce : avant / maintenant"),
            ("5", "Collectif", f"📌 Leçon 3 imparfait / PC ({pg('Leçon 3')}) · sons ({pg('Sons')})", f"Coup de pouce : décor ou action (p. {CPp[1]})"), ("6", "Rotation", f"📌 Leçon 4 raconter, réagir ({pg('Leçon 4')})", "Coup de pouce : réagir à l'oral"),
            ("7", "Collectif", f"Frise ({pg('Consignes & école')})", "Coup de pouce : ma frise simple"), ("8", "Rotation", f"Album, interview ({pg('Document de la vie')}) · ateliers ({pg('Atelier')})", "Coup de pouce : légendes de photos"),
            ("9", "Seul", f"Tâche finale ({pg('Tâche finale')})", "Coup de pouce : souvenir sur le modèle"), ("10", "Seul", f"Test ({pg('Test')})", f"Coup de pouce : test adapté ({pg('★ Coup de pouce · Test')})")]
    rot = [["🎧 Écouter-Parler", "Raconte-moi ! · jeux de cour du monde", "20 min", "—"], ["📖 Lire", "Témoignage · album de Fatou · souvenir de Yonas", "20 min", "Oui"], ["✏️ Écrire", "Imparfait / PC · dé des histoires", "20 min", "● oui"],
           ["🧩 Jouer", "Mémory avant / maintenant", "20 min", "Paires au dos"], ["👩‍🏫 Table d'appui", "Coup de pouce · décor / action", "20 min", "—"]]
    ev1 = '''<h3>Partie B (10 points)</h3><p class="sm"><b>B1</b> : 1 pt par phrase à l'imparfait correcte · <b>B2</b> : <span class="sol">… quand ma mère est entrée / quand j'ai entendu un bruit.</span> (PC juste 1, 2 phrases cohérentes 2) · <b>B3</b> : décor à l'imparfait (1), événement au PC (1), sentiment (1), organisation (1).</p>
<h3>Test ★ Coup de pouce</h3><p class="sm"><b>Ex. 1 :</b> <span class="sol">l'Ukraine · il neigeait · le patin · elle est tombée</span> · <b>Ex. 2 :</b> <span class="sol">🖼️ · ⚡ · 🖼️ · ⚡</span> · <b>Ex. 3 :</b> phrase personnelle.</p>'''
    ev2 = f'''<h2>Grille · tâche finale « Le récit d'un souvenir »</h2>{table(["Critère", "Très bien", "Bien", "À retravailler", "Points"], [["<b>Structure</b> : situation, événements, sentiments, fin", "Complète", "Partielle", "Désorganisée", "/ 4"], ["<b>Imparfait</b> (formes et emplois)", "Juste", "Quelques erreurs", "Beaucoup", "/ 5"], ["<b>Passé composé</b> (auxiliaire, accords)", "Juste", "Quelques erreurs", "Beaucoup", "/ 4"], ["<b>Mots du temps</b>, vocabulaire des sentiments", "Variés", "Quelques-uns", "Absents", "/ 3"], ["<b>Oral</b> : raconter sans lire, répondre", "Fluide", "Hésitant", "Lu", "/ 4"]], ["64mm", "32mm", "32mm", "32mm", "22mm"])}
<h2 class="mt4">Différencier et remédier</h2>{table(["Difficulté", "Remédiation"], [["Former l'imparfait", "Toujours partir de « nous » ; tableau des terminaisons affiché ; chant des terminaisons."], ["Imparfait / PC", "Métaphore du film : le décor (imparfait) / les actions (PC) ; frise avec ruban long et éclair ⚡."], ["Prononciation j'ai joué / je jouais", "Miroir : sourire [e] / bouche ouverte [ɛ] ; dictée de paires."], ["Siècles", "Règle : on ajoute 1 aux deux premiers chiffres (1953 → 19 + 1 = 20e)."], ["Élève rapide", "Interview réelle d'un adulte (6 questions), rédigée et lue à la classe ; comparaison d'une photo d'autrefois / d'aujourd'hui."]], ["50mm", "132mm"])}
<div class="astuce mt4"><b>Prudence et bienveillance :</b> les souvenirs d'enfance peuvent réveiller des souffrances (guerre, deuil, séparation). Toujours offrir le choix d'un souvenir heureux, drôle ou <b>imaginaire</b>, ou le souvenir d'une autre personne (interview). Ne pas exiger de photo. Si un élève se livre, accueillir sans relancer et en parler au CPMS si nécessaire.</div>'''
    T = teacher_book(b, E, "V2 · M3", "", MC, 3, "Souvenirs d'enfance",
                     "<li><b>Communication :</b> raconter et décrire au passé, réagir à un récit.</li><li><b>Lexique :</b> jeux d'enfance, école d'autrefois, sentiments, marqueurs temporels.</li><li><b>Grammaire :</b> imparfait (formation, emplois) ; imparfait ou passé composé.</li><li><b>Phonétique :</b> j'ai joué [e] / je jouais [ɛ].</li><li><b>FLSco :</b> frise chronologique, siècles, chiffres romains.</li><li><b>Documents :</b> témoignage, album photo, interview.</li><li><b>★ Coup de pouce :</b> souvenir court, recette de l'imparfait, décor / action.</li>",
                     '<p class="sm"><b style="color:#E4572E">Indispensable</b> : imparfait des verbes fréquents (être, avoir, faire, aller, -er), « quand j\'étais petit(e) ».</p><p class="sm"><b style="color:#d9a400">Important</b> : imparfait / passé composé, mots du temps.</p><p class="sm"><b style="color:#2BA88F">Enrichissement</b> : frise, siècles, récit long.</p>',
                     "Photos d'enfance (facultatif, avec accord) ou dessins · objets d'autrefois si possible (plume, encrier, vieux cartable) · ruban pour la frise · dés.", "<b>Invité possible :</b> une personne âgée du quartier ou de l'école vient raconter son enfance (préparer les questions à l'imparfait p. du document de la vie).",
                     days, "« Quand j'étais petit(e)… » en chaîne · un verbe du jour à l'imparfait · le mot d'autrefois du jour.", rot, key, (ev1, ev2), start=tstart)
    if render:
        to_pdf(T.html(), '/home/claude/syllabus/out/V2_M3_prof.pdf')
    return b, T


if __name__ == "__main__":
    b, T = build_v2m3()
    print(b.n, T.n)
