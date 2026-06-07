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

By default it copies from the canonical `slides/_template/` deck (the most refined deck — AI Studio Share, guided sketch session, live exit-ticket activity). `_template` is excluded from GitHub Pages deploy.

Options:
- `--from <template-slug>`: copy from a different existing deck instead of `_template`
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

No upcoming talks queued. Canonical `slides/_template/` deck now exists — `new:talk` copies from it by default.

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

### 2026-06-07
- Completed: Full v2 revision pass on `paper/position-paper.md` across 6 commits (all pushed; gist `312a9f4` kept in sync — that's the public link sent to Sara Barnett for her §3c quote). Closed all reviewer action items: Jason Mock's §4 rigor edits (§4.1 recursion, §4.2 viva shelf-life, §4.3 AI-skill→fluency variance, §4.4 motivation-cost + Eccles&Wigfield/Hidi&Renninger, §2.2 recursive/learner-judged termination); Sahib/Amber reach additions (§1 pervasiveness lead, new §2.6 career-readiness + workforce-transferability-as-bet); Nathan Yang's failure-learning track (new §2.5 Fishbach/Eskreis-Winkler + Woolley + Kapur-consolidation). Added Grit-CART canonical reference (newsletter + repo) and normalized the §2.3 trajectory to C-A-R-T. Reframed literacy→**fluency** (Resnick 2002). Corrected pre-couplet timeline (MakerLab 2013, Digital Making course 2015, IS/OM practicum=BADM 372 since Fall 2022, BADM 350 tech-strategy pivot 2025), credited Dan McCreary, MSBAi→MSBA. Ran a **Codex editorial review** and applied 9 edits (overclaim audit, §4.1 assessable-surfaces reframe, US `judgment` spelling). Separately: refreshed **canvas-mcp** impact stats (142★, PyPI 503/mo, npm 69/mo), deployed to canvas-mcp.illinihunt.org, **hardened the PyPI fetch** (3× retry + last-good guard, fixing silent `curl -sf`→0 corruption) and cleaned 3 bad history points.
- Next: (1) **Aaron Bennett's distribution decision** — white paper for peer deans vs. 3–4 mainstream Gies-site pieces (packaging, not content); (2) **§3c Sara Barnett quote** still pending (email sent; placeholder stays — don't ship dean-facing until it lands). All other feedback items closed. Codex flagged §5-length + references-pruning but both deferred ("working paper, change at final publishing"). See `paper/feedback.md`.

*Older entries archived to `docs/session-archive.md`*
