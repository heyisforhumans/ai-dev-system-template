# Peer Review — What It Is and When to Use It

> This doc explains the cross-agent plan review system. It's an advanced pattern for when you have multiple AI workspaces.

---

## The Problem It Solves

When you write an implementation plan, your AI can't see what it doesn't know. A second agent reading the same plan against the live source catches:
- "Already done" claims that are wrong
- Missing pieces the first agent assumed were handled
- Conflicting state between what the plan describes and what the code actually does

---

## How It Works

1. **Project workspace** — where you build the app — writes `_plan.md` to the shared drop zone
2. **Orchestrator workspace** reads it against live source, writes back `_handoff.md`
3. Project agent reads handoff before building

### The Drop Zone

```
GCP/Artifacts/<project-name>/
├── feature_plan.md           ← Project agent writes this
├── feature_plan_reviewed.md  ← Orchestrator writes this
└── feature_handoff.md        ← Orchestrator writes this
```

---

## When to Use It

| Use peer review | Skip it |
|---|---|
| Non-trivial implementation plans (3+ files, schema changes) | Single-file bug fixes |
| Anything touching infra, migrations, or auth | Routine page/component builds |

---

## If You Only Have One Workspace

Use `/audit` to self-check your plan before building. Peer review is a force multiplier for when the project grows enough to warrant a second agent.
