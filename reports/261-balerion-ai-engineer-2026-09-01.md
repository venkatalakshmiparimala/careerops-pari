# 261 — Balerion AI — AI/Software Engineer (Agentic Mortgage Platform)

**Date:** 2026-09-01
**Score:** 4.8/5 — APPLY (PropTech/mortgage boost +0.3 applied)
**URL:** https://news.ycombinator.com/item?id=49522897 (HN: Who is hiring? September 2026)
**PDF:** ❌
**Legitimacy:** High Confidence — $6M seed Kleiner Perkins-led (April 2026), paying customer FM Home Loans ($2B+ loan volume), named founders (Berkeley/PayPal/Ocrolus/Snowflake), visa sponsorship confirmed, company page live at balerion.ai

---

## Block A — CV Match

**Domain match is exceptional — income verification is the core product.**

| JD Requirement | CV Proof Point |
|---------------|----------------|
| Income qualification & document processing for mortgage | Entrata: owned HUD income-limit pipeline 7 years — federal source → 180,000 domain records powering housing eligibility + income compliance ✓ |
| "Routing scanned pages to OCR vs. text extraction when text layer is unreliable" | LeaseI: OCR in tech stack; document extraction pipeline for lease compliance data ✓ |
| "Extraction pipelines where a wrong number is much worse than a missing one" | Entrata: 100% PHI compliance, Libsodium encryption, income data integrity across 100K+ housing units ✓ |
| "Running long agent workflows durably so failure doesn't restart the whole loan" | Entrata: RabbitMQ async processing with retry, idempotency, and dead-letter guarantees (= Restate concept) ✓ |
| "Evaluating multi-step output against guidelines that are themselves ambiguous" | AgentProbe: LLM-as-judge scoring against ambiguous quality criteria, 5-metric eval engine, CI-integrated regression gate ✓ |
| Python (production-grade) | Python 8yr, FastAPI, production SaaS platform ✓ |
| AWS | S3, EC2, RDS, Glue at enterprise scale ✓ |
| Docker + CI/CD | Docker containerization (50% scalability improvement), GitHub Actions CI/CD ✓ |
| Agentic AI workflows | LeaseI 8-agent LangGraph stateful system + AgentProbe ✓ |
| PydanticAI (Python AI framework) | Python 8yr + Pydantic-family pattern; structured outputs throughout LeaseI ✓ |
| Postgres | PostgreSQL throughout Entrata multi-tenant SaaS ✓ |

**ATS note:** Application is email-based (vishal@balerion.ai, subject "HN") — no ATS scoring system. Quality of CV and domain alignment matter most.

**Only gap:** Restate (durable execution framework) — not in background, but RabbitMQ idempotency/retry patterns are the same architectural concept; easy to speak to.

---

## Block B — North Star Alignment

**Archetype: AI Engineer at early-stage PropTech/mortgage startup.** Balerion AI is solving the $12K/loan mortgage origination cost problem with agentic AI — exactly the AI-for-regulated-workflows problem LeaseI and AgentProbe address. KP-backed with paying enterprise customer = not vaporware. Income qualification is the literal product; user's 7yr HUD income-limit pipeline is the most relevant background in the market.

---

## Block C — Compensation

$250K+ base salary + meaningful seed-stage equity (KP-led Series: serious upside) + 5% 401(k) match + full health coverage + commuter stipend + gym membership + daily office breakfast & lunch + full relocation to SF covered. Top quartile in total comp; seed equity at KP-backed company has real upside.

**Score: 5/5**

---

## Block D — Cultural Signals

- Kleiner Perkins-led seed ($6M, April 2026) = serious investor validation
- Founders from Berkeley, PayPal, Ocrolus (document AI specialists), Snowflake — technical caliber
- Paying customer already deployed (FM Home Loans, $2B+ volume) = product-market signal
- 10-person team = founder-adjacent early hire; high ownership, high impact
- HN posting = engineering-forward culture (HN is where technical founders hire)
- "Build with Claude Code every day" mentioned in adjacent HN postings from same cohort — agentic AI companies at this stage tend to use Anthropic stack
- Full relocation covered = serious about bringing the right person to SF

**Score: 4.5/5**

---

## Block E — Red Flags

