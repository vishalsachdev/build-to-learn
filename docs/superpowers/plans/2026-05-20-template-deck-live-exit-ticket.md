# Template Deck + Live Exit-Ticket Activity Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create a canonical `slides/_template/` deck that `npm run new:talk` copies from, and add a live exit-ticket-app activity to it.

**Architecture:** Copy the LLTLC deck (most refined) into `slides/_template/` + `materials/_template/`, generic-ize event-specific content, add a facilitator-cue slide and rework the closing Exit Ticket slide, and point `new-talk.mjs` at the new template by default.

**Tech Stack:** Slidev 0.50, Node ESM script (`scripts/new-talk.mjs`), GitHub Actions deploy.

> **Naming note — deviation from spec:** The spec said `slides/template/`. The template folder is named **`_template`** (leading underscore) instead. Reason: `new-talk.mjs`'s `replaceInMarkdownFiles` does a blind `contents.replaceAll(templateSlug, newSlug)` across every `.md` file. The word "template" appears as ordinary content in the deck (`titleTemplate:`, "Pick a Template", "Starter prompt template") — a `template` slug would corrupt all of it. `_template` never appears in prose, so the replace stays safe.

---

## File Structure

- `slides/_template/` — new canonical deck (copy of LLTLC deck, generic-ized + edited)
- `materials/_template/` — new canonical materials (copy of LLTLC materials, generic-ized + edited)
- `scripts/new-talk.mjs` — modify line 163 default template
- `.github/workflows/deploy.yml` — modify build loop to skip `_template`

---

## Task 1: Create the `_template` deck and materials by copying LLTLC

**Files:**
- Create: `slides/_template/` (from `slides/2026-05-18-lltlc/`)
- Create: `materials/_template/` (from `materials/2026-05-18-lltlc/`)

- [ ] **Step 1: Copy the slides deck, excluding build artifacts**

```bash
cd /Users/vishal/teaching/talks/build-to-learn
rsync -a --exclude node_modules --exclude dist --exclude .slidev --exclude slides.pdf \
  slides/2026-05-18-lltlc/ slides/_template/
```

- [ ] **Step 2: Copy the materials**

```bash
rsync -a materials/2026-05-18-lltlc/ materials/_template/
```

- [ ] **Step 3: Remove the carried-over post-talk feedback file**

`feedback.md` is LLTLC-specific reflections — the template should ship a blank one. `new-talk.mjs` does not auto-create it, so reset it to a blank stub.

```bash
cat > materials/_template/feedback.md <<'EOF'
# Post-Talk Feedback

Fill in after delivering this talk. Distill recurring patterns into the repo-root `INSIGHTS.md`.

## What worked

## What to change

## Audience reactions

## Notes for next time
EOF
```

- [ ] **Step 4: Verify the copy**

Run: `ls slides/_template && ls materials/_template`
Expected: `slides/_template` shows `package.json README.md slides.md`; `materials/_template` shows the 7 material `.md` files. No `node_modules/` or `slides.pdf` under `slides/_template`.

- [ ] **Step 5: Commit**

```bash
git add slides/_template materials/_template
git commit -m "chore: scaffold _template deck from LLTLC deck"
```

---

## Task 2: Generic-ize event-specific identifiers in `_template`

Replace the LLTLC slug, event name, date, and Padlet URL so the template carries placeholders.

**Files:**
- Modify: `slides/_template/package.json`
- Modify: `slides/_template/README.md`
- Modify: `slides/_template/slides.md`
- Modify: files under `materials/_template/`

- [ ] **Step 1: Replace the deck slug string everywhere in `_template`**

`new-talk.mjs` replaces the *template slug string* in `.md` files when scaffolding a new talk. The template's own files must therefore contain `_template`, not `2026-05-18-lltlc`.

```bash
grep -rl '2026-05-18-lltlc' slides/_template materials/_template \
  | xargs sed -i '' 's#2026-05-18-lltlc#_template#g'
```

- [ ] **Step 2: Set the build base path in `package.json`**

In `slides/_template/package.json`, change the `build` script value to:

```json
"build": "slidev build --base /build-to-learn/_template/",
```

- [ ] **Step 3: Generic-ize `slides/_template/README.md` header**

Replace the session/date lines (currently `**Session:** Lincoln Legacy...` / `**Date:** 2026-05-18`) with:

```markdown
**Session:** TEMPLATE — replace when scaffolding via `npm run new:talk`
**Date:** YYYY-MM-DD
```

(The `/build-to-learn/_template/` URL is already correct after Step 1.)

- [ ] **Step 4: Generic-ize the title-slide event line in `slides.md`**

In `slides/_template/slides.md`, the title-slide block contains:

