---
# https://sli.dev/guide/configuration.html
theme: apple-basic
title: 'Build To Learn'
titleTemplate: '%s - Learn To Build'
author: 'Vishal Sachdev'
fonts:
  sans: 'IBM Plex Sans'
  serif: 'Spectral'
  mono: 'IBM Plex Mono'
info: |
  Building to Learn, Learning to Build
  A workshop about shifting from teachers as content deliverers to teachers as builders.
# enable unocss
unocss: true
# some information about your slides
download: 'https://github.com/vishalsachdev'
colorSchema: 'auto'
background: 'https://source.unsplash.com/collection/94734566/1920x1080'
# turn slide animations on or off
transition: slide-left
# use `build` to apply multiple themes
# theme: seriph, apple-basic, default, etc
---

<div class="relative h-full flex flex-col items-center justify-center text-center pb-10">
  <div class="text-5xl font-bold leading-tight">Build To Learn</div>
  <div class="text-2xl mt-2 font-semibold">Learn To Build</div>

  <div class="mt-6 text-xl font-semibold text-blue-500 dark:text-blue-300">
    LLTLC · May 19, 2026
  </div>

  <div class="mt-8">
    <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
      @vishalsachdev <carbon:arrow-right class="inline"/>
    </span>
  </div>

  <div class="mt-4 text-xs opacity-80 space-y-1">
    <div><a href="https://chatwithgpt.substack.com/" target="_blank" class="underline">chatwithgpt.substack.com</a></div>
    <div><a href="https://www.linkedin.com/in/vishalsachdev" target="_blank" class="underline">LinkedIn - vishalsachdev</a></div>
  </div>

  <div class="absolute bottom-4 left-0 right-0 text-center text-[10px] opacity-70">Use &lt;- and -&gt; to navigate</div>
</div>

---

# Welcome

<div class="text-xl leading-relaxed">

Welcome, faculty and instructional designers. Today's workshop is about a **fundamental shift**:

<div class="mt-8 text-center text-2xl font-bold text-blue-500">
Instructors as Content Deliverers → Instructors as Builders
</div>

<div class="mt-12 p-6 bg-blue-50 dark:bg-blue-900 rounded-lg">
🎯 By the end of this session, you'll have built something real that you can use in your next class session.
</div>

</div>

---

# Today's Agenda

<div class="grid grid-cols-4 gap-4 my-8">

<div class="p-4 bg-gray-100 dark:bg-gray-800 rounded-xl text-center">
<div class="text-3xl mb-2">🧠</div>
<div class="text-lg font-bold">Mental Models</div>
<div class="text-sm text-gray-500">~15 min</div>
</div>

<div class="p-4 bg-yellow-50 dark:bg-yellow-900 rounded-xl text-center">
<div class="text-3xl mb-2">✏️</div>
<div class="text-lg font-bold">Sketch</div>
<div class="text-sm text-gray-500">8 min hands-on</div>
</div>

<div class="p-4 bg-blue-50 dark:bg-blue-900 rounded-xl text-center">
<div class="text-3xl mb-2">🤖</div>
<div class="text-lg font-bold">Build</div>
<div class="text-sm text-gray-500">15 min hands-on</div>
</div>

<div class="p-4 bg-emerald-50 dark:bg-emerald-900 rounded-xl text-center">
<div class="text-3xl mb-2">🚀</div>
<div class="text-lg font-bold">Share & Next Steps</div>
<div class="text-sm text-gray-500">~10 min</div>
</div>

</div>

<div class="mt-8 p-4 bg-gradient-to-r from-orange-50 to-pink-50 dark:from-orange-900 dark:to-pink-900 rounded-xl text-center text-xl">
<strong>~50% hands-on</strong> — You'll leave with something you built today
</div>

---

# The Shift

<div class="grid grid-cols-2 gap-12 items-center my-12">

<div class="p-6 bg-gray-100 dark:bg-gray-800 rounded-lg">

<div class="flex items-center gap-3 mb-4">
<div class="text-3xl">❌</div>
<h2 class="text-2xl font-bold">THE PROBLEM</h2>
</div>

<div class="space-y-4 text-lg">
<div>🤖 Assessments AI can game</div>
<div>📺 Instructors deliver content</div>
<div>🛋️ Students consume</div>
<div>⏱️ Shrinking attention spans</div>
</div>

</div>

<div class="p-8 bg-gradient-to-br from-blue-50 to-emerald-50 dark:from-blue-900 dark:to-emerald-900 rounded-xl border-2 border-blue-300">

