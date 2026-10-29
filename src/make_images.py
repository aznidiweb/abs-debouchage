# Génère les images de partage (og.png), logo et icônes à partir de HTML/SVG.  Usage : python3 src/make_images.py
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build import LOGO, OUT
from content import PHONE_DISPLAY
from playwright.sync_api import sync_playwright

def og(title, sub, chips):
    ch = "".join(f'<span>{c}</span>' for c in chips)
    return f'''<html><body style="margin:0;width:1200px;height:630px;background:#0c1d38;font-family:Arial,Helvetica,sans-serif;color:#fff;position:relative;overflow:hidden">
<div style="position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.05) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.05) 1px,transparent 1px);background-size:48px 48px"></div>
<div style="position:absolute;right:-180px;top:-220px;width:700px;height:700px;background:radial-gradient(circle,rgba(249,115,22,.35),transparent 62%)"></div>
<div style="position:absolute;left:72px;top:64px;display:flex;align-items:center;gap:18px"><div style="width:72px;height:72px">{LOGO}</div><div><div style="font-weight:900;font-size:34px;letter-spacing:-.5px">ABS DÉBOUCHAGE</div><div style="color:#fb923c;font-weight:700;letter-spacing:3px;font-size:16px;margin-top:6px">{sub}</div></div></div>
<div style="position:absolute;left:72px;top:210px;font-weight:900;font-size:76px;line-height:1.02;letter-spacing:-2px;width:1000px">{title}</div>
<div style="position:absolute;left:72px;bottom:64px;display:flex;gap:14px;align-items:center">
 <div style="background:#c2410c;border-radius:16px;padding:18px 28px;font-weight:900;font-size:40px">☎ {PHONE_DISPLAY}</div>
 <div style="display:flex;gap:10px;font-size:22px;font-weight:700;color:#dbe6f7">{ch}</div></div>
<style>span{{border:2px solid rgba(255,255,255,.25);border-radius:999px;padding:10px 18px}}svg{{width:100%;height:100%}}</style>
</body></html>'''

p = sync_playwright().start(); b = p.chromium.launch()
def shot(htmlstr, path, w, h, transparent=False):
    pg = b.new_page(viewport={"width": w, "height": h})
    pg.set_content(htmlstr); pg.screenshot(path=os.path.join(OUT, path), omit_background=transparent); pg.close()
os.makedirs(os.path.join(OUT, "assets"), exist_ok=True)
shot(og('Débouchage à Bruxelles<br><span style="color:#fb923c;border:0;padding:0;font-size:76px">sur place en 30 min</span>', "URGENCE 24H/24 – 7J/7", ["Devis gratuit", "Agréé assurances"]), "assets/og.png", 1200, 630)
shot(og('Ontstopping in Brussel<br><span style="color:#fb923c;border:0;padding:0;font-size:76px">binnen 30 min ter plaatse</span>', "SPOED 24/7", ["Gratis offerte", "Erkend door verzekeraars"]), "assets/og-nl.png", 1200, 630)
icon = lambda s: f'<html><body style="margin:0;width:{s}px;height:{s}px">{LOGO.replace("<svg ", f"<svg width={s} height={s} ")}</body></html>'
for name, s in (("apple-touch-icon.png", 180), ("icon-192.png", 192), ("icon-512.png", 512), ("assets/logo.png", 512), ("favicon-32.png", 32)):
    shot(icon(s), name, s, s, transparent=True)
b.close()
# favicon.ico à partir du PNG 32px
from PIL import Image
im = Image.open(os.path.join(OUT, "favicon-32.png")); im.save(os.path.join(OUT, "favicon.ico"), sizes=[(32, 32)]); os.remove(os.path.join(OUT, "favicon-32.png"))
print("images OK")
