"""Volume 2 · Module 1 « Nouveau départ » (A2)."""
import sys
sys.path.insert(0, '/home/claude/syllabus')
from lib.base import *
from lib.art import *
from lib.module import *
from lib.v2 import CP, CPCOL, v2_cover, v2_mon_livre
from lib.render import to_pdf

MC = "#2BA88F"
PAYS = [("🇸🇾", "la Syrie", "syrien · syrienne", "l'arabe"), ("🇺🇦", "l'Ukraine", "ukrainien · ukrainienne", "l'ukrainien"), ("🇦🇫", "l'Afghanistan", "afghan · afghane", "le dari, le pachto"),
        ("🇪🇷", "l'Érythrée", "érythréen · érythréenne", "le tigrinya"), ("🇬🇳", "la Guinée", "guinéen · guinéenne", "le peul, le français"), ("🇲🇦", "le Maroc", "marocain · marocaine", "l'arabe, le berbère"),
        ("🇨🇴", "la Colombie", "colombien · colombienne", "l'espagnol"), ("🇹🇷", "la Turquie", "turc · turque", "le turc"), ("🇷🇴", "la Roumanie", "roumain · roumaine", "le roumain"),
        ("🇧🇷", "le Brésil", "brésilien · brésilienne", "le portugais"), ("🇨🇩", "la RD Congo", "congolais · congolaise", "le lingala, le français"), ("🇧🇪", "la Belgique", "belge · belge", "le français, le néerlandais, l'allemand")]
QUAL = [("🔍", "curieux · curieuse"), ("🧘", "patient · patiente"), ("📏", "sérieux · sérieuse"), ("🦁", "courageux · courageuse"), ("😂", "drôle · drôle"), ("🙈", "timide · timide"),
        ("🤝", "sociable · sociable"), ("🎨", "créatif · créative"), ("💪", "travailleur · travailleuse"), ("💛", "gentil · gentille"), ("🗂️", "organisé · organisée"), ("⚡", "sportif · sportive")]
ETRE = ["aller", "venir", "arriver", "partir", "entrer", "sortir", "monter", "descendre", "naître", "mourir", "rester", "tomber", "retourner", "devenir", "revenir", "passer (par)"]


def maison_etre():
    fl = [(60, ["⬆️ monter", "⬇️ descendre", "👶 naître", "⚰️ mourir"]), (92, ["🚪 entrer", "🏃 sortir", "🛋️ rester", "🤕 tomber"]), (124, ["➡️ aller", "⬅️ venir", "🛬 arriver", "✈️ partir"])]
    t = ""
    for y, ws in fl:
        step = 184 / len(ws)
        t += "".join(f'<text x="{8 + step * (i + .5):.0f}" y="{y}" font-size="7.2" text-anchor="middle" font-family="Poppins" font-weight="700">{w}</text>' for i, w in enumerate(ws))
    return (f'<svg viewBox="0 0 200 140" width="100%" style="max-height:84mm"><polygon points="100,2 196,40 4,40" fill="#2BA88F"/><text x="100" y="31" font-size="11" text-anchor="middle" font-family="Poppins" font-weight="800" fill="#fff">LA MAISON D\'ÊTRE</text>'
            f'<rect x="8" y="40" width="184" height="98" fill="#EEF8F4" stroke="#2BA88F" stroke-width="2"/><line x1="8" y1="72" x2="192" y2="72" stroke="#2BA88F"/><line x1="8" y1="104" x2="192" y2="104" stroke="#2BA88F"/>{t}</svg>')


