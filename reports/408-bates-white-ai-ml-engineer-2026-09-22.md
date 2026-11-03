# Evaluation: Bates White -- AI/ML Engineer (AI Workflows & Agents)

**Date:** 2026-09-22
**URL:** (pasted directly, no URL provided)
**Archetype:** AI/ML Engineer / Applied AI Platform (Boutique Consulting)
**Score:** 4.1/5
**Legitimacy:** High Confidence
**PDF:** output/cv-venkata-lakshmi-parimala-pasupuleti-bates-white-2026-09-22.pdf
**Location:** Washington DC (hybrid 3 days/week; Virginia home turf -- no relocation)
**Comp:** $160,000-$190,000 base + discretionary bonus

---

## A) Role Summary

| Dimension | Detail |
|-----------|--------|
| Archetype | AI/ML Engineer -- design, build, and deploy AI workflows and autonomous agents using LLMs, RAG, multi-step orchestration, and enterprise AI platforms; own evaluation, monitoring, and responsible AI practices; enable broader data engineering team |
| Domain | Bates White -- boutique economic consulting firm, DC-based; advanced economic/financial/econometric analysis for law firms, government agencies, corporations; Vault Guide Top 50 Consulting Firms; WTOP Top Workplaces 11 consecutive years |
| Stack | Azure AI Foundry, Azure OpenAI, Databricks, AWS Bedrock/SageMaker, Google Cloud Vertex AI / Gemini (primary: Azure-focused) |
| Seniority | 7yr minimum -- above junior/mid; equivalent to Senior AI Engineer IC; no formal L-grades at boutique consulting |
| Location | **Washington DC hybrid, 3 days/week in-office. Virginia = home turf. No relocation.** |
| Company | Bates White -- established firm (founded 1999, ~200 employees, Vault Top 50); H-1B infrastructure likely; confirm at screen |
| TL;DR | Strong core match: LangGraph 3 production systems, AgentProbe = evaluation/monitoring platform (MLOps/LLMOps category), responsible AI (HIPAA/PHI), RAG + guardrails. Gaps: Azure AI services layer (Foundry/OpenAI absent; infrastructure Azure present), "3 years AI" timeline tight (1.5-2yr explicit; quality compensates), Databricks absent. Location and comp are exceptional. Score 4.1 -- Apply. |

---

## B) Match with CV

| JD Requirement | CV Match | Strength |
|----------------|----------|----------|
| 7yr SWE/DE experience | 9yr total SWE | ✅ Exceeds |
| 3yr hands-on AI/LLM/agents | AgentProbe (2025) + LeaseI (2025-2026) + Magizhs (2025) + GMU Research (2024-2026) ≈ 1.5-2yr intensive | ⚠️ Timeline tight (quality compensates) |
| Python | Python 9yr primary | ✅ Strong |
| LangChain / LangGraph / comparable | LangGraph: 3 production systems (LeaseI 8-agent, AgentProbe, Magizhs) | ✅ Exceptional |
| RAG pipelines, vector databases, embeddings | LeaseI RAG; AgentProbe ChromaDB; AI on FHIR embeddings | ✅ Strong |
| Agent workflows, tool use, function calling | LeaseI (8-agent, conditional routing, tool calling); Magizhs (planning agent) | ✅ Strong |
| Prompt engineering + model evaluation + guardrails | AgentProbe (5-metric eval, LLM-as-judge, hallucination detection); prompt design across all projects | ✅ Strong |
| CI/CD for AI workflows | AgentProbe: CI-integrated regression gate (GitHub Actions) | ✅ Direct match |
| Monitor, evaluate, improve deployed AI systems | AgentProbe: production monitoring, regression suite, pass@k harness, token efficiency tracking | ✅ Direct match |
| Responsible AI / data privacy / security | AI on FHIR (HIPAA-compliant, RBAC, PHI); Entrata PHI compliance (zero incidents) | ✅ Strong |
| REST APIs + enterprise integration | FastAPI 15-endpoint; Entrata third-party integrations | ✅ Strong |
| SQL + structured/unstructured data | PostgreSQL 9yr; OCR/document intelligence (LeaseI) | ✅ Strong |
| MLOps/LLMOps tooling (MLflow, W&B, LangSmith) | Built AgentProbe = evaluation/monitoring platform same category; MLflow/W&B absent | ⚠️ Built equivalent; named tools absent |
| Azure AI Foundry / Azure OpenAI | Azure in stack (infrastructure); AI Foundry/Azure OpenAI absent from CV | ⚠️ Azure present, AI services gap |
| Databricks | Not in stack | ❌ Gap |
| AWS Bedrock / SageMaker | AWS present (S3/EC2/RDS/Glue); Bedrock/SageMaker absent | ⚠️ AWS present; AI services gap |
| Google Cloud / Vertex AI / Gemini | Not in stack | ❌ Gap |
| Multi-modal (vision, audio) | LeaseI OCR (document); no audio/video multimodal | ⚠️ Partial; listed as "plus" |
| Communication with stakeholders/leadership | Magizhs (external client architecture reviews); Entrata (cross-functional); GMU TA (600+ students) | ✅ Present |

