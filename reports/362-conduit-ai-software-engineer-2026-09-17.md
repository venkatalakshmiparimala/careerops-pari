# Evaluation: Conduit AI -- Software Engineer (Member of Technical Staff)

**Date:** 2026-09-17
**URL:** (pasted directly, no URL provided)
**Archetype:** Agentic / Automation + PropTech AI Engineer (housing + hospitality)
**Score:** 4.5/5
**Legitimacy:** High Confidence
**PDF:** output/cv-venkata-lakshmi-parimala-pasupuleti-conduit-2026-09-17.pdf (2 pages, 93 KB est.)
**Location:** Remote (SF on-site for interview/work day, travel compensated; "remote option if SF does not work")
**Comp:** $130,000 -- $220,000 base + 0.20%--1.20% equity

---

## A) Role Summary

| Dimension | Detail |
|-----------|--------|
| Archetype | Agentic / Automation + PropTech AI Engineer |
| Domain | Hospitality AI agents -- guest communication, internal operations, leasing, onboarding, scheduling for hotels/vacation rentals/resorts. "Starting with housing and hospitality." |
| Function | Build the agentic platform end-to-end: response pipeline, knowledge retrieval, tool orchestration, eval, observability, voice |
| Seniority | Member of Technical Staff -- flat engineering org, no hierarchy, no formal leveling. Zero hard block. |
| Location | Remote (SF for interview work day, travel compensated; remote option stated) |
| Company | Conduit AI -- YC-backed, founded 2024, 15 employees, $3.1M seed (YC, a16z Scout, YouTube co-founder Jawed Karim, Snapdocs founder Aaron) |
| TL;DR | Remote agentic AI engineer role at a 15-person YC seed startup building hospitality + housing AI agents. The JD describes LeaseI almost word for word. Comp $130K-$220K + early equity. H-1B at 15-person seed = near-zero -- this is the defining risk. |

---

## B) Match with CV

| JD Requirement | CV Match | Strength |
|----------------|----------|----------|
| Production AI systems that real users depend on | LeaseI: 93.6% precision on 1,240 test cases; AgentProbe CI eval gate; Entrata 100K+ MAU | ✅ Exceptional |
| Response generation pipeline (router, orchestrator, synthesizer, escalation) | LeaseI: 8-agent LangGraph StateGraph (Triage → Retrieval → Config → Historical → Reasoning → Validation → HITL Escalation) -- exactly this pattern | ✅ Direct, architecturally identical |
| Knowledge retrieval -- reliability under contradictory/stale docs | LeaseI: TF-IDF RAG, section-aware chunking, missing/conflicting clause detection, 100% citation correctness, stale-document handling | ✅ Direct |
| Tool orchestration -- function calling, multi-step workflows, API failures mid-workflow | LeaseI: conditional edges, multi-step tool calls, HITL escalation when confidence drops; Magizhs: FAA corpus tool calls with validation guardrails | ✅ Direct |
| Evaluation framework -- quality against real conversations, regression detection | AgentProbe: 5-metric eval engine, CI regression gate, LLM-as-judge, multi-trial sampling, 1,240+ test cases | ✅ Direct, purpose-built for exactly this |
| Observability -- trace what was retrieved, what was ignored, where confidence dropped | AgentProbe: structured observability, agent tracing, confidence scoring, result tracking across eval runs | ✅ Direct |
| Controls for non-engineers (CX teams, support leads) | LeaseI Tenant Self-Service surface: "safety boundary tested -- never auto-resolves eligibility/config/calculation for a tenant"; legible outputs for non-technical users | ✅ Present |
| Housing + hospitality domain ("leasing, onboarding, scheduling, retention") | 8yr Entrata (leasing, property management, tenant onboarding, scheduling workflows) -- exact domain | ✅ Exceptional (8yr domain depth) |
| Pragmatic about models (frontier vs small vs regex) | AgentProbe multi-provider routing (Anthropic, OpenAI, Groq); LeaseI: TF-IDF RAG (no vector DB -- deliberate choice for reliability); "sometimes the right answer is a regex" is how LeaseI was designed | ✅ Direct |
| Ships production, small team, owns outcome | Entrata: 7yr sole pipeline ownership, zero compliance violations; AgentProbe + LeaseI built solo | ✅ Strong |
| Voice (real-time, transcription, tight latency) | Not in portfolio | ⚠️ Gap (nice-to-have in JD) |
| Optional agent coding session (record yourself with an AI agent) | Claude Code is her primary daily tool -- she could record a real workflow | ✅ Unique opportunity |

**The architectural match is the closest this evaluation system has produced.** The JD's description of Conduit's platform -- "the router, orchestrator, and synthesizer that classify intent, assemble context, select tools, generate a response, and decide whether to send it or escalate" -- is a description of LeaseI's 8-agent pipeline written by someone who didn't know LeaseI existed. Same routing logic, same retrieval reliability problem, same eval discipline, same HITL design principle.

**One genuine gap:** Voice (real-time transcription, tight latency). Listed in the JD as a work area, not as a qualification. Not a blocker.

---