```html
  <div class="mt-6 text-xl font-semibold text-blue-500 dark:text-blue-300">
    LLTLC · May 19, 2026
  </div>
```

Change the inner text to:

```html
  <div class="mt-6 text-xl font-semibold text-blue-500 dark:text-blue-300">
    YOUR EVENT · MONTH DAY, YEAR
  </div>
```

- [ ] **Step 5: Generic-ize the Padlet short URL**

`go.illinois.edu/lltlc` appears in `slides/_template/slides.md` (two places), `materials/_template/padlet-content.md`, and `materials/_template/feedback.md` was reset in Task 1 so skip it. Replace across the template:

```bash
grep -rl 'go.illinois.edu/lltlc' slides/_template materials/_template \
  | xargs sed -i '' 's#go.illinois.edu/lltlc#go.illinois.edu/YOUR-EVENT#g'
```

- [ ] **Step 6: Verify no LLTLC-specific identifiers remain**

Run: `grep -rn 'lltlc\|LLTLC\|2026-05-18\|May 19, 2026' slides/_template materials/_template`
Expected: no matches (exit code 1). If any remain, generic-ize them.

- [ ] **Step 7: Commit**

```bash
git add slides/_template materials/_template
git commit -m "chore: generic-ize _template deck (slug, event, date, Padlet URL)"
```

---

## Task 3: Add the facilitator-cue slide to the `_template` deck

Insert a new slide after the "Remember: Iterate" slide and before the `CLOSING` divider slide.

**Files:**
- Modify: `slides/_template/slides.md`

- [ ] **Step 1: Locate the insertion point**

Run: `grep -n 'Remember: Iterate\|CLOSING' slides/_template/slides.md`
Expected: two lines — `# Remember: Iterate` and a `<div ...>CLOSING` line a few lines below it, separated by a `---`.

- [ ] **Step 2: Insert the facilitator slide**

In `slides/_template/slides.md`, find the slide separator `---` that sits immediately *before* the `CLOSING` slide's `<div ...>` block. Insert this complete slide (followed by its own `---`) so it becomes a slide between "Remember: Iterate" and "CLOSING":

```markdown
# 🛠️ Facilitator: Build the Exit Ticket — Live

<div class="text-lg opacity-80 mb-4">While participants build, you build too — model the exact workflow <em>and</em> create your feedback channel.</div>

<div class="grid grid-cols-2 gap-6 my-5">

<div class="p-5 bg-blue-50 dark:bg-blue-900 rounded-xl">
<div class="text-3xl mb-2">1️⃣</div>
<div class="font-bold mb-1">Open AI Studio → Chat</div>
<div class="text-sm">Paste the prompt below. Iterate if needed.</div>
</div>

<div class="p-5 bg-emerald-50 dark:bg-emerald-900 rounded-xl">
<div class="text-3xl mb-2">2️⃣</div>
<div class="font-bold mb-1">Share → copy the link</div>
<div class="text-sm">Drop it on the Exit Ticket slide / Padlet so participants can submit.</div>
</div>

</div>

<div class="p-4 bg-yellow-50 dark:bg-yellow-900 rounded-xl border-l-8 border-yellow-500">
<div class="font-bold text-sm mb-1">📋 Paste into AI Studio Chat (swap in your email):</div>
<div class="font-mono text-xs leading-relaxed">Generate a single HTML file — inline CSS + JS, no external libraries — a workshop exit-ticket form. Fields: overall rating (1–5 stars), "What worked / what clicked", "What you'd change", "What will you build — or have your students build — in the next 2 weeks?", and an optional name. A Submit button opens a pre-filled email to your-email@example.edu with all answers in the body. Clean, mobile-friendly.</div>
</div>

---
```

- [ ] **Step 3: Verify slide count and structure**

Run: `grep -n 'Facilitator: Build the Exit Ticket' slides/_template/slides.md`
Expected: exactly one match, positioned (by line number) after `# Remember: Iterate` and before the `CLOSING` div.

- [ ] **Step 4: Commit**

```bash
git add slides/_template/slides.md
git commit -m "feat: add facilitator-cue slide for live exit-ticket build"
```

---

## Task 4: Replace the static Exit Ticket slide in the `_template` deck

Convert the 3-static-prompt Exit Ticket slide into a workshop-impression slide that points at the live app the facilitator built.

**Files:**
- Modify: `slides/_template/slides.md`

- [ ] **Step 1: Locate the current Exit Ticket slide**

Run: `grep -n 'Exit Ticket' slides/_template/slides.md`
Expected: the `# Exit Ticket` heading line (plus the Task 3 facilitator slide line). The slide body is everything from `# Exit Ticket` down to the next `---` separator.

