import sys
sys.path.insert(0, '/home/claude/syllabus')
from lib.base import *
from lib.art import *
from lib.render import to_pdf
from build.m1_a import build_a, MC
from build.m1_b import build_b
from build.m1_c import build_c, WS, ws_html, WS_WORDS
from build.m1_d import build_d


def build_m1(start=1, tstart=1, render=True):
    b = Book("V1 · M1", "Volume 1 · Premiers pas · Module 1 · Bonjour !", MC, start=start)
    E = Ex(b)
    build_a(b, E); build_b(b, E); build_c(b, E); key = build_d(b, E)

    # ---------- plan de travail ----------
    cells = ""
    for n, pg, lv, at, al, t in E.all:
        col = {"A": "#E4572E", "B": "#4A7BD1", "C": "#2BA88F", "D": "#9B5DE5", "P": "#1F2A44"}.get(at, "#9aa1b1")
        star = '<span style="color:#d9a400">★</span>' if al else ''
        cells += (f'<div style="border:1.5px solid #dfe3ea;border-left:4px solid {col};border-radius:1.5mm;padding:.8mm 1.5mm;display:flex;align-items:center;justify-content:space-between;font-size:8.5pt">'
                  f'<span><b>{n}</b>{star} <span class="muted">p.{pg}</span></span>{dots(lv).replace("3.2mm","2.2mm")}<span class="chk" style="width:3.6mm;height:3.6mm;margin:0"></span></div>')
    plan = f'''<h2>Mon plan de travail · Module 1</h2>
    <p class="sm">Quand j'ai fini un exercice et qu'il est corrigé, je coche la case ☑. Les ★ = parcours Alpha. La couleur = l'atelier :
    <span class="atl A">🎧</span> <span class="atl B">📖</span> <span class="atl C">✏️</span> <span class="atl D">🧩</span> <span class="atl P">👩‍🏫</span> · gris = activité de classe.</p>
    <div style="display:grid;grid-template-columns:repeat(7,1fr);gap:1.3mm">{cells}</div>
    <div class="grid3 mt4">
    <div class="card"><b>📌 Mes leçons à étudier</b><p class="sm">☐ Leçon 1 · Saluer<br>☐ Leçon 2 · Les consignes<br>☐ Leçon 3 · Se présenter<br>☐ Leçon 4 · Être et avoir<br>☐ Leçon 5 · Les nombres 0–20<br>☐ Leçon 6 · L'alphabet</p></div>
    <div class="card"><b>🎯 Ma tâche finale</b><p class="sm">☐ Interview<br>☐ Affiche<br>☐ Présentation orale</p><b>📝 Mon test</b><p class="sm">Date : ............ Note : ...... / 40</p></div>
    <div class="card"><b>✍️ Signature</b><p class="sm">Élève :<br><br>Prof :<br><br>Parent :</p></div></div>'''
    b.pages = [pg.replace("%%PLAN_DE_TRAVAIL%%", plan) for pg in b.pages]
    if render: to_pdf(b.html(), '/home/claude/syllabus/out/V1_M1_Bonjour_eleve.pdf')
    print("élève:", b.n, "pages,", E.n, "exercices")

    # =============== LIVRET ENSEIGNANT ===============
    T = Book("V1 · M1", "Volume 1 · Module 1 · Bonjour ! · Livret enseignant", MC, teacher=True, start=tstart)
    M = b.marks
    def pg(sec):
        p = M.get(sec, [])
        return f"p. {p[0]}–{p[-1]}" if len(p) > 1 else (f"p. {p[0]}" if p else "")
    def exs(sec):
        ps = set(M.get(sec, []))
        ns = [n for n, p, *_ in E.all if p in ps]
        return f"ex. {ns[0]}–{ns[-1]}" if len(ns) > 1 else (f"ex. {ns[0]}" if ns else "")

    T.page(f'''<div style="background:{MC};color:#fff;margin:-17mm -14mm 6mm -14mm;padding:20mm 14mm 10mm 14mm">
    <div style="font-size:12pt;font-weight:700;opacity:.9">LIVRET ENSEIGNANT · VOLUME 1 · MODULE 1</div><div style="font-size:40pt;font-weight:800;line-height:1.05">Bonjour !</div>
    <div style="font-size:13pt;margin-top:3mm">Déroulement · scripts · corrigés · clé QCM · grilles d'évaluation</div></div>
    <div class="grid2">
    <div class="card"><h3 style="margin-top:0">Objectifs du module</h3><ul class="sm" style="padding-left:5mm;margin:0">
    <li><b>Communication :</b> saluer, prendre congé, se présenter, questionner un pair (tu) et un adulte (vous).</li>
    <li><b>Lexique :</b> salutations, pays et langues, nombres 0–20, matériel scolaire, mots de la fiche d'identité.</li>
    <li><b>Grammaire :</b> je m'appelle / j'ai … ans / je viens de ; être et avoir au singulier ; élision je → j'.</li>
    <li><b>Phonétique :</b> voyelles [a] [i] [o] [u] ; alphabet et épellation.</li>
    <li><b>FLSco :</b> les 24 consignes-pictogrammes ; phrases de survie en classe ; remplir une feuille de réponses.</li>
    <li><b>★ Alpha :</b> étapes 0–1 (geste graphique, latéralité, prénom, voyelles, chiffres).</li></ul></div>
    <div class="card"><h3 style="margin-top:0">Les priorités</h3>
    <p class="sm"><b style="color:#E4572E">Indispensable</b> (tous les élèves) : saluer, les 4 questions de présentation, J'ai … ans, nombres 0–20, consignes, « Je ne comprends pas ».</p>
    <p class="sm"><b style="color:#d9a400">Important</b> : alphabet et épellation, être/avoir, fiche d'inscription, tu/vous.</p>
    <p class="sm"><b style="color:#2BA88F">Enrichissement</b> : de/d'/du devant les pays, il/elle, numéros de téléphone, lettre à la prof.</p>
    <h3>Matériel</h3><p class="sm">Dé · jetons (bingo) · ciseaux, colle · grandes feuilles pour le mur de la classe · objets de la classe · étiquettes-prénoms préparées pour le groupe Alpha.</p>
    <h3>Durée</h3><p class="sm">± 10 jours de cours (± 20 périodes). Élève {b.n - min(min(v) for v in b.marks.values()) + 1} pages · {E.n} exercices.</p></div></div>
    <div class="attention mt4"><b>Accueil :</b> ce module peut être fait à n'importe quel moment de l'année par un élève qui arrive. Associer le nouvel élève à un « parrain » qui parle sa langue si possible, et lui faire faire en priorité : {pg("Saluer")} (saluer), {pg("Consignes")} (consignes), {pg("Leçon 3")} (se présenter), {pg("Consignes & école")} (phrases de survie).</div>''', "Vue d'ensemble")

    days = [
     ("1", "Collectif + Alpha", f"Découverte du livre ({pg('Mon livre')}) · ouverture ({pg('Ouverture')}) · plan de travail ({pg('Mon plan de travail')}) · la BD ({pg('Découvrir')}, {exs('Découvrir')})", f"Groupe Alpha : « Je me prépare à écrire » (p. {M['★ Alpha'][0]})"),
     ("2", "Collectif puis rotation", f"Saluer ({pg('Saluer')}, {exs('Saluer')}) · 📌 Leçon 1 ({pg('Leçon 1')})", "Alpha : graphisme"),
     ("3", "Collectif (jeux) puis seul", f"Les consignes ({pg('Consignes')}, {exs('Consignes')}) · 📌 Leçon 2 ({pg('Leçon 2')}) · cartes à découper ({pg('Jeu à découper')})", "Alpha : mon prénom"),
     ("4", "Collectif puis duo", f"Documents de la vie : carte d'élève et fiche d'inscription ({pg('Document de la vie')}, {exs('Document de la vie')})", "Alpha : la lettre a"),
     ("5", "Rotation", f"📌 Leçon 3 ({pg('Leçon 3')}) · S'entraîner · Pays et langues ({pg('Pays et langues')}, {exs('Pays et langues')})", "Alpha : la lettre i"),
     ("6", "Rotation", f"📌 Leçon 4 être/avoir ({pg('Leçon 4')}) · 📌 Leçon 5 nombres ({pg('Leçon 5')}) · bingo ({pg('Jeu')})", "Alpha : la lettre o"),
     ("7", "Rotation", f"📌 Leçon 6 alphabet ({pg('Leçon 6')}) · sons ({pg('Sons')}) · matériel ({pg('Lexique')})", "Alpha : les lettres u et é"),
     ("8", "Ateliers en rotation", f"Ateliers des 4 pôles ({pg('Atelier')}, {exs('Atelier')}) · phrases de survie ({pg('Consignes & école')})", "Alpha : révision voyelles + chiffres"),
     ("9", "Groupes de 2", f"Tâche finale « Le mur de notre classe » ({pg('Tâche finale')})", "Alpha : affiche avec aide (dictée à l'adulte)"),
     ("10", "Seul", f"🔁 Je révise ({pg('Je révise')}) · test ({pg('Test')}) · je sais faire ({pg('Je sais faire')}) · mes mots ({pg('Mes mots')})", f"Alpha : test Alpha ({pg('★ Alpha · Test')})"),
    ]
    T.page(f'''<h2>Déroulement conseillé</h2>
    {table(["Jour", "Organisation", "Contenu (cahier élève)", "Groupe ★ Alpha"], [[f"<b>{d}</b>", o, c, a] for d, o, c, a in days], ["12mm", "30mm", "95mm", "45mm"])}
    <h3 class="mt4">Rituels quotidiens (10 premières minutes)</h3>
    <p class="sm">Saluer chaque élève à la porte (« Bonjour X ! — Bonjour Madame ! ») · la date au tableau · « Ça va ? » avec les 4 visages (ex. 11) · un élève épelle son prénom · compter les présents.</p>
    <h3>Rotation des ateliers (jour 8)</h3>
    {table(["Pôle", "Fiches", "Durée", "Autocorrection"], [["🎧 Écouter-Parler", "Identités secrètes · présentation orale", "20 min", "Non (prof circule)"], ["📖 Lire", "Messages du réseau de la classe", "20 min", "Oui (corrigé au mur)"], ["✏️ Écrire", "Recopier · compléter · lettre à la prof", "20 min", "● oui · ●●● prof"], ["🧩 Jouer", "Mots mêlés · dé des questions · jeu de l'oie", "20 min", "Entre joueurs"], ["👩‍🏫 Table d'appui", "Alpha : voyelles · autres : épellation, être/avoir", "20 min", "—"]], ["38mm", "70mm", "20mm", "54mm"])}''', "Déroulement")

    # pagination intelligente selon la longueur des textes
    import re, math
    def cost(row, widths):
        c = 0
        for txt, w in zip(row, widths):
            t = re.sub(r"<[^>]+>", "", str(txt))
            c = max(c, math.ceil(len(t) / max(1, w * 0.52)))
        return c * 4.4 + 4.5
    def paginate(rows, widths, budget_first, budget):
        pages, cur, used, bud = [], [], 0, budget_first
        for r in rows:
            k = cost(r, widths)
            if cur and used + k > bud:
                pages.append(cur); cur, used, bud = [], 0, budget
            cur.append(r); used += k
        if cur: pages.append(cur)
        return pages

    srows = [[f"p. {p}", f"<b>{n}</b>", t, s] for p, n, t, s in E.scripts]
    W = [14, 10, 48, 110]
    for i, chunk in enumerate(paginate(srows, W, 190, 215)):
        T.page(("<h2>Scripts à lire à voix haute</h2><p class='sm muted'>Les activités d'écoute se font sans enregistrement : l'enseignante (ou un élève avancé) lit le script. Lire lentement, deux fois, à voix naturelle.</p>" if i == 0 else "") +
               table(["Page", "Ex.", "Activité", "Script et conduite"], chunk, [f"{w}mm" for w in W]), "Scripts")

    crow = [[f"p. {p}", f"<b>{n}</b>", f'<span class="sm">{t}</span>', f'<span class="sol">{s}</span>'] for p, n, t, s in E.sols]
    W = [14, 10, 56, 102]
    for i, chunk in enumerate(paginate(crow, W, 200, 212)):
        T.page(("<h2>Corrigés</h2>" if i == 0 else "") + table(["Page", "Ex.", "Consigne", "Corrigé"], chunk, [f"{w}mm" for w in W]), "Corrigés")

    grid, sol, _ = WS
    T.page(f'<h2>Corrigé · mots mêlés</h2>{ws_html(grid, sol, 11)}<p class="c mt2">{" · ".join(WS_WORDS)}</p>', "Corrigés")

    kk = key.split(", ")
    krows = "".join(f'<div class="card c" style="padding:2mm"><b>{k.split("-")[0]}</b> → <span class="sol" style="font-size:14pt">{k.split("-")[1]}</span></div>' for k in kk)
    T.page(f'''<h2>Test du module · clé et barème</h2>
    <h3>Partie A · QCM (20 points, 1 point par question)</h3>
    <div style="display:grid;grid-template-columns:repeat(10,1fr);gap:2mm">{krows}</div>
    <div class="card mt2" style="font-family:monospace;font-size:11pt"><b>Clé à encoder dans l'application :</b> {key}</div>
    <p class="sm mt2">Questions 15 à 17 : la mini-carte d'élève (Grace MBALA, DASPA A). Questions 12 à 14 : pictogrammes. Les élèves non lecteurs passent le test ★ Alpha.</p>
    <h3>Partie B · Écrit (10 points)</h3>
    <p class="sm"><b>B1</b> (1 pt par nombre ; ½ pt si erreur d'orthographe mineure) : <span class="sol">cinq · onze · quatorze · dix-huit · vingt</span></p>
    <p class="sm"><b>B2</b> (5 pts) : 1 pt par élément — salutation ou prénom (Je m'appelle…) · âge avec <i>J'ai … ans</i> · pays (<i>Je viens de…</i>) · langue(s) (<i>Je parle…</i>) · majuscules et points corrects dans au moins 4 phrases.</p>
    <h3>Partie C · Oral (10 points)</h3>
    {table(["Critère", "2 / 2 (ou 4 / 4)", "1 / 2", "0"], [["Saluer / prendre congé (/2)", "Salue et prend congé spontanément, registre adapté (Madame)", "Une seule des deux, ou registre inadapté", "Aucune formule"],
     ["4 questions (/4)", "1 pt par réponse compréhensible en phrase (J'ai 14 ans)", "½ pt : réponse en un mot (« 14 »)", "Pas de réponse"], ["Épeler son prénom (/2)", "Sans erreur", "1 ou 2 erreurs (E/I, G/J)", "Ne peut pas"], ["Compter 0–20 (/2)", "Sans erreur", "1 à 3 erreurs ou hésitations", "S'arrête avant 10"]], ["42mm", "56mm", "48mm", "36mm"])}
    <h3>Test ★ Alpha (20 points)</h3>
    <p class="sm"><b>Exercice 2, la prof dit :</b> <span class="sol">1. i — 2. é — 3. u — 4. a</span> · <b>Exercice 3 :</b> <span class="sol">A–a, O–o, U–u, I–i</span> · <b>Exercice 4 :</b> <span class="sol">3 · 6 · 8 · 10</span> · Exercice 1 : 4 pts si prénom complet et lisible, 2 pts si une lettre manque ou est inversée.</p>''', "Évaluation")

    T.page(f'''<h2>Grille · tâche finale « Le mur de notre classe »</h2>
    {table(["Critère", "Très bien", "Bien", "À retravailler", "Points"], [
     ["<b>Contenu</b> : 5 informations sur le camarade (prénom, âge, pays, langue, ville / goût)", "5 infos exactes", "3–4 infos", "0–2 infos", "/ 5"],
     ["<b>Langue</b> : il / elle + a, vient, parle, habite", "Verbes corrects partout", "1–2 erreurs", "Plus de 2 erreurs", "/ 5"],
     ["<b>Écrit</b> : majuscules, points, orthographe des mots du module", "Soigné et correct", "Quelques oublis", "Difficile à lire", "/ 4"],
     ["<b>Oral</b> : parle fort, regarde la classe, lit sans s'arrêter", "Clair et fluide", "Lit avec hésitations", "Inaudible ou bloqué", "/ 4"],
     ["<b>Soin</b> : portrait, présentation de l'affiche", "Très soigné", "Correct", "Peu soigné", "/ 2"]], ["64mm", "32mm", "28mm", "36mm", "22mm"])}
    <p class="sm mt2"><b>Total : / 20.</b> Pour les élèves ★ Alpha : l'affiche est faite en dictée à l'adulte ; évaluer seulement l'oral (/ 10) et le prénom écrit.</p>
    <h2 class="mt4">Différencier et remédier</h2>
    {table(["Difficulté observée", "Remédiation proposée"], [
     ["Confond « je suis » et « j'ai » pour l'âge", "Reprendre la leçon 4 en geste : ✋ sur le cœur = je suis ; main qui tient un objet = j'ai. Ex. corrigés en chœur. Chaîne orale « J'ai … ans, et toi ? »."],
     ["Ne comprend pas les consignes", "Cartes-consignes collées sur la table ; jeu « Jacques a dit » chaque jour pendant 5 minutes ; le parrain reformule dans la langue commune."],
     ["Confond E / I, G / J à l'épellation", "Associer chaque lettre à une forme de bouche et à un geste : E (bouche ronde, comme dans « le ») / I (sourire, comme dans « île ») ; G « gé » / J « ji ». Dictées de lettres en duo."],
     ["Nombres 11–16 confondus", "Bingo quotidien ; cartes chiffre / mot en memory ; compter les présents chaque matin."],
     ["Élève très rapide", "Exercices ●●● ; lettre à la prof ; rôle de « tuteur » au pôle 🧩 ; préparer l'affiche multilingue « Bonjour » de la classe."],
     ["Élève Alpha qui stagne", "Revenir aux tracés et au prénom ; travailler la discrimination visuelle (ex. AMINA) avec d'autres prénoms ; réduire le nombre de lettres travaillées."]], ["58mm", "124mm"])}''', "Évaluation")

    if render: to_pdf(T.html(), '/home/claude/syllabus/out/V1_M1_Bonjour_livret_enseignant.pdf')
    print("prof:", T.n, "pages")

    return b, T


if __name__ == '__main__':
    build_m1()
