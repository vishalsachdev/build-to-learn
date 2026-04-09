---
theme: apple-basic
title: 'Build To Learn'
titleTemplate: '%s - Learn To Build'
author: 'Vishal Sachdev'
fonts:
  sans: 'IBM Plex Sans'
  serif: 'Spectral'
  mono: 'IBM Plex Mono'
info: |
  Build To Learn, Learn To Build
  What happens when a business professor treats AI as a building material. Projects, demos, and lessons from shipping real products with AI.
unocss: true
download: 'https://github.com/vishalsachdev'
colorSchema: 'auto'
transition: slide-left
---

<div class="relative h-full flex flex-col items-center justify-center text-center pb-10">
  <div class="text-5xl font-bold leading-tight">Build To Learn</div>
  <div class="text-2xl mt-2 font-semibold">Learn To Build</div>

  <div class="mt-6 text-xl font-semibold text-blue-500 dark:text-blue-300">
    Research Park Data + AI User Group · April 10, 2026
  </div>

  <div class="mt-8">
    <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
      Vishal Sachdev <carbon:arrow-right class="inline"/>
    </span>
  </div>

  <div class="mt-2 text-sm opacity-80">
    Clinical Associate Professor, Gies College of Business
  </div>

  <div class="mt-4 flex items-center justify-center gap-6">
    <img src="/qr-substack.png" class="w-24 h-24" alt="QR code for chatwithgpt.substack.com" />
    <div class="text-xs opacity-80 space-y-1 text-left">
      <div><a href="https://chatwithgpt.substack.com/" target="_blank" class="underline">chatwithgpt.substack.com</a></div>
      <div><a href="https://www.linkedin.com/in/vishalsachdev" target="_blank" class="underline">linkedin.com/in/vishalsachdev</a></div>
    </div>
  </div>

  <div class="absolute bottom-4 left-0 right-0 text-center text-[10px] opacity-70">Use &lt;- and -&gt; to navigate</div>
</div>

---

# About Me

<div class="grid grid-cols-2 gap-12 items-center my-8">

<div>

<div class="space-y-4 text-lg">
<div><strong>Day job:</strong> I run a 3D printing lab and an analytics masters program at Gies</div>
<div><strong>Side quest:</strong> I build things with AI — a lot of things</div>
<div><strong>Background:</strong> 7 years in industry, 18 years in academia</div>
</div>

<div class="mt-8 p-4 bg-blue-50 dark:bg-blue-900 rounded-lg text-lg">
I'm not an AI researcher. I'm a <strong>practitioner</strong> who builds real products and uses them in real classrooms.
</div>

</div>

<div class="p-6 bg-gradient-to-br from-orange-50 to-blue-50 dark:from-orange-900 dark:to-blue-900 rounded-xl text-center">
<div class="text-6xl mb-4">50+</div>
<div class="text-xl font-bold">projects shipped in the last year</div>
<div class="text-sm mt-2 opacity-70">open source tools, web apps, bots, APIs, websites, research prototypes</div>
</div>

</div>

---

# Today's Agenda

<div class="grid grid-cols-4 gap-4 my-8">

<div class="p-4 bg-gray-100 dark:bg-gray-800 rounded-xl text-center">
<div class="text-3xl mb-2">🧠</div>
<div class="text-lg font-bold">Framework</div>
<div class="text-sm text-gray-500">10 min</div>
</div>

<div class="p-4 bg-yellow-50 dark:bg-yellow-900 rounded-xl text-center">
<div class="text-3xl mb-2">🔧</div>
<div class="text-lg font-bold">Projects</div>
<div class="text-sm text-gray-500">30 min</div>
</div>

<div class="p-4 bg-blue-50 dark:bg-blue-900 rounded-xl text-center">
<div class="text-3xl mb-2">⚡</div>
<div class="text-lg font-bold">Live Build</div>
<div class="text-sm text-gray-500">10 min</div>
</div>

<div class="p-4 bg-emerald-50 dark:bg-emerald-900 rounded-xl text-center">
<div class="text-3xl mb-2">💬</div>
<div class="text-lg font-bold">Q&A</div>
<div class="text-sm text-gray-500">10 min</div>
</div>

</div>

<div class="mt-8 p-4 bg-gradient-to-r from-orange-50 to-blue-50 dark:from-orange-900 dark:to-blue-900 rounded-xl text-center text-xl">
One person built everything you'll see today. That's the point.
</div>

