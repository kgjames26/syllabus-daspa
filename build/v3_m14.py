"""Volume 3 · Module 14 « Le théâtre » (B1 + français de scolarisation).

Lire et jouer une scène : le texte théâtral (personnages, répliques, didascalies, acte, scène, monologue, aparté),
les procédés du comique, la mise en voix et la mise en scène.
Langue : les types de phrases (déclarative, interrogative, impérative, exclamative) et l'exclamation (interjections,
Quel… !, Que… !, Comme… !) ; les formes de phrases (affirmative / négative, neutre / emphatique, active / passive).
FLSco : lire un texte théâtral. Fil rouge : la classe monte un spectacle pour la fête de fin d'année de l'Athénée.
Textes : extraits de Molière (domaine public) — L'Avare (IV, 7), Le Bourgeois gentilhomme (II, 4), Les Fourberies de
Scapin (II, 7) — et une scène originale, « Le GSM disparu » (constante GSM).
Visuels : plateau() (plan de la scène : cour, jardin, avant-scène, coulisses), masques() (comédie / tragédie, SVG),
scene() (mise en page d'un texte théâtral : noms, répliques, didascalies en italique).
Faits réels : Molière (1622-1673), dates des pièces ; marionnettes liégeoises (Tchantchès) ; Article 27 (asbl belge).
"""
import sys
sys.path.insert(0, '/home/claude/syllabus')
from lib.base import *
from lib.art import *
from lib.module import *
from lib.v3 import CP, CPCOL, EPR, disc_tag
from lib.render import to_pdf

import os
BUMP = int(os.environ.get("BUMP", "58"))
SCR = int(os.environ.get("SCR", "120"))
MC = "#7A3E9D"
TINT = "#F2E9F7"


def chk3(items, w=128):
    return table(["", "😀", "🙂", "😕"], [[x, '<span class="chk"></span>', '<span class="chk"></span>', '<span class="chk"></span>'] for x in items], [f"{w}mm", "18mm", "18mm", "18mm"])


def tall(html, h):
    return html.replace("<td></td>", f'<td style="height:{h}mm"></td>')


def compact(html):
    return html.replace('class="t"', 'class="t compact"')


def card(t, lh=2):
    return f'<div class="card" style="line-height:{lh}">{t}</div>'


def scene(lines_, titre="", fs=9.6, num=False, bg="#FFFDF6"):
    """Texte théâtral : lines_ = [(PERSONNAGE ou None pour une didascalie seule, texte)] ; didascalies entre [ ]."""
    import re
    out = ""
    for k, (p, t) in enumerate(lines_, 1):
        t = re.sub(r"\[([^\]]+)\]", r'<i style="color:#6b5a7a">(\1)</i>', t)
        n = f'<span class="xs muted" style="display:inline-block;width:5mm">{k}</span>' if num else ""
        if p is None:
            out += f'<p style="margin:.8mm 0;text-align:center">{n}<i style="color:#6b5a7a">{t}</i></p>'
        else:
            out += f'<p style="margin:.8mm 0">{n}<b style="letter-spacing:.5px;color:#1F2A44">{p}</b>. — {t}</p>'
    tt = f'<div class="c" style="font-weight:800;color:{MC};margin-bottom:1.2mm">{titre}</div>' if titre else ""
    return f'<div class="doc" style="transform:none;background:{bg};border:1.5px solid #9aa1b1;padding:2.5mm 4mm;font-size:{fs}pt;line-height:1.38;font-family:\'DejaVu Serif\'">{tt}{out}</div>'


AVARE = [(None, "SCÈNE VII · HARPAGON. [Il crie au voleur dès le jardin, et vient sans chapeau.]"),
         ("HARPAGON", "Au voleur ! au voleur ! à l'assassin ! au meurtrier ! Justice, juste Ciel ! je suis perdu, je suis assassiné, on m'a coupé la gorge, on m'a dérobé mon argent. Qui peut-ce être ? Qu'est-il devenu ? Où est-il ? Où se cache-t-il ? Que ferai-je pour le trouver ? Où courir ? Où ne pas courir ? N'est-il point là ? N'est-il point ici ? Qui est-ce ? Arrête. Rends-moi mon argent, coquin… [Il se prend lui-même le bras.] Ah ! c'est moi. Mon esprit est troublé, et j'ignore où je suis, qui je suis, et ce que je fais.")]

BOURGEOIS = [("MONSIEUR JOURDAIN", "Quoi ? quand je dis : « Nicole, apportez-moi mes pantoufles, et me donnez mon bonnet de nuit », c'est de la prose ?"),
              ("MAÎTRE DE PHILOSOPHIE", "Oui, Monsieur."),
              ("MONSIEUR JOURDAIN", "Par ma foi ! il y a plus de quarante ans que je dis de la prose sans que j'en susse rien, et je vous suis le plus obligé du monde de m'avoir appris cela.")]

GSM = [(None, "Le GSM disparu · Une scène originale en un acte. Personnages : MATEO, FATOU, YONAS, MADAME LAMBERT. Dans la classe, à la récréation."),
       ("MATEO", "[entrant en courant, affolé] Mon GSM ! Mon GSM ! Quelqu'un a vu mon GSM ?"),
       ("FATOU", "[sans lever les yeux de son cahier] Encore ? C'est la troisième fois cette semaine !"),
       ("MATEO", "Cette fois, c'est sérieux ! On me l'a volé ! Quel malheur ! Toutes mes photos, toute ma musique…"),
       ("YONAS", "[à part, au public] Toute sa musique… Enfin un peu de silence dans le bus !"),
       ("MATEO", "Qu'est-ce que tu dis, toi ?"),
       ("YONAS", "Moi ? Rien. Je dis que c'est terrible. Vraiment terrible."),
       ("MATEO", "[il regarde sous les bancs, dans la poubelle, derrière le tableau] Il n'est pas là… Il n'est pas ici… Où est-il ? Qui l'a pris ? [Il saisit Yonas par le bras.] C'est toi !"),
       ("YONAS", "Lâche-moi ! Je n'ai rien pris ! Je n'ai jamais touché à ton GSM !"),
       ("FATOU", "Mateo, calme-toi. Réfléchis : où l'as-tu utilisé pour la dernière fois ?"),
       ("MATEO", "Pendant le cours de maths… Non ! Il est interdit à l'école. Je ne l'ai pas sorti du tout."),
       ("FATOU", "Donc, tu ne l'as pas utilisé depuis ce matin ?"),
       ("MATEO", "Jamais ! Enfin… presque jamais. [Un téléphone sonne. Silence. Tous regardent Mateo.]"),
       ("YONAS", "Tiens ! Ta poche chante, Mateo."),
       ("MATEO", "[il sort le GSM de sa poche, rouge de honte] Ah ! C'est… c'est le mien."),
       ("MADAME LAMBERT", "[entrant] Que se passe-t-il ici ? Et qu'est-ce que c'est que ce téléphone allumé ?"),
       ("MATEO", "Rien, Madame ! C'est… c'est un voleur que j'ai attrapé."),
       ("FATOU et YONAS", "[ensemble, au public] Quel comédien !")]


def plateau(w=150):
    """Plan de la scène vu du public : jardin à gauche, cour à droite."""
    return (f'<svg viewBox="0 0 200 112" width="{w}mm" style="max-width:100%">'
            '<rect x="10" y="6" width="180" height="70" fill="#F2E9F7" stroke="#7A3E9D" stroke-width="1.2"/>'
            '<rect x="10" y="6" width="22" height="70" fill="#E0D0EC"/><rect x="168" y="6" width="22" height="70" fill="#E0D0EC"/>'
            '<rect x="32" y="62" width="136" height="14" fill="#EBDDF4"/>'
            '<text x="21" y="44" font-size="6" text-anchor="middle" font-family="Poppins" transform="rotate(-90 21 44)">coulisses</text>'
            '<text x="179" y="44" font-size="6" text-anchor="middle" font-family="Poppins" transform="rotate(90 179 44)">coulisses</text>'
            '<text x="100" y="22" font-size="7" text-anchor="middle" font-family="Poppins">fond de scène (lointain)</text>'
            '<text x="100" y="45" font-size="9" text-anchor="middle" font-family="Poppins" font-weight="700" fill="#7A3E9D">LA SCÈNE (le plateau)</text>'
            '<text x="100" y="71" font-size="7" text-anchor="middle" font-family="Poppins">avant-scène</text>'
            '<text x="50" y="58" font-size="8" text-anchor="middle" font-family="Poppins" font-weight="700">JARDIN</text>'
            '<text x="150" y="58" font-size="8" text-anchor="middle" font-family="Poppins" font-weight="700">COUR</text>'
            + "".join(f'<circle cx="{x}" cy="{y}" r="3" fill="#9aa1b1"/>' for y in (90, 100) for x in range(30, 175, 12)) +
            '<text x="100" y="110" font-size="7" text-anchor="middle" font-family="Poppins">LE PUBLIC (la salle)</text></svg>')


def masques(w=40):
    """Masques de la comédie et de la tragédie."""
    m = lambda cx, smile, col: (f'<ellipse cx="{cx}" cy="30" rx="18" ry="22" fill="{col}" stroke="#1F2A44" stroke-width="1.2"/>'
                                f'<ellipse cx="{cx - 7}" cy="24" rx="4" ry="3" fill="#1F2A44"/><ellipse cx="{cx + 7}" cy="24" rx="4" ry="3" fill="#1F2A44"/>'
                                + (f'<path d="M{cx - 9} 38 Q{cx} 48 {cx + 9} 38" stroke="#1F2A44" stroke-width="2" fill="none"/>' if smile else f'<path d="M{cx - 9} 44 Q{cx} 34 {cx + 9} 44" stroke="#1F2A44" stroke-width="2" fill="none"/>'))
    return f'<svg viewBox="0 0 90 56" width="{w}mm">{m(24, True, "#FFD166")}{m(66, False, "#9DB4E8")}</svg>'


