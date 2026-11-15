"""Volume 1 · Module 1 — partie B : être/avoir, nombres, alphabet, sons, matériel, ateliers, jeux."""
import random
from lib.base import *
from lib.art import *

NUM = ["zéro", "un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf", "dix", "onze", "douze", "treize", "quatorze", "quinze", "seize", "dix-sept", "dix-huit", "dix-neuf", "vingt"]


def dice(n, size=40):
    pos = {1: [(20, 20)], 2: [(11, 11), (29, 29)], 3: [(10, 10), (20, 20), (30, 30)], 4: [(11, 11), (29, 11), (11, 29), (29, 29)],
           5: [(11, 11), (29, 11), (20, 20), (11, 29), (29, 29)], 6: [(11, 10), (29, 10), (11, 20), (29, 20), (11, 30), (29, 30)]}
    d = "".join(f'<circle cx="{x}" cy="{y}" r="3.6" fill="#1F2A44"/>' for x, y in pos.get(n, []))
    return f'<svg viewBox="0 0 40 40" width="{size}" height="{size}"><rect x="2" y="2" width="36" height="36" rx="7" fill="#fff" stroke="#1F2A44" stroke-width="2"/>{d}</svg>'


def build_b(b, E):
    # ================= LEÇON 4 : ÊTRE ET AVOIR =================
    l5 = lecon("Les verbes être et avoir", f'''
<div class="grid2">
<div class="card" style="background:#fff"><h3 style="margin:0 0 2mm 0;color:#4A7BD1">ÊTRE</h3>
<p class="big">je <b>suis</b></p><p class="big">tu <b>es</b></p><p class="big">il / elle <b>est</b></p>
<p class="sm muted mt2">Je suis Mateo. Je suis en classe. Tu es gentil. Elle est prof.</p></div>
<div class="card" style="background:#fff"><h3 style="margin:0 0 2mm 0;color:#E4572E">AVOIR</h3>
<p class="big">j'<b>ai</b></p><p class="big">tu <b>as</b></p><p class="big">il / elle <b>a</b></p>
<p class="sm muted mt2">J'ai 14 ans. Tu as un crayon. Il a un livre.</p></div></div>
<div class="grid2 mt2">
<div class="astuce" style="margin:0"><b>je → j'</b> devant une voyelle :<br>j'ai · j'habite · j'écoute · j'aime</div>
<div class="attention" style="margin:0"><b>L'âge = AVOIR</b><br>Il <b>a</b> 16 ans. ✅ &nbsp; Il <s>est</s> 16 ans. ❌</div></div>''')
    e = E("Je complète avec suis, es, est.", f'''<div class="grid2">
<p>1. Je {blank("s")} Amina.</p><p>2. Tu {blank("s")} en classe.</p><p>3. Elle {blank("s")} la prof.</p><p>4. Mme Lambert {blank("s")} gentille.</p></div>''', ["complete"], 1, "C",
          sol="1. suis — 2. es — 3. est — 4. est")
    e2 = E("Je complète avec ai, as, a.", f'''<div class="grid2">
<p>1. J'{blank("s")} 15 ans.</p><p>2. Tu {blank("s")} quel âge ?</p><p>3. Yonas {blank("s")} 14 ans.</p><p>4. Daria {blank("s")} un livre.</p></div>''', ["complete"], 1, "C",
           sol="1. ai — 2. as — 3. a — 4. a")
    b.page(f'{l5}{e}{e2}', "Leçon 4")

    e3 = E("Être ou avoir ? J'entoure le bon verbe.", f'''<div class="grid2">
<p>1. Je <b>suis / ai</b> 13 ans.</p><p>2. Tu <b>es / as</b> de la classe B ?</p><p>3. Il <b>est / a</b> un cahier.</p><p>4. Elle <b>est / a</b> professeure.</p>
<p>5. Fatou <b>est / a</b> 14 ans.</p><p>6. Je <b>suis / ai</b> content.</p></div>''', ["entoure"], 2, "C",
           sol="1. ai — 2. es — 3. a — 4. est — 5. a — 6. suis")
    e4 = E("Je corrige l'erreur. Je barre et j'écris la bonne phrase.", f'''
<p>1. Je suis 15 ans. → {blank("xl")}</p><p>2. Bilal est 16 ans. → {blank("xl")}</p><p>3. Tu a 14 ans. → {blank("xl")}</p>''', ["barre", "ecris"], 3, "C",
           sol="1. J'ai 15 ans. — 2. Bilal a 16 ans. — 3. Tu as 14 ans.")
    e5 = E("Le jeu du dé : je lance le dé et je fais une phrase avec le pronom.", f'''<div class="grid6">
{"".join(f'<div class="card c">{dice(i, 34)}<div class="word">{p}</div></div>' for i, p in zip(range(1, 7), ["je", "tu", "il", "elle", "Yonas", "Mme Lambert"]))}</div>
<p class="sm mt2">Exemple : 🎲 3 → « Il a 12 ans. » / « Il est gentil. »</p>''', ["joue", "parle", "duo"], 2, "D",
           sol="Réponses libres. Vérifier : je suis / j'ai ; tu es / tu as ; il, elle, Yonas, Mme Lambert → est / a.")
    def ea(k, mood, txt):
        return f'<div class="card c">{avatar(k, 56, mood)}<p class="sm">{txt}</p></div>'
    e5b = E("Je regarde les images. Je complète avec est ou a.", '<div class="grid4">' + ea("bilal", "sourire", "Bilal ____ des lunettes.") + ea("yonas", "rire", "Yonas ____ content.") + ea("fatou", "triste", "Fatou ____ triste.") + ea("amina", "sourire", "Amina ____ un foulard bleu.") + '</div>',
             ["regarde", "complete"], 2, "C", sol="Bilal a des lunettes · Yonas est content · Fatou est triste · Amina a un foulard bleu")
    b.page(f'{e3}{e4}{e5}{e5b}', "S'entraîner")

    # ================= LEÇON 5 : NOMBRES =================
    def ncard(i):
        vis = dice(i, 26) if 1 <= i <= 6 else ("" if i == 0 else dice(6, 22) + dice(i - 6, 22) if i <= 12 else "")
        return f'<div class="card c" style="padding:1.5mm"><div style="font-size:20pt;font-weight:800;color:#E4572E;line-height:1.1">{i}</div><div class="word" style="font-size:10.5pt">{NUM[i]}</div><div style="height:7mm">{vis}</div></div>'
    l6 = lecon("Les nombres de 0 à 20", f'<div class="grid6" style="grid-template-columns:repeat(7,1fr);gap:2mm">{"".join(ncard(i) for i in range(21))}</div>'
               '<div class="astuce mt2" style="margin-bottom:0">17 = dix-<b>sept</b> (10 + 7) · 18 = dix-<b>huit</b> (10 + 8) · 19 = dix-<b>neuf</b> (10 + 9). Le trait d\'union : dix<b>-</b>sept.</div>')
    e6 = E("J'écoute et je répète les nombres. Puis je compte avec mes doigts.", "", ["ecoute", "repete"], 1, "A",
           script="Compter de 0 à 20 lentement, puis à l'envers (20 → 0). Jeux : compter de 2 en 2 ; dire un nombre au hasard, les élèves montrent avec les doigts ; un élève dit un nombre, son voisin dit le suivant.",
           sol="Activité orale. Attention à la prononciation de six [sis], dix [dis], et au [z] de « deux ans » [døzɑ̃], « trois ans », « six ans » [sizɑ̃], « dix ans » [dizɑ̃].")
    vie = [("🚌", '<span style="background:#E4572E;color:#fff;padding:1mm 3mm;border-radius:2mm;font-weight:800">BUS 12</span>'), ("🎂", '<b style="font-size:16pt">15</b> ans'), ("🚪", '<span style="border:2px solid #1F2A44;padding:1mm 3mm;font-weight:800">Classe 14</span>'), ("📕", 'page <b>18</b>'), ("⏰", '<b style="font-size:14pt">8 h</b>'), ("🏠", 'Rue du Marché <b>8</b>')]
    e6b = E("Les nombres dans la vie. Je lis le nombre à voix haute. J'écris le nombre en lettres.", '<div class="grid3">' + "".join(f'<div class="card c"><span class="emo s">{e}</span><div class="mt2">{t}</div><div class="line"></div></div>' for e, t in vie) + '</div>',
              ["lis", "ecris"], 2, "B", sol="douze · quinze · quatorze · dix-huit · huit · huit")
    b.page(f'{l6}{e6}{e6b}', "Leçon 5")

    emoj = [("🍎", 3), ("⚽", 7), ("✏️", 12), ("🌟", 15), ("🐟", 9), ("📚", 18)]
    cnt = "".join(f'<div class="card"><div style="font-size:15pt;line-height:1.25;letter-spacing:1px">{e * n}</div><p class="mt2">{blank("s")} = {blank()}</p></div>' for e, n in emoj)
    e7 = E("Je compte. J'écris le nombre en chiffres et en lettres.", f'<div class="grid3">{cnt}</div>', ["numerote", "ecris"], 1, "C",
           sol="🍎 3 trois · ⚽ 7 sept · ✏️ 12 douze · 🌟 15 quinze · 🐟 9 neuf · 📚 18 dix-huit")
    e8 = E("Je relie le chiffre et le mot.", relie(["<b class='big'>11</b>", "<b class='big'>16</b>", "<b class='big'>4</b>", "<b class='big'>20</b>", "<b class='big'>13</b>", "<b class='big'>19</b>"],
            ["vingt", "treize", "onze", "dix-neuf", "quatre", "seize"]), ["relie"], 1, "B", sol="11 onze · 16 seize · 4 quatre · 20 vingt · 13 treize · 19 dix-neuf")
    e8b = E("Défi ! Le nombre mystère. Qui suis-je ?", '<div class="grid2">' + "".join(f'<div class="card"><p class="sm">{t}</p><p>→ {blank()}</p></div>' for t in ["Je suis entre 10 et 12.", "Je suis 10 + 5.", "Je suis le plus grand nombre de la leçon.", "Je suis 2 fois 8."]) + '</div>',
             ["lis", "ecris"], 3, "C", sol="onze (11) · quinze (15) · vingt (20) · seize (16)")
    b.page(f'{e7}{e8}{e8b}', "S'entraîner")

    e9 = E("Dictée de nombres : j'écoute et j'écris le chiffre.", '<div class="grid5">' + "".join(f'<div class="card c"><b>{chr(97+i)}.</b><div class="line"></div></div>' for i in range(10)) + '</div>',
           ["ecoute", "ecris"], 2, "A", script="Dicter deux fois chaque nombre : a. 6 — b. 14 — c. 2 — d. 17 — e. 12 — f. 5 — g. 20 — h. 13 — i. 10 — j. 16",
           sol="a. 6 — b. 14 — c. 2 — d. 17 — e. 12 — f. 5 — g. 20 — h. 13 — i. 10 — j. 16")
    e10 = E("Je calcule et j'écris le résultat en lettres.", f'''<div class="grid2">
<p class="big">5 + 5 = {blank()}</p><p class="big">8 + 4 = {blank()}</p><p class="big">20 − 6 = {blank()}</p><p class="big">9 + 9 = {blank()}</p>
<p class="big">3 + 4 = {blank()}</p><p class="big">15 − 4 = {blank()}</p></div>
<p class="sm muted">+ = plus &nbsp;·&nbsp; − = moins &nbsp;·&nbsp; = égale</p>''', ["ecris"], 2, "C", sol="dix · douze · quatorze · dix-huit · sept · onze")
    e11 = E("Défi ! Les numéros de téléphone. Je lis les numéros à voix haute, deux par deux.", '''<div class="grid3">
<div class="card c">🚑 Urgences<br><b class="huge">112</b><p class="xs">« cent douze » ou « un – un – deux »</p></div>
<div class="card c">📞 L'école<br><b class="big">081 / 12 13 14</b></div><div class="card c">📱 Maman<br><b class="big">0470 / 11 15 19</b></div></div>
<p class="sm mt2">En Belgique, on lit souvent les numéros de téléphone par groupes de 2 chiffres : 12 13 14 = « douze, treize, quatorze ».</p>''', ["lis", "parle"], 3, "A",
            sol="Lecture : zéro-quatre-vingt-un (ou 0-8-1), douze, treize, quatorze · zéro-quatre-sept-zéro, onze, quinze, dix-neuf. Retenir : 112 = numéro d'urgence européen.")
    b.page(f'{e9}{e10}{e11}', "S'entraîner")

    # ================= BINGO =================
    random.seed(4)
    grids = []
    for g in range(4):
        nums = random.sample(range(0, 21), 9)
        cells = "".join(f'<div style="border:2px solid #1F2A44;height:17mm;display:flex;align-items:center;justify-content:center;font-size:20pt;font-weight:800">{n}</div>' for n in nums)
        grids.append(f'<div class="card"><div class="c" style="font-weight:800;color:#9B5DE5">BINGO {g+1}</div><div style="display:grid;grid-template-columns:repeat(3,1fr);gap:1.5mm">{cells}</div></div>')
    e12 = E("Bingo des nombres ! Je découpe une grille. La prof dit des nombres : je mets un jeton. 3 jetons alignés = BINGO !", f'<div class="grid2">{"".join(grids)}</div>',
            ["decoupe", "ecoute", "joue"], 1, "D", script="Tirer au hasard des nombres de 0 à 20 (petits papiers dans une boîte). Les dire deux fois. Variante ●●● : dire des calculs (« trois plus quatre ») au lieu des nombres. Un élève qui gagne relit ses nombres à voix haute pour vérifier.",
            sol="Jeu. Vérifier la lecture des nombres du gagnant.")
    e12b = E("Je complète les suites de nombres.", '<div class="grid2">' + "".join(f'<p class="big">{t}</p>' for t in ["0 · 2 · 4 · ___ · 8 · ___", "20 · 19 · 18 · ___ · ___ · 15", "5 · 10 · ___ · 20", "1 · 3 · 5 · ___ · ___ · 11"]) + '</div>',
              ["complete"], 2, "C", sol="6, 10 · 17, 16 · 15 · 7, 9")
    b.page(f'{e12}{e12b}', "Jeu")

    # ================= LEÇON 6 : ALPHABET =================
    abc = [("A", "a", "ananas", "🍍"), ("B", "bé", "banane", "🍌"), ("C", "cé", "cadeau", "🎁"), ("D", "dé", "dauphin", "🐬"), ("E", "e", "étoile", "⭐"), ("F", "èf", "fraise", "🍓"), ("G", "gé", "gâteau", "🎂"),
           ("H", "ach", "hélicoptère", "🚁"), ("I", "i", "île", "🏝️"), ("J", "ji", "jus", "🧃"), ("K", "ka", "kiwi", "🥝"), ("L", "èl", "lune", "🌙"), ("M", "èm", "maison", "🏠"), ("N", "èn", "nuage", "☁️"),
           ("O", "o", "orange", "🍊"), ("P", "pé", "pomme", "🍎"), ("Q", "ku", "quatre", "4️⃣"), ("R", "èr", "robot", "🤖"), ("S", "ès", "soleil", "☀️"), ("T", "té", "téléphone", "📱"), ("U", "u", "usine", "🏭"),
           ("V", "vé", "vélo", "🚲"), ("W", "double vé", "wagon", "🚃"), ("X", "iks", "taxi", "🚕"), ("Y", "i grec", "yoyo", "🪀"), ("Z", "zèd", "zèbre", "🦓")]
    vow = set("AEIOUY")
    cells = "".join(f'<div class="card c" style="padding:1.2mm;{"background:#FFF1EB;border-color:#F5C4AF" if L in vow else ""}"><div style="font-size:17pt;font-weight:800;line-height:1">{L} {L.lower()}</div><div class="xs muted">« {s} »</div><div style="font-size:15pt;line-height:1.2">{em}</div><div class="xs">{w}</div></div>' for L, s, w, em in abc)
    l7 = lecon("L'alphabet", f'<div class="grid6" style="grid-template-columns:repeat(7,1fr);gap:1.6mm">{cells}</div>'
               '<p class="sm mt2" style="margin-bottom:0">🟧 Les <b>voyelles</b> : a, e, i, o, u, y. Les autres lettres sont des <b>consonnes</b>. — <b>MAJUSCULE</b> : A B C · <b>minuscule</b> : a b c</p>')
    e13 = E("J'écoute et je chante l'alphabet.", "", ["ecoute", "repete"], 1, "A", script="Dire l'alphabet lettre par lettre en montrant chaque case. Puis le rythmer par groupes : A B C D / E F G / H I J K / L M N O P / Q R S T / U V / W X / Y Z. Insister sur E [ə] / I [i] / U [y] et sur G [ʒe] / J [ʒi], qui sont souvent confondus.",
            sol="Activité orale. Points de vigilance : E/I, G/J, U/OU.")
    e13b = E("Attention aux lettres qui se ressemblent ! J'entoure la lettre du modèle.", '<div class="grid2">' + "".join(f'<div class="card flex"><span class="huge" style="background:#FFD166;padding:0 3mm;border-radius:2mm">{m}</span><span class="big" style="letter-spacing:3mm">{r}</span></div>' for m, r in [("b", "d p b q d b"), ("p", "q p b p d q"), ("m", "n m u m n w"), ("u", "n u v u n u")]) + '</div>',
              ["regarde", "entoure"], 2, "B", sol="b : 3e et 6e lettres · p : 2e et 4e · m : 2e et 4e · u : 2e, 4e et 6e")
    b.page(f'{l7}{e13}{e13b}', "Leçon 6")

    e14 = E("J'écoute et j'entoure la lettre que j'entends.", '<div class="grid2">' + "".join(
        f'<p class="big"><b>{i+1}.</b> &nbsp;' + " &nbsp; ".join(r) + '</p>' for i, r in enumerate([["E", "I", "A"], ["G", "J", "Z"], ["U", "O", "I"], ["B", "P", "V"], ["H", "A", "K"], ["Q", "K", "U"]])) + '</div>',
        ["ecoute", "entoure"], 1, "A", script="Dire deux fois chaque lettre : 1. I — 2. G — 3. U — 4. V — 5. H — 6. Q", sol="1. I — 2. G — 3. U — 4. V — 5. H — 6. Q")
    e15 = E("Je complète l'alphabet avec la lettre qui manque.", '<div class="grid3">' + "".join(f'<p class="big">{x}</p>' for x in [
        f"A B {blank('s')} D", f"F {blank('s')} H I", f"L M {blank('s')} O", f"{blank('s')} R S T", f"U {blank('s')} W X", f"X Y {blank('s')}"]) + '</div>', ["complete"], 1, "C",
        sol="C · G · N · Q · V · Z")
    e16 = E("J'épelle. J'écoute les prénoms épelés et je les écris.", '<div class="grid4">' + "".join(f'<div class="card"><b>{i}.</b><div class="line"></div></div>' for i in range(1, 5)) + '</div>',
            ["ecoute", "ecris"], 2, "A", script="Épeler deux fois chaque prénom : 1. A-M-I-N-A — 2. Y-O-N-A-S — 3. F-A-T-O-U — 4. B-I-L-A-L", sol="1. AMINA — 2. YONAS — 3. FATOU — 4. BILAL")
    e17 = E("J'épelle mon prénom et mon nom à mon voisin. Il écrit. Je vérifie.", f'<p>Mon voisin a écrit : {blank("xl")}</p><p class="sm muted">Pour aider : « A comme ananas », « B comme banane »…</p>', ["parle", "duo"], 2, "A",
            sol="Réponses personnelles. Faire remarquer : on épelle souvent son nom au secrétariat, chez le médecin, au téléphone.")
    e18 = E("Défi ! Je classe les lettres de mon prénom : voyelles / consonnes.", '<div class="grid2"><div class="card"><b>Voyelles</b><div class="line"></div></div><div class="card"><b>Consonnes</b><div class="line"></div></div></div>',
            ["ecris"], 3, "C", sol="Réponses personnelles (voyelles : a, e, i, o, u, y).")
    b.page(f'{e14}{e15}{e16}{e17}{e18}', "S'entraîner")

    # ================= PHONÉTIQUE =================
    sons = [("[a]", "#E4572E", "chat 🐱 · papa 👨 · ami"), ("[i]", "#2BA88F", "lit 🛏️ · six 6 · midi"), ("[o]", "#4A7BD1", "vélo 🚲 · moto 🏍️ · photo"), ("[u]", "#9B5DE5", "loup 🐺 · roue 🛞 · bonjour")]
    sc = "".join(f'<div class="card c" style="border-color:{c}"><div style="font-size:24pt;font-weight:800;color:{c}">{s}</div><div class="sm">{w}</div></div>' for s, c, w in sons)
    imgs = [("🐱", "chat"), ("🚲", "vélo"), ("🛏️", "lit"), ("🐺", "loup"), ("🍕", "pizza"), ("🎂", "gâteau"), ("📷", "photo"), ("🦁", "lion"), ("🧀", "fromage"), ("🛞", "roue"), ("🏍️", "moto"), ("🚌", "bus")]
    ic = "".join(f'<div class="card c" style="padding:1.5mm"><span class="emo s">{e}</span><div class="xs">{w}</div><div class="xs" style="letter-spacing:2mm">○○○○</div></div>' for e, w in imgs)
    e19 = E("J'écoute les sons. Je répète.", f'<div class="grid4">{sc}</div><div class="astuce mt2" style="margin-bottom:0">Le son <b>[u]</b> s\'écrit avec deux lettres : <b>ou</b> (loup, bonjour). La lettre <b>u</b> seule fait un autre son : <b>[y]</b> (tu, usine). Attention !</div>',
            ["ecoute", "repete"], 1, "A", script="Prononcer chaque son longuement en exagérant la forme de la bouche : [a] bouche ouverte, [i] sourire, [o] bouche ronde, [u] bouche très ronde et en avant. Puis les mots-exemples.",
            sol="Activité orale.")
    e20 = E("J'écoute le mot. J'entends [a], [i], [o] ou [u] ? Je colorie le bon rond : 🔴 [a] 🟢 [i] 🔵 [o] 🟣 [u].", f'<div class="grid6">{ic}</div>', ["ecoute", "colorie"], 2, "A",
            script="Lire chaque mot deux fois : chat, vélo, lit, loup, pizza, gâteau, photo, lion, fromage, roue, moto, bus (bus : piège, on entend [y] → aucun rond, ou faire remarquer que c'est le son de « tu »).",
            sol="chat [a] · vélo [o] · lit [i] · loup [u] · pizza [i] et [a] · gâteau [a] et [o] · photo [o] · lion [i] (+ [ɔ̃]) · fromage [o] et [a] · roue [u] · moto [o] · bus : aucun ([y])")
    e21 = E("Défi ! Je trouve un mot avec [a], [i], [o], [u] dans les leçons du module.", '<div class="grid4">' + "".join(f'<div class="card"><b>{s}</b><div class="line"></div></div>' for s, *_ in sons) + '</div>', ["ecris"], 3, "C",
            sol="Exemples : [a] Amina, Madame, ans, ami · [i] six, dix, merci, Daria · [o] stylo, photo, au (revoir) · [u] bonjour, vous, où, Fatou")
    b.page(f'<h2>J\'écoute bien · Les voyelles [a] [i] [o] [u]</h2>{e19}{e20}{e21}', "Sons")

    # ================= MATÉRIEL =================
    mat = [("✏️", "un crayon"), ("🖊️", "un stylo"), ("📏", "une latte"), ("✂️", "des ciseaux"), ("📒", "un cahier"), ("📕", "un livre"),
           ("🎒", "un cartable"), ("👝", "un plumier"), ("🧴", "de la colle"), ("📄", "une feuille"), ("🖍️", "des crayons de couleur"), ("🧽", "une gomme")]
    mc = "".join(f'<div class="card c"><span class="emo">{e}</span><div class="word">{w}</div></div>' for e, w in mat)
    e22 = E("Le matériel de la classe. J'écoute et je répète.", f'<div class="grid6">{mc}</div><div class="astuce mt2" style="margin-bottom:0">🇧🇪 En Belgique, on dit <b>une latte</b> (en France : une règle) et <b>un plumier</b> (en France : une trousse).</div>',
            ["ecoute", "repete"], 1, "A", script="Montrer chaque objet réel de la classe en le nommant. Puis jeu « Montre-moi… » : « Montre-moi un crayon ! » Les élèves lèvent l'objet.", sol="Activité orale.")
    e23 = E("J'ai… / Je n'ai pas… Je regarde dans mon cartable et je coche.", table(["Objet", "J'ai ✅", "Je n'ai pas ❌"], [[f"{e} {w}", '<span class="chk"></span>', '<span class="chk"></span>'] for e, w in mat[:6]], ["100mm", "40mm", "40mm"]),
            ["regarde", "coche"], 1, "C", sol="Réponses personnelles. Prolongement : « Tu as un crayon ? — Oui, j'ai un crayon. »")
    e24 = E("Défi ! Je demande à mon voisin : « Tu as un… ? » Il répond : « Oui, j'ai un… » ou « Non, je n'ai pas de… ».", '', ["parle", "duo"], 3, "A",
            sol="Accepter « Non, je n'ai pas de crayon. » (la négation sera travaillée au module 6).")
    e24b = E("Qu'est-ce que c'est ? J'écris le mot sous l'image.", '<div class="grid6">' + "".join(f'<div class="card c"><span class="emo">{e}</span><div class="line"></div></div>' for e in ["✂️", "📒", "🎒", "📏", "🧽", "✏️"]) + '</div>',
              ["regarde", "ecris"], 2, "C", sol="des ciseaux · un cahier · un cartable · une latte · une gomme · un crayon")
    b.page(f'{e22}{e23}{e24}{e24b}', "Lexique")

    # ================= LES GESTES DE L'ÉLÈVE (FLSco) =================
    phr = [("✋", "Je lève la main pour parler."), ("❓", "Je ne comprends pas."), ("🔁", "Vous pouvez répéter, s'il vous plaît ?"), ("🗣️", "Comment on dit … en français ?"),
           ("✍️", "Comment on écrit … ?"), ("🚻", "Je peux aller aux toilettes, s'il vous plaît ?"), ("🤒", "J'ai mal. Je peux aller à l'infirmerie ?"), ("🙋", "J'ai fini !"),
           ("🤝", "Tu peux m'aider ?"), ("📖", "C'est quelle page ?"), ("😕", "Pardon ! Excusez-moi."), ("👍", "D'accord ! / Oui, je comprends.")]
    pc = "".join(f'<div class="card flex" style="padding:2.5mm;gap:2mm"><span class="emo s">{e}</span><span class="word">{t}</span></div>' for e, t in phr)
    e25 = E("Les phrases de survie en classe. J'écoute, je répète, je mime.", f'<div class="grid2">{pc}</div>', ["ecoute", "repete"], 1, "P",
            script="Lire chaque phrase et la mimer. Puis la prof mime une situation (elle fait semblant de ne pas comprendre, d'avoir fini…) et les élèves disent la phrase. Afficher ces phrases au mur toute l'année.",
            sol="Activité orale. À afficher au mur des ressources.")
    e26 = E("Que dis-tu ? J'écris la phrase.", f'''<div class="grid2">
<div class="card"><p>1. Tu ne comprends pas l'exercice.</p><div class="line"></div></div><div class="card"><p>2. Tu as terminé ton travail.</p><div class="line"></div></div>
<div class="card"><p>3. Tu ne connais pas le mot « gomme » en français.</p><div class="line"></div></div><div class="card"><p>4. La prof parle trop vite.</p><div class="line"></div></div></div>''', ["lis", "ecris"], 2, "C",
            sol="1. Je ne comprends pas. — 2. J'ai fini ! — 3. Comment on dit … en français ? — 4. Vous pouvez répéter, s'il vous plaît ?")
    b.page(f'<span class="tag-doc">🎒 FRANÇAIS DE L\'ÉCOLE</span><h2>Je suis un élève : les phrases utiles</h2>{e25}{e26}', "Consignes & école")
