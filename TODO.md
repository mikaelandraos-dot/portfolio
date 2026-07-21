# TODO — Portfolio

## 🔴 Priorité haute

- [x] **Remplacer le placeholder L'Èze Harmonies** : le visuel typographique temporaire a été remplacé par une photo réelle du festival (`images/concert-leze-harmonies.jpg`). Les vraies maquettes de refonte / captures avant-après restent à ajouter si Mikaël souhaite enrichir la galerie du projet id 5.
- [ ] **Créer le compte Behance** et réserver le pseudo `mikaelandraos` (le footer, la section contact et le JSON-LD pointent pour l'instant vers Malt — `docs/behance-kit.md` reste prêt pour quand le compte Behance existera).
- [x] **Vérifier le profil LinkedIn + Malt** : slugs publics (`linkedin.com/in/mikael-andraos`, `malt.fr/profile/mikaelandraos`) confirmés par Mikaël.

## 🟠 Priorité moyenne

- [x] **Favicon** : mark de l'ancre (teaser du futur logo/nom de marque Aencre Consulting) décliné en plusieurs tailles (`favicon.ico`, 16/32/48, `apple-touch-icon` 180×180), posé sur toutes les pages.
- [x] **Image Open Graph dédiée** : `images/og-image.png` (1200×630, couleurs « Grâce Institutionnelle », positionnement + « AEncre » en ligature AE) posée sur toutes les pages.
- [ ] **Nom de domaine personnalisé** (ex. mikaelandraos.com) : mettre à jour canonical, og:url, JSON-LD, sitemap, et configurer GitHub Pages.
- [x] **Optimiser les images** : redimensionner les PNG/JPG à l'affichage réel avant de les committer (voir règle ci-dessous) — appliqué au logo et à la photo L'Èze Harmonies.

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

## 🔁 Routine de synchronisation (à chaque mise à jour de contenu)

Le site est la **source de vérité**. À chaque nouveau projet ou changement de positionnement :

1. Mettre à jour `projectsData` + hero/meta/JSON-LD dans `index.html` (et `<lastmod>` du sitemap).
2. Répercuter sur le **PDF portfolio Canva** (mêmes projets, même phrase de positionnement, mêmes coordonnées).
3. Répercuter sur le **CV** (intitulé identique au jobTitle JSON-LD, mêmes références).
4. Répercuter sur **Behance** (un projet Behance par entrée de `projectsData` — voir `docs/behance-kit.md`).
5. Vérifier que les 4 supports racontent la même histoire avec le même vocabulaire (SEO/GEO, institutions culturelles, marques de prestige).
