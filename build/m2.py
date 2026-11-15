import sys
sys.path.insert(0, '/home/claude/syllabus')
from lib.base import *
from lib.module import plan_de_travail, teacher_book, helpers
from lib.render import to_pdf
from build.m2_a import build_a, MC
from build.m2_b import build_b
from build.m2_c import build_c


def build_m2(start=1, tstart=1, render=True):
    b = Book("V1 · M2", "Volume 1 · Premiers pas · Module 2 · Mon école", MC, start=start)
    E = Ex(b)
    build_a(b, E); build_b(b, E); key = build_c(b, E)
    plan_de_travail(b, E, 2, ["Un, une, des", "Le, la, l', les · le pluriel", "Il y a · Où est… ?", "Demander de l'aide · s'excuser", "Les consignes à deux actions"], "☐ Visite et choix des lieux<br>☐ Pages du guide<br>☐ Présentation")
    if render: to_pdf(b.html(), '/home/claude/syllabus/out/V1_M2_Mon_ecole_eleve.pdf')
    print("élève:", b.n, "pages,", E.n, "exercices")
    pg, exs = helpers(b, E)
    A = b.marks["★ Alpha"]
    days = [
     ("1", "Collectif", f"Ouverture ({pg('Ouverture')}) · plan de travail · la BD ({pg('Découvrir')}, {exs('Découvrir')})", f"Alpha : lettre m (p. {A[0]})"),
     ("2", "Collectif + rotation", f"Les objets ({pg('Lexique')}) · 📌 Leçon 1 un/une/des ({pg('Leçon 1')})", f"Alpha : lettre l (p. {A[1]})"),
     ("3", "Rotation", f"📌 Leçon 2 le/la/les ({pg('Leçon 2')}) · S'entraîner · jeu de Kim", f"Alpha : lettre s (p. {A[2]})"),
     ("4", "Visite de l'école", f"Les lieux · le plan ({pg('Document de la vie')}) · 📌 Leçon 3 il y a ({pg('Leçon 3')})", f"Alpha : lettre r (p. {A[3]})"),
     ("5", "Rotation", "Les personnes de l'école · les cours · l'horaire", f"Alpha : syllabes (p. {A[4]})"),
     ("6", "Collectif + jeux de rôle", f"📌 Leçon 4 aide et excuses ({pg('Leçon 4')}) · le règlement", f"Alpha : premiers mots (p. {A[5]})"),
     ("7", "Rotation", f"Consignes à 2 actions ({pg('Consignes & école')}) · sons ({pg('Sons')}) · 🔁 révision M1", f"Alpha : dictée de syllabes (p. {A[6]})"),
     ("8", "Ateliers", f"Ateliers des 4 pôles ({pg('Atelier')}, {exs('Atelier')})", "Alpha : révision + memory"),
     ("9", "Groupes de 3", f"Tâche finale « Le guide de notre école » ({pg('Tâche finale')})", "Alpha : dessins + étiquettes de lieux"),
     ("10", "Seul", f"🔁 Je révise · test ({pg('Test')}) · je sais faire · mes mots", f"Alpha : test Alpha ({pg('★ Alpha · Test')})")]
    rot = [["🎧 Écouter-Parler", "Devinettes « Où suis-je ? » · décrire la classe", "20 min", "Réponse au dos des cartes"], ["📖 Lire", "Page internet de l'école", "20 min", "Oui (corrigé au mur)"],
           ["✏️ Écrire", "Liste de matériel · message au nouvel élève", "20 min", "● oui · ●●● prof"], ["🧩 Jouer", "Memory · mots croisés", "20 min", "Entre joueurs"], ["👩‍🏫 Table d'appui", "Alpha : syllabes · autres : le/la/les, pluriel", "20 min", "—"]]
    eval1 = '''<h3>Partie B · Écrit (10 points)</h3><p class="sm"><b>B1</b> (1 pt par réponse) : <span class="sol">un cahier · une gomme · une chaise · un ordinateur</span></p>
    <p class="sm"><b>B2</b> (1 pt par phrase correcte avec « il y a » + article) · <b>B3</b> (3 pts) : formule polie (1) + verbe « pouvoir / prêter » (1) + « s'il vous plaît » ou vouvoiement (1). Ex. : <span class="sol">Madame, vous pouvez me prêter un stylo, s'il vous plaît ?</span></p>
    <h3>Partie C · Oral (10 points)</h3><p class="sm">Objets : ½ pt par objet avec le bon article · lieux : 1 pt par lieu situé (« au 1er étage », « au rez-de-chaussée ») · chemin : « Excusez-moi, où est… ? » + merci (2) · retard : « Excusez-moi pour le retard » (2).</p>
    <h3>Test ★ Alpha (20 points)</h3><p class="sm"><b>Ex. 1, la prof dit :</b> <span class="sol">mi · lu · sa · ré</span> · <b>Ex. 2 :</b> <span class="sol">lama–🦙, mur–🧱, lire–📖, ami–🙋</span> · <b>Ex. 3, dicter :</b> <span class="sol">ma, li, so, ru</span> (1 pt chacune) · Ex. 4 et 5 : 1 pt par mot (½ sans article).</p>'''
    eval2 = f'''<h2>Grille · tâche finale « Le guide de notre école »</h2>
    {table(["Critère", "Très bien", "Bien", "À retravailler", "Points"], [["<b>Contenu</b> : 4 lieux, chacun avec 3 informations", "4 lieux complets", "3 lieux / infos partielles", "Moins de 3 lieux", "/ 6"], ["<b>Langue</b> : il y a, articles, pluriel", "Correct partout", "Quelques erreurs", "Beaucoup d'erreurs", "/ 6"], ["<b>Oral</b> : présentation claire d'un lieu", "Clair, fluide", "Hésitant", "Bloqué", "/ 4"], ["<b>Collaboration et soin</b>", "Excellent", "Correct", "Insuffisant", "/ 4"]], ["64mm", "32mm", "32mm", "32mm", "22mm"])}
    <h2 class="mt4">Différencier et remédier</h2>
    {table(["Difficulté", "Remédiation"], [["Genre des noms (un/une)", "Code couleur bleu/rose sur les étiquettes de la classe ; memory ; toujours écrire le mot avec son article."], ["Le / la / les à l'oral", "Jeu « Donne-moi le… » avec les objets réels ; dictée d'objets."], ["Il y a / il est", "Images à décrire chaque matin (rituel « Qu'est-ce qu'il y a sur l'image ? »)."], ["Se repérer dans l'école", "Visite réelle avec le plan ; chasse au trésor (indices écrits dans chaque lieu)."], ["Élève rapide", "Exercices ●●● ; rédiger les devinettes « Où suis-je ? » pour la classe ; traduire le guide dans sa langue."], ["Alpha : confusion m / n", "Tracer en grand, compter les « ponts » (m = 2 ponts, n = 1 pont) ; cartes-syllabes."]], ["50mm", "132mm"])}'''
    T = teacher_book(b, E, "V1 · M2", "", MC, 2, "Mon école",
      "<li><b>Communication :</b> nommer objets et lieux, se repérer, demander de l'aide, s'excuser, être poli (tu/vous).</li><li><b>Lexique :</b> 24 objets de la classe, 16 lieux, personnel de l'école, matières.</li><li><b>Grammaire :</b> un/une/des, le/la/l'/les, pluriel en -s, il y a / il n'y a pas de, où est / où sont, c'est / ce sont.</li><li><b>Phonétique :</b> [y]/[u], [s]/[z], ils sont / ils ont.</li><li><b>FLSco :</b> plan, horaire, règlement, consignes à deux actions.</li><li><b>★ Alpha :</b> étape 2 — m, l, s, r ; syllabes ; premiers mots.</li>",
      '<p class="sm"><b style="color:#E4572E">Indispensable</b> : lieux de l\'école, demander de l\'aide, « Excusez-moi », il y a, objets de base.</p><p class="sm"><b style="color:#d9a400">Important</b> : genre (un/une, le/la), pluriel, lecture de l\'horaire.</p><p class="sm"><b style="color:#2BA88F">Enrichissement</b> : il n\'y a pas de, [s]/[z], règlement.</p>',
      "Objets réels de la classe · plan réel de l'école · horaire réel des élèves · ciseaux (memory, devinettes) · appareil photo ou tablette pour le guide (facultatif).",
      "<b>Conseil :</b> faire la visite réelle de l'école dès le jour 4. Remplacer les noms fictifs (Athénée des Tilleuls, Mme Lambert, M. Diallo) par ceux de l'école dans les échanges oraux.",
      days, "Date + météo · « Qu'est-ce qu'il y a dans la classe aujourd'hui ? » · un élève lit l'horaire du jour au tableau · révision rapide des nombres (M1).", rot, key, (eval1, eval2), start=tstart)
    if render: to_pdf(T.html(), '/home/claude/syllabus/out/V1_M2_Mon_ecole_livret_enseignant.pdf')
    print("prof:", T.n)

    return b, T


if __name__ == '__main__':
    build_m2()
