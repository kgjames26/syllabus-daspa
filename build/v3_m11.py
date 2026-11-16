"""Volume 3 · Module 11 « Citoyens » (B1 + français de scolarisation).

Connaître ses droits et ses devoirs, comprendre la démocratie, participer à la vie de l'école.
Langue : le subjonctif présent (formation, verbes irréguliers) pour exprimer l'obligation, l'interdiction,
le souhait et la volonté (subjonctif ou infinitif ? ⚠️ espérer + indicatif). FLSco : lire un texte de loi simplifié.
Fil rouge : l'élection des délégués de la classe DASPA de l'Athénée de Hautrive (Yonas et Daria sont candidats)
et le conseil communal des jeunes de Hautrive.
Visuels : balance_dd() (droits et devoirs), bulletin() (bulletin de vote fictif), institutions() (les niveaux de
pouvoir en Belgique), etapes() (les étapes d'une élection), articles() (texte de loi simplifié, articles numérotés).
Faits réels vérifiés en novembre 2026 : Convention internationale des droits de l'enfant (ONU, 20 novembre 1989,
54 articles, ratifiée par la Belgique en 1991), obligation scolaire de 5 à 18 ans (depuis 2020), vote obligatoire,
histoire du droit de vote en Belgique (1831, 1893, 1919, 1948, 1981, 2024), conseil de participation.
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
MC = "#5C4A9E"
TINT = "#ECE9F7"


def chk3(items, w=128):
    return table(["", "😀", "🙂", "😕"], [[x, '<span class="chk"></span>', '<span class="chk"></span>', '<span class="chk"></span>'] for x in items], [f"{w}mm", "18mm", "18mm", "18mm"])


def tall(html, h):
    return html.replace("<td></td>", f'<td style="height:{h}mm"></td>')


def compact(html):
    return html.replace('class="t"', 'class="t compact"')


def card(t, lh=2):
    return f'<div class="card" style="line-height:{lh}">{t}</div>'


def balance_dd(quiz=False):
    """Droits et devoirs face à face (quiz=True : colonnes vides à compléter)."""
    D = [("📚", "J'ai le droit d'aller à l'école.", "Je dois suivre les cours et faire mon travail."),
         ("🗣️", "J'ai le droit de donner mon avis.", "Je dois respecter l'avis des autres."),
         ("🛡️", "J'ai le droit d'être protégé(e) contre la violence.", "Je ne dois blesser personne, ni par des gestes ni par des mots."),
         ("🎮", "J'ai le droit de jouer et de me reposer.", "Je dois respecter le matériel et les horaires.")]
    rows = ""
    for ic, d, v in D:
        a, b = ('', '') if quiz else (d, v)
        rows += (f'<div style="display:grid;grid-template-columns:1fr 9mm 1fr;gap:1.5mm;align-items:center;margin-bottom:1.4mm">'
                 f'<div class="card sm" style="padding:1.6mm 2.5mm;background:#fff;border-left:4px solid {MC};min-height:8mm">{a}</div>'
                 f'<div class="c" style="font-size:15pt">{ic}</div>'
                 f'<div class="card sm" style="padding:1.6mm 2.5mm;background:#fff;border-right:4px solid #E4572E;min-height:8mm">{b}</div></div>')
    head = (f'<div style="display:grid;grid-template-columns:1fr 9mm 1fr;gap:1.5mm;margin-bottom:1.5mm"><div class="c" style="font-weight:800;color:{MC}">✅ MES DROITS</div><div class="c">⚖️</div>'
            f'<div class="c" style="font-weight:800;color:#E4572E">📌 MES DEVOIRS</div></div>')
    return f'<div style="background:{TINT};border-radius:3mm;padding:2.5mm">{head}{rows}</div>'


CANDS = [("Daria KOVALENKO", "« Une classe où chacun ose parler »"), ("Yonas TESFAYE", "« Plus de sport et de sorties ! »"), ("Fatou CAMARA", "« Une école plus verte »")]


def bulletin(marque=None, fs=9.4):
    """Bulletin de vote fictif pour l'élection des délégués (marque = index du candidat coché, ou None)."""
    rows = ""
    for i, (n, s) in enumerate(CANDS):
        box = '<span style="display:inline-block;width:5mm;height:5mm;border:1.4px solid #1F2A44;border-radius:50%;background:' + ("#1F2A44" if marque == i else "#fff") + '"></span>'
        rows += f'<tr><td style="width:10mm;text-align:center">{box}</td><td><b>{n}</b><br><span class="xs muted">{s}</span></td></tr>'
    return (f'<div class="doc" style="transform:none;background:#fff;border:1.5px solid #1F2A44;padding:2.5mm 3.5mm;font-size:{fs}pt;max-width:92mm">'
            f'<div class="c xs" style="letter-spacing:1px;font-weight:700;color:{MC}">ATHÉNÉE DE HAUTRIVE · BULLETIN DE VOTE</div>'
            f'<div class="c" style="font-weight:800;margin:1mm 0">Élection des délégués de la classe DASPA</div>'
            f'<div class="xs c muted" style="margin-bottom:1.5mm">Noircissez <b>un seul</b> rond. Un bulletin avec deux ronds noircis ou un signe est <b>nul</b>.</div>'
            f'<table style="width:100%;border-collapse:collapse" class="sm">{rows}</table>'
            f'<div class="xs muted c" style="margin-top:1.5mm">Vote secret · jeudi 19 novembre · local 12 (document fictif)</div></div>')


def institutions():
    """Les niveaux de pouvoir en Belgique (schéma simplifié)."""
    L = [("🇧🇪", "L'État fédéral", "Parlement fédéral (Chambre : 150 députés) · Gouvernement fédéral · le Roi", "justice, armée, police fédérale, sécurité sociale, affaires étrangères"),
         ("🗣️", "3 Communautés", "française (Fédération Wallonie-Bruxelles) · flamande · germanophone", "l'enseignement, la culture, la jeunesse, le sport"),
         ("🗺️", "3 Régions", "wallonne · flamande · Bruxelles-Capitale", "l'emploi, le logement, l'environnement, les transports (TEC)"),
         ("🏞️", "10 provinces", "conseil provincial · gouverneur", "des écoles, des routes, des services culturels"),
         ("🏘️", "Les communes", "conseil communal · bourgmestre et échevins", "l'état civil (cartes d'identité), la propreté, les plaines de vacances")]
    out = ""
    for i, (ic, t, who, what) in enumerate(L):
        out += (f'<div style="display:grid;grid-template-columns:{8 + i * 4}mm 1fr;gap:0;margin-bottom:.6mm"><div></div>'
                f'<div class="card" style="padding:.9mm 2.5mm;background:#fff;border-left:5px solid {MC}"><b style="color:{MC}">{ic} {t}</b> · <span class="sm">{who}</span><br><span class="xs muted">s\'occupe par exemple de : {what}</span></div></div>')
    return out


def etapes(w=182):
    """Les étapes d'une élection."""
    st = [("📣", "On annonce l'élection"), ("✋", "Les candidats se présentent"), ("📝", "La campagne : programmes, affiches, discours"), ("🗳️", "Le vote secret"), ("🔢", "Le dépouillement : on compte les voix"), ("🎉", "Les résultats : les élus")]
    out = ""
    for i, (ic, t) in enumerate(st):
        out += f'<div class="card c xs" style="flex:1;padding:1.5mm 1mm;background:#fff;border-top:4px solid {MC}"><div style="font-size:15pt">{ic}</div><b>{i + 1}.</b> {t}</div>'
        if i < len(st) - 1:
            out += '<div style="align-self:center;color:#9aa1b1;font-weight:800">→</div>'
    return f'<div style="display:flex;gap:1mm;width:{w}mm;max-width:100%">{out}</div>'


CIDE = [("2", "Non-discrimination", "Tous les enfants ont les mêmes droits, quels que soient leur origine, leur langue, leur religion, leur sexe, leur handicap ou la situation de leurs parents."),
        ("3", "L'intérêt de l'enfant", "Dans toutes les décisions qui concernent un enfant, l'intérêt supérieur de l'enfant doit passer en premier."),
        ("7", "Nom et nationalité", "Dès sa naissance, l'enfant a le droit d'avoir un nom et une nationalité."),
        ("12", "Le droit d'être entendu", "L'enfant a le droit de donner son opinion sur les questions qui le concernent. Les adultes doivent en tenir compte, selon son âge et sa maturité."),
        ("19", "Protection contre la violence", "Les États doivent protéger l'enfant contre toute forme de violence, de mauvais traitement ou de négligence."),
        ("22", "Les enfants réfugiés", "L'enfant réfugié ou qui demande à être reconnu comme réfugié a droit à une protection et à une aide particulières."),
        ("28", "Le droit à l'éducation", "L'enfant a le droit d'aller à l'école. L'enseignement primaire doit être obligatoire et gratuit. La discipline scolaire doit respecter la dignité de l'enfant."),
        ("31", "Repos et loisirs", "L'enfant a le droit au repos, aux loisirs, au jeu et de participer à la vie culturelle et artistique.")]


def articles(sel=None, fs=9.2, titres=True):
    """Extraits simplifiés de la Convention internationale des droits de l'enfant, présentés comme un texte de loi."""
    sel = sel if sel is not None else range(len(CIDE))
    out = ""
    for i in sel:
        n, t, x = CIDE[i]
        tt = f' · <i>{t}</i>' if titres else ''
        out += f'<p style="margin:0 0 1.3mm"><b style="color:{MC}">Article {n}</b>{tt}<br>{x}</p>'
    return (f'<div class="doc" style="transform:none;background:#FFFDF6;border:1.5px solid #9aa1b1;padding:2.5mm 4mm;font-size:{fs}pt;line-height:1.36;font-family:\'DejaVu Serif\'">'
            f'<div class="c" style="font-weight:800;color:#1F2A44;margin-bottom:1.5mm">Convention internationale des droits de l\'enfant (ONU, 1989)<br><span class="xs muted" style="font-weight:400">extraits simplifiés pour la classe</span></div>{out}</div>')


