"""Contrôle de mise en page : python3 lib/overflow.py out/X.html → marge libre (mm) sous le contenu de chaque page ; OVERFLOW si < 1 mm, VIDE si > 110 mm."""
import sys
from playwright.sync_api import sync_playwright
import os; html=os.path.abspath(sys.argv[1])
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':900,'height':1200})
    pg.goto('file://'+html); pg.wait_for_timeout(1500)
    r=pg.evaluate('''()=>{const out=[];document.querySelectorAll('section.page').forEach((s,i)=>{
      if(s.classList.contains('full'))return; const f=s.querySelector('.ftr'); if(!f)return;
      const ft=f.getBoundingClientRect().top; const st=s.getBoundingClientRect(); let mx=0;
      s.querySelectorAll('*').forEach(e=>{ if(e.closest('.ftr')||e.closest('.hdr'))return; const r=e.getBoundingClientRect(); if(r.height>0&&r.bottom>mx)mx=r.bottom;});
      out.push([i+1, Math.round((ft-mx)/3.78), Math.round((st.bottom-mx)/3.78)]);});return out;}''')
    for i,free,_ in r:
        flag = 'OVERFLOW' if free<1 else ('VIDE' if free>110 else '')
        print(i, free, flag)
    b.close()
