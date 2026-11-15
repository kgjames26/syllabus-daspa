import sys
sys.path.insert(0, '/home/claude/syllabus')
from lib.base import *
from lib.art import *
from lib.progression import *
from lib.render import to_pdf, preview

C = "#1F2A44"
b = Book("GUIDE", "Collection FLESco DASPA · Guide général et progression", C, teacher=True)

# ---------- 1. COUVERTURE ----------
cast = "".join(avatar(k, 110, m) for k, m in [("amina", "rire"), ("yonas", "sourire"), ("daria", "sourire"), ("mateo", "rire"), ("bilal", "sourire"), ("fatou", "rire")])
b.page(f'''
<div style="height:297mm;background:linear-gradient(160deg,#1F2A44 0%,#2E4372 60%,#4A7BD1 100%);color:#fff;padding:22mm 18mm;position:relative">
 <div style="font-size:12pt;letter-spacing:3px;opacity:.8;font-weight:600">COLLECTION FLESco · DASPA · SECONDAIRE</div>
 <div style="font-size:46pt;font-weight:800;line-height:1.02;margin-top:14mm">Le français,<br>pas à pas</div>
 <div style="font-size:18pt;margin-top:6mm;opacity:.9">Guide général de l'enseignant<br>et progression des trois volumes</div>
 <div style="display:flex;gap:4mm;margin-top:20mm">
  <div style="background:#E4572E;border-radius:4mm;padding:5mm;flex:1"><div style="font-size:30pt;font-weight:800">1</div><b>Premiers pas</b><br><span style="opacity:.85">Alpha → A1</span></div>
  <div style="background:#2BA88F;border-radius:4mm;padding:5mm;flex:1"><div style="font-size:30pt;font-weight:800">2</div><b>Je me débrouille</b><br><span style="opacity:.85">A2</span></div>
  <div style="background:#4A7BD1;border:2px solid #fff;border-radius:4mm;padding:5mm;flex:1"><div style="font-size:30pt;font-weight:800">3</div><b>Je réussis à l'école</b><br><span style="opacity:.85">B1 + français de scolarisation</span></div>
 </div>
 <div style="position:absolute;bottom:22mm;left:18mm;right:18mm;display:flex;justify-content:space-between;align-items:flex-end">{cast}</div>
</div>''', full=True)

# ---------- 2. BIENVENUE / SOMMAIRE ----------
b.page(f'''
<h1>Bienvenue</h1>
<p class="big" style="max-width:150mm">Cette collection est pensée comme <b>le support unique</b> du cours de français en DASPA : tout ce qu'il faut pour enseigner, faire pratiquer, évaluer et corriger se trouve dans les volumes et leurs livrets enseignant.</p>
<div class="grid2 mt4">
 <div class="card"><h3 style="margin-top:0">Ce que contient chaque module</h3>
 <ul style="margin:0;padding-left:5mm">
 <li>une ouverture illustrée et les objectifs « Je vais apprendre à… »</li>
 <li>un <b>document de la vie réelle</b> comme point de départ</li>
 <li>des leçons <b>📌 À étudier</b> courtes et visuelles</li>
 <li>des exercices à <b>3 niveaux</b> et des <b>ateliers</b> en rotation</li>
 <li>un parcours <b>★ Alpha</b> pour les élèves qui apprennent à lire</li>
 <li>une <b>tâche finale</b> concrète</li>
 <li>des <b>révisions en spirale</b> des modules précédents</li>
 <li>un <b>test</b> avec grille QCM et grille critériée</li>
 </ul></div>
 <div class="card"><h3 style="margin-top:0">Ce que contient le livret enseignant</h3>
 <ul style="margin:0;padding-left:5mm">
 <li>le déroulement conseillé, période par période</li>
 <li>les <b>scripts</b> des activités d'écoute (à lire à voix haute)</li>
 <li>le plan de rotation des ateliers</li>
 <li><b>tous les corrigés</b>, page par page</li>
 <li>la clé QCM prête à encoder dans une appli de correction par scan</li>
 <li>les grilles d'évaluation de l'oral et de l'écrit</li>
 <li>les pistes de différenciation</li>
 </ul></div>
</div>
<h2 class="mt4">Sommaire du guide</h2>
{table(["", "Partie", "Page"], [
 ["1", "Les principes de la collection", "3"],
 ["2", "L'architecture des trois volumes", "4"],
 ["3", "L'anatomie d'un module", "5"],
 ["4", "Les codes visuels (pictogrammes, niveaux, ateliers)", "6"],
 ["5", "La classe flexible : organisation et rotations", "7–8"],
 ["6", "Le parcours ★ Alpha", "9"],
 ["7", "L'évaluation et la correction", "10"],
 ["8", "Progression du volume 1 — Premiers pas", "11–13"],
 ["9", "Progression du volume 2 — Je me débrouille", "14–15"],
 ["10", "Progression du volume 3 — Je réussis à l'école", "16–17"],
 ["11", "La spirale : les notions qui reviennent", "18"],
 ["12", "Calendrier indicatif", "19"],
], ["10mm", "140mm", "20mm"])}
''', "Bienvenue")

