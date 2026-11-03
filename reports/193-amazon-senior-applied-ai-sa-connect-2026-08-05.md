# Evaluation: Amazon — Senior Applied AI Solutions Architect (Amazon Connect)

**Date:** 2026-08-05
**URL:** https://amazon.jobs/en/jobs/10467812/senior-applied-ai-solutions-architect-amazon-connect-applied-ai-sa-aivt
**Archetype:** AI Solutions Architect / Forward Deployed Engineer — customer-facing agentic AI deployment
**Score:** 3.0/5
**Legitimacy:** High Confidence
**PDF:** ❌

---

## A) Role Summary

| Dimension | Detail |
|-----------|--------|
| **Archetype** | Senior Applied AI SA — customer-facing; lead technical discovery, design agentic AI solutions, deploy MCP servers, build multi-agent workflows for Amazon Connect customers |
| **Domain** | Amazon Connect (cloud contact center) — AI velocity team accelerating customer adoption of Connect's AI capabilities |
| **Function** | Customer-facing deployment — discovery, PoC, production rollout, reusable implementation guides; 25–40% travel |
| **Seniority** | Senior (7+ years required) — L6/L7 equivalent at Amazon; competitive bar |
| **Location** | Herndon VA (+ SF, NYC, Seattle, Arlington, Denver, Atlanta, Chicago, Mountain View) — **Herndon is adjacent to Parimala's current location; zero relocation** |
| **H-1B** | Not stated — Amazon is a top-3 US H-1B sponsor, 10,000+ petitions annually; high confidence |
| **Comp** | $153,600–$207,800 (Herndon/other); $169,000–$228,600 (NYC); $176,600–$239,000 (SF) + RSUs + sign-on |
| **Interview** | Amazon standard: 5–6 rounds (phone screen, virtual loop, bar raiser, leadership principles, system design, technical) — **confirmed 4+ round process** |
| **TL;DR** | Strong agentic AI + SA profile overlap; Herndon VA = zero relocation; Amazon H-1B = certain. Three blockers: Amazon Connect domain gap, Bedrock/Lambda/serverless gaps, and Amazon's 5–6 round loop conflicts hard with 2-round preference (−1.0 penalty). Score 3.0 — SKIP. |

---

## B) Match with CV

| JD Requirement | CV Evidence | Strength |
|----------------|-------------|----------|
| Agentic AI patterns (multi-agent, tool use, function calling) | LeaseI 8-agent LangGraph; AgentProbe 3-agent runtime with tool calling | Strong |
| Technical discovery + customer solution design | Entrata cross-functional delivery across Compliance/Legal/Ops/Product (120+ sprints); Magizhs production deployment with client verticals | Partial |
| Prompt engineering + agent creation | LeaseI prompt design; Magizhs chain-of-thought + structured outputs | Strong |
| RAG / document processing / embeddings / vector search | LeaseI TF-IDF RAG; AgentProbe ChromaDB RAG | Strong |
| Python | Primary language, 8+ years | Strong |
| AWS (general) | Entrata production (S3, EC2, RDS, Glue); 100% PHI compliance migration | Strong |
| 7+ years technology experience | 8+ years total | Meets |
| MCP (Model Context Protocol) | Familiarity via Claude Code daily use; has NOT built MCP servers | **Weak** |
| **Amazon Connect domain** | Not in background — no contact center / CCaaS experience | **Gap** |
| **Amazon Bedrock** | Not in background (uses Anthropic/OpenAI APIs directly, not Bedrock) | **Gap** |
| **Serverless (Lambda, API Gateway, Step Functions)** | Not in stack | **Gap** |
| Agent-to-Agent communication patterns | LangGraph inter-agent state handoffs (analogous) | Partial |
| 25–40% travel | No prior travel-heavy role | Flag |
| Senior-level bar (7+ YOE, competitive Amazon loop) | 8+ years but single employer; Amazon bar is extremely high | Concern |

---

## C) Level and Strategy

**Score: 3.0/5 — SKIP**

Two compounding reasons:

**1. Amazon interview loop: confirmed 4+ rounds (−1.0 penalty)**
Amazon's standard loop for Senior SA: recruiter screen → phone technical → virtual on-site (4–5 rounds: technical, system design, leadership principles × 2, bar raiser). This is not speculation — it is Amazon's published process. Hard preference is 2 rounds maximum. −1.0 applied per strategy.

