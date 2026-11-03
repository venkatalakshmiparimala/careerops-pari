# 481 — Splitero — Applied AI Engineer

**Score:** 4.4/5
**URL:** https://job-boards.greenhouse.io/splitero/jobs/5162723008
**PDF:** ❌
**Legitimacy:** High Confidence
**Archetype:** Applied AI Engineer / PropTech
**Date:** 2026-09-28

---

## Block A — Match with CV

| JD Requirement | Evidence |
|----------------|----------|
| 6+ years SWE, 2+ years production AI/LLM | 8 years SWE at Entrata + 2+ years AI: LeaseI (8-agent LangGraph pipeline, production), AgentProbe (eval engine, multi-provider LLM router), Magizhs (forward deployed AI engineer) |
| LLM APIs, RAG, agentic workflow design | LeaseI: RAG pipeline with citation grounding, 8-agent LangGraph StateGraph, conditional routing; AgentProbe: multi-provider LLM router (OpenAI/Anthropic/Groq/Ollama) |
| Evaluation frameworks for LLM outputs | AgentProbe: 5-metric eval engine (correctness, groundedness, latency, token efficiency, hallucination rate), CI-integrated regression gate, golden datasets — built *from scratch* |
| Vector databases, embedding pipelines | ChromaDB (AgentProbe), embedding pipelines in both projects |
| Multi-agent frameworks (LangChain, LlamaIndex) | LangChain + LangGraph production use |
| Python, TypeScript/Node.js, PostgreSQL, AWS | All confirmed in cv.md + 8 years production |
| Self-directed, "team of one" | Built LeaseI + AgentProbe entirely solo — no PM, no roadmap, shipped to 1,240 test case eval |
| Translate AI concepts for non-technical stakeholders | Entrata: primary technical translator for enterprise customers; GMU: workshops for 600+ students |
| Operationalizing AI tooling | Magizhs: embedded with operations teams, deployed into production; AgentProbe: used to evaluate LeaseI across 1,240+ cases |
| Fintech/PropTech preferred | Entrata = 8 years housing tech (multifamily + affordable housing). Splitero = home equity real estate fintech. Domain gap is mortgage lending specifically, not housing broadly. |
| SOC 2 / data privacy preferred | 100% PHI compliance on AWS S3 migration (Entrata); HIPAA-compliant RBAC in AI on FHIR |

**Gap:** CGA/ALM systems — unfamiliar domain-specific lending tools. Mitigated: role frames this as "from 0 to 1," meaning building from scratch. Also: n8n/Make/Zapier not in background — gap on low-code orchestration tools.

**Score: 4.2**

---

## Block B — North Star Alignment

- **Archetype:** "Applied AI Engineer" + "PropTech AI Engineer" = both primary targets in _profile.md
- **"Applied AI Engineer" framing:** This role is exactly the archetype — AI discovery + delivery embedded in a product/operations org, building on top of AI platforms, not GPU infra. LeaseI + AgentProbe are the exact proof points.
- **Solo ownership:** JD says "team of one, run your own backlog, don't need a fully defined spec" — Parimala built LeaseI + AgentProbe 100% solo. No one else applying walks in with that proof.
- **Cross-functional embedding:** "Embed within operations and business teams" — Entrata + Magizhs both demonstrate this pattern exactly.
- **PropTech + real estate fintech:** Preferred experience is "fintech, proptech, or real estate technology" — 8 years at Entrata is exactly this. The preferred bar is already cleared.

**Score: 4.5**

---

## Block C — Comp

- **Base:** $135,000 – $175,000 (no variable mentioned; startup equity likely)
- Comp floor removed (2026-07-30 strategy shift). Range is below senior market but appropriate for this company size/stage.
- Remote first = no relocation cost; WeWork access + stipends.
- Equity upside at early-stage startup.

**Score: 3.8**

---

## Block D — Cultural Signals

