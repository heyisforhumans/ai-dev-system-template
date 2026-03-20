#!/usr/bin/env python3
"""
memory_model.py — Component Memory Generator
=============================================
Reads context about a component (source files, agent memory files, optional
text) and calls an AI API to produce a structured component_memory.md
in the component's memory/ directory.

Usage:
  python3 scripts/memory_model.py \\
    --component-name "My Feature" \\
    --component-path /path/to/your/app \\
    --output-dir /path/to/your/app/memory \\
    --output-filename my_feature_component_memory.md \\
    --source-files backend/app/routers/feature.py frontend/src/pages/FeaturePage.tsx \\
    --agent-memory-files .agents/memory/my-app.md \\
    --context-text "Design decisions and gotchas from this session" \\
    --workspace-root /path/to/workspace

API Key: set AI_API_KEY environment variable (falls back to GEMINI_API_KEY).
"""

import argparse
import sys
import os
import datetime
import textwrap

# ---------------------------------------------------------------------------
# Gemini SDK import
# ---------------------------------------------------------------------------
try:
    from google import genai
    from google.genai import types as genai_types
except ImportError:
    print("❌  google-genai not installed. Run: pip3 install google-genai")
    sys.exit(1)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def read_file_safe(path: str, max_chars: int = 12000) -> str:
    """Read a file, truncating if very large, with a header."""
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()
        if len(content) > max_chars:
            content = content[:max_chars] + f"\n\n... [truncated at {max_chars} chars] ..."
        return f"### File: {path}\n```\n{content}\n```\n\n"
    except Exception as e:
        return f"### File: {path}\n[Could not read: {e}]\n\n"


def resolve_path(base: str, rel_or_abs: str) -> str:
    """Resolve a path that may be relative to base, or already absolute."""
    if os.path.isabs(rel_or_abs):
        return rel_or_abs
    return os.path.join(base, rel_or_abs)


