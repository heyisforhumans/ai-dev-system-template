# Quickstart — AI Dev System

> Set up your AI dev system in 15 minutes. After this, your AI knows your project and you never have to re-explain it.

---

## What This Is

A memory stack for AI-assisted development. Your AI reads it at the start of every session so it knows what you're building, what decisions you've made, and where everything lives — without you having to explain it again.

---

## Prerequisites

- Git
- An AI tool (Antigravity, Cursor, Claude, GPT — any works)
- 15 minutes for the first session. Every session after: 60 seconds.

---

## Setup (Do This Once)

### 1. Clone this template into your project

```bash
git clone https://github.com/heyisforhumans/ai-dev-system-template .agents-template
cp -r .agents-template/.agents ./
rm -rf .agents-template
```

### 2. Open your AI and say:

> "Read `.agents/BOOTSTRAP.md` and run `/kickoff`."

Your AI will detect it's a first session and walk you through setup.

### 3. Commit when done

```bash
git add .agents/
git commit -m "chore: add AI dev system memory files"
```

---

## Every Session After That

Start with:
> "Run `/kickoff`."

That's it.

---

## The 3 Commands You'll Use Every Session

| Command | When | What it does |
|---|---|---|
| `/kickoff` | Session start | Orients AI from memory, surfaces open questions |
| `/save-memory` | Session end | Writes what was done to memory files |
| `/debug` | Something broke | Structured debugging — logs first, then hypothesis |

---

## The 4 Others Worth Knowing

| Command | When |
|---|---|
| `/new-app` | Scaffolding a new app |
| `/audit` | Code hygiene check — catches MVC violations |
| `/memory-model-component` | Generating deep docs for a finished component |
| `/retrospective` | Post-feature — captures lessons learned |

---

## Tips

- **One session = one goal.** Define done before you start.
- **Check logs before the browser.** `docker logs [container] --tail 50` is free.
- **Memory goes stale.** Run `/save-memory` every session.
