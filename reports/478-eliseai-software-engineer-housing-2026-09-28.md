# 478 — EliseAI — Software Engineer (Housing)

**Score:** 4.8/5
**URL:** https://eliseai.com/careers (or https://jobs.ashbyhq.com/eliseai)
**PDF:** ❌
**Legitimacy:** High Confidence
**Archetype:** Software Engineer (AI-focused, Product Engineering) + Agentic/Automation
**Date:** 2026-09-28

---

## Block A — Match with CV

**Requirements met:**

| JD Requirement | Evidence |
|----------------|----------|
| "1+ years Java, C#, Go, or Python" | 8+ years Python (Entrata backend, LeaseI, AgentProbe) + Java (Entrata India) — vastly exceeds stated bar |
| "System design and scalable architecture" | 20+ production modules at Entrata, 100K+ MAU, 1M+ records, Docker microservices redesign (50% scalability gain) |
| "Build systems that enable autonomous buildings to operate intelligently" | *This is exactly what Parimala did for 8 years.* HUD income-limit pipeline (180K domain records), eligibility/rent calculations, RabbitMQ async workflows — all for property management operations |
| "Work directly with customers to develop and own features end-to-end" | Primary technical consultant for affordable housing customers at Entrata; coordinated cross-system dependencies, validated integrations before go-live |
| "Bias for action, quick idea-to-implementation" | Built LeaseI (8-agent LangGraph platform) and AgentProbe solo; both in production with eval metrics |
| "Startup mindset, ownership, urgency" | 8 years as the sole long-term owner of HUD compliance modules — critical correctness environment (a wrong import affects thousands of residents) |

**Nice-to-haves met:**

| Nice-to-have | Evidence |
|--------------|----------|
| Microservices + event-driven distributed systems | RabbitMQ async pipelines with idempotency + retry logic at Entrata |
| ML and data | LangGraph, AgentProbe eval engine, GMU MS Data Analytics |
| AWS | S3 migration (100% PHI compliance), EC2, RDS, Lambda, Glue |

**Score: 5.0** — every hard requirement met at 8× the stated bar; every nice-to-have covered

---

## Block B — North Star Alignment

- **Primary archetype:** Software Engineer (AI-focused) — listed #1 in _profile.md
- **PropTech domain boost:** EliseAI is a *direct competitor to Entrata* in housing AI — 1 in 6 US apartments. Parimala spent 8 years building the very workflows EliseAI is now automating with AI. No other candidate brings this.
- **"Build systems for autonomous buildings"** = Entrata's mission statement verbatim. This is not a stretch-fit role — it is Parimala's career in AI form.
- LeaseI is the perfect proof point: 8-agent pipeline for housing compliance operations, exactly the kind of AI infrastructure EliseAI is building. Not just a side project — it solves the same class of problem EliseAI solves.
- EliseAI's $250M Series E from a16z, 111+ open roles, rapid growth → strong career trajectory for someone at this stage

**Score: 5.0** — PropTech #1 priority + exact domain + primary archetype + best available proof point

---

## Block C — Comp

- **Stated range:** $240,000–$300,000 base + equity + 100% medical/dental/vision + relocation + unlimited vacation + meals
- This is exceptional compensation — well above the $100K–$140K target and above typical NYC AI startup ranges
- Equity in a unicorn ($1B+ valuation after $250M Series E) adds meaningful upside
- Relocation package included (NYC move)

**Score: 5.0** — top-quartile compensation with equity upside in a well-funded unicorn

---

## Block D — Cultural Signals

**Positive:**
- a16z-backed unicorn, $250M Series E — strong financial position, real growth trajectory
- 100+ deploys/day — genuine engineering culture, not bureaucratic
- "Operate like a small startup within a startup" — high autonomy, high ownership
- Direct customer impact: housing affects millions of renters daily
- Mission alignment with Parimala's 8-year career (affordable housing, leasing, compliance)
- Strong benefits: 401k, unlimited tokens, fitness stipend, relocation support

**Neutral / Watch:**
- 4-5 days in-office NYC — high culture, but requires relocation from Virginia; relocation package is offered
- "Hard, intense, most rewarding work" — this is a high-expectation environment; matches Parimala's track record but worth calibrating in interview
- "We hire the best, expect the best" — implies a competitive screening process

