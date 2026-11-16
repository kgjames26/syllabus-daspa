"""Table des matières détaillée + index « je cherche… » pour un volume.

Tout est calculé à partir des pages réellement produites (Book.raw), donc les numéros
de page restent justes quand on ajoute ou modifie un module.
"""
import re
from .base import *
from .module import paginate
from .measure import pack

TAG = re.compile(r"<[^>]+>")
RUB = {  # rubrique -> (icône, libellé court)
    "Ouverture": ("🚪", "Ouverture"), "Mon plan de travail": ("🗂️", "Plan de travail"), "Découvrir": ("👀", "Découvrir (BD)"), "Lexique": ("🔤", "Vocabulaire"),
    "Leçon": ("📌", "Leçon"), "S'entraîner": ("✏️", "S'entraîner"), "Document de la vie": ("📄", "Document de la vie"), "Consignes & école": ("🎒", "Français de l'école"),
    "Sons": ("👂", "Sons"), "Je révise": ("🔁", "Révision"), "Atelier": ("🧩", "Atelier"), "★ Alpha": ("★", "Alpha"), "Tâche finale": ("🎯", "Tâche finale"),
    "Test": ("📝", "Test"), "★ Alpha · Test": ("★", "Test Alpha"), "Je sais faire": ("✅", "Je sais faire"), "Mes mots": ("📒", "Mes mots"), "Le plan": ("🗺️", "Document"),
}


def clean(t):
    t = TAG.sub("", t).replace("&#39;", "'").replace("&nbsp;", " ")
    return re.sub(r"\s+", " ", t).strip(" ·")


def rubrique(sec):
    if sec.startswith("Leçon"):
        return "Leçon"
    if sec.startswith("Atelier"):
        return "Atelier"
    return sec if sec in RUB else "Autre"


def page_title(sec, body):
    """Le meilleur titre lisible d'une page."""
    m = re.search(r'<div class="lt">.*?</div><h3[^>]*>(.*?)</h3>', body, re.S)
    if m and (sec.startswith("Leçon") or sec == "Consignes & école"):
        return clean(m.group(1))
    m = re.search(r"TÂCHE FINALE</div><div[^>]*>(.*?)</div>", body, re.S)
    if m:
        return clean(m.group(1))
    m = re.search(r'★ ALPHA</span><span class="big">(.*?)</span>', body, re.S)
    if m:
        return clean(m.group(1))
    for pat in (r"<h2[^>]*>(.*?)</h2>", r'<div class="lt">.*?</div><h3[^>]*>(.*?)</h3>', r'<div class="ex-t">(.*?)</div>'):
        m = re.search(pat, body, re.S)
        if m:
            t = clean(m.group(1))
            if t and t not in ("Mon plan de travail",):
                return t
    return sec


def exercises(body):
    return [clean(x) for x in re.findall(r'<div class="ex-t">(.*?)</div>', body, re.S)]


def entries(book):
    """Regroupe les pages consécutives d'une même rubrique : [(p1, p2, rub, sec, titre, [exos])]."""
    out = []
    for n, sec, body in getattr(book, "raw", []):
        if sec in ("Sommaire", "_", ""):
            continue
        rub = rubrique(sec)
        t = page_title(sec, body)
        ex = exercises(body)
        last = out[-1] if out else None
        merge = last and last[1] == n - 1 and (
            (last[3] == sec and rub not in ("Leçon", "Document de la vie", "★ Alpha", "Atelier"))
            or (sec == "S'entraîner" and last[2] in ("Leçon", "Lexique"))
            or (rub == "★ Alpha" and last[2] == "★ Alpha" and t.startswith("Je") and last[4].startswith("Je"))
            or (sec == last[3] and t == last[4]))
        if merge:
            out[-1] = (last[0], n, last[2], last[3], last[4], last[5] + ex)
        else:
            out.append((n, n, rub, sec, t, ex))
    return out


def pp(a, b):
    return f"p. {a}" if a == b else f"p. {a}–{b}"


