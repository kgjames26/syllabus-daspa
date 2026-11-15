"""Volume 1 · Module 8 « Vêtements et météo »."""
import sys
sys.path.insert(0, '/home/claude/syllabus')
from lib.base import *
from lib.art import *
from lib.alpha import AL, letter_page, syll_table
from lib.module import *
from lib.render import to_pdf

MC = "#3A86C8"
VET = [("👕", "le t-shirt"), ("👚", "le pull"), ("🧥", "le manteau"), ("🧥", "la veste"), ("👖", "le pantalon"), ("🩳", "le short"),
       ("👗", "la robe"), ("👔", "la chemise"), ("🧣", "l'écharpe"), ("🧤", "les gants"), ("🧢", "la casquette"), ("👒", "le chapeau"),
       ("🧦", "les chaussettes"), ("👟", "les baskets"), ("👢", "les bottes"), ("🩴", "les sandales"), ("🥾", "les chaussures"), ("🎒", "le sac"),
       ("☂️", "le parapluie"), ("🕶️", "les lunettes de soleil"), ("🩱", "le maillot"), ("🧕", "le foulard"), ("🎽", "le training"), ("🪖", "le bonnet")]
VET[23] = ("🧶", "le bonnet")
COUL = [("#E53935", "rouge"), ("#1E88E5", "bleu"), ("#43A047", "vert"), ("#FDD835", "jaune"), ("#111111", "noir"), ("#FFFFFF", "blanc"),
        ("#9E9E9E", "gris"), ("#FB8C00", "orange"), ("#8D6E63", "brun"), ("#EC407A", "rose"), ("#8E24AA", "violet"), ("#81D4FA", "bleu clair")]
METEO = [("☀️", "Il fait beau. Il y a du soleil."), ("🌤️", "Il y a des éclaircies."), ("☁️", "Il y a des nuages. C'est gris."), ("🌧️", "Il pleut."),
         ("⛈️", "Il y a de l'orage."), ("❄️", "Il neige."), ("🌬️", "Il y a du vent."), ("🌫️", "Il y a du brouillard."),
         ("🥵", "Il fait chaud."), ("🥶", "Il fait froid."), ("🧊", "Il gèle."), ("🌡️", "Il fait 12 degrés.")]


def swatch(col, w="10mm"):
    return f'<span style="display:inline-block;width:{w};height:6mm;border-radius:1.2mm;background:{col};border:1px solid #888;vertical-align:middle"></span>'


def belgique(data):
    """Carte schématique de la Belgique avec météo par ville. data : {ville: (emoji, temp)}."""
    pos = {"Ostende": (32, 34), "Bruges": (48, 36), "Anvers": (92, 30), "Bruxelles": (88, 58), "Mons": (60, 88), "Charleroi": (88, 92),
           "Namur": (110, 86), "Liège": (142, 72), "Arlon": (150, 138)}
    poly = "8,44 28,26 52,22 70,14 88,10 106,16 122,12 140,26 150,40 168,50 176,66 166,84 172,104 164,124 160,146 144,150 132,134 118,124 104,108 84,104 64,98 46,88 28,72 14,60"
    pts = ""
    for v, (x, y) in pos.items():
        if v in data:
            em, t = data[v]
            pts += (f'<circle cx="{x}" cy="{y}" r="1.6" fill="#1F2A44"/><text x="{x}" y="{y - 4}" font-size="10" text-anchor="middle">{em}</text>'
                    f'<text x="{x}" y="{y + 7}" font-size="5" text-anchor="middle" font-family="Poppins" font-weight="700" fill="#1F2A44">{v}</text>'
                    f'<text x="{x + 9}" y="{y - 4}" font-size="5.5" font-family="Poppins" font-weight="800" fill="#E53935">{t}°</text>')
    return (f'<svg viewBox="0 0 190 160" width="100%" style="max-height:110mm"><polygon points="{poly}" fill="#E8F3E1" stroke="#5B7F4A" stroke-width="1.2"/>'
            f'<path d="M8 44 L0 36" stroke="#5B7F4A"/><text x="4" y="20" font-size="5" fill="#3A86C8" font-family="Poppins" font-style="italic">mer du Nord</text>{pts}</svg>')


