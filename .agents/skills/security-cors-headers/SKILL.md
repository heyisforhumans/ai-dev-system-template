---
name: security-cors-headers
description: Patterns and checklists for CORS policies and security headers in FastAPI backends. Use this whenever adding CORS support, hardening security headers, or debugging CORS errors.
---

> [!NOTE]
> **Example Stack Skill** — Specific to FastAPI + Nginx. Adapt origin URLs to your domain.

# Security Headers & CORS

## FastAPI CORS Setup

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://yourdomain.com"],  # replace with your domain
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["Authorization", "Content-Type"],
)
```

> ⚠️ **Never use `allow_origins=["*"]`** in production — it bypasses CORS entirely.

## Security Headers Middleware

```python
from starlette.middleware.base import BaseHTTPMiddleware

class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
        response.headers["X-XSS-Protection"] = "1; mode=block"
        response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
        return response

app.add_middleware(SecurityHeadersMiddleware)
```

## Hide API Docs in Production

```python
app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)
```

## Pre-Deploy Checklist

- [ ] `CORSMiddleware` uses specific domain (not `*`)
- [ ] `/docs`, `/redoc`, `/openapi.json` disabled or Nginx-blocked
- [ ] Security headers present in responses
- [ ] All sensitive endpoints require authentication
- [ ] No secrets logged or returned in error responses

## Common CORS Errors

| Browser Error | Cause | Fix |
|---|---|---|
| `No 'Access-Control-Allow-Origin'` | CORS middleware missing or wrong origin | Fix `CORSMiddleware` |
| Credentials flag error | `allow_credentials=True` with `allow_origins=["*"]` | Use a specific origin |
| Preflight OPTIONS returns 404 | Backend not handling OPTIONS | `CORSMiddleware` handles this automatically |
