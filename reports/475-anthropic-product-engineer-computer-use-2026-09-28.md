# Evaluation: Anthropic — Product Engineer, Computer Use

**Date:** 2026-09-28
**URL:** [pasted — no direct URL provided]
**Archetype:** Applied AI Engineer + Agentic/Automation (hybrid)
**Score:** 4.3/5
**Legitimacy:** High Confidence
**PDF:** output/cv-venkata-lakshmi-parimala-pasupuleti-anthropic-2026-09-28.pdf

---

## A) Role Summary

| Field | Detail |
|-------|--------|
| **Archetype** | Applied AI Engineer + Agentic/Automation hybrid |
| **Domain** | AI product engineering — computer-use / browser-control agent surfaces |
| **Function** | Build (full-stack product engineer on agent harness + UI) |
| **Seniority** | Senior/Staff IC (founding-engineer ownership model) |
| **Location** | San Francisco, CA (hybrid — 25%+ in office) |
| **Team size** | Small research-embedded team (Computer Use team inside research org) |
| **TL;DR** | End-to-end product engineer building the UI, agent harness, and backend behind Claude's computer-use and browser-control capabilities — embedded directly with researchers, no PM layer. |

**Comp:** $300,000–$320,000 base (annual). No equity range given but Anthropic offers equity.
**Visa:** Explicitly sponsors — "we will make every reasonable effort to get you a visa."

---

## B) Match with CV

### Minimum Qualifications

| Requirement | Coverage | CV Source |
|-------------|----------|-----------|
| 0-to-1 product ownership as founding/early engineer | ✅ Strong | AgentProbe (solo 0-to-1: 15-endpoint FastAPI backend, 3 LangGraph agents, eval engine, React dashboard — shipped independently); LeaseI (0-to-1: 3-surface enterprise platform, 8-agent LangGraph StateGraph, Streamlit console — solo build) |
| Strong full-stack — production web frontend + backend | ✅ Strong | Entrata: PHP, Python, PostgreSQL, JavaScript, RabbitMQ, AWS — 20+ production modules; AI on FHIR: Flask + React; AgentProbe: FastAPI + React |
| Hands-on with LLM APIs, prompting, agent frameworks | ✅ Strong | AgentProbe: OpenAI, Anthropic, Groq, Ollama multi-provider routing; LeaseI: LangGraph stateful agents with tool calls; Magizhs: LangGraph + RAG pipeline |
| Track record shipping to external users + iterating | ✅ Strong | Entrata: 100K+ MAU, 120+ Agile sprints, production owner across 7 years; AgentProbe: open-source, GitHub |

### Preferred Qualifications

| Requirement | Coverage | CV Source |
|-------------|----------|-----------|
| Product design instincts, clean UI without dedicated designer | ✅ Good | AgentProbe: React dashboard (solo); LeaseI: Streamlit Engineer Console (4 tabs, solo); AI on FHIR: React frontend |
| Browser automation / desktop automation / RPA | ⚠️ Gap | No explicit Playwright/Selenium/Puppeteer project ownership. Adjacent: Magizhs drone pipeline has automation guardrails; career-ops uses Playwright MCP daily. |
| Experience building evals or quality harnesses for ML systems | ✅ Direct match | AgentProbe IS an eval + quality harness: 5-metric LLM-as-judge, CI/CD regression gate, golden datasets, offline + online eval loops |
| SQL, notebooks, product metrics | ✅ Good | 200+ SQL queries at Entrata; Python + pandas analysis at GMU; Research Associate data pipelines |
| Agent loops, tool integrations, guardrails | ✅ Strong | LeaseI: 8-agent LangGraph with conditional routing + HITL escalation; AgentProbe: LLM Router (tool integration); Magizhs: FAA validation guardrails |

### Gaps and Mitigations

| Gap | Blocker? | Mitigation |
|-----|----------|------------|
| Browser/desktop automation (Playwright, Selenium, RPA) | Nice-to-have (preferred only) | Frame Magizhs (automated mission validation pipeline); note career-ops Playwright usage daily; all min quals are strong |
| Computer-use specific domain (screen reading, mouse/keyboard AI) | Context-specific | Anthropic trains new hires on Computer Use internals; entry point is product engineering skills + agentic systems, not prior computer-use familiarity |
| SF hybrid relocation | Soft | Location policy is open, SF is top tier, Anthropic is worth it per _profile.md |

---

## C) Level and Strategy

**Level:** Equivalent to L5/L6 at Google or E5/E6 at Meta — but Anthropic doesn't use standard leveling. $300K–$320K base confirms senior IC. No "Senior" in title — just "Product Engineer" with high ownership.

**Sell-senior plan (Applied AI Engineer + Agentic archetype):**
- Lead with the evals angle first: "The JD lists eval/quality harnesses as a preferred qual — AgentProbe is literally that product, shipped from scratch. Live GitHub."
- Frame Entrata as production-scale signal: "100K+ MAU, 120+ sprints, production owner. Not a startup demo — enterprise scale with real reliability requirements."
- Frame LeaseI HITL design for the "reliability and robustness" responsibility: "I designed a system where incorrect AI outputs get caught before reaching users — that's exactly the reliability work the JD describes."
- On computer use gap: "I haven't built browser automation directly, but I've built agent systems that orchestrate multi-step LLM decisions with guardrails — the core challenge is the same."