# ---------- 3. PRINCIPES ----------
princ = [
    ("🌍", "Partir de la vie réelle", "Chaque module démarre d'un document que l'élève rencontre vraiment : carte d'élève, horaire de bus, ticket de caisse, courrier de la commune. La langue s'apprend parce qu'elle sert tout de suite."),
    ("🎒", "Français de scolarisation dès le premier jour", "L'objectif d'un DASPA est la classe ordinaire. Les consignes, le vocabulaire des disciplines et les gestes scolaires (souligner, justifier, lire un tableau) sont travaillés dès le volume 1, puis approfondis au volume 3."),
    ("🔁", "La spirale plutôt que le survol", "Les notions essentielles reviennent plusieurs fois, à des niveaux croissants. Chaque module contient une page « Je révise » qui reprend les modules précédents. Le tableau de la page 18 montre ces retours."),
    ("⚖️", "Tout n'a pas le même poids", "Les priorités sont claires : l'oral de survie, les consignes, le code écrit et le présent passent avant les subtilités. Le temps consacré à chaque notion suit son utilité réelle pour l'élève."),
    ("🎯", "Une tâche finale à chaque module", "L'élève produit quelque chose d'utile et de visible : un guide de l'école, une affiche, un itinéraire, une invitation. Les exercices préparent cette tâche."),
    ("🪜", "Trois niveaux dans chaque activité", "● découverte, ●● entraînement, ●●● défi. Tous les élèves travaillent la même notion, à leur niveau. Personne n'est bloqué, personne ne s'ennuie."),
    ("👁️", "Voir pour comprendre", "Illustrations, pictogrammes constants, personnages récurrents : l'image porte le sens tant que la langue ne le peut pas encore. Les consignes sont toujours accompagnées de leurs pictogrammes."),
    ("🤝", "Les langues des élèves sont une ressource", "Des rubriques « Dans ma langue » invitent à comparer, traduire, expliquer. Un élève qui sait déjà lire dans sa langue transfère ses stratégies ; un élève non lecteur montre ce qu'il sait à l'oral."),
]
cards = "".join(f'<div class="card" style="border-left:5px solid #4A7BD1"><div class="flex top"><span class="emo s">{e}</span><div><b>{t}</b><p class="sm" style="margin-top:1mm">{d}</p></div></div></div>' for e, t, d in princ)
b.page(f'<h1>1. Les principes</h1><p class="muted mb4">Huit choix pédagogiques qui guident tous les volumes, alignés sur l\'approche FLE + français langue de scolarisation (FLSco) privilégiée en Fédération Wallonie-Bruxelles.</p><div class="grid2">{cards}</div>', "Principes")