---

<div class="h-full flex items-center justify-center bg-gradient-to-br from-orange-500 to-blue-600 text-white">
<div class="text-center">
<div class="text-8xl font-bold mb-4">PART 1</div>
<div class="text-4xl mb-8">The Framework</div>
<div class="text-2xl opacity-90">How to think about building with AI</div>
</div>
</div>

---

# The Premise

<div class="flex items-center justify-center h-full">

<div class="max-w-4xl">

<div class="p-10 bg-gradient-to-r from-blue-100 to-orange-100 dark:from-blue-900 dark:to-orange-900 rounded-2xl border-l-8 border-orange-500 shadow-xl">

<div class="text-3xl font-bold leading-relaxed mb-6">
AI has commoditized intelligence.<br/>
<span class="text-orange-600 dark:text-orange-300">What's scarce now are human dispositions.</span>
</div>

<div class="text-xl text-gray-600 dark:text-gray-300">
Curiosity, agency, experimentation, and judgment — the things AI can't do for you.
</div>

</div>

<div class="mt-10 text-xl text-center leading-relaxed">
I develop these dispositions by <strong>building things</strong>, not by reading about building things.
</div>

</div>

</div>

---

# GRIT-CART: A Builder's Framework

<div class="my-8">

<div class="grid grid-cols-4 gap-4 mb-8">

<div class="p-5 bg-gradient-to-br from-purple-50 to-purple-100 dark:from-purple-900 dark:to-purple-800 rounded-xl text-center">
<div class="text-4xl mb-3 font-bold text-purple-600 dark:text-purple-300">C</div>
<div class="text-lg font-bold">Curiosity</div>
<div class="text-sm mt-2">What don't I know?</div>
</div>

<div class="p-5 bg-gradient-to-br from-orange-50 to-orange-100 dark:from-orange-900 dark:to-orange-800 rounded-xl text-center">
<div class="text-4xl mb-3 font-bold text-orange-600 dark:text-orange-300">A</div>
<div class="text-lg font-bold">Agency</div>
<div class="text-sm mt-2">What can I do about it?</div>
</div>

<div class="p-5 bg-gradient-to-br from-blue-50 to-blue-100 dark:from-blue-900 dark:to-blue-800 rounded-xl text-center">
<div class="text-4xl mb-3 font-bold text-blue-600 dark:text-blue-300">R</div>
<div class="text-lg font-bold">Resourceful Experimentation</div>
<div class="text-sm mt-2">What small bet can I test?</div>
</div>

<div class="p-5 bg-gradient-to-br from-emerald-50 to-emerald-100 dark:from-emerald-900 dark:to-emerald-800 rounded-xl text-center">
<div class="text-4xl mb-3 font-bold text-emerald-600 dark:text-emerald-300">T</div>
<div class="text-lg font-bold">Thoughtful Judgment</div>
<div class="text-sm mt-2">Should I persist, pivot, or stop?</div>
</div>

</div>

<div class="p-6 bg-gray-100 dark:bg-gray-800 rounded-xl text-center">
<div class="text-2xl font-bold mb-2">GRIT = the engine that drives repeated passes through the CART loop</div>
<div class="text-lg">Each project is a "shot on goal." Not all are perfect. That's the point.</div>
</div>

</div>

---

# Three Shifts Happening Right Now

<div class="space-y-6 my-8">

<div class="p-5 bg-gradient-to-r from-orange-50 to-orange-100 dark:from-orange-900 dark:to-orange-800 rounded-xl flex items-start gap-4">
<div class="text-3xl font-bold text-orange-600 dark:text-orange-300 mt-1">1</div>
<div>
<div class="font-bold text-xl mb-1">From Data Entry to Data Direction</div>
<div class="text-lg">AI handles rote work. The human decides what questions to ask, what matters, what to do with the answer.</div>
</div>
</div>

<div class="p-5 bg-gradient-to-r from-blue-50 to-blue-100 dark:from-blue-900 dark:to-blue-800 rounded-xl flex items-start gap-4">
<div class="text-3xl font-bold text-blue-600 dark:text-blue-300 mt-1">2</div>
<div>
<div class="font-bold text-xl mb-1">From Specialists to T-Shaped Builders</div>
<div class="text-lg">Domain knowledge + AI fluency. You don't need to code — you need to describe what you want built clearly.</div>
</div>
</div>

