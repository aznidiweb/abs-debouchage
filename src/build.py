# -*- coding: utf-8 -*-
"""
Générateur du site ABS Débouchage.
Usage :  python3 src/build.py      → régénère tout le dossier public/
"""
import json, os, shutil, html, datetime
from content import *

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(ROOT), "public")
TODAY = datetime.date.today().isoformat()
VERSION = TODAY.replace("-", "")
e = html.escape

# ---------------------------------------------------------------- icônes SVG
P = {
 "phone": '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/>',
 "check": '<path d="M20 6 9 17l-5-5"/>',
 "clock": '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
 "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/>',
 "file": '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M16 13H8M16 17H8M10 9H8"/>',
 "euro": '<path d="M4 10h12M4 14h9"/><path d="M19 6a7.7 7.7 0 0 0-5.2-2A7.9 7.9 0 0 0 6 12c0 4.4 3.5 8 7.8 8 2 0 3.8-.8 5.2-2"/>',
 "gauge": '<path d="m12 14 4-4"/><path d="M3.34 19a10 10 0 1 1 17.32 0"/>',
 "camera": '<path d="m22 8-6 4 6 4V8z"/><rect x="2" y="6" width="14" height="12" rx="2"/>',
 "toilet": '<path d="M6 3h7v8H6z"/><path d="M4 11h16c0 3.3-2.7 6-6 6h-4c-3.3 0-6-2.7-6-6z"/><path d="m9 17-1 4h8l-1-4"/>',
 "sanibroyeur": '<path d="M4 3h6v8H4z"/><path d="M2 11h13c0 3-2.2 5.5-5 5.5H7.5C4.6 16.5 2 14 2 11z"/><path d="m6 16.5-1 4.5h7l-1-4.5"/><path d="m19 3-2.5 4h4L18 11"/>',
 "sink": '<path d="M12 3v5M12 3h4"/><path d="M3 10h18"/><path d="M5 10v2a5 5 0 0 0 5 5h4a5 5 0 0 0 5-5v-2"/><path d="M12 17v4"/>',
 "basin": '<path d="M9 4h3v5"/><path d="M3 9h18v1a7 7 0 0 1-7 7h-4a7 7 0 0 1-7-7z"/><path d="M12 17v4"/>',
 "shower": '<path d="m4 4 2.5 2.5"/><path d="M13.5 6.5a4.95 4.95 0 0 0-7 7"/><path d="M15 5 5 15"/><path d="M14 17v.01M10 16v.01M13 13v.01M16 10v.01M11 20v.01M17 14v.01M20 11v.01"/>',
 "bath": '<path d="M9 6 6.5 3.5a1.5 1.5 0 0 0-1-.5C4.68 3 4 3.68 4 4.5V17a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-5"/><path d="M10 5 8 7M2 12h20M7 19v2M17 19v2"/>',
 "pipes": '<path d="M2 6h8a4 4 0 0 1 4 4v11"/><path d="M2 10h6a2 2 0 0 1 2 2v9"/><path d="M18 3v6M22 3v6M16 9h8"/>',
 "manhole": '<circle cx="12" cy="12" r="9"/><path d="M7 9h10M6 12h12M7 15h10"/>',
 "drain": '<rect x="4" y="4" width="16" height="16" rx="3"/><path d="M8.5 8v8M12 8v8M15.5 8v8"/>',
 "arrow": '<path d="M5 12h14M12 5l7 7-7 7"/>',
 "chev": '<path d="m6 9 6 6 6-6"/>',
 "plus": '<path d="M12 5v14M5 12h14"/>',
 "alert": '<path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3"/><path d="M12 9v4M12 17h.01"/>',
 "pin": '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/>',
 "mail": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/>',
 "zap": '<path d="M13 2 3 14h9l-1 8 10-12h-9l1-8z"/>',
 "menu": '<path d="M4 6h16M4 12h16M4 18h16"/>',
 "help": '<circle cx="12" cy="12" r="10"/><path d="M9.1 9a3 3 0 0 1 5.8 1c0 2-3 3-3 3M12 17h.01"/>',
 "chevlr": '<path d="m9 6-6 6 6 6M15 6l6 6-6 6"/>',
 "truck": '<path d="M10 17h4V5H2v12h3"/><path d="M20 17h2v-3.34a4 4 0 0 0-1.17-2.83L19 9h-5"/><path d="M14 17h1"/><circle cx="7.5" cy="17.5" r="2.5"/><circle cx="17.5" cy="17.5" r="2.5"/>',
}
WA_PATH = '<path d="M17.47 14.38c-.3-.15-1.75-.86-2.02-.96-.27-.1-.47-.15-.67.15-.2.3-.77.96-.94 1.16-.17.2-.35.22-.64.07-.3-.15-1.25-.46-2.38-1.47-.88-.78-1.48-1.75-1.65-2.05-.17-.3-.02-.46.13-.6.13-.14.3-.35.45-.52.15-.18.2-.3.3-.5.1-.2.05-.37-.03-.52-.07-.15-.67-1.61-.92-2.2-.24-.58-.49-.5-.67-.51h-.57c-.2 0-.52.07-.8.37-.27.3-1.04 1.02-1.04 2.48s1.07 2.88 1.21 3.08c.15.2 2.1 3.2 5.08 4.49.71.3 1.26.49 1.7.63.71.22 1.36.19 1.87.12.57-.09 1.75-.72 2-1.41.25-.7.25-1.29.17-1.41-.07-.13-.27-.2-.57-.35zM12.05 21.8a9.87 9.87 0 0 1-5.03-1.38l-.36-.21-3.74.98 1-3.65-.24-.37a9.86 9.86 0 0 1-1.51-5.26c0-5.45 4.44-9.88 9.89-9.88 2.64 0 5.12 1.03 6.99 2.9a9.82 9.82 0 0 1 2.89 6.99c0 5.45-4.43 9.88-9.89 9.88zm8.41-18.3A11.82 11.82 0 0 0 12.05 0C5.5 0 .16 5.34.16 11.89c0 2.1.55 4.14 1.59 5.95L.06 24l6.3-1.65a11.88 11.88 0 0 0 5.68 1.45h.01c6.55 0 11.89-5.34 11.89-11.89 0-3.18-1.24-6.16-3.48-8.41z"/>'

def ico(name, cls=""):
    if name == "wa":
        return f'<svg class="ico ico-fill {cls}" viewBox="0 0 24 24" aria-hidden="true">{WA_PATH}</svg>'
    return f'<svg class="ico {cls}" viewBox="0 0 24 24" aria-hidden="true">{P[name]}</svg>'

