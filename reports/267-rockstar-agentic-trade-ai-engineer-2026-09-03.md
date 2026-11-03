# 267 — [Unnamed via Rockstar] — AI Engineer, Agentic Execution System (Global Trade)

**Date:** 2026-09-03
**Score:** 3.8/5 — APPLY
**URL:** N/A (JD provided via Rockstar recruiting; company unnamed)
**PDF:** ❌
**Legitimacy:** Proceed with Caution — Company is unnamed in JD; all signals point to a real seed-stage startup (oversubscribed round, named VCs in NYC and SF, specific domain), but identity requires verification before applying

---

## Block A — CV Match

**Technical alignment is exceptional — the role description reads like a spec written against AgentProbe + LeaseI.**

| JD Requirement | CV Proof Point |
|---------------|----------------|
| "Agentic harness: tool routing, policy enforcement, memory, grounding" | LeaseI: 8-agent LangGraph StateGraph with real conditional edges, routing logic, SQLite state/memory, deterministic policy guardrails, citation grounding ✓ |
| "Tool calling, MCP, context engineering" | MCP in skills; Claude Code MCP integration; LeaseI tool calling throughout; AgentProbe multi-provider routing ✓ |
| "Evaluation and reliability infrastructure safe enough for financial actions" | AgentProbe: CI-integrated regression gate, 5-metric eval engine (correctness, groundedness, hallucination rate), LLM-as-judge — zero regressions shipped across 1,240+ test cases ✓ |
| "Ingesting unstructured, contradictory data from emails, documents, legacy systems" | LeaseI: OCR-fallback document ingestion (pdfplumber, pytesseract), multi-source RAG retrieval, missing/conflicting clause detection ✓ |
| 4+ years high-quality engineering environments | 8yr production Python at Entrata (enterprise SaaS at 100K+ MAU, 99.5% uptime) ✓ |
| Python, TypeScript, AWS/GCP | Python 8yr; TypeScript; AWS S3, EC2, RDS, Glue ✓ |
| "Judgment about model tradeoffs — reliable, cost-efficient, not just impressive demos" | AgentProbe multi-provider routing (Anthropic/OpenAI/Ollama) for cost optimization; LeaseI hand-rolled TF-IDF RAG (deliberate choice over LangChain vector DB) — engineering judgment over hype ✓ |
| LLM evaluation (valued) | AgentProbe is an LLM evaluation framework — 5-metric engine, LLM-as-judge, CI-integrated ✓ |
| Mentoring future engineers (valued) | Mentored 5+ engineers at Entrata; 600+ students at GMU ✓ |
| High ownership, bias for action | 7yr solo ownership of HUD income-limit pipeline; built AgentProbe + LeaseI end-to-end independently ✓ |

**Gaps:**
- Neo4j / graph databases — not in background (SQLite, PostgreSQL; graph DB is a meaningful gap for "context graph" core)
- Supply chain / global trade domain — no direct experience (adjacent: Entrata financial/compliance transactions, RabbitMQ async at volume)
- Startup experience — single employer background; GMU and Magizhs internship; limited early-stage startup context

**ATS baseline:** ~17/20. Strong on agentic, eval, Python, AWS, reliability, MCP, tool calling. Gap: graph databases.

---

## Block B — North Star Alignment

**Archetype: Agentic / Automation — the highest-priority archetype in the target list.** "Agents don't assist with the work — they do it" is the literal definition of Agentic / Automation. The reliability focus ("right 95% of the time isn't good enough") is the exact problem AgentProbe was built to solve. Early engineer scope ("more like a technical founder's than a spec to implement") fits the profile of someone who built two full AI systems independently. This is a rare case where the role description maps almost exactly to existing portfolio work.

**Score: 4.5/5**

---

## Block C — Compensation

Undisclosed. Seed stage early AI engineer (well-funded, oversubscribed round, leading VCs) in 2026 agentic AI space: estimated $160K–$220K base + 0.5–1.5% equity. Equity upside is meaningful if the company succeeds. However no salary is confirmed and seed-stage risk is real. Cannot score above 3.5 without a disclosed number.

**Score: 3.5/5**

---

## Block D — Cultural Signals

- "Real product ownership" + "scope looks more like an early technical founder's" — matches a candidate who built two production AI systems solo
- "Bias for action," "direct communication," "high ownership" — consistent with the writing style and background
- "Works directly with how enterprise customers operate" — forward-deployed element; cross-functional delivery
- Onsite San Francisco — Virginia-based candidate; relocation required; no relocation package mentioned in JD
- Seed stage — high upside, high risk; smaller team, faster iteration, more ambiguity
- Strategy note: "prefer 2-3 round processes; boost startups Series A–C" — seed is earlier than preferred but not excluded

**Score: 3.5/5**

---

## Block E — Red Flags

1. **Onsite San Francisco — no relocation package stated** — Virginia → SF relocation is a significant commitment; worth clarifying immediately with the recruiter
2. **H-1B at seed stage** — small early-stage companies can sponsor but infrastructure is thinner; verify explicitly before investing application effort
3. **Company unnamed** — identity not confirmed; cannot verify funding claims or team background without additional research
4. **Neo4j / graph database gap** — "context graph" is core to the role; this is a meaningful skill gap, not a peripheral one; JD notes "drive to learn fast" as acceptable
5. **No salary disclosed** — standard for recruiter-placed seed roles; estimate is strong but unconfirmed

**Adjustment: -0.4**

---

## Block F — Global Score

| Factor | Signal |
|--------|--------|
| CV match | 4.5 — agentic harness, tool calling, MCP, LLM eval, reliability infra, Python, TypeScript, AWS — near-perfect; Neo4j is the only meaningful gap |
| North Star | 4.5 — Agentic/Automation archetype #1; reliability + evaluation for financial-consequence AI = AgentProbe's exact problem statement |
| Comp | 3.5 — undisclosed; seed early AI engineer signals $160K–$220K + equity; unconfirmed |
| Culture | 3.5 — founding engineer ownership culture fits; onsite SF relocation is the main drag |
| Red flags | -0.4 — onsite SF no relocation, H-1B at seed, unnamed company, Neo4j gap |

**Global: 3.8/5 — APPLY**

> Below the 4.5 threshold for non-PropTech roles, but the technical alignment here is the strongest in the pipeline outside Balerion AI. The role is asking for exactly what AgentProbe and LeaseI demonstrate. Worth pursuing — verify company identity and H-1B sponsorship first via the recruiter.

---

## Block G — Posting Legitimacy

**Proceed with Caution.** Placed via Rockstar recruiting — a legitimate technical recruiting firm. The JD is detailed, technically specific, and consistent with a real seed-stage AI startup (specific domain, named VC backing in NYC and SF, specific technical requirements). However the company is unnamed, which is normal for recruiter-placed roles at stealth or pre-announce startups but requires verification. Ask the recruiter for the company name and website before submitting materials.

---

## Machine Summary

```yaml
company: "[Unnamed via Rockstar recruiting]"
role: AI Engineer, Agentic Execution System
score: 3.8
status: Evaluated
date: 2026-09-03
salary_low: null
salary_high: null
location: San Francisco CA (onsite, full-time)
remote: false
visa: unconfirmed (seed stage — verify before applying)
proptech_boost: false
h1b_status: unconfirmed
top_match: agentic harness + tool calling + MCP + LLM eval + reliability infra — maps directly to LeaseI + AgentProbe portfolio
gaps: Neo4j/graph databases (core to role), onsite SF relocation, H-1B at seed, company unnamed, no salary
```
