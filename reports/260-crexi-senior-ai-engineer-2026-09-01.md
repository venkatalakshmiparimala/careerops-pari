# 260 — Crexi — Senior AI Engineer

**Date:** 2026-09-01
**Score:** 4.7/5 — APPLY (PropTech threshold 4.0+, +0.3 boost applied)
**URL:** https://builtin.com/job/senior-ai-engineer/10649062
**PDF:** ❌
**Legitimacy:** High Confidence — Active BuiltIn listing, specific salary, detailed Anthropic/AWS Bedrock tech stack, commercial real estate PropTech

---

## Block A — CV Match

**Exceptional alignment — JD reads like a description of what the user has built.**

| JD Requirement | CV Proof Point |
|---------------|----------------|
| "Multi-step agentic workflows, routing, planning, tool use, state management using LangGraph/LangChain" | LeaseI: 8-agent LangGraph stateful system with conditional routing, tool calling, state management ✓ |
| "Build evaluation frameworks and production monitoring systems" | AgentProbe: 5-metric eval engine, LLM-as-judge, CI-integrated regression gate — exactly this ✓ |
| "Develop context and retrieval pipelines for proprietary data" | LeaseI RAG + AgentProbe ChromaDB vector retrieval ✓ |
| "Anthropic models on AWS Bedrock, including Bedrock AgentCore" | Anthropic API in cv.md; AWS infrastructure throughout Entrata ✓ |
| "Guardrails, structured outputs, graceful ambiguity handling" | LeaseI deterministic guardrails on every regulated output ✓ |
| "Leverage agentic coding tools like Claude Code" | **User runs Claude Code daily** — explicit advantage ✓ |
| "Ensure AI outputs are explainable and source-linked" | LeaseI: 100% citation correctness, every answer cited to exact source clause ✓ |
| "LLM evaluation pipelines with offline evals and HITL annotation" | AgentProbe + LeaseI HITL escalation — preferred qual fully met ✓ |
| Python proficiency + backend services | Python 8yr, FastAPI ✓ |
| AWS cloud infrastructure | S3, EC2, RDS, Glue ✓ |
| RAG systems, embeddings, vector search | ChromaDB, TF-IDF, semantic search ✓ |
| "2+ years building LLM-powered applications" | AgentProbe (2025) + LeaseI (2026) + Magizhs intern ✓ |

**Only gap:** AWS Bedrock-specific experience (user has Anthropic API directly; Bedrock is the same models via AWS wrapper). Not a meaningful gap.

**ATS baseline (cv.md):** ~17/20. Patches: "AWS Bedrock", "Claude Code", "commercial real estate" framing, "source-linked".

---

## Block B — North Star Alignment

**Archetype: AI Engineer at PropTech company.** Crexi is commercial real estate — PropTech +0.3 boost applies. The agentic AI role is the exact archetype the user has been building toward. AgentProbe is the evaluation framework. LeaseI is the agentic workflow system. This is the best technical alignment of all PropTech roles found today.

---

## Block C — Compensation

$179,000 – $241,000 annually. Top quartile for a Senior AI Engineer. No comp floor concern.

**Score: 5/5**

---

## Block D — Cultural Signals

- Crexi: commercial real estate platform (listings, analytics, marketplace) — PropTech with clear data product
- Anthropic on AWS Bedrock = serious AI investment (not just LLM wrappers)
- Claude Code explicitly in required skills — team actually uses the tools
- Remote or hybrid (Playa Vista, CA base) — user open to all US locations
- "Prototype against user feedback with Product and Design teams" — collaborative, product-oriented

**Score: 4.5/5**

---

## Block E — Red Flags

1. **H-1B sponsorship: UNCONFIRMED** — Crexi not in confirmed-sponsor list. Verify before applying.
2. **"2+ years building LLM-powered applications"** — borderline; user has AgentProbe + LeaseI + Magizhs (all 2025-2026). Honest answer: ~1.5-2 years. Not a hard block.
3. **Playa Vista CA hybrid** — relocation possible; user confirmed open to all US locations.
4. **AWS Bedrock** — user has Anthropic API directly; Bedrock is same models via AWS. Honest framing, not fabrication.

**Adjustment: -0.3**

---

## Block F — Global Score

| Factor | Signal |
|--------|--------|
| CV match | 5.0 — LangGraph, evaluation framework, HITL, Claude Code, Anthropic, RAG |
| North Star | 5.0 — AI Engineer archetype, PropTech commercial real estate |
| Comp | 5.0 — $179K-$241K top quartile |
| Culture | 4.5 — real AI investment, Claude Code in stack, remote/hybrid |
| Red flags | -0.3 — H-1B unconfirmed, LLM years borderline |
| PropTech boost | +0.3 |

**Global: 4.7/5 — APPLY (verify H-1B first)**

---

## Block G — Posting Legitimacy

**High Confidence.** Active BuiltIn listing, specific salary, extremely detailed tech stack (names Anthropic, AWS Bedrock, AgentCore, LangGraph, LangChain, Claude Code, Codex), clear company identity (Crexi, Playa Vista CA). No ghost indicators.

---

## Story Bank — STAR+R

**Evaluation framework story:**
- Situation: Building LeaseI — needed to measure whether LLM outputs met compliance accuracy before trusting them in production
- Task: Build evaluation infrastructure before shipping any prompt to production
- Action: Built AgentProbe first — 5-metric eval engine, CI gate, LLM-as-judge, offline evals across 1,240 test cases
- Result: Zero regressions shipped; every prompt variant evaluated before merge
- Relevance: "Build evaluation frameworks and production monitoring systems to assess quality and business outcomes"

**Agentic workflow story:**
- Situation: Compliance investigation workflows took a full day due to scattered context across code, settings, tickets, regulatory rules
- Task: Build multi-step agentic system to automate investigation routing and context retrieval
- Action: 8-agent LangGraph pipeline with routing → retrieval → reasoning → validation → HITL escalation
- Result: 93.6% precision across 1,240 test cases; engineers get ranked, evidence-backed root-cause hypotheses
- Relevance: "Design multi-step agentic workflows including routing, planning, tool use, and state management"

**Claude Code + source-linked outputs story:**
- Situation: Every LeaseI answer needed to be verifiable — compliance decisions can't rest on LLM inference alone
- Task: Ensure every AI output is cited to an exact source clause or flagged as unsupported
- Action: Built citation grounding into the retrieval layer; 100% citation correctness enforced in eval harness
- Result: Zero unsupported compliance decisions in production
- Relevance: "Ensure AI outputs are explainable and source-linked"
