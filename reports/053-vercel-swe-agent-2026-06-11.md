# Evaluation: Vercel — Software Engineer, Agent

**Date:** 2026-06-11
**URL:** https://job-boards.greenhouse.io/vercel/jobs/5704320004
**Archetype:** Agentic / Automation
**Score:** 3.8/5
**Legitimacy:** High Confidence
**PDF:** output/cv-vercel-swe-agent-2026-06-11.pdf

---

## A) Role Summary

| Field | Detail |
|-------|--------|
| Archetype | Agentic / Automation — production agent that investigates incidents, fixes builds, reviews code, answers questions |
| Domain | Ship a single unified agent across dashboard, CLI, Slack with multi-step reasoning, sandboxed code execution, autonomous action |
| Function | Build (greenfield agent design, tool integrations, prompt engineering, RAG, infrastructure) |
| Seniority | Senior–Staff IC (7+ years required; comp at Staff level) |
| Remote | Hybrid — San Francisco |
| Comp | $232,000–$348,000 + equity (Staff-level band, SF) |
| TL;DR | Build the AI agent that makes Vercel feel like having a seasoned infra engineer on your team. Design multi-step agentic workflows, sandboxed execution, dynamic skill injection, and tool integrations across the platform. |

---

## B) Match with CV

| JD Requirement | CV Match | Strength |
|----------------|----------|----------|
| Agentic systems design | AgentProbe: 3-agent LangGraph system (Orchestrator, RAG Tracer, Auto Fix), multi-step reasoning, tool calls | ✅ Direct proof |
| Multi-step agent workflows coordinating across tools/APIs | AgentProbe: plan-execute-react loop, cross-agent state management | ✅ Direct proof |
| LLM APIs (Anthropic, OpenAI) + prompt engineering | AgentProbe: multi-provider routing (Anthropic/OpenAI/Groq/Ollama), calibrated judge prompts | ✅ Direct proof |
| RAG pipelines | AgentProbe: ChromaDB + embeddings + retrieval scoring | ✅ Direct proof |
| 7+ years SWE | 8+ years (Entrata 2017–2024 + GMU TA) | ✅ Exceeds |
| Full-stack (infra, CI/CD, observability) | FastAPI + React + GitHub Actions CI/CD; Docker + AWS + PostgreSQL at Entrata | ✅ Solid |
| Ship independently, influence architecture | AgentProbe built greenfield to open-source; 20+ modules at Entrata across 120+ sprints | ✅ Strong |
| Strong TypeScript proficiency | TS listed in skills; Entrata primary was JS/Python; no TS-first portfolio project | ⚠️ Gap — documented but not demonstrated |
| Dynamic skill injection / runtime capability acquisition | Not in CV; novel infrastructure challenge | ⚠️ New territory |
| Sandboxed execution environments | Not explicit in CV | ⚠️ Adjacent (Docker containerization at Entrata) |
| H-1B | Vercel is US-headquartered, well-funded (Series E, ~500 employees) — likely H-1B sponsor; verify | ⚠️ Confirm |

**Gaps:**
- **TypeScript primary**: The hard requirement is "strong TypeScript proficiency." Parimala's portfolio is Python/JS. TypeScript is in skills but not demonstrated in featured projects. Needs to be directly addressed.
- **Sandboxed execution / dynamic skill injection**: Interesting novel challenge but not a direct proof point in CV.
- **Vercel/Next.js ecosystem**: Bonus only — not a blocker.

---

## C) Score Rationale

3.8/5 — The agent mission is an exact archetype match (multi-step reasoning, LLM APIs, RAG, tool integrations = AgentProbe entire stack). Comp is exceptional ($232–348K). Location now open (SF hybrid fine). TypeScript gap is the primary drag — it's a stated hard requirement and Parimala's public projects are Python-primary. However, the agent work maps perfectly and TypeScript proficiency from Entrata JS background is real even if not leading. H-1B needs confirmation. If TypeScript depth can be demonstrated, this is a 4.2+ role.

---

## Machine Summary

```yaml
report_num: 053
company: Vercel
role: Software Engineer, Agent
date: 2026-06-11
score: 3.8
archetype: Agentic / Automation
legitimacy: High Confidence
location: San Francisco (hybrid)
comp_range: "$232,000–$348,000 + equity (Staff-level band)"
visa_risk: low-medium (well-funded US company ~500 employees — likely H-1B, verify)
key_gaps:
  - TypeScript primary language (hard requirement; Parimala Python/JS-primary — not TS-first in portfolio)
  - Sandboxed execution environments / dynamic skill injection (new territory)
  - H-1B: verify in recruiter screen
key_strengths:
  - AgentProbe = exact proof: multi-step LangGraph agents, LLM APIs, RAG, prompt engineering, tool calls
  - Agentic systems design greenfield to open-source — matches "ship independently, influence architecture"
  - Comp $232-348K exceptional
  - Location open (SF hybrid fine)
location_risk: low — user open to any location
recommend: apply — TypeScript gap acknowledged; agent match too strong to skip; lead with AgentProbe
```
