# Evaluation: Capital One — Lead AI Engineer (AI Foundations)

**Date:** 2026-07-30
**URL:** https://capitalonecareers.com/job/-/-/234/98436292208
**Archetype:** AI Platform / LLMOps + Agentic / Automation
**Score:** 3.5/5
**Legitimacy:** High Confidence
**PDF:** output/capital-one-lead-ai-engineer-2026-07-30.pdf

---

## A) Role Summary

| Dimension | Detail |
|-----------|--------|
| **Archetype** | AI Platform / LLMOps (primary) + Agentic / Automation (secondary) |
| **Domain** | Foundation model training, GenAI platform engineering, LLM inference |
| **Function** | Build — IC contributor on internal GenAI infrastructure |
| **Seniority** | Lead (Capital One-specific = Senior IC, not Staff — confirmed by insider) |
| **Location** | Hybrid — McLean VA / Cambridge MA / NYC / San Jose CA |
| **H-1B** | Confirmed sponsor |
| **Comp** | $197K–$245K |
| **TL;DR** | Build the GenAI platform and agentic AI infrastructure that all Capital One engineers use internally — foundation models, LLM inference, eval tooling, agent orchestration |

---

## B) Match with CV

**Strong matches:**

| JD Requirement | CV Evidence | Strength |
|----------------|-------------|----------|
| Multi-agent orchestration (LangGraph) | AgentProbe 3-agent LangGraph runtime (Orchestrator, RAG Tracer, Auto Fix); LeaseI 8-agent StateGraph; Magizhs LangGraph stateful graph | Strong |
| LLM evaluation frameworks | AgentProbe CI-integrated 5-metric LLM-as-judge eval engine (factual accuracy, hallucination, retrieval, completeness, compliance) | Strong |
| RAG pipelines | ChromaDB RAG (AgentProbe), hand-rolled TF-IDF cosine similarity (LeaseI), 100% citation correctness | Strong |
| Multi-provider LLM routing | AgentProbe: Anthropic/OpenAI/Groq/Ollama dynamic routing | Strong |
| FastAPI backend at scale | 15-endpoint FastAPI (AgentProbe) + Entrata production backend 100K+ MAU | Strong |
| Observability / tracing | AgentProbe React dashboard: per-run metrics, regression drift, latency, retrieval quality | Medium |
| AWS infrastructure | Entrata S3/EC2/RDS/Glue, 100K+ MAU, 100% PHI compliance migration | Medium |
| PyTorch | Entrata production AI pipeline (1.6M records, custom neural network); CrashClarity | Medium-light |
| Python | Primary language across all roles and projects | Strong |

**Gaps and mitigations:**

| Gap | Hard blocker? | Adjacent experience | Mitigation |
|-----|---------------|---------------------|------------|
| Foundation model pre-training / fine-tuning | Near-blocker | Entrata PyTorch pipeline builds a custom NN for data transformation (not a foundation model) | Frame as "custom neural network for domain data transformation at 1.6M-record scale with production compliance gates" — don't overclaim |
| LLM inference serving at scale (vLLM, TensorRT) | Moderate | AgentProbe routes to API providers — orchestration, not serving infrastructure | "Multi-provider routing with fallback" is a real skill; acknowledge API-layer vs serving-layer honestly |
| Distributed training / GPU cluster management | Moderate | No direct evidence | Don't claim it; position as adjacent to infra-layer engineers on the team |
| Internal developer platform engineering (1000s devs) | Moderate | Entrata's service-based architecture revamp: designed for other engineers to consume | Reframe as "platform thinking for internal consumers" |

**Bottom line:** Agentic + eval + RAG side maps very well. Foundation model / inference infrastructure gap is real — candidates with production LLM serving pipelines at financial-institution scale will be in this pool.

---

## C) Level and Strategy

