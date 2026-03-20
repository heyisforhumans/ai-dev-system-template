---
description: Controller layer conventions (Rails-inspired). Covers router structure, CRUD functions, auth guards, and naming.
---

# The Controller Layer — The Manager

> *Rails equivalent: `app/controllers/` + `config/routes.rb`*
> The Controller handles requests, applies business logic, and returns responses. It reads from the Model and decides what the View gets.

---

## Stack

| Rails | Our Stack |
|---|---|
| `ApplicationController` | FastAPI `APIRouter` in `routers/` |
| `before_action` | FastAPI `Depends()` middleware/guards |
| `routes.rb` | Router `prefix` + `include_router` in `main.py` |
| `render json:` | Pydantic `response_model=` |

---

## File Structure

```
backend/app/
├── main.py            ← App entry — mounts all routers
├── auth.py            ← Auth controller — JWT, password, current_user
└── routers/
    ├── users.py       ← One file per resource
    ├── orders.py
    └── [resource].py
```

---

## Naming Conventions

- Router files: **plural snake_case** — `orders.py`, `notifications.py`
- Router functions: **`verb_noun`** — `create_order`, `list_orders`, `get_current_user`
- HTTP verbs: `GET` = read, `POST` = create, `PUT/PATCH` = update, `DELETE` = destroy

---

## Router Template

```python
router = APIRouter(prefix="/orders", tags=["orders"])

@router.get("/", response_model=list[OrderRead])
def list_orders(db: Session = Depends(get_db),
                current_user: User = Depends(get_current_user)):
    return crud.get_orders(db, user_id=current_user.id)

@router.post("/", response_model=OrderRead, status_code=201)
def create_order(order: OrderCreate,
                 db: Session = Depends(get_db),
                 current_user: User = Depends(get_current_user)):
    return crud.create_order(db, order, user_id=current_user.id)
```

---

## Rules

1. **Routers don't touch the DB directly.** All DB access goes through `crud.py` or a service layer.
2. **Auth via `Depends`.** Every protected route uses `current_user: User = Depends(get_current_user)`.
3. **`response_model` always set.** Never return raw dicts — always declare the Pydantic schema.
4. **One router per resource.** `orders.py` handles orders only — no cross-resource logic.
5. **Status codes are explicit.** `201` for create, `204` for delete, `200` for everything else.