def build_v2m1(start=1, tstart=1, render=True):
    b = Book("V2 · M1", "Volume 2 · Je me débrouille · Module 1 · Nouveau départ", MC, start=start)
    E = Ex(b)
    v2_cover(b, "Je me<br>débrouille", "Niveau A2 · lire, raconter, agir seul", "Module 1 · Nouveau départ")
    v2_mon_livre(b)
    vis = '<div class="c" style="font-size:38pt;line-height:1.3">🎒🗺️🗣️📚💬<br>🌍🇧🇪🤝✨📝</div>'
    opening(b, MC, 1, "Nouveau départ", vis, [("🙋", "me présenter en détail (pays, langues, études, qualités)"), ("🗣️", "parler de mes langues et de mon parcours scolaire"), ("🔁", "réviser le présent"),
            ("⬅️", "raconter au passé composé avec avoir et être"), ("📧", "lire et écrire un courriel de présentation"), ("📜", "comprendre le règlement de l'école (ROI)")],
            ["Qu'est-ce que tu as appris l'année passée ?", "Combien de langues tu parles ? Où tu les utilises ?", "Quelle est ta qualité principale ?"],
            ["la nationalité", "la langue maternelle", "la qualité", "je suis né(e)", "je suis arrivé(e)", "depuis", "le parcours", "le courriel", "le règlement", "l'objet"], "#E3F4EE")

    # ---------- Découvrir ----------
    bd = '<div class="grid2" style="gap:3mm">' + "".join([
        bd_case(1, lr("prof", ["Bonjour à tous ! Bienvenue en deuxième année au DASPA. Aujourd'hui, une nouvelle élève arrive : voici Nour."], "nour", ["Bonjour…"], "sourire", "neutre")),
        bd_case(2, lr("nour", ["Je m'appelle Nour. J'ai 14 ans. Je suis syrienne, mais j'ai habité trois ans en Turquie."], "yonas", ["Bienvenue, Nour ! Tu parles quelles langues ?"], "sourire", "sourire")),
        bd_case(3, lr("nour", ["L'arabe, c'est ma langue maternelle. Je parle aussi turc et un peu anglais. Le français, j'ai commencé il y a deux mois."], extra='<div class="c" style="font-size:20pt">🇸🇾🇹🇷🇬🇧➡️🇧🇪</div>')),
        bd_case(4, lr("daria", ["Moi aussi, je suis arrivée sans parler français ! Maintenant, je lis des livres en français."], "nour", ["C'est vrai ? Tu es arrivée quand ?"], "rire", "surpris")),
        bd_case(5, lr("daria", ["Il y a un an et demi. Au début, c'était difficile. Mais je suis curieuse et travailleuse !"], "mateo", ["Et elle est un peu bavarde aussi ! 😄"], "rire", "rire")),
        bd_case(6, lr("prof", ["Cette année, vous allez apprendre à vous débrouiller seuls. Le premier projet : votre portrait de langues !"], "nour", ["J'ai déjà hâte !"], "sourire", "rire")),
    ]) + '</div>'
    e = E("J'écoute et je lis la BD : une nouvelle élève.", bd, ["ecoute", "lis"], 1, "A",
          script="Lire deux fois, puis distribuer les rôles. Faire relever : les pays, les langues, les verbes au passé (j'ai habité, j'ai commencé, je suis arrivée). Demander : « Et vous, vous êtes arrivés quand ? » (sans insister : chacun dit ce qu'il veut).", sol="Activité orale.")
    b.page(f'<h2>Découvrir · Une nouvelle élève</h2>{e}', "Découvrir")
    e = E("Je réponds par une phrase complète.", f'<p>1. Quelle est la nationalité de Nour ? {blank("xl")}</p><p>2. Où est-ce qu\'elle a habité avant la Belgique ? Combien de temps ? {blank("xl")}</p><p>3. Quelles langues parle-t-elle ? {blank("xl")}</p><p>4. Daria est arrivée quand ? {blank("xl")}</p><p>5. Quelles sont les qualités de Daria ? {blank("xl")}</p><p>6. Quel est le premier projet de la classe ? {blank("xl")}</p>',
          ["lis", "ecris"], 1, "B", sol="1. Elle est syrienne. — 2. Elle a habité en Turquie pendant trois ans. — 3. l'arabe (langue maternelle), le turc, un peu l'anglais et le français. — 4. il y a un an et demi — 5. curieuse, travailleuse (et un peu bavarde) — 6. le portrait de langues")
    e2 = E("Vrai, faux ou on ne sait pas ?", table(["", "Vrai", "Faux", "On ne sait pas"], [[x, '<span class="chk"></span>', '<span class="chk"></span>', '<span class="chk"></span>'] for x in ["Nour a commencé le français il y a deux ans.", "Nour a des frères et sœurs.", "Daria lit des livres en français.", "Mateo trouve que Daria parle beaucoup."]], ["110mm", "22mm", "22mm", "28mm"]), ["lis", "coche"], 2, "B",
           sol="Faux (il y a deux mois) · On ne sait pas · Vrai · Vrai")
    b.page(f'{e}{e2}<div class="astuce">« <b>Je me débrouille</b> » = je trouve une solution seul(e), je n\'ai pas besoin d\'aide. C\'est le titre de ce volume !</div>', "Découvrir")
    txt = '''<div class="doc" style="transform:none;padding:4mm;background:#fff;border:1px solid #d0d6e0"><div class="flex" style="justify-content:space-between"><b style="color:#2BA88F">📰 LE JOURNAL DU DASPA · n° 12</b><span class="xs muted">septembre</span></div>
<h3 style="margin:2mm 0">Rencontre avec Nour, notre nouvelle élève</h3>
<p class="sm" style="line-height:1.6"><b>Nour, présente-toi !</b> — Je m'appelle Nour Haddad, j'ai 14 ans et je suis née à Alep, en Syrie. J'ai deux petits frères et une grande sœur.<br>
<b>Tu es en Belgique depuis quand ?</b> — Depuis le mois de juillet. Avant, nous avons habité trois ans à Gaziantep, en Turquie. Là-bas, je suis allée à l'école turque : j'ai appris le turc en six mois !<br>
<b>Qu'est-ce que tu aimes à l'école ?</b> — J'adore les maths et les sciences. Plus tard, je voudrais devenir pharmacienne. Par contre, je n'aime pas beaucoup le sport…<br>
<b>Comment tu te décris ?</b> — Je suis sérieuse et patiente, mais un peu timide au début. Quand je connais les gens, je suis très drôle ! 😄<br>
<b>Ton premier jour en Belgique ?</b> — Il a plu toute la journée ! Je suis sortie sans parapluie… Maintenant, je suis toujours prête.</p></div>'''
    e = E("Je lis l'interview du journal de l'école. Je complète la fiche de Nour.", txt + table(["", ""], [["Nom et âge", ""], ["Lieu de naissance", ""], ["Famille", ""], ["En Belgique depuis", ""], ["Matières préférées", ""], ["Métier rêvé", ""], ["Qualités", ""]], ["50mm", "132mm"]).replace("<td></td>", '<td style="height:7mm"></td>'),
          ["lis", "ecris"], 2, "B", sol="Nour Haddad, 14 ans · Alep (Syrie) · deux petits frères, une grande sœur · juillet · maths et sciences · pharmacienne · sérieuse, patiente, (timide au début), drôle")
    b.page(f'<h2>Découvrir · L\'interview</h2>{e}', "Découvrir")

    # ---------- Lexique ----------
    rows = [[f'<span style="font-size:15pt">{f}</span>', f"<b>{p}</b>", n, f'<span class="sm">{l}</span>'] for f, p, n, l in PAYS]
    e = E("Pays, nationalités, langues. J'écoute et je répète. Je complète la dernière ligne pour moi.", table(["", "Pays", "Nationalité (masc. · fém.)", "Langue(s)"], rows + [["🌍", "", "", ""]], ["12mm", "40mm", "70mm", "60mm"]), ["ecoute", "repete", "ecris"], 1, "A",
          script="Lire chaque ligne. Faire remarquer : le pays a un article (la Syrie, le Maroc), la nationalité n'a pas de majuscule (elle est syrienne), mais le nom de l'habitant en a une (les Syriens). Chacun complète sa ligne.", sol="Ligne personnelle.")
    b.page(f'<h2>Pays, nationalités, langues</h2>{e}<div class="attention">Majuscule ? <b>la Syrie</b> (pays) · <b>un Syrien</b> (la personne) · <b>il est syrien</b> (adjectif, pas de majuscule) · <b>l\'arabe</b> (langue, pas de majuscule).</div>', "Lexique")
    e = E("Les qualités. J'écoute et je répète.", '<div class="grid4">' + "".join(f'<div class="card c" style="padding:2mm"><span class="emo s">{em}</span><div class="sm"><b>{q}</b></div></div>' for em, q in QUAL) + '</div>', ["ecoute", "repete"], 1, "A",
          script="Lire masculin puis féminin. Jeu : chaque élève choisit une qualité pour son voisin (« Tu es patiente parce que… »). Rester bienveillant.", sol="Activité orale.")
    e2 = E("Les matières de l'école. Je relie.", relie(["les mathématiques", "les sciences", "l'histoire", "la géographie", "l'éducation physique", "le néerlandais"], ["les pays, les cartes", "le sport", "les nombres, les calculs", "une autre langue de Belgique", "le passé, les événements", "les plantes, le corps, l'énergie"]), ["relie"], 1, "B",
           sol="maths → nombres · sciences → plantes, corps · histoire → passé · géo → pays, cartes · EP → sport · néerlandais → langue de Belgique")
    b.page(f'{e}{e2}', "Lexique")

    # ---------- Leçon 1 : présent (révision) ----------
    l1 = lecon("Le présent : je révise les verbes essentiels", table(["", "-er : parler", "-ir : finir", "être", "avoir", "aller", "faire"], [[p] + v for p, v in zip(["je / j'", "tu", "il / elle / on", "nous", "vous", "ils / elles"],
                [["parle", "finis", "suis", "ai", "vais", "fais"], ["parles", "finis", "es", "as", "vas", "fais"], ["parle", "finit", "est", "a", "va", "fait"], ["parlons", "finissons", "sommes", "avons", "allons", "faisons"], ["parlez", "finissez", "êtes", "avez", "allez", "faites"], ["parlent", "finissent", "sont", "ont", "vont", "font"]])], ["28mm", "26mm", "26mm", "24mm", "24mm", "26mm", "28mm"]) +
               '<p class="mt2"><b>Autres verbes utiles :</b> venir (je viens, nous venons, ils viennent) · pouvoir (je peux) · vouloir (je veux) · savoir (je sais, nous savons, ils savent) · connaître (je connais, nous connaissons)</p><p class="sm">Le présent sert à parler <b>d\'aujourd\'hui</b>, d\'une <b>habitude</b> (je vais au club le mercredi) et d\'une <b>action qui continue</b> avec <b>depuis</b> (j\'habite ici depuis un an).</p>')
    e = E("Je conjugue au présent.", '<p>1. Nour (venir) ______ de Syrie. 2. Nous (finir) ______ à 15 h 30. 3. Vous (savoir) ______ parler turc ? 4. Mes parents (connaître) ______ bien la ville. 5. Je (pouvoir) ______ t\'aider. 6. Les élèves (faire) ______ un projet.</p>', ["complete"], 1, "C",
          sol="vient · finissons · savez · connaissent · peux · font")
    b.page(f'{l1}{e}', "Leçon 1")
    e = E("Savoir ou connaître ? Je complète.", '<div class="astuce" style="margin-top:0"><b>savoir</b> + verbe / une information (je sais nager, je sais où il habite) · <b>connaître</b> + une personne, un lieu (je connais Nour, je connais Namur)</div><p>1. Tu ______ Mme Lambert ? 2. Je ______ jouer de la guitare. 3. Nous ______ bien Bruxelles. 4. Elle ______ où est la bibliothèque. 5. Vous ______ la réponse ?</p>', ["complete"], 2, "C",
          sol="connais · sais · connaissons · sait · savez")
    e2 = E("J'écris 5 phrases au présent sur moi aujourd'hui : où j'habite (depuis…), ce que je sais faire, ce que j'aime, ce que je fais le week-end.", lines(5), ["ecris"], 2, "C", sol="Production : verbes variés, depuis + durée.")
    e3 = E("Défi ! Je trouve et je corrige les 4 erreurs.", '<div class="card big">Nous finons à 16 h. Vous faisez du sport ? Je connais nager. Ils vient de Guinée.</div>' + lines(1), ["barre", "ecris"], 3, "C", sol="finissons · faites · Je sais nager · Ils viennent")
    b.page(f'{e}{e2}{e3}', "S'entraîner")

    # ---------- Leçon 2 : nationalités et qualités (accord) ----------
    l2 = lecon("Masculin et féminin des nationalités et des qualités", table(["Terminaison", "Masculin", "Féminin", "Exemples"], [["-ien → -ienne", "syrien", "syrienne", "ukrainien(ne), colombien(ne)"], ["-ain → -aine", "marocain", "marocaine", "roumain(e), africain(e)"], ["-ais → -aise", "congolais", "congolaise", "français(e), anglais(e)"],
              ["-eux → -euse", "curieux", "curieuse", "sérieux, courageux"], ["-if → -ive", "sportif", "sportive", "créatif, actif"], ["-eur → -euse", "travailleur", "travailleuse", "menteur, rêveur"], ["-e → -e", "belge, timide", "belge, timide", "drôle, sociable, calme"], ["⚠️ irrégulier", "gentil · turc", "gentille · turque", "grec → grecque"]], ["34mm", "34mm", "34mm", "80mm"]) +
               '<p class="mt2">Pluriel : + <b>s</b> (des élèves syriens) — mais <b>-eux</b> ne change pas (ils sont curieux) et <b>-ais</b> non plus (ils sont congolais).</p>')
    e = E("Je mets au féminin.", '<div class="grid2"><p>1. Il est ukrainien. → Elle est ______.</p><p>2. Il est courageux. → Elle est ______.</p><p>3. Il est créatif. → Elle est ______.</p><p>4. Il est gentil. → Elle est ______.</p><p>5. Il est turc. → Elle est ______.</p><p>6. Il est drôle. → Elle est ______.</p></div>', ["ecris"], 1, "C",
          sol="ukrainienne · courageuse · créative · gentille · turque · drôle")
    b.page(f'{l2}{e}', "Leçon 2")
    e = E("J'écoute : c'est un garçon 👦, une fille 👧 ou on ne sait pas ❓ ?", checks(8, ["👦", "👧", "❓"]), ["ecoute", "coche"], 2, "A",
          script="1. Je suis colombienne. — 2. Je suis belge. — 3. Je suis sérieux. — 4. Je suis sportive. — 5. Je suis timide. — 6. Je suis marocain. — 7. Je suis travailleuse. — 8. Je suis curieux.",
          sol="1. 👧 — 2. ❓ — 3. 👦 — 4. 👧 — 5. ❓ — 6. 👦 — 7. 👧 — 8. 👦")
    e2 = E("Je décris 2 camarades (nationalité + 2 qualités + une preuve : « parce que… »).", lines(4), ["ecris", "regarde"], 2, "C", sol="Ex. : Fatou est guinéenne. Elle est drôle et courageuse parce qu'elle…")
    e3 = E("Jeu « Qui est-ce ? » : je décris un élève de la classe sans dire son nom. Les autres devinent.", '<div class="card"><p>Il / Elle est… Il / Elle parle… Il / Elle est arrivé(e)… Il / Elle aime…</p></div>', ["parle", "groupe", "joue"], 2, "A", sol="Accord oral des adjectifs.")
    b.page(f'{e}{e2}{e3}', "S'entraîner")

    # ---------- Leçon 3 : passé composé avec avoir (révision) ----------
    l3 = lecon("Le passé composé avec avoir (révision)", '''<p><b>avoir</b> au présent + <b>participe passé</b> : j'<b>ai</b> appris · tu <b>as</b> habité · il <b>a</b> fini · nous <b>avons</b> pris · vous <b>avez</b> vu · ils <b>ont</b> fait</p>
<div class="grid3"><div class="card" style="background:#fff"><b>-er → -é</b><p class="sm">habiter → habité<br>commencer → commencé<br>étudier → étudié</p></div><div class="card" style="background:#fff"><b>-ir → -i</b><p class="sm">finir → fini<br>choisir → choisi<br>dormir → dormi</p></div>
<div class="card" style="background:#fff"><b>⚠️ irréguliers</b><p class="sm">faire → fait · prendre → pris · apprendre → appris · comprendre → compris · voir → vu · lire → lu · avoir → eu · être → été · pouvoir → pu · vouloir → voulu · écrire → écrit · dire → dit · mettre → mis · connaître → connu</p></div></div>
<p class="mt2">Négation : je <b>n\'</b>ai <b>pas</b> compris. — Question : Tu <b>as</b> déjà <b>visité</b> Bruxelles ? — Avec <b>il y a</b> : j\'ai commencé le français <b>il y a</b> deux mois (= deux mois avant aujourd\'hui).</p>''')
    e = E("Je conjugue au passé composé.", '<p>1. L\'année passée, j\'(apprendre) ______ à lire en français. 2. Nour (habiter) ______ en Turquie. 3. Nous (choisir) ______ un projet. 4. Tu (comprendre) ______ la consigne ? 5. Mes cousins (faire) ______ un long voyage. 6. Vous (lire) ______ le règlement ?</p>', ["complete"], 1, "C",
          sol="j'ai appris · a habité · avons choisi · as compris · ont fait · avez lu")
    b.page(f'{l3}{e}', "Leçon 3")
    e = E("J'écris le participe passé et je classe le verbe.", table(["-é", "-i", "-u", "-is / -it / autre"], [["", "", "", ""]], ["45mm"] * 4).replace("<td></td>", '<td style="height:24mm"></td>') + '<p class="sm mt2">regarder · finir · voir · prendre · dormir · lire · écrire · aimer · connaître · choisir · mettre · pouvoir · dire · parler</p>', ["ecris"], 2, "C",
          sol="-é : regardé, aimé, parlé · -i : fini, dormi, choisi · -u : vu, lu, connu, pu · autre : pris, écrit, mis, dit")
    e2 = E("Je réponds à la forme négative.", '<p>1. Tu as fini tes devoirs ? — Non, ______________________</p><p>2. Vous avez vu le film ? — Non, ______________________</p>', ["ecris"], 2, "C", sol="je n'ai pas fini mes devoirs · nous n'avons pas vu le film")
    e3 = E("L'année passée au DASPA : j'écris 4 choses que j'ai apprises ou faites.", lines(4), ["ecris"], 2, "C", sol="L'année passée, j'ai appris… j'ai lu… j'ai fait… j'ai eu…")
    b.page(f'{e}{e2}{e3}', "S'entraîner")

    # ---------- Leçon 4 : passé composé avec être ----------
    l4 = lecon("Le passé composé avec être", f'''<div class="flex top" style="gap:3mm"><div style="width:118mm;flex:none">{maison_etre()}</div><div class="card grow" style="background:#fff"><b>ÊTRE</b> au présent + participe<p>je <b>suis</b> arrivé(e)<br>tu <b>es</b> arrivé(e)<br>il <b>est</b> arrivé · elle <b>est</b> arrivé<b>e</b><br>nous <b>sommes</b> arrivé(e)<b>s</b><br>vous <b>êtes</b> arrivé(e)(s)<br>ils <b>sont</b> arrivé<b>s</b> · elles <b>sont</b> arrivé<b>es</b></p></div></div>
<div class="attention" style="margin-top:2mm">Avec <b>être</b>, le participe <b>s'accorde avec le sujet</b> comme un adjectif : Nour est arrivé<b>e</b>. Ses frères sont né<b>s</b> en Turquie. — Aussi : retourner, revenir, devenir, passer (par). Participes à retenir : né · mort · venu · devenu · descendu.</div>
<p class="sm">Être aussi pour <b>tous les verbes pronominaux</b> : je me suis levé(e), elle s'est habillée.</p>''')
    e = E("Avoir ou être ? Je complète avec l'auxiliaire.", '<p>1. Je ___ arrivée en juillet. 2. Nous ___ visité la ville. 3. Mes frères ___ nés à Alep. 4. Tu ___ mangé ? 5. Elle ___ sortie sans parapluie. 6. Ils ___ appris le turc.</p>', ["complete"], 1, "C", sol="suis · avons · sont · as · est · ont")
    b.page(f'{l4}{e}', "Leçon 4")
    e = E("J'accorde le participe passé (si nécessaire).", '<p>1. Daria est arrivé__ en Belgique il y a un an. 2. Yonas et Mateo sont parti__ au foot. 3. Nour et sa sœur sont né__ en Syrie. 4. Nous avons mangé__ à la cantine. 5. Les filles sont resté__ en classe. 6. Il est tombé__ dans la cour.</p>', ["complete"], 2, "C",
          sol="arrivée · partis · nées · mangé (avoir : pas d'accord) · restées · tombé")
    e2 = E("J'écoute le récit de Bilal. Je coche : avoir ou être ? Puis j'écris le verbe.", table(["Verbe entendu", "avoir", "être"], [[blank("l"), '<span class="chk"></span>', '<span class="chk"></span>'] for _ in range(6)], ["120mm", "30mm", "32mm"]), ["ecoute", "coche", "ecris"], 2, "A",
           script="Samedi, je suis allé à Liège avec mon père. Nous avons pris le train à 9 h. Nous sommes arrivés à 10 h. J'ai visité la gare des Guillemins : elle est magnifique ! Ensuite, nous avons mangé des boulets. Le soir, nous sommes rentrés très tard.",
           sol="suis allé (être) · avons pris (avoir) · sommes arrivés (être) · ai visité (avoir) · avons mangé (avoir) · sommes rentrés (être)")
    e3 = E("Je raconte un voyage ou une sortie (6 phrases, au moins 3 verbes avec être).", lines(5), ["ecris"], 3, "C", sol="Production : accords avec être.")
    b.page(f'{e}{e2}{e3}', "S'entraîner")

    # ---------- Leçon 5 : parler de son parcours ----------
    l5 = lecon("Parler de mon parcours (dates et durées)", table(["Pour dire…", "J'utilise…", "Exemple"], [["une date", "en + année · le + date", "Je suis né(e) <b>en</b> 2012. Je suis arrivé(e) <b>le</b> 3 juillet."], ["un moment passé", "il y a + durée", "J'ai commencé le français <b>il y a</b> deux mois."], ["une durée finie", "pendant + durée", "J'ai habité en Turquie <b>pendant</b> trois ans."], ["une action qui continue", "depuis + durée / date (présent !)", "J'habite à Namur <b>depuis</b> un an / <b>depuis</b> juillet."], ["un ordre", "d'abord, ensuite, puis, après, enfin", "<b>D\'abord</b>, je suis allé(e) à l\'école en Guinée. <b>Ensuite</b>…"]], ["38mm", "50mm", "94mm"]) +
               '<div class="astuce">Ton parcours, c\'est ton histoire : tu choisis ce que tu racontes. Tu peux parler seulement de l\'école, des langues ou de tes loisirs. 💬</div>')
    e = E("Je complète avec en, il y a, pendant ou depuis.", '<p>1. Je suis né ___ 2011. 2. J\'apprends le français ___ un an. 3. Nous sommes arrivés ___ six mois. 4. J\'ai étudié l\'anglais ___ deux ans. 5. Elle habite ici ___ septembre. 6. Il a commencé l\'école ___ 2018.</p>', ["complete"], 2, "C",
          sol="en · depuis · il y a · pendant · depuis · en")
    b.page(f'{l5}{e}', "Leçon 5")
    tl = '<svg viewBox="0 0 180 30" width="100%"><line x1="5" y1="15" x2="175" y2="15" stroke="#1F2A44" stroke-width="1.2"/><path d="M175 15 l-4 -3 v6z" fill="#1F2A44"/>' + "".join(f'<circle cx="{x}" cy="15" r="2" fill="#2BA88F"/><text x="{x}" y="9" font-size="4.6" text-anchor="middle" font-family="Poppins" font-weight="700">{a}</text><text x="{x}" y="25" font-size="4" text-anchor="middle" font-family="Poppins">{t}</text>' for x, a, t in [(22, "2012", "naissance · Alep"), (60, "2018", "école en Syrie"), (98, "2022", "Turquie : école turque"), (138, "juillet 2025", "Belgique"), (166, "auj.", "DASPA")]) + '</svg>'
    e = E("Je lis la ligne du temps de Nour. J'écris son parcours en 5 phrases (en, pendant, il y a, depuis).", tl + lines(5), ["lis", "ecris"], 2, "C",
          sol="Nour est née en 2012 à Alep. Elle a commencé l'école en 2018. En 2022, elle est partie en Turquie ; elle est allée à l'école turque pendant trois ans. Elle est arrivée en Belgique en juillet 2025. Elle est au DASPA depuis septembre.")
    e2 = E("Ma ligne du temps scolaire (je choisis 4 étapes) et mes phrases.", '<svg viewBox="0 0 180 14" width="100%"><line x1="5" y1="7" x2="175" y2="7" stroke="#1F2A44" stroke-width="1.2"/><path d="M175 7 l-4 -3 v6z" fill="#1F2A44"/></svg><div class="grid4">' + '<div class="card" style="height:16mm"></div>' * 4 + '</div>' + lines(3), ["dessine", "ecris"], 2, "C", sol="Production personnelle.")
    b.page(f'{e}{e2}', "S'entraîner")

    # ---------- FLESco : ROI ----------
    l6 = lecon("Comprendre un règlement (ROI)", '<p>Le <b>R.O.I.</b> (règlement d\'ordre intérieur) dit les <b>droits</b> et les <b>devoirs</b> des élèves. Il est organisé en <b>articles</b> (Art. 1, Art. 2…).</p>' +
               table(["Je lis…", "Ça veut dire…"], [["L'élève <b>doit</b>… · Il est <b>obligatoire</b> de…", "Je dois le faire ✅"], ["Il est <b>interdit</b> de… · L'élève <b>ne peut pas</b>…", "Je ne peux pas ⛔"], ["L'élève <b>peut</b>… · Il est <b>autorisé</b> à…", "J'ai le droit 👍"], ["<b>Sous peine de</b> sanction · une <b>sanction</b>", "une punition si je ne respecte pas"], ["<b>justifier</b> une absence", "donner un papier qui explique (certificat, mot des parents)"]], ["90mm", "92mm"]))
    roi = '''<div class="doc" style="transform:none;padding:4mm;background:#FBFBF7;border:1px solid #c9ced8;font-family:'DejaVu Serif';font-size:9.5pt;line-height:1.5"><div class="c"><b>Athénée fictif de la Vallée · Règlement d'ordre intérieur (extraits)</b></div>
<p><b>Art. 4 — Horaire.</b> Les cours commencent à 8 h 25. L'élève doit être présent dans la cour à 8 h 20. Après 8 h 35, l'élève en retard passe par l'accueil et fait signer son journal de classe.</p>
<p><b>Art. 7 — Absences.</b> Toute absence doit être justifiée. Pour une absence de 1 à 3 jours, un mot des parents suffit (maximum 8 demi-jours par année). À partir de 4 jours, un certificat médical est obligatoire. Le document est remis à l'éducateur le jour du retour.</p>
<p><b>Art. 9 — GSM.</b> L'usage du GSM est interdit pendant les cours et dans les couloirs. Il est autorisé dans la cour pendant les récréations. En cas de non-respect, le GSM est confisqué jusqu'à la fin de la journée.</p>
<p><b>Art. 12 — Respect.</b> Chacun a le droit d'être respecté, quelles que soient sa langue, son origine ou sa religion. Les insultes et les moqueries sont interdites sous peine de sanction.</p>
<p><b>Art. 15 — Tenue.</b> Une tenue de sport est obligatoire au cours d'éducation physique.</p></div>'''
    b.page(f'<span class="tag-doc">🎒 FRANÇAIS DE L\'ÉCOLE</span>{l6}{roi}', "Consignes & école")
    e = E("Je lis le ROI. Je réponds et je note le numéro de l'article.", f'<p>1. À quelle heure je dois être dans la cour ? {blank()} (Art. ___)</p><p>2. Je suis malade 5 jours. Qu\'est-ce que je dois apporter ? {blank("l")} (Art. ___)</p><p>3. Je peux utiliser mon GSM pendant la récré ? {blank()} (Art. ___)</p><p>4. Qu\'est-ce qui se passe si j\'utilise mon GSM en classe ? {blank("xl")} (Art. ___)</p><p>5. Un élève se moque de l\'accent de Nour. Que dit le ROI ? {blank("xl")} (Art. ___)</p>',
          ["lis", "ecris"], 2, "B", sol="1. à 8 h 20 (Art. 4) — 2. un certificat médical (Art. 7) — 3. Oui, dans la cour (Art. 9) — 4. Il est confisqué jusqu'à la fin de la journée (Art. 9) — 5. Les moqueries sont interdites, sanction (Art. 12)")
    e2 = E("Je classe : obligatoire ✅, interdit ⛔ ou autorisé 👍 ?", table(["Phrase du ROI", "✅", "⛔", "👍"], [[x] + ['<span class="chk"></span>'] * 3 for x in ["justifier une absence", "utiliser le GSM en classe", "utiliser le GSM à la récré", "porter une tenue de sport au cours d'EP", "insulter un camarade"]], ["122mm", "20mm", "20mm", "20mm"]), ["lis", "coche"], 1, "B",
           sol="✅ · ⛔ · 👍 · ✅ · ⛔")
    e3 = E("Défi ! En groupe, nous écrivons 3 articles pour le règlement de NOTRE classe (doit / interdit / peut).", lines(3), ["ecris", "groupe"], 3, "C", sol="Formules du ROI réemployées.")
    b.page(f'{e}{e2}{e3}', "Consignes & école")

    # ---------- Documents de la vie ----------
    mail = '''<div class="doc" style="transform:none;padding:0;background:#fff;border:1px solid #c9ced8;border-radius:2mm;overflow:hidden"><div style="background:#F1F3F6;padding:2mm 4mm;font-size:9.5pt">
<b>De :</b> c.martin@athenee-vallee.be (fictif) · <b>À :</b> parents et élèves du DASPA<br><b>Objet :</b> Bienvenue en septembre ! Informations pratiques</div>
<div style="padding:3mm 4mm;font-size:10pt;line-height:1.55">Chers élèves, chers parents,<br><br>Je suis Mme Martin, coordinatrice du DASPA. Toute l'équipe vous souhaite une très bonne rentrée !<br>
Voici quelques informations importantes :<br>• La rentrée a lieu le lundi 1er septembre à 8 h 25. Rendez-vous au local 12.<br>• Le premier jour, apportez une trousse, un classeur et votre journal de classe (il est donné à l'école).<br>
• Le repas chaud coûte 3,50 €. Vous pouvez aussi apporter vos tartines.<br>• Une réunion pour les parents aura lieu le jeudi 11 septembre à 18 h. Un interprète sera présent (arabe, ukrainien, dari).<br><br>
Pour toute question, vous pouvez m'écrire ou téléphoner au 081 00 00 00 (de 8 h à 16 h).<br><br>Bien cordialement,<br>Claire Martin<br><span class="xs muted">Coordinatrice DASPA · Athénée fictif de la Vallée</span></div></div>'''
    e = E("Je lis le courriel de bienvenue. Je réponds.", f'<p>1. Qui écrit ? Quel est son rôle ? {blank("xl")}</p><p>2. Quel est l\'objet du courriel ? {blank("xl")}</p><p>3. Qu\'est-ce que j\'apporte le premier jour ? {blank("xl")}</p><p>4. Quand est la réunion des parents ? Qui va aider à comprendre ? {blank("xl")}</p><p>5. Je trouve la formule d\'appel (le début) et la formule finale (la fin). {blank("xl")}</p>',
          ["lis", "ecris"], 2, "B", sol="1. Mme Claire Martin, coordinatrice du DASPA — 2. Bienvenue en septembre ! Informations pratiques — 3. une trousse, un classeur, son journal de classe — 4. jeudi 11 septembre à 18 h ; un interprète — 5. « Chers élèves, chers parents » · « Bien cordialement »")
    b.page(f'<span class="tag-doc">📄 DOCUMENT DE LA VIE</span><h2>Un courriel de bienvenue</h2>{mail}<div class="mt4">{e}</div>', "Document de la vie")
    st = table(["Partie du courriel", "Exemple formel (prof, école)", "Exemple familier (ami)"], [["<b>Objet</b>", "Absence de mardi", "Coucou !"], ["<b>Formule d'appel</b>", "Madame, · Bonjour Madame Martin,", "Salut Nour !"], ["<b>Message</b>", "Je vous écris parce que… Pourriez-vous… ?", "Tu sais quoi ? …"], ["<b>Formule finale</b>", "Bien cordialement, · Merci d'avance,", "Bisous · À demain !"], ["<b>Signature</b>", "Prénom NOM, classe DASPA 2", "Daria"]], ["40mm", "76mm", "66mm"])
    e = E("Le courriel : formel ou familier ? Je classe les formules.", st + '<p class="sm mt2">Je souligne en vert les formules pour un adulte de l\'école, en orange celles pour un ami.</p>', ["lis", "souligne"], 1, "B", sol="Formel : colonne 2 · familier : colonne 3. On vouvoie un adulte de l'école.")
    e2 = E("J'écris un courriel à Mme Martin pour me présenter (objet, formule d'appel, 5 phrases, formule finale, signature).", '<div class="card" style="padding:2mm"><p class="sm"><b>Objet :</b> ____________________________</p>' + lines(7) + '</div>', ["ecris"], 2, "C", sol="Structure complète, vouvoiement, présent + passé composé.")
    b.page(f'<span class="tag-doc">📄 DOCUMENT DE LA VIE</span><h2>Écrire un courriel</h2>{e}{e2}', "Document de la vie")
    prof = f'''<div class="doc" style="transform:none;padding:4mm;background:#fff;border:2px solid #2BA88F;border-radius:3mm"><div class="flex top" style="gap:4mm">{avatar("mateo", 70)}<div class="grow"><b style="font-size:14pt">Mateo Rojas</b> <span class="xs muted">· profil d'élève · plateforme de la classe (fictive)</span>
<table class="t" style="margin-top:2mm;font-size:9.5pt"><tr><td style="width:36mm"><b>Âge · classe</b></td><td>15 ans · DASPA 2</td></tr><tr><td><b>Langues</b></td><td>espagnol (maternelle) · français (depuis 2024) · un peu d'anglais</td></tr>
<tr><td><b>Matières préférées</b></td><td>éducation physique, géographie</td></tr><tr><td><b>Je suis…</b></td><td>sociable, sportif, parfois distrait 😅</td></tr><tr><td><b>J'ai déjà…</b></td><td>joué dans un club de foot à Medellín · gagné le tournoi de la MJ</td></tr>
<tr><td><b>Cette année, je veux…</b></td><td>lire un roman en français · réussir mon stage de découverte</td></tr><tr><td><b>Mon conseil aux nouveaux</b></td><td>« N'ayez pas peur de faire des erreurs : tout le monde en fait ! »</td></tr></table></div></div></div>'''
    e = E("Je lis le profil de Mateo. Vrai ou faux ? Je corrige si c'est faux.", vf(["Mateo parle trois langues.", "Mateo est en Belgique depuis l'année passée seulement.", "Il a joué dans un club de foot en Colombie.", "Il veut lire un roman en espagnol."]), ["lis", "coche"], 2, "B",
          sol="Vrai · Faux (le français depuis 2024 : on ne sait pas exactement, mais plus d'un an) · Vrai · Faux (en français)")
    e2 = E("Je remplis mon profil d'élève.", table(["", ""], [["Âge · classe", ""], ["Langues", ""], ["Matières préférées", ""], ["Je suis…", ""], ["J'ai déjà…", ""], ["Cette année, je veux…", ""], ["Mon conseil aux nouveaux", ""]], ["52mm", "130mm"]).replace("<td></td>", '<td style="height:8mm"></td>'), ["ecris"], 2, "C", sol="Production personnelle (présent, passé composé, vouloir + infinitif).")
    b.page(f'<span class="tag-doc">📄 DOCUMENT DE LA VIE</span><h2>Un profil d\'élève</h2>{prof}<div class="mt4">{e}{e2}</div>', "Document de la vie")

    # ---------- Sons : liaison ils ont / ils sont ----------
    e = E("[z] ou [s] ? « ils ont » ou « ils sont » ? J'écoute et je répète.", '<div class="grid2"><div class="card c"><div class="huge">ils‿ont [ilzɔ̃]</div><p>avoir · on entend <b>[z]</b> (liaison)</p><p class="sm">ils‿ont appris · elles‿ont vu · nous‿avons · vous‿avez</p></div><div class="card c"><div class="huge">ils sont [ilsɔ̃]</div><p>être · on entend <b>[s]</b></p><p class="sm">ils sont arrivés · elles sont nées</p></div></div>', ["ecoute", "repete"], 1, "A",
          script="Opposer lentement : ils ont / ils sont ; elles ont / elles sont. Faire mettre la main sur la gorge : [z] vibre, [s] ne vibre pas.", sol="Activité orale.")
    e2 = E("J'écoute et je coche : avoir [z] ou être [s] ?", checks(8, ["ils ont [z]", "ils sont [s]"]), ["ecoute", "coche"], 2, "A",
           script="1. Ils sont partis. — 2. Ils ont mangé. — 3. Elles ont fini. — 4. Elles sont venues. — 5. Ils sont belges. — 6. Ils ont 15 ans. — 7. Elles sont arrivées. — 8. Ils ont compris.",
           sol="1. s — 2. z — 3. z — 4. s — 5. s — 6. z — 7. s — 8. z")
    e3 = E("Les liaisons obligatoires. Je marque la liaison ‿ et je lis à voix haute.", '<div class="card big" style="line-height:2">les élèves · nous avons · vous êtes · mes amis · un enfant · des écoles · ils habitent · trois ans · deux heures · en Italie</div>', ["lis", "parle"], 2, "B",
           sol="les‿élèves · nous‿avons · vous‿êtes · mes‿amis · un‿enfant · des‿écoles · ils‿habitent · trois‿ans · deux‿heures · en‿Italie")
    b.page(f'<h2>J\'écoute bien · Les liaisons</h2>{e}{e2}{e3}', "Sons")
    e = E("🔁 Volume 1 · Le futur proche.", '<p>Cette année, je (lire) ______________ un livre. Nous (faire) ______________ un stage.</p>', ["complete"], 1, "C", sol="vais lire · allons faire")
    e2 = E("🔁 Volume 1 · Les verbes pronominaux.", '<p>Ce matin, je (se lever) ______ à 6 h 30. Demain, nous (se reposer) ______________.</p>', ["complete"], 2, "C", sol="me suis levé(e) (passé composé avec être !) · allons nous reposer")
    e3 = E("🔁 Volume 1 · Poser des questions.", '<p>— ______________ tu es arrivé(e) ? — En juillet. — ______________ langues tu parles ? — Trois.</p>', ["complete"], 1, "C", sol="Quand · Combien de")
    b.page(f'<h2>🔁 Je révise le volume 1</h2>{e}{e2}{e3}', "Je révise")

    # ---------- Ateliers ----------
    e = E("Le speed-dating des présentations : 2 minutes par camarade. Je pose 4 questions, je note les réponses, puis je change de place.", table(["Prénom", "Pays · langues", "Arrivé(e) quand ?", "Une qualité", "Un point commun avec moi"], [["", "", "", "", ""] for _ in range(4)], ["26mm", "40mm", "34mm", "34mm", "48mm"]).replace("<td></td>", '<td style="height:12mm"></td>'), ["parle", "ecris", "groupe"], 1, "A",
          sol="Questions au présent et au passé composé.")
    cards = [("Je suis né(e) dans un autre pays que mes parents.", ""), ("J'ai déjà habité dans 3 pays.", ""), ("Je parle plus de 3 langues.", ""), ("Je suis arrivé(e) en Belgique cette année.", ""), ("J'ai déjà pris l'avion.", ""), ("J'ai appris une langue en moins d'un an.", "")]
    e2 = E("Le bingo « J'ai déjà… » : je trouve un camarade pour chaque case (« Tu as déjà… ? Tu es déjà… ? »).", '<div class="grid3">' + "".join(f'<div class="card" style="min-height:22mm"><p class="sm">{t}</p><div class="line"></div></div>' for t, _ in cards) + '</div>', ["parle", "ecris", "groupe"], 2, "D", sol="Questions au passé composé avec déjà.")
    b.page(f'{atl_head("A", "Atelier · Faire connaissance")}{e}{e2}', "Atelier")
    e = E("Le dé du passé : je lance 2 dés. Dé 1 = le sujet (1 je, 2 tu, 3 elle, 4 nous, 5 vous, 6 ils). Dé 2 = le verbe (1 arriver, 2 apprendre, 3 partir, 4 voir, 5 naître, 6 faire). Je dis la phrase au passé composé. Mon équipe vérifie avec le tableau.", '<div class="c" style="font-size:30pt">🎲🎲</div>' + table(["", "1 arriver", "2 apprendre", "3 partir", "4 voir", "5 naître", "6 faire"], [["auxiliaire", "être", "avoir", "être", "avoir", "être", "avoir"], ["participe", "arrivé", "appris", "parti", "vu", "né", "fait"]], ["26mm"] + ["26mm"] * 6), ["joue", "parle", "groupe"], 2, "D",
          sol="Ex. : 3 + 5 → Elle est née. 6 + 1 → Ils sont arrivés.")
    e2 = E("Je lis le texte de Fatou et je trouve les 5 erreurs de passé composé.", '<div class="card"><p>« Je suis né en 2011 en Guinée. J\'ai allé à l\'école à Conakry pendant cinq ans. Ensuite, ma famille a partie. Nous sommes arrivé en Belgique en 2024. Au début, je n\'ai rien comprendu ! Maintenant, je parle bien français. »</p></div>' + lines(2), ["lis", "barre", "ecris"], 3, "B",
           sol="je suis née · je suis allée · ma famille est partie · nous sommes arrivés · je n'ai rien compris")
    b.page(f'{atl_head("D", "Atelier · Jouer avec le passé")}{e}{e2}', "Atelier")

    # ---------- ★ Coup de pouce ----------
    e = E("Je lis le texte court. Je souligne les verbes.", '<div class="card" style="background:#F2FBF7"><p class="big" style="line-height:1.8">Je m\'appelle Nour. J\'ai 14 ans.<br>Je suis syrienne.<br>Je parle arabe et turc.<br>Je suis arrivée en Belgique en juillet.<br>J\'aime les maths.</p></div>', ["lis", "souligne"], 1, "P", alpha=True,
          sol="m'appelle · ai · suis · parle · suis arrivée · aime")
    e2 = E("Je relie la question et la réponse.", relie(["Tu as quel âge ?", "Tu viens d'où ?", "Tu parles quelles langues ?", "Tu es arrivée quand ?"], ["En juillet.", "J'ai 14 ans.", "Je viens de Syrie.", "Arabe et turc."]), ["lis", "relie"], 1, "B", alpha=True,
           sol="âge → 14 ans · d'où → Syrie · langues → arabe et turc · quand → juillet")
    b.page(CP.format(t="Je lis et je comprends") + e + e2, "★ Coup de pouce")
    e = E("Avoir ou être ? Je regarde la maison d'être et je choisis.", '<div class="grid2">' + "".join(f'<div class="card"><p class="big">{t}</p></div>' for t in ["Je ( ai / suis ) mangé.", "Je ( ai / suis ) arrivé.", "Elle ( a / est ) partie.", "Nous ( avons / sommes ) parlé."]) + '</div>', ["lis", "entoure"], 1, "C", alpha=True,
          sol="ai · suis · est · avons")
    e2 = E("Je complète mon texte avec le modèle de Nour.", '<div class="card" style="background:#F2FBF7"><p class="big" style="line-height:2.2">Je m\'appelle ____________. J\'ai ______ ans.<br>Je suis ____________. Je parle ____________.<br>Je suis arrivé(e) en Belgique en ____________.<br>J\'aime ____________.</p></div>', ["ecris"], 1, "C", alpha=True, sol="Texte personnel sur le modèle.")
    b.page(CP.format(t="J'écris avec un modèle") + e + e2, "★ Coup de pouce")

    # ---------- Tâche finale : portrait de langues ----------
    sil = '''<svg viewBox="0 0 120 170" width="100%" style="max-height:120mm"><g fill="none" stroke="#1F2A44" stroke-width="1.6"><circle cx="60" cy="22" r="15"/><path d="M45 40 Q60 34 75 40 L88 46 L100 90 L90 92 L80 60 L80 108 L74 165 L63 165 L60 115 L57 165 L46 165 L40 108 L40 60 L30 92 L20 90 L32 46 Z"/></g></svg>'''
    e = E("Je colorie ma silhouette des langues : une couleur par langue. Où est la langue dans mon corps ? (dans la tête = je la pense, dans le cœur = je l'aime, dans les mains = je l'écris, dans les pieds = je l'utilise dehors…)", f'<div class="grid2"><div class="card c">{sil}</div><div><b>Ma légende</b>' + "".join(f'<div class="flex mt2"><span style="display:inline-block;width:10mm;height:6mm;border:1px solid #888;border-radius:1mm"></span><span class="line grow"></span></div>' for _ in range(6)) + '</div></div>', ["colorie", "ecris"], 1, "C",
          sol="Silhouette personnelle + légende.")
    b.page(tache_head("Mon portrait de langues", "Je colorie ma silhouette des langues, j'écris mon texte « Moi et mes langues », puis je le présente à la classe (2 minutes).") + e, "Tâche finale", levels=False)
    e = E("J'écris « Moi et mes langues » (10 lignes) : qui je suis, mes langues (où, avec qui, depuis quand), mon parcours scolaire (au passé), mes qualités pour apprendre, mes projets avec le français.", lines(11), ["ecris"], 2, "C", sol="Évaluation avec la grille du livret.")
    b.page(e + table(["Je vérifie :", "✅"], [[x, '<span class="chk"></span>'] for x in ["Je présente mes langues : où, avec qui, depuis quand.", "Je raconte au passé composé (avoir ET être).", "J'accorde les participes avec être.", "J'utilise en, il y a, pendant, depuis.", "Je présente mon portrait à l'oral sans lire tout le texte."]], ["160mm", "22mm"]), "Tâche finale", levels=False)
    e = E("Je révise.", '<p>1. Elle (arriver) ______________ en 2024. 2. Nous (finir) ______ à 15 h 30. (présent) 3. Il est créatif → elle est ______. 4. J\'habite ici ______ deux ans. 5. Je (ne pas comprendre) ______________ la question. 6. Tu ______ (savoir / connaître) Nour ?</p>', ["ecris"], 2, "C",
          sol="est arrivée · finissons · créative · depuis · n'ai pas compris · connais")
    e2 = E("Défi ! Je corrige les 5 erreurs.", '<div class="card big">Mes sœurs sont né en Syrie. J\'ai venu en Belgique il y a un an. J\'habite à Liège pendant six mois. Ma mère est très courageux. Nous avons partis en train.</div>' + lines(2), ["barre", "ecris"], 3, "C",
           sol="sont nées · je suis venu(e) · depuis six mois · courageuse · sommes partis")
    b.page(f'<h2>🔁 Je révise tout le module</h2>{e}{e2}', "Je révise")

    # ---------- Test ----------
    Q = [("Il est syrien. Elle est…", ["syrien", "syriene", "syrienne", "syriennes"]), ("Il est courageux. Elle est…", ["courageux", "courageuse", "courageuxe", "courageuse·s"]), ("Il est gentil. Elle est…", ["gentil", "gentile", "gentille", "gentilles"]),
         ("La langue de l'Ukraine :", ["l'Ukraine", "ukrainienne", "l'ukrainien", "Ukrainien"]), ("Nous ____ à 16 h. (finir)", ["finons", "finissons", "finissez", "finent"]), ("Vous ____ du sport ? (faire)", ["faisez", "faites", "fesez", "font"]),
         ("Je ____ nager.", ["connais", "sais", "suis", "ai"]), ("Je ____ bien Namur.", ["sais", "connais", "vais", "fais"]), ("J'____ appris le turc.", ["ai", "suis", "as", "est"]), ("Elle ____ arrivée en juillet.", ["a", "est", "ai", "es"]),
         ("Mes frères sont ____ en Syrie.", ["né", "née", "nés", "nées"]), ("Nous avons ____ à la cantine.", ["mangé", "mangés", "mangées", "manger"]), ("prendre → participe :", ["prendu", "pris", "prit", "prené"]), ("Négation : J'ai compris. →", ["Je n'ai pas compris.", "Je ai pas compris.", "Je n'ai compris pas.", "Je ne pas ai compris."]),
         ("J'habite ici ____ un an.", ["il y a", "pendant", "depuis", "en"]), ("Je suis arrivé ____ deux mois.", ["depuis", "il y a", "pendant", "en"]), ("Je suis né ____ 2012.", ["en", "il y a", "depuis", "pendant"]),
         ("ROI : « Il est interdit de… » =", ["je dois", "je peux", "je ne peux pas", "c'est conseillé"]), ("Courriel à la coordinatrice, je commence par :", ["Salut !", "Coucou Claire", "Madame,", "Hé !"]), ("« Ils ont » : on entend…", ["[s]", "[z]", "rien", "[t]"])]
    ans = ["syrienne", "courageuse", "gentille", "l'ukrainien", "finissons", "faites", "sais", "connais", "ai", "est", "nés", "mangé", "pris", "Je n'ai pas compris.", "depuis", "il y a", "en", "je ne peux pas", "Madame,", "[z]"]
    key = key_from(Q, ans)
    test_pages(b, 1, "Nouveau départ", Q, f'<h3>B1. Je me présente : nationalité, langues, 2 qualités. (… / 3)</h3>{lines(2, True)}<h3>B2. Je raconte mon arrivée ou un voyage (4 phrases au passé composé, avoir et être). (… / 4)</h3>{lines(3, True)}<h3>B3. J\'écris le début et la fin d\'un courriel à la direction. (… / 3)</h3>{lines(2, True)}',
               [["me présenter en détail (2 minutes)", "/ 4", ""], ["répondre à « Tu es arrivé(e) quand ? Tu parles quelles langues ? »", "/ 3", ""], ["expliquer une règle du ROI", "/ 3", ""]],
               f'<h3>1. Je lis et je réponds. (… / 6)</h3><div class="card big" style="line-height:1.7">Je m\'appelle Ali. J\'ai 15 ans. Je suis afghan. Je parle dari et anglais. Je suis arrivé en Belgique en mars.</div><p>Âge : ______ Nationalité : ______ Langues : ______ Arrivée : ______</p><h3>2. Avoir ou être ? J\'entoure. (… / 4)</h3><div class="card big">J\' ( ai / suis ) mangé. · Elle ( a / est ) partie. · Nous ( avons / sommes ) parlé. · Il ( a / est ) arrivé.</div><h3>3. Je complète ma présentation. (… / 6)</h3><div class="card big" style="line-height:2">Je m\'appelle ______. J\'ai ___ ans. Je suis ______. Je parle ______.</div><h3>4. Je dis mes langues à la prof (oral). (… / 4)</h3><div class="card">☐ je comprends ☐ je réponds ☐ phrase complète ☐ « je suis arrivé(e) »</div>')
    closing(b, 1, ["Je sais dire ma nationalité, mes langues, mes qualités.", "Je sais accorder les nationalités et les qualités au féminin.", "Je sais conjuguer les verbes essentiels au présent.", "Je sais choisir savoir ou connaître.", "Je sais conjuguer au passé composé avec avoir.",
                   "Je sais conjuguer au passé composé avec être (et accorder).", "Je sais utiliser en, il y a, pendant, depuis.", "Je sais lire un ROI (obligatoire, interdit, autorisé).", "Je sais lire et écrire un courriel formel.", "Je fais les liaisons (ils‿ont, nous‿avons).", "Je sais présenter mon portrait de langues."],
            [("🌍", "la nationalité"), ("🗣️", "la langue maternelle"), ("🔍", "curieux · curieuse"), ("🧘", "patient · patiente"), ("📏", "sérieux · sérieuse"), ("🦁", "courageux · courageuse"), ("🙈", "timide"), ("💪", "travailleur · travailleuse"), ("🎨", "créatif · créative"), ("🤝", "sociable"),
             ("👶", "je suis né(e)"), ("🛬", "je suis arrivé(e)"), ("✈️", "je suis parti(e)"), ("📚", "j'ai appris"), ("⏳", "depuis"), ("⏮️", "il y a"), ("📏", "pendant"), ("🧭", "le parcours"), ("📜", "le règlement (ROI)"), ("✅", "obligatoire"), ("⛔", "interdit"),
             ("📧", "le courriel"), ("✉️", "l'objet"), ("🤝", "Bien cordialement")])
    plan_de_travail(b, E, 1, ["Le présent (révision)", "Nationalités et qualités (accord)", "Le passé composé avec avoir", "Le passé composé avec être", "Parler de mon parcours", "Comprendre un ROI"], "☐ Ma silhouette des langues<br>☐ Mon texte « Moi et mes langues »<br>☐ Ma présentation orale")
    if render:
        to_pdf(b.html(), '/home/claude/syllabus/out/V2_M1_eleve.pdf')

    # ---------- Livret enseignant ----------
    pg, exs = helpers(b, E)
    CPp = b.marks["★ Coup de pouce"]
    days = [("1", "Collectif", f"Accueil · Mon livre · ouverture · BD ({pg('Découvrir')})", f"Coup de pouce : texte court (p. {CPp[0]})"), ("2", "Collectif", f"Interview · pays, langues, qualités ({pg('Lexique')})", "Coup de pouce : lexique en images"),
            ("3", "Rotation", f"📌 Leçon 1 présent ({pg('Leçon 1')})", "Coup de pouce : tableau des verbes"), ("4", "Rotation", f"📌 Leçon 2 nationalités, qualités ({pg('Leçon 2')})", "Coup de pouce : masculin / féminin à l'oral"),
            ("5", "Collectif", f"📌 Leçon 3 passé composé avoir ({pg('Leçon 3')})", "Coup de pouce : participes en -é"), ("6", "Rotation", f"📌 Leçon 4 passé composé être ({pg('Leçon 4')}) · liaisons ({pg('Sons')})", f"Coup de pouce : avoir ou être (p. {CPp[1]})"),
            ("7", "Collectif", f"📌 Leçon 5 parcours ({pg('Leçon 5')}) · ROI ({pg('Consignes & école')})", "Coup de pouce : ROI en pictos"), ("8", "Rotation", f"Courriel, profil ({pg('Document de la vie')}) · ateliers ({pg('Atelier')})", "Coup de pouce : texte avec modèle"),
            ("9", "Seul", f"Tâche finale ({pg('Tâche finale')})", "Coup de pouce : silhouette + 5 phrases"), ("10", "Seul", f"Test ({pg('Test')})", f"Coup de pouce : test adapté ({pg('★ Coup de pouce · Test')})")]
    rot = [["🎧 Écouter-Parler", "Speed-dating · Qui est-ce ?", "20 min", "—"], ["📖 Lire", "Interview · profil de Mateo · ROI", "20 min", "Oui"], ["✏️ Écrire", "Courriel · ligne du temps", "20 min", "● oui"],
           ["🧩 Jouer", "Dé du passé · bingo « J'ai déjà… »", "20 min", "Tableau du dé"], ["👩‍🏫 Table d'appui", "Coup de pouce · auxiliaire être", "20 min", "—"]]
    ev1 = '''<h3>Partie B (10 points)</h3><p class="sm"><b>B1</b> : nationalité accordée (1), langues (1), 2 qualités accordées (1) · <b>B2</b> : auxiliaire juste ×4 (2), participes et accords (2) · <b>B3</b> : <span class="sol">Objet + « Madame, / Monsieur, » … « Bien cordialement, Prénom NOM »</span> (3).</p>
<h3>Test ★ Coup de pouce</h3><p class="sm"><b>Ex. 1 :</b> <span class="sol">15 ans · afghan · dari et anglais · en mars</span> · <b>Ex. 2 :</b> <span class="sol">ai · est · avons · est</span> · <b>Ex. 3 :</b> présentation personnelle.</p>'''
    ev2 = f'''<h2>Grille · tâche finale « Mon portrait de langues »</h2>{table(["Critère", "Très bien", "Bien", "À retravailler", "Points"], [["<b>Contenu</b> : langues (où, avec qui, depuis quand), parcours, projets", "Complet", "Partiel", "Pauvre", "/ 5"], ["<b>Passé composé</b> avoir / être, accords", "Juste", "Quelques erreurs", "Beaucoup", "/ 5"], ["<b>Marqueurs</b> en, il y a, pendant, depuis", "3-4 justes", "1-2", "0", "/ 3"], ["<b>Silhouette</b> et légende", "Soignée", "Correcte", "À revoir", "/ 2"], ["<b>Oral</b> : présentation sans lire", "Fluide", "Hésitante", "Lue", "/ 5"]], ["64mm", "32mm", "32mm", "32mm", "22mm"])}
<h2 class="mt4">Différencier et remédier</h2>{table(["Difficulté", "Remédiation"], [["Avoir ou être", "Affiche « maison d'être » ; gestes (monter, descendre…) ; tri d'étiquettes-verbes."], ["Accord du participe avec être", "Code couleur : sujet féminin → e rose, pluriel → s bleu ; dictée de phrases avec Nour / Nour et sa sœur."], ["depuis / il y a / pendant", "Ligne du temps au sol : l'élève se place et dit la phrase."], ["Courriel formel", "Modèle à trous ; relecture en duo avec la grille « objet, appel, message, formule finale »."], ["Élève rapide", "Interview d'un adulte de l'école pour le journal du DASPA (8 questions, texte rédigé)."]], ["50mm", "132mm"])}
<div class="astuce mt4"><b>Le parcours, avec prudence :</b> le « portrait de langues » (biographie langagière) valorise le plurilinguisme sans exiger de raconter l'exil. Ne jamais forcer un récit de migration ; proposer de centrer sur l'école et les langues. Signaler au CPMS toute détresse. Le profil d'élève et la silhouette peuvent rester dans le cahier (pas d'affichage obligatoire).</div>'''
    T = teacher_book(b, E, "V2 · M1", "", MC, 1, "Nouveau départ",
                     "<li><b>Communication :</b> se présenter en détail, parler de ses langues et de son parcours scolaire.</li><li><b>Lexique :</b> pays, nationalités, langues, qualités, matières.</li><li><b>Grammaire :</b> présent (révision, savoir / connaître) ; accord des adjectifs ; passé composé avec avoir et être ; en / il y a / pendant / depuis.</li><li><b>Phonétique :</b> liaisons, ils ont [z] / ils sont [s].</li><li><b>FLSco :</b> comprendre un règlement d'ordre intérieur.</li><li><b>Documents :</b> courriel de bienvenue, profil d'élève, journal de l'école.</li><li><b>★ Coup de pouce :</b> texte court, avoir ou être, écrire avec un modèle.</li>",
                     '<p class="sm"><b style="color:#E4572E">Indispensable</b> : se présenter, passé composé avec avoir et les verbes être les plus fréquents (aller, venir, arriver, partir, naître).</p><p class="sm"><b style="color:#d9a400">Important</b> : accords, depuis / il y a, ROI.</p><p class="sm"><b style="color:#2BA88F">Enrichissement</b> : courriel formel complet, liaisons.</p>',
                     "ROI réel de l'école · affiche « maison d'être » · crayons de couleur (silhouette) · dés · un exemple de courriel de l'école.", "<b>Rentrée et positionnement :</b> ce module sert aussi d'évaluation diagnostique. Les élèves qui arrivent directement en volume 2 (lecteurs-scripteurs) découvrent les codes du cahier p. 2 ; les pages ★ Coup de pouce aident ceux qui sortent du volume 1.",
                     days, "Présentation d'un camarade en 3 phrases · « depuis quand ? » · un verbe de la maison d'être mimé.", rot, key, (ev1, ev2), start=tstart)
    if render:
        to_pdf(T.html(), '/home/claude/syllabus/out/V2_M1_prof.pdf')
    return b, T


if __name__ == "__main__":
    b, T = build_v2m1()
    print(b.n, T.n)