<div class="flex items-center gap-3 mb-4">
<div class="text-3xl">💡</div>
<h2 class="text-2xl font-bold">THE NEW PARADIGM</h2>
</div>

<div class="space-y-4 text-lg">
<div>⚡ Projects requiring agency</div>
<div>🔧 Instructors BUILD tools</div>
<div>🎨 Students CREATE</div>
<div>🔥 Curiosity & ownership</div>
</div>

</div>

</div>

---

# The Philosophy

<div class="text-center p-8 bg-gradient-to-r from-emerald-100 to-blue-100 dark:from-emerald-900 dark:to-blue-900 rounded-2xl border-l-4 border-emerald-500 mb-8">
<div class="text-3xl font-bold italic leading-relaxed">
"Not by banning AI,<br/>but by making creation the default."
</div>
</div>

<div class="flex justify-between items-center my-12">
  <div class="text-center p-6 rounded-lg hover:bg-blue-50 dark:hover:bg-blue-900 transition">
    <div class="text-7xl mb-4">🔧</div>
    <div class="font-bold text-xl">You become<br/>builders</div>
  </div>
  <div class="text-5xl text-blue-500">→</div>
  <div class="text-center p-6 rounded-lg hover:bg-blue-50 dark:hover:bg-blue-900 transition">
    <div class="text-7xl mb-4">🎓</div>
    <div class="font-bold text-xl">You teach<br/>building</div>
  </div>
  <div class="text-5xl text-blue-500">→</div>
  <div class="text-center p-6 rounded-lg hover:bg-blue-50 dark:hover:bg-blue-900 transition">
    <div class="text-7xl mb-4">🚀</div>
    <div class="font-bold text-xl">Students become<br/>creators</div>
  </div>
</div>

---

# Why Building Works

<div class="grid grid-cols-3 gap-8 my-12">

<div class="p-6 bg-gradient-to-br from-orange-50 to-orange-100 dark:from-orange-900 dark:to-orange-800 rounded-xl">
<div class="text-5xl mb-4">⚡</div>
<h3 class="text-2xl font-bold mb-3 text-orange-600 dark:text-orange-300">AGENCY</h3>
<p class="text-lg">When you own what you make, you're invested — this is true for you <em>and</em> your students</p>
</div>

<div class="p-6 bg-gradient-to-br from-blue-50 to-blue-100 dark:from-blue-900 dark:to-blue-800 rounded-xl">
<div class="text-5xl mb-4">🔄</div>
<h3 class="text-2xl font-bold mb-3 text-blue-600 dark:text-blue-300">ITERATION</h3>
<p class="text-lg">Learning happens through attempt → feedback → refinement cycles</p>
</div>

<div class="p-6 bg-gradient-to-br from-emerald-50 to-emerald-100 dark:from-emerald-900 dark:to-emerald-800 rounded-xl">
<div class="text-5xl mb-4">🔍</div>
<h3 class="text-2xl font-bold mb-3 text-emerald-600 dark:text-emerald-300">CURIOSITY</h3>
<p class="text-lg">Building something real sparks questions worksheets never will</p>
</div>

</div>

<div class="text-center text-xl mt-8 p-4 bg-gray-100 dark:bg-gray-800 rounded-lg">
💡 These principles apply to <strong>you today</strong> AND to <strong>your students</strong> when you teach them
</div>

---

<div class="h-full flex items-center justify-center bg-gradient-to-br from-emerald-500 to-blue-500 text-white">
<div class="text-center">
<div class="text-8xl font-bold mb-4">PART 1</div>
<div class="text-4xl mb-8">Mental Models</div>
<div class="text-2xl opacity-90">How to think about working with AI</div>
</div>
</div>

---

# The Key Insight

<div class="flex items-center justify-center h-full">

<div class="max-w-4xl">

<div class="p-10 bg-gradient-to-r from-blue-100 to-emerald-100 dark:from-blue-900 dark:to-emerald-900 rounded-2xl border-l-8 border-blue-500 shadow-xl">

<div class="text-4xl font-bold leading-relaxed mb-8">
"The skill that makes you great at AI isn't technical.<br/>
<span class="text-blue-600 dark:text-blue-300">It's social.</span>"
</div>

<div class="text-xl text-gray-600 dark:text-gray-300">
— Riedl & Weidmann, "Quantifying Human-AI Synergy" (2025)
</div>

</div>

<div class="mt-10 text-xl text-center leading-relaxed">
It's about <strong>perspective-taking</strong> — understanding what the AI knows and doesn't know.
</div>