LOGO = '''<svg viewBox="0 0 48 48" aria-hidden="true"><rect width="48" height="48" rx="3" fill="#c8470a"/><rect x="3" y="3" width="42" height="42" rx="1" fill="none" stroke="#121518" stroke-width="2"/><path d="M24 8.5c5.8 6.8 9.8 12.2 9.8 17.6a9.8 9.8 0 0 1-19.6 0c0-5.4 4-10.8 9.8-17.6z" fill="#fff"/><path d="M19.2 27.6a4.9 4.9 0 0 0 4.9 4.6" stroke="#c8470a" stroke-width="2.6" fill="none" stroke-linecap="round"/><path d="M9 39.5h30" stroke="#121518" stroke-width="3"/></svg>'''

# ---------------------------------------------------------------- URLs
def url(lang, page=""):
    """page: '' pour l'accueil, sinon slug sans extension"""
    base = "/" if lang == "fr" else "/nl/"
    return base + page

def abs_url(lang, page=""):
    return SITE_URL + url(lang, page)

def svc_by_id(i):
    return next(s for s in SERVICES if s["id"] == i)

# ---------------------------------------------------------------- blocs communs
def btn_call(L, cls="btn-lg", label=None):
    return f'<a class="btn btn-call {cls}" href="tel:{PHONE_TEL}">{ico("phone")}<span>{label or UI[L]["call_now"]}</span></a>'

def btn_wa(L, cls="btn-lg", href="#devis", label=None):
    return f'<a class="btn btn-wa {cls}" href="{href}">{ico("wa")}<span>{label or UI[L]["wa_quote"]}</span></a>'

def header(L, alt_url, current=""):
    u = UI[L]
    items = "".join(
        f'<a href="{url(L, s["slug"][L])}"><span class="tile tile-blue">{ico(s["icon"])}</span><span>{e(s[L]["name"])}<small>{(u["from"]+" "+str(s["price"])+" €") if s["price"] else u["on_quote"]}</small></span></a>'
        for s in SERVICES)
    lang_sw = (f'<span>FR</span><a href="{alt_url}" hreflang="nl" lang="nl">NL</a>' if L == "fr"
               else f'<a href="{alt_url}" hreflang="fr" lang="fr">FR</a><span>NL</span>')
    def cur(k): return ' aria-current="page"' if current == k else ""
    return f'''<a class="skip" href="#main">{"Aller au contenu" if L=="fr" else "Naar de inhoud"}</a>
<div class="topbar"><div class="wrap">
 <div class="live"><span class="pulse" aria-hidden="true"></span><span class="hide-sm">{e(u["top"])}</span><span class="show-sm">{"Disponible 24h/24 – 7j/7" if L=="fr" else "Beschikbaar 24/7"}</span><b class="hide-sm">· {PHONE_DISPLAY}</b></div>
 <nav class="lang" aria-label="Langue / Taal">{lang_sw}</nav>
</div></div>
<header class="header"><div class="wrap">
 <a class="brand" href="{url(L)}" aria-label="{BRAND} – {u["home"]}">{LOGO}<span><span class="brand-name">ABS DÉBOUCHAGE</span><span class="brand-sub">{e(u["brand_sub"])}</span></span></a>
 <nav class="nav" id="nav" aria-label="Navigation">
  <div class="dd"><button type="button" aria-expanded="false" aria-haspopup="true">{u["nav_services"]} {ico("chev")}</button><div class="dd-menu">{items}</div></div>
  <a href="{url(L)}#tarifs">{u["nav_prices"]}</a>
  <a href="{url(L)}#zones">{u["nav_zones"]}</a>
  <a href="{url(L, u["about_slug"])}"{cur("about")}>{u["nav_about"]}</a>
  <a href="{url(L, u["contact_slug"])}"{cur("contact")}>{u["nav_contact"]}</a>
 </nav>
 <a class="btn btn-call head-call" href="tel:{PHONE_TEL}" aria-label="{u["call"]} {PHONE_DISPLAY}">{ico("phone")}<span>{PHONE_DISPLAY}</span></a>
 <button class="burger" type="button" aria-label="{u["menu"]}" aria-controls="nav" aria-expanded="false">{ico("menu")}</button>
</div></header>'''

def footer(L):
    u = UI[L]
    svc_links = "".join(f'<li><a href="{url(L, s["slug"][L])}">{e(s[L]["name"])}</a></li>' for s in SERVICES[:6])
    svc_links2 = "".join(f'<li><a href="{url(L, s["slug"][L])}">{e(s[L]["name"])}</a></li>' for s in SERVICES[6:])
    return f'''<footer class="footer"><div class="wrap">
 <div class="footer-grid">
  <div>
   <a class="brand" href="{url(L)}">{LOGO}<span><span class="brand-name">ABS DÉBOUCHAGE</span><span class="brand-sub">{e(u["brand_sub"])}</span></span></a>
   <p>{e(u["foot_about"])}</p>
   <a class="phone" href="tel:{PHONE_TEL}">{ico("phone")}{PHONE_DISPLAY}</a>
  </div>
  <div><h4>{u["foot_services"]}</h4><ul>{svc_links}</ul></div>
  <div><h4>&nbsp;</h4><ul>{svc_links2}<li><a href="{url(L, u["about_slug"])}">{u["nav_about"]}</a></li><li><a href="{url(L, u["contact_slug"])}">{u["nav_contact"]}</a></li></ul></div>
  <div><h4>{u["foot_info"]}</h4><ul>
   <li>{u["foot_hours"]}</li>
   <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
   <li>{u["vat"]} : {VAT}</li>
   <li>{u["insured"]}</li>
  </ul></div>
 </div>
 <div class="legal"><span>© {datetime.date.today().year} {BRAND} · {u["rights"]} · {TX[L]["photo_credit"]}</span><a href="{url(L, u["privacy_slug"])}">{u["privacy"]}</a></div>
</div></footer>
<div class="mbar">{btn_call(L, "", u["call"])}{btn_wa(L, "", "#devis", "WhatsApp")}</div>'''

