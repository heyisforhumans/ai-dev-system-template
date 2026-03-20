---
description: Patterns and anti-patterns for Docker Compose services. Use whenever working with docker-compose.yml or debugging container issues.
---

> [!NOTE]
> **Example Stack Skill** — Specific to Docker Compose orchestration. Adapt port numbers and service names to your project.

# Docker Compose Patterns

## Standard Service Template

```yaml
version: "3.9"

services:
  api:
    build: .
    container_name: my-app-api
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=${DATABASE_URL}
      - SECRET_KEY=${SECRET_KEY}
    volumes:
      - ./backend:/app          # dev only — remove in production
    depends_on:
      - db
    restart: unless-stopped

  db:
    image: postgres:15
    container_name: my-app-db
    environment:
      - POSTGRES_USER=${DB_USER}
      - POSTGRES_PASSWORD=${DB_PASSWORD}
      - POSTGRES_DB=${DB_NAME}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    restart: unless-stopped

volumes:
  postgres_data:
```

## Port Ownership

Assign and document ports in `BOOTSTRAP.md` and `RUNBOOK.md`:

```
8000 — API (FastAPI)
5432 — PostgreSQL (internal only, not exposed)
3000 — Frontend dev server (not in docker-compose, local only)
```

> ⚠️ **Port conflicts** are the most common Docker headache. Always check `docker ps` before starting a new service.

## Common Commands

```bash
# Start all services
docker-compose up -d

# Rebuild and restart
docker-compose up --build -d

# Tail logs
docker-compose logs -f api

# Stop all
docker-compose down

# Stop and remove volumes (DESTROYS DB DATA)
docker-compose down -v
```

## Anti-Patterns

- ❌ Don't mount source volumes in production — build the image instead
- ❌ Don't hardcode secrets in `docker-compose.yml` — use env vars from `.env`
- ❌ Don't expose the DB port (5432) to the host in production
- ❌ Don't use `restart: always` — use `restart: unless-stopped` (allows manual stop)

## Debugging Checklist

| Symptom | Cause | Fix |
|---|---|---|
| Port already in use | Another container using same port | Check `docker ps`, stop the conflict |
| Container exits immediately | App crash at startup | `docker-compose logs api` to see error |
| DB connection refused | DB not ready when API starts | Add `depends_on` + retry logic in app |
| Changes not reflected | Old image cached | `docker-compose up --build -d` |