</div>

</div>

---

# Theory of Mind for AI

<div class="my-8">

<div class="p-6 bg-emerald-50 dark:bg-emerald-900 rounded-xl mb-8 text-xl">
<div class="text-4xl mb-3">🧠</div>
Your capacity to <strong>model another agent's</strong> beliefs, goals, and perspective.
</div>

<div class="grid grid-cols-2 gap-8 my-12">

<div class="p-6 bg-orange-50 dark:bg-orange-900 rounded-lg">
<div class="text-3xl mb-3">🤔</div>
<h3 class="font-bold text-xl mb-2">When you get a bad response, ask:</h3>
<ul class="space-y-2 text-lg">
<li>❓ "What false assumption is the AI making?"</li>
<li>❓ "What context am I taking for granted?"</li>
</ul>
</div>

<div class="p-6 bg-blue-50 dark:bg-blue-900 rounded-lg flex items-center justify-center">
<div class="text-center">
<div class="text-5xl mb-4">🌉</div>
<div class="text-2xl font-bold">Your job is to be the bridge</div>
<div class="text-3xl my-4">💭 ←→ 🤖</div>
<div class="text-lg">Intent ←→ AI's understanding</div>
</div>
</div>

</div>

</div>

---

# Be the Bridge

<div class="flex items-center h-full">

<div class="p-10 bg-gradient-to-br from-blue-50 to-emerald-50 dark:from-blue-900 dark:to-emerald-900 rounded-2xl border-l-8 border-emerald-500">

<div class="text-5xl mb-6 text-center">🌉</div>

<div class="text-2xl leading-relaxed italic">
"If I ask AI to 'make a quiz for my students,' it doesn't know their <span class="text-orange-600 dark:text-orange-300 font-bold">course level & modality</span>, what we <span class="text-blue-600 dark:text-blue-300 font-bold">just covered</span>, whether it's <span class="text-emerald-600 dark:text-emerald-300 font-bold">formative or summative</span>, or what <span class="text-green-600 dark:text-green-300 font-bold">accessibility + accommodations</span> are in play."
</div>

<div class="mt-8 text-2xl font-bold text-center text-emerald-600 dark:text-emerald-300">
My job is to be the bridge — to translate my tacit knowledge into explicit context.
</div>

</div>

</div>

---

# Theory of Mind → Context Engineering

<div class="my-4">

<div class="text-center mb-4 text-2xl font-bold">
<span class="line-through text-gray-400">PROMPT ENGINEERING</span>
<span class="mx-4">→</span>
<span class="text-blue-600 dark:text-blue-300">CONTEXT ENGINEERING</span>
</div>

<div class="grid grid-cols-2 gap-6 mt-4">

<div class="p-5 bg-gray-100 dark:bg-gray-800 rounded-xl">
<div class="text-3xl mb-2">❌</div>
<h3 class="text-xl font-bold mb-2">Prompt Engineering</h3>
<p class="text-base">Wordsmithing — finding the magic phrase, the clever trick</p>
</div>

<div class="p-5 bg-gradient-to-br from-blue-50 to-emerald-50 dark:from-blue-900 dark:to-emerald-900 rounded-xl border-2 border-blue-300"><div class="text-3xl mb-2">✅</div>
<h3 class="text-xl font-bold mb-2">Context Engineering</h3>
<p class="text-base"><strong>What information</strong> you include, not how cleverly you phrase it</p>
</div>

</div>

<div class="mt-4 p-4 bg-yellow-50 dark:bg-yellow-900 rounded-xl text-center text-lg">
💡 You don't need to learn <em>prompting</em>. You need to make your <strong>tacit knowledge explicit</strong>.
</div>

</div>

---

# The Three Stances

<div class="my-4">

<div class="space-y-3">

<div class="p-4 bg-red-50 dark:bg-red-900 rounded-xl border-l-4 border-red-500 flex items-start gap-4">
<div class="text-3xl">❌</div>
<div>
<div class="font-bold text-lg">Stance 1: Don't know the domain</div>
<div class="text-base">AI gives garbage mixed with gold, can't tell which</div>
</div>
</div>

<div class="p-4 bg-yellow-50 dark:bg-yellow-900 rounded-xl border-l-4 border-yellow-500 flex items-start gap-4">
<div class="text-3xl">⚠️</div>
<div>
<div class="font-bold text-lg">Stance 2: Know domain, resist adapting</div>
<div class="text-base">Only get time savings on rote tasks</div>
</div>
</div>

