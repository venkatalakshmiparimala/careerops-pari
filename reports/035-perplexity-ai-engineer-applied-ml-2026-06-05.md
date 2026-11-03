# Evaluation: Perplexity — AI Engineer, Applied ML (MTS Software Engineer, Applied AI)

**Date:** 2026-06-05
**URL:** https://jobs.ashbyhq.com/perplexity/3c656963-876a-458d-bca6-916a42a24c1a
**Archetype:** ML Engineer / AI Platform
**Score:** 3.8/5
**Legitimacy:** High Confidence
**PDF:** pending

---

## A) Role Summary

| Field | Detail |
|-------|--------|
| Archetype | ML Engineer / AI Platform |
| Domain | Applied ML, LLM personalization, RAG, query understanding, agentic decomposition |
| Function | Build + Research |
| Seniority | Mid-Senior (MS/PhD preferred; equivalent experience accepted) |
| Remote | Onsite — New York, NY (SF also listed) |
| Comp | $160K–$240K base; $250K–$450K+ total comp (Levels.fyi, June 2026) |
| TL;DR | Own the full ML lifecycle at Perplexity — data analysis, modeling, LLM evaluation, A/B testing, and iterative improvement across personalization, query understanding, and content discovery. |

---

## B) Match with CV

| JD Requirement | CV Match | Strength |
|----------------|----------|----------|
| BS/MS/PhD in CS or related | M.S. Data Analytics Engineering, GMU (GPA 3.87, May 2026) | ✅ Strong |
| Full ML lifecycle (data → model → eval → monitoring) | AgentProbe 5-metric eval engine; CrashClarity (feature engineering → model → dashboard); AI on FHIR (NLP pipeline) | ✅ Strong |
| LLM prompt engineering | AgentProbe LLM Router + Auto Fix agent (automated prompt iteration) | ✅ Direct proof |
| RAG-based systems | AgentProbe: ChromaDB RAG pipeline, retrieval evaluation, RAG Tracer agent | ✅ Direct proof |
| Query understanding / intent modeling | AI on FHIR: NLP-to-FHIR query mapping (EN/ES), intent → structured API call | ✅ Adjacent |
| Agentic decomposition | AgentProbe Orchestrator agent: multi-step reasoning, tool routing, decomposition | ✅ Direct proof |
| Open-source contributions in ML/NLP/IR | AgentProbe: public GitHub, open-source eval toolkit | ✅ Strong signal |
| LLM evaluation + iterative improvement | AgentProbe: 5-metric judges + Auto Fix = evaluation-driven improvement loop | ✅ Direct proof |
| Personalization (user modeling, retrieval, ranking) | Not in CV — AgentProbe does retrieval eval but not user-level personalization | ⚠️ Real gap |
| Content discovery / feed ranking | Not in CV | ⚠️ Real gap |
| Production ML at consumer scale | AgentProbe is project-scale; Entrata is enterprise but not ML-driven | ⚠️ Gap |
| A/B testing at scale | Not explicitly in CV | ⚠️ Soft gap |

**Gaps and mitigations:**
- **Personalization / user modeling / content ranking** — Hard: this is 40% of the JD. ChromaDB retrieval and RAG ranking are adjacent but not user personalization. Mitigate by framing AgentProbe's retrieval quality metric (ranking relevant chunks) as ranking experience. Acknowledge gap honestly if asked.
- **Consumer-scale production ML** — Soft: Perplexity runs at tens of millions of queries/day. AgentProbe is project-scale. Entrata's 1M+ records + 100K+ MAU is adjacent infrastructure scale. Mitigate by framing Entrata as production discipline, AgentProbe as applied ML depth.
- **A/B testing** — Soft: not in CV but standard practice. Note TDD/BDD mindset and eval-driven iteration as analog.
- **H-1B sponsorship** — Medium risk: Perplexity filed only 3 LCAs in FY2026, with a stated policy of "case-by-case" sponsorship. Not a hard no, but worth flagging.

---

## C) Level and Strategy

