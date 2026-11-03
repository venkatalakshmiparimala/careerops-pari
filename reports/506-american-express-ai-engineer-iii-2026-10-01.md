# Evaluation: American Express — AI Engineer III (Agentic AI)

**Date:** 2026-10-01
**URL:** https://www.linkedin.com/jobs/view/american-express-ai-engineer-iii
**Archetype:** Agentic / Automation + AI Platform / LLMOps
**Score:** 4.3/5
**Legitimacy:** High Confidence
**PDF:** output/506-american-express-ai-engineer-iii-2026-10-01.pdf

---

## A) Role Summary

| Attribute | Detail |
|---|---|
| **Archetype** | Agentic AI Engineer + LLM Platform |
| **Domain** | Financial Services — Enterprise Data & AI |
| **Function** | Build production agentic AI systems, RAG pipelines, LLM services, evaluation/monitoring tooling |
| **Seniority** | Engineer III / Mid-level (4+ years) |
| **Location** | Sunrise, FL — Onsite |
| **Comp** | Not disclosed (Amex Sr AI Engineer II range: ~$140–200K) |
| **Sponsorship** | Case by case |

---

## B) Match Analysis

### Strong Fits
- **Agentic AI building:** LeaseI = 8-agent LangGraph system with durable state, tool use, conditional routing, HITL — exactly "intelligent adaptive systems that plan, reason, and act across complex workflows"
- **RAG pipelines:** LeaseI hybrid search (TF-IDF + semantic reranking), OCR ingestion, citation grounding; AgentProbe RAG eval engine
- **LLM evaluation / monitoring tooling:** AgentProbe is directly what they describe — 5-metric eval engine, CI regression harness, golden datasets; this is the "contributing to shared AI infrastructure such as evaluation or monitoring tooling" bullet verbatim
- **Python:** 8+ years production Python
- **Regulated environment:** 7 years HUD/LIHTC compliance at Entrata (zero violations, PHI-encrypted pipelines) = financial services analog
- **Open-source contributions:** AgentProbe = preferred qual hit
- **AI-assisted development:** Claude Code daily use + AgentProbe as dev-loop eval tool
- **Cloud:** AWS (S3, EC2, RDS, Lambda) + GCP familiarity + Azure OpenAI

### Gaps
- **Go:** Listed alongside Python/TS; not a hard requirement; Python covers the must-haves
- **Kafka:** Event-driven experience is RabbitMQ-based; functionally equivalent but Kafka not production-used
- **gRPC:** Listed as a service type; REST covered, gRPC is a gap
- **Financial services domain:** Entrata = regulated housing (HUD/LIHTC), not banking — strong analog but not direct fintech

### Sponsorship Risk
- "Case by case" = not guaranteed; Amex is a known H-1B sponsor historically but this specific role has no commitment

---

## C) Score Breakdown

| Dimension | Score | Notes |
|---|---|---|
| Role fit | 4.5 | Agentic AI + RAG + eval tooling = direct stack match; LeaseI + AgentProbe are the proof points |
| Domain | 3.8 | Fintech/regulated domain gap offset by 7yr HUD compliance analog |
| Location | 3.5 | Onsite Sunrise FL; user open to any US location but requires relocation |
| Comp | 4.0 | Undisclosed but Amex AI Engineer comp typically $140–190K |
| Sponsorship | 3.5 | Case by case — risk factor |
| **Weighted** | **4.3** | Apply |

---

## D) Differentiator Positioning

**Lead with:** AgentProbe as their "evaluation or monitoring tooling" analog — exact same scope. Then LeaseI as production agentic system evidence. Then Entrata regulated-env credibility.

**Frame Entrata as:** "regulated compliance environment (HUD/LIHTC) requiring the same auditability, explainability, and reliability standards as financial services — zero violations, zero security incidents across 7 years."

**Frame AgentProbe as:** "CI-integrated LLM evaluation toolkit with golden datasets and LLM-as-judge scoring — the kind of evaluation infrastructure that lets a team maintain production AI quality over time without breaking."

---

## E) Interview Story Bank

**"Tell me about a production AI system you've built"**
LeaseI: 8-agent LangGraph, durable state, HITL escalation, CI regression harness, 93.6% precision at 1,240 test cases. Designed so LLMs reason but deterministic/human logic makes every regulated compliance call.

**"How do you ensure AI systems are reliable and auditable?"**
Two angles: (1) LeaseI — every agent decision audit-logged, citation-grounded, HITL-gated when confidence below threshold; (2) AgentProbe — CI regression harness with LLM-as-judge scoring that catches degradations before they ship.

**"Experience in regulated environments?"**
7 years owning HUD/LIHTC compliance pipelines at Entrata — a wrong income-limit import triggers regulatory corrections for thousands of residents. Same auditability, explainability, and zero-tolerance-for-errors mindset as financial services.

---

## F) Recommendation

**Apply.** Score 4.3. Strongest proof points: AgentProbe (direct match for eval/monitoring tooling) + LeaseI (production agentic system with HITL + CI regression). Regulated environment experience covers the fintech gap.

Sponsorship risk is real — confirm during screening. Onsite FL requires relocation planning.

---

## G) Posting Legitimacy

**Tier: High Confidence** — American Express is a major enterprise, active Amex Tech hiring page. Application window closes 10/28/2026 per JD.

---

## Machine Summary

```yaml
company: American Express
role: AI Engineer III
archetype: agentic_ai_llmops
score: 4.3
apply: true
location: Sunrise, FL
onsite: true
sponsorship: case_by_case
comp_disclosed: false
key_match: leaseI_agentic + agentprobe_eval_tooling + regulated_env
gaps: [go, kafka, grpc, fintech_domain]
report: 506-american-express-ai-engineer-iii-2026-10-01.md
```
