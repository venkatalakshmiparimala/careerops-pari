# Evaluation: Berkley Technology Services -- Sr. AI Engineer

**Date:** 2026-09-23
**URL:** https://www.berkleytechnologyservices.com/ (pasted directly; LinkedIn sourced)
**Archetype:** Applied AI Engineer / LLMOps -- Production Agentic Systems
**Score:** 3.6/5
**Legitimacy:** High Confidence
**PDF:** ✅
**Location:** Urbandale, IA · Wilmington, DE (key offices; remote/hybrid status not specified)
**Comp:** Not disclosed · Fortune 500 insurance tech subsidiary · est. $115,000–$155,000 base

---

## A) Role Summary

| Dimension | Detail |
|-----------|--------|
| Archetype | Applied AI Engineer / LLMOps -- build, test, operate AI-enabled services and agentic workflows; RAG pipelines; integration into web apps; production observability; Responsible AI |
| Domain | Berkley Technology Services (BTS) -- IT services subsidiary of W. R. Berkley Corporation (Fortune 500, Commercial Lines Insurance); ~60+ operating units; Urbandale IA + Wilmington DE offices |
| Function | Python AI services + microservices; end-to-end RAG (Azure AI Search / Pinecone); agentic workflows (LangGraph / n8n / ADK); CI/CD + observability (Datadog/LangSmith); Responsible AI guardrails; agile collaboration |
| Seniority | Sr. AI Engineer -- "5+ years SE + 3+ years applied AI/LLM in production" -- AI-specific Senior where proof points (LangGraph, RAG, multi-agent, AgentProbe) are demonstrable; different from FAANG Senior SWE leveling |
| Location | Urbandale IA + Wilmington DE (office locations); no remote/hybrid designation in JD |
| H-1B | **Likely yes** -- BTS is backed by W. R. Berkley Corporation (Fortune 500, ~$12B revenue); large corporations at this scale routinely sponsor H-1B for specialized tech talent; confirm at first contact |
| TL;DR | Target archetype (Applied AI / LLMOps). Strong technical match on core stack: LangGraph, RAG, multi-agent, Python, AgentProbe eval, Claude Code. Gaps: Azure AI Foundry / Pinecone (have ChromaDB), A2A protocol, Langsmith/Datadog observability. Location (Urbandale IA / Wilmington DE) not major tech hub; no comp disclosed. Sr. title at insurance subsidiary -- different evaluation axis from FAANG Senior. Score 3.6 -- Evaluated, CV generated. |

---

## B) Match with CV

