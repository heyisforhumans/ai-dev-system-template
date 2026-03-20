---
description: Save session memory to the relevant per-app and system files, index any new component memories, and commit to git
---

# /save-memory

Run this after any non-trivial task, or manually with `/save-memory`.
Auto-triggered after any task that touched 3+ files or involved a deploy, bug fix, or architecture decision.

---

## Step 1 — Identify What Was Touched

Map each app or system worked on to its Tier 2 memory file in `.agents/memory/`:
- Personal apps → `.agents/memory/[app-name].md`
- Infrastructure / server / Nginx → `.agents/global_context.md`
- AI memory system changes → `.agents/ai-dev-system.md`
- MVC / skill / workflow changes → `.agents/mvc_framework.md`

Update **all** files that were touched.

---

## Step 2 — Append a Session Summary Block

Add to the bottom of each relevant memory file:

```markdown
---

## YYYY-MM-DD — [Short Task Title]
- [durable fact, decision, or gotcha — one line each]
- Architecture decisions made and why
- Ports, paths, env vars, or deploy steps that changed
- Known bugs or constraints discovered
- Current state snapshot if it changed
```

**Only durable technical facts.** No conversational summaries.

---

## Step 3 — Index Any New Component Memories

If `/memory-model-component` was run this session, add it to the **Component Memories** table in `.agents/memory/[app].md`:

```markdown
## Component Memories
| Component | File | Date |
|---|---|---|
| [Feature Name] | `[app]/memory/[feature]_component_memory.md` | YYYY-MM-DD |
```

Create the table if it doesn't exist yet.

---

## Step 4 — Update Snapshot Tables If Anything Changed

If the task changed any of these, update inline (not just the session block):
- **Current State Snapshot** table — port, URL, container name, deploy status
- **Removed / Deprecated** — if anything was deleted or superseded
- **Open Questions** — close answered ones, add new ones

---

## Step 5 — Check Cross-System Files

| File | Update when... |
|---|---|
| `.agents/BOOTSTRAP.md` | Any snapshot changed — URL, port, deploy command, key gotcha |
| `.agents/global_context.md` | Infrastructure changed |
| `.agents/ai-dev-system.md` | Memory conventions or skills/workflows changed |

---

## Step 6 — Flag If RUNBOOK Needs Updating

If architecture changed (new dependency, changed port, new env var, different deploy process):
> ⚠️ **RUNBOOK may need updating**: `[app]/RUNBOOK.md`

Update it now if clear-cut. If it needs thought, add to Open Questions.

---

## Step 7 — Commit to Git

```bash
git add .agents/ && git commit -m "memory: [app-name] — [short description]" && git push
```

If a client app's memory files were also updated, commit them separately in their own repo.

---

## Step 8 — Confirm to User

```
📝 Memory saved:
- .agents/memory/[app].md — [what was added]
[⚠️ RUNBOOK may need updating: app/RUNBOOK.md]
✅ Committed: [short hash]
```

---

## 3-Tier Memory — Decision Guide

| Fact type | Write to |
|---|---|
| Broad architectural knowledge | Tier 1 — your AI tool handles it automatically |
| Session facts, current state, gotchas | `.agents/memory/[app].md` (Tier 2) |
| Deep component docs (10-section) | `[app]/memory/[component]_component_memory.md` (Tier 3) |
| Global infra facts | `.agents/global_context.md` |
| AI system conventions | `.agents/ai-dev-system.md` |

**Rule of thumb**: "What does this system do?" → Tier 2. "How do I extend this specific feature without reading the code?" → Tier 3.
