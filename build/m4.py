"""Volume 1 · Module 4 « Ma famille et moi »."""
import sys
sys.path.insert(0, '/home/claude/syllabus')
from lib.base import *
from lib.art import *
from lib.alpha import AL, letter_page, syll_table, slide
from lib.module import plan_de_travail, teacher_book, helpers
from lib.render import to_pdf

MC = "#C94F7C"
FAM = {"jorge": dict(skin="moyen", style="chauve", beard=True, gray=True, shirt="#6B8F3E"), "rosa": dict(skin="moyen", style="long", gray=True, glasses=True, shirt="#C94F7C"),
       "carlos": dict(skin="moyen", hair="#2a1a10", style="court", beard=True, shirt="#2E4057"), "lucia": dict(skin="mat", hair="#111", style="long", shirt="#F29E4C"),
       "diego": dict(skin="moyen", hair="#2a1a10", style="court", glasses=True, shirt="#7A5BC7"), "ana": dict(skin="clair", hair="#B5651D", style="boucle", shirt="#2BA88F", eyes="#2E7D32"),
       "lucas": dict(skin="moyen", hair="#2a1a10", style="court", shirt="#E4572E"), "mateo": dict(skin="moyen", hair="#3B2516", style="court", shirt="#4A7BD1"),
       "valentina": dict(skin="mat", hair="#111", style="queue", shirt="#F2C14E"), "pablo": dict(skin="clair", hair="#B5651D", style="boucle", shirt="#9B5DE5", eyes="#2E7D32")}


def fcard(k, name, role, size=54):
    return f'<div class="c" style="width:30mm">{face(size=size, **FAM[k])}<div class="word" style="font-size:10pt">{name}</div><div class="xs muted">{role}</div></div>'


def tree():
    line = lambda w: f'<div style="height:5mm;border-left:2px solid #1F2A44;margin:0 auto;width:0"></div>'
    return f'''<div class="doc" style="transform:none;padding:4mm;background:#FFFDF8">
<div class="c" style="font-weight:800;color:{MC};margin-bottom:2mm">🌳 L'arbre de la famille Ramírez</div>
<div class="flex" style="justify-content:center;gap:4mm">{fcard("jorge", "Jorge", "70 ans")}<div style="align-self:center;font-size:16pt">❤️</div>{fcard("rosa", "Rosa", "68 ans")}</div>
<div style="width:80mm;margin:0 auto;border-top:2px solid #1F2A44;height:5mm;border-left:2px solid #1F2A44;border-right:2px solid #1F2A44"></div>
<div class="flex" style="justify-content:space-around">
<div class="flex" style="gap:2mm">{fcard("carlos", "Carlos", "45 ans")}<div style="align-self:center">❤️</div>{fcard("lucia", "Lucía", "42 ans")}</div>
<div class="flex" style="gap:2mm">{fcard("diego", "Diego", "40 ans")}<div style="align-self:center">❤️</div>{fcard("ana", "Ana", "38 ans")}</div></div>
<div class="flex" style="justify-content:space-around"><div style="width:70mm;border-top:2px solid #1F2A44;height:4mm;border-left:2px solid #1F2A44;border-right:2px solid #1F2A44;margin-top:2mm"></div><div style="width:2px;height:6mm;background:#1F2A44;margin-top:2mm"></div></div>
<div class="flex" style="justify-content:space-around"><div class="flex" style="gap:4mm">{fcard("lucas", "Lucas", "18 ans")}{fcard("mateo", "Mateo", "15 ans")}{fcard("valentina", "Valentina", "10 ans")}</div>{fcard("pablo", "Pablo", "12 ans")}</div></div>'''


QUI = [("Karim", dict(skin="mat", hair="#111", style="court", beard=True, eyes="#3B2516", shirt="#2E4057")), ("Lina", dict(skin="clair", hair="#E8C26A", style="long", eyes="#1E5AA8", shirt="#C94F7C")),
       ("Paul", dict(skin="clair", hair="#B5651D", style="court", glasses=True, eyes="#2E7D32", shirt="#2BA88F")), ("Aïcha", dict(skin="fonce", hair="#111", style="boucle", eyes="#3B2516", shirt="#F2C14E")),
       ("Omar", dict(skin="fonce", hair="#111", style="chauve", beard=True, eyes="#3B2516", shirt="#7A5BC7")), ("Nina", dict(skin="clair", hair="#111", style="queue", glasses=True, eyes="#3B2516", shirt="#E4572E")),
       ("Léo", dict(skin="moyen", hair="#E8C26A", style="boucle", eyes="#1E5AA8", shirt="#4A7BD1")), ("Sara", dict(skin="moyen", hair="#B5651D", style="long", eyes="#2E7D32", shirt="#6B8F3E")),
       ("Marc", dict(skin="clair", hair="#BDBDBD", style="court", glasses=True, beard=True, eyes="#1E5AA8", shirt="#9B5DE5", gray=True)), ("Zoé", dict(skin="clair", hair="#B5651D", style="boucle", eyes="#1E5AA8", shirt="#F29E4C")),
       ("Ali", dict(skin="moyen", hair="#111", style="court", eyes="#3B2516", shirt="#E4572E")), ("Mia", dict(skin="mat", hair="#3B2516", style="long", glasses=True, eyes="#3B2516", shirt="#2BA88F"))]


