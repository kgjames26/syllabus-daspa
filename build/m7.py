"""Volume 1 · Module 7 « Faire les courses »."""
import sys
sys.path.insert(0, '/home/claude/syllabus')
from lib.base import *
from lib.art import *
from lib.alpha import AL, letter_page, syll_table
from lib.module import *
from lib.render import to_pdf

MC = "#2E8B57"
MAG = [("🥖", "la boulangerie", "le pain, les croissants"), ("🥩", "la boucherie", "la viande"), ("🍎", "le marché", "les fruits et légumes"), ("🛒", "le supermarché", "un peu de tout"),
       ("💊", "la pharmacie", "les médicaments"), ("👕", "le magasin de vêtements", "les habits"), ("📰", "la librairie", "les journaux, les cahiers"), ("🍬", "l'épicerie (le night shop)", "les petites courses")]


def euro(v):
    return f"{v:.2f} €".replace(".", ",")


def build_m7(start=1, tstart=1, render=True):
    b = Book("V1 · M7", "Volume 1 · Premiers pas · Module 7 · Faire les courses", MC, start=start)
    E = Ex(b)
    vis = '<div class="c" style="font-size:40pt;line-height:1.3">🛒🥖🍎💶<br>🧾🏪💳🛍️</div>'
    opening(b, MC, 7, "Faire les courses", vis, [("🏪", "nommer les magasins"), ("💶", "compter l'argent en euros"), ("🔢", "compter jusqu'à 1000"), ("❓", "demander un prix : Combien ça coûte ?"),
            ("🙋", "dire je voudrais, je veux, je peux"), ("🧾", "lire un ticket de caisse et une publicité")],
            ["Où est-ce que tu fais les courses ?", "Dans ton pays, il y a des marchés ? On discute le prix ?", "Combien coûte un pain en Belgique ?"],
            ["le magasin", "le prix", "l'euro", "le centime", "combien ?", "je voudrais", "un kilo", "une bouteille", "le ticket", "la caisse"], "#E6F4EC")
    bd = '<div class="grid2" style="gap:3mm">' + "".join([
        bd_case(1, lr("amina", ["Samedi, je vais au marché avec ma mère."], "fatou", ["Je viens avec vous ? J'adore le marché !"], "sourire", "rire")),
        bd_case(2, lr("amina", ["Bonjour Monsieur ! Je voudrais un kilo de tomates, s'il vous plaît."], extra='<div class="c" style="font-size:26pt">🍅🍅🍅⚖️</div>')),
        bd_case(3, f'<div class="flex top" style="margin-top:5mm">{face(size=72, skin="clair", hair="#888", style="chauve", beard=True, shirt="#2E8B57")}<div>{bub("Voilà ! Et avec ça ?")}</div></div><div class="flex top" style="justify-content:flex-end">{bub("Des pommes. Combien coûtent les pommes ?")}{avatar("fatou", 70, flip=True)}</div>'),
        bd_case(4, f'<div class="flex top" style="margin-top:5mm">{face(size=72, skin="clair", hair="#888", style="chauve", beard=True, shirt="#2E8B57")}<div>{bub("2,50 € le kilo.")}</div></div><div class="flex top" style="justify-content:flex-end">{bub("Un kilo de pommes, s&#39;il vous plaît.")}{avatar("amina", 70, flip=True)}</div>'),
        bd_case(5, f'<div class="flex top" style="margin-top:5mm">{face(size=72, skin="clair", hair="#888", style="chauve", beard=True, shirt="#2E8B57")}<div>{bub("Ça fait 5,30 € en tout.")}</div></div><div class="flex top" style="justify-content:flex-end">{bub("Voici 10 euros.")}{avatar("amina", 70, flip=True)}</div>'),
        bd_case(6, f'<div class="flex top" style="margin-top:5mm">{face(size=72, skin="clair", hair="#888", style="chauve", beard=True, shirt="#2E8B57")}<div>{bub("Et voilà 4,70 € de monnaie. Merci, bonne journée !")}</div></div><div class="flex top" style="justify-content:flex-end">{bub("Merci, au revoir !")}{avatar("fatou", 70, "rire", flip=True)}</div>'),
    ]) + '</div>'
    e = E("J'écoute et je regarde la BD : au marché.", bd, ["ecoute", "regarde"], 1, "A", script="Lire deux fois. Faire répéter : « Je voudrais… », « Combien coûtent… ? », « Ça fait combien ? ». Montrer de vraies pièces et billets (ou les modèles à découper).", sol="Activité orale.")
    b.page(f'<h2>Découvrir · Au marché</h2>{e}', "Découvrir")
    e = E("Je réponds.", f'<p>1. Amina achète quoi ? {blank("xl")}</p><p>2. Les pommes coûtent combien le kilo ? {blank()}</p><p>3. Ça fait combien en tout ? {blank()}</p><p>4. Amina donne combien ? {blank()} Le marchand rend combien ? {blank()}</p>',
          ["lis", "ecris"], 1, "B", sol="1. un kilo de tomates et un kilo de pommes — 2. 2,50 € — 3. 5,30 € — 4. 10 € ; 4,70 €")
    e2 = E("Défi ! Les tomates coûtent combien le kilo ? Je calcule.", f'<p>5,30 € − 2,50 € = {blank()}</p>', ["ecris"], 3, "C", sol="2,80 €")
    b.page(f'{e}{e2}', "Découvrir")

    e = E("Les magasins. J'écoute et je répète.", '<div class="grid4">' + "".join(f'<div class="card c"><span class="emo">{e}</span><div class="word" style="font-size:10pt">{w}</div><div class="xs muted">{d}</div></div>' for e, w, d in MAG) + '</div>', ["ecoute", "repete"], 1, "A", script="Présenter chaque magasin : « À la boulangerie, j'achète du pain. »", sol="Activité orale.")
    e2 = E("Où est-ce que j'achète… ? Je relie.", relie(["des croissants", "un steak", "un sirop", "un t-shirt", "un cahier", "des bananes"], ["à la pharmacie", "au marché", "à la boulangerie", "à la librairie", "à la boucherie", "au magasin de vêtements"]), ["relie"], 1, "B",
           sol="croissants → boulangerie · steak → boucherie · sirop → pharmacie · t-shirt → vêtements · cahier → librairie · bananes → marché")
    b.page(f'<h2>Les magasins</h2>{e}{e2}', "Lexique")

    l1 = lecon("Les nombres de 70 à 1000", f'''{table(["", "Belgique 🇧🇪", "France 🇫🇷"], [["70", "<b>septante</b>", "soixante-dix"], ["80", "<b>quatre-vingts</b>", "quatre-vingts"], ["90", "<b>nonante</b>", "quatre-vingt-dix"]], ["30mm", "76mm", "76mm"])}
<p class="mt2">71 septante et un · 75 septante-cinq · 81 quatre-vingt-un · 92 nonante-deux · 99 nonante-neuf</p>
<p>100 <b>cent</b> · 101 cent un · 150 cent cinquante · 200 <b>deux cents</b> · 250 deux cent cinquante · 500 cinq cents · 1000 <b>mille</b></p>
<div class="astuce" style="margin-bottom:0">En Belgique, on dit <b>septante</b> et <b>nonante</b> : c'est plus facile ! Tu entendras aussi soixante-dix et quatre-vingt-dix (France, télé). Les deux sont justes.</div>''')
    e = E("J'écoute et j'écris le nombre.", '<div class="grid5">' + "".join(f'<div class="card c"><b>{chr(97+i)}.</b><div class="line"></div></div>' for i in range(10)) + '</div>', ["ecoute", "ecris"], 2, "A",
          script="a. 70 — b. 85 — c. 93 — d. 100 — e. 77 — f. 150 — g. 300 — h. 99 — i. 1000 — j. 81", sol="70 · 85 · 93 · 100 · 77 · 150 · 300 · 99 · 1000 · 81")
    e2 = E("J'écris en lettres (à la belge).", '<div class="grid3">' + "".join(f'<p><b>{n}</b> → {blank("l")}</p>' for n in [72, 80, 91, 100, 200, 500]) + '</div>', ["ecris"], 2, "C", sol="septante-deux · quatre-vingts · nonante et un · cent · deux cents · cinq cents")
    b.page(f'{l1}{e}{e2}', "Leçon 1")

    coins = [("1 c", "#C87533"), ("2 c", "#C87533"), ("5 c", "#C87533"), ("10 c", "#D4AF37"), ("20 c", "#D4AF37"), ("50 c", "#D4AF37"), ("1 €", "#C0C0C0"), ("2 €", "#D4AF37")]
    cs = "".join(f'<div class="c"><svg viewBox="0 0 40 40" width="16mm"><circle cx="20" cy="20" r="18" fill="{c}" stroke="#555" stroke-width="1.2"/><circle cx="20" cy="20" r="13" fill="none" stroke="#fff" stroke-width=".6" opacity=".6"/><text x="20" y="24" font-size="10" text-anchor="middle" font-family="Poppins" font-weight="800" fill="#1F2A44">{t}</text></svg></div>' for t, c in coins)
    notes = [("5 €", "#B0B0B0"), ("10 €", "#E57373"), ("20 €", "#64B5F6"), ("50 €", "#FFB74D"), ("100 €", "#81C784")]
    ns = "".join(f'<div style="background:{c};border:1.5px solid #555;border-radius:2mm;width:30mm;height:16mm;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:14pt">{t}</div>' for t, c in notes)
    l2 = lecon("L'argent : les euros", f'''<p><b>Les pièces</b> (dessins simplifiés)</p><div class="flex" style="justify-content:space-around">{cs}</div><p class="mt2"><b>Les billets</b></p><div class="flex" style="justify-content:space-around">{ns}</div>
<p class="mt2">1 euro = 100 centimes · <b>3,50 €</b> se dit « trois euros cinquante » · 0,80 € = « quatre-vingts centimes »</p><p><b>Combien ça coûte ?</b> / <b>C'est combien ?</b> → Ça coûte 2 €. · <b>Ça fait combien ?</b> → Ça fait 7,40 €.</p>''')
    e = E("Je compte l'argent. J'écris le total.", '<div class="grid3">' + "".join(f'<div class="card c">{t}<p>= {blank()}</p></div>' for t in ["10 € + 5 € + 2 €", "20 € + 1 € + 50 c", "2 € + 2 € + 20 c + 10 c", "50 € + 20 € + 5 €", "1 € + 50 c + 50 c", "100 € + 50 € + 10 €"]) + '</div>', ["ecris"], 1, "C",
          sol="17 € · 21,50 € · 4,30 € · 75 € · 2 € · 160 €")
    b.page(f'{l2}{e}', "Leçon 2")
    e = E("Je rends la monnaie.", table(["Je paie", "Je donne", "On me rend"], [["3,50 €", "5 €", ""], ["7,20 €", "10 €", ""], ["12 €", "20 €", ""], ["16,40 €", "20 €", ""]], ["60mm", "60mm", "62mm"]), ["ecris"], 2, "C", sol="1,50 € · 2,80 € · 8 € · 3,60 €")
    e2 = E("J'écoute les prix et je les écris.", '<div class="grid4">' + "".join(f'<div class="card c"><span class="emo s">{em}</span><div class="line"></div></div>' for em in ["🥖", "🥛", "🍫", "🧀", "🍌", "🧃", "🥚", "🍕"]) + '</div>', ["ecoute", "ecris"], 2, "A",
           script="Le pain coûte 2,40 €. Le lait coûte 1,15 €. Le chocolat coûte 1,99 €. Le fromage coûte 4,50 €. Les bananes coûtent 1,80 € le kilo. Le jus coûte 2,25 €. Les œufs coûtent 3,10 €. La pizza coûte 5,90 €.",
           sol="2,40 · 1,15 · 1,99 · 4,50 · 1,80 · 2,25 · 3,10 · 5,90 €")
    e3 = E("Défi ! J'ai 10 €. Qu'est-ce que je peux acheter avec les prix de l'exercice précédent ? J'écris 2 possibilités.", lines(2), ["ecris"], 3, "C", sol="Exemple : pain + fromage + jus = 9,15 € · pizza + chocolat + lait = 9,04 €")
    b.page(f'{e}{e2}{e3}', "S'entraîner")

    l3 = lecon("Vouloir · pouvoir · Je voudrais (poli)", f'''<div class="grid3"><div class="card" style="background:#fff"><b>VOULOIR</b><p>je veux<br>tu veux<br>il / elle veut<br>nous voulons<br>vous voulez<br>ils / elles veulent</p></div>
<div class="card" style="background:#fff"><b>POUVOIR</b><p>je peux<br>tu peux<br>il / elle peut<br>nous pouvons<br>vous pouvez<br>ils / elles peuvent</p></div><div class="card" style="background:#fff"><b>Poli 🙏</b><p>Je <b>voudrais</b> un pain.<br>Je <b>peux</b> payer par carte ?<br>Vous <b>pouvez</b> m'aider ?</p><p class="sm muted">« Je veux » est direct ; au magasin, on dit « je voudrais ».</p></div></div>
<p class="mt2"><b>Les quantités :</b> un kilo <b>de</b> pommes · 500 grammes <b>de</b> fromage · une bouteille <b>d'</b>eau · un paquet <b>de</b> pâtes · une boîte <b>de</b> thon · un litre <b>de</b> lait · beaucoup <b>de</b> · un peu <b>de</b></p>''')
    e = E("Je conjugue vouloir et pouvoir.", '<p>1. Tu ______ (vouloir) un café ? 2. Nous ______ (pouvoir) payer. 3. Ils ______ (vouloir) des frites. 4. Je ______ (pouvoir) entrer ? 5. Vous ______ (vouloir) un sac ? 6. Elle ______ (pouvoir) venir.</p>', ["complete"], 2, "C",
          sol="veux · pouvons · veulent · peux · voulez · peut")
    b.page(f'{l3}{e}', "Leçon 3")
    e = E("Je relie la quantité et le produit.", relie(["une bouteille", "un kilo", "un paquet", "une boîte", "un litre", "une tranche"], ["de pâtes", "de jambon", "d'eau", "de lait", "de pommes de terre", "de thon"]), ["relie"], 1, "B",
          sol="bouteille → d'eau · kilo → de pommes de terre · paquet → de pâtes · boîte → de thon · litre → de lait · tranche → de jambon")
    e2 = E("Je transforme en phrase polie avec « je voudrais ».", '<p>1. Donnez-moi un pain ! → ______________________</p><p>2. Je veux deux croissants. → ______________________</p>', ["ecris"], 2, "C", sol="Je voudrais un pain, s'il vous plaît. · Je voudrais deux croissants, s'il vous plaît.")
    e3 = E("Jeu de rôle à la boulangerie : je commande et je paie.", '<div class="card"><p>Prix : 🥖 baguette 1,40 € · 🥐 croissant 1,10 € · 🍞 pain gris 2,90 € · 🍩 couque 1,60 €</p></div>', ["parle", "duo"], 2, "A", sol="Bonjour, je voudrais… Ça fait combien ? Voici… Merci, au revoir ! (en Belgique, « une couque » = viennoiserie)")
    b.page(f'{e}{e2}{e3}', "S'entraîner")

    pub = f'''<div class="doc" style="transform:none;padding:3mm;background:#FFFDE7;border:3px solid #E53935"><div class="c" style="font-size:20pt;font-weight:800;color:#E53935">SUPER MARCHÉ « LE PANIER » · PROMOS DE LA SEMAINE</div><div class="c sm">du mercredi 14 au mardi 20 octobre · magasin fictif</div>
<div class="grid4 mt2">{"".join(f'<div class="card c"><span class="emo">{e}</span><b class="sm">{n}</b><div style="color:#E53935;font-weight:800;font-size:14pt">{p}</div><div class="xs muted">{o}</div></div>' for e, n, p, o in [("🍌", "Bananes 1 kg", "1,49 €", "au lieu de 1,99 €"), ("🥛", "Lait 1 L", "0,99 €", ""), ("🍝", "Pâtes 500 g", "2 pour 1,80 €", ""), ("🍗", "Poulet 1 kg", "6,90 €", "-20 %"), ("🧃", "Jus d'orange 1 L", "1,79 €", ""), ("🍫", "Chocolat", "1+1 gratuit", "2,20 € le paquet"), ("🧻", "Papier toilette x6", "3,49 €", ""), ("🍞", "Pain de mie", "1,29 €", "")])}</div></div>'''
    e = E("Je lis la publicité. Je réponds.", f'<p>1. La promo commence quel jour ? {blank()} 2. Combien coûtent les bananes ? {blank()} Avant ? {blank()}</p><p>3. 4 paquets de pâtes coûtent combien ? {blank()} 4. « 1+1 gratuit » : 2 chocolats coûtent {blank()}.</p>',
          ["lis", "ecris"], 2, "B", sol="1. mercredi 14 octobre — 2. 1,49 € ; 1,99 € — 3. 3,60 € — 4. 2,20 €")
    b.page(f'<span class="tag-doc">📄 DOCUMENT DE LA VIE</span><h2>La publicité du supermarché</h2>{pub}<div class="mt4">{e}</div>', "Document de la vie")
    tk = '''<div class="doc" style="transform:rotate(1deg);width:80mm;margin:auto;padding:4mm;font-family:'DejaVu Sans Mono';font-size:9pt;background:#fff;border:1px solid #ccc"><div class="c"><b>LE PANIER</b><br>Rue du Pont 3 · Namur</div>----------------------------<br>
Bananes 1 kg ............ 1,49<br>Lait 1 L x2 ............. 1,98<br>Pâtes 500 g x2 .......... 1,80<br>Poulet 1 kg ............. 6,90<br>Pain de mie ............. 1,29<br>----------------------------<br><b>TOTAL ................. 13,46</b><br>Espèces ................ 20,00<br>Rendu ................... 6,54<br>----------------------------<br>15/10/2026 · 17:42 · Caisse 3<div class="c">Merci de votre visite !</div></div>'''
    e = E("Je lis le ticket de caisse. Je réponds.", f'<p>1. Combien de litres de lait ? {blank("s")} 2. Le total : {blank()} 3. Le client paie comment ? {blank()} 4. On lui rend : {blank()} 5. Date et heure : {blank("l")}</p>', ["lis", "ecris"], 2, "B",
          sol="1. 2 — 2. 13,46 € — 3. en espèces (billet de 20 €) — 4. 6,54 € — 5. le 15/10/2026 à 17 h 42")
    e2 = E("Défi ! Je vérifie le calcul du ticket. Il est juste ?", f'<p>{blank("xl")}</p>', ["ecris"], 3, "C", sol="1,49 + 1,98 + 1,80 + 6,90 + 1,29 = 13,46 € ✔ ; 20 − 13,46 = 6,54 € ✔")
    b.page(f'<span class="tag-doc">📄 DOCUMENT DE LA VIE</span><h2>Le ticket de caisse</h2>{tk}<div class="mt4">{e}{e2}</div>', "Document de la vie")

    l4 = lecon("Résoudre un petit problème (méthode)", '<p>1️⃣ Je lis 2 fois. 2️⃣ Je souligne la <b>question</b>. 3️⃣ J\'entoure les <b>nombres utiles</b>. 4️⃣ Je choisis l\'opération : + (en tout, ensemble) · − (il reste, la différence, la monnaie) · × (chaque, fois) · ÷ (partager). 5️⃣ Je calcule. 6️⃣ J\'écris une <b>phrase réponse</b>.</p>')
    probs = ["Bilal achète 3 croissants à 1,10 € chacun. Combien il paie ?", "Daria a 15 €. Elle achète un livre à 8,50 €. Combien il lui reste ?", "Un paquet de 6 bouteilles coûte 4,20 €. Combien coûte une bouteille ?", "Fatou achète du pain (2,40 €) et du fromage (4,50 €). Elle donne 10 €. Combien on lui rend ?"]
    e = E("Je résous les problèmes avec la méthode.", "".join(f'<div class="card mb2"><p class="sm"><b>{i}.</b> {p}</p><p>Opération : {blank("l")} Réponse : {blank("xl")}</p></div>' for i, p in enumerate(probs, 1)), ["lis", "souligne", "ecris"], 2, "C",
          sol="1. 3 × 1,10 = 3,30 € — 2. 15 − 8,50 = 6,50 € — 3. 4,20 ÷ 6 = 0,70 € — 4. 2,40 + 4,50 = 6,90 ; 10 − 6,90 = 3,10 €")
    b.page(f'<span class="tag-doc">🎒 FRANÇAIS DE L\'ÉCOLE</span>{l4}{e}', "Consignes & école")

    e = E("[ɑ̃] an/en, [ɛ̃] in, [wa] oi. J'écoute et je répète.", '<div class="grid3"><div class="card c"><div class="huge">[ɑ̃]</div><p>an · en · am · em<br>argent · banane · cent · enfant</p></div><div class="card c"><div class="huge">[ɛ̃]</div><p>in · ain · ein · un<br>pain · vingt · magasin · lundi</p></div><div class="card c"><div class="huge">[wa]</div><p>oi<br>poisson · trois · soixante · boîte</p></div></div>', ["ecoute", "repete"], 1, "A",
          script="Paires : vent / vin, sans / cinq, banc / bain. Faire sentir l'air du nez.", sol="Activité orale.")
    e2 = E("J'écoute : [ɑ̃] ou [ɛ̃] ?", checks(8, ["[ɑ̃]", "[ɛ̃]"]), ["ecoute", "coche"], 2, "A", script="1. pain — 2. cent — 3. vingt — 4. argent — 5. magasin — 6. banane — 7. lundi — 8. enfant", sol="1. ɛ̃ — 2. ɑ̃ — 3. ɛ̃ — 4. ɑ̃ — 5. ɛ̃ — 6. ɑ̃ — 7. ɛ̃ — 8. ɑ̃")
    b.page(f'<h2>J\'écoute bien</h2>{e}{e2}', "Sons")
    e = E("🔁 Module 6 · Du, de la, des.", '<p>J\'achète ___ pain, ___ viande et ___ pommes.</p>', ["complete"], 1, "C", sol="du · de la · des")
    e2 = E("🔁 Module 6 · Négation.", '<p>J\'ai de l\'argent. → ______________________</p>', ["ecris"], 2, "C", sol="Je n'ai pas d'argent.")
    e3 = E("🔁 Module 5 · Où je vais ? J'ai besoin d'un médicament → ______", '', ["ecris"], 1, "C", sol="à la pharmacie")
    b.page(f'<h2>🔁 Je révise les modules 5 et 6</h2>{e}{e2}{e3}', "Je révise")

    e = E("Le marché de la classe : je découpe les étiquettes-prix. Un élève est vendeur, les autres achètent avec l'argent à découper.", '<div class="grid4">' + "".join(f'<div class="card c" style="border-style:dashed"><span class="emo s">{e}</span><b>{p}</b></div>' for e, p in [("🍎", "1,20 €"), ("🍌", "0,90 €"), ("🥖", "1,40 €"), ("🧀", "3,50 €"), ("🥛", "1,10 €"), ("🍫", "1,99 €"), ("🧃", "2,25 €"), ("🥚", "2,80 €")]) + '</div>' +
          '<div class="grid5 mt2">' + "".join(f'<div style="border:1.5px dashed #555;height:14mm;display:flex;align-items:center;justify-content:center;font-weight:800">{t}</div>' for t in ["5 €", "5 €", "10 €", "1 €", "1 €", "2 €", "50 c", "50 c", "20 c", "10 c"]) + '</div>', ["decoupe", "parle", "joue"], 2, "D",
          sol="Jeu de rôle : je voudrais…, ça fait…, voici…, je vous rends…")
    b.page(f'{atl_head("D", "Atelier · Jouer au marché")}{e}', "Atelier")
    e = E("J'écris ma liste de courses pour la semaine (8 produits avec la quantité).", lines(8), ["ecris"], 1, "C", sol="Ex. : un kilo de pommes, deux litres de lait…")
    e2 = E("Je lis le message et je réponds à la question.", '<div class="card">📱 <b>Maman :</b> « Yonas, tu peux passer au magasin ? Il faut un pain, un litre de lait et 6 œufs. Voici 10 €. Garde la monnaie pour toi ! 😉 »</div><p>Avec les prix de la publicité (lait 0,99 €, pain de mie 1,29 €) et des œufs à 2,80 €, Yonas garde combien ? ' + blank() + '</p>', ["lis", "ecris"], 3, "B", sol="0,99 + 1,29 + 2,80 = 5,08 € ; 10 − 5,08 = 4,92 €")
    b.page(f'{atl_head("C", "Atelier · Lire et écrire")}{e}{e2}', "Atelier")

    letter_page(b, E, "an", "[ɑ̃]", [("🍌", "banane"), ("🧒", "enfant"), ("👩", "maman"), ("💶", "argent")], "anoanuao", [("🍌", "banane", 1), ("🧒", "enfant", 1), ("🍞", "pain", 0), ("👩", "maman", 1), ("🐟", "poisson", 0), ("🐘", "éléphant", 1), ("🦁", "lion", 0), ("🥭", "mangue", 1)], MC)
    letter_page(b, E, "in", "[ɛ̃]", [("🍞", "pain"), ("🐇", "lapin"), ("🏪", "magasin"), ("🍇", "raisin")], "ianinina", [("🍞", "pain", 1), ("🐇", "lapin", 1), ("🍌", "banane", 0), ("🏪", "magasin", 1), ("🍇", "raisin", 1), ("🐟", "poisson", 0), ("🛁", "bain", 1), ("👩", "maman", 0)], MC)
    letter_page(b, E, "oi", "[wa]", [("🐟", "poisson"), ("3️⃣", "trois"), ("👑", "roi"), ("⭐", "étoile")], "ooiaoiou", [("🐟", "poisson", 1), ("3️⃣", "trois", 1), ("🍞", "pain", 0), ("👑", "roi", 1), ("⭐", "étoile", 1), ("🍌", "banane", 0), ("🐈", "chat", 0), ("📦", "boîte", 1)], MC)
    e = E("Je lis les mots du magasin et les phrases.", '<div class="grid4">' + "".join(f'<div class="card c"><span class="emo s">{e}</span><div class="huge" style="font-size:16pt">{w}</div></div>' for e, w in [("🍞", "pain"), ("🍌", "ba·na·ne"), ("🏪", "ma·ga·sin"), ("💶", "ar·gent")]) + '</div>' +
          '<div class="grid2 mt2">' + "".join(f'<div class="card"><p class="big">{t}</p></div>' for t in ["Maman a du pain.", "Le lapin a une banane.", "Il y a trois poissons.", "Sami va au magasin."]) + '</div>', ["lis"], 2, "P", alpha=True, sol="Lecture.")
    e2 = E("Dictée.", guide_lines(2, 20), ["ecoute", "ecris"], 2, "P", alpha=True, script="Dicter : an — in — oi — pain — trois — banane", sol="an in oi pain trois banane")
    b.page(AL.format(t="Je lis et j'écris") + e + e2, "★ Alpha", color=MC)

    e = E("Avec mon groupe, je prépare les courses pour un pique-nique de classe (12 élèves). Budget : 30 €. J'utilise les prix de la publicité ou de vrais prospectus.", table(["Produit", "Quantité", "Prix unitaire", "Total"], [["", "", "", ""] for _ in range(7)] + [["", "", "<b>TOTAL</b>", ""]], ["60mm", "36mm", "40mm", "46mm"]).replace("<td></td>", '<td style="height:10mm"></td>'),
          ["ecris", "groupe"], 2, "C", sol="Évaluation avec la grille : total ≤ 30 €, quantités réalistes pour 12.")
    b.page(tache_head("Les courses du pique-nique", "Nous faisons la liste, nous calculons le budget, puis nous jouons les achats au « marché de la classe ».") + e +
           table(["Je vérifie :", "✅"], [[x, '<span class="chk"></span>'] for x in ["Assez de nourriture et de boissons pour 12.", "Le total est inférieur ou égal à 30 €.", "J'écris les quantités (un kilo de, une bouteille de…).", "Je sais acheter poliment (je voudrais…)."]], ["160mm", "22mm"]), "Tâche finale", levels=False)
    e = E("Je révise.", '<p>1. 75 en lettres (Belgique) : ________ 2. Je ______ (vouloir) un pain. 3. Une bouteille ___ eau. 4. 20 € − 13,50 € = ________</p>', ["ecris"], 2, "C", sol="septante-cinq · veux (voudrais) · d' · 6,50 €")
    e2 = E("Défi ! Je corrige les 3 erreurs.", '<div class="card big">Je veut un kilo des pommes. Ça coûte combien d\'euro ?</div>' + lines(1), ["barre", "ecris"], 3, "C", sol="Je veux (je voudrais) · un kilo de pommes · combien d'euros")
    b.page(f'<h2>🔁 Je révise tout le module</h2>{e}{e2}', "Je révise")

    Q = [("🥖 J'achète le pain à :", ["la boucherie", "la boulangerie", "la pharmacie", "la librairie"]), ("70 en Belgique :", ["septante", "soixante-dix-dix", "sept-dix", "nonante"]), ("90 en Belgique :", ["quatre-vingts", "nonante", "neuf-dix", "septante"]),
         ("80 :", ["huitante… ou quatre-vingts", "quatre-vingts", "octante-dix", "nonante"]), ("200 :", ["deux cent", "deux cents", "deux-cent", "deux mille"]), ("1 € = ____ centimes", ["10", "50", "100", "1000"]),
         ("3,50 € se dit :", ["trois euros cinquante", "trente-cinq euros", "trois cinquante centimes", "cinquante trois"]), ("Je paie 6,40 € avec 10 €. On me rend :", ["4,60 €", "3,60 €", "4,40 €", "16,40 €"]),
         ("Au magasin, poli :", ["Je veux un pain.", "Donne pain !", "Je voudrais un pain, s'il vous plaît.", "Un pain !"]), ("Nous ____ payer par carte ?", ["peux", "pouvons", "peuvent", "pouvez"]),
         ("Ils ____ des frites.", ["veut", "voulons", "veulent", "voulez"]), ("une bouteille ____ eau", ["de", "d'", "du", "des"]), ("un kilo ____ pommes", ["des", "du", "de", "d'"]),
         ("Sur la pub, « 1+1 gratuit » : je paie", ["1 produit et j'en ai 2", "2 produits", "rien", "3 produits"]), ("Sur un ticket, « Rendu » =", ["le prix", "la monnaie", "la date", "le magasin"]),
         ("3 croissants à 1,10 € =", ["3,30 €", "1,13 €", "4,10 €", "3,10 €"]), ("J'entends [ɛ̃] comme dans « pain » :", ["banane", "cent", "lapin", "argent"]), ("J'entends [wa] :", ["trois", "train", "tout", "tard"]),
         ("🔁 Je mange ____ soupe.", ["du", "de la", "des", "de l'"]), ("🔁 « Je n'ai pas ____ argent. »", ["de l'", "d'", "des", "du"])]
    Q[3] = (Q[3][0], ["quatre-vingt-dix", "quatre-vingts", "huit-dix", "nonante"])
    ans = ["la boulangerie", "septante", "nonante", "quatre-vingts", "deux cents", "100", "trois euros cinquante", "3,60 €", "Je voudrais un pain, s'il vous plaît.", "pouvons", "veulent", "d'", "de", "1 produit et j'en ai 2", "la monnaie", "3,30 €", "lapin", "trois", "de la", "d'"]
    key = key_from(Q, ans)
    test_pages(b, 7, "Faire les courses", Q, f'<h3>B1. J\'écris en lettres : 72 · 95 · 300. (… / 3)</h3>{lines(1, True)}<h3>B2. Je résous : « J\'achète 2 jus à 2,25 € et un pain à 1,40 €. Je donne 10 €. Combien on me rend ? » (… / 3)</h3>{lines(2, True)}<h3>B3. J\'écris ma liste de courses (4 produits avec quantité). (… / 4)</h3>{lines(2, True)}',
               [["acheter au marché / à la boulangerie (jeu de rôle)", "/ 5", ""], ["lire 5 prix", "/ 3", ""], ["rendre la monnaie avec de l'argent fictif", "/ 2", ""]],
               f'<h3>1. J\'écoute et j\'entoure. (… / 4)</h3><div class="grid4">{"".join(f"<div class=\'card c big\' style=\'font-weight:700\'>{r}</div>" for r in ["an in oi", "oi on an", "in an ou", "on oi in"])}</div><h3>2. Je lis et je relie. (… / 4)</h3>{relie([f"<b class=big>{w}</b>" for w in ["pain", "trois", "banane", "lapin"]], ["<span class=\'emo s\'>🍌</span>", "<span class=\'emo s\'>🐇</span>", "<span class=\'emo s\'>🍞</span>", "<span class=\'emo s\'>3️⃣</span>"])}<h3>3. Dictée. (… / 4)</h3>{guide_lines(1, 22)}<h3>4. Je compte l\'argent (oral, avec les pièces). (… / 4)</h3><div class="card">☐ 3 € ☐ 5 € ☐ 7,50 € ☐ 12 €</div><h3>5. J\'achète un pain (oral). (… / 4)</h3><div class="card">☐ bonjour ☐ je voudrais ☐ je paie ☐ merci</div>')
    closing(b, 7, ["Je sais nommer les magasins.", "Je sais compter jusqu'à 1000 (septante, nonante).", "Je connais les pièces et les billets.", "Je sais demander un prix.", "Je sais rendre la monnaie.", "Je sais dire je voudrais, je veux, je peux.", "Je sais dire les quantités.", "Je sais lire une publicité et un ticket.", "Je sais résoudre un petit problème.", "★ Je sais lire an, in, oi, pain, trois…"],
            [(e, w) for e, w, _ in MAG] + [("💶", "l'euro"), ("🪙", "la pièce"), ("💵", "le billet"), ("🏷️", "le prix"), ("🧾", "le ticket"), ("💳", "la carte"), ("🛒", "le caddie"), ("🛍️", "le sac"), ("⚖️", "un kilo"), ("🍾", "une bouteille"), ("📦", "un paquet"), ("🥫", "une boîte"), ("💯", "cent"), ("🔢", "mille"), ("🙋", "je voudrais"), ("💰", "la monnaie")])
    plan_de_travail(b, E, 7, ["Les nombres de 70 à 1000", "L'argent : les euros", "Vouloir · pouvoir · quantités", "Résoudre un petit problème"], "☐ Liste et budget du pique-nique<br>☐ Achats au marché de la classe")
    if render:
        to_pdf(b.html(), '/home/claude/syllabus/out/V1_M7_eleve.pdf')
    pg, exs = helpers(b, E)
    A = b.marks["★ Alpha"]
    days = [("1", "Collectif", f"Ouverture · BD ({pg('Découvrir')}) · magasins ({pg('Lexique')})", f"Alpha : an (p. {A[0]})"), ("2", "Collectif", f"📌 Leçon 1 nombres ({pg('Leçon 1')})", f"Alpha : in (p. {A[1]})"),
            ("3", "Rotation", f"📌 Leçon 2 euros ({pg('Leçon 2')})", f"Alpha : oi (p. {A[2]})"), ("4", "Rotation", f"📌 Leçon 3 vouloir, pouvoir ({pg('Leçon 3')})", f"Alpha : lecture (p. {A[3]})"),
            ("5", "Collectif", f"Publicité et ticket ({pg('Document de la vie')})", "Alpha : révision"), ("6", "Rotation", f"Problèmes ({pg('Consignes & école')}) · sons", "Alpha : pièces"),
            ("7", "Ateliers", f"Marché de la classe ({pg('Atelier')})", "Alpha : marché"), ("8", "Rotation", "🔁 Révision · liste de courses", "Alpha : dictée"), ("9", "Groupes", f"Tâche finale ({pg('Tâche finale')})", "Alpha : courses avec images"), ("10", "Seul", f"Test ({pg('Test')})", f"Alpha : test ({pg('★ Alpha · Test')})")]
    rot = [["🎧 Écouter-Parler", "Boulangerie (jeu de rôle)", "20 min", "—"], ["📖 Lire", "Message de maman + calcul", "20 min", "Oui"], ["✏️ Écrire", "Liste de courses", "20 min", "● oui"], ["🧩 Jouer", "Marché de la classe", "20 min", "Entre joueurs"], ["👩‍🏫 Table d'appui", "Alpha : an in oi · autres : monnaie, problèmes", "20 min", "—"]]
    ev1 = '''<h3>Partie B (10 points)</h3><p class="sm"><b>B1</b> : <span class="sol">septante-deux · nonante-cinq · trois cents</span> · <b>B2</b> : <span class="sol">2 × 2,25 + 1,40 = 5,90 € ; 10 − 5,90 = 4,10 €</span> (opérations 2, phrase 1) · <b>B3</b> : 1 pt par produit avec quantité + de.</p>
<h3>Test ★ Alpha</h3><p class="sm"><b>Ex. 1, dire :</b> <span class="sol">in · oi · an · on</span> · <b>Ex. 2 :</b> <span class="sol">pain–🍞, trois–3️⃣, banane–🍌, lapin–🐇</span> · <b>Ex. 3, dicter :</b> <span class="sol">an, oi, pain, trois</span>.</p>'''
    ev2 = f'''<h2>Grille · tâche finale « Les courses du pique-nique »</h2>{table(["Critère", "Très bien", "Bien", "À retravailler", "Points"], [["<b>Liste</b> réaliste pour 12", "Oui", "Partielle", "Non", "/ 4"], ["<b>Calculs</b> justes, budget respecté", "Justes", "1-2 erreurs", "Faux", "/ 6"], ["<b>Langue</b> : quantités, je voudrais", "Correct", "Quelques erreurs", "Beaucoup", "/ 5"], ["<b>Jeu de rôle</b> d'achat", "Fluide", "Hésitant", "Bloqué", "/ 5"]], ["64mm", "32mm", "32mm", "32mm", "22mm"])}
<h2 class="mt4">Différencier et remédier</h2>{table(["Difficulté", "Remédiation"], [["septante / nonante / quatre-vingts", "Bingo 70-100 ; affiche Belgique / France."], ["Rendre la monnaie", "Compter en avançant (6,40 → 7 → 10) avec les pièces à découper."], ["Problèmes", "Mots-clés (en tout, il reste, chaque) en couleur ; dessiner la situation."], ["Élève rapide", "Comparer deux prospectus réels ; calculer des pourcentages simples (-20 %)."]], ["50mm", "132mm"])}'''
    T = teacher_book(b, E, "V1 · M7", "", MC, 7, "Faire les courses",
                     "<li><b>Communication :</b> acheter, demander un prix, payer, compter la monnaie.</li><li><b>Lexique :</b> magasins, argent, quantités, emballages.</li><li><b>Grammaire :</b> vouloir, pouvoir, je voudrais, quantité + de.</li><li><b>Nombres :</b> 70-1000 (septante, nonante).</li><li><b>Phonétique :</b> [ɑ̃], [ɛ̃], [wa].</li><li><b>FLSco :</b> résoudre un problème (méthode en 6 étapes).</li><li><b>★ Alpha :</b> an/en, in/ain, oi.</li>",
                     '<p class="sm"><b style="color:#E4572E">Indispensable</b> : prix, euros, je voudrais, monnaie.</p><p class="sm"><b style="color:#d9a400">Important</b> : nombres 70-1000, quantités, ticket.</p><p class="sm"><b style="color:#2BA88F">Enrichissement</b> : problèmes à étapes, promotions.</p>',
                     "Pièces et billets fictifs (à découper) · prospectus réels de supermarchés · balance (facultatif).", "<b>Sortie possible :</b> visite d'un marché ou d'un supermarché proche avec une liste et un petit budget.",
                     days, "« Combien ça coûte ? » avec un objet du jour · calcul mental de monnaie · nombre du jour en lettres (septante…).", rot, key, (ev1, ev2), start=tstart)
    if render:
        to_pdf(T.html(), '/home/claude/syllabus/out/V1_M7_prof.pdf')
    return b, T


if __name__ == "__main__":
    b, T = build_m7()
    print(b.n, T.n)