# ---------- 4. ARCHITECTURE ----------
vcards = ""
for v, n_mod in zip(VOLUMES, (12, 14, 16)):
    vcards += f'''<div class="card" style="border-top:8px solid {v["couleur"]}">
<div class="flex"><div style="font-size:34pt;font-weight:800;color:{v["couleur"]}">{v["code"][1]}</div>
<div><div style="font-size:15pt;font-weight:700">{v["titre"]}</div><div class="muted">{v["niveau"]} · {n_mod} modules · ± {v["pages"]} pages</div></div></div>
<p class="sm mt2"><b>Pour qui ?</b> {v["public"]}</p><p class="sm"><b>Visée :</b> {v["visee"]}</p></div>'''
flow = '''<svg viewBox="0 0 180 46" width="100%">
<defs><marker id="ar" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0 0 L6 3 L0 6Z" fill="#1F2A44"/></marker></defs>
<rect x="1" y="12" width="28" height="22" rx="3" fill="#EEF1F6" stroke="#1F2A44" stroke-width=".5"/><text x="15" y="21.5" font-size="3.6" text-anchor="middle" font-family="Poppins" font-weight="700">Arrivée</text><text x="15" y="27" font-size="3" text-anchor="middle" font-family="Poppins">test de</text><text x="15" y="30.5" font-size="3" text-anchor="middle" font-family="Poppins">positionnement</text>
<rect x="38" y="4" width="30" height="16" rx="3" fill="#FFD166"/><text x="53" y="11" font-size="3.6" text-anchor="middle" font-family="Poppins" font-weight="700">★ Parcours Alpha</text><text x="53" y="16" font-size="3" text-anchor="middle" font-family="Poppins">(dans le volume 1)</text>
<rect x="38" y="26" width="30" height="16" rx="3" fill="#E4572E"/><text x="53" y="33" font-size="3.8" text-anchor="middle" font-family="Poppins" font-weight="700" fill="#fff">Volume 1</text><text x="53" y="38" font-size="3" text-anchor="middle" font-family="Poppins" fill="#fff">Alpha → A1</text>
<rect x="78" y="15" width="28" height="16" rx="3" fill="#2BA88F"/><text x="92" y="22" font-size="3.8" text-anchor="middle" font-family="Poppins" font-weight="700" fill="#fff">Volume 2</text><text x="92" y="27" font-size="3" text-anchor="middle" font-family="Poppins" fill="#fff">A2</text>
<rect x="116" y="15" width="28" height="16" rx="3" fill="#4A7BD1"/><text x="130" y="22" font-size="3.8" text-anchor="middle" font-family="Poppins" font-weight="700" fill="#fff">Volume 3</text><text x="130" y="27" font-size="3" text-anchor="middle" font-family="Poppins" fill="#fff">B1 + FLSco</text>
<rect x="152" y="12" width="27" height="22" rx="3" fill="#1F2A44"/><text x="165.5" y="21.5" font-size="3.6" text-anchor="middle" font-family="Poppins" font-weight="700" fill="#fff">Classe</text><text x="165.5" y="26.5" font-size="3.6" text-anchor="middle" font-family="Poppins" font-weight="700" fill="#fff">ordinaire</text>
<path d="M29 20 L37 13" stroke="#1F2A44" stroke-width=".6" marker-end="url(#ar)"/><path d="M29 27 L37 33" stroke="#1F2A44" stroke-width=".6" marker-end="url(#ar)"/><path d="M53 20 L53 25" stroke="#1F2A44" stroke-width=".6" marker-end="url(#ar)"/>
<path d="M68 33 L77 26" stroke="#1F2A44" stroke-width=".6" marker-end="url(#ar)"/><path d="M106 23 L115 23" stroke="#1F2A44" stroke-width=".6" marker-end="url(#ar)"/><path d="M144 23 L151 23" stroke="#1F2A44" stroke-width=".6" marker-end="url(#ar)"/>
<path d="M29 23 Q55 -2 88 14" stroke="#1F2A44" stroke-width=".4" stroke-dasharray="1.5 1" fill="none" marker-end="url(#ar)"/>
</svg>'''
b.page(f'''<h1>2. Trois volumes = trois niveaux</h1>
<p class="muted">Les volumes correspondent à des <b>niveaux de langue</b>, pas à des années scolaires. Un élève entre dans le volume qui correspond à son niveau et avance à son rythme ; un élève déjà scolarisé et rapide peut passer du volume 1 au volume 2 en quelques mois.</p>
<div class="card mt4 mb4">{flow}<p class="xs muted c">Le pointillé : un élève qui arrive avec de bonnes bases (langue latine, scolarité solide) peut entrer directement dans le volume 2 après le test de positionnement.</p></div>
<div style="display:flex;flex-direction:column;gap:4mm">{vcards}</div>
<div class="astuce mt4"><b>Volume et classe flexible :</b> dans une même salle, des élèves des volumes 1, 2 et 3 peuvent travailler en même temps. Les modules des trois volumes sont alignés par grands thèmes (l'école, la santé, la ville…) pour permettre des moments communs à l'oral.</div>
''', "Architecture")

# ---------- 5. ANATOMIE ----------
steps = [
    ("#E4572E", "Ouverture", "1 p.", "Grande illustration, objectifs « Je vais apprendre à… », mots-clés. On observe, on parle, on fait des hypothèses."),
    ("#F29E4C", "Document de la vie", "2–3 p.", "Un document réaliste (fictif mais fidèle) : on le découvre, on repère, on comprend."),
    ("#F2B705", "Découvrir", "3–4 p.", "Compréhension guidée, oral puis écrit, avec les personnages récurrents."),
    ("#2BA88F", "📌 Leçons à étudier", "3–5 p.", "Encadrés jaunes : ce que l'élève doit savoir par cœur. Courts, illustrés, à relire à la maison."),
    ("#4A7BD1", "S'entraîner", "8–12 p.", "Exercices variés à 3 niveaux : relier, entourer, compléter, classer, jeux, mots croisés, images à décrire."),
    ("#9B5DE5", "Ateliers", "4–6 p.", "Fiches autonomes pour les 4 pôles : 🎧 Écouter-Parler, 📖 Lire, ✏️ Écrire, 🧩 Jouer."),
    ("#FFD166", "★ Parcours Alpha", "6–10 p.", "Graphisme, lettres, sons, syllabes, pour les élèves qui apprennent à lire et à écrire."),
    ("#C94F7C", "Consignes & FLSco", "1–2 p.", "Les gestes et mots de l'école, de plus en plus complexes."),
    ("#1F2A44", "Tâche finale", "2 p.", "Le projet concret qui mobilise tout le module."),
    ("#5E6B85", "Je révise · Test · Je sais faire", "5–6 p.", "Révision spirale, test noté avec grille QCM, autoévaluation."),
]
rows = "".join(f'<div class="flex mb2" style="gap:3mm"><div style="background:{c};width:6mm;height:16mm;border-radius:2mm"></div><div style="width:48mm"><b>{t}</b><div class="xs muted">{p}</div></div><div class="sm grow">{d}</div></div>' for c, t, p, d in steps)
b.page(f'''<h1>3. L'anatomie d'un module</h1>
<p class="muted mb4">Tous les modules suivent la même structure. Les élèves s'y repèrent vite, ce qui est essentiel en classe flexible : chacun sait où il en est et ce qui vient ensuite.</p>
{rows}
<div class="attention mt4"><b>Volume des modules.</b> Volume 1 : ± 45 pages par module (12 modules + annexes = ± 600 p.). Volume 2 : ± 52 pages (14 modules = ± 800 p.). Volume 3 : ± 58 pages (16 modules = ± 1 000 p.). Le livret enseignant de chaque module (corrigés, scripts, déroulement) s'ajoute à ces pages.</div>''', "Anatomie d'un module")

