# Template Deck + Live Exit-Ticket Activity — Design

**Date:** 2026-05-20
**Repo:** build-to-learn

## Goal

1. Create a canonical `template` deck so `npm run new:talk` copies from a stable
   source instead of "whichever slug sorts last".
2. Add a live exit-ticket-app activity to that template: while participants build
   in AI Studio, the facilitator builds a workshop-feedback app the same way —
   modeling the workflow and producing the feedback channel.

## Part 1 — Canonical `template` deck

- Copy `slides/2026-05-18-lltlc/` → `slides/template/` (exclude `node_modules/`,
  `dist/`, `.slidev/`). LLTLC is the most refined deck — latest conventions
  (AI Studio Share, longer guided sketch).
- Copy `materials/2026-05-18-lltlc/` → `materials/template/`.
- Generic-ize LLTLC specifics in the copies:
  - Session title → generic placeholder.
  - Date → generic placeholder.
  - Padlet URL `go.illinois.edu/lltlc` → `go.illinois.edu/YOUR-EVENT`.
  - `slides/template/package.json` build script → `--base /build-to-learn/template/`.
- `scripts/new-talk.mjs` line 163: change `opts.from ?? slugs.at(-1)` to
  `opts.from ?? 'template'`. The `--from <slug>` override still works.

**Known trade-off:** the GitHub Actions workflow builds every `slides/*`, so
`template` will also publish at `/build-to-learn/template/`. Acceptable — it acts
as a live reference deck. Excluding it from the workflow is optional follow-up.

## Part 2 — Live exit-ticket activity (template deck only)

### New facilitator-cue slide

Inserted after "Remember: Iterate", before the CLOSING divider.

- Title: "Facilitator: Build the Exit Ticket — Live"
- Body: while participants build, the facilitator builds a workshop-feedback app
  in AI Studio; it models the workflow and becomes the feedback channel. When
  done: Share → copy link → put on closing slide / Padlet.
- Carries the ready-to-paste AI Studio prompt (facilitator swaps in their email):

  > "Generate a single HTML file, inline CSS + JS, no external libraries — a
  > workshop exit-ticket form. Fields: overall rating (1–5 stars), 'What worked /
  > what clicked', 'What you'd change', 'What will you build — or have your
  > students build — in the next 2 weeks?', and an optional name. A Submit button
  > opens a pre-filled email to `[your-email@example.edu]` with all answers in the
  > body. Clean, mobile-friendly."

### Replace the static "Exit Ticket" slide

Current slide = 3 static prompt cards (clicked / fuzzy / what will you build).
New slide = the workshop-impression questions plus a pointer to the live app the
facilitator built: "Open the link, submit your exit ticket." Keeps the 🚀
"what will you build in 2 weeks" prompt as the final field.

### Materials

Add the build-session facilitator step (build the exit-ticket app) to
`materials/template/run-of-session.md`.

## Out of scope

- No `exit-ticket.html` starter file — facilitator builds it live from the prompt.
- Collection is the `mailto:` Submit button — no backend, honest single-HTML
  AI Studio artifact. Facilitator receives N separate emails.
- No changes to the existing LLTLC / Research Park / other delivered decks.
