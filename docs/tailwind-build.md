# Passer du CDN Tailwind à un vrai build (CLI + purge)

État au 25 juillet 2026. Ce document décrit **pourquoi** le site charge aujourd'hui Tailwind par CDN, **ce que ça coûte**, et **comment** basculer sur une feuille de style compilée. Les chiffres cités ont été mesurés sur le dépôt, pas estimés.

## D'où vient le CDN

L'hypothèse de Mikaël est juste sur le fond, avec une nuance sur la cause.

Le premier squelette du site a été produit en une passe par un générateur qui rendait un fichier HTML unique et autonome. Dans ce format, `<script src="https://cdn.tailwindcss.com"></script>` est le seul moyen de faire fonctionner Tailwind : il n'y a ni `package.json`, ni étape de compilation, ni fichier CSS à côté. Le CDN embarque le moteur Tailwind entier en JavaScript, qui génère les styles dans le navigateur au chargement.

La nuance porte sur le « rendu plus rapide » : le CDN accélère l'**écriture** (aucune installation, un copier-coller suffit), pas l'**affichage**, qu'il ralentit au contraire. C'est un artefact d'échafaudage, pas un choix d'architecture, et la documentation de Tailwind le réserve explicitement au prototypage.

Le CDN a survécu ensuite pour une raison mécanique : chaque nouvelle page a été créée en copiant l'en-tête de la précédente. La configuration se retrouve aujourd'hui dupliquée à l'identique sur les 11 pages du site.

## Ce que ça coûte

Sur chaque page, le navigateur doit télécharger le moteur Tailwind, l'exécuter, parcourir le DOM pour relever les classes utilisées, générer la feuille de style correspondante, puis l'injecter. Le premier rendu visuellement stable attend la fin de cette chaîne. Un fichier CSS statique, lui, est découvert dans le `<head>` et chargé en parallèle du HTML, sans exécution de JavaScript.

Trois effets concrets :

- **Retard du premier rendu** sur toutes les pages, avec un risque de flash de contenu non stylé si le script tarde.
- **Aucune mise en cache utile** de la feuille de style : le résultat est recalculé à chaque page et à chaque visite.
- **Dépendance à un tiers** : si `cdn.tailwindcss.com` est inaccessible, le site s'affiche sans aucun style. C'est exactement ce qui se produit dans l'environnement de développement utilisé pour ce dépôt, où le domaine est bloqué.

Mesure faite en compilant le site réel avec la CLI Tailwind, configuration et contenus identiques à la production :

| Feuille compilée | Poids |
| --- | --- |
| Brute | 46,7 Ko |
| Minifiée | 32,3 Ko |
| **Minifiée + gzip (ce qui transite)** | **6,6 Ko** |

6,6 Ko de CSS statique remplacent le téléchargement et l'exécution du moteur complet. Le poids exact du bundle CDN n'a pas pu être mesuré ici (domaine bloqué), mais l'ordre de grandeur est sans commune mesure : il s'agit d'un compilateur, pas d'une feuille de style.

## Version de Tailwind : v3 d'abord

Tailwind 4 est disponible et déplace la configuration du JavaScript vers le CSS (`@theme`). Le site est écrit en conventions v3 (`tailwind.config` avec `theme.extend`), et la palette `slate` y est **remappée**, ce qui est précisément le genre de personnalisation qui se traduit mal automatiquement.

Recommandation : **migrer d'abord vers un build v3**, qui ne demande aucune réécriture de classe et dont le résultat doit être visuellement identique au pixel près. Un éventuel passage en v4 est un second chantier, à mener seulement une fois le build en place et vérifié. Mener les deux d'un coup rendrait impossible de savoir laquelle des deux modifications a cassé un rendu.

## Architecture cible

```
portfolio/
├── package.json              # tailwindcss en devDependency + scripts npm
├── tailwind.config.js        # la config aujourd'hui dupliquée sur 11 pages
├── src/
│   └── tailwind.css          # @tailwind + le <style> commun mutualisé
├── assets/
│   └── site.css              # feuille compilée, servie par les pages
└── *.html                    # <link rel="stylesheet"> au lieu du <script>
```

### `package.json`

```json
{
  "name": "portfolio",
  "private": true,
  "scripts": {
    "dev": "tailwindcss -i src/tailwind.css -o assets/site.css --watch",
    "build": "tailwindcss -i src/tailwind.css -o assets/site.css --minify"
  },
  "devDependencies": {
    "tailwindcss": "^3.4.0"
  }
}
```

### `tailwind.config.js`

La clé `content` est ce que l'on appelait « purge » en v2 : la liste des fichiers que Tailwind parcourt pour ne garder que les classes réellement utilisées. Tout ce qui n'y figure pas est absent de la feuille finale.

```js
module.exports = {
  content: ['./*.html', './blog/*.html', './blog-articles/*.html'],
  theme: {
    extend: {
      colors: {
        brand: { 50:'#eef1f8', 100:'#e0e6f3', 400:'#41538f', 500:'#1e3a8a', 600:'#15295f', 900:'#0f1f49' },
        indigo: { 500:'#1e3a8a' },
        slate: { 50:'#faf7f1', 100:'#f1ead9', 200:'#e6dfce', 300:'#d3c9b2', 400:'#9b9486',
                 500:'#7c7567', 600:'#574f40', 700:'#3e3729', 800:'#2a2820', 900:'#1c2b3a', 950:'#141b24' }
      },
      fontFamily: {
        display: ['Gloock', 'serif'],
        sans: ['Instrument Sans', 'sans-serif'],
        mono: ['Geist Mono', 'monospace'],
      }
    }
  }
}
```

