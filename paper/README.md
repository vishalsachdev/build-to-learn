# buildtolearn/ — #BuildToLearn / #LearnToBuild position-paper workspace

A layered position paper articulating the philosophy of `#BuildToLearn` and `#LearnToBuild`.
**Gitignored on purpose** — contains real names, draft thesis, and trademark-provenance evidence.

## Reading order
1. `thesis.md` — the canonical ~200-word thesis (every artifact quotes this verbatim).
2. `one-pager.md` — 500–700 words; most distilled form; for trademark counsel / 90-second Dean ask / donor handoff.
3. `deck.md` — 14–18 slides; for the Dean conversation.
4. `essay.md` — 3–5k words; Hybrid Builder publishable + standalone PDF.

Supporting:
- `evidence-base.md` — curated narrative source (articulation moment, pre-couplet practice, the 47 BTL posts, companion concepts, student exemplars).
- `references.md` — learning-theory citations mapped to specific claims.
- `provenance.csv` — first-use / cadence / last-use per protected hashtag, for trademark counsel.
- `corpus.csv` / `corpus.json` — filtered, themed source data.

## Refresh from a new export
1. Unzip the new `Complete_LinkedInDataExport_*` in the repo root.
2. `python3 buildtolearn/extract.py` (auto-detects newest Complete export; or `--export <path>`).
3. Re-do curation; thesis edits ripple to all three artifacts via `thesis.md`.

## Rendering (external tools — none installed by this repo)
- `essay.md` and `one-pager.md` → PDF: `pandoc essay.md -o essay.pdf` (install pandoc separately).
- `deck.md` → HTML/PDF slides: `npx @slidev/cli deck.md` (Slidev) or `npx @marp-team/marp-cli deck.md --pdf` (Marp).

## Design
See `docs/superpowers/specs/2026-05-15-buildtolearn-position-paper-design.md`.

## Tone contract (applies to every artifact here)
- Subject IS you. First-person allowed and expected — you are the articulator of the thesis.
- Claim what's real. Show artifacts (linked); cite theory; name students/faculty for specific contributions.
- Theory is load-bearing, not decorative. Every learning-theory claim cites `references.md`.
- Distinguish facts from arguments. "I built X" is fact, plainly stated. "The philosophy says Y" is argument, defended.
- Praise outward where it's earned — accurate sourcing, not false modesty.
- No stacked superlatives outside verbatim quotes.
- The couplet stays sharp — `#BuildToLearn` and `#LearnToBuild` carry the `thesis.md` definitions everywhere; different examples, same definitions.
- Honest about limits — equity, AI access, assessment integrity, the Credé grit critique.
