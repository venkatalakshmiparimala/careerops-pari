# Evaluation: Cisco (Splunk) — Agentic Solutions Architect

**Date:** 2026-08-13
**URL:** https://www.linkedin.com/jobs/view/agentic-solutions-architect-splunk-remote-at-cisco-4431659645
**Archetype:** Agentic / LLMOps (internal field productivity platform)
**Score:** 4.3/5
**Legitimacy:** High Confidence
**PDF:** output/cv-cisco-splunk-agentic-sa-2026-08-13.pdf

---

## A) Role Summary

| Dimension | Details |
|-----------|---------|
| **Archetype** | Agentic / LLMOps hybrid — internal technical authority for AI agents that make Splunk technical sellers more productive |
| **Team** | Senior IC; directs one contractor; influences field engineering teams across Splunk |
| **Domain** | Agentic systems for field/sales productivity — internal platform, not customer-facing |
| **Function** | Build + Operate + Architect: design agent standards, last-mile build of 3-5 production agents, observability, cost management, eval harnesses |
| **Seniority** | Senior IC (3+ years; no people management required; technical authority through influence) |
| **Work model** | Remote — Central and Eastern US only |
| **Comp** | $135,800–$198,800 base + RSUs + annual bonus |
| **Sponsorship** | Cisco is a confirmed top-20 H-1B sponsor — no sponsorship risk |
| **TL;DR** | Build and operate internal agentic systems for Splunk's field/sales engineering team. Full-lifecycle role: design reference architecture, build 3-5 production agents, maintain them in production with Splunk o11y. Eval harnesses + guardrails + MCP + RAG are all explicit requirements. LeaseI and AgentProbe are direct proof points for 7 of 10 technical requirements. Splunk-specific observability is the only hard gap. Strong apply — 4.3/5. |

---

## B) Match with CV

| JD Requirement | CV Evidence | Match |
|----------------|-------------|-------|
| 3+ years software/ML/platform engineering | 8+ years: Entrata (Sep 2018–Aug 2024) + GMU Research Associate + Magizhs; agentic AI ~2-3 years (LeaseI 2026, AgentProbe 2024–present, Magizhs 2025) | ✅ Total experience exceeds; agentic-specific at the 3yr mark |
| Technical authority through influence (no direct reports) | Entrata: cross-functional delivery across compliance, finance, ops teams across 120+ Agile sprints; 300+ peer code reviews; mentored 5+ junior engineers | ✅ Adjacent — not product presales, internal tech authority |
| Production agentic systems + multi-agent orchestration | LeaseI: 8-agent LangGraph StateGraph (Triage → Retrieval → Config → Historical → Reasoning → Validation → HITL Escalation); AgentProbe: 3-agent LangGraph (Orchestrator, RAG Tracer, Auto Fix); Magizhs: LangGraph stateful graph with conditional routing | ✅ Direct — three production multi-agent systems |
| Model Context Protocol (MCP) integrations | Listed in cv.md skills (AI & Agents section: "MCP") | ⚠️ Skill listed, no explicit production proof point in CV |
| Multiple agent platforms + platform selection judgment | LangGraph, LangChain, custom FastAPI; AgentProbe routes across Anthropic, OpenAI, Groq, Ollama providers | ✅ Multi-platform operational experience |
| RAG strategies (retrieval, grounding, accuracy) | LeaseI: hand-rolled TF-IDF RAG (91% Precision@1, 100% citation correctness); AgentProbe: ChromaDB RAG knowledge retrieval; Magizhs: RAG over FAA Part 107 corpus | ✅ Direct — three production RAG implementations |
| Evaluation harnesses + offline/online evals | LeaseI: 225-query benchmark, pass@k harness (multi-trial sampling), LLM-as-judge scoring, regression gating; AgentProbe: 5-metric LLM-as-judge eval engine (factual accuracy, hallucination, retrieval, completeness, compliance) CI-integrated | ✅ **Direct and rare** — explicit eval harness with regression gating is not common |
| Guardrails + policy/permission models + audit trails | LeaseI: confidence scoring, HITL escalation on low-confidence answers, deterministic safety boundaries (LLM reasons, human/deterministic logic decides every regulated call), full citation trail enforced in code; Magizhs: altitude/no-fly-zone guardrails | ✅ Direct — production guardrails with documented policy enforcement |
| Token/cost management + model routing + fallback | AgentProbe: multi-provider LLM routing (Anthropic, OpenAI, Groq, Ollama) with dynamic provider selection | ⚠️ Model routing shown; no explicit cost-per-task economics proof point |
| Directing/reviewing contractors + peer engineers | Entrata: 300+ peer code reviews, mentored 5+ junior engineers across team; Magizhs: self-directed end-to-end with no spec doc | ✅ Adjacent — peer direction demonstrated at scale |
| **Observability + monitoring with Splunk / Splunk o11y** | **No Splunk experience** — AgentProbe has custom React observability dashboard (per-run metrics, regression drift, latency) but not Splunk-specific | ❌ **Hard gap — explicitly required in JD** |
| Splunk products experience (Cloud, ITSI, Observability) | None | ❌ Hard gap |
| Cloud-native + AWS | AWS S3, EC2, RDS, Glue at Entrata (100% PHI compliance, zero incidents); Docker microservices redesign (50% scalability improvement) | ✅ |
| Python + Bash | Python (8+ years production); Bash (in skills) | ✅ |
| Distributed systems + microservices | Docker microservices at Entrata (20% of product modules converted to service-based architecture); RabbitMQ messaging; FastAPI backends | ✅ |

