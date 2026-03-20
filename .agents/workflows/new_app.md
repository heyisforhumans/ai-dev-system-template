---
description: Scaffold a new app with the MVC directory structure and all memory files in one command
---

# /new-app

Run this when starting a new application. Creates the full MVC folder skeleton, memory files, RUNBOOK, and registers the app in BOOTSTRAP — all in one pass.

---

## Step 1 — Get App Info

Ask the user (or infer from context):
- **App name** — e.g. "farm-inventory-pro"
- **Stack** — e.g. "FastAPI + React + PostgreSQL" (default to workspace stack from BOOTSTRAP)
- **Where it lives** — e.g. `apps/[app-name]/` for personal apps, or a separate Desktop folder for client work
- **Is this client work?** — if yes, it gets its own repo (never tracked in the main workspace)

---

## Step 2 — Create MVC Directory Skeleton

```bash
mkdir -p [app-path]/{backend/app/{models,routers},frontend/src/{pages,components,contexts},fixtures,memory,docs,deploy,alembic/versions}
touch [app-path]/RUNBOOK.md
touch [app-path]/docs/SPEC.md
touch [app-path]/docs/NOTES.md
touch [app-path]/.env
touch [app-path]/.env.example
touch [app-path]/docker-compose.yml
touch [app-path]/Makefile
```

Explain to the user what each folder is for as you create it.

---

## Step 3 — Create Memory Files

Copy `_app_template.md` → `.agents/memory/[app-name].md`:
- Fill in the app name, stack, and path
- Add today's date as the initial session entry

Copy `_RUNBOOK_template.md` → `[app-path]/RUNBOOK.md`:
- Fill in the app name, stack, and port

---

## Step 4 — Register in BOOTSTRAP

Add the app to the Apps table in `.agents/BOOTSTRAP.md`:
```markdown
| [App Name] | dev | localhost:[PORT] | [one-line description] |
```

Add to the "Active memory files" list:
```markdown
- `.agents/memory/[app-name].md`
```

---

## Step 5 — Update ai-dev-system.md

Add the new app to the workspace app inventory in `.agents/ai-dev-system.md`.

---

## Step 6 — Confirm and Commit

Show the user what was created:
```
✅ Created [app-name]:
   [app-path]/
   ├── backend/app/{models,routers}/
   ├── frontend/src/{pages,components,contexts}/
   ├── fixtures/, memory/, docs/, deploy/
   └── RUNBOOK.md

Memory files:
   .agents/memory/[app-name].md
   BOOTSTRAP.md updated
```

Then suggest a git commit:
```bash
git add .agents/ [app-path]/ && git commit -m "feat: scaffold [app-name] with MVC structure"
```