<div class="p-4 bg-gradient-to-r from-green-50 to-blue-50 dark:from-green-900 dark:to-blue-900 rounded-xl border-l-4 border-green-500 flex items-start gap-4">
<div class="text-3xl">🚀</div>
<div>
<div class="font-bold text-lg">Stance 3: Know domain + collaborate creatively</div>
<div class="text-base font-bold text-green-600 dark:text-green-300">DRAMATIC AMPLIFICATION</div>
</div>
</div>

</div>

<div class="mt-4 p-3 bg-blue-50 dark:bg-blue-900 rounded-xl text-center text-base">
<strong>You are domain experts in teaching and learning.</strong> Today we move you to <span class="text-green-600 dark:text-green-300 font-bold">Stance 3</span>.
</div>

</div>

---

# Architect, Not Coder

<div class="grid grid-cols-2 gap-12 items-center my-12">

<div class="text-center">
<div class="text-8xl mb-6">👨‍🏫</div>
<div class="text-3xl font-bold mb-4">You</div>
<div class="text-xl">Describe what your learners need</div>
<div class="text-lg mt-4 p-4 bg-emerald-50 dark:bg-emerald-900 rounded-lg">
Your expertise: <strong>Pedagogy</strong>
</div>
</div>

<div class="text-center">
<div class="text-8xl mb-6">🤖</div>
<div class="text-3xl font-bold mb-4">AI</div>
<div class="text-xl">Builds it</div>
<div class="text-lg mt-4 p-4 bg-blue-50 dark:bg-blue-900 rounded-lg">
AI expertise: <strong>HTML/JavaScript</strong>
</div>
</div>

</div>

<div class="mt-8 p-6 bg-gradient-to-r from-orange-50 to-pink-50 dark:from-orange-900 dark:to-pink-900 rounded-xl text-center text-2xl font-bold">
Never let "I can't code" stop you — your students won't either 🚀
</div>

---

# Iterate, Don't Perfect

<div class="grid grid-cols-2 gap-12 my-12">

<div class="p-8 bg-gray-100 dark:bg-gray-800 rounded-xl text-center">
<div class="text-6xl mb-4">❌</div>
<h3 class="text-2xl font-bold mb-4 line-through">Get prompt perfect first time</h3>
<div class="text-lg text-gray-500">Impossible and frustrating</div>
</div>

<div class="p-8 bg-gradient-to-br from-green-50 to-blue-50 dark:from-green-900 dark:to-blue-900 rounded-xl border-2 border-green-300">
<div class="text-6xl mb-4">✅</div>
<h3 class="text-2xl font-bold mb-4">Describe what's wrong</h3>
<div class="text-lg">Your first prompt won't be right.<br/><strong class="text-green-600 dark:text-green-300">That's expected and fine!</strong></div>
</div>

</div>

<div class="mt-8 text-center text-2xl">
<div class="p-6 bg-blue-50 dark:bg-blue-900 rounded-xl inline-block">
🔄 <strong>Iteration</strong> beats <s>perfection</s>
</div>
</div>

---

# Live Demo: Mental Models in Action

<div class="flex items-center justify-center h-full">

<div class="text-center max-w-3xl">

<div class="text-8xl mb-8">🎬</div>

<div class="text-3xl mb-8">Let me show you these mental models in action with examples I've built.</div>

<div class="p-6 bg-blue-50 dark:bg-blue-900 rounded-xl text-xl">
Watch for: <strong>Theory of Mind</strong>, <strong>Context Engineering</strong>, and <strong>Iteration</strong> in practice
</div>

</div>

</div>

---

<div class="h-full flex items-center justify-center bg-gradient-to-br from-green-500 to-blue-500 text-white">
<div class="text-center">
<div class="text-8xl font-bold mb-4">PART 2</div>
<div class="text-4xl mb-8">Your Tools</div>
<div class="text-2xl opacity-90">Excalidraw → Google AI Studio</div>
</div>
</div>

---

# Your Tools

<div class="text-center my-16">

<div class="text-xl mb-8">Let's talk about the tools you'll use today — and can teach your students.</div>

<div class="flex justify-center items-center gap-8 text-5xl">
<div>✏️ <span class="text-2xl">Excalidraw</span></div>
<div class="text-blue-500">→</div>
<div>🤖 <span class="text-2xl">AI Studio</span></div>
<div class="text-blue-500">→</div>
<div>🚀 <span class="text-2xl">Live App</span></div>
</div>

</div>

---

# The Flow

<div class="grid grid-cols-3 gap-6 my-12">

