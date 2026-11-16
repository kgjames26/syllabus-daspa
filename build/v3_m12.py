"""Volume 3 · Module 12 « Vers le monde du travail » (B1 + français de scolarisation).

Découvrir les métiers, lire une offre d'emploi, rédiger un CV et une lettre de motivation, passer un entretien.
Langue : le conditionnel présent (formation et emplois : politesse, souhait, conseil, hypothèse avec si + imparfait),
le registre formel (vouvoiement, formules, mots du registre soutenu). FLSco : les écrits professionnels.
Fil rouge : Bilal postule comme animateur à la plaine de vacances communale de Hautrive (job étudiant d'été).
Visuels : cv() (modèle de CV, vide ou rempli), lettre() (lettre de motivation annotée ①-⑧), escalier() (les étapes
d'une candidature), thermo() (thermomètre des registres), etoile() (étoile des compétences en SVG).
Faits réels (job étudiant : 650 h par an, contrat écrit, Student@work ; règles pour les 15 ans) vérifiés en novembre 2026.
"""
import sys
sys.path.insert(0, '/home/claude/syllabus')
from lib.base import *
from lib.art import *
from lib.module import *
from lib.v3 import CP, CPCOL, EPR, disc_tag
from lib.render import to_pdf

import os
import math
BUMP = int(os.environ.get("BUMP", "36"))
SCR = int(os.environ.get("SCR", "120"))
MC = "#2F6F73"
TINT = "#E4F1F1"
F = disc_tag("français")


def chk3(items, w=128):
    return table(["", "😀", "🙂", "😕"], [[x, '<span class="chk"></span>', '<span class="chk"></span>', '<span class="chk"></span>'] for x in items], [f"{w}mm", "18mm", "18mm", "18mm"])


def tall(html, h):
    return html.replace("<td></td>", f'<td style="height:{h}mm"></td>')


def compact(html):
    return html.replace('class="t"', 'class="t compact"')


def cv(rempli=True, fs=8.6):
    """Modèle de CV d'élève sur deux colonnes (rempli : CV de Bilal ; sinon cases vides à compléter)."""
    def bloc(t, c):
        return f'<div style="margin-bottom:1.6mm"><div style="font-weight:800;color:{MC};border-bottom:1.2px solid {MC};font-size:{fs + .6}pt;margin-bottom:.8mm">{t}</div>{c}</div>'
    V = (lambda s: s) if rempli else (lambda s: '<div class="line" style="margin:2.6mm 0 0"></div>' * max(1, s.count("<br>") + 1))
    gauche = (bloc("Contact", V("Rue des Tilleuls 14<br>4999 Hautrive<br>0470 12 34 56<br>bilal.cv@exemple.be")) + bloc("Langues", V("Dari : langue maternelle<br>Pachto : bon niveau<br>Français : B1 · Anglais : A2")) +
              bloc("Atouts", V("ponctuel · patient<br>souriant · sportif")) + bloc("Loisirs", V("football (entraîneur des U8)<br>dessin, jeux de société")))
    droite = (bloc("Profil", V("Élève de 17 ans, dynamique et patient, je cherche un job étudiant d'animateur pour l'été.")) +
              bloc("Formation", V("2025-2027 : DASPA puis 3e secondaire, Athénée de Hautrive<br>2019-2024 : école secondaire à Kaboul (Afghanistan)")) +
              bloc("Expériences", V("Depuis 2025 : aide-entraîneur bénévole, RFC Hautrive (enfants de 6 à 8 ans)<br>Été 2025 : aide à l'épicerie sociale (bénévolat, 2 semaines)")) +
              bloc("Compétences", V("animer un groupe d'enfants · organiser un jeu · premiers secours (formation Croix-Rouge, 1 jour)")))
    nom = "Bilal AHMADI" if rempli else "Prénom NOM : ......................................"
    return (f'<div class="doc" style="transform:none;background:#fff;border:1.5px solid #9aa1b1;padding:3mm 4mm;font-size:{fs}pt;line-height:1.35">'
            f'<div class="flex" style="justify-content:space-between;align-items:center;margin-bottom:2mm"><div><b style="font-size:{fs + 6}pt;color:#1F2A44">{nom}</b><br><span style="color:{MC}">{"Candidat animateur · plaine de vacances" if rempli else "Le poste que je cherche : ....................................."}</span></div>'
            f'<div style="width:17mm;height:20mm;border:1.2px dashed #9aa1b1;border-radius:2mm;display:flex;align-items:center;justify-content:center" class="xs muted">photo<br>(facultative)</div></div>'
            f'<div style="display:grid;grid-template-columns:1fr 2fr;gap:4mm"><div style="background:{TINT};padding:2mm;border-radius:2mm">{gauche}</div><div>{droite}</div></div></div>')


LETTRE = [("①", "Bilal AHMADI<br>Rue des Tilleuls 14<br>4999 Hautrive<br>0470 12 34 56 · bilal.cv@exemple.be", "l'expéditeur (moi)"),
          ("②", "Administration communale de Hautrive<br>Service Jeunesse · Plaine de vacances<br>Place du Marché 1<br>4999 Hautrive", "le destinataire"),
          ("③", "Hautrive, le 15 mars 2027", "le lieu et la date"),
          ("④", "<b>Objet :</b> candidature au poste d'animateur (plaine d'été 2027)", "l'objet"),
          ("⑤", "Madame, Monsieur,", "la formule d'appel"),
          ("⑥", "J'ai lu avec intérêt votre annonce publiée sur le site de la commune et je souhaiterais poser ma candidature au poste d'animateur pour le mois de juillet.<br>"
                "Depuis un an, j'aide bénévolement l'entraîneur des U8 du RFC Hautrive : j'ai appris à animer un groupe d'enfants, à organiser des jeux et à rester calme quand il y a des conflits. "
                "J'ai aussi suivi une formation d'un jour aux premiers secours. Je suis ponctuel, patient et je parle dari et pachto, ce qui pourrait être utile avec certaines familles.<br>"
                "Travailler à la plaine me permettrait de découvrir le métier d'éducateur, que j'aimerais exercer plus tard.", "le corps : ① pourquoi j'écris · ② ce que j'apporte · ③ ce que j'attends"),
          ("⑦", "Je serais très heureux de vous rencontrer pour un entretien. Dans l'attente de votre réponse, je vous prie d'agréer, Madame, Monsieur, mes salutations distinguées.", "la conclusion et la formule de politesse"),
          ("⑧", "Bilal Ahmadi<br><i>Annexe : curriculum vitae</i>", "la signature (et les annexes)")]


def lettre(annot=True, fs=9.6):
    """Lettre de motivation de Bilal, annotée ①-⑧ (annot=False : numéros seuls, pour l'exercice)."""
    def part(k):
        n, t, d = LETTRE[k]
        tag = f'<span style="color:#fff;background:{MC};border-radius:50%;padding:0 1.2mm;font-size:{fs - .5}pt;font-weight:700;margin-right:1mm">{n}</span>'
        return f'<div style="margin-bottom:1.6mm">{tag}{t}</div>'
    leg = ("".join(f'<div class="xs" style="margin-bottom:.8mm"><b style="color:{MC}">{n}</b> {d}</div>' for n, t, d in LETTRE) if annot else "")
    corps = (f'<div class="grid2" style="grid-template-columns:1fr 1fr;gap:2mm">{part(0)}<div style="text-align:right">{part(1)}</div></div>'
             f'<div style="text-align:right">{part(2)}</div>{part(3)}{part(4)}{part(5)}{part(6)}<div style="text-align:right">{part(7)}</div>')
    doc = f'<div class="doc" style="transform:none;background:#fff;border:1.5px solid #9aa1b1;padding:3mm 4mm;font-size:{fs}pt;line-height:1.38;font-family:\'DejaVu Serif\'">{corps}</div>'
    if not annot:
        return doc
    return f'<div style="display:grid;grid-template-columns:3.1fr 1fr;gap:3mm;align-items:start">{doc}<div class="card" style="background:{TINT};padding:2mm">{leg}</div></div>'


def escalier(w=180):
    """Les étapes d'une candidature, en escalier."""
    steps = ["Je me connais<br>(qualités, envies)", "Je cherche<br>une offre", "Je lis<br>l'offre", "J'écris<br>CV + lettre", "J'envoie et<br>je relance", "Je passe<br>l'entretien", "J'ai le job !<br>Je signe le contrat"]
    out = ""
    for i, s in enumerate(steps):
        h = 10 + i * 5.2
        out += (f'<div style="flex:1;display:flex;flex-direction:column;justify-content:flex-end;align-items:center">'
                f'<div class="xs" style="text-align:center;line-height:1.15;margin-bottom:1mm">{s}</div>'
                f'<div style="width:100%;height:{h}mm;background:{MC};opacity:{.45 + i * .08};border-radius:1.5mm 1.5mm 0 0;color:#fff;font-weight:800;display:flex;align-items:flex-start;justify-content:center;padding-top:1mm">{i + 1}</div></div>')
    return f'<div style="display:flex;gap:1.2mm;align-items:flex-end;width:{w}mm;max-width:100%">{out}</div>'


def thermo():
    """Thermomètre des registres de langue."""
    rows = [("SOUTENU", "#1F2A44", "Je vous saurais gré de bien vouloir m'accorder un entretien.", "lettre officielle, discours"),
            ("COURANT", MC, "Pourriez-vous me recevoir pour un entretien ?", "école, travail, courriel"),
            ("FAMILIER", "#E4572E", "Tu peux me caser un rendez-vous ?", "amis, famille, SMS")]
    return '<div style="display:grid;grid-template-columns:12mm 1fr;gap:2mm;align-items:stretch">' + \
        '<div style="background:linear-gradient(#1F2A44,#2F6F73,#E4572E);border-radius:6mm;min-height:36mm"></div><div>' + \
        "".join(f'<div class="card" style="padding:1.4mm 2.5mm;margin-bottom:1.4mm;border-left:4px solid {c}"><b style="color:{c}">{t}</b> · <i>« {ex} »</i> <span class="xs muted">→ {u}</span></div>' for t, c, ex, u in rows) + '</div></div>'


def etoile(vals=None, w=62):
    """Étoile des compétences (radar à 6 branches) : vals = notes de 0 à 4, ou None pour une étoile vide à colorier."""
    labs = ["communiquer", "travailler en équipe", "être ponctuel(le)", "s'organiser", "être créatif(ve)", "parler plusieurs langues"]
    cx, cy, R = 60, 52, 34
    pts = lambda r: [(cx + r * math.sin(2 * math.pi * k / 6), cy - r * math.cos(2 * math.pi * k / 6)) for k in range(6)]
    g = ""
    for lv in range(1, 5):
        g += '<polygon points="' + " ".join(f"{x:.1f},{y:.1f}" for x, y in pts(R * lv / 4)) + '" fill="none" stroke="#c9d3d3" stroke-width=".5"/>'
    for (x, y) in pts(R):
        g += f'<line x1="{cx}" y1="{cy}" x2="{x:.1f}" y2="{y:.1f}" stroke="#c9d3d3" stroke-width=".5"/>'
    if vals:
        p = [(cx + R * v / 4 * math.sin(2 * math.pi * k / 6), cy - R * v / 4 * math.cos(2 * math.pi * k / 6)) for k, v in enumerate(vals)]
        g += '<polygon points="' + " ".join(f"{x:.1f},{y:.1f}" for x, y in p) + f'" fill="{MC}" fill-opacity=".35" stroke="{MC}" stroke-width="1"/>'
    for k, (x, y) in enumerate(pts(R + 7)):
        anc = "middle" if abs(x - cx) < 3 else ("start" if x > cx else "end")
        g += f'<text x="{x:.1f}" y="{y + 1.5:.1f}" font-size="5" text-anchor="{anc}" font-family="Poppins" fill="#1F2A44">{labs[k]}</text>'
    return f'<svg viewBox="0 0 120 100" width="{w}mm" style="max-width:100%">{g}</svg>'


