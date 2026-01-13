import fs from 'node:fs/promises';
import path from 'node:path';

const REPO_ROOT = process.cwd();

function parseArgs(argv) {
  const opts = {
    slug: null,
    from: null,
    session: null,
    date: null,
    title: null,
    dryRun: false,
    force: false,
  };

  for (let i = 0; i < argv.length; i += 1) {
    const arg = argv[i];
    if (arg === '--dry-run') opts.dryRun = true;
    else if (arg === '--force') opts.force = true;
    else if (arg === '--slug') opts.slug = argv[++i] ?? null;
    else if (arg === '--from') opts.from = argv[++i] ?? null;
    else if (arg === '--session') opts.session = argv[++i] ?? null;
    else if (arg === '--date') opts.date = argv[++i] ?? null;
    else if (arg === '--title') opts.title = argv[++i] ?? null;
    else if (arg === '--help' || arg === '-h') opts.help = true;
    else throw new Error(`Unknown arg: ${arg}`);
  }

  return opts;
}

function usage() {
  return [
    'Usage:',
    '  npm run new:talk -- --slug <deck-slug> [--from <template-slug>] [--session "..."] [--date YYYY-MM-DD] [--title "..."] [--dry-run] [--force]',
    '',
    'Examples:',
    '  npm run new:talk -- --slug 2026-01-13-my-event --session "My Event (Online)" --date 2026-01-13',
    '  npm run new:talk -- --slug 2026-01-13-my-event --from 2025-01-09-future-world-alliance-online',
    '  npm run new:talk -- --slug 2026-01-13-my-event --dry-run',
    '',
    'Notes:',
    '  - Creates `slides/<slug>/` and `materials/<slug>/` by copying from a template.',
    '  - Updates `slides/<slug>/package.json` to use `--base /build-to-learn/<slug>/` for GitHub Pages.',
  ].join('\n');
}

async function pathExists(p) {
  try {
    await fs.access(p);
    return true;
  } catch {
    return false;
  }
}

async function listDeckSlugs() {
  const slidesDir = path.join(REPO_ROOT, 'slides');
  const entries = await fs.readdir(slidesDir, { withFileTypes: true });
  const slugs = [];
  for (const entry of entries) {
    if (!entry.isDirectory()) continue;
    const deckDir = path.join(slidesDir, entry.name);
    if (await pathExists(path.join(deckDir, 'package.json'))) slugs.push(entry.name);
  }
  slugs.sort();
  return slugs;
}

function ensureSafeSlug(slug) {
  if (!slug) throw new Error('Missing required --slug');
  if (!/^[a-z0-9][a-z0-9-]*$/.test(slug)) {
    throw new Error(`Invalid slug "${slug}". Use lowercase letters/numbers and hyphens only.`);
  }
}

async function copyDir(src, dest, { dryRun, force }) {
  if (dryRun) return;

  const ignored = new Set(['node_modules', 'dist', '.slidev', '.vite']);

  await fs.cp(src, dest, {
    recursive: true,
    force,
    errorOnExist: !force,
    filter: (srcPath) => !ignored.has(path.basename(srcPath)),
  });
}

async function replaceInMarkdownFiles(dir, from, to, { dryRun }) {
  if (dryRun) return;
  if (!(await pathExists(dir))) return;

  const entries = await fs.readdir(dir, { withFileTypes: true });
  for (const entry of entries) {
    if (!entry.isFile()) continue;
    if (!entry.name.endsWith('.md')) continue;

    const filePath = path.join(dir, entry.name);
    const contents = await fs.readFile(filePath, 'utf8');
    if (!contents.includes(from)) continue;

    const next = contents.replaceAll(from, to);
    await fs.writeFile(filePath, next, 'utf8');
  }
}

async function updateDeckSlidesMd(deckDir, { title, dryRun }) {
  if (!title) return;
  if (dryRun) return;

  const slidesPath = path.join(deckDir, 'slides.md');
  if (!(await pathExists(slidesPath))) return;

  const contents = await fs.readFile(slidesPath, 'utf8');
  const escaped = title.replaceAll("'", "''");
  const next = contents.replace(/^title:\s*.*$/m, `title: '${escaped}'`);
  await fs.writeFile(slidesPath, next, 'utf8');
}

async function updateDeckPackageJson(deckDir, slug, { dryRun }) {
  if (dryRun) return;
  const packageJsonPath = path.join(deckDir, 'package.json');
  const raw = await fs.readFile(packageJsonPath, 'utf8');
  const parsed = JSON.parse(raw);

  parsed.scripts = parsed.scripts ?? {};
  parsed.scripts.build = `slidev build --base /build-to-learn/${slug}/`;

  const next = `${JSON.stringify(parsed, null, 2)}\n`;
  await fs.writeFile(packageJsonPath, next, 'utf8');
}

