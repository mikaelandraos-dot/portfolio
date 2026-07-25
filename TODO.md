# TODO — Portfolio

## 🔴 Priorité haute

- [x] **Remplacer le placeholder L'Èze Harmonies** : le visuel typographique temporaire a été remplacé par une photo réelle du festival (`images/concert-leze-harmonies.jpg`). Les vraies maquettes de refonte / captures avant-après restent à ajouter si Mikaël souhaite enrichir la galerie du projet id 5.
- [ ] **Créer le compte Behance** et réserver le pseudo `mikaelandraos` (le footer, la section contact et le JSON-LD pointent pour l'instant vers Malt — `docs/behance-kit.md` reste prêt pour quand le compte Behance existera).
- [x] **Vérifier le profil LinkedIn + Malt** : slugs publics (`linkedin.com/in/mikael-andraos`, `malt.fr/profile/mikaelandraos`) confirmés par Mikaël.

## 🟠 Priorité moyenne

- [x] **Favicon** : mark de l'ancre (teaser du futur logo/nom de marque Aencre Consulting) décliné en plusieurs tailles (`favicon.ico`, 16/32/48, `apple-touch-icon` 180×180), posé sur toutes les pages.
- [x] **Image Open Graph dédiée** : `images/og-image.png` (1200×630, couleurs « Grâce Institutionnelle », positionnement + « AEncre » en ligature AE) posée sur toutes les pages.
- [ ] **Nom de domaine personnalisé** (ex. mikaelandraos.com) : mettre à jour canonical, og:url, JSON-LD, sitemap, et configurer GitHub Pages.
- [x] **Optimiser les images** : redimensionner les PNG/JPG à l'affichage réel avant de les committer (voir règle ci-dessous) — appliqué au logo, à la photo L'Èze Harmonies, aux visuels de projets, aux photos du poste de travail et aux images du blog.
- [x] **Bandeau logos « Ils m'ont fait confiance »** : bandeau défilant implémenté dans `index.html` (composant piloté par `trustedByData`, comme `projectsData`), avec les 5 logos prévus — Printemps des Arts de Monte-Carlo, Fondation Princesse Charlène de Monaco, festival L'Èze Harmonies, Musée Océanographique de Monaco, Office de Tourisme Métropolitain (Explore Nice Côte d'Azur) — chacun pointant vers son site officiel (nouvel onglet). Prêt à recevoir Audiovista et March on Mars le moment venu.
- [x] **Ajouter page FAQ** : `faq.html` — bio courte + photo en encart rond en hero, puis FAQ en accordéons (même format que les articles du blog) organisée en 3 groupes : le métier en clair (stratégie de contenu, SEO/GEO, content marketing, stratège créatif, UX/UI), positionnement (institutions culturelles, remote), missions & tarifs (TJM freelance, démarrage). Schéma FAQPage en JSON-LD, lien ajouté à la nav de toutes les pages + sitemap.
- [ ] **Trouver un emploi à `images/blog-social-media-strategy.jpg`** : visuel fourni en juillet, aucun article ne traite aujourd'hui de stratégie social media.
- [ ] **Enrichir les visuels des projets** : ajouter aux galeries de `projectsData` des visuels réseaux sociaux et des photos de coulisses (travail en cours, making-of) pour les projets existants.
- [x] **Illustrer la méthodologie** : carte « Mon poste de travail » ajoutée à la section Compétences (fond bleu neutre, une photo du poste de travail de Mikaël apparaît au survol/tap parmi 3, au hasard) ; illustration bleu/or (`blog-brushstroke-ornament.png`) posée en fond discret dans la FAQ et la section À propos du site principal.
- [x] **Illustrer le blog** : photo de couverture sous le titre pour les 6 articles, seconde image après le glossaire pour 3 d'entre eux (newsletters/AIDA, SEO & GEO, tunnel de don UX), et photo de couverture (stylo plume) sur la page de listing `blog/index.html`.
- [x] **Article pilier « trois piliers »** : `blog-articles/trois-piliers-visibilite-conversion.html` publié le 25/07/2026 — il raconte le narratif trouvé → lu → choisi, sert de plaque tournante du maillage interne et introduit la catégorie « Méthode » dans le filtre du listing.
- [x] **Maillage interne refondu** (25/07/2026) : chaque article reçoit exactement 3 cartes entrantes (motif en anneau documenté dans `CLAUDE.md`), et chaque article porte un paragraphe de rattachement contextuel vers le pilier et vers un article voisin. Avant refonte, `design-sobriete` et `storytelling` n'avaient qu'un seul lien entrant chacun.
- [x] **Note de collecte études de cas** : `docs/etudes-de-cas.md` — métriques à relever par client, trame de l'étude de cas FPCM, informations manquantes et voies pour obtenir des témoignages.
- [x] **Textes anglais accueil + FAQ** : `docs/traduction-en.md`, en relecture. Le blog reste en français.
- [x] **Portrait animé de la FAQ** : la photo statique laisse place à une vidéo au survol (ou au tap sur mobile), avec fondu long + flou/zoom qui se dissipent pour adoucir la coupure de pose, et démarrage du fondu conditionné à `readyState`/`canplay` pour éviter tout flash au chargement.

### Règle standing : optimisation des images

Pour toute nouvelle image ajoutée au site :
1. Redimensionner (Pillow/`convert`, LANCZOS) aux dimensions réelles d'affichage (pas de PNG/JPG plus grand que son plus grand usage sur le site — hero, carte de projet, favicon, etc.).
2. Garder le PNG uniquement si la transparence est nécessaire (logos, marks) ; sinon préférer le JPG pour les photos.
3. Toujours ajouter `loading="lazy"` sur les `<img>` hors above-the-fold.
4. Vérifier le poids final (viser < 50 Ko pour les images d'illustration, < 15 Ko pour les marks/logos).

## 🟢 Améliorations futures

- [x] **Core Web Vitals — `width`/`height` sur les images** (25/07/2026) : les 50 `<img>` locales du site portent désormais leurs dimensions intrinsèques, ce qui laisse le navigateur réserver la place avant le chargement et supprime le décalage de mise en page (CLS).
- [ ] Analytics respectueux de la vie privée (Plausible, GoatCounter ou Umami).
- [x] Micro-animations au scroll (IntersectionObserver, apparitions douces) — implémenté (`.reveal-up`, compteur animé sur les statistiques).
- [x] Page 404 personnalisée pour GitHub Pages — `404.html`, ancre échouée sur le rivage.
- [ ] Témoignages clients (citations) si accord des clients.
- [ ] **Passer de Tailwind CDN à un build Tailwind CLI** (perfs + purge CSS). C'est aujourd'hui le principal frein aux Core Web Vitals : `cdn.tailwindcss.com` compile les classes dans le navigateur au chargement, ce qui retarde le premier rendu sur toutes les pages. Tailwind déconseille lui-même ce mode en production. À traiter avant toute autre optimisation de performance.
  **Chantier planifié et chiffré dans `docs/tailwind-build.md`** (25/07/2026) : 5 étapes, une PR par étape. Compilation testée sur le site réel, la feuille complète pèse **6,6 Ko en gzip**. Point à trancher avant de commencer : commiter le CSS compilé (option A, simple mais oubli possible) ou compiler dans GitHub Actions (option B, recommandée, change la façon dont Pages publie le site).
  - [ ] Étape 1 — outillage (`package.json`, `tailwind.config.js`, `src/tailwind.css`), sans toucher aux pages
  - [ ] Étape 2 — mutualiser le `<style>` recopié sur les 11 pages
  - [ ] Étape 3 — basculer les 11 pages du `<script>` CDN vers `<link rel="stylesheet">`
  - [ ] Étape 4 — publication (option A ou B)
  - [ ] Étape 5 — mesure PageSpeed avant/après
- [ ] **Auto-héberger les Google Fonts** — second poste de latence après le CDN Tailwind : quatre familles chargées depuis un domaine tiers en tête de page. À envisager une fois le build Tailwind en place, pas avant.

---

# 💡 Pistes d'amélioration — design, ergonomie & contenu

Revue faite le 25 juillet 2026, une fois les chantiers visuels terminés. Classée par
rapport impact / effort. Les points marqués **⚠️** sont des correctifs (quelque chose
ne respecte pas une règle déjà posée), le reste sont des propositions.

## 🔴 P1 — À traiter en priorité

### 1. ✅ Alléger les médias — fait le 25/07/2026

Le dossier `images/` est passé de **3,5 Mo à 1,7 Mo (−51 %)** :

- Supprimé `images/mikael-andraos.png` (1,2 Mo), qui n'était plus utilisé nulle part — le
  portrait réellement affiché est `mikael-andraos-portrait.jpg` (26 Ko). La référence
  périmée de `docs/behance-kit.md` a été corrigée.
- Supprimé `images/favicon-48.png`, orphelin (seuls les 16 et 32 px sont posés en
  `<link rel="icon">`).
- Converti 8 captures d'écran de PNG en JPG et redimensionnées à 900 px (la modale
  projet plafonne à 768 px) : `landing-printemps-des-arts` 372→80 Ko,
  `page-dons-fpcm` 280→75 Ko, `arborescence-site-fpcm` 157→62 Ko, les 3 newsletters
  et les 2 pages du rapport FPCM dans la même passe.

**Reste à arbitrer — la vidéo du portrait (3,8 Mo)** : elle est en `preload="none"`, donc
elle ne pénalise pas le chargement initial de la FAQ, mais elle reste lourde pour un effet
de survol. Deux options : la ré-encoder plus court/plus compressé (viser < 1,5 Mo), ou la
servir en WebM en plus du MP4.

### 2. Ajouter des témoignages clients

C'est **le levier de conversion le plus manquant** aujourd'hui. Le site montre le travail
et le raisonnement, mais aucune voix extérieure ne valide la collaboration. Trois citations
courtes (2–3 lignes) avec nom, fonction et institution suffiraient — placées entre le
bandeau de logos et la section Projets, ou juste avant le formulaire de contact.

Bloque sur un préalable : il faut l'accord écrit des clients. En attendant, une variante
plus facile à obtenir : une **recommandation LinkedIn** existante, citée et liée vers le
profil (avec accord).

### 3. ✅ Rafraîchir le `<lastmod>` du sitemap — fait le 25/07/2026

Les dates sont figées aux 21–22 juillet alors que le contenu a bougé les 24 et 25. La
routine de synchronisation le prévoit déjà, mais ça n'a pas été fait sur les derniers lots.
À intégrer systématiquement — ou à automatiser via une petite GitHub Action.

## 🟠 P2 — Fort intérêt, effort modéré

### 4. Passer d'une galerie de projets à de vraies études de cas

Aujourd'hui, chaque projet tient dans une modale : contexte, livrables, quelques visuels.
C'est propre, mais ça reste du « voici ce que j'ai produit ». Pour un positionnement de
**stratège** (et pas d'exécutant), il manque le raisonnement : quel était le problème,
qu'est-ce qui a été décidé et pourquoi, qu'est-ce que ça a changé.

Le format existe déjà sur le site : les articles de blog font exactement ça. Une page
d'étude de cas par projet phare (2 ou 3 suffisent), sur le même gabarit que les articles,
serait la suite logique — avec un lien « Lire l'étude de cas » depuis la modale.

**Prérequis absolu** : ne rien inventer. Les chiffres de résultat doivent venir de Mikaël
(ou être remplacés par des observations qualitatives assumées comme telles).

### 5. Rendre la carte « Mon poste de travail » lisible sur mobile

Sur desktop l'effet de survol est découvrable par accident. Sur mobile, rien n'indique
que la carte est tapable — elle ressemble à un simple bloc bleu. Un discret « Touchez pour
voir » (ou une icône) dans l'état neutre réglerait le problème sans alourdir le design.

### 6. ⚠️ Deux correctifs d'accessibilité

- **Aucune page n'a de lien d'évitement** (« Aller au contenu principal »). Sur des pages
  avec un header fixe et une nav complète, c'est le premier réflexe attendu au clavier.
- **Une miniature de galerie n'a pas d'`alt`** (`index.html:784`, les vignettes de la
  modale projet). Les autres images du site sont correctement décrites — c'est un oubli
  isolé, corrigeable en une ligne.

### 7. ❌ Un flux RSS pour le blog — écarté le 25/07/2026

Six articles publiés, un rythme régulier : le blog est assez mûr pour être suivi. Un
`feed.xml` statique (généré à la main ou par script) coûte peu et sert deux publics — les
lecteurs fidèles, et les agrégateurs qui alimentent les moteurs génératifs.

## 🟢 P3 — À considérer plus tard

### 8. ✅ Pousser plus loin les données structurées — fait le 25/07/2026

Le site fait déjà bien le travail (`Person`, `FAQPage`, `BlogPosting`). Trois ajouts qui
seraient à la fois utiles et démonstratifs pour quelqu'un qui vend du SEO/GEO :

- `BreadcrumbList` sur les articles (fil d'Ariane visible + balisé).
- `Service` ou `OfferCatalog` sur la page d'accueil, pour décrire les prestations en
  langage machine.
- `author` enrichi sur les `BlogPosting` (lien vers la page FAQ comme page d'auteur), ce
  qui renforce le signal E-E-A-T.

Les trois sont en place :

- `BreadcrumbList` sur les 7 articles, avec un fil d'Ariane **visible** (Accueil / Blog /
  catégorie) qui remplace l'ancien lien « Tous les articles ».
- `OfferCatalog` sur la page d'accueil, greffé au `Person` : les 4 prestations décrites en
  langage machine, sans prix, avec `areaServed` Monaco + France.
- `author` enrichi sur les `BlogPosting` : `url` pointe vers la FAQ comme page d'auteur,
  avec `jobTitle` et `sameAs` (LinkedIn, Malt) — signal E-E-A-T.

S'y ajoutent 2 questions sur les prestations dans le `FAQPage`. Argument de vente
accessoire : le site devient sa propre démonstration.

### 9. ✅ Une section « Prestations » explicite — fait le 25/07/2026

La FAQ répond au « comment je travaille » et les Compétences listent les savoir-faire,
mais un visiteur pressé ne trouve nulle part une réponse frontale à « qu'est-ce que je
peux vous acheter ? ». Trois formats nommés (par exemple : audit ponctuel /
accompagnement éditorial / refonte UX) clarifieraient l'entrée en relation, sans avoir à
afficher de tarifs.

Arbitrages de Mikaël le 25/07/2026 : quatre formats (audit ponctuel, accompagnement
éditorial, refonte UX / site, stratégie complète), section placée entre Compétences et
Contact, **aucune indication de prix**, et chaque carte décrit les livrables puis le
déroulé. Lien « Prestations » ajouté à la navigation des 11 pages. Traduction anglaise
dans `docs/traduction-en.md`.

### 10. Bloc auteur en fin d'article

Les articles se terminent sur les sources et « À lire aussi ». Un court bloc auteur
(portrait, une phrase, lien FAQ + Malt) capitaliserait sur la lecture pour ramener vers
le cœur du site — et renforce le signal d'expertise côté SEO/GEO.

### 11. 🚧 Version anglaise — en cours

Périmètre arrêté le 25/07/2026 : accueil + FAQ seulement, le blog reste en français
(traduire 7 articles doublerait la maintenance à chaque mise à jour, pour un gain
incertain tant qu'aucune demande internationale ne s'est manifestée).

Les textes traduits sont dans `docs/traduction-en.md`, en attente de relecture par
Mikaël, section Prestations comprise. L'intégration (pages `en/`, `hreflang`, canonical, sitemap, sélecteur
de langue) ne démarre qu'une fois les textes validés.

### 12. Bouton « haut de page » sur les pages longues

Il existe sur l'accueil (via le logo du pied de page). Les articles de blog font 350 à
530 lignes et n'en ont pas — un bouton flottant apparaissant au scroll serait cohérent
avec la barre de progression de lecture déjà en place.

---

## 🔁 Routine de synchronisation (à chaque mise à jour de contenu)

Le site est la **source de vérité**. À chaque nouveau projet ou changement de positionnement :

1. Mettre à jour `projectsData` + hero/meta/JSON-LD dans `index.html` (et `<lastmod>` du sitemap).
2. Répercuter sur le **PDF portfolio Canva** (mêmes projets, même phrase de positionnement, mêmes coordonnées).
3. Répercuter sur le **CV** (intitulé identique au jobTitle JSON-LD, mêmes références).
4. Répercuter sur **Behance** (un projet Behance par entrée de `projectsData` — voir `docs/behance-kit.md`).
5. Vérifier que les 4 supports racontent la même histoire avec le même vocabulaire (SEO/GEO, institutions culturelles, marques de prestige).
