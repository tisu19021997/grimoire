---
date: 2026-04-23
source: https://simonwillison.net/guides/agentic-engineering-patterns/what-is-agentic-engineering/
tags: [agentic-engineering, claude-code, llm, practice]
mood: clarifying
---

# agentic engineering — Simon Willison's framing

Simon is staking out a definition so it doesn't melt into the "vibe coding" puddle. **The whole piece is a rescue mission for two words.**

## the rescue

- **Vibe coding** = the *original* Karpathy meaning: you don't look at the code. Prototype-grade. "I vibe coded this" should keep meaning *I haven't even read how it works.*
- **Agentic engineering** = the other end of the scale. Pros using coding agents (Claude Code, OpenAI Codex, Gemini CLI) to **amplify** existing expertise, not bypass it.

Stretching "vibe coding" to cover any LLM-assisted code, Simon argues, is a mistake — it devalues the term's useful narrowness. We *need* a word for unreviewed prototype-grade output that isn't the same word we use for production work.

## what a coding agent actually is

> Software that calls an LLM with your prompt and a set of tool definitions, runs whichever tools the LLM requests, feeds the results back, and loops until the goal is met.

**Code execution is the defining capability.** Without it you have a chatbot. With it, the agent can iterate toward something that *demonstrably works* — tests run, output checked, loop continues.

## the meta-move

Simon's stated goal for the guide: name patterns that *won't go stale as the tools advance.* That's the same move [[karpathy-llm-wiki]] makes for personal knowledge — **compile once at the right level of abstraction, query forever.** This vault is built on the same bet.

## threads to pull

- Which of his patterns survive the next model jump? Which look obvious in hindsight already?
- Where's the line between *amplifying* expertise and *outsourcing the part where you'd have learned something*?
- Is there a "vibe X" for music? Vibe guitar — playing without learning theory? Vibe photography — auto mode and a good preset? When is vibe-mode the right choice and when does it rob you?

See also: [[claude-code]], [[vibe-coding]], [[karpathy-llm-wiki]]
