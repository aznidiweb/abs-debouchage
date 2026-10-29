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
 "chevr": '<path d="m9 6 6 6-6 6"/>',
 "chevl": '<path d="m15 6-6 6 6 6"/>',
 "truck": '<path d="M10 17h4V5H2v12h3"/><path d="M20 17h2v-3.34a4 4 0 0 0-1.17-2.83L19 9h-5"/><path d="M14 17h1"/><circle cx="7.5" cy="17.5" r="2.5"/><circle cx="17.5" cy="17.5" r="2.5"/>',
}
WA_PATH = '<path d="M17.47 14.38c-.3-.15-1.75-.86-2.02-.96-.27-.1-.47-.15-.67.15-.2.3-.77.96-.94 1.16-.17.2-.35.22-.64.07-.3-.15-1.25-.46-2.38-1.47-.88-.78-1.48-1.75-1.65-2.05-.17-.3-.02-.46.13-.6.13-.14.3-.35.45-.52.15-.18.2-.3.3-.5.1-.2.05-.37-.03-.52-.07-.15-.67-1.61-.92-2.2-.24-.58-.49-.5-.67-.51h-.57c-.2 0-.52.07-.8.37-.27.3-1.04 1.02-1.04 2.48s1.07 2.88 1.21 3.08c.15.2 2.1 3.2 5.08 4.49.71.3 1.26.49 1.7.63.71.22 1.36.19 1.87.12.57-.09 1.75-.72 2-1.41.25-.7.25-1.29.17-1.41-.07-.13-.27-.2-.57-.35zM12.05 21.8a9.87 9.87 0 0 1-5.03-1.38l-.36-.21-3.74.98 1-3.65-.24-.37a9.86 9.86 0 0 1-1.51-5.26c0-5.45 4.44-9.88 9.89-9.88 2.64 0 5.12 1.03 6.99 2.9a9.82 9.82 0 0 1 2.89 6.99c0 5.45-4.43 9.88-9.89 9.88zm8.41-18.3A11.82 11.82 0 0 0 12.05 0C5.5 0 .16 5.34.16 11.89c0 2.1.55 4.14 1.59 5.95L.06 24l6.3-1.65a11.88 11.88 0 0 0 5.68 1.45h.01c6.55 0 11.89-5.34 11.89-11.89 0-3.18-1.24-6.16-3.48-8.41z"/>'

def ico(name, cls=""):
    if name == "wa":
        return f'<svg class="ico ico-fill {cls}" viewBox="0 0 24 24" aria-hidden="true">{WA_PATH}</svg>'
    return f'<svg class="ico {cls}" viewBox="0 0 24 24" aria-hidden="true">{P[name]}</svg>'