def build_v3m12(start=1, tstart=1, render=True):
    b = Book("V3 · M12", "Volume 3 · Je réussis à l'école · Module 12 · Vers le monde du travail", MC, start=start)
    E = Ex(b)
    P = {}
    vis = ('<div class="flex" style="justify-content:space-around;align-items:flex-end">' + avatar("bilal", 80, "sourire") + '<div style="font-size:32pt">📄 ✉️</div>' + avatar("fatou", 80, "rire")
           + '<div style="font-size:32pt">🤝 🔧</div>' + avatar("mateo", 80, "pense") + avatar("educ", 80, "sourire") + '</div>')
    opening(b, MC, 12, "Vers le monde du travail", vis, [("🧭", "parler des métiers, des compétences et des formations"), ("📰", "lire une offre d'emploi ou de stage"), ("🗂️", "rédiger mon CV"),
            ("✉️", "écrire une lettre de motivation et un courriel formel"), ("🎩", "utiliser le conditionnel et le registre formel"), ("🤝", "me présenter lors d'un entretien")],
            ["Quel métier aimerais-tu faire plus tard ? Pourquoi ?", "As-tu déjà travaillé (aider la famille, bénévolat, job) ?", "Qu'est-ce qu'un « bon » travail pour toi ?"],
            ["un métier", "un emploi", "un job étudiant", "un stage", "une offre", "un CV", "une lettre de motivation", "un entretien", "une compétence", "une formation", "postuler"], TINT)

    # ---------- Découvrir ----------
    bd = '<div class="grid2" style="gap:3mm">' + "".join([
        bd_case(1, lr("bilal", ["Cet été, je voudrais gagner un peu d'argent. J'ai vu une annonce : la commune cherche des animateurs pour la plaine de vacances !"], "mateo", ["Tu as quel âge ? Tu as le droit de travailler ?"], "rire", "pense")),
        bd_case(2, lr("educ", ["En Belgique, on peut avoir un job étudiant à partir de 15 ans, à certaines conditions. Il faut un contrat écrit."], "bilal", ["J'ai 17 ans : c'est parfait !"], "sourire", "rire")),
        bd_case(3, lr("fatou", ["Ils demandent un CV et une lettre de motivation. Tu sais faire ça ?"], "bilal", ["Euh… Je mettrais : « Salut, je veux le job, merci » ?"], "pense", "surpris")),
        bd_case(4, lr("prof", ["Surtout pas ! Une lettre de motivation est un écrit formel. On vouvoie, on utilise des formules de politesse et souvent le conditionnel."], "bilal", ["Le conditionnel ? « Je voudrais », « je serais heureux » ?"], "sourire", "pense")),
        bd_case(5, lr("amina", ["Moi, plus tard, j'aimerais être infirmière. Je devrais peut-être faire un stage à l'hôpital ?"], "educ", ["Bonne idée ! Et toi, Mateo, la mécanique t'intéresse : tu pourrais te renseigner sur l'alternance."], "sourire", "sourire")),
        bd_case(6, lr("prof", ["Ce mois-ci, chacun préparera un vrai dossier de candidature : un CV, une lettre… et un entretien avec M. Diallo !"], "bilal", ["Un entretien ? J'ai déjà le trac !"], "rire", "surpris")),
    ]) + '</div>'
    e = E("J'écoute et je lis la BD : Bilal cherche un job.", bd, ["ecoute", "lis"], 1, "A",
          script="Lire deux fois en changeant de voix. ", sol="Activité orale.")
    b.page(f'<h2>Découvrir · Bilal cherche un job</h2>{e}', "Découvrir")
    e = E("Je réponds par une phrase complète.", f'<p>1. Quel job Bilal veut-il faire cet été ? {blank("xl")}</p><p>2. À partir de quel âge peut-on avoir un job étudiant en Belgique ? Que faut-il ? {blank("xl")}</p><p>3. Quels documents la commune demande-t-elle ? {blank("xl")}</p><p>4. Pourquoi la lettre de Bilal (case 3) ne convient-elle pas ? {blank("xl")}</p><p>5. Quels projets Amina et Mateo ont-ils ? {blank("xl")}</p>', ["lis", "ecris"], 1, "B",
          sol="1. Animateur à la plaine de vacances de la commune. — 2. À partir de 15 ans, à certaines conditions ; il faut un contrat écrit. — 3. Un CV et une lettre de motivation. — 4. Elle est familière (« Salut », « je veux ») : une lettre de motivation est un écrit formel (vouvoiement, formules de politesse, conditionnel). — 5. Amina veut devenir infirmière (stage à l'hôpital) ; Mateo s'intéresse à la mécanique (alternance).")
    e2 = E("Vrai ou faux ? Je coche et je corrige les phrases fausses.", vf(["Bilal veut travailler pendant l'année scolaire.", "Pour un job étudiant, un accord oral suffit.", "Dans une lettre de motivation, on vouvoie.", "Chaque élève passera un entretien avec M. Diallo."]), ["lis", "coche"], 1, "B",
           sol="Faux (cet été, pendant les vacances) · Faux (il faut un contrat écrit) · Vrai · Vrai")
    e3 = E("Mes expériences. J'écris ce que je sais déjà faire, à l'école, à la maison, dans un club ou dans mon pays (aider, garder, réparer, traduire…).", lines(3), ["ecris"], 2, "C",
           sol="Ex. : Je garde souvent mes petits frères. Je traduis les papiers de l'administration pour mes parents. Au pays, j'aidais mon oncle dans son magasin.")
    e4 = E("Ce qui compte pour moi dans un travail. Je classe de 1 (le plus important) à 6, puis je compare avec mon voisin.", compact(table(["", "Mon classement"], [[x, ""] for x in ["gagner beaucoup d'argent", "aider les autres", "travailler dehors, bouger", "avoir des horaires réguliers", "apprendre tout le temps", "travailler en équipe"]], ["130mm", "52mm"])), ["lis", "ecris", "duo"], 1, "A",
           sol="Classement personnel ; justifier à l'oral : « Pour moi, le plus important, c'est… parce que… »")
    b.page(f'{e}{e2}{e3}{e4}', "Découvrir")
    temo = [("Nadia, 34 ans", "infirmière", "Je travaille de nuit une semaine sur trois. Ce que j'aime ? Le contact avec les patients. Il faut être solide, précise et savoir rester calme. J'ai fait trois ans d'études (bachelier) après le secondaire."),
            ("Marc, 52 ans", "mécanicien", "J'ai appris le métier en alternance : deux jours à l'école, trois jours au garage. Aujourd'hui, les voitures sont pleines d'électronique : je me forme encore chaque année."),
            ("Leïla, 27 ans", "boulangère", "Je commence à 4 h du matin ! C'est dur, mais j'adore voir les clients repartir avec du pain chaud. J'ai suivi une formation en apprentissage, puis j'ai ouvert ma boulangerie."),
            ("Samuel, 41 ans", "comptable", "Je travaille dans un bureau, avec des chiffres, mais aussi avec des gens : je conseille les entreprises. Il faut être rigoureux et aimer les mathématiques.")]
    e = E("J'écoute et je lis quatre témoignages (personnes fictives). Je complète le tableau.", '<div class="grid2" style="gap:2mm">' + "".join(f'<div class="card" style="background:#fff;padding:2mm 3mm"><b style="color:{MC}">{n}</b> · <i>{m}</i><p class="sm" style="margin:1mm 0 0">« {t} »</p></div>' for n, m, t in temo) + '</div>' +
          tall(compact(table(["", "Lieu de travail", "Une qualité nécessaire", "Sa formation"], [["Nadia", "", "", ""], ["Marc", "", "", ""], ["Leïla", "", "", ""], ["Samuel", "", "", ""]], ["24mm", "50mm", "54mm", "54mm"])), 12), ["ecoute", "lis", "ecris"], 2, "B",
          script="Une voix par témoignage. Avant : « Qui travaille la nuit ? très tôt ? » Après : « Quel métier te plairait ? »",
          sol="Nadia : hôpital ; calme, précise, solide ; bachelier (3 ans) · Marc : garage ; se former, aimer l'électronique ; alternance · Leïla : sa boulangerie ; courage, se lever tôt ; apprentissage · Samuel : bureau ; rigoureux, aimer les maths ; (études de comptabilité, non précisées)")
    e2 = E("Et toi ? Quel métier de ces quatre témoignages te plairait le plus, et pourquoi ? Lequel ne te plairait pas ? (3 phrases, avec « J'aimerais… parce que… »)", lines(5), ["ecris"], 2, "C",
           sol="Ex. : J'aimerais être boulanger parce que j'aime faire plaisir aux gens. Par contre, je ne voudrais pas être comptable : je n'aime pas rester assis toute la journée.")
    b.page(f'<h2>Découvrir · Des métiers et des gens</h2>{e}{e2}', "Découvrir")

    # ---------- Lexique ----------
    e = E("Les mots du travail. Je lis l'encadré.", '<div class="grid2">' + "".join(f'<div class="card" style="background:#fff"><b>{t}</b><p class="sm" style="margin:1mm 0 0">{d}</p></div>' for t, d in [
        ("💼 Travailler", "un <b>métier</b> (ce qu'on sait faire : boulanger) · un <b>emploi</b>, un <b>poste</b> (une place de travail) · un <b>job</b> (familier : un petit travail) · un <b>employeur</b> / un <b>travailleur</b>, un <b>employé</b> · un <b>salaire</b> (brut / net)"),
        ("🔎 Chercher", "une <b>offre d'emploi</b>, une <b>annonce</b> · <b>postuler</b>, <b>poser sa candidature</b> · un <b>candidat</b>, une <b>candidate</b> · un <b>CV</b> (curriculum vitae) · une <b>lettre de motivation</b> · un <b>entretien</b> (d'embauche) · <b>embaucher</b>, <b>engager</b>"),
        ("🎓 Se former", "une <b>formation</b> · un <b>diplôme</b>, un <b>certificat</b> · un <b>stage</b> (on apprend en entreprise) · l'<b>alternance</b> (école + entreprise) · un <b>apprenti</b> · se <b>reconvertir</b>"),
        ("⭐ Les compétences", "les <b>savoirs</b> (ce que je connais) · les <b>savoir-faire</b> (ce que je sais faire) · le <b>savoir-être</b> (mes qualités : ponctuel, poli, motivé) · une <b>expérience</b> · un <b>atout</b>")]) + '</div>', ["lis"], 1, "B", sol="Lecture de l'encadré.")
    e2 = E("Métier, emploi ou job ? Je complète.", '<div class="card" style="line-height:2">1. Mon père est électricien : c\'est un beau ______________ . 2. Cet été, j\'ai trouvé un petit ______________ dans un supermarché. 3. Le chômage baisse : il y a plus d\'______________ dans la région. 4. Elle a obtenu un ______________ de secrétaire à la commune.</div>', ["lis", "complete"], 1, "C",
           sol="1. métier — 2. job — 3. emplois (offres d'emploi) — 4. poste (emploi)")
    e3 = E("Savoir, savoir-faire ou savoir-être ? Je classe : être ponctuel · parler néerlandais · utiliser un tableur · être poli · connaître le code de la route · réparer un vélo · être patient · connaître les règles d'hygiène.", tall(table(["📘 Savoirs", "🛠️ Savoir-faire", "🙂 Savoir-être"], [["", "", ""]], ["60mm", "61mm", "61mm"]), 15), ["lis", "ecris"], 2, "C",
           sol="Savoirs : connaître le code de la route, connaître les règles d'hygiène · Savoir-faire : parler néerlandais, utiliser un tableur, réparer un vélo · Savoir-être : être ponctuel, être poli, être patient")
    e4 = E("Les familles de mots. Je complète.", compact(table(["Verbe", "Nom de l'action", "Nom de la personne"], [["travailler", "le travail", ""], ["former", "", "le formateur"], ["employer", "l'emploi", ""], ["candidater / postuler", "", ""], ["recruter", "", ""]], ["60mm", "61mm", "61mm"])).replace("<td></td>", '<td style="height:7mm"></td>'), ["complete"], 2, "C",
           sol="le travailleur, la travailleuse · la formation · l'employeur / l'employé(e) · la candidature, le candidat / la candidate · le recrutement, le recruteur / la recruteuse")
    b.page(f'<h2>Les mots du travail</h2>{e}{e2}{e3}{e4}', "Lexique")
    e = E("Les secteurs et les métiers. Je relie le métier et son secteur.", relie(["une aide-soignante", "un maçon", "une cuisinière", "un informaticien", "une vendeuse", "un chauffeur de bus"], ["l'informatique", "la vente, le commerce", "les transports", "la construction", "la santé", "l'horeca (hôtels, restaurants, cafés)"]), ["lis", "relie"], 1, "B",
          sol="aide-soignante → santé · maçon → construction · cuisinière → horeca · informaticien → informatique · vendeuse → vente · chauffeur de bus → transports")
    e2 = E("Masculin, féminin. J'écris le métier au féminin.", compact(table(["Masculin", "Féminin", "Masculin", "Féminin"], [["un infirmier", "", "un coiffeur", ""], ["un vendeur", "", "un directeur", ""], ["un mécanicien", "", "un médecin", ""], ["un boulanger", "", "un chauffeur", ""]], ["44mm", "47mm", "44mm", "47mm"])).replace("<td></td>", '<td style="height:6.5mm"></td>'), ["ecris"], 2, "C",
           sol="infirmière · coiffeuse · vendeuse · directrice · mécanicienne · médecin (une médecin) · boulangère · chauffeuse (une chauffeur, en Belgique aussi)")
    e3 = E("Les qualités. Je complète avec un adjectif : ponctuel · rigoureux · patient · dynamique · sociable · autonome.", '<div class="card" style="line-height:2">1. Il arrive toujours à l\'heure : il est ______________ . 2. Elle travaille seule, sans aide : elle est ______________ . 3. Il ne s\'énerve jamais avec les enfants : il est ______________ . 4. Elle vérifie tout, sans erreur : elle est ______________ . 5. Il aime parler avec les gens : il est ______________ . 6. Elle a beaucoup d\'énergie : elle est ______________ .</div>', ["complete"], 1, "C",
           sol="1. ponctuel — 2. autonome — 3. patient — 4. rigoureuse — 5. sociable — 6. dynamique")
    e4 = E("Défi ! Je choisis un métier et j'écris 3 phrases : ce que fait la personne, où elle travaille, deux qualités nécessaires.", lines(3), ["ecris"], 3, "C",
           sol="Ex. : Une puéricultrice s'occupe des bébés et des jeunes enfants. Elle travaille dans une crèche ou à l'hôpital. Elle doit être patiente et attentive.")
    b.page(f'<h2>Les métiers et les qualités</h2>{e}{e2}{e3}{e4}', "Lexique")

    # ---------- Leçon 1 : le conditionnel présent (formation) ----------
    l1 = lecon("Le conditionnel présent : la formation", '<p class="sm" style="margin-bottom:1.5mm">Conditionnel = <b>radical du futur</b> + <b>terminaisons de l\'imparfait</b> : <b>-ais, -ais, -ait, -ions, -iez, -aient</b>.</p>' +
        compact(table(["", "aimer", "finir", "prendre", "être", "avoir"], [["je / j'", "aimer<b>ais</b>", "finir<b>ais</b>", "prendr<b>ais</b>", "ser<b>ais</b>", "aur<b>ais</b>"], ["tu", "aimer<b>ais</b>", "finir<b>ais</b>", "prendr<b>ais</b>", "ser<b>ais</b>", "aur<b>ais</b>"], ["il / elle / on", "aimer<b>ait</b>", "finir<b>ait</b>", "prendr<b>ait</b>", "ser<b>ait</b>", "aur<b>ait</b>"],
                                                  ["nous", "aimer<b>ions</b>", "finir<b>ions</b>", "prendr<b>ions</b>", "ser<b>ions</b>", "aur<b>ions</b>"], ["vous", "aimer<b>iez</b>", "finir<b>iez</b>", "prendr<b>iez</b>", "ser<b>iez</b>", "aur<b>iez</b>"], ["ils / elles", "aimer<b>aient</b>", "finir<b>aient</b>", "prendr<b>aient</b>", "ser<b>aient</b>", "aur<b>aient</b>"]], ["32mm", "30mm", "30mm", "30mm", "30mm", "30mm"])) +
        '<p class="sm" style="margin:1.5mm 0 1mm"><b>Radicaux irréguliers</b> (les mêmes qu\'au futur) : aller → <b>ir</b>- · faire → <b>fer</b>- · pouvoir → <b>pourr</b>- · vouloir → <b>voudr</b>- · devoir → <b>devr</b>- · savoir → <b>saur</b>- · venir → <b>viendr</b>- · voir → <b>verr</b>- · falloir → il <b>faudr</b>ait · envoyer → <b>enverr</b>-</p>'
        '<div class="astuce" style="margin:1mm 0 0">⚠️ <b>Futur ou conditionnel ?</b> je parler<b>ai</b> (futur, [e]) ≠ je parler<b>ais</b> (conditionnel, [ɛ]). Astuce : je remplace par « nous » → nous parlerons (futur) / nous parlerions (conditionnel).</div>')
    e = E("Je conjugue au conditionnel présent.", '<div class="card" style="line-height:2">1. Je (vouloir) ______________ un rendez-vous. 2. Tu (pouvoir) ______________ m\'aider ? 3. Elle (aimer) ______________ travailler dehors. 4. Nous (être) ______________ heureux de vous rencontrer. 5. Vous (avoir) ______________ un moment ? 6. Ils (devoir) ______________ envoyer leur CV. 7. On (aller) ______________ à la plaine. 8. Il (falloir) ______________ arriver à l\'heure.</div>', ["complete"], 1, "C",
          sol="1. voudrais — 2. pourrais — 3. aimerait — 4. serions — 5. auriez — 6. devraient — 7. irait — 8. faudrait")
    e2 = E("Je retrouve l'infinitif de chaque verbe au conditionnel.", '<div class="card" style="line-height:2">1. nous ferions → ______________ 2. elles iraient → ______________ 3. tu saurais → ______________ 4. vous viendriez → ______________ 5. il enverrait → ______________ 6. je verrais → ______________</div>', ["lis", "complete"], 2, "C",
           sol="1. faire — 2. aller — 3. savoir — 4. venir — 5. envoyer — 6. voir")
    b.page(f'{l1}{e}{e2}', "Leçon 1")
    e = E("Futur ou conditionnel ? J'entoure la bonne forme.", '<div class="card" style="line-height:2">1. Demain, je (<b>commencerai</b> / <b>commencerais</b>) mon stage à 8 h. 2. Si j\'avais le temps, je (<b>ferai</b> / <b>ferais</b>) du bénévolat. 3. Je (<b>voudrai</b> / <b>voudrais</b>) parler au responsable, s\'il vous plaît. 4. L\'année prochaine, j\'(<b>aurai</b> / <b>aurais</b>) 16 ans. 5. À ta place, je (<b>relirai</b> / <b>relirais</b>) ma lettre.</div>', ["lis", "entoure"], 2, "C",
          sol="1. commencerai (action certaine, demain) — 2. ferais (hypothèse) — 3. voudrais (politesse) — 4. aurai (fait certain) — 5. relirais (conseil)")
    e2 = E("J'écoute 8 phrases. Futur [e] ou conditionnel [ɛ] ? Je coche.", checks(8, ["futur", "conditionnel"]), ["ecoute", "coche"], 2, "A",
           script="1. Je travaillerais le samedi. 2. Je serai là. 3. J'aimerais venir. 4. J'enverrai mon CV. 5. Je pourrais commencer. 6. Je ferai un stage. 7. Je voudrais un renseignement. 8. J'irai en bus.",
           sol="futur : 2, 4, 6, 8 · conditionnel : 1, 3, 5, 7")
    e3 = E("Je complète le tableau des radicaux.", compact(table(["Infinitif", "Futur (je)", "Conditionnel (je)", "Conditionnel (nous)"], [["faire", "je ferai", "", ""], ["venir", "", "", ""], ["savoir", "", "", ""], ["envoyer", "", "", ""], ["voir", "", "", ""]], ["40mm", "46mm", "48mm", "48mm"])).replace("<td></td>", '<td style="height:6.5mm"></td>'), ["complete"], 2, "C",
           sol="faire : je ferais, nous ferions · venir : je viendrai, je viendrais, nous viendrions · savoir : je saurai, je saurais, nous saurions · envoyer : j'enverrai, j'enverrais, nous enverrions · voir : je verrai, je verrais, nous verrions")
    e4 = E("Je mets les verbes au conditionnel pour rendre le message de Bilal plus poli.", f'<div class="card" style="font-family:\'Comic Sans MS\',cursive;background:#fff">« Bonjour, je <u>veux</u> des informations sur la plaine. <u>Pouvez</u>-vous m\'envoyer le formulaire ? J\'<u>aime</u> aussi savoir si vous <u>avez</u> encore des places en août. »</div>{lines(2)}', ["lis", "ecris"], 2, "C",
           sol="Bonjour, je voudrais des informations sur la plaine. Pourriez-vous m'envoyer le formulaire ? J'aimerais aussi savoir si vous auriez encore des places en août.")
    e5 = E("Défi ! Si j'étais directeur ou directrice de mon école pendant une journée… J'écris 4 phrases au conditionnel.", lines(3), ["ecris"], 3, "C",
           sol="Ex. : Je supprimerais les cours le vendredi après-midi. Les élèves pourraient choisir leur musique à la récréation. Nous mangerions dehors quand il fait beau. Il y aurait un cours de cuisine.")
    b.page(f'{e}{e2}{e3}{e4}{e5}', "S'entraîner")

    # ---------- Leçon 2 : les emplois du conditionnel ----------
    l2 = lecon("Les emplois du conditionnel", compact(table(["J'utilise le conditionnel pour…", "Exemples"], [
        ["① <b>être poli</b> (demander)", "Je <b>voudrais</b> un renseignement. · <b>Pourriez</b>-vous me rappeler ? · <b>Auriez</b>-vous un moment ?"],
        ["② exprimer un <b>souhait</b>, un rêve", "J'<b>aimerais</b> devenir infirmière. · Je <b>souhaiterais</b> faire un stage."],
        ["③ donner un <b>conseil</b>", "Tu <b>devrais</b> relire ta lettre. · À ta place, je <b>mettrais</b> une photo. · Il <b>faudrait</b> arriver en avance."],
        ["④ faire une <b>hypothèse</b> (imaginer)", "<b>Si</b> j'<b>avais</b> un job, j'<b>économiserais</b> pour mon permis."],
        ["⑤ donner une information <b>non confirmée</b> (module 8)", "Selon la presse, l'usine <b>engagerait</b> 50 personnes."]], ["66mm", "116mm"])) +
        '<div class="astuce" style="margin:2mm 0 0">🔑 <b>L\'hypothèse :</b> <b>si + imparfait</b> → <b>conditionnel présent</b>. « Si je <b>parlais</b> néerlandais, je <b>trouverais</b> plus facilement un travail. » ⚠️ Jamais de conditionnel après « si » : <s>si j\'aurais</s> → si j\'avais.</div>')
    e = E("Quel emploi du conditionnel ? J'écris le numéro de la leçon (① à ⑤).", '<div class="card" style="line-height:1.9">___ Tu devrais te renseigner au Forem. &nbsp; ___ Pourriez-vous me dire où se trouve l\'accueil ? &nbsp; ___ Si j\'étais riche, je voyagerais. &nbsp; ___ J\'aimerais tant travailler avec des animaux ! &nbsp; ___ D\'après la radio, le magasin fermerait en juin. &nbsp; ___ À ta place, j\'enverrais la lettre aujourd\'hui.</div>', ["lis", "ecris"], 1, "B",
          sol="③ · ① · ④ · ② · ⑤ · ③")
    e2 = E("Si + imparfait → conditionnel. Je conjugue.", '<div class="card" style="line-height:1.75">1. Si je (avoir) ______________ 18 ans, je (passer) ______________ mon permis. 2. Si tu (venir) ______________ plus tôt, tu (voir) ______________ le directeur. 3. Si nous (parler) ______________ néerlandais, nous (pouvoir) ______________ travailler à Bruxelles. 4. S\'il (faire) ______________ beau, les enfants (jouer) ______________ dehors.</div>', ["complete"], 2, "C",
           sol="1. avais, passerais — 2. venais, verrais — 3. parlions, pourrions — 4. faisait, joueraient")
    e3 = E("J'imagine. Je termine les phrases avec un verbe au conditionnel.", '<div class="card" style="line-height:2">1. Si je gagnais au Lotto, ______________________________ . 2. Si j\'étais ministre de l\'Éducation, ______________________________ .</div>', ["complete"], 2, "C",
           sol="Ex. : 1. j'offrirais une maison à mes parents. — 2. je donnerais une tablette à chaque élève.")
    b.page(f'{l2}{e}{e2}{e3}', "Leçon 2")
    e = E("Je donne des conseils à Bilal avec : tu devrais · à ta place, je… · il faudrait · tu pourrais.", '<p>1. Il a écrit sa lettre au crayon. → {0}</p><p>2. Il ne connaît pas l\'adresse de la plaine. → {0}</p><p>3. Il a peur de l\'entretien. → {0}</p><p>4. Son adresse électronique est « bilal-le-boss@… ». → {0}</p>'.format(blank("xl")), ["ecris"], 2, "C",
          sol="Ex. : 1. Tu devrais l'écrire à l'ordinateur. — 2. Tu pourrais la chercher sur le site de la commune. — 3. À ta place, je m'entraînerais avec un ami. — 4. Il faudrait créer une adresse sérieuse (prénom.nom@…).")
    e2 = E("Je rends ces demandes polies (conditionnel + vous).", '<p>1. Donne-moi le formulaire. → {0}</p><p>2. Je veux parler au patron. → {0}</p><p>3. Vous avez un stylo ? → {0}</p>'.format(blank("xl")), ["ecris"], 1, "C",
           sol="1. Pourriez-vous me donner le formulaire, s'il vous plaît ? — 2. Je voudrais parler au responsable, s'il vous plaît. — 3. Auriez-vous un stylo, s'il vous plaît ?")
    e3 = E("J'écoute la conversation téléphonique et je réponds.", f'<p>1. Pourquoi Fatou téléphone-t-elle ? {blank("xl")}</p><p>2. Relève deux phrases au conditionnel. Quel est leur emploi ? {blank("xl")}</p><p>3. Que doit faire Fatou ? Avant quelle date ? {blank("xl")}</p>', ["ecoute", "ecris"], 2, "A",
           script="— Pharmacie du Pont, bonjour. — Bonjour Madame, je suis Fatou Camara. Je voudrais savoir si vous accepteriez une stagiaire aux vacances de Pâques. J'aimerais découvrir le métier d'assistante en pharmacie. — Vous pourriez nous envoyer un CV et une lettre, par courriel, avant le 1er mars ? — Bien sûr. Merci beaucoup, Madame !",
           sol="1. Pour demander un stage pendant les vacances de Pâques (découvrir le métier d'assistante en pharmacie). — 2. « Je voudrais savoir », « vous accepteriez » (politesse), « J'aimerais découvrir » (souhait), « Vous pourriez nous envoyer » (demande polie). — 3. Envoyer un CV et une lettre par courriel avant le 1er mars.")
    e4 = E("Défi ! Mon métier de rêve. J'écris 5 phrases : quel métier j'aimerais faire, pourquoi, ce que je devrais faire pour y arriver, et ce que je ferais si je n'y arrivais pas.", lines(5), ["ecris"], 3, "C",
           sol="Ex. : J'aimerais devenir pilote d'avion, car j'adore voyager. Je devrais être bon en maths et en anglais. Il faudrait aussi faire une formation longue et coûteuse. Si je n'y arrivais pas, je travaillerais dans un aéroport.")
    b.page(f'{e}{e2}{e3}{e4}', "S'entraîner")

    # ---------- Leçon 3 : le registre formel ----------
    l3 = lecon("Les registres de langue et le registre formel", thermo() +
        compact(table(["Familier / courant", "Formel (lettre, entretien, courriel professionnel)"], [
            ["Salut ! / Bonjour Monsieur,", "Madame, Monsieur, (je ne connais pas le nom) · Madame Dumont, (je le connais)"],
            ["Tu peux… ? / Je veux…", "Pourriez-vous… ? · Je souhaiterais… · Je voudrais…"],
            ["un boulot, un job · bosser", "un emploi, un poste · travailler"],
            ["Je vous envoie mon CV.", "Je vous prie de trouver ci-joint mon curriculum vitae."],
            ["Merci, à plus !", "Je vous remercie de votre attention. · Veuillez agréer, Madame, Monsieur, mes salutations distinguées."]], ["68mm", "114mm"])) +
        '<div class="astuce" style="margin:2mm 0 0">🎩 <b>Dans le registre formel :</b> je <b>vouvoie</b> · j\'écris des phrases <b>complètes</b> (avec « ne… pas ») · je n\'utilise <b>ni abréviations ni émoticônes</b> · je choisis des mots <b>précis</b> · j\'utilise le <b>conditionnel</b> de politesse. 🇧🇪 « Je vous prie d\'agréer… » se dit aussi en Belgique ; « Bien à vous » est une formule finale très courante en Belgique dans les courriels.</div>')
    e = E("Familier (F), courant (C) ou soutenu (S) ? J'écris la lettre.", '<div class="card" style="line-height:1.9">___ « T\'as pas un boulot pour moi ? » &nbsp; ___ « Je vous saurais gré de me tenir informé. » &nbsp; ___ « Avez-vous un emploi à me proposer ? » &nbsp; ___ « Ce job est trop cool ! » &nbsp; ___ « Je cherche un travail pour l\'été. » &nbsp; ___ « Veuillez agréer mes salutations distinguées. »</div>', ["lis", "ecris"], 1, "B",
          sol="F · S · C · F · C · S")
    e2 = E("Le mot précis. Je remplace « faire » par un verbe plus précis : rédiger · passer · suivre · effectuer.", '<div class="card" style="line-height:2">1. faire un CV → ______________ un CV 2. faire un entretien → ______________ un entretien 3. faire une formation → ______________ une formation 4. faire un stage → ______________ un stage</div>', ["complete"], 2, "C",
           sol="1. rédiger — 2. passer — 3. suivre — 4. effectuer")
    b.page(f'{l3}{e}{e2}', "Leçon 3")
    e = E("Je traduis en registre formel.", '<p>1. Salut, je veux bosser chez vous cet été. → {0}</p><p>2. T\'as reçu mon CV ? → {0}</p><p>3. Je peux venir lundi ? → {0}</p><p>4. Merci, à plus ! → {0}</p>'.format(blank("xl")), ["ecris"], 2, "C",
          sol="1. Madame, Monsieur, je souhaiterais travailler dans votre entreprise cet été. — 2. Avez-vous bien reçu mon curriculum vitae ? — 3. Pourrais-je venir lundi ? / Serait-il possible de venir lundi ? — 4. Je vous remercie. Bien à vous. (ou une formule de politesse complète)")
    e2 = E("Je relie le mot familier et le mot formel.", relie(["un boulot", "bosser", "le patron", "le fric", "se planter", "un truc"], ["l'argent, le salaire", "se tromper, échouer", "un emploi", "travailler", "une chose, un objet", "le responsable, le directeur"]), ["lis", "relie"], 1, "B",
           sol="boulot → emploi · bosser → travailler · patron → responsable · fric → argent · se planter → se tromper · truc → chose")
    e3 = E("Le courriel de Mateo est trop familier. Je le réécris en registre formel (6 lignes).", f'<div class="card" style="font-family:\'Comic Sans MS\',cursive;background:#fff;font-size:10pt">Objet : stage<br>Salut ! Moi c Mateo, j\'ai 16 ans et je kiffe les voitures 😍. Vous prenez des stagiaires ? Je peux venir quand vous voulez. Répondez vite svp ! Bisous, Mateo</div>{lines(6)}', ["lis", "ecris"], 2, "C",
           sol="Objet : demande de stage en mécanique automobile. Madame, Monsieur, Je m'appelle Mateo Ramírez, j'ai 16 ans et je suis élève à l'Athénée de Hautrive. Je suis passionné par la mécanique automobile. Accepteriez-vous un stagiaire pendant les vacances de Pâques ? Je suis disponible du 29 mars au 9 avril. Je vous remercie de votre réponse. Bien à vous, Mateo Ramírez")
    e4 = E("À l'oral : tu ou vous ? Je coche, puis je joue une des scènes avec mon voisin.", compact(table(["", "tu", "vous"], [[x, '<span class="chk"></span>', '<span class="chk"></span>'] for x in ["Je parle à la responsable du magasin pendant l'entretien.", "Je parle à un autre animateur de mon âge, à la plaine.", "Je téléphone à la secrétaire de la commune.", "Je parle à un enfant de 7 ans, à la plaine."]], ["140mm", "21mm", "21mm"])), ["lis", "coche", "duo"], 1, "A",
           sol="vous · tu · vous · tu (on tutoie souvent les enfants et les collègues de son âge ; en cas de doute, on vouvoie)")
    b.page(f'{e}{e2}{e3}{e4}', "S'entraîner")

    # ---------- Leçon 4 : lire une offre, faire son CV ----------
    offre = f'''<div class="doc" style="transform:none;background:#fff;border:1.5px solid #9aa1b1;padding:2.5mm 4mm;font-size:9pt;line-height:1.35">
<div class="flex" style="justify-content:space-between"><b style="font-size:11.5pt;color:{MC}">Le magasin FraisMarché de Hautrive engage</b><span class="xs muted">(offre fictive)</span></div>
<b>Étudiant(e) jobiste · réassort et caisse · week-ends et vacances</b>
<div class="grid2" style="gap:3mm;margin-top:1mm"><div><b>① Missions :</b> remplir les rayons, accueillir et renseigner les clients, tenir la caisse (après formation).<br><b>② Profil :</b> 16 ans minimum · ponctuel(le), souriant(e), aimant le contact · la connaissance du néerlandais est un <b>atout</b>.</div>
<div><b>③ Conditions :</b> contrat d'occupation d'étudiant · samedis de 9 h à 17 h + 3 semaines en juillet · salaire selon le barème légal.<br><b>④ Pour postuler :</b> CV + lettre de motivation à jobs@fraismarche-exemple.be avant le 30 avril (réf. JOB-27).</div></div></div>'''
    l4 = lecon("Lire une offre d'emploi et rédiger un CV", '<p class="sm" style="margin-bottom:1mm">Une offre d\'emploi contient presque toujours : ① les <b>missions</b> (ce qu\'on fera) · ② le <b>profil</b> (ce qu\'on demande : âge, diplôme, qualités ; un « atout » = un plus, pas obligatoire) · ③ les <b>conditions</b> (contrat, horaire, salaire) · ④ la <b>marche à suivre</b> pour postuler (documents, adresse, date limite, référence).</p>' + offre +
        '<div class="astuce" style="margin:2mm 0 0">🗂️ <b>Le CV</b> tient sur <b>une page</b> : mes coordonnées · un court <b>profil</b> · ma <b>formation</b> (de la plus récente à la plus ancienne) · mes <b>expériences</b> (jobs, stages, bénévolat, aide familiale) · mes <b>langues</b> (avec le niveau : A2, B1…) · mes <b>compétences</b> et <b>atouts</b> · mes <b>loisirs</b>. Une adresse électronique sérieuse, aucune faute, une mise en page claire. La photo n\'est pas obligatoire en Belgique.</div>')
    e = E("Je relis l'offre de FraisMarché. Je réponds.", f'<p class="sm">1. Quelles seront les missions du jobiste ? {blank("xl")}</p><p class="sm">2. Yonas a 15 ans. Peut-il postuler ? Pourquoi ? {blank("xl")}</p><p class="sm">3. Bilal ne parle pas néerlandais. Peut-il quand même postuler ? Justifie avec un mot de l\'offre. {blank("xl")}</p><p class="sm">4. Quels documents faut-il envoyer ? À qui ? Quand ? Que faut-il indiquer dans l\'objet ? {blank("xl")}</p>', ["lis", "ecris"], 2, "B",
          sol="1. Remplir les rayons, accueillir et renseigner les clients, tenir la caisse. — 2. Non : il faut avoir 16 ans minimum. — 3. Oui : le néerlandais est seulement un « atout » (un plus, pas une obligation). — 4. Un CV et une lettre de motivation, par courriel à jobs@fraismarche-exemple.be, avant le 30 avril ; indiquer la référence JOB-27.")
    e2 = E("Je remets les rubriques dans l'ordre de l'offre : où le candidat trouve-t-il… ? J'écris ①, ②, ③ ou ④.", '<div class="card" style="line-height:1.9">___ « Envoyez votre candidature avant le 30 avril. » ___ « Vous accueillerez les clients. » ___ « Vous êtes ponctuel et souriant. » ___ « Contrat d\'occupation d\'étudiant. »</div>', ["lis", "ecris"], 1, "B",
           sol="④ · ① · ② · ③")
    e3 = E("Défi ! J'écris une petite offre d'emploi (5 lignes) pour un job étudiant de mon choix, avec les quatre parties : missions, profil, conditions, candidature.", lines(4), ["ecris"], 3, "C",
           sol="Offre avec les quatre parties ; vocabulaire de l'offre (vous accueillerez…, profil : …, atout, contrat, envoyer CV et lettre avant le…).")
    b.page(f'{l4}{e}{e2}{e3}', "Leçon 4")
    P["cv"] = b.n + 1
    e = E("J'observe le CV de Bilal (personnage fictif). Je réponds.", cv(True, 9.2) + f'<p class="sm mt2">1. Dans quelles rubriques trouve-t-on ses expériences de bénévolat ? Pourquoi est-ce utile de les noter ? {blank("xl")}</p><p class="sm">2. Dans quel ordre sont présentées les formations ? {blank("l")}</p><p class="sm">3. Relève deux savoir-faire et deux savoir-être. {blank("xl")}</p><p class="sm">4. Pourquoi Bilal a-t-il choisi l\'adresse « bilal.cv@… » et pas « bilal-le-boss@… » ? {blank("xl")}</p>', ["lis", "ecris"], 2, "B",
          sol="1. Dans « Expériences » : même sans job payé, le bénévolat montre des compétences (animer, organiser, être fiable). — 2. De la plus récente à la plus ancienne (ordre antichronologique). — 3. Savoir-faire : animer un groupe d'enfants, organiser un jeu, premiers secours ; savoir-être : ponctuel, patient, souriant. — 4. Une adresse sérieuse donne une image professionnelle.")
    e2 = E("Le CV : vrai ou faux ? Je coche.", vf(["Un CV d'élève peut tenir sur une seule page.", "On commence par la formation la plus ancienne.", "On peut noter le bénévolat et l'aide à la famille.", "La photo est obligatoire en Belgique.", "On indique son niveau dans chaque langue."]), ["lis", "coche"], 1, "B",
          sol="Vrai · Faux (la plus récente d'abord) · Vrai · Faux (facultative) · Vrai")
    b.page(f'{e}{e2}', "S'entraîner")
    e = E("Mon étoile des compétences. Je colorie de 0 (pas du tout) à 4 (très bien) pour chaque branche, puis j'écris une phrase sur ma meilleure compétence.", '<div class="grid2" style="grid-template-columns:1fr 1.2fr;gap:3mm;align-items:center"><div class="c">' + etoile(None, 66) + '</div><div><p class="xs muted" style="margin:0 0 1mm">Exemple : l\'étoile de Bilal</p>' + etoile([4, 3, 4, 2, 3, 3], 52) + f'</div></div><p>Ma meilleure compétence : {blank("xl")}</p>', ["colorie", "ecris"], 1, "C",
           sol="Production personnelle ; inviter l'élève à donner un exemple concret (« Je suis ponctuel : je ne suis jamais arrivé en retard cette année. »).")
    e3 = E("Je transforme mes expériences en compétences pour mon CV.", tall(compact(table(["Ce que j'ai fait", "La compétence pour le CV"], [["Je garde mes petits frères.", "s'occuper d'enfants, être responsable"], ["Je traduis les courriers pour mes parents.", ""], ["J'aide mon oncle au marché le dimanche.", ""], ["Je suis capitaine de mon équipe de basket.", ""]], ["90mm", "92mm"])), 8), ["lis", "ecris"], 2, "C",
           sol="Ex. : traduire de ma langue vers le français, rédiger, aider à des démarches administratives · servir les clients, rendre la monnaie, travailler tôt · motiver une équipe, travailler en équipe, prendre des responsabilités")
    e4 = E("Défi ! J'écris le « profil » de mon CV en 2 phrases (qui je suis, ce que je cherche, une qualité).", lines(2), ["ecris"], 3, "C",
           sol="Ex. : Élève de 16 ans, sérieuse et souriante, je cherche un job étudiant dans la vente pour les vacances d'été. J'aime le contact avec les clients et je parle quatre langues.")
    b.page(f'{e}{e3}{e4}', "S'entraîner")

    # ---------- Leçon 5 (FLSco) : les écrits professionnels ----------
    P["lettre"] = b.n + 1
    l5 = lecon("Les écrits professionnels : la lettre de motivation", '<p class="sm" style="margin-bottom:1.5mm">La lettre de motivation accompagne le CV. Elle répond à trois questions : <b>pourquoi j\'écris</b> (le poste, où j\'ai vu l\'offre) · <b>ce que j\'apporte</b> (mes expériences, mes qualités, avec des exemples) · <b>ce que j\'attends</b> (ce que le poste m\'apporterait, un entretien). Elle tient sur une page.</p>' + lettre(True))
    b.page(f'<span class="tag-doc">🎒 FRANÇAIS DE L\'ÉCOLE</span>{l5}', "Consignes & école")
    e = E(f"J'analyse la lettre de Bilal (p. {P['lettre']}). Je réponds.", f'<p class="sm">1. Relève les trois verbes au conditionnel du corps de la lettre (⑥ et ⑦). Quel est leur emploi ? {blank("xl")}</p><p class="sm">2. Quel exemple concret Bilal donne-t-il pour montrer qu\'il sait animer un groupe ? {blank("xl")}</p><p class="sm">3. Quel atout « original » Bilal met-il en avant ? {blank("l")}</p><p class="sm">4. Que signifie « Annexe : curriculum vitae » ? {blank("l")}</p>', ["lis", "ecris"], 2, "B",
          sol="1. souhaiterais (politesse / souhait), pourrait (hypothèse prudente), permettrait (hypothèse), aimerais (souhait), serais (politesse) — accepter trois d'entre eux. — 2. Il aide l'entraîneur des U8 du RFC Hautrive depuis un an. — 3. Il parle dari et pachto (utile avec certaines familles). — 4. Le CV est joint à la lettre.")
    e2 = E("Les consignes des écrits scolaires et professionnels. Je relie la consigne et ce qu'il faut faire.", relie(["Rédigez une lettre formelle.", "Argumentez votre candidature.", "Respectez la mise en page.", "Joignez les documents.", "Indiquez la référence."], ["Je mets les pièces demandées avec ma lettre.", "J'écris le code de l'offre dans l'objet.", "J'écris en vouvoyant, avec les formules de politesse.", "Je place l'expéditeur, le destinataire, la date, l'objet…", "Je donne des raisons et des exemples qui montrent que je conviens."]), ["lis", "relie"], 1, "B",
           sol="lettre formelle → vouvoiement et formules · argumentez → raisons et exemples · mise en page → expéditeur, destinataire… · joignez → les pièces · référence → code dans l'objet")
    e3 = E("Le courriel formel. Je remets dans l'ordre le courriel de Fatou à la pharmacie (1 à 6).", '<div class="card sm" style="line-height:1.8">___ Je vous remercie de votre attention et reste à votre disposition pour un entretien.<br>___ <b>Objet :</b> demande de stage d\'observation · vacances de Pâques<br>___ Bien à vous,<br>___ Madame,<br>___ Suite à notre conversation téléphonique de ce matin, je vous envoie ma candidature pour un stage d\'observation du 29 mars au 2 avril. Vous trouverez en pièces jointes mon CV et ma lettre de motivation.<br>___ Fatou Camara · 0485 98 76 54</div>', ["lis", "numerote"], 2, "C",
           sol="Objet (1) · Madame, (2) · Suite à notre conversation… (3) · Je vous remercie… (4) · Bien à vous, (5) · Fatou Camara (6)")
    e4 = E("Défi ! J'écris le paragraphe « ce que j'apporte » (⑥) d'une lettre de motivation pour l'offre de FraisMarché, avec deux exemples concrets.", lines(4), ["ecris"], 3, "C",
           sol="Ex. : Chaque dimanche, j'aide mon oncle à son étal au marché de Hautrive : je sers les clients, je rends la monnaie et je range la marchandise. Je suis ponctuelle et j'aime le contact. Je parle aussi anglais et un peu de néerlandais, ce qui pourrait être utile avec certains clients.")
    b.page(f'{e}{e2}{e3}{e4}', "Consignes & école")

    # ---------- Leçon 6 : l'entretien ----------
    l6 = lecon("Passer un entretien", compact(table(["Moment", "Ce que je fais et ce que je dis"], [
        ["🚪 Avant", "Je relis l'offre et ma lettre · je prépare des réponses · j'arrive <b>5 à 10 minutes en avance</b> · tenue propre et adaptée · GSM éteint."],
        ["🤝 L'accueil", "« Bonjour Madame, je suis Bilal Ahmadi, j'ai rendez-vous à 14 h. » · je souris, je regarde la personne · j'attends qu'on m'invite à m'asseoir."],
        ["💬 Les questions", "« Présentez-vous. » · « Pourquoi ce poste ? » · « Quelles sont vos qualités ? Vos défauts ? » · « Que feriez-vous si… ? » → je réponds par des phrases complètes, avec des <b>exemples</b>."],
        ["❓ Mes questions", "« Quels seraient mes horaires ? » · « Y aurait-il une formation au début ? » · « Quand aurai-je une réponse ? »"],
        ["👋 La fin", "« Je vous remercie de m'avoir reçu. Au revoir, Madame. » · je serre la main si on me la tend."]], ["30mm", "152mm"])) +
        '<div class="astuce" style="margin:2mm 0 0">💡 <b>Le défaut qui devient une qualité :</b> « Je suis parfois trop perfectionniste : je vérifie tout plusieurs fois, mais j\'apprends à m\'organiser. » · <b>La question « Que feriez-vous si… ? »</b> : je réponds au <b>conditionnel</b> : « Si un enfant se blessait, je préviendrais tout de suite le responsable. »</div>')
    e = E("Je remets l'entretien dans l'ordre (1 à 6).", '<div class="card sm" style="line-height:1.8">___ « Quand pourrais-je avoir une réponse ? »<br>___ « Bonjour Monsieur, je suis Fatou Camara, j\'ai rendez-vous à 10 h. »<br>___ « Je vous remercie de m\'avoir reçue. Au revoir. »<br>___ « Asseyez-vous, je vous en prie. Présentez-vous en quelques mots. »<br>___ « Pourquoi avez-vous choisi notre pharmacie ? »<br>___ « J\'ai 16 ans, je suis élève en quatrième année et j\'aimerais découvrir… »</div>', ["lis", "numerote"], 1, "B",
          sol="« Bonjour Monsieur… » (1) · « Asseyez-vous… » (2) · « J'ai 15 ans… » (3) · « Pourquoi avez-vous choisi… » (4) · « Quand pourrais-je… » (5) · « Je vous remercie… » (6)")
    b.page(f'{l6}{e}', "Leçon 6")
    e = E("Bonne ou mauvaise attitude ? Je coche.", compact(table(["", "👍", "👎"], [[x, '<span class="chk"></span>', '<span class="chk"></span>'] for x in ["J'arrive 5 minutes en avance.", "Je mâche un chewing-gum pendant l'entretien.", "Je regarde la personne quand elle me parle.", "Je réponds seulement « oui » ou « non ».", "Je pose une question sur les horaires.", "Je regarde mon GSM pendant que la personne parle.", "Je remercie à la fin."]], ["140mm", "21mm", "21mm"])), ["lis", "coche"], 1, "B",
          sol="👍 : 1, 3, 5, 7 · 👎 : 2, 4, 6")
    e2 = E("« Que feriez-vous si… ? » Je réponds au conditionnel.", '<p>1. Que feriez-vous si un enfant pleurait parce qu\'il veut rentrer chez lui ? {0}</p><p>2. Que feriez-vous si un client était fâché ? {0}</p><p>3. Que feriez-vous si vous étiez en retard à cause du bus ? {0}</p>'.format(blank("xl")), ["ecris"], 2, "C",
           sol="Ex. : 1. Je le rassurerais, je lui proposerais un jeu et je préviendrais le responsable. — 2. Je l'écouterais calmement et j'appellerais un responsable si nécessaire. — 3. Je téléphonerais tout de suite pour prévenir et m'excuser.")
    e3 = E("J'écoute deux candidats qui se présentent. Qui a la meilleure présentation ? Je coche ce que j'entends.", compact(table(["", "Candidat 1", "Candidate 2"], [[x, '<span class="chk"></span>', '<span class="chk"></span>'] for x in ["salue et dit son nom", "parle de ses expériences avec un exemple", "explique pourquoi il / elle veut le poste", "utilise un registre formel"]], ["110mm", "36mm", "36mm"])), ["ecoute", "coche"], 2, "A",
           script="1 : « Ben… Moi, c'est Kevin. J'ai besoin de fric pour l'été, quoi. J'aime bien les gosses. » — 2 : « Bonjour Madame. Je suis Daria Kovalenko, j'ai 16 ans. Je fais de l'aide aux devoirs à la maison de quartier : j'ai appris à être patiente. J'aimerais travailler à la plaine, car j'adore les activités créatives. »",
           sol="La candidate 2 (Daria) coche toutes les cases ; le candidat 1 (fictif) ne fait qu'une présentation familière, sans exemple ni salutation.")
    e4 = E("Défi ! Je prépare ma réponse à « Présentez-vous en une minute » : qui je suis, ma formation, une expérience, deux qualités avec un exemple, pourquoi ce poste.", lines(5), ["ecris"], 3, "C",
           sol="Production personnelle structurée (5 éléments), registre formel, au moins un conditionnel (« J'aimerais… »).")
    b.page(f'{e}{e2}{e3}{e4}', "S'entraîner")

    # ---------- Documents de la vie ----------
    plaine = f'''<div class="doc" style="transform:none;border:2px solid {MC};background:#fff;padding:3mm 4mm;font-size:9.3pt;line-height:1.38">
<div class="flex" style="justify-content:space-between;align-items:center"><div><span class="xs" style="color:{MC};font-weight:700">COMMUNE DE HAUTRIVE · SERVICE JEUNESSE</span><br><b style="font-size:14pt;color:#1F2A44">☀️ Plaines de vacances 2027 : nous engageons des animateurs (H/F/X)</b></div><span class="xs muted">(offre fictive)</span></div>
<div class="grid2" style="gap:3mm;margin-top:1.5mm"><div><b>Vos missions</b><br>· animer un groupe de 10 à 12 enfants de 3 à 12 ans ;<br>· préparer et encadrer des jeux, des bricolages, des sorties ;<br>· veiller à la sécurité des enfants ;<br>· accueillir les parents le matin et le soir.<br><b>Votre profil</b><br>· avoir 16 ans au 1er juillet 2027 ;<br>· être disponible au moins deux semaines ;<br>· être dynamique, patient(e) et responsable ;<br>· brevet d'animateur ou expérience avec des enfants : un <b>atout</b>.</div>
<div><b>Nous offrons</b><br>· un contrat d'occupation d'étudiant ;<br>· des journées de 8 h 30 à 16 h 30, du lundi au vendredi ;<br>· une rémunération selon le barème communal ;<br>· une formation obligatoire de deux jours (5 et 6 juin).<br><b>Comment postuler ?</b><br>Envoyez votre CV et une lettre de motivation au Service Jeunesse, Place du Marché 1, 4999 Hautrive, ou à plaines@hautrive-exemple.be <b>avant le 31 mars 2027</b>. Les candidats retenus seront invités à un entretien en avril.<br><span class="xs muted">La commune de Hautrive pratique une politique d'égalité des chances.</span></div></div></div>'''
    e = E("Je lis l'offre de la commune. Je réponds.", plaine + f'<p class="mt2">1. Que veut dire « (H/F/X) » ? Pourquoi l\'écrit-on ? {blank("xl")}</p><p>2. Cite deux missions de l\'animateur. {blank("xl")}</p><p>3. Bilal n\'a pas de brevet d\'animateur. Peut-il postuler ? Justifie. {blank("xl")}</p><p>4. Bilal part en vacances du 6 au 20 juin. Est-ce un problème ? Pourquoi ? {blank("xl")}</p><p>5. Quelle est la date limite ? Que se passera-t-il ensuite ? {blank("l")}</p>', ["lis", "ecris"], 2, "B",
          sol="1. Homme / Femme / X (personne qui ne se reconnaît dans aucun des deux) : l'offre s'adresse à tout le monde, sans discrimination. — 2. Animer un groupe de 10 à 12 enfants, préparer des jeux et des bricolages, veiller à la sécurité, accueillir les parents. — 3. Oui : le brevet est un atout, pas une obligation ; son expérience au club de foot compte. — 4. Oui : la formation obligatoire a lieu les 5 et 6 juin (il manquerait le 6 juin) ; il devrait en parler au Service Jeunesse. — 5. Le 31 mars 2027 ; les candidats retenus seront invités à un entretien en avril.")
    e2 = E("Belgicismes et mots de l'administration. Je relie.", relie(["une plaine de vacances", "un GSM", "le barème", "une farde", "septante"], ["un téléphone portable", "soixante-dix", "le tableau officiel des salaires", "un centre aéré, un centre de loisirs (en France)", "une chemise, un classeur pour ranger des feuilles"]), ["lis", "relie"], 1, "B",
           sol="plaine de vacances → centre aéré (France) · GSM → téléphone portable · barème → tableau des salaires · farde → chemise, classeur · septante → soixante-dix")
    b.page(f'<span class="tag-doc">📄 DOCUMENT DE LA VIE</span><h2>Une offre de job étudiant</h2>{e}{e2}', "Document de la vie")
    P["job"] = b.n + 1
    depl = f'''<div class="doc" style="transform:none;border:1.5px solid #9aa1b1;background:#FFFDF6;padding:3mm 4mm;font-size:9.2pt;line-height:1.38">
<div class="flex" style="justify-content:space-between"><b style="font-size:12.5pt;color:#E4572E">💶 Job étudiant : ce que tu dois savoir</b><span class="xs muted">Point Jeunes de Hautrive (service fictif) · règles en vigueur en 2026</span></div>
<div class="grid2" style="gap:3mm;margin-top:1mm">
<div><b>① Le contrat</b> : un <b>contrat d'occupation d'étudiant</b> écrit, signé <b>avant</b> le premier jour de travail. Tu en reçois une copie.<br><b>② La période d'essai</b> : les <b>3 premiers jours</b> de travail. Pendant ces jours, toi ou ton employeur pouvez arrêter le contrat sans préavis. Ces jours sont payés.<br><b>③ Les heures</b> : <b>650 heures</b> par année civile (de janvier à décembre) avec des cotisations sociales réduites (2,71 % de ton salaire brut). Tu peux vérifier ton compteur sur le site officiel <b>Student@work</b>.</div>
<div><b>④ Tu es mineur ?</b> Au maximum 8 h par jour et 40 h par semaine ; une pause de 30 minutes après 4 h 30 de travail. Pas de travail de nuit (de 20 h à 6 h), sauf exceptions à partir de 16 ans.<br><b>⑤ Tu as 15 ans ?</b> C'est possible, mais avec des règles plus strictes : travaux légers, peu d'heures pendant l'année scolaire, jamais le dimanche ni les jours fériés.<br><b>⑥ Le salaire</b> : il ne peut pas être inférieur au salaire minimum, qui dépend de ton âge.<br>❓ Une question ? Les centres <b>Infor Jeunes</b> répondent gratuitement.</div></div></div>'''
    e = E("Je lis le dépliant d'information. Je réponds.", depl + f'<p class="mt2">1. Quand le contrat doit-il être signé ? {blank("xl")}</p><p>2. Le troisième jour, Daria se rend compte que le job ne lui plaît pas. Que peut-elle faire ? {blank("xl")}</p><p>3. Combien d\'heures un étudiant peut-il travailler par an avec des cotisations réduites ? Où vérifier ? {blank("xl")}</p><p>4. Yonas a 15 ans. Le restaurant lui propose de travailler le dimanche jusqu\'à 22 h. Est-ce permis ? Justifie avec deux règles. {blank("xl")}</p>', ["lis", "ecris"], 2, "B",
          sol="1. Avant le premier jour de travail (contrat écrit). — 2. Elle est encore en période d'essai : elle peut arrêter le contrat sans préavis (le jour travaillé est payé). — 3. 650 heures par année civile ; sur le site Student@work. — 4. Non : à 15 ans, jamais le dimanche ; et un mineur ne travaille pas la nuit (après 20 h ; avant 16 ans, aucune exception).")
    e2 = E("Je reformule les règles avec « il faut que », « on doit », « il est interdit de » (module 7).", '<p>1. (contrat) → {0}</p><p>2. (nuit, mineurs) → {0}</p>'.format(blank("xl")), ["ecris"], 3, "C",
           sol="Ex. : 1. Il faut que l'étudiant signe un contrat écrit avant de commencer. — 2. Il est interdit de faire travailler un mineur entre 20 h et 6 h (sauf exceptions à partir de 16 ans).")
    e3 = E(disc_tag("maths") + " Daria (16 ans) travaille 4 h chaque samedi pendant 40 semaines, puis 3 semaines de 38 h en juillet. Combien d'heures travaille-t-elle dans l'année ? Reste-t-elle sous le contingent ? Combien d'heures lui reste-t-il ?", f'<p>{blank("xl")}</p><p>{blank("xl")}</p>', ["ecris"], 2, "C",
           sol="4 × 40 = 160 h ; 38 × 3 = 114 h ; 160 + 114 = 274 h < 650 h : oui ; il lui reste 650 − 274 = 376 h.")
    b.page(f'<span class="tag-doc">📄 DOCUMENT DE LA VIE</span><h2>Les règles du job étudiant</h2>{e}{e2}{e3}', "Document de la vie")

    # ---------- Vers les épreuves ----------
    TXT = ["Chaque année, des milliers d'élèves du secondaire passent par une étape importante : le choix d'une orientation. Faut-il continuer dans l'enseignement général, choisir une option technique ou professionnelle, ou se tourner vers l'alternance ? Pour beaucoup de jeunes, la question fait peur.",
           "Pourtant, se tromper n'est pas grave. « Une orientation n'est jamais définitive », rappelle une conseillère d'un centre PMS. « Des passerelles existent : on peut changer d'option, reprendre des études plus tard ou se former à l'âge adulte. » Elle conseille surtout de ne pas choisir une filière uniquement parce que les amis y vont.",
           "Comment bien choisir ? D'abord, il faudrait apprendre à se connaître : ce que l'on aime, ce que l'on réussit, les situations dans lesquelles on se sent bien. Ensuite, il est utile de découvrir des métiers concrètement, par un stage d'observation, une visite d'entreprise ou une rencontre avec un professionnel. Enfin, on peut se renseigner auprès des centres PMS, des services d'information sur les études et les professions ou lors des salons de l'orientation.",
           "Les élèves qui ont appris le français récemment hésitent parfois à viser des études longues. Les conseillers sont clairs : la langue s'apprend, et la motivation compte autant que les notes. Un jeune qui parle plusieurs langues possède même un atout précieux sur le marché du travail."]
    P["epr"] = b.n + 1
    texte = '<div class="card" style="background:#fff;font-size:9.6pt;line-height:1.45;padding:2.5mm 4mm"><b style="color:' + MC + '">S\'orienter : et si on avait le droit de se tromper ?</b> <span class="xs muted">(article écrit pour le cahier)</span>' + "".join(f'<p style="margin:1.2mm 0"><b class="xs" style="color:{MC}">§{i}</b> {t}</p>' for i, t in enumerate(TXT, 1)) + '</div>'
    e = E("Entraînement de type CE1D : je lis l'article et je réponds en justifiant.", texte +
          f'<p class="sm mt2" style="margin-bottom:1mm">a) Quel est le thème de l\'article ? Formule-le en une phrase. {blank("xl")}</p><p class="sm" style="margin-bottom:1mm">b) Recopie la phrase du § 2 qui montre que l\'on peut changer d\'orientation. {blank("xl")}</p><p class="sm" style="margin-bottom:1mm">c) Le § 3 donne trois conseils. Relève les trois mots qui organisent ce paragraphe. {blank("l")}</p><p class="sm" style="margin-bottom:1mm">d) « il <b>faudrait</b> apprendre à se connaître » : à quel mode est ce verbe ? Quel est son emploi ? {blank("l")}</p>', ["lis", "ecris"], 3, "C",
          sol="a) Le choix de l'orientation scolaire et le droit de se tromper. — b) « Une orientation n'est jamais définitive » / « Des passerelles existent : on peut changer d'option… ». — c) D'abord, Ensuite, Enfin. — d) Conditionnel présent : un conseil.")
    b.page(EPR.format(k="CE1D", t="Lire un texte informatif") + e, "Vers les épreuves")
    e = E("Suite de l'épreuve.", f'<p class="sm">e) Vrai ou faux ? Justifie par une citation : « Selon les conseillers, les notes comptent plus que la motivation. » {blank("xl")}</p><p class="sm">f) Trouve dans le § 2 le contraire de « provisoire » et, dans le § 4, un mot qui signifie « un avantage ». {blank("l")}</p><p class="sm">g) Donne ton avis en 3 lignes : faut-il faire un stage avant de choisir une orientation ? Utilise un connecteur.</p>{lines(3)}', ["lis", "ecris"], 3, "C",
          sol="e) Faux : « la motivation compte autant que les notes » (§ 4). — f) « définitive » (§ 2) ; « un atout » (§ 4). — g) Avis argumenté : ex. « Oui, car un stage permet de découvrir concrètement un métier ; en effet, on comprend mieux ce qu'on aime. »")
    e2 = E("Entraînement DELF B1 · production écrite (160 mots minimum).", f'<div class="card" style="background:{TINT}"><b>Sujet :</b> Vous avez vu cette annonce sur le site d\'une auberge de jeunesse en Belgique : « Cherchons jeunes motivés (16-20 ans) pour aider à l\'accueil et au petit-déjeuner, juillet-août. Langues étrangères appréciées. » Vous écrivez au responsable pour poser votre candidature : vous vous présentez, vous expliquez vos motivations et vos qualités, et vous posez deux questions sur les conditions de travail.</div>' + lines(8), ["ecris"], 3, "C",
           sol="Grille DELF B1 (production écrite, 25 points) : respect de la consigne (lettre formelle, présentation, motivations, qualités, deux questions) et du nombre de mots, cohérence (connecteurs), registre formel (formules d'appel et de politesse, vouvoiement), conditionnel de politesse, lexique du travail, orthographe.")
    b.page(f'{e}{e2}<div class="astuce">💡 Au DELF B1, la <b>production orale</b> commence par un <b>entretien dirigé</b> (2 à 3 minutes, sans préparation) : l\'examinateur te pose des questions sur toi, tes études, tes projets. Comme dans un entretien d\'embauche, réponds par des phrases complètes et développe avec un exemple. Entraîne-toi à l\'atelier A !</div>', "Vers les épreuves")

    # ---------- Sons ----------
    e = E("Futur [e] ou conditionnel [ɛ] ? J'écoute et je répète.", '<div class="grid2"><div class="card c"><div class="big"><b>[e]</b> futur</div><p class="big" style="margin:1mm 0 0">je parler<b>ai</b> · j\'ir<b>ai</b> · je fer<b>ai</b> · je viendr<b>ai</b></p></div><div class="card c"><div class="big"><b>[ɛ]</b> conditionnel</div><p class="big" style="margin:1mm 0 0">je parler<b>ais</b> · j\'ir<b>ais</b> · je fer<b>ais</b> · je viendr<b>ais</b></p></div></div><p class="sm mt2" style="margin:2mm 0 0">✏️ [e] : la bouche est presque fermée, les lèvres tirées (comme pour sourire). [ɛ] : la bouche est plus ouverte. 🇧🇪 En Belgique, on fait en général bien la différence ; dans une partie de la France, beaucoup de gens prononcent les deux de la même façon : à l\'écrit, il faut donc réfléchir au sens !</p>', ["ecoute", "repete"], 1, "A",
          script="Lire chaque paire deux fois en exagérant l'ouverture de la bouche sur [ɛ].", sol="Activité orale.")
    e2 = E("J'écoute : [e] ou [ɛ] ? Je coche.", checks(8, ["[e]", "[ɛ]"]), ["ecoute", "coche"], 2, "A", script="1. j'aimerais — 2. j'aurai — 3. je saurais — 4. je serai — 5. je voudrais — 6. je pourrai — 7. j'enverrais — 8. je verrai",
           sol="[e] : 2, 4, 6, 8 · [ɛ] : 1, 3, 5, 7")
    e3 = E("La politesse : j'écoute et je répète (voix qui monte ↗).", '<div class="card big" style="line-height:1.9">Pourriez-vous m\'aider ↗ ? · Auriez-vous un moment ↗ ? · Serait-il possible de venir lundi ↗ ?<br>Je vous remercie ↘. · Au revoir, Madame ↘.</div>', ["ecoute", "repete"], 1, "A",
           script="Questions : voix montante ; déclaratives : voix descendante.", sol="Activité orale.")
    e4 = E("Dictée : j'écoute deux fois et j'écris (attention : futur ou conditionnel ?).", lines(3), ["ecoute", "ecris"], 2, "A",
           script="« Madame, je souhaiterais travailler dans votre magasin. Je serai libre dès juillet. Un entretien serait-il possible ? »",
           sol="Madame, je souhaiterais travailler dans votre magasin. Je serai libre dès juillet. Un entretien serait-il possible ?")
    b.page(f'<h2>J\'écoute bien · [e] / [ɛ] et la politesse</h2>{e}{e2}{e3}{e4}', "Sons")
    e = E("Les liaisons du registre formel. Je marque les liaisons (‿) puis je lis.", '<div class="card big" style="line-height:2">1. Je vous‿en prie. 2. Vous‿avez reçu ma lettre ? 3. Nous‿aimerions vous‿inviter. 4. Je suis très‿heureux. 5. Quand‿aurai-je une réponse ? 6. C\'est‿un‿emploi intéressant.</div>', ["lis", "repete"], 1, "A",
          sol="1. vous‿en — 2. Vous‿avez — 3. Nous‿aimerions, vous‿inviter — 4. très‿heureux — 5. Quand‿aurai-je ([t]) — 6. C'est‿un‿emploi")
    e2 = E("Au téléphone : j'épelle mon nom et mon adresse électronique. Je lis l'encadré, puis je m'entraîne avec mon voisin.", '<div class="card sm" style="background:#fff">« Je m\'appelle Bilal Ahmadi : A-H-M-A-D-I. » · « Mon adresse, c\'est bilal <b>point</b> cv <b>arobase</b> exemple <b>point</b> be. » · Le tiret : <b>tiret</b> (-) · le tiret bas : <b>tiret bas</b> (_) · un numéro de GSM se lit par groupes de deux : <b>zéro quatre</b> · <b>septante</b> · <b>douze</b> · <b>trente-quatre</b> · <b>cinquante-six</b>.</div>' + lines(1), ["lis", "parle", "duo"], 2, "A",
           sol="Le voisin note ce qu'il entend ; on compare avec l'original. Attention aux nombres belges : 0470 = zéro quatre septante.")
    e3 = E("J'écoute le message laissé sur un répondeur et je note les informations.", compact(table(["Qui appelle ?", "Pourquoi ?", "Quand ?", "Numéro à rappeler"], [["", "", "", ""]], ["44mm", "48mm", "44mm", "46mm"])).replace("<td></td>", '<td style="height:13mm"></td>'), ["ecoute", "ecris"], 2, "A",
           script="« Bonjour, ici Mme Lejeune, du Service Jeunesse de Hautrive, pour Bilal Ahmadi. Nous aimerions vous rencontrer pour un entretien le mercredi 14 avril à 15 h 30. Pourriez-vous confirmer au 087 65 43 21 ? Je répète : zéro quatre-vingt-sept, soixante-cinq, quarante-trois, vingt et un. Merci ! »",
           sol="Mme Lejeune, Service Jeunesse de Hautrive · inviter Bilal à un entretien · mercredi 14 avril, 15 h 30 · 087 65 43 21")
    e4 = E("Je lis vite et bien.", '<div class="card big c" style="line-height:1.8">Si Sacha savait, Sacha serait sûr de son stage.<br>Je voudrais bien que vous veniez voir mon CV vert.</div>', ["lis", "repete"], 2, "A", sol="Activité orale (virelangues écrits pour la classe).")
    e5 = E("À mon tour : je laisse un message sur le répondeur d'un employeur (en duo : l'un parle, l'autre note). Je prépare mon message.", '<div class="card sm" style="background:#fff">Je salue · je dis mon nom (et je l\'épelle) · je dis pourquoi j\'appelle · je donne mon numéro (deux fois, lentement) · je remercie et je salue.</div>' + lines(2), ["ecris", "parle", "duo"], 2, "A",
           sol="Ex. : Bonjour Madame, ici Fatou Camara, C-A-M-A-R-A. Je vous appelle au sujet du stage d'observation. Pourriez-vous me rappeler au 0485 98 76 54 ? Je répète : 0485 98 76 54. Merci beaucoup, au revoir.")
    b.page(f'<h2>J\'écoute bien · au téléphone</h2>{e}{e2}{e3}{e4}{e5}', "Sons")

    # ---------- Révision spirale ----------
    e = E("🔁 V3 · Module 7 · Le subjonctif après « il faut que ». Je complète : Il faut que tu (envoyer) ______________ ta lettre et que tu (être) ______________ à l'heure à l'entretien.", "", ["complete"], 2, "C", sol="envoies · sois")
    e2 = E("🔁 V3 · Module 10 · Les figures de style. « Ce stage a été une porte ouverte sur mon avenir. » C'est une ______________ .", "", ["complete"], 1, "C", sol="métaphore")
    e3 = E("🔁 V3 · Module 9 · L'imparfait. Je conjugue : Quand j'(être) ______________ petit, je (vouloir) ______________ devenir pompier.", "", ["complete"], 1, "C", sol="étais · voulais")
    e4 = E("🔁 V3 · Module 8 · Le passif. « La commune engage vingt animateurs. » → Vingt animateurs ______________________________ .", "", ["ecris"], 2, "C", sol="Vingt animateurs sont engagés par la commune.")
    e5 = E("🔁 V3 · Module 7 · Donner son avis. Faut-il avoir un job étudiant pendant l'année scolaire ? Mon avis en 2 phrases avec « d'une part… d'autre part ».", lines(2), ["ecris"], 2, "C", sol="Ex. : D'une part, un job permet de gagner de l'argent et d'apprendre ; d'autre part, il peut fatiguer et faire baisser les notes. Je pense qu'il vaut mieux travailler seulement pendant les vacances.")
    e6 = E("🔁 V3 · Module 2 · La langue des maths. Bilal travaille 7 h par jour pendant 10 jours à la plaine. Combien d'heures cela fait-il ? Combien d'heures lui restera-t-il sur son contingent annuel de 650 h ?", '<p>' + blank("xl") + '</p>', ["ecris"], 2, "C", sol="7 × 10 = 70 h · 650 − 70 = 580 h")
    e7 = E("🔁 V2 · Module 14 · Le futur simple. Je conjugue : L'année prochaine, je (faire) ______________ un stage et j'(apprendre) ______________ un métier.", "", ["complete"], 1, "C", sol="ferai · apprendrai")
    e8 = E("🔁 V2 · Module 12 · Les démarches. Dans un formulaire, que dois-je écrire à la rubrique « Nationalité » ? Et à « Lieu de naissance » ?", '<p>' + blank("xl") + '</p>', ["ecris"], 1, "C", sol="Le nom de ma nationalité (ex. : afghane, belge) · la ville et le pays où je suis né(e).")
    b.page(f'<h2>🔁 Je révise les modules précédents</h2>{e}{e2}{e3}{e4}{e5}{e6}{e7}{e8}', "Je révise")

    # ---------- Ateliers ----------
    e = E("En trio, nous jouons un entretien (4 min) : je tire une carte « poste ».",  '<div class="grid4" style="gap:1.5mm">' + "".join(f'<div class="card c sm" style="border:1.5px dashed {MC};padding:2.5mm 1mm"><span style="font-size:16pt">{ic}</span><br>{t}</div>' for ic, t in [("🏖️", "animateur de plaine"), ("🛒", "jobiste au supermarché"), ("🍟", "équipier en snack"), ("📚", "aide à la bibliothèque"), ("🐴", "aide au manège"), ("💊", "stage en pharmacie"), ("🔧", "stage au garage"), ("🏥", "stage à la maison de repos")]) + '</div>' +
          compact(table(["Questions du recruteur", ""], [["Présentez-vous. · Pourquoi ce poste ?", ""], ["Quelles sont vos qualités ? Un défaut ?", ""], ["Que feriez-vous si… ? (une situation difficile)", ""], ["Avez-vous des questions ?", ""]], ["100mm", "82mm"])).replace("<td></td>", '<td style="height:6mm"></td>'), ["parle", "groupe"], 2, "A",
          script="Modéliser un entretien avec un volontaire (la prof = recruteur) ; puis tourner les rôles trois fois.",
          sol="Activité orale ; l'observateur remplit la grille de l'exercice suivant.")
    e2 = E("L'observateur coche ce qu'il voit et entend, puis donne un conseil au candidat (au conditionnel !).", chk3(["Il salue, sourit et regarde le recruteur.", "Il répond par des phrases complètes, avec des exemples.", "Il vouvoie et utilise des formules polies.", "Il pose au moins une question.", "Il remercie à la fin."]) + f'<p class="mt2">Mon conseil : « Tu pourrais… / Tu devrais… » {blank("xl")}</p>', ["ecoute", "coche"], 1, "A",
           sol="Grille remplie ; conseil au conditionnel (ex. : Tu devrais parler plus lentement.).")
    e3 = E("Je prépare mes réponses aux deux questions les plus difficiles : « Quel est votre défaut ? » et « Que feriez-vous si un enfant (ou un client) refusait de vous écouter ? »", lines(4), ["ecris"], 3, "C",
           sol="Ex. : Je suis parfois un peu timide, mais je fais des efforts : au club, j'ai appris à parler devant les parents. · Je lui parlerais calmement, je lui expliquerais la règle et, si nécessaire, je demanderais l'aide du responsable.")
    b.page(f'{atl_head("A", "Atelier · Les entretiens de la classe")}{e}{e2}{e3}', "Atelier")
    ann = [("A", "Boulangerie Lemaire (Hautrive) cherche étudiant(e) pour la vente, samedi et dimanche de 7 h à 13 h. 16 ans min. Se présenter au magasin avec un CV."),
           ("B", "Asbl Les Petits Pas : stage d'observation (1 semaine) dans notre crèche pour élève intéressé(e) par la puériculture. Envoyer une lettre à stage@petitspas-exemple.be."),
           ("C", "Garage Delvaux : apprenti(e) mécanicien(ne) en alternance (CEFA), 3 jours par semaine au garage. Permis de conduire non requis. Téléphoner au 04 123 45 67."),
           ("D", "Recherche baby-sitter pour 2 enfants (4 et 7 ans), le mercredi après-midi. Références souhaitées. Contact par SMS uniquement : 0499 11 22 33.")]
    e = E("Je lis quatre petites annonces (fictives). Je complète le tableau.", '<div class="grid2" style="gap:2mm">' + "".join(f'<div class="card sm" style="background:#fff;padding:2mm 3mm"><b style="color:{MC}">{k}.</b> {t}</div>' for k, t in ann) + '</div>' +
          tall(compact(table(["", "Job, stage ou formation ?", "Comment postuler ?", "Pour qui ? (je cite un camarade)"], [["A", "", "", ""], ["B", "", "", ""], ["C", "", "", ""], ["D", "", "", ""]], ["12mm", "52mm", "60mm", "58mm"])), 8), ["lis", "ecris"], 2, "B",
          sol="A : job étudiant ; se présenter au magasin avec un CV ; un élève de 16 ans ou plus qui aime le contact · B : stage d'observation ; lettre par courriel ; Amina (intérêt pour les soins) · C : formation en alternance (apprentissage) ; téléphoner ; Mateo · D : petit job (baby-sitting) ; SMS ; un élève qui a l'habitude des enfants (Bilal, Fatou…)")
    e2 = E("Quelle annonce demande le moins de formalités ? Laquelle demande une lettre ? Pourquoi, à ton avis ?", lines(2), ["lis", "ecris"], 2, "B",
           sol="La D (un SMS) et la A (se présenter avec un CV) ; la B demande une lettre, car un stage dans une crèche exige de la motivation et du sérieux (on s'occupe de bébés).")
    e3 = E("Défi ! J'écris une petite annonce (4 lignes) pour proposer mes services : aide aux devoirs, traduction, garde d'animaux…", lines(4), ["ecris"], 3, "C",
           sol="Annonce avec : le service, pour qui, quand, une qualité ou une compétence, un moyen de contact.")
    b.page(f'{atl_head("B", "Atelier · Les petites annonces")}{e}{e2}{e3}', "Atelier")
    e = E("Je rédige mon CV au propre, sur le modèle du CV de Bilal (p. {0}).".format(P["cv"]), cv(False, 10.4), ["ecris"], 3, "C",
          sol="CV d'une page, toutes les rubriques remplies, formation dans l'ordre antichronologique, langues avec niveau, compétences tirées de vraies expériences, adresse électronique sérieuse.")
    b.page(f'{atl_head("C", "Atelier · Mon CV")}{e}', "Atelier")
    cases = ["Tu arrives 10 minutes en avance : avance de 2 cases.", "Ton GSM sonne pendant l'entretien : recule de 3 cases.", "Dis une qualité et un exemple.", "Conjugue « pouvoir » au conditionnel (je, nous).", "Tu as oublié ton CV : passe un tour.", "Transforme en formel : « Salut, t'as un job ? »",
             "Que ferais-tu si un client criait ?", "Cite trois rubriques d'un CV.", "Tu poses une bonne question : rejoue !", "Dis un métier de la santé et un métier de la construction.", "Épelle ton nom.", "Tu as signé le contrat : BRAVO !"]
    plateau = '<div class="grid4" style="gap:1.4mm">' + "".join(f'<div class="card sm" style="padding:2mm;min-height:23mm;background:{"#FFE8D6" if i == 11 else "#fff"}"><b style="color:{MC}">{i + 1}</b> {t}</div>' for i, t in enumerate(cases)) + '</div>'
    e = E("Le jeu « Décroche le job ! » (2 à 4 joueurs, un dé, un pion par joueur).", '<p class="sm" style="margin:0 0 1.5mm">On lance le dé et on avance. Sur une case « question », on répond : si la réponse est juste (les autres joueurs vérifient avec le cahier), on reste ; sinon, on recule d\'une case. Le premier qui arrive à la case 12 a décroché le job !</p>' + plateau, ["joue", "groupe"], 2, "D",
          sol="Réponses : 4. je pourrais, nous pourrions · 6. Bonjour, auriez-vous un emploi à me proposer ? · 7. Je l'écouterais calmement et j'appellerais un responsable. · 8. Ex. : coordonnées, formation, expériences, langues, compétences, loisirs · 10. Ex. : infirmier, aide-soignante ; maçon, électricienne.")
    e2 = E("Le jeu « Qui suis-je ? » (toute la classe). Un élève choisit un métier en secret ; les autres posent des questions fermées (oui / non). Il faut trouver en moins de 10 questions.", '<div class="card sm" style="background:#fff">Exemples de questions : « Est-ce que tu travailles dehors ? » · « Est-ce que tu portes un uniforme ? » · « Est-ce qu\'il faudrait faire de longues études pour faire ce métier ? » · « Est-ce que tu travailles avec des enfants ? »</div>', ["joue", "parle", "groupe"], 1, "D",
           sol="Jeu oral ; exiger des questions bien formées (est-ce que + phrase / inversion).")
    e3 = E("Après le jeu : j'invente deux nouvelles cases pour le plateau (une question sur le conditionnel ou le registre formel, et une situation d'entretien avec sa conséquence).", lines(2), ["ecris"], 2, "C",
           sol="Ex. : « Dis trois verbes irréguliers au conditionnel. » · « Tu as bien préparé tes questions : avance d'une case. »")
    b.page(f'{atl_head("D", "Atelier · Décroche le job !")}{e}{e2}{e3}', "Atelier")

    # ---------- ★ Coup de pouce ----------
    e = E("Je relie le métier et le dessin.", relie(["un cuisinier", "une infirmière", "un mécanicien", "une coiffeuse", "un maçon"], ["🔧", "🧱", "✂️", "🍳", "💉"]), ["relie"], 1, "B", alpha=True, sol="cuisinier → 🍳 · infirmière → 💉 · mécanicien → 🔧 · coiffeuse → ✂️ · maçon → 🧱")
    e2 = E("Je complète avec : un CV · un entretien · un stage · un salaire.", '<p class="big" style="line-height:2.1">1. L\'argent que je reçois pour mon travail : ______________ .<br>2. La feuille où j\'écris ma formation et mes expériences : ______________ .<br>3. Le rendez-vous avec le patron pour avoir le travail : ______________ .<br>4. J\'apprends un métier dans une entreprise : ______________ .</p>', ["complete"], 1, "C", alpha=True, sol="1. un salaire — 2. un CV — 3. un entretien — 4. un stage")
    e3 = E("J'entoure les qualités.", '<div class="card big c" style="line-height:2">ponctuel · paresseux · poli · impoli · patient · en retard · souriant</div>', ["entoure"], 1, "C", alpha=True, sol="ponctuel · poli · patient · souriant")
    b.page(CP.format(t="Les métiers") + e + e2 + e3, "★ Coup de pouce")
    e = E("Je lis le modèle. Je complète au conditionnel.", '<div class="card" style="background:#F2F6FD"><p class="big" style="margin:0">Modèle : je veux → je <b>voudrais</b> · j\'aime → j\'<b>aimerais</b></p></div><p class="big" style="line-height:2.1;margin:2mm 0 0">1. Je (vouloir) ______________ un rendez-vous.<br>2. J\'(aimer) ______________ travailler à la plaine.<br>3. Vous (pouvoir) ______________ m\'aider ?<br>4. Je (être) ______________ heureux de venir.</p>', ["lis", "complete"], 1, "C", alpha=True, sol="1. voudrais — 2. aimerais — 3. pourriez — 4. serais")
    e2 = E("Poli ou pas poli ? Je coche.", compact(table(["", "😊 poli", "😠 pas poli"], [[x, '<span class="chk"></span>', '<span class="chk"></span>'] for x in ["Donne-moi le formulaire !", "Pourriez-vous m'aider, s'il vous plaît ?", "Je voudrais un rendez-vous.", "Salut, je veux le job."]], ["120mm", "30mm", "32mm"])), ["lis", "coche"], 1, "B", alpha=True, sol="pas poli · poli · poli · pas poli")
    e3 = E("Je relie le début et la fin de la lettre.", relie(["Madame,", "Je voudrais", "Je vous remercie", "Bien à"], ["vous,", "travailler chez vous.", "Monsieur,", "de votre attention."]), ["relie"], 1, "B", alpha=True, sol="Madame, → Monsieur, · Je voudrais → travailler chez vous. · Je vous remercie → de votre attention. · Bien à → vous,")
    b.page(CP.format(t="Le conditionnel et la politesse") + e + e2 + e3, "★ Coup de pouce")
    e = E("Je complète ma fiche CV.", '<div class="card" style="background:#F2F6FD"><p class="big" style="line-height:2.2;margin:0">Prénom et NOM : ______________________<br>Âge : ______ Téléphone : ______________________<br>Langues : ______________________<br>École : ______________________<br>Une qualité : ______________________</p></div>', ["ecris"], 1, "C", alpha=True, sol="Fiche complète et lisible.")
    e2 = E("Je me présente à l'entretien. Je complète, puis je dis le texte à la prof.", '<p class="big" style="line-height:2.1">Bonjour Madame. Je m\'appelle ______________ . J\'ai ______ ans. Je parle ______________ . Je suis ______________ (une qualité). Je voudrais ______________ (le travail). Merci, au revoir !</p>', ["complete", "parle"], 1, "A", alpha=True, sol="Présentation complète, dite avec le regard et le sourire.")
    e3 = E("Je recopie la fin de la lettre.", '<div class="card" style="background:#F2F6FD"><p class="big" style="margin:0">Je vous remercie. Bien à vous,</p></div>' + lines(2), ["recopie"], 1, "C", alpha=True, sol="Copie lisible, avec la majuscule et la virgule.")
    b.page(CP.format(t="Mon CV et mon entretien") + e + e2 + e3, "★ Coup de pouce")

    # ---------- Tâche finale ----------
    e = E("Je choisis une offre et je prépare mon dossier.", '<p class="sm" style="margin:0 0 1mm">Je choisis : ☐ l\'offre de la plaine (p. {0}) ☐ l\'offre de FraisMarché (leçon 4) ☐ une annonce de l\'atelier B ☐ une vraie offre trouvée avec la prof (site du Forem, d\'Actiris, panneau d\'un magasin…)</p>'.format(P["job"] - 1) +
          tall(compact(table(["Mon dossier", "Ce que j'écris / ce que je prépare", "✅"], [["L'offre : poste, employeur, date limite, référence", "", '<span class="chk"></span>'], ["Mon CV (atelier C), mis à jour pour ce poste", "", '<span class="chk"></span>'], ["Trois raisons de ma candidature (pourquoi ce poste ?)", "", '<span class="chk"></span>'], ["Deux expériences + deux qualités avec un exemple", "", '<span class="chk"></span>'], ["Deux questions à poser à l'entretien", "", '<span class="chk"></span>']], ["62mm", "104mm", "16mm"])), 25), ["lis", "ecris"], 2, "C",
          sol="Fiche complète : offre analysée, raisons, exemples, questions préparées.")
    b.page(tache_head("Mon dossier de candidature", "Chaque élève répond à une offre : il rédige son CV et sa lettre de motivation, envoie un courriel d'accompagnement, puis passe un entretien de 5 minutes avec M. Diallo ou un adulte invité.") + e, "Tâche finale", levels=False)
    e = E("J'écris ma lettre de motivation (brouillon), sur le modèle de la lettre de Bilal (p. {0}) : ① à ⑧.".format(P["lettre"]), lines(18), ["ecris"], 3, "C",
          sol="Lettre formelle complète : mise en page ①-⑧, objet précis, corps en trois parties (pourquoi j'écris, ce que j'apporte avec exemples, ce que j'attends), conditionnel de politesse, formule finale, aucune abréviation.")
    b.page(e, "Tâche finale", levels=False)
    e = E("J'écris le courriel qui accompagne ma candidature (objet, formule d'appel, 2 phrases, formule finale, signature).", lines(6), ["ecris"], 2, "C",
          sol="Ex. : Objet : candidature au poste d'animateur. Madame, Monsieur, Je vous prie de trouver ci-joint mon CV et ma lettre de motivation pour le poste d'animateur de la plaine d'été. Je reste à votre disposition pour un entretien. Bien à vous, Bilal Ahmadi.")
    b.page(e + compact(table(["Je vérifie avant d'envoyer :", "✅"], [[x, '<span class="chk"></span>'] for x in ["Mon CV tient sur une page, sans faute, avec une adresse électronique sérieuse.", "Ma lettre a les 8 parties et un objet précis.", "Je donne des exemples concrets de mes expériences et qualités.", "J'utilise le registre formel (vous, formules de politesse, pas d'abréviation).", "J'ai fait relire mon dossier par un camarade et par la prof.", "J'ai préparé ma présentation d'une minute et deux questions."]], ["160mm", "22mm"])) +
           '<div class="astuce mt2">🤝 Le jour de l\'entretien : arrive en avance, éteins ton GSM, souris, regarde la personne, réponds avec des exemples… et n\'oublie pas de remercier !</div>' +
           E("Après l'entretien : je m'auto-évalue et j'écris ce que je ferais mieux la prochaine fois (au conditionnel).", chk3(["Mon dossier était complet et soigné.", "J'ai parlé clairement, avec des exemples.", "J'ai utilisé le registre formel."]) + lines(2), ["ecris", "coche"], 1, "C", sol="Auto-évaluation et objectif au conditionnel (ex. : La prochaine fois, je parlerais plus lentement.)."), "Tâche finale", levels=False)
    e = E("Je révise.", '<p>1. Un petit travail pendant les vacances : un ______________ étudiant. 2. On apprend un métier à l\'école et en entreprise : l\'______________ . 3. Le document qui résume ma formation et mes expériences : le ______________ . 4. Le rendez-vous pour obtenir le poste : l\'______________ . 5. Les qualités (ponctuel, poli…) : le ______________ . 6. « Je voudrais » est au ______________ . 7. Dans une lettre, je ______________ le destinataire.</p>', ["complete"], 1, "C",
          sol="1. job — 2. alternance — 3. CV — 4. entretien — 5. savoir-être — 6. conditionnel (présent) — 7. vouvoie")
    e2 = E("Je corrige le début de lettre de Mateo : 5 erreurs (formule d'appel, registre, conditionnel après « si », abréviation, formule finale).", '<div class="card" style="font-family:\'Comic Sans MS\',cursive;background:#fff;font-size:10.3pt">« Cher patron, Je veux bosser dans votre garage. Si vous m\'engageriez, je serais super content. J\'ai fait un stage ds un garage en Colombie. Bisous, Mateo »</div>' + lines(4), ["lis", "ecris"], 2, "C",
           sol="Madame, Monsieur, · Je souhaiterais travailler dans votre garage. · Si vous m'engagiez (pas de conditionnel après « si »), je serais très heureux. · « dans » (pas d'abréviation « ds ») · Je vous prie d'agréer, Madame, Monsieur, mes salutations distinguées. / Bien à vous, Mateo Ramírez")
    e3 = E("Défi ! Je complète la carte mentale du module : un mot ou un exemple par branche.", tall(compact(table(["Branche", "Mes mots / mes exemples"], [["les métiers et les secteurs", ""], ["les compétences (savoir, savoir-faire, savoir-être)", ""], ["le conditionnel (4 emplois)", ""], ["le registre formel", ""], ["le CV et la lettre", ""], ["l'entretien", ""]], ["66mm", "116mm"])), 12), ["lis", "ecris"], 3, "C",
           sol="Productions variées ; vérifier un exemple juste par branche (ex. : conditionnel : je voudrais, tu devrais, j'aimerais, si j'avais… je ferais).")
    b.page(f'<h2>🔁 Je révise tout le module</h2>{e}{e2}{e3}', "Je révise")

    # ---------- Test ----------
    Q = [("Un petit travail payé pendant les vacances s'appelle…", ["un job étudiant", "un diplôme", "un entretien", "un bénévolat"]), ("Apprendre un métier à l'école et en entreprise, c'est…", ["l'alternance", "le chômage", "le bénévolat", "le salaire"]),
         ("« Être ponctuel » est…", ["un savoir-être", "un savoir", "un diplôme", "un secteur"]), ("Une aide-soignante travaille dans le secteur…", ["de la santé", "de la construction", "des transports", "de la vente"]),
         ("« Vouloir » au conditionnel (je) :", ["je voudrais", "je voudrai", "je voulais", "je veux"]), ("« Pouvoir » au conditionnel (vous) :", ["vous pourriez", "vous pourrez", "vous pouviez", "vous pouvez"]),
         ("« Être » au conditionnel (nous) :", ["nous serions", "nous serons", "nous étions", "nous sommes"]), ("« Tu devrais relire ta lettre » exprime…", ["un conseil", "un fait certain", "un ordre", "le passé"]),
         ("« J'aimerais devenir infirmière » exprime…", ["un souhait", "une obligation", "un fait passé", "une interdiction"]), ("Si j'avais le temps, je… du bénévolat.", ["ferais", "ferai", "faisais", "fais"]),
         ("Après « si » (hypothèse), on utilise…", ["l'imparfait", "le conditionnel", "le futur", "le subjonctif"]), ("La formule d'appel formelle est…", ["Madame, Monsieur,", "Salut,", "Coucou,", "Cher ami,"]),
         ("En registre formel, « un boulot » devient…", ["un emploi", "un truc", "un job", "un taf"]), ("Dans un CV, on présente les formations…", ["de la plus récente à la plus ancienne", "par ordre alphabétique", "de la plus ancienne à la plus récente", "au hasard"]),
         ("Dans une offre, « un atout » est…", ["un plus, pas obligatoire", "une obligation", "un salaire", "un horaire"]), ("La partie « Objet » d'une lettre indique…", ["le sujet de la lettre", "l'adresse", "la date", "la signature"]),
         ("Pendant un entretien, il faut…", ["donner des exemples", "garder son GSM allumé", "tutoyer le recruteur", "répondre seulement « oui »"]), ("En Belgique, un job étudiant demande…", ["un contrat écrit", "un accord oral", "un diplôme", "une photo"]),
         ("Je parlerais : la terminaison se prononce…", ["[ɛ]", "[e]", "[i]", "[ɑ̃]"]), ("🔁 Subjonctif : « Il faut que tu … à l'heure. »", ["sois", "es", "seras", "serais"])]
    ans = [q[1][0] for q in Q]
    qrot = [1, 3, 0, 2, 2, 0, 3, 1, 0, 2, 3, 1, 2, 0, 1, 3, 0, 2, 3, 1]
    Q = [(q, o[r:] + o[:r]) for (q, o), r in zip(Q, qrot)]
    key = key_from(Q, ans)
    test_pages(b, 12, "Vers le monde du travail", Q, f'<h3>B1. Rends ces phrases polies et formelles, au conditionnel. (… / 3)</h3><p>1. Je veux un rendez-vous. {blank("xl")}</p><p>2. Tu peux m\'envoyer le contrat ? {blank("xl")}</p><p>3. Salut, j\'ai besoin d\'infos sur le job. {blank("xl")}</p><h3>B2. Complète : Si je (trouver) ______ un job, j\'(acheter) ______ un vélo. Si tu (venir) ______ à l\'entretien, tu (voir) ______ la directrice. (… / 2)</h3><h3>B3. Écris le corps d\'une lettre de motivation (6 lignes) pour un job de vendeur ou de vendeuse : pourquoi tu écris, ce que tu apportes (un exemple), ce que tu attends. (… / 5)</h3>{lines(6, True)}',
               [["se présenter comme dans un entretien (nom, formation, expérience)", "/ 3", ""], ["répondre à « Pourquoi ce poste ? » et « Quelles sont vos qualités ? »", "/ 4", ""], ["répondre à « Que feriez-vous si… ? » au conditionnel", "/ 3", ""]],
               '<h3>1. Je relie le métier et le dessin. (… / 4)</h3>' + relie(["un cuisinier", "une infirmière", "un mécanicien", "une coiffeuse"], ["✂️", "🔧", "🍳", "💉"]) + '<h3>2. J\'entoure les qualités. (… / 4)</h3><div class="card big">poli · paresseux · ponctuel · impoli · patient · souriant</div><h3>3. Je complète au conditionnel : Je (vouloir) ______ un rendez-vous. Vous (pouvoir) ______ m\'aider ? (… / 4)</h3><h3>4. Je complète : Madame, ______ (formule d\'appel) · Bien à ______ . (… / 3)</h3><h3>5. Oral : je me présente pour un job (nom, âge, langues, une qualité). (… / 5)</h3>')
    closing(b, 12, ["Je parle des métiers, des secteurs et des qualités.", "Je distingue savoir, savoir-faire et savoir-être.", "Je conjugue les verbes au conditionnel présent.", "J'utilise le conditionnel pour être poli, souhaiter, conseiller, imaginer.", "J'emploie si + imparfait → conditionnel.", "Je passe du registre familier au registre formel.",
                    "Je lis une offre d'emploi (missions, profil, conditions, candidature).", "Je rédige mon CV.", "J'écris une lettre de motivation et un courriel formel.", "Je me présente lors d'un entretien.", "Je connais les règles du job étudiant en Belgique."],
            [("💼", "un métier, un emploi"), ("🏖️", "un job étudiant"), ("🎓", "une formation, un diplôme"), ("🏢", "un stage"), ("🔁", "l'alternance"), ("📰", "une offre d'emploi"), ("✍️", "postuler, une candidature"), ("🗂️", "un CV"), ("✉️", "une lettre de motivation"), ("🤝", "un entretien"), ("🧑‍💼", "un employeur, un recruteur"), ("💶", "un salaire (brut, net)"),
             ("⭐", "une compétence"), ("🛠️", "un savoir-faire"), ("🙂", "le savoir-être"), ("➕", "un atout"), ("⏰", "ponctuel"), ("🧘", "patient"), ("📏", "rigoureux"), ("📄", "un contrat"), ("⏳", "la période d'essai"), ("🎩", "le registre formel"), ("📎", "ci-joint, une annexe"), ("🧭", "s'orienter")])
    plan_de_travail(b, E, 12, ["Le conditionnel : formation", "Les emplois du conditionnel", "Le registre formel", "L'offre d'emploi et le CV", "La lettre de motivation", "L'entretien"], "☐ Choix de l'offre<br>☐ CV<br>☐ Lettre + courriel<br>☐ Entretien")
    b.pages = [x.replace("padding:.8mm 1.5mm;display:flex", "padding:.3mm 1.5mm;display:flex").replace("repeat(7,1fr);gap:1.3mm", "repeat(7,1fr);gap:.7mm").replace("align-items:center;justify-content:space-between;font-size:8.5pt", "align-items:center;justify-content:space-between;font-size:8pt") for x in b.pages]  # plan compact
    if render:
        to_pdf(b.html(), '/home/claude/syllabus/out/V3_M12_eleve.pdf')

    pg, exs = helpers(b, E)
    CPp = b.marks["★ Coup de pouce"]
    days = [("1", "Collectif", f"Ouverture · BD · témoignages ({pg('Découvrir')})", f"CP les métiers (p. {CPp[0]})"), ("2", "Collectif + duo", f"Lexique : travail, métiers, qualités ({pg('Lexique')})", "CP métiers et qualités"),
            ("3", "Rotation", f"📌 Leçon 1 conditionnel : formation ({pg('Leçon 1')}) · sons [e] / [ɛ] ({pg('Sons')})", f"CP conditionnel (p. {CPp[1]})"), ("4", "Collectif", f"📌 Leçon 2 emplois du conditionnel ({pg('Leçon 2')})", "CP politesse"),
            ("5", "Rotation", f"📌 Leçon 3 registre formel ({pg('Leçon 3')})", "CP poli / pas poli"), ("6", "Collectif", f"📌 Leçon 4 offre et CV ({pg('Leçon 4')}) · offre de la plaine ({pg('Document de la vie')})", f"CP fiche CV (p. {CPp[2]})"),
            ("7", "Rotation", f"📌 Leçon 5 lettre de motivation ({pg('Consignes & école')}) · règles du job étudiant", "CP fin de lettre"), ("8", "Ateliers", f"📌 Leçon 6 entretien ({pg('Leçon 6')}) · ateliers ({pg('Atelier')}) · CE1D, DELF ({pg('Vers les épreuves')})", "CP se présenter"),
            ("9", "Classe + invité", f"Tâche finale : dossier et entretiens ({pg('Tâche finale')})", "Entretien guidé, questions écrites à l'avance"), ("10", "Seul", f"Test ({pg('Test')})", f"CP test ({pg('★ Coup de pouce · Test')})")]
    rot = [["🎧 Écouter-Parler", "Simulations d'entretien en trio", "30 min", "Grille de l'observateur"], ["📖 Lire", "Les petites annonces", "20 min", "Oui"], ["✏️ Écrire", "Mon CV au propre", "30 min", "Relecture entre pairs + prof"],
           ["🧩 Jouer", "« Décroche le job ! » + « Qui suis-je ? »", "20 min", "Les joueurs vérifient"], ["👩‍🏫 Table d'appui", "Coup de pouce · conditionnel, politesse, fiche CV", "20 min", "—"]]
    ev1 = f'''<h3>Partie B (10 points)</h3><p class="sm"><b>B1</b> : <span class="sol">Je voudrais (souhaiterais) un rendez-vous, s'il vous plaît. · Pourriez-vous m'envoyer le contrat ? · Bonjour, je souhaiterais (j'aimerais) des informations sur le job.</span> (1 pt chacune : conditionnel + registre). · <b>B2</b> : <span class="sol">trouvais, achèterais · venais, verrais</span> (0,5 pt chacun). · <b>B3</b> : les trois parties (2), un exemple concret (1), registre formel et conditionnel (1), langue (1).</p>
<h3>Partie C · oral (10 points)</h3><p class="sm">La prof (ou M. Diallo) joue le recruteur pour un poste de jobiste. L'élève se présente : nom, formation, une expérience (3) · il répond à « Pourquoi ce poste ? » et « Quelles sont vos qualités ? » avec un exemple (4) · il répond au conditionnel à une question « Que feriez-vous si… ? » (3).</p>
<h3>Test ★ Coup de pouce (20 points)</h3><p class="sm"><b>1 :</b> <span class="sol">cuisinier → 🍳 · infirmière → 💉 · mécanicien → 🔧 · coiffeuse → ✂️</span> (4) · <b>2 :</b> <span class="sol">poli · ponctuel · patient · souriant</span> (4) · <b>3 :</b> <span class="sol">voudrais · pourriez</span> (4) · <b>4 :</b> <span class="sol">Monsieur · vous</span> (3) · <b>5 :</b> présentation compréhensible (5).</p>
<h3>Lire les résultats du QCM : quelle remédiation ?</h3>{table(["Questions", "Compétence", "Si moins de la moitié est juste…"], [["1 à 4", "lexique du travail", f"lexique ({pg('Lexique')}) + coup de pouce p. {CPp[0]}"], ["5 à 11", "le conditionnel (formation, emplois, si + imparfait)", f"leçons 1 et 2 ({pg('Leçon 1')}, {pg('Leçon 2')}) + coup de pouce p. {CPp[1]}"], ["12 et 13", "le registre formel", f"leçon 3 ({pg('Leçon 3')})"], ["14 à 16", "offre, CV, lettre", f"leçons 4 et 5 ({pg('Leçon 4')}, {pg('Consignes & école')})"], ["17 et 18", "entretien, job étudiant", f"leçon 6 ({pg('Leçon 6')}) + dépliant ({pg('Document de la vie')})"], ["19", "[e] / [ɛ]", f"sons ({pg('Sons')})"], ["20", "révision (subjonctif)", "module 7"]], ["24mm", "62mm", "96mm"])}'''
    ev2 = f'''<h2>Grille · tâche finale « Mon dossier de candidature »</h2>{table(["Critère", "Très bien", "Bien", "À retravailler", "Points"], [["<b>CV</b> : rubriques complètes, une page, ordre antichronologique, sans faute", "Complet", "Partiel", "Incomplet", "/ 4"], ["<b>Lettre</b> : mise en page ①-⑧, objet, formules", "Respectée", "Quelques oublis", "Absente", "/ 3"], ["<b>Lettre</b> : contenu en trois parties, exemples concrets, adaptée à l'offre", "Convaincante", "Générale", "Hors sujet", "/ 4"], ["<b>Langue</b> : registre formel, conditionnel, orthographe", "Maîtrisée", "Quelques erreurs", "Familière", "/ 3"], ["<b>Courriel</b> d'accompagnement", "Correct", "Incomplet", "Absent", "/ 1"], ["<b>Entretien</b> : accueil, réponses développées, questions, remerciements", "Aisé", "Correct", "Difficile", "/ 5"]], ["66mm", "30mm", "30mm", "34mm", "22mm"])}
<h2 class="mt4">Différencier et remédier</h2>{table(["Difficulté", "Remédiation"], [["Conditionnel / futur", "Affiche « futur = -rai, -ras… ; conditionnel = -rais, -rait… (comme l'imparfait) » ; test du « nous » (parlerons / parlerions) ; dictées flash de 5 formes."], ["Registre familier", "Tableau à deux colonnes affiché en classe (familier → formel) ; réécrire un SMS en courriel ; jeu de rôle avec un « directeur » imaginaire."], ["Pas d'expérience à mettre dans le CV", "Partir de la vie réelle : garde des frères et sœurs, traduction pour la famille, aide au commerce familial, sport, bénévolat, parcours migratoire (langues, adaptation) : ce sont des compétences."], ["Trac à l'entretien", "Entretien d'abord en duo avec un camarade, puis avec la prof ; fiche de réponses préparées ; enregistrement audio pour s'écouter."], ["Élève rapide", "Répondre à une vraie offre (Forem, Actiris, site de la commune) ; rédiger une lettre de candidature spontanée ; préparer la partie 1 du DELF B1 oral (entretien dirigé)."]], ["50mm", "132mm"])}'''
    rep = f'''<h2>Le monde du travail : repères</h2>
<div class="attention"><b>Points d'attention.</b> Certains élèves travaillent déjà (aide familiale, commerce, parfois travail non déclaré) ou portent la charge d'aider leur famille financièrement : aborder le sujet sans jugement, rappeler les droits (contrat écrit, salaire minimum, limites horaires) et orienter discrètement vers le centre PMS ou un service Infor Jeunes si besoin. Le statut de séjour peut conditionner l'accès au travail : ne pas interroger les élèves sur ce point en classe ; renvoyer les questions individuelles vers les services compétents.</div>
{table(["Repère", "Ce qu'il faut savoir (vérifié en novembre 2026)"], [["Le job étudiant", "Contrat d'occupation d'étudiant écrit, signé avant le début du travail (copie à l'étudiant) · les 3 premiers jours de travail sont une période d'essai (fin possible sans préavis, journées payées) · 650 heures par année civile avec cotisations de solidarité réduites (2,71 % pour l'étudiant, 5,42 % pour l'employeur) ; compteur consultable sur le site officiel Student@work · salaire minimum fonction de l'âge (au 1er juillet 2026 : 100 % du revenu minimum à partir de 21 ans, 67 % à 16 ans et moins)."], ["Les jeunes travailleurs mineurs", "Au maximum 8 h par jour et 40 h par semaine ; pause de 30 minutes après 4 h 30 de travail ; travail de nuit (20 h - 6 h) interdit en principe, avec des exceptions à partir de 16 ans dans certains secteurs ; jamais entre minuit et 4 h. Depuis mai 2026, un élève de 15 ans encore soumis à l'obligation scolaire à temps plein peut signer un contrat d'étudiant pour des travaux légers : 2 h par jour d'école et 12 h par semaine en période scolaire, ni dimanche ni jour férié."], ["S'informer, s'orienter", "Les centres PMS (gratuits, dans chaque école) · le SIEP (Service d'information sur les études et les professions) · le Forem (Wallonie) et Actiris (Bruxelles) : services publics de l'emploi · les centres Infor Jeunes · l'alternance : CEFA (enseignement) et IFAPME (formation des classes moyennes, Wallonie)."], ["Le DELF B1", "La production orale compte trois parties : entretien dirigé (sans préparation), exercice en interaction, expression d'un point de vue (avec préparation). La production écrite demande un texte d'au moins 160 mots (souvent une lettre ou un message formel)."]], ["40mm", "142mm"])}
<div class="attention mt2"><b>Fictif :</b> la commune de Hautrive et son Service Jeunesse, la plaine de vacances, le magasin FraisMarché, la boulangerie Lemaire, le garage Delvaux, l'asbl Les Petits Pas, la pharmacie du Pont, le Point Jeunes de Hautrive, l'Athénée de Hautrive, le RFC Hautrive, les témoignages (Nadia, Marc, Leïla, Samuel), les adresses électroniques et les numéros de téléphone. Les règles du job étudiant, les services d'orientation (PMS, SIEP, Forem, Actiris, Infor Jeunes, CEFA, IFAPME) et le site Student@work sont réels.</div>
<h3>Belgicismes du module</h3><p class="sm">un <b>job étudiant</b> (aussi en France) et un <b>jobiste</b> (belgicisme : étudiant qui travaille) · une <b>plaine de vacances</b> (France : centre aéré, centre de loisirs) · un <b>GSM</b> (France : un portable) · une <b>farde</b> (France : une chemise, un classeur) · <b>septante</b>, <b>nonante</b> · le <b>barème</b> (grille officielle des salaires, très courant en Belgique) · « <b>Bien à vous</b> », formule finale de courriel très fréquente en Belgique · <b>H/F/X</b> dans les offres d'emploi · une <b>asbl</b> (association sans but lucratif ; France : association loi 1901).</p>'''
    import re as _re
    def _court(t, n=90):
        t2 = _re.sub(r"<[^>]+>", "", t)
        return t if len(t2) <= n else t2[:n].rsplit(" ", 1)[0] + "…"
    E.sols = [(p, n, _court(t), s) for p, n, t, s in E.sols]
    import lib.module as _LM
    _pg = _LM.paginate
    _LM.paginate = lambda rows, w, bf, bb: _pg(rows, w, bf + (SCR if bf == 190 else BUMP), bb + BUMP)
    _tb = _LM.table
    _LM.table = lambda *a, **k: compact(_tb(*a, **k))
    T = teacher_book(b, E, "V3 · M12", "", MC, 12, "Vers le monde du travail",
                     "<li><b>Communication :</b> parler des métiers et des compétences ; lire une offre d'emploi ; rédiger un CV, une lettre de motivation et un courriel formel ; passer un entretien.</li><li><b>Lexique :</b> le travail (métier, emploi, poste, job, salaire, employeur), la candidature (offre, postuler, CV, lettre, entretien), la formation (stage, alternance, diplôme), les compétences (savoir, savoir-faire, savoir-être, atout), les secteurs et les qualités.</li><li><b>Langue :</b> le conditionnel présent (formation, radicaux irréguliers) et ses emplois (politesse, souhait, conseil, hypothèse avec si + imparfait, information non confirmée) ; le registre formel.</li><li><b>Oral :</b> [e] / [ɛ] (futur / conditionnel) ; intonation de la politesse ; téléphoner et épeler.</li><li><b>FLSco :</b> les écrits professionnels (lettre de motivation annotée, courriel formel) ; consignes rédigez, argumentez, joignez.</li><li><b>Épreuves :</b> CE1D (texte informatif sur l'orientation) ; DELF B1 production écrite (lettre de candidature) et entretien dirigé.</li><li><b>Documents :</b> offre de la plaine de vacances communale, dépliant sur les règles du job étudiant, offre de supermarché, petites annonces, CV et lettre modèles.</li>",
                     '<p class="sm"><b style="color:#E4572E">Indispensable</b> : conditionnel de politesse (je voudrais, pourriez-vous), vouvoiement, CV simple, se présenter.</p><p class="sm"><b style="color:#d9a400">Important</b> : emplois du conditionnel, si + imparfait, structure de la lettre, lecture d\'une offre.</p><p class="sm"><b style="color:#2BA88F">Enrichissement</b> : registre soutenu, lettre complète argumentée, CE1D, DELF B1, vraie candidature.</p>',
                     "Un exemplaire du cahier par élève · quelques vraies offres d'emploi locales (journaux gratuits, sites du Forem, d'Actiris, de la commune) · ordinateurs pour mettre le CV au propre · dés et pions pour « Décroche le job ! » · cartes « poste » découpées · si possible, un adulte invité (éducateur, parent, recruteur) pour les entretiens.", "<b>Avant de commencer :</b> fixer dès le jour 1 la date des entretiens et l'adulte qui les fera passer (M. Diallo dans le cahier). Faire le lien avec le centre PMS : certains élèves ont un vrai projet de stage ou de job. Rappeler que toute expérience compte (famille, club, bénévolat, parcours dans plusieurs pays) : personne n'arrive « sans rien » à mettre dans son CV.",
                     days, "« Le conditionnel du jour » : une demande impolie au tableau, à reformuler poliment · « Un métier, une qualité » : chaque élève tire un métier et cite une qualité nécessaire · « Tu ou vous ? » : la prof décrit une situation, la classe répond.", rot, key, (ev1, ev2), extra_pages=[(rep, "Repères")], start=tstart)
    _LM.paginate = _pg
    _LM.table = _tb
    if render:
        to_pdf(T.html(), '/home/claude/syllabus/out/V3_M12_prof.pdf')
    return b, T


if __name__ == "__main__":
    b, T = build_v3m12()
    print(b.n, T.n)
