# Multi-Tool AI Agent using MCP

This project demonstrates how to build a **tool-augmented AI agent** using **MCP (Model Context Protocol)** and **LangChain**, where a single agent can interact with multiple external tools dynamically.

---

## What I Built

- Created **two MCP servers**:
  - A **Math server** for arithmetic operations
  - A **Weather server** exposed over HTTP
- Built a **client AI agent** that:
  - Connects to multiple MCP servers
  - Automatically selects the correct tool based on the user query
  - Uses an LLM to reason and invoke tools

---

## Example Queries

```text
User: what's (3 + 4) * 12?
User: what's the weather in dwarka sec-3 today?
<img width="1387" height="142" alt="image" src="https://github.com/user-attachments/assets/b155454f-e997-42dc-9d7c-027416bc2957" />

```
## Tech Stack Used

- Python

- LangChain

- MCP (Model Context Protocol)

- FastMCP

- Groq LLM (qwen/qwen3-32b)

- AsyncIO

## Key Learnings

- How AI agents interact with external tools

- How MCP enables standardized tool communication

- Managing multiple tool servers (stdio + HTTP)

- Letting the model decide which tool to call and when
