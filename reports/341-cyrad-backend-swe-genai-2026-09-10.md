# 341 — Cyrad — Backend Software Engineer (GenAI)

**Date:** 2026-09-10
**Score:** 2.8/5 — SKIP (H-1B sponsorship unknown — small startup, no public signal; "high-consequence operational environments" = likely defense/national security = clearance risk; "production GenAI required, not side-project exposure" = portfolio gap; strong technical fit on RAG+eval+agentic if blockers clear)
**URL:** cyrad.io/careers — Backend Software Engineer – GenAI (Arlington, VA or Seattle, WA) — Onsite
**PDF:** ❌
**Legitimacy:** Medium Confidence — Cyrad (cyrad.io, © 2025, Talent@cyrad.io); small startup with active careers page; JD is coherent and specific; company is obscure/pre-public with no traceable funding rounds; compensation ($190K-$240K) is high but plausible for early-stage defense/govtech

---

## Machine Summary

```yaml
company: Cyrad
role: Backend Software Engineer (GenAI)
score: 2.8
status: SKIP
date: 2026-09-10
salary_low: 190000
salary_high: 240000
location: Arlington VA or Seattle WA (onsite, user's preference Arlington VA)
remote: false (onsite)
visa: UNKNOWN — JD silent; small startup (cyrad.io, copyright 2025); no public H-1B sponsorship record; typical early-stage startups often cannot or do not sponsor
proptech_boost: false
h1b_status: unknown_small_startup
target_level: Senior/Staff IC — startup (not FAANG formal leveling); 6yr minimum = accessible
top_match: RAG architectures ✓ (LeaseI + AgentProbe); vector databases ✓ (ChromaDB); LLM integrations ✓ (multi-provider); agentic/tool-calling ✓ (LangGraph 8-agent); evaluation systems ✓ (AgentProbe = exact match — 5-metric engine + CI gate + LLM-as-Judge); production APIs + distributed systems ✓ (FastAPI + Entrata 7yr); 9yr SWE (6yr req ✓); Arlington VA location ✓
gaps: H-1B sponsorship unknown (primary risk); likely defense/national security context = clearance probability; "production GenAI required, not experimental or side-project" = AgentProbe/LeaseI are portfolio-quality (strong but technically portfolio); Kubernetes (preferred); fine-tuning / inference optimization (preferred); Cyrad is obscure with no traceable funding
contact: Talent@cyrad.io
```

---

## Block A — Archetype Fit (4/5)

**Archetype: AI Platform / LLMOps + Applied AI Engineer**

The JD is a near-perfect description of what AgentProbe is: "evaluation and testing infrastructure that measures output quality, surfaces failure modes, and prevents regressions, so that AI behavior can be trusted in settings where mistakes carry consequences." That's the CI regression gate + 5-metric eval engine + LLM-as-Judge harness — built from first principles.

"RAG architectures, vector search, LLM integrations, agentic or tool-calling systems" — all present in the portfolio. "Not prototypes or thin wrappers around third-party models" — AgentProbe and LeaseI are both architecturally substantive.

The "high-consequence operational environments" framing is Cyrad's differentiator. This likely means defense, law enforcement, emergency response, or critical infrastructure — domains where AI mistakes have real-world consequences. The LeaseI HITL guardrails (deterministic logic decides regulated calls, LLM never makes final compliance decisions) maps philosophically to this culture.

Gap: Domain is unknown but likely defense-adjacent. User has no defense/govtech background. The engineering approach is right; the domain context is new.

## Block B — Technical Fit (4/5)

**Confirmed matches:**
- ✅ RAG architectures — LeaseI (TF-IDF RAG, section-aware chunking, citation-backed) + AgentProbe (ChromaDB RAG)
- ✅ Vector databases — ChromaDB (AgentProbe)
- ✅ LLM integrations — multi-provider routing: Anthropic API, OpenAI API, Ollama
- ✅ Agentic/tool-calling systems — LeaseI 8-agent LangGraph StateGraph with conditional routing + tool calls; AgentProbe orchestrator
- ✅ Evaluation and testing systems — AgentProbe is the proof point: 5-metric eval engine (correctness, groundedness, hallucination rate, latency, token efficiency), pass@k multi-trial harness, LLM-as-Judge scoring, CI regression gate blocking regressions before deployment — this is the exact system the JD describes
- ✅ Production APIs — FastAPI 15-endpoint backend (AgentProbe); FastAPI + Uvicorn (LeaseI)
- ✅ Distributed systems / backend — Entrata 7yr: RabbitMQ async processing, idempotency guarantees, PostgreSQL at scale, Docker microservices
- ✅ AWS — S3, EC2, RDS, Glue (Entrata production)
- ✅ 9yr backend SWE (6yr minimum met)
- ✅ "Ownership mentality" — Entrata 7yr production ownership, zero compliance violations

