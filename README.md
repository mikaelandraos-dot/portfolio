# Portfolio — Mikaël Andraos

**Stratégie créative & content marketing — SEO/GEO, Contenu et UX**, pour institutions culturelles et marques de prestige.

🔗 **Site en ligne :** https://mikaelandraos-dot.github.io/portfolio/

## Références présentées

- Printemps des Arts de Monte-Carlo — réseaux sociaux, newsletters & storytelling culturel
- Fondation Princesse Charlène de Monaco — supports print institutionnels, UX du tunnel de don
- Festival L'Èze Harmonies — refonte UX & optimisation SEO

## Sous le capot

- Site statique **une seule page** (`index.html`) : aucun build, aucune dépendance.
- Tailwind CSS (CDN) + Google Fonts (Gloock, Instrument Sans, Geist Mono).
- Design system « **Grâce Institutionnelle** » : bleu encre `#1e3a8a`, palette ivoire chaude, typographie éditoriale serif — documenté dans [CLAUDE.md](CLAUDE.md).
- Dark mode, filtres de projets, galerie modale, formulaire de contact (FormSubmit) — JavaScript vanilla.
- SEO/GEO : meta, Open Graph, canonical, JSON-LD `Person`, `robots.txt` et `sitemap.xml`.

## Développement

```bash
python3 -m http.server 8000
# puis ouvrir http://localhost:8000
```

Les projets se modifient dans le tableau `projectsData` en bas d'`index.html`. Les images vont dans `images/` (kebab-case, sans accent).

Voir [TODO.md](TODO.md) pour les chantiers en cours et [docs/behance-kit.md](docs/behance-kit.md) pour la déclinaison Behance.

## Contact

- ✉️ mikael.andraos@gmail.com
- [LinkedIn](https://linkedin.com/in/mikael-andraos) · [Behance](https://www.behance.net/mikaelandraos)
