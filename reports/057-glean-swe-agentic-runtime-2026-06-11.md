# Evaluation: Glean — Software Engineer, Agentic Runtime

**Date:** 2026-06-11
**URL:** https://job-boards.greenhouse.io/gleanwork/jobs/4616929005
**Archetype:** Agentic / Automation + AI Platform / LLMOps
**Score:** 4.0/5
**Legitimacy:** High Confidence
**PDF:** output/cv-glean-swe-agentic-runtime-2026-06-11.pdf

---

## A) Role Summary

| Field | Detail |
|-------|--------|
| Archetype | Agentic / Automation + AI Platform — build the low-latency runtime powering all Glean agents and assistant at scale |
| Domain | Enterprise Work AI — search, assistant, agents across 100+ SaaS connectors |
| Function | Runtime engineering: multi-turn orchestration, tool calling, model routing, memory/state, streaming, safety |
| Seniority | Mid-level SWE (3+ years required) |
| Remote | Bay Area hybrid (Mountain View — 3–4 days/week in office) |
| Comp | $170,000–$265,000 annually + equity + benefits |
| TL;DR | Build the agent runtime core: session lifecycle, tool execution, model routing, streaming, observability, fault isolation — the foundation all Glean agents run on. |

---

## B) Match with CV

| JD Requirement | CV Match | Strength |
|----------------|----------|----------|
| Multi-turn orchestration | AgentProbe: 3-agent LangGraph system (Orchestrator, RAG Tracer, Auto Fix), multi-step state across tool calls | ✅ Direct proof |
| Tool calling + structured execution | AgentProbe: tool routing, function calling across LangGraph agent loop | ✅ Direct proof |
| Model routing / multi-provider LLM | AgentProbe: dynamic routing across Anthropic, OpenAI, Groq, Ollama by task + latency + capability | ✅ Direct proof |
| Memory / session state | AgentProbe: context + session state management across multi-step agent runs | ✅ Direct proof |
| Observability (tracing, metrics, dashboards) | AgentProbe: 15-endpoint FastAPI backend + React observability dashboard + CI/CD eval gates | ✅ Direct proof |
| Production distributed systems / cloud | Entrata: AWS S3/EC2/RDS/Glue, 1.6M records, 100K+ MAU, 99.5% uptime | ✅ Strong |
| Python | 8+ years production Python (Entrata 2017–2024) | ✅ Exceeds 3+ years |
| Docker / containerization | Entrata: Docker containerization for 30%+ of microservices | ✅ Present |
| LLM integrations (OpenAI, Anthropic) | AgentProbe: live API integration with Anthropic + OpenAI + Groq | ✅ Direct proof |
| 3+ years SWE | 8+ years (Entrata 2017–2024 + GMU TA) | ✅ Exceeds |
| Kubernetes | Not explicitly mentioned in CV (Docker yes, K8s not) | ⚠️ Gap |
| Kafka / Pub/Sub / streaming systems | RabbitMQ at Entrata (adjacent); gRPC/WebSockets not mentioned | ⚠️ Adjacent |
| Redis / caching | Not mentioned | ⚠️ Gap |

**Gaps:**
- Kubernetes: Docker strong, K8s not explicit
- Streaming infra (Kafka, gRPC): adjacent via RabbitMQ/microservices but not direct
- Redis: not in stack
- Bay Area hybrid 3–4 days/week = relocation from Virginia

---

## C) Score Rationale

4.0/5 — Core agent runtime work (multi-turn orchestration, tool calling, model routing, memory/state) maps exactly to AgentProbe. Python exceeds the requirement. Comp $170–265K is well above target. Gaps in K8s, Redis, Kafka are secondary requirements ("familiarity a plus") rather than hard blockers. Location requires Bay Area relocation; user open to any US location. Visa sponsorship not explicitly stated — verify early (Glean is 1000+ employees, likely sponsors).

---

## Machine Summary

```yaml
report_num: 057
company: Glean
role: Software Engineer, Agentic Runtime
date: 2026-06-11
score: 4.0
archetype: Agentic / Automation + AI Platform / LLMOps
legitimacy: High Confidence
location: Mountain View, CA — hybrid 3–4 days/week
comp_range: "$170,000–$265,000 annually + equity"
visa_risk: medium (1000+ employees likely sponsors but not stated — verify)
key_gaps:
  - Kubernetes not explicitly in CV
  - Kafka/Redis not in stack (secondary requirements)
  - Bay Area relocation required
key_strengths:
  - AgentProbe = exact proof for multi-turn orchestration, tool calling, model routing, memory/state
  - Python 8+ years (exceeds 3+ required)
  - Observability: FastAPI backend + React dashboard + CI/CD eval gates
  - Comp $170-265K well above target
  - Glean is recognized AI company (Fast Company Top 10, 1000+ employees)
location_risk: medium — relocation to Bay Area required
recommend: apply — agent runtime is exact AgentProbe match; verify visa sponsorship first
```
