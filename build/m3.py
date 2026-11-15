"""Volume 1 · Module 3 « Le temps qui passe »."""
import sys
import calendar
import math
sys.path.insert(0, '/home/claude/syllabus')
from lib.base import *
from lib.art import *
from lib.alpha import AL, letter_page, syll_table, slide
from lib.module import plan_de_travail, teacher_book, helpers
from lib.render import to_pdf

MC = "#7B5EA7"
JOURS = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]
N2 = {21: "vingt et un", 22: "vingt-deux", 23: "vingt-trois", 24: "vingt-quatre", 25: "vingt-cinq", 26: "vingt-six", 27: "vingt-sept", 28: "vingt-huit", 29: "vingt-neuf",
      30: "trente", 31: "trente et un", 32: "trente-deux", 40: "quarante", 41: "quarante et un", 45: "quarante-cinq", 50: "cinquante", 51: "cinquante et un", 55: "cinquante-cinq",
      60: "soixante", 61: "soixante et un", 69: "soixante-neuf", 35: "trente-cinq", 38: "trente-huit", 47: "quarante-sept", 52: "cinquante-deux", 64: "soixante-quatre", 33: "trente-trois", 44: "quarante-quatre", 66: "soixante-six"}


def clock(h, m, size=30, label=False):
    ha = math.radians(((h % 12) + m / 60) * 30 - 90)
    ma = math.radians(m * 6 - 90)
    ticks = "".join(f'<line x1="{20+15*math.cos(math.radians(i*30))}" y1="{20+15*math.sin(math.radians(i*30))}" x2="{20+17*math.cos(math.radians(i*30))}" y2="{20+17*math.sin(math.radians(i*30))}" stroke="#1F2A44" stroke-width="{1.4 if i%3==0 else .7}"/>' for i in range(12))
    nums = "".join(f'<text x="{20+12*math.cos(math.radians(n*30-90))}" y="{20+12*math.sin(math.radians(n*30-90))+1.6}" font-size="4.2" text-anchor="middle" font-family="Poppins" font-weight="600">{n}</text>' for n in (12, 3, 6, 9))
    return (f'<svg viewBox="0 0 40 40" width="{size}mm" height="{size}mm"><circle cx="20" cy="20" r="18.5" fill="#fff" stroke="#1F2A44" stroke-width="1.6"/>{ticks}{nums}'
            f'<line x1="20" y1="20" x2="{20+8*math.cos(ha)}" y2="{20+8*math.sin(ha)}" stroke="#1F2A44" stroke-width="2.2" stroke-linecap="round"/>'
            f'<line x1="20" y1="20" x2="{20+13.5*math.cos(ma)}" y2="{20+13.5*math.sin(ma)}" stroke="#E4572E" stroke-width="1.4" stroke-linecap="round"/><circle cx="20" cy="20" r="1.4" fill="#1F2A44"/></svg>')


def month_cal(year, month, marks=None, title=True, small=False):
    marks = marks or {}
    cal = calendar.Calendar(0).monthdayscalendar(year, month)
    fs = "8.5pt" if small else "10pt"
    h = f'<div style="font-weight:800;color:{MC};text-align:center;margin-bottom:1mm">{MOIS[month-1].upper()} {year}</div>' if title else ""
    h += f'<table style="border-collapse:collapse;width:100%;font-size:{fs};text-align:center"><tr>' + "".join(f'<th style="padding:1mm;color:{"#E4572E" if i>4 else "#1F2A44"}">{d[:2]}</th>' for i, d in enumerate(JOURS)) + '</tr>'
    for wk in cal:
        h += "<tr>" + "".join(f'<td style="border:1px solid #dde;padding:1.2mm;{marks.get(d, "") if d else ""}{"color:#E4572E;" if i>4 and d else ""}">{d or ""}</td>' for i, d in enumerate(wk)) + "</tr>"
    return h + "</table>"


