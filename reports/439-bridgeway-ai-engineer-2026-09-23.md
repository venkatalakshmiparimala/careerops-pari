# Evaluation: Bridgeway — AI Engineer

**Date:** 2026-09-23
**URL:** (pasted JD)
**Archetype:** AI Platform / LLMOps + Agentic / Automation (hybrid)
**Score:** 4.4/5
**Legitimacy:** High Confidence
**PDF:** ✅ output/cv-venkata-lakshmi-parimala-pasupuleti-bridgeway-2026-09-23.pdf

---

## A) Role Summary

| Dimension | Details |
|-----------|---------|
| **Archetype** | AI Platform / LLMOps + Agentic / Automation (both primary) |
| **Domain** | Fund office / benefits fund administration — HIPAA + SOC 2 + NIST regulated |
| **Function** | Build production LLM services, RAG pipelines, eval frameworks, agentic capabilities in regulated multi-tenant SaaS |
| **Seniority** | Mid-level (3–5 years experience target) |
| **Work model** | Remote — East Coast preferred ✅ (Virginia qualifies perfectly) |
| **Comp** | Not disclosed — 3–5 yr target suggests $110K–$145K range |
| **Sponsorship** | Not stated — flag in screening |
| **TL;DR** | HIPAA + PHI + multi-tenant SaaS + RAG + eval frameworks = direct Entrata + AI on FHIR + AgentProbe match. East Coast remote ✅. Sponsorship unconfirmed — ask early. Score 4.4/5 — strong match, borderline threshold. |

---

## B) Match with CV

| JD Requirement | CV Evidence | Match |
|---|---|---|
| LLM orchestration + agent and tool-using systems | LeaseI: 8-agent LangGraph StateGraph with conditional routing, HITL escalation, tool boundaries; Magizhs: agentic LangGraph stateful graph | ✅ Direct match |
| Evaluation frameworks | AgentProbe: 5-metric eval engine, CI-integrated regression harness, LLM-as-judge, pass@k harness, golden datasets | ✅ AgentProbe IS this |
| RAG + retrieval-backed features | LeaseI: hybrid TF-IDF + semantic RAG layer, section-aware chunking, citation grounding, retrieval evaluation | ✅ Direct match |
| Enterprise data architectures (Databricks, Azure/AWS) | Azure Databricks in cv.md; AWS S3 + Glue + RDS at Entrata; Azure Data Factory + ADLS in skills | ✅ |
| HIPAA + PHI handling + audit logging | AI on FHIR: HIPAA-compliant RBAC across medical records; Entrata: 100% PHI compliance on AWS S3 migration, Libsodium-encrypted pipelines, zero security incidents | ✅ Strong signal |
| Multi-tenant SaaS data isolation | Entrata 7 years: multi-tenant PostgreSQL schemas, data isolation across tenant records, schema-level separation for financial + eligibility + document workflows | ✅ Perfect fit |
| SOC 2 + NIST compliance context | Entrata is a production SaaS with compliance requirements; PHI + regulated financial data; LeaseI: deterministic audit trail for every decision | ✅ Adjacent (add to skills) |
| Python production services + pipelines | 8+ years Python at Entrata + GMU + projects | ✅ |
| CI/CD + IaC + MLOps | GitHub Actions CI/CD; Terraform + Pulumi in cv.md; LLMOps in skills | ✅ |
| Prompt injection defenses + LLM security controls | Guardrails in cv.md; LeaseI: safety boundary enforced in code (eligibility never resolved by AI); output validation layer | ✅ |
| Semantic search + summarization + anomaly narration | Semantic Search + ChromaDB in skills; Isolation Forest anomaly detection at GMU; summarization via LLM in LeaseI | ✅ |
| Cost management for AI systems | AgentProbe: latency + token efficiency as first-class metrics; model routing across OpenAI/Anthropic/Groq/Ollama for cost optimization | ✅ |
| **Preferred: regulated industry, HIPAA/SOC 2/NIST** | Entrata (PHI, financial compliance); AI on FHIR (HIPAA); LeaseI (compliance enforcement in code) | ✅ Strong preferred match |
| **Preferred: multi-tenant SaaS identity/access patterns** | Entrata multi-tenant, 100K+ MAU, per-tenant data isolation across eligibility + financial schemas | ✅ |
| Fund office / alternative investments domain | No direct fund/investment experience | ⚠️ Domain gap (AI skills transfer) |
| Sponsorship | Not stated | ⚠️ Unconfirmed — ask in screening |

