# MVC File Structure Guide

> Every project starts clean. Every file has a home. Nobody asks "where does this go?"

---

## The Workspace (Top Level)

```
[workspace-root]/
├── README.md                ← Entry point for humans and AI
├── apps/                    ← All personal/internal apps
│   └── [app-name]/          ← Each app lives here
├── scripts/                 ← Dev utilities (memory_model.py, etc.)
├── experiments/             ← Throwaway code, prototypes, spike work
├── infra/                   ← Nginx configs, server assets
├── .agents/                 ← AI brain (BOOTSTRAP, memory, skills, workflows)
├── .env                     ← Secrets — NEVER committed to git
└── .gitignore
```

**Client work:** Always in its own separate directory and git repo (e.g., `~/Desktop/ClientName/`). **Never** tracked inside the workspace repo. This is a hard rule — it keeps client code portable and transferable.

---

## One App (MVC Layout)

```
[app-name]/
│
├── backend/                 ← Server-side code
│   └── app/
│       ├── models/          ← MODEL — data shapes and DB tables
│       │   ├── users.py
│       │   ├── orders.py
│       │   └── __init__.py
│       ├── routers/         ← CONTROLLER — API endpoints
│       │   ├── users.py
│       │   ├── orders.py
│       │   └── __init__.py
│       ├── schemas.py       ← VIEW contract — Pydantic (what API exposes)
│       ├── auth.py          ← Auth logic
│       ├── db.py            ← DB connection
│       ├── main.py          ← App entry point, mounts all routers
│       └── seed.py          ← Dev/test seed data
│
├── frontend/                ← Client-side code
│   └── src/
│       ├── pages/           ← VIEW — full-page React components
│       │   ├── LoginPage.tsx
│       │   ├── DashboardPage.tsx
│       │   └── [Resource]Page.tsx
│       ├── components/      ← COMPONENT — reusable UI pieces
│       │   ├── DataTable.tsx
│       │   └── ConfirmModal.tsx
│       ├── contexts/        ← Shared React state (auth, notifications)
│       │   └── AuthContext.tsx
│       ├── api/             ← Typed API client
│       │   └── client.ts
│       └── index.css        ← Global design system (tokens, typography)
│
├── alembic/                 ← DB migrations
│   └── versions/
│
├── fixtures/                ← Test data files (excluded from Docker)
├── memory/                  ← AI component docs (excluded from Docker)
├── docs/                    ← Human documentation
│   ├── SPEC.md              ← Feature specification
│   └── NOTES.md             ← Dev notes and gotchas
├── deploy/                  ← Nginx configs, deployment assets
│
├── docker-compose.yml
├── Makefile                 ← Common commands (make deploy, make seed, etc.)
├── RUNBOOK.md               ← Operational guide (how to deploy, restart, debug)
├── .env                     ← Secrets (gitignored)
└── .env.example             ← Template for required env vars
```

---

## The One-Line Rule Per Folder

| Folder | One-line rule |
|---|---|
| `backend/app/models/` | **Data shapes.** Everything about what exists and its rules. |
| `backend/app/routers/` | **Request handling.** What happens when an endpoint is called. |
| `frontend/src/pages/` | **Full screens.** One file per route. Fetches its own data. |
| `frontend/src/components/` | **Reusable UI.** Used in 2+ pages, or complex enough to isolate. |
| `frontend/src/contexts/` | **Shared state.** Auth, notifications, anything truly app-wide. |
| `fixtures/` | **Test data only.** Never deployed. Gitignored from Docker. |
| `memory/` | **AI-generated docs.** Never deployed. Gitignored from Docker. |
| `docs/` | **Human documentation.** SPEC, NOTES, decisions. |
| `deploy/` | **Deployment assets.** Nginx configs, CI scripts. |

---

## What Goes in `.dockerignore`

Always exclude these from Docker builds:

```dockerignore
fixtures/
memory/
docs/
.env
.env.*
node_modules/
__pycache__/
.git/
.gitignore
```

These are development-only assets. Production containers should only contain runnable code.

---

## The Client Work Rule

> Client projects are never tracked inside your workspace repo.

**Why:** Client code may need to be transferred, shared, or audited separately. Mixing it into your personal workspace creates legal and practical complications.

**Convention:**
```
~/Desktop/
├── [workspace-root]/    ← Your workspace repo
└── [ClientName]/        ← Client project — its own git repo
    └── [app-name]/
```

Document this boundary in `.agents/global_context.md`.
