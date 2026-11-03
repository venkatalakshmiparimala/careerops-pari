# 268 — Intellivo — Sr. AI/Machine Learning Engineer

**Date:** 2026-09-03
**Score:** 2.6/5 — SKIP
**URL:** N/A (JD provided directly — Intellivo, Memphis TN / remote)
**PDF:** ❌
**Legitimacy:** High Confidence — Intellivo is a real, established company (26yr, 200+ health plan clients); role is consistent with their subrogation technology focus; no ghost indicators

---

## Block A — CV Match

**Strong on LLM integration and document intelligence. Meaningful gaps on Azure, healthcare/claims domain, traditional ML training, and entity resolution.**

| JD Requirement | CV Proof Point |
|---------------|----------------|
| 5+ years ML, data science, or data engineering | 8yr production Python + data pipelines at Entrata; MS Data Analytics Engineering ✓ |
| Python + SQL | Python 8yr; 200+ SQL optimizations across PostgreSQL/Oracle/MySQL ✓ |
| Foundation model API usage — Claude, OpenAI, Ollama | AgentProbe: Anthropic API, OpenAI API, Ollama multi-provider routing ✓ |
| LangChain and LangGraph | Core stack in both AgentProbe and LeaseI ✓ |
| Prompt design, tool calling, structured output | Throughout both projects ✓ |
| RAG + vector stores | AgentProbe (ChromaDB); LeaseI (TF-IDF RAG) ✓ |
| Document intelligence, OCR, information extraction | LeaseI: pdfplumber + pytesseract OCR fallback, section-aware chunking, field extraction ✓ |
| "Build practical evaluation into everything" | AgentProbe: 5-metric eval engine, LLM-as-judge, CI regression gate — evaluation-first philosophy ✓ |
| PHI compliance, access controls | Entrata: 100% PHI compliance (Libsodium), zero security incidents across 7yr ✓ |
| scikit-learn, PyTorch | Both in background; ML pipelines at GMU (R² = 0.977) ✓ |
| "Speak up when a simpler answer is right" | LeaseI: deliberately chose hand-rolled TF-IDF over LangChain vector DB — judgment over hype ✓ |

**Gaps:**
- **Azure (ML, AI Foundry, Azure OpenAI)** — required qualification; user is AWS-native; Azure not in background
- **Healthcare / insurance / claims data** — strongly preferred; AI on FHIR is adjacent (FHIR format) but not insurance claims, subrogation, or TPL
- **SageMaker / H2O / AutoML platforms** — required; user has scikit-learn and PyTorch but not managed ML training platforms
- **Synthetic data generation** — not in background
- **Entity resolution, record linkage, fuzzy matching** — preferred; not explicitly in background
- **Azure certification (AI-102, DP-100)** — preferred; not held

**ATS baseline:** ~13/20. Significant gaps on Azure, healthcare domain, SageMaker, synthetic data.

---

## Block B — North Star Alignment

**Partial archetype match.** "ML Engineer (applied, product-facing only)" partially fits — the LLM integration, document intelligence, and evaluation components align. But the role also requires traditional ML training (classification, entity matching, propensity scoring with SageMaker/H2O/AutoML) and deployment on Azure — this edges toward the ML infrastructure territory that's a hard block in the profile. Healthcare/insurance/subrogation domain has no overlap with Entrata PropTech or any other experience area. "Sr." title at a 26-year-old established company with 200+ health plan customers (likely 200+ employees) also raises the Senior-penalty flag.

**Score: 2.5/5**

---

## Block C — Compensation

Undisclosed. Memphis, TN location with remote option: typical market for this stack and level in a Memphis-headquartered company is $130K–$165K. Lower ceiling than coastal AI engineering roles. No equity signal (established company, not startup).

**Score: 2.5/5**

---

## Block D — Cultural Signals

- "Builder's role, not a research role" — right culture framing
- 26-year company — established, stable, slower pace than startup
- "Innovative startup mentality" — common claim from legacy companies; treat with skepticism
- Healthcare/insurance subrogation = stable niche, meaningful outcomes, but not cutting-edge AI product
- Remote-friendly but Memphis-preferred — not a blocker
- PHI / compliance-heavy environment — Entrata background is genuinely relevant here

**Score: 3.0/5**

---

## Block E — Red Flags

1. **Azure required, not preferred** — "Working knowledge of Microsoft Azure for deploying and operating ML workloads" is listed under required qualifications; user's cloud experience is AWS-only
2. **Healthcare/claims domain gap** — "strongly preferred"; no subrogation, insurance, or claims processing background
3. **SageMaker / H2O / AutoML** — required; user has scikit-learn/PyTorch but not managed ML training platforms; this edges toward ML infra territory
4. **"Sr." title at an established company** — 26yr company, 200+ health plan clients = likely 200+ employees; Senior interview bar risk (confirmed pattern from prior rejections)
5. **Comp ceiling** — Memphis-based company, undisclosed; likely below coastal AI engineering market

**Adjustment: -0.3**

---

## Block F — Global Score

| Factor | Signal |
|--------|--------|
| CV match | 3.0 — LLM integration, document intelligence, RAG, eval, PHI all match; Azure, healthcare, SageMaker, entity resolution are real gaps |
| North Star | 2.5 — partial ML Engineer archetype; Azure gap, traditional ML training, healthcare domain, Senior title at established company |
| Comp | 2.5 — undisclosed; Memphis-based company likely below coastal AI market |
| Culture | 3.0 — right builder culture; 26yr legacy company; PHI-compliant environment |
| Red flags | -0.3 — Azure required + healthcare domain + SageMaker + Senior title risk |

**Global: 2.6/5 — SKIP**

> The document intelligence, OCR, LLM integration, and PHI compliance aspects are genuine matches. But Azure is a required qualification (not preferred) and it's not in the background. The healthcare/claims domain gap and SageMaker requirement add further friction. The role itself is not wrong for the archetype — it's a skills mismatch on the required qualifications, not a domain or culture mismatch.

---

## Block G — Posting Legitimacy

**High Confidence.** Intellivo is a verifiable, established company (intellivo.com) with 26 years of operation in health plan subrogation. Role is consistent with their product direction. Specific team (IT and Programming), employment type (full-time), experience level, and company background all consistent. No ghost indicators.

---

## Machine Summary

```yaml
company: Intellivo
role: Sr. AI/Machine Learning Engineer
score: 2.6
status: SKIP
date: 2026-09-03
salary_low: null
salary_high: null
location: Memphis TN (remote, Memphis preferred)
remote: true
visa: unconfirmed
proptech_boost: false
h1b_status: unconfirmed
top_match: LLM integration, document intelligence, OCR, RAG, LangChain/LangGraph, PHI compliance, LLM evaluation
gaps: Azure required (not in background), healthcare/claims domain, SageMaker/AutoML, synthetic data, entity resolution, Senior title at 200+ employee company
```
