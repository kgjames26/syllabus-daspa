"""Volume 2 · Module 6 « Découvrir la Belgique » (A2)."""
import sys
sys.path.insert(0, '/home/claude/syllabus')
from lib.base import *
from lib.art import *
from lib.module import *
from lib.v2 import CP, CPCOL
from lib.render import to_pdf

MC = "#C0392B"
TINT = "#FDF0E6"
K = 150  # pixels SVG par degré de latitude


def P(lon, lat):
    return (lon - 2.45) * K * 0.636 + 6, (51.6 - lat) * K + 4


def poly(pts):
    return " ".join(f"{P(a, b)[0]:.1f},{P(a, b)[1]:.1f}" for a, b in pts)


BEL = [(2.55, 51.09), (3.37, 51.37), (3.9, 51.36), (4.24, 51.37), (4.79, 51.50), (5.10, 51.43), (5.48, 51.30), (5.84, 51.16), (5.76, 50.95), (5.69, 50.76), (6.02, 50.75), (6.27, 50.63), (6.40, 50.33), (6.13, 50.13),
       (5.97, 50.17), (5.75, 49.79), (5.90, 49.50), (5.47, 49.50), (5.10, 49.70), (4.85, 49.80), (4.87, 50.14), (4.66, 49.97), (4.20, 49.96), (4.14, 50.25), (3.70, 50.30), (3.29, 50.53), (3.10, 50.78), (2.90, 50.69), (2.63, 50.80)]
FLA = BEL[:10] + [(5.0, 50.76), (4.6, 50.74), (4.15, 50.71), (3.6, 50.73), (3.10, 50.78), (2.90, 50.69), (2.63, 50.80)]
GER = [(6.02, 50.75), (6.27, 50.63), (6.40, 50.33), (6.13, 50.13), (5.97, 50.25), (6.0, 50.45), (5.88, 50.62)]
VILLES = [("Bruxelles", 4.35, 50.85, "cap"), ("Anvers", 4.40, 51.22, "v"), ("Gand", 3.72, 51.05, "v"), ("Bruges", 3.22, 51.21, "v"), ("Liège", 5.57, 50.63, "v"), ("Namur", 4.87, 50.47, "capr"), ("Charleroi", 4.44, 50.41, "v"),
          ("Mons", 3.95, 50.45, "v"), ("Arlon", 5.82, 49.68, "v"), ("Eupen", 6.03, 50.63, "v"), ("Binche", 4.17, 50.41, "p"), ("Dinant", 4.91, 50.26, "p")]
MEUSE = [(4.83, 50.10), (4.91, 50.26), (4.87, 50.47), (5.24, 50.52), (5.57, 50.63), (5.69, 50.76), (5.76, 50.95), (5.84, 51.16)]
SAMBRE = [(4.15, 50.27), (4.44, 50.41), (4.87, 50.47)]
ESCAUT = [(3.45, 50.48), (3.39, 50.61), (3.55, 50.80), (3.72, 51.05), (4.10, 51.10), (4.40, 51.22), (4.27, 51.37)]


def carte(w="100%", legend=True, names=True, quiz=False):
    out = [f'<polygon points="{poly(BEL)}" fill="#FCE3B0" stroke="#1F2A44" stroke-width="1.6"/>', f'<polygon points="{poly(FLA)}" fill="#FFF3C4" stroke="none"/>', f'<polygon points="{poly(GER)}" fill="#F7C9A8" stroke="none"/>',
           f'<polygon points="{poly(BEL)}" fill="none" stroke="#1F2A44" stroke-width="1.6"/>', f'<polyline points="{poly(FLA[9:])}" fill="none" stroke="#7a8193" stroke-width="1" stroke-dasharray="4 3"/>']
    for riv, nm, at in [(MEUSE, "Meuse", 1), (SAMBRE, "Sambre", 0), (ESCAUT, "Escaut", 2)]:
        out.append(f'<polyline points="{poly(riv)}" fill="none" stroke="#3A86FF" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>')
        if names and not quiz:
            x, y = P(*riv[at])
            out.append(f'<text x="{x + 5:.0f}" y="{y + 12:.0f}" font-size="9" fill="#2563c9" font-style="italic" font-family="Poppins">{nm}</text>')
    bx, by = P(4.35, 50.85)
    out.append(f'<circle cx="{bx:.0f}" cy="{by:.0f}" r="11" fill="#F4A6A6" stroke="#1F2A44" stroke-width=".8"/>')
    for i, (nm, lo, la, t) in enumerate(VILLES):
        x, y = P(lo, la)
        if t == "cap":
            out.append(f'<rect x="{x - 4:.0f}" y="{y - 4:.0f}" width="8" height="8" fill="{MC}" stroke="#1F2A44"/>')
        elif t == "capr":
            out.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="5" fill="#fff" stroke="{MC}" stroke-width="3"/>')
        elif t == "v":
            out.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="3.6" fill="#1F2A44"/>')
        else:
            out.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="2.4" fill="#fff" stroke="#1F2A44" stroke-width="1.2"/>')
        lab = str(i + 1) if quiz else nm
        if names:
            dx, dy = {"Bruxelles": (13, 4), "Eupen": (-38, 4), "Liège": (-30, -6), "Arlon": (-34, 4), "Charleroi": (4, 15), "Binche": (-22, 15), "Mons": (-32, 4), "Dinant": (6, 4), "Namur": (7, -4)}.get(nm, (6, 4))
            if quiz:
                dx, dy = 6, 4
            out.append(f'<text x="{x + dx:.0f}" y="{y + dy:.0f}" font-size="{10 if not quiz else 11}" font-weight="700" font-family="Poppins">{lab}</text>')
    tx, ty = P(6.09, 50.50)
    out.append(f'<path d="M{tx:.0f} {ty - 6:.0f} l5 9 h-10z" fill="#6B4A2B"/>')
    if names and not quiz:
        out.append(f'<text x="{tx - 58:.0f}" y="{ty + 16:.0f}" font-size="8.5" font-family="Poppins">Botrange 694 m</text>')
    sx, sy = P(2.6, 49.75)
    L = 50 / 111 * K
    out.append(f'<rect x="{sx:.0f}" y="{sy:.0f}" width="{L:.0f}" height="5" fill="#1F2A44"/><rect x="{sx + L / 2:.0f}" y="{sy:.0f}" width="{L / 2:.0f}" height="5" fill="#fff" stroke="#1F2A44"/><text x="{sx:.0f}" y="{sy + 16:.0f}" font-size="9" font-family="Poppins">0</text><text x="{sx + L - 14:.0f}" y="{sy + 16:.0f}" font-size="9" font-family="Poppins">50 km</text>')
    nx, ny = P(2.75, 51.5)
    out.append(f'<path d="M{nx:.0f} {ny + 18:.0f} L{nx:.0f} {ny - 6:.0f} M{nx - 6:.0f} {ny + 2:.0f} L{nx:.0f} {ny - 8:.0f} L{nx + 6:.0f} {ny + 2:.0f}" stroke="#1F2A44" stroke-width="2" fill="none"/><text x="{nx - 4:.0f}" y="{ny - 11:.0f}" font-size="11" font-weight="800" font-family="Poppins">N</text>')
    for nm, lo, la in [("MER DU NORD", 2.9, 51.5), ("PAYS-BAS", 4.6, 51.56), ("ALLEMAGNE", 5.95, 51.02), ("FRANCE", 3.0, 50.1), ("LUX.", 6.05, 49.75)]:
        x, y = P(lo, la)
        out.append(f'<text x="{x:.0f}" y="{y:.0f}" font-size="8.5" fill="#7a8193" font-family="Poppins" letter-spacing="1">{nm}</text>')
    W, H = P(6.6, 49.4)
    svg = f'<svg viewBox="0 0 {W:.0f} {H:.0f}" width="{w}">{"".join(out)}</svg>'
    if not legend:
        return svg
    leg = "".join(f'<div class="flex xs" style="gap:2mm;margin-bottom:1mm"><span style="display:inline-block;width:6mm;height:4mm;{st}"></span>{t}</div>' for st, t in [
        (f"background:{MC};width:3.5mm;height:3.5mm", "capitale du pays"), (f"border:2.5px solid {MC};border-radius:50%;width:4mm", "capitale de la Wallonie"), ("background:#1F2A44;border-radius:50%;width:3mm;height:3mm", "grande ville"),
        ("border:1.5px solid #1F2A44;border-radius:50%;width:2.5mm;height:2.5mm", "petite ville"), ("background:#FFF3C4;border:1px solid #ccc", "Région flamande"), ("background:#FCE3B0;border:1px solid #ccc", "Région wallonne"),
        ("background:#F4A6A6;border-radius:50%", "Région de Bruxelles-Capitale"), ("background:#F7C9A8;border:1px solid #ccc", "communes germanophones (en Wallonie)"), ("border-top:2.5px solid #3A86FF;height:0", "fleuve, rivière"),
        ("border-top:1.5px dashed #7a8193;height:0", "limite de région"), ("border-top:2px solid #1F2A44;height:0", "frontière du pays"), ("", "▲ point culminant")])
    return f'<div class="grid2" style="grid-template-columns:2.2fr 1fr;align-items:center;gap:3mm">{svg}<div class="card" style="padding:2mm"><b class="sm">Légende</b>{leg}</div></div>'


