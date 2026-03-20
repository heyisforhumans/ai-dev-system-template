# BOOTSTRAP — AI System Orientation File

> **🤖 INSTRUCTIONS FOR AI AGENTS — READ AND ACT ON THIS IMMEDIATELY:**
>
> 1. Check whether this file contains the string `[UNCONFIGURED]` below.
> 2. **If `[UNCONFIGURED]` is present → DO NOT SUMMARIZE. Run the first-run onboarding flow:**
>    - Say the greeting message defined in `.agents/workflows/kickoff.md`
>    - Walk the user through setup conversationally
>    - Help them fill in this file section by section
> 3. **If `[UNCONFIGURED]` is gone → orient for a normal session per `kickoff.md` Step 2.**
>
> You are not a file explorer. You are an AI with a memory system. Act accordingly.

**Status: [UNCONFIGURED]** ← Remove this line once setup is complete.

---

## How to Use This File

This is the first file your AI reads at the start of every session. It contains:
- Who you are and what you're building
- The apps in this workspace and their current status
- Key infrastructure facts
- The AI memory conventions in use

**Fill this in during your first session.** Your AI will help you.

---

## Workspace Identity

```
Owner:        [ YOUR NAME ]
GitHub:       [ YOUR GITHUB USERNAME ]
AI Tool:      [ Antigravity / Cursor / Claude / GPT ]
Stack:        [ e.g. FastAPI + React + PostgreSQL + Docker ]
Workspace:    [ /path/to/your/workspace ]
```

---

## Apps in This Workspace

| App | Status | URL | Notes |
|---|---|---|---|
| [ App Name ] | [ active / dev / paused ] | [ URL or localhost:PORT ] | [ one-line description ] |

> **Client work lives outside this workspace** — in its own repo and directory (e.g. `~/Desktop/ClientName/`). Never tracked here.

---

## Infrastructure

```
VM / Server:  [ e.g. GCP VM, Heroku, local only ]
Domain:       [ your domain or N/A ]
SSH Key:      [ e.g. ~/.ssh/id_ed25519 ]
Container:    [ Docker / docker-compose / N/A ]
DB:           [ PostgreSQL / SQLite / N/A ]
```

---

## AI Memory System

This workspace uses a 3-tier memory system:

| Tier | Location | What goes here |
|---|---|---|
| 1 — Auto | KI system (Antigravity) or session paste | Broad architectural knowledge |
| 2 — Session | `.agents/memory/[app].md` | Current state, gotchas, decisions |
| 3 — Component | `[app]/memory/[component]_component_memory.md` | Deep per-feature docs |

**Active memory files:**
- [ List your app memory files here after first session ]

---

## Key Conventions

- **MVC file structure** — see `mvc_framework.md` and `docs/file-structure.md`
- **Skills** — load when working in a layer (models, controllers, views, components)
- **Workflows** — `/kickoff` at session start, `/save-memory` at session end
- **Secrets** — always in `.env`, never committed

---

## Open Questions

- [ Add questions here as they come up ]

---

*Remove the `[UNCONFIGURED]` marker at the top once this file is filled in.*