# ---------- 6. CODES VISUELS ----------
b.page(f'''<h1>4. Les codes visuels</h1>
<h2>Les 24 pictogrammes de consignes</h2>
<p class="sm">Ils sont enseignés dans le module 1 du volume 1 et accompagnent <b>chaque consigne</b> de la collection. Au volume 3, ils s'effacent progressivement : l'élève doit alors comprendre la consigne écrite seule.</p>
<div class="card mb4">{picto_legend(list(PICTO_LABEL))}</div>
<h2>Les niveaux de difficulté</h2>
<div class="grid3 mb4">
<div class="card"><b>{dots(1)} Découverte</b><p class="sm">Avec appui visuel fort, modèle donné, choix limité. Tout élève doit réussir.</p></div>
<div class="card"><b>{dots(2)} Entraînement</b><p class="sm">Le cœur de la notion. L'élève applique seul.</p></div>
<div class="card"><b>{dots(3)} Défi</b><p class="sm">Transfert, production plus libre, réflexion sur la langue. Pour aller plus loin.</p></div>
</div>
<h2>Les pôles d'ateliers</h2>
<div class="grid2 mb4">
<div class="card"><span class="atl A">{ATELIERS["A"]}</span><p class="sm mt2">Dialogues, jeux de rôle, écoute de scripts lus par un élève ou la prof, enregistrements sur tablette si disponible.</p></div>
<div class="card"><span class="atl B">{ATELIERS["B"]}</span><p class="sm mt2">Lecture de documents, compréhension, coin lecture.</p></div>
<div class="card"><span class="atl C">{ATELIERS["C"]}</span><p class="sm mt2">Copie, production guidée, production libre.</p></div>
<div class="card"><span class="atl D">{ATELIERS["D"]}</span><p class="sm mt2">Cartes, dominos, lotos, mots croisés, jeux de plateau à découper.</p></div>
</div>
<div class="flex"><span class="alpha-tag" style="font-size:11pt">★ ALPHA</span><span class="sm">Activité du parcours d'alphabétisation (voir p. 9). Les autres élèves peuvent la sauter ou l'utiliser comme remédiation en écriture.</span></div>
<div class="flex mt2"><span class="atl P" style="font-size:10pt">{ATELIERS["P"]}</span><span class="sm">Activité qui se fait à la table d'appui, en petit groupe, avec l'enseignante.</span></div>''', "Codes visuels")

