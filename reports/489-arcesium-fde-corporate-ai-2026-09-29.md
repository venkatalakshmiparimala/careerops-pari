# Evaluation: Arcesium — Forward Deployed Engineer, Corporate AI Transformation

**Date:** 2026-09-29
**URL:** (not provided — paste URL here)
**Archetype:** AI Forward Deployed + Agentic/Automation
**Score:** 4.6/5
**Legitimacy:** High Confidence
**PDF:** output/489-arcesium-fde-corporate-ai-2026-09-29.pdf

---

## A) Role Summary

| Dimension | Detail |
|-----------|--------|
| Archetype | AI Forward Deployed (primary) + Agentic/Automation (secondary) |
| Domain | Financial technology / enterprise AI transformation |
| Function | Build — agents, workflow automations, internal tools |
| Seniority | Senior (6+ YOE) |
| Remote | Not stated — NYC HQ (Arcesium), likely hybrid |
| Team size | "One of the first few members" of new Corporate AI Transformation team |
| TL;DR | Build internal AI agents and workflow automations for a fintech serving hedge funds; own from prototype to production and drive adoption across business teams. |

---

## B) Match with CV

| JD Requirement | CV Match | Strength |
|----------------|----------|----------|
| 6+ years hands-on engineering | 8+ years Entrata (Senior SWE, production systems, 100K+ MAU) | Strong |
| Strong APIs, data, systems design | 20+ full-stack modules; 200+ SQL queries optimized; FastAPI backend (LeaseI, AgentProbe) | Strong |
| Build internal tools for business teams | LeaseI: built for support engineers to investigate eligibility tickets — exact internal-tool-for-business-team pattern | Exact |
| Agents, LLMs, agent frameworks | LeaseI 8-agent LangGraph StateGraph (Triage → Retrieval → Configuration → Historical Incident → Structured Data → Reasoning → Validation → HITL); AgentProbe 3-agent orchestration | Exact |
| MCP servers | Magizhs internship: built MCP server for drone mission planning; Workiva/career-ops context | Strong |
| Design agent architectures reliably | LeaseI: conditional routing, durable state, HITL escalation gate, deterministic compliance boundary | Exact |
| Prototype → production | LeaseI: vague support pain point → 8-agent production platform + eval harness (93.6% precision, 1,240 test cases) | Exact |
| Reusable components, templates, playbooks | AgentProbe: 15-endpoint FastAPI eval toolkit, reusable across LLM providers (OpenAI/Anthropic/Groq/Ollama), CI-integrated regression harness | Exact |
| Define KPIs, measure impact | LeaseI: 5-metric eval harness (precision 93.6%, F1 87.9%, pass@1 81.7%, pass@3 88.3%); AgentProbe: 5-metric engine (correctness, groundedness, latency, token efficiency, hallucination rate) | Strong |
| Credibility with senior leaders | GMU TA: delivered workshops to 600+ students; Research Associate: dashboards for faculty leadership (40% comprehension boost); Entrata: 300+ peer code reviews, mentored 5+ engineers | Moderate |
| Build-vs-buy decisions | LeaseI: chose hand-rolled TF-IDF over LangChain RAG — deliberate cost/reliability trade-off; AgentProbe: built from scratch to eliminate vendor dependency | Strong |
| Ambiguity → working prototype fast | LeaseI origin: 1-day support investigation problem → structured problem statement → 8-agent solution | Exact |

**Gaps:**

| Gap | Type | Mitigation |
|-----|------|------------|
| Financial industry domain (investment ops, prime brokerage) | Soft gap | Entrata: HUD income limits, rent calculations, PHI compliance = regulated financial data at scale; the compliance mindset transfers |
| Arcesium-specific corporate systems (Snowflake, proprietary data warehouse) | Nice-to-have | Arcesium expects ramp-up on internal platforms; "willingness to learn" is explicit |
| H-1B sponsorship not stated | Uncertainty | Arcesium is a ~700-person fintech — likely H-1B sponsor; verify at first contact |

---

## C) Level and Strategy

**Level detected:** 6+ YOE, "first few members" of founding team — no formal leveling. Treated as senior IC with high ownership from day one.

