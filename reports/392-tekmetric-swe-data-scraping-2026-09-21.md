# Evaluation: Tekmetric -- Software Engineer (Web Scraping / Data Pipelines / Search)

**Date:** 2026-09-21
**URL:** (pasted directly, no URL provided)
**Archetype:** Data Engineering / Web Scraping / Search Infrastructure
**Score:** 2.5/5
**Legitimacy:** High Confidence
**PDF:** N/A (below threshold)
**Location:** Remote ✅
**Comp:** Undisclosed

---

## A) Role Summary

| Dimension | Detail |
|-----------|--------|
| Archetype | Data Engineering -- large-scale web scraping, data ingestion/classification, ElasticSearch indexing |
| Domain | Auto repair shop SaaS (Tekmetric); building data ingestion + classification infrastructure |
| Function | Build distributed crawlers, scrape/extract from web/PDFs/APIs, normalize data, index via ElasticSearch/OpenSearch, orchestrate with Airflow, scale with Spark on EMR |
| Seniority | "Software Engineer" (no Senior title) -- 3+ yr required; startup est. 2017, no formal leveling concern |
| Location | Remote ✅ |
| Company | Tekmetric -- auto repair shop SaaS, Houston 2017, growing startup; likely 100-300 employees |
| TL;DR | Web scraping + ElasticSearch + Airflow + Spark are the core required stack -- none of them are in her portfolio at production depth. Python/AWS/OCR/NLP/K8s overlap is real but doesn't compensate. Good company (startup, remote, no leveling concern, interesting AI crawler direction) but wrong technical specialty. Score 2.5 -- SKIP. |

---

## B) Match with CV

| JD Requirement | CV Match | Strength |
|----------------|----------|----------|
| 3+ years Python | Python 9yr primary | ✅ Exceeds |
| AWS | AWS S3, EC2, RDS, Glue -- 7yr | ✅ Present |
| Kubernetes | K8s confirmed (Entrata) | ✅ Present |
| REST API integration | FastAPI, third-party data integrations | ✅ Present |
| PDF processing / OCR | LeaseI: OCR-fallback ingestion pipeline | ✅ Present |
| NLP and ML (nice to have) | spaCy, BERT, scikit-learn, LangGraph -- all present | ✅ Strong (nice to have fully covered) |
| LLM frameworks (nice to have) | LangGraph, LLM APIs -- strong | ✅ Strong (nice to have fully covered) |
| Document classification (nice to have) | LeaseI: clause extraction, compliance classification | ✅ Present |
| NoSQL / SQL | PostgreSQL 9yr, NoSQL present | ✅ Present |
| **Web scraping / Scrapy at scale** | **Zero scraping experience -- not her background** | ❌ Core gap |
| **ElasticSearch / OpenSearch** | Not in stack | ❌ Core gap |
| **Airflow** | Listed as "learning" -- not production | ❌ Core gap |
| **Spark / EMR** | Apache Spark familiarity only -- not production | ❌ Core gap |
| Anti-scraping mechanisms | Not in background | ❌ Gap |
| H-1B sponsorship | Startup, no mention in JD -- unconfirmed | ⚠️ Verify |

---

## C) Why This Doesn't Fit

**The core required stack is wrong.** The explicit job summary: "expertise in web scraping, data processing, and search technologies." The primary 3+ years experience requirement is Python "with building crawling/scraping solutions at scale" -- not general Python, specifically scraping at scale. She has none of that. ElasticSearch/OpenSearch is the search indexing layer the whole pipeline feeds into -- also absent. Airflow and Spark are orchestration and scale tools listed as core requirements, not nice-to-haves -- both are learning/familiarity level at best.

**What she has is real but peripheral.** Python/AWS/K8s/REST/OCR/NLP -- all present and strong. The AI crawler direction ("perhaps AI agents") and NLP/classification work are genuinely interesting matches. But those are downstream of the scraping infrastructure she'd be primarily building.

**Good company characteristics.** Startup (no leveling concern), remote, active engineering culture, interesting problem space. The concern is purely technical specialization mismatch, not company/culture.

---

## G) Posting Legitimacy

**High Confidence.** Tekmetric is a verifiable, funded startup (Houston, 2017). Active engineering hiring with leadership networking event detail. Role description is technically specific and credible.

---

## Recommendation: SKIP (2.5/5)

Web scraping/Scrapy, ElasticSearch/OpenSearch, Airflow, and Spark are all simultaneously core requirements -- all simultaneously missing or at learning level.

---

## Machine Summary

```yaml
report: 392
company: Tekmetric
role: Software Engineer -- Web Scraping / Data Pipelines / Search
date: 2026-09-21
score: 2.5
archetype: Data Engineering / Web Scraping / Search Infrastructure
legitimacy: High Confidence
url: null
status: SKIP
gaps:
  - Web scraping / Scrapy at scale (core required, absent)
  - ElasticSearch / OpenSearch (core required, absent)
  - Airflow (core required, learning level only)
  - Spark / EMR (core required, familiarity only)
  - Anti-scraping mechanisms (specialized, absent)
strengths:
  - Python 9yr
  - AWS / K8s / REST APIs
  - OCR / PDF processing (LeaseI)
  - NLP/ML nice-to-haves fully covered (spaCy, BERT, LangGraph, scikit-learn)
h1b: Startup, unconfirmed -- would need to verify
location: Remote (no issue)
```
