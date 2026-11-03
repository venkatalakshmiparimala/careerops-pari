# 345 — RealPage — AI Developer IV (Internal AI CoE)

**Date:** 2026-09-15
**Score:** 4.2/5 — APPLY (PropTech boost; multifamily SaaS = direct Entrata domain overlap; LangGraph + evaluation frameworks + Playwright explicitly listed in nice-to-haves = AgentProbe is literally the answer; regulated compliance domain ✓; Python + TypeScript ✓; AWS + GCP ✓; remote unconfirmed but large company; PE-backed = cost risk)
**URL:** RealPage Careers — AI Developer IV (Internal AI Center of Excellence)
**PDF:** ✅ `output/345-realpage-ai-developer-iv-2026-09-15.pdf`
**Legitimacy:** High Confidence — RealPage (largest PropTech/multifamily SaaS, Thoma Bravo PE, $10.2B acquisition 2021; Internal AI CoE role consistent with enterprise AI adoption wave)

---

## Machine Summary

```yaml
company: RealPage
role: AI Developer IV — Internal AI Center of Excellence
score: 4.2
status: Applied
date: 2026-09-15
salary_low: unspecified
salary_high: unspecified
location: unspecified (likely remote or Richardson TX HQ)
remote: unconfirmed — JD silent on location; large company supports remote
visa: LIKELY_SPONSORS — RealPage is large enterprise ($10.2B, 5,000+ employees); H-1B infrastructure standard at this scale; not explicitly confirmed
proptech_boost: true (multifamily property management SaaS = exact Entrata domain; +0.3 applied)
h1b_status: likely_sponsors_large_company
target_level: Senior IC — "AI Developer IV" = Level 4 individual contributor; 6+ years required; not Staff/Lead/Principal
top_match: LangGraph explicitly listed (nice-to-have) ✓; Evaluation frameworks explicitly listed (nice-to-have = AgentProbe) ✓; Playwright explicitly listed (nice-to-have) ✓; RAG ✓; Vector databases (ChromaDB) ✓; Agent orchestration ✓; Python 9yr ✓; TypeScript ✓; AWS + GCP ✓; PropTech domain (8yr Entrata = same customer base) ✓; Regulated compliance data ✓; AI coding tools (Claude Code) ✓; Engineering enablement (GMU 600+ students, Entrata 5+ engineers) ✓
gaps: Azure (listed first in cloud requirements; AWS + GCP cover the requirement but Azure not in profile); Internal developer platform experience (soft gap — AgentProbe is close); AI adoption program leadership (partial — GMU mentoring is adjacent); PE-backed company risk
```

---

## Block A — Archetype Fit (4.5/5)

**Archetype: AI Platform / LLMOps + Agentic / Automation**

The Internal AI Center of Excellence role is asking for someone who builds reusable AI tools, patterns, and evaluation infrastructure for engineering teams — and then enables those teams to adopt them. This maps to the exact combination of what you've built:

- **AgentProbe** = their evaluation framework need, embodied. The JD explicitly calls out "Evaluation frameworks such as OpenAI Evals, LangSmith Evals, RAGAS, or custom evaluation harnesses" as a nice-to-have. AgentProbe is a custom evaluation harness with CI-integrated regression gates, LLM-as-Judge scoring, and pass@k multi-trial sampling — built to evaluate production AI systems like LeaseI. You didn't use someone else's framework; you built one.
- **LeaseI** = production agentic workflow in a regulated domain (PropTech compliance). The JD wants someone who can "help engineering teams move from experimentation to repeatable production use" — LeaseI is exactly that: 8-agent LangGraph pipeline that went from hypothesis to 93.6% precision in production testing.
- **Entrata enablement angle** = 7 years at a multifamily SaaS company that is RealPage's closest direct competitor, building internal debugging tools (40% triage time reduction), automating 80% of manual workflows, mentoring 5+ engineers, running 300+ code reviews. The GMU TA role (600+ students) reinforces the enablement dimension.

