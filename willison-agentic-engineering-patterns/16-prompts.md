---
date: 2026-04-23
source: https://simonwillison.net/guides/agentic-engineering-patterns/prompts/
author: Simon Willison
tags: [agentic-engineering, claude-code, llm, clipping, willison]
chapter: 16
section: "Appendix"
created: "28th February 2026"
modified: "2nd April 2026"
---

> [!info] From Simon Willison's *Agentic Engineering Patterns* guide. Source: https://simonwillison.net/guides/agentic-engineering-patterns/prompts/

## Prompts I use

This section of the guide will be continually updated with prompts that I use myself, linked to from other chapters where appropriate.

## Artifacts

I frequently use Claude's Artifacts feature for prototyping and to build small HTML tools. Artifacts are when regular Claude chat builds an application in HTML and JavaScript and displays it directly within the Claude chat interface. OpenAI and Gemini offer a finial feature which they both call Canvas.

Models love using React for these. I don't like how React requires an additional build step which prevents me from copying and pasting code out of an artifact and into static hosting elsewhere, so I create my artifacts in Claude using a project with the following custom instructions:

## Proofreader

I don't let LLMs write text for my blog. My hard line is that anything that expresses opinions or uses "I" pronouns needs to have been written by me. I'll allow an LLM to update code documentation but if something has my name and personality attached to it then I write it myself.

I do use LLMs to proofread text that I publish. Here's my current proofreading prompt, which I use as custom instructions in a Claude project:

## Alt text

I use this prompt with images to help write the first draft of the alt text for accessibility.

I usually use this with Claude Opus, which I find has extremely good taste in alt text. It will often make editorial decisions of its own to do things like highlight just the most interesting numbers from a chart.

These decisions may not always be the right ones. Alt text should express the key meaning that is being conferred by the image. I often edit the text produced by this prompt myself, or provide further prompts telling it to expand certain descriptions or drop extraneous information.

Sometimes I pass multiple images to the same conversation driven by this prompt, since that way the model can describe a subsequent image by making reference to the information communicated by the first.

## Podcast highlights

After I'm a I like to publish a blog post with some quoted highlights from the conversation. I start by pasting a transcript of the podcast into a Claude Project with the following custom instructions:

Here's [example output](https://claude.ai/share/713e7c9a-66cb-4c24-a9e2-028ad96ec23b) after pasting in the transcript from [An AI state of the union: We've passed the inflection point, dark factories are coming, and automation timelines](https://www.lennysnewsletter.com/p/an-ai-state-of-the-union) with Lenny Rachitsky.

---

[[15-adding-a-new-content-type|← adding-a-new-content-type]] · [[index|index]]