**Level reality check:** Capital One Lead = Senior IC (confirmed insider). Salary ($197K–$245K) maps to L5/L6 at major tech. Competition includes engineers who have shipped LLM inference pipelines in production.

**"Sell senior without lying" plan:**
- Open with the eval + observability angle — AgentProbe's CI-integrated 5-metric eval engine is a genuine differentiator. Most candidates have used eval frameworks; Parimala built one.
- Frame LeaseI's 8-agent StateGraph + HITL as production-grade agentic design — conditional routing, escalation logic, and safety boundary are platform-engineer decisions.
- Frame Entrata's PyTorch pipeline as "takes AI from notebook to production with compliance gates and output validation."
- Acknowledge inference infra gap proactively: "I've worked at the orchestration + eval layer; I ramp infrastructure concerns quickly."

**"If they downlevel me" plan:**
Capital One doesn't have a direct Senior Associate AI track. Negotiate 6-month review with clear Lead promotion criteria if downleveled.

---

## D) Comp and Demand

| Item | Data |
|------|------|
| Offered range | $197K–$245K |
| Market for Senior AI Engineer at Capital One | $180K–$230K base (financial services premium) |
| H-1B sponsorship | Confirmed |
| Comp vs Parimala target ($100K–$140K) | 40–75% above target — excellent outcome if offer lands |
| Comp score | 5/5 |
| Demand signal | Capital One IFX team actively building; AI infrastructure at Tier-1 financial firms = high-demand, slow-to-fill |

---

## E) Customization Plan

| # | Section | Current | Proposed | Why |
|---|---------|---------|---------|-----|
| 1 | Summary | "dual-mode AI platform" | Lead with: "Built LangGraph multi-agent evaluation infrastructure (AgentProbe: 5-metric CI-integrated eval engine, multi-provider routing; LeaseI: 8-agent StateGraph with conditional HITL)" | IFX eval + agentic framing first |
| 2 | LeaseI bullet | Phase 1 citation correctness lead | Lead with: "8-agent LangGraph StateGraph with real conditional edges, confidence-gated HITL escalation, and root-cause tracing across settings + release history" | Platform/infra framing over domain framing |
| 3 | AgentProbe bullet | "15-endpoint FastAPI" lead | Lead with: "CI-integrated 5-metric LLM-as-judge eval engine — factual accuracy, hallucination, retrieval, completeness, compliance — every commit scored, regressions blocked before merge" | Eval-platform angle IFX will care about |
| 4 | Entrata AI Pipeline | "custom neural network" | Add: "output validation, quality gates, and compliance controls — production AI, not prototyping" | Signals production rigor without overclaiming |
| 5 | Skills | PyTorch buried | Move PyTorch + TensorFlow higher under ML; add "LLM inference routing (Anthropic/OpenAI/Groq/Ollama)" explicitly | Matches IFX stack signals |

---

## F) Interview Plan

