"""Volume 1 · Module 1 « Bonjour ! » — partie A : couverture, ouverture, découverte, leçons, documents de vie."""
from lib.base import *
from lib.art import *

MC = "#E4572E"
CAST_INFO = [
    ("amina", "Amina", "KHALIL", 15, "Syrie", "de Syrie", "arabe, un peu d'anglais"),
    ("yonas", "Yonas", "TESFAYE", 14, "Érythrée", "d'Érythrée", "tigrinya"),
    ("daria", "Daria", "KOVALENKO", 13, "Ukraine", "d'Ukraine", "ukrainien, russe"),
    ("mateo", "Mateo", "RAMÍREZ", 15, "Colombie", "de Colombie", "espagnol"),
    ("bilal", "Bilal", "AHMADI", 16, "Afghanistan", "d'Afghanistan", "dari, pachto"),
    ("fatou", "Fatou", "CAMARA", 14, "Guinée", "de Guinée", "peul, soussou, un peu de français"),
]


def build_a(b, E):
    # ================= COUVERTURE DU VOLUME =================
    cast = "".join(f'<div style="text-align:center">{avatar(k, 118, m)}</div>' for k, m in [("amina", "rire"), ("yonas", "sourire"), ("daria", "rire"), ("mateo", "sourire"), ("bilal", "rire"), ("fatou", "sourire")])
    b.page(f'''
<div style="height:297mm;background:#FFF6EE;position:relative;overflow:hidden">
 <div style="position:absolute;top:-40mm;right:-40mm;width:150mm;height:150mm;border-radius:50%;background:#E4572E"></div>
 <div style="position:absolute;bottom:-30mm;left:-30mm;width:110mm;height:110mm;border-radius:50%;background:#FFD166"></div>
 <div style="position:absolute;top:60mm;right:20mm;width:30mm;height:30mm;border-radius:50%;background:#2BA88F"></div>
 <div style="position:relative;padding:24mm 18mm">
  <div style="font-size:11pt;letter-spacing:3px;font-weight:700;color:#E4572E">FRANÇAIS · DASPA · VOLUME 1</div>
  <div style="font-size:60pt;font-weight:800;line-height:1;margin-top:10mm;color:#1F2A44">Premiers<br>pas</div>
  <div style="font-size:18pt;margin-top:6mm;color:#1F2A44">Parcours ★ Alpha → niveau A1</div>
  <div style="margin-top:14mm;display:flex;gap:3mm;flex-wrap:wrap;max-width:120mm">
   {"".join(f'<span class="pill" style="background:#fff;border:2px solid #1F2A44;font-size:13pt">{w}</span>' for w in ["Bonjour", "Salut", "Hello", "Привіт", "مرحبا", "Salam", "Olá", "Hola", "Selam", "Merhaba"])}
  </div>
 </div>
 <div style="position:absolute;bottom:34mm;left:14mm;right:14mm;display:flex;justify-content:space-between;align-items:flex-end;background:#fff;border-radius:8mm;padding:6mm 6mm 0 6mm;box-shadow:0 2mm 6mm rgba(0,0,0,.12)">{cast}</div>
 <div style="position:absolute;bottom:14mm;left:18mm;font-size:10pt;color:#1F2A44"><b>Module 1 · Bonjour !</b> — édition de travail</div>
</div>''', full=True)

    # ================= CE LIVRE APPARTIENT À =================
    b.page(f'''
<div class="flex top" style="gap:8mm">
 <div style="width:62mm;height:78mm;border:3px dashed #1F2A44;border-radius:4mm;display:flex;align-items:center;justify-content:center;text-align:center" class="muted">Ma photo<br>ou mon dessin</div>
 <div class="grow">
  <h1>Ce livre est à moi !</h1>
  <p class="big mt4">Prénom : {blank("l")}</p>
  <p class="big mt4">Nom : {blank("l")}</p>
  <p class="big mt4">Classe : {blank()}</p>
  <p class="big mt4">Ma prof : {blank("l")}</p>
 </div>
</div>
<h2 class="mt4" style="margin-top:10mm">Comment utiliser mon livre ?</h2>
<div class="grid2">
 <div class="card"><b>Les points = la difficulté</b>
  <p class="mt2">{dots(1)} &nbsp;Je découvre. C'est facile.</p>
  <p>{dots(2)} &nbsp;Je m'entraîne.</p>
  <p>{dots(3)} &nbsp;Défi ! Je vais plus loin.</p></div>
 <div class="card"><b>Les couleurs = les ateliers</b>
  <p class="mt2"><span class="atl A">{ATELIERS["A"]}</span></p><p><span class="atl B">{ATELIERS["B"]}</span></p>
  <p><span class="atl C">{ATELIERS["C"]}</span></p><p><span class="atl D">{ATELIERS["D"]}</span></p>
  <p><span class="atl P">{ATELIERS["P"]}</span></p></div>
 <div class="card"><b>📌 À ÉTUDIER</b><p class="sm mt2">Le cadre jaune, c'est la leçon. Je la lis à la maison. Je l'apprends par cœur.</p>
  <div class="lecon" style="margin:4mm 0 0 0;padding:2mm 3mm"><div class="lt">📌 À ÉTUDIER</div><p class="sm" style="margin-top:2mm">Je m'appelle…</p></div></div>
 <div class="card"><b><span class="alpha-tag">★ ALPHA</span> J'apprends à lire et à écrire</b><p class="sm mt2">Ces pages sont pour les élèves qui apprennent les lettres. La prof te dit si c'est pour toi.</p>
 <p class="mt2"><b>🔁 Je révise</b> — <span class="sm">je reprends ce que j'ai appris.</span></p><p><b>📝 Test</b> — <span class="sm">je montre ce que je sais.</span></p></div>
</div>''', "Mon livre", levels=False)

    b.page("%%SOMMAIRE%%", "Sommaire", levels=False)

    # ================= OUVERTURE DU MODULE =================
    obj = [("👋", "saluer et dire au revoir"), ("🙋", "dire mon nom, mon âge, mon pays"), ("❓", "poser des questions à un camarade"),
           ("🔢", "compter de 0 à 20"), ("🔤", "dire l'alphabet et épeler mon nom"), ("✏️", "comprendre les consignes de la classe")]
    objs = "".join(f'<div class="flex mb2"><span class="emo s">{e}</span><span class="big">{t}</span></div>' for e, t in obj)
    b.page(f'''
<div style="background:{MC};color:#fff;margin:-17mm -14mm 6mm -14mm;padding:16mm 14mm 6mm 14mm">
 <div style="font-size:13pt;font-weight:700;opacity:.9">MODULE 1</div>
 <div style="font-size:44pt;font-weight:800;line-height:1">Bonjour !</div>
</div>
<div class="c">{scene_classroom(690)}</div>
<div class="grid2 mt4">
 <div><h2>Je vais apprendre à…</h2>{objs}</div>
 <div>
  <div class="card" style="background:#FFF6EE;border-color:#F5C4AF"><h3 style="margin-top:0">🗣️ On parle ensemble</h3>
  <p>Regarde l'image. Qu'est-ce que tu vois ?</p><p>Tu connais des mots en français ?</p><p>Comment on dit « bonjour » dans ta langue ?</p>
  <p class="mt2">Dans ma langue, on dit : {blank("l")}</p></div>
  <div class="card mt4"><h3 style="margin-top:0">🔑 Les mots-clés</h3>
  {"".join(f'<span class="pill">{w}</span>' for w in ["bonjour", "au revoir", "je m'appelle", "le nom", "le prénom", "l'âge", "le pays", "la langue", "l'alphabet", "les nombres"])}</div>
 </div>
</div>''', "Ouverture", levels=False)

    # ================= PLAN DE TRAVAIL =================
    # rempli à la fin (placeholder remplacé dans m1.py)
    b.page("%%PLAN_DE_TRAVAIL%%", "Mon plan de travail", levels=False)

    # ================= DÉCOUVRIR : LA BD =================
    def case(n, inner, h=72):
        return f'<div style="border:2.5px solid #1F2A44;border-radius:3mm;height:{h}mm;position:relative;padding:3mm;background:#FFFDF8"><div style="position:absolute;top:2mm;left:2mm;background:#1F2A44;color:#fff;width:6mm;height:6mm;border-radius:50%;font-size:9pt;font-weight:700;display:flex;align-items:center;justify-content:center">{n}</div>{inner}</div>'

    def bub(t, side="l"):
        return f'<div class="bubble" style="margin:0 0 2mm 0;font-size:11.5pt">{t}</div>'

    bd = '<div class="grid2" style="gap:3mm">' + "".join([
        case(1, f'<div class="flex top" style="margin-top:5mm">{avatar("prof", 95, "sourire")}<div>{bub("Bonjour ! Je m&#39;appelle Madame Lambert.")}{bub("Je suis votre professeure de français.")}</div></div>'),
        case(2, f'<div class="flex top" style="margin-top:5mm;justify-content:space-around">{avatar("amina", 80, "rire")}{avatar("bilal", 80, "sourire")}{avatar("fatou", 80, "rire")}</div><div class="c">{bub("Bonjour, Madame !")}</div>'),
        case(3, f'<div class="flex top" style="margin-top:5mm">{avatar("prof", 78, "sourire")}<div>{bub("Comment tu t&#39;appelles ?")}</div></div><div class="flex top" style="justify-content:flex-end">{bub("Je m&#39;appelle Yonas.")}{avatar("yonas", 78, "sourire", flip=True)}</div>'),
        case(4, f'<div class="flex top" style="margin-top:5mm">{avatar("prof", 78, "sourire")}<div>{bub("Tu as quel âge, Yonas ?")}</div></div><div class="flex top" style="justify-content:flex-end">{bub("J&#39;ai 14 ans.")}{avatar("yonas", 78, "rire", flip=True)}</div>'),
        case(5, f'<div class="flex top" style="margin-top:5mm">{avatar("prof", 78, "pense")}<div>{bub("Tu viens d&#39;où ?")}</div></div><div class="flex top" style="justify-content:flex-end">{bub("Je viens d&#39;Érythrée.")}{avatar("yonas", 78, "sourire", flip=True)}</div>'),
        case(6, f'<div class="flex top" style="margin-top:5mm">{avatar("daria", 78, "rire")}<div>{bub("Salut Yonas ! Moi, c&#39;est Daria.")}{bub("Je viens d&#39;Ukraine.")}</div></div><div class="flex top" style="justify-content:flex-end">{bub("Salut Daria !")}{avatar("yonas", 70, "rire", flip=True)}</div>'),
    ]) + '</div>'
    e1 = E("J'écoute et je regarde la BD. Je répète.", bd, ["ecoute", "regarde", "repete"], 1, "A",
           script="Lire la BD deux fois, en changeant de voix pour chaque personnage. 1re écoute : les élèves suivent du doigt les cases. 2e écoute : arrêt après chaque bulle, la classe répète en chœur.<br><i>Case 1 — Mme Lambert : Bonjour ! Je m'appelle Madame Lambert. Je suis votre professeure de français. Case 2 — Les élèves : Bonjour, Madame ! Case 3 — Mme Lambert : Comment tu t'appelles ? Yonas : Je m'appelle Yonas. Case 4 — Mme Lambert : Tu as quel âge, Yonas ? Yonas : J'ai 14 ans. Case 5 — Mme Lambert : Tu viens d'où ? Yonas : Je viens d'Érythrée. Case 6 — Daria : Salut Yonas ! Moi, c'est Daria. Je viens d'Ukraine. Yonas : Salut Daria !</i>",
           sol="Activité orale. Vérifier la prononciation de « je m'appelle » [ʒəmapɛl] et de « j'ai » [ʒe].")
    b.page(f'<h2>Découvrir · La rentrée</h2>{e1}', "Découvrir")

    # ================= DÉCOUVRIR : questions sur la BD =================
    names = ["Yonas", "Daria", "Amina", "Mme Lambert"]
    e2 = E("Qui parle ? J'entoure le bon prénom.", f'''
<table class="t"><tr><th style="width:50%">Phrase</th><th>Qui parle ?</th></tr>
{"".join(f"<tr><td>{q}</td><td>{'&nbsp;&nbsp;&nbsp;'.join(names)}</td></tr>" for q in ["« Je m'appelle Madame Lambert. »", "« J'ai 14 ans. »", "« Moi, c'est Daria. »", "« Comment tu t'appelles ? »", "« Je viens d'Érythrée. »"])}
</table>''', ["lis", "entoure"], 1, "B", sol="1. Mme Lambert — 2. Yonas — 3. Daria — 4. Mme Lambert — 5. Yonas")
    e3 = E("Vrai ou faux ? Je coche.", table(["", "Vrai ✅", "Faux ❌"], [
        [x, '<span class="chk"></span>', '<span class="chk"></span>'] for x in
        ["La prof s'appelle Madame Lambert.", "Yonas a 15 ans.", "Yonas vient d'Érythrée.", "Daria vient de Syrie.", "La prof est professeure de mathématiques."]], ["120mm", "30mm", "30mm"]),
        ["lis", "coche"], 2, "B", sol="1. Vrai — 2. Faux (il a 14 ans) — 3. Vrai — 4. Faux (elle vient d'Ukraine) — 5. Faux (de français)")
    e4 = E("Je complète la fiche de Yonas.", f'''
<div class="card flex" style="max-width:150mm">{avatar("yonas", 80)}<div class="grow">
<p>Prénom : {blank("l")}</p><p>Âge : {blank()} ans</p><p>Pays : {blank("l")}</p></div></div>''', ["ecris", "complete"], 2, "C",
        sol="Prénom : Yonas — Âge : 14 ans — Pays : Érythrée")
    e5 = E("Défi ! J'écris la présentation de Daria.", f'''<div class="flex">{avatar("daria", 70)}<div class="grow">
<p>Je m'appelle {blank("l")}.</p><p>Je viens {blank("l")}.</p></div></div>''', ["ecris"], 3, "C",
        sol="Je m'appelle Daria. Je viens d'Ukraine.")
    b.page(f'{e2}{e3}{e4}{e5}', "Découvrir")

    # ================= SALUER =================
    sal = [("🌅", "le matin", "Bonjour !"), ("☀️", "l'après-midi", "Bonjour !"), ("🌆", "le soir", "Bonsoir !"), ("🌙", "la nuit", "Bonne nuit !"),
           ("👋", "je pars", "Au revoir !"), ("😊", "avec un copain", "Salut !"), ("📅", "je vois la personne demain", "À demain !"), ("🙏", "on m'aide", "Merci !")]
    cards = "".join(f'<div class="card c"><span class="emo">{e}</span><div class="xs muted">{s}</div><div class="word big">{w}</div></div>' for e, s, w in sal)
    e6 = E("J'écoute, je regarde et je répète.", f'<div class="grid4">{cards}</div>', ["ecoute", "regarde", "repete"], 1, "A",
           script="Lire chaque carte : « Le matin, je dis : Bonjour ! » … « On m'aide, je dis : Merci ! ». Faire répéter en chœur, puis par rangée, puis individuellement. Mimer chaque situation (bâillement pour la nuit, geste de la main pour au revoir).",
           sol="Activité orale.")
    tuvous = f'''<div class="grid2">
<div class="card"><div class="flex">{avatar("daria", 64, "rire")}<span style="font-size:20pt">↔</span>{avatar("yonas", 64, "rire", flip=True)}</div>
<p class="big mt2"><b>Avec un copain, une copine :</b></p><p class="big">Salut ! Ça va ?</p><p class="sm muted">Je dis <b>tu</b>. 👕</p></div>
<div class="card"><div class="flex">{avatar("mateo", 64, "sourire")}<span style="font-size:20pt">↔</span>{avatar("prof", 64, "sourire", flip=True)}</div>
<p class="big mt2"><b>Avec la prof, un adulte :</b></p><p class="big">Bonjour, Madame ! Vous allez bien ?</p><p class="sm muted">Je dis <b>vous</b>. 👔</p></div></div>'''
    e7 = E("Tu ou vous ? Je regarde.", tuvous, ["regarde", "lis"], 1)
    b.page(f'<h2>Saluer · Dire au revoir</h2>{e6}{e7}', "Saluer")

    # ================= EXERCICES SALUER =================
    e8 = E("Je relie la situation et la phrase.", relie(
        ['<span class="emo s">🌅</span> le matin', '<span class="emo s">🌙</span> la nuit', '<span class="emo s">👋</span> je pars', '<span class="emo s">🙏</span> on m\'aide', '<span class="emo s">🌆</span> le soir'],
        ["Merci !", "Bonsoir !", "Bonjour !", "Au revoir !", "Bonne nuit !"]), ["relie"], 1, "B",
        sol="le matin → Bonjour ! · la nuit → Bonne nuit ! · je pars → Au revoir ! · on m'aide → Merci ! · le soir → Bonsoir !")
    e9 = E("Salut ou Bonjour, Madame ? J'entoure.", f'''<div class="grid3">
<div class="card c">{avatar("fatou", 70, "rire")}<p class="sm">Fatou, ta copine</p><p><b>Salut !</b> &nbsp;/&nbsp; <b>Bonjour, Madame !</b></p></div>
<div class="card c">{avatar("prof", 70)}<p class="sm">Mme Lambert, la prof</p><p><b>Salut !</b> &nbsp;/&nbsp; <b>Bonjour, Madame !</b></p></div>
<div class="card c">{avatar("educ", 70, "rire")}<p class="sm">M. Diallo, l'éducateur</p><p><b>Salut !</b> &nbsp;/&nbsp; <b>Bonjour, Monsieur !</b></p></div></div>''', ["regarde", "entoure"], 2, "B",
        sol="Fatou → Salut ! · Mme Lambert → Bonjour, Madame ! · M. Diallo → Bonjour, Monsieur !")
    e10 = E("Je complète les bulles.", f'''<div class="grid2">
<div class="card"><div class="flex top">{avatar("bilal", 64, "sourire")}<div class="bubble">Salut Mateo ! Ça va ?</div></div><div class="flex top" style="justify-content:flex-end"><div class="bubble">{blank("l")} Bilal ! Oui, ça va.</div>{avatar("mateo", 64, "rire", flip=True)}</div></div>
<div class="card"><div class="flex top">{avatar("amina", 64, "sourire")}<div class="bubble">{blank("l")}, Madame !</div></div><div class="flex top" style="justify-content:flex-end"><div class="bubble">Au revoir, Amina ! À demain !</div>{avatar("prof", 64, "sourire", flip=True)}</div></div></div>''', ["ecris", "complete"], 2, "C",
        sol="1. Salut (Bilal !) — 2. Au revoir (, Madame !)")
    ca_va = "".join(f'<div class="card c"><span class="emo">{e}</span><div class="word">{t}</div></div>' for e, t in [("😄", "Ça va très bien !"), ("🙂", "Ça va bien."), ("😐", "Comme ci, comme ça."), ("🙁", "Ça ne va pas.")])
    e11 = E("Ça va ? Je réponds avec mon visage et ma phrase. À deux.", f'<div class="grid4">{ca_va}</div><p class="mt2">Aujourd\'hui, moi : {blank("xl")}</p>', ["parle", "duo"], 1, "A",
            sol="Réponse libre. Encourager les élèves à varier les réponses et à renvoyer la question : « Et toi ? ».")
    b.page(f'{e8}{e9}{e10}{e11}', "Saluer")

    # ================= LEÇON 1 =================
    l1 = lecon("Saluer et dire au revoir", f'''
<table class="t" style="background:#fff"><tr><th>Quand ?</th><th>Avec un copain (tu)</th><th>Avec un adulte (vous)</th><th>Dans ma langue</th></tr>
<tr><td>🌅 J'arrive</td><td><b>Salut !</b></td><td><b>Bonjour, Madame / Monsieur !</b></td><td></td></tr>
<tr><td>🌆 Le soir</td><td><b>Salut !</b></td><td><b>Bonsoir, Madame / Monsieur !</b></td><td></td></tr>
<tr><td>👋 Je pars</td><td><b>Salut ! / À demain !</b></td><td><b>Au revoir, Madame / Monsieur !</b></td><td></td></tr>
<tr><td>🌙 Je vais dormir</td><td colspan="2"><b>Bonne nuit !</b></td><td></td></tr>
<tr><td>❓ Je demande</td><td><b>Ça va ?</b></td><td><b>Vous allez bien ?</b></td><td></td></tr>
<tr><td>💬 Je réponds</td><td colspan="2"><b>Ça va bien, merci. Et toi ? / Et vous ?</b></td><td></td></tr>
</table>
<div class="flex mt2"><span class="emo s">⚠️</span><p class="sm" style="margin:0"><b>Madame</b> = une femme adulte. <b>Monsieur</b> = un homme adulte. En Belgique, à l'école, on dit souvent <b>Madame</b> ou <b>Monsieur</b> à la prof et au prof.</p></div>''')
    e12 = E("Dans ma langue : j'écris les mots de la leçon (ou je les dis à la prof).", "<p class='sm muted'>Je complète la dernière colonne de la leçon.</p>", ["ecris"], 1,
            sol="Réponses personnelles. Valoriser les langues des élèves ; possibilité de créer une affiche multilingue de la classe.")
    e13 = E("Jeu de rôle : je joue la scène avec un camarade.", '''<div class="grid3">
<div class="card"><b>Scène 1</b><p class="sm">Tu arrives à l'école le matin. Tu vois ton copain.</p></div>
<div class="card"><b>Scène 2</b><p class="sm">Tu rentres à la maison. Tu dis au revoir à la prof.</p></div>
<div class="card"><b>Scène 3</b><p class="sm">Tu rencontres le directeur dans le couloir.</p></div></div>''', ["parle", "duo"], 2, "A",
        sol="1. Salut ! Ça va ? — Ça va bien, et toi ? · 2. Au revoir, Madame ! À demain ! · 3. Bonjour, Monsieur ! (vouvoiement)")
    e13b = E("Tu ou vous ? J'écoute la phrase et je coche.", table(["", "1", "2", "3", "4", "5", "6"], [["👕 tu"] + ['<span class="chk"></span>'] * 6, ["👔 vous"] + ['<span class="chk"></span>'] * 6], ["30mm"] + ["25mm"] * 6),
             ["ecoute", "coche"], 2, "A", script="Lire deux fois : 1. Salut Amina ! Ça va ? — 2. Bonjour Madame, vous allez bien ? — 3. Au revoir Monsieur ! — 4. Salut ! À demain ! — 5. Bonsoir Madame ! — 6. Ça va, Yonas ?",
             sol="1. tu — 2. vous — 3. vous — 4. tu — 5. vous — 6. tu")
    b.page(f'{l1}{e12}{e13}{e13b}', "Leçon 1")

    # ================= CONSIGNES 1 =================
    imp = [("ecoute", "Écoute !", "J'écoute."), ("parle", "Parle !", "Je parle."), ("lis", "Lis !", "Je lis."), ("ecris", "Écris !", "J'écris."),
           ("regarde", "Regarde !", "Je regarde."), ("repete", "Répète !", "Je répète."), ("entoure", "Entoure !", "J'entoure."), ("souligne", "Souligne !", "Je souligne."),
           ("relie", "Relie !", "Je relie."), ("coche", "Coche !", "Je coche."), ("colorie", "Colorie !", "Je colorie."), ("barre", "Barre !", "Je barre.")]
    imp2 = [("complete", "Complète !", "Je complète."), ("recopie", "Recopie !", "Je recopie."), ("decoupe", "Découpe !", "Je découpe."), ("colle", "Colle !", "Je colle."),
            ("dessine", "Dessine !", "Je dessine."), ("trace", "Trace !", "Je trace."), ("numerote", "Numérote !", "Je numérote."), ("montre", "Montre !", "Je montre."),
            ("joue", "Joue !", "Je joue."), ("seul", "Travaille seul !", "Je travaille seul."), ("duo", "Travaille à deux !", "Je travaille à deux."), ("groupe", "Travaillez en groupe !", "Je travaille en groupe.")]

    def pcards(lst):
        return '<div class="grid4">' + "".join(f'<div class="card c" style="padding:2.5mm">{picto(k, 52)}<div class="word" style="font-size:12pt;margin-top:1mm">{a}</div><div class="sm muted">{c}</div></div>' for k, a, c in lst) + '</div>'
    e14 = E("Les consignes de la classe (1). J'écoute, je regarde, je fais le geste.", pcards(imp), ["ecoute", "regarde", "montre"], 1, "P",
            script="Jeu « Jacques a dit » : la prof dit une consigne (« Écoute ! », « Lis ! »…) et les élèves font le geste correspondant (main à l'oreille, livre ouvert, crayon…). Puis la prof montre un pictogramme sans parler : les élèves disent la consigne.",
            sol="Activité orale et gestuelle. Proposer un geste fixe par consigne et le garder toute l'année.")
    b.page(f'<h2>Les consignes · Ce que la prof dit</h2><p>Dans ce livre, chaque exercice a des petits dessins : les <b>pictogrammes</b>. Ils disent ce que tu dois faire.</p>{e14}', "Consignes")
    e15 = E("Les consignes de la classe (2).", pcards(imp2), ["ecoute", "regarde", "montre"], 1, "P",
            script="Même jeu avec la 2e série. Ajouter : la prof dit « Travaille seul ! » / « Travaillez à deux ! » / « Travaillez en groupe ! » et les élèves se déplacent.",
            sol="Activité orale et gestuelle.")
    e15b = E("J'écoute la prof. Je numérote les pictogrammes dans l'ordre (1 à 6).", '<div class="grid6">' + "".join(f'<div class="card c">{picto(k, 48)}<div class="circ" style="margin:2mm auto 0 auto"></div></div>' for k in ["coche", "ecris", "decoupe", "ecoute", "colle", "lis"]) + '</div>',
              ["ecoute", "numerote"], 2, "A", script="Lire deux fois : « 1. Lis ! — 2. Écoute ! — 3. Découpe ! — 4. Colle ! — 5. Écris ! — 6. Coche ! »",
              sol="Dans l'ordre affiché : coche 6 · écris 5 · découpe 3 · écoute 2 · colle 4 · lis 1")
    b.page(f'{e15}{e15b}<div class="astuce"><b>Astuce :</b> découpe les cartes des consignes de la page des jeux et colle-les sur ta table ou dans ton cahier.</div>', "Consignes")

    # ================= CONSIGNES : exercices =================
    e16 = E("Je relie le pictogramme et la consigne.", relie([picto(k, 40) for k in ["lis", "entoure", "relie", "ecris", "ecoute", "coche"]],
            ["Écoute !", "Coche !", "Lis !", "Relie !", "Écris !", "Entoure !"]), ["relie"], 1, "B",
            sol="Lis → Lis ! · entoure → Entoure ! · relie → Relie ! · écris → Écris ! · écoute → Écoute ! · coche → Coche !")
    e17 = E("Je fais la consigne.", f'''<div class="grid2">
<div class="card"><div class="flex">{picto("entoure", 32)}<b>Entoure</b> le chat.</div><div class="c" style="font-size:30pt">🐶 🐱 🐟 🐦</div></div>
<div class="card"><div class="flex">{picto("barre", 32)}<b>Barre</b> le chien.</div><div class="c" style="font-size:30pt">🐱 🐶 🐟 🐦</div></div>
<div class="card"><div class="flex">{picto("souligne", 32)}<b>Souligne</b> le mot <i>bonjour</i>.</div><p class="c big">merci · salut · bonjour · au revoir</p></div>
<div class="card"><div class="flex">{picto("coche", 32)}<b>Coche</b> la pomme.</div><div class="c" style="font-size:24pt"><span class="chk"></span>🍌 <span class="chk"></span>🍎 <span class="chk"></span>🍊</div></div>
<div class="card"><div class="flex">{picto("colorie", 32)}<b>Colorie</b> le cercle en rouge.</div><svg viewBox="0 0 120 30" width="100%" height="22mm"><circle cx="20" cy="15" r="12" fill="none" stroke="#1F2A44" stroke-width="1.5"/><rect x="50" y="3" width="24" height="24" fill="none" stroke="#1F2A44" stroke-width="1.5"/><path d="M95 27 L107 3 L119 27Z" fill="none" stroke="#1F2A44" stroke-width="1.5"/></svg></div>
<div class="card"><div class="flex">{picto("numerote", 32)}<b>Numérote</b> de 1 à 3.</div><div class="c" style="font-size:24pt">🍰 <span class="circ"></span> &nbsp;🧁 <span class="circ"></span> &nbsp;🍪 <span class="circ"></span></div><p class="xs muted c">grand → petit</p></div>
</div>''', ["lis", "regarde"], 2, "C",
            sol="Entoure le chat (2e image) · barre le chien (2e image) · souligne « bonjour » · coche la pomme · colorie le cercle (1re forme) en rouge · numérote 🍰 1, 🧁 2, 🍪 3 (du plus grand au plus petit).")
    e18 = E("Défi ! J'écris la consigne sous le pictogramme.", '<div class="grid6">' + "".join(f'<div class="card c">{picto(k, 44)}<div class="line" style="height:8mm"></div></div>' for k in ["regarde", "decoupe", "colle", "dessine", "recopie", "repete"]) + '</div>',
            ["ecris"], 3, "C", sol="Regarde ! · Découpe ! · Colle ! · Dessine ! · Recopie ! · Répète !")
    b.page(f'{e16}{e17}{e18}', "Consignes")

    # ================= LEÇON 2 : CONSIGNES =================
    l2 = lecon("Comprendre les consignes", f'''
<div class="grid2"><div>
<p>La prof dit : <b>Écoute !</b> → Je fais : <b>J'écoute.</b></p>
<p>La prof dit : <b>Lis !</b> → Je fais : <b>Je lis.</b></p>
<p>La prof dit : <b>Écris !</b> → Je fais : <b>J'écris.</b></p>
<p class="mt2">Avec <b>tout le groupe</b>, la prof dit : <b>Écoutez !</b> <b>Lisez !</b> <b>Écrivez !</b></p>
</div><div>
<table class="t" style="background:#fff"><tr><th>Avec un picto</th><th>La consigne</th></tr>
<tr><td>{picto("ecoute", 26)}{picto("entoure", 26)}</td><td>J'écoute et j'entoure.</td></tr>
<tr><td>{picto("lis", 26)}{picto("relie", 26)}</td><td>Je lis et je relie.</td></tr>
<tr><td>{picto("ecris", 26)}{picto("duo", 26)}</td><td>J'écris avec un camarade.</td></tr>
</table></div></div>
<div class="attention" style="margin-bottom:0"><b>Je ne comprends pas la consigne ?</b> Je lève la main ✋ et je dis : <b>« Je ne comprends pas. Vous pouvez répéter, s'il vous plaît ? »</b></div>''')
    e19 = E("Je lis les deux pictogrammes et je dis la consigne.", '<div class="grid4">' + "".join(
        f'<div class="card c">{picto(a, 36)}{picto(c, 36)}<div class="line" style="height:7mm"></div></div>' for a, c in [("ecoute", "repete"), ("lis", "souligne"), ("regarde", "coche"), ("decoupe", "colle")]) + '</div>',
        ["lis", "parle"], 2, "A", sol="J'écoute et je répète. · Je lis et je souligne. · Je regarde et je coche. · Je découpe et je colle.")
    e20 = E("Défi ! Je dessine les pictogrammes de la consigne.", '<div class="grid3">' + "".join(
        f'<div class="card"><p class="sm">{t}</p><div style="height:20mm;border:1.5px dashed #b9bfcc;border-radius:2mm"></div></div>' for t in ["J'écoute et j'entoure.", "Je lis et je relie.", "Je regarde et je colorie."]) + '</div>',
        ["dessine"], 3, "C", sol="Écoute + entoure · Lis + relie · Regarde + colorie (dessins des pictogrammes, approximatifs acceptés).")
    def choix(cons, ks):
        return f'<div class="card"><p class="sm"><b>{cons}</b></p><div class="flex" style="gap:2mm">' + "".join(picto(k, 34) for k in ks) + '</div></div>'
    e20b = E("Je lis la consigne. J'entoure les 2 bons pictogrammes.", '<div class="grid2">' + choix("J'écoute et je répète.", ["lis", "ecoute", "repete", "coche"]) + choix("Je découpe et je colle.", ["colle", "dessine", "decoupe", "relie"]) +
             choix("Je lis et je souligne.", ["souligne", "ecris", "barre", "lis"]) + choix("Je regarde et je dessine.", ["colorie", "regarde", "dessine", "montre"]) + '</div>', ["lis", "entoure"], 2, "B",
             sol="1. écoute + répète — 2. colle + découpe — 3. souligne + lis — 4. regarde + dessine")
    b.page(f'{l2}{e19}{e20}{e20b}', "Leçon 2")

    # ================= DOCUMENT DE LA VIE 1 : CARTE D'ÉLÈVE =================
    carte = f'''<div class="doc" style="width:150mm;margin:4mm auto 6mm auto;border-radius:5mm;overflow:hidden;border:1px solid #ddd">
<div style="background:#1F4E79;color:#fff;padding:3mm 5mm;display:flex;justify-content:space-between;align-items:center">
 <div><div style="font-size:13pt;font-weight:800">ATHÉNÉE DES TILLEULS</div><div style="font-size:8pt;opacity:.85">Rue des Tilleuls 24 · 5000 Namur · 081 00 00 00</div></div>
 <div style="font-size:22pt">🌳</div></div>
<div style="display:flex;gap:5mm;padding:4mm 5mm;background:linear-gradient(135deg,#fff 60%,#E8F0F8)">
 <div style="width:32mm;height:40mm;background:#DDE6F0;border-radius:2mm;display:flex;align-items:flex-end;justify-content:center;overflow:hidden">{avatar("mateo", 120)}</div>
 <div style="font-size:10.5pt;line-height:1.75">
  <div style="font-size:8pt;color:#1F4E79;font-weight:700;letter-spacing:1px">CARTE D'ÉLÈVE · 2026–2027</div>
  <div><span class="muted sm">NOM :</span> <b>RAMÍREZ</b></div>
  <div><span class="muted sm">Prénom :</span> <b>Mateo</b></div>
  <div><span class="muted sm">Né le :</span> <b>03/05/2011</b></div>
  <div><span class="muted sm">Classe :</span> <b>DASPA B</b></div>
  <div><span class="muted sm">N° d'élève :</span> <b>26-0417</b></div>
 </div>
 <div style="margin-left:auto;align-self:flex-end;text-align:center"><svg viewBox="0 0 60 24" width="34mm">{"".join(f'<rect x="{i*2}" y="0" width="{1 if i%3 else 1.6}" height="20" fill="#1F2A44"/>' for i in range(29))}</svg><div class="xs">26-0417</div></div>
</div>
<div style="background:#F2B705;padding:1.5mm 5mm;font-size:8pt;font-weight:700">Cette carte est personnelle. Montre-la à l'entrée et à la bibliothèque.</div>
</div>'''
    e21 = E("Je regarde la carte. Je réponds avec mes mots ou avec un geste.", '<p>Qu\'est-ce que c\'est ? C\'est pour qui ? C\'est pour quoi ? Tu as une carte comme ça ?</p>', ["regarde", "parle"], 1, "P",
            sol="C'est une carte d'élève. C'est la carte de Mateo. Elle sert à entrer dans l'école, à la bibliothèque, à prouver qu'on est élève de l'école.")
    e22 = E("J'entoure le NOM en rouge 🔴 et le prénom en bleu 🔵 sur la carte.", '<div class="astuce" style="margin:0"><b>Le NOM</b> = le nom de la famille (souvent en MAJUSCULES). <b>Le prénom</b> = le nom de la personne. <br>Mateo RAMÍREZ : le prénom = <b>Mateo</b>, le NOM = <b>RAMÍREZ</b>.</div>', ["entoure", "colorie"], 1, "B",
            sol="NOM en rouge : RAMÍREZ — prénom en bleu : Mateo.")
    e22b = E("Vrai ou faux ? Je coche.", table(["", "Vrai", "Faux"], [[x, '<span class="chk"></span>', '<span class="chk"></span>'] for x in ["L'élève s'appelle Mateo.", "L'école est à Liège.", "La carte est pour l'année 2026–2027.", "Mateo est dans la classe DASPA A."]], ["130mm", "25mm", "25mm"]),
              ["lis", "coche"], 2, "B", sol="1. Vrai — 2. Faux (Namur) — 3. Vrai — 4. Faux (DASPA B)")
    b.page(f'<span class="tag-doc">📄 DOCUMENT DE LA VIE</span><h2>La carte d\'élève</h2>{carte}{e21}{e22}{e22b}', "Document de la vie")

    e23 = E("Je lis la carte et je réponds.", f'''
<p>1. Le prénom de l'élève : {blank("l")}</p><p>2. Le nom de l'élève : {blank("l")}</p><p>3. La classe : {blank()}</p>
<p>4. Le nom de l'école : {blank("xl")}</p><p>5. La ville de l'école : {blank()}</p>''', ["lis", "ecris"], 2, "B",
            sol="1. Mateo — 2. RAMÍREZ — 3. DASPA B — 4. Athénée des Tilleuls — 5. Namur")
    e24 = E("Mateo est né le 03/05/2011. Quel âge a Mateo en 2026 ? J'entoure.", '<p class="big c"><span class="pill">13 ans</span> <span class="pill">14 ans</span> <span class="pill">15 ans</span> <span class="pill">16 ans</span></p>'
            '<p class="sm muted c">03/05/2011 = le 3 mai 2011 (jour / mois / année)</p>', ["lis", "entoure"], 3, "B",
            sol="15 ans (2026 − 2011 = 15 ; son anniversaire, le 3 mai, est passé à la rentrée).")
    mycard = f'''<div class="doc" style="width:150mm;margin:2mm auto;border-radius:5mm;overflow:hidden;border:1px solid #ccc;transform:none">
<div style="background:#1F4E79;color:#fff;padding:3mm 5mm;font-weight:800">MA CARTE D'ÉLÈVE · 2026–2027</div>
<div style="display:flex;gap:5mm;padding:4mm 5mm"><div style="width:32mm;height:40mm;border:2px dashed #9aa1b1;border-radius:2mm;display:flex;align-items:center;justify-content:center;text-align:center" class="xs muted">ma photo<br>ou<br>mon dessin</div>
<div class="grow" style="line-height:2.3"><div>NOM : {blank("l")}</div><div>Prénom : {blank("l")}</div><div>Né(e) le : {blank()}</div><div>Classe : {blank()}</div></div></div></div>'''
    e25 = E("Je fais ma carte d'élève.", mycard, ["ecris", "dessine"], 2, "C", sol="Réponses personnelles. Vérifier : NOM en majuscules, date au format jj/mm/aaaa.")
    b.page(f'{e23}{e24}{e25}', "Document de la vie")

    # ================= DOCUMENT 2 : FICHE D'INSCRIPTION =================
    fiche = f'''<div class="doc" style="padding:6mm 7mm;border:1px solid #ccc;margin:2mm 0 5mm 0">
<div class="flex" style="justify-content:space-between;border-bottom:2px solid #1F4E79;padding-bottom:2mm"><div><b style="color:#1F4E79">ATHÉNÉE DES TILLEULS</b><div class="xs muted">Secrétariat des élèves</div></div><div style="font-weight:800;font-size:13pt">FICHE D'INSCRIPTION</div></div>
<div style="font-family:Inter;font-size:10.5pt;line-height:2.1;margin-top:3mm">
<div style="display:grid;grid-template-columns:42mm 1fr">
<span class="muted">NOM :</span><span style="font-family:'TeX Gyre Chorus',cursive;font-size:15pt;color:#1a3a8a">Camara</span>
<span class="muted">Prénom :</span><span style="font-family:'TeX Gyre Chorus';font-size:15pt;color:#1a3a8a">Fatou</span>
<span class="muted">Sexe :</span><span>☐ M &nbsp;&nbsp; ☒ F</span>
<span class="muted">Date de naissance :</span><span style="font-family:'TeX Gyre Chorus';font-size:15pt;color:#1a3a8a">12 / 02 / 2012</span>
<span class="muted">Pays de naissance :</span><span style="font-family:'TeX Gyre Chorus';font-size:15pt;color:#1a3a8a">Guinée</span>
<span class="muted">Langue(s) parlée(s) :</span><span style="font-family:'TeX Gyre Chorus';font-size:15pt;color:#1a3a8a">peul, soussou, un peu de français</span>
<span class="muted">Adresse :</span><span style="font-family:'TeX Gyre Chorus';font-size:15pt;color:#1a3a8a">Rue du Marché 8, 5000 Namur</span>
<span class="muted">Téléphone (parent) :</span><span style="font-family:'TeX Gyre Chorus';font-size:15pt;color:#1a3a8a">0470 00 00 00</span>
<span class="muted">Classe :</span><span>DASPA B</span>
</div></div>
<div class="flex xs muted" style="justify-content:space-between;margin-top:2mm"><span>Date : 20/08/2026</span><span>Signature du parent : <span style="font-family:'TeX Gyre Chorus';font-size:14pt;color:#1a3a8a">A. Camara</span></span></div></div>'''
    e26 = E("Je lis la fiche de Fatou. Je souligne les réponses.", '<p class="sm">Le prénom · le pays · les langues · l\'adresse</p>', ["lis", "souligne"], 1, "B",
            sol="Prénom : Fatou · pays de naissance : Guinée · langues : peul, soussou, un peu de français · adresse : Rue du Marché 8, 5000 Namur.")
    e27 = E("Je réponds aux questions.", f'''
<div class="grid2"><div><p>1. Fatou est un garçon ou une fille ? {blank()}</p><p>2. Fatou est née en quelle année ? {blank()}</p><p>3. Fatou habite dans quelle ville ? {blank()}</p></div>
<div><p>4. Fatou parle combien de langues ? {blank("s")}</p><p>5. Qui signe la fiche ? {blank()}</p><p>6. Fatou a quel âge ? {blank("s")} ans</p></div></div>''', ["lis", "ecris"], 2, "B",
            sol="1. une fille (F coché) — 2. en 2012 — 3. à Namur — 4. trois (peul, soussou, français) — 5. le parent (A. Camara) — 6. 14 ans")
    b.page(f'<span class="tag-doc">📄 DOCUMENT DE LA VIE</span><h2>La fiche d\'inscription</h2>{fiche}{e26}{e27}', "Document de la vie")

    words_fiche = ["NOM", "Prénom", "Date de naissance", "Pays de naissance", "Langues", "Adresse", "Téléphone", "Signature"]
    e28 = E("Je relie le mot de la fiche et l'image.", relie(
        [f'<b>{w}</b>' for w in ["Date de naissance", "Adresse", "Téléphone", "Signature", "Langues"]],
        ['<span class="emo s">🏠</span>', '<span class="emo s">✍️</span>', '<span class="emo s">🎂</span>', '<span class="emo s">🗣️</span>', '<span class="emo s">📞</span>']), ["relie"], 1, "B",
        sol="Date de naissance → 🎂 · Adresse → 🏠 · Téléphone → 📞 · Signature → ✍️ · Langues → 🗣️")
    myfiche = f'''<div class="card" style="font-size:11pt;line-height:2.3"><div style="display:grid;grid-template-columns:48mm 1fr">
{"".join(f'<span><b>{w} :</b></span><span>{blank("xl")}</span>' for w in ["NOM", "Prénom", "Date de naissance", "Pays de naissance", "Langue(s)", "Ville"])}
<span><b>Sexe :</b></span><span><span class="chk"></span>M &nbsp;&nbsp;<span class="chk"></span>F</span></div></div>'''
    e29 = E("Je remplis ma fiche d'inscription.", myfiche + '<div class="attention mt2" style="margin-bottom:0">⚠️ Je ne donne pas mon adresse ou mon téléphone à n\'importe qui ! Seulement à l\'école, à la commune, au médecin…</div>', ["ecris"], 2, "C",
            sol="Réponses personnelles. Vérifier les majuscules (NOM, ville, pays) et le format de la date.")
    lieux = [("🏫", "à l'école"), ("🏥", "chez le médecin"), ("🏛️", "à la commune"), ("🛒", "au supermarché"), ("📚", "à la bibliothèque"), ("🎮", "sur un jeu en ligne")]
    e29b = E("Où est-ce que je donne mon nom et mon adresse ? Je coche ✅ oui ou ❌ non. Je discute avec la classe.", '<div class="grid6">' + "".join(f'<div class="card c"><span class="emo s">{e}</span><div class="xs">{t}</div><div class="mt2"><span class="chk"></span>✅ <span class="chk"></span>❌</div></div>' for e, t in lieux) + '</div>',
              ["regarde", "coche", "groupe"], 3, "P", sol="Oui : école, médecin, commune, bibliothèque (inscription). Non : supermarché (sauf carte de fidélité, au choix), jeu en ligne (jamais son adresse !). Discussion sur la protection des données personnelles.")
    b.page(f'{e28}{e29}{e29b}', "Document de la vie")

    # ================= LEÇON 3 : SE PRÉSENTER =================
    l3 = lecon("Se présenter", f'''
<table class="t" style="background:#fff">
<tr><th style="width:42%">Je demande ❓</th><th>Je réponds 💬</th></tr>
<tr><td>Comment tu t'appelles ?</td><td><b>Je m'appelle</b> Amina. / <b>Moi, c'est</b> Amina.</td></tr>
<tr><td>Tu as quel âge ?</td><td><b>J'ai</b> 15 <b>ans</b>.</td></tr>
<tr><td>Tu viens d'où ?</td><td><b>Je viens de</b> Syrie. / <b>Je viens du</b> Maroc. / <b>Je viens d'</b>Ukraine.</td></tr>
<tr><td>Tu habites où ?</td><td><b>J'habite à</b> Namur.</td></tr>
<tr><td>Tu parles quelles langues ?</td><td><b>Je parle</b> arabe et un peu français.</td></tr>
</table>
<div class="grid2 mt2"><div class="attention" style="margin:0"><b>⚠️ L'âge :</b> J'<b>ai</b> 15 ans. ✅<br>Je <s>suis</s> 15 ans. ❌</div>
<div class="astuce" style="margin:0"><b>Avec la prof :</b> Comment <b>vous</b> vous appelez ? Vous venez d'où ?</div></div>''')
    e30 = E("J'écoute et je répète les questions. Je pose les questions à mon voisin.", '<p class="sm">Je note ses réponses :</p>' + "".join(f'<p>{q} {blank("l")}</p>' for q in ["Prénom :", "Âge :", "Pays :", "Langues :"]), ["ecoute", "repete", "duo"], 1, "A",
            script="Lire chaque question de la leçon avec une intonation montante bien marquée. Faire répéter. Puis faire une chaîne : chaque élève pose une question à son voisin de droite.",
            sol="Réponses personnelles.")
    e30b = E("Question ou réponse ? J'écoute la voix. J'écris ? ou . à la fin.", '<div class="grid2">' + "".join(f'<p class="big">{i}. {t} <span class="blank s"></span></p>' for i, t in enumerate(["Tu as quel âge", "Je viens de Guinée", "Tu viens d'où", "Tu parles arabe", "J'habite à Namur", "Ça va"], 1)) + '</div>'
              '<div class="astuce" style="margin-bottom:0">La question : la voix monte ↗ à la fin. La réponse : la voix descend ↘.</div>', ["ecoute", "ecris"], 2, "A",
              script="Lire avec une intonation très marquée : 1. Tu as quel âge ? ↗ — 2. Je viens de Guinée. ↘ — 3. Tu viens d'où ? ↗ — 4. Tu parles arabe ? ↗ (question par l'intonation seule) — 5. J'habite à Namur. ↘ — 6. Ça va ? ↗",
              sol="1. ? — 2. . — 3. ? — 4. ? — 5. . — 6. ?")
    b.page(f'{l3}{e30}{e30b}', "Leçon 3")

    # ================= QUI EST-CE ? =================
    cards = "".join(f'''<div class="card" style="padding:2.5mm"><div class="flex" style="gap:2mm">{avatar(k, 60)}<div style="font-size:9.5pt;line-height:1.35"><b style="font-size:11pt">{p} {n}</b><br>🎂 {a} ans<br>🌍 {pays}<br>🗣️ {lg}</div></div></div>''' for k, p, n, a, pays, de, lg in CAST_INFO)
    e31 = E("Je lis les cartes des élèves de la classe.", f'<div class="grid3">{cards}</div>', ["lis"], 1, "B")
    e32 = E("Qui est-ce ? J'écris le prénom.", f'''
<p>1. J'ai 16 ans. Je viens d'Afghanistan. → {blank()}</p>
<p>2. Je viens de Guinée. Je parle peul et soussou. → {blank()}</p>
<p>3. J'ai 13 ans. Je parle ukrainien. → {blank()}</p>
<p>4. Je viens de Colombie. Je parle espagnol. → {blank()}</p>
<p>5. J'ai 15 ans. Je parle arabe. → {blank()}</p>''', ["lis", "ecris"], 1, "B", sol="1. Bilal — 2. Fatou — 3. Daria — 4. Mateo — 5. Amina")
    e33 = E("J'écris la présentation de Bilal (avec « je »).", f'''<div class="flex top">{avatar("bilal", 60, "sourire")}<div class="grow">{lines(4)}</div></div>''', ["ecris"], 2, "C",
            sol="Je m'appelle Bilal (Ahmadi). J'ai 16 ans. Je viens d'Afghanistan. Je parle dari et pachto.")
    e34 = E("Défi ! J'écris la présentation de Fatou avec « elle ».", f'<p class="sm muted">Exemple : Elle s\'appelle… Elle a … ans. Elle vient de… Elle parle…</p>{lines(3)}', ["ecris"], 3, "C",
            sol="Elle s'appelle Fatou (Camara). Elle a 14 ans. Elle vient de Guinée. Elle parle peul, soussou et un peu français.")
    b.page(f'{e31}{e32}{e33}{e34}', "S'entraîner")

    # ================= DIALOGUE EN ORDRE =================
    L = {1: ("mateo", "Bonjour ! Je m'appelle Mateo. Et toi ?"), 2: ("amina", "Moi, c'est Amina. Tu as quel âge ?"), 3: ("mateo", "J'ai 15 ans. Et toi ?"),
         4: ("amina", "Moi aussi, j'ai 15 ans ! Tu viens d'où ?"), 5: ("mateo", "Je viens de Colombie. Et toi ?"), 6: ("amina", "Je viens de Syrie.")}
    order = [2, 1, 5, 6, 3, 4]
    e35 = E("Je remets le dialogue dans l'ordre. Je numérote de 1 à 6.", '<div class="card">' + "".join(
        f'<div class="flex mb2"><span class="circ"></span>{avatar(L[k][0], 38)}<span>{L[k][1]}</span></div>' for k in order) + '</div>', ["lis", "numerote"], 2, "B",
        sol="Ordre des lignes dans l'exercice : 2 – 1 – 5 – 6 – 3 – 4. Dialogue : Bonjour ! Je m'appelle Mateo. Et toi ? / Moi, c'est Amina. Tu as quel âge ? / J'ai 15 ans. Et toi ? / Moi aussi, j'ai 15 ans ! Tu viens d'où ? / Je viens de Colombie. Et toi ? / Je viens de Syrie.")
    e36 = E("Je trouve la bonne réponse. Je relie.", relie(["Comment tu t'appelles ?", "Tu as quel âge ?", "Tu viens d'où ?", "Tu habites où ?", "Ça va ?"],
            ["J'habite à Namur.", "Ça va bien, merci.", "Je m'appelle Yonas.", "Je viens du Maroc.", "J'ai 14 ans."]), ["relie"], 1, "B",
            sol="Comment tu t'appelles ? → Je m'appelle Yonas. · Tu as quel âge ? → J'ai 14 ans. · Tu viens d'où ? → Je viens du Maroc. · Tu habites où ? → J'habite à Namur. · Ça va ? → Ça va bien, merci.")
    e37 = E("Défi ! J'écris la question.", f'''
<p>1. {blank("xl")} ? — Je m'appelle Daria.</p><p>2. {blank("xl")} ? — J'ai 13 ans.</p><p>3. {blank("xl")} ? — Je viens d'Ukraine.</p>''', ["ecris"], 3, "C",
            sol="1. Comment tu t'appelles ? — 2. Tu as quel âge ? — 3. Tu viens d'où ?")
    e37b = E("Je joue le dialogue avec un camarade. Puis on change les prénoms, les âges et les pays.", '<div class="card flex">' + avatar("mateo", 50, "rire") + avatar("amina", 50, "rire", flip=True) + '<p class="sm grow">Exemple : « Bonjour ! Je m\'appelle <u>Sami</u>. Et toi ? — Moi, c\'est <u>Ana</u>. Tu as quel âge ? … »</p></div>',
              ["parle", "duo"], 2, "A", sol="Production orale libre ; vérifier les 4 questions et la forme « J'ai … ans ».")
    b.page(f'{e35}{e36}{e37}{e37b}', "S'entraîner")

    # ================= PAYS ET LANGUES =================
    pays = [("Syrie", "de Syrie", "l'arabe"), ("Ukraine", "d'Ukraine", "l'ukrainien"), ("Érythrée", "d'Érythrée", "le tigrinya"), ("Afghanistan", "d'Afghanistan", "le dari, le pachto"),
            ("Guinée", "de Guinée", "le peul, le soussou"), ("Colombie", "de Colombie", "l'espagnol"), ("Maroc", "du Maroc", "l'arabe, l'amazigh"), ("Brésil", "du Brésil", "le portugais"),
            ("Congo (RDC)", "du Congo", "le lingala, le swahili"), ("Roumanie", "de Roumanie", "le roumain"), ("Turquie", "de Turquie", "le turc"), ("Palestine", "de Palestine", "l'arabe")]
    pt = table(["Pays", "Je viens…", "On parle…"], [[f"<b>{p}</b>", f"Je viens <b>{d}</b>.", l] for p, d, l in pays], ["40mm", "70mm", "72mm"])
    l4 = lecon("Je viens de… · Je parle…", f'''{pt}
<p class="mt2">Mon pays : <b>Je viens {blank("l")}</b> &nbsp;&nbsp; Mes langues : <b>Je parle {blank("l")}</b>.</p>
<p class="sm muted">Ton pays n'est pas dans la liste ? Demande à la prof et écris-le ici.</p>''')
    b.page(f'<h2>Les pays et les langues de la classe</h2>{l4}', "Pays et langues")

    e38 = E("Je complète avec de, d' ou du.", f'''<div class="grid2">
<p>1. Je viens {blank("s")} Syrie.</p><p>2. Je viens {blank("s")} Ukraine.</p><p>3. Je viens {blank("s")} Maroc.</p>
<p>4. Je viens {blank("s")} Guinée.</p><p>5. Je viens {blank("s")} Afghanistan.</p><p>6. Je viens {blank("s")} Brésil.</p></div>
<div class="astuce" style="margin-bottom:0">Je regarde la leçon ! d' → devant a, e, i, o, u, é (Afghanistan, Ukraine, Érythrée).</div>''', ["complete"], 2, "C",
            sol="1. de — 2. d' — 3. du — 4. de — 5. d' — 6. du")
    e39 = E("Enquête dans la classe : je pose la question à 5 camarades.", table(["Prénom", "Tu viens d'où ?", "Tu parles quelles langues ?"], [["", "", ""] for _ in range(5)], ["50mm", "66mm", "66mm"]).replace("<td></td>", '<td style="height:10mm"></td>'),
            ["parle", "ecris", "groupe"], 2, "A", sol="Réponses personnelles. Exploiter les résultats : combien de pays ? combien de langues dans la classe ?")
    e40 = E("Défi ! Dans notre classe, on parle … langues. J'écris la liste.", lines(2), ["ecris"], 3, "C", sol="Réponse selon la classe.")
    e40b = E("« Bonjour » dans les langues du monde. Je relie.", relie(["<b>Hola !</b>", "<b>Hello !</b>", "<b>Olá !</b>", "<b>Merhaba !</b>", "<b>Привіт !</b>", "<b>مرحبا</b>"],
              ["le portugais", "l'arabe", "l'espagnol", "l'ukrainien", "l'anglais", "le turc"]), ["lis", "relie"], 2, "B",
              sol="Hola → espagnol · Hello → anglais · Olá → portugais · Merhaba → turc · Привіт → ukrainien · مرحبا → arabe")
    b.page(f'{e38}{e39}{e40}{e40b}', "Pays et langues")
