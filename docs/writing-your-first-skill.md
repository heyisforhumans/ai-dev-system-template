# Writing Your First Skill

> Skills are how you teach the AI the conventions of your specific stack. This guide walks you through writing one from scratch.

---

## What Is a Skill?

A skill is a markdown file that tells the AI:
1. What layer/domain it's working in
2. What files to create and where
3. What naming conventions to follow
4. What rules to never break

The AI reads the relevant skill before starting work, so it follows your conventions without being told each time.

---

## When to Write a Skill

Write a skill when:
- You have a consistent pattern the AI keeps getting wrong
- You've figured out the "right way" to do something in your stack
- You want to capture conventions from a `/retrospective` or debug session
- You're adding a new technology that the AI doesn't know your conventions for

---

## The Skill File Format

Skills live in `.agents/skills/[skill-name]/SKILL.md`.

```markdown
---
description: One-line description of what this skill covers and when to load it
---

# [Skill Name]

> Brief description of this layer/domain and its job

---

## Stack

| Generic concept | Your specific tool |
|---|---|
| [what it does] | [your tool name] |

---

## File Structure

\`\`\`
where/
├── files/        ← go in this structure
└── like/this.py
\`\`\`

---

## Naming Conventions

- Files: [your naming pattern]
- Classes: [your naming pattern]
- Functions: [your naming pattern]

---

## [Code Template / Example]

\`\`\`python
# Show a concrete example of what a file in this layer looks like
\`\`\`

---

## Rules

1. **Rule one.** Explanation.
2. **Rule two.** Explanation.
3. **Rule three.** Explanation.

---

## Gotchas

Known issues and non-obvious behavior in this domain:
- **Issue**: description. **Why**: explanation. **Fix**: action.
```

---

## Example: Writing a "Redis Caching" Skill

Say you use Redis for caching and the AI keeps implementing it differently each time. Here's how you'd write a skill:

**File:** `.agents/skills/redis-caching/SKILL.md`

```markdown
---
description: Redis caching conventions. Covers key naming, TTL standards, and cache invalidation patterns.
---

# Redis Caching — The Speedway

> Cache frequently-read data. Never cache data that must be real-time accurate.

## File Structure

\`\`\`
backend/app/
├── cache.py       ← Redis client + helper functions
└── routers/
    └── products.py ← Example: routes that use caching
\`\`\`

## Key Naming Convention

Always use: `[resource]:[id]:[field]`
- `product:42:details`
- `user:7:cached_orders`

## TTL Standards

| Data type | TTL |
|---|---|
| Product catalog | 1 hour (3600s) |
| User session data | 15 minutes (900s) |
| Never cache | Real-time inventory counts |

## Rules

1. **Use the helper, not the client directly.** All cache calls go through `cache.py` helpers.
2. **Always set a TTL.** No cache entry should live forever.
3. **Invalidate on write.** When a product is updated, delete `product:[id]:*`.
```

---

## After Writing Your Skill

1. Add it to `.agents/ai-dev-system.md` in the skills list
2. Add the load trigger: when should the AI load this skill? (e.g., "when working on caching logic")
3. Test it: start a session about the relevant domain and see if the AI follows the conventions

---

## Tips

- **Start with an existing skill as a template.** Copy `mvc-models/SKILL.md` and adapt it.
- **Keep rules short.** A rule that needs 3 sentences to explain is probably two rules.
- **Add Gotchas as you discover them.** The best time to add a gotcha is right after you've been burned by it.
- **Skills evolve.** Update them when conventions change — stale skills are worse than no skill.
