# Build to Learn, Learn to Build

A 60-minute, hands-on workshop that helps educators shift from content delivery to building real tools with AI. Participants leave with a working classroom tool they can use immediately and a repeatable workflow they can teach to students.

## What this repo contains
- `slides.md`: Slidev deck (primary presentation)
- `outline.md`: Talk track and narrative outline
- `run-of-session.md`: Facilitator run sheet with timing and prompts
- `worksheet.md`: Participant worksheet + resources
- `ad-for-talk.md`: Short abstract/description for promotion
- `images/`: Worksheet screenshots
- `dist/`: Built slide output (if generated)

## Workshop flow (1 hour)
1. The shift and the arc (teachers as builders)
2. Mental models for working with AI
3. Live demo
4. Build session 1: brainstorm in tldraw
5. Build session 2: make it real in AI Studio
6. Publish (optional) + share + reflection

## Run the slides locally
This deck is built with Slidev.

```bash
npm install
npm run dev
```

Slidev will print the local URL in the terminal.

## Build / export
```bash
npm run build
npm run export
```

Note: `npm run build` uses `--base /build-to-learn/` for GitHub Pages.

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
