"""Volume 2 · Module 2 « Chez moi » (A2)."""
import sys
sys.path.insert(0, '/home/claude/syllabus')
from lib.base import *
from lib.art import *
from lib.module import *
from lib.v2 import CP, CPCOL
from lib.render import to_pdf

MC = "#C77D2E"
PIECES = [("🛋️", "le salon"), ("🍳", "la cuisine"), ("🛏️", "la chambre"), ("🛁", "la salle de bains"), ("🚽", "les toilettes (le WC)"), ("🚪", "le couloir / le hall"),
          ("🍷", "la cave"), ("📦", "le grenier"), ("🌳", "le jardin"), ("🪴", "la terrasse / le balcon"), ("🚗", "le garage"), ("🧺", "la buanderie")]
MEUBLES = [("🛏️", "le lit"), ("🚪", "l'armoire"), ("🛋️", "le canapé"), ("🪑", "la chaise"), ("🍽️", "la table"), ("📚", "l'étagère"), ("💡", "la lampe"), ("🧊", "le frigo"),
           ("🔥", "la cuisinière"), ("🫧", "la machine à laver"), ("🚿", "la douche"), ("🛁", "la baignoire"), ("🚰", "l'évier / le lavabo"), ("🌡️", "le radiateur"), ("🪟", "la fenêtre"), ("🖥️", "le bureau")]


def voisine(size=72, mood="neutre"):
    return face(skin="clair", hair="#BDBDBD", style="court", glasses=True, size=size, shirt="#8E6C8A", gray=True)


def chambre_scene(labels=True):
    items = [("🛏️", 36, 114, "le lit"), ("🐈", 52, 139, "le chat"), ("🪟", 100, 40, "la fenêtre"), ("🖥️", 162, 108, "le bureau"), ("🪑", 128, 134, "la chaise"), ("💡", 162, 80, "la lampe"),
             ("📚", 172, 60, "l'étagère"), ("🎒", 184, 136, "le sac"), ("🧸", 18, 92, "l'ours"), ("🪴", 82, 134, "la plante"), ("🖼️", 40, 52, "le cadre")]
    t = "".join(f'<text x="{x}" y="{y}" font-size="22" text-anchor="middle">{e}</text>' + (f'<text x="{x}" y="{y + 9}" font-size="5.5" text-anchor="middle" font-family="Poppins" font-weight="700" fill="#5a4a3a">{n}</text>' if labels else "") for e, x, y, n in items)
    return (f'<svg viewBox="0 0 200 150" width="100%" style="max-height:92mm"><rect x="2" y="2" width="196" height="146" rx="4" fill="#FFF8EE" stroke="#C77D2E" stroke-width="2"/>'
            f'<rect x="2" y="100" width="196" height="48" fill="#F3E3CC"/>{t}</svg>')


