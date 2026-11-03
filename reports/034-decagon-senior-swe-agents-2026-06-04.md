# Evaluation: Decagon — Senior Software Engineer, Agents

**Date:** 2026-06-04
**URL:** https://jobs.ashbyhq.com/decagon/90c40e13-345e-4855-944e-c8f6b462a78e
**Archetype:** Agentic / Automation
**Score:** 4.0/5
**Legitimacy:** High Confidence
**PDF:** pending

---

## A) Role Summary

| Field | Detail |
|-------|--------|
| Archetype | Agentic / Automation |
| Domain | AI agent deployment, enterprise-scale LLM integration, multi-channel (voice, chat, SMS, email) |
| Function | Build |
| Seniority | Senior (5+ years required; 8+ matched) |
| Remote | Full onsite — New York City |
| Comp | $250K–$330K base + equity |
| TL;DR | Design and ship AI agents for enterprise customers at Decagon — a conversational AI platform serving Chime, Block, Oura Health, and Avis. Own agent deployment end-to-end: from implementation through continuous evaluation and iteration. |

---

## B) Match with CV

| JD Requirement | CV Match | Strength |
|----------------|----------|----------|
| 5+ years SWE experience | 8+ years at Entrata (2017–2024) | ✅ Exceeds |
| Python proficiency | Entrata (Python backend), AgentProbe (Python/FastAPI/LangGraph), AI on FHIR (Flask) | ✅ Strong |
| TypeScript proficiency | Listed in CV technical skills, used in front-end components at Entrata | ✅ Present |
| Async programming | FastAPI (async-native), LangGraph (async agent orchestration) | ✅ Strong |
| AI agent building | AgentProbe: 3 LangGraph agents (Orchestrator, RAG Tracer, Auto Fix), multi-step reasoning, tool calls | ✅ Direct proof |
| Model evaluation & experimentation | AgentProbe 5-metric eval engine, LLM-powered judges — exact pattern | ✅ Direct proof |
| Strong debugging skills | 100+ high-priority bugs resolved at Entrata; 5+ debugging tools built; TDD/BDD | ✅ Strong |
| Cross-customer trends / enterprise delivery | 120+ Agile sprints, 100K+ MAU, cross-functional delivery at Entrata | ✅ Adjacent |
| Multi-modal model development | Not in CV | ⚠️ Soft gap (preferred, not required) |
| Voice AI / voice channels | Not in CV | ⚠️ Gap |
| Enterprise customer-facing deployment | AgentProbe is project-scale; Entrata was internal, not customer-facing SaaS | ⚠️ Gap |

**Gaps and mitigations:**
- **Multi-modal / Voice** — Preferred, not required. Decagon serves voice, chat, SMS, email. Gap is real for voice specifically; LLM evaluation across modalities is adjacent to AgentProbe's eval engine.
- **Enterprise customer-facing deployment** — Soft: AgentProbe is a project, not production SaaS. Mitigate by framing Entrata's 100K+ MAU and 1M+ records as production enterprise scale; AgentProbe's Azure deployment as customer-facing API.
- **Company-specific agent platform** — Decagon has proprietary agent platform; ramp-up expected. Mitigate: LangGraph expertise is the closest existing analog.

---

## C) Level and Strategy

**Level detected:** Senior (5+ years minimum). Parimala at 8+ years is a strong fit.

**Sell senior plan:**
- Lead with AgentProbe as live proof of agentic system design: 3 LangGraph agents, LLM Router, multi-step reasoning, tool calls, real-time trace enrichment
- Frame the 5-metric eval engine as exactly what the JD asks for: "experimenting with and running evaluations on the latest text and voice models"
- Quote: *"I built AgentProbe to evaluate and improve multi-agent systems before deployment. The Orchestrator, RAG Tracer, and Auto Fix agents together form a continuous improvement loop — which is the same loop Decagon runs at enterprise scale."*
- Reference specific Decagon customers (Chime, Block, Oura) — these are production, mission-critical deployments. Entrata's 99.5% uptime and zero-security-incident record demonstrate the same discipline.

**If they downlevel:** Role is already senior; unlikely to downlevel given comp ($250K+). Accept if base ≥ $200K with equity.

---

## D) Comp and Demand

| Source | Range | Notes |
|--------|-------|-------|
| Job posting | $250K–$330K base + equity | Listed directly |
| Levels.fyi | $305K–$510K+ total comp | Includes equity — base + RSU |
| Glassdoor | $250K–$375K | Senior SWE, Product role listed at this range |

**Assessment:** $250K–$330K base is 79–136% above Parimala's $100K–$140K target — exceptional. Backed by a16z and Accel. Founded 2023 with 51-200 employees — early stage with meaningful equity upside.

**H-1B:** Confirmed — 9 LCAs filed FY2026, 100% approval rate. DOL classified as non-willful violator. Strong sponsor.

---

## E) Customization Plan

| # | Section | Current | Proposed change | Why |
|---|---------|---------|-----------------|-----|
| 1 | Summary | Generic SWE + AI builder | Lead with: *"Software engineer specializing in AI agent systems — built AgentProbe, a multi-agent evaluation toolkit with 3 LangGraph agents, Python/TypeScript async backend, and automated prompt iteration"* | Mirrors Decagon's exact stack |
| 2 | AgentProbe project | General description | Emphasize: multi-agent architecture, tool calls, async orchestration, LLM evaluation loop | JD keywords: agents, evaluation, experimentation |
| 3 | Entrata bullets | Scale + reliability | Reframe one bullet: cross-functional delivery, production debugging, iterative sprint delivery | JD: "continuous iteration", "debugging skills" |
| 4 | Competencies | LLM eval focus | Add: Multi-Agent Orchestration, Async Python, TypeScript, Tool Calls, Enterprise AI Deployment | Match JD language |
| 5 | Skills | Languages | Promote TypeScript higher; add "async programming" explicitly | JD explicitly lists TypeScript + async |

