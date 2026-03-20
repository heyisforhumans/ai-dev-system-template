---
description: Build React/Vite frontends and serve static output from a FastAPI backend. Use this whenever frontend changes need to be deployed.
---

> [!NOTE]
> **Example Stack Skill** — Specific to Vite + FastAPI static file serving. Adapt paths to your project.

# React/Vite Build & Deploy

## Build the Frontend

```bash
cd frontend && npm run build
```

Output goes to `frontend/dist/`.

## Copy to FastAPI Static Directory

```bash
rm -rf backend/app/static && cp -r frontend/dist backend/app/static
```

## Serve Static Files in FastAPI

In `main.py`:
```python
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app.mount("/static", StaticFiles(directory="app/static/assets"), name="static")

@app.get("/{full_path:path}")
async def serve_spa(full_path: str):
    return FileResponse("app/static/index.html")
```

> ⚠️ **Catch-all route must be last** in `main.py` — after all API routers are mounted. Otherwise all API routes return the index.html.

## If Running in Docker

Add to `Dockerfile`:
```dockerfile
COPY backend/ /app/
```

Make sure `frontend/dist` was copied into `backend/app/static` **before** the Docker build.

Or use a multi-stage build:
```dockerfile
FROM node:18 AS frontend-build
WORKDIR /frontend
COPY frontend/ .
RUN npm install && npm run build

FROM python:3.11-slim
COPY backend/ /app/
COPY --from=frontend-build /frontend/dist /app/app/static
```

## Deployment Checklist

- [ ] `npm run build` completed without errors
- [ ] `backend/app/static/` contains `index.html` and `assets/`
- [ ] Catch-all route is last in `main.py`
- [ ] If Docker: rebuild image after copying static files
- [ ] Test in browser — check Network tab for 404s on assets

## Debugging

| Symptom | Cause | Fix |
|---|---|---|
| API routes return HTML | Catch-all route registered before API routers | Move catch-all to bottom of `main.py` |
| Assets 404 | `static` mount path mismatch | Check `directory=` path in `StaticFiles` |
| Old UI showing | Docker not rebuilt | `docker-compose up --build` |
| Vite base path wrong | Deployed to a subpath | Set `base` in `vite.config.ts` |
