# -*- coding: utf-8 -*-
"""
Génère src/map_data.py : les contours SVG des communes (carte de la zone d'intervention).
À relancer seulement si on change la liste des communes affichées.

Source : contours des communes belges (Statbel, via github.com/mathiasleroy/belgium-geographic-data,
fichier dist/polygons/be-municip-lamberts.geo.json, projection Lambert 72).
Usage : python3 make_map.py chemin/vers/be-municip-lamberts.geo.json
"""
import json, sys, math, os

BXL = {21001: "Anderlecht", 21002: "Auderghem", 21003: "Berchem-Sainte-Agathe", 21004: "Bruxelles-Ville",
       21005: "Etterbeek", 21006: "Evere", 21007: "Forest", 21008: "Ganshoren", 21009: "Ixelles",
       21010: "Jette", 21011: "Koekelberg", 21012: "Molenbeek-Saint-Jean", 21013: "Saint-Gilles",
       21014: "Saint-Josse-ten-Noode", 21015: "Schaerbeek", 21016: "Uccle", 21017: "Watermael-Boitsfort",
       21018: "Woluwe-Saint-Lambert", 21019: "Woluwe-Saint-Pierre"}
PERI = {23094: "Zaventem", 23088: "Vilvorde", 23016: "Dilbeek", 23098: "Drogenbos", 23099: "Kraainem",
        23103: "Wezembeek-Oppem", 23047: "Machelen", 23025: "Grimbergen"}
# communes voisines dessinées en gris, juste pour situer la carte
CTX = [23102, 23050, 23003, 23100, 23101, 23033, 23062, 24104, 23077, 23081, 23002, 23086, 23096, 23038, 24086]

W = 600          # largeur du viewBox
TOL = 60         # tolérance de simplification, en mètres

def rdp(pts, eps):
    if len(pts) < 3: return pts
    (x1, y1), (x2, y2) = pts[0], pts[-1]
    dx, dy = x2 - x1, y2 - y1; n = math.hypot(dx, dy) or 1e-9
    i_max, d_max = 0, 0
    for i in range(1, len(pts) - 1):
        x, y = pts[i]
        d = abs(dy * x - dx * y + x2 * y1 - y2 * x1) / n
        if d > d_max: i_max, d_max = i, d
    if d_max <= eps: return [pts[0], pts[-1]]
    return rdp(pts[:i_max + 1], eps)[:-1] + rdp(pts[i_max:], eps)

def rings(geom):
    if geom["type"] == "Polygon": return [geom["coordinates"][0]]
    return [p[0] for p in geom["coordinates"]]

def main(src):
    feats = {f["properties"]["NIS5"]: f["geometry"] for f in json.load(open(src))["features"]}
    keep = list(BXL) + list(PERI)
    xs = [p[0] for k in keep for r in rings(feats[k]) for p in r]
    ys = [p[1] for k in keep for r in rings(feats[k]) for p in r]
    pad = 900
    x0, x1, y0, y1 = min(xs) - pad, max(xs) + pad, min(ys) - pad, max(ys) + pad
    s = W / (x1 - x0); H = round((y1 - y0) * s)
    def proj(p): return (round((p[0] - x0) * s, 1), round((y1 - p[1]) * s, 1))
    def path(geom):
        out = []
        for r in rings(geom):
            r = [tuple(p) for p in r]; m = len(r) // 2   # anneau fermé : on simplifie les deux moitiés
            pts = rdp(r[:m + 1], TOL)[:-1] + rdp(r[m:], TOL)
            if len(pts) < 4: continue
            q = [proj(p) for p in pts]
            out.append("M" + " ".join(f"{x:g},{y:g}" for x, y in q[:-1]) + "Z")
        return "".join(out)
    def centre(geom):
        r = max(rings(geom), key=len); a = cx = cy = 0
        for (xa, ya), (xb, yb) in zip(r, r[1:]):
            c = xa * yb - xb * ya; a += c; cx += (xa + xb) * c; cy += (ya + yb) * c
        a /= 2; return proj((cx / (6 * a), cy / (6 * a)))
    data = {"w": W, "h": H,
            "bxl": [(n, path(feats[k]), centre(feats[k])) for k, n in BXL.items()],
            "peri": [(n, path(feats[k]), centre(feats[k])) for k, n in PERI.items()],
            "ctx": [path(feats[k]) for k in CTX if k in feats]}
    dst = os.path.join(os.path.dirname(__file__), "map_data.py")
    open(dst, "w").write("# Généré par make_map.py — ne pas modifier à la main\nMAP = " + repr(data) + "\n")
    print(dst, os.path.getsize(dst), "octets, viewBox", W, H)

if __name__ == "__main__":
    main(sys.argv[1])
