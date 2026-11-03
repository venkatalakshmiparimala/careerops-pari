# 340 — Evinova (AstraZeneca) — Senior Software Engineer (Study Designer)

**Date:** 2026-09-10
**Score:** 3.8/5 — APPLY (⚠️ CLOSING TOMORROW 11-Sept-2026; Claude Code explicit JD match; FastAPI + Python + React + TypeScript + AWS = core stack; RAG pipelines + MCP both listed in AI stack; production ownership culture exact match; visa unconfirmed but AstraZeneca multinational = likely sponsors)
**URL:** AstraZeneca Careers — Senior Software Engineer, Evinova Study Designer (Gaithersburg, MD) — Job ID R-259750
**PDF:** ✅ `output/340-evinova-senior-swe-study-designer-2026-09-10.pdf`
**Legitimacy:** High Confidence — Evinova is AstraZeneca's digital health subsidiary (NASDAQ: AZN); active role posted 09/09/2026; salary disclosed; real product (Study Designer for clinical teams)

---

## Machine Summary

```yaml
company: Evinova (AstraZeneca)
role: Senior Software Engineer (Study Designer)
score: 3.8
status: Applied
date: 2026-09-10
salary_low: 127352
salary_high: 167149
location: Gaithersburg, MD (hybrid 3 days/office, WFH Friday)
remote: partial (Mon-Thu office, Fri WFH)
visa: UNCONFIRMED — JD silent on sponsorship; AstraZeneca is a UK/Sweden multinational with US operations and is a historic H-1B sponsor; not confirmed for this specific role
proptech_boost: false
h1b_status: likely_sponsors_unconfirmed
target_level: Senior SWE — health-tech startup culture under AstraZeneca (not FAANG formal leveling)
top_match: Claude Code explicitly named in JD ("Claude Code, Cursor, Copilot — or equivalents") = strongest differentiator; FastAPI ✓; Python 9yr ✓; React + TypeScript ✓; AWS ✓; Docker ✓; GitHub Actions ✓; RAG pipelines ✓ (AgentProbe + LeaseI); MCP ✓ (LeaseI); PostgreSQL ✓; production ownership mindset (7yr Entrata 99.5% uptime) = exact JD culture match; observability/tracing (AgentProbe LangFuse-equivalent); mentoring + code reviews ✓
gaps: Node.js (listed as backend alongside Python — Python-primary candidate); Kubernetes/EKS (not in profile); LangFuse (specific tool — but observability concept is present); AWS Bedrock (user uses Anthropic API directly); MongoDB (not in profile); Visa not confirmed; Gaithersburg MD ~50 min from Arlington VA (3 days/week = manageable)
closing_date: 2026-09-11 — TOMORROW
```

---

## Block A — Archetype Fit (4/5)

**Archetype: Software Engineer (AI-focused) + Applied AI Engineer**

Study Designer is a clinical trial design product — complex domain logic + fast-moving AI. The JD is unusually explicit about how they want engineers to work: "build things that last AND ship things that work," "responsible for your code in production," "use AI fluently, not blindly." That culture description maps exactly to how this candidate works: Claude Code daily as primary tool, owns features end-to-end, 7yr production ownership at Entrata.

The AI/ML infra stack listed — AWS Bedrock, LiteLLM, **LangFuse**, **OpenTelemetry**, **RAG pipelines**, **MCP** — is where the fit shines. AgentProbe has LangFuse-equivalent structured tracing + 5-metric eval engine. LeaseI has both RAG pipelines and MCP. Both are explicit in the JD.

Gap: "Node.js" sits in the backend list alongside Python. The user is Python-primary. TypeScript + React is strong on the frontend side. The JD says "we don't expect full coverage" on the stack — Python + FastAPI + React + TypeScript + AWS covers most of it.

## Block B — Technical Fit (3.5/5)

**Confirmed matches:**
- ✅ Python (9yr, required depth)
- ✅ FastAPI (explicit — LeaseI + AgentProbe + Magizhs backend)
- ✅ React + TypeScript (frontend — Entrata, AI on FHIR)
- ✅ PostgreSQL (Entrata 200+ query optimizations)
- ✅ AWS (S3, EC2, RDS) — primary cloud
- ✅ Docker (microservices redesign at Entrata)
- ✅ GitHub Actions CI/CD (AgentProbe CI regression gate)
- ✅ RAG pipelines (LeaseI TF-IDF RAG + AgentProbe ChromaDB RAG)
- ✅ MCP (LeaseI architecture)
- ✅ Claude Code (daily — explicit JD call-out)
- ✅ Redis/ElastiCache (Redis caching in profile)
- ✅ LangGraph (AgentProbe + LeaseI 8-agent)
- ✅ Production observability + tracing (AgentProbe structured tracing, Entrata monitoring + alerting)
- ✅ Mentoring + code reviews (5+ engineers mentored, 300+ reviews)

