---
description: Generate a structured component_memory.md for the component you just finished building
---

# /memory-model-component

Run this when you have just finished building or significantly modifying a component or feature.
Calls an AI API to generate a deep 10-section technical memory document.

---

## Step 1 — Auto-Detect Context

Read back through the current conversation to infer:

| Variable | How to infer |
|---|---|
| `COMPONENT_NAME` | The most recently finished feature/component |
| `COMPONENT_PATH` | The app root of that feature |
| `OUTPUT_DIR` | `COMPONENT_PATH/memory/` — create if it doesn't exist |
| `OUTPUT_FILENAME` | `[component_slug]_component_memory.md` — be specific |
| `SOURCE_FILES` | All files created or edited during this conversation (relative to `COMPONENT_PATH`) |
| `AGENT_MEMORY_FILES` | The `.agents/memory/[app-name].md` file for this app |
| `CONTEXT_TEXT` | Design decisions, gotchas, business logic from this conversation |

Only ask the user if `COMPONENT_PATH` is ambiguous.

---

## Step 2 — Run the Script

```bash
python3 scripts/memory_model.py \
  --component-name "COMPONENT_NAME" \
  --component-path /path/to/app \
  --output-dir /path/to/app/memory \
  --output-filename specific_component_memory.md \
  --source-files relative/file1.py relative/file2.tsx \
  --agent-memory-files .agents/memory/app-name.md \
  --context-text "Design decisions and gotchas from this session" \
  --workspace-root /path/to/workspace/root
```

**API key**: Script reads `AI_API_KEY` from environment, falling back to `GEMINI_API_KEY`.
Set `WaitMsBeforeAsync` to `90000` — script usually finishes in ~30s.

---

## Step 3 — Register the Output

Add to the Component Memories table in `.agents/memory/[app].md`:
```markdown
## Component Memories
| Component | File | Date |
|---|---|---|
| [Feature Name] | `[app]/memory/[feature]_component_memory.md` | YYYY-MM-DD |
```

---

## Notes

- `memory/` is for AI-generated artifacts only — human docs go in `docs/`
- Both `memory/` and `docs/` should be excluded from Docker builds via `.dockerignore`
- Re-running is safe — overwrites the existing file
- Output sections: Overview, Architecture, API Contract, DB Schema, Frontend Integration, Business Logic, Key Design Decisions, Gotchas, Extension Guide, Testing Checklist