def build_m8(start=1, tstart=1, render=True):
    b = Book("V1 · M8", "Volume 1 · Premiers pas · Module 8 · Vêtements et météo", MC, start=start)
    E = Ex(b)
    vis = '<div class="c" style="font-size:40pt;line-height:1.3">☀️🌧️❄️🌬️🌡️<br>🧥🧣👕👖👢</div>'
    opening(b, MC, 8, "Vêtements et météo", vis, [("👕", "nommer les vêtements"), ("🎨", "dire les couleurs et les accorder"), ("🌦️", "dire le temps qu'il fait"),
            ("🌡️", "lire une température, une carte météo"), ("🍂", "nommer les saisons et les mois"), ("💬", "conseiller une tenue : mets ton manteau !")],
            ["Quel temps fait-il aujourd'hui ?", "Dans ton pays, il fait chaud ? Il neige ?", "Qu'est-ce que tu portes aujourd'hui ?"],
            ["il fait beau", "il pleut", "il fait froid", "le manteau", "le pull", "la couleur", "la saison", "mettre", "porter", "les degrés"], "#E4F0FA")

    # ---------- Découvrir ----------
    bd = '<div class="grid2" style="gap:3mm">' + "".join([
        bd_case(1, lr("yonas", ["Brrr ! Il fait froid ! Il pleut encore !"], "mateo", ["Yonas ! Tu es en t-shirt ? On est en novembre !"], "triste", "surpris", '<div class="c" style="font-size:22pt">🌧️🌬️</div>')),
        bd_case(2, lr("yonas", ["En Érythrée, il fait chaud toute l'année. Je n'ai pas de manteau."], "fatou", ["Moi non plus, la première année ! J'avais très froid."], "pense")),
        bd_case(3, lr("prof", ["En Belgique, en hiver, il faut un manteau, une écharpe et des gants."], extra='<div class="c" style="font-size:26pt">🧥🧣🧤🧶</div>')),
        bd_case(4, lr("daria", ["Samedi, il y a une bourse aux vêtements à l'école. C'est pas cher !"], "yonas", ["Super ! Je cherche un manteau bleu ou noir."], "sourire", "rire")),
        bd_case(5, lr("amina", ["Regarde ! Une veste noire et un bonnet rouge. Ça coûte 5 euros."], "yonas", ["J'adore ! Je mets la veste… Elle est trop grande ?"], "rire", "pense")),
        bd_case(6, lr("mateo", ["Non, elle est parfaite ! Maintenant, tu peux sortir sous la pluie !"], "yonas", ["Merci ! Vive la drache belge !"], "rire", "rire", '<div class="c" style="font-size:22pt">☂️😄</div>')),
    ]) + '</div>'
    e = E("J'écoute et je regarde la BD : il fait froid !", bd, ["ecoute", "regarde"], 1, "A",
          script="Lire deux fois. Mimer « brrr » (froid) et « pff » (chaud). Montrer par la fenêtre : « Quel temps fait-il ? ». Faire répéter : « Il fait froid », « Il pleut », « Je mets ma veste ».", sol="Activité orale.")
    b.page(f'<h2>Découvrir · Il fait froid !</h2>{e}', "Découvrir")
    e = E("Je réponds.", f'<p>1. Quel temps fait-il ? {blank("l")}</p><p>2. Yonas porte quel vêtement ? {blank()}</p><p>3. En hiver, en Belgique, il faut… {blank("xl")}</p><p>4. Yonas achète quoi ? De quelle couleur ? {blank("xl")}</p><p>5. Ça coûte combien ? {blank()}</p>',
          ["lis", "ecris"], 1, "B", sol="1. Il fait froid, il pleut. — 2. un t-shirt — 3. un manteau, une écharpe et des gants — 4. une veste noire et un bonnet rouge — 5. 5 euros")
    e2 = E("Vrai ou faux ?", vf(["En Érythrée, il fait froid en hiver.", "Yonas n'a pas de manteau.", "La bourse aux vêtements est samedi.", "La veste est trop grande."]), ["lis", "coche"], 2, "B",
           sol="Faux (il fait chaud toute l'année) · Vrai · Vrai · Faux (elle est parfaite)")
    e3 = E("Défi ! Le temps dans mon pays : je dis 3 phrases à mon voisin.", lines(3), ["parle", "ecris"], 3, "C", sol="Production libre : Dans mon pays, il fait… En été… En hiver…")
    b.page(f'{e}{e2}{e3}<div class="astuce">🇧🇪 En Belgique, on dit « <b>il drache</b> » quand il pleut très fort : c\'est une <b>drache</b> ! Une <b>bourse aux vêtements</b> = on vend et on achète des vêtements de seconde main, pas cher.</div>', "Découvrir")

    # ---------- Lexique ----------
    e = E("Les vêtements. J'écoute et je répète.", emogrid(VET, 6), ["ecoute", "repete"], 1, "A",
          script="Montrer chaque image (ou un vrai vêtement de la caisse), dire le mot avec l'article, faire répéter. Jeu « Jacques a dit : touche ton pantalon ! ».", sol="Activité orale.")
    b.page(f'<h2>Les vêtements</h2>{e}', "Lexique")
    e = E("Je classe : on porte ça quand ?", table(["☀️ Quand il fait chaud", "🥶 Quand il fait froid", "🌧️ Quand il pleut", "☀️🥶🌧️ Toujours"], [["", "", "", ""]], ["45mm", "45mm", "45mm", "47mm"]).replace("<td></td>", '<td style="height:32mm"></td>') +
          '<p class="sm mt2">le short · les gants · le parapluie · les sandales · l\'écharpe · les bottes · le maillot · le bonnet · le manteau · les lunettes de soleil · les chaussettes · le pantalon</p>',
          ["ecris"], 1, "C", sol="Chaud : short, sandales, maillot, lunettes de soleil · Froid : gants, écharpe, bonnet, manteau · Pluie : parapluie, bottes · Toujours : chaussettes, pantalon")
    e2 = E("Je relie le vêtement et la partie du corps.", relie(["le bonnet", "l'écharpe", "les gants", "les chaussettes", "le pantalon", "la ceinture"], ["sur les jambes", "sur la tête", "à la taille", "aux mains", "aux pieds", "autour du cou"]),
           ["relie"], 1, "B", sol="bonnet → tête · écharpe → cou · gants → mains · chaussettes → pieds · pantalon → jambes · ceinture → taille")
    b.page(f'{e}{e2}', "Lexique")

    cl = "".join(f'<div class="card c" style="padding:2mm">{swatch(c, "100%")}<div class="word" style="font-size:10pt;margin-top:1mm">{n}</div></div>' for c, n in COUL)
    e = E("Les couleurs. J'écoute et je répète.", f'<div class="grid6">{cl}</div>', ["ecoute", "repete"], 1, "A", script="Dire chaque couleur. Jeu : « Levez-vous si vous portez du bleu ! ». Ajouter : clair / foncé (bleu clair, vert foncé).", sol="Activité orale.")
    e2 = E("J'écoute et je colorie le vêtement de la bonne couleur.", '<div class="grid6">' + "".join(f'<div class="card c"><span class="emo" style="filter:grayscale(1);opacity:.55">{em}</span><b>{i}</b></div>' for i, em in enumerate(["👕", "👖", "🧣", "🧢", "🧦", "👗"], 1)) + '</div><p class="sm muted">Je colorie aux crayons de couleur à côté de l\'image, ou j\'écris la couleur.</p>' + lines(1),
           ["ecoute", "colorie"], 1, "A", script="1. Le t-shirt est jaune. 2. Le pantalon est bleu. 3. L'écharpe est rouge. 4. La casquette est verte. 5. Les chaussettes sont blanches. 6. La robe est rose.", sol="1. jaune — 2. bleu — 3. rouge — 4. verte — 5. blanches — 6. rose")
    e3 = E("Qu'est-ce que je porte aujourd'hui ? Je dessine et j'écris.", '<div class="grid2"><div class="card" style="height:42mm"></div><div>' + lines(4) + '</div></div>', ["dessine", "ecris"], 2, "C", sol="Ex. : Je porte un pantalon bleu, un pull gris et des baskets blanches.")
    b.page(f'<h2>Les couleurs</h2>{e}{e2}{e3}', "Lexique")

    # ---------- Leçon 1 : porter / mettre ----------
    l1 = lecon("Porter · mettre · un, une, des", f'''<div class="grid3"><div class="card" style="background:#fff"><b>PORTER</b> (verbe en -er)<p>je porte<br>tu portes<br>il / elle porte<br>nous portons<br>vous portez<br>ils / elles portent</p></div>
<div class="card" style="background:#fff"><b>METTRE</b> ⚠️<p>je mets<br>tu mets<br>il / elle met<br>nous mettons<br>vous mettez<br>ils / elles mettent</p></div>
<div class="card" style="background:#fff"><b>Le sens</b><p><b>Je porte</b> un pull = j'ai le pull sur moi.</p><p><b>Je mets</b> mon manteau = je prends le manteau et je l'habille. 🧥➡️🙂</p><p><b>J'enlève</b> ma veste ⬅️</p></div></div>
<p class="mt2">Je porte <b>un</b> manteau · <b>une</b> écharpe · <b>des</b> gants. — Je <b>ne</b> porte <b>pas de</b> manteau. (négation → pas de, pas d')</p>
<p>Mon / ma / mes : <b>mon</b> pull · <b>ma</b> veste · <b>mes</b> bottes (et <b>mon</b> écharpe devant une voyelle !)</p>''')
    e = E("Je conjugue mettre.", '<p>1. Je ______ mon pull. 2. Tu ______ tes bottes. 3. Il ______ un bonnet. 4. Nous ______ nos gants. 5. Vous ______ une veste. 6. Elles ______ leurs baskets.</p>', ["complete"], 1, "C",
          sol="mets · mets · met · mettons · mettez · mettent")
    b.page(f'{l1}{e}', "Leçon 1")
    e = E("Je complète avec porter ou mettre (au présent).", '<p>1. Aujourd\'hui, Fatou ______ une robe jaune.</p><p>2. Il pleut ! Je ______ mes bottes.</p><p>3. À la piscine, nous ______ un maillot.</p><p>4. Il fait froid, tu ______ ton écharpe ?</p>', ["complete"], 2, "C",
          sol="porte · mets · portons (mettons) · mets")
    e2 = E("Je transforme à la forme négative.", '<p>1. Je porte un manteau. → ______________________</p><p>2. Il met des gants. → ______________________</p><p>3. Elle porte une casquette. → ______________________</p>', ["ecris"], 2, "C",
           sol="Je ne porte pas de manteau. · Il ne met pas de gants. · Elle ne porte pas de casquette.")
    e3 = E("Je regarde mes camarades. Qui porte… ? J'écris les prénoms.", table(["Qui porte…", "Prénom(s)"], [["un pull", ""], ["des baskets", ""], ["une veste", ""], ["des lunettes", ""], ["quelque chose de rouge", ""]], ["70mm", "112mm"]), ["regarde", "ecris", "groupe"], 1, "A",
           sol="Réponses selon la classe : Mateo porte un pull…")
    b.page(f'{e}{e2}{e3}', "S'entraîner")

    # ---------- Leçon 2 : accord des couleurs ----------
    l2 = lecon("Les couleurs s'accordent (masculin · féminin · pluriel)", f'''{table(["", "masculin", "féminin + e", "pluriel + s"], [["vert", "un pull vert", "une robe vert<b>e</b>", "des gants vert<b>s</b> · des bottes vert<b>es</b>"], ["noir", "un sac noir", "une veste noir<b>e</b>", "des sacs noir<b>s</b>"], ["gris", "un pull gris", "une veste gris<b>e</b>", "des pulls gris (déjà un s !)"], ["blanc", "un t-shirt blanc", "une chemise blanc<b>he</b> ⚠️", "des chaussettes blanc<b>hes</b>"], ["violet", "un bonnet violet", "une robe violet<b>te</b> ⚠️", "des robes violet<b>tes</b>"]], ["20mm", "44mm", "52mm", "66mm"])}
<div class="grid2 mt2"><div class="astuce" style="margin:0">Déjà un <b>e</b> à la fin → pas de changement au féminin : rouge, jaune, rose, orange… une robe <b>rouge</b>.</div>
<div class="attention" style="margin:0"><b>orange</b> et <b>marron</b> ne changent jamais : des pulls <b>orange</b>. La couleur se place <b>après</b> le nom : un pull <b>bleu</b>.</div></div>''')
    e = E("J'accorde la couleur.", '<p>1. une jupe (vert) ______ 2. des pantalons (noir) ______ 3. une chemise (blanc) ______ 4. des chaussures (gris) ______</p><p>5. une écharpe (rouge) ______ 6. des bottes (brun) ______ 7. des robes (orange) ______ 8. une casquette (bleu) ______</p>', ["complete"], 2, "C",
          sol="verte · noirs · blanche · grises · rouge · brunes · orange · bleue")
    b.page(f'{l2}{e}', "Leçon 2")
    e = E("Je décris les vêtements de Daria et de Bilal.", '<div class="grid2"><div class="card c">' + avatar("daria", 80) + '<p class="sm">👗 robe : rose · 🧥 veste : blanc · 👢 bottes : noir</p></div><div class="card c">' + avatar("bilal", 80) + '<p class="sm">👖 pantalon : gris · 👕 t-shirt : vert · 👟 baskets : bleu</p></div></div>' + lines(2),
          ["regarde", "ecris"], 2, "C", sol="Daria porte une robe rose, une veste blanche et des bottes noires. · Bilal porte un pantalon gris, un t-shirt vert et des baskets bleues.")
    e2 = E("J'écoute et je coche : masculin ou féminin ?", checks(8, ["masculin", "féminin"]), ["ecoute", "coche"], 2, "A",
           script="1. verte — 2. gris — 3. blanche — 4. noir — 5. violette — 6. vert — 7. grise — 8. blanc", sol="1. F — 2. M — 3. F — 4. M — 5. F — 6. M — 7. F — 8. M")
    e3 = E("Défi ! Je corrige les erreurs d'accord.", '<div class="card big">Amina porte une veste noir, des chaussures blanc et un foulard bleue.</div>' + lines(1), ["barre", "ecris"], 3, "C",
           sol="une veste noire · des chaussures blanches · un foulard bleu")
    b.page(f'{e}{e2}{e3}', "S'entraîner")

    # ---------- Leçon 3 : la météo, les saisons ----------
    mt = "".join(f'<div class="card c" style="background:#fff;padding:2mm"><span class="emo s">{em}</span><div class="xs" style="font-weight:600">{t}</div></div>' for em, t in METEO)
    l3 = lecon("Quel temps fait-il ?", f'''<div class="grid6">{mt}</div>
<div class="grid2 mt2"><div class="card" style="background:#fff"><b>Il fait</b> + beau, chaud, froid, gris, doux, 20 degrés<br><b>Il y a</b> + du soleil, du vent, des nuages, de l'orage, du brouillard<br><b>Il</b> pleut · <b>il</b> neige · <b>il</b> gèle</div>
<div class="card" style="background:#fff"><b>La température</b> 🌡️<br>18 °C = dix-huit degrés<br>0 °C = zéro degré<br>−3 °C = <b>moins</b> trois degrés</div></div>''')
    e = E("J'écoute la météo et je relie la ville et le temps.", relie(["Bruxelles", "Liège", "Ostende", "Arlon", "Namur"], ["🌬️ du vent", "❄️ il neige", "🌧️ il pleut", "☀️ il fait beau", "🌫️ du brouillard"]), ["ecoute", "relie"], 1, "A",
          script="Aujourd'hui, à Bruxelles, il pleut. À Liège, il fait beau. À la mer, à Ostende, il y a beaucoup de vent. Dans les Ardennes, à Arlon, il neige ! Et à Namur, attention au brouillard le matin.",
          sol="Bruxelles → il pleut · Liège → il fait beau · Ostende → vent · Arlon → il neige · Namur → brouillard")
    b.page(f'{l3}{e}', "Leçon 3")
    sais = [("🌸", "le printemps", "mars · avril · mai", "Il fait doux. Il pleut un peu."), ("☀️", "l'été", "juin · juillet · août", "Il fait chaud. Il y a du soleil."),
            ("🍂", "l'automne", "septembre · octobre · novembre", "Il y a du vent. Il pleut."), ("❄️", "l'hiver", "décembre · janvier · février", "Il fait froid. Il gèle, il neige.")]
    l4 = lecon("Les saisons et les mois", '<div class="grid4">' + "".join(f'<div class="card c" style="background:#fff"><span class="emo">{e}</span><b>{s}</b><div class="xs muted">{m}</div><div class="xs">{d}</div></div>' for e, s, m, d in sais) + '</div>' +
               '<p class="mt2"><b>au</b> printemps · <b>en</b> été · <b>en</b> automne · <b>en</b> hiver · <b>en</b> janvier · <b>au mois de</b> mai</p>')
    e = E("Je complète avec au ou en.", '<p>1. ___ été, je vais à la mer. 2. ___ hiver, il neige. 3. ___ printemps, il y a des fleurs. 4. Mon anniversaire est ___ mars. 5. ___ automne, les feuilles tombent.</p>', ["complete"], 1, "C",
          sol="En · En · Au · en · En")
    e2 = E("Je réponds avec une phrase.", f'<p>1. Quel temps fait-il en été en Belgique ? {blank("xl")}</p><p>2. Quelle est ta saison préférée ? Pourquoi ? {blank("xl")}</p><p>3. Ton anniversaire est en quelle saison ? {blank("xl")}</p>', ["ecris"], 2, "C",
           sol="1. En été, il fait chaud / il y a du soleil (et parfois il pleut !). — 2-3. Réponses personnelles.")
    b.page(f'{l4}{e}{e2}', "Leçon 4")
    e = E("J'écoute et j'écris la température.", '<div class="grid6">' + "".join(f'<div class="card c"><b>{c}</b> 🌡️<div class="line"></div></div>' for c in "abcdef") + '</div>', ["ecoute", "ecris"], 2, "A",
          script="a. Il fait 25 degrés. — b. Il fait moins 4 degrés. — c. Il fait 12 degrés. — d. Il fait zéro degré. — e. Il fait 31 degrés. — f. Il fait moins 10 degrés.", sol="25 °C · −4 °C · 12 °C · 0 °C · 31 °C · −10 °C")
    e2 = E("Je conseille ! Quel temps fait-il ? Qu'est-ce que tu mets ?", '<div class="grid4">' + "".join(f'<div class="card c"><span class="emo">{em}</span><div class="line"></div><div class="line"></div></div>' for em in ["🌧️", "🥵", "❄️", "🌬️"]) + '</div>', ["regarde", "ecris"], 2, "C",
           sol="Il pleut : mets ton parapluie / tes bottes · Il fait chaud : mets un short · Il neige : mets ton bonnet, tes gants · Il y a du vent : mets une veste")
    e3 = E("Jeu de rôle : « Maman, il fait quel temps ? » — Je regarde par la fenêtre, je dis le temps et je conseille un vêtement.", '<div class="card"><p>— Il fait quel temps aujourd\'hui ? — Il fait… / Il y a… / Il pleut… — Alors, mets ton… / tes… !</p></div>', ["parle", "duo"], 2, "A",
           sol="Impératif de mettre : mets ! mettons ! mettez ! (prends ton parapluie !)")
    b.page(f'{e}{e2}{e3}', "S'entraîner")

    # ---------- FLESco : lire une carte avec une légende ----------
    l5 = lecon("Lire une carte ou un schéma avec une légende (méthode)", '<p>1️⃣ Je lis le <b>titre</b> : de quoi parle la carte ? 2️⃣ Je regarde la <b>légende</b> : chaque symbole a un sens. 3️⃣ Je cherche le <b>lieu</b> demandé. 4️⃣ Je lis le <b>symbole</b> et le <b>nombre</b>. 5️⃣ Je réponds avec une phrase.</p><p class="sm">On trouve des légendes partout à l\'école : en géographie, en sciences, sur un plan, sur un graphique.</p>')
    carte = belgique({"Ostende": ("🌬️", 9), "Anvers": ("🌧️", 8), "Bruxelles": ("🌧️", 9), "Mons": ("☁️", 10), "Charleroi": ("🌤️", 10), "Namur": ("🌫️", 7), "Liège": ("☀️", 11), "Arlon": ("❄️", 1)})
    leg = '<div class="card" style="padding:2mm"><b class="sm">Légende</b>' + "".join(f'<div class="xs">{e} {t}</div>' for e, t in [("☀️", "soleil"), ("🌤️", "éclaircies"), ("☁️", "nuages"), ("🌧️", "pluie"), ("❄️", "neige"), ("🌬️", "vent"), ("🌫️", "brouillard"), ("<b style=color:#E53935>9°</b>", "température (°C)")]) + '</div>'
    b.page(f'<span class="tag-doc">🎒 FRANÇAIS DE L\'ÉCOLE</span>{l5}<h3>Météo en Belgique · mardi 17 novembre</h3><div class="flex top"><div class="grow">{carte}</div><div style="width:38mm">{leg}</div></div>', "Consignes & école")
    e = E("Je lis la carte et je réponds.", f'<p>1. Quel temps fait-il à Bruxelles ? {blank("l")}</p><p>2. Où est-ce qu\'il neige ? {blank()}</p><p>3. Quelle est la température à Liège ? {blank()}</p><p>4. Où fait-il le plus froid ? {blank()} Le plus chaud ? {blank()}</p><p>5. À Ostende, je mets un short ou une veste ? Pourquoi ? {blank("xl")}</p>',
          ["lis", "ecris"], 2, "B", sol="1. Il pleut. — 2. à Arlon — 3. 11 degrés — 4. à Arlon (1 °C) ; à Liège (11 °C) — 5. une veste : il y a du vent et il fait 9 degrés.")
    e2 = E("Défi ! Je calcule la différence de température entre Liège et Arlon.", f'<p>{blank("xl")}</p>', ["ecris"], 3, "C", sol="11 − 1 = 10 degrés")
    e3 = E("Je dessine une légende pour le plan de ma classe (4 symboles).", '<div class="grid4">' + '<div class="card" style="height:22mm"></div>' * 4 + '</div>', ["dessine", "ecris"], 2, "C", sol="Ex. : ▢ table · ● porte · ★ tableau · ♦ fenêtre")
    b.page(f'{e}{e2}{e3}', "Consignes & école")

    # ---------- Documents de la vie ----------
    days = [("Lun", "🌧️", 6, 11), ("Mar", "🌧️", 7, 9), ("Mer", "☁️", 4, 8), ("Jeu", "🌤️", 2, 7), ("Ven", "☀️", -1, 6), ("Sam", "❄️", -3, 2), ("Dim", "🌬️", 0, 5)]
    bul = '<div class="doc" style="transform:none;padding:3mm;background:#F3F8FD;border:2px solid #3A86C8"><div class="c" style="font-size:18pt;font-weight:800;color:#3A86C8">MÉTÉO · Namur · semaine du 16 au 22 novembre</div><div class="c xs muted">prévisions · site fictif</div>' + \
        '<div class="grid6 mt2" style="grid-template-columns:repeat(7,1fr)">' + "".join(f'<div class="card c" style="padding:2mm;background:#fff"><b>{d}</b><span class="emo">{em}</span><div class="sm"><span style="color:#1E88E5;font-weight:800">{mn}°</span> / <span style="color:#E53935;font-weight:800">{mx}°</span></div></div>' for d, em, mn, mx in days) + '</div>' + \
        '<p class="xs mt2"><span style="color:#1E88E5;font-weight:800">bleu</span> = minimum (la nuit) · <span style="color:#E53935;font-weight:800">rouge</span> = maximum (l\'après-midi) · Vent : 🌬️ fort dimanche (60 km/h) · ⚠️ Risque de verglas samedi matin.</p></div>'
    e = E("Je lis le bulletin météo. Je réponds.", f'<p>1. Quel temps fait-il lundi ? {blank()} 2. Quel jour il neige ? {blank()}</p><p>3. La température maximum mercredi ? {blank()} 4. La température minimum samedi ? {blank()}</p><p>5. Quel jour il fait le plus beau ? {blank()} 6. Pourquoi faire attention samedi matin ? {blank("xl")}</p>',
          ["lis", "ecris"], 2, "B", sol="1. Il pleut. — 2. samedi — 3. 8 degrés — 4. moins 3 degrés — 5. vendredi (soleil) — 6. Il y a du verglas : la route glisse (il gèle).")
    b.page(f'<span class="tag-doc">📄 DOCUMENT DE LA VIE</span><h2>Le bulletin météo de la semaine</h2>{bul}<div class="mt4">{e}</div><div class="astuce">Le <b>verglas</b> = de la glace sur la route. Ça glisse ! On marche doucement.</div>', "Document de la vie")
    cat = [("🧥", "Doudoune", "noire, bleue", "S · M · L · XL", "39,90 €", "29,90 €"), ("👖", "Jean", "bleu", "34 → 44", "24,99 €", ""), ("👚", "Pull col roulé", "gris, rose, vert", "XS → L", "17,50 €", ""), ("🧣", "Écharpe + bonnet", "rouge, gris", "taille unique", "12 €", "9,60 €"),
           ("👟", "Baskets", "blanches", "36 → 45", "34,95 €", ""), ("🧤", "Gants tactiles", "noirs", "S · M · L", "8,99 €", ""), ("👢", "Bottes de pluie", "jaunes, vertes", "30 → 42", "19 €", "15,20 €"), ("☂️", "Parapluie", "à pois", "—", "7,50 €", "")]
    cg = '<div class="doc" style="transform:none;padding:3mm;background:#fff;border:2px solid #1F2A44"><div class="flex" style="justify-content:space-between"><b style="font-size:18pt">MODE & CO · Catalogue hiver</b><span style="background:#E53935;color:#fff;padding:1mm 3mm;border-radius:2mm;font-weight:800">SOLDES −20 %</span></div><div class="xs muted">magasin fictif · prix barré = ancien prix</div>' + \
        '<div class="grid4 mt2">' + "".join(f'<div class="card c" style="padding:2mm"><span class="emo">{e}</span><b class="sm">{n}</b><div class="xs">Couleurs : {c}<br>Tailles : {t}</div>' + (f'<div><s class="xs muted">{p}</s> <b style="color:#E53935;font-size:12pt">{s}</b></div>' if s else f'<div><b style="font-size:12pt">{p}</b></div>') + '</div>' for e, n, c, t, p, s in cat) + '</div></div>'
    e = E("Je lis le catalogue. Je réponds.", f'<p>1. La doudoune existe en quelles couleurs ? {blank("l")} 2. Elle coûte combien en soldes ? {blank()}</p><p>3. Les bottes de pluie : quelles tailles ? {blank()} 4. Quels articles sont en soldes ? {blank("xl")}</p><p>5. J\'achète un jean et des gants. Je paie combien ? {blank()}</p>',
          ["lis", "ecris"], 2, "B", sol="1. noire, bleue — 2. 29,90 € — 3. du 30 au 42 — 4. doudoune, écharpe + bonnet, bottes de pluie — 5. 24,99 + 8,99 = 33,98 €")
    e2 = E("Défi ! J'ai 50 €. Je m'habille pour l'hiver. J'écris ma liste et le total.", lines(3), ["ecris"], 3, "C", sol="Ex. : doudoune 29,90 + écharpe-bonnet 9,60 + gants 8,99 = 48,49 € ✔")
    b.page(f'<span class="tag-doc">📄 DOCUMENT DE LA VIE</span><h2>Le catalogue de vêtements</h2>{cg}<div class="mt4">{e}{e2}</div>', "Document de la vie")
    etq = '''<div class="doc" style="transform:rotate(-1.5deg);width:70mm;margin:auto;padding:4mm;background:#fff;border:1px solid #bbb;font-size:10pt"><div class="c"><b>MODE & CO</b></div><hr><div class="c" style="font-size:22pt;font-weight:800">M</div>
<div class="c">100 % coton</div><hr><div class="c" style="font-size:14pt">🫧 30° · 🚫🔥 · 🚫🌀 · ♨️ doux</div><div class="xs c">Laver à 30 degrés · pas d'eau de Javel · pas de sèche-linge · repasser doux</div><hr><div class="xs c">Fabriqué au Portugal</div></div>'''
    e = E("Je lis l'étiquette du pull. Je coche vrai ou faux.", vf(["Le pull est en taille M.", "Je lave le pull à 60 degrés.", "Je peux mettre le pull au sèche-linge.", "Le pull est en coton.", "Le pull vient du Portugal."]), ["lis", "coche"], 2, "B",
          sol="Vrai · Faux (30 degrés) · Faux · Vrai · Vrai")
    e2 = E("Les tailles. Je relie.", relie(["S", "M", "L", "XL"], ["très grand", "petit", "grand", "moyen"]), ["relie"], 1, "B", sol="S → petit · M → moyen · L → grand · XL → très grand")
    e3 = E("Au magasin : je demande une autre taille. Je joue avec mon voisin.", '<div class="card"><p>— Bonjour, vous avez ce pull en taille L ? — Oui, voilà. — Je peux l\'essayer ? — Oui, la cabine est là. — Il est trop petit / trop grand / parfait !</p></div>', ["parle", "duo"], 2, "A", sol="Révision M7 : je voudrais, je peux, combien ça coûte ?")
    b.page(f'<span class="tag-doc">📄 DOCUMENT DE LA VIE</span><h2>L\'étiquette du vêtement</h2>{etq}<div class="mt4">{e}{e2}{e3}</div>', "Document de la vie")

    # ---------- Sons ----------
    e = E("[e] et [ɛ]. J'écoute et je répète.", '<div class="grid2"><div class="card c"><div class="huge">[e]</div><p>é · er · ez · et<br>été · bébé · porter · vous mettez · et</p><p class="sm muted">La bouche sourit 😁</p></div><div class="card c"><div class="huge">[ɛ]</div><p>è · ê · ai · ei · e + 2 consonnes<br>mère · fête · il fait · la neige · la veste</p><p class="sm muted">La bouche s\'ouvre un peu plus 😮</p></div></div>', ["ecoute", "repete"], 1, "A",
          script="Paires : été / était, les / lait, thé / tête, fée / fait. Exagérer l'ouverture de la bouche.", sol="Activité orale.")
    e2 = E("J'écoute : [e] ou [ɛ] ?", checks(8, ["[e]", "[ɛ]"]), ["ecoute", "coche"], 2, "A", script="1. été — 2. neige — 3. veste — 4. porter — 5. mère — 6. bébé — 7. il fait — 8. vous mettez", sol="1. e — 2. ɛ — 3. ɛ — 4. e — 5. ɛ — 6. e — 7. ɛ — 8. e")
    e3 = E("J'entoure é en bleu et è / ê / ai en rouge.", '<div class="card big" style="line-height:1.8">l\'été · la fête · un pull vert · la chaîne · il gèle · le bébé · il fait frais · la météo · mettez votre bonnet · une chemise légère</div>', ["entoure", "colorie"], 2, "B",
           sol="é : été, bébé, météo, mettez, légère (é) · è/ê/ai : fête, chaîne, gèle, fait, frais, légère (è) ; vert (e+2 consonnes)")
    b.page(f'<h2>J\'écoute bien</h2>{e}{e2}{e3}', "Sons")

    e = E("🔁 Module 7 · Les prix.", '<p>Une écharpe coûte 12 €. Je donne 20 €. On me rend ______. — 85 en lettres (Belgique) : ______________</p>', ["ecris"], 2, "C", sol="8 € · quatre-vingt-cinq")
    e2 = E("🔁 Module 7 · Je voudrais…", '<p>Je veux un pull. → (poli) ______________________</p>', ["ecris"], 1, "C", sol="Je voudrais un pull, s'il vous plaît.")
    e3 = E("🔁 Module 6 · J'aime / je n'aime pas.", '<p>J\'adore ___ été. Je n\'aime pas ___ pluie. Je déteste ___ froid.</p>', ["complete"], 1, "C", sol="l' · la · le")
    b.page(f'<h2>🔁 Je révise les modules 6 et 7</h2>{e}{e2}{e3}', "Je révise")

    # ---------- Ateliers ----------
    cards = [("☀️", "Il fait beau"), ("🌧️", "Il pleut"), ("❄️", "Il neige"), ("🌬️", "Il y a du vent"), ("🌫️", "Il y a du brouillard"), ("🥵", "Il fait chaud"), ("🥶", "Il fait froid"), ("⛈️", "Il y a de l'orage")]
    e = E("Le mémory de la météo : je découpe les 16 cartes. Je retourne 2 cartes : l'image et la phrase. Je lis à voix haute. Paire = je garde !", '<div class="grid4">' + "".join(f'<div class="card c" style="border-style:dashed;height:22mm;display:flex;align-items:center;justify-content:center"><span class="emo">{em}</span></div>' for em, _ in cards) +
          "".join(f'<div class="card c" style="border-style:dashed;height:22mm;display:flex;align-items:center;justify-content:center"><b>{t}</b></div>' for _, t in cards) + '</div>', ["decoupe", "joue", "groupe"], 1, "D", sol="Jeu : dire la phrase à chaque carte retournée.")
    b.page(f'{atl_head("D", "Atelier · Le mémory de la météo")}{e}', "Atelier")
    e = E("Habille Mateo ! Je lance le dé météo, puis je découpe et je colle les bons vêtements. Je dis : « Il pleut, Mateo met… ».", '<div class="grid2"><div class="card c">' + avatar("mateo", 120) + '<p class="sm">🎲 1 ☀️ · 2 🌧️ · 3 ❄️ · 4 🌬️ · 5 🥵 · 6 🥶</p></div><div class="grid4">' +
          "".join(f'<div class="card c" style="border-style:dashed;padding:1mm"><span class="emo s">{em}</span><div class="xs">{w}</div></div>' for em, w in VET[:16]) + '</div></div>', ["decoupe", "colle", "parle", "joue"], 2, "D", sol="Ex. : Il neige, Mateo met son manteau, son bonnet et ses gants.")
    e2 = E("Le défilé de mode de la classe : je présente la tenue d'un camarade.", '<div class="card"><p>Voici Fatou ! Elle porte une robe… avec… Ses chaussures sont… C\'est parfait pour l\'hiver / l\'été !</p></div>', ["parle", "groupe"], 2, "A", sol="Accord des couleurs à l'oral (verte, blanche…).")
    b.page(f'{atl_head("D", "Atelier · Habiller et présenter")}{e}{e2}', "Atelier")
    e = E("Je lis la carte postale de Daria. Je réponds.", '<div class="doc" style="transform:rotate(-1deg);padding:4mm;background:#FFFCF2;border:1px solid #d8c9a8"><div class="grid2"><p class="sm" style="font-family:\'DejaVu Serif\'">Salut Amina !<br>Je suis à la mer à Ostende avec ma famille. Il fait froid et il y a beaucoup de vent ! Je porte mon gros pull rouge, mon manteau et mon bonnet. Demain, il va pleuvoir… On va visiter l\'aquarium. Bisous !<br>Daria</p><div class="c"><div style="font-size:30pt">🌊🌬️🏖️</div><div class="xs" style="border-top:1px solid #aaa;margin-top:4mm;padding-top:2mm">Amina Benali<br>Rue des Écoles 12<br>5000 Namur</div></div></div></div>' +
          f'<p class="mt2">1. Où est Daria ? {blank()} 2. Quel temps fait-il ? {blank("l")}</p><p>3. Qu\'est-ce qu\'elle porte ? {blank("xl")} 4. Quel temps demain ? {blank()}</p>', ["lis", "ecris"], 2, "B",
          sol="1. à Ostende, à la mer — 2. Il fait froid, il y a du vent — 3. son pull rouge, son manteau et son bonnet — 4. Il va pleuvoir.")
    e2 = E("J'écris une carte postale à un ami : où je suis, le temps, mes vêtements (4 phrases).", lines(4), ["ecris"], 2, "C", sol="Production libre avec : Je suis à… Il fait… Je porte… Bisous !")
    b.page(f'{atl_head("C", "Atelier · Lire et écrire")}{e}{e2}', "Atelier")

    # ---------- ★ Alpha ----------
    letter_page(b, E, "é", "[e]", [("👶", "bébé"), ("☕", "café"), ("📺", "télé"), ("☀️", "été")], "eèêaeèou", [("👶", "bébé", 1), ("☕", "café", 1), ("🐟", "poisson", 0), ("📺", "télé", 1), ("🌧️", "pluie", 0), ("⭐", "étoile", 1), ("🐘", "éléphant", 1), ("🧥", "manteau", 0)], MC)
    letter_page(b, E, "è", "[ɛ]", [("👩", "mère"), ("👨", "père"), ("🦓", "zèbre"), ("🧒", "frère")], "eéêaeéou", [("👩", "mère", 1), ("🦓", "zèbre", 1), ("👶", "bébé", 0), ("👨", "père", 1), ("🎉", "fête", 1), ("☕", "café", 0), ("🧒", "frère", 1), ("🍌", "banane", 0)], MC)
    letter_page(b, E, "ai", "[ɛ]", [("🥛", "lait"), ("🏠", "maison"), ("✋", "main"), ("🌨️", "neige")], "aieaiauo", [("🥛", "lait", 1), ("🌨️", "neige", 1), ("🍞", "pain", 0), ("🏠", "maison", 1), ("🦓", "zèbre", 1), ("☕", "café", 0), ("🎉", "fête", 1), ("👶", "bébé", 0)], MC)
    e = E("Je lis les syllabes et les mots.", syll_table(["m", "p", "t", "l"], "é è ai") + '<div class="grid4 mt2">' + "".join(f'<div class="card c"><span class="emo s">{em}</span><div class="huge" style="font-size:16pt">{w}</div></div>' for em, w in [("👶", "bé·bé"), ("☕", "ca·fé"), ("👩", "mè·re"), ("🥛", "lait")]) + '</div>', ["lis"], 1, "P", alpha=True, sol="Lecture des syllabes : mé mè mai, pé pè pai…")
    e2 = E("Je lis les phrases. Je montre l'image.", '<div class="grid2">' + "".join(f'<div class="card"><p class="big">{t}</p></div>' for t in ["Il fait beau. ☀️", "Il pleut. 🌧️", "Il neige. ❄️", "Le bébé a un pull rouge. 👶"]) + '</div>', ["lis", "montre"], 2, "P", alpha=True, sol="Lecture.")
    b.page(AL.format(t="Je lis") + e + e2, "★ Alpha", color=MC)
    e = E("Je relie le mot et l'image.", relie([f'<b class="big">{w}</b>' for w in ["pull", "bébé", "neige", "mère", "lait"]], [f'<span class="emo s">{x}</span>' for x in ["❄️", "🥛", "👚", "👩", "👶"]]), ["lis", "relie"], 1, "B", alpha=True, sol="pull–👚 · bébé–👶 · neige–❄️ · mère–👩 · lait–🥛")
    e2 = E("Je recopie : il fait froid.", trace("il fait froid", 24, 2), ["recopie", "trace"], 1, "C", alpha=True, sol="Écriture.")
    e3 = E("Dictée.", guide_lines(2, 20), ["ecoute", "ecris"], 2, "P", alpha=True, script="Dicter : é — è — ai — bébé — lait — il pleut", sol="é è ai bébé lait il pleut")
    b.page(AL.format(t="J'écris") + e + e2 + e3, "★ Alpha", color=MC)

    # ---------- Tâche finale ----------
    e = E("Avec mon groupe, je prépare le « conseil tenue » de la semaine pour la classe. J'utilise le bulletin météo de la page « Document de la vie » ou une vraie appli météo.", table(["Jour", "Météo (dessin + phrase)", "Température", "Notre conseil : mets…"], [[d, "", "", ""] for d in ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi"]], ["24mm", "62mm", "30mm", "66mm"]).replace("<td></td>", '<td style="height:15mm"></td>'),
          ["ecris", "dessine", "groupe"], 2, "C", sol="Évaluation avec la grille : phrases météo justes, conseils logiques, impératif de mettre.")
    b.page(tache_head("Le conseil tenue de la semaine", "Nous lisons la météo, nous écrivons un conseil pour chaque jour, puis nous présentons notre affiche à la classe (comme à la télé !).") + e +
           table(["Je vérifie :", "✅"], [[x, '<span class="chk"></span>'] for x in ["Il y a la météo de chaque jour (il fait, il pleut, il y a…).", "J'écris la température (degrés, moins…).", "Les conseils sont logiques (pluie → parapluie).", "J'accorde les couleurs.", "Je présente à l'oral comme à la télé."]], ["160mm", "22mm"]), "Tâche finale", levels=False)
    e = E("Je révise.", '<p>1. Nous ______ (mettre) nos gants. 2. une veste (blanc) ______ 3. ___ hiver, il fait froid. 4. −5 °C se dit : ______________ 5. Il ______ (pluie) → Il ______.</p>', ["ecris"], 2, "C",
          sol="mettons · blanche · En · moins cinq degrés · Il pleut.")
    e2 = E("Défi ! Je corrige les 4 erreurs.", '<div class="card big">En hiver, il fait froide. Je met mon pantalon verts et ma écharpe.</div>' + lines(1), ["barre", "ecris"], 3, "C",
           sol="il fait froid (pas de e) · Je mets · mon pantalon vert · mon écharpe")
    b.page(f'<h2>🔁 Je révise tout le module</h2>{e}{e2}', "Je révise")

    # ---------- Test ----------
    Q = [("🧣 C'est :", ["un bonnet", "une écharpe", "des gants", "une casquette"]), ("On met les gants…", ["aux pieds", "sur la tête", "aux mains", "autour du cou"]),
         ("Je ____ mon manteau.", ["met", "mets", "mettons", "mettez"]), ("Vous ____ vos bottes.", ["mettez", "mettent", "mets", "mettons"]),
         ("une robe ____", ["vert", "verte", "verts", "vertes"]), ("une chemise ____", ["blanc", "blanche", "blance", "blanches"]),
         ("des pulls ____", ["orange", "oranges", "orangé", "orangées"]), ("des chaussures ____", ["noir", "noire", "noirs", "noires"]),
         ("🌧️ :", ["Il neige.", "Il pleut.", "Il fait chaud.", "Il y a du soleil."]), ("🌬️ :", ["Il y a du vent.", "Il fait du vent.", "Il est vent.", "Il vente."]),
         ("−2 °C se dit :", ["deux degrés", "moins deux degrés", "plus deux degrés", "zéro deux degrés"]), ("Les mois de l'été :", ["juin, juillet, août", "mars, avril, mai", "décembre, janvier, février", "septembre, octobre, novembre"]),
         ("____ printemps, il fait doux.", ["En", "Au", "À la", "Le"]), ("Il fait froid. Je conseille :", ["Mets ton short !", "Mets ton bonnet !", "Mets tes sandales !", "Enlève ton pull !"]),
         ("Sur une carte, la ____ explique les symboles.", ["légende", "question", "date", "taille"]), ("Sur l'étiquette, « 30° » veut dire :", ["il fait 30 degrés", "laver à 30 degrés", "taille 30", "30 euros"]),
         ("Je ne porte pas ____ manteau.", ["un", "de", "du", "le"]), ("J'entends [e] comme dans « été » :", ["mère", "fête", "bébé", "lait"]),
         ("🔁 Une veste à 18 €, je donne 20 €. On me rend :", ["2 €", "3 €", "12 €", "38 €"]), ("🔁 Au magasin, poli :", ["Je veux ça.", "Je voudrais ce pull, s'il vous plaît.", "Donne le pull !", "Pull !"])]
    ans = ["une écharpe", "aux mains", "mets", "mettez", "verte", "blanche", "orange", "noires", "Il pleut.", "Il y a du vent.", "moins deux degrés", "juin, juillet, août", "Au", "Mets ton bonnet !",
           "légende", "laver à 30 degrés", "de", "bébé", "2 €", "Je voudrais ce pull, s'il vous plaît."]
    key = key_from(Q, ans)
    test_pages(b, 8, "Vêtements et météo", Q, f'<h3>B1. Je décris ma tenue avec 3 vêtements et 3 couleurs. (… / 4)</h3>{lines(2, True)}<h3>B2. Il neige et il fait −4 °C. J\'écris le temps et je conseille une tenue. (… / 3)</h3>{lines(2, True)}<h3>B3. J\'écris les 4 saisons. (… / 3)</h3>{lines(1, True)}',
               [["dire le temps qu'il fait (3 images)", "/ 3", ""], ["décrire la tenue d'un camarade (couleurs accordées)", "/ 4", ""], ["conseiller : « Mets ton… ! »", "/ 3", ""]],
               f'<h3>1. J\'écoute et j\'entoure. (… / 4)</h3><div class="grid4">{"".join(f"<div class=\'card c big\' style=\'font-weight:700\'>{r}</div>" for r in ["é è ai", "ai é è", "è ai é", "é ai è"])}</div><h3>2. Je lis et je relie. (… / 4)</h3>{relie([f"<b class=big>{w}</b>" for w in ["bébé", "lait", "mère", "neige"]], ["<span class=\'emo s\'>👩</span>", "<span class=\'emo s\'>❄️</span>", "<span class=\'emo s\'>👶</span>", "<span class=\'emo s\'>🥛</span>"])}<h3>3. Dictée. (… / 4)</h3>{guide_lines(1, 22)}<h3>4. Je dis le temps (oral, avec les images). (… / 4)</h3><div class="card">☐ ☀️ ☐ 🌧️ ☐ ❄️ ☐ 🥶</div><h3>5. Je montre et je dis 4 vêtements. (… / 4)</h3><div class="card">☐ pull ☐ pantalon ☐ manteau ☐ chaussures</div>')
    closing(b, 8, ["Je sais nommer les vêtements.", "Je sais dire les couleurs.", "Je sais accorder les couleurs (verte, blanche…).", "Je sais conjuguer porter et mettre.", "Je sais dire le temps qu'il fait.",
                   "Je sais lire une température (moins…).", "Je connais les saisons et les mois.", "Je sais lire une carte avec une légende.", "Je sais lire un bulletin météo, un catalogue, une étiquette.", "Je sais conseiller une tenue.", "★ Je sais lire é, è, ai, bébé, lait…"],
            VET[:14] + [("☀️", "le soleil"), ("🌧️", "la pluie"), ("❄️", "la neige"), ("🌬️", "le vent"), ("☁️", "le nuage"), ("🌫️", "le brouillard"), ("🌡️", "la température"), ("🌸", "le printemps"), ("🏖️", "l'été"), ("🍂", "l'automne"), ("⛄", "l'hiver"), ("🎨", "la couleur"), ("🏷️", "l'étiquette"), ("📏", "la taille")])
    plan_de_travail(b, E, 8, ["Porter · mettre", "L'accord des couleurs", "Quel temps fait-il ?", "Les saisons et les mois", "Lire une carte avec une légende"], "☐ Affiche « conseil tenue » de la semaine<br>☐ Présentation « comme à la télé »")
    if render:
        to_pdf(b.html(), '/home/claude/syllabus/out/V1_M8_eleve.pdf')

    # ---------- Livret enseignant ----------
    pg, exs = helpers(b, E)
    A = b.marks["★ Alpha"]
    days = [("1", "Collectif", f"Ouverture · BD ({pg('Découvrir')})", f"Alpha : é (p. {A[0]})"), ("2", "Collectif", f"Vêtements et couleurs ({pg('Lexique')})", f"Alpha : è (p. {A[1]})"),
            ("3", "Rotation", f"📌 Leçon 1 porter, mettre ({pg('Leçon 1')})", f"Alpha : ai (p. {A[2]})"), ("4", "Rotation", f"📌 Leçon 2 accord des couleurs ({pg('Leçon 2')})", f"Alpha : lecture (p. {A[3]})"),
            ("5", "Collectif", f"📌 Leçons 3-4 météo, saisons ({pg('Leçon 3')}, {pg('Leçon 4')})", f"Alpha : écriture (p. {A[4]})"), ("6", "Rotation", f"Carte et légende ({pg('Consignes & école')}) · sons", "Alpha : météo en images"),
            ("7", "Collectif", f"Bulletin, catalogue, étiquette ({pg('Document de la vie')})", "Alpha : vêtements réels"), ("8", "Ateliers", f"Mémory, habiller Mateo, carte postale ({pg('Atelier')})", "Alpha : mémory (images)"),
            ("9", "Groupes", f"Tâche finale ({pg('Tâche finale')})", "Alpha : dessin + 1 phrase"), ("10", "Seul", f"Test ({pg('Test')})", f"Alpha : test ({pg('★ Alpha · Test')})")]
    rot = [["🎧 Écouter-Parler", "Défilé de mode · jeu de rôle « taille »", "20 min", "—"], ["📖 Lire", "Carte postale · étiquette", "20 min", "Oui"], ["✏️ Écrire", "Accord des couleurs · carte postale", "20 min", "● oui"],
           ["🧩 Jouer", "Mémory météo · habiller Mateo", "20 min", "Entre joueurs"], ["👩‍🏫 Table d'appui", "Alpha : é è ai · autres : mettre, accords", "20 min", "—"]]
    ev1 = '''<h3>Partie B (10 points)</h3><p class="sm"><b>B1</b> : 1 pt par vêtement + couleur bien accordée (max 4) · <b>B2</b> : <span class="sol">Il neige et il fait froid (moins quatre degrés). Mets ton manteau, ton bonnet et tes gants !</span> (météo 1, conseil 2) · <b>B3</b> : <span class="sol">le printemps, l'été, l'automne, l'hiver</span> (4 justes = 3 pts).</p>
<h3>Test ★ Alpha</h3><p class="sm"><b>Ex. 1, dire :</b> <span class="sol">è · é · ai · ai</span> · <b>Ex. 2 :</b> <span class="sol">bébé–👶, lait–🥛, mère–👩, neige–❄️</span> · <b>Ex. 3, dicter :</b> <span class="sol">é, ai, bébé, lait</span>.</p>'''
    ev2 = f'''<h2>Grille · tâche finale « Le conseil tenue de la semaine »</h2>{table(["Critère", "Très bien", "Bien", "À retravailler", "Points"], [["<b>Météo</b> : phrases justes (il fait, il pleut, il y a)", "Oui", "Partielle", "Non", "/ 5"], ["<b>Températures</b> lues et dites", "Justes", "1-2 erreurs", "Fausses", "/ 3"], ["<b>Conseils</b> logiques, impératif « mets »", "Oui", "Partiel", "Non", "/ 6"], ["<b>Langue</b> : accords des couleurs, articles", "Correct", "Quelques erreurs", "Beaucoup", "/ 3"], ["<b>Présentation orale</b>", "Fluide", "Hésitante", "Bloquée", "/ 3"]], ["64mm", "32mm", "32mm", "32mm", "22mm"])}
<h2 class="mt4">Différencier et remédier</h2>{table(["Difficulté", "Remédiation"], [["Accord des couleurs", "Étiquettes « e » et « s » mobiles à poser derrière l'adjectif ; tri de vrais vêtements masculins / féminins."], ["Il fait / il y a", "Deux colonnes affichées : il fait + adjectif · il y a + du/de la/des + nom."], ["mettre (irrégulier)", "Chant / rythme « je mets, tu mets, il met » ; dé de conjugaison."], ["Températures négatives", "Thermomètre vertical affiché en classe, relevé quotidien."], ["Élève rapide", "Comparer la météo de 3 capitales (appli) ; écrire un bulletin pour la radio de l'école."]], ["50mm", "132mm"])}
<div class="astuce mt4"><b>Interculturel et sensibilité :</b> certains élèves découvrent le froid et la neige ; d'autres n'ont pas de vêtements adaptés. Proposer la <b>bourse aux vêtements</b> discrètement (CPMS, associations, vestiaire de l'école). Valoriser les tenues traditionnelles : le foulard, le boubou, la djellaba… sont aussi des vêtements à nommer.</div>'''
    T = teacher_book(b, E, "V1 · M8", "", MC, 8, "Vêtements et météo",
                     "<li><b>Communication :</b> décrire une tenue, dire le temps qu'il fait, conseiller.</li><li><b>Lexique :</b> vêtements, couleurs, météo, saisons, mois, tailles.</li><li><b>Grammaire :</b> porter, mettre ; accord des couleurs ; il fait / il y a / il pleut ; au / en + saison ; pas de.</li><li><b>Phonétique :</b> [e] / [ɛ].</li><li><b>FLSco :</b> lire une carte avec une légende.</li><li><b>Documents :</b> bulletin météo, catalogue, étiquette.</li><li><b>★ Alpha :</b> é, è, ai.</li>",
                     '<p class="sm"><b style="color:#E4572E">Indispensable</b> : vêtements de base, il fait froid / il pleut, mets ton…</p><p class="sm"><b style="color:#d9a400">Important</b> : accord des couleurs, températures, saisons.</p><p class="sm"><b style="color:#2BA88F">Enrichissement</b> : étiquette d\'entretien, soldes, carte et légende.</p>',
                     "Caisse de vrais vêtements · thermomètre · crayons de couleur · dé · ciseaux et colle · appli ou site météo (projeté).", "<b>Rituel météo :</b> chaque matin, un élève « présentateur » relève le temps et la température et les note sur l'affiche de la classe.",
                     days, "Météo du jour (présentateur) · « Qui porte du bleu ? » · le mois et la saison du jour.", rot, key, (ev1, ev2), start=tstart)
    if render:
        to_pdf(T.html(), '/home/claude/syllabus/out/V1_M8_prof.pdf')
    return b, T


if __name__ == "__main__":
    b, T = build_m8()
    print(b.n, T.n)
