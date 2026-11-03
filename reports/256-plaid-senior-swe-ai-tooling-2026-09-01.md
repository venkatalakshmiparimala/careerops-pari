# 256 — Plaid — Senior Software Engineer, AI Tooling

**Date:** 2026-09-01
**Score:** 4.0/5 — APPLY
**URL:** https://plaid.com/careers/openings/engineering/senior-software-engineer-ai-tooling/
**PDF:** ❌
**Legitimacy:** High Confidence — Live Plaid careers page, specific salary disclosed, role matches Plaid's known AI infrastructure push

---

## Block A — CV Match

**AI tooling builder story: AgentProbe is this.** Plaid wants someone to build AI-native internal tools for non-engineering workflows. AgentProbe is exactly that: a 15-endpoint FastAPI platform for evaluating AI outputs, built for internal engineering workflows at zero vendor cost. The LeaseI platform is also internal tooling — a support investigation platform for engineers and compliance staff.

**Proof point alignment:**
- Python 8yr ✓
- "Hands-on experience using AI-powered development tools, agents, or automation" — LangGraph, agentic workflows, multi-agent orchestration ✓
- "Agentic workflows, automation, or AI-enabled internal applications" — LeaseI + AgentProbe ✓
- "Building and operating production systems" — 99.5% uptime, 100K+ MAU ✓
- "Internal tools, platforms, or workflow software" — Entrata debugging/monitoring tools (40% triage reduction) ✓
- "Define platform constraints for auth" — HIPAA RBAC in AI on FHIR ✓
- "Own systems end-to-end" — 7-year ownership pattern ✓
- 5+ years required: 8 years ✓

**ATS baseline (cv.md):** 15/18 — missing exact phrases "internal tools", "auth", "operate". Patched in CV.

---

## Block B — North Star Alignment

**Archetype:** AI tooling builder at fintech infrastructure company. This is not the PropTech/income-verification archetype, but the AI tooling angle is directly aligned with the user's two strongest projects. Plaid is a confirmed H-1B sponsor (prior evaluation). $190K-$262K pushes comp well above any floor.

**Strategy note:** Role is about internal tooling, not core product. "Translate ambiguous pain points into simple, durable software products" requires product judgment the CV demonstrates via LeaseI's problem-driven design. The user built something because they identified a real internal pain point (engineers spending a day reconstructing context). That's exactly the Plaid narrative.

---

## Block C — Compensation

$190,800 – $262,800/year. Exceptional — top quartile for Senior SWE. No comp floor concern.

**Score: 5/5**

---

## Block D — Cultural Signals

- Plaid is fintech infrastructure powering millions of bank connections (Venmo, Robinhood, Betterment)
- Growing AI team — Engineering Manager + Staff + Senior roles all open simultaneously
- SF HQ / NYC — user open to both
- Plaid confirmed H-1B sponsor (from prior evaluation #85)
- "Retool, Scaffold" mentioned — internal tooling stack, not standard FAANG

**Score: 4.5/5**

---

## Block E — Red Flags

1. **Formal leveling company** — Plaid has structured leveling. Rejection pattern at formal-leveling companies at Senior level. Mitigating: this role explicitly focuses on "first version" and "builder mindset" — may be evaluated differently than core product roles.

2. **"First version" of a new product surface** — This favors entrepreneurial/startup engineering more than reliability maintenance. The user's Entrata story is maintenance + ownership, not "build something that doesn't exist yet." AgentProbe + LeaseI demonstrate the builder pattern though.

3. **Multi-round interview process** — Plaid known for rigorous technical screens. Preferred 2-3 rounds per strategy may be exceeded.

4. **Not fraud/PropTech domain** — Fintech infrastructure but not the income verification story. AI tooling is not domain-specific.

**Adjustment: -0.5**

---

## Block F — Global Score

| Factor | Signal |
|--------|--------|
| CV match | 4.0 — Python, agentic AI, production, internal tooling via AgentProbe/Entrata |
| North Star | 3.5 — AI tooling builder ✓; PropTech/income verification ✗ |
| Comp | 5.0 — $190K-$262K exceptional |
| Culture | 4.5 — top fintech company, AI investment, confirmed H-1B sponsor |
| Red flags | -0.5 — formal leveling risk, builder archetype vs maintenance/reliability |

**Global: 4.0/5 — APPLY**

---

## Block G — Posting Legitimacy

**High Confidence.** Live Plaid careers page, specific salary range, multiple AI roles open simultaneously. No ghost indicators.

---

## ATS Patches for CV

- "internal tools" → AgentProbe = internal AI tooling platform; Entrata internal debugging tools
- "auth" → RBAC authentication boundaries in AI on FHIR
- "operate" → "build, ship, and operate" phrasing in Entrata bullets

---

## Story Bank — STAR+R

**Internal tools builder story (Block A lead):**
- Situation: AI outputs at scale had no systematic way to measure quality — engineers couldn't catch regressions before production
- Task: Build internal tooling to evaluate AI outputs without vendor dependency
- Action: Built AgentProbe — 15-endpoint FastAPI platform, 5-metric quality engine, CI-integrated regression gate
- Result: Zero regressions shipped; engineers can detect AI quality drops before merge
- Relevance: Exactly the "AI-native internal tool surface" Plaid wants — translating ambiguous pain point into simple, durable product

**Ownership from ambiguity story:**
- Situation: LeaseI started with an unclear problem — users couldn't articulate why investigations took a full day
- Task: Define the problem, prototype the solution, validate with real compliance cases
- Action: Built three-surface platform, iterated from MVP to 93.6% precision
- Result: Clear, evidence-backed root-cause hypotheses across 1,240 test cases
- Relevance: "Translate ambiguous internal pain points into simple, durable software products"
