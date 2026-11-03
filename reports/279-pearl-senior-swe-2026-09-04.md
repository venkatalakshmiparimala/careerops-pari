# 279 — Pearl — Senior Software Engineer

**Date:** 2026-09-04
**Score:** 3.0/5 — SKIP
**URL:** N/A (JD provided directly — Pearl)
**PDF:** ❌
**Legitimacy:** High Confidence — Pearl is a real, funded dental AI company (founded 2019, $58M Series B 2022); FDA-cleared computer vision product; JD is technically specific and credible

---

## Block A — CV Match

**Agentic/LLM systems match is strong. Node.js/TypeScript as primary backend is the critical gap — user is Python-primary; no production Node.js experience in background.**

| JD Requirement | CV Proof Point |
|---------------|----------------|
| "LLM-based systems — prompting, structured outputs, tool usage" | AgentProbe (Anthropic + OpenAI APIs); LeaseI (tool routing, structured evidence outputs) ✓ |
| "Agentic systems with tool-calling" | LeaseI 8-agent LangGraph (tool-calling, HITL, conditional routing); AgentProbe agentic eval ✓ |
| "Claude / Cursor / Copilot — hands-on AI coding tools" | Claude Code daily use ✓ |
| "PostgreSQL — production scale" | 200+ SQL query optimizations at Entrata; complex multi-tenant schemas; 8yr ✓ |
| "React — frontend" | AI on FHIR: React.js/TypeScript frontend ✓ |
| "AWS (S3, Lambda, SQS)" | AWS S3/EC2/RDS/Glue at Entrata ✓; Lambda and SQS not in background ⚠️ |
| "Event-driven systems (Kafka/SQS)" | RabbitMQ async processing at Entrata (adjacent; retry, idempotency, DLQ) ⚠️ |
| "5+ years production software engineering" | 8yr at Entrata + Magizhs ✓ |
| Multi-tenant SaaS (nice-to-have) | Entrata is multi-tenant SaaS at scale ✓ |
| ETL pipelines (nice-to-have) | HUD income-limit pipeline, data migrations, S3 document pipeline at Entrata ✓ |
| Healthcare/dental tech (nice-to-have) | AI on FHIR (healthcare-adjacent); no dental/imaging background ⚠️ |
| Agent frameworks (nice-to-have) | LangGraph, LangChain ✓ |
| **Node.js / TypeScript as primary backend** | TypeScript listed in skills (used frontend in AI on FHIR); **no production Node.js backend experience** — Python/PHP are the primary backend languages ❌ |

**Gaps:**
- **Node.js/TypeScript as primary backend** — required, not nice-to-have; user is Python/PHP primary; ATS will miss Node.js keywords in backend context
- **AWS Lambda, SQS** — S3/EC2/RDS confirmed; Lambda and SQS not in background
- **Dental/healthcare domain** — AI on FHIR is healthcare-adjacent but not imaging or clinical AI
- **IaC** — not in background

**ATS baseline:** ~14/20. Strong on LLM/agentic, Claude Code, PostgreSQL, event-driven, multi-tenant SaaS. Gap on Node.js (primary backend), Lambda, SQS, healthcare domain terms.

---

## Block B — North Star Alignment

**Archetype: Software Engineer (AI-focused) — correct archetype.** The agentic systems and LLM integration requirements (tool-calling, structured outputs, multi-step reasoning) map directly to AgentProbe and LeaseI. Claude Code explicit in JD is a strong alignment signal. However, the role requires Node.js/TypeScript as the backend language, not Python — this is the primary technical friction. User's TypeScript experience is frontend-only (AI on FHIR); backend production is Python/PHP.

Pearl is a founded-2019 startup (~100-200 employees at Series B stage) — below the 200-employee formal-leveling threshold; the "Senior" title hard block does not fully apply here. However, technical screening will probe Node.js depth specifically, where the background is thin.

