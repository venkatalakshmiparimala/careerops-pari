# 292 — Unknown Private Credit Firm — AI Platform Software Engineer

**Date:** 2026-09-08
**Score:** 2.6/5 — SKIP (H-1B hard block: firm explicitly cannot sponsor immigration — application impossible regardless of domain fit; technical match is the strongest in the session outside of C3 AI; $200K–$250K + bonus disclosed; NYC 5d/week relocation required)
**URL:** via recruiter (Matt@Stabilesearch.com, Stabile Search) — direct company URL not disclosed
**PDF:** ❌
**Legitimacy:** Medium-High Confidence — Posted by a named recruiter (Matt Stabile, Stabile Search) with personal email; $10B+ AUM private credit firm description is plausible and specific (50 employees, fourth fund raise, Midtown Manhattan); no direct company URL or name to verify independently; no ghost indicators; salary range disclosed

---

## Block A — CV Match

**Technical alignment is exceptional — this JD describes what AgentProbe and LeaseI already are. RAG infrastructure over documents, agent harnesses, provenance tracking, Claude Code as daily tooling, production AI for non-technical stakeholders — every requirement maps directly to existing proof points. The H-1B hard block makes none of this matter.**

| JD Requirement | CV Proof Point |
|---------------|----------------|
| "Python, TypeScript/JavaScript, Rust, or Go — strong fundamentals" | Python 9yr primary ✓✓; TypeScript (AI on FHIR) ✓; JavaScript ✓ |
| "AI coding tools (Claude Code, Cursor, Codex) as primary development mode" | Claude Code used daily to build LeaseI, AgentProbe, Magizhs; orchestrating parallel tasks, review cycles, deployment ✓✓✓ (named explicitly in JD) |
| "Built AI tools for end users — chatbots or LLM-driven automation of business processes" | Magizhs: agentic AI concept-to-production for external customer; LeaseI: tenant self-service + investment professional-grade document intelligence ✓✓ |
| "Built the platform itself: RAG infrastructure and data ingestion, agent layer" | AgentProbe: multi-provider RAG eval + LLM router + 15-endpoint FastAPI service; LeaseI: hand-rolled TF-IDF RAG (deliberate — no LangChain), ChromaDB in AgentProbe, LangGraph 8-agent pipeline ✓✓✓ |
| "Own and extend production AI systems — investment memo pipeline, DDQ automation, RAG over financial documents" | LeaseI: RAG over lease documents (section-aware chunking, 100% citation correctness); Entrata: HUD income-limit pipeline → 180K domain records powering eligibility decisions ✓✓ (housing compliance ≠ private credit, but the pattern is identical: read authoritative documents, extract structured output, support regulated decisions) |
| "Build provenance tracking, source attribution, review workflows" | LeaseI: 100% citation correctness, 100% grounding on eval set; Phase 3 correctly traces false-ineligibility ticket to misconfigured setting + release tag; deterministic citation with source document reference ✓✓✓ |
| "Build and maintain agent infrastructure: harnesses, skills, subagents, tool integrations" | AgentProbe: 3 LangGraph agents (Orchestrator, RAG Tracer, Auto Fix) with harness and tool routing; LeaseI: 8-agent LangGraph StateGraph with HITL escalation, conditional edges, memory ✓✓✓ |
| "Run projects end to end: design, implementation, deployment, ongoing production support" | LeaseI solo concept-to-production; AgentProbe end-to-end; Entrata 7yr HUD pipeline solo; Magizhs: design → production in weeks ✓✓ |
| "Translate workflows of non-technical stakeholders into tools they will actually rely on" | Entrata: 120+ Agile sprints with product/compliance/operations; Magizhs: stakeholder scoping from ambiguous requirements; GMU: 600+ students; COO-level communication ✓ |
| "Vector databases, document parsing, Anthropic/OpenAI agent SDKs — a plus" | ChromaDB (AgentProbe); OCR (LeaseI document parsing, section-aware chunking); Anthropic API (AgentProbe primary provider); OpenAI API (multi-provider routing) ✓✓ |
| "Financial services or document-heavy, compliance-sensitive domain preferred" | Document-heavy ✓; compliance-sensitive ✓ (HUD, HIPAA, PHI); financial services = housing compliance adjacent (income verification, HUD eligibility calculations) ✓/⚠️ — private credit (underwriting, DDQ, investment memos) is a distinct domain |
| "3–5 years of professional SWE experience; flexibility for exceptional engineer" | 9yr 8mo professional SWE (Jan 2017 → present); JD has explicit flexibility language for exceptional engineers with strong track records ✓ |
| "Legally authorized to work in the US — unable to sponsor immigration" | F-1 STEM OPT → H-1B pathway required; this firm explicitly cannot sponsor now or in the future ✗✗ HARD BLOCK |
| "Finance culture, not startup culture" | Entrata background is startup/growth-stage SaaS; not financial services culture ⚠️ |