<div class="p-5 bg-gradient-to-r from-emerald-50 to-emerald-100 dark:from-emerald-900 dark:to-emerald-800 rounded-xl flex items-start gap-4">
<div class="text-3xl font-bold text-emerald-600 dark:text-emerald-300 mt-1">3</div>
<div>
<div class="font-bold text-xl mb-1">From Consuming Tools to Building Tools</div>
<div class="text-lg">The old model: learn software. The new model: <strong>build</strong> the tool you need.</div>
</div>
</div>

</div>

---

# The Three Stances

<div class="my-8">

<div class="space-y-6">

<div class="p-6 bg-red-50 dark:bg-red-900 rounded-xl border-l-4 border-red-500 flex items-start gap-4">
<div class="text-4xl">❌</div>
<div>
<div class="font-bold text-xl mb-2">Don't know the domain</div>
<div class="text-lg">AI gives garbage mixed with gold, and you can't tell which is which</div>
</div>
</div>

<div class="p-6 bg-yellow-50 dark:bg-yellow-900 rounded-xl border-l-4 border-yellow-500 flex items-start gap-4">
<div class="text-4xl">⚠️</div>
<div>
<div class="font-bold text-xl mb-2">Know domain, resist adapting</div>
<div class="text-lg">You only get time savings on rote tasks — autocomplete for your existing workflow</div>
</div>
</div>

<div class="p-6 bg-gradient-to-r from-green-50 to-blue-50 dark:from-green-900 dark:to-blue-900 rounded-xl border-l-4 border-green-500 flex items-start gap-4">
<div class="text-4xl">🚀</div>
<div>
<div class="font-bold text-xl mb-2">Know domain + collaborate creatively</div>
<div class="text-lg font-bold text-green-600 dark:text-green-300">DRAMATIC AMPLIFICATION — a solo builder ships like a team</div>
</div>
</div>

</div>

<div class="mt-8 p-4 bg-blue-50 dark:bg-blue-900 rounded-xl text-center text-xl">
Everyone in this room has domain expertise. The question is: are you in <span class="text-green-600 dark:text-green-300 font-bold">Stance 3</span>?
</div>

</div>

---

<div class="h-full flex items-center justify-center bg-gradient-to-br from-blue-600 to-emerald-500 text-white">
<div class="text-center">
<div class="text-8xl font-bold mb-4">PART 2</div>
<div class="text-4xl mb-8">The Projects</div>
<div class="text-2xl opacity-90">Four shots on goal — live demos</div>
</div>
</div>

---

# Project 1: Canvas MCP

<div class="grid grid-cols-2 gap-8 my-6">

<div>
<div class="text-lg mb-4"><strong>What:</strong> An open-source server that gives AI assistants (Claude, ChatGPT, Codex) the ability to interact with Canvas LMS — 90+ tools for grading, analytics, peer review, messaging, accessibility.</div>

<div class="space-y-2 text-base">
<div>80+ GitHub stars, 30 forks, 9 contributors</div>
<div>Published on PyPI, npm, MCP Registry, skills.sh</div>
<div>Used in 2 live courses with 200+ students</div>
<div>290+ automated tests, TDD-enforced</div>
</div>

