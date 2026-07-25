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
- [ ] **Enrichir les visuels des projets** : ajouter aux galeries de `projectsData` des visuels réseaux sociaux et des photos de coulisses (travail en cours, making-of) pour les projets existants.
- [x] **Illustrer la méthodologie** : carte « Mon poste de travail » ajoutée à la section Compétences (fond bleu neutre, une photo du poste de travail de Mikaël apparaît au survol/tap parmi 3, au hasard) ; illustration bleu/or (`blog-brushstroke-ornament.png`) posée en fond discret dans la FAQ et la section À propos du site principal.
- [x] **Illustrer le blog** : photo de couverture sous le titre pour les 6 articles, seconde image après le glossaire pour 3 d'entre eux (newsletters/AIDA, SEO & GEO, tunnel de don UX), et photo de couverture (stylo plume) sur la page de listing `blog/index.html`.
- [x] **Portrait animé de la FAQ** : la photo statique laisse place à une vidéo au survol (ou au tap sur mobile), avec fondu long + flou/zoom qui se dissipent pour adoucir la coupure de pose, et démarrage du fondu conditionné à `readyState`/`canplay` pour éviter tout flash au chargement.

### Règle standing : optimisation des images

Pour toute nouvelle image ajoutée au site :
1. Redimensionner (Pillow/`convert`, LANCZOS) aux dimensions réelles d'affichage (pas de PNG/JPG plus grand que son plus grand usage sur le site — hero, carte de projet, favicon, etc.).
2. Garder le PNG uniquement si la transparence est nécessaire (logos, marks) ; sinon préférer le JPG pour les photos.
3. Toujours ajouter `loading="lazy"` sur les `<img>` hors above-the-fold.
4. Vérifier le poids final (viser < 50 Ko pour les images d'illustration, < 15 Ko pour les marks/logos).

## 🟢 Améliorations futures

- [ ] Analytics respectueux de la vie privée (Plausible, GoatCounter ou Umami).
- [x] Micro-animations au scroll (IntersectionObserver, apparitions douces) — implémenté (`.reveal-up`, compteur animé sur les statistiques).
- [x] Page 404 personnalisée pour GitHub Pages — `404.html`, ancre échouée sur le rivage.
- [ ] Témoignages clients (citations) si accord des clients.
- [ ] Passer de Tailwind CDN à un build Tailwind CLI (perfs + purge CSS) — seulement si le site grossit.

---

# 💡 Pistes d'amélioration — design, ergonomie & contenu

Revue faite le 25 juillet 2026, une fois les chantiers visuels terminés. Classée par
rapport impact / effort. Les points marqués **⚠️** sont des correctifs (quelque chose
ne respecte pas une règle déjà posée), le reste sont des propositions.

## 🔴 P1 — À traiter en priorité

### 1. ⚠️ Alléger les médias (correctif, effort faible, gain immédiat)

Le dossier `images/` pèse 3,5 Mo et `videos/` 3,8 Mo. Trois problèmes concrets :

- **`images/mikael-andraos.png` (1,2 Mo) n'est plus utilisé nulle part** dans le site — le
  portrait réellement affiché est `mikael-andraos-portrait.jpg` (26 Ko). Le fichier n'est
  plus référencé que par `docs/behance-kit.md`. À supprimer (et corriger la référence dans
  le kit Behance) : **−34 % sur le poids du dossier images** pour une ligne de commande.
- **`images/favicon-48.png` est orphelin** : seuls les 16 et 32 px sont posés dans les
  `<link rel="icon">`. Soit l'ajouter, soit le supprimer.
- **5 images dépassent largement la règle des 50 Ko** : `landing-printemps-des-arts.png`
  (376 Ko), `page-dons-fpcm.png` (284 Ko), `arborescence-site-fpcm.png` (160 Ko),
  `pda-instagram-2026.jpg` (112 Ko), `newsletter-printemps-3.png` (92 Ko). Ce sont des
  captures d'écran en PNG : les repasser en JPG (ou WebP) les ramènerait sous les 60 Ko
  sans perte visible.

**Sur la vidéo (3,8 Mo)** : elle est en `preload="none"`, donc elle ne pénalise pas le
chargement initial de la FAQ — mais elle reste lourde pour un effet de survol. Deux
options : la ré-encoder plus court/plus compressé (viser < 1,5 Mo), ou la servir en WebM
en plus du MP4. À arbitrer selon l'importance qu'on donne à l'effet.

### 2. Ajouter des témoignages clients

C'est **le levier de conversion le plus manquant** aujourd'hui. Le site montre le travail
et le raisonnement, mais aucune voix extérieure ne valide la collaboration. Trois citations
courtes (2–3 lignes) avec nom, fonction et institution suffiraient — placées entre le
bandeau de logos et la section Projets, ou juste avant le formulaire de contact.

Bloque sur un préalable : il faut l'accord écrit des clients. En attendant, une variante
plus facile à obtenir : une **recommandation LinkedIn** existante, citée et liée vers le
profil (avec accord).

### 3. ⚠️ Rafraîchir le `<lastmod>` du sitemap

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

### 7. Un flux RSS pour le blog

Six articles publiés, un rythme régulier : le blog est assez mûr pour être suivi. Un
`feed.xml` statique (généré à la main ou par script) coûte peu et sert deux publics — les
lecteurs fidèles, et les agrégateurs qui alimentent les moteurs génératifs.

## 🟢 P3 — À considérer plus tard

### 8. Pousser plus loin les données structurées (cohérence avec le positionnement GEO)

Le site fait déjà bien le travail (`Person`, `FAQPage`, `BlogPosting`). Trois ajouts qui
seraient à la fois utiles et démonstratifs pour quelqu'un qui vend du SEO/GEO :

- `BreadcrumbList` sur les articles (fil d'Ariane visible + balisé).
- `Service` ou `OfferCatalog` sur la page d'accueil, pour décrire les prestations en
  langage machine.
- `author` enrichi sur les `BlogPosting` (lien vers la page FAQ comme page d'auteur), ce
  qui renforce le signal E-E-A-T.

Argument de vente accessoire : le site devient sa propre démonstration.

### 9. Une section « Prestations » explicite

La FAQ répond au « comment je travaille » et les Compétences listent les savoir-faire,
mais un visiteur pressé ne trouve nulle part une réponse frontale à « qu'est-ce que je
peux vous acheter ? ». Trois formats nommés (par exemple : audit ponctuel /
accompagnement éditorial / refonte UX) clarifieraient l'entrée en relation, sans avoir à
afficher de tarifs.

### 10. Bloc auteur en fin d'article

Les articles se terminent sur les sources et « À lire aussi ». Un court bloc auteur
(portrait, une phrase, lien FAQ + Malt) capitaliserait sur la lecture pour ramener vers
le cœur du site — et renforce le signal d'expertise côté SEO/GEO.

### 11. Version anglaise

À envisager seulement si Mikaël vise des marques de prestige hors francophonie. C'est un
chantier lourd (duplication de toutes les pages + `hreflang`) : à ne lancer que si une
demande réelle apparaît, pas par anticipation.

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