def build_v2m6(start=1, tstart=1, render=True):
    b = Book("V2 · M6", "Volume 2 · Je me débrouille · Module 6 · Découvrir la Belgique", MC, start=start)
    E = Ex(b)
    vis = carte("80%", legend=False)
    vis = f'<div class="flex" style="justify-content:center;gap:6mm"><div style="width:110mm">{vis}</div><div class="c" style="font-size:30pt;line-height:1.35">🇧🇪<br>🎭🧇<br>🏰🍟</div></div>'
    opening(b, MC, 6, "Découvrir la Belgique", vis, [("🗺️", "situer les régions, les provinces et les grandes villes"), ("🎭", "présenter une fête, une tradition"), ("⚖️", "comparer (plus… que, moins… que, aussi… que)"),
            ("🏆", "dire le meilleur, le plus grand, le moins cher (superlatif)"), ("🏛️", "comprendre comment la Belgique est organisée"), ("🧭", "lire une carte et sa légende")],
            ["Tu connais quelles villes belges ?", "Quelle fête de Belgique tu as déjà vue ?", "Qu'est-ce qui est différent de ton pays ?"],
            ["la région", "la province", "la commune", "la ville", "la fête", "la tradition", "le fleuve", "plus… que", "le plus…", "la légende"], TINT)

    # ---------- Découvrir ----------
    bd = '<div class="grid2" style="gap:3mm">' + "".join([
        bd_case(1, lr("prof", ["En juin, on part en excursion ! Regardez la carte : nous sommes ici, à Namur, la capitale de la Wallonie."], extra='<div class="c" style="font-size:22pt">🗺️📍🚌</div>')),
        bd_case(2, lr("daria", ["Namur, c'est plus petit que Bruxelles ?"], "prof", ["Oui ! Bruxelles est beaucoup plus grande. Et Anvers est la plus grande ville du pays."], "pense", "sourire")),
        bd_case(3, lr("bilal", ["En Belgique, on parle combien de langues ?"], "educ", ["Trois : le néerlandais, le français et l'allemand. Le néerlandais est la langue la plus parlée."], "surpris", "sourire")),
        bd_case(4, lr("fatou", ["Et le 21 juillet, c'est quoi ?"], "amina", ["C'est la fête nationale ! Il y a un défilé et un feu d'artifice à Bruxelles."], "pense", "rire")),
        bd_case(5, lr("mateo", ["Moi, j'ai vu le carnaval de Binche. Les Gilles lancent des oranges ! C'est le carnaval le plus beau du monde !"], extra='<div class="c" style="font-size:22pt">🎭🍊🥁</div>', ma="rire")),
        bd_case(6, lr("yonas", ["On peut aller à la mer ? La mer, c'est mieux que la montagne !"], "prof", ["La Belgique n'a pas de vraies montagnes… mais les Ardennes sont aussi belles que la côte !"], "rire", "rire")),
    ]) + '</div>'
    e = E("J'écoute et je lis la BD : on prépare l'excursion.", bd, ["ecoute", "lis"], 1, "A",
          script="Lire deux fois. Montrer Namur, Bruxelles, Anvers, Binche sur une carte murale. Faire repérer les comparaisons : plus petit que, beaucoup plus grande, la plus grande, la plus parlée, le plus beau, mieux que, aussi belles que.", sol="Activité orale.")
    b.page(f'<h2>Découvrir · On prépare l\'excursion</h2>{e}', "Découvrir")
    e = E("Je réponds par une phrase complète.", f"<p>1. Quelle est la capitale de la Wallonie ? {blank('l')}</p><p>2. Quelle est la plus grande ville de Belgique ? {blank('l')}</p><p>3. Quelles sont les trois langues officielles ? {blank('xl')}</p><p>4. Que se passe-t-il le 21 juillet ? {blank('xl')}</p><p>5. Que lancent les Gilles de Binche ? {blank('l')}</p>",
          ["lis", "ecris"], 1, "B", sol="1. Namur — 2. Anvers — 3. le néerlandais, le français et l'allemand — 4. la fête nationale : défilé et feu d'artifice à Bruxelles — 5. des oranges")
    e2 = E("Je relève dans la BD 4 comparaisons. Je les classe.", table(["⚖️ Comparer deux choses (plus… que, aussi… que, mieux que)", "🏆 La première, la meilleure (le plus…)"], [["", ""]], ["91mm", "91mm"]).replace("<td></td>", '<td style="height:26mm"></td>'), ["lis", "ecris"], 2, "B",
           sol="Comparer : plus petit que, beaucoup plus grande, mieux que la montagne, aussi belles que la côte · Le premier : la plus grande ville, la langue la plus parlée, le carnaval le plus beau")
    e3 = E("Et toi ? Quelle ville ou quel endroit de Belgique tu veux visiter ? Pourquoi ? (2 phrases)", lines(2), ["ecris"], 2, "C", sol="Réponse personnelle.")
    b.page(f'{e}{e2}{e3}', "Découvrir")
    fiche = '''<div class='card' style='background:#FFFBF5;line-height:1.55'><h3 style='margin-top:0;color:''' + MC + '''\'>La Belgique en bref</h3>
<p>La Belgique est un petit pays d'Europe de l'Ouest. Elle a des frontières avec la France, le Luxembourg, l'Allemagne et les Pays-Bas, et une côte de 67 km sur la mer du Nord. Le 1er janvier 2025, elle comptait <b>presque 11,8 millions d'habitants</b>.</p>
<p>La Belgique est indépendante depuis <b>1830</b>. C'est une <b>monarchie constitutionnelle</b> : le chef de l'État est le roi (le roi Philippe depuis 2013), mais ce sont le Parlement et le gouvernement qui décident des lois.</p>
<p>C'est aussi un <b>État fédéral</b>. Il y a <b>trois Régions</b> (la Région flamande, la Région wallonne et la Région de Bruxelles-Capitale) et <b>trois Communautés</b> qui s'occupent par exemple de l'école et de la culture : la Communauté flamande, la Communauté française (on dit aussi Fédération Wallonie-Bruxelles) et la Communauté germanophone. Le pays a <b>dix provinces</b> et plus de 500 <b>communes</b>. Chaque commune a un <b>bourgmestre</b>.</p>
<p>Bruxelles est la capitale de la Belgique… et aussi une capitale de l'Europe : la Commission européenne et le Conseil de l'Union européenne y ont leur siège.</p></div>'''
    e = E("Je lis la fiche. Je réponds.", fiche + f"<p class='mt2'>1. Combien de pays voisins a la Belgique ? Lesquels ? {blank('xl')}</p><p>2. Depuis quand la Belgique est-elle indépendante ? {blank()}</p><p>3. Qui est le chef de l'État ? {blank('l')}</p><p>4. Quelle Communauté organise ton école ? {blank('l')}</p><p>5. Comment s'appelle le chef d'une commune ? {blank()}</p>", ["lis", "ecris"], 2, "B",
          sol="1. quatre : la France, le Luxembourg, l'Allemagne, les Pays-Bas — 2. depuis 1830 — 3. le roi Philippe — 4. la Communauté française (Fédération Wallonie-Bruxelles) — 5. le bourgmestre")
    b.page(f'<h2>Découvrir · La Belgique en bref</h2>{e}', "Découvrir")

    # ---------- Lexique ----------
    e = E("Le pays et son organisation. J'écoute et je répète.", emogrid([("🇧🇪", "le pays, l'État"), ("🗺️", "la région"), ("🧩", "la province"), ("🏘️", "la commune"), ("👑", "le roi, la reine"), ("🏛️", "le parlement"), ("🗳️", "voter, l'élection"), ("📜", "la loi"),
                                                                                      ("🎩", "le / la bourgmestre"), ("🏙️", "la capitale"), ("🗣️", "la langue officielle"), ("🇪🇺", "l'Union européenne")], 6), ["ecoute", "repete"], 1, "A",
          script="Lire chaque mot. Expliquer avec un dessin en cercles emboîtés : la commune (la plus petite) → la province → la région → le pays → l'Union européenne.", sol="Activité orale.")
    e2 = E("Du plus petit au plus grand. Je numérote de 1 à 5.", "<p class='big'>___ la province &nbsp; ___ la commune &nbsp; ___ l'Union européenne &nbsp; ___ la Région wallonne &nbsp; ___ la Belgique</p>", ["numerote"], 1, "B", sol="province 2 · commune 1 · Union européenne 5 · Région wallonne 3 · Belgique 4")
    e3 = E("Je complète avec les mots de l'encadré.", "<p class='sm'>bourgmestre · roi · capitale · langues · commune</p><p>1. J'habite à Jambes : c'est une partie de la ______ de Namur. 2. Le ______ de ma commune s'occupe de la police et de la sécurité. 3. Philippe est le ______ des Belges. 4. Bruxelles est la ______ du pays. 5. La Belgique a trois ______ officielles.</p>", ["complete"], 1, "C",
           sol="1. commune — 2. bourgmestre — 3. roi — 4. capitale — 5. langues")
    b.page(f'<h2>Les mots du pays</h2>{e}{e2}{e3}', "Lexique")
    e = E("Le paysage. J'écoute et je répète.", emogrid([("🌊", "la mer, la côte"), ("🏖️", "la plage, les dunes"), ("🌲", "la forêt"), ("⛰️", "la colline"), ("🏞️", "la vallée"), ("💧", "le fleuve, la rivière"), ("🌾", "la campagne"), ("🏭", "l'industrie"),
                                                         ("🏰", "le château, la citadelle"), ("⛪", "la cathédrale"), ("🧱", "le beffroi"), ("🚢", "le port")], 6), ["ecoute", "repete"], 1, "A",
          script="Lire chaque mot. Associer : la côte (Ostende, La Panne), les Ardennes (forêts, collines), la Meuse (vallée), Anvers (port), les beffrois (Mons, Tournai, Bruges).", sol="Activité orale.")
    e2 = E("Je relie le lieu et sa description.", relie(["la côte belge", "les Ardennes", "Anvers", "la Meuse", "la citadelle de Namur"], ["un grand port sur l'Escaut", "un fleuve qui traverse Namur et Liège", "une forteresse sur une colline", "des forêts, des collines, des rivières", "67 km de plages et de dunes"]), ["relie"], 1, "B",
           sol="côte → 67 km de plages · Ardennes → forêts, collines · Anvers → port sur l'Escaut · Meuse → fleuve Namur-Liège · citadelle → forteresse sur une colline")
    b.page(f'<h2>Les mots du paysage</h2>{e}{e2}', "Lexique")
    fetes = [("🎊", "1er janvier", "le Nouvel An"), ("🎭", "février-mars", "le carnaval (Binche, Malmedy…)"), ("🐉", "dimanche de la Trinité", "le Doudou à Mons"), ("🇧🇪", "21 juillet", "la fête nationale"),
             ("🐓", "3e week-end de septembre", "les Fêtes de Wallonie (Namur)"), ("🏫", "27 septembre", "la fête de la Fédération Wallonie-Bruxelles (congé scolaire)"), ("🕯️", "1er novembre", "la Toussaint"), ("🎁", "6 décembre", "la Saint-Nicolas")]
    e = E("Les fêtes et les traditions en Belgique. J'écoute et je lis.", table(["", "Quand ?", "Quoi ?"], [[f'<span style="font-size:14pt">{a}</span>', f"<b>{q}</b>", t] for a, q, t in fetes], ["12mm", "62mm", "108mm"]), ["ecoute", "lis"], 1, "A",
          script="Lire le tableau. Préciser : à la Saint-Nicolas, les enfants reçoivent des cadeaux et des friandises (spéculoos, mandarines, chocolat) ; au Doudou, saint Georges combat le dragon sur la Grand-Place de Mons (le « Lumeçon »). Demander : « Quelle fête ressemble à une fête de ton pays ? »", sol="Activité orale.")
    e2 = E("Quelle fête ? J'écris le nom.", "<p>1. Les enfants reçoivent des cadeaux et des spéculoos le 6 décembre : ______________</p><p>2. Saint Georges combat le dragon à Mons : ______________</p><p>3. Il y a un défilé militaire à Bruxelles : ______________</p><p>4. Les élèves n'ont pas école le 27 septembre : ______________</p>", ["lis", "ecris"], 1, "B",
           sol="1. la Saint-Nicolas — 2. le Doudou — 3. la fête nationale (21 juillet) — 4. la fête de la Fédération Wallonie-Bruxelles")
    b.page(f'<h2>Les mots des fêtes</h2>{e}{e2}', "Lexique")
    bel = table(["En Belgique, on dit…", "Ça veut dire…", "Exemple"], [["le / la <b>bourgmestre</b> (à Liège : le <b>mayeur</b>)", "le maire", "La bourgmestre inaugure le parc."], ["un <b>échevin</b>, une <b>échevine</b>", "un adjoint au maire", "L'échevin des sports visite l'école."], ["une <b>drache</b>", "une grosse averse, une pluie forte", "Quelle drache ce matin !"], ["un <b>kot</b>", "une chambre d'étudiant", "Mon frère loue un kot à Louvain-la-Neuve."], ["<b>septante</b>, <b>nonante</b>", "soixante-dix, quatre-vingt-dix", "La Belgique est indépendante depuis 1830 : mille huit cent trente."]], ["58mm", "54mm", "70mm"])
    e = E("Je lis les belgicismes. Je réécris les phrases en français de France.", bel + "<p class='mt2'>1. L'échevine de la culture organise la fête. → ______________________________</p><p>2. Prends ton parapluie, il va dracher ! → ______________________________</p><p>3. Le bourgmestre de Namur parle aux habitants. → ______________________________</p>", ["lis", "ecris"], 2, "B",
          sol="1. L'adjointe au maire chargée de la culture… — 2. il va pleuvoir très fort — 3. Le maire de Namur…")
    e2 = E("Les spécialités. Je relie la spécialité et sa description.", relie(["🧇 la gaufre de Liège", "🍟 les frites", "🍫 la praline", "🍪 le spéculoos", "🥘 la carbonnade flamande"], ["un biscuit à la cannelle (Saint-Nicolas)", "un bonbon de chocolat fourré", "du bœuf cuit à la bière", "des pommes de terre frites, souvent avec une sauce", "une gaufre au sucre perlé"]), ["relie"], 1, "B",
           sol="gaufre de Liège → sucre perlé · frites → pommes de terre · praline → chocolat fourré · spéculoos → biscuit à la cannelle · carbonnade → bœuf à la bière")
    b.page(f'<h2>🇧🇪 Les mots d\'ici · belgicismes et spécialités</h2>{e}{e2}', "Lexique")

    # ---------- Leçon 1 : le comparatif ----------
    l1 = lecon("Comparer : le comparatif", table(["", "avec un adjectif", "avec un nom", "avec un verbe"], [["➕ supériorité", "Bruxelles est <b>plus</b> grande <b>que</b> Namur.", "Anvers a <b>plus d'</b>habitants <b>que</b> Gand.", "Il pleut <b>plus que</b> chez moi."], ["➖ infériorité", "Namur est <b>moins</b> grande <b>que</b> Liège.", "Arlon a <b>moins d'</b>habitants <b>que</b> Mons.", "Je voyage <b>moins que</b> toi."], ["🟰 égalité", "Les Ardennes sont <b>aussi</b> belles <b>que</b> la côte.", "J'ai <b>autant de</b> cours <b>que</b> toi.", "Il travaille <b>autant que</b> moi."]], ["30mm", "54mm", "52mm", "46mm"]) +
               '<div class="attention" style="margin:2mm 0 0">⚠️ L\'adjectif s\'accorde : Bruxelles est plus grand<b>e</b>. · bon → <b>meilleur</b> (pas « plus bon ») : Les frites belges sont <b>meilleures que</b>… · bien → <b>mieux</b> : Je parle <b>mieux</b> français <b>qu\'</b>avant. · mauvais → plus mauvais / <b>pire</b>.</div>'
               '<p class="sm">Pour insister : <b>beaucoup</b> plus / <b>un peu</b> moins / <b>bien</b> plus. Après <b>que</b>, on utilise le pronom tonique : plus grand que <b>moi</b>, <b>toi</b>, <b>lui</b>, <b>elle</b>…</p>')
    e = E("Je compare avec plus… que (+), moins… que (−) ou aussi… que (=).", "<p>1. La Meuse (+ long) ______________ la Sambre. 2. Namur (− grand) ______________ Liège. 3. Le train (= pratique) ______________ le bus. 4. En hiver, les journées (− long) ______________ en été. 5. Ma ville (+ calme) ______________ Bruxelles.</p>", ["complete"], 1, "C",
          sol="1. est plus longue que — 2. est moins grande que — 3. est aussi pratique que — 4. sont moins longues qu' — 5. est plus calme que")
    b.page(f'{l1}{e}', "Leçon 1")
    villes = table(["Ville", "Habitants (environ, 2025)", "Province", "Un monument"], [["Anvers", "540 000", "Anvers", "la cathédrale Notre-Dame"], ["Charleroi", "205 000", "Hainaut", "le beffroi"], ["Liège", "197 000", "Liège", "l'escalier de la Montagne de Bueren"], ["Namur", "114 000", "Namur", "la citadelle"], ["Mons", "96 000", "Hainaut", "le beffroi (UNESCO)"], ["Arlon", "31 000", "Luxembourg", "la tour romaine"]], ["32mm", "50mm", "40mm", "60mm"])
    e = E("Je lis le tableau. J'écris 5 phrases de comparaison (habitants : plus d'… que, moins d'… que, autant d'… que).", villes + "<p class='xs muted'>Chiffres arrondis.</p>" + lines(4), ["lis", "ecris"], 2, "C",
          sol="Ex. : Anvers a plus d'habitants que Charleroi. Namur a moins d'habitants que Liège. Charleroi a un peu plus d'habitants que Liège. Arlon a beaucoup moins d'habitants que Mons. Mons et Charleroi sont dans la même province (le Hainaut).")
    e2 = E("Bon ou bien ? Meilleur ou mieux ? Je complète.", "<p>1. Cette gaufre est ______ que l'autre. 2. Tu chantes ______ que moi ! 3. Le train est une ______ solution que la voiture pour aller à Bruxelles. 4. Aujourd'hui, je me sens ______ qu'hier.</p>", ["complete"], 2, "C", sol="1. meilleure — 2. mieux — 3. meilleure — 4. mieux")
    b.page(f'{e}{e2}', "S'entraîner")
    e = E("J'écoute Daria comparer Kyiv et Namur. Je coche + (plus), − (moins) ou = (aussi).", table(["Kyiv est … que Namur", "+", "−", "="], [[x, '<span class="chk"></span>', '<span class="chk"></span>', '<span class="chk"></span>'] for x in ["grande", "vieille (ancienne)", "froide en hiver", "verte (parcs)", "chère"]], ["110mm", "24mm", "24mm", "24mm"]), ["ecoute", "coche"], 2, "A",
          script="« Kyiv est beaucoup plus grande que Namur : il y a presque trois millions d'habitants ! Les deux villes sont aussi anciennes l'une que l'autre : elles ont plus de mille ans. En hiver, Kyiv est plus froide : il y a souvent de la neige. Namur est aussi verte que Kyiv, avec beaucoup de parcs et de forêts autour. Et la vie est moins chère à Kyiv qu'ici. »",
          sol="grande + · ancienne = · froide + · verte = · chère −")
    e2 = E("Mon pays et la Belgique. J'écris 5 phrases de comparaison (climat, taille, nourriture, école, langues…).", "<p class='sm'>Ex. : En Syrie, il fait plus chaud qu'en Belgique. L'école commence plus tôt ici.</p>" + lines(5), ["ecris"], 2, "C", sol="Comparaisons personnelles, accords justes.")
    e3 = E("Jeu « Qui est le plus… ? » : en groupe, on compare deux élèves (avec leur accord !), deux villes, deux plats : « Le couscous est aussi bon que les frites ! » La classe vote.", "", ["parle", "groupe", "joue"], 1, "A", sol="Comparaisons orales, respect de chacun.")
    b.page(f'{e}{e2}{e3}', "S'entraîner")

    # ---------- Leçon 2 : le superlatif ----------
    l2 = lecon("Dire le premier, le dernier : le superlatif", '''<div class='grid2'><div class='card' style='background:#fff'><b>🏆 le / la / les + plus + adjectif (+ de…)</b><p class='sm'>Anvers est <b>la plus</b> grande ville <b>de</b> Belgique.<br>La Meuse est <b>le plus</b> long fleuve <b>de</b> Wallonie.<br>Botrange est <b>le point le plus</b> haut <b>du</b> pays.</p></div>
<div class='card' style='background:#fff'><b>🔻 le / la / les + moins + adjectif</b><p class='sm'>Arlon est <b>la</b> ville <b>la moins</b> peuplée du tableau.<br>C'est <b>le</b> chemin <b>le moins</b> long.</p></div></div>
<p class='mt2'>Avec un nom : <b>le plus de</b> / <b>le moins de</b> → C'est Anvers qui a <b>le plus d'</b>habitants. · Avec un verbe : C'est Yonas qui court <b>le plus vite</b>.</p>
<div class='attention' style='margin:1mm 0'>⚠️ bon → <b>le meilleur</b>, <b>la meilleure</b> · bien → <b>le mieux</b> · Place : si l'adjectif est après le nom, on répète l'article : la ville <b>la plus</b> belle ; les fêtes <b>les plus</b> connues.</div>''')
    e = E("Je forme le superlatif (+ ou −).", "<p>1. Le Doudou est une fête (+ connu) ______________ de Mons. 2. Botrange est l'endroit (+ haut) ______________ de Belgique. 3. Le carnaval de Binche est (+ célèbre) ______________ du pays. 4. Février est le mois (− long) ______________ de l'année. 5. C'est la gaufre (+ bon) ______________ de la ville !</p>", ["complete"], 1, "C",
          sol="1. la plus connue — 2. le plus haut — 3. le plus célèbre — 4. le moins long (le plus court) — 5. la meilleure")
    e2 = E("J'écoute le guide. Je complète les records.", "<p>1. La Grand-Place de Bruxelles est une des places ______________ d'Europe. 2. Le port d'Anvers est le ______________ port de Belgique. 3. La citadelle de Namur est une des ______________ forteresses d'Europe. 4. Pour Yonas, les frites de la friterie de l'école sont ______________ !</p>", ["ecoute", "complete"], 2, "A",
           script="« 1. Voici la Grand-Place de Bruxelles : c'est une des places les plus belles d'Europe. 2. Le port d'Anvers est le plus grand port de Belgique. 3. La citadelle de Namur est une des plus grandes forteresses d'Europe. 4. Et Yonas dit : les frites de la friterie de l'école sont les meilleures ! »",
           sol="1. les plus belles — 2. plus grand — 3. plus grandes — 4. les meilleures")
    e3 = E("Comparatif (2 choses) ou superlatif (le n° 1) ? J'écris C ou S.", "<p>___ Liège est plus grande que Namur. ___ C'est la plus belle fête. ___ Mons est aussi joli que Tournai. ___ Anvers a le plus d'habitants. ___ Je cours moins vite que toi. ___ C'est le meilleur gâteau du monde.</p>", ["lis", "ecris"], 1, "B", sol="C · S · C · S · C · S")
    b.page(f'{l2}{e}{e2}{e3}', "Leçon 2")
    e = E("Je lis le tableau des villes (page précédente). Je réponds avec un superlatif.", "<p>1. Quelle ville a le plus d'habitants ? ______________________________</p><p>2. Quelle ville a le moins d'habitants ? ______________________________</p><p>3. Quelle est la plus grande ville de Wallonie dans le tableau ? ______________________________</p>", ["lis", "ecris"], 2, "B",
          sol="1. C'est Anvers qui a le plus d'habitants. — 2. C'est Arlon qui a le moins d'habitants. — 3. C'est Charleroi.")
    e2 = E("Le quiz des records belges. J'entoure la bonne réponse, puis je vérifie avec la prof.", "<p>1. Le plus long fleuve de Wallonie : la Meuse / la Sambre / l'Ourthe</p><p>2. Le point le plus haut de Belgique : Botrange (694 m) / le Mont-Blanc / la citadelle de Namur</p><p>3. La langue la plus parlée en Belgique : le français / le néerlandais / l'allemand</p><p>4. La plus petite des trois Régions : la Flandre / la Wallonie / Bruxelles-Capitale</p>", ["lis", "entoure"], 2, "B",
           sol="1. la Meuse — 2. Botrange (694 m) — 3. le néerlandais — 4. la Région de Bruxelles-Capitale")
    e4 = E("Je transforme la phrase au superlatif avec le mot entre parenthèses.", "<p>1. Anvers est une grande ville. (de Belgique) → ______________________________</p><p>2. Le Doudou est une fête connue. (de Mons) → ______________________________</p><p>3. C'est un bon restaurant. (du quartier) → ______________________________</p>", ["ecris"], 2, "C",
           sol="1. Anvers est la plus grande ville de Belgique. — 2. Le Doudou est la fête la plus connue de Mons. — 3. C'est le meilleur restaurant du quartier.")
    e3 = E("Défi ! Mes records : j'écris 4 phrases au superlatif sur ma vie (le plus beau jour, le meilleur plat, la ville la plus…, le moment le plus difficile).", lines(4), ["ecris"], 3, "C", sol="Superlatifs corrects (accord, article, de).")
    b.page(f'{e}{e2}{e4}{e3}', "S'entraîner")

    # ---------- Leçon 3 : situer ----------
    l3 = lecon("Situer un lieu", table(["Pour…", "Je dis…"], [["une ville", "<b>à</b> Namur, <b>à</b> Bruxelles · (attention : <b>au</b> Caire, <b>à la</b> Louvière)"], ["un pays féminin (finit souvent par -e) ou une région", "<b>en</b> Belgique, <b>en</b> France, <b>en</b> Syrie · <b>en</b> Wallonie, <b>en</b> Flandre"], ["un pays masculin", "<b>au</b> Luxembourg, <b>au</b> Maroc, <b>au</b> Congo"], ["un pays pluriel", "<b>aux</b> Pays-Bas, <b>aux</b> États-Unis"], ["une province, une zone", "<b>dans</b> la province de Liège, <b>dans</b> les Ardennes, <b>à</b> la côte (belgicisme courant), <b>au bord de</b> la mer"]], ["60mm", "122mm"]) +
               '''<div class='grid2 mt2'><div class='card' style='background:#fff'><b>🧭 Les points cardinaux</b><p class='sm'>au <b>nord</b> de · au <b>sud</b> de · à l'<b>est</b> de · à l'<b>ouest</b> de · au <b>centre</b> de · au nord-est de…<br>Liège est <b>à l'est de</b> Namur. Arlon est <b>au sud du</b> pays.</p></div>
<div class='card' style='background:#fff'><b>📏 La distance</b><p class='sm'><b>près de</b> · <b>loin de</b> · <b>à</b> 60 km <b>de</b> · <b>entre</b> … et … · <b>au bord de</b> la Meuse · <b>sur</b> la côte<br>Namur est <b>à</b> 60 km <b>de</b> Bruxelles, <b>entre</b> Charleroi et Liège.</p></div></div>''')
    e = E("À, en, au ou aux ? Je complète.", "<p>1. J'habite ___ Charleroi, ___ Belgique. 2. Mon oncle vit ___ Pays-Bas. 3. Bilal est né ___ Maroc. 4. Les Ardennes sont ___ Wallonie. 5. On va ___ Luxembourg pour l'excursion. 6. Ma cousine habite ___ Liège.</p>", ["complete"], 1, "C",
          sol="1. à · en — 2. aux — 3. au — 4. en — 5. au — 6. à")
    e2 = E("Je classe les pays : en (féminin), au (masculin) ou aux (pluriel) ?", table(["en …", "au …", "aux …"], [["", "", ""]], ["61mm", "61mm", "60mm"]).replace("<td></td>", '<td style="height:20mm"></td>') + "<p class='sm mt2'>Syrie · Maroc · Pays-Bas · Ukraine · Congo · Afghanistan (au, mais en devant voyelle : en Afghanistan !) · Érythrée · États-Unis · Brésil · Guinée · Portugal · Philippines</p>", ["lis", "ecris"], 2, "C",
           sol="en : Syrie, Ukraine, Érythrée, Guinée, Afghanistan (masculin, mais commence par une voyelle) · au : Maroc, Congo, Brésil, Portugal · aux : Pays-Bas, États-Unis, Philippines")
    b.page(f'{l3}{e}{e2}', "Leçon 3")
    e = E("Je regarde la carte. Je situe les villes avec les points cardinaux.", carte("100%", legend=False) + "<p>1. Liège est ______________ de Namur. 2. Bruges est ______________ du pays. 3. Arlon est ______________ de la Belgique. 4. Mons est ______________ de Bruxelles. 5. Namur est ______________ Charleroi et Liège.</p>", ["regarde", "ecris"], 2, "B",
          sol="1. à l'est — 2. au nord-ouest — 3. au sud — 4. au sud-ouest — 5. entre")
    b.page(f'{e}', "S'entraîner")
    e = E("Devinettes : je lis et je trouve la ville sur la carte.", "<p>1. Je suis au bord de la Meuse, à l'est de Namur, dans une grande province francophone. Je suis… ______________</p><p>2. Je suis au nord du pays, sur l'Escaut. J'ai un très grand port. Je suis… ______________</p><p>3. Je suis la capitale de la Belgique et une capitale de l'Europe. Je suis… ______________</p><p>4. Je suis la ville la plus au sud du pays, près du Luxembourg. Je suis… ______________</p>", ["lis", "ecris"], 2, "B",
          sol="1. Liège — 2. Anvers — 3. Bruxelles — 4. Arlon")
    e2 = E("J'écoute le guide dans le bus. Je trace le trajet sur la carte de la page précédente et je note les villes dans l'ordre.", f"<p>Départ : Namur → {blank()} → {blank()} → {blank()} → retour à Namur</p>", ["ecoute", "trace", "ecris"], 2, "A",
           script="« Bonjour à tous ! Nous partons de Namur et nous suivons la Meuse vers le sud. Notre premier arrêt est à Dinant, la ville d'Adolphe Sax, l'inventeur du saxophone. Ensuite, nous allons vers l'ouest, jusqu'à Binche, la ville du carnaval. Après le dîner, nous continuons vers l'ouest jusqu'à Mons pour voir le beffroi. Et ce soir, retour à Namur ! »",
           sol="Dinant → Binche → Mons (trajet : sud puis ouest)")
    e3 = E("Je présente ma ville ou mon village d'origine : où ? (pays, région, points cardinaux, distance d'une grande ville). 3 phrases.", lines(3), ["ecris"], 2, "C", sol="Ex. : Je viens de Homs, en Syrie. Homs est au centre du pays, à 160 km au nord de Damas.")
    b.page(f'{e}{e2}{e3}', "S'entraîner")

    # ---------- Leçon 4 : présenter une fête, une tradition ----------
    l4 = lecon("Présenter une fête, une tradition", table(["Je présente…", "Je dis…"], [["le nom, le lieu, la date", "Le Doudou est une fête de Mons. Elle a lieu chaque année, le dimanche de la Trinité (en mai ou en juin)."], ["l'origine", "C'est une tradition très ancienne : elle date du Moyen Âge. / Elle existe depuis 1380."], ["ce qu'on fait", "Les gens <b>se réunissent</b> sur la Grand-Place. <b>On</b> chante, <b>on</b> danse, <b>on</b> mange…"], ["ce qu'on porte, ce qu'on mange", "Les Gilles portent un costume, un masque de cire et un chapeau à plumes d'autruche."], ["mon avis (avec un superlatif !)", "Pour moi, c'est la fête la plus impressionnante de Wallonie. J'aime surtout…"]], ["52mm", "130mm"]) +
               '<p class="sm mt2"><b>Mots utiles :</b> avoir lieu · se dérouler · célébrer · fêter · un défilé · un cortège · une procession · un géant · un feu d\'artifice · un costume traditionnel · un plat typique. · <b>On</b> = les gens (verbe à la 3ᵉ personne du singulier).</p>')
    e = E("Je lis la présentation de Fatou. Je souligne : le nom (bleu), le lieu et la date (vert), ce qu'on fait (rouge), son avis (noir).", "<div class='card' style='line-height:1.7'>Chez nous, en Guinée, la fête la plus importante pour ma famille, c'est la Tabaski. Elle a lieu chaque année, mais la date change parce qu'elle suit le calendrier lunaire. Le matin, on met nos plus beaux vêtements et on va à la prière. Ensuite, on partage un grand repas avec la famille, les voisins et les personnes pauvres. Pour moi, c'est la fête la plus généreuse de l'année !</div>", ["lis", "souligne"], 1, "B",
          sol="Nom : la Tabaski · Lieu/date : en Guinée, chaque année, date selon le calendrier lunaire · On fait : beaux vêtements, prière, grand repas partagé · Avis : la fête la plus généreuse")
    b.page(f'{l4}{e}', "Leçon 4")
    e = E("Je remets la présentation du carnaval de Binche dans l'ordre (1 à 5).", "<div class='card'>" + "".join(f"<p style='margin:1mm 0'><span class='blank s'></span> {t}</p>" for t in ["Le Mardi gras, les Gilles dansent dans les rues au son des tambours et lancent des oranges.", "Le carnaval de Binche est la fête la plus célèbre de cette petite ville du Hainaut.", "Pour moi, c'est la fête la plus incroyable de Belgique !", "Il a lieu chaque année, en février ou en mars, pendant trois jours.", "Depuis 2003, l'UNESCO le reconnaît comme un trésor du patrimoine de l'humanité."]) + "</div>", ["lis", "numerote"], 2, "B",
          sol="3 · 1 · 5 · 2 · 4")
    e2 = E("J'écoute Mateo présenter une fête de Colombie. Je complète la fiche.", f"<div class='card'><p>Nom : {blank('l')} · Ville : {blank('l')}<br>Quand ? {blank('l')} · Combien de jours ? {blank()}<br>Ce qu'on fait : {blank('xl')}<br>Son avis : {blank('xl')}</p></div>", ["ecoute", "ecris"], 2, "A",
           script="« Je vous présente le carnaval de Barranquilla, en Colombie. Il a lieu chaque année en février ou en mars, quatre jours avant le mercredi des Cendres. Il y a des défilés immenses, des danses, des costumes de toutes les couleurs et beaucoup de musique. Les gens se lancent de la farine et de la mousse ! Pour moi, c'est le carnaval le plus joyeux du monde… même plus joyeux que le carnaval de Binche ! »",
           sol="carnaval de Barranquilla · Barranquilla (Colombie) · février ou mars · 4 jours · défilés, danses, costumes, musique, on se lance de la farine et de la mousse · le plus joyeux du monde, plus joyeux que Binche")
    e3 = E("À mon tour : je présente une fête de mon pays ou de ma famille (6 phrases) avec la structure de la leçon.", lines(5), ["ecris"], 2, "C", sol="Présentation structurée : nom, lieu/date, origine, activités, avis.")
    b.page(f'{e}{e2}{e3}', "S'entraîner")

    # ---------- FLSco : lire une carte ----------
    l5 = lecon("Lire une carte et sa légende (méthode)", '''<p>1️⃣ Je lis le <b>titre</b> : de quoi parle la carte ? &nbsp; 2️⃣ Je cherche l'<b>orientation</b> (la flèche du nord : le nord est souvent en haut). &nbsp; 3️⃣ Je lis la <b>légende</b> : chaque couleur, chaque symbole a un sens. &nbsp; 4️⃣ J'utilise l'<b>échelle</b> pour calculer une distance. &nbsp; 5️⃣ Je réponds en citant ce que je <b>vois</b> sur la carte.</p>
<p class='sm'><b>L'échelle :</b> sur cette carte, la barre noire et blanche = 50 km. Je mesure la distance entre deux villes avec une règle ou une bande de papier, puis je compare avec la barre. <b>Vocabulaire de la consigne :</b> situer, localiser, repérer, mesurer, calculer, comparer, identifier.</p>''')
    e = E("Je lis la carte « La Belgique : régions, villes et fleuves » et sa légende. Je réponds.", "<p class='c sm'><b>La Belgique : régions, villes et fleuves</b></p>" + carte() + f"<p>1. Quel symbole indique la capitale du pays ? {blank()} Et la capitale de la Wallonie ? {blank()}</p><p>2. Quelle couleur représente la Région wallonne ? {blank()}</p><p>3. Quel fleuve passe à Namur et à Liège ? {blank()} Et à Gand et à Anvers ? {blank()}</p><p>4. Où se trouvent les communes germanophones ? {blank('l')}</p>", ["lis", "ecris"], 2, "B",
          sol="1. un carré rouge · un cercle blanc bordé de rouge — 2. orange clair — 3. la Meuse · l'Escaut — 4. à l'est de la Wallonie, près de l'Allemagne (Eupen)")
    b.page(f'<span class="tag-doc">🎒 FRANÇAIS DE L\'ÉCOLE</span>{l5}{e}', "Consignes & école")
    e = E("J'utilise l'échelle. Je mesure sur la carte et je calcule la distance à vol d'oiseau.", table(["Trajet", "Sur la carte (cm)", "Distance réelle (km)"], [["Namur → Liège", "", ""], ["Namur → Bruxelles", "", ""], ["Mons → Arlon", "", ""]], ["70mm", "56mm", "56mm"]).replace("<td></td>", '<td style="height:9mm"></td>') + "<p class='xs muted'>Aide : je mesure la barre de l'échelle (50 km) et je fais une règle de trois.</p>", ["ecris"], 2, "C",
          sol="Valeurs approchées : Namur–Liège ≈ 55 km · Namur–Bruxelles ≈ 55-60 km · Mons–Arlon ≈ 150 km (accepter ± 10 km selon la mesure)")
    e2 = E("Les mots de la consigne en géographie. Je relie.", relie(["localiser", "mesurer", "identifier", "comparer"], ["trouver ce qui est pareil et différent", "dire où se trouve quelque chose", "dire ce que c'est, donner le nom", "trouver une longueur avec une règle"]), ["relie"], 1, "B",
           sol="localiser → dire où · mesurer → longueur · identifier → donner le nom · comparer → pareil / différent")
    e3 = E("La carte muette : j'écris le nom de chaque ville numérotée.", carte("78%", legend=False, quiz=True) + "<p class='sm'>" + " · ".join(f"{i + 1}. ________" for i in range(len(VILLES))) + "</p>", ["regarde", "ecris"], 3, "C",
           sol=" · ".join(f"{i + 1}. {v[0]}" for i, v in enumerate(VILLES)))
    b.page(f'{e}{e2}{e3}', "Consignes & école")

    # ---------- Documents de la vie ----------
    dep = f'''<div class='doc' style='transform:none;display:grid;grid-template-columns:1fr 1fr 1fr;border:1.5px solid #9aa1b1;font-size:9.4pt;line-height:1.4'>
<div style='background:{MC};color:#fff;padding:4mm'><div style='font-size:9pt;letter-spacing:2px'>OFFICE DU TOURISME</div><div style='font-size:20pt;font-weight:800;line-height:1.05;margin:2mm 0'>Namur,<br>au cœur de la Wallonie</div><div style='font-size:28pt'>🏰🚡⛵</div><p>Entre Sambre et Meuse, la capitale de la Wallonie vous accueille toute l'année !</p></div>
<div style='padding:3mm 4mm'><b style='color:{MC}'>À voir</b><p>🏰 <b>La citadelle</b> : une des plus grandes forteresses d'Europe, sur une colline au-dessus de la ville. Souterrains et vue magnifique.</p><p>🚡 <b>Le téléphérique</b> : il monte du centre-ville jusqu'à la citadelle en quelques minutes.</p><p>⛵ <b>La Meuse en bateau</b> : croisières vers Dinant au printemps et en été.</p></div>
<div style='padding:3mm 4mm;background:#FDF0E6'><b style='color:{MC}'>Infos pratiques</b><p>🚆 En train : environ 1 heure depuis Bruxelles.<br>🚲 Location de vélos près de la gare.<br>🎉 Fêtes de Wallonie : 3ᵉ week-end de septembre.</p><p><b>Balade contée « Les secrets de la citadelle »</b><br>le samedi à 14 h · durée 1 h 30<br>adultes 8 € · enfants (6-12 ans) 4 € · moins de 6 ans gratuit</p><p class='xs muted'>Dépliant fictif à usage pédagogique ; horaires et tarifs inventés.</p></div></div>'''
    e = E("Je lis le dépliant touristique. Je réponds.", f"<p>1. Où se trouve Namur ? Entre quelles rivières ? {blank('xl')}</p><p>2. Cite 3 choses à faire à Namur. {blank('xl')}</p><p>3. Comment monter à la citadelle sans marcher ? {blank('l')}</p><p>4. Une famille (2 adultes + 2 enfants de 8 et 11 ans) fait la balade contée : combien paie-t-elle ? {blank()}</p><p>5. Trouve dans le dépliant un superlatif. {blank('l')}</p>", ["lis", "ecris"], 2, "B",
          sol="1. au cœur de la Wallonie, entre la Sambre et la Meuse — 2. visiter la citadelle, prendre le téléphérique, faire une croisière sur la Meuse, une balade contée, louer un vélo — 3. en téléphérique — 4. 2 × 8 + 2 × 4 = 24 € — 5. « une des plus grandes forteresses d'Europe »")
    b.page(f'<span class="tag-doc">📄 DOCUMENT DE LA VIE</span><h2>Un dépliant touristique</h2>{dep}<div class="mt4">{e}</div>', "Document de la vie")
    prog = table(["Heure", "21 juillet · Fête nationale · Bruxelles (programme type)"], [["10 h", "Te Deum (cérémonie religieuse) en présence de la famille royale"], ["16 h", "Défilé militaire et civil (pompiers, police, secours) dans le centre"], ["toute la journée", "Fête au parc de Bruxelles : stands, animations, concerts gratuits"], ["23 h", "Feu d'artifice"]], ["34mm", "148mm"])
    e = E("Je lis le programme de la fête nationale. Vrai ou faux ?", prog + "<p class='xs muted'>Programme simplifié : les heures exactes changent chaque année.</p>" + vf(["Le défilé a lieu le matin.", "Les concerts au parc sont gratuits.", "Le feu d'artifice commence à 23 h.", "Il y a seulement des militaires dans le défilé."]), ["lis", "coche"], 1, "B",
          sol="Faux (16 h) · Vrai · Vrai · Faux (aussi pompiers, police, secours)")
    e2 = E("J'écris un message à un(e) ami(e) pour l'inviter à une fête en Belgique (Saint-Nicolas, Doudou, 21 juillet…) : quoi, où, quand, ce qu'on va faire (5 lignes).", lines(5), ["ecris"], 2, "C", sol="Invitation : salutation, fête, lieu, date, programme, proposition de rendez-vous.")
    e3 = E("Je compare la fête nationale belge et la fête nationale de mon pays (date, activités) : 2 phrases.", lines(2), ["ecris"], 2, "C", sol="Ex. : En Syrie, la fête nationale est le 17 avril ; il y a aussi un défilé, mais pas de feu d'artifice.")
    b.page(f'<span class="tag-doc">📄 DOCUMENT DE LA VIE</span><h2>Un programme de fête</h2>{e}{e2}{e3}', "Document de la vie")

    # ---------- Sons : nasales ----------
    e = E("Les trois voyelles nasales. J'écoute et je répète (l'air passe par le nez 👃).", "<div class='grid3'>" + "".join(f"<div class='card c'><div class='huge'>{s}</div><p class='sm'>{w}</p></div>" for s, w in [("[ɑ̃] an, en", "G<b>an</b>d · Fl<b>an</b>dre · <b>An</b>vers · Ardennes ✗ · la Fr<b>an</b>ce · le c<b>en</b>tre"), ("[ɔ̃] on, om", "M<b>on</b>s · la régi<b>on</b> · la Wall<b>on</b>ie ✗ · le p<b>on</b>t · le n<b>om</b>"), ("[ɛ̃] in, ain, ein", "B<b>in</b>che · Din<b>an</b>t ✗ · le tr<b>ain</b> · pl<b>ein</b> · le v<b>in</b> · Saint-Nicolas")]) + "</div><div class='astuce'>✗ Attention : <b>Ardennes</b>, <b>Wallonie</b> : la voyelle n'est pas nasale quand elle est suivie de <b>nn</b> ou d'une voyelle (Wa-llo-nie). Dinant = [di-nɑ̃].</div>", ["ecoute", "repete"], 1, "A",
          script="Faire tenir le nez : avec une nasale, le son change. Paires : Gand / gant / gond / gain · ment / mont / main · Mons / mains / ment.", sol="Activité orale.")
    e2 = E("J'écoute : [ɑ̃], [ɔ̃] ou [ɛ̃] ? Je coche.", checks(8, ["[ɑ̃] an", "[ɔ̃] on", "[ɛ̃] in"]), ["ecoute", "coche"], 2, "A", script="1. Mons — 2. Gand — 3. Binche — 4. le pont — 5. le centre — 6. le train — 7. la région — 8. la France",
           sol="1. [ɔ̃] — 2. [ɑ̃] — 3. [ɛ̃] — 4. [ɔ̃] — 5. [ɑ̃] — 6. [ɛ̃] — 7. [ɔ̃] — 8. [ɑ̃]")
    e3 = E("Je lis vite et bien.", "<div class='card big c' style='line-height:1.8'>De Mons à Gand, en train, on chante :<br>« Binche, Dinant, Anvers… quelles belles régions ! »</div>", ["lis", "parle"], 2, "B", sol="Lecture expressive.")
    b.page(f'<h2>J\'écoute bien · les voyelles nasales</h2>{e}{e2}{e3}', "Sons")
    e = E("Les noms de lieux. J'écoute et je répète. Je souligne les lettres qu'on ne prononce pas.", "<div class='card big' style='line-height:2'>Bruxelles [bʁysɛl] · Liège · Namur · Charleroi · Anvers · Bruges · Arlon · Louvain-la-Neuve · Ostende · Spa · Tournai · Waterloo</div>", ["ecoute", "repete", "souligne"], 2, "A",
          script="Insister : Bruxelles se dit [bʁysɛl] (« ss »), Anvers sans s final prononcé, Liège avec [ɛ], Waterloo avec [w]. Lettres muettes : Bruxelle(s), Anver(s), Charleroi (le -oi = [wa]).", sol="Lettres muettes : le s de Bruxelles et d'Anvers, le e final de Liège, Bruges, Ostende…")
    e2 = E("Septante, nonante : j'écoute les années et les nombres. J'écris en chiffres.", f"<p>1. {blank()} 2. {blank()} 3. {blank()} 4. {blank()} 5. {blank()} 6. {blank()}</p>", ["ecoute", "ecris"], 2, "A",
           script="1. mille huit cent trente (1830) — 2. mille neuf cent cinquante-huit (1958, l'Atomium) — 3. septante-cinq — 4. nonante-quatre — 5. deux mille vingt-cinq — 6. six cent nonante-quatre (694 m, Botrange)",
           sol="1. 1830 — 2. 1958 — 3. 75 — 4. 94 — 5. 2025 — 6. 694")
    e3 = E("À deux : je dis une date importante de ma vie ou de mon pays (avec septante / nonante si possible). Mon voisin l'écrit en chiffres.", lines(1), ["parle", "duo"], 1, "A", sol="Dates dites et écrites correctement.")
    e4 = E("Je lis à voix haute en disant bien les nombres.", "<div class='card big' style='line-height:1.9'>La Belgique est indépendante depuis 1830. Le 1er janvier 2025, elle avait presque 11,8 millions d'habitants. Botrange mesure 694 mètres. L'Atomium a été construit en 1958. Namur est à 60 kilomètres de Bruxelles.</div>", ["lis", "parle"], 2, "B",
           sol="mille huit cent trente · onze virgule huit millions · six cent nonante-quatre · mille neuf cent cinquante-huit · soixante")
    b.page(f'<h2>J\'écoute bien · lieux et nombres</h2>{e}{e2}{e3}{e4}', "Sons")

    # ---------- Révision spirale ----------
    e = E("🔁 Module 5 · Depuis, il y a, pendant.", "<p>J'habite en Belgique ______ deux ans. Je suis allé(e) à Bruxelles ______ un mois. Nous avons visité la citadelle ______ deux heures.</p>", ["complete"], 2, "C", sol="depuis · il y a · pendant")
    e2 = E("🔁 Module 5 · Devoir + infinitif. Pour l'excursion, qu'est-ce qu'on doit apporter ? (3 phrases)", lines(2), ["ecris"], 1, "C", sol="Ex. : On doit apporter un pique-nique. Vous devez prendre un imperméable. Je dois avoir ma carte d'identité.")
    e3 = E("🔁 Module 4 · Les pronoms COD / COI.", "<p>Tu connais Bruxelles ? — Oui, je ______ connais. Tu as écrit à tes cousins ? — Oui, je ______ ai écrit une carte postale.</p>", ["complete"], 2, "C", sol="la · leur")
    e4 = E("🔁 Module 3 · Imparfait ou passé composé ?", "<p>Quand j'(arriver) ______________ en Belgique, il (faire) ______________ très froid et il (pleuvoir) ______________ .</p>", ["complete"], 2, "C", sol="suis arrivé(e) · faisait · pleuvait")
    e5 = E("🔁 Module 2 · Les prépositions de lieu. Je décris où se trouve la citadelle de Namur (2 prépositions).", lines(1), ["ecris"], 1, "C", sol="Ex. : La citadelle est au-dessus de la ville, sur une colline, entre la Sambre et la Meuse.")
    e6 = E("🔁 Module 1 · Je me présente à un guide touristique : nom, pays, langues, depuis quand je suis en Belgique (3 phrases).", lines(2), ["ecris"], 1, "C", sol="Ex. : Je m'appelle Fatou. Je viens de Guinée. Je parle peul et français. Je suis en Belgique depuis un an.")
    b.page(f'<h2>🔁 Je révise les modules 1 à 5</h2>{e}{e2}{e3}{e4}{e5}{e6}', "Je révise")

    # ---------- Ateliers ----------
    e = E("Le guide touristique : en duo, je choisis un lieu de la carte. Je prépare 4 phrases (où, quoi voir, quoi faire, mon avis avec un superlatif) et je fais la visite guidée pour la classe, comme dans un bus.", table(["Lieu choisi", "Où ?", "À voir / à faire", "Mon avis"], [["", "", "", ""]], ["36mm", "40mm", "62mm", "44mm"]).replace("<td></td>", '<td style="height:30mm"></td>'), ["parle", "duo"], 2, "A",
          sol="Présentation orale : situer, décrire, superlatif.")
    e2 = E("Le débat express : « La ville ou la campagne ? », « La mer ou les Ardennes ? ». Je donne mon avis avec 2 comparaisons. Les autres réagissent : « Je suis d'accord / pas d'accord parce que… »", "", ["parle", "groupe"], 2, "A", sol="Comparatifs, avis argumenté.")
    e3 = E("Le jeu « Quelle ville suis-je ? » : je choisis une ville de la carte. Les autres posent des questions fermées : « Tu es au nord de Namur ? Tu es plus grande que Mons ? Tu as un carnaval ? » Je réponds oui / non. 5 questions maximum !", "<div class='card sm c'>au nord / au sud de… ? · plus grande / plus petite que… ? · au bord de la Meuse / de l'Escaut ? · en Flandre / en Wallonie ? · une fête célèbre ?</div>", ["parle", "groupe", "joue"], 1, "A", sol="Questions avec comparatifs et prépositions de lieu.")
    b.page(f'{atl_head("A", "Atelier · Guides et débats")}{e}{e2}{e3}', "Atelier")
    bin_ = '''<div class='card' style='line-height:1.6;background:#FFFBF5'><h3 style='margin-top:0'>Les Gilles de Binche</h3><p>Chaque année, pendant les trois jours gras qui précèdent le mercredi des Cendres, la petite ville de Binche, dans le Hainaut, vit au rythme du carnaval. Le personnage le plus célèbre est le <b>Gille</b>. Le Mardi gras, dès l'aube, les Gilles se préparent chez eux. Ils portent un costume décoré de lions et d'étoiles, des sabots et une ceinture de grelots appelée l'<b>apertintaille</b>. Le matin, ils portent un masque de cire avec des lunettes vertes. L'après-midi, ils mettent un immense chapeau de plumes d'autruche.</p>
<p>Au son des tambours, les Gilles dansent dans les rues en tapant des sabots. Ils lancent des oranges au public : c'est un cadeau, il ne faut pas les renvoyer ! Depuis 2003, le carnaval de Binche est reconnu par l'UNESCO comme un chef-d'œuvre du patrimoine oral et immatériel de l'humanité.</p></div>'''
    e = E("Je lis le texte. Je réponds.", bin_ + f"<p class='mt2'>1. Quand a lieu le carnaval de Binche ? {blank('xl')}</p><p>2. Comment s'appelle la ceinture de grelots ? {blank()}</p><p>3. Que porte le Gille le matin ? Et l'après-midi ? {blank('xl')}</p><p>4. Que faut-il faire si on reçoit une orange ? {blank('l')}</p><p>5. Pourquoi l'UNESCO est-elle citée ? {blank('xl')}</p>", ["lis", "ecris"], 2, "B",
          sol="1. pendant les trois jours gras avant le mercredi des Cendres (le grand jour : le Mardi gras) — 2. l'apertintaille — 3. le matin : un masque de cire avec des lunettes vertes ; l'après-midi : un chapeau de plumes d'autruche — 4. la garder, ne pas la renvoyer (c'est un cadeau) — 5. Depuis 2003, elle reconnaît le carnaval comme chef-d'œuvre du patrimoine de l'humanité.")
    e2 = E("Vrai ou faux ? Je coche.", vf(["Le carnaval de Binche dure une semaine.", "Les Gilles portent des sabots.", "Il faut renvoyer les oranges aux Gilles.", "Le chapeau de plumes est porté l'après-midi."]), ["lis", "coche"], 1, "B", sol="Faux (trois jours gras) · Vrai · Faux · Vrai")
    b.page(f'{atl_head("B", "Atelier · Lire une tradition")}{e}{e2}', "Atelier")
    e = E("J'écris une carte postale à ma famille ou à un(e) ami(e) depuis une ville belge (8 lignes) : où je suis, ce que j'ai vu (passé composé), une comparaison avec mon pays, un superlatif.", "<div class='grid2' style='grid-template-columns:1.4fr 1fr'><div class='card' style='min-height:62mm'>" + lines(6) + "</div><div class='card' style='min-height:62mm'><div class='r' style='font-size:20pt'>📮</div>" + lines(3) + "<p class='xs muted'>adresse</p></div></div>", ["ecris"], 2, "C",
          sol="Carte : lieu, passé composé, comparatif, superlatif, formule de fin.")
    e2 = E("Je dessine et je légende le blason ou le symbole de ma ville (ou de ma commune en Belgique) : couleurs, animaux, objets. J'écris 2 phrases d'explication.", "<div class='card' style='height:38mm'></div>" + lines(2), ["dessine", "ecris"], 1, "C", sol="Dessin légendé et explication.")
    b.page(f'{atl_head("C", "Atelier · Cartes postales")}{e}{e2}', "Atelier")
    qs = [("Quelle est la capitale de la Belgique ?", "Bruxelles"), ("Combien de langues officielles ?", "trois"), ("Quel fleuve passe à Liège ?", "la Meuse"), ("Quelle ville a le carnaval des Gilles ?", "Binche"), ("Quelle est la date de la fête nationale ?", "le 21 juillet"),
          ("Où se trouve la citadelle sur une colline ?", "à Namur"), ("Qui reçoit des cadeaux le 6 décembre ?", "les enfants (Saint-Nicolas)"), ("Comment dit-on 90 en Belgique ?", "nonante"), ("Quel est le point le plus haut du pays ?", "Botrange"), ("Comment s'appelle le chef de la commune ?", "le bourgmestre"),
          ("Quelle est la plus grande ville du pays ?", "Anvers"), ("Comment s'appelle la capitale de la Wallonie ?", "Namur"),
          ("Quelle fête a lieu à Mons ?", "le Doudou"), ("Quelle est la date de la Saint-Nicolas ?", "le 6 décembre"), ("Comment s'appelle une chambre d'étudiant ?", "un kot"), ("Quel fleuve passe à Anvers ?", "l'Escaut")]
    cards = "".join(f"<div class='card' style='border-style:dashed;min-height:22mm;padding:2mm'><b class='xs' style='color:{MC}'>❓ {i + 1}</b><p class='sm' style='margin:0'>{q}</p></div>" for i, (q, _) in enumerate(qs))
    e = E("Le quiz belge : je découpe les cartes. En équipe, on tire une carte et on répond. Une bonne réponse = 1 point. Bonus : faire une phrase avec un comparatif ou un superlatif = 1 point de plus.", f"<div class='grid4'>{cards}</div>", ["decoupe", "joue", "groupe"], 1, "D",
          sol=" · ".join(f"{i + 1}. {a}" for i, (_, a) in enumerate(qs)))
    e2 = E("La feuille de score de mon équipe.", table(["Équipe", "Bonnes réponses", "Bonus (phrase)", "Total"], [["", "", "", ""] for _ in range(4)], ["60mm", "44mm", "44mm", "34mm"]).replace("<td></td>", '<td style="height:9mm"></td>'), ["ecris", "joue"], 1, "D", sol="Calcul des points.")
    b.page(f'{atl_head("D", "Atelier · Le quiz belge")}{e}{e2}', "Atelier")

    # ---------- ★ Coup de pouce ----------
    e = E("Je lis et je recopie.", "<div class='card' style='background:#F2FBF7'><p class='big' style='line-height:2'>La Belgique a trois régions :<br>la Flandre, la Wallonie et Bruxelles.<br>La capitale, c'est Bruxelles. 🇧🇪</p></div>" + lines(2), ["lis", "recopie"], 1, "B", alpha=True, sol="Copie correcte.")
    e2 = E("Je relie la fête et la date.", relie(["🇧🇪 la fête nationale", "🎁 la Saint-Nicolas", "🎊 le Nouvel An"], ["le 1er janvier", "le 21 juillet", "le 6 décembre"]), ["relie"], 1, "B", alpha=True, sol="fête nationale → 21 juillet · Saint-Nicolas → 6 décembre · Nouvel An → 1er janvier")
    e3 = E("À, en ou au ?", "<div class='card big' style='line-height:2'>J'habite ___ Namur, ___ Belgique.<br>Mon cousin habite ___ Maroc.</div>", ["complete"], 1, "C", alpha=True, sol="à · en · au")
    e4 = E("J'entoure les 3 langues de la Belgique.", "<div class='card big c'>français · anglais · néerlandais · arabe · allemand · espagnol</div>", ["entoure"], 1, "B", alpha=True, sol="français · néerlandais · allemand")
    b.page(CP.format(t="La Belgique") + e + e2 + e3 + e4, "★ Coup de pouce")
    e = E("Je compare avec le modèle (+ plus… que · − moins… que).", "<div class='card' style='background:#F2FBF7'><p class='big' style='line-height:2.1'>🐘 / 🐭 L'éléphant est <b>plus</b> grand <b>que</b> la souris.<br>🚲 / 🚗 Le vélo est ______ rapide ______ la voiture.<br>🏙️ / 🏡 Bruxelles est ______ grande ______ mon village.</p></div>", ["complete"], 1, "C", alpha=True, sol="moins … que · plus … que")
    e2 = E("Le plus ! J'entoure.", "<div class='card big' style='line-height:2'>Anvers est (la plus / le plus) grande ville.<br>Botrange est (le plus / la plus) haut point.<br>C'est (le meilleur / le plus bon) gâteau !</div>", ["entoure"], 1, "B", alpha=True, sol="la plus · le plus · le meilleur")
    e3 = E("Je compare deux choses de ma vie avec le modèle.", "<div class='card' style='background:#F2FBF7'><p class='big' style='line-height:2.1'>Mon pays est ______ chaud ______ la Belgique.<br>Ma ville est ______ grande ______ Namur.</p></div>", ["ecris"], 1, "C", alpha=True, sol="Comparaisons personnelles.")
    b.page(CP.format(t="Comparer") + e + e2 + e3, "★ Coup de pouce")
    e = E("Je regarde la carte et je complète : nord, sud, est, ouest.", "<div class='card c' style='font-size:14pt;line-height:1.6'>⬆️ nord<br>⬅️ ouest &nbsp;🧭&nbsp; est ➡️<br>⬇️ sud</div><div class='card big' style='line-height:2'>La mer est au ______ de la Belgique.<br>Arlon est au ______ .<br>Liège est à l'______ de Namur.</div>", ["regarde", "complete"], 1, "C", alpha=True, sol="nord (nord-ouest) · sud · est")
    e2 = E("Je présente une fête avec le modèle.", "<div class='card' style='background:#F2FBF7'><p class='big' style='line-height:2.1'>La fête s'appelle ____________ .<br>Elle a lieu en / le ____________ .<br>On ____________ et on ____________ .<br>J'aime cette fête parce que ____________ .</p></div>", ["ecris"], 1, "C", alpha=True, sol="Présentation guidée.")
    e3 = E("Je relie la fête et le dessin.", relie(["le carnaval", "la Saint-Nicolas", "la fête nationale"], ["🎁", "🇧🇪", "🎭"]), ["relie"], 1, "B", alpha=True, sol="carnaval → 🎭 · Saint-Nicolas → 🎁 · fête nationale → 🇧🇪")
    b.page(CP.format(t="Situer · présenter une fête") + e + e2 + e3, "★ Coup de pouce")

    # ---------- Tâche finale ----------
    e = E("Je choisis une ville (en Belgique ou dans mon pays) et je fais mes recherches (livres, CDI, internet avec la prof). Je remplis la fiche.", table(["Rubrique", "Mes informations"], [["Nom, pays, région / province", ""], ["Situation (points cardinaux, fleuve, distance d'une grande ville)", ""], ["Nombre d'habitants (environ) et comparaison avec une autre ville", ""], ["2 monuments ou lieux à voir", ""], ["1 fête ou tradition", ""], ["1 spécialité (plat, objet)", ""], ["Mon avis (superlatif) + pourquoi", ""], ["Mes sources (où j'ai trouvé les informations)", ""]], ["70mm", "112mm"]).replace("<td></td>", '<td style="height:14mm"></td>'), ["ecris"], 1, "C",
          sol="Fiche complète, sources notées.")
    b.page(tache_head("Exposé illustré d'une ville", "Je présente une ville à la classe (3 minutes) avec une affiche illustrée : situation sur une carte, chiffres, monuments, une fête et mon avis.") + e, "Tâche finale", levels=False)
    e = E("Je fais le brouillon de mon affiche : le titre, une petite carte avec une légende, 3 dessins avec légendes, 2 chiffres.", "<div class='card' style='height:118mm;border:2px dashed #9aa1b1;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:auto 1fr 1fr;gap:3mm;padding:3mm'><div style='grid-column:1/3;border-bottom:1px solid #ddd' class='c muted'>TITRE</div><div class='card muted xs'>ma carte + légende + échelle</div><div class='card muted xs'>chiffres et comparaisons</div><div class='card muted xs'>monuments (dessins + légendes)</div><div class='card muted xs'>fête, spécialité, mon avis</div></div>", ["dessine", "ecris"], 2, "C",
          sol="Affiche organisée et légendée.")
    b.page(e + table(["Je vérifie :", "✅"], [[x, '<span class="chk"></span>'] for x in ["Mon affiche a un titre et une carte avec une légende.", "Je situe la ville (à, en, au ; nord, sud…).", "J'utilise au moins 2 comparatifs et 1 superlatif.", "Je présente une fête ou une tradition.", "Je parle 3 minutes en regardant la classe, sans lire.", "Je cite mes sources."]], ["160mm", "22mm"]), "Tâche finale", levels=False)
    e = E("Je prépare mes notes pour l'oral : des mots-clés seulement (pas de phrases complètes !).", "<div class='grid2'>" + "".join(f"<div class='card'><b class='sm'>{t}</b>" + lines(2) + "</div>" for t in ["1. Introduction (« Je vais vous présenter… »)", "2. Situation et chiffres", "3. À voir", "4. Fête / spécialité", "5. Mon avis", "6. Conclusion (« Merci ! Vous avez des questions ? »)"]) + "</div>", ["ecris"], 2, "C",
          sol="Notes en mots-clés.")
    e2 = E("J'écoute les exposés des autres. Pour chaque exposé, je note une information et je pose une question.", table(["Ville", "Une information", "Ma question"], [["", "", ""] for _ in range(4)], ["40mm", "72mm", "70mm"]).replace("<td></td>", '<td style="height:9mm"></td>'), ["ecoute", "ecris"], 2, "A", sol="Écoute active, questions pertinentes.")
    b.page(f'{e}{e2}', "Tâche finale", levels=False)
    e = E("Je révise.", "<p>1. La Belgique a ______ régions et ______ langues officielles. 2. J'habite ___ Belgique, ___ Mons. 3. Anvers est (+ grand) ______________ Namur. 4. C'est la gaufre (+ bon) ______________ ! 5. Liège est à l'______ de Namur. 6. Le chef de la commune : le ______________ . 7. 1830 = l'année de l'______________ .</p>", ["ecris"], 2, "C",
          sol="1. trois · trois — 2. en · à — 3. plus grande que — 4. la meilleure — 5. est — 6. bourgmestre — 7. indépendance")
    e2 = E("Défi ! Je corrige les 6 erreurs.", "<div class='card big'>J'habite en Namur, à Belgique. Namur est plus petit que Liège. La citadelle est le monument la plus célèbre de la ville. Les gaufres sont plus bonnes qu'au Maroc. J'aime mieux la mer que les Ardennes parce que c'est plus beau que.</div>" + lines(2), ["barre", "ecris"], 3, "C",
           sol="à Namur · en Belgique · plus petite · le monument le plus célèbre · meilleures · plus beau (sans « que » à la fin)")
    e3 = E("Je compare deux fêtes (une fête belge et une fête de mon pays) en 3 phrases.", lines(3), ["ecris"], 2, "C", sol="Comparatifs justes, vocabulaire des fêtes.")
    e4 = E("Je situe 3 villes avec les points cardinaux ou une distance (aide : la carte de la leçon 3).", lines(2), ["ecris"], 2, "C", sol="Ex. : Bruges est au nord-ouest. Arlon est au sud, près du Luxembourg. Liège est à l'est de Namur.")
    b.page(f'<h2>🔁 Je révise tout le module</h2>{e}{e2}{e3}{e4}', "Je révise")

    # ---------- Test ----------
    Q = [("La capitale de la Belgique :", ["Namur", "Bruxelles", "Anvers", "Liège"]), ("La capitale de la Wallonie :", ["Namur", "Charleroi", "Mons", "Bruxelles"]), ("Les langues officielles de Belgique :", ["français, anglais, allemand", "néerlandais, français, allemand", "français, néerlandais, anglais", "seulement le français"]),
         ("La fête nationale belge :", ["le 14 juillet", "le 21 juillet", "le 27 septembre", "le 6 décembre"]), ("Le chef d'une commune en Belgique :", ["le maire", "le bourgmestre", "le gouverneur", "le roi"]), ("Le fleuve de Namur et de Liège :", ["l'Escaut", "la Meuse", "la Seine", "le Rhin"]),
         ("Bruxelles est ____ grande ____ Namur.", ["plus … que", "plus … de", "le plus … que", "aussi … de"]), ("Les frites sont ____ que les chips !", ["plus bonnes", "meilleures", "mieux", "les meilleures"]), ("Tu parles ____ français qu'avant.", ["meilleur", "mieux", "plus bon", "plus bien"]),
         ("Arlon a ____ habitants que Liège.", ["moins d'", "moins", "moins des", "le moins"]), ("Anvers est ____ grande ville de Belgique.", ["la plus", "le plus", "plus", "très"]), ("C'est le monument ____ célèbre de Mons.", ["la plus", "le plus", "plus que", "aussi"]),
         ("J'habite ____ Belgique.", ["à", "au", "en", "aux"]), ("Mon oncle vit ____ Pays-Bas.", ["en", "au", "aux", "à"]), ("Liège est ____ de Namur.", ["au nord", "à l'est", "au sud", "à l'ouest"]),
         ("Sur une carte, la ____ explique les symboles.", ["légende", "échelle", "flèche", "frontière"]), ("L'échelle sert à…", ["trouver le nord", "calculer une distance", "lire les couleurs", "écrire le titre"]), ("« une drache » (belgicisme) =", ["une fête", "une forte pluie", "une rivière", "un repas"]),
         ("Dans « Mons », on entend…", ["[ɑ̃]", "[ɔ̃]", "[ɛ̃]", "[o]"]), ("🔁 J'habite en Belgique ____ deux ans.", ["il y a", "depuis", "pendant", "dans"])]
    ans = ["Bruxelles", "Namur", "néerlandais, français, allemand", "le 21 juillet", "le bourgmestre", "la Meuse", "plus … que", "meilleures", "mieux", "moins d'", "la plus", "le plus", "en", "aux", "à l'est", "légende", "calculer une distance", "une forte pluie", "[ɔ̃]", "depuis"]
    key = key_from(Q, ans)
    test_pages(b, 6, "Découvrir la Belgique", Q, f"<h3>B1. Compare ta ville d'origine et une ville belge : 3 phrases (plus… que, moins… que, aussi… que). (… / 3)</h3>{lines(2, True)}<h3>B2. Écris 3 superlatifs sur la Belgique ou sur ton pays. (… / 3)</h3>{lines(2, True)}<h3>B3. Présente une fête en 4 phrases (nom, lieu et date, ce qu'on fait, ton avis). (… / 4)</h3>{lines(2, True)}",
               [["situer 3 villes sur la carte (points cardinaux)", "/ 3", ""], ["présenter une fête ou une ville (1 minute)", "/ 4", ""], ["comparer deux lieux à l'oral", "/ 3", ""]],
               "<h3>1. Je complète : la Belgique. (… / 4)</h3><div class='card big'>La capitale : ____________ · La fête nationale : le ____ juillet<br>Trois régions : la Flandre, la ____________ et ____________</div><h3>2. À, en ou au ? (… / 4)</h3><div class='card big'>___ Bruxelles · ___ France · ___ Maroc · ___ Liège</div><h3>3. Plus ou moins ? Je regarde et je complète. (… / 4)</h3><div class='card big'>🐘 L'éléphant est ______ grand que 🐭 la souris.<br>🐌 L'escargot est ______ rapide que 🐆 le guépard.</div><h3>4. Nord, sud, est ou ouest ? (… / 4)</h3><div class='card big'>La mer est au ______ . Arlon est au ______ .</div><h3>5. Oral : je dis une fête que j'aime. (… / 4)</h3>")
    closing(b, 6, ["Je sais dire comment la Belgique est organisée (régions, communautés, communes).", "Je sais situer les grandes villes et les fleuves.", "Je sais dire à, en, au, aux devant un lieu.", "Je sais utiliser les points cardinaux et les distances.", "Je sais comparer (plus… que, moins… que, aussi… que).", "Je sais utiliser meilleur et mieux.",
                   "Je sais utiliser le superlatif (le plus, le moins, le meilleur).", "Je sais présenter une fête, une tradition.", "Je sais lire une carte, sa légende et son échelle.", "Je sais lire un dépliant touristique.", "Je sais faire un exposé illustré."],
            [("🗺️", "la région"), ("🧩", "la province"), ("🏘️", "la commune"), ("🎩", "le / la bourgmestre"), ("👑", "le roi"), ("🏙️", "la capitale"), ("🗣️", "la langue officielle"), ("🌊", "la côte"), ("🌲", "la forêt"), ("💧", "le fleuve"), ("🏰", "la citadelle"), ("🧱", "le beffroi"),
             ("🎭", "le carnaval"), ("🎁", "la Saint-Nicolas"), ("🇧🇪", "la fête nationale"), ("🎆", "le feu d'artifice"), ("🧭", "le nord, le sud…"), ("📏", "l'échelle"), ("🔑", "la légende"), ("➕", "plus… que"), ("🏆", "le plus…"), ("🌧️", "une drache")])
    plan_de_travail(b, E, 6, ["Le comparatif", "Le superlatif", "Situer un lieu", "Présenter une fête", "Lire une carte et sa légende"], "☐ Ma fiche de recherche<br>☐ Mon affiche<br>☐ Mon exposé (3 min)")
    if render:
        to_pdf(b.html(), '/home/claude/syllabus/out/V2_M6_eleve.pdf')

    pg, exs = helpers(b, E)
    CPp = b.marks["★ Coup de pouce"]
    days = [("1", "Collectif", f"Ouverture · BD · la Belgique en bref ({pg('Découvrir')})", f"CP la Belgique (p. {CPp[0]})"), ("2", "Collectif", f"Lexique pays, paysage, fêtes, belgicismes ({pg('Lexique')})", "CP fêtes et dates"),
            ("3", "Rotation", f"📌 Leçon 1 comparatif ({pg('Leçon 1')})", f"CP comparer (p. {CPp[1]})"), ("4", "Rotation", f"📌 Leçon 2 superlatif ({pg('Leçon 2')})", "CP le plus"),
            ("5", "Collectif", f"📌 Leçon 3 situer ({pg('Leçon 3')}) · sons ({pg('Sons')})", f"CP points cardinaux (p. {CPp[2]})"), ("6", "Rotation", f"📌 Leçon 4 présenter une fête ({pg('Leçon 4')})", "CP fête guidée"),
            ("7", "Collectif", f"📌 Carte et légende ({pg('Consignes & école')})", "CP carte simplifiée"), ("8", "Rotation", f"Documents ({pg('Document de la vie')}) · ateliers ({pg('Atelier')})", "CP dépliant (questions 1-3)"),
            ("9", "Seul", f"Tâche finale : recherches et affiche ({pg('Tâche finale')})", "CP affiche guidée"), ("10", "Seul", f"Exposés · test ({pg('Test')})", f"CP test ({pg('★ Coup de pouce · Test')})")]
    rot = [["🎧 Écouter-Parler", "Guide touristique · débat", "20 min", "—"], ["📖 Lire", "Gilles de Binche · dépliant", "20 min", "Oui"], ["✏️ Écrire", "Carte postale · blason", "20 min", "● oui"],
           ["🧩 Jouer", "Quiz belge", "20 min", "Réponses p. corrigés"], ["👩‍🏫 Table d'appui", "Coup de pouce · comparer", "20 min", "—"]]
    ev1 = '''<h3>Partie B (10 points)</h3><p class="sm"><b>B1</b> : 1 pt par comparaison correcte (structure + accord). · <b>B2</b> : 1 pt par superlatif correct (article, accord, « de »). · <b>B3</b> : nom (1), lieu et date (1), activités avec « on » (1), avis (1).</p>
<h3>Partie C · oral (10 points)</h3><p class="sm">Avec la carte du cahier : « Où est Liège ? Arlon ? Bruges ? » (3) · présentation d'une fête ou d'une ville en 1 minute (4) · comparer deux lieux choisis par la prof, par ex. Bruxelles et Namur (3).</p>
<h3>Test ★ Coup de pouce (20 points)</h3><p class="sm"><b>1 :</b> <span class="sol">Bruxelles · 21 · Wallonie · Bruxelles</span> · <b>2 :</b> <span class="sol">à · en · au · à</span> · <b>3 :</b> <span class="sol">plus · moins</span> (2 pts chacun) · <b>4 :</b> <span class="sol">nord · sud</span> (2 pts chacun) · <b>5 :</b> phrase sur une fête (4).</p>'''
    ev2 = f'''<h2>Grille · tâche finale « Exposé illustré d'une ville »</h2>{table(["Critère", "Très bien", "Bien", "À retravailler", "Points"], [["<b>Contenu</b> : situation, chiffres, monuments, fête, avis", "Complet", "Partiel", "Pauvre", "/ 4"], ["<b>Affiche</b> : titre, carte légendée, illustrations", "Claire", "Incomplète", "Confuse", "/ 3"], ["<b>Langue</b> : comparatifs et superlatif", "≥ 3 justes", "1-2", "Aucun", "/ 4"], ["<b>Situer</b> : prépositions, points cardinaux", "Justes", "Quelques erreurs", "Beaucoup", "/ 3"], ["<b>Oral</b> : 3 min, sans lire, regard, voix", "Fluide", "Hésitant", "Lu", "/ 4"], ["<b>Sources</b> citées", "Oui", "Partielles", "Non", "/ 2"]], ["66mm", "30mm", "30mm", "34mm", "22mm"])}
<h2 class="mt4">Différencier et remédier</h2>{table(["Difficulté", "Remédiation"], [["Accord dans la comparaison", "Repérer le nom comparé et son genre : « Bruxelles (une ville) est plus grand<b>e</b> »."], ["bon / bien", "Bon = adjectif (avec un nom) → meilleur ; bien = adverbe (avec un verbe) → mieux. Tri d'étiquettes."], ["à / en / au / aux", "Carte du monde avec des pays coloriés : rose = féminin (en), bleu = masculin (au), vert = pluriel (aux)."], ["Lire une carte", "Partir de la carte de l'école (plan) puis de la commune, avant la carte du pays ; utiliser une bande de papier pour l'échelle."], ["Élève rapide", "Comparer deux climatogrammes ou deux villes avec un tableau de données ; préparer un quiz pour la classe."]], ["44mm", "138mm"])}'''
    rep = f'''<h2>La Belgique : repères pour l'enseignant</h2>
<h3>Faits utilisés dans le cahier (vérifiés en novembre 2026)</h3>{table(["Repère", "Information"], [["Population", "11 825 551 habitants au 1er janvier 2025 (Statbel) : « presque 11,8 millions »."], ["Chef de l'État", "Le roi Philippe, depuis le 21 juillet 2013."], ["Institutions", "État fédéral : 3 Régions (flamande, wallonne, Bruxelles-Capitale), 3 Communautés (flamande, française = Fédération Wallonie-Bruxelles, germanophone), 10 provinces, plus de 500 communes (565 depuis les fusions de 2025)."], ["Indépendance", "1830 ; fête nationale le 21 juillet (prestation de serment de Léopold Iᵉʳ en 1831)."], ["Fêtes", "27 septembre : fête de la Fédération Wallonie-Bruxelles (congé scolaire) · Fêtes de Wallonie à Namur le 3ᵉ week-end de septembre · Doudou à Mons le dimanche de la Trinité · Saint-Nicolas le 6 décembre."], ["Binche", "Carnaval proclamé chef-d'œuvre du patrimoine oral et immatériel de l'humanité par l'UNESCO en 2003."], ["Géographie", "Botrange, 694 m, point culminant · côte d'environ 67 km · Meuse (Namur, Liège), Escaut (Tournai, Gand, Anvers), Sambre (Charleroi, Namur)."], ["Villes", "Chiffres arrondis : Anvers ≈ 540 000 ; Charleroi ≈ 205 000 (plus grande ville de Wallonie) ; Liège ≈ 197 000 ; Namur ≈ 114 000 ; Mons ≈ 96 000 ; Arlon ≈ 31 000. À actualiser avec Statbel si nécessaire."]], ["34mm", "148mm"])}
<div class="attention mt2"><b>Neutralité :</b> présenter les institutions et la diversité linguistique de façon factuelle, sans débat communautaire. Valoriser autant les fêtes des pays d'origine que les fêtes belges ; certains élèves ne fêtent pas certaines fêtes (Saint-Nicolas, carnaval) : ne jamais imposer.</div>
<p class="sm"><b>La carte du cahier</b> est un schéma simplifié dessiné pour la classe (contours approximatifs, frontière linguistique simplifiée, enclaves non représentées). Pour les mesures d'échelle, accepter une marge d'erreur.</p>'''
    T = teacher_book(b, E, "V2 · M6", "", MC, 6, "Découvrir la Belgique",
                     "<li><b>Communication :</b> présenter un lieu, une région, une fête ; comparer ; donner son avis.</li><li><b>Lexique :</b> institutions simples, paysage, fêtes et traditions, spécialités ; belgicismes (bourgmestre, échevin, drache, kot).</li><li><b>Grammaire :</b> comparatif (adjectif, nom, verbe), meilleur / mieux, superlatif ; prépositions devant les noms de lieux.</li><li><b>Phonétique :</b> voyelles nasales [ɑ̃] [ɔ̃] [ɛ̃] ; noms de lieux ; septante / nonante.</li><li><b>FLSco :</b> lire une carte, sa légende, son échelle ; verbes de consigne en géographie.</li><li><b>Documents :</b> carte de Belgique, dépliant touristique, programme de fête.</li><li><b>★ Coup de pouce :</b> la Belgique en 3 phrases, comparer avec modèle, points cardinaux, fête guidée.</li>",
                     '<p class="sm"><b style="color:#E4572E">Indispensable</b> : capitale, 3 régions, 3 langues, plus / moins… que, à / en / au.</p><p class="sm"><b style="color:#d9a400">Important</b> : superlatif, meilleur / mieux, points cardinaux, présenter une fête.</p><p class="sm"><b style="color:#2BA88F">Enrichissement</b> : échelle, institutions, recherche documentaire.</p>',
                     "Grande carte murale de Belgique · atlas · règles ou bandes de papier (échelle) · dépliants touristiques réels de la région · ciseaux (quiz) · grandes feuilles pour les affiches.", "<b>Sortie possible :</b> visite de la commune (rencontre avec un échevin) ou d'une ville proche, préparée avec le dépliant et la carte. Lire la page « Repères » du livret avant de commencer.",
                     days, "Un lieu de Belgique du jour (où ? que voir ?) · une comparaison du jour (« Aujourd'hui, il fait plus froid qu'hier ») · un nombre en septante / nonante.", rot, key, (ev1, ev2), extra_pages=[(rep, "Repères")], start=tstart)
    if render:
        to_pdf(T.html(), '/home/claude/syllabus/out/V2_M6_prof.pdf')
    return b, T


if __name__ == "__main__":
    b, T = build_v2m6()
    print(b.n, T.n)
