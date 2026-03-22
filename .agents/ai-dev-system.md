# AI Dev System — System State

> This file is maintained by the AI agent. Update it when the memory system, skills, or workflows change.

---

## Memory System

**3-Tier Architecture:**
- Tier 1: Auto-loaded by AI tool (KI system on Antigravity, or paste BOOTSTRAP at session start)
- Tier 2: `.agents/memory/[app].md` — session context, updated via `/save-memory`
- Tier 3: `[app]/memory/[feature]_component_memory.md` — deep docs, generated via `/memory-model-component`

---

## Active Memory Files

*Add entries here as you create app memory files:*

- None yet — run `/new-app` to scaffold your first app

---

## Skills

**Universal MVC Skills (load based on layer being worked on):**
| Skill | Layer | Load when... |
|---|---|---|
| `mvc-models` | Model | Working on database tables, schemas |
| `mvc-controllers` | Controller | Working on API endpoints, business logic |
| `mvc-views` | View | Working on frontend pages |
| `mvc-components` | Component | Working on reusable UI components |

**Example Stack Skills (adapt or replace for your stack):**
| Skill | Domain | Load when... |
|---|---|---|
| `fastapi-auth` | Auth | Implementing/debugging JWT auth |
| `react-vite-build` | Deploy | Building/deploying frontend |
| `docker-compose-patterns` | Infra | Working with containers |
| `security-cors-headers` | Security | Adding CORS or security headers |

---

## Workflows

| Workflow | Command | Purpose |
|---|---|---|
| `kickoff` | `/kickoff` | Session start + first-run detection + memory freshness check |
| `new_app` | `/new-app` | Scaffold a new app's MVC structure |
| `save_memory` | `/save-memory` | Write session facts to memory files |
| `memory_model_component` | `/memory-model-component` | Generate deep component docs |
| `debug` | `/debug` | Structured debugging — logs-first, hypothesis-driven |
| `retrospective` | `/retrospective` | Post-feature lessons → memory |
| `audit` | `/audit` | MVC filesystem lint — catch layer violations + oversized files |

---

## Docs

| Doc | Purpose |
|---|---|
| `docs/how-mvc-works.md` | Restaurant analogy explainer — for onboarding |
| `docs/file-structure.md` | Annotated folder tree for new apps |
| `docs/multi-workspace-coordination.md` | Orchestrator + worker pattern for multi-agent setups |
| `docs/peer_review_placeholder.md` | How to connect a GCP orchestrator for plan review |

---

## MVC Framework

See `docs/how-mvc-works.md` and `docs/file-structure.md` for full conventions.

---

## Open Questions

- [ ] Add questions here as they come up