def build_v3m14(start=1, tstart=1, render=True):
    b = Book("V3 · M14", "Volume 3 · Je réussis à l'école · Module 14 · Le théâtre", MC, start=start)
    E = Ex(b)
    P = {}
    vis = ('<div class="flex" style="justify-content:space-around;align-items:flex-end">' + avatar("mateo", 80, "surpris") + masques(34) + avatar("fatou", 80, "rire")
           + '<div style="font-size:32pt">🎭 🎟️</div>' + avatar("yonas", 80, "rire") + avatar("prof", 80, "sourire") + '</div>')
    opening(b, MC, 14, "Le théâtre", vis, [("📜", "lire un texte de théâtre (répliques, didascalies)"), ("🎭", "découvrir Molière et le comique"), ("❓", "reconnaître les types de phrases et l'exclamation"),
            ("🔄", "utiliser les formes de phrases (négative, emphatique)"), ("🗣️", "dire un texte avec la bonne intonation"), ("🎬", "jouer une scène devant un public")],
            ["Es-tu déjà allé(e) au théâtre ? Qu'as-tu vu ?", "Dans ton pays, quels spectacles regarde-t-on (conte, marionnettes, théâtre de rue) ?", "As-tu le trac quand tu parles devant la classe ?"],
            ["une pièce", "une scène", "un acte", "une réplique", "une didascalie", "un personnage", "un comédien", "le public", "la mise en scène", "une exclamation", "répéter"], TINT)

    # ---------- Découvrir ----------
    P["bd"] = b.n + 1
    bd = '<div class="grid2" style="gap:3mm">' + "".join([
        bd_case(1, lr("prof", ["Pour la fête de fin d'année, notre classe va jouer une pièce de théâtre !"], "mateo", ["Génial ! Moi, je veux le rôle principal !"], "sourire", "rire")),
        bd_case(2, lr("amina", ["Une pièce ? Mais je n'ai jamais fait de théâtre… Et si j'oublie mon texte ?"], "educ", ["Tout le monde a le trac ! On va répéter souvent : c'est ça, le secret."], "pense", "sourire")),
        bd_case(3, lr("prof", ["Nous lirons d'abord Molière, un auteur français du XVIIe siècle. Ses comédies font rire depuis plus de 350 ans !"], "bilal", ["350 ans ? Et ça fait encore rire ?"], "sourire", "surpris")),
        bd_case(4, lr("yonas", ["« Au voleur ! au voleur ! à l'assassin ! » C'est quoi, ce texte ?"], "prof", ["C'est Harpagon, dans L'Avare : un vieil homme qui a perdu son argent. Regarde les points d'exclamation : il crie, il panique !"], "rire", "sourire")),
        bd_case(5, lr("fatou", ["Et les mots en italique, entre parenthèses ? On doit les lire ?"], "prof", ["Non, ce sont les didascalies : elles disent aux comédiens comment bouger et comment parler."], "pense", "sourire")),
        bd_case(6, lr("daria", ["Et si on écrivait aussi notre propre scène ?"], "mateo", ["Oui ! Une histoire de GSM perdu… J'ai déjà le titre !"], "sourire", "rire")),
    ]) + '</div>'
    e = E("J'écoute et je lis la BD : la classe va jouer une pièce.", bd, ["ecoute", "lis"], 1, "A",
          script="Lire deux fois en changeant de voix ; exagérer la panique sur la réplique d'Harpagon.", sol="Activité orale.")
    b.page(f'<h2>Découvrir · En scène !</h2>{e}', "Découvrir")
    e = E("Je réponds par une phrase complète.", f'<p>1. Pour quelle occasion la classe va-t-elle jouer une pièce ? {blank("xl")}</p><p>2. De quoi Amina a-t-elle peur ? Que lui conseille M. Diallo ? {blank("xl")}</p><p>3. Qui est Molière ? {blank("xl")}</p><p>4. Pourquoi Harpagon crie-t-il ? {blank("xl")}</p><p>5. Qu\'est-ce qu\'une didascalie ? {blank("xl")}</p>', ["lis", "ecris"], 1, "B",
          sol="1. Pour la fête de fin d'année. — 2. Elle a peur d'oublier son texte ; M. Diallo lui conseille de répéter souvent (tout le monde a le trac). — 3. Un auteur français du XVIIe siècle qui a écrit des comédies. — 4. Parce qu'on lui a volé son argent. — 5. Une indication (en italique, entre parenthèses) qui dit aux comédiens comment bouger et parler ; on ne la lit pas à voix haute.")
    e2 = E("Vrai ou faux ? Je coche et je corrige les phrases fausses.", vf(["Mateo veut un petit rôle.", "Les comédies de Molière ont plus de 350 ans.", "Les didascalies se lisent à voix haute pendant le spectacle.", "Daria propose d'écrire une scène originale."]), ["lis", "coche"], 1, "B",
           sol="Faux (le rôle principal) · Vrai · Faux (elles ne se disent pas) · Vrai")
    e3 = E("Je relève dans la BD une phrase qui pose une question, une phrase qui exprime une émotion forte et une phrase qui donne un ordre ou un conseil.", tall(compact(table(["❓ une question", "❗ une émotion forte", "👉 un ordre, un conseil"], [["", "", ""]], ["60mm", "61mm", "61mm"])), 14), ["lis", "ecris"], 2, "C",
           sol="Ex. : « Et si j'oublie mon texte ? » / « Et ça fait encore rire ? » · « Génial ! » / « Au voleur ! » · « Regarde les points d'exclamation » (impératif)")
    e4 = E("Et toi ? Raconte un spectacle que tu as vu (théâtre, cirque, conte, marionnettes, concert), ici ou dans ton pays : où, quoi, ce que tu as ressenti.", lines(3), ["ecris", "duo"], 2, "C",
           sol="Ex. : Dans mon pays, j'ai vu un spectacle de marionnettes au marché. Un conteur racontait l'histoire d'un roi. Tout le monde riait, moi aussi !")
    b.page(f'{e}{e2}{e3}{e4}', "Découvrir")
    e = E("J'observe le plan d'une scène de théâtre. Je lis les mots à voix haute.", '<div class="c">' + plateau(150) + '</div><div class="astuce" style="margin:1.5mm 0 0">💡 Vus <b>de la salle</b>, le <b>jardin</b> est à gauche et la <b>cour</b> à droite. Moyen mnémotechnique : <b>J</b>ésus-<b>C</b>hrist → <b>J</b>ardin à gauche, <b>C</b>our à droite (les initiales, lues de gauche à droite). Les comédiens attendent dans les <b>coulisses</b>, invisibles du public.</div>', ["lis", "regarde"], 1, "B",
          sol="Lecture ; faire montrer jardin et cour dans la classe (vue depuis les bancs).")
    e2 = E("J'écoute les indications de la metteuse en scène et je dessine le trajet de chaque comédien sur le plan (une couleur par comédien).", '<div class="c">' + plateau(110) + '</div>', ["ecoute", "dessine"], 2, "A",
           script="1. Mateo entre côté jardin et court jusqu'au centre de la scène. 2. Fatou est assise à l'avant-scène, côté cour. 3. Yonas sort des coulisses côté cour et vient au milieu, au fond de la scène.",
           sol="Mateo : de la gauche (jardin) vers le centre · Fatou : devant, à droite (avant-scène, cour) · Yonas : de la droite (coulisses cour) vers le fond, au milieu.")
    b.page(f'<h2>Découvrir · Le lieu du théâtre</h2>{e}{e2}', "Découvrir")

    # ---------- Lexique ----------
    e = E("Les mots du théâtre. Je lis l'encadré.", '<div class="grid2">' + "".join(f'<div class="card" style="background:#fff"><b>{t}</b><p class="sm" style="margin:1mm 0 0">{d}</p></div>' for t, d in [
        ("📜 Le texte", "une <b>pièce</b> (de théâtre) · un <b>acte</b> (une grande partie) · une <b>scène</b> (une partie de l'acte) · une <b>réplique</b> (ce que dit un personnage) · une <b>tirade</b> (une longue réplique) · un <b>monologue</b> (un personnage seul parle) · un <b>aparté</b> (au public, les autres « n'entendent pas ») · une <b>didascalie</b>"),
        ("🎭 Les gens", "l'<b>auteur</b>, le <b>dramaturge</b> · un <b>personnage</b> · un <b>comédien</b>, une <b>comédienne</b>, un <b>acteur</b> · un <b>rôle</b> · le <b>metteur en scène</b> · le <b>public</b>, les <b>spectateurs</b> · une <b>troupe</b>"),
        ("🎬 Le spectacle", "la <b>scène</b>, le <b>plateau</b> · les <b>coulisses</b> · le <b>rideau</b> · le <b>décor</b> · les <b>costumes</b> · les <b>accessoires</b> · l'<b>éclairage</b> · une <b>représentation</b> · la <b>première</b> · les <b>applaudissements</b>"),
        ("🎟️ Les genres et les verbes", "une <b>comédie</b> (pour faire rire) · une <b>tragédie</b> (une fin malheureuse) · une <b>farce</b> · <b>jouer</b> un rôle · <b>répéter</b>, une <b>répétition</b> · <b>apprendre</b> son texte · <b>improviser</b> · <b>avoir le trac</b> · <b>saluer</b>")]) + '</div>', ["lis"], 1, "B", sol="Lecture de l'encadré.")
    e2 = E("Je complète avec : réplique · coulisses · répétition · trac · costumes · rideau.", card("1. Avant d'entrer en scène, Amina tremble : elle a le ______________ . 2. Mateo attend son tour dans les ______________ . 3. Le ______________ se lève : le spectacle commence. 4. Fatou a oublié sa ______________ : Yonas lui souffle le texte. 5. Les ______________ du XVIIe siècle sont magnifiques. 6. Demain, nous avons une ______________ générale."), ["complete"], 1, "C",
           sol="1. trac — 2. coulisses — 3. rideau — 4. réplique — 5. costumes — 6. répétition")
    e3 = E("Monologue, tirade, aparté ou dialogue ? Je relie.", relie(["Harpagon est seul et parle de son argent volé.", "Yonas dit une phrase au public ; Mateo ne l'entend pas.", "Fatou et Mateo se parlent, chacun à son tour.", "Un personnage parle très longtemps devant les autres."], ["un dialogue", "une tirade", "un monologue", "un aparté"]), ["lis", "relie"], 2, "B",
           sol="Harpagon seul → monologue · Yonas au public → aparté · Fatou et Mateo → dialogue · parle longtemps → tirade")
    b.page(f'<h2>Les mots du théâtre</h2>{e}{e2}{e3}', "Lexique")
    e = E("Les émotions sur scène. Je relie l'émotion et la didascalie qui la montre.", relie(["la colère", "la peur", "la joie", "la tristesse", "la surprise"], ["[en sautant de joie]", "[les yeux pleins de larmes]", "[il recule, tremblant]", "[en frappant du poing sur la table]", "[bouche bée, il laisse tomber son sac]"]), ["lis", "relie"], 1, "B",
          sol="colère → en frappant du poing · peur → il recule, tremblant · joie → en sautant de joie · tristesse → les yeux pleins de larmes · surprise → bouche bée")
    e2 = E("Comment le dire ? Je complète chaque didascalie avec un adverbe : doucement · sèchement · timidement · joyeusement · ironiquement.", card("1. « Bonjour… je… je suis nouvelle. » [______________] 2. « Sors d'ici tout de suite ! » [______________] 3. « Bravo, quelle bonne idée de perdre les clés ! » [______________] 4. « Chut, le bébé dort. » [______________] 5. « On a gagné ! » [______________]"), ["complete"], 2, "C",
           sol="1. timidement — 2. sèchement — 3. ironiquement — 4. doucement — 5. joyeusement")
    e3 = E("Comédie ou tragédie ? Je lis les résumés (pièces imaginaires) et je coche.", compact(table(["", "comédie", "tragédie"], [[x, '<span class="chk"></span>', '<span class="chk"></span>'] for x in ["Un valet rusé trompe son vieux maître pour aider deux amoureux ; tout finit par un mariage.", "Une reine doit choisir entre son amour et son pays ; elle meurt à la fin.", "Un homme se croit malade et se fait soigner par une servante déguisée en médecin.", "Deux familles ennemies se battent ; les deux jeunes héros perdent la vie."]], ["140mm", "21mm", "21mm"])), ["lis", "coche"], 1, "B",
           sol="comédie · tragédie · comédie · tragédie")
    e4 = E("Défi ! J'écris trois didascalies pour une scène où un élève arrive en retard en classe (une pour l'entrée, une pour le ton, une pour un geste).", lines(3), ["ecris"], 3, "C",
           sol="Ex. : [Il entre sur la pointe des pieds, essoufflé.] · [d'une petite voix] · [Il cache son sac derrière son dos.]")
    b.page(f'<h2>Les émotions et les genres</h2>{e}{e2}{e3}{e4}', "Lexique")

    # ---------- Leçon 1 (FLSco) : lire un texte théâtral ----------
    P["avare"] = b.n + 1
    l1 = lecon("Lire un texte théâtral", '<p class="sm" style="margin-bottom:1.5mm">Un texte de théâtre est écrit pour être <b>joué</b>. Il n\'y a pas de narrateur : l\'histoire avance par les <b>paroles</b> des personnages. On y trouve :</p>' +
        compact(table(["Élément", "Comment le reconnaître ?"], [["la liste des <b>personnages</b>", "au début de la pièce, avec leur rôle (« HARPAGON, père de Cléante et d'Élise »)"], ["l'<b>acte</b> et la <b>scène</b>", "en chiffres romains : Acte IV, scène 7 = (IV, 7) ; une nouvelle scène commence quand un personnage entre ou sort"], ["les <b>répliques</b>", "le nom du personnage (souvent en majuscules), puis ce qu'il dit"], ["les <b>didascalies</b>", "en italique ou entre parenthèses : gestes, ton, lieu, entrées et sorties — on ne les dit pas"]], ["48mm", "134mm"])) +
        '<p class="sm" style="margin:2mm 0 1mm"><b>Molière</b> (Jean-Baptiste Poquelin, 1622-1673), auteur et comédien français. Dans <b>L\'Avare</b> (1668), Harpagon aime tellement l\'argent qu\'il cache une cassette pleine d\'or dans son jardin. On la lui vole…</p>' +
        scene(AVARE, "L'Avare, acte IV, scène 7 (Molière, 1668)", 9.4) +
        '<div class="astuce" style="margin:2mm 0 0">🧭 <b>Pour lire une scène, je me demande :</b> ① <b>Qui</b> parle, à qui ? ② <b>Où</b> et <b>quand</b> ? (didascalies) ③ <b>Que se passe-t-il</b> ? (le problème, l\'enjeu) ④ <b>Comment</b> les personnages parlent-ils ? (ponctuation, ton) ⑤ Quel <b>effet</b> sur le public ? (rire, peur, émotion)</div>')
    e = E(f"Je relis le monologue d'Harpagon (p. {P['avare']}). Je réponds.", f'<p class="sm">1. Pourquoi est-ce un <b>monologue</b> ? Combien de personnages sont en scène ? {blank("xl")}</p><p class="sm">2. Que vient-il d\'arriver à Harpagon ? {blank("xl")}</p><p class="sm">3. Compte les points d\'interrogation et les points d\'exclamation. Que montrent-ils de son état ? {blank("xl")}</p><p class="sm">4. « Rends-moi mon argent, coquin… » : à qui Harpagon parle-t-il vraiment ? Pourquoi est-ce drôle ? {blank("xl")}</p><p class="sm">5. Relève une exagération (une hyperbole) au début de la réplique. {blank("xl")}</p>', ["lis", "ecris"], 2, "B",
          sol="1. Harpagon est seul en scène (un seul nom au début de la scène) : il parle sans interlocuteur. — 2. On lui a volé son argent (sa cassette). — 3. 10 points d'interrogation et 6 points d'exclamation : il panique, il est affolé, il ne sait plus où il est. — 4. Il se parle à lui-même : il attrape son propre bras en croyant tenir le voleur ; c'est un comique de geste et de situation. — 5. « je suis assassiné, on m'a coupé la gorge » (il exagère : on lui a seulement volé son argent).")
    b.page(f'<span class="tag-doc">🎒 FRANÇAIS DE L\'ÉCOLE</span>{l1}{e}', "Consignes & école")
    e2 = E("Je repère les éléments du texte théâtral. Je relie.", relie(["IV, 7", "Il crie au voleur dès le jardin, et vient sans chapeau.", "Il se prend lui-même le bras.", "Au voleur ! au voleur !"], ["une réplique", "l'acte et la scène", "une didascalie de geste", "une didascalie de lieu et de costume"]), ["lis", "relie"], 1, "B",
           sol="IV, 7 → acte et scène · Il crie… sans chapeau → didascalie de lieu et de costume · Il se prend… → didascalie de geste · Au voleur ! → réplique")
    e = E("Je lis la scène originale « Le GSM disparu » avec mon groupe (4 lecteurs). Je ne lis pas les didascalies : je les joue !", scene(GSM, "", 9.1, True), ["lis", "parle", "groupe"], 1, "A",
          sol="Lecture expressive à quatre voix ; les didascalies sont mimées.")
    P["gsm"] = b.n + 1
    b.page(f'{e2}<h2>Une scène originale · Le GSM disparu</h2>{e}', "Consignes & école")
    e = E(f"Je relis « Le GSM disparu » (p. {P['gsm']}). Je réponds.", f'<p class="sm">1. Combien y a-t-il de personnages ? Où se passe la scène ? {blank("xl")}</p><p class="sm">2. Relève un aparté. Comment le reconnais-tu ? {blank("xl")}</p><p class="sm">3. Quelle réplique d\'Harpagon Mateo imite-t-il (ligne 8) ? {blank("xl")}</p><p class="sm">4. Quel est le coup de théâtre (le moment où tout change) ? {blank("xl")}</p><p class="sm">5. Pourquoi la fin est-elle drôle ? {blank("xl")}</p>', ["lis", "ecris"], 2, "B",
          sol="1. Quatre personnages (Mateo, Fatou, Yonas, Mme Lambert) ; dans la classe, à la récréation. — 2. « Toute sa musique… Enfin un peu de silence dans le bus ! » : didascalie « à part, au public ». — 3. « Où est-il ? Qui l'a pris ? … C'est toi ! » imite « Où est-il ? … Qui est-ce ? Arrête. » et le geste de saisir le bras. — 4. Le téléphone sonne dans la poche de Mateo. — 5. Mateo, pris en faute, invente un mensonge (« un voleur que j'ai attrapé ») et Fatou et Yonas le commentent ensemble au public.")
    e2 = E("Je transforme le récit en texte théâtral : j'écris 4 répliques avec des didascalies.", '<div class="card sm" style="background:#fff">Récit : Daria entre dans la classe, très fâchée. Elle demande à Bilal s\'il a pris son cahier. Bilal, surpris, répond qu\'il ne l\'a pas touché. Daria s\'excuse : le cahier était dans son sac.</div>' + lines(4), ["lis", "ecris"], 3, "C",
           sol="Ex. : DARIA. — [entrant, furieuse] Bilal ! C'est toi qui as pris mon cahier ? / BILAL. — [surpris, les mains levées] Moi ? Je ne l'ai même pas touché ! / DARIA. — [elle fouille son sac, gênée] Oh… Il était là. / BILAL. — [en souriant] Tu vois ! / DARIA. — Pardon, Bilal…")
    e3 = E("Je relève dans « Le GSM disparu » deux phrases de chaque type.", tall(compact(table(["déclarative", "interrogative", "impérative", "exclamative"], [["", "", "", ""]], ["45mm", "45mm", "46mm", "46mm"])), 22), ["lis", "ecris"], 2, "C",
           sol="Ex. : déclarative : « Il n'est pas là… », « Je n'ai rien pris ! » (avec !) · interrogative : « Quelqu'un a vu mon GSM ? », « Où est-il ? » · impérative : « Lâche-moi ! », « Calme-toi. » · exclamative : « Quel malheur ! », « Quel comédien ! »")
    b.page(f'{e}{e2}{e3}', "Consignes & école")

    # ---------- Leçon 2 : les types de phrases ----------
    l2 = lecon("Les quatre types de phrases", compact(table(["Type", "Pour…", "Ponctuation", "Exemples"], [
        ["<b>déclarative</b>", "dire, raconter, informer", ". (point)", "Harpagon a perdu son argent."],
        ["<b>interrogative</b>", "poser une question", "? (point d'interrogation)", "Où est-il ? · Est-ce que tu l'as vu ? · As-tu vu mon GSM ?"],
        ["<b>impérative</b> (injonctive)", "donner un ordre, un conseil, une interdiction", ". ou !", "Rends-moi mon argent ! · Calme-toi. · Ne crie pas."],
        ["<b>exclamative</b>", "exprimer une émotion forte (joie, colère, peur, surprise)", "! (point d'exclamation)", "Quel malheur ! · Je suis perdu ! · Comme c'est beau !"]], ["30mm", "48mm", "36mm", "68mm"])) +
        '<p class="sm" style="margin:1.5mm 0 1mm"><b>Les trois façons de poser une question</b> : ① l\'intonation (familier) : Tu as vu mon GSM ? ↗ · ② « est-ce que » (courant) : Est-ce que tu as vu mon GSM ? · ③ l\'<b>inversion</b> du sujet (soutenu, à l\'écrit) : As-tu vu mon GSM ? · Où <b>est-il</b> ? · Votre fils <b>a-t-il</b> vu mon GSM ? (avec un -t- entre deux voyelles)</p>'
        '<div class="astuce" style="margin:1mm 0 0">🎭 Au théâtre, le type de phrase guide la <b>voix</b> du comédien : la voix <b>monte</b> à la fin d\'une question fermée ↗, elle <b>descend</b> à la fin d\'une déclarative ↘, elle devient <b>forte</b> et <b>vive</b> dans l\'exclamation.</div>')
    e = E("Je lis les répliques et j'écris le type de phrase : D (déclarative), Int (interrogative), Imp (impérative), E (exclamative).", card("1. ___ Quelqu'un a vu mon GSM ? 2. ___ Calme-toi. 3. ___ Quel malheur ! 4. ___ Il n'est pas là. 5. ___ Lâche-moi ! 6. ___ Que se passe-t-il ici ? 7. ___ Je n'ai rien pris. 8. ___ Quel comédien !"), ["lis", "ecris"], 1, "B",
          sol="1. Int — 2. Imp — 3. E — 4. D — 5. Imp (avec un point d'exclamation) — 6. Int — 7. D — 8. E")
    e2 = E("Je pose la même question de trois façons (intonation, est-ce que, inversion).", f'<p class="sm">Question : (vous / aimer le théâtre)</p><p>1. {blank("xl")}</p><p>2. {blank("xl")}</p><p>3. {blank("xl")}</p>', ["ecris"], 2, "C",
           sol="1. Vous aimez le théâtre ? — 2. Est-ce que vous aimez le théâtre ? — 3. Aimez-vous le théâtre ?")
    b.page(f'{l2}{e}{e2}', "Leçon 2")
    e = E("Je transforme la phrase déclarative dans le type demandé.", '<div class="card sm" style="background:#fff">Phrase de départ : Tu apprends ton texte.</div>' + f'<p>1. interrogative (inversion) : {blank("xl")}</p><p>2. impérative : {blank("xl")}</p><p>3. exclamative : {blank("xl")}</p>', ["ecris"], 2, "C",
          sol="1. Apprends-tu ton texte ? — 2. Apprends ton texte ! (Apprends ton texte.) — 3. Comme tu apprends bien ton texte ! / Tu apprends ton texte !")
    e2 = E("L'inversion avec -t-. Je pose la question en inversant le sujet.", card("1. Il joue le rôle d'Harpagon. → ______________________ ? 2. Elle a le trac. → ______________________ ? 3. Mateo aime la scène. → ______________________ ? 4. On commence à 20 h. → ______________________ ?"), ["ecris"], 2, "C",
           sol="1. Joue-t-il le rôle d'Harpagon ? — 2. A-t-elle le trac ? — 3. Mateo aime-t-il la scène ? — 4. Commence-t-on à 20 h ?")
    e3 = E("J'écoute 8 répliques. Question ↗ ou affirmation ↘ ? Je coche selon l'intonation.", checks(8, ["question ↗", "affirmation ↘"]), ["ecoute", "coche"], 2, "A",
           script="1. Tu as ton texte ↗ 2. Tu as ton texte ↘ 3. Il est là ↘ 4. Il est là ↗ 5. On commence ↗ 6. On commence ↘ 7. C'est fini ↘ 8. C'est fini ↗",
           sol="question : 1, 4, 5, 8 · affirmation : 2, 3, 6, 7")
    e4 = E("Défi ! J'écris 4 répliques d'une dispute entre deux frères pour la télécommande, avec les quatre types de phrases.", lines(4), ["ecris"], 3, "C",
           sol="Ex. : — Donne-moi la télécommande ! (impérative) — Pourquoi est-ce que je te la donnerais ? (interrogative) — Parce que c'est mon tour. (déclarative) — Quel égoïste tu es ! (exclamative)")
    b.page(f'{e}{e2}{e3}{e4}', "S'entraîner")

    # ---------- Leçon 3 : l'exclamation ----------
    l3 = lecon("L'exclamation et l'interjection", compact(table(["Pour s'exclamer, j'utilise…", "Exemples"], [
        ["une <b>interjection</b> (un petit mot qui exprime une émotion)", "<b>Ah !</b> (surprise, soulagement) · <b>Oh !</b> (étonnement) · <b>Hélas !</b> (tristesse) · <b>Aïe !</b> (douleur) · <b>Ouf !</b> (soulagement) · <b>Bravo !</b> · <b>Chut !</b> · <b>Zut !</b> · <b>Hein ?</b> (familier)"],
        ["<b>Quel</b>, <b>quelle</b>, <b>quels</b>, <b>quelles</b> + nom (accordé)", "<b>Quel</b> malheur ! · <b>Quelle</b> surprise ! · <b>Quels</b> beaux costumes !"],
        ["<b>Que</b>, <b>Comme</b> + phrase", "<b>Que</b> c'est drôle ! · <b>Comme</b> il joue bien ! · <b>Qu'</b>il est bavard !"],
        ["<b>Ce que</b>, <b>Qu'est-ce que</b> (courant, oral)", "<b>Ce qu'</b>il est fatigant ! · <b>Qu'est-ce qu'</b>on a ri !"],
        ["une phrase <b>sans verbe</b> (nominale)", "Au voleur ! · Silence ! · Magnifique ! · Quel comédien !"]], ["66mm", "116mm"])) +
        '<div class="astuce" style="margin:2mm 0 0">⚠️ <b>Quel</b> s\'accorde avec le nom : quel<b>le</b> chance, quel<b>s</b> acteurs, quel<b>les</b> actrices. À l\'oral, les quatre formes se prononcent [kɛl]. ✏️ On ne met jamais de point d\'exclamation <b>et</b> un point final : un seul signe, sauf pour l\'effet « ?! » (surprise + question), à réserver aux textes familiers.</div>')
    e = E("J'écris l'interjection qui convient : Aïe · Ouf · Hélas · Chut · Bravo · Zut.", card("1. ______ ! Je me suis cogné la tête. 2. ______ ! Le bébé dort. 3. ______ ! J'ai oublié mon texte à la maison. 4. ______ ! Quelle belle représentation ! 5. ______ ! On a retrouvé le GSM. 6. ______ ! Il est trop tard, le rideau est tombé."), ["complete"], 1, "C",
          sol="1. Aïe — 2. Chut — 3. Zut — 4. Bravo — 5. Ouf — 6. Hélas")
    e2 = E("Quel, quelle, quels ou quelles ? J'accorde.", card("1. ______ belle pièce ! 2. ______ costumes magnifiques ! 3. ______ trac ! 4. ______ comédiennes talentueuses ! 5. ______ idée géniale ! 6. ______ applaudissements !"), ["complete"], 1, "C",
           sol="1. Quelle — 2. Quels — 3. Quel — 4. Quelles — 5. Quelle — 6. Quels")
    b.page(f'{l3}{e}{e2}', "Leçon 3")
    e = E("Je transforme en phrase exclamative avec quel, que ou comme.", f'<p>1. Ce décor est très beau. → {blank("xl")}</p><p>2. Il y a beaucoup de spectateurs ce soir. → {blank("xl")}</p><p>3. Fatou joue très bien. → {blank("xl")}</p><p>4. C\'est une histoire triste. → {blank("xl")}</p>', ["ecris"], 2, "C",
          sol="Ex. : 1. Que ce décor est beau ! / Comme ce décor est beau ! — 2. Que de spectateurs ce soir ! / Quel monde ce soir ! — 3. Comme Fatou joue bien ! — 4. Quelle histoire triste !")
    e2 = E("J'écoute la même phrase dite avec cinq émotions différentes. J'écris l'émotion : joie · colère · peur · tristesse · surprise.", card("« Il est là ! » 1. ______________ 2. ______________ 3. ______________ 4. ______________ 5. ______________"), ["ecoute", "ecris"], 2, "A",
           script="Dire « Il est là ! » successivement : 1. avec joie (voix haute, sourire) ; 2. avec colère (forte, sèche) ; 3. avec peur (chuchotée, tremblante) ; 4. avec tristesse (lente, basse) ; 5. avec surprise (montante, brève).",
           sol="1. joie — 2. colère — 3. peur — 4. tristesse — 5. surprise")
    e3 = E("À mon tour ! En duo, je dis « Tu es encore en retard ! » avec une émotion tirée au sort. Mon voisin devine. Puis j'écris la didascalie qui correspond à chaque émotion.", lines(2), ["parle", "duo", "ecris"], 1, "A",
           sol="Ex. : [en colère, les bras croisés] · [tristement, en baissant la tête] · [en riant] · [inquiète, en regardant sa montre]")
    e4 = E("Défi ! J'écris un court monologue (4 phrases) d'un personnage qui vient de gagner au Lotto, avec deux interjections et deux types d'exclamation différents.", lines(4), ["ecris"], 3, "C",
           sol="Ex. : [Il regarde son billet, bouche bée.] Oh ! Ce n'est pas possible ! Quelle chance incroyable ! Comme je suis heureux ! Ah ! Je vais enfin pouvoir offrir une maison à ma mère !")
    b.page(f'{e}{e2}{e3}{e4}', "S'entraîner")

    # ---------- Leçon 4 : les formes de phrases ----------
    l4 = lecon("Les formes de phrases", '<p class="sm" style="margin-bottom:1.5mm">Chaque phrase a un <b>type</b> (leçon 2) et peut prendre plusieurs <b>formes</b> :</p>' +
        compact(table(["Forme", "Exemples"], [
            ["<b>affirmative</b> / <b>négative</b>", "Il a pris mon GSM. → Il <b>n\'</b>a <b>pas</b> pris mon GSM. · <b>ne… plus</b> (fin) · <b>ne… jamais</b> (à aucun moment) · <b>ne… rien</b> (aucune chose) · <b>ne… personne</b> (aucune personne) · <b>ne… aucun(e)</b> · <b>ne… que</b> (= seulement, sens restrictif) · <b>ni… ni…</b>"],
            ["<b>neutre</b> / <b>emphatique</b> (on met un mot en valeur)", "Mateo a perdu son GSM. → <b>C\'est</b> Mateo <b>qui</b> a perdu son GSM. · <b>C\'est</b> son GSM <b>que</b> Mateo a perdu. · Son GSM, Mateo <b>l\'</b>a perdu. (détachement)"],
            ["<b>active</b> / <b>passive</b> (module 8)", "Molière a écrit L\'Avare. → L\'Avare <b>a été écrit par</b> Molière."]], ["50mm", "132mm"])) +
        '<div class="grid2" style="gap:2mm;margin-top:2mm"><div class="astuce" style="margin:0">✏️ <b>À l\'écrit</b>, la négation a deux parties : je <b>ne</b> sais <b>pas</b>. Aux temps composés : je <b>n\'</b>ai <b>rien</b> vu, mais je <b>n\'</b>ai vu <b>personne</b>. Avec l\'infinitif : <b>ne pas</b> courir.</div>'
        '<div class="attention" style="margin:0">🗣️ <b>À l\'oral familier</b>, on supprime souvent le « ne » : « J\'ai rien pris ! » Au théâtre, cela peut montrer qu\'un personnage parle familièrement. Dans un écrit scolaire, le « ne » est <b>obligatoire</b>.</div></div>')
    e = E("Je mets les phrases à la forme négative avec la négation demandée.", card("1. Je comprends tout. (ne… rien) → ______________________ 2. Quelqu'un a vu mon GSM. (ne… personne → Personne…) → ______________________ 3. Il joue toujours le méchant. (ne… jamais) → ______________________ 4. Elle a encore le trac. (ne… plus) → ______________________"), ["ecris"], 1, "C",
          sol="1. Je ne comprends rien. — 2. Personne n'a vu mon GSM. — 3. Il ne joue jamais le méchant. — 4. Elle n'a plus le trac.")
    e2 = E("Je mets en valeur le mot souligné avec « C'est… qui » ou « C'est… que ».", card("1. <u>Fatou</u> a trouvé la solution. → ______________________ 2. Mateo cherche <u>son GSM</u>. → ______________________ 3. <u>Molière</u> a écrit Le Bourgeois gentilhomme. → ______________________"), ["ecris"], 2, "C",
           sol="1. C'est Fatou qui a trouvé la solution. — 2. C'est son GSM que Mateo cherche. — 3. C'est Molière qui a écrit Le Bourgeois gentilhomme.")
    b.page(f'{l4}{e}{e2}', "Leçon 4")
    e = E("Oral familier ou écrit correct ? Je réécris les répliques avec une négation complète.", card("1. « J'ai rien pris ! » 2. « T'as vu personne ? » 3. « Je l'ai jamais touché ! » 4. « On sait pas. »", 1.9) + lines(2), ["lis", "ecris"], 1, "C",
          sol="1. Je n'ai rien pris ! — 2. Tu n'as vu personne ? (N'as-tu vu personne ?) — 3. Je ne l'ai jamais touché ! — 4. On ne sait pas.")
    e2 = E("« ne… que » = seulement. Je réécris avec ne… que.", card("1. Il a seulement deux répliques. → ______________________ 2. Nous répétons seulement le mardi. → ______________________ 3. Elle porte seulement un chapeau comme costume. → ______________________"), ["ecris"], 2, "C",
           sol="1. Il n'a que deux répliques. — 2. Nous ne répétons que le mardi. — 3. Elle ne porte qu'un chapeau comme costume.")
    e3 = E("Type et forme. Je complète le tableau pour chaque phrase.", tall(compact(table(["Phrase", "Type", "Forme(s)"], [["C'est toi qui as pris mon GSM !", "", ""], ["N'as-tu rien vu ?", "", ""], ["Ne crie pas.", "", ""], ["L'Avare a été écrit par Molière.", "", ""]], ["86mm", "46mm", "50mm"])), 7), ["lis", "ecris"], 3, "C",
           sol="exclamative · affirmative, emphatique — interrogative · négative — impérative · négative — déclarative · affirmative, passive")
    e4 = E("Défi ! Mateo nie tout. J'écris 4 répliques où il répond à Mme Lambert avec quatre négations différentes (ne… pas, ne… rien, ne… jamais, ne… personne).", lines(4), ["ecris"], 3, "C",
           sol="Ex. : — Tu as utilisé ton GSM ? — Non, Madame, je ne l'ai pas utilisé ! — Qu'as-tu fait pendant le cours ? — Je n'ai rien fait de mal ! — Tu l'allumes souvent en classe ? — Jamais ! Je ne l'allume jamais ! — Qui t'a appelé alors ? — Personne ne m'a appelé…")
    b.page(f'{e}{e2}{e3}{e4}', "S'entraîner")

    # ---------- Leçon 5 : Molière et le comique ----------
    P["comique"] = b.n + 1
    l5 = lecon("Molière et les procédés du comique", compact(table(["Le comique de…", "C'est…", "Exemple chez Molière"], [
        ["<b>mots</b>", "jeux de mots, répétitions, mots inventés, langage déformé", "« Que diable allait-il faire dans cette galère ? » (répété sept fois dans Les Fourberies de Scapin, II, 7)"],
        ["<b>gestes</b>", "coups, chutes, grimaces, poursuites", "Harpagon s'attrape lui-même par le bras (L'Avare, IV, 7)"],
        ["<b>situation</b>", "quiproquo (un personnage en prend un autre pour quelqu'un d'autre), déguisement, malentendu", "Toinette, la servante, se déguise en médecin (Le Malade imaginaire)"],
        ["<b>caractère</b>", "un défaut exagéré : l'avarice, la vanité, la peur d'être malade", "Monsieur Jourdain veut à tout prix devenir un « gentilhomme » (Le Bourgeois gentilhomme)"]], ["26mm", "62mm", "94mm"])) +
        '<p class="sm" style="margin:2mm 0 1mm"><b>Le Bourgeois gentilhomme</b> (1670) : Monsieur Jourdain, un riche bourgeois, prend des leçons pour ressembler aux nobles. Son maître de philosophie lui explique qu\'il y a deux façons d\'écrire : les vers et la prose.</p>' +
        scene(BOURGEOIS, "Le Bourgeois gentilhomme, acte II, scène 4 (Molière, 1670) · extrait", 9.3) +
        '<div class="astuce" style="margin:2mm 0 0">📚 Molière a aussi écrit <b>Les Fourberies de Scapin</b> (1671) et <b>Le Malade imaginaire</b> (1673). Il s\'est senti mal sur scène pendant la quatrième représentation du Malade imaginaire, où il jouait… un malade, et il est mort quelques heures plus tard, le 17 février 1673. Le français est parfois appelé « la langue de Molière ».</div>')
    e = E("Je relis l'extrait du Bourgeois gentilhomme. Je réponds.", f'<p class="sm">1. Qu\'est-ce que Monsieur Jourdain vient de découvrir ? {blank("xl")}</p><p class="sm">2. Depuis combien de temps parle-t-il en prose ? Pourquoi est-ce drôle ? {blank("xl")}</p><p class="sm">3. Quel type de comique est-ce surtout ? {blank("l")}</p>', ["lis", "ecris"], 2, "B",
          sol="1. Qu'il parle en prose (le langage de tous les jours) sans le savoir. — 2. Depuis plus de quarante ans ; il est fier d'apprendre une chose banale : tout le monde parle en prose ! — 3. Comique de caractère (sa naïveté, sa vanité) et de mots.")
    b.page(f'{l5}{e}', "Leçon 5")
    e = E("Quel comique ? J'écris : mots, gestes, situation ou caractère.", compact(table(["Situation (scènes imaginaires)", "Comique de…"], [["Un personnage glisse sur une peau de banane.", ""], ["Un avare refuse d'acheter des bougies et reste dans le noir.", ""], ["Un valet répète « Et le dessert ? » à chaque réplique de son maître.", ""], ["Une fille se déguise en garçon et son père ne la reconnaît pas.", ""], ["Mateo cherche son GSM partout alors qu'il est dans sa poche.", ""]], ["140mm", "42mm"])), ["lis", "ecris"], 1, "B",
          sol="gestes · caractère · mots · situation · situation")
    e2 = E("J'écoute la scène de la galère (Les Fourberies de Scapin, résumée par la prof). Je réponds.", f'<p class="sm">1. Que raconte Scapin à Géronte ? {blank("xl")}</p><p class="sm">2. Quelle phrase Géronte répète-t-il ? Pourquoi ? {blank("xl")}</p><p class="sm">3. Pourquoi le public rit-il ? {blank("xl")}</p>', ["ecoute", "ecris"], 2, "A",
           script="Résumé : Scapin, un valet rusé, veut obtenir de l'argent de Géronte, un vieux père avare. Il invente une histoire : des Turcs auraient enlevé Léandre, le fils de Géronte, sur une galère, et demandent une rançon de cinq cents écus. Géronte ne veut pas payer. Il répète sans arrêt : « Que diable allait-il faire dans cette galère ? », puis il cherche toutes les excuses pour garder son argent.",
           sol="1. Que Léandre, son fils, a été enlevé par des Turcs sur une galère et qu'il faut payer une rançon (histoire inventée). — 2. « Que diable allait-il faire dans cette galère ? » : il ne veut pas payer, il repousse le moment de donner son argent. — 3. À cause de la répétition (comique de mots) et de son avarice exagérée (comique de caractère) ; le public sait que Scapin ment (comique de situation).")
    e3 = E("Je compare Harpagon et Géronte : quel défaut ont-ils en commun ? Quelle autre ressemblance vois-tu ?", lines(2), ["lis", "ecris"], 2, "C",
           sol="Ils sont tous les deux avares : ils aiment l'argent plus que tout (même plus que leurs enfants). Tous les deux sont des vieux pères ridicules dont le public se moque.")
    e4 = E("Défi ! J'invente un personnage comique avec un défaut exagéré (le peureux, le menteur, le gourmand…) et j'écris sa première réplique avec une didascalie.", lines(3), ["ecris"], 3, "C",
           sol="Ex. : Le gourmand. GASTON. — [la bouche pleine, en cachant un gâteau derrière son dos] Moi ? Manger avant le repas ? Jamais ! Je n'ai rien mangé depuis… cinq minutes !")
    b.page(f'{e}{e2}{e3}{e4}', "S'entraîner")

    # ---------- Leçon 6 : jouer une scène ----------
    l6 = lecon("Jouer une scène : la voix, le corps, l'espace", compact(table(["", "Je pense à…"], [
        ["🗣️ <b>La voix</b>", "le <b>volume</b> (on doit m'entendre au fond de la salle) · le <b>débit</b> (lent, rapide) · l'<b>articulation</b> · l'<b>intonation</b> (question ↗, affirmation ↘, émotion) · les <b>pauses</b> (un silence peut être très fort)"],
        ["🧍 <b>Le corps</b>", "le <b>regard</b> (vers mon partenaire ou vers le public dans un aparté) · les <b>gestes</b> (larges, visibles) · le <b>visage</b> (les émotions) · la <b>posture</b> (droit, courbé, assis…) · <b>ne jamais tourner le dos au public</b>"],
        ["🗺️ <b>L'espace</b>", "mes <b>entrées</b> et <b>sorties</b> (côté cour, côté jardin) · mes <b>déplacements</b> · ma place par rapport aux autres · l'<b>avant-scène</b> pour les moments importants"],
        ["🤝 <b>Le groupe</b>", "écouter les répliques des autres · réagir même quand je ne parle pas · attendre la fin des rires du public · aider un partenaire qui oublie son texte"]], ["32mm", "150mm"])) +
        '<div class="astuce" style="margin:2mm 0 0">🧠 <b>Pour apprendre mon texte</b> : je le lis à voix haute plusieurs fois · je cache mes répliques et je les dis en écoutant celles des autres (enregistrées sur mon GSM) · j\'apprends aussi les gestes · je répète un peu chaque jour plutôt que tout la veille. 😰 <b>Contre le trac</b> : respirer lentement par le ventre, sourire, se concentrer sur son personnage.</div>')
    e = E("Bon conseil ou mauvais conseil ? Je coche.", compact(table(["", "👍", "👎"], [[x, '<span class="chk"></span>', '<span class="chk"></span>'] for x in ["Je parle assez fort pour que le fond de la salle m'entende.", "Je tourne le dos au public pour parler à mon partenaire.", "Je fais des gestes larges et visibles.", "Quand je ne parle pas, je regarde mes chaussures.", "Si un partenaire oublie son texte, je l'aide discrètement.", "J'apprends tout mon texte la veille du spectacle."]], ["140mm", "21mm", "21mm"])), ["lis", "coche"], 1, "B",
          sol="👍 : 1, 3, 5 · 👎 : 2, 4, 6")
    b.page(f'{l6}{e}', "Leçon 6")
    e = E("Exercice de voix (toute la classe). Je dis la phrase « Le rideau se lève. » en suivant chaque consigne.", '<div class="grid3" style="gap:1.5mm">' + "".join(f'<div class="card c sm" style="border:1.5px dashed {MC};padding:2mm 1mm"><span style="font-size:15pt">{ic}</span><br>{t}</div>' for ic, t in [("🐭", "en chuchotant"), ("🦁", "très fort, sans crier"), ("🐢", "très lentement"), ("🐇", "très vite, en articulant"), ("😱", "avec peur"), ("😂", "en riant")]) + '</div>', ["parle", "groupe"], 1, "A",
          script="Faire l'exercice en chœur puis individuellement ; insister sur l'articulation quand on parle vite.", sol="Activité orale.")
    e2 = E("J'annote la réplique pour la jouer : je souligne le mot le plus important, je marque les pauses (|) et j'écris une didascalie de geste.", '<div class="card big" style="background:#fff;line-height:1.9">MATEO. — Cette fois, c\'est sérieux ! On me l\'a volé ! Quel malheur ! Toutes mes photos, toute ma musique…</div>' + lines(1), ["lis", "souligne", "ecris"], 2, "C",
           sol="Ex. : Cette fois, | c'est <u>sérieux</u> ! | On me l'a <u>volé</u> ! | Quel malheur ! | Toutes mes photos, | toute ma musique… [Il s'effondre sur une chaise, la tête dans les mains.]")
    e3 = E("Les mots de la mise en scène. Je complète : metteuse en scène · accessoire · costume · éclairage · décor.", card("1. Le GSM de Mateo est un ______________ . 2. La ______________ dit aux comédiens où se placer. 3. Les tables et le tableau de la classe forment le ______________ . 4. Le chapeau d'Harpagon fait partie de son ______________ . 5. À la fin, l'______________ s'éteint doucement."), ["complete"], 1, "C",
           sol="1. accessoire — 2. metteuse en scène — 3. décor — 4. costume — 5. éclairage")
    e4 = E("Défi ! Je prépare une fiche de mise en scène pour les lignes 2 à 5 du « GSM disparu » : pour chaque réplique, où est le comédien, quel geste, quel ton ?", tall(compact(table(["Ligne", "Place sur scène", "Geste", "Ton"], [["2 (Mateo)", "", "", ""], ["3 (Fatou)", "", "", ""], ["4 (Mateo)", "", "", ""], ["5 (Yonas)", "", "", ""]], ["24mm", "52mm", "54mm", "52mm"])), 7), ["lis", "ecris"], 3, "C",
           sol="Ex. : 2 : entre côté jardin, court au centre ; bras levés ; affolé · 3 : assise à l'avant-scène cour ; ne lève pas les yeux ; lasse · 4 : au centre ; mains sur la tête ; dramatique · 5 : s'avance vers le public ; clin d'œil ; malicieux, à voix plus basse.")
    b.page(f'{e}{e2}{e3}{e4}', "S'entraîner")

    # ---------- Documents de la vie ----------
    prog = f'''<div class="doc" style="transform:none;border:2px solid {MC};background:#fff;padding:3mm 4mm;font-size:9.1pt;line-height:1.38">
<div class="flex" style="justify-content:space-between;align-items:center"><div><span class="xs" style="color:{MC};font-weight:700">CENTRE CULTUREL DE HAUTRIVE · SAISON 2026-2027</span><br><b style="font-size:14pt;color:#1F2A44">🎭 Ce mois-ci au théâtre</b></div><span class="xs muted">(document fictif)</span></div>
<div class="grid2" style="gap:3mm;margin-top:1.5mm"><div><b>L'Avare</b> · de Molière · Compagnie du Petit Pont<br><span class="xs">Une mise en scène moderne : Harpagon cache ses économies… dans un coffre-fort numérique ! Dès 12 ans · 1 h 40 sans entracte.</span><br>📅 ven. 12 et sam. 13 mars, 20 h<br><br><b>Tchantchès et le dragon</b> · marionnettes liégeoises<br><span class="xs">Le héros populaire de Liège, avec son béret et son grand nez, affronte un dragon. Spectacle familial, en français (quelques mots de wallon). Dès 6 ans · 50 min.</span><br>📅 mer. 17 mars, 15 h</div>
<div><b>Tarifs</b><br>Plein tarif : 14 € · Étudiants et moins de 26 ans : 8 € · Écoles (en journée) : 5 €<br>Tickets <b>Article 27</b> acceptés (pour les personnes à petits revenus : renseignez-vous auprès de votre CPAS ou d'une association partenaire).<br><b>Réservations</b> : à l'accueil (du mardi au samedi, de 10 h à 17 h), au 087 12 34 56 ou sur ccl-hautrive-exemple.be.<br><span class="xs muted">Les places réservées non retirées 15 minutes avant le début du spectacle sont remises en vente. Les retardataires ne seront admis qu'à un moment propice.</span></div></div></div>'''
    e = E("Je lis le programme du centre culturel. Je réponds.", prog + f'<p class="sm mt2">1. Quels spectacles le centre propose-t-il ce mois-ci ? Lequel conviendrait à ton petit frère de 7 ans ? Pourquoi ? {blank("xl")}</p><p class="sm">2. Combien paiera la classe (14 élèves + 2 professeurs) pour L\'Avare en soirée, au tarif étudiant pour les élèves et au plein tarif pour les professeurs ? {blank("xl")}</p><p class="sm">3. Qu\'est-ce que les tickets Article 27 ? {blank("xl")}</p><p class="sm">4. Que se passe-t-il si on arrive en retard ? Que signifie « à un moment propice » ? {blank("xl")}</p>', ["lis", "ecris"], 2, "B",
          sol="1. L'Avare (dès 12 ans) et Tchantchès et le dragon (dès 6 ans, spectacle familial) : le second convient à un enfant de 7 ans. — 2. 14 × 8 = 112 € + 2 × 14 = 28 € → 140 €. — 3. Des tickets à prix réduit pour les personnes qui ont de petits revenus (association Article 27, en Belgique). — 4. On n'entre pas tout de suite : on attend un moment qui ne dérange pas le spectacle (par exemple, entre deux scènes).")
    e2 = E("Je téléphone pour réserver (en duo : le client et l'agent d'accueil). Je prépare mes questions avec des phrases interrogatives variées.", lines(3), ["ecris", "parle", "duo"], 2, "A",
           sol="Ex. : Bonjour, est-ce qu'il reste des places pour L'Avare samedi soir ? Combien coûte une place pour un étudiant ? Pourrais-je réserver trois places ? Jusqu'à quelle heure faut-il retirer les billets ?")
    b.page(f'<span class="tag-doc">📄 DOCUMENT DE LA VIE</span><h2>Le programme du centre culturel</h2>{e}{e2}', "Document de la vie")
    aud = f'''<div class="doc" style="transform:none;border:1.5px solid #9aa1b1;background:#FFFDF6;padding:3mm 4mm;font-size:9.3pt;line-height:1.4">
<div class="flex" style="justify-content:space-between"><b style="font-size:13pt;color:#E4572E">📣 Audition · La troupe de l'Athénée recrute !</b><span class="xs muted">valves de l'Athénée (document fictif)</span></div>
<p style="margin:1.5mm 0">Tu as envie de monter sur scène ? Tu aimes faire rire, émouvoir, inventer ? La troupe de l'Athénée prépare <b>« Le Médecin malgré lui »</b> de Molière pour le mois de mai.</p>
<p style="margin:1mm 0"><b>Qui ?</b> Tous les élèves, de la 1re à la 6e et du DASPA. <b>Aucune expérience demandée</b>, seulement de la motivation et de la régularité.</p>
<p style="margin:1mm 0"><b>L'audition :</b> mercredi 3 février, de 13 h à 15 h, à la salle polyvalente. Prépare : ① une courte présentation (nom, classe, pourquoi tu veux jouer) ; ② une réplique de ton choix (une minute maximum), apprise par cœur ; ③ une improvisation sur un thème donné le jour même.</p>
<p style="margin:1mm 0"><b>Les répétitions</b> ont lieu chaque mercredi de 13 h à 15 h, puis aussi le samedi matin pendant les deux dernières semaines.</p>
<p style="margin:1mm 0 0">Inscription auprès de M. Diallo (local des éducateurs) <b>avant le 29 janvier</b>. N'oublie pas l'autorisation signée par tes parents !</p></div>'''
    e = E("Je lis l'annonce d'audition. Je réponds.", aud + f'<p class="sm mt2">1. Quelle pièce la troupe va-t-elle jouer ? De quel auteur ? {blank("l")}</p><p class="sm">2. Amina n\'a jamais fait de théâtre. Peut-elle se présenter ? Justifie avec une citation. {blank("xl")}</p><p class="sm">3. Quelles sont les trois épreuves de l\'audition ? {blank("xl")}</p><p class="sm">4. Quel engagement demande la troupe ? Est-ce compatible avec un job le samedi matin ? {blank("xl")}</p>', ["lis", "ecris"], 2, "B",
          sol="1. « Le Médecin malgré lui », de Molière. — 2. Oui : « Aucune expérience demandée, seulement de la motivation et de la régularité ». — 3. Une présentation, une réplique apprise par cœur (une minute), une improvisation. — 4. Venir à toutes les répétitions (chaque mercredi de 13 h à 15 h, et le samedi matin les deux dernières semaines) : un job le samedi matin poserait problème à la fin.")
    e2 = E("Je prépare ma présentation pour l'audition (3 phrases) : nom, classe, pourquoi je veux jouer.", lines(3), ["ecris", "parle"], 2, "C",
           sol="Ex. : Bonjour, je m'appelle Amina et je suis en DASPA. Je n'ai jamais fait de théâtre, mais j'aimerais apprendre à parler devant un public. Ce serait aussi une bonne façon de progresser en français !")
    e3 = E("Belgicismes et mots de la culture. Je relie.", relie(["les valves", "un CPAS", "le wallon", "un centre culturel", "Tchantchès"], ["une langue régionale de Wallonie", "le héros populaire des marionnettes liégeoises", "le panneau d'affichage", "un lieu public qui organise des spectacles et des ateliers", "le centre public d'action sociale de la commune"]), ["lis", "relie"], 1, "B",
           sol="valves → panneau d'affichage · CPAS → centre public d'action sociale · wallon → langue régionale · centre culturel → lieu de spectacles et d'ateliers · Tchantchès → héros des marionnettes liégeoises")
    b.page(f'<span class="tag-doc">📄 DOCUMENT DE LA VIE</span><h2>Une audition</h2>{e}{e2}{e3}', "Document de la vie")

    # ---------- Vers les épreuves ----------
    FRIGO = [(None, "Une cuisine, le soir. KARIM, 15 ans, et sa sœur LINA, 17 ans. (Scène originale.)"),
             ("LINA", "[ouvrant le frigo, furieuse] Qui a mangé mon yaourt ? C'était le dernier !"),
             ("KARIM", "[cachant une cuillère derrière son dos] Quel yaourt ? Il y avait un yaourt ?"),
             ("LINA", "Ne fais pas l'innocent ! Il y avait mon nom dessus, en grosses lettres."),
             ("KARIM", "Je ne sais pas lire les étiquettes. [À part.] Surtout quand j'ai faim."),
             ("LINA", "Montre-moi tes mains."),
             ("KARIM", "[il montre une main, puis l'autre, en faisant passer la cuillère d'une main à l'autre] Voilà ! Rien ! Absolument rien !"),
             ("LINA", "[elle saisit la cuillère] Et ça ? C'est un accessoire de magie ?"),
             ("KARIM", "Ah… ça. Ce n'est pas ce que tu crois ! Je… je l'ai trouvée par terre."),
             ("LINA", "Pleine de yaourt à la fraise ? Comme c'est étrange !"),
             ("KARIM", "[il recule vers la porte] Bon. Demain, je t'en achète deux. Promis !"),
             ("LINA", "Trois. Et c'est toi qui fais la vaisselle ce soir."),
             ("KARIM", "[il sort en soupirant] Hélas ! Le crime ne paie pas…")]
    P["epr"] = b.n + 1
    e = E("Entraînement de type CE1D : je lis la scène et je réponds en justifiant.", scene(FRIGO, "Le yaourt disparu", 9.2, True) +
          f'<p class="sm mt2" style="margin-bottom:1mm">a) Où et quand se passe la scène ? Quel élément du texte te le dit ? {blank("xl")}</p><p class="sm" style="margin-bottom:1mm">b) Quel est le problème au début de la scène ? {blank("xl")}</p><p class="sm" style="margin-bottom:1mm">c) Relève l\'aparté. Que révèle-t-il au public ? {blank("xl")}</p><p class="sm" style="margin-bottom:1mm">d) Ligne 7 : quel type de comique la didascalie crée-t-elle ? Explique. {blank("xl")}</p><p class="sm" style="margin-bottom:1mm">e) Ligne 10 : « Comme c\'est étrange ! » Lina est-elle vraiment étonnée ? Quel ton doit prendre la comédienne ? {blank("xl")}</p><p class="sm" style="margin-bottom:1mm">f) Donne le type et la forme de la phrase « Ce n\'est pas ce que tu crois ! » (ligne 9). {blank("l")}</p>', ["lis", "ecris"], 3, "C",
          sol="a) Dans une cuisine, le soir : la didascalie initiale. — b) Le yaourt de Lina a disparu ; Karim l'a mangé. — c) « Surtout quand j'ai faim » : Karim avoue au public qu'il a mangé le yaourt. — d) Comique de gestes : il fait passer la cuillère d'une main à l'autre pour la cacher, et le public le voit. — e) Non : elle est ironique (elle sait que Karim ment) ; ton ironique, moqueur. — f) Exclamative, négative.")
    b.page(EPR.format(k="CE1D", t="Lire un texte théâtral") + e, "Vers les épreuves")
    e = E("Suite de l'épreuve.", f'<p class="sm">g) Pourquoi la dernière réplique est-elle drôle ? Relève l\'interjection. {blank("xl")}</p><p class="sm">h) Écris une réplique de plus pour Lina, avec une didascalie.</p>{lines(2)}', ["lis", "ecris"], 3, "C",
          sol="g) Karim parle comme un grand criminel (« Le crime ne paie pas ») pour un simple yaourt : exagération comique ; interjection « Hélas ! ». — h) Ex. : LINA. — [criant vers la porte, en souriant] Et n'oublie pas : à la fraise !")
    e2 = E("Entraînement DELF B1 · production orale, partie 2 : l'exercice en interaction (jeu de rôle, 3 à 4 minutes, sans préparation).", f'<div class="card" style="background:{TINT}"><b>Sujet :</b> Vous avez réservé deux places de théâtre pour samedi. À l\'accueil, l\'employé vous dit que votre réservation n\'existe pas et que le spectacle est complet. Vous discutez avec lui pour trouver une solution. <i>L\'examinateur joue le rôle de l\'employé.</i></div>' +
           compact(table(["Pour réussir, je…", "Mes phrases"], [["salue et explique le problème", ""], ["exprime mon mécontentement poliment (exclamation, négation)", ""], ["propose ou demande une solution (conditionnel)", ""], ["conclus (accepte, remercie)", ""]], ["74mm", "108mm"])).replace("<td></td>", '<td style="height:11mm"></td>') + '<div class="card sm mt2" style="background:#fff"><b>💬 Phrases utiles</b> · Excusez-moi, mais il doit y avoir une erreur. · Ce n\'est pas possible ! J\'ai réservé il y a une semaine. · Pourriez-vous vérifier encore une fois, s\'il vous plaît ? · Est-ce qu\'il reste des places pour une autre date ? · Serait-il possible d\'être remboursé ? · Je comprends, ce n\'est pas votre faute. · Très bien, je vous remercie de votre aide.</div><div class="astuce">🎓 Au DELF B1, l\'examinateur peut jouer un personnage difficile : il refuse, il hésite. Reste poli, propose des solutions et utilise des questions variées. Ce n\'est pas grave si tu ne « gagnes » pas : on évalue ta capacité à interagir.</div>', ["parle", "ecris"], 3, "A",
           sol="Grille DELF B1 (partie 2) : réaliser la tâche (expliquer, réagir, négocier), registre adapté (vouvoiement, politesse même dans le mécontentement), phrases interrogatives et exclamatives variées, conditionnel de politesse (« Pourriez-vous… ? »), interaction naturelle.")
    b.page(f'{e}{e2}', "Vers les épreuves")

    # ---------- Sons ----------
    e = E("L'intonation : j'écoute et je répète en suivant les flèches.", '<div class="card big" style="line-height:2">Il est là. ↘ (déclarative) · Il est là ? ↗ (question) · Il est là ! ↗↘ (exclamation : la voix monte haut puis tombe)<br>Où est-il ? ↘ (question avec un mot interrogatif : la voix descend) · Est-ce qu\'il est là ? ↗<br>Sors ! ↘ (ordre : voix forte et brève)</div><p class="sm" style="margin:2mm 0 0">✏️ Une question fermée (réponse oui / non) monte ↗. Une question avec <b>où, qui, quand, pourquoi…</b> commence haut et descend souvent ↘.</p>', ["ecoute", "repete"], 1, "A",
          script="Lire chaque phrase deux fois en exagérant la mélodie.", sol="Activité orale.")
    e2 = E("J'écoute : la phrase est-elle déclarative, interrogative ou exclamative ? Je coche.", checks(8, ["déclarative", "interrogative", "exclamative"]), ["ecoute", "coche"], 2, "A",
           script="1. C'est fini ? 2. C'est fini ! 3. C'est fini. 4. Tu viens ? 5. Quelle chance ! 6. Il pleut. 7. Il pleut ? 8. Il pleut !",
           sol="déclarative : 3, 6 · interrogative : 1, 4, 7 · exclamative : 2, 5, 8")
    e3 = E("Articuler comme un comédien. Je lis lentement, puis de plus en plus vite.", '<div class="card big c" style="line-height:1.8">Un chasseur sachant chasser doit savoir chasser sans son chien.<br>Les chaussettes de l\'archiduchesse sont-elles sèches ? Archi-sèches !<br>Ton thé t\'a-t-il ôté ta toux ?</div>', ["lis", "repete"], 2, "A", sol="Activité orale (virelangues traditionnels).")
    e4 = E("Dictée : j'écoute deux fois et j'écris (attention à la ponctuation !).", lines(3), ["ecoute", "ecris"], 2, "A",
           script="« Quel malheur ! Où est mon GSM ? Je ne l'ai pas perdu, on me l'a volé ! Rends-le-moi tout de suite ! »",
           sol="Quel malheur ! Où est mon GSM ? Je ne l'ai pas perdu, on me l'a volé ! Rends-le-moi tout de suite !")
    b.page(f'<h2>J\'écoute bien · l\'intonation des phrases</h2>{e}{e2}{e3}{e4}', "Sons")
    e = E("Le « e » muet au théâtre. J'écoute la prof : dans le langage familier, on « avale » certains e. Je barre les e qui ne se prononcent pas.", '<div class="card big" style="line-height:2">1. Je ne sais pas. → « J\'sais pas. » 2. Tu le veux ? → « Tu l\'veux ? » 3. Petit à petit → « P\'tit à p\'tit » 4. Samedi → « Sam\'di »</div><p class="sm" style="margin:2mm 0 0">🎭 Un comédien peut avaler les e pour jouer un personnage familier. Pour un personnage noble ou dans les <b>vers</b> (poésie, théâtre en vers), on prononce davantage de e (module 10).</p>', ["ecoute", "barre"], 2, "A",
          script="Lire chaque phrase d'abord soignée, puis familière.", sol="1. Je n(e) sais pas — 2. Tu l(e) veux — 3. P(e)tit à p(e)tit — 4. Sam(e)di")
    e2 = E("J'écoute le début de scène et je note le ton de chaque réplique : affolé · moqueur · fâché · gêné · ironique.", card("1. MATEO : ______________ 2. YONAS (aparté) : ______________ 3. YONAS (« Lâche-moi ! ») : ______________ 4. MATEO (« C'est le mien. ») : ______________ 5. FATOU et YONAS (« Quel comédien ! ») : ______________"), ["ecoute", "ecris"], 2, "A",
           script="Jouer les cinq répliques du « GSM disparu » (lignes 2, 5, 9, 15, 18) avec le ton adéquat, sans le nommer.",
           sol="1. affolé — 2. moqueur — 3. fâché — 4. gêné — 5. ironique")
    e3 = E("Les liaisons interdites et obligatoires. Je lis à voix haute : je fais la liaison (‿) ou non (|).", '<div class="card big" style="line-height:2">1. les‿acteurs · les‿actrices 2. un‿aparté 3. Molière | a écrit (pas de liaison après un nom singulier) 4. Ils‿ont joué. 5. le | héros (h aspiré : pas de liaison) · les | héros 6. C\'est‿une comédie.</div>', ["lis", "repete"], 1, "A",
           sol="Liaisons : les‿acteurs, les‿actrices, un‿aparté, ils‿ont, c'est‿une · pas de liaison : Molière | a, le | héros, les | héros (h aspiré)")
    e4 = E("À mon tour ! Je dis une réplique de Molière (Harpagon ou Monsieur Jourdain) devant mon groupe. Le groupe m'évalue.", chk3(["On m'entend bien (volume, articulation).", "Mon intonation suit la ponctuation.", "Mon visage et mes gestes montrent l'émotion."]), ["parle", "groupe"], 2, "A",
           sol="Évaluation par les pairs ; chaque observateur donne un conseil (« Tu pourrais… »).")
    b.page(f'<h2>J\'écoute bien · dire un texte</h2>{e}{e2}{e3}{e4}', "Sons")

    # ---------- Révision spirale ----------
    e = E("🔁 V3 · Module 13 · La cause. Je complète : Harpagon panique ______________ (parce que / pour que) on lui a volé son argent.", "", ["complete"], 1, "C", sol="parce que")
    e2 = E("🔁 V3 · Module 11 · Le subjonctif. Il faut que tu (apprendre) ______________ ton texte et que tu (être) ______________ à l'heure.", "", ["complete"], 1, "C", sol="apprennes · sois")
    e3 = E("🔁 V3 · Module 12 · Le conditionnel. Si j'étais comédien, je (jouer) ______________ des comédies.", "", ["complete"], 1, "C", sol="jouerais")
    e4 = E("🔁 V3 · Module 6 · Le discours indirect. Mateo crie : « On m'a volé mon GSM ! » → Mateo crie qu'______________________________ .", "", ["ecris"], 2, "C", sol="on lui a volé son GSM")
    e5 = E("🔁 V3 · Module 9 · Le récit. Je transforme la réplique en phrase de récit au passé : LINA. — [furieuse] Qui a mangé mon yaourt ?", lines(1), ["ecris"], 2, "C", sol="Ex. : Furieuse, Lina demanda (a demandé) qui avait mangé son yaourt.")
    e6 = E("🔁 V3 · Module 10 · Poésie. Une pièce peut être écrite en vers ou en ______________ . Un vers de douze syllabes s'appelle un ______________ .", "", ["complete"], 2, "C", sol="prose · alexandrin")
    e7 = E("🔁 V3 · Module 4 · L'histoire. Molière a vécu au XVIIe siècle. En quelle période de l'histoire ? (Antiquité, Moyen Âge, Temps modernes, Époque contemporaine)", '<p>' + blank("xl") + '</p>', ["ecris"], 1, "C", sol="Les Temps modernes (1492-1789)")
    e8 = E("🔁 V3 · Module 8 · Le passif. « Le public applaudit les comédiens. » → Les comédiens ______________________________ .", "", ["ecris"], 2, "C", sol="Les comédiens sont applaudis par le public.")
    b.page(f'<h2>🔁 Je révise les modules précédents</h2>{e}{e2}{e3}{e4}{e5}{e6}{e7}{e8}', "Je révise")

    # ---------- Ateliers ----------
    imp = [("🏥", "Chez le médecin : le patient a mal partout, sauf… où il pense."), ("🛒", "Au supermarché : deux clients veulent la dernière boîte de chocolats."), ("🚌", "Dans le bus : quelqu'un a pris ta place réservée."), ("🎂", "Un anniversaire surprise… qui rate."), ("🐶", "Un chien qui parle entre dans la classe."), ("🌧️", "Deux touristes perdus sous la pluie à Liège.")]
    e = E("Improvisation (groupes de 2 ou 3) : nous tirons une carte, nous préparons 2 minutes, puis nous jouons 2 minutes devant la classe.", '<div class="grid3" style="gap:1.5mm">' + "".join(f'<div class="card c sm" style="border:1.5px dashed {MC};padding:2mm 1mm"><span style="font-size:15pt">{ic}</span><br>{t}</div>' for ic, t in imp) + '</div>' +
          compact(table(["Les règles de l'impro", ""], [["J'accepte les idées de mon partenaire (« Oui, et… »).", ""], ["J'utilise les quatre types de phrases.", ""], ["J'exagère un défaut ou une émotion.", ""], ["Nous trouvons une fin.", ""]], ["120mm", "62mm"])), ["parle", "groupe"], 2, "A",
          script="Faire une démonstration avec un volontaire ; chronométrer.",
          sol="Activité orale ; le public note un procédé comique observé.")
    e2 = E("Je suis spectateur : pour une impro, je note un procédé comique et une phrase exclamative que j'ai entendue.", lines(2), ["ecoute", "ecris"], 1, "A",
           sol="Ex. : Comique de situation : le chien répond aux questions de la prof. Phrase exclamative : « Quel chien intelligent ! »")
    b.page(f'{atl_head("A", "Atelier · Impro !")}{e}{e2}', "Atelier")
    e = E("Je lis la page de présentation de la pièce et la liste des personnages (pièce imaginaire). Je réponds.", '<div class="doc" style="transform:none;background:#FFFDF6;border:1.5px solid #9aa1b1;padding:3mm 4mm;font-family:\'DejaVu Serif\';font-size:9.6pt;line-height:1.45"><div class="c"><b style="font-size:13pt">LA CLÉ DU GRENIER</b><br><i>Comédie en trois actes</i></div><p style="margin:2mm 0 1mm"><b>PERSONNAGES</b></p><p style="margin:0">MADAME PINSON, propriétaire d\'une vieille maison, très méfiante.<br>LÉON, son neveu, étudiant, toujours sans argent.<br>ROSE, la voisine, curieuse et bavarde.<br>UN SERRURIER.</p><p style="margin:2mm 0 0"><i>La scène se passe de nos jours, dans le salon de Madame Pinson, à Namur.</i></p><p style="margin:2mm 0 0"><b>ACTE I · Scène 1</b><br><i>MADAME PINSON, seule, cherchant partout.</i><br>MADAME PINSON. — Ma clé ! Où est ma clé ? Elle était là, sur la table… Quelqu\'un est entré !</p></div>' +
          f'<p class="sm mt2">1. Quel est le genre de la pièce ? Combien d\'actes a-t-elle ? {blank("l")}</p><p class="sm">2. Quel trait de caractère de chaque personnage peut créer du comique ? {blank("xl")}</p><p class="sm">3. Imagine ce qui va se passer dans la scène 2 : qui entre ? Pourquoi ? {blank("xl")}</p>', ["lis", "ecris"], 2, "B",
          sol="1. Une comédie en trois actes. — 2. Mme Pinson : méfiante ; Léon : sans argent (suspect idéal) ; Rose : bavarde. — 3. Ex. : Rose entre, curieuse, et accuse Léon.")
    e2 = E("Je compare le début de « La Clé du grenier » et le monologue d'Harpagon : deux ressemblances.", lines(2), ["lis", "ecris"], 3, "B",
           sol="Les deux personnages sont seuls en scène (monologue), ils ont perdu un objet précieux, ils posent beaucoup de questions et pensent qu'on les a volés.")
    e3 = E("Je dessine l'affiche de « La Clé du grenier » : le titre, le genre, un dessin qui donne envie, le lieu et la date de la représentation.", '<div style="height:58mm;border:1.5px dashed #9aa1b1;border-radius:3mm;background:#fff"></div>', ["dessine", "ecris"], 2, "C",
           sol="Affiche lisible : titre, « comédie en trois actes », dessin en lien avec la clé ou les personnages, informations pratiques (lieu, date, heure).")
    b.page(f'{atl_head("B", "Atelier · Lire le début d\'une pièce")}{e}{e2}{e3}', "Atelier")
    e = E("J'écris la scène 2 de « La Clé du grenier » (10 à 12 répliques) : Rose ou Léon entre ; on soupçonne quelqu'un ; un coup de théâtre ; une fin drôle. J'utilise des didascalies, un aparté, les quatre types de phrases et au moins deux négations.", lines(17), ["ecris"], 3, "C",
          sol="Scène présentée correctement (noms, tirets, didascalies en italique ou entre parenthèses), progression (soupçon → coup de théâtre → fin), au moins un procédé comique, types et formes de phrases variés.")
    e2 = E("Je relis ma scène avec la grille.", chk3(["La présentation est correcte (noms, répliques, didascalies).", "Il y a un aparté et un coup de théâtre.", "J'utilise les quatre types de phrases et deux négations.", "Il y a au moins un procédé comique."]), ["lis", "coche"], 1, "C", sol="Grille complétée ; corriger avant de faire lire la scène par un autre groupe.")
    b.page(f'{atl_head("C", "Atelier · J\'écris une scène")}{e}{e2}', "Atelier")
    cases = ["Départ : le rideau se lève !", "Dis « Quel malheur ! » avec trois émotions différentes.", "Tu as oublié ton texte : recule de 2 cases.", "Qu'est-ce qu'une didascalie ?", "Mets à la forme négative : « J'ai tout compris. »", "Le public rit : avance de 2 cases !",
             "Cite une pièce de Molière.", "Pose la question « tu aimes le théâtre » avec l'inversion.", "Tu tournes le dos au public : passe un tour.", "Où est le côté jardin (vu de la salle) ?", "Donne un exemple de comique de geste.", "Salut final : BRAVO, applaudissements !"]
    plateau_jeu = '<div class="grid4" style="gap:1.4mm">' + "".join(f'<div class="card sm" style="padding:2mm;min-height:22mm;background:{"#FFE8D6" if i == 11 else "#fff"}"><b style="color:{MC}">{i + 1}</b> {t}</div>' for i, t in enumerate(cases)) + '</div>'
    e = E("Le jeu « En scène ! » (2 à 4 joueurs, un dé, un pion par joueur).", '<p class="sm" style="margin:0 0 1.5mm">On lance le dé et on avance. Sur une case « question », on répond ou on joue : si les autres sont d\'accord, on reste ; sinon, on recule d\'une case. Le premier qui arrive à la case 12 salue le public !</p>' + plateau_jeu, ["joue", "groupe"], 2, "D",
          sol="Réponses : 4. une indication de jeu (geste, ton, lieu) qu'on ne dit pas · 5. Je n'ai rien compris. · 7. Ex. : L'Avare, Le Bourgeois gentilhomme · 8. Aimes-tu le théâtre ? · 10. à gauche · 11. Ex. : une chute, une poursuite, des coups de bâton.")
    e2 = E("Le jeu du « miroir » et des « statues » (toute la classe). En duo, l'un fait des gestes lents, l'autre les imite comme dans un miroir. Puis la prof dit une émotion et tout le monde devient une statue qui l'exprime.", '<div class="card sm" style="background:#fff">Émotions possibles : la peur · la colère · la fierté · la timidité · la surprise · l\'ennui · la joie. Le public devine l\'émotion de chaque statue.</div>', ["joue", "groupe"], 1, "D",
           sol="Jeu d'échauffement corporel ; nommer les émotions en français.")
    e3 = E("Après les jeux : j'écris trois didascalies qui décrivent les statues que j'ai préférées.", lines(2), ["ecris"], 2, "C",
           sol="Ex. : [Il serre les poings, les sourcils froncés.] · [Elle cache son visage dans ses mains.] · [Il bombe le torse, le menton levé.]")
    b.page(f'{atl_head("D", "Atelier · En scène !")}{e}{e2}{e3}', "Atelier")

    # ---------- ★ Coup de pouce ----------
    e = E("Je relie le mot et le dessin.", relie(["le rideau", "le public", "un costume", "un masque", "un comédien"], ["🎭", "👥", "🤡", "👗", "🟥"]), ["relie"], 1, "B", alpha=True, sol="rideau → 🟥 · public → 👥 · costume → 👗 · masque → 🎭 · comédien → 🤡 (accepter)")
    e2 = E("Je complète avec : scène · texte · public · trac.", '<p class="big" style="line-height:2.1">1. J\'apprends mon ______________ par cœur.<br>2. Le comédien joue sur la ______________ .<br>3. Le ______________ applaudit.<br>4. J\'ai peur avant de jouer : j\'ai le ______________ .</p>', ["complete"], 1, "C", alpha=True, sol="1. texte — 2. scène — 3. public — 4. trac")
    e3 = E("Je lis la réplique. J'entoure le nom du personnage en rouge et la didascalie en bleu.", '<div class="card big" style="line-height:2">YONAS. — (en riant) Ta poche chante, Mateo !</div>', ["lis", "entoure"], 1, "C", alpha=True, sol="Rouge : YONAS · Bleu : (en riant)")
    b.page(CP.format(t="Le théâtre") + e + e2 + e3, "★ Coup de pouce")
    e = E("Je mets le bon signe : . ? !", '<p class="big" style="line-height:2.1">1. Où est mon GSM __<br>2. Quel malheur __<br>3. Il est dans ma poche __<br>4. Tu viens au théâtre __<br>5. Bravo __</p>', ["complete"], 1, "C", alpha=True, sol="1. ? — 2. ! — 3. . — 4. ? — 5. !")
    e2 = E("Je lis le modèle. Je mets à la forme négative.", '<div class="card" style="background:#F2F6FD"><p class="big" style="margin:0">Modèle : J\'ai le trac. → Je <b>n\'</b>ai <b>pas</b> le trac.</p></div><p class="big" style="line-height:2.1;margin:2mm 0 0">1. Je joue. → ______________________<br>2. Il parle fort. → ______________________<br>3. Nous avons le texte. → ______________________</p>', ["lis", "ecris"], 1, "C", alpha=True, sol="1. Je ne joue pas. — 2. Il ne parle pas fort. — 3. Nous n'avons pas le texte.")
    e3 = E("Je dis la phrase « Il est là » avec la voix qui monte ↗ (question), puis qui descend ↘ (je dis une information).", '<div class="card big c">Il est là ? ↗ &nbsp;&nbsp; · &nbsp;&nbsp; Il est là. ↘</div>', ["parle", "repete"], 1, "A", alpha=True, sol="Activité orale.")
    b.page(CP.format(t="Les phrases : . ? ! et ne… pas") + e + e2 + e3, "★ Coup de pouce")
    e = E("J'apprends deux répliques et je les joue avec la prof.", '<div class="card big" style="background:#F2F6FD;line-height:2">MATEO. — (affolé) Mon GSM ! Où est mon GSM ?<br>FATOU. — (calme) Regarde dans ta poche !</div>', ["lis", "parle"], 1, "A", alpha=True, sol="Répliques dites avec le ton indiqué.")
    e2 = E("J'écris l'émotion sous chaque visage : content · fâché · triste · surpris.", '<div class="grid4" style="gap:2mm">' + "".join(f'<div class="card c"><div style="font-size:26pt">{x}</div><div class="line" style="margin-top:3mm"></div></div>' for x in ["😃", "😠", "😢", "😲"]) + '</div>', ["regarde", "ecris"], 1, "C", alpha=True, sol="content · fâché · triste · surpris")
    e3 = E("Je recopie l'interjection et la phrase.", '<div class="card" style="background:#F2F6FD"><p class="big" style="margin:0">Bravo ! Quelle belle pièce !</p></div>' + lines(1), ["recopie"], 1, "C", alpha=True, sol="Copie lisible et exacte, avec les points d'exclamation.")
    b.page(CP.format(t="Je joue une petite scène") + e + e2 + e3, "★ Coup de pouce")

    # ---------- Tâche finale ----------
    e = E("Nous choisissons notre scène et nous distribuons les rôles.", '<p class="sm" style="margin:0 0 1mm">Nous jouons : ☐ « Le GSM disparu » (p. {0}) ☐ « Le yaourt disparu » (épreuve CE1D) ☐ la scène 2 de « La Clé du grenier » écrite à l\'atelier C ☐ un extrait de Molière choisi avec la prof</p>'.format(P["gsm"]) +
          tall(compact(table(["Notre projet", "Ce que nous décidons", "✅"], [["Les rôles (qui joue qui ?)", "", '<span class="chk"></span>'], ["Le metteur en scène et le souffleur", "", '<span class="chk"></span>'], ["Le décor et les accessoires", "", '<span class="chk"></span>'], ["Les costumes (simples !)", "", '<span class="chk"></span>'], ["Le calendrier des répétitions", "", '<span class="chk"></span>']], ["62mm", "104mm", "16mm"])), 18), ["lis", "ecris", "groupe"], 2, "C",
          sol="Fiche complète : rôles distribués, responsabilités, liste des accessoires, calendrier.")
    b.page(tache_head("Notre représentation", "Chaque groupe met en scène et joue une scène (3 à 5 minutes) devant un public (une autre classe, les parents, la fête de l'école). Les élèves sont tour à tour comédiens, metteurs en scène, souffleurs et spectateurs.") + e, "Tâche finale", levels=False)
    e = E("Je prépare mon rôle : je recopie mes répliques, et j'ajoute pour chacune le ton, le geste et ma place sur scène.", tall(compact(table(["Ma réplique (début)", "Ton", "Geste", "Place"], [["", "", "", ""] for _ in range(6)], ["80mm", "32mm", "38mm", "32mm"])), 13), ["ecris"], 3, "C",
          sol="Fiche de rôle complète et cohérente avec les didascalies et le caractère du personnage.")
    e2 = E("Je dessine le plan de notre mise en scène (décor, entrées, déplacements) sur le plateau.", '<div class="c">' + plateau(105) + '</div>', ["dessine"], 2, "C",
           sol="Plan clair : décor placé, entrées côté cour / jardin, flèches de déplacement.")
    b.page(e + e2, "Tâche finale", levels=False)
    e = E("Le jour de la représentation : j'évalue la scène d'un autre groupe.", chk3(["On entend et on comprend tous les comédiens.", "Les émotions et le caractère des personnages sont visibles.", "Les déplacements sont clairs ; personne ne tourne le dos au public.", "Le comique (ou l'émotion) fonctionne : le public réagit."]) + f'<p class="sm mt2">Mon moment préféré : {blank("xl")}</p>', ["ecoute", "coche"], 1, "A",
          sol="Grille remplie ; moment préféré décrit en une phrase.")
    e2 = E("Après la représentation : je m'auto-évalue et j'écris ce que je ferais différemment (au conditionnel).", chk3(["J'ai appris mon texte et je l'ai dit avec expression.", "J'ai participé aux répétitions et aidé mon groupe.", "J'ai géré mon trac."]) + lines(2), ["ecris", "coche"], 1, "C",
           sol="Auto-évaluation ; objectif au conditionnel (ex. : La prochaine fois, je parlerais plus fort et je ferais des gestes plus grands.).")
    b.page(compact(table(["Je vérifie avant la représentation :", "✅"], [[x, '<span class="chk"></span>'] for x in ["Je connais mon texte par cœur (et les répliques qui précèdent les miennes).", "Je sais où entrer, où me placer, où sortir.", "Les accessoires et les costumes sont prêts.", "Nous avons fait une répétition générale complète."]], ["160mm", "22mm"])) + e + e2, "Tâche finale", levels=False)
    e = E("Je révise.", '<p>1. Ce que dit un personnage : une ______________ . 2. L\'indication en italique pour les comédiens : une ______________ . 3. Un personnage seul en scène qui parle : un ______________ . 4. Une phrase qui pose une question est ______________ . 5. « Quel malheur ! » est une phrase ______________ . 6. « C\'est Mateo qui a perdu son GSM » est à la forme ______________ . 7. Vu de la salle, le côté cour est à ______________ .</p>', ["complete"], 1, "C",
          sol="1. réplique — 2. didascalie — 3. monologue — 4. interrogative — 5. exclamative — 6. emphatique — 7. droite")
    e2 = E("Je corrige la scène de Mateo : 5 erreurs (présentation, didascalie, négation, quel, ponctuation).", '<div class="card" style="font-family:\'Comic Sans MS\',cursive;background:#fff;font-size:10.3pt">« Mateo : Ou est mon GSM. FATOU — il est fâché : Je l\'ai pas vu ! MATEO — Quelle malheur ! »</div>' + lines(4), ["lis", "ecris"], 2, "C",
           sol="MATEO. — (nom en majuscules, point, tiret) · « Où est mon GSM ? » (accent et point d'interrogation) · la didascalie doit être en italique ou entre parenthèses et concerner Fatou : FATOU. — (fâchée) · « Je ne l'ai pas vu ! » (négation complète à l'écrit) · « Quel malheur ! » (malheur est masculin)")
    e3 = E("Défi ! Je complète la carte mentale du module : un mot ou un exemple par branche.", tall(compact(table(["Branche", "Mes mots / mes exemples"], [["le texte théâtral", ""], ["le lieu (scène, cour, jardin…)", ""], ["les types de phrases", ""], ["l'exclamation et les interjections", ""], ["les formes de phrases (négation, emphase)", ""], ["Molière et le comique", ""]], ["66mm", "116mm"])), 11), ["lis", "ecris"], 3, "C",
           sol="Productions variées ; vérifier un exemple juste par branche (ex. : comique de mots : « Que diable allait-il faire dans cette galère ? »).")
    b.page(f'<h2>🔁 Je révise tout le module</h2>{e}{e2}{e3}', "Je révise")

    # ---------- Test ----------
    Q = [("Ce que dit un personnage s'appelle…", ["une réplique", "une didascalie", "un acte", "un décor"]), ("Une indication de geste ou de ton pour les comédiens est…", ["une didascalie", "une tirade", "une réplique", "un aparté"]),
         ("Un personnage seul en scène qui parle fait…", ["un monologue", "un dialogue", "un aparté", "un entracte"]), ("Une réplique dite au public, que les autres personnages « n'entendent pas », est…", ["un aparté", "un monologue", "une tirade", "une scène"]),
         ("Vu de la salle, le côté jardin est…", ["à gauche", "à droite", "au fond", "devant"]), ("Molière a écrit…", ["L'Avare", "Les Misérables", "Le Petit Prince", "Candide"]),
         ("« Où est mon GSM ? » est une phrase…", ["interrogative", "déclarative", "impérative", "exclamative"]), ("« Rends-moi mon argent ! » est une phrase…", ["impérative", "interrogative", "déclarative", "passive"]),
         ("La question avec inversion est :", ["Aimes-tu le théâtre ?", "Tu aimes le théâtre ?", "Est-ce que tu aimes le théâtre ?", "Tu aimes le théâtre."]), ("… belle pièce !", ["Quelle", "Quel", "Quels", "Quelles"]),
         ("« Hélas ! » exprime…", ["la tristesse", "la joie", "la douleur physique", "le silence"]), ("« Aïe ! » exprime…", ["la douleur", "le soulagement", "l'admiration", "le doute"]),
         ("Forme négative de « J'ai tout vu » :", ["Je n'ai rien vu.", "Je n'ai pas tout vu personne.", "J'ai rien vu.", "Je n'ai jamais tout."]), ("« Personne n'a vu mon GSM » : la négation est…", ["ne… personne", "ne… pas", "ne… plus", "ne… que"]),
         ("« C'est Fatou qui a trouvé le GSM » est à la forme…", ["emphatique", "passive", "négative", "interrogative"]), ("« Il n'a que deux répliques » signifie…", ["il a seulement deux répliques", "il n'a aucune réplique", "il a beaucoup de répliques", "il a deux répliques de plus"]),
         ("Répéter sans cesse la même phrase, c'est le comique de…", ["mots", "gestes", "situation", "caractère"]), ("Un défaut exagéré (l'avarice d'Harpagon), c'est le comique de…", ["caractère", "gestes", "mots", "situation"]),
         ("Dans une question fermée (oui / non), la voix…", ["monte à la fin", "descend à la fin", "reste plate", "s'arrête"]), ("🔁 Cause : « Il a le trac … il n'a jamais joué. »", ["parce qu'", "pour qu'", "afin qu'", "si bien qu'"])]
    ans = [q[1][0] for q in Q]
    qrot = [2, 1, 3, 0, 1, 3, 2, 0, 1, 2, 3, 1, 0, 2, 3, 1, 2, 0, 3, 1]
    Q = [(q, o[r:] + o[:r]) for (q, o), r in zip(Q, qrot)]
    key = key_from(Q, ans)
    test_pages(b, 14, "Le théâtre", Q, f'<h3>B1. Transforme « Tu connais Molière. » en phrase interrogative (inversion), impérative et exclamative. (… / 3)</h3><p>{blank("xl")}</p><p>{blank("xl")}</p><h3>B2. Mets à la forme négative : « Quelqu\'un m\'a aidé. » (ne… personne) · « Je comprends tout. » (ne… rien) (… / 2)</h3><p>{blank("xl")}</p><h3>B3. Écris une courte scène (6 répliques) entre deux personnages : présentation correcte, deux didascalies, un aparté, une exclamation, une négation. (… / 5)</h3>{lines(6, True)}',
               [["lire une réplique avec la bonne intonation (question, exclamation)", "/ 3", ""], ["jouer une courte scène avec un partenaire (voix, gestes, regard)", "/ 4", ""], ["expliquer ce qu'est une didascalie et un aparté", "/ 3", ""]],
               '<h3>1. Je relie le mot et le dessin. (… / 4)</h3>' + relie(["le public", "un masque", "un costume", "le rideau"], ["🟥", "👗", "👥", "🎭"]) + '<h3>2. Je mets le bon signe : . ? ! (… / 4)</h3><div class="card big">Où est le théâtre __ · Bravo __ · Je joue Harpagon __ · Tu as le trac __</div><h3>3. Je mets à la forme négative : Je joue. → ______ · Il parle. → ______ (… / 4)</h3><h3>4. Je complète : Je dis mon ______ (mes répliques). J\'ai peur avant de jouer : j\'ai le ______ . (… / 3)</h3><h3>5. Oral : je dis « Mon GSM ! Où est mon GSM ? » avec l\'émotion. (… / 5)</h3>')
    closing(b, 14, ["Je reconnais les éléments d'un texte théâtral (répliques, didascalies, acte, scène).", "Je connais les mots du théâtre et du lieu scénique.", "Je connais Molière et quelques-unes de ses pièces.", "Je reconnais et j'utilise les quatre types de phrases.", "Je pose une question de trois façons.", "J'utilise l'exclamation et les interjections.",
                    "J'emploie les formes négative et emphatique.", "Je reconnais les procédés du comique.", "Je dis un texte avec la bonne intonation.", "J'écris une courte scène.", "Je joue une scène devant un public."],
            [("🎭", "une pièce de théâtre"), ("📖", "un acte, une scène"), ("💬", "une réplique"), ("📏", "une tirade"), ("🗣️", "un monologue"), ("🤫", "un aparté"), ("✍️", "une didascalie"), ("🧑‍🎤", "un comédien, une comédienne"), ("👤", "un personnage, un rôle"), ("🎬", "le metteur en scène"), ("👥", "le public, un spectateur"), ("🟥", "le rideau, les coulisses"),
             ("🏠", "le décor, un accessoire"), ("👗", "un costume"), ("😂", "une comédie"), ("😢", "une tragédie"), ("🔁", "répéter, une répétition"), ("😰", "avoir le trac"), ("👏", "applaudir, saluer"), ("❓", "interrogatif, interrogative"), ("❗", "exclamatif, exclamative"), ("👉", "impératif, impérative"), ("🚫", "la forme négative"), ("🔦", "la forme emphatique")])
    plan_de_travail(b, E, 14, ["Lire un texte théâtral", "Les types de phrases", "L'exclamation", "Les formes de phrases", "Molière et le comique", "Jouer une scène"], "☐ Choix de la scène, rôles<br>☐ Fiche de rôle<br>☐ Répétitions<br>☐ Représentation")
    b.pages = [x.replace("padding:.8mm 1.5mm;display:flex", "padding:.3mm 1.5mm;display:flex").replace("repeat(7,1fr);gap:1.3mm", "repeat(7,1fr);gap:.7mm").replace("align-items:center;justify-content:space-between;font-size:8.5pt", "align-items:center;justify-content:space-between;font-size:8pt") for x in b.pages]  # plan compact
    if render:
        to_pdf(b.html(), '/home/claude/syllabus/out/V3_M14_eleve.pdf')

    pg, exs = helpers(b, E)
    CPp = b.marks["★ Coup de pouce"]
    days = [("1", "Collectif", f"Ouverture · BD · le lieu du théâtre ({pg('Découvrir')})", f"CP le théâtre (p. {CPp[0]})"), ("2", "Collectif + duo", f"Lexique : théâtre, émotions, genres ({pg('Lexique')})", "CP le théâtre"),
            ("3", "Collectif", f"📌 Leçon 1 lire un texte théâtral : Harpagon, « Le GSM disparu » ({pg('Consignes & école')})", "Lecture à deux voix avec la prof"), ("4", "Rotation", f"📌 Leçon 2 types de phrases ({pg('Leçon 2')}) · sons ({pg('Sons')})", f"CP . ? ! (p. {CPp[1]})"),
            ("5", "Rotation", f"📌 Leçon 3 exclamation ({pg('Leçon 3')}) · 📌 Leçon 4 formes de phrases ({pg('Leçon 4')})", "CP ne… pas"), ("6", "Collectif", f"📌 Leçon 5 Molière et le comique ({pg('Leçon 5')}) · programme et audition ({pg('Document de la vie')})", "Exemples mimés"),
            ("7", "Rotation", f"📌 Leçon 6 jouer une scène ({pg('Leçon 6')}) · CE1D, DELF ({pg('Vers les épreuves')})", f"CP petite scène (p. {CPp[2]})"), ("8", "Ateliers", f"Ateliers : impro, lecture, écriture, jeux ({pg('Atelier')})", "Rôle de souffleur"),
            ("9", "Groupes + public", f"Tâche finale : répétitions et représentation ({pg('Tâche finale')})", "Petit rôle avec deux répliques"), ("10", "Seul", f"Test ({pg('Test')})", f"CP test ({pg('★ Coup de pouce · Test')})")]
    rot = [["🎧 Écouter-Parler", "Impro (cartes « situation »)", "30 min", "Le public note un procédé"], ["📖 Lire", "« La Clé du grenier » (liste des personnages, scène 1)", "20 min", "Oui"], ["✏️ Écrire", "La scène 2 de « La Clé du grenier »", "30 min", "Grille de relecture"],
           ["🧩 Jouer", "« En scène ! » + miroir et statues", "20 min", "Les joueurs vérifient"], ["👩‍🏫 Table d'appui", "Coup de pouce · ponctuation, négation, petite scène", "20 min", "—"]]
    ev1 = f'''<h3>Partie B (10 points)</h3><p class="sm"><b>B1</b> : <span class="sol">Connais-tu Molière ? · Connais Molière ! (Apprends à connaître Molière.) · Comme tu connais bien Molière ! / Tu connais Molière !</span> (1 pt chacune). · <b>B2</b> : <span class="sol">Personne ne m'a aidé. · Je ne comprends rien.</span> (1 pt chacune). · <b>B3</b> : présentation (1), deux didascalies et un aparté (2), exclamation et négation (1), cohérence (1).</p>
<h3>Partie C · oral (10 points)</h3><p class="sm">L'élève lit une réplique (ex. : Harpagon) avec l'intonation de la question et de l'exclamation (3) · il joue avec un partenaire les lignes 13 à 16 du « GSM disparu » (voix, gestes, regard) (4) · il explique ce qu'est une didascalie et un aparté, avec un exemple (3).</p>
<h3>Test ★ Coup de pouce (20 points)</h3><p class="sm"><b>1 :</b> <span class="sol">public → 👥 · masque → 🎭 · costume → 👗 · rideau → 🟥</span> (4) · <b>2 :</b> <span class="sol">? · ! · . · ?</span> (4) · <b>3 :</b> <span class="sol">Je ne joue pas. · Il ne parle pas.</span> (4) · <b>4 :</b> <span class="sol">texte · trac</span> (3) · <b>5 :</b> réplique dite avec émotion (5).</p>
<h3>Lire les résultats du QCM : quelle remédiation ?</h3>{table(["Questions", "Compétence", "Si moins de la moitié est juste…"], [["1 à 6", "le texte et le lieu théâtral, Molière", f"leçon 1 ({pg('Consignes & école')}) + lexique ({pg('Lexique')}) + coup de pouce p. {CPp[0]}"], ["7 à 9", "les types de phrases, l'inversion", f"leçon 2 ({pg('Leçon 2')}) + coup de pouce p. {CPp[1]}"], ["10 à 12", "l'exclamation, les interjections", f"leçon 3 ({pg('Leçon 3')})"], ["13 à 16", "les formes de phrases", f"leçon 4 ({pg('Leçon 4')})"], ["17 et 18", "le comique", f"leçon 5 ({pg('Leçon 5')})"], ["19", "l'intonation", f"sons ({pg('Sons')})"], ["20", "révision (cause)", "module 13"]], ["24mm", "62mm", "96mm"])}'''
    ev2 = f'''<h2>Grille · tâche finale « Notre représentation »</h2>{table(["Critère", "Très bien", "Bien", "À retravailler", "Points"], [["<b>Texte</b> su par cœur, sans hésitation", "Parfait", "Quelques trous", "Lu", "/ 4"], ["<b>Voix</b> : volume, articulation, intonation adaptée aux types de phrases", "Expressive", "Correcte", "Inaudible", "/ 4"], ["<b>Corps</b> : gestes, visage, regard ; face au public", "Vivant", "Correct", "Figé", "/ 4"], ["<b>Mise en scène</b> : entrées, déplacements, décor, accessoires", "Soignée", "Simple", "Confuse", "/ 4"], ["<b>Travail de groupe</b> : répétitions, entraide", "Exemplaire", "Correct", "Insuffisant", "/ 2"], ["<b>Rôle de spectateur</b> : écoute, grille d'évaluation", "Attentif", "Correct", "Dissipé", "/ 2"]], ["66mm", "30mm", "30mm", "34mm", "22mm"])}
<h2 class="mt4">Différencier et remédier</h2>{table(["Difficulté", "Remédiation"], [["Mémoriser un texte", "Rôles courts (2 à 4 répliques) ; enregistrer les répliques des partenaires sur un GSM ; apprendre avec les gestes ; souffleur prévu pour chaque groupe."], ["Timidité, trac", "Commencer par des exercices collectifs (chœur, statues) ; jouer d'abord en petit groupe ; rôle de souffleur, de régisseur ou de bruiteur possible au début."], ["Types de phrases / intonation", "Cartes « . ? ! » à brandir quand la prof lit une phrase ; même phrase dite avec trois ponctuations."], ["Négation à l'écrit", "Tableau « oral familier → écrit » affiché ; jeu du « ne » oublié : la classe lève la main quand la prof oublie le « ne »."], ["Élève rapide", "Apprendre la tirade d'Harpagon en entier ; écrire une scène complète en un acte ; lire une autre comédie de Molière en version adaptée ; préparer la partie 2 du DELF B1 oral."]], ["50mm", "132mm"])}'''
    rep = f'''<h2>Le théâtre : repères</h2>
<div class="attention"><b>Points d'attention.</b> Jouer devant les autres peut être très difficile pour certains élèves (timidité, pudeur, rapport au corps, rapport à l'image dans certaines cultures, vécu traumatique) : proposer d'autres rôles tout aussi importants (souffleur, metteur en scène, régisseur, bruiteur, créateur d'affiche) et ne jamais forcer. Demander l'autorisation des parents avant de filmer ou de photographier. Éviter les scènes de contact physique ; adapter les gestes (le « bras saisi » peut être mimé à distance).</div>
{table(["Repère", "Ce qu'il faut savoir (vérifié en novembre 2026)"], [["Molière", "Jean-Baptiste Poquelin, dit Molière (1622-1673), auteur, comédien et chef de troupe. Pièces citées : Le Médecin malgré lui (1666), L'Avare (1668, en prose), Le Bourgeois gentilhomme (1670, comédie-ballet), Les Fourberies de Scapin (1671), Le Malade imaginaire (1673). Il est pris d'un malaise pendant la 4e représentation du Malade imaginaire et meurt le soir même, le 17 février 1673. Ses textes sont dans le domaine public ; les extraits du cahier sont cités sans modification (orthographe modernisée des éditions courantes)."], ["Les extraits", "L'Avare, IV, 7 (monologue d'Harpagon, début et fin du premier mouvement) · Le Bourgeois gentilhomme, II, 4 (la prose) · Les Fourberies de Scapin, II, 7 (« Que diable allait-il faire dans cette galère ? », réplique répétée par Géronte) : résumé oral, non cité en entier."], ["Théâtre en Belgique", "Les marionnettes liégeoises et leur héros populaire Tchantchès (béret, foulard, grand nez) ; le Théâtre royal de Toone, marionnettes bruxelloises ; les centres culturels (reconnus par la FWB) dans de nombreuses communes ; l'asbl Article 27 facilite l'accès à la culture pour les personnes à petits revenus (tickets à prix réduit via des partenaires sociaux, dont les CPAS)."], ["Le lieu scénique", "Côté cour (droite) et côté jardin (gauche) vus de la salle ; les termes viennent de la salle des Tuileries, à Paris, au XVIIIe siècle, située entre une cour et un jardin. Avant-scène, lointain, coulisses, plateau."]], ["40mm", "142mm"])}
<div class="attention mt2"><b>Fictif :</b> « Le GSM disparu », « Le yaourt disparu » et « La Clé du grenier » (scènes originales), le centre culturel de Hautrive et sa programmation (la Compagnie du Petit Pont, « Tchantchès et le dragon »), la troupe de l'Athénée et son audition, les tarifs et numéros. Molière, ses pièces et les extraits, Tchantchès, Toone et Article 27 sont réels.</div>
<h3>Belgicismes du module</h3><p class="sm">les <b>valves</b> (panneau d'affichage) · le <b>GSM</b> (portable) · le <b>CPAS</b> (centre public d'action sociale) · un <b>centre culturel</b> (aussi en France, mais réseau propre à la FWB) · le <b>wallon</b> (langue régionale endogène de Wallonie) · <b>septante</b>, <b>nonante</b> · <b>avoir bon</b> (familier : « On a bon ! » = on s'amuse, c'est agréable).</p>'''
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
    T = teacher_book(b, E, "V3 · M14", "", MC, 14, "Le théâtre",
                     "<li><b>Communication :</b> lire un texte théâtral ; dire une réplique avec expression ; improviser ; écrire une courte scène ; jouer une scène devant un public ; réserver un spectacle.</li><li><b>Lexique :</b> le texte (pièce, acte, scène, réplique, tirade, monologue, aparté, didascalie), les gens (comédien, personnage, metteur en scène, public), le lieu (plateau, coulisses, cour, jardin), le spectacle (décor, costume, accessoire, représentation), les genres (comédie, tragédie), les émotions.</li><li><b>Langue :</b> les types de phrases (déclarative, interrogative, impérative, exclamative), les trois façons de poser une question (dont l'inversion), l'exclamation (quel, que, comme) et les interjections ; les formes de phrases (négative : ne… pas, plus, jamais, rien, personne, que ; emphatique : c'est… qui / que ; passive).</li><li><b>Oral :</b> intonation des types de phrases ; articulation ; le e muet ; liaisons et h aspiré.</li><li><b>FLSco :</b> lire un texte théâtral (méthode en 5 questions) ; littérature : Molière et les quatre comiques.</li><li><b>Épreuves :</b> CE1D (lecture d'une scène) ; DELF B1 production orale, partie 2 (interaction).</li><li><b>Documents :</b> programme d'un centre culturel (tarifs, Article 27), annonce d'audition ; extraits de Molière (L'Avare, Le Bourgeois gentilhomme) et scènes originales.</li>",
                     '<p class="sm"><b style="color:#E4572E">Indispensable</b> : réplique et didascalie, ponctuation des types de phrases, ne… pas à l\'écrit, dire une réplique.</p><p class="sm"><b style="color:#d9a400">Important</b> : inversion, exclamation avec quel / que / comme, autres négations, procédés du comique.</p><p class="sm"><b style="color:#2BA88F">Enrichissement</b> : forme emphatique, tirade d\'Harpagon, écriture d\'une scène complète, CE1D, DELF B1.</p>',
                     "Un exemplaire du cahier par élève · un espace dégagé (salle polyvalente, classe aux bancs poussés) · quelques accessoires (chapeau, téléphone factice, cuillère, cassette) · cartes « situation » pour l'impro · dés et pions pour « En scène ! » · si possible, une captation vidéo de L'Avare ou du Bourgeois gentilhomme (extraits) et une sortie au théâtre ou au centre culturel.", "<b>Avant de commencer :</b> fixer la date et le public de la représentation (fête de fin d'année, autre classe, parents) et réserver la salle. Prévoir une progression douce : jeux collectifs avant de jouer seul. Se renseigner sur le centre culturel local (spectacles scolaires, Article 27) : une sortie au théâtre donne beaucoup de sens au module.",
                     days, "« La phrase du jour » : une phrase dite avec trois ponctuations, la classe devine · « L'émotion mystère » : un élève dit « Bonjour » avec une émotion, les autres la nomment · « Le ne oublié » : la prof parle familièrement, la classe corrige à l'écrit.", rot, key, (ev1, ev2), extra_pages=[(rep, "Repères")], start=tstart)
    _LM.paginate = _pg
    _LM.table = _tb
    if render:
        to_pdf(T.html(), '/home/claude/syllabus/out/V3_M14_prof.pdf')
    return b, T


if __name__ == "__main__":
    b, T = build_v3m14()
    print(b.n, T.n)
