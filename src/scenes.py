# -*- coding: utf-8 -*-
"""
Scènes animées des pages services (SVG + CSS, aucune librairie).
Une boucle de 12 s découpée en 4 temps ; la légende change à chaque temps.
  A = WC / sanibroyeur      B = évier / lavabo / cuisine
  C = douche / baignoire / siphon de sol      D = égout      E = inspection caméra
Le CSS des scènes est produit par scene_css() et ajouté à styles.css au moment du build.
"""
import html

T = 12  # durée d'une boucle, en secondes

KIND = {"wc": "A", "sanibroyeur": "A", "evier": "B", "lavabo": "B", "cuisine": "B",
        "douche": "C", "baignoire": "C", "siphon": "C", "egout": "D", "camera": "E"}

FIRST = {  # première légende, propre à chaque service
    "wc": ("WC bouché : l'eau ne descend plus", "Wc verstopt: het water zakt niet meer"),
    "sanibroyeur": ("Sanibroyeur bloqué : la cuvette se remplit", "Sanibroyeur geblokkeerd: de pot loopt vol"),
    "evier": ("Évier bouché : l'eau stagne", "Gootsteen verstopt: het water blijft staan"),
    "lavabo": ("Lavabo bouché : l'eau stagne", "Lavabo verstopt: het water blijft staan"),
    "cuisine": ("Évacuation de cuisine bouchée", "Keukenafvoer verstopt"),
    "douche": ("Douche bouchée : l'eau stagne", "Douche verstopt: het water blijft staan"),
    "baignoire": ("Baignoire bouchée : l'eau stagne", "Bad verstopt: het water blijft staan"),
    "siphon": ("Siphon de sol bouché", "Afvoerputje verstopt"),
    "egout": ("Égout bouché : racines et graisses", "Riool verstopt: wortels en vet"),
    "camera": ("Caméra HD dans la canalisation", "HD-camera in de leiding"),
}
STEPS = {
    "A": (("Furet électrique dans le siphon", "Elektrische veer in de sifon"),
          ("Le bouchon cède, l'eau s'évacue", "De prop geeft mee, het water loopt weg"),
          ("Chasse d'eau testée : ça s'écoule", "Spoeling getest: het loopt weer")),
    "B": (("On démonte le siphon", "We demonteren de sifon"),
          ("Bouchon retiré, siphon nettoyé", "Prop verwijderd, sifon gereinigd"),
          ("Remonté sans fuite : ça s'écoule", "Lekvrij teruggeplaatst: het loopt weer")),
    "C": (("Grille ouverte, crochet dans le siphon", "Rooster open, haak in de sifon"),
          ("Cheveux et savon retirés", "Haren en zeep verwijderd"),
          ("L'eau s'écoule à nouveau", "Het water loopt weer weg")),
    "D": (("Hydrocureuse haute pression", "Hogedrukreiniger"),
          ("Racines coupées, dépôts décollés", "Wortels weggesneden, afzetting los"),
          ("Égout propre : ça s'écoule", "Riool proper: het loopt weer")),
    "E": (("Images en direct sur l'écran", "Live beelden op het scherm"),
          ("Défaut localisé au centimètre", "Defect tot op de centimeter gelokaliseerd"),
          ("Rapport vidéo remis", "Videorapport bezorgd")),
}
ARIA = {
    "A": ("Animation : un WC bouché est débouché au furet électrique, puis l'eau s'évacue.",
          "Animatie: een verstopt toilet wordt met een elektrische veer ontstopt, daarna loopt het water weg."),
    "B": ("Animation : le siphon sous l'évier est démonté, le bouchon retiré, puis l'eau s'écoule.",
          "Animatie: de sifon onder de gootsteen wordt gedemonteerd, de prop verwijderd, daarna loopt het water weg."),
    "C": ("Animation : la grille de douche est ouverte, les cheveux retirés au crochet, puis l'eau s'écoule.",
          "Animatie: het douchrooster gaat open, de haren worden met een haak verwijderd, daarna loopt het water weg."),
    "D": ("Animation : une buse haute pression avance dans l'égout et dégage racines et graisses.",
          "Animatie: een hogedrukkop gaat door de riool en verwijdert wortels en vet."),
    "E": ("Animation : une caméra avance dans la canalisation et localise une fissure.",
          "Animatie: een camera gaat door de leiding en lokaliseert een barst."),
}