**No hard gaps on required qualifications.** Domain gap (fund office) is in the implementation layer, not the AI skills layer — the JD explicitly separates "data team owns pipeline operation" from "AI engineer builds the LLM/RAG features."

---

## C) Level and Strategy

| Dimension | Finding |
|-----------|---------|
| Title | AI Engineer (no level specified) |
| Experience target | 3–5 years — she has 8+; overqualified by numbers but role is hands-on building, not architecture leadership |
| Her fit | Senior-equivalent hands-on builder; 8yr SWE depth with 2yr AI focus. Will exceed JD bar. |
| Risk | Budget may be calibrated to 3–5yr comp. Salary may be lower than her $110K+ target — but comp floor removed. |
| Strategy | Lead with regulated-industry AI: "I've built RAG and agentic systems in HIPAA-regulated, multi-tenant SaaS — at Entrata for 7 years and in my own LeaseI project. Compliance enforcement in code, not just in prompts, is how I build." |

---

## D) Comp and Demand

| Metric | Data |
|--------|------|
| JD range | Not disclosed |
| Estimated range | $110K–$145K (AI Engineer, East Coast, 3–5yr target; she may be able to negotiate above due to 8yr depth) |
| Score | **3.5/5** — unknown, estimated mid-range |
| Equity | Not mentioned (likely small company — fund admin space) |

---

## E) Customization Plan

| # | Section | Proposed change |
|---|---------|-----------------|
| 1 | Summary | Lead with HIPAA/PHI compliance + multi-tenant SaaS + production RAG. "AI Engineer building LLM and retrieval systems in regulated, multi-tenant environments — HIPAA-compliant (AI on FHIR), 100% PHI compliance at Entrata (7yr multi-tenant SaaS), AgentProbe eval framework, LeaseI 8-agent LangGraph system with audit trail + HITL." |
| 2 | LeaseI | Emphasize: RAG pipeline, citation grounding, audit trail (every decision cited or flagged), compliance enforcement in code, HITL for regulated decisions |
| 3 | AgentProbe | Lead with: eval framework, 5-metric engine, CI-integrated regression harness, cost controls (token efficiency metrics), model routing |
| 4 | AI on FHIR | Lead with: HIPAA-compliant RBAC, PHI across structured medical records — maps directly to their HIPAA/PHI requirement |
| 5 | Entrata | Lead with: multi-tenant data isolation, PHI compliance (100%), regulated financial data, schema design across 100K+ MAU |
| 6 | Skills | Push: HIPAA, SOC 2, NIST, PHI Compliance, Audit Logging, Multi-Tenant Data Isolation, Prompt Injection Defense to top of AI skills |

---

## F) Interview Plan

| # | JD Requirement | Story |
|---|----------------|-------|
| 1 | Build production LLM services in regulated environment | LeaseI: HIPAA-adjacent compliance system — every AI decision is either cited to exact source clause or escalated to human. Enforcement in code, not prompt. |
| 2 | RAG evaluation + retrieval quality feedback loops | AgentProbe: 5-metric eval engine evaluated LeaseI across 1,240 lease PDFs — groundedness, retrieval quality, hallucination rate all first-class metrics. Feedback loop: eval reveals gap → prompt/chunking change → re-run harness. |
| 3 | Multi-tenant SaaS data isolation + PHI patterns | Entrata 7yr: per-tenant schema isolation for eligibility + financial + document workflows; 100% PHI compliance on AWS S3 migration with Libsodium-encrypted pipelines; zero security incidents. |
| 4 | Prompt injection + LLM security controls | LeaseI: tenant self-service agent has a code-enforced safety boundary — eligibility questions never resolved by AI, always routed to staff. "I don't trust prompts for safety boundaries — I trust code." |
| 5 | Cost management + model routing | AgentProbe LLM Router: routes OpenAI/Anthropic/Groq/Ollama dynamically; latency + token efficiency are eval metrics, not afterthoughts. Ollama for dev = zero cost. |
| 6 | Lakehouse / analytics integration (Databricks/Azure) | Azure Databricks + Azure Data Factory + ADLS in production stack; ETL pipelines at Entrata feeding financial + eligibility reporting layers. |
| 7 | On-call + incident response for AI systems | Owned RabbitMQ async system through production incidents at Entrata — retry logic, idempotency, root cause analysis and post-incident remediation for annual rent-schedule cycles. |

