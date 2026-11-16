"""Volume 1 · Module 12 « Hier et demain » (+ bilan A1)."""
import sys
sys.path.insert(0, '/home/claude/syllabus')
from lib.base import *
from lib.art import *
from lib.alpha import AL, letter_page, syll_table
from lib.module import *
from lib.render import to_pdf

MC = "#283593"
TEMPS = [("⬅️⬅️", "avant-hier"), ("⬅️", "hier"), ("📍", "aujourd'hui"), ("➡️", "demain"), ("➡️➡️", "après-demain")]
PP = [("manger", "mangé"), ("jouer", "joué"), ("regarder", "regardé"), ("parler", "parlé"), ("visiter", "visité"), ("acheter", "acheté"), ("faire", "fait ⚠️"), ("prendre", "pris ⚠️"),
      ("voir", "vu ⚠️"), ("lire", "lu ⚠️"), ("boire", "bu ⚠️"), ("avoir", "eu ⚠️"), ("être", "été ⚠️"), ("écrire", "écrit ⚠️"), ("dormir", "dormi"), ("finir", "fini")]


def frise(marks):
    """Frise passé / présent / futur avec des repères."""
    pts = "".join(f'<line x1="{x}" y1="9" x2="{x}" y2="17" stroke="#1F2A44"/><text x="{x}" y="{23 + 6 * (i % 2)}" font-size="4.6" text-anchor="middle" font-family="Poppins" font-weight="600">{t}</text>' for i, (x, t) in enumerate(marks))
    return ('<svg viewBox="0 0 180 32" width="100%"><rect x="5" y="2" width="70" height="6" rx="2" fill="#B3C7F7"/><rect x="80" y="2" width="20" height="6" rx="2" fill="#FFD166"/><rect x="105" y="2" width="70" height="6" rx="2" fill="#B6E2C8"/>'
            '<text x="40" y="6.8" font-size="4.5" text-anchor="middle" font-family="Poppins" font-weight="800">PASSÉ</text><text x="90" y="6.8" font-size="4" text-anchor="middle" font-family="Poppins" font-weight="800">PRÉSENT</text><text x="140" y="6.8" font-size="4.5" text-anchor="middle" font-family="Poppins" font-weight="800">FUTUR</text>'
            f'<line x1="5" y1="13" x2="175" y2="13" stroke="#1F2A44" stroke-width="1.2"/><path d="M175 13 l-4 -3 v6z" fill="#1F2A44"/>{pts}</svg>')


