# Passer du CDN Tailwind à un vrai build (CLI + purge)

> **Migration réalisée le 25 juillet 2026.** Le site est compilé et publié par
> `.github/workflows/deploy.yml`. Ce document garde la trace du raisonnement,
> des mesures et des arbitrages ; le mode d'emploi au quotidien est dans
> `CLAUDE.md`, section « Build Tailwind ».

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

## Publication : GitHub Pages ne compile rien

GitHub Pages sert les fichiers du dépôt tels quels. Une commande `npm run build` locale ne s'exécutera jamais côté serveur. Deux options se présentaient :

**Option A — commiter la feuille compilée.** `assets/site.css` versionné, `npm run build` lancé à la main avant chaque commit qui touche des classes. Simple, aucun outillage. Défaut réel : un oubli de rebuild produit un site aux styles périmés, **sans erreur visible** ni au commit ni au déploiement. La page s'affiche presque correctement, seul l'élément concerné est cassé.

**Option B — compiler dans GitHub Actions.** Retenue le 25/07/2026. Le dépôt ne contient que les sources ; le workflow compile, vérifie et publie. L'oubli devient impossible par construction.

Bascule à faire **une fois** dans l'interface, sans quoi le workflow publiera dans le vide : **Settings → Pages → Source → GitHub Actions**.

### Précaution pendant la transition

Tant que la source Pages reste « Deploy from a branch », le site en ligne lit les fichiers de la branche. Si `assets/site.css` n'y était pas, le site s'afficherait **sans aucun style** entre la fusion et la bascule du réglage.

`assets/site.css` est donc **versionné à titre transitoire**. Conséquence tant que le réglage n'est pas fait : lancer `npm run build` et committer le résultat à chaque changement de style. Une fois la bascule effectuée, ajouter le fichier au `.gitignore` — c'est à ce moment seulement que l'oubli de compilation devient réellement impossible.

Le dépôt étant public, les minutes Actions sont gratuites et illimitées.

### Ce que le workflow fait en plus

- **Il vérifie avant de publier.** `scripts/verifier-pages.py` contrôle le HTML, les blocs JSON-LD, les liens internes, les images référencées, et les règles standing du blog (pas de légende, `alt=""`, `data-site="blog"`). Ces contrôles n'existaient que sous forme de commandes tapées à la main ; ils tournent désormais à chaque push et bloquent la publication en cas d'échec.
- **Il ne publie que ce qui doit l'être.** Le site est assemblé par `rsync` dans `_site`, en excluant les sources (`src/`, `tailwind.config.js`), l'outillage npm et **les notes internes**. Auparavant, `TODO.md`, `CLAUDE.md`, `docs/brand-voice.md` et surtout `docs/etudes-de-cas.md` — qui contient des relevés de missions clientes — étaient servis publiquement, GitHub Pages publiant tout le contenu de la branche.
- **Il compile les Pull Requests sans les publier.** Une PR qui casse le CSS ou une règle échoue avant d'atteindre `main`.

## Ce qui a été trouvé en cours de route

La mutualisation des 11 blocs `<style>` a mis au jour une **dérive entre les copies**, invisible tant que chaque page portait la sienne :

| Divergence | Constat | Décision |
| --- | --- | --- |
| `.hero-anim` | `.7s` sur les 7 articles, `.8s` sur l'accueil, la FAQ et le listing | Unifié à `.8s` |
| `@keyframes heroFadeUp` | `translateY(14px)` sur les articles, `16px` ailleurs | Unifié à `16px` |
| `h1, h2, h3` | `404.html` ne stylait que `h1, h2` | Unifié sur les trois |
| `@media (prefers-reduced-motion)` | 6 variantes, chacune couvrant un sous-ensemble différent | Fusionnées en un bloc unique, plus complet que chaque original |
| `.font-mono` dans le blog | Instrument Sans dans le blog, Space Grotesk sur le site principal | **Divergence voulue** (voir `CLAUDE.md`), conservée via `body[data-site="blog"]` |

Les quatre premières lignes sont des dérives accidentelles, nées de copier-coller successifs. Les écarts sont imperceptibles à l'œil (une animation d'entrée à 100 ms près), mais ils illustrent le vrai coût du CSS dupliqué : rien ne signale que deux pages ont divergé.

Un piège évité au passage : `.method-row` référence le curseur par `url('images/logo-aencre-cursor.png')`. Une fois la règle déplacée dans `assets/site.css`, ce chemin se résout depuis `assets/` et non depuis la racine — il a fallu le passer en `../images/`.

## Vérification : comparaison visuelle automatisée

Le risque du chantier n'était pas de casser le site franchement, c'était de décaler un détail sans que personne le remarque. La méthode employée :

1. Servir le site (`python3 -m http.server`).
2. Capturer les 11 pages avec Playwright, en pleine hauteur, à 1440 px et 390 px, animations neutralisées et images `lazy` forcées en `eager` pour que la capture soit déterministe.
3. Rejouer les mêmes captures après bascule, comparer pixel à pixel.

Cette méthode valide la migration elle-même (mutualisation du CSS, bascule des pages). Elle ne valide pas l'équivalence CDN → CSS compilé, les deux étant générés par le même moteur à partir de la même configuration.

## Résultat

| | Avant | Après |
| --- | --- | --- |
| Feuille de style | générée en JS à chaque chargement | `assets/site.css`, **8,4 Ko en gzip** |
| CSS dupliqué dans le HTML | ~3,5 Ko par page × 11 | 0 |
| Config Tailwind | recopiée sur 11 pages | `tailwind.config.js` |
| Vérifications | commandes tapées à la main | bloquantes dans le workflow |
| Notes internes en ligne | oui | non |

## Ce que le chantier ne règle pas

- **Les Google Fonts** restent quatre familles chargées depuis un domaine tiers, en tête de page. C'est désormais le premier poste de latence. Les auto-héberger est le chantier suivant.
- **Le poids des images** est déjà traité par la règle d'optimisation en place (`CLAUDE.md`).
- **Les décalages de mise en page** ont été réglés en juillet 2026 par l'ajout de `width`/`height` sur les 50 images locales.
- **Le passage en Tailwind v4** reste ouvert, et reste un chantier distinct.

## Étape restante

**Mesurer.** PageSpeed Insights sur l'accueil, un article et la FAQ, pour objectiver le gain. À faire une fois le premier déploiement Actions passé.
