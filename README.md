# AI Dev System Template

> A portable, model-agnostic memory and workflow system for AI-assisted software development.
> Modeled after Rails MVC conventions. Works with Antigravity, Claude, GPT, Cursor, and any AI coding tool.

---

## What This Is

When you build with an AI, two problems emerge:
1. **The AI forgets everything between sessions.** You re-explain your project every time.
2. **The codebase gets disorganized.** Without conventions, files end up wherever.

This template solves both. It gives your AI a persistent memory system and a clear MVC-based file structure — from day one.

---

## Quickstart (5 minutes)

```bash
# 1. Clone this repo into your project workspace
git clone https://github.com/heyisforhumans/ai-dev-system-template .agents-template
# Or copy the .agents/ folder directly into your project root

# 2. Copy and fill in your API key
cp .env.template .env
# Edit .env → add your AI_API_KEY

# 3. Open the folder in your AI tool (Antigravity, Cursor, etc.)
# Say anything. The AI will detect it's a fresh install and guide you through setup.
```

That's it. The AI handles the rest.

---

## What's Included

```
.agents/
├── BOOTSTRAP.md              ← AI reads this first every session
├── mvc_framework.md          ← MVC conventions and layer definitions
├── memory/                   ← Per-app session memory + RUNBOOK templates
├── workflows/                ← 6 power workflows (/kickoff, /new-app, /debug, etc.)
└── skills/                   ← 8 skills: 4 universal MVC + 4 example stack skills

docs/                         ← Human-readable guides
scripts/
├── memory_model.py           ← AI-powered component memory generator
└── validate_env.sh           ← Checks env vars before running
```

---

## Workflows

| Workflow | What it does |
|---|---|
| `/kickoff` | ⭐ Orients the AI at session start. First-run: triggers onboarding. |
| `/new-app` | Scaffolds a new app: MVC folder structure + all memory files in one command |
| `/save-memory` | Writes session facts to memory files + git commit |
| `/memory-model-component` | Generates deep component docs via AI API |
| `/debug` | Structured debugging: error → memory check → hypothesis → fix → document |
| `/retrospective` | Post-feature learnings written to memory |

---

## Learning the System

New to MVC or AI memory systems? Start with [`GETTING_STARTED.md`](./GETTING_STARTED.md).

Or dive into:
- [`docs/how-mvc-works.md`](./docs/how-mvc-works.md) — MVC explained with a restaurant analogy
- [`docs/how-memory-works.md`](./docs/how-memory-works.md) — the 3-tier memory system
- [`docs/file-structure.md`](./docs/file-structure.md) — canonical project layout
- [`docs/platform-guide.md`](./docs/platform-guide.md) — notes for Antigravity, Claude, GPT, Cursor

---

## License

MIT — fork it, adapt it, share it.

---

*Built by [heyisforhumans](https://github.com/heyisforhumans). Inspired by Rails conventions, built for the AI-assisted development era.*