PORC = "#dfe7f1"; DARK = "#0b1b2e"; PIPE = "#9fb0c4"; WATER = "#38bdf8"; CLOG = "#8a5a2b"; TOOL = "#fbbf24"

def _check(x, y):
    return (f'<g class="sc-ok" transform="translate({x} {y})"><circle r="17" fill="#16a34a"/>'
            f'<path d="M-7 0l5 5 9-10" fill="none" stroke="#fff" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/></g>')

def svg_A():
    return f'''<defs><clipPath id="scA-in"><path d="M126 146H322Q316 200 258 222Q160 214 126 146Z"/></clipPath></defs>
<rect y="300" width="480" height="40" fill="#12263f"/>
<rect x="318" y="40" width="112" height="100" rx="12" fill="{PORC}"/><rect x="396" y="56" width="20" height="8" rx="4" fill="#b6c3d3"/>
<path d="M110 140H340V150Q336 214 280 236L276 300H196L200 252Q118 222 110 150Z" fill="{PORC}"/>
<path d="M126 146H322Q316 200 258 222Q160 214 126 146Z" fill="{DARK}"/>
<g clip-path="url(#scA-in)"><rect class="scA-water" x="118" y="150" width="214" height="90" fill="{WATER}" opacity=".85"/></g>
<rect x="226" y="300" width="20" height="40" fill="#1b3554"/>
<path d="M258 222C246 250 222 238 214 258C206 278 236 280 236 300V340" fill="none" stroke="{DARK}" stroke-width="18" stroke-linecap="round"/>
<path class="scA-still" d="M258 222C246 250 222 238 214 258" fill="none" stroke="{WATER}" stroke-width="11" stroke-linecap="round" opacity=".85"/>
<path class="sc-flow scA-flow" d="M258 222C246 250 222 238 214 258C206 278 236 280 236 300V340" fill="none" stroke="#7dd3fc" stroke-width="5" stroke-linecap="round"/>
<g class="scA-clog"><path d="M205 252c3-9 18-11 22-2 5 7-1 17-10 16-8 2-15-6-12-14z" fill="{CLOG}"/><circle cx="212" cy="257" r="2.4" fill="#5c3a19"/><circle cx="220" cy="252" r="1.8" fill="#a8743f"/></g>
<g class="scA-frag"><circle cx="230" cy="290" r="5" fill="{CLOG}"/><circle cx="240" cy="306" r="3.5" fill="{CLOG}"/></g>
<path class="scA-fur" pathLength="100" d="M108 57C170 57 200 110 222 180C232 205 250 214 252 228C246 246 224 244 216 256" fill="none" stroke="{TOOL}" stroke-width="4" stroke-linecap="round"/>
<g class="scA-mot"><rect x="34" y="38" width="76" height="38" rx="10" fill="#c2410c"/><rect x="44" y="48" width="30" height="6" rx="3" fill="#fb7a35"/><circle cx="96" cy="57" r="6" fill="#7c2d12"/></g>
{_check(196, 108)}'''

def svg_B():
    return f'''<defs><clipPath id="scB-in"><path d="M100 98H280V126Q280 148 258 148H122Q100 148 100 126Z"/></clipPath></defs>
<rect x="440" width="40" height="340" fill="#12263f"/>
<rect x="30" y="84" width="330" height="14" rx="3" fill="#1b3554"/>
<path d="M305 84V50Q305 36 291 36H262" fill="none" stroke="{PIPE}" stroke-width="8" stroke-linecap="round"/>
<path d="M90 98H290V128Q290 158 260 158H120Q90 158 90 128Z" fill="{PORC}"/>
<path d="M100 98H280V126Q280 148 258 148H122Q100 148 100 126Z" fill="{DARK}"/>
<g clip-path="url(#scB-in)"><rect class="scB-water" x="96" y="102" width="190" height="50" fill="{WATER}" opacity=".85"/></g>
<rect x="181" y="156" width="18" height="40" fill="{PIPE}"/><rect x="178" y="186" width="24" height="10" rx="2" fill="#cbd5e1"/>
<path d="M259 214H440" stroke="{PIPE}" stroke-width="18"/><path d="M259 214H440" stroke="{DARK}" stroke-width="9"/>
<path class="scB-bucket" d="M176 292H264L255 336H185Z" fill="#1b3554" stroke="#33557c" stroke-width="2"/>
<g class="scB-u">
 <path d="M190 196V232Q190 262 220 262Q250 262 250 232V214" fill="none" stroke="{PIPE}" stroke-width="18"/>
 <path d="M190 196V232Q190 262 220 262Q250 262 250 232V214" fill="none" stroke="{DARK}" stroke-width="9"/>
 <rect class="scB-nut" x="238" y="206" width="24" height="16" rx="3" fill="#cbd5e1"/>
 <g class="scB-clog"><path d="M211 256c2-7 15-8 18-1 4 6-1 13-9 12-7 1-12-5-9-11z" fill="{CLOG}"/></g>
</g>
<path class="sc-flow scB-flow" d="M190 150V232Q190 262 220 262Q250 262 250 232V214H440" fill="none" stroke="#7dd3fc" stroke-width="4" stroke-linecap="round"/>
{_check(190, 54)}'''

