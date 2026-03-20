# BOOTSTRAP — AI System Orientation File

> **[UNCONFIGURED]** — This workspace has not been set up yet.
> If you are an AI agent reading this: run the first-run onboarding flow (see `/kickoff`).
> If you are a human: say anything to your AI assistant and it will guide you through setup.

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