<div class="mt-4 p-3 bg-orange-50 dark:bg-orange-900 rounded-lg text-base">
<strong>CART:</strong> Curiosity ("what if AI could manage my course?") → Agency (built 90+ tools solo) → Experimentation (QC'd my own course live) → Judgment (what should AI NOT do?)
</div>
</div>

<div class="p-6 bg-gray-100 dark:bg-gray-800 rounded-xl">
<div class="text-sm font-bold mb-3 text-gray-500">LIVE DEMO</div>

<div class="space-y-3 text-base">
<div class="p-3 bg-white dark:bg-gray-700 rounded-lg font-mono text-sm">"Show me which students haven't submitted their peer reviews"</div>
<div class="p-3 bg-white dark:bg-gray-700 rounded-lg font-mono text-sm">"Audit this course for accessibility issues"</div>
<div class="p-3 bg-white dark:bg-gray-700 rounded-lg font-mono text-sm">"Grade these 5 submissions using the rubric"</div>
</div>

<div class="mt-4 text-center">
<div class="text-sm font-bold text-blue-500">canvas-mcp.illinihunt.org</div>
</div>
</div>

</div>

---

# What is MCP?

<div class="my-8">

<div class="p-6 bg-blue-50 dark:bg-blue-900 rounded-xl mb-8">
<div class="text-2xl font-bold mb-3">Model Context Protocol</div>
<div class="text-lg">An open standard (by Anthropic) that lets AI assistants <strong>use tools</strong> — not just generate text, but take actions in real systems.</div>
</div>

<div class="grid grid-cols-3 gap-6">

<div class="p-5 bg-gray-100 dark:bg-gray-800 rounded-xl text-center">
<div class="text-4xl mb-3">💬</div>
<div class="font-bold text-lg mb-2">Before MCP</div>
<div class="text-base">AI generates text. You copy-paste it somewhere. Manual glue everywhere.</div>
</div>

<div class="p-5 bg-gradient-to-br from-blue-50 to-emerald-50 dark:from-blue-900 dark:to-emerald-900 rounded-xl text-center border-2 border-blue-300">
<div class="text-4xl mb-3">🔧</div>
<div class="font-bold text-lg mb-2">After MCP</div>
<div class="text-base">AI calls structured tools directly. Reads data, takes actions, reports results.</div>
</div>

<div class="p-5 bg-gradient-to-br from-orange-50 to-orange-100 dark:from-orange-900 dark:to-orange-800 rounded-xl text-center">
<div class="text-4xl mb-3">🌐</div>
<div class="font-bold text-lg mb-2">Why It Matters</div>
<div class="text-base">One protocol, any AI assistant. Build once, use everywhere. Like USB for AI.</div>
</div>

</div>

</div>

---

# Project 2: IlliniHunt

<div class="grid grid-cols-2 gap-8 my-6">

<div>
<div class="text-lg mb-4"><strong>What:</strong> Product Hunt for the University of Illinois. A community platform where UIUC students and faculty showcase projects they've built.</div>

<div class="space-y-2 text-base">
<div>React 18 + TypeScript + Supabase + Vercel</div>
<div>Google OAuth restricted to @illinois.edu</div>
<div>Trending algorithm, moderation, content reporting</div>
<div>Row-level security, keyboard nav, ARIA attributes</div>
</div>

<div class="mt-4 p-3 bg-orange-50 dark:bg-orange-900 rounded-lg text-base">
<strong>CART:</strong> Curiosity ("what if UIUC had its own Product Hunt?") → Agency (shipped it) → Experimentation (trending algorithm, moderation) → Judgment (does this serve the community?)
</div>
</div>

<div class="p-6 bg-gray-100 dark:bg-gray-800 rounded-xl">
<div class="text-sm font-bold mb-3 text-gray-500">LIVE DEMO</div>

<div class="space-y-4 text-base">
<div>Browse live projects at illinihunt.org</div>
<div>Show the full-stack architecture</div>
<div>Walk through the moderation system</div>
<div>Show how one person ships a production app</div>
</div>

<div class="mt-6 p-4 bg-blue-50 dark:bg-blue-900 rounded-lg text-center">
<div class="text-lg font-bold text-blue-500">illinihunt.org</div>
</div>
</div>

</div>

---

# Project 3: WhatsApp AI Teaching Assistant

<div class="grid grid-cols-2 gap-8 my-6">

<div>
<div class="text-lg mb-4"><strong>What:</strong> A WhatsApp bot on my personal number that acts as a TA for 36 students. Socratic questioning, drip campaigns, guardrails against cheating.</div>

<div class="space-y-2 text-base">
<div>Node.js + PostgreSQL + WhatsApp gateway</div>
<div>Two AI agents: student-facing (Claude) + professor-facing (GPT-4o)</div>
<div>Jailbreak detection, off-topic filtering, rate limiting</div>
<div>109 sessions, 97 hours of student interaction in 3 days</div>
</div>

<div class="mt-4 p-3 bg-orange-50 dark:bg-orange-900 rounded-lg text-base">
<strong>CART:</strong> Curiosity ("what if students could text AI?") → Agency (deployed on my phone) → Experimentation (drip campaigns, guardrails) → Judgment (is this ethical? transparent?)
</div>
</div>

<div class="p-6 bg-gray-100 dark:bg-gray-800 rounded-xl">
<div class="text-sm font-bold mb-3 text-gray-500">LIVE DEMO</div>

<div class="space-y-4 text-base">
<div>Show a real student conversation</div>
<div>Demonstrate the guardrails: try to jailbreak it</div>
<div>Show the drip campaign system</div>
<div>Walk through the dual-agent architecture</div>
</div>

<div class="mt-6 p-4 bg-yellow-50 dark:bg-yellow-900 rounded-lg text-center text-sm">
Published: "I Put an AI Teaching Assistant in My Students' WhatsApp"
</div>
</div>

</div>

---

# Production Lessons: Guardrails

<div class="my-8">

<div class="text-xl mb-6">What I learned deploying AI that talks to real users every day:</div>

<div class="grid grid-cols-2 gap-6">

<div class="p-5 bg-red-50 dark:bg-red-900 rounded-xl">
<div class="text-2xl mb-2">🛡️</div>
<div class="font-bold text-lg mb-2">Jailbreak Detection</div>
<div class="text-base">Students will try. "Ignore all previous instructions" hit on day 2. Multi-layer defense: system prompt hardening + output monitoring.</div>
</div>

<div class="p-5 bg-yellow-50 dark:bg-yellow-900 rounded-xl">
<div class="text-2xl mb-2">🎯</div>
<div class="font-bold text-lg mb-2">Scope Control</div>
<div class="text-base">Without guardrails, "show me the answer" works. Socratic mode means the bot asks questions back — but you have to enforce it.</div>
</div>

<div class="p-5 bg-blue-50 dark:bg-blue-900 rounded-xl">
<div class="text-2xl mb-2">📊</div>
<div class="font-bold text-lg mb-2">Rate Limiting</div>
<div class="text-base">30 AI calls/hour. Without it, one student's infinite loop burns your API budget in minutes.</div>
</div>

<div class="p-5 bg-emerald-50 dark:bg-emerald-900 rounded-xl">
<div class="text-2xl mb-2">🔒</div>
<div class="font-bold text-lg mb-2">Safety Confirmations</div>
<div class="text-base">Broadcasts to 36 students require YES/NO confirmation. One typo in a bulk message is a very bad day.</div>
</div>

</div>

</div>

---

# Project 4: MakerLab Website

<div class="grid grid-cols-2 gap-8 my-6">

<div>
<div class="text-lg mb-4"><strong>What:</strong> The website for the world's first business school 3D printing lab. 32 pages, 301 blog posts, migrated from Squarespace. AI-agent optimized.</div>

<div class="space-y-2 text-base">
<div>Pure HTML/CSS/JS — no framework, no build step</div>
<div>301 blog posts migrated with Python scripts</div>
<div>llms.txt, agent-guide.json, OpenAPI spec</div>
<div>3D Print Quote Calculator with Three.js preview</div>
<div>WCAG 2.1 AA accessible</div>
</div>

<div class="mt-4 p-3 bg-orange-50 dark:bg-orange-900 rounded-lg text-base">
<strong>CART:</strong> Curiosity ("what if our website could talk to AI?") → Agency (migrated 301 posts) → Experimentation (llms.txt, agent APIs) → Judgment (does AI-readable design serve humans?)
</div>
</div>

<div class="p-6 bg-gray-100 dark:bg-gray-800 rounded-xl">
<div class="text-sm font-bold mb-3 text-gray-500">LIVE DEMO</div>

<div class="space-y-4 text-base">
<div>Ask ChatGPT about MakerLab — it knows the site</div>
<div>Show llms.txt and agent-guide.json</div>
<div>3D print quote calculator with live preview</div>
<div>Monthly blog auto-generation from order data</div>
</div>

<div class="mt-6 p-4 bg-blue-50 dark:bg-blue-900 rounded-lg text-center">
<div class="text-lg font-bold text-blue-500">makerlab.illinois.edu</div>
</div>
</div>

</div>

---

# Making Your Work AI-Readable

<div class="my-8">

<div class="text-xl mb-6">A pattern that applies to any project — make your systems understandable to AI agents:</div>

<div class="grid grid-cols-3 gap-6">

<div class="p-5 bg-gray-100 dark:bg-gray-800 rounded-xl">
<div class="text-3xl mb-3 font-mono font-bold">/llms.txt</div>
<div class="text-base">A simple text file telling AI what your site is about. Like robots.txt, but for LLMs.</div>
</div>

<div class="p-5 bg-gray-100 dark:bg-gray-800 rounded-xl">
<div class="text-3xl mb-3 font-mono font-bold">MCP</div>
<div class="text-base">Structured tools AI can call. Read data, take actions, report results — not just scrape HTML.</div>
</div>

<div class="p-5 bg-gray-100 dark:bg-gray-800 rounded-xl">
<div class="text-3xl mb-3 font-mono font-bold">Schema.org</div>
<div class="text-base">Structured data that both search engines and AI agents can parse.</div>
</div>

</div>

<div class="mt-8 p-4 bg-blue-50 dark:bg-blue-900 rounded-xl text-center text-lg">
The next generation of SEO isn't for Google — it's for AI agents. Every data scientist should care about this.
</div>

</div>

---

<div class="h-full flex items-center justify-center bg-gradient-to-br from-purple-600 to-pink-500 text-white">
<div class="text-center">
<div class="text-8xl font-bold mb-4">PART 3</div>
<div class="text-4xl mb-8">Live Build</div>
<div class="text-2xl opacity-90">Let's build something right now</div>
</div>
</div>

---

# Live Build: Your Idea, 10 Minutes

<div class="flex items-center justify-center h-full">

<div class="text-center max-w-3xl">

<div class="text-6xl mb-8">⚡</div>

<div class="text-2xl mb-8">Give me a problem or an idea.<br/>I'll build a working prototype in front of you.</div>

<div class="grid grid-cols-2 gap-6 mb-8">
<div class="p-4 bg-gray-100 dark:bg-gray-800 rounded-lg text-left">
<div class="font-bold mb-2">Tools I might use:</div>
<div class="text-base space-y-1">
<div>Claude Code (AI coding agent)</div>
<div>Google AI Studio (no-code builder)</div>
<div>Cursor / VS Code</div>
</div>
</div>
<div class="p-4 bg-gray-100 dark:bg-gray-800 rounded-lg text-left">
<div class="font-bold mb-2">What makes a good suggestion:</div>
<div class="text-base space-y-1">
<div>A pain point you actually have</div>
<div>A tool your team wishes existed</div>
<div>Something you'd want to take home</div>
</div>
</div>
</div>

<div class="p-4 bg-orange-50 dark:bg-orange-900 rounded-xl text-lg">
This is Stance 3 in action: <strong>domain expertise + AI collaboration = dramatic amplification</strong>
</div>

</div>

</div>

---

# The Pattern

<div class="my-8">

<div class="text-xl mb-6">Every project I showed you followed the same loop:</div>

<div class="flex justify-between items-center my-12">
  <div class="text-center p-6 rounded-lg bg-purple-50 dark:bg-purple-900">
    <div class="text-5xl mb-4">🤔</div>
    <div class="font-bold text-lg">Curiosity</div>
    <div class="text-sm mt-2">"What if...?"</div>
  </div>
  <div class="text-3xl text-gray-400">→</div>
  <div class="text-center p-6 rounded-lg bg-orange-50 dark:bg-orange-900">
    <div class="text-5xl mb-4">🔨</div>
    <div class="font-bold text-lg">Agency</div>
    <div class="text-sm mt-2">Build it</div>
  </div>
  <div class="text-3xl text-gray-400">→</div>
  <div class="text-center p-6 rounded-lg bg-blue-50 dark:bg-blue-900">
    <div class="text-5xl mb-4">🧪</div>
    <div class="font-bold text-lg">Experiment</div>
    <div class="text-sm mt-2">Ship to real users</div>
  </div>
  <div class="text-3xl text-gray-400">→</div>
  <div class="text-center p-6 rounded-lg bg-emerald-50 dark:bg-emerald-900">
    <div class="text-5xl mb-4">⚖️</div>
    <div class="font-bold text-lg">Judgment</div>
    <div class="text-sm mt-2">Keep, pivot, or kill</div>
  </div>
</div>

<div class="p-6 bg-gray-100 dark:bg-gray-800 rounded-xl text-center text-xl">
You develop taste by shipping, not by theorizing. The CART loop is how you take <strong>shots on goal</strong>.
</div>

</div>

---

# Context Engineering > Prompt Engineering

<div class="my-8">

<div class="text-center mb-8 text-3xl font-bold">
<span class="line-through text-gray-400">PROMPT ENGINEERING</span>
<span class="mx-4">→</span>
<span class="text-blue-600 dark:text-blue-300">CONTEXT ENGINEERING</span>
</div>

<div class="grid grid-cols-2 gap-8 mt-8">

<div class="p-8 bg-gray-100 dark:bg-gray-800 rounded-xl">
<div class="text-4xl mb-4">❌</div>
<h3 class="text-xl font-bold mb-3">Prompt Engineering</h3>
<p class="text-lg">Wordsmithing — finding the magic phrase. Fragile and non-transferable.</p>
</div>

<div class="p-8 bg-gradient-to-br from-blue-50 to-emerald-50 dark:from-blue-900 dark:to-emerald-900 rounded-xl border-2 border-blue-300">
<div class="text-4xl mb-4">✅</div>
<h3 class="text-xl font-bold mb-3">Context Engineering</h3>
<p class="text-lg"><strong>What information</strong> you give AI, how you structure it, and what tools you connect. That's what Canvas MCP is — 90 tools of structured context.</p>
</div>

</div>

<div class="mt-8 p-4 bg-yellow-50 dark:bg-yellow-900 rounded-xl text-center text-lg">
The best AI results come from <strong>domain expertise made explicit</strong>, not clever prompting tricks.
</div>

</div>

---

# What You Can Do This Week

<div class="my-8">

<div class="grid grid-cols-3 gap-6">

<div class="p-6 bg-gradient-to-br from-orange-50 to-orange-100 dark:from-orange-900 dark:to-orange-800 rounded-xl">
<div class="text-4xl mb-3">1</div>
<div class="font-bold text-lg mb-3">Build Something Small</div>
<div class="text-base">Open Google AI Studio or Claude. Describe a tool your team needs. Ship it this week. It doesn't have to be perfect.</div>
</div>

<div class="p-6 bg-gradient-to-br from-blue-50 to-blue-100 dark:from-blue-900 dark:to-blue-800 rounded-xl">
<div class="text-4xl mb-3">2</div>
<div class="font-bold text-lg mb-3">Make Your Work AI-Readable</div>
<div class="text-base">Add an llms.txt to your project. Write a CLAUDE.md or AGENTS.md for your codebase. Structure your data for AI consumption.</div>
</div>

<div class="p-6 bg-gradient-to-br from-emerald-50 to-emerald-100 dark:from-emerald-900 dark:to-emerald-800 rounded-xl">
<div class="text-4xl mb-3">3</div>
<div class="font-bold text-lg mb-3">Move to Stance 3</div>
<div class="text-base">Stop using AI as autocomplete. Start collaborating: describe what you need, iterate, ship. Your domain expertise is the scarce ingredient.</div>
</div>

</div>

<div class="mt-8 p-4 bg-gray-100 dark:bg-gray-800 rounded-xl text-center text-xl">
The gap between "I use AI" and "I build with AI" is where the value lives.
</div>

</div>

---

# Let's Talk

<div class="flex items-center justify-center h-full">

<div class="text-center max-w-3xl">

<div class="text-5xl font-bold mb-4">Build To Learn. Learn To Build.</div>

<div class="text-xl mb-8 opacity-80">
Everything you saw today was built by one person using AI as a collaborator.<br/>
Your domain expertise is the scarce ingredient. Start building.
</div>

<div class="grid grid-cols-3 gap-6 mb-8">
<div class="p-4 bg-gray-100 dark:bg-gray-800 rounded-lg">
<div class="font-bold mb-2">Projects</div>
<div class="text-sm space-y-1">
<div>canvas-mcp.illinihunt.org</div>
<div>illinihunt.org</div>
<div>makerlab.illinois.edu</div>
</div>
</div>
<div class="p-4 bg-gray-100 dark:bg-gray-800 rounded-lg">
<div class="font-bold mb-2">Connect</div>
<div class="text-sm space-y-1">
<div><a href="https://chatwithgpt.substack.com/" target="_blank" class="underline">chatwithgpt.substack.com</a></div>
<div><a href="https://www.linkedin.com/in/vishalsachdev" target="_blank" class="underline">linkedin.com/in/vishalsachdev</a></div>
<div>vishal@illinois.edu</div>
</div>
</div>
<div class="flex items-center justify-center">
<div class="text-center">
<img src="/qr-substack.png" class="w-28 h-28 mx-auto" alt="QR code for chatwithgpt.substack.com" />
<div class="text-xs mt-1 opacity-70">Newsletter</div>
</div>
</div>
</div>

<div class="text-2xl">💬 Q&A — What do you want to build?</div>

</div>

</div>
