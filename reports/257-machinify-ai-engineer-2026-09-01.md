# 257 — Machinify — AI Engineer

**Date:** 2026-09-01
**Score:** 4.7/5 — APPLY (strong match)
**URL:** N/A (JD provided directly)
**PDF:** ❌
**Legitimacy:** High Confidence — detailed JD with specific salary band, healthcare-specific domain, 85+ health plans named, technology stack explicit

---

## Block A — CV Match

**Near-perfect alignment.** The JD reads like a description of what the user has already built:

| JD Requirement | CV Proof Point |
|---------------|----------------|
| "RAG pipelines, agents, tool-use systems, multi-step workflows" | LeaseI (8-agent LangGraph) + AgentProbe ✓ |
| "write evals before you write prompts, treat both as code" | AgentProbe is built on this exact philosophy — CI-integrated regression gate, 5-metric quality engine ✓ |
| "1+ year shipping LLM-based features in production" | AgentProbe + LeaseI, both production-hardened with CI gates ✓ |
| "LangGraph" | LeaseI = 8-agent LangGraph stateful system ✓ |
| "ChromaDB / vector store" | AgentProbe uses ChromaDB ✓ |
| "HITL, human-in-the-loop UX patterns" | LeaseI HITL escalation when confidence below threshold ✓ |
| "cost controls, observability, guardrails" | AgentProbe token efficiency metric + observability; LeaseI deterministic guardrails ✓ |
| "MCP (Model Context Protocol)" | In cv.md skills ✓ (nice-to-have) |
| "Python + TypeScript" | Python 8yr, TypeScript in skills ✓ |
| "Claude, GPT, Gemini, open-weight Llama" | OpenAI API, Anthropic API, Groq, Ollama in cv.md ✓ |
| "function calling, structured outputs, context management, embedding models" | In cv.md AI skills ✓ |
| Healthcare domain | AI on FHIR — NLP platform for healthcare records, HIPAA-compliant ✓ |
| "contributions to open-source AI tooling" | AgentProbe is open-source ✓ (nice-to-have) |

**Only gap:** Fine-tuning (LoRA/QLoRA, SFT, DPO) — listed as nice-to-have, not required. Not in cv.md; do not fabricate.

**ATS baseline (cv.md):** ~17/20 key terms. Patches: "evals", "cost controls", "healthcare intelligence".

---

## Block B — North Star Alignment

**Archetype: AI Engineer (production LLM systems) at healthcare intelligence company.** This is the exact archetype the user is targeting — building AI systems that work in production, not research prototypes. The healthcare domain adds a strong story layer (AI on FHIR) that most candidates won't have. The "evals-first" philosophy matches how AgentProbe was built. The "unglamorous infrastructure" framing (caching, streaming, retries, fallbacks) matches Entrata's operational reliability patterns.

---

## Block C — Compensation

$210,000 – $280,000+ base, plus meaningful equity, plus 401(k) match. This is top-of-market for an AI Engineer. No hard comp floor currently.

**Score: 5/5**

---

## Block D — Cultural Signals

- 100% remote, digital-first (user confirmed no location constraints)
- 85+ health plans, 270M lives — meaningful healthcare mission, not vaporware
- "powerfully clear ways to maximize financial outcomes and drive down healthcare costs" — healthcare cost reduction = social good framing
- Unlimited PTO, top-tier medical/dental/vision, FSA/HSA, tuition reimbursement
- "Flexible and trusting environment where you'll feel empowered" — autonomy signal
- Multiple levels hired at once ($210K-$280K+ range) — shows org depth and growth

**Score: 4.5/5**

---

## Block E — Red Flags

1. **H-1B sponsorship: UNCONFIRMED** — Machinify not in confirmed-sponsor list. EAD (OPT) likely qualifies. VERIFY before applying. If they don't sponsor, this is a long-term risk even if they hire now.

2. **Fine-tuning gap** — LoRA/QLoRA, SFT, DPO not in cv.md. Nice-to-have in JD, not required. Honest absence.

3. **"1+ year shipping LLM-based features in production"** — AgentProbe + LeaseI both qualify. The Magizhs intern experience also contributes. Low risk.

4. **Healthcare intelligence specifics** — Machinify operates in claims processing, payment integrity, utilization review. The user's healthcare story (AI on FHIR) is Python NLP, not payer-side claims. The framing will need to be healthcare AI broadly, not claims-specific.

**Adjustment: -0.3**

---

## Block F — Global Score

| Factor | Signal |
|--------|--------|
| CV match | 5.0 — LangGraph, ChromaDB, HITL, evals-first, MCP, healthcare, open-source |
| North Star | 5.0 — AI Engineer archetype, production LLM systems, exact stack |
| Comp | 5.0 — $210K-$280K+ with equity |
| Culture | 4.5 — remote, healthcare mission, autonomous environment |
| Red flags | -0.3 — H-1B unconfirmed, fine-tuning gap, claims domain gap |

**Global: 4.7/5 — APPLY immediately after verifying H-1B sponsorship**

---

## Block G — Posting Legitimacy

**High Confidence.** Extremely specific JD with named tools (LangGraph, Inngest, Temporal, pgvector, Pinecone, Turbopuffer, Weaviate, vLLM, TGI, SGLang, MCP), concrete technology opinions ("most public benchmarks are misleading"), detailed salary range, specific client scale (85 health plans, 270M lives). No ghost indicators.

---

## ATS Keywords for CV

Core additions needed:
- "evals" / "evaluation suite" — AgentProbe is exactly this
- "cost controls" / "cost-aware" — AgentProbe token efficiency metric
- "healthcare" framing — AI on FHIR + affordable housing as health-adjacent
- "streaming" — can reference LeaseI's stateful streaming pipeline
- "guardrails" — LeaseI deterministic guardrails

---

## Story Bank — STAR+R

**Evals-before-prompts story:**
- Situation: Building LeaseI — needed to measure whether LLM outputs were accurate before relying on them in a compliance context
- Task: Define what "good" means before writing a single prompt
- Action: Built AgentProbe first — eval suite with 5 metrics, CI gate, LLM-as-judge. Then evaluated every prompt variant against the harness
- Result: 93.6% precision across 1,240 test cases; CI gate catches regressions before merge
- Relevance: "Write evals before you write prompts, treat both as code"

**Unglamorous infrastructure story:**
- Situation: RabbitMQ async system at Entrata needed production-grade reliability, not just happy-path function
- Task: Build retry logic, idempotency guarantees, dead-letter handling, monitoring
- Action: Implemented the full retry/idempotency/observability stack; owned it through production incidents
- Result: System survived annual rent-schedule changes and production incidents without data corruption
- Relevance: "Build the unglamorous infrastructure that makes LLMs production-grade"

**Healthcare AI story:**
- Situation: Clinical staff couldn't query medical records in natural language — had to navigate complex FHIR API manually
- Task: Build NLP system translating natural-language queries into FHIR calls
- Action: BERT embeddings + LLM inference + HIPAA-compliant RBAC with full data isolation
- Result: ~60% reduction in manual clinical retrieval time
- Relevance: Healthcare AI domain credibility for Machinify