def svg_C():
    hair = "".join(f'<path d="{d}" fill="none" stroke="#c9a27e" stroke-width="2.2" stroke-linecap="round"/>' for d in
                   ("M218 206c6 6-4 12 4 18s-2 12 6 16", "M240 204c-6 8 5 12-2 19s4 12-2 17", "M226 210c8 2 4 10 12 12s2 10 8 12", "M222 230c6-4 12 2 18-2"))
    return f'''<rect x="0" y="0" width="480" height="164" fill="#0d2136"/>
<g fill="#16304d"><rect x="0" y="0" width="480" height="2"/><rect x="0" y="54" width="480" height="2"/><rect x="0" y="108" width="480" height="2"/><rect x="118" width="2" height="164"/><rect x="238" width="2" height="164"/><rect x="358" width="2" height="164"/></g>
<path d="M230 170V236Q230 262 256 262H480" fill="none" stroke="{PIPE}" stroke-width="34"/>
<path d="M230 170V236Q230 262 256 262H480" fill="none" stroke="{DARK}" stroke-width="24"/>
<rect x="0" y="170" width="212" height="34" fill="#1b3554"/><rect x="248" y="170" width="232" height="34" fill="#1b3554"/>
<rect x="0" y="164" width="212" height="6" fill="#2b4a6e"/><rect x="248" y="164" width="232" height="6" fill="#2b4a6e"/>
<g class="scC-hair">{hair}</g>
<ellipse class="scC-pud" cx="230" cy="161" rx="176" ry="7" fill="{WATER}" opacity=".75"/>
<ellipse class="scC-swirl" cx="230" cy="163" rx="22" ry="5" fill="none" stroke="#7dd3fc" stroke-width="2"/>
<g class="scC-grate"><rect x="206" y="157" width="48" height="8" rx="2" fill="#cbd5e1"/><path d="M214 159v4M222 159v4M230 159v4M238 159v4M246 159v4" stroke="#64748b" stroke-width="2"/></g>
<path class="sc-flow scC-flow" d="M230 166V236Q230 262 256 262H480" fill="none" stroke="#7dd3fc" stroke-width="5" stroke-linecap="round"/>
<path class="scC-tool" pathLength="100" d="M330 24Q270 70 240 120L232 168L230 222q-2 8 6 8" fill="none" stroke="{TOOL}" stroke-width="3.5" stroke-linecap="round"/>
{_check(330, 110)}'''

