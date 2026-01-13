# Build to Learn, Learn to Build

A 60-minute, hands-on workshop that helps educators shift from content delivery to building real tools with AI. Participants leave with a working classroom tool they can use immediately and a repeatable workflow they can teach to students.

## Repo structure
- `slides/` — slide decks by date/audience/format
- `materials/` — facilitator guides, worksheets, outlines
- `assets/` — shared images/logos
- `dist/` — built slide outputs (optional)

## Live Slide Decks

- **Illinois Tech (Jan 13, 2026)**: https://vishalsachdev.github.io/build-to-learn/2026-01-13-illinois-tech/
- **Future World Alliance (Jan 9, 2025)**: https://vishalsachdev.github.io/build-to-learn/2025-01-09-future-world-alliance-online/

## Talk Versions

### 2026-01-13: Illinois Tech
- `slides/2026-01-13-illinois-tech/slides.md`
- `materials/2026-01-13-illinois-tech/worksheet.md`

### 2025-01-09: Future World Alliance (Online)
- `slides/2025-01-09-future-world-alliance-online/slides.md`
- `materials/2025-01-09-future-world-alliance-online/run-of-session.md`
- `materials/2025-01-09-future-world-alliance-online/worksheet.md`
- `materials/2025-01-09-future-world-alliance-online/outline.md`
- `materials/2025-01-09-future-world-alliance-online/ad-for-talk.md`
- `materials/2025-01-09-future-world-alliance-online/original-outline.md`

## Run the slides locally
Each version is self-contained. From the version folder:

```bash
cd slides/2026-01-13-illinois-tech
npm install
npm run dev
```

Slidev will print the local URL in the terminal.

## Build / export
```bash
cd slides/2026-01-13-illinois-tech
npm run build
```

Note: Each deck's `build` script sets a versioned base path like `--base /build-to-learn/<deck-slug>/` for GitHub Pages deployment.

## Key links used in the session
- Sketch: https://excalidraw.com
- Build: https://aistudio.google.com
- GitHub Pages: https://pages.github.com
- Free course: https://grow.google/ai-for-educators
- Shared Excalidraw session (create before workshop): [Provide to participants]

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
