# 255 — Checkr (Truework Division) — Senior Software Engineer (Python), Mortgage

**Date:** 2026-09-01
**Score:** 4.3/5 — APPLY (PropTech threshold 4.0+)
**URL:** https://job-boards.greenhouse.io/checkr/jobs/8171375
**PDF:** ❌
**Legitimacy:** High Confidence — Live Greenhouse posting, specific salary, YC 2024 + Forbes Cloud 100

---

## Block A — CV Match

**Domain hit: direct.** Truework serves 8 of the top 10 US mortgage lenders with income and employment verification. Entrata's HUD income-limit pipeline is structurally identical: federal source data → 180,000 domain records → eligibility calculations that determine whether residents qualify for housing. The compliance stakes are the same. The data integrity requirements are the same. The regulatory consequences of a wrong output are the same.

**Proof point alignment:**
- Python 8yr ✓
- RESTful APIs (FastAPI) ✓
- JavaScript secondary ✓ (Skills + AI on FHIR React)
- Production ownership at 99.5% uptime, 100K+ MAU ✓
- Monitoring/triage/resolve: debugging tools reduced triage 40% ✓
- Scalable, performant, secure: Docker 50% scalability, 200+ SQL optimizations, Libsodium PHI ✓
- 5+ years requirement: 8 years ✓

**Missing from cv.md:** "MVP", "experimentation", "customer-centric/product-oriented". Patching in CV.

**ATS baseline (cv.md):** 14/18 key terms. Missing: MVP, experimentation, customer-centric, mortgage/income verification explicit language.

---

## Block B — North Star Alignment

**Archetype:** Mid-level Python backend, income/employment verification, PropTech-adjacent. Truework is the exact intersection of: (1) Python production backend, (2) income verification domain = Entrata's core business, (3) financial/compliance data pipeline work the user has done for 7 years.

Strategy shift (2026-07-30) prioritizes PropTech/FDE with 4.0+ apply threshold. This role qualifies on domain alone.

**PropTech boost applied: +0.3**

---

## Block C — Compensation

$185,000 – $218,000 base salary (SF). No hard comp floor currently. This is top-quartile for a Senior SWE Python role. Strong.

**Score: 5/5**

---

## Block D — Cultural Signals

- Checkr: Forbes Cloud 100 2025, Y Combinator 2024 Breakthrough Company, 140K clients (Uber, Airbnb, Anthropic, DoorDash, Pennymac)
- Truework division: semi-independent, startup agility + parent resources — historically the best of both worlds
- Mission: "safe and fair decisions" — mission-driven framing that resonates
- Benefits: 100% medical/dental/vision, $25K fertility/adoption, flexible PTO, monthly stipends, relocation possible
- SF hybrid 3+ days/week — user is open to all US locations; relocation stipend "possible" at hub locations

**Score: 4/5**

---

## Block E — Red Flags

1. **Senior title at formal-leveling company** — Checkr has structured leveling (140K company, 45 open roles). Rejection pattern at AppFolio, Juniper Square, Amazon at Senior level. Mitigating factor: Truework is a startup-within-a-company, may have less rigid leveling formality. JD says "5+ years" — not "7+" or "10+". Flagged but not disqualifying.

2. **Location: SF hybrid 3+ days** — user lives in Virginia. Relocation required or significant travel commitment. User confirmed open to SF.

3. **H-1B sponsorship: UNCONFIRMED** — Checkr does not explicitly state sponsorship policy in JD. EAD (OPT) likely qualifies. Verify before applying.

4. **Posting age**: Fetched live today (2026-09-01). No age concern.

**Adjustment: -0.2**

---

## Block F — Global Score

| Factor | Signal |
|--------|--------|
| CV match | 4.5 — Python, REST APIs, production ownership, domain fit |
| North Star | 4.5 — income verification = Entrata's exact domain |
| Comp | 5.0 — $185K-$218K top quartile |
| Culture | 4.0 — strong company, SF hybrid, relocation possible |
| Red flags | -0.2 — Senior leveling risk + H-1B unconfirmed |
| PropTech boost | +0.3 |

**Global: 4.3/5 — APPLY**

---

## Block G — Posting Legitimacy

**High Confidence.** Live Greenhouse board, specific salary range disclosed, active Apply button, technology specifics match Truework's known stack, company details match public Checkr profile. No ghost indicators.

---

## ATS Keyword Patch for CV

Add to Entrata bullet: "income verification / employment verification" framing; "experimentation / MVP" to Magizhs or projects; "customer-centric" to mentorship/cross-team bullet.

---

## Story Bank — STAR+R

**Income verification domain story (Block A lead):**
- Situation: HUD income limit import — annual federal release, ~180K domain records, wrong import = thousands of residents get wrong eligibility
- Task: Own end-to-end pipeline: fetch → validate → transform → reconcile → deploy
- Action: Built validation suite, rollback preparation, reconciliation checks at every stage
- Result: Zero compliance violations across 7 years of ownership
- Relevance: Truework solves structurally identical problem for mortgage lenders

**Python production reliability story:**
- Situation: RabbitMQ async processing of gross-rent updates across thousands of tenant records
- Task: Design for retry, idempotency, dead-letter handling
- Action: Implemented idempotency guarantees, retry logic, double-processing elimination
- Result: System survived production incidents and annual rent-schedule changes without data corruption
- Relevance: Truework needs same reliability for income/employment verification APIs serving mortgage lenders
