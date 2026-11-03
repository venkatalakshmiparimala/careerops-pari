# Evaluation: Sierra — Software Engineer, Agent (New Grad)

**Date:** 2026-06-12
**URL:** https://jobs.ashbyhq.com/sierra/6a75b530-b7bb-4439-bb67-37b4f2b75b96
**Archetype:** Agentic / Automation + AI Forward Deployed
**Score:** 4.2/5
**Legitimacy:** High Confidence
**PDF:** output/cv-sierra-swe-agent-new-grad-2026-06-12.pdf

---

## A) Role Summary

| Field | Detail |
|-------|--------|
| Archetype | Agentic engineer: build + ship AI agents for enterprise customers |
| Domain | Enterprise AI agents — retail, healthcare, fintech, telecom, travel |
| Function | Build agents end-to-end; ship 6+ production launches in year one; own agent logic + evals |
| Seniority | New Grad / APX Program |
| Location | San Francisco, CA (onsite required) — relocation from McLean VA required |
| Comp | Not disclosed. Levels.fyi: Senior Agent Engineer $300K base + $150K equity = $460K TC. New grad estimate: $150-200K base, $230-310K TC |
| TL;DR | AgentProbe is the exact proof point for this role: building AI agents for enterprise customers is what Sierra does and what Parimala built. Top-tier company (Bret Taylor), strong comp. Onsite SF + H-1B conditional ("will do our best") are the only caveats. Strong apply. |

---

## B) Match with CV

| JD Requirement | CV Match | Strength |
|----------------|----------|----------|
| Recent CS grad / graduating 2026 | M.S. Data Analytics Engineering, GMU, May 2026 | ✅ |
| Build and ship AI agents for enterprise customers | AgentProbe: 3-agent LangGraph system (Orchestrator routes tasks, RAG Tracer validates retrieval, Auto Fix closes hallucination loops) — the same multi-agent architecture Sierra deploys at scale | ✅ Direct proof |
| Python | 8+ years Python production at Entrata | ✅ Far exceeds new grad bar |
| Multi-agent orchestration + tool calls | AgentProbe: LangGraph state machines, inter-agent handoffs, tool call routing | ✅ Direct proof |
| LLM evaluation / agent reliability | AgentProbe: 5-metric LLM-as-judge engine (factual accuracy, hallucination, retrieval, completeness, compliance) with CI/CD gates | ✅ Direct proof |
| Enterprise-scale delivery | Entrata: 100K+ MAU, 120+ Agile sprints, 20+ modules shipped, 99.5% uptime | ✅ Strong |
| Domains: healthcare, fintech, retail | AI on FHIR (HIPAA-compliant FHIR + LLM); Entrata (real estate fintech at scale) | ✅ Present |
| Fast iteration + shipping culture | Entrata: 120+ sprint cycles; AgentProbe shipped end-to-end | ✅ |
| H-1B sponsorship | "We'll do our best to support your visa process" — conditional (no confirmed LCA filings found for Sierra AI) | ⚠️ Conditional |

**Gaps:**
- No specific tech stack listed in JD (Sierra may use proprietary LLM orchestration, not LangGraph — learnable)
- Onsite SF required — relocation from McLean VA needed
- H-1B is conditional; Sierra AI is a young company (founded 2023) with limited H-1B filing history vs Scale AI (83 LCAs, 97% approval)
- "New grad" framing may trigger bias against 8-year resume — mitigate by framing as "new grad with production depth"

---

## C) Level and Strategy

**Level:** New grad / APX track. Parimala has 8 years — she's over-qualified on experience but correctly positioned given May 2026 graduation.

**Sell the combination:**
- "I didn't build a toy demo — I built a production multi-agent platform. AgentProbe's architecture (Orchestrator → RAG Tracer → Auto Fix) mirrors what Sierra deploys for its customers. I can ship your agents from day one, not after a learning curve."
- Frame Entrata tenure as production engineering rigor: real enterprise customers, not side projects
- The new grad positioning is correct (May 2026 grad) — but the proof points are not typical new grad material

**If they ask about salary on the form:** Use the negotiation script from _profile.md, anchor higher given the SF cost of living and company tier.

**On visa:** Proactively mention STEM OPT (3 years coverage) and strong academic profile during screen. Don't hide it.

---

## D) Comp and Demand

- **Role range:** Not disclosed. New grad at this level: $150-200K base typical for top SF AI startups
- **Total comp estimate:** $230-310K TC for new grad (base + equity at $4.5B valuation)
- **vs. target:** Significantly above target ($100-140K) — top-tier new grad comp
- **Sierra valuation:** $4.5B (as of 2024 Series B); Bret Taylor pedigree → IPO/acquisition path is credible
- **H-1B risk:** Conditional. Young company, limited filing history. Mitigate with STEM OPT coverage (3 years)

---

## E) Customization Plan