# ---------- 7. CLASSE FLEXIBLE 1 ----------
plan = '''<svg viewBox="0 0 180 110" width="100%">
<rect x="1" y="1" width="178" height="108" rx="3" fill="#FAFBFD" stroke="#1F2A44" stroke-width=".8"/>
<rect x="60" y="2" width="60" height="4" fill="#2F5D50"/><text x="90" y="10" font-size="3.2" text-anchor="middle" font-family="Poppins">tableau</text>
<g><rect x="70" y="40" width="40" height="22" rx="11" fill="#1F2A44"/><text x="90" y="50" font-size="3.6" fill="#fff" text-anchor="middle" font-family="Poppins" font-weight="700">TABLE D'APPUI</text><text x="90" y="55" font-size="3" fill="#fff" text-anchor="middle" font-family="Poppins">avec l'enseignante</text></g>
<g><rect x="8" y="14" width="44" height="30" rx="4" fill="#FDE3DB" stroke="#E4572E" stroke-width=".8"/><text x="30" y="27" font-size="4" text-anchor="middle" font-family="Poppins" font-weight="700" fill="#E4572E">🎧 Écouter-Parler</text><text x="30" y="33" font-size="3" text-anchor="middle" font-family="Poppins">îlot calme, casques</text></g>
<g><rect x="128" y="14" width="44" height="30" rx="4" fill="#E1EAFB" stroke="#4A7BD1" stroke-width=".8"/><text x="150" y="27" font-size="4" text-anchor="middle" font-family="Poppins" font-weight="700" fill="#4A7BD1">📖 Lire</text><text x="150" y="33" font-size="3" text-anchor="middle" font-family="Poppins">coin lecture, coussins</text></g>
<g><rect x="8" y="64" width="44" height="34" rx="4" fill="#DDF3EC" stroke="#2BA88F" stroke-width=".8"/><text x="30" y="79" font-size="4" text-anchor="middle" font-family="Poppins" font-weight="700" fill="#2BA88F">✏️ Écrire</text><text x="30" y="85" font-size="3" text-anchor="middle" font-family="Poppins">tables individuelles</text></g>
<g><rect x="128" y="64" width="44" height="34" rx="4" fill="#EEE3FC" stroke="#9B5DE5" stroke-width=".8"/><text x="150" y="79" font-size="4" text-anchor="middle" font-family="Poppins" font-weight="700" fill="#9B5DE5">🧩 Jouer</text><text x="150" y="85" font-size="3" text-anchor="middle" font-family="Poppins">grande table, jeux</text></g>
<g><rect x="66" y="80" width="48" height="22" rx="3" fill="#FFF3C4" stroke="#F2B705" stroke-width=".8"/><text x="90" y="90" font-size="3.6" text-anchor="middle" font-family="Poppins" font-weight="700">Mur des ressources</text><text x="90" y="95.5" font-size="3" text-anchor="middle" font-family="Poppins">affiches, corrigés autonomes, bacs</text></g>
<path d="M52 30 Q90 18 128 30" stroke="#1F2A44" stroke-width=".5" fill="none" stroke-dasharray="1.5 1"/><path d="M150 44 L150 64" stroke="#1F2A44" stroke-width=".5" stroke-dasharray="1.5 1"/><path d="M128 82 Q90 68 52 82" stroke="#1F2A44" stroke-width=".5" fill="none" stroke-dasharray="1.5 1"/><path d="M30 64 L30 44" stroke="#1F2A44" stroke-width=".5" stroke-dasharray="1.5 1"/>
<text x="90" y="25" font-size="3" text-anchor="middle" font-family="Poppins" fill="#555">rotation ↻</text>
</svg>'''
b.page(f'''<h1>5. La classe flexible</h1>
<p class="muted">L'école combine trois modes d'organisation. La collection est construite pour les trois, et pour passer de l'un à l'autre dans la même semaine.</p>
<div class="grid3 mb4">
<div class="card" style="border-top:6px solid #E4572E"><b>Mode 1 · Ateliers en rotation</b><p class="sm">4 pôles + table d'appui. Les groupes tournent toutes les 20 à 25 minutes. Chaque module fournit les fiches des 4 pôles.</p></div>
<div class="card" style="border-top:6px solid #2BA88F"><b>Mode 2 · Groupes de besoins</b><p class="sm">Les élèves sont regroupés selon leur niveau (volume, parcours Alpha). Les groupes changent après chaque bilan.</p></div>
<div class="card" style="border-top:6px solid #4A7BD1"><b>Mode 3 · Plan de travail</b><p class="sm">Chaque élève a sa feuille de route du module et avance à son rythme. L'enseignante circule et anime la table d'appui.</p></div>
</div>
<h2>Exemple d'aménagement de la salle</h2>
<div class="card mb4">{plan}</div>
<div class="astuce"><b>Le mur des ressources</b> rassemble les affiches des leçons (les encadrés 📌 agrandis), les pictogrammes de consignes, l'alphabet, les nombres et une boîte de <b>corrigés autonomes</b> pour les exercices ●. Les élèves s'autocorrigent au stylo vert : l'enseignante garde son temps pour la table d'appui.</div>''', "Classe flexible")

# ---------- 8. CLASSE FLEXIBLE 2 ----------
rot = table(["Temps", "Groupe 1 (Alpha)", "Groupe 2 (V1 lecteurs)", "Groupe 3 (V1 avancés)", "Groupe 4 (V2/V3)"], [
    ["0–10 min", "Rituel commun : date, météo, « Quoi de neuf ? », mot du jour", "", "", ""],
    ["10–30", "👩‍🏫 Table d'appui", "🧩 Jouer", "✏️ Écrire", "📖 Lire"],
    ["30–50", "🧩 Jouer", "👩‍🏫 Table d'appui", "📖 Lire", "✏️ Écrire"],
    ["50–70", "🎧 Écouter-Parler", "📖 Lire", "👩‍🏫 Table d'appui", "🧩 Jouer"],
    ["70–90", "✏️ Écrire (★ Alpha)", "🎧 Écouter-Parler", "🧩 Jouer", "👩‍🏫 Table d'appui"],
    ["90–100", "Bilan commun : « Qu'est-ce que j'ai appris ? » + plan de travail mis à jour", "", "", ""],
], ["18mm", "40mm", "40mm", "40mm", "40mm"])
rot = rot.replace("<td>Rituel commun", '<td colspan="4">Rituel commun').replace("<td></td><td></td><td></td></tr>", "</tr>", 1)
rot = rot.replace("<td>Bilan commun", '<td colspan="4">Bilan commun').replace("<td></td><td></td><td></td></tr>", "</tr>", 1)
b.page(f'''<h1>Rotation type (2 périodes)</h1>
<p class="muted mb4">Le groupe Alpha passe <b>en premier</b> à la table d'appui, quand l'attention est maximale. Le pôle 🎧 se place loin du pôle 📖.</p>
{rot}
<h2 class="mt4">Le plan de travail</h2>
<p class="sm">Au début de chaque module, l'élève reçoit sa feuille de route (fournie dans le module). Il y coche les exercices faits, colorie son niveau atteint et note les leçons à étudier. C'est l'outil central du mode 3 et le lien avec les parents.</p>
<h2 class="mt4">Quand un élève change-t-il de groupe ?</h2>
{table(["Situation", "Décision"], [
 ["Réussite ≥ 80 % au test de module et aux tâches ●●●", "Passe au groupe supérieur ou avance d'un module en autonomie"],
 ["Réussite entre 50 et 80 %", "Reste dans son groupe ; fiches de remédiation ciblées"],
 ["Réussite < 50 %", "Table d'appui renforcée ; reprise des pages ● ; vérifier le parcours Alpha"],
 ["Élève Alpha qui atteint l'étape 4 (lecture de phrases)", "Rejoint le groupe « V1 lecteurs » pour l'écrit"],
 ["Fin du volume 1 + bilan A1 réussi", "Entre dans le volume 2"],
], ["90mm", "92mm"])}
<div class="astuce mt4"><b>Accueil d'un nouvel élève en cours d'année :</b> test de positionnement (annexe du volume 1), puis module 1 en autonomie avec un « parrain » de la classe. Le module 1 de chaque volume est conçu pour être fait à tout moment de l'année.</div>''', "Classe flexible")

