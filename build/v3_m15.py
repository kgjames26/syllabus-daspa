"""Volume 3 · Module 15 « Résumer, synthétiser » (B1 + français de scolarisation).

Repérer l'essentiel d'un texte, prendre des notes, reformuler, résumer, rédiger un compte rendu et une synthèse
de documents. Langue : la reformulation (synonymes, nominalisation, changement de construction) et les substituts
(pronoms, synonymes, termes génériques, reprises résomptives « ce phénomène »). FLSco : le résumé et le compte rendu.
Fil rouge : la classe prépare un dossier sur les abeilles après la visite du rucher pédagogique du parc de Hautrive
(apicultrice : Mme Renard, personnage fictif) ; Bilal et Fatou présentent la synthèse à la classe.
Visuels : entonnoir() (du texte au résumé), abeille() (SVG), pollinisation() (schéma), confrontation() (tableau
de synthèse de documents), notes() (fiche de prise de notes avec abréviations).
Faits réels vérifiés (novembre 2026) : Journée mondiale des abeilles (20 mai, ONU) ; environ 400 espèces d'abeilles
sauvages en Belgique ; une colonie d'abeilles mellifères ; part des cultures qui dépendent des pollinisateurs (FAO) ;
gestion sans pesticides des espaces publics en Wallonie (2019) ; fauchage tardif.
"""
import sys
sys.path.insert(0, '/home/claude/syllabus')
from lib.base import *
from lib.art import *
from lib.module import *
from lib.v3 import CP, CPCOL, EPR, disc_tag
from lib.render import to_pdf

import os
BUMP = int(os.environ.get("BUMP", "48"))
SCR = int(os.environ.get("SCR", "120"))
MC = "#B7791F"
TINT = "#FBF3E4"
S = disc_tag("sciences")


def chk3(items, w=128):
    return table(["", "😀", "🙂", "😕"], [[x, '<span class="chk"></span>', '<span class="chk"></span>', '<span class="chk"></span>'] for x in items], [f"{w}mm", "18mm", "18mm", "18mm"])


def tall(html, h):
    return html.replace("<td></td>", f'<td style="height:{h}mm"></td>')


def compact(html):
    return html.replace('class="t"', 'class="t compact"')


def card(t, lh=2):
    return f'<div class="card" style="line-height:{lh}">{t}</div>'


def texte(titre, paras, src="texte écrit pour le cahier", fs=9.5, num=True):
    p = "".join(f'<p style="margin:1.1mm 0">{f"<b class=xs style=color:{MC}>§{i}</b> " if num else ""}{t}</p>' for i, t in enumerate(paras, 1))
    return f'<div class="card" style="background:#fff;font-size:{fs}pt;line-height:1.44;padding:2.5mm 4mm"><b style="color:{MC}">{titre}</b> <span class="xs muted">({src})</span>{p}</div>'


def abeille(w=26):
    """Petite abeille stylisée (SVG original)."""
    return (f'<svg viewBox="0 0 60 44" width="{w}mm"><ellipse cx="20" cy="12" rx="10" ry="7" fill="#DCEBFA" stroke="#9aa1b1"/><ellipse cx="34" cy="10" rx="10" ry="7" fill="#DCEBFA" stroke="#9aa1b1"/>'
            '<ellipse cx="28" cy="26" rx="16" ry="11" fill="#F6C343" stroke="#1F2A44" stroke-width="1.2"/><path d="M22 16 v20 M30 15 v22 M38 17 v18" stroke="#1F2A44" stroke-width="3"/>'
            '<circle cx="46" cy="24" r="6" fill="#1F2A44"/><path d="M12 26 l-6 0" stroke="#1F2A44" stroke-width="2"/><path d="M48 18 q4 -8 8 -6 M46 18 q0 -9 4 -10" stroke="#1F2A44" fill="none"/></svg>')


def entonnoir():
    """Du texte au résumé : un entonnoir en quatre étapes."""
    st = [("📖", "Je lis tout le texte (deux fois)", 100), ("🖍️", "Je surligne l'idée principale de chaque paragraphe", 84), ("📝", "Je note les idées-clés avec mes mots", 68), ("✂️", "Je rédige le résumé (environ ¼ du texte)", 52)]
    out = ""
    for ic, t, w in st:
        out += f'<div style="width:{w}%;margin:0 auto 1.2mm;background:{MC};color:#fff;border-radius:2mm;padding:1.2mm 2mm;text-align:center;font-size:9pt;opacity:{.55 + (100 - w) / 110}"><b>{ic}</b> {t}</div>'
    return out


def pollinisation():
    """Schéma : la pollinisation par une abeille."""
    box = lambda t: f'<div class="card c sm" style="padding:1.4mm;background:#fff;border:2px solid {MC};flex:1">{t}</div>'
    arr = '<div style="align-self:center;color:#9aa1b1;font-weight:800">➜</div>'
    return ('<div style="display:flex;gap:1.2mm">' + box("🌼 1. L'abeille butine une fleur : elle boit le <b>nectar</b>.") + arr + box("🟡 2. Du <b>pollen</b> se colle à ses poils.") + arr
            + box("🌸 3. Sur une autre fleur de la même espèce, elle dépose du pollen.") + arr + box("🍎 4. La fleur est <b>fécondée</b> : elle devient un <b>fruit</b> avec des graines.") + '</div>')


def notes(vide=False):
    """Fiche de prise de notes : abréviations et symboles."""
    rows = [("→", "entraîne, a pour conséquence"), ("←", "vient de, est causé par"), ("+", "et, en plus"), ("≠", "différent de, contraire"), ("=", "égal, c'est-à-dire"), ("↗ / ↘", "augmente / diminue"),
            ("qqch / qqn", "quelque chose / quelqu'un"), ("ex.", "par exemple"), ("pb", "problème"), ("cf.", "voir, se reporter à"), ("env.", "environ"), ("Be / Wal.", "Belgique / Wallonie")]
    cell = "".join(f'<div class="card sm" style="padding:1mm 2mm;background:#fff"><b style="color:{MC}">{a}</b> {"…………" if vide else b}</div>' for a, b in rows)
    return f'<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:1.2mm">{cell}</div>'


def confrontation(rows, docs=("Doc. 1", "Doc. 2", "Doc. 3"), vide=False, h=9):
    """Tableau de confrontation pour une synthèse de documents."""
    body = [[q] + (["" for _ in docs] if vide else r) for q, r in rows]
    t = compact(table(["Question"] + list(docs), body, ["40mm"] + [f"{int(142 / len(docs))}mm"] * len(docs)))
    return tall(t, h) if vide else t


DOC1 = ["L'abeille mellifère, celle qui produit le miel, vit en colonie dans une ruche. Une colonie compte une seule reine, qui pond les œufs, quelques centaines de mâles et, en été, jusqu'à plusieurs dizaines de milliers d'ouvrières. Les ouvrières se partagent le travail : elles nettoient la ruche, nourrissent les larves, construisent les rayons de cire, gardent l'entrée et vont butiner.",
        "Pour fabriquer du miel, les butineuses récoltent le nectar des fleurs. Elles le transportent jusqu'à la ruche, où d'autres ouvrières le transforment et le déposent dans les alvéoles. L'eau s'évapore peu à peu ; le nectar devient alors du miel, que les abeilles consomment pendant l'hiver.",
        "En butinant, les abeilles rendent aussi un service essentiel à la nature : elles transportent le pollen d'une fleur à l'autre. Cette pollinisation permet aux plantes de produire des fruits et des graines. Selon l'Organisation des Nations unies pour l'alimentation et l'agriculture (FAO), environ trois quarts des principales cultures alimentaires du monde dépendent, au moins en partie, des pollinisateurs."]