LOGO = '''<svg viewBox="0 0 48 48" aria-hidden="true"><rect width="48" height="48" rx="10" fill="#0b2545"/><path d="M24 9.5c5.6 6.6 9.4 11.8 9.4 17a9.4 9.4 0 0 1-18.8 0c0-5.2 3.8-10.4 9.4-17z" fill="#fff"/><path d="M19.6 27.4a4.7 4.7 0 0 0 4.6 4.4" stroke="#0b2545" stroke-width="2.4" fill="none" stroke-linecap="round"/><rect x="14" y="38" width="20" height="3" rx="1.5" fill="#c2410c"/></svg>'''

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
 <a class="brand" href="{url(L)}" aria-label="{BRAND} – {u["home"]}">{LOGO}<span><span class="brand-name">ABS Débouchage</span><span class="brand-sub">{e(u["brand_sub"])}</span></span></a>
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
   <a class="brand" href="{url(L)}">{LOGO}<span><span class="brand-name">ABS Débouchage</span><span class="brand-sub">{e(u["brand_sub"])}</span></span></a>
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
<meta name="theme-color" content="#0b2545">
<meta name="format-detection" content="telephone=no">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Lexend:wght@500;600;700&family=Source+Sans+3:wght@400;600;700&display=swap">
<link rel="stylesheet" href="/assets/styles.css?v={VERSION}">
{ld}
</head>
<body>
{header(L, url(other, alt_page), current)}
<main id="main">
{body}
</main>
{footer(L)}
<script src="/assets/app.js?v={VERSION}" defer></script>
</body>
</html>'''


# ---------------------------------------------------------------- photos (Unsplash, licence libre)
PHOTOS = {
 "toilet": ("photo-1676210134050-6f12c6898395", {"fr": "Technicien intervenant sur un WC", "nl": "Technieker aan het werk aan een toilet"}),
 "cabinet": ("photo-1676210133055-eab6ef033ce3", {"fr": "Intervention sur une canalisation sous un évier", "nl": "Werk aan een afvoer onder een gootsteen"}),
 "wall": ("photo-1676210134188-4c05dd172f89", {"fr": "Technicien travaillant sur une canalisation", "nl": "Technieker aan het werk aan een leiding"}),
 "sinkdrain": ("photo-1654440122140-f1fc995ddb34", {"fr": "Bonde d'évier en métal", "nl": "Metalen afvoerplug"}),
 "floordrain": ("photo-1745265796934-c34e78554872", {"fr": "Siphon de sol métallique", "nl": "Metalen vloerputje"}),
 "manhole": ("photo-1779518083245-bb0397ac17f9", {"fr": "Intervention sur une plaque d'égout", "nl": "Werk aan een rioolputdeksel"}),
 "tunnel": ("photo-1608094920051-d3a31d5db8db", {"fr": "Intérieur d'une conduite", "nl": "Binnenkant van een leiding"}),
 "tools": ("photo-1771122453274-d3270e73cf94", {"fr": "Sac à outils de plombier", "nl": "Gereedschapstas van een loodgieter"}),
}
SVC_PHOTO = {"wc": "toilet", "sanibroyeur": "toilet", "evier": "cabinet", "lavabo": "sinkdrain", "douche": "floordrain",
             "baignoire": "sinkdrain", "cuisine": "cabinet", "egout": "manhole", "siphon": "floordrain", "camera": "tunnel"}

def photo_url(key, w=1200):
    return f"https://images.unsplash.com/{PHOTOS[key][0]}?auto=format&fit=crop&w={w}&q=72"

def img(key, L, eager=False, sizes="(max-width: 960px) 100vw, 560px"):
    src = ", ".join(f"{photo_url(key, w)} {w}w" for w in (480, 800, 1200, 1600))
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    return f'<img src="{photo_url(key, 1200)}" srcset="{src}" sizes="{sizes}" alt="{e(PHOTOS[key][1][L])}" width="1200" height="1200" {load} decoding="async">'

TX = {
 "fr": {"label": "Débouchage d'urgence à Bruxelles",
        "h1": "Canalisation bouchée&nbsp;? <span>Un technicien chez vous en 30&nbsp;minutes.</span>",
        "avail": ("Technicien disponible maintenant", "Délai moyen d'arrivée : 30 min"),
        "facts": [("24h/24 – 7j/7", "Week-ends et jours fériés"), ("30 minutes", "Délai moyen d'arrivée"), ("Dès 80 €", "Prix annoncé avant travaux"), ("Agréé assurances", "Facture avec n° TVA")],
        "why_label": "Nos engagements", "why_title": "Une entreprise sérieuse, joignable à toute heure",
        "how_label": "Comment ça se passe", "how_title": "Trois étapes, sans mauvaise surprise",
        "photo_credit": "Photos : Unsplash"},
 "nl": {"label": "Spoedontstopping in Brussel",
        "h1": "Afvoer verstopt? <span>Een technieker binnen 30&nbsp;minuten bij je.</span>",
        "avail": ("Technieker nu beschikbaar", "Gemiddelde aankomsttijd: 30 min"),
        "facts": [("24/7", "Ook weekends en feestdagen"), ("30 minuten", "Gemiddelde aankomsttijd"), ("Vanaf 80 €", "Prijs vooraf gekend"), ("Erkend door verzekeraars", "Factuur met btw-nummer")],
        "why_label": "Onze engagementen", "why_title": "Een betrouwbaar bedrijf, op elk uur bereikbaar",
        "how_label": "Hoe het werkt", "how_title": "Drie stappen, zonder verrassingen",
        "photo_credit": "Foto's: Unsplash"},
}

def sh(label, title, lead=None, center=False):
    return f'<div class="sh{" center" if center else ""} reveal"><span class="label">{label}</span><h2>{title}</h2>{f"<p>{lead}</p>" if lead else ""}</div>'

# ---------------------------------------------------------------- diagnostic express
def diagnostic(L, pre=None, section=True, cls="soft"):
    U = DIAG_UI[L]; u = UI[L]
    svc = {}
    for s in SERVICES:
        tip = s[L]["tip"]
        for pfx in ("En attendant : ", "En attendant le technicien : ", "In afwachting: "):
            if tip.startswith(pfx): tip = tip[len(pfx):]
        tip = tip[0].upper() + tip[1:]
        svc[s["id"]] = {"name": s[L]["name"], "price": s["price"], "tip": tip, "sits": [[a, (b if L == "fr" else c)] for a, b, c in DIAG[s["id"]]]}
    svc["autre"] = {"name": U["other"], "price": None, "tip": None, "sits": [[a, (b if L == "fr" else c)] for a, b, c in DIAG["autre"]]}
    ui = {k: U[k] for k in ("step", "sev", "price", "price_q", "wait", "wait_generic", "wa")}
    ui["from"] = u["from"]
    ui["chev"] = ico("chevr")
    ui["icons"] = {"urgent": ico("alert"), "today": ico("clock"), "plan": ico("check")}
    data = {"svc": svc, "ui": ui, "num": WHATSAPP, "pre": pre}
    order = ["wc", "evier", "douche", "lavabo", "baignoire", "egout", "siphon", "sanibroyeur", "autre"]
    opts = "".join(
        f'<button type="button" class="d-opt" data-svc="{i}" aria-pressed="false">{ico(svc_by_id(i)["icon"] if i != "autre" else "help")}<span>{e(svc[i]["name"])}</span></button>'
        for i in order)
    uid = f"dg-{L}-{pre or 'home'}"
    widget = f'''<div class="diag reveal" data-d="1" data-diag='{e(json.dumps(data, ensure_ascii=False), quote=True)}'>
 <div class="diag-head"><h3>{U["box"]}</h3><div class="diag-steps" aria-live="polite"><span data-steplabel>{U["step"].replace("{n}", "1")}</span><span class="diag-bar" aria-hidden="true"><i class="on"></i><i></i><i></i></span></div></div>
 <div class="diag-body">
  <div class="diag-panel" data-p="1">
   <p class="diag-q" tabindex="-1">{U["q1"]}</p><p class="diag-hint">{U["h1"]}</p>
   <div class="diag-grid">{opts}</div>
  </div>
  <div class="diag-panel" data-p="2" hidden>
   <p class="diag-q" tabindex="-1">{U["q2"]}</p><p class="diag-hint">{U["h2"]}</p>
   <div class="d-list" data-sits></div>
   <div class="diag-nav"><button type="button" class="d-back" data-back="1">{ico("chevl")}{U["back"]}</button></div>
  </div>
  <div class="diag-panel" data-p="3" hidden>
   <p class="diag-q" tabindex="-1" style="margin-bottom:16px">{U["q3"]}</p>
   <div data-result></div>
   <div class="fields">
    <div class="field"><label for="{uid}-w">{U["where"]}</label><input id="{uid}-w" name="where" type="text" autocomplete="address-level2" placeholder="{e(U["where_ph"])}" aria-describedby="{uid}-err"><p class="err" id="{uid}-err" role="alert">{U["err"]}</p></div>
    <div class="field"><label for="{uid}-n">{U["name"]} <small>{U["opt"]}</small></label><input id="{uid}-n" name="name" type="text" autocomplete="given-name"></div>
   </div>
   <div class="res-actions">
    <button type="button" class="btn btn-wa-solid btn-lg" data-send>{ico("wa")}<span>{U["send"]}</span></button>
    <a class="btn btn-call btn-lg" href="tel:{PHONE_TEL}">{ico("phone")}<span>{U["call"]}</span></a>
   </div>
   <p class="diag-note">{U["note"]}</p>
   <p class="diag-sent" role="status">{U["sent"]}</p>
   <div class="diag-nav"><button type="button" class="d-back" data-back="2">{ico("chevl")}{U["back"]}</button></div>
  </div>
 </div>
 <div class="diag-noscript"><p style="margin-bottom:12px">{U["noscript"]}</p>{btn_call(L, "btn-lg", PHONE_DISPLAY)}</div>
