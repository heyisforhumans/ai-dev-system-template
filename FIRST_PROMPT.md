# 👋 FIRST_PROMPT.md — Your Starter Message

Copy and send this as your **very first message** to the AI, word for word:

---

## 📋 Copy This

```
I've just set up the AI Dev System template. Before we do anything else, I want you to fully orient yourself with this workspace. Please:

1. Read .agents/BOOTSTRAP.md — this is your orientation file
2. Read .agents/ai-dev-system.md — understand the memory conventions and skills
3. Read .agents/workflows/kickoff.md — and then run it
4. Read docs/how-memory-works.md — so you understand the 3-tier memory system
5. Read docs/file-structure.md — so you understand the MVC conventions we follow

After reading all of these:
- If BOOTSTRAP.md contains [UNCONFIGURED], introduce yourself and begin first-run onboarding
- If it's configured, orient for a normal session and tell me what you now know about this workspace

I want you to actually internalize this system — not summarize the files, but understand them.
You are my AI development partner. This memory stack is how we maintain a persistent, evolving relationship.
The better you know these files, the better our collaboration gets.
```

---

## What Happens After

The AI will do a thorough read of your workspace, then either:

- **First-run (what you want now):** Introduce the memory system, ask questions about your project, and walk you through filling in `BOOTSTRAP.md`
- **Returning session:** Summarize what it knows about your project and ask what you're working on today

After the first session, you won't need this prompt anymore. The AI will orient itself automatically at the start of each session.

---

## Giving the AI Access to This Folder

| Tool | How to grant folder access |
|---|---|
| **Antigravity** | Open VS Code with this folder as your workspace — it reads `.agents/` automatically |
| **Cursor / Windsurf / Cline** | Open the folder, point the AI at it, and paste the prompt above |
| **Claude** | Share individual files or paste key `.agents/` file contents into the chat |
| **ChatGPT Projects** | Upload key files to a Project so they load every session |

---

*After your first session, you can delete or ignore this file.*
