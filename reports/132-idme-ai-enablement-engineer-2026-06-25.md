# Evaluation: ID.me — AI Enablement Engineer, IT

**Date:** 2026-06-25
**URL:** https://job-boards.greenhouse.io/idme/jobs/7777644003
**Archetype:** Agentic / Automation + AI Platform / LLMOps (Internal Enablement)
**Score:** 4.3/5
**Legitimacy:** High Confidence
**PDF:** output/cv-idme-ai-enablement-engineer-2026-06-25.pdf

---

## A) Role Summary

| Dimension | Detail |
|-----------|--------|
| Archetype | Agentic / Automation + AI Platform / LLMOps (Corporate IT Enablement) |
| Domain | Identity Verification / Government Services (internal AI automation) |
| Function | Build and deploy production AI automations for internal teams — LLM agents, RAG pipelines, MCP servers, integrations with internal systems |
| Seniority | Mid-Senior (4+ YOE) |
| Remote | Full onsite, 5 days/week — McLean, VA or Mountain View, CA |
| Stack | Python, Go, TypeScript, AWS Bedrock/Agents, RAG, MCP servers, vector databases, orchestration frameworks (LangGraph/LangChain), evaluation tools |
| Comp | $154,347–$170,709 base (Mountain View stated range; McLean likely $130K–$160K) |
| TL;DR | Build production AI automations for ID.me's internal teams — near-perfect stack match, exceptional comp, McLean VA location advantage; held below 4.5 by full onsite 5d/wk and unclear visa sponsorship |

---

## B) Match with CV

| JD Requirement | CV Match | Strength |
|----------------|----------|----------|
| 4+ years experience | 8 years Entrata + GMU Research Associate + Magizhs intern | ✅ Exceeds |
| Production LLM/AI | Entrata AI pipeline (1.6M records), AgentProbe (3-agent LangGraph), LeaseI | ✅ Direct |
| Python | Python primary stack across all roles and projects | ✅ Direct |
| TypeScript | TypeScript in AgentProbe frontend | ✅ Direct |
| RAG pipelines | LeaseI (93.6% precision, 1,240 legal PDFs), AgentProbe ChromaDB RAG | ✅ Direct |
| Agentic systems / multi-agent | AgentProbe 3-agent LangGraph runtime (Orchestrator, RAG Tracer, Auto Fix), Magizhs LangGraph mission planner | ✅ Direct |
| "Production mindset — error handling, logging, observability, testing or evaluations" | AgentProbe 5-metric LLM-as-judge eval engine, CI/CD regression gates blocking production, React observability dashboard | ✅ Direct exact match |
| Evaluation tools / production-quality portfolio (not prototypes) | AgentProbe (live GitHub, 15-endpoint FastAPI, CI/CD gates), LeaseI (pass@k harness, LLM-as-judge, regression gate) | ✅ Direct |
| Orchestration frameworks | LangGraph, LangChain — primary stack in AgentProbe and LeaseI | ✅ Direct |
| Vector databases | ChromaDB in AgentProbe + LeaseI | ✅ Direct |
| 1+ years AWS Bedrock/Agents | AWS S3/RDS/Glue at Entrata — NOT Bedrock specifically | ⚠️ Gap (AWS foundation transfers; Bedrock is a managed LLM service layer) |
| MCP servers | MCP familiarity as user — no production MCP server shipped | ⚠️ Partial (listed as "ideal," not required) |
| Go | Not in production stack | ❌ Gap (role accepts Python OR Go OR TypeScript — Python+TS cover it) |

**Gaps:**
1. **AWS Bedrock** — managed LLM service on AWS. AWS cloud knowledge (S3, RDS, Glue, IAM) transfers directly; Bedrock adds an API layer, not a new paradigm.
2. **MCP servers** — tool-calling architecture in AgentProbe is directly adjacent. MCP is a protocol; AgentProbe already implements inter-agent tool calling.
3. **IT/internal context** — automating internal workflows vs. customer-facing product AI. Skills transfer 100%; framing shifts slightly.

---

## C) Level and Strategy

**Level detected:** Mid-Senior IC (4+ YOE, production AI required)
**Parimala's natural level:** Senior (8+ YOE) — overqualified on YOE, exact fit on stack

**Framing:**
- Lead with AgentProbe: "I built exactly what this role describes — production multi-agent system with eval infrastructure, CI/CD regression gates, and observability dashboard. Live GitHub, not slides."
- On "production mindset": "Every AI system I build has eval gates before production. AgentProbe blocks failing runs automatically — that's the observability + testing mindset the JD calls for."
- On AWS Bedrock: "I ran AWS at production scale for PHI-compliant data pipelines. Bedrock is the managed LLM layer on infrastructure I already know — different service, same cloud."
- On MCP: "AgentProbe implements tool-calling and inter-agent state handoffs — MCP is the same concept as a protocol. Straightforward extension."

---

## D) Comp and Demand

| Data Point | Detail |
|------------|--------|
| JD stated comp | $154,347–$170,709 base (Mountain View — California pay transparency) |
| Estimated McLean range | $130K–$160K (cost-of-living adjusted, ~15% below Mountain View) |
| Vs Parimala's target ($100–140K) | Exceeds target at any point in the range |
| H-1B / Visa sponsorship | Not explicitly stated — application asks about "future sponsorship needs" (ambiguous) |
| ID.me H-1B history | Needs verification — government contractor context may add complexity |
| Background check | "Extensive" — ID.me contracts with IRS, VA, state unemployment agencies |

---

## E) Customization Plan

**Pending user decision — below 4.5 threshold.**

