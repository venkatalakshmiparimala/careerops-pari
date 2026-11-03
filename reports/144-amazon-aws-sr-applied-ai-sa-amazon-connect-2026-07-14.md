# Evaluation: Amazon (AWS) — Senior Applied AI Solutions Architect, Amazon Connect

**Date:** 2026-07-14
**URL:** https://www.amazon.jobs/en/jobs/10390088/senior-applied-ai-solutions-architect-amazon-connect-applied-ai-sa-aivt
**Archetype:** AI Solutions Architect (primary) + AI Forward Deployed (secondary)
**Score:** 3.8/5
**Legitimacy:** Proceed with Caution (recruiter outreach overrides; ask "backfill or new headcount?" in screen)
**PDF:** pending

---

## A) Role Summary

| Field | Detail |
|-------|--------|
| Archetype | AI Solutions Architect + AI Forward Deployed |
| Domain | Agentic AI / LLMOps — Amazon Connect + Amazon Bedrock |
| Function | Customer-facing technical deployment + architecture |
| Seniority | Senior (Amazon L6 equivalent) |
| Remote | Not remote; Herndon VA, Arlington VA, Seattle, NYC, Atlanta, Chicago, Denver, SF, Mountain View; 25–40% travel |
| Comp (listed) | $153,600–$207,800 base (Chicago); RSUs + sign-on on top |
| Deadline | **July 17, 2026 — 3 days** |
| TL;DR | Help enterprise customers deploy Amazon Connect AI — Bedrock model selection, agentic workflow design, MCP server configuration, A2A architecture, serverless integrations. Hands-on build + customer engagement hybrid. |

---

## B) Match with CV

| JD Requirement | CV Evidence | Match |
|---|---|---|
| 7+ years technology domain | 8+ years Entrata (Jan 2017–Aug 2024), Python/PHP/PostgreSQL/JS | ✅ |
| LLMs, prompt engineering, RAG | AgentProbe (RAG, ChromaDB, multi-provider routing); LeaseI (93.6% precision, 1,240 PDFs) | ✅ Strong |
| Agentic AI patterns | AgentProbe 3-agent LangGraph runtime (Orchestrator, RAG Tracer, Auto Fix), tool calling | ✅ Strong |
| MCP and/or A2A protocols | Not in CV by name; adjacent via AgentProbe tool calling + multi-agent state handoffs | ⚠️ Adjacent |
| 3+ years design/implementation | 20+ production modules, 120+ Agile sprints | ✅ |
| Travel 25–40% | Not in CV | ⚠️ Unstated |
| Amazon Bedrock | AWS (S3, EC2, RDS, Glue) present; Bedrock not explicit | ⚠️ Gap (preferred) |
| Amazon Connect / contact center | Zero experience | ❌ Gap (preferred) |
| Serverless (Lambda, API GW, Step Functions) | Not in CV; general AWS present | ⚠️ Gap |
| CI/CD pipelines | GitHub Actions in AgentProbe | ✅ |
| CS/ML degree or AWS cert | MS Data Analytics Engineering, GMU, GPA 3.87 | ✅ (degree) |

**Gaps and mitigations:**

1. **Amazon Connect / contact center** (preferred) — Frame Entrata as "enterprise SaaS for housing operations at 100K+ MAU scale" — same domain motion, different vertical. Navigable.
2. **Amazon Bedrock** (preferred) — Familiarize before screen (AWS free tier, 2 hours). Lead with existing AWS (S3/EC2/RDS/Glue) + LLM API experience (OpenAI, Anthropic, Groq, Ollama).
3. **MCP server deployment** (basic req — "familiarity") — AgentProbe tool-calling layer is architecturally equivalent. State: "familiar with MCP protocol design; AgentProbe implements the same multi-provider tool routing pattern."
4. **Serverless patterns** — Real gap. Cite Docker microservices migration at Entrata (50% scalability improvement). Position as "AWS production experience; serverless is an extension of same infra patterns."
5. **SA customer-facing experience** — Entrata cross-functional delivery (compliance, ops, product, 120+ sprints); GMU TA (600+ students). Not formal SA, but the motion matches.

---

## C) Level and Strategy

