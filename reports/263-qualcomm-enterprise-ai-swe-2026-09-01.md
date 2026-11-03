# 263 — Qualcomm — Senior Software Engineer, Enterprise AI Platform

**Date:** 2026-09-01
**Score:** 2.8/5 — User override APPLY
**URL:** N/A (JD provided directly — Qualcomm Careers, Enterprise AI Platform & Solutions)
**PDF:** ❌
**Legitimacy:** High Confidence — Qualcomm official JD with salary range, specific team (Enterprise AI Platform and Solutions), onsite location (San Diego CA), EEO statement, accommodation contact

---

## Block A — CV Match

**Technical stack alignment is exceptional — RAG, agentic, eval frameworks, MCP all explicitly required or preferred.**

| JD Requirement | CV Proof Point |
|---------------|----------------|
| "RAG solutions: document ingestion, indexing, embeddings, vector search, reranking, retrieval optimization, grounding, evaluation frameworks" | LeaseI: full RAG pipeline (TF-IDF, OCR, vector search, reranking, retrieval); AgentProbe: evaluation frameworks with grounding metrics ✓ |
| "Multi-agent systems and evaluation frameworks" (nice-to-have) | AgentProbe + LeaseI 8-agent LangGraph — exact match for both ✓ |
| "Agentic workflows, agents, AI services into enterprise applications" | LeaseI 8-agent stateful LangGraph system ✓ |
| "MCP-compatible services" | MCP in skills; Claude Code MCP integration ✓ |
| "Tracing/observability tools for LLM systems" (nice-to-have) | AgentProbe: LLM observability, latency tracking, hallucination rate, token efficiency monitoring ✓ |
| "CI/CD pipelines, observability, monitoring, tracing for AI applications" | AgentProbe CI-integrated regression gate; GitHub Actions CI/CD ✓ |
| Python | Python 8yr ✓ |
| JavaScript, TypeScript | TypeScript, JavaScript throughout ✓ |
| "Full-stack applications: backend services, APIs, data integration layers" | Python + FastAPI backend; TypeScript/JavaScript; React (AI on FHIR) ✓ |
| Cloud-native AWS | AWS S3, EC2, RDS, Glue ✓ |
| Docker | Docker containerization ✓ |
| "API design, microservices, authentication, authorization" | FastAPI REST APIs; 20+ microservice modules; PHI-compliant auth pipelines ✓ |
| "Debugging across traditional systems and AI/LLM-driven behavior" | AgentProbe hallucination detection + LLM-as-judge; Entrata production debugging at scale ✓ |

**Gaps:**
- Kubernetes (Docker covered; K8s not in background)
- Elasticsearch (ChromaDB/TF-IDF vector search covered; not Elasticsearch specifically)
- Java / C#.NET (Python + JavaScript/TypeScript covers the stack; Java/C# not in background)
- React.js primary (used in AI on FHIR; not primary frontend framework)

**ATS baseline:** ~17/20. Patches: Kubernetes context, vector search/Elasticsearch framing, full-stack emphasis, MCP, agentic, evaluation frameworks.

---

## Block B — North Star Alignment

**Archetype: AI software engineer building enterprise AI platform.** Qualcomm's Enterprise AI Platform team builds RAG, agentic, and LLM-powered capabilities for internal enterprise use. Strong technical alignment to user's project portfolio; domain is semiconductor/hardware company internal tooling rather than PropTech or external AI product. Not the primary target archetype but technically closest match of any role evaluated.

---

## Block C — Compensation

$111,300–$166,900 base. Qualcomm also offers RSUs and bonuses at senior levels; total comp can reach $180K-$220K with equity. However, base ceiling of $167K is below Crexi ($179K-$241K), Microsoft (L63 ~$180K-$230K), and Balerion ($250K+). Significantly below market for this exact stack in 2026.

**Score: 2.0/5**

---

## Block D — Cultural Signals

- Qualcomm: established semiconductor/software company; stable, large engineering org
- Enterprise AI Platform = real AI investment, not just AI-washing; RAG + agents + MCP explicitly
- "Fast-paced, execution-driven" — startup-like energy within a large company
- 5 days/week onsite San Diego — no hybrid, no remote; significant for Virginia-based candidate
- No relocation package mentioned in JD
- Qualcomm international hiring culture = likely H-1B friendly

**Score: 2.5/5**

---

## Block E — Red Flags

1. **Salary $111K–$167K base** — significantly below market; lowest base ceiling of any role evaluated this session
2. **5-day onsite San Diego** — full-time onsite; Virginia → San Diego relocation with no package confirmed in JD
3. **H-1B unconfirmed** — Qualcomm likely sponsors (large international workforce) but not explicitly stated
4. **Kubernetes gap** — "Kubernetes-based environments" listed in responsibilities; Docker covered
5. **Java/C#.NET** — listed in must-haves; user is Python + JS/TS primary
6. **Internal enterprise platform** — building tooling for Qualcomm's own operations; less external product impact

**Adjustment: -0.3 (user override to APPLY)**

---

## Block F — Global Score

| Factor | Signal |
|--------|--------|
| CV match | 4.5 — RAG, agentic, eval frameworks, MCP, observability, Python, APIs, CI/CD — best technical match of any role today |
| North Star | 3.0 — AI engineer archetype ✓; internal enterprise platform at hardware company; not PropTech |
| Comp | 2.0 — $111K-$167K base; below market for this stack |
| Culture | 2.5 — Qualcomm stable; 5-day onsite SD; no relocation package; large company pace |
| Red flags | -0.3 — salary, onsite SD, Kubernetes/Java gaps, H-1B unconfirmed |

**Global: 2.8/5 — User override APPLY**

---

## Block G — Posting Legitimacy

**High Confidence.** Qualcomm official JD with salary range ($111,300–$166,900), specific team name (Enterprise AI Platform and Solutions), exact location (San Diego CA), EEO statement, disability accommodation contact (disability-accomodations@qualcomm.com). No ghost indicators.

---

## Machine Summary

```yaml
company: Qualcomm
role: Senior Software Engineer, Enterprise AI Platform
score: 2.8
status: Evaluated
date: 2026-09-01
salary_low: 111300
salary_high: 166900
location: San Diego CA (5-day onsite)
remote: false
visa: likely (unconfirmed)
proptech_boost: false
h1b_status: unconfirmed
top_match: RAG + agentic + eval frameworks + MCP + observability — best technical stack match of session
gaps: Kubernetes, Java/C#, Elasticsearch, salary below market, onsite SD relocation
```
