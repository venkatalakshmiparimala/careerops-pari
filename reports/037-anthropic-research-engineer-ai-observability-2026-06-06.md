# Evaluation: Anthropic — Research Engineer, AI Observability

**Date:** 2026-06-06
**URL:** https://job-boards.greenhouse.io/anthropic/jobs/5125083008
**Archetype:** AI Platform / LLMOps
**Score:** 4.3/5
**Legitimacy:** High Confidence
**PDF:** pending

---

## A) Role Summary

| Field | Detail |
|-------|--------|
| Archetype | AI Platform / LLMOps |
| Domain | AI observability, monitoring systems, LLM evaluation, agentic integrations, unstructured data at scale |
| Function | Build |
| Seniority | Senior (5+ years required; 8+ matched) |
| Remote | Hybrid — San Francisco, CA (min 25% in-office) |
| Comp | $320,000–$405,000 base |
| TL;DR | Build the AI-based monitoring and observability layer Anthropic uses to maintain human oversight over its own models — using Claude to analyze massive datasets, surface unexpected patterns, and develop agentic integrations that investigate findings autonomously. |

---

## B) Match with CV

| JD Requirement | CV Match | Strength |
|----------------|----------|----------|
| 5+ years SWE with ML systems exposure | 8+ years at Entrata + AgentProbe + MS | ✅ Exceeds |
| LLM application development | AgentProbe: LangChain/LangGraph, LLM Router, FastAPI backend | ✅ Direct proof |
| LLM evaluation familiarity | AgentProbe 5-metric eval engine with LLM-powered judges | ✅ Direct proof |
| AI observability / monitoring systems | AgentProbe: RAG Tracer (trace enrichment), React dashboard, per-query visibility | ✅ Direct proof |
| Agentic integrations | AgentProbe: 3 LangGraph agents (Orchestrator, RAG Tracer, Auto Fix) | ✅ Direct proof |
| Building tools others use (UX, reliability, docs) | AgentProbe: open-source, public GitHub, documented API | ✅ Strong signal |
| Large-scale data processing frameworks | AWS Glue + S3 pipelines (1M+ records at Entrata), ChromaDB vector store | ✅ Strong |
| Productionizing internal tools | 15-endpoint FastAPI backend, 20+ production modules at Entrata | ✅ Strong |
| Developer-facing platforms | AgentProbe = developer tool; FastAPI REST API with full docs | ✅ Strong |
| Monitoring/observability background | AgentProbe dashboard: per-run metrics, trace visualization, eval score tracking | ✅ Adjacent proof |
| Comfort with ambiguity in small teams | Solo-built AgentProbe; Entrata cross-functional delivery | ✅ Strong |
| PhD / deep research background | No PhD; MS GPA 3.87 | ⚠️ Soft (Bachelor's accepted) |

**Gaps and mitigations:**
- **Research depth** — Title says "Research Engineer" but JD is engineering-dominant (implement, build, extend, develop). No PhD required. Mitigate by emphasizing engineering execution alongside applied research mindset.
- **Unstructured text at scale** — Entrata data pipelines (1M+ records) + ChromaDB (vector embeddings over unstructured text) are direct analogs. Mitigate with specific framing.
- **SF relocation** — Hybrid (25% minimum = ~1 week/month). More manageable than full onsite; profile says open to relocation for strong opportunities.

---

## C) Level and Strategy

**Level detected:** Senior IC (5+ years required). Parimala at 8+ years is a strong fit.

**Sell plan:**
- Lead with the precise match: *"I built AgentProbe because I needed a system to monitor and observe multi-agent AI pipelines — the same problem this role owns at Anthropic's scale."*
- The "using Claude itself to make sense of data" framing in the JD is exactly AgentProbe's LLM-as-judge pattern — LLMs evaluating LLM outputs. Name it explicitly.
- Frame Auto Fix agent as the "agentic integration that autonomously investigates and acts on findings" the JD describes
- Anthropic is safety-first — lead with the human oversight angle: AgentProbe's eval engine was designed to keep humans informed about AI quality before deployment

**If they downlevel:** Accept if base ≥ $250K. At $320K floor this is a career-defining comp step.

---

## D) Comp and Demand

| Source | Range | Notes |
|--------|-------|-------|
| Job posting | $320K–$405K base | Listed directly |
| Market (Levels.fyi, 2026) | $280K–$450K+ total comp | Senior RE at AI safety lab |
| Anthropic standing | Top-tier AI safety lab | Meaningful equity + mission |

**Assessment:** $320K–$405K base is 129–189% above Parimala's $100K–$140K target. This is the highest base of all 5+ jobs processed so far. Anthropic is a confirmed top H-1B sponsor with excellent approval rates.

**H-1B:** Top-tier sponsor — Anthropic files hundreds of LCAs annually, high approval rate.

---

## E) Customization Plan

| # | Section | Current | Proposed change | Why |
|---|---------|---------|-----------------|-----|
| 1 | Summary | Generic AI builder | Lead with: *"Research engineer specializing in AI observability and LLM evaluation — built AgentProbe, an open-source monitoring toolkit with trace enrichment, LLM-powered judges, and agentic investigation pipelines"* | Mirrors JD language exactly |
| 2 | AgentProbe | General description | Emphasize: monitoring + observability angle, trace enrichment, human oversight framing, LLM-as-judge pattern | JD: "maintain meaningful human oversight", "surface unexpected patterns" |
| 3 | Auto Fix agent | Prompt iteration | Reframe as: *"agentic integration that autonomously investigates eval failures and acts on findings"* | JD exact language |
| 4 | Entrata data pipelines | AWS S3 migration | Reframe: *"built large-scale data processing frameworks processing 1M+ records"* | JD: "processing large volumes of unstructured text data" |
| 5 | Summary framing | Mission-neutral | Add safety angle: *"designed to keep humans informed about AI quality — preventing regressions before they reach users"* | Anthropic is safety-first; align to mission |

---

## F) Interview Plan

| # | JD Requirement | Story | S | T | A | R | Reflection |
|---|----------------|-------|---|---|---|---|------------|
| 1 | AI observability + monitoring | AgentProbe dashboard + RAG Tracer | No visibility into why agent runs failed — silent failures | Build trace-level observability for multi-agent RAG | RAG Tracer agent enriches traces per run; React dashboard visualizes per-query: retrieval score, generation score, eval score | Full trace visibility from query → retrieval → generation → eval; every run inspectable | Async trace streaming > sync — blocking on trace collection kills throughput |
| 2 | LLM evaluation + human oversight | AgentProbe 5-metric eval engine | No systematic way to know if AI output quality degraded between deployments | Design eval system that keeps humans informed before every release | LLM-powered judges (5 metrics) score every run; dashboard surfaces unexpected patterns; Auto Fix triggers on threshold breach | Human stays in control: see every failure, understand root cause, approve fixes | Calibrated confidence intervals on judge scores matter more than raw metric values |
| 3 | Agentic integrations that investigate findings | AgentProbe Auto Fix agent | Eval failures required manual diagnosis and prompt rewriting | Build agent that autonomously investigates and acts on findings | Auto Fix reads eval scores, identifies failure pattern, selects fix strategy, rewrites prompt, re-runs eval | Closed loop: failure detected → diagnosed → fixed → re-evaluated without human intervention per cycle | Human-in-the-loop checkpoints at confidence thresholds — full autonomy has failure modes too |
| 4 | Large-scale data processing frameworks | Entrata AWS pipelines | All client data in manual, insecure, fragmented processes | Build automated data processing at scale | AWS S3 + Glue + EC2 pipelines; Libsodium encryption; automated quality checks at each stage | 1M+ records, 100% PHI compliance, zero security incidents, 80% workload eliminated | Schema validation at ingestion catches 80% of downstream data quality issues |
| 5 | Building tools others use | AgentProbe open source | Needed a reusable eval framework others could run locally | Ship a developer tool, not just personal infrastructure | Public GitHub, documented 15-endpoint API, README with setup, React dashboard, multi-provider support | Open-source tool used beyond my own projects; demonstrates UX and reliability discipline | Documentation is a first-class feature — undocumented tools have zero adoption |

**Case study to present:** AgentProbe observability loop — show how RAG Tracer enriches traces, how the eval dashboard surfaces patterns across runs, and how Auto Fix closes the loop. Frame it as: *"I built a mini version of what this team owns — AI using AI to monitor AI."*

**Red flag questions:**
- *"You don't have a research background"* → *"The JD is engineering-dominant — implement, build, extend, develop. My background is exactly that: I built an observability system that surfaces unexpected patterns in LLM outputs. The research mindset I bring is: measure first, then fix. That's AgentProbe."*
- *"Why Anthropic specifically?"* → *"The mission of maintaining human oversight over AI resonates directly with what I built. AgentProbe's eval engine was designed to keep humans informed before AI systems degrade. Scaling that to Anthropic's training and deployment context is exactly the problem I want to work on."*

---

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|--------|---------|--------|
| Posting freshness | Active on Greenhouse | Positive |
| Apply button | Active | Positive |
| JD specificity | Named responsibilities (agentic integrations, unstructured data, strategic direction), specific context (training + deployment monitoring) | Positive |
| Salary listed | Yes ($320K–$405K) — rare and strong signal | Positive |
| Company health | Anthropic is the top AI safety lab; no layoffs/freeze signals | Positive |
| H-1B | Top-tier sponsor, hundreds of LCAs annually | Positive |
| Reposting | Not seen in scan-history.tsv | Positive |

---

## Keywords Extracted

ai observability, monitoring systems, llm evaluation, agentic integrations, unstructured data, human oversight, research engineer, claude api, llm-as-judge, trace enrichment, data processing frameworks, developer platform, internal tools, python, ml systems, anthropic, safety, cross-functional

---

## Machine Summary

```yaml
report_num: 037
company: Anthropic
role: Research Engineer, AI Observability
date: 2026-06-06
score: 4.3
archetype: AI Platform / LLMOps
legitimacy: High Confidence
location: San Francisco, CA — hybrid (min 25% in-office)
comp_range: "$320K–$405K base"
visa_risk: low (Anthropic = top H-1B sponsor)
key_gaps:
  - No PhD (Bachelor's accepted — soft gap)
  - SF relocation (hybrid min 25% — manageable)
key_strengths:
  - AgentProbe = direct proof of AI observability, trace enrichment, LLM-as-judge
  - Auto Fix agent = agentic integration that investigates and acts on findings
  - Open-source tool with UX + reliability discipline demonstrated
  - Mission alignment: human oversight of AI = AgentProbe's design goal
  - Exceptional comp ($320-405K base)
location_risk: medium — hybrid SF, relocation from Virginia but only 25% in-office
recommend: strong apply — domain match is near-perfect; highest comp of all roles processed; Anthropic is top H-1B sponsor
```
