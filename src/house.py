# -*- coding: utf-8 -*-
"""Illustration de l'intro : maison en coupe, l'eau circule de chaque appareil jusqu'à l'égout."""
import html

TXT = {"fr": ("Salle de bain", "Cuisine", "Égout", "Illustration : une maison en coupe ; l'eau de la salle de bain et de la cuisine s'écoule jusqu'à l'égout, chaque point est contrôlé."),
       "nl": ("Badkamer", "Keuken", "Riool", "Illustratie: een huis in doorsnede; het water van badkamer en keuken loopt weg naar de riool, elk punt wordt gecontroleerd.")}

PIPE = "#9fb0c4"; DARK = "#0b1b2e"; PORC = "#dfe7f1"

def _pipe(d, cls, delay):
    return (f'<path d="{d}" fill="none" stroke="{PIPE}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<path d="{d}" fill="none" stroke="{DARK}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<path class="hs-w {cls}" style="animation-delay:{delay}s" d="{d}" fill="none" stroke="#38bdf8" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>')

def _ok(x, y, i):
    return (f'<g class="hs-ok" style="--i:{i}" transform="translate({x} {y})"><circle r="9" fill="#16a34a"/>'
            f'<path d="M-4 0l3 3 5-6" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></g>')

def house_svg(L):
    bath, kitchen, sewer, aria = TXT[L]
    e = html.escape
    return f'''<svg class="house" viewBox="0 0 400 250" role="img" aria-label="{e(aria)}">
<rect width="400" height="250" fill="{DARK}"/>
<g fill="#16304d"><circle cx="320" cy="34" r="1.5"/><circle cx="350" cy="58" r="1"/><circle cx="300" cy="80" r="1.2"/><circle cx="372" cy="22" r="1.4"/></g>
<rect y="196" width="400" height="54" fill="#0e2033"/><rect y="194" width="400" height="3" fill="#2b4a6e"/>
<polygon points="28,74 155,16 282,74" fill="#1b3554"/><rect x="40" y="72" width="230" height="124" fill="#12263f" stroke="#2b4a6e" stroke-width="2"/>
<rect x="40" y="132" width="230" height="3" fill="#2b4a6e"/>
<text x="52" y="90" class="hs-l">{e(bath)}</text><text x="52" y="150" class="hs-l">{e(kitchen)}</text><text x="334" y="186" class="hs-l">{e(sewer)}</text>
<!-- baignoire -->
<path d="M58 106H134V118Q134 128 124 128H68Q58 128 58 118Z" fill="{PORC}"/><path d="M64 106H128V116H64Z" fill="#38bdf8" opacity=".7" class="hs-bathw"/>
<path d="M128 106V96H138" fill="none" stroke="{PIPE}" stroke-width="3" stroke-linecap="round"/>
<!-- WC -->
<rect x="206" y="94" width="16" height="24" rx="3" fill="{PORC}"/><path d="M176 112H212V116Q210 126 196 128H188Q176 124 176 116Z" fill="{PORC}"/><rect x="186" y="128" width="10" height="4" fill="{PORC}"/>
<!-- cuisine -->
<rect x="56" y="164" width="104" height="6" rx="2" fill="#2b4a6e"/><rect x="60" y="170" width="96" height="26" fill="#1b3554"/>
<path d="M82 164H122V170Q122 176 116 176H88Q82 176 82 170Z" fill="{PORC}"/><path d="M134 164V150H122" fill="none" stroke="{PIPE}" stroke-width="3" stroke-linecap="round"/>
<!-- évacuations -->
{_pipe("M96 128V131H245", "w1", 0)}{_pipe("M191 132V131", "w1b", 0)}{_pipe("M102 176V182H245", "w2", .3)}
{_pipe("M245 84V232H352", "w3", .6)}
<rect x="346" y="196" width="28" height="44" fill="{DARK}" stroke="#2b4a6e" stroke-width="2"/><rect x="342" y="192" width="36" height="5" rx="2" fill="#64748b"/>
{_ok(140, 100, 0)}{_ok(228, 104, 1)}{_ok(132, 156, 2)}{_ok(360, 214, 3)}
</svg>'''