# ---------- 9. ALPHA ----------
etapes = [
    ("0", "Entrer dans l'écrit", "Tenir un crayon, tracer des lignes et des formes, se repérer sur la page (haut, bas, gauche, droite), reconnaître son prénom."),
    ("1", "Les voyelles et les premiers mots", "a, i, o, u, e, é ; reconnaître des mots-images ; recopier son prénom."),
    ("2", "Consonnes continues et syllabes", "m, l, s, r, f, v, n ; combiner consonne + voyelle (ma, li, so) ; lire des syllabes."),
    ("3", "Consonnes occlusives et premiers mots lus", "p, t, d, b, c, g ; lire des mots de 2 syllabes ; écrire sous dictée de syllabes."),
    ("4", "Les sons complexes et la phrase", "ou, on, an, in, oi, ch, gn ; lire et écrire une phrase simple."),
    ("5", "Lecteur débutant", "Lire un petit texte, comprendre un document simple : rejoint le groupe des lecteurs."),
]
et = "".join(f'<div class="flex mb2"><div style="background:#FFD166;min-width:13mm;height:13mm;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:15pt">{n}</div><div><b>{t}</b><div class="sm">{d}</div></div></div>' for n, t, d in etapes)
b.page(f'''<h1>6. Le parcours ★ Alpha</h1>
<p class="muted mb4">Certains élèves n'ont jamais été scolarisés ou écrivent dans un autre alphabet. Le parcours Alpha est <b>intégré dans le volume 1</b> : ces élèves suivent les mêmes thèmes et les mêmes activités orales que les autres, mais leurs pages d'écrit sont spécifiques.</p>
<div class="grid2">
<div>{et}</div>
<div>
<div class="card mb4"><b>Les principes du parcours</b><ul class="sm" style="padding-left:5mm;margin:1mm 0">
<li>L'oral d'abord : on n'écrit que des mots que l'élève comprend et sait dire.</li>
<li>Méthode syllabique explicite, très progressive, avec beaucoup de répétition.</li>
<li>Police sans empattement avec <b>a</b> et <b>g</b> d'écriture (Poppins), grande taille, lignes guides colorées.</li>
<li>Les mots du thème du module servent de mots-repères (ex. module 1 : <i>ami, papa, Amina</i>).</li>
<li>Écriture script d'abord ; l'écriture liée est proposée en option au volume 2.</li>
</ul></div>
<div class="card mb4"><b>Les profils différents</b><ul class="sm" style="padding-left:5mm;margin:1mm 0">
<li><b>Non scolarisé :</b> tout le parcours depuis l'étape 0.</li>
<li><b>Lecteur d'un autre alphabet</b> (arabe, cyrillique, tigrinya…) : entre à l'étape 1 ou 2 ; il connaît le principe de l'écrit, il doit apprendre un nouveau code et le sens gauche → droite pour certains.</li>
<li><b>Peu scolarisé, alphabet latin</b> (ex. Guinée, Brésil) : commence souvent à l'étape 2 ou 3.</li>
</ul></div>
<div class="attention"><b>Point de vigilance :</b> ne pas confondre difficulté de lecture et difficulté de compréhension. Un élève Alpha peut être très avancé à l'oral : il participe pleinement aux activités 🎧.</div>
</div></div>
<h2 class="mt4">Où se trouvent les étapes dans le volume 1 ?</h2>
{table(["Étape", "Modules", "Repère de réussite (fin d'étape)"], [
 ["0 – 1", "M1", "Écrit son prénom seul ; reconnaît et trace a, i, o, u, e"],
 ["2", "M2 – M3", "Lit 20 syllabes simples ; recopie un mot sans modèle à côté"],
 ["3", "M3 – M5", "Lit des mots de 2 syllabes ; écrit 10 mots du thème sous dictée"],
 ["4", "M6 – M9", "Lit une phrase de 5 à 7 mots ; écrit une phrase simple"],
 ["5", "M10 – M12", "Lit un texte de 5 phrases et répond à 3 questions"],
], ["20mm", "30mm", "132mm"])}
<p class="sm muted mt2">Un élève peut avancer plus vite : les pages ★ de tous les modules restent accessibles dans le volume ; le plan de travail indique où il en est.</p>''', "Parcours Alpha")

