# Génère les images de partage (og.png), logo et icônes à partir de HTML/SVG.  Usage : python3 src/make_images.py
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build import LOGO, OUT
from content import PHONE_DISPLAY
from playwright.sync_api import sync_playwright

import base64
_FONT = base64.b64encode(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "fonts", "plus-jakarta-sans.woff2"), "rb").read()).decode()

def og(line, call):
    """Image de partage : logo au centre (lisible même quand l'aperçu est recadré en carré), fond bleu nuit du site."""
    logo = LOGO.replace("<svg ", '<svg width="100%" height="100%" ')
    return f'''<html><head><style>
@font-face{{font-family:J;src:url(data:font/woff2;base64,{_FONT}) format("woff2");font-weight:200 800}}
body{{margin:0;width:1200px;height:630px;overflow:hidden;font-family:J,Arial,sans-serif;color:#fff;
 background:radial-gradient(90% 120% at 50% 35%,#123468 0%,#0a1a33 48%,#060d19 100%)}}
.c{{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}}
.lg{{width:176px;height:176px;border-radius:44px;box-shadow:0 0 0 10px rgba(84,136,247,.16),0 24px 60px -18px rgba(0,0,0,.7)}}
.nm{{margin-top:34px;font-weight:800;font-size:66px;letter-spacing:-1.5px;line-height:1}}
.nm b{{color:#5488f7;font-weight:800}}
.ln{{margin-top:18px;font-size:27px;font-weight:600;color:#c9d6ee}}
.ph{{margin-top:30px;display:inline-flex;align-items:center;gap:14px;background:#1156c7;border-radius:999px;padding:14px 30px 14px 16px;font-size:32px;font-weight:800;letter-spacing:.5px}}
.ph i{{width:44px;height:44px;border-radius:50%;background:#fff;display:flex;align-items:center;justify-content:center}}
.ph svg{{width:24px;height:24px}}
</style></head><body><div class="c">
<div class="lg">{logo}</div>
<div class="nm">ABS <b>Débouchage</b></div>
<div class="ln">{line}</div>
<div class="ph"><i><svg viewBox="0 0 24 24" fill="none" stroke="#1156c7" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/></svg></i>{call}</div>
</div></body></html>'''

p = sync_playwright().start(); b = p.chromium.launch()
def shot(htmlstr, path, w, h, transparent=False):
    pg = b.new_page(viewport={"width": w, "height": h})
    pg.set_content(htmlstr); pg.screenshot(path=os.path.join(OUT, path), omit_background=transparent); pg.close()
os.makedirs(os.path.join(OUT, "assets"), exist_ok=True)
shot(og("7j/7 · 6h–21h · Bruxelles et toute la Belgique", PHONE_DISPLAY), "assets/og.png", 1200, 630)
shot(og("7/7 · 6–21 uur · Brussel en heel België", PHONE_DISPLAY), "assets/og-nl.png", 1200, 630)
# WhatsApp n'affiche pas l'aperçu si l'image dépasse ~300 Ko : palette 256 couleurs (≈120 Ko, rendu identique)
from PIL import Image
for _p in ("assets/og.png", "assets/og-nl.png"):
    _f = os.path.join(OUT, _p)
    Image.open(_f).convert("RGB").quantize(colors=256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.FLOYDSTEINBERG).save(_f, optimize=True)
icon = lambda s: f'<html><body style="margin:0;width:{s}px;height:{s}px">{LOGO.replace("<svg ", f"<svg width={s} height={s} ")}</body></html>'
for name, s in (("apple-touch-icon.png", 180), ("icon-192.png", 192), ("icon-512.png", 512), ("assets/logo.png", 512), ("favicon-32.png", 32)):
    shot(icon(s), name, s, s, transparent=True)
b.close()
# favicon.ico à partir du PNG 32px
from PIL import Image
im = Image.open(os.path.join(OUT, "favicon-32.png")); im.save(os.path.join(OUT, "favicon.ico"), sizes=[(32, 32)]); os.remove(os.path.join(OUT, "favicon-32.png"))
print("images OK")