ROOTS = (230, 320, 400); GREASE = (180, 360)
def svg_D():
    roots = "".join(f'<g class="scD-r{i}"><path d="M{x} 163q-6 18 4 30q8 12-2 26M{x+2} 180q10 4 14 16M{x} 196q-12 2-16 14" fill="none" stroke="#8b6b3f" stroke-width="3" stroke-linecap="round"/></g>' for i, x in enumerate(ROOTS))
    grease = "".join(f'<ellipse class="scD-g{i}" cx="{x}" cy="235" rx="30" ry="7" fill="#a3895a"/>' for i, x in enumerate(GREASE))
    return f'''<rect width="480" height="62" fill="#12263f"/><rect y="60" width="480" height="4" fill="#2b4a6e"/>
<rect y="64" width="480" height="276" fill="#0e2033"/>
<g fill="#16304d"><circle cx="160" cy="100" r="3"/><circle cx="300" cy="120" r="2.5"/><circle cx="420" cy="96" r="3"/><circle cx="380" cy="300" r="2.5"/><circle cx="140" cy="290" r="3"/></g>
<g><rect x="16" y="22" width="98" height="38" rx="7" fill="#c2410c"/><rect x="24" y="30" width="40" height="12" rx="3" fill="#fb7a35"/><circle cx="36" cy="60" r="8" fill="#0b1b2e" stroke="#475569" stroke-width="3"/><circle cx="94" cy="60" r="8" fill="#0b1b2e" stroke="#475569" stroke-width="3"/></g>
<rect x="52" y="64" width="46" height="100" fill="{DARK}" stroke="#2b4a6e" stroke-width="3"/>
<rect x="34" y="160" width="460" height="80" rx="6" fill="{DARK}" stroke="{PIPE}" stroke-width="6"/>
{roots}{grease}
<path class="sc-flow scD-flow" d="M40 226H480" fill="none" stroke="#7dd3fc" stroke-width="6" stroke-linecap="round"/>
<rect x="73" y="60" width="4" height="142" fill="{TOOL}"/>
<rect class="scD-hose" x="75" y="198" width="360" height="4" fill="{TOOL}"/>
<g class="scD-noz"><g transform="translate(75 200)">
 <g class="scD-jet" fill="none" stroke="#7dd3fc" stroke-width="3" stroke-linecap="round"><path d="M-2-4l-28-18M-2 4l-28 18M-4 0h-30"/></g>
 <path d="M-6-8h16l8 8-8 8h-16z" fill="#e2e8f0"/></g></g>'''

def svg_E(L):
    m = "Fissure · 4,2 m" if L == "fr" else "Barst · 4,2 m"
    return f'''<rect width="480" height="340" fill="#0e2033"/>
<rect x="-6" y="170" width="492" height="80" fill="{DARK}" stroke="{PIPE}" stroke-width="6"/>
<g fill="#2b4a6e"><rect x="120" y="167" width="6" height="86"/><rect x="240" y="167" width="6" height="86"/><rect x="400" y="167" width="6" height="86"/></g>
<path d="M322 173l6 9-5 6 9 9" fill="none" stroke="#ef4444" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
<g class="scE-mark"><circle cx="328" cy="186" r="10" fill="none" stroke="#ef4444" stroke-width="2.5"/><rect x="286" y="120" width="88" height="24" rx="12" fill="#ef4444"/><text x="330" y="136" text-anchor="middle" font-size="12" font-weight="800" fill="#fff">{m}</text></g>
<rect class="scE-cable" x="0" y="208" width="290" height="4" fill="{TOOL}"/>
<g class="scE-cam"><g transform="translate(20 0)">
 <polygon points="0,200 80,180 80,240 0,220" fill="#fde047" opacity=".16"/>
 <rect x="-34" y="198" width="34" height="24" rx="6" fill="#e2e8f0"/><circle cx="0" cy="210" r="7" fill="#0ea5e9" stroke="#e2e8f0" stroke-width="3"/></g></g>
<g transform="translate(20 18)">
 <rect width="176" height="120" rx="12" fill="{DARK}" stroke="#2b4a6e" stroke-width="2"/>
 <rect x="10" y="10" width="156" height="92" rx="6" fill="#0f172a"/>
 <g class="scE-tun" fill="none" stroke="#475569" stroke-width="2"><circle cx="88" cy="56" r="10"/><circle cx="88" cy="56" r="10"/><circle cx="88" cy="56" r="10"/></g>
 <circle cx="88" cy="56" r="40" fill="none" stroke="#334155" stroke-width="3"/>
 <path class="scE-crk" d="M70 26l8 10-6 7 10 10" fill="none" stroke="#ef4444" stroke-width="3" stroke-linecap="round"/>
 <circle class="scE-rec" cx="22" cy="22" r="4" fill="#ef4444"/><text x="30" y="26" font-size="10" font-weight="800" fill="#cbd5e1">REC</text>
 <rect x="10" y="106" width="60" height="6" rx="3" fill="#1e293b"/></g>'''

