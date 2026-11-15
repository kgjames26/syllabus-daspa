"""Volume 1 · Module 6 « À table ! »."""
import sys
sys.path.insert(0, '/home/claude/syllabus')
from lib.base import *
from lib.art import *
from lib.alpha import AL, letter_page, syll_table
from lib.module import *
from lib.render import to_pdf

MC = "#E07A1F"
ALIM = [("🍞", "le pain"), ("🧀", "le fromage"), ("🥛", "le lait"), ("🧈", "le beurre"), ("🥚", "l'œuf"), ("🍗", "le poulet"), ("🐟", "le poisson"), ("🥩", "la viande"),
        ("🍚", "le riz"), ("🍝", "les pâtes"), ("🥔", "les pommes de terre"), ("🍟", "les frites"), ("🥗", "la salade"), ("🥕", "la carotte"), ("🍅", "la tomate"), ("🥦", "le brocoli"),
        ("🍎", "la pomme"), ("🍌", "la banane"), ("🍊", "l'orange"), ("🍓", "la fraise"), ("🍫", "le chocolat"), ("🍰", "le gâteau"), ("💧", "l'eau"), ("🧃", "le jus")]


def build_m6(start=1, tstart=1, render=True):
    b = Book("V1 · M6", "Volume 1 · Premiers pas · Module 6 · À table !", MC, start=start)
    E = Ex(b)
    vis = '<div class="c" style="font-size:40pt;line-height:1.3">🍞🧀🥗🍝🍗<br>🍎🍌🍰🥛🧃</div>'
    opening(b, MC, 6, "À table !", vis, [("🍽️", "nommer les aliments et les repas"), ("❤️", "dire ce que j'aime et ce que je n'aime pas"), ("🚫", "dire non : je ne mange pas…"),
            ("🥖", "dire du pain, de la soupe, des frites"), ("📋", "lire le menu de la cantine"), ("👩‍🍳", "suivre une recette")],
            ["Qu'est-ce que tu manges le matin ?", "Quel est ton plat préféré ? Un plat de ton pays ?", "Il y a des aliments que tu ne manges pas ? Pourquoi ?"],
            ["le petit-déjeuner", "le dîner", "le souper", "j'aime", "je n'aime pas", "le menu", "la recette", "du pain", "de l'eau", "végétarien"], "#FFF1E3")
    bd = '<div class="grid2" style="gap:3mm">' + "".join([
        bd_case(1, lr("fatou", ["Midi ! On va au réfectoire ? J'ai faim !"], "amina", ["Oui ! Qu'est-ce qu'il y a au menu ?"], "rire")),
        bd_case(2, lr("bilal", ["Aujourd'hui : soupe aux légumes, poulet, riz et une pomme."], extra='<div class="c" style="font-size:28pt">🥣🍗🍚🍎</div>')),
        bd_case(3, lr("amina", ["Moi, je ne mange pas de porc. Il y a du porc ?"], "educ", ["Non, c'est du poulet. Et il y a toujours un plat végétarien."], "pense")),
        bd_case(4, lr("mateo", ["Beurk ! Je n'aime pas la soupe !"], "fatou", ["Moi, j'adore la soupe ! Tu me donnes ta soupe ?"], "triste", "rire")),
        bd_case(5, lr("daria", ["En Ukraine, on mange du bortsch : c'est une soupe rouge avec des betteraves."], "yonas", ["Chez moi, on mange de l'injera avec les doigts !"], "sourire", "rire")),
        bd_case(6, lr("mateo", ["Hmm, le poulet est délicieux ! Bon appétit !"], "bilal", ["Bon appétit ! Tu peux me passer l'eau, s'il te plaît ?"], "rire")),
    ]) + '</div>'
    e = E("J'écoute et je regarde la BD : au réfectoire.", bd, ["ecoute", "regarde"], 1, "A", script="Lire la BD deux fois. Mimer « beurk » et « miam ». Faire répéter : « J'ai faim », « Bon appétit », « Tu peux me passer… ? ».", sol="Activité orale.")
    b.page(f'<h2>Découvrir · Au réfectoire</h2>{e}', "Découvrir")
    e = E("Je réponds.", f'<p>1. Qu\'est-ce qu\'il y a au menu ? {blank("xl")}</p><p>2. Qu\'est-ce qu\'Amina ne mange pas ? {blank()}</p><p>3. Qui n\'aime pas la soupe ? {blank()}</p><p>4. Qu\'est-ce que le bortsch ? {blank("xl")}</p><p>5. Que dit Bilal pour demander l\'eau ? {blank("xl")}</p>',
          ["lis", "ecris"], 1, "B", sol="1. soupe aux légumes, poulet, riz, une pomme — 2. du porc — 3. Mateo — 4. une soupe rouge ukrainienne avec des betteraves — 5. Tu peux me passer l'eau, s'il te plaît ?")
    e2 = E("Vrai ou faux ?", vf(["Il y a toujours un plat végétarien.", "Fatou n'aime pas la soupe.", "Yonas mange l'injera avec une fourchette.", "Mateo aime le poulet."]), ["lis", "coche"], 2, "B", sol="Vrai · Faux (elle adore) · Faux (avec les doigts) · Vrai")
    e3 = E("Défi ! Je présente un plat de mon pays à la classe (3 phrases).", lines(3), ["parle", "ecris"], 3, "C", sol="Production libre : Chez moi, on mange… C'est… J'aime…")
    b.page(f'{e}{e2}{e3}<div class="astuce">🇧🇪 En Belgique, on dit <b>le déjeuner</b> (le matin), <b>le dîner</b> (à midi) et <b>le souper</b> (le soir). En France : petit-déjeuner, déjeuner, dîner. Les deux sont corrects !</div>', "Découvrir")

    e = E("Les aliments. J'écoute et je répète.", emogrid(ALIM, 6), ["ecoute", "repete"], 1, "A", script="Montrer chaque image, dire le mot, faire répéter. Classer ensemble : fruits, légumes, viande/poisson, produits laitiers, féculents, sucreries, boissons.", sol="Activité orale.")
    e2 = E("Je classe les aliments dans la bonne famille.", table(["🍎 Fruits", "🥕 Légumes", "🍗 Viande / poisson / œuf", "🧀 Lait / fromage", "🍞 Pain, riz, pâtes"], [["", "", "", "", ""]]).replace("<td></td>", '<td style="height:30mm"></td>'), ["lis", "ecris"], 2, "C",
           sol="Fruits : pomme, banane, orange, fraise · Légumes : carotte, tomate, brocoli, salade · Viande… : poulet, poisson, viande, œuf · Lait : lait, fromage, beurre · Féculents : pain, riz, pâtes, pommes de terre")
    b.page(f'<h2>Les aliments</h2>{e}{e2}', "Lexique")

    l1 = lecon("Les repas · Exprimer ses goûts", f'''{table(["Repas", "Belgique", "Quand ?", "Exemple"], [["🌅", "le déjeuner", "le matin", "du pain, du lait, des céréales"], ["☀️", "le dîner", "à midi", "de la soupe, du poulet, du riz"], ["🍪", "le goûter (les 4 heures)", "l'après-midi", "un fruit, un biscuit"], ["🌙", "le souper", "le soir", "des pâtes, de la salade"]], ["14mm", "40mm", "36mm", "92mm"])}
<div class="grid4 mt2">{"".join(f'<div class="card c" style="background:#fff;padding:2mm"><span class="emo s">{e}</span><b class="sm">{t}</b></div>' for e, t in [("😍", "J'adore"), ("😋", "J'aime (bien)"), ("😕", "Je n'aime pas"), ("🤢", "Je déteste")])}</div>
<p class="mt2">J'aime <b>le</b> chocolat. Je n'aime pas <b>les</b> carottes. (après aimer, adorer, détester → <b>le, la, les</b>)</p><p>Et toi ? — <b>Moi aussi</b> 👍 / <b>Moi non</b> 👎 · — Je n'aime pas… — <b>Moi non plus</b> / <b>Moi si</b>.</p>''')
    e = E("Sondage : je pose la question à 4 camarades. « Tu aimes… ? »", table(["Prénom", "le poisson", "les frites", "la salade", "le chocolat"], [["", "", "", "", ""] for _ in range(4)], ["40mm", "35mm", "35mm", "35mm", "37mm"]).replace("<td></td>", '<td style="height:9mm"></td>'),
          ["parle", "ecris", "groupe"], 1, "A", sol="Réponses personnelles (noter 😍 😋 😕 🤢).")
    b.page(f'{l1}{e}', "Leçon 1")
    e = E("J'écoute Mateo et Daria. Je coche ce qu'ils aiment 😋 ou n'aiment pas 😕.", table(["", "🍝 pâtes", "🐟 poisson", "🍫 chocolat", "🥦 brocoli"], [["Mateo", "", "", "", ""], ["Daria", "", "", "", ""]], ["30mm", "38mm", "38mm", "38mm", "38mm"]).replace("<td></td>", '<td style="height:9mm"></td>'),
          ["ecoute", "coche"], 2, "A", script="Mateo : « J'adore les pâtes ! Je n'aime pas le poisson. J'aime le chocolat, bien sûr. Le brocoli ? Je déteste ! » — Daria : « Moi, j'aime le poisson. Les pâtes, j'aime bien. Je n'aime pas beaucoup le chocolat. Et j'adore le brocoli ! »",
          sol="Mateo : pâtes 😍, poisson 😕, chocolat 😋, brocoli 🤢 · Daria : pâtes 😋, poisson 😋, chocolat 😕, brocoli 😍")
    e2 = E("Moi aussi, moi non plus, moi si, moi non ? Je réponds.", '<p>1. — J\'aime les fraises. — (je suis d\'accord) ______</p><p>2. — Je n\'aime pas le café. — (je suis d\'accord) ______</p><p>3. — J\'aime le poisson. — (je ne suis pas d\'accord) ______</p><p>4. — Je n\'aime pas le riz. — (je ne suis pas d\'accord) ______</p>', ["complete"], 3, "C",
           sol="Moi aussi · Moi non plus · Moi non · Moi si")
    e3 = E("J'écris 4 phrases : j'adore, j'aime, je n'aime pas, je déteste.", lines(4), ["ecris"], 2, "C", sol="Production personnelle (le, la, les).")
    b.page(f'{e}{e2}{e3}', "S'entraîner")

    l2 = lecon("Du, de la, de l', des (une quantité qu'on ne compte pas)", f'''{table(["", "Je mange / je bois…", "Exemple"], [["masculin", "<b>du</b>", "du pain, du fromage, du riz"], ["féminin", "<b>de la</b>", "de la soupe, de la viande, de la salade"], ["voyelle", "<b>de l'</b>", "de l'eau, de l'huile"], ["pluriel", "<b>des</b>", "des pâtes, des frites, des fraises"]], ["40mm", "50mm", "92mm"])}
<div class="grid2 mt2"><div class="astuce" style="margin:0">J'<b>aime le</b> pain (en général) → Je <b>mange du</b> pain (une partie).</div><div class="attention" style="margin:0">Avec la négation : <b>pas de</b> / <b>pas d'</b><br>Je ne mange <b>pas de</b> viande. Je ne bois <b>pas d'</b>eau gazeuse.</div></div>''')
    e = E("Du, de la, de l' ou des ? Je complète.", '<div class="grid2">' + "".join(f'<p>Je mange {blank("s")} {w}.</p>' for w in ["pain", "soupe", "frites", "riz", "viande", "fraises"]) + "".join(f'<p>Je bois {blank("s")} {w}.</p>' for w in ["eau", "lait"]) + '</div>', ["complete"], 1, "C",
          sol="du pain · de la soupe · des frites · du riz · de la viande · des fraises · de l'eau · du lait")
    b.page(f'{l2}{e}', "Leçon 2")

    l3 = lecon("La négation : ne… pas", f'''<p class="big">Je mange du porc. → Je <b>ne</b> mange <b>pas</b> de porc.</p><p class="big">J'aime le café. → Je <b>n'</b>aime <b>pas</b> le café.</p>
<div class="grid2 mt2"><div class="card" style="background:#fff">Le verbe est <b>au milieu</b> : ne + <u>verbe</u> + pas<br>ne → <b>n'</b> devant une voyelle (n'aime, n'ai, n'est)</div><div class="card" style="background:#fff">À l'oral, on oublie souvent « ne » : « J'aime pas » 🗣️ — mais à l'écrit, on l'écrit toujours ✍️ !</div></div>''')
    e = E("Je mets à la forme négative.", '<p>1. Je mange de la viande. → ______________________</p><p>2. Tu aimes les carottes. → ______________________</p><p>3. Il boit du café. → ______________________</p><p>4. J\'ai faim. → ______________________</p>', ["ecris"], 2, "C",
          sol="1. Je ne mange pas de viande. — 2. Tu n'aimes pas les carottes. — 3. Il ne boit pas de café. — 4. Je n'ai pas faim.")
    e2 = E("Ce que je mange et ce que je ne mange pas (régimes, religions, allergies, goûts). J'écris 2 phrases.", lines(2), ["ecris"], 2, "C", sol="Exemple : Je ne mange pas de porc. Je mange du poulet. (Respecter les choix de chacun.)")
    b.page(f'{l3}{e}{e2}', "Leçon 3")

    menu = [("Lundi", "Soupe de tomates", "Spaghetti bolognaise 🍝 / ♣ spaghetti aux légumes", "Yaourt"), ("Mardi", "—", "Poulet, riz, haricots verts 🍗", "Pomme"),
            ("Mercredi", "—", "(pas de repas : pas cours l'après-midi)", "—"), ("Jeudi", "Soupe aux légumes", "Poisson pané, purée, épinards 🐟 / ♣ omelette", "Banane"), ("Vendredi", "—", "Boulettes sauce tomate, frites 🍟 / ♣ boulettes végétales", "Gâteau au chocolat 🍰")]
    mt = "".join(f'<tr><td style="padding:1.8mm;border:1px solid #e6d3bf;font-weight:700;background:#FFF1E3">{d}</td><td style="padding:1.8mm;border:1px solid #e6d3bf">{s}</td><td style="padding:1.8mm;border:1px solid #e6d3bf">{p}</td><td style="padding:1.8mm;border:1px solid #e6d3bf">{d2}</td></tr>' for d, s, p, d2 in menu)
    e = E("Je lis le menu. Je réponds.", f'<div class="grid2"><p>1. Le lundi, l\'entrée : {blank()}</p><p>2. Le jeudi, le plat : {blank("l")}</p><p>3. Il y a des frites quel jour ? {blank()}</p><p>4. Le dessert du vendredi : {blank()}</p><p>5. Que veut dire ♣ ? {blank()}</p><p>6. Prix d\'un repas : {blank()}</p></div>',
          ["lis", "ecris"], 2, "B", sol="1. soupe de tomates — 2. poisson pané, purée, épinards — 3. vendredi — 4. gâteau au chocolat — 5. plat végétarien — 6. 4,20 €")
    b.page(f'''<span class="tag-doc">📄 DOCUMENT DE LA VIE</span><h2>Le menu du réfectoire</h2><div class="doc" style="transform:none;padding:3mm"><div class="flex" style="justify-content:space-between"><b style="color:{MC}">ATHÉNÉE DES TILLEULS · Menu de la semaine du 12 au 16 octobre</b><span class="pill">Repas : 4,20 €</span></div>
<table style="border-collapse:collapse;width:100%;font-size:10pt;font-family:Inter;margin-top:2mm"><tr><th style="background:{MC};color:#fff;padding:1.5mm">Jour</th><th style="background:{MC};color:#fff">Entrée</th><th style="background:{MC};color:#fff">Plat</th><th style="background:{MC};color:#fff">Dessert</th></tr>{mt}</table>
<p class="xs muted mt2">♣ = plat végétarien. Allergies : prévenir l'éducateur. Le pain et l'eau sont à volonté.</p></div><div class="mt4">{e}</div>''', "Document de la vie")
    e = E("Je choisis mon menu pour la semaine et je l'explique : « Le lundi, je prends… parce que j'aime… »", lines(4), ["ecris"], 2, "C", sol="Production libre.")
    e2 = E("Défi ! Je calcule : je mange au réfectoire 4 jours par semaine. Combien je paie ? Et pour 4 semaines ?", f'<p>1 semaine : {blank()} · 4 semaines : {blank()}</p>', ["ecris"], 3, "C", sol="4 × 4,20 = 16,80 € · 4 × 16,80 = 67,20 €")
    b.page(f'{e}{e2}', "Document de la vie")

    rec = '''<div class="doc" style="transform:none;padding:4mm"><div class="c" style="font-size:16pt;font-weight:800;color:#E07A1F">🥞 LES CRÊPES (pour 4 personnes)</div>
<div class="grid2 mt2"><div class="card"><b>Ingrédients</b><p>🌾 250 g de farine<br>🥚 4 œufs<br>🥛 ½ litre de lait<br>🧂 une pincée de sel<br>🧈 un peu de beurre</p></div><div class="card"><b>Ustensiles</b><p>🥣 un saladier · 🥄 un fouet · 🍳 une poêle · 🥄 une louche</p></div></div>
<div class="card mt2"><b>Préparation</b><p>1. Mettez la farine et le sel dans le saladier.<br>2. Ajoutez les œufs et mélangez.<br>3. Versez le lait petit à petit. Mélangez bien avec le fouet.<br>4. Laissez reposer la pâte 30 minutes.<br>5. Faites chauffer la poêle avec un peu de beurre.<br>6. Versez une louche de pâte. Faites cuire 1 minute de chaque côté.<br>7. Mangez avec du sucre, de la confiture ou du chocolat. Bon appétit !</p></div></div>'''
    l4 = lecon("Lire une recette", '<p>Une recette a 3 parties : <b>les ingrédients</b> (quoi ?), <b>les ustensiles</b> (avec quoi ?), <b>la préparation</b> (comment ? — les étapes numérotées). Les verbes sont à <b>l\'impératif</b> (vous) : mettez, ajoutez, mélangez, versez.</p>')
    e = E("Je lis la recette. Je réponds.", f'<p>1. Combien d\'œufs ? {blank("s")} 2. Combien de lait ? {blank()} 3. La pâte repose combien de temps ? {blank()}</p><p>4. J\'entoure les verbes à l\'impératif dans la recette. 5. ●●● Je cherche dans le dictionnaire (ou je demande) : « une pincée » = {blank("l")}</p>',
          ["lis", "entoure", "ecris"], 2, "B", sol="1. 4 — 2. ½ litre — 3. 30 minutes — 4. mettez, ajoutez, mélangez, versez, laissez, faites, mangez — 5. une très petite quantité (entre deux doigts)")
    b.page(f'<span class="tag-doc">🎒 FRANÇAIS DE L\'ÉCOLE</span>{l4}{rec}{e}', "Consignes & école")
    e = E("Je remets les étapes de la recette dans l'ordre (sans regarder !).", '<div class="card">' + "".join(f'<p><span class="circ"></span>{t}</p>' for t in ["Versez une louche de pâte dans la poêle.", "Mettez la farine dans le saladier.", "Laissez reposer 30 minutes.", "Ajoutez les œufs.", "Versez le lait petit à petit."]) + '</div>', ["lis", "numerote"], 2, "B",
          sol="Ordre affiché : 5 – 1 – 4 – 2 – 3")
    e2 = E("Défi ! J'écris la recette d'un plat simple de mon pays (ingrédients + 4 étapes à l'impératif).", lines(6), ["ecris"], 3, "C", sol="Production libre ; vérifier l'impératif et les quantités.")
    b.page(f'{e}{e2}', "Consignes & école")

    e = E("[b] / [p], [u] « ou », [ɔ̃] « on ». J'écoute et je répète.", '<div class="grid3"><div class="card c"><div class="huge">[b] / [p]</div><p>beurre / peur · bain / pain · boire / poire</p></div><div class="card c"><div class="huge">[u] ou</div><p>soupe · poulet · fourchette · goût</p></div><div class="card c"><div class="huge">[ɔ̃] on</div><p>bonbon · melon · poisson · on mange</p></div></div>', ["ecoute", "repete"], 1, "A",
          script="Paires : bain/pain, boire/poire, bonbon/pompon. Faire sentir l'air du nez pour [ɔ̃].", sol="Activité orale.")
    e2 = E("J'écoute : [b] ou [p] ?", checks(8, ["[b]", "[p]"]), ["ecoute", "coche"], 2, "A", script="1. pain — 2. beurre — 3. pomme — 4. banane — 5. poulet — 6. boire — 7. poisson — 8. bonbon", sol="1. p — 2. b — 3. p — 4. b — 5. p — 6. b — 7. p — 8. b")
    b.page(f'<h2>J\'écoute bien</h2>{e}{e2}', "Sons")

    e = E("🔁 Module 5 · J'ai mal…", '<p>J\'ai trop mangé : j\'ai mal ___ ventre. J\'ai mangé trop de bonbons : j\'ai mal ___ dents.</p>', ["complete"], 1, "C", sol="au · aux")
    e2 = E("🔁 Module 4 · J'accorde.", '<p>La soupe est (bon) ______. Les frites sont (chaud) ______. Le gâteau est (petit) ______.</p>', ["complete"], 2, "C", sol="bonne · chaudes · petit")
    e3 = E("🔁 Module 3 · L'heure des repas : j'écris en lettres.", '<p>Le dîner est à 11 h 55 → ______________ · Le souper est à 19 h → ______________</p>', ["ecris"], 2, "C", sol="onze heures cinquante-cinq · dix-neuf heures")
    b.page(f'<h2>🔁 Je révise les modules 3 à 5</h2>{e}{e2}{e3}', "Je révise")

    e = E("Au restaurant : je joue la scène (serveur / client) avec le menu.", '<div class="card"><p>— Bonjour, vous désirez ? — Je voudrais une soupe et du poulet, s\'il vous plaît. — Et comme boisson ? — De l\'eau, s\'il vous plaît. — Voilà ! Bon appétit ! — L\'addition, s\'il vous plaît !</p></div>', ["parle", "duo"], 2, "A", sol="Jeu de rôle.")
    e2 = E("Le loto des aliments : la prof dit un aliment, je pose un jeton.", emogrid([(e, "") for e, w in ALIM[:12]], 6, False), ["ecoute", "joue"], 1, "D", script="Dire au hasard : le fromage, le poisson, le pain, le riz…", sol="Jeu.")
    b.page(f'{atl_head("A", "Ateliers · Parler et jouer")}{e}{e2}', "Atelier")
    txt = '<div class="card" style="background:#FFFDF8;line-height:1.6"><b>Le petit-déjeuner dans le monde</b><br>En Belgique, on mange souvent des tartines avec du beurre et de la confiture, ou du choco. On boit du lait, du café ou du thé. Au Maroc, on mange du pain avec de l\'huile d\'olive et du miel, et on boit du thé à la menthe. Au Japon, on mange du riz, de la soupe miso et du poisson. En Colombie, on mange des arepas : des petites galettes de maïs avec du fromage. Et toi ?</div>'
    e = E("Je lis le texte.", txt, ["lis"], 1, "B")
    e2 = E("Je relie le pays et le petit-déjeuner.", relie(["la Belgique", "le Maroc", "le Japon", "la Colombie"], ["riz, soupe miso, poisson", "arepas au fromage", "tartines, choco", "pain, huile d'olive, thé à la menthe"]), ["lis", "relie"], 2, "B",
           sol="Belgique → tartines · Maroc → huile d'olive, thé · Japon → riz, miso · Colombie → arepas")
    e3 = E("J'écris mon petit-déjeuner (3 phrases avec du, de la, des).", lines(3), ["ecris"], 2, "C", sol="Production personnelle.")
    b.page(f'{atl_head("B", "Ateliers · Lire et écrire")}{e}{e2}{e3}', "Atelier")

    letter_page(b, E, "b", "[b]", [("🍌", "banane"), ("🍬", "bonbon"), ("🧈", "beurre"), ("🚌", "bus")], "dpqdpdqp", [("🍌", "banane", 1), ("🍬", "bonbon", 1), ("🍞", "pain", 0), ("🚌", "bus", 1), ("🍎", "pomme", 0), ("🥖", "baguette", 1), ("🐟", "poisson", 0), ("🧈", "beurre", 1)], MC)
    letter_page(b, E, "ou", "[u]", [("🥣", "soupe"), ("🍗", "poulet"), ("🐺", "loup"), ("🛞", "roue")], "uonuoaun", [("🥣", "soupe", 1), ("🍗", "poulet", 1), ("🍌", "banane", 0), ("🐺", "loup", 1), ("🌙", "lune", 0), ("🍴", "fourchette", 1), ("🚌", "bus", 0), ("🛞", "roue", 1)], MC)
    letter_page(b, E, "on", "[ɔ̃]", [("🍬", "bonbon"), ("🐟", "poisson"), ("🍈", "melon"), ("🦁", "lion")], "oanounao", [("🍬", "bonbon", 1), ("🐟", "poisson", 1), ("🥣", "soupe", 0), ("🍈", "melon", 1), ("🦁", "lion", 1), ("🍎", "pomme", 0), ("🍌", "banane", 0), ("🧅", "oignon", 1)], MC)
    e = E("Je lis les mots du repas.", '<div class="grid4">' + "".join(f'<div class="card c"><span class="emo s">{e}</span><div class="huge" style="font-size:16pt">{w.replace("-", "<span style=color:#E4572E>·</span>")}</div></div>' for e, w in [("🍌", "ba-na-ne"), ("🍬", "bon-bon"), ("🥣", "sou-pe"), ("🍗", "pou-let"), ("🍈", "me-lon"), ("🐟", "poi-sson"), ("🍅", "to-ma-te"), ("🥗", "sa-la-de")]) + '</div>',
          ["lis"], 1, "P", alpha=True, script="Lecture syllabique puis globale.", sol="banane · bonbon · soupe · poulet · melon · poisson · tomate · salade")
    e2 = E("Je lis les phrases.", '<div class="grid2">' + "".join(f'<div class="card"><p class="big">{t}</p></div>' for t in ["Papa mange du poulet.", "Mila a un bonbon.", "Je bois de la soupe.", "Rémi aime le melon."]) + '</div>', ["lis"], 2, "B", alpha=True, sol="Lecture.")
    e3 = E("Dictée.", guide_lines(2, 20), ["ecoute", "ecris"], 2, "P", alpha=True, script="Dicter : bou — bon — ba — soupe — bonbon — poulet", sol="bou bon ba soupe bonbon poulet")
    b.page(AL.format(t="Je lis et j'écris") + e + e2 + e3, "★ Alpha", color=MC)

    grid = table(["Jour", "Entrée", "Plat (+ ♣ végétarien)", "Dessert"], [[d, "", "", ""] for d in ["Lundi", "Mardi", "Jeudi", "Vendredi"]], ["26mm", "44mm", "68mm", "44mm"]).replace("<td></td>", '<td style="height:20mm"></td>')
    e = E("En groupe, nous composons le menu de la semaine de la classe : équilibré, avec un plat végétarien, et un plat d'un pays de la classe chaque jour.", grid, ["ecris", "groupe"], 2, "C", sol="Évaluation avec la grille.")
    b.page(tache_head("Le menu de la classe", "Nous inventons un menu équilibré pour une semaine. Puis nous le présentons et nous votons pour le meilleur menu.") + e +
           table(["Je vérifie :", "✅"], [[x, '<span class="chk"></span>'] for x in ["Chaque jour : une entrée ou un fruit, un plat, un dessert.", "Un plat végétarien chaque jour.", "Des plats de nos pays.", "J'écris du, de la, des correctement.", "Je présente le menu : « Le lundi, il y a… »"]], ["160mm", "22mm"]), "Tâche finale", levels=False)
    e = E("Je révise : du, de la, des / pas de.", '<p>Je mange ___ riz et ___ salade. Je bois ___ eau. Je ne mange pas ___ viande.</p>', ["complete"], 1, "C", sol="du · de la · de l' · de")
    e2 = E("J'aime / je n'aime pas : forme négative.", '<p>J\'aime les épinards. → ______________________</p>', ["ecris"], 2, "C", sol="Je n'aime pas les épinards.")
    e3 = E("Défi ! Je corrige les 3 erreurs.", '<div class="card big">Je mange de le pain. Je ne bois pas du lait. J\'aime pas les frites.</div>' + lines(2), ["barre", "ecris"], 3, "C", sol="du pain · pas de lait · Je n'aime pas les frites")
    b.page(f'<h2>🔁 Je révise tout le module</h2>{e}{e2}{e3}', "Je révise")

    Q = [("🍞 =", ["le fromage", "le pain", "le beurre", "le lait"]), ("🐟 =", ["le poulet", "la viande", "le poisson", "l'œuf"]), ("Une fraise, c'est :", ["un légume", "un fruit", "une boisson", "un plat"]),
         ("En Belgique, le repas de midi s'appelle :", ["le dîner", "le souper", "le déjeuner", "le goûter"]), ("Le repas du soir en Belgique :", ["le déjeuner", "le dîner", "le souper", "la collation"]),
         ("😍 =", ["Je déteste", "J'adore", "Je n'aime pas", "Je mange"]), ("Je mange ____ pain.", ["du", "de la", "des", "de l'"]), ("Je bois ____ eau.", ["du", "de la", "de l'", "des"]),
         ("Je mange ____ frites.", ["du", "de la", "de l'", "des"]), ("Je ne mange pas ____ viande.", ["de la", "du", "de", "des"]),
         ("Forme négative de « J'aime le café » :", ["Je aime pas le café.", "Je n'aime pas le café.", "Je ne pas aime le café.", "J'aime ne pas le café."]), ("— Je n'aime pas le riz. — D'accord : ____", ["Moi aussi.", "Moi si.", "Moi non plus.", "Moi oui."]),
         ("Sur le menu, ♣ veut dire :", ["plat végétarien", "plat épicé", "plat chaud", "dessert"]), ("Dans une recette, « Mélangez » est :", ["un ingrédient", "un ustensile", "une étape", "un prix"]),
         ("Pour la recette des crêpes, il faut combien d'œufs ?", ["2", "4", "6", "250"]), ("« Tu peux me passer l'eau, s'il te plaît ? » est :", ["poli", "pas poli", "une question sur l'heure", "un ordre du médecin"]),
         ("J'entends [ɔ̃] comme dans « bonbon » :", ["soupe", "poisson", "banane", "lune"]), ("J'entends [u] comme dans « soupe » :", ["poulet", "pain", "bus", "salade"]),
         ("🔁 J'ai mal ____ ventre.", ["à la", "au", "aux", "à l'"]), ("🔁 Police en Belgique :", ["112", "101", "18", "070"])]
    ans = ["le pain", "le poisson", "un fruit", "le dîner", "le souper", "J'adore", "du", "de l'", "des", "de", "Je n'aime pas le café.", "Moi non plus.", "plat végétarien", "une étape", "4", "poli", "poisson", "poulet", "au", "101"]
    key = key_from(Q, ans)
    test_pages(b, 6, "À table !", Q, f'<h3>B1. J\'écris ce que je mange au dîner (3 aliments avec du, de la, des). (… / 3)</h3>{lines(2, True)}<h3>B2. J\'écris mes goûts : 2 choses que j\'aime, 2 que je n\'aime pas. (… / 4)</h3>{lines(4, True)}<h3>B3. Je mets à la forme négative : « Je mange du poisson. » (… / 3)</h3>{lines(1, True)}',
               [["commander au restaurant (jeu de rôle)", "/ 4", ""], ["dire mes goûts et réagir (moi aussi / moi non plus)", "/ 3", ""], ["présenter un plat de mon pays", "/ 3", ""]],
               f'<h3>1. J\'écoute et j\'entoure. (… / 4)</h3><div class="grid4">{"".join(f"<div class=\'card c big\' style=\'font-weight:700;white-space:nowrap\'>{r}</div>" for r in ["ba bo bu", "bou ba bon", "lon lou la", "son sou sa"])}</div><h3>2. Je lis et je relie. (… / 4)</h3>{relie([f"<b class=big>{w}</b>" for w in ["soupe", "bonbon", "banane", "poulet"]], ["<span class=\'emo s\'>🍌</span>", "<span class=\'emo s\'>🍗</span>", "<span class=\'emo s\'>🥣</span>", "<span class=\'emo s\'>🍬</span>"])}<h3>3. Dictée. (… / 4)</h3>{guide_lines(1, 22)}<h3>4. Je nomme 4 aliments (oral). (… / 4)</h3><div class="grid4">{"".join(f"<div class=\'card c\' style=\'font-size:26pt\'>{x}</div>" for x in ["🍞", "🍎", "🧀", "💧"])}</div><h3>5. Je dis : « J\'aime… / Je n\'aime pas… » (oral). (… / 4)</h3><div class="card">☐ ☐ ☐ ☐</div>')
    closing(b, 6, ["Je sais nommer 20 aliments.", "Je connais les repas (déjeuner, dîner, souper).", "Je sais dire j'adore, j'aime, je n'aime pas, je déteste.", "Je sais répondre moi aussi / moi non plus.", "Je sais dire du, de la, des.", "Je sais faire une phrase négative.", "Je sais lire un menu.", "Je sais lire une recette.", "Je sais commander au restaurant.", "★ Je sais lire ba, bou, bon, soupe, bonbon…"],
            ALIM + [("🌅", "le déjeuner"), ("☀️", "le dîner"), ("🌙", "le souper"), ("😍", "adorer"), ("🤢", "détester"), ("🍽️", "le repas"), ("📋", "le menu"), ("👩‍🍳", "la recette")])
    plan_de_travail(b, E, 6, ["Les repas · exprimer ses goûts", "Du, de la, des", "La négation ne… pas", "Lire une recette"], "☐ Menu de la classe<br>☐ Présentation et vote")
    if render:
        to_pdf(b.html(), '/home/claude/syllabus/out/V1_M6_eleve.pdf')
    pg, exs = helpers(b, E)
    A = b.marks["★ Alpha"]
    days = [("1", "Collectif", f"Ouverture · BD ({pg('Découvrir')})", f"Alpha : b (p. {A[0]})"), ("2", "Collectif", f"Les aliments ({pg('Lexique')}) · 📌 Leçon 1 ({pg('Leçon 1')})", f"Alpha : ou (p. {A[1]})"),
            ("3", "Rotation", f"📌 Leçon 2 partitifs ({pg('Leçon 2')})", f"Alpha : on (p. {A[2]})"), ("4", "Rotation", f"📌 Leçon 3 négation ({pg('Leçon 3')})", f"Alpha : lecture (p. {A[3]})"),
            ("5", "Collectif", f"Menu du réfectoire ({pg('Document de la vie')})", "Alpha : révision"), ("6", "Atelier cuisine (si possible)", f"Recette des crêpes ({pg('Consignes & école')})", "Alpha : ingrédients en images"),
            ("7", "Rotation", f"Sons ({pg('Sons')}) · 🔁 révision", "Alpha : dictée"), ("8", "Ateliers", f"Ateliers ({pg('Atelier')})", "Alpha : loto"), ("9", "Groupes", f"Tâche finale ({pg('Tâche finale')})", "Alpha : menu en images"), ("10", "Seul", f"Test ({pg('Test')})", f"Alpha : test ({pg('★ Alpha · Test')})")]
    rot = [["🎧 Écouter-Parler", "Restaurant (jeu de rôle)", "20 min", "—"], ["📖 Lire", "Petit-déjeuner dans le monde", "20 min", "Oui"], ["✏️ Écrire", "Mon petit-déjeuner · recette de mon pays", "20 min", "● oui"], ["🧩 Jouer", "Loto des aliments", "20 min", "Entre joueurs"], ["👩‍🏫 Table d'appui", "Alpha : b, ou, on · autres : du/de la, négation", "20 min", "—"]]
    ev1 = '''<h3>Partie B (10 points)</h3><p class="sm"><b>B1</b> : 1 pt par aliment avec le bon partitif · <b>B2</b> : 1 pt par phrase (le/la/les après aimer) · <b>B3</b> : <span class="sol">Je ne mange pas de poisson.</span> (ne… pas 2 pts, « de » 1 pt).</p>
<h3>Partie C (10 points)</h3><p class="sm">Restaurant : saluer, commander avec « je voudrais », boisson, addition (4) · goûts + réaction (3) · plat de son pays (3).</p>
<h3>Test ★ Alpha</h3><p class="sm"><b>Ex. 1, dire :</b> <span class="sol">bo · bon · lou · son</span> · <b>Ex. 2 :</b> <span class="sol">soupe–🥣, bonbon–🍬, banane–🍌, poulet–🍗</span> · <b>Ex. 3, dicter :</b> <span class="sol">bou, bon, soupe, bonbon</span>.</p>'''
    ev2 = f'''<h2>Grille · tâche finale « Le menu de la classe »</h2>{table(["Critère", "Très bien", "Bien", "À retravailler", "Points"], [["<b>Contenu</b> : 4 jours complets, végétarien, plats du monde", "Complet", "Partiel", "Insuffisant", "/ 6"], ["<b>Langue</b> : partitifs, négation", "Correct", "Quelques erreurs", "Beaucoup", "/ 6"], ["<b>Présentation orale</b>", "Fluide", "Hésitante", "Bloquée", "/ 5"], ["<b>Collaboration</b>", "Excellente", "Correcte", "Faible", "/ 3"]], ["64mm", "32mm", "32mm", "32mm", "22mm"])}
<div class="attention mt4"><b>Respect :</b> les interdits alimentaires (religion, allergie, choix) se respectent sans jugement. Vérifier les allergies avant tout atelier cuisine ou dégustation.</div>
<h2 class="mt4">Différencier et remédier</h2>{table(["Difficulté", "Remédiation"], [["aimer le / manger du", "Affiche : « j'aime → LE (tout) / je mange → DU (un morceau) » avec un gâteau entier / une part."], ["pas de", "Jeu « menteur » : un élève dit ce qu'il ne mange pas, les autres vérifient la forme."], ["Élève rapide", "Écrire le livre de recettes de la classe ; comparer les prix de deux menus."]], ["50mm", "132mm"])}'''
    T = teacher_book(b, E, "V1 · M6", "", MC, 6, "À table !",
                     "<li><b>Communication :</b> parler des repas, exprimer ses goûts, commander, réagir.</li><li><b>Lexique :</b> 24 aliments, repas belges, ustensiles.</li><li><b>Grammaire :</b> partitifs du/de la/de l'/des, ne… pas (de), aimer + le/la/les.</li><li><b>Phonétique :</b> [b]/[p], [u], [ɔ̃].</li><li><b>FLSco :</b> lire une recette (structure, impératif, quantités).</li><li><b>★ Alpha :</b> b, ou, on.</li>",
                     '<p class="sm"><b style="color:#E4572E">Indispensable</b> : aliments de base, j\'aime / je n\'aime pas, repas.</p><p class="sm"><b style="color:#d9a400">Important</b> : partitifs, négation, menu.</p><p class="sm"><b style="color:#2BA88F">Enrichissement</b> : recette, calculs de prix.</p>',
                     "Menu réel du réfectoire · ingrédients des crêpes (atelier facultatif) · jetons.", "<b>Atelier cuisine :</b> si l'école le permet, réaliser la recette des crêpes (vérifier les allergies).",
                     days, "« Qu'est-ce que tu as mangé ce matin ? » · lecture du menu du jour · un mot d'aliment dans les langues de la classe.", rot, key, (ev1, ev2), start=tstart)
    if render:
        to_pdf(T.html(), '/home/claude/syllabus/out/V1_M6_prof.pdf')
    return b, T


if __name__ == "__main__":
    b, T = build_m6()
    print(b.n, T.n)
