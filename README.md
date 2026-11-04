# Site ABS Débouchage

## 👉 [Voir le site en ligne : abs-debouchage.pages.dev](https://abs-debouchage.pages.dev/)

Version néerlandaise : [abs-debouchage.pages.dev/nl/](https://abs-debouchage.pages.dev/nl/)

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

Cloudflare Pages publie automatiquement le dossier `public/`.
Le domaine final est défini dans `SITE_URL` (src/content.py).
