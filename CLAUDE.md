# CLAUDE.md — Portfolio Mikaël Andraos

Guidance pour Claude Code (claude.ai/code) sur ce dépôt.

## Vue d'ensemble

Portfolio personnel de Mikaël Andraos — **« Stratégie créative & content marketing — SEO/GEO, Contenu, UX »** — entièrement en français.
Site statique **multi-pages sans build ni framework** : `index.html` (accueil, une seule page), `blog/index.html` (liste des articles, accessible via l'URL `/blog/`), `blog-articles/*.html` (articles individuels) et `404.html` (page d'erreur personnalisée, servie automatiquement par GitHub Pages). Pas de dépendances.
Hébergé sur GitHub Pages : https://mikaelandraos-dot.github.io/portfolio/ — pousser sur `main` déploie.

## Développement

```bash
python3 -m http.server 8000
# puis ouvrir http://localhost:8000
```
Ou ouvrir `index.html` directement. Pas de linter ni de tests — vérifier dans le navigateur : filtres, modale, mobile.

## Design system « Grâce Institutionnelle »

Défini dans la config Tailwind inline et le `<style>` du `<head>` :

- **Bleu encre signature** : `brand-500` = `#1e3a8a` (actions primaires, accents ; hover `brand-600`).
- **Palette chaude** : l'échelle `slate` est **remappée** vers des tons ivoire/anthracite (`slate-50` = `#faf7f1`, etc.) — utiliser les classes `slate-*` habituelles, elles rendent chaud. `.bg-white` est forcé en blanc cassé `#fffdf8`.
- **Typographie** : `Gloock` (serif display — appliqué automatiquement à h1/h2/h3 en graisse 400, ne pas mettre de `font-bold` sur les titres), `Instrument Sans` (texte), `Space Grotesk` (micro-labels — appliqué automatiquement via `.tracking-widest`/`.tracking-wider`/`.font-mono`). `Geist Mono` reste utilisé dans le pied de page (sélecteur `footer`) de **toutes** les pages, y compris le blog. Sur le site principal (`index.html`, `404.html`), il est aussi réservé à l'encart Méthode de la section À propos (`.method-card`) et aux libellés de contact/formulaire (`.label-geist`) — ne pas l'étendre ailleurs sans en discuter avec Mikaël. **Dans le blog (`blog/index.html` et `blog-articles/*.html`), en dehors du pied de page, Geist Mono n'est plus utilisé** (depuis juillet 2026) : les micro-labels en majuscules (catégories, sommaire) restent en Space Grotesk, mais les dates, temps de lecture et signature d'auteur (`.font-mono` hors `tracking-wider`/`tracking-widest`) sont en Instrument Sans, comme le reste du texte.
- **Détails éditoriaux** : filets fins (`h-px`), numéros display, ornement ✳, micro-labels en capitales espacées.
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

Articles dans `blog-articles/*.html`, listés par le tableau `articlesData` en bas de `blog/index.html` (l'ajout d'un article demande une entrée dans ce tableau **et** une `<url>` dans `sitemap.xml`). Catégories : `methode`, `seo-geo`, `contenu`, `ux` — chacune a son bouton de filtre en haut du listing.

`trois-piliers-visibilite-conversion.html` est l'**article pilier** : il raconte le narratif trouvé → lu → choisi et sert de plaque tournante du maillage. Tous les autres articles s'y rattachent.

**Règle standing — maillage interne** : à chaque ajout ou suppression d'article, refaire la répartition des liens au lieu de se contenter d'ajouter des liens au nouvel article.

1. **Bloc « À lire aussi »** (fin d'article, 3 cartes) : la répartition doit rester équilibrée, chaque article recevant **le même nombre de cartes entrantes** (3 aujourd'hui). Le motif en place est un anneau `pilier → seo-geo → seo-local → newsletters → storytelling → design → ux-tunnel` avec des décalages de +1, +3 et +5, ce qui garantit mathématiquement 3 entrants par article. En cas d'ajout, recalculer plutôt que rattacher au hasard.
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
- **Favicon** : mark de l'ancre sur fond bleu encre, décliné en `images/favicon-{16,32,48}.png`, `images/apple-touch-icon.png` (180×180) et `images/favicon.ico`. Posé via 4 `<link rel="icon"/apple-touch-icon">` juste après `<title>` sur **toutes** les pages (chemins relatifs à adapter selon la profondeur du dossier).
- **Image Open Graph** : `images/og-image.png` (1200×630) — fond bleu encre, mark de l'ancre en filigrane, nom + positionnement en Gloock/Space Grotesk, et le mot-symbole « Æncre Consulting » (ligature AE du glyphe `Æ` de Gloock) glissé discrètement en coin, teaser du futur nom de marque. Référencée par tous les `og:image`/`twitter:image`/JSON-LD `image`.

## Conventions & workflow

- Formulaire de contact : FormSubmit AJAX (`formsubmit.co/ajax/...`), champ `_honey` anti-bot — pas de backend.
- Accessibilité : modale `role="dialog"`/`aria-modal`, `aria-label` sur les boutons d'icônes, `aria-expanded` sur le menu mobile, alt descriptifs.
- `main` est protégée : développer sur une branche, ouvrir une PR. Commits en français, à l'impératif.
- Tenir `TODO.md` à jour ; la routine de synchronisation site/PDF Canva/CV/Behance y est décrite. `docs/behance-kit.md` contient la déclinaison Behance.
