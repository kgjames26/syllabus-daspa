"""Volume 1 · Module 1 — partie C : ateliers, jeux à découper, parcours Alpha."""
import random
from lib.base import *
from lib.art import *
from build.m1_a import CAST_INFO


def wordsearch(words, n=10, seed=7):
    random.seed(seed)
    g = [[None] * n for _ in range(n)]
    placed = {}
    for w in words:
        for _ in range(500):
            d = random.choice([(0, 1), (1, 0)])
            r = random.randrange(n - (len(w) - 1) * d[0])
            c = random.randrange(n - (len(w) - 1) * d[1])
            cells = [(r + i * d[0], c + i * d[1]) for i in range(len(w))]
            if all(g[y][x] in (None, w[i]) for i, (y, x) in enumerate(cells)):
                for i, (y, x) in enumerate(cells):
                    g[y][x] = w[i]
                placed[w] = cells
                break
    alpha = "ABCDEFGHIJLMNOPRSTUVZ"
    sol = {cell for cs in placed.values() for cell in cs}
    full = [[g[y][x] or random.choice(alpha) for x in range(n)] for y in range(n)]
    return full, sol, placed


def ws_html(grid, sol=None, cell=12):
    n = len(grid)
    out = f'<div style="display:grid;grid-template-columns:repeat({n},{cell}mm);gap:0;border:2px solid #1F2A44;width:max-content;margin:auto">'
    for y in range(n):
        for x in range(n):
            hl = "background:#FFD166;" if sol and (y, x) in sol else ""
            out += f'<div style="width:{cell}mm;height:{cell}mm;border:.5px solid #cfd4dd;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:{cell*1.25}pt;{hl}">{grid[y][x]}</div>'
    return out + '</div>'


WS_WORDS = ["BONJOUR", "SALUT", "MERCI", "NOM", "PRENOM", "AGE", "PAYS", "LANGUE", "DIX", "ONZE"]
WS = wordsearch(WS_WORDS)


