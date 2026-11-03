# Evaluation: Clive Collective — AI Software Developer (Agentic Systems & Automation)

**Date:** 2026-09-23
**URL:** (pasted JD)
**Archetype:** Agentic / Automation + Applied AI Engineer (both primary)
**Score:** 3.8/5
**Legitimacy:** High Confidence
**PDF:** ❌ below 4.0 hard floor (comp drags score)

---

## A) Role Summary

| Dimension | Details |
|-----------|---------|
| **Archetype** | Agentic / Automation + Applied AI Engineer |
| **Domain** | Restaurant / hospitality — private dining, CRM, lead management, reservation + event platform integrations |
| **Function** | Build production agentic systems, automations, CRM integrations, and AI-powered workflows for restaurant operations |
| **Seniority** | IC — "title matters less than what you can build" |
| **Work model** | Flexible schedule listed — likely remote/hybrid; location not specified |
| **Comp** | $70,000–$90,000 base — **significantly below target** |
| **Sponsorship** | Not mentioned — small restaurant group; sponsorship unlikely |
| **TL;DR** | The technical AI match is one of the cleanest of the session — Claude Code explicitly mentioned, MCP, tool calling, HITL, idempotency, retry logic, event-driven, Python/TypeScript = exact stack. But comp ($70K–$90K) is well below target and drags score below the 4.0 hard floor. Sponsorship unknown/unlikely at a small restaurant company. Score 3.8/5 — SKIP on comp. |

---

## B) Match with CV

| JD Requirement | CV Evidence | Match |
|---|---|---|
| Building with modern AI systems — not just ChatGPT | LeaseI (8-agent LangGraph), AgentProbe (eval infrastructure), Magizhs (shipped to client) | ✅ |
| **Claude Code specifically mentioned** | Uses Claude Code as primary dev tool | ✅ Direct |
| **MCP** | MCP in cv.md ✅ | ✅ |
| Tool calling, agent orchestration, HITL approvals | LeaseI: conditional routing, HITL escalation; AgentProbe: tool-calling agents | ✅ |
| Python and/or JavaScript/TypeScript | Python (8+ yrs), TypeScript in cv.md | ✅ |
| APIs, webhooks, authentication, event-driven | RabbitMQ 7yr event-driven; 20+ API integrations at Entrata; OpenAPI in cv.md | ✅ |
| Idempotency, retry logic, duplicate prevention | RabbitMQ: designed retry + idempotency guarantees; owned through production incidents | ✅ Direct |
| Logging, monitoring, observability | OpenTelemetry, Prometheus, Grafana; AgentProbe trace-level observability | ✅ |
| Evaluation of AI systems (accuracy, reliability, cost) | AgentProbe: 5-metric eval engine, LLM-as-judge, CI regression harness | ✅ Direct |
| CI/CD, automated tests | GitHub Actions, TDD in cv.md | ✅ |
| "Substantial personal project or open-source contribution" | AgentProbe: live open-source on GitHub | ✅ Strong signal |
| CRM, lead management, sales automation | No direct experience | ⚠️ Domain gap |
| Restaurant/hospitality platforms (R365, OpenTable, etc.) | No restaurant domain experience | ⚠️ Domain gap |
| Work directly with operators, translate operational problems | Entrata 7yr: worked with compliance + product + ops stakeholders; Magizhs: direct client collaboration | ✅ Adjacent |
| **Comp: $70K–$90K base** | Target range $80K–$140K; $70K–$90K is below target | ⚠️ Below target |
| **Sponsorship** | Not mentioned — restaurant group; unlikely to sponsor | ⚠️ Risk |

---

## C) Level and Strategy