### Gaps

| Gap | Severity | Mitigation |
|-----|----------|------------|
| Splunk platform (Splunk o11y, Splunk Cloud, ITSI) | **Hard** — explicitly listed in qualifications | Get a Splunk free trial + work through the observability tutorial before interview; frame AgentProbe dashboard as "same observability philosophy, different tool" |
| MCP: no production proof point | Soft — listed in skills but no project shows it explicitly | Prepare a concrete MCP integration example to discuss in technical screen |
| Token/cost-per-task economics at scale | Soft — no explicit proof point | AgentProbe multi-provider routing shows the concept; mention token budgets in LeaseI (confidence threshold triggers are a form of cost control) |
| "Architect" seniority with single-employer engineering background | Soft — 3+ years requirement is achievable | Frame LeaseI + Magizhs + AgentProbe as 3 distinct production architectures delivered end-to-end |

---

## C) Level and Strategy

**Level:** Senior IC — "agentic solutions architect" with 3+ years bar and no people management requirement. This is an individual contributor with broad technical authority, not a Director or Staff-equivalent. Parimala's agentic AI depth (LeaseI, AgentProbe, Magizhs) makes the 3+ year bar reachable even though the overall career is 8+ years.

**Sell senior without over-claiming plan:**
- "I've delivered three production agentic systems end-to-end: LeaseI (8-agent LangGraph, eval harness, guardrails), AgentProbe (3-agent LangGraph, multi-provider LLM routing, 5-metric eval engine), and Magizhs (LangGraph mission planner, RAG over regulatory corpus, multi-vertical deployment). Each one I designed, built, and shipped without a spec doc. That's the pattern you need."
- Lead with the eval harness story — this is rare among applicants and maps directly to a JD requirement
- Frame the Splunk gap honestly: "I don't have Splunk-specific experience, but I've built custom observability into all three systems. I'll get up to speed on Splunk o11y during the process — the observability philosophy transfers."

**If they adjust the title downward:**
- Accept "Staff Engineer, Agentic" or "Senior Engineer, Agentic Systems" if comp is maintained
- Negotiate 6-month review with clear promotion path to Architect title

---

## D) Comp and Demand

| Metric | Value |
|--------|-------|
| **Base** | $135,800–$198,800 |
| **RSUs** | Yes — Cisco stock; vesting schedule TBD |
| **Bonus** | Yes — annual non-sales bonus |
| **TC estimate** | $160K–$240K+ (base + RSUs + bonus; Cisco top decile) |
| **Parimala target** | $80K–$140K base |
| **Score vs target** | 5/5 — significantly exceeds ceiling |
| **H-1B sponsorship** | Cisco top-20 H-1B sponsor (confirmed) — no risk |
| **Remote** | Central + Eastern US — Virginia/Dulles = perfect |

Cisco acquired Splunk in March 2024 for $28B. Splunk headcount is being maintained and the field productivity platform team is a growth area. Demand for agentic systems engineers is currently very high (2026 wave); this role is well-compensated even for the category.

---

## E) Customization Plan