- [ ] **Step 2: Replace the slide body**

Replace the entire `# Exit Ticket` slide (from the `# Exit Ticket` heading through to — but not including — the next `---` separator) with:

```markdown
# Exit Ticket

<div class="text-lg opacity-80 mb-4">Two minutes — open the link your facilitator shared and submit.</div>

<div class="space-y-3 my-4">

<div class="p-3 bg-gradient-to-r from-yellow-100 to-orange-100 dark:from-yellow-900 dark:to-orange-900 rounded-xl border-l-8 border-yellow-500">
<div class="text-lg font-bold">⭐ How was the workshop? (rate 1–5)</div>
</div>

<div class="p-3 bg-gradient-to-r from-blue-100 to-emerald-100 dark:from-blue-900 dark:to-emerald-900 rounded-xl border-l-8 border-blue-500">
<div class="text-lg font-bold">💡 What worked — what clicked</div>
</div>

<div class="p-3 bg-gradient-to-r from-pink-100 to-rose-100 dark:from-pink-900 dark:to-rose-900 rounded-xl border-l-8 border-pink-500">
<div class="text-lg font-bold">🔧 What you'd change</div>
</div>

<div class="p-3 bg-gradient-to-r from-green-100 to-teal-100 dark:from-green-900 dark:to-teal-900 rounded-xl border-l-8 border-green-500">
<div class="text-lg font-bold">🚀 What will you build — or have your students build — in the next 2 weeks?</div>
</div>

</div>

<div class="mt-4 p-3 bg-gradient-to-r from-blue-100 to-emerald-100 dark:from-blue-900 dark:to-emerald-900 rounded-xl text-center text-lg">
📝 <strong>Exit ticket app:</strong> <span class="font-mono underline">[facilitator pastes the AI Studio link]</span>
</div>

```

(Keep the trailing blank line before the existing `---` separator.)

- [ ] **Step 3: Verify the old static prompts are gone**

Run: `grep -n 'One thing still fuzzy\|One thing that clicked' slides/_template/slides.md`
Expected: no matches (exit code 1).

- [ ] **Step 4: Commit**

```bash
git add slides/_template/slides.md
git commit -m "feat: rework Exit Ticket slide to point at live feedback app"
```

---

## Task 5: Update `materials/_template/run-of-session.md`

Add the "build the exit-ticket app" facilitator step into the build session, and update the Exit Ticket close.

**Files:**
- Modify: `materials/_template/run-of-session.md`

- [ ] **Step 1: Add the facilitator step to BUILD SESSION 2**

In `materials/_template/run-of-session.md`, find the `### 0:28-0:43 — BUILD SESSION 2: Make It Real (15 min)` section. Immediately after the `**Circulate and coach:**` list (the three bullet items ending with `"That's working! What's next?"`), insert this block:

```markdown

**While they build — build the exit-ticket app yourself:**
- Open AI Studio → Chat and paste the exit-ticket prompt (on the "Facilitator: Build the Exit Ticket" slide).
- Swap `your-email@example.edu` for your real address before sending the prompt.
- Iterate once or twice, then click **Share** and copy the public link.
- Paste that link onto the Exit Ticket slide (the `[facilitator pastes the AI Studio link]` placeholder) and/or the Padlet.
- This models the exact workflow participants are doing — and gives you a live feedback channel.
```

- [ ] **Step 2: Update the Exit Ticket close section**

Find the `### 0:58-1:00 — Exit Ticket & Close (2 min)` section. Replace its body with:

```markdown
**Exit ticket:** Point participants at the exit-ticket app you built and shared. Ask them to open the link and submit — rating, what worked, what they'd change, and what they'll build in the next 2 weeks.

**Close:** Thank them. "Now go build something." Remind them their built-app URLs live on the Padlet.
```

(If the existing section already has different timing in the heading, keep the existing heading text — only replace the body paragraphs.)

- [ ] **Step 3: Verify**

Run: `grep -n 'build the exit-ticket app yourself' materials/_template/run-of-session.md`
Expected: exactly one match.

- [ ] **Step 4: Commit**

```bash
git add materials/_template/run-of-session.md
git commit -m "docs: add live exit-ticket app step to _template run-of-session"
```

---

## Task 6: Point `new-talk.mjs` at the `_template` deck by default

**Files:**
- Modify: `scripts/new-talk.mjs:163`

- [ ] **Step 1: Change the default template**

In `scripts/new-talk.mjs`, line 163 currently reads:

```js
  const templateSlug = opts.from ?? slugs.at(-1);
```

Change it to:

```js
  const templateSlug = opts.from ?? '_template';
```

- [ ] **Step 2: Improve the missing-template error message**

