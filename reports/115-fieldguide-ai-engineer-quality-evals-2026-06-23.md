# 115 — Fieldguide · AI Engineer, Quality (Evals)

**Date:** 2026-06-23
**Score:** 4.3/5
**URL:** https://jobs.ashbyhq.com/fieldguide/d86bef91-71ab-494f-a3c8-393ad8c55063
**PDF:** ❌
**Legitimacy:** Medium Confidence — Fieldguide (YC-backed, 8VC-backed, audit AI startup); Ashby ATS; active posting confirmed 2026-06-23

---

## Block A — Role Summary

| Field | Detail |
|---|---|
| Archetype | AI Platform / LLMOps — Evaluation Infrastructure |
| Domain | Audit & Advisory AI — evaluation platform for agentic audit workflows at enterprise scale |
| Function | Build unified eval platform, observability systems, automated model evaluation pipelines, comparison frameworks, production feedback loops |
| Seniority | Mid-Senior (no explicit year requirement; "multiple years shipping production software") |
| Location | San Francisco, CA preferred · Remote US accepted |
| Comp | $170,000–$220,000 + equity |
| H-1B | ⚠️ Unconfirmed — YC/8VC-backed startup; no LCA filings found; verify before investing interview time |

---

## Block B — Match with CV

| Requirement | Evidence | Strength |
|---|---|---|
| Evaluation infrastructure for agentic systems | AgentProbe 5-metric LLM-as-judge engine, CI/CD quality gates, pass@k harness | ✅ Direct — AgentProbe IS this job |
| LangGraph | AgentProbe (3-agent LangGraph runtime) | ✅ Direct |
| LangSmith integration | Not specifically (AgentProbe builds equivalent trace-level observability) | ⚠️ Tooling gap — same concept |
| Langfuse | Not in stack | ⚠️ Minor — learnable |
| Python | 8+ years production | ✅ Strong |
| TypeScript | Listed in skills; AgentProbe backend adjacent | ✅ Good |
| React | AgentProbe React observability dashboard | ✅ Direct |
| PostgreSQL | 8+ years at Entrata across 200+ SQL queries | ✅ Strong |
| Production LLM features shipped | Entrata AI pipeline (1.6M records, quality gates, prod deployment) | ✅ Strong |
| Observability / trace execution | AgentProbe: per-run metrics, retrieval quality, regression drift, latency dashboard | ✅ Direct |
| Automated model evaluation pipelines | AgentProbe CI/CD gates blocking failing runs before production | ✅ Direct |
| Compliance-adjacent domain | LeaseI (10 compliance rules, auditable decisions) + AI on FHIR (HIPAA) | ✅ Good — audit domain is regulatory |
| "Multiple years shipping production software" | 8 years Entrata, 20+ modules, 120+ Agile sprints | ✅ Strong |

**Gap assessment:** No meaningful technical gaps. LangSmith/Langfuse are tooling wrappers around concepts AgentProbe already implements. TypeScript is listed in her skills. This is the strongest technical match in the pipeline for evaluation work.

---

## Block C — Level & Strategy

No explicit year requirement. "Multiple years of experience" + $170K–$220K suggests mid-senior expectations. The role is about **evaluation methodology and shipping**, not classical CS — no DSA risk. Fieldguide wants someone who thinks deeply about what good AI evaluation looks like and builds it. AgentProbe demonstrates exactly that.

**Domain:** Fieldguide builds AI for accounting and audit professionals — a regulated, compliance-heavy domain. Not PropTech, but compliance and auditability are core themes in LeaseI (deterministic rules engine, full audit trail) and AI on FHIR (HIPAA RBAC). Frame compliance AI experience as directly transferable.

**Positioning:**
1. **AgentProbe = the product they're building** — 5-metric eval engine, CI/CD gates, trace observability. Most candidates talk about evaluation theory; you shipped an eval system.
2. **Compliance + auditability angle** — LeaseI's deterministic rules engine + full audit trail maps to what audit AI needs.
3. **Production discipline** — Entrata's quality gates and output validation show you've shipped AI into production with zero tolerance for errors.

**H-1B is the gating question.** Verify in first recruiter contact. YC/8VC-backed startups at this stage often do sponsor (they need global talent to compete), but it is not confirmed.

---

## Block D — Comp

$170,000–$220,000 + equity. Well above target ($100K–$140K). Equity meaningful at YC/8VC-backed stage — depends on series and valuation. Strong offer if H-1B confirms.

---

## Block E — Why 4.3

| Factor | Score |
|---|---|
| CV match | 4.8 — AgentProbe is literally the job description |
| North Star fit | 5.0 — Evaluation infrastructure for agentic systems = highest-priority archetype |
| Comp | 5.0 — well above target |
| Location | 4.5 — Remote accepted; SF preferred adds mild friction |
| AgentProbe eval boost | +0.3 |
| H-1B unconfirmed | -0.5 — startup, no LCA filings found |
| TypeScript depth | -0.2 — listed but not primary stack |
| **Global** | **4.3/5** |

**Note:** If H-1B confirms → score rises to 4.8/5. This is the best technical match in the pipeline.

---

## Block G — Posting Legitimacy

**Medium Confidence.**
- Fieldguide: YC-backed (W22), 8VC-backed audit AI startup; legitimate company with real funding
- Role posted on Ashby ATS + YC jobs board + 8VC jobs board — multi-channel = likely active
- H-1B: no LCA filings found — small startup, may not have sponsored before
- Salary disclosed ($170K–$220K) — legitimate signal

## Machine Summary

```yaml
id: 115
company: Fieldguide
role: AI Engineer, Quality (Evals)
date: 2026-06-23
score: 4.3
status: Evaluated
pdf: false
url: https://jobs.ashbyhq.com/fieldguide/d86bef91-71ab-494f-a3c8-393ad8c55063
location: SF preferred / Remote US
comp_base: "$170,000–$220,000"
archetype: AI Platform / LLMOps — Evaluation Infrastructure
verdict: Best technical match in pipeline; H-1B unconfirmed is the only blocker — verify first, apply immediately if confirmed
```
