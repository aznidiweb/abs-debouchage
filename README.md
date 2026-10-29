# Site ABS Débouchage

Site statique bilingue (FR/NL) pour ABS Débouchage, Bruxelles.

- `src/content.py` : **tous les textes** (services, prix, FAQ, communes, coordonnées).
- `src/build.py` : génère le site dans `public/`.
- `src/assets/` : styles et script.
- `src/make_images.py` : régénère l'image de partage et les icônes.

Après une modification :

```
python3 src/build.py
git add -A && git commit -m "..." && git push
```

Netlify publie automatiquement le dossier `public/`.
Le domaine final est défini dans `SITE_URL` (src/content.py).