**Recommended angle:** "I've built the AI layer AND the eval harness on top of a regulated system with HIPAA, PHI, and multi-tenant data isolation. That combination is exactly what your JD asks for — not just 'builds RAG' but 'builds RAG where a compliance mistake has real consequences.'"

**Red-flag questions:**
- "You're overqualified for 3–5yr target" → "I'm a hands-on builder first — 8 years of production engineering means I ship faster, not that I want to manage. The JD is about building; that's exactly what I do."
- "No fund office experience" → "The AI layer is my contribution — RAG over domain documents, retrieval quality eval, LLM safety controls. Your data team owns the fund-specific pipelines. I bring the AI implementation expertise in a regulated, multi-tenant environment — that's the same problem I've solved before, different domain documents."
- "Sponsorship?" → Ask in screen. East Coast remote match reduces cost concerns.

---

## G) Posting Legitimacy

| Signal | Finding | Weight |
|--------|---------|--------|
| Company | Bridgeway — specific JD with team context, stack named, compliance context specific | Positive |
| Salary | Not disclosed | Neutral |
| Tech specificity | Databricks, Azure, LangGraph-level orchestration, HIPAA/SOC 2/NIST, PHI boundary patterns — real technical content | Positive |
| Remote/location | Remote, East Coast preference — clear policy | Positive |
| JD quality | Well-structured, specific responsibilities, realistic requirements | Positive |
| Sponsorship | Not stated — verify | Unknown |

**Assessment: High Confidence** — Real opening with specific tech and compliance context.

---

## Verdict

**4.4/5 — Below 4.5 threshold but strong match. Apply with user approval.**

Every required technical qualification maps to AgentProbe, LeaseI, or Entrata:
- LLM orchestration + agentic systems ✅ (LeaseI 8-agent LangGraph)
- Evaluation frameworks ✅ (AgentProbe — literally this)
- HIPAA + PHI + multi-tenant ✅ (Entrata + AI on FHIR)
- RAG with enterprise data ✅ (LeaseI + Azure Databricks)
- Prompt injection + safety controls ✅ (code-enforced boundaries)

Only drag: sponsorship unconfirmed + fund office domain gap (AI layer transfers, domain doesn't matter for her role) + comp unknown.

**Recommended:** Confirm sponsorship in first contact. If confirmed, this is a strong apply.

---

## Keywords extracted

LLM orchestration, evaluation frameworks, RAG, retrieval, agent, tool-using, HIPAA, PHI, SOC 2, NIST, multi-tenant, data isolation, Databricks, Azure, lakehouse, Python, prompt injection, audit logging, CI/CD, MLOps, LLMOps, cost management, model routing, FastAPI, LangGraph, regulated industry, production AI, semantic search, chunking, embeddings, observability

## Machine Summary
```yaml
company: Bridgeway
role: AI Engineer
score: 4.4
archetype: AI Platform/LLMOps + Agentic/Automation (both primary)
level: Mid (3-5yr target)
comp_range: "Not disclosed (~$110K-$145K estimated)"
location: Remote (East Coast preferred — Virginia qualifies)
sponsorship: Not stated — verify in screening
apply: Borderline (4.4 < 4.5) — strong match, recommend confirm sponsorship then apply
top_proof_points:
  - AgentProbe (eval framework = their exact requirement)
  - LeaseI (8-agent LangGraph + RAG + HITL + compliance enforcement in code)
  - Entrata 7yr multi-tenant SaaS + 100% PHI compliance (HIPAA/SOC 2 context)
  - AI on FHIR (HIPAA-compliant RBAC over PHI records)
key_gap:
  - Fund office / alternative investments domain (AI layer transfers; data team owns pipelines)
  - Sponsorship unconfirmed
```
