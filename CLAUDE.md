## Project: build-to-learn

This repo is a “talk factory” for Slidev decks + facilitation materials, designed so each talk can be duplicated with small edits and then deployed to GitHub Pages for sharing.

### Structure
- `slides/<deck-slug>/` — a self-contained Slidev project (has its own `package.json`)
- `materials/<deck-slug>/` — run-of-session, worksheet, outline, etc.
- `assets/` — shared images/logos
- GitHub Pages publishes each deck at `/<deck-slug>/` under the repo site.

### Create a new talk (duplicate + rebase for Pages)

Pick a slug like `YYYY-MM-DD-org-format` (lowercase, hyphens).

```bash
# creates slides/<slug>/ and materials/<slug>/ by copying from a template
npm run new:talk -- --slug 2026-01-13-my-event --session "My Event (Online)" --date 2026-01-13
```

Options:
- `--from <template-slug>`: copy from a specific existing deck (defaults to the newest slug under `slides/`)
- `--dry-run`: show what would happen without writing files
- `--force`: overwrite an existing destination (use carefully)

What it does:
- Copies `slides/<template>/` → `slides/<slug>/` (excluding `node_modules/`, `dist/`, `.slidev/`)
- Copies `materials/<template>/` → `materials/<slug>/` (if present)
- Sets `slides/<slug>/package.json` build script to `slidev build --base /build-to-learn/<slug>/`
- Updates the deck’s `README.md` URL/session/date (when present)

### Run a deck locally
```bash
cd slides/<deck-slug>
npm install
npm run dev
```

### Build a deck
```bash
cd slides/<deck-slug>
npm run build
```

### Deploy
Push to `main`. The GitHub Actions workflow builds every deck under `slides/*` and publishes them to GitHub Pages.

---

## Current Focus

Research Park deck delivered. Next up: LLTLC (May 18).

## Upcoming Talks

| Date | Event | Slug | Status |
|------|-------|------|--------|
| 2026-02-20 | CITL Workshop (Urbana, IL) | `2026-02-20-citl` | Delivered |
| 2026-04-10 | Research Park Data + AI User Group | `2026-research-park-ai-ds` | Delivered |
| 2026-05-18 | LLTLC (Urbana, IL) | `2026-05-18-lltlc` | Proposal submitted |

## Design Decisions

### Ideation speed problem (2026-01-22)
Participants struggle to ideate what to build from scratch. Solutions implemented:
1. **Screenshot + Remix** as the fastest default path — take a screenshot of any website/PDF/app, paste into Excalidraw, annotate with changes, upload to AI Studio
2. **Paper sketch + phone photo** as a low-friction alternative to digital sketching
3. **Three paths** instead of one: Screenshot+Remix (fastest), Pick a Template, Solve Your Pain Point

### Output constraint (2026-01-22)
Restricted to **single HTML+JS page** with inline CSS/JS, no external dependencies, vanilla JS only.

### Chat mode + Netlify Drop (2026-02-16)
Switched from AI Studio Build mode (generates React) to **Chat mode** (generates single HTML files). Replaced GitHub Pages as primary deploy with **Netlify Drop** (drag & drop, live in seconds). GitHub Pages kept as optional "for permanence" follow-up.

## Post-Talk Feedback

After delivering a talk, fill in `materials/<slug>/feedback.md` with facilitator reflections. Then distill recurring patterns into `INSIGHTS.md` at the repo root. New talks created via `npm run new:talk` automatically get a blank `feedback.md`.

## Session Log

### 2026-04-10
- Completed: Delivered Research Park talk. Captured feedback: CLI demos resonated, "not a coder" framing was the hook, MCP/CLI/skills triad (meeting-prep/debrief example) clicked with audience. Saved talk conventions to auto memory (demo format, folder organization).
- Next: Fill in `materials/2026-research-park-ai-ds/feedback.md`. Prepare LLTLC deck (May 18).
