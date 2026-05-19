# LLTLC Post-Talk Feedback (2026-05-19)

**Event:** Lincoln Legacy Teaching and Learning Community
**Date delivered:** 2026-05-19 11am (rescheduled from 2026-05-18)
**Duration:** 50 min workshop

## Reception
Good reception overall.

## What changed mid-flight
Used **AI Studio's public Share link** instead of Netlify Drop for deployment. Simpler, no extra tool to learn, stays inside the same surface where they built. Audience picked it up faster than a multi-tool workflow would have.

## Critical gotcha (worth remembering forever)
**AI Studio has two confusingly-similar buttons:**
- ✅ **Share** → free public link, anyone can view → this is what we want
- ❌ **Publish** → routes into a credit-card flow → wrong path for a workshop

Tell participants explicitly: "Click **Share**, not Publish." Multiple people will land on Publish by accident and hit the paywall otherwise.

## What worked
- Padlet (go.illinois.edu/lltlc) as single share surface — minimal cognitive load
- "Not a coder" / architect framing
- Theory of Mind framing for AI collaboration
- Pinned posts in Padlet meant minimal verbal-instructions overhead

## What to change for next delivery
- Make AI Studio Share the **primary** deploy path
- Demote Netlify Drop to an optional extension ("for permanence" or "if you want a custom URL")
- Add a warning slide or callout: **"Use Share, not Publish"** with screenshots of both buttons
- Maybe drop GitHub Pages mention entirely from the in-workshop time — it's a follow-up at best

### Sketch session needs more time + more direction (Build Session 1)
- 8 minutes is not enough. Participants need more time **and** more direction during the sketch step.
- Some don't see why they need an image at all — they want to jump straight to text prompting.
- But sketching is a **forcing function for human effort**: it surfaces what you actually want, exposes gaps before you talk to the AI, and resists the "let AI figure it out" tendency. That's the whole pedagogical point — don't compress it away.
- **Next-delivery moves:**
  - Extend Build Session 1 to **12-15 min** (cut equivalently from Mental Models — that section has 7+ slides and can be compressed to the 3 essentials: Theory of Mind, Context Engineering, Architect-Not-Coder)
  - Add a **"Why sketch?"** mini-slide before Build Session 1 making the forcing-function argument explicit ("sketching = thinking; AI can't read minds; ugly is fine")
  - Provide **more directed prompts** during sketching ("circle the most important element", "label what each button does", "add a sticky-note to anything that should be dynamic") — turn it into a guided exercise, not a blank-canvas anxiety moment
  - Walk the room and **prompt individuals by name** during the first 2 minutes — participants who hear someone else get a directive prompt unstick faster

## Action items
- [x] Update slides + run-of-session to reflect Share-primary workflow
- [x] Capture Share-vs-Publish gotcha in auto memory
- [x] Update CLAUDE.md design decisions