def quote_form(L, preselect=None, compact=False):
    u = UI[L]
    wa = dict(u["wa"]); wa["num"] = WHATSAPP
    choices = [s for s in SERVICES if s["id"] in ("wc", "evier", "douche", "baignoire", "lavabo", "egout", "siphon")]
    if preselect and preselect not in [c["id"] for c in choices]:
        choices = [svc_by_id(preselect)] + choices[:6]
    opts = "".join(
        f'<label class="opt"><input type="radio" name="prob" value="{c["id"]}" data-label="{e(c[L]["name"])}"{" checked" if c["id"]==preselect else ""}><span>{ico(c["icon"])}{e(c[L]["name"])}</span></label>'
        for c in choices)
    opts += f'<label class="opt"><input type="radio" name="prob" value="autre" data-label="{u["other_pb"]}"><span>{ico("help")}{u["other_pb"]}</span></label>'
    urg = "".join(
        f'<label class="opt"><input type="radio" name="urg" value="{k}"{" checked" if k=="now" else ""}><span>{ico(i)}{u["u"][k]}</span></label>'
        for k, i in (("now", "zap"), ("today", "clock"), ("plan", "file")))
    return f'''<form class="qf reveal" data-wa='{e(json.dumps(wa, ensure_ascii=False), quote=True)}' novalidate>
 <fieldset><legend><span>1</span>{u["f_prob"]}</legend><div class="opts">{opts}</div></fieldset>
 <fieldset><legend><span>2</span>{u["f_urg"]}</legend><div class="opts opts-row">{urg}</div></fieldset>
 <div class="grid2">
  <div><label class="lbl" for="where-{L}{preselect or ''}"><span>3</span>{u["f_where"]}</label><input type="text" id="where-{L}{preselect or ''}" name="where" autocomplete="address-level2" placeholder="{e(u["ph_where"])}"></div>
  <div><label class="lbl" for="name-{L}{preselect or ''}">{u["f_name"]}</label><input type="text" id="name-{L}{preselect or ''}" name="name" autocomplete="given-name" placeholder="{e(u["ph_name"])}"></div>
 </div>
 <label class="lbl" for="det-{L}{preselect or ''}"><span>4</span>{u["f_desc"]}</label>
 <textarea id="det-{L}{preselect or ''}" name="det" placeholder="{e(u["ph_desc"])}"></textarea>
 <p class="err" role="alert">{ico("alert")}{u["err"]}</p>
 <button class="btn btn-wa btn-lg btn-block" type="submit">{ico("wa")}<span>{u["send"]}</span></button>
 <p class="note">{u["note"]}</p>
</form>'''

def faq_html(items):
    return '<div class="faq">' + "".join(
        f'<details class="reveal"><summary>{e(q)}{ico("plus")}</summary><p>{e(a)}</p></details>' for q, a in items) + '</div>'

def faq_schema(items):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}

def business_schema(L):
    return {
        "@context": "https://schema.org", "@type": "Plumber", "@id": SITE_URL + "/#business",
        "name": BRAND, "url": SITE_URL + "/", "telephone": PHONE_TEL, "email": EMAIL,
        "vatID": VAT_RAW, "image": SITE_URL + "/assets/og.png", "logo": SITE_URL + "/assets/logo.png",
        "priceRange": "€€", "currenciesAccepted": "EUR",
        "address": {"@type": "PostalAddress", "addressLocality": "Bruxelles" if L=="fr" else "Brussel", "addressRegion": "Bruxelles-Capitale", "addressCountry": "BE"},
        "geo": {"@type": "GeoCoordinates", "latitude": 50.8466, "longitude": 4.3528},
        "openingHoursSpecification": [{"@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"], "opens": "00:00", "closes": "23:59"}],
        "areaServed": [{"@type": "City", "name": c[0] if L=="fr" else c[1]} for c in COMMUNES],
        "knowsLanguage": ["fr", "nl"],
    }

def crumbs_schema(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i+1, "name": n, "item": u} for i, (n, u) in enumerate(items)]}

def layout(L, page, title, desc, body, alt_page, schemas=(), current="", noindex=False):
    other = UI[L]["other"]
    canon = abs_url(L, page)
    alt = abs_url(other, alt_page)
    fr_url = canon if L == "fr" else alt
    nl_url = canon if L == "nl" else alt
    ld = "".join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in schemas)
    robots = '<meta name="robots" content="noindex">' if noindex else '<meta name="robots" content="index, follow, max-image-preview:large">'
    return f'''<!doctype html>
<html lang="{L}-BE">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
{robots}
<link rel="canonical" href="{canon}">
<link rel="alternate" hreflang="fr-BE" href="{fr_url}">
<link rel="alternate" hreflang="nl-BE" href="{nl_url}">
<link rel="alternate" hreflang="x-default" href="{fr_url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:locale" content="{"fr_BE" if L=="fr" else "nl_BE"}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{SITE_URL}/assets/og{"" if L=="fr" else "-nl"}.png">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#f2efe8">
<meta name="format-detection" content="telephone=no">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700;800&family=Barlow:wght@400;500;600;700&display=swap">
<link rel="stylesheet" href="/assets/styles.css?v={VERSION}">
{ld}
</head>
<body>
{header(L, url(other, alt_page), current)}
<div class="pipe-progress" aria-hidden="true"><span class="cap t"></span><span class="tube"><span class="water"></span></span><span class="cap b"></span></div>
<div class="mpipe" aria-hidden="true"><i></i></div>
<main id="main">
{body}
</main>
{footer(L)}
<script src="/assets/app.js?v={VERSION}" defer></script>
</body>
</html>'''


# ---------------------------------------------------------------- photos (Unsplash, licence libre)
PHOTOS = {
 "toilet": ("photo-1676210134050-6f12c6898395", {"fr": "Technicien en gants rouges intervenant sur un WC", "nl": "Technieker met rode handschoenen aan een toilet"}),
 "cabinet": ("photo-1676210133055-eab6ef033ce3", {"fr": "Intervention sur une canalisation sous un évier", "nl": "Werk aan een afvoer onder een gootsteen"}),
 "wall": ("photo-1676210134188-4c05dd172f89", {"fr": "Technicien travaillant sur une canalisation", "nl": "Technieker aan het werk aan een leiding"}),
 "sinkdrain": ("photo-1654440122140-f1fc995ddb34", {"fr": "Bonde d'évier en métal en gros plan", "nl": "Metalen afvoerplug van dichtbij"}),
 "floordrain": ("photo-1745265796934-c34e78554872", {"fr": "Siphon de sol métallique sur béton mouillé", "nl": "Metalen vloerputje op nat beton"}),
 "manhole": ("photo-1779518083245-bb0397ac17f9", {"fr": "Intervention sur une plaque d'égout", "nl": "Werk aan een rioolputdeksel"}),
 "tunnel": ("photo-1608094920051-d3a31d5db8db", {"fr": "Intérieur d'une conduite, comme vu par la caméra", "nl": "Binnenkant van een leiding, zoals de camera ze ziet"}),
 "tools": ("photo-1771122453274-d3270e73cf94", {"fr": "Sac à outils de plombier", "nl": "Gereedschapstas van een loodgieter"}),
}
SVC_PHOTO = {"wc": "toilet", "sanibroyeur": "toilet", "evier": "cabinet", "lavabo": "sinkdrain", "douche": "floordrain",
             "baignoire": "sinkdrain", "cuisine": "cabinet", "egout": "manhole", "siphon": "floordrain", "camera": "tunnel"}

def photo_url(key, w=1200):
    return f"https://images.unsplash.com/{PHOTOS[key][0]}?auto=format&fit=crop&w={w}&q=70"

def img(key, L, cls="", eager=False, sizes="(max-width: 960px) 100vw, 50vw"):
    src = ", ".join(f"{photo_url(key, w)} {w}w" for w in (600, 900, 1300, 1800))
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    return f'<img class="{cls}" src="{photo_url(key, 1300)}" srcset="{src}" sizes="{sizes}" alt="{e(PHOTOS[key][1][L])}" {load} decoding="async">'