| # | Section | Change | Why |
|---|---------|--------|-----|
| 1 | Summary | Lead with "builds enterprise AI agents" framing — mirror Sierra's product domain | Role is literally "Software Engineer, Agent" for enterprise customers |
| 2 | AgentProbe bullets | Emphasize: "deployed agents across multiple task domains — the same architecture Sierra uses for enterprise customer deployments in retail, healthcare, and fintech" | Maps to Sierra's customer industries |
| 3 | Eval engine | "CI/CD gates ensure agents are reliable in production — the quality bar Sierra's enterprise customers require" | Sierra's value prop is reliable, deployable AI agents |
| 4 | Entrata | Lead with: "shipped production systems serving enterprise customers across 20+ modules" — mirrors Sierra's enterprise customer delivery model | Sierra deploys agents for enterprise customers at scale |
| 5 | AI on FHIR | Highlight healthcare + HIPAA-compliance angle — Sierra serves healthcare customers | Domain alignment signal |

---

## F) Interview Plan

| # | JD Focus | Story | S | T | A | R | Reflection |
|---|----------|-------|---|---|---|---|------------|
| 1 | Build enterprise AI agents | AgentProbe: 3-agent LangGraph | No production multi-agent framework existed for testing | Ship a full agent platform | LangGraph Orchestrator + RAG Tracer + Auto Fix with tool calls | 6 agent interaction patterns tested end-to-end | Would add streaming output earlier |
| 2 | Agent reliability | AgentProbe 5-metric eval engine | LLM hallucinations undetectable before prod | Make agents auditable | 5-metric LLM-as-judge CI/CD gates | Zero hallucination-escaped-to-production in testing | Would add adversarial test cases |
| 3 | Enterprise delivery | Entrata 120+ sprint delivery | 20+ modules across cross-functional product teams | Primary technical contact per module | Full-stack: Python, TypeScript, React, PostgreSQL, GraphQL | 100K+ MAU, 99.5% uptime, zero security incidents | Would document earlier |
| 4 | Healthcare/compliance domain | AI on FHIR | Natural language → FHIR APIs with no compliance framework | End-to-end HIPAA-compliant LLM integration | BERT + embeddings + RBAC + GraphQL | ~60% retrieval time reduction, HIPAA-compliant | Would add FHIR R4 structured output |
| 5 | Fast shipping | AgentProbe: LLM Router | Different tasks need different models, no routing existed | Build dynamic model selection | Multi-provider routing: Anthropic, OpenAI, Groq, Ollama by capability | Zero hardcoded models in production | Would add latency telemetry per provider |

**Case study to present:** "Sierra deploys AI agents for enterprise customers in retail and healthcare. Here's how I built the same architecture from scratch: Orchestrator receives the task suite, routes to RAG Tracer for retrieval quality validation, routes to Auto Fix for hallucination repair. Every run scored across 5 metrics. CI/CD gate fails if quality drops. This is the reliability bar enterprise customers need — and I built it before interviewing here."

---

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|--------|---------|--------|
| Freshness | Active listing on Ashby | Positive |
| Company traction | $4.5B valuation, Series B 2024, Bret Taylor + Clay Bavor founders | Positive |
| JD specificity | "Software Engineer, Agent" — specific role tied to APX program | Positive |
| Apply button | Active (Ashby ATS) | Positive |
| H-1B uncertainty | Conditional sponsorship; young company, limited filing history | Mixed |

---

## Keywords

AI agents, multi-agent systems, LangGraph, LangChain, enterprise AI, agent engineering, Python, RAG, LLM evaluation, production AI, new grad, APX, Sierra, agentic AI, FastAPI, ChromaDB, prompt engineering

---

## Machine Summary

```yaml
report_num: 079
company: Sierra
role: Software Engineer, Agent (New Grad)
date: 2026-06-12
score: 4.2
archetype: Agentic / Automation + AI Forward Deployed
legitimacy: High Confidence
location: San Francisco, CA (onsite — relocation from McLean VA required)
comp_range: "~$150-200K base, $230-310K TC est. (top-tier SF AI startup, new grad)"
visa_risk: medium (conditional "will do our best", young company, limited H-1B history)
key_gaps:
  - Onsite SF relocation required from McLean VA
  - H-1B conditional ("will do our best") — lower confidence than Scale AI
  - No confirmed LCA filing history for Sierra AI
  - Proprietary stack may differ from LangGraph (learnable)
key_strengths:
  - AgentProbe = direct proof for "Software Engineer, Agent" role
  - 8+ years Python far exceeds new grad bar
  - Healthcare + fintech domain experience matches Sierra's customer verticals
  - Bret Taylor (OpenAI Board Chair) company = top-tier prestige + comp
  - LangGraph multi-agent architecture = Sierra's core product pattern
  - APX program is designed for exactly this profile
recommend: strong apply — AgentProbe is the proof of concept for this exact company
```