1. **Seed stage risk** — 10-person team, ~6 months post-funding; inherently higher risk than established company. Mitigated: KP-led, paying customer, specific domain moat.
2. **Onsite SF** — full-time onsite in San Francisco; user is in Virginia; relocation covered and user confirmed open to SF.
3. **PydanticAI / Restate** — neither in cv.md; Python expertise and RabbitMQ idempotency/retry patterns cover the conceptual overlap.
4. **Informal application process** — email only (vishal@balerion.ai, subject "HN"); no ATS; faster response but less structured.

**Adjustment: -0.2 (seed stage risk + tech stack specifics)**

---

## Block F — Global Score

| Factor | Signal |
|--------|--------|
| CV match | 5.0 — income qualification pipeline = core product; OCR+document extraction; durable async; evals; Python 8yr |
| North Star | 4.5 — AI Engineer at PropTech mortgage startup; exactly the archetype |
| Comp | 5.0 — $250K+ base + KP seed equity + full benefits + relocation |
| Culture | 4.5 — KP-backed, paying customer, Berkeley/PayPal/Ocrolus founders, HN-found |
| Red flags | -0.2 — seed stage, onsite SF relocation, PydanticAI/Restate gap |
| PropTech boost | +0.3 |

**Global: 4.8/5 — APPLY**

**How to apply:** Email vishal@balerion.ai with subject line containing "HN" + resume PDF + GitHub link

---

## Block G — Posting Legitimacy

**High Confidence.** Company page live at balerion.ai, $6M seed announced April 2026 (Kleiner Perkins-led, covered by Pulse2), FM Home Loans customer deployment confirmed, named founders with verifiable backgrounds (LinkedIn/Berkeley). HN "Who is hiring?" posting format with specific technical problems described = authentic engineering team, not recruiter post. CTO's personal email for applications = founder-level hiring.

---

## Story Bank — STAR+R

**Income verification domain story (exact match):**
- Situation: Mortgage origination requires accurate income data — wrong numbers on a loan have regulatory consequences more serious than missing numbers
- Task: Own end-to-end income-limit pipeline for federal HUD affordable housing eligibility
- Action: Built and maintained pipeline 7 years — federal source → 180,000 domain records → income thresholds powering eligibility decisions across 100K+ housing units; 100% data integrity guarantees (Libsodium-encrypted PHI pipelines, zero incidents)
- Result: 99.5% uptime SLA, 100K+ monthly active users depending on income data accuracy
- Relevance: "Extraction pipelines where a wrong number is much worse than a missing one" — this is the exact invariant we enforced

**Durable agent workflow story:**
- Situation: LeaseI needed multi-step agent workflows that survive partial failures without restarting the full investigation
- Task: Build 8-agent pipeline where each step's completion is idempotent and failure at step N doesn't replay steps 1-N-1
- Action: LangGraph stateful system with state persistence at each node; at Entrata, RabbitMQ with retry, dead-letter, and idempotency guarantees on 7yr income pipeline
- Result: 99.5% uptime SLA; agent workflows complete even under degraded conditions
- Relevance: "Running long agent workflows durably so a failure three steps in doesn't restart the whole loan"

**Eval against ambiguous guidelines story:**
- Situation: AgentProbe needed to evaluate whether LLM outputs met compliance criteria — but compliance guidelines are inherently ambiguous (what counts as "correct" answer to a lease compliance question?)
- Task: Build evaluation that works against ambiguous ground truth
- Action: LLM-as-judge scoring where the judge model interprets ambiguous criteria; 5-metric engine (correctness, groundedness, hallucination rate, latency, token efficiency); calibrated against 1,240 test cases
- Result: Zero regressions shipped; even ambiguous criteria have measurable regression gates
- Relevance: "Evaluating multi-step output against guidelines that are themselves ambiguous"

## Machine Summary

```yaml
company: Balerion AI
role: AI/Software Engineer (Agentic Mortgage Platform)
score: 4.8
status: Evaluated
date: 2026-09-01
salary_low: 250000
salary_high: 300000
location: San Francisco CA (onsite, relocation covered)
remote: false
visa: confirmed
proptech_boost: true
h1b_status: confirmed
apply_method: email (vishal@balerion.ai, subject HN + resume + GitHub)
top_match: income verification pipeline domain exact match; OCR document extraction; durable async workflows; multi-step agent evals
gaps: PydanticAI/Restate not in cv.md; seed stage risk
```
