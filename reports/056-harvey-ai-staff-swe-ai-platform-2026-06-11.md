# Evaluation: Harvey AI — Staff Software Engineer, AI Platform

**Date:** 2026-06-11
**URL:** https://jobs.ashbyhq.com/harvey/01da8934-d3e3-4ebb-beb9-681b3c24fb9c
**Archetype:** AI Platform / LLMOps
**Score:** 4.2/5
**Legitimacy:** High Confidence
**PDF:** output/cv-harvey-ai-staff-swe-ai-platform-2026-06-11.pdf

---

## A) Role Summary

| Field | Detail |
|-------|--------|
| Archetype | AI Platform / LLMOps — build the foundation every product and agent team at Harvey builds upon |
| Domain | Legal AI — model routing, context management, eval frameworks, shared abstractions for all Harvey products |
| Function | Platform (build infra, not just use it — SDKs, primitives, routing, eval tooling) |
| Seniority | Staff IC (8+ years, cross-team technical leadership) |
| Remote | SF or NY — 3+ days/week in-office |
| Comp | $238,000–$290,000 base + equity (median total comp ~$336K) |
| TL;DR | Build Harvey's AI Platform layer: model routing, context engineering, eval infrastructure, and shared abstractions that make every product team faster. The foundation all of Harvey's agents run on. |

---

## B) Match with CV

| JD Requirement | CV Match | Strength |
|----------------|----------|----------|
| Model integration, routing, multi-provider AI | AgentProbe: dynamic routing across Anthropic, OpenAI, Groq, Ollama by task + latency + capability | ✅ Direct proof |
| Evaluation infrastructure for teams | AgentProbe: 5-metric LLM-as-judge eval engine, CI/CD gates, regression tracking — shared eval system | ✅ Direct proof |
| Context management + session state | AgentProbe: multi-step agent runs with state preservation across tool calls | ✅ Direct proof |
| Agent architecture + platform primitives | AgentProbe: plan-execute-react loop, 3-agent runtime, 15-endpoint FastAPI backend as platform layer | ✅ Direct proof |
| Python | 8+ years production Python | ✅ Exceeds |
| TypeScript + React | Skills listed; Entrata JS/TS; AgentProbe React dashboard | ✅ Present (not primary) |
| Azure OpenAI | Azure in CV; AgentProbe OpenAI API integration | ✅ Adjacent |
| 8+ years SWE + staff track record | 8+ years (meets); technical leadership via code reviews, debugging tools, secure standards | ✅ Meets |
| Multi-model/multi-provider AI in production | AgentProbe: exact use case | ✅ Direct proof |
| Legal domain | New — same gap as Agents role; agent patterns transfer; AI on FHIR shows domain-specific AI | ⚠️ Same mitigation |
| H-1B | a16z/Sequoia-backed — same situation as Agents role; verify | ⚠️ Confirm |
| Concurrent Harvey application (#58 Agents) | Already applied to Sr SWE Agents same day — check if Harvey allows multiple concurrent apps | ⚠️ Verify policy |

**Gaps:**
- Legal domain (same as Agents role — agent patterns transfer regardless of domain)
- TypeScript not primary language in portfolio
- Staff cross-team leadership is inferred from Entrata breadth; no explicit multi-team leadership at a tech company
- Already applied to Harvey Sr SWE Agents (#58) — confirm Harvey allows concurrent applications before submitting

---

## C) Score Rationale

4.2/5 — AI Platform is arguably a better technical match than Agents role. Model routing + eval infrastructure + context management = AgentProbe built exactly these systems. The "platform that teams build on" framing maps perfectly to AgentProbe's 15-endpoint FastAPI backend serving as a foundation layer. Comp $238–290K base is strong. H-1B same situation as Agents role. Concurrent Harvey application needs a quick check before submitting.

---

## Machine Summary

```yaml
report_num: 056
company: Harvey AI
role: Staff Software Engineer, AI Platform
date: 2026-06-11
score: 4.2
archetype: AI Platform / LLMOps
legitimacy: High Confidence
location: SF or NY — 3+ days/week in-office
comp_range: "$238,000–$290,000 base + equity (~$336K median total)"
visa_risk: medium (a16z/Sequoia-backed — same as Agents role; verify H-1B)
key_gaps:
  - Legal domain (same as Agents role — patterns transfer)
  - Concurrent Harvey application — confirm policy before submitting
  - TypeScript not primary in portfolio
key_strengths:
  - AgentProbe = exact proof for model routing, eval infra, context management, agent architecture
  - Python 8+ years production
  - Platform-builder framing (FastAPI backend as foundation layer)
  - Comp $238-290K base strong
  - Location open (SF/NY hybrid fine)
location_risk: low — user open to any location
recommend: strong apply — verify Harvey concurrent application policy first
```