# ---------- recherche « je cherche… » ----------
NEEDS = [
    ("Communiquer", [
        ("Saluer, se présenter", r"salu|présente|je m'appelle|bonjour"),
        ("Parler de sa famille, décrire une personne", r"famille|décri(re|s) une personne|portrait"),
        ("Être poli, demander de l'aide, s'excuser", r"poli|aide|excuse|je voudrais"),
        ("Dire ce qu'on aime, ses goûts", r"goût|aime|adore|déteste"),
        ("Acheter, demander un prix", r"prix|acheter|courses|marché|combien"),
        ("Demander et expliquer un chemin", r"chemin|direction|itinéraire|gauche|droite"),
        ("Dire où on a mal, la santé", r"mal |santé|médecin|corps|pharmacie"),
        ("Inviter, accepter, refuser", r"invit|accepte|refuse"),
        ("Raconter (ordre, passé)", r"racont|d'abord|chronolog|week-end|excursion"),
        ("Parler de ses projets (futur)", r"futur|projet|vacances|demain"),
    ]),
    ("Grammaire et conjugaison", [
        ("Être et avoir", r"être et avoir|\bêtre\b.*\bavoir\b"),
        ("Le présent des verbes en -er", r"verbes en -er|présent des verbes"),
        ("Verbes irréguliers (aller, faire, mettre, vouloir, pouvoir, devoir)", r"\baller\b|\bfaire\b|mettre|vouloir|pouvoir|devoir"),
        ("Les verbes pronominaux (se lever)", r"pronomina|se lever|s'habiller"),
        ("L'impératif (consignes, conseils)", r"impératif"),
        ("Le passé composé", r"passé composé"),
        ("Le futur proche", r"futur proche"),
        ("Les articles (un, le, du…)", r"un, une|le, la|du, de la|articles"),
        ("Les possessifs (mon, ma, mes)", r"mon, ma|possessif"),
        ("Masculin, féminin, accord des adjectifs", r"masculin|féminin|accord"),
        ("La négation (ne… pas, jamais)", r"négation|ne… pas|ne… jamais|jamais"),
        ("Poser une question", r"question|est-ce que|quel \?"),
        ("Les prépositions de lieu (où ?)", r"préposition|où est|il y a|où c'est"),
        ("Au, à la, aux · à pied, en bus", r"aller à|au · à la|à pied|transports"),
        ("La fréquence (toujours, souvent)", r"fréquence|toujours|souvent"),
    ]),
    ("Vocabulaire", [
        ("L'alphabet", r"alphabet"), ("Les nombres", r"nombre"), ("L'heure", r"heure"), ("Les jours, les mois, la date", r"jours|mois|date|calendrier"),
        ("L'argent, les euros", r"euro|argent|monnaie"), ("Les saisons et la météo", r"saison|météo|temps fait-il|température"), ("Les couleurs", r"couleur"),
        ("Les vêtements", r"vêtement|tenue|habill"), ("La nourriture, les repas", r"aliment|repas|menu|recette|cantine"), ("Le corps", r"corps"),
        ("L'école, la classe", r"école|classe|cartable|emploi du temps|journal de classe"), ("La ville, les transports", r"ville|quartier|transport|bus"),
        ("Les sports et les loisirs", r"sport|loisir"), ("Les actions de la journée", r"journée|routine"),
    ]),
    ("Compétences de l'école (FLESco)", [
        ("Comprendre les consignes", r"consigne"), ("Lire un document (affiche, horaire, ticket…)", r"lis (l'|le |la )|lire un|document"),
        ("Lire une carte, un plan, une légende", r"carte|plan|légende"), ("Résoudre un problème", r"problème"), ("Remplir un formulaire", r"formulaire|fiche"),
        ("Décrire une image", r"décrire une image"), ("Mettre dans l'ordre (chronologie)", r"ordre|chronolog|ligne du temps"),
    ]),
]


def find(mods, pattern):
    """mods : [(label, entries)] → « M3 p. 12, 15 · M7 p. 40 »."""
    rx = re.compile(pattern, re.I)
    res = []
    for label, ents in mods:
        pages = []
        for p1, p2, rub, sec, t, ex in ents:
            if rub in ("Test", "Test Alpha", "Je sais faire", "Mes mots", "Mon plan de travail", "Ouverture", "★ Alpha · Test", "Je révise"):
                continue
            hay = t + " " + " ".join(ex[:1] if rub in ("Atelier", "Sons") else ex)
            if rx.search(t) or (rub in ("Leçon", "Consignes & école", "Document de la vie", "Lexique") and rx.search(hay)):
                if not pages or pages[-1][1] < p1 - 1:
                    pages.append([p1, p2])
                else:
                    pages[-1][1] = max(pages[-1][1], p2)
        if pages:
            res.append(f'<b>{label}</b> ' + ", ".join(str(a) if a == b else f"{a}–{b}" for a, b in pages[:4]))
    return " · ".join(res)


