---
description: Component conventions for React stack. Covers what makes something a component vs a page, props patterns, and when to write a component_memory.md.
---

# The Component Layer — The Engineer

> *Rails equivalent: partials (`_form.html.erb`, `_nav.html.erb`)*
> A component is a self-contained, reusable piece of UI. If a view element appears in more than one place, or is complex enough to have its own state and behavior, it's a component.

---

## Component vs Page — The Rule

| It's a **Page** if... | It's a **Component** if... |
|---|---|
| It maps to a route (`/orders`, `/dashboard`) | It appears on more than one page |
| It is the top-level owner of a resource | It has its own props interface |
| It fetches its own data on mount | It receives data via props |

---

## File Structure

```
frontend/src/
├── components/
│   ├── NotificationBell.tsx   ← Feature component (reused across pages)
│   ├── DataTable.tsx          ← Generic presentational component
│   └── ConfirmModal.tsx       ← Shared modal component
└── pages/
    └── OrdersPage.tsx         ← Page that *uses* these components
```

---

## Naming Conventions

- **PascalCase descriptive noun** — `NotificationBell`, `DataTable`, `ConfirmModal`
- Props interface: **`[Component]Props`** — `NotificationBellProps`, `DataTableProps`
- Event handlers: **`on[Action]`** — `onClose`, `onChange`, `onSubmit`

---

## Component Template

```tsx
interface DataTableProps {
  rows: Row[];
  onRowClick: (row: Row) => void;
}

export default function DataTable({ rows, onRowClick }: DataTableProps) {
  return (
    <div className="data-table">
      {/* implementation */}
    </div>
  );
}
```

---

## When to Write a `_component_memory.md`

Write one when:
- The component took significant iteration to get right
- It has non-obvious state management or edge cases
- Another agent would need it to recreate the component accurately

Store it in:
```
[app]/memory/[component_name]_component_memory.md
```

`memory/` is for AI-generated artifacts only — human docs go in `docs/`. Both are excluded from Docker builds via `.dockerignore`.

Use the `/memory-model-component` workflow after completing a significant component.

---

## Rules

1. **Components receive data, pages fetch it.** A component should never call the API directly.
2. **One responsibility per component.** `NotificationBell` shows the count — it doesn't render the full notification list.
3. **Props over global state.** Prefer props over reaching into global context, unless state is truly app-wide (auth, theme).
4. **Co-locate tests.** `DataTable.test.tsx` lives next to `DataTable.tsx`.