| Dimension | Finding |
|-----------|---------|
| Technical match | Near-perfect. Claude Code + MCP + tool calling + HITL + idempotency + Python/TypeScript + event-driven = every technical requirement met from cv.md. AgentProbe is the open-source proof point they're specifically asking for. |
| Comp gap | $70K–$90K base is significantly below her $80K–$140K target (and well below the $100K–$160K market for agentic AI skills). Even at $90K top of range, this is below what the technical match would command elsewhere. |
| Sponsorship risk | Clive Collective is a restaurant group, not a tech company. H-1B sponsorship from a restaurant business is uncommon and unlikely. No mention of sponsorship in JD. |
| Domain gap | Restaurant/hospitality CRM + reservations + event platforms — none of this is in her background. JD explicitly says domain knowledge is not required ("title matters less than what you can build"), but she'd be ramping on R365, OpenTable, and restaurant-specific integrations. |

---

## D) Comp and Demand

| Metric | Data |
|--------|------|
| JD range | $70,000–$90,000 base |
| Score | **2.0/5** — significantly below target; below $80K floor at lower end |
| Note | Potential product ownership mentioned but "not guaranteed" — speculative |

---

## G) Posting Legitimacy

| Signal | Finding | Weight |
|--------|---------|--------|
| Company | Clive Collective — restaurant/hospitality group; real operating business | Positive |
| Tech specificity | Claude Code, MCP, Hermes, OpenClaw, R365 — unusually specific and real | Positive |
| Comp disclosed | $70K–$90K | Positive |
| Application requirements | Asks for GitHub, live demo, stack explanation — serious employer, not a ghost posting | Positive |
| Sponsorship | Not mentioned | Unknown |

**Assessment: High Confidence** — real company, unusually well-written JD for a restaurant group. Employer clearly knows what they want.

---

## Verdict

**3.8/5 — SKIP on comp.**

The technical AI match is genuinely one of the strongest of the session — Claude Code mentioned by name, MCP, tool calling, HITL, idempotency, event-driven, Python/TypeScript, open-source GitHub signal — every single requirement maps to Parimala's actual stack.

But: **$70K–$90K is significantly below what these skills command.** The agentic AI + Python + production engineering combination is worth $110K–$160K on the open market right now. Accepting $70K–$90K underprices the skill set by 30–40%.

Additionally, sponsorship from a restaurant group is unlikely.

**If she's willing to take lower comp for a hands-on agentic AI role with real ownership + product equity upside:** worth a conversation. The work itself is interesting and the JD signals a technically serious employer. But go in knowing the comp conversation will be hard.

---

## Application Requirements (if applying)

The JD specifically asks for:
1. A live product, demo, portfolio, or GitHub — **AgentProbe** (`github.com/venkatalakshmiparimala/AgentProbe`) + **LeaseI** (`github.com/venkatalakshmiparimala/Lease_complaince_rag`)
2. Tools + stack + one meaningful technical problem solved
3. A recent agentic AI tool/release you tested + what you learned
4. How you'd turn a manual business workflow into production software

All four are easy wins. AgentProbe directly answers #1, #2, and #4. The idempotency + RabbitMQ story answers the screening question about preventing duplicate sends.

---

## Keywords extracted

Python, JavaScript, TypeScript, Claude Code, MCP, tool calling, agent orchestration, HITL, idempotency, retry logic, event-driven, webhooks, APIs, CRM, lead management, reservations, restaurant platforms, R365, observability, CI/CD, automated testing, LLM evaluation

## Machine Summary
```yaml
company: Clive Collective
role: AI Software Developer (Agentic Systems & Automation)
score: 3.8
archetype: Agentic/Automation + Applied AI Engineer (both primary)
level: IC (3+ yr implied)
comp_range: "$70,000-$90,000 base (below target)"
location: Likely remote/flexible — not specified
sponsorship: Not mentioned — restaurant group; unlikely
apply: SKIP — below 4.0 hard floor; comp drags score (tech match is excellent)
top_proof_points:
  - Claude Code (specifically named in JD — she uses it daily)
  - LeaseI + AgentProbe (MCP + tool calling + HITL + idempotency + eval)
  - RabbitMQ idempotency + retry (exact answer to screening question about duplicate sends)
  - AgentProbe open-source GitHub (specifically requested in application)
key_gap:
  - Comp $70K-$90K vs $100K-$160K market value for these skills
  - Sponsorship unknown/unlikely at restaurant group
  - Restaurant/hospitality domain (minor — not required per JD)
```