# ---------------------------------------------------------------- textes de mise en page
TX = {
 "fr": {
  "eyebrow": "Débouchage d'urgence · Bruxelles",
  "h1": "Bouché&nbsp;?<br><em>On arrive en 30&nbsp;min.</em>",
  "stamp": ("24/7", "30 min"),
  "ticker": ["Débouchage WC", "Évier", "Douche", "Égout", "Caméra HD", "24h/24 – 7j/7", "Devis gratuit", "Sur place en 30 min"],
  "story_tag": "Comment on débouche", "story_title": "Du bouchon à l'écoulement, en 4 étapes",
  "story_lead": "Descendez : voici ce qui se passe dans votre canalisation pendant notre intervention.",
  "story": [["On localise le bouchon", "La caméra descend dans le tuyau et nous montre exactement où ça bloque, et pourquoi. Pas besoin de casser pour chercher."],
            ["Le furet casse le bouchon", "Un furet électrique rotatif avance jusqu'au bouchon et le découpe, sans abîmer le tuyau ni la faïence."],
            ["La haute pression nettoie", "Un jet d'eau jusqu'à 400 bars décolle la graisse, le calcaire et les racines sur toute la paroi."],
            ["Ça coule. On vérifie.", "Test d'écoulement à plein débit, nettoyage de la zone, facture remise sur place."]],
  "story_states": ["Diagnostic caméra", "Furet en action", "Hydrocurage 400 bars", "Écoulement OK"],
  "story_hud": ("Vue en coupe", "Distance"),
  "ba_tag": "Vue caméra", "ba_title": "Avant / après un hydrocurage",
  "ba_lead": "Faites glisser pour comparer l'intérieur d'une canalisation encrassée et la même après notre passage.",
  "ba_before": "Avant", "ba_after": "Après",
  "ba_points": ["Graisse, calcaire, racines : un bouchon se forme pendant des années.", "Le furet ouvre le passage, la haute pression nettoie toute la paroi.", "Résultat : un tuyau propre, qui ne se rebouche pas la semaine suivante."],
  "ba_note": "Illustration — vue caméra simulée.", "ba_aria": "Comparer avant et après",
  "why_tag": "Nos engagements", "why_title": "Pourquoi on nous appelle", "why_big": ["30'", "0 €", "400", "TVA"],
  "photo_credit": "Photos : Unsplash",
  "zones_more": "Votre commune n'est pas dans la liste ? Appelez, on vous dit tout de suite si on peut venir.",
 },
 "nl": {
  "eyebrow": "Spoedontstopping · Brussel",
  "h1": "Verstopt?<br><em>Binnen 30&nbsp;min bij je.</em>",
  "stamp": ("24/7", "30 min"),
  "ticker": ["Ontstopping wc", "Gootsteen", "Douche", "Riool", "HD-camera", "24/7", "Gratis offerte", "Binnen 30 min ter plaatse"],
  "story_tag": "Hoe we ontstoppen", "story_title": "Van verstopping tot vrije afvoer, in 4 stappen",
  "story_lead": "Scroll naar beneden: zo gaat het eraan toe in je leiding tijdens onze interventie.",
  "story": [["We lokaliseren de verstopping", "De camera gaat in de leiding en toont ons precies waar het vastzit, en waarom. Geen breekwerk om te zoeken."],
            ["De veer breekt de prop", "Een elektrische draaiende veer gaat tot aan de verstopping en snijdt ze door, zonder de leiding te beschadigen."],
            ["Hogedruk reinigt", "Een waterstraal tot 400 bar verwijdert vet, kalk en wortels over de hele wand."],
            ["Het loopt. We controleren.", "Doorlooptest op vol debiet, opkuis van de werkzone, factuur ter plaatse."]],
  "story_states": ["Camera-diagnose", "Veer aan het werk", "Hogedruk 400 bar", "Afvoer OK"],
  "story_hud": ("Doorsnede", "Afstand"),
  "ba_tag": "Camerabeeld", "ba_title": "Voor / na een hogedrukreiniging",
  "ba_lead": "Schuif om de binnenkant van een vervuilde leiding te vergelijken met dezelfde leiding na onze interventie.",
  "ba_before": "Voor", "ba_after": "Na",
  "ba_points": ["Vet, kalk, wortels: een verstopping groeit jarenlang.", "De veer maakt de doorgang vrij, hogedruk reinigt de hele wand.", "Resultaat: een propere leiding die de week erna niet opnieuw verstopt."],
  "ba_note": "Illustratie — gesimuleerd camerabeeld.", "ba_aria": "Voor en na vergelijken",
  "why_tag": "Onze engagementen", "why_title": "Waarom men ons belt", "why_big": ["30'", "0 €", "400", "Btw"],
  "photo_credit": "Foto's: Unsplash",
  "zones_more": "Je gemeente staat er niet bij? Bel ons, we zeggen je meteen of we kunnen komen.",
 }
}

def shead(no, tag, title, lead=None):
    return f'''<div class="shead reveal"><span class="no" aria-hidden="true">{no}</span><div><span class="tag">{tag}</span><h2>{title}</h2></div>{f"<p>{lead}</p>" if lead else ""}</div>'''

def quote_section(L, preselect=None, cls="", no="05"):
    u = UI[L]
    steps = "".join(f'<li><b>{i+1}</b><span>{e(t)}</span></li>' for i, t in enumerate(u["q_steps"]))
    return f'''<section class="section {cls}" id="devis"><div class="wrap">
 {shead(no, u["q_kick"], u["q_title"])}
 <div class="quote">
 <div class="reveal">
  <p style="font-size:19px">{u["q_lead"]}</p>
  <ol class="quote-steps">{steps}</ol>
  <p class="quote-alt">{ico("phone")}<span>{"Vous préférez parler à quelqu'un ?" if L=="fr" else "Liever iemand spreken?"}</span> <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></p>
 </div>
 {quote_form(L, preselect)}
 </div>
</div></section>'''

def ticker(L):
    items = "".join(f"<span>{e(t)}</span>" for t in TX[L]["ticker"]) * 3
    return f'<div class="ticker" aria-hidden="true"><div class="ticker-track">{items}</div></div>'

def stamp(L):
    a, b = TX[L]["stamp"]
    return f'<div class="stamp" aria-hidden="true"><span class="ring"></span><div><b>{a}</b><span>{b}</span></div></div>'

def final_cta(L):
    u = UI[L]
    return f'''<section class="section final"><div class="wrap">
 <div class="reveal"><h2>{u["fin_title"]}</h2><p>{u["fin_lead"]}</p><a class="big" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></div>
 <div class="cta-col reveal" data-d="1">{btn_wa(L, "btn-lg")}<a class="btn btn-dark btn-lg" href="{url(L, u["contact_slug"])}">{u["nav_contact"]}</a></div>
</div></section>'''