</div>'''
    if not section:
        return widget
    pros = "".join(f'<li>{ico("check")}<span>{e(p)}</span></li>' for p in U["pros"])
    return f'''<section class="section {cls}" id="diagnostic"><div class="wrap diag-wrap">
 <div class="diag-aside reveal">
  <span class="label">{U["label"]}</span>
  <h2>{U["title"]}</h2>
  <p>{U["lead"]}</p>
  <ul>{pros}</ul>
  <p class="alt">{U["alt"]}<br><a href="tel:{PHONE_TEL}">{ico("phone")}{PHONE_DISPLAY}</a></p>
 </div>
 {widget}
</div></section>'''

# ---------------------------------------------------------------- blocs
def hero(L, h1_html, lead, photo, crumbs=None, extra="", label=None):
    u = UI[L]; t = TX[L]
    checks = "".join(f'<li>{ico("check")}{e(c)}</li>' for c in u["chk"])
    cr = ""
    if crumbs:
        cr = '<ol class="crumbs">' + "".join((f'<li><a href="{h}">{e(n)}</a></li>' if h else f'<li aria-current="page">{e(n)}</li>') for n, h in crumbs) + '</ol>'
    lab = "" if crumbs else f'<span class="label">{label or t["label"]}</span>'
    a1, a2 = t["avail"]
    return f'''<section class="hero"><div class="wrap">
 <div>
  {cr}{lab}
  <h1>{h1_html}</h1>
  <p class="lead">{e(lead)}</p>
  {extra}
  <div class="cta-row">{btn_call(L)}{btn_wa(L, "btn-lg", "#diagnostic", DIAG_UI[L]["label"])}</div>
  <ul class="checks">{checks}</ul>
 </div>
 <div class="hero-media">
  <div class="ph">{img(photo, L, eager=True)}</div>
  <div class="avail">{ico("check")}<div><strong>{a1}</strong><span>{a2}</span></div></div>
 </div>
