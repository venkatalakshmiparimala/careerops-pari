# Evaluation: Capgemini -- Forward Deployed Engineer (FDE), Applied AI

**Date:** 2026-09-21
**URL:** (pasted directly, no URL provided)
**Archetype:** Forward Deployed Engineer / AI Delivery (Consulting)
**Score:** 3.2/5
**Legitimacy:** High Confidence
**PDF:** N/A (below 4.0 FDE threshold)
**Location:** Atlanta, GA -- Hybrid
**Comp:** $82,082 -- $193,440 base

---

## A) Role Summary

| Dimension | Detail |
|-----------|--------|
| Archetype | FDE -- Applied AI delivery at client sites; conversational AI + agentic frameworks; prototype-to-production |
| Domain | Capgemini consulting -- delivering AI solutions inside enterprise client environments |
| Function | Lead agentic AI development; build multi-agent systems; integrate with enterprise platforms; develop eval pipelines + observability; client-facing delivery |
| Seniority | "Forward Deployed Engineer" (FDE) -- her target archetype; consulting firm title, not tech SWE IC ladder |
| Location | Atlanta GA -- hybrid; not penalized per profile |
| Company | Capgemini -- global consulting/tech firm, 340,000 employees; major H-1B sponsor |
| TL;DR | FDE = target archetype. Agentic AI match is strong (AgentProbe + LeaseI). Three simultaneous required gaps: (1) GCP (required -- she has AWS); (2) Terraform/IaC (required -- not in stack); (3) Client-facing consulting/PS delivery (same gap as Salesforce FDE #386). Score 3.2 -- below 4.0 FDE threshold. SKIP. |

---

## B) Match with CV

| JD Requirement | CV Match | Strength |
|----------------|----------|----------|
| Python | Python 9yr primary | ✅ Strong |
| Agentic AI, multi-agent systems, orchestration | LangGraph (8-agent LeaseI); AgentProbe (multi-provider routing) | ✅ Strong |
| RAG, vector databases, knowledge base integrations | AgentProbe: ChromaDB; LeaseI: TF-IDF RAG | ✅ Present |
| LLM evaluation pipelines + observability | AgentProbe: 5-metric eval, CI gate, agent tracing | ✅ Strong |
| Full-stack + enterprise API integrations | FastAPI, React, TypeScript; third-party integrations at Entrata | ✅ Present |
| Microservices, security, system integrations | Docker, K8s, RabbitMQ; HIPAA-compliant systems | ✅ Present |
| ReAct / self-reflection / agent orchestration patterns | LangGraph conditional routing; HITL escalation | ✅ Present (preferred) |
| M.S. CS/AI related | M.S. Data Analytics Engineering (GPA 3.87) | ✅ Present (preferred) |
| **GCP (required)** | **AWS primary; Azure secondary; GCP not in stack** | ❌ Required gap |
| **Terraform / IaC (required)** | Not in stack | ❌ Required gap |
| **Client-facing consulting / PS delivery** | Internal SaaS (Entrata) + short external engagement (Magizhs); not formal consulting track | ❌ Gap (same concern as Salesforce FDE #386) |
| MLOps (monitoring, logging, observability) | AgentProbe CI gate + tracing; limited formal MLOps tooling | ⚠️ Partial |
| H-1B sponsorship | Capgemini is one of the top H-1B sponsors in the US | ✅ Safe |

---

## C) Why This Doesn't Clear 4.0

**Three simultaneous required gaps.** GCP, Terraform, and client-facing consulting experience are all required (not preferred). GCP and Terraform appear in the "Required Skills" section explicitly. Client-facing delivery is the core function of an FDE at a consulting firm.

**GCP gap is real.** AWS and GCP are conceptually transferable but operationally different. "Strong experience with GCP and cloud-native architecture" at a consulting firm means deploying Vertex AI, Cloud Run, GKE, BigQuery -- none of which she's used in production.

**Terraform gap is concrete.** IaC is in the required skills list. Not the same as having Docker/K8s experience.

**Same client-facing concern as Salesforce FDE (#386).** Capgemini is a consulting firm -- every engagement is a client deployment. The FDE role is inherently consulting delivery. Her background is internal SaaS product engineering.

**What's genuinely strong.** Python/agentic AI/RAG/LLM eval match is excellent. If GCP and Terraform were swapped for AWS and she had consulting experience, this would score 4.2+.

---

## D) Comp and Demand

| Source | Range | Notes |
|--------|-------|-------|
| Disclosed | $82,082 -- $193,440 base | Wide range; typical for consulting tiers |
| H-1B | Capgemini = top 5 US H-1B sponsor | ✅ Safe, no issue |
| Location | Atlanta GA hybrid | Not penalized |

---

## G) Posting Legitimacy

**High Confidence.** Capgemini is a verifiable global company (340K employees). Detailed JD with specific technical requirements. Comp range disclosed per transparency law. No ghost signals.

---

## Recommendation: SKIP (3.2/5 -- below 4.0 FDE threshold)

Three required gaps simultaneously: GCP, Terraform, and client-facing consulting delivery.

---

## Machine Summary

```yaml
report: 395
company: Capgemini
role: Forward Deployed Engineer -- Applied AI
date: 2026-09-21
score: 3.2
archetype: Forward Deployed Engineer / AI Delivery (Consulting)
legitimacy: High Confidence
url: null
status: SKIP
gaps:
  - GCP (required -- she has AWS)
  - Terraform / IaC (required -- not in stack)
  - Client-facing consulting / PS delivery (required for consulting FDE)
strengths:
  - Python/agentic AI/RAG/LLM eval: strong
  - AgentProbe + LeaseI = direct proof points for AI delivery
  - FDE target archetype
h1b: Capgemini top US H-1B sponsor -- safe
comp_range: $82,082--$193,440
location: Atlanta GA hybrid (not penalized)
```
