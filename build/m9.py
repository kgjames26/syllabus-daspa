"""Volume 1 · Module 9 « Ma ville, mon quartier »."""
import sys
sys.path.insert(0, '/home/claude/syllabus')
from lib.base import *
from lib.art import *
from lib.alpha import AL, letter_page, syll_table
from lib.module import *
from lib.render import to_pdf

MC = "#7A5BC7"
LIEUX = [("🚉", "la gare"), ("🏦", "la banque"), ("⛪", "l'église"), ("🏥", "l'hôpital"), ("🏫", "l'école"), ("🏛️", "la maison communale"), ("📮", "la poste"), ("🌳", "le parc"),
         ("💊", "la pharmacie"), ("🛒", "le supermarché"), ("📚", "la bibliothèque"), ("🏊", "la piscine"), ("🍟", "la friterie"), ("🏠", "la maison"), ("🚒", "la caserne des pompiers"), ("⚽", "le terrain de foot"),
         ("👮", "le commissariat"), ("🕌", "la mosquée"), ("🎬", "le cinéma"), ("🏪", "le magasin")]
TRANS = [("🚶", "à pied"), ("🚲", "à vélo"), ("🛴", "en trottinette"), ("🚌", "en bus"), ("🚋", "en tram"), ("🚇", "en métro"), ("🚆", "en train"), ("🚗", "en voiture")]
# plan : (colonne, ligne) -> (emoji, nom)
PLAN = {(0, 0): ("🚉", "gare"), (1, 0): ("🏦", "banque"), (2, 0): ("⛪", "église"), (3, 0): ("🏥", "hôpital"),
        (0, 1): ("🏫", "école"), (1, 1): ("🏛️", "maison communale"), (2, 1): ("📮", "poste"), (3, 1): ("🌳", "parc"),
        (0, 2): ("💊", "pharmacie"), (1, 2): ("🛒", "supermarché"), (2, 2): ("📚", "bibliothèque"), (3, 2): ("🏊", "piscine"),
        (0, 3): ("🍟", "friterie"), (1, 3): ("🏠", "chez Yonas"), (2, 3): ("🚒", "pompiers"), (3, 3): ("⚽", "foot")}


def plan_quartier(blank_names=False, route=None):
    W, H, s = 200, 170, 6  # s = demi-largeur de rue
    xs, ys = [0, 50, 100, 150, 200], [0, 42, 84, 126, 168]
    out = [f'<rect x="0" y="0" width="{W}" height="{H}" fill="#9AA3B2"/>']
    for c in range(4):
        for r in range(4):
            x0, x1 = xs[c] + (s if c else 2), xs[c + 1] - (s if c < 3 else 2)
            y0, y1 = ys[r] + (s if r else 2), ys[r + 1] - (s if r < 3 else 2)
            em, n = PLAN[(c, r)]
            fill = "#CDE8C2" if n in ("parc", "foot") else "#F4EFE6"
            out.append(f'<rect x="{x0}" y="{y0}" width="{x1 - x0}" height="{y1 - y0}" rx="2" fill="{fill}" stroke="#7d8597" stroke-width=".4"/>')
            out.append(f'<text x="{(x0 + x1) / 2}" y="{(y0 + y1) / 2 + 2}" font-size="13" text-anchor="middle">{em}</text>')
            lab = "" if blank_names else n
            out.append(f'<text x="{(x0 + x1) / 2}" y="{y1 - 3}" font-size="4.6" text-anchor="middle" font-family="Poppins" font-weight="700" fill="#1F2A44">{lab}</text>')
            out.append(f'<text x="{x0 + 2.5}" y="{y0 + 5}" font-size="4" font-family="Poppins" fill="#9aa1b1">{"ABCD"[c]}{r + 1}</text>')
    for y, n in [(42, "rue de la Gare"), (84, "rue du Marché"), (126, "avenue des Tilleuls")]:
        out.append(f'<text x="100" y="{y + 1.6}" font-size="4.2" text-anchor="middle" font-family="Poppins" font-style="italic" fill="#fff">{n}</text>')
    for x, n in [(50, "rue de l'Église"), (100, "rue Haute"), (150, "rue Verte")]:
        out.append(f'<text x="{x + 1.5}" y="105" font-size="4.2" text-anchor="middle" font-family="Poppins" font-style="italic" fill="#fff" transform="rotate(-90 {x + 1.5} 105)">{n}</text>')
    if route:
        out.append(f'<polyline points="{route}" fill="none" stroke="#E4572E" stroke-width="2" stroke-dasharray="3 2" stroke-linecap="round"/>')
    out.append('<g transform="translate(207,14)"><circle r="8" fill="#fff" stroke="#1F2A44" stroke-width=".6"/><path d="M0 -6 L3 2 L0 0 L-3 2Z" fill="#E4572E"/><text y="6" font-size="4.5" text-anchor="middle" font-family="Poppins" font-weight="800">N</text></g>')
    return f'<svg viewBox="0 0 {W + 16} {H}" width="100%" style="max-height:140mm;border-radius:2mm">{"".join(out)}</svg>'


def sign(kind, txt=""):
    shapes = {
        "stop": '<polygon points="12,2 28,2 38,12 38,28 28,38 12,38 2,28 2,12" fill="#D32F2F" stroke="#fff" stroke-width="1.5"/><text x="20" y="24" font-size="9" text-anchor="middle" font-family="Poppins" font-weight="800" fill="#fff">STOP</text>',
        "interdit": '<circle cx="20" cy="20" r="18" fill="#D32F2F"/><rect x="8" y="17" width="24" height="6" fill="#fff"/>',
        "parking": '<rect x="3" y="3" width="34" height="34" rx="4" fill="#1565C0"/><text x="20" y="30" font-size="24" text-anchor="middle" font-family="Poppins" font-weight="800" fill="#fff">P</text>',
        "ecole": '<polygon points="20,3 38,36 2,36" fill="#fff" stroke="#D32F2F" stroke-width="3.5"/><text x="20" y="32" font-size="13" text-anchor="middle">🚸</text>',
        "pieton": '<rect x="3" y="3" width="34" height="34" rx="3" fill="#1565C0"/><polygon points="20,7 34,32 6,32" fill="#fff"/><text x="20" y="30" font-size="11" text-anchor="middle">🚶</text>',
        "velo": '<circle cx="20" cy="20" r="18" fill="#1565C0"/><text x="20" y="26" font-size="16" text-anchor="middle">🚲</text>',
        "bus": '<rect x="3" y="3" width="34" height="34" rx="3" fill="#fff" stroke="#1F2A44" stroke-width="1.5"/><text x="20" y="26" font-size="16" text-anchor="middle">🚌</text>',
        "sortie": '<rect x="3" y="8" width="34" height="24" rx="2" fill="#2E7D32"/><text x="20" y="24" font-size="8" text-anchor="middle" font-family="Poppins" font-weight="800" fill="#fff">SORTIE</text>',
    }
    return f'<svg viewBox="0 0 40 40" width="16mm">{shapes[kind]}</svg>'