**Preferred gaps:**
- ⚠️ Agentic AI — ✅ (LeaseI 8-agent + AgentProbe) — this preferred is actually met
- ⚠️ Model evaluation — ✅ (AgentProbe) — met
- ❌ Fine-tuning — not in profile
- ❌ Kubernetes — not in profile (Docker ✓)
- ❌ Edge deployment — not in profile
- ❌ Inference optimization — not in profile

**The "production GenAI required, not experimental" risk:** AgentProbe and LeaseI are production-quality portfolio projects — not enterprise-deployed systems. Magizhs (May-Aug 2025) is production but small-scale. Entrata (7yr) is production-grade engineering but pre-GenAI era. A senior interviewer could challenge whether portfolio projects count as "production GenAI." This is a real but manageable gap — the engineering depth is genuine.

## Block C — Compensation (5/5)

$190K–$240K base + equity + sign-on bonus. Best compensation in the current pipeline by a wide margin. For Arlington VA, this is top-of-market for senior/staff IC GenAI engineering. Equity at an early-stage company could be significant upside if Cyrad exits.

## Block D — Risk Flags (2/5)

⚠️ **H-1B sponsorship unknown — primary risk:** Cyrad is a small startup (cyrad.io, copyright 2025). No public funding announcements, no recognizable investor portfolio. Small early-stage startups frequently lack the resources or legal infrastructure to sponsor H-1B. This is not confirmed either way — it's simply unknown.

⚠️ **Likely defense/national security = clearance risk:** "High-consequence operational environments" + stealth company description + Arlington VA tech cluster = high probability of defense or national security work. Many roles in this space require at minimum a Secret clearance. H-1B holders face significant barriers to US security clearances. The JD does NOT state clearance requirement, but the context makes it plausible.

⚠️ **Obscure company:** Cyrad has no traceable public presence (no Crunchbase, no news coverage found in training data). This is not necessarily disqualifying for a young startup, but it increases uncertainty on all fronts: funding runway, team size, culture, visa infrastructure.

✅ **Not FAANG formal leveling:** Startup IC role. Interview likely focuses on technical depth and product judgment, not LeetCode grinding.

✅ **Compensation is genuine signal:** $190K-$240K at a startup that can afford this rate suggests meaningful funding or revenue — even if not public.

## Block E — Differentiation (4.5/5)

If the company sponsors and clearance is not required:

AgentProbe is a direct answer to the JD's core request: "build the evaluation and testing infrastructure that measures output quality, surfaces failure modes, and prevents regressions, so that AI behavior can be trusted in settings where mistakes carry consequences." This is literally what AgentProbe is. The 5-metric eval engine + CI gate + LLM-as-Judge + pass@k harness = exact match.

LeaseI's HITL architecture ("LLM reasons, deterministic logic decides every regulated call") maps to the philosophy of AI in high-consequence environments. This cultural fit is differentiating.

Entrata 7yr production ownership demonstrates the "ownership mentality" the JD specifically names — not a corporate cog, an engineer who owns the system end-to-end.

## Block F — Logistics (3/5)

- Location: Arlington VA onsite — user is in Arlington VA ✓. Zero commute problem.
- Visa: Unknown — must confirm before investing time
- Contact: Talent@cyrad.io — can cold-email to ask about sponsorship
- Process: Startup = likely 2-3 rounds, speed-to-offer faster than enterprise
- Clearance: Unknown — must ask directly

---

## Verdict

**SKIP — 2.8/5.** Not because of technical fit (which is genuinely strong), but because two unknowns need to resolve before this is worth pursuing:

1. **Does Cyrad sponsor H-1B?** — Email Talent@cyrad.io before applying
2. **Is clearance required?** — Ask in the same email

If both answers are favorable: revisit immediately. The technical fit (RAG + eval systems + agentic + production backend) is 4.0+, the compensation is exceptional, and the Arlington VA location is ideal. A 5-line cold email to Talent@cyrad.io resolves both questions faster than submitting a full application into the unknown.

**Suggested cold email to Talent@cyrad.io:**
> Subject: Backend GenAI Role — Quick Clarifying Questions Before Applying
> "I'm very interested in the Backend Software Engineer – GenAI role. Before submitting, I wanted to confirm two things: (1) Does Cyrad sponsor H-1B visas for this position? (2) Does the role require or lead to a security clearance? I have 9 years of backend experience, production RAG and evaluation systems, and am based in Arlington, VA. Happy to share more — just want to confirm fit first."
