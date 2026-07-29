# CLAUDE.md — Portfolio Mikaël Andraos

Guidance pour Claude Code (claude.ai/code) sur ce dépôt.

## Vue d'ensemble

Portfolio personnel de Mikaël Andraos — **« Stratégie créative & content marketing — SEO/GEO, Contenu, UX »** — entièrement en français.
Site statique **multi-pages sans framework** : `index.html` (accueil, une seule page), `blog/index.html` (liste des articles, accessible via l'URL `/blog/`), `blog-articles/*.html` (articles individuels) et `404.html` (page d'erreur personnalisée, servie automatiquement par GitHub Pages). Aucune dépendance à l'exécution : la seule dépendance de développement est Tailwind.
Hébergé sur GitHub Pages : pousser sur `main` déclenche le workflow qui compile et publie — https://www.mikaelandraos.fr/

## Développement

Le CSS est **compilé** depuis juillet 2026 (voir « Build Tailwind » plus bas). Il faut donc lancer la compilation en parallèle du serveur :

```bash
npm install          # une seule fois
npm run dev          # recompile assets/site.css à chaque modification
python3 -m http.server 8000   # dans un second terminal
# puis ouvrir http://localhost:8000
```

Ouvrir `index.html` directement au lieu de passer par le serveur fonctionne aussi, à condition qu'`assets/site.css` ait déjà été compilé au moins une fois.

Avant de committer :

```bash
npm run build                     # feuille minifiée
python3 scripts/verifier-pages.py # HTML, JSON-LD, liens, images, règles du blog
```

Ces deux commandes tournent aussi dans le workflow GitHub Actions, qui échoue si l'une des deux échoue. En complément, vérifier dans le navigateur ce qu'aucun script ne couvre : filtres, modale, rendu mobile.

## Build Tailwind

- **Sources** : `src/tailwind.css` (directives `@tailwind` + toutes les règles maison) et `tailwind.config.js` (palette et polices). C'est **là** qu'on modifie le style, jamais dans une page.
- **Sortie** : `assets/site.css`, régénéré par `npm run build`.
  ⚠️ **Mesure transitoire** : ce fichier est versionné pour l'instant, le temps que la source GitHub Pages passe de « branche » à « GitHub Actions ». Tant que ce réglage n'est pas fait, le site en ligne lit le fichier tel qu'il est dans la branche : il faut donc lancer `npm run build` **et committer le résultat** à chaque changement de style, sinon le site affiche l'ancien CSS. Une fois la bascule faite (Settings → Pages → Source → GitHub Actions), ajouter `assets/site.css` au `.gitignore` : le workflow le recompilera à chaque publication.
- **Les pages ne portent plus ni `<script src="cdn.tailwindcss.com">`, ni `tailwind.config` inline, ni bloc `<style>`.** Elles ont un seul `<link rel="stylesheet" href="assets/site.css">` (chemin relatif à adapter selon la profondeur du dossier). Ne pas réintroduire de CSS inline : une règle qui n'existe que sur une page a quand même sa place dans `src/tailwind.css`, les sélecteurs étant tous propres à leur contexte.
- **Pages de blog** : leur `<body>` porte `data-site="blog"`, ce qui déclenche la règle qui bascule `.font-mono` en Instrument Sans hors pied de page. Un nouvel article sans cet attribut aura la mauvaise police.
- **Classes construites en JavaScript** : elles doivent apparaître en toutes lettres dans la source (`height: "h-9 sm:h-11"` dans `trustedByData`). Ne jamais concaténer un nom de classe (`` `h-${n}` ``) : Tailwind ne le détecterait pas et la classe disparaîtrait à la compilation.
- **Publication** : `.github/workflows/deploy.yml` compile, vérifie, puis publie sur GitHub Pages. Seuls les fichiers servis sont copiés — les sources, l'outillage npm et les notes internes (`docs/`, `TODO.md`, `CLAUDE.md`, calendrier éditorial) ne sont plus mis en ligne. Une PR est compilée et vérifiée mais jamais publiée.
- Le contexte complet de cette migration est dans `docs/tailwind-build.md`.

## Design system « Grâce Institutionnelle »

Défini dans `tailwind.config.js` (palette, polices) et `src/tailwind.css` (règles maison) :

