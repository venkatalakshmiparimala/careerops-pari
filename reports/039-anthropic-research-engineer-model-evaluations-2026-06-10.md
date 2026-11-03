# Evaluation: Anthropic — Research Engineer, Model Evaluations

**Date:** 2026-06-10
**URL:** https://job-boards.greenhouse.io/anthropic/jobs/5198255008
**Archetype:** AI Platform / LLMOps
**Score:** 3.8/5
**Legitimacy:** High Confidence
**PDF:** output/cv-anthropic-model-evaluations-2026-06-10.pdf

---

## A) Role Summary

| Field | Detail |
|-------|--------|
| Archetype | AI Platform / LLMOps |
| Domain | LLM evaluation, model health dashboards, distributed eval infrastructure, capability + safety evals |
| Function | Build + Research |
| Seniority | Senior IC (advanced Python + distributed systems required) |
| Remote | Remote-friendly + SF, CA + NYC, NY |
| Comp | $320,000–$485,000 base |
| TL;DR | Design and run evaluations measuring Claude's reasoning, agentic behavior, and safety properties — build the infrastructure to execute evals reliably at checkpoint scale, own dashboards tracking model health during training, and diagnose anomalous eval results fast. |

---

## B) Match with CV

| JD Requirement | CV Match | Strength |
|----------------|----------|----------|
| Advanced Python in production/research | 8+ years Python at Entrata + AgentProbe FastAPI backend | ✅ Strong |
| Distributed systems / data pipelines at scale | AWS Glue + S3 pipelines (1M+ records at Entrata) | ✅ Strong |
| LLM experience + prompting techniques | AgentProbe: multi-provider LLM routing, prompt engineering across Anthropic/OpenAI/Groq | ✅ Direct proof |
| Evaluation metrics for language models | AgentProbe 5-metric LLM-as-judge engine (correctness, hallucination, retrieval, completeness, compliance) | ✅ Direct proof |
| Observability / monitoring / experiment tracking | AgentProbe RAG Tracer: per-run trace enrichment, React dashboard, eval score tracking across runs | ✅ Direct proof |
| Data visualization + dashboard development | AgentProbe React observability dashboard with per-query metrics visualization | ✅ Direct proof |
| Statistical + experimental design | MS Data Analytics Engineering (GPA 3.87); CrashClarity: full ML lifecycle, model comparison | ✅ Strong |
| Cross-team collaboration + communication | 120+ Agile sprints at Entrata across 20+ projects; TA role at GMU | ✅ Strong |
| Genuine concern about AI implications | AgentProbe designed explicitly for human oversight before AI deployment | ✅ Strong signal |
| ML training infrastructure (checkpoint testing during training) | No direct experience with training-time infrastructure | ⚠️ Real gap |
| Large-scale dataset sourcing/curation for LLM training | No LLM training dataset curation experience | ⚠️ Soft gap |
| Diagnosing model vs infrastructure issues during training runs | No live training run support experience | ⚠️ Real gap |

**Gaps and mitigations:**
- **Training infrastructure** — Core responsibility is "distributed eval execution for reliable checkpoint testing" and "model health during training cycles." Parimala's eval experience is inference-time (deployed systems), not training-time. This is the main gap.
- **Mitigation:** Framing: eval design and infrastructure thinking transfers — the problem of "did the model regress" is identical at inference and training. Distributed pipeline experience at Entrata (1M+ records, AWS Glue) covers infrastructure credibility.
- **Dataset curation** — Preferred, not required. Skip.
- **Remote-friendly location** — Virginia is fine; the role explicitly lists remote-friendly.

---

## C) Level and Strategy

**Level detected:** Senior IC. "Advanced Python" + "distributed systems" + production systems support = mid-senior.

**Sell plan:**
- Lead with the eval depth: *"I built a 5-metric LLM-as-judge eval engine from scratch — correctness, hallucination, retrieval quality, completeness, and compliance. I know what it takes to make eval results trustworthy, not just present."*
- Dashboard + observability: AgentProbe tracks eval scores across runs — that's model health monitoring at small scale. Same pattern as training run dashboards.
- Be transparent about the training gap: *"My eval experience is inference-time. I haven't supported live training runs, but the infrastructure and diagnostic thinking is identical — and I learn production systems fast."*
- Mission alignment: the "genuine concern about societal implications" requirement is authentic for Parimala — AgentProbe's human oversight design is the proof.

**If they downlevel:** Accept if base ≥ $280K. At $320K floor this is still career-defining.

---

## D) Comp and Demand

| Source | Range | Notes |
|--------|-------|-------|
| Job posting | $320K–$485K base | Listed directly — highest of all roles processed |
| Market (Levels.fyi, 2026) | $300K–$500K+ total comp | Research Engineer at top AI safety lab |
| Anthropic standing | Top AI safety lab | Meaningful equity + mission |

**Assessment:** $320K–$485K is the highest base range seen across all 45 applications. Remote-friendly makes this accessible without relocation. Top H-1B sponsor.

**H-1B:** Anthropic sponsors visas with retained immigration counsel. Top-tier sponsor.

---

## E) Customization Plan