**Dental AI domain** is niche and off-target — not PropTech, not fraud, not general enterprise SaaS. The agentic engineering case (AgentProbe + LeaseI) is compelling for the LLM systems angle but doesn't bridge the stack mismatch.

**Score: 3.0/5**

---

## Block C — Compensation

**Undisclosed.** Pearl raised $58M Series B in 2022. For a US remote Senior SWE at a funded dental AI startup, typical market rate is $130K–$180K base + equity. The equity may have meaningful upside if Pearl continues to scale in the dental AI market, but there is no comp signal to score above baseline.

**Score: 2.5/5**

---

## Block D — Cultural Signals

- Remote across United States — no relocation ✓
- AI-native company — LLM systems, agentic workflows, Claude/Copilot in JD — not AI-washing
- FDA-cleared product — engineering rigor; compliance-minded culture (familiar from Entrata)
- Series B startup (founded 2019) — structured enough to avoid chaos, small enough to have real scope
- Dental tech is a niche — neither a positive nor negative signal for culture fit
- H-1B: Pearl has VC backing and is a real company; likely sponsors but unconfirmed

**Score: 3.5/5**

---

## Block E — Red Flags

1. **Node.js/TypeScript primary backend** — the JD's primary technical requirement is Node.js; user is Python-primary; ATS filtering and technical screening both carry risk here; this is the single biggest blocker
2. **Comp undisclosed** — no signal; startup; could be below target or could be competitive; no way to score
3. **H-1B unconfirmed** — Series B startup with VC backing; likely sponsors but not confirmed; worth verifying before investing in prep
4. **Dental/healthcare domain gap** — nice-to-have, not required, but lack of any clinical/dental context limits differentiation at interview

**Adjustment: −0.3**

---

## Block F — Global Score

| Factor | Signal |
|--------|--------|
| CV match | 3.0 — Agentic/LLM, Claude Code, PostgreSQL, React, event-driven, multi-tenant SaaS all match; Node.js primary backend is the critical gap; Lambda/SQS not in background |
| North Star | 3.0 — SWE AI-focused archetype ✓; startup-appropriate Senior title; Node.js stack mismatch is the primary friction; dental domain is off-target |
| Comp | 2.5 — undisclosed; Series B startup; estimated $130K–$180K but no signal |
| Culture | 3.5 — remote US, AI-native, agentic focus, compliance-minded (FDA-cleared) |
| Red flags | −0.3 — Node.js primary gap; comp undisclosed; H-1B unconfirmed; dental domain gap |

**Global: 3.0/5 — SKIP**

> Node.js/TypeScript as the primary backend language is the blocker. The agentic/LLM fit (AgentProbe, LeaseI, Claude Code) is strong and would resonate in a Python shop. At Pearl, the recruiter screen and technical assessment will probe Node.js depth specifically — and that depth isn't there. If Pearl has a Python-backend team or the user is willing to ramp on Node.js explicitly, this could be worth a conversation. Otherwise, the stack mismatch + undisclosed comp + unconfirmed H-1B don't justify the investment.

---

## Block G — Posting Legitimacy

**High Confidence.** Pearl is a real, VC-backed dental AI company (founded 2019, $58M Series B). FDA clearance for computer vision product is documented. JD is technically specific (Node.js, PostgreSQL, LangGraph-adjacent frameworks, tool-calling patterns). No ghost indicators.

---

## Machine Summary

```yaml
company: Pearl
role: Senior Software Engineer
score: 3.0
status: SKIP
date: 2026-09-04
salary_low: null
salary_high: null
location: Remote (United States)
remote: true
visa: unconfirmed (Series B startup)
proptech_boost: false
h1b_status: unconfirmed
top_match: Agentic/LLM systems, Claude Code, PostgreSQL, React, multi-tenant SaaS, event-driven patterns
gaps: Node.js primary backend (critical), AWS Lambda/SQS, dental/healthcare domain, comp undisclosed, H-1B unconfirmed
```
