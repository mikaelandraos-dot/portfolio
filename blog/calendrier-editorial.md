# Calendrier éditorial — Blog

Suivi de la publication des articles du blog (`/blog/`). Cadence visée : 1 à 2 articles par mois. Cochez au fur et à mesure ; ajoutez vos idées de posts LinkedIn sous chaque article publié.

---

## ✅ Publiés (7)

- [x] **De la visibilité à la conversion : les trois piliers d'une présence en ligne** — 🏛️ **article pilier**
  Catégorie : Méthode · Publié le 25/07/2026 · [En ligne](https://mikaelandraos-dot.github.io/portfolio/blog-articles/trois-piliers-visibilite-conversion.html)
  - [ ] Idée post LinkedIn n°1 :
  - [ ] Idée post LinkedIn n°2 :

- [x] **Design d'interface et sobriété : pourquoi le minimalisme inspire confiance**
  Catégorie : UX & Design · Publié le 21/07/2026 · [En ligne](https://mikaelandraos-dot.github.io/portfolio/blog-articles/design-sobriete-confiance.html)
  - [ ] Idée post LinkedIn n°1 :
  - [ ] Idée post LinkedIn n°2 :

- [x] **Storytelling de marque : raconter une histoire sans jamais sonner pompeux**
  Catégorie : Contenu & Copy · Publié le 21/07/2026 · [En ligne](https://mikaelandraos-dot.github.io/portfolio/blog-articles/storytelling-marque-sans-pompeux.html)
  - [ ] Idée post LinkedIn n°1 :
  - [ ] Idée post LinkedIn n°2 :

- [x] **Le SEO local : dominer les résultats de recherche près de chez soi**
  Catégorie : SEO & GEO · Publié le 21/07/2026 · [En ligne](https://mikaelandraos-dot.github.io/portfolio/blog-articles/seo-local-institutions-culturelles.html)
  - [ ] Idée post LinkedIn n°1 :
  - [ ] Idée post LinkedIn n°2 :

- [x] **SEO & GEO : comment être trouvé par Google ET par l'intelligence artificielle**
  Catégorie : SEO & GEO · Publié le 12/07/2026 · [En ligne](https://mikaelandraos-dot.github.io/portfolio/blog-articles/seo-geo-institutions-culturelles.html)
  - [ ] Idée post LinkedIn n°1 :
  - [ ] Idée post LinkedIn n°2 :

- [x] **Newsletters qui convertissent : la méthode AIDA appliquée à la culture**
  Catégorie : Contenu & Copy · Publié le 05/07/2026 · [En ligne](https://mikaelandraos-dot.github.io/portfolio/blog-articles/newsletters-methode-aida.html)
  - [ ] Idée post LinkedIn n°1 :
  - [ ] Idée post LinkedIn n°2 :

- [x] **UX et tunnels de don : réduire la friction sans perdre l'émotion**
  Catégorie : UX & Design · Publié le 28/06/2026 · [En ligne](https://mikaelandraos-dot.github.io/portfolio/blog-articles/ux-tunnel-don-friction.html)
  - [ ] Idée post LinkedIn n°1 :
  - [ ] Idée post LinkedIn n°2 :

---

## 🕓 À venir (idées non écrites)

### Contenu & Copy

- [ ] **Éditorial : moins, mais mieux**
  Angle : stratégie éditoriale « qualité plutôt que quantité » — calendrier éditorial réaliste pour une petite équipe, sans jargon.
  Date proposée : 25/08/2026

### Méthode & Stratégie

- [ ] **Context engineering pour les créatifs : produire plus vite, sans perdre en qualité**
  Angle : comment structurer ses prompts/contextes IA pour accélérer l'idéation et la rédaction sans sacrifier la justesse.
  Date proposée : 22/09/2026

### SEO & GEO

- [ ] **Stratégie social media : ce que les réseaux apportent vraiment à la visibilité**
  Angle : la place des réseaux sociaux dans le pilier « être trouvé », et ce qu'ils ne remplacent pas. Le visuel `images/blog-social-media-strategy.jpg` attend cet article depuis juillet 2026.
  Date proposée : à caler

---

## Notes

### Catégories du blog

Quatre catégories, chacune avec son bouton de filtre en haut du listing : **Méthode** (`methode`), **SEO & GEO** (`seo-geo`), **Contenu & Copy** (`contenu`), **UX & Design** (`ux`). La catégorie Méthode a été créée en juillet 2026 pour accueillir l'article pilier, qui traverse les trois autres.

### Checklist d'un nouvel article

Chaque nouvel article doit :

- citer ses sources (lien direct vers l'étude ou l'organisme) ;
- inclure un petit glossaire des termes techniques introduits ;
- proposer une FAQ en accordéons ;
- citer **une seule** mission concrète du portfolio, pour le maillage interne ;
- porter des visuels **sans légende ni description** : pas de `<figcaption>`, `alt=""` sur les illustrations (elles accompagnent le propos, elles ne l'expliquent pas) ;
- être ajouté au tableau `articlesData` dans `blog/index.html` **et** au `sitemap.xml` ;
- porter un `BlogPosting` en JSON-LD et un `BreadcrumbList`.

### Maillage interne

**La répartition des liens se recalcule à chaque ajout ou suppression d'article**, elle ne s'improvise pas. Les règles complètes (motif en anneau, comptage des liens entrants, ancres descriptives) sont dans `CLAUDE.md`, section « Blog & maillage interne ».

État au 25/07/2026 : chaque article reçoit exactement **3 cartes entrantes** et **2 liens contextuels entrants**. L'article pilier en totalise 9. Vérification rapide :

```bash
grep -o 'href="[a-z0-9-]*\.html"' blog-articles/*.html | sort | uniq -c | sort -rn
```

### Règle de cadrage (depuis juillet 2026)

Éviter de trop insister sur « institutions culturelles, fondations, festivals » dans le corps des articles — le positionnement reste vrai mais n'a pas besoin d'être rappelé à chaque paragraphe. Généraliser les exemples (« une organisation », « une structure locale »...) sauf pour **un** rappel de mission concret par article, qui reste bienvenu pour le maillage interne. Les statistiques/recherches générales, glossaires et FAQ restent le cœur de chaque article.

### Répartition des liens vers les projets

À équilibrer sur la durée : L'Èze Harmonies (SEO & GEO, SEO local), Printemps des Arts de Monte-Carlo (Newsletters AIDA, Storytelling), Fondation Princesse Charlène de Monaco (UX tunnels de don, Design & sobriété) — 2 articles chacun à ce jour. L'article pilier ne cite aucune mission en particulier, ce qui est cohérent avec son rôle de plaque tournante.

### Divers

- Les dates proposées suivent une cadence d'environ 2 à 4 semaines à partir du dernier article publié — à ajuster librement.
- Une fois un article rédigé, cochez-le dans la section « Publiés » et déplacez-le hors de « À venir ».
- Les articles sont rédigés directement en HTML dans `blog-articles/`. Il n'y a pas de fichiers Markdown intermédiaires versionnés dans le dépôt.
- Voix de marque et règles d'écriture : `docs/brand-voice.md`, à relire avant publication.