def build_v3m15(start=1, tstart=1, render=True):
    b = Book("V3 · M15", "Volume 3 · Je réussis à l'école · Module 15 · Résumer, synthétiser", MC, start=start)
    E = Ex(b)
    P = {}
    vis = ('<div class="flex" style="justify-content:space-around;align-items:flex-end">' + avatar("bilal", 80, "pense") + abeille(30) + avatar("fatou", 80, "sourire")
           + '<div style="font-size:32pt">📚 ✂️ 📝</div>' + avatar("prof", 80, "sourire") + avatar("daria", 80, "rire") + '</div>')
    opening(b, MC, 15, "Résumer, synthétiser", vis, [("🔍", "repérer l'idée principale et les mots-clés"), ("📝", "prendre des notes rapidement"), ("🔄", "reformuler avec mes mots"),
            ("🔗", "utiliser les substituts pour éviter les répétitions"), ("✂️", "résumer un texte et rédiger un compte rendu"), ("🧩", "faire la synthèse de plusieurs documents")],
            ["Raconte en une phrase le dernier film que tu as vu.", "Comment fais-tu pour étudier une longue leçon ?", "Que sais-tu des abeilles ?"],
            ["résumer", "un résumé", "l'essentiel", "une idée principale", "un mot-clé", "prendre des notes", "reformuler", "un substitut", "un compte rendu", "une synthèse", "un document"], TINT)

    # ---------- Découvrir ----------
    P["bd"] = b.n + 1
    bd = '<div class="grid2" style="gap:3mm">' + "".join([
        bd_case(1, lr("prof", ["Hier, nous avons visité le rucher du parc. Bilal, peux-tu résumer la visite en quelques phrases ?"], "bilal", ["Euh… On est arrivés, on a mis une combinaison, après on a vu les abeilles, après Mme Renard a parlé, après…"], "sourire", "pense")),
        bd_case(2, lr("fatou", ["Bilal, tu racontes tout ! Un résumé, ce n'est pas ça."], "bilal", ["Alors c'est quoi ?"], "rire", "surpris")),
        bd_case(3, lr("prof", ["Résumer, c'est garder l'essentiel, avec tes propres mots, en peu de phrases. Il faut choisir ce qui est important."], "daria", ["Comme quand on raconte un film à un ami sans dire chaque scène !"], "sourire", "rire")),
        bd_case(4, lr("bilal", ["D'accord. Je recommence : nous avons découvert comment vivent les abeilles et pourquoi elles sont menacées."], "prof", ["Excellent ! Tu as dit l'essentiel en une phrase."], "pense", "rire")),
        bd_case(5, lr("prof", ["Pour notre dossier, vous lirez trois documents sur les abeilles. Ensuite, vous ferez une synthèse : vous rassemblerez les informations de tous les documents."], "fatou", ["Une synthèse, c'est un résumé de plusieurs textes à la fois ?"], "sourire", "pense")),
        bd_case(6, lr("educ", ["Exactement ! Et vous la présenterez à la classe de M. Martin pour la Journée mondiale des abeilles, le 20 mai."], "bilal", ["Alors cette fois, je ne dirai pas « après… après… après » !"], "sourire", "rire")),
    ]) + '</div>'
    e = E("J'écoute et je lis la BD : Bilal apprend à résumer.", bd, ["ecoute", "lis"], 1, "A",
          script="Lire deux fois en changeant de voix ; insister sur les « après » répétés de Bilal.", sol="Activité orale.")
    b.page(f'<h2>Découvrir · Raconter tout ou résumer ?</h2>{e}', "Découvrir")
    e = E("Je réponds par une phrase complète.", f'<p>1. Qu\'a fait la classe hier ? {blank("xl")}</p><p>2. Pourquoi le premier résumé de Bilal ne convient-il pas ? {blank("xl")}</p><p>3. Selon Mme Lambert, qu\'est-ce que résumer ? {blank("xl")}</p><p>4. Quelle est la différence entre un résumé et une synthèse ? {blank("xl")}</p><p>5. Quand et pour qui la classe présentera-t-elle sa synthèse ? {blank("xl")}</p>', ["lis", "ecris"], 1, "B",
          sol="1. Elle a visité le rucher du parc. — 2. Il raconte tout dans l'ordre (« après… après… ») au lieu de garder l'essentiel. — 3. Garder l'essentiel, avec ses propres mots, en peu de phrases. — 4. Un résumé reprend un seul texte ; une synthèse rassemble les informations de plusieurs documents. — 5. Le 20 mai (Journée mondiale des abeilles), pour la classe de M. Martin.")
    e2 = E("Vrai ou faux ? Je coche et je corrige les phrases fausses.", vf(["Un résumé doit raconter tous les détails.", "Dans un résumé, on utilise ses propres mots.", "Une synthèse rassemble plusieurs documents.", "Le deuxième résumé de Bilal est trop long."]), ["lis", "coche"], 1, "B",
           sol="Faux (seulement l'essentiel) · Vrai · Vrai · Faux (il tient en une phrase et il est excellent)")
    e3 = E("À toi ! Je résume en une phrase un film, une série ou un livre que j'aime (titre + personnage + problème + fin).", lines(2), ["ecris"], 2, "C",
           sol="Ex. : Dans « Le Roi Lion », un jeune lion, Simba, quitte son royaume après la mort de son père, puis il revient pour vaincre son oncle Scar et devenir roi.")
    e4 = E("En duo : je raconte ma journée d'hier à mon voisin en 30 secondes seulement. Il compte les « après » et les « et puis » !", '<div class="card sm" style="background:#fff">Pour éviter « après » : d\'abord · ensuite · puis · plus tard · enfin · finalement. Pour aller à l\'essentiel : je garde trois moments importants.</div>', ["parle", "duo"], 1, "A",
           sol="Activité orale ; le voisin note les connecteurs utilisés.")
    b.page(f'{e}{e2}{e3}{e4}', "Découvrir")
    e = E(S + " Je lis le texte documentaire sur l'abeille mellifère.", '<div class="flex" style="gap:3mm;align-items:center"><div style="flex:1">' + texte("La vie des abeilles (document 1)", DOC1) + '</div><div>' + abeille(24) + '</div></div>', ["lis"], 1, "B",
          sol="Lecture silencieuse puis à voix haute.")
    P["doc1"] = b.n + 1
    e2 = E("J'observe le schéma de la pollinisation et je l'explique à mon voisin avec « d'abord, ensuite, puis, enfin ».", pollinisation(), ["regarde", "parle", "duo"], 1, "A",
           sol="D'abord, l'abeille boit le nectar d'une fleur. Ensuite, du pollen se colle à ses poils. Puis elle dépose ce pollen sur une autre fleur. Enfin, la fleur fécondée devient un fruit.")
    e3 = E("Je trouve le titre de chaque paragraphe du document 1 (un groupe nominal).", f'<p>§ 1 : {blank("xl")}</p><p>§ 2 : {blank("xl")}</p><p>§ 3 : {blank("xl")}</p>', ["lis", "ecris"], 2, "C",
           sol="§ 1 : La vie en colonie (l'organisation de la ruche). § 2 : La fabrication du miel. § 3 : Le rôle des abeilles dans la pollinisation.")
    b.page(f'<h2>Découvrir · Un texte documentaire</h2>{e}{e2}{e3}', "Découvrir")

    # ---------- Lexique ----------
    e = E("Les mots pour résumer et synthétiser. Je lis l'encadré.", '<div class="grid2">' + "".join(f'<div class="card" style="background:#fff"><b>{t}</b><p class="sm" style="margin:1mm 0 0">{d}</p></div>' for t, d in [
        ("🔍 Repérer", "l'<b>essentiel</b> · le <b>thème</b> (de quoi on parle) · l'<b>idée principale</b> · une idée <b>secondaire</b> · un <b>détail</b> · un <b>exemple</b> · un <b>mot-clé</b> · <b>surligner</b> · <b>souligner</b> · <b>relever</b>"),
        ("🔄 Transformer", "<b>reformuler</b> (dire autrement) · <b>résumer</b> (dire en plus court) · <b>condenser</b> · <b>supprimer</b> · <b>regrouper</b> · <b>généraliser</b> · <b>paraphraser</b> (répéter presque mot à mot : à éviter !)"),
        ("📄 Les écrits", "un <b>résumé</b> · un <b>compte rendu</b> (d'une visite, d'une réunion, d'un livre) · une <b>synthèse</b> · une <b>fiche</b> de lecture · des <b>notes</b> · un <b>plan</b> · une <b>source</b> · un <b>document</b>"),
        ("🔗 Les mots de la synthèse", "<b>tous les documents</b> s'accordent sur… · <b>selon</b> le document 1… · <b>de même</b> · <b>en revanche</b> · <b>alors que</b> · <b>par ailleurs</b> · <b>en résumé</b> · <b>bref</b> · <b>en conclusion</b>")]) + '</div>', ["lis"], 1, "B", sol="Lecture de l'encadré.")
    e2 = E("Je complète avec : thème · idée principale · détail · mots-clés · source.", card("1. Le ______________ du document 1, ce sont les abeilles. 2. « La colonie a une seule reine » est l'______________ du § 1. 3. « Les ouvrières nettoient la ruche » est un ______________ . 4. « nectar », « pollen », « pollinisation » sont des ______________ . 5. La FAO est la ______________ d'une information chiffrée.", 1.85), ["complete"], 1, "C",
           sol="1. thème — 2. idée principale (accepter : la colonie est organisée) — 3. détail — 4. mots-clés — 5. source")
    e3 = E("Je relie le verbe et sa définition.", relie(["reformuler", "résumer", "synthétiser", "paraphraser"], ["dire la même chose avec d'autres mots", "rassembler les informations de plusieurs documents", "répéter le texte presque mot à mot", "dire l'essentiel en moins de mots"]), ["lis", "relie"], 1, "B",
           sol="reformuler → dire avec d'autres mots · résumer → l'essentiel en moins de mots · synthétiser → rassembler plusieurs documents · paraphraser → répéter presque mot à mot")
    e4 = E("Les mots génériques. J'écris un mot qui regroupe toute la liste (un « mot-chapeau »).", card("1. pommes, poires, cerises → des ______________ 2. abeilles, papillons, bourdons → des ______________ 3. reine, ouvrières, mâles → les membres de la ______________ 4. pesticides, maladies, perte des fleurs → les ______________ du déclin des abeilles"), ["complete"], 2, "C",
           sol="1. fruits — 2. insectes (pollinisateurs) — 3. colonie — 4. causes (menaces)")
    b.page(f'<h2>Les mots du résumé et de la synthèse</h2>{e}{e2}{e3}{e4}', "Lexique")
    e = E(S + " Les mots des abeilles. Je relie.", relie(["la ruche", "l'apiculteur, l'apicultrice", "butiner", "une alvéole", "le nectar", "un essaim"], ["un groupe d'abeilles qui quitte la ruche avec une reine", "la maison des abeilles", "le liquide sucré des fleurs", "aller de fleur en fleur pour récolter le nectar", "la personne qui élève les abeilles", "une petite case de cire à six côtés"]), ["lis", "relie"], 1, "B",
          sol="ruche → maison · apiculteur → personne qui élève · butiner → de fleur en fleur · alvéole → case de cire · nectar → liquide sucré · essaim → groupe qui quitte la ruche")
    e2 = E("Les familles de mots. Je complète.", tall(compact(table(["Verbe", "Nom", "Adjectif / autre"], [["polliniser", "la pollinisation", "un pollinisateur"], ["menacer", "", "menacé"], ["protéger", "", ""], ["disparaître", "", "—"], ["diminuer", "", "—"]], ["60mm", "61mm", "61mm"])), 6.5), ["complete"], 2, "C",
           sol="la menace · la protection, protégé (protecteur) · la disparition · la diminution")
    e3 = E("Je supprime les détails. Je barre ce qui n'est pas essentiel dans chaque phrase.", card("1. Hier matin, vers dix heures, sous un beau soleil, la classe a visité le rucher du parc de Hautrive. 2. Mme Renard, qui porte toujours un chapeau jaune, élève des abeilles depuis vingt ans. 3. Les abeilles, ces petits insectes rayés si travailleurs, sont menacées.", 1.9), ["lis", "barre"], 2, "C",
           sol="1. barrer : vers dix heures, sous un beau soleil (garder : la classe a visité le rucher) — 2. barrer : qui porte toujours un chapeau jaune — 3. barrer : ces petits insectes rayés si travailleurs")
    e4 = E("Défi ! Je réduis chaque phrase à l'essentiel en 6 mots maximum.", f'<p class="sm">1. Dans de nombreux jardins de Belgique, les propriétaires installent aujourd\'hui de petits abris en bois pour les insectes. → {blank("xl")}</p><p class="sm">2. À cause des produits chimiques utilisés dans les champs, beaucoup d\'abeilles meurent chaque année. → {blank("xl")}</p>', ["ecris"], 3, "C",
           sol="Ex. : 1. Les Belges installent des hôtels à insectes. — 2. Les pesticides tuent beaucoup d'abeilles.")
    b.page(f'<h2>Les mots des abeilles</h2>{e}{e2}{e3}{e4}', "Lexique")

    # ---------- Leçon 1 : repérer l'essentiel, prendre des notes ----------
    l1 = lecon("Repérer l'essentiel et prendre des notes", '<p class="sm" style="margin-bottom:1.5mm">Dans un texte documentaire, chaque <b>paragraphe</b> développe en général <b>une idée principale</b>, souvent annoncée dans la <b>première phrase</b>. Les autres phrases donnent des <b>explications</b>, des <b>exemples</b>, des <b>chiffres</b>, des <b>détails</b>.</p>' +
        compact(table(["Pour trouver l'essentiel, je cherche…", "Indices"], [["le <b>thème</b>", "le titre, les mots répétés, les illustrations"], ["l'<b>idée principale</b> de chaque paragraphe", "la première (ou la dernière) phrase ; je me demande : « Que veut dire l'auteur ici ? »"], ["les <b>mots-clés</b>", "les mots importants, souvent en gras, répétés ou techniques"], ["l'<b>organisation</b> du texte", "les connecteurs : d'abord, ensuite, en effet, mais, donc, enfin"]], ["62mm", "120mm"])) +
        '<p class="sm" style="margin:2mm 0 1mm"><b>Prendre des notes</b>, c\'est écrire vite seulement l\'essentiel : des <b>mots-clés</b> (pas de phrases complètes), des <b>abréviations</b> et des <b>symboles</b>, une présentation claire (tirets, flèches, retraits).</p>' + notes() +
        '<div class="astuce" style="margin:1.5mm 0 0">✏️ Exemple : « Les abeilles transportent le pollen d\'une fleur à l\'autre, ce qui permet aux plantes de produire des fruits. » → <b>abeilles : pollen fleur → fleur → fruits</b></div>')
    e = E(f"Je relis le document 1 (p. {P['doc1']}). Je souligne l'idée principale de chaque paragraphe, puis je la recopie.", f'<p class="sm">§ 1 : {blank("xl")}</p><p class="sm">§ 2 : {blank("xl")}</p><p class="sm">§ 3 : {blank("xl")}</p>', ["lis", "souligne", "ecris"], 2, "B",
          sol="§ 1 : « L'abeille mellifère […] vit en colonie dans une ruche. » § 2 : « Pour fabriquer du miel, les butineuses récoltent le nectar des fleurs. » (le nectar devient du miel) § 3 : « les abeilles […] transportent le pollen d'une fleur à l'autre » (la pollinisation)")
    b.page(f'{l1}{e}', "Leçon 1")
    e = E("Je prends des notes : je transforme chaque phrase avec des mots-clés, des abréviations et des symboles.", f'<p class="sm">1. Le nombre d\'abeilles sauvages diminue en Belgique à cause de la disparition des fleurs. → {blank("xl")}</p><p class="sm">2. L\'apicultrice récolte environ vingt kilos de miel par ruche et par an. → {blank("xl")}</p><p class="sm">3. Les pesticides sont différents des engrais : ils tuent les insectes. → {blank("xl")}</p>', ["ecris"], 2, "C",
          sol="Ex. : 1. abeilles sauvages ↘ Be ← disparition fleurs — 2. apicultrice : env. 20 kg miel / ruche / an — 3. pesticides ≠ engrais : tuent insectes")
    e2 = E("Je fais l'inverse : je rédige des phrases complètes à partir des notes.", f'<p class="sm">1. ouvrières → nettoient ruche + nourrissent larves → {blank("xl")}</p><p class="sm">2. hiver : abeilles mangent miel ≠ butinent → {blank("xl")}</p>', ["ecris"], 2, "C",
           sol="1. Les ouvrières nettoient la ruche et nourrissent les larves. — 2. En hiver, les abeilles mangent le miel ; elles ne butinent pas.")
    e3 = E("J'écoute la présentation de Mme Renard, l'apicultrice, et je prends des notes dans la fiche.", tall(compact(table(["Sujet", "Mes notes"], [["Nombre d'abeilles dans une ruche en été", ""], ["Vie d'une ouvrière (durée)", ""], ["Travail de la reine", ""], ["Récolte de miel", ""], ["Ennemis des abeilles", ""]], ["66mm", "116mm"])), 8), ["ecoute", "ecris"], 2, "A",
           script="« Bienvenue au rucher ! En été, une ruche compte jusqu'à 50 000 abeilles. Une ouvrière vit seulement cinq à six semaines en été : elle s'use au travail ! La reine, elle, peut vivre plusieurs années ; elle pond jusqu'à 2 000 œufs par jour au printemps. Ici, je récolte environ 20 kilos de miel par ruche et par an. Les ennemis des abeilles ? Le varroa, un petit parasite, le frelon asiatique… et les pesticides. »",
           sol="jusqu'à 50 000 abeilles · env. 5-6 semaines (été) · pond jusqu'à 2 000 œufs / jour (printemps) ; vit plusieurs années · env. 20 kg / ruche / an · varroa (parasite), frelon asiatique, pesticides")
    e4 = E("Défi ! Je résume ma fiche de notes en 2 phrases complètes.", lines(2), ["ecris"], 3, "C",
           sol="Ex. : Une ruche compte jusqu'à 50 000 abeilles en été : une reine qui pond jusqu'à 2 000 œufs par jour et des ouvrières qui vivent quelques semaines. Les abeilles sont menacées par le varroa, le frelon asiatique et les pesticides.")
    b.page(f'{e}{e2}{e3}{e4}', "S'entraîner")

    # ---------- Leçon 2 : reformuler ----------
    l2 = lecon("Reformuler : dire la même chose autrement", compact(table(["Procédé", "Texte de départ", "Reformulation"], [
        ["un <b>synonyme</b>", "Les abeilles sont <b>en danger</b>.", "Les abeilles sont <b>menacées</b>."],
        ["un <b>mot générique</b> (mot-chapeau)", "Les pesticides, les maladies et les parasites tuent les abeilles.", "<b>Plusieurs menaces</b> tuent les abeilles."],
        ["la <b>nominalisation</b> (module 8)", "Les abeilles <b>disparaissent</b>, c'est inquiétant.", "La <b>disparition</b> des abeilles est inquiétante."],
        ["changer la <b>construction</b> (actif / passif, cause / conséquence)", "Les pesticides tuent les abeilles.", "Les abeilles <b>sont tuées par</b> les pesticides. · Les abeilles meurent <b>à cause des</b> pesticides."],
        ["<b>regrouper</b> deux phrases", "Les abeilles butinent. Elles pollinisent les fleurs.", "<b>En butinant</b>, les abeilles pollinisent les fleurs."]], ["44mm", "68mm", "70mm"])) +
        '<div class="astuce" style="margin:2mm 0 0">🗣️ Pour annoncer une reformulation : <b>autrement dit</b> · <b>c\'est-à-dire</b> · <b>en d\'autres termes</b> · <b>cela signifie que</b>. ⚠️ Reformuler n\'est pas <b>paraphraser</b> : je ne recopie pas le texte en changeant un seul mot ; je ne change pas le <b>sens</b>.</div>')
    e = E("Je remplace le mot souligné par un synonyme : nombreuses · essentiel · récolter · diminuer · protéger.", card("1. Le rôle des abeilles est <u>très important</u>. → ______________ 2. Il faut <u>défendre</u> les pollinisateurs. → ______________ 3. Les espèces <u>en grand nombre</u> → les espèces ______________ 4. Le nombre d'abeilles continue à <u>baisser</u>. → ______________ 5. <u>Prendre</u> le miel → ______________ le miel"), ["complete"], 1, "C",
          sol="1. essentiel — 2. protéger — 3. nombreuses — 4. diminuer — 5. récolter")
    e2 = E("Nominalisation. Je transforme le verbe souligné en nom.", card("1. Les fleurs <u>disparaissent</u>. → La ______________ des fleurs. 2. Les abeilles <u>se reproduisent</u>. → La ______________ des abeilles. 3. On <u>protège</u> les insectes. → La ______________ des insectes. 4. Le miel <u>est produit</u>. → La ______________ du miel."), ["complete"], 1, "C",
           sol="1. disparition — 2. reproduction — 3. protection — 4. production")
    b.page(f'{l2}{e}{e2}', "Leçon 2")
    e = E("Reformulation ou paraphrase ? Je coche.", compact(table(["Texte : « Les abeilles sauvages ont besoin de fleurs variées pour se nourrir. »", "reformulation", "paraphrase"], [[x, '<span class="chk"></span>', '<span class="chk"></span>'] for x in ["1. Les abeilles sauvages ont besoin de fleurs différentes pour se nourrir.", "2. Pour s'alimenter, les abeilles sauvages doivent trouver une grande diversité de fleurs.", "3. La nourriture des abeilles sauvages dépend de la variété des fleurs."]], ["126mm", "28mm", "28mm"])), ["lis", "coche"], 2, "B",
          sol="1. paraphrase (un seul mot changé) · 2. reformulation · 3. reformulation (nominalisation)")
    e2 = E("Je reformule chaque phrase avec le procédé demandé.", f'<p class="sm">1. (passif) L\'apicultrice récolte le miel en septembre. → {blank("xl")}</p><p class="sm">2. (nominalisation) Les abeilles déclinent, ce qui inquiète les scientifiques. → {blank("xl")}</p><p class="sm">3. (regrouper avec un participe présent) Les abeilles volent de fleur en fleur. Elles transportent le pollen. → {blank("xl")}</p><p class="sm">4. (mot générique) Les tulipes, les roses et les marguerites attirent les abeilles. → {blank("xl")}</p>', ["ecris"], 2, "C",
           sol="1. Le miel est récolté par l'apicultrice en septembre. — 2. Le déclin des abeilles inquiète les scientifiques. — 3. Volant de fleur en fleur, les abeilles transportent le pollen. — 4. Les fleurs attirent les abeilles.")
    e3 = E("J'explique avec « autrement dit » ou « c'est-à-dire ».", f'<p class="sm">1. Les abeilles sont des pollinisateurs, {blank("l")}</p><p class="sm">2. Cette espèce est menacée d\'extinction, {blank("l")}</p>', ["ecris"], 2, "C",
           sol="Ex. : 1. … c'est-à-dire qu'elles transportent le pollen d'une fleur à l'autre. — 2. … autrement dit, elle risque de disparaître complètement.")
    e4 = E("Défi ! Je reformule tout le § 2 du document 1 en 2 phrases, sans recopier plus de trois mots à la suite.", lines(3), ["ecris"], 3, "C",
           sol="Ex. : Les abeilles rapportent à la ruche le liquide sucré qu'elles trouvent dans les fleurs. Ce liquide sèche dans les alvéoles et se change en miel, leur nourriture pour l'hiver.")
    b.page(f'{e}{e2}{e3}{e4}', "S'entraîner")

    # ---------- Leçon 3 : les substituts ----------
    l3 = lecon("Les substituts : reprendre sans répéter", '<p class="sm" style="margin-bottom:1.5mm">🔁 <b>Rappel du module 9</b> (le récit) : pour ne pas répéter un mot, on le remplace par un <b>substitut</b>. Dans un texte documentaire et dans un résumé, les substituts rendent le texte <b>clair</b> et <b>court</b>.</p>' +
        compact(table(["Substitut", "Exemples (l'abeille mellifère…)"], [
            ["un <b>pronom</b>", "<b>elle</b> · <b>la</b> · <b>lui</b> · <b>celle-ci</b> · <b>en</b> · <b>y</b> : Les fleurs ? Les abeilles <b>y</b> trouvent du nectar."],
            ["un <b>synonyme</b>", "l'abeille domestique · l'abeille à miel"],
            ["un <b>terme générique</b>", "cet <b>insecte</b> · ce <b>pollinisateur</b>"],
            ["une <b>périphrase</b> (une expression qui désigne)", "la <b>petite ouvrière de la ruche</b> · l'<b>infatigable butineuse</b>"],
            ["une <b>reprise résomptive</b> (résume toute une idée)", "Les abeilles disparaissent. <b>Ce phénomène</b> inquiète. · <b>Cette situation</b> · <b>Ce problème</b> · <b>Cela</b>"]], ["58mm", "124mm"])) +
        '<div class="astuce" style="margin:2mm 0 0">⚠️ Le substitut doit être <b>clair</b> : on doit savoir tout de suite de qui ou de quoi on parle. « Les abeilles butinent les fleurs. <b>Elles</b> sont jaunes. » → Qui est jaune ? Les abeilles ou les fleurs ? Mieux : « <b>Ces fleurs</b> sont jaunes. »</div>')
    e = E("J'entoure les substituts qui reprennent « les abeilles sauvages » et je les relie par une flèche au mot de départ.", card("Les abeilles sauvages sont moins connues que l'abeille à miel. Pourtant, ces insectes sont très nombreux : on en compte environ 400 espèces en Belgique. La plupart d'entre elles vivent seules. Ces pollinisatrices discrètes creusent souvent leur nid dans le sol.", 1.9), ["lis", "entoure"], 1, "B",
          sol="ces insectes · en (on en compte) · elles (d'entre elles) · ces pollinisatrices discrètes")
    e2 = E("Je remplace les mots répétés par un pronom ou un substitut varié.", '<div class="card" style="line-height:1.9">Mme Renard est apicultrice. <u>Mme Renard</u> a douze ruches. <u>Les douze ruches</u> se trouvent dans le parc. Mme Renard aime les abeilles et parle souvent <u>des abeilles</u> aux enfants.</div>' + lines(2), ["lis", "ecris"], 2, "C",
           sol="Ex. : Mme Renard est apicultrice. Elle a douze ruches, qui se trouvent dans le parc. Cette passionnée aime les abeilles et en parle souvent aux enfants.")
    b.page(f'{l3}{e}{e2}', "Leçon 3")
    e = E("Je choisis la reprise résomptive qui convient : ce phénomène · cette mesure · ce problème · cette découverte.", card("1. Les pesticides chimiques sont interdits dans les parcs. ______________ protège les insectes. 2. Le nombre d'abeilles diminue partout en Europe. ______________ inquiète les agriculteurs. 3. Des chercheurs ont trouvé une nouvelle espèce d'abeille. ______________ a surpris tout le monde. 4. Le frelon asiatique attaque les ruches. Les apiculteurs cherchent des solutions à ______________ ."), ["complete"], 2, "C",
          sol="1. Cette mesure — 2. Ce phénomène — 3. Cette découverte — 4. ce problème")
    e2 = E("Le pronom est-il clair ? Je corrige les phrases ambiguës.", f'<p class="sm">1. Les abeilles butinent les fleurs. Elles sont violettes. → {blank("xl")}</p><p class="sm">2. Fatou parle à Daria de sa ruche. → {blank("xl")}</p>', ["lis", "ecris"], 3, "C",
           sol="Ex. : 1. Les abeilles butinent les fleurs. Ces fleurs sont violettes. — 2. Fatou parle à Daria de la ruche de son oncle (de la ruche de Daria).")
    e3 = E("J'écoute le court texte sur le bourdon et je compte combien de fois on utilise un substitut. J'en écris trois.", lines(2), ["ecoute", "ecris"], 2, "A",
           script="« Le bourdon est plus gros et plus poilu que l'abeille. Cet insecte supporte bien le froid : on le voit butiner dès la fin de l'hiver. Ce pollinisateur est très utile aux agriculteurs, qui l'utilisent parfois dans les serres pour polliniser les tomates. »",
           sol="Quatre substituts : cet insecte, le (on le voit), ce pollinisateur, l' (qui l'utilisent).")
    e4 = E("Défi ! J'écris 4 phrases sur un animal de mon pays, sans jamais répéter son nom : j'utilise un pronom, un terme générique, une périphrase et une reprise résomptive.", lines(4), ["ecris"], 3, "C",
           sol="Ex. : Le chameau vit dans le désert. Cet animal peut rester plusieurs jours sans boire. Le « vaisseau du désert » transporte les marchandises depuis des siècles. Cette résistance étonne les scientifiques.")
    b.page(f'{e}{e2}{e3}{e4}', "S'entraîner")

    # ---------- Leçon 4 (FLSco) : le résumé et le compte rendu ----------
    P["resume"] = b.n + 1
    l4 = lecon("Le résumé et le compte rendu", '<div class="grid2" style="gap:3mm"><div><p class="sm" style="margin:0 0 1mm"><b style="color:' + MC + '">✂️ Le résumé d\'un texte</b></p>' + entonnoir() +
        '<p class="sm" style="margin:1.5mm 0 0"><b>Les règles d\'or</b> : environ <b>¼</b> (ou ⅓) de la longueur du texte · l\'<b>ordre</b> du texte est respecté · <b>mes mots</b> (pas de citation) · <b>pas d\'opinion</b> personnelle, pas de « je » · au <b>présent</b> · des <b>connecteurs</b> pour relier les idées · je supprime les exemples et les détails.</p></div>'
        '<div><p class="sm" style="margin:0 0 1mm"><b style="color:' + MC + '">🗒️ Le compte rendu</b></p><p class="sm" style="margin:0">Il rapporte ce qui s\'est passé ou ce qui a été dit (une <b>visite</b>, une <b>réunion</b>, un <b>exposé</b>, une <b>expérience</b>) pour quelqu\'un qui n\'était pas là.</p>' +
        compact(table(["Partie", "Contenu"], [["En-tête", "quoi ? quand ? où ? qui ? (date, lieu, participants)"], ["Corps", "les moments ou les sujets importants, dans l'ordre, au passé composé ou au présent"], ["Fin", "les décisions, ce qu'on retient, la suite"]], ["20mm", "68mm"])) +
        '<p class="sm" style="margin:1mm 0 0">Pour rapporter des paroles : Mme Renard <b>explique</b> que… · <b>précise</b> que… · <b>rappelle</b> que… · <b>souligne</b> que… · <b>conseille</b> de… · <b>propose</b> que… (+ subj.)</p></div></div>' +
        '<div class="card sm mt2" style="background:' + TINT + '"><b>Exemple de résumé du document 1</b> (≈ 60 mots pour un texte d\'environ 220 mots) : L\'abeille mellifère vit dans une ruche organisée autour d\'une reine et de nombreuses ouvrières qui se partagent les tâches. Les butineuses récoltent le nectar, que la colonie transforme en miel pour l\'hiver. En passant de fleur en fleur, les abeilles transportent aussi le pollen : cette pollinisation est indispensable à une grande partie de nos cultures.</div>')
    e = E("J'analyse l'exemple de résumé du document 1. Je coche ce qui est vrai.", compact(table(["Le résumé…", "oui", "non"], [[x, '<span class="chk"></span>', '<span class="chk"></span>'] for x in ["respecte l'ordre des trois paragraphes", "recopie des phrases entières du texte", "donne l'avis de l'élève (« je trouve que… »)", "garde le chiffre de la FAO", "utilise un substitut résomptif (« cette pollinisation »)", "est environ quatre fois plus court que le texte"]], ["140mm", "21mm", "21mm"])), ["lis", "coche"], 1, "B",
          sol="oui · non · non · non (le chiffre est remplacé par « une grande partie ») · oui · oui")
    b.page(f'<span class="tag-doc">🎒 FRANÇAIS DE L\'ÉCOLE</span>{l4}{e}', "Consignes & école")
    e2 = E("Bon ou mauvais résumé ? Je lis les trois résumés du § 3 et je justifie mon choix.", '<div class="card sm" style="line-height:1.7">A. « Les abeilles transportent le pollen d\'une fleur à l\'autre, ce qui permet aux plantes de produire des fruits et des graines ; beaucoup de cultures en dépendent. »<br>B. « Je trouve que les abeilles sont très importantes, il faut les protéger ! »<br>C. « En butinant, les abeilles rendent aussi un service essentiel à la nature : elles transportent le pollen d\'une fleur à l\'autre. »</div>' + lines(2), ["lis", "ecris"], 2, "B",
           sol="A est le bon résumé (essentiel, mots personnels, pas d'opinion). B donne une opinion et oublie la pollinisation. C recopie le texte (paraphrase) et oublie la conséquence (les fruits, les cultures).")
    e3 = E("Les consignes du résumé. Je relie la consigne et ce qu'il faut faire.", relie(["Résumez le texte au quart de sa longueur.", "Ne citez pas le texte.", "Respectez l'énonciation.", "Indiquez le nombre de mots.", "Dégagez les idées essentielles."], ["Je compte les mots et j'écris le total à la fin.", "J'écris environ quatre fois moins de mots.", "Je repère et je garde ce qui est important.", "Je n'utilise pas les phrases du texte entre guillemets.", "Je ne dis pas « je » si l'auteur ne le dit pas ; je garde le point de vue du texte."]), ["lis", "relie"], 1, "B",
           sol="au quart → quatre fois moins de mots · ne citez pas → pas de guillemets · énonciation → pas de « je », point de vue du texte · nombre de mots → compter · idées essentielles → repérer et garder")
    e4 = E("Je résume en une phrase chaque paragraphe du document 1 (p. {0}), avec mes mots.".format(P["doc1"]), f'<p class="sm">§ 1 : {blank("xl")}</p><p class="sm">§ 2 : {blank("xl")}</p><p class="sm">§ 3 : {blank("xl")}</p>', ["lis", "ecris"], 2, "C",
           sol="Ex. : § 1 : Dans la ruche, une reine et des milliers d'ouvrières se partagent le travail. § 2 : Le nectar récolté devient du miel, la réserve de l'hiver. § 3 : En butinant, les abeilles pollinisent les plantes dont dépendent nos cultures.")
    b.page(f'{e2}{e3}{e4}', "Consignes & école")
    e = E("Je résume le texte (environ 120 mots) en 30 à 40 mots.", texte("Le fauchage tardif", ["En Wallonie, de nombreuses communes participent au programme de fauchage tardif : le long de certaines routes, l'herbe n'est coupée qu'à partir de la fin de l'été, au lieu de plusieurs fois au printemps. Pendant ce temps, les fleurs sauvages ont le temps de fleurir et de produire des graines.",
                                                                                       "Ces bords de routes fleuris deviennent de véritables refuges pour les insectes pollinisateurs, mais aussi pour les petits animaux. Ils relient entre eux les espaces naturels, comme des couloirs. Des panneaux signalent souvent ces zones aux automobilistes, qui pourraient croire que les bords de route sont mal entretenus."], num=False) + lines(4), ["lis", "ecris"], 3, "C",
          sol="Ex. : En Wallonie, grâce au fauchage tardif, certains bords de routes ne sont tondus qu'à la fin de l'été. Les fleurs sauvages peuvent ainsi fleurir et ces bandes deviennent des refuges et des couloirs pour les pollinisateurs et la petite faune. (≈ 40 mots)")
    e2 = E("Je rapporte les paroles de Mme Renard pour mon compte rendu avec un verbe introducteur varié (expliquer, préciser, conseiller, rappeler).", f'<p class="sm">1. « Une ouvrière vit cinq à six semaines en été. » → {blank("xl")}</p><p class="sm">2. « Plantez des fleurs dans votre jardin ! » → {blank("xl")}</p><p class="sm">3. « Les abeilles ne piquent que si elles se sentent menacées. » → {blank("xl")}</p>', ["ecris"], 2, "C",
           sol="Ex. : 1. Mme Renard explique qu'une ouvrière vit cinq à six semaines en été. — 2. Elle conseille de planter des fleurs dans son jardin. — 3. Elle rappelle (précise) que les abeilles ne piquent que si elles se sentent menacées.")
    e3 = E("Défi ! J'écris le compte rendu de la visite du rucher (8 lignes) pour le journal de l'école : en-tête, trois moments importants, ce que la classe retient. J'utilise mes notes de l'exercice précédent.", lines(7), ["ecris"], 3, "C",
           sol="Ex. : Le 6 mai, la classe DASPA a visité le rucher pédagogique du parc de Hautrive. D'abord, les élèves ont enfilé une combinaison et observé une ruche. Ensuite, Mme Renard, l'apicultrice, a expliqué l'organisation de la colonie… Enfin, elle a présenté les menaces (varroa, frelon asiatique, pesticides). La classe retient que chacun peut aider les abeilles en plantant des fleurs.")
    b.page(f'{e}{e2}{e3}', "Consignes & école")

    # ---------- Leçon 5 : la synthèse de documents ----------
    DOC2 = ["Quand on parle d'abeilles, on pense à la ruche et au miel. Pourtant, en Belgique, on compte environ 400 espèces d'abeilles sauvages, et la plupart ne vivent pas en colonie : elles sont solitaires. Beaucoup creusent leur nid dans le sol ; d'autres s'installent dans des tiges creuses ou dans de vieux murs.",
            "Ces abeilles sauvages sont d'excellentes pollinisatrices, parfois plus efficaces que l'abeille domestique pour certaines plantes. Or, une grande partie d'entre elles sont en déclin. Les spécialistes citent plusieurs causes : la disparition des prairies fleuries et des haies, l'usage de pesticides, le changement climatique, et la concurrence avec les ruches trop nombreuses dans certaines villes."]
    infog = (f'<div class="card" style="background:#fff;padding:2.5mm 3.5mm"><b style="color:{MC}">Document 3 · Comment aider les pollinisateurs ?</b> <span class="xs muted">(infographie fictive d\'après des conseils d\'associations de protection de la nature)</span>'
             '<div class="grid4" style="gap:1.5mm;margin-top:1.5mm">' + "".join(f'<div class="card c xs" style="padding:1.5mm;background:{TINT}"><div style="font-size:16pt">{ic}</div>{t}</div>' for ic, t in [("🌼", "Semer des fleurs locales et variées, du printemps à l'automne"), ("🚫", "Ne pas utiliser de pesticides au jardin"), ("🌾", "Laisser un coin d'herbe haute (tondre moins souvent)"), ("🪵", "Installer un abri : tiges creuses, bois percé, sol nu")]) + '</div>'
             '<p class="xs" style="margin:1.5mm 0 0">🇧🇪 En Wallonie, les espaces publics (parcs, trottoirs, cimetières) sont gérés sans pesticides chimiques depuis 2019. Le 20 mai, c\'est la <b>Journée mondiale des abeilles</b>, proclamée par l\'ONU.</p></div>')
    P["synth"] = b.n + 1
    l5 = lecon("La synthèse de documents", '<p class="sm" style="margin-bottom:1.5mm">Une <b>synthèse</b> rassemble les informations de <b>plusieurs documents</b> sur un même thème, pour répondre à une <b>question</b>. Elle ne résume pas les documents l\'un après l\'autre : elle les <b>confronte</b> (ce qu\'ils disent en commun, ce qui les différencie, ce que chacun ajoute).</p>' +
        compact(table(["Étape", "Ce que je fais"], [["① La question", "Je formule la question de la synthèse (ex. : Pourquoi faut-il protéger les abeilles et comment ?)"], ["② Le tableau", "Pour chaque document, je note les idées utiles dans un tableau de confrontation (une colonne par document)"], ["③ Le plan", "Je regroupe les idées par thème (2 ou 3 parties), pas par document"], ["④ La rédaction", "Introduction (thème + question + documents) · développement (une partie = un paragraphe) · conclusion (réponse à la question)"]], ["30mm", "152mm"])) +
        '<div class="astuce" style="margin:2mm 0 0">🔗 <b>Pour confronter</b> : les trois documents <b>s\'accordent</b> sur… · <b>selon</b> le document 2… · le document 3 <b>ajoute</b> que… · <b>de même</b>, <b>également</b> (ressemblance) · <b>en revanche</b>, <b>alors que</b>, <b>tandis que</b> (différence) · <b>par ailleurs</b> (une autre idée). Je ne donne <b>pas mon avis</b> dans une synthèse.</div>')
    e = E("Je lis le document 2 et le document 3.", texte("Document 2 · Les abeilles sauvages, ces inconnues", DOC2) + '<div class="mt2">' + infog + '</div>', ["lis"], 1, "B", sol="Lecture ; vérifier la compréhension des mots solitaire, déclin, concurrence.")
    b.page(f'{l5}{e}', "Leçon 5")
    e2 = E(f"Je complète le tableau de confrontation des trois documents (document 1 : p. {P['doc1']}).", confrontation([("Les abeilles : qui sont-elles ?", None), ("Pourquoi sont-elles utiles ?", None), ("Quelles menaces ?", None), ("Que faire ?", None)], vide=True, h=19), ["lis", "ecris"], 2, "C",
           sol="Qui ? Doc. 1 : abeille mellifère, colonie (reine, ouvrières) · Doc. 2 : env. 400 espèces sauvages en Belgique, surtout solitaires · Doc. 3 : « pollinisateurs ». Utiles ? Doc. 1 : miel + pollinisation (¾ des cultures, FAO) · Doc. 2 : excellentes pollinisatrices · Doc. 3 : —. Menaces ? Doc. 1 : — · Doc. 2 : perte des prairies et haies, pesticides, climat, concurrence des ruches · Doc. 3 : (pesticides, tonte). Que faire ? Doc. 1 : — · Doc. 2 : — · Doc. 3 : fleurs locales, pas de pesticides, herbe haute, abris ; Wallonie sans pesticides dans l'espace public.")
    e3 = E("Ressemblance ou différence ? Je complète avec : de même · en revanche · alors que · également.", card("1. Le document 1 parle de l'abeille à miel, ______________ le document 2 présente les abeilles sauvages. 2. Le document 2 cite les pesticides comme menace ; le document 3 conseille ______________ de ne pas en utiliser. 3. L'abeille domestique vit en colonie. ______________ , la plupart des abeilles sauvages sont solitaires. 4. Les abeilles domestiques pollinisent les fleurs ; ______________ , les abeilles sauvages sont d'excellentes pollinisatrices."), ["complete"], 2, "C",
          sol="1. alors que — 2. également — 3. En revanche — 4. de même")
    b.page(f'{e2}{e3}', "Leçon 5")
    e = E("Je choisis le meilleur plan pour la synthèse « Pourquoi et comment protéger les abeilles ? ». Je justifie.", '<div class="card sm" style="line-height:1.7">Plan A : I. Le document 1 · II. Le document 2 · III. Le document 3<br>Plan B : I. Des insectes indispensables · II. Des insectes menacés · III. Des gestes pour les protéger</div>' + lines(2), ["lis", "ecris"], 2, "B",
           sol="Le plan B : il regroupe les idées par thème et répond à la question ; le plan A juxtapose des résumés (ce n'est pas une synthèse).")
    e2 = E("J'écris l'introduction de la synthèse (3 phrases) : le thème, la question, les trois documents.", lines(4), ["ecris"], 2, "C",
           sol="Ex. : Les abeilles sont au cœur de nombreuses discussions sur la nature. Pourquoi faut-il les protéger et comment ? Pour répondre, nous nous appuyons sur un texte sur l'abeille mellifère, un article sur les abeilles sauvages et une infographie de conseils.")
    e3 = E("Défi ! J'écris la partie II de la synthèse (« Des insectes menacés »), en confrontant au moins deux documents.", lines(7), ["ecris"], 3, "C",
           sol="Ex. : Pourtant, ces insectes sont menacés. Selon le document 2, une grande partie des abeilles sauvages de Belgique est en déclin, à cause de la disparition des prairies fleuries et des haies, des pesticides et du changement climatique. Le document 3 confirme le danger des pesticides, puisqu'il conseille de ne plus en utiliser au jardin.")
    b.page(f'{e}{e2}{e3}', "S'entraîner")

    # ---------- Documents de la vie ----------
    depl = f'''<div class="doc" style="transform:none;border:2px solid {MC};background:#FFFDF6;padding:3mm 4mm;font-size:9.1pt;line-height:1.38">
<div class="flex" style="justify-content:space-between;align-items:center"><div><span class="xs" style="color:{MC};font-weight:700">COMMUNE DE HAUTRIVE · SERVICE ENVIRONNEMENT</span><br><b style="font-size:14pt;color:#1F2A44">🐝 Le rucher pédagogique du parc</b></div><span class="xs muted">(dépliant fictif)</span></div>
<div class="grid2" style="gap:3mm;margin-top:1.5mm"><div><b>Visites guidées</b> pour les écoles et les familles, d'avril à septembre, le mercredi après-midi et le samedi matin, avec Mme Renard, apicultrice. Durée : 1 h 30. Gratuit pour les écoles de la commune ; 3 € par adulte, gratuit pour les moins de 12 ans.<br><b>Au programme</b> : observation d'une ruche vitrée · dégustation de miel · fabrication d'un petit abri à abeilles sauvages.<br><b>Sécurité</b> : combinaisons et voiles fournis. Les personnes allergiques aux piqûres doivent le signaler à l'inscription.</div>
<div><b>Le saviez-vous ?</b> Pour produire un pot de miel, les abeilles doivent butiner des centaines de milliers de fleurs.<br><b>Le 20 mai</b>, Journée mondiale des abeilles : portes ouvertes de 10 h à 17 h, stands, bourse aux graines de fleurs mellifères.<br><b>Réservation</b> obligatoire au moins deux semaines à l'avance : environnement@hautrive-exemple.be ou 087 65 12 34 (du lundi au vendredi, de 9 h à 12 h).</div></div></div>'''
    e = E("Je lis le dépliant du rucher pédagogique. Je réponds.", depl + f'<p class="sm mt2">1. Quand peut-on visiter le rucher ? Combien de temps dure la visite ? {blank("xl")}</p><p class="sm">2. La famille de Fatou (deux adultes et trois enfants de 6, 9 et 14 ans) visite le rucher. Combien paie-t-elle ? {blank("xl")}</p><p class="sm">3. Que doit faire une personne allergique aux piqûres ? {blank("xl")}</p><p class="sm">4. La classe veut venir le 6 mai. Avant quelle date doit-elle réserver ? Comment ? {blank("xl")}</p><p class="sm">5. Résume le dépliant en une phrase. {blank("xl")}</p>', ["lis", "ecris"], 2, "B",
          sol="1. D'avril à septembre, le mercredi après-midi et le samedi matin ; 1 h 30. — 2. 2 × 3 € + 14 ans : 3 € (plus de 12 ans) = 9 € ; les enfants de 6 et 9 ans sont gratuits. — 3. Le signaler à l'inscription. — 4. Avant le 22 avril (deux semaines avant) ; par courriel ou par téléphone en semaine de 9 h à 12 h. — 5. Ex. : La commune propose des visites guidées de son rucher pédagogique pour découvrir les abeilles, sur réservation.")
    e2 = E("J'écris le courriel de réservation de la classe (registre formel, module 12) : objet, date souhaitée, nombre d'élèves, une question.", lines(5), ["ecris"], 2, "C",
           sol="Ex. : Objet : réservation d'une visite scolaire — Madame, Monsieur, Je vous écris de la part de la classe DASPA de l'Athénée de Hautrive. Nous souhaiterions visiter le rucher pédagogique le mercredi 6 mai à 14 h, avec 16 élèves et 2 professeurs. Pourriez-vous nous dire si une élève allergique peut participer ? Bien à vous, …")
    b.page(f'<span class="tag-doc">📄 DOCUMENT DE LA VIE</span><h2>Un dépliant</h2>{e}{e2}', "Document de la vie")
    cr = f'''<div class="doc" style="transform:none;border:1.5px solid #9aa1b1;background:#fff;padding:3mm 4mm;font-size:9.1pt;line-height:1.38;font-family:'DejaVu Serif'">
<b style="font-size:11pt">Compte rendu de la réunion du conseil des élèves</b> <span class="xs muted">(document fictif)</span><br>
<span class="xs"><b>Date :</b> jeudi 23 avril 2027, de 12 h 30 à 13 h 15 · <b>Lieu :</b> local 12, Athénée de Hautrive · <b>Présents :</b> 14 délégués, M. Diallo (éducateur) · <b>Excusés :</b> les délégués de 5e (voyage scolaire) · <b>Secrétaire :</b> Daria Kovalenko (DASPA)</span>
<p style="margin:1.5mm 0"><b>1. Projet « Une cour pour les abeilles ».</b> Fatou Camara présente la proposition de la classe DASPA : transformer un coin de la cour en prairie fleurie et y installer un abri à abeilles sauvages. Plusieurs délégués soulignent que le projet est peu coûteux. Les délégués de 1re craignent les piqûres ; M. Diallo précise que les abeilles sauvages sont très peu agressives. <b>Décision :</b> le projet est adopté à 12 voix contre 2.</p>
<p style="margin:1.5mm 0"><b>2. Fontaine à eau.</b> La direction a accepté l'installation d'une deuxième fontaine près du réfectoire. Elle sera installée en juin.</p>
<p style="margin:1.5mm 0 0"><b>3. Divers.</b> Les délégués rappellent que la fête de fin d'année aura lieu le 26 juin. <b>Prochaine réunion :</b> jeudi 21 mai, même heure, même lieu.</p></div>'''
    e = E("Je lis le compte rendu de réunion. Je réponds.", cr + f'<p class="sm mt2">1. Retrouve dans l\'en-tête : quoi, quand, où, qui. {blank("xl")}</p><p class="sm">2. Qu\'est-ce que la classe DASPA a proposé ? Quelle a été la décision ? {blank("xl")}</p><p class="sm">3. Quelle crainte ont exprimée certains délégués ? Comment M. Diallo les a-t-il rassurés ? {blank("xl")}</p><p class="sm">4. Relève deux verbes qui introduisent des paroles rapportées. {blank("l")}</p>', ["lis", "ecris"], 2, "B",
          sol="1. La réunion du conseil des élèves ; le jeudi 23 avril 2027 de 12 h 30 à 13 h 15 ; au local 12 de l'Athénée ; 14 délégués et M. Diallo (secrétaire : Daria). — 2. Transformer un coin de la cour en prairie fleurie avec un abri à abeilles sauvages ; le projet est adopté à 12 voix contre 2. — 3. Les délégués de 1re craignent les piqûres ; M. Diallo précise que les abeilles sauvages sont très peu agressives. — 4. présente, soulignent, craignent, précise, rappellent (deux au choix).")
    e2 = E("À la place d'un délégué absent, je résume la réunion en 3 phrases pour ma classe (sans détails inutiles).", lines(3), ["ecris"], 2, "C",
           sol="Ex. : Le conseil des élèves a adopté le projet de la classe DASPA : un coin de la cour deviendra une prairie fleurie pour les abeilles sauvages. Une deuxième fontaine à eau sera installée en juin près du réfectoire. La prochaine réunion aura lieu le 21 mai.")
    b.page(f'<span class="tag-doc">📄 DOCUMENT DE LA VIE</span><h2>Un compte rendu de réunion</h2>{e}{e2}', "Document de la vie")

    # ---------- Vers les épreuves ----------
    TXT = ["Le moustique tigre, reconnaissable à ses rayures noires et blanches, est originaire d'Asie du Sud-Est. Depuis une trentaine d'années, il se répand dans le monde entier, en voyageant notamment dans des pneus usagés et des plantes transportées par bateau. En Europe, il s'est d'abord installé dans le Sud, puis il progresse peu à peu vers le nord.",
           "Ce petit insecte inquiète les autorités sanitaires, car il peut transmettre certains virus, comme ceux de la dengue ou du chikungunya, lorsqu'il pique une personne déjà infectée puis une autre. En Belgique, sa présence est surveillée depuis plusieurs années : des pièges sont placés près des lieux à risque, comme les parkings d'autoroute ou les entreprises de pneus.",
           "Contrairement à beaucoup d'autres moustiques, le moustique tigre pique surtout en journée. Il pond ses œufs dans de très petites quantités d'eau stagnante : une soucoupe sous un pot de fleurs, un seau oublié, une gouttière bouchée. C'est pourquoi chacun peut agir en vidant régulièrement tout ce qui retient l'eau autour de la maison.",
           "Les spécialistes rappellent toutefois qu'il ne faut pas céder à la panique. La plupart des piqûres sont seulement désagréables. En revanche, signaler la présence de l'insecte aux autorités permet de mieux suivre son installation et d'agir rapidement."]
    P["epr"] = b.n + 1
    e = E("Entraînement de type CE1D : je lis le texte documentaire et je réponds.", texte("Le moustique tigre, un voyageur indésirable", TXT, fs=9.3) +
          f'<p class="sm mt2" style="margin-bottom:1mm">a) Quel est le thème du texte ? {blank("xl")}</p><p class="sm" style="margin-bottom:1mm">b) Donne un titre à chaque paragraphe. {blank("xl")}{blank("xl")}</p><p class="sm" style="margin-bottom:1mm">c) Relève trois substituts qui désignent le moustique tigre. {blank("xl")}</p><p class="sm" style="margin-bottom:1mm">d) « Ce petit insecte inquiète les autorités sanitaires » : reformule cette phrase avec la nominalisation de « inquiéter ». {blank("xl")}</p><p class="sm" style="margin-bottom:1mm">e) Pourquoi chacun peut-il agir contre le moustique tigre ? Réponds avec tes mots. {blank("xl")}</p>', ["lis", "ecris"], 3, "C",
          sol="a) Le moustique tigre, son arrivée en Europe et en Belgique, les risques et les gestes de prévention. — b) § 1 : Un insecte venu d'Asie qui voyage · § 2 : Un risque pour la santé, sous surveillance · § 3 : Des habitudes particulières et des gestes simples · § 4 : Pas de panique, mais signaler. — c) « Ce petit insecte », « il », « l'insecte » (« son installation »). — d) Ex. : Ce petit insecte est une source d'inquiétude pour les autorités sanitaires. / L'inquiétude des autorités sanitaires vient de ce petit insecte. — e) Parce qu'il pond dans de très petites quantités d'eau : en vidant ce qui retient l'eau autour de la maison, on l'empêche de se reproduire.")
    b.page(EPR.format(k="CE1D", t="Résumer un texte documentaire") + e, "Vers les épreuves")
    e = E("Suite de l'épreuve.", f'<p class="sm">f) Résume le texte en 50 à 60 mots. Indique le nombre de mots.</p>{lines(7)}', ["lis", "ecris"], 3, "C",
          sol="f) Ex. : Venu d'Asie, le moustique tigre s'étend en Europe en voyageant avec les marchandises. Il inquiète, car il peut transmettre des virus ; la Belgique le surveille. Comme il pond dans de petites flaques, chacun peut vider l'eau stagnante. Sans paniquer, il faut signaler sa présence. (≈ 55 mots)")
    e2 = E("Entraînement DELF B1 · compréhension de l'oral : j'écoute un court reportage radio (deux fois) et je réponds.", f'<p class="sm">1. De quel événement parle le reportage ? Où se passe-t-il ? {blank("xl")}</p><p class="sm">2. Combien de ruches y a-t-il sur le toit ? {blank("l")}</p><p class="sm">3. Pourquoi les abeilles se portent-elles bien en ville, selon l\'apiculteur ? (deux raisons) {blank("xl")}</p><p class="sm">4. Quel problème le spécialiste signale-t-il ? {blank("xl")}</p><p class="sm">5. Que conseille-t-il aux auditeurs ? {blank("xl")}</p><p class="sm">6. Résume le reportage en une phrase. {blank("xl")}</p><div class="astuce">🎓 Au DELF B1, la compréhension de l\'oral dure environ 25 minutes : trois documents enregistrés, que l\'on entend deux fois. Lis les questions avant la première écoute et prends des notes rapides avec des symboles (leçon 1) !</div>', ["ecoute", "ecris"], 3, "A",
           script="Reportage (fictif) : « Nous sommes sur le toit d'une bibliothèque à Liège, où six ruches ont été installées il y a trois ans. L'apiculteur, Thomas, est ravi : “En ville, les abeilles trouvent des fleurs variées dans les parcs et les jardins, et il y a moins de pesticides qu'à la campagne.” Mais un spécialiste des insectes nuance : “Attention, s'il y a trop de ruches au même endroit, les abeilles domestiques prennent la nourriture des abeilles sauvages.” Son conseil : planter plus de fleurs, plutôt qu'installer toujours plus de ruches. »",
           sol="1. Des ruches installées sur le toit d'une bibliothèque ; à Liège. — 2. Six ruches. — 3. Les fleurs sont variées (parcs, jardins) et il y a moins de pesticides qu'à la campagne. — 4. Trop de ruches au même endroit : les abeilles domestiques prennent la nourriture des abeilles sauvages. — 5. Planter plus de fleurs plutôt qu'installer plus de ruches. — 6. Ex. : À Liège, des ruches sur un toit se portent bien, mais un spécialiste rappelle qu'il vaut mieux planter des fleurs que multiplier les ruches.")
    b.page(f'{e}{e2}', "Vers les épreuves")

    # ---------- Sons ----------
    e = E("[s] ou [z] ? J'écoute et je répète.", '<div class="grid2"><div class="card c"><div class="big"><b>[s]</b></div><p class="big" style="margin:1mm 0 0">un poi<b>ss</b>on · un de<b>ss</b>ert · le <b>s</b>ucre · une <b>s</b>ynthèse · la <b>c</b>ire · na<b>ti</b>on</p></div><div class="card c"><div class="big"><b>[z]</b></div><p class="big" style="margin:1mm 0 0">un poi<b>s</b>on · un dé<b>s</b>ert · la ro<b>s</b>e · ré<b>s</b>umer · <b>z</b>éro · les‿abeilles</p></div></div><p class="sm" style="margin:2mm 0 0">✏️ Entre deux voyelles, un seul <b>s</b> se prononce [z] (ré<b>s</b>umé, ro<b>s</b>e) ; <b>ss</b> se prononce [s] (poi<b>ss</b>on). [s] : l\'air passe, la gorge ne vibre pas. [z] : la gorge vibre (pose ta main sur ta gorge !).</p>', ["ecoute", "repete"], 1, "A",
          script="Lire les paires poisson / poison, dessert / désert en faisant sentir la vibration.", sol="Activité orale.")
    e2 = E("J'écoute : [s] ou [z] ? Je coche.", checks(8, ["[s]", "[z]"]), ["ecoute", "coche"], 2, "A", script="1. le résumé 2. la synthèse 3. la cuisine 4. un coussin 5. une cousine 6. il pense 7. une base 8. une basse",
           sol="[s] : 2, 4, 6, 8 · [z] : 1, 3, 5, 7")
    e3 = E("J'écris s ou ss, puis je lis à voix haute.", card("1. un ré__umé 2. une pa__ion 3. la cui__ine 4. la cha__e 5. une ro__e 6. la pre__e 7. un pa__age 8. elle choi__it"), ["complete", "repete"], 1, "C",
           sol="1. résumé — 2. passion — 3. cuisine — 4. chasse — 5. rose — 6. presse — 7. passage — 8. choisit")
    e4 = E("Dictée : j'écoute deux fois et j'écris.", lines(3), ["ecoute", "ecris"], 2, "A",
           script="« Pour résumer un texte, il faut choisir l'essentiel. Ensuite, on reformule les idées principales avec ses propres mots, sans donner son avis. »",
           sol="Pour résumer un texte, il faut choisir l'essentiel. Ensuite, on reformule les idées principales avec ses propres mots, sans donner son avis.")
    b.page(f'<h2>J\'écoute bien · [s] / [z]</h2>{e}{e2}{e3}{e4}', "Sons")
    e = E("Résumer à l'oral. J'écoute deux résumés du même film. Lequel est le meilleur ? Je coche ce que j'entends.", compact(table(["", "Résumé 1", "Résumé 2"], [[x, '<span class="chk"></span>', '<span class="chk"></span>'] for x in ["dit le titre et le genre", "présente le personnage principal et son problème", "va à l'essentiel (moins d'une minute)", "évite « et après… et après… »", "ne raconte pas toute la fin (pas de « divulgâchage »)"]], ["110mm", "36mm", "36mm"])), ["ecoute", "coche"], 2, "A",
          script="1 : « Alors, au début, il y a un garçon, et après il va à l'école, et après il rencontre un chien, et après le chien se perd, et après il le cherche, et après… » — 2 : « “Le Chien du port” est un film d'aventures. Tom, un garçon de douze ans, recueille un chien abandonné. Quand le chien disparaît, Tom part à sa recherche dans toute la ville. Je ne vous dis pas la fin ! »",
          sol="Le résumé 2 coche toutes les cases ; le résumé 1 raconte tout avec « et après » et ne donne ni titre ni genre.")
    e2 = E("Je lis le résumé du document 1 (p. {0}) à voix haute en respectant les groupes de souffle (|) : je respire seulement aux barres.".format(P["resume"]), '<div class="card big" style="background:#fff;line-height:1.9">L\'abeille mellifère vit dans une ruche | organisée autour d\'une reine | et de nombreuses ouvrières | qui se partagent les tâches. | Les butineuses récoltent le nectar, | que la colonie transforme en miel | pour l\'hiver.</div>', ["lis", "repete"], 1, "A",
           sol="Lecture fluide ; la voix descend à la fin de chaque phrase.")
    e3 = E("Les liaisons du texte documentaire. Je marque les liaisons (‿) puis je lis.", '<div class="card big" style="line-height:2">1. les‿abeilles · les‿ouvrières · les‿insectes 2. un‿essaim · un‿apiculteur 3. Elles‿y trouvent du nectar. 4. trois‿espèces · deux‿abris 5. C\'est‿essentiel.</div>', ["lis", "repete"], 1, "A",
           sol="[z] : les‿abeilles, les‿ouvrières, les‿insectes, elles‿y, trois‿espèces, deux‿abris · [n] : un‿essaim, un‿apiculteur · [t] : c'est‿essentiel")
    e4 = E("À mon tour ! En une minute, je résume oralement à mon voisin un texte que j'ai lu dans ce module (ou une leçon d'un autre cours). Il chronomètre et me dit si j'ai gardé l'essentiel.", lines(1), ["parle", "duo"], 2, "A",
           sol="Activité orale ; le voisin note une idée essentielle oubliée, s'il y en a une.")
    b.page(f'<h2>J\'écoute bien · résumer à l\'oral</h2>{e}{e2}{e3}{e4}', "Sons")

    # ---------- Révision spirale ----------
    e = E("🔁 V3 · Module 14 · Les types de phrases. « Que les abeilles sont travailleuses ! » est une phrase ______________ .", "", ["complete"], 1, "C", sol="exclamative")
    e2 = E("🔁 V3 · Module 13 · Le but. Je complète : On plante des fleurs ______________ (pour / pour que) les abeilles trouvent du nectar.", "", ["complete"], 1, "C", sol="pour que")
    e3 = E("🔁 V3 · Module 11 · Le subjonctif. Il faut que nous (protéger) ______________ les abeilles et que chacun (faire) ______________ un effort.", "", ["complete"], 1, "C", sol="protégions · fasse")
    e4 = E("🔁 V3 · Module 8 · Le passif. « Les abeilles pollinisent les fleurs. » → Les fleurs ______________________________ .", "", ["ecris"], 2, "C", sol="Les fleurs sont pollinisées par les abeilles.")
    e5 = E("🔁 V3 · Module 7 · Donner son avis. Faut-il installer des ruches sur le toit de l'école ? Mon avis en 2 phrases avec un argument.", lines(2), ["ecris"], 2, "C", sol="Ex. : Oui, je pense que ce serait une bonne idée, car les élèves pourraient observer les abeilles. Cependant, il faudrait aussi planter beaucoup de fleurs.")
    e6 = E("🔁 V3 · Module 6 · Le discours indirect. Mme Renard dit : « Les abeilles ne piquent pas sans raison. » → Mme Renard dit que ______________________________ .", "", ["ecris"], 2, "C", sol="les abeilles ne piquent pas sans raison")
    e7 = E("🔁 V3 · Module 2 · Les maths. Une ruche donne 20 kg de miel par an. Combien de pots de 500 g peut-on remplir ?", '<p>' + blank("xl") + '</p>', ["ecris"], 1, "C", sol="20 kg = 20 000 g ; 20 000 ÷ 500 = 40 pots")
    e8 = E("🔁 V3 · Module 5 · La géographie. Je cite deux types de paysages en Belgique où l'on peut trouver des fleurs sauvages pour les abeilles.", '<p>' + blank("xl") + '</p>', ["ecris"], 1, "C", sol="Ex. : les prairies, les bords de routes en fauchage tardif, les forêts (lisières), les jardins, les parcs.")
    b.page(f'<h2>🔁 Je révise les modules précédents</h2>{e}{e2}{e3}{e4}{e5}{e6}{e7}{e8}', "Je révise")

    # ---------- Ateliers ----------
    e = E("Le téléphone arabe du résumé (groupes de 4). Le premier lit un court texte (carte de la prof) et le résume oralement au deuxième en 3 phrases ; le deuxième le résume au troisième en 2 phrases ; le troisième au quatrième en 1 phrase. Le quatrième écrit la phrase. On compare avec le texte !", lines(2), ["parle", "ecoute", "groupe"], 2, "A",
          script="Préparer 6 cartes de textes documentaires courts (100 mots) sur des animaux ou des inventions.",
          sol="La phrase finale garde-t-elle l'idée principale ? Discussion : quelles informations ont été perdues, lesquelles étaient vraiment essentielles ?")
    e2 = E("L'exposé flash (seul, 1 minute) : je présente à la classe un document du module (1, 2 ou 3) à partir de mes seules notes.", tall(compact(table(["Mes notes (mots-clés, symboles)"], [[""]], ["182mm"])), 30), ["ecris", "parle"], 2, "A",
           sol="Notes sous forme de mots-clés ; exposé fluide, sans lire de phrases entières.")
    e3 = E("Je suis auditeur : je note l'idée principale de l'exposé d'un camarade et une question à lui poser.", lines(2), ["ecoute", "ecris"], 1, "A",
           sol="Ex. : Idée principale : les abeilles sauvages sont nombreuses et souvent solitaires. Question : Comment peut-on les reconnaître ?")
    b.page(f'{atl_head("A", "Atelier · Résumer à l\'oral")}{e}{e2}{e3}', "Atelier")
    art = texte("Les vers de terre, ouvriers du sol", ["Discrets, les vers de terre jouent pourtant un rôle immense. En creusant leurs galeries, ils aèrent le sol et permettent à l'eau de pluie de s'infiltrer. Ils mangent aussi les feuilles mortes et les restes de plantes, qu'ils transforment en un engrais naturel très riche.",
                                                                    "Dans une prairie en bonne santé, on peut compter des centaines de vers sous chaque mètre carré. Mais le labour profond, certains produits chimiques et le tassement du sol par les machines agricoles réduisent leur nombre. Pour les protéger, des agriculteurs travaillent moins la terre et laissent des débris végétaux à la surface."], fs=9.4)
    e = E("Je lis le texte et je prends des notes en mots-clés et symboles (dans la colonne de droite).", '<div style="display:grid;grid-template-columns:1.6fr 1fr;gap:3mm">' + art + '<div class="card" style="background:' + TINT + ';min-height:60mm"><b class="sm">Mes notes</b></div></div>', ["lis", "ecris"], 2, "B",
          sol="Ex. : vers de terre = rôle +++ · galeries → sol aéré + eau s'infiltre · mangent feuilles mortes → engrais naturel · prairie : centaines / m² · ↘ ← labour, chimie, tassement (machines) · protection : moins travailler terre + débris en surface")
    e2 = E("Je rédige le résumé du texte en 35 à 45 mots, à partir de mes notes seulement (je cache le texte !).", lines(4), ["ecris"], 3, "C",
           sol="Ex. : Les vers de terre aèrent le sol, aident l'eau à s'infiltrer et transforment les débris végétaux en engrais. Très nombreux dans les prairies, ils diminuent à cause du labour, des produits chimiques et des machines ; certains agriculteurs changent leurs pratiques pour les protéger. (≈ 45 mots)")
    e3 = E("J'échange mon résumé avec mon voisin : il vérifie avec la grille.", chk3(["Le résumé respecte l'ordre du texte.", "Il garde les idées essentielles, sans détails.", "Il n'y a ni citation ni opinion.", "Il compte 35 à 45 mots."]), ["lis", "coche"], 1, "B", sol="Grille remplie ; amélioration proposée.")
    b.page(f'{atl_head("B", "Atelier · Des notes au résumé")}{e}{e2}{e3}', "Atelier")
    e = E("Je rédige la synthèse complète « Pourquoi et comment protéger les abeilles ? » (15 à 18 lignes) à partir de mon tableau de confrontation (p. {0}) : introduction, trois parties, conclusion.".format(P["synth"] + 1), lines(16), ["ecris"], 3, "C",
          sol="Synthèse organisée par thèmes (utilité, menaces, solutions), confrontation des documents (selon le document…, de même, en revanche), substituts variés, reformulation (pas de citations longues), pas d'opinion, conclusion qui répond à la question ; environ 200 mots.")
    e2 = E("Je relis ma synthèse avec la grille.", chk3(["J'ai une introduction (thème, question, documents) et une conclusion.", "Mes parties suivent un thème, pas un document.", "Je confronte les documents avec des connecteurs.", "J'utilise des substituts et je reformule sans recopier."]), ["lis", "coche"], 1, "C", sol="Grille complétée ; corriger avant de recopier au propre.")
    b.page(f'{atl_head("C", "Atelier · J\'écris une synthèse")}{e}{e2}', "Atelier")
    cases = ["Départ : tu ouvres le dossier « Abeilles ».", "Donne un synonyme de « important ».", "Tu as recopié une phrase entière : recule de 2 cases !", "Nominalise : « disparaître ».", "Remplace « les abeilles » par un terme générique.", "Ton résumé respecte l'ordre du texte : avance de 2 cases.",
             "Que signifie le symbole → ?", "Cite une règle du résumé.", "Tu as donné ton avis dans la synthèse : passe un tour.", "Qu'est-ce qu'une reprise résomptive ? Donne un exemple.", "Cite deux connecteurs pour comparer des documents.", "Arrivée : synthèse parfaite ! BRAVO !"]
    plateau = '<div class="grid4" style="gap:1.4mm">' + "".join(f'<div class="card sm" style="padding:2mm;min-height:22mm;background:{"#FFE8D6" if i == 11 else "#fff"}"><b style="color:{MC}">{i + 1}</b> {t}</div>' for i, t in enumerate(cases)) + '</div>'
    e = E("Le jeu « La course au résumé » (2 à 4 joueurs, un dé, un pion par joueur).", '<p class="sm" style="margin:0 0 1.5mm">On lance le dé et on avance. Sur une case « question », on répond : si la réponse est juste (les autres vérifient dans le cahier), on reste ; sinon, on recule d\'une case. Le premier qui arrive à la case 12 a gagné !</p>' + plateau, ["joue", "groupe"], 2, "D",
          sol="Réponses : 2. essentiel, capital, majeur · 4. la disparition · 5. ces insectes (ces pollinisateurs) · 7. entraîne, a pour conséquence · 8. Ex. : pas d'opinion ; mes propres mots ; environ ¼ du texte ; respecter l'ordre · 10. un mot qui résume toute une idée (ce phénomène, cette situation) · 11. de même, en revanche, alors que, également.")
    e2 = E("Le jeu « Le titre en 5 mots » (toute la classe). La prof lit un court article de journal (adapté) ; chacun écrit un titre de 5 mots maximum. On vote pour le titre qui résume le mieux l'article.", lines(1), ["joue", "ecoute", "groupe"], 1, "D",
           sol="Jeu ; discuter : un bon titre donne le thème et l'idée principale.")
    e3 = E("Le jeu du « mot interdit » (en duo). Je fais deviner un mot du module (résumé, synthèse, pollinisation, ruche…) sans le dire, en le reformulant.", '<div class="card sm" style="background:#fff">Exemple : « C\'est un texte plus court qui garde seulement l\'essentiel d\'un autre texte. » → un résumé !</div>', ["joue", "parle", "duo"], 1, "D",
           sol="Jeu oral de reformulation ; vérifier la précision des définitions.")
    b.page(f'{atl_head("D", "Atelier · Jeux de résumé")}{e}{e2}{e3}', "Atelier")

    # ---------- ★ Coup de pouce ----------
    e = E("Je relie le mot et le dessin.", relie(["une abeille", "une fleur", "le miel", "une ruche", "un fruit"], ["🍯", "🏠🐝", "🌼", "🍎", "🐝"]), ["relie"], 1, "B", alpha=True, sol="abeille → 🐝 · fleur → 🌼 · miel → 🍯 · ruche → 🏠🐝 · fruit → 🍎")
    e2 = E("Je lis le petit texte et j'entoure la phrase la plus importante.", '<div class="card big" style="line-height:2">Les abeilles sont très utiles. Elles font du miel. Elles aident les fleurs à faire des fruits. Elles ont des rayures jaunes et noires.</div>', ["lis", "entoure"], 1, "C", alpha=True, sol="Les abeilles sont très utiles.")
    e3 = E("Je complète le résumé en une phrase.", '<p class="big" style="line-height:2.1">Les abeilles sont ______________ : elles font du ______________ et elles aident les fleurs.</p>', ["complete"], 1, "C", alpha=True, sol="utiles · miel")
    e4 = E("Je souligne les deux mots-clés de chaque phrase.", '<p class="big" style="line-height:2.1">1. Les abeilles font du miel.<br>2. Les fleurs donnent du nectar.<br>3. La reine pond des œufs.</p>', ["souligne"], 1, "C", alpha=True, sol="1. abeilles, miel — 2. fleurs, nectar — 3. reine, œufs")
    b.page(CP.format(t="L'essentiel") + e + e2 + e3 + e4, "★ Coup de pouce")
    e = E("Je remplace le mot répété par il, elle, ils ou elles.", '<p class="big" style="line-height:2.1">1. Mme Renard a des ruches. <u>Mme Renard</u> → ______ aime les abeilles.<br>2. Les abeilles butinent. <u>Les abeilles</u> → ______ font du miel.<br>3. Bilal lit le texte. <u>Bilal</u> → ______ prend des notes.</p>', ["complete"], 1, "C", alpha=True, sol="1. Elle — 2. Elles — 3. Il")
    e2 = E("Je relie le mot et son synonyme.", relie(["important", "petit", "commencer", "finir"], ["terminer", "essentiel", "débuter", "minuscule"]), ["relie"], 1, "B", alpha=True, sol="important → essentiel · petit → minuscule · commencer → débuter · finir → terminer")
    e3 = E("Je recopie les symboles et leur sens.", '<div class="card" style="background:#F2F6FD"><p class="big" style="margin:0">+ = et · → = donc · ≠ = différent · ex. = par exemple</p></div>' + lines(1), ["recopie"], 1, "C", alpha=True, sol="Copie exacte.")
    b.page(CP.format(t="Remplacer et reformuler") + e + e2 + e3, "★ Coup de pouce")
    e = E("Je résume ma journée en 3 phrases : d'abord… ensuite… enfin…", '<p class="big" style="line-height:2.1">D\'abord, ______________________ .<br>Ensuite, ______________________ .<br>Enfin, ______________________ .</p>', ["complete"], 1, "C", alpha=True, sol="Trois phrases simples avec les connecteurs.")
    e2 = E("Je dis à la prof, en une phrase, de quoi parle le texte des abeilles.", '<div class="card big c">Le texte parle des ______________ . Elles sont ______________ .</div>', ["parle"], 1, "A", alpha=True, sol="… des abeilles. Elles sont utiles (menacées).")
    e3 = E("Résumé ou pas résumé ? Je coche.", compact(table(["", "court ✅", "trop long ❌"], [["« Les abeilles font du miel et aident les fleurs. »", '<span class="chk"></span>', '<span class="chk"></span>'], ["« Les abeilles, qui sont jaunes et noires, qui volent, qui ont des ailes, qui… »", '<span class="chk"></span>', '<span class="chk"></span>']], ["120mm", "30mm", "32mm"])), ["lis", "coche"], 1, "B", alpha=True, sol="court ✅ · trop long ❌")
    e4 = E("Je trouve un titre court pour l'histoire.", '<div class="card big" style="line-height:1.9">Tom perd son chien au parc. Il le cherche partout. Le soir, le chien revient à la maison.</div><p class="big">Titre : ______________________</p>', ["lis", "ecris"], 1, "C", alpha=True, sol="Ex. : Le chien perdu. / Tom et son chien.")
    b.page(CP.format(t="Je résume ma journée") + e + e2 + e3 + e4, "★ Coup de pouce")

    # ---------- Tâche finale ----------
    e = E("Avec mon groupe, je choisis un thème et je rassemble trois documents (manuel, article, infographie, vidéo) avec l'aide de la prof.", '<p class="sm" style="margin:0 0 1mm">Thèmes possibles : ☐ les abeilles (documents du module) ☐ le sommeil des ados (module 13) ☐ le GSM à l\'école (module 7) ☐ un autre thème choisi avec la prof : ______________</p>' +
          tall(compact(table(["Notre dossier", "Ce que nous décidons", "✅"], [["La question de la synthèse", "", '<span class="chk"></span>'], ["Document 1 (titre, source)", "", '<span class="chk"></span>'], ["Document 2 (titre, source)", "", '<span class="chk"></span>'], ["Document 3 (titre, source)", "", '<span class="chk"></span>'], ["Qui fait quoi ? (lecture, notes, rédaction, présentation)", "", '<span class="chk"></span>']], ["62mm", "104mm", "16mm"])), 16) +
          f'<div class="mt2">{entonnoir()}</div>', ["lis", "ecris", "groupe"], 2, "C",
          sol="Question claire, trois documents variés et fiables, sources notées, rôles répartis.")
    b.page(tache_head("Notre synthèse de documents", "Chaque groupe lit trois documents sur un même thème, remplit un tableau de confrontation, rédige une synthèse d'une page et la présente oralement à une autre classe en 3 minutes, avec une affiche ou un diaporama.") + e, "Tâche finale", levels=False)
    e = E("Je complète le tableau de confrontation de nos trois documents.", confrontation([("Idée 1 :", None), ("Idée 2 :", None), ("Idée 3 :", None), ("Ce qui est différent", None), ("Ce que chacun ajoute", None)], vide=True, h=17), ["lis", "ecris"], 2, "C",
          sol="Tableau rempli en mots-clés, une ligne par idée, une colonne par document.")
    e2 = E("Notre plan (par thèmes, pas par documents).", '<div class="card" style="line-height:2.1">Introduction : ______________________________________<br>I. ______________________________________<br>II. ______________________________________<br>III. ______________________________________<br>Conclusion : ______________________________________</div>', ["ecris"], 2, "C",
           sol="Plan thématique cohérent avec la question.")
    b.page(e + e2, "Tâche finale", levels=False)
    e = E("Le jour de la présentation : j'évalue la présentation d'un autre groupe.", chk3(["La question et les documents sont présentés.", "Les idées sont regroupées par thèmes.", "Les orateurs parlent à partir de notes (ils ne lisent pas tout).", "La conclusion répond à la question."]) + f'<p class="sm mt2">Ce que j\'ai appris : {blank("xl")}</p>', ["ecoute", "coche"], 1, "A",
          sol="Grille remplie ; une information apprise, formulée en phrase complète.")
    e2 = E("Après la présentation : je m'auto-évalue et j'écris ce que nous ferions mieux (au conditionnel).", chk3(["J'ai lu les documents et pris des notes.", "J'ai participé à la rédaction de la synthèse.", "J'ai présenté ma partie sans lire."]) + lines(2), ["ecris", "coche"], 1, "C",
           sol="Auto-évaluation ; objectif au conditionnel (ex. : La prochaine fois, nous choisirions des documents plus différents.).")
    b.page(compact(table(["Je vérifie avant de rendre la synthèse :", "✅"], [[x, '<span class="chk"></span>'] for x in ["Elle tient sur une page (environ 200 mots).", "Elle confronte les trois documents (selon…, de même, en revanche).", "Je n'ai pas recopié de phrases : j'ai reformulé.", "Il n'y a pas d'opinion personnelle.", "Les sources sont indiquées."]], ["160mm", "22mm"])) + e + e2, "Tâche finale", levels=False)
    e = E("Je révise.", '<p>1. Dire la même chose avec d\'autres mots : ______________ . 2. Un texte court qui garde l\'essentiel d\'un seul texte : un ______________ . 3. Rassembler plusieurs documents : une ______________ . 4. Le texte qui rapporte une visite ou une réunion : un ______________ . 5. « Ce phénomène » est une reprise ______________ . 6. Un résumé fait environ le ______________ du texte. 7. Le symbole « ↘ » signifie ______________ .</p>', ["complete"], 1, "C",
          sol="1. reformuler — 2. résumé — 3. synthèse — 4. compte rendu — 5. résomptive — 6. quart (¼) — 7. diminue")
    e2 = E("Je corrige le résumé de Mateo : 5 erreurs (opinion, citation, détail, répétition, ordre).", '<div class="card" style="font-family:\'Comic Sans MS\',cursive;background:#fff;font-size:10.3pt">« À mon avis, les abeilles sont géniales. Les abeilles font du miel. « Elles transportent le pollen d\'une fleur à l\'autre. » Les abeilles ont des poils et des rayures jaunes. Les abeilles vivent dans une ruche avec une reine. »</div>' + lines(4), ["lis", "ecris"], 2, "C",
           sol="Supprimer l'opinion « À mon avis… géniales » · ne pas citer : reformuler la phrase entre guillemets · supprimer le détail (poils, rayures) · remplacer « les abeilles » répété par des substituts (elles, ces insectes) · respecter l'ordre du texte : d'abord la colonie, puis le miel, puis la pollinisation.")
    e3 = E("Défi ! Je complète la carte mentale du module : un mot ou un exemple par branche.", tall(compact(table(["Branche", "Mes mots / mes exemples"], [["repérer l'essentiel", ""], ["prendre des notes (symboles)", ""], ["reformuler (procédés)", ""], ["les substituts", ""], ["le résumé et le compte rendu", ""], ["la synthèse de documents", ""]], ["66mm", "116mm"])), 11), ["lis", "ecris"], 3, "C",
           sol="Productions variées ; vérifier un exemple juste par branche (ex. : substitut : ce pollinisateur ; reformuler : nominalisation disparaître → la disparition).")
    b.page(f'<h2>🔁 Je révise tout le module</h2>{e}{e2}{e3}', "Je révise")

    # ---------- Test ----------
    Q = [("Dire la même chose avec d'autres mots, c'est…", ["reformuler", "paraphraser", "citer", "relever"]), ("Un texte qui rassemble les informations de plusieurs documents est…", ["une synthèse", "un résumé", "une citation", "une réplique"]),
         ("Un résumé fait environ…", ["le quart du texte", "le double du texte", "la même longueur", "une seule ligne"]), ("Dans un résumé, on peut…", ["reformuler avec ses mots", "donner son avis", "recopier des phrases", "ajouter des exemples"]),
         ("L'idée principale d'un paragraphe se trouve souvent…", ["dans la première phrase", "dans un exemple", "dans un chiffre", "dans la ponctuation"]), ("Le symbole « → » signifie…", ["entraîne", "différent", "environ", "diminue"]),
         ("« ≠ » signifie…", ["différent de", "égal à", "augmente", "par exemple"]), ("Le nom correspondant à « disparaître » est…", ["la disparition", "le disparu", "disparaissant", "la disparaison"]),
         ("Synonyme de « menacé » :", ["en danger", "protégé", "nombreux", "utile"]), ("« Les abeilles pollinisent les fleurs » au passif :", ["Les fleurs sont pollinisées par les abeilles.", "Les fleurs pollinisent les abeilles.", "Les abeilles sont pollinisées.", "Les fleurs ont pollinisé."]),
         ("« Ce phénomène » dans « Les abeilles disparaissent. Ce phénomène inquiète. » est…", ["une reprise résomptive", "un pronom personnel", "une citation", "un verbe"]), ("Un terme générique pour « abeille, bourdon, papillon » :", ["des insectes", "des oiseaux", "des fleurs", "des ruches"]),
         ("« Les fleurs ? Les abeilles … trouvent du nectar. »", ["y", "en", "le", "lui"]), ("Un compte rendu de visite commence par…", ["quoi, quand, où, qui", "mon opinion", "la conclusion", "une question"]),
         ("Pour rapporter des paroles dans un compte rendu : « Mme Renard … que les abeilles sont utiles. »", ["explique", "explique-t-elle", "expliquer", "explication"]), ("Dans une synthèse, le plan est organisé…", ["par thèmes", "par documents", "au hasard", "par ordre alphabétique"]),
         ("Connecteur qui marque une différence :", ["en revanche", "de même", "également", "aussi"]), ("En Belgique, on compte environ … espèces d'abeilles sauvages.", ["400", "4", "40", "40 000"]),
         ("« résumé » se prononce avec…", ["[z]", "[s]", "[ʃ]", "[ʒ]"]), ("🔁 Types de phrases : « Que c'est beau ! » est…", ["exclamative", "interrogative", "impérative", "déclarative"])]
    ans = [q[1][0] for q in Q]
    qrot = [3, 1, 0, 2, 1, 3, 2, 0, 3, 1, 2, 0, 1, 3, 0, 2, 1, 3, 0, 2]
    Q = [(q, o[r:] + o[:r]) for (q, o), r in zip(Q, qrot)]
    key = key_from(Q, ans)
    test_pages(b, 15, "Résumer, synthétiser", Q, f'<h3>B1. Reformule : « Les abeilles disparaissent à cause des pesticides. » (nominalisation) · « Mme Renard a douze ruches. Mme Renard aime ses abeilles. » (substitut) (… / 2)</h3><p>{blank("xl")}</p><p>{blank("xl")}</p><h3>B2. Prends des notes (mots-clés et symboles) : « Le nombre de bourdons diminue en Europe, notamment à cause du changement climatique. » (… / 1)</h3><p>{blank("xl")}</p><h3>B3. Résume en 30 à 40 mots le texte « Le fauchage tardif » (p. {P["resume"] + 2}) ou un autre texte donné par la prof. Indique le nombre de mots. (… / 7)</h3>{lines(6, True)}',
               [["résumer oralement un texte court en 30 secondes", "/ 4", ""], ["expliquer la différence entre résumé et synthèse", "/ 3", ""], ["reformuler une phrase donnée par la prof", "/ 3", ""]],
               '<h3>1. Je relie le mot et le dessin. (… / 4)</h3>' + relie(["le miel", "une abeille", "une fleur", "un fruit"], ["🌼", "🍎", "🍯", "🐝"]) + '<h3>2. J\'entoure la phrase la plus importante. (… / 4)</h3><div class="card big">Les abeilles sont utiles. Elles ont six pattes. Elles aiment le soleil.</div><h3>3. Je remplace le mot souligné : <u>Les abeilles</u> font du miel. → ______ font du miel. (… / 4)</h3><h3>4. Je complète : D\'______, je lis. Ensuite, j\'écris. ______, je relis. (… / 3)</h3><h3>5. Oral : je dis en une phrase de quoi parle un texte lu en classe. (… / 5)</h3>')
    closing(b, 15, ["Je repère le thème, l'idée principale et les mots-clés d'un texte.", "Je prends des notes avec des abréviations et des symboles.", "Je reformule (synonymes, nominalisation, passif).", "J'utilise des substituts variés et clairs.", "Je fais la différence entre reformuler et paraphraser.", "Je résume un texte en respectant les règles.",
                    "Je rédige un compte rendu (visite, réunion).", "Je confronte plusieurs documents dans un tableau.", "Je rédige une synthèse organisée par thèmes.", "Je résume oralement un texte ou un film.", "Je présente une synthèse à partir de mes notes."],
            [("✂️", "résumer, un résumé"), ("🧩", "synthétiser, une synthèse"), ("🗒️", "un compte rendu"), ("🔄", "reformuler"), ("🔍", "l'essentiel"), ("💡", "l'idée principale"), ("🔑", "un mot-clé"), ("🖍️", "surligner"), ("📝", "prendre des notes"), ("➡️", "un symbole, une abréviation"), ("🔗", "un substitut"), ("🎩", "un terme générique"),
             ("📄", "un document, une source"), ("⚖️", "confronter, comparer"), ("📊", "un tableau de confrontation"), ("🗂️", "un plan"), ("🐝", "une abeille, un pollinisateur"), ("🏠", "une ruche, une colonie"), ("🌼", "le nectar, le pollen"), ("🌸", "la pollinisation"), ("🍯", "le miel, butiner"), ("📉", "le déclin, diminuer"), ("🛡️", "protéger, la protection"), ("👩‍🌾", "un apiculteur, une apicultrice")])
    plan_de_travail(b, E, 15, ["Repérer l'essentiel, prendre des notes", "Reformuler", "Les substituts", "Le résumé et le compte rendu", "La synthèse de documents"], "☐ Thème et documents<br>☐ Tableau de confrontation<br>☐ Synthèse rédigée<br>☐ Présentation orale")
    b.pages = [x.replace("padding:.8mm 1.5mm;display:flex", "padding:.3mm 1.5mm;display:flex").replace("repeat(7,1fr);gap:1.3mm", "repeat(7,1fr);gap:.7mm").replace("align-items:center;justify-content:space-between;font-size:8.5pt", "align-items:center;justify-content:space-between;font-size:8pt") for x in b.pages]  # plan compact
    if render:
        to_pdf(b.html(), '/home/claude/syllabus/out/V3_M15_eleve.pdf')

    pg, exs = helpers(b, E)
    CPp = b.marks["★ Coup de pouce"]
    days = [("1", "Collectif", f"Ouverture · BD · document 1 et pollinisation ({pg('Découvrir')})", f"CP l'essentiel (p. {CPp[0]})"), ("2", "Collectif + duo", f"Lexique : résumer, synthétiser, abeilles ({pg('Lexique')})", "CP l'essentiel"),
            ("3", "Rotation", f"📌 Leçon 1 repérer l'essentiel, prendre des notes ({pg('Leçon 1')})", "Fiche de symboles agrandie"), ("4", "Collectif", f"📌 Leçon 2 reformuler ({pg('Leçon 2')}) · sons ({pg('Sons')})", f"CP reformuler (p. {CPp[1]})"),
            ("5", "Rotation", f"📌 Leçon 3 substituts ({pg('Leçon 3')})", "CP il, elle, ils"), ("6", "Collectif", f"📌 Leçon 4 résumé et compte rendu ({pg('Consignes & école')}) · documents ({pg('Document de la vie')})", f"CP ma journée (p. {CPp[2]})"),
            ("7", "Rotation", f"📌 Leçon 5 synthèse de documents ({pg('Leçon 5')}) · CE1D, DELF ({pg('Vers les épreuves')})", "Tableau de confrontation prérempli"), ("8", "Ateliers", f"Ateliers : oral, notes, synthèse, jeux ({pg('Atelier')})", "Résumé oral guidé"),
            ("9", "Groupes", f"Tâche finale : synthèse et présentation ({pg('Tâche finale')})", "Rôle de lecteur-noteur"), ("10", "Seul", f"Test ({pg('Test')})", f"CP test ({pg('★ Coup de pouce · Test')})")]
    rot = [["🎧 Écouter-Parler", "Téléphone arabe du résumé + exposé flash", "30 min", "Comparaison avec le texte"], ["📖 Lire", "Les vers de terre : notes et résumé", "25 min", "Grille entre pairs"], ["✏️ Écrire", "Synthèse sur les abeilles", "30 min", "Grille de relecture"],
           ["🧩 Jouer", "« La course au résumé », titre en 5 mots, mot interdit", "20 min", "Les joueurs vérifient"], ["👩‍🏫 Table d'appui", "Coup de pouce · essentiel, substituts, résumé guidé", "20 min", "—"]]
    ev1 = f'''<h3>Partie B (10 points)</h3><p class="sm"><b>B1</b> : <span class="sol">La disparition des abeilles est due aux pesticides. · Mme Renard a douze ruches. Elle aime ses abeilles (Cette apicultrice…).</span> (1 pt chacune). · <b>B2</b> : <span class="sol">bourdons ↘ Europe ← changement climatique</span> (1 pt). · <b>B3</b> : essentiel conservé (3), mots personnels, sans citation ni opinion (2), longueur respectée et indiquée (1), langue (1).</p>
<h3>Partie C · oral (10 points)</h3><p class="sm">L'élève résume en 30 secondes un texte court lu devant lui (4) · il explique la différence entre résumé et synthèse avec un exemple (3) · il reformule une phrase donnée par la prof avec un procédé au choix (3).</p>
<h3>Test ★ Coup de pouce (20 points)</h3><p class="sm"><b>1 :</b> <span class="sol">miel → 🍯 · abeille → 🐝 · fleur → 🌼 · fruit → 🍎</span> (4) · <b>2 :</b> <span class="sol">Les abeilles sont utiles.</span> (4) · <b>3 :</b> <span class="sol">Elles</span> (4) · <b>4 :</b> <span class="sol">abord · Enfin</span> (3) · <b>5 :</b> une phrase compréhensible (5).</p>
<h3>Lire les résultats du QCM : quelle remédiation ?</h3>{table(["Questions", "Compétence", "Si moins de la moitié est juste…"], [["1 à 5", "résumé, synthèse, idée principale", f"leçons 1 et 4 ({pg('Leçon 1')}, {pg('Consignes & école')}) + coup de pouce p. {CPp[0]}"], ["6 et 7", "prise de notes", f"leçon 1 ({pg('Leçon 1')})"], ["8 à 10", "reformuler", f"leçon 2 ({pg('Leçon 2')}) + coup de pouce p. {CPp[1]}"], ["11 à 13", "les substituts", f"leçon 3 ({pg('Leçon 3')})"], ["14 à 17", "compte rendu et synthèse", f"leçons 4 et 5 ({pg('Consignes & école')}, {pg('Leçon 5')})"], ["18", "les abeilles (contenu)", f"documents ({pg('Découvrir')}, {pg('Leçon 5')})"], ["19", "[s] / [z]", f"sons ({pg('Sons')})"], ["20", "révision (types de phrases)", "module 14"]], ["24mm", "62mm", "96mm"])}'''
    ev2 = f'''<h2>Grille · tâche finale « Notre synthèse de documents »</h2>{table(["Critère", "Très bien", "Bien", "À retravailler", "Points"], [["<b>Tableau de confrontation</b> : idées en mots-clés, trois documents", "Complet", "Partiel", "Absent", "/ 3"], ["<b>Organisation</b> : introduction, plan par thèmes, conclusion qui répond", "Claire", "Partielle", "Juxtaposition", "/ 4"], ["<b>Confrontation</b> : selon…, de même, en revanche", "Systématique", "Ponctuelle", "Absente", "/ 3"], ["<b>Langue</b> : reformulation, substituts, pas de citation ni d'opinion", "Maîtrisée", "Quelques maladresses", "Recopie", "/ 4"], ["<b>Présentation orale</b> : à partir de notes, clarté, durée", "Aisée", "Correcte", "Lue", "/ 4"], ["<b>Sources</b> indiquées", "Toutes", "Certaines", "Aucune", "/ 2"]], ["66mm", "30mm", "30mm", "34mm", "22mm"])}
<h2 class="mt4">Différencier et remédier</h2>{table(["Difficulté", "Remédiation"], [["Trouver l'idée principale", "Question guide par paragraphe (« Que veut dire l'auteur ? ») ; choisir entre trois propositions ; surligner une seule phrase par paragraphe."], ["Recopier au lieu de reformuler", "Résumer texte caché, à partir des notes seulement ; banque de synonymes ; règle « jamais plus de trois mots à la suite du texte »."], ["Substituts", "Chaîne de couleurs : surligner toutes les reprises d'un même référent ; jeu « mot interdit »."], ["Synthèse = résumés juxtaposés", "Tableau de confrontation obligatoire ; plan par thèmes donné ; connecteurs de comparaison affichés."], ["Élève rapide", "Synthèse de quatre documents dont un graphique ; compte rendu d'une émission radio ; préparation de l'épreuve de synthèse du CE1D ou de la compréhension DELF B1."]], ["50mm", "132mm"])}'''
    rep = f'''<h2>Résumer et synthétiser : repères</h2>
<div class="attention"><b>Points d'attention.</b> Résumer suppose de comprendre finement le texte : pour les élèves encore fragiles, travailler d'abord à l'oral (raconter un film, une journée) et sur des textes très courts. La peur des abeilles et les allergies aux piqûres sont fréquentes : se renseigner avant toute visite de rucher (trousse de secours, élèves allergiques signalés). Valoriser les savoirs des élèves : apiculture et miel existent dans de nombreuses cultures (plusieurs élèves peuvent en parler).</div>
{table(["Repère", "Ce qu'il faut savoir (vérifié en novembre 2026)"], [["Les abeilles", "Abeille mellifère (Apis mellifera) : colonie avec une reine, des ouvrières (jusqu'à plusieurs dizaines de milliers en été) et des mâles. Belgique : environ 400 espèces d'abeilles sauvages, en majorité solitaires, dont une part importante est menacée (liste rouge). FAO : environ 75 % des principales cultures alimentaires dépendent au moins en partie des pollinisateurs. Menaces : perte d'habitats et de fleurs, pesticides, changement climatique, parasites (varroa), frelon asiatique, concurrence entre abeilles domestiques et sauvages quand les ruches sont trop nombreuses."], ["Initiatives", "Journée mondiale des abeilles : 20 mai (proclamée par l'ONU en 2017, célébrée depuis 2018). Wallonie : espaces publics gérés sans pesticides chimiques depuis le 1er juin 2019 ; programme de fauchage tardif des bords de routes dans de nombreuses communes."], ["Le résumé à l'école", "Compétence travaillée au CE1D et au CESS ; règles habituelles : environ ¼ (ou un nombre de mots imposé), respect de l'ordre et de l'énonciation du texte, reformulation, pas de jugement personnel. Au DELF B1, pas de résumé, mais la compréhension écrite et orale demande de repérer l'essentiel."]], ["40mm", "142mm"])}
<div class="attention mt2"><b>Fictif :</b> le rucher pédagogique du parc de Hautrive, Mme Renard, le dépliant et ses tarifs, le compte rendu du conseil des élèves, l'infographie du document 3 (conseils inspirés de ceux d'associations réelles), le reportage radio (Liège), le film « Le Chien du port ». Les faits sur les abeilles, le moustique tigre, les vers de terre, le fauchage tardif, la gestion sans pesticides en Wallonie et la Journée mondiale des abeilles sont réels.</div>
<h3>Belgicismes du module</h3><p class="sm">le <b>conseil des élèves</b> · le <b>local</b> (France : la salle) · le <b>réfectoire</b> · le <b>fauchage tardif</b> (programme wallon) · <b>septante</b>, <b>nonante</b> · une <b>farde</b> pour classer les documents (France : une chemise).</p>'''
    import re as _re
    def _court(t, n=90):
        t2 = _re.sub(r"<[^>]+>", "", t)
        return t if len(t2) <= n else t2[:n].rsplit(" ", 1)[0] + "…"
    E.sols = [(p, n, _court(t), s) for p, n, t, s in E.sols]
    E.scripts = [(p, n, _court(t, 50), s) for p, n, t, s in E.scripts]
    import lib.module as _LM
    _pg = _LM.paginate
    _LM.paginate = lambda rows, w, bf, bb: _pg(rows, w, bf + (SCR if bf == 190 else BUMP), bb + BUMP)
    _tb = _LM.table
    _LM.table = lambda *a, **k: compact(_tb(*a, **k))
    T = teacher_book(b, E, "V3 · M15", "", MC, 15, "Résumer, synthétiser",
                     "<li><b>Communication :</b> repérer l'essentiel d'un texte ; prendre des notes ; résumer un texte et un film ; rédiger un compte rendu (visite, réunion) ; faire la synthèse de plusieurs documents et la présenter.</li><li><b>Lexique :</b> les mots du résumé et de la synthèse (essentiel, idée principale, mot-clé, reformuler, condenser, source, confronter) ; les abeilles et la pollinisation.</li><li><b>Langue :</b> la reformulation (synonymes, termes génériques, nominalisation, passif, regroupement) ; les substituts (pronoms dont en et y, synonymes, termes génériques, périphrases, reprises résomptives) ; les verbes introducteurs du discours rapporté ; les connecteurs de comparaison.</li><li><b>Oral :</b> [s] / [z] ; groupes de souffle ; résumer à l'oral.</li><li><b>FLSco :</b> le résumé (règles, entonnoir) et le compte rendu ; la synthèse de documents (tableau de confrontation, plan thématique) ; sciences (pollinisation).</li><li><b>Épreuves :</b> CE1D (résumé d'un texte documentaire : le moustique tigre) ; DELF B1 compréhension de l'oral (reportage).</li><li><b>Documents :</b> dépliant d'un rucher pédagogique, compte rendu de réunion, trois documents sur les abeilles (texte, article, infographie).</li>",
                     '<p class="sm"><b style="color:#E4572E">Indispensable</b> : trouver l\'idée principale, résumer en une phrase, pronoms substituts, quelques symboles de prise de notes.</p><p class="sm"><b style="color:#d9a400">Important</b> : règles du résumé, reformulation (nominalisation, synonymes), compte rendu, tableau de confrontation.</p><p class="sm"><b style="color:#2BA88F">Enrichissement</b> : reprises résomptives, synthèse rédigée complète, CE1D, DELF B1.</p>',
                     "Un exemplaire du cahier par élève · surligneurs de trois couleurs · cartes de textes courts (100 mots) pour le téléphone arabe · chronomètre · si possible, une visite d'un rucher (pédagogique, communal ou d'un apiculteur local) ou une ruche vitrée en vidéo · dés et pions pour « La course au résumé ».", "<b>Avant de commencer :</b> le module mobilise tous les modules précédents (lecture de textes documentaires, nominalisation, discours rapporté) : c'est une excellente préparation à la passerelle (module 16) et aux épreuves. Si une visite est prévue, vérifier les allergies et la météo ; sinon, la BD et le dépliant permettent de travailler sans sortie. Prévoir des textes d'autres cours (sciences, histoire) pour les résumés : c'est là que la compétence sera la plus utile.",
                     days, "« Le titre en 5 mots » : un court article, chacun propose un titre · « Le symbole du jour » : une abréviation au tableau à réutiliser dans la journée · « Un film en une phrase » : un élève résume un film, la classe vérifie l'essentiel.", rot, key, (ev1, ev2), extra_pages=[(rep, "Repères")], start=tstart)
    _LM.paginate = _pg
    _LM.table = _tb
    if render:
        to_pdf(T.html(), '/home/claude/syllabus/out/V3_M15_prof.pdf')
    return b, T


if __name__ == "__main__":
    b, T = build_v3m15()
    print(b.n, T.n)
