# LangChain — AI Engineer

**Date:** 2026-07-25
**URL:** https://jobs.ashbyhq.com/langchain/639878f2-c0a5-4d88-89ea-3487e2623f47
**Archetype:** AI Forward Deployed / Agentic AI Engineer
**Score:** 4.6/5
**Legitimacy:** High Confidence
**Verification:** unconfirmed (batch mode)
**PDF:** output/cv-venkata-lakshmi-parimala-pasupuleti-langchain-ai-engineer-2026-07-25.pdf

---

## A — CV Match

**Score: 4.5/5**

The role asks for an AI Engineer to design and build production-grade multi-agent systems for enterprise customers using LangChain/LangGraph. Parimala's match is direct and strong:

- **LangGraph/LangChain** — AgentProbe is built on LangGraph (3-agent runtime: Orchestrator, RAG Tracer, Auto Fix) with multi-provider LLM routing (Anthropic, OpenAI, Groq, Ollama). LeaseI uses an 8-agent LangGraph pipeline. This is the core tech ask and she has production-level work in it.
- **Multi-agent systems with Subagents/Handoffs/Router patterns** — AgentProbe's Orchestrator agent uses router/conditional dispatch; LeaseI's pipeline has conditional escalation edges and HITL handoffs. Exact pattern match.
- **Evaluation frameworks + A/B testing prompts** — AgentProbe's 5-metric LLM-as-judge eval pipeline (factual accuracy, hallucination, retrieval, completeness, compliance) CI-integrated with regression gate. Direct proof point.
- **State management (short-term and long-term memory)** — LeaseI manages persistent agent state across 8-agent pipeline. AgentProbe's ChromaDB layer handles long-term retrieval state.
- **RAG pipelines + vector stores** — ChromaDB RAG in AgentProbe; TF-IDF + OCR-fallback retrieval in LeaseI; AI on FHIR used FHIR-backed embeddings.
- **Python at production quality** — 8+ years Python at Entrata (1M+ records, 100K+ MAU) + all projects in Python.
- **Enterprise customer-facing experience** — Entrata shipping production modules for enterprise property management customers, cross-functional delivery across 120+ Agile sprints.
- **Guiding customers on deployment** — cross-functional delivery experience at Entrata; built systems with quality gates, compliance controls, and documentation.

Minor gap: 5+ years of software development required (she has 8+) and 2+ years AI/ML specifically (she has ~2 years of active AI work). The 2-year AI requirement is tight given her AI work started ~2024, but AgentProbe + LeaseI + Entrata's production AI pipeline cover it.

No Go/Rust/C++ requirement. Python + TypeScript are in scope. No clearance needed.

---

## B — North Star Alignment

**Score: 4.8/5**

LangChain is *the* company for this archetype. Their products are LangGraph, LangSmith, and LangChain — the exact tools Parimala uses daily. Working here means:

- Building multi-agent systems using her exact stack
- Exposure to the broadest set of enterprise agent engineering patterns
- Working directly on the platform her projects are built on — massive credibility signal
- The GTM/AI Engineer hybrid role (customer-facing + building) maps exactly to her Forward Deployed / Applied AI Engineer archetype

Boost applied: +0.3 for role at a company building agentic AI products (LangChain is explicitly on the boost list). +0.3 for LangChain/LangGraph/multi-agent core match. These boosts are captured in the global score.

---

## C — Compensation

**Score: 4.0/5**

Reported range: $160K–$180K + equity. This is above Parimala's $100K–$140K target — she is well within range and the role pays above her ceiling, which is a strong positive signal. The "no longer accepting applications" flag on one source was from a mirror/cache; the canonical Ashby URL is active per search results. Equity at LangChain (Series B, $125M raised from IVP/Sequoia/Benchmark/CapitalG/Sapphire) has meaningful upside.

---

## D — Cultural Signals

**Score: 4.5/5**

- **Series B, $125M raised** — well-funded, not early-stage risk; stable enough to deliver on roles
- **Mission-driven** — "make intelligent agents ubiquitous" — aligns with her work in agentic systems
- **Remote acceptable** — "SF or NYC preferred; US remote acceptable" — Virginia remote works
- **GTM department** — AI Engineer sits in GTM; customer-facing and product-shaping role, not pure support
- **Founding team credibility** — built by the LangChain founders; technical culture, not sales-led
- Possible concern: "SF or NYC preferred" may create bias toward local candidates in interviews; however role is US remote eligible

H-1B sponsorship: no explicit mention in posting. LangChain is a well-known tech company with prior H-1B sponsorships. Uncertain — flag for Parimala to confirm before applying.

---

## E — Red Flags

**Score: 4.0/5**

- **Visa sponsorship not confirmed** — this is the main risk. The job posting does not mention H-1B sponsorship, and one cached source noted "unable to sponsor" language. Parimala must confirm sponsorship before investing time in application.
- **"No longer accepting applications"** seen on one third-party mirror — verify the canonical Ashby URL is still active before applying.
- **2+ years AI/ML requirement** — she is on the edge; make sure AgentProbe + LeaseI timeline (2024–present) is clearly dated in application.
- No clearance, no Go/Rust, no infra/GPU hard blocks.

---

## F — Global Score

**4.6/5** — Strong match. Role archetype, tech stack, and proof points align tightly. LangChain is on the explicit boost list. Compensation exceeds her target. The only meaningful risk is visa sponsorship uncertainty — confirm this first. If sponsorship is available, this is a top-priority application.

**Recommend applying** — with visa sponsorship confirmation as the go/no-go gate.

---

## G — Posting Legitimacy

**High Confidence**

- Canonical Ashby URL returned in multiple independent searches with current job metadata
- Company is well-known, verifiable (Series B, multiple active job postings)
- JD is technically specific with real skills (LangGraph, subagent patterns, eval frameworks, A/B testing)
- Multiple independent sources corroborate the $160K–$180K salary range
- "No longer accepting applications" flag appears only on a third-party cache (Lux Capital job board), not on the canonical Ashby URL — likely stale cache, not a closing signal

---

## Interview Prep Notes

**Strongest proof points to lead with:**
1. AgentProbe — 3-agent LangGraph runtime, 5-metric eval engine (factual accuracy, hallucination, retrieval, completeness, compliance), CI-integrated, 100% local — this is a direct portfolio demo of what the job does
2. LeaseI — 8-agent LangGraph HITL pipeline, conditional escalation edges, 93.6% precision — shows enterprise-grade multi-agent design
3. Entrata production AI pipeline — 1.6M records, quality gates, output validation — shows production rigor

**Likely interview topics:**
- Walk through a multi-agent architecture you designed: routing logic, state management, failure modes
- How do you evaluate LLM agents in production? (answer: AgentProbe's 5-metric eval pipeline)
- How do you handle non-determinism in agent outputs? (answer: HITL design in LeaseI, regression gate in AgentProbe)
- Customer scenario: enterprise client wants to add memory to their agent — how do you architect it?

**Framing tip:** Position AgentProbe as a live demo of the exact work this role involves. Offer to walk through the codebase in the technical screen.
