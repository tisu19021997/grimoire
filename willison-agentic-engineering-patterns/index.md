---
date: 2026-04-23
source: https://simonwillison.net/guides/agentic-engineering-patterns/
author: Simon Willison
tags: [agentic-engineering, claude-code, llm, clipping, willison, guide-index]
---

# Agentic Engineering Patterns — Simon Willison

Full clone of Simon's in-progress guide, pulled 2026-04-23. Chapters keep his exact words (web-clipper style), attribution at the top of each file, source link intact. My own synthesis lives in [[agentic-engineering]] at vault root.

> Source: https://simonwillison.net/guides/agentic-engineering-patterns/

## Chapters

### 1. Principles

- [[01-what-is-agentic-engineering|What is agentic engineering?]]
- [[02-code-is-cheap|Writing code is cheap now]]
- [[03-hoard-things-you-know-how-to-do|Hoard things you know how to do]]
- [[04-better-code|AI should help us produce better code]]
- [[05-anti-patterns|Anti-patterns: things to avoid]]

### 2. Working with coding agents

- [[06-how-coding-agents-work|How coding agents work]]
- [[07-using-git-with-coding-agents|Using Git with coding agents]]
- [[08-subagents|Subagents]]

### 3. Testing and QA

- [[09-red-green-tdd|Red/green TDD]]
- [[10-first-run-the-tests|First run the tests]]
- [[11-agentic-manual-testing|Agentic manual testing]]

### 4. Understanding code

- [[12-linear-walkthroughs|Linear walkthroughs]]
- [[13-interactive-explanations|Interactive explanations]]

### 5. Annotated prompts

- [[14-gif-optimization|GIF optimization tool using WebAssembly and Gifsicle]]
- [[15-adding-a-new-content-type|Adding a new content type to my blog-to-newsletter tool]]

### 6. Appendix

- [[16-prompts|Prompts I use]]

## notes

- The guide is explicitly a living document — Simon says no chapter is ever finished. Re-pull periodically if something feels stale. Last pulled: **2026-04-23**.
- Refresh: `./_refresh.sh` from this folder (needs `defuddle` + `python3`). Overwrites chapter files only; leaves `index.md` and the scripts alone.
- My own take + threads to pull: [[agentic-engineering]]
- Cross-refs: [[claude-code]], [[vibe-coding]], [[karpathy-llm-wiki]]