Le JavaScript du site est écrit **à l'intérieur** des fichiers HTML : les globs ci-dessus le couvrent donc déjà. Point vérifié : les classes injectées dynamiquement (`class="${logo.height} ..."` dans `trustedByData`) tirent leurs valeurs de chaînes complètes présentes dans la source (`"h-9 sm:h-11"`), que le scanner relève sans difficulté. **Aucune `safelist` n'est nécessaire aujourd'hui**, mais la règle est à retenir : ne jamais composer un nom de classe par concaténation (`` `h-${n}` ``), sinon la classe disparaît à la compilation.

### `src/tailwind.css`

```css
@tailwind base;
@tailwind components;
@tailwind utilities;

/* Le <style> aujourd'hui dupliqué dans chaque page vient ici. */
```

## Le point à trancher : GitHub Pages ne compile rien

GitHub Pages sert les fichiers du dépôt tels quels. Une commande `npm run build` locale ne s'exécutera jamais côté serveur. Deux options :

**Option A — commiter la feuille compilée.** `assets/site.css` est versionné, `npm run build` est lancé à la main avant chaque commit qui touche des classes. Simple, aucun outillage. Défaut réel : un oubli de rebuild produit un site aux styles périmés, sans erreur visible ni au commit ni au déploiement.

**Option B — compiler dans GitHub Actions (recommandé).** Le dépôt ne contient que les sources ; le workflow compile et publie. L'oubli devient impossible.

```yaml
# .github/workflows/deploy.yml
name: Build & deploy
on:
  push:
    branches: [main]
permissions:
  contents: read
  pages: write
  id-token: write
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 22
      - run: npm ci
      - run: npm run build
      - uses: actions/upload-pages-artifact@v3
        with:
          path: .
  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment:
      name: github-pages
    steps:
      - uses: actions/deploy-pages@v4
```

Bascule à faire une fois dans l'interface : **Settings → Pages → Source → GitHub Actions**.

L'option B change la façon dont le site est publié. C'est la seule partie du chantier qui touche à l'infrastructure, et la seule qui puisse rendre le site inaccessible si elle est mal faite : à traiter seule, dans sa propre PR, et à vérifier immédiatement en ligne.

## Le chantier, par étapes

Chaque étape est une PR distincte, vérifiable indépendamment.

**Étape 1 — Outillage, sans rien changer au site.**
Ajouter `package.json`, `tailwind.config.js`, `src/tailwind.css`, `.gitignore` (`node_modules/`). Compiler, comparer la feuille obtenue au rendu actuel. Les 11 pages continuent d'utiliser le CDN : aucun risque, rien n'est publié.

**Étape 2 — Mutualiser le `<style>` inline.**
Le bloc `<style>` est aujourd'hui recopié dans chaque page, avec des variantes selon la profondeur du dossier (`.method-row` pointe vers `images/`, `../images/` selon la page). Rassembler le tronc commun dans `src/tailwind.css`, ne laisser en page que ce qui est réellement spécifique. Étape purement mécanique, mais celle où une différence entre deux copies peut se perdre : comparer les 11 blocs avant de fusionner.

**Étape 3 — Basculer les pages.**
Sur chaque page, remplacer les trois éléments (`<script src="cdn...">`, `<script>tailwind.config = {...}</script>`, bloc `<style>` mutualisé) par un unique `<link rel="stylesheet" href="assets/site.css">`, chemin relatif adapté selon le dossier. C'est l'étape à vérifier page par page.

**Étape 4 — Publication.**
Mettre en place l'option A ou B ci-dessus.

**Étape 5 — Mesure.**
PageSpeed Insights sur l'accueil, un article et la FAQ, avant/après, pour objectiver le gain.

## Vérification : comparaison visuelle automatisée

Le risque du chantier n'est pas de casser le site franchement, c'est de décaler un détail sans que personne le remarque. La compilation locale rend une comparaison automatique possible, et elle a déjà été utilisée sur ce dépôt :

1. Servir le site (`python3 -m http.server 8000`).
2. Capturer chaque page avec Playwright, en 1440 px et en 390 px.
3. Rejouer les mêmes captures après bascule, comparer pixel à pixel.

Une différence attendue subsiste : le CDN génère les styles après le chargement, la feuille compilée les applique immédiatement. Attendre la stabilisation de la page avant capture, sinon la comparaison remonte des écarts qui n'en sont pas.

## Ce que le chantier ne règle pas

- **Les Google Fonts** restent quatre familles chargées depuis un domaine tiers, en tête de page. C'est le second poste de latence après le CDN Tailwind. Les auto-héberger est un chantier séparé, à envisager après celui-ci.
- **Le poids des images** est déjà traité par la règle d'optimisation en place (`CLAUDE.md`).
- **Les décalages de mise en page** ont été réglés en juillet 2026 par l'ajout de `width`/`height` sur les 50 images locales.
