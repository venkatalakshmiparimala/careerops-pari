# Evaluation: Amazon — Partner Solution Architect, AWS SAIL

**Date:** 2026-08-10
**URL:** https://www.amazon.jobs/en/jobs/10497780/partner-solution-architect-aws-sail
**Archetype:** Agentic/Automation + AI Solutions Architect (hybrid)
**Score:** 4.3/5
**Legitimacy:** High Confidence
**PDF:** ❌

---

## A) Role Summary

| Dimension | Details |
|-----------|---------|
| **Archetype** | Agentic/Automation + AI Solutions Architect |
| **Team** | AWS SAIL (Streamlined Automation & Innovation Launchpad) — within AWS Specialist & Partner Org (ASP) |
| **Domain** | Multi-agent AI systems, partner enablement, AWS Bedrock/AgentCore |
| **Function** | Co-build production AI agents + partner-facing technical delivery |
| **Seniority** | Mid-Senior (Amazon L5–L6) |
| **Work model** | Hybrid — Austin TX, Seattle WA, **Arlington VA**, New York NY |
| **Comp** | $131,300–$177,600 base (non-NY); $144,500–$195,400 (NY) + RSUs + signing |
| **Sponsorship** | YES — Amazon is a top-5 H-1B sponsor |
| **TL;DR** | Write production AI agents on Bedrock/AgentCore to automate partner workflows AND work with partners on their own AI use cases — technically serious builder role at AWS, 10 min from home in Arlington VA. |

---

## B) Match with CV

| JD Requirement | CV Evidence | Match |
|----------------|-------------|-------|
| 2+ yrs application/infrastructure design | 8+ years shipping 20+ full-stack modules at Entrata (PropTech, 100K+ MAU) | ✅ Exceeds |
| 4+ yrs technology domain (software, cloud, systems) | 8 years Python/PHP/JS/PostgreSQL production engineering + AWS S3/EC2/RDS/Glue | ✅ Exceeds |
| 4+ yrs IT development or consulting | Entrata Senior SWE Sep 2018–Aug 2024 + Trainee/Associate from Jan 2017 | ✅ Exceeds |
| Multi-agent orchestration | AgentProbe: 3-agent LangGraph (Orchestrator, RAG Tracer, Auto Fix) + LeaseI: 8-agent LangGraph with real conditional edges and HITL escalation | ✅ Direct |
| Build production code + run evaluation passes | AgentProbe: CI-integrated 5-metric LLM-as-judge eval engine blocking failing runs pre-production | ✅ Direct |
| Prompt engineering + RAG | AgentProbe ChromaDB RAG pipeline; LeaseI TF-IDF hand-rolled retrieval with section-aware chunking; Magizhs FAA compliance RAG layer with cited sources | ✅ Direct |
| Deliver workshops on agentic AI | GMU Teaching Assistant: 600+ students across MIS 303; Python, database design, applied ML | ✅ Strong adjacent |
| AWS development experience (preferred) | AWS S3 migration at Entrata (100% PHI compliance, zero incidents); EC2, RDS, Glue | ✅ Partial (no Bedrock) |
| Cloud migration/transformation (preferred) | Client document migration to AWS S3; microservices revamp; service-based architecture conversion | ✅ |

### Gaps

| Gap | Blocker? | Mitigation |
|-----|----------|------------|
| **AWS Bedrock / AgentCore** — not in CV | Soft — preferred, not required | Architecture patterns from LangGraph/OpenAI/Anthropic API transfer directly. Add a Bedrock demo to AgentProbe before applying (see Block E). |
| **MCP servers** — not explicit in CV | Soft | MCP is ~1 year old. LangGraph tool-calling patterns transfer. Study MCP SDK docs; mention understanding in cover letter. |
| **Partner ecosystem experience** | Soft | Cross-functional delivery at Entrata with enterprise clients + 600+ students taught = strong adjacent; not direct partner management. |
| **AWS Certification** | Not required | Not in JD. Low risk. |

---

## C) Level and Strategy

**Level detected:** L5 (SDE II equiv.) or L6 (Senior) — comp range and 4-yr minimum suggest L5 floor. "Partner SA" without Senior/Principal prefix = open-leveling window.

**Sell your level:**
- Don't say "I've been building agentic systems." Say: "AgentProbe has a CI-integrated eval pipeline that blocks failing agent runs before production — I built that because I've seen what happens when evals are an afterthought."
- On Bedrock gap: "I know the patterns cold — LangGraph, multi-agent state machines, HITL escalation, tool routing. Bedrock's agent model maps directly to what I've built. Give me a sprint and I'll have something running."
- On workshops: Lead with the 600-student TA role — teaching AI concepts at scale is exactly what "deliver workshops on agentic AI architecture" means.

