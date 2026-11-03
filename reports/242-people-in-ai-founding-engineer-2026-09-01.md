# Evaluation: People In AI (Unnamed Startup) — Founding Engineer

**Date:** 2026-09-01
**URL:** (LinkedIn Easy Apply — verify on LinkedIn or contact Jacob Bisson)
**Archetype:** Forward Deployed Engineer / Founding Engineer (AI-native data platform)
**Score:** 4.3/5
**Legitimacy:** Medium Confidence — recruiter-posted, company identity not disclosed
**PDF:** —

---

## A) Role Summary

| Dimension | Detail |
|-----------|--------|
| Archetype | FDE / Founding Engineer — first full-time engineer at an early-stage AI startup; own product, architecture, data pipelines, AI evaluation, and customer delivery |
| Team | ~2 people (technical founder + this hire); company not named — recruiter is People In AI |
| Function | Ship product end-to-end; design reliable data ingestion pipelines; build AI evaluation and validation systems; diagnose failure modes; work directly with customers; shape engineering culture |
| Seniority | Founding Engineer (first hire) — startup, no formal leveling; no hard block |
| Location | NYC Metropolitan Area, Hybrid |
| Comp | **$170,000–$190,000 base + 1%–2% equity** (significant at early stage with capital) |
| H-1B | **Not confirmed — critical risk.** First engineer hire at early-stage startup; H-1B infrastructure unlikely to exist yet. "Well-funded" is stated — verify sponsorship before pursuing. |
| TL;DR | AgentProbe IS this job description. "Build evaluation and validation systems around models and AI agents" — that is AgentProbe, word for word. LeaseI covers "agentic AI workflows." Entrata covers "reliable pipelines, multi-tenant architecture, fragmented data." FDE archetype is the primary target. H-1B at first-engineer stage is the critical unknown. Score 4.3/5. |

---

## B) Match with CV

### What You'll Do

| Responsibility | CV Match | Quality |
|----------------|----------|---------|
| Own critical product and engineering systems end-to-end | HUD pipeline ownership (7yr, sole owner); 20+ production modules shipped end-to-end at Entrata | **STRONG** |
| Design reliable pipelines and integrations for complex, fragmented data | HUD import (federal→180K domain records); RabbitMQ event-driven processing; ETL pipelines; AWS Glue; multi-source data ingestion | **STRONG** |
| **Build evaluation and validation systems around models and AI agents** | **AgentProbe: 5-metric eval engine (correctness, groundedness, latency, token efficiency, hallucination rate), CI regression gate, LLM-as-judge, pass@k harness — this is the responsibility, not a proxy** | **EXACT MATCH** |
| **Diagnose AI failure modes and improve reliability, accuracy and efficiency** | **AgentProbe: hallucination detection, confidence scoring, failure mode analysis; LeaseI: HITL escalation when confidence too low; 93.6% precision across 1,240 test cases** | **EXACT MATCH** |
| Work directly with customers to turn operational challenges into intuitive product experiences | Entrata: cross-functional delivery with customers and PMs across 120+ sprints; LeaseI built from a real customer investigation failure | **STRONG** |
| Pragmatic architectural decisions: security, data isolation, scalability | PHI-compliant Libsodium pipelines (zero incidents); Entrata multi-tenant SaaS (100K+ MAU); Docker microservices (50% scalability improvement) | **STRONG** |
| Shape engineering culture, standards, future hiring | Mentored 5+ engineers; 300+ peer code reviews; built internal debugging tools | **MODERATE** |

### What You'll Bring

| Requirement | CV Match | Quality |
|-------------|----------|---------|
| Owning systems and architectural decisions in fast-moving environments | Entrata remote (Sep 2018–Aug 2024); 7yr sole ownership of compliance-critical pipeline | **STRONG** |
| Track record shipping directly to customers, iterating quickly | 20+ production modules; AgentProbe open-source (public); LeaseI end-to-end | **STRONG** |
| AI-native engineering approach, rigorously evaluating outputs | AgentProbe was built precisely because "vibes-based" evaluation wasn't enough for compliance-critical AI | **STRONG** |
| Production AI: evaluations, observability, failure modes, cost | AgentProbe: 15-endpoint eval backend, multi-provider LLM routing (cost control), agent observability dashboard | **STRONG** |
| Mentoring / early team-building | 5+ engineers mentored; 300+ code reviews | **MODERATE** |

### Tech Stack

| Stack Item | CV Match | Quality |
|------------|----------|---------|
| Agentic AI and LLM-powered workflows | LeaseI (8-agent LangGraph) + Magizhs (agentic mission planner) | **STRONG** |
| Model evaluation and validation | AgentProbe — this is the exact system described | **EXACT** |
| Data ingestion and processing pipelines | HUD pipeline, RabbitMQ, ETL, AWS Glue, PySpark | **STRONG** |
| Secure multi-tenant architecture | Entrata: PHI compliance, Libsodium encryption, multi-tenant SaaS | **STRONG** |
| Third-party integrations | Multiple external integrations at Entrata (HUD, federal, state regulatory systems) | **MODERATE** |
| Production AI observability | AgentProbe dashboard (40% debugging time reduction); agent tracing in skills | **STRONG** |

---

## C) Assessment

**No hard block fires.**

"Founding Engineer" is not a Senior/Staff title at a formal-leveling company — it's a startup's first hire. No language hard block (Python is not excluded). No clearance requirement. NYC hybrid is acceptable.

**This job description is AgentProbe + LeaseI + Entrata in a single posting.**