</div></section>'''

def facts(L):
    items = "".join(f"<li><b>{e(a)}</b><span>{e(b)}</span></li>" for a, b in TX[L]["facts"])
    return f'<div class="facts"><div class="wrap"><ul>{items}</ul></div></div>'

def services_grid(L, exclude=None):
    u = UI[L]; cards = []
    for i, s in enumerate(x for x in SERVICES if x["id"] != exclude):
        price = f'{u["from"]} {s["price"]} €' if s["price"] else u["on_quote"]
        cards.append(f'''<article class="svc reveal" data-d="{i%3}">{ico(s["icon"])}
 <h3><a href="{url(L, s["slug"][L])}">{e(s[L]["name"])}</a></h3>
 <p>{e(s[L]["card"])}</p>
 <div class="svc-foot"><b>{price}</b><span class="link">{u["learn"]}{ico("arrow")}</span></div>
</article>''')
    return '<div class="svc-grid">' + "".join(cards) + '</div>'

def how_section(L, cls=""):
    u = UI[L]; t = TX[L]
    steps = "".join(f'<li class="reveal" data-d="{i}"><h3>{e(a)}</h3><p>{e(b)}</p></li>' for i, (a, b) in enumerate(u["how"]))
    return f'<section class="section {cls}"><div class="wrap">{sh(t["how_label"], t["how_title"])}<ol class="steps">{steps}</ol></div></section>'

def why_section(L, photo="wall", cls=""):
    u = UI[L]; t = TX[L]
    items = "".join(f'<li>{ico(ic)}<div><h3>{e(a)}</h3><p>{e(b)}</p></div></li>' for ic, a, b in u["why"])
    return f'''<section class="section {cls}"><div class="wrap why">
 <div class="why-ph reveal">{img(photo, L)}</div>
 <div class="reveal" data-d="1"><span class="label">{t["why_label"]}</span><h2 style="font-size:clamp(28px,3.2vw,38px);font-weight:700;margin-bottom:28px">{t["why_title"]}</h2><ul class="why-list">{items}</ul></div>