**Level detected:** Mid-Senior IC (MTS = Member of Technical Staff — standard SWE level at AI-first startups). MS + 8+ years = strong fit.

**Sell plan:**
- Lead with AgentProbe as proof of the exact applied ML loop they're describing: data → model → eval → iterate
- Frame the 5-metric eval engine + Auto Fix agent as a closed-loop improvement system — the same cycle the JD describes ("evaluation, offline/online A/B testing, and iterative improvement")
- Quote: *"I built AgentProbe's Auto Fix agent because I needed a system that closes the loop automatically — eval detects failure, fix agent rewrites the prompt, re-runs the eval. That's exactly Perplexity's applied ML cycle."*
- The open-source signal is important here — Perplexity values research-adjacent contributors. Lead with the GitHub link.

**On personalization gap:** Don't fabricate experience. Frame ChromaDB retrieval ranking (relevance scoring across chunks) as adjacent. In cover letter, acknowledge the gap and signal appetite to ramp.

---

## D) Comp and Demand

| Source | Range | Notes |
|--------|-------|-------|
| Levels.fyi (June 2026) | $200K–$507K total comp | Median $507K for SWE; base $160K–$240K |
| Glassdoor | $180K–$300K | Engineering roles, limited data |
| Market context | AI-first startup, Series B+ stage, high-growth | Strong equity upside |

**Assessment:** Base $160K–$240K is 14–71% above Parimala's $100K–$140K target. Total comp with equity ($250K–$450K+) is exceptional. Perplexity valuation has grown significantly — meaningful equity upside.

**H-1B risk: MEDIUM** — Only 3 LCAs filed FY2026 (vs. Decagon: 9, Glean: confirmed). Perplexity's stated policy: "unable to sponsor for all roles or candidates." Ask during recruiter screen before investing heavily.

---

## E) Customization Plan

| # | Section | Current | Proposed change | Why |
|---|---------|---------|-----------------|-----|
| 1 | Summary | Generic SWE + AI builder | Lead with: *"ML engineer — built AgentProbe, an open-source applied ML system with LLM-powered evaluation, RAG retrieval pipelines, and automated prompt iteration. Full ML lifecycle from data to production."* | Mirrors JD language |
| 2 | AgentProbe bullet | General description | Emphasize: evaluation-driven improvement loop, retrieval ranking, query decomposition via Orchestrator agent | JD: eval + A/B testing + iterative improvement |
| 3 | AgentProbe project | RAG Tracer description | Reframe: *"RAG retrieval evaluation — scores ranking quality of retrieved chunks against query intent"* | Closest proxy for retrieval/ranking experience |
| 4 | AI on FHIR | NLP pipeline | Reframe as: *"Query understanding pipeline mapping natural language intent to structured API calls (EN/ES)"* | JD: query understanding + intent modeling |
| 5 | CrashClarity | Predictive modeling | Keep — demonstrates full ML lifecycle (feature engineering → model → evaluation → dashboard) | JD: data analysis → modeling → evaluation |
| 6 | Skills | ML section | Promote: evaluation, prompt engineering, RAG, embeddings; add "iterative model improvement" | JD keyword alignment |

---

## F) Interview Plan

