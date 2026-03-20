---
description: Post-feature retrospective — capture lessons learned and write them to memory
---

# /retrospective

Run this after finishing a significant feature or sprint. Takes 5 minutes. Turns tribal knowledge into durable memory.

---

## Step 1 — What Did We Build?

Summarize in 2–3 sentences:
- What feature/component was completed
- What user problem it solves
- What files were created or modified (list them)

---

## Step 2 — What Was Harder Than Expected?

Ask yourself (or the user):
- Was there anything that took 3x longer than it should have?
- What did you have to debug that felt avoidable?
- Were there any surprises about how the system worked?

---

## Step 3 — What Did You Learn?

Specifically:
- What would you do differently on the next similar feature?
- Any new patterns or anti-patterns discovered?
- Any documentation that was missing and would have helped?

---

## Step 4 — Write to Memory

Add a Retrospective entry to `.agents/memory/[app].md`:

```markdown
### Retrospective: [Feature Name] — YYYY-MM-DD
- **What was built**: [2-sentence summary]
- **What was hard**: [the unexpected things]
- **Lessons learned**: [what to do differently next time]
- **Patterns to reuse**: [anything worth extracting into a skill or workflow]
```

---

## Step 5 — Should This Become a Skill?

Ask: *"Would the lessons from this feature help an AI agent on a similar task in a different project?"*

If yes → this is a candidate for a new skill file. Note it in `idea_backlog.md`:
```
- [ ] New skill: [skill topic] — based on [feature] learnings
```

---

## Step 6 — Run /save-memory

Finalize with `/save-memory` to commit the retrospective entry to git.
