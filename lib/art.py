"""Bibliothèque d'illustrations SVG originales : personnages récurrents, pictogrammes de consignes, objets."""

SKIN = {"clair": "#F6D7C3", "moyen": "#E0AC84", "mat": "#C68A5E", "fonce": "#8D5A3B", "tres_fonce": "#5E3A26"}

# ---------- PERSONNAGES RÉCURRENTS (les 3 volumes) ----------
CAST = {
    "amina": dict(skin="mat", hair="hijab", hair_col="#3E6FB0", shirt="#F29E4C", name="Amina", lashes=True),
    "yonas": dict(skin="tres_fonce", hair="court_boucle", hair_col="#1d1d1d", shirt="#2BA88F", name="Yonas"),
    "daria": dict(skin="clair", hair="tresses", hair_col="#E8C26A", shirt="#C94F7C", name="Daria", lashes=True),
    "mateo": dict(skin="moyen", hair="court_meche", hair_col="#3B2516", shirt="#4A7BD1", name="Mateo"),
    "bilal": dict(skin="moyen", hair="court", hair_col="#1d1d1d", shirt="#7A5BC7", name="Bilal", glasses=True),
    "fatou": dict(skin="fonce", hair="afro_puffs", hair_col="#1d1d1d", shirt="#F2C14E", name="Fatou", lashes=True),
    "nour": dict(skin="moyen", hair="carre", hair_col="#2B1A12", shirt="#E07A1F", name="Nour", lashes=True),
    "prof": dict(skin="clair", hair="carre", hair_col="#8B4A2B", shirt="#2E4057", name="Mme Lambert", glasses=True, lashes=True, adult=True),
    "educ": dict(skin="fonce", hair="chauve_barbe", hair_col="#2a2a2a", shirt="#6B8F3E", name="M. Diallo", adult=True),
}


def _darken(hex_col, f=0.8):
    h = hex_col.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return "#%02x%02x%02x" % (int(r * f), int(g * f), int(b * f))