**Detected level:** Senior = Amazon L6
**Parimala's natural SA level:** L5–L6 (engineering depth = L6; SA track record = L5)

**Sell senior plan:**
- Lead with production scale (1M+ records, 100K+ MAU, 120+ sprints) — demonstrates enterprise-grade execution
- AgentProbe = architectural judgment on record (system design + validation + CI/CD gate)
- LLM eval expertise = differentiator in SA interviews — most SA candidates configure; few can evaluate and harden
- Frame GMU Research Associate as: "applied statistical rigor to ambiguous problems at scale (R²=0.977, 190+ countries)"

**If downleveled to L5:**
- Accept if base ≥ $140K (L5 Amazon SA = $120–170K per Levels.fyi)
- Negotiate 6-month review with L6 promotion criteria tied to customer adoption metrics

---

## D) Comp and Demand

| Source | Range | Notes |
|--------|-------|-------|
| JD (Chicago base) | $153,600–$207,800 | Salary listed; RSUs + sign-on additional |
| Glassdoor (Senior AWS SA) | $176K–$216K base | 25th–75th percentile |
| Levels.fyi (Amazon SA median) | $279K total comp | L6 range with RSUs + bonus |
| Demand | High | AI SA with MCP/agentic expertise is emerging scarcity |

**Comp score: 5.0** — $153K low end exceeds Parimala's $140K top target. Total comp with RSUs estimated $200–280K.

**H-1B:** Amazon is the #1 H-1B sponsor in the US — 12,391 approvals FY2025. Files under "Amazon Web Services, Inc." This is the best possible H-1B outcome in the market.

---

## E) Customization Plan

| # | Section | Current | Proposed change | Why |
|---|---------|---------|-----------------|-----|
| 1 | Summary | "ML Engineer with 8+ years..." | Lead with "enterprise AI deployment at scale" + agentic systems + customer-facing framing | SA audience reads summary first |
| 2 | Skills – Cloud | AWS (S3, EC2, RDS, Glue) | Add "Amazon Bedrock (familiarizing)", "AWS Lambda / API Gateway / Step Functions", "MCP protocol" | Keyword gap vs JD basic requirements |
| 3 | AgentProbe | "multi-provider routing" | Add: "MCP-compatible tool routing layer; agent-to-agent state handoffs" | Maps to MCP/A2A language in JD |
| 4 | Entrata | Production modules, compliance | Add: "technical SME bridging engineering, compliance, and operations stakeholders across 100K+ unit portfolios" | Signals SA-style cross-functional engagement |
| 5 | LeaseI | "agentic LangGraph RAG pipeline" | Reframe: "deployed agentic RAG compliance pipeline for enterprise housing workflows — deterministic rules engine + LLM-as-judge validation; production-ready with audit trail" | Maps to "validate pre-production systems" |

---

## F) Interview Plan

| # | JD Requirement | Story | S | T | A | R | Reflection |
|---|---|---|---|---|---|---|---|
| 1 | Technical discovery sessions | Entrata compliance module scoping | Competing HUD/LIHTC requirements across stakeholders | Map 20+ compliance needs into coherent spec | Cross-functional sessions; data flow + state diagrams | 20+ modules shipped, zero compliance violations | Surface ambiguity early — undisclosed assumption costs 3x to fix post-deploy |
| 2 | Design agentic AI solutions | AgentProbe 3-agent architecture | Testing multi-agent LLM systems with no hardcoded logic | General-purpose 3-agent system with dynamic routing | Orchestrator → RAG Tracer → Auto Fix; 15-endpoint FastAPI | 100% local, zero cost; CI/CD gate on every commit | Routing logic should be data-driven, not conditional chains |
| 3 | Data readiness assessments | 1.6M HUD income limits import | Client data across 5 years, varying schemas | Assess, normalize, import reliably | Generic SQL import + validation rules; family-size/income threshold automation | Zero integrity issues post-launch; process adopted for all future import cycles | Readiness checklist written before import saved 2 weeks of debugging |
| 4 | RAG over domain documents | LeaseI lease compliance RAG | 1,240 lease PDFs, 5 US states, federal standards | Production RAG with citations and auditability | LangGraph + deterministic rules + LLM-as-judge with pass@k harness | 93.6% precision, 87.9% F1; pass@1 81.7% | Deterministic rules for hard constraints + LLM for soft interpretation = best of both |
| 5 | Multi-provider LLM routing | AgentProbe LLM Router | Different tasks had different latency/quality tradeoffs | Dynamic routing to best provider per task | Provider abstraction (Anthropic, OpenAI, Groq, Ollama); fallback logic | 40% faster runs; near-zero cost via Ollama for low-stakes tasks | Abstract routing contract early — swapping providers is cheap when designed for it |
| 6 | Secure cloud data access | Entrata PHI migration | 100K+ resident SSNs + phone numbers to AWS S3 | 100% PHI compliance, zero incidents | Libsodium encryption across DB; updated 50%+ of codebase for all insert/retrieve paths | 100% PHI compliance; zero rollback; zero security incidents | Encryption at data layer (not just transport) is non-negotiable for regulated data |

