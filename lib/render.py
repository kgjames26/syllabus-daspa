import subprocess, os
def to_pdf(html, path):
    hp = path.replace('.pdf', '.html')
    with open(hp, 'w') as f: f.write(html)
    subprocess.run(['google-chrome','--headless','--no-sandbox','--disable-gpu','--no-pdf-header-footer',
                    '--virtual-time-budget=10000', f'--print-to-pdf={path}', 'file://'+os.path.abspath(hp)],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
def preview(path, outdir, pages=None, r=45):
    os.makedirs(outdir, exist_ok=True)
    args = ['pdftoppm','-r',str(r),'-png']
    if pages: args += ['-f',str(pages[0]),'-l',str(pages[1])]
    subprocess.run(args+[path, os.path.join(outdir,'p')], check=True)
