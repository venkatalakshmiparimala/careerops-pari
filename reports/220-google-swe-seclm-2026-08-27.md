# Evaluation: Google — Software Engineer (SecLM / Gemini AI)

**Date:** 2026-08-27
**URL:** (not provided — pasted as JD text; verify posting is active before applying)
**Archetype:** AI Platform / LLMOps + Agentic / Automation (hybrid)
**Score:** 4.1/5
**Legitimacy:** Proceed with Caution
**PDF:** output/cv-venkata-lakshmi-parimala-pasupuleti-google-2026-08-27.pdf

---

## A) Role Summary

| Dimension | Detail |
|-----------|--------|
| Archetype | AI Platform / LLMOps + Agentic / Automation (hybrid) |
| Domain | Security AI — Gemini SecLM platform (RAG + agentic workflows over Mandiant security intelligence) |
| Function | Build — implement AI features, RAG pipelines, agentic workflows, ML infrastructure |
| Seniority | "Software Engineer" — 2yr Python minimum; maps to L4 at Google. NOT "Senior SWE" — hard block does NOT apply. |
| Remote | Not specified; Google SWE roles are typically hybrid |
| Comp | $147K–$210K base + 15% bonus + equity — TC likely $250K–$350K+ at L4 |
| TL;DR | Build the AI engineering layer of Google's security AI platform (SecLM) — RAG, agentic orchestration, evaluations, ML infrastructure — using Gemini and Mandiant's threat intelligence. |

---

## B) Match with CV

| JD Requirement | CV Match | Quality |
|----------------|----------|---------|
| Bachelor's degree | MS Data Analytics Engineering, GPA 3.87 — exceeds minimum; preferred MS/PhD met | **STRONG** |
| 2+ years Python | 8+ years Python at Entrata + all AI projects | **STRONG** |
| 1+ year GenAI | AgentProbe (eval engine, LangGraph, multi-provider routing) + LeaseI (8-agent LangGraph, RAG) + Magizhs internship | **STRONG** |
| RAG pipelines / grounding | LeaseI hand-rolled TF-IDF RAG (100% citation correctness, 0% unsupported-claim rate); AgentProbe ChromaDB RAG eval | **STRONG** |
| Agentic workflows | LeaseI 8-agent LangGraph StateGraph with conditional routing + HITL escalation; AgentProbe 3-agent orchestration | **STRONG** |
| Evaluations | AgentProbe 5-metric eval engine + CI-integrated regression gate, 1,240+ test cases | **STRONG** |
| ML infrastructure | FastAPI microservices, CI/CD, Docker — not GPU/SageMaker infra | **PARTIAL** |
| Model optimization / data processing | PySpark, feature engineering (CrashClarity, GMU research) | **PARTIAL** |
| GoLang (preferred) | Not in stack | **GAP** |
| Data structures / algorithms (preferred) | Academic exposure; not a highlighted strength | **PARTIAL** |
| Security domain | No cybersecurity background | **GAP** (not required for builder role) |

### Gaps and mitigations

| Gap | Blocker? | Mitigation |
|-----|----------|-----------|
| GoLang | No (preferred only) | "Python-primary; can pick up Go — shipped production async systems (RabbitMQ, idempotency guarantees) at Entrata" |
| Security domain | No — engineers build the platform; Mandiant provides the intelligence data | Frame as "I build the AI orchestration layer; security expertise lives in the retrieval corpus" |
| D&A depth (LeetCode bar) | **Yes — primary risk** | Google's coding bar requires Medium-Hard LeetCode fluency + systems design. Needs 3-4 weeks dedicated prep. Non-negotiable. |
| ML infra at Google scale | No — SecLM is applied AI, not infra | AgentProbe + LeaseI cover applied ML; emphasize "production-grade AI systems, not GPU infra" |

---

## C) Level and Strategy

**Level:** Maps to L4 at Google (base $150K–$175K). The $147K–$210K JD range spans L4-L5. With 8+ years total but one-employer depth + academic AI projects, likely L4 offer.

**Hard block check:** Title is "Software Engineer" — NOT "Senior SWE." The profile HARD BLOCK for Google Senior SWE does NOT apply. This is the correct level target.

**"Sell at the right level" plan:**
- Lead with the two production AI systems (AgentProbe + LeaseI) — Google values shipped systems, not concepts.
- The security context parallels LeaseI's compliance AI: "LLM reasons, human or deterministic logic decides every regulated call" mirrors the trust requirements of security AI recommendations.
- Frame Entrata HUD pipeline as data reliability under regulatory pressure — parallels security intelligence data integrity.
- L4 at Google expects ownership of features, not org leadership. Frame accordingly.

**Critical interview risk:** Google's SWE process runs 4-5 rounds: coding (2x, LeetCode Medium-Hard), systems design (1-2x), behavioral (Googleyness). Without 3-4 weeks of focused algorithmic prep, this is the primary failure mode regardless of fit. Start prep immediately if applying.

**"If downleveled to L3" plan:** Accept only if total comp (base + equity + bonus) clears $200K+ and H-1B sponsorship is confirmed. Request 12-month promotion review.

---

## D) Comp and Demand

| Level | Base | Bonus (15%) | Equity (est. annual) | Est. TC |
|-------|------|------------|---------------------|---------|
| L4 (likely) | $150K–$175K | $22K–$26K | $80K–$120K | $250K–$320K |
| L5 (stretch) | $180K–$210K | $27K–$31K | $120K–$200K | $330K–$440K |
| JD published base | $147K–$210K | 15% target | not disclosed | — |

