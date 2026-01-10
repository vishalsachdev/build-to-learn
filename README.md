# Build to Learn, Learn to Build

A 60-minute, hands-on workshop that helps educators shift from content delivery to building real tools with AI. Participants leave with a working classroom tool they can use immediately and a repeatable workflow they can teach to students.

## Repo structure
- `slides/` — slide decks by date/audience/format
- `materials/` — facilitator guides, worksheets, outlines
- `assets/` — shared images/logos
- `dist/` — built slide outputs (optional)

## Current version
- `slides/2025-01-09-future-world-alliance-online/slides.md`
- `materials/2025-01-09-future-world-alliance-online/run-of-session.md`
- `materials/2025-01-09-future-world-alliance-online/worksheet.md`
- `materials/2025-01-09-future-world-alliance-online/outline.md`
- `materials/2025-01-09-future-world-alliance-online/ad-for-talk.md`
- `materials/2025-01-09-future-world-alliance-online/original-outline.md`

## Run the slides locally
Each version is self-contained. From the version folder:

```bash
cd slides/2025-01-09-future-world-alliance-online
npm install
npm run dev
```

Slidev will print the local URL in the terminal.

## Build / export
```bash
cd slides/2025-01-09-future-world-alliance-online
npm run build
npm run export
```

Note: This version builds with `--base /build-to-learn/2025-01-09-future-world-alliance-online/` for GitHub Pages.

## Key links used in the session
- Brainstorm: https://makereal.tldraw.com
- Build: https://aistudio.google.com
- GitHub Pages: https://pages.github.com
- Free course: https://grow.google/ai-for-educators
- Shared doc (fill in before session): https://go.illinois.edu/buildtolearn

## Facilitation tips
- Bring 1-2 real demo artifacts to show prompt evolution.
- Emphasize iteration over perfection.
- Push for a live URL to create accountability.
- End with a concrete next step: one lesson where students build.

## Contact
- vishal@illinois.edu
- https://chatwithgpt.substack.com/
- https://www.linkedin.com/in/vishalsachdev
- https://github.com/vishalsachdev
