"""Volume 3 · Module 10 « Poésie et chanson » (B1 + français de scolarisation).

Lire, dire et écrire un poème : vers, strophes, rimes, syllabes, images (comparaison, métaphore, personnification),
sons (allitération, assonance, anaphore, refrain). Poèmes du domaine public : Verlaine (VERLAINE), Hugo (HUGO),
Desbordes-Valmore (SAADI), Apollinaire (MIRABEAU, 1re strophe), chanson traditionnelle « À la claire fontaine ».
Slam et poèmes originaux écrits pour la classe. Visuels : poeme() (mise en page de poème avec rimes colorées),
syllabes() (découpage des syllabes), calligramme() (exemple de calligramme en SVG).
"""
import sys
sys.path.insert(0, '/home/claude/syllabus')
from lib.base import *
from lib.art import *
from lib.module import *
from lib.v3 import CP, CPCOL, EPR, disc_tag
from lib.render import to_pdf

import os
BUMP = int(os.environ.get("BUMP", "28"))
MC = "#9C2E5E"
TINT = "#F8E8EF"
SERIF = "font-family:'DejaVu Serif';line-height:1.55"
F = disc_tag("français")


def chk3(items, w=128):
    return table(["", "😀", "🙂", "😕"], [[x, '<span class="chk"></span>', '<span class="chk"></span>', '<span class="chk"></span>'] for x in items], [f"{w}mm", "18mm", "18mm", "18mm"])


def tall(html, h):
    return html.replace("<td></td>", f'<td style="height:{h}mm"></td>')


def compact(html):
    return html.replace('class="t"', 'class="t compact"')


RC = {"A": "#E4572E", "B": "#4A7BD1", "C": "#2BA88F", "D": "#9B5DE5", "E": "#D1495B", "F": "#F29E4C"}


def poeme(titre, auteur, strophes, fs=10.5, rimes=None, num=False, note=""):
    """Poème : strophes = liste de listes de vers ; rimes = liste parallèle de lettres (A, B…) à afficher en couleur."""
    out, k = "", 0
    for si, st in enumerate(strophes):
        lines_ = ""
        for vi, v in enumerate(st):
            k += 1
            r = rimes[si][vi] if rimes else ""
            tag = f'<b style="color:{RC.get(r, "#555")};font-family:Poppins;font-size:8pt;margin-left:2mm">{r}</b>' if r else ""
            n = f'<span class="xs muted" style="display:inline-block;width:6mm;font-family:Poppins">{k}</span>' if num else ""
            lines_ += f'<div>{n}{v}{tag}</div>'
        out += f'<div style="margin-bottom:2mm">{lines_}</div>'
    return (f'<div class="card" style="{SERIF};background:#FFFCF5;border:1.5px solid #d8c9a8;font-size:{fs}pt;padding:3mm 5mm">'
            f'<div style="font-family:Poppins;margin-bottom:1.5mm">{F} <b style="color:{MC}">{titre}</b> <span class="xs muted">— {auteur}</span></div>{out}'
            + (f'<div class="xs muted" style="font-family:Poppins">{note}</div>' if note else "") + '</div>')


VERLAINE = [["Il pleure dans mon cœur", "Comme il pleut sur la ville ;", "Quelle est cette langueur", "Qui pénètre mon cœur ?"],
            ["Ô bruit doux de la pluie", "Par terre et sur les toits !", "Pour un cœur qui s'ennuie,", "Ô le chant de la pluie !"],
            ["Il pleure sans raison", "Dans ce cœur qui s'écœure.", "Quoi ! nulle trahison ?…", "Ce deuil est sans raison."],
            ["C'est bien la pire peine", "De ne savoir pourquoi", "Sans amour et sans haine", "Mon cœur a tant de peine !"]]
VERLAINE_R = [list("ABAA"), list("CDCC"), list("EFEE"), list("GHGG")]

HUGO = [["Demain, dès l'aube, à l'heure où blanchit la campagne,", "Je partirai. Vois-tu, je sais que tu m'attends.", "J'irai par la forêt, j'irai par la montagne.", "Je ne puis demeurer loin de toi plus longtemps."],
        ["Je marcherai les yeux fixés sur mes pensées,", "Sans rien voir au dehors, sans entendre aucun bruit,", "Seul, inconnu, le dos courbé, les mains croisées,", "Triste, et le jour pour moi sera comme la nuit."],
        ["Je ne regarderai ni l'or du soir qui tombe,", "Ni les voiles au loin descendant vers Harfleur,", "Et quand j'arriverai, je mettrai sur ta tombe", "Un bouquet de houx vert et de bruyère en fleur."]]

SAADI = [["J'ai voulu ce matin te rapporter des roses ;", "Mais j'en avais tant pris dans mes ceintures closes", "Que les nœuds trop serrés n'ont pu les contenir."],
         ["Les nœuds ont éclaté. Les roses envolées", "Dans le vent, à la mer s'en sont toutes allées.", "Elles ont suivi l'eau pour ne plus revenir ;"],
         ["La vague en a paru rouge et comme enflammée.", "Ce soir, ma robe encore en est tout embaumée…", "Respires-en sur moi l'odorant souvenir."]]
SAADI_R = [list("AAB"), list("CCB"), list("DDB")]

MIRABEAU = [["Sous le pont Mirabeau coule la Seine", "Et nos amours", "Faut-il qu'il m'en souvienne", "La joie venait toujours après la peine"], ["Vienne la nuit sonne l'heure", "Les jours s'en vont je demeure"]]

FONTAINE = [["À la claire fontaine", "M'en allant promener", "J'ai trouvé l'eau si belle", "Que je m'y suis baigné."], ["Il y a longtemps que je t'aime,", "Jamais je ne t'oublierai."]]

SLAM = [["J'ai deux langues dans la bouche, et aucune ne se tait,", "L'une sent le pain du matin, l'autre le café,", "L'une dit « maman », l'autre dit « madame »,", "Et entre les deux, je construis mon âme."],
        ["On m'a dit : « Choisis ! » Comme on choisit un train.", "Mais je ne suis pas une gare, je suis un chemin.", "Mes mots sont des valises, mes phrases des ponts,", "Je traverse la Meuse avec mes chansons."],
        ["Alors écoute-moi bien, toi qui me trouves étrange :", "Mon accent n'est pas une faute, c'est un mélange.", "J'ai deux langues dans la bouche, et je les garde, les deux :", "Avec une, je parle ; avec deux, je rêve mieux."]]


def syllabes(vers, coupes):
    """Affiche un vers découpé en syllabes (coupes = liste des syllabes)."""
    cells = "".join(f'<span style="display:inline-block;border:1.2px solid {MC};border-radius:1.2mm;padding:.5mm 1.4mm;margin:.4mm;font-size:10pt;background:#fff">{c}<sup class="xs" style="color:{MC};margin-left:.5mm">{i}</sup></span>' for i, c in enumerate(coupes, 1))
    return f'<div class="card" style="padding:2mm 3mm"><div class="sm" style="{SERIF}">« {vers} »</div><div style="margin-top:1mm">{cells}</div></div>'


def calligramme(w=60):
    """Calligramme original : une goutte de pluie formée par le texte."""
    mots = ["il", "pleut", "des", "mots", "doux", "sur", "ma", "ville", "grise", "chaque", "goutte", "est", "une", "lettre", "qui", "tombe", "et", "qui", "chante", "tout", "bas", "pour", "moi"]
    rows = [1, 2, 2, 3, 3, 3, 3, 3, 2, 1]
    out, k, y = [], 0, 14
    for r in rows:
        line = " ".join(mots[k:k + r]); k += r
        out.append(f'<text x="50" y="{y}" font-size="7.2" text-anchor="middle" fill="#4A7BD1" font-family="DejaVu Serif">{line}</text>')
        y += 9
    return f'<svg viewBox="0 0 100 110" width="{w}mm" style="max-width:100%">{"".join(out)}</svg>'