</div></section>'''

def prices_section(L, cls=""):
    u = UI[L]; plans = ""
    for i, (name, price, feats) in enumerate(u["plans"]):
        hot = i == 0
        amount = f'<small>{u["from_long"]}</small><div class="amount">{price}&nbsp;€</div>' if price else f'<small>{u["price_lbl"]}</small><div class="amount q">{u["on_quote"]}</div>'
        fl = "".join(f'<li>{ico("check")}<span>{e(f)}</span></li>' for f in feats)
        btn = btn_call(L, "btn-block", u["ask_price"]) if hot else f'<a class="btn btn-ghost btn-block" href="tel:{PHONE_TEL}">{ico("phone")}<span>{u["ask_price"]}</span></a>'
        plans += f'<div class="plan{" hot" if hot else ""} reveal" data-d="{i}"><span class="tag">{u["badge"] if hot else "&nbsp;"}</span><h3>{e(name)}</h3>{amount}<ul>{fl}</ul>{btn}</div>'
    return f'''<section class="section {cls}" id="tarifs"><div class="wrap">
 {sh(u["p_kick"], u["p_title"], u["p_lead"])}
 <div class="plans">{plans}</div><p class="p-note">{u["p_note"]}</p>
</div></section>'''

def zones_section(L, cls=""):
    u = UI[L]
    communes = "".join(f'<li>{e(c[0] if L=="fr" else c[1])} <small>{c[2]}</small></li>' for c in COMMUNES)
    peri = "".join(f'<li>{e(c[0] if L=="fr" else c[1])}</li>' for c in PERIPHERIE)
    more = ("Votre commune n'est pas dans la liste ? Appelez-nous, on vous dit tout de suite si on peut venir." if L == "fr"
            else "Je gemeente staat er niet bij? Bel ons, we zeggen je meteen of we kunnen komen.")
    return f'''<section class="section {cls}" id="zones"><div class="wrap">
 {sh(u["z_kick"], u["z_title"], u["z_lead"])}
 <div class="zones">
  <ul class="zlist reveal">{communes}</ul>
  <div class="zone-box reveal" data-d="1"><h3>{u["z_peri"]}</h3><ul>{peri}</ul><p>{more}</p>{btn_call(L, "btn-block", PHONE_DISPLAY)}</div>
 </div>
</div></section>'''

def faq_html(items):
    return '<div class="faq reveal">' + "".join(f'<details><summary>{e(q)}{ico("chev")}</summary><p>{e(a)}</p></details>' for q, a in items) + '</div>'

def faq_section(L, items, title=None, cls=""):
    u = UI[L]
    return f'<section class="section {cls}" id="faq"><div class="wrap">{sh(u["f_kick"], title or u["f_title"], center=True)}{faq_html(items)}</div></section>'

def final_cta(L):
    u = UI[L]
    return f'''<section class="section-sm navy final on-navy"><div class="wrap">
 <div class="reveal"><h2>{u["fin_title"]}</h2><p>{u["fin_lead"]}</p><a class="phone" href="tel:{PHONE_TEL}">{ico("phone")}{PHONE_DISPLAY}</a></div>
 <div class="cta-col reveal" data-d="1">{btn_call(L, "btn-lg", u["call_now"])}{btn_wa(L, "btn-lg", "#diagnostic", DIAG_UI[L]["label"])}</div>
</div></section>'''

# ---------------------------------------------------------------- pages
def page_home(L):
    u = UI[L]; t = TX[L]
    body = hero(L, t["h1"], u["hero_lead"], "toilet") + facts(L) + diagnostic(L) + f'''
<section class="section" id="services"><div class="wrap">
 {sh(u["s_kick"], u["s_title"], u["s_lead"])}
 {services_grid(L)}
