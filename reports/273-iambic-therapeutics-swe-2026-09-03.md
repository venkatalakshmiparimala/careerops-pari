# 273 — Iambic Therapeutics — Software Engineer (Data Acquisition & Curation, Enchant)

**Date:** 2026-09-03
**Score:** 3.1/5 — SKIP
**URL:** N/A (JD provided directly — Iambic Therapeutics)
**PDF:** ❌
**Legitimacy:** High Confidence — Iambic Therapeutics is a real AI-native drug discovery company (founded 2021, ~$100M Series A); Enchant is a real multimodal biomedical transformer model; JD is highly specific and technically credible

---

## Block A — CV Match

**The agentic engineering and evaluation harness requirements map directly to AgentProbe + LeaseI. The biomedical data domain is the critical gap.**

| JD Requirement | CV Proof Point |
|---------------|----------------|
| M.S. in computational STEM | M.S. Data Analytics Engineering, GPA 3.87 ✓ |
| Strong Python engineering, production-quality software | Python 8yr; 20+ production modules at Entrata ✓ |
| LLM APIs (Claude, GPT) + agentic patterns (tool use, orchestration, multi-step reasoning) | AgentProbe (Anthropic + OpenAI APIs); LeaseI 8-agent LangGraph ✓ |
| Agent orchestration frameworks | LangGraph, LangChain — core stack ✓ |
| "Evaluation harnesses for LLM-generated code" (preferred) | AgentProbe is literally this — CI-integrated eval gate for LLM outputs ✓ |
| ETL design, data validation, structured + unstructured data at scale | Entrata HUD pipeline (180K domain records); 200+ SQL optimizations; LeaseI multi-source document ingestion ✓ |
| Python testing frameworks (pytest) | AgentProbe: 1,240+ test cases; CI regression suite ✓ |
| Agent security practices: sandboxing, scoped credentials, audit logs, prompt injection | LeaseI: deterministic guardrails, audit trail per decision, HITL escalation; AgentProbe: hallucination detection ✓ |
| AWS, Docker (preferred) | AWS S3/EC2/RDS/Glue; Docker containerization ✓ |
| Data provenance, reproducibility, auditable reports | LeaseI: every output cited to exact source or flagged unsupported; PHI compliance (zero incidents) ✓ |

**Gaps:**
- **Biomedical/chemical data formats** — PDB, UniProt, ChEMBL, SDF/MOL, FASTA — required familiarity; zero background (AI on FHIR is healthcare-adjacent but not molecular/cheminformatics)
- **Drug discovery domain** — molecular biology, genomics, proteomics, assay data — no background
- **Large-scale ML training dataset construction** — data pipelines at Entrata are adjacent but not ML training data curation at this scale
- Kubernetes — Docker confirmed; K8s not in background

**ATS baseline:** ~15/20. Strong on agentic engineering, evaluation, Python, ETL, security. Gap on biomedical domain terms.

---

## Block B — North Star Alignment

**Archetype: Agentic / Automation — correct archetype.** "The model writes the code, the code runs the pipeline" — building agents that generate code to run data pipelines is a genuinely interesting agentic engineering problem. AgentProbe and LeaseI are directly relevant. However, the role is fundamentally about building data infrastructure for a biomedical AI model — the domain (drug discovery: molecules, proteins, assays, 'omics) is far from any target archetype. "Data acquisition for ML training" also edges toward ML data infrastructure. The engineering core is exciting; the domain creates friction.

**Score: 3.0/5**

---

## Block C — Compensation

Undisclosed. Iambic Therapeutics is a Series A biotech startup. Typical range for this stack/level at a biotech startup in San Diego: $130K–$170K base + equity. Equity upside depends on drug pipeline success — high variance, longer horizon than software company equity. No comp signal to score above 3.0.

**Score: 3.0/5**

---

## Block D — Cultural Signals

- Iambic is AI-native in biotech — not traditional pharma; genuine technical ambition
- "Evaluation harnesses," "auditable reports," "agent security" — engineering culture that takes reliability seriously
- San Diego (La Jolla) — likely onsite for a lab-adjacent biotech company; Virginia → San Diego relocation with no package stated
- Series A startup — faster pace, broader scope, meaningful equity, higher risk
- Biotech time horizon for equity is longer than software (drug pipeline → exit takes years)

**Score: 3.0/5**

---

## Block E — Red Flags

1. **Biomedical domain gap** — listed as a required qualification ("Familiarity with biomedical or chemical data sources and formats"); "familiarity" is a lower bar than expertise, but PDB/FASTA/ChEMBL are specialized formats with real learning curve
2. **Location likely San Diego onsite** — JD doesn't state location explicitly; Iambic is headquartered in La Jolla, CA; biotech companies are typically onsite
3. **Comp undisclosed** — standard for startup but no signal to assess
4. **H-1B at Series A startup** — possible but more friction than established company
5. **Domain adjacency risk** — "Large-scale biomedical dataset construction for ML training" is adjacent to ML data infrastructure hard block

**Adjustment: -0.3**

---

## Block F — Global Score

| Factor | Signal |
|--------|--------|
| CV match | 3.5 — agentic orchestration, LLM APIs, evaluation harnesses, ETL, Python, agent security — strong engineering fit; biomedical data formats are the required gap |
| North Star | 3.0 — Agentic/Automation archetype ✓; biotech domain off-target; ML training data infra edges toward hard-block territory |
| Comp | 3.0 — undisclosed; Series A biotech; likely $130K-$170K + equity with long horizon |
| Culture | 3.0 — AI-native, evaluation-focused culture is right; San Diego relocation and biotech pace are the friction |
| Red flags | -0.3 — biomedical domain gap, onsite SD likely, comp unknown, H-1B at startup |

**Global: 3.1/5 — SKIP**

> The engineering problem (agentic code generation for data pipelines, with evaluation harnesses) maps very well to the portfolio. The blocker is domain: the role requires working knowledge of molecular/genomic/clinical data formats, and none of the background covers that. If you have any interest in biomedical data and are willing to ramp on the domain, this is worth a conversation — the agentic engineering case for AgentProbe + LeaseI is genuinely strong.

---

## Block G — Posting Legitimacy

**High Confidence.** Iambic Therapeutics is a real, well-funded AI drug discovery company. "Enchant" is their documented multimodal model. JD is highly specific (exact data format names, detailed agent architecture requirements, sandboxing practices). No ghost indicators.

---

## Machine Summary

```yaml
company: Iambic Therapeutics
role: Software Engineer (Data Acquisition & Curation)
score: 3.1
status: SKIP
date: 2026-09-03
salary_low: null
salary_high: null
location: San Diego CA (La Jolla — likely onsite; not stated in JD)
remote: unconfirmed
visa: unconfirmed (Series A startup)
proptech_boost: false
h1b_status: unconfirmed
top_match: agentic orchestration, LLM APIs, evaluation harnesses, ETL/data pipelines, Python, agent security — strong engineering fit
gaps: biomedical data formats (required), drug discovery domain, ML training dataset curation, San Diego onsite likely, comp undisclosed
```
