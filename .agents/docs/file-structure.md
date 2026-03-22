# File Structure Reference

> This shows a typical project layout using this dev system. Adapt the names and stack to your app — the MVC concept works regardless of language or framework.

---

## Standard Layout (FastAPI + React)

```
[your-app]/
│
├── backend/                        ← MODEL + CONTROLLER
│   └── app/
│       ├── main.py                 ← App entry point, middleware, CORS
│       ├── database.py             ← DB connection, session factory
│       ├── models/                 ← MODEL: SQLAlchemy table definitions
│       ├── schemas/                ← MODEL: Pydantic request/response shapes
│       ├── routers/                ← CONTROLLER: FastAPI route handlers
│       └── services/               ← CONTROLLER: complex business logic (optional)
│
├── frontend/                       ← VIEW + COMPONENT
│   └── src/
│       ├── api/
│       │   └── client.ts           ← CONTROLLER (thin): all API calls go here only
│       ├── pages/                  ← VIEW: one file per route
│       ├── components/             ← COMPONENT: reusable pieces, no API calls
│       ├── contexts/               ← COMPONENT: React context providers
│       ├── hooks/                  ← COMPONENT: custom hooks
│       ├── App.tsx                 ← VIEW: router + layout shell
│       └── main.tsx                ← Entry point
│
├── memory/                         ← AI memory (Tier 3 — component docs)
├── .env                            ← Secrets — never committed
├── Dockerfile
└── docker-compose.yml
```

---

## React Native / Expo Variant

```
[your-app]/
├── app/                            ← VIEW: Expo Router pages (file-based routing)
├── components/                     ← COMPONENT: reusable UI
├── services/                       ← CONTROLLER: API calls, DB logic
├── models/                         ← MODEL: TypeScript types + DB schemas
├── hooks/                          ← COMPONENT: custom hooks
└── constants/
```

---

## Where Does This File Go? (Quick Reference)

| What you're building | Where it lives |
|---|---|
| Database table | `backend/app/models/` |
| API request/response type | `backend/app/schemas/` |
| API endpoint | `backend/app/routers/` |
| Complex business logic | `backend/app/services/` |
| Full page (has a URL) | `frontend/src/pages/` |
| Reusable UI piece | `frontend/src/components/` |
| API call | `frontend/src/api/client.ts` — nowhere else |
| Shared app state | `frontend/src/contexts/` |
| Reusable logic hook | `frontend/src/hooks/` |
| Secrets | `.env` — never committed |