**If downleveled to L4:**
- Acceptable if comp is $120K+ base — L4 SA at Amazon still clears target.
- Negotiate 6-month performance review with clear L5 promotion criteria.
- Frame: "I'd rather start here and demonstrate impact than start anywhere else."

---

## D) Comp and Demand

| Metric | Value | Source |
|--------|-------|--------|
| Listed base (non-NY) | $131,300–$177,600 | JD |
| Listed base (NY) | $144,500–$195,400 | JD |
| Estimated TC at L5 (Levels.fyi) | $200K–$260K | RSUs + signing typical |
| Estimated TC at L6 (Levels.fyi) | $280K–$350K | Senior SA range |
| Parimala's target | $80K–$140K base | _profile.md |
| Score vs target | 5/5 | Base alone exceeds target ceiling |

Amazon's AWS SA roles are among the most competitive-paying SA tracks in cloud. Total comp will significantly exceed the base range through RSUs (typically 4-year vest with 5% year-1 / 15% year-2 cliff structure) and a signing bonus (often $15K–$40K at L5).

Demand trend: AWS SAIL is a new internal AI automation team — this is not a legacy hire. Active investment in Bedrock/AgentCore partner ecosystem acceleration. High confidence this is a live headcount.

---

## E) Customization Plan

| # | Section | Current | Proposed change | Why |
|---|---------|---------|-----------------|-----|
| 1 | **Summary** | "Built AgentProbe — 3-agent LangGraph..." | Add: "multi-agent architectures on AWS and open-source frameworks (LangGraph, Bedrock-compatible patterns)" | Mirrors JD language directly |
| 2 | **AgentProbe bullets** | Eval engine description is accurate | Add explicit phrase: "ran automated evaluation passes validating agent output quality across all commits" | JD says "run evaluation passes to validate quality" verbatim |
| 3 | **LeaseI bullets** | 8-agent HITL description present | Lead with: "Designed multi-agent orchestration (8-agent LangGraph StateGraph, conditional routing, HITL escalation) for enterprise compliance workflows" | Maps directly to "design multi-agent orchestration" |
| 4 | **TA role** | "Mentored 600+ students across MIS 303" | Add: "Delivered technical workshops on AI applications, Python automation, and database design to 600+ students" | Maps to "deliver workshops on agentic AI architecture" |
| 5 | **Skills section** | Lists "AWS (S3, EC2, RDS, Glue)" | Add: "AWS Bedrock (evaluating), AgentCore, MCP" — flag as in-progress if honest | Bedrock is in every JD requirement; even "learning" signals initiative |

**LinkedIn:** Mirror the same 5 changes in Featured section and About. Add "AWS Partner AI" to headline for this application window.

---

## F) Interview Plan

| # | JD Requirement | Story | S | T | A | R | Reflection |
|---|---------------|-------|---|---|---|---|------------|
| 1 | Design multi-agent architectures | **AgentProbe 3-agent LangGraph runtime** | Needed a real multi-agent eval system, not a chatbot wrapper | Ship 3-agent runtime with inter-agent state handoffs | Orchestrator → RAG Tracer → Auto Fix via LangGraph; multi-provider LLM routing; 15-endpoint FastAPI backend | Live GitHub repo, CI blocks failing agent runs pre-production | Agents fail in non-obvious ways — observability must be designed first, not bolted on |
| 2 | Build AI agents automating workflows | **LeaseI 8-agent support investigation pipeline** | Enterprise support tickets required 8 investigation paths: triage, retrieval, config, historical, structured data, reasoning, validation, escalation | Build a pipeline that produces ranked, evidence-backed root-cause hypotheses without AI making final regulated calls | 8-agent LangGraph StateGraph with real conditional edges; HITL escalation when confidence too low; deterministic rules handle eligibility decisions | End-to-end validated on real misconfiguration root-cause scenario; 93.6% precision on 1,240 lease PDFs | LLM reasons, humans decide — this boundary has to be enforced in code, not trusted to prompting |
| 3 | Improve agent accuracy via RAG | **AgentProbe ChromaDB RAG + LeaseI TF-IDF retrieval** | RAG quality was the primary driver of agent accuracy variance across test runs | Build retrieval that surfaces the right context for each query type | ChromaDB pipeline for AgentProbe; hand-rolled TF-IDF with section-aware chunking and hybrid reranking path for LeaseI | 100% citation correctness on Phase 1 eval set; per-run retrieval quality visible in React dashboard | Retrieval and generation are separate failure modes — you need separate metrics for each |
| 4 | Run evaluation passes / validate quality | **AgentProbe CI-integrated 5-metric eval engine** | Production LLM outputs vary unpredictably — needed automatic quality gates that don't require manual QA | Integrate evals into CI so every commit is scored and regressions block merge | LLM-as-judge with 5 metrics (factual accuracy, hallucination, retrieval, completeness, compliance); GitHub Actions pipeline; regression drift dashboard | Zero manual QA per commit; CI blocks failing runs automatically | The judge prompt must itself be tested — meta-evaluation is a real engineering discipline |
| 5 | Deliver workshops on agentic AI | **GMU Teaching Assistant: 600+ students** | MIS 303 covered Python, databases, and applied analytics — students needed practical AI application framing | Translate abstract CS concepts into hands-on workshops with no ramp-up time for students | Weekly office hours, lab guidance, supplementary exercises, one-on-one debugging, rubric-aligned grading | 600+ students mentored across two subject areas over one academic year | Technical depth only matters if you can communicate it — workshop design is its own skill |
| 6 | Own full partner engagement lifecycle | **Entrata enterprise client delivery** | 100K+ MAU property management platform; every module shipped touched live client workflows | Deliver 20+ production modules end-to-end across 120+ Agile sprints without breaking production | Led sprint planning, story estimation, cross-functional coordination with compliance/operations/product | 99.5% uptime across 6+ months; 40% deployment time reduction; 0 compliance violations | Enterprise delivery discipline — scope, communicate, ship, stabilize. No heroics, just systems. |