<div class="text-center p-6 bg-gradient-to-br from-yellow-50 to-orange-50 dark:from-yellow-900 dark:to-orange-900 rounded-xl border-2 border-yellow-300">

<div class="text-5xl mb-4">✏️</div>
<div class="text-3xl font-bold mb-2">STEP 1</div>
<div class="text-2xl font-bold mb-4 text-yellow-600 dark:text-yellow-300">Excalidraw</div>
<div class="text-xl font-bold mb-3">Sketch your idea</div>
<ul class="text-left text-base space-y-1">
<li>✓ Low stakes</li>
<li>✓ Visual brainstorm</li>
<li>✓ excalidraw.com</li>
</ul>

</div>

<div class="text-center p-6 bg-gradient-to-br from-blue-50 to-emerald-50 dark:from-blue-900 dark:to-emerald-900 rounded-xl border-2 border-blue-300">

<div class="text-5xl mb-4">🤖</div>
<div class="text-3xl font-bold mb-2">STEP 2</div>
<div class="text-2xl font-bold mb-4 text-blue-600 dark:text-blue-300">AI Studio</div>
<div class="text-xl font-bold mb-3">Make it real</div>
<ul class="text-left text-base space-y-1">
<li>✓ Iterate with chat</li>
<li>✓ See live preview</li>
<li>✓ aistudio.google.com</li>
</ul>

</div>

<div class="text-center p-6 bg-gradient-to-br from-green-50 to-teal-50 dark:from-green-900 dark:to-teal-900 rounded-xl border-2 border-green-300">

<div class="text-5xl mb-4">🚀</div>
<div class="text-3xl font-bold mb-2">STEP 3</div>
<div class="text-2xl font-bold mb-4 text-green-600 dark:text-green-300">Netlify Drop</div>
<div class="text-xl font-bold mb-3">Drag, drop, live</div>
<ul class="text-left text-base space-y-1">
<li>✓ No signup needed</li>
<li>✓ Live URL in seconds</li>
<li>✓ app.netlify.com/drop</li>
</ul>

</div>

</div>

---

# Higher-Ed Guardrails

<div class="max-w-4xl mx-auto my-12">

<div class="p-8 bg-gradient-to-br from-yellow-50 to-orange-50 dark:from-yellow-900 dark:to-orange-900 rounded-2xl border-l-8 border-yellow-500">

<div class="text-2xl font-bold mb-4">Before you build</div>

<ul class="text-lg space-y-3">
  <li>🔒 <strong>Privacy:</strong> don’t paste student PII (names, IDs, grades). Use synthetic examples.</li>
  <li>♿ <strong>Accessibility:</strong> check contrast, headings, keyboard use, and accommodations/UDL.</li>
  <li>🎯 <strong>Alignment:</strong> tie the tool to outcomes + assessment intent (formative vs summative).</li>
  <li>📚 <strong>Copyright:</strong> respect licensed content; cite sources and avoid uploading PDFs.</li>
  <li>🏫 <strong>Policy:</strong> follow your institution's guidance for AI / privacy / security before production use.</li>
</ul>

</div>

</div>

---

# Sketch First (Two Options)

<div class="grid grid-cols-2 gap-8 my-6">

<div class="p-6 bg-yellow-50 dark:bg-yellow-900 rounded-xl">
<div class="text-4xl mb-3">💻</div>
<h3 class="text-xl font-bold mb-2">Option A: Excalidraw</h3>
<ul class="text-base space-y-1">
<li>• excalidraw.com</li>
<li>• Sketch boxes, buttons, text</li>
<li>• Export as PNG</li>
</ul>
</div>

<div class="p-6 bg-orange-50 dark:bg-orange-900 rounded-xl">
<div class="text-4xl mb-3">📝</div>
<h3 class="text-xl font-bold mb-2">Option B: Paper + Phone</h3>
<ul class="text-base space-y-1">
<li>• Sketch on paper</li>
<li>• Take a photo</li>
<li>• Upload to AI Studio</li>
</ul>
</div>

</div>

<div class="mt-4 p-4 bg-blue-50 dark:bg-blue-900 rounded-lg text-center">
💡 Both work equally well — AI Studio accepts any image
</div>

<div class="mt-3 p-3 bg-orange-50 dark:bg-orange-900 rounded-lg text-center text-sm">
📱 Phone tip: take the photo on your phone, then AirDrop/email it to yourself and continue on your laptop. Netlify Drop is desktop-friendly.
</div>

---

# Screenshot + Remix (Fastest Path)

<div class="grid grid-cols-4 gap-4 my-6">