**Hard Gaps:**
- **H-1B sponsorship required — firm cannot sponsor** — the single disqualifying fact; explicitly stated as "unable to sponsor or take over sponsorship of an employment visa now or in the future"; cannot be worked around, cannot be disclosed differently in an application, not a risk but an absolute impossibility
- **Private credit domain** — investment underwriting, DDQ structure, investment memo format, credit workflow — entirely distinct from housing compliance; learnable but unfamiliar; customer conversations will involve loan underwriting and fund operations from day one
- **Finance culture** — 50-person private credit firm reporting to COO-level stakeholders; Entrata is startup SaaS; cultural adaptation is possible but real

**ATS baseline:** ~16/20. Python ✓, Claude Code ✓, RAG ✓, LangGraph ✓, agents ✓, document parsing ✓, vector databases ✓, Anthropic API ✓, provenance/attribution ✓, production AI ✓. H-1B block overrides all of it.

---

## Block B — North Star Alignment

**AI Platform / Applied AI Engineer archetype — the exact target. This is what AgentProbe and LeaseI built toward: production RAG infrastructure, agent harnesses, document intelligence for non-technical end users, end-to-end ownership with a small team.** The explicit Claude Code requirement in the JD is a direct signal that this team operates the way the background demonstrates.

The "second engineer to the lead" structure maps well — not a Staff/Senior bar to clear, just a genuine proof point that you can build and ship production AI systems. The flexibility on years ("exceptional engineer with a strong track record of shipping") is a genuine softening of the 3-5 year minimum.

The finance culture and private credit domain are learnable gaps. The provenance tracking, citation correctness, and RAG-over-documents pattern is identical to what LeaseI does — the documents are credit memos and DDQs instead of lease agreements and HUD specs, but the system architecture is the same.

**None of this matters because of the H-1B block.** The application cannot proceed. Even if the score were 5.0/5, the visa constraint is non-negotiable on the firm's side.

**Score: 4.0/5** (strong archetype match; domain and culture learning curves present but manageable; H-1B block treated separately in red flags)

---

## Block C — Compensation

**Disclosed: $200,000–$250,000 base + discretionary bonus + fully paid health/dental/vision premiums including dependents + 401(k) + commuter benefits + PTO.** The fully paid premiums (including dependents) add significant real value beyond the base. Discretionary bonus at a $10B+ AUM private credit firm can be meaningful (finance bonus culture). No equity — private credit firms typically don't offer equity to non-partners. For an AI platform engineer, this is the highest disclosed comp this session after OpenAI.

**Score: 5.0/5**

---

## Block D — Cultural Signals

- "Build tools they will actually rely on" — results-accountable, outcome-focused culture ✓
- Second engineer to the platform builder — direct mentorship, high ownership, no bureaucracy ✓
- 50-person firm, reporting to COO level — high visibility, high trust required ✓
- "No voluntary turnover in five years" — stable, low-churn culture ✓
- Finance culture explicitly called out — "not a startup culture"; Parimala's background is startup SaaS ⚠️
- NYC 5 days/week, summer Fridays WFH only — relocation from Virginia required; no long-term remote ⚠️
- H-1B: explicitly cannot sponsor — hard incompatibility ✗✗

**Score: 3.0/5**

---

## Block E — Red Flags