def avatar(key, size=90, mood="sourire", bubble=None, flip=False, bg=None):
    """Buste d'un personnage. mood: sourire, rire, neutre, triste, surpris, pense, fache."""
    c = CAST[key]
    skin = SKIN[c["skin"]]
    hc = c["hair_col"]
    sh = c["shirt"]
    parts = []
    if bg:
        parts.append(f'<circle cx="50" cy="52" r="48" fill="{bg}"/>')
    # cheveux arrière
    if c["hair"] == "tresses":
        parts.append(f'<path d="M24 42 Q20 75 28 92 L36 92 Q30 70 32 45Z M76 42 Q80 75 72 92 L64 92 Q70 70 68 45Z" fill="{hc}"/>')
    if c["hair"] == "carre":
        parts.append(f'<path d="M22 40 Q20 70 28 72 L72 72 Q80 70 78 40 Q76 14 50 14 Q24 14 22 40Z" fill="{hc}"/>')
    if c["hair"] == "hijab":
        parts.append(f'<path d="M18 50 Q16 14 50 12 Q84 14 82 50 Q84 78 74 92 L26 92 Q16 78 18 50Z" fill="{hc}"/>')
    # corps
    parts.append(f'<path d="M14 100 Q16 76 50 74 Q84 76 86 100Z" fill="{sh}"/>')
    parts.append(f'<path d="M42 74 L50 84 L58 74Z" fill="{skin if c["hair"]!="hijab" else _darken(hc,0.85)}"/>')
    # cou
    if c["hair"] != "hijab":
        parts.append(f'<rect x="43" y="62" width="14" height="14" rx="4" fill="{_darken(skin,0.9)}"/>')
    # oreilles
    if c["hair"] not in ("hijab",):
        parts.append(f'<circle cx="27" cy="46" r="5" fill="{skin}"/><circle cx="73" cy="46" r="5" fill="{skin}"/>')
    # tête
    parts.append(f'<ellipse cx="50" cy="44" rx="23" ry="25" fill="{skin}"/>')
    # cheveux avant
    h = c["hair"]
    if h == "hijab":
        parts.append(f'<path d="M26 44 Q26 18 50 18 Q74 18 74 44 Q72 26 50 24 Q28 26 26 44Z" fill="{_darken(hc,0.9)}"/>')
    elif h == "court_boucle":
        for x, y in [(32, 26), (40, 21), (50, 19), (60, 21), (68, 26), (36, 31), (64, 31), (28, 34), (72, 34)]:
            parts.append(f'<circle cx="{x}" cy="{y}" r="7" fill="{hc}"/>')
    elif h == "tresses":
        parts.append(f'<path d="M26 44 Q24 18 50 17 Q76 18 74 44 Q70 30 58 28 Q50 34 40 28 Q30 30 26 44Z" fill="{hc}"/>')
        parts.append(f'<circle cx="31" cy="90" r="4" fill="#C94F7C"/><circle cx="69" cy="90" r="4" fill="#C94F7C"/>')
    elif h == "court_meche":
        parts.append(f'<path d="M26 42 Q24 16 52 17 Q78 18 74 40 Q66 28 54 30 Q46 22 38 30 Q30 32 26 42Z" fill="{hc}"/>')
    elif h == "court":
        parts.append(f'<path d="M27 40 Q27 17 50 17 Q73 17 73 40 Q70 27 50 27 Q30 27 27 40Z" fill="{hc}"/>')
    elif h == "afro_puffs":
        parts.append(f'<circle cx="26" cy="22" r="11" fill="{hc}"/><circle cx="74" cy="22" r="11" fill="{hc}"/>')
        parts.append(f'<path d="M27 40 Q27 18 50 18 Q73 18 73 40 Q68 27 50 27 Q32 27 27 40Z" fill="{hc}"/>')
    elif h == "carre":
        parts.append(f'<path d="M26 42 Q26 18 50 18 Q74 18 74 42 Q66 26 46 28 Q34 30 26 42Z" fill="{hc}"/>')
    elif h == "chauve_barbe":
        parts.append(f'<path d="M30 52 Q32 70 50 71 Q68 70 70 52 Q66 62 50 63 Q34 62 30 52Z" fill="{hc}"/>')
    # yeux
    ey = 45
    if mood == "rire":
        parts.append(f'<path d="M37 {ey} Q41 {ey-4} 45 {ey}" stroke="#222" stroke-width="2.2" fill="none" stroke-linecap="round"/>'
                     f'<path d="M55 {ey} Q59 {ey-4} 63 {ey}" stroke="#222" stroke-width="2.2" fill="none" stroke-linecap="round"/>')
    elif mood == "surpris":
        parts.append(f'<circle cx="41" cy="{ey}" r="3.6" fill="#222"/><circle cx="59" cy="{ey}" r="3.6" fill="#222"/>')
    else:
        parts.append(f'<ellipse cx="41" cy="{ey}" rx="2.6" ry="3.2" fill="#222"/><ellipse cx="59" cy="{ey}" rx="2.6" ry="3.2" fill="#222"/>'
                     f'<circle cx="42" cy="{ey-1}" r="0.9" fill="#fff"/><circle cx="60" cy="{ey-1}" r="0.9" fill="#fff"/>')
    if c.get("lashes") and mood not in ("rire",):
        parts.append(f'<path d="M38.4 {ey-2} l-2.6 -1.4 M61.6 {ey-2} l2.6 -1.4" stroke="#222" stroke-width="1.3" stroke-linecap="round"/>')
    # sourcils
    if mood == "triste":
        parts.append('<path d="M36 37 L45 39 M64 37 L55 39" stroke="#333" stroke-width="1.8" stroke-linecap="round"/>')
    elif mood == "pense":
        parts.append('<path d="M36 38 Q41 35 46 38 M54 36 Q59 33 64 36" stroke="#333" stroke-width="1.8" fill="none" stroke-linecap="round"/>')
    elif mood == "surpris":
        parts.append('<path d="M36 36 Q41 32 46 36 M54 36 Q59 32 64 36" stroke="#333" stroke-width="1.8" fill="none" stroke-linecap="round"/>')
    elif mood == "fache":
        parts.append('<path d="M35 36 L46 40 M65 36 L54 40" stroke="#333" stroke-width="2.4" stroke-linecap="round"/>')
    # lunettes
    if c.get("glasses"):
        parts.append('<circle cx="41" cy="45" r="7" fill="none" stroke="#333" stroke-width="1.6"/>'
                     '<circle cx="59" cy="45" r="7" fill="none" stroke="#333" stroke-width="1.6"/>'
                     '<path d="M48 45 L52 45" stroke="#333" stroke-width="1.6"/>')
    # joues
    parts.append(f'<circle cx="35" cy="54" r="4" fill="#E86A6A" opacity="0.25"/><circle cx="65" cy="54" r="4" fill="#E86A6A" opacity="0.25"/>')
    # bouche
    if mood == "sourire":
        parts.append('<path d="M42 55 Q50 62 58 55" stroke="#7A2E2E" stroke-width="2.2" fill="none" stroke-linecap="round"/>')
    elif mood == "rire":
        parts.append('<path d="M41 54 Q50 66 59 54Z" fill="#7A2E2E"/><path d="M44 55 L56 55 L55 57 L45 57Z" fill="#fff"/>')
    elif mood == "neutre" or mood == "pense":
        parts.append('<path d="M44 57 L56 57" stroke="#7A2E2E" stroke-width="2.2" stroke-linecap="round"/>')
    elif mood == "triste":
        parts.append('<path d="M42 60 Q50 53 58 60" stroke="#7A2E2E" stroke-width="2.2" fill="none" stroke-linecap="round"/>')
    elif mood == "surpris":
        parts.append('<ellipse cx="50" cy="58" rx="4" ry="5" fill="#7A2E2E"/>')
    elif mood == "fache":
        parts.append('<path d="M42 59 Q50 55 58 59" stroke="#7A2E2E" stroke-width="2.6" fill="none" stroke-linecap="round"/>')
    tr = ' transform="translate(100,0) scale(-1,1)"' if flip else ''
    svg = f'<svg viewBox="0 0 100 100" width="{size}" height="{size}" class="av"><g{tr}>{"".join(parts)}</g></svg>'
    if bubble:
        return f'<div class="avb"><div class="avb-img">{svg}</div><div class="bubble">{bubble}</div></div>'
    return svg