<div class="p-4 bg-gray-100 dark:bg-gray-800 rounded-xl text-center">
<div class="text-4xl mb-2">📸</div>
<div class="text-sm font-bold">1. Screenshot</div>
<div class="text-xs mt-1">Any website, PDF, app, or tool you like</div>
</div>

<div class="p-4 bg-yellow-100 dark:bg-yellow-900 rounded-xl text-center">
<div class="text-4xl mb-2">📋</div>
<div class="text-sm font-bold">2. Paste into Excalidraw</div>
<div class="text-xs mt-1">Or upload directly to AI Studio</div>
</div>

<div class="p-4 bg-orange-100 dark:bg-orange-900 rounded-xl text-center">
<div class="text-4xl mb-2">✏️</div>
<div class="text-sm font-bold">3. Annotate</div>
<div class="text-xs mt-1">"Change this to X" / "Add Y here"</div>
</div>

<div class="p-4 bg-green-100 dark:bg-green-900 rounded-xl text-center">
<div class="text-4xl mb-2">🚀</div>
<div class="text-sm font-bold">4. Upload + Build</div>
<div class="text-xs mt-1">AI creates your customized version</div>
</div>

</div>

<div class="p-6 bg-gradient-to-r from-emerald-50 to-blue-50 dark:from-emerald-900 dark:to-blue-900 rounded-xl mt-4">
<div class="text-xl font-bold mb-3">Why this works:</div>
<div class="grid grid-cols-2 gap-4 text-base">
<div>✓ No blank page problem — you have a starting point</div>
<div>✓ Shows the AI exactly what you want</div>
<div>✓ Your annotations = your customizations</div>
<div>✓ Output: single HTML+JS page you can host free</div>
</div>
</div>

---

<div class="h-full flex items-center justify-center bg-gradient-to-br from-yellow-400 to-orange-500 text-white">
<div class="text-center">
<div class="text-9xl mb-8">🎨</div>
<div class="text-7xl font-bold mb-6">BUILD SESSION 1</div>
<div class="text-4xl mb-4">Brainstorm in Excalidraw</div>
<div class="text-6xl font-bold">8 minutes</div>
</div>
</div>

---

# Three Ways to Start

<div class="grid grid-cols-3 gap-4 my-4">

<div class="p-4 bg-gradient-to-br from-green-50 to-emerald-100 dark:from-green-900 dark:to-emerald-800 rounded-xl border-2 border-green-400">
<div class="text-3xl mb-2">📸</div>
<h3 class="text-lg font-bold text-green-700 dark:text-green-300">Fastest: Screenshot + Remix</h3>
<div class="text-sm mt-2 space-y-1">
<div>1. Screenshot a website, PDF, or app you like</div>
<div>2. Paste into Excalidraw</div>
<div>3. Add text annotations: "change this", "add that"</div>
<div>4. Upload to AI Studio</div>
</div>
<div class="mt-3 text-xs bg-green-200 dark:bg-green-700 p-2 rounded">Best for: "I want something like THIS but for MY class"</div>
</div>

<div class="p-4 bg-gradient-to-br from-yellow-50 to-orange-100 dark:from-yellow-900 dark:to-orange-800 rounded-xl">
<div class="text-3xl mb-2">📝</div>
<h3 class="text-lg font-bold">Pick a Template</h3>
<div class="text-sm mt-2 space-y-1">
<div>📚 Vocabulary flashcards</div>
<div>🎲 Random student picker</div>
<div>⏰ Activity timer</div>
<div>✅ Quick formative quiz</div>
<div>📝 Exit ticket</div>
</div>
<div class="mt-3 text-xs bg-yellow-200 dark:bg-yellow-700 p-2 rounded">Best for: "I know what I need"</div>
</div>

<div class="p-4 bg-gradient-to-br from-blue-50 to-indigo-100 dark:from-blue-900 dark:to-indigo-800 rounded-xl">
<div class="text-3xl mb-2">💡</div>
<h3 class="text-lg font-bold">Solve Your Pain Point</h3>
<div class="text-sm mt-2 space-y-1">
<div>What takes too long?</div>
<div>What do students struggle with?</div>
<div>What's tedious every week?</div>
</div>
<div class="mt-3 text-xs bg-blue-200 dark:bg-blue-700 p-2 rounded">Best for: "I have a specific problem"</div>
</div>

</div>

<div class="mt-4 p-3 bg-blue-100 dark:bg-blue-800 rounded-lg text-center">
<div class="text-base font-bold mb-1">📋 Drop sketches + finished URLs here</div>
<div class="text-sm">Padlet: <span class="underline font-mono">go.illinois.edu/lltlc</span></div>
</div>