- **Bleu encre signature** : `brand-500` = `#1e3a8a` (actions primaires, accents ; hover `brand-600`).
- **Palette chaude** : l'échelle `slate` est **remappée** vers des tons ivoire/anthracite (`slate-50` = `#faf7f1`, etc.) — utiliser les classes `slate-*` habituelles, elles rendent chaud. `.bg-white` est forcé en blanc cassé `#fffdf8`.
- **Typographie** : `Gloock` (serif display — appliqué automatiquement à h1/h2/h3 en graisse 400, ne pas mettre de `font-bold` sur les titres), `Instrument Sans` (texte), `Space Grotesk` (micro-labels — appliqué automatiquement via `.tracking-widest`/`.tracking-wider`/`.font-mono`). `Geist Mono` reste utilisé dans le pied de page (sélecteur `footer`) de **toutes** les pages, y compris le blog. Sur le site principal (`index.html`, `404.html`), il est aussi réservé à l'encart Méthode de la section À propos (`.method-card`) et aux libellés de contact/formulaire (`.label-geist`) — ne pas l'étendre ailleurs sans en discuter avec Mikaël. **Dans le blog (`blog/index.html` et `blog-articles/*.html`), en dehors du pied de page, Geist Mono n'est plus utilisé** (depuis juillet 2026) : les micro-labels en majuscules (catégories, sommaire) restent en Space Grotesk, mais les dates, temps de lecture et signature d'auteur (`.font-mono` hors `tracking-wider`/`tracking-widest`) sont en Instrument Sans, comme le reste du texte.
- **Détails éditoriaux** : filets fins (`h-px`), numéros display, ornement ✳, micro-labels en capitales espacées. Les **numéros display** sont réservés aux suites ordonnées (les trois temps de la méthode dans l'encart À propos, les statistiques) : ne pas les utiliser pour numéroter une liste dont l'ordre n'a pas de sens.
- **Symboles en filigrane du hero** (`index.html`, section `#hero-section`, visibles à partir de `lg` seulement) : trois marques discrètes en fond, toutes calées sur le même décalage vertical `-top-16` et une opacité proche (`0.06`–`0.08`) pour se lire comme un trio délibéré plutôt que des éléments épars — le mark de l'ancre en haut à gauche, le "&" en `font-display` en haut à droite, l'ornement ✳ isolé au centre droit à mi-hauteur (`top-96 right-[8%]`), à l'écart du bandeau de logos en bas de section. Toute nouvelle marque ajoutée là doit rester dans ce triangle de composition et à une opacité comparable, sans jamais chevaucher le texte, les boutons ou le bandeau de logos.
- **Icônes** : l'iconographie reste rare et cantonnée à `index.html`, où elle suit **un seul gabarit**, harmonisé le 26/07/2026 : pictogramme au trait de 20 px (`w-5 h-5`, `stroke-width="1.5"`) centré dans un carré de 44 px `w-11 h-11 rounded-xl border border-brand-100 bg-brand-50 text-brand-500`. Douze cadres au total, mesurés identiques :
  - les cinq cartes de Compétences (`.skill-icon`), qui gardent leur signature propre : le cadre pivote au survol et laisse apparaître le mark de l'ancre à la place du pictogramme ;
  - les quatre cartes de Prestations (`.prestation-icon`), qui s'inversent en bleu plein au survol ;
  - les trois cartes de contact, sans état de survol. Le glyphe LinkedIn y fait exception en restant un logo plein (`fill="currentColor"`, sans contour) : c'est une marque, pas un pictogramme maison.

  Toute nouvelle icône reprend ce gabarit. Ne pas l'étendre à d'autres sections : ailleurs, la hiérarchie passe par la typographie et les filets. Les flèches et chevrons de contrôle (12 px, `stroke-width="2"`) et les pictogrammes du bouton de menu ne relèvent pas de ce vocabulaire et gardent leur trait plus épais, faute de quoi ils rendraient trop maigre à cette taille.
- **Pas de dark mode** : retiré du site (juillet 2026) pour fiabiliser l'affichage — ne pas réintroduire de classes `dark:` ni de bouton de bascule sans en discuter avec Mikaël.

Pas de couleurs vives hors palette, pas d'esthétique « tech/terminal ».

## Contenu & messages

- **Positionnement** : « Stratégie créative et content marketing — SEO/GEO, Contenu et UX ». Aligné partout : `<title>`, metas, JSON-LD `jobTitle`, hero.
- **Narratif de méthode** : être **trouvé** (SEO/GEO) → être **lu** (contenu/copy) → être **choisi** (UX/design).
- **Références clients (3)** : Printemps des Arts de Monte-Carlo, Fondation Princesse Charlène de Monaco, Festival L'Èze Harmonies — noms complets, partout.
- **Ne jamais inventer** de mission, client ou résultat : demander les faits à Mikaël avant d'ajouter une référence.
- **Voix de marque / style rédactionnel** : `docs/brand-voice.md` détaille les règles d'écriture (éviter les propositions entassées entre tirets façon anglais, éviter le schéma « ce n'est pas X, c'est Y », éviter de construire un argument en pointant d'abord une mauvaise pratique). À appliquer à tout nouveau texte long (articles de blog, pages, textes clients) et à relire avant publication.