def build_v3m10(start=1, tstart=1, render=True):
    b = Book("V3 · M10", "Volume 3 · Je réussis à l'école · Module 10 · Poésie et chanson", MC, start=start)
    E = Ex(b)
    P = {}
    vis = ('<div class="flex" style="justify-content:space-around;align-items:flex-end">' + avatar("daria", 80, "sourire") + '<div style="font-size:34pt">🎤 🌧️</div>' + avatar("mateo", 80, "rire")
           + '<div style="font-size:34pt">🌹 🎶</div>' + avatar("yonas", 80, "sourire") + avatar("prof", 80, "sourire") + '</div>')
    opening(b, MC, 10, "Poésie et chanson", vis, [("📜", "lire un poème : vers, strophes, rimes"), ("🔢", "compter les syllabes d'un vers"), ("🖼️", "reconnaître les images : comparaison, métaphore, personnification"),
            ("🎵", "entendre les sons : allitération, assonance, refrain"), ("🔍", "analyser un poème en quelques phrases"), ("🎤", "dire un poème ou un slam lors du récital de la classe")],
            ["Connais-tu un poème ou une chanson par cœur ? Dans quelle langue ?", "Le rap et le slam, est-ce de la poésie ?", "Pourquoi les gens écrivent-ils des poèmes ?"],
            ["un poème", "un vers", "une strophe", "une rime", "une syllabe", "une image", "une comparaison", "une métaphore", "un refrain", "réciter", "un récital"], TINT)

    # ---------- Découvrir ----------
    P["bd"] = b.n + 1
    bd = '<div class="grid2" style="gap:3mm">' + "".join([
        bd_case(1, lr("prof", ["Ce mois-ci, nous allons lire, dire et écrire de la poésie. À la fin, nous ferons un récital."], "mateo", ["De la poésie ? C'est pour les vieux, ça ! Moi, j'écoute du rap."], "sourire", "neutre")),
        bd_case(2, lr("prof", ["Le rap, c'est aussi de la poésie : des rimes, du rythme, des images…"], "mateo", ["Ah bon ? Alors je suis poète sans le savoir !"], "rire", "surpris")),
        bd_case(3, lr("daria", ["En Ukraine, on apprend beaucoup de poèmes par cœur. Je connais encore des vers de Taras Chevtchenko."], "yonas", ["Chez nous, en Érythrée, ma grand-mère chante des poèmes en tigrigna pendant les fêtes."], "sourire", "rire")),
        bd_case(4, lr("fatou", ["Moi, j'aime le slam. On dit ses textes sur scène, sans musique."], "educ", ["Il y a des scènes ouvertes de slam à Liège et à Bruxelles. Tout le monde peut monter sur scène !"], "rire", "sourire")),
        bd_case(5, lr("bilal", ["Mais comment on écrit un poème ? Il faut que ça rime ?"], "prof", ["Pas forcément ! Il faut surtout des images, des sons… et des émotions."], "pense", "sourire")),
        bd_case(6, lr("amina", ["Pour le récital, on pourrait dire des poèmes dans toutes nos langues !"], "prof", ["Magnifique idée : un poème en français, et un poème dans ta langue."], "rire", "rire")),
    ]) + '</div>'
    e = E("J'écoute et je lis la BD : poètes sans le savoir.", bd, ["ecoute", "lis"], 1, "A",
          script="Lire deux fois en changeant de voix, puis poser les questions de l'exercice suivant à l'oral. Tour de table : « Quel poème ou quelle chanson connais-tu par cœur ? »", sol="Activité orale.")
    b.page(f'<h2>Découvrir · Poètes sans le savoir</h2>{e}', "Découvrir")
    e = E("Je réponds par une phrase complète.", f'<p>1. Qu\'est-ce que la classe va faire à la fin du module ? {blank("xl")}</p><p>2. Pourquoi Mme Lambert dit-elle que le rap est de la poésie ? {blank("xl")}</p><p>3. Quelles traditions poétiques Daria et Yonas connaissent-ils ? {blank("xl")}</p><p>4. Qu\'est-ce que le slam, d\'après Fatou ? {blank("xl")}</p><p>5. Un poème doit-il rimer ? Que faut-il surtout ? {blank("xl")}</p>', ["lis", "ecris"], 1, "B",
          sol="1. Un récital (les élèves diront des poèmes). — 2. Parce qu'il y a des rimes, du rythme et des images. — 3. Daria : apprendre des poèmes par cœur (Taras Chevtchenko) ; Yonas : les poèmes chantés en tigrigna par sa grand-mère. — 4. Des textes dits sur scène, sans musique. — 5. Pas forcément ; il faut des images, des sons et des émotions.")
    e2 = E("Vrai ou faux ? Je coche et je corrige les phrases fausses.", vf(["Mateo aime la poésie depuis toujours.", "Il existe des scènes ouvertes de slam en Belgique.", "Un poème doit toujours rimer.", "Le récital sera seulement en français."]), ["lis", "coche"], 1, "B",
           sol="Faux (il pense que c'est pour les vieux) · Vrai · Faux (pas forcément) · Faux (aussi dans les langues des élèves)")
    e3 = E("La poésie dans ma langue. J'écris le titre (ou le premier vers) d'un poème ou d'une chanson que je connais, dans ma langue, et je le traduis en français.", lines(3), ["ecris"], 2, "C",
           sol="Production personnelle ; inviter l'élève à le dire à la classe et à expliquer le sens.")
    e4 = E("Mon rapport à la poésie. Je coche, puis je compare avec mon voisin.", table(["", "souvent", "parfois", "jamais"], [[x, '<span class="chk"></span>', '<span class="chk"></span>', '<span class="chk"></span>'] for x in ["J'écoute des chansons et je lis les paroles.", "J'apprends des textes par cœur.", "J'écris des textes, des chansons, des messages poétiques.", "J'écoute du rap ou du slam."]], ["110mm", "24mm", "24mm", "24mm"]).replace('class="t"', 'class="t compact"'), ["lis", "coche", "duo"], 1, "A",
           sol="Réponses personnelles.")
    b.page(f'{e}{e2}{e3}{e4}', "Découvrir")
    P["verl"] = b.n + 1
    e = E("J'écoute et je lis le poème de Paul Verlaine. Je réponds.", '<div class="grid2" style="grid-template-columns:1.05fr 1fr;gap:4mm;align-items:start">' + poeme("Il pleure dans mon cœur", "Paul Verlaine, <i>Romances sans paroles</i> (1874)", VERLAINE, 10.4, note="« Il pleut doucement sur la ville. » (Arthur Rimbaud), citation placée par Verlaine en tête du poème.") +
          f'<div><p>1. Quel temps fait-il ? {blank("l")}</p><p>2. Comment se sent le poète ? Relève 3 mots. {blank("l")}{blank("l")}</p><p>3. Sait-il pourquoi il est triste ? Recopie le vers qui le montre. {blank("l")}{blank("l")}</p><p>4. Quel mot revient le plus souvent ? Combien de fois ? {blank("l")}</p><p>5. Compare : « Il <b>pleure</b> dans mon cœur » / « Il <b>pleut</b> sur la ville ». Que remarques-tu ? {blank("l")}{blank("l")}</p></div></div>', ["ecoute", "lis", "ecris"], 2, "B",
          script="Lire le poème lentement, deux fois, en marquant la fin de chaque vers. Laisser un silence après la lecture. Demander : « Quelle couleur, quelle saison, quelle musique vous fait-il imaginer ? »",
          sol="1. Il pleut sur la ville. — 2. Triste, mélancolique : « pleure », « langueur », « s'ennuie », « deuil », « peine ». — 3. Non : « Il pleure sans raison » / « De ne savoir pourquoi ». — 4. « cœur » (6 fois, dont « s'écœure ») — accepter « peine » / « raison » (2 fois). — 5. Les deux verbes se ressemblent (pleurer / pleuvoir) : la pluie dehors = les larmes dedans ; le temps reflète l'émotion.")
    e2 = E("Et toi ? Quel temps correspond à ton humeur aujourd'hui ? J'écris 2 vers sur le modèle : « Il … dans mon cœur / Comme il … sur … ».", lines(2), ["ecris"], 2, "C",
           sol="Ex. : Il brille dans mon cœur / Comme il fait beau sur la mer. / Il gronde dans mon cœur / Comme l'orage sur Liège.")
    b.page(f'<h2>Découvrir · Un poème</h2>{e}{e2}', "Découvrir")

    # ---------- Lexique ----------
    e = E("Les mots de la poésie. Je lis l'encadré.", '<div class="grid2">' + "".join(f'<div class="card" style="background:#fff"><b>{t}</b><p class="sm" style="margin:1mm 0 0">{d}</p></div>' for t, d in [
        ("📜 Le poème", "un <b>poète</b>, une <b>poétesse</b> · un <b>poème</b> · un <b>recueil</b> de poèmes · un <b>vers</b> (une ligne du poème) · une <b>strophe</b> (un groupe de vers) · un <b>titre</b>"),
        ("🎵 La musique des mots", "la <b>rime</b> (le même son à la fin de deux vers) · le <b>rythme</b> · une <b>syllabe</b> · un <b>refrain</b> (des vers répétés) · un <b>couplet</b> (dans une chanson)"),
        ("🖼️ Les images", "une <b>image</b> · une <b>comparaison</b> · une <b>métaphore</b> · une <b>personnification</b> · un <b>symbole</b> (la colombe = la paix)"),
        ("🎤 Dire la poésie", "<b>lire à voix haute</b> · <b>réciter</b> (dire par cœur) · <b>déclamer</b> (dire avec force) · un <b>récital</b> · une <b>scène ouverte</b> · le <b>slam</b> · le <b>rap</b>")]) + '</div>', ["lis"], 1, "B", sol="Lecture de l'encadré.")
    e2 = E(f"J'observe le poème de Verlaine (p. {P['verl']}) et je complète.", '<div class="card" style="line-height:2">Ce poème a ______ strophes. Chaque strophe a ______ vers : c\'est un <b>quatrain</b>. Le poème a ______ vers en tout. Le premier vers et le dernier vers de chaque strophe se terminent par le même ______ : ils <b>riment</b>. Le poète s\'appelle ______________ ; le recueil s\'appelle ______________ .</div>', ["lis", "complete"], 1, "C",
           sol="4 strophes · 4 vers (quatrain) · 16 vers · son (mot) · Paul Verlaine · Romances sans paroles")
    e3 = E("Les noms des strophes. Je relie.", relie(["un distique", "un tercet", "un quatrain", "un quintil"], ["une strophe de 4 vers", "une strophe de 5 vers", "une strophe de 2 vers", "une strophe de 3 vers"]), ["lis", "relie"], 1, "B",
           sol="distique → 2 vers · tercet → 3 vers · quatrain → 4 vers · quintil → 5 vers")
    e4 = E("Chanson ou poème ? Je classe les mots : couplet · strophe · refrain · vers · mélodie · recueil · album · chanteur · poète.", tall(table(["🎶 surtout la chanson", "📜 surtout le poème", "les deux"], [["", "", ""]], ["60mm", "60mm", "62mm"]), 13), ["lis", "ecris"], 2, "C",
           sol="Chanson : couplet, mélodie, album, chanteur · Poème : strophe, recueil, poète · Les deux : refrain, vers")
    b.page(f'<h2>Les mots de la poésie</h2>{e}{e2}{e3}{e4}', "Lexique")
    e = E("Les mots des émotions poétiques. Je relie le mot et sa définition.", relie(["la mélancolie", "la nostalgie", "l'émerveillement", "la colère", "la tendresse", "l'espoir"], ["une douce affection pour quelqu'un", "une tristesse vague et douce, sans raison précise", "le fait de croire qu'un avenir meilleur est possible", "le regret d'un lieu ou d'un temps passés", "l'admiration devant quelque chose de beau", "un sentiment violent de révolte"]), ["lis", "relie"], 1, "B",
          sol="mélancolie → tristesse vague · nostalgie → regret du passé · émerveillement → admiration · colère → révolte · tendresse → douce affection · espoir → avenir meilleur")
    e2 = E("Quelle émotion domine ? Pour chaque vers, j'écris une émotion de l'exercice précédent.", '<div class="card" style="line-height:1.9">1. « Il pleure dans mon cœur / Comme il pleut sur la ville » ______________ 2. « Je pense à la maison de mon enfance, au jasmin de la cour » ______________ 3. « Ô ciel étoilé, que tu es beau ! » ______________ 4. « Demain, le soleil se lèvera pour nous » ______________</div>', ["lis", "ecris"], 2, "B",
           sol="1. la mélancolie — 2. la nostalgie — 3. l'émerveillement — 4. l'espoir")
    e3 = E("Les familles de mots. Je complète.", table(["Nom", "Verbe", "Adjectif"], [["la poésie", "—", ""], ["le rythme", "", "rythmé"], ["la rime", "", "—"], ["l'émotion", "émouvoir", ""], ["la musique", "—", ""]], ["60mm", "61mm", "61mm"]).replace("<td></td>", '<td style="height:7mm"></td>').replace('class="t"', 'class="t compact"'), ["complete"], 2, "C",
           sol="poétique · rythmer · rimer · émouvant / ému · musical")
    e4 = E("Défi ! J'écris 3 phrases pour expliquer ce que la poésie (ou une chanson) m'apporte, avec un mot des émotions.", lines(3), ["ecris"], 3, "C",
           sol="Ex. : Quand j'écoute la chanson préférée de ma mère, je ressens de la nostalgie. Elle me rappelle notre maison au pays. Pourtant, elle me donne aussi de l'espoir.")
    b.page(f'<h2>Les mots des émotions</h2>{e}{e2}{e3}{e4}', "Lexique")

    # ---------- Leçon 1 : vers, strophes, rimes ----------
    l1 = lecon("Le vers, la strophe et les rimes", '<p class="sm" style="margin-bottom:1.5mm">Un <b>vers</b> commence souvent par une <b>majuscule</b>, même au milieu d\'une phrase. Une <b>rime</b> = le même son à la fin de deux vers (on écoute le son, pas l\'orthographe : <i>temps / attends</i>). On note les rimes avec des lettres : A, B, C…</p>' +
        table(["Disposition", "Schéma", "Exemple de fins de vers"], [["rimes <b>plates</b> (suivies)", "A A B B", "roses / closes / envolées / allées"], ["rimes <b>croisées</b>", "A B A B", "campagne / attends / montagne / longtemps"], ["rimes <b>embrassées</b>", "A B B A", "ville / cœur / langueur / tranquille"]], ["50mm", "36mm", "96mm"]).replace('class="t"', 'class="t compact"') +
        '<div class="astuce" style="margin:2mm 0 0">🎧 <b>Rime pauvre, suffisante, riche :</b> un seul son commun (ami / joli : [i]) = pauvre ; deux sons (attends / longtemps : [tɑ̃]) = suffisante ; trois sons ou plus (vallée / allée : [ale]) = riche. Un poème sans rimes s\'écrit en <b>vers libres</b> (comme beaucoup de slams et de poèmes modernes).</div>')
    e = E("Je lis le poème de Marceline Desbordes-Valmore. J'écris la lettre de chaque rime à la fin des vers, puis je réponds.", '<div class="grid2" style="grid-template-columns:1.2fr 1fr;gap:4mm;align-items:start">' + poeme("Les roses de Saadi", "Marceline Desbordes-Valmore, <i>Poésies inédites</i> (1860)", SAADI, 10.2) +
          f'<div><p class="sm">1. Combien de strophes ? Comment s\'appellent-elles ? {blank()}</p><p class="sm">2. Schéma des rimes de la 1re strophe : ___ ___ ___</p><p class="sm">3. Quel son revient à la fin de chaque strophe ? {blank("s")}</p><p class="sm">4. Que voulait faire la poétesse ? Que s\'est-il passé ? {blank("l")}{blank("l")}</p><p class="sm">5. Que reste-t-il des roses le soir ? {blank("l")}</p></div></div>', ["lis", "ecris"], 2, "B",
          sol="1. Trois strophes de trois vers : des tercets. — 2. A A B (roses / closes / contenir ; puis C C B ; D D B). — 3. [iʁ] : contenir, revenir, souvenir. — 4. Rapporter des roses à quelqu'un qu'elle aime ; les nœuds ont éclaté, le vent a emporté les roses dans la mer. — 5. Leur parfum (sa robe est « embaumée ») : un « odorant souvenir ».")
    P["saadi"] = b.n + 1
    b.page(f'{l1}{e}', "Leçon 1")
    e = E("Plates, croisées ou embrassées ? J'écris le schéma et le nom.", '<div class="grid3" style="gap:2mm">' + "".join(f'<div class="card sm" style="background:#fff;{SERIF}">{x}<p style="font-family:Poppins;margin:1mm 0 0">Schéma : ______ <br>Rimes : ______________</p></div>' for x in ["Le chat dort sur le <b>toit</b>,<br>La lune veille sur la <b>ville</b>,<br>Le vent souffle sur le <b>bois</b>,<br>Tout est calme et <b>tranquille</b>.", "J\'aime le bruit de la <b>mer</b>,<br>Le cri joyeux des <b>mouettes</b>,<br>Les vagues qui font la <b>fête</b>,<br>Et le goût du sel <b>amer</b>.", "Il neige sur la <b>place</b>,<br>Les enfants font des <b>traces</b>,<br>Le vieux banc est tout <b>blanc</b>,<br>Le silence est <b>grand</b>."]) + '</div>', ["lis", "ecris"], 1, "C",
          sol="1. ABAB, croisées · 2. ABBA, embrassées · 3. AABB, plates")
    e2 = E("Je trouve 3 mots qui riment avec chaque mot (attention : le son, pas l'orthographe !).", table(["cœur", "nuit", "pluie", "chanson"], [["", "", "", ""]], ["45mm", "45mm", "45mm", "47mm"]).replace("<td></td>", '<td style="height:15mm"></td>'), ["ecris"], 1, "C",
           sol="Ex. : cœur → peur, fleur, bonheur · nuit → bruit, minuit, lit · pluie → ennui, aujourd'hui, parapluie · chanson → maison, poisson, raison")
    e3 = E("Je complète le poème avec des mots qui riment (rimes croisées).", f'<div class="card" style="{SERIF};line-height:2">Le matin, dans la cour de l\'<b>école</b>,<br>Les enfants courent sous le ______________ ,<br>Les cartables volent, les rires ______________ ,<br>Et le ballon tourne et ______________ .</div>', ["complete"], 2, "C",
           sol="Ex. : soleil · s'envolent / décollent · vermeil (ou : …tourne et rebondit — accepter toute rime ABAB cohérente : école / s'envolent, soleil / réveil)")
    e4 = E("J'écoute 6 paires de mots. Ça rime ? Je coche oui ou non.", checks(6, ["oui", "non"]), ["ecoute", "coche"], 1, "A",
           script="1. temps / attends — 2. mer / amer — 3. fleur / fleuve — 4. roses / closes — 5. ville / tranquille — 6. pluie / plage",
           sol="oui : 1, 2, 4, 5 · non : 3, 6")
    e5 = E("Défi ! J'écris un quatrain sur la saison de mon choix, en rimes croisées (ABAB).", lines(4), ["ecris"], 3, "C",
           sol="Production personnelle : 4 vers avec majuscule, schéma ABAB respecté, une image si possible.")
    b.page(f'{e}{e2}{e3}{e4}{e5}', "S'entraîner")

    # ---------- Leçon 2 : compter les syllabes ----------
    l2 = lecon("Compter les syllabes d'un vers", '<p class="sm" style="margin-bottom:1mm">En poésie, on compte les <b>syllabes prononcées</b>. Le vers de 12 syllabes s\'appelle l\'<b>alexandrin</b> ; le vers de 8 syllabes, l\'<b>octosyllabe</b> ; le vers de 6 syllabes, l\'<b>hexasyllabe</b>.</p>' +
        syllabes("Je partirai. Vois-tu, je sais que tu m'attends.", ["Je", "par", "ti", "rai.", "Vois", "-tu,", "je", "sais", "que", "tu", "m'at", "tends."]) +
        '<p class="sm mt2" style="margin-bottom:1mm">⚠️ <b>Le « e » muet</b> (sans accent) : ① il <b>se prononce</b> devant une consonne : « Seul, inconnu, le dos courb<b>é</b>… » → « Tris-<b>te</b>, et le jour » : non ! devant une voyelle, il <b>s\'efface</b> (élision) : « Tris-t(e) et » ; ② il <b>ne compte pas</b> en fin de vers : « cam-pa-gn(e) ». · <b>La diérèse</b> : parfois, le poète prononce deux voyelles en deux syllabes pour allonger le vers (« vi-o-lon » au lieu de « vio-lon »).</p>'
        '<div class="astuce" style="margin:1mm 0 0">✋ <b>Méthode :</b> je lis le vers à voix haute, lentement, en tapant chaque syllabe sur la table ; je barre les « e » qui s\'effacent devant une voyelle et le « e » final ; je vérifie avec mes doigts.</div>')
    P["hugo"] = b.n + 1
    e = E("Je lis le poème de Victor Hugo. Je compte les syllabes des vers 1, 3 et 8 (je découpe sous le vers).", '<div class="grid2" style="grid-template-columns:1.35fr 1fr;gap:3mm;align-items:start">' + poeme("Demain, dès l'aube…", "Victor Hugo, <i>Les Contemplations</i> (1856)", HUGO, 9.4, num=True) +
          f'<div class="sm"><p>Vers 1 : ______ syllabes</p><p>Vers 3 : ______ syllabes</p><p>Vers 8 : ______ syllabes</p><p>Ces vers sont des ______________ .</p><p>Schéma des rimes : ______________ (rimes ______________ )</p></div></div>', ["lis", "ecris"], 2, "B",
          sol="12 syllabes chacun. V1 : De-main-dès-l'au-b(e) à-l'heu-r(e) où-blan-chit-la-cam-pa-gn(e) · V3 : J'i-rai-par-la-fo-rêt-j'i-rai-par-la-mon-ta-gn(e) · V8 : Tris-t(e) et-le-jour-pour-moi-se-ra-com-me-la-nuit. Ce sont des alexandrins ; rimes croisées ABAB.")
    b.page(f'{l2}{e}', "Leçon 2")
    e = E("Je compte les syllabes (je barre les « e » muets qui ne se prononcent pas).", '<div class="card" style="' + SERIF + ';line-height:2">1. « Il pleure dans mon cœur » → ______ syllabes<br>2. « Sous le pont Mirabeau coule la Seine » → ______ syllabes<br>3. « À la claire fontaine » → ______ syllabes<br>4. « J\'ai voulu ce matin te rapporter des roses » → ______ syllabes</div>', ["lis", "complete"], 2, "C",
          sol="1. Il-pleu-re-dans-mon-cœur = 6 (le e de pleure se prononce devant « dans ») — 2. Sous-le-pont-Mi-ra-beau-cou-le-la-Sei-n(e) = 10 — 3. À-la-clai-re-fon-tai-n(e) = 6 — 4. J'ai-vou-lu-ce-ma-tin-te-rap-por-ter-des-ro-s(es) = 12")
    e2 = E("Le « e » muet : se prononce-t-il ? J'entoure les « e » prononcés et je barre les « e » muets.", f'<div class="card" style="{SERIF};line-height:2">1. Une étoile brille. 2. Elle regarde la lune. 3. La pluie tombe sur la ville endormie. 4. Le monde entier se tait.</div>', ["entoure", "barre"], 2, "C",
           sol="Prononcés (devant une consonne) : étoi<u>le</u> (devant brille), El<u>le</u>, <u>re</u>garde, regar<u>de</u> (devant la), tom<u>be</u>, <u>Le</u>, <u>se</u>. Muets : Un(e) (devant étoile), brill(e) et lun(e) et endormi(e) (fin de vers), vill(e) (devant endormie), mond(e) (devant entier).")
    e3 = E("J'écoute le vers et je tape les syllabes sur la table. J'écris le nombre.", '<p>1. ______ 2. ______ 3. ______ 4. ______</p>', ["ecoute", "ecris"], 2, "A",
           script="Lire en détachant les syllabes : 1. « Les jours s'en vont je demeure » (7) — 2. « Je ne puis demeurer loin de toi plus longtemps » (12) — 3. « Ô bruit doux de la pluie » (6) — 4. « Il y a longtemps que je t'aime » (8)",
           sol="1. 7 — 2. 12 — 3. 6 — 4. 8")
    e4 = E("Défi ! J'écris deux vers de 8 syllabes (octosyllabes) qui riment, sur mon quartier.", lines(2), ["ecris"], 3, "C",
           sol="Ex. : Dans ma rue, le matin, il pleut, (8) / Les parapluies sont rouges et bleus. (8)")
    e5 = E("Le « e » devant une voyelle s'efface (élision). Je barre les « e » qui s'effacent et je compte les syllabes.", f'<div class="card" style="{SERIF};line-height:2">1. « Une étoile au loin » → ______ 2. « La neige est belle » → ______ 3. « Comme une ombre » → ______ 4. « Elle arrive enfin » → ______</div>', ["lis", "complete"], 2, "C",
           sol="1. Un(e) é-toi-l(e) au-loin = 5 — 2. La-nei-g(e) est-bel-l(e) = 4 — 3. Com-m(e) u-n(e) om-br(e) = 3 — 4. El-l(e) a-rri-v(e) en-fin = 5")
    e6 = E("La diérèse. Dans ces vers, le poète prononce « i-on » en deux syllabes pour avoir le bon compte. Je découpe le mot souligné.", f'<div class="card" style="{SERIF};line-height:2">1. « Une douce <u>passion</u> » → pa-____-____ 2. « Les <u>violons</u> de l\'automne » → ____-____-____ 3. « La <u>nation</u> entière » → ____-____-____</div>', ["lis", "complete"], 3, "C",
           sol="1. pa-ssi-on — 2. vi-o-lons — 3. na-ti-on (avec diérèse ; dans la langue courante, on dit pa-ssion, vio-lons, na-tion)")
    b.page(f'{e}{e2}{e3}{e4}{e5}{e6}', "S'entraîner")

    # ---------- Leçon 3 : les images ----------
    l3 = lecon("Les images poétiques : comparaison, métaphore, personnification", table(["Figure", "Définition", "Exemple"], [
        ["la <b>comparaison</b>", "rapproche deux éléments avec un <b>outil de comparaison</b> : comme, tel, pareil à, ressembler à…", "« le jour pour moi sera <b>comme</b> la nuit » (Hugo)"],
        ["la <b>métaphore</b>", "rapproche deux éléments <b>sans outil</b> de comparaison", "« Mes mots sont des valises, mes phrases des ponts » (slam)"],
        ["la <b>personnification</b>", "donne à une chose ou un animal des <b>actions ou des sentiments humains</b>", "« Il pleure dans mon cœur » · « le vent chante »"],
        ["l'<b>hyperbole</b>", "<b>exagère</b> pour frapper l'esprit", "« Je te l'ai dit mille fois ! » · « mourir de rire »"]], ["32mm", "80mm", "70mm"]).replace('class="t"', 'class="t compact"') +
        '<div class="astuce" style="margin:2mm 0 0">🔍 <b>Pour analyser une image :</b> ① je trouve les deux éléments rapprochés (le comparé et le comparant) ; ② je cherche leur point commun ; ③ je dis l\'effet produit. « La lune est une lampe » : la lune / une lampe → elles éclairent la nuit → une image douce, familière.</div>')
    e = E("Comparaison (C), métaphore (M), personnification (P) ou hyperbole (H) ? J'écris la lettre.", '<div class="card" style="line-height:1.85">___ « Ses yeux brillent comme des étoiles. » &nbsp; ___ « La ville s\'endort sous la pluie. » &nbsp; ___ « Ce sac pèse une tonne ! »<br>___ « La mer est un miroir. » &nbsp; ___ « Le soleil sourit aux enfants. » &nbsp; ___ « Elle est rapide tel un guépard. » &nbsp; ___ « Ton rire est une chanson. »</div>', ["lis", "ecris"], 1, "B",
          sol="C · P · H · M · P · C · M")
    e2 = E("J'invente des comparaisons originales (pas « blanc comme la neige » !).", '<div class="card" style="line-height:2">1. Ma ville est grise comme ______________ . 2. Ton rire est léger comme ______________ . 3. Le bus est lent comme ______________ . 4. Mon cœur bat vite comme ______________ .</div>', ["complete"], 1, "C",
           sol="Ex. : 1. un vieux pull de grand-père — 2. une bulle de savon — 3. un dimanche sans fin — 4. les pas d'un enfant qui court")
    e3 = E("J'exagère ! Je transforme en hyperbole.", '<p>1. J\'ai très faim. → {0}</p><p>2. Il fait très froid. → {0}</p>'.format(blank("xl")), ["ecris"], 2, "C",
           sol="Ex. : 1. Je pourrais manger un éléphant ! / Je meurs de faim. — 2. On gèle, c'est le pôle Nord !")
    b.page(f'{l3}{e}{e2}{e3}', "Leçon 3")
    e = E("J'analyse les images : je trouve le comparé, le comparant et le point commun.", tall(table(["Image", "Comparé", "Comparant", "Point commun"], [["« La lune est une lampe. »", "la lune", "une lampe", "elles éclairent la nuit"], ["« Mes mots sont des valises. »", "", "", ""], ["« La vague en a paru rouge et comme enflammée. »", "", "", ""], ["« La neige est un drap blanc sur la ville. »", "", "", ""]], ["64mm", "36mm", "36mm", "46mm"]), 8).replace('class="t"', 'class="t compact"'), ["lis", "ecris"], 2, "C",
          sol="mes mots / des valises / ils transportent quelque chose (ses souvenirs, sa culture) · la vague / une chose enflammée (le feu) / la couleur rouge des roses · la neige / un drap blanc / elle couvre tout, blanche et douce")
    e2 = E("Je transforme les comparaisons en métaphores.", '<p>1. Ta voix est comme du miel. → {0}</p><p>2. La route ressemble à un serpent. → {0}</p><p>3. Ses cheveux sont comme de l\'or. → {0}</p>'.format(blank("xl")), ["ecris"], 1, "C",
           sol="1. Ta voix est du miel. — 2. La route est un serpent. — 3. Ses cheveux sont de l'or.")
    e3 = E("Je personnifie ces éléments avec un verbe humain : la pluie · le vent · la maison · la nuit.", lines(2), ["ecris"], 2, "C",
           sol="Ex. : La pluie pleure sur les toits. Le vent siffle une chanson. La vieille maison soupire. La nuit nous prend dans ses bras.")
    e4 = E("J'écoute 5 phrases tirées de chansons et de slams (écrits pour la classe). J'écris la figure de style.", '<p>1. ______________ 2. ______________ 3. ______________ 4. ______________ 5. ______________</p>', ["ecoute", "ecris"], 2, "A",
           script="1. « Ma ville est un océan de lumières. » — 2. « Le métro avale les gens et les recrache plus loin. » — 3. « Je t'attends depuis mille ans. » — 4. « Tes yeux sont noirs comme la nuit d'été. » — 5. « Le vieux piano raconte nos souvenirs. »",
           sol="1. métaphore — 2. personnification — 3. hyperbole — 4. comparaison — 5. personnification")
    e5 = E("Défi ! J'écris un petit poème de 4 vers sur la ville où j'habite, avec une comparaison, une métaphore et une personnification.", lines(4), ["ecris"], 3, "C",
           sol="Production personnelle : trois figures identifiables (l'élève les souligne de trois couleurs).")
    b.page(f'{e}{e2}{e3}{e4}{e5}', "S'entraîner")

    # ---------- Leçon 4 : les sons et les répétitions ----------
    l4 = lecon("La musique des mots : sons et répétitions", table(["Procédé", "Définition", "Exemple"], [
        ["l'<b>allitération</b>", "répétition d'un même son <b>consonne</b>", "« Pour qui sont ces serpents qui sifflent sur vos têtes ? » (Racine) : [s]"],
        ["l'<b>assonance</b>", "répétition d'un même son <b>voyelle</b>", "« Il pleure dans mon cœur / Comme il pleut » : [œ], [ø]"],
        ["l'<b>anaphore</b>", "répétition d'un même mot <b>en début de vers</b> ou de phrase", "« <b>J\'irai</b> par la forêt, <b>j\'irai</b> par la montagne. » (Hugo)"],
        ["le <b>refrain</b>", "vers répétés entre les strophes ou les couplets", "« Vienne la nuit sonne l'heure / Les jours s'en vont je demeure » (Apollinaire)"]], ["32mm", "64mm", "86mm"]).replace('class="t"', 'class="t compact"') +
        '<div class="astuce" style="margin:2mm 0 0">🎶 Les sons créent une <b>ambiance</b> : les [s] et les [ʃ] évoquent le souffle, le vent, le serpent ; les [ʁ] et les [k] la dureté, la colère ; les [l] et les [u] la douceur. Le refrain donne un <b>rythme</b> et aide à <b>mémoriser</b> : c\'est pour cela que les chansons en ont presque toujours un.</div>')
    P["chans"] = b.n + 1
    e = E("Je lis deux textes célèbres : le début d'un poème de Guillaume Apollinaire et une chanson traditionnelle. Je réponds.", '<div class="grid2" style="gap:3mm">' + poeme("Le Pont Mirabeau (1re strophe et refrain)", "Guillaume Apollinaire, <i>Alcools</i> (1913)", MIRABEAU, 9.8) + poeme("À la claire fontaine (1er couplet et refrain)", "chanson traditionnelle", FONTAINE, 9.8) + '</div>' +
          f'<p class="mt2">1. Qu\'est-ce qui manque dans le poème d\'Apollinaire ? Pourquoi, à ton avis ? {blank("xl")}</p><p>2. Relève les deux refrains. Quel est le thème commun des deux textes ? {blank("xl")}</p><p>3. Quel son revient dans le refrain d\'Apollinaire (« Vienne… demeure ») ? {blank("l")}</p>', ["lis", "ecris"], 2, "B",
          sol="1. La ponctuation : le lecteur choisit ses pauses ; les vers coulent comme l'eau de la Seine. — 2. « Vienne la nuit sonne l'heure / Les jours s'en vont je demeure » ; « Il y a longtemps que je t'aime, / Jamais je ne t'oublierai. » Thème commun : l'amour, le temps qui passe, l'eau (Seine, fontaine). — 3. [œ] / [ø] et [ʁ] : heure, demeure (et [ɑ̃] : vienne… s'en vont).")
    b.page(f'{l4}{e}', "Leçon 4")
    e = E("Allitération ou assonance ? J'écris le son répété et le nom du procédé.", '<div class="card" style="line-height:1.9">1. « Le vent violent vole les voiles. » → son ______ : ______________ 2. « La lune brune sur la dune. » → son ______ : ______________ 3. « Chut ! Chuchote, ma chère Charlotte. » → son ______ : ______________ 4. « Il dit oui à la pluie de minuit. » → son ______ : ______________</div>', ["lis", "complete"], 1, "C",
          sol="1. [v] : allitération — 2. [y] (+ [n]) : assonance — 3. [ʃ] : allitération — 4. [i] (et [ɥi]) : assonance")
    e2 = E("J'écris une anaphore de 4 vers qui commencent tous par « Je rêve d'un monde où… ».", lines(4), ["ecris"], 2, "C",
           sol="Ex. : Je rêve d'un monde où les frontières sont des ponts, / Je rêve d'un monde où chaque langue est une chanson, / Je rêve d'un monde où personne n'a peur, / Je rêve d'un monde où l'école est un bonheur.")
    e3 = E("J'écoute le slam « Deux langues » (écrit pour la classe). Je lève la main quand j'entends une répétition. Puis je complète.", f'<p>1. Le vers qui revient au début et à la fin : {blank("xl")}</p><p>2. Deux métaphores : {blank("xl")}</p><p>3. Quel est le message du slam ? {blank("xl")}</p>', ["ecoute", "ecris"], 2, "A",
           script="Lire le slam « Deux langues » (texte complet dans l'atelier A), avec rythme et sans musique : « J'ai deux langues dans la bouche, et aucune ne se tait… »",
           sol="1. « J'ai deux langues dans la bouche » — 2. « Mes mots sont des valises, mes phrases des ponts » ; « je ne suis pas une gare, je suis un chemin » — 3. On peut garder sa langue maternelle et le français : le mélange est une richesse, pas une faute.")
    e4 = E("Défi ! J'invente un virelangue (une phrase difficile à dire) avec une allitération en [p], [t] ou [ʁ].", lines(1), ["ecris"], 2, "C",
           sol="Ex. : Papa porte un petit pot de purée pour Paul.")
    e5 = E("« Pour qui sont ces serpents qui sifflent sur vos têtes ? » (Racine). Quel son est répété ? Quel animal l'auteur fait-il entendre ? Quel effet ?", lines(2), ["lis", "ecris"], 3, "B",
           sol="Le son [s] (allitération) : on entend le sifflement des serpents ; l'effet est inquiétant, menaçant.")
    b.page(f'{e}{e2}{e3}{e4}{e5}', "S'entraîner")

    # ---------- Leçon 5 (FLSco) : analyser un poème ----------
    l5 = lecon("Analyser un poème : la méthode", table(["Étape", "Je me demande…"], [
        ["① Première lecture", "Qu'est-ce que je ressens ? Quelle image me reste en tête ?"], ["② Le thème", "De quoi parle le poème ? (la nature, l'amour, la mort, le temps, l'exil…) Qui parle (« je ») ? À qui (« tu ») ?"],
        ["③ La forme", "Combien de strophes, de vers, de syllabes ? Quelles rimes ? Vers libres ou réguliers ?"], ["④ Les procédés", "Quelles images (comparaison, métaphore…) ? Quels sons, quelles répétitions ? Quels temps verbaux ?"],
        ["⑤ L'interprétation", "Quel est l'effet produit ? Quel est le message ? Pourquoi le titre ?"]], ["38mm", "144mm"]).replace('class="t"', 'class="t compact"') +
        '<div class="astuce" style="margin:2mm 0 0">✍️ <b>Rédiger un paragraphe d\'analyse :</b> une <b>idée</b> (« Le poète exprime sa tristesse… ») + une <b>citation</b> entre guillemets avec le numéro du vers (« Je marcherai les yeux fixés sur mes pensées », v. 5) + une <b>explication</b> du procédé et de son effet (« La marche montre… »). Je n\'écris pas seulement « c\'est beau » : je <b>justifie</b>.</div>')
    e = E(f"J'analyse « Demain, dès l'aube… » (p. {P['hugo']}). Je réponds aux questions de la méthode.", f'<p class="sm">1. Ce que je ressens à la première lecture : {blank("xl")}</p><p class="sm">2. Qui parle ? À qui ? Où va le poète ? (Lis le dernier vers !) {blank("xl")}</p><p class="sm">3. Relève les verbes au futur des vers 1 à 5. Que montrent-ils ? {blank("xl")}</p><p class="sm">4. Quels détails du paysage le poète refuse-t-il de regarder (strophe 3) ? Pourquoi ? {blank("xl")}</p><p class="sm">5. Relève l\'anaphore du vers 3. Quel effet produit-elle ? {blank("xl")}</p><p class="sm">6. Le vers 7 énumère des adjectifs : « Seul, inconnu, le dos courbé… ». Quel portrait du poète dessinent-ils ? {blank("xl")}</p>', ["lis", "ecris"], 2, "B",
          sol="1. Réponse personnelle (tristesse, émotion, surprise à la fin). — 2. Le poète (« je ») parle à quelqu'un (« tu ») qu'on croit vivant ; au dernier vers, on découvre qu'il va sur une tombe : celle de sa fille Léopoldine, morte en 1843. — 3. partirai, irai, marcherai (et « sais », « attends ») : la décision, le voyage certain ; il imagine déjà le chemin. — 4. « l'or du soir », « les voiles au loin » : il ne voit rien, il pense seulement à sa fille ; sa douleur l'isole du monde. — 5. « J'irai… j'irai » : la répétition montre sa détermination, rien ne l'arrêtera. — 6. Un homme seul, triste, accablé, enfermé dans sa douleur.")
    b.page(f'<span class="tag-doc">🎒 FRANÇAIS DE L\'ÉCOLE</span>{l5}{e}', "Consignes & école")
    e = E("La chute du poème. Relis le dernier vers de Hugo. Pourquoi peut-on dire que le poème a une « chute », comme une nouvelle (module 9) ?", lines(2), ["lis", "ecris"], 2, "B",
          sol="Pendant deux strophes, on croit à un rendez-vous d'amour (« je sais que tu m'attends ») ; le dernier vers révèle qu'il s'agit d'une tombe : la surprise change le sens de tout le poème.")
    e2 = E("Je complète le paragraphe d'analyse avec : citation · tristesse · comparaison · nuit · v. 8.", f'<div class="card" style="{SERIF};line-height:1.9">Dans la deuxième strophe, le poète exprime sa ______________ . Il écrit : « le jour pour moi sera comme la nuit » ( ______ ). Cette ______________ montre que même en plein jour, il ne voit que la ______________ : le deuil a tout assombri. La ______________ permet de justifier mon idée.</div>', ["lis", "complete"], 1, "C",
           sol="tristesse · v. 8 · comparaison · nuit · citation")
    e3 = E("Dans les autres cours ! Je relie la consigne et ce que je dois faire.", relie(["Relève…", "Identifie le procédé.", "Interprète.", "Commente ce vers.", "Justifie par une citation."], ["Je recopie les mots du texte qui correspondent.", "J'explique le sens caché, l'effet, le message.", "Je donne le nom de la figure ou du procédé.", "Je recopie des mots exacts entre guillemets pour prouver.", "J'explique ce que dit le vers, comment et pourquoi."]), ["lis", "relie"], 1, "B",
           sol="Relève → recopier les mots · Identifie → donner le nom · Interprète → sens caché, effet · Commente → ce que dit le vers, comment, pourquoi · Justifie → citation entre guillemets")
    e4 = E(f"Défi ! J'écris un paragraphe d'analyse (5 lignes) sur le poème de Verlaine (p. {P['verl']}) : une idée + une citation + l'explication d'un procédé.", lines(5), ["ecris"], 3, "C",
           sol="Ex. : Verlaine exprime une tristesse sans cause. Il écrit : « Il pleure dans mon cœur / Comme il pleut sur la ville » (v. 1-2). La comparaison rapproche les larmes et la pluie : le paysage reflète l'âme du poète. Les répétitions de « cœur » et les sons doux renforcent cette mélancolie.")
    b.page(f'{e}{e2}{e3}{e4}', "Consignes & école")

    # ---------- Leçon 6 : écrire un poème ----------
    l6 = lecon("Écrire un poème : des formes pour commencer", '<div class="grid2" style="gap:3mm;grid-template-columns:1.4fr 1fr"><div>' + table(["Forme", "Règle"], [["l'<b>acrostiche</b>", "les premières lettres des vers forment un mot vertical (un prénom, un mot-clé)"], ["le <b>haïku</b>", "un petit poème japonais de 3 vers (5, 7 et 5 syllabes) sur un instant de la nature"], ["le <b>calligramme</b>", "le texte dessine la forme de ce dont il parle (Apollinaire en a écrit beaucoup)"], ["« <b>Si j\'étais…</b> »", "chaque vers commence par « Si j'étais… je serais… » (le conditionnel !)"], ["« <b>à la manière de</b> »", "je garde la structure d'un poème célèbre et je change les mots"]], ["36mm", "86mm"]).replace('class="t"', 'class="t compact"') +
        f'</div><div class="c">{calligramme(50)}<div class="xs muted">calligramme écrit pour la classe : « Il pleut des mots doux… »</div></div></div>' +
        '<div class="card sm mt2" style="background:#fff;' + SERIF + '"><b style="font-family:Poppins">Exemples (écrits pour la classe) :</b> acrostiche — <b>P</b>luie sur la ville / <b>L</b>armes du ciel gris / <b>U</b>ne flaque où je saute / <b>I</b>l fait doux quand même / <b>E</b>t le soleil revient. · haïku — <i>Neige sur la cour</i> (5) / <i>un oiseau laisse ses pas</i> (7) / <i>le silence chante</i> (5).</div>')
    e = E("J'écris l'acrostiche de mon prénom (ou du mot ÉCOLE, AMI, RÊVE).", lines(5), ["ecris"], 1, "C", sol="Production personnelle : chaque vers commence par la bonne lettre ; le poème a un sens.")
    b.page(f'{l6}{e}', "Leçon 6")
    e = E("J'écris un haïku sur la saison d'aujourd'hui (5 / 7 / 5 syllabes). Je compte sur mes doigts !", '<p class="sm">(5) ______________________________<br>(7) ______________________________<br>(5) ______________________________</p>', ["ecris"], 2, "C",
          sol="Ex. : Feuilles dans le vent (5) / novembre danse en silence (7) / le ciel est si bas (5)")
    e2 = E("J'écris un poème « Si j'étais… » de 4 vers (je serais + conditionnel).", '<div class="card sm" style="background:#fff;' + SERIF + '"><i>Modèle : Si j\'étais un oiseau, je volerais jusqu\'à ma grand-mère. / Si j\'étais la mer, je bercerais les bateaux…</i></div>' + lines(4), ["ecris"], 2, "C",
           sol="Production personnelle : 4 vers « Si j'étais…, je + conditionnel » corrects (volerais, serais, chanterais…).")
    e3 = E("À la manière de Verlaine : je réécris la première strophe en changeant la météo et l'émotion.", f'<div class="card sm" style="{SERIF}"><i>Il pleure dans mon cœur / Comme il pleut sur la ville ; / Quelle est cette langueur / Qui pénètre mon cœur ?</i></div><div class="card sm" style="{SERIF};line-height:2.1">Il ______________ dans mon cœur<br>Comme il ______________ sur ______________ ;<br>Quel est ce ______________<br>Qui ______________ mon cœur ?</div>', ["ecris"], 3, "C",
           sol="Ex. : Il brille dans mon cœur / Comme il fait beau sur la plage ; / Quel est ce grand bonheur / Qui réchauffe mon cœur ?")
    e4 = E("Je dessine un calligramme : j'écris une phrase poétique en forme de soleil, de cœur, de maison ou d'arbre.", '<div style="border:1.5px dashed #9aa1b1;border-radius:3mm;height:48mm"></div>', ["dessine", "ecris"], 2, "C",
           sol="Production personnelle : le texte suit la forme dessinée et parle de cet objet.")
    b.page(f'{e}{e2}{e3}{e4}', "S'entraîner")

    # ---------- Documents de la vie ----------
    aff = f'''<div class="doc" style="transform:none;border:2px solid #1F2A44;background:#1F2A44;color:#fff;padding:3mm 4mm;font-size:9.6pt;line-height:1.4">
<div class="flex" style="justify-content:space-between"><b style="font-size:16pt;color:#FFD166">🎤 SLAM'ADOS · Scène ouverte</b><span class="xs" style="opacity:.8">(événement fictif)</span></div>
<p style="margin:1mm 0">Centre culturel de Hautrive · <b>vendredi 19 mars 2027, 19 h</b> · Journée mondiale de la poésie : le 21 mars</p>
<div class="grid2" style="gap:3mm"><div><b>📝 Les règles de la scène</b><br>① Un texte de <b>ta</b> création · ② <b>3 minutes</b> maximum · ③ <b>pas de musique</b>, pas de costume, pas d'accessoire · ④ toutes les langues sont les bienvenues (avec une phrase en français pour présenter) · ⑤ le public écoute en silence et applaudit en claquant des doigts 🫰</div>
<div><b>✍️ Inscription</b> : avant le 12 mars, à l'accueil du centre culturel ou par courriel (slamados@ccHautrive.be, adresse fictive) · 12-20 ans · entrée gratuite pour le public<br><b>🎁 Atelier de préparation</b> : les mercredis 3 et 10 mars, 14 h-16 h, avec le slameur Nassim B.<br><b>♿</b> Salle accessible aux personnes à mobilité réduite.</div></div></div>'''
    e = E("Je lis l'affiche de la scène ouverte de slam. Je réponds.", aff + f'<p class="mt2">1. Où et quand a lieu la scène ouverte ? Pourquoi cette date ? {blank("xl")}</p><p>2. Peut-on dire le texte d\'un rappeur célèbre ? Avec une musique ? Justifie. {blank("xl")}</p><p>3. Yonas veut dire un slam en tigrigna. Est-ce possible ? À quelle condition ? {blank("xl")}</p><p>4. Comment le public montre-t-il qu\'il aime un texte ? {blank("l")}</p><p>5. Combien coûte l\'entrée ? Qui peut monter sur scène ? {blank("l")}</p>', ["lis", "ecris"], 2, "B",
          sol="1. Au centre culturel de Hautrive, le vendredi 19 mars 2027 à 19 h ; c'est juste avant la Journée mondiale de la poésie (21 mars). — 2. Non : il faut un texte de sa création, sans musique. — 3. Oui, toutes les langues sont acceptées, avec une phrase en français pour présenter. — 4. En claquant des doigts. — 5. Gratuite ; les jeunes de 12 à 20 ans inscrits avant le 12 mars.")
    e2 = E("Je rédige le courriel d'inscription de Yonas (5 lignes) : formule d'appel, présentation, titre et langue du texte, question sur l'atelier, formule de politesse.", lines(5), ["ecris"], 2, "C",
           sol="Ex. : Madame, Monsieur, Je m'appelle Yonas, j'ai 15 ans et je voudrais m'inscrire à la scène ouverte du 19 mars. Je dirai un slam intitulé « Deux langues », en tigrigna et en français. Est-il encore possible de participer à l'atelier du 3 mars ? Je vous remercie. Bien cordialement, Yonas T.")
    b.page(f'<span class="tag-doc">📄 DOCUMENT DE LA VIE</span><h2>Une scène ouverte de slam</h2>{e}{e2}', "Document de la vie")
    album = f'''<div class="doc" style="transform:none;border:1.5px solid #9aa1b1;background:#fff;padding:3mm 4mm;font-size:9.4pt;line-height:1.4"><div class="flex" style="justify-content:space-between"><b style="font-size:12pt;color:{MC}">💿 Livret de l'album « Racines » · Lina K.</b><span class="xs muted">(album et artiste fictifs)</span></div>
<div class="grid2" style="gap:3mm;margin-top:1mm"><div><b>Liste des titres</b><br>1. Ma rue (3'12) · 2. Deux langues (feat. Nassim B.) (2'58) · 3. La Meuse en hiver (4'05) · 4. Lettre à ma grand-mère (3'40) · 5. Septante fois (3'01)</div>
<div style="{SERIF}"><b style="font-family:Poppins">Paroles · 3. La Meuse en hiver (extrait)</b><br><i>La Meuse est un ruban gris qui ne dort jamais,<br>Elle porte mes secrets jusqu'à la mer du Nord,<br>Et quand le brouillard tombe sur les quais,<br>Je chante plus fort, je chante plus fort.</i></div></div>
<p class="xs muted" style="margin:1.5mm 0 0">Paroles et musique : Lina K. · Tous droits réservés. Reproduction interdite sans autorisation. Les droits d'auteur sont gérés par une société de gestion collective.</p></div>'''
    e = E("Je lis le livret d'un album. Je réponds.", album + f'<p class="mt2">1. Quel titre est le plus long ? Le plus court ? {blank("l")}</p><p>2. Que veut dire « feat. » (de l\'anglais <i>featuring</i>) ? {blank("l")}</p><p>3. Dans l\'extrait, relève une métaphore et une personnification. {blank("xl")}</p><p>4. Quel vers est répété ? Quel effet ? {blank("xl")}</p><p>5. Pourquoi est-il interdit de recopier les paroles et de les publier sans autorisation ? {blank("xl")}</p>', ["lis", "ecris"], 2, "B",
          sol="1. La Meuse en hiver (4'05) ; Deux langues (2'58). — 2. « avec la participation de » (un autre artiste chante avec elle). — 3. Métaphore : « La Meuse est un ruban gris » ; personnification : « qui ne dort jamais », « Elle porte mes secrets ». — 4. « Je chante plus fort » : insistance, courage contre la tristesse. — 5. À cause du droit d'auteur : les paroles appartiennent à leur auteur, qui doit donner son accord (et être payé).")
    e2 = E("Belgicismes en chanson. Le titre 5 s'appelle « Septante fois ». Je relie le nombre belge et le nombre de France.", relie(["septante", "nonante", "septante-sept", "nonante-neuf"], ["quatre-vingt-dix-neuf", "soixante-dix", "soixante-dix-sept", "quatre-vingt-dix"]), ["lis", "relie"], 1, "B",
           sol="septante → soixante-dix · nonante → quatre-vingt-dix · septante-sept → soixante-dix-sept · nonante-neuf → quatre-vingt-dix-neuf")
    e3 = E("J'écris le premier couplet (4 vers) d'une chanson sur un fleuve ou une rue que j'aime, avec un refrain de 2 vers.", lines(6), ["ecris"], 3, "C",
           sol="Production personnelle : un couplet de 4 vers, un refrain de 2 vers, au moins une image.")
    b.page(f'<span class="tag-doc">📄 DOCUMENT DE LA VIE</span><h2>Le livret d\'un album</h2>{e}{e2}{e3}', "Document de la vie")

    # ---------- Vers les épreuves ----------
    e = E(f"Entraînement de type CE1D : je relis « Les roses de Saadi » (p. {P['saadi']}) et je réponds en justifiant.", poeme("Les roses de Saadi", "Marceline Desbordes-Valmore (1860)", SAADI, 11, num=True) +
          f'<p class="sm mt2" style="margin-bottom:1mm">a) Qui parle (« je ») ? À qui (« te ») ? Que s\'est-il passé ? {blank("xl")}</p><p class="sm" style="margin-bottom:1mm">b) Relève une comparaison. Explique-la. {blank("xl")}</p><p class="sm" style="margin-bottom:1mm">c) Relève deux mots qui appartiennent au champ lexical de la mer. {blank("l")}</p><p class="sm" style="margin-bottom:1mm">d) Compte les syllabes du vers 1. Comment s\'appelle ce vers ? {blank("l")}</p><p class="sm" style="margin-bottom:1mm">e) Quel sens est évoqué dans la dernière strophe ? Cite deux mots. {blank("l")}</p>', ["lis", "ecris"], 3, "C",
          sol="a) La poétesse parle à la personne aimée ; elle voulait lui apporter des roses, mais les nœuds ont éclaté et le vent les a emportées dans la mer. — b) « rouge et comme enflammée » (v. 7) : la vague couverte de pétales rouges ressemble à du feu. — c) la mer, l'eau, la vague. — d) 12 syllabes : un alexandrin. — e) L'odorat : « embaumée », « odorant ».")
    e2 = E("Le vocabulaire du poème. Je relie le mot et son sens.", relie(["des ceintures closes", "contenir", "embaumée", "odorant", "enflammée"], ["qui sent bon", "parfumée", "en feu", "garder à l'intérieur", "des ceintures fermées (où l'on glissait les fleurs)"]), ["lis", "relie"], 2, "B",
           sol="ceintures closes → ceintures fermées · contenir → garder à l'intérieur · embaumée → parfumée · odorant → qui sent bon · enflammée → en feu")
    b.page(EPR.format(k="CE1D", t="Lire et analyser un poème") + e + e2, "Vers les épreuves")
    e = E("Suite de l'épreuve.", f'<p class="sm">f) « Respires-en sur moi l\'odorant souvenir » : que reste-t-il des roses ? Pourquoi ce vers est-il plutôt joyeux, malgré la perte ? {blank("xl")}</p><p class="sm">g) Rédige un paragraphe d\'analyse (4 lignes) : « Ce poème transforme une perte en souvenir. » Utilise une citation.</p>{lines(4)}', ["lis", "ecris"], 3, "C",
          sol="f) Le parfum : la robe est embaumée ; la poétesse offre quand même un souvenir, une émotion — la perte devient un cadeau. — g) Ex. : Les roses sont perdues, emportées par la mer (« Elles ont suivi l'eau pour ne plus revenir », v. 6). Pourtant, leur parfum reste sur la robe : « Respires-en sur moi l'odorant souvenir » (v. 9). L'impératif invite l'être aimé à partager ce souvenir : la perte devient un cadeau.")
    e2 = E("Entraînement DELF B1 · production orale, partie 2 (exercice en interaction, environ 3 à 4 minutes, sans préparation).", f'<div class="card" style="background:{TINT}"><b>Sujet :</b> Votre école organise un récital de poésie. Votre ami(e) (joué(e) par l\'examinateur) refuse d\'y participer : il (elle) trouve que la poésie est ennuyeuse et il (elle) a peur de parler en public. Vous essayez de le (la) convaincre : vous proposez des solutions et vous répondez à ses objections.</div>' +
           tall(table(["Je prépare des phrases utiles", ""], [["Proposer : Et si tu… ? / Tu pourrais… / Pourquoi pas… ?", ""], ["Rassurer : Ne t'inquiète pas, … / Je comprends, mais…", ""], ["Répondre à une objection : C'est vrai, mais… / Certes…, cependant…", ""], ["Conclure : Alors, d'accord ? / On essaie ensemble ?", ""]], ["90mm", "92mm"]), 9).replace('class="t"', 'class="t compact"'), ["parle", "duo"], 3, "P",
           sol="Grille DELF B1 (interaction) : réaliser la tâche (convaincre), réagir aux objections, proposer des solutions, utiliser les formules d'interaction, lexique et grammaire adaptés, prononciation. Jouer la scène en duo, puis avec la prof.")
    b.page(f'{e}{e2}<div class="astuce">💡 Au DELF B1 (partie 2), il n\'y a pas de bonne ou de mauvaise opinion : l\'examinateur évalue ta capacité à <b>discuter</b>, à <b>argumenter</b> et à <b>réagir</b>. Écoute bien ses objections et réponds-y une par une.</div>', "Vers les épreuves")

    # ---------- Sons ----------
    e = E("Dire un poème : le souffle et les pauses. Je lis l'encadré, puis je m'entraîne avec la première strophe de Verlaine.", '<div class="astuce" style="margin:0 0 2mm">🫁 Je <b>respire</b> avant chaque vers · je fais une <b>petite pause</b> à la fin du vers ( / ) et une <b>grande pause</b> à la fin de la strophe ( // ) · je prononce les « e » qui comptent (« Il pleu-<b>re</b> dans mon cœur ») · je fais les <b>liaisons</b> obligatoires · je <b>regarde</b> le public et je ne lis pas trop vite.</div>' +
          f'<div class="card" style="{SERIF};font-size:12pt;line-height:1.8">Il pleu<b>re</b> dans mon cœur /<br>Comme il pleut sur la ville ; /<br>Quelle est cet<b>te</b> langueur /<br>Qui pénètre mon cœur ? //</div>', ["lis", "parle"], 1, "A",
          sol="Lecture évaluée : pauses, « e » prononcés, liaisons (« Comme‿il »), intonation montante sur la question.")
    e2 = E("J'écoute deux lectures de « Demain, dès l'aube… » (strophe 1). Laquelle respecte le poème ? Je coche ce que j'entends dans la bonne lecture.", table(["Dans la bonne lecture…", "✅"], [[x, '<span class="chk"></span>'] for x in ["le lecteur fait une pause après « Je partirai. »", "il compte les 12 syllabes (« l'au-be à » → « l'au-b(e) à »)", "il lit très vite, comme une liste", "sa voix est grave et lente", "il oublie de respirer"]], ["160mm", "22mm"]).replace('class="t"', 'class="t compact"'), ["ecoute", "coche"], 2, "A",
           script="Lire la première strophe deux fois : d'abord vite, monotone, en avalant les syllabes ; puis lentement, gravement, avec une pause après « Je partirai. » et à la fin de chaque vers.",
           sol="La 2e lecture : pause après « Je partirai. », 12 syllabes respectées, voix grave et lente.")
    e3 = E("Les liaisons dans les poèmes. Je marque les liaisons (‿) puis je lis.", f'<div class="card" style="{SERIF};font-size:11.5pt;line-height:2">1. Les nœuds ont éclaté. 2. Elles ont suivi l\'eau. 3. Les jours s\'en vont. 4. Il y a longtemps que je t\'aime. 5. Mes yeux fixés sur mes pensées.</div>', ["lis", "repete"], 2, "A",
           sol="1. Les‿nœuds ont‿éclaté (liaison « nœuds‿ont » facultative, [z]) — 2. Elles‿ont suivi — 3. pas de liaison obligatoire (s'en‿vont : non) — 4. Il‿y‿a — 5. Mes‿yeux")
    e4 = E("En trio : chacun dit une strophe d'un poème du module, par cœur ou en lisant. Les autres évaluent.", chk3(["Je respire et je fais les pauses.", "Je prononce bien les syllabes et les liaisons.", "Ma voix exprime l'émotion du poème."]), ["parle", "groupe", "coche"], 2, "A", sol="Activité orale évaluée entre pairs.")
    b.page(f'<h2>J\'écoute bien · dire un poème</h2>{e}{e2}{e3}{e4}', "Sons")
    e = E("Les sons [ʁ] et [l]. J'écoute et je répète.", '<div class="grid2"><div class="card c"><div class="big"><b>[ʁ]</b> comme « rime »</div><p class="big" style="margin:1mm 0 0"><b>r</b>ime · <b>r</b>êve · c<b>r</b>i · mé<b>r</b>i<b>r</b> · cœu<b>r</b> · lang<b>r</b>e… non : langueu<b>r</b></p></div><div class="card c"><div class="big"><b>[l]</b> comme « lune »</div><p class="big" style="margin:1mm 0 0"><b>l</b>une · vi<b>ll</b>e · p<b>l</b>uie · fi<b>l</b> · seu<b>l</b> · voi<b>l</b>e</p></div></div><p class="sm mt2" style="margin:2mm 0 0">✏️ [ʁ] se prononce au fond de la gorge (comme un petit gargarisme) ; [l] avec la pointe de la langue derrière les dents. ⚠️ « ville » = [vil] mais « fille » = [fij].</p>', ["ecoute", "repete"], 1, "A",
          script="Lire chaque mot deux fois. Faire placer la main sur la gorge pour [ʁ] ; faire voir la langue pour [l]. Corriger « langre » (mot inexistant) → « langueur ». Opposer « ville » [vil] et « fille » [fij].",
          sol="Activité orale.")
    e2 = E("J'écoute : [ʁ] ou [l] ? Je coche.", checks(8, ["[ʁ]", "[l]"]), ["ecoute", "coche"], 2, "A", script="1. la rue — 2. lu — 3. la roue — 4. le loup — 5. riz — 6. lit — 7. rang — 8. lent",
           sol="[ʁ] : 1, 3, 5, 7 · [l] : 2, 4, 6, 8")
    e3 = E("Je lis vite et bien.", '<div class="card big c" style="line-height:1.8">La lune lit la lettre lente de la ville.<br>Le rat rêveur rit sous la rue, rond et roux.</div>', ["lis", "repete"], 2, "A", sol="Activité orale (virelangues écrits pour la classe).")
    e4 = E("Dictée de vers : j'écoute deux fois et j'écris.", lines(3), ["ecoute", "ecris"], 2, "A",
           script="« Il pleure dans mon cœur / Comme il pleut sur la ville ; / Quelle est cette langueur / Qui pénètre mon cœur ? » (Verlaine)",
           sol="Il pleure dans mon cœur / Comme il pleut sur la ville ; / Quelle est cette langueur / Qui pénètre mon cœur ?")
    b.page(f'<h2>J\'écoute bien · [ʁ] et [l]</h2>{e}{e2}{e3}{e4}', "Sons")

    # ---------- Révision spirale ----------
    e = E("🔁 V3 · Module 9 · Le passé simple. J'écris l'infinitif : « Les nœuds éclatèrent. Les roses s'envolèrent. La vague devint rouge. » → ______________ · ______________ · ______________", "", ["ecris"], 2, "C", sol="éclater · s'envoler · devenir")
    e2 = E("🔁 V3 · Module 9 · La description. J'enrichis : « une rose » → une rose ______________ ______________ qui ______________", "", ["complete"], 1, "C", sol="Ex. : une rose rouge de Saadi qui sent bon")
    e3 = E("🔁 V3 · Module 8 · Le passif. « Le vent emporta les roses. » → Les roses ______________________________ .", "", ["ecris"], 2, "C", sol="Les roses furent (ont été) emportées par le vent.")
    e4 = E("🔁 V3 · Module 7 · Donner son avis. Quel poème du module préfères-tu ? 2 phrases : mon avis + une raison avec « car » ou « en effet ».", lines(2), ["ecris"], 2, "C", sol="Ex. : Je préfère « Les roses de Saadi ». En effet, l'image des roses dans la mer est très belle.")
    e5 = E("🔁 V3 · Module 6 · Le discours indirect. Hugo écrit : « Je partirai. » → Hugo écrit qu'il ______________ .", "", ["complete"], 1, "C", sol="… qu'il partira.")
    e6 = E("🔁 V3 · Module 5 · La comparaison (grammaire). Je complète avec plus… que, aussi… que, moins… que : Le poème de Hugo est ______ long ______ celui de Verlaine (12 vers contre 16). Ses vers sont ______ longs ______ ceux de Verlaine (12 syllabes contre 6).", "", ["complete"], 2, "C", sol="moins… que · plus… que")
    e7 = E("🔁 V2 · Module 4 · Les émotions. J'écris l'adjectif : la tristesse → ______ · la joie → ______ · la colère → ______ · la peur → ______", "", ["complete"], 1, "C", sol="triste · joyeux / joyeuse · en colère (coléreux) · peureux / apeuré")
    e8 = E("🔁 V2 · Module 14 · Le conditionnel (j'aimerais). Je complète : Si j'étais poète, j'(écrire) ______________ sur la mer et je (chanter) ______________ ma ville.", "", ["complete"], 1, "C", sol="j'écrirais · je chanterais")
    b.page(f'<h2>🔁 Je révise les modules précédents</h2>{e}{e2}{e3}{e4}{e5}{e6}{e7}{e8}', "Je révise")

    # ---------- Ateliers ----------
    e = E("J'écoute et je lis le slam « Deux langues » (écrit pour la classe). Je réponds.", poeme("Deux langues", "slam écrit pour la classe", SLAM, 10) + f'<p class="mt2">1. Que représentent les « deux langues » ? {blank("xl")}</p><p>2. Explique la métaphore « je ne suis pas une gare, je suis un chemin ». {blank("xl")}</p><p>3. Que répond le slameur à ceux qui trouvent son accent étrange ? {blank("xl")}</p>', ["ecoute", "lis", "ecris"], 2, "A",
          script="Dire le slam avec rythme, sans musique, en marquant les rimes et en regardant la classe. Le redire une deuxième fois en faisant claquer des doigts aux rimes.",
          sol="1. Sa langue maternelle et le français. — 2. Une gare est un lieu où l'on doit choisir une destination ; un chemin relie deux endroits : il ne veut pas choisir, il relie ses deux cultures. — 3. Que son accent n'est pas une faute mais un mélange, une richesse.")
    e2 = E("En chœur : la classe dit le slam. Un groupe dit les vers, un autre groupe répète le dernier mot de chaque vers en écho.", chk3(["Nous respectons le rythme ensemble.", "Les rimes s'entendent bien.", "Nous mettons de l'émotion dans la voix."]), ["parle", "groupe", "coche"], 1, "A", sol="Activité orale collective.")
    e3 = E("J'écris une strophe de 4 vers pour continuer le slam, en commençant par « J'ai deux langues dans la bouche… ».", lines(4), ["ecris"], 3, "C", sol="Production personnelle : 4 vers, au moins une rime et une image.")
    b.page(f'{atl_head("A", "Atelier · Le slam de la classe")}{e}{e2}{e3}', "Atelier")
    poems = [("Daria", "Kyiv, je t'ai laissée / dans une valise bleue. / Liège, tu m'as prêté / un parapluie et du feu."), ("Bilal", "Mon quartier est un livre / que j'ouvre chaque matin : / la boulangère est une page, / le bus, le dernier chapitre."), ("Fatou", "Le soleil de Dakar / dort dans ma poche. / Quand il fait gris ici, / je le sors, tout doucement.")]
    e = E("Les poèmes des élèves de la classe (écrits pour le cahier). Je lis et je complète le tableau.", '<div class="grid3" style="gap:2mm">' + "".join(f'<div class="card" style="{SERIF};background:#FFFCF5;font-size:10pt;padding:2mm 3mm"><b style="font-family:Poppins;color:{MC}">{n}</b><br>{t.replace(" / ", "<br>")}</div>' for n, t in poems) + '</div>' +
          tall(table(["", "Le thème", "Une image (figure)", "L'émotion"], [["Daria", "", "", ""], ["Bilal", "", "", ""], ["Fatou", "", "", ""]], ["24mm", "50mm", "60mm", "48mm"]), 12).replace('class="t"', 'class="t compact"'), ["lis", "ecris"], 2, "B",
          sol="Daria : l'exil (Kyiv → Liège) ; personnification (Liège prête un parapluie et du feu) ; nostalgie et réconfort · Bilal : son quartier ; métaphore filée (le quartier est un livre, la boulangère une page) ; tendresse · Fatou : le souvenir de Dakar ; métaphore / personnification (le soleil dort dans sa poche) ; nostalgie, espoir")
    e2 = E("Quel poème de la classe préfères-tu ? J'explique pourquoi en 3 phrases, avec une citation.", lines(3), ["ecris"], 2, "C", sol="Avis personnel : préférence, raison, citation entre guillemets.")
    e3 = E("Les vers libres. Ces poèmes riment-ils ? Comment le poète crée-t-il quand même de la musique ?", lines(2), ["lis", "ecris"], 3, "B",
           sol="Presque pas de rimes (sauf « bleue / feu », assonance) : ce sont des vers libres ; la musique vient des images, des répétitions de structure et du rythme des vers courts.")
    b.page(f'{atl_head("B", "Atelier · Les poètes de la classe")}{e}{e2}{e3}', "Atelier")
    e = E("J'écris mon poème (ou mon slam) pour le récital : 3 strophes, sur le thème « D'ici et d'ailleurs ».", '<div class="card sm" style="background:#fff">Je choisis : ☐ vers libres ☐ rimes ☐ slam · J\'utilise au moins : une comparaison, une métaphore, une répétition (anaphore ou refrain), un mot de ma langue. Je donne un titre.</div><p class="mt2" style="margin-bottom:1mm"><b>Titre :</b> ' + blank("xl") + '</p>' + lines(13), ["ecris"], 3, "C",
          sol="Poème de 3 strophes : thème respecté, figures demandées identifiables, titre, travail sur les sons ou le rythme.")
    e2 = E("Je fais lire mon poème à mon voisin. Il souligne en couleur les figures et me donne un conseil.", chk3(["Il y a une comparaison, une métaphore et une répétition.", "Le poème a un titre et 3 strophes.", "On entend une musique (rimes, sons, rythme)."]), ["lis", "duo", "coche"], 1, "C", sol="Relecture entre pairs.")
    b.page(f'{atl_head("C", "Atelier · J\'écris mon poème")}{e}{e2}', "Atelier")
    dom = [("pluie", "nuit"), ("cœur", "fleur"), ("mer", "hiver"), ("ville", "tranquille"), ("chanson", "maison"), ("temps", "printemps"), ("lune", "brune"), ("rêve", "trêve"), ("ciel", "miel"), ("soleil", "réveil"), ("amour", "toujours"), ("étoile", "voile")]
    cards = '<div class="grid6" style="gap:1.2mm">' + "".join(f'<div class="card c" style="padding:5mm 0;display:flex;border-color:{MC}"><span style="flex:1;border-right:1.5px dashed {MC}">{a}</span><span style="flex:1">{z}</span></div>' for a, z in [(dom[i][1], dom[(i + 1) % 12][0]) for i in range(12)]) + '</div>'
    e = E("Le jeu « Les dominos des rimes » (2 à 4 joueurs).", '<div class="card sm" style="background:#fff">On découpe les 12 dominos. On les distribue. Le premier joueur pose un domino ; le suivant doit poser un domino dont la moitié <b>rime</b> avec le bout libre. Si on ne peut pas jouer, on passe. Bonus : celui qui invente un vers avec les deux mots qui riment gagne 1 point. Le premier qui n\'a plus de dominos a gagné.</div>' + cards, ["joue", "groupe"], 2, "D",
          sol="Les dominos forment une boucle : nuit / cœur → fleur / mer → hiver / ville → … ; chaque moitié droite rime avec la moitié gauche du domino suivant (pluie-nuit, cœur-fleur, mer-hiver…).")
    e2 = E("Le cadavre exquis poétique (en groupe de 4). Chacun écrit une partie de la phrase sans voir les autres, puis on plie la feuille et on lit le résultat.", '<div class="card sm" style="background:#fff">① un nom + un adjectif (« La lune bleue ») · ② un verbe (« chante ») · ③ un complément (« sur les toits de Liège ») · ④ une comparaison (« comme un enfant qui rêve »). On recommence 3 fois et on garde la phrase la plus poétique pour le récital.</div>' + lines(3), ["ecris", "groupe"], 1, "D",
           sol="Productions libres ; le jeu, inventé par les surréalistes dans les années 1920, montre que des rapprochements inattendus créent des images.")
    e3 = E("Après le jeu : j'écris deux vers qui riment avec deux mots d'un domino.", lines(2), ["ecris"], 2, "C", sol="Ex. : Sous la lune brune, / je compte les étoiles une à une.")
    b.page(f'{atl_head("D", "Atelier · Jouer avec les mots")}{e}{e2}{e3}', "Atelier")

    # ---------- ★ Coup de pouce ----------
    e = E("Je relie le mot et le dessin.", relie(["la pluie", "la lune", "une rose", "la mer", "le cœur"], ["🌹", "❤️", "🌊", "🌧️", "🌙"]), ["relie"], 1, "B", alpha=True, sol="pluie → 🌧️ · lune → 🌙 · rose → 🌹 · mer → 🌊 · cœur → ❤️")
    e2 = E("J'entoure les mots qui riment avec « cœur ».", '<div class="card big c" style="line-height:2">fleur · chat · peur · vélo · bonheur · table · sœur · pluie</div>', ["entoure"], 1, "C", alpha=True, sol="fleur · peur · bonheur · sœur")
    e3 = E("Je compte les vers et les strophes du poème de Verlaine (p. {0}).".format(P["verl"]), '<p class="big" style="line-height:2.1">Il y a ______ strophes.<br>Chaque strophe a ______ vers.<br>Le poète s\'appelle ______________ .</p>', ["lis", "complete"], 1, "C", alpha=True, sol="4 · 4 · Paul Verlaine")
    e4 = E("Je relie les mots qui riment.", relie(["mer", "chat", "ville", "jour"], ["toujours", "tranquille", "hiver", "rat"]), ["relie"], 1, "B", alpha=True, sol="mer → hiver · chat → rat · ville → tranquille · jour → toujours")
    b.page(CP.format(t="Le poème") + e + e2 + e3 + e4, "★ Coup de pouce")
    e = E("Je lis le modèle. Je complète la comparaison.", '<div class="card" style="background:#F2F6FD"><p class="big" style="margin:0">Modèle : La lune est ronde <b>comme</b> un ballon.</p></div><p class="big" style="line-height:2.1;margin:2mm 0 0">1. La neige est blanche comme ______________ .<br>2. Le soleil est jaune comme ______________ .<br>3. Mon chat est doux comme ______________ .</p>', ["lis", "complete"], 1, "C", alpha=True, sol="Ex. : 1. du lait / le sucre — 2. un citron — 3. un nuage / la soie")
    e2 = E("Je relie : la chose et l'action humaine (personnification).", relie(["Le vent", "La pluie", "Le soleil", "La maison"], ["sourit.", "dort.", "chante.", "pleure."]), ["relie"], 1, "B", alpha=True, sol="Ex. : Le vent chante · La pluie pleure · Le soleil sourit · La maison dort (d'autres associations sont possibles)")
    e3 = E("Je complète avec un mot qui rime.", '<div class="card" style="background:#F2F6FD"><p class="big" style="line-height:2.1;margin:0">Il pleut sur la ville,<br>tout est ______________ .<br>J\'ai un chat gris,<br>qui dort dans mon ______________ .</p></div>', ["complete"], 1, "C", alpha=True, sol="tranquille · lit")
    b.page(CP.format(t="Les images et les rimes") + e + e2 + e3, "★ Coup de pouce")
    e = E("J'écris un acrostiche avec le mot AMI.", '<div class="card" style="background:#F2F6FD"><p class="big" style="line-height:2.3;margin:0"><b>A</b> ______________________<br><b>M</b> ______________________<br><b>I</b> ______________________</p></div>', ["ecris"], 1, "C", alpha=True, sol="Ex. : Avec toi, je ris / Main dans la main / Ici et partout")
    e2 = E("Je complète le poème « Si j'étais… ».", '<p class="big" style="line-height:2.1">Si j\'étais un oiseau, je ______________ (voler).<br>Si j\'étais la mer, je ______________ (chanter).<br>Si j\'étais un arbre, je ______________ (danser) avec le vent.</p>', ["complete"], 1, "C", alpha=True, sol="volerais · chanterais · danserais")
    e3 = E("Je relie le mot et son nom en poésie.", relie(["une ligne du poème", "un groupe de vers", "le même son à la fin"], ["une rime", "un vers", "une strophe"]), ["relie"], 1, "B", alpha=True, sol="ligne → un vers · groupe de vers → une strophe · même son → une rime")
    e4 = E("Je dis à la prof un poème court ou les paroles d'une chanson que je connais (en français ou dans ma langue).", '', ["parle"], 1, "A", alpha=True, sol="Récitation compréhensible de 2 à 4 vers.")
    b.page(CP.format(t="J'écris et je dis") + e + e2 + e3 + e4, "★ Coup de pouce")

    # ---------- Tâche finale ----------
    e = E("Je choisis deux textes pour le récital et je prépare ma fiche.", '<p class="sm" style="margin:0 0 1mm">① <b>un poème du patrimoine</b> (Verlaine, Hugo, Desbordes-Valmore, Apollinaire, La Fontaine… ou un poème de la bibliothèque) · ② <b>mon propre poème ou slam</b> (atelier C) — ou un poème de ma langue, présenté en français.</p>' +
          tall(table(["", "Texte 1 (patrimoine)", "Texte 2 (création ou ma langue)"], [["Titre et auteur", "", ""], ["Pourquoi je l'ai choisi", "", ""], ["Le thème et l'émotion", "", ""], ["Une figure de style à expliquer au public", "", ""], ["Mes marques de lecture (pauses, mots à faire entendre)", "", ""]], ["50mm", "66mm", "66mm"]), 27).replace('class="t"', 'class="t compact"'), ["lis", "ecris"], 2, "C",
          sol="Fiche complète : deux textes choisis et justifiés, thème, émotion, une figure expliquée, marques de lecture.")
    b.page(tache_head("Le récital de la classe", "Chaque élève dit deux textes devant un public (une autre classe, les parents) : un poème du patrimoine et sa propre création — ou un poème de sa langue. Avant chaque texte, il le présente en une ou deux phrases.") + e, "Tâche finale", levels=False)
    e = E("Je prépare ma présentation et je m'entraîne à dire mes textes.", '<div class="card" style="background:#FFFCF5;font-size:10pt"><b>👀 Exemple : la présentation de Daria</b><p style="margin:1mm 0 0;font-style:italic">« Je vais vous dire un poème de Victor Hugo, « Demain, dès l\'aube… ». Hugo l\'a écrit pour sa fille Léopoldine, morte très jeune. J\'ai choisi ce poème parce qu\'il parle d\'un voyage et d\'un amour qui ne finit pas. Écoutez bien le dernier vers… »</p></div>' +
          '<p class="mt2" style="margin-bottom:1mm"><b>Ma présentation du texte 1 :</b></p>' + lines(5) + '<p style="margin-bottom:1mm"><b>Ma présentation du texte 2 :</b></p>' + lines(5) +
          table(["Je m'entraîne…", "1re fois", "2e fois", "3e fois"], [[x, '<span class="chk"></span>', '<span class="chk"></span>', '<span class="chk"></span>'] for x in ["seul(e), à voix haute, devant un miroir", "devant mon voisin, qui chronomètre (2 à 3 minutes en tout)", "par cœur, avec le regard vers le public"]], ["110mm", "24mm", "24mm", "24mm"]).replace('class="t"', 'class="t compact"'), ["ecris", "parle"], 2, "C",
          sol="Présentations courtes (auteur, contexte, raison du choix) ; entraînement en trois étapes.")
    b.page(e, "Tâche finale", levels=False)
    e = E("Le jour du récital : je suis aussi un public attentif. J'écoute deux camarades et je remplis la grille.", table(["", "Camarade 1 : ............", "Camarade 2 : ............"], [["Il présente son texte (auteur, raison du choix).", '<span class="chk"></span>', '<span class="chk"></span>'], ["Il dit le texte clairement, avec les pauses.", '<span class="chk"></span>', '<span class="chk"></span>'], ["Sa voix exprime l'émotion du poème.", '<span class="chk"></span>', '<span class="chk"></span>'], ["Il regarde le public.", '<span class="chk"></span>', '<span class="chk"></span>'], ["Ce que j'ai préféré :", "", ""]], ["90mm", "46mm", "46mm"]).replace("<td></td>", '<td style="height:12mm"></td>').replace('class="t"', 'class="t compact"'), ["ecoute", "coche"], 1, "A",
          sol="Grille du public remplie ; retour bienveillant aux camarades.")
    b.page(e + table(["Je vérifie avant le récital :", "✅"], [[x, '<span class="chk"></span>'] for x in ["J'ai choisi deux textes et je sais pourquoi.", "Je connais mes textes par cœur (ou je les lis en levant souvent les yeux).", "J'ai préparé une présentation de 1 ou 2 phrases pour chaque texte.", "Je sais expliquer une figure de style d'un de mes textes.", "Je respire, je fais les pauses, je prononce les « e » qui comptent.", "Mon poème personnel a un titre, des images et une musique."]], ["160mm", "22mm"]).replace('class="t"', 'class="t compact"') + '<div class="astuce mt2">🎤 Le trac est normal ! Respire profondément trois fois avant de commencer, pose les pieds bien à plat, et regarde une personne amie dans le public.</div>' + E("Après le récital : je m'auto-évalue et j'écris ce que je ferai mieux la prochaine fois.", chk3(["J'ai dit mes textes clairement, sans aller trop vite.", "J'ai exprimé l'émotion des poèmes.", "J'ai été un public attentif."]) + lines(2), ["ecris", "coche"], 1, "C", sol="Auto-évaluation personnelle et un objectif d'amélioration."), "Tâche finale", levels=False)
    e = E("Je révise.", '<p>1. Une ligne d\'un poème : un ______________ 2. Un groupe de vers : une ______________ 3. Une strophe de 4 vers : un ______________ 4. Un vers de 12 syllabes : un ______________ 5. Rimes ABAB : rimes ______________ 6. Répétition d\'un mot en début de vers : une ______________ 7. Une image sans « comme » : une ______________</p>', ["complete"], 1, "C",
          sol="1. vers — 2. strophe — 3. quatrain — 4. alexandrin — 5. croisées — 6. anaphore — 7. métaphore")
    e2 = E("Je corrige l'analyse de Mateo : 4 erreurs (nom de la figure, citation, nombre de syllabes, explication absente).", '<div class="card" style="font-family:\'Comic Sans MS\',cursive;background:#fff;font-size:10.3pt">« Dans le poème de Verlaine, il y a une métaphore : il pleure dans mon cœur comme il pleut sur la ville. Les vers ont 8 syllabes. C\'est beau. »</div>' + lines(4), ["lis", "ecris"], 2, "C",
           sol="C'est une comparaison (outil « comme ») · la citation doit être entre guillemets avec les vers : « Il pleure dans mon cœur / Comme il pleut sur la ville » (v. 1-2) · les vers ont 6 syllabes · il faut expliquer l'effet : la pluie extérieure reflète la tristesse du poète.")
    e3 = E("Défi ! Je trouve dans le module un exemple de chaque procédé, avec le titre du texte.", tall(table(["Procédé", "Exemple et titre"], [["une comparaison", ""], ["une métaphore", ""], ["une personnification", ""], ["une anaphore", ""], ["un refrain", ""]], ["44mm", "138mm"]), 7).replace('class="t"', 'class="t compact"'), ["lis", "ecris"], 3, "C",
           sol="Ex. : comparaison « le jour pour moi sera comme la nuit » (Demain, dès l'aube…) · métaphore « Mes mots sont des valises » (Deux langues) · personnification « Il pleure dans mon cœur » (Verlaine) · anaphore « J'irai… j'irai » (Hugo) · refrain « Vienne la nuit sonne l'heure… » (Le Pont Mirabeau)")
    b.page(f'<h2>🔁 Je révise tout le module</h2>{e}{e2}{e3}', "Je révise")

    # ---------- Test ----------
    Q = [("Une ligne d'un poème s'appelle…", ["un vers", "une strophe", "une rime", "un refrain"]), ("Une strophe de quatre vers est…", ["un quatrain", "un tercet", "un distique", "un sonnet"]), ("Des rimes ABAB sont…", ["croisées", "plates", "embrassées", "libres"]),
         ("Des rimes AABB sont…", ["plates", "croisées", "embrassées", "riches"]), ("Un vers de 12 syllabes est…", ["un alexandrin", "un octosyllabe", "un hexasyllabe", "un haïku"]), ("Combien de syllabes dans « Il pleure dans mon cœur » ?", ["6", "5", "7", "8"]),
         ("En fin de vers, le « e » muet…", ["ne compte pas", "compte toujours", "compte double", "se prononce [e]"]), ("« Ses yeux brillent comme des étoiles » est…", ["une comparaison", "une métaphore", "une personnification", "une anaphore"]), ("« La mer est un miroir » est…", ["une métaphore", "une comparaison", "une hyperbole", "une allitération"]),
         ("« Le vent chante dans les arbres » est…", ["une personnification", "une comparaison", "une rime", "un refrain"]), ("« Je te l'ai dit mille fois ! » est…", ["une hyperbole", "une métaphore", "une anaphore", "une assonance"]), ("La répétition d'un son consonne s'appelle…", ["une allitération", "une assonance", "une anaphore", "une rime"]),
         ("« J'irai par la forêt, j'irai par la montagne » contient…", ["une anaphore", "une hyperbole", "une comparaison", "un haïku"]), ("Des vers répétés entre les strophes forment…", ["un refrain", "un couplet", "un tercet", "un acrostiche"]), ("Un poème dont les premières lettres forment un mot est…", ["un acrostiche", "un calligramme", "un haïku", "un slam"]),
         ("Un haïku compte…", ["3 vers (5-7-5 syllabes)", "4 vers", "14 vers", "12 syllabes par vers"]), ("« Demain, dès l'aube… » a été écrit par…", ["Victor Hugo", "Paul Verlaine", "Guillaume Apollinaire", "Marceline Desbordes-Valmore"]), ("Dans une analyse, pour justifier, je…", ["cite le texte entre guillemets", "écris « c'est beau »", "recopie tout le poème", "donne mon âge"]),
         ("Dire un poème par cœur, c'est…", ["le réciter", "le recopier", "le résumer", "le traduire"]), ("🔁 Passé simple : « Les roses s'____ dans le vent. »", ["envolèrent", "envolaient", "envolent", "envoleront"])]
    ans = [q[1][0] for q in Q]
    qrot = [2, 0, 3, 1, 1, 3, 0, 2, 3, 1, 0, 2, 1, 3, 2, 0, 3, 1, 2, 0]
    Q = [(q, o[r:] + o[:r]) for (q, o), r in zip(Q, qrot)]
    key = key_from(Q, ans)
    test_pages(b, 10, "Poésie et chanson", Q, f'<h3>B1. Lis ce quatrain écrit pour la classe. Donne le schéma et le nom des rimes, puis compte les syllabes du vers 1. (… / 3)</h3><div class="card" style="{SERIF}">Le soir descend sur la colline, / La lune allume ses lanternes, / Une chouette au loin s\'incline, / Et le vent dort dans les citernes.</div><p>Schéma : {blank()} Nom : {blank()} Syllabes du vers 1 : {blank("s")}</p><h3>B2. Relève une personnification et une métaphore dans ce quatrain. (… / 3)</h3>{lines(1, True)}<h3>B3. Écris un poème de 4 vers sur la nuit, avec une comparaison et une anaphore. (… / 4)</h3>{lines(4, True)}',
               [["dire un poème avec expression (pauses, syllabes, émotion)", "/ 3", ""], ["présenter le poème : auteur, thème, raison du choix", "/ 3", ""], ["expliquer une figure de style d'un poème du module", "/ 4", ""]],
               '<h3>1. Je relie. (… / 4)</h3>' + relie(["la pluie", "la lune", "la mer", "une rose"], ["🌊", "🌹", "🌧️", "🌙"]) + '<h3>2. J\'entoure les mots qui riment avec « nuit ». (… / 4)</h3><div class="card big">pluie · table · bruit · lit · chat · minuit</div><h3>3. Je complète la comparaison : La neige est blanche comme ______ . (… / 3)</h3><h3>4. Je complète : Si j\'étais un oiseau, je ______ (voler). Si j\'étais la mer, je ______ (chanter). (… / 4)</h3><h3>5. Oral : je dis un poème court ou une chanson. (… / 5)</h3>')
    closing(b, 10, ["Je reconnais un vers, une strophe, un quatrain, un tercet.", "Je trouve le schéma des rimes (plates, croisées, embrassées).", "Je compte les syllabes d'un vers (e muet, alexandrin).", "Je reconnais une comparaison, une métaphore, une personnification.", "J'entends une allitération, une assonance, une anaphore, un refrain.", "J'analyse un poème avec la méthode et une citation.",
                    "J'écris un acrostiche, un haïku, un poème « Si j'étais… ».", "Je dis un poème en respectant les pauses et les liaisons.", "Je lis une affiche de scène ouverte et un livret d'album.", "Je connais quelques poètes du patrimoine (Hugo, Verlaine…).", "J'ai participé au récital de la classe."],
            [("📜", "un poème, un poète"), ("📏", "un vers"), ("🧱", "une strophe, un quatrain"), ("🎵", "une rime"), ("🔢", "une syllabe, un alexandrin"), ("🔁", "un refrain, un couplet"), ("🪞", "une comparaison"), ("🖼️", "une métaphore"), ("🌬️", "une personnification"), ("💥", "une hyperbole"), ("🐍", "une allitération"), ("🎶", "une assonance"),
             ("↪️", "une anaphore"), ("🔤", "un acrostiche"), ("🌸", "un haïku"), ("✏️", "un calligramme"), ("🎤", "le slam, une scène ouverte"), ("🗣️", "réciter, déclamer"), ("🥀", "la mélancolie"), ("🕰️", "la nostalgie"), ("✨", "l'émerveillement"), ("📚", "un recueil"), ("💿", "un album, les paroles"), ("©️", "le droit d'auteur")])
    plan_de_travail(b, E, 10, ["Le vers, la strophe, les rimes", "Compter les syllabes", "Les images poétiques", "Les sons et les répétitions", "Analyser un poème", "Écrire un poème"], "☐ Choix des deux textes<br>☐ Présentations écrites<br>☐ Entraînement (3 fois)<br>☐ Récital")
    b.pages = [x.replace("padding:.8mm 1.5mm;display:flex", "padding:.3mm 1.5mm;display:flex").replace("repeat(7,1fr);gap:1.3mm", "repeat(7,1fr);gap:.7mm").replace("align-items:center;justify-content:space-between;font-size:8.5pt", "align-items:center;justify-content:space-between;font-size:8pt") for x in b.pages]  # plan compact
    if render:
        to_pdf(b.html(), '/home/claude/syllabus/out/V3_M10_eleve.pdf')

    pg, exs = helpers(b, E)
    CPp = b.marks["★ Coup de pouce"]
    days = [("1", "Collectif", f"Ouverture · BD · Verlaine ({pg('Découvrir')})", f"CP le poème (p. {CPp[0]})"), ("2", "Collectif + duo", f"Lexique : poésie, émotions ({pg('Lexique')})", "CP mots de la poésie"),
            ("3", "Rotation", f"📌 Leçon 1 vers, strophes, rimes ({pg('Leçon 1')})", "CP rimes"), ("4", "Collectif", f"📌 Leçon 2 syllabes ({pg('Leçon 2')}) · dire un poème ({pg('Sons')})", "CP taper les syllabes"),
            ("5", "Rotation", f"📌 Leçon 3 images ({pg('Leçon 3')})", f"CP images et rimes (p. {CPp[1]})"), ("6", "Collectif", f"📌 Leçon 4 sons et répétitions ({pg('Leçon 4')})", "CP comparaisons"),
            ("7", "Rotation", f"📌 Leçon 5 analyser ({pg('Consignes & école')}) · slam, album ({pg('Document de la vie')})", "CP « Si j'étais… »"), ("8", "Ateliers", f"📌 Leçon 6 écrire ({pg('Leçon 6')}) · ateliers ({pg('Atelier')}) · CE1D, DELF ({pg('Vers les épreuves')})", f"CP j'écris et je dis (p. {CPp[2]})"),
            ("9", "Classe + public", f"Tâche finale : préparation et récital ({pg('Tâche finale')})", "Dire un texte court, à deux"), ("10", "Seul", f"Test ({pg('Test')})", f"CP test ({pg('★ Coup de pouce · Test')})")]
    rot = [["🎧 Écouter-Parler", "Le slam « Deux langues » + chœur", "25 min", "Corrigé du livret"], ["📖 Lire", "Les poètes de la classe", "25 min", "Oui"], ["✏️ Écrire", "Mon poème pour le récital", "30 min", "Grille entre pairs"],
           ["🧩 Jouer", "Dominos des rimes + cadavre exquis", "20 min", "Les joueurs vérifient"], ["👩‍🏫 Table d'appui", "Coup de pouce · rimes, comparaisons", "20 min", "—"]]
    ev1 = f'''<h3>Partie B (10 points)</h3><p class="sm"><b>B1</b> : <span class="sol">ABAB · rimes croisées · 8 syllabes (Le-soir-des-cend-sur-la-col-li-n(e))</span> (1 pt chacun). · <b>B2</b> : <span class="sol">personnification : « La lune allume ses lanternes » / « le vent dort » ; métaphore : « ses lanternes » (les étoiles)</span> (1,5 pt chacun). · <b>B3</b> : 4 vers (1), comparaison (1), anaphore (1), images et langue (1).</p>
<h3>Partie C · oral (10 points)</h3><p class="sm">L'élève dit un poème du module ou sa création, par cœur ou en lisant avec le regard vers la prof : pauses, syllabes, liaisons, émotion (3) · il présente le texte : auteur, thème, raison du choix (3) · la prof lui montre un vers : il nomme la figure de style et explique son effet (4).</p>
<h3>Test ★ Coup de pouce (20 points)</h3><p class="sm"><b>1 :</b> <span class="sol">pluie → 🌧️ · lune → 🌙 · mer → 🌊 · rose → 🌹</span> (4) · <b>2 :</b> <span class="sol">pluie · bruit · lit · minuit</span> (4) · <b>3 :</b> comparaison logique (3) · <b>4 :</b> <span class="sol">volerais · chanterais</span> (4) · <b>5 :</b> récitation compréhensible (5).</p>
<h3>Lire les résultats du QCM : quelle remédiation ?</h3>{table(["Questions", "Compétence", "Si moins de la moitié est juste…"], [["1 à 7", "vers, strophes, rimes, syllabes", f"leçons 1 et 2 ({pg('Leçon 1')}, {pg('Leçon 2')}) + coup de pouce p. {CPp[0]}"], ["8 à 11", "les images", f"leçon 3 ({pg('Leçon 3')}) + coup de pouce p. {CPp[1]}"], ["12 à 14", "sons et répétitions", f"leçon 4 ({pg('Leçon 4')})"], ["15 à 19", "formes, analyse, dire", f"leçons 5 et 6 ({pg('Consignes & école')}, {pg('Leçon 6')})"], ["20", "révision (passé simple)", "module 9, leçon 2"]], ["24mm", "62mm", "96mm"])}'''
    ev2 = f'''<h2>Grille · tâche finale « Le récital »</h2>{table(["Critère", "Très bien", "Bien", "À retravailler", "Points"], [["<b>Choix et présentation</b> des textes (auteur, contexte, raison du choix)", "Claire", "Partielle", "Absente", "/ 3"], ["<b>Diction</b> : articulation, syllabes, liaisons, pauses", "Maîtrisée", "Quelques erreurs", "Difficile", "/ 4"], ["<b>Expressivité</b> : voix, rythme, émotion, regard", "Vivante", "Correcte", "Monotone", "/ 4"], ["<b>Mémorisation</b> (ou lecture fluide en levant les yeux)", "Par cœur", "Avec aide", "Lecture hachée", "/ 2"], ["<b>Création personnelle</b> : images, sons, structure, titre", "Riche", "Simple", "Inachevée", "/ 5"], ["<b>Public</b> : écoute et grille d'observation", "Attentif", "Correct", "Inattentif", "/ 2"]], ["66mm", "30mm", "30mm", "34mm", "22mm"])}
<h2 class="mt4">Différencier et remédier</h2>{table(["Difficulté", "Remédiation"], [["Rimes", "Écouter le son, pas l'orthographe : dire les mots à voix haute, colorier les sons de fin de vers ; dictionnaire de rimes en ligne avec la prof."], ["Syllabes", "Taper les syllabes sur la table ; barrer d'abord les « e » finaux et les « e » devant voyelle ; travailler en duo (l'un compte, l'autre vérifie)."], ["Figures de style", "Affiche « comme = comparaison ; sans comme = métaphore ; chose qui agit comme un humain = personnification » ; trier des cartes-exemples."], ["Trac, timidité", "Dire le texte à deux ou en chœur ; enregistrer sa voix à l'avance ; commencer par sa langue maternelle, puis le français."], ["Élève rapide", "Apprendre un sonnet entier ; écrire un calligramme complexe ; participer à une scène ouverte de slam ; traduire un poème de sa langue en français."]], ["50mm", "132mm"])}'''
    rep = f'''<h2>Poésie et chanson : repères</h2>
<div class="attention"><b>Sujets sensibles.</b> « Demain, dès l'aube… » parle du deuil d'un enfant (Léopoldine Hugo, noyée en 1843 à 19 ans) ; « Il pleure dans mon cœur » d'une tristesse sans cause. Prévenir avant la lecture, laisser les élèves libres de ne pas dire ces textes au récital. Valoriser les poèmes et chansons des langues des élèves : les présenter en français est une compétence à part entière.</div>
{table(["Repère", "Ce qu'il faut savoir (vérifié en novembre 2026)"], [["Les poètes du module", "Marceline Desbordes-Valmore (1786-1859) : « Les roses de Saadi » paraît dans les <i>Poésies inédites</i> (1860), après sa mort · Victor Hugo (1802-1885) : « Demain, dès l'aube… », daté du 3 septembre 1847, dans <i>Les Contemplations</i> (1856) · Paul Verlaine (1844-1896) : « Il pleure dans mon cœur », <i>Romances sans paroles</i> (1874) · Guillaume Apollinaire (1880-1918) : « Le Pont Mirabeau », <i>Alcools</i> (1913) · Racine (1639-1699) : vers d'<i>Andromaque</i> (1667). Tous ces textes sont dans le domaine public (en Belgique, 70 ans après la mort de l'auteur)."], ["La poésie en Belgique", "Émile Verhaeren (1855-1916) est le grand poète belge du symbolisme. Depuis 2014, la Belgique désigne un « Poète national », alternativement francophone et néerlandophone (Charles Ducal fut le premier ; Laurence Vielle, Els Moors, Carl Norac, Mustafa Kör ont suivi). Laurence Vielle a reçu en novembre 2026 le prix Guillaume-Apollinaire."], ["Journée mondiale", "La Journée mondiale de la poésie, proclamée par l'UNESCO en 1999, a lieu chaque année le 21 mars."], ["Le droit d'auteur", "Les paroles de chansons et les poèmes récents sont protégés : on peut les lire en classe, mais pas les publier (site, journal de classe) sans autorisation. En Belgique, la SABAM gère les droits de nombreux auteurs et compositeurs. Les textes de l'album « Racines » et le slam « Deux langues » sont inventés pour le cahier."], ["Taras Chevtchenko", "Taras Chevtchenko (1814-1861), poète et peintre, est considéré comme le poète national de l'Ukraine (cité par Daria dans la BD)."]], ["30mm", "152mm"])}
<div class="attention mt2"><b>Fictif :</b> le slam « Deux langues », les poèmes des élèves, les quatrains et virelangues d'exercice, l'album « Racines » de Lina K., la scène ouverte « Slam'ados » et le slameur Nassim B. ; le calligramme « Il pleut des mots doux ». Les textes de Hugo, Verlaine, Desbordes-Valmore, Apollinaire, Racine et la chanson traditionnelle sont authentiques.</div>
<h3>Belgicismes du module</h3><p class="sm"><b>septante, nonante</b> · une <b>farde</b> pour ranger ses poèmes · « <b>savoir</b> » au sens de pouvoir (« Tu sais dire ton poème ? ») · le <b>centre culturel</b> (institution culturelle locale reconnue par la Fédération Wallonie-Bruxelles). Applaudir en <b>claquant des doigts</b> est une habitude des scènes de slam, en Belgique comme en France.</p>'''
    import re as _re
    def _court(t, n=90):
        t2 = _re.sub(r"<[^>]+>", "", t)
        return t if len(t2) <= n else t2[:n].rsplit(" ", 1)[0] + "…"
    E.sols = [(p, n, _court(t), s) for p, n, t, s in E.sols]
    import lib.module as _LM
    _pg = _LM.paginate
    _LM.paginate = lambda rows, w, bf, bb: _pg(rows, w, bf + (70 if bf == 190 else BUMP), bb + BUMP)
    _tb = _LM.table
    _LM.table = lambda *a, **k: compact(_tb(*a, **k))
    T = teacher_book(b, E, "V3 · M10", "", MC, 10, "Poésie et chanson",
                     "<li><b>Communication :</b> lire, dire et écrire un poème ; présenter un texte ; participer à un récital.</li><li><b>Lexique :</b> la poésie (vers, strophe, quatrain, rime, syllabe, alexandrin, refrain, couplet, recueil), les émotions poétiques (mélancolie, nostalgie, émerveillement, tendresse), dire la poésie (réciter, déclamer, slam, scène ouverte).</li><li><b>Langue :</b> les figures de style simples (comparaison, métaphore, personnification, hyperbole, allitération, assonance, anaphore) ; compter les syllabes (e muet, élision, diérèse) ; le conditionnel dans « Si j'étais… ».</li><li><b>Oral :</b> dire un poème (souffle, pauses, liaisons) ; [ʁ] / [l].</li><li><b>FLSco :</b> analyser un poème (méthode en 5 étapes, paragraphe idée-citation-explication) ; consignes relève, identifie, interprète, commente, justifie.</li><li><b>Épreuves :</b> CE1D (lire et analyser un poème) ; DELF B1 production orale, exercice en interaction.</li><li><b>Documents :</b> poèmes du domaine public (Hugo, Verlaine, Desbordes-Valmore, Apollinaire), chanson traditionnelle, slam et poèmes écrits pour la classe, affiche de scène ouverte, livret d'album.</li>",
                     '<p class="sm"><b style="color:#E4572E">Indispensable</b> : vers, strophe, rime, comparaison, métaphore, personnification, dire un poème avec les pauses.</p><p class="sm"><b style="color:#d9a400">Important</b> : schéma des rimes, syllabes et e muet, sons et répétitions, analyse avec citation.</p><p class="sm"><b style="color:#2BA88F">Enrichissement</b> : rimes riches, diérèse, hyperbole, CE1D, DELF B1, slam en public.</p>',
                     "Un exemplaire du cahier par élève · enregistrements des poèmes (voix de la prof ou d'un comédien) · recueils de poésie de la bibliothèque · dominos des rimes découpés · feuilles A4 pour les calligrammes · un micro (même éteint !) pour le récital · si possible, la venue d'un slameur ou d'une slameuse.", "<b>Avant de commencer :</b> annoncer le récital dès le jour 1 et fixer la date avec le public invité (autre classe, parents). Chaque élève choisit tôt son poème du patrimoine pour avoir le temps de l'apprendre. Encourager les élèves à apporter un poème ou une chanson de leur langue : ces textes font souvent les plus beaux moments du récital.",
                     days, "« Le vers du jour » : un vers écrit au tableau, on compte les syllabes et on cherche la figure · « Une rime par élève » sur un mot donné · lecture à voix haute d'un poème court, chaque jour par un élève différent.", rot, key, (ev1, ev2), extra_pages=[(rep, "Repères")], start=tstart)
    _LM.paginate = _pg
    _LM.table = _tb
    if render:
        to_pdf(T.html(), '/home/claude/syllabus/out/V3_M10_prof.pdf')
    return b, T


if __name__ == "__main__":
    b, T = build_v3m10()
    print(b.n, T.n)