def services_list(L, exclude=None):
    u = UI[L]; rows = []; n = 0
    for s in SERVICES:
        if s["id"] == exclude: continue
        n += 1
        price = f'{u["from"]} {s["price"]} €' if s["price"] else u["on_quote"]
        ph = photo_url(SVC_PHOTO[s["id"]], 500)
        rows.append(f'''<li class="svc-row reveal">
 <span class="n">{n:02d}</span>
 <h3><a href="{url(L, s["slug"][L])}">{e(s[L]["name"])}</a></h3>
 <p>{e(s[L]["card"])}</p>
 <span class="pr">{price}</span>
 <span class="go">{ico("arrow")}</span>
 <span class="thumb" style="background-image:url('{ph}')" aria-hidden="true"></span>
</li>''')
    return '<ul class="svc-list">' + "".join(rows) + '</ul>'

def story_svg():
    return '''<svg class="story-svg" viewBox="0 0 600 400" role="img" aria-hidden="true">
 <rect width="600" height="400" fill="#0b1a2a"/>
 <g stroke="#1f3a57" stroke-width="1">''' + "".join(f'<path d="M{x} 0V400"/>' for x in range(0, 601, 40)) + "".join(f'<path d="M0 {y}H600"/>' for y in range(0, 401, 40)) + '''</g>
 <g font-family="ui-monospace,Menlo,monospace" font-size="11" fill="#6f87a3">''' + "".join(f'<text x="{x+4}" y="118">{x/600*3.4:.1f} m</text><path d="M{x} 122v10" stroke="#6f87a3"/>' for x in range(0, 600, 120)) + '''</g>
 <rect x="0" y="140" width="600" height="120" fill="#24425f"/>
 <rect x="0" y="152" width="600" height="96" fill="#0f2338"/>
 <rect x="130" y="132" width="26" height="136" fill="#2f5274"/><rect x="450" y="132" width="26" height="136" fill="#2f5274"/>
 <rect id="back" x="0" y="176" width="345" height="70" fill="#2f7fd1" opacity=".8"/>
 <g id="flow" opacity="0"><rect x="0" y="228" width="600" height="18" fill="#2f7fd1"/><path class="flow" d="M0 236H600" stroke="#bfe0ff" stroke-width="3" opacity=".7"/></g>
 <g id="clog">
  <path d="M352 158c18-10 44-6 58 6 14 12 20 30 16 50s-12 32-30 36-40 0-50-14-14-30-10-46 0-24 16-32z" fill="#6b4a2b"/>
  <circle cx="370" cy="190" r="9" fill="#4d331d"/><circle cx="395" cy="215" r="12" fill="#4d331d"/><circle cx="360" cy="228" r="6" fill="#8a6a3e"/><circle cx="405" cy="180" r="5" fill="#8a6a3e"/>
  <path d="M340 170c10 8 20 4 30 14M400 240c-6-10-18-8-24-18M410 170c-8 12-2 22-12 30" stroke="#a88a5c" stroke-width="2" fill="none"/>
 </g>
 <g id="jet" opacity="0" stroke="#bfe0ff" stroke-width="3" stroke-linecap="round"><path d="M300 200h34M300 186l32-10M300 214l32 10M300 176l26-20M300 224l26 20"/></g>
 <line id="cable" x1="0" y1="200" x2="0" y2="200" stroke="#d9d3c4" stroke-width="5" stroke-dasharray="3 5" opacity="0"/>
 <g id="tool" opacity="0"><g class="spin"><circle cx="0" cy="200" r="15" fill="#c8470a"/><path d="M-15 200h30M0 185v30" stroke="#121518" stroke-width="4"/></g></g>
 <g id="cam">
  <line x1="-600" y1="200" x2="-30" y2="200" stroke="#f2c230" stroke-width="3"/>
  <path id="cone" d="M0 200 L90 168 L90 232 Z" fill="#f6dc6a" opacity="0"/>
  <rect x="-34" y="188" width="34" height="24" rx="3" fill="#f2c230"/><circle cx="0" cy="200" r="8" fill="#fff6c7" stroke="#121518" stroke-width="2"/>
 </g>
 <g id="ok" opacity="0"><circle cx="530" cy="70" r="34" fill="#25d366"/><path d="M514 70l11 11 21-22" stroke="#06301a" stroke-width="6" fill="none" stroke-linecap="round" stroke-linejoin="round"/></g>
</svg>'''

def pipe_view(kind):
    """Vue caméra simulée : 'before' (encrassé) ou 'after' (propre)."""
    if kind == "after":
        return '''<svg viewBox="0 0 400 400" aria-hidden="true" class="after">
 <defs><radialGradient id="pga" cx="50%" cy="48%" r="62%"><stop offset="0" stop-color="#040506"/><stop offset=".22" stop-color="#16191b"/><stop offset=".55" stop-color="#5b6062"/><stop offset=".85" stop-color="#9ea2a1"/><stop offset="1" stop-color="#c4c6c3"/></radialGradient></defs>
 <rect width="400" height="400" fill="url(#pga)"/>
 <g fill="none" stroke="#e6e8e4" stroke-opacity=".22"><circle cx="200" cy="194" r="168"/><circle cx="200" cy="194" r="112"/><circle cx="200" cy="194" r="70" stroke-opacity=".16"/><circle cx="200" cy="194" r="40" stroke-opacity=".1"/></g>
 <ellipse cx="200" cy="350" rx="170" ry="34" fill="#8fb9d6" opacity=".35"/>
 <ellipse cx="200" cy="300" rx="96" ry="18" fill="#8fb9d6" opacity=".22"/>
 <ellipse cx="200" cy="262" rx="52" ry="9" fill="#8fb9d6" opacity=".15"/>
 <ellipse cx="120" cy="90" rx="90" ry="34" fill="#fff" opacity=".10" transform="rotate(-28 120 90)"/>
 <g stroke="#fff" stroke-opacity=".55" stroke-width="1.5"><path d="M200 170v-14M200 218v14M176 194h-14M224 194h14"/></g>
</svg>'''
    return '''<svg viewBox="0 0 400 400" aria-hidden="true" class="before">
 <defs><radialGradient id="pgb" cx="50%" cy="48%" r="62%"><stop offset="0" stop-color="#050403"/><stop offset=".22" stop-color="#1d1610"/><stop offset=".55" stop-color="#4f3e29"/><stop offset=".85" stop-color="#76603f"/><stop offset="1" stop-color="#8e7a58"/></radialGradient></defs>
 <rect width="400" height="400" fill="url(#pgb)"/>
 <g fill="#2e2113" opacity=".95">
  <path d="M30 120c30-20 60 10 80-6s40-30 60-10-10 50-40 54-60 20-80 0-40-20-20-38z"/>
  <path d="M260 60c30 0 60 20 90 50s20 60-10 70-50-20-70-40-40-80-10-80z"/>
  <path d="M20 260c30-10 50 20 80 30s40 50 10 70-70 0-90-30 0-70 0-70z"/>
  <path d="M300 250c40-10 80 20 80 60s-40 60-80 50-50-40-40-70 40-40 40-40z"/>
 </g>
 <g fill="#5d4527"><circle cx="90" cy="130" r="10"/><circle cx="320" cy="110" r="14"/><circle cx="60" cy="300" r="12"/><circle cx="340" cy="300" r="9"/><circle cx="150" cy="70" r="7"/></g>
 <g stroke="#a1814f" stroke-width="3" fill="none" stroke-linecap="round" opacity=".9">
  <path d="M200 20c-4 40 10 60 0 100s-20 50-6 80"/><path d="M196 70c-20 10-30 30-50 34"/><path d="M204 100c18 8 26 26 44 30"/><path d="M198 150c-14 12-16 26-30 34"/>
  <path d="M240 26c-10 30 6 50-6 76"/><path d="M160 30c10 26-6 40 2 66"/>
 </g>
 <path d="M140 160c20-30 90-34 120-6s30 80 0 100-90 24-118-6-22-58-2-88z" fill="#3a2a17"/>
 <g fill="#6b5232"><circle cx="175" cy="190" r="12"/><circle cx="225" cy="220" r="16"/><circle cx="210" cy="175" r="7"/><circle cx="170" cy="235" r="9"/></g>
 <ellipse cx="200" cy="352" rx="168" ry="32" fill="#4f4325" opacity=".75"/>
 <g stroke="#fff" stroke-opacity=".45" stroke-width="1.5"><path d="M200 170v-14M200 218v14M176 194h-14M224 194h14"/></g>
</svg>'''

