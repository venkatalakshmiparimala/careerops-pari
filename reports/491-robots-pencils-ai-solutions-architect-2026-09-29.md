# Evaluation: Robots & Pencils — AI Solutions Architect (IC)

**Date:** 2026-09-29
**URL:** (not provided — paste URL here)
**Archetype:** AI Solutions Architect + AI Platform/LLMOps
**Score:** 4.0/5
**Legitimacy:** High Confidence
**PDF:** output/491-robots-pencils-ai-solutions-architect-2026-09-29.pdf

---

## A) Role Summary

| Dimension | Detail |
|-----------|--------|
| Archetype | AI Solutions Architect (primary) + AI Platform/LLMOps (secondary) |
| Domain | Enterprise AI consulting — 30-45 day production delivery cycles |
| Function | Build + Architect — LLM apps, agentic systems, RAG, eval, LLMOps |
| Seniority | Senior IC Architect (7+ YOE, 3+ in AI/ML architecture) |
| Remote | Likely remote (no office mentioned; company is distributed) |
| Team size | Consulting firm; multi-engagement IC contributor |
| TL;DR | Design and deliver production AI systems for enterprise clients — agentic orchestration, RAG strategy, LLMOps standards, eval pipelines — as a senior IC architect who also mentors and sets team standards. |

---

## B) Match with CV

| JD Requirement | CV Match | Strength |
|----------------|----------|----------|
| Multi-agent orchestration (LangGraph) | LeaseI: 8-agent LangGraph StateGraph with durable state, conditional routing, HITL escalation | Exact |
| RAG and context-engineering strategy | LeaseI: hybrid TF-IDF + semantic reranking, citation grounding, chunking strategy, section-aware ingestion | Strong |
| Eval pipelines, LLM-as-judge, offline + online eval | AgentProbe: 5-metric eval engine, golden datasets, CI regression harness, LLM-as-judge scoring, online + offline loops | Exact |
| Prompt versioning, LLMOps standards | AgentProbe: multi-provider routing, prompt version management across OpenAI/Anthropic/Groq/Ollama | Strong |
| Guardrails, observability, tracing | LeaseI: HITL escalation gate, deterministic compliance boundary, hallucination prevention by design; AgentProbe: hallucination rate tracking | Strong |
| Responsible AI — PII, data isolation, prompt-injection defense | Entrata: 100% PHI compliance, Libsodium-encrypted pipelines, zero security incidents; LeaseI: LLM never auto-decides regulated calls | Strong |
| Fine-tuning vs prompting vs RAG tradeoffs | LeaseI: chose hand-rolled TF-IDF RAG over LangChain (controllability > speed); GMU: fine-tuned HuggingFace/PyTorch classification model | Moderate |
| Python + one other language | Python (primary), PHP/Java/TypeScript (Entrata), C# 1.5yr | Strong |
| Cloud-native architecture (AWS, microservices, containers) | AWS S3/Bedrock/Lambda; Docker/Kubernetes; microservices redesign at Entrata | Strong |
| AI-forward tools (Claude, Cursor) | Active Claude Code user; building with Anthropic API | Strong |
| Mentoring junior/mid engineers | Mentored 5+ at Entrata; 300+ peer code reviews; GMU TA (600+ students) | Strong |
| 7+ years SWE | 8+ years (Jan 2017 – present) | Strong |

**Gaps:**

| Gap | Type | Mitigation |
|-----|------|------------|
| "3 years AI/ML architecture leadership" | Real gap — she has ~2 years of focused AI project work, not enterprise AI architect role | Frame project-level architectural decisions (LeaseI 8-agent design, AgentProbe build-vs-buy) as architecture decision ownership |
| Model serving/inference optimization (streaming, quantization, batching, caching at scale) | Real gap — no production model serving infrastructure ownership | AWS Bedrock experience + streaming inference in AgentProbe; honest acknowledgment in interviews |
| AWS AI certifications | Nice-to-have — not a blocker | Frame GMU MS + live open-source projects as equivalent signal |
| Multi-engagement consulting (30-45 day cycles) | New context | Entrata: shipped production modules on compressed Agile sprint cadence across 8 years |

---

## C) Level and Strategy

**Level:** Senior IC Architect — this is not a people-manager role. IC contributor who sets standards and mentors through technical influence.