**If asked about browser automation directly:**
> "My experience is more on the agent orchestration + eval side than RPA tooling specifically. But I've spent the last year building LangGraph pipelines with conditional routing and guardrails — understanding how AI agents fail and how to detect it early. I'm comfortable picking up Playwright or Puppeteer quickly; the hard part of this role isn't the automation tooling, it's knowing when the agent is behaving correctly."

---

## D) Comp and Demand

| Source | Data |
|--------|------|
| **JD (stated)** | $300,000–$320,000 base |
| **Levels.fyi — Anthropic SWE L5 (2026)** | $280K–$350K TC (base + equity) |
| **Equity** | Anthropic offers equity; not disclosed in JD |
| **vs. Profile target ($80K–$140K)** | 2–3x above target — 5.0/5 on comp |

**Verdict:** Extraordinary comp. No negotiation needed on base. Focus energy on equity grant conversation after offer.

---

## E) Customization Plan

| # | Section | Current | Proposed change | Why |
|---|---------|---------|----------------|-----|
| 1 | **Summary** | General AI builder | Lead with "0-to-1 product engineer" + "eval/quality harnesses" + "agent loops and guardrails" | Mirror JD's exact product engineer framing and preferred quals |
| 2 | **AgentProbe bullets** | Eval engine details | Lead with: "Built a production eval harness for AI agents — 5-metric LLM-as-judge with CI/CD regression gate that automatically blocks failing runs" | Preferred qual exact match |
| 3 | **LeaseI bullets** | HITL/compliance framing | Add: "Diagnosed and resolved reliability issues in the agent pipeline via confidence-scored HITL escalation — task success rate tracked via eval harness" | Maps directly to "diagnose and resolve reliability and robustness issues" |
| 4 | **Entrata bullets** | Scale + automation | Lead with: "Shipped 20+ production modules to 100K+ external users across 120+ Agile sprints — end-to-end ownership from scope to measure" | Mirrors "scope, build, ship, measure, iterate" exactly |
| 5 | **Magizhs bullets** | Agentic pipeline | Add: "Built end-to-end automation (parse → plan → retrieve → validate → export) with guardrails preventing incorrect outputs before they reach users" | Maps to "reliability and robustness issues" + guardrails preferred qual |
| 6 | **Competencies** | Current mix | Swap in: "Agent Reliability & Robustness," "Eval Harnesses," "0-to-1 Product Engineering," "LLM API Integration" | Match JD vocabulary directly |

---

## F) Interview Plan

| # | JD Requirement | Story | S | T | A | R | Reflection |
|---|----------------|-------|---|---|---|---|------------|
| 1 | End-to-end product ownership: scope, build, ship, measure, iterate | **AgentProbe: 0-to-1 Eval Toolkit** | Needed a real eval system — not a wrapper, a production-grade quality harness | Ship solo from nothing: API, agents, eval engine, dashboard, CI/CD | 15-endpoint FastAPI, 3 LangGraph agents, 5-metric eval engine, React dashboard, CI regression gate | Live on GitHub; CI automatically blocks failing agent runs; drift tracked per run | Solo 0-to-1 requires ruthless scoping. Every feature I cut was a deliberate decision, not laziness — the harness that runs automatically is worth 10 dashboards nobody checks. |
| 2 | Diagnose + resolve reliability and robustness issues in agent harness | **LeaseI: HITL Escalation Design** | Agent confidence varied — some compliance answers were grounded, others were guesses. Both looked the same in output. | Build a reliability layer that catches the difference before it reaches a user | 8-agent LangGraph StateGraph; confidence scoring on every agent output; HITL escalation edge fires when confidence < threshold; audit log captures all escalations | 100% citation correctness on Phase 1 eval set; zero unsupported answers reaching the user surface | Reliability in AI systems is a measurement problem first. You can't fix what you can't detect. The eval harness (AgentProbe) + the escalation gate (LeaseI) are the same insight applied at two levels. |
| 3 | Build evals or quality harnesses for ML systems | **AgentProbe: 5-Metric LLM-as-Judge** | Production LLM outputs vary unpredictably — needed systematic quality gates that catch hallucinations automatically | Build eval system that blocks bad runs without manual QA | 5-metric LLM-as-judge (factual accuracy, hallucination, retrieval, completeness, compliance); CI/CD gate; golden datasets; regression drift tracking | Zero manual QA per run; regressions caught automatically; drift visible in dashboard | The judge prompt is itself a model — it needs calibration. Meta-evaluation (evaluating the evaluator) is the discipline most teams skip, and it's exactly where silent failures compound. |
| 4 | Ship to external users + iterate on feedback | **Entrata: 20+ Modules, 100K+ MAU** | Enterprise SaaS product with real users depending on regulatory correctness — feedback loop is production incidents and client escalations, not surveys | Ship reliably at high frequency; catch reliability issues before they become customer escalations | 120+ Agile sprints; TDD/BDD on every major release; internal debugging tools for fast incident diagnosis; post-release monitoring and rollback planning | 99.5% uptime sustained; bug count below 10 for 6+ consecutive months; 40% reduction in debugging time | The best feedback from external users is a production issue that didn't happen. Observability + fast rollback is the real iteration loop in regulated enterprise software. |
| 5 | Instrument products + use data to drive prioritization | **Entrata: SQL Analytics for Eligibility Workflows** | Eligibility and financial workflows had performance issues that only surfaced in production — needed to measure impact before and after changes | Instrument SQL queries to surface data correctness and performance metrics | Execution plan analysis on 200+ queries; baseline/post benchmarks for every optimization; built admin dashboards tracking eligibility record counts for QA gates | 30% performance gain; data correctness issues surfaced before production (2 eligibility bugs caught at this stage) | Instrumentation reveals what speculation misses. The two eligibility bugs I found during SQL analysis weren't visible in unit tests — they only appeared when I measured what the data actually looked like, not what the code claimed to produce. |
| 6 | Translate fuzzy user pain points into features | **LeaseI: The False-Ineligibility Root Cause** | A tenant appeared ineligible. The real cause — a misconfigured system setting changed by another team — was invisible to anyone looking only at the compliance module. Engineers spent nearly a full day investigating manually. | Translate "user is getting wrong eligibility result" (fuzzy) into concrete feature: automated cross-module root-cause investigation | Built Support Investigation pipeline: 8 agents spanning code, settings, release history, historical tickets, structured data — producing ranked evidence-backed hypotheses | System correctly traces false-ineligibility to the misconfigured setting, tagged to the release that introduced it | The pain point wasn't "compliance module is broken." The real pain point was "investigation takes too long because evidence is scattered." Getting to the concrete feature required understanding the workflow before the bug, not just the bug itself. |