def plan_echelle():
    """Plan à l'échelle réelle 1 cm = 1 m (1 unité = 1 mm à l'impression)."""
    rooms = [(0, 0, 50, 40, "salon"), (50, 0, 30, 40, "cuisine"), (80, 0, 40, 40, "chambre 1"), (0, 40, 40, 40, "chambre 2"), (40, 40, 30, 40, "couloir"), (70, 40, 30, 40, "SdB"), (100, 40, 20, 40, "réserve")]
    r = "".join(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#FFF8EE" stroke="#1F2A44" stroke-width=".8"/><text x="{x + w / 2}" y="{y + h / 2 + 1.5}" font-size="4.2" text-anchor="middle" font-family="Poppins" font-weight="700">{n}</text>' for x, y, w, h, n in rooms)
    grid = "".join(f'<line x1="{i}" y1="0" x2="{i}" y2="80" stroke="#E7D7C2" stroke-width=".2"/>' for i in range(0, 121, 10)) + "".join(f'<line x1="0" y1="{j}" x2="120" y2="{j}" stroke="#E7D7C2" stroke-width=".2"/>' for j in range(0, 81, 10))
    scale = '<g transform="translate(0,88)"><rect x="0" y="0" width="10" height="2.4" fill="#1F2A44"/><rect x="10" y="0" width="10" height="2.4" fill="#fff" stroke="#1F2A44" stroke-width=".4"/><text x="0" y="7" font-size="3.6" font-family="Poppins">0</text><text x="9" y="7" font-size="3.6" font-family="Poppins">1 m</text><text x="19" y="7" font-size="3.6" font-family="Poppins">2 m</text><text x="30" y="2.6" font-size="3.8" font-family="Poppins" font-weight="700">Échelle : 1 cm = 1 m</text></g>'
    door = '<rect x="0" y="78" width="0" height="0"/><line x1="52" y1="80" x2="58" y2="80" stroke="#fff" stroke-width="1.6"/><text x="55" y="84.5" font-size="3.4" text-anchor="middle" font-family="Poppins">entrée</text>'
    return f'<svg viewBox="-2 -2 124 98" style="width:124mm;height:98mm">{grid}{r}{door}{scale}</svg>'


def build_v2m2(start=1, tstart=1, render=True):
    b = Book("V2 · M2", "Volume 2 · Je me débrouille · Module 2 · Chez moi", MC, start=start)
    E = Ex(b)
    vis = '<div class="c" style="font-size:38pt;line-height:1.3">🏠🏢🛋️🛏️🍳<br>🔑📦🧺🔇🤝</div>'
    opening(b, MC, 2, "Chez moi", vis, [("🏠", "décrire un logement : les pièces, les meubles, les équipements"), ("📍", "dire où sont les objets avec précision"), ("📌", "remplacer un lieu par y ou en"),
            ("🤝", "régler poliment un problème avec un voisin"), ("📰", "lire une annonce immobilière et un règlement d'immeuble"), ("📐", "lire un plan à l'échelle et calculer une surface")],
            ["Tu habites dans une maison ou un appartement ?", "Quelle est ta pièce préférée ? Pourquoi ?", "Tu as déjà eu un problème avec un voisin ?"],
            ["la pièce", "le meuble", "le loyer", "les charges", "le propriétaire", "le locataire", "le voisin", "y", "en", "l'échelle"], "#F8EBDD")

    # ---------- Découvrir ----------
    bd = '<div class="grid2" style="gap:3mm">' + "".join([
        bd_case(1, lr("yonas", ["Ça y est ! On a déménagé ! Notre nouvel appartement est au troisième étage."], "mateo", ["Super ! Il y a combien de chambres ?"], "rire", "sourire", '<div class="c" style="font-size:20pt">🏢📦🔑</div>')),
        bd_case(2, lr("yonas", ["Trois ! Enfin, j'ai ma chambre à moi. Avant, je dormais avec mes deux frères."], "mateo", ["Tu y as mis ton poster du Barça ?"], "rire", "rire")),
        bd_case(3, lr("yonas", ["Oui ! Mais hier soir, il y a eu un problème… Quelqu'un a frappé à la porte à 23 h."], extra='<div class="c" style="font-size:22pt">🚪✊⏰</div>', ma="pense")),
        bd_case(4, f'<div class="flex top" style="margin-top:5mm">{voisine()}<div>{bub("Bonsoir. Excusez-moi de vous déranger, mais la musique est très forte. J&#39;habite juste en dessous et je travaille tôt demain.")}</div></div>'),
        bd_case(5, lr("yonas", ["Oh, je suis vraiment désolé, Madame ! Je ne savais pas qu'on entendait tout. Je baisse tout de suite."], ma="triste", extra=f'<div class="flex top" style="justify-content:flex-end">{bub("Merci, c&#39;est gentil. Bienvenue dans l&#39;immeuble !")}{voisine(60)}</div>')),
        bd_case(6, lr("mateo", ["Et maintenant ?"], "yonas", ["Maintenant, j'écoute ma musique avec un casque ! Et Mme Dubois m'a invité à goûter ses gaufres."], "pense", "rire", '<div class="c" style="font-size:20pt">🎧🧇😄</div>')),
    ]) + '</div>'
    e = E("J'écoute et je lis la BD : un nouvel appartement.", bd, ["ecoute", "lis"], 1, "A",
          script="Lire deux fois. Faire jouer la scène voisine / Yonas. Relever les formules polies : « Excusez-moi de vous déranger », « Je suis vraiment désolé », « Je baisse tout de suite ».", sol="Activité orale.")
    b.page(f'<h2>Découvrir · Un nouvel appartement</h2>{e}', "Découvrir")
    e = E("Je réponds par une phrase complète.", f'<p>1. À quel étage est le nouvel appartement ? {blank("xl")}</p><p>2. Qu\'est-ce qui change pour Yonas ? {blank("xl")}</p><p>3. Pourquoi la voisine frappe à la porte ? Donne 2 raisons. {blank("xl")}</p><p>4. Comment Yonas réagit ? {blank("xl")}</p><p>5. Comment l\'histoire se termine ? {blank("xl")}</p>',
          ["lis", "ecris"], 1, "B", sol="1. au troisième étage — 2. Il a sa chambre à lui (avant, il dormait avec ses frères). — 3. La musique est trop forte, elle habite en dessous, elle travaille tôt. — 4. Il s'excuse et baisse la musique tout de suite. — 5. Il écoute la musique avec un casque ; la voisine l'invite à goûter ses gaufres.")
    e2 = E("Je relève les formules polies de la BD.", table(["Pour…", "La voisine / Yonas dit…"], [["déranger poliment", ""], ["expliquer le problème", ""], ["s'excuser", ""], ["proposer une solution", ""], ["remercier, accueillir", ""]], ["60mm", "122mm"]).replace("<td></td>", '<td style="height:8mm"></td>'), ["lis", "ecris"], 2, "B",
           sol="Excusez-moi de vous déranger · la musique est très forte, je travaille tôt · Je suis vraiment désolé, je ne savais pas · Je baisse tout de suite · Merci, c'est gentil. Bienvenue !")
    b.page(f'{e}{e2}', "Découvrir")
    txt = '''<div class="card" style="background:#FFFBF5"><p style="line-height:1.65"><b>Ma nouvelle chambre — par Daria</b><br>
Nous habitons maintenant dans une petite maison avec un jardin, à Jambes. Au rez-de-chaussée, il y a le salon, la cuisine et les toilettes. À l'étage, il y a trois chambres et la salle de bains. Ma chambre se trouve au fond du couloir, à droite. Elle n'est pas très grande (environ 9 m²), mais elle est claire : la fenêtre donne sur le jardin.<br>
Contre le mur de gauche, il y a mon lit. Au-dessus du lit, j'ai accroché des photos de mes amies de Kharkiv. En face de la fenêtre, il y a un petit bureau et une chaise bleue. Mes livres sont sur une étagère, entre le bureau et l'armoire. Sous le lit, je range mes boîtes de dessins.<br>
Le seul problème : le chauffage ne marche pas bien. Ma mère a téléphoné au propriétaire. Il dit qu'il va envoyer un chauffagiste la semaine prochaine. En attendant, je porte deux pulls ! 🥶</p></div>'''
    e = E("Je lis le texte de Daria. Je réponds.", txt + f'<p>1. Quel type de logement ? Où ? {blank("xl")}</p><p>2. Quelles pièces au rez-de-chaussée ? {blank("xl")}</p><p>3. Où est la chambre de Daria ? {blank("xl")}</p><p>4. Qu\'est-ce qu\'il y a au-dessus du lit ? Sous le lit ? {blank("xl")}</p><p>5. Quel est le problème ? Quelle est la solution ? {blank("xl")}</p>',
          ["lis", "ecris"], 2, "B", sol="1. une petite maison avec jardin, à Jambes — 2. le salon, la cuisine, les toilettes — 3. au fond du couloir, à droite (à l'étage) — 4. des photos de ses amies ; ses boîtes de dessins — 5. le chauffage ne marche pas bien ; le propriétaire va envoyer un chauffagiste")
    b.page(f'<h2>Découvrir · La chambre de Daria</h2>{e}', "Découvrir")

    # ---------- Lexique ----------
    e = E("Les pièces du logement. J'écoute et je répète.", emogrid(PIECES, 6), ["ecoute", "repete"], 1, "A", script="Dire chaque pièce. Demander : « Qu'est-ce qu'on fait dans la cuisine ? Dans la buanderie ? » Faire remarquer : au rez-de-chaussée, au premier étage, au sous-sol (la cave).", sol="Activité orale.")
    types = [("🏠", "une maison (2, 3 ou 4 façades)"), ("🏢", "un appartement (un « appart »)"), ("🛏️", "un studio (une seule pièce)"), ("🎓", "un kot (chambre d'étudiant)"), ("🏘️", "un logement social"), ("🏚️", "une maison mitoyenne")]
    e2 = E("Les types de logement. Je lis et je relie à la définition.", relie([t for _, t in types[:5]], ["une petite chambre louée par un étudiant", "un logement pas cher, géré par une société publique", "un logement dans un immeuble", "un bâtiment pour une famille, avec souvent un jardin", "une pièce pour vivre, dormir et cuisiner"]), ["lis", "relie"], 2, "B",
           sol="maison → bâtiment pour une famille · appartement → dans un immeuble · studio → une pièce pour tout · kot → chambre d'étudiant · logement social → pas cher, société publique")
    b.page(f'<h2>Le logement</h2>{e}{e2}<div class="astuce">🇧🇪 Une maison <b>4 façades</b> n\'a pas de voisin collé ; une maison <b>2 façades</b> (mitoyenne) a des voisins des deux côtés. Un <b>kot</b> est une chambre d\'étudiant (mot belge).</div>', "Lexique")
    e = E("Les meubles et les équipements. J'écoute et je répète.", emogrid(MEUBLES, 8 if False else 4), ["ecoute", "repete"], 1, "A", script="Dire chaque mot. Jeu : « Dans quelle pièce ? » — le frigo → dans la cuisine.", sol="Activité orale.")
    e2 = E("Je classe les meubles et équipements dans les pièces.", table(["🍳 Cuisine", "🛁 Salle de bains", "🛏️ Chambre", "🛋️ Salon"], [["", "", "", ""]], ["45mm"] * 4).replace("<td></td>", '<td style="height:26mm"></td>') + '<p class="sm mt2">le frigo · la douche · le lit · le canapé · l\'évier · la baignoire · l\'armoire · la télé · la cuisinière · le lavabo · le bureau · la table basse</p>', ["ecris"], 1, "C",
           sol="Cuisine : frigo, évier, cuisinière · SdB : douche, baignoire, lavabo · Chambre : lit, armoire, bureau · Salon : canapé, télé, table basse")
    b.page(f'{e}{e2}', "Lexique")

    # ---------- Leçon 1 : décrire un logement ----------
    l1 = lecon("Décrire un logement", '''<div class="grid2"><div class="card" style="background:#fff"><b>Situer les pièces</b><p class="sm">au sous-sol · au rez-de-chaussée · au premier / deuxième étage · à l'étage · au fond du couloir · à gauche / à droite de l'entrée</p><p class="sm"><b>Il y a</b> trois chambres. · La cuisine <b>se trouve</b> au rez-de-chaussée. · La fenêtre <b>donne sur</b> le jardin.</p></div>
<div class="card" style="background:#fff"><b>Les adjectifs du logement</b><p class="sm">grand ≠ petit · clair ≠ sombre · calme ≠ bruyant · moderne ≠ ancien · propre ≠ sale · chaud ≠ froid, humide · meublé (avec meubles) · équipé (cuisine équipée) · spacieux · confortable</p></div></div>
<div class="attention" style="margin-top:2mm">La plupart des adjectifs se placent <b>après</b> le nom : une pièce <b>claire</b>. Mais quelques adjectifs courts se placent <b>avant</b> : <b>grand, petit, beau, joli, nouveau, vieux, bon</b> → une <b>petite</b> maison, un <b>grand</b> salon.<br>⚠️ Devant une voyelle : un <b>bel</b> appartement · un <b>nouvel</b> immeuble · un <b>vieil</b> escalier</div>''')
    e = E("Je place l'adjectif avant ou après le nom et je l'accorde.", '<p>1. une maison (petit) → ______________ 2. une chambre (clair) → ______________ 3. un appartement (beau) → ______________ 4. une cuisine (moderne) → ______________ 5. un immeuble (nouveau) → ______________ 6. des pièces (grand) → ______________</p>', ["ecris"], 2, "C",
          sol="une petite maison · une chambre claire · un bel appartement · une cuisine moderne · un nouvel immeuble · de grandes pièces / des grandes pièces")
    b.page(f'{l1}{e}', "Leçon 1")
    e = E("J'écoute la description. Je coche les bonnes informations.", table(["", "Oui", "Non"], [[x, '<span class="chk"></span>', '<span class="chk"></span>'] for x in ["C'est un appartement.", "Il est au rez-de-chaussée.", "Il y a deux chambres.", "La cuisine est équipée.", "Il y a un balcon.", "Le quartier est bruyant."]], ["130mm", "26mm", "26mm"]), ["ecoute", "coche"], 2, "A",
          script="« J'habite dans un appartement au deuxième étage. Il y a un salon assez grand, une cuisine équipée et deux chambres. La salle de bains est petite, mais moderne. Il n'y a pas de balcon, c'est dommage. Le quartier est très calme, près d'un parc. »",
          sol="Oui · Non (2e étage) · Oui · Oui · Non · Non (calme)")
    e2 = E("Je décris mon logement (ou un logement imaginaire) : 6 phrases avec il y a, se trouver, donner sur et 3 adjectifs.", lines(6), ["ecris"], 2, "C", sol="Production libre ; vérifier la place des adjectifs.")
    e3 = E("Défi ! Je dessine le plan de mon logement idéal et je le présente à mon voisin.", '<div class="card" style="height:38mm"></div>', ["dessine", "parle", "duo"], 3, "C", sol="Présentation orale avec les prépositions.")
    b.page(f'{e}{e2}{e3}', "S'entraîner")

    # ---------- Leçon 2 : prépositions ----------
    preps = [("sur", "📕 sur la table"), ("sous", "🐈 sous le lit"), ("dans", "👕 dans l'armoire"), ("devant", "🪑 devant le bureau"), ("derrière", "📦 derrière la porte"), ("entre", "📚 entre le bureau et l'armoire"),
             ("à côté de", "💡 à côté du lit"), ("en face de", "🛋️ en face de la télé"), ("au-dessus de", "🖼️ au-dessus du canapé"), ("au-dessous de", "🧦 au-dessous de l'étagère"), ("contre", "🛏️ contre le mur"), ("au milieu de", "🧶 au milieu de la pièce"),
             ("au fond de", "🚪 au fond du couloir"), ("à gauche de", "⬅️ à gauche de la fenêtre"), ("autour de", "🪑 autour de la table"), ("par terre", "🎒 par terre")]
    l2 = lecon("Dire où sont les objets", '<div class="grid4">' + "".join(f'<div class="card" style="background:#fff;padding:1.5mm"><b class="sm">{p}</b><div class="xs">{x}</div></div>' for p, x in preps) + '</div>' +
               '<p class="mt2">⚠️ <b>de + le = du</b> (à côté <b>du</b> lit) · <b>de + les = des</b> (près <b>des</b> fenêtres) · de la, de l\' ne changent pas.</p>')
    e = E("Je regarde la chambre. J'écris où sont les objets.", chambre_scene() + '<p>1. Le chat est ______________ lit. 2. La lampe est ______________ bureau. 3. La chaise est ______________ bureau. 4. Le cadre est ______________ lit. 5. Le sac est ______________ (sol).</p>', ["regarde", "ecris"], 2, "C",
          sol="sous le / au pied du · sur le / au-dessus du · devant le · au-dessus du · par terre")
    b.page(f'{l2}{e}', "Leçon 2")
    e = E("Je complète avec du, de la, de l', des.", '<p>1. La lampe est à côté ___ lit. 2. Le tapis est au milieu ___ chambre. 3. Le vélo est près ___ escalier. 4. La table est en face ___ fenêtres. 5. Le frigo est à gauche ___ évier. 6. La cave est au-dessous ___ cuisine.</p>', ["complete"], 1, "C",
          sol="du · de la · de l' · des · de l' · de la")
    e2 = E("Dictée de dessin : j'écoute et je dessine la pièce.", '<div class="card" style="height:62mm"></div>', ["ecoute", "dessine"], 2, "A",
           script="Dessine un salon. Au milieu, il y a une table ronde avec quatre chaises autour. Contre le mur de droite, il y a un canapé. Au-dessus du canapé, il y a un grand cadre. En face du canapé, il y a une télé. Un chat dort sous la table. À gauche de la fenêtre, il y a une plante.",
           sol="Vérifier : table au milieu + 4 chaises, canapé à droite, cadre au-dessus, télé en face, chat sous la table, plante à gauche de la fenêtre.")
    e3 = E("Jeu « Où est mon stylo ? » : je cache un objet dans la classe. Mon voisin pose des questions (« Il est sous… ? »). Je réponds par oui / non.", '', ["parle", "duo", "joue"], 1, "A", sol="Questions avec prépositions.")
    b.page(f'{e}{e2}{e3}', "S'entraîner")

    # ---------- Leçon 3 : y ----------
    l3 = lecon("Le pronom y (= à / dans / chez + un lieu)", table(["Question", "Réponse avec y"], [["Tu vas <b>à la cave</b> ?", "Oui, j'<b>y</b> vais."], ["Vous habitez <b>dans cet immeuble</b> ?", "Oui, nous <b>y</b> habitons depuis 2 ans."], ["Il est <b>chez sa tante</b> ?", "Non, il n'<b>y</b> est pas."], ["Tu es allé(e) <b>au grenier</b> ?", "Oui, j'<b>y</b> suis allé(e) hier."], ["Tu vas aller <b>à la commune</b> ?", "Oui, je vais <b>y</b> aller demain."]], ["90mm", "92mm"]) +
               '<div class="attention" style="margin-top:2mm"><b>y</b> remplace un lieu déjà dit. Il se place <b>devant le verbe conjugué</b> (j\'<b>y</b> vais, je n\'<b>y</b> vais pas, j\'<b>y</b> suis allé) — sauf au futur proche : je vais <b>y</b> aller (devant l\'infinitif). À l\'impératif : <b>Vas-y !</b> <b>Allons-y !</b></div>')
    e = E("Je réponds avec y.", '<p>1. Tu vas au supermarché ? — Oui, ______________________</p><p>2. Ta sœur habite à Liège ? — Non, ______________________</p><p>3. Vous êtes allés à la mer ? — Oui, ______________________</p><p>4. Tu vas retourner dans ton ancien quartier ? — Oui, ______________________</p>', ["ecris"], 2, "C",
          sol="j'y vais · elle n'y habite pas · nous y sommes allés · je vais y retourner")
    b.page(f'{l3}{e}', "Leçon 3")

    # ---------- Leçon 4 : en ----------
    l4 = lecon("Le pronom en (= de + un lieu)", table(["Question", "Réponse avec en"], [["Tu viens <b>de la cave</b> ?", "Oui, j'<b>en</b> viens."], ["Il sort <b>du magasin</b> ?", "Oui, il <b>en</b> sort."], ["Vous revenez <b>de Bruxelles</b> ?", "Non, nous n'<b>en</b> revenons pas."], ["Elle est partie <b>de chez elle</b> ?", "Oui, elle <b>en</b> est partie à 8 h."]], ["90mm", "92mm"]) +
               '<div class="grid2 mt2"><div class="card" style="background:#fff"><b>y</b> ➡️ je vais <b>vers</b> le lieu, je suis <b>dans</b> le lieu<p class="sm">aller à, être à / dans / chez, habiter à</p></div><div class="card" style="background:#fff"><b>en</b> ⬅️ je <b>quitte</b> le lieu<p class="sm">venir de, sortir de, revenir de, partir de</p></div></div><p class="sm muted">Au module 9, tu verras <b>en</b> pour les quantités (j\'en veux deux).</p>')
    e = E("y ou en ? Je complète.", '<p>1. Tu vas au parc ? — Oui, j\'___ vais. 2. Tu reviens de l\'école ? — Oui, j\'___ reviens. 3. Elle habite dans ce quartier ? — Oui, elle ___ habite. 4. Ils sortent du cinéma ? — Oui, ils ___ sortent. 5. Vous allez chez le médecin ? — Oui, nous ___ allons. 6. Tu viens de la cuisine ? — Non, je n\'___ viens pas.</p>', ["complete"], 2, "C",
          sol="y · en · y · en · y · en")
    b.page(f'{l4}{e}', "Leçon 4")
    e = E("Je remplace les mots soulignés par y ou en.", '<p>1. Je vais <u>à la buanderie</u>. → ______________________</p><p>2. Nous revenons <u>du marché</u>. → ______________________</p><p>3. Il n\'est pas <u>dans sa chambre</u>. → ______________________</p><p>4. Je suis sorti <u>de la maison</u> à 7 h. → ______________________</p>', ["ecris"], 2, "C",
          sol="J'y vais. · Nous en revenons. · Il n'y est pas. · J'en suis sorti à 7 h.")
    e2 = E("J'écoute : j'entends y ou en ? Je coche.", checks(8, ["y", "en"]), ["ecoute", "coche"], 2, "A",
           script="1. J'y vais. — 2. J'en viens. — 3. On y va ! — 4. Il en sort. — 5. Nous y habitons. — 6. Elle en revient. — 7. Vas-y ! — 8. Ils en partent.", sol="1. y — 2. en — 3. y — 4. en — 5. y — 6. en — 7. y — 8. en")
    e3 = E("Défi ! Mini-dialogue : je pose 4 questions à mon voisin sur les lieux de son quotidien. Il répond avec y ou en.", lines(3), ["parle", "ecris", "duo"], 3, "A", sol="Ex. : — Tu vas souvent à la bibliothèque ? — Oui, j'y vais le mercredi.")
    b.page(f'{e}{e2}{e3}', "S'entraîner")

    # ---------- Leçon 5 : régler un problème avec un voisin ----------
    l5 = lecon("Régler un problème avec un voisin", table(["Étape", "Je dis…"], [["1. Je commence poliment", "Bonjour Monsieur / Madame. Excusez-moi de vous déranger…"], ["2. J'explique le problème", "Il y a un problème : … · Votre chien aboie toute la journée. · Il y a de l'eau qui coule du plafond."],
              ["3. Je demande une solution", "Est-ce que vous <b>pourriez</b> baisser la musique ? · Ce serait possible de… ?"], ["4. Je propose", "On <b>pourrait</b> … · Je vous propose de…"], ["5. Je remercie", "Merci beaucoup pour votre compréhension. Bonne soirée !"],
              ["On me fait un reproche", "Je suis (vraiment) désolé(e). · Je ne savais pas. · Ça ne se reproduira plus. · Excusez-moi, je fais attention."]], ["50mm", "132mm"]) +
               '<p class="sm mt2"><b>pourriez / pourrait</b> = le verbe pouvoir au conditionnel : c\'est plus <b>poli</b> (on le verra au module 11).</p>')
    e = E("Je remets le dialogue dans l'ordre (1 à 6).", '<div class="card"><p>☐ — Ah, je suis désolé ! Je ne savais pas que ça vous gênait. ☐ — Bonjour Monsieur, excusez-moi de vous déranger. ☐ — Merci beaucoup, bonne journée ! ☐ — Votre vélo est toujours dans le hall et on ne peut pas passer avec la poussette. ☐ — Je vais le mettre à la cave dès ce soir. ☐ — Bonjour. Oui ?</p></div>', ["lis", "numerote"], 2, "B",
          sol="Dans l'ordre des cases : 4 · 1 · 6 · 3 · 5 · 2")
    b.page(f'{l5}{e}', "Leçon 5")
    probs = [("🔊", "Le voisin fait la fête jusqu'à 2 h du matin."), ("🐕", "Le chien du voisin aboie quand il est seul."), ("🗑️", "Une voisine laisse ses poubelles devant ta porte."), ("💧", "De l'eau coule de ton plafond (salle de bains du voisin)."), ("🚲", "Ton vélo prend la place du voisin dans le local vélos.")]
    e = E("Jeu de rôle : je choisis une situation. Je joue la scène avec mon voisin (5 étapes). Puis on change de rôle.", '<div class="grid2">' + "".join(f'<div class="card flex"><span class="emo s">{em}</span><span class="sm">{t}</span></div>' for em, t in probs) + '</div>', ["parle", "duo"], 2, "A",
          sol="Grille d'observation : politesse, explication claire, demande au conditionnel, solution, remerciement.")
    e2 = E("J'écris un petit mot poli à glisser sous la porte d'un voisin (situation au choix).", '<div class="card" style="background:#FFFDE7;min-height:52mm">' + lines(6) + '</div>', ["ecris"], 2, "C", sol="Ex. : Bonjour Madame, je suis votre voisin du 3e. Excusez-moi de vous déranger… Est-ce que vous pourriez… ? Merci beaucoup. Yonas (3e étage)")
    b.page(f'{e}{e2}', "S'entraîner")

    # ---------- FLESco : plan à l'échelle ----------
    l6 = lecon("Lire un plan à l'échelle (méthode)", '<p>L\'<b>échelle</b> dit combien la réalité est plus grande que le dessin. <b>1 cm = 1 m</b> : 1 cm sur le plan = 1 m en vrai.</p><p>1️⃣ Je lis l\'échelle. 2️⃣ Je <b>mesure</b> avec ma latte (en cm). 3️⃣ Je <b>convertis</b> : 4 cm → 4 m. 4️⃣ Pour la <b>surface</b> d\'une pièce rectangulaire : longueur × largeur = … m² (mètres carrés).</p><p class="sm">À l\'école : en maths (échelles, aires), en géographie (cartes : 1 cm = 10 km), en sciences (schémas).</p>')
    e = E("Je mesure le plan avec ma latte. Je complète le tableau.", '<div class="c">' + plan_echelle() + '</div>' + table(["Pièce", "Longueur (m)", "Largeur (m)", "Surface (m²)"], [[p, "", "", ""] for p in ["salon", "cuisine", "chambre 1", "SdB (salle de bains)"]], ["50mm", "44mm", "44mm", "44mm"]), ["regarde", "ecris"], 2, "C",
          sol="salon 5 × 4 = 20 m² · cuisine 3 × 4 = 12 m² · chambre 1 : 4 × 4 = 16 m² · SdB (salle de bains) 3 × 4 = 12 m²")
    b.page(f'<span class="tag-doc">🎒 FRANÇAIS DE L\'ÉCOLE</span>{l6}{e}', "Consignes & école")
    e = E("Je réponds avec le plan.", f'<p>1. Quelle est la pièce la plus grande ? {blank()} 2. Quelle est la surface totale de l\'appartement ? {blank()}</p><p>3. Je veux mettre un lit de 2 m dans la chambre 2. C\'est possible ? Pourquoi ? {blank("xl")}</p><p>4. Sur une carte, l\'échelle est 1 cm = 10 km. Deux villes sont à 6 cm. La distance réelle ? {blank()}</p>', ["lis", "ecris"], 2, "B",
          sol="1. le salon (20 m²) — 2. 12 × 8 = 96 m² — 3. Oui, la chambre 2 mesure 4 m × 4 m. — 4. 60 km")
    e2 = E("Je dessine le plan de ma chambre (ou de la classe) à l'échelle 1 cm = 1 m sur le quadrillage.", '<div style="height:70mm;background-image:linear-gradient(#E7D7C2 1px,transparent 1px),linear-gradient(90deg,#E7D7C2 1px,transparent 1px);background-size:10mm 10mm;border:1px solid #C77D2E"></div>', ["dessine"], 3, "C", sol="Plan cohérent ; échelle notée.")
    b.page(f'{e}{e2}', "Consignes & école")

    # ---------- Documents de la vie ----------
    ann = '''<div class="doc" style="transform:none;padding:3mm;background:#fff;border:2px solid #C77D2E"><div class="flex" style="justify-content:space-between"><b style="font-size:14pt">🔑 IMMO-VALLÉE · Annonces · agence fictive</b><span class="xs muted">mise à jour : novembre</span></div>
<div class="grid2 mt2"><div class="card" style="padding:2.5mm"><b>A LOUER · Namur (Salzinnes)</b><p class="sm" style="margin:1mm 0">App. 2 ch. au 2e ét. avec asc. · ± 75 m² · séj. lumineux · cuis. éq. · SdB (douche) · WC séparé · cave · PEB C<br><b>Loyer : 780 €/mois</b> + 90 € charges (eau, communs)<br>Garantie locative : 2 mois · Libre au 1/12 · Animaux non admis</p></div>
<div class="card" style="padding:2.5mm"><b>A LOUER · Jambes</b><p class="sm" style="margin:1mm 0">Maison 2 façades · 3 ch. · jardin 60 m² · ± 110 m² · cuis. sem.-éq. · SdB (baignoire) · grenier · PEB E (à rénover)<br><b>Loyer : 950 €/mois</b> (charges non comprises)<br>Garantie : 2 mois · Libre de suite · Visites le samedi</p></div>
<div class="card" style="padding:2.5mm"><b>A LOUER · Namur centre</b><p class="sm" style="margin:1mm 0">Studio meublé au 4e ét. sans asc. · ± 28 m² · kitchenette · douche · idéal étudiant · PEB D<br><b>Loyer : 520 €/mois</b> charges comprises (eau, chauffage, internet)<br>Libre au 1/9</p></div>
<div class="card" style="padding:2.5mm;background:#FFF8EE"><b>📖 Les abréviations</b><p class="xs" style="margin:1mm 0">app. = appartement · ch. = chambre · ét. = étage · asc. = ascenseur · séj. = séjour (salon) · cuis. éq. = cuisine équipée · sem.-éq. = semi-équipée · SdB = salle de bains · PEB = certificat de performance énergétique (A = très économique → G = consomme beaucoup)</p></div></div></div>'''
    e = E("Je lis les annonces. Je réponds.", f'<p>1. Quel logement a un jardin ? {blank()} 2. Quel logement est meublé ? {blank()}</p><p>3. Pour l\'appartement de Salzinnes, combien je paie par mois au total ? {blank()}</p><p>4. La garantie locative de l\'appartement = combien d\'euros ? {blank()}</p><p>5. Quel logement consomme le plus d\'énergie ? Comment je le sais ? {blank("xl")}</p><p>6. Une famille de 5 avec un chat cherche un logement : quelle annonce ? Pourquoi ? {blank("xl")}</p>',
          ["lis", "ecris"], 2, "B", sol="1. la maison de Jambes — 2. le studio — 3. 780 + 90 = 870 € — 4. 2 × 780 = 1560 € — 5. la maison (PEB E) — 6. la maison de Jambes : 3 chambres, jardin, et l'appartement n'accepte pas les animaux")
    b.page(f'<span class="tag-doc">📄 DOCUMENT DE LA VIE</span><h2>Les annonces immobilières</h2>{ann}<div class="mt4">{e}</div>', "Document de la vie")
    reg = '''<div class="doc" style="transform:none;padding:4mm;background:#FBFBF7;border:1px solid #c9ced8;font-size:9.8pt;line-height:1.5"><div class="c"><b>Résidence « Les Tilleuls » · Règlement d'ordre intérieur de l'immeuble (extraits, fictif)</b></div>
<p><b>1. Calme.</b> Entre 22 h et 7 h, les occupants évitent tout bruit qui peut gêner les voisins (musique forte, cris, travaux). Les travaux bruyants sont autorisés du lundi au samedi, de 8 h à 19 h.</p>
<p><b>2. Déchets.</b> Les sacs-poubelles se déposent uniquement le mardi soir devant l'immeuble, dans les sacs officiels de la commune. Les cartons sont pliés.</p>
<p><b>3. Parties communes.</b> Le hall, les escaliers et l'ascenseur doivent rester libres. Il est interdit d'y laisser des vélos, des poussettes ou des chaussures. Les vélos se rangent dans le local vélos (sous-sol).</p>
<p><b>4. Animaux.</b> Les petits animaux sont acceptés s'ils ne dérangent pas les voisins. Les chiens sont tenus en laisse dans les parties communes.</p>
<p><b>5. Problème technique.</b> En cas de fuite d'eau ou de panne de chauffage, prévenez immédiatement le syndic : 081 00 00 00 (24 h/24).</p></div>'''
    e = E("Je lis le règlement de l'immeuble. Vrai ou faux ? Je note le numéro de la règle.", table(["", "Vrai", "Faux", "Règle n°"], [[x, '<span class="chk"></span>', '<span class="chk"></span>', ""] for x in ["Je peux passer l'aspirateur à 23 h.", "Je sors mes poubelles le lundi matin.", "Je laisse ma poussette dans le hall.", "Mon chien peut se promener sans laisse dans l'escalier.", "Il y a de l'eau au plafond : j'appelle le syndic.", "Je peux faire des travaux le samedi à 10 h."]], ["110mm", "20mm", "20mm", "32mm"]), ["lis", "coche"], 2, "B",
          sol="Faux (1) · Faux, mardi soir (2) · Faux (3) · Faux (4) · Vrai (5) · Vrai (1)")
    b.page(f'<span class="tag-doc">📄 DOCUMENT DE LA VIE</span><h2>Le règlement de l\'immeuble</h2>{reg}<div class="mt4">{e}</div><div class="astuce">Le <b>syndic</b> gère l\'immeuble (entretien, réparations des parties communes). Le <b>propriétaire</b> loue le logement au <b>locataire</b>.</div>', "Document de la vie")
    lettre = '''<div class="doc" style="transform:none;padding:4mm;background:#fff;border:1px solid #c9ced8;font-size:10pt;line-height:1.55">
<div style="text-align:right">Famille Petrenko<br>Rue des Roses 14<br>5100 Jambes</div><p>Monsieur Lemaire<br>Avenue Reine Astrid 3<br>5000 Namur</p><div style="text-align:right">Jambes, le 18 novembre</div>
<p><b>Objet : chauffage en panne</b></p><p>Monsieur,</p><p>Je suis locataire de votre maison de la rue des Roses depuis le 1er octobre. Depuis lundi, le chauffage ne fonctionne plus à l'étage : les radiateurs des trois chambres restent froids. Il fait 14 °C dans les chambres et mes enfants dorment mal.</p>
<p>Pourriez-vous envoyer un chauffagiste le plus rapidement possible ? Je suis disponible tous les jours après 16 h. Vous pouvez me joindre au 0470 00 00 00.</p><p>Je vous remercie d'avance pour votre aide.</p><p>Veuillez agréer, Monsieur, mes salutations distinguées.</p><p>Olena Petrenko</p></div>'''
    e = E("Je lis la lettre de la maman de Daria. Je retrouve les parties de la lettre.", lettre + table(["Partie", "Dans la lettre"], [["l'expéditeur (qui écrit)", ""], ["le destinataire", ""], ["le lieu et la date", ""], ["l'objet", ""], ["le problème", ""], ["la demande", ""], ["la formule finale", ""]], ["56mm", "126mm"]).replace("<td></td>", '<td style="height:6.5mm"></td>'), ["lis", "ecris"], 2, "B",
          sol="Famille Petrenko · M. Lemaire · Jambes, le 18 novembre · chauffage en panne · radiateurs froids à l'étage depuis lundi · envoyer un chauffagiste · Veuillez agréer, Monsieur, mes salutations distinguées.")
    b.page(f'<span class="tag-doc">📄 DOCUMENT DE LA VIE</span><h2>Une lettre au propriétaire</h2>{e}', "Document de la vie")

    # ---------- Sons : [s] / [z] ----------
    e = E("[s] ou [z] ? J'écoute et je répète.", '<div class="grid2"><div class="card c"><div class="huge">[s]</div><p>s, ss, c (e, i), ç, t(ion)<br>le <b>s</b>alon · la pi<b>sc</b>ine · le de<b>ss</b>ert · le gar<b>ç</b>on · la répara<b>t</b>ion</p></div><div class="card c"><div class="huge">[z]</div><p>z · s entre deux voyelles<br>la mai<b>s</b>on · la cui<b>s</b>ine · la chai<b>s</b>e · <b>z</b>éro · les‿enfants</p></div></div>', ["ecoute", "repete"], 1, "A",
          script="Paires : poisson / poison, dessert / désert, ils sont / ils ont, le cousin / le coussin. Main sur la gorge : [z] vibre.", sol="Activité orale.")
    e2 = E("J'écoute et je coche : [s] ou [z] ?", checks(8, ["[s]", "[z]"]), ["ecoute", "coche"], 2, "A", script="1. la maison — 2. le salon — 3. le coussin — 4. le cousin — 5. la cuisine — 6. la caisse — 7. douze — 8. la tasse",
           sol="1. z — 2. s — 3. s — 4. z — 5. z — 6. s — 7. z — 8. s")
    e3 = E("Je complète avec s ou ss. Puis je lis à voix haute.", '<p class="big">une mai__on · un de__ert · une chemi__e · la pi__cine (sc) · un cou__in (pour s\'asseoir) · la vali__e · le pa__age · la cui__ine</p>', ["complete", "lis"], 2, "C",
           sol="maison · dessert · chemise · piscine · coussin · valise · passage · cuisine")
    b.page(f'<h2>J\'écoute bien · [s] et [z]</h2>{e}{e2}{e3}', "Sons")
    e = E("🔁 Module 1 · Le passé composé (avoir / être).", '<p>Nous (déménager) ______________ en octobre. Ma sœur (arriver) ______________ hier.</p>', ["complete"], 2, "C", sol="avons déménagé · est arrivée")
    e2 = E("🔁 Module 1 · depuis / il y a.", '<p>J\'habite ici ______ deux ans. Nous avons visité l\'appartement ______ une semaine.</p>', ["complete"], 1, "C", sol="depuis · il y a")
    e3 = E("🔁 Module 1 · Le courriel formel.", '<p>Je commence une lettre au propriétaire par : ______________ et je termine par : ______________</p>', ["ecris"], 2, "C", sol="Monsieur / Madame, · Veuillez agréer… / Bien cordialement,")
    b.page(f'<h2>🔁 Je révise le module 1</h2>{e}{e2}{e3}', "Je révise")

    # ---------- Ateliers ----------
    e = E("Les 7 différences : je compare les deux chambres. J'écris les différences avec des prépositions.", '<div class="grid2"><div class="card c">' + chambre_scene(False) + '</div><div class="card c">' +
          chambre_scene(False).replace('>🐈<', '>🐕<').replace('x="100" y="40" font-size="22" text-anchor="middle">🪟', 'x="60" y="40" font-size="22" text-anchor="middle">🪟').replace('>🎒<', '>⚽<').replace('x="162" y="80"', 'x="40" y="80"').replace('>🪴<', '>🌵<').replace('>🧸<', '>🤖<').replace('>🖼️<', '>🕰️<') + '</div></div>' + lines(4),
          ["regarde", "ecris"], 2, "B", sol="chien au lieu du chat · fenêtre à gauche · ballon au lieu du sac · lampe au-dessus du lit (pas sur le bureau) · cactus au lieu de la plante · robot au lieu de l'ours · horloge au lieu du cadre")
    e2 = E("Le jeu des pièces : un élève pense à une pièce. Les autres posent des questions avec y (« On y dort ? On y mange ? »). Il répond oui / non.", '', ["parle", "groupe", "joue"], 1, "D", sol="Oui, on y dort → la chambre.")
    b.page(f'{atl_head("D", "Atelier · Jouer avec l espace")}{e}{e2}'.replace("l espace", "l'espace"), "Atelier")
    e = E("Je lis le message de Bilal dans le groupe de l'immeuble. Je réponds.", '<div class="card">📱 <b>Groupe « Résidence Les Tilleuls »</b><br><b>Bilal (4e) :</b> « Bonjour à tous ! Je suis Bilal, j\'habite au 4e depuis septembre avec mes parents. Samedi, on organise une petite fête des voisins dans la cour, de 15 h à 18 h. Chacun apporte quelque chose à manger. Ma mère fait des pâtisseries marocaines 😋. On y va ensemble ? »<br><b>Mme Dubois (2e) :</b> « Quelle bonne idée ! J\'y serai avec mes gaufres. »<br><b>M. Haddad (1er) :</b> « Désolé, je n\'y serai pas, je travaille. Bonne fête ! »</div>' +
          f'<p>1. Qu\'est-ce que Bilal organise ? Où ? Quand ? {blank("xl")}</p><p>2. Qui va venir ? Qui ne vient pas ? Pourquoi ? {blank("xl")}</p><p>3. Que remplace « y » dans « J\'y serai » ? {blank()}</p>', ["lis", "ecris"], 2, "B",
          sol="1. une fête des voisins dans la cour, samedi de 15 h à 18 h — 2. Mme Dubois vient ; M. Haddad ne vient pas, il travaille — 3. à la fête (dans la cour)")
    e2 = E("J'écris ma réponse dans le groupe : j'accepte (et j'apporte quelque chose) ou je refuse poliment.", lines(3), ["ecris"], 2, "C", sol="Réponse avec y.")
    b.page(f'{atl_head("C", "Atelier · Lire et écrire")}{e}{e2}', "Atelier")

    # ---------- ★ Coup de pouce ----------
    e = E("Je lis et je montre la pièce sur le dessin.", '<div class="card" style="background:#F2FBF7"><p class="big" style="line-height:1.9">J\'habite dans un appartement.<br>Il y a un salon, une cuisine et deux chambres.<br>Ma chambre est petite.<br>Mon lit est contre le mur.<br>Mon chat dort sous le lit. 🐈</p></div>' +
          '<div class="grid4">' + "".join(f'<div class="card c"><span class="emo">{e}</span><b>{t}</b></div>' for e, t in [("🛋️", "le salon"), ("🍳", "la cuisine"), ("🛏️", "la chambre"), ("🛁", "la salle de bains")]) + '</div>', ["lis", "montre"], 1, "P", alpha=True, sol="Lecture accompagnée.")
    e2 = E("J'entoure la bonne préposition.", '<div class="grid2">' + "".join(f'<div class="card"><p class="big">{t}</p></div>' for t in ["Le chat est ( sur / sous ) le lit. 🐈⬇️", "La lampe est ( sur / sous ) la table. 💡⬆️", "Le sac est ( devant / derrière ) la porte. 🎒🚪", "Le livre est ( dans / sur ) le sac. 📕🎒"]) + '</div>', ["lis", "entoure"], 1, "C", alpha=True,
           sol="sous · sur · devant · dans")
    b.page(CP.format(t="Ma maison") + e + e2, "★ Coup de pouce")
    e = E("y : je relie la question et la réponse.", relie(["Tu vas à l'école ?", "Tu habites à Namur ?", "Tu vas à la piscine ?"], ["Oui, j'y habite.", "Non, je n'y vais pas.", "Oui, j'y vais."]), ["lis", "relie"], 1, "B", alpha=True, sol="école → j'y vais · Namur → j'y habite · piscine → je n'y vais pas (ou oui)")
    e2 = E("Je décris ma chambre avec le modèle.", '<div class="card" style="background:#F2FBF7"><p class="big" style="line-height:2.2">Ma chambre est ____________ (petite / grande).<br>Il y a un lit, ____________ et ____________.<br>Mon lit est ____________ la fenêtre.<br>J\'aime ma chambre parce que ____________.</p></div>', ["ecris"], 1, "C", alpha=True, sol="Texte personnel sur le modèle.")
    b.page(CP.format(t="J'écris avec un modèle") + e + e2, "★ Coup de pouce")

    # ---------- Tâche finale ----------
    e = E("Partie 1 · J'écris une annonce pour louer un logement (réel ou imaginaire) : type, lieu, étage, surface, pièces, équipements, loyer + charges, PEB, date de disponibilité. J'utilise 3 abréviations et je dessine le plan.",
          '<div class="grid2"><div class="card" style="min-height:70mm;background:#fff"><b class="sm">Mon annonce</b>' + lines(7) + '</div><div class="card" style="min-height:70mm"><b class="sm">Le plan (échelle 1 cm = 1 m)</b></div></div>', ["ecris", "dessine"], 2, "C", sol="Toutes les informations de l'annonce + plan.")
    b.page(tache_head("Mon annonce et ma lettre au propriétaire", "J'écris une annonce de location, puis j'imagine que j'habite ce logement : j'écris une lettre au propriétaire pour signaler un problème.") + e, "Tâche finale", levels=False)
    e = E("Partie 2 · J'écris la lettre au propriétaire (comme la maman de Daria) : expéditeur, destinataire, lieu et date, objet, problème (depuis quand ?), demande polie (pourriez-vous… ?), disponibilités, formule finale, signature.", lines(12), ["ecris"], 2, "C", sol="Structure complète de la lettre.")
    b.page(e + table(["Je vérifie :", "✅"], [[x, '<span class="chk"></span>'] for x in ["Mon annonce contient toutes les informations (loyer, charges, pièces…).", "Mes adjectifs sont bien placés et accordés.", "Ma lettre a toutes les parties (objet, formule finale…).", "Ma demande est polie (pourriez-vous… ?).", "J'utilise depuis + durée pour le problème."]], ["160mm", "22mm"]), "Tâche finale", levels=False)
    e = E("Je révise.", '<p>1. un appartement (beau) → un ______ appartement 2. La lampe est à côté ___ lit. 3. Tu vas à la cave ? — Oui, j\'___ vais. 4. Tu viens du jardin ? — Oui, j\'___ viens. 5. Au mot « loyer », j\'associe : ______ 6. 4 m × 3 m = ______ m²</p>', ["ecris"], 2, "C",
          sol="bel · du · y · en · l'argent payé chaque mois au propriétaire · 12")
    e2 = E("Défi ! Je corrige les 5 erreurs.", '<div class="card big">J\'habite dans une maison petite. La télé est en face de le canapé. Tu vas au grenier ? Oui, j\'en vais. Il revient de la cave ? Oui, il y revient. C\'est un nouveau appartement.</div>' + lines(2), ["barre", "ecris"], 3, "C",
           sol="une petite maison · en face du canapé · j'y vais · il en revient · un nouvel appartement")
    b.page(f'<h2>🔁 Je révise tout le module</h2>{e}{e2}', "Je révise")

    # ---------- Test ----------
    Q = [("On dort dans…", ["la cuisine", "la chambre", "la cave", "le garage"]), ("On lave le linge dans…", ["la buanderie", "le salon", "le grenier", "le couloir"]), ("Le contraire de « calme » :", ["clair", "bruyant", "sombre", "propre"]),
         ("un ____ appartement", ["beau", "bel", "belle", "beaux"]), ("une ____ maison", ["petit", "petite", "petits", "petites"]), ("une chambre ____", ["clair", "claire", "claires", "clairs"]),
         ("La lampe est à côté ____ lit.", ["de le", "du", "de la", "des"]), ("🖼️ au-dessus du canapé : le cadre est…", ["sous le canapé", "plus haut que le canapé", "derrière le canapé", "dans le canapé"]),
         ("Tu vas à la cave ? — Oui, j'____ vais.", ["en", "y", "le", "la"]), ("Tu viens du parc ? — Oui, j'____ viens.", ["y", "en", "le", "lui"]), ("Il habite à Liège ? — Non, il ____.", ["n'en habite pas", "n'y habite pas", "y n'habite pas", "habite n'y pas"]),
         ("Futur proche + y :", ["J'y vais aller.", "Je vais y aller.", "Je vais aller y.", "Y je vais aller."]), ("Pour se plaindre poliment :", ["Arrêtez !", "Est-ce que vous pourriez baisser la musique ?", "C'est nul !", "Baisse !"]),
         ("Pour s'excuser :", ["Je suis désolé, ça ne se reproduira plus.", "Ce n'est pas moi.", "Et alors ?", "Tant pis."]), ("Dans une annonce, « ch. » =", ["charges", "chambre", "chauffage", "chien"]),
         ("Le loyer est 700 € + 80 € de charges. Total :", ["620 €", "700 €", "780 €", "880 €"]), ("Échelle 1 cm = 1 m. 5 cm sur le plan =", ["5 cm", "50 cm", "5 m", "50 m"]),
         ("Une pièce de 4 m × 5 m fait…", ["9 m²", "20 m²", "18 m²", "45 m²"]), ("Dans « maison », le s se prononce :", ["[s]", "[z]", "[ʃ]", "il est muet"]), ("🔁 Nous ____ déménagé en octobre.", ["sommes", "avons", "ont", "sont"])]
    ans = ["la chambre", "la buanderie", "bruyant", "bel", "petite", "claire", "du", "plus haut que le canapé", "y", "en", "n'y habite pas", "Je vais y aller.", "Est-ce que vous pourriez baisser la musique ?", "Je suis désolé, ça ne se reproduira plus.", "chambre", "780 €", "5 m", "20 m²", "[z]", "avons"]
    key = key_from(Q, ans)
    test_pages(b, 2, "Chez moi", Q, f'<h3>B1. Je décris ma chambre : 3 meubles avec 3 prépositions différentes. (… / 3)</h3>{lines(2, True)}<h3>B2. Je réponds avec y ou en : Tu vas souvent au parc ? / Tu reviens de l\'école à quelle heure ? (… / 2)</h3>{lines(2, True)}<h3>B3. J\'écris un mot poli à un voisin : son chien aboie toute la journée. (… / 5)</h3>{lines(3, True)}',
               [["décrire mon logement (pièces, adjectifs)", "/ 4", ""], ["dire où sont 3 objets de la classe", "/ 3", ""], ["jeu de rôle : se plaindre poliment à un voisin", "/ 3", ""]],
               f'<h3>1. Je lis et je réponds. (… / 6)</h3><div class="card big" style="line-height:1.7">J\'habite dans une maison. Il y a trois chambres. Ma chambre est grande. Mon bureau est devant la fenêtre.</div><p>Logement : ______ Chambres : ______ Ma chambre : ______ Le bureau : ______</p><h3>2. J\'entoure. (… / 4)</h3><div class="card big">Le chat est ( sur / sous ) le lit 🐈⬇️ · Tu vas à l\'école ? Oui, j\'( y / en ) vais.</div><h3>3. Je nomme 4 pièces. (… / 6)</h3>{lines(1, True)}<h3>4. Je décris ma chambre à la prof (oral). (… / 4)</h3><div class="card">☐ je comprends ☐ 2 meubles ☐ 1 préposition ☐ phrase complète</div>')
    closing(b, 2, ["Je sais nommer les pièces, les meubles, les équipements.", "Je connais les types de logement en Belgique.", "Je sais décrire un logement (il y a, se trouver, donner sur).", "Je sais placer et accorder les adjectifs (une petite maison, un bel appartement).", "Je sais dire où sont les objets avec précision.",
                   "Je sais utiliser y (lieu).", "Je sais utiliser en (venir de…).", "Je sais me plaindre et m'excuser poliment.", "Je sais lire une annonce immobilière (abréviations, loyer, charges).", "Je sais lire un plan à l'échelle et calculer une surface.", "Je sais écrire une lettre au propriétaire."],
            PIECES[:10] + MEUBLES[:6] + [("💶", "le loyer"), ("🧾", "les charges"), ("🔐", "la garantie locative"), ("👔", "le propriétaire"), ("🙋", "le locataire"), ("📐", "l'échelle"), ("⬛", "le mètre carré (m²)"), ("🏢", "le syndic")])
    plan_de_travail(b, E, 2, ["Décrire un logement", "Dire où sont les objets", "Le pronom y", "Le pronom en", "Régler un problème avec un voisin", "Lire un plan à l'échelle"], "☐ Mon annonce + plan<br>☐ Ma lettre au propriétaire")
    if render:
        to_pdf(b.html(), '/home/claude/syllabus/out/V2_M2_eleve.pdf')

    pg, exs = helpers(b, E)
    CPp = b.marks["★ Coup de pouce"]
    days = [("1", "Collectif", f"Ouverture · BD ({pg('Découvrir')})", f"Coup de pouce : ma maison (p. {CPp[0]})"), ("2", "Collectif", f"Pièces, logements, meubles ({pg('Lexique')})", "Coup de pouce : lexique en images"),
            ("3", "Rotation", f"📌 Leçon 1 décrire ({pg('Leçon 1')})", "Coup de pouce : adjectifs simples"), ("4", "Rotation", f"📌 Leçon 2 prépositions ({pg('Leçon 2')})", "Coup de pouce : sur / sous / dans"),
            ("5", "Collectif", f"📌 Leçons 3-4 y et en ({pg('Leçon 3')}, {pg('Leçon 4')})", f"Coup de pouce : y (p. {CPp[1]})"), ("6", "Rotation", f"📌 Leçon 5 voisins ({pg('Leçon 5')}) · sons ({pg('Sons')})", "Coup de pouce : jeu de rôle guidé"),
            ("7", "Collectif", f"Plan à l'échelle ({pg('Consignes & école')}) — prévoir des lattes", "Coup de pouce : mesurer avec aide"), ("8", "Rotation", f"Annonces, règlement, lettre ({pg('Document de la vie')}) · ateliers ({pg('Atelier')})", "Coup de pouce : modèle de chambre"),
            ("9", "Seul", f"Tâche finale ({pg('Tâche finale')})", "Coup de pouce : annonce à trous + mot au voisin"), ("10", "Seul", f"Test ({pg('Test')})", f"Coup de pouce : test adapté ({pg('★ Coup de pouce · Test')})")]
    rot = [["🎧 Écouter-Parler", "Jeu de rôle voisins · dictée de dessin", "20 min", "—"], ["📖 Lire", "Annonces · règlement · lettre", "20 min", "Oui"], ["✏️ Écrire", "Mot au voisin · description de logement", "20 min", "● oui"],
           ["🧩 Jouer", "7 différences · jeu des pièces (y)", "20 min", "Corrigé au dos"], ["👩‍🏫 Table d'appui", "Coup de pouce · y / en", "20 min", "—"]]
    ev1 = '''<h3>Partie B (10 points)</h3><p class="sm"><b>B1</b> : 1 pt par préposition juste (du / de la) · <b>B2</b> : <span class="sol">Oui, j'y vais souvent / Non, je n'y vais pas souvent. · J'en reviens à 16 h.</span> · <b>B3</b> : formule polie (1), problème (1), demande au conditionnel (2), remerciement (1).</p>
<h3>Test ★ Coup de pouce</h3><p class="sm"><b>Ex. 1 :</b> <span class="sol">une maison · trois · grande · devant la fenêtre</span> · <b>Ex. 2 :</b> <span class="sol">sous · y</span> · <b>Ex. 3 :</b> 4 pièces au choix.</p>'''
    ev2 = f'''<h2>Grille · tâche finale « Mon annonce et ma lettre au propriétaire »</h2>{table(["Critère", "Très bien", "Bien", "À retravailler", "Points"], [["<b>Annonce</b> : informations complètes, abréviations", "Complète", "Partielle", "Pauvre", "/ 5"], ["<b>Plan</b> à l'échelle", "Juste", "Approximatif", "Absent", "/ 3"], ["<b>Lettre</b> : toutes les parties", "Oui", "Il manque 1-2", "Beaucoup", "/ 5"], ["<b>Politesse</b> : conditionnel, formules", "Oui", "Partielle", "Non", "/ 3"], ["<b>Langue</b> : adjectifs, prépositions, depuis", "Correcte", "Quelques erreurs", "Beaucoup", "/ 4"]], ["64mm", "32mm", "32mm", "32mm", "22mm"])}
<h2 class="mt4">Différencier et remédier</h2>{table(["Difficulté", "Remédiation"], [["Prépositions", "Manipuler des objets réels (une boîte, un crayon) ; dictée de dessin en duo."], ["y / en", "Flèches au tableau : ➡️ vers le lieu = y ; ⬅️ quitter le lieu = en ; tri d'étiquettes de verbes (aller, venir, sortir…)."], ["Place de l'adjectif", "Mémo « BAGS » (Beauté, Âge, Grandeur, bonté) affiché : ces adjectifs vont avant."], ["Échelle et surface", "Mesurer d'abord la classe en vrai (mètre ruban), puis la dessiner."], ["Élève rapide", "Comparer 3 vraies annonces (sites immobiliers) : rapport qualité-prix, PEB, charges."]], ["50mm", "132mm"])}
<div class="astuce mt4"><b>Sensibilité :</b> certains élèves vivent en centre d'accueil, en logement provisoire ou à plusieurs dans une pièce. Toujours proposer « un logement réel <b>ou imaginaire</b> ». Ne jamais demander de photos du logement. Les informations sur les droits des locataires (garantie, état des lieux, logement social) peuvent être utiles aux familles : lien avec le CPAS ou une AIS si besoin.</div>'''
    T = teacher_book(b, E, "V2 · M2", "", MC, 2, "Chez moi",
                     "<li><b>Communication :</b> décrire un logement, situer des objets, régler un problème de voisinage.</li><li><b>Lexique :</b> pièces, types de logement, meubles, équipements, location (loyer, charges, garantie, PEB).</li><li><b>Grammaire :</b> place et accord de l'adjectif (bel, nouvel, vieil) ; prépositions de lieu ; pronoms y et en (lieu).</li><li><b>Phonétique :</b> [s] / [z].</li><li><b>FLSco :</b> plan à l'échelle, surface en m².</li><li><b>Documents :</b> annonces immobilières, règlement d'immeuble, lettre au propriétaire, message de groupe.</li><li><b>★ Coup de pouce :</b> ma maison, sur / sous / dans, y, description guidée.</li>",
                     '<p class="sm"><b style="color:#E4572E">Indispensable</b> : pièces et meubles, prépositions courantes, se plaindre / s\'excuser poliment.</p><p class="sm"><b style="color:#d9a400">Important</b> : y, lire une annonce, lettre au propriétaire.</p><p class="sm"><b style="color:#2BA88F">Enrichissement</b> : en (lieu), échelle et surfaces, PEB.</p>',
                     "Lattes et mètre ruban · objets à manipuler · annonces réelles (journal, site) · catalogue de meubles à découper (facultatif).", "<b>Lien maths :</b> la page « plan à l'échelle » peut se faire avec le professeur de mathématiques (aire du rectangle, conversions).",
                     days, "« Où est… ? » avec un objet caché · une phrase avec y · l'annonce du jour (une vraie annonce lue ensemble).", rot, key, (ev1, ev2), start=tstart)
    if render:
        to_pdf(T.html(), '/home/claude/syllabus/out/V2_M2_prof.pdf')
    return b, T


if __name__ == "__main__":
    b, T = build_v2m2()
    print(b.n, T.n)