**Sell without overstating:**
- Lead with: "I've done this exact workflow before — LeaseI started as an ambiguous support pain point and I turned it into a production 8-agent system with an eval harness that runs regression gates in CI."
- Key phrase: "I ship, not just prototype." AgentProbe = reusable toolkit other teams can use. LeaseI = internal platform in production.
- Arcesium wants a "builder, systems engineer, and product thinker rolled into one" — match each exactly: builder (LeaseI, AgentProbe), systems engineer (Entrata microservices, 200+ SQL queries), product thinker (identified root-cause pattern in support tickets, designed the 3-surface architecture).

**If they test on financial domain:**
- "I spent 8 years building systems where a wrong calculation affected thousands of residents' eligibility — HUD income limits, rent calculations, HAP payments. The stakes were regulatory, not just technical. That compliance-first mindset maps directly to financial operations."

**Growth path:** First few members = fastest path to ownership and scope expansion. No downleveling concern for this structure.

---

## D) Comp and Demand

| Item | Detail |
|------|--------|
| Stated range | $180,000–$220,000 base |
| Year-end bonus | Guaranteed in first year (amount not stated) |
| 401k match | Yes |
| Medical | Yes |
| Market position | Top-quartile NYC fintech for Senior IC |
| Levels.fyi comparable | NYC fintech Senior SWE: $180K–$240K TC (Goldman, Jane Street, Citadel range); Arcesium is smaller but range holds |
| Comp score | 5/5 — well above target range |

---

## E) Customization Plan

| # | Section | Current | Proposed Change | Why |
|---|---------|---------|-----------------|-----|
| 1 | Summary headline | "Agentic AI Engineer · LangGraph · RAG Pipelines..." | "Forward Deployed AI Engineer · Agent Architect · LangGraph · MCP · Enterprise AI Transformation" | Match FDE + transformation framing exactly |
| 2 | Summary body | Generic AI engineer framing | Open with LeaseI origin story: ambiguous business problem → structured agent architecture → production system. "I turn operational pain points into reliable agent workflows." | Arcesium's entire JD is this sentence |
| 3 | LeaseI bullet ordering | Support investigation listed mid-project | Lead with: "Identified an ambiguous support bottleneck (1-day investigations → systematic root cause) and turned it into an 8-agent LangGraph pipeline running in production with a 5-metric eval harness" | Matches "ambiguous problem → working prototype → production-grade" exactly |
| 4 | AgentProbe | Framed as eval toolkit | Add framing: "Reusable AI workflow evaluation toolkit — reusable templates, regression harness, build-vs-buy documentation" | Matches "create reusable components, templates and playbooks" |
| 5 | Entrata | Compliance/backend framing | Add: "Shipped 20+ internal tools used by operations and support teams across the property management lifecycle" | Makes Entrata = internal tooling for business teams |
| 6 | Skills | Broad keyword list | Add to front: "Enterprise AI Transformation, Business Workflow Automation, Corporate AI Systems, LLM Agent Deployment" | Direct JD keyword match |

---

## F) Interview Plan

| # | JD Requirement | Story | S | T | A | R | Reflection |
|---|----------------|-------|---|---|---|---|------------|
| 1 | "Ambiguous problem → working prototype → production" | LeaseI origin | Support team spending full day on eligibility investigation; root cause always buried in system settings | Build a tool that connected product knowledge, regulatory rules, and incident history | Designed 8-agent LangGraph StateGraph with conditional routing and HITL escalation gate | 93.6% precision on 1,240 cases; pass@1 81.7%; engineers spend <5 min on cases that took a day | Should have built the eval harness before the agents, not after |
| 2 | "Reusable components that accelerate work across the firm" | AgentProbe | Each AI project built evaluation from scratch — no reusable methodology | Build a toolkit other engineers could use | 15-endpoint FastAPI eval engine, 5-metric scoring, multi-provider LLM routing, CI-integrated regression | Teams could evaluate LLMs locally at zero cost without vendor lock-in | Would invest more in documentation earlier — adoption is blocked by discoverability |
| 3 | "MCP, agent frameworks, rapidly prototype" | Magizhs MCP server | Marketing/real estate teams needed mission planning from natural language requests | Build an agentic system that translated NL survey requests into flight plans with FAA compliance | LangGraph stateful graph (parse → plan → retrieve → validate → export); RAG over FAA Part 107; MCP server for operator tool integration | Compliant missions route to QGroundControl export; non-compliant missions blocked with cited regulation | MCP layer made integration with downstream tools much cleaner than REST alone |
| 4 | "Design agent architectures that complete business tasks reliably" | LeaseI HITL gate | Compliance decisions can't be made by LLMs — the system needed a hard boundary | Design a conditional routing system that escalated low-confidence or regulated calls to humans | LLM reasons and ranks hypotheses; deterministic logic or human makes every final regulated call; HITL gate triggers when confidence < threshold | Zero false AI auto-decisions on regulated eligibility calls in production eval | Core design rule: LLM extracts, human or deterministic logic decides. Would make this a first principle from day one, not something added after the architecture was set. |
| 5 | "Build-vs-buy evaluation for AI workflows" | LeaseI RAG decision | Standard approach was LangChain RAG with vector DB; cost and reliability concerns | Evaluate whether to use standard tooling or build custom retrieval | Built hand-rolled TF-IDF + semantic reranking; no LangChain dependency, no ChromaDB, no API costs | 100% citation correctness on Phase 1 eval set; zero vendor outage risk | Build-vs-buy isn't always "buy is faster" — for compliance systems, controllability > speed |
| 6 | "Credibility with senior leaders, say hard things clearly" | Entrata stakeholder communication | HUD income limit pipeline had a data quality issue discovered 2 days before rollout | Needed to communicate scope of problem and rollback plan to non-technical stakeholders | Wrote plain-language impact analysis; proposed rollback with reconciliation; coordinated with compliance and ops leads | Zero compliance violations across 7-year ownership; stakeholders trusted the communication process | Learned to lead with "here's what we know, here's what we're doing" not "here's what went wrong" |

