---
description: Structured debugging procedure — error → memory check → hypothesis → fix → document
---

# /debug

Run this when something is broken and you're not sure why.
Prevents spinning in circles. Every debug session ends with a documented outcome.

---

## Step 0 — Check Logs First *(do this before anything else)*

**Before opening a browser, before reading code, before forming any hypothesis:**

```bash
docker logs [container-name] --tail 50
# or for compose:
docker compose logs [service] --tail 50 2>&1
```

Look for: `ERROR`, `Traceback`, `Exception`, `WARN`, connection refused, 404, 500.

**Cost rule:** Log inspection = free. Browser/DOM inspection = expensive. Always exhaust logs first.

- If the log has a clear traceback → go to Step 4 (form hypothesis). Skip 1–3.
- If the log shows nothing → the problem is likely frontend. Now open the browser.

---

## Step 1 — Read the Error

Copy the full error message (including stack trace if available). Identify:
- **What failed**: which endpoint, function, or component
- **Error type**: 500 server error, 404, CORS, import error, DB error, etc.
- **When it started**: after a specific change? always? intermittent?

---

## Step 2 — Check Memory for Known Issues

Read `.agents/memory/[app].md` — specifically the **Gotchas** and most recent session entries.

Ask: *"Has this exact issue been seen before?"*

If yes → apply the documented fix, skip to Step 5.

---

## Step 3 — Check Relevant Skill

If the error is in a known domain, read the relevant skill:
- Auth/JWT errors → `skills/fastapi-auth/SKILL.md`
- CORS errors → `skills/security-cors-headers/SKILL.md`
- Docker/container errors → `skills/docker-compose-patterns/SKILL.md`
- DB errors → `skills/mvc-models/SKILL.md`

Skills often contain **Gotchas** sections with known footguns.

---

## Step 4 — Form a Hypothesis

State your hypothesis explicitly before touching any code:
> "I think the problem is [X] because [Y]. My fix is [Z]."

Don't try multiple things simultaneously — fix one thing at a time.

---

## Step 5 — Apply Fix and Test

Apply the minimal fix. Verify:
- Does the specific error go away?
- Did anything else break?

If the fix didn't work: note what you learned, form a new hypothesis, repeat.

---

## Step 6 — Document the Outcome

Whether the fix worked or not, write one line to `.agents/memory/[app].md`:

**If fixed:**
```
- Gotcha: [error description]. Fix: [what you did]. Root cause: [why it happened].
```

**If unresolved:**
```
- Open question: [error description]. Tried: [what you tried]. Needs: [what's needed to solve].
```

Then run `/save-memory` if the session is ending.

---

## Anti-Patterns to Avoid

- ❌ Changing multiple things at once
- ❌ Restarting the server/container without reading the logs first
- ❌ "Let me just try this" without forming a hypothesis
- ❌ Fixing the error without understanding why it happened
