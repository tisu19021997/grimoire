---
date: 2026-04-23
source: https://simonwillison.net/guides/agentic-engineering-patterns/first-run-the-tests/
author: Simon Willison
tags: [agentic-engineering, claude-code, llm, clipping, willison]
chapter: 10
section: "Testing and QA"
created: "24th February 2026"
modified: "28th February 2026"
---

> [!info] From Simon Willison's *Agentic Engineering Patterns* guide. Source: https://simonwillison.net/guides/agentic-engineering-patterns/first-run-the-tests/

## First run the tests

Automated tests are no longer optional when working with coding agents.

The old excuses for not writing them - that they're time consuming and expensive to constantly rewrite while a codebase is rapidly evolving - no longer hold when an agent can knock them into shape in just a few minutes.

They're also *vital* for ensuring AI-generated code does what it claims to do. If the code has never been executed it's pure luck if it actually works when deployed to production.

Tests are also a great tool to help get an agent up to speed with an existing codebase. Watch what happens when you ask Claude Code or similar about an existing feature - the chances are high that they'll find and read the relevant tests.

Agents are already biased towards testing, but the presence of an existing test suite will almost certainly push the agent into testing new changes that it makes.

Any time I start a new session with an agent against an existing project I'll start by prompting a variant of the following:

For my Python projects I have [pyproject.toml set up](https://til.simonwillison.net/uv/dependency-groups) such that I can prompt this instead:These four word prompts serve several purposes:
1. It tells the agent that there is a test suite and forces it to figure out how to run the tests. This makes it almost certain that the agent will run the tests in the future to ensure it didn't break anything.
2. Most test harnesses will give the agent a rough indication of how many tests they are. This can act as a proxy for how large and complex the project is, and also hints that the agent should search the tests themselves if they want to learn more.
3. It puts the agent in a testing mindset. Having run the tests it's natural for it to then expand them with its own tests later on.

Similar to ["Use red/green TDD"](https://simonwillison.net/guides/agentic-engineering-patterns/red-green-tdd/), "First run the tests" provides a four word prompt that encompasses a substantial amount of software engineering discipline that's already baked into the models.

---

[[09-red-green-tdd|← red-green-tdd]] · [[index|index]] · [[11-agentic-manual-testing|agentic-manual-testing →]]
