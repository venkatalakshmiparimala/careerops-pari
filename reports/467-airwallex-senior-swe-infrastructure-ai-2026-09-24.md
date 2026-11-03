# Evaluation: Airwallex — Senior Software Engineer, Infrastructure AI

**Date:** 2026-09-24
**URL:** (pasted JD)
**Archetype:** AI Platform / LLMOps + Infrastructure AI Engineer
**Score:** 4.4/5
**Legitimacy:** High Confidence
**PDF:** ✅ output/cv-venkata-lakshmi-parimala-pasupuleti-airwallex-infra-ai-swe-2026-09-24.pdf

---

## A) Role Summary

| Dimension | Details |
|-----------|---------|
| **Archetype** | Infrastructure AI Engineer — building autonomous SRE/DevOps/DBA agents on internal agent platform |
| **Domain** | Airwallex — $11B global payments fintech; 250K+ business customers (Brex, Navan, Qantas, SHEIN); backed by Visa, Mastercard, Sequoia, T. Rowe Price |
| **Function** | Build goal-oriented infrastructure AI agents on "Quartermaster" (internal platform) that automate SRE/DevOps/DBA workflows; agent architecture, safety guardrails, HITL escalation, evaluation frameworks; interact with K8s, Terraform, AWS/GCP, databases, CI/CD |
| **Seniority** | 3+ years required; senior IC, ground-floor team |
| **Work model** | **Hybrid — Seattle, WA** (explicitly stated); relocation from Virginia required |
| **Comp** | Not disclosed — $11B unicorn fintech; estimated $180K–$250K+ |
| **Sponsorship** | Not stated — $11B valuation, 27 global offices, 2,300+ employees; high H-1B probability; verify in screen |
| **TL;DR** | JD states explicitly: "Hands-on experience building agentic AI systems — this is a core requirement, not a nice-to-have." That is Parimala's exact profile. LangGraph 8-agent LeaseI covers orchestration, tool-use, agent state, durable memory, HITL — every architectural element listed. AgentProbe covers the evaluation framework requirement ("define metrics, build evaluation frameworks to measure whether agents reliably achieve their goals"). Infrastructure stack (K8s, Terraform, Prometheus, Grafana, AWS) all covered. SRE domain gap mitigated: the JD explicitly says you partner with SRE/DevOps teams who provide the domain context — your job is to build the agents. Fintech threshold (FDE): 4.4/5 above 4.0 → **apply.** |

---

## B) Match with CV

| JD Requirement | CV Evidence | Match |
|---|---|---|
| 3+ years SWE | 8+ yrs | ✅ |
| **Python / Java / Kotlin** | **Python 8+ yrs; Java (Spring Boot); Kotlin in cv.md** | ✅ Primary |
| Go | Not in stack | ❌ Gap (Python/Java/Kotlin cover requirement) |
| AWS / GCP | AWS (S3, EC2, RDS, Lambda, Bedrock, SageMaker) + GCP/Vertex AI | ✅ |
| Kubernetes | K8s in cv.md | ✅ |
| Terraform | Terraform in cv.md | ✅ |
| CI/CD | GitHub Actions CI/CD; CI regression harness (AgentProbe) | ✅ |
| **"Core requirement": Agentic AI — planning, reasoning, tool-use, agent state, memory** | **LeaseI: 8-agent LangGraph (orchestration runtime, tool calling, durable state management, memory retrieval, conditional routing, HITL escalation)** | ✅ **Direct proof — stated core requirement** |
| **Agent orchestration frameworks (LangGraph, CrewAI, AutoGen)** | **LangGraph (primary); LangChain; LangSmith; MCP** | ✅ |
| **Evaluate and improve agent performance — metrics, eval frameworks** | **AgentProbe: task completion metrics, precision/recall/F1, CI regression harness, golden datasets, pass@k — exactly "build evaluation frameworks to measure whether agents reliably achieve their goals"** | ✅ **Direct proof** |
| **Safety guardrails + HITL escalation** | **Guardrails in cv.md; LeaseI HITL escalation when confidence too low; prompt injection defense, OWASP LLM Top 10** | ✅ |
| Observability (Prometheus, Grafana, Datadog) | Prometheus + Grafana + OpenTelemetry (40% debugging time reduction); OpenSearch/Elasticsearch | ✅ |
| Database knowledge (schema migrations, query optimization) | PostgreSQL 8yr; 200+ SQL optimizations; data modeling; stored procedure refactoring | ✅ |
| Cross-functional collaboration, global distributed teams | Entrata India team; GMU research; 120+ Agile sprints | ✅ |
| Production infrastructure ownership | Entrata: 99.5% uptime, 100K+ MAU, production incident ownership | ✅ |
| Comp: ~$180K–$250K est. | Undisclosed; $11B unicorn | ✅ |
| Location: Seattle hybrid | Virginia — relocation to Seattle required | ⚠️ |
| Sponsorship | Not stated — $11B global company; high probability | Likely ✅ |

---

## D) Comp and Demand

| Metric | Data |
|--------|------|
| Estimated | Airwallex senior SWE Seattle: ~$180K–$250K base + equity (unicorn fintech) |
| Score | **4.5/5** — undisclosed but unicorn fintech at this stage typically offers strong comp + equity |

---

## G) Posting Legitimacy

**Assessment: High Confidence** — Airwallex is real ($11B valuation, NYSE-listed investors, 250K+ customers including Brex/Navan/Qantas/SHEIN). "Quartermaster" internal agent platform is a specific authentic detail. Seattle hybrid location and anti-fraud notice both consistent with a legitimate large company posting.

---

## Machine Summary
```yaml
company: Airwallex
role: Senior Software Engineer, Infrastructure AI
score: 4.4
archetype: AI Platform / LLMOps + Infrastructure AI Engineer
level: 3+ yr req; senior IC; ground-floor team
comp_range: "~$180K-$250K base + equity (estimated, not disclosed)"
location: Hybrid — Seattle, WA; relocation from Virginia required
sponsorship: Not stated — $11B global fintech; high H-1B probability; verify in screen
apply: YES — 4.4/5; fintech (FDE) threshold 4.0+; agentic AI core match; startup-like within established unicorn
boost_applied: AgentProbe eval boost (+0.3); fintech/FDE classification (4.0+ apply threshold)
top_proof_points:
  - LeaseI 8-agent LangGraph = exact "agentic AI core requirement" (orchestration, tool-use, agent state, HITL escalation)
  - AgentProbe = exact "build evaluation frameworks for agent effectiveness" (metrics, CI regression, golden datasets)
  - Infrastructure stack: K8s + Terraform + Prometheus + Grafana + AWS/GCP + CI/CD
  - Safety guardrails, HITL, prompt injection defense, OWASP LLM Top 10
  - Production system ownership at scale (Entrata 99.5% uptime, 100K+ MAU)
key_gap:
  - Go language: not in stack (Python/Java/Kotlin cover requirement)
  - SRE domain: adjacent (production ownership) but not SRE-titled; mitigated by JD partnering model
  - Seattle hybrid: relocation from Virginia required
  - Sponsorship unconfirmed (likely; verify early)
```
