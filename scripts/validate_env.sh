#!/usr/bin/env bash
# validate_env.sh — Check required environment variables before running
# Run this before your first session or after cloning

set -e

REQUIRED_VARS=(
  "AI_API_KEY"
)

OPTIONAL_VARS=(
  "GEMINI_API_KEY"
  "DATABASE_URL"
  "SECRET_KEY"
)

echo ""
echo "🔍 AI Dev System — Environment Check"
echo "══════════════════════════════════════"

# Check .env file exists
if [ -f ".env" ]; then
  echo "✅ .env file found"
  source .env 2>/dev/null || true
else
  echo "⚠️  No .env file found"
  echo "   Run: cp .env.template .env  and fill in your values"
  echo ""
fi

# Check required vars
echo ""
echo "Required variables:"
MISSING=0
for VAR in "${REQUIRED_VARS[@]}"; do
  VALUE="${!VAR:-}"
  if [ -z "$VALUE" ]; then
    # Also check GEMINI_API_KEY as fallback for AI_API_KEY
    if [ "$VAR" = "AI_API_KEY" ] && [ -n "${GEMINI_API_KEY:-}" ]; then
      echo "  ✅ $VAR — not set, but GEMINI_API_KEY is set (will be used as fallback)"
    else
      echo "  ❌ $VAR — NOT SET"
      MISSING=$((MISSING + 1))
    fi
  else
    # Show only first 8 chars for security
    MASKED="${VALUE:0:8}..."
    echo "  ✅ $VAR = $MASKED"
  fi
done

# Check optional vars
echo ""
echo "Optional variables:"
for VAR in "${OPTIONAL_VARS[@]}"; do
  VALUE="${!VAR:-}"
  if [ -z "$VALUE" ]; then
    echo "  ○  $VAR — not set (may be required depending on your stack)"
  else
    MASKED="${VALUE:0:8}..."
    echo "  ✅ $VAR = $MASKED"
  fi
done

# Check Python + google-genai
echo ""
echo "Dependencies:"
if command -v python3 &>/dev/null; then
  echo "  ✅ python3 found: $(python3 --version)"
  if python3 -c "from google import genai" 2>/dev/null; then
    echo "  ✅ google-genai installed"
  else
    echo "  ⚠️  google-genai not installed — run: pip3 install google-genai"
  fi
else
  echo "  ❌ python3 not found"
fi

echo ""
if [ $MISSING -eq 0 ]; then
  echo "✅ All required variables are set. Ready to go!"
else
  echo "❌ $MISSING required variable(s) missing. Set them in .env before continuing."
fi
echo ""
