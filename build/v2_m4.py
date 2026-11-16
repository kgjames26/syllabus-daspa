"""Volume 2 · Module 4 « Émotions et caractère » (A2)."""
import sys
sys.path.insert(0, '/home/claude/syllabus')
from lib.base import *
from lib.art import *
from lib.module import *
from lib.v2 import CP, CPCOL
from lib.render import to_pdf

MC = "#D1495B"
TINT = "#FCE8EB"
EMOS = [("😄", "joyeux / joyeuse"), ("😢", "triste"), ("😠", "fâché(e), en colère"), ("😨", "avoir peur"), ("😲", "surpris(e)"), ("😰", "stressé(e), inquiet / inquiète"),
        ("😞", "déçu(e)"), ("😒", "jaloux / jalouse"), ("😌", "fier / fière"), ("😍", "amoureux / amoureuse"), ("🥱", "s'ennuyer"), ("😮‍💨", "soulagé(e)")]
CARAC = [("gentil", "gentille"), ("généreux", "généreuse"), ("curieux", "curieuse"), ("courageux", "courageuse"), ("sérieux", "sérieuse"), ("nerveux", "nerveuse"),
         ("sportif", "sportive"), ("bavard", "bavarde"), ("patient", "patiente"), ("têtu", "têtue"), ("timide", "timide"), ("drôle", "drôle"), ("calme", "calme"), ("honnête", "honnête")]
REL = [("🤝", "s'entendre bien avec"), ("💬", "se disputer"), ("🕊️", "se réconcilier, faire la paix"), ("😏", "se moquer de"), ("🫂", "consoler"), ("🙏", "pardonner"),
       ("🤞", "avoir confiance en"), ("💌", "être amoureux / amoureuse de"), ("🆘", "aider"), ("👂", "écouter")]


def mood_card(k, m, label):
    return f'<div class="card c" style="padding:2mm">{avatar(k, 64, m)}<div class="sm" style="margin-top:1mm">{label}</div></div>'


def thermo(words, col):
    n = len(words)
    cells = "".join(f'<div style="flex:1;background:{col};opacity:{0.35 + 0.65 * i / max(1, n - 1):.2f};color:#fff;font-weight:700;text-align:center;padding:1.5mm 1mm;font-size:9.5pt;border-radius:1.5mm">{w}</div>' for i, w in enumerate(words))
    return f'<div style="display:flex;gap:1mm;align-items:center"><span class="xs">un peu</span>{cells}<span class="xs">très fort</span></div>'


