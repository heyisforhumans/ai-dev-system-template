---
description: View layer conventions (Rails-inspired). Covers pages, modals, sidebars, persistent layout elements, and CSS conventions.
---

# The View Layer — The Presenter

> *Rails equivalent: `app/views/` + layouts + partials*
> The View is what the user reads, sees, and interacts with. It receives data from the Controller and presents it — it contains no business logic.

---

## Stack

| Rails | Our Stack |
|---|---|
| `.erb` page templates | React page components in `pages/` |
| `layouts/application.html.erb` | Persistent layout elements (Sidebar, Navbar) |
| Partials (`_form.html.erb`) | Reusable components in `components/` |
| Modals / dialogs | Modal components scoped to their page |

---

## File Structure

```
frontend/src/
├── pages/             ← Full-page views (one per route)
│   ├── DashboardPage.tsx
│   ├── OrdersPage.tsx
│   └── LoginPage.tsx
├── components/        ← Reusable sub-views (see mvc-components skill)
├── layouts/           ← Persistent layout elements
│   ├── Sidebar.tsx
│   └── Navbar.tsx
└── index.css          ← Global design system (tokens, typography, base styles)
```

---

## Naming Conventions

- Pages: **`[Resource]Page`** — `DashboardPage`, `OrdersPage`, `AdminPage`, `LoginPage`
- Modals: **`[Action]Modal`** — scoped to the page that owns them
- Layout elements: **descriptive noun** — `Sidebar`, `Navbar`, `NotificationBell`
- CSS classes: **kebab-case** — `.order-table`, `.sidebar-nav-item`, `.modal-overlay`

---

## What Belongs in a View

✅ Display logic — formatting dates, truncating strings, conditional rendering
✅ User interaction — form inputs, button clicks, navigation
✅ Local UI state — open/closed modal, active tab, hover state
❌ Business logic — calculations, data transformations
❌ Direct API calls — use a typed `api.ts` fetch wrapper, not raw `fetch()` inline

---

## Page Template

```tsx
export default function OrdersPage() {
  const [orders, setOrders] = useState<Order[]>([]);

  useEffect(() => {
    api.getOrders().then(setOrders);
  }, []);

  return (
    <div className="page-container">
      <h1 className="page-title">Orders</h1>
      {/* content */}
    </div>
  );
}
```

---

## CSS / Design System Rules

1. **`index.css` owns the tokens.** Colors, spacing, typography — define once, reference everywhere.
2. **No inline styles on layout.** Use class names. Inline styles are for dynamic values only.
3. **Persistent elements (Sidebar, Navbar) live in `layouts/`**, not inside any page.
4. **Modals are owned by their page** until needed in 2+ places — then they move to `components/`.
