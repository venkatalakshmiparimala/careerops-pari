# Evaluation: IMO Health — Staff AI Engineer

**Date:** 2026-06-11
**URL:** https://jobs.lever.co/imo-online/6fd7edae-2cf1-4d24-8e1c-99ac967ce5df
**Archetype:** AI Platform / LLMOps + ML Engineer
**Score:** 4.0/5
**Legitimacy:** High Confidence
**PDF:** output/cv-imo-health-staff-ai-engineer-2026-06-11.pdf

---

## A) Role Summary

| Field | Detail |
|-------|--------|
| Archetype | AI Platform / LLMOps — own full ML lifecycle, integrate LLMs/agentic systems into clinical products |
| Domain | Healthcare AI — clinical terminology, coding, NLP on unstructured clinical data |
| Function | Build + MLOps (production ML systems, CI/CD, monitoring, LLM integration) |
| Seniority | Staff IC (8+ years required) |
| Remote | Remote available OR hybrid 3d/wk (Chicago/Houston/Roseville) |
| Comp | $170,000–$250,000 |
| TL;DR | Own production AI systems end-to-end: train → deploy → monitor → retrain. Integrate LLMs, GenAI, and agentic systems into IMO clinical products. Healthcare NLP (FHIR, clinical coding, unstructured data) is the domain. |

---

## B) Match with CV

| JD Requirement | CV Match | Strength |
|----------------|----------|----------|
| 8+ years SWE / AI/ML engineering | 8+ years (Entrata 2017–2024 + GMU TA) | ✅ Meets |
| Expert Python production engineering | Python primary language; 1.6M record automation at Entrata | ✅ Direct proof |
| LLMs + GenAI + agentic systems in production | AgentProbe: 3-agent LangGraph system, multi-provider LLM routing | ✅ Direct proof |
| NLP (tokenization, embeddings, classification) | AI on FHIR: BERT, spaCy, embeddings, EN/ES NLP | ✅ Direct proof |
| Healthcare exposure (explicit plus) | AI on FHIR: FHIR APIs, HIPAA-compliant RBAC, clinical record queries | ✅ Rare differentiator |
| Vector databases + embedding-based search | AgentProbe: ChromaDB + embeddings + retrieval scoring | ✅ Direct proof |
| CI/CD for ML systems | AgentProbe: GitHub Actions CI/CD with eval regression gates | ✅ Direct proof |
| Docker + cloud (AWS/Azure) | Entrata: Docker containerization (30%+ of modules); AWS S3/EC2/RDS/Glue | ✅ Direct proof |
| Hugging Face / PyTorch / TensorFlow | AI on FHIR: BERT/spaCy; cv.md lists PyTorch, Hugging Face | ✅ Direct proof |
| Build monitoring + observability for ML | AgentProbe: 15-endpoint FastAPI + React dashboard, per-run eval scoring | ✅ Adjacent |
| MLOps tools (MLflow, SageMaker, Kubeflow) | Not in CV — standard MLOps toolchain gap | ⚠️ Gap |
| Kubernetes | Not in CV (Docker yes, K8s no) | ⚠️ Gap |
| Production ML retraining / model lifecycle | AgentProbe eval loop; no explicit retraining pipeline experience | ⚠️ Adjacent |
| H-1B | Healthcare AI specialist firm ~500-1000 employees; verify sponsorship | ⚠️ Confirm |

**Gaps:**
- **MLOps toolchain** (MLflow, SageMaker, Kubeflow) — not in CV; addressable since AgentProbe shows the same discipline (CI/CD eval gates = same outcome)
- **Kubernetes** — Docker yes, K8s no; common gap for Python-first engineers
- **Production model retraining** — AgentProbe shows eval-driven quality loops, not classic retrain pipelines

**Differentiator:**
- **AI on FHIR** — clinical NLP with FHIR APIs, HIPAA-compliant RBAC, BERT/spaCy on medical records. JD explicitly calls healthcare exposure a "plus." Most candidates won't have this.

---

## C) Score Rationale

4.0/5 — Python + LLMs + agentic systems + healthcare NLP = genuine stack overlap across two proof points (AgentProbe + AI on FHIR). The healthcare AI on FHIR differentiator is rare and directly relevant to IMO's clinical AI product. MLflow/Kubeflow/K8s gaps are real but not blocking — CI/CD eval pipelines + Docker + AWS cover the production engineering discipline. Remote option available. Comp $170–250K strong. H-1B needs verification.

---

## Machine Summary

```yaml
report_num: 054
company: IMO Health
role: Staff AI Engineer
date: 2026-06-11
score: 4.0
archetype: AI Platform / LLMOps + ML Engineer
legitimacy: High Confidence
location: Remote available OR hybrid 3d/wk (Chicago/Houston/Roseville CA)
comp_range: "$170,000–$250,000"
visa_risk: medium (healthcare AI specialist firm — verify H-1B in screen)
key_gaps:
  - MLOps toolchain (MLflow, SageMaker, Kubeflow) — not in CV
  - Kubernetes — Docker yes, K8s no
  - Production model retraining cycle
  - H-1B: verify early
key_strengths:
  - AI on FHIR = rare healthcare NLP proof point (JD explicitly calls this a plus)
  - AgentProbe = direct proof for LLMs, agentic systems, vector search, CI/CD eval
  - Python 8+ years production
  - BERT/spaCy/embeddings from AI on FHIR + AgentProbe
  - Docker + AWS from Entrata
  - Healthcare domain match few candidates can claim
location_risk: low — remote available
recommend: strong apply — healthcare AI on FHIR differentiator is rare; lead with it
```