## Projets

Tableau `projectsData` dans le script en bas d'`index.html` :

```js
{
  id: Number, title: String, client: String,
  category: "digital" | "print" | "ux",
  categoryLabel: String,        // badge de la carte
  shortDescription: String,     // carte (3 lignes max)
  longDescription: String,      // modale
  deliverable: String,
  imageUrl: String,             // "images/nom-en-kebab-case.png"
  fallbackUrl: String,          // Unsplash, utilisé en onerror
  gallery: [String],            // >1 image = miniatures dans la modale
}
```

Images dans `images/`, noms en kebab-case sans accent. Le projet L'Èze Harmonies (id 5) utilise une photo réelle du festival (`concert-leze-harmonies.jpg`).

**Règle standing — optimisation des images** : avant de committer toute nouvelle image, la redimensionner (Pillow/`convert`, rééchantillonnage LANCZOS) aux dimensions réelles d'affichage sur le site (jamais plus grande que son plus grand usage — hero, carte, favicon...), garder le PNG seulement si la transparence est nécessaire (sinon JPG pour les photos), et ajouter `loading="lazy"` sur les `<img>` hors above-the-fold. Viser < 50 Ko pour les illustrations, < 15 Ko pour les marks/logos.

## Blog & maillage interne

`blog/calendrier-editorial.md` suit les articles publiés, les idées à venir et la checklist de publication.

Articles dans `blog-articles/*.html`, listés par le tableau `articlesData` en bas de `blog/index.html` (l'ajout d'un article demande une entrée dans ce tableau **et** une `<url>` dans `sitemap.xml`). Catégories : `methode`, `seo-geo`, `contenu`, `ux` — chacune a son bouton de filtre en haut du listing.

**Règle standing — images du blog : ne pas les décrire.** Les visuels d'article (couverture et figures secondaires) sont des illustrations abstraites, présentes pour accompagner le propos, pas pour l'expliquer. Elles ne portent donc aucune description :

- **Pas de `<figcaption>`.** Ne pas ajouter de légende du type « Trois galets, et rien d'autre : chaque élément gardé doit justifier sa place ». Une image qui a besoin d'être commentée n'a pas sa place dans l'article.
- **`alt=""` sur toutes les illustrations d'article** (`images/blog-*`). C'est aussi le traitement correct côté accessibilité : un lecteur d'écran ne gagne rien à entendre « trois plaques de verre superposées », et l'image est alors ignorée proprement.
- **Exceptions**, qui gardent un `alt` réel : les logos (`logo-aencre.png`, logos clients), les captures d'écran de projet et tout schéma qui porte une information absente du texte. Si une image doit vraiment être expliquée, l'expliquer dans le corps du texte, pas en légende.

`trois-piliers-visibilite-conversion.html` est l'**article pilier** : il raconte le narratif trouvé → lu → choisi et sert de plaque tournante du maillage. Tous les autres articles s'y rattachent.

**Règle standing — maillage interne** : à chaque ajout ou suppression d'article, refaire la répartition des liens au lieu de se contenter d'ajouter des liens au nouvel article.

1. **Bloc « À lire aussi »** (fin d'article, 3 cartes) : la répartition doit rester équilibrée, chaque article recevant **le même nombre de cartes entrantes** (3 aujourd'hui). Le motif en place est un anneau de 8 nœuds, `pilier → seo-geo → ai-overviews → seo-local → newsletters → storytelling → design → ux-tunnel`, avec des décalages de +1, +3 et +5. Ces trois décalages étant distincts et non nuls modulo 8, chacun est une permutation de l'anneau, ce qui garantit mathématiquement 3 entrants par article. En cas d'ajout, recalculer l'anneau entier plutôt que rattacher au hasard, et revérifier que les décalages restent distincts et non nuls modulo la nouvelle taille.
2. **Liens contextuels en corps de texte** : chaque article porte, juste après son paragraphe d'introduction, un court paragraphe de rattachement qui pointe vers l'article pilier **et** vers un article voisin de la même famille. Ces liens comptent davantage que les cartes pour le référencement, parce qu'ils sont entourés de texte qui les qualifie.
3. **Ancres descriptives** : le texte du lien décrit le contenu visé (« les tunnels de don et leur friction »), jamais « cliquez ici » ni l'URL brute.
4. **Vérification** : après modification, contrôler qu'aucun article n'a moins de 3 liens entrants et qu'aucun lien ne pointe vers un fichier absent. Un comptage rapide :
   ```bash
   grep -o 'href="[a-z0-9-]*\.html"' blog-articles/*.html | sort | uniq -c | sort -rn
   ```