def scene(L, sid, ico_pause, ico_play):
    k = KIND[sid]; fr = L == "fr"; ix = 0 if fr else 1
    caps = [FIRST[sid][ix]] + [s[ix] for s in STEPS[k]]
    body = {"A": svg_A, "B": svg_B, "C": svg_C, "D": svg_D}.get(k, lambda: svg_E(L))()
    e = html.escape
    pause = "Mettre l’animation en pause" if fr else "Animatie pauzeren"
    play = "Relancer l’animation" if fr else "Animatie afspelen"
    lab = "Vue en coupe" if fr else "Doorsnede"
    return f'''<figure class="sc-box sc-{k}" data-scene data-pause="{e(pause)}" data-play="{e(play)}">
 <svg class="sc-svg" viewBox="0 0 480 340" role="img" aria-label="{e(ARIA[k][ix])}">{body}</svg>
 <figcaption class="sc-foot"><span class="sc-bar" aria-hidden="true"><i></i></span>
  <span class="sc-cap" aria-hidden="true"><i></i><span>{"</span><span>".join(e(c) for c in caps)}</span></span>
  <span class="sc-lab">{lab}</span>
  <button type="button" class="sc-pause" aria-pressed="false" aria-label="{e(pause)}" data-ico-play="{e(ico_play)}">{ico_pause}</button></figcaption>
</figure>'''

# ------------------------------------------------------------------ CSS
def _kf(name, frames):
    return f"@keyframes {name}{{" + "".join(f"{p}%{{{v}}}" for p, v in frames) + "}"

def _win(name, a, b, fade=2):
    """visible entre a% et b% (opacité)"""
    return _kf(name, [(0, "opacity:0"), (a, "opacity:0"), (a + fade, "opacity:1"), (b - fade, "opacity:1"), (b, "opacity:0"), (100, "opacity:0")])

def _gone(name, t):
    """présent jusqu'à t%, disparaît, revient en fin de boucle"""
    return _kf(name, [(0, "opacity:1"), (t, "opacity:1"), (t + 2, "opacity:0"), (95, "opacity:0"), (100, "opacity:1")])

