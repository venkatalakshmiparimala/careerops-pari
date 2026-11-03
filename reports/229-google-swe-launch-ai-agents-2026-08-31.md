# Evaluation: Google — Software Engineer, Launch Team (AI Agents + Evaluation)

**Date:** 2026-08-31
**URL:** (pasted as JD text — verify on careers.google.com)
**Archetype:** Agentic / AI Platform (hybrid — evaluation frameworks + agent orchestration)
**Score:** 4.5/5
**Legitimacy:** High Confidence
**PDF:** output/cv-venkata-lakshmi-parimala-pasupuleti-google-launch-2026-08-31.pdf

---

## A) Role Summary

| Dimension | Detail |
|-----------|--------|
| Archetype | Agentic / AI Platform hybrid — AI agents for SDLC automation + automated evaluation frameworks |
| Team | Launch team (Core) — automated SDLC governance, AI-driven launch workflows for Google development teams |
| Function | Build AI agents + "skills," evaluation frameworks for agent accuracy/safety, observability/monitoring, full feature lifecycle ownership |
| Seniority | "Software Engineer" (no Senior prefix in title) — salary $147K–$210K maps to L4/L5 at Google |
| Location | Not specified in JD — Google offices (Mountain View, NYC, etc.) |
| Comp | $147,000–$210,000 + 15% bonus target + equity |
| H-1B | Tier-1 — Google (Alphabet) is among the highest-volume H-1B sponsors in the US |
| TL;DR | Near-perfect archetype match. AgentProbe IS the evaluation framework this JD describes. LeaseI IS the agentic workflow system. MCP is called out explicitly in preferred quals. The technical depth maps to every responsibility. Google's interview loop requires LeetCode prep — that's the only gate. |

---

## B) Match with CV

### Minimum Qualifications

| Requirement | CV Match | Quality |
|-------------|----------|---------|
| Bachelor's or equivalent | B.Tech CS (JNTU) + M.S. Data Analytics Engineering (GMU, GPA 3.87) | STRONG |
| 2yr Python/Java/Kotlin | 8+ years Python | STRONG |
| Building AI/ML platforms for cloud customers | AgentProbe: cloud-deployable, REST API-native eval platform; Entrata AI pipeline (PyTorch + OpenAI API) | STRONG |

### Preferred Qualifications

| Requirement | CV Match | Quality |
|-------------|----------|---------|
| Master's in CS or related | M.S. Data Analytics Engineering GMU (GPA 3.87) | STRONG |
| Web applications | FastAPI (15-endpoint), Flask, React, Streamlit | STRONG |
| Scalable backend services + complex data models | 100K+ MAU, 99.5% uptime; schema design for 20+ production modules | STRONG |
| Generative AI + LLMs + Agentic workflows | AgentProbe (multi-provider LLM routing) + LeaseI (8-agent LangGraph) | STRONG |
| **MCP (Model Context Protocol)** | **AgentProbe MCP architecture — rare; explicitly in JD preferred quals** | **STRONG** |
| CLI, text processing, web applications | Bash scripting, Python text pipelines, FastAPI/Flask | STRONG |

### Responsibilities

| Responsibility | CV Proof Point | Quality |
|----------------|----------------|---------|
| Design + implement AI agents and "skills" | LeaseI: 8-node LangGraph with discrete agent skills (Triage, Retrieval, Reasoning, Validation, Escalation) | STRONG |
| Build automated evaluation frameworks | **AgentProbe = exactly this** — 5-metric eval engine, CI regression gate, LLM-as-judge, pass@k harness | EXACT MATCH |
| Measure agent performance, accuracy, safety | AgentProbe: correctness, groundedness, hallucination rate, latency, token efficiency | EXACT MATCH |
| Full lifecycle ownership (design → deployment → maintenance) | Entrata: 120+ sprints, 20+ modules end-to-end; AgentProbe + LeaseI built and maintained | STRONG |
| Observability + monitoring + alerting | AgentProbe React dashboard, structured logging, per-run metric tracking, CI gates | STRONG |
| Code reviews + testing coverage + documentation | 300+ reviews; AgentProbe CI regression gate; 120+ sprint docs | STRONG |
| Identify gaps + technical debt + bottlenecks | Entrata: 200+ SQL query optimizations; AgentProbe: eval harness catching regressions | STRONG |

---

## C) Level and Strategy

Title is "Software Engineer" — no Senior prefix. Google uses this title across L3–L5 externally; salary range ($147K–$210K) maps to L4 (mid) or low-L5. Hard block (Senior at formal-leveling company) does **not** fire on this title.

**Why this role is exceptional for Parimala:**

1. **AgentProbe is the answer to every evaluation framework question.** JD says "build and maintain automated evaluation frameworks to measure agent performance, accuracy, and safety." AgentProbe does exactly that: 5-metric eval engine (correctness, groundedness, hallucination, latency, token efficiency), CI-integrated regression gate, LLM-as-judge scoring, pass@k harness across 1,240+ test cases. No other candidate will walk in with this.

2. **LeaseI answers every agent design question.** JD says "design, implement, and refine AI agents and their underlying skills." LeaseI is an 8-node LangGraph system with discrete, composable agent skills that route, retrieve, reason, validate, and escalate — exactly the pattern the Launch team is describing for SDLC automation.

3. **MCP is explicitly listed in preferred quals.** AgentProbe's MCP architecture — any agent connects via REST API without code changes — maps directly. This is rare in the candidate pool.