def build_m9(start=1, tstart=1, render=True):
    b = Book("V1 · M9", "Volume 1 · Premiers pas · Module 9 · Ma ville, mon quartier", MC, start=start)
    E = Ex(b)
    vis = '<div class="c" style="font-size:40pt;line-height:1.3">🏫🏥📮🚉🏦<br>🚌🚲🚶🗺️🚦</div>'
    opening(b, MC, 9, "Ma ville, mon quartier", vis, [("🏙️", "nommer les lieux de la ville"), ("🚌", "dire comment je me déplace"), ("📍", "dire où c'est : à côté de, en face de…"),
            ("🧭", "demander et expliquer un chemin"), ("🗺️", "lire un plan et un horaire de bus"), ("🚸", "comprendre les panneaux")],
            ["Tu habites loin de l'école ?", "Tu viens à l'école comment : à pied, en bus ?", "Qu'est-ce qu'il y a dans ton quartier ?"],
            ["la rue", "le quartier", "à gauche", "à droite", "tout droit", "à côté de", "en face de", "le bus", "l'arrêt", "le plan"], "#EFEAFB")

    # ---------- Découvrir ----------
    bd = '<div class="grid2" style="gap:3mm">' + "".join([
        bd_case(1, lr("daria", ["Pardon, Monsieur ! Je cherche la bibliothèque, s'il vous plaît."], extra='<div class="c" style="font-size:22pt">🗺️❓</div>')),
        bd_case(2, f'<div class="flex top" style="margin-top:5mm">{face(size=72, skin="mat", hair="#333", style="court", glasses=True, shirt="#6B8F3E")}<div>{bub("La bibliothèque ? C&#39;est près d&#39;ici. Tu es à pied ?")}</div></div><div class="flex top" style="justify-content:flex-end">{bub("Oui, je suis à pied.")}{avatar("daria", 70, flip=True)}</div>'),
        bd_case(3, f'<div class="flex top" style="margin-top:5mm">{face(size=72, skin="mat", hair="#333", style="court", glasses=True, shirt="#6B8F3E")}<div>{bub("Va tout droit dans la rue du Marché. Ensuite, traverse la rue Haute.")}</div></div><div class="c" style="font-size:24pt">⬆️🚸</div>'),
        bd_case(4, f'<div class="flex top" style="margin-top:5mm">{face(size=72, skin="mat", hair="#333", style="court", glasses=True, shirt="#6B8F3E")}<div>{bub("La bibliothèque est à droite, en face de la poste.")}</div></div><div class="flex top" style="justify-content:flex-end">{bub("À droite, en face de la poste. Merci beaucoup !")}{avatar("daria", 70, "rire", flip=True)}</div>'),
        bd_case(5, lr("daria", ["Oh non ! Je suis perdue… Ici, il y a une friterie et des pompiers."], "yonas", ["Daria ! Qu'est-ce que tu fais ici ? J'habite à côté !"], "triste", "surpris")),
        bd_case(6, lr("yonas", ["Tu as tourné à gauche ! Viens, on y va ensemble."], "daria", ["Merci, Yonas ! Je ne connais pas encore bien le quartier."], "rire", "sourire", '<div class="c" style="font-size:22pt">🚶‍♀️🚶📚</div>')),
    ]) + '</div>'
    e = E("J'écoute et je regarde la BD : je cherche la bibliothèque.", bd, ["ecoute", "regarde"], 1, "A",
          script="Lire deux fois. Montrer avec les bras : à gauche, à droite, tout droit. Faire répéter : « Pardon, je cherche… », « C'est loin ? », « Va tout droit, tourne à gauche ».", sol="Activité orale.")
    b.page(f'<h2>Découvrir · Je cherche la bibliothèque</h2>{e}', "Découvrir")
    e = E("Je réponds.", f'<p>1. Daria cherche quel lieu ? {blank("l")}</p><p>2. Elle est à pied ou en bus ? {blank()}</p><p>3. Le monsieur dit : va tout droit dans la rue… {blank("l")}</p><p>4. La bibliothèque est en face de… {blank()}</p><p>5. Pourquoi Daria est perdue ? {blank("xl")}</p>',
          ["lis", "ecris"], 1, "B", sol="1. la bibliothèque — 2. à pied — 3. du Marché — 4. la poste — 5. Elle a tourné à gauche (elle ne connaît pas bien le quartier).")
    e2 = E("Vrai ou faux ?", vf(["La bibliothèque est loin.", "Daria doit traverser la rue Haute.", "Yonas habite à côté de la friterie.", "Daria connaît bien le quartier."]), ["lis", "coche"], 2, "B", sol="Faux (c'est près) · Vrai · Vrai · Faux")
    e3 = E("Défi ! Avec mon voisin, je joue la scène. Je change le lieu (la piscine, la gare…).", lines(2), ["parle", "duo"], 3, "A", sol="Jeu de rôle : Pardon, je cherche… Va tout droit… Merci !")
    b.page(f'{e}{e2}{e3}<div class="astuce">🇧🇪 En Belgique, la <b>maison communale</b> = la mairie (en France). On y va pour la carte d\'identité, le domicile… Une <b>friterie</b> (ou « fritkot ») vend des frites !</div>', "Découvrir")

    # ---------- Lexique ----------
    e = E("Les lieux de la ville. J'écoute et je répète.", emogrid(LIEUX, 5), ["ecoute", "repete"], 1, "A",
          script="Dire chaque lieu. Demander : « Qu'est-ce qu'on fait à la poste ? » → On envoie une lettre. À la banque ? À la maison communale ?", sol="Activité orale.")
    b.page(f'<h2>Les lieux de la ville</h2>{e}', "Lexique")
    e = E("Où est-ce que je vais ? Je relie.", relie(["Je veux un livre.", "J'ai mal, c'est grave.", "Je prends le train.", "Je veux nager.", "J'envoie un colis.", "Je fais ma carte d'identité."], ["à la piscine", "à la maison communale", "à la bibliothèque", "à la poste", "à l'hôpital", "à la gare"]),
          ["relie"], 1, "B", sol="livre → bibliothèque · grave → hôpital · train → gare · nager → piscine · colis → poste · carte d'identité → maison communale")
    e2 = E("Les transports. J'écoute et je répète.", emogrid(TRANS, 4), ["ecoute", "repete"], 1, "A", script="Dire chaque transport : « Je viens à l'école à pied / en bus… ». Attention : à pied, à vélo, mais en bus, en voiture.", sol="Activité orale.")
    e3 = E("Sondage : « Tu viens à l'école comment ? » Je compte dans la classe.", table(["🚶 à pied", "🚌 en bus", "🚗 en voiture", "🚲 à vélo", "🚆 en train / tram"], [["", "", "", "", ""]], ["36mm"] * 5).replace("<td></td>", '<td style="height:14mm"></td>'), ["parle", "groupe", "ecris"], 1, "A", sol="Résultats de la classe. Phrase : La majorité vient… ")
    b.page(f'{e}{e2}{e3}', "Lexique")

    # ---------- Leçon 1 : aller à ----------
    l1 = lecon("Aller à · au · à la · à l' · aux", f'''<div class="grid2"><div class="card" style="background:#fff"><b>ALLER</b> ⚠️<p>je vais<br>tu vas<br>il / elle va<br>nous allons<br>vous allez<br>ils / elles vont</p></div>
<div class="card" style="background:#fff">{table(["", "à + …", "exemple"], [["masculin", "<b>au</b> (à + le)", "au parc, au cinéma"], ["féminin", "<b>à la</b>", "à la gare, à la poste"], ["voyelle", "<b>à l'</b>", "à l'école, à l'hôpital"], ["pluriel", "<b>aux</b> (à + les)", "aux toilettes"], ["ville", "<b>à</b>", "à Namur, à Liège"]], ["24mm", "28mm", "40mm"])}</div></div>
<p class="mt2"><b>Je vais à pied, à vélo · en bus, en voiture, en train.</b> — Tu vas où ? — Je vais <b>chez</b> Yonas / <b>chez</b> le médecin (une personne → chez).</p>''')
    e = E("Je conjugue aller.", '<p>1. Je ______ à l\'école. 2. Tu ______ au parc ? 3. Elle ______ à la gare. 4. Nous ______ à la piscine. 5. Vous ______ à Liège. 6. Ils ______ au cinéma.</p>', ["complete"], 1, "C",
          sol="vais · vas · va · allons · allez · vont")
    b.page(f'{l1}{e}', "Leçon 1")
    e = E("Je complète avec au, à la, à l', aux, à ou chez.", '<p>1. Je vais ___ poste. 2. Il va ___ supermarché. 3. Nous allons ___ hôpital. 4. Tu vas ___ toilettes ? 5. Elle habite ___ Charleroi. 6. Je vais ___ le dentiste. 7. On va ___ parc. 8. Vous allez ___ bibliothèque.</p>', ["complete"], 2, "C",
          sol="à la · au · à l' · aux · à · chez · au · à la")
    e2 = E("Je complète avec à ou en.", '<p>1. Je viens ___ pied. 2. Mon père va travailler ___ voiture. 3. Daria va ___ Bruxelles ___ train. 4. Bilal vient ___ vélo.</p>', ["complete"], 1, "C", sol="à · en · à, en · à")
    e3 = E("J'écoute : Fatou raconte sa semaine. Où va-t-elle ? Je relie le jour et le lieu.", relie(["lundi", "mardi", "mercredi", "samedi", "dimanche"], ["🕌 à la mosquée", "🏊 à la piscine", "📚 à la bibliothèque", "🛒 au supermarché", "⚽ au terrain de foot"]), ["ecoute", "relie"], 2, "A",
           script="Lundi, je vais à la bibliothèque. Mardi, je vais au terrain de foot avec mon frère. Mercredi après-midi, je vais à la piscine. Samedi, je vais au supermarché avec ma mère. Et dimanche, je vais à la mosquée avec ma famille.",
           sol="lundi → bibliothèque · mardi → foot · mercredi → piscine · samedi → supermarché · dimanche → mosquée")
    b.page(f'{e}{e2}{e3}', "S'entraîner")

    # ---------- Leçon 2 : prépositions de lieu ----------
    preps = [("à côté de", "🏠🏦"), ("en face de", "🏠 ↔️ 🏦"), ("entre", "🏦🏠🏪"), ("devant", "🚗 ⬅ 🏠"), ("derrière", "🏠 ➡ 🌳"), ("près de 👍", "🏠·🏫"), ("loin de 👎", "🏠 ········ 🏫"), ("au coin de la rue", "↱🏪")]
    l2 = lecon("Où c'est ? Les prépositions de lieu", '<div class="grid4">' + "".join(f'<div class="card c" style="background:#fff;padding:2mm"><div style="font-size:16pt">{v}</div><b class="sm">{p}</b></div>' for p, v in preps) + '</div>' +
               '<p class="mt2">La poste est <b>à côté de la</b> maison communale. · La banque est <b>en face du</b> parc ⚠️ (de + le = <b>du</b>) · <b>près de l\'</b>école · <b>loin des</b> magasins (de + les = <b>des</b>)</p><p><b>Il y a</b> une pharmacie <b>dans</b> ma rue. · J\'habite <b>rue</b> Verte, <b>au numéro</b> 12.</p>')
    e = E("Je regarde le plan du quartier (page suivante). Vrai ou faux ?", vf(["La poste est entre la maison communale et le parc.", "La bibliothèque est en face de la poste.", "La gare est à côté de l'hôpital.", "La maison de Yonas est entre la friterie et les pompiers.", "La piscine est à côté du parc."]), ["regarde", "coche"], 2, "B",
          sol="Vrai · Vrai · Faux (à côté de la banque) · Vrai · Vrai")
    b.page(f'{l2}{e}', "Leçon 2")
    b.page(f'<h2>🗺️ Le plan du quartier</h2><p class="sm muted">Chaque case a une lettre et un chiffre (A1, B2…). Le Nord est en haut.</p>{plan_quartier()}', "Le plan")
    e = E("Je complète avec à côté de (du), en face de (du), entre, près de.", '<p>1. La pharmacie est ___________ supermarché.</p><p>2. La poste est ___________ la maison communale ___ le parc.</p><p>3. L\'école est ___________ la gare.</p><p>4. Le supermarché est ___________ la maison communale (de l\'autre côté de la rue).</p>', ["regarde", "complete"], 2, "C",
          sol="1. à côté du — 2. entre… et — 3. près de / à côté de — 4. en face de")
    e2 = E("Je lis la case et j'écris le lieu.", '<div class="grid6">' + "".join(f'<div class="card c"><b>{k}</b><div class="line"></div></div>' for k in ["A1", "C1", "B3", "D3", "C4", "D2"]) + '</div>', ["regarde", "ecris"], 1, "B", sol="A1 gare · C1 église · B3 supermarché · D3 piscine · C4 pompiers · D2 parc")
    e3 = E("Défi ! J'écris 3 phrases pour décrire mon quartier.", lines(3), ["ecris"], 3, "C", sol="Ex. : J'habite rue… Il y a un parc près de ma maison. La boulangerie est en face de…")
    b.page(f'{e}{e2}{e3}', "S'entraîner")

    # ---------- Leçon 3 : impératif et directions ----------
    dirs = [("⬅️", "Tourne à gauche"), ("➡️", "Tourne à droite"), ("⬆️", "Va tout droit"), ("🚸", "Traverse la rue"), ("🚌", "Prends le bus"), ("🔁", "Continue"), ("↩️", "Retourne / fais demi-tour"), ("🛑", "Arrête-toi")]
    l3 = lecon("Expliquer un chemin : l'impératif", '<div class="grid4">' + "".join(f'<div class="card c" style="background:#fff;padding:2mm"><span class="emo s">{e}</span><b class="sm">{t}</b></div>' for e, t in dirs) + '</div>' +
               table(["", "tu (un ami)", "vous (poli, plusieurs)"], [["tourner", "Tourne !", "Tournez !"], ["aller", "Va !", "Allez !"], ["prendre", "Prends !", "Prenez !"], ["traverser", "Traverse !", "Traversez !"]], ["40mm", "70mm", "72mm"]) +
               '<p class="mt2">Pas de sujet : <s>tu tournes</s> → <b>Tourne</b> à droite ! · Les mots d\'ordre : <b>d\'abord</b>… <b>ensuite</b>… <b>puis</b>… <b>enfin</b>… · la <b>première</b> / la <b>deuxième</b> rue à gauche</p><p><b>Pour demander :</b> Pardon, je cherche… / Où est… ? / Pour aller à…, s\'il vous plaît ? / C\'est loin ?</p>')
    e = E("Je transforme à l'impératif (tu puis vous).", '<p>1. tu tournes à gauche → __________ / __________</p><p>2. tu vas tout droit → __________ / __________</p><p>3. tu prends le bus 7 → __________ / __________</p>', ["ecris"], 2, "C",
          sol="Tourne à gauche / Tournez à gauche · Va tout droit / Allez tout droit · Prends le bus 7 / Prenez le bus 7")
    b.page(f'{l3}{e}', "Leçon 3")
    e = E("J'écoute le chemin. Je suis avec le doigt sur le plan. J'arrive où ?", f'<p>Chemin 1 : {blank("l")} Chemin 2 : {blank("l")} Chemin 3 : {blank("l")}</p>', ["ecoute", "montre", "ecris"], 2, "A",
          script="Départ : l'école (A2). Chemin 1 : Sors de l'école, va tout droit dans la rue du Marché. Traverse la rue de l'Église. C'est à droite, en face de la maison communale. → supermarché. Chemin 2 : Prends la rue de l'Église vers le nord. Tourne à droite dans la rue de la Gare. Continue. C'est le bâtiment avec une croix, à gauche. → église. Chemin 3 : Va tout droit dans la rue du Marché jusqu'à la rue Verte. Le grand jardin est à gauche. → parc.",
          sol="1. le supermarché — 2. l'église — 3. le parc")
    e2 = E("J'explique le chemin de la gare (A1) à la piscine (D3). Je dessine la flèche sur le plan, puis j'écris.", lines(4), ["regarde", "ecris"], 3, "C",
           sol="Ex. : Sors de la gare. Va tout droit dans la rue de la Gare jusqu'à la rue Verte. Tourne à droite. Traverse la rue du Marché. La piscine est à gauche (après le parc).")
    e3 = E("Jeu de rôle : un élève est un touriste, l'autre explique le chemin avec le plan.", '<div class="card"><p>— Pardon, pour aller à…, s\'il vous plaît ? — Allez tout droit… tournez… — C\'est loin ? — Non, c\'est à 5 minutes à pied. — Merci !</p></div>', ["parle", "duo"], 2, "A", sol="Impératif avec vous (poli) pour un adulte inconnu.")
    b.page(f'{e}{e2}{e3}', "S'entraîner")

    # ---------- FLESco : lire un plan ----------
    l4 = lecon("Lire un plan (méthode)", '<p>1️⃣ Je trouve le <b>Nord</b> (la flèche N). 2️⃣ Je repère le <b>départ</b> et l\'<b>arrivée</b>. 3️⃣ J\'utilise les <b>cases</b> (A1, B2…) : la lettre = la colonne, le chiffre = la ligne. 4️⃣ Je suis les <b>rues</b> avec le doigt. 5️⃣ Je tourne le plan dans le sens de la marche si c\'est difficile.</p><p class="sm">À l\'école : plan de l\'école, carte de géographie, tableau à double entrée, bataille navale, graphique.</p>')
    e = E("Je repère les cases sur le plan du quartier.", f'<p>1. L\'école est dans la case {blank("s")} 2. La maison de Yonas : {blank("s")} 3. L\'hôpital : {blank("s")}</p><p>4. Quel lieu est au Nord de la poste ? {blank()} 5. Quel lieu est au Sud de la bibliothèque ? {blank()}</p>', ["regarde", "ecris"], 2, "B",
          sol="1. A2 — 2. B4 — 3. D1 — 4. l'église — 5. la caserne des pompiers")
    grid = '<table class="t" style="width:auto;margin:auto">' + '<tr><th></th>' + "".join(f'<th style="width:14mm;text-align:center">{c}</th>' for c in "ABCDE") + '</tr>' + "".join(f'<tr><th style="text-align:center">{r}</th>' + '<td style="height:12mm"></td>' * 5 + '</tr>' for r in range(1, 5)) + '</table>'
    e2 = E("Je dessine dans le tableau : 🌳 en B2, 🏠 en D1, 🏫 en A4, 🚌 en E3, ⭐ en C3.", grid, ["dessine"], 1, "C", sol="Vérifier la position des 5 dessins (lettre = colonne, chiffre = ligne).")
    e3 = E("Défi ! Bataille navale à deux : je cache 3 lieux dans la grille. Mon voisin devine : « B2 ? » — « Oui, c'est le parc ! »", '', ["joue", "duo"], 3, "D", sol="Jeu : vocabulaire des lieux + coordonnées.")
    b.page(f'<span class="tag-doc">🎒 FRANÇAIS DE L\'ÉCOLE</span>{l4}{e}{e2}{e3}', "Consignes & école")

    # ---------- Documents de la vie ----------
    arr = ["Gare", "Rue Haute", "Maison communale", "École Saint-Joseph", "Bibliothèque", "Piscine", "Hôpital"]
    hor = [["07:12", "07:42", "08:12", "12:42", "16:12"], ["07:15", "07:45", "08:15", "12:45", "16:15"], ["07:18", "07:48", "08:18", "12:48", "16:18"], ["07:22", "07:52", "08:22", "12:52", "16:22"], ["07:25", "07:55", "08:25", "12:55", "16:25"], ["07:29", "07:59", "08:29", "12:59", "16:29"], ["07:35", "08:05", "08:35", "13:05", "16:35"]]
    ht = '<div class="doc" style="transform:none;padding:3mm;background:#FFFDE7;border:2px solid #F9A825"><div class="flex" style="justify-content:space-between"><b style="font-size:16pt">🚌 LIGNE 7 · Gare → Hôpital</b><span class="xs muted">du lundi au vendredi · réseau fictif</span></div>' + \
         table(["Arrêt"] + ["départ"] * 5, [[f'<b>{a}</b>'] + h for a, h in zip(arr, hor)], ["52mm"] + ["26mm"] * 5) + '<p class="xs mt2">⚠️ Pas de bus le dimanche. Mercredi : dernier bus à 12:42. Ticket : 2,10 € · gratuit pour les moins de 12 ans · abonnement scolaire possible.</p></div>'
    e = E("Je lis l'horaire du bus. Je réponds.", f'<p>1. Le bus 7 va de la gare à… {blank()} 2. Combien d\'arrêts ? {blank("s")}</p><p>3. Je prends le bus de 07:42 à la gare. J\'arrive à l\'école à quelle heure ? {blank()}</p><p>4. Le trajet gare → hôpital dure combien de minutes ? {blank()} 5. Il y a un bus le dimanche ? {blank()}</p><p>6. Le ticket coûte combien ? {blank()}</p>',
          ["lis", "ecris"], 2, "B", sol="1. l'hôpital — 2. 7 arrêts — 3. 07:52 — 4. 23 minutes — 5. Non — 6. 2,10 €")
    e2 = E("Défi ! L'école commence à 08:20. Je suis à l'arrêt « Rue Haute ». Quel bus je prends ? Pourquoi ?", lines(1), ["ecris"], 3, "C", sol="Le bus de 07:45 (arrivée 07:52). Le bus de 08:15 arrive à 08:22 : trop tard !")
    b.page(f'<span class="tag-doc">📄 DOCUMENT DE LA VIE</span><h2>L\'horaire du bus</h2>{ht}<div class="mt4">{e}{e2}</div><div class="astuce">Pour lire l\'heure du bus : 07:42 = sept heures quarante-deux. Au chauffeur : « Bonjour, un ticket pour l\'hôpital, s\'il vous plaît. »</div>', "Document de la vie")
    sg = [("stop", "Stop ! On s'arrête."), ("interdit", "Sens interdit : on ne passe pas."), ("parking", "Parking : on gare la voiture."), ("ecole", "Attention, école ! Des enfants traversent."),
          ("pieton", "Passage pour piétons."), ("velo", "Piste cyclable : pour les vélos."), ("bus", "Arrêt de bus."), ("sortie", "Sortie.")]
    e = E("Les panneaux de la rue. J'écoute et je répète.", '<div class="grid4">' + "".join(f'<div class="card c">{sign(k)}<div class="xs" style="font-weight:600">{t}</div></div>' for k, t in sg) + '</div>', ["ecoute", "repete"], 1, "A",
          script="Lire chaque panneau. Promenade dans le quartier : photographier les panneaux autour de l'école.", sol="Activité orale.")
    e2 = E("Je relie le panneau et la consigne.", relie([sign(k) for k in ["interdit", "ecole", "velo", "stop"]], ["Je roule ici à vélo.", "Je m'arrête.", "Je ne passe pas.", "Je fais attention aux enfants."]), ["relie"], 1, "B",
           sol="sens interdit → je ne passe pas · école → attention aux enfants · vélo → je roule ici à vélo · stop → je m'arrête")
    e3 = E("La sécurité : je complète les règles du piéton avec traverse, regarde, attends.", '<p>1. Je ________ à gauche et à droite. 2. Je ________ sur le passage pour piétons. 3. Le feu est rouge 🔴 : j\'________.</p>', ["complete"], 2, "C", sol="regarde · traverse · attends")
    b.page(f'<span class="tag-doc">📄 DOCUMENT DE LA VIE</span><h2>Les panneaux</h2>{e}{e2}{e3}', "Document de la vie")
    e = E("Je lis le message et je dessine le chemin sur le plan du quartier.", '<div class="card">📱 <b>Yonas :</b> « Salut Bilal ! Samedi, viens chez moi à 14 h. Tu sors de l\'école. Prends la rue de l\'Église vers le Sud. Traverse la rue du Marché et l\'avenue des Tilleuls. Ma maison est à gauche, en face de la friterie. Numéro 8. Sonne 2 fois ! »</div>' +
          f'<p class="mt2">1. Bilal va où ? {blank()} À quelle heure ? {blank("s")}</p><p>2. Il traverse quelles rues ? {blank("xl")}</p><p>3. La maison est en face de… {blank()} Numéro : {blank("s")}</p>', ["lis", "ecris"], 2, "B",
          sol="1. chez Yonas, à 14 h — 2. la rue du Marché et l'avenue des Tilleuls — 3. la friterie ; 8 (case B4)")
    e2 = E("Je remplis la fiche « Mon adresse ».", table(["", ""], [["Nom et prénom", ""], ["Rue et numéro", ""], ["Code postal et ville", ""], ["Je viens à l'école", ""], ["Mon arrêt de bus", ""]], ["60mm", "122mm"]).replace("<td></td>", '<td style="height:9mm"></td>'), ["ecris"], 1, "C",
           sol="Informations personnelles (vérifier code postal à 4 chiffres en Belgique).")
    b.page(f'<span class="tag-doc">📄 DOCUMENT DE LA VIE</span><h2>Une invitation et une adresse</h2>{e}{e2}<div class="astuce">En Belgique, on écrit : <b>Rue Verte 12, 5000 Namur</b> (la rue, le numéro, puis le code postal et la ville).</div>', "Document de la vie")

    # ---------- Sons ----------
    e = E("[ø], [œ], [ɲ], [j]. J'écoute et je répète.", '<div class="grid4"><div class="card c"><div class="huge">[ø]</div><p>eu (fin du mot)<br>deux · bleu · peu · le feu</p></div><div class="card c"><div class="huge">[œ]</div><p>eu + consonne<br>heure · fleur · jeune · neuf</p></div><div class="card c"><div class="huge">[ɲ]</div><p>gn<br>montagne · Espagne · ligne · signe</p></div><div class="card c"><div class="huge">[j]</div><p>ill · y · i + voyelle<br>fille · feuille · crayon · rue de Liège</p></div></div>', ["ecoute", "repete"], 1, "A",
          script="Paires : deux / douze, peu / pou, ligne / line (comparer). Bouche arrondie pour eu.", sol="Activité orale.")
    e2 = E("J'écoute : j'entends eu, gn ou ill ?", checks(8, ["eu", "gn", "ill"]), ["ecoute", "coche"], 2, "A", script="1. la ligne — 2. le feu — 3. la fille — 4. bleu — 5. la montagne — 6. la feuille — 7. l'heure — 8. le signe",
           sol="1. gn — 2. eu — 3. ill — 4. eu — 5. gn — 6. ill — 7. eu — 8. gn")
    e3 = E("Je complète avec eu, gn ou ill.", '<p>le f___ rouge 🔴 · la li___e de bus · une f___le · la ___re (🕘) · une ba___oire · le pei___e</p>', ["complete"], 2, "C", sol="feu · ligne · fille · heure · baignoire · peigne")
    b.page(f'<h2>J\'écoute bien</h2>{e}{e2}{e3}', "Sons")
    e = E("🔁 Module 8 · La météo.", '<p>❄️ → ______________ · 🌬️ → ______________</p>', ["ecris"], 1, "C", sol="Il neige. · Il y a du vent.")
    e2 = E("🔁 Module 8 · J'accorde.", '<p>une veste (noir) ______ · des bottes (blanc) ______</p>', ["complete"], 2, "C", sol="noire · blanches")
    e3 = E("🔁 Module 7 · J'ai 5 €. Le ticket de bus coûte 2,10 €. On me rend : ______", '', ["ecris"], 2, "C", sol="2,90 €")
    b.page(f'<h2>🔁 Je révise les modules 7 et 8</h2>{e}{e2}{e3}', "Je révise")

    # ---------- Ateliers ----------
    e = E("Le robot humain : un élève a les yeux fermés (le robot). Son camarade le guide dans la classe jusqu'à un objet caché : « Va tout droit, 3 pas ! Tourne à gauche ! Stop ! »", '<div class="grid4">' + "".join(f'<div class="card c" style="border-style:dashed;height:20mm;display:flex;flex-direction:column;align-items:center;justify-content:center"><span class="emo s">{em}</span><b class="xs">{t}</b></div>' for em, t in dirs) + '</div><p class="sm muted mt2">Je découpe les cartes-flèches pour la version silencieuse.</p>',
          ["parle", "joue", "duo", "decoupe"], 1, "D", sol="Jeu : impératif (va, tourne, avance, stop).")
    e2 = E("Le loto des lieux : la prof dit une phrase, je pose un jeton sur le lieu.", '<div class="grid4">' + "".join(f'<div class="card c" style="padding:1mm"><span class="emo s">{em}</span><div class="xs">{n}</div></div>' for em, n in LIEUX[:16]) + '</div>', ["ecoute", "joue"], 1, "D",
           sol="Phrases : « Je veux nager » → piscine ; « J'achète un timbre » → poste…")
    b.page(f'{atl_head("D", "Atelier · Jouer avec les directions")}{e}{e2}', "Atelier")
    e = E("Je lis le texte de Mateo. Je réponds.", '<div class="card"><p>« J\'habite à Charleroi, rue de la Station, au numéro 25. C\'est un quartier animé. En face de mon immeuble, il y a une boulangerie. À côté, il y a une pharmacie et un petit parc. L\'école est loin : je prends le métro, puis je marche 10 minutes. Le samedi, je vais à la piscine à vélo. J\'aime mon quartier, mais il y a beaucoup de voitures ! »</p></div>' +
          f'<p>1. Mateo habite où ? {blank("xl")}</p><p>2. Qu\'est-ce qu\'il y a en face de son immeuble ? {blank()}</p><p>3. Comment va-t-il à l\'école ? {blank("xl")}</p><p>4. Qu\'est-ce qu\'il n\'aime pas ? {blank()}</p>', ["lis", "ecris"], 2, "B",
          sol="1. à Charleroi, rue de la Station 25 — 2. une boulangerie — 3. en métro, puis à pied (10 minutes) — 4. les voitures (il y en a beaucoup)")
    e2 = E("À mon tour : je présente mon quartier comme Mateo (5 phrases).", lines(5), ["ecris"], 2, "C", sol="Production : J'habite… En face… À côté… Je vais à l'école… J'aime / je n'aime pas…")
    b.page(f'{atl_head("C", "Atelier · Lire et écrire")}{e}{e2}', "Atelier")

    # ---------- ★ Alpha ----------
    letter_page(b, E, "eu", "[ø]", [("2️⃣", "deux"), ("🔥", "feu"), ("🌸", "fleur"), ("🔵", "bleu")], "eaueoeau", [("2️⃣", "deux", 1), ("🔥", "feu", 1), ("🚌", "bus", 0), ("🌸", "fleur", 1), ("🔵", "bleu", 1), ("🏠", "maison", 0), ("🕘", "heure", 1), ("🚲", "vélo", 0)], MC)
    letter_page(b, E, "gn", "[ɲ]", [("⛰️", "montagne"), ("🍄", "champignon"), ("🦢", "cygne"), ("🛁", "baignoire")], "gngnangu", [("⛰️", "montagne", 1), ("🍄", "champignon", 1), ("🚗", "voiture", 0), ("🦢", "cygne", 1), ("🛁", "baignoire", 1), ("📚", "livre", 0), ("🕷️", "araignée", 1), ("🏫", "école", 0)], MC)
    letter_page(b, E, "ill", "[j]", [("👧", "fille"), ("🍃", "feuille"), ("☀️", "soleil"), ("🐛", "chenille")], "ilillili", [("👧", "fille", 1), ("🍃", "feuille", 1), ("🚌", "bus", 0), ("☀️", "soleil", 1), ("🐛", "chenille", 1), ("🏥", "hôpital", 0), ("👂", "oreille", 1), ("🚉", "gare", 0)], MC)
    e = E("Je lis les mots de la ville.", '<div class="grid4">' + "".join(f'<div class="card c"><span class="emo s">{em}</span><div class="huge" style="font-size:16pt">{w}</div></div>' for em, w in [("🚌", "bus"), ("🏫", "é·co·le"), ("🚉", "ga·re"), ("🌳", "parc"), ("🚲", "vé·lo"), ("🔥", "feu"), ("🛣️", "rue"), ("🏠", "mai·son")]) + '</div>', ["lis"], 1, "P", alpha=True, sol="Lecture.")
    e2 = E("Je lis les phrases. Je montre la flèche.", '<div class="grid2">' + "".join(f'<div class="card"><p class="big">{t}</p></div>' for t in ["Va à gauche. ⬅️", "Va à droite. ➡️", "Va tout droit. ⬆️", "Le bus est bleu. 🚌"]) + '</div>', ["lis", "montre"], 2, "P", alpha=True, sol="Lecture + geste.")
    b.page(AL.format(t="Je lis") + e + e2, "★ Alpha", color=MC)
    e = E("Je relie le mot et l'image.", relie([f'<b class="big">{w}</b>' for w in ["gare", "feu", "fille", "bus", "parc"]], [f'<span class="emo s">{x}</span>' for x in ["🚌", "👧", "🌳", "🚉", "🔥"]]), ["lis", "relie"], 1, "B", alpha=True, sol="gare–🚉 · feu–🔥 · fille–👧 · bus–🚌 · parc–🌳")
    e2 = E("Je recopie mon adresse (avec l'aide de la prof).", guide_lines(2, 22), ["recopie", "ecris"], 1, "C", alpha=True, sol="Écriture de l'adresse personnelle.")
    e3 = E("Dictée.", guide_lines(2, 20), ["ecoute", "ecris"], 2, "P", alpha=True, script="Dicter : eu — gn — ill — deux — feu — fille", sol="eu gn ill deux feu fille")
    b.page(AL.format(t="J'écris") + e + e2 + e3, "★ Alpha", color=MC)

    # ---------- Tâche finale ----------
    e = E("Je dessine le plan simple de mon chemin de l'école à ma maison (ou à un lieu que j'aime). J'ajoute 3 lieux, le Nord et une légende. Puis j'écris les directions.", '<div class="card" style="height:85mm"></div>', ["dessine", "seul"], 2, "C", sol="Plan lisible : départ, arrivée, rues, 3 lieux, légende.")
    b.page(tache_head("Mon itinéraire illustré", "Je dessine mon chemin, j'écris les directions, puis je l'explique à un camarade qui doit le suivre sur mon plan.") + e, "Tâche finale", levels=False)
    e = E("J'écris les directions (5 phrases au moins) avec d'abord, ensuite, puis, enfin.", lines(6), ["ecris"], 2, "C", sol="Ex. : D'abord, je sors de l'école. Ensuite, je tourne à droite. Puis je prends le bus 7…")
    b.page(e + table(["Je vérifie :", "✅"], [[x, '<span class="chk"></span>'] for x in ["Mon plan a un départ, une arrivée et le Nord.", "Il y a 3 lieux et une légende.", "J'utilise l'impératif ou je, avec des mots d'ordre.", "J'utilise 2 prépositions (à côté de, en face de…).", "Mon camarade arrive au bon endroit !"]], ["160mm", "22mm"]), "Tâche finale", levels=False)
    e = E("Je révise.", '<p>1. Nous ______ (aller) ___ piscine. 2. Je vais ___ hôpital. 3. tu prends → (impératif) ______ 4. La poste est en face ___ parc. 5. Je viens ___ pied.</p>', ["ecris"], 2, "C",
          sol="allons, à la · à l' · Prends · du · à")
    e2 = E("Défi ! Je corrige les 4 erreurs.", '<div class="card big">Je vais à le parc en vélo. Tu tournes à gauche ! La banque est à côté de la le gare.</div>' + lines(1), ["barre", "ecris"], 3, "C",
           sol="au parc · à vélo · Tourne à gauche ! · à côté de la gare")
    b.page(f'<h2>🔁 Je révise tout le module</h2>{e}{e2}', "Je révise")

    # ---------- Test ----------
    Q = [("📮 C'est :", ["la banque", "la poste", "la gare", "l'église"]), ("Pour un livre, je vais :", ["à la piscine", "à la bibliothèque", "à la banque", "à l'hôpital"]),
         ("Je viens ____ pied.", ["en", "à", "au", "de"]), ("Il va à Liège ____ train.", ["à", "en", "au", "par le"]),
         ("Nous ____ au parc.", ["allons", "allez", "vont", "vais"]), ("Ils ____ à l'école.", ["va", "vont", "allons", "vas"]),
         ("Je vais ____ cinéma.", ["à le", "au", "à la", "aux"]), ("Tu vas ____ gare ?", ["au", "à la", "à l'", "aux"]),
         ("Elle va ____ école.", ["à le", "au", "à la", "à l'"]), ("Je vais ____ le médecin.", ["à", "au", "chez", "en"]),
         ("⬅️ :", ["Tourne à droite.", "Tourne à gauche.", "Va tout droit.", "Arrête-toi."]), ("Impératif de « tu prends » :", ["Prend !", "Prends !", "Tu prends !", "Prenez-tu !"]),
         ("Poli, à un adulte :", ["Tourne à gauche !", "Tournez à gauche, s'il vous plaît.", "Tu tournes !", "Gauche !"]), ("La banque est en face ____ parc.", ["de le", "du", "de la", "des"]),
         ("🏦🏠🏪 : la maison est ____ la banque et le magasin.", ["entre", "devant", "derrière", "loin de"]), ("Sur un plan, « B3 » = colonne ____, ligne ____", ["3 · B", "B · 3", "B · B", "3 · 3"]),
         ("Panneau rouge octogonal :", ["Parking", "Stop", "Arrêt de bus", "Sortie"]), ("Le bus part à 07:45 et arrive à 08:05. Le trajet dure :", ["10 minutes", "20 minutes", "45 minutes", "1 heure"]),
         ("J'entends [ɲ] comme dans « montagne » :", ["ligne", "fille", "feu", "gare"]), ("🔁 Il fait froid, mets ton ____ !", ["short", "manteau", "maillot", "sandales"])]
    ans = ["la poste", "à la bibliothèque", "à", "en", "allons", "vont", "au", "à la", "à l'", "chez", "Tourne à gauche.", "Prends !", "Tournez à gauche, s'il vous plaît.", "du", "entre", "B · 3", "Stop", "20 minutes", "ligne", "manteau"]
    key = key_from(Q, ans)
    test_pages(b, 9, "Ma ville, mon quartier", Q, f'<h3>B1. Je regarde le plan du quartier. J\'écris où est la pharmacie (2 prépositions). (… / 3)</h3>{lines(1, True)}<h3>B2. J\'explique le chemin de l\'école (A2) à la poste (C2). (… / 4)</h3>{lines(2, True)}<h3>B3. Je dis comment je viens à l\'école et combien de temps. (… / 3)</h3>{lines(1, True)}',
               [["demander un chemin poliment", "/ 3", ""], ["expliquer un chemin sur le plan", "/ 4", ""], ["présenter mon quartier (3 lieux)", "/ 3", ""]],
               f'<h3>1. J\'écoute et j\'entoure. (… / 4)</h3><div class="grid4">{"".join(f"<div class=\'card c big\' style=\'font-weight:700\'>{r}</div>" for r in ["eu gn ill", "gn ill eu", "ill eu gn", "eu ill gn"])}</div><h3>2. Je lis et je relie. (… / 4)</h3>{relie([f"<b class=big>{w}</b>" for w in ["bus", "feu", "fille", "gare"]], ["<span class=\'emo s\'>🔥</span>", "<span class=\'emo s\'>🚉</span>", "<span class=\'emo s\'>🚌</span>", "<span class=\'emo s\'>👧</span>"])}<h3>3. Dictée. (… / 4)</h3>{guide_lines(1, 22)}<h3>4. Je montre la direction (oral). (… / 4)</h3><div class="card">☐ à gauche ☐ à droite ☐ tout droit ☐ stop</div><h3>5. Je dis 4 lieux de la ville (images). (… / 4)</h3><div class="card">☐ 🏫 ☐ 🚉 ☐ 🏥 ☐ 📮</div>')
    closing(b, 9, ["Je sais nommer les lieux de la ville.", "Je sais dire comment je me déplace (à pied, en bus…).", "Je sais conjuguer aller.", "Je sais dire au, à la, à l', aux, chez.", "Je sais dire où c'est (à côté de, en face de…).",
                   "Je sais demander un chemin poliment.", "Je sais expliquer un chemin (tourne, va, prends).", "Je sais lire un plan avec des cases.", "Je sais lire un horaire de bus.", "Je comprends les panneaux.", "★ Je sais lire eu, gn, ill…"],
            LIEUX[:14] + [("🛣️", "la rue"), ("🏘️", "le quartier"), ("🚏", "l'arrêt"), ("⬅️", "à gauche"), ("➡️", "à droite"), ("⬆️", "tout droit"), ("🚸", "traverser"), ("🗺️", "le plan"), ("🧭", "le Nord"), ("🚦", "le feu"), ("📍", "l'adresse"), ("🚌", "le bus")])
    plan_de_travail(b, E, 9, ["Aller à · au · à la · aux", "Les prépositions de lieu", "Expliquer un chemin : l'impératif", "Lire un plan"], "☐ Mon itinéraire illustré<br>☐ Mon camarade suit mon chemin")
    if render:
        to_pdf(b.html(), '/home/claude/syllabus/out/V1_M9_eleve.pdf')

    # ---------- Livret enseignant ----------
    pg, exs = helpers(b, E)
    A = b.marks["★ Alpha"]
    days = [("1", "Collectif", f"Ouverture · BD ({pg('Découvrir')})", f"Alpha : eu (p. {A[0]})"), ("2", "Collectif", f"Lieux et transports ({pg('Lexique')})", f"Alpha : gn (p. {A[1]})"),
            ("3", "Rotation", f"📌 Leçon 1 aller à ({pg('Leçon 1')})", f"Alpha : ill (p. {A[2]})"), ("4", "Rotation", f"📌 Leçon 2 prépositions + plan ({pg('Leçon 2')}, {pg('Le plan')})", f"Alpha : lecture (p. {A[3]})"),
            ("5", "Collectif", f"📌 Leçon 3 directions ({pg('Leçon 3')})", f"Alpha : écriture, adresse (p. {A[4]})"), ("6", "Rotation", f"Lire un plan ({pg('Consignes & école')}) · sons", "Alpha : flèches (robot)"),
            ("7", "Sortie", f"Horaire, panneaux, adresse ({pg('Document de la vie')}) · promenade dans le quartier", "Alpha : photos des panneaux"), ("8", "Ateliers", f"Robot humain, loto, texte de Mateo ({pg('Atelier')})", "Alpha : loto des lieux"),
            ("9", "Seul + duo", f"Tâche finale ({pg('Tâche finale')})", "Alpha : plan dessiné + 3 flèches"), ("10", "Seul", f"Test ({pg('Test')})", f"Alpha : test ({pg('★ Alpha · Test')})")]
    rot = [["🎧 Écouter-Parler", "Jeu de rôle « touriste » avec le plan", "20 min", "—"], ["📖 Lire", "Message de Yonas · texte de Mateo · horaire", "20 min", "Oui"], ["✏️ Écrire", "Aller à / prépositions · mon quartier", "20 min", "● oui"],
           ["🧩 Jouer", "Robot humain · bataille navale · loto", "20 min", "Entre joueurs"], ["👩‍🏫 Table d'appui", "Alpha : eu gn ill · autres : impératif, plan", "20 min", "—"]]
    ev1 = '''<h3>Partie B (10 points)</h3><p class="sm"><b>B1</b> : <span class="sol">La pharmacie est à côté du supermarché, près de l'école / en face de… (case A3).</span> · <b>B2</b> : <span class="sol">Sors de l'école. Va tout droit dans la rue du Marché. Traverse la rue de l'Église. Continue : la poste est à gauche, entre la maison communale et le parc.</span> (logique 2, impératif 2) · <b>B3</b> : moyen de transport + à/en + durée.</p>
<h3>Test ★ Alpha</h3><p class="sm"><b>Ex. 1, dire :</b> <span class="sol">gn · eu · ill · gn</span> · <b>Ex. 2 :</b> <span class="sol">bus–🚌, feu–🔥, fille–👧, gare–🚉</span> · <b>Ex. 3, dicter :</b> <span class="sol">eu, gn, feu, fille</span>.</p>'''
    ev2 = f'''<h2>Grille · tâche finale « Mon itinéraire illustré »</h2>{table(["Critère", "Très bien", "Bien", "À retravailler", "Points"], [["<b>Plan</b> : départ, arrivée, Nord, 3 lieux, légende", "Complet", "Partiel", "Incomplet", "/ 5"], ["<b>Directions</b> justes et dans l'ordre", "Oui", "1-2 erreurs", "Non", "/ 5"], ["<b>Langue</b> : impératif, prépositions, au/à la", "Correct", "Quelques erreurs", "Beaucoup", "/ 5"], ["<b>Oral</b> : le camarade arrive au bon endroit", "Oui", "Avec aide", "Non", "/ 5"]], ["64mm", "32mm", "32mm", "32mm", "22mm"])}
<h2 class="mt4">Différencier et remédier</h2>{table(["Difficulté", "Remédiation"], [["Gauche / droite", "Bracelet ou gommette sur la main droite ; jeu « Jacques a dit » ; tourner le plan dans le sens de la marche."], ["au / à la / à l' / aux", "Tableau des contractions affiché ; cartes-lieux avec l'article en couleur."], ["Impératif", "Partir de « tu tournes » et barrer « tu » ; comparer avec les consignes du cahier (lis, écris, entoure)."], ["Lire un plan", "Plan de la classe, puis de l'école, puis du quartier ; bataille navale."], ["Élève rapide", "Itinéraire avec deux transports (bus + à pied) sur un vrai plan TEC / Google Maps projeté."]], ["50mm", "132mm"])}
<div class="astuce mt4"><b>Sécurité et autonomie :</b> c'est le bon moment pour vérifier que chaque élève connaît son adresse, son arrêt de bus et le numéro d'urgence 112 (module 5). Ne jamais demander de montrer l'adresse à la classe : la fiche « Mon adresse » reste personnelle.</div>'''
    T = teacher_book(b, E, "V1 · M9", "", MC, 9, "Ma ville, mon quartier",
                     "<li><b>Communication :</b> demander et indiquer un chemin, se déplacer, décrire son quartier.</li><li><b>Lexique :</b> lieux de la ville, transports, directions, panneaux.</li><li><b>Grammaire :</b> aller ; au / à la / à l' / aux / chez ; à pied, en bus ; prépositions de lieu ; impératif (tu, vous).</li><li><b>Phonétique :</b> [ø] / [œ], [ɲ], [j].</li><li><b>FLSco :</b> lire un plan, un tableau à double entrée.</li><li><b>Documents :</b> horaire de bus, panneaux, invitation, adresse.</li><li><b>★ Alpha :</b> eu, gn, ill.</li>",
                     '<p class="sm"><b style="color:#E4572E">Indispensable</b> : lieux utiles, à gauche / à droite / tout droit, son adresse.</p><p class="sm"><b style="color:#d9a400">Important</b> : au / à la, prépositions, horaire de bus.</p><p class="sm"><b style="color:#2BA88F">Enrichissement</b> : impératif avec vous, coordonnées, itinéraire à deux transports.</p>',
                     "Plan du quartier de l'école (commune, TEC) · horaires réels de bus · appareil photo / tablette · jetons · ciseaux.", "<b>Sortie conseillée :</b> promenade autour de l'école pour photographier les lieux et les panneaux, puis créer le plan de la classe.",
                     days, "« Je vais à… » en chaîne · le robot humain (2 min) · un panneau du jour.", rot, key, (ev1, ev2), start=tstart)
    if render:
        to_pdf(T.html(), '/home/claude/syllabus/out/V1_M9_prof.pdf')
    return b, T


if __name__ == "__main__":
    b, T = build_m9()
    print(b.n, T.n)
