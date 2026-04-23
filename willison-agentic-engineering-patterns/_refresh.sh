#!/usr/bin/env bash
# Re-pull Simon Willison's Agentic Engineering Patterns guide into this folder.
# Simon updates chapters in place; run this when you want a fresh snapshot.
#
# Usage:  ./_refresh.sh
# Deps:   defuddle (`npm install -g defuddle`), python3
#
# Idempotent: overwrites *-slug.md chapter files; leaves index.md, _refresh.sh,
# and _process.py alone.

set -euo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BASE="https://simonwillison.net/guides/agentic-engineering-patterns"

SLUGS=(
  what-is-agentic-engineering
  code-is-cheap
  hoard-things-you-know-how-to-do
  better-code
  anti-patterns
  how-coding-agents-work
  using-git-with-coding-agents
  subagents
  red-green-tdd
  first-run-the-tests
  agentic-manual-testing
  linear-walkthroughs
  interactive-explanations
  gif-optimization
  adding-a-new-content-type
  prompts
)

if ! command -v defuddle >/dev/null 2>&1; then
  echo "defuddle not found. install with: npm install -g defuddle" >&2
  exit 1
fi

RAW="$(mktemp -d)"
trap 'rm -rf "$RAW"' EXIT

echo "fetching ${#SLUGS[@]} chapters -> $RAW"
for slug in "${SLUGS[@]}"; do
  defuddle parse "$BASE/$slug/" --md -o "$RAW/$slug.md" &
done
wait

echo "processing into $DIR"
python3 "$DIR/_process.py" "$RAW" "$DIR"

echo "done. pulled on $(date -u +%Y-%m-%d) ."