**Gaps:**
- ⚠️ Node.js — primary backend language alongside Python; not in profile
- ⚠️ Kubernetes/EKS — not in profile; Docker ✓ but not K8s
- ⚠️ LangFuse — specific tool; AgentProbe's tracing is conceptually equivalent
- ⚠️ AWS Bedrock — user uses Anthropic API directly (same capability, different API)
- ⚠️ MongoDB — not in profile
- ⚠️ Kafka — RabbitMQ is similar (event-driven async) but not Kafka specifically
- ⚠️ Next.js — not in profile
- ❌ AWS CDK (TypeScript) — not in profile

## Block C — Compensation (3.5/5)

$127,352–$167,149 + STI bonus + equity-based long-term incentive + full benefits (401k, health, tuition reimbursement). For Gaithersburg MD (lower COL than DC proper), this is solid. The equity component at an AstraZeneca subsidiary is meaningful. Tuition reimbursement relevant for M.S. completion. Acceptable range.

## Block D — Risk Flags (3.5/5)

⚠️ **Visa unconfirmed:** AstraZeneca (parent company) is a UK/Sweden multinational that has historically sponsored H-1B in the US extensively. Evinova is its digital health subsidiary. No explicit statement in this JD either way. Risk: moderate. If AstraZeneca's US ops policy applies = likely fine. If Evinova operates as a separate H-1B filer = unknown.

⚠️ **Node.js gap:** Backend is Node.js + Python. If the Study Designer team is Node.js-heavy, Python-primary candidate may feel this. Python + FastAPI + TypeScript + React coverage is strong enough to get through screening.

✅ **Not FAANG formal leveling:** Evinova/AstraZeneca health-tech culture — the JD reads like a startup engineering values document, not a FAANG rubric. Interview likely focuses on engineering judgment, production experience, and AI fluency.

⚠️ **Gaithersburg MD commute:** ~45-55 min from Arlington VA, 3 days/week. Manageable but not trivial.

⚠️ **Closing tomorrow:** Must submit today.

## Block E — Differentiation (4.5/5)

**Claude Code explicit JD mention** is the single strongest differentiator — the user uses it daily and can speak to it with depth and specificity. Very few candidates can match this signal.

**RAG + MCP combo** — both explicitly listed in the AI/ML infra. Both in the portfolio (LeaseI: TF-IDF RAG + MCP; AgentProbe: ChromaDB RAG). Not common.

**Production ownership story** — Entrata 7yr at 99.5% uptime, owned 20+ modules in production, zero compliance violations. The JD's core value — "you are responsible for your code in production, not just in a pull request" — is the user's lived experience, not a talking point.

**AI fluency narrative** — "AI fluently, not blindly" describes exactly how the user works. Can speak to this with real examples: Claude Code for code gen + architecture review + test gen, evaluating output with AgentProbe eval engine, building HITL guardrails for regulated decisions in LeaseI.

## Block F — Logistics (3.5/5)

- Location: Gaithersburg MD — hybrid 3 days. User in Arlington VA. ~50 min commute. Workable.
- Visa: Unconfirmed. Verify before or during application.
- Compensation: $127K–$167K + equity + bonus. Acceptable.
- Closing: 11-Sept-2026 = TOMORROW. Submit today.
- Process: AstraZeneca/Evinova typically 3-4 rounds (technical screen → coding → system design → team fit). Not FAANG-style LeetCode.

---

## Verdict

**APPLY — 3.8/5.** The Claude Code explicit mention alone makes this worth submitting. FastAPI + Python + React + TypeScript + AWS + RAG + MCP covers most of the stack. The production ownership culture is a genuine fit, not a stretch. Node.js gap is real but the JD explicitly says "we don't expect full coverage." Visa is the key unknown — AstraZeneca's multinational status makes it likely but not confirmed.

**Lead with:** Claude Code daily use (explicit JD call-out) → RAG pipelines + MCP (both LeaseI + AgentProbe, both listed in JD) → production ownership (Entrata 7yr, code owned in production not just PRs) → full-stack (FastAPI/Python backend + React/TypeScript frontend + AWS).

**Don't overclaim:** Node.js (say Python-primary, TypeScript-comfortable); Kubernetes (Docker yes, K8s learning); LangFuse (observability culture yes, LangFuse specifically learning).