PropTech domain is a direct match. RealPage and Entrata serve the same NMHC Top 50 operators. The affordable housing compliance, lease management, and property data workflows you owned at Entrata are the exact domain RealPage's platform covers.

**One nuance:** This is an internal-facing role (AI CoE, developer productivity) rather than a product-facing role. That means the stakeholders are engineers and engineering leaders, not end customers. That's actually well-suited to your profile — you've been an internal enabler (tools, mentoring, automation) at Entrata for 7 years.

## Block B — Technical Fit (4.5/5)

**Required — Confirmed matches:**
- ✅ Python 9yr — primary stack throughout
- ✅ TypeScript/JavaScript — Entrata, AgentProbe frontend, AI on FHIR
- ✅ LLM-based application development — LeaseI, AgentProbe (multi-provider: Anthropic, OpenAI, Groq, Ollama)
- ✅ Prompt engineering — enforced in code across LeaseI decision boundaries; few-shot, chain-of-thought, output validation
- ✅ Tool calling / function calling — LangGraph tool calls in both LeaseI and AgentProbe
- ✅ RAG architectures — LeaseI (hand-rolled TF-IDF RAG, section-aware chunking), AgentProbe (ChromaDB semantic retrieval)
- ✅ Vector databases / semantic retrieval — ChromaDB in AgentProbe
- ✅ Multi-step workflow / agent orchestration — LangGraph 8-agent pipeline (LeaseI), LangGraph orchestration (AgentProbe)
- ✅ CI/CD — GitHub Actions (AgentProbe regression gate, Entrata pipelines)
- ✅ Git-based development — throughout
- ✅ Automated testing — CI-integrated eval gate blocking quality regressions (AgentProbe)
- ✅ API design — 15-endpoint FastAPI backend (AgentProbe), FastAPI (LeaseI)
- ✅ Observability and logging — structured logging + monitoring at Entrata; agent tracing in AgentProbe
- ✅ AI coding tools — Claude Code (daily workflow), AI-assisted development
- ✅ AWS (S3, EC2, RDS, Glue, Lambda) — 7yr Entrata + GCP Cloud Storage

**Nice-to-haves — Matched:**
- ✅ LangGraph — explicitly listed; used in both LeaseI (8-agent) and AgentProbe (3-agent)
- ✅ Evaluation frameworks — AgentProbe IS the answer (custom eval harness, not vendor-dependent)
- ✅ Playwright — explicitly listed; used in career-ops PDF generation and testing workflows
- ✅ Privacy / compliance / regulated-data — HUD/LIHTC (7yr, zero violations), HIPAA (AI on FHIR)
- ✅ PropTech domain — 8yr Entrata (direct RealPage competitor, same customer base)
- ✅ AI adoption / enablement — GMU TA (600+ students, Python/SQL/distributed systems), Entrata mentoring (5+ engineers)
- ✅ Knowledge management / enterprise search — RAG over regulatory document corpus (LeaseI TF-IDF retrieval)

**Gaps:**
- ⚠️ Azure — listed first in cloud requirements ("Azure, GCP, or AWS" — listed in that order). AWS ✓ + GCP ✓ covers the requirement, but Azure is not in profile. Most CoE work in a mixed enterprise will touch Azure tooling (Azure OpenAI Service is the dominant enterprise LLM deployment). Not a blocker — "or similar" language confirms AWS/GCP qualify — but worth acknowledging.
- ⚠️ Internal developer platform experience — they specifically want someone who's built "internal developer platforms, engineering productivity tools, or enablement frameworks." AgentProbe is close (open-source toolkit, reusable patterns), but it's not a corporate internal platform. Entrata debugging tools + automation pipelines provide supporting evidence.
- ⚠️ OpenAI Agents SDK / Google ADK / Semantic Kernel / CrewAI — other agent frameworks listed as nice-to-haves; LangGraph ✓ covers the category but not the specific named frameworks.

## Block C — Compensation (3.0/5)