def scene_css():
    c = []
    a = lambda sel, name, extra="": c.append(f"{sel}{{animation:{name} {T}s infinite{(' ' + extra) if extra else ''}}}")
    # --- A : WC
    c.append(_kf("scA-water", [(0, "transform:none"), (52, "transform:none"), (70, "transform:translateY(46px)"), (93, "transform:translateY(46px)"), (100, "transform:none")])); a(".scA-water", "scA-water", "ease-in-out")
    c.append(_kf("scA-fur", [(0, "stroke-dashoffset:100"), (25, "stroke-dashoffset:100"), (42, "stroke-dashoffset:0"), (52, "stroke-dashoffset:0"), (64, "stroke-dashoffset:100"), (100, "stroke-dashoffset:100")])); a(".scA-fur", "scA-fur", "ease-in-out")
    c.append(_kf("scA-mot", [(0, "transform:none"), (40, "transform:none"), (41, "transform:translate(1px,-1px)"), (42, "transform:translate(-1px,1px)"), (43, "transform:translate(1px,1px)"), (44, "transform:translate(-1px,-1px)"), (45, "transform:translate(1px,0)"), (46, "transform:translate(-1px,1px)"), (47, "transform:translate(1px,-1px)"), (48, "transform:translate(0,1px)"), (49, "transform:none"), (100, "transform:none")])); a(".scA-mot", "scA-mot")
    c.append(_kf("scA-clog", [(0, "transform:none;opacity:1"), (42, "transform:none;opacity:1"), (44, "transform:translate(1px,-1px)"), (46, "transform:translate(-1px,1px)"), (48, "transform:translate(1px,1px);opacity:1"), (54, "transform:translate(10px,30px) scale(.4);opacity:0"), (96, "transform:none;opacity:0"), (100, "transform:none;opacity:1")])); a(".scA-clog", "scA-clog")
    c.append(_kf("scA-frag", [(0, "opacity:0;transform:none"), (50, "opacity:0;transform:none"), (53, "opacity:1"), (64, "opacity:0;transform:translateY(40px)"), (100, "opacity:0")])); a(".scA-frag", "scA-frag")
    c.append(_kf("scA-still", [(0, "opacity:1"), (50, "opacity:1"), (54, "opacity:0"), (95, "opacity:0"), (100, "opacity:1")])); a(".scA-still", "scA-still")
    c.append(_win("scA-flow", 52, 90)); c.append(".scA-flow{animation:scA-flow 12s infinite,scFlow .8s linear infinite}")
    # --- B : évier
    c.append(_kf("scB-water", [(0, "transform:none"), (66, "transform:none"), (80, "transform:translateY(44px)"), (94, "transform:translateY(44px)"), (100, "transform:none")])); a(".scB-water", "scB-water", "ease-in-out")
    c.append(_kf("scB-nut", [(0, "transform:none"), (25, "transform:none"), (27, "transform:scaleX(.3)"), (29, "transform:none"), (31, "transform:scaleX(.3)"), (33, "transform:none"), (56, "transform:none"), (58, "transform:scaleX(.3)"), (60, "transform:none"), (62, "transform:scaleX(.3)"), (64, "transform:none"), (100, "transform:none")])); a(".scB-nut", "scB-nut")
    c.append(_kf("scB-u", [(0, "transform:none"), (34, "transform:none"), (42, "transform:translateY(42px)"), (54, "transform:translateY(42px)"), (62, "transform:none"), (100, "transform:none")])); a(".scB-u", "scB-u", "ease-in-out")
    c.append(_kf("scB-clog", [(0, "transform:none;opacity:1"), (44, "transform:none;opacity:1"), (50, "transform:translateY(24px);opacity:0"), (96, "transform:none;opacity:0"), (100, "transform:none;opacity:1")])); a(".scB-clog", "scB-clog", "ease-in")
    c.append(_win("scB-bucket", 24, 72, 3)); a(".scB-bucket", "scB-bucket")
    c.append(_win("scB-flow", 66, 92)); c.append(".scB-flow{animation:scB-flow 12s infinite,scFlow .8s linear infinite}")
    # --- C : douche
    c.append(_kf("scC-grate", [(0, "transform:none"), (25, "transform:none"), (32, "transform:translate(-50px,-34px) rotate(-24deg)"), (60, "transform:translate(-50px,-34px) rotate(-24deg)"), (67, "transform:none"), (100, "transform:none")])); a(".scC-grate", "scC-grate", "ease-in-out")
    c.append(_kf("scC-tool", [(0, "stroke-dashoffset:100"), (32, "stroke-dashoffset:100"), (44, "stroke-dashoffset:0"), (50, "stroke-dashoffset:0"), (60, "stroke-dashoffset:100"), (100, "stroke-dashoffset:100")])); a(".scC-tool", "scC-tool", "ease-in-out")
    c.append(_kf("scC-hair", [(0, "transform:none;opacity:1"), (50, "transform:none;opacity:1"), (60, "transform:translate(70px,-150px);opacity:0"), (96, "transform:none;opacity:0"), (100, "transform:none;opacity:1")])); a(".scC-hair", "scC-hair", "ease-in")
    c.append(_kf("scC-pud", [(0, "transform:none"), (68, "transform:none"), (86, "transform:scaleX(.04)"), (94, "transform:scaleX(.04)"), (100, "transform:none")])); a(".scC-pud", "scC-pud", "ease-in")
    c.append(_win("scC-swirl", 68, 88)); c.append(".scC-swirl{animation:scC-swirl 12s infinite,scSpin .9s ease-out infinite}")
    c.append(_win("scC-flow", 68, 92)); c.append(".scC-flow{animation:scC-flow 12s infinite,scFlow .8s linear infinite}")
    # --- D : égout (la buse avance de 25 % à 62 %, de x=75 à x=435)
    c.append(_kf("scD-noz", [(0, "transform:none"), (25, "transform:none"), (62, "transform:translateX(360px)"), (74, "transform:translateX(360px)"), (82, "transform:none"), (100, "transform:none")])); a(".scD-noz", "scD-noz", "linear")
    c.append(_kf("scD-hose", [(0, "transform:scaleX(0)"), (25, "transform:scaleX(0)"), (62, "transform:scaleX(1)"), (74, "transform:scaleX(1)"), (82, "transform:scaleX(0)"), (100, "transform:scaleX(0)")])); a(".scD-hose", "scD-hose", "linear")
    c.append(_win("scD-jet", 25, 70)); c.append(".scD-jet{animation:scD-jet 12s infinite,scFlow .4s linear infinite}")
    for i, x in enumerate(ROOTS):
        t = round(25 + 37 * (x - 75) / 360, 1); c.append(_gone(f"scD-r{i}", t)); a(f".scD-r{i}", f"scD-r{i}")
    for i, x in enumerate(GREASE):
        t = round(25 + 37 * (x - 75) / 360, 1); c.append(_gone(f"scD-g{i}", t)); a(f".scD-g{i}", f"scD-g{i}")
    c.append(_win("scD-flow", 70, 94)); c.append(".scD-flow{animation:scD-flow 12s infinite,scFlow .8s linear infinite}")
    # --- E : caméra (avance 6 %→46 %, arrêt sur la fissure, retour 84 %→97 %)
    c.append(_kf("scE-cam", [(0, "transform:none"), (6, "transform:none"), (46, "transform:translateX(270px)"), (84, "transform:translateX(270px)"), (97, "transform:none"), (100, "transform:none")])); a(".scE-cam", "scE-cam", "ease-in-out")
    c.append(_kf("scE-cable", [(0, "transform:scaleX(.07)"), (6, "transform:scaleX(.07)"), (46, "transform:scaleX(1)"), (84, "transform:scaleX(1)"), (97, "transform:scaleX(.07)"), (100, "transform:scaleX(.07)")])); a(".scE-cable", "scE-cable", "ease-in-out")
    c.append(_win("scE-mark", 50, 86)); a(".scE-mark", "scE-mark")
    c.append(_win("scE-crk", 46, 84)); a(".scE-crk", "scE-crk")
    c.append(_kf("scE-tunw", [(0, "opacity:1"), (46, "opacity:1"), (48, "opacity:0"), (84, "opacity:0"), (86, "opacity:1"), (100, "opacity:1")]))
    c.append(".scE-tun{animation:scE-tunw 12s infinite}.scE-tun circle{transform-box:fill-box;transform-origin:center;animation:scTun 1.2s linear infinite}.scE-tun circle:nth-child(2){animation-delay:-.4s}.scE-tun circle:nth-child(3){animation-delay:-.8s}")
    c.append(".scE-rec{animation:scBlink 1s steps(2) infinite}")
    # --- communs
    c.append(_kf("scFlow", [(100, "stroke-dashoffset:-16")]))
    c.append(_kf("scSpin", [(0, "transform:scale(1.6)"), (100, "transform:scale(.3)")]))
    c.append(_kf("scTun", [(0, "transform:scale(.4);opacity:0"), (30, "opacity:1"), (100, "transform:scale(4.6);opacity:0")]))
    c.append(_kf("scBlink", [(0, "opacity:1"), (100, "opacity:.15")]))
    c.append(_win("scOk", 80, 97)); c.append(".sc-ok{animation:scOk 12s infinite}")
    c.append(".sc-flow{stroke-dasharray:6 10}")
    c.append(".scA-fur,.scC-tool{stroke-dasharray:100}")
    c.append(".scB-nut,.scC-pud,.scC-swirl,.scD-hose,.scE-cable{transform-box:fill-box;transform-origin:center}.scD-hose,.scE-cable{transform-origin:left center}")
    c.append(".scC-grate,.scC-hair{transform-box:fill-box;transform-origin:center}")
    # légendes : un temps chacune
    c.append(_kf("scCap", [(0, "opacity:0;transform:translateY(4px)"), (1.5, "opacity:1;transform:none"), (23.5, "opacity:1;transform:none"), (25, "opacity:0;transform:translateY(-4px)"), (100, "opacity:0")]))
    c.append("".join(f".sc-cap span:nth-of-type({i+1}){{animation:scCap {T}s infinite {i*T/4}s both}}" for i in range(4)))
    c.append(_kf("scBar", [(0, "transform:scaleX(0)"), (100, "transform:scaleX(1)")]))
    c.append(f".sc-bar i{{animation:scBar {T}s linear infinite}}")
    c.append(".sc-box.off *,.sc-box.off *::before,.sc-box.paused *,.sc-box.paused *::before{animation-play-state:paused!important}")
    return "\n".join(c)

def scene_mini(L, sid, uid):
    """Scène seule (sans légende ni bouton), pour les cartes services ; ids rendus uniques."""
    k = KIND[sid]
    body = {"A": svg_A, "B": svg_B, "C": svg_C, "D": svg_D}.get(k, lambda: svg_E(L))()
    body = body.replace("scA-in", f"scA-in-{uid}").replace("scB-in", f"scB-in-{uid}")
    return f'<svg class="sc-msvg" viewBox="0 0 480 340" preserveAspectRatio="xMidYMid slice" aria-hidden="true" focusable="false">{body}</svg>'