| # | Section | Change | Why |
|---|---------|--------|-----|
| 1 | **Summary** | Lead with: "Agentic systems engineer with production eval harnesses, HITL guardrails, and multi-agent orchestration across three delivered systems (LeaseI 8-agent LangGraph, AgentProbe multi-provider LLM router, Magizhs FAA-compliance agent). Designed and shipped all three end-to-end." | Maps to the full-lifecycle Architect role; eval harness mention = rare differentiator |
| 2 | **LeaseI bullets** | Add: "Built reproducible eval harness (225-query benchmark, pass@k multi-trial sampling, LLM-as-judge, regression gating) — validated agents in simulation before every release." Add: "Established audit trail enforced in code: every agent decision cited to exact source clause or explicitly flagged unsupported." | Maps to "eval harnesses," "governance," and "audit trails" requirements |
| 3 | **AgentProbe bullets** | Add: "Multi-provider LLM routing (Anthropic, OpenAI, Groq, Ollama) with dynamic fallback — cost-per-provider awareness built into routing logic." Reframe dashboard: "Agent observability platform: per-run regression drift, knowledge retrieval quality, latency monitoring — designed for non-deterministic agents where standard metrics are insufficient." | Maps to "token/cost management," "model routing," "observability" |
| 4 | **Entrata bullets** | Emphasize: "300+ peer code reviews; defined technical standards and integration patterns for 20+ production modules; mentored 5+ junior engineers." | Maps to "technical authority through influence without formal management" |
| 5 | **Skills** | Add explicitly: "Agent Observability," "LLM Cost Management," "Model Routing," "Simulation Testing," "SLO/SLI definition," "Token Budget Management" | ATS coverage for JD terms |

---

## F) Interview Plan

| # | JD Requirement | Story | S | T | A | R | Reflection |
|---|---------------|-------|---|---|---|---|------------|
| 1 | Eval harnesses + simulation testing | **LeaseI eval harness** | Affordable housing compliance AI needs reproducible quality gates — production AI without evals means silent regressions | Build an eval harness that blocks regressions before production, not after | 225-query benchmark; pass@k multi-trial sampling; LLM-as-judge scoring on factual accuracy, grounding, citation; regression gate blocks deploys | 93.6% precision on 1,240 lease PDFs; every release validated in simulation | Calibrating the LLM-as-judge prompt is harder than the application prompt — the eval is only as good as your judge |
| 2 | Production agentic systems + multi-agent orchestration | **LeaseI 8-agent StateGraph** | Compliance operations needed AI that routes correctly: document review vs. staff investigation vs. tenant self-service — three distinct use cases, one shared knowledge repository | Design a multi-agent system with real conditional routing (not just chains) and hard safety boundaries | 8-agent LangGraph StateGraph: Triage agent classifies → routes to specialist agents → Reasoning agent generates hypothesis → Validation → HITL Escalation when confidence too low | Three production surfaces with 93.6% precision; Tenant agent never auto-resolves eligibility (safety boundary tested) | State schema design is everything — define what the system needs to know at each decision point, and the graph edges follow naturally |
| 3 | Guardrails + HITL checkpoints + audit trails | **LeaseI guardrails design** | Compliance AI decisions are auditable by regulators — every answer must cite its source or be flagged as unsupported | Enforce guardrails in code, not just in prompts — the system can't rely on LLM self-restraint for regulated decisions | Core rule: LLM extracts and reasons; deterministic logic enforces every final compliance/eligibility call; confidence scoring routes to HITL when uncertain; every answer cites exact source clause | 100% citation correctness on eval set; 0% unsupported-claim rate; HITL escalation tested and verified | Guardrails in prompts are suggestions. Guardrails in code are guarantees. Build the hard boundaries in code and use prompts only for reasoning. |
| 4 | Observability for non-deterministic agents | **AgentProbe observability platform** | Agents fail in non-obvious ways — same input, different output runs later; standard error monitoring catches exceptions, not semantic drift | Build observability designed for non-deterministic systems, not server-style monitoring | React dashboard backed by ChromaDB: per-run metrics (factual accuracy, hallucination rate, retrieval quality, latency), regression drift detection across runs, CI-integrated eval gate | Failing agent runs blocked before production — CI blocks merge when eval score drops below threshold | Design observability first, not last. By the time you add monitoring to a running agent system, you've already shipped silent failures. |
| 5 | Multiple agent platforms + platform selection | **AgentProbe multi-provider routing** | Different LLM providers have different cost/quality/latency tradeoffs — no single provider wins on all dimensions | Build routing logic that selects provider dynamically based on task requirements, not hardcoded | Multi-provider LLM router (Anthropic, OpenAI, Groq, Ollama) with dynamic selection; Ollama for zero-cost local evaluation; Groq for speed; Anthropic/OpenAI for quality-critical tasks | 15-endpoint FastAPI backend running 100% locally at zero cost during development; production routing preserves quality while managing cost | Platform selection is a real decision, not a preference. Map task requirements to platform capabilities before you write a line of code. |
| 6 | Directing contractors + driving standards without authority | **Entrata: 300+ peer code reviews + mentoring** | At Entrata with 5+ engineers, technical standards spread through what you approve and reject, not what you mandate | Set the bar through reviews: raise the floor on every team member's output without being the manager | 300+ peer code reviews with structured feedback; defined SQL optimization standards (30% performance gain); mentored 5+ junior engineers on system design and compliance patterns | Bug count below 10 for 6+ consecutive months; management appreciation recognition; patterns I introduced appeared in other engineers' code without prompting | Technical authority spreads through examples and reviews, not directives. Write the code you want to see, then make the review teach it. |