**Recommended case study to present:** LeaseI — specifically the architecture decision session: how I scoped a vague problem into 8 discrete agents, why I added the HITL gate, and how I measured success without a labeled dataset initially.

**Red-flag questions:**
- *"You were at Entrata for 7 years — can you move fast in a startup?"*
  → "LeaseI went from problem statement to production multi-agent system in under 3 months. AgentProbe is live on GitHub and used for eval. Speed isn't new — I just have more practice with enterprise reliability alongside it."
- *"Do you have financial services domain experience?"*
  → "I spent 8 years in a domain where a wrong calculation affected thousands of residents' eligibility for housing — HUD income limits, rent subsidies, PHI data. The compliance stakes were real. The patterns of regulated financial workflows — audit trails, deterministic boundary logic, rollback readiness — are exactly what I built at Entrata."

---

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|--------|---------|--------|
| Posting date | Posted 2026-09-29 (today) | Positive |
| Apply button | JD text provided directly — active posting | Positive |
| Description specificity | Names specific technologies (LLMs, agent frameworks, MCPs), clear scope, explicit first-team framing | Positive |
| Salary transparency | $180K–$220K explicitly stated with bonus structure | Positive |
| Company hiring signals | No recent layoff news for Arcesium; growth-stage fintech (founded 2014, ~700 employees) | Positive |
| Role-company fit | "Corporate AI Transformation team" is a common strategic initiative at fintech firms in 2026 | Positive |
| Requirements realism | 6+ YOE matches role scope; no contradictions | Positive |

**Context:** Arcesium is a well-funded fintech (backed by D.E. Shaw and JPMorgan Chase). New AI transformation team = legitimate strategic hire, not a ghost posting. Fresh posting, explicit team framing, salary stated.

---

## Keywords Extracted (ATS)

Forward Deployed Engineer, Corporate AI Transformation, agent frameworks, LLMs, MCP, workflow automation, internal tools, prototype to production, systems design, APIs, data systems, KPIs, build-vs-buy, reusable components, scalable solutions, business workflow automation, LangGraph, Python, FastAPI, enterprise AI, ambiguous problem, iterative delivery, agentic workflows, production-grade

---

## Machine Summary

```yaml
role: Forward Deployed Engineer, Corporate AI Transformation
company: Arcesium
score: 4.6
archetype: AI Forward Deployed + Agentic/Automation
location: NYC (likely hybrid)
salary_range: $180000-$220000
sponsorship: unconfirmed (verify at first contact)
top_proof_points:
  - LeaseI 8-agent LangGraph pipeline (ambiguous problem to production)
  - AgentProbe reusable eval toolkit (reusable components + build-vs-buy)
  - Magizhs MCP server (agent frameworks + MCP)
  - Entrata internal tooling for business operations (7 years)
key_gaps:
  - financial investment domain (investment ops, prime brokerage) — soft gap
  - Arcesium-specific toolchain — expect ramp-up
recommendation: apply — FDE priority category, exact archetype match, top-quartile comp
```