def build_m3(start=1, tstart=1, render=True):
    b = Book("V1 · M3", "Volume 1 · Premiers pas · Module 3 · Le temps qui passe", MC, start=start)
    E = Ex(b)

    # ================= OUVERTURE =================
    obj = [("📅", "dire les jours, les mois, la date"), ("🎂", "dire la date de mon anniversaire"), ("🕗", "lire et dire l'heure"), ("🔢", "compter jusqu'à 69"),
           ("📒", "utiliser mon journal de classe"), ("🗓️", "lire le calendrier de l'école"), ("🗣️", "parler : je parle, tu écoutes, il regarde")]
    objs = "".join(f'<div class="flex mb2"><span class="emo s">{e}</span><span class="big">{t}</span></div>' for e, t in obj)
    scene = f'''<div class="flex" style="justify-content:space-around;background:#F3EEFA;border-radius:4mm;padding:4mm">
<div class="card" style="width:70mm">{month_cal(2026, 9, {24: "background:#FFD166;font-weight:800;"}, small=True)}</div>{clock(8, 20, 42)}
<div class="c"><div style="font-size:30pt">🍂☀️<br>❄️🌸</div><div class="sm">les saisons</div></div></div>'''
    b.page(f'''<div style="background:{MC};color:#fff;margin:-17mm -14mm 6mm -14mm;padding:16mm 14mm 6mm 14mm"><div style="font-size:13pt;font-weight:700;opacity:.9">MODULE 3</div><div style="font-size:44pt;font-weight:800;line-height:1">Le temps qui passe</div></div>
{scene}<div class="grid2 mt4"><div><h2>Je vais apprendre à…</h2>{objs}</div><div><div class="card" style="background:#F3EEFA;border-color:#D5C8EA"><h3 style="margin-top:0">🗣️ On parle ensemble</h3>
<p>Quel jour sommes-nous aujourd'hui ?</p><p>Quelle heure est-il ?</p><p>Dans ton pays, il y a des saisons ? Il fait froid en hiver ?</p><p>Dans ta culture, on utilise le même calendrier ?</p></div>
<div class="card mt4"><h3 style="margin-top:0">🔑 Les mots-clés</h3>{"".join(f'<span class="pill">{w}</span>' for w in ["aujourd'hui", "demain", "hier", "la semaine", "le mois", "la date", "l'heure", "l'anniversaire", "le journal de classe", "les vacances"])}</div></div></div>''', "Ouverture", levels=False)
    b.page("%%PLAN_DE_TRAVAIL%%", "Mon plan de travail", levels=False)

    # ================= BD =================
    def case(n, inner):
        return f'<div style="border:2.5px solid #1F2A44;border-radius:3mm;min-height:64mm;position:relative;padding:3mm;background:#FFFDF8"><div style="position:absolute;top:2mm;left:2mm;background:#1F2A44;color:#fff;width:6mm;height:6mm;border-radius:50%;font-size:9pt;font-weight:700;display:flex;align-items:center;justify-content:center">{n}</div>{inner}</div>'

    def bub(t):
        return f'<div class="bubble" style="margin:0 0 2mm 0;font-size:11pt">{t}</div>'

    def lr(a, ta, bb, tb, ma="sourire", mb="sourire"):
        return (f'<div class="flex top" style="margin-top:5mm">{avatar(a, 74, ma)}<div>{"".join(bub(x) for x in ta)}</div></div>'
                f'<div class="flex top" style="justify-content:flex-end">{"".join(bub(x) for x in tb)}{avatar(bb, 74, mb, flip=True)}</div>')
    bd = '<div class="grid2" style="gap:3mm">' + "".join([
        case(1, lr("prof", ["Bonjour tout le monde ! Quel jour sommes-nous ?"], "fatou", ["Aujourd'hui, nous sommes lundi !"], "sourire", "rire")),
        case(2, lr("prof", ["Très bien, Fatou. Et la date ?"], "yonas", ["Lundi 21 septembre 2026 !"], "sourire", "sourire")),
        case(3, lr("bilal", ["Madame ! Demain, c'est mon anniversaire !"], "prof", ["Ah oui ? Tu as quel âge demain ?"], "rire", "surpris")),
        case(4, lr("bilal", ["Demain, j'ai 17 ans !"], "daria", ["Joyeux anniversaire, Bilal ! 🎂"], "rire", "rire")),
        case(5, f'<div class="flex top" style="margin-top:5mm">{avatar("mateo", 74, "surpris")}<div>{bub("Pardon, Madame ! Je suis en retard…")}</div></div><div class="flex top" style="justify-content:flex-end">{bub("Quelle heure est-il, Mateo ?")}{avatar("prof", 74, "pense", flip=True)}</div>'),
        case(6, f'<div class="flex top" style="margin-top:5mm">{avatar("mateo", 74, "triste")}<div>{bub("Il est 8 h 35…")}</div><div style="margin-left:auto">{clock(8, 35, 24)}</div></div><div class="flex top" style="justify-content:flex-end">{bub("Le cours commence à 8 h 20 ! Demain, tu arrives à l&#39;heure !")}{avatar("prof", 70, "neutre", flip=True)}</div>'),
    ]) + '</div>'
    e = E("J'écoute et je regarde la BD : le lundi matin en classe.", bd, ["ecoute", "regarde"], 1, "A",
          script="Lire la BD deux fois. Montrer la date au tableau et l'horloge de la classe. Faire répéter les questions : « Quel jour sommes-nous ? » « Quelle heure est-il ? » « Joyeux anniversaire ! »", sol="Activité orale.")
    b.page(f'<h2>Découvrir · Lundi matin</h2>{e}', "Découvrir")
    e = E("Je réponds aux questions sur la BD.", f'''<p>1. Quel jour sommes-nous dans la BD ? {blank()}</p><p>2. Quelle est la date ? {blank("l")}</p><p>3. Quand est l'anniversaire de Bilal ? {blank()}</p>
<p>4. Bilal a quel âge demain ? {blank("s")} ans</p><p>5. Mateo arrive à quelle heure ? {blank()}</p><p>6. Le cours commence à quelle heure ? {blank()}</p>''', ["lis", "ecris"], 1, "B",
          sol="1. lundi — 2. le lundi 21 septembre 2026 — 3. demain (le mardi 22 septembre) — 4. 17 ans — 5. à 8 h 35 — 6. à 8 h 20")
    e2 = E("Vrai ou faux ?", table(["", "Vrai", "Faux"], [[x, '<span class="chk"></span>', '<span class="chk"></span>'] for x in ["Mateo est en retard.", "L'anniversaire de Bilal, c'est aujourd'hui.", "Mateo arrive 15 minutes en retard.", "Daria dit « Joyeux anniversaire »."]], ["130mm", "25mm", "25mm"]),
           ["lis", "coche"], 2, "B", sol="1. Vrai — 2. Faux (demain) — 3. Vrai (8 h 35 − 8 h 20 = 15 minutes) — 4. Vrai")
    e3 = E("Défi ! Je joue la scène 5-6 avec un camarade. Je change l'heure.", '', ["parle", "duo"], 3, "A", sol="Production orale.")
    b.page(f'{e}{e2}{e3}', "Découvrir")

    # ================= LEÇON 1 : JOURS =================
    jc = ["#FFE5DC", "#E1EAFB", "#DDF3EC", "#FFF3C4", "#EEE3FC", "#FCE4EC", "#FCE4EC"]
    jl = "".join(f'<div class="card c" style="background:{c};padding:2mm"><div class="xs muted">{i+1}</div><div class="word">{d}</div><div class="xs">{"🏫" if i<5 else "🏠"}</div></div>' for i, (d, c) in enumerate(zip(JOURS, jc)))
    l1 = lecon("Les jours de la semaine", f'''<div style="display:grid;grid-template-columns:repeat(7,1fr);gap:2mm">{jl}</div>
<div class="grid3 mt2"><div class="card c" style="background:#fff"><b>hier</b><p class="sm">dimanche</p></div><div class="card c" style="background:#FFD166"><b>aujourd'hui</b><p class="sm">lundi</p></div><div class="card c" style="background:#fff"><b>demain</b><p class="sm">mardi</p></div></div>
<p class="mt2">Quel jour sommes-nous ? → <b>Nous sommes lundi.</b> / <b>On est lundi.</b> / <b>C'est lundi.</b></p>
<div class="grid2"><div class="astuce" style="margin:0">Les jours s'écrivent avec une <b>minuscule</b> : lundi (pas Lundi), sauf au début de la phrase.</div>
<div class="astuce" style="margin:0"><b>le samedi</b> = tous les samedis 🔁<br><b>samedi</b> = ce samedi-là</div></div>''')
    e = E("J'écoute et je répète les jours. Je chante la chanson des jours.", '', ["ecoute", "repete"], 1, "A",
          script="Dire les jours en tapant dans les mains. Puis jeu de la chaîne : un élève dit « lundi », le suivant « mardi »… Puis à l'envers. Questions : « Quel jour après jeudi ? Quel jour avant lundi ? »", sol="Activité orale.")
    b.page(f'{l1}{e}', "Leçon 1")

    e = E("Je complète la suite des jours.", '<div class="grid2">' + "".join(f'<p class="big">{t}</p>' for t in [f"lundi · {blank()} · mercredi", f"{blank()} · vendredi · samedi", f"samedi · {blank()} · lundi", f"mercredi · {blank()} · {blank()}"]) + '</div>',
          ["complete"], 1, "C", sol="mardi · jeudi · dimanche · jeudi, vendredi")
    e2 = E("Hier, aujourd'hui, demain. Je complète.", table(["Hier", "Aujourd'hui", "Demain"], [["", "mardi", ""], ["", "vendredi", ""], ["", "dimanche", ""], ["mercredi", "", ""]], ["60mm", "60mm", "62mm"]),
           ["complete"], 2, "C", sol="lundi · mardi · mercredi / jeudi · vendredi · samedi / samedi · dimanche · lundi / mercredi · jeudi · vendredi")
    e3 = E("J'entoure la bonne réponse.", '''<p>1. Le jour après mardi : <b>lundi / mercredi / jeudi</b></p><p>2. Les jours sans école : <b>mercredi et jeudi / samedi et dimanche / lundi et vendredi</b></p>
<p>3. Il y a … jours dans une semaine : <b>5 / 7 / 10</b></p><p>4. Le mercredi après-midi, en Belgique, au secondaire : <b>il y a cours / il n'y a pas cours</b></p>''', ["lis", "entoure"], 1, "B",
           sol="1. mercredi — 2. samedi et dimanche — 3. 7 — 4. il n'y a pas cours")
    e4 = E("Défi ! Ma semaine : j'écris une activité pour chaque jour.", "".join(f'<p><b style="display:inline-block;width:26mm">{d} :</b> {blank("xl")}</p>' for d in JOURS), ["ecris"], 3, "C",
           sol="Exemple : Le lundi, j'ai gym. Le samedi, je joue au football.")
    b.page(f'{e}{e2}{e3}{e4}', "S'entraîner")

    # ================= LEÇON 2 : MOIS, SAISONS, DATE =================
    seas = [("🍂", "l'automne", "septembre · octobre · novembre"), ("❄️", "l'hiver", "décembre · janvier · février"), ("🌸", "le printemps", "mars · avril · mai"), ("☀️", "l'été", "juin · juillet · août")]
    mc = "".join(f'<div class="card c" style="padding:1.5mm;background:#fff"><div class="xs muted">{i+1}</div><div class="word" style="font-size:10.5pt">{m}</div></div>' for i, m in enumerate(MOIS))
    sc = "".join(f'<div class="card c" style="background:#fff"><span class="emo s">{e}</span><b>{s}</b><div class="xs">{m}</div></div>' for e, s, m in seas)
    l2 = lecon("Les mois · les saisons · la date", f'''<div class="grid6">{mc}</div><div class="grid4 mt2">{sc}</div>
<div class="card mt2" style="background:#fff"><p><b>La date :</b> le + jour + numéro + mois + année</p><p class="big">Nous sommes <b>le lundi 21 septembre 2026</b>. → 21/09/2026</p>
<p>⚠️ Le premier jour du mois : <b>le 1<sup>er</sup></b> (premier) octobre. Les autres : le 2, le 3… (deux, trois…)</p>
<p>Mon anniversaire, c'est <b>le 22 septembre</b>. Je suis né(e) <b>en</b> 2009. On dit : <b>en</b> septembre, <b>en</b> été, <b>en</b> hiver, <b>en</b> automne, mais <b>au</b> printemps.</p></div>''')
    e = E("J'écoute et je répète les mois. Je lève la main au mois de mon anniversaire !", '', ["ecoute", "repete"], 1, "A",
          script="Dire les 12 mois. Chaque élève se lève quand il entend le mois de son anniversaire. Faire une « frise des anniversaires » au mur.", sol="Activité orale.")
    b.page(f'{l2}{e}', "Leçon 2")

    e = E("Je relie le mois et la saison.", relie(["janvier", "juillet", "octobre", "avril", "décembre"], ["le printemps 🌸", "l'hiver ❄️", "l'automne 🍂", "l'été ☀️", "l'hiver ❄️"]), ["relie"], 1, "B",
          sol="janvier → l'hiver · juillet → l'été · octobre → l'automne · avril → le printemps · décembre → l'hiver")
    e2 = E("J'écris la date en lettres.", '<div class="grid2">' + "".join(f'<p>{d} → {blank("l")}</p>' for d in ["03/10/2026", "25/12/2026", "01/01/2027", "14/02/2027"]) + '</div>', ["ecris"], 2, "C",
           sol="le 3 octobre 2026 · le 25 décembre 2026 · le 1er janvier 2027 · le 14 février 2027")
    e3 = E("J'écoute la date et je l'écris en chiffres (jj/mm/aaaa).", '<div class="grid4">' + "".join(f'<div class="card"><b>{i}.</b><div class="line"></div></div>' for i in range(1, 5)) + '</div>', ["ecoute", "ecris"], 2, "A",
           script="Dicter deux fois : 1. le 5 mars 2027 — 2. le 1er juillet 2027 — 3. le 18 novembre 2026 — 4. le 30 août 2026", sol="1. 05/03/2027 — 2. 01/07/2027 — 3. 18/11/2026 — 4. 30/08/2026")
    e4 = E("Les anniversaires de la classe. Je demande la date à 5 camarades : « C'est quand, ton anniversaire ? »", table(["Prénom", "Date d'anniversaire", "Saison"], [["", "", ""] for _ in range(5)], ["50mm", "80mm", "52mm"]).replace("<td></td>", '<td style="height:9mm"></td>'),
           ["parle", "ecris", "groupe"], 2, "A", sol="Réponses personnelles.")
    e5 = E("Défi ! Mon mois préféré : j'explique pourquoi (2 phrases).", lines(2), ["ecris"], 3, "C", sol="Exemple : Mon mois préféré, c'est juillet, parce que c'est l'été. Il y a les vacances.")
    b.page(f'{e}{e2}{e3}{e4}{e5}', "S'entraîner")

    # ================= DOC : CALENDRIER SCOLAIRE =================
    conges = [("Rentrée scolaire", "lundi 24 août 2026", "#DDF3EC"), ("Fête de la Fédération Wallonie-Bruxelles", "dimanche 27 septembre 2026", "#fff"), ("🍂 Congé d'automne (Toussaint)", "du lundi 19 au vendredi 30 octobre 2026", "#FFE5DC"),
              ("Armistice", "mercredi 11 novembre 2026", "#fff"), ("❄️ Vacances d'hiver (Noël)", "du lundi 21 décembre 2026 au vendredi 1er janvier 2027", "#E1EAFB"),
              ("🎭 Congé de détente (Carnaval)", "du lundi 22 février au vendredi 5 mars 2027", "#FFF3C4"), ("🌸 Vacances de printemps (Pâques)", "du lundi 26 avril au vendredi 7 mai 2027", "#FCE4EC"),
              ("☀️ Vacances d'été", "à partir du vendredi 2 juillet 2027", "#FFD166")]
    ct = "".join(f'<tr><td style="padding:2mm;border-bottom:1px solid #dde;background:{c}"><b>{n}</b></td><td style="padding:2mm;border-bottom:1px solid #dde;background:{c}">{d}</td></tr>' for n, d, c in conges)
    e = E("Je lis le calendrier. Je réponds.", f'''<p>1. La rentrée, c'est quel jour ? {blank("l")}</p><p>2. Le congé d'automne commence le {blank("l")}.</p><p>3. Combien de semaines de vacances en hiver ? {blank("s")}</p>
<p>4. Les vacances de printemps finissent le {blank("l")}.</p><p>5. Le 11 novembre 2026, c'est quel jour de la semaine ? {blank()}</p>''', ["lis", "ecris"], 2, "B",
          sol="1. le lundi 24 août 2026 — 2. lundi 19 octobre 2026 — 3. deux — 4. vendredi 7 mai 2027 — 5. un mercredi")
    b.page(f'''<span class="tag-doc">📄 DOCUMENT DE LA VIE</span><h2>Le calendrier scolaire 2026–2027</h2><div class="doc" style="transform:none;padding:3mm"><div style="font-weight:800;color:{MC};margin-bottom:2mm">Fédération Wallonie-Bruxelles · enseignement obligatoire · congés et vacances</div>
<table style="border-collapse:collapse;width:100%;font-size:10pt;font-family:Inter">{ct}</table><p class="xs muted mt2">Source : calendrier officiel de la Fédération Wallonie-Bruxelles pour 2026–2027.</p></div><div class="mt4">{e}</div>''', "Document de la vie")
    e = E("Je regarde le calendrier d'octobre 2026. Je colorie les jours de congé en orange.", f'<div class="card" style="width:120mm;margin:auto">{month_cal(2026, 10)}</div>', ["regarde", "colorie"], 1, "B",
          sol="Du lundi 19 au vendredi 30 octobre (et les week-ends : 17-18, 24-25, 31). Les élèves retournent à l'école le lundi 2 novembre… qui est aussi un jour férié (fête des morts) : reprise le mardi 3.")
    e2 = E("Défi ! Les fêtes dans mon pays. J'écris une fête et sa date.", f'<p>Dans mon pays, il y a la fête de {blank("l")}. C\'est le {blank("l")}.</p><p>Dans ma famille, on fête {blank("l")}.</p>', ["ecris"], 3, "C", sol="Production libre ; valoriser la diversité des calendriers (hégirien, orthodoxe, éthiopien…).")
    b.page(f'{e}{e2}', "Document de la vie")

    # ================= LEÇON 3 : NOMBRES 21-69 =================
    dz = [(20, "vingt"), (30, "trente"), (40, "quarante"), (50, "cinquante"), (60, "soixante")]
    dzc = "".join(f'<div class="card c" style="background:#fff"><div class="huge" style="color:{MC}">{n}</div><div class="word">{w}</div></div>' for n, w in dz)
    l3 = lecon("Les nombres de 21 à 69", f'''<div class="grid5">{dzc}</div>
<table class="t mt2" style="background:#fff"><tr><th>21</th><th>22</th><th>23</th><th>24</th><th>25</th><th>26</th><th>27</th><th>28</th><th>29</th></tr>
<tr><td>vingt <b>et</b> un</td><td>vingt-deux</td><td>vingt-trois</td><td>vingt-quatre</td><td>vingt-cinq</td><td>vingt-six</td><td>vingt-sept</td><td>vingt-huit</td><td>vingt-neuf</td></tr></table>
<div class="grid2 mt2"><div class="astuce" style="margin:0"><b>Le truc :</b> dizaine + trait d'union + unité<br>34 = trente<b>-</b>quatre · 57 = cinquante<b>-</b>sept</div>
<div class="attention" style="margin:0"><b>Avec 1 :</b> vingt <b>et</b> un · trente <b>et</b> un · quarante <b>et</b> un · cinquante <b>et</b> un · soixante <b>et</b> un (pas de trait d'union)</div></div>''')
    e = E("J'écoute et je répète. Je compte de 20 à 69 avec la classe.", '', ["ecoute", "repete"], 1, "A", script="Compter en chœur de 20 à 69 en marquant les dizaines (frapper dans les mains à 30, 40, 50, 60). Puis de 5 en 5 : 20, 25, 30… et de 10 en 10.", sol="Activité orale.")
    b.page(f'{l3}{e}', "Leçon 3")
    pairs = [33, 47, 52, 61, 38, 66, 29, 44]
    e = E("Je relie le nombre et le mot.", relie([f'<b class="big">{n}</b>' for n in pairs[:6]], [N2[n] for n in [61, 38, 33, 66, 52, 47]]), ["relie"], 1, "B",
          sol="33 trente-trois · 47 quarante-sept · 52 cinquante-deux · 61 soixante et un · 38 trente-huit · 66 soixante-six")
    e2 = E("Dictée de nombres : j'écoute et j'écris le chiffre.", '<div class="grid5">' + "".join(f'<div class="card c"><b>{chr(97+i)}.</b><div class="line"></div></div>' for i in range(10)) + '</div>', ["ecoute", "ecris"], 2, "A",
           script="Dicter deux fois : a. 24 — b. 31 — c. 45 — d. 59 — e. 62 — f. 37 — g. 50 — h. 68 — i. 41 — j. 26", sol="a. 24 — b. 31 — c. 45 — d. 59 — e. 62 — f. 37 — g. 50 — h. 68 — i. 41 — j. 26")
    e3 = E("J'écris en lettres.", '<div class="grid3">' + "".join(f'<p><b>{n}</b> → {blank("l")}</p>' for n in [21, 35, 44, 51, 64, 69]) + '</div>', ["ecris"], 2, "C",
           sol="vingt et un · trente-cinq · quarante-quatre · cinquante et un · soixante-quatre · soixante-neuf")
    e4 = E("Défi ! Les nombres dans la vie : je lis et je calcule.", '<div class="grid3"><div class="card c">🚌 Bus <b>45</b> → bus <b>52</b><p class="sm">Différence ?</p>' + blank("s") + '</div><div class="card c">🎂 Né en 1960. En 2026 ?<p class="sm">Âge ?</p>' + blank("s") + ' ans</div><div class="card c">⏱️ 1 heure = ? minutes</div></div>',
           ["lis", "ecris"], 3, "C", sol="7 · 66 ans · 60 minutes")
    b.page(f'{e}{e2}{e3}{e4}', "S'entraîner")
    random_bingo = [[21, 34, 45, 58, 62, 39, 27, 50, 66], [33, 47, 52, 61, 29, 44, 68, 25, 40], [31, 46, 55, 63, 22, 38, 49, 57, 60], [24, 36, 41, 53, 65, 30, 48, 59, 69]]
    grids = "".join(f'<div class="card"><div class="c" style="font-weight:800;color:#9B5DE5">BINGO {i+1}</div><div style="display:grid;grid-template-columns:repeat(3,1fr);gap:1.5mm">' + "".join(f'<div style="border:2px solid #1F2A44;height:16mm;display:flex;align-items:center;justify-content:center;font-size:19pt;font-weight:800">{n}</div>' for n in g) + '</div></div>' for i, g in enumerate(random_bingo))
    e = E("Bingo de 21 à 69 ! Je découpe une grille. La prof dit les nombres.", f'<div class="grid2">{grids}</div>', ["decoupe", "ecoute", "joue"], 1, "D",
          script="Tirer des nombres de 21 à 69. Variante ●●● : dire un calcul (« quarante plus six »).", sol="Jeu.")
    b.page(e, "Jeu")

    # ================= LEÇON 4 : HEURE =================
    hs = [(8, 0, "Il est huit heures."), (8, 20, "Il est huit heures vingt."), (10, 15, "Il est dix heures quinze."), (12, 0, "Il est midi."), (13, 30, "Il est treize heures trente."), (0, 0, "Il est minuit.")]
    hc = "".join(f'<div class="card c" style="background:#fff">{clock(h, m, 24)}<div class="word">{"%d h %02d" % (h, m) if m else "%d h" % h}</div><div class="xs">{t}</div></div>' for h, m, t in hs)
    l4 = lecon("L'heure · Quel ? Quelle ?", f'''<div class="grid3">{hc}</div>
<div class="grid2 mt2"><div class="card" style="background:#fff"><p><b>Quelle heure est-il ?</b> → Il est 9 h 10.</p><p><b>À quelle heure</b> commence le cours ? → <b>À</b> 8 h 20.</p><p class="sm">On écrit : 9 h 10 · 14 h 05 (en Belgique, on écrit souvent 9h10).</p></div>
<div class="card" style="background:#fff"><p><b>Quel</b> + masculin : quel jour ? quel âge ?</p><p><b>Quelle</b> + féminin : quelle heure ? quelle date ?</p><p class="sm muted">●●● À l'oral : 9 h 15 = neuf heures <b>et quart</b> · 9 h 30 = neuf heures <b>et demie</b> · 8 h 45 = neuf heures <b>moins le quart</b>.</p></div></div>''')
    e = E("J'écoute et je montre l'heure sur mon horloge en carton.", '', ["ecoute", "montre"], 1, "P", script="Chaque élève a une horloge en carton (ou le dessin p. suivante). Dire : Il est 7 h. — Il est 9 h 30. — Il est 12 h. — Il est 15 h 15. — Il est 10 h 45. Les élèves placent les aiguilles et montrent.", sol="Activité gestuelle.")
    b.page(f'{l4}{e}', "Leçon 4")
    times = [(7, 0), (9, 30), (11, 15), (2, 45), (4, 10), (6, 50)]
    e = E("Quelle heure est-il ? J'écris l'heure sous l'horloge.", '<div class="grid3">' + "".join(f'<div class="card c">{clock(h, m, 30)}<div class="line"></div></div>' for h, m in times) + '</div>', ["regarde", "ecris"], 1, "C",
          sol="7 h 00 · 9 h 30 · 11 h 15 · 2 h 45 (14 h 45) · 4 h 10 (16 h 10) · 6 h 50 (18 h 50)")
    def empty_clock():
        ticks = "".join(f'<line x1="{20+15*math.cos(math.radians(i*30))}" y1="{20+15*math.sin(math.radians(i*30))}" x2="{20+17*math.cos(math.radians(i*30))}" y2="{20+17*math.sin(math.radians(i*30))}" stroke="#1F2A44" stroke-width="1"/>' for i in range(12))
        nums = "".join(f'<text x="{20+12*math.cos(math.radians(n*30-90))}" y="{20+12*math.sin(math.radians(n*30-90))+1.6}" font-size="4" text-anchor="middle" font-family="Poppins">{n}</text>' for n in range(1, 13))
        return f'<svg viewBox="0 0 40 40" width="30mm"><circle cx="20" cy="20" r="18.5" fill="#fff" stroke="#1F2A44" stroke-width="1.6"/>{ticks}{nums}<circle cx="20" cy="20" r="1.2"/></svg>'
    e2 = E("Je dessine les aiguilles.", '<div class="grid4">' + "".join(f'<div class="card c">{empty_clock()}<b>{t}</b></div>' for t in ["3 h 00", "6 h 30", "10 h 15", "1 h 45"]) + '</div>', ["dessine"], 2, "C",
           sol="Petite aiguille sur 3 / grande sur 12 · petite entre 6 et 7, grande sur 6 · petite juste après 10, grande sur 3 · petite presque sur 2, grande sur 9")
    e3 = E("J'écoute : à quelle heure ? Je relie l'activité et l'heure.", relie(["🍽️ le repas de midi", "🏫 le début des cours", "☕ la récréation", "🏠 la fin des cours", "⚽ le match"], ["15 h 15", "10 h 00", "11 h 55", "17 h 30", "8 h 20"]),
           ["ecoute", "relie"], 2, "A", script="Lire : Le début des cours est à 8 h 20. La récréation est à 10 h. Le repas de midi est à 11 h 55. La fin des cours est à 15 h 15. Le match est à 17 h 30.",
           sol="repas → 11 h 55 · début → 8 h 20 · récréation → 10 h 00 · fin → 15 h 15 · match → 17 h 30")
    b.page(f'{e}{e2}{e3}', "S'entraîner")
    e = E("Quel ou quelle ? Je complète.", '<div class="grid2">' + "".join(f'<p>{blank("s")} {w} ?</p>' for w in ["heure est-il", "jour sommes-nous", "âge as-tu", "est ta date de naissance", "est ton numéro de classe", "saison préfères-tu"]) + '</div>', ["complete"], 2, "C",
          sol="Quelle heure · Quel jour · Quel âge · Quelle est ta date · Quel est ton numéro · Quelle saison")
    e2 = E("Défi ! L'heure à l'oral : je relie.", relie(["9 h 15", "9 h 30", "8 h 45", "12 h 00"], ["neuf heures et demie", "midi", "neuf heures et quart", "neuf heures moins le quart"]), ["relie"], 3, "B",
           sol="9 h 15 et quart · 9 h 30 et demie · 8 h 45 neuf heures moins le quart · 12 h midi")
    e3 = E("Mon horloge à découper : je colle sur du carton, j'attache les aiguilles avec une attache parisienne.", f'<div class="flex" style="justify-content:center;gap:10mm">{empty_clock().replace("30mm", "80mm")}<svg viewBox="0 0 30 60" width="25mm"><path d="M15 2 L19 10 L17 10 L17 55 L13 55 L13 10 L11 10Z" fill="#E4572E" stroke="#1F2A44" stroke-width=".6"/></svg><svg viewBox="0 0 30 60" width="25mm"><path d="M15 18 L19 26 L17 26 L17 55 L13 55 L13 26 L11 26Z" fill="#1F2A44"/></svg></div>',
           ["decoupe", "colle"], 1, "D", sol="Bricolage (utilisé dans les activités d'écoute sur l'heure).")
    b.page(f'{e}{e2}{e3}', "S'entraîner")

    # ================= LEÇON 5 : PRÉSENT -ER =================
    l5 = lecon("Le présent des verbes en -er (je, tu, il, elle)", f'''<div class="grid3">
{"".join(f'<div class="card" style="background:#fff"><b style="color:{MC}">{v.upper()}</b><p>je {r}<b>e</b><br>tu {r}<b>es</b><br>il / elle {r}<b>e</b></p></div>' for v, r in [("parler", "parl"), ("regarder", "regard"), ("écouter", "écout")])}</div>
<div class="grid2 mt2"><div class="card" style="background:#fff"><p>Je <b>commence</b> à 8 h 20. Tu <b>termines</b> à 15 h 15.<br>Il <b>arrive</b> en retard. Elle <b>aime</b> le lundi.<br>J'<b>habite</b> à Namur. Tu <b>travailles</b> le samedi ?</p></div>
<div class="astuce" style="margin:0"><b>Je, il, elle</b> → <b>-e</b> · <b>tu</b> → <b>-es</b><br>On entend la même chose : je parle = tu parles = il parle 👂<br>Mais on écrit différemment ✍️ !<br>je + voyelle → j' : j'écoute, j'aime, j'arrive</div></div>''')
    e = E("J'écoute et je répète. Je mime le verbe.", '<div class="grid6">' + "".join(f'<div class="card c"><span class="emo s">{e}</span><div class="xs">{v}</div></div>' for e, v in [("🗣️", "parler"), ("👀", "regarder"), ("👂", "écouter"), ("🏃", "arriver"), ("❤️", "aimer"), ("🏠", "habiter"), ("▶️", "commencer"), ("⏹️", "terminer"), ("💼", "travailler"), ("🎵", "chanter"), ("💃", "danser"), ("🍽️", "manger")]) + '</div>',
          ["ecoute", "repete"], 1, "A", script="Dire chaque verbe, mimer, faire répéter. Puis : « Je chante » (la prof mime) → « Tu chantes » (en montrant un élève) → « Il chante ».", sol="Activité orale.")
    b.page(f'{l5}{e}', "Leçon 5")
    e = E("Je complète avec la bonne terminaison : -e ou -es.", '<div class="grid2">' + "".join(f'<p>{t}</p>' for t in ["1. Je parl___ arabe.", "2. Tu écout___ la prof.", "3. Il arriv___ à 8 h.", "4. Tu regard___ l'horloge.", "5. Elle aim___ l'été.", "6. J'habit___ à Liège."]) + '</div>', ["complete"], 1, "C",
          sol="1. parle — 2. écoutes — 3. arrive — 4. regardes — 5. aime — 6. habite")
    e2 = E("Je conjugue le verbe entre parenthèses.", '<div class="grid2">' + "".join(f'<p>{t}</p>' for t in [f"1. Le cours (commencer) {blank()} à 8 h 20.", f"2. Tu (terminer) {blank()} à quelle heure ?", f"3. Je (travailler) {blank()} le samedi.", f"4. Mateo (arriver) {blank()} en retard.", f"5. Tu (chanter) {blank()} bien !", f"6. Elle (danser) {blank()} le dimanche."]) + '</div>',
           ["ecris"], 2, "C", sol="1. commence — 2. termines — 3. travaille — 4. arrive — 5. chantes — 6. danse")
    e3 = E("J'entoure le sujet (je, tu, il, elle, un prénom) et je souligne le verbe.", '<p>1. Daria écoute la radio. 2. Tu regardes la date. 3. J\'aime le printemps. 4. Il commence à 9 h. 5. Fatou chante.</p>', ["entoure", "souligne"], 2, "B",
           sol="Daria / écoute · Tu / regardes · J' / aime · Il / commence · Fatou / chante")
    e4 = E("Défi ! Ma journée en 4 phrases avec des verbes en -er et des heures.", lines(4), ["ecris"], 3, "C", sol="Exemple : J'arrive à l'école à 8 h 10. Le cours commence à 8 h 20. Je mange à 12 h. Je termine à 15 h 15.")
    b.page(f'{e}{e2}{e3}{e4}', "S'entraîner")

    # ================= DOC : JOURNAL DE CLASSE =================
    jdc = [("Lundi 21/09", "Français : leçon 📌 les jours (p. 7) à étudier", "Maths : ex. 4 et 5 p. 12"), ("Mardi 22/09", "🎂 Anniversaire de Bilal !", "Sciences : apporter une bouteille vide"),
           ("Mercredi 23/09", "Français : dictée de nombres (21–69)", "—"), ("Jeudi 24/09", "Bibliothèque : rendre le livre", "Gym : tenue de sport ⚽"), ("Vendredi 25/09", "Test de français module 3", "Signature des parents ✍️")]
    jt = "".join(f'<tr><td style="padding:2mm;border:1px solid #ccd;font-weight:700;width:30mm;background:#F3EEFA">{d}</td><td style="padding:2mm;border:1px solid #ccd;font-family:\'TeX Gyre Chorus\';font-size:14pt;color:#1a3a8a">{a}</td><td style="padding:2mm;border:1px solid #ccd;font-family:\'TeX Gyre Chorus\';font-size:14pt;color:#1a3a8a">{c}</td></tr>' for d, a, c in jdc)
    e = E("Je lis le journal de classe de Daria. Je réponds.", f'''<p>1. Quel jour Daria a un test ? {blank()}</p><p>2. Qu'est-ce que Daria apporte le mardi ? {blank("l")}</p><p>3. Quand faut-il la tenue de sport ? {blank()}</p>
<p>4. Quel jour est l'anniversaire de Bilal ? {blank()}</p><p>5. Qui signe le journal de classe le vendredi ? {blank()}</p>''', ["lis", "ecris"], 2, "B",
          sol="1. le vendredi 25/09 — 2. une bouteille vide (pour les sciences) — 3. le jeudi — 4. le mardi 22/09 — 5. les parents")
    b.page(f'''<span class="tag-doc">📄 DOCUMENT DE LA VIE</span><h2>Le journal de classe</h2><div class="astuce">🇧🇪 En Belgique, chaque élève a un <b>journal de classe</b> : on y note les devoirs, les leçons et les messages. Les parents le signent chaque semaine.</div>
<div class="doc" style="transform:none;padding:3mm"><b>Journal de classe · Daria KOVALENKO · DASPA B · semaine 5</b><table style="border-collapse:collapse;width:100%;margin-top:2mm;font-size:10pt"><tr><th style="background:{MC};color:#fff;padding:1.5mm">Jour</th><th style="background:{MC};color:#fff;padding:1.5mm">À faire / à étudier</th><th style="background:{MC};color:#fff;padding:1.5mm">À apporter / messages</th></tr>{jt}</table></div><div class="mt4">{e}</div>''', "Document de la vie")
    e = E("Lire un tableau à double entrée. Je trouve l'information au croisement de la ligne et de la colonne.", f'''<div class="astuce">👉 Je mets un doigt sur la <b>ligne</b> (le jour), un doigt sur la <b>colonne</b> (« À apporter »). Mes doigts se rencontrent : c'est la réponse !</div>
<p>1. Jeudi + « À apporter » → {blank("l")}</p><p>2. Lundi + « À faire » → {blank("xl")}</p><p>3. Mercredi + « À apporter » → {blank()}</p>''', ["lis", "montre", "ecris"], 2, "B",
           sol="1. tenue de sport (et rendre le livre est dans « À faire ») — 2. leçon les jours (p. 7) à étudier — 3. rien (—)")
    e2 = E("J'écris dans mon journal de classe ce que la prof dit.", table(["Jour", "À faire / à étudier", "À apporter"], [["lundi", "", ""], ["mardi", "", ""], ["jeudi", "", ""]], ["30mm", "90mm", "62mm"]).replace("<td></td>", '<td style="height:10mm"></td>'),
           ["ecoute", "ecris"], 3, "A", script="Dicter lentement : « Pour lundi, étudier la leçon sur les mois. Pour mardi, faire l'exercice 3 page 20 et apporter des crayons de couleur. Pour jeudi, apporter la tenue de gym. »",
           sol="lundi : étudier la leçon sur les mois · mardi : ex. 3 p. 20 / crayons de couleur · jeudi : — / tenue de gym")
    b.page(f'<span class="tag-doc">🎒 FRANÇAIS DE L\'ÉCOLE</span><h2>Lire un tableau à double entrée</h2>{e}{e2}', "Consignes & école")

    # ================= SONS =================
    e = E("Le son [e] et le son [ɛ]. J'écoute et je répète.", '''<div class="grid2"><div class="card c" style="border-color:#2BA88F"><div class="huge" style="color:#2BA88F">[e]</div><p>é · er · ez · et</p><p>été ☀️ · café ☕ · parler · nez 👃 · et</p><p class="sm muted">la bouche sourit 😊</p></div>
<div class="card c" style="border-color:#E4572E"><div class="huge" style="color:#E4572E">[ɛ]</div><p>è · ê · ai · e(+ consonne)</p><p>mère · fête 🎉 · mai · lait 🥛 · merci</p><p class="sm muted">la bouche est plus ouverte</p></div></div>''',
          ["ecoute", "repete"], 1, "A", script="Paires : été / était — les / lait — fée / fait — dé / dès. Faire sentir l'ouverture de la bouche (un doigt entre les dents pour [ɛ]).", sol="Activité orale.")
    e2 = E("J'écoute. [e] ou [ɛ] ? Je coche.", table(["", "1", "2", "3", "4", "5", "6", "7", "8"], [["[e]"] + ['<span class="chk"></span>'] * 8, ["[ɛ]"] + ['<span class="chk"></span>'] * 8], ["20mm"] + ["20mm"] * 8),
           ["ecoute", "coche"], 2, "A", script="Lire deux fois : 1. été — 2. mai — 3. café — 4. fête — 5. parler — 6. merci — 7. lait — 8. nez", sol="1. [e] — 2. [ɛ] — 3. [e] — 4. [ɛ] — 5. [e] — 6. [ɛ] — 7. [ɛ] — 8. [e]")
    e3 = E("Les liaisons avec les nombres et l'heure. J'écoute et je répète.", '''<div class="grid3"><div class="card c">deux‿heures<br><span class="sm">[døzœʁ]</span></div><div class="card c">trois‿ans<br><span class="sm">[tʁwazɑ̃]</span></div><div class="card c">six‿heures<br><span class="sm">[sizœʁ]</span></div>
<div class="card c">neuf‿heures<br><span class="sm">[nœvœʁ] ⚠️ f → v</span></div><div class="card c">dix‿ans<br><span class="sm">[dizɑ̃]</span></div><div class="card c">vingt‿et un<br><span class="sm">[vɛ̃teœ̃]</span></div></div>''',
           ["ecoute", "repete"], 2, "A", script="Lire chaque expression lentement en marquant la liaison, faire répéter. Puis : « Il est deux heures, trois heures… onze heures. »", sol="Activité orale.")
    b.page(f'<h2>J\'écoute bien · [e] / [ɛ] · les liaisons</h2>{e}{e2}{e3}', "Sons")

    # ================= RÉVISE M1-M2 =================
    e = E("🔁 Module 2 · Un, une, le, la ? Je complète.", '<p>Dans ___ classe, il y a ___ horloge. ___ tableau est vert. J\'ai ___ cahier et ___ livres.</p>', ["complete"], 1, "C", sol="la · une · Le · un · des")
    e2 = E("🔁 Module 2 · Où vais-je ?", '<p>1. J\'ai mal → ___________ 2. C\'est midi → ___________ 3. Je veux un livre → ___________</p>', ["ecris"], 1, "C", sol="l'infirmerie · le réfectoire · la bibliothèque")
    e3 = E("🔁 Module 1 · Être ou avoir ?", '<p>Bilal ___ 16 ans. Il ___ afghan… non ! Il vient d\'Afghanistan. Daria ___ gentille. Tu ___ un GSM ?</p>'.replace("Il ___ afghan… non ! Il vient d'Afghanistan. ", ""), ["complete"], 2, "C", sol="a · est · as")
    e4 = E("🔁 Modules 1-2 · Je réponds poliment.", '<p>1. Tu arrives en retard : ____________________________</p><p>2. Tu n\'as pas de stylo : ____________________________</p><p>3. Tu ne comprends pas : ____________________________</p>', ["ecris"], 2, "C",
           sol="Excusez-moi pour le retard. · Tu peux me prêter un stylo, s'il te plaît ? · Vous pouvez répéter, s'il vous plaît ?")
    b.page(f'<h2>🔁 Je révise les modules 1 et 2</h2>{e}{e2}{e3}{e4}', "Je révise")

    # ================= ATELIERS =================
    cards = [(7, 30), (12, 0), (16, 45), (9, 15), (20, 0), (13, 10)]
    e = E("Quelle heure est-il ? Je découpe les cartes. Je montre une carte, mon camarade dit l'heure.", '<div class="grid3">' + "".join(f'<div class="card c" style="border-style:dashed">{clock(h % 12, m, 32)}<div class="xs muted" style="transform:rotate(180deg)">{h} h {m:02d}</div></div>' for h, m in cards) + '</div>',
          ["decoupe", "parle", "duo"], 1, "A", sol="Réponses au dos (à l'envers).")
    e2 = E("Interview : je pose les questions à un camarade et je note.", table(["Question", "Réponse"], [[q, ""] for q in ["Quel jour on est aujourd'hui ?", "C'est quand, ton anniversaire ?", "Tu te lèves à quelle heure ?", "Quel est ton jour préféré ? Pourquoi ?", "Quelle est ta saison préférée ?"]], ["90mm", "92mm"]).replace("<td></td>", '<td style="height:9mm"></td>'),
           ["parle", "ecris", "duo"], 2, "A", sol="Réponses personnelles.")
    b.page(f'<span class="atl A" style="font-size:12pt;padding:1.5mm 4mm">{ATELIERS["A"]}</span><h2 class="mt2">Atelier · Écouter et parler</h2>{e}{e2}', "Atelier")
    aff = f'''<div class="doc" style="transform:rotate(-1deg);padding:5mm;background:linear-gradient(160deg,#FFF3C4,#FFE5DC);border:2px solid #F2B705">
<div class="c" style="font-size:22pt;font-weight:800;color:#E4572E">🎉 FÊTE DE L'ÉCOLE 🎉</div><div class="c big"><b>Samedi 12 juin 2027</b> · de 14 h à 19 h</div>
<div class="grid2 mt2"><div><p>🎤 14 h 30 : spectacle des élèves (salle de gym)</p><p>🌍 15 h 30 : repas du monde (cour)</p><p>⚽ 16 h 00 : match profs – élèves</p></div>
<div><p>🎨 Atelier dessin : de 14 h à 17 h (local 12)</p><p>🎵 18 h 00 : concert</p><p>💶 Entrée gratuite · repas : 5 €</p></div></div><p class="c sm">Athénée des Tilleuls · Rue des Tilleuls 24 · Namur</p></div>'''
    e = E("Je lis l'affiche.", aff, ["lis"], 1, "B")
    e2 = E("Je réponds.", f'''<div class="grid2"><p>1. La fête est quel jour ? {blank()}</p><p>2. Elle commence à quelle heure ? {blank()}</p><p>3. Le match commence à {blank()}.</p><p>4. Le repas coûte {blank("s")}.</p></div>
<p>5. ●● Combien d'heures dure la fête ? {blank("s")}</p><p>6. ●●● Je veux voir le spectacle et le concert. J'arrive à quelle heure ? Je pars à quelle heure ? {blank("xl")}</p>''', ["lis", "ecris"], 2, "B",
            sol="1. le samedi 12 juin 2027 — 2. à 14 h — 3. 16 h — 4. 5 € — 5. cinq heures — 6. j'arrive avant 14 h 30 et je pars après le concert (vers 19 h)")
    b.page(f'<span class="atl B" style="font-size:12pt;padding:1.5mm 4mm">{ATELIERS["B"]}</span><h2 class="mt2">Atelier · Lire</h2>{e}{e2}', "Atelier")
    e = E("Je recopie la date du jour et l'heure, comme au tableau.", f'<div class="card" style="background:#2F5D50;color:#fff;font-size:16pt;text-align:center">Nous sommes le jeudi 1er octobre 2026. Il est 10 h 15.</div>{lines(2, True)}', ["recopie"], 1, "C", sol="Copie.")
    e2 = E("J'écris une carte d'anniversaire pour un camarade.", f'''<div style="border:3px dashed #C94F7C;border-radius:5mm;padding:5mm;background:#FFF5F8"><div class="c" style="font-size:28pt">🎂🎈🎁</div><p style="line-height:2.3">Cher / Chère {blank("l")},<br>Joyeux anniversaire ! Aujourd'hui, le {blank("l")}, tu as {blank("s")} ans.<br>{blank("xl")}<br>Bisous / Amitiés, {blank()}</p></div>''',
            ["ecris"], 2, "C", sol="Production personnelle ; vérifier la date en lettres et « tu as … ans ».")
    e3 = E("Défi ! J'écris mon week-end idéal : jour, heure, activité (5 phrases).", lines(5), ["ecris"], 3, "C", sol="Production libre avec verbes en -er et heures.")
    b.page(f'<span class="atl C" style="font-size:12pt;padding:1.5mm 4mm">{ATELIERS["C"]}</span><h2 class="mt2">Atelier · Écrire</h2>{e}{e2}{e3}', "Atelier")
    dom = [((8, 0), "huit heures"), ((9, 30), "neuf heures et demie"), ((3, 15), "trois heures et quart"), ((6, 0), "six heures"), ((10, 45), "onze heures moins le quart"), ((12, 0), "midi"), ((4, 30), "quatre heures et demie"), ((1, 15), "une heure et quart")]
    dc = "".join(f'<div style="display:flex;border:2px solid #1F2A44;border-radius:3mm;height:30mm;overflow:hidden"><div style="flex:1;display:flex;align-items:center;justify-content:center;border-right:2px dashed #1F2A44">{clock(*dom[i][0], 24)}</div><div style="flex:1;display:flex;align-items:center;justify-content:center;font-weight:700;text-align:center;font-size:10pt;padding:1mm">{dom[(i+1) % 8][1]}</div></div>' for i in range(8))
    e = E("Les dominos de l'heure. Je découpe. J'assemble l'horloge et la phrase qui correspond.", f'<div class="grid2">{dc}</div>', ["decoupe", "joue", "groupe"], 2, "D", sol="Chaîne : 8 h → huit heures … chaque horloge se colle à la phrase correspondante (le dernier domino rejoint le premier).")
    e2 = E("Le code des jours : chaque jour a une couleur. Je colorie la case du bon jour.", '<p class="sm">lundi 🟥 · mardi 🟦 · mercredi 🟩 · jeudi 🟨 · vendredi 🟪</p>' + table(["Indice", "Jour"], [["Le jour avant mardi", ""], ["Le jour après mercredi", ""], ["Le jour de la gym (horaire du module 2)", ""], ["Le premier jour du week-end", ""]], ["130mm", "52mm"]),
           ["lis", "colorie"], 2, "D", sol="lundi · jeudi · lundi et jeudi · samedi")
    b.page(f'<span class="atl D" style="font-size:12pt;padding:1.5mm 4mm">{ATELIERS["D"]}</span><h2 class="mt2">Atelier · Jouer</h2>{e}{e2}', "Atelier")

    # ================= ALPHA =================
    letter_page(b, E, "p", "[p]", [("👨", "papa"), ("🍎", "pomme"), ("🍕", "pizza"), ("🦜", "perroquet")], "qbdgbqdb",
                [("👨", "papa", 1), ("🍎", "pomme", 1), ("🐱", "chat", 0), ("🍕", "pizza", 1), ("🌙", "lune", 0), ("🏴‍☠️", "pirate", 1), ("🛏️", "lit", 0), ("🥔", "patate", 1)], MC)
    letter_page(b, E, "t", "[t]", [("🍅", "tomate"), ("🐢", "tortue"), ("📱", "téléphone"), ("🚕", "taxi")], "flfkhfil",
                [("🍅", "tomate", 1), ("🐢", "tortue", 1), ("🦙", "lama", 0), ("🚕", "taxi", 1), ("🏍️", "moto", 1), ("🧱", "mur", 0), ("👜", "sac", 0), ("🐱", "chat", 0)], MC)
    letter_page(b, E, "d", "[d]", [("🐬", "dauphin"), ("🎲", "dé"), ("🦷", "dent"), ("🦖", "dinosaure")], "bpqbpbqo",
                [("🐬", "dauphin", 1), ("🎲", "dé", 1), ("🍅", "tomate", 0), ("🦷", "dent", 1), ("🥗", "salade", 1), ("👨", "papa", 0), ("🐢", "tortue", 0), ("🎂", "anniversaire", 0)], MC)
    letter_page(b, E, "n", "[n]", [("☁️", "nuage"), ("🪹", "nid"), ("👃", "nez"), ("🍍", "ananas")], "mumuhvmu",
                [("☁️", "nuage", 1), ("👃", "nez", 1), ("🦙", "lama", 0), ("🍍", "ananas", 1), ("🌙", "lune", 1), ("🎲", "dé", 0), ("🛞", "roue", 0), ("🐱", "chat", 0)], MC)
    e = E("Je lis les syllabes.", syll_table(["p", "t", "d", "n"]) + '<div class="grid4 mt2">' + slide("p", "a") + slide("t", "o") + slide("d", "i") + slide("n", "u") + '</div>', ["lis", "repete"], 1, "P", alpha=True,
          script="Lire en ligne, en colonne, puis au hasard. Attention p/b et t/d : main sur la gorge (pas de vibration pour p et t).", sol="pa pi po pu pé / ta ti to tu té / da di do du dé / na ni no nu né")
    e2 = E("Les syllabes à l'envers : la voyelle d'abord ! Je lis.", '<div class="grid6">' + "".join(f'<div class="card c huge">{s}</div>' for s in ["al", "il", "or", "ur", "as", "is", "ot", "ip", "ad", "an", "ir", "ol"]) + '</div>', ["lis"], 2, "P", alpha=True,
           script="Faire lire : a-l → al. Comparer la / al, li / il, ro / or.", sol="Lecture : al il or ur as is ot ip ad an ir ol")
    b.page(AL.format(t="Je lis des syllabes") + e + e2, "★ Alpha", color=MC)
    words = [("👨", "pa-pa", "papa"), ("🏍️", "mo-to", "moto"), ("🍅", "to-ma-te", "tomate"), ("🥗", "sa-la-de", "salade"), ("🏴‍☠️", "pi-ra-te", "pirate"), ("🤒", "ma-la-de", "malade"), ("🥔", "pa-ta-te", "patate"), ("🌙", "lu-ne", "lune")]
    e = E("Je lis les mots, syllabe par syllabe.", '<div class="grid4">' + "".join(f'<div class="card c"><span class="emo s">{e}</span><div class="huge" style="font-size:18pt">{s.replace("-", "<span style=color:#E4572E>·</span>")}</div></div>' for e, s, w in words) + '</div>', ["lis"], 1, "P", alpha=True,
          script="Lire avec l'élève, syllabe par syllabe, puis le mot entier.", sol=" · ".join(w for _, _, w in words))
    e2 = E("Je lis les petites phrases. Je dessine.", '<div class="grid2">' + "".join(f'<div class="card"><p class="big">{t}</p><div style="height:22mm;border:1.5px dashed #b9bfcc;border-radius:2mm"></div></div>' for t in ["Papa a une moto.", "Sami lit.", "Mila a une tomate.", "Rémi a la salade."]) + '</div>',
           ["lis", "dessine"], 2, "B", alpha=True, sol="Lecture des phrases ; dessins cohérents.")
    b.page(AL.format(t="Je lis des mots et des phrases") + e + e2, "★ Alpha", color=MC)
    e = E("Dictée de syllabes et de mots.", guide_lines(3, 20), ["ecoute", "ecris"], 2, "P", alpha=True, script="Dicter : pa — to — di — nu — moto — papa — tapis — lune", sol="pa to di nu moto papa tapis lune")
    e2 = E("J'écris le mot sous l'image.", '<div class="grid4">' + "".join(f'<div class="card c"><span class="emo">{e}</span><div class="line"></div></div>' for e in ["🏍️", "🍅", "👨", "🌙"]) + '</div>', ["ecris"], 3, "C", alpha=True, sol="moto · tomate · papa · lune")
    e3 = E("Je recopie les jours (les mots de la classe).", trace("lundi", 26, 2) + trace("mardi", 26, 2) + trace("samedi", 26, 1), ["recopie", "trace"], 1, "C", alpha=True, sol="Copie.")
    b.page(AL.format(t="J'écris") + e + e2 + e3, "★ Alpha", color=MC)

    # ================= TÂCHE FINALE =================
    e = E("Mon journal de classe pour une semaine. Je remplis avec mon horaire réel et les devoirs de la semaine.", table(["Jour · date", "Cours", "À faire / à étudier", "À apporter"], [[f"<b>{d}</b><br>....../......", "", "", ""] for d in JOURS[:5]], ["30mm", "45mm", "60mm", "47mm"]).replace("<td></td>", '<td style="height:24mm"></td>'),
          ["ecris"], 2, "C", sol="Évaluation avec la grille de la tâche finale.")
    b.page(f'''<div style="background:#1F2A44;color:#fff;margin:-17mm -14mm 5mm -14mm;padding:15mm 14mm 5mm 14mm"><div style="font-size:11pt;font-weight:700;opacity:.8">🎯 TÂCHE FINALE</div><div style="font-size:26pt;font-weight:800">Ma semaine dans mon journal de classe</div>
<div class="sm" style="opacity:.9">Je note correctement les dates, les heures, les devoirs et les messages. Puis je présente ma semaine à la classe.</div></div>{e}''', "Tâche finale", levels=False)
    chk = table(["Je vérifie :", "✅"], [[x, '<span class="chk"></span>'] for x in ["Les dates sont complètes (jour + numéro + mois).", "Les jours ont une minuscule.", "J'ai noté les devoirs et les leçons.", "Je sais présenter ma semaine (5 phrases avec des verbes en -er)."]], ["160mm", "22mm"])
    e = E("Je présente ma semaine à la classe : « Le lundi 5 octobre, je commence à 8 h 20. J'ai… »", lines(5), ["ecris", "parle"], 2, "A", sol="Production orale évaluée avec la grille.")
    b.page(f'{chk}{e}', "Tâche finale", levels=False)

    # ================= RÉVISE =================
    e = E("Je complète avec un jour, un mois ou une saison.", '<p>1. Après jeudi, c\'est ________. 2. Le mois de Noël : ________. 3. Juillet, c\'est en ________. 4. Le premier mois de l\'année : ________.</p>', ["complete"], 1, "C", sol="vendredi · décembre · été · janvier")
    e2 = E("J'écris l'heure en chiffres.", '<p>huit heures vingt : ______ · midi : ______ · quinze heures quinze : ______ · dix heures et demie : ______</p>', ["ecris"], 2, "C", sol="8 h 20 · 12 h 00 · 15 h 15 · 10 h 30")
    e3 = E("Je conjugue au présent.", '<p>Je (regarder) ________ · Tu (écouter) ________ · Elle (commencer) ________ · Tu (aimer) ________</p>', ["ecris"], 2, "C", sol="regarde · écoutes · commence · aimes")
    e4 = E("Défi ! Je corrige les 4 erreurs.", '<div class="card big">Aujourd\'hui, nous sommes Mardi le 3 Octobre. Tu commence à huit heure.</div>' + lines(2), ["barre", "ecris"], 3, "C",
           sol="mardi (minuscule) · le mardi 3 octobre (ordre + minuscule) · tu commences · huit heures")
    b.page(f'<h2>🔁 Je révise tout le module</h2>{e}{e2}{e3}{e4}', "Je révise")

    # ================= TEST =================
    head = f'''<div style="background:#1F2A44;color:#fff;margin:-17mm -14mm 4mm -14mm;padding:14mm 14mm 4mm 14mm;display:flex;justify-content:space-between;align-items:flex-end"><div><div style="font-size:11pt;font-weight:700;opacity:.8">📝 TEST · MODULE 3</div><div style="font-size:24pt;font-weight:800">Le temps qui passe</div></div><div class="sm" style="text-align:right">Prénom : ......................................<br>Date : ........ / ........ / ............</div></div>'''
    Q = [("Le jour après lundi :", ["dimanche", "mardi", "jeudi", "mercredi"]), ("Les jours du week-end :", ["lundi et mardi", "jeudi et vendredi", "samedi et dimanche", "mercredi et jeudi"]),
         ("Aujourd'hui, c'est mardi. Demain, c'est :", ["lundi", "mercredi", "jeudi", "dimanche"]), ("Le mois après mars :", ["février", "mai", "juin", "avril"]),
         ("Décembre, janvier, février, c'est :", ["l'hiver", "l'été", "le printemps", "l'automne"]), ("21/09/2026 =", ["le 21 septembre 2026", "le 9 février 2026", "le 21 novembre 2026", "le 2 septembre 2026"]),
         ("Le 1/10 se dit :", ["le un octobre", "le premier octobre", "le dix octobre", "le premier novembre"]), ("45 =", ["quatorze-cinq", "cinquante-quatre", "quarante-cinq", "quatre-cinq"]),
         ("soixante et un =", ["61", "16", "71", "51"]), ("trente-huit =", ["83", "28", "48", "38"]),
         (f'{clock(9, 0, 13)} Il est :', ["neuf heures", "trois heures", "douze heures", "six heures"]), (f'{clock(2, 30, 13)} Il est :', ["deux heures trente", "six heures dix", "trois heures", "six heures et quart"]),
         ("12 h 00 =", ["minuit", "midi", "deux heures", "dix heures"]), ("____ heure est-il ?", ["Quel", "Quels", "Quelle", "Où"]),
         ("Tu ____ la radio.", ["écoute", "écoutons", "écoutent", "écoutes"]), ("Il ____ à 8 h 20.", ["commence", "commences", "commencez", "commencer"]),
         ("Sur le calendrier, la rentrée 2026 est le :", ["lundi 24 août", "lundi 1er septembre", "vendredi 2 juillet", "lundi 19 octobre"]),
         ("Dans le journal de classe, j'écris :", ["mes devoirs et mes leçons", "mon numéro de GSM", "mes jeux vidéo", "rien"]),
         ("🔁 Je mange à midi :", ["au réfectoire", "à l'infirmerie", "au secrétariat", "à la bibliothèque"]), ("🔁 ____ livres", ["un", "une", "le", "des"])]
    key = "1-B, 2-C, 3-B, 4-D, 5-A, 6-A, 7-B, 8-C, 9-A, 10-D, 11-A, 12-A, 13-B, 14-C, 15-D, 16-A, 17-A, 18-A, 19-A, 20-D"
    # rééquilibrage : quelques réponses déplacées
    Q[10] = (Q[10][0], ["trois heures", "neuf heures", "douze heures", "six heures"])
    Q[11] = (Q[11][0], ["six heures dix", "trois heures", "deux heures trente", "six heures et quart"])
    Q[16] = (Q[16][0], ["lundi 1er septembre", "vendredi 2 juillet", "lundi 24 août", "lundi 19 octobre"])
    Q[17] = (Q[17][0], ["mon numéro de GSM", "mes devoirs et mes leçons", "mes jeux vidéo", "rien"])
    Q[18] = (Q[18][0], ["à l'infirmerie", "au secrétariat", "à la bibliothèque", "au réfectoire"])
    key = "1-B, 2-C, 3-B, 4-D, 5-A, 6-A, 7-B, 8-C, 9-A, 10-D, 11-B, 12-C, 13-B, 14-C, 15-D, 16-A, 17-C, 18-B, 19-D, 20-D"
    p1 = "".join(qcm_line(i + 1, q, o) for i, (q, o) in enumerate(Q[:10]))
    p2 = "".join(qcm_line(i + 11, q, o) for i, (q, o) in enumerate(Q[10:]))
    b.page(f'{head}<div class="flex" style="justify-content:space-between"><h2 style="margin:0">Partie A · Je choisis la bonne réponse</h2><span class="score">…… / 20</span></div><p class="sm muted">J\'entoure la lettre, puis je noircis le rond sur la feuille de réponses.</p>{p1}', "Test", levels=False)
    b.page(p2, "Test", levels=False)
    b.page(f'''<div class="flex" style="justify-content:space-between"><h2 style="margin:0">Partie B · J'écris</h2><span class="score">…… / 10</span></div>
<h3>B1. J'écris la date d'aujourd'hui en lettres. (… / 2)</h3>{lines(1, True)}<h3>B2. J'écris l'heure. (… / 3)</h3><div class="grid3">{"".join(f'<div class="card c">{clock(h, m, 26)}<div class="line"></div></div>' for h, m in [(7, 30), (10, 15), (4, 50)])}</div>
<h3>B3. J'écris 5 phrases sur ma semaine (jours, heures, verbes en -er). (… / 5)</h3>{lines(5, True)}
<div class="flex mt4" style="justify-content:space-between"><h2 style="margin:0">Partie C · Je parle avec la prof</h2><span class="score">…… / 10</span></div>
{table(["Je sais…", "Points", "✅"], [["dire les jours et les mois", "/ 2", ""], ["dire la date et mon anniversaire", "/ 2", ""], ["lire 4 heures sur une horloge", "/ 4", ""], ["lire 4 nombres entre 21 et 69", "/ 2", ""]], ["120mm", "30mm", "32mm"])}
<div class="card mt2 c"><span class="huge">TOTAL : …… / 40</span></div>''', "Test", levels=False)
    ta = f'''<div style="background:#FFD166;margin:-17mm -14mm 4mm -14mm;padding:14mm 14mm 4mm 14mm"><div style="font-size:11pt;font-weight:800">★ ALPHA · 📝 TEST · MODULE 3</div><div style="font-size:22pt;font-weight:800">Le temps qui passe</div></div>
<h3>1. J'écoute et j'entoure la syllabe. (… / 4)</h3><div class="grid4">{"".join(f'<div class="card c big" style="font-weight:700;white-space:nowrap">{r}</div>' for r in ["pa po pi", "ta tu ti", "da di do", "na ni nu"])}</div>
<h3>2. Je lis et je relie. (… / 4)</h3>{relie([f'<b class="big">{w}</b>' for w in ["moto", "papa", "tomate", "lune"]], ['<span class="emo s">🌙</span>', '<span class="emo s">🍅</span>', '<span class="emo s">🏍️</span>', '<span class="emo s">👨</span>'])}
<h3>3. J'écris les syllabes et les mots dictés. (… / 4)</h3>{guide_lines(1, 22)}
<h3>4. Je dis les jours de la semaine (oral). (… / 4)</h3><div class="card">lundi ☐ mardi ☐ mercredi ☐ jeudi ☐ vendredi ☐ samedi ☐ dimanche ☐</div>
<h3>5. Je lis l'heure (oral). (… / 4)</h3><div class="grid4">{"".join(f'<div class="card c">{clock(h, 0, 24)}</div>' for h in (3, 8, 12, 6))}</div><div class="card c mt2"><span class="huge">TOTAL : …… / 20</span></div>'''
    b.page(ta, "★ Alpha · Test", levels=False)
    items = ["Je sais dire les jours de la semaine.", "Je sais dire hier, aujourd'hui, demain.", "Je sais dire les mois et les saisons.", "Je sais dire et écrire la date.", "Je sais dire mon anniversaire.",
             "Je sais compter jusqu'à 69.", "Je sais lire l'heure.", "Je sais dire quel / quelle.", "Je sais conjuguer un verbe en -er (je, tu, il).", "Je sais lire le calendrier scolaire.", "Je sais utiliser mon journal de classe.", "★ Je sais lire pa, to, di, nu, moto, papa…"]
    tb = table(["", "😀 Oui !", "🙂 Un peu", "😕 Pas encore", "La prof"], [[x, '<span class="chk"></span>', '<span class="chk"></span>', '<span class="chk"></span>', ""] for x in items], ["92mm", "20mm", "20mm", "24mm", "26mm"])
    b.page(f'<h2>✅ Je sais faire</h2>{tb}<div class="grid2 mt4"><div class="card"><b>Ce que j\'aime dans ce module :</b>{lines(2)}</div><div class="card"><b>C\'est difficile pour moi :</b>{lines(2)}</div></div>', "Je sais faire", levels=False)
    mots = [("📅", "le jour"), ("🗓️", "la semaine"), ("📆", "le mois"), ("🍂", "l'automne"), ("❄️", "l'hiver"), ("🌸", "le printemps"), ("☀️", "l'été"), ("⏪", "hier"), ("📍", "aujourd'hui"), ("⏩", "demain"),
            ("🎂", "l'anniversaire"), ("🕗", "l'heure"), ("⏱️", "la minute"), ("🌞", "midi"), ("🌙", "minuit"), ("📒", "le journal de classe"), ("📚", "les devoirs"), ("📌", "la leçon"), ("🏖️", "les vacances"), ("🎉", "la fête"),
            ("▶️", "commencer"), ("⏹️", "terminer"), ("🏃", "arriver"), ("🗣️", "parler"), ("👂", "écouter"), ("👀", "regarder"), ("❤️", "aimer"), ("💼", "travailler"), ("⏰", "en retard"), ("✅", "à l'heure")]
    half = len(mots) // 2
    mt = lambda lst: table(["", "Français", "Dans ma langue"], [[f'<span style="font-size:13pt">{e}</span>', f"<b>{w}</b>", ""] for e, w in lst], ["12mm", "40mm", "36mm"]).replace("<td>", '<td style="padding:1.6mm 2mm">')
    b.page(f'<h2>📒 Mes mots du module 3</h2><div class="grid2">{mt(mots[:half])}{mt(mots[half:])}</div>', "Mes mots", levels=False)

    plan_de_travail(b, E, 3, ["Les jours de la semaine", "Les mois · les saisons · la date", "Les nombres de 21 à 69", "L'heure · quel / quelle", "Le présent des verbes en -er"], "☐ Journal de classe d'une semaine<br>☐ Présentation orale")
    if render:
        to_pdf(b.html(), '/home/claude/syllabus/out/V1_M3_eleve.pdf')
    pg, exs = helpers(b, E)
    A = b.marks["★ Alpha"]
    days = [("1", "Collectif", f"Ouverture · plan de travail · BD ({pg('Découvrir')})", f"Alpha : p (p. {A[0]})"), ("2", "Collectif + rotation", f"📌 Leçon 1 les jours ({pg('Leçon 1')})", f"Alpha : t (p. {A[1]})"),
            ("3", "Rotation", f"📌 Leçon 2 mois, saisons, date ({pg('Leçon 2')}) · frise des anniversaires", f"Alpha : d (p. {A[2]})"), ("4", "Collectif", f"Calendrier scolaire ({pg('Document de la vie')})", f"Alpha : n (p. {A[3]})"),
            ("5", "Rotation", f"📌 Leçon 3 nombres 21–69 ({pg('Leçon 3')}) · bingo ({pg('Jeu')})", f"Alpha : syllabes (p. {A[4]})"), ("6", "Collectif + bricolage", f"📌 Leçon 4 l'heure ({pg('Leçon 4')}) · horloge à découper", f"Alpha : mots et phrases (p. {A[5]})"),
            ("7", "Rotation", f"📌 Leçon 5 verbes en -er ({pg('Leçon 5')}) · journal de classe · tableau à double entrée ({pg('Consignes & école')})", f"Alpha : dictée (p. {A[6]})"),
            ("8", "Ateliers", f"Ateliers ({pg('Atelier')}) · sons ({pg('Sons')}) · 🔁 révision M1-M2", "Alpha : révision"), ("9", "Seul puis oral", f"Tâche finale ({pg('Tâche finale')})", "Alpha : journal simplifié (jours recopiés)"),
            ("10", "Seul", f"Je révise · test ({pg('Test')}) · je sais faire · mes mots", f"Alpha : test ({pg('★ Alpha · Test')})")]
    rot = [["🎧 Écouter-Parler", "Cartes-horloges · interview", "20 min", "Réponses au dos"], ["📖 Lire", "Affiche de la fête de l'école", "20 min", "Oui"], ["✏️ Écrire", "Date au tableau · carte d'anniversaire", "20 min", "● oui · ●●● prof"],
           ["🧩 Jouer", "Dominos de l'heure · code des jours", "20 min", "Entre joueurs"], ["👩‍🏫 Table d'appui", "Alpha : p t d n · autres : l'heure, -e/-es", "20 min", "—"]]
    ev1 = '''<h3>Partie B · Écrit (10 points)</h3><p class="sm"><b>B1</b> : 2 pts si date complète et correcte (jour + numéro + mois + année, minuscules) · <b>B2</b> : <span class="sol">7 h 30 · 10 h 15 · 4 h 50 (ou 16 h 50)</span> · <b>B3</b> : 1 pt par phrase correcte (verbe en -er bien conjugué + repère de temps).</p>
<h3>Partie C · Oral (10 points)</h3><p class="sm">Jours et mois dans l'ordre (2) · date du jour + anniversaire (2) · 4 horloges (1 pt chacune) · 4 nombres (½ pt chacun).</p>
<h3>Test ★ Alpha (20 points)</h3><p class="sm"><b>Ex. 1, dire :</b> <span class="sol">po · ti · da · nu</span> · <b>Ex. 2 :</b> <span class="sol">moto–🏍️, papa–👨, tomate–🍅, lune–🌙</span> · <b>Ex. 3, dicter :</b> <span class="sol">pa, di, moto, papa</span> · Ex. 4 : ½ pt par jour (arrondi) · Ex. 5 : <span class="sol">3 h, 8 h, 12 h (midi), 6 h</span>.</p>'''
    ev2 = f'''<h2>Grille · tâche finale « Ma semaine dans mon journal de classe »</h2>{table(["Critère", "Très bien", "Bien", "À retravailler", "Points"], [["<b>Dates</b> complètes et correctes", "5 dates justes", "3-4", "0-2", "/ 5"], ["<b>Contenu</b> : cours, devoirs, messages", "Complet", "Partiel", "Presque vide", "/ 5"], ["<b>Orthographe</b> : jours en minuscules, mots du module", "Correct", "Quelques erreurs", "Beaucoup", "/ 4"], ["<b>Oral</b> : présentation avec verbes en -er et heures", "Fluide", "Hésitant", "Bloqué", "/ 6"]], ["64mm", "32mm", "32mm", "32mm", "22mm"])}
<h2 class="mt4">Différencier et remédier</h2>{table(["Difficulté", "Remédiation"], [["Ordre des jours / mois", "Chanson quotidienne ; frise au mur ; cartes à remettre dans l'ordre (chronomètre)."], ["Lecture de l'heure", "Horloge en carton à chaque cours ; d'abord les heures pleines, puis les demies, puis les minutes de 5 en 5."], ["Nombres 21-69 (soixante / seize…)", "Bingo, dictée quotidienne de 5 nombres, jeu du « nombre mystère »."], ["-e / -es", "Code : tu = 2 lettres → -es (2 lettres) ; affiche « tu → s »."], ["Élève rapide", "Heure à l'oral (et quart, moins le quart) ; calculer des durées ; écrire le calendrier des fêtes de son pays."], ["Alpha : p / b, t / d", "Main sur la gorge : p et t ne vibrent pas ; cartes-syllabes en paires."]], ["50mm", "132mm"])}'''
    T = teacher_book(b, E, "V1 · M3", "", MC, 3, "Le temps qui passe",
                     "<li><b>Communication :</b> dire la date, l'heure, son anniversaire, parler de son horaire et de sa semaine.</li><li><b>Lexique :</b> jours, mois, saisons, heure, fêtes, journal de classe, vacances.</li><li><b>Grammaire :</b> présent des verbes en -er (singulier), quel/quelle, à + heure, en + mois/saison.</li><li><b>Phonétique :</b> [e]/[ɛ], liaisons avec les nombres (deux‿heures, neuf‿heures).</li><li><b>FLSco :</b> calendrier scolaire, journal de classe, tableau à double entrée.</li><li><b>★ Alpha :</b> étapes 2-3 — p, t, d, n ; syllabes inversées ; mots de 2-3 syllabes ; premières phrases.</li>",
                     '<p class="sm"><b style="color:#E4572E">Indispensable</b> : jours, date, heure (pleines et demies), journal de classe.</p><p class="sm"><b style="color:#d9a400">Important</b> : mois, saisons, nombres jusqu\'à 69, -e/-es.</p><p class="sm"><b style="color:#2BA88F">Enrichissement</b> : et quart / moins le quart, liaisons, fêtes du monde.</p>',
                     "Horloge de la classe · horloges en carton + attaches parisiennes · calendrier mural · journaux de classe réels des élèves · jetons (bingo).",
                     "<b>Rituel clé :</b> à partir de ce module, un élève écrit chaque matin la date et l'heure au tableau. C'est la meilleure révision en spirale.",
                     days, "Date et heure au tableau par un élève · « Quel jour sommes-nous ? Quel jour demain ? » · anniversaires de la semaine · lecture du journal de classe.", rot, key, (ev1, ev2), start=tstart)
    if render:
        to_pdf(T.html(), '/home/claude/syllabus/out/V1_M3_prof.pdf')
    return b, T


if __name__ == "__main__":
    b, T = build_m3()
    print(b.n, T.n)