5. Ne pas empiler les liens : une seule mission du portfolio citée par article (voir `docs/brand-voice.md`), et pas plus de deux liens internes par section de texte.

## SEO

- `<head>` : meta description, canonical, Open Graph/Twitter, JSON-LD `Person` (`sameAs` : LinkedIn + Malt). Tenir aligné avec le positionnement.
- `robots.txt` et `sitemap.xml` à la racine — mettre à jour `<lastmod>` lors de changements de contenu.
- URLs absolues basées sur GitHub Pages ; à remplacer si un domaine perso est acheté.
- **Favicon** : mark de l'ancre sur fond bleu encre, décliné en `images/favicon-{16,32,96}.png`, `images/apple-touch-icon.png` (180×180) et `images/favicon.ico` (48×48). Posé via 5 `<link rel="icon"/apple-touch-icon">` juste après `<title>` sur **toutes** les pages (chemins relatifs à adapter selon la profondeur du dossier). Le PNG 96×96 (ajouté le 29/07/2026) répond aux critères de Google pour l'affichage du favicon dans les résultats de recherche : taille carrée, multiple de 48 px, au moins 48×48 — le favori 32×32 seul en était trop proche. Google ne recrawle et n'affiche ce favicon qu'après avoir réindexé le site ; sur un domaine tout juste migré (`www.mikaelandraos.fr`, 26/07/2026), compter plusieurs jours à quelques semaines avant qu'il apparaisse dans les résultats, indépendamment de la conformité technique.
- **Image Open Graph** : `images/og-image.png` (1200×630) — fond bleu encre, mark de l'ancre en filigrane, nom + positionnement en Gloock/Space Grotesk, et le mot-symbole « Æncre Consulting » (ligature AE du glyphe `Æ` de Gloock) glissé discrètement en coin, teaser du futur nom de marque. Référencée par tous les `og:image`/`twitter:image`/JSON-LD `image`.

## Responsive & menu mobile

Relevé et corrigé lors du QA du 26/07/2026 (mesures Playwright de 320 à 1440 px, 11 pages) :

- **Point de bascule de la navigation : `lg` (1024 px), pas `md`.** L'en-tête complet réclame 834 px ; en basculant à 768 px, il débordait de 66 px pendant que le bouton du menu avait déjà disparu — soit un iPad en portrait sans aucune navigation atteignable. Ne pas ramener ce seuil à `md` sans remesurer. Seul `404.html` reste en `md` : son en-tête ne porte pas les deux appels à l'action et tient dans 744 px.
- **Le panneau du menu vit hors de `<header>`.** L'en-tête porte `backdrop-blur-md`, ce qui en fait le bloc conteneur de ses descendants `fixed` : replacé à l'intérieur, le panneau verrait `top-16 bottom-0` se résoudre dans une bande de 64 px et n'aurait aucune hauteur. Même piège pour tout futur élément `fixed` placé dans l'en-tête.
- **Cibles tactiles** : les règles `@media (pointer: coarse)` de `src/tailwind.css` portent les filtres, le bouton de copie et les liens de contact et de pied de page à 44 px. Elles ne changent rien au rendu à la souris.
- **Bandeau de logos** : le fondu des bords est en pixels (28 px) et non en pourcentage. À 10 %, il mangeait 39 px sur un écran de 390 px, soit la moitié du premier logo.
- Toute nouvelle page reprend le bloc `#mobile-menu` d'`index.html` en adaptant les chemins relatifs, et la logique `setMenu` qui l'accompagne en bas de page.

## Conventions & workflow

- Formulaire de contact : FormSubmit AJAX (`formsubmit.co/ajax/...`), champ `_honey` anti-bot — pas de backend.
- Accessibilité : modale `role="dialog"`/`aria-modal`, `aria-label` sur les boutons d'icônes, `aria-expanded` sur le menu mobile, alt descriptifs sur les images qui portent une information (logos, captures de projet). Les illustrations décoratives du blog font exception : voir la règle ci-dessous.
- `main` est protégée : développer sur une branche, ouvrir une PR. Commits en français, à l'impératif.
- Tenir `TODO.md` à jour ; la routine de synchronisation site/PDF Canva/CV/Behance y est décrite. `docs/behance-kit.md` contient la déclinaison Behance.