| # | JD Requirement | Story | Situation | Task | Action | Result | Reflection |
|---|----------------|-------|-----------|------|--------|--------|------------|
| 1 | Ship reliable AI systems in production | Entrata AI Pipeline | AI operations still manual-Excel at 1.6M-record scale | Build first production AI pipeline with compliance gates | PyTorch + OpenAI API + output validation + quality gates | Zero compliance violations at launch | Should have documented the validation schema earlier; it became the de facto standard |
| 2 | Build and maintain eval frameworks | AgentProbe eval engine | No CI-integrated eval existed for LLM agents | Build 5-metric eval that runs on every commit | LLM-as-judge scoring + GitHub Actions integration | Every commit scored; regressions blocked before merge | LLM-as-judge is slow — learned to cache reference answers to cut CI time |
| 3 | Multi-agent orchestration + HITL | LeaseI 8-agent graph | Support tickets being diagnosed manually by engineers | Design investigation pipeline: Triage → Retrieval → Config → History → Reasoning → Validation → Escalation | 8-agent LangGraph StateGraph, conditional edges, confidence-gated HITL | Correctly traces false-ineligibility to misconfigured setting + release tag | Built HITL in from the start — much harder to retrofit after agents are deployed |
| 4 | Safety + guardrails in GenAI systems | LeaseI Tenant Self-Service + Magizhs FAA | Tenants asking eligibility questions; AI risk of wrong answer | Design hard safety boundary: regulated decisions always route to staff | Guardrails enforced in code + routing layer; FAA altitude/battery/no-fly-zone checks | 0 safety boundary violations in eval | Defense in depth: guardrails at prompt layer AND routing layer both needed |
| 5 | Production systems at scale | Entrata 100K+ MAU, 99.5% uptime | 6-year production system serving property managers | Maintain uptime while shipping 20+ modules | Docker containerization (50% execution time cut), SQL tuning 200+ queries (30% gain), PHI compliance | 6 consecutive months below 10 bugs | Uptime is a cultural decision — on-call discipline matters as much as code quality |
| 6 | AWS cloud infrastructure | Entrata AWS S3 migration | 100K+ resident sensitive records needed migration | Encrypt and migrate with zero data loss, zero compliance violations | Libsodium encryption, 100% of SSNs/phones, updated 50%+ of codebase | 100% PHI compliance, zero security incidents | Start with encryption schema before migration — retrofitting costs 3x |

**Red-flag Q&A:**

*"All your AI experience is in personal projects — how do we know it's production-ready?"*
> "LeaseI and AgentProbe are designed to the same standard as my Entrata work — compliance gates, output validation, HITL escalation, CI-integrated evals. The domain differs but the rigor is the same. AgentProbe blocks regressions on every commit — that's production discipline, not prototyping."

*"Why apply for AI Foundations — you seem more product-facing than infra?"*
> "The eval layer and the orchestration layer are where I'm strongest, and that's core to what IFX is building. I'm ramping the serving-infrastructure side — I learn systems concerns fast, and I bring the agentic + eval depth your infra-only engineers often don't have."

*"You were at Entrata for 8+ years — single employer. How do we know you can adapt?"*
> "Entrata grew from startup to 100K+ MAU SaaS during my tenure — I adapted to microservices, containerization, cloud migration, and AI adoption as each wave hit. That's not one employer, it's one company going through four architectural generations."

**Recommended case study:** AgentProbe. Lead with the CI-integrated eval pipeline — directly relevant to what IFX builds internally.

---

## G) Posting Legitimacy

| Signal | Finding | Weight |
|--------|---------|--------|
| Posting freshness | Recently posted | Positive |
| Company hiring signals | Capital One IFX actively hiring AI engineers (confirmed LinkedIn + insider) | Positive |
| Apply button state | Active | Positive |
| H-1B sponsorship | Explicitly stated | Positive |
| Role-company fit | Tier-1 financial institution building internal GenAI platform — coherent and expected | Positive |
| Description quality | Specific: team name (IFX), salary range, locations, technical stack | Positive |

**Assessment: High Confidence** — Real, active opening.

---

## Machine Summary

```yaml
company: Capital One
role: Lead AI Engineer (AI Foundations)
date: 2026-07-30
score: 3.5
archetype: AI Platform / LLMOps + Agentic / Automation
legitimacy: High Confidence
compensation: "$197K–$245K"
h1b: confirmed
location: Hybrid (McLean VA / Cambridge MA / NYC / San Jose CA)
verdict: conditional_apply
key_gap: foundation model training + LLM inference serving at scale
key_strength: LangGraph multi-agent + CI eval engine + RAG pipelines
```

---

## Keywords extracted

LangGraph, multi-agent orchestration, LLM evaluation, LLM-as-judge, RAG pipelines, ChromaDB, FastAPI, foundation model, LLM inference, PyTorch, AWS, observability, agentic AI, HITL, guardrails, GenAI platform, multi-provider routing, CI/CD, production AI, eval framework
