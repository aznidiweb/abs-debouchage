# Demandes d'intervention : mise en service

Le formulaire « Diagnostic express » du site envoie chaque demande à `https://absdebouchage.be/api/demande`
(fichier `functions/api/demande.js`, exécuté par Cloudflare Pages).

**Tant que rien n'est configuré, le site fonctionne comme avant** : le formulaire voit que le serveur n'est pas prêt
(`GET /api/demande` → `"ready": false`) et propose « Envoyer via WhatsApp », avec la demande déjà rédigée.
Aucun « Demande envoyée » n'est jamais affiché sans réponse positive du serveur.

Le serveur devient « prêt » dès qu'**au moins un** de ces deux canaux fiables existe : la base de données (D1) ou l'e-mail.
Recommandé : les deux, plus le stockage des photos (R2).

| Canal | Ce qu'il faut | Où |
|---|---|---|
| Base de données | une base D1 nommée `abs-demandes` + le schéma | wrangler.toml (`[[d1_databases]]`) |
| Photos | un bucket R2 `abs-demandes-photos` | wrangler.toml (`[[r2_buckets]]`) |
| E-mail | un compte Resend, le domaine absdebouchage.be vérifié, une clé API | secret `RESEND_API_KEY` + variables `LEAD_EMAIL_TO`, `LEAD_EMAIL_FROM` |
| WhatsApp | un compte WhatsApp Business **API Cloud** (Meta), un modèle approuvé | secret `WA_TOKEN` + variables `WA_PHONE_ID`, `WA_TO`, `WA_TEMPLATE`, `WA_LANG` |

## 1. Base de données (D1)

```bash
npx wrangler d1 create abs-demandes            # note l'identifiant affiché (database_id)
npx wrangler d1 execute abs-demandes --remote --file=migrations/0001_demandes.sql
```

Dans `wrangler.toml`, décommenter le bloc `[[d1_databases]]` et coller l'identifiant.

Voir les demandes : Cloudflare → Storage & Databases → D1 → abs-demandes → Console :
`SELECT id, received_at, urgency, problem, postal_code, city, name, phone FROM demandes ORDER BY received_at DESC;`

## 2. Photos (R2)

```bash
npx wrangler r2 bucket create abs-demandes-photos
```

Décommenter le bloc `[[r2_buckets]]`. Les photos sont rangées sous `demandes/AAAAMMJJ/<numéro>/photo-1.jpg`.
Le bucket reste **privé** (aucun accès public n'est nécessaire : les photos arrivent aussi en pièce jointe de l'e-mail).

## 3. E-mail (Resend)

1. Créer un compte sur resend.com, ajouter le domaine `absdebouchage.be` et copier les enregistrements DNS demandés
   (SPF, DKIM) chez le gestionnaire du domaine. Attendre « Verified ».
2. Créer une clé API (« Sending access »).
3. Variables : `LEAD_EMAIL_TO` = l'adresse qui reçoit les demandes (plusieurs possibles, séparées par des virgules),
   `LEAD_EMAIL_FROM` = `ABS Débouchage <demandes@absdebouchage.be>`.
4. Secret : `npx wrangler pages secret put RESEND_API_KEY --project-name abs-debouchage`.

L'e-mail contient toutes les informations, un bouton « Appeler », les photos en pièce jointe, et « Répondre » écrit
directement au client s'il a donné son e-mail. Le sujet commence par « 🔴 URGENT » quand c'est urgent.

## 4. Notification WhatsApp (facultatif)

Les liens `wa.me` ne permettent pas d'envoyer un message automatiquement : il faut l'**API WhatsApp Business Cloud** de Meta.

1. Meta Business → WhatsApp → API Cloud : un numéro expéditeur (différent du 0484 72 47 24 s'il est déjà utilisé dans l'appli WhatsApp Business), un jeton d'accès permanent (utilisateur système).
2. Créer un modèle `nouvelle_demande` (catégorie « Utilitaire », langue français) avec ce corps :
   `Nouvelle demande {{1}} : {{2}}, {{3}}, à {{4}}. Client : {{5}}.`
3. Variables : `WA_PHONE_ID` (identifiant du numéro expéditeur), `WA_TO` (numéro qui reçoit, format 32484724724),
   `WA_TEMPLATE` = `nouvelle_demande`, `WA_LANG` = `fr`. Secret : `WA_TOKEN`.

La notification WhatsApp complète l'e-mail ou la base : elle ne suffit pas seule à rendre le serveur « prêt ».

## 5. Vérifier

- `https://absdebouchage.be/api/demande` doit afficher `"ready": true` et les canaux actifs.
- Faire une vraie demande de test depuis le site : l'écran affiche un numéro `ABS-AAAAMMJJ-XXXXX`, l'e-mail arrive, la ligne apparaît dans D1.
- En cas d'échec, l'erreur est visible dans Cloudflare → Pages → abs-debouchage → Functions → Logs (aucune donnée sensible n'y est écrite, seulement le numéro et la cause).

## Tests

```bash
node --test tests/api.test.mjs            # la fonction serveur, avec un environnement simulé
(cd public && python3 -m http.server 8765) & node tests/form.e2e.cjs   # le formulaire dans un vrai navigateur
```
