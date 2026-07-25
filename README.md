# Portfolio — Mikaël Andraos

**Stratégie créative & content marketing — SEO/GEO, Contenu et UX**, pour institutions culturelles et marques de prestige.

🔗 **Site en ligne :** https://mikaelandraos-dot.github.io/portfolio/

## Références présentées

- Printemps des Arts de Monte-Carlo — réseaux sociaux, newsletters & storytelling culturel
- Fondation Princesse Charlène de Monaco — supports print institutionnels, UX du tunnel de don
- Festival L'Èze Harmonies — refonte UX & optimisation SEO/GEO

## Structure

Site statique **multi-pages**, sans build ni framework, sans dépendance :

| Fichier / dossier | Rôle |
| --- | --- |
| `index.html` | Accueil : hero, à propos & méthode, projets (modale + filtres), compétences, contact |
| `faq.html` | Qui suis-je + FAQ en accordéons, portrait animé au survol |
| `blog/index.html` | Liste des articles (filtres par catégorie), servie sur `/blog/` |
| `blog-articles/*.html` | Les 6 articles, avec sommaire, barre de progression et glossaire |
| `404.html` | Page d'erreur personnalisée, servie automatiquement par GitHub Pages |
| `images/` · `videos/` | Médias (kebab-case, sans accent) |
| `docs/` | `brand-voice.md` (règles d'écriture) et `behance-kit.md` (déclinaison Behance) |

## Sous le capot

- Tailwind CSS (CDN, config inline dupliquée par page) + Google Fonts (Gloock, Instrument Sans, Space Grotesk, Geist Mono).
- Design system « **Grâce Institutionnelle** » : bleu encre `#1e3a8a`, échelle `slate` remappée en tons ivoire chauds, typographie éditoriale serif — documenté dans [CLAUDE.md](CLAUDE.md).
- **Pas de dark mode** (retiré en juillet 2026 pour fiabiliser l'affichage).
- JavaScript vanilla : filtres de projets, galerie modale, bandeau de logos défilant, compteurs animés, révélations au scroll, portrait vidéo au survol, formulaire de contact (FormSubmit, sans backend).
- SEO/GEO : meta, Open Graph/Twitter, canonical, JSON-LD (`Person`, `FAQPage`, `BlogPosting`), `robots.txt` et `sitemap.xml`.

## Développement

```bash
python3 -m http.server 8000
# puis ouvrir http://localhost:8000
```

Pas de linter ni de tests : vérifier dans le navigateur (filtres, modale, mobile).

- Les projets se modifient dans le tableau `projectsData`, en bas d'`index.html`.
- Les logos du bandeau « Ils m'ont fait confiance » se modifient dans `trustedByData`, juste en dessous.
- Toute nouvelle image doit passer par la **règle standing d'optimisation** décrite dans [TODO.md](TODO.md) (redimensionner à la taille d'affichage réelle, JPG pour les photos, `loading="lazy"` hors above-the-fold).
- Tout nouveau texte long doit respecter [docs/brand-voice.md](docs/brand-voice.md).

`main` est protégée : développer sur une branche, ouvrir une PR. Commits en français, à l'impératif.

Voir [TODO.md](TODO.md) pour les chantiers en cours et les pistes d'amélioration priorisées.

## Contact

- ✉️ mikael.andraos@gmail.com
- [LinkedIn](https://linkedin.com/in/mikael-andraos) · [Malt](https://www.malt.fr/profile/mikaelandraos)