# ---------- 10. EVALUATION ----------
b.page(f'''<h1>7. Évaluer et corriger</h1>
{table(["Outil", "Quand ?", "Ce qu'il évalue", "Correction"], [
 ["Test de positionnement", "À l'arrivée de l'élève", "Oral, lecture, écriture, scolarité antérieure", "Grille rapide (annexe V1)"],
 ["Exercices ●", "Pendant le module", "Notion en cours", "Autocorrection (corrigés au mur)"],
 ["Exercices ●● et ●●●", "Pendant le module", "Application et transfert", "Livret enseignant"],
 ["Tâche finale", "Fin du module", "Compétence globale", "Grille critériée fournie"],
 ["Test de module", "Fin du module", "Compréhension + langue (QCM) et production", "QCM : scan ; production : grille"],
 ["Bilan trimestriel", "Après M3, M6, M9, M12", "Toutes les notions depuis le début (spirale)", "QCM : scan ; oral : grille"],
 ["Je sais faire", "Fin du module", "Autoévaluation", "L'élève, puis échange avec l'enseignante"],
], ["36mm", "34mm", "62mm", "50mm"])}
<h2 class="mt4">La correction par scan (QCM)</h2>
<p class="sm">Chaque test commence par une partie QCM (réponses A, B, C, D). Le livret enseignant donne la <b>clé de correction</b> sous la forme « 1-B, 2-D, 3-A… », prête à être encodée dans une application de correction par photo comme <b>ZipGrade</b> (application pour smartphone).</p>
<div class="grid2 mb4">
<div class="card"><b>Mode d'emploi</b><ol class="sm" style="padding-left:5mm;margin:1mm 0">
<li>Dans l'application, créer un « quiz » par test (même nombre de questions).</li>
<li>Encoder la clé donnée dans le livret enseignant.</li>
<li>Imprimer les feuilles-réponses de l'application et les distribuer avec le test.</li>
<li>Les élèves reportent leurs réponses (cases à noircir) — un entraînement est prévu dans le module 1.</li>
<li>Photographier chaque feuille : la note s'affiche immédiatement.</li>
</ol></div>
<div class="card"><b>Ce qui reste à corriger à la main</b><p class="sm">Les productions écrites et orales ne peuvent pas être corrigées automatiquement : c'est là que l'évaluation a le plus de valeur. Pour aller vite, chaque production a une <b>grille critériée</b> (3 à 5 critères, cases à cocher) et des exemples de réponses attendues dans le livret enseignant.</p>
<p class="sm"><b>Élèves ★ Alpha :</b> leurs tests sont surtout oraux et à images ; la prof coche la grille pendant la passation.</p></div>
</div>
<div class="attention"><b>Remarque :</b> l'application de scan et ses feuilles-réponses ne font pas partie de la collection ; les tests fonctionnent aussi sur papier, avec la clé du livret.</div>''', "Évaluation")


# ---------- 11-12. V1 ----------
def v1_table(mods, start):
    rows = []
    for i, m in enumerate(mods, start):
        t, com, lex, gram, phon, alpha, doc, fl, tache = m
        rows.append([f'<b style="font-size:13pt">{i}</b>', f'<b>{t}</b><div class="xs muted">{doc}</div>', f'<span class="xs">{com}</span>',
                     f'<span class="xs"><b>Lex.</b> {lex}<br><b>Gram.</b> {gram}</span>', f'<span class="xs"><b>Oral/code :</b> {phon}<br><b>★</b> {alpha}<br><b>FLSco :</b> {fl}</span>', f'<span class="xs">{tache}</span>'])
    return table(["M", "Thème · document de vie", "Communication", "Lexique · grammaire", "Phonétique · Alpha · FLSco", "Tâche finale"], rows, ["7mm", "34mm", "32mm", "42mm", "42mm", "25mm"])


b.page(f'<h1 style="color:#E4572E">8. Volume 1 · Premiers pas</h1><p class="muted">Alpha → A1 · 12 modules · bilans trimestriels après les modules 3, 6, 9 et 12.</p>{v1_table(V1[:4], 1)}', "Progression V1", color="#E4572E")
b.page(f'{v1_table(V1[4:8], 5)}', "Progression V1", color="#E4572E")
b.page(f'{v1_table(V1[8:], 9)}<div class="lecon mt4"><div class="lt">ANNEXES DU VOLUME 1</div><p class="sm">Test de positionnement · 4 bilans trimestriels · imagier général (± 600 mots) · tableaux de conjugaison illustrés · lexique « dans ma langue » à compléter par l\'élève · jeux à découper (lotos, dominos, cartes) · certificat de fin de volume.</p></div>', "Progression V1", color="#E4572E")