def build_toc(Book, code, title, color, modules, annex=None, prof=None, start=1, teacher=False):
    """modules : [(num, titre, book_élève, book_prof)] ; prof=True ajoute la colonne livret enseignant."""
    S = Book(code, title, color, teacher=teacher, start=start)
    mods = [(f"M{num}", entries(b)) for num, t, b, T in modules]
    vol = re.sub(r" · (Livret enseignant|Index).*", "", title)

    # 1. mode d'emploi
    legend = "".join(f'<div class="card c" style="padding:1.5mm"><div style="font-size:14pt">{RUB[k][0]}</div><div class="xs"><b>{RUB[k][1]}</b></div></div>' for k in ["Découvrir", "Lexique", "Leçon", "S'entraîner", "Document de la vie", "Consignes & école", "Sons", "Atelier", "★ Alpha", "Tâche finale", "Test", "Je révise"])
    how = [("Je prépare mon prochain cours", "Partie 1 : je cherche le module, je vois toutes ses rubriques dans l'ordre du cahier, avec les pages élève" + (" et les pages du livret (déroulement, scripts, corrigés, évaluation)." if prof else ".")),
           ("Je veux travailler une matière précise", "Partie 2 « Je cherche… » : un besoin (l'impératif, l'heure, un formulaire…) → toutes les pages où on le travaille, dans tous les modules."),
           ("Je cherche un type d'activité", "Partie 3 : tous les documents de la vie, les pages ★ Alpha, les sons, les ateliers, les tâches finales et les tests, module par module."),
           ("Je cherche un mémo pour les élèves", "Les annexes en fin de cahier élève : conjugaison, grammaire, sons, nombres, consignes en images.")]
    S.page(f'<h1>Table des matières détaillée</h1><p class="muted mb4">{vol} · tous les numéros renvoient au <b>cahier élève</b>' + (" ; la colonne « Livret » renvoie à ce livret enseignant." if prof else ".") + '</p>' +
           table(["Je veux…", "Où regarder ?"], [[f"<b>{a}</b>", b2] for a, b2 in how], ["60mm", "122mm"]) +
           
           '<h3 class="mt4">Les 12 modules en un coup d\'œil</h3>' + table(["", "Module", "Pages élève"] + (["Livret"] if prof else []),
                                                                               [[f"<b>{num}</b>", t, pp(min(min(v) for v in b.marks.values()), b.n)] + ([pp(min(min(v) for v in T.marks.values()), T.n)] if prof else []) for num, t, b, T in modules] +
                                                                               ([["📎", "Annexes · mémos", pp(min(min(v) for v in annex.marks.values()), annex.n)] + ([""] if prof else [])] if annex else []),
                                                                               ["10mm", "112mm", "30mm"] + (["30mm"] if prof else [])), "Table des matières", levels=False)

    # 2. partie 1 : module par module (une fiche par module, 2 par page)
    def short(x, rub):
        x = re.sub(r"^(Atelier|Ateliers) · ", "", x)
        x = re.sub(r"^La lettre ", "", x)
        if rub == "Sons":
            x = re.split(r"\. | J'écoute| :", x)[0]
        if rub in ("Atelier", "Document de la vie", "Lexique", "Découvrir") and len(x) > 46:
            x = re.split(r"\. |, | : | \(", x)[0]
            if len(x) > 46:
                x = x[:44].rsplit(" ", 1)[0] + "…"
        return x

    def fiche(num, t, b, T):
        ents = entries(b)
        groups = [("📌 Leçons", ("Leçon",)), ("👀 BD · 🔤 Vocabulaire", ("Découvrir", "Lexique")), ("📄 Documents", ("Document de la vie", "Le plan")), ("🎒 Fr. de l'école", ("Consignes & école",)),
                  ("👂 Sons", ("Sons",)), ("★ Alpha", ("★ Alpha",)), ("🧩 Ateliers", ("Atelier",)), ("🎯 Tâche · 🔁 Révision", ("Tâche finale", "Je révise")), ("📝 Évaluation", ("Test", "★ Alpha · Test", "Je sais faire", "Mes mots"))]
        rows = []
        for lab, rubs in groups:
            items, seen = [], set()
            for p1, p2, rub, sec, tt, ex in ents:
                if rub in rubs or sec in rubs:
                    x = short(ex[0] if rub == "Sons" and ex else tt, rub)
                    if rub == "Leçon":
                        x = f"<b>{sec.replace('Leçon ', 'L')}</b> {tt}"
                    if rub == "Je révise":
                        x = "🔁 révision"
                    if rub in ("Test", "★ Alpha · Test", "Je sais faire", "Mes mots"):
                        x = {"Test": "Test /40", "★ Alpha · Test": "★ Test Alpha /20", "Je sais faire": "Je sais faire", "Mes mots": "Mes mots"}[rub]
                    if x in seen:
                        continue
                    seen.add(x)
                    items.append(f'{x} <span style="color:{color};font-weight:800">{pp(p1, p2)[3:]}</span>')
            if items:
                sep = "<br>" if lab.startswith("📌") else " · "
                rows.append(f'<tr><td style="width:34mm;vertical-align:top;white-space:nowrap"><b class="xs">{lab}</b></td><td class="xs" style="line-height:1.45">{sep.join(items)}</td></tr>')
        if prof and T is not None:
            tm = T.marks
            lv = " · ".join(f'{k} <span style="color:{color};font-weight:800">{pp(tm[k][0], tm[k][-1])[3:]}</span>' for k in ["Vue d'ensemble", "Déroulement", "Scripts", "Corrigés", "Évaluation"] if k in tm)
            rows.append(f'<tr style="background:#FFF4EF"><td><b class="xs">👩‍🏫 Livret enseignant</b></td><td class="xs">{lv}</td></tr>')
        p0 = min(min(v) for v in b.marks.values())
        return (f'<div style="margin-bottom:3mm"><div style="background:{color};color:#fff;padding:1.5mm 3mm;border-radius:2mm 2mm 0 0;display:flex;justify-content:space-between;align-items:center">'
                f'<b style="font-size:12pt">Module {num} · {t}</b><span class="sm">élève p. {p0}–{b.n}</span></div><table class="t compact" style="margin:0">{"".join(rows)}</table></div>')

    fiches = [fiche(*m) for m in modules]
    for i, grp in enumerate(pack(fiches, 232, 252)):
        S.page(("<h2>1 · Module par module</h2><p class='sm muted' style='margin-top:-1mm'>Les numéros en couleur = pages du cahier élève" + (" ; la ligne « Livret enseignant » = pages de ce livret." if prof else ".") + "</p>" if i == 0 else "") + "".join(grp), "Table des matières", levels=False)

    # 3. partie 2 : je cherche…
    rows = []
    for cat, needs in NEEDS:
        rows.append([f'<div style="background:{color};color:#fff;padding:1mm 2mm;border-radius:1mm;font-weight:800">{cat}</div>', ""])
        for lab, rx in needs:
            r = find(mods, rx)
            if r:
                rows.append([f'<b class="sm">{lab}</b>', f'<span class="sm">{r}</span>'])
    W2 = [62, 120]
    def blk(r):
        cg = f'<colgroup><col style="width:{W2[0]}mm"><col style="width:{W2[1]}mm"></colgroup>'
        tr = (f"<td colspan=2>{r[0]}</td>" if r[1] == "" else f"<td>{r[0]}</td><td>{r[1]}</td>")
        return f'<table class="t" style="margin-top:-1px">{cg}<tr>{tr}</tr></table>'
    for i, ch in enumerate(pack([blk(r) for r in rows], 232, 252)):
        body = "".join(ch)
        S.page(("<h2>2 · Je cherche… (index par besoin)</h2><p class='sm muted'>M3 12–14 = module 3, pages 12 à 14 du cahier élève. Les leçons à étudier (📌) sont en général sur la première page citée.</p>" if i == 0 else "") +
               body, "Index", levels=False)

    # 4. partie 3 : par type d'activité
    cats = [("📌 Toutes les leçons à étudier", ("Leçon",)), ("🎒 Français de l'école (méthodes)", ("Consignes & école",)), ("📄 Documents", ("Document de la vie", "Le plan")), ("👂 Sons et phonétique", ("Sons",)),
            ("★ Parcours Alpha", ("★ Alpha",)), ("🧩 Ateliers et jeux", ("Atelier",)), ("🎯 Tâches finales", ("Tâche finale",)), ("📝 Tests", ("Test", "★ Alpha · Test"))]
    rows = []
    for cat, rubs in cats:
        rows.append([f'<div style="background:{color};color:#fff;padding:1mm 2mm;border-radius:1mm;font-weight:800">{cat}</div>', ""])
        for (lab, ents), (num, t, b, T) in zip(mods, modules):
            items = []
            seen = set()
            for p1, p2, rub, sec, tt, ex in ents:
                if rub in rubs or sec in rubs:
                    x = (ex[0] if rub == "Sons" and ex else tt)
                    if rub in ("Test", "★ Alpha · Test"):
                        x = "Test" if rub == "Test" else "★ Test Alpha"
                    if (x, rub) in seen:
                        continue
                    seen.add((x, rub))
                    items.append(f"{x} <b>({p1})</b>")
            if items:
                rows.append([f'<b class="sm">{lab} · {t}</b>', '<span class="sm">' + " · ".join(items) + '</span>'])
    for i, ch in enumerate(pack([blk(r) for r in rows], 238, 252)):
        body = "".join(ch)
        S.page(("<h2>3 · Par type d'activité</h2><p class='sm muted'>Le numéro entre parenthèses = la page du cahier élève.</p>" if i == 0 else "") +
               body, "Index", levels=False)
    return S
