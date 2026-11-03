# 295 — Smartsheet — Senior Software Engineer I, Automation

**Date:** 2026-09-08
**Score:** 2.5/5 — SKIP (H-1B likely blocked: "legally eligible to work in the U.S. on an ongoing basis" = no sponsorship language; Senior at 3,000-person public company = formal leveling concern; agentic AI / HITL / RAG / MCP alignment is strong; Step Functions / Bedrock Agents / UiPath / Datadog gaps; remote US ✓; comp undisclosed)
**URL:** Smartsheet careers
**PDF:** ❌
**Legitimacy:** High Confidence — Smartsheet is a publicly traded SaaS company (NYSE: SMAR, ~$2B market cap); JD is specific to the Automation team with concrete technical requirements; salary range not disclosed but benefits listed in detail; no ghost indicators

---

## Block A — CV Match

**Strong alignment on the AI/automation core — agentic workflows, HITL, RAG, MCP all map directly to LeaseI and AgentProbe. The AWS-specific products (Step Functions, Bedrock Agents) and enterprise tools (UiPath, Datadog) are the meaningful gaps. H-1B language is the primary blocker.**

| JD Requirement | CV Proof Point |
|---------------|----------------|
| "5+ years building scalable applications or enterprise-grade integration services" | 9yr 8mo professional SWE; Entrata: multi-tenant SaaS, 100K+ MAU, 99.5% uptime ✓✓ |
| "5+ years Python, JavaScript/Node.js, or TypeScript" | Python 9yr ✓✓; TypeScript ✓; JavaScript ✓; Node.js ⚠️ (TypeScript background but Node.js not standalone) |
| "1+ years GenAI/agentic workflows with measurable business impact" | AgentProbe (production LLM platform); LeaseI (8-agent HITL platform, 93.6% precision); Magizhs (customer-facing agentic AI deployed to external client) ✓✓✓ |
| "Design Agentic Workflows using AWS Step Functions and Bedrock Agents" | LangGraph (8-agent StateGraph with conditional edges, memory, HITL) ✓✓; AWS Step Functions ✗; Bedrock Agents ✗ (uses Anthropic API directly — conceptual transfer credible) |
| "MCP & Protocol Mastery: MCP, REST APIs, OAuth" | MCP listed in technical skills ✓; FastAPI (15-endpoint REST) ✓✓; OAuth not explicitly implemented ⚠️ |
| "Optimize RAG Performance: chunking, embedding, vector DB" | AgentProbe: ChromaDB embeddings, multi-provider RAG; LeaseI: section-aware chunking, TF-IDF retrieval, reranking ✓✓✓ |
| "Design Human-in-the-Loop: UiPath Action Center as safety gate for AI decisions" | LeaseI: HITL escalation when confidence below threshold; deterministic safety boundary for tenant agent ✓✓ (UiPath ✗ — different tool, same pattern) |
| "Standardize Context via MCP across org" | MCP in technical skills ✓ — but enterprise-scale MCP implementation across CRM/ERP not in background ⚠️ |
| "AWS Step Functions, EventBridge, SQS/SNS" | RabbitMQ async (event-driven pattern) ✓/⚠️; AWS SQS/SNS ✗; Step Functions ✗; EventBridge ✗ |
| "Observability: Datadog, CloudWatch" | Production monitoring at Entrata (internal tools); CloudWatch adjacent through AWS work ⚠️; Datadog not in background ✗ |
| "Mentor junior/mid engineers on AI prompt engineering, MCP, UiPath" | Entrata: 5+ engineers mentored; GMU: 600+ students ✓; UiPath mentoring ✗ |
| "Agile/Scrum, technical roadmaps with PMs" | 120+ Agile sprints at Entrata; cross-functional delivery ✓✓ |
| "Production support rotation, root-cause analysis" | Entrata: production incident ownership, debugging tools reducing triage 40% ✓ |
| "Legally eligible to work in the U.S. on an ongoing basis" | F-1 STEM OPT → H-1B sponsorship required; "ongoing basis" = no sponsorship language ✗ |

**Hard Gaps:**
- **H-1B: "legally eligible on an ongoing basis"** — this phrase is standard language for companies that do not sponsor immigration; F-1 STEM OPT satisfies current eligibility but not "ongoing" without H-1B sponsorship; Smartsheet's public H-1B filing history would need verification
- **AWS Step Functions / EventBridge / SQS/SNS** — the AWS orchestration stack this team uses; RabbitMQ is the event-driven analogue but different product and operational model
- **Amazon Bedrock Agents** — required for the agentic workflow architecture; uses Anthropic API directly, not through Bedrock; conceptual transfer is real but product-specific interview questions will expose the gap
- **UiPath Integration Service + Action Center** — RPA platform; completely absent from background; the HITL pattern is the same but UiPath is its own product ecosystem
- **Datadog** — observability platform; not in background; CloudWatch is adjacent but Datadog is a distinct tool with its own query language and dashboards

**ATS baseline:** ~13/20. Python ✓, TypeScript ✓, agentic AI ✓, RAG ✓, HITL ✓, MCP ✓, REST APIs ✓, AWS ✓. Step Functions/Bedrock/UiPath/Datadog/EventBridge all missing.

---

## Block B — North Star Alignment

**AI automation platform — adjacent to the AI Platform / Applied AI archetype.** The Automation team at Smartsheet builds agentic workflows, HITL controls, RAG systems, and MCP integrations for internal enterprise use — similar to what FDE does for external customers, but internal-facing. The technical depth (agentic, HITL, RAG, MCP) maps well.