def build_m12(start=1, tstart=1, render=True):
    b = Book("V1 · M12", "Volume 1 · Premiers pas · Module 12 · Hier et demain", MC, start=start)
    E = Ex(b)
    vis = '<div class="c" style="font-size:40pt;line-height:1.3">📸🏖️🎂⬅️📍➡️<br>🎒✈️🗓️🏆⭐🎓</div>'
    opening(b, MC, 12, "Hier et demain", vis, [("⬅️", "raconter ce que j'ai fait (le passé composé)"), ("➡️", "dire ce que je vais faire (le futur proche)"), ("🗓️", "utiliser hier, aujourd'hui, demain…"),
            ("📸", "raconter un week-end, une excursion"), ("🧭", "reconnaître passé, présent, futur dans une consigne"), ("🏆", "faire le bilan de mon année : je sais faire !")],
            ["Qu'est-ce que tu as fait le week-end dernier ?", "Qu'est-ce que tu vas faire pendant les vacances ?", "Qu'est-ce que tu as appris cette année ?"],
            ["hier", "demain", "le week-end dernier", "la semaine prochaine", "j'ai mangé", "je vais manger", "le passé", "le futur", "l'excursion", "le bilan"], "#E8EAF6")

    # ---------- Découvrir ----------
    bd = '<div class="grid2" style="gap:3mm">' + "".join([
        bd_case(1, lr("prof", ["Bonjour ! Lundi matin… Qu'est-ce que vous avez fait ce week-end ?"], extra='<div class="c" style="font-size:22pt">🗓️❓</div>')),
        bd_case(2, lr("amina", ["Samedi, j'ai fait les courses avec ma mère. Dimanche, j'ai visité Bruxelles !"], extra='<div class="c" style="font-size:22pt">🛒🏙️</div>', ma="rire")),
        bd_case(3, lr("bilal", ["Moi, j'ai joué aux jeux vidéo… et j'ai dormi ! J'ai bien dormi, Madame !"], "prof", ["Bravo, Bilal ! 😄"], "rire", "rire")),
        bd_case(4, lr("daria", ["J'ai eu une bonne nouvelle : mon père a eu un visa. Il arrive bientôt !"], "fatou", ["Oh, c'est génial, Daria !"], "rire", "surpris")),
        bd_case(5, lr("prof", ["Et la semaine prochaine, nous allons faire une excursion au musée !"], "yonas", ["Super ! On va prendre le train ?"], "sourire", "rire")),
        bd_case(6, lr("prof", ["Oui ! Nous allons partir à 8 h. Vous allez écrire un petit texte sur la visite."], "mateo", ["Et après, on va manger des frites ? 🍟"], "sourire", "rire")),
    ]) + '</div>'
    e = E("J'écoute et je regarde la BD : le lundi matin.", bd, ["ecoute", "regarde"], 1, "A",
          script="Lire deux fois. Montrer la main en arrière (⬅️ passé) et en avant (➡️ futur). Faire répéter : « J'ai fait… », « J'ai joué… », « Nous allons partir… ».", sol="Activité orale.")
    b.page(f'<h2>Découvrir · Le lundi matin</h2>{e}', "Découvrir")
    e = E("Je réponds.", f'<p>1. Qu\'est-ce qu\'Amina a fait samedi ? Dimanche ? {blank("xl")}</p><p>2. Qu\'est-ce que Bilal a fait ? {blank("xl")}</p><p>3. Quelle est la bonne nouvelle de Daria ? {blank("xl")}</p><p>4. Qu\'est-ce que la classe va faire la semaine prochaine ? {blank("xl")}</p>',
          ["lis", "ecris"], 1, "B", sol="1. Elle a fait les courses ; elle a visité Bruxelles. — 2. Il a joué aux jeux vidéo et il a dormi. — 3. Son père a eu un visa, il arrive bientôt. — 4. une excursion au musée (en train)")
    e2 = E("C'est passé ⬅️ ou futur ➡️ ?", table(["", "⬅️ passé", "➡️ futur"], [[x, '<span class="chk"></span>', '<span class="chk"></span>'] for x in ["J'ai visité Bruxelles.", "Nous allons faire une excursion.", "J'ai dormi.", "On va prendre le train ?", "Vous allez écrire un texte."]], ["110mm", "36mm", "36mm"]), ["lis", "coche"], 1, "B",
           sol="passé · futur · passé · futur · futur")
    e3 = E("Défi ! Je dis à mon voisin 2 choses que j'ai faites et 1 chose que je vais faire.", lines(2), ["parle", "duo"], 3, "A", sol="J'ai… J'ai… Je vais…")
    b.page(f'{e}{e2}{e3}', "Découvrir")

    # ---------- Lexique : temps ----------
    e = E("Les mots du temps. J'écoute et je répète.", '<div class="grid5">' + "".join(f'<div class="card c"><div style="font-size:18pt">{em}</div><b>{t}</b></div>' for em, t in TEMPS) + '</div>' +
          frise([(20, "le mois dernier"), (45, "la semaine dernière"), (65, "hier"), (90, "maintenant"), (115, "demain"), (140, "la semaine prochaine"), (165, "l'année prochaine")]), ["ecoute", "repete"], 1, "A",
          script="Aujourd'hui, c'est lundi. Hier, c'était dimanche. Demain, ce sera mardi. Faire une frise au tableau avec la date du jour.", sol="Activité orale.")
    e2 = E("Je complète avec hier, aujourd'hui ou demain (aujourd'hui = mercredi).", '<p>1. Mardi, c\'est ______. 2. Jeudi, c\'est ______. 3. Mercredi, c\'est ______.</p><p>4. ______, j\'ai joué au foot. 5. ______, je vais aller à la piscine.</p>', ["complete"], 1, "C", sol="hier · demain · aujourd'hui · Hier · Demain")
    e3 = E("Je relie le mot et le temps.", relie(["le week-end dernier", "maintenant", "la semaine prochaine", "l'année dernière", "ce soir"], ["➡️ futur", "⬅️ passé", "📍 présent", "⬅️ passé", "➡️ futur (proche)"]), ["relie"], 2, "B",
           sol="week-end dernier → passé · maintenant → présent · semaine prochaine → futur · année dernière → passé · ce soir → futur proche")
    b.page(f'<h2>Hier, aujourd\'hui, demain</h2>{e}{e2}{e3}', "Lexique")
    act = [("🛒", "faire les courses"), ("🏙️", "visiter une ville"), ("🎂", "fêter un anniversaire"), ("👵", "rendre visite à sa famille"), ("🎬", "voir un film"), ("🏖️", "aller à la mer"), ("🧹", "ranger sa chambre"), ("🥾", "se promener en forêt"),
           ("🍕", "manger au restaurant"), ("📞", "téléphoner à un ami"), ("🎮", "jouer aux jeux vidéo"), ("🛌", "dormir / se reposer")]
    e = E("Les activités du week-end et des vacances. J'écoute et je répète.", emogrid(act, 6), ["ecoute", "repete"], 1, "A", script="Dire chaque activité. Demander : « Qui a fait ça ce week-end ? » (lever la main).", sol="Activité orale.")
    e2 = E("Sondage : « Qu'est-ce que tu as fait ce week-end ? » Je coche et je compte.", table(["Activité", "Prénoms", "Total"], [[f"{em} {t}", "", ""] for em, t in act[:6]], ["70mm", "84mm", "28mm"]), ["parle", "ecris", "groupe"], 1, "A", sol="Bilan : 5 élèves ont fait les courses…")
    b.page(f'{e}{e2}', "Lexique")

    # ---------- Leçon 1 : passé composé ----------
    l1 = lecon("Le passé composé avec avoir", f'''<p><b>avoir</b> au présent + <b>participe passé</b> = une action finie dans le passé.</p>
<div class="grid2"><div class="card" style="background:#fff"><b>MANGER</b> → mangé<p>j'<b>ai</b> mangé<br>tu <b>as</b> mangé<br>il / elle / on <b>a</b> mangé<br>nous <b>avons</b> mangé<br>vous <b>avez</b> mangé<br>ils / elles <b>ont</b> mangé</p></div>
<div class="card" style="background:#fff"><b>Le participe passé</b><p>verbes en <b>-er</b> → <b>-é</b> : jouer → joué, regarder → regardé</p><p>⚠️ À apprendre par cœur :</p>{table(["", ""], [[f"{a} → <b>{p}</b>"] + [f"{c} → <b>{d}</b>"] for (a, p), (c, d) in zip(PP[6:11], PP[11:16])], ["50%", "50%"])}</div></div>''')
    e = E("J'écris le participe passé.", '<div class="grid4">' + "".join(f'<p>{v} → {blank()}</p>' for v in ["parler", "danser", "faire", "prendre", "voir", "lire", "écouter", "boire"]) + '</div>', ["ecris"], 1, "C",
          sol="parlé · dansé · fait · pris · vu · lu · écouté · bu")
    b.page(f'{l1}{e}', "Leçon 1")
    e = E("Je conjugue au passé composé.", '<p>1. Hier, je (regarder) ______________ un film.</p><p>2. Tu (manger) ______________ des frites ?</p><p>3. Elle (faire) ______________ ses devoirs.</p><p>4. Nous (prendre) ______________ le bus.</p><p>5. Vous (visiter) ______________ le musée.</p><p>6. Ils (voir) ______________ un match.</p>', ["complete"], 2, "C",
          sol="j'ai regardé · as mangé · a fait · avons pris · avez visité · ont vu")
    e2 = E("J'écoute Mateo : qu'est-ce qu'il a fait ce week-end ? Je coche.", '<div class="grid6">' + "".join(f'<div class="card c"><span class="emo">{em}</span><span class="chk"></span></div>' for em in ["⚽", "🎬", "🍕", "📚", "🏊", "👵"]) + '</div>', ["ecoute", "coche"], 2, "A",
           script="Samedi matin, j'ai joué au foot. L'après-midi, j'ai rendu visite à ma grand-mère. Le soir, on a mangé une pizza. Dimanche, j'ai vu un film au cinéma avec mon frère. Je n'ai pas fait mes devoirs… oups !",
           sol="⚽ oui · 🎬 oui · 🍕 oui · 📚 non · 🏊 non · 👵 oui")
    e3 = E("J'écris 3 choses que j'ai faites hier.", lines(3), ["ecris"], 2, "C", sol="Production personnelle au passé composé.")
    b.page(f'{e}{e2}{e3}', "S'entraîner")

    # ---------- Leçon 2 : négation PC + marqueurs ----------
    l2 = lecon("La négation au passé composé · raconter", '''<div class="attention">Je <b>n'</b>ai <b>pas</b> mangé. · Il <b>n'</b>a <b>pas</b> fait ses devoirs. · Nous <b>n'</b>avons <b>jamais</b> vu la mer. → <b>ne / n'</b> + avoir + <b>pas</b> + participe</div>
<p><b>Pour raconter :</b> hier · avant-hier · samedi dernier · le week-end dernier · la semaine dernière · il y a 2 jours · l'année dernière<br>+ <b>d'abord, ensuite, après, enfin</b> (module 10) · C'était super ! (= c'est au passé)</p>
<p class="sm muted">⚠️ Quelques verbes (aller, venir, partir, arriver, naître…) se conjuguent avec <b>être</b> : je suis allé(e). On les étudie au volume 2. Pour l'instant, on apprend : <b>je suis allé(e)</b>.</p>''')
    e = E("Je transforme à la forme négative.", '<p>1. J\'ai mangé. → ______________________</p><p>2. Tu as fini ? → ______________________</p><p>3. Ils ont vu le film. → ______________________</p>', ["ecris"], 2, "C", sol="Je n'ai pas mangé. · Tu n'as pas fini ? · Ils n'ont pas vu le film.")
    b.page(f'{l2}{e}', "Leçon 2")
    e = E("Je remets le récit dans l'ordre (1 à 5).", '<div class="card"><p>☐ Ensuite, nous avons visité le château. ☐ Le week-end dernier, je suis allée à Namur avec ma famille. ☐ Enfin, nous avons pris le train de 18 h. ☐ D\'abord, nous avons pris le téléphérique. ☐ Après, nous avons mangé une gaufre. C\'était super !</p></div>', ["lis", "numerote"], 2, "B",
          sol="1. Le week-end dernier… 2. D'abord… téléphérique 3. Ensuite… château 4. Après… gaufre 5. Enfin… train")
    e2 = E("Je raconte mon week-end dernier (5 phrases avec d'abord, ensuite, enfin + 1 négation).", lines(5), ["ecris"], 2, "C", sol="Production : passé composé, mots d'ordre, une négation.")
    e3 = E("Jeu « Menteur ! » : je dis 3 phrases sur mon week-end, 1 est fausse. La classe devine.", '', ["parle", "groupe", "joue"], 3, "A", sol="Écoute active ; réponses au passé composé.")
    b.page(f'{e}{e2}{e3}', "S'entraîner")

    # ---------- Leçon 3 : futur proche ----------
    l3 = lecon("Le futur proche : aller + infinitif", f'''<div class="grid2"><div class="card" style="background:#fff"><b>aller</b> au présent + <b>infinitif</b><p>je <b>vais</b> partir<br>tu <b>vas</b> partir<br>il / elle / on <b>va</b> partir<br>nous <b>allons</b> partir<br>vous <b>allez</b> partir<br>ils / elles <b>vont</b> partir</p></div>
<div class="card" style="background:#fff"><b>Quand ?</b><p>tout à l'heure · ce soir · demain · ce week-end · la semaine prochaine · l'année prochaine · pendant les vacances</p><p><b>Négation :</b> je <b>ne</b> vais <b>pas</b> partir.</p><p>Demain, je <b>vais jouer</b> au foot. ⚽</p></div></div>''')
    e = E("Je conjugue au futur proche.", '<p>1. Demain, je (jouer) ______________. 2. Ce soir, tu (regarder) ______________ un film. 3. Elle (partir) ______________ en vacances. 4. Nous (faire) ______________ une excursion. 5. Ils (prendre) ______________ le train.</p>', ["complete"], 1, "C",
          sol="vais jouer · vas regarder · va partir · allons faire · vont prendre")
    b.page(f'{l3}{e}', "Leçon 3")
    e = E("Passé composé ou futur proche ? Je complète.", '<p>1. Hier, je ______________ (manger) une pizza. 2. Demain, je ______________ (manger) un couscous.</p><p>3. La semaine dernière, nous ______________ (visiter) le musée. 4. La semaine prochaine, nous ______________ (visiter) le zoo.</p>', ["complete"], 2, "C",
          sol="j'ai mangé · je vais manger · avons visité · allons visiter")
    e2 = E("J'écoute : c'est passé ⬅️, présent 📍 ou futur ➡️ ?", checks(8, ["⬅️", "📍", "➡️"]), ["ecoute", "coche"], 2, "A",
           script="1. J'ai joué. — 2. Je joue. — 3. Je vais jouer. — 4. Nous avons fini. — 5. Elle va venir. — 6. Il mange. — 7. Vous allez voir. — 8. Ils ont pris le bus.",
           sol="1. ⬅️ — 2. 📍 — 3. ➡️ — 4. ⬅️ — 5. ➡️ — 6. 📍 — 7. ➡️ — 8. ⬅️")
    e3 = E("Mes projets pour les vacances : j'écris 4 phrases au futur proche.", lines(4), ["ecris"], 2, "C", sol="Pendant les vacances, je vais…")
    b.page(f'{e}{e2}{e3}', "S'entraîner")

    # ---------- FLESco : passé / présent / futur dans les consignes ----------
    l4 = lecon("Passé, présent, futur dans une consigne", table(["", "Je reconnais…", "Exemple de consigne", "Je fais quoi ?"], [["⬅️", "as / a + participe", "Relis ce que tu <b>as écrit</b>.", "Je vérifie mon travail (c'est déjà fait)."], ["📍", "verbe au présent / impératif", "<b>Lis</b> le texte. · Tu <b>lis</b> le texte.", "Je fais maintenant."], ["➡️", "vas / va + infinitif", "Tu <b>vas présenter</b> ton travail.", "Je fais plus tard : je me prépare."]], ["10mm", "42mm", "70mm", "60mm"]) +
               '<p class="sm mt2">À l\'école : « La semaine prochaine, vous <b>allez avoir</b> une interro. » → je dois étudier ! · « Vous <b>avez vu</b> la leçon 3 » → c\'est déjà étudié.</p>')
    e = E("Je lis la consigne. Je coche : c'est déjà fait ⬅️, maintenant 📍, plus tard ➡️ ?", table(["Consigne", "⬅️", "📍", "➡️"], [[c] + ['<span class="chk"></span>'] * 3 for c in ["Souligne les verbes.", "Vérifie les mots que tu as soulignés.", "Demain, nous allons corriger ensemble.", "Tu as lu le texte ? Réponds aux questions.", "Jeudi, vous allez rendre le dossier."]], ["124mm", "19mm", "19mm", "20mm"]), ["lis", "coche"], 2, "B",
          sol="📍 · ⬅️ (tu as souligné) + 📍 vérifie · ➡️ · ⬅️ + 📍 · ➡️")
    e2 = E("J'écris dans mon journal de classe ce que la prof annonce.", lines(2), ["ecoute", "ecris"], 2, "A", script="« Lundi prochain, vous allez avoir un test sur le passé composé. Mardi, nous allons visiter la bibliothèque communale. »", sol="Lundi : test passé composé · Mardi : visite bibliothèque communale")
    b.page(f'<span class="tag-doc">🎒 FRANÇAIS DE L\'ÉCOLE</span>{l4}{e}{e2}', "Consignes & école")

    # ---------- Documents de la vie ----------
    exc = '''<div class="doc" style="transform:none;padding:4mm;background:#fff;border:2px solid #283593"><div class="flex" style="justify-content:space-between"><b style="font-size:15pt">🏛️ EXCURSION · Bruxelles · mardi 15 juin</b><span class="xs">document fictif</span></div>
<table class="t" style="margin-top:2mm"><tr><th style="width:24mm">Heure</th><th>Programme</th></tr><tr><td>7 h 45</td><td>Rendez-vous devant l'école (soyez à l'heure !)</td></tr><tr><td>8 h 12</td><td>Train Namur → Bruxelles-Central 🚆</td></tr><tr><td>10 h 00</td><td>Visite guidée du musée des Sciences naturelles 🦖</td></tr>
<tr><td>12 h 00</td><td>Pique-nique au parc (apporter son repas et une bouteille d'eau)</td></tr><tr><td>13 h 30</td><td>Promenade : Grand-Place, Manneken-Pis</td></tr><tr><td>16 h 18</td><td>Train retour · arrivée à l'école vers 17 h 30</td></tr></table>
<p class="xs">Prix : 12 € (train + musée) · À payer avant le 1er juin · Talon-réponse à rendre signé · Tenue confortable, K-way 🌧️</p>
<div style="border-top:1.5px dashed #888;margin-top:2mm;padding-top:2mm" class="sm">✂ ············ Talon-réponse ············<br>Je soussigné(e) ____________, parent de ____________, autorise / n'autorise pas (barrer) mon enfant à participer à l'excursion. Signature : ________</div></div>'''
    e = E("Je lis le programme de l'excursion (c'est le futur !). Je réponds.", f'<p>1. Rendez-vous où et à quelle heure ? {blank("xl")}</p><p>2. On va visiter quoi ? {blank("l")} 3. Qu\'est-ce que je dois apporter ? {blank("xl")}</p><p>4. Ça coûte combien ? Avant quand ? {blank("xl")} 5. Qui signe le talon ? {blank()}</p>', ["lis", "ecris"], 2, "B",
          sol="1. devant l'école à 7 h 45 — 2. le musée des Sciences naturelles (+ Grand-Place, Manneken-Pis) — 3. mon repas, une bouteille d'eau, un K-way — 4. 12 €, avant le 1er juin — 5. un parent")
    b.page(f'<span class="tag-doc">📄 DOCUMENT DE LA VIE</span><h2>Le programme d\'une excursion</h2>{exc}<div class="mt4">{e}</div>', "Document de la vie")
    e = E("Après l'excursion : je lis le texte de Fatou (c'est le passé !). Je réponds.", '<div class="card" style="background:#FFFBEA"><p>« Mardi, nous avons fait une excursion à Bruxelles. D\'abord, nous avons pris le train à 8 h 12. Ensuite, nous avons visité le musée : j\'ai vu des squelettes de dinosaures, c\'était impressionnant ! À midi, nous avons mangé au parc. L\'après-midi, nous avons vu la Grand-Place. Mateo a acheté une gaufre. Je n\'ai pas vu le Manneken-Pis : il y avait trop de monde ! Enfin, nous avons pris le train du retour. J\'ai adoré cette journée ! »</p></div>' +
          f'<p>1. Qu\'est-ce que Fatou a vu au musée ? {blank("xl")}</p><p>2. Où est-ce qu\'ils ont mangé ? {blank()} 3. Qu\'est-ce que Mateo a acheté ? {blank()}</p><p>4. Qu\'est-ce que Fatou n\'a pas vu ? Pourquoi ? {blank("xl")}</p><p>5. Je souligne les verbes au passé composé dans le texte.</p>', ["lis", "souligne", "ecris"], 2, "B",
          sol="1. des squelettes de dinosaures — 2. au parc — 3. une gaufre — 4. le Manneken-Pis : il y avait trop de monde — 5. avons fait, avons pris, avons visité, ai vu, avons mangé, avons vu, a acheté, n'ai pas vu, avons pris, ai adoré")
    e2 = E("Défi ! Je compare le programme et le texte : qu'est-ce qui est différent ?", lines(2), ["lis", "ecris"], 3, "C", sol="Fatou n'a pas vu le Manneken-Pis (prévu au programme).")
    b.page(f'<span class="tag-doc">📄 DOCUMENT DE LA VIE</span><h2>Raconter une excursion</h2>{e}{e2}', "Document de la vie")
    e = E("Je lis les messages. C'est passé ⬅️ ou futur ➡️ ? J'écris la réponse.", "".join(f'<div class="card mb2">📱 <b>{n} :</b> « {t} »<div class="flex" style="justify-content:space-between"><span class="sm">⬅️ ☐ ➡️ ☐</span><span class="line" style="width:60%"></span></div></div>' for n, t in [("Daria", "Mon père est arrivé hier soir ! On a pleuré de joie ❤️"), ("Bilal", "Demain je vais m'inscrire au club de judo. Tu viens avec moi ?"), ("Mme Lambert", "Rappel : vendredi, nous allons faire la fête de fin d'année. Apportez un plat de votre pays !")]),
          ["lis", "coche", "ecris"], 2, "C", sol="Daria ⬅️ (Super ! Je suis contente pour toi !) · Bilal ➡️ (Oui, avec plaisir / Désolé…) · Mme Lambert ➡️ (D'accord, je vais apporter…)")
    e2 = E("J'écris une carte de vœux / de fin d'année à un camarade ou à la prof (ce que j'ai aimé + un souhait).", '<div class="card" style="height:42mm;background:#FFFBEA"></div>', ["ecris", "dessine"], 2, "C", sol="Ex. : Cette année, j'ai appris… J'ai aimé… Bonnes vacances !")
    b.page(f'<span class="tag-doc">📄 DOCUMENT DE LA VIE</span><h2>Des messages et une carte</h2>{e}{e2}', "Document de la vie")

    # ---------- Sons : révision ----------
    sons = [("[a]", "a"), ("[i]", "i, y"), ("[o]", "o, au, eau"), ("[u]", "ou"), ("[y]", "u"), ("[e]", "é, er, ez"), ("[ɛ]", "è, ê, ai"), ("[ø]", "eu"), ("[ɑ̃]", "an, en"), ("[ɛ̃]", "in, ain"), ("[ɔ̃]", "on"), ("[wa]", "oi"), ("[ʃ]", "ch"), ("[ɲ]", "gn"), ("[j]", "ill, y"), ("[k]", "c, k, qu")]
    e = E("Tous les sons de l'année. J'écoute, je répète, je donne un mot pour chaque son.", '<div class="grid4">' + "".join(f'<div class="card c" style="padding:2mm"><b class="huge" style="font-size:15pt">{s}</b><div class="xs muted">{l}</div><div class="line"></div></div>' for s, l in sons) + '</div>', ["ecoute", "repete", "ecris"], 1, "A",
          script="Dire chaque son avec un mot exemple. Ex. : [y] lune, [u] loup, [ɔ̃] bonbon. Les élèves trouvent un autre mot.", sol="Exemples : ami, lit, auto, loup, lune, été, fête, deux, enfant, pain, bonbon, roi, chat, montagne, fille, café.")
    e2 = E("Le [e] du passé et le [ɛ] du présent : j'écoute et je répète.", '<div class="grid2"><div class="card c"><p class="big">j\'ai mangé ⬅️</p><p class="sm muted">[e] fermé</p></div><div class="card c"><p class="big">il fait / c\'est 📍</p><p class="sm muted">[ɛ] ouvert</p></div></div>', ["ecoute", "repete"], 2, "A",
           script="j'ai joué — j'ai parlé — c'est — il fait — j'ai fait. Insister sur le é final des participes.", sol="Activité orale.")
    b.page(f'<h2>J\'écoute bien · Révision de tous les sons</h2>{e}{e2}', "Sons")
    e = E("🔁 Module 11 · Jouer / faire.", '<p>Je joue ___ basket et je fais ___ natation.</p>', ["complete"], 1, "C", sol="au · de la")
    e2 = E("🔁 Module 10 · Se lever.", '<p>Demain, je vais ___ lever à 6 h. (⚠️ futur proche d\'un verbe pronominal)</p>', ["complete"], 3, "C", sol="me (je vais me lever)")
    e3 = E("🔁 Modules 7 et 9 · L'excursion coûte 12 €. Je donne 20 €. On me rend : ______ · Je vais ___ musée.", '', ["ecris"], 2, "C", sol="8 € · au")
    b.page(f'<h2>🔁 Je révise les modules 9, 10 et 11</h2>{e}{e2}{e3}', "Je révise")

    # ---------- Ateliers ----------
    e = E("Le dé du temps : je lance 2 dés. Dé 1 = quand (1-2 hier ⬅️, 3-4 aujourd'hui 📍, 5-6 demain ➡️). Dé 2 = l'action. Je dis la phrase au bon temps.", '<div class="grid6">' + "".join(f'<div class="card c"><b>{i}</b><span class="emo s">{em}</span><div class="xs">{t}</div></div>' for i, (em, t) in enumerate([("⚽", "jouer au foot"), ("🍕", "manger une pizza"), ("🎬", "voir un film"), ("📚", "faire les devoirs"), ("🚆", "prendre le train"), ("📞", "téléphoner")], 1)) + '</div>', ["joue", "parle", "duo"], 2, "D",
          sol="Ex. : dé 1 = 2, dé 2 = 3 → Hier, j'ai vu un film.")
    e2 = E("Le bingo des verbes : la prof dit un verbe à l'infinitif, je trouve et je coche le participe passé.", table(None, [["mangé", "fait", "vu", "pris"], ["lu", "joué", "bu", "eu"], ["été", "écrit", "fini", "regardé"], ["dormi", "parlé", "acheté", "visité"]], ["25%"] * 4).replace("<td>", '<td style="text-align:center;height:12mm;font-weight:700">'), ["ecoute", "coche", "joue"], 1, "D",
           sol="Participes à reconnaître.")
    b.page(f'{atl_head("D", "Atelier · Jouer avec le temps")}{e}{e2}', "Atelier")
    e = E("Mon album photo : je colle ou je dessine 3 souvenirs de l'année et j'écris une phrase au passé sous chaque photo.", '<div class="grid3">' + '<div class="card" style="height:46mm"></div>' * 3 + '</div>' + lines(3), ["dessine", "colle", "ecris"], 2, "C", sol="Phrases au passé composé.")
    e2 = E("Je lis le message de Yonas et je réponds : qu'est-ce que tu vas faire pendant les vacances ?", '<div class="card">📱 <b>Yonas :</b> « Salut ! L\'école est finie ! 🎉 Moi, je vais aller au stage de foot en juillet. En août, je vais aider mon oncle au magasin. Et toi ? »</div>' + lines(3), ["lis", "ecris"], 2, "C", sol="Réponse au futur proche (3 projets).")
    b.page(f'{atl_head("C", "Atelier · Lire et écrire")}{e}{e2}', "Atelier")

    # ---------- ★ Alpha : petit texte de 5 phrases ----------
    e = E("Je lis le texte (5 phrases). Je montre les images.", '<div class="card" style="background:#FFFBEA"><p class="big" style="line-height:1.9">Hier, c\'était samedi. 🗓️<br>Sami a joué au foot. ⚽<br>Il a mangé des frites. 🍟<br>Le soir, il a vu un film. 🎬<br>Demain, il va aller à la mer. 🏖️</p></div>', ["lis", "montre"], 1, "P", alpha=True, sol="Lecture accompagnée, puis seul.")
    e2 = E("Je réponds : je colorie la bonne image.", "".join(f'<div class="card mb2 flex" style="justify-content:space-between"><p class="big" style="margin:0">{t}</p><span style="font-size:22pt">{o}</span></div>' for t, o in [("Sami a joué au…", "🎾 ⚽ 🏀"), ("Il a mangé des…", "🍟 🍎 🍰"), ("Demain, il va aller…", "🏫 🏖️ 🏥")]), ["lis", "colorie"], 1, "B", alpha=True, sol="⚽ · 🍟 · 🏖️")
    b.page(AL.format(t="Je lis un petit texte") + e + e2, "★ Alpha", color=MC)
    e = E("Hier ⬅️ ou demain ➡️ ? Je lis et je relie.", relie([f'<span class="big">{t}</span>' for t in ["J'ai mangé.", "Je vais manger.", "Il a joué.", "Il va jouer."]], ["⬅️ hier", "➡️ demain", "⬅️ hier", "➡️ demain"]), ["lis", "relie"], 1, "B", alpha=True, sol="ai mangé ⬅️ · vais manger ➡️ · a joué ⬅️ · va jouer ➡️")
    e2 = E("Je recopie : hier, j'ai joué.", trace("hier, j'ai joué", 24, 1), ["recopie", "trace"], 1, "C", alpha=True, sol="Écriture.")
    e3 = E("Dictée de 2 phrases.", guide_lines(2, 20), ["ecoute", "ecris"], 2, "P", alpha=True, script="« J'ai mangé. » — « Je vais jouer. »", sol="J'ai mangé. Je vais jouer.")
    b.page(AL.format(t="J'écris") + e + e2 + e3, "★ Alpha", color=MC)
    alp = [("Je connais les lettres de l'alphabet.", "M1"), ("Je lis les syllabes (ma, pa, lu…).", "M2-M4"), ("Je lis les sons ou, on, an, in, oi.", "M6-M7"), ("Je lis é, è, ai, eu, gn, ill.", "M8-M9"), ("Je lis des mots de la vie (bus, école, pain…).", "M1-M12"),
           ("Je lis une phrase simple.", "M11"), ("Je lis un petit texte de 5 phrases.", "M12"), ("J'écris mon nom, mon prénom, mon adresse.", "M4-M9"), ("J'écris des mots sous la dictée.", "M1-M12"), ("J'écris une petite phrase.", "M11-M12")]
    b.page(AL.format(t="Mon bilan ★ Alpha de l'année") + table(["Je sais…", "Module", "😀", "🙂", "😕"], [[a, f'<span class="sm muted">{m}</span>', '<span class="chk"></span>', '<span class="chk"></span>', '<span class="chk"></span>'] for a, m in alp], ["104mm", "24mm", "18mm", "18mm", "18mm"]) +
           '<div class="card mt4 c"><p class="big">Je suis fier / fière de moi ! ⭐</p><p class="sm">Signature de la prof : ____________</p></div>', "★ Alpha", color=MC)

    # ---------- Tâche finale : carnet de réussites + bilan A1 ----------
    e = E("Mon carnet de réussites : je choisis mes 3 plus belles réussites de l'année (un texte, une tâche finale, un test…). J'explique pourquoi.", table(["Ma réussite", "Module", "Pourquoi je suis fier / fière"], [["", "", ""] for _ in range(3)], ["70mm", "22mm", "90mm"]).replace("<td></td>", '<td style="height:18mm"></td>'), ["ecris", "seul"], 2, "C", sol="Choix personnel argumenté (parce que…).")
    e2 = E("Je raconte mon année (passé) et mes projets (futur) : 4 phrases au passé composé + 3 phrases au futur proche.", lines(7), ["ecris"], 2, "C", sol="Cette année, j'ai appris… J'ai rencontré… L'année prochaine, je vais…")
    b.page(tache_head("Mon carnet de réussites", "Je regarde mon cahier de l'année, je choisis mes réussites, je raconte mon année et mes projets, puis je présente mon carnet à la classe.") + e + e2, "Tâche finale", levels=False)
    a1 = [("🎧 Écouter", ["Je comprends les consignes de la classe.", "Je comprends quand on parle lentement de moi, de ma famille, de l'école.", "Je comprends des prix, des heures, des chiffres.", "Je comprends un chemin simple."]),
          ("📖 Lire", ["Je lis un horaire, une affiche, un menu, une publicité.", "Je lis un message court (SMS, carte).", "Je lis un formulaire simple."]),
          ("🗣️ Parler", ["Je me présente et je présente ma famille.", "Je pose des questions simples (où, quand, combien…).", "J'achète quelque chose, je demande un chemin.", "Je raconte ma journée et mon week-end."]),
          ("✏️ Écrire", ["Je remplis un formulaire (nom, adresse, date).", "J'écris un message court, une invitation.", "J'écris un petit texte sur moi (5-6 phrases)."])]
    rows = []
    for k, its in a1:
        rows.append([f'<b>{k}</b>', "", "", "", ""])
        rows += [[f'<span class="sm">{x}</span>', '<span class="chk"></span>', '<span class="chk"></span>', '<span class="chk"></span>', ""] for x in its]
    b.page('<h2>🏆 Mon bilan A1 · Je sais faire en français</h2><p class="sm muted">Le niveau A1 est le premier niveau du Cadre européen des langues. Je coche, puis la prof valide.</p>' +
           table(["", "😀 Oui", "🙂 Un peu", "😕 Pas encore", "Prof"], rows, ["104mm", "18mm", "20mm", "22mm", "18mm"]) + '<div class="card mt4 c" style="background:#E8EAF6"><p class="big">🎓 Bravo ! Volume 1 terminé. Rendez-vous au volume 2 : « En route ! »</p></div>', "Tâche finale", levels=False)
    e = E("Je révise.", '<p>1. Hier, nous ______ (prendre) le bus. 2. Demain, je ______ (partir). 3. Elle n\'a ___ mangé. 4. faire → participe : ______ 5. ______, je vais à la mer. (le jour après aujourd\'hui)</p>', ["ecris"], 2, "C",
          sol="avons pris · vais partir · pas · fait · Demain")
    e2 = E("Défi ! Je corrige les 4 erreurs.", '<div class="card big">Hier, je vais jouer au foot. J\'ai prendu le bus. Demain, nous avons visité le zoo. Il a pas mangé.</div>' + lines(1), ["barre", "ecris"], 3, "C",
           sol="Hier, j'ai joué · J'ai pris · Demain, nous allons visiter · Il n'a pas mangé")
    b.page(f'<h2>🔁 Je révise tout le module</h2>{e}{e2}', "Je révise")

    # ---------- Test ----------
    Q = [("Aujourd'hui, c'est mardi. Hier, c'était…", ["mercredi", "lundi", "jeudi", "dimanche"]), ("Le jour après aujourd'hui :", ["hier", "demain", "avant-hier", "maintenant"]),
         ("Passé composé : j'____ mangé.", ["ai", "as", "a", "suis"]), ("Nous ____ joué.", ["avons", "avez", "ont", "allons"]), ("Ils ____ regardé un film.", ["a", "ont", "avons", "vont"]),
         ("faire → participe passé :", ["faisé", "fait", "fais", "faire"]), ("prendre → participe passé :", ["prendu", "prit", "pris", "prené"]), ("voir → participe passé :", ["voi", "vu", "voyé", "vit"]),
         ("Négation : J'ai mangé. →", ["Je n'ai pas mangé.", "Je ai pas mangé.", "Je n'ai mangé pas.", "Je pas ai mangé."]), ("Futur proche : je ____ partir.", ["vais", "ai", "suis", "va"]),
         ("Elles ____ visiter le musée.", ["vont", "va", "allons", "ont"]), ("Demain, nous ____ au zoo.", ["avons allé", "allons aller", "avons été", "allé"]),
         ("Hier, je ____ au foot.", ["vais jouer", "ai joué", "joue", "va jouer"]), ("« La semaine prochaine » =", ["le passé", "le présent", "le futur", "aujourd'hui"]),
         ("« Tu vas présenter ton travail. » Je le fais…", ["maintenant", "plus tard", "c'est déjà fait", "jamais"]), ("« Relis ce que tu as écrit. » L'écriture est…", ["à faire plus tard", "déjà faite", "interdite", "au futur"]),
         ("Sur le talon-réponse, qui signe ?", ["le chauffeur", "un parent", "le musée", "le directeur du train"]), ("Dans « j'ai mangé », on entend :", ["[e]", "[ɛ]", "[a] à la fin", "[ø]"]),
         ("🔁 Je fais ____ natation.", ["du", "de la", "au", "à la"]), ("🔁 Je ____ couche à 22 h.", ["me", "te", "se", "nous"])]
    ans = ["lundi", "demain", "ai", "avons", "ont", "fait", "pris", "vu", "Je n'ai pas mangé.", "vais", "vont", "allons aller", "ai joué", "le futur", "plus tard", "déjà faite", "un parent", "[e]", "de la", "me"]
    key = key_from(Q, ans)
    test_pages(b, 12, "Hier et demain", Q, f'<h3>B1. J\'écris 3 phrases sur mon week-end dernier (passé composé). (… / 4)</h3>{lines(2, True)}<h3>B2. J\'écris 2 phrases sur mes vacances (futur proche). (… / 3)</h3>{lines(1, True)}<h3>B3. Je mets à la forme négative : « Il a fini. » / « Je vais partir. » (… / 3)</h3>{lines(1, True)}',
               [["raconter mon week-end", "/ 4", ""], ["dire mes projets", "/ 3", ""], ["répondre : « Qu'est-ce que tu as appris cette année ? »", "/ 3", ""]],
               f'<h3>1. Je lis le texte. (… / 4)</h3><div class="card big" style="line-height:1.7">Hier, Lina a mangé une pomme. Elle a joué au parc. Demain, elle va aller à l\'école.</div><h3>2. Je réponds : j\'entoure. (… / 4)</h3><div class="card big">Lina a mangé… 🍎 🍌 · Elle a joué… 🏫 🌳 · Demain, elle va… 🏫 🏖️</div><h3>3. Hier ⬅️ ou demain ➡️ ? (… / 4)</h3><div class="card big">J\'ai joué. ⬅️ ➡️ · Je vais manger. ⬅️ ➡️</div><h3>4. Dictée : 1 phrase. (… / 4)</h3>{guide_lines(1, 22)}<h3>5. Je dis ce que j\'ai fait hier (oral). (… / 4)</h3><div class="card">☐ je comprends ☐ je réponds ☐ « j\'ai… » ☐ phrase complète</div>')
    closing(b, 12, ["Je sais dire hier, aujourd'hui, demain…", "Je sais conjuguer au passé composé avec avoir.", "Je connais les participes fait, pris, vu, lu, bu, eu, été.", "Je sais dire je n'ai pas…", "Je sais conjuguer au futur proche.",
                    "Je sais raconter un week-end, une excursion.", "Je sais parler de mes projets.", "Je reconnais passé, présent, futur dans une consigne.", "Je sais lire un programme et un talon-réponse.", "Je connais tous les sons de l'année.", "★ Je sais lire un petit texte de 5 phrases."],
            [("⬅️", "hier"), ("📍", "aujourd'hui"), ("➡️", "demain"), ("🗓️", "le week-end dernier"), ("🗓️", "la semaine prochaine"), ("🍽️", "j'ai mangé"), ("⚽", "j'ai joué"), ("🎬", "j'ai vu"), ("📖", "j'ai lu"), ("🛠️", "j'ai fait"), ("🚌", "j'ai pris"),
             ("🚀", "je vais partir"), ("🏛️", "le musée"), ("🚆", "l'excursion"), ("📝", "le talon-réponse"), ("🏖️", "les vacances"), ("🎯", "le projet"), ("🏆", "la réussite"), ("📸", "le souvenir"), ("🎓", "le bilan")])
    plan_de_travail(b, E, 12, ["Le passé composé avec avoir", "La négation au passé · raconter", "Le futur proche", "Passé, présent, futur dans les consignes"], "☐ Mon carnet de réussites<br>☐ Mon bilan A1")
    if render:
        to_pdf(b.html(), '/home/claude/syllabus/out/V1_M12_eleve.pdf')

    pg, exs = helpers(b, E)
    A = b.marks["★ Alpha"]
    days = [("1", "Collectif", f"Ouverture · BD ({pg('Découvrir')}) · mots du temps", f"Alpha : petit texte (p. {A[0]})"), ("2", "Collectif", f"Activités du week-end ({pg('Lexique')})", f"Alpha : hier / demain (p. {A[1]})"),
            ("3", "Rotation", f"📌 Leçon 1 passé composé ({pg('Leçon 1')})", "Alpha : relire le texte, dictée"), ("4", "Rotation", f"📌 Leçon 2 négation, raconter ({pg('Leçon 2')})", "Alpha : album photo + 1 mot"),
            ("5", "Collectif", f"📌 Leçon 3 futur proche ({pg('Leçon 3')})", "Alpha : je vais…"), ("6", "Rotation", f"Consignes et temps ({pg('Consignes & école')}) · sons", "Alpha : révision des sons"),
            ("7", "Collectif", f"Excursion, texte de Fatou, messages ({pg('Document de la vie')})", "Alpha : messages lus par la prof"), ("8", "Ateliers", f"Dé du temps, bingo, album ({pg('Atelier')})", f"Alpha : bilan de l'année (p. {A[2]})"),
            ("9", "Seul", f"Carnet de réussites + bilan A1 ({pg('Tâche finale')})", "Alpha : carnet (dessins + phrases)"), ("10", "Seul", f"Test ({pg('Test')}) · fête de fin d'année", f"Alpha : test ({pg('★ Alpha · Test')})")]
    rot = [["🎧 Écouter-Parler", "Menteur ! · mon week-end", "20 min", "—"], ["📖 Lire", "Texte de Fatou · messages", "20 min", "Oui"], ["✏️ Écrire", "Passé composé / futur proche · album", "20 min", "● oui"],
           ["🧩 Jouer", "Dé du temps · bingo des participes", "20 min", "Entre joueurs"], ["👩‍🏫 Table d'appui", "Alpha : petit texte · autres : participes irréguliers", "20 min", "—"]]
    ev1 = '''<h3>Partie B (10 points)</h3><p class="sm"><b>B1</b> : auxiliaire juste (2) + participes justes (2) · <b>B2</b> : aller conjugué + infinitif (3) · <b>B3</b> : <span class="sol">Il n'a pas fini. · Je ne vais pas partir.</span> (1,5 + 1,5).</p>
<h3>Test ★ Alpha</h3><p class="sm"><b>Ex. 2 :</b> <span class="sol">🍎 · 🌳 · 🏫</span> · <b>Ex. 3 :</b> <span class="sol">J'ai joué ⬅️ · Je vais manger ➡️</span> · <b>Ex. 4, dicter :</b> <span class="sol">Hier, j'ai mangé.</span></p>'''
    ev2 = f'''<h2>Grille · tâche finale « Mon carnet de réussites »</h2>{table(["Critère", "Très bien", "Bien", "À retravailler", "Points"], [["<b>Réussites</b> choisies et justifiées (parce que)", "3 justifiées", "2", "0-1", "/ 4"], ["<b>Passé composé</b> (4 phrases)", "Juste", "1-2 erreurs", "Beaucoup", "/ 6"], ["<b>Futur proche</b> (3 phrases)", "Juste", "1 erreur", "Beaucoup", "/ 4"], ["<b>Présentation orale</b> du carnet", "Fluide", "Hésitante", "Bloquée", "/ 6"]], ["64mm", "32mm", "32mm", "32mm", "22mm"])}
<h2 class="mt4">Différencier et remédier</h2>{table(["Difficulté", "Remédiation"], [["Auxiliaire avoir oublié", "Formule visuelle « ai / as / a + é » ; cartes avoir à poser devant le participe."], ["Participes irréguliers", "Bingo, mémory infinitif / participe ; affiche des 8 irréguliers."], ["Passé / futur confondus", "Frise au sol : l'élève se déplace à gauche (passé) / à droite (futur) en disant la phrase."], ["Verbes avec être", "Accepter « je suis allé(e) » comme expression figée ; reprise au volume 2."], ["Élève rapide", "Raconter un souvenir de son pays (8 phrases) ; écrire le programme d'une excursion idéale."]], ["50mm", "132mm"])}
<div class="astuce mt4"><b>Fin d'année et transition :</b> le bilan A1 sert de document de passage (conseil de classe, orientation, sortie du DASPA). Le garder dans le dossier de l'élève. Prudence avec les récits du passé : laisser choisir des souvenirs heureux ou de l'année scolaire, sans demander le parcours migratoire.</div>'''
    T = teacher_book(b, E, "V1 · M12", "", MC, 12, "Hier et demain",
                     "<li><b>Communication :</b> raconter un événement passé, parler de ses projets, faire le bilan.</li><li><b>Lexique :</b> marqueurs de temps, activités du week-end et des vacances, excursion.</li><li><b>Grammaire :</b> passé composé avec avoir (participes réguliers et irréguliers fréquents) ; négation ; futur proche.</li><li><b>Phonétique :</b> révision de tous les sons ; [e] du participe.</li><li><b>FLSco :</b> reconnaître passé / présent / futur dans une consigne.</li><li><b>Documents :</b> programme d'excursion, talon-réponse, récit, messages.</li><li><b>★ Alpha :</b> lire un petit texte de 5 phrases ; bilan Alpha.</li>",
                     '<p class="sm"><b style="color:#E4572E">Indispensable</b> : hier / demain, j\'ai + participe en -é, je vais + infinitif.</p><p class="sm"><b style="color:#d9a400">Important</b> : participes irréguliers, négation, raconter avec des mots d\'ordre.</p><p class="sm"><b style="color:#2BA88F">Enrichissement</b> : je suis allé(e), récit de 8 phrases.</p>',
                     "Dés · photos de l'année (avec accord) · frise au sol (ruban adhésif) · cahiers des élèves pour le carnet de réussites.", "<b>Fin d'année :</b> organiser une exposition des carnets de réussites ou une fête où chaque élève présente une réussite (parents invités).",
                     days, "« Qu'est-ce que tu as fait hier ? » en chaîne · un participe du jour · la date d'hier / de demain.", rot, key, (ev1, ev2), start=tstart)
    if render:
        to_pdf(T.html(), '/home/claude/syllabus/out/V1_M12_prof.pdf')
    return b, T


if __name__ == "__main__":
    b, T = build_m12()
    print(b.n, T.n)
