---
description: Model layer conventions (Rails-inspired). Covers naming, file structure, SQLAlchemy patterns, and Pydantic schemas.
---

# The Model Layer — The Librarian

> *Rails equivalent: `app/models/` + `db/`*
> The Model defines what data exists, its shape, and its rules. Nothing else decides these things.

---

## Stack

| Rails | Our Stack |
|---|---|
| `ActiveRecord` models | `SQLAlchemy` ORM models |
| Schema migrations | `Alembic` migrations |
| Serializers | `Pydantic` schemas in `schemas.py` |

---

## File Structure

```
backend/app/
├── models/            ← SQLAlchemy model classes (one file per domain)
├── schemas.py         ← All Pydantic request/response schemas
├── db.py              ← Engine, SessionLocal, Base
└── alembic/versions/  ← Migration files
```

---

## Naming Conventions

- Model classes: **singular PascalCase** — `User`, `Order`, `HarvestRecord`
- Table names: **plural snake_case** — `users`, `orders`, `harvest_records`
- Schema classes: **`[Model]Create`**, **`[Model]Read`**, **`[Model]Update`**
- Foreign keys: **`[table_singular]_id`** — e.g. `user_id`, `order_id`

---

## SQLAlchemy Model Template

```python
class HarvestRecord(Base):
    __tablename__ = "harvest_records"

    id         = Column(Integer, primary_key=True, index=True)
    user_id    = Column(Integer, ForeignKey("users.id"), nullable=False)
    quantity   = Column(Float, nullable=False)
    unit       = Column(String, default="lbs")
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="harvest_records")
```

## Pydantic Schema Template

```python
class HarvestRecordCreate(BaseModel):
    quantity: float
    unit:     str = "lbs"

class HarvestRecordRead(HarvestRecordCreate):
    id:         int
    user_id:    int
    created_at: datetime
    class Config:
        from_attributes = True
```

---

## Rules

1. **Models own the truth.** Never define data shape in a router — always reference the model.
2. **Schemas are not models.** `schemas.py` is the API surface; `models/` is the DB shape.
3. **All timestamps in UTC.** Use `default=datetime.utcnow`, never `datetime.now()`.
4. **Relationships declared on both sides.** If `User` has `harvest_records`, `HarvestRecord` has `user`.