**Sell strategy:**
- Lead with: "I've designed multi-agent architectures, built eval pipelines from scratch, and shipped production AI in compressed timelines. LeaseI went from problem statement to production with a regression harness in under 3 months."
- On architecture experience gap: "My AI architecture experience is project-level, not enterprise-title-level. But the actual decisions I've made — 8-agent stateful orchestration, build-vs-buy on RAG, deterministic compliance boundary design — are the decisions your clients need."
- On model serving gap: "My serving experience is via AWS Bedrock and streaming inference patterns in AgentProbe. I'd lean on your team on quantization and batching at scale while contributing immediately on orchestration, eval, and RAG."

**What makes her compelling for a consulting firm:**
- AgentProbe is open-source and public — signals she ships and stands behind her work
- LeaseI framing: designed 3 surfaces sharing one evidence model — that's the kind of system architecture thinking consulting clients pay for
- She can talk to non-engineers (GMU TA, faculty presentations, 300+ code reviews communicating technical decisions)

---

## D) Comp and Demand

| Item | Detail |
|------|--------|
| Stated range | $146,071 – $201,541 USD |
| Comp score | 4/5 — above target range; strong for IC |
| Benefits | Unlimited PTO, medical/dental/vision, 401k |
| H-1B | Robots & Pencils is a Canadian company (HQ Toronto); US roles may offer TN visa or H-1B; verify at first contact |

---

## E) Customization Plan

| # | Section | Current | Proposed Change | Why |
|---|---------|---------|-----------------|-----|
| 1 | Summary headline | Generic AI engineer | "AI Solutions Architect · LangGraph · RAG · LLMOps · Eval Pipelines · Responsible AI · Python · AWS" | Matches archetype keywords exactly |
| 2 | Summary | Production engineer framing | Lead with architectural decisions: "I've designed 8-agent orchestration architectures, defined RAG strategy (build-vs-buy), and built the LLMOps eval infrastructure to keep non-deterministic systems reliable in CI" | This is what the JD pays for |
| 3 | LeaseI | Support investigation framing | Reframe as architectural case study: 3-surface platform on one evidence model; 8-agent StateGraph design decisions; why HITL gate + deterministic boundary; build-vs-buy on RAG | Shows architectural thinking, not just coding |
| 4 | AgentProbe | Eval toolkit | Add: "defined LLMOps standards — prompt versioning, eval pipelines, CI/CD for AI workloads, offline + online eval loops, LLM-as-judge scoring" | Direct JD language match |
| 5 | Skills | Broad | Add to front: "AI Solutions Architecture, LLMOps, Responsible AI, Prompt-Injection Defense, Grounding Controls, Eval Pipelines" | ATS keyword coverage |

---

## F) Interview Plan

| # | JD Requirement | Story | S | T | A | R | Reflection |
|---|----------------|-------|---|---|---|---|------------|
| 1 | "Define AI system architecture, lead design across LLM applications" | LeaseI 3-surface architecture | Needed one platform serving 3 different user types (support engineers, tenants, staff) — couldn't build 3 separate systems | Design a shared evidence model serving all 3 surfaces with different safety profiles | 3-surface architecture sharing one SQLite knowledge repository; different safety boundaries per surface (staff can escalate, tenant agent never auto-decides eligibility) | 93.6% precision on 1,240 test cases; zero false AI auto-decisions on regulated calls | The hardest architectural decision was the safety boundary — where does AI authority end and human authority begin? That question should be answered in the architecture, not left to prompt engineering |
| 2 | "Drive RAG and context-engineering strategy, hybrid retrieval, reranking" | LeaseI RAG build-vs-buy decision | Standard LangChain RAG with vector DB was available; cost and controllability concerns | Evaluate whether to use standard tooling or build hand-rolled retrieval | Built TF-IDF + semantic reranking without LangChain — no API costs, no vendor dependency, full citation-grounding control | 100% citation correctness on Phase 1 eval set; zero unsupported-claim rate | Build-vs-buy on RAG is a context-engineering question, not just a cost question — when citation correctness is a compliance requirement, controllability > convenience |
| 3 | "Define LLMOps and MLOps standards, eval pipelines, prompt versioning, CI/CD" | AgentProbe as LLMOps standard | No reusable eval methodology across LLM projects; no way to regression-test in CI | Build a reusable LLMOps toolkit that defines standards | 5-metric engine, golden datasets, CI regression harness, prompt version management, multi-provider routing, LLM-as-judge | Teams evaluate LLMs locally at zero cost; regression failures surface before merge | The discipline of "define your eval metrics before writing your first prompt" is the hardest part to instill in teams |
| 4 | "Responsible AI — PII, data isolation, prompt-injection defense, grounding" | Entrata PHI compliance | 100K+ housing units with PHI documents migrating to AWS S3 | Design migration with full PHI compliance — zero data exposure | Libsodium-encrypted pipelines, multi-tenant data isolation at the storage layer, access controls per record type | 100% PHI compliance, zero security incidents across full migration | Data isolation is an architecture decision, not a feature — if it isn't in the schema and the access layer from day one, you're patching it forever |
| 5 | "Fine-tuning vs prompting vs RAG tradeoffs" | GMU fine-tuning + LeaseI RAG | Different problems demand different approaches — had to make the call on both | Choose and justify approach on two separate projects | LeaseI: RAG (domain documents, citation required, no training data); GMU: fine-tuning (classification, fixed label space, labeled data available) | Both performed at target accuracy; LeaseI in production, GMU deployed to Quart inference API | Fine-tuning is the right call when you have labeled data and a fixed output schema; RAG is right when the knowledge changes or citation is required; prompting alone when the task is reasoning, not retrieval |