def build_v2m4(start=1, tstart=1, render=True):
    b = Book("V2 · M4", "Volume 2 · Je me débrouille · Module 4 · Émotions et caractère", MC, start=start)
    E = Ex(b)
    vis = '<div class="flex" style="justify-content:space-around">' + "".join(avatar(k, 82, m) for k, m in [("daria", "triste"), ("mateo", "fache"), ("fatou", "sourire"), ("yonas", "surpris"), ("amina", "rire"), ("bilal", "pense")]) + '</div>'
    opening(b, MC, 4, "Émotions et caractère", vis, [("💗", "dire ce que je ressens et pourquoi"), ("🧑‍🤝‍🧑", "décrire le caractère d'une personne"), ("🫂", "réagir, consoler, encourager, m'excuser"),
            ("🔁", "remplacer un nom par un pronom (le, la, lui, leur…)"), ("⚖️", "choisir entre « c'est » et « il est »"), ("📖", "repérer les sentiments dans un récit")],
            ["Comment tu te sens aujourd'hui ?", "Qu'est-ce qui te rend heureux / heureuse ?", "Un bon ami, c'est quelqu'un comment ?"],
            ["l'émotion", "le sentiment", "le caractère", "content(e)", "triste", "fâché(e)", "avoir peur", "consoler", "s'excuser", "un ami / une amie"], TINT)

    # ---------- Découvrir : BD ----------
    bd = '<div class="grid2" style="gap:3mm">' + "".join([
        bd_case(1, lr("prof", ["Je vous rends les contrôles de maths."], "daria", ["Oh non… 6 sur 20. Je suis tellement déçue !"], "neutre", "triste")),
        bd_case(2, lr("mateo", ["Six ? Ha ha ! Tu es nulle, Daria !"], "daria", ["Arrête ! Ce n'est pas drôle. Tu m'énerves !"], "rire", "fache")),
        bd_case(3, lr("fatou", ["Ne t'inquiète pas, ce n'est qu'un contrôle. Je peux t'aider, si tu veux."], "daria", ["Merci, Fatou. Tu es vraiment gentille."], "sourire", "sourire")),
        bd_case(4, lr("educ", ["Mateo, à ton avis, comment se sent Daria ?"], "mateo", ["Elle est fâchée… et triste. Je lui ai fait de la peine."], "neutre", "pense")),
        bd_case(5, lr("mateo", ["Daria, je suis désolé. C'était méchant. Tu me pardonnes ?"], "daria", ["D'accord… mais ne recommence pas !"], "triste", "sourire")),
        bd_case(6, lr("yonas", ["On fait la paix ? On révise ensemble pour le prochain contrôle ?"], "amina", ["Super idée ! Ensemble, on est plus forts !"], "rire", "rire")),
    ]) + '</div>'
    e = E("J'écoute et je lis la BD : le jour du contrôle.", bd, ["ecoute", "lis"], 1, "A",
          script="Lire deux fois en mettant le ton (déception, colère, douceur, regret). Faire montrer sur les visages : triste, fâchée, gentille, désolé. Demander : « Qui console ? Qui s'excuse ? Qui propose une solution ? »", sol="Activité orale.")
    b.page(f'<h2>Découvrir · Le jour du contrôle</h2>{e}', "Découvrir")
    e = E("Je réponds par une phrase complète.", f'<p>1. Quelle note a Daria ? Comment elle se sent ? {blank("xl")}</p><p>2. Que dit Mateo ? Est-ce gentil ? {blank("xl")}</p><p>3. Qui console Daria ? Que propose-t-elle ? {blank("xl")}</p><p>4. Qui aide Mateo à comprendre ? {blank("xl")}</p><p>5. Que fait Mateo à la fin ? {blank("xl")}</p>',
          ["lis", "ecris"], 1, "B", sol="1. 6 sur 20 ; elle est déçue (triste). — 2. « Tu es nulle ! » ; non, c'est méchant, il se moque. — 3. Fatou ; elle propose de l'aider. — 4. M. Diallo, l'éducateur. — 5. Il s'excuse : « Je suis désolé. Tu me pardonnes ? »")
    rows = [["Daria (case 1)", ""], ["Daria (case 2)", ""], ["Fatou (case 3)", ""], ["Mateo (case 5)", ""], ["Amina (case 6)", ""]]
    e2 = E("Comment se sentent les personnages ? J'écris un mot de l'encadré.", '<p class="sm">déçue · fâchée · gentille, calme · désolé · enthousiaste</p>' + table(["Personnage", "Émotion"], rows, ["60mm", "122mm"]), ["lis", "ecris"], 1, "B",
           sol="déçue · fâchée · gentille, calme · désolé · enthousiaste")
    e3 = E("Et toi ? Tu as déjà vécu une situation comme Daria ou comme Mateo ? Qu'est-ce que tu as fait ? (2 phrases)", lines(2), ["ecris"], 3, "C", sol="Réponse personnelle (passé composé).")
    b.page(f'{e}{e2}{e3}', "Découvrir")
    jour = '''<div class="card" style="background:#FFFBF5;font-family:'DejaVu Serif';line-height:1.6"><p class="sm" style="margin:0 0 1mm"><b>Mardi 14 novembre</b></p>
<p>Cher journal,</p><p>Aujourd'hui, c'était une journée bizarre. Ce matin, j'étais stressée parce qu'on recevait les contrôles de maths. Et j'avais raison : 6 sur 20 ! J'avais envie de pleurer. Puis Mateo s'est moqué de moi devant toute la classe. J'étais furieuse ! J'ai crié « Arrête ! » et mes joues sont devenues toutes rouges.</p>
<p>Heureusement, Fatou est venue près de moi. Elle m'a souri et elle m'a dit : « Je peux t'aider. » Fatou, c'est une fille super : elle est patiente et elle ne juge jamais personne.</p>
<p>À midi, Mateo m'a demandé pardon. Il avait l'air sincère, alors je lui ai pardonné. Au fond, il n'est pas méchant, il est un peu bête quand il veut faire rire les autres.</p>
<p>Ce soir, je me sens mieux. Je suis soulagée et même un peu fière : demain, je commence les révisions avec Fatou et Yonas. Je vais y arriver !</p><p class="r">Daria</p></div>'''
    e = E("Je lis le journal intime de Daria. Je réponds.", jour + f'<p class="mt2">1. Pourquoi Daria était stressée le matin ? {blank("xl")}</p><p>2. Quels signes montrent sa colère ? {blank("xl")}</p><p>3. Comment Daria décrit le caractère de Fatou ? Et de Mateo ? {blank("xl")}</p><p>4. Trouve 4 mots d\'émotion et classe-les : 😀 agréable / 😟 désagréable. {blank("xl")}</p>', ["lis", "ecris"], 2, "B",
          sol="1. On recevait les contrôles de maths. — 2. Elle a crié « Arrête ! », ses joues sont devenues rouges. — 3. Fatou : patiente, elle ne juge personne ; Mateo : pas méchant, un peu bête quand il veut faire rire. — 4. Agréable : soulagée, fière, (je me sens) mieux · Désagréable : stressée, furieuse, envie de pleurer")
    b.page(f'<h2>Découvrir · Le journal de Daria</h2>{e}', "Découvrir")

    # ---------- Lexique ----------
    e = E("Les émotions. J'écoute, je répète et je mime.", '<div class="grid4">' + "".join(f'<div class="card c" style="padding:2mm"><span class="emo s">{em}</span><b class="sm">{t}</b></div>' for em, t in EMOS) + '</div>', ["ecoute", "repete"], 1, "A",
          script="Dire chaque émotion avec le ton et le visage. Puis jeu du miroir : la prof mime, les élèves disent la phrase « Je suis… / J'ai peur ». Faire remarquer : on dit « je suis triste » mais « j'ai peur ».", sol="Activité orale.")
    faces = '<div class="grid6">' + "".join(mood_card(k, m, f"{i}. ……………") for i, (k, m) in enumerate([("yonas", "rire"), ("amina", "triste"), ("bilal", "fache"), ("fatou", "surpris"), ("mateo", "pense"), ("daria", "neutre")], 1)) + '</div>'
    e2 = E("Je regarde les visages. J'écris l'émotion.", faces + '<p class="sm mt2">surpris(e) · fâché(e) · joyeux / joyeuse · triste · inquiet / inquiète (il réfléchit) · calme, neutre</p>', ["regarde", "ecris"], 1, "B",
           sol="1. Yonas est joyeux. — 2. Amina est triste. — 3. Bilal est fâché. — 4. Fatou est surprise. — 5. Mateo est inquiet / il réfléchit. — 6. Daria est calme.")
    b.page(f'<h2>Les mots des émotions</h2>{e}{e2}', "Lexique")
    e = E("J'écoute : quelle émotion ? J'écris le numéro sous l'emoji.", '<div class="grid6">' + "".join(f'<div class="card c"><span class="emo s">{x}</span><div class="line" style="height:7mm"></div></div>' for x in ["😄", "😢", "😠", "😨", "😲", "😮‍💨"]) + '</div>', ["ecoute", "ecris"], 2, "A",
          script="1. « Oh ! Tu es là ? Je ne t'attendais pas ! » (surprise) — 2. « J'ai gagné ! J'ai gagné le concours ! » (joie) — 3. « Ouf… le test est fini, et c'est réussi. » (soulagement) — 4. « Il y a un bruit dans le noir… Qui est là ? » (peur) — 5. « Mon chat est mort ce matin… » (tristesse) — 6. « Ça suffit ! Rends-moi mon GSM ! » (colère)",
          sol="😄 2 · 😢 5 · 😠 6 · 😨 4 · 😲 1 · 😮‍💨 3")
    e2 = E("Je complète avec une émotion.", '<p>1. Mon meilleur ami part au Canada. Je suis ________________ .</p><p>2. Demain, c\'est l\'examen. Je suis ________________ .</p><p>3. Ma petite sœur prend toujours mes affaires ! Je suis ________________ .</p><p>4. J\'ai réussi mon test de natation. Je suis ________________ de moi.</p><p>5. Il n\'y a rien à faire ce dimanche. Je m\'________________ .</p><p>6. On m\'a organisé une fête… je ne savais rien ! Je suis ________________ .</p>', ["complete"], 1, "C",
           sol="1. triste — 2. stressé(e) / inquiet, inquiète — 3. fâché(e) / énervé(e) — 4. fier / fière — 5. m'ennuie — 6. surpris(e)")
    e3 = E("Les familles de mots. Je trouve le nom ou l'adjectif.", table(["Le nom", "L'adjectif"], [["la joie", "joyeux / joyeuse"], ["la tristesse", ""], ["", "fâché(e)"], ["la peur", ""], ["", "surpris(e)"], ["la fierté", ""], ["la jalousie", ""]], ["91mm", "91mm"]).replace("<td></td>", '<td style="height:6.5mm"></td>'), ["ecris"], 3, "C",
           sol="triste · la colère (la fâcherie est rare) · peureux, peureuse (ou effrayé) · la surprise · fier, fière · jaloux, jalouse")
    b.page(f'{e}{e2}{e3}', "Lexique")
    car = table(["Masculin", "Féminin", "Masculin", "Féminin"], [[f"il est <b>{a}</b>", f"elle est <b>{c}</b>", f"il est <b>{x}</b>", f"elle est <b>{y}</b>"] for (a, c), (x, y) in zip(CARAC[:7], CARAC[7:])], ["45mm", "46mm", "45mm", "46mm"])
    e = E("Le caractère. J'écoute et je répète. J'entends la différence masculin / féminin ?", car + '<div class="astuce">-eux → <b>-euse</b> · -if → <b>-ive</b> · -il → <b>-ille</b> · -e → <b>-e</b> (pas de changement : timide, drôle, calme, honnête, sympa)</div>', ["ecoute", "repete"], 1, "A",
          script="Lire chaque paire. Faire lever la main quand on entend une différence (gentil/gentille, généreux/généreuse, sportif/sportive, bavard/bavarde, patient/patiente) et rester immobile quand on n'en entend pas (têtu/têtue, timide, drôle…).", sol="On entend la différence : gentil, généreux, curieux, courageux, sérieux, nerveux, sportif, bavard, patient. On ne l'entend pas : têtu, timide, drôle, calme, honnête.")
    e2 = E("Les contraires. Je relie.", relie(["gentil", "patient", "calme", "généreux", "courageux", "travailleur", "timide"], ["peureux", "égoïste", "sociable, à l'aise", "méchant", "paresseux", "nerveux", "impatient"]), ["relie"], 1, "B",
           sol="gentil ↔ méchant · patient ↔ impatient · calme ↔ nerveux · généreux ↔ égoïste · courageux ↔ peureux · travailleur ↔ paresseux · timide ↔ sociable")
    b.page(f'<h2>Les mots du caractère</h2>{e}{e2}', "Lexique")
    e = E("Qui est-ce ? Je lis la définition et j'écris l'adjectif (masculin ou féminin).", '<p>1. Amina partage toujours son goûter. Elle est ______________ .</p><p>2. Bilal parle, parle, parle… en classe aussi ! Il est ______________ .</p><p>3. Fatou attend calmement, elle explique dix fois. Elle est ______________ .</p><p>4. Yonas pose toujours des questions sur tout. Il est ______________ .</p><p>5. Daria ne change jamais d\'avis, même quand elle a tort ! Elle est ______________ .</p><p>6. Mateo fait rire tout le monde. Il est ______________ .</p>', ["lis", "ecris"], 1, "C",
          sol="1. généreuse — 2. bavard — 3. patiente — 4. curieux — 5. têtue — 6. drôle")
    e2 = E("Les relations. J'écoute et je répète. Puis je complète les phrases.", emogrid(REL, 5) + '<p class="mt2">1. Mateo s\'est ______________ de Daria. 2. Après la dispute, ils se sont ______________ . 3. Quand mon amie pleure, je la ______________ . 4. Je dis mes secrets à Fatou : j\'ai ______________ en elle.</p>', ["ecoute", "complete"], 2, "A",
           script="Lire les dix expressions. Expliquer « se disputer / se réconcilier » avec deux marionnettes ou deux élèves volontaires.", sol="1. moqué — 2. réconciliés — 3. console — 4. confiance")
    b.page(f'<h2>Le caractère · les relations</h2>{e}{e2}', "Lexique")

    # ---------- Belgicismes ----------
    bel = table(["En Belgique, on entend…", "Ça veut dire…", "Exemple"], [["être fâché <b>sur</b> quelqu'un", "être fâché contre quelqu'un", "Elle est fâchée sur son frère."], ["avoir <b>dur</b>", "avoir des difficultés", "J'ai dur avec les maths."], ["être <b>bleu</b> de quelqu'un", "être amoureux / amoureuse", "Il est bleu de sa voisine !"], ["faire <b>de son nez</b>", "faire le malin, se vanter", "Arrête de faire de ton nez !"]], ["54mm", "56mm", "72mm"])
    e = E("Je lis les belgicismes. Je réécris les phrases en français de France (ou standard).", bel + '<p class="mt2">1. Mon ami a dur en néerlandais. → ______________________________</p><p>2. Ma sœur est bleue d\'un garçon de sa classe. → ______________________________</p><p>3. Pourquoi tu es fâché sur moi ? → ______________________________</p>', ["lis", "ecris"], 2, "B",
          sol="1. Mon ami a des difficultés en néerlandais. — 2. Ma sœur est amoureuse d'un garçon de sa classe. — 3. Pourquoi tu es fâché contre moi ?")
    e2 = E("Les expressions imagées. Je relie l'expression et son sens.", relie(["avoir le cafard", "être aux anges", "voir rouge", "avoir le cœur gros", "en avoir marre (familier)", "avoir la trouille (familier)"], ["être très en colère", "avoir peur", "être triste, avoir de la peine", "être très heureux", "être déprimé, avoir des idées noires", "en avoir assez"]) + '<p class="sm mt2">Et dans ta langue ? J\'écris une expression imagée pour une émotion et je la traduis mot à mot : ______________________________________</p>', ["relie", "ecris"], 2, "B",
           sol="cafard → déprimé, idées noires · aux anges → très heureux · voir rouge → très en colère · cœur gros → triste · en avoir marre → en avoir assez · la trouille → avoir peur")
    b.page(f'<h2>🇧🇪 Les mots d\'ici · les belgicismes des émotions</h2><p class="sm">Ces expressions sont très utilisées en Belgique. On les comprend à l\'oral avec les amis, mais à l\'école, dans un texte, on choisit plutôt le français standard.</p>{e}{e2}', "Lexique")

    # ---------- Leçon 1 : exprimer ses sentiments ----------
    l1 = lecon("Dire ce que je ressens", table(["Structure", "Exemples"], [["<b>je suis</b> + adjectif", "Je suis content(e), triste, déçu(e), fâché(e), stressé(e), fier / fière."], ["<b>j'ai</b> + nom", "J'ai <b>peur</b> (du noir). J'ai <b>honte</b>. J'ai <b>le trac</b>. J'ai <b>envie de</b> pleurer / de rire."], ["<b>je me sens</b> + adjectif", "Je me sens seul(e). Je me sens mieux. Je me sens bien ici."], ["<b>ça me</b> + verbe", "Ça m'énerve ! Ça me fait plaisir. Ça me fait peur. Ça me rend triste / heureux."]], ["48mm", "134mm"]) +
               '<p class="mt2"><b>Dire pourquoi :</b> Je suis triste <b>parce que</b> mon ami est parti. · Je suis stressé(e) <b>quand</b> j\'ai un examen. · Je suis content(e) <b>de</b> te voir.</p>'
               '<p><b>Dire l\'intensité :</b> un peu &lt; assez &lt; très &lt; vraiment / tellement → Je suis <b>tellement</b> fier !</p>'
               '<div class="attention" style="margin:1mm 0 0">⚠️ <b>J\'ai peur</b> (pas « je suis peur ») · <b>Je suis</b> content (pas « j\'ai content »).</div>')
    e = E("Je suis ou j'ai ? Je complète.", '<p>1. ______ peur des chiens. 2. ______ très fâché ! 3. ______ honte de ma note. 4. ______ envie de dormir. 5. ______ fière de toi. 6. ______ le trac avant le spectacle.</p>', ["complete"], 1, "C", sol="1. J'ai — 2. Je suis — 3. J'ai — 4. J'ai — 5. Je suis — 6. J'ai")
    b.page(f'{l1}{e}', "Leçon 1")
    e = E("Je dis pourquoi. Je relie et j'écris 4 phrases avec « parce que » ou « quand ».", relie(["Je suis stressé", "Je suis heureuse", "J'ai peur", "Ça m'énerve", "Je me sens seul"], ["… je ne connais personne.", "… il y a un orage.", "… j'ai un contrôle.", "… mon frère prend mon chargeur.", "… je vois ma famille."]) + lines(3), ["relie", "ecris"], 2, "C",
          sol="stressé ← contrôle · heureuse ← famille · peur ← orage · m'énerve ← chargeur · seul ← je ne connais personne (avec parce que / quand)")
    e2 = E("Le thermomètre des émotions. Je classe du plus faible au plus fort.", '<p>1. content · ravi · heureux → ______________________</p><p>2. énervé · furieux · fâché → ______________________</p><p>3. inquiet · terrifié · effrayé → ______________________</p>' + thermo(["content", "heureux", "ravi"], MC), ["lis", "numerote"], 2, "B",
           sol="1. content < heureux < ravi — 2. énervé < fâché < furieux — 3. inquiet < effrayé < terrifié")
    e3 = E("En duo : « Comment tu te sens quand… ? » Je pose 4 questions. Mon voisin répond avec une émotion + parce que / quand.", '<div class="card"><p class="sm">… tu parles devant la classe ? · … tu reçois un message de ta famille ? · … il pleut le week-end ? · … quelqu\'un se moque de toi ? · … tu réussis un exercice difficile ?</p></div>', ["parle", "duo"], 1, "A", sol="Ex. : Je suis stressé(e) quand je parle devant la classe.")
    b.page(f'{e}{e2}{e3}', "S'entraîner")

    # ---------- Leçon 2 : c'est / il est ----------
    l2 = lecon("« C'est » ou « il / elle est » ?", '''<div class="grid2"><div class="card" style="background:#fff"><b>C'EST / CE SONT</b> + 👤 qui ?
<p class="sm">+ un déterminant + nom : <b>C'est</b> <u>un</u> garçon drôle. <b>C'est</b> <u>mon</u> ami. <b>Ce sont</b> <u>mes</u> cousines.<br>+ un nom propre : <b>C'est</b> Fatou.<br>+ un pronom : <b>C'est</b> moi ! <b>C'est</b> lui.<br>+ adjectif pour <b>commenter</b> une situation : <b>C'est</b> super ! <b>C'est</b> triste. <b>C'est</b> difficile.</p></div>
<div class="card" style="background:#fff"><b>IL EST / ELLE EST / ILS SONT</b> + 🖼️ comment ?
<p class="sm">+ un adjectif pour décrire <b>une personne</b> (ou une chose déjà nommée) : <b>Il est</b> gentil. <b>Elle est</b> têtue. <b>Ils sont</b> bavards.<br>+ une profession <b>sans article</b> : <b>Il est</b> éducateur. <b>Elle est</b> infirmière.<br>(mais : <b>C'est un</b> éducateur sympa.)</p></div></div>
<p class="mt2">🔎 <b>Le truc :</b> après le mot, il y a <b>un / une / mon / le…</b> ? → <b>c'est</b>. Il y a <b>seulement un adjectif</b> pour une personne ? → <b>il / elle est</b>.</p>
<p class="sm">Mateo ? <b>C'est</b> un garçon drôle. <b>Il est</b> parfois un peu bête, mais <b>c'est</b> mon copain. Et sa blague ? <b>C'était</b> méchant !</p>''')
    e = E("C'est, ce sont, il est ou elle est ? Je complète.", '<p>1. Regarde la photo : ______ Bilal. ______ très gentil. 2. Mme Lambert ? ______ professeure. ______ une professeure patiente. 3. ______ mes amies du DASPA. 4. Tu as réussi ? ______ génial ! 5. Fatou ? ______ curieuse et ______ une fille courageuse.</p>', ["complete"], 1, "C",
          sol="1. C'est · Il est — 2. Elle est · C'est — 3. Ce sont — 4. C'est — 5. Elle est · c'est")
    e2 = E("J'écoute les 5 devinettes. J'écris le numéro de la devinette sous la bonne personne.", '<div class="grid5">' + "".join(f'<div class="card c" style="padding:1.5mm">{avatar(k, 52, "sourire")}<div class="xs">n° ………</div></div>' for k in ["fatou", "educ", "bilal", "prof", "amina"]) + '</div>', ["ecoute", "ecris"], 2, "A",
           script="1. « C'est un adulte. Il est éducateur. Il est calme et il écoute les élèves. » (M. Diallo) — 2. « C'est une élève. Elle est patiente. Elle porte des couettes. » (Fatou) — 3. « C'est un garçon bavard. Il porte des lunettes. » (Bilal) — 4. « C'est une femme. Elle est professeure de français. Elle porte des lunettes. » (Mme Lambert) — 5. « C'est une fille généreuse. Elle porte un foulard bleu. » (Amina)",
           sol="Fatou → 2 · M. Diallo → 1 · Bilal → 3 · Mme Lambert → 4 · Amina → 5")
    b.page(f'{l2}{e}{e2}', "Leçon 2")
    e = E("J'entoure la bonne forme.", '<div class="card big" style="line-height:1.9">1. (C\'est / Il est) mon frère. (C\'est / Il est) très sportif.<br>2. (C\'est / Elle est) une chanteuse célèbre. (C\'est / Elle est) belge.<br>3. Le film ? (C\'est / Il est) trop long !<br>4. Mon père ? (C\'est / Il est) chauffeur de bus.<br>5. Se moquer des autres, (c\'est / il est) méchant.</div>', ["entoure"], 2, "B",
          sol="1. C'est · Il est — 2. C'est · Elle est — 3. Il est (le film, déjà nommé) — 4. Il est — 5. c'est")
    e2 = E("Le portrait de mon ami(e). J'écris 5 phrases avec c'est / il est / elle est et 3 adjectifs de caractère.", '<div class="card sm" style="background:#FCF7F8">Modèle : Mon meilleur ami, c\'est Yonas. Il est érythréen. C\'est un garçon calme et curieux. Il est très patient avec moi. C\'est super d\'avoir un ami comme lui !</div>' + lines(5), ["ecris"], 2, "C",
           sol="Portrait personnel : c'est + déterminant/nom propre ; il/elle est + adjectif.")
    e3 = E("Défi ! Je corrige les 3 erreurs.", '<div class="card big">Ma tante, elle est une femme formidable. C\'est infirmière à Liège. Elle est drôle et c\'est généreuse.</div>' + lines(1), ["barre", "ecris"], 3, "C",
           sol="c'est une femme formidable · Elle est infirmière · elle est généreuse")
    b.page(f'{e}{e2}{e3}', "S'entraîner")

    # ---------- Leçon 3 : COD ----------
    l3 = lecon("Les pronoms COD : je ne répète pas le nom", '''<p>Le <b>COD</b> (complément d'objet direct) répond à la question <b>qui ?</b> ou <b>quoi ?</b> après le verbe, <b>sans préposition</b>.<br>Tu aides <u>Daria</u> ? → Oui, je <b>l'</b>aide. · Tu connais <u>Mateo</u> ? → Oui, je <b>le</b> connais.</p>
<div class="grid2"><div>''' + table(["Personne", "Pronom COD"], [["moi", "me (m')"], ["toi", "te (t')"], ["lui (masc.)", "<b>le</b> (l')"], ["elle (fém.)", "<b>la</b> (l')"], ["nous / vous", "nous / vous"], ["eux, elles", "<b>les</b>"]], ["40mm", "45mm"]) + '''</div>
<div class="card" style="background:#fff"><b>📍 La place : AVANT le verbe</b><p class="sm">Je <b>la</b> console. · Il <b>m'</b>aide. · Je <b>vous</b> écoute.<br>Négation : Je <b>ne le</b> vois <b>pas</b>.<br>Avec un infinitif : Je vais <b>l'</b>appeler. Je peux <b>t'</b>aider.<br>Au passé composé : Je <b>l'</b>ai vu. (Daria ? Je l'ai vu<b>e</b> → accord, on le voit à l'écrit.)</p></div></div>
<p class="sm">Verbes fréquents avec COD : aimer, aider, consoler, écouter, regarder, inviter, attendre, appeler, connaître, comprendre, croire, remercier, trouver.</p>''')
    e = E("Je souligne le COD et je le remplace par le, la, l' ou les.", '<p>1. Je regarde <i>la photo</i>. → Je ______ regarde.</p><p>2. Fatou console <i>Daria</i>. → Fatou ______ console.</p><p>3. Nous invitons <i>nos amis</i>. → Nous ______ invitons.</p><p>4. Tu écoutes <i>le professeur</i>. → Tu ______ écoutes.</p><p>5. Mateo n\'aime pas <i>les maths</i>. → Mateo ne ______ aime pas.</p>', ["souligne", "complete"], 1, "C",
          sol="1. la — 2. la — 3. les — 4. l' — 5. les")
    b.page(f'{l3}{e}', "Leçon 3")
    e = E("Je réponds avec un pronom COD.", '<p>1. Tu connais Mme Lambert ? — Oui, je ______________________ .</p><p>2. Tu m\'aides ? — Oui, je ______________________ .</p><p>3. Vous nous attendez ? — Oui, nous ______________________ .</p><p>4. Tu as compris la leçon ? — Non, je ______________________ .</p><p>5. Tu vas appeler ta mère ? — Oui, je vais ______________________ .</p><p>6. Tu regardes cette série ? — Non, je ______________________ .</p>', ["ecris"], 2, "C",
          sol="1. la connais — 2. t'aide — 3. vous attendons — 4. ne l'ai pas comprise — 5. l'appeler — 6. ne la regarde pas")
    e2 = E("J'écoute. De quoi ou de qui on parle ? Je coche.", table(["", "le gâteau", "la musique", "les photos", "Yonas"], [[str(i), *(['<span class="chk"></span>'] * 4)] for i in range(1, 6)], ["20mm", "40mm", "40mm", "40mm", "42mm"]), ["ecoute", "coche"], 2, "A",
           script="1. « Je l'adore, ce rythme ! Je l'écoute tous les jours. » — 2. « Je les regarde souvent : on voit toute ma famille. » — 3. « Il est très bon ! Ma grand-mère l'a fait au chocolat. » — 4. « Je le trouve gentil. Je l'aide en maths et il m'aide en anglais. » — 5. « Je les ai imprimées pour l'album de la classe. »",
           sol="1. la musique — 2. les photos — 3. le gâteau — 4. Yonas — 5. les photos")
    e3 = E("Défi ! Je remets les mots dans l'ordre.", '<p>1. pas / la / ne / comprends / je → ______________________</p><p>2. aider / peux / te / je → ______________________</p><p>3. ai / l\' / hier / je / vu → ______________________</p>', ["ecris"], 3, "C", sol="1. Je ne la comprends pas. — 2. Je peux t'aider. — 3. Je l'ai vu hier.")
    b.page(f'{e}{e2}{e3}', "S'entraîner")

    # ---------- Leçon 4 : COI ----------
    l4 = lecon("Les pronoms COI : lui, leur…", '''<p>Le <b>COI</b> (complément d'objet indirect) répond à la question <b>à qui ?</b>. Le verbe se construit avec <b>à</b> + une personne.<br>Je parle <u>à Daria</u>. → Je <b>lui</b> parle. · J'écris <u>à mes parents</u>. → Je <b>leur</b> écris.</p>
<div class="grid2"><div>''' + table(["Personne", "Pronom COI"], [["à moi", "me (m')"], ["à toi", "te (t')"], ["à lui / à elle", "<b>lui</b>"], ["à nous / à vous", "nous / vous"], ["à eux / à elles", "<b>leur</b>"]], ["40mm", "45mm"]) + '''<p class="xs mt2">⚠️ <b>lui</b> = masculin ET féminin. <b>leur</b> ne prend pas de -s ici.</p></div>
<div class="card" style="background:#fff"><b>Verbes avec « à quelqu'un »</b><p class="sm">parler à · dire à · demander à · répondre à · téléphoner à · écrire à · envoyer à · donner à · prêter à · sourire à · expliquer à · faire confiance à · faire de la peine à</p>
<p class="sm"><b>📍 Même place que le COD :</b> Je <b>ne lui</b> parle <b>pas</b>. · Je vais <b>leur</b> téléphoner. · Je <b>lui</b> ai dit la vérité.</p></div></div>
<div class="astuce" style="margin:1mm 0 0">COD ou COI ? Je pose la question : j'aide <b>qui ?</b> → COD (le, la, les) · je parle <b>à qui ?</b> → COI (lui, leur).</div>''')
    e = E("Je remplace les mots soulignés par lui ou leur.", '<p>1. Je téléphone <u>à ma grand-mère</u>. → Je ______ téléphone.</p><p>2. Mateo demande pardon <u>à Daria</u>. → Mateo ______ demande pardon.</p><p>3. La prof explique la leçon <u>aux élèves</u>. → La prof ______ explique la leçon.</p><p>4. Tu souris <u>à ton voisin</u>. → Tu ______ souris.</p>', ["complete"], 1, "C", sol="1. lui — 2. lui — 3. leur — 4. lui")
    b.page(f'{l4}{e}', "Leçon 4")
    e = E("Je réponds avec un pronom COI.", '<p>1. Tu écris à tes cousins ? — Oui, je ______________________ .</p><p>2. Tu as parlé au directeur ? — Non, je ______________________ .</p><p>3. Tu me prêtes ton bic ? — Oui, je ______________________ .</p><p>4. Vous allez répondre à Mme Lambert ? — Oui, nous allons ______________________ .</p><p>5. Tu fais confiance à Fatou ? — Oui, je ______________________ .</p>', ["ecris"], 2, "C",
          sol="1. leur écris — 2. ne lui ai pas parlé — 3. te prête mon bic — 4. lui répondre — 5. lui fais confiance")
    e2 = E("COD ou COI ? Je choisis : le, la, les, lui ou leur.", '<p>1. Daria ? Je ______ console et je ______ donne un mouchoir. 2. Mes parents ? Je ______ aime et je ______ téléphone tous les soirs. 3. Le nouveau ? Je ______ invite à jouer et je ______ montre l\'école. 4. Mes amies ? Je ______ attends et je ______ envoie un message.</p>', ["complete"], 2, "C",
           sol="1. la · lui — 2. les · leur — 3. l' · lui — 4. les · leur")
    e3 = E("Le jeu du « Qui suis-je ? » : je pense à une personne de la classe. Les autres posent des questions avec des pronoms : « Tu lui parles souvent ? Tu l'aides ? Tu le / la trouves drôle ? » Je réponds par oui / non.", '', ["parle", "groupe", "joue"], 2, "A",
           sol="Questions oui/non avec pronoms COD et COI.")
    b.page(f'{e}{e2}{e3}', "S'entraîner")
    e = E("Je transforme : je remplace les mots soulignés par des pronoms (COD ou COI).", '<p>1. Fatou aide <u>Daria</u>. Elle donne un conseil <u>à Daria</u>.<br>→ Fatou ______ aide. Elle ______ donne un conseil.</p><p>2. Mateo fait rire <u>ses copains</u>. Il raconte des blagues <u>à ses copains</u>.<br>→ Mateo ______ fait rire. Il ______ raconte des blagues.</p><p>3. Mme Lambert écoute <u>les élèves</u>. Elle pose des questions <u>aux élèves</u>.<br>→ Mme Lambert ______ écoute. Elle ______ pose des questions.</p>', ["complete"], 2, "C",
          sol="1. l' · lui — 2. les · leur — 3. les · leur")
    e2 = E("Je lis le message de Bilal et je remplace les répétitions par des pronoms. Je recopie.", '<div class="card"><p>Salut Yonas ! J\'ai vu Amina ce matin. J\'ai trouvé Amina un peu triste. J\'ai parlé à Amina et j\'ai demandé à Amina ce qui se passait. Ses parents sont malades. On peut écrire à ses parents une carte ? Je vais acheter la carte demain.</p></div>' + lines(4), ["lis", "recopie"], 3, "C",
           sol="J'ai vu Amina ce matin. Je l'ai trouvée un peu triste. Je lui ai parlé et je lui ai demandé ce qui se passait. … On peut leur écrire une carte ? Je vais l'acheter demain.")
    b.page(f'<h2>S\'entraîner · COD et COI ensemble</h2>{e}{e2}', "S'entraîner")

    # ---------- Leçon 5 : réagir, consoler, s'excuser ----------
    l5 = lecon("Réagir · consoler · encourager · s'excuser", table(["Pour…", "Je dis…", "On me répond…"], [
        ["🫂 <b>consoler</b>", "Ne t'inquiète pas. · Ce n'est pas grave. · Je comprends. · Ça va aller. · Je suis là.", "Merci, c'est gentil."],
        ["💪 <b>encourager</b>", "Courage ! · Tu vas y arriver ! · Tu peux le faire ! · Bravo, continue !", "Merci, j'espère !"],
        ["🙏 <b>s'excuser</b>", "Pardon. · Excuse-moi. · Je suis (vraiment) désolé(e). · Je ne voulais pas te faire de la peine.", "Ce n'est pas grave. · Je te pardonne. · D'accord, mais ne recommence pas."],
        ["🎉 <b>féliciter</b>", "Félicitations ! · Bravo ! · Je suis content(e) pour toi !", "Merci beaucoup !"],
        ["😟 <b>montrer de l'intérêt</b>", "Qu'est-ce qui se passe ? · Tu veux en parler ? · Ça va mieux ?", "Oui, merci. / Non, pas maintenant."],
        ["🛑 <b>dire non calmement</b>", "Arrête, s'il te plaît. · Ça ne me fait pas rire. · Je n'aime pas ça.", ""]], ["40mm", "88mm", "54mm"]) +
        '<div class="astuce">À l\'école, on peut dire à quelqu\'un « Je ne suis pas d\'accord » <b>sans crier</b> : je dis ce que je ressens (« je suis fâché(e) parce que… ») et ce que je veux (« je veux que tu arrêtes »).</div>')
    e = E("Que dis-tu ? Je relie la situation et la réaction.", relie(["Ton amie a perdu son grand-père.", "Ton copain a réussi son examen.", "Tu as cassé le bic de ta voisine.", "Ton ami a peur de parler en classe.", "Quelqu'un se moque de ton accent."], ["Arrête, s'il te plaît. Ça ne me fait pas rire.", "Courage ! Tu vas y arriver !", "Je suis désolé(e), je vais t'en acheter un autre.", "Félicitations ! Je suis content(e) pour toi !", "Je suis vraiment désolé(e). Je suis là si tu veux parler."]), ["lis", "relie"], 1, "B",
          sol="grand-père → Je suis vraiment désolé(e)… · examen → Félicitations ! · bic → Je suis désolé(e), je vais t'en acheter un autre · peur → Courage ! · accent → Arrête, s'il te plaît")
    b.page(f'{l5}{e}', "Leçon 5")
    e = E("J'écoute les 4 dialogues. Qu'est-ce que la personne fait ? Je coche.", checks(4, ["console", "encourage", "s'excuse", "félicite"]), ["ecoute", "coche"], 2, "A",
          script="1. — J'ai raté le bus et je suis arrivé en retard… — Ce n'est pas grave, ça arrive à tout le monde. (console) — 2. — Pardon, Amina, j'ai oublié ton anniversaire. Je suis vraiment désolé. (s'excuse) — 3. — J'ai eu 18 sur 20 en sciences ! — Bravo ! Je suis fière de toi ! (félicite) — 4. — Je dois chanter devant toute l'école demain… — Tu chantes super bien. Tu vas y arriver ! (encourage)",
          sol="1. console — 2. s'excuse — 3. félicite — 4. encourage")
    e2 = E("Je complète les dialogues.", '<p>1. — J\'ai perdu mon chat… — <span class="blank xl"></span></p><p>2. — Oh, pardon, j\'ai renversé ton jus ! — <span class="blank xl"></span></p><p>3. — Demain, j\'ai mon premier jour de stage. J\'ai peur. — <span class="blank xl"></span></p><p>4. — Tu es nul en foot ! Ha ha ! — <span class="blank xl"></span></p>', ["ecris"], 2, "C",
           sol="1. Oh, je suis désolé(e) ! Tu veux en parler ? — 2. Ce n'est pas grave. — 3. Courage, tu vas y arriver ! — 4. Arrête, s'il te plaît, ça ne me fait pas rire.")
    e3 = E("Jeu de rôle en duo. Je tire une carte-situation et je joue la scène (30 secondes) : une personne raconte, l'autre réagit.", '<div class="grid4">' + "".join(f'<div class="card c sm" style="border-style:dashed">{s}</div>' for s in ["Tu as oublié le rendez-vous avec ton ami.", "Ton amie a gagné un concours de dessin.", "Ton copain est nouveau et il est seul.", "Ta voisine a raté son test."]) + '</div>', ["parle", "duo", "joue"], 2, "A", sol="Réactions adaptées : s'excuser · féliciter · inviter / encourager · consoler.")
    e4 = E("Je remets le dialogue dans l'ordre (1 à 5).", '<div class="card">' + "".join(f'<p style="margin:1mm 0"><span class="blank s"></span> {t}</p>' for t in ["— D'accord, je te pardonne. Mais fais attention !", "— Bilal, je peux te parler ? Je suis désolée pour hier.", "— Merci ! Tu veux venir jouer au ping-pong à la récré ?", "— J'ai pris ton cahier sans demander et je l'ai abîmé.", "— Pour hier ? Qu'est-ce qui s'est passé ?"]) + '</div>', ["lis", "numerote"], 2, "B",
           sol="4 · 1 · 5 · 3 · 2")
    b.page(f'{e}{e2}{e3}{e4}', "S'entraîner")

    # ---------- FLSco ----------
    l6 = lecon("Les sentiments dans un récit : dire ou montrer", '''<p>Dans une histoire, l'auteur peut <b>dire</b> l'émotion (<i>Il avait peur.</i>) ou la <b>montrer</b> par le corps, les gestes, la voix (<i>Ses mains tremblaient.</i>). Pour comprendre un récit, je cherche ces <b>indices</b>.</p>'''
               + table(["Indices", "Exemples"], [["🧍 le corps", "il rougit · elle pâlit · ses mains tremblent · son cœur bat fort · il a les larmes aux yeux · elle sourit jusqu'aux oreilles"],
                                                  ["🤲 les gestes", "il serre les poings · elle baisse la tête · il saute de joie · elle se cache le visage · il claque la porte"],
                                                  ["🗣️ les verbes de parole", "murmurer · chuchoter · crier · hurler · soupirer · bégayer · s'exclamer · répondre sèchement"],
                                                  ["✨ les adverbes", "tristement · joyeusement · doucement · nerveusement · fièrement"]], ["40mm", "142mm"]) +
               '<p class="sm mt2"><b>Pour la consigne « Relève les indices qui montrent que… »</b> → je recopie les mots exacts du texte, entre guillemets, et je dis quelle émotion ils montrent.</p>')
    e = E("Quelle émotion ? J'écris l'émotion montrée par chaque phrase.", '<p>1. Yonas serrait les poings et sa voix tremblait de rage. → ______________</p><p>2. Amina a baissé la tête ; une larme a coulé sur sa joue. → ______________</p><p>3. Bilal a sauté de joie et il a embrassé tout le monde. → ______________</p><p>4. Fatou a ouvert grand les yeux : « Quoi ? Ce n\'est pas possible ! » → ______________</p>', ["lis", "ecris"], 1, "B",
          sol="1. la colère — 2. la tristesse — 3. la joie — 4. la surprise")
    b.page(f'<span class="tag-doc">🎒 FRANÇAIS DE L\'ÉCOLE</span>{l6}{e}', "Consignes & école")
    rec = '''<div class="card" style="font-family:'DejaVu Serif';line-height:1.6;background:#FFFBF5"><p><b>Le premier jour</b></p>
<p>Ce matin-là, Samir est arrivé devant la grande grille de l'école. Il a regardé les centaines d'élèves qui riaient et criaient dans la cour. Son cœur battait très fort. Il tenait la sangle de son sac si fort que ses doigts étaient tout blancs.</p>
<p>Une fille s'est approchée. « Tu es nouveau ? » a-t-elle demandé avec un grand sourire. Samir a rougi. « Oui… » a-t-il murmuré. Il ne trouvait plus ses mots.</p>
<p>« Moi, c'est Léa. Viens, je te montre la classe ! » Samir a respiré profondément. Ses épaules se sont relâchées. Pour la première fois depuis une semaine, il a souri.</p></div>'''
    e = E("Je lis le récit. Je relève les indices des émotions de Samir.", rec + table(["Moment", "Indices (mots du texte)", "Émotion"], [["Devant la grille", "", ""], ["Quand Léa lui parle", "", ""], ["À la fin", "", ""]], ["40mm", "100mm", "42mm"]).replace("<td></td>", '<td style="height:10mm"></td>'), ["lis", "souligne", "ecris"], 2, "B",
          sol="Devant la grille : « son cœur battait très fort », « ses doigts étaient tout blancs » → peur, stress · Avec Léa : « a rougi », « a murmuré », « ne trouvait plus ses mots » → timidité, gêne · À la fin : « a respiré profondément », « ses épaules se sont relâchées », « il a souri » → soulagement, joie")
    e2 = E("J'écris : je montre l'émotion sans la dire. Je transforme la phrase avec un indice du corps, un geste ou un verbe de parole.", '<p>1. Daria était fâchée. → ______________________________________</p><p>2. Yonas était très content. → ______________________________________</p><p>3. Amina avait peur. → ______________________________________</p>', ["ecris"], 3, "C",
           sol="Ex. : 1. Daria a serré les poings et elle a crié. — 2. Yonas a sauté de joie. — 3. Les mains d'Amina tremblaient.")
    b.page(f'{e}{e2}', "Consignes & école")

    # ---------- Documents de la vie ----------
    cour = '''<div class="doc" style="transform:none;border:2px solid #1F2A44;overflow:hidden"><div style="background:#1F2A44;color:#fff;padding:2mm 4mm;display:flex;justify-content:space-between;align-items:center"><b style="font-size:15pt;letter-spacing:1px">ADO'MAG</b><span class="xs">n° 112 · novembre · Courrier des lecteurs</span></div>
<div class="grid2" style="padding:3mm 4mm;gap:5mm"><div style="font-size:10.5pt;line-height:1.5"><p><b style="color:''' + MC + '''">« Je me sens invisible »</b></p><p>Bonjour Ado'Mag,<br>J'ai 14 ans et je suis arrivée en Belgique il y a six mois. Je vais dans une école à Namur. Je parle de mieux en mieux français, mais j'ai encore un accent. Deux filles de ma classe se moquent de moi : elles imitent ma voix et elles rient. Je ne leur réponds pas parce que j'ai peur. À la récré, je reste seule et je me sens invisible. Le soir, je suis triste et je n'ai pas envie de retourner à l'école. Mes parents travaillent beaucoup, je ne veux pas les inquiéter. Qu'est-ce que je peux faire ?</p><p class="r"><i>Lina, 14 ans</i></p></div>
<div style="font-size:10.5pt;line-height:1.5;background:#FCE8EB;border-radius:2mm;padding:2.5mm"><p><b>La réponse de Sophie, de la rédaction</b></p><p>Chère Lina,<br>D'abord, bravo : apprendre une nouvelle langue en six mois, c'est un énorme travail ! Ton accent n'est pas un défaut, il raconte ton histoire.<br>Ce que ces filles font, c'est de la moquerie, et ce n'est pas acceptable. Tu n'es pas responsable. <b>Parles-en</b> à un adulte de confiance : un professeur, un éducateur ou le centre PMS de ton école. Tu peux aussi en parler à tes parents : ils préfèrent sûrement le savoir.<br>Pour la récré, cherche un club ou une activité (sport, chorale, bibliothèque) : c'est plus facile de se faire des amis quand on fait quelque chose ensemble. Courage, tu n'es pas seule !</p></div></div></div>'''
    e = E("Je lis la lettre de Lina et la réponse. Je réponds.", f'<p>1. Quel est le problème de Lina ? {blank("xl")}</p><p>2. Relève 3 mots ou expressions qui disent ses émotions. {blank("xl")}</p><p>3. Pourquoi Lina ne parle pas à ses parents ? {blank("xl")}</p><p>4. Quels sont les 3 conseils de Sophie ? {blank("xl")}</p>', ["lis", "ecris"], 2, "B",
          sol="1. Deux filles se moquent de son accent ; elle reste seule à la récré. — 2. j'ai peur · je me sens invisible · je suis triste · je n'ai pas envie (de retourner à l'école) — 3. Ils travaillent beaucoup, elle ne veut pas les inquiéter. — 4. En parler à un adulte de confiance (prof, éducateur, centre PMS) · en parler à ses parents · chercher un club ou une activité.")
    b.page(f'<span class="tag-doc">📄 DOCUMENT DE LA VIE</span><h2>Le courrier des lecteurs d\'un magazine</h2>{cour}<div class="mt4">{e}</div>', "Document de la vie")
    e = E("Vrai ou faux ? Je coche et je justifie avec une phrase du texte.", vf(["Lina est en Belgique depuis un an.", "Lina répond aux filles qui se moquent d'elle.", "Pour Sophie, l'accent de Lina est un défaut.", "Sophie dit que Lina n'est pas responsable."]) + lines(2), ["lis", "coche"], 2, "B",
          sol="Faux (« il y a six mois ») · Faux (« Je ne leur réponds pas ») · Faux (« Ton accent n'est pas un défaut ») · Vrai (« Tu n'es pas responsable »)")
    e2 = E("Je trouve les pronoms dans la lettre de Lina. Ils remplacent qui ?", '<p>1. « Je ne <b>leur</b> réponds pas » → leur = ______________</p><p>2. « je ne veux pas <b>les</b> inquiéter » → les = ______________</p><p>3. « Parles-<b>en</b> » → en = ______________</p>', ["lis", "ecris"], 2, "B",
           sol="1. aux deux filles — 2. ses parents — 3. de ce problème (la moquerie)")
    e3 = E("À mon tour : j'écris une courte réponse à Lina (5 lignes) avec 2 conseils et 1 encouragement.", '<p class="sm">Chère Lina, … Tu peux… · Tu devrais… · N\'oublie pas que… · Courage !</p>' + lines(5), ["ecris"], 3, "C", sol="Réponse personnelle : formule d'appel, 2 conseils, 1 encouragement, signature.")
    b.page(f'{e}{e2}{e3}', "Document de la vie")
    aff = f'''<div class="doc" style="transform:rotate(.4deg);border:3px solid {MC};padding:5mm;background:#fff"><div class="flex" style="justify-content:space-between"><div><div style="font-size:24pt;font-weight:800;color:{MC};line-height:1.05">Tu as besoin<br>de parler ?</div><p class="sm" style="margin-top:2mm">Tu es triste, stressé(e), tu as un problème à l'école ou à la maison, quelqu'un te fait du mal ?<br><b>Tu n'es pas seul(e). Des adultes sont là pour t'écouter.</b></p></div><div>{avatar("educ", 84, "sourire")}</div></div>
<div class="grid3 mt2" style="gap:3mm"><div class="card" style="border-color:{MC}"><b>🏫 À l'école</b><p class="sm">M. Diallo, éducateur<br>bureau 12 (rez-de-chaussée)<br>tous les jours, 8 h – 16 h</p></div>
<div class="card" style="border-color:{MC}"><b>🩺 Le centre PMS</b><p class="sm">psychologue, assistante sociale, infirmière<br>permanence à l'école le <b>mardi</b>, 9 h – 12 h<br>gratuit et confidentiel</p></div>
<div class="card" style="border-color:{MC}"><b>📞 Le 103</b><p class="sm">ligne d'écoute pour les jeunes<br><b>gratuit</b>, tous les jours<br>de 10 h à minuit<br>chat : 103ecoute.be</p></div></div>
<p class="xs mt2 c">🚨 En cas de danger ou d'urgence : <b>112</b> · École secondaire des Trois-Ponts — affiche du conseil des élèves</p></div>'''
    e = E("Je lis l'affiche de l'école. Je réponds.", f'<p>1. À qui s\'adresse cette affiche ? {blank("xl")}</p><p>2. Où se trouve le bureau de M. Diallo ? {blank("l")}</p><p>3. Quand peut-on rencontrer le centre PMS à l\'école ? {blank("l")}</p><p>4. Il est 22 h, tu ne vas pas bien. Qui peux-tu contacter ? Comment ? {blank("xl")}</p><p>5. Quel numéro appeler en cas d\'urgence ? {blank()}</p>', ["lis", "ecris"], 2, "B",
          sol="1. aux élèves qui ont un problème, qui ont besoin de parler — 2. bureau 12, au rez-de-chaussée — 3. le mardi de 9 h à 12 h — 4. le 103 (par téléphone, gratuit, jusqu'à minuit) ou le chat 103ecoute.be — 5. le 112")
    b.page(f'<span class="tag-doc">📄 DOCUMENT DE LA VIE</span><h2>Une affiche de l\'école</h2>{aff}<div class="mt4">{e}</div>', "Document de la vie")
    sms = '<div class="card" style="background:#EEF1F6;max-width:110mm;margin:0 auto">' + "".join(
        f'<div style="display:flex;justify-content:{"flex-end" if me else "flex-start"};margin:1.5mm 0"><div style="background:{"#D1495B" if me else "#fff"};color:{"#fff" if me else "#1F2A44"};border-radius:3mm;padding:1.5mm 3mm;max-width:80mm;font-size:10pt">{t}</div></div>' for me, t in [
            (False, "<b>Mateo</b> · 18:42<br>Daria, tu es là ? 🙁"), (False, "Je voulais encore te dire pardon pour ce matin. C'était vraiment nul de ma part."), (True, "Ok… Ça m'a fait de la peine, tu sais. Tout le monde a ri."),
            (False, "Je sais. J'ai honte. Je ne recommencerai pas, promis 🤝"), (True, "D'accord, je te pardonne. Mais tu dois m'aider en maths alors 😄"), (False, "Deal ! Demain à la récré ? 📐"), (True, "Ça marche ! 👍")]) + '</div>'
    e = E("Je lis la conversation. Je réponds.", sms + f'<p class="mt2">1. Pourquoi Mateo écrit à Daria ? {blank("xl")}</p><p>2. Comment Daria se sentait ce matin ? {blank("l")}</p><p>3. Que promet Mateo ? Que demande Daria ? {blank("xl")}</p><p>4. « Deal », « Ça marche » : c\'est un langage familier ou formel ? {blank()}</p>', ["lis", "ecris"], 1, "B",
          sol="1. pour s'excuser encore — 2. Elle avait de la peine (blessée, triste). — 3. Il promet de ne pas recommencer ; elle demande de l'aide en maths. — 4. familier (entre amis)")
    e2 = E("J'écris un message d'excuse (4 lignes) : j'ai oublié l'anniversaire de mon ami(e).", lines(4), ["ecris"], 2, "C", sol="Ex. : Salut… Je suis vraiment désolé(e), j'ai oublié ton anniversaire ! Je ne voulais pas te faire de la peine. Je t'invite à manger une gaufre mercredi ?")
    b.page(f'<span class="tag-doc">📄 DOCUMENT DE LA VIE</span><h2>Une conversation de messagerie</h2>{e}{e2}', "Document de la vie")

    # ---------- Sons ----------
    e = E("Les sons [ø] et [œ]. J'écoute et je répète.", '<div class="grid2"><div class="card c"><div class="huge">[ø] heureux</div><p>la bouche est presque fermée, ronde 😗<br>heur<b>eux</b> · nerv<b>eux</b> · curi<b>eux</b> · d<b>eux</b> · un p<b>eu</b> · bl<b>eu</b></p></div><div class="card c"><div class="huge">[œ] la peur</div><p>la bouche est plus ouverte 😮<br>la p<b>eu</b>r · le c<b>œu</b>r · ma s<b>œu</b>r · pl<b>eu</b>rer · s<b>eu</b>l · j<b>eu</b>ne</p></div></div>'
          '<div class="astuce">À la fin du mot, on écrit -eu, -eux → souvent [ø]. Devant une consonne prononcée (r, l…) → souvent [œ].</div>', ["ecoute", "repete"], 1, "A",
          script="Faire sentir la différence en tenant la main sous le menton : il descend plus pour [œ]. Paires : deux / deuil… ; heureux / heure ; peu / peur ; nerveux / nerveuse (attention : -euse = [ø] + [z]).", sol="Activité orale.")
    e2 = E("J'écoute : [ø] ou [œ] ? Je coche.", checks(8, ["[ø] heureux", "[œ] peur"]), ["ecoute", "coche"], 2, "A", script="1. curieux — 2. seul — 3. le cœur — 4. un peu — 5. pleurer — 6. nerveux — 7. ma sœur — 8. bleu",
           sol="1. [ø] — 2. [œ] — 3. [œ] — 4. [ø] — 5. [œ] — 6. [ø] — 7. [œ] — 8. [ø]")
    e3 = E("Je lis vite et bien (virelangue).", '<div class="card big c" style="line-height:1.8">Le jeune curieux a peur, il pleure un peu ;<br>sa sœur, heureuse, lui ouvre son cœur.</div>', ["lis", "parle"], 2, "B", sol="Lecture à voix haute.")
    b.page(f'<h2>J\'écoute bien · [ø] et [œ]</h2>{e}{e2}{e3}', "Sons")
    e = E("L'intonation des émotions. J'écoute la même phrase dites de 4 façons. Je relie le numéro et l'émotion.", '<div class="card big c">« Il est parti. »</div>' + relie(["Phrase 1", "Phrase 2", "Phrase 3", "Phrase 4"], ["😢 tristesse (voix basse, lente)", "😲 surprise (la voix monte)", "😄 joie (voix forte, rapide)", "😠 colère (voix forte, sèche)"]), ["ecoute", "relie"], 2, "A",
          script="Dire « Il est parti. » 1. avec joie (soulagement, rapide, sourire) — 2. avec tristesse (lent, voix basse) — 3. avec colère (sec, fort) — 4. avec surprise (montée : « Il est parti ?! »)",
          sol="1 → joie · 2 → tristesse · 3 → colère · 4 → surprise")
    e2 = E("À moi ! Je tire une émotion et je dis la phrase avec le bon ton. La classe devine.", '<div class="grid3">' + "".join(f'<div class="card c big">{p}</div>' for p in ["« C'est l'heure. »", "« Tu as vu ça ? »", "« Il pleut encore. »"]) + '</div><div class="flex mt2" style="justify-content:center;gap:6mm;font-size:22pt">😄 😢 😠 😨 😲 🥱</div>', ["parle", "groupe", "joue"], 1, "A", sol="Activité orale.")
    e3 = E("La ponctuation des émotions. J'ajoute . ! ? ou … puis je lis avec le ton.", '<div class="astuce" style="margin-top:0">! = émotion forte (joie, colère, surprise) · ? = question · … = hésitation, tristesse, suspense</div><div class="card big" style="line-height:1.9">1. Super, on a gagné ___ 2. Tu viens avec moi ___ 3. Je ne sais pas ___ peut-être ___ 4. Arrête tout de suite ___ 5. Il est parti sans dire au revoir ___</div>', ["ecris", "lis"], 2, "C",
           sol="1. ! — 2. ? — 3. … … — 4. ! — 5. … (ou .)")
    b.page(f'<h2>J\'écoute bien · la voix des émotions</h2>{e}{e2}{e3}', "Sons")

    # ---------- Révision spirale ----------
    e = E("🔁 Module 3 · Imparfait ou passé composé ?", '<p>Quand j\'(être) ______ petit, j\'(avoir) ______ peur du noir. Un soir, la lumière (s\'éteindre) ______________ et j\'(crier) ______________ .</p>', ["complete"], 2, "C", sol="étais · avais · s'est éteinte · ai crié")
    e2 = E("🔁 Module 2 · y et en.", '<p>Tu vas au club de théâtre ? — Oui, j\'___ vais le mercredi. · Tu reviens de la piscine ? — Oui, j\'___ reviens.</p>', ["complete"], 1, "C", sol="y · en")
    e3 = E("🔁 Module 1 · Le passé composé avec être.", '<p>Daria (devenir) ______________ toute rouge. Les filles (partir) ______________ en riant.</p>', ["complete"], 2, "C", sol="est devenue · sont parties")
    e4 = E("🔁 Module 1 · Les qualités. Je cite 3 qualités pour me présenter dans un nouveau groupe.", lines(1), ["ecris"], 1, "C", sol="Ex. : Je suis curieux, patient et sportif.")
    e5 = E("🔁 Module 2 · Les prépositions de lieu. Je décris la chambre de Daria.", '<div class="card c" style="font-size:22pt">🛏️ 🪟 🧸 📚 🪴</div><p>Le nounours est ______ le lit. La plante est ______ la fenêtre. Les livres sont ______ l\'étagère.</p>', ["complete"], 1, "C", sol="sur · devant / à côté de · sur / dans")
    e6 = E("🔁 Module 3 · Je raconte un souvenir où j'étais très content(e) ou surpris(e) (3 phrases : décor à l'imparfait, événement au passé composé).", lines(3), ["ecris"], 3, "C", sol="Ex. : J'avais 10 ans. Nous étions chez mes grands-parents. Tout à coup, mon père est arrivé avec un chiot : j'étais tellement surpris !")
    b.page(f'<h2>🔁 Je révise les modules 1 à 3</h2>{e}{e2}{e3}{e4}{e5}{e6}', "Je révise")

    # ---------- Ateliers ----------
    cartes = [("😄", "Je suis tellement content(e) de te voir !"), ("😢", "Mon chien est malade…"), ("😠", "Tu as encore pris mon chargeur !"), ("😨", "Tu as entendu ce bruit ?"), ("😲", "Quoi ? Tu pars demain ?"), ("😰", "Le test commence dans 2 minutes…"), ("😌", "J'ai réussi mon permis vélo !"), ("😞", "Le match est annulé…")]
    e = E("Le théâtre des émotions : en groupe, je découpe les cartes. Je tire une carte, je joue la phrase (voix + visage + gestes). Les autres disent l'émotion et réagissent (consoler, féliciter…).", '<div class="grid4">' + "".join(f'<div class="card c" style="border-style:dashed;min-height:26mm;padding:2mm"><span class="emo s">{em}</span><p class="sm">{t}</p></div>' for em, t in cartes) + '</div>', ["decoupe", "parle", "groupe"], 1, "A",
          sol="Émotion reconnue + réaction adaptée (Courage ! · Bravo ! · Ne t'inquiète pas…).")
    e2 = E("Dialogue à inventer en duo : deux amis se disputent puis se réconcilient (8 répliques). On le joue devant la classe.", table(["Étape", "Réplique"], [["1. Le problème", ""], ["2. La colère", ""], ["3. L'excuse", ""], ["4. La réconciliation", ""]], ["44mm", "138mm"]).replace("<td></td>", '<td style="height:10mm"></td>'), ["ecris", "duo", "parle"], 3, "A",
           sol="Dialogue : émotions exprimées, excuse, pardon.")
    b.page(f'{atl_head("A", "Atelier · Le théâtre des émotions")}{e}{e2}', "Atelier")
    quiz = [("Ton ami a un problème. Tu…", ["l'écoutes pendant une heure.", "lui donnes vite une solution.", "lui proposes d'aller jouer au foot."]),
            ("Un nouvel élève arrive. Tu…", ["lui montres l'école.", "lui expliques les règles du DASPA.", "l'invites à ton match."]),
            ("Tu as un conflit avec un copain. Tu…", ["lui demandes comment il se sent.", "cherches qui a raison.", "oublies vite et tu passes à autre chose."]),
            ("Le week-end, avec tes amis, tu préfères…", ["parler de tout.", "organiser une sortie.", "faire du sport."])]
    qh = "".join(f'<p style="margin-bottom:1mm"><b>{i}. {q}</b><br>' + " &nbsp; ".join(f'<span class="circ" style="width:5.5mm;height:5.5mm;font-size:8pt">{s}</span>{o}' for s, o in zip(["▲", "■", "●"], opts)) + '</p>' for i, (q, opts) in enumerate(quiz, 1))
    res = '<div class="grid3 mt2" style="gap:2mm"><div class="card sm"><b>Une majorité de ▲ : l\'ami confident.</b> Tu es à l\'écoute, patient(e) et doux / douce. On te dit tous les secrets !</div><div class="card sm"><b>Une majorité de ■ : l\'ami organisé.</b> Tu es sérieux / sérieuse et pratique : avec toi, on trouve toujours une solution.</div><div class="card sm"><b>Une majorité de ● : l\'ami énergique.</b> Tu es drôle et sportif / sportive : avec toi, on oublie les soucis !</div></div>'
    e = E("Je lis le test d'un magazine « Quel ami es-tu ? ». J'entoure mes réponses et je lis mon profil. Puis je réponds : je suis d'accord avec mon profil ? Pourquoi ?", f'<div class="card" style="background:#FCF7F8">{qh}{res}</div>' + lines(2), ["lis", "entoure", "ecris"], 2, "B",
          sol="Lecture du profil ; réponse argumentée : « Je suis d'accord parce que… »")
    b.page(f'{atl_head("B", "Atelier · Le test de magazine")}{e}', "Atelier")
    e = E("La boîte à mots gentils : j'écris un message anonyme et gentil à 3 élèves de la classe (une qualité + pourquoi). La prof les distribue vendredi.", '<div class="grid3">' + ('<div class="card" style="border-style:dashed;min-height:46mm"><p class="sm">Pour : ......................</p><p class="xs muted">Tu es … parce que …</p></div>') * 3 + '</div>', ["ecris", "decoupe"], 1, "C",
          sol="Ex. : Pour Yonas : tu es patient parce que tu m'expliques toujours les exercices.")
    e2 = E("J'écris une carte : je félicite ou je console une personne (5 lignes). Je choisis la situation : une naissance, un examen réussi, un déménagement, une maladie.", '<div class="card" style="min-height:50mm;background:#FFFBF5"><p class="sm muted">Cher / Chère ……… ,</p>' + lines(4) + '</div>', ["ecris"], 2, "C", sol="Carte : formule d'appel, émotion, souhait, signature.")
    b.page(f'{atl_head("C", "Atelier · Les mots qui font du bien")}{e}{e2}', "Atelier")
    cases = ["DÉPART", "Dis une chose qui te rend heureux / heureuse.", "Mime « fâché ». Les autres devinent.", "Complète : J'ai peur de…", "Recule de 2 cases 😬", "Fais un compliment à ton voisin.", "c'est ou il est ? « … un ami fidèle. »", "Console : « Je suis tombé. »", "Rejoue !", "Remplace : Je parle à Fatou → je ___ parle.", "Dis 3 adjectifs de caractère au féminin.",
             "Excuse-toi : tu as marché sur son pied.", "Avance de 2 cases 🎉", "Quand es-tu stressé(e) ?", "Dis « heureux » et « peur » 3 fois vite.", "Remplace : J'aide mes amis → je ___ aide.", "Félicite : « J'ai 18/20 ! »", "Contraire de « généreux » ?", "Raconte un moment où tu étais fier / fière.", "ARRIVÉE 🏁"]
    grid = '<div style="display:grid;grid-template-columns:repeat(5,1fr);gap:2mm">' + "".join(f'<div class="card c" style="min-height:27mm;padding:1.5mm;background:{"#FCE8EB" if i % 2 else "#fff"};display:flex;flex-direction:column;justify-content:center"><b style="color:{MC}">{i + 1}</b><span class="xs">{t}</span></div>' for i, t in enumerate(cases)) + '</div>'
    e = E("Le jeu de l'oie des émotions (2 à 4 joueurs, 1 dé, 1 pion chacun). Je lance le dé, j'avance, je fais l'action de la case. Si c'est faux, je recule d'une case.", grid, ["joue", "groupe"], 2, "D",
          sol="Cases 7 : C'est · 10 : lui · 11 : gentille, curieuse, sportive… · 16 : les · 18 : égoïste")
    b.page(f'{atl_head("D", "Atelier · Le jeu de l oie des émotions")}{e}'.replace("jeu de l oie", "jeu de l'oie"), "Atelier")

    # ---------- ★ Coup de pouce ----------
    e = E("Je regarde et je complète : je suis ou j'ai ?", '<div class="grid4">' + "".join(f'<div class="card c" style="padding:2mm"><span class="emo s">{em}</span><p class="big" style="margin:0">{t}</p></div>' for em, t in [("😄", "Je ___ content."), ("😢", "Je ___ triste."), ("😨", "J'___ peur."), ("😠", "Je ___ fâché.")]) + '</div>', ["regarde", "complete"], 1, "C", alpha=True,
          sol="suis · suis · ai · suis")
    e2 = E("Je relie la phrase et le visage.", relie(["J'ai réussi mon test !", "Mon ami est parti.", "Il y a un bruit…", "Arrête !"], ["😨", "😠", "😄", "😢"]), ["relie"], 1, "B", alpha=True, sol="test → 😄 · parti → 😢 · bruit → 😨 · Arrête → 😠")
    e3 = E("Je dis comment je me sens aujourd'hui.", '<div class="card" style="background:#F2FBF7"><p class="big" style="line-height:2.2">Aujourd\'hui, je suis ________________ parce que ________________________ .</p></div>', ["ecris"], 1, "C", alpha=True, sol="Phrase personnelle.")
    b.page(CP.format(t="Les émotions") + e + e2 + e3, "★ Coup de pouce")
    e = E("Masculin → féminin. Je complète.", table(["Il est…", "Elle est…"], [["gentil", "genti____"], ["généreux", "généreu____"], ["sportif", "sporti____"], ["patient", "patient____"], ["timide", "timid____"]], ["91mm", "91mm"]), ["complete"], 1, "C", alpha=True,
          sol="gentille · généreuse · sportive · patiente · timide")
    e2 = E("C'est ou il est ? J'entoure. (Truc : un, une, mon, ma → c'est.)", '<div class="card big" style="line-height:2">(C\'est / Il est) mon ami Yonas.<br>(C\'est / Il est) calme.<br>(C\'est / Elle est) une fille drôle.<br>(C\'est / Elle est) gentille.</div>', ["entoure"], 1, "B", alpha=True, sol="C'est · Il est · C'est · Elle est")
    e3 = E("Je présente un(e) ami(e) avec le modèle.", '<div class="card" style="background:#F2FBF7"><p class="big" style="line-height:2.1">C\'est ______________ (prénom).<br>C\'est un garçon / une fille ______________ .<br>Il / Elle est ______________ et ______________ .</p></div>', ["ecris"], 1, "C", alpha=True, sol="Portrait sur le modèle.")
    b.page(CP.format(t="Le caractère · c'est / il est") + e + e2 + e3, "★ Coup de pouce")
    e = E("Le, la, les ? Je regarde le nom et je complète.", '<div class="card"><p class="big" style="line-height:2">J\'aide <u>Daria</u> (fém.). → Je <b>___</b> aide.<br>Je regarde <u>le film</u> (masc.). → Je <b>___</b> regarde.<br>J\'écoute <u>mes amis</u> (pluriel). → Je <b>___</b> écoute.</p></div>', ["complete"], 1, "C", alpha=True, sol="l' (la) · le · les")
    e2 = E("Lui ou leur ? (1 personne → lui · 2 personnes ou plus → leur)", '<div class="card"><p class="big" style="line-height:2">Je parle <u>à Fatou</u>. → Je ___ parle.<br>Je téléphone <u>à mes parents</u>. → Je ___ téléphone.<br>J\'écris <u>à Bilal</u>. → Je ___ écris.</p></div>', ["complete"], 1, "C", alpha=True, sol="lui · leur · lui")
    e3 = E("Je m'excuse avec le modèle.", '<div class="card" style="background:#F2FBF7"><p class="big" style="line-height:2.1">Pardon, ________ . Je suis désolé(e).<br>J\'ai ________________________ .<br>Je ne voulais pas te faire de la peine.</p></div>', ["ecris"], 1, "C", alpha=True, sol="Excuse sur le modèle.")
    e4 = E("Je console ou je félicite ? Je relie.", relie(["J'ai 18 sur 20 !", "Je suis malade…", "J'ai gagné le match !", "Mon chat est perdu…"], ["Ne t'inquiète pas.", "Bravo !", "Bravo !", "Ne t'inquiète pas."]), ["relie"], 1, "B", alpha=True, sol="18/20 → Bravo ! · malade → Ne t'inquiète pas. · match → Bravo ! · chat → Ne t'inquiète pas.")
    b.page(CP.format(t="Les petits mots le, la, lui…") + e + e2 + e3 + e4, "★ Coup de pouce")

    # ---------- Tâche finale ----------
    let = '''<div class="card" style="background:#FFFBF5;font-family:'DejaVu Serif';line-height:1.55;font-size:10.5pt">
<p class="r">Namur, le 20 novembre</p><p>Cher Samuel,</p>
<p>Comment vas-tu ? Ça fait longtemps ! Ici, tout va mieux. Au début, je me sentais seul et j'étais souvent triste : je ne comprenais rien et il faisait toujours gris. Maintenant, je suis plus calme et je suis content d'aller à l'école.</p>
<p>J'ai un nouvel ami, Bilal. C'est un garçon très drôle. Il est bavard, mais il est aussi généreux : il me prête ses cours et il m'aide en français. Je l'aime bien !</p>
<p>La semaine passée, j'ai vécu un moment fort : j'ai présenté un exposé devant la classe. Mes mains tremblaient, mais à la fin, tout le monde a applaudi. J'étais tellement fier !</p>
<p>Et toi ? Comment ça se passe à l'école ? Tu vois encore nos amis ? Dis-leur bonjour de ma part. Je pense souvent à toi. Courage pour tes examens, tu vas y arriver !</p>
<p>Je t'embrasse,<br>Yonas</p></div>'''
    ann = '<div class="sm">' + "".join(f'<p style="margin-bottom:1.5mm"><span class="pill" style="background:{TINT}">{a}</span> {t}</p>' for a, t in [("1", "lieu, date"), ("2", "formule d'appel : Cher… / Chère…"), ("3", "demander des nouvelles"), ("4", "dire comment je me sens (avant / maintenant)"), ("5", "décrire un ami : c'est / il est + caractère"), ("6", "raconter un moment fort + l'émotion"), ("7", "poser des questions, encourager"), ("8", "formule de fin + signature")]) + '</div>'
    e = E("Je lis la lettre de Yonas. Je retrouve dans la lettre les 8 étapes (j'écris le numéro dans la marge).", f'<div class="grid2" style="grid-template-columns:2fr 1fr">{let}{ann}</div>', ["lis", "numerote"], 1, "B",
          sol="1. Namur, le 20 novembre · 2. Cher Samuel · 3. Comment vas-tu ? · 4. Au début… Maintenant… · 5. J'ai un nouvel ami, Bilal… · 6. La semaine passée… · 7. Et toi ?… Courage… · 8. Je t'embrasse, Yonas")
    b.page(tache_head("Une lettre à un ami", "J'écris une lettre (12 à 15 lignes) à un(e) ami(e) qui habite loin : je dis comment je me sens, je décris une personne et je raconte un moment fort. Je la lis à la classe et je peux l'envoyer.") + e, "Tâche finale", levels=False)
    e = E("Je prépare ma lettre : je remplis le plan.", table(["Étape", "Mes idées"], [["À qui ? (prénom, où il / elle habite)", ""], ["Mes émotions : avant (imparfait) / maintenant (présent)", ""], ["Une personne : c'est… il / elle est… (3 adjectifs) + un pronom (je l'aime bien, je lui parle…)", ""], ["Un moment fort (passé composé) + l'émotion + un indice du corps", ""], ["2 questions + 1 encouragement", ""], ["Formule de fin", ""]], ["74mm", "108mm"]).replace("<td></td>", '<td style="height:19mm"></td>'), ["ecris"], 1, "C",
          sol="Plan complet.")
    b.page(e, "Tâche finale", levels=False)
    e = E("J'écris ma lettre au propre (12 à 15 lignes).", '<p class="r">.................., le ...................</p>' + lines(15), ["ecris"], 2, "C", sol="Évaluation avec la grille du livret.")
    b.page(e + table(["Je vérifie :", "✅"], [[x, '<span class="chk"></span>'] for x in ["J'ai un lieu, une date, « Cher / Chère », une formule de fin.", "J'exprime au moins 3 émotions (je suis, j'ai, je me sens).", "Je décris le caractère d'une personne (c'est / il est).", "J'utilise au moins 2 pronoms (le, la, lui, leur…).", "Je pose des questions et j'encourage mon ami(e)."]], ["160mm", "22mm"]), "Tâche finale", levels=False)
    e = E("Je révise.", '<p>1. féminin de « courageux » : ______ 2. ______ peur des araignées. 3. ______ ma prof. ______ très patiente. 4. Je parle à mes cousins → je ______ parle. 5. Tu aides Amina ? → Oui, je ______ aide. 6. Pour consoler : « Ne ______ pas ! » 7. « avoir dur » (belgicisme) = ______________</p>', ["ecris"], 2, "C",
          sol="1. courageuse — 2. J'ai — 3. C'est · Elle est — 4. leur — 5. l' — 6. t'inquiète — 7. avoir des difficultés")
    e2 = E("Défi ! Je corrige les 6 erreurs.", '<div class="card big">Mon amie Lina, elle est une fille timide. Je suis peur pour elle parce que des filles la moquent. Je leurs parle et je lui console. C\'est généreuse.</div>' + lines(2), ["barre", "ecris"], 3, "C",
           sol="c'est une fille timide · J'ai peur · des filles se moquent d'elle · Je leur parle · je la console · Elle est généreuse")
    e3 = E("Je réagis. J'écris une réponse pour chaque message.", '<p>1. « Ma grand-mère est à l\'hôpital… » → ______________________________</p><p>2. « J\'ai trouvé un stage chez un boulanger ! » → ______________________________</p><p>3. « Tu as pris mon bic sans demander ! » → ______________________________</p><p>4. « Demain, je passe mon entretien… j\'ai le trac. » → ______________________________</p>', ["ecris"], 2, "C",
           sol="1. Oh, je suis désolé(e)… Je suis là si tu veux parler. — 2. Félicitations ! — 3. Pardon, excuse-moi, je te le rends. — 4. Courage, tu vas y arriver !")
    b.page(f'<h2>🔁 Je révise tout le module</h2>{e}{e2}{e3}', "Je révise")

    # ---------- Test ----------
    Q = [("😨 Je ____ peur.", ["suis", "ai", "fais", "me sens"]), ("Féminin de « généreux » :", ["généreuse", "généreuxe", "généreusse", "généreue"]), ("Le contraire de « patient » :", ["calme", "impatient", "timide", "gentil"]),
         ("Il parle tout le temps. Il est…", ["timide", "bavard", "têtu", "paresseux"]), ("Après une dispute, on…", ["se moque", "se réconcilie", "s'ennuie", "se dispute"]), ("Du plus faible au plus fort :", ["fâché, énervé, furieux", "énervé, fâché, furieux", "furieux, fâché, énervé", "fâché, furieux, énervé"]),
         ("____ mon meilleur ami.", ["Il est", "C'est", "Elle est", "Ils sont"]), ("Mon père ? ____ chauffeur.", ["C'est", "Il est", "C'est un", "Il est un"]), ("Fatou ? ____ très patiente.", ["C'est", "Elle est", "Ce sont", "Il est"]),
         ("Tu aides Daria ? — Oui, je ____ aide.", ["lui", "l'", "leur", "les"]), ("Tu parles à Daria ? — Oui, je ____ parle.", ["la", "lui", "leur", "le"]), ("Tu écris à tes parents ? — Oui, je ____ écris.", ["les", "leurs", "leur", "lui"]),
         ("Tu regardes ce film ? — Non, je ____.", ["ne le regarde pas", "ne regarde le pas", "le ne regarde pas", "ne lui regarde pas"]), ("Je peux ____ aider ?", ["te", "t'", "toi", "tu"]),
         ("Pour consoler, je dis :", ["Bravo !", "Ne t'inquiète pas.", "Arrête !", "Félicitations !"]), ("Pour s'excuser, je dis :", ["Je suis désolé(e).", "Courage !", "Ça m'énerve.", "C'est super !"]),
         ("« Ses mains tremblaient. » montre…", ["la joie", "la peur", "l'ennui", "la fierté"]), ("« Il a murmuré » = il a parlé…", ["très fort", "très doucement", "en colère", "en riant"]),
         ("« heureux » : on entend…", ["[œ] comme « peur »", "[ø] comme « deux »", "[ɔ]", "[e]"]), ("🔁 Quand j'____ petit, j'avais peur du noir.", ["ai été", "étais", "suis", "serai"])]
    ans = ["ai", "généreuse", "impatient", "bavard", "se réconcilie", "énervé, fâché, furieux", "C'est", "Il est", "Elle est", "l'", "lui", "leur", "ne le regarde pas", "t'", "Ne t'inquiète pas.", "Je suis désolé(e).", "la peur", "très doucement", "[ø] comme « deux »", "étais"]
    key = key_from(Q, ans)
    test_pages(b, 4, "Émotions et caractère", Q, f'<h3>B1. Je décris le caractère d\'un(e) ami(e) : 3 phrases avec c\'est / il est / elle est. (… / 3)</h3>{lines(2, True)}<h3>B2. Je remplace les mots soulignés par un pronom : J\'invite <u>Amina</u>. Je donne un cadeau <u>à Amina</u>. Je remercie <u>ses parents</u>. (… / 3)</h3>{lines(1, True)}<h3>B3. Ton ami(e) a raté son test. Tu lui écris un message pour le / la consoler et l\'encourager (4 phrases). (… / 4)</h3>{lines(3, True)}',
               [["dire comment je me sens et pourquoi", "/ 3", ""], ["décrire le caractère d'une personne", "/ 3", ""], ["réagir à 2 situations (consoler, s'excuser, féliciter)", "/ 4", ""]],
               f'<h3>1. J\'écris l\'émotion sous chaque visage. (… / 4)</h3><div class="grid4">' + "".join(f'<div class="card c"><span class="emo s">{x}</span><div class="line" style="height:7mm"></div></div>' for x in ["😄", "😢", "😠", "😨"]) + f'</div><h3>2. Je complète : je suis ou j\'ai ? (… / 4)</h3><div class="card big">Je ____ triste. · J\'____ peur. · Je ____ content. · J\'____ honte.</div><h3>3. C\'est ou il est ? J\'entoure. (… / 4)</h3><div class="card big">(C\'est / Il est) mon frère. (C\'est / Il est) gentil.<br>(C\'est / Elle est) ma prof. (C\'est / Elle est) calme.</div><h3>4. Lui ou leur ? (… / 4)</h3><div class="card big">Je parle à Yonas → je ____ parle. · J\'écris à mes amis → je ____ écris.<br>Je téléphone à ma mère → je ____ téléphone. · Je réponds aux profs → je ____ réponds.</div><h3>5. Oral : je console la prof (« Je suis triste… »). (… / 4)</h3>')
    closing(b, 4, ["Je sais nommer 12 émotions.", "Je sais dire ce que je ressens (je suis, j'ai, je me sens) et pourquoi.", "Je sais décrire le caractère (masculin / féminin).", "Je sais choisir entre c'est et il / elle est.", "Je sais utiliser le, la, l', les (COD).", "Je sais utiliser lui et leur (COI).",
                   "Je sais consoler, encourager, féliciter.", "Je sais m'excuser et pardonner.", "Je sais repérer les indices d'une émotion dans un récit.", "Je sais lire un courrier des lecteurs et une affiche.", "Je sais écrire une lettre à un ami."],
            EMOS + [("🧑‍🤝‍🧑", "le caractère"), ("🤗", "gentil / gentille"), ("🎁", "généreux / généreuse"), ("🔍", "curieux / curieuse"), ("🗣️", "bavard / bavarde"), ("🐏", "têtu / têtue"), ("💬", "se disputer"), ("🕊️", "se réconcilier"), ("🫂", "consoler"), ("🙏", "s'excuser, pardonner"), ("💓", "le cœur bat fort"), ("🤫", "murmurer")])
    plan_de_travail(b, E, 4, ["Dire ce que je ressens", "C'est ou il / elle est ?", "Les pronoms COD", "Les pronoms COI", "Réagir, consoler, s'excuser", "Les sentiments dans un récit"], "☐ Le plan de ma lettre<br>☐ Ma lettre au propre<br>☐ Je la lis à la classe")
    if render:
        to_pdf(b.html(), '/home/claude/syllabus/out/V2_M4_eleve.pdf')

    pg, exs = helpers(b, E)
    CPp = b.marks["★ Coup de pouce"]
    days = [("1", "Collectif", f"Ouverture · BD « Le jour du contrôle » ({pg('Découvrir')})", f"CP émotions (p. {CPp[0]})"), ("2", "Collectif", f"Journal de Daria · lexique émotions et caractère ({pg('Lexique')})", "CP je suis / j'ai"),
            ("3", "Rotation", f"📌 Leçon 1 dire ce que je ressens ({pg('Leçon 1')})", "CP météo du jour"), ("4", "Rotation", f"📌 Leçon 2 c'est / il est ({pg('Leçon 2')})", f"CP féminin (p. {CPp[1]})"),
            ("5", "Collectif", f"📌 Leçon 3 COD ({pg('Leçon 3')})", f"CP le, la, les (p. {CPp[2]})"), ("6", "Rotation", f"📌 Leçon 4 COI ({pg('Leçon 4')})", "CP lui / leur"),
            ("7", "Collectif", f"📌 Leçon 5 réagir ({pg('Leçon 5')}) · sons ({pg('Sons')})", "CP s'excuser"), ("8", "Rotation", f"Récit ({pg('Consignes & école')}) · documents ({pg('Document de la vie')}) · ateliers ({pg('Atelier')})", "CP lire l'affiche"),
            ("9", "Seul", f"Tâche finale : la lettre ({pg('Tâche finale')})", "CP lettre courte"), ("10", "Seul", f"Test ({pg('Test')})", f"CP test ({pg('★ Coup de pouce · Test')})")]
    rot = [["🎧 Écouter-Parler", "Théâtre des émotions · dispute", "20 min", "—"], ["📖 Lire", "Ado'Mag · test de magazine", "20 min", "Oui"], ["✏️ Écrire", "Mots gentils · carte", "20 min", "● oui"],
           ["🧩 Jouer", "Jeu de l'oie des émotions", "20 min", "Réponses p. corrigés"], ["👩‍🏫 Table d'appui", "Coup de pouce · pronoms le / la / lui / leur", "20 min", "—"]]
    ev1 = '''<h3>Partie B (10 points)</h3><p class="sm"><b>B1</b> : 1 pt par phrase correcte (c'est + déterminant/nom ; il/elle est + adjectif accordé). · <b>B2</b> : <span class="sol">Je l'invite. Je lui donne un cadeau. Je les remercie.</span> (1 pt chacun) · <b>B3</b> : formule de consolation (1), encouragement (1), au moins une émotion ou un pronom (1), correction de la langue (1).</p>
<h3>Partie C · oral (10 points)</h3><p class="sm">Situations proposées par la prof : « J'ai perdu mon portefeuille. » (consoler) · « Tu as marché sur mon sac ! » (s'excuser) · « J'ai réussi mon CEB ! » (féliciter). Évaluer la pertinence de la réaction et le ton.</p>
<h3>Test ★ Coup de pouce (20 points)</h3><p class="sm"><b>1 :</b> <span class="sol">content / joyeux · triste · fâché · peur</span> · <b>2 :</b> <span class="sol">suis · ai · suis · ai</span> · <b>3 :</b> <span class="sol">C'est · Il est · C'est · Elle est</span> · <b>4 :</b> <span class="sol">lui · leur · lui · leur</span> · <b>5 :</b> une formule de consolation adaptée (4 pts).</p>'''
    ev2 = f'''<h2>Grille · tâche finale « Une lettre à un ami »</h2>{table(["Critère", "Très bien", "Bien", "À retravailler", "Points"], [["<b>Forme de la lettre</b> : lieu, date, formule d'appel, formule de fin", "Complète", "Partielle", "Absente", "/ 3"], ["<b>Émotions</b> : variées, justifiées (parce que, quand)", "≥ 3, justifiées", "2", "1 ou aucune", "/ 4"], ["<b>Portrait</b> : c'est / il est, adjectifs accordés", "Juste", "Quelques erreurs", "Beaucoup", "/ 4"], ["<b>Pronoms</b> COD / COI", "≥ 2 justes", "1", "Aucun", "/ 3"], ["<b>Moment fort</b> au passé (imparfait / PC)", "Juste", "Quelques erreurs", "Beaucoup", "/ 3"], ["<b>Lecture à la classe</b> : ton, prononciation", "Expressive", "Correcte", "Difficile", "/ 3"]], ["66mm", "30mm", "30mm", "34mm", "22mm"])}
<h2 class="mt4">Différencier et remédier</h2>{table(["Difficulté", "Remédiation"], [["« Je suis peur »", "Affiche à deux colonnes JE SUIS + adjectif / J'AI + nom ; on la complète tout le module."], ["Accord des adjectifs", "Familles de terminaisons en couleur (-eux/-euse, -if/-ive) ; dictée muette : la prof dit le masculin, l'élève écrit le féminin."], ["C'est / il est", "Le « truc du déterminant » : je cherche un, une, mon… après. Jeu de tri avec étiquettes."], ["COD / COI", "Poser la question « qui ? » ou « à qui ? » ; flèches dessinées du pronom vers le nom qu'il remplace ; manipulations avec des cartes-mots."], ["Élève rapide", "Réécrire la BD sous forme de récit en montrant les émotions ; répondre à une autre lettre du courrier des lecteurs."]], ["44mm", "138mm"])}'''
    bien = f'''<h2>Émotions en classe : précautions et ressources</h2>
<div class="attention"><b>Un thème sensible.</b> Pour des élèves primo-arrivants, parler d'émotions peut réveiller des vécus lourds (exil, deuil, séparation, harcèlement). Toujours laisser la possibilité de parler d'un personnage, d'une situation inventée ou de « quelqu'un que je connais ». Ne jamais obliger à se livrer devant le groupe.</div>
<h3>Rituel conseillé : la météo des émotions</h3><p class="sm">Chaque matin, chaque élève place son prénom (pince à linge) sur un emoji ou dit « Aujourd'hui, je suis… parce que… ». La prof note discrètement les élèves qui restent plusieurs jours sur une émotion difficile.</p>
<h3>Si un élève se confie</h3><p class="sm">Écouter sans juger, remercier pour la confiance, ne pas promettre le secret absolu, puis relayer vers l'éducateur, la direction ou le centre PMS selon les procédures de l'école. En cas de danger : 112.</p>
<h3>Ressources réelles mentionnées dans le cahier</h3>{table(["Ressource", "Ce qu'il faut savoir"], [["Centre PMS", "Chaque école de la Fédération Wallonie-Bruxelles est liée à un centre psycho-médico-social : service gratuit (psychologues, assistants sociaux, infirmiers)."], ["Le 103", "Ligne d'écoute gratuite pour les jeunes (et les parents), financée par la Fédération Wallonie-Bruxelles ; tous les jours de 10 h à minuit ; chat sur le site 103ecoute.be (vérifier les horaires à jour avant d'afficher)."], ["112", "Numéro d'urgence européen (police, pompiers, ambulance)."]], ["36mm", "146mm"])}
<h3>Belgicismes du module</h3><p class="sm">fâché <b>sur</b> (= contre) · avoir <b>dur</b> (= avoir des difficultés) · être <b>bleu de</b> (= amoureux) · faire <b>de son nez</b> (= se vanter). À accueillir à l'oral, à « traduire » à l'écrit scolaire.</p>
<h3>Point de langue pour l'enseignant</h3><p class="sm">L'accord du participe passé avec le COD placé avant (« je l'ai vue ») est seulement signalé au niveau A2 ; il sera systématisé au volume 3. « Se moquer de » se pronominalise avec « de » (pas COD) : on ne dit pas « elles la moquent ».</p>'''
    T = teacher_book(b, E, "V2 · M4", "", MC, 4, "Émotions et caractère",
                     "<li><b>Communication :</b> exprimer ses sentiments, réagir, consoler, encourager, s'excuser.</li><li><b>Lexique :</b> émotions (et leur intensité), caractère (masculin / féminin, contraires), relations ; belgicismes.</li><li><b>Grammaire :</b> pronoms COD (me, te, le, la, les…) et COI (lui, leur…) ; c'est / il est.</li><li><b>Phonétique :</b> [ø] / [œ] ; l'intonation expressive.</li><li><b>FLSco :</b> le vocabulaire des sentiments dans un récit (dire / montrer, indices).</li><li><b>Documents :</b> courrier des lecteurs, affiche d'aide, conversation de messagerie, test de magazine.</li><li><b>★ Coup de pouce :</b> je suis / j'ai, féminin, c'est / il est, le / la / lui / leur guidés.</li>",
                     '<p class="sm"><b style="color:#E4572E">Indispensable</b> : 12 émotions, je suis / j\'ai / je me sens, consoler et s\'excuser.</p><p class="sm"><b style="color:#d9a400">Important</b> : caractère accordé, c\'est / il est, le / la / les, lui / leur.</p><p class="sm"><b style="color:#2BA88F">Enrichissement</b> : indices dans un récit, intensité, pronoms au passé composé.</p>',
                     "Cartes-émotions (emojis agrandis) · pinces à linge pour la météo des émotions · dés et pions (jeu de l'oie) · boîte pour les mots gentils · enveloppes et timbres si les lettres sont envoyées.", "<b>Climat de classe :</b> ce module est l'occasion d'installer des règles de respect (« on ne se moque pas », « je dis ce que je ressens sans crier »). Lire la page « Émotions en classe » du livret avant de commencer.",
                     days, "Météo des émotions (« Aujourd'hui, je suis… parce que… ») · un adjectif de caractère du jour (masc. / fém.) · un compliment à un camarade.", rot, key, (ev1, ev2), extra_pages=[(bien, "Bien-être")], start=tstart)
    if render:
        to_pdf(T.html(), '/home/claude/syllabus/out/V2_M4_prof.pdf')
    return b, T


if __name__ == "__main__":
    b, T = build_v2m4()
    print(b.n, T.n)