---

<div class="h-full flex items-center justify-center bg-gradient-to-br from-blue-500 to-emerald-600 text-white">
<div class="text-center">
<div class="text-9xl mb-8">🚀</div>
<div class="text-7xl font-bold mb-6">BUILD SESSION 2</div>
<div class="text-4xl mb-4">Make It Real in AI Studio</div>
<div class="text-6xl font-bold">15 minutes</div>
</div>
</div>

---

# AI Studio: Chat Mode

- Open **aistudio.google.com** → **Chat** (not Build — Chat gives you a single HTML file)
- Upload your sketch / screenshot / paper photo
- Ask: *"Generate a single HTML file with inline CSS and JS — no external libraries — that does X"*
- When you like it, save the file → drag onto **app.netlify.com/drop** → live URL in seconds
- Then iterate: "Make the button bigger" / "Add a score counter" / "Make it work on mobile"

---

# Remember: Iterate

Try saying:
- "Make the button bigger"
- "Add a score counter"
- "Change colors to match my school"
- "Make it work on mobile"

**THEORY OF MIND CHECK**
- "What context is the AI missing?"
- "What assumption is it making?"

---

<div class="h-full flex items-center justify-center bg-gradient-to-br from-emerald-600 to-pink-500 text-white">
<div class="text-center">
<div class="text-8xl font-bold mb-4">CLOSING</div>
<div class="text-4xl opacity-90">What's Next</div>
<div class="text-2xl mt-8">Let's bring it home</div>
</div>
</div>

---

# The Multiplier Effect

<div class="grid grid-cols-2 gap-8 items-center my-8">

<div class="text-center">
<div class="p-6 bg-blue-50 dark:bg-blue-900 rounded-2xl">
<div class="text-4xl mb-3">👨‍🏫</div>
<div class="text-xl font-bold">You — an educator — just built something</div>
<div class="text-4xl font-bold text-blue-600 dark:text-blue-300 my-3">in an hour</div>
</div>

<div class="text-4xl my-4">⬇️</div>

<div class="p-6 bg-gradient-to-r from-emerald-50 to-pink-50 dark:from-emerald-900 dark:to-pink-900 rounded-2xl">
<div class="text-xl font-bold mb-2">Now imagine your students doing this</div>
<div class="text-5xl">🚀</div>
</div>
</div>

<div class="text-center">
<div class="p-6 bg-gradient-to-br from-green-100 to-teal-100 dark:from-green-900 dark:to-teal-900 rounded-2xl">
<div class="text-xl mb-4">If you teach <span class="text-4xl font-bold text-blue-600 dark:text-blue-300">30 students</span> to be builders...</div>

<div class="text-3xl my-4">×</div>

<div class="text-xl mb-2">Each creates one tool =</div>
<div class="text-5xl font-bold text-green-600 dark:text-green-300">30 new</div>
<div class="text-lg mt-2">learning resources — created by the people who need them most</div>
</div>
</div>

</div>

---

# Same Principles, For Students

<div class="grid grid-cols-3 gap-6 my-8">

<div class="p-4 bg-gradient-to-br from-orange-50 to-orange-100 dark:from-orange-900 dark:to-orange-800 rounded-xl text-center">
<div class="text-5xl mb-3">⚡</div>
<h3 class="text-xl font-bold mb-2 text-orange-600 dark:text-orange-300">AGENCY</h3>
<p class="text-base">When students build their own study tools, they <strong>own their learning</strong></p>
</div>

<div class="p-4 bg-gradient-to-br from-blue-50 to-blue-100 dark:from-blue-900 dark:to-blue-800 rounded-xl text-center">
<div class="text-5xl mb-3">🔄</div>
<h3 class="text-xl font-bold mb-2 text-blue-600 dark:text-blue-300">ITERATION</h3>
<p class="text-base">"Fix what's wrong" beats "get it right the first time"</p>
</div>

<div class="p-4 bg-gradient-to-br from-emerald-50 to-emerald-100 dark:from-emerald-900 dark:to-emerald-800 rounded-xl text-center">
<div class="text-5xl mb-3">🔍</div>
<h3 class="text-xl font-bold mb-2 text-emerald-600 dark:text-emerald-300">CURIOSITY</h3>
<p class="text-base">"What else could I build?" — the question we want them asking</p>
</div>

</div>

---

# For Faculty

<div class="space-y-6 my-8">

