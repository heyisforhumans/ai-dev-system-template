---
description: Orient the AI at the start of every session. Detects first-run and triggers onboarding.
---

# /kickoff

Run this at the start of every session, or say "let's get started" / "what were we working on?".
The AI runs this automatically when the conversation begins.

---

## Step 1 — Detect First-Run

Open and read `.agents/BOOTSTRAP.md`.

**IMPORTANT**: Search for the string `[UNCONFIGURED]` in the file.

**If `[UNCONFIGURED]` is found:**

**→ STOP. Do not summarize files. Run first-run onboarding immediately.**

Say exactly this:

> 👋 Hey — it looks like this is your **first session** with the AI Dev System.
>
> This memory stack is modeled after Rails MVC conventions, adapted for AI-assisted development. It gives me a persistent memory of your project so you never have to re-explain things between sessions.
>
> **Would you like me to walk you through how it works and help you configure your workspace?** It takes about 10 minutes, and after that I'll remember everything about your project automatically.

If yes:
1. Walk through `GETTING_STARTED.md` section by section, conversationally — don't paste the whole document
2. Help the user fill in `.agents/BOOTSTRAP.md` interactively, one section at a time
3. Create their first app memory file if they name an app
4. When done: "You're all set! Remove the `[UNCONFIGURED]` line from BOOTSTRAP.md and commit your `.agents/` folder. Future sessions will start automatically."

If no → note that setup can be done anytime with `/kickoff`.

**Do not proceed to Step 2 on a first-run session.**

---

## Step 2 — Normal Session Orientation

If BOOTSTRAP is configured, read it fully. Then:

### 2a — Load Active App Memory
For each app listed in BOOTSTRAP's "Active memory files" section:
- Read the corresponding `.agents/memory/[app].md`
- Note the most recent session entry (date + what was done)
- Note any Open Questions

### 2b — Surface the Context
Reply with a brief orientation (3–5 bullets max):

```
🧠 Session start — [Date]

Last session: [what was worked on, from memory file]
Open questions: [any unresolved questions]
Active backlog: [top 1–2 items from idea_backlog.md]
Ready to work on: [inferred from context, or ask]
```

### 2c — Ask What to Work On
If it's not clear from context, ask:
> "What are we working on today?"

---

## Step 3 — Load Relevant Skills

Based on what you'll be working on, load the relevant skill:
- Working on database models → read `skills/mvc-models/SKILL.md`
- Working on API routes → read `skills/mvc-controllers/SKILL.md`
- Working on frontend pages → read `skills/mvc-views/SKILL.md`
- Working on reusable components → read `skills/mvc-components/SKILL.md`
- Auth/JWT work → read `skills/fastapi-auth/SKILL.md`
- Docker/containers → read `skills/docker-compose-patterns/SKILL.md`

---

## Notes

- This workflow runs in under 60 seconds on a configured workspace
- First-run onboarding typically takes 10–15 minutes
- After first-run, the user should commit the filled-in `.agents/` folder to their repo