4. **The mission is observability and velocity.** "Compresses end-to-end feature delivery timelines... proactive compliance posture." Parimala built a platform (AgentProbe) for exactly this in the AI evaluation context.

**Interview note:** Google's loop requires LeetCode (DSA: medium/hard) + system design rounds. The technical fit is exceptional — 2–3 weeks of LeetCode prep is the prerequisite, same as #220 (Google SecLM). This is the investment to unlock a $200K+ TC role at the world's top H-1B sponsor.

---

## D) Comp

| Metric | Value |
|--------|-------|
| Base | $147,000–$210,000 |
| Bonus | 15% target (~$22K–$31.5K) |
| Equity | Google RSUs — significant at L4/L5 (est. $50K–$150K/yr vesting) |
| TC estimate | $220K–$380K (L4–L5 range at Google) |
| vs. target ($80K–$140K) | Substantially above target — top-quartile outcome |
| Comp score | 5.0/5 |

H-1B: Alphabet/Google filed 4,000+ LCA petitions in FY2025 — among the top sponsors in the US. Approval rate ~99%.

---

## E) Customization Plan

| # | Section | Change | Why |
|---|---------|--------|-----|
| 1 | Summary | Lead with evaluation frameworks + agentic systems + MCP | Mirrors JD's first two responsibilities exactly |
| 2 | AgentProbe | "Automated evaluation framework: 5-metric eval engine, CI regression gate, LLM-as-judge, pass@k harness" | JD says "build and maintain automated evaluation frameworks" |
| 3 | LeaseI | "8-agent LangGraph with composable agent skills — Triage, Retrieval, Reasoning, Validation, Escalation" | JD says "design AI agents and their underlying skills" |
| 4 | Entrata | "Full lifecycle ownership + observability tooling: debug dashboards, performance monitoring, telemetry" | JD says "observability and predictability" |
| 5 | Skills | Surface MCP, LLM evaluation, agent orchestration, observability first | ATS + recruiter keyword alignment |

---

## F) Interview Plan

| # | JD Requirement | Story | Metric |
|---|---------------|-------|--------|
| 1 | Automated evaluation frameworks | AgentProbe eval engine | 5 metrics, 1,240+ test cases, pass@1 81.7% |
| 2 | Agent design + skills | LeaseI 8-node LangGraph | Triage → Retrieval → Reasoning → Validation → Escalation |
| 3 | Observability + monitoring | AgentProbe React dashboard | Per-run metrics, retrieval drift, latency tracking |
| 4 | Full lifecycle ownership | Entrata 120+ sprints + LeaseI/AgentProbe | Design → deploy → maintain → incident response |
| 5 | MCP | AgentProbe MCP architecture | Any agent via REST API; plug-and-play enterprise connectivity |
| 6 | Safety + accuracy in agents | LeaseI responsible AI rule | LLM reasons, deterministic logic decides every regulated call |
| 7 | Code quality + testing | AgentProbe CI regression gate + 300+ Entrata reviews | Zero regressions merged without eval gate passing |

**LeetCode prep path (2–3 weeks before applying):**
- Focus: Arrays/Strings, Trees, Graphs, Dynamic Programming (medium difficulty)
- Google-specific: system design at scale (distributed eval systems, agent orchestration infra)
- Same guidance as #220 (Google SecLM)

---

## G) Posting Legitimacy

**High Confidence**

| Signal | Finding | Weight |
|--------|---------|--------|
| Company | Google / Alphabet — S&P 500, top-5 market cap | Positive |
| JD specificity | Named team (Launch/Core), specific mission, agent skills vocabulary | Positive |
| No PERM signals | No LI-DNI/LI-DNP, no DOL boilerplate, no exact address, no prevailing wage floor | Positive |
| Salary | $147K–$210K wide range — real market comp, not prevailing wage | Positive |
| Preferred quals depth | MCP, agentic workflows, evaluation frameworks — recruiter-written specificity | Positive |
| H-1B | Tier-1 — 4,000+ LCA filings FY2025, ~99% approval | Positive |

---

## Keywords Extracted

software engineer, AI agents, evaluation frameworks, agent performance, agentic workflows, MCP, Model Context Protocol, LLMs, generative AI, observability, monitoring, logging, alerting, Python, scalable backend, web applications, CI/CD, SDLC, code reviews, testing coverage, technical documentation, Google, Core team, Launch team, automated evaluation, agent safety

---

## Machine Summary

```yaml
company: Google (Alphabet)
role: Software Engineer, Launch Team (AI Agents + Evaluation)
date: 2026-08-31
score: 4.5
archetype: Agentic / AI Platform (hybrid)
legitimacy: High Confidence
recommend: APPLY — near-perfect archetype match; AgentProbe = exact eval framework; LeaseI = exact agentic system; MCP in preferred quals; H-1B tier-1; prereq 2-3wk LeetCode prep
comp_low: 147000
comp_high: 210000
comp_bonus: 15% target
comp_tc_est: 220000-380000
location: unspecified (Google offices — Mountain View / NYC / etc.)
h1b_sponsor: tier-1 (4000+ LCA FY2025, ~99% approval)
hard_block: NO — title is "Software Engineer" not Senior
key_gap: Google interview loop requires LeetCode prep (2-3 weeks); no GCP-specific experience
key_strength: AgentProbe = automated evaluation framework (exact JD match); LeaseI = 8-agent system with composable skills; MCP explicit in preferred quals — rare combination
priority: high — 4.5/5, top archetype match, top H-1B sponsor, $220K+ TC potential
```