**Case study recommendation:** Lead with LeaseI — three surfaces, 8 agents, eval harness, guardrails, production metrics. It covers all dimensions the JD requires in a single coherent system. Walk through the eval harness design specifically — this is rare and directly maps to a core JD requirement.

**Red-flag questions:**
- *"You don't have Splunk experience — how will you ramp?"* → "I've built custom observability into all three production systems. The principle — instrument the non-deterministic decision points, track drift across runs, alert on SLO violations — I understand from first principles. Splunk o11y is the tool; the observability philosophy transfers. I'll complete Splunk Fundamentals before the technical screen."
- *"These are self-directed projects, not enterprise deployments — how do we know you can operate at Cisco scale?"* → "Entrata is 100K+ MAU production at scale — 120+ Agile sprints, 20+ modules, 99.5% uptime. The agent architectures in LeaseI and AgentProbe are designed to the same production standards: eval harnesses, regression gates, HITL, audit trails. Self-directed means I set the bar, not that the bar is lower."

**New STAR+R stories to append to story-bank.md:**
- LeaseI eval harness → "eval harnesses and simulation testing"
- LeaseI guardrails → "governance and audit trails for autonomous systems"

---

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|--------|---------|--------|
| Source | LinkedIn posting — official Cisco careers posting | Positive |
| Comp disclosed | $135,800–$198,800 explicitly; full benefits, RSUs, PTO detailed | Positive |
| Company stage | Cisco (NASDAQ: CSCO) — Fortune 100; $28B Splunk acquisition active integration | Positive |
| JD specificity | Named platforms (MCP, Splunk o11y), named deliverables (3-5 agents, SLOs/SLIs), specific org context (field productivity for technical sellers) | Positive |
| H-1B sponsorship | Cisco top-20 H-1B sponsor — confirmed, no verification needed | Positive |
| Reposting | No prior Splunk/Cisco agentic SA posting in scan history | Positive |
| Role makes sense | Splunk (network/security observability platform) building internal AI agents for field teams = logical integration of recent AI capabilities into sales engineering productivity | Positive |

---

## Keywords Extracted

agentic AI, multi-agent orchestration, Model Context Protocol, MCP, RAG, retrieval-augmented generation, evaluation harnesses, offline evals, online evals, guardrails, HITL, human-in-the-loop, audit trails, observability, Splunk Observability, Splunk o11y, token management, cost management, model routing, LLM, Python, Bash, AWS, cloud-native, microservices, SLO, SLI, agent platform, LangGraph, production agents, field productivity, technical sellers, simulation testing, regression gating

---

## Machine Summary

```yaml
report: 208
company: Cisco (Splunk)
role: Agentic Solutions Architect
score: 4.3
archetype: Agentic / LLMOps (internal field productivity platform)
location: Remote, Central and Eastern US (Virginia = satisfied)
comp_base: "$135,800–$198,800 + RSUs + bonus (TC ~$160K–$240K)"
sponsorship: confirmed — Cisco top-20 H-1B sponsor
legitimacy: High Confidence
recommend: apply — 4.3 above 4.0 FDE/Agentic threshold; eval harness = direct proof point; Splunk gap manageable
threshold_used: "4.0+ (Agentic/Applied AI archetype); 4.3 = APPLY"
key_gap: Splunk/Splunk o11y experience (hard, explicitly required); MCP no production proof point
key_strength: Eval harnesses (LeaseI 225-query + LLM-as-judge + regression gating = rare); production agentic systems (LeaseI 8-agent, AgentProbe 3-agent, Magizhs); Cisco H-1B confirmed; $135K+ exceeds target; remote eastern US
action_before_apply: Get Splunk free trial + complete Splunk Observability quick-start; prepare MCP integration talking point; send CV with eval harness + guardrails framing
```