No salary disclosed. RealPage is PE-backed (Thoma Bravo) — compensation culture in PE companies trends conservative compared to venture-backed startups. At a large company, AI Developer IV likely falls in the $130K–$160K range depending on location (Richardson TX HQ vs remote vs major market). No equity component (PE-owned, not publicly traded — employee equity is limited). Benefits are standard enterprise. The role compensates in career capital (building internal AI infrastructure at one of the largest PropTech companies), not in equity upside.

## Block D — Risk Flags (3.0/5)

⚠️ **PE-backed (Thoma Bravo):** Thoma Bravo is a large PE firm known for cost optimization post-acquisition. RealPage was acquired in 2021 for $10.2B. Internal CoE roles at PE-backed companies carry higher layoff/restructuring risk than at venture-backed or public companies. If cost-cutting happens, internal tooling teams are often in scope.

⚠️ **DOJ Antitrust Lawsuit (Oct 2024):** The Department of Justice filed an antitrust lawsuit against RealPage for their YieldStar revenue management algorithm, alleging it facilitated rent collusion among landlords. The case is ongoing. This creates legal/PR uncertainty around the company and may affect hiring pace, culture, and long-term stability. Not a hard block, but worth researching the current status before accepting an offer.

⚠️ **Internal CoE role visibility:** Building internal tools is valuable engineering work, but these roles can become invisible in large organizations. Career progression in a CoE depends heavily on executive sponsorship and whether the AI adoption mandate is real or aspirational.

✅ **Large company = likely sponsors H-1B:** 5,000+ employees, established legal infrastructure, enterprise hiring at scale. Likely sponsors but not confirmed.

✅ **PropTech domain is exactly your background:** RealPage serves the same operators you built software for at Entrata. Domain onboarding is near-zero.

## Block E — Differentiation (4.5/5)

**AgentProbe is the answer to their explicit requirement.** The JD lists "Evaluation frameworks such as OpenAI Evals, LangSmith Evals, RAGAS, or custom evaluation harnesses" as a nice-to-have. AgentProbe is a custom evaluation harness — not a configuration of someone else's tool. You built it to solve a real production problem (evaluating LeaseI across 1,240 compliance test cases). The CI-integrated regression gate, LLM-as-Judge with pass@k sampling, and 5-metric quality engine are exactly the "practical evaluation and governance practices" the JD describes as a core responsibility.

**LangGraph is explicitly listed** in their nice-to-haves. You've used it in production in two systems (8-agent LeaseI pipeline, AgentProbe orchestration). This is not familiarity — it's production experience.

**PropTech domain is rare in AI candidates.** Most AI/LLM engineers applying to this role will have financial, healthcare, or tech-generic backgrounds. You have 8 years of hands-on domain knowledge in exactly the business domain RealPage operates in. You know lease compliance, HUD income limits, affordable housing eligibility, tenant workflows. This translates directly to the AI use cases RealPage needs internally.

**Enablement experience is genuine.** 600+ students mentored at GMU, 5+ engineers at Entrata, internal debugging tools built and deployed — the "working directly with engineering teams to help them adopt AI" responsibility is not a stretch for you; it's what you've been doing.

## Block F — Logistics (3.5/5)

- Location: Unspecified — RealPage HQ is Richardson TX; large enterprise supports remote engineering; JD does not restrict location
- Visa: Large company, likely sponsors H-1B — worth confirming during recruiting process
- Equity: PE-backed = minimal equity; compensation is salary + benefits
- PE risk: Thoma Bravo cost optimization culture is real; confirm team stability and CoE budget during interviews
- Process: Large enterprise likely 4–5 rounds (technical screen + system design + behavioral + portfolio review)

---

## Verdict

**APPLY — 4.2/5.** LangGraph, evaluation frameworks, and Playwright are all explicitly named in the nice-to-haves — AgentProbe directly answers all three. PropTech domain overlap with Entrata is a genuine differentiator. Python + TypeScript + AWS/GCP covers the required stack. Azure is a gap worth addressing (can reference familiarity with Azure OpenAI Service conceptually). The DOJ lawsuit and PE-backed risk are real concerns to research — but they affect offer evaluation, not application decision.
