# Evaluation: dv01 — AI ML Engineer

**Date:** 2026-06-11
**URL:** https://job-boards.greenhouse.io/dv01/jobs/8191101002
**Archetype:** AI Platform / LLMOps (FinTech ML)
**Score:** 3.3/5
**Legitimacy:** High Confidence
**PDF:** pending

---

## A) Role Summary

| Field | Detail |
|-------|--------|
| Archetype | AI Platform / FinTech ML — Document Intelligence |
| Domain | Unstructured banking document parsing, ML model lifecycle, data ingestion, lending/capital markets |
| Function | Build (end-to-end ML systems + MLOps) |
| Seniority | Mid-Senior IC (3+ years) |
| Remote | New York, US — likely NYC-based, not remote |
| Comp | $145,000–$160,000 base |
| TL;DR | Build and maintain AI/ML solutions to extract insights from unstructured banking documents (loan docs, etc.). Own the full ML lifecycle: model development, MLOps, CI/CD, continuous training, performance tracking. Stack: Python, PyTorch, GCP, Databricks, MLflow, FastAPI, Docker/K8s. |

---

## ⚠️ LOCATION FLAG

LinkedIn lists this as **New York, United States** — likely NYC onsite or hybrid, not remote. Confirm remote/hybrid policy before investing application time. At $145-160K, NYC onsite is a significant relocation ask vs. remote alternatives at similar or higher comp.

---

## B) Match with CV

| JD Requirement | CV Match | Strength |
|----------------|----------|----------|
| Python 3+ years production | 8+ years Python at Entrata + AgentProbe | ✅ Exceeds |
| Gen AI 1+ year hands-on | AgentProbe: Anthropic, OpenAI, Groq, Ollama multi-provider | ✅ Direct proof |
| CI/CD + DevOps practices | GitHub Actions CI/CD + Docker in AgentProbe | ✅ Strong |
| FastAPI or Flask | AgentProbe: 15-endpoint FastAPI production backend | ✅ Direct proof |
| Docker containerization | AgentProbe + Entrata microservices | ✅ Strong |
| SQL proficiency | 8+ years PostgreSQL at Entrata + MS coursework | ✅ Strong |
| Fintech/lending domain | Fraud/risk targeting (Capital One, Intuit, Chime, Sezzle) + Entrata financial data | ✅ Adjacent |
| PyTorch/TensorFlow | CrashClarity (scikit-learn + R); Entrata income limits module (PyTorch + OpenAI) | ✅ Demonstrated |
| MLflow (eval + performance tracking) | Not in CV — AgentProbe has custom eval tracking but not MLflow | ⚠️ Gap |
| GCP (preferred) | AWS + Azure in CV; no GCP | ⚠️ Gap |
| Databricks / BigQuery | Not in CV | ⚠️ Gap |
| Kubernetes | Docker yes; K8s not in CV | ⚠️ Gap |
| Document parsing / NLP for banking docs | AI on FHIR: BERT + spaCy + NLP pipeline on medical records | ✅ Adjacent |
| Continuous training / MLOps | Not explicitly demonstrated | ⚠️ Soft gap |

**Gaps and mitigations:**
- **MLflow** — Specifically required for eval + performance tracking. AgentProbe has a custom eval engine doing the same thing (run-level metrics, regression detection, trend tracking) — frame as "I built the equivalent; MLflow is a tool ramp not a concept gap."
- **GCP** — AWS + Azure experience covers cloud fundamentals. GCP is "preferred" not required.
- **Databricks/BigQuery** — Big data platforms not in CV. AWS Glue (Spark-based) covers distributed data processing concepts.
- **K8s** — Docker is in CV; K8s is additive. Not a disqualifier.
- **NYC location** — This is the biggest risk. If the role requires onsite NYC, it blocks unless willing to relocate.

---

## C) Level and Strategy

**Level detected:** Mid-Senior IC. 3+ year bar with 1 year Gen AI is relatively accessible — Parimala exceeds it.

**Sell plan (if location is workable):**
- Lead with Entrata's production ML work: *"I automated HUD income limit data transformation using Python, PyTorch, and OpenAI API — replacing manual Excel workflows across 1.6M records. That's exactly the document intelligence pattern dv01 is building."*
- AgentProbe's eval pipeline maps to the MLflow/performance tracking requirement.
- AI on FHIR's BERT + NLP pipeline on medical documents is the closest analog to banking document parsing.