**2. Domain + stack gaps**
Amazon Connect is a specific product (cloud contact center). This SA role is focused on accelerating Connect AI adoption — customers will ask product-specific questions. No CCaaS or contact center background in CV. Bedrock (Amazon's managed LLM service) is the implied delivery vehicle; Parimala has used Anthropic/OpenAI APIs directly, not Bedrock. Lambda/Step Functions serverless not in stack.

**What's genuine:** The agentic AI fundamentals (multi-agent orchestration, tool calling, RAG, confidence scoring, HITL) are real and map well. The SA angle (customer-facing, PoC to production) aligns with Entrata cross-functional delivery. Herndon VA location and Amazon H-1B certainty are strong positives — but can't overcome the process and domain gaps at this score level.

**If the user wants to pursue anyway:** The strongest angle is the agentic AI depth (LeaseI + AgentProbe) + AWS production experience (Entrata). The MCP gap is bridgeable with a few hours of self-study (building a simple MCP server). Bedrock gap is harder — needs hands-on project before applying. Amazon interview prep requires 4–6 weeks minimum (LP stories × 14 principles, system design, coding).

---

## D) Comp and Demand

| Item | Data |
|------|------|
| Herndon VA salary | $153,600–$207,800 |
| NYC salary | $169,000–$228,600 |
| SF salary | $176,600–$239,000 |
| RSUs | Yes — standard Amazon RSU grant |
| Sign-on | Yes — available |
| H-1B | High confidence — Amazon top-3 US sponsor |
| Location | Herndon VA available — zero relocation |
| Interview | 5–6 rounds (confirmed Amazon process) |
| Comp score | 5/5 — exceptional range, fully disclosed |

---

## E) Customization Plan

Not applicable — SKIP. If pursuing: would need to build Bedrock + MCP server project first.

---

## F) Interview Plan

Not applicable — SKIP. Amazon LP prep alone requires 4–6 weeks dedicated preparation.

---

## G) Posting Legitimacy

| Signal | Finding | Weight |
|--------|---------|--------|
| Company | Amazon / AWS — NYSE: AMZN, $2T+ market cap | Positive |
| Job ID | 10467812 — real AWS careers posting | Positive |
| Comp | $153K–$239K disclosed with city breakdown — high transparency | Positive |
| Locations | 9 US cities including Herndon VA | Positive |
| Recruiting deadline | 08/30/2026 — active window | Positive |
| H-1B | Amazon files 10,000+ H-1B petitions/year | Positive |
| Travel | 25–40% travel requirement — real field SA role | Positive |

**Assessment: High Confidence** — Real, active Amazon posting with full compensation disclosure.

---

## Machine Summary

```yaml
company: Amazon (AWS)
role: Senior Applied AI Solutions Architect — Amazon Connect
date: 2026-08-05
score: 3.0
archetype: AI Solutions Architect / Forward Deployed Engineer
legitimacy: High Confidence
compensation: "$153,600–$239,000 depending on location + RSUs + sign-on"
h1b: High Confidence (Amazon top-3 US sponsor, 10,000+ petitions/year)
location: Herndon VA available (zero relocation) + 8 other US cities
verdict: skip
key_gap: Amazon Connect domain (CCaaS); Amazon Bedrock not in stack; Lambda/serverless not in stack; MCP server building (weak); Amazon 5-6 round loop (confirmed 4+ rounds = -1.0 penalty)
key_strength: agentic AI depth (LeaseI + AgentProbe); AWS production experience (Entrata); Herndon VA zero relocation; Amazon H-1B certainty; comp exceptional ($153K-$207K Herndon)
```

---

## Keywords extracted

Senior Solutions Architect, Amazon Connect, Applied AI, Agentic AI, Multi-Agent, MCP, Model Context Protocol, Agent-to-Agent, Amazon Bedrock, Lambda, API Gateway, Step Functions, Serverless, RAG, Embeddings, Vector Search, Hybrid Search, Prompt Engineering, Tool Calling, Function Calling, Customer-Facing, AWS, Python, Herndon VA