async function updateDeckReadme(deckDir, templateSlug, slug, { session, date, dryRun }) {
  if (dryRun) return;
  const readmePath = path.join(deckDir, 'README.md');
  if (!(await pathExists(readmePath))) return;

  let contents = await fs.readFile(readmePath, 'utf8');
  contents = contents.replaceAll(`/build-to-learn/${templateSlug}/`, `/build-to-learn/${slug}/`);
  contents = contents.replaceAll(`build-to-learn/${templateSlug}/`, `build-to-learn/${slug}/`);
  contents = contents.replaceAll(`materials/${templateSlug}/`, `materials/${slug}/`);

  if (session) contents = contents.replace(/^(\*\*Session:\*\*)\s*.*$/m, `$1 ${session}`);
  if (date) contents = contents.replace(/^(\*\*Date:\*\*)\s*.*$/m, `$1 ${date}`);

  await fs.writeFile(readmePath, contents, 'utf8');
}

async function main() {
  const opts = parseArgs(process.argv.slice(2));
  if (opts.help) {
    process.stdout.write(`${usage()}\n`);
    return;
  }

  ensureSafeSlug(opts.slug);

  const slugs = await listDeckSlugs();
  if (slugs.length === 0) throw new Error('No templates found under slides/* (expected at least one Slidev deck).');

  const templateSlug = opts.from ?? slugs.at(-1);
  if (!templateSlug) throw new Error('Could not determine a template deck (unexpected).');

  const templateSlidesDir = path.join(REPO_ROOT, 'slides', templateSlug);
  const templateMaterialsDir = path.join(REPO_ROOT, 'materials', templateSlug);

  const newSlidesDir = path.join(REPO_ROOT, 'slides', opts.slug);
  const newMaterialsDir = path.join(REPO_ROOT, 'materials', opts.slug);

  if (!slugs.includes(templateSlug)) {
    throw new Error(`Template "${templateSlug}" not found under slides/. Available: ${slugs.join(', ')}`);
  }

  if (await pathExists(newSlidesDir)) {
    if (!opts.force) throw new Error(`Already exists: slides/${opts.slug} (use --force to overwrite)`);
  }
  if (await pathExists(newMaterialsDir)) {
    if (!opts.force) throw new Error(`Already exists: materials/${opts.slug} (use --force to overwrite)`);
  }

  const planLines = [
    `Template deck: slides/${templateSlug}`,
    `New deck:      slides/${opts.slug}`,
    `Template mat:  materials/${templateSlug}${(await pathExists(templateMaterialsDir)) ? '' : ' (missing)'}`,
    `New mat:       materials/${opts.slug}`,
    `Mode:          ${opts.dryRun ? 'dry-run (no files written)' : 'write'}`,
  ];
  process.stdout.write(`${planLines.join('\n')}\n\n`);

  if (opts.dryRun) {
    process.stdout.write('Planned changes:\n');
    process.stdout.write(`  - Copy slides/${templateSlug} -> slides/${opts.slug} (excluding node_modules/, dist/, .slidev/)\n`);
    process.stdout.write(`  - Copy materials/${templateSlug} -> materials/${opts.slug} (if present)\n`);
    process.stdout.write(`  - Set slides/${opts.slug}/package.json: scripts.build = "slidev build --base /build-to-learn/${opts.slug}/"\n`);
    process.stdout.write(`  - Update slides/${opts.slug}/README.md (URL slug + optional session/date)\n`);
    if (opts.title) process.stdout.write(`  - Update slides/${opts.slug}/slides.md title\n`);
    process.stdout.write('\n');
  } else {
    await copyDir(templateSlidesDir, newSlidesDir, { dryRun: opts.dryRun, force: opts.force });
    if (await pathExists(templateMaterialsDir)) {
      await copyDir(templateMaterialsDir, newMaterialsDir, { dryRun: opts.dryRun, force: opts.force });
    } else {
      await fs.mkdir(newMaterialsDir, { recursive: true });
    }

    await replaceInMarkdownFiles(newSlidesDir, templateSlug, opts.slug, { dryRun: opts.dryRun });
    await replaceInMarkdownFiles(newMaterialsDir, templateSlug, opts.slug, { dryRun: opts.dryRun });

    await updateDeckPackageJson(newSlidesDir, opts.slug, { dryRun: opts.dryRun });
    await updateDeckReadme(newSlidesDir, templateSlug, opts.slug, { session: opts.session, date: opts.date, dryRun: opts.dryRun });
    await updateDeckSlidesMd(newSlidesDir, { title: opts.title, dryRun: opts.dryRun });
  }

  process.stdout.write('Next steps:\n');
  process.stdout.write(`  - Edit slides:     slides/${opts.slug}/slides.md\n`);
  process.stdout.write(`  - Edit materials:  materials/${opts.slug}/\n`);
  process.stdout.write(`  - Run locally:     cd slides/${opts.slug} && npm install && npm run dev\n`);
  process.stdout.write(`  - Publish:         git push (GitHub Pages deploys on main)\n`);
}

main().catch((err) => {
  process.stderr.write(`${err?.message ?? String(err)}\n\n${usage()}\n`);
  process.exit(1);
});
