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

Welcome, educators. Today's workshop is about a **fundamental shift**:

<div class="mt-8 text-center text-2xl font-bold text-blue-500">
Teachers as Content Deliverers → Teachers as Builders
</div>

<div class="mt-12 p-6 bg-blue-50 dark:bg-blue-900 rounded-lg">
🎯 By the end of this session, you'll have built something real that you can use Monday morning.
</div>

</div>

---

# The Shift

<div class="grid grid-cols-2 gap-8">

<div class="p-6 bg-gray-100 dark:bg-gray-800 rounded-lg">

<div class="flex items-center gap-3 mb-4">
<div class="text-3xl">📉</div>
<h2 class="text-2xl font-bold">YESTERDAY</h2>
</div>

- 🤖 Assessments AI can game
- 📺 Teachers deliver content
- 🛋️ Students consume
- ⏱️ Shrinking attention spans

</div>

<div class="p-6 bg-blue-50 dark:bg-blue-900 rounded-lg border-2 border-blue-300">

<div class="flex items-center gap-3 mb-4">
<div class="text-3xl">📈</div>
<h2 class="text-2xl font-bold">TODAY</h2>
</div>

- ⚡ Projects requiring agency
- 🔧 Teachers BUILD tools
- 🎨 Students CREATE
- 🔥 Curiosity & ownership

</div>

</div>

---

# The Problem

<div class="grid grid-cols-2 gap-12 items-center my-12">

<div class="space-y-8">

<div class="text-4xl">❌</div>

### Traditional assessments?
**AI can game them.**

<div class="text-4xl">📉</div>

### Students consuming content?
**Their attention spans are shrinking.**

</div>

<div class="p-8 bg-gradient-to-br from-blue-50 to-emerald-50 dark:from-blue-900 dark:to-emerald-900 rounded-xl">

<div class="text-5xl mb-6">💡</div>

### The New Paradigm

Teachers build tools for their **specific context**

Students become **creators**, not consumers

</div>

</div>

---

# The Arc

<div class="flex justify-between items-center my-16">
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

# The Philosophy

<div class="my-12">

<div class="text-center p-8 bg-gradient-to-r from-emerald-100 to-blue-100 dark:from-emerald-900 dark:to-blue-900 rounded-2xl border-l-4 border-emerald-500">
<div class="text-3xl font-bold italic leading-relaxed">
"Not by banning AI,<br/>but by making creation the default."
</div>
</div>

<div class="mt-12 text-lg leading-relaxed space-y-4">

This is the arc of today:

<div class="grid grid-cols-3 gap-6 mt-8">
<div class="p-4 bg-blue-50 dark:bg-blue-900 rounded-lg text-center">
<div class="text-3xl mb-2">1️⃣</div>
YOU become builders
</div>
<div class="p-4 bg-blue-50 dark:bg-blue-900 rounded-lg text-center">
<div class="text-3xl mb-2">2️⃣</div>
You teach students to build
</div>
<div class="p-4 bg-blue-50 dark:bg-blue-900 rounded-lg text-center">
<div class="text-3xl mb-2">3️⃣</div>
Engagement transforms
</div>
</div>

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

# Mental Models

<div class="text-xl text-center my-16">

Now let's talk about **HOW** to work with AI effectively.

<div class="text-3xl mt-8 mb-4">🧠</div>

These mental models will serve you **far beyond today**.

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
The skill that makes you great at AI isn't technical.<br/>
It's <strong>social</strong>. It's about <strong>perspective-taking</strong>.
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
"If I ask AI to 'make a quiz for my students,' it doesn't know their <span class="text-orange-600 dark:text-orange-300 font-bold">reading level</span>, what we <span class="text-blue-600 dark:text-blue-300 font-bold">just covered</span>, whether it's <span class="text-emerald-600 dark:text-emerald-300 font-bold">formative or summative</span>, or that half my class are <span class="text-green-600 dark:text-green-300 font-bold">ELL students</span>.
</div>

<div class="mt-8 text-2xl font-bold text-center text-emerald-600 dark:text-emerald-300">
My job is to be the bridge — to translate my tacit knowledge into explicit context.
</div>

</div>

</div>

---

# Theory of Mind → Context Engineering

<div class="my-12">

<div class="text-center mb-8 text-3xl font-bold">
<span class="line-through text-gray-400">PROMPT ENGINEERING</span>
<span class="mx-4">→</span>
<span class="text-blue-600 dark:text-blue-300">CONTEXT ENGINEERING</span>
</div>

<div class="grid grid-cols-2 gap-8 mt-12">

<div class="p-8 bg-gray-100 dark:bg-gray-800 rounded-xl">
<div class="text-4xl mb-4">❌</div>
<h3 class="text-xl font-bold mb-3">Prompt Engineering</h3>
<p class="text-lg">Wordsmithing — finding the magic phrase, the clever trick</p>
</div>

<div class="p-8 bg-gradient-to-br from-blue-50 to-emerald-50 dark:from-blue-900 dark:to-emerald-900 rounded-xl border-2 border-blue-300">
<div class="text-4xl mb-4">✅</div>
<h3 class="text-xl font-bold mb-3">Context Engineering</h3>
<p class="text-lg"><strong>What information</strong> you include, not how cleverly you phrase it</p>
</div>

