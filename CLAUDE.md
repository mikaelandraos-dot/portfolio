# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **single-file static portfolio** for Mikaël Andraos (freelance copywriter & UX designer), written entirely in French. The entire site lives in `index.html` — no build step, no package manager, no framework.

## Development

**Running locally:**
```bash
python3 -m http.server 8000
# then open http://localhost:8000
```
Or open `index.html` directly in a browser — it works without a server.

**There are no build tools, linters, or test suites.** Changes are made directly to `index.html` and previewed in the browser.

## Architecture

Everything is in one file (`index.html`):

- **Tailwind CSS** loaded via CDN with a custom `tailwind.config` (defined inline in a `<script>` tag) that adds `brand.*` colors and the Inter font family.
- **Google Fonts** (Inter) loaded via CDN link.
- **Vanilla JavaScript** (no framework) at the bottom of `<body>`, handling: dark/light theme toggle, mobile menu, project grid rendering, category filtering, modal gallery with keyboard navigation, and contact form submission.
- **Images** are local files in `images/`. Each project entry includes a `fallbackUrl` (Unsplash) used via `onerror` if the local image fails.

## Adding or Editing Projects

All project data lives in the `projectsData` array (around line 351 of `index.html`). Each project object has these fields:

```js
{
  id: Number,           // unique integer
  title: String,        // displayed in card and modal
  client: String,       // displayed as subtitle
  category: String,     // one of: "digital", "print", "ux"
  categoryLabel: String,// human-readable label for the badge
  shortDescription: String,  // shown on the card (line-clamped to 3 lines)
  longDescription: String,   // shown in the modal
  tools: String,        // comma-separated; only first item shown on card
  deliverable: String,  // shown in modal footer
  imageUrl: String,     // path to local image (e.g., "images/foo.png")
  fallbackUrl: String,  // Unsplash URL used if imageUrl fails to load
  gallery: [String],    // array of local image paths; enables prev/next nav in modal if length > 1
}
```

## Key Conventions

- **Language:** All UI text and content is in French.
- **Color system:** Use `brand-500` (`#2563eb`) for primary actions/accents. The Tailwind config defines `brand.50` through `brand.900`.
- **Dark mode:** Toggled by adding/removing the `dark` class on `<html>`. Preference is persisted in `localStorage` under the key `color-theme`. Use `dark:` variant classes for dark mode styles.
- **Layout:** Content is constrained with `max-w-7xl mx-auto px-4 sm:px-6 lg:px-8`.
- **Contact form:** Submits via AJAX to `https://formsubmit.co/ajax/mikael.andraos@gmail.com` — no backend required. The `_honey` hidden field is a bot trap.
- **Accessibility:** Modal uses `role="dialog"` and `aria-modal="true"`. Navigation arrows and close button have `aria-label`. Images have descriptive `alt` text.

## Deployment

The site is intended for GitHub Pages (mentioned in `README.md`). No CI/CD pipeline exists — pushing to the repo is the deployment mechanism.