---

## C) Why This Scores 4.1

**Core match is strong.** Python, LangGraph, RAG, agent orchestration, model evaluation, guardrails, responsible AI (HIPAA/PHI), CI/CD for AI, SQL -- all present and well-evidenced. The JD's core function (build AI workflows + autonomous agents + evaluation + governance) maps directly to LeaseI + AgentProbe.

**AgentProbe is the evaluation/monitoring answer.** The JD asks for "monitor, evaluate, and continuously improve accuracy, performance, cost, and reliability of deployed AI systems" and "MLOps/LLMOps tooling for experiment tracking and model monitoring." AgentProbe is a purpose-built evaluation and regression platform -- built independently from the same design insight as MLflow and LangSmith. She can speak to this category with credibility because she built it.

**CI/CD for AI workflows is a direct match.** "Build and maintain CI/CD pipelines and automated testing for AI workflows and agents" -- AgentProbe's CI-integrated regression gate is exactly this, blocking quality degradation on every commit.

**Responsible AI match is strong.** The JD has extensive language around "data privacy and security, prompt injection and abuse mitigation, evaluation and guardrails, AI governance policies." AI on FHIR (HIPAA-compliant, RBAC, PHI data) + Entrata PHI compliance (zero security incidents across full S3/AWS migration) + AgentProbe (hallucination detection, output validation, guardrails) covers this dimension comprehensively.

**Location is a material positive.** Washington DC hybrid, 3 days/week in-office. Virginia = she doesn't need to relocate. This is a rare combination: strong comp ($160-190K + bonus), Vault Top 50 prestige firm, within normal commuting range of home.

**The "3 years AI" timeline is the key tension.** By strict counting: Magizhs (May-Aug 2025, 4mo) + LeaseI/AgentProbe (2025-2026, ~1yr) + GMU Research (2024-2026, ~2yr but not exclusively AI) ≈ 1.5-2yr explicit AI/LLM work against a 3-year bar. Mitigant: quality of output (8-agent production LangGraph, open-source eval platform, 1,240 test cases, CI-integrated regression) demonstrates genuine senior-level depth that many 3yr practitioners don't reach. Boutique consulting firms often evaluate demonstrated output over year-counting.

**Azure AI platform gap.** Bates White is Azure-focused (Azure AI Foundry, Azure OpenAI). Azure is in her stack at infrastructure level -- not the AI services layer. Azure OpenAI specifically is an API layer over the same OpenAI models she already uses (OpenAI API), so the transfer is fast. Can acknowledge the AI services gap and frame as "Azure infrastructure experience + multi-provider LLM API depth; Azure OpenAI is immediate pickup."

**Databricks absent.** Listed as a primary platform alongside Azure AI Foundry. Not in stack. This is a genuine gap but an onboarding concern at a company whose core differentiator is the AI orchestration layer, not the data lakehouse.

---

## D) Comp and Demand

| Source | Range | Notes |
|--------|-------|-------|
| Disclosed | **$160,000-$190,000 base + discretionary bonus** | Among highest in pipeline |
| Total | $160K-$190K + bonus + tuition reimbursement up to $75K + benefits | One of top total comp packages evaluated |
| H-1B | Established DC consulting firm (founded 1999, Vault Top 50, ~200 employees) | ✅ Likely capable; confirm at screen |
| Location | Washington DC hybrid (3 days/week in-office); Virginia = no relocation | ✅ Home turf; +0.2 location boost |

---

## E) CV Plan

