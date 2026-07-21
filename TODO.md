# TODO — Portfolio

## 🔴 Priorité haute

- [x] **Remplacer le placeholder L'Èze Harmonies** : le visuel typographique temporaire a été remplacé par une photo réelle du festival (`images/concert-leze-harmonies.jpg`). Les vraies maquettes de refonte / captures avant-après restent à ajouter si Mikaël souhaite enrichir la galerie du projet id 5.
- [ ] **Créer le compte Behance** et réserver le pseudo `mikaelandraos` (le footer, la section contact et le JSON-LD pointent pour l'instant vers Malt — `docs/behance-kit.md` reste prêt pour quand le compte Behance existera).
- [ ] **Vérifier le profil LinkedIn** : le site pointe vers `linkedin.com/in/mikael-andraos` — confirmer que c'est bien le slug public exact.

## 🟠 Priorité moyenne

- [ ] **Favicon** : monogramme « MA » serif (ivoire sur bleu `#1e3a8a`) en `<link rel="icon">`.
- [ ] **Image Open Graph dédiée** : l'og:image actuelle est le portrait ; créer un visuel 1200×630 aux couleurs « Grâce Institutionnelle » avec le positionnement.
- [ ] **Nom de domaine personnalisé** (ex. mikaelandraos.com) : mettre à jour canonical, og:url, JSON-LD, sitemap, et configurer GitHub Pages.
- [ ] **Optimiser les images** : convertir les PNG lourds en WebP (avec fallback) et redimensionner à l'affichage réel.

## 🟢 Améliorations futures

- [ ] Analytics respectueux de la vie privée (Plausible, GoatCounter ou Umami).
- [x] Micro-animations au scroll (IntersectionObserver, apparitions douces) — implémenté (`.reveal-up`, compteur animé sur les statistiques).
- [ ] Page 404 personnalisée pour GitHub Pages.
- [ ] Témoignages clients (citations) si accord des clients.
- [ ] Passer de Tailwind CDN à un build Tailwind CLI (perfs + purge CSS) — seulement si le site grossit.

## 🔁 Routine de synchronisation (à chaque mise à jour de contenu)

Le site est la **source de vérité**. À chaque nouveau projet ou changement de positionnement :

1. Mettre à jour `projectsData` + hero/meta/JSON-LD dans `index.html` (et `<lastmod>` du sitemap).
2. Répercuter sur le **PDF portfolio Canva** (mêmes projets, même phrase de positionnement, mêmes coordonnées).
3. Répercuter sur le **CV** (intitulé identique au jobTitle JSON-LD, mêmes références).
4. Répercuter sur **Behance** (un projet Behance par entrée de `projectsData` — voir `docs/behance-kit.md`).
5. Vérifier que les 4 supports racontent la même histoire avec le même vocabulaire (SEO/GEO, institutions culturelles, marques de prestige).
