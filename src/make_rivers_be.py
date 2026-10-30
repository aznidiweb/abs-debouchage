# -*- coding: utf-8 -*-
"""Ajoute les cours d'eau à src/map_be.py (même repère que les provinces).
Sources : Natural Earth 10m (Meuse, Escaut, Sûre, Grote Gete) + tracés simplifiés (Senne, Sambre, Lys, Ourthe, Dyle, Canal Albert)
à partir de villes repères. Calage : transformation affine ajustée sur les 4 points extrêmes de la Belgique.
Usage : python3 make_rivers_be.py <ne_10m_rivers_lake_centerlines.geojson> <ne_10m_rivers_europe.geojson> <be-provinces-unk-WGS84.geo.json>"""
import json, sys, math, os, re

K = math.cos(math.radians(50.5))
# (lon, lat) réels  ↔  points extrêmes trouvés dans le fichier des provinces
REF_LL = [(2.5461, 51.0897), (6.4085, 50.3237), (4.7765, 51.5051), (5.4718, 49.4969)]

def solve(A, b):
    n = len(A[0]); M = [[sum(A[k][i] * A[k][j] for k in range(len(A))) for j in range(n)] + [sum(A[k][i] * b[k] for k in range(len(A)))] for i in range(n)]
    for c in range(n):
        p = max(range(c, n), key=lambda r: abs(M[r][c])); M[c], M[p] = M[p], M[c]
        for r in range(n):
            if r != c:
                f = M[r][c] / M[c][c]; M[r] = [a - f * bb for a, bb in zip(M[r], M[c])]
    return [M[i][n] / M[i][i] for i in range(n)]

# tracés simplifiés (villes repères, lon/lat)
HAND = {
 "Senne": [(4.07, 50.58), (4.17, 50.66), (4.24, 50.73), (4.30, 50.80), (4.35, 50.85), (4.38, 50.89), (4.43, 50.93), (4.47, 50.99), (4.48, 51.03)],
 "Dyle": [(4.61, 50.62), (4.61, 50.72), (4.66, 50.80), (4.70, 50.88), (4.62, 50.98), (4.48, 51.03), (4.37, 51.09), (4.30, 51.12)],
 "Sambre": [(4.11, 50.30), (4.20, 50.33), (4.29, 50.34), (4.37, 50.38), (4.44, 50.41), (4.55, 50.43), (4.69, 50.44), (4.79, 50.46), (4.87, 50.46)],
 "Lys": [(2.88, 50.69), (3.05, 50.76), (3.12, 50.80), (3.26, 50.83), (3.40, 50.90), (3.53, 50.98), (3.63, 51.03), (3.72, 51.05)],
 "Ourthe": [(5.79, 50.13), (5.68, 50.20), (5.57, 50.27), (5.46, 50.35), (5.50, 50.45), (5.55, 50.54), (5.58, 50.63)],
 "Canal Albert": [(5.62, 50.65), (5.60, 50.78), (5.52, 50.88), (5.33, 50.93), (5.10, 51.03), (4.85, 51.13), (4.62, 51.19), (4.42, 51.23)],
}
MAIN = {"Maas": "Meuse", "Schelde": "Escaut", "Sûre": "Sûre", "Grote Gete": "Gete"}

def main(ne_main, ne_eu, prov):
    fs = [f for f in json.load(open(prov))["features"] if f["properties"]["name"] != "UNK"]
    pts = []
    for f in fs:
        g = f["geometry"]; rs = [g["coordinates"][0]] if g["type"] == "Polygon" else [p[0] for p in g["coordinates"]]
        for r in rs: pts += [tuple(p) for p in r]
    ext = [min(pts, key=lambda p: p[0]), max(pts, key=lambda p: p[0]), max(pts, key=lambda p: p[1]), min(pts, key=lambda p: p[1])]
    A = [[lo * K, la, 1] for lo, la in REF_LL]
    ax = solve(A, [p[0] for p in ext]); ay = solve(A, [p[1] for p in ext])
    ll2hc = lambda lo, la: (ax[0] * lo * K + ax[1] * la + ax[2], ay[0] * lo * K + ay[1] * la + ay[2])
    # même cadrage que make_map_be.py
    x0, x1 = min(p[0] for p in pts), max(p[0] for p in pts); y0, y1 = min(p[1] for p in pts), max(p[1] for p in pts)
    pad = (x1 - x0) * .03; x0 -= pad; x1 += pad; y0 -= pad; y1 += pad
    s = 600 / (x1 - x0)
    proj = lambda lo, la: (lambda q: (round((q[0] - x0) * s, 1), round((y1 - q[1]) * s, 1)))(ll2hc(lo, la))
    inside = lambda lo, la: 2.4 < lo < 6.5 and 49.4 < la < 51.6
    rivers = []
    for path, key in ((ne_main, "name"), (ne_eu, "name")):
        for ft in json.load(open(path))["features"]:
            n = ft["properties"].get(key); g = ft["geometry"]
            if n not in MAIN or not g: continue
            lines = g["coordinates"] if g["type"] == "MultiLineString" else [g["coordinates"]]
            for l in lines:
                seg = [p for p in l if inside(*p[:2])]
                if len(seg) < 3: continue
                q = [proj(*p[:2]) for p in seg]
                rivers.append((MAIN[n], "M" + " ".join(f"{x:g},{y:g}" for x, y in q), 1 if n in ("Maas", "Schelde") else 2))
    for n, l in HAND.items():
        q = [proj(*p) for p in l]
        d = "M" + f"{q[0][0]:g},{q[0][1]:g}"
        for i in range(1, len(q)):   # courbes lissées (Catmull-Rom → Bézier)
            p0 = q[i - 2] if i > 1 else q[i - 1]; p1 = q[i - 1]; p2 = q[i]; p3 = q[i + 1] if i + 1 < len(q) else q[i]
            c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6); c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
            d += f"C{c1[0]:.1f},{c1[1]:.1f} {c2[0]:.1f},{c2[1]:.1f} {p2[0]:g},{p2[1]:g}"
        rivers.append((n, d, 3 if n == "Canal Albert" else 2))
    bxl = proj(4.3517, 50.8503)
    dst = os.path.join(os.path.dirname(os.path.abspath(__file__)), "map_be.py")
    src = open(dst).read()
    src = re.sub(r"\nRIVERS = .*", "", src, flags=re.S)
    src += "RIVERS = " + repr(rivers) + "\nBXL = " + repr(bxl) + "\n"
    open(dst, "w").write(src); print(len(rivers), "tracés", bxl, os.path.getsize(dst))

if __name__ == "__main__":
    main(*sys.argv[1:4])