**Recruiter screen must-ask:** *"Is this role NYC onsite, hybrid, or remote?"* — Before any further investment.

---

## D) Comp and Demand

| Source | Range | Notes |
|--------|-------|-------|
| Job posting | $145K–$160K | Disclosed |
| Market | $160K–$220K for Sr ML Engineer in NYC | Below market for NYC cost of living |
| Remote equivalent | $130K–$160K | More competitive if remote |

**Assessment:** $145-160K is below market for a senior ML engineer in NYC — though dv01 is a smaller fintech data company, not a FAANG or AI lab. If the role is remote, comp is more reasonable relative to Virginia cost of living.

**H-1B:** dv01 is a smaller fintech company (~50-100 employees). H-1B history unclear — verify in first call.

---

## E) Customization Plan

| # | Section | Current | Proposed change | Why |
|---|---------|---------|-----------------|-----|
| 1 | Summary | Varies | Lead: *"ML engineer with production Python, NLP pipeline experience, and full AI/ML lifecycle — built document intelligence systems and automated data transformation pipelines at scale"* | JD: document parsing + ML lifecycle |
| 2 | Entrata | General | Elevate: PyTorch + OpenAI income limits module (1.6M records), NLP/document processing, financial data pipelines | JD: banking doc intelligence + production ML |
| 3 | AI on FHIR | Secondary | Promote: NLP pipeline on structured documents (BERT, spaCy, embeddings) — analog to banking doc parsing | JD: document parsers + classifiers |
| 4 | AgentProbe | Eval focus | Emphasize: eval pipeline = MLflow equivalent (run-level metrics, regression detection) | JD: MLflow, performance tracking |

---

## F) Interview Plan

| # | JD Requirement | Story | Key Points |
|---|----------------|-------|------------|
| 1 | Document parsing / NLP pipeline | AI on FHIR: BERT + spaCy + NLP → FHIR APIs | NLP pipeline design, entity extraction, structured output from unstructured text |
| 2 | Production ML lifecycle + MLOps | Entrata income limits module (PyTorch + OpenAI) + AgentProbe | Training → eval → deploy → monitor → retrain loop |
| 3 | Performance tracking / eval | AgentProbe: 5-metric eval engine, regression tracking across runs | "I built the equivalent of MLflow for LLM eval — same discipline, different tool" |
| 4 | Python + FastAPI production | AgentProbe 15-endpoint backend + Entrata 1M+ records | Production-grade code, async, quality gates |
| 5 | Financial/lending domain | Fraud roles targeted (Capital One, Intuit, Signifyd); Entrata financial data | Fintech awareness, regulatory data sensitivity |

---

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|--------|---------|--------|
| Salary disclosed | $145K–$160K | Positive |
| Company | dv01: established fintech data platform, Series B+ | Positive |
| JD specificity | Named tools (MLflow, Databricks, BigQuery, K8s) — not a ghost posting | Positive |
| LinkedIn active | Listed as active on LinkedIn | Positive |
| H-1B | Small fintech — unclear; verify | ⚠️ Confirm |
| Location | NYC — confirm remote policy | ⚠️ Confirm |

---

## Keywords Extracted

ai ml engineer, machine learning, document intelligence, mlflow, databricks, bigquery, python, pytorch, fastapi, docker, kubernetes, gcp, nlp, fintech, lending, dv01, production ml, mlops

---

## Machine Summary

```yaml
report_num: 046
company: dv01
role: AI ML Engineer
date: 2026-06-11
score: 3.3
archetype: AI Platform / LLMOps
legitimacy: High Confidence
location: New York, US (likely NYC onsite — confirm remote policy)
comp_range: "$145K–$160K base"
visa_risk: medium-high (small fintech company, H-1B history unknown — verify)
key_gaps:
  - MLflow (required — AgentProbe custom eval = same concept, different tool)
  - Databricks / BigQuery (not in CV)
  - GCP preferred (AWS + Azure in CV)
  - Kubernetes (Docker yes; K8s no)
  - NYC location — must confirm remote policy before applying
key_strengths:
  - Python 8+ years production
  - Entrata: PyTorch + OpenAI income limits module (1.6M records) = production ML
  - AI on FHIR: NLP pipeline on documents = document parsing analog
  - AgentProbe eval engine = MLflow equivalent
  - Fintech domain adjacent
location_risk: high if NYC onsite — confirm before applying
recommend: confirm remote policy + H-1B before applying; score below 4.0 threshold — only proceed if remote confirmed
```
