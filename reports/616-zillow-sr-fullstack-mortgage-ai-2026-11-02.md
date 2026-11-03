# 616 — Zillow — Senior Fullstack Engineer, Mortgage Fulfillment AI

**Date:** 2026-11-02
**Score:** 4.1/5
**URL:** https://zillow.wd5.myworkdayjobs.com/zillow_group_external/job/remote-usa/senior-fullstack-engineer--mortgage-fulfillment-ai_p751548-2
**PDF:** ✅ `output/zillow-mortgage-ai-cv-2026-11-02.pdf`
**Legitimacy:** Tier 1 — Direct company posting (Workday)

---

## A — Role & Company Fit

Zillow Group is the most-visited US real estate platform. The Mortgage Fulfillment AI team is building agentic AI to shorten the mortgage journey — document collection, condition clearing, closing coordination — reducing human handoffs in a regulated financial environment.

Parimala's fit:
- **Entrata lender-facing workflows** — HUD/Tax Credit certification pipelines, income verification, lender data integrations. Direct analog to mortgage fulfillment operations.
- **Agentic systems + evals** — exactly what the role centers on: agent design, eval infrastructure, agent core infra.
- **LeaseI** — 8-agent LangGraph platform over financial documents with LLM-as-judge CI evals, HITL escalation, production reliability (idempotency, retries).
- **Remote Virginia** — $156K–$249K range for VA.

Key risks:
- **8+ years YOE** — she has 7+ (close but stated as requirement).
- **Senior title at Zillow** — large formal-leveling company; risk per strategy.
- **Mortgage-specific** — TRID/RESPA/Encompass domain not in background; real estate adjacent but not direct mortgage.

**Score: 4.1/5** (PropTech threshold 4.0 cleared)

---

## B — Technical Match

| Requirement | Coverage |
|-------------|----------|
| Agentic AI system design | ✅ LeaseI 8-agent LangGraph + Intuit (current) |
| Eval pipeline design | ✅ AgentProbe + LeaseI LLM-as-judge CI harness |
| LLM/ML serving + orchestration | ✅ FastAPI + LangGraph + Anthropic Claude |
| Idempotency / retries / reliability | ✅ RabbitMQ async (Entrata, 99.5% uptime) |
| Third-party API integrations | ✅ HUD/Tax Credit federal integrations (Entrata) |
| Observability + structured logging | ✅ Prometheus + OpenTelemetry (Intuit current) |
| Python + cloud (AWS) | ✅ Full coverage |
| Mortgage domain (TRID/RESPA/Encompass) | ⚠️ Real estate adjacent, not direct; learning curve |
| 8+ years YOE | ⚠️ 7+ years (Jan 2017–present) |

---

## C — Compensation

Remote Virginia: $156K–$249K base + equity. Strong comp for a mid-level band.

---

## D — Location & Logistics

Fully remote, any US state including Virginia. Sponsorship unknown — Zillow historically UNKNOWN, sponsorship case-by-case at large tech companies.

---

## E — Growth & Mission

Zillow Mortgage Fulfillment is a well-funded team with a clear AI mission. "Senior" at Zillow translates to strong L5/L6 IC scope. Real career signal in the resume.

---

## F — Recommendation

**Apply** — 4.1/5. PropTech threshold cleared. Lender-facing Entrata workflows + LeaseI agentic eval system tell a compelling story. Senior leveling at Zillow is a known risk given past patterns but the role is IC-focused and not management. Sponsorship TBD.

---

## Machine Summary

```yaml
id: 616
company: Zillow
role: Senior Fullstack Engineer, Mortgage Fulfillment AI
score: 4.1
date: "2026-11-02"
archetype: agentic-ai-engineer
domain: proptech-mortgage
location: remote-US
status: Evaluated
pdf: zillow-mortgage-ai-cv-2026-11-02.pdf
strengths:
  - Entrata lender-facing HUD/Tax Credit workflows — mortgage adjacent
  - LeaseI 8-agent + eval infra — exact role focus
  - AgentProbe LLM-as-judge CI harness
  - Remote VA $156K-$249K comp
gaps:
  - 8yr YOE req (she has 7+)
  - Senior at Zillow (formal leveling risk)
  - Mortgage-specific domain (TRID/RESPA/Encompass) — learning curve
  - Sponsorship TBD
recommendation: Apply with caution on Senior leveling risk
```