Line 172-174 currently throws a generic error. Update the message so a missing `_template` is self-explanatory. Replace:

```js
  if (!slugs.includes(templateSlug)) {
    throw new Error(`Template "${templateSlug}" not found under slides/. Available: ${slugs.join(', ')}`);
  }
```

with:

```js
  if (!slugs.includes(templateSlug)) {
    throw new Error(
      `Template "${templateSlug}" not found under slides/. ` +
      `Default template is "_template"; pass --from <slug> to copy from another deck. ` +
      `Available: ${slugs.join(', ')}`,
    );
  }
```

- [ ] **Step 3: Verify with a dry run**

Run: `npm run new:talk -- --slug 2099-01-01-plan-verify --dry-run`
Expected output includes the line `Template deck: slides/_template` and `Mode: dry-run (no files written)`. No `slides/2099-01-01-plan-verify` directory is created (confirm with `ls slides | grep 2099` → no match).

- [ ] **Step 4: Commit**

```bash
git add scripts/new-talk.mjs
git commit -m "feat: default new:talk to the _template deck"
```

---

## Task 7: Skip `_template` in the GitHub Actions deploy build

The deploy workflow builds every `slides/*`. `_template` is a scaffold, not a deliverable talk — skip it so it does not publish a stray deck.

**Files:**
- Modify: `.github/workflows/deploy.yml`

- [ ] **Step 1: Add a skip in the build loop**

In `.github/workflows/deploy.yml`, the build loop has this line:

```bash
            slug="$(basename "$dir")"
            echo "Building Slidev deck: $slug"
```

Insert a skip immediately after the `slug=` assignment and before the `echo`:

```bash
            slug="$(basename "$dir")"

            if [ "$slug" = "_template" ]; then
              echo "Skipping scaffold deck: $slug"
              continue
            fi

            echo "Building Slidev deck: $slug"
```

- [ ] **Step 2: Verify YAML is still valid**

Run: `python3 -c "import yaml,sys; yaml.safe_load(open('.github/workflows/deploy.yml')); print('YAML OK')"`
Expected: `YAML OK`

- [ ] **Step 3: Commit**

```bash
git add .github/workflows/deploy.yml
git commit -m "ci: skip _template scaffold deck in deploy build"
```

---

## Task 8: Build-verify the `_template` deck

Confirm the edited template deck still builds cleanly (it would otherwise break the deploy if the skip in Task 7 were ever removed, and proves the new slides have no syntax errors).

**Files:** none (verification only)

- [ ] **Step 1: Install deps and build**

```bash
cd slides/_template
npm install --no-audit --no-fund
npm run build
```

Expected: build completes with no error; a `dist/` directory is produced.

- [ ] **Step 2: Clean the build artifact**

```bash
rm -rf dist
cd ../..
```

Expected: `git status --short slides/_template` shows no `dist/` (it is gitignored or absent).

- [ ] **Step 3: Final scaffold smoke test**

```bash
npm run new:talk -- --slug 2099-01-01-smoke --session "Smoke Test" --date 2099-01-01
grep -rn '_template' slides/2099-01-01-smoke materials/2099-01-01-smoke
```

Expected: the scaffold succeeds; `grep` returns no matches (every `_template` string was rewritten to `2099-01-01-smoke`). Confirm `slides/2099-01-01-smoke/package.json` build script reads `--base /build-to-learn/2099-01-01-smoke/`.

- [ ] **Step 4: Remove the smoke-test scaffold**

```bash
rm -rf slides/2099-01-01-smoke materials/2099-01-01-smoke
```

Expected: `git status --short` shows no `2099-01-01-smoke` paths.

- [ ] **Step 5: Final commit (if anything staged)**

No code changes expected from this task. If `git status` is clean, skip. Otherwise investigate before committing.

---

## Self-Review

**Spec coverage:**
- Part 1 — canonical `_template` deck: Tasks 1, 2 (copy + generic-ize); `new-talk.mjs` default: Task 6. ✓
- Part 1 trade-off (template publishing on Pages): Task 7 resolves it (skip in deploy). ✓
- Part 2 — facilitator-cue slide: Task 3. ✓
- Part 2 — replace static Exit Ticket slide: Task 4. ✓
- Part 2 — materials run-of-session update: Task 5. ✓
- Out of scope honored: no `exit-ticket.html` starter file; mailto collection only; no edits to delivered decks. ✓

**Placeholder scan:** No "TBD"/"TODO"/vague steps — every edit shows exact content. ✓

**Type/name consistency:** Folder name `_template` and slug string `_template` used consistently across all tasks and in `new-talk.mjs`. Build base `/build-to-learn/_template/` consistent between Task 2 and Task 6's scaffold output check. ✓