Every responsibility maps to a named proof point:
- "Build evaluation and validation systems around AI agents" → AgentProbe (not a stretch — this is the definition of AgentProbe)
- "Diagnose AI failure modes" → AgentProbe hallucination detection + LeaseI HITL confidence gate
- "Design reliable pipelines for fragmented data" → HUD pipeline (few thousand federal rows → 180K domain records, zero violations over 7 years)
- "Secure multi-tenant architecture" → Entrata PHI compliance, Libsodium, zero security incidents

The "AI-native engineering approach using modern models while rigorously evaluating their outputs" is the specific combination most candidates cannot demonstrate: building and shipping AI *and* building the evaluation infrastructure to know whether it works. AgentProbe is that infrastructure.

**The company is unnamed — medium legitimacy.**

People In AI is a specialist AI recruiter (legitimate firm). The unnamed company is described as: early-stage, well-funded, "complex data-heavy business workflows," "operational and financial problems within a large, established industry." That suggests FinTech, insurance, healthcare, legal, or PropTech — all domains where Entrata experience (regulatory compliance, multi-tenant, fragmented data) transfers. No red flags in the JD language itself. Jacob Bisson (job poster) is identifiable on LinkedIn — recruiter relationship is real.

**H-1B is the critical question.**

First full-time engineer at an early-stage startup almost certainly means no existing H-1B infrastructure. Sponsoring H-1B requires an immigration attorney, USCIS cap registration, and time. "Well-funded" suggests they have resources to do it — but the intent must be confirmed before investing time. Contact Jacob Bisson directly before applying: *"Does the company sponsor H-1B for this role?"*

**Comp is strong for an early-stage role.**

$170K–$190K base is solid. The 1%–2% equity is the real story: at an early-stage company with capital and early traction, that's meaningful if they succeed. This is not a typical underpaying startup — they have capital and are paying market rate.

**Score: 4.3/5**

| Factor | Weight |
|--------|--------|
| FDE/Founding Engineer archetype = primary target | +++ |
| AgentProbe = exact "build eval/validation systems for AI agents" | +++ |
| Entrata multi-tenant + pipelines + PHI compliance | +++ |
| LeaseI = agentic workflows | ++ |
| Comp: $170K–$190K + 1%–2% equity | ++ |
| H-1B at first-engineer stage = critical unknown | -0.4 |
| Company identity hidden | -0.1 |

Above 4.0 FDE threshold → **APPLY** after H-1B confirmation.

---

## D) Comp

| Metric | Value |
|--------|-------|
| Base | $170,000–$190,000 |
| Equity | 1%–2% (early-stage; significant if company succeeds) |
| Bonus | Not mentioned |
| TC estimate | $175K–$200K near-term; upside is in equity |
| vs. target | Above prior floor; strong for FDE/founding role |
| Comp score | 4.5/5 |

---

## E) If You Apply

**Before submitting:** Message Jacob Bisson on LinkedIn — "Does the company sponsor H-1B visas for this role?" One question, one message. Don't spend time on the application until confirmed.

**If H-1B confirmed — CV framing:**

| Angle | Framing |
|-------|---------|
| AI evaluation ownership | "Built AgentProbe from scratch: 5-metric eval engine, CI regression gate, LLM-as-judge, hallucination detection — exactly the evaluation and validation infrastructure this role describes" |
| Founding context | "Owned Entrata's HUD compliance pipeline solo for 7 years — zero violations, zero security incidents; I know what full ownership of a compliance-critical system actually means" |
| Data pipelines | "Designed and maintained data ingestion pipelines for regulatory data at scale (180K domain records per release cycle)" |
| Agentic AI | "LeaseI: 8-agent autonomous investigation platform built end-to-end — same pattern as the AI workflows described here" |

**Cover letter hook:** Lead with AgentProbe and the insight behind it — *"I built an eval framework because I didn't trust vibes-based AI assessment for compliance-critical decisions."* That's exactly the "AI-native, rigorous evaluation" mindset the JD is looking for.

---

## G) Posting Legitimacy

**Medium Confidence**

| Signal | Finding |
|--------|---------|
| Recruiter | People In AI — specialist AI talent firm, identifiable LinkedIn presence |
| Job poster | Jacob Bisson — Hiring Engineer for high-growth startups; identifiable on LinkedIn |
| Company | **Not disclosed** — described but not named |
| JD specificity | High — specific tech stack, specific responsibilities, specific equity range |
| Comp transparency | $170K–$190K + 1%–2% equity listed explicitly — unusual and positive |
| Easy Apply | LinkedIn Easy Apply suggests active recruiter posting, not scraped |

---

## Machine Summary

```yaml
company: People In AI (unnamed startup)
role: Founding Engineer
date: 2026-09-01
score: 4.3
archetype: Forward Deployed Engineer / Founding Engineer (AI-native data platform)
legitimacy: Medium Confidence — recruiter posting, company not named; People In AI is a real firm
recommend: APPLY — FDE threshold met (4.0+); AgentProbe = exact "build eval/validation systems for AI agents"; H-1B MUST be verified before applying (first-engineer hire at early-stage startup = no existing H-1B infrastructure likely)
comp_low: 170000
comp_high: 190000
comp_equity: 1%-2% (early stage)
comp_tc_est: 175000-200000 near-term; equity upside significant
location: NYC Metropolitan Area (Hybrid)
h1b_sponsor: unconfirmed — CRITICAL; message Jacob Bisson before applying
hard_block: NO — "Founding Engineer" title not Senior/Staff; Python not excluded; no clearance
key_gap: H-1B unknown at early-stage startup; company identity hidden
key_strength: AgentProbe (exact eval/validation systems match); LeaseI (agentic workflows); Entrata (reliable pipelines, multi-tenant, PHI compliance, fragmented data ownership 7yr); FDE archetype = primary target
priority: APPLY after H-1B confirmed — 4.3/5, FDE threshold exceeded
```