def before_after(L, no="03", cls="white"):
    t = TX[L]
    pts = "".join(f"<li><b>{i+1:02d}</b><span>{e(p)}</span></li>" for i, p in enumerate(t["ba_points"]))
    return f'''<section class="section {cls}" id="avant-apres"><div class="wrap">
 {shead(no, t["ba_tag"], t["ba_title"], t["ba_lead"])}
 <div class="ba">
  <div class="reveal">
   <div class="ba-view">
    {pipe_view("after")}{pipe_view("before")}
    <span class="ba-tag l">{t["ba_before"]}</span><span class="ba-tag r">{t["ba_after"]}</span>
    <div class="ba-hud mono"><span class="rec">REC · CAM 01</span><span>Ø 110 mm · 3,40 m</span></div>
    <span class="ba-line"></span>
    <input type="range" min="0" max="100" value="55" aria-label="{t["ba_aria"]}">
    <span class="ba-knob">{ico("chevlr")}</span>
   </div>
   <p class="ba-note">{t["ba_note"]}</p>
  </div>
  <div class="reveal" data-d="1">
   <ul class="ba-points">{pts}</ul>
   <div class="cta-row" style="margin-top:30px">{btn_call(L, "btn-lg")}</div>
  </div>
 </div>
</div></section>'''

def story_section(L, no="02"):
    t = TX[L]
    steps = "".join(f'<li><span class="k">0{i+1}</span><h3>{e(a)}</h3><p>{e(b)}</p></li>' for i, (a, b) in enumerate(t["story"]))
    return f'''<section class="section dark story on-dark" data-states='{e(json.dumps(t["story_states"], ensure_ascii=False), quote=True)}'><div class="wrap">
 {shead(no, t["story_tag"], t["story_title"], t["story_lead"])}
 <div class="story-grid">
  <div class="story-stage">
   {story_svg()}
   <div class="story-hud mono"><span>{t["story_hud"][0]} · <b data-state>{t["story_states"][0]}</b></span><span>{t["story_hud"][1]} <b data-dist>0,00 m</b></span></div>
  </div>
  <ol class="story-steps">{steps}</ol>
 </div>
</div></section>'''

def why_section(L, no="04"):
    u = UI[L]; t = TX[L]
    items = "".join(f'<li class="reveal" data-d="{i}"><b>{t["why_big"][i]}</b><div><h3>{e(a)}</h3><p>{e(b)}</p></div></li>' for i, (_, a, b) in enumerate(u["why"]))
    return f'''<section class="section"><div class="wrap">
 {shead(no, t["why_tag"], t["why_title"])}
 <div class="why reveal">
  <div class="why-photo" data-par>{img("wall", L)}</div>
  <ul class="why-list">{items}</ul>
 </div>
</div></section>'''

def prices_section(L, no="06", cls=""):
    u = UI[L]; plans = ""
    for i, (name, price, feats) in enumerate(u["plans"]):
        hot = i == 0
        amount = f'<small>{u["from_long"]}</small><div class="amount">{price}&nbsp;€</div>' if price else f'<small>{u["price_lbl"]}</small><div class="amount q">{u["on_quote"]}</div>'
        fl = "".join(f'<li>{ico("check")}{e(f)}</li>' for f in feats)
        btn = btn_call(L, "btn-block", u["ask_price"]) if hot else f'<a class="btn btn-line btn-block" href="tel:{PHONE_TEL}">{ico("phone")}<span>{u["ask_price"]}</span></a>'
        badge = f'<span class="badge">{u["badge"]}</span>' if hot else ""
        plans += f'<div class="plan{" hot" if hot else ""}">{badge}<h3>{e(name)}</h3>{amount}<ul>{fl}</ul>{btn}</div>'
    return f'''<section class="section {cls}" id="tarifs"><div class="wrap">
 {shead(no, u["p_kick"], u["p_title"], u["p_lead"])}
 <div class="plans reveal">{plans}</div><p class="p-note">{u["p_note"]}</p>
</div></section>'''

def zones_section(L, no="07"):
    u = UI[L]
    communes = "".join(f'<li>{e(c[0] if L=="fr" else c[1])} <small>{c[2]}</small></li>' for c in COMMUNES)
    peri = "".join(f'<li>{e(c[0] if L=="fr" else c[1])}</li>' for c in PERIPHERIE)
    return f'''<section class="section white" id="zones"><div class="wrap">
 {shead(no, u["z_kick"], u["z_title"], u["z_lead"])}
 <div class="zones">
  <ul class="zlist reveal">{communes}</ul>
  <div class="zone-card reveal" data-d="1"><h3>{u["z_peri"]}</h3><ul>{peri}</ul><p style="margin-bottom:20px">{TX[L]["zones_more"]}</p>{btn_call(L, "btn-block", PHONE_DISPLAY)}</div>
 </div>
</div></section>'''

def faq_section(L, items, no="08", title=None):
    u = UI[L]
    return f'''<section class="section" id="faq"><div class="wrap">
 {shead(no, u["f_kick"], title or u["f_title"])}
 {faq_html(items)}
</div></section>'''

def hero(L, h1_html, lead, photo, crumbs=None, extra="", eager=True, cls=""):
    u = UI[L]
    checks = "".join(f'<li>{ico("check")}{e(c)}</li>' for c in u["chk"])
    cr = ""
    if crumbs:
        cr = '<ol class="crumbs">' + "".join((f'<li><a href="{h}">{e(n)}</a></li>' if h else f'<li aria-current="page">{e(n)}</li>') for n, h in crumbs) + '</ol>'
    eyebrow = "" if crumbs else f'<span class="eyebrow">{TX[L]["eyebrow"]}</span>'
    return f'''<section class="hero {cls}"><div class="wrap">
 <div class="reveal">
  {cr}{eyebrow}
  <h1>{h1_html}</h1>
  <p class="lead">{e(lead)}</p>
  {extra}
  <div class="cta-row">{btn_call(L)}{btn_wa(L)}</div>
  <ul class="checks">{checks}</ul>
 </div>
 <div class="hero-photo wipe">
  <div class="ph">{img(photo, L, eager=eager)}</div>
  {stamp(L)}
 </div>
</div></section>'''