</div>

<div class="mt-10 p-6 bg-yellow-50 dark:bg-yellow-900 rounded-xl text-center text-xl">
💡 You don't need to learn <em>prompting</em>.<br/>
You need to make your <strong>tacit knowledge explicit</strong>.
</div>

</div>

---

# The Three Stances

<div class="my-8">

<div class="space-y-6">

<div class="p-6 bg-red-50 dark:bg-red-900 rounded-xl border-l-4 border-red-500 flex items-start gap-4">
<div class="text-4xl">❌</div>
<div>
<div class="font-bold text-xl mb-2">Stance 1: Don't know the domain</div>
<div class="text-lg">AI gives garbage mixed with gold, can't tell which</div>
</div>
</div>

<div class="p-6 bg-yellow-50 dark:bg-yellow-900 rounded-xl border-l-4 border-yellow-500 flex items-start gap-4">
<div class="text-4xl">⚠️</div>
<div>
<div class="font-bold text-xl mb-2">Stance 2: Know domain, resist adapting</div>
<div class="text-lg">Only get time savings on rote tasks</div>
</div>
</div>

<div class="p-6 bg-gradient-to-r from-green-50 to-blue-50 dark:from-green-900 dark:to-blue-900 rounded-xl border-l-4 border-green-500 flex items-start gap-4">
<div class="text-4xl">🚀</div>
<div>
<div class="font-bold text-xl mb-2">Stance 3: Know domain + collaborate creatively</div>
<div class="text-lg font-bold text-green-600 dark:text-green-300">DRAMATIC AMPLIFICATION</div>
</div>
</div>

</div>

<div class="mt-10 p-6 bg-blue-50 dark:bg-blue-900 rounded-xl text-center text-xl">
<strong>You are domain experts in teaching and learning.</strong><br/>
Today we move you to <span class="text-green-600 dark:text-green-300 font-bold">Stance 3</span>.
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

# LIVE DEMO

# Examples

## Mental models in action

Now let me show you these mental models in action with some examples I've built.

---

<div class="h-full flex items-center justify-center bg-gradient-to-br from-green-500 to-blue-500 text-white">
<div class="text-center">
<div class="text-8xl font-bold mb-4">PART 2</div>
<div class="text-4xl mb-8">Your Tools</div>
<div class="text-2xl opacity-90">tldraw → Google AI Studio</div>
</div>
</div>

---

# Your Tools

<div class="text-center my-16">

<div class="text-xl mb-8">Let's talk about the tools you'll use today — and can teach your students.</div>

<div class="flex justify-center items-center gap-8 text-5xl">
<div>✏️ <span class="text-2xl">tldraw</span></div>
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
<div class="text-2xl font-bold mb-4 text-yellow-600 dark:text-yellow-300">tldraw</div>
<div class="text-xl font-bold mb-3">Sketch your idea</div>
<ul class="text-left text-base space-y-1">
<li>✓ Low stakes</li>
<li>✓ Visual brainstorm</li>
<li>✓ makereal.tldraw.com</li>
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

<div class="text-center p-6 bg-gradient-to-br from-green-50 to-teal-50 dark:from-green-900 dark:to-teal-900 rounded-xl border-2 border-green-300 border-dashed opacity-80">

<div class="text-5xl mb-4">🚀</div>
<div class="text-3xl font-bold mb-2">STEP 3 <span class="text-base font-normal">(optional)</span></div>
<div class="text-2xl font-bold mb-4 text-green-600 dark:text-green-300">GitHub</div>
<div class="text-xl font-bold mb-3">Save your work</div>
<ul class="text-left text-base space-y-1">
<li>✓ Publish live</li>
<li>✓ Build portfolio</li>
<li>✓ github.com</li>
</ul>

</div>

</div>

---

# tldraw: Sketch First

- Lowers the "blank page" problem
- You're drawing, not coding
- Sketch boxes, buttons, text. Ugly is fine.
- Share with others
  - Invite by email, publish online, export PNG

**Open now:**  
makereal.tldraw.com

---

<div class="h-full flex items-center justify-center bg-gradient-to-br from-yellow-400 to-orange-500 text-white">
<div class="text-center">
<div class="text-9xl mb-8">🎨</div>
<div class="text-7xl font-bold mb-6">BUILD SESSION 1</div>
<div class="text-4xl mb-4">Brainstorm in tldraw</div>
<div class="text-6xl font-bold">8 minutes</div>
</div>
</div>

---

# Pick One to Build

<div class="grid grid-cols-2 gap-4 my-4">

<div class="p-3 bg-blue-50 dark:bg-blue-900 rounded-lg hover:scale-105 transition">
📚 <strong>Vocabulary flashcards</strong>
<div class="text-sm text-gray-600 dark:text-gray-400">For any subject — students can make their own too</div>
</div>

<div class="p-3 bg-emerald-50 dark:bg-emerald-900 rounded-lg hover:scale-105 transition">
🎲 <strong>Random student picker</strong>
<div class="text-sm text-gray-600 dark:text-gray-400">Fair participation, add your class names</div>
</div>