| JD Requirement | CV Match | Strength |
|----------------|----------|----------|
| 5+ years professional SE | 9yr total | ✅ Exceeds |
| 3+ years applied AI/LLM in production | Magizhs (production LangGraph, 2025); AgentProbe + LeaseI; GMU AI research (Aug 2024–May 2026) -- ~1.5yr concentrated, strong proof points | ⚠️ Stretch on YOE, strong on proof points |
| Python + modern engineering practices | Python 9yr; testing, linting, typing, packaging (AgentProbe CI/CD gate) | ✅ Strong |
| **LangGraph / agentic frameworks** | **LangGraph core stack: LeaseI (8-agent), AgentProbe, Magizhs production system** | ✅✅ Exact |
| End-to-end RAG pipelines (connectors, parsing, chunking, embeddings, indexing, retrieval) | LeaseI: OCR ingestion, section-aware chunking, ChromaDB embeddings + retrieval; Magizhs RAG over regulatory corpus | ✅ Strong |
| **Azure AI Search / Pinecone** | **ChromaDB (not Pinecone/Azure AI Search)** | ❌ Tool gap (vector DB concept ✅) |
| Multi-agent systems using MCP + A2A | LangGraph multi-agent ✅; Claude Code MCP usage ✅; A2A (Google Agent-to-Agent protocol) ❌ | ⚠️ Partial |
| Agentic AI dev tools: Cursor, Claude Code, Copilot | Claude Code daily ✅; Cursor/Copilot not primary tools | ✅ Hit |
| CI/CD + containerization | GitHub Actions, Docker, K8s | ✅ Strong |
| AI Observability: Datadog / LangSmith | AgentProbe: agent tracing, hallucination detection, CI regression gate (custom platform, not Datadog/LangSmith) | ⚠️ Custom platform present, named tools absent |
| Telemetry (logs/metrics/traces), dashboards, alerts | AgentProbe eval metrics + CI reports; Entrata observability (performance monitoring) | ⚠️ Adjacent |
| Responsible AI, data protection, PII, guardrails | AgentProbe hallucination detection, output validation; Magizhs compliance guardrails; AI on FHIR HIPAA/PII | ✅ Strong |
| FastAPI / REST integration with web applications | FastAPI (Magizhs 15-endpoint backend); REST APIs at Entrata | ✅ Strong |
| Fine-tuning LLMs (nice-to-have) | HuggingFace Transformers + PyTorch fine-tuning at GMU | ✅ Nice-to-have hit |
| NLP models (nice-to-have) | spaCy, BERT (AI on FHIR, GMU research) | ✅ Nice-to-have hit |
| LLM eval frameworks: DeepEval, RAGAs (nice-to-have) | AgentProbe custom eval (LLM-as-judge, pass@k, hallucination detection) -- concept ✅, named frameworks ❌ | ⚠️ Custom platform covers intent |
| Insurance / regulated domain (implicit) | No insurance domain; HIPAA/PHI regulated domain (healthcare) | ⚠️ Adjacent |

---

## C) Scoring

**Target archetype with strong technical core.** Applied AI Engineer / LLMOps is Archetype #1 in the profile. The role's primary technical requirements -- LangGraph agentic workflows, end-to-end RAG pipelines, production Python services, AI eval infrastructure, Responsible AI guardrails -- are all demonstrably present. LeaseI and AgentProbe are exactly the kind of proof points this JD is asking for.

**Sr. AI Engineer title at insurance subsidiary -- lower leveling risk than FAANG Senior.** The confirmed rejection pattern (AppFolio, Amazon, Juniper Square) was at pure tech companies with structured leveling interviews. BTS is a Fortune 500 IT services subsidiary evaluating specifically AI production experience. "5+ years SE + 3+ years applied AI/LLM" -- the AI requirement is the differentiated bar, and Parimala's portfolio addresses it with two production agentic systems. The evaluation axis is different from SWE seniority leveling at tech companies.

**3yr AI/LLM gap is real.** The JD says "3+ years of hands-on applied AI/LLM engineering delivering agentic AI production systems." Parimala's concentrated AI engineering work is ~1.5 years (Magizhs 2025 + GMU research from Aug 2024 + AgentProbe + LeaseI). The proof points are strong -- LeaseI (8-agent, 1,240 test cases, 93.6% precision) and AgentProbe (CI-integrated eval platform) are production-grade systems. But the calendar YOE is shorter than the 3yr ask. Address proactively: "I've built more production agentic AI than most engineers with 3yr in the field" is the honest framing.

**Azure AI Foundry / Pinecone gap.** The JD specifies Azure AI Search and Pinecone as the vector DB stack. ChromaDB is used instead. The underlying RAG engineering is identical -- chunking, embeddings, indexing, retrieval. The platform is different. Mentionable in cover letter; not a knockout gap.

**Langsmith / Datadog absent.** "AI Observability in platforms like Datadog and LangSmith" is listed as a required qualification. AgentProbe is Parimala's answer to the same problem (agent tracing, CI regression gate, eval metrics, LLM-as-judge). Named tools absent, but the engineering discipline is present and demonstrated.

**A2A not in portfolio.** Google's Agent-to-Agent (A2A) protocol is listed as a requirement ("Multi-agent systems using MCP and A2A technologies"). A2A is an emerging standard (released 2025). LangGraph multi-agent covers the multi-agent requirement; A2A as a protocol standard is not in the portfolio. Small gap; A2A is not yet ubiquitous.

