---
description: MVC filesystem lint — catch layer violations, oversized files, and inline anti-patterns before they become debt
---

# /audit

Run this when starting a new app, after a large feature push, or when code hygiene feels off.
Catches structural drift early. Takes 5–10 minutes on a typical project.

---

## Step 1 — Pages / Views Layer

Scan `frontend/src/pages/`:

**Checks:**
- [ ] Every `.tsx` in `pages/` is imported by a `<Route>` in `App.tsx` or the router file
- [ ] No page file is >300 lines — if it is, flag for component extraction
- [ ] No page contains inline `fetch()` calls — data fetching belongs in a hook or controller layer
- [ ] No page imports another page directly (pages only import components)

---

## Step 2 — Components Layer

Scan `frontend/src/components/`:

**Checks:**
- [ ] No component contains API calls — components receive data as props
- [ ] No component manages app-wide state (should use Context or be lifted to a page)
- [ ] No component is >200 lines without a clear reason
- [ ] Generic components have no app-specific logic baked in

---

## Step 3 — Controllers / API Layer

Scan `backend/app/routers/`:

**Checks:**
- [ ] No router contains business logic beyond request parsing + DB call + response format
- [ ] No router file is >200 lines
- [ ] No hardcoded credentials, tokens, or IDs in any router
- [ ] Every route has an auth guard or is explicitly marked public

---

## Step 4 — Models Layer

Scan `backend/app/models/`:

**Checks:**
- [ ] No model imports from `routers/` (no circular dependency upward)
- [ ] Every table has a primary key
- [ ] No raw SQL strings in model files

---

## Step 5 — API Client (Frontend)

**Checks:**
- [ ] No `fetch()` or API calls exist outside `api/` 
- [ ] Base URL comes from an env variable, not hardcoded
- [ ] Auth token injection is in one place only

---

## Step 6 — Secrets and Config

**Checks:**
- [ ] `.env` is in `.gitignore`
- [ ] No API keys or tokens in any source file
- [ ] No `console.log` of auth tokens or user PII

---

## Step 7 — Report

Write a short summary to `.agents/memory/[app].md` under a new dated entry:

```
## YYYY-MM-DD — /audit run
- Clean: [layers with no issues]
- Flagged: [specific files + violations]
- Actions taken: [what was fixed now vs. added to backlog]
```

---

## Anti-Patterns Reference

| Anti-pattern | Where it usually hides | Fix |
|---|---|---|
| Inline `fetch()` in page | `pages/InventoryPage.tsx` | Move to `useInventory()` hook |
| API call in component | `components/DataTable.tsx` | Pass data as prop from parent |
| Business logic in router | `routers/orders.py` | Extract to `services/order_service.py` |
| Model importing router | `models/user.py` | Invert dep — router imports model, never reverse |
| Hardcoded base URL | `api/client.ts` | `import.meta.env.VITE_API_URL` |