<div class="p-3 bg-green-50 dark:bg-green-900 rounded-lg hover:scale-105 transition">
⏰ <strong>Activity timer</strong>
<div class="text-sm text-gray-600 dark:text-gray-400">Transitions, group work, think-pair-share</div>
</div>

<div class="p-3 bg-orange-50 dark:bg-orange-900 rounded-lg hover:scale-105 transition">
✅ <strong>Quick formative quiz</strong>
<div class="text-sm text-gray-600 dark:text-gray-400">Check understanding on today's lesson</div>
</div>

<div class="p-3 bg-pink-50 dark:bg-pink-900 rounded-lg hover:scale-105 transition">
📝 <strong>Exit ticket</strong>
<div class="text-sm text-gray-600 dark:text-gray-400">What clicked? What's still fuzzy?</div>
</div>

<div class="p-3 bg-teal-50 dark:bg-teal-900 rounded-lg hover:scale-105 transition">
🎯 <strong>Learning objective tracker</strong>
<div class="text-sm text-gray-600 dark:text-gray-400">Students self-assess against goals</div>
</div>

</div>

<div class="mt-4 p-4 bg-gradient-to-r from-yellow-50 to-orange-50 dark:from-yellow-900 dark:to-orange-900 rounded-xl text-center text-lg">
💡 <strong>Or...</strong> solve a real challenge from your classroom!<br/>
<span class="text-base">All of these are achievable — and you can assign them to students too.</span>
</div>

<div class="mt-4 p-3 bg-blue-100 dark:bg-blue-800 rounded-lg text-center">
<div class="text-base font-bold mb-1">📋 Track your progress</div>
<div class="text-sm">Open the shared worksheet: <a href="https://github.com/vishalsachdev/build-to-learn/blob/main/materials/2025-01-09-future-world-alliance-online/worksheet.md" target="_blank" class="underline font-mono">go.illinois.edu/buildtolearn</a></div>
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

# AI Studio: Build Mode

- Export tldraw sketch as PNG (or describe it)
- Open aistudio.google.com → Build mode
- Paste image or describe what you want
- Iterate: "Make the button bigger" / "Add a score counter" / "Add AI features"

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

# The Multiplier

<div class="flex items-center justify-center h-full">

<div class="text-center">

<div class="p-6 bg-blue-50 dark:bg-blue-900 rounded-2xl mb-8">
<div class="text-4xl mb-3">👨‍🏫</div>
<div class="text-2xl font-bold">You — an educator — just built something</div>
<div class="text-5xl font-bold text-blue-600 dark:text-blue-300 my-3">in an hour</div>
</div>

<div class="text-5xl mb-6">⬇️</div>

<div class="p-6 bg-gradient-to-r from-emerald-50 to-pink-50 dark:from-emerald-900 dark:to-pink-900 rounded-2xl">
<div class="text-2xl font-bold mb-3">Now imagine</div>
<div class="text-4xl font-bold text-emerald-600 dark:text-emerald-300">your students doing this</div>
<div class="text-6xl mt-4">🚀</div>
</div>

</div>

</div>

---

# Scale the Impact

<div class="flex items-center justify-center h-full">

<div class="text-center max-w-3xl">

<div class="text-2xl mb-6">If you teach</div>

<div class="p-6 bg-gradient-to-r from-blue-100 to-emerald-100 dark:from-blue-900 dark:to-emerald-900 rounded-2xl mb-6">
<div class="text-6xl font-bold text-blue-600 dark:text-blue-300">30 students</div>
<div class="text-xl mt-3">to be builders too</div>
</div>

<div class="text-4xl my-6">×</div>

<div class="p-6 bg-gradient-to-r from-green-100 to-teal-100 dark:from-green-900 dark:to-teal-900 rounded-2xl">
<div class="text-xl mb-3">Each creates one tool =</div>
<div class="text-6xl font-bold text-green-600 dark:text-green-300">30 new</div>
<div class="text-2xl mt-3">learning resources — created by the people who need them most</div>
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

# For Teachers

<div class="space-y-6 my-8">

<div class="p-6 bg-gradient-to-r from-emerald-100 to-blue-100 dark:from-emerald-900 dark:to-blue-900 rounded-xl border-l-8 border-emerald-500">
<div class="text-4xl mb-4">📅</div>
<div class="text-xl font-bold mb-2">Pick ONE lesson in the next 2 weeks</div>
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
<div class="text-base">Post your app URL in the doc</div>
</div>

</div>

</div>

---

# Resources

<div class="grid grid-cols-2 gap-4 my-8">

<div class="p-4 bg-yellow-50 dark:bg-yellow-900 rounded-xl">
<div class="text-3xl mb-2">✏️</div>
<h3 class="text-lg font-bold mb-1">Brainstorm</h3>
<div class="text-base font-mono">makereal.tldraw.com</div>
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
📄 <strong>Today's prompt library + portfolios:</strong> [shared doc link]
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
<div class="text-lg font-bold">What will you build — or have your students build — in the next 2 weeks?</div>
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
