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

LLTLC delivered (rescheduled to May 19). No upcoming talks queued.

## Upcoming Talks

| Date | Event | Slug | Status |
|------|-------|------|--------|
| 2026-02-20 | CITL Workshop (Urbana, IL) | `2026-02-20-citl` | Delivered |
| 2026-04-10 | Research Park Data + AI User Group | `2026-research-park-ai-ds` | Delivered |
| 2026-05-19 | LLTLC (Urbana, IL) | `2026-05-18-lltlc` | Delivered |

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

### AI Studio Share as primary deploy (2026-05-19, LLTLC)
After delivering LLTLC, demoted Netlify Drop to optional extension. **AI Studio's "Share" button** (free public link, in-tool) is now the primary deploy path. Critical gotcha: tell participants to click **Share, not Publish** — Publish opens a credit-card / billing flow. Netlify Drop and GitHub Pages are now "extensions for permanence or custom URLs."

### Sketch session needs ≥12 min + active guidance (2026-05-19, LLTLC)
8-min Build Session 1 was too short and underguided. Participants will try to skip sketching entirely — but sketching is the **forcing function for human effort**, which is the whole pedagogical point. Next decks should: allocate 12-15 min for the sketch step (trim Mental Models), add a "Why sketch?" mini-slide, and give directed prompts ("circle the most important element", "label each button") instead of open ones.

## Post-Talk Feedback

After delivering a talk, fill in `materials/<slug>/feedback.md` with facilitator reflections. Then distill recurring patterns into `INSIGHTS.md` at the repo root. New talks created via `npm run new:talk` automatically get a blank `feedback.md`.

## Session Log

### 2026-05-19
- Completed: Delivered LLTLC (rescheduled from May 18). Pre-talk: switched deck to Netlify Drop convention, fixed bottom-of-slide overflow on slides 11+12, added Padlet (go.illinois.edu/lltlc) as single share surface, added phone-photo workflow tip, deployed to GH Pages. During delivery: used AI Studio Share instead of Netlify Drop (simpler, stays in-tool). Two durable lessons captured in auto memory: (1) **AI Studio Share vs Publish** — Publish is a credit-card trap, always direct to Share; (2) **Sketch is the forcing function** — give it 12-15 min and active prompts, never compress.
- Next: No talks queued. When the next workshop is scheduled, apply the new conventions: AI Studio Share primary, longer/guided sketch session, "Why sketch?" slide.

### 2026-04-10
- Completed: Delivered Research Park talk. Captured feedback: CLI demos resonated, "not a coder" framing was the hook, MCP/CLI/skills triad (meeting-prep/debrief example) clicked with audience. Saved talk conventions to auto memory (demo format, folder organization).
- Next: Fill in `materials/2026-research-park-ai-ds/feedback.md`. Prepare LLTLC deck (May 18).