<div class="p-6 bg-gradient-to-r from-emerald-100 to-blue-100 dark:from-emerald-900 dark:to-blue-900 rounded-xl border-l-8 border-emerald-500">
<div class="text-4xl mb-4">📅</div>
<div class="text-xl font-bold mb-2">Pick ONE class session or module in the next 2 weeks</div>
<div class="text-lg">where students <strong>BUILD</strong> instead of consume</div>
</div>

<div class="grid grid-cols-2 gap-6">

<div class="p-4 bg-orange-50 dark:bg-orange-900 rounded-xl text-center">
<div class="text-4xl mb-3">🤝</div>
<div class="text-lg font-bold mb-1">Right now:</div>
<div class="text-base">Find an accountability partner at work</div>
</div>

<div class="p-4 bg-green-50 dark:bg-green-900 rounded-xl text-center">
<div class="text-4xl mb-3">🔗</div>
<div class="text-lg font-bold mb-1">Right now:</div>
<div class="text-base">Post your Netlify URL on the Padlet</div>
</div>

</div>

</div>

---

# Resources

<div class="grid grid-cols-2 gap-4 my-8">

<div class="p-4 bg-yellow-50 dark:bg-yellow-900 rounded-xl">
<div class="text-3xl mb-2">✏️</div>
<h3 class="text-lg font-bold mb-1">Brainstorm</h3>
<div class="text-base font-mono">excalidraw.com</div>
</div>

<div class="p-4 bg-blue-50 dark:bg-blue-900 rounded-xl">
<div class="text-3xl mb-2">🤖</div>
<h3 class="text-lg font-bold mb-1">Build</h3>
<div class="text-base font-mono">aistudio.google.com</div>
</div>

<div class="p-4 bg-emerald-50 dark:bg-emerald-900 rounded-xl">
<div class="text-3xl mb-2">🎨</div>
<h3 class="text-lg font-bold mb-1">App Gallery</h3>
<div class="text-base">AI Studio → App Gallery</div>
</div>

<div class="p-4 bg-green-50 dark:bg-green-900 rounded-xl">
<div class="text-3xl mb-2">📚</div>
<h3 class="text-lg font-bold mb-1">Free Course (2 hrs)</h3>
<div class="text-base font-mono">grow.google/ai-for-educators</div>
</div>

</div>

<div class="mt-6 p-4 bg-gradient-to-r from-blue-100 to-emerald-100 dark:from-blue-900 dark:to-emerald-900 rounded-xl text-center text-lg">
📋 <strong>Padlet (share your URLs):</strong> <span class="font-mono underline">go.illinois.edu/lltlc</span>
</div>

---

# Exit Ticket

<div class="space-y-4 my-6">

<div class="p-4 bg-gradient-to-r from-yellow-100 to-orange-100 dark:from-yellow-900 dark:to-orange-900 rounded-xl border-l-8 border-yellow-500">
<div class="text-3xl mb-2">💡</div>
<div class="text-lg font-bold">One thing that clicked</div>
</div>

<div class="p-4 bg-gradient-to-r from-blue-100 to-emerald-100 dark:from-blue-900 dark:to-emerald-900 rounded-xl border-l-8 border-blue-500">
<div class="text-3xl mb-2">❓</div>
<div class="text-lg font-bold">One thing still fuzzy</div>
</div>

<div class="p-4 bg-gradient-to-r from-green-100 to-teal-100 dark:from-green-900 dark:to-teal-900 rounded-xl border-l-8 border-green-500">
<div class="text-3xl mb-2">🚀</div>
<div class="text-lg font-bold">What will you build — or have your students build — in the next 2 weeks of your course?</div>
</div>

</div>

---

<div class="h-full flex items-center justify-center bg-gradient-to-br from-emerald-600 via-blue-600 to-green-500 text-white">

<div class="text-center max-w-4xl p-12">

<div class="text-8xl mb-8">🎉</div>

<div class="text-7xl font-bold mb-8">Thank You!</div>

<div class="text-5xl font-bold mb-12 animate-pulse">
Now go build something.
</div>

<div class="space-y-4 text-2xl bg-white bg-opacity-20 p-8 rounded-2xl backdrop-blur">
<div>📧 https://chatwithgpt.substack.com/</div>
<div>💼 LinkedIn - vishalsachdev</div>
</div>

<div class="mt-12 text-xl leading-relaxed">
Thank you for being here today.<br/>
I can't wait to see what <strong>you create</strong><br/>
— and what <strong>your students create</strong> after you teach them.
</div>

</div>

</div>