**"Senior Software Engineer I" at Smartsheet (~3,000 employees, public company):** Smartsheet levels as SWE I → SWE II → Senior SWE I → Senior SWE II → Principal. "Senior SWE I" is the entry point of Senior — roughly equivalent to a strong mid-level at FAANG companies. The formal leveling concern applies but is less severe than at Amazon or Google; Smartsheet's engineering bar for Senior I is more achievable with the background.

The H-1B language is the dominant concern. If Smartsheet confirms H-1B sponsorship, this role re-evaluates significantly higher.

**Score: 2.5/5** (strong AI automation match; H-1B likely blocked; formal leveling; product stack gaps)

---

## Block C — Compensation

**Undisclosed.** "Competitive base salary" + 401K (50% match up to 6%) + monthly productivity stipend + 12 paid holidays + 24 weeks parental leave + Udemy access. For a Senior SWE I at a ~$2B public SaaS company on the West Coast (Bellevue HQ, remote eligible), estimate $140K–$185K base + equity (public company RSUs). No disclosed range to confirm.

**Score: 3.0/5**

---

## Block D — Cultural Signals

- **Remote-first US** — "work remotely from anywhere in the US where Smartsheet is a registered employer" — Virginia qualifies ✓✓ (zero relocation cost, immediate start)
- "Treating internal systems with the same rigor as customer-facing software" — engineering-first mindset ✓
- Agentic AI + HITL + MCP as core team direction — matches technical priorities ✓
- Public company (NYSE: SMAR) — stable, structured, not startup chaos ✓
- Agile/Scrum + production support rotation — mature engineering culture ✓
- H-1B: "legally eligible on an ongoing basis" — likely no sponsorship ✗
- UiPath/Datadog/Step Functions culture — enterprise tooling stack; different from Parimala's current stack ⚠️

**Score: 3.5/5** (remote ✓✓; AI-forward ✓; public company stable ✓; H-1B likely blocked ✗)

---

## Block E — Red Flags

1. **H-1B likely blocked** — "legally eligible to work in the U.S. on an ongoing basis" is standard no-sponsorship language; F-1 STEM OPT gives 3yr current authorization but does not satisfy "ongoing basis" without H-1B approval; Smartsheet's actual H-1B filing history would need verification before applying
2. **Senior at public company (~3,000 employees)** — formal leveling applies; "Senior SWE I" is the lower Senior tier, making the bar more achievable than Senior at FAANG, but still a structured evaluation with leveling criteria
3. **AWS Step Functions / Bedrock Agents** — the orchestration and AI product stack this team uses; LangGraph/Anthropic API is the background equivalent but different products with different operational models
4. **UiPath** — RPA platform with its own product ecosystem; Action Center is the HITL tool they use; no background in UiPath means one of the three core technical pillars (agentic / HITL via UiPath / RAG) has a product gap
5. **Datadog** — required for observability; not in background

**Adjustment: −0.5**

---

## Block F — Global Score

| Factor | Signal |
|--------|--------|
| CV match | 3.0 — agentic ✓✓; HITL ✓✓; RAG/chunking/embeddings ✓✓; MCP ✓; Python ✓✓; TypeScript ✓; Step Functions/Bedrock/UiPath/Datadog ✗; H-1B language ✗ |
| North Star | 2.5 — AI automation = adjacent archetype; Senior I at public company (milder than FAANG); H-1B likely blocked; product stack gaps |
| Comp | 3.0 — undisclosed; estimated $140K–$185K; 401K match; remote adds real value; public equity |
| Culture | 3.5 — remote US ✓✓; engineering-first ✓; agentic AI direction ✓; H-1B likely blocked ✗ |
| Red flags | −0.5 — H-1B likely blocked; formal leveling; Step Functions/Bedrock/UiPath/Datadog gaps |

**Global: 2.5/5 — SKIP**

> The agentic AI + HITL + RAG + MCP technical match is genuinely strong — LeaseI covers HITL and agentic, AgentProbe covers RAG and LLMOps, MCP is in the skills list. The remote-US position is a real win. But the "legally eligible to work in the U.S. on an ongoing basis" language is almost certainly no-sponsorship, which makes the application impossible without H-1B approval in hand. Beyond that, the Step Functions / Bedrock Agents / UiPath product stack are all required skills where the background has conceptual analogues but not the same tools. If you can verify Smartsheet sponsors H-1B (check their LCA filings at h1bdata.info), this re-evaluates to ~3.2/5 and is worth a push.

---

## Block G — Posting Legitimacy

**High Confidence.** Smartsheet is a publicly traded SaaS company (NYSE: SMAR). JD is specific and internally consistent (Automation team, AWS AI&Data stack, UiPath integration, MCP implementation). Benefits listed in detail. The Bellevue HQ and remote-US option are consistent with Smartsheet's known operations. No ghost indicators.

---

## Machine Summary

```yaml
company: Smartsheet
role: Senior Software Engineer I, Automation
score: 2.5
status: SKIP
date: 2026-09-08
salary_low: null
salary_high: null
location: Remote US (Bellevue, WA HQ; Virginia eligible)
remote: true
visa: likely_blocked ("legally eligible to work in the U.S. on an ongoing basis" = no sponsorship language; verify at h1bdata.info)
proptech_boost: false
h1b_status: likely_blocked
top_match: Agentic AI (LeaseI 8-agent HITL); RAG/chunking/embeddings (AgentProbe); MCP in skills; Python; TypeScript; HITL design; remote US; Agile/mentorship
gaps: H-1B likely blocked; Step Functions/EventBridge/SQS; Bedrock Agents; UiPath Action Center; Datadog; Senior at public company (formal leveling)
```