def build_m4(start=1, tstart=1, render=True):
    b = Book("V1 · M4", "Volume 1 · Premiers pas · Module 4 · Ma famille et moi", MC, start=start)
    E = Ex(b)
    obj = [("👨‍👩‍👧‍👦", "présenter ma famille"), ("🧑", "décrire une personne : physique et caractère"), ("🔤", "dire mon, ma, mes · ton, ta, tes · son, sa, ses"),
           ("⚖️", "accorder l'adjectif : grand / grande"), ("📋", "conjuguer être et avoir avec nous, vous, ils"), ("🖼️", "décrire une image")]
    objs = "".join(f'<div class="flex mb2"><span class="emo s">{e}</span><span class="big">{t}</span></div>' for e, t in obj)
    b.page(f'''<div style="background:{MC};color:#fff;margin:-17mm -14mm 6mm -14mm;padding:16mm 14mm 6mm 14mm"><div style="font-size:13pt;font-weight:700;opacity:.9">MODULE 4</div><div style="font-size:44pt;font-weight:800;line-height:1">Ma famille et moi</div></div>
<div class="flex" style="justify-content:space-around;background:#FCEAF1;border-radius:4mm;padding:4mm">{"".join(face(size=78, **FAM[k]) for k in ["rosa", "carlos", "lucia", "mateo", "valentina", "jorge"])}</div>
<div class="grid2 mt4"><div><h2>Je vais apprendre à…</h2>{objs}</div><div><div class="card" style="background:#FCEAF1;border-color:#F0C3D5"><h3 style="margin-top:0">🗣️ On parle ensemble</h3>
<p>Qui sont ces personnes ? Elles ont quel âge ?</p><p>Dans ta langue, comment on dit « maman », « papa » ?</p><p>Tu peux parler de ta famille ou d'une personne importante pour toi.</p></div>
<div class="card mt4"><h3 style="margin-top:0">🔑 Les mots-clés</h3>{"".join(f'<span class="pill">{w}</span>' for w in ["la famille", "le père", "la mère", "le frère", "la sœur", "grand", "petit", "les cheveux", "les yeux", "gentil"])}</div></div></div>''', "Ouverture", levels=False)
    b.page("%%PLAN_DE_TRAVAIL%%", "Mon plan de travail", levels=False)

    # ---- BD
    def case(n, inner):
        return f'<div style="border:2.5px solid #1F2A44;border-radius:3mm;min-height:62mm;position:relative;padding:3mm;background:#FFFDF8"><div style="position:absolute;top:2mm;left:2mm;background:#1F2A44;color:#fff;width:6mm;height:6mm;border-radius:50%;font-size:9pt;font-weight:700;display:flex;align-items:center;justify-content:center">{n}</div>{inner}</div>'

    def bub(t):
        return f'<div class="bubble" style="margin:0 0 2mm 0;font-size:11pt">{t}</div>'
    photo = f'<div style="border:3px solid #fff;box-shadow:0 1mm 3mm rgba(0,0,0,.3);background:#E1EAFB;display:flex;gap:1mm;padding:2mm;transform:rotate(-3deg);width:max-content;margin:2mm auto">{"".join(face(size=40, **FAM[k]) for k in ["carlos", "lucia", "lucas", "mateo", "valentina"])}</div>'
    bd = '<div class="grid2" style="gap:3mm">' + "".join([
        case(1, f'<div class="flex top" style="margin-top:5mm">{avatar("mateo", 70, "rire")}<div>{bub("Regarde, Daria ! C&#39;est une photo de ma famille.")}</div></div>{photo}'),
        case(2, f'<div class="flex top" style="margin-top:5mm">{avatar("daria", 70, "surpris")}<div>{bub("Oh ! Qui est le grand homme avec une barbe ?")}</div></div><div class="flex top" style="justify-content:flex-end">{bub("C&#39;est mon père. Il s&#39;appelle Carlos.")}{avatar("mateo", 70, flip=True)}</div>'),
        case(3, f'<div class="flex top" style="margin-top:5mm">{avatar("mateo", 70)}<div>{bub("Et voici ma mère, Lucía. Elle a les cheveux longs et noirs.")}{bub("Elle est très gentille.")}</div></div>'),
        case(4, f'<div class="flex top" style="margin-top:5mm">{avatar("daria", 70, "pense")}<div>{bub("Tu as des frères et sœurs ?")}</div></div><div class="flex top" style="justify-content:flex-end">{bub("Oui, un grand frère, Lucas, et une petite sœur, Valentina.")}{avatar("mateo", 70, "rire", flip=True)}</div>'),
        case(5, f'<div class="flex top" style="margin-top:5mm">{avatar("mateo", 70)}<div>{bub("Et toi, Daria ? Ta famille est ici ?")}</div></div><div class="flex top" style="justify-content:flex-end">{bub("Ma mère et mon petit frère sont ici. Mon père est en Ukraine.")}{avatar("daria", 70, "triste", flip=True)}</div>'),
        case(6, f'<div class="flex top" style="margin-top:5mm">{avatar("mateo", 70, "sourire")}<div>{bub("Tu lui parles souvent ?")}</div></div><div class="flex top" style="justify-content:flex-end">{bub("Oui, tous les soirs, en vidéo ! 📱")}{avatar("daria", 70, "sourire", flip=True)}</div>'),
    ]) + '</div>'
    e = E("J'écoute et je regarde la BD : la photo de famille.", bd, ["ecoute", "regarde"], 1, "A",
          script="Lire la BD deux fois. Aborder le sujet avec délicatesse : certaines familles sont séparées. Insister : chacun parle de qui il veut (famille, famille d'accueil, amis, personne de confiance).", sol="Activité orale.")
    b.page(f'<h2>Découvrir · La photo de famille</h2>{e}', "Découvrir")
    e = E("Je réponds.", f'''<p>1. Comment s'appelle le père de Mateo ? {blank()}</p><p>2. Comment est la mère de Mateo ? {blank("xl")}</p><p>3. Mateo a combien de frères et sœurs ? {blank()}</p>
<p>4. Où est le père de Daria ? {blank()}</p><p>5. Daria parle à son père comment ? {blank("l")}</p>''', ["lis", "ecris"], 1, "B",
          sol="1. Carlos — 2. Elle a les cheveux longs et noirs, elle est gentille — 3. deux (un frère et une sœur) — 4. en Ukraine — 5. en vidéo, tous les soirs")
    e2 = E("Vrai ou faux ?", table(["", "Vrai", "Faux"], [[x, '<span class="chk"></span>', '<span class="chk"></span>'] for x in ["Le père de Mateo a une barbe.", "Lucas est le petit frère de Mateo.", "Valentina est la sœur de Mateo.", "La mère de Daria est en Belgique."]], ["130mm", "25mm", "25mm"]),
           ["lis", "coche"], 2, "B", sol="1. Vrai — 2. Faux (grand frère) — 3. Vrai — 4. Vrai")
    e3 = E("Défi ! Je montre une photo (ou un dessin) d'une personne importante pour moi et je la présente en 3 phrases.", '', ["parle", "montre"], 3, "A", sol="Production orale libre — respecter le choix de l'élève.")
    b.page(f'{e}{e2}{e3}<div class="astuce">💛 Toutes les familles sont différentes. Tu peux parler de ta famille, de ta famille d\'accueil, de tes amis ou d\'une famille que tu inventes.</div>', "Découvrir")

    # ---- Leçon 1 famille
    rows = [("le grand-père 👴", "la grand-mère 👵", "les grands-parents"), ("le père (papa)", "la mère (maman)", "les parents"), ("le frère", "la sœur", "les frères et sœurs"),
            ("le fils", "la fille", "les enfants"), ("l'oncle", "la tante", ""), ("le cousin", "la cousine", "les cousins"), ("le mari", "la femme", "")]
    l1 = lecon("La famille", f'''{table(["👨 masculin", "👩 féminin", "👨‍👩 pluriel"], [list(r) for r in rows], ["60mm", "60mm", "62mm"])}
<p class="mt2">J'ai <b>un</b> frère. Je n'ai pas <b>de</b> sœur. Je suis <b>fils / fille unique</b> (sans frère ni sœur).</p>
<p>Mon <b>grand</b> frère = plus âgé · ma <b>petite</b> sœur = plus jeune.</p>''')
    b.page(f'{l1}<h3>Regarde l\'arbre de la famille de Mateo :</h3>{tree()}', "Leçon 1")
    e = E("Je regarde l'arbre. Je complète.", '<div class="grid2">' + "".join(f'<p>{t}</p>' for t in [f"1. Carlos est le {blank()} de Mateo.", f"2. Rosa est la {blank()} de Mateo.", f"3. Valentina est la {blank()} de Mateo.", f"4. Diego est l'{blank()} de Mateo.",
           f"5. Pablo est le {blank()} de Mateo.", f"6. Ana est la {blank()} de Mateo.", f"7. Jorge et Rosa sont les {blank()} de Mateo.", f"8. Lucía est la {blank()} de Carlos."]) + '</div>', ["lis", "complete"], 1, "B",
          sol="1. père — 2. grand-mère — 3. sœur — 4. oncle — 5. cousin — 6. tante — 7. grands-parents — 8. femme")
    e2 = E("Qui suis-je ? Je lis et j'écris le prénom (arbre de la famille Ramírez).", '<div class="grid2">' + "".join(f'<div class="card"><p class="sm">{t}</p><p>→ {blank()}</p></div>' for t in ["J'ai 70 ans. Je suis le grand-père.", "J'ai 18 ans. Je suis le frère de Mateo.", "Je suis la mère de Pablo.", "Je suis le fils de Diego et Ana."]) + '</div>', ["lis", "ecris"], 2, "B",
           sol="Jorge · Lucas · Ana · Pablo")
    e3 = E("J'écoute Valentina présenter sa famille. J'entoure les bonnes réponses.", '<p>1. Valentina a <b>8 / 10 / 12</b> ans. 2. Son père s\'appelle <b>Carlos / Diego / Jorge</b>. 3. Elle a <b>un / deux / trois</b> frères. 4. Son cousin a <b>10 / 12 / 15</b> ans.</p>', ["ecoute", "entoure"], 2, "A",
           script="« Bonjour ! Je m'appelle Valentina, j'ai dix ans. Mon père s'appelle Carlos et ma mère s'appelle Lucía. J'ai deux frères : Lucas, il a dix-huit ans, et Mateo, il a quinze ans. Mon cousin Pablo a douze ans. Il est très drôle ! »",
           sol="1. 10 — 2. Carlos — 3. deux — 4. 12")
    e4 = E("Défi ! Je dessine mon arbre (ma famille, ou une famille inventée) avec 6 personnes minimum.", '<div class="card" style="height:62mm"></div>', ["dessine", "ecris"], 3, "C", sol="Production libre.")
    b.page(f'{e}{e2}{e3}{e4}', "S'entraîner")

    # ---- Leçon 2 possessifs
    l2 = lecon("Mon, ma, mes · ton, ta, tes · son, sa, ses", f'''{table(["", "masculin", "féminin", "pluriel"], [["à moi (je)", "<b>mon</b> père", "<b>ma</b> mère", "<b>mes</b> parents"], ["à toi (tu)", "<b>ton</b> frère", "<b>ta</b> sœur", "<b>tes</b> cousins"], ["à lui / à elle (il, elle)", "<b>son</b> oncle", "<b>sa</b> tante", "<b>ses</b> grands-parents"]], ["46mm", "45mm", "45mm", "46mm"])}
<div class="grid2 mt2"><div class="attention" style="margin:0">Devant une voyelle, <b>ma → mon</b> : <b>mon</b> amie, <b>mon</b> école (même si c'est féminin !)</div>
<div class="astuce" style="margin:0"><b>son / sa</b> dépend de l'objet, pas de la personne :<br>Mateo → <b>sa</b> mère · Daria → <b>son</b> père</div></div>''')
    e = E("J'entoure le bon mot.", '<div class="grid2">' + "".join(f'<p>{t}</p>' for t in ["1. <b>Mon / Ma / Mes</b> mère est gentille.", "2. <b>Mon / Ma / Mes</b> cousins habitent à Liège.", "3. Tu as <b>ton / ta / tes</b> cahier ?", "4. Daria parle à <b>son / sa / ses</b> père.",
          "5. Mateo aime <b>son / sa / ses</b> sœur.", "6. <b>Mon / Ma</b> amie s'appelle Fatou."]) + '</div>', ["entoure"], 1, "C", sol="1. Ma — 2. Mes — 3. ton — 4. son — 5. sa — 6. Mon (amie commence par une voyelle)")
    b.page(f'{l2}{e}', "Leçon 2")
    e = E("Je complète avec mon, ma ou mes.", '<p class="big">Voici ___ famille. ___ père s\'appelle Omar. ___ mère s\'appelle Leila. J\'ai deux frères : ___ frères ont 8 et 12 ans. ___ grand-mère habite avec nous. ___ école est à Namur.</p>', ["complete"], 1, "C",
          sol="ma · Mon · Ma · mes · Ma · Mon (école)")
    e2 = E("Je transforme : il ou elle → son, sa, ses.", '<p>1. Le père de Mateo → ___ père</p><p>2. La sœur de Mateo → ___ sœur</p><p>3. Les cousins de Daria → ___ cousins</p><p>4. Le frère de Fatou → ___ frère</p>', ["ecris"], 2, "C", sol="son · sa · ses · son")
    e3 = E("Je pose des questions à mon voisin avec ton, ta, tes. Il répond avec mon, ma, mes.", '<p class="sm">« Comment s\'appelle ta mère ? — Ma mère s\'appelle… » « Tes cousins habitent où ? — Mes cousins habitent… »</p>', ["parle", "duo"], 2, "A", sol="Production orale.")
    e4 = E("Défi ! Je trouve et je corrige les 3 erreurs.", '<div class="card big">Ma ami Yonas a un frère. Sa frère s\'appelle Abel. Ses mère est gentille.</div>' + lines(1), ["barre", "ecris"], 3, "C", sol="Mon ami · Son frère · Sa mère")
    b.page(f'{e}{e2}{e3}{e4}', "S'entraîner")

    # ---- Leçon 3 description
    phys = [("📏", "grand(e)"), ("🔻", "petit(e)"), ("🧒", "jeune"), ("👴", "âgé(e) / vieux"), ("💪", "fort(e)"), ("🧍", "mince")]
    chev = [("courts", "#3B2516"), ("longs", "#3B2516"), ("blonds", "#E8C26A"), ("bruns", "#5A3A1E"), ("noirs", "#111"), ("roux", "#B5651D"), ("bouclés", "#3B2516"), ("gris / blancs", "#BDBDBD")]
    yeux = [("bleus", "#1E5AA8"), ("verts", "#2E7D32"), ("marron", "#5A3A1E"), ("noirs", "#111")]
    car = [("😊", "gentil(le)"), ("😂", "drôle"), ("😌", "calme"), ("😳", "timide"), ("😎", "sympa"), ("😠", "sévère"), ("🤓", "intelligent(e)"), ("🏃", "sportif / sportive")]
    l3 = lecon("Décrire une personne", f'''<div class="grid2"><div><b>Il / Elle est…</b> (le corps)<div class="grid3 mt2">{"".join(f'<div class="card c" style="padding:1.5mm;background:#fff"><span class="emo s">{e}</span><div class="xs">{w}</div></div>' for e, w in phys)}</div></div>
<div><b>Il / Elle a les cheveux…</b><div class="grid4 mt2">{"".join(f'<div class="card c" style="padding:1mm;background:#fff"><div style="width:9mm;height:5mm;border-radius:2mm;background:{c};margin:auto"></div><div class="xs">{w}</div></div>' for w, c in chev)}</div>
<b class="mt2" style="display:block">Il / Elle a les yeux…</b><div class="grid4 mt2">{"".join(f'<div class="card c" style="padding:1mm;background:#fff"><div style="width:6mm;height:6mm;border-radius:50%;background:{c};margin:auto"></div><div class="xs">{w}</div></div>' for w, c in yeux)}</div></div></div>
<p class="mt2"><b>Il a une barbe 🧔 / une moustache · Elle a des lunettes 👓</b></p><b>Le caractère : Il / Elle est…</b><div class="grid4 mt2">{"".join(f'<div class="card c" style="padding:1.5mm;background:#fff"><span class="emo s">{e}</span><div class="xs">{w}</div></div>' for e, w in car)}</div>''')
    b.page(l3, "Leçon 3")
    e = E("Je regarde et je décris. Je complète.", '<div class="grid2">' + "".join(f'<div class="card flex">{face(size=60, **FAM[k])}<div class="sm" style="line-height:2">{t}</div></div>' for k, t in [
        ("jorge", f"Jorge est {blank()}. Il a une {blank()}. Il a les cheveux {blank()}."), ("ana", f"Ana a les cheveux {blank()} et {blank()}. Elle a les yeux {blank()}."),
        ("lucia", f"Lucía a les cheveux {blank()} et {blank()}."), ("diego", f"Diego a les cheveux {blank()}. Il a des {blank()}.")]) + '</div>', ["regarde", "complete"], 1, "C",
          sol="Jorge : âgé, barbe, gris/blancs · Ana : roux, bouclés, verts · Lucía : longs, noirs · Diego : courts (bruns), lunettes")
    e2 = E("J'écoute la description. Je trouve la bonne personne et j'écris son prénom.", '<div class="grid6">' + "".join(f'<div class="card c" style="padding:1mm">{face(size=46, **f)}<div class="xs"><b>{chr(65+i)}</b></div></div>' for i, (n, f) in enumerate(QUI[:6])) + '</div><p class="mt2">1. → lettre ___ &nbsp; 2. → lettre ___ &nbsp; 3. → lettre ___</p>',
           ["ecoute", "regarde"], 2, "A", script="1. Elle a les cheveux longs et blonds. Elle a les yeux bleus. — 2. Il n'a pas de cheveux. Il a une barbe noire. — 3. Elle a des lunettes et une queue de cheval noire.",
           sol="1. B (Lina) — 2. E (Omar) — 3. F (Nina)")
    b.page(f'{e}{e2}', "S'entraîner")

    # ---- Leçon 4 accord adjectif
    l4 = lecon("Masculin et féminin des adjectifs", f'''{table(["Règle", "Il… (masculin)", "Elle… (féminin)"], [["En général : + <b>e</b>", "grand · petit · blond · fort", "grand<b>e</b> · petit<b>e</b> · blond<b>e</b> · fort<b>e</b>"], ["Déjà un -e : pas de changement", "calme · timide · jeune · drôle · mince", "calme · timide · jeune · drôle · mince"], ["-il → -ille", "gentil", "genti<b>lle</b>"], ["-if → -ive", "sportif", "sporti<b>ve</b>"], ["Au pluriel : + s", "ils sont grand<b>s</b>", "elles sont grande<b>s</b>"]], ["58mm", "62mm", "62mm"])}
<div class="astuce" style="margin-bottom:0">👂 On entend souvent la différence : peti<b>t</b> (muet) / peti<b>te</b> (on entend « t ») ; gran<b>d</b> / gran<b>de</b>.</div>''')
    e = E("J'écris l'adjectif au féminin.", '<div class="grid3">' + "".join(f'<p>{a} → {blank()}</p>' for a in ["grand", "petit", "blond", "gentil", "calme", "sportif", "fort", "intelligent", "drôle"]) + '</div>', ["ecris"], 1, "C",
          sol="grande · petite · blonde · gentille · calme · sportive · forte · intelligente · drôle")
    b.page(f'{l4}{e}', "Leçon 4")
    e = E("J'accorde l'adjectif.", '<div class="grid2">' + "".join(f'<p>{t}</p>' for t in ["1. Ma mère est (petit) ______.", "2. Mon frère est (grand) ______.", "3. Ma sœur est (gentil) ______.", "4. Mes cousines sont (blond) ______.", "5. Mon oncle est (drôle) ______.", "6. Ta tante est (sportif) ______."]) + '</div>',
          ["complete"], 2, "C", sol="1. petite — 2. grand — 3. gentille — 4. blondes — 5. drôle — 6. sportive")
    e2 = E("Le jeu « Qui est-ce ? ». Je découpe les 12 cartes. Je choisis une personne en secret. Mon camarade pose des questions : « C'est une fille ? Il a des lunettes ? » Je réponds oui / non.", '<div class="grid6">' + "".join(f'<div class="card c" style="border-style:dashed;padding:1mm">{face(size=50, **f)}<div class="word" style="font-size:10pt">{n}</div></div>' for n, f in QUI) + '</div>',
           ["decoupe", "joue", "duo"], 2, "D", sol="Jeu oral : questions fermées avec le vocabulaire de la description.")
    e3 = E("Défi ! Je décris mon meilleur ami ou ma meilleure amie (physique + caractère, 5 phrases).", lines(5), ["ecris"], 3, "C", sol="Production libre ; vérifier les accords.")
    b.page(f'{e}{e2}{e3}', "S'entraîner")

    # ---- Leçon 5 être avoir complet
    l5 = lecon("Être et avoir : tous les pronoms", f'''<div class="grid2"><div class="card" style="background:#fff"><b style="color:#4A7BD1">ÊTRE</b><p>je suis<br>tu es<br>il / elle / on est<br><b>nous sommes</b><br><b>vous êtes</b><br><b>ils / elles sont</b></p></div>
<div class="card" style="background:#fff"><b style="color:#E4572E">AVOIR</b><p>j'ai<br>tu as<br>il / elle / on a<br><b>nous avons</b><br><b>vous avez</b><br><b>ils / elles ont</b></p></div></div>
<div class="grid2 mt2"><div class="astuce" style="margin:0"><b>nous</b> = moi + d'autres · <b>vous</b> = toi + d'autres (ou politesse) · <b>ils</b> = des garçons (ou mélange) · <b>elles</b> = que des filles · <b>on</b> = nous (à l'oral)</div>
<div class="attention" style="margin:0">👂 ils <b>s</b>ont [s] (être) ≠ ils_<b>o</b>nt [z] (avoir) — revois le module 2 !</div></div>''')
    e = E("Je complète avec être.", '<p class="big">Nous ______ en classe. Vous ______ frères ? Mes parents ______ gentils. Elles ______ sympas. On ______ contents.</p>', ["complete"], 1, "C", sol="sommes · êtes · sont · sont · est")
    e2 = E("Je complète avec avoir.", '<p class="big">Nous ______ deux chats. Vous ______ des cousins ? Ils ______ 12 ans. Elles ______ les yeux bleus. On ______ un test.</p>', ["complete"], 1, "C", sol="avons · avez · ont · ont · a")
    b.page(f'{l5}{e}{e2}', "Leçon 5")
    e = E("Être ou avoir ? J'entoure.", '<div class="grid2">' + "".join(f'<p>{t}</p>' for t in ["1. Nous <b>sommes / avons</b> 15 ans.", "2. Ils <b>sont / ont</b> grands.", "3. Vous <b>êtes / avez</b> des lunettes.", "4. Elles <b>sont / ont</b> sœurs.", "5. Mes grands-parents <b>sont / ont</b> 70 ans.", "6. Nous <b>sommes / avons</b> contents."]) + '</div>', ["entoure"], 2, "C",
          sol="1. avons — 2. sont — 3. avez — 4. sont — 5. ont — 6. sommes")
    e2 = E("J'écoute : ils sont ou ils ont ? Je coche.", table(["", "1", "2", "3", "4", "5", "6"], [["ils sont [s]"] + ['<span class="chk"></span>'] * 6, ["ils ont [z]"] + ['<span class="chk"></span>'] * 6], ["36mm"] + ["24mm"] * 6),
           ["ecoute", "coche"], 2, "A", script="Lire deux fois : 1. Ils ont un chien. — 2. Ils sont grands. — 3. Elles ont 13 ans. — 4. Elles sont gentilles. — 5. Ils sont belges. — 6. Ils ont faim.", sol="1. ont — 2. sont — 3. ont — 4. sont — 5. sont — 6. ont")
    e3 = E("Défi ! J'écris 4 phrases sur ma classe avec nous et ils / elles.", lines(4), ["ecris"], 3, "C", sol="Exemple : Nous sommes 14 élèves. Nous avons cours de français. Les filles sont sympas. Elles ont 13 ou 14 ans.")
    b.page(f'{e}{e2}{e3}', "S'entraîner")

    # ---- Documents de la vie
    fp = f'''<div class="doc" style="transform:rotate(-1deg);padding:6mm;background:#F2F9FF;border:2px solid #9AD3F5;text-align:center"><div style="font-size:30pt">👶🍼⭐</div>
<div style="font-family:'TeX Gyre Chorus';font-size:24pt;color:#1E5AA8">Bienvenue, Noah !</div><p class="big">Noah est né le <b>3 octobre 2026</b> à 7 h 45.</p><p>Il pèse 3,4 kg et mesure 51 cm.</p>
<p>Ses parents, <b>Sofia et Youssef</b>, et sa grande sœur <b>Lina</b> (6 ans) sont très heureux !</p><p class="sm muted">Rue des Lilas 5 · 4000 Liège</p></div>'''
    e = E("Je lis le faire-part de naissance. Je réponds.", f'''<p>1. Le bébé s'appelle comment ? {blank()}</p><p>2. Il est né quel jour ? À quelle heure ? {blank("l")}</p><p>3. Comment s'appellent ses parents ? {blank("l")}</p><p>4. Qui est Lina ? {blank("l")}</p><p>5. Le bébé pèse combien ? {blank()}</p>''',
          ["lis", "ecris"], 2, "B", sol="1. Noah — 2. le 3 octobre 2026 à 7 h 45 — 3. Sofia et Youssef — 4. sa grande sœur (6 ans) — 5. 3,4 kg")
    b.page(f'<span class="tag-doc">📄 DOCUMENT DE LA VIE</span><h2>Le faire-part de naissance</h2>{fp}<div class="mt4">{e}</div><div class="astuce">En Belgique, on envoie souvent un faire-part (une petite carte) pour annoncer une naissance ou un mariage. On offre parfois un cadeau au bébé.</div>', "Document de la vie")
    post = f'''<div class="doc" style="transform:none;border:1px solid #ddd;border-radius:4mm;padding:4mm;max-width:150mm;margin:auto"><div class="flex">{avatar("fatou", 44, "rire")}<div><b>Fatou C.</b><div class="xs muted">MaClasse · il y a 2 h</div></div></div>
<div style="background:#FFF3C4;border-radius:3mm;padding:4mm;margin:3mm 0;display:flex;gap:2mm;justify-content:center">{face("fonce", "#111", "long", False, False, size=56, shirt="#E4572E")}{face("fonce", "#111", "court", True, False, size=56, shirt="#2E4057")}{face("fonce", "#111", "boucle", size=46, shirt="#2BA88F")}{avatar("fatou", 56, "rire")}</div>
<p>Dimanche en famille ! ❤️ Ma mère <b>Aminata</b> est grande et très drôle. Mon oncle <b>Ibrahima</b> a une barbe, il est un peu sévère mais gentil 😄. Mon petit cousin <b>Sekou</b> a 5 ans, il a les cheveux bouclés. On mange du riz au poisson ! 🍚🐟</p><div class="xs muted">❤️ 21 · 💬 6 commentaires</div></div>'''
    e = E("Je lis le message de Fatou. Je relie la personne et la description.", post + relie(["Aminata", "Ibrahima", "Sekou"], ["5 ans, cheveux bouclés", "grande et drôle", "barbe, un peu sévère"]), ["lis", "relie"], 2, "B",
          sol="Aminata → grande et drôle (la mère) · Ibrahima → barbe, un peu sévère (l'oncle) · Sekou → 5 ans, cheveux bouclés (le cousin)")
    e2 = E("Défi ! J'écris un commentaire au message de Fatou (2 phrases).", lines(2), ["ecris"], 3, "C", sol="Exemple : Super photo ! Ta mère est belle. Moi aussi, j'aime le riz au poisson !")
    b.page(f'<span class="tag-doc">📄 DOCUMENT DE LA VIE</span><h2>Un message sur un réseau social</h2>{e}{e2}', "Document de la vie")

    # ---- FLSco : décrire une image
    sc = f'''<div class="card" style="background:#E8F6F2;padding:3mm"><svg viewBox="0 0 180 80" width="100%"><rect x="0" y="0" width="180" height="80" fill="#DFF2FF"/><rect x="0" y="55" width="180" height="25" fill="#8BC34A"/><circle cx="160" cy="14" r="8" fill="#FFD166"/>
<rect x="20" y="38" width="40" height="4" fill="#8a6b47"/><text x="22" y="36" font-size="9">🧺</text><text x="100" y="70" font-size="12">⚽</text><text x="6" y="54" font-size="16">🌳</text><text x="150" y="58" font-size="16">🌳</text><text x="125" y="40" font-size="9">🐕</text></svg>
<div class="flex" style="justify-content:space-around;margin-top:-22mm">{face(size=48, **FAM["rosa"])}{face(size=48, **FAM["jorge"])}{face(size=40, **FAM["valentina"])}{face(size=44, **FAM["pablo"])}</div></div>'''
    l6 = lecon("Décrire une image : la méthode", '''<p>1️⃣ <b>Je dis ce que c'est :</b> C'est une photo / un dessin de… · 2️⃣ <b>Je dis où :</b> dans un parc, à la maison… · 3️⃣ <b>Je dis qui :</b> Il y a… personnes.<br>
4️⃣ <b>Je décris :</b> À gauche, … À droite, … Au milieu, … Devant, derrière · 5️⃣ <b>Je donne mon avis :</b> J'aime cette image parce que…</p>''')
    e = E("Je décris l'image avec la méthode (oral, puis 5 phrases écrites).", sc + lines(5), ["regarde", "parle", "ecris"], 2, "C",
          sol="C'est un dessin d'une famille dans un parc. Il y a quatre personnes. À gauche, il y a la grand-mère, elle a des lunettes. Le grand-père a une barbe. Il y a deux enfants. Il y a un chien, un ballon et des arbres. Il fait beau.")
    b.page(f'<span class="tag-doc">🎒 FRANÇAIS DE L\'ÉCOLE</span>{l6}{e}', "Consignes & école")

    # ---- Sons
    e = E("[f] et [v], [ʃ] et [ʒ]. J'écoute et je répète.", '''<div class="grid2"><div class="card c"><div class="huge">[f] / [v]</div><p>fille 👧 / ville 🏙️ · fer / vert · neuf / neuve</p><p class="sm muted">Les dents touchent la lèvre. [v] vibre !</p></div>
<div class="card c"><div class="huge">[ʃ] ch / [ʒ] j, ge</div><p>chat 🐱 / jambe 🦵 · cheveux / jeune · bouche / rouge</p><p class="sm muted">Comme pour dire « chut » 🤫. [ʒ] vibre !</p></div></div>''', ["ecoute", "repete"], 1, "A",
          script="Main sur la gorge : pas de vibration pour [f] et [ʃ], vibration pour [v] et [ʒ]. Paires : fille/ville, fou/vous, chou/joue, cheveux/jeu.", sol="Activité orale.")
    e2 = E("J'écoute. Je coche le son.", table(["", "1", "2", "3", "4", "5", "6", "7", "8"], [["[f]"] + ['<span class="chk"></span>'] * 8, ["[v]"] + ['<span class="chk"></span>'] * 8, ["[ʃ]"] + ['<span class="chk"></span>'] * 8, ["[ʒ]"] + ['<span class="chk"></span>'] * 8], ["20mm"] + ["20mm"] * 8),
           ["ecoute", "coche"], 2, "A", script="Lire : 1. frère — 2. cheveux — 3. jeune — 4. vous — 5. fille — 6. chat — 7. village — 8. joue", sol="1. [f] — 2. [ʃ] — 3. [ʒ] — 4. [v] — 5. [f] — 6. [ʃ] — 7. [v] (+ [ʒ] à la fin) — 8. [ʒ]")
    e3 = E("Virelangue ! Je le dis de plus en plus vite.", '<div class="card c big">« Un chasseur sachant chasser doit savoir chasser sans son chien. »</div>', ["repete", "parle"], 3, "A", sol="Activité orale (virelangue traditionnel).")
    b.page(f'<h2>J\'écoute bien · [f] / [v] · [ʃ] / [ʒ]</h2>{e}{e2}{e3}', "Sons")

    # ---- Révise M1-M3
    e = E("🔁 Module 3 · J'écris la date de l'anniversaire d'une personne de ma famille.", f'<p>L\'anniversaire de {blank()} , c\'est le {blank("l")}.</p>', ["ecris"], 1, "C", sol="Réponse personnelle (le + numéro + mois).")
    e2 = E("🔁 Module 3 · Quelle heure est-il ?", '<p>8 h 30 → ____________ · 12 h → ____________ · 17 h 15 → ____________</p>', ["ecris"], 2, "C", sol="huit heures trente · midi · dix-sept heures quinze")
    e3 = E("🔁 Module 2 · Il y a… Je décris l'image du parc (p. précédente) en 2 phrases.", lines(2), ["ecris"], 1, "C", sol="Il y a un chien. Il y a des arbres et un ballon.")
    e4 = E("🔁 Module 1 · Les nombres. J'écris l'âge des membres de la famille Ramírez en lettres.", '<p>Diego : ______ · Lucía : ______ · Lucas : ______ · Pablo : ______</p>', ["ecris"], 2, "C", sol="quarante · quarante-deux · dix-huit · douze")
    b.page(f'<h2>🔁 Je révise les modules 1 à 3</h2>{e}{e2}{e3}{e4}', "Je révise")

    # ---- Ateliers
    e = E("Le portrait parlé : je décris une personne de la classe (sans dire son nom). Les autres devinent.", '<p class="sm">« C\'est une fille. Elle est grande. Elle a les cheveux longs et noirs. Elle est drôle… »</p>', ["parle", "groupe"], 1, "A", sol="Jeu oral.")
    e2 = E("Interview « famille » : je pose 5 questions à un camarade et je note.", table(["Question", "Réponse"], [[q, ""] for q in ["Tu as des frères et sœurs ?", "Comment ils s'appellent ?", "Ils ont quel âge ?", "Comment est ton meilleur ami ?", "Qui est la personne la plus drôle de ta famille ?"]], ["90mm", "92mm"]).replace("<td></td>", '<td style="height:9mm"></td>'),
           ["parle", "ecris", "duo"], 2, "A", sol="Réponses personnelles (l'élève peut refuser de parler de sa famille et parler d'amis).")
    b.page(f'<span class="atl A" style="font-size:12pt;padding:1.5mm 4mm">{ATELIERS["A"]}</span><h2 class="mt2">Atelier · Écouter et parler</h2>{e}{e2}', "Atelier")
    txt = '''<div class="card" style="background:#FFFDF8;font-size:11pt;line-height:1.6"><b>Ma famille</b> — par Yonas<br>Je m'appelle Yonas. J'ai 14 ans. J'habite à Namur avec mon oncle Tesfay et ma tante Saba. Mon oncle est grand et calme. Il a une petite barbe. Il travaille dans un magasin. Ma tante est petite et très gentille. Elle a les cheveux longs et noirs. Elle fait de bons repas ! Ils ont une fille, ma cousine Ruth. Elle a 6 ans. Elle est drôle et elle parle beaucoup. Mes parents et mes deux sœurs habitent en Éthiopie. Je leur téléphone le dimanche. Ma famille me manque, mais ici, je suis bien.</div>'''
    e = E("Je lis le texte de Yonas.", txt, ["lis"], 1, "B")
    e2 = E("Je réponds.", f'<div class="grid2"><p>1. Yonas habite avec qui ? {blank("l")}</p><p>2. Comment est son oncle ? {blank("l")}</p><p>3. Qui est Ruth ? {blank("l")}</p><p>4. Où sont ses parents ? {blank()}</p></div><p>5. ●●● Comment se sent Yonas ? Je cite une phrase du texte. {blank("xl")}</p>',
            ["lis", "ecris"], 2, "B", sol="1. avec son oncle Tesfay et sa tante Saba (et sa cousine) — 2. grand et calme, avec une petite barbe — 3. sa cousine (6 ans) — 4. en Éthiopie — 5. « Ma famille me manque, mais ici, je suis bien. »")
    b.page(f'<span class="atl B" style="font-size:12pt;padding:1.5mm 4mm">{ATELIERS["B"]}</span><h2 class="mt2">Atelier · Lire</h2>{e}{e2}', "Atelier")
    e = E("Je recopie la description.", '<div class="card" style="background:#F7F8FB"><p class="big">Ma sœur s\'appelle Valentina. Elle a dix ans. Elle est petite et drôle. Elle a les cheveux noirs.</p></div>' + lines(3, True), ["recopie"], 1, "C", sol="Copie.")
    e2 = E("Je présente une personne (complète).", f'<div class="card" style="line-height:2.3">Je te présente {blank("l")}. C\'est mon / ma {blank()}. Il / Elle a {blank("s")} ans. Il / Elle est {blank("l")}. Il / Elle a les cheveux {blank()} et les yeux {blank()}. Il / Elle est très {blank()}.</div>', ["ecris", "complete"], 2, "C", sol="Production personnelle.")
    e3 = E("Défi ! J'écris un texte « Ma famille » (comme Yonas) : 8 phrases.", lines(7), ["ecris"], 3, "C", sol="Production libre.")
    b.page(f'<span class="atl C" style="font-size:12pt;padding:1.5mm 4mm">{ATELIERS["C"]}</span><h2 class="mt2">Atelier · Écrire</h2>{e}{e2}{e3}', "Atelier")
    fam7 = [("👴", "Grand-père"), ("👵", "Grand-mère"), ("👨", "Père"), ("👩", "Mère"), ("👦", "Fils"), ("👧", "Fille")]
    cards = "".join(f'<div style="border:2px solid #1F2A44;border-radius:3mm;height:36mm;display:flex;flex-direction:column;align-items:center;justify-content:center;background:{c}"><span style="font-size:28pt">{e}</span><b class="sm">{n}</b><span class="xs">famille {f}</span></div>' for f, c in [("Martin", "#FFE5DC"), ("Diallo", "#E1EAFB"), ("Popescu", "#DDF3EC")] for e, n in fam7)
    e = E("Le jeu des 7 familles (version 3 familles). Je découpe. On distribue. Je demande : « Dans la famille Diallo, je voudrais la mère ! » Celui qui a une famille complète la pose.", f'<div class="grid6">{cards}</div>', ["decoupe", "joue", "groupe"], 2, "D",
          sol="Jeu oral : « Dans la famille…, je voudrais le / la… » — « Bonne pioche ! »")
    b.page(f'<span class="atl D" style="font-size:12pt;padding:1.5mm 4mm">{ATELIERS["D"]}</span><h2 class="mt2">Atelier · Jouer</h2>{e}', "Atelier")

    # ---- Alpha
    letter_page(b, E, "f", "[f]", [("🍓", "fraise"), ("👧", "fille"), ("🔥", "feu"), ("🌸", "fleur")], "tltkthlt",
                [("🍓", "fraise", 1), ("👧", "fille", 1), ("🚲", "vélo", 0), ("🔥", "feu", 1), ("🌸", "fleur", 1), ("🐱", "chat", 0), ("🍅", "tomate", 0), ("☕", "café", 1)], MC)
    letter_page(b, E, "v", "[v]", [("🚲", "vélo"), ("🍷", "verre"), ("🐄", "vache"), ("🏙️", "ville")], "wuywnuyw",
                [("🚲", "vélo", 1), ("🐄", "vache", 1), ("🍓", "fraise", 0), ("🏙️", "ville", 1), ("👧", "fille", 0), ("✈️", "avion", 1), ("🔥", "feu", 0), ("📖", "livre", 1)], MC)
    letter_page(b, E, "ch", "[ʃ]", [("🐱", "chat"), ("🍫", "chocolat"), ("🪑", "chaise"), ("🐄", "vache")], "cjshcjsh",
                [("🐱", "chat", 1), ("🍫", "chocolat", 1), ("🦵", "jambe", 0), ("🪑", "chaise", 1), ("🐄", "vache", 1), ("🧃", "jus", 0), ("🍓", "fraise", 0), ("🐶", "chien", 1)], MC)
    letter_page(b, E, "j", "[ʒ]", [("🧃", "jus"), ("🦵", "jambe"), ("🟡", "jaune"), ("👗", "jupe")], "igyigyiq",
                [("🧃", "jus", 1), ("🦵", "jambe", 1), ("🐱", "chat", 0), ("🟡", "jaune", 1), ("👗", "jupe", 1), ("🪑", "chaise", 0), ("🎮", "jeu", 1), ("🚲", "vélo", 0)], MC)
    e = E("Je lis les syllabes.", syll_table(["f", "v", "ch", "j"]), ["lis"], 1, "P", alpha=True, script="Lecture en ligne, en colonne, au hasard. Attention ch = 2 lettres, 1 son.", sol="fa fi fo fu fé / va vi vo vu vé / cha chi cho chu ché / ja ji jo ju jé")
    words = [("🐱", "chat"), ("🍫", "cho-co-lat"), ("🚲", "vé-lo"), ("🐄", "va-che"), ("🧃", "jus"), ("👗", "ju-pe"), ("☕", "ca-fé"), ("🦶", "pied")]
    words[7] = ("🎲", "dé")
    e2 = E("Je lis les mots de la famille et de la maison.", '<div class="grid4">' + "".join(f'<div class="card c"><span class="emo s">{e}</span><div class="huge" style="font-size:17pt">{w.replace("-", "<span style=color:#E4572E>·</span>")}</div></div>' for e, w in [("👨", "pa-pa"), ("👩", "ma-man"), ("👧", "fi-lle"), ("🐱", "chat"), ("🍫", "cho-co-lat"), ("🐄", "va-che"), ("🧃", "jus"), ("👗", "ju-pe")]) + '</div>',
           ["lis"], 1, "P", alpha=True, script="Lire avec l'élève syllabe par syllabe. Note : « maman » contient « an » (vu plus tard) : le lire globalement.", sol="papa · maman · fille · chat · chocolat · vache · jus · jupe")
    b.page(AL.format(t="Je lis") + e + e2, "★ Alpha", color=MC)
    e = E("Je lis les phrases et je dessine.", '<div class="grid2">' + "".join(f'<div class="card"><p class="big">{t}</p><div style="height:22mm;border:1.5px dashed #b9bfcc;border-radius:2mm"></div></div>' for t in ["Papa a un vélo.", "Le chat a du lait.", "Ma sœur a une jupe.", "Fatou a du chocolat."]) + '</div>', ["lis", "dessine"], 2, "B", alpha=True, sol="Lecture et dessins.")
    e2 = E("Dictée.", guide_lines(2, 20), ["ecoute", "ecris"], 2, "P", alpha=True, script="Dicter : fa — vi — cho — ju — vélo — chat — papa", sol="fa vi cho ju vélo chat papa")
    e3 = E("J'écris : mon papa, ma maman (je recopie).", trace("papa", 26, 2) + trace("maman", 26, 2), ["recopie"], 1, "C", alpha=True, sol="Copie.")
    b.page(AL.format(t="Je lis des phrases, j'écris") + e + e2 + e3, "★ Alpha", color=MC)

    # ---- Tâche finale
    e = E("Mon affiche « Ma famille » (ou « Les personnes importantes pour moi »). Je dessine ou je colle des photos. J'écris 2 phrases par personne.", '<div style="border:4px solid ' + MC + ';border-radius:6mm;padding:4mm;height:150mm;background:#FFFDF8;display:grid;grid-template-columns:1fr 1fr;gap:4mm">' + "".join(f'<div style="border:2px dashed #b9bfcc;border-radius:3mm;padding:2mm"><div style="height:28mm"></div>{lines(2)}</div>' for _ in range(4)) + '</div>',
          ["dessine", "ecris", "colle"], 2, "C", sol="Évaluation avec la grille.")
    b.page(f'''<div style="background:#1F2A44;color:#fff;margin:-17mm -14mm 5mm -14mm;padding:15mm 14mm 5mm 14mm"><div style="font-size:11pt;font-weight:700;opacity:.8">🎯 TÂCHE FINALE</div><div style="font-size:26pt;font-weight:800">L'affiche de ma famille</div>
<div class="sm" style="opacity:.9">Je présente 4 personnes (famille, amis, famille d'accueil, ou famille inventée) : qui c'est, son âge, sa description, son caractère.</div></div>{e}''', "Tâche finale", levels=False)
    chk = table(["Je vérifie :", "✅"], [[x, '<span class="chk"></span>'] for x in ["4 personnes avec un dessin ou une photo.", "J'utilise mon / ma / mes.", "J'accorde les adjectifs (grand / grande).", "J'utilise il a / elle est correctement.", "Je présente mon affiche à l'oral (1 minute)."]], ["160mm", "22mm"])
    e = E("Je prépare ma présentation orale : « Voici mon… Il s'appelle… »", lines(5), ["ecris", "parle"], 2, "A", sol="Oral évalué avec la grille.")
    b.page(f'{chk}{e}', "Tâche finale", levels=False)

    e = E("J'écris le mot de la famille.", '<p>Le père de mon père : ________ · La sœur de ma mère : ________ · Le fils de mon oncle : ________ · La fille de mes parents : ________</p>', ["ecris"], 2, "C", sol="mon grand-père · ma tante · mon cousin · ma sœur (ou moi !)")
    e2 = E("Mon, ma ou mes ? / J'accorde.", '<p>___ frère est (grand) ______. ___ sœurs sont (petit) ______. ___ amie est (gentil) ______.</p>', ["complete"], 2, "C", sol="Mon / grand · Mes / petites · Mon / gentille")
    e3 = E("Être ou avoir ?", '<p>Nous ______ cousins. Vous ______ trois enfants ? Ils ______ blonds. Elles ______ 10 ans.</p>', ["complete"], 1, "C", sol="sommes · avez · sont · ont")
    e4 = E("Défi ! Je corrige les 4 erreurs.", '<div class="card big">Ma père est grande. Il a les cheveux court. Mes sœur sont drôles. Ils ont gentils.</div>' + lines(2), ["barre", "ecris"], 3, "C", sol="Mon père · grand · courts · Mes sœurs · Ils sont gentils")
    b.page(f'<h2>🔁 Je révise tout le module</h2>{e}{e2}{e3}{e4}', "Je révise")

    # ---- Test
    head = f'''<div style="background:#1F2A44;color:#fff;margin:-17mm -14mm 4mm -14mm;padding:14mm 14mm 4mm 14mm;display:flex;justify-content:space-between;align-items:flex-end"><div><div style="font-size:11pt;font-weight:700;opacity:.8">📝 TEST · MODULE 4</div><div style="font-size:24pt;font-weight:800">Ma famille et moi</div></div><div class="sm" style="text-align:right">Prénom : ......................................<br>Date : ........ / ........ / ............</div></div>'''
    Q = [("La mère de ma mère, c'est ma :", ["tante", "sœur", "cousine", "grand-mère"]), ("Le frère de mon père, c'est mon :", ["oncle", "cousin", "grand-père", "fils"]),
         ("Le fils de mon oncle, c'est mon :", ["frère", "cousin", "père", "neveu… non"]), ("____ mère est gentille.", ["Mon", "Mes", "Ma", "Ta mes"]),
         ("____ parents habitent à Namur.", ["Mon", "Ma", "Mes", "Son"]), ("____ amie s'appelle Lina.", ["Mon", "Ma", "Mes", "Sa"]),
         ("Mateo aime ____ sœur.", ["son", "ses", "mon", "sa"]), ("Ma sœur est ____.", ["petit", "petits", "petite", "petites"]),
         ("Mon oncle est ____.", ["gentille", "gentil", "gentils", "gentilles"]), ("Elle a les cheveux ____.", ["long", "longue", "longs", "longues"]),
         ("Nous ____ 15 ans.", ["sommes", "avons", "êtes", "ont"]), ("Ils ____ grands.", ["ont", "sont", "avons", "êtes"]),
         ("Vous ____ des frères ?", ["êtes", "avez", "ont", "sont"]), ("Il a une barbe =", ["👓", "🧔", "👧", "👶"]),
         ("Le contraire de « grand » :", ["vieux", "jeune", "petit", "mince"]), ("« Il rit beaucoup », il est :", ["timide", "sévère", "calme", "drôle"]),
         ("Sur le faire-part, le bébé s'appelle Noah. Noah est :", ["le grand-père", "le bébé", "la sœur", "le père"]), ("J'entends [ʃ] comme dans « chat » :", ["jupe", "cheveux", "fille", "vélo"]),
         ("🔁 Le jour après jeudi :", ["mercredi", "samedi", "vendredi", "dimanche"]), ("🔁 Il est 8 h 30 =", ["huit heures trente", "trente heures huit", "huit heures trois", "dix-huit heures"])]
    Q[2] = (Q[2][0], ["frère", "cousin", "père", "oncle"])
    Q[3] = (Q[3][0], ["Mon", "Mes", "Ma", "Ton"])
    key = "1-D, 2-A, 3-B, 4-C, 5-C, 6-A, 7-D, 8-C, 9-B, 10-C, 11-B, 12-B, 13-B, 14-B, 15-C, 16-D, 17-B, 18-B, 19-C, 20-A"
    p1 = "".join(qcm_line(i + 1, q, o) for i, (q, o) in enumerate(Q[:10]))
    p2 = "".join(qcm_line(i + 11, q, o) for i, (q, o) in enumerate(Q[10:]))
    b.page(f'{head}<div class="flex" style="justify-content:space-between"><h2 style="margin:0">Partie A · Je choisis la bonne réponse</h2><span class="score">…… / 20</span></div>{p1}', "Test", levels=False)
    b.page(p2, "Test", levels=False)
    b.page(f'''<div class="flex" style="justify-content:space-between"><h2 style="margin:0">Partie B · J'écris</h2><span class="score">…… / 10</span></div>
<h3>B1. Je décris la personne : 4 phrases (physique). (… / 4)</h3><div class="flex top">{face(size=90, **FAM["ana"])}<div class="grow">{lines(4, True)}</div></div>
<h3>B2. Je présente une personne importante pour moi : 6 phrases (qui, âge, physique, caractère). (… / 6)</h3>{lines(6, True)}
<div class="flex mt4" style="justify-content:space-between"><h2 style="margin:0">Partie C · Je parle avec la prof</h2><span class="score">…… / 10</span></div>
{table(["Je sais…", "Points", "✅"], [["présenter ma famille (ou des personnes proches)", "/ 4", ""], ["décrire une personne de la classe", "/ 3", ""], ["décrire une image (méthode)", "/ 3", ""]], ["120mm", "30mm", "32mm"])}
<div class="card mt2 c"><span class="huge">TOTAL : …… / 40</span></div>''', "Test", levels=False)
    ta = f'''<div style="background:#FFD166;margin:-17mm -14mm 4mm -14mm;padding:14mm 14mm 4mm 14mm"><div style="font-size:11pt;font-weight:800">★ ALPHA · 📝 TEST · MODULE 4</div><div style="font-size:22pt;font-weight:800">Ma famille et moi</div></div>
<h3>1. J'écoute et j'entoure la syllabe. (… / 4)</h3><div class="grid4">{"".join(f'<div class="card c big" style="font-weight:700;white-space:nowrap">{r}</div>' for r in ["fa fo fi", "va vu vé", "cha cho chi", "ja ju jo"])}</div>
<h3>2. Je lis et je relie. (… / 4)</h3>{relie([f'<b class="big">{w}</b>' for w in ["chat", "vélo", "jus", "papa"]], ['<span class="emo s">👨</span>', '<span class="emo s">🧃</span>', '<span class="emo s">🐱</span>', '<span class="emo s">🚲</span>'])}
<h3>3. Dictée. (… / 4)</h3>{guide_lines(1, 22)}
<h3>4. Je montre et je dis (oral) : le père, la mère, le frère, la sœur. (… / 4)</h3><div class="grid4">{"".join(f'<div class="card c">{face(size=60, **FAM[k])}</div>' for k in ["carlos", "lucia", "lucas", "valentina"])}</div>
<h3>5. Je décris (oral) : grand, petit, cheveux, lunettes. (… / 4)</h3><div class="card c">{face(size=70, **FAM["diego"])} {face(size=70, **FAM["ana"])}</div><div class="card c mt2"><span class="huge">TOTAL : …… / 20</span></div>'''
    b.page(ta, "★ Alpha · Test", levels=False)
    items = ["Je sais nommer les membres de la famille.", "Je sais présenter ma famille ou mes proches.", "Je sais dire mon, ma, mes / ton, ta, tes / son, sa, ses.", "Je sais décrire le physique d'une personne.", "Je sais décrire le caractère.",
             "Je sais accorder l'adjectif (grand / grande).", "Je sais conjuguer être et avoir avec tous les pronoms.", "Je sais lire un faire-part.", "Je sais décrire une image avec la méthode.", "★ Je sais lire fa, vi, cho, ju, chat, vélo…"]
    tb = table(["", "😀 Oui !", "🙂 Un peu", "😕 Pas encore", "La prof"], [[x, '<span class="chk"></span>', '<span class="chk"></span>', '<span class="chk"></span>', ""] for x in items], ["92mm", "20mm", "20mm", "24mm", "26mm"])
    b.page(f'<h2>✅ Je sais faire</h2>{tb}<div class="grid2 mt4"><div class="card"><b>Ce que j\'aime :</b>{lines(2)}</div><div class="card"><b>C\'est difficile :</b>{lines(2)}</div></div>', "Je sais faire", levels=False)
    mots = [("👨‍👩‍👧", "la famille"), ("👨", "le père"), ("👩", "la mère"), ("👦", "le frère"), ("👧", "la sœur"), ("👴", "le grand-père"), ("👵", "la grand-mère"), ("🧔", "l'oncle"), ("👩‍🦰", "la tante"), ("🧒", "le cousin"),
            ("👶", "le bébé"), ("👫", "les parents"), ("🧒", "les enfants"), ("📏", "grand(e)"), ("🔻", "petit(e)"), ("💇", "les cheveux"), ("👁️", "les yeux"), ("🧔", "la barbe"), ("👓", "les lunettes"), ("😊", "gentil(le)"),
            ("😂", "drôle"), ("😌", "calme"), ("😳", "timide"), ("😠", "sévère"), ("🏃", "sportif / sportive"), ("🧑", "jeune"), ("👴", "âgé(e)"), ("❤️", "aimer"), ("🤝", "l'ami(e)"), ("📸", "la photo")]
    half = len(mots) // 2
    mt = lambda lst: table(["", "Français", "Dans ma langue"], [[f'<span style="font-size:13pt">{e}</span>', f"<b>{w}</b>", ""] for e, w in lst], ["12mm", "40mm", "36mm"]).replace("<td>", '<td style="padding:1.6mm 2mm">')
    b.page(f'<h2>📒 Mes mots du module 4</h2><div class="grid2">{mt(mots[:half])}{mt(mots[half:])}</div>', "Mes mots", levels=False)

    plan_de_travail(b, E, 4, ["La famille", "Mon, ma, mes…", "Décrire une personne", "Masculin / féminin des adjectifs", "Être et avoir : tous les pronoms", "Décrire une image"], "☐ Affiche (4 personnes)<br>☐ Présentation orale")
    if render:
        to_pdf(b.html(), '/home/claude/syllabus/out/V1_M4_eleve.pdf')
    pg, exs = helpers(b, E)
    A = b.marks["★ Alpha"]
    days = [("1", "Collectif", f"Ouverture · BD ({pg('Découvrir')})", f"Alpha : f (p. {A[0]})"), ("2", "Collectif + rotation", f"📌 Leçon 1 la famille + arbre ({pg('Leçon 1')})", f"Alpha : v (p. {A[1]})"),
            ("3", "Rotation", f"📌 Leçon 2 possessifs ({pg('Leçon 2')})", f"Alpha : ch (p. {A[2]})"), ("4", "Collectif", f"📌 Leçon 3 décrire ({pg('Leçon 3')}) · portrait parlé", f"Alpha : j (p. {A[3]})"),
            ("5", "Rotation", f"📌 Leçon 4 accords ({pg('Leçon 4')}) · Qui est-ce ?", f"Alpha : syllabes (p. {A[4]})"), ("6", "Rotation", f"📌 Leçon 5 être/avoir ({pg('Leçon 5')})", f"Alpha : phrases (p. {A[5]})"),
            ("7", "Collectif", f"Documents de la vie ({pg('Document de la vie')}) · décrire une image ({pg('Consignes & école')})", "Alpha : révision"), ("8", "Ateliers", f"Ateliers ({pg('Atelier')}) · sons ({pg('Sons')}) · 🔁 révision", "Alpha : jeu des familles"),
            ("9", "Seul puis oral", f"Tâche finale ({pg('Tâche finale')})", "Alpha : affiche avec dictée à l'adulte"), ("10", "Seul", f"Test ({pg('Test')}) · je sais faire · mes mots", f"Alpha : test ({pg('★ Alpha · Test')})")]
    rot = [["🎧 Écouter-Parler", "Portrait parlé · interview", "20 min", "—"], ["📖 Lire", "Texte de Yonas", "20 min", "Oui"], ["✏️ Écrire", "Copie · présentation à compléter · texte libre", "20 min", "● oui · ●●● prof"],
           ["🧩 Jouer", "Jeu des familles · Qui est-ce ?", "20 min", "Entre joueurs"], ["👩‍🏫 Table d'appui", "Alpha : f v ch j · autres : accords, possessifs", "20 min", "—"]]
    ev1 = '''<h3>Partie B · Écrit (10 points)</h3><p class="sm"><b>B1</b> (1 pt par phrase) : <span class="sol">Elle a les cheveux roux et bouclés. Elle a les yeux verts. Elle est jeune. Elle a un t-shirt vert.</span> · <b>B2</b> : qui (1), âge (1), physique (2), caractère (1), possessifs et accords (1).</p>
<h3>Partie C · Oral (10 points)</h3><p class="sm">Famille / proches : 4 personnes avec lien et âge (4) · description d'un camarade : 3 traits corrects (3) · image : méthode en 5 étapes (3).</p>
<h3>Test ★ Alpha</h3><p class="sm"><b>Ex. 1, dire :</b> <span class="sol">fo · vé · chi · ju</span> · <b>Ex. 2 :</b> <span class="sol">chat–🐱, vélo–🚲, jus–🧃, papa–👨</span> · <b>Ex. 3, dicter :</b> <span class="sol">fa, cho, vélo, chat</span>.</p>'''
    ev2 = f'''<h2>Grille · tâche finale « L'affiche de ma famille »</h2>{table(["Critère", "Très bien", "Bien", "À retravailler", "Points"], [["<b>Contenu</b> : 4 personnes, lien, âge, description, caractère", "Complet", "Partiel", "Insuffisant", "/ 6"], ["<b>Langue</b> : possessifs, accords, être/avoir", "Correct", "Quelques erreurs", "Beaucoup", "/ 6"], ["<b>Oral</b> : 1 minute, clair", "Fluide", "Hésitant", "Bloqué", "/ 5"], ["<b>Soin</b>", "Très soigné", "Correct", "Peu soigné", "/ 3"]], ["64mm", "32mm", "32mm", "32mm", "22mm"])}
<div class="attention mt4"><b>⚠️ Point de vigilance :</b> pour des élèves primo-arrivants, la famille peut être un sujet douloureux (séparation, deuil, mineurs non accompagnés). Toujours proposer le choix : famille, famille d'accueil, amis, éducateurs, ou famille inventée (la famille Ramírez peut servir de modèle). Ne jamais exiger de photo.</div>
<h2 class="mt4">Différencier et remédier</h2>{table(["Difficulté", "Remédiation"], [["son / sa", "Rappel : on regarde le mot qui suit (son père, sa mère), pas la personne."], ["Accords", "Code couleur : adjectif rose = + e ; tableau « mots qui ne changent pas » (calme, drôle, jeune)."], ["sont / ont", "Main sur la gorge [s]/[z] ; dictée de 10 phrases courtes."], ["Élève rapide", "Décrire un personnage célèbre fictif ; écrire le texte « Ma famille » en 10 phrases ; faire l'arbre de la classe."]], ["50mm", "132mm"])}'''
    T = teacher_book(b, E, "V1 · M4", "", MC, 4, "Ma famille et moi",
                     "<li><b>Communication :</b> présenter sa famille ou ses proches, décrire le physique et le caractère, décrire une image.</li><li><b>Lexique :</b> famille, description physique, caractère.</li><li><b>Grammaire :</b> possessifs, accord de l'adjectif (genre et nombre), être et avoir à toutes les personnes.</li><li><b>Phonétique :</b> [f]/[v], [ʃ]/[ʒ], ils sont / ils ont.</li><li><b>FLSco :</b> décrire une image (méthode en 5 étapes, réutilisée dans toutes les disciplines).</li><li><b>★ Alpha :</b> étape 3 — f, v, ch, j ; lecture de phrases simples.</li>",
                     '<p class="sm"><b style="color:#E4572E">Indispensable</b> : membres de la famille, il/elle est/a, description simple.</p><p class="sm"><b style="color:#d9a400">Important</b> : possessifs, accords, nous/vous/ils.</p><p class="sm"><b style="color:#2BA88F">Enrichissement</b> : caractère nuancé, faire-part, virelangue.</p>',
                     "Ciseaux · cartes « Qui est-ce ? » et « 7 familles » imprimées · grandes feuilles pour les affiches · photos facultatives.",
                     "<b>Sujet sensible :</b> lire la note de vigilance de la grille d'évaluation avant de commencer. La famille Ramírez sert de modèle neutre pour tous.",
                     days, "Date et heure au tableau · « Comment est … aujourd'hui ? » (description d'un camarade volontaire) · un mot de la famille dans les langues de la classe.", rot, key, (ev1, ev2), start=tstart)
    if render:
        to_pdf(T.html(), '/home/claude/syllabus/out/V1_M4_prof.pdf')
    return b, T


if __name__ == "__main__":
    b, T = build_m4()
    print(b.n, T.n)