def build_prompt(args: argparse.Namespace, file_blocks: str) -> str:
    date_str = datetime.datetime.now().strftime("%Y-%m-%d")

    extra_context = ""
    if args.context_text:
        extra_context = f"\n## Additional Developer Context\n{args.context_text}\n"

    return textwrap.dedent(f"""
    You are a senior software engineer creating a detailed technical memory document
    for a specific component or feature. This document will be read by:
    1. **Human developers** who need to understand what was built and why.
    2. **AI coding agents** who need to implement future features on top of this
       component without re-reading the full conversation history.

    Write the memory document in clear, structured markdown. Every section should
    label which audience it primarily targets: [FOR HUMANS], [FOR AI], or [BOTH].

    ---

    Component Name: {args.component_name}
    Component Path: {args.component_path}
    Date: {date_str}
    {extra_context}

    ## Source Files

    {file_blocks}

    ---

    ## Instructions

    Produce a `component_memory.md` file with the following sections.
    Where a section is not applicable, omit it rather than writing "N/A".

    #### 1. Overview [BOTH]
    2-4 sentence description of what this component does and why it exists.
    Include the user-facing problem it solves.

    #### 2. Architecture [FOR AI]
    - What files were created or modified
    - Key classes, functions, and their responsibilities
    - Data flow: how data enters and leaves this component
    - Any important state machines or enum values

    #### 3. API Contract [FOR AI]
    If this component exposes or consumes an API, document as a table:
    | Method | Path | Request Body | Response | Auth Required |
    Include query params, status codes, and error shapes.

    #### 4. Database Schema [FOR AI]
    If new models/tables were added, show fields, types, and relationships.
    Note any nullable fields and their meaning.

    #### 5. Frontend Integration [FOR AI]
    - Which React components/pages consume or trigger this component
    - Polling intervals, event handlers, or state changes triggered
    - Any localStorage/cookie usage

    #### 6. Business Logic [BOTH]
    The rules embedded in this component that reflect real-world workflow decisions.
    These are the "why" facts not obvious from reading the code.

    #### 7. Key Design Decisions [BOTH]
    Numbered list of architectural choices made and the reason for each.
    Include trade-offs considered but rejected.

    #### 8. Gotchas & Known Issues [BOTH]
    Non-obvious facts, footguns, or known bugs.
    Format: **Issue**: description. **Why**: explanation. **Fix/Workaround**: action.

    #### 9. Extension Guide [FOR AI]
    Step-by-step instructions for the most likely future tasks on this component.
    Keep these as numbered steps an AI agent can follow directly.

    #### 10. Testing Checklist [BOTH]
    Bulleted list of manual steps to verify the component works correctly.
    Should be runnable by a human tester without reading any code.

    ---

    Output ONLY the markdown content, starting with `# {args.component_name} — Component Memory`.
    Do not include any preamble or explanation outside the markdown document itself.
    """).strip()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate a component_memory.md for a finished component."
    )
    parser.add_argument("--component-name", required=True,
                        help="Human-readable name of the component")
    parser.add_argument("--component-path", required=True,
                        help="Absolute path to the component root folder")
    parser.add_argument("--output-dir", required=True,
                        help="Directory where the memory file will be written")
    parser.add_argument("--output-filename", default="component_memory.md",
                        help="Output filename (default: component_memory.md)")
    parser.add_argument("--source-files", nargs="*", default=[],
                        help="Source files, relative to --component-path or absolute")
    parser.add_argument("--agent-memory-files", nargs="*", default=[],
                        help="Agent .md memory files, relative to --workspace-root or absolute")
    parser.add_argument("--context-text", default="",
                        help="Optional freeform context from the developer or AI agent")
    parser.add_argument("--workspace-root", default=os.getcwd(),
                        help="Root of your workspace (for resolving .agents/ paths)")
    parser.add_argument("--api-key", default="",
                        help="API key (falls back to AI_API_KEY or GEMINI_API_KEY env var)")
    parser.add_argument("--model", default="gemini-2.5-flash",
                        help="Model to use (default: gemini-2.5-flash)")

    args = parser.parse_args()

    # -----------------------------------------------------------------------
    # API key resolution — workspace-root-relative .env fallback
    # -----------------------------------------------------------------------
    api_key = (
        args.api_key
        or os.environ.get("AI_API_KEY", "")
        or os.environ.get("GEMINI_API_KEY", "")
    )

    if not api_key:
        env_candidates = [
            os.path.join(args.workspace_root, ".env"),
            os.path.expanduser("~/.env"),
        ]
        for env_path in env_candidates:
            if os.path.exists(env_path):
                with open(env_path) as f:
                    for line in f:
                        line = line.strip()
                        if line.startswith("AI_API_KEY=") or line.startswith("GEMINI_API_KEY="):
                            api_key = line.split("=", 1)[1].strip().strip('"').strip("'")
                            break
            if api_key:
                break

    if not api_key:
        print("❌  No API key found.")
        print("    Set AI_API_KEY in your environment or in .env at your workspace root.")
        print("    Run: scripts/validate_env.sh to check your setup.")
        sys.exit(1)

    print(f"\n🧠  Memory Model: {args.component_name}")
    print(f"📁  Output: {args.output_dir}/{args.output_filename}")
    print()

    # -----------------------------------------------------------------------
    # Collect file content
    # -----------------------------------------------------------------------
    file_blocks = ""

    if args.source_files:
        print(f"📄  Reading {len(args.source_files)} source file(s)...")
        for rel_path in args.source_files:
            abs_path = resolve_path(args.component_path, rel_path)
            file_blocks += read_file_safe(abs_path)

    if args.agent_memory_files:
        print(f"📚  Reading {len(args.agent_memory_files)} agent memory file(s)...")
        file_blocks += "\n## Agent Memory Files\n\n"
        for rel_path in args.agent_memory_files:
            abs_path = resolve_path(args.workspace_root, rel_path)
            file_blocks += read_file_safe(abs_path, max_chars=8000)

    if not file_blocks.strip():
        file_blocks = "[No source files provided — generating from component name and context only]"

    # -----------------------------------------------------------------------
    # Build prompt and call API
    # -----------------------------------------------------------------------
    prompt = build_prompt(args, file_blocks)

    print(f"🤖  Calling {args.model}...")
    try:
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model=args.model,
            contents=prompt,
        )
        result_text = response.text or ""
    except Exception as e:
        print(f"❌  API error: {e}")
        sys.exit(1)

    # -----------------------------------------------------------------------
    # Write output
    # -----------------------------------------------------------------------
    os.makedirs(args.output_dir, exist_ok=True)
    out_path = os.path.join(args.output_dir, args.output_filename)

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(result_text)

    print(f"\n✅  Written to: {out_path}")
    print()
    lines = result_text.splitlines()
    preview = lines[:30]
    print("─" * 60)
    print("Preview (first 30 lines):")
    print("─" * 60)
    print("\n".join(preview))
    if len(lines) > 30:
        print(f"... [{len(lines) - 30} more lines]")
    print()


if __name__ == "__main__":
    main()