# ---------- PICTOGRAMMES DE CONSIGNES ----------
PICTO_LABEL = {
    "ecoute": "J'écoute", "parle": "Je parle", "lis": "Je lis", "ecris": "J'écris", "entoure": "J'entoure",
    "relie": "Je relie", "colorie": "Je colorie", "coche": "Je coche", "souligne": "Je souligne", "decoupe": "Je découpe",
    "colle": "Je colle", "regarde": "Je regarde", "repete": "Je répète", "seul": "Seul", "duo": "À deux",
    "groupe": "En groupe", "recopie": "Je recopie", "complete": "Je complète", "barre": "Je barre", "montre": "Je montre",
    "dessine": "Je dessine", "trace": "Je trace", "numerote": "Je numérote", "joue": "Je joue",
}


def picto(name, size=34):
    s = '<svg viewBox="0 0 40 40" width="%d" height="%d" class="picto">' % (size, size)
    bg = '<rect x="1" y="1" width="38" height="38" rx="9" fill="#fff" stroke="#1F2A44" stroke-width="2"/>'
    k = "#1F2A44"
    body = {
        "ecoute": f'<path d="M14 26 Q10 12 20 9 Q30 8 29 18 Q29 22 25 24 Q22 26 23 30 Q22 33 18 32" fill="none" stroke="{k}" stroke-width="2.6" stroke-linecap="round"/><path d="M19 18 Q20 14 24 16" fill="none" stroke="{k}" stroke-width="2.2" stroke-linecap="round"/>',
        "parle": f'<path d="M8 12 Q8 8 12 8 L28 8 Q32 8 32 12 L32 22 Q32 26 28 26 L18 26 L11 32 L13 26 L12 26 Q8 26 8 22Z" fill="#FFD166" stroke="{k}" stroke-width="2"/><circle cx="15" cy="17" r="1.8" fill="{k}"/><circle cx="20" cy="17" r="1.8" fill="{k}"/><circle cx="25" cy="17" r="1.8" fill="{k}"/>',
        "lis": f'<path d="M6 12 Q13 9 20 12 L20 31 Q13 28 6 31Z" fill="#9AD3F5" stroke="{k}" stroke-width="2"/><path d="M34 12 Q27 9 20 12 L20 31 Q27 28 34 31Z" fill="#CDEBFB" stroke="{k}" stroke-width="2"/>',
        "ecris": f'<path d="M10 30 L12 23 L27 8 L32 13 L17 28Z" fill="#FFB347" stroke="{k}" stroke-width="2" stroke-linejoin="round"/><path d="M10 30 L12 23 L17 28Z" fill="#F6D7C3" stroke="{k}" stroke-width="1.6"/><path d="M8 34 L32 34" stroke="{k}" stroke-width="2"/>',
        "entoure": f'<text x="20" y="25" font-size="13" text-anchor="middle" font-family="Poppins" font-weight="700" fill="{k}">ab</text><ellipse cx="20" cy="21" rx="14" ry="10" fill="none" stroke="#E4572E" stroke-width="2.6"/>',
        "relie": f'<circle cx="9" cy="12" r="3.5" fill="{k}"/><circle cx="31" cy="28" r="3.5" fill="{k}"/><path d="M9 12 L31 28" stroke="#E4572E" stroke-width="2.6"/><circle cx="9" cy="28" r="3.5" fill="none" stroke="{k}" stroke-width="2"/><circle cx="31" cy="12" r="3.5" fill="none" stroke="{k}" stroke-width="2"/>',
        "colorie": f'<rect x="7" y="8" width="7" height="22" rx="2" fill="#E4572E" stroke="{k}" stroke-width="1.5" transform="rotate(-12 10 19)"/><rect x="16" y="8" width="7" height="22" rx="2" fill="#2BA88F" stroke="{k}" stroke-width="1.5"/><rect x="25" y="8" width="7" height="22" rx="2" fill="#4A7BD1" stroke="{k}" stroke-width="1.5" transform="rotate(12 28 19)"/>',
        "coche": f'<rect x="8" y="8" width="24" height="24" rx="4" fill="#fff" stroke="{k}" stroke-width="2"/><path d="M12 20 L18 26 L29 12" stroke="#2BA88F" stroke-width="3.4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>',
        "souligne": f'<text x="20" y="22" font-size="13" text-anchor="middle" font-family="Poppins" font-weight="700" fill="{k}">abc</text><path d="M7 28 L33 28" stroke="#E4572E" stroke-width="3" stroke-linecap="round"/>',
        "decoupe": f'<circle cx="12" cy="28" r="4.5" fill="none" stroke="{k}" stroke-width="2.4"/><circle cx="12" cy="12" r="4.5" fill="none" stroke="{k}" stroke-width="2.4"/><path d="M15 25 L33 11 M15 15 L33 29" stroke="{k}" stroke-width="2.4" stroke-linecap="round"/>',
        "colle": f'<rect x="13" y="14" width="14" height="20" rx="3" fill="#9AD3F5" stroke="{k}" stroke-width="2"/><rect x="15" y="6" width="10" height="9" rx="2" fill="#fff" stroke="{k}" stroke-width="2"/>',
        "regarde": f'<path d="M5 20 Q20 6 35 20 Q20 34 5 20Z" fill="#fff" stroke="{k}" stroke-width="2.2"/><circle cx="20" cy="20" r="6" fill="#4A7BD1"/><circle cx="20" cy="20" r="2.6" fill="{k}"/>',
        "repete": f'<path d="M10 18 A10 10 0 0 1 30 16" fill="none" stroke="{k}" stroke-width="2.6"/><path d="M30 8 L30 16 L22 16" fill="none" stroke="{k}" stroke-width="2.6"/><path d="M30 22 A10 10 0 0 1 10 24" fill="none" stroke="#E4572E" stroke-width="2.6"/><path d="M10 32 L10 24 L18 24" fill="none" stroke="#E4572E" stroke-width="2.6"/>',
        "seul": f'<circle cx="20" cy="13" r="5.5" fill="#F29E4C" stroke="{k}" stroke-width="1.8"/><path d="M10 33 Q10 21 20 21 Q30 21 30 33Z" fill="#F29E4C" stroke="{k}" stroke-width="1.8"/>',
        "duo": f'<circle cx="13" cy="13" r="5" fill="#F29E4C" stroke="{k}" stroke-width="1.6"/><path d="M5 32 Q5 21 13 21 Q21 21 21 32Z" fill="#F29E4C" stroke="{k}" stroke-width="1.6"/><circle cx="27" cy="13" r="5" fill="#2BA88F" stroke="{k}" stroke-width="1.6"/><path d="M19 32 Q19 21 27 21 Q35 21 35 32Z" fill="#2BA88F" stroke="{k}" stroke-width="1.6"/>',
        "groupe": f'<circle cx="11" cy="15" r="4" fill="#F29E4C" stroke="{k}" stroke-width="1.4"/><circle cx="29" cy="15" r="4" fill="#4A7BD1" stroke="{k}" stroke-width="1.4"/><path d="M4 31 Q4 22 11 22 Q18 22 18 31Z" fill="#F29E4C" stroke="{k}" stroke-width="1.4"/><path d="M22 31 Q22 22 29 22 Q36 22 36 31Z" fill="#4A7BD1" stroke="{k}" stroke-width="1.4"/><circle cx="20" cy="12" r="4.5" fill="#2BA88F" stroke="{k}" stroke-width="1.4"/><path d="M12 33 Q12 20 20 20 Q28 20 28 33Z" fill="#2BA88F" stroke="{k}" stroke-width="1.4"/>',
        "recopie": f'<rect x="5" y="9" width="12" height="22" rx="2" fill="#fff" stroke="{k}" stroke-width="1.8"/><rect x="23" y="9" width="12" height="22" rx="2" fill="#fff" stroke="{k}" stroke-width="1.8"/><path d="M8 15 H14 M8 19 H14 M8 23 H14 M26 15 H32 M26 19 H31" stroke="{k}" stroke-width="1.4"/><path d="M17 20 L23 20 M20 17 L23 20 L20 23" stroke="#E4572E" stroke-width="2" fill="none"/>',
        "complete": f'<text x="6" y="24" font-size="12" font-family="Poppins" font-weight="700" fill="{k}">a</text><rect x="15" y="12" width="12" height="15" rx="2" fill="#FFF3C4" stroke="#E4572E" stroke-width="2" stroke-dasharray="3 2"/><text x="29" y="24" font-size="12" font-family="Poppins" font-weight="700" fill="{k}">c</text>',
        "barre": f'<text x="20" y="25" font-size="14" text-anchor="middle" font-family="Poppins" font-weight="700" fill="{k}">abc</text><path d="M7 30 L33 12" stroke="#E4572E" stroke-width="3" stroke-linecap="round"/>',
        "montre": f'<path d="M14 34 L14 20 Q14 17 17 17 L17 7 Q17 4 20 4 Q23 4 23 7 L23 17 L28 18 Q32 19 31 23 L29 34Z" fill="#F6D7C3" stroke="{k}" stroke-width="2" stroke-linejoin="round"/>',
        "dessine": f'<rect x="6" y="7" width="28" height="22" rx="2" fill="#fff" stroke="{k}" stroke-width="2"/><path d="M9 26 L16 17 L21 22 L25 18 L31 26Z" fill="#2BA88F"/><circle cx="27" cy="12" r="3" fill="#FFD166"/><path d="M20 29 L20 35 M14 35 L26 35" stroke="{k}" stroke-width="2"/>',
        "trace": f'<path d="M7 30 Q12 8 20 20 Q28 32 33 10" fill="none" stroke="{k}" stroke-width="2.4" stroke-dasharray="3 3" stroke-linecap="round"/><circle cx="7" cy="30" r="3" fill="#2BA88F"/>',
        "numerote": f'<text x="20" y="27" font-size="17" text-anchor="middle" font-family="Poppins" font-weight="800" fill="{k}">123</text>',
        "joue": f'<rect x="7" y="7" width="26" height="26" rx="5" fill="#fff" stroke="{k}" stroke-width="2.2"/><circle cx="14" cy="14" r="2.6" fill="{k}"/><circle cx="26" cy="14" r="2.6" fill="{k}"/><circle cx="20" cy="20" r="2.6" fill="{k}"/><circle cx="14" cy="26" r="2.6" fill="{k}"/><circle cx="26" cy="26" r="2.6" fill="{k}"/>',
    }[name]
    return s + bg + body + '</svg>'


