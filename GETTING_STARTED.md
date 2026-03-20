# Getting Started with the AI Dev System

> You don't need to know what MVC is. You don't need to be technical.
> This guide explains everything from scratch and gets you up and running in 15 minutes.

---

## What Problem Does This Solve?

Imagine hiring a brilliant contractor. They're incredible at their job. But every Monday morning, they walk in with **complete amnesia** — no memory of what they built last week, what decisions you made together, or how your project is organized.

That's what working with an AI is like by default.

This system gives your AI a **persistent memory** — a set of structured files that live in your project. The AI reads them at the start of every session and picks up exactly where you left off. The longer you work together, the smarter and more useful it gets.

---

## The 3 Types of Memory

Think of it like a new employee's onboarding materials:

| Memory Type | What it's like | Where it lives |
|---|---|---|
| **Tier 1 — Always loaded** | The company handbook | Auto-loaded by your AI tool |
| **Tier 2 — Session context** | Your project's current state | `.agents/memory/[app].md` |
| **Tier 3 — Deep docs** | Technical specifications | `[app]/memory/[feature]_component_memory.md` |

You don't need to manage Tier 1 — your AI tool handles it. For Tier 2, you'll run `/save-memory` at the end of sessions. Tier 3 is generated automatically when you finish a significant feature.

---

## What is MVC?

MVC stands for **Model, View, Controller**. It's a way of organizing your code so everyone (human and AI) always knows where things belong.

**Think of it like a restaurant:**

| MVC Layer | Restaurant equivalent | In your code |
|---|---|---|
| **Model** | The recipe cards | Database tables, data shapes |
| **Controller** | The kitchen manager | API routes, business logic |
| **View** | The menu the customer sees | Frontend pages, UI components |

Every file in your project belongs to one of these layers. The AI knows exactly where to create new files and where to look for existing ones.

---

## Your First 15 Minutes

### Step 1: Clone and set up
```bash
git clone https://github.com/heyisforhumans/ai-dev-system-template /path/to/your/project
cp .env.template .env
# Open .env and add your AI_API_KEY
```

### Step 2: Open the folder in your AI tool
Point your AI coding assistant (Antigravity, Cursor, Claude, etc.) at this folder. See [`docs/platform-guide.md`](./docs/platform-guide.md) if you're not sure how.

### Step 3: Send the first prompt

**This is the only non-obvious step.** Your AI won't self-activate by just having the files — you need to tell it what to do once.

Open **[`FIRST_PROMPT.md`](./FIRST_PROMPT.md)** in this folder and copy-paste the message inside. Send it as your first message.

The AI will respond:

> *"👋 Hey — it looks like this is your first session with the AI Dev System. This memory stack is modeled after Rails MVC conventions, adapted for AI-assisted development. Would you like me to walk you through how it works and help you configure your workspace?"*

Say yes. It walks you through filling in `BOOTSTRAP.md` (~10 minutes). After that, you never need to explain your project again.

### Step 4: Start building
Use `/new-app` when you're ready to start a project:
> "Let's start a new app called [name]"

The AI creates the entire MVC folder structure and all memory files automatically.

---

## Key Workflows (Commands You'll Use)

| Command | When to use |
|---|---|
| `/kickoff` | Start of every session — AI orients itself |
| `/save-memory` | End of every session — AI writes facts to memory files |
| `/new-app` | Starting a new application |
| `/debug` | When something is broken and you're not sure why |
| `/memory-model-component` | After finishing a major feature |
| `/retrospective` | After a sprint or big feature — capture lessons learned |

---

## The File Structure You'll See

Every project follows the same MVC layout:

```
your-project/
├── backend/
│   └── app/
│       ├── models/      ← The Librarian (data shapes)
│       ├── routers/     ← The Manager (business logic)
│       └── schemas.py   ← The Presenter (API surface)
├── frontend/
│   └── src/
│       ├── pages/       ← Full-page views
│       └── components/  ← Reusable UI pieces
├── memory/              ← AI component docs (not deployed)
├── docs/                ← Human documentation
└── RUNBOOK.md           ← How to deploy and operate this app
```

See [`docs/file-structure.md`](./docs/file-structure.md) for the full annotated version.

---

## What to Read Next

- [`docs/how-mvc-works.md`](./docs/how-mvc-works.md) — deeper MVC explanation with examples
- [`docs/how-memory-works.md`](./docs/how-memory-works.md) — how the 3-tier memory system works
- [`docs/platform-guide.md`](./docs/platform-guide.md) — specific notes for your AI tool
- [`docs/writing-your-first-skill.md`](./docs/writing-your-first-skill.md) — customizing the system for your stack
