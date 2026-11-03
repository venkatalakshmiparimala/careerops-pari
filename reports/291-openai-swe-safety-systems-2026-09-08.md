# 291 — OpenAI — Software Engineer, Safety Systems

**Date:** 2026-09-08
**Score:** 2.3/5 — SKIP (Tech stack: Terraform, Kubernetes, Kafka, Azure — 4 simultaneous gaps; content safety/abuse domain not in background; OpenAI = FAANG-equivalent interview loop; comp $207K–$385K is exceptional but domain is wrong)
**URL:** https://openai.com/careers
**PDF:** ❌
**Legitimacy:** High Confidence — OpenAI needs no introduction; salary range $207K–$385K disclosed; JD is specific to Safety Systems team; no ghost indicators

---

## Block A — CV Match

**Tech stack is 4-deep in gaps simultaneously (Terraform, Kubernetes, Kafka, Azure). Content safety/abuse domain is the core of the role and is absent from background. Python and ML deployment are the genuine matches. OpenAI softens the tech stack requirement ("we want engineers who understand fundamental problems") — but the domain gap is structural.**

| JD Requirement | CV Proof Point |
|---------------|----------------|
| "Python or modern languages (C++, Rust, Go); quickly ramp on Python" | Python 9yr primary — no ramp needed ✓✓ |
| "Built and run production services in high growth, rapidly scaling environment" | Entrata: 99.5% uptime, 9yr production, multi-tenant SaaS; Docker microservices; RabbitMQ; AWS ✓ |
| "Content safety, fraud, or abuse" | Entrata: HUD income-limit compliance = income fraud detection (falsified paystubs, HUD override detection) — adjacent ✓/⚠️; no direct content moderation or anti-abuse platform experience ✗ |
| "Deployed classifiers or ML models in production" | LeaseI: 8-agent LangGraph classifier routing (93.6% precision); AgentProbe: 5-metric LLM quality engine with CI gate; GMU: PyTorch/scikit-learn (R²=0.977) ✓✓ |
| "Diagnose and remediate active incidents, build tooling for root causes" | Entrata: built debugging tools reducing triage time 40%; sub-10 bug count 6+ months; production incident ownership ✓ |
| "Understand trade-offs of capabilities vs. risks — deploy safely" | LeaseI: staged autonomy with HITL escalation + deterministic guardrails; AgentProbe: regression gate before ship ✓ |
| "Strong project management — self-directed, remove roadblocks" | Solo builds throughout; Magizhs: ambiguous requirements → production in weeks ✓ |
| Infrastructure: Terraform | Not in background ✗ |
| Infrastructure: Kubernetes | Not in background ✗ |
| Infrastructure: Kafka | Not in background ✗ (RabbitMQ is analogous but distinct) |
| Infrastructure: Azure | AWS in background; not Azure ✗ |
| "Architect anti-abuse and content moderation infrastructure" | No content moderation or anti-abuse systems in background ✗✗ |
| "Novel AI techniques to measure, monitor AI models' alignment to human values" | AgentProbe: LLM-as-Judge, correctness/groundedness evaluation — adjacent to alignment measurement ✓/⚠️ |

**Hard Gaps:**
- **Tech stack (Terraform, Kubernetes, Kafka, Azure)** — four simultaneous gaps; OpenAI says they value "understanding fundamental problems" over specific tools, which partially softens this; RabbitMQ → Kafka conceptual transfer is credible; AWS → Azure is learnable; Terraform and K8s are harder without direct experience
- **Content safety / anti-abuse domain** — the core of the role; detecting abuse, content moderation infrastructure, trust & safety platform — specialized domain with its own classifiers, signals, and operational patterns; not in background
- **"Abuse, content moderation infrastructure" architecture** — role requires building the systems that detect bad actors at scale; no direct analogue in background

**ATS baseline:** ~9/20. Python ✓, ML deployment ✓, production services ✓, incident management ✓. Terraform/K8s/Kafka/Azure/content safety all missing.

---

## Block B — North Star Alignment

**FAANG-equivalent interview loop + content safety domain mismatch.** OpenAI is among the most selective companies to interview at — their bar is well above Amazon/Juniper Square, where the rejection pattern already demonstrated the Senior technical screening gap.

The "Software Engineer" title (not "Senior") is a mild positive — the strategy hard-blocks Staff/Senior at formal-leveling companies, and this is a step below that. But OpenAI's bar for any engineering hire is exceptional, and content safety is a specialized domain. The role requires genuine trust & safety expertise (abuse signals, classifier design, incident response for live abuse at scale) that the background doesn't cover.

