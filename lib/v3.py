"""Réglages communs au volume 3 « Je réussis à l'école » (B1 + français de scolarisation)."""
from .base import Ex
from .module import set_volume

V3COL = "#4A7BD1"
CPCOL = "#CFE0FA"
set_volume(3, "★ Coup de pouce", "★ COUP DE POUCE", CPCOL, "coup de pouce : pages de remédiation guidées")
Ex.TAG = "★ COUP DE POUCE"

CP = ('<div style="background:' + CPCOL + ';margin:-17mm -14mm 4mm -14mm;padding:15mm 14mm 3mm 14mm;display:flex;align-items:center;gap:4mm">'
      '<span style="font-size:20pt;font-weight:800">★ COUP DE POUCE</span><span class="big">{t}</span></div>')

# bandeau des pages « Vers les épreuves » (CE1D, DELF B1)
EPR = ('<div style="background:#1F2A44;color:#fff;margin:-17mm -14mm 4mm -14mm;padding:14mm 14mm 4mm 14mm"><div style="font-size:10.5pt;font-weight:700;opacity:.85;letter-spacing:1px">🎓 VERS LES ÉPREUVES · {k}</div>'
       '<div style="font-size:21pt;font-weight:800">{t}</div></div>')

DISC = {"maths": ("📐", "#E4572E"), "sciences": ("🔬", "#2BA88F"), "histoire": ("🏛️", "#9B5DE5"), "géographie": ("🗺️", "#4A7BD1"), "français": ("📚", "#D1495B"), "citoyenneté": ("⚖️", "#6B8F3E")}


def disc_tag(d):
    e, c = DISC[d]
    return f'<span style="background:{c};color:#fff;font-size:8.5pt;font-weight:700;padding:.6mm 2.4mm;border-radius:3mm">{e} {d.upper()}</span>'


def v3_cover(b, title, sub, mod_label):
    from .art import avatar
    cast = "".join(f'<div style="text-align:center">{avatar(k, 92, m)}</div>' for k, m in [("amina", "sourire"), ("yonas", "rire"), ("daria", "sourire"), ("mateo", "rire"), ("bilal", "sourire"), ("fatou", "rire"), ("prof", "sourire")])
    b.page(f'''<div style="height:297mm;background:#EEF3FC;position:relative;overflow:hidden">
 <div style="position:absolute;top:-60mm;right:-60mm;width:150mm;height:150mm;border-radius:50%;background:{V3COL}"></div>
 <div style="position:absolute;bottom:-45mm;left:-45mm;width:125mm;height:125mm;border-radius:50%;background:#2BA88F;opacity:.85"></div>
 <div style="position:absolute;top:66mm;right:26mm;width:24mm;height:24mm;border-radius:50%;background:#FFD166"></div>
 <div style="position:relative;padding:24mm 18mm">
  <div style="font-size:11pt;letter-spacing:3px;font-weight:700;color:{V3COL}">FRANÇAIS · DASPA · VOLUME 3</div>
  <div style="font-size:54pt;font-weight:800;line-height:1;margin-top:10mm;color:#1F2A44">{title}</div>
  <div style="font-size:17pt;margin-top:6mm;color:#1F2A44">{sub}</div>
  <div style="margin-top:14mm;display:flex;gap:3mm;flex-wrap:wrap;max-width:128mm">
   {"".join(f'<span class="pill" style="background:#fff;border:2px solid #1F2A44;font-size:12pt">{w}</span>' for w in ["comprendre les cours", "prendre des notes", "argumenter", "maths", "sciences", "histoire", "géographie", "CE1D", "DELF B1"])}
  </div>
 </div>
 <div style="position:absolute;bottom:34mm;left:12mm;right:12mm;display:flex;justify-content:space-between;align-items:flex-end;background:#fff;border-radius:8mm;padding:6mm 5mm 0 5mm;box-shadow:0 2mm 6mm rgba(0,0,0,.12)">{cast}</div>
 <div style="position:absolute;bottom:14mm;left:18mm;font-size:10pt;color:#1F2A44"><b>{mod_label}</b> — édition de travail</div>
</div>''', full=True)


def v3_mon_livre(b):
    from .base import blank, dots, ATELIERS
    b.page(f'''<div class="flex top" style="gap:8mm">
 <div style="width:58mm;height:70mm;border:3px dashed #1F2A44;border-radius:4mm;display:flex;align-items:center;justify-content:center;text-align:center" class="muted">Ma photo<br>ou mon dessin</div>
 <div class="grow"><h1>Ce livre est à moi !</h1>
  <p class="big mt4">Prénom et NOM : {blank("l")}</p><p class="big mt4">Classe : {blank()} Année scolaire : {blank()}</p>
  <p class="big mt4">Ma classe d'accueil après le DASPA : {blank("l")}</p><p class="big mt4">Mes langues : {blank("l")}</p></div></div>
<h2 class="mt4" style="margin-top:8mm">Le volume 3, comment ça marche ?</h2>
<div class="grid2">
 <div class="card"><b>Un module = environ 2 semaines</b><p class="sm mt2">👀 Je découvre → 🔤 j'apprends le vocabulaire (aussi celui des cours) → 📌 j'étudie les leçons → ✏️ je m'entraîne → 📄 je lis des documents → 🎒 je travaille la méthode et la langue des disciplines → 🎓 je me prépare aux épreuves (CE1D, DELF B1) → 🎯 tâche finale → 📝 test.</p></div>
 <div class="card"><b>Les points = la difficulté</b><p class="mt2">{dots(1)} &nbsp;Je comprends.</p><p>{dots(2)} &nbsp;Je m'entraîne.</p><p>{dots(3)} &nbsp;Défi : comme en classe ordinaire !</p></div>
 <div class="card"><b>Les couleurs = les ateliers</b><p class="mt2"><span class="atl A">{ATELIERS["A"]}</span> <span class="atl B">{ATELIERS["B"]}</span> <span class="atl C">{ATELIERS["C"]}</span></p><p><span class="atl D">{ATELIERS["D"]}</span> <span class="atl P">{ATELIERS["P"]}</span></p></div>
 <div class="card"><b><span class="alpha-tag" style="background:{CPCOL}">★ COUP DE POUCE</span></b><p class="sm mt2">Des pages guidées pour revoir l'essentiel du module avec des modèles. La prof te dit si c'est pour toi ; tout le monde peut s'en servir pour réviser.</p></div>
</div>
<div class="astuce mt4"><b>Nouveau au volume 3 :</b> des textes plus longs, la langue des <b>maths</b>, des <b>sciences</b>, de l'<b>histoire</b> et de la <b>géographie</b>, des méthodes pour étudier, et des pages <b>🎓 Vers les épreuves</b> pour préparer le CE1D et le DELF B1. Tu es presque prêt(e) pour la classe ordinaire ! 🚀</div>''', "Mon livre", levels=False)
    b.page("%%SOMMAIRE%%", "Sommaire", levels=False)