Frame: "AI/ML Engineer with production LangGraph systems and an open-source LLMOps evaluation platform -- AgentProbe covers the monitoring, evaluation, and CI/CD-gated quality your JD describes. Responsible AI built in: HIPAA compliance in production from two separate systems."

- Summary: LangGraph production depth + AgentProbe as MLOps/LLMOps evaluation platform + HIPAA responsible AI + Entrata production engineering rigor
- Skills: LangGraph, LangChain, Python, RAG, vector databases, embeddings, LLM evaluation, guardrails, CI/CD, Azure, AWS, HIPAA, FastAPI, PostgreSQL, MLOps/LLMOps
- Magizhs: external client delivery, architecture reviews, build-vs-buy decisions on orchestration/RAG/validation
- Entrata: PHI compliance, production Python backend, reliability at scale
- Projects: AgentProbe (MLOps/LLMOps evaluation platform = direct MLflow/LangSmith category) + LeaseI (multi-agent production system with RAG + guardrails + HITL) + AI on FHIR (HIPAA-compliant responsible AI)

---

## G) Posting Legitimacy

**High Confidence.** Bates White is a verifiable, established Washington DC consulting firm (founded 1999, Vault Guide Top 50 Consulting multiple years, WTOP Top Workplaces 11 consecutive years, website: bateswhite.com). Salary range disclosed ($160K-$190K). Specific and detailed JD with named platforms. Real careers email. No ghost signals.

---

## Recommendation: Apply (4.1/5 -- clears threshold with DC location boost)

Strong core match on agents, LangGraph, RAG, evaluation, CI/CD for AI, responsible AI (HIPAA). Location is perfect (Virginia/DC hybrid, no relocation). Compensation is the highest base in the active pipeline ($160-190K + bonus + $75K tuition).

Primary gaps to acknowledge: "3 years AI" timeline is 1.5-2yr by strict count (quality depth compensates); Azure AI services (Foundry/Azure OpenAI) gap -- can frame as fast pickup from existing Azure + multi-provider LLM depth; Databricks absent.

Must confirm at first contact: H-1B sponsorship + Metro/commute logistics for Virginia-to-DC hybrid.

---

## Machine Summary

```yaml
report: 408
company: Bates White
role: AI/ML Engineer (AI Workflows & Agents)
date: 2026-09-22
score: 4.1
archetype: AI/ML Engineer / Applied AI Platform (Boutique Consulting)
legitimacy: High Confidence
url: null
status: Evaluated
recommendation: Apply
threshold: 4.5 (non-PropTech standard) -- below; 4.0 (DC home turf +0.2) -- clears
boosts_applied:
  - LangGraph 3 production systems (LeaseI 8-agent, AgentProbe, Magizhs)
  - AgentProbe = MLOps/LLMOps evaluation + monitoring platform (MLflow/LangSmith category)
  - Responsible AI: HIPAA-compliant AI on FHIR + Entrata PHI (zero incidents)
  - RAG + vector DB + agent orchestration + guardrails + CI/CD = core JD coverage
  - Location: Virginia/DC home turf, hybrid 3 days/week; +0.2
  - Comp: $160-190K + bonus + $75K tuition (top of pipeline)
  - Established firm (Vault Top 50, 1999) = H-1B likely capable
penalties:
  - "3 years AI" timeline: ~1.5-2yr explicit AI/LLM work vs 3yr bar (-0.2)
  - Azure AI Foundry / Azure OpenAI absent at AI services layer (-0.2)
  - Databricks absent (-0.1)
  - MLflow / W&B absent (AgentProbe is equivalent; named tools missing) (-0.1)
  - Google Cloud / Vertex AI absent (-0.1)
  - Multi-modal gap (OCR only; "plus" not required) (-0.1; nice-to-have)
gaps:
  - "3 years AI" by strict count (quality compensates)
  - Azure AI Foundry / Azure OpenAI (infrastructure Azure only)
  - Databricks (not in stack)
  - MLflow / W&B / LangSmith (built equivalent with AgentProbe)
  - Google Cloud / Vertex AI / Gemini (absent)
h1b: Likely -- established DC consulting firm (founded 1999, Vault Top 50, ~200 employees); confirm at screen
comp_range: $160,000-$190,000 base + discretionary bonus + tuition reimbursement up to $75K
location: Washington DC hybrid (3 days/week in-office); Virginia = no relocation; +0.2 boost
```
