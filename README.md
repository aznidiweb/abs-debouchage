# Site ABS Débouchage

## 👉 [Voir le site en ligne : www.absdebouchage.be](https://www.absdebouchage.be/)

Version néerlandaise : [www.absdebouchage.be/nl/](https://www.absdebouchage.be/nl/)

Site statique bilingue (FR/NL) pour ABS Débouchage, débouchage et plomberie dans toute la Belgique (base à Bruxelles).

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

**Demandes d'intervention** : le formulaire envoie à `functions/api/demande.js`. Mise en service (base, photos, e-mail, WhatsApp) : voir [CONFIGURATION-DEMANDES.md](CONFIGURATION-DEMANDES.md).