def bubble_svg(text, w=160, h=60, tail="left", fill="#fff"):
    return text


# ---------- SCÈNES ----------
def scene_classroom(width=700):
    """Une classe vue de face : tableau, prof, élèves. Utilisée en ouverture de module."""
    s = [f'<svg viewBox="0 0 700 330" width="{width}" class="scene">']
    s.append('<rect x="0" y="0" width="700" height="330" fill="#FDF6E9"/>')
    s.append('<rect x="0" y="250" width="700" height="80" fill="#E9D8B9"/>')
    # fenêtre
    s.append('<rect x="560" y="30" width="110" height="120" rx="6" fill="#BFE3F7" stroke="#8a6b47" stroke-width="6"/><path d="M615 30 V150 M560 90 H670" stroke="#8a6b47" stroke-width="5"/>'
             '<circle cx="640" cy="60" r="12" fill="#FFD166"/>')
    # tableau
    s.append('<rect x="120" y="30" width="400" height="160" rx="8" fill="#2F5D50" stroke="#8a6b47" stroke-width="8"/>')
    s.append('<text x="320" y="95" font-family="Poppins" font-size="42" font-weight="700" fill="#fff" text-anchor="middle">Bonjour !</text>')
    s.append('<text x="320" y="140" font-family="Poppins" font-size="20" fill="#E8F3EE" text-anchor="middle">Hello · Привіт · مرحبا · Salam · Olá</text>')
    s.append('<text x="320" y="172" font-family="Poppins" font-size="16" fill="#cfe6dc" text-anchor="middle">lundi 24 août</text>')
    # horloge
    s.append('<circle cx="60" cy="70" r="30" fill="#fff" stroke="#1F2A44" stroke-width="4"/><path d="M60 70 L60 50 M60 70 L74 76" stroke="#1F2A44" stroke-width="4" stroke-linecap="round"/>')
    # alphabet frise
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i, L in enumerate(letters):
        x = 20 + i * 26
        s.append(f'<rect x="{x}" y="205" width="22" height="26" rx="4" fill="{["#F29E4C","#2BA88F","#4A7BD1","#C94F7C","#F2C14E"][i%5]}"/><text x="{x+11}" y="224" font-family="Poppins" font-size="15" font-weight="700" fill="#fff" text-anchor="middle">{L}</text>')
    s.append('</svg>')
    return "".join(s)