| # | Section | Current | Proposed change | Why |
|---|---------|---------|-----------------|-----|
| 1 | Summary | AI observability focus | Lead: *"Research engineer specializing in LLM evaluation and model health monitoring — built a 5-metric eval engine and observability dashboard that tracks model quality across runs"* | Mirrors JD's core: evaluation + dashboards + health tracking |
| 2 | AgentProbe | General | Emphasize: 5-metric eval engine design, dashboard tracking across runs, prompting experiments, eval result diagnosis | JD: "design and execute evaluations", "dashboards tracking model health", "diagnose anomalous results" |
| 3 | Entrata data pipelines | AWS S3 | Reframe as: *"distributed data processing framework at scale — 1M+ records, automated quality checks, zero-defect pipeline"* | JD: distributed systems + infrastructure at scale |
| 4 | Competencies | Observability-heavy | Add: LLM Capability Evaluation, Eval Infrastructure, Model Health Dashboards, Experimental Design | JD core pillars |
| 5 | Summary framing | Safety-neutral | Add: *"genuine concern about AI's societal implications — AgentProbe was designed to keep humans in control"* | JD explicitly asks for this |

---

## F) Interview Plan

| # | JD Requirement | Story | S | T | A | R | Reflection |
|---|----------------|-------|---|---|---|---|------------|
| 1 | Design and execute LLM evaluations | AgentProbe 5-metric eval engine | No systematic way to know if LLM output quality held across runs | Design a multi-metric eval system for LLM outputs | Defined 5 metrics (correctness, hallucination, retrieval, completeness, compliance); built LLM-as-judge scoring per metric; tracked across runs in dashboard | Reliable eval signal per run; unexpected patterns surface automatically; Auto Fix triggers on threshold breach | Calibrating judge confidence matters more than raw score — a judge that's wrong 20% of the time destroys eval signal |
| 2 | Dashboards tracking model health | AgentProbe React dashboard | No visibility into whether eval scores were trending up or down across runs | Build dashboard tracking model health over time | React dashboard: per-run eval scores, retrieval quality, generation quality, anomaly flags — all visible across multiple runs | Pattern detection across runs; regressions visible before they compound | Time-series eval tracking is more valuable than point-in-time snapshots |
| 3 | Diagnose anomalous eval results | AgentProbe Auto Fix + RAG Tracer | Eval failure with no attribution — was it retrieval, generation, or prompt? | Build diagnostic system that attributes failures to root cause | RAG Tracer enriches per stage: retrieval score, generation score, prompt inputs — failure attribution to specific component | Auto Fix can act on diagnosis; human sees root cause, not just failure flag | Separating retrieval quality from generation quality is the key diagnostic split — most eval systems conflate them |
| 4 | Distributed data pipelines at scale | Entrata AWS pipelines | Client data in fragmented, manual processes | Build automated pipeline handling 1M+ records | AWS S3 + Glue + EC2; automated quality checks at each stage; Libsodium encryption | 80% workload eliminated; zero security incidents; reliable at scale | Schema validation at ingestion catches 80% of downstream issues |
| 5 | Experiments: prompting + sampling effects | AgentProbe multi-provider + prompt engineering | Need to compare model behavior across providers and prompt variants | Run structured prompt experiments across Anthropic/OpenAI/Groq | Multi-provider eval runs: same query, different providers, different prompt variants; eval engine scores each | Clear signal on which provider/prompt combination performs best per metric | Sampling temperature has outsized effect on hallucination rate — more so than prompt length |

**Case study to present:** AgentProbe eval pipeline — show the 5 metrics, how the dashboard tracks health across runs, and how the Auto Fix agent diagnoses failures. Frame it as: *"This is eval infrastructure at small scale. I understand the problem deeply enough to scale it."*

**Red flag questions:**
- *"You haven't worked on training-time evals"* → *"That's fair — my eval experience is inference-time, not checkpoint evaluation during training. But the core problems are identical: did the model regress, where, and why. I've built the diagnosis and dashboard layer. Learning the training-run operational context is a ramp, not a fundamental gap."*
- *"Why apply to both Anthropic roles?"* → *"They're meaningfully different problems. AI Observability is about monitoring deployed systems. Model Evaluations is about measuring model quality during development. I'm genuinely interested in both — and applied to both because the domain fit is strong in different ways."*

---

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|--------|---------|--------|
| Posting freshness | Active on Greenhouse | Positive |
| Apply button | Active | Positive |
| JD specificity | Named responsibilities (checkpoint testing, training run dashboards, capability + safety evals), specific team context | Positive |
| Salary listed | Yes ($320K–$485K) — rare and strong signal | Positive |
| Company health | Anthropic: top AI safety lab; no layoffs/freeze signals | Positive |
| H-1B | Top-tier sponsor with retained immigration counsel | Positive |
| Different from #037 | Distinct role — training-time vs deployment-time | Positive |

---

## Keywords Extracted

llm evaluation, model health dashboards, eval infrastructure, distributed systems, checkpoint testing, capability evaluation, safety evaluation, observability, experiment tracking, prompting, data pipelines, python, anthropic, research engineer, agentic behavior, reasoning evaluation

---

## Machine Summary

```yaml
report_num: 039
company: Anthropic
role: Research Engineer, Model Evaluations
date: 2026-06-10
score: 3.8
archetype: AI Platform / LLMOps
legitimacy: High Confidence
location: Remote-friendly + SF, CA + NYC, NY
comp_range: "$320K–$485K base"
visa_risk: low (Anthropic = top H-1B sponsor with immigration counsel)
key_gaps:
  - No training-time eval / checkpoint infrastructure experience (main gap)
  - No LLM training dataset curation (preferred only)
key_strengths:
  - AgentProbe 5-metric eval engine = direct proof of LLM evaluation design
  - React dashboard = model health tracking across runs
  - RAG Tracer = observability + anomaly diagnosis
  - Distributed pipelines at Entrata = infrastructure credibility
  - Mission alignment: human oversight framing is authentic
  - Exceptional comp ($320-485K — highest of all roles)
location_risk: low — remote-friendly
recommend: apply — eval depth is strong; training gap is real but bridgeable; highest comp of all roles; same great H-1B sponsor
```