def build_v3m11(start=1, tstart=1, render=True):
    b = Book("V3 · M11", "Volume 3 · Je réussis à l'école · Module 11 · Citoyens", MC, start=start)
    E = Ex(b)
    P = {}
    vis = ('<div class="flex" style="justify-content:space-around;align-items:flex-end">' + avatar("daria", 80, "sourire") + '<div style="font-size:32pt">🗳️ ⚖️</div>' + avatar("yonas", 80, "rire")
           + '<div style="font-size:32pt">🤝 📜</div>' + avatar("prof", 80, "sourire") + avatar("fatou", 80, "pense") + '</div>')
    opening(b, MC, 11, "Citoyens", vis, [("⚖️", "parler de mes droits et de mes devoirs"), ("📜", "lire un règlement, une charte et un texte de loi simplifié"), ("🏛️", "comprendre comment fonctionne la démocratie en Belgique"),
            ("📐", "utiliser le subjonctif pour exprimer l'obligation et le souhait"), ("🗳️", "voter et organiser une élection"), ("📣", "écrire un programme et le présenter")],
            ["As-tu déjà voté (à l'école, dans un club, dans ton pays) ?", "Quels sont tes droits à l'école ? Et tes devoirs ?", "Qu'est-ce qu'un bon délégué de classe ?"],
            ["un droit", "un devoir", "un citoyen", "la démocratie", "voter", "une élection", "un candidat", "un délégué", "un règlement", "une loi", "le subjonctif"], TINT)

    # ---------- Découvrir ----------
    P["bd"] = b.n + 1
    bd = '<div class="grid2" style="gap:3mm">' + "".join([
        bd_case(1, lr("prof", ["Jeudi prochain, nous élirons les deux délégués de la classe. Qui veut être candidat ?"], "yonas", ["Moi ! Je veux que nous fassions plus de sport !"], "sourire", "rire")),
        bd_case(2, lr("daria", ["Moi aussi, je me présente. Je voudrais que chacun ose parler en classe, même ceux qui sont timides."], "bilal", ["Un délégué, ça sert à quoi, au juste ?"], "sourire", "pense")),
        bd_case(3, lr("educ", ["Le délégué représente la classe. Il transmet les idées des élèves aux professeurs et à la direction, et il participe au conseil des élèves."], "fatou", ["Alors, il faut qu'on choisisse bien !"], "sourire", "pense")),
        bd_case(4, lr("mateo", ["Dans mon pays, je n'ai jamais voté. Comment ça se passe ?"], "prof", ["Le vote est secret : chacun choisit seul, dans l'isoloir. Ensuite, on compte les voix : c'est le dépouillement."], "surpris", "sourire")),
        bd_case(5, lr("amina", ["Et les élèves, ils ont des droits ? Ou seulement des devoirs ?"], "educ", ["Les deux ! Le règlement de l'école les explique. Et la Convention des droits de l'enfant protège tous les enfants du monde."], "pense", "sourire")),
        bd_case(6, lr("yonas", ["Daria, que le meilleur gagne !"], "daria", ["D'accord ! Mais j'aimerais que la campagne reste amicale."], "rire", "rire")),
    ]) + '</div>'
    e = E("J'écoute et je lis la BD : une élection dans la classe.", bd, ["ecoute", "lis"], 1, "A",
          script="Lire deux fois en changeant de voix. ", sol="Activité orale.")
    b.page(f'<h2>Découvrir · Qui sera délégué ?</h2>{e}', "Découvrir")
    e = E("Je réponds par une phrase complète.", f'<p>1. Qu\'est-ce que la classe va faire jeudi prochain ? {blank("xl")}</p><p>2. Qui sont les candidats ? Que veut chacun d\'eux ? {blank("xl")}</p><p>3. Selon M. Diallo, quel est le rôle d\'un délégué ? {blank("xl")}</p><p>4. Comment se passe le vote ? Qu\'est-ce que le dépouillement ? {blank("xl")}</p><p>5. Quels textes expliquent les droits des élèves et des enfants ? {blank("xl")}</p>', ["lis", "ecris"], 1, "B",
          sol="1. Elle va élire ses deux délégués. — 2. Yonas (plus de sport) et Daria (que chacun ose parler en classe). — 3. Il représente la classe, transmet les idées des élèves aux professeurs et à la direction et participe au conseil des élèves. — 4. Le vote est secret, chacun choisit seul dans l'isoloir ; le dépouillement, c'est le moment où l'on compte les voix. — 5. Le règlement de l'école et la Convention des droits de l'enfant.")
    e2 = E("Vrai ou faux ? Je coche et je corrige les phrases fausses.", vf(["La classe va élire un seul délégué.", "Mateo a déjà voté dans son pays.", "Pendant le vote, on peut regarder le bulletin du voisin.", "Daria souhaite une campagne amicale."]), ["lis", "coche"], 1, "B",
           sol="Faux (deux délégués) · Faux (il n'a jamais voté) · Faux (le vote est secret) · Vrai")
    e3 = E("Dans la BD, je relève trois phrases avec « que » suivi d'un verbe. J'écris le verbe et son infinitif.", tall(compact(table(["Phrase", "Verbe", "Infinitif"], [["", "", ""], ["", "", ""], ["", "", ""]], ["104mm", "38mm", "40mm"])), 7), ["lis", "ecris"], 2, "C",
           sol="« je veux que nous fassions » → fassions, faire · « je voudrais que chacun ose » → ose, oser · « il faut qu'on choisisse » → choisisse, choisir · « que le meilleur gagne » → gagne, gagner · « j'aimerais que la campagne reste » → reste, rester (trois au choix)")
    e4 = E("Et toi ? As-tu déjà voté ou choisi un représentant (école, club, famille, pays) ? Raconte en 3 phrases.", lines(3), ["ecris", "duo"], 2, "C",
           sol="Ex. : Dans mon ancienne école, nous avons élu un chef de classe à main levée. Dans mon club de foot, l'entraîneur choisit le capitaine. Je n'ai jamais voté avec un bulletin secret.")
    b.page(f'{e}{e2}{e3}{e4}', "Découvrir")
    e = E("J'observe : mes droits et mes devoirs à l'école. Je lis chaque ligne à voix haute avec mon voisin.", balance_dd(), ["lis", "parle", "duo"], 1, "A",
          sol="Lecture à deux voix : l'un lit le droit, l'autre le devoir qui lui correspond.")
    e2 = E("Droit ou devoir ? Je coche.", compact(table(["", "droit", "devoir"], [[x, '<span class="chk"></span>', '<span class="chk"></span>'] for x in ["Être soigné quand on est malade.", "Arriver à l'heure aux cours.", "Avoir un nom et une nationalité.", "Respecter les règles de la classe.", "Donner son avis sur ce qui nous concerne.", "Prendre soin des livres prêtés."]], ["140mm", "21mm", "21mm"])), ["lis", "coche"], 1, "B",
           sol="droit · devoir · droit · devoir · droit · devoir")
    e3 = E("J'écoute trois élèves (personnages fictifs). De quel droit parlent-ils ? Je complète.", tall(compact(table(["", "Le droit", "Ce qui s'est passé"], [["Inès", "", ""], ["Karim", "", ""], ["Sofia", "", ""]], ["24mm", "60mm", "98mm"])), 10), ["ecoute", "ecris"], 2, "A",
           script="Inès : « Chez moi, les filles quittaient l'école à 12 ans ; ici, je continue. » Karim : « On m'insultait ; l'éducateur m'a protégé. » Sofia : « Au conseil des élèves, j'ai donné mon avis. »",
           sol="Inès : le droit à l'éducation ; elle peut continuer l'école en Belgique · Karim : le droit d'être protégé contre la violence ; il en a parlé à l'éducateur · Sofia : le droit de donner son avis ; elle a parlé au conseil des élèves")
    e4 = E("Défi ! J'ajoute deux lignes à la balance : un droit et le devoir qui va avec.", lines(2), ["ecris"], 3, "C",
           sol="Ex. : J'ai le droit d'utiliser l'ordinateur de l'école. → Je dois l'utiliser seulement pour le travail et ne pas l'abîmer.")
    b.page(f'<h2>Découvrir · Des droits et des devoirs</h2>{e}{e2}{e3}{e4}', "Découvrir")

    # ---------- Lexique ----------
    e = E("Les mots de la citoyenneté. Je lis l'encadré.", '<div class="grid2">' + "".join(f'<div class="card" style="background:#fff"><b>{t}</b><p class="sm" style="margin:1mm 0 0">{d}</p></div>' for t, d in [
        ("⚖️ Droits et règles", "un <b>droit</b> (ce qu'on peut faire ou recevoir) · un <b>devoir</b>, une <b>obligation</b> (ce qu'on doit faire) · une <b>interdiction</b> · une <b>règle</b> · un <b>règlement</b> · une <b>loi</b> · une <b>charte</b> (des engagements) · une <b>sanction</b>"),
        ("🗳️ Voter", "une <b>élection</b> · <b>élire</b> · un <b>électeur</b> · un <b>candidat</b> · se <b>présenter</b> · une <b>campagne</b> · un <b>programme</b> · un <b>bulletin</b> de vote · l'<b>isoloir</b> · une <b>voix</b> · le <b>dépouillement</b> · un <b>élu</b> · la <b>majorité</b>"),
        ("🏛️ La démocratie", "le <b>citoyen</b>, la <b>citoyenne</b> · le <b>peuple</b> · le <b>pouvoir</b> · le <b>Parlement</b> (les <b>députés</b> votent les lois) · le <b>gouvernement</b> (les <b>ministres</b>) · la <b>Constitution</b> · la <b>commune</b>, le <b>bourgmestre</b> 🇧🇪"),
        ("🤝 Participer", "<b>représenter</b> · un <b>délégué</b> · un <b>conseil</b> (des élèves, communal) · <b>débattre</b> · <b>proposer</b> · <b>s'engager</b> · le <b>respect</b> · la <b>solidarité</b> · l'<b>égalité</b> · la <b>liberté</b>")]) + '</div>', ["lis"], 1, "B", sol="Lecture de l'encadré.")
    e2 = E("Je complète avec : élire · candidat · isoloir · dépouillement · voix · programme.", card("1. Le jour du vote, chaque électeur va seul dans l'______________ . 2. Après le vote, on compte les bulletins : c'est le ______________ . 3. Yonas a obtenu dix ______________ . 4. Daria est ______________ : elle se présente à l'élection. 5. Dans son ______________ , elle explique ses idées. 6. Nous allons ______________ deux délégués."), ["complete"], 1, "C",
           sol="1. isoloir — 2. dépouillement — 3. voix — 4. candidate — 5. programme — 6. élire")
    e3 = E("Les familles de mots. Je complète.", tall(compact(table(["Verbe", "Nom de l'action", "Nom de la personne"], [["élire", "l'élection", ""], ["voter", "", "le votant, l'électeur"], ["représenter", "", ""], ["gouverner", "", ""], ["participer", "", ""]], ["60mm", "61mm", "61mm"])), 6.5), ["complete"], 2, "C",
           sol="l'élu(e), l'électeur · le vote · la représentation, le représentant · le gouvernement, le gouverneur (et le gouvernant) · la participation, le participant")
    e4 = E("Le bon mot. J'entoure.", card("1. En Belgique, voter est un (<b>droit</b> / <b>devoir</b>) et une obligation. 2. Les députés votent les (<b>lois</b> / <b>chartes</b>). 3. Le chef de la commune s'appelle le (<b>maire</b> 🇫🇷 / <b>bourgmestre</b> 🇧🇪). 4. Celui qui a été choisi par vote est un (<b>élu</b> / <b>électeur</b>)."), ["lis", "entoure"], 1, "C",
           sol="1. devoir (c'est à la fois un droit et un devoir : vote obligatoire) — 2. lois — 3. bourgmestre (en Belgique ; « maire » en France) — 4. élu")
    b.page(f'<h2>Les mots de la citoyenneté</h2>{e}{e2}{e3}{e4}', "Lexique")
    e = E("Je relie le mot et sa définition.", relie(["la démocratie", "la Constitution", "un citoyen", "la majorité", "une sanction", "une charte"], ["plus de la moitié des voix", "une punition quand on ne respecte pas une règle", "un texte où un groupe écrit ses engagements", "le régime où le peuple choisit ceux qui le gouvernent", "une personne qui a des droits et des devoirs dans un pays", "la loi la plus importante d'un pays"]), ["lis", "relie"], 1, "B",
          sol="démocratie → le peuple choisit · Constitution → loi la plus importante · citoyen → droits et devoirs dans un pays · majorité → plus de la moitié des voix · sanction → punition · charte → engagements")
    e2 = E("Les valeurs. Je complète avec : liberté · égalité · solidarité · respect.", card("1. Filles et garçons ont les mêmes droits : c'est l'______________ . 2. J'aide un camarade qui ne comprend pas : c'est la ______________ . 3. Je peux dire ce que je pense : c'est la ______________ d'expression. 4. J'écoute les autres sans me moquer : c'est le ______________ ."), ["complete"], 1, "C",
           sol="1. égalité — 2. solidarité — 3. liberté — 4. respect")
    e3 = E("Les contraires. Je trouve le contraire avec un préfixe (in-, il-, im-, dés-, ir-).", tall(compact(table(["Mot", "Contraire", "Mot", "Contraire"], [["légal", "", "juste", ""], ["égal", "", "obéir", ""], ["responsable", "", "possible", ""]], ["44mm", "47mm", "44mm", "47mm"])), 6.5), ["ecris"], 2, "C",
           sol="illégal · injuste · inégal · désobéir · irresponsable · impossible")
    e4 = E("Défi ! J'explique à un camarade qui vient d'arriver ce qu'est une élection, en 3 phrases, avec au moins 4 mots de l'encadré.", lines(3), ["ecris"], 3, "C",
           sol="Ex. : Une élection, c'est un moment où les électeurs choisissent leurs représentants. Les candidats présentent leur programme pendant la campagne. Le jour du vote, chacun met son bulletin dans l'urne en secret, puis on compte les voix.")
    b.page(f'<h2>La démocratie et les valeurs</h2>{e}{e2}{e3}{e4}', "Lexique")

    # ---------- Leçon 1 : le subjonctif présent (formation) ----------
    l1 = lecon("Le subjonctif présent : la formation", '<p class="sm" style="margin-bottom:1.5mm">Le subjonctif s\'emploie presque toujours après <b>que</b>. Pour le former, je prends le <b>radical de « ils » au présent</b> (ils <b>finiss</b>ent) + <b>-e, -es, -e, -ions, -iez, -ent</b>. Avec <b>nous</b> et <b>vous</b>, la forme ressemble à l\'<b>imparfait</b> : que nous venions, que vous preniez.</p>' +
        compact(table(["", "parler", "finir", "venir", "être", "avoir"], [["que je / j'", "parl<b>e</b>", "finiss<b>e</b>", "vienn<b>e</b>", "sois", "aie"], ["que tu", "parl<b>es</b>", "finiss<b>es</b>", "vienn<b>es</b>", "sois", "aies"], ["qu'il / elle / on", "parl<b>e</b>", "finiss<b>e</b>", "vienn<b>e</b>", "soit", "ait"],
                                                         ["que nous", "parl<b>ions</b>", "finiss<b>ions</b>", "ven<b>ions</b>", "soyons", "ayons"], ["que vous", "parl<b>iez</b>", "finiss<b>iez</b>", "ven<b>iez</b>", "soyez", "ayez"], ["qu'ils / elles", "parl<b>ent</b>", "finiss<b>ent</b>", "vienn<b>ent</b>", "soient", "aient"]], ["34mm", "30mm", "30mm", "30mm", "29mm", "29mm"])) +
        '<p class="sm" style="margin:1.5mm 0 1mm"><b>Deux radicaux</b> (comme venir) : prendre → que je <b>prenne</b>, que nous <b>prenions</b> · boire → <b>boive</b>, <b>buvions</b> · devoir → <b>doive</b>, <b>devions</b> · voir → <b>voie</b>, <b>voyions</b> · recevoir → <b>reçoive</b>, <b>recevions</b>.<br><b>Irréguliers</b> : aller → que j\'<b>aille</b>, que nous <b>allions</b> · faire → que je <b>fasse</b> · pouvoir → que je <b>puisse</b> · savoir → que je <b>sache</b> · vouloir → que je <b>veuille</b>, que nous <b>voulions</b> · falloir → qu\'il <b>faille</b>.</p>'
        '<div class="astuce" style="margin:1mm 0 0">🔁 <b>Rappel du module 7</b> : « il faut que + subjonctif ». ⚠️ Avec les verbes en <b>-er</b>, je, tu, il et ils se prononcent souvent comme au présent (que je parle = je parle) : c\'est le <b>sens</b> et le mot <b>que</b> qui m\'aident.</div>')
    e = E("Je conjugue au subjonctif présent.", card("1. que je (voter) ______________ 2. que tu (choisir) ______________ 3. qu'elle (prendre) ______________ 4. que nous (venir) ______________ 5. que vous (être) ______________ 6. qu'ils (avoir) ______________ 7. que j'(aller) ______________ 8. que nous (faire) ______________"), ["complete"], 1, "C",
          sol="1. vote — 2. choisisses — 3. prenne — 4. venions — 5. soyez — 6. aient — 7. aille — 8. fassions")
    e2 = E("Je retrouve l'infinitif de chaque verbe au subjonctif.", card("1. que tu saches → ______________ 2. qu'il puisse → ______________ 3. que nous voyions → ______________ 4. qu'elles boivent → ______________ 5. que je veuille → ______________ 6. qu'on doive → ______________"), ["lis", "complete"], 2, "C",
           sol="1. savoir — 2. pouvoir — 3. voir — 4. boire — 5. vouloir — 6. devoir")
    b.page(f'{l1}{e}{e2}', "Leçon 1")
    e = E("Du présent au subjonctif. Je complète le tableau.", tall(compact(table(["Infinitif", "Présent (ils)", "Subjonctif (je)", "Subjonctif (nous)"], [["élire", "ils élisent", "que j'élise", ""], ["écrire", "", "", ""], ["mettre", "", "", ""], ["dire", "", "", ""], ["recevoir", "", "", ""]], ["40mm", "46mm", "48mm", "48mm"])), 6.5), ["complete"], 2, "C",
          sol="élire : que nous élisions · écrire : ils écrivent, que j'écrive, que nous écrivions · mettre : ils mettent, que je mette, que nous mettions · dire : ils disent, que je dise, que nous disions · recevoir : ils reçoivent, que je reçoive, que nous recevions")
    e2 = E("J'écoute 8 phrases. Le verbe est-il à l'indicatif ou au subjonctif ? Je coche.", checks(8, ["indicatif", "subjonctif"]), ["ecoute", "coche"], 2, "A",
           script="1. Nous faisons. 2. Il faut que nous fassions. 3. Je sais que tu es là. 4. Je veux que tu sois là. 5. Il faut qu'elle puisse. 6. Elle peut. 7. Vous allez. 8. Il faut que vous alliez.",
           sol="indicatif : 1, 3, 6, 7 · subjonctif : 2, 4, 5, 8")
    e3 = E("Je complète avec être ou avoir au subjonctif.", card("1. Il faut que tu ______________ à l'heure au bureau de vote. 2. Il faut que nous ______________ notre carte d'élève. 3. Il faut que les délégués ______________ à l'écoute. 4. Il faut que vous ______________ le temps de lire les programmes. 5. Il faut que je ______________ honnête."), ["complete"], 1, "C",
           sol="1. sois — 2. ayons — 3. soient — 4. ayez — 5. sois")
    e4 = E("Les verbes à deux radicaux. Je complète.", card("1. Il faut que je (prendre) ______________ la parole et que nous (prendre) ______________ une décision. 2. Il faut qu'il (venir) ______________ et que vous (venir) ______________ aussi. 3. Il faut que tu (voir) ______________ le directeur et que nous le (voir) ______________ ensemble."), ["complete"], 2, "C",
           sol="1. prenne, prenions — 2. vienne, veniez — 3. voies, voyions")
    e5 = E("Défi ! Je choisis un verbe irrégulier (aller, faire, pouvoir, savoir ou vouloir) et je le conjugue au subjonctif à toutes les personnes. Puis j'écris une phrase avec « il faut que ».", lines(3), ["ecris"], 3, "C",
           sol="Ex. : que je fasse, que tu fasses, qu'il fasse, que nous fassions, que vous fassiez, qu'ils fassent. Il faut que nous fassions une affiche pour la campagne.")
    b.page(f'{e}{e2}{e3}{e4}{e5}', "S'entraîner")

    # ---------- Leçon 2 : l'obligation et l'interdiction ----------
    l2 = lecon("Exprimer l'obligation et l'interdiction", compact(table(["Pour exprimer…", "Expressions + subjonctif", "Exemples"], [
        ["une <b>obligation</b>", "il faut que · il est obligatoire que · exiger que · le règlement impose que", "Il faut que chaque élève <b>ait</b> sa carte. · Le règlement exige que nous <b>soyons</b> à l'heure."],
        ["une <b>nécessité</b>", "il est nécessaire que · il est important que · il est indispensable que", "Il est important que les délégués <b>sachent</b> écouter."],
        ["une <b>interdiction</b>", "il ne faut pas que · il est hors de question que", "Il ne faut pas que tu <b>montres</b> ton bulletin."]], ["32mm", "68mm", "82mm"])) +
        '<div class="astuce" style="margin:2mm 0 1mm">🔀 <b>Règle générale ou personne précise ?</b> Il faut <b>voter</b>. (tout le monde : <b>infinitif</b>) → Il faut que <b>tu</b> <b>votes</b>. (une personne : <b>subjonctif</b>) · Il est interdit <b>de fumer</b>. (infinitif) · Les élèves <b>doivent</b> respecter le règlement. (<b>devoir</b> + infinitif)</div>'
        '<p class="sm" style="margin:0">📜 Dans les <b>règlements</b> et les <b>lois</b>, on trouve souvent : « L\'élève <b>est tenu de</b>… » (= il doit) · « Il <b>est interdit de</b>… » · « Toute absence <b>doit être</b> justifiée. » (passif, module 8) · le <b>présent</b> à valeur d\'obligation : « L\'élève <b>présente</b> son journal de classe. »</p>')
    e = E("J'entoure la forme correcte.", card("1. Il faut que les candidats (<b>respectent</b> / <b>respecter</b>) les autres. 2. Il faut (<b>voter</b> / <b>votes</b>) en silence. 3. Il est important que tu (<b>dis</b> / <b>dises</b>) la vérité. 4. Il ne faut pas que nous (<b>soyons</b> / <b>sommes</b>) en retard. 5. Il est interdit (<b>de courir</b> / <b>que courir</b>) dans les couloirs."), ["lis", "entoure"], 1, "C",
          sol="1. respectent — 2. voter (règle générale) — 3. dises — 4. soyons — 5. de courir")
    e2 = E("Je transforme avec « il faut que » + subjonctif.", f'<p>1. Les électeurs doivent montrer leur carte. → {blank("xl")}</p><p>2. Tu dois aller dans l\'isoloir. → {blank("xl")}</p><p>3. Nous devons faire le dépouillement. → {blank("xl")}</p>', ["ecris"], 2, "C",
           sol="1. Il faut que les électeurs montrent leur carte. — 2. Il faut que tu ailles dans l'isoloir. — 3. Il faut que nous fassions le dépouillement.")
    b.page(f'{l2}{e}{e2}', "Leçon 2")
    e = E("Les règles de l'élection. J'écoute M. Diallo et je complète avec le verbe au subjonctif.", card("« Pour que l'élection soit juste, il faut que chaque candidat ______________ (écrire) un programme. Il est important que vous ______________ (lire) toutes les affiches. Le jour du vote, il faut que chacun ______________ (aller) seul dans l'isoloir. Il ne faut pas que vous ______________ (dire) pour qui vous votez. Enfin, il est nécessaire que deux élèves ______________ (pouvoir) vérifier le dépouillement. »", 1.95), ["ecoute", "complete"], 2, "A",
          script="Lire le texte avec les verbes.",
          sol="écrive · lisiez · aille · disiez · puissent")
    e2 = E("Règle générale ou personne précise ? Je complète avec l'infinitif ou le subjonctif.", card("1. Il faut (respecter) ______________ le matériel. 2. Il faut que vous (respecter) ______________ le matériel. 3. Il est interdit d'(utiliser) ______________ son GSM en classe. 4. Il est important que Yonas (prendre) ______________ la parole. 5. Il est nécessaire de (savoir) ______________ nager. 6. Il faut que tu (savoir) ______________ ta leçon."), ["complete"], 2, "C",
           sol="1. respecter — 2. respectiez — 3. utiliser — 4. prenne — 5. savoir — 6. saches")
    e3 = E("Je réécris les règles du règlement de la bibliothèque en commençant par « Il faut que les élèves… » ou « Il ne faut pas que les élèves… ».", '<div class="card sm" style="background:#fff;font-family:\'DejaVu Serif\'">Art. 1. L\'élève est tenu de rendre les livres dans les quinze jours. · Art. 2. Il est interdit de manger dans la salle de lecture. · Art. 3. L\'élève doit faire silence.</div>' + lines(3), ["lis", "ecris"], 2, "C",
           sol="Il faut que les élèves rendent les livres dans les quinze jours. · Il ne faut pas que les élèves mangent dans la salle de lecture. · Il faut que les élèves fassent silence.")
    e4 = E("Défi ! La classe organise une sortie au Parlement. J'écris 4 règles pour le voyage, avec quatre expressions différentes (il faut que, il est important que, il ne faut pas que, il est indispensable que).", lines(4), ["ecris"], 3, "C",
           sol="Ex. : Il faut que tout le monde soit à la gare à 8 h. Il est important que vous ayez votre carte d'identité. Il ne faut pas que quelqu'un se perde. Il est indispensable que chacun prenne un pique-nique.")
    b.page(f'{e}{e2}{e3}{e4}', "S'entraîner")

    # ---------- Leçon 3 : le souhait et la volonté ----------
    l3 = lecon("Exprimer le souhait et la volonté", compact(table(["Pour exprimer…", "Expressions + subjonctif", "Exemples"], [
        ["la <b>volonté</b>", "je veux que · j'exige que · je demande que · je refuse que", "Je veux que tout le monde <b>puisse</b> parler."],
        ["le <b>souhait</b>", "je souhaite que · je voudrais que · j'aimerais que · je préfère que · j'ai envie que", "J'aimerais que la cour <b>soit</b> plus verte."],
        ["un <b>vœu</b> (seul)", "Que + subjonctif !", "<b>Que</b> le meilleur <b>gagne</b> ! · <b>Que</b> chacun <b>fasse</b> son possible !"]], ["30mm", "72mm", "80mm"])) +
        '<div class="grid2" style="gap:2mm;margin-top:2mm"><div class="astuce" style="margin:0">👤 <b>Même sujet → infinitif</b><br>Je veux <b>être</b> délégué. (moi… moi)<br><b>Deux sujets différents → que + subjonctif</b><br>Je veux que <b>tu sois</b> délégué. (moi… toi)<br><s>Je veux que je sois délégué.</s></div>'
        '<div class="attention" style="margin:0">⚠️ <b>Attention aux pièges :</b> <b>espérer que</b>, <b>penser que</b>, <b>croire que</b>, <b>être sûr que</b> + <b>indicatif</b>.<br>J\'espère que tu <b>gagneras</b>. · Je pense que Daria <b>est</b> sérieuse.<br>Mais à la forme négative : Je ne pense pas qu\'elle <b>soit</b> candidate. (subjonctif)</div></div>')
    e = E("Infinitif ou subjonctif ? Je complète avec le verbe entre parenthèses.", card("1. Je veux (voter) ______________ pour Daria. 2. Je veux que tu (voter) ______________ pour Daria. 3. Fatou aimerait (devenir) ______________ déléguée. 4. Mme Lambert souhaite que les élèves (devenir) ______________ autonomes. 5. Nous préférons que vous (venir) ______________ demain. 6. Je refuse que l'on (faire) ______________ du bruit pendant le vote."), ["complete"], 2, "C",
          sol="1. voter — 2. votes — 3. devenir — 4. deviennent — 5. veniez — 6. fasse")
    e2 = E("Subjonctif ou indicatif ? J'entoure.", card("1. J'espère que tu (<b>viendras</b> / <b>viennes</b>) au conseil. 2. Je souhaite que tu (<b>viendras</b> / <b>viennes</b>) au conseil. 3. Je pense que Yonas (<b>a</b> / <b>ait</b>) de bonnes idées. 4. Je voudrais que Yonas (<b>a</b> / <b>ait</b>) plus de temps. 5. Je ne crois pas qu'il (<b>peut</b> / <b>puisse</b>) gagner."), ["lis", "entoure"], 2, "C",
           sol="1. viendras (espérer + indicatif) — 2. viennes — 3. a (penser + indicatif) — 4. ait — 5. puisse (forme négative)")
    b.page(f'{l3}{e}{e2}', "Leçon 3")
    e = E("Les souhaits de la classe. J'écoute et je relie chaque élève à son souhait.", relie(["Amina", "Mateo", "Bilal", "Fatou", "Yonas"], ["qu'on organise un tournoi de foot.", "que la cantine propose des repas végétariens.", "qu'il y ait des poubelles de tri dans la cour.", "que l'école ouvre la bibliothèque à midi.", "que les profs expliquent plus lentement."]), ["ecoute", "relie"], 1, "A",
          script="Amina : « J'aimerais que la cantine soit végétarienne. » Mateo : « Que les profs expliquent lentement ! » Bilal : « La bibliothèque à midi. » Fatou : « Du tri dans la cour. » Yonas : « Un tournoi de foot ! »",
          sol="Amina → repas végétariens · Mateo → profs plus lents · Bilal → bibliothèque à midi · Fatou → poubelles de tri · Yonas → tournoi de foot")
    e2 = E("Je transforme : je rapporte le souhait avec « vouloir que » ou « souhaiter que ».", f'<p>1. Daria : « Tout le monde doit pouvoir parler. » → Daria veut que {blank("l")}</p><p>2. Les parents : « Les enfants font leurs devoirs. » → Les parents souhaitent que {blank("l")}</p><p>3. La directrice : « Vous êtes polis avec le personnel. » → La directrice exige que {blank("l")}</p>', ["ecris"], 2, "C",
           sol="1. … tout le monde puisse parler. — 2. … leurs enfants fassent leurs devoirs. — 3. … nous soyons (les élèves soient) polis avec le personnel.")
    e3 = E("Je corrige les erreurs : une par phrase.", card("1. Je veux que je sois délégué. 2. J'espère que tu sois élu. 3. Il faut que nous allons voter. 4. Je souhaite que vous faites un effort.", 1.9) + lines(2), ["lis", "ecris"], 3, "C",
           sol="1. Je veux être délégué (même sujet → infinitif). — 2. J'espère que tu seras élu (espérer + indicatif). — 3. Il faut que nous allions voter. — 4. Je souhaite que vous fassiez un effort.")
    e4 = E("Défi ! Mes souhaits pour mon école et pour le monde. J'écris 4 phrases avec quatre expressions différentes (je souhaite que, j'aimerais que, je voudrais que, je refuse que…).", lines(4), ["ecris"], 3, "C",
           sol="Ex. : Je souhaite que tous les enfants du monde puissent aller à l'école. J'aimerais que notre cour soit plus verte. Je voudrais qu'on ait plus de sorties. Je refuse qu'on se moque des nouveaux élèves.")
    b.page(f'{e}{e2}{e3}{e4}', "S'entraîner")

    # ---------- Leçon 4 (FLSco) : lire un texte de loi simplifié ----------
    P["loi"] = b.n + 1
    l4 = lecon("Lire un texte de loi (ou un règlement)", '<p class="sm" style="margin-bottom:1.5mm">Une loi, un décret ou un règlement est découpé en <b>articles</b> numérotés (Art. 1, Art. 2…). Un article peut contenir des <b>paragraphes</b> (§ 1, § 2) ou des <b>alinéas</b> (des retours à la ligne). Chaque article répond à la question : <b>qui</b> a <b>quel droit</b> ou <b>quel devoir</b> ?</p>' +
        compact(table(["Je cherche…", "Les mots qui le montrent"], [
            ["✅ un <b>droit</b>", "a le droit de · peut · bénéficie de · est libre de · a droit à"],
            ["📌 une <b>obligation</b>", "doit · est tenu de · est obligatoire · veille à · il faut que · présent : « L'élève <b>présente</b> son journal de classe. »"],
            ["⛔ une <b>interdiction</b>", "il est interdit de · ne peut pas · ne doit pas · aucun… ne"],
            ["🔍 une <b>condition</b>, une <b>exception</b>", "si · à condition que (+ subjonctif) · sauf · excepté · quel(le)s que soient · dès (dès sa naissance)"]], ["52mm", "130mm"])) +
        '<div class="card" style="background:#fff;margin-top:2mm"><b style="color:' + MC + '">🧭 Ma méthode en 4 étapes</b><p class="sm" style="margin:1mm 0 0">① Je lis le <b>titre</b> de l\'article. ② Je repère <b>qui</b> est concerné (l\'enfant, les parents, l\'État, l\'élève, l\'école). ③ Je repère le <b>verbe</b> : droit, obligation ou interdiction ? ④ Je <b>reformule</b> avec mes mots : « Cet article veut dire que… »</p></div>' +
        '<div class="grid2" style="gap:2mm;margin-top:2mm"><div class="card sm" style="background:#FFFDF6;font-family:\'DejaVu Serif\'"><b>Texte officiel</b> (loi belge du 29 juin 1983 sur l\'obligation scolaire, art. 1er, § 1er, extrait) : « Le mineur est soumis à l\'obligation scolaire pendant une période de treize années qui commence avec l\'année scolaire qui prend cours dans l\'année où il atteint l\'âge de cinq ans et qui se termine à la fin de l\'année scolaire, dans l\'année au cours de laquelle il atteint l\'âge de dix-huit ans. »</div>'
        '<div class="card sm" style="background:' + TINT + '"><b>Je reformule</b> : En Belgique, tous les enfants <b>doivent</b> aller à l\'école (ou suivre un enseignement) <b>de 5 à 18 ans</b>, c\'est-à-dire pendant treize années scolaires. C\'est une <b>obligation</b> pour les jeunes et pour leurs parents. 💡 Il s\'agit d\'une obligation <b>scolaire</b> : on peut aussi l\'accomplir, par exemple, à l\'école à la maison, sous contrôle.</div></div>')
    e0 = E("Droit, obligation ou interdiction ? Je classe les mots soulignés.", card("1. L'élève <u>a le droit de</u> consulter ses copies. 2. L'élève <u>est tenu de</u> justifier ses absences. 3. <u>Il est interdit de</u> fumer dans l'école. 4. Tout élève <u>peut</u> demander à rencontrer un éducateur. 5. <u>Aucun</u> élève <u>ne peut</u> quitter l'école sans autorisation.", 1.8) + tall(compact(table(["✅ droit", "📌 obligation", "⛔ interdiction"], [["", "", ""]], ["60mm", "61mm", "61mm"])), 9), ["lis", "ecris"], 1, "C",
           sol="droit : 1, 4 · obligation : 2 · interdiction : 3, 5")
    b.page(f'<span class="tag-doc">🎒 FRANÇAIS DE L\'ÉCOLE</span>{l4}{e0}', "Consignes & école")
    e = E("Je lis les extraits de la Convention internationale des droits de l'enfant et je réponds.", articles(fs=8.9) +
          f'<p class="sm mt2" style="margin-bottom:1mm">1. Quel article protège un enfant qui arrive en Belgique pour fuir la guerre ? {blank("l")}</p><p class="sm" style="margin-bottom:1mm">2. Dans l\'article 28, relève une obligation et dis qui la doit. {blank("xl")}</p><p class="sm" style="margin-bottom:1mm">3. Quel article permet aux élèves de donner leur avis sur le règlement de l\'école ? Justifie avec un mot du texte. {blank("xl")}</p><p class="sm" style="margin-bottom:1mm">4. Que signifie « quels que soient leur origine, leur langue… » (art. 2) ? {blank("xl")}</p>', ["lis", "ecris"], 2, "B",
          sol="1. L'article 22 (les enfants réfugiés). — 2. « L'enseignement primaire doit être obligatoire et gratuit » : c'est une obligation pour les États (et la discipline « doit respecter » la dignité de l'enfant : obligation pour l'école). — 3. L'article 12 : « le droit de donner son opinion sur les questions qui le concernent ». — 4. Peu importe leur origine, leur langue… : tous les enfants ont les mêmes droits, sans exception.")
    e1 = E("Je reformule chaque article avec mes mots, en commençant par « Cet article veut dire que… ».", f'<p class="sm">Article 7 → {blank("xl")}</p><p class="sm">Article 19 → {blank("xl")}</p><p class="sm">Article 31 → {blank("xl")}</p>', ["lis", "ecris"], 2, "C",
          sol="Art. 7 : … chaque bébé reçoit un nom et une nationalité dès sa naissance. — Art. 19 : … les pays doivent protéger les enfants contre les coups, les mauvais traitements et l'abandon. — Art. 31 : … les enfants ont le droit de se reposer, de jouer et de participer à des activités culturelles.")
    b.page(f'{e}{e1}', "Consignes & école")
    e = E("Quel article ? Je lis chaque situation et j'écris le numéro de l'article de la Convention qui concerne l'enfant.", compact(table(["Situation", "Article"], [["Sara, 9 ans, doit travailler toute la journée et n'a jamais le temps de jouer.", ""], ["Le juge demande à Malik avec quel parent il voudrait vivre.", ""], ["À la cantine, on refuse de servir Lina à cause de sa religion.", ""], ["Un bébé naît dans un camp de réfugiés : on l'inscrit à l'état civil.", ""]], ["150mm", "32mm"])), ["lis", "ecris"], 2, "B",
           sol="31 (repos, jeu ; aussi le travail des enfants) · 12 (droit d'être entendu ; et 3, l'intérêt de l'enfant) · 2 (non-discrimination) · 7 (nom et nationalité ; et 22)")
    e2 = E("Les consignes de la classe de citoyenneté. Je relie la consigne et ce qu'il faut faire.", relie(["Reformulez l'article.", "Identifiez le destinataire de la règle.", "Justifiez par une citation.", "Comparez les deux textes.", "Illustrez par un exemple."], ["Je dis qui doit respecter la règle.", "Je donne une situation concrète.", "Je dis la même chose avec mes mots.", "Je recopie les mots exacts du texte, entre guillemets.", "Je cherche les ressemblances et les différences."]), ["lis", "relie"], 1, "B",
           sol="reformulez → avec mes mots · identifiez le destinataire → qui doit respecter · justifiez par une citation → mots exacts entre guillemets · comparez → ressemblances et différences · illustrez → situation concrète")
    e3 = E("Le jeu de l'article mystère (en duo). Je choisis un article de la Convention (p. {0}) et j'invente une situation où ce droit n'est pas respecté. Mon voisin devine le numéro de l'article et dit ce qu'il faudrait faire (« Il faudrait que… »).".format(P["loi"] + 1), lines(2), ["parle", "ecris", "duo"], 2, "A",
           sol="Ex. : « Un enfant n'a pas de papiers parce que ses parents ne l'ont jamais déclaré. » → article 7 ; il faudrait qu'on l'inscrive à l'état civil.")
    e4 = E("Défi ! J'écris un article de loi (2 phrases) pour protéger un droit qui me semble important et qui n'est pas dans les extraits.", lines(3), ["ecris"], 3, "C",
           sol="Ex. : Article 32. L'enfant a le droit d'être protégé contre le travail dangereux. Aucun enfant ne peut être obligé de travailler au lieu d'aller à l'école.")
    b.page(f'{e}{e2}{e3}{e4}', "Consignes & école")

    # ---------- Leçon 5 : la démocratie en Belgique ----------
    l5 = lecon(disc_tag("citoyenneté") + " La démocratie en Belgique", '<p class="sm" style="margin-bottom:1.5mm">La <b>démocratie</b> (du grec <i>dêmos</i>, le peuple, et <i>kratos</i>, le pouvoir) est un régime où le <b>peuple</b> choisit ses représentants par des <b>élections libres</b>. Le pouvoir y est partagé en <b>trois</b> : le pouvoir <b>législatif</b> (le Parlement <b>vote</b> les lois) · le pouvoir <b>exécutif</b> (le gouvernement <b>applique</b> les lois) · le pouvoir <b>judiciaire</b> (les juges <b>font respecter</b> les lois). La Belgique est une <b>monarchie constitutionnelle</b> (le Roi règne, mais ce sont les ministres qui gouvernent) et un <b>État fédéral</b> : le pouvoir est partagé entre plusieurs niveaux.</p>' +
        institutions() + '<div class="astuce" style="margin:1.5mm 0 0">🗳️ En Belgique, le <b>vote est obligatoire</b> pour les citoyens belges à partir de <b>18 ans</b>. En 2024, les jeunes de <b>16 et 17 ans</b> ont pu voter pour la première fois, aux élections européennes. 🇧🇪 Le chef de la commune s\'appelle le <b>bourgmestre</b> (en France : le maire) ; il est aidé par les <b>échevins</b> (en France : les adjoints).</div>')
    e = E("Je relie le pouvoir et ce qu'il fait.", relie(["le pouvoir législatif", "le pouvoir exécutif", "le pouvoir judiciaire"], ["les juges font respecter les lois.", "le Parlement vote les lois.", "le gouvernement applique les lois."]), ["lis", "relie"], 1, "B",
          sol="législatif → le Parlement vote les lois · exécutif → le gouvernement applique les lois · judiciaire → les juges font respecter les lois")
    e2 = E("Qui s'en occupe ? J'écris le niveau de pouvoir : fédéral, Communauté, Région ou commune.", compact(table(["Je veux…", "Niveau", "Je veux…", "Niveau"], [["une nouvelle carte d'identité", "", "inscrire mon frère à l'école", ""], ["savoir pourquoi le bus TEC est en retard", "", "m'engager dans l'armée", ""], ["inscrire ma sœur à la plaine de vacances", "", "signaler une rivière polluée", ""]], ["56mm", "35mm", "56mm", "35mm"])), ["lis", "ecris"], 2, "C",
          sol="carte d'identité → commune · école → Communauté (Fédération Wallonie-Bruxelles) · bus TEC → Région wallonne · armée → fédéral · plaine de vacances → commune · rivière polluée → Région (environnement)")
    b.page(f'{l5}{e}{e2}', "Leçon 5")
    e = E(disc_tag("histoire") + " Le droit de vote en Belgique : une longue conquête. Je relie la date et l'événement.", relie(["1831", "1893", "1919", "1948", "1981", "2024"], ["Le droit de vote passe de 21 à 18 ans.", "Seuls les hommes riches votent (le vote censitaire : environ 1 % de la population).", "Les femmes obtiennent le droit de vote aux élections législatives.", "Les jeunes de 16 et 17 ans votent aux élections européennes.", "Tous les hommes votent, mais certains ont plusieurs voix (vote plural) ; le vote devient obligatoire.", "Un homme = une voix (suffrage universel masculin pur)."]), ["lis", "relie"], 2, "B",
           sol="1831 → vote censitaire · 1893 → vote plural et obligatoire · 1919 → un homme = une voix · 1948 → les femmes · 1981 → 18 ans · 2024 → 16-17 ans aux européennes")
    e2 = E("Le jour du vote. Je lis la description de quatre bulletins et j'écris : valable, nul ou blanc.", '<div class="grid2" style="grid-template-columns:auto 1fr;gap:3mm;align-items:center">' + bulletin(0, 8.4) + compact(table(["Bulletin", "Valable, nul ou blanc ?"], [["A : un seul rond noirci (comme le modèle)", ""], ["B : deux ronds noircis", ""], ["C : un rond noirci et « Vive Yonas ! » écrit dessus", ""], ["D : aucun rond noirci", ""]], ["52mm", "36mm"])) + '</div>', ["lis", "ecris"], 1, "B",
           sol="A : valable · B : nul · C : nul (un signe ou un texte rend le bulletin nul) · D : blanc (il ne compte pour aucun candidat)")
    e3 = E("Défi ! Faut-il que le vote soit obligatoire ? Je donne mon avis en 3 phrases, avec un argument et un subjonctif.", lines(3), ["ecris"], 3, "C",
           sol="Ex. : Je pense que le vote obligatoire est une bonne chose. En effet, il faut que tout le monde participe aux décisions, pas seulement ceux qui s'intéressent à la politique. Cependant, il faudrait que les citoyens soient mieux informés.")
    b.page(f'{e}{e2}{e3}', "S'entraîner")

    # ---------- Leçon 6 : le programme électoral ----------
    P["prog"] = b.n + 1
    prog = f'''<div class="doc" style="transform:none;background:#fff;border:2px solid {MC};padding:2.5mm 4mm;font-size:9.1pt;line-height:1.36">
<div class="flex" style="justify-content:space-between;align-items:center"><div><b style="font-size:13pt;color:{MC}">① Daria, une voix pour chacun !</b><br><span class="xs muted">Programme de Daria Kovalenko, candidate déléguée de la classe DASPA</span></div><span style="font-size:20pt">🗳️</span></div>
<p style="margin:1mm 0"><b>②</b> Je m'appelle Daria, j'ai 16 ans et je suis arrivée d'Ukraine il y a deux ans. Je connais les difficultés des nouveaux élèves : moi aussi, au début, je n'osais pas parler.</p>
<p style="margin:1mm 0"><b>③</b> Aujourd'hui, certains élèves restent seuls à la récréation et beaucoup ont peur de poser des questions en classe.</p>
<p style="margin:1mm 0"><b>④ Si vous m'élisez, je proposerai :</b><br>1. un système de <b>parrainage</b> : chaque nouvel élève aura un « parrain » ou une « marraine » ;<br>2. une <b>boîte à idées</b> dans la classe, vidée chaque mois au conseil des élèves ;<br>3. un <b>club de conversation</b> le mardi midi, pour que chacun puisse s'entraîner à parler.</p>
<p style="margin:1mm 0"><b>⑤</b> Je m'engage à vous écouter, à transmettre fidèlement vos idées et à vous rendre compte de chaque réunion.</p>
<p style="margin:1mm 0 0"><b>⑥</b> Le 19 novembre, votez pour une classe où personne n'a peur de parler. <b>Votez Daria !</b></p></div>'''
    l6 = lecon("Écrire un programme et convaincre", '<div style="display:grid;grid-template-columns:2fr 1fr;gap:3mm;align-items:start">' + prog + '<div class="card sm" style="background:' + TINT + ';padding:2mm">'
        '<b style="color:' + MC + '">Les 6 parties</b><br>① un <b>slogan</b> (court, rythmé)<br>② je me <b>présente</b><br>③ le <b>constat</b> : ce qui ne va pas<br>④ mes <b>propositions</b> (numérotées, concrètes, réalistes)<br>⑤ mon <b>engagement</b><br>⑥ l\'<b>appel au vote</b></div></div>' +
        compact(table(["Pour…", "J'utilise…"], [["promettre", "le <b>futur</b> : je proposerai, nous organiserons · <b>je m'engage à</b> + infinitif · <b>si</b> + présent → futur : « <b>Si</b> vous m'<b>élisez</b>, je <b>proposerai</b>… »"],
                                               ["exprimer mes objectifs", "<b>je veux que</b>, <b>je souhaite que</b> + subjonctif · <b>pour que</b> + subjonctif : « pour que chacun <b>puisse</b> parler »"],
                                               ["convaincre", "le « <b>nous</b> » et le « <b>vous</b> » (je m'adresse aux électeurs) · des <b>questions</b> : « Qui n'a jamais eu peur de parler ? » · le <b>rythme en trois</b> : « écouter, transmettre, rendre compte »"]], ["38mm", "144mm"])) +
        '<div class="astuce" style="margin:1.5mm 0 0">⚖️ <b>Une promesse honnête</b> est <b>réaliste</b> : un délégué ne peut pas supprimer les interros ! Il peut <b>proposer</b>, <b>demander</b>, <b>transmettre</b>. ⚠️ <b>Si</b> + présent → futur (promesse possible) ≠ <b>si</b> + imparfait → conditionnel (hypothèse, module 12).</div>')
    e = E(f"J'analyse le programme de Daria (p. {P['prog']}). Je réponds.", f'<p class="sm">1. Quel est le slogan de Daria ? Pourquoi est-il efficace ? {blank("xl")}</p><p class="sm">2. Quel constat fait-elle (partie ③) ? {blank("xl")}</p><p class="sm">3. Relève deux verbes au futur et un verbe au subjonctif. Justifie le subjonctif. {blank("xl")}</p><p class="sm">4. Ses propositions sont-elles réalistes ? Pourquoi ? {blank("xl")}</p>', ["lis", "ecris"], 2, "B",
          sol="1. « Daria, une voix pour chacun ! » : court, il joue sur le mot « voix » (la parole et le vote). — 2. Des élèves restent seuls à la récréation et beaucoup ont peur de poser des questions. — 3. Futur : proposerai, aura (sera vidée) ; subjonctif : « pour que chacun puisse » (après « pour que »). — 4. Oui : ce sont des actions simples que la classe peut organiser avec l'accord des professeurs.")
    b.page(f'{l6}{e}', "Leçon 6")
    e = E("Si + présent → futur. Je conjugue pour écrire des promesses.", card("1. Si vous m'(élire) ______________ , je (demander) ______________ des bancs dans la cour. 2. Si nous (gagner) ______________ , nous (organiser) ______________ un tournoi. 3. Si tu (voter) ______________ pour moi, tu ne le (regretter) ______________ pas. 4. Si les élèves (avoir) ______________ des idées, je les (transmettre) ______________ ."), ["complete"], 2, "C",
           sol="1. élisez, demanderai — 2. gagnons, organiserons — 3. votes, regretteras — 4. ont, transmettrai")
    e2 = E("Promesse réaliste ou irréaliste ? Je coche.", compact(table(["", "réaliste", "irréaliste"], [[x, '<span class="chk"></span>', '<span class="chk"></span>'] for x in ["« Je supprimerai tous les devoirs. »", "« Je demanderai à la direction une fontaine à eau. »", "« J'organiserai une collecte de vêtements. »", "« Avec moi, les vacances dureront quatre mois. »", "« Je transmettrai vos idées au conseil des élèves. »"]], ["140mm", "21mm", "21mm"])), ["lis", "coche"], 1, "B",
           sol="irréaliste · réaliste · réaliste · irréaliste · réaliste")
    e3 = E("J'écoute le discours de Yonas. Je note ses trois propositions et son slogan.", tall(compact(table(["Proposition 1", "Proposition 2", "Proposition 3", "Slogan"], [["", "", "", ""]], ["46mm", "46mm", "46mm", "44mm"])), 13), ["ecoute", "ecris"], 2, "A",
           script="« Je suis Yonas. Élu, je proposerai : un tournoi de foot et de basket en mai ; la salle de sport ouverte le jeudi midi ; une sortie à vélo au printemps. Bouger ensemble, c'est mieux apprendre ! »",
           sol="1. un tournoi de foot et de basket entre les classes (en mai) · 2. ouvrir la salle de sport le jeudi midi · 3. une sortie à vélo au printemps · slogan : « Bouger ensemble, c'est mieux apprendre ! »")
    e4 = E("Défi ! J'invente trois slogans pour trois candidats imaginaires (un sur l'environnement, un sur la cantine, un sur l'entraide).", lines(3), ["ecris"], 3, "C",
           sol="Ex. : « Une cour verte, une tête ouverte ! » · « Bien manger pour mieux étudier ! » · « Ensemble, personne ne reste derrière ! »")
    b.page(f'{e}{e2}{e3}{e4}', "S'entraîner")

    # ---------- Documents de la vie ----------
    roi = f'''<div class="doc" style="transform:none;background:#FFFDF6;border:1.5px solid #9aa1b1;padding:2.5mm 4mm;font-size:8.9pt;line-height:1.34;font-family:'DejaVu Serif'">
<div class="flex" style="justify-content:space-between"><b style="font-size:11pt;color:#1F2A44">Athénée de Hautrive · Règlement d'ordre intérieur (ROI) · extraits</b><span class="xs muted">(document fictif)</span></div>
<p style="margin:1.2mm 0"><b>Art. 4 · Présence.</b> L'élève est tenu de suivre tous les cours et activités prévus à son horaire. Les cours commencent à 8 h 25 ; tout retard est noté au journal de classe.</p>
<p style="margin:1.2mm 0"><b>Art. 5 · Absences.</b> Toute absence doit être justifiée. Pour une absence de plus de trois jours, un certificat médical est exigé. Les parents (ou l'élève majeur) peuvent justifier eux-mêmes un nombre limité de demi-journées par année, fixé par la Fédération Wallonie-Bruxelles. Brosser un cours constitue une absence injustifiée.</p>
<p style="margin:1.2mm 0"><b>Art. 9 · Respect.</b> Chacun a droit au respect de sa personne, de ses convictions et de ses biens. Toute forme de violence, d'insulte, de harcèlement ou de discrimination, y compris sur les réseaux sociaux, est interdite.</p>
<p style="margin:1.2mm 0"><b>Art. 12 · Participation.</b> Chaque classe élit deux délégués au mois de novembre. Les délégués représentent leur classe au conseil des élèves. Des élèves élus siègent au conseil de participation.</p>
<p style="margin:1.2mm 0 0"><b>Art. 15 · Sanctions.</b> En cas de non-respect du présent règlement, l'élève peut recevoir, selon la gravité des faits : une remarque au journal de classe, une retenue, une exclusion d'un cours ou, dans les cas les plus graves, une exclusion définitive, après audition de l'élève et de ses parents.</p></div>'''
    P["roi"] = b.n + 1
    e = E("Je lis les extraits du règlement de l'école. Je réponds.", roi + f'<p class="sm mt2" style="margin-bottom:1mm">1. Que signifie le sigle ROI ? Pourquoi chaque école en a-t-elle un ? {blank("xl")}</p><p class="sm" style="margin-bottom:1mm">2. Mateo a été malade pendant cinq jours. Que doit-il apporter ? Justifie avec l\'article. {blank("xl")}</p><p class="sm" style="margin-bottom:1mm">3. Quel article protège Karim, insulté sur un groupe de messagerie ? Cite les mots exacts. {blank("xl")}</p><p class="sm" style="margin-bottom:1mm">4. Avant une exclusion définitive, quel droit l\'élève a-t-il ? {blank("xl")}</p>', ["lis", "ecris"], 2, "B",
          sol="1. Règlement d'ordre intérieur : il fixe les règles de vie (droits, devoirs, sanctions) pour que tout le monde les connaisse. — 2. Un certificat médical (absence de plus de trois jours, art. 5). — 3. L'article 9 : « Toute forme de violence, d'insulte, de harcèlement […] y compris sur les réseaux sociaux, est interdite. » — 4. Le droit d'être entendu : « après audition de l'élève et de ses parents ».")
    e2 = E("Belgicismes de l'école. Je relie le mot belge et son équivalent en France.", relie(["brosser un cours", "le journal de classe", "une interro", "les valves", "le préfet (d'un athénée)"], ["le directeur (d'un lycée)", "le panneau d'affichage", "sécher un cours", "le cahier de textes, l'agenda scolaire", "un contrôle"]), ["lis", "relie"], 1, "B",
           sol="brosser → sécher un cours · journal de classe → cahier de textes · interro → contrôle · valves → panneau d'affichage · préfet → directeur (proviseur)")
    b.page(f'<span class="tag-doc">📄 DOCUMENT DE LA VIE</span><h2>Le règlement de l\'école</h2>{e}{e2}', "Document de la vie")
    P["ccj"] = b.n + 1
    ccj = f'''<div class="doc" style="transform:none;border:2px solid #2BA88F;background:#fff;padding:3mm 4mm;font-size:9.2pt;line-height:1.38">
<div class="flex" style="justify-content:space-between;align-items:center"><div><span class="xs" style="color:#2BA88F;font-weight:700">COMMUNE DE HAUTRIVE · SERVICE JEUNESSE</span><br><b style="font-size:14pt;color:#1F2A44">🏛️ Conseil communal des jeunes : deviens conseiller !</b></div><span class="xs muted">(document fictif)</span></div>
<div class="grid2" style="gap:3mm;margin-top:1.5mm"><div><b>C'est quoi ?</b> Un groupe de 20 jeunes élus pour deux ans. Ils se réunissent une fois par mois à l'hôtel de ville, donnent leur avis au conseil communal et mènent des projets pour les jeunes de la commune (skatepark, fête de quartier, propreté…).<br><b>Qui peut se présenter ?</b> Tous les jeunes de <b>12 à 17 ans</b> qui habitent ou vont à l'école à Hautrive, <b>quelle que soit leur nationalité</b>.<br><b>Qui vote ?</b> Les élèves des écoles secondaires de Hautrive, en classe, le 2 février.</div>
<div><b>Comment être candidat ?</b><br>① remplir le formulaire de candidature (avec la signature d'un parent) ;<br>② écrire un court programme (10 lignes maximum) ;<br>③ le déposer au Service Jeunesse ou l'envoyer à ccj@hautrive-exemple.be <b>avant le 15 décembre</b>.<br><b>Ce que tu y gagnes :</b> tu découvres comment fonctionne ta commune, tu apprends à parler en public, à débattre et à mener un projet… et tu rencontres le bourgmestre !</div></div></div>'''
    e = E("Je lis l'appel à candidatures. Je réponds.", ccj + f'<p class="mt2 sm">1. Combien de jeunes sont élus ? Pour combien de temps ? {blank("l")}</p><p class="sm">2. Yonas n\'est pas belge. Peut-il se présenter ? Justifie. {blank("xl")}</p><p class="sm">3. Quelles sont les trois étapes pour être candidat ? Quelle est la date limite ? {blank("xl")}</p><p class="sm">4. Cite deux projets que peut mener le conseil. {blank("l")}</p><p class="sm">5. Pourquoi faut-il la signature d\'un parent, à ton avis ? {blank("xl")}</p>', ["lis", "ecris"], 2, "B",
          sol="1. 20 jeunes, pour deux ans. — 2. Oui : « quelle que soit leur nationalité » ; il suffit d'avoir entre 12 et 17 ans et d'habiter ou d'aller à l'école à Hautrive. — 3. Remplir le formulaire (signé par un parent), écrire un programme de 10 lignes maximum, le déposer ou l'envoyer avant le 15 décembre. — 4. Un skatepark, une fête de quartier, des actions de propreté. — 5. Parce que les candidats sont mineurs : les parents doivent être d'accord.")
    e2 = E("Je remplis le formulaire de candidature (pour moi ou pour un personnage).", compact(table(["Nom et prénom", "Âge", "École et classe", "Pourquoi je me présente (une phrase)"], [["", "", "", ""]], ["44mm", "16mm", "40mm", "82mm"])).replace("<td></td>", '<td style="height:12mm"></td>'), ["ecris"], 1, "C",
           sol="Formulaire complet ; la phrase de motivation contient un souhait (« Je voudrais que les jeunes… »).")
    e3 = E(disc_tag("maths") + " Au dépouillement, 240 élèves ont voté : 12 bulletins sont nuls et 8 sont blancs. Combien de votes sont valables ? Une candidate obtient 57 voix valables : quel pourcentage des votes valables cela représente-t-il ? (arrondis à l'unité)", f'<p>{blank("xl")}</p>', ["ecris"], 2, "C",
           sol="240 − 12 − 8 = 220 votes valables · 57 ÷ 220 × 100 ≈ 25,9 → environ 26 %")
    b.page(f'<span class="tag-doc">📄 DOCUMENT DE LA VIE</span><h2>Le conseil communal des jeunes</h2>{e}{e2}{e3}', "Document de la vie")

    # ---------- Vers les épreuves ----------
    TXT = ["Dans de nombreuses écoles secondaires de Belgique francophone, les élèves de chaque classe élisent un ou deux délégués au début de l'année. Ces délégués se réunissent ensuite au sein d'un conseil des élèves. Cette pratique n'est pas seulement une tradition : elle permet aux jeunes de découvrir, à leur échelle, le fonctionnement d'une démocratie.",
           "Le rôle du délégué est souvent mal connu. Il ne s'agit ni d'un « chef de classe » ni d'un surveillant. Le délégué est un porte-parole : il recueille les idées et les difficultés de ses camarades, les transmet aux professeurs ou à la direction, puis il rend compte des réponses obtenues. Pour bien jouer ce rôle, il faut qu'il sache écouter tout le monde, y compris ceux qui ne pensent pas comme lui.",
           "Le conseil des élèves peut aussi mener des projets : installer des bancs dans la cour, organiser une journée de solidarité, proposer des changements au règlement. Dans l'enseignement secondaire, des élèves élus siègent également au conseil de participation, aux côtés des enseignants, des parents et de la direction. Ils peuvent y donner leur avis sur la vie de l'école.",
           "Cette participation correspond à un droit reconnu par la Convention internationale des droits de l'enfant, adoptée par l'ONU le 20 novembre 1989 : le droit, pour l'enfant, d'exprimer son opinion sur les questions qui le concernent. Encore faut-il que les adultes écoutent vraiment. Les spécialistes le rappellent : un conseil des élèves dont les propositions restent toujours sans réponse décourage les jeunes, au lieu de les former à la citoyenneté."]
    P["epr"] = b.n + 1
    texte = '<div class="card" style="background:#fff;font-size:9.5pt;line-height:1.44;padding:2.5mm 4mm"><b style="color:' + MC + '">Le délégué de classe : un apprentissage de la démocratie</b> <span class="xs muted">(article écrit pour le cahier)</span>' + "".join(f'<p style="margin:1.1mm 0"><b class="xs" style="color:{MC}">§{i}</b> {t}</p>' for i, t in enumerate(TXT, 1)) + '</div>'
    e = E("Entraînement de type CE1D : je lis l'article et je réponds en justifiant.", texte +
          f'<p class="sm mt2" style="margin-bottom:1mm">a) Quelle est l\'idée principale du texte ? Formule-la en une phrase. {blank("xl")}</p><p class="sm" style="margin-bottom:1mm">b) Selon le § 2, le délégué est-il un « chef de classe » ? Quel mot du texte définit son rôle ? {blank("xl")}</p><p class="sm" style="margin-bottom:1mm">c) Cite les trois actions du délégué décrites au § 2. {blank("xl")}</p><p class="sm" style="margin-bottom:1mm">d) « il faut qu\'il <b>sache</b> écouter » (§ 2) : à quel mode et à quel temps est ce verbe ? Pourquoi ? {blank("xl")}</p><p class="sm" style="margin-bottom:1mm">e) Vrai ou faux ? Justifie par une citation : « Seuls les professeurs et la direction siègent au conseil de participation. » {blank("xl")}</p><p class="sm" style="margin-bottom:1mm">f) Dans le § 4, à quoi renvoie le pronom « les » dans « au lieu de <b>les</b> former » ? {blank("l")}</p>', ["lis", "ecris"], 3, "C",
          sol="d) Subjonctif présent (savoir), après « il faut que ». — e) Faux : des élèves élus y siègent « aux côtés des enseignants, des parents et de la direction » (§ 3). — f) Les jeunes. — a) Élire des délégués et participer au conseil des élèves permet aux jeunes d'apprendre la démocratie (à condition que les adultes les écoutent). — b) Non : c'est un « porte-parole ». — c) Il recueille les idées et les difficultés, il les transmet, il rend compte des réponses.")
    b.page(EPR.format(k="CE1D", t="Lire un texte informatif") + e, "Vers les épreuves")
    e = E("Suite de l'épreuve.", f'<p class="sm">g) Selon toi, à quoi sert un délégué ? Réponds en 3 lignes avec un connecteur.</p>{lines(4)}', ["lis", "ecris"], 3, "C",
          sol="g) Avis structuré (ex. : « Un délégué sert à faire entendre la voix des élèves ; en effet, il transmet leurs idées à la direction. »).")
    e2 = E("Entraînement DELF B1 · production orale, partie 3 : j'exprime un point de vue (préparation : 10 minutes ; exposé et discussion : 5 à 7 minutes).", f'<div class="card" style="background:{TINT}"><b>Document :</b> « Dans une école de Liège, ce sont les élèves qui ont réécrit une partie du règlement, avec les professeurs. Résultat : moins de sanctions et une meilleure ambiance. Pour la directrice, « les élèves respectent mieux une règle qu\'ils ont aidé à écrire ». Mais certains parents s\'inquiètent : les jeunes sont-ils assez mûrs pour décider ? » <span class="xs muted">(texte fictif)</span><br><b>Consigne :</b> Dégagez le thème du document, puis donnez votre opinion : faut-il que les élèves participent à l\'écriture du règlement de leur école ?</div>' +
           compact(table(["Mon plan", "Mes idées"], [["① Le thème (une phrase)", ""], ["② Mon opinion + argument 1 et un exemple", ""], ["③ Argument 2 (ou une concession : certes… mais)", ""], ["④ Conclusion", ""]], ["66mm", "116mm"])).replace("<td></td>", '<td style="height:14mm"></td>') + '<div class="astuce mt2">🎓 Au DELF B1, l\'examinateur pose ensuite des questions pour approfondir ou contredire ton avis : garde ton calme, reformule la question (« Si je comprends bien, vous me demandez si… ») et défends ton point de vue avec un exemple.</div>', ["parle", "ecris"], 3, "A",
           sol="Grille DELF B1 (partie 3) : thème dégagé, opinion claire, arguments illustrés d'exemples, connecteurs, concession, au moins un subjonctif (il faut que, je souhaite que), réponses aux questions de l'examinateur.")
    b.page(f'{e}{e2}', "Vers les épreuves")

    # ---------- Sons ----------
    e = E("[ɔ̃] ou [jɔ̃] ? Présent ou subjonctif ? J'écoute et je répète.", '<div class="grid2"><div class="card c"><div class="big"><b>[ɔ̃]</b> présent</div><p class="big" style="margin:1mm 0 0">nous vot<b>ons</b> · nous chois<b>issons</b> · nous pren<b>ons</b> · nous all<b>ons</b></p></div><div class="card c"><div class="big"><b>[jɔ̃]</b> subjonctif (et imparfait)</div><p class="big" style="margin:1mm 0 0">que nous vot<b>ions</b> · que nous chois<b>issions</b> · que nous pren<b>ions</b> · que nous all<b>ions</b></p></div></div><p class="sm" style="margin:2mm 0 0">✏️ Le son [j] (comme dans <i>yeux</i>) est court mais bien audible : nous vot<b>i</b>ons. Avec <b>avoir</b>, <b>être</b>, <b>voir</b>, <b>croire</b>, on écrit <b>y</b> : que nous <b>ayons</b>, <b>soyons</b>, <b>voyions</b>, <b>croyions</b>.</p>', ["ecoute", "repete"], 1, "A",
          script="Lire chaque paire deux fois en marquant bien le [j].", sol="Activité orale.")
    e2 = E("J'écoute : [ɔ̃] ou [jɔ̃] ? Je coche.", checks(8, ["[ɔ̃]", "[jɔ̃]"]), ["ecoute", "coche"], 2, "A", script="1. parlions 2. écoutons 3. lisions 4. faisons 5. ayons 6. sommes 7. soyons 8. disons (avec « nous »)",
           sol="[ɔ̃] : 2, 4, 6, 8 · [jɔ̃] : 1, 3, 5, 7")
    e3 = E("J'écris -ons ou -ions, puis je lis la phrase à voix haute.", card("1. Il faut que nous vot____ jeudi. 2. Aujourd'hui, nous prépar____ les affiches. 3. Il est important que nous écout____ tout le monde. 4. Nous compt____ les voix après le vote. 5. Je veux que nous organis____ une fête."), ["complete", "repete"], 1, "C",
           sol="1. votions — 2. préparons — 3. écoutions — 4. comptons — 5. organisions")
    e4 = E("Dictée : j'écoute deux fois et j'écris (attention au subjonctif !).", lines(3), ["ecoute", "ecris"], 2, "A",
           script="« Il faut que nous choisissions bien nos délégués. Je souhaite que chacun puisse donner son avis et que les élus soient à l'écoute de la classe. »",
           sol="Il faut que nous choisissions bien nos délégués. Je souhaite que chacun puisse donner son avis et que les élus soient à l'écoute de la classe.")
    b.page(f'<h2>J\'écoute bien · [ɔ̃] / [jɔ̃]</h2>{e}{e2}{e3}{e4}', "Sons")
    e = E("Les liaisons de la citoyenneté. Je marque les liaisons (‿) puis je lis.", '<div class="card big" style="line-height:2">1. les‿élections · les‿électeurs 2. un‿élu · un‿enfant 3. Vous‿avez le droit de voter. 4. les‿enfants ont des‿obligations (pas de liaison après « et » : droits et | devoirs) 5. C\'est‿important. 6. nos‿idées · nos‿engagements</div>', ["lis", "repete"], 1, "A",
          sol="Liaisons en [z] : les‿élections, les‿électeurs, vous‿avez, nos‿idées, nos‿engagements · en [n] : un‿élu, un‿enfant · en [t] : c'est‿important · aussi les‿enfants, des‿obligations · jamais après « et ».")
    e2 = E("Parler pour convaincre. J'écoute la prof, puis je lis en respectant les pauses (|) et en insistant sur les mots en gras.", '<div class="card big" style="line-height:1.9;background:#fff">Chers camarades, | qui n\'a jamais eu <b>peur</b> de parler ? ↗ | Moi, | je veux une classe où <b>chacun</b> | ose <b>lever la main</b>. | Je vous promets trois choses : | <b>écouter</b>, | <b>transmettre</b>, | <b>rendre compte</b>. | Le 19 novembre, | votez <b>Daria</b> ! ↘</div>', ["ecoute", "repete"], 2, "A",
           script="Voix forte ; pauses ; rythme en trois.", sol="Activité orale ; l'élève respecte les pauses, monte la voix sur la question et la descend à la fin.")
    e3 = E("J'écoute les résultats de l'élection annoncés par Mme Lambert. Je complète le tableau.", compact(table(["Candidat", "Daria", "Yonas", "Fatou", "Bulletins nuls", "Bulletins blancs"], [["Nombre de voix", "", "", "", "", ""]], ["36mm", "25mm", "25mm", "25mm", "36mm", "35mm"])).replace("<td></td>", '<td style="height:10mm"></td>') + f'<p class="sm mt2">Qui sont les deux délégués ? {blank("xl")}</p>', ["ecoute", "ecris"], 2, "A",
           script="« Dix-huit bulletins : Daria, sept voix ; Yonas, six ; Fatou, quatre ; un bulletin nul, aucun blanc. Bravo à nos délégués, Daria et Yonas ! »",
           sol="Daria 7 · Yonas 6 · Fatou 4 · nuls 1 · blancs 0 · Les délégués sont Daria et Yonas.")
    e4 = E("Je lis vite et bien.", '<div class="card big c" style="line-height:1.8">Si six citoyens choisissent six sièges, ces six sièges sont-ils sûrs ?<br>Qu\'il faille que Félix vote vite, voilà ce que veut Valérie.</div>', ["lis", "repete"], 2, "A", sol="Activité orale (virelangues écrits pour la classe).")
    b.page(f'<h2>J\'écoute bien · le discours et les résultats</h2>{e}{e2}{e3}{e4}', "Sons")

    # ---------- Révision spirale ----------
    e = E("🔁 V3 · Module 12 · Le conditionnel. Je complète : Si j'(être) ______________ bourgmestre, je (construire) ______________ un skatepark.", "", ["complete"], 1, "C", sol="étais · construirais")
    e2 = E("🔁 V3 · Module 4 · L'histoire. En quelle année la Belgique a-t-elle adopté sa Constitution ? ______________", "", ["complete"], 1, "C", sol="1831")
    e3 = E("🔁 V3 · Module 8 · Le passif. « Les élèves élisent les délégués. » → Les délégués ______________________________ .", "", ["ecris"], 2, "C", sol="Les délégués sont élus par les élèves.")
    e4 = E("🔁 V3 · Module 7 · Les connecteurs. Je complète avec : en effet · pourtant · donc. Le vote est secret ; ______________ , personne ne peut voir votre choix. Yonas a fait une belle campagne ; ______________ , il n'a pas gagné. Fatou a eu le moins de voix ; ______________ , elle n'est pas élue.", "", ["complete"], 2, "C", sol="en effet · pourtant · donc")
    e5 = E("🔁 V3 · Module 9 · Le passé simple. Je conjugue : Ce jour-là, les citoyens (aller) ______________ voter et le roi (signer) ______________ la loi.", "", ["complete"], 2, "C", sol="allèrent · signa")
    e6 = E("🔁 V3 · Module 10 · Les figures de style. « Le vote est la voix du peuple. » C'est une ______________ .", "", ["complete"], 1, "C", sol="métaphore")
    e7 = E("🔁 V3 · Module 6 · Le discours indirect. Daria dit : « Je serai à votre écoute. » → Daria dit qu'elle ______________________________ .", "", ["ecris"], 2, "C", sol="Daria dit qu'elle sera à notre écoute.")
    e8 = E("🔁 V2 · Module 12 · Les démarches. Où demande-t-on une carte d'identité en Belgique ? Quel document faut-il présenter le jour des élections ?", '<p>' + blank("xl") + '</p>', ["ecris"], 1, "C", sol="À l'administration communale (service population) · la convocation électorale et la carte d'identité.")
    b.page(f'<h2>🔁 Je révise les modules précédents</h2>{e}{e2}{e3}{e4}{e5}{e6}{e7}{e8}', "Je révise")

    # ---------- Ateliers ----------
    pb = [("🍽️", "La file à la cantine est trop longue."), ("📱", "Des photos de classe circulent sans autorisation."), ("🧹", "La cour est sale après la récréation."), ("📚", "Les nouveaux élèves ne comprennent pas les consignes."), ("🚲", "Il n'y a pas de parking à vélos."), ("🔇", "Le local d'étude est trop bruyant.")]
    e = E("Le conseil de classe des élèves (groupes de 4) : nous tirons une carte « problème », nous en discutons et nous proposons deux solutions.", '<div class="grid3" style="gap:1.5mm">' + "".join(f'<div class="card c sm" style="border:1.5px dashed {MC};padding:2mm 1mm"><span style="font-size:15pt">{ic}</span><br>{t}</div>' for ic, t in pb) + '</div>' +
          compact(table(["Rôle", "Ce qu'il fait"], [["🎤 le président", "donne la parole, surveille le temps (5 min)"], ["✍️ le secrétaire", "note les propositions"], ["🗣️ le porte-parole", "présente les solutions à la classe"], ["⚖️ le gardien des règles", "vérifie que chacun parle et que tout le monde est respecté"]], ["50mm", "132mm"])) +
          f'<p class="mt2 sm">Nos deux propositions (avec « nous proposons que » + subjonctif) :</p>{lines(2)}', ["parle", "groupe", "ecris"], 2, "A",
          script="Modéliser un conseil au tableau.",
          sol="Ex. : Nous proposons que les classes aillent à la cantine à tour de rôle. Nous proposons qu'un élève de chaque classe soit responsable de la propreté de la cour pendant une semaine.")
    e2 = E("Après le conseil : la classe vote à main levée pour la meilleure proposition. J'écris le résultat et je dis si je suis d'accord.", lines(2), ["ecoute", "ecris"], 1, "A",
           sol="Ex. : La proposition « une cantine à tour de rôle » a obtenu 12 voix sur 18. Je suis d'accord, car on attendra moins longtemps.")
    b.page(f'{atl_head("A", "Atelier · Le conseil des élèves")}{e}{e2}', "Atelier")
    charte = f'''<div class="doc" style="transform:none;background:#fff;border:1.5px solid #9aa1b1;padding:2.5mm 4mm;font-size:9.3pt;line-height:1.38">
<div class="c"><b style="font-size:11.5pt;color:{MC}">Charte du délégué de classe</b><br><span class="xs muted">Athénée de Hautrive (document fictif)</span></div>
<p style="margin:1.2mm 0">En tant que délégué(e), <b>je m'engage à</b> :</p>
<p style="margin:.8mm 0">1. écouter tous les élèves de ma classe, même ceux qui n'ont pas voté pour moi ;<br>2. transmettre fidèlement les idées et les problèmes de la classe, sans les changer ;<br>3. rendre compte à la classe de chaque réunion du conseil des élèves ;<br>4. garder pour moi les informations personnelles qu'un élève me confie ;<br>5. donner l'exemple dans le respect du règlement.</p>
<p style="margin:1.2mm 0 0"><b>L'école s'engage à</b> : réunir le conseil des élèves au moins une fois par trimestre, répondre par écrit à ses propositions et permettre aux délégués de quitter un cours pour une réunion, avec l'accord du professeur.</p>
<p class="xs muted" style="margin:1mm 0 0;text-align:right">Signatures : le / la délégué(e) · la direction</p></div>'''
    e = E("Je lis la charte du délégué. Je réponds.", charte + f'<p class="sm mt2">1. Quelle est la différence entre une charte et un règlement ? (aide : qui s\'engage ? y a-t-il des sanctions ?) {blank("xl")}</p><p class="sm">2. Quel engagement protège la vie privée des élèves ? {blank("l")}</p><p class="sm">3. À quoi l\'école s\'engage-t-elle ? Cite deux engagements. {blank("xl")}</p>', ["lis", "ecris"], 2, "B",
          sol="1. Dans une charte, des personnes s'engagent volontairement et la signent (souvent sans sanctions) ; un règlement impose des règles à tous, avec des sanctions. — 2. L'engagement 4 (garder pour soi les informations personnelles). — 3. Réunir le conseil au moins une fois par trimestre, répondre par écrit aux propositions, permettre aux délégués de quitter un cours pour une réunion.")
    e2 = E("Je reformule deux engagements de la charte avec « il faut que le délégué… ».", lines(2), ["ecris"], 2, "C",
           sol="Ex. : Il faut que le délégué écoute tous les élèves. Il faut que le délégué rende compte de chaque réunion.")
    e3 = E("Règlement ou charte ? Je compare le ROI de l'Athénée (p. {0}) et la charte du délégué. Je complète le tableau.".format(P["roi"]), tall(compact(table(["", "Le ROI", "La charte du délégué"], [["Qui l'écrit ? Qui le signe ?", "", ""], ["À qui s'adresse-t-il ?", "", ""], ["Un verbe typique", "", ""], ["Y a-t-il des sanctions ?", "", ""]], ["52mm", "65mm", "65mm"])), 9), ["lis", "ecris"], 3, "B",
           sol="ROI : écrit par l'école (pouvoir organisateur), s'impose sans signature personnelle (les parents en prennent connaissance) / charte : écrite et signée par le délégué et la direction · ROI : tous les élèves / charte : le délégué et l'école · ROI : « est tenu de », « est interdite » / charte : « je m'engage à » · ROI : oui (art. 15) / charte : non")
    b.page(f'{atl_head("B", "Atelier · Lire une charte")}{e}{e2}{e3}', "Atelier")
    e = E("Nous écrivons la charte de notre classe (en groupe, puis on met en commun). Je complète le modèle avec au moins 6 engagements.", f'<div class="card" style="background:#FFFDF6;font-family:\'DejaVu Serif\';padding:3mm 4mm"><div class="c"><b style="font-size:12pt;color:{MC}">Charte de la classe ______________</b></div><p style="margin:2mm 0 1mm"><b>Pour que chacun se sente bien et puisse apprendre, nous nous engageons à :</b></p>' + "".join(f'<p style="margin:0">{i}. {blank("xl")}</p>' for i in range(1, 7)) + f'<p style="margin:2mm 0 1mm"><b>Nous souhaitons que nos professeurs</b> {blank("xl")}</p><p style="margin:0 0 1mm"><b>Si quelqu\'un ne respecte pas la charte, nous proposons que</b> {blank("xl")}</p><p class="xs muted" style="text-align:right;margin:2mm 0 0">Fait à Hautrive, le ............ · Signatures de tous les élèves</p></div>', ["ecris", "groupe"], 3, "C",
          sol="Charte avec six engagements à l'infinitif (respecter la parole de chacun, aider les nouveaux, prendre soin du matériel, arriver à l'heure, ne pas se moquer, parler français en classe…), un souhait au subjonctif et une proposition au subjonctif.")
    e2 = E("Je relis la charte de mon groupe avec la grille.", chk3(["Les engagements commencent par un verbe à l'infinitif.", "Les engagements sont clairs et réalistes.", "Il y a un souhait et une proposition au subjonctif.", "Il n'y a pas de faute d'orthographe."]), ["lis", "coche"], 1, "C", sol="Grille complétée ; corriger avant de recopier au propre sur une affiche.")
    b.page(f'{atl_head("C", "Atelier · La charte de la classe")}{e}{e2}', "Atelier")
    cases = ["Départ : tu as 18 ans, tu reçois ta convocation électorale.", "Conjugue « être » au subjonctif (que je, que nous).", "Tu as oublié ta carte d'identité : recule de 2 cases.", "Cite deux droits de l'enfant.", "Qui vote les lois en Belgique ?", "Complète : Il faut que tu (faire) … ton devoir.",
             "Tu aides un électeur âgé à trouver son bureau de vote : avance de 2 cases.", "Cite les trois pouvoirs.", "Ton bulletin a deux croix : il est nul ! Passe un tour.", "Un vœu : Que le meilleur … (gagner) !", "Qui est le chef de la commune en Belgique ?", "Les résultats : tu es élu(e) ! BRAVO !"]
    plateau = '<div class="grid4" style="gap:1.4mm">' + "".join(f'<div class="card sm" style="padding:2mm;min-height:22mm;background:{"#FFE8D6" if i == 11 else "#fff"}"><b style="color:{MC}">{i + 1}</b> {t}</div>' for i, t in enumerate(cases)) + '</div>'
    e = E("Le jeu « Le parcours du citoyen » (2 à 4 joueurs, un dé, un pion par joueur).", '<p class="sm" style="margin:0 0 1.5mm">On lance le dé et on avance. Sur une case « question », on répond : si la réponse est juste (les autres vérifient dans le cahier), on reste ; sinon, on recule d\'une case. Le premier qui arrive à la case 12 est élu !</p>' + plateau, ["joue", "groupe"], 2, "D",
          sol="Réponses : 2. que je sois, que nous soyons · 4. Ex. : aller à l'école, donner son avis, être protégé, jouer · 5. Le Parlement (les députés) · 6. fasses · 8. législatif, exécutif, judiciaire · 10. gagne · 11. le bourgmestre.")
    e2 = E("Le jeu « Il faut que… » (toute la classe, en chaîne). Le premier élève dit une phrase ; le suivant la répète et ajoute une règle avec un autre verbe. Celui qui se trompe sur le subjonctif sort du jeu.", '<div class="card sm" style="background:#fff">Exemple : « Pour être un bon délégué, il faut que tu <b>écoutes</b>. » → « … il faut que tu écoutes et que tu <b>sois</b> patient. » → « … il faut que tu écoutes, que tu sois patient et que tu <b>prennes</b> des notes. »</div>', ["joue", "parle", "groupe"], 1, "D",
           sol="Jeu oral ; vérifier les formes (soit, ait, fasse, aille, puisse, sache, prenne, vienne).")
    e3 = E("Après le jeu : j'invente deux nouvelles cases (une question sur le subjonctif ou la démocratie, et une situation avec sa conséquence).", lines(2), ["ecris"], 2, "C",
           sol="Ex. : « Conjugue “aller” au subjonctif avec nous. » (que nous allions) · « Tu as lu tous les programmes avant de voter : avance d'une case. »")
    b.page(f'{atl_head("D", "Atelier · Le parcours du citoyen")}{e}{e2}{e3}', "Atelier")

    # ---------- ★ Coup de pouce ----------
    e = E("Je relie le mot et le dessin.", relie(["voter", "un bulletin", "une urne", "un candidat", "la loi"], ["🙋", "📜", "🗳️", "📄", "✋✅"]), ["relie"], 1, "B", alpha=True, sol="voter → ✋✅ · un bulletin → 📄 · une urne → 🗳️ · un candidat → 🙋 · la loi → 📜")
    e2 = E("Je complète avec : voter · délégué · secret · voix.", '<p class="big" style="line-height:2.1">1. Le ______________ parle pour la classe.<br>2. Je choisis un candidat : je vais ______________ .<br>3. Personne ne voit mon choix : le vote est ______________ .<br>4. Yonas a 6 ______________ .</p>', ["complete"], 1, "C", alpha=True, sol="1. délégué — 2. voter — 3. secret — 4. voix")
    e3 = E("Droit ou devoir ? J'entoure : D = droit, V = devoir.", '<div class="card big" style="line-height:2">aller à l\'école : D / V · respecter les autres : D / V · jouer : D / V · arriver à l\'heure : D / V</div>', ["entoure"], 1, "C", alpha=True, sol="aller à l'école : D (et aussi une obligation) · respecter les autres : V · jouer : D · arriver à l'heure : V")
    b.page(CP.format(t="Voter") + e + e2 + e3, "★ Coup de pouce")
    e = E("Je lis le modèle. Je complète au subjonctif.", '<div class="card" style="background:#F2F6FD"><p class="big" style="margin:0">Modèle : ils parlent → il faut que je <b>parle</b> · ils écoutent → il faut que tu <b>écoutes</b></p></div><p class="big" style="line-height:2.1;margin:2mm 0 0">1. ils votent → il faut que je ______________ .<br>2. ils lisent → il faut que tu ______________ .<br>3. ils choisissent → il faut qu\'il ______________ .<br>4. ils écrivent → il faut qu\'elle ______________ .</p>', ["lis", "complete"], 1, "C", alpha=True, sol="1. vote — 2. lises — 3. choisisse — 4. écrive")
    e2 = E("Je recopie les formes de « être » et « avoir ».", '<div class="card" style="background:#F2F6FD"><p class="big" style="margin:0">que je <b>sois</b> · que tu <b>sois</b> · qu\'il <b>soit</b><br>que j\'<b>aie</b> · que tu <b>aies</b> · qu\'il <b>ait</b></p></div>' + lines(2), ["recopie"], 1, "C", alpha=True, sol="Copie lisible et exacte.")
    e3 = E("J'entoure le bon verbe.", '<p class="big" style="line-height:2.1">1. Il faut que tu (<b>es</b> / <b>sois</b>) à l\'heure.<br>2. Il faut qu\'il (<b>fait</b> / <b>fasse</b>) ses devoirs.<br>3. Il faut que j\'(<b>aille</b> / <b>vais</b>) voter.</p>', ["entoure"], 1, "C", alpha=True, sol="1. sois — 2. fasse — 3. aille")
    b.page(CP.format(t="Le subjonctif après « il faut que »") + e + e2 + e3, "★ Coup de pouce")
    e = E("Je souhaite… Je complète avec un mot de la liste : propre · ensemble · aide · parler.", '<p class="big" style="line-height:2.1">1. Je voudrais que la cour soit ______________ .<br>2. J\'aimerais qu\'on m\'______________ en maths.<br>3. Je souhaite qu\'on puisse ______________ en classe.<br>4. Je veux qu\'on joue ______________ .</p>', ["complete"], 1, "C", alpha=True, sol="1. propre — 2. aide — 3. parler — 4. ensemble")
    e2 = E("Mon petit programme. Je complète, puis je le dis à la prof.", '<p class="big" style="line-height:2.1">Je m\'appelle ______________ . Je veux être délégué(e). Si vous votez pour moi, je vais ______________ . Je voudrais que la classe soit ______________ . Votez pour moi !</p>', ["complete", "parle"], 1, "A", alpha=True, sol="Programme complet, dit avec une voix claire.")
    e3 = E("Je lis la règle de la classe et je dessine le pictogramme.", '<div class="grid2" style="gap:3mm"><div class="card big">Il faut que je lève la main pour parler.<div style="height:22mm;border:1.5px dashed #9aa1b1;border-radius:2mm;margin-top:2mm"></div></div><div class="card big">Il ne faut pas que je mange en classe.<div style="height:22mm;border:1.5px dashed #9aa1b1;border-radius:2mm;margin-top:2mm"></div></div></div>', ["lis", "dessine"], 1, "C", alpha=True, sol="Ex. : une main levée ✋ · un sandwich barré 🚫.")
    b.page(CP.format(t="Mes souhaits et mon programme") + e + e2 + e3, "★ Coup de pouce")

    # ---------- Tâche finale ----------
    e = E("Je prépare ma candidature (ou je soutiens un candidat de mon groupe).", tall(compact(table(["Ma campagne", "Ce que j'écris / ce que je prépare", "✅"], [["Le constat : deux problèmes dans notre classe ou notre école", "", '<span class="chk"></span>'], ["Trois propositions concrètes et réalistes", "", '<span class="chk"></span>'], ["Mon slogan", "", '<span class="chk"></span>'], ["Mon engagement (je m'engage à…)", "", '<span class="chk"></span>'], ["Mon affiche : slogan, photo ou dessin, trois idées", "", '<span class="chk"></span>']], ["62mm", "104mm", "16mm"])), 20) +
          f'<div class="mt2">{etapes()}</div>', ["lis", "ecris"], 2, "C",
          sol="Fiche complète : constat, propositions réalistes, slogan, engagement, projet d'affiche.")
    b.page(tache_head("L'élection des délégués", "La classe organise une vraie élection : les candidats écrivent un programme, font campagne (affiche et discours d'une minute), puis la classe vote à bulletin secret et dépouille les votes. Les autres élèves sont électeurs, assesseurs ou journalistes.") + e, "Tâche finale", levels=False)
    e = E(f"J'écris mon programme (brouillon), sur le modèle de celui de Daria (p. {P['prog']}) : ① à ⑥, avec au moins deux futurs et deux subjonctifs.", lines(15), ["ecris"], 3, "C",
          sol="Programme complet : slogan, présentation, constat, trois propositions numérotées et réalistes, engagement, appel au vote ; futur des promesses (si + présent → futur), subjonctif (je veux que, pour que), registre adapté aux camarades.")
    e2 = E("Je prépare mon discours d'une minute : je souligne dans mon programme les trois idées que je dirai et j'écris ma première phrase (une question pour accrocher le public).", lines(2), ["ecris", "parle"], 2, "A",
           sol="Ex. : « Qui n'a jamais attendu vingt minutes à la cantine ? »")
    b.page(e + e2, "Tâche finale", levels=False)
    e = E("Le jour du vote. Nous votons à bulletin secret, puis les assesseurs dépouillent. Je note les résultats.", '<div class="grid2" style="grid-template-columns:auto 1fr;gap:3mm;align-items:start">' + bulletin(None, 8.6) + compact(table(["Candidat(e)", "Voix"], [["", ""], ["", ""], ["", ""], ["Bulletins nuls", ""], ["Bulletins blancs", ""], ["Total des bulletins", ""]], ["56mm", "30mm"])).replace("<td></td>", '<td style="height:6mm"></td>') + '</div>' +
          f'<p class="sm mt2">Les élus sont : {blank("xl")}</p>', ["ecris", "groupe"], 1, "C",
          sol="Tableau rempli ; vérifier que le total = voix + nuls + blancs ; les deux candidats qui ont le plus de voix sont élus.")
    e2 = E("Après l'élection : je m'auto-évalue et j'écris ce que je souhaite pour mes délégués (au subjonctif).", chk3(["J'ai participé à la campagne (programme, affiche ou discours).", "J'ai voté en respectant les règles du vote secret.", "J'ai utilisé le subjonctif et le futur à bon escient."]) + lines(2), ["ecris", "coche"], 1, "C",
           sol="Auto-évaluation ; souhait au subjonctif (ex. : Je souhaite que nos délégués nous écoutent et qu'ils défendent nos idées.).")
    b.page(e + compact(table(["Je vérifie avant la campagne :", "✅"], [[x, '<span class="chk"></span>'] for x in ["Mon programme a les six parties.", "Mes propositions sont concrètes et réalistes.", "J'ai utilisé le futur pour promettre et le subjonctif pour mes souhaits.", "Mon discours dure environ une minute et commence par une question."]], ["160mm", "22mm"])) + e2, "Tâche finale", levels=False)
    e = E("Je révise.", '<p>1. Le moment où l\'on compte les voix : le ______________ . 2. Celui qui se présente à une élection : le ______________ . 3. La loi la plus importante d\'un pays : la ______________ . 4. Le Parlement vote les lois : c\'est le pouvoir ______________ . 5. Le chef de la commune en Belgique : le ______________ . 6. Après « il faut que », le verbe est au ______________ . 7. Après « espérer que », le verbe est à l\'______________ .</p>', ["complete"], 1, "C",
          sol="1. dépouillement — 2. candidat — 3. Constitution — 4. législatif — 5. bourgmestre — 6. subjonctif — 7. indicatif")
    e2 = E("Je corrige le programme de Mateo : 5 erreurs (subjonctif, infinitif, espérer, si + futur, promesse irréaliste).", '<div class="card" style="font-family:\'Comic Sans MS\',cursive;background:#fff;font-size:10.3pt">« Votez Mateo ! Je veux que nous allons au garage pour un atelier mécanique. Je veux que je sois votre délégué. J\'espère que vous votiez pour moi. Si vous m\'élirez, je proposerai un tournoi. Et avec moi, il n\'y aura plus jamais d\'interros ! »</div>' + lines(4), ["lis", "ecris"], 2, "C",
           sol="… que nous allions au garage · Je veux être votre délégué (même sujet → infinitif) · J'espère que vous voterez pour moi (indicatif) · Si vous m'élisez (si + présent), je proposerai… · supprimer la promesse irréaliste sur les interros (ex. : « Je demanderai que les interros soient annoncées une semaine à l'avance. »)")
    e3 = E("Défi ! Je complète la carte mentale du module : un mot ou un exemple par branche.", tall(compact(table(["Branche", "Mes mots / mes exemples"], [["les droits et les devoirs", ""], ["l'élection (6 étapes)", ""], ["la démocratie en Belgique", ""], ["le subjonctif : obligation", ""], ["le subjonctif : souhait (et le piège d'espérer)", ""], ["le texte de loi et le programme", ""]], ["66mm", "116mm"])), 11), ["lis", "ecris"], 3, "C",
           sol="Productions variées ; vérifier un exemple juste par branche (ex. : souhait : je souhaite que tu viennes ; mais j'espère que tu viendras).")
    b.page(f'<h2>🔁 Je révise tout le module</h2>{e}{e2}{e3}', "Je révise")

    # ---------- Test ----------
    Q = [("Celui qui se présente à une élection est…", ["un candidat", "un électeur", "un assesseur", "un juge"]), ("Le moment où l'on compte les voix s'appelle…", ["le dépouillement", "la campagne", "l'isoloir", "le programme"]),
         ("La loi la plus importante d'un pays est…", ["la Constitution", "la charte", "le règlement", "le décret"]), ("En Belgique, le chef de la commune est…", ["le bourgmestre", "le préfet", "le gouverneur", "le ministre"]),
         ("Le Parlement, qui vote les lois, exerce le pouvoir…", ["législatif", "exécutif", "judiciaire", "communal"]), ("« Être » au subjonctif (que tu) :", ["que tu sois", "que tu es", "que tu seras", "que tu serais"]),
         ("« Faire » au subjonctif (que nous) :", ["que nous fassions", "que nous faisons", "que nous ferons", "que nous faisions"]), ("« Aller » au subjonctif (qu'il) :", ["qu'il aille", "qu'il va", "qu'il ira", "qu'il allait"]),
         ("Il faut que vous … la vérité.", ["disiez", "dites", "direz", "diriez"]), ("Il faut … en silence. (règle générale)", ["voter", "que vote", "votes", "votions"]),
         ("Je veux … délégué. (moi)", ["être", "que je sois", "que je suis", "je serai"]), ("J'espère que tu … à la réunion.", ["viendras", "viennes", "venir", "venais"]),
         ("Je souhaite que les élèves … écoutés.", ["soient", "sont", "seront", "être"]), ("Si vous m'élisez, je … un tournoi.", ["proposerai", "proposerais", "propose", "proposais"]),
         ("Dans un texte de loi, « est tenu de » exprime…", ["une obligation", "un droit", "une interdiction", "un souhait"]), ("L'article 12 de la Convention des droits de l'enfant protège…", ["le droit de donner son opinion", "le droit au travail", "le droit de vote", "le droit de conduire"]),
         ("Un bulletin avec deux ronds noircis est…", ["nul", "blanc", "valable", "secret"]), ("Dans une charte, les personnes…", ["s'engagent", "sont punies", "votent les lois", "jugent"]),
         ("« que nous parlions » : la terminaison se prononce…", ["[jɔ̃]", "[ɔ̃]", "[ɛ̃]", "[ɑ̃]"]), ("🔁 Conditionnel : « Si j'étais bourgmestre, je … un parc. »", ["créerais", "créerai", "crée", "créais"])]
    ans = [q[1][0] for q in Q]
    qrot = [2, 0, 3, 1, 1, 3, 0, 2, 3, 1, 0, 2, 2, 3, 1, 0, 3, 1, 2, 0]
    Q = [(q, o[r:] + o[:r]) for (q, o), r in zip(Q, qrot)]
    key = key_from(Q, ans)
    test_pages(b, 11, "Citoyens", Q, f'<h3>B1. Complète au subjonctif. (… / 3)</h3><p>Il faut que nous (choisir) ______ nos délégués. Je veux que tu (être) ______ candidat. Il est important qu\'ils (pouvoir) ______ parler.</p><h3>B2. Infinitif, subjonctif ou indicatif ? Corrige si nécessaire. (… / 2)</h3><p>1. Je veux que je parle au directeur. {blank("xl")}</p><p>2. J\'espère que vous soyez à l\'heure. {blank("xl")}</p><h3>B3. Écris un court programme de délégué (6 lignes) : un slogan, un constat, deux propositions (futur), un souhait (subjonctif), un appel au vote. (… / 5)</h3>{lines(6, True)}',
               [["expliquer un droit et un devoir de l'élève", "/ 3", ""], ["présenter son programme en une minute (futur, subjonctif)", "/ 4", ""], ["répondre à une question : « Faut-il que le vote soit obligatoire ? »", "/ 3", ""]],
               '<h3>1. Je relie le mot et le dessin. (… / 4)</h3>' + relie(["voter", "une urne", "la loi", "un candidat"], ["📜", "🙋", "✋✅", "🗳️"]) + '<h3>2. Droit ou devoir ? J\'écris D ou V. (… / 4)</h3><div class="card big">jouer : ___ · respecter les autres : ___ · aller à l\'école : ___ · arriver à l\'heure : ___</div><h3>3. Je complète : Il faut que tu (être) ______ à l\'heure. Il faut que je (faire) ______ mon devoir. (… / 4)</h3><h3>4. Je complète : Le vote est ______ (personne ne voit). Le ______ parle pour la classe. (… / 3)</h3><h3>5. Oral : je dis pourquoi je veux être délégué(e) (2 phrases). (… / 5)</h3>')
    closing(b, 11, ["Je parle de mes droits et de mes devoirs.", "J'utilise le vocabulaire de l'élection et de la démocratie.", "Je conjugue les verbes au subjonctif présent (réguliers et irréguliers).", "J'exprime une obligation ou une interdiction avec le subjonctif.", "J'exprime un souhait ou une volonté (subjonctif ou infinitif).", "Je sais qu'« espérer que » est suivi de l'indicatif.",
                    "Je lis un texte de loi simplifié et je le reformule.", "Je lis un règlement et une charte.", "J'explique comment fonctionne la démocratie en Belgique.", "J'écris un programme et je le présente pour convaincre.", "Je vote et je participe au dépouillement."],
            [("⚖️", "un droit, un devoir"), ("📜", "une loi, un article"), ("📋", "un règlement (ROI)"), ("🤝", "une charte, s'engager"), ("🚫", "une interdiction"), ("🔨", "une sanction"), ("🧑‍🤝‍🧑", "un citoyen, une citoyenne"), ("🏛️", "la démocratie"), ("📘", "la Constitution"), ("🏢", "le Parlement, un député"), ("👔", "le gouvernement, un ministre"), ("🏘️", "le bourgmestre, la commune"),
             ("🗳️", "une élection, élire"), ("🙋", "un candidat, se présenter"), ("📣", "une campagne, un programme"), ("📄", "un bulletin de vote"), ("🚪", "l'isoloir"), ("🔢", "le dépouillement, une voix"), ("🏅", "un élu, la majorité"), ("🎤", "un délégué, représenter"), ("🗣️", "un porte-parole"), ("🌍", "l'égalité, la solidarité"), ("🕊️", "la liberté"), ("📐", "le subjonctif")])
    plan_de_travail(b, E, 11, ["Le subjonctif : formation", "L'obligation et l'interdiction", "Le souhait et la volonté", "Lire un texte de loi", "La démocratie en Belgique", "Le programme électoral"], "☐ Constat et propositions<br>☐ Programme et affiche<br>☐ Discours d'une minute<br>☐ Vote et dépouillement")
    b.pages = [x.replace("padding:.8mm 1.5mm;display:flex", "padding:.3mm 1.5mm;display:flex").replace("repeat(7,1fr);gap:1.3mm", "repeat(7,1fr);gap:.7mm").replace("align-items:center;justify-content:space-between;font-size:8.5pt", "align-items:center;justify-content:space-between;font-size:8pt") for x in b.pages]  # plan compact
    if render:
        to_pdf(b.html(), '/home/claude/syllabus/out/V3_M11_eleve.pdf')

    pg, exs = helpers(b, E)
    CPp = b.marks["★ Coup de pouce"]
    days = [("1", "Collectif", f"Ouverture · BD · droits et devoirs ({pg('Découvrir')})", f"CP voter (p. {CPp[0]})"), ("2", "Collectif + duo", f"Lexique : citoyenneté, élection, valeurs ({pg('Lexique')})", "CP droit ou devoir"),
            ("3", "Rotation", f"📌 Leçon 1 subjonctif : formation ({pg('Leçon 1')}) · sons [ɔ̃] / [jɔ̃] ({pg('Sons')})", f"CP subjonctif (p. {CPp[1]})"), ("4", "Collectif", f"📌 Leçon 2 obligation, interdiction ({pg('Leçon 2')})", "CP il faut que"),
            ("5", "Rotation", f"📌 Leçon 3 souhait, volonté ({pg('Leçon 3')})", f"CP mes souhaits (p. {CPp[2]})"), ("6", "Collectif", f"📌 Leçon 4 texte de loi : Convention des droits de l'enfant ({pg('Consignes & école')}) · ROI ({pg('Document de la vie')})", "Lecture guidée article par article"),
            ("7", "Rotation", f"📌 Leçon 5 démocratie en Belgique ({pg('Leçon 5')}) · conseil communal des jeunes", "Schéma des niveaux de pouvoir colorié"), ("8", "Ateliers", f"📌 Leçon 6 programme ({pg('Leçon 6')}) · ateliers ({pg('Atelier')}) · CE1D, DELF ({pg('Vers les épreuves')})", "CP mon petit programme"),
            ("9", "Classe", f"Tâche finale : campagne, discours, vote, dépouillement ({pg('Tâche finale')})", "Rôle d'assesseur ou de journaliste"), ("10", "Seul", f"Test ({pg('Test')})", f"CP test ({pg('★ Coup de pouce · Test')})")]
    rot = [["🎧 Écouter-Parler", "Le conseil des élèves (cartes « problème »)", "30 min", "Le gardien des règles"], ["📖 Lire", "La charte du délégué", "20 min", "Oui"], ["✏️ Écrire", "La charte de la classe", "30 min", "Grille de relecture"],
           ["🧩 Jouer", "« Le parcours du citoyen » + « Il faut que… »", "20 min", "Les joueurs vérifient"], ["👩‍🏫 Table d'appui", "Coup de pouce · subjonctif, souhaits, programme", "20 min", "—"]]
    ev1 = f'''<h3>Partie B (10 points)</h3><p class="sm"><b>B1</b> : <span class="sol">choisissions · sois · puissent</span> (1 pt chacun). · <b>B2</b> : <span class="sol">Je veux parler au directeur (même sujet → infinitif) · J'espère que vous serez à l'heure (espérer + indicatif)</span> (1 pt chacun). · <b>B3</b> : les cinq éléments (2), futur des promesses (1), subjonctif du souhait (1), langue (1).</p>
<h3>Partie C · oral (10 points)</h3><p class="sm">L'élève explique un droit et le devoir qui l'accompagne (3) · il présente son programme en une minute, avec des promesses au futur et un souhait au subjonctif (4) · il répond à la question « Faut-il que le vote soit obligatoire ? » en donnant un avis et un argument (3).</p>
<h3>Test ★ Coup de pouce (20 points)</h3><p class="sm"><b>1 :</b> <span class="sol">voter → ✋✅ · une urne → 🗳️ · la loi → 📜 · un candidat → 🙋</span> (4) · <b>2 :</b> <span class="sol">D · V · D · V</span> (4) · <b>3 :</b> <span class="sol">sois · fasse</span> (4) · <b>4 :</b> <span class="sol">secret · délégué</span> (3) · <b>5 :</b> deux phrases compréhensibles (5).</p>
<h3>Lire les résultats du QCM : quelle remédiation ?</h3>{table(["Questions", "Compétence", "Si moins de la moitié est juste…"], [["1 à 5", "lexique de l'élection et de la démocratie", f"lexique ({pg('Lexique')}) + leçon 5 ({pg('Leçon 5')}) + coup de pouce p. {CPp[0]}"], ["6 à 9", "formation du subjonctif", f"leçon 1 ({pg('Leçon 1')}) + coup de pouce p. {CPp[1]}"], ["10 à 13", "obligation, souhait ; infinitif / subjonctif / indicatif", f"leçons 2 et 3 ({pg('Leçon 2')}, {pg('Leçon 3')})"], ["14", "si + présent → futur (promesse)", f"leçon 6 ({pg('Leçon 6')})"], ["15 à 18", "texte de loi, Convention, vote, charte", f"leçon 4 ({pg('Consignes & école')}) + documents ({pg('Document de la vie')}) + atelier B"], ["19", "[ɔ̃] / [jɔ̃]", f"sons ({pg('Sons')})"], ["20", "révision (conditionnel)", "module 12"]], ["24mm", "62mm", "96mm"])}'''
    ev2 = f'''<h2>Grille · tâche finale « L'élection des délégués »</h2>{table(["Critère", "Très bien", "Bien", "À retravailler", "Points"], [["<b>Programme</b> : les six parties (slogan, présentation, constat, propositions, engagement, appel)", "Complet", "Partiel", "Incomplet", "/ 4"], ["<b>Propositions</b> concrètes, réalistes, adaptées à la classe", "Convaincantes", "Générales", "Irréalistes", "/ 4"], ["<b>Langue</b> : futur des promesses, subjonctif du souhait, orthographe", "Maîtrisée", "Quelques erreurs", "Fragile", "/ 4"], ["<b>Discours</b> : une minute, voix claire, pauses, regard, accroche", "Aisé", "Correct", "Difficile", "/ 4"], ["<b>Participation au vote</b> : règles du vote secret, rôle d'assesseur ou de journaliste", "Exemplaire", "Correcte", "Passive", "/ 2"], ["<b>Affiche</b> : slogan lisible, trois idées", "Réussie", "Correcte", "Absente", "/ 2"]], ["66mm", "30mm", "30mm", "34mm", "22mm"])}
<h2 class="mt4">Différencier et remédier</h2>{table(["Difficulté", "Remédiation"], [["Former le subjonctif", "Affiche « ils + -ent → que je + -e » ; dominos présent (ils) / subjonctif ; cartes des 8 irréguliers (être, avoir, aller, faire, pouvoir, savoir, vouloir, falloir) à réviser chaque jour en rituel."], ["Infinitif ou subjonctif ?", "Flèches de couleur : même sujet = une flèche (infinitif) ; deux sujets différents = deux flèches (que + subjonctif)."], ["Espérer + subjonctif (erreur fréquente)", "Mini-affiche « espérer, penser, croire → indicatif » ; jeu du « juste / faux » en début de cours."], ["Lire un texte de loi", "Surligner en trois couleurs (droit, obligation, interdiction) ; reformuler en duo ; partir d'une situation concrète vécue."], ["Élève rapide", "Lire un extrait réel de la Convention (site de l'UNICEF ou du Délégué général aux droits de l'enfant) ; préparer un exposé sur le conseil communal des jeunes de la commune de l'école ; s'entraîner à la partie 3 du DELF B1 oral."]], ["50mm", "132mm"])}'''
    rep = f'''<h2>La citoyenneté : repères</h2>
<div class="attention"><b>Points d'attention.</b> Certains élèves viennent de pays où voter était dangereux ou interdit : présenter le vote comme une pratique de la classe, sans demander aux élèves de parler de la politique de leur pays ni de leurs opinions. Rappeler que chacun peut participer (délégués, conseil communal des jeunes, associations) et que les droits de l'enfant s'appliquent à <b>tous</b> les enfants. Ne pas interroger les élèves sur leur statut de séjour.</div>
{table(["Repère", "Ce qu'il faut savoir (vérifié en novembre 2026)"], [["La Convention internationale des droits de l'enfant (CIDE)", "Adoptée par l'Assemblée générale des Nations unies le 20 novembre 1989 (d'où la Journée internationale des droits de l'enfant, le 20 novembre) ; 54 articles ; ratifiée par la Belgique en 1991 et par presque tous les pays du monde. Extraits simplifiés, numéros d'articles exacts. En Belgique : article 22bis de la Constitution ; en FWB, le Délégué général aux droits de l'enfant."], ["L'obligation scolaire", "Loi du 29 juin 1983 : depuis la rentrée 2020, l'obligation scolaire commence à 5 ans (au lieu de 6) et dure jusqu'à 18 ans, soit treize années. L'enseignement à domicile est possible, sous contrôle."], ["Le vote en Belgique", "Vote obligatoire (instauré en 1893) pour les citoyens belges majeurs (18 ans). Étapes historiques : 1831 vote censitaire (environ 1 % de la population) · 1893 suffrage universel masculin tempéré par le vote plural · 1919 « un homme, une voix » · 1948 droit de vote des femmes aux élections législatives (premier vote en 1949 ; elles votaient déjà aux élections communales depuis 1921) · 1981 âge du vote abaissé de 21 à 18 ans · 2024 les jeunes de 16 et 17 ans votent pour la première fois aux élections européennes. Étrangers : vote communal possible, sous conditions."], ["Les institutions", "État fédéral, monarchie constitutionnelle ; Chambre : 150 députés ; 3 Communautés, 3 Régions, 10 provinces, des communes. L'enseignement relève des Communautés ; les TEC, de la Région wallonne."], ["La participation à l'école", "ROI obligatoire dans chaque école. Dans le secondaire, des élèves élus siègent au conseil de participation. Délégués et conseil des élèves : selon l'organisation de chaque école. Lien possible avec le cours d'éducation à la philosophie et à la citoyenneté (EPC)."]], ["40mm", "142mm"])}
<div class="attention mt2"><b>Fictif :</b> l'Athénée de Hautrive et son ROI, la charte du délégué, le conseil communal des jeunes de Hautrive et son appel à candidatures, l'élection de la classe (candidats, programmes, résultats), le bulletin de vote, l'école de Liège du document DELF, les témoignages (Inès, Karim, Sofia), les adresses électroniques. La Convention des droits de l'enfant (extraits simplifiés), la loi sur l'obligation scolaire, l'histoire du droit de vote et les institutions belges sont réelles.</div>
<h3>Belgicismes du module</h3><p class="sm">le <b>bourgmestre</b> et les <b>échevins</b> (France : le maire et ses adjoints) · <b>brosser</b> un cours (France : sécher) · le <b>journal de classe</b> (France : cahier de textes, agenda) · une <b>interro</b> (France : un contrôle, une interrogation écrite) · les <b>valves</b> (France : le panneau d'affichage) · le <b>préfet</b> d'un athénée (France : proviseur, directeur) · un <b>athénée</b> (établissement secondaire officiel) · le <b>ROI</b> (France : règlement intérieur) · la <b>convocation électorale</b>.</p>'''
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
    T = teacher_book(b, E, "V3 · M11", "", MC, 11, "Citoyens",
                     "<li><b>Communication :</b> parler de ses droits et de ses devoirs ; lire un règlement, une charte et un texte de loi simplifié ; comprendre le fonctionnement de la démocratie ; écrire et présenter un programme ; voter.</li><li><b>Lexique :</b> droits et règles (droit, devoir, loi, règlement, charte, sanction), l'élection (candidat, campagne, bulletin, isoloir, dépouillement, élu), la démocratie (citoyen, Parlement, gouvernement, Constitution, bourgmestre), les valeurs.</li><li><b>Langue :</b> le subjonctif présent (formation, verbes à deux radicaux, irréguliers) pour exprimer l'obligation, l'interdiction, le souhait et la volonté ; infinitif ou subjonctif ; espérer + indicatif ; si + présent → futur (promesses).</li><li><b>Oral :</b> [ɔ̃] / [jɔ̃] (présent / subjonctif) ; liaisons ; parler pour convaincre (pauses, insistance).</li><li><b>FLSco :</b> lire un texte de loi (articles, droit / obligation / interdiction, reformuler) ; consignes reformulez, identifiez, justifiez par une citation, illustrez ; citoyenneté (les trois pouvoirs, les niveaux de pouvoir, l'histoire du droit de vote).</li><li><b>Épreuves :</b> CE1D (texte informatif sur le délégué de classe) ; DELF B1 production orale, partie 3 (point de vue).</li><li><b>Documents :</b> ROI de l'école, appel à candidatures du conseil communal des jeunes, Convention des droits de l'enfant (extraits simplifiés), charte du délégué, bulletin de vote, programme électoral.</li>",
                     '<p class="sm"><b style="color:#E4572E">Indispensable</b> : il faut que + subjonctif (être, avoir, faire, aller), droits et devoirs, vocabulaire du vote.</p><p class="sm"><b style="color:#d9a400">Important</b> : souhait et volonté (infinitif ou subjonctif), lire un article de loi, les trois pouvoirs, le programme.</p><p class="sm"><b style="color:#2BA88F">Enrichissement</b> : espérer + indicatif, histoire du droit de vote, CE1D, DELF B1 oral, conseil communal des jeunes.</p>',
                     "Un exemplaire du cahier par élève · une urne (boîte en carton) et un isoloir improvisé (paravent ou tableau mobile) · bulletins photocopiés (p. de la tâche finale) · grandes feuilles pour les affiches · dés et pions pour « Le parcours du citoyen » · cartes « problème » découpées · si possible, le ROI réel de l'école et la convention de la Journée des droits de l'enfant (20 novembre).", "<b>Avant de commencer :</b> se renseigner sur l'organisation réelle des délégués dans l'école (date de l'élection, conseil des élèves) : la tâche finale peut devenir la vraie élection des délégués de la classe. Si le module tombe en novembre, le relier à la Journée internationale des droits de l'enfant (20 novembre). Vérifier si la commune a un conseil communal des jeunes ou des enfants : une visite ou l'invitation d'un jeune conseiller rend le module très concret.",
                     days, "« Le subjonctif du jour » : un verbe irrégulier au tableau, conjugué en chœur · « Droit ou devoir ? » : la prof lit une phrase, la classe lève une carte verte (droit) ou rouge (devoir) · « Espérer ou souhaiter ? » : compléter une phrase à l'oral avec le bon mode.", rot, key, (ev1, ev2), extra_pages=[(rep, "Repères")], start=tstart)
    _LM.paginate = _pg
    _LM.table = _tb
    if render:
        to_pdf(T.html(), '/home/claude/syllabus/out/V3_M11_prof.pdf')
    return b, T


if __name__ == "__main__":
    b, T = build_v3m11()
    print(b.n, T.n)
