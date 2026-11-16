"""Volume 1 · Module 11 « Loisirs et sport »."""
import sys
sys.path.insert(0, '/home/claude/syllabus')
from lib.base import *
from lib.art import *
from lib.alpha import AL, letter_page, syll_table
from lib.module import *
from lib.render import to_pdf

MC = "#00897B"
SPORTS = [("⚽", "le football"), ("🏀", "le basket"), ("🏐", "le volley"), ("🎾", "le tennis"), ("🏓", "le ping-pong"), ("🥊", "la boxe"), ("🥋", "le judo"), ("🏊", "la natation"),
          ("🚴", "le vélo"), ("🏃", "la course"), ("💃", "la danse"), ("🤸", "la gymnastique"), ("🛹", "le skate"), ("🧗", "l'escalade"), ("🏏", "le cricket"), ("♟️", "les échecs")]
LOISIRS = [("🎮", "les jeux vidéo"), ("🎸", "la guitare"), ("🎹", "le piano"), ("🎤", "chanter"), ("🎨", "dessiner"), ("📖", "lire"), ("🎬", "le cinéma"), ("📺", "les séries"),
           ("🧶", "le tricot"), ("🍳", "cuisiner"), ("📷", "la photo"), ("🌳", "se promener")]


def build_m11(start=1, tstart=1, render=True):
    b = Book("V1 · M11", "Volume 1 · Premiers pas · Module 11 · Loisirs et sport", MC, start=start)
    E = Ex(b)
    vis = '<div class="c" style="font-size:40pt;line-height:1.3">⚽🏀🥊🏊💃🎸<br>🎮🎨📖🎬📷♟️</div>'
    opening(b, MC, 11, "Loisirs et sport", vis, [("⚽", "parler de mes loisirs et de mes sports"), ("🎯", "dire jouer au… / faire du…"), ("❓", "poser des questions : est-ce que, quand, où…"),
            ("💌", "inviter, accepter, refuser poliment"), ("📝", "remplir un formulaire d'inscription"), ("📣", "lire une affiche d'activités")],
            ["Qu'est-ce que tu fais le mercredi après-midi ?", "Quel sport on aime dans ton pays ?", "Tu connais une maison de jeunes ou un club près de chez toi ?"],
            ["le loisir", "le sport", "jouer au", "faire du", "on", "est-ce que", "inviter", "avec plaisir", "désolé", "le formulaire"], "#E0F2F1")

    # ---------- Découvrir ----------
    bd = '<div class="grid2" style="gap:3mm">' + "".join([
        bd_case(1, lr("mateo", ["Fatou, qu'est-ce que tu fais mercredi après-midi ?"], "fatou", ["Rien de spécial. Pourquoi ?"], "sourire", "pense")),
        bd_case(2, lr("mateo", ["Il y a un tournoi de foot à la maison de jeunes. Tu veux venir ?"], extra='<div class="c" style="font-size:26pt">⚽🏆</div>')),
        bd_case(3, lr("fatou", ["Le foot ? Bof… Je ne joue pas au foot. Moi, je fais de la danse !"], "mateo", ["Il y a aussi un atelier de danse hip-hop à 15 h !"], "neutre", "rire")),
        bd_case(4, lr("fatou", ["Super ! Avec plaisir ! On y va comment ?"], "mateo", ["On prend le bus 7 ensemble. Rendez-vous à 13 h 30 à l'arrêt."], "rire", "sourire")),
        bd_case(5, lr("yonas", ["Et moi ? Je peux venir aussi ?"], "mateo", ["Bien sûr ! Tu joues dans mon équipe !"], "pense", "rire")),
        bd_case(6, lr("daria", ["Désolée, je ne peux pas : j'ai cours de piano. Mais samedi, on va au cinéma ?"], "fatou", ["D'accord ! Bonne idée !"], "triste", "rire")),
    ]) + '</div>'
    e = E("J'écoute et je regarde la BD : une invitation.", bd, ["ecoute", "regarde"], 1, "A",
          script="Lire deux fois. Mettre en scène : un élève invite, l'autre accepte 👍 ou refuse 👎. Faire répéter : « Tu veux venir ? », « Avec plaisir ! », « Désolé, je ne peux pas. »", sol="Activité orale.")
    b.page(f'<h2>Découvrir · Tu veux venir ?</h2>{e}', "Découvrir")
    e = E("Je réponds.", f'<p>1. Qu\'est-ce qu\'il y a mercredi à la maison de jeunes ? {blank("xl")}</p><p>2. Fatou fait quel sport ? {blank()}</p><p>3. Rendez-vous où ? À quelle heure ? {blank("xl")}</p><p>4. Pourquoi Daria ne peut pas venir ? {blank("xl")}</p><p>5. Qu\'est-ce que Daria propose ? {blank("l")}</p>',
          ["lis", "ecris"], 1, "B", sol="1. un tournoi de foot (et un atelier de danse hip-hop) — 2. la danse — 3. à l'arrêt du bus 7, à 13 h 30 — 4. Elle a cours de piano. — 5. aller au cinéma samedi")
    e2 = E("Qui accepte 👍 ? Qui refuse 👎 ?", table(["", "👍 accepte", "👎 refuse"], [[n, '<span class="chk"></span>', '<span class="chk"></span>'] for n in ["Fatou (danse)", "Yonas", "Daria"]], ["80mm", "50mm", "52mm"]), ["lis", "coche"], 1, "B", sol="Fatou 👍 · Yonas 👍 · Daria 👎 (mais elle propose autre chose)")
    e3 = E("Défi ! J'invite mon voisin à une activité. Il accepte ou il refuse avec une raison.", lines(2), ["parle", "duo"], 3, "A", sol="Tu veux… ? — Avec plaisir ! / Désolé, je ne peux pas, je dois…")
    b.page(f'{e}{e2}{e3}<div class="astuce">🇧🇪 En Belgique, une <b>maison de jeunes</b> (MJ) propose des activités gratuites ou pas chères pour les 12-26 ans. En Belgique francophone, le <b>mercredi après-midi</b>, il n\'y a pas cours : c\'est le moment des clubs et des activités !</div>', "Découvrir")

    # ---------- Lexique ----------
    e = E("Les sports. J'écoute et je répète.", emogrid(SPORTS, 6), ["ecoute", "repete"], 1, "A", script="Dire chaque sport et mimer. Demander : « Quel sport tu aimes ? Quel sport on fait dans ton pays ? » (cricket, lutte, capoeira…)", sol="Activité orale.")
    e2 = E("Les loisirs. J'écoute et je répète.", emogrid(LOISIRS, 6), ["ecoute", "repete"], 1, "A", script="Dire chaque loisir. Jeu du mime en équipe.", sol="Activité orale.")
    b.page(f'<h2>Les sports et les loisirs</h2>{e}{e2}', "Lexique")
    e = E("Je classe les sports.", table(["⚽ avec un ballon", "💧 dans l'eau", "🥊 sport de combat", "🎶 avec de la musique"], [["", "", "", ""]], ["45mm"] * 4).replace("<td></td>", '<td style="height:30mm"></td>') +
          '<p class="sm mt2">le football · la natation · la boxe · la danse · le basket · le judo · le volley · le water-polo · la gymnastique rythmique · le karaté</p>', ["ecris"], 1, "C",
          sol="Ballon : football, basket, volley (water-polo) · Eau : natation, water-polo · Combat : boxe, judo, karaté · Musique : danse, gymnastique rythmique")
    e2 = E("Où est-ce que je pratique ? Je relie.", relie(["la natation", "le football", "le basket", "l'escalade", "la danse", "le cinéma"], ["au terrain / au stade", "à la salle de danse", "à la piscine", "dans une salle de sport", "sur un mur d'escalade", "dans une salle de cinéma"]),
           ["relie"], 1, "B", sol="natation → piscine · football → terrain · basket → salle de sport · escalade → mur · danse → salle de danse · cinéma → salle de cinéma")
    b.page(f'{e}{e2}', "Lexique")

    # ---------- Leçon 1 : jouer au / faire du ----------
    l1 = lecon("Jouer au… · faire du… · le verbe faire", f'''<div class="grid3"><div class="card" style="background:#fff"><b>FAIRE</b> ⚠️<p>je fais<br>tu fais<br>il / elle / on fait<br>nous faisons<br>vous faites<br>ils / elles font</p></div>
<div class="card" style="background:#fff"><b>JOUER À</b> (un jeu, un sport avec ballon)<p>jouer <b>au</b> foot, <b>au</b> tennis<br>jouer <b>à la</b> pétanque<br>jouer <b>aux</b> cartes, <b>aux</b> échecs<br>jouer <b>de la</b> guitare, <b>du</b> piano 🎸 (instrument → de)</p></div>
<div class="card" style="background:#fff"><b>FAIRE DE</b> (une activité)<p>faire <b>du</b> vélo, <b>du</b> judo<br>faire <b>de la</b> danse, <b>de la</b> natation<br>faire <b>de l'</b>escalade<br>Négation : je ne fais <b>pas de</b> sport.</p></div></div>''')
    e = E("Je conjugue faire.", '<p>1. Je ______ du vélo. 2. Tu ______ de la boxe ? 3. Il ______ du judo. 4. Nous ______ de la natation. 5. Vous ______ du sport ? 6. Elles ______ de la danse.</p>', ["complete"], 1, "C",
          sol="fais · fais · fait · faisons · faites · font")
    b.page(f'{l1}{e}', "Leçon 1")
    e = E("Je complète avec au, à la, aux, du, de la, de l'.", '<p>1. Je joue ___ basket. 2. Elle fait ___ gymnastique. 3. Nous jouons ___ cartes. 4. Tu fais ___ escalade ? 5. Il joue ___ piano. 6. Ils font ___ skate. 7. On joue ___ échecs. 8. Je joue ___ guitare.</p>', ["complete"], 2, "C",
          sol="au · de la · aux · de l' · du · du · aux · de la")
    e2 = E("J'écoute : qui fait quoi ? Je relie.", relie(["Bilal", "Amina", "Yonas", "Daria", "Mateo"], ["🥋 du judo", "🎹 du piano", "🏃 de la course", "⚽ au foot", "📖 lire"]), ["ecoute", "relie"], 2, "A",
           script="Bilal fait du judo le samedi. Amina adore lire : elle va à la bibliothèque. Yonas fait de la course : il court très vite ! Daria joue du piano depuis 6 ans. Et Mateo joue au foot tous les mercredis.",
           sol="Bilal → judo · Amina → lire · Yonas → course · Daria → piano · Mateo → foot")
    e3 = E("Je transforme à la forme négative.", '<p>1. Je fais du sport. → ______________________</p><p>2. Il joue au tennis. → ______________________</p>', ["ecris"], 2, "C", sol="Je ne fais pas de sport. · Il ne joue pas au tennis. (jouer à : pas de changement !)")
    b.page(f'{e}{e2}{e3}', "S'entraîner")

    # ---------- Leçon 2 : aimer + infinitif, on ----------
    l2 = lecon("Aimer + verbe · le pronom « on »", '''<div class="grid2"><div class="card" style="background:#fff"><b>J'aime / j'adore / je préfère / je déteste + verbe à l'infinitif</b><p>J'aime <b>nager</b>. · J'adore <b>danser</b>. · Je déteste <b>courir</b>. · Je préfère <b>jouer</b> aux jeux vidéo.</p><p>Je <b>n'</b>aime <b>pas</b> chanter.</p></div>
<div class="card" style="background:#fff"><b>ON</b> = nous (à l'oral, très souvent !)<p><b>On</b> va au cinéma ? = <b>Nous allons</b> au cinéma ?</p><p>Le verbe avec <b>on</b> = comme <b>il / elle</b> : on joue, on fait, on va, on prend.</p></div></div>
<p class="mt2"><b>Pour dire pourquoi :</b> J'aime le foot <b>parce que</b> c'est amusant / je joue avec mes amis. — C'est super, génial, cool, nul, difficile, fatigant.</p>''')
    e = E("Je complète avec un verbe à l'infinitif.", '<p>1. J\'adore ______ (🏊). 2. Il aime ______ (🎨). 3. Nous préférons ______ (🍳). 4. Elle déteste ______ (🏃).</p>', ["complete"], 1, "C", sol="nager · dessiner · cuisiner · courir")
    b.page(f'{l2}{e}', "Leçon 2")
    e = E("Je transforme avec « on ».", '<p>1. Nous jouons au basket. → On ______________</p><p>2. Nous allons à la piscine. → On ______________</p><p>3. Nous faisons du vélo. → On ______________</p>', ["ecris"], 2, "C", sol="On joue au basket. · On va à la piscine. · On fait du vélo.")
    e2 = E("Sondage : « Qu'est-ce que tu aimes faire ? Pourquoi ? » Je pose la question à 4 camarades.", table(["Prénom", "Il / elle aime…", "parce que…"], [["", "", ""] for _ in range(4)], ["40mm", "70mm", "72mm"]).replace("<td></td>", '<td style="height:9mm"></td>'), ["parle", "ecris", "groupe"], 1, "A",
           sol="Ex. : Fatou aime danser parce que c'est amusant.")
    e3 = E("Défi ! J'écris mon portrait « loisirs » : j'adore…, j'aime…, je n'aime pas…, je déteste…, parce que…", lines(3), ["ecris"], 3, "C", sol="Production libre avec infinitifs et parce que.")
    b.page(f'{e}{e2}{e3}', "S'entraîner")

    # ---------- Leçon 3 : poser des questions ----------
    qw = [("Est-ce que…?", "Est-ce que tu fais du sport ?", "oui / non"), ("Qu'est-ce que…?", "Qu'est-ce que tu fais mercredi ?", "une chose"), ("Où…?", "Où est le club ?", "un lieu"), ("Quand…?", "Quand est le match ?", "un jour"),
          ("À quelle heure…?", "À quelle heure commence le film ?", "une heure"), ("Avec qui…?", "Avec qui tu vas au cinéma ?", "une personne"), ("Combien…?", "Combien coûte l'inscription ?", "un nombre"), ("Pourquoi…?", "Pourquoi tu aimes la danse ?", "parce que…")]
    l3 = lecon("Poser une question", table(["Le mot", "Exemple", "La réponse"], [[f'<b>{a}</b>', b2, f'<span class="sm muted">{c}</span>'] for a, b2, c in qw], ["36mm", "100mm", "46mm"]) +
               '<p class="mt2">3 façons de poser une question oui / non : <b>Tu fais du sport ?</b> ↗️ (la voix monte) · <b>Est-ce que</b> tu fais du sport ? · (écrit soutenu) <b>Fais-tu</b> du sport ?</p>')
    e = E("Je trouve la question.", '<p>1. — ______________________ ? — Je fais du judo.</p><p>2. — ______________________ ? — Le match est samedi.</p><p>3. — ______________________ ? — À la piscine communale.</p><p>4. — ______________________ ? — Avec ma sœur.</p>', ["ecris"], 2, "C",
          sol="Qu'est-ce que tu fais (comme sport) ? · Quand est le match ? · Où (est-ce que tu nages) ? · Avec qui (tu vas…) ?")
    b.page(f'{l3}{e}', "Leçon 3")
    e = E("J'écoute : c'est une question ↗️ ou une affirmation ↘️ ?", checks(8, ["↗️ question", "↘️ affirmation"]), ["ecoute", "coche"], 1, "A",
          script="1. Tu viens ? — 2. Tu viens. — 3. Il fait du sport ? — 4. On va au cinéma. — 5. C'est loin ? — 6. Elle aime danser. — 7. Vous jouez au foot ? — 8. On y va.",
          sol="1. ↗️ — 2. ↘️ — 3. ↗️ — 4. ↘️ — 5. ↗️ — 6. ↘️ — 7. ↗️ — 8. ↘️")
    e2 = E("Je relie la question et la réponse.", relie(["Combien coûte le cours ?", "À quelle heure commence le match ?", "Pourquoi tu fais de la boxe ?", "Est-ce que tu viens ?", "Où est la salle ?"], ["Parce que j'aime me défendre.", "Oui, avec plaisir !", "À côté de la piscine.", "15 euros par mois.", "À 14 h."]), ["lis", "relie"], 1, "B",
           sol="Combien → 15 euros · À quelle heure → 14 h · Pourquoi → parce que · Est-ce que → Oui · Où → à côté de la piscine")
    e3 = E("Interview d'un champion ! Je prépare 5 questions pour un sportif (ou un camarade), puis je joue l'interview.", lines(5), ["ecris", "parle", "duo"], 3, "A", sol="Questions variées avec 5 mots interrogatifs différents.")
    b.page(f'{e}{e2}{e3}', "S'entraîner")

    # ---------- Leçon 4 : inviter, accepter, refuser ----------
    l4 = lecon("Inviter · accepter · refuser", f'''<div class="grid3"><div class="card" style="background:#fff"><b>💌 Inviter</b><p>Tu veux venir… ?<br>Ça te dit de… ?<br>On va… ?<br>Je t'invite à…</p></div>
<div class="card" style="background:#E8F5E9"><b>👍 Accepter</b><p>Oui, avec plaisir !<br>D'accord !<br>Bonne idée !<br>Super, merci !</p></div>
<div class="card" style="background:#FDECEA"><b>👎 Refuser (poli)</b><p>Désolé(e), je ne peux pas.<br>Merci, mais…<br>Je dois + verbe : je <b>dois</b> aider ma mère.<br>Une autre fois ?</p></div></div>
<p class="mt2"><b>DEVOIR</b> : je dois · tu dois · il / elle / on doit · nous devons · vous devez · ils doivent (+ infinitif) — Je dois <b>étudier</b>.</p>''')
    e = E("J'accepte ou je refuse ? J'écris la réponse.", '<p>1. Tu veux jouer au basket ? (👍) → ______________________</p><p>2. Ça te dit d\'aller au cinéma ce soir ? (👎 étudier) → ______________________</p><p>3. On fait du vélo samedi ? (👎 aller chez ma tante) → ______________________</p>', ["ecris"], 2, "C",
          sol="Oui, avec plaisir ! · Désolé(e), je ne peux pas, je dois étudier. · Merci, mais je dois aller chez ma tante. Une autre fois ?")
    b.page(f'{l4}{e}', "Leçon 4")
    e = E("Je conjugue devoir.", '<p>1. Je ______ faire mes devoirs. 2. Nous ______ partir. 3. Ils ______ aider leur père. 4. Tu ______ venir à 14 h.</p>', ["complete"], 2, "C", sol="dois · devons · doivent · dois")
    e2 = E("Jeu de rôle au téléphone : j'invite, mon camarade accepte ou refuse. On fixe le jour, l'heure et le lieu.", '<div class="card"><p>📞 — Allô, c\'est… ! Tu veux… ? — … — On se retrouve où ? À quelle heure ? — … — Super, à samedi !</p></div>', ["parle", "duo"], 2, "A", sol="Fixer le rendez-vous : où, quand, à quelle heure.")
    e3 = E("Je lis l'invitation. J'écris une réponse (j'accepte ou je refuse avec une raison).", '<div class="card" style="background:#FFF8E1">🎉 <b>Fête d\'anniversaire de Bilal !</b><br>Samedi 12 décembre, de 14 h à 18 h · Salle de la maison de jeunes · Jeux, musique et gâteaux 🎂<br>Réponds avant le 8 décembre au 0470 00 00 00 (SMS). Viens avec ton maillot : on va aussi à la piscine !</div>' + lines(3), ["lis", "ecris"], 2, "C",
           sol="Ex. : Salut Bilal ! Merci pour l'invitation. Avec plaisir, je viens ! / Désolé, je ne peux pas, je dois… Bon anniversaire !")
    b.page(f'{e}{e2}{e3}', "S'entraîner")

    # ---------- FLESco : remplir un formulaire ----------
    l5 = lecon("Remplir un formulaire (méthode)", '<p>1️⃣ Je lis <b>toutes</b> les cases avant d\'écrire. 2️⃣ J\'écris le <b>NOM</b> de famille en MAJUSCULES, le <b>prénom</b> en minuscules avec une majuscule. 3️⃣ La date : <b>jj / mm / aaaa</b> (12/03/2011). 4️⃣ Je <b>coche</b> ☑ ou j\'<b>entoure</b> ce qui est vrai. 5️⃣ « Barrer la mention inutile » = je barre ce qui est faux. 6️⃣ Je relis, je <b>date</b> et je <b>signe</b>.</p><p class="sm">À l\'école : inscription à une excursion, talon-réponse, fiche santé, formulaire d\'examen, inscription au CPMS…</p>')
    e = E("Je lis et je relie le mot du formulaire et le sens.", relie(["NOM", "Prénom", "Date de naissance", "Domicile", "Nationalité", "Signature"], ["le jour où je suis né(e)", "mon nom de famille", "le pays de mon passeport", "mon adresse", "je signe avec mon stylo", "mon premier nom (Fatou, Yonas…)"]), ["lis", "relie"], 1, "B",
          sol="NOM → nom de famille · Prénom → premier nom · Date de naissance → le jour où je suis né · Domicile → adresse · Nationalité → pays du passeport · Signature → je signe")
    e2 = E("J'écris la date en chiffres (jj/mm/aaaa).", '<p>le 5 mars 2011 → ___/___/______ · le 23 novembre 2010 → ___/___/______ · le 1er janvier 2012 → ___/___/______</p>', ["ecris"], 2, "C", sol="05/03/2011 · 23/11/2010 · 01/01/2012")
    b.page(f'<span class="tag-doc">🎒 FRANÇAIS DE L\'ÉCOLE</span>{l5}{e}{e2}', "Consignes & école")

    # ---------- Documents de la vie ----------
    aff = '''<div class="doc" style="transform:none;padding:4mm;background:linear-gradient(135deg,#00897B,#26A69A);color:#fff;border-radius:3mm"><div class="c" style="font-size:22pt;font-weight:800">MAISON DE JEUNES « LE TREMPLIN »</div><div class="c">Activités du mercredi et du samedi · 12-18 ans · structure fictive</div>
<div class="grid3 mt2" style="color:#1F2A44">''' + "".join(f'<div class="card" style="background:#fff"><div class="c" style="font-size:24pt">{e}</div><b>{t}</b><div class="xs">{d}</div></div>' for e, t, d in [
        ("💃", "Danse hip-hop", "mercredi 15 h-17 h · 20 € / trimestre"), ("⚽", "Mini-foot", "mercredi 14 h-16 h · gratuit"), ("🎧", "Atelier DJ & rap", "samedi 10 h-12 h · 15 € / trimestre"),
        ("📚", "École des devoirs", "lundi, mardi, jeudi 16 h-17 h 30 · gratuit"), ("🎮", "Tournoi e-sport", "samedi 19 décembre 14 h · inscription obligatoire"), ("🏕️", "Stage de Carnaval", "du 15 au 19 février · 60 € (repas compris)")]) + '''</div>
<div class="c mt2" style="font-size:10pt">📍 Rue des Écoles 4, 5000 Namur · 📞 081 00 00 00 · Inscriptions : sur place, le mercredi de 13 h à 14 h · Réduction pour les familles nombreuses</div></div>'''
    e = E("Je lis l'affiche. Je réponds.", f'<p>1. La maison de jeunes est pour quel âge ? {blank()} 2. Quelles activités sont gratuites ? {blank("xl")}</p><p>3. La danse, c\'est quel jour ? À quelle heure ? Combien ? {blank("xl")}</p><p>4. Comment s\'inscrire ? {blank("xl")} 5. Le stage de Carnaval coûte combien ? {blank()}</p>',
          ["lis", "ecris"], 2, "B", sol="1. de 12 à 18 ans — 2. le mini-foot et l'école des devoirs — 3. le mercredi, de 15 h à 17 h, 20 € par trimestre — 4. sur place, le mercredi de 13 h à 14 h — 5. 60 € (repas compris)")
    b.page(f'<span class="tag-doc">📄 DOCUMENT DE LA VIE</span><h2>L\'affiche de la maison de jeunes</h2>{aff}<div class="mt4">{e}</div><div class="astuce">L\'<b>école des devoirs</b> aide les élèves à faire leurs devoirs après l\'école. C\'est souvent gratuit !</div>', "Document de la vie")
    frm = '<div class="doc" style="transform:none;padding:4mm;background:#fff;border:2px solid #1F2A44"><div class="flex" style="justify-content:space-between"><b style="font-size:14pt">FORMULAIRE D\'INSCRIPTION · Club de basket « Les Aigles »</b><span class="xs">saison 2026-2027 · club fictif</span></div>' + \
          table(["", ""], [["NOM", ""], ["Prénom", ""], ["Date de naissance (jj/mm/aaaa)", ""], ["Sexe", "☐ F   ☐ M   ☐ autre"], ["Adresse (rue, n°, code postal, ville)", ""], ["Téléphone des parents", ""], ["Langue(s) parlée(s) à la maison", ""],
                         ["Catégorie", "☐ U14 (né en 2013-2014)   ☐ U16 (2011-2012)   ☐ U18 (2009-2010)"], ["Allergie / problème de santé", "☐ non   ☐ oui : ________________"], ["Photos sur le site du club", "J'accepte / Je refuse (barrer la mention inutile)"],
                         ["Date et signature (élève + parent)", ""]], ["70mm", "112mm"]).replace("<td></td>", '<td style="height:9mm"></td>') + '<p class="xs">Cotisation : 120 € / an (payable en 3 fois). Entraînements : mardi et jeudi 17 h-18 h 30.</p></div>'
    e = E("Je remplis le formulaire pour moi (ou pour Yonas, né le 14/06/2012, rue Verte 8, 5000 Namur).", frm, ["lis", "ecris", "coche"], 2, "C",
          sol="Vérifier : NOM en majuscules, date jj/mm/aaaa, catégorie selon l'année de naissance (2012 → U16), mention barrée, signature.")
    b.page(f'<span class="tag-doc">📄 DOCUMENT DE LA VIE</span><h2>Le formulaire d\'inscription</h2>{e}', "Document de la vie")
    e = E("Je lis le formulaire et je réponds.", f'<p>1. Les entraînements sont quels jours ? {blank()} 2. La cotisation coûte combien par an ? {blank()}</p><p>3. Je suis né(e) en 2011 : ma catégorie ? {blank("s")} 4. « Barrer la mention inutile » : je fais quoi ? {blank("xl")}</p>', ["lis", "ecris"], 2, "B",
          sol="1. mardi et jeudi — 2. 120 € — 3. U16 — 4. Je barre ce qui n'est pas vrai (J'accepte ou Je refuse).")
    e2 = E("Défi ! La cotisation se paie en 3 fois. Combien chaque fois ?", f'<p>{blank("xl")}</p>', ["ecris"], 3, "C", sol="120 ÷ 3 = 40 €")
    e3 = E("Les messages courts. Je relie le SMS et le sens.", relie(["Dsl, je peux pas 😕", "Ok pr sam 👍", "Tu viens ? 🙂", "À +", "Mdr 😂"], ["J'accepte pour samedi.", "Je ris beaucoup.", "Désolé, je ne peux pas.", "À plus tard.", "Est-ce que tu viens ?"]), ["lis", "relie"], 2, "B",
           sol="Dsl → désolé, je ne peux pas · Ok pr sam → j'accepte pour samedi · Tu viens ? → est-ce que tu viens · À + → à plus tard · Mdr → je ris beaucoup")
    b.page(f'<span class="tag-doc">📄 DOCUMENT DE LA VIE</span><h2>Lire un formulaire · des SMS</h2>{e}{e2}{e3}<div class="attention">Sur un formulaire officiel ou dans un courriel à la prof, on n\'écrit <b>pas</b> en langage SMS.</div>', "Document de la vie")

    # ---------- Sons : intonation ----------
    e = E("L'intonation de la question. J'écoute, je répète en faisant le geste ✋↗️ / ✋↘️.", '<div class="grid2"><div class="card c"><div style="font-size:24pt">↗️</div><p class="big">Tu viens ? · C\'est loin ? · On y va ?</p><p class="sm muted">La voix monte à la fin.</p></div><div class="card c"><div style="font-size:24pt">↘️</div><p class="big">Tu viens. · C\'est loin. · On y va.</p><p class="sm muted">La voix descend à la fin.</p></div></div>', ["ecoute", "repete"], 1, "A",
          script="Lire chaque paire en exagérant. Les questions avec un mot (où, quand…) peuvent descendre : Où tu vas ? ↘️", sol="Activité orale.")
    e2 = E("J'écoute et je mets . ou ? à la fin.", '<p class="big">1. Tu fais du sport __ 2. Elle aime la danse __ 3. On joue au foot __ 4. C\'est gratuit __ 5. Il est malade __ 6. Vous venez samedi __</p>', ["ecoute", "complete"], 2, "A",
           script="1. Tu fais du sport ? (↗️) 2. Elle aime la danse. (↘️) 3. On joue au foot ? (↗️) 4. C'est gratuit. (↘️) 5. Il est malade ? (↗️) 6. Vous venez samedi. (↘️)", sol="? · . · ? · . · ? · .")
    e3 = E("Les émotions ! Je lis la même phrase : contente 😀, triste 😢, en colère 😠, surprise 😮.", '<div class="card c big">« Il y a un match samedi. »</div>', ["parle", "duo"], 2, "A", sol="Jeu de voix : intonation et émotion.")
    b.page(f'<h2>J\'écoute bien</h2>{e}{e2}{e3}', "Sons")
    e = E("🔁 Module 10 · Les verbes pronominaux.", '<p>Le samedi, je ___ lève tard. Nous ___ dépêchons pour le match.</p>', ["complete"], 1, "C", sol="me · nous")
    e2 = E("🔁 Module 10 · La fréquence.", '<p>Je fais du sport (0 %). → ______________________</p>', ["ecris"], 2, "C", sol="Je ne fais jamais de sport.")
    e3 = E("🔁 Module 9 · Aller à.", '<p>Mercredi, je vais ___ piscine et ___ cinéma.</p>', ["complete"], 1, "C", sol="à la · au")
    b.page(f'<h2>🔁 Je révise les modules 9 et 10</h2>{e}{e2}{e3}', "Je révise")

    # ---------- Ateliers ----------
    e = E("Trouve quelqu'un qui… ! Je me lève, je pose la question (Est-ce que tu… ?). Oui → j'écris le prénom.", '<div class="grid3">' + "".join(f'<div class="card" style="min-height:20mm"><p class="sm">{t}</p><div class="line"></div></div>' for t in ["… fait du vélo", "… joue d'un instrument", "… aime cuisiner", "… fait un sport de combat", "… va à la piscine", "… lit des mangas", "… joue aux échecs", "… regarde des séries", "… aime chanter"]) + '</div>', ["parle", "ecris", "groupe"], 1, "A",
          sol="Questions oui / non avec est-ce que ou intonation.")
    e2 = E("Le dé des questions : je lance le dé et je pose la question à mon voisin. 1 Où… ? 2 Quand… ? 3 Avec qui… ? 4 Qu'est-ce que… ? 5 Pourquoi… ? 6 Est-ce que… ?", '<div class="c" style="font-size:30pt">🎲</div>', ["joue", "parle", "duo"], 2, "D", sol="Questions variées sur les loisirs.")
    b.page(f'{atl_head("D", "Atelier · Questions et loisirs")}{e}{e2}', "Atelier")
    e = E("Je lis le message de Yonas. Je réponds.", '<div class="card">📱 <b>Yonas :</b> « Salut Mateo ! Merci pour le tournoi de mercredi, c\'était génial ! On a gagné 3 à 2 😎. Samedi, je vais courir au parc avec mon cousin. Tu veux venir ? On part à 10 h de chez moi. Après, on peut manger des frites à la friterie. Réponds-moi vite ! »</div>' +
          f'<p>1. Qui a gagné le tournoi ? Le score ? {blank("xl")}</p><p>2. Qu\'est-ce que Yonas fait samedi ? Avec qui ? {blank("xl")}</p><p>3. Rendez-vous où et à quelle heure ? {blank("xl")}</p>', ["lis", "ecris"], 2, "B",
          sol="1. l'équipe de Yonas (et Mateo) ; 3 à 2 — 2. Il va courir au parc avec son cousin. — 3. chez Yonas, à 10 h")
    e2 = E("J'écris la réponse de Mateo : il refuse poliment et propose un autre jour.", lines(3), ["ecris"], 2, "C", sol="Ex. : Merci Yonas ! Désolé, samedi je ne peux pas : je dois aller chez ma grand-mère. On court dimanche ?")
    b.page(f'{atl_head("C", "Atelier · Lire et écrire")}{e}{e2}', "Atelier")

    # ---------- ★ Alpha : lire des phrases complètes ----------
    e = E("Je lis les mots du sport.", '<div class="grid4">' + "".join(f'<div class="card c"><span class="emo s">{em}</span><div class="huge" style="font-size:16pt">{w}</div></div>' for em, w in [("⚽", "foot"), ("🏊", "pis·ci·ne"), ("🥊", "boxe"), ("🎾", "ten·nis"), ("🚴", "vé·lo"), ("💃", "dan·se"), ("🎮", "jeu"), ("📖", "li·vre")]) + '</div>', ["lis"], 1, "P", alpha=True, sol="Lecture.")
    e2 = E("Je lis la phrase et je colorie l'image juste.", "".join(f'<div class="card mb2 flex" style="justify-content:space-between"><p class="big" style="margin:0">{t}</p><span style="font-size:22pt">{o}</span></div>' for t, o in [("Je joue au foot.", "⚽ 🎾 🏊"), ("Il fait du vélo.", "🥊 🚴 📖"), ("Elle aime danser.", "💃 🎮 🏀"), ("On va à la piscine.", "🏫 🏊 🎬")]), ["lis", "colorie"], 1, "B", alpha=True, sol="⚽ · 🚴 · 💃 · 🏊")
    b.page(AL.format(t="Je lis des phrases") + e + e2, "★ Alpha", color=MC)
    e = E("Je lis le petit texte. Je réponds avec le doigt (je montre l'image).", '<div class="card" style="background:#FFFBEA"><p class="big" style="line-height:1.8">Sami a 14 ans.<br>Il aime le sport.<br>Le mercredi, il joue au foot.<br>Le samedi, il va à la piscine.</p></div>' +
          '<p class="big">1. Sami aime… 📖 ⚽ 🎸 &nbsp; 2. Le mercredi… 🏊 ⚽ 🎬 &nbsp; 3. Le samedi… 🏊 🏀 🥊</p>', ["lis", "montre"], 2, "P", alpha=True, sol="1. ⚽ (le sport) — 2. ⚽ — 3. 🏊")
    e2 = E("Je remets les mots dans l'ordre. J'écris la phrase.", "".join(f'<div class="flex mb2">{"".join(f"<span class=pill style=font-size:13pt>{w}</span>" for w in ws)}</div>' + guide_lines(1, 18) for ws in [["foot.", "joue", "Je", "au"], ["aime", "Il", "lire."]]), ["lis", "ecris"], 2, "C", alpha=True, sol="Je joue au foot. · Il aime lire.")
    b.page(AL.format(t="Je lis un texte") + e + e2, "★ Alpha", color=MC)
    e = E("Je remplis la fiche (avec l'aide de la prof).", table(["", ""], [["NOM", ""], ["Prénom", ""], ["Âge", ""], ["Mon sport", ""]], ["50mm", "132mm"]).replace("<td></td>", '<td style="height:14mm"></td>'), ["ecris"], 1, "C", alpha=True, sol="Nom en majuscules, prénom, âge, sport.")
    e2 = E("Dictée de phrases.", guide_lines(3, 20), ["ecoute", "ecris"], 2, "P", alpha=True, script="Dicter lentement, mot par mot : « Je joue. » — « Il fait du vélo. » — « On va au parc. »", sol="Je joue. Il fait du vélo. On va au parc.")
    b.page(AL.format(t="J'écris des phrases") + e + e2, "★ Alpha", color=MC)

    # ---------- Tâche finale ----------
    e = E("J'écris une invitation à une activité (sport, loisir, fête) pour un camarade : quoi, quand, où, à quelle heure, quoi apporter, comment répondre.", '<div class="card" style="height:62mm;background:#FFFBEA"></div>', ["ecris", "dessine"], 2, "C", sol="Les 6 informations sont présentes.")
    e2 = E("Je réponds à l'invitation que j'ai reçue d'un camarade : j'accepte ou je refuse poliment (avec une raison et une proposition).", '<div class="card" style="height:40mm"></div>', ["lis", "ecris"], 2, "C", sol="Formule d'accueil, réponse, raison si refus, formule finale.")
    b.page(tache_head("Mon invitation et ma réponse", "J'écris une invitation, je l'échange avec un camarade, puis j'écris une réponse à l'invitation que je reçois.") + e + e2 +
           table(["Je vérifie :", "✅"], [[x, '<span class="chk"></span>'] for x in ["Mon invitation dit quoi, quand, où, à quelle heure.", "J'utilise jouer au / faire du correctement.", "Ma réponse est polie (merci, désolé(e), avec plaisir).", "Si je refuse, je donne une raison (je dois…)."]], ["160mm", "22mm"]), "Tâche finale", levels=False)
    e = E("Je révise.", '<p>1. Nous ______ (faire) du vélo. 2. Je joue ___ tennis. 3. Elle fait ___ natation. 4. ______ tu viens ? (oui / non) 5. Je ne peux pas, je ______ (devoir) étudier.</p>', ["ecris"], 2, "C",
          sol="faisons · au · de la · Est-ce que · dois")
    e2 = E("Défi ! Je corrige les 4 erreurs.", '<div class="card big">Je fais du danse et je joue à le foot. Vous faisez du sport ? Désolé, je dois étudie.</div>' + lines(1), ["barre", "ecris"], 3, "C",
           sol="de la danse · au foot · Vous faites · je dois étudier")
    b.page(f'<h2>🔁 Je révise tout le module</h2>{e}{e2}', "Je révise")

    # ---------- Test ----------
    Q = [("🏊 :", ["le tennis", "la natation", "la boxe", "le vélo"]), ("🎸 Je joue ____ guitare.", ["au", "de la", "à la", "du"]), ("Je joue ____ foot.", ["du", "au", "de la", "à le"]),
         ("Elle fait ____ danse.", ["du", "de la", "au", "à la"]), ("Il fait ____ escalade.", ["de l'", "du", "de la", "au"]), ("Nous ____ du sport.", ["faisons", "faites", "font", "fais"]),
         ("Vous ____ du judo ?", ["faisez", "faites", "faisons", "font"]), ("J'adore ____.", ["nage", "nager", "nages", "nagé"]), ("On ____ au cinéma ?", ["allons", "va", "vont", "allez"]),
         ("Question oui / non :", ["Où tu vas ?", "Est-ce que tu viens ?", "Quand est le match ?", "Qu'est-ce que tu fais ?"]), ("— ____ commence le film ? — À 20 h.", ["Où", "À quelle heure", "Avec qui", "Pourquoi"]),
         ("— ____ tu fais de la boxe ? — Parce que j'aime ça.", ["Pourquoi", "Combien", "Quand", "Où"]), ("Accepter :", ["Désolé, je ne peux pas.", "Avec plaisir !", "Une autre fois.", "Je dois étudier."]),
         ("Refuser poliment :", ["Non !", "Je ne veux pas.", "Désolé, je ne peux pas, je dois aider ma mère.", "Nul !"]), ("Ils ____ partir.", ["doit", "doivent", "devons", "dois"]),
         ("Sur un formulaire, le NOM s'écrit :", ["en minuscules", "en MAJUSCULES", "en couleur", "en chiffres"]), ("La date « 5 mars 2011 » :", ["05/03/2011", "03/05/2011", "2011/05/03", "5/2011/3"]),
         ("« Barrer la mention inutile » =", ["entourer", "barrer ce qui est faux", "souligner", "signer"]), ("« Tu viens ? » ↗️ La voix…", ["monte", "descend", "ne change pas", "s'arrête"]),
         ("🔁 Je ____ lève tard le samedi.", ["te", "se", "me", "nous"])]
    ans = ["la natation", "de la", "au", "de la", "de l'", "faisons", "faites", "nager", "va", "Est-ce que tu viens ?", "À quelle heure", "Pourquoi", "Avec plaisir !", "Désolé, je ne peux pas, je dois aider ma mère.", "doivent", "en MAJUSCULES", "05/03/2011", "barrer ce qui est faux", "monte", "me"]
    key = key_from(Q, ans)
    test_pages(b, 11, "Loisirs et sport", Q, f'<h3>B1. J\'écris 2 phrases sur mes loisirs avec jouer au / faire du. (… / 2)</h3>{lines(1, True)}<h3>B2. J\'écris 3 questions avec où, quand, est-ce que. (… / 3)</h3>{lines(2, True)}<h3>B3. Mon ami m\'invite au cinéma samedi. Je refuse poliment avec une raison. (… / 5)</h3>{lines(2, True)}',
               [["inviter un camarade (quoi, quand, où)", "/ 4", ""], ["accepter ou refuser poliment", "/ 3", ""], ["répondre à 3 questions sur mes loisirs", "/ 3", ""]],
               f'<h3>1. Je lis et je relie. (… / 4)</h3>{relie([f"<b class=big>{w}</b>" for w in ["foot", "vélo", "danse", "piscine"]], ["<span class=\'emo s\'>💃</span>", "<span class=\'emo s\'>🏊</span>", "<span class=\'emo s\'>⚽</span>", "<span class=\'emo s\'>🚴</span>"])}<h3>2. Je lis la phrase et j\'entoure l\'image. (… / 4)</h3><div class="card big">Il fait du vélo. 🥊 🚴 📖 · Je joue au foot. ⚽ 🎸 🏊</div><h3>3. Je remets les mots dans l\'ordre. (… / 4)</h3><div class="flex"><span class="pill">va</span><span class="pill">On</span><span class="pill">parc.</span><span class="pill">au</span></div>{guide_lines(1, 20)}<h3>4. Dictée : 1 phrase. (… / 4)</h3>{guide_lines(1, 22)}<h3>5. Je dis mon sport préféré (oral). (… / 4)</h3><div class="card">☐ je comprends ☐ je réponds ☐ phrase complète ☐ je pose une question</div>')
    closing(b, 11, ["Je sais nommer des sports et des loisirs.", "Je sais conjuguer faire.", "Je sais dire jouer au… / faire du…", "Je sais dire j'aime + verbe et pourquoi.", "Je sais utiliser « on ».",
                    "Je sais poser une question (est-ce que, où, quand…).", "Je sais inviter, accepter, refuser.", "Je sais conjuguer devoir.", "Je sais remplir un formulaire.", "Je sais lire une affiche d'activités.", "★ Je sais lire des phrases et un petit texte."],
            SPORTS[:12] + LOISIRS[:6] + [("💌", "inviter"), ("👍", "avec plaisir"), ("😕", "désolé(e)"), ("📝", "le formulaire"), ("🏠", "la maison de jeunes"), ("❓", "est-ce que")])
    plan_de_travail(b, E, 11, ["Jouer au · faire du · faire", "Aimer + verbe · on", "Poser une question", "Inviter · accepter · refuser", "Remplir un formulaire"], "☐ Mon invitation<br>☐ Ma réponse à une invitation")
    if render:
        to_pdf(b.html(), '/home/claude/syllabus/out/V1_M11_eleve.pdf')

    pg, exs = helpers(b, E)
    A = b.marks["★ Alpha"]
    days = [("1", "Collectif", f"Ouverture · BD ({pg('Découvrir')})", f"Alpha : mots du sport (p. {A[0]})"), ("2", "Collectif", f"Sports et loisirs ({pg('Lexique')})", f"Alpha : phrases-images (p. {A[0]})"),
            ("3", "Rotation", f"📌 Leçon 1 jouer au / faire du ({pg('Leçon 1')})", f"Alpha : petit texte (p. {A[1]})"), ("4", "Rotation", f"📌 Leçon 2 aimer + verbe, on ({pg('Leçon 2')})", f"Alpha : mots dans l'ordre (p. {A[1]})"),
            ("5", "Collectif", f"📌 Leçon 3 questions ({pg('Leçon 3')}) · intonation ({pg('Sons')})", f"Alpha : fiche + dictée (p. {A[2]})"), ("6", "Rotation", f"📌 Leçon 4 inviter ({pg('Leçon 4')})", "Alpha : inviter à l'oral"),
            ("7", "Collectif", f"Formulaire ({pg('Consignes & école')}) · affiche, inscription ({pg('Document de la vie')})", "Alpha : son nom en majuscules"), ("8", "Ateliers", f"Trouve quelqu'un qui…, dé des questions, message ({pg('Atelier')})", "Alpha : trouve quelqu'un (images)"),
            ("9", "Duo", f"Tâche finale ({pg('Tâche finale')})", "Alpha : invitation dessinée + 1 phrase"), ("10", "Seul", f"Test ({pg('Test')})", f"Alpha : test ({pg('★ Alpha · Test')})")]
    rot = [["🎧 Écouter-Parler", "Trouve quelqu'un qui… · téléphone", "20 min", "—"], ["📖 Lire", "Affiche · message de Yonas", "20 min", "Oui"], ["✏️ Écrire", "Formulaire · réponse à une invitation", "20 min", "● oui"],
           ["🧩 Jouer", "Dé des questions · mime des sports", "20 min", "Entre joueurs"], ["👩‍🏫 Table d'appui", "Alpha : phrases · autres : au / du, questions", "20 min", "—"]]
    ev1 = '''<h3>Partie B (10 points)</h3><p class="sm"><b>B1</b> : 1 pt par phrase juste (au / du / de la) · <b>B2</b> : 1 pt par question bien formée · <b>B3</b> : <span class="sol">Merci pour l'invitation ! Désolé(e), je ne peux pas samedi : je dois aider ma mère. On y va dimanche ?</span> (politesse 2, raison avec devoir 2, proposition 1).</p>
<h3>Test ★ Alpha</h3><p class="sm"><b>Ex. 1 :</b> <span class="sol">foot–⚽, vélo–🚴, danse–💃, piscine–🏊</span> · <b>Ex. 2 :</b> <span class="sol">🚴 · ⚽</span> · <b>Ex. 3 :</b> <span class="sol">On va au parc.</span> · <b>Ex. 4, dicter :</b> <span class="sol">Je joue au foot.</span></p>'''
    ev2 = f'''<h2>Grille · tâche finale « Mon invitation et ma réponse »</h2>{table(["Critère", "Très bien", "Bien", "À retravailler", "Points"], [["<b>Invitation</b> : quoi, quand, où, heure, quoi apporter, répondre", "6 infos", "4-5", "≤ 3", "/ 6"], ["<b>Langue</b> : jouer au / faire du, questions", "Correct", "Quelques erreurs", "Beaucoup", "/ 4"], ["<b>Réponse</b> polie, raison (je dois…)", "Oui", "Partielle", "Non", "/ 5"], ["<b>Présentation</b> : mise en page, écriture", "Soignée", "Correcte", "À revoir", "/ 5"]], ["64mm", "32mm", "32mm", "32mm", "22mm"])}
<h2 class="mt4">Différencier et remédier</h2>{table(["Difficulté", "Remédiation"], [["jouer au / faire du", "Deux boîtes : « avec un ballon / un jeu » → jouer à · « une activité » → faire de ; instrument → jouer de."], ["Questions", "Cartes-mots interrogatifs + cartes-réponses à apparier ; geste de l'intonation."], ["Refuser poliment", "Banque de raisons affichée (je dois aider, étudier, aller chez…)."], ["Formulaire", "Remplir d'abord un formulaire d'un personnage fictif, puis le sien."], ["Élève rapide", "Comparer deux vraies offres de clubs (prix, horaires) et argumenter son choix."]], ["50mm", "132mm"])}
<div class="astuce mt4"><b>Inclusion :</b> beaucoup d'élèves DASPA ne savent pas qu'ils peuvent accéder aux clubs, maisons de jeunes et écoles de devoirs. Inviter un animateur de la MJ locale ; signaler les aides (chèques sport, réductions communales, CPAS). Respecter les choix (piscine mixte, tenue).</div>'''
    T = teacher_book(b, E, "V1 · M11", "", MC, 11, "Loisirs et sport",
                     "<li><b>Communication :</b> parler de ses loisirs, inviter, accepter, refuser, poser des questions.</li><li><b>Lexique :</b> sports, loisirs, lieux de loisirs, formulaire.</li><li><b>Grammaire :</b> faire, devoir ; jouer au / faire du ; aimer + infinitif ; on ; questions (est-ce que, mots interrogatifs).</li><li><b>Phonétique :</b> intonation de la question.</li><li><b>FLSco :</b> remplir un formulaire, écrire une date.</li><li><b>Documents :</b> affiche de maison de jeunes, formulaire d'inscription, SMS.</li><li><b>★ Alpha :</b> lecture de phrases complètes et d'un petit texte.</li>",
                     '<p class="sm"><b style="color:#E4572E">Indispensable</b> : je fais / je joue, inviter, accepter, refuser, remplir NOM / prénom / date.</p><p class="sm"><b style="color:#d9a400">Important</b> : questions, on, aimer + infinitif.</p><p class="sm"><b style="color:#2BA88F">Enrichissement</b> : SMS, interview, comparaison d\'offres.</p>',
                     "Dés · ballons ou objets de sport · affiches réelles de la commune / MJ · formulaires réels (anonymisés).", "<b>Visite ou invité :</b> un animateur de la maison de jeunes ou d'un club présente ses activités ; les élèves préparent leurs questions (leçon 3).",
                     days, "« Tu fais quoi mercredi ? » en chaîne · une question du jour à poser à la prof · mime d'un sport.", rot, key, (ev1, ev2), start=tstart)
    if render:
        to_pdf(T.html(), '/home/claude/syllabus/out/V1_M11_prof.pdf')
    return b, T


if __name__ == "__main__":
    b, T = build_m11()
    print(b.n, T.n)
