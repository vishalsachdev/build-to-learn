# Session Archive

Older session-log entries moved out of `CLAUDE.md` to keep it concise.

### 2026-05-22
- Completed: Exported a fresh LLTLC PDF to Box (added `playwright-chromium` dev dep to that deck for `slidev export`). Built the canonical `slides/_template/` + `materials/_template/` deck (copied from LLTLC, generic-ized) and pointed `npm run new:talk` at it by default; `_template` is skipped in the GH Pages deploy. Added the **live exit-ticket activity**: a facilitator-cue slide ("while participants build, you build a workshop-feedback app in AI Studio") with a ready-to-paste prompt, and reworked the closing Exit Ticket slide from static prompts to workshop-impression questions pointing at the facilitator's live mailto-based app. Spec + plan in `docs/superpowers/`. Committed AGENTS.md and gitignored `.claude/`.
- Next: When the next workshop is scheduled, `new:talk` now scaffolds from `_template` with the exit-ticket activity built in. Facilitator-side: try the live exit-ticket flow at the next delivery to validate the mailto-collection assumption.

### 2026-05-19
- Completed: Delivered LLTLC (rescheduled from May 18). Pre-talk: switched deck to Netlify Drop convention, fixed bottom-of-slide overflow on slides 11+12, added Padlet (go.illinois.edu/lltlc) as single share surface, added phone-photo workflow tip, deployed to GH Pages. During delivery: used AI Studio Share instead of Netlify Drop (simpler, stays in-tool). Two durable lessons captured in auto memory: (1) **AI Studio Share vs Publish** — Publish is a credit-card trap, always direct to Share; (2) **Sketch is the forcing function** — give it 12-15 min and active prompts, never compress.
- Next: No talks queued. When the next workshop is scheduled, apply the new conventions: AI Studio Share primary, longer/guided sketch session, "Why sketch?" slide.

### 2026-04-10
- Completed: Delivered Research Park talk. Captured feedback: CLI demos resonated, "not a coder" framing was the hook, MCP/CLI/skills triad (meeting-prep/debrief example) clicked with audience. Saved talk conventions to auto memory (demo format, folder organization).
- Next: Fill in `materials/2026-research-park-ai-ds/feedback.md`. Prepare LLTLC deck (May 18).
