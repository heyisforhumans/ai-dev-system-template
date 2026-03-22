# How MVC Works

> Read this during onboarding. After this, you'll know exactly where every file goes.

---

## The Restaurant Analogy

Think of your app as a restaurant:

- **Model = Recipe Cards** — the rules about data. What an "invoice" looks like, what fields it has, what's required. The recipe doesn't care who ordered it or how it's plated. It's just the truth about the thing.
- **Controller = Kitchen Manager** — what happens when a request comes in. "GET /invoices" → fetch all invoices → return them. Business logic lives here. The kitchen manager reads recipe cards and coordinates the kitchen but never talks to customers directly.
- **View = The Menu** — what the user sees and interacts with. Pages, components, forms. The menu describes the food; it doesn't cook it.

**The rule:** Every file we create lives in exactly one of these three layers. The AI always knows where to put things because the layers are non-negotiable.

---

## One Real Example

Let's say we're building a "create invoice" feature:

| Layer | File | Job |
|---|---|---|
| **Model** | `backend/app/models/invoice.py` | Defines `Invoice` table — fields, types, relationships |
| **Controller** | `backend/app/routers/invoices.py` | `POST /invoices` — validates input, creates DB row, returns result |
| **View** | `frontend/src/pages/NewInvoicePage.tsx` | The form the user fills out. Calls the controller. Shows feedback. |
| **Component** | `frontend/src/components/LineItemRow.tsx` | Reusable row inside the form — not a page itself |

Notice: `NewInvoicePage.tsx` never touches the database. `invoice.py` never knows the user exists. Each layer has one job.

---

## The Layer Tests

Not sure where a file goes? Ask:

- "Does this define what data looks like?" → **Model**
- "Does this handle a request or contain business logic?" → **Controller**
- "Does this render something the user sees?" → **View** or **Component**
- "Is it a full page (has a route)?" → **View/Page**
- "Is it a reusable piece inside a page?" → **Component**

---

## What Breaks When You Mix Layers

| Anti-pattern | Problem |
|---|---|
| Fetch call inside a component | Component is now doing Controller work — hard to test, hard to reuse |
| Business logic in a route handler that's 200 lines | Controller is doing Model work — impossible to unit test |
| Database query directly on the frontend | Skipped two layers — security nightmare |

---

## The Short Version

> Model = shape of data.
> Controller = what happens.
> View = what the user sees.
> One file, one job, one layer.