Levels.fyi 2026: L4 median TC = $288K, L5 median TC = $414K.

**Comp score: 5.0/5** — top of market for any AI/SWE role. Even at L4, this is 2-3x the PropTech/mid-level target range.

**H-1B:** Google is among the top 5 H-1B sponsors in the US. Essentially no sponsorship risk.

**Demand trend:** Google is actively hiring AI/ML engineers (2,000 planned) while cutting non-AI headcount. SecLM/Gemini Cloud AI roles fall into the hiring category. Cloud revenue +63% YoY.

---

## E) Customization Plan

| # | Section | Change | Why |
|---|---------|--------|-----|
| 1 | Summary | Lead with "generative AI" + RAG + agentic workflows; add "security-domain AI" angle (LeaseI compliance trust AI → parallels SecLM) | SecLM is trust/compliance AI — cite "LLM reasons, human decides" as trust engineering |
| 2 | AgentProbe | "AI evaluation framework" → "LLM evaluation and grounding verification framework" | Mirrors "evaluations incorporating security intelligence" JD language |
| 3 | LeaseI | Add "information retrieval" and "grounding" as explicit terms | These are SecLM's exact language for RAG with security data |
| 4 | Skills | Surface "Python, LangChain, LangGraph, RAG, Agentic AI, LLM Evaluation, Grounding" as lead cluster | Matches JD minimums + preferred exactly |
| 5 | Entrata | Add "system reliability" framing: "zero violations across 7 years" | Google values reliability signals alongside feature velocity |

---

## F) Interview Plan

| # | JD Requirement | STAR+R Story | Key metrics |
|---|---------------|-------------|------------|
| 1 | RAG / grounding | LeaseI Phase 1 TF-IDF RAG | 100% citation correctness, 0% unsupported-claim rate — every answer grounded or flagged |
| 2 | Agentic workflows | LeaseI 8-agent LangGraph | Correctly traces false-ineligibility to misconfigured setting; HITL when confidence too low |
| 3 | Evaluations | AgentProbe eval engine | 5 metrics, 1,240+ test cases, CI-integrated regression gate; pass@1 81.7% |
| 4 | Code quality + design reviews | Entrata 300+ peer reviews + debugging tools | 40% debugging time reduction, <10 bugs for 6+ months |
| 5 | Triage / debug production issues | Entrata HUD pipeline incident ownership | Zero compliance violations across 7 years of annual cycles |
| 6 | Cross-functional collaboration | Entrata AWS S3 migration | Led AH module integration across teams; 100% PHI compliance, zero security incidents |

**Recommended case study:** LeaseI — "I built a 3-surface AI platform where every final decision in a regulated context is either grounded to a cited source or escalated to a human. That same trust architecture is what SecLM needs for security recommendations." Direct framing for a security AI audience.

**Red-flag questions:**
- *"No Go experience?"* → "Python-primary. I shipped production systems at Entrata in PHP when I had zero prior PHP experience — onboarded and shipped in the first sprint. Go is syntactically closer to Python than PHP was."
- *"No security background?"* → "SecLM's AI layer is about grounding, retrieval accuracy, and agentic reliability. That's exactly what I built in LeaseI. The Mandiant intelligence is the security layer; my job is to make the AI orchestration trustworthy."

---

## G) Posting Legitimacy

**Assessment: Proceed with Caution**

| Signal | Finding | Weight |
|--------|---------|--------|
| JD source | Pasted as text — no URL or date | Neutral |
| Company legitimacy | Google/Alphabet — unquestionable | **Positive** |
| JD tech specificity | SecLM, Gemini, RAG, agentic workflows, Mandiant — product-specific, not generic | **Positive** |
| Salary published | $147K–$210K explicitly stated | **Positive** |
| Google AI hiring | 2,000 AI/ML engineer hires planned; Cloud revenue +63% | **Positive** |
| Google Cloud cybersecurity cuts | Mandiant-linked cybersecurity staff laid off in 2026 | **Caution** |
| SecLM/Mandiant dependency | JD cites "Mandiant's frontline intelligence" — team restructuring near product | **Caution** |
| H-1B sponsorship | Google files thousands of LCAs annually; tier-1 sponsor | **Positive** |

**Context notes:** Mandiant staff cuts appear to be security practitioners (analysts), not AI platform engineers. Google is simultaneously cutting non-AI headcount and hiring AI engineers — this role is in the "hiring" bucket. Verify posting is active before investing significant interview prep effort.

---

## Keywords extracted

SecLM, Gemini, generative AI, RAG, grounding, agentic workflows, LLM evaluation, Python, GoLang, information retrieval, distributed computing, large-scale system design, natural language processing, AI platform, ML infrastructure, model optimization, data processing, code reviews, testability, security intelligence, Mandiant, threat intelligence, Google Cloud

---

## Machine Summary

```yaml
company: Google
role: Software Engineer (SecLM / Gemini AI)
date: 2026-08-27
score: 4.1
archetype: AI Platform / LLMOps + Agentic / Automation
legitimacy: Proceed with Caution
recommend: apply (with LeetCode prep as prerequisite)
comp_low: 147000
comp_high: 210000
tc_est_l4: 250000-320000
location: US (hybrid, location not specified)
h1b_sponsor: confirmed (tier-1)
hard_block: NO (title is "Software Engineer" not "Senior SWE")
key_gap: GoLang (preferred only), security domain, algorithmic interview bar
key_strength: RAG + agentic + LLM eval (AgentProbe + LeaseI = direct proof points)
interview_warning: Google algorithmic bar requires 3-4 weeks dedicated LeetCode prep
```