def ecole_plan():
    pass


def face(skin="moyen", hair="#3B2516", style="court", beard=False, glasses=False, eyes="#3B2516", size=60, shirt="#4A7BD1", gray=False):
    """Visage générique paramétrable (pour familles, jeux « Qui est-ce ? »)."""
    sk = SKIN.get(skin, skin)
    if gray:
        hair = "#BDBDBD"
    p = [f'<path d="M16 100 Q18 78 50 76 Q82 78 84 100Z" fill="{shirt}"/>', f'<rect x="43" y="62" width="14" height="14" rx="4" fill="{_darken(sk,.9)}"/>']
    if style in ("long", "queue"):
        p.append(f'<path d="M24 40 Q20 80 30 86 L70 86 Q80 80 76 40 Q74 14 50 14 Q26 14 24 40Z" fill="{hair}"/>')
    p.append(f'<circle cx="27" cy="46" r="5" fill="{sk}"/><circle cx="73" cy="46" r="5" fill="{sk}"/><ellipse cx="50" cy="44" rx="23" ry="25" fill="{sk}"/>')
    if style == "court":
        p.append(f'<path d="M27 40 Q27 17 50 17 Q73 17 73 40 Q70 27 50 27 Q30 27 27 40Z" fill="{hair}"/>')
    elif style in ("long", "queue"):
        p.append(f'<path d="M26 42 Q26 18 50 18 Q74 18 74 42 Q66 26 50 28 Q34 26 26 42Z" fill="{hair}"/>')
    elif style == "boucle":
        for x, y in [(32, 26), (40, 21), (50, 19), (60, 21), (68, 26), (28, 34), (72, 34)]:
            p.append(f'<circle cx="{x}" cy="{y}" r="7" fill="{hair}"/>')
    elif style == "chauve":
        p.append(f'<path d="M27 44 Q26 34 30 30 M73 44 Q74 34 70 30" stroke="{hair}" stroke-width="4" fill="none"/>')
    if beard:
        p.append(f'<path d="M30 52 Q32 70 50 71 Q68 70 70 52 Q66 62 50 63 Q34 62 30 52Z" fill="{hair}"/>')
    p.append(f'<circle cx="41" cy="45" r="3.2" fill="{eyes}"/><circle cx="59" cy="45" r="3.2" fill="{eyes}"/><circle cx="41.8" cy="44" r="1" fill="#fff"/><circle cx="59.8" cy="44" r="1" fill="#fff"/>')
    if gray:
        p.append('<path d="M35 52 Q37 54 39 52 M61 52 Q63 54 65 52" stroke="#a0705a" stroke-width="1" fill="none"/>')
    if glasses:
        p.append('<circle cx="41" cy="45" r="7" fill="none" stroke="#333" stroke-width="1.6"/><circle cx="59" cy="45" r="7" fill="none" stroke="#333" stroke-width="1.6"/><path d="M48 45 L52 45" stroke="#333" stroke-width="1.6"/>')
    p.append('<path d="M42 56 Q50 62 58 56" stroke="#7A2E2E" stroke-width="2.2" fill="none" stroke-linecap="round"/>')
    return f'<svg viewBox="0 0 100 100" width="{size}" height="{size}">{"".join(p)}</svg>'