AgentProbe's alignment evaluation framing is the closest intellectual match — but LLM quality evaluation ≠ content moderation infrastructure in an interview context.

**Score: 1.5/5** (FAANG-equivalent loop; content safety domain gap; not FDE/PropTech archetype)

---

## Block C — Compensation

**Disclosed: $207,000–$385,000.** The widest and highest range evaluated this session. OpenAI's equity is significant (private company — IPO/acquisition path, not liquid now). If this role could be landed, the comp would be exceptional. But comp alone does not make a low-probability application viable.

**Score: 5.0/5**

---

## Block D — Cultural Signals

- AGI safety mission — genuinely important work ✓
- "Pragmatic — know when to build quick fix vs. robust solution" — resonates ✓
- Content safety culture: active incident response, abuse signals, moderation at scale — specialized ops culture ⚠️
- FAANG-equivalent: structured interviews, system design loops, bar-raiser ⚠️
- SF-based (inferred from SFCO and LA County references); likely hybrid/in-person
- H-1B: OpenAI is a confirmed H-1B sponsor ✓

**Score: 3.0/5**

---

## Block E — Red Flags

1. **4 tech stack gaps simultaneously** — Terraform, Kubernetes, Kafka, Azure; each alone is manageable; all four at once in a specialized company's interview is high risk even with OpenAI's "fundamental problems" softening
2. **Content safety/anti-abuse domain** — the entire Safety Systems team purpose; no background in building abuse detection, content moderation classifiers, or trust & safety platforms
3. **OpenAI interview bar** — the most selective non-defense engineering employer evaluating today; the prior rejection pattern at Amazon applies here at higher severity
4. **Private company equity** — $207K–$385K includes equity; OpenAI equity is valuable on paper but illiquid (no public market yet); not an immediate negative but worth noting vs. NYSE-listed C3 AI
5. **Location** — SF in-person/hybrid; relocation from Virginia required

**Adjustment: −0.8**

---

## Block F — Global Score

| Factor | Signal |
|--------|--------|
| CV match | 2.5 — Python ✓✓; ML deployment ✓; production services ✓; AgentProbe adjacent to alignment eval; Terraform/K8s/Kafka/Azure all missing; content safety domain absent |
| North Star | 1.5 — FAANG-equivalent loop; content safety ≠ target archetype; "SWE" title is better than "Senior" but OpenAI bar is still exceptional |
| Comp | 5.0 — $207K–$385K disclosed; OpenAI equity; exceptional ceiling |
| Culture | 3.0 — AGI safety mission ✓; pragmatic culture ✓; content moderation ops culture ⚠️; FAANG loop ⚠️ |
| Red flags | −0.8 — 4 tech stack gaps; content safety domain; OpenAI selective bar; illiquid equity |

**Global: 2.3/5 — SKIP**

> The comp is the most attractive in the pipeline ($207K–$385K, OpenAI equity). But the domain (content safety, anti-abuse, content moderation) is completely outside the background, and the tech stack has 4 gaps simultaneously. OpenAI's engineering bar is the highest of any company evaluated this session — and the prior rejection pattern (Juniper Square, AppFolio, Amazon) suggests the Senior technical screening loop is already a consistent point of failure. OpenAI would be a harder version of that same challenge, in a domain you've never worked in, with a tech stack you'd need to learn from scratch. The comp makes it emotionally tempting; the probability of clearing their bar makes it a poor use of application energy vs. roles where the domain match is genuine.

---

## Block G — Posting Legitimacy

**High Confidence.** OpenAI needs no introduction. Salary range is explicitly disclosed ($207K–$385K). Legal boilerplate (SFCO, LA County ordinances) is consistent with a real California employer. No ghost indicators.

---

## Machine Summary

```yaml
company: OpenAI
role: Software Engineer, Safety Systems
score: 2.3
status: SKIP
date: 2026-09-08
salary_low: 207000
salary_high: 385000
location: San Francisco, CA (hybrid/in-person; relocation required)
remote: unconfirmed
visa: confirmed (OpenAI is a top H-1B sponsor)
proptech_boost: false
h1b_status: confirmed
top_match: Python; ML model deployment; production services; incident management; AgentProbe adjacent to alignment eval; OpenAI H-1B confirmed; comp exceptional
gaps: Content safety/anti-abuse domain absent; Terraform/Kubernetes/Kafka/Azure all missing; FAANG-equivalent loop; OpenAI selectivity; illiquid equity
```
