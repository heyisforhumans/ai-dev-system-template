# Platform Guide — AI Tool-Specific Notes

> This memory system works with any AI coding tool. This guide covers platform-specific setup and behavior.

---

## Antigravity (VS Code Extension)

**Memory:** Antigravity has a built-in Knowledge Item (KI) system that automatically distills knowledge from conversations and stores it at `~/.gemini/antigravity/knowledge/`. This is your Tier 1 memory — you don't manage it directly.

**First-run:** When you open a workspace with an unconfigured `BOOTSTRAP.md`, Antigravity will detect it and trigger the onboarding flow automatically.

**Workflows:** Type `/kickoff`, `/save-memory`, `/new-app`, etc. directly in the chat. Antigravity reads the `.agents/workflows/` folder automatically.

**Skills:** Antigravity loads relevant skills based on context. You can also say "read the mvc-models skill" to load it explicitly.

**Component memories:** After finishing a major feature, run `/memory-model-component`. Antigravity calls the Gemini API and writes the doc to `[app]/memory/`.

**KI naming:** If Antigravity creates a KI with a generic name (like `overview.md`), you can rename the artifact file and update the `metadata.json` in `~/.gemini/antigravity/knowledge/[ki-name]/` to match.

**Recommended `.env` key:** `GEMINI_API_KEY` (for `memory_model.py`)

---

## Claude (claude.ai or API)

**Memory:** Claude has no persistent memory system. At the start of each session, paste the contents of:
1. `.agents/BOOTSTRAP.md`
2. `.agents/memory/[your-app].md` (the most relevant app)

You can say: *"Here's my project context — [paste BOOTSTRAP contents]"*

**Workflows:** Claude can follow the workflow instructions if you say the workflow name and paste the relevant `.md` file. Example:
> "Follow this workflow: [paste kickoff.md contents]"

Or give Claude access to your project folder and ask it to read `.agents/workflows/kickoff.md`.

**Component memories:** Run `python3 scripts/memory_model.py` manually with a Claude or OpenAI API key (set `AI_API_KEY` or modify the script to use your provider).

**Recommended workflow:** Keep sessions short and run `/save-memory` at the end of each one. Paste relevant context at the start of each new session.

**Recommended `.env` key:** `AI_API_KEY` or `ANTHROPIC_API_KEY`

---

## ChatGPT (chat.openai.com or API)

**Memory:** ChatGPT Plus has limited memory features built in, but they're not structured for this system. Treat it like Claude — paste `BOOTSTRAP.md` at the start of each session.

**Projects feature (ChatGPT Plus):** If you use ChatGPT Projects, you can upload `BOOTSTRAP.md` as a project file so it's always available. Do the same with active app memory files.

**Workflows:** Same approach as Claude — paste the workflow markdown and ask GPT to follow it.

**Component memories:** Use `memory_model.py` with an OpenAI API key by modifying the script to use the OpenAI SDK.

---

## Cursor / Windsurf / Cline

**Memory:** These tools typically support a "rules" or "system prompt" file that loads on every session. Use this for BOOTSTRAP:

- **Cursor:** Add BOOTSTRAP.md contents to `.cursorrules` in your workspace root
- **Windsurf:** Use the workspace instructions/system prompt feature
- **Cline:** Use the system prompt configuration

**Workflows:** Cursor/Windsurf can read files from your project. Point the AI at `.agents/workflows/kickoff.md` and ask it to follow the steps.

**Skills:** Same approach — ask the agent to read the relevant skill file before starting work.

**Component memories:** `memory_model.py` works the same way — run it from the terminal with your API key set.

---

## General Tips (All Platforms)

1. **Fill in BOOTSTRAP.md completely on day one.** The more context it has, the less you'll need to repeat yourself.

2. **Run `/save-memory` at the end of every session.** Even a brief summary is better than nothing. The next session will start much faster.

3. **Trust the file structure.** When you or the AI aren't sure where a file goes, check `docs/file-structure.md`. The answer is always there.

4. **Start with `/kickoff`.** Even if you know what you're working on, running kickoff ensures the AI is oriented and has the right skills loaded.