If user overrides and applies:

| # | Section | Proposed Change | Why |
|---|---------|-----------------|-----|
| 1 | Headline | "AI Engineer · LangGraph · Multi-Agent · RAG · Agentic Pipelines · LLMOps · Python · TypeScript · AWS · Production Eval" | Matches role vocabulary exactly |
| 2 | Summary | Lead with AgentProbe "production mindset" framing — eval gates, observability, CI/CD. Map LeaseI as production RAG proof. | JD's "production-quality automations (not prototypes)" is the key filter |
| 3 | AgentProbe | Emphasize eval engine + CI/CD regression gates + observability dashboard + MCP-adjacent tool calling | Direct match to JD language |
| 4 | Entrata | Add AWS depth — "ran S3/RDS/Glue at production scale, extending to Bedrock" framing | Closes Bedrock gap |
| 5 | Skills | Add "AWS Bedrock (familiar, extending AWS infrastructure background)" | Acknowledges gap honestly |

---

## F) Interview Plan

| # | JD Requirement | STAR+R Story | Reflection |
|---|----------------|-------------|------------|
| 1 | Production mindset — observability, testing, evaluations | AgentProbe: 5-metric LLM-as-judge eval engine; CI/CD gates block every failing run before production; React dashboard with per-run metrics, latency, retrieval drift | Production AI without eval infrastructure is staging. I treat eval as part of shipping, not an afterthought |
| 2 | Build and deploy RAG pipelines | LeaseI: 93.6% precision on 1,240 legal PDFs — extraction, chunking, embedding, retrieval, deterministic rules engine, pass@k eval harness | RAG precision comes from chunking strategy and retrieval tuning, not just model selection |
| 3 | Multi-agent orchestration | AgentProbe 3-agent LangGraph runtime (Orchestrator → RAG Tracer → Auto Fix), tool calling, inter-agent state handoffs, conditional routing | The hardest multi-agent problem is state recovery at failure — not the happy path |
| 4 | AWS production experience | Entrata: AWS S3/RDS/Glue migration — 100% PHI compliance, zero incidents across all client data | I know the AWS IAM/security model. Adding Bedrock is adding a service, not relearning a platform |
| 5 | Portfolio of production-quality automations | AgentProbe (live GitHub, 15-endpoint FastAPI, 3 LangGraph agents, CI/CD): not a demo, not a prototype. LeaseI: production RAG with regression-gated eval harness | Both are live. That's the distinction the JD asks for |

**Government background check context:**
- ID.me processes identity verification for IRS, VA, state unemployment. Extensive background check expected.
- OPT status is lawful US work authorization — not disqualifying. But some government-contractor contracts have residency or citizenship preferences not disclosed in JD.
- **Action item:** Before investing application effort, ask recruiter: "Does this role have any citizenship or residency requirements due to government contracts?"

---

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|--------|---------|--------|
| Greenhouse posting | Active Greenhouse job board — ID.me's standard ATS | Positive |
| Specific tech stack | AWS Bedrock, MCP servers, orchestration frameworks, evaluation tools — highly specific, not boilerplate | Positive |
| "Not prototypes" filter language | Explicit qualifier signals a real open req with a hiring bar | Positive |
| Comp range disclosed | $154,347–$170,709 — specific range under California pay transparency | Positive |
| Team context | Corporate AI Enablement & Efficiency — specific internal org | Positive |
| Background check / drug test | Consistent with government identity contractor, not a ghost indicator | Neutral |
| Visa sponsorship unclear | Application asks about future needs — does not confirm or deny | Neutral |

---

## Verdict

**Score 4.3/5 — just below 4.5 threshold. Hold for user decision.**

**Strong case FOR applying:**
- Near-perfect stack match: Python, LangGraph, RAG, eval frameworks, vector DBs, multi-agent — every core requirement is a direct proof point
- Exceptional comp ($154K–$170K Mountain View / est. $130K–$160K McLean) — well above $100–140K target
- McLean, VA — zero relocation, near candidate, same time zone
- "Production mindset" JD language maps exactly to AgentProbe CI/CD eval gates

**Why not 4.5:**
- Full onsite 5 days/week — not remote-flexible; daily commute in McLean
- Visa sponsorship unconfirmed — ID.me government work adds ambiguity about H-1B sponsorship willingness
- Government background check process may have residency preferences not stated in JD
- Internal IT enablement framing (vs. product-facing AI) — minor, but a slight fit gap

**Recommended action:** Verify ID.me H-1B sponsorship history and ask recruiter about citizenship/residency requirements. If sponsorship is confirmed and no citizenship block exists, override threshold — comp and stack match justify it.

---

## Keywords Extracted

AI Enablement Engineer, LLM, RAG, agents, MCP servers, AWS Bedrock, AWS Agents, Python, TypeScript, Go, vector database, orchestration frameworks, LangGraph, LangChain, evaluation tools, LLM evaluation, observability, production AI, multi-agent, CI/CD, McLean Virginia, identity verification

---

## Machine Summary

```yaml
company: ID.me
role: AI Enablement Engineer, IT
score: 4.3
status: Evaluated
date: 2026-06-25
location: McLean VA / Mountain View CA (full onsite 5d/wk)
salary_range: "$154K–$171K (Mountain View stated; McLean est. $130K–$160K)"
visa_sponsorship: unclear (government contractor context; no explicit policy)
h1b_risk: medium-high
archetype: Agentic / Automation + AI Platform / LLMOps
pdf: N/A (pending user decision)
url: https://job-boards.greenhouse.io/idme/jobs/7777644003
```