## C) Level and Strategy

**No hard block.** Conduit has 15 employees and a flat engineering org with no titles above "member of technical staff." There is nothing to be mismatched against. The founders are doing the first calls themselves.

**Sell plan:**
- LeaseI as the direct architectural proof: "I built a system that does exactly what you described. 8-agent LangGraph pipeline with routing, retrieval, tool orchestration, eval, and HITL. Different vertical (real estate compliance vs. hospitality), same design problems. I built AgentProbe because I needed an eval framework to trust it in production."
- Domain: "I spent 8 years at a company that runs leasing, onboarding, scheduling, and retention workflows for rental housing. Hospitality guest management is the same operation -- different context, same coordination work."
- Pragmatic model choices: "LeaseI uses hand-rolled TF-IDF RAG instead of a vector database because it's more reliable for the compliance use case. I chose that deliberately. That's the kind of tradeoff call the JD is describing."
- Optional video: Record a real Claude Code session building something small and technically interesting. This is a genuine advantage she can execute.

**The founders call (20 min):** No prep needed per the JD. Lead with LeaseI + AgentProbe, describe the eval discipline, mention the domain.

**Technical interview (45 min):** The three stated problems are LeaseI problems. Debugging a retrieval pipeline returning wrong context = exactly the contradictory/stale document problem she solved. Designing tool use for a multi-step workflow = LangGraph conditional routing she built. Why a response went sideways on a real conversation = AgentProbe trace analysis.

---

## D) Comp and Demand

| Source | Range | Notes |
|--------|-------|-------|
| Disclosed | $130,000 -- $220,000 base | Wide range; 15-person seed = senior end likely $130-$160K |
| Equity | 0.20%--1.20% | Seed stage, 15 employees; meaningful if company succeeds |
| Funding | $3.1M seed | YC + a16z Scout; lean but quality investors |
| Parimala's target | $80K--$140K | Floor ($130K) at top of target range |

**Risk note:** $3.1M seed funding a team of 15 at $130-$220K base is a significant burn. Verify the actual cash offer during the process -- they may be offering stock-heavy packages at the lower end of the range.

**Equity upside:** 0.20% at a YC company that goes on to raise Series A/B/C could be significant. "1000+ global hospitality brands across 120 countries" -- if that traction holds, the equity could matter. It's speculative but not zero.

---

## E) Customization Plan

| # | Section | Current | Change | Why |
|---|---------|---------|--------|-----|
| 1 | Summary | Generic SWE | Open with: "I built LeaseI -- an 8-agent LangGraph agentic platform for real estate compliance workflows. The architecture: routing, retrieval from a complex regulatory corpus, tool orchestration, eval against 1,240 test cases, and HITL escalation when confidence drops. That is Conduit's platform applied to housing and hospitality, and I built it because the same coordination problem exists in leasing and property management." | Direct LeaseI → Conduit bridge |
| 2 | Projects | Dealpath/PermitFlow framing | LeaseI: lead with the 8-agent pipeline description using Conduit's exact language (router, orchestrator, synthesizer, escalation); AgentProbe: eval framework that catches regressions before customers see them | Mirror the JD language |
| 3 | Entrata | SaaS framing | Reframe as: "8yr building leasing, onboarding, scheduling, and retention workflows for rental housing -- the same operations Conduit automates for hospitality" | Direct domain bridge |
| 4 | Skills | General order | Promote LangGraph, Agentic AI, RAG, Tool Orchestration, LLM Evaluation, Observability to first line | JD emphasis |
| 5 | Magizhs | Generic AI | Reframe as: "Built an agentic system that retrieves from a regulatory corpus, validates against rules, and decides whether to proceed or escalate -- same orchestration pattern as Conduit's guest workflow agents" | Reinforces agentic depth |

---

## F) Interview Plan

| # | JD Problem | Story + Answer | Key Insight |
|---|------------|----------------|-------------|
| 1 | Debug a retrieval pipeline returning wrong context | LeaseI: contradictory/stale document problem -- section-aware chunking, missing/conflicting clause detection, 100% citation correctness requirement | Retrieval reliability comes from schema, not model; the retrieval layer determines whether the generation is trustworthy |
| 2 | Design tool use for a multi-step workflow | LeaseI: 8-agent conditional routing (Triage → Retrieval → Config → Historical → Reasoning → Validation → HITL) -- design decisions on when each agent hands off vs. continues | Multi-step tool use requires designing failure modes first; what happens when the third-party API goes down mid-conversation? |
| 3 | Why a response went sideways on a real conversation | AgentProbe: trace analysis -- what was retrieved, what confidence was, why model chose what it did | Observability is what makes CX teams trust the system; without the trace, you're debugging in the dark |
| 4 | Controls for non-engineers | LeaseI Tenant Self-Service: behavior legible and adjustable by support leads without code | "Legible, testable, adjustable" -- three separate properties that require three separate design decisions |
| 5 | Founders call: what you have built | LeaseI → AgentProbe: built the product (agentic compliance AI), then built the eval framework to trust it | I don't ship a prompt change without knowing what it does across a thousand conversations -- that discipline is why AgentProbe exists |

