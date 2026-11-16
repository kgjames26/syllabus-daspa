"""Réglages communs au volume 2 « Je me débrouille » (A2)."""
from .base import Ex
from .module import set_volume

V2COL = "#2BA88F"
CPCOL = "#BDE7DA"
set_volume(2, "★ Coup de pouce", "★ COUP DE POUCE", CPCOL, "coup de pouce : pages simplifiées pour ceux qui ont besoin d'aide")
Ex.TAG = "★ COUP DE POUCE"

CP = ('<div style="background:' + CPCOL + ';margin:-17mm -14mm 4mm -14mm;padding:15mm 14mm 3mm 14mm;display:flex;align-items:center;gap:4mm">'
      '<span style="font-size:20pt;font-weight:800">★ COUP DE POUCE</span><span class="big">{t}</span></div>')


def v2_cover(b, title, sub, mod_label):
    from .art import avatar
    cast = "".join(f'<div style="text-align:center">{avatar(k, 92, m)}</div>' for k, m in [("nour", "rire"), ("yonas", "sourire"), ("daria", "rire"), ("mateo", "sourire"), ("amina", "rire"), ("bilal", "sourire"), ("fatou", "rire")])
    b.page(f'''<div style="height:297mm;background:#EEF8F4;position:relative;overflow:hidden">
 <div style="position:absolute;top:-70mm;right:-70mm;width:160mm;height:160mm;border-radius:50%;background:{V2COL}"></div>
 <div style="position:absolute;bottom:-40mm;left:-40mm;width:120mm;height:120mm;border-radius:50%;background:#4A7BD1;opacity:.85"></div>
 <div style="position:absolute;top:62mm;right:22mm;width:26mm;height:26mm;border-radius:50%;background:#FFD166"></div>
 <div style="position:relative;padding:24mm 18mm">
  <div style="font-size:11pt;letter-spacing:3px;font-weight:700;color:{V2COL}">FRANÇAIS · DASPA · VOLUME 2</div>
  <div style="font-size:58pt;font-weight:800;line-height:1;margin-top:10mm;color:#1F2A44">{title}</div>
  <div style="font-size:18pt;margin-top:6mm;color:#1F2A44">{sub}</div>
  <div style="margin-top:14mm;display:flex;gap:3mm;flex-wrap:wrap;max-width:125mm">
   {"".join(f'<span class="pill" style="background:#fff;border:2px solid #1F2A44;font-size:12pt">{w}</span>' for w in ["raconter", "comprendre", "agir seul", "lire", "écrire", "réussir", "oser"])}
  </div>
 </div>
 <div style="position:absolute;bottom:34mm;left:12mm;right:12mm;display:flex;justify-content:space-between;align-items:flex-end;background:#fff;border-radius:8mm;padding:6mm 5mm 0 5mm;box-shadow:0 2mm 6mm rgba(0,0,0,.12)">{cast}</div>
 <div style="position:absolute;bottom:14mm;left:18mm;font-size:10pt;color:#1F2A44"><b>{mod_label}</b> — édition de travail</div>
</div>''', full=True)


def v2_mon_livre(b):
    from .base import blank, dots, ATELIERS
    b.page(f'''<div class="flex top" style="gap:8mm">
 <div style="width:58mm;height:70mm;border:3px dashed #1F2A44;border-radius:4mm;display:flex;align-items:center;justify-content:center;text-align:center" class="muted">Ma photo<br>ou mon dessin</div>
 <div class="grow"><h1>Ce livre est à moi !</h1>
  <p class="big mt4">Prénom et NOM : {blank("l")}</p><p class="big mt4">Classe : {blank()} Année scolaire : {blank()}</p>
  <p class="big mt4">Ma prof de français : {blank("l")}</p><p class="big mt4">Mes langues : {blank("l")}</p></div></div>
<h2 class="mt4" style="margin-top:8mm">Le volume 2, comment ça marche ?</h2>
<div class="grid2">
 <div class="card"><b>Un module = environ 2 semaines</b><p class="sm mt2">👀 Je découvre (BD, texte) → 🔤 j'apprends les mots → 📌 j'étudie les leçons → ✏️ je m'entraîne → 📄 je lis des documents de la vie → 🎒 je travaille le français de l'école → 🎯 je réalise la tâche finale → 📝 je passe le test.</p></div>
 <div class="card"><b>Les points = la difficulté</b><p class="mt2">{dots(1)} &nbsp;Je découvre.</p><p>{dots(2)} &nbsp;Je m'entraîne.</p><p>{dots(3)} &nbsp;Défi ! Je vais plus loin.</p></div>
 <div class="card"><b>Les couleurs = les ateliers</b><p class="mt2"><span class="atl A">{ATELIERS["A"]}</span> <span class="atl B">{ATELIERS["B"]}</span> <span class="atl C">{ATELIERS["C"]}</span></p><p><span class="atl D">{ATELIERS["D"]}</span> <span class="atl P">{ATELIERS["P"]}</span></p></div>
 <div class="card"><b><span class="alpha-tag" style="background:{CPCOL}">★ COUP DE POUCE</span></b><p class="sm mt2">Ces pages reprennent l'essentiel du module avec plus d'aide : textes plus courts, modèles, exercices guidés. La prof te dit si c'est pour toi. Tout le monde peut les utiliser pour réviser !</p></div>
</div>
<div class="astuce mt4"><b>Nouveau au volume 2 :</b> des textes plus longs, le passé, des documents vrais de la vie en Belgique et beaucoup de <b>français de l'école</b> pour préparer la classe ordinaire. Courage, tu as déjà fait un grand chemin ! 💪</div>''', "Mon livre", levels=False)
    b.page("%%SOMMAIRE%%", "Sommaire", levels=False)