---

## F) Interview Plan

| # | JD Requirement | Story | S | T | A | R | Reflection |
|---|----------------|-------|---|---|---|---|------------|
| 1 | AI agent building + evaluation | AgentProbe 3-agent system | No reliable pre-deployment test for multi-agent RAG | Build an evaluation system for agentic AI pipelines | 3 LangGraph agents: Orchestrator (routes), RAG Tracer (trace enrichment), Auto Fix (prompt iteration on failure) | 5-metric eval engine, full trace visibility, automated prompt iteration | Would build async eval streaming from day one — sync is too slow at agent scale |
| 2 | Evaluating text/voice models | AgentProbe LLM-powered judges | Hard to know if eval metrics correlate with real quality | Design metrics that predict user satisfaction | 5 metrics based on where RAG systems fail most: hallucination, retrieval, completeness, compliance, correctness | Actionable metrics — Auto Fix agent triggers on score thresholds | Calibrating judge confidence intervals matters more than metric count |
| 3 | Enterprise delivery + debugging | Entrata 100+ bug resolution | 100+ high-priority bugs blocking production releases | Maintain stability across 100K+ MAU platform | Root-cause analysis, debugging tools, TDD/BDD gates, peer code reviews | 99.5% uptime; sub-10 bug count for 6+ consecutive months | Build debugging instrumentation before shipping, not after |
| 4 | Iterative agent improvement | AgentProbe Auto Fix agent | Eval scores degraded but no automated way to iterate | Close the loop: eval failure → prompt improvement | Auto Fix agent reads eval scores, selects fix strategy, rewrites prompt, re-runs eval | Automated prompt iteration without human intervention | Human-in-the-loop checkpoints are still needed at thresholds |
| 5 | Cross-customer trends | Entrata 120+ sprint delivery | Different clients had different workflows creating fragmented codebase | Identify common patterns, build reusable modules | Abstracted 20+ modules into shared components; documented patterns across 120+ sprints | Faster delivery, reduced duplication — set cross-team standards | Common abstractions only emerge after 3+ customer pain points overlap |

**Case study to present:** AgentProbe evaluation loop — walk through: query → agent orchestration → RAG retrieval → LLM generation → LLM judge scoring → 5-metric output → Auto Fix agent → re-run. Frame it as: *"This is the evaluation and iteration loop Decagon needs to run at enterprise scale."*

**Red flag questions:**
- *"You haven't deployed AI agents to enterprise customers"* → *"AgentProbe is project-scale, but the systems patterns — async orchestration, trace enrichment, eval-driven iteration — are identical. At Entrata I shipped production systems to 100K+ users across 120+ Agile sprints with 99.5% uptime. The discipline is the same."*
- *"We need voice AI experience"* → *"I don't have voice specifically, but my LLM evaluation framework is modality-agnostic — it scores any text output from any model. Voice transcriptions are text. I'd ramp into voice-specific evaluation patterns in the first sprint."*

---

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|--------|---------|--------|
| Posting freshness | Active on Ashby + Accel job board | Positive |
| Apply button | Active | Positive |
| JD specificity | Named tech (Python, TypeScript, async), specific responsibilities (cross-customer trends, LLM eval), named customers | Positive |
| Company health | Backed by a16z + Accel; 51-200 employees; active hiring across roles | Positive |
| H-1B record | 9 LCAs FY2026, 100% approval rate | Positive |
| Salary listed | Yes ($250K–$330K) | Positive |
| Reposting | Not seen in scan-history.tsv | Positive |
| Risk flag | Early-stage startup (founded 2023) — equity upside but higher startup risk | Neutral |

---

## Keywords Extracted

ai agents, agentic ai, software engineer, python, typescript, async programming, multi-agent, llm evaluation, model evaluation, voice ai, enterprise deployment, langchain, langgraph, tool calls, agent orchestration, debugging, iterative improvement, cross-functional, customer-facing, decagon

---

## Machine Summary

```yaml
report_num: 034
company: Decagon
role: Senior Software Engineer, Agents
date: 2026-06-04
score: 4.0
archetype: Agentic / Automation
legitimacy: High Confidence
location: New York City — full onsite
comp_range: "$250K–$330K base + equity"
visa_risk: low (9 LCAs FY2026, 100% approval)
key_gaps:
  - Multi-modal / voice AI (preferred, not required)
  - Enterprise customer-facing deployment (project-scale only)
key_strengths:
  - AgentProbe = 3 LangGraph agents = direct proof of agentic system design
  - Model evaluation pattern matches JD requirement exactly
  - Python + TypeScript + async = full stack match
  - 8+ years exceeds 5+ requirement
  - Exceptional comp ($250-330K base)
  - H-1B confirmed sponsor
location_risk: medium-high — full onsite NYC, relocation from Virginia required
recommend: apply — archetype match is near-perfect; NYC onsite is main hurdle but comp justifies relocation
```