| # | JD Requirement | Story | S | T | A | R | Reflection |
|---|----------------|-------|---|---|---|---|------------|
| 1 | LLM evaluation + iterative improvement | AgentProbe eval loop | No automated way to detect model degradation between releases | Build closed-loop eval system | LLM judges score 5 metrics → Auto Fix agent rewrites prompt on failure → re-runs eval | Automated prompt iteration without human intervention per eval cycle | Human-in-the-loop checkpoints still needed at confidence thresholds |
| 2 | RAG + retrieval | AgentProbe RAG Tracer | Couldn't tell if retrieval was the failure point or generation | Build trace-level retrieval evaluation | RAG Tracer agent enriches traces: retrieval score per chunk, relevance ranking, completeness check | Full trace visibility from query → retrieval → generation → eval score | Chunk-level relevance scoring matters more than document-level |
| 3 | Query understanding / intent | AI on FHIR NLP pipeline | Clinicians couldn't query FHIR records without coding | Build NL-to-API query understanding system | spaCy + BERT + LLMs to map EN/ES intent → structured FHIR API call | ~60% reduction in manual retrieval time; multilingual | Intent disambiguation before API call is the hardest part |
| 4 | Full ML lifecycle | CrashClarity + AgentProbe | Needed to go from raw data to actionable insights + deployed model | Own data → model → eval → deploy cycle | Feature engineering, RF + LR modeling, evaluation, GitHub Pages dashboard | 85%+ accuracy; non-technical stakeholder-accessible outputs | Model interpretability matters as much as accuracy for real-world use |
| 5 | Cross-functional collaboration | Entrata 120+ sprints | Shifting requirements across product, design, QA teams | Own features end-to-end across full-stack | Agile/Scrum collaboration, TDD/BDD, peer code reviews, documentation | Sub-10 bug count 6+ consecutive months; 40% deployment time reduction | Write decisions down — that's the real cross-functional multiplier |

**Case study to present:** AgentProbe eval loop — query decomposition (Orchestrator) → retrieval (ChromaDB RAG) → generation → LLM judge scoring → Auto Fix prompt iteration. Frame it as: *"A closed-loop applied ML system. This is the cycle Perplexity runs at scale."*

**Red flag questions:**
- *"You don't have personalization experience"* → *"That's fair — user modeling and feed ranking are areas I'd ramp into. But the ML infrastructure is identical: retrieval, ranking, evaluation, iteration. I've built all of those components in AgentProbe and CrashClarity. The domain-specific patterns are 4-6 weeks."*
- *"Can Perplexity sponsor your visa?"* → Ask early in recruiter screen. Their policy is case-by-case — worth confirming before going deep.

---

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|--------|---------|--------|
| Posting freshness | Active on Ashby + LinkedIn + ZipRecruiter + Greenhouse mirror | Positive |
| Apply button | Active | Positive |
| JD specificity | Named domains (personalization, query understanding, content discovery), specific techniques (RAG, prompt engineering, A/B testing) | Positive |
| Company health | Series B+, growing fast, no layoffs/freeze signals in 2026 | Positive |
| H-1B | 3 LCAs FY2026 — low volume, case-by-case policy | Caution |
| Salary listed | Not in JD; market data from Levels.fyi ($160K–$240K base) | Neutral |
| Reposting | Not seen in scan-history.tsv | Positive |

---

## Keywords Extracted

applied ml, ai engineer, llm, rag, retrieval, ranking, personalization, user modeling, query understanding, intent modeling, agentic decomposition, prompt engineering, evaluation, a/b testing, ml lifecycle, feature engineering, open source, nlp, information retrieval, python, member of technical staff, perplexity

---

## Machine Summary

```yaml
report_num: 035
company: Perplexity
role: AI Engineer, Applied ML (MTS Software Engineer, Applied AI)
date: 2026-06-05
score: 3.8
archetype: ML Engineer / AI Platform
legitimacy: High Confidence
location: New York, NY (also SF) — onsite
comp_range: "$160K–$240K base; $250K–$450K+ total comp"
visa_risk: medium (3 LCAs FY2026, case-by-case sponsorship policy)
key_gaps:
  - Personalization / user modeling / content ranking (real gap — 40% of JD)
  - Consumer-scale production ML
  - A/B testing at scale
  - H-1B sponsorship not guaranteed
key_strengths:
  - AgentProbe = direct proof of RAG, LLM eval, prompt iteration, agentic decomposition
  - Open-source contribution signal (valued at research-adjacent companies)
  - Full ML lifecycle demonstrated across AgentProbe + CrashClarity + AI on FHIR
  - MS GPA 3.87 — strong for research-adjacent role
location_risk: high — onsite NYC or SF from Virginia
recommend: apply but verify visa sponsorship early in recruiter screen; personalization gap is real, be honest about it
```