def vx_table(mods, color, start=1):
    rows = [[f'<b>{i}</b>', f'<b>{t}</b>', f'<span class="xs">{com}</span>', f'<span class="xs"><b>Lex.</b> {lex}<br><b>Gram.</b> {gram}</span>', f'<span class="xs">{doc}</span>', f'<span class="xs">{fl}</span>', f'<span class="xs">{tache}</span>']
            for i, (t, com, lex, gram, doc, fl, tache) in enumerate(mods, start)]
    return table(["M", "Thème", "Communication", "Lexique · grammaire", "Document de vie", "FLSco", "Tâche finale"], rows, ["6mm", "24mm", "30mm", "40mm", "30mm", "28mm", "24mm"]).replace('class="t"','class="t compact"')


b.page(f'<h1 style="color:#2BA88F">9. Volume 2 · Je me débrouille</h1><p class="muted">A2 · 14 modules · ± 800 pages · bilans après les modules 4, 7, 11 et 14.</p>{vx_table(V2[:7], "#2BA88F")}', "Progression V2", color="#2BA88F")
b.page(vx_table(V2[7:], "#2BA88F", 8), "Progression V2", color="#2BA88F")
b.page(f'<h1 style="color:#4A7BD1">10. Volume 3 · Je réussis à l\'école</h1><p class="muted">B1 + français de scolarisation · 16 modules · ± 1 000 pages · bilans après les modules 4, 8, 12 et 16 · préparation au DELF A2/B1.</p>{vx_table(V3[:7], "#4A7BD1")}', "Progression V3", color="#4A7BD1")
b.page(vx_table(V3[7:], "#4A7BD1", 8), "Progression V3", color="#4A7BD1")

# ---------- 15. SPIRALE ----------
sp = table(["Notion", "Où elle revient (niveau croissant)"], [[f"<b>{n}</b>", " → ".join(w)] for n, w in SPIRALE], ["50mm", "132mm"])
b.page(f'''<h1>11. La spirale</h1>
<p class="muted mb4">Certaines notions sont trop importantes pour être vues une seule fois. Elles reviennent, à chaque fois plus loin. Chaque module contient aussi une page « 🔁 Je révise » qui reprend 3 notions des modules précédents.</p>
{sp}
<h2 class="mt4">La hiérarchie des priorités</h2>
<div class="grid3">
<div class="card" style="border-top:6px solid #E4572E"><b>Priorité 1 — vital</b><p class="sm">Se présenter, consignes, demander de l'aide, urgences, nombres, heure, code écrit de base, présent. <b>Travaillé dans chaque module.</b></p></div>
<div class="card" style="border-top:6px solid #F2B705"><b>Priorité 2 — essentiel</b><p class="sm">Passé composé, futur proche, négation, questions, lexique thématique, documents administratifs. <b>Revu 3 à 5 fois.</b></p></div>
<div class="card" style="border-top:6px solid #2BA88F"><b>Priorité 3 — enrichissement</b><p class="sm">Nuances, registres, figures de style, temps littéraires. <b>Abordé quand les bases sont solides.</b></p></div>
</div>''', "Spirale")

# ---------- 16. CALENDRIER ----------
cal = table(["Période", "Volume 1 (12 modules)", "Volume 2 (14 modules)", "Volume 3 (16 modules)"], [
    ["Fin août → congé d'automne", "M1 – M2", "M1 – M3", "M1 – M3"],
    ["Automne → congé d'hiver", "M3 – M4 + bilan 1", "M4 – M5 + bilan 1", "M4 – M6 + bilan 1"],
    ["Hiver → congé de détente", "M5 – M6 + bilan 2", "M6 – M7 + bilan 2", "M7 – M8 + bilan 2"],
    ["Détente → congé de printemps", "M7 – M9 + bilan 3", "M8 – M11 + bilan 3", "M9 – M12 + bilan 3"],
    ["Printemps → fin juin", "M10 – M12 + bilan 4", "M12 – M14 + bilan 4", "M13 – M16 + bilan 4"],
], ["48mm", "44mm", "45mm", "45mm"])
b.page(f'''<h1>12. Calendrier indicatif</h1>
<p class="muted mb4">Repères pour une classe qui suivrait un volume sur une année scolaire complète (calendrier de la Fédération Wallonie-Bruxelles avec congés d'automne, d'hiver, de détente et de printemps de deux semaines). En classe flexible, chaque élève avance à son rythme : ces repères servent surtout à vérifier qu'un groupe n'est pas en retard.</p>
{cal}
<h2 class="mt4">Une semaine type dans un module</h2>
{table(["Jour", "Contenu"], [
 ["1", "Ouverture + document de la vie (collectif, oral)"],
 ["2", "Découvrir + première leçon 📌"],
 ["3–6", "Entraînement et ateliers en rotation ; parcours ★ Alpha en parallèle"],
 ["7", "Consignes & FLSco + 🔁 Je révise"],
 ["8–9", "Tâche finale (en groupes)"],
 ["10", "Test + Je sais faire ; mise à jour du plan de travail"],
], ["20mm", "162mm"])}
<p class="sm muted mt2">Un module du volume 1 représente environ 10 journées de cours de français (± 3 semaines).</p>''', "Calendrier")

to_pdf(b.html(), '/home/claude/syllabus/out/00_Guide_general_et_progression.pdf')
print("pages", b.n)