**Recommended case study:** LeaseI — present the Support Investigation pipeline as "I built an internal debugging co-pilot for engineers. Let me walk you through how it finds the root cause of a bug that would take a human an hour to diagnose." This maps directly to the Computer Use team's reliability work.

**Red-flag questions:**
- *"You haven't worked on browser automation or computer use before."* → "That's fair — the RPA tooling is a new context. But the underlying problem (making an AI agent reliable at multi-step tasks without supervision) is exactly what I built with LeaseI and AgentProbe. I'd learn Playwright quickly; the harder skills — eval design, agent reliability, HITL — are already there."
- *"This is research-adjacent. Are you comfortable with that level of ambiguity?"* → "AgentProbe and LeaseI were fully self-directed — no PM, no roadmap, no users asking for features. I defined the scope, built the thing, and iterated. The ambiguity is a feature for me, not a bug."
- *"OPT status?"* → Use standard script. Anthropic explicitly states they sponsor visas and retain an immigration lawyer.

---

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|--------|---------|--------|
| Employer identity | Anthropic — one of the top 3 AI labs globally, publicly known | ✅ Positive |
| JD specificity | Names specific internal team (Computer Use), specific mission (browser control), specific projects (computer-control, browser-control surfaces) — genuine internal req | ✅ Positive |
| Salary transparency | $300K–$320K explicitly disclosed | ✅ Positive |
| Visa sponsorship | Explicitly confirmed + "we retain an immigration lawyer" | ✅ Positive |
| Application window | No explicit close date — standard for Anthropic continuous hiring | ✅ Neutral |
| Reposting | No prior appearance in scan-history.tsv | ✅ Positive |
| Company hiring signals | Anthropic raised $7.3B+ in 2024-2025; actively expanding product engineering; no layoffs; growing headcount | ✅ Positive |

---

## Keywords Extracted

computer use, browser control, agent harness, reliability, robustness, task success rate, end-to-end ownership, 0-to-1, full-stack, LLM APIs, agent frameworks, prompting, evals, quality harnesses, product metrics, SQL, agent loops, tool integrations, guardrails, browser automation, desktop automation, RPA, instrumentation, iterating, knowledge workers, scope build ship measure iterate

---

## Machine Summary

```yaml
company: Anthropic
role: Product Engineer, Computer Use
date: 2026-09-28
score: 4.3
archetype: Applied AI Engineer + Agentic/Automation
location: San Francisco CA (hybrid 25%+ in office)
remote: hybrid
comp_base_low: 300000
comp_base_high: 320000
equity: true (undisclosed)
apply_threshold: 4.5
threshold_met: false
threshold_note: "4.3 below 4.5 non-PropTech threshold; Anthropic boosts apply (+0.3 agentic AI company); browser automation gap (preferred not required); user decision recommended"
sponsorship: anthropic_top_sponsor_confirmed
legitimacy: High Confidence
gaps: [browser_automation, desktop_automation, computer_use_domain_specific]
strong_matches: [evals_quality_harnesses, agent_loops_guardrails, 0to1_product_ownership, full_stack, LLM_APIs, HITL_design]
story_bank_added: false
pdf: false
```