**Recommended case study:** LeaseI architecture decision session — specifically "3 surfaces, one evidence model, different safety profiles" — this is the kind of thinking enterprise clients pay consulting firms for.

**Red-flag questions:**
- *"You don't have 3 years of formal AI architecture title experience."*
  → "I have the architectural decisions. LeaseI: 8 agents, stateful orchestration, HITL gate, citation-grounded RAG — those are architecture decisions I made and own. AgentProbe: defined LLMOps standards from scratch. The title was 'Senior Software Engineer' and 'Research Associate' — the work was AI architect work."
- *"Do you have H-1B/work authorization?"*
  → "I'm on F-1 STEM OPT (3 years). I'd want to confirm your US sponsorship path — are you able to support H-1B, TN, or O-1?"

---

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|--------|---------|--------|
| Description quality | Specific technologies (LangGraph, Bedrock Agents, AgentCore), clear responsibilities, defined comp range | Positive |
| Salary disclosed | $146K–$201K stated — serious posting | Positive |
| Company reputation | Robots & Pencils is a well-known AI consulting firm (founded 2011, 300+ employees) | Positive |
| Role-company fit | AI consulting firm building 30-45 day production AI = exactly this role | Positive |
| Requirements realism | 7+ YOE + 3 AI architecture years is achievable; no unrealistic contradictions | Positive |

---

## Keywords Extracted (ATS)

AI Solutions Architect, LLM applications, agentic systems, multi-agent orchestration, LangGraph, Amazon Bedrock, RAG, hybrid retrieval, reranking, context engineering, LLMOps, MLOps, eval pipelines, LLM-as-judge, prompt versioning, CI/CD, guardrails, observability, responsible AI, prompt-injection defense, grounding, fine-tuning, model serving, AWS, Python, TypeScript, cloud-native, microservices, containerization, technical mentoring

---

## Machine Summary

```yaml
role: AI Solutions Architect (IC)
company: Robots & Pencils
score: 4.0
archetype: AI Solutions Architect + AI Platform/LLMOps
location: Remote (distributed consulting firm)
salary_range: $146071-$201541
sponsorship: uncertain — Canadian HQ, verify TN/H-1B/O-1 path at first contact
top_proof_points:
  - LeaseI: 3-surface architecture + 8-agent LangGraph design decisions
  - AgentProbe: LLMOps standards (eval pipelines, prompt versioning, CI/CD)
  - Entrata: PHI compliance + responsible AI data isolation
  - GMU: fine-tuning decision (vs RAG) — build-vs-buy tradeoff ownership
key_gaps:
  - "3 years AI/ML architecture leadership" — gap; mitigate with project-level decisions
  - model serving/inference optimization at scale — real gap
  - consulting multi-engagement context — new
recommendation: user override — apply. Frame as IC architect role; lead with architectural decision ownership not title
```