1. **H-1B cannot sponsor — absolute hard block** — "My client is unable to sponsor or take over sponsorship of an employment visa now or in the future." F-1 STEM OPT → H-1B transition requires employer sponsorship; this firm has made a permanent policy decision not to offer it; this is not a "it depends" — it's categorical; the application cannot proceed
2. **Finance culture, not startup culture** — explicitly called out in the JD as a requirement, not a description; private credit firms have a distinct operational culture (formal hierarchy, investment professional expectations, institutional norms) that differs from housing SaaS
3. **Private credit domain** — investment underwriting, DDQ automation, investment memo generation — specialized financial workflows; not impossible to learn but the platform will be used by investment professionals from day one and domain fluency will be expected fast
4. **NYC 5 days/week** — relocation from Virginia required; no remote path; 5 days/week with summer Fridays only is among the most restrictive in-office requirements in the pipeline
5. **Recruiter-posted, company anonymous** — cannot independently verify the firm, H-1B history, or team size; the $10B+ AUM claim and fourth fund raise are plausible but unverifiable; Stabile Search is a real search firm, which reduces ghost risk

**Adjustment: −1.5** (−1.0 for H-1B absolute block; −0.3 for finance culture + NYC relocation; −0.2 for domain learning curve)

---

## Block F — Global Score

| Factor | Signal |
|--------|--------|
| CV match | 4.5 — Python ✓✓; Claude Code named ✓✓; RAG infra ✓✓; agent harnesses ✓✓; provenance/citation = LeaseI 100% citation correctness ✓✓; document intelligence ✓✓; stakeholder translation ✓; private credit domain ⚠️; H-1B block ✗✗ |
| North Star | 4.0 — AI Platform/Applied AI = primary target archetype; second engineer = right level; "exceptional engineer" flexibility on years ✓; finance culture and domain learnable; H-1B treated in red flags |
| Comp | 5.0 — $200K–$250K base + bonus + fully paid premiums; highest base in pipeline after OpenAI |
| Culture | 3.0 — ownership ✓; stable culture ✓; finance culture ⚠️; NYC 5d/week ⚠️; H-1B absolute incompatibility ✗ |
| Red flags | −1.5 — H-1B cannot sponsor (absolute block); finance culture; NYC relocation; domain gap; anonymous firm |

**Global: 2.6/5 — SKIP**

> The technical match here is the strongest in the session. AgentProbe literally is the platform they're building — RAG infrastructure, agent harnesses, provenance tracking, Claude Code as the development mode. LeaseI's citation correctness and document intelligence is exactly the provenance and review workflow they need. The $200K–$250K base is exceptional. If the visa were solvable, this would be a 4.5/5 APPLY with very strong domain alignment. But the H-1B block is categorical: the firm has made a permanent policy decision not to sponsor immigration now or in the future, and F-1 STEM OPT to H-1B requires employer sponsorship. The application is not risky — it's impossible. Don't apply.

---

## Block G — Posting Legitimacy

**Medium-High Confidence.** Posted by Matt Stabile (Stabile Search) with a personal email (Matt@Stabilesearch.com). Stabile Search is a verifiable executive search firm. The $10B+ AUM private credit firm description is specific and plausible — fourth fund raise, 50 employees, Midtown Manhattan HQ, no voluntary turnover in five years. Salary range disclosed. Recruiter-sourced postings add one layer of indirection (cannot verify the company directly), but the specificity of the JD (second engineer to the platform builder, DDQ automation, investment memo generation) and the firm description argue for a real posting. Low ghost risk.

---

## Machine Summary

```yaml
company: Unknown Private Credit Firm (via Stabile Search / Matt@Stabilesearch.com)
role: AI Platform Software Engineer (second engineer)
score: 2.6
status: SKIP
date: 2026-09-08
salary_low: 200000
salary_high: 250000
location: New York City, NY (5 days/week onsite; summer Fridays WFH only; relocation required)
remote: false
visa: hard_blocked (firm explicitly cannot sponsor now or in the future)
proptech_boost: false
h1b_status: hard_blocked
top_match: RAG infrastructure; agent harnesses; LeaseI provenance/citation correctness = JD provenance tracking; Claude Code named; document intelligence; $200K-$250K + bonus; second engineer seat = right level
gaps: H-1B cannot sponsor (absolute disqualifier); private credit domain (DDQ, investment memos, underwriting); finance culture (not startup); NYC 5d/week relocation; company anonymous via recruiter
```
