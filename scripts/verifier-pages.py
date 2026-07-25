#!/usr/bin/env python3
"""Vérifications du site avant publication.

Reprend les contrôles qui étaient faits à la main : HTML bien formé, JSON-LD
valide, liens internes et images qui existent, feuille de style compilée
présente, et respect des règles standing du blog (pas de légende sous les
illustrations, alt vide).

Usage : python3 scripts/verifier-pages.py
Sortie : code 0 si tout passe, 1 sinon (ce qui fait échouer le workflow).
"""

from __future__ import annotations

import glob
import html.parser
import json
import os
import re
import sys
from urllib.parse import unquote, urlparse

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
erreurs: list[str] = []


def pages() -> list[str]:
    motifs = ('*.html', 'blog/*.html', 'blog-articles/*.html')
    trouvees: list[str] = []
    for motif in motifs:
        trouvees += glob.glob(os.path.join(RACINE, motif))
    return sorted(os.path.relpath(p, RACINE) for p in trouvees)


class VerificateurHTML(html.parser.HTMLParser):
    """Signale les balises de structure non refermées."""

    A_FERMER = {'html', 'head', 'body', 'main', 'section', 'article',
                'header', 'footer', 'nav', 'div', 'ul', 'ol', 'figure'}

    def __init__(self) -> None:
        super().__init__()
        self.pile: list[tuple[str, int]] = []

    def handle_starttag(self, tag, attrs):
        if tag in self.A_FERMER:
            self.pile.append((tag, self.getpos()[0]))

    def handle_endtag(self, tag):
        if tag in self.A_FERMER:
            for i in range(len(self.pile) - 1, -1, -1):
                if self.pile[i][0] == tag:
                    del self.pile[i]
                    return


def verifier(fichier: str) -> None:
    chemin = os.path.join(RACINE, fichier)
    with open(chemin, encoding='utf-8') as f:
        source = f.read()
    dossier = os.path.dirname(chemin)

    # -- HTML bien formé ----------------------------------------------------
    verif = VerificateurHTML()
    try:
        verif.feed(source)
    except Exception as exc:                                  # pragma: no cover
        erreurs.append(f'{fichier} : HTML illisible ({exc})')
    for tag, ligne in verif.pile:
        erreurs.append(f'{fichier}:{ligne} : <{tag}> jamais refermée')

    # -- JSON-LD ------------------------------------------------------------
    blocs = re.findall(r'<script type="application/ld\+json">(.*?)</script>',
                       source, re.S)
    for i, bloc in enumerate(blocs, 1):
        try:
            json.loads(bloc)
        except json.JSONDecodeError as exc:
            erreurs.append(f'{fichier} : JSON-LD n°{i} invalide ({exc})')

    # -- Feuille de style compilée -----------------------------------------
    if 'cdn.tailwindcss.com' in source:
        erreurs.append(f'{fichier} : référence au CDN Tailwind restée en place')
    if not re.search(r'<link rel="stylesheet" href="[^"]*assets/site\.css">', source):
        erreurs.append(f'{fichier} : la feuille assets/site.css n\'est pas liée')

    # -- Images et liens internes ------------------------------------------
    for src in re.findall(r'<img[^>]+src="([^"]+)"', source):
        if src.startswith(('http://', 'https://', 'data:')) or '${' in src:
            continue
        if not os.path.isfile(os.path.join(dossier, unquote(src))):
            erreurs.append(f'{fichier} : image absente -> {src}')

    for href in re.findall(r'<a[^>]+href="([^"]+)"', source):
        if href.startswith(('http://', 'https://', 'mailto:', 'tel:', '#')) or '${' in href:
            continue
        cible = unquote(urlparse(href).path)
        if not cible:
            continue
        chemin_cible = os.path.normpath(os.path.join(dossier, cible))
        if os.path.isdir(chemin_cible):
            chemin_cible = os.path.join(chemin_cible, 'index.html')
        if not os.path.exists(chemin_cible):
            erreurs.append(f'{fichier} : lien mort -> {href}')

    # -- Règles standing du blog -------------------------------------------
    if fichier.startswith(('blog/', 'blog-articles/')):
        if '<figcaption' in source:
            erreurs.append(
                f'{fichier} : légende sous une image. Les illustrations du blog '
                f'ne se décrivent pas (voir CLAUDE.md).')
        for balise in re.findall(r'<img[^>]+>', source):
            src_match = re.search(r'src="([^"]+)"', balise)
            alt_match = re.search(r'alt="([^"]*)"', balise)
            if not src_match:
                continue
            src = src_match.group(1)
            if 'images/blog-' not in src:
                continue
            if alt_match is None or alt_match.group(1).strip():
                erreurs.append(
                    f'{fichier} : l\'illustration {os.path.basename(src)} doit '
                    f'porter alt="" (voir CLAUDE.md).')
        if not re.search(r'<body[^>]+data-site="blog"', source):
            erreurs.append(
                f'{fichier} : <body> sans data-site="blog" ; la règle de police '
                f'du blog ne s\'appliquera pas.')


def main() -> int:
    liste = pages()
    if not liste:
        print('Aucune page trouvée.', file=sys.stderr)
        return 1

    for fichier in liste:
        verifier(fichier)

    if not os.path.isfile(os.path.join(RACINE, 'assets', 'site.css')):
        erreurs.append('assets/site.css absent : lancer `npm run build`.')

    if erreurs:
        print(f'{len(erreurs)} problème(s) :\n', file=sys.stderr)
        for e in erreurs:
            print(f'  - {e}', file=sys.stderr)
        return 1

    print(f'{len(liste)} pages vérifiées, rien à signaler.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
