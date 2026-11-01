# -*- coding: utf-8 -*-
"""Optimisation après build (PageSpeed) :
1. retire du CSS les règles dont les classes/ids n'existent nulle part (HTML générés + scripts),
2. retire les @keyframes jamais utilisées, minifie,
3. intègre le CSS dans chaque page (<style>) : plus de requête qui bloque l'affichage."""
import os, re, glob

def _corpus(out, only=None):
    words = set()
    for f in ([only] if only else glob.glob(os.path.join(out, "**", "*.html"), recursive=True)):
        h = open(f, encoding="utf-8").read()
        for m in re.finditer(r'\bclass="([^"]*)"', h): words.update(m.group(1).split())
        for m in re.finditer(r'\bid="([^"]*)"', h): words.add(m.group(1))
        for m in re.finditer(r'\b(data-[\w-]+|aria-[\w-]+|role|hidden|open|disabled|type|href|lang)\b', h): words.add(m.group(1))
        for sc in re.findall(r'<script(?![^>]*application/ld\+json)[^>]*>(.*?)</script>', h, flags=re.S):
            words.update(re.findall(r'[A-Za-z][\w-]*', sc))
    for f in glob.glob(os.path.join(out, "assets", "*.js")):
        js = open(f, encoding="utf-8").read()
        words.update(re.findall(r'[A-Za-z][\w-]*', js))     # tout mot présent dans les scripts (classes ajoutées dynamiquement)
    return words

def _strip_comments(css):
    return re.sub(r'/\*.*?\*/', '', css, flags=re.S)

def _blocks(css):
    """Découpe le CSS en blocs de premier niveau : (prélude, corps) ; corps=None pour les instructions @charset/@import."""
    i, n, out = 0, len(css), []
    while i < n:
        j = css.find('{', i); k = css.find(';', i)
        if j == -1: break
        if css[i:].lstrip().startswith('@') and k != -1 and k < j:
            out.append((css[i:k+1].strip(), None)); i = k + 1; continue
        pre = css[i:j].strip(); depth, p = 1, j + 1
        while p < n and depth:
            c = css[p]
            if c == '{': depth += 1
            elif c == '}': depth -= 1
            p += 1
        out.append((pre, css[j+1:p-1])); i = p
    return out

def _sel_used(sel, words):
    s = re.sub(r':(?:not|is|where|has)\((?:[^()]|\([^()]*\))*\)', '', sel)   # le contenu de :not()… n'est pas requis
    s = re.sub(r'::?[\w-]+(\([^)]*\))?', '', s)
    for tok in re.findall(r'\.([\w-]+)', s):
        if tok not in words: return False
    for tok in re.findall(r'#([\w-]+)', s):
        if tok not in words: return False
    for tok in re.findall(r'\[([\w-]+)', s):
        if tok not in words: return False
    return True

def _purge(css, words):
    out = []
    for pre, body in _blocks(css):
        if body is None: out.append(pre); continue
        if pre.startswith('@media') or pre.startswith('@supports'):
            inner = _purge(body, words)
            if inner.strip(): out.append(pre + '{' + inner + '}')
        elif pre.startswith('@'):
            out.append(pre + '{' + body + '}')            # @font-face, @keyframes… (keyframes triées plus bas)
        else:
            sels = [s.strip() for s in re.split(r',(?![^()]*\))', pre) if s.strip()]
            keep = [s for s in sels if _sel_used(s, words)]
            if keep: out.append(','.join(keep) + '{' + body + '}')
    return ''.join(out)

def _drop_unused_keyframes(css):
    names = set(re.findall(r'@keyframes\s+([\w-]+)', css))
    rest = re.sub(r'@keyframes\s+[\w-]+\s*\{(?:[^{}]|\{[^{}]*\})*\}', '', css)
    used = {n for n in names if re.search(r'\b' + re.escape(n) + r'\b', rest)}
    return re.sub(r'@keyframes\s+([\w-]+)\s*\{(?:[^{}]|\{[^{}]*\})*\}', lambda m: m.group(0) if m.group(1) in used else '', css)

def _minify(css):
    css = re.sub(r'\s+', ' ', css)
    css = re.sub(r'\s*([{};,>])\s*', r'\1', css)
    css = re.sub(r'\s*:\s*(?![^{]*\{)', ':', css)   # deux-points hors sélecteurs
    css = css.replace(';}', '}')
    return css.strip()

def optimize(out):
    path = os.path.join(out, "assets", "styles.css")
    raw = _strip_comments(open(path, encoding="utf-8").read())
    # le CSS sera dans la page : les chemins relatifs (polices…) deviennent absolus
    raw = re.sub(r'url\(\s*(["\']?)(?!data:|https?:|/)([^"\')]+)\1\s*\)', lambda m: 'url(' + m.group(1) + '/assets/' + m.group(2) + m.group(1) + ')', raw)
    full = _minify(_drop_unused_keyframes(_purge(raw, _corpus(out))))
    open(path, "w", encoding="utf-8").write(full)          # version complète (secours)
    tag = re.compile(r'<link rel="stylesheet" href="/assets/styles\.css\?v=[^"]*">')
    sizes = []
    for f in glob.glob(os.path.join(out, "**", "*.html"), recursive=True):
        h = open(f, encoding="utf-8").read()
        if not tag.search(h): continue
        css = _minify(_drop_unused_keyframes(_purge(raw, _corpus(out, only=f))))   # uniquement ce que la page utilise
        sizes.append(len(css))
        open(f, "w", encoding="utf-8").write(tag.sub(lambda m: "<style>" + css + "</style>", h))
    return len(raw), max(sizes) if sizes else len(full)
