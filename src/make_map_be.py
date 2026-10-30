# -*- coding: utf-8 -*-
"""Génère src/map_be.py : contours SVG des provinces belges (carte « partout en Belgique »).
Source : be-provinces-unk-WGS84.geo.json (github.com/mathiasleroy/belgium-geographic-data, données Highcharts).
Usage : python3 make_map_be.py chemin/vers/be-provinces-unk-WGS84.geo.json"""
import json, sys, math, os
from make_map import rdp

NAMES = {  # nom source : (id, FR, NL, codes postaux)
 "Brussels": ("bxl", "Bruxelles", "Brussel", "1000–1299"),
 "Walloon Brabant": ("bw", "Brabant wallon", "Waals-Brabant", "1300–1499"),
 "Flemish Brabant": ("vb", "Brabant flamand", "Vlaams-Brabant", "1500–1999, 3000–3499"),
 "Antwerp": ("an", "Anvers", "Antwerpen", "2000–2999"),
 "Limburg": ("li", "Limbourg", "Limburg", "3500–3999"),
 "Liege": ("lg", "Liège", "Luik", "4000–4999"),
 "Namur": ("na", "Namur", "Namen", "5000–5999"),
 "Hainaut": ("ha", "Hainaut", "Henegouwen", "6000–6599, 7000–7999"),
 "Luxembourg": ("lu", "Luxembourg", "Luxemburg", "6600–6999"),
 "West Flanders": ("wv", "Flandre-Occidentale", "West-Vlaanderen", "8000–8999"),
 "East Flanders": ("ov", "Flandre-Orientale", "Oost-Vlaanderen", "9000–9999"),
}
W = 600

def main(src):
    feats = [f for f in json.load(open(src))["features"] if f["properties"]["name"] in NAMES]
    feats.sort(key=lambda f: f["properties"]["name"] == "Brussels")  # Bruxelles dessinée en dernier (au-dessus du Brabant flamand)
    k = 1  # coordonnées déjà projetées dans ce fichier
    def rings(g): return [g["coordinates"][0]] if g["type"] == "Polygon" else [p[0] for p in g["coordinates"]]
    pts = [(p[0] * k, p[1]) for f in feats for r in rings(f["geometry"]) for p in r]
    x0, x1 = min(p[0] for p in pts), max(p[0] for p in pts); y0, y1 = min(p[1] for p in pts), max(p[1] for p in pts)
    pad = (x1 - x0) * .03; x0 -= pad; x1 += pad; y0 -= pad; y1 += pad
    s = W / (x1 - x0); H = round((y1 - y0) * s)
    proj = lambda p: (round((p[0] * k - x0) * s, 1), round((y1 - p[1]) * s, 1))
    out = []
    for f in feats:
        pid, fr, nl, cp = NAMES[f["properties"]["name"]]
        d, big, area = "", None, 0
        for r in rings(f["geometry"]):
            r = [tuple(p) for p in r]; m = len(r) // 2
            q = r
            if len(q) < 4: continue
            qq = [proj(p) for p in q]
            d += "M" + " ".join(f"{x:g},{y:g}" for x, y in qq[:-1]) + "Z"
            a = abs(sum(xa * yb - xb * ya for (xa, ya), (xb, yb) in zip(qq, qq[1:])))
            if a > area: area, big = a, qq
        cx = sum(p[0] for p in big) / len(big); cy = sum(p[1] for p in big) / len(big)
        out.append((pid, fr, nl, cp, d, (round(cx, 1), round(cy, 1))))
    dst = os.path.join(os.path.dirname(os.path.abspath(__file__)), "map_be.py")
    open(dst, "w").write("# Généré par make_map_be.py — ne pas modifier à la main\nMAP_BE = " + repr({"w": W, "h": H, "prov": out}) + "\n")
    print(dst, os.path.getsize(dst), W, H)

if __name__ == "__main__":
    main(sys.argv[1])
