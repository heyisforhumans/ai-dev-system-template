---
name: fastapi-auth
description: Boilerplate, patterns, and debugging procedures for authentication in FastAPI applications. Covers JWT tokens, password hashing with bcrypt, OAuth2 password flow, and common auth bugs. Use this whenever a task involves implementing, debugging, or modifying login, session, or token logic in a FastAPI backend.
---

> [!NOTE]
> **Example Stack Skill** — This skill is specific to the FastAPI + bcrypt + JWT stack. Use it as a template to write skills for your own auth implementation.

# FastAPI Auth Skill

## Dependencies

```bash
pip install "python-jose[cryptography]" passlib[bcrypt] python-multipart
```

## Password Hashing

```python
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(plain: str) -> str:
    return pwd_context.hash(plain)

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)
```

> ⚠️ **Common Bug**: Storing a plain string in the DB and calling `verify_password()` against it will always return `False`. Always hash on write, never on read.

## JWT Token Creation & Verification

```python
from jose import JWTError, jwt
from datetime import datetime, timedelta

SECRET_KEY = os.getenv("SECRET_KEY")  # Never hardcode
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24  # 24 hours

def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_token(token: str) -> dict:
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        return None
```

## Login Endpoint (OAuth2 Password Flow)

```python
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

@router.post("/auth/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = get_user_by_username(form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": user.username, "role": user.role})
    return {"access_token": token, "token_type": "bearer"}
```

> ⚠️ **Frontend Payload**: `OAuth2PasswordRequestForm` expects `application/x-www-form-urlencoded`, NOT JSON.
> ```js
> const formData = new URLSearchParams();
> formData.append("username", username);
> formData.append("password", password);
> fetch("/auth/login", { method: "POST", body: formData });
> ```
> Sending JSON causes a 422 error.

## Protected Route

```python
async def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = decode_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    user = get_user_by_username(payload.get("sub"))
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    return user
```

## Debugging Checklist

| Symptom | Likely cause | Fix |
|---|---|---|
| "Invalid credentials" always | Password not hashed in DB | Hash with `hash_password()` and re-store |
| 422 on login | Frontend sending JSON not form data | Switch to `URLSearchParams` |
| Token always invalid | Wrong SECRET_KEY | Ensure same key at encode and decode |
| 401 on valid token | Token expired | Extend `ACCESS_TOKEN_EXPIRE_MINUTES` |
| CORS error on login | Missing origin in CORSMiddleware | Add frontend origin to `allow_origins` |