# ---------------------------------------------------------------- pages
def page_home(L):
    u = UI[L]; t = TX[L]
    body = hero(L, t["h1"], u["hero_lead"], "toilet") + ticker(L) + f'''
<section class="section white" id="services"><div class="wrap">
 {shead("01", u["s_kick"], u["s_title"], u["s_lead"])}
 {services_list(L)}
</div></section>''' + story_section(L, "02") + before_after(L, "03") + why_section(L, "04") + \
        quote_section(L, cls="white", no="05") + prices_section(L, "06") + zones_section(L, "07") + \
        faq_section(L, u["faq"], "08") + final_cta(L)
    schemas = [business_schema(L), faq_schema(u["faq"]),
               {"@context": "https://schema.org", "@type": "WebSite", "name": BRAND, "url": SITE_URL + "/", "inLanguage": f"{L}-BE"}]
    return layout(L, "", u["home_title"], u["home_desc"], body, "", schemas)

def page_service(L, s):
    u = UI[L]; c = s[L]; other = u["other"]
    price = (f'<div class="sv-price"><b>{u["from"]} {s["price"]}&nbsp;€</b><small>{u["sv_price_free"]}</small></div>' if s["price"]
             else f'<div class="sv-price"><b>{u["on_quote"]}</b><small>{u["sv_price_free"]}</small></div>')
    signs = "".join(f'<li>{ico("alert")}{e(x)}</li>' for x in c["signs"])
    causes = "".join(f'<li>{ico("help")}{e(x)}</li>' for x in c["causes"])
    method = "".join(f'<li class="reveal" data-d="{i}"><h3>{e(a)}</h3><p>{e(b)}</p></li>' for i, (a, b) in enumerate(c["method"]))
    tip = c["tip"].split(" : ", 1)[-1] if c["tip"].startswith("En attendant") else (c["tip"].split(": ", 1)[-1] if c["tip"].startswith("In afwachting") else c["tip"])
    crumbs = [(u["home"], abs_url(L)), (c["name"], abs_url(L, s["slug"][L]))]
    communes = ", ".join(x[0] if L == "fr" else x[1] for x in COMMUNES)
    n = iter(range(1, 20))
    nx = lambda: f"{next(n):02d}"
    body = hero(L, e(c["h1"]), c["intro"], SVC_PHOTO[s["id"]], crumbs=[(u["home"], url(L)), (c["name"], None)], extra=price, cls="sv-hero") + ticker(L) + f'''
<section class="section white"><div class="wrap">
 {shead(nx(), c["name"], "Bouché ? Voici pourquoi." if L=="fr" else "Verstopt? Dit is waarom.")}
 <div class="cols2">
  <div class="box reveal"><h2>{u["sv_signs"]}</h2><ul class="list warn">{signs}</ul></div>
  <div class="box reveal" data-d="1"><h2>{u["sv_causes"]}</h2><ul class="list info">{causes}</ul></div>
 </div>
</div></section>
<section class="section dark on-dark"><div class="wrap">
 {shead(nx(), "Méthode" if L=="fr" else "Werkwijze", u["sv_method"])}
 <ol class="method">{method}</ol>
</div></section>
<section class="section-sm"><div class="wrap">
 <div class="tip reveal">{ico("alert")}<div><h2>{u["sv_tip"]}</h2><p>{e(tip)}</p></div></div>
</div></section>''' + (before_after(L, nx()) if s["id"] in ("camera", "egout", "cuisine") else "") + \
        quote_section(L, s["id"], cls="white", no=nx()) + \
        faq_section(L, c["faq"], nx(), f'{u["sv_faq"]}') + f'''
<section class="section white"><div class="wrap">
 {shead(nx(), u["s_kick"], u["sv_other"], u["sv_zone"] + " : " + e(communes) + ".")}
 {services_list(L, exclude=s["id"])}
</div></section>''' + final_cta(L)
    svc_schema = {"@context": "https://schema.org", "@type": "Service", "name": c["name"], "serviceType": c["name"],
                  "description": c["desc"], "url": abs_url(L, s["slug"][L]), "image": photo_url(SVC_PHOTO[s["id"]], 1200),
                  "provider": {"@id": SITE_URL + "/#business"},
                  "areaServed": {"@type": "City", "name": "Bruxelles" if L == "fr" else "Brussel"},
                  "availableChannel": {"@type": "ServiceChannel", "servicePhone": PHONE_TEL}}
    if s["price"]:
        svc_schema["offers"] = {"@type": "Offer", "priceCurrency": "EUR", "price": s["price"],
                                "priceSpecification": {"@type": "PriceSpecification", "minPrice": s["price"], "priceCurrency": "EUR"}}
    schemas = [business_schema(L), svc_schema, faq_schema(c["faq"]), crumbs_schema(crumbs)]
    return layout(L, s["slug"][L], c["title"], c["desc"], body, s["slug"][other], schemas)

def page_about(L):
    u = UI[L]; a = ABOUT[L]; other = u["other"]
    blocks = "".join(f'<div class="box reveal" data-d="{i}"><h2>{e(t)}</h2><ul class="list">{"".join(f"<li>{ico("check")}{e(x)}</li>" for x in items)}</ul></div>'
                     for i, (t, items) in enumerate(a["blocks"]))
    body = hero(L, e(a["h1"]), a["lead"], "tools", crumbs=[(u["home"], url(L)), (u["nav_about"], None)]) + ticker(L) + f'''
<section class="section white"><div class="wrap">{shead("01", "ABS", a["h1"])}<div class="blocks">{blocks}</div></div></section>''' + \
        story_section(L, "02") + prices_section(L, "03") + final_cta(L)
    crumbs = [(u["home"], abs_url(L)), (u["nav_about"], abs_url(L, u["about_slug"]))]
    return layout(L, u["about_slug"], a["title"], a["desc"], body, UI[other]["about_slug"], [business_schema(L), crumbs_schema(crumbs)], current="about")