**Optional video (do it):** Record a real Claude Code session -- design and build a small retrieval or tool-orchestration component in 5 minutes. This is a genuine differentiator. She uses Claude Code every day. Most candidates will skip this; she should submit it.

---

## G) Posting Legitimacy

**Assessment: High Confidence (with seed-stage caveats)**

| Signal | Finding | Weight |
|--------|---------|--------|
| Company identity | Conduit AI -- YC W25 (Y Combinator), 15 employees, SF, real product with 1000+ hospitality customers | Positive |
| Investor quality | YC + a16z Scout + YouTube co-founder + Snapdocs founder = strong seed signal | Positive |
| Description quality | JD is highly specific, architecturally precise, describes real engineering work -- not boilerplate | Positive |
| Traction | 1000+ global hospitality brands, 120+ countries -- extraordinary for seed stage | Positive |
| Comp transparency | $130K-$220K + 0.20%-1.20% equity explicitly disclosed | Positive |
| Seed stage risk | $3.1M raised; 15 people; could pivot or fail; standard early-stage risk | Noted |
| H-1B/OPT | **15 employees, seed stage, YC class company -- almost certainly zero H-1B infrastructure.** Highest-risk sponsorship situation in today's pipeline. | ⚠️ Critical |

---

## Recommendation: Apply -- H-1B Conversation First (Critical Gate)

**Score 4.5/5 = above threshold for agentic AI roles.** This is the highest-scoring role evaluated today and the strongest technical match in the current pipeline.

**Why this is exceptional:**
- The JD describes LeaseI. Not "similar to LeaseI" -- architecturally describes the same system. Router, orchestrator, synthesizer, escalation = LeaseI's 8-agent pipeline. Retrieval reliability under contradictory/stale docs = LeaseI's TF-IDF challenge. Eval framework catching regressions = AgentProbe. Observability trace = AgentProbe. HITL escalation = LeaseI design rule.
- Domain: "housing and hospitality, where communication is the operation -- leasing, onboarding, scheduling, retention" = 8yr Entrata.
- Remote role. No seniority hard block. Flat org.

**The single defining risk: H-1B at a 15-person seed company.** YC companies are willing to do things standard companies won't, but setting up an H-1B program from zero at a 15-person startup requires a founder who cares enough to run the process. This is a direct conversation question, not a background research item. Email or DM the founders: "I want to be direct -- I'm on STEM OPT with H-1B eligibility. Would Conduit sponsor?" Founders at YC companies respect directness. If yes, this is a top-priority application.

**Action sequence:**
1. Find founders on LinkedIn/X (Punn Kam, Cole Rubin) -- direct message, one sentence: "I'm on STEM OPT and want to be upfront about sponsorship before applying. Is this a path Conduit would pursue?"
2. If yes: apply immediately. Submit the optional agent coding video.
3. If no: note it -- Conduit would be a strong role if the visa situation changes.

---

## Keywords Extracted

`LangGraph`, `agentic AI`, `RAG`, `knowledge retrieval`, `tool orchestration`, `function calling`, `LLM evaluation`, `observability`, `HITL`, `multi-agent`, `response pipeline`, `React`, `TypeScript`, `PostgreSQL`, `Python`, `FastAPI`, `hospitality`, `leasing`, `housing`, `real estate`, `evaluation framework`, `CI/CD`, `full stack`, `production AI`

---

## Machine Summary

```yaml
report: 362
company: Conduit AI
role: Software Engineer (Member of Technical Staff)
date: 2026-09-17
score: 4.5
archetype: Agentic / Automation + PropTech AI Engineer
legitimacy: High Confidence
url: null
status: Evaluated
apply_threshold: 4.5 (agentic AI) / 4.0 (PropTech) -- exceeds both
recommendation: apply_conditional
condition: >
  H-1B/OPT sponsorship at 15-person seed company = near-zero history.
  Direct founder outreach required before applying. One message: "I'm on STEM OPT.
  Would Conduit sponsor?" YC founders respect directness.
boosts_applied:
  - LeaseI = architecturally identical to Conduit's product (direct proof point, not analog)
  - 8yr housing/leasing domain (exact domain: "housing and hospitality, leasing, onboarding, scheduling, retention")
  - AgentProbe = eval framework JD explicitly describes as a core system
  - Remote role, flat org, no title hard block
gaps:
  - Voice (real-time, transcription, tight latency) -- not in portfolio; listed as work area not qualification
  - H-1B at seed stage = highest-risk situation in pipeline
  - $3.1M seed = company risk; burn vs. comp offer to verify
strengths:
  - LeaseI 8-agent pipeline = Conduit's exact architecture description
  - AgentProbe = Conduit's eval/observability requirement
  - 8yr Entrata leasing/housing = Conduit's stated domain
  - Remote + flat org = no leveling/location blockers
  - Optional video: Claude Code session = genuine differentiator she can execute
company_size: 15 employees (YC W25)
funding: $3.1M seed (YC, a16z Scout)
comp_base: $130K-$220K + 0.20%-1.20% equity
```