**Case study to present:** AgentProbe — frame as "I built an SA tool for AI systems: deploy agentic agents, then use AgentProbe to validate pre-production." Directly maps to "validate pre-production systems" in JD.

**Red-flag answers:**
- *"No Amazon Connect experience"* → "I built enterprise SaaS for housing operations for 8 years — complex customer workflows, compliance constraints, 100K+ MAU. Domain is new; pattern is the same. LeaseI proves I ramp fast: built a production housing compliance RAG with zero prior LegalTech background."
- *"No SA experience"* → "8 years at Entrata as technical SME bridging engineering, compliance, ops, and product — designing solutions with stakeholders before building them, supporting post-deploy. SA motion is familiar; the title is new."
- *"AWS layoffs 2026"* → Ask recruiter: "Is this net-new headcount or a backfill?"

---

## G) Posting Legitimacy

**Assessment: Proceed with Caution** *(recruiter outreach is a strong overriding positive)*

| Signal | Finding | Weight |
|--------|---------|--------|
| Active apply button | Yes — active with hard July 17 deadline | Positive |
| Recruiter direct outreach | Prarthana Kakkattukoiloth YogeshKumar contacted user directly | Strongly Positive |
| Posting freshness | Hard July 17 deadline implies current, active hiring | Positive |
| JD specificity | Named: Amazon Connect, Bedrock, MCP, A2A, Lambda, Step Functions — not boilerplate | Positive |
| Amazon 2026 layoffs | 16,000+ cuts; AWS professional services specifically mentioned | Concerning |
| AWS AI hiring | Amazon continues to invest and hire in AI/cloud | Positive |
| Scan history | No prior Amazon Connect SA posting seen | Neutral |
| Role type | Senior AI SA is hard to fill — longer open windows are normal | Neutral |

**Context:** Layoff overlap with "AWS professional services" is the only concern. This role sits in the Specialist org for Amazon Connect AI — a strategic growth product, not classic managed services. Ghost postings don't have recruiters calling candidates. **One question clears this:** "Is this net-new headcount or a backfill?"

---

## Keywords extracted

Amazon Connect, Amazon Bedrock, MCP server, Model Context Protocol, A2A protocol, agentic AI, LLM, RAG, retrieval-augmented generation, prompt engineering, AWS Lambda, API Gateway, Step Functions, serverless, solutions architect, technical discovery, data readiness, CI/CD, contact center AI, multi-agent, LangGraph, enterprise AI, cloud architecture

---

## Machine Summary

```yaml
company: Amazon (AWS)
role: Senior Applied AI Solutions Architect - Amazon Connect
date: 2026-07-14
score: 3.8
archetype: AI Solutions Architect + AI Forward Deployed
location: Herndon VA / Arlington VA / Seattle / NYC / Atlanta / Chicago / Denver / SF / Mountain View
remote: false
travel: 25-40%
comp_base_low: 153600
comp_base_high: 207800
comp_total_est: 250000
h1b: confirmed (#1 sponsor, 12391 approvals FY2025)
deadline: 2026-07-17
legitimacy: Proceed with Caution
recruiter_contact: Prarthana Kakkattukoiloth YogeshKumar
decision: Below 4.5 threshold but recruiter outreach + deadline + H-1B + local VA location warrant applying
```
