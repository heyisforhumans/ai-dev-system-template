# How MVC Works — A Plain English Guide

> No coding experience required. This guide uses a restaurant analogy to explain MVC from the ground up.

---

## The Problem MVC Solves

Imagine you're a restaurant owner. You have recipes, a kitchen manager, and menus for customers. If all of these are mixed together — recipes inside the menu, kitchen manager writing on napkins — things get chaotic fast.

MVC is simply a convention for keeping these three things separate. Each layer has one job, and they don't do each other's jobs.

---

## The Three Layers

### 🗂️ Model — The Recipe Cards
**What it is:** The data. The rules about data. The database.

**Restaurant analogy:** The kitchen's recipe cards. Each card defines what an ingredient is, what goes into a dish, and the rules (e.g., "must be fresh, never frozen"). The recipe cards don't talk to customers. They just define what exists.

**In your code:**
- Database tables (users, orders, products)
- The shape of data (an Order has a total, a date, a status)
- Relationships (an Order belongs to a User)

**Where it lives:** `backend/app/models/`

---

### 🎛️ Controller — The Kitchen Manager
**What it is:** The logic. The rules about what happens when.

**Restaurant analogy:** The kitchen manager takes orders from the waiter (requests), reads the recipe cards (Model), decides what to cook and in what order, and tells the kitchen what to do. The manager doesn't write the recipe cards, and they don't design the menu.

**In your code:**
- API endpoints (`GET /orders`, `POST /orders`)
- Business logic ("can this user see this order?")
- Orchestrating data in and out

**Where it lives:** `backend/app/routers/`

---

### 🪟 View — The Menu
**What it is:** What the customer sees. The user interface.

**Restaurant analogy:** The menu is what the customer reads and interacts with. It shows information in a readable format. It doesn't know how the kitchen works, and it doesn't decide what's in the recipes.

**In your code:**
- React pages and components
- What the user sees in the browser
- Forms, buttons, tables, modals

**Where it lives:** `frontend/src/pages/` and `frontend/src/components/`

---

## How They Work Together

```
User clicks "Place Order" →

View (React)         → sends request to →
Controller (FastAPI)  → reads/writes →
Model (SQLAlchemy)    → talks to →
Database (PostgreSQL)

                    ↓
                    
Database             → data returned to →
Model                → shaped by →
Controller           → formatted for →
View                 → displayed to →
User
```

---

## Why This Matters for AI

When your AI knows which layer it's working in, it:
- Knows exactly which files to create and where
- Knows what belongs in a file and what doesn't
- Never puts database logic in the UI or UI logic in the database

That's why the skills are organized by layer. Before starting a task, the AI loads the relevant layer's skill and follows its conventions automatically.

---

## The One Rule to Remember

**Each layer has one job. Don't mix them.**

- Views don't fetch data from the database
- Controllers don't format HTML or CSS
- Models don't handle user clicks

When everything follows this rule, any developer (or AI) can open a file and immediately know what it does and what it should contain.