def build_c(b, E):
    # ================= ATELIER ÉCOUTER-PARLER =================
    ids = [("Sami", "13", "Maroc", "arabe, amazigh", "Liège"), ("Ana", "15", "Brésil", "portugais", "Charleroi"), ("Olek", "14", "Ukraine", "ukrainien", "Namur"),
           ("Merve", "16", "Turquie", "turc", "Mons"), ("Grace", "12", "Congo", "lingala, français", "Namur"), ("Ion", "15", "Roumanie", "roumain", "Liège")]
    idc = "".join(f'''<div style="border:2px dashed #9aa1b1;border-radius:3mm;padding:3mm;background:#FFF6EE"><div style="font-weight:800;color:#E4572E">CARTE D'IDENTITÉ SECRÈTE</div>
<div style="font-size:10.5pt;line-height:1.6">👤 Prénom : <b>{p}</b><br>🎂 Âge : <b>{a} ans</b><br>🌍 Pays : <b>{c}</b><br>🗣️ Langues : <b>{l}</b><br>🏠 Ville : <b>{v}</b></div></div>''' for p, a, c, l, v in ids)
    e1 = E("Le jeu des identités secrètes. Je découpe les cartes. Je tire une carte : je deviens ce personnage ! Mon camarade me pose les 5 questions.",
           f'<div class="grid3">{idc}</div><div class="card mt4"><b>Les questions :</b> Comment tu t\'appelles ? · Tu as quel âge ? · Tu viens d\'où ? · Tu parles quelles langues ? · Tu habites où ?</div>',
           ["decoupe", "parle", "duo"], 2, "A", sol="Jeu oral. Variante ●●● : le camarade ne voit pas la carte et doit noter les réponses, puis présenter le personnage à la classe (« Il s'appelle… »).")
    e2 = E("Je me présente devant la classe (5 phrases). Je m'entraîne d'abord avec mon voisin.", '''<div class="grid5">
<div class="card c">👋<br><span class="sm">Bonjour !</span></div><div class="card c">🙋<br><span class="sm">Je m'appelle…</span></div><div class="card c">🎂<br><span class="sm">J'ai … ans.</span></div>
<div class="card c">🌍<br><span class="sm">Je viens de…</span></div><div class="card c">🗣️<br><span class="sm">Je parle…</span></div></div>''', ["parle", "seul"], 1, "A",
           sol="Production orale évaluée avec la grille « Je me présente » du livret enseignant (préparation de la tâche finale).")
    b.page(f'<span class="atl A" style="font-size:12pt;padding:1.5mm 4mm">{ATELIERS["A"]}</span><h2 class="mt2">Atelier · Écouter et parler</h2>{e1}{e2}', "Atelier")

    # ================= ATELIER LIRE =================
    def post(k, nom, txt, likes):
        return f'''<div class="card" style="border-radius:4mm;padding:3mm"><div class="flex" style="gap:2mm">{avatar(k, 42)}<div><b>{nom}</b><div class="xs muted">MaClasse · DASPA B</div></div></div>
<p class="mt2" style="font-size:10.5pt">{txt}</p><div class="xs muted">❤️ {likes} · 💬 répondre</div></div>'''
    posts = '<div class="grid2">' + post("daria", "Daria K.", "Salut ! Je m'appelle Daria. J'ai 13 ans. Je viens d'Ukraine. J'habite à Namur avec ma maman et mon petit frère. Je parle ukrainien et russe. 🌻", 12) + \
        post("bilal", "Bilal A.", "Bonjour à tous ! Je suis Bilal. J'ai 16 ans. Je viens d'Afghanistan. Je parle dari et pachto. J'aime le football ! ⚽", 9) + \
        post("fatou", "Fatou C.", "Coucou ! Moi, c'est Fatou. J'ai 14 ans. Je viens de Guinée. Je parle peul, soussou et un peu français. J'aime chanter ! 🎤", 15) + \
        post("mateo", "Mateo R.", "Hola… euh, bonjour ! 😄 Je m'appelle Mateo. J'ai 15 ans. Je viens de Colombie. Je parle espagnol. Le français, c'est difficile mais j'aime bien !", 11) + '</div>'
    e3 = E("Je lis les messages sur le réseau de la classe.", posts, ["lis"], 1, "B")
    e4 = E("Qui… ? J'écris le prénom.", f'''<div class="grid2">
<p>1. … aime le football ? {blank()}</p><p>2. … a un petit frère ? {blank()}</p><p>3. … aime chanter ? {blank()}</p><p>4. … parle espagnol ? {blank()}</p>
<p>5. … a le plus de ❤️ ? {blank()}</p><p>6. … est le plus âgé ? {blank()}</p></div>''', ["lis", "ecris"], 2, "B",
           sol="1. Bilal — 2. Daria — 3. Fatou — 4. Mateo — 5. Fatou (15) — 6. Bilal (16 ans)")
    e5 = E("Défi ! Je réponds à un message (2 ou 3 phrases).", f'<div class="flex top">{avatar("amina", 40)}<div class="grow">{lines(3)}</div></div>', ["ecris"], 3, "C",
           sol="Exemple : Salut Fatou ! Moi aussi, j'aime chanter ! Je m'appelle Amina, j'ai 15 ans et je viens de Syrie.")
    b.page(f'<span class="atl B" style="font-size:12pt;padding:1.5mm 4mm">{ATELIERS["B"]}</span><h2 class="mt2">Atelier · Lire</h2>{e3}{e4}{e5}', "Atelier")

    # ================= ATELIER ÉCRIRE =================
    e6 = E("Je recopie la présentation de Yonas.", f'<div class="card" style="background:#F7F8FB"><p class="big">Bonjour ! Je m\'appelle Yonas. J\'ai 14 ans. Je viens d\'Érythrée. Je parle tigrinya.</p></div>{lines(3, True)}',
           ["recopie"], 1, "C", sol="Copie sans erreur ; vérifier majuscules et points.")
    e7 = E("J'écris ma présentation. Je complète.", f'''<div class="card"><p class="big" style="line-height:2.2">Bonjour ! Je m'appelle {blank("l")}.<br>J'ai {blank("s")} ans. Je viens {blank("l")}.<br>
J'habite à {blank("l")}. Je parle {blank("xl")}.</p></div>''', ["ecris", "complete"], 2, "C", sol="Réponses personnelles.")
    e8 = E("Défi ! J'écris une lettre à la prof pour me présenter (5 à 7 phrases). J'ajoute une question pour la prof.", f'<p class="sm muted">Madame, … / Je m\'appelle… / … / Et vous, … ? / Au revoir !</p>{lines(7)}',
           ["ecris"], 3, "C", sol="Production libre. Critères : salutation (Madame), au moins 4 informations, une question au vouvoiement (Vous parlez quelles langues ? Vous habitez où ?), formule finale.")
    b.page(f'<span class="atl C" style="font-size:12pt;padding:1.5mm 4mm">{ATELIERS["C"]}</span><h2 class="mt2">Atelier · Écrire</h2>{e6}{e7}{e8}', "Atelier")

    # ================= ATELIER JOUER : MOTS MÊLÉS + DÉ =================
    grid, sol, _ = WS
    e9 = E("Les mots mêlés. Je trouve les 10 mots (→ et ↓). Je les colorie.", f'{ws_html(grid, cell=11)}<p class="c mt2">{" · ".join(WS_WORDS)}</p>', ["lis", "colorie"], 1, "D",
           sol="Voir la grille corrigée dans le livret enseignant.")
    code = '<div class="card c" style="font-size:9pt;letter-spacing:.5px">' + " · ".join(f"<b>{chr(65+i)}</b>={i+1}" for i in range(26)) + '</div>'
    msgs = [("2 · 15 · 14 · 10 · 15 · 21 · 18", "BONJOUR"), ("13 · 5 · 18 · 3 · 9", "MERCI"), ("19 · 1 · 12 · 21 · 20", "SALUT")]
    e9b = E("Le code secret ! A = 1, B = 2, C = 3… Je décode les mots.", code + '<div class="grid3 mt2">' + "".join(f'<div class="card c"><p class="sm"><b>{m}</b></p><div class="line"></div></div>' for m, _ in msgs) + '</div><p class="sm mt2">●●● J\'écris mon prénom en code : ' + blank("xl") + '</p>',
             ["lis", "ecris"], 2, "D", sol="BONJOUR · MERCI · SALUT")
    b.page(f'<span class="atl D" style="font-size:12pt;padding:1.5mm 4mm">{ATELIERS["D"]}</span><h2 class="mt2">Atelier · Jouer</h2>{e9}{e9b}', "Atelier")

    # dé à découper
    qs = ["Comment tu t'appelles ?", "Tu as quel âge ?", "Tu viens d'où ?", "Tu parles quelles langues ?", "Tu habites où ?", "Ça va ?"]
    emo = ["🙋", "🎂", "🌍", "🗣️", "🏠", "😊"]
    S = 40
    pos = [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2), (1, 3)]
    sq = ""
    for (cx, cy), q, em in zip(pos, qs, emo):
        x, y = 10 + cx * S, 4 + cy * S
        sq += f'<rect x="{x}" y="{y}" width="{S}" height="{S}" fill="#fff" stroke="#1F2A44" stroke-width=".6"/><text x="{x+S/2}" y="{y+17}" font-size="11" text-anchor="middle">{em}</text>'
        words = q.split(" ")
        l1 = " ".join(words[:2]); l2 = " ".join(words[2:])
        sq += f'<text x="{x+S/2}" y="{y+27}" font-size="3.6" text-anchor="middle" font-family="Poppins" font-weight="600">{l1}</text><text x="{x+S/2}" y="{y+32}" font-size="3.6" text-anchor="middle" font-family="Poppins" font-weight="600">{l2}</text>'
    tabs = ""
    for cy in (0, 2, 3):
        y0 = 4 + cy * S
        xl, xr = 10 + S, 10 + 2 * S
        tabs += f'<path d="M{xl} {y0} L{xl-6} {y0+5} L{xl-6} {y0+S-5} L{xl} {y0+S}Z" fill="#eef1f6" stroke="#1F2A44" stroke-width=".4" stroke-dasharray="1.5 1"/>'
        tabs += f'<path d="M{xr} {y0} L{xr+6} {y0+5} L{xr+6} {y0+S-5} L{xr} {y0+S}Z" fill="#eef1f6" stroke="#1F2A44" stroke-width=".4" stroke-dasharray="1.5 1"/>'
    cube = f'<svg viewBox="0 0 140 170" width="118mm" style="display:block;margin:auto">{tabs}{sq}</svg>'
    e10 = E("Le dé des questions. Je découpe, je plie et je colle le dé. Je lance le dé et je pose la question à mon camarade.", cube + '<p class="xs muted c">Les parties grises = les languettes à coller.</p>',
            ["decoupe", "colle", "joue"], 1, "D", sol="Jeu. Le camarade répond par une phrase complète.")
    b.page(f'{e10}', "Atelier")

    # jeu de l'oie
    tasks = ["DÉPART 🚩", "Dis bonjour à ton voisin.", "Compte de 0 à 10.", "Dis ton âge.", "Épelle ton prénom.", "🔙 Recule de 2 cases.", "Dis : « Je ne comprends pas. »",
             "Compte de 10 à 20.", "Dis le nom de ton pays.", "Mime : J'écoute.", "⏩ Avance de 3 cases.", "Dis 3 lettres voyelles.", "Pose une question à un joueur.",
             "Dis : « Au revoir, Madame ! »", "Dis 4 objets de la classe.", "🔙 Retourne au départ !", "Combien font 7 + 8 ?", "Dis ta langue.", "Dis l'alphabet de A à J.",
             "Présente le joueur à ta gauche.", "⏸️ Passe un tour.", "Dis 5 consignes.", "Comment on dit « merci » dans ta langue ?", "Épelle le prénom d'un joueur.", "ARRIVÉE 🏆"]
    cols = 5
    cells = []
    for i, t in enumerate(tasks):
        r, c = divmod(i, cols)
        cc = c if r % 2 == 0 else cols - 1 - c
        color = ["#FFE5DC", "#DDF3EC", "#E1EAFB", "#EEE3FC", "#FFF3C4"][i % 5]
        if i in (0, len(tasks) - 1):
            color = "#FFD166"
        cells.append((r, cc, f'<div style="background:{color};border:2px solid #1F2A44;border-radius:3mm;height:40mm;padding:2mm;position:relative;font-size:10pt;font-weight:600;display:flex;align-items:center;justify-content:center;text-align:center"><span style="position:absolute;top:1mm;left:2mm;font-weight:800;font-size:12pt">{i+1}</span>{t}</div>'))
    cells.sort(key=lambda x: (x[0], x[1]))
    board = '<div style="display:grid;grid-template-columns:repeat(5,1fr);gap:2mm">' + "".join(c[2] for c in cells) + '</div>'
    e11 = E("Le jeu de l'oie « Bonjour ! ». En groupe de 3 ou 4. Un dé, un pion par joueur. Je fais l'action de la case !", board + '<p class="xs muted mt2">Le chemin fait des zigzags : 1 → 5, puis 6 → 10 de droite à gauche, etc.</p>',
            ["joue", "groupe"], 2, "D", sol="Jeu oral. Case 17 : quinze. Les joueurs vérifient entre eux ; la prof arbitre.")
    b.page(f'{e11}', "Atelier")

    # cartes consignes à découper
    keys = list(PICTO_LABEL)
    imp = {"ecoute": "Écoute", "parle": "Parle", "lis": "Lis", "ecris": "Écris", "entoure": "Entoure", "relie": "Relie", "colorie": "Colorie", "coche": "Coche", "souligne": "Souligne",
           "decoupe": "Découpe", "colle": "Colle", "regarde": "Regarde", "repete": "Répète", "seul": "Seul", "duo": "À deux", "groupe": "En groupe", "recopie": "Recopie",
           "complete": "Complète", "barre": "Barre", "montre": "Montre", "dessine": "Dessine", "trace": "Trace", "numerote": "Numérote", "joue": "Joue"}
    cc = "".join(f'<div style="border:1.5px dashed #9aa1b1;height:38mm;display:flex;flex-direction:column;align-items:center;justify-content:center">{picto(k, 70)}<div style="font-weight:700;font-size:12pt;margin-top:1mm">{imp[k]}</div></div>' for k in keys)
    b.page(f'<h2>Les cartes des consignes · à découper</h2><p class="sm">Jeu de mémoire (memory) : imprime deux fois la page. Ou jeu « Jacques a dit ».</p><div style="display:grid;grid-template-columns:repeat(4,1fr);gap:0">{cc}</div>', "Jeu à découper")

    # ================= PARCOURS ALPHA =================
    AL = '<div style="background:#FFD166;margin:-17mm -14mm 4mm -14mm;padding:15mm 14mm 3mm 14mm;display:flex;align-items:center;gap:4mm"><span style="font-size:22pt;font-weight:800">★ ALPHA</span><span class="big">{t}</span></div>'

    # A1 : se repérer + lignes
    def path_ex(a, b_, kind):
        d = {"h": "M20 15 L170 15", "v": "M95 4 L95 46", "o": "M20 30 Q55 0 95 30 T170 30", "z": "M20 40 L50 10 L80 40 L110 10 L140 40 L170 10"}[kind]
        return f'<svg viewBox="0 0 190 50" width="100%" height="24mm"><text x="2" y="24" font-size="16">{a}</text><path d="{d}" fill="none" stroke="#7d8597" stroke-width="1.2" stroke-dasharray="3 2.5"/><text x="172" y="24" font-size="16">{b_}</text><circle cx="20" cy="{15 if kind=="h" else 30 if kind=="o" else 40}" r="2" fill="#2BA88F"/></svg>'
    e12 = E("Je tiens bien mon crayon. Je trace le chemin, sans lever le crayon. ➡️", '<div class="card">' + path_ex("🐱", "🥛", "h") + path_ex("🐝", "🌻", "o") + path_ex("🐰", "🥕", "z") + '</div>',
            ["trace"], 1, alpha=True, sol="Observer la tenue du crayon (pince pouce-index, crayon posé sur le majeur) et le sens gauche → droite.")
    hb = f'''<div class="grid2"><div class="card c"><svg viewBox="0 0 100 80" width="100%" height="48mm"><rect x="2" y="2" width="96" height="76" fill="none" stroke="#1F2A44" stroke-width="1.5"/>
<text x="50" y="16" font-size="12" text-anchor="middle">☀️</text><text x="50" y="74" font-size="12" text-anchor="middle">🌳</text><text x="10" y="45" font-size="12">🐶</text><text x="78" y="45" font-size="12">🐱</text>
<text x="50" y="45" font-size="6" text-anchor="middle" font-family="Poppins">le milieu</text></svg></div>
<div><p class="big">☀️ en <b>haut</b> ⬆️</p><p class="big">🌳 en <b>bas</b> ⬇️</p><p class="big">🐶 à <b>gauche</b> ⬅️</p><p class="big">🐱 à <b>droite</b> ➡️</p>
<p class="sm muted mt2">On lit et on écrit de gauche ➡️ à droite, et de haut ⬇️ en bas.</p></div></div>'''
    e13 = E("Haut, bas, gauche, droite. J'écoute et je montre.", hb, ["ecoute", "montre"], 1, "P", alpha=True,
            script="Montrer l'image : « Le soleil est en haut. Montre en haut ! » etc. Puis consignes : « Mets ton crayon en haut de la page ! À gauche de ton cahier ! » Vérifier que l'élève commence ses lignes à gauche.",
            sol="Activité orale et gestuelle.")
    rain = '<svg viewBox="0 0 190 60" width="100%" height="30mm">' + "".join(f'<text x="{8+i*30}" y="14" font-size="13">☁️</text>' + "".join(f'<path d="M{14+i*30+j*7} 18 L{14+i*30+j*7} 56" stroke="#4A7BD1" stroke-width="1.1" stroke-dasharray="2.5 2"/><circle cx="{14+i*30+j*7}" cy="18" r="1.3" fill="#2BA88F"/>' for j in range(3)) for i in range(6)) + '</svg>'
    e13b = E("La pluie tombe : je trace de haut ⬇️ en bas.", f'<div class="card">{rain}</div>', ["trace"], 1, "C", alpha=True, sol="Traits verticaux de haut en bas, réguliers.")
    b.page(AL.format(t="Je me prépare à écrire") + e12 + e13b + e13, "★ Alpha", color="#E4572E")

    # A2 graphisme
    def pattern(d):
        return f'<svg viewBox="0 0 182 24" width="100%" height="15mm" style="display:block;margin-bottom:2mm"><rect x="0" y="4" width="182" height="16" fill="#EAF4FF"/><line x1="0" y1="20" x2="182" y2="20" stroke="#E4572E" stroke-width=".5"/><path d="{d}" fill="none" stroke="#1F2A44" stroke-width="1.3" stroke-dasharray="2 1.6"/></svg>'
    loops = "M4 20 " + " ".join(f"C{8+i*14} 0 {18+i*14} 0 {18+i*14} 20" for i in range(12))
    waves = "M4 12 " + " ".join(f"Q{11+i*14} {4 if i%2==0 else 20} {18+i*14} 12" for i in range(12))
    pics = "M4 20 " + " ".join(f"L{11+i*14} 4 L{18+i*14} 20" for i in range(12))
    bridges = "M4 20 " + " ".join(f"Q{11+i*14} -2 {18+i*14} 20" for i in range(12))
    circles = "".join(f"M{14+i*16} 12 a6 6 0 1 0 0.01 0 " for i in range(11))
    e14 = E("Je repasse sur les pointillés. Puis je continue seul.", "".join(pattern(d) + guide_lines(1, 18) for d in [pics, bridges, waves, circles, loops]),
            ["trace"], 1, "C", alpha=True, sol="Observer la régularité, la taille (entre les lignes), le sens (les ronds : sens inverse des aiguilles d'une montre, comme pour a, o, d, g).")
    b.page(AL.format(t="Les formes des lettres") + e14, "★ Alpha", color="#E4572E")

    # A3 prénom
    names = ["AMINA", "AMIRA", "AMINA", "ANIMA", "MINA", "AMINA", "ADINA", "AMNIA"]
    e15 = E("La prof écrit mon prénom. Je regarde bien. Je repasse. J'écris.", f'''<div class="card" style="height:28mm;border:3px solid #1F2A44"><span class="xs muted">La prof écrit ici :</span></div>
<p class="mt2 sm">Je repasse et j'écris :</p>{guide_lines(3, 22)}''', ["regarde", "trace", "ecris"], 1, "P", alpha=True,
            sol="La prof écrit le prénom en capitales d'imprimerie (et en minuscules à côté). Objectif d'étape 0–1 : écrire son prénom seul, sans modèle.")
    e16 = E("J'entoure le prénom AMINA, quand c'est exactement le même.", f'<div class="card c" style="font-size:12pt"><span class="pill" style="background:#FFD166;font-size:16pt">AMINA</span></div><div class="grid4 mt2">' +
            "".join(f'<div class="card c" style="font-size:16pt;font-weight:700;letter-spacing:1px">{n}</div>' for n in names) + '</div>', ["regarde", "entoure"], 2, "B", alpha=True,
            sol="AMINA est en 1re, 3e et 6e position (3 fois). Pièges : AMIRA, ANIMA, MINA, ADINA, AMNIA.")
    e17 = E("Je trouve les prénoms de la classe. J'entoure les lettres de mon prénom.", '<div class="grid6">' + "".join(f'<div class="card c" style="font-weight:700">{p.upper()}</div>' for _, p, *_ in CAST_INFO) + '</div>'
            + f'<div class="card c mt2" style="font-size:15pt;letter-spacing:1.2mm;font-weight:700">ABCDEFGHIJKLMNOPQRSTUVWXYZ</div>', ["regarde", "entoure"], 2, alpha=True, sol="Réponses personnelles.")
    b.page(AL.format(t="Mon prénom") + e15 + e16 + e17, "★ Alpha", color="#E4572E")

    # A4-A6 voyelles
    SND = {"A": [("🐱", "chat", 1), ("🛏️", "lit", 0), ("👨", "papa", 1), ("🚲", "vélo", 0), ("👜", "sac", 1), ("🏍️", "moto", 0), ("🍍", "ananas", 1), ("🌙", "lune", 0)],
           "I": [("🛏️", "lit", 1), ("6️⃣", "six", 1), ("🐱", "chat", 0), ("🍕", "pizza", 1), ("🐺", "loup", 0), ("🚲", "vélo", 0), ("🐭", "souris", 1), ("🚌", "bus", 0)],
           "O": [("🚲", "vélo", 1), ("🏍️", "moto", 1), ("🐱", "chat", 0), ("🛏️", "lit", 0), ("🦴", "os", 1), ("🤖", "robot", 1), ("🌙", "lune", 0), ("🍕", "pizza", 0)],
           "U": [("🌙", "lune", 1), ("🚌", "bus", 1), ("🐢", "tortue", 1), ("🐱", "chat", 0), ("🛏️", "lit", 0), ("🧃", "jus", 1), ("🚲", "vélo", 0), ("🏍️", "moto", 0)],
           "É": [("🚲", "vélo", 1), ("🏫", "école", 1), ("👶", "bébé", 1), ("🐱", "chat", 0), ("🛏️", "lit", 0), ("☕", "café", 1), ("🌙", "lune", 0), ("🚌", "bus", 0)]}

    def vowel_page(L, words, distract, extra_title):
        grid_letters = list(L.lower() * 7 + distract)
        random.seed(ord(L))
        random.shuffle(grid_letters)
        gl = "".join(f'<span style="display:inline-block;width:10mm;text-align:center;font-size:20pt;font-weight:600">{c}</span>' for c in grid_letters)
        wc = "".join(f'<div class="card c"><span class="emo">{e}</span><div class="word" style="font-size:13pt">{w.replace(L.lower(), f"<span style=color:#E4572E>{L.lower()}</span>", 1)}</div></div>' for e, w in words)
        ex1 = E(f"La lettre {L.lower()} — {L}. J'écoute, je regarde les mots.", f'<div class="flex"><div style="font-size:72pt;font-weight:800;color:#E4572E;line-height:1;width:55mm" class="c">{L}{L.lower()}</div><div class="grid4 grow">{wc}</div></div>',
                ["ecoute", "regarde"], 1, "P", alpha=True, script=f"Dire le son de la lettre, puis chaque mot en insistant sur le son : {', '.join(w for _, w in words)}. Faire répéter. Faire chercher des prénoms de la classe avec ce son.",
                sol="Activité orale.")
        ex2 = E(f"J'entoure toutes les lettres {L.lower()}.", f'<div class="card" style="line-height:1.6">{gl}</div>', ["entoure"], 1, "B", alpha=True,
                sol=f"Il y a 7 lettres « {L.lower()} ».")
        ex3 = E(f"Je trace {L.lower()} et {L}.", trace(L.lower(), 30, 8) + trace(L, 30, 8) + trace(L.lower() * 2, 30, 4), ["trace"], 1, "C", alpha=True,
                sol=f"Observer le point de départ et le sens du tracé de « {L.lower()} ».")
        lst = SND[L]
        ex4 = E(f"J'écoute le mot. J'entends {L.lower()} ? Je colorie l'image.", '<div class="grid4">' + "".join(f'<div class="card c" style="padding:2mm"><span class="emo s">{e}</span></div>' for e, w, ok in lst) + '</div>',
                ["ecoute", "colorie"], 2, "A", alpha=True, script="Dire chaque mot deux fois : " + ", ".join(w for _, w, _ in lst) + ".",
                sol="Oui : " + ", ".join(w for _, w, ok in lst if ok) + " · Non : " + ", ".join(w for _, w, ok in lst if not ok))
        ex5 = E(f"J'écris {L.lower()} et {L} tout seul, sans modèle.", guide_lines(2, 20), ["ecris"], 2, "C", alpha=True, sol="Écriture autonome ; vérifier la taille et la régularité.")
        return ex1 + ex2 + ex3 + ex4 + ex5

    b.page(AL.format(t="La lettre a") + vowel_page("A", [("🍍", "ananas"), ("✈️", "avion"), ("🐱", "chat"), ("👨", "papa")], "oeuicmnoe", ""), "★ Alpha", color="#E4572E")
    b.page(AL.format(t="La lettre i") + vowel_page("I", [("🏝️", "île"), ("🛏️", "lit"), ("6️⃣", "six"), ("🦎", "iguane")], "lteaujoar", ""), "★ Alpha", color="#E4572E")
    b.page(AL.format(t="La lettre o") + vowel_page("O", [("🍊", "orange"), ("🚲", "vélo"), ("🏍️", "moto"), ("🦴", "os")], "acedauqeb", ""), "★ Alpha", color="#E4572E")
    b.page(AL.format(t="La lettre u") + vowel_page("U", [("🏭", "usine"), ("🌙", "lune"), ("🐢", "tortue"), ("🚌", "bus")], "nvoaenrvo", ""), "★ Alpha", color="#E4572E")
    b.page(AL.format(t="La lettre é") + vowel_page("É", [("🏫", "école"), ("🐘", "éléphant"), ("⭐", "étoile"), ("🚲", "vélo")], "eaoeiuaco", ""), "★ Alpha", color="#E4572E")

    # A révision voyelles
    e18 = E("Je relie la majuscule et la minuscule.", relie([f'<b style="font-size:22pt">{x}</b>' for x in "AIOUÉ"], [f'<b style="font-size:22pt">{x}</b>' for x in "uaéoi"]), ["relie"], 1, "B", alpha=True,
            sol="A–a · I–i · O–o · U–u · É–é")
    imgs = [("🍍", "a"), ("🏝️", "i"), ("🍊", "o"), ("🏫", "é"), ("✈️", "a"), ("🏭", "u")]
    e19 = E("J'écoute le mot. J'entends quel son au début ? J'entoure la lettre.", '<div class="grid3">' + "".join(
        f'<div class="card c"><span class="emo">{e}</span><p class="big" style="letter-spacing:3mm">a i o u é</p></div>' for e, _ in imgs) + '</div>', ["ecoute", "entoure"], 2, "A", alpha=True,
        script="Dire chaque mot en appuyant sur le premier son : ananas, île, orange, école, avion, usine.", sol="ananas a · île i · orange o · école é · avion a · usine u")
    e20 = E("J'écris la lettre qui manque.", '<div class="grid3">' + "".join(f'<div class="card c"><span class="emo">{e}</span><p class="huge">{w}</p></div>' for e, w in [("🛏️", "l _ t"), ("🚲", "vél _"), ("👨", "p _ p _")]) + '</div>',
            ["complete", "ecris"], 3, "C", alpha=True, sol="lit (i) · vélo (o) · papa (a, a)")
    e20b = E("Dictée : la prof dit une voyelle, je l'écris.", guide_lines(2, 20), ["ecoute", "ecris"], 2, "P", alpha=True,
             script="Dicter : a — o — i — é — u — a — i — o (laisser le temps ; montrer la bouche si besoin).", sol="a o i é u a i o")
    b.page(AL.format(t="Je révise les voyelles") + e18 + e19 + e20 + e20b, "★ Alpha", color="#E4572E")

    # A chiffres
    e21 = E("Je trace les chiffres.", "".join(trace(" ".join(str(i) for i in rng), 26, 1, model=False) for rng in [range(0, 6), range(6, 11)]) + "".join(trace(str(i), 28, 7) for i in [1, 4]), ["trace"], 1, "C", alpha=True,
            sol="Vérifier le sens du tracé (le 1 et le 4 commencent en haut ; le 0 tourne comme le o).")
    cnt = [("🍎", 2), ("⭐", 5), ("🐟", 3), ("🌸", 7), ("⚽", 4), ("🎈", 9)]
    e22 = E("Je compte et j'entoure le bon chiffre.", '<div class="grid3">' + "".join(f'<div class="card c"><div style="font-size:17pt">{e*n}</div><p class="big" style="letter-spacing:2mm">{" ".join(str(x) for x in sorted({n, (n+2)%10, (n+5)%10}))}</p></div>' for e, n in cnt) + '</div>',
            ["numerote", "entoure"], 1, "B", alpha=True, sol="🍎 2 · ⭐ 5 · 🐟 3 · 🌸 7 · ⚽ 4 · 🎈 9")
    from build.m1_b import dice
    e22b = E("Je relie le chiffre et le dé.", relie([f'<b style="font-size:22pt">{x}</b>' for x in [3, 5, 1, 6, 2]], [dice(n, 30) for n in [6, 1, 3, 2, 5]]), ["relie"], 1, "B", alpha=True,
             sol="3–⚂ (3 points) · 5–⚄ · 1–⚀ · 6–⚅ · 2–⚁")
    b.page(AL.format(t="Les chiffres de 0 à 10") + e21 + e22 + e22b, "★ Alpha", color="#E4572E")