</div></section>''' + how_section(L, "soft") + why_section(L) + prices_section(L, "soft") + zones_section(L) + \
        faq_section(L, u["faq"], cls="soft") + final_cta(L)
    schemas = [business_schema(L), faq_schema(u["faq"]),
               {"@context": "https://schema.org", "@type": "WebSite", "name": BRAND, "url": SITE_URL + "/", "inLanguage": f"{L}-BE"}]
    return layout(L, "", u["home_title"], u["home_desc"], body, "", schemas)

def page_service(L, s):
    u = UI[L]; c = s[L]; other = u["other"]
    price = (f'<p class="price-line"><b>{u["from"]} {s["price"]}&nbsp;€</b><span>{u["sv_price_free"]}</span></p>' if s["price"]
             else f'<p class="price-line"><b>{u["on_quote"]}</b><span>{u["sv_price_free"]}</span></p>')
    signs = "".join(f'<li>{ico("alert")}<span>{e(x)}</span></li>' for x in c["signs"])
    causes = "".join(f'<li>{ico("help")}<span>{e(x)}</span></li>' for x in c["causes"])
    method = "".join(f'<li class="reveal" data-d="{i}"><h3>{e(a)}</h3><p>{e(b)}</p></li>' for i, (a, b) in enumerate(c["method"]))
    tip = c["tip"]
    for pfx in ("En attendant : ", "In afwachting: "):
        if tip.startswith(pfx): tip = tip[len(pfx):]
    tip = tip[0].upper() + tip[1:]
    crumbs = [(u["home"], abs_url(L)), (c["name"], abs_url(L, s["slug"][L]))]
    communes = ", ".join(x[0] if L == "fr" else x[1] for x in COMMUNES)
    body = hero(L, e(c["h1"]), c["intro"], SVC_PHOTO[s["id"]], crumbs=[(u["home"], url(L)), (c["name"], None)], extra=price) + facts(L) + f'''
<section class="section"><div class="wrap">
 <div class="cols2">
  <div class="box reveal"><h2>{u["sv_signs"]}</h2><ul class="list warn">{signs}</ul></div>
  <div class="box reveal" data-d="1"><h2>{u["sv_causes"]}</h2><ul class="list info">{causes}</ul></div>
 </div>
</div></section>
<section class="section soft"><div class="wrap">
 {sh("Méthode" if L=="fr" else "Werkwijze", u["sv_method"])}
 <ol class="method">{method}</ol>
 <div class="tip reveal" style="margin-top:28px">{ico("alert")}<div><h3>{u["sv_tip"]}</h3><p>{e(tip)}</p></div></div>
</div></section>''' + diagnostic(L, pre=s["id"], cls="") + faq_section(L, c["faq"], cls="soft") + f'''
<section class="section"><div class="wrap">
 {sh(u["s_kick"], u["sv_other"], u["sv_zone"] + " : " + e(communes) + ".")}
 {services_grid(L, exclude=s["id"])}
