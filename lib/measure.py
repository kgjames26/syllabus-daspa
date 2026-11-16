"""Mesure la hauteur réelle (mm) de fragments HTML avec Chrome headless, pour paginer sans débordement."""
import json, os, re, subprocess, tempfile
from .base import CSS

PX_MM = 96 / 25.4


def heights(fragments, width_mm=182):
    """Hauteur en mm de chaque fragment, rendu à la largeur utile d'une page."""
    body = "".join(f'<div class="m" style="width:{width_mm}mm;display:flow-root">{f}</div>' for f in fragments)
    js = ("<script>window.onload=function(){var h=[];document.querySelectorAll('.m').forEach(function(d){h.push(d.getBoundingClientRect().height)});"
          "var p=document.createElement('pre');p.id='H';p.textContent=JSON.stringify(h);document.body.appendChild(p)}</script>")
    html = f'<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><style>{CSS}</style></head><body style="width:210mm">{body}{js}</body></html>'
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False) as f:
        f.write(html)
        path = f.name
    out = subprocess.run(['google-chrome', '--headless', '--no-sandbox', '--disable-gpu', '--virtual-time-budget=8000', '--dump-dom', 'file://' + path],
                         capture_output=True, text=True).stdout
    os.unlink(path)
    m = re.search(r'<pre id="H">(.*?)</pre>', out, re.S)
    return [x / PX_MM for x in json.loads(m.group(1))]


def pack(blocks, first, budget, gap=0):
    """Regroupe des blocs (html) en pages selon leur hauteur réelle. first/budget en mm."""
    hs = heights(blocks)
    pages, cur, used, bud = [], [], 0, first
    for blk, h in zip(blocks, hs):
        if cur and used + h + gap > bud:
            pages.append(cur)
            cur, used, bud = [], 0, budget
        cur.append(blk)
        used += h + gap
    if cur:
        pages.append(cur)
    return pages