- Fully remote ✅
- "OneTeam" culture, transparency, doing the right thing — signals
- Real mission: helping homeowners access home equity trapped by rising rates — not just "disrupting fintech"
- Reports to VP of Product and Engineering — high visibility, cross-functional charter
- Small team vibe (co-founders directly present in JD) — autonomy + ownership aligned with Parimala's work style
- Real estate equity is a regulated domain — overlaps with Entrata's affordable housing compliance expertise

**Score: 4.0**

---

## Block E — Red Flags

- **CGA/ALM gap:** Specific lending tools unfamiliar. Mitigated by "from 0 to 1" framing and domain-adjacent (housing/real estate) background.
- **n8n/Make/Zapier gap:** Not in background. Low-code orchestration tools are learnable; LangGraph orchestration covers the underlying skill.
- **Company size + funding stage:** No large funding round disclosed; startup stage = higher risk than established scale-up.
- **$135-175K is below senior market:** Acceptable with floor removed.

**Score: −0.3**

---

## Block F — Global Score

| Dimension | Score |
|-----------|-------|
| Match with CV | 4.2 |
| North Star Alignment | 4.5 |
| Comp | 3.8 |
| Cultural | 4.0 |
| Red Flags | −0.3 |

**Global: 4.4/5** — PropTech domain (apply at 4.0+); strong Applied AI + PropTech archetype match. Lead with LeaseI + AgentProbe as solo-built production AI proof points. The "team of one, no spec needed" requirement is Parimala's exact work style.

---

## Block G — Posting Legitimacy

- Splitero is a funded real estate fintech startup (home equity sharing)
- Greenhouse ATS, active posting with compensation range disclosed
- Co-founders named in JD (Gifford + Zvaifler), LinkedIn-verifiable
- No sponsorship statement = assume US citizens/GC only; verify before applying

**Legitimacy: High Confidence**

---

## STAR Stories to Prepare

**"Tell us about a time you built an AI solution from scratch without a defined spec."**
> LeaseI. I identified the problem myself — housing compliance operations teams drowning in multi-system investigation work — framed the use case, defined the architecture (8-agent LangGraph pipeline across Triage → Retrieval → Configuration → Historical → Structured Data → Reasoning → Validation → HITL), built it solo, and measured outcomes (93.6% precision on 1,240 test cases). No PM, no roadmap. Same way I'd run an AI initiative at Splitero: problem first, architecture second, ship and measure.

**"How do you figure out where AI creates leverage in a business?"**
> At Magizhs, I embedded directly with operations teams before touching a line of code. Led discovery workshops to map every manual workflow step, asked where decisions were being delayed or repeated, and triaged those into AI candidates by ROI and feasibility. Same process at Entrata where I translated recurring customer implementation patterns into product features. That's the AI Discovery & Strategy part of this role — I've done it in production.

**"Walk us through your AI evaluation approach."**
> I built AgentProbe specifically because the eval problem was unsolved for LeaseI. Five metrics: correctness, groundedness, latency, token efficiency, hallucination rate. CI-integrated regression gate with golden datasets. Multi-provider LLM router so I could compare outputs across OpenAI/Anthropic/Groq. Used it to validate LeaseI across 1,240+ test cases. The same toolkit I'd bring to evaluate every AI workflow at Splitero before it goes to production.

---

## ATS Keywords

JD terms to confirm in CV: LLM APIs, prompt engineering, RAG, agentic workflow, multi-agent, LangChain, vector database, embedding pipelines, evaluation framework, Python, TypeScript, Node.js, PostgreSQL, AWS, cross-functional, production AI, proptech, real estate, self-directed, workflow automation.

---

## Machine Summary

```yaml
id: 481
company: Splitero
role: Applied AI Engineer
score: 4.4
archetype: Applied AI Engineer / PropTech
domain: Real Estate Fintech / PropTech
location: Remote US
comp_range: "$135,000-$175,000"
legitimacy: High Confidence
recommendation: Apply — PropTech domain match; solo AI builder proof points (LeaseI + AgentProbe) directly match "team of one" requirement
key_risk: CGA/ALM lending tools gap; n8n/Make not in background; company stage/size unclear
date: 2026-09-28
```