def page_contact(L):
    u = UI[L]; other = u["other"]
    title = ("Contact – Débouchage Bruxelles 24h/24 | ABS Débouchage" if L == "fr" else "Contact – Ontstopping Brussel 24/7 | ABS Débouchage")
    desc = (f"Contactez ABS Débouchage 24h/24 : téléphone {PHONE_DISPLAY}, WhatsApp ou e-mail. Technicien sur place en 30 min partout à Bruxelles." if L == "fr"
            else f"Contacteer ABS Débouchage 24/7: telefoon {PHONE_DISPLAY}, WhatsApp of e-mail. Technieker binnen 30 min ter plaatse in heel Brussel.")
    h1 = "Contactez-nous,<br><em>24h/24.</em>" if L == "fr" else "Contacteer ons,<br><em>24/7.</em>"
    lead = ("Le plus rapide : appelez-nous ou envoyez votre demande sur WhatsApp. Un technicien peut être chez vous dans 30 minutes." if L == "fr"
            else "Het snelst: bel ons of stuur je aanvraag via WhatsApp. Een technieker kan binnen 30 minuten bij je zijn.")
    cards = [("phone", u["call"], PHONE_DISPLAY, f"tel:{PHONE_TEL}"), ("wa", "WhatsApp", PHONE_DISPLAY, f"https://wa.me/{WHATSAPP}"),
             ("mail", "E-mail", EMAIL, f"mailto:{EMAIL}"), ("clock", u["foot_hours"], "24/7 · 365", None)]
    ch = "".join((f'<a class="c-card" href="{h}"' + (' target="_blank" rel="noopener"' if h.startswith("http") else "") + '>' if h else '<div class="c-card">') +
                 f'{ico(ic)}<small>{e(l)}</small><b>{e(v)}</b>' + ('</a>' if h else '</div>') for ic, l, v, h in cards)
    body = hero(L, h1, lead, "cabinet", crumbs=[(u["home"], url(L)), (u["nav_contact"], None)]) + f'''
<section class="section-sm white"><div class="wrap"><div class="contact-grid reveal">{ch}</div></div></section>''' + \
        quote_section(L, no="01") + zones_section(L, "02") + final_cta(L)
    crumbs = [(u["home"], abs_url(L)), (u["nav_contact"], abs_url(L, u["contact_slug"]))]
    return layout(L, u["contact_slug"], title, desc, body, UI[other]["contact_slug"], [business_schema(L), crumbs_schema(crumbs)], current="contact")

def page_privacy(L):
    u = UI[L]; other = u["other"]; t, paras = PRIVACY[L]
    body = f'''<section class="section"><div class="wrap"><ol class="crumbs"><li><a href="{url(L)}">{u["home"]}</a></li><li aria-current="page">{e(t)}</li></ol>
 <h1 style="font-size:clamp(46px,6vw,80px);margin-bottom:36px">{e(t)}</h1>
 <div class="prose">{"".join(f"<p>{e(p)}</p>" for p in paras)}<p><small>{"Mise à jour" if L=="fr" else "Bijgewerkt"} : {TODAY}</small></p></div></div></section>'''
    return layout(L, u["privacy_slug"], f"{t} | {BRAND}", t + " – " + BRAND, body, UI[other]["privacy_slug"])

def page_404():
    L = "fr"; u = UI[L]
    body = f'''<section class="section"><div class="wrap">
 <h1 style="font-size:clamp(60px,10vw,140px);margin-bottom:20px">404<br><em style="font-style:normal;color:var(--orange)">{u["notfound"]}</em></h1>
 <p style="font-size:20px;max-width:620px;margin-bottom:30px">{u["notfound_lead"]}</p>
 <div class="cta-row">{btn_call(L)}<a class="btn btn-line btn-lg" href="/">{u["home"]}</a></div>
 <p style="margin-top:24px"><a href="/nl/" style="text-decoration:underline">Nederlands → {UI["nl"]["notfound"]}</a></p>
</div></section>'''
    return layout(L, "404", f'{u["notfound"]} | {BRAND}', u["notfound_lead"], body, "", noindex=True)

def write(rel, content):
    p = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(content)

def build():
    # on garde les images générées (og, favicon) si elles existent
    keep = {}
    for k in ("assets/og.png", "assets/og-nl.png", "assets/logo.png", "apple-touch-icon.png", "favicon.ico", "icon-192.png", "icon-512.png"):
        p = os.path.join(OUT, k)
        if os.path.exists(p):
            keep[k] = open(p, "rb").read()
    if os.path.exists(OUT): shutil.rmtree(OUT)
    os.makedirs(OUT)
    for k, v in keep.items():
        os.makedirs(os.path.dirname(os.path.join(OUT, k)), exist_ok=True)
        open(os.path.join(OUT, k), "wb").write(v)
    os.makedirs(os.path.join(OUT, "assets"), exist_ok=True)
    shutil.copy(os.path.join(ROOT, "assets", "styles.css"), os.path.join(OUT, "assets", "styles.css"))
    shutil.copy(os.path.join(ROOT, "assets", "app.js"), os.path.join(OUT, "assets", "app.js"))

    urls = []  # (fr_page, nl_page, priority)
    for L in ("fr", "nl"):
        pre = "" if L == "fr" else "nl/"
        write(pre + "index.html", page_home(L))
        for s in SERVICES:
            write(pre + s["slug"][L] + ".html", page_service(L, s))
        u = UI[L]
        write(pre + u["about_slug"] + ".html", page_about(L))
        write(pre + u["contact_slug"] + ".html", page_contact(L))
        write(pre + u["privacy_slug"] + ".html", page_privacy(L))
    write("404.html", page_404())

    pairs = [("", "", "1.0")] + [(s["slug"]["fr"], s["slug"]["nl"], "0.9") for s in SERVICES] + \
            [(UI["fr"]["contact_slug"], UI["nl"]["contact_slug"], "0.7"), (UI["fr"]["about_slug"], UI["nl"]["about_slug"], "0.6"),
             (UI["fr"]["privacy_slug"], UI["nl"]["privacy_slug"], "0.2")]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for fr, nl, pr in pairs:
        for L, pg in (("fr", fr), ("nl", nl)):
            sm.append(f'<url><loc>{abs_url(L, pg)}</loc><lastmod>{TODAY}</lastmod><priority>{pr}</priority>'
                      f'<xhtml:link rel="alternate" hreflang="fr-BE" href="{abs_url("fr", fr)}"/>'
                      f'<xhtml:link rel="alternate" hreflang="nl-BE" href="{abs_url("nl", nl)}"/>'
                      f'<xhtml:link rel="alternate" hreflang="x-default" href="{abs_url("fr", fr)}"/></url>')
    sm.append("</urlset>")
    write("sitemap.xml", "\n".join(sm))
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n")
    write("favicon.svg", LOGO.replace('aria-hidden="true"', 'xmlns="http://www.w3.org/2000/svg"'))
    write("site.webmanifest", json.dumps({"name": BRAND, "short_name": "ABS", "start_url": "/", "display": "standalone",
          "background_color": "#0c1d38", "theme_color": "#0c1d38",
          "icons": [{"src": "/icon-192.png", "sizes": "192x192", "type": "image/png"}, {"src": "/icon-512.png", "sizes": "512x512", "type": "image/png"}]}))
    print("OK –", sum(len(f) for _, _, f in os.walk(OUT)), "fichiers dans public/")

if __name__ == "__main__":
    build()