**Score: 4.0** — high conviction on mission/growth/comp; in-office relocation is the only friction

---

## Block E — Red Flags

**Minor:**
- **OPT/H-1B sponsorship:** EliseAI is not a named top H-1B sponsor. As a well-funded startup hiring aggressively (111+ roles), they likely sponsor, but it must be confirmed explicitly during the application process. Include OPT pitch in cover letter.
- **Relocation to NYC required:** Virginia → NYC is a real life change. Relocation package is offered. Not a dealbreaker per location policy ("open to relocation for strong opportunities").

**Not a concern:**
- "1+ year" requirement is vastly exceeded — they're clearly hiring for quality over years-of-experience matching
- In-office culture: user is open to any US location per memory

**Score: −0.2** total penalty (sponsorship uncertainty)

---

## Block F — Global Score

| Dimension | Score |
|-----------|-------|
| Match with CV | 5.0 |
| North Star Alignment | 5.0 |
| Comp | 5.0 |
| Cultural Signals | 4.0 |
| Red Flags | −0.2 |
| **PropTech domain boost** | +0.3 |

**Global: 4.8/5** — Recommend applying immediately. This is the highest-priority role in the current pipeline.

---

## Block G — Posting Legitimacy

- EliseAI raised $250M Series E (a16z) in 2026 — company is actively scaling
- 111+ open roles listed on BuiltIn as of 2026-09-28 — genuine hiring wave
- Specific salary range stated ($240K–$300K) — compliance with salary transparency laws, signals real intent
- JD contains operational specifics ("100+ deploys per day", "design to deployment ownership") — not a ghost posting
- Recent activity on BuiltIn (roles posted hours to days ago)

**Legitimacy: High Confidence**

---

## STAR Stories to Prepare

**"Tell me about a time you owned a critical system end-to-end."**
> At Entrata, I owned the annual HUD income-limit import pipeline for nearly 7 years. A few thousand federal rows expanded into ~180,000 domain records powering eligibility, rent, HAP, and tax-credit calculations for 100K+ housing units. Every release included baseline validation, reconciliation, and rollback preparation — because one wrong import means thousands of residents get the wrong eligibility decision. Zero compliance violations across the ownership period.

**"Tell me about a time you worked directly with customers to build a feature."**
> Served as the primary technical consultant for affordable housing customer onboardings at Entrata. I'd map their multi-system business logic to platform capabilities, write per-team technical specs, coordinate cross-system dependencies, and validate integrations end-to-end before go-live. Zero compliance failures at go-live across every deployment.

**"Tell me about an AI system you built end-to-end."**
> Built LeaseI — a 3-surface enterprise AI platform for housing compliance operations. 8-agent LangGraph pipeline with durable state, hybrid TF-IDF + semantic RAG, HITL escalation when confidence is too low. Core design rule enforced in code: LLM extracts and reasons; deterministic logic or a human makes every final regulated call. 93.6% precision / 87.9% F1 on 1,240 test cases across 5 US states.

---

## ATS Keyword Gap Analysis

**JD keywords → verified present in cv.md:**
- autonomous buildings ❌ (needs patch)
- end-to-end ownership ✅
- scalability and reliability ✅
- continuous integration ✅
- observability ✅
- microservices ✅
- event-driven ✅ (RabbitMQ)
- machine learning ✅
- AWS ✅
- Python ✅
- Java ✅
- product features ✅
- architecture patterns ✅
- startup mindset ❌ (needs framing)
- 100+ deploys ❌ (add fast-release context)

**Patch needed:** Frame summary around "building intelligent software for property operations" and add fast-deployment context.

---

## Machine Summary

```yaml
id: 478
company: EliseAI
role: Software Engineer (Housing)
score: 4.8
archetype: Software Engineer (AI-focused, Product Engineering)
domain: PropTech / Housing AI
location: New York City, NY (In-Office, 4-5 days/week)
salary_range: "$240,000-$300,000"
legitimacy: High Confidence
recommendation: Apply immediately — highest-priority role in pipeline
key_differentiator: 8 years building exactly the workflows EliseAI automates; LeaseI is the proof point
sponsorship_risk: Moderate — not a named top H-1B sponsor; confirm in application
date: 2026-09-28
```
