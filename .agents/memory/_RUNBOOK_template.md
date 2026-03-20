# [App Name] — RUNBOOK

> Operational guide for running, deploying, and debugging this app.
> Keep this updated when anything changes.

---

## Quick Reference

| What | Value |
|---|---|
| App | [App Name] |
| Port | [PORT] |
| Local URL | `http://localhost:[PORT]` |
| Deployed URL | [URL or N/A] |
| Container name | `[app-name]-api` |
| DB container | `[app-name]-db` |
| Start command | `docker-compose up -d` |

---

## Local Development

```bash
# Start the database
docker-compose up -d db

# Install backend dependencies
cd backend && pip install -r requirements.txt

# Run migrations
alembic upgrade head

# Start backend
uvicorn app.main:app --reload --port [PORT]

# Start frontend (separate terminal)
cd frontend && npm install && npm run dev
```

---

## Production Deployment

```bash
# Build and start all containers
docker-compose up --build -d

# Check status
docker ps | grep [app-name]

# Tail logs
docker-compose logs -f api
```

---

## Database

```bash
# Run migrations
alembic upgrade head

# Create a new migration
alembic revision --autogenerate -m "describe the change"

# Connect to DB directly
docker exec -it [app-name]-db psql -U [DB_USER] -d [DB_NAME]
```

---

## Environment Variables

Copy `.env.example` → `.env` and fill in:

| Variable | Description |
|---|---|
| `DATABASE_URL` | PostgreSQL connection string |
| `SECRET_KEY` | JWT signing key (generate with `openssl rand -hex 32`) |
| `[OTHER_VARS]` | [Description] |

---

## Common Problems

| Symptom | Likely cause | Fix |
|---|---|---|
| Container won't start | .env missing or wrong vars | Check `docker-compose logs [service]` |
| DB connection refused | DB not ready | Wait 5s and retry, or add retry logic |
| Old UI showing | Docker cache stale | `docker-compose up --build -d` |
| Auth always fails | SECRET_KEY mismatch | Verify same key in .env and running container |

---

## Monitoring

```bash
# Container health
docker ps

# App logs
docker-compose logs -f api

# DB logs
docker-compose logs -f db
```

---

*Last updated: YYYY-MM-DD*
