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
- **Typographie** : `Gloock` (serif display — appliqué automatiquement à h1/h2/h3 en graisse 400, ne pas mettre de `font-bold` sur les titres), `Instrument Sans` (texte), `Space Grotesk` (micro-labels — appliqué automatiquement via `.tracking-widest`/`.tracking-wider`/`.font-mono`). `Geist Mono` reste utilisé sur le site principal (`index.html`, `404.html`), mais **seulement** dans le pied de page (sélecteur `footer`), l'encart Méthode de la section À propos (`.method-card`) et les libellés de contact/formulaire (`.label-geist`) — ne pas l'étendre ailleurs sans en discuter avec Mikaël. **Le blog (`blog/index.html` et `blog-articles/*.html`) n'utilise plus Geist Mono du tout** (depuis juillet 2026) : dates, temps de lecture et pied de page y sont tous en Space Grotesk — ne pas le réintroduire dans ces pages.
- **Détails éditoriaux** : filets fins (`h-px`), numéros display, ornement ✳, micro-labels en capitales espacées.
- **Pas de dark mode** : retiré du site (juillet 2026) pour fiabiliser l'affichage — ne pas réintroduire de classes `dark:` ni de bouton de bascule sans en discuter avec Mikaël.

Pas de couleurs vives hors palette, pas d'esthétique « tech/terminal ».

## Contenu & messages

- **Positionnement** : « Stratégie créative et content marketing — SEO/GEO, Contenu et UX ». Aligné partout : `<title>`, metas, JSON-LD `jobTitle`, hero.
- **Narratif de méthode** : être **trouvé** (SEO/GEO) → être **lu** (contenu/copy) → être **choisi** (UX/design).
- **Références clients (3)** : Printemps des Arts de Monte-Carlo, Fondation Princesse Charlène de Monaco, Festival L'Èze Harmonies — noms complets, partout.
- **Ne jamais inventer** de mission, client ou résultat : demander les faits à Mikaël avant d'ajouter une référence.

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
