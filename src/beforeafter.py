# -*- coding: utf-8 -*-
"""Comparateur avant / après (illustrations SVG dans le style du site).
À remplacer par les vraies photos du client dès qu'il les fournit."""
import html, math, random

def _blobs(rnd, n, cx, cy, rmin, rmax, size, colors, opac=(.6, .95)):
    out = []
    for _ in range(n):
        a = rnd.uniform(0, 2 * math.pi); r = rnd.uniform(rmin, rmax)
        x, y = cx + r * math.cos(a), cy + r * math.sin(a) * .92
        s = rnd.uniform(*size); c = rnd.choice(colors); o = rnd.uniform(*opac)
        rx, ry, rot = s, s * rnd.uniform(.55, 1), rnd.uniform(0, 180)
        out.append(f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="{rx:.1f}" ry="{ry:.1f}" transform="rotate({rot:.0f} {x:.1f} {y:.1f})" fill="{c}" opacity="{o:.2f}"/>')
    return "".join(out)

def sink(state):
    """Vue du dessus d'un évier inox, bonde au centre."""
    rnd = random.Random(7)
    base = ('<defs><radialGradient id="ba-steel" cx="45%" cy="40%" r="70%"><stop offset="0" stop-color="#e9eef3"/><stop offset=".55" stop-color="#b9c3cd"/><stop offset="1" stop-color="#7d8995"/></radialGradient>'
            '<radialGradient id="ba-hole" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#0b1b2e"/><stop offset=".75" stop-color="#1b2633"/><stop offset="1" stop-color="#55606b"/></radialGradient>'
            '<radialGradient id="ba-grease" cx="50%" cy="50%" r="50%"><stop offset=".25" stop-color="#8a6a2b" stop-opacity=".75"/><stop offset=".7" stop-color="#a0813f" stop-opacity=".45"/><stop offset="1" stop-color="#a0813f" stop-opacity="0"/></radialGradient></defs>'
            '<rect width="480" height="360" fill="#5f6b77"/><rect width="480" height="360" fill="url(#ba-steel)" opacity=".55"/>'
            '<ellipse cx="240" cy="180" rx="196" ry="166" fill="url(#ba-steel)" stroke="#8f9aa6" stroke-width="6"/>'
            '<ellipse cx="240" cy="180" rx="150" ry="126" fill="none" stroke="#a7b1bb" stroke-width="2" opacity=".6"/>')
    hole = ('<ellipse cx="240" cy="182" rx="62" ry="54" fill="#6b7682"/><ellipse cx="240" cy="182" rx="54" ry="47" fill="none" stroke="#c5ced6" stroke-width="5"/>'
            '<ellipse cx="240" cy="184" rx="42" ry="36" fill="url(#ba-hole)"/>')
    if state == "before":
        dirt = ('<ellipse cx="240" cy="182" rx="170" ry="146" fill="url(#ba-grease)"/>'
                + _blobs(rnd, 90, 240, 182, 60, 150, (4, 16), ["#6f5326", "#8a6a2b", "#5a4420", "#9b7b3c", "#4b3a1c"])
                + _blobs(rnd, 30, 240, 182, 70, 140, (2, 5), ["#2f6b2b", "#d9c7a2", "#3c2c14"]))
        murky = '<ellipse cx="240" cy="186" rx="40" ry="33" fill="#4a3b1f" opacity=".85"/>' + _blobs(rnd, 12, 240, 186, 0, 30, (3, 8), ["#6f5326", "#2f2412"])
        return base + dirt + hole + murky
    shine = ('<path d="M112 120 Q180 64 300 70" fill="none" stroke="#fff" stroke-width="10" stroke-linecap="round" opacity=".55"/>'
             '<path d="M352 252 Q330 300 270 314" fill="none" stroke="#fff" stroke-width="6" stroke-linecap="round" opacity=".35"/>'
             + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" opacity=".85"/>' for x, y, r in ((170, 250, 4), (322, 132, 3), (300, 268, 2.5), (150, 160, 2))))
    return base + shine + hole + '<ellipse cx="226" cy="172" rx="10" ry="6" fill="#fff" opacity=".25"/>'

def pipe(state):
    """Vue dans la canalisation (perspective en anneaux)."""
    rnd = random.Random(11)
    rings = []
    for i in range(9):
        k = 1 - i * .105; rx, ry = 230 * k, 190 * k
        col = ["#4d5864", "#56616d", "#606b77", "#68737f", "#717c88", "#7a8591", "#838e9a", "#8c97a3", "#95a0ac"][i]
        rings.append(f'<ellipse cx="240" cy="182" rx="{rx:.0f}" ry="{ry:.0f}" fill="{col}"/>')
    base = '<rect width="480" height="360" fill="#3d4752"/>' + "".join(rings)
    if state == "before":
        rust = ('<ellipse cx="240" cy="182" rx="232" ry="192" fill="#7a4a22" opacity=".55"/>'
                + _blobs(rnd, 160, 240, 182, 40, 220, (6, 22), ["#6b3f1c", "#8a5426", "#5a3417", "#9b6a3a", "#3f2a16", "#a87a45"], (.55, 1))
                + _blobs(rnd, 50, 240, 182, 30, 120, (3, 9), ["#c2b28a", "#2b1d10", "#b98d55"]))
        hole = ('<ellipse cx="248" cy="176" rx="34" ry="26" fill="#120b06"/>' + _blobs(rnd, 18, 248, 176, 20, 40, (6, 12), ["#5a3417", "#7a4a22"], (.8, 1)))
        return base + rust + hole
    clean = "".join(f'<ellipse cx="240" cy="182" rx="{230*(1-i*.105):.0f}" ry="{190*(1-i*.105):.0f}" fill="none" stroke="#b9c3cd" stroke-width="1.5" opacity=".5"/>' for i in range(9))
    shine = '<path d="M60 150 Q90 40 240 22" fill="none" stroke="#fff" stroke-width="8" stroke-linecap="round" opacity=".3"/>'
    hole = '<ellipse cx="240" cy="182" rx="88" ry="72" fill="#1a232d"/><ellipse cx="240" cy="182" rx="60" ry="49" fill="#0b1b2e"/>'
    water = ('<path d="M40 250 Q240 395 440 250 Q440 300 240 372 Q40 300 40 250Z" fill="#38bdf8" opacity=".45"/>'
             '<path d="M90 272 Q240 360 390 272" fill="none" stroke="#bae6fd" stroke-width="3" opacity=".7"/>')
    return base + clean + shine + hole + water

TX = {
 "fr": {"title": "Avant / après", "lead": "Faites glisser pour voir la différence.", "tabs": ("Évier", "Canalisation"),
        "before": "Avant", "after": "Après", "note": "Illustration d'un résultat type.", "range": "Comparer avant et après",
        "chips": ("Prix annoncé avant", "Aucun travail sans accord", "Facture pour l'assurance")},
 "nl": {"title": "Voor / na", "lead": "Schuif om het verschil te zien.", "tabs": ("Gootsteen", "Leiding"),
        "before": "Voor", "after": "Na", "note": "Illustratie van een typisch resultaat.", "range": "Voor en na vergelijken",
        "chips": ("Prijs vooraf", "Geen werk zonder akkoord", "Factuur voor de verzekering")},
}

def compare_html(L, ico, cta, phone_tel, phone_display, or_txt):
    T = TX[L]; e = html.escape
    def u(svg, tag):
        return svg.replace('id="ba-', f'id="ba{tag}-').replace('url(#ba-', f'url(#ba{tag}-')
    def pane(i, fn):
        return (f'<div class="ba-pane{" on" if i == 0 else ""}" data-ba="{i}">'
                f'<svg class="ba-img ba-after" viewBox="0 0 480 360" aria-hidden="true">{u(fn("after"), f"a{i}")}</svg>'
                f'<svg class="ba-img ba-before" viewBox="0 0 480 360" aria-hidden="true">{u(fn("before"), f"b{i}")}</svg></div>')
    tabs = "".join(f'<button type="button" class="ba-tab" role="tab" aria-selected="{"true" if i == 0 else "false"}" data-tab="{i}">{e(t)}</button>' for i, t in enumerate(T["tabs"]))
    chips = "".join(f'<li>{ico("check")}<span>{e(c)}</span></li>' for c in T["chips"])
    return f'''<div class="ba reveal" data-d="1" data-compare>
 <div class="ba-head"><div><h3>{e(T["title"])}</h3><p>{e(T["lead"])}</p></div><div class="ba-tabs" role="tablist">{tabs}</div></div>
 <div class="ba-stage" style="--x:50%">
  {pane(0, sink)}{pane(1, pipe)}
  <span class="ba-lab l">{e(T["before"])}</span><span class="ba-lab r">{e(T["after"])}</span>
  <span class="ba-handle" aria-hidden="true"><i><svg viewBox="0 0 24 24"><path d="M9 7l-5 5 5 5M15 7l5 5-5 5" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg></i></span>
  <input class="ba-range" type="range" min="0" max="100" value="50" aria-label="{e(T["range"])}">
 </div>
 <p class="ba-note">{e(T["note"])}</p>
 <ul class="ba-chips">{chips}</ul>
 <a class="btn btn-wa btn-lg btn-block" href="#diagnostic">{ico("wa")}<span>{e(cta)}</span></a>
 <p class="peng-or">{e(or_txt)} <a href="tel:{phone_tel}">{phone_display}</a></p>
</div>'''