**Case study to present:** AgentProbe — show the GitHub repo live. Walk: architecture diagram → agent state machine → eval pipeline → CI dashboard. Say "I built this because the problem was real, not because it's impressive." Takes 8–10 minutes to walk well.

**Red-flag questions:**

- *"Have you worked with AWS Bedrock?"* → "Not with Bedrock specifically yet — I've built production agentic systems on the OpenAI and Anthropic APIs and understand the multi-agent patterns cold. Bedrock's agent model maps directly to what I've built in LangGraph. I've been studying the AgentCore docs. I can be productive in a sprint."
- *"This role is partner-facing — do you have partner management experience?"* → "At Entrata I shipped production modules that directly touched 100K+ MAU enterprise clients — every sprint decision had real client impact. And as a TA I translated technical concepts for 600+ students with zero context. I work well with technical and non-technical audiences."
- *"What's your Bedrock demo?"* → If you've built one before the interview: show it. If not, be honest: "I haven't yet — but I can build one this week. Should I?"

---

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|--------|---------|--------|
| Source domain | Official amazon.jobs URL with job ID 10497780 | Positive |
| Team specificity | Named team (AWS SAIL), specific org (ASP) | Positive |
| JD specificity | Named tools: Bedrock, AgentCore, MCP servers — not generic boilerplate | Positive |
| Location specificity | 4 specific cities with salary ranges per market | Positive |
| Comp disclosed | $131K–$177K (non-NY) explicitly listed | Positive |
| Amazon AI investment | AWS is actively building Bedrock/AgentCore ecosystem; SAIL is a new team — not a legacy backfill | Positive |
| Prior Amazon evaluations | Reports 144 and 193 were Amazon Connect SA roles — different team, different function | Neutral |
| Apply button | WebFetch confirms posting is live and active | Positive |

No ghost job indicators. This is a real, active opening on a new team.

---

## Keywords Extracted

multi-agent orchestration, AWS Bedrock, AgentCore, MCP servers, partner solution architect, agentic AI, production code, RAG, prompt engineering, retrieval-augmented generation, evaluation passes, agent accuracy, partner workflows, technical validations, competency assessments, AWS Specialist, agentic architecture, deployment patterns, co-build, partner engagement, AI use cases

---

## Machine Summary

```yaml
report: 196
company: Amazon
role: Partner Solution Architect, AWS SAIL
score: 4.3
archetype: Agentic/Automation + AI Solutions Architect
location: Arlington VA / Austin TX / Seattle WA / NYC
comp_base: "$131,300–$177,600 (non-NY)"
sponsorship: confirmed (top-5 H-1B sponsor)
legitimacy: High Confidence
recommend: apply
threshold_used: "4.0+ (FDE-adjacent)"
key_gap: AWS Bedrock / AgentCore — not in CV
key_strength: 8-agent LangGraph HITL (LeaseI) + CI-integrated eval engine (AgentProbe) + Arlington VA = zero relocation
action_before_apply: Add Bedrock demo to GitHub before submitting
```
