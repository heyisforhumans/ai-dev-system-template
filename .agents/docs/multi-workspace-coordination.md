# Multi-Workspace Coordination

How to use multiple AI workspaces together without collisions or duplicated work.

---

## The Pattern

```
Orchestrator Workspace (GCP / ops)
├── Reads plans from all projects
├── Audits implementation plans via /peer-review
├── Owns infrastructure decisions (VMs, Nginx, Docker, SSL)
├── Writes to GCP/Artifacts/<project>/ as the handoff channel
└── Does NOT write code in other project folders

Worker Workspace (your project)
├── Executes within its own folder
├── Writes plans to GCP/Artifacts/<project>/ before building
├── Reads GCP handoff before starting any non-trivial task
└── Does NOT make infra/VM changes
```

---

## When to Use Each Agent

| Task type | Use this workspace |
|---|---|
| Bug fix, single-file edit | Project workspace |
| New page, component, route | Project workspace |
| DB schema change | Project workspace, then flag for orchestrator review |
| Infra change (Nginx, Docker, SSL) | Orchestrator workspace only |
| Implementation plan review | Orchestrator workspace via /peer-review |

---

## Handoff Protocol

1. **Project agent** writes `_plan.md` to `GCP/Artifacts/<project>/`
2. **Orchestrator agent** runs `/peer-review` — writes `_handoff.md` to same folder
3. **Project agent** reads `_handoff.md` before building — resolves blockers first
4. After build, **project agent** updates its memory file

---

## Credit Budget Awareness

- One agent active at a time unless truly parallel
- Orchestrator session = strategy only. Don't burn credits on file edits.
- Project sessions = execution only. Escalate architecture questions to orchestrator.
- Use warm kickoff when resuming — don't re-read memory that's already loaded.