</div></section>''' + final_cta(L)
    svc_schema = {"@context": "https://schema.org", "@type": "Service", "name": c["name"], "serviceType": c["name"],
                  "description": c["desc"], "url": abs_url(L, s["slug"][L]), "image": photo_url(SVC_PHOTO[s["id"]], 1200),
                  "provider": {"@id": SITE_URL + "/#business"},
                  "areaServed": {"@type": "City", "name": "Bruxelles" if L == "fr" else "Brussel"},
                  "availableChannel": {"@type": "ServiceChannel", "servicePhone": PHONE_TEL}}
    if s["price"]:
        svc_schema["offers"] = {"@type": "Offer", "priceCurrency": "EUR", "price": s["price"],
                                "priceSpecification": {"@type": "PriceSpecification", "minPrice": s["price"], "priceCurrency": "EUR"}}
    return layout(L, s["slug"][L], c["title"], c["desc"], body, s["slug"][other],
                  [business_schema(L), svc_schema, faq_schema(c["faq"]), crumbs_schema(crumbs)])

def page_about(L):
    u = UI[L]; a = ABOUT[L]; other = u["other"]
    blocks = "".join(f'<div class="box reveal" data-d="{i}"><h2>{e(t)}</h2><ul class="list ok">{"".join(f"<li>{ico(chr(99)+chr(104)+chr(101)+chr(99)+chr(107))}<span>{e(x)}</span></li>" for x in items)}</ul></div>'
                     for i, (t, items) in enumerate(a["blocks"]))
    body = hero(L, e(a["h1"]), a["lead"], "tools", crumbs=[(u["home"], url(L)), (u["nav_about"], None)]) + facts(L) + \
        f'<section class="section"><div class="wrap"><div class="blocks">{blocks}</div></div></section>' + \
        how_section(L, "soft") + prices_section(L) + final_cta(L)
    crumbs = [(u["home"], abs_url(L)), (u["nav_about"], abs_url(L, u["about_slug"]))]
    return layout(L, u["about_slug"], a["title"], a["desc"], body, UI[other]["about_slug"], [business_schema(L), crumbs_schema(crumbs)], current="about")

def page_contact(L):
    u = UI[L]; other = u["other"]
    title = ("Contact – Débouchage Bruxelles 24h/24 | ABS Débouchage" if L == "fr" else "Contact – Ontstopping Brussel 24/7 | ABS Débouchage")
    desc = (f"Contactez ABS Débouchage 24h/24 : téléphone {PHONE_DISPLAY}, WhatsApp ou e-mail. Technicien sur place en 30 min partout à Bruxelles." if L == "fr"
            else f"Contacteer ABS Débouchage 24/7: telefoon {PHONE_DISPLAY}, WhatsApp of e-mail. Technieker binnen 30 min ter plaatse in heel Brussel.")
    h1 = "Contactez-nous, <span>24h/24.</span>" if L == "fr" else "Contacteer ons, <span>24/7.</span>"
    lead = ("Le plus rapide : appelez-nous ou faites le diagnostic express. Un technicien peut être chez vous dans 30 minutes." if L == "fr"
            else "Het snelst: bel ons of doe de snelle diagnose. Een technieker kan binnen 30 minuten bij je zijn.")
    cards = [("phone", u["call"], PHONE_DISPLAY, f"tel:{PHONE_TEL}"), ("wa", "WhatsApp", PHONE_DISPLAY, f"https://wa.me/{WHATSAPP}"),
             ("mail", "E-mail", EMAIL, f"mailto:{EMAIL}"), ("clock", u["foot_hours"], "24/7 · 365", None)]
    ch = "".join((f'<a class="c-card" href="{h}"' + (' target="_blank" rel="noopener"' if h.startswith("http") else "") + '>' if h else '<div class="c-card">') +
                 f'{ico(ic)}<small>{e(l)}</small><b>{e(v)}</b>' + ('</a>' if h else '</div>') for ic, l, v, h in cards)
    body = hero(L, h1, lead, "cabinet", crumbs=[(u["home"], url(L)), (u["nav_contact"], None)]) + \
        f'<section class="section-sm"><div class="wrap"><div class="contact-grid reveal">{ch}</div></div></section>' + \
        diagnostic(L) + zones_section(L) + final_cta(L)
    crumbs = [(u["home"], abs_url(L)), (u["nav_contact"], abs_url(L, u["contact_slug"]))]
    return layout(L, u["contact_slug"], title, desc, body, UI[other]["contact_slug"], [business_schema(L), crumbs_schema(crumbs)], current="contact")

def page_privacy(L):
    u = UI[L]; other = u["other"]; t, paras = PRIVACY[L]
    body = f'''<section class="section"><div class="wrap"><ol class="crumbs"><li><a href="{url(L)}">{u["home"]}</a></li><li aria-current="page">{e(t)}</li></ol>
 <h1 style="font-size:clamp(32px,4vw,44px);margin-bottom:28px">{e(t)}</h1>
 <div class="prose">{"".join(f"<p>{e(p)}</p>" for p in paras)}<p><small>{"Mise à jour" if L=="fr" else "Bijgewerkt"} : {TODAY}</small></p></div></div></section>'''
    return layout(L, u["privacy_slug"], f"{t} | {BRAND}", t + " – " + BRAND, body, UI[other]["privacy_slug"])

def page_404():
    L = "fr"; u = UI[L]
    body = f'''<section class="section"><div class="wrap">
 <span class="label">Erreur 404</span>
 <h1 style="font-size:clamp(32px,4vw,48px);margin-bottom:16px">{u["notfound"]}</h1>
 <p style="font-size:19px;max-width:620px;margin-bottom:28px">{u["notfound_lead"]}</p>
 <div class="cta-row">{btn_call(L)}<a class="btn btn-ghost btn-lg" href="/">{u["home"]}</a></div>
 <p style="margin-top:24px"><a class="link" href="/nl/">Nederlands – {UI["nl"]["notfound"]}</a></p>
</div></section>'''
    return layout(L, "404", f'{u["notfound"]} | {BRAND}', u["notfound_lead"], body, "", noindex=True)


# ---------------------------------------------------------------- écriture
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