**Location: Urbandale IA / Wilmington DE.** These are not major tech hubs. The JD doesn't specify remote or hybrid. Need to clarify work arrangement at screening. User memory confirms open to any US location, but a de facto onsite requirement at these locations would be a friction point.

**Nice-to-haves: two hits.** Fine-tuning (HuggingFace + PyTorch at GMU) and NLP models (spaCy + BERT) are both listed as nice-to-haves -- both present.

---

## D) Comp and Demand

| Source | Range | Notes |
|--------|-------|-------|
| Disclosed | **Not disclosed** | Standard for insurance industry postings |
| Estimated | **$115,000–$155,000 base** | Senior AI Engineer at Fortune 500 insurance tech subsidiary in IA/DE market; below coastal AI rates |
| H-1B | **Likely yes** -- W. R. Berkley Corporation (Fortune 500, ~$12B revenue) | Confirm at first contact; BTS serves 60+ global operating units -- complex HR infra implies H-1B infrastructure |
| Location | Urbandale IA or Wilmington DE; remote/hybrid status unconfirmed | Clarify at screening |

---

## E) Red Flags

- **3yr applied AI gap** -- calendar YOE ~1.5yr concentrated; proof points strong but timeline is a stretch
- **Azure AI Search / Pinecone absent** -- ChromaDB present; platform gap, not conceptual gap
- **LangSmith / Datadog absent** -- AgentProbe covers the observability engineering; named tools absent
- **A2A protocol absent** -- emerging standard; LangGraph multi-agent covers the intent
- **Location unclear** -- Urbandale IA / Wilmington DE; remote/hybrid not specified
- **Insurance domain** -- no industry background; HIPAA/healthcare adjacent but not insurance
- **Comp likely below coastal AI rates** -- insurance tech in Midwest/East

---

## F) Recommendation: Evaluated (3.6/5)

Target archetype (Applied AI / LLMOps) + strong core technical match (LangGraph, RAG, multi-agent, eval). Sr. title at insurance subsidiary is lower leveling risk than FAANG Senior SWE. Main gaps: 3yr AI YOE (proof points strong, timeline short), Azure AI tools/Pinecone/Langsmith absent. Location and comp are question marks. Apply if H-1B confirmed and work arrangement is acceptable. Lead with LeaseI + AgentProbe as the production AI engineering proof points the JD specifically requests.

---

## Machine Summary

```yaml
report: 422
company: Berkley Technology Services
role: Sr. AI Engineer
date: 2026-09-23
score: 3.6
archetype: Applied AI Engineer / LLMOps
legitimacy: High Confidence
url: https://www.berkleytechnologyservices.com/
status: Evaluated
gaps:
  - 3yr applied AI/LLM requirement -- ~1.5yr calendar YOE, strong proof points
  - Azure AI Foundry / Pinecone not in portfolio (ChromaDB present)
  - LangSmith / Datadog absent (AgentProbe covers engineering discipline)
  - A2A (Agent-to-Agent) protocol not in portfolio
  - Insurance domain -- no background
  - Location unclear (Urbandale IA / Wilmington DE; remote status unspecified)
strengths:
  - LangGraph in production (LeaseI 8-agent + AgentProbe + Magizhs) -- exact match
  - End-to-end RAG pipelines (ChromaDB, section-aware chunking, OCR ingestion)
  - AgentProbe eval infrastructure (CI-integrated, LLM-as-judge, hallucination detection)
  - Python 9yr + FastAPI + microservices
  - Responsible AI + guardrails + HITL
  - Claude Code daily use (exact JD requirement)
  - Fine-tuning nice-to-have: HuggingFace + PyTorch ✅
  - NLP nice-to-have: spaCy + BERT ✅
h1b: Likely yes -- Fortune 500 parent (W. R. Berkley); confirm at screening
comp_range: est. $115,000-$155,000 base (insurance tech, Urbandale IA / Wilmington DE)
location: Urbandale, IA · Wilmington, DE (remote/hybrid status unconfirmed)
```
