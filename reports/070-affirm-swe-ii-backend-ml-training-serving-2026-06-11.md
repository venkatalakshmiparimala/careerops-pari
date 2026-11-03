# Evaluation: Affirm — Software Engineer II, Backend (ML Training & Serving)

**Date:** 2026-06-11
**URL:** https://job-boards.greenhouse.io/affirm/jobs/7762568003
**Archetype:** ML Engineer / Backend Platform
**Score:** 3.7/5
**Legitimacy:** High Confidence
**PDF:** ❌

---

## A) Role Summary

| Field | Detail |
|-------|--------|
| Archetype | ML Engineer / Backend Platform — build distributed training + serving infrastructure |
| Domain | Fintech ML infrastructure (underwriting, fraud, servicing, personalization) |
| Function | Build systems enabling model training pipelines and model serving at scale |
| Seniority | SWE II — 1.5+ years required |
| Remote | Remote US |
| Comp | $142K–$192K base (most US states) / $160K–$210K (CA, WA, NY, NJ, CT) + equity + benefits |
| TL;DR | Backend platform engineering for ML infra at Affirm. Strong Python/AWS match, but core is training/serving platform — adjacent to, not direct overlap with, Parimala's AI application stack. |

---

## B) Match with CV

| JD Requirement | CV Match | Strength |
|----------------|----------|----------|
| Python proficiency | 8+ years production (Entrata + AgentProbe) | ✅ Exceeds |
| Backend systems design | 20+ full-stack modules, 100K+ MAU at Entrata | ✅ Direct |
| AWS | S3, EC2, RDS, Glue at Entrata (PHI compliance, zero incidents) | ✅ Direct |
| MySQL / relational databases | PostgreSQL + MySQL, 200+ queries tuned, 30% perf gain | ✅ Direct |
| Distributed systems | Microservices, RabbitMQ, Docker (50% execution time cut) | ✅ Solid |
| Kubernetes | Not explicitly in CV — Docker yes, K8s no | ❌ Gap |
| ML training infrastructure | PyTorch at Entrata for data transformation (1.6M records); not training pipeline orchestration | ⚠️ Adjacent |
| Model serving infrastructure | AgentProbe: LLM serving endpoints (application layer); not model serving platform layer | ⚠️ Adjacent |
| Team collaboration / on-call | Entrata 99.5% uptime, Agile delivery, peer code reviews | ✅ Present |
| H-1B sponsorship | Affirm publicly traded (AFRM), multi-state offices — likely strong sponsor | ✅ Likely |

**Key gap:** The role targets engineers who build the *platform* that trains and serves models — training orchestration, feature pipelines, inference serving infrastructure. Parimala's ML work is at the *application layer* (using LLMs and models via AgentProbe, not building the training/serving platform underneath them). Adjacent, not direct.

---

## C) Score Rationale

3.7/5 — Python/AWS/backend foundations are a strong match, and comp ($142–192K) actually exceeds the target range. The SWE II level means requirements are low relative to 8+ YOE. However, the core skill gap is real: ML training & serving infrastructure (K8s, training orchestration, model serving) is adjacent to but not the same as AI application development. Kubernetes gap is manageable but absent from CV. Recommended for a second-pass once 4.0+ queue is cleared.

---

## Machine Summary

```yaml
report_num: 070
company: Affirm
role: Software Engineer II, Backend (ML Training & Serving)
date: 2026-06-11
score: 3.7
archetype: ML Engineer / Backend Platform
legitimacy: High Confidence
location: Remote US
comp_range: "$142K–$192K base (other US) / $160K–$210K (CA/WA/NY/NJ/CT)"
visa_risk: low (Affirm publicly traded, multi-state — likely H-1B sponsor)
key_gaps:
  - Kubernetes not in CV
  - ML training/serving infrastructure (application layer vs. platform layer)
key_strengths:
  - Python 8+ years (far exceeds 1.5+ required)
  - AWS direct match (S3, EC2, RDS, Glue)
  - Backend/distributed systems at Entrata scale
  - Comp exceeds target range
  - Remote US, SWE II level accessible
recommend: second-pass — below 4.0 threshold; evaluate after 4.0+ queue cleared
```
