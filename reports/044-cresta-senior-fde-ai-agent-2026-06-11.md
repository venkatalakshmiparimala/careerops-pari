# Evaluation: Cresta — Senior Forward Deployed Engineer (AI Agent)

**Date:** 2026-06-11
**URL:** https://job-boards.greenhouse.io/cresta/jobs/4759347008
**Archetype:** AI Platform / LLMOps (FDE)
**Score:** 3.6/5
**Legitimacy:** High Confidence
**PDF:** output/cv-cresta-senior-fde-ai-agent-2026-06-11.pdf

---

## A) Role Summary

| Field | Detail |
|-------|--------|
| Archetype | AI Platform / LLMOps — Forward Deployed Engineer |
| Domain | AI agents for contact centers, LLM-powered coaching, enterprise customer deployment |
| Function | Build + Customer-Facing (technical advisor, demos, implementation plans) |
| Seniority | Senior IC (3+ years SWE/consulting/AI-ML) |
| Remote | Remote US |
| Comp | $185K–$235K base + annual bonus + equity |
| TL;DR | Build, optimize, and deploy AI agents on Cresta's platform at enterprise customer sites. Gather requirements, run demos, create implementation plans, serve as technical advisor. Part engineering, part solutions engineering — strong customer-facing component. |

---

## B) Match with CV

| JD Requirement | CV Match | Strength |
|----------------|----------|----------|
| Python proficiency | 8+ years production Python at Entrata + AgentProbe FastAPI | ✅ Exceeds |
| AI agent frameworks, function calling, RAG | AgentProbe: 3 LangGraph agents, custom tool calls, end-to-end RAG + ChromaDB | ✅ Direct proof |
| LLM hands-on experience | AgentProbe: Anthropic, OpenAI, Groq, Ollama multi-provider | ✅ Direct proof |
| Cloud platforms (AWS/GCP/Azure) | AWS (S3, EC2, RDS, Glue) + Azure at Entrata; AgentProbe Azure-compatible | ✅ Strong |
| CI/CD, containerization, monitoring | Docker + GitHub Actions CI/CD + observability dashboard in AgentProbe | ✅ Strong |
| API, webhook, data pipeline integration | 15-endpoint FastAPI + 1M+ record pipelines at Entrata | ✅ Strong |
| Golang proficiency | Not in CV — no Go experience | ⚠️ Real gap |
| Customer-facing: demos, requirements, implementation plans | No enterprise customer-facing experience | ⚠️ Real gap |
| 3+ years SWE/consulting/AI-ML | 8+ years SWE + 2 years focused AI/ML | ✅ Exceeds |
| Cross-functional (PMs, ML engineers) | 120+ Agile sprints across Product/Engineering/QA at Entrata | ✅ Strong |
| Contact center / conversational AI domain | No contact center background | ⚠️ Domain gap |

**Gaps and mitigations:**
- **Golang** — Listed as required alongside Python. Parimala has no Go. Mitigate: frame Python as primary language for agent development; acknowledge Go as a ramp item; AgentProbe is all Python which is where the agent logic lives.
- **Customer-facing** — FDE is 50% technical advisor, not just builder. No enterprise consulting or pre/post-sales experience. Mitigate: AgentProbe as an open-source tool (user-facing documentation, external API, community feedback = same discipline) + TA at GMU (translating complexity for non-technical audiences).
- **Contact center domain** — Cresta's entire product is built around contact centers and agent coaching. Not a background Parimala has. Mitigate: domain ramp, but the AI agent architecture is transferable.

---

## C) Level and Strategy

**Level detected:** Senior IC with FDE profile. 3+ years is a low bar — Parimala exceeds it easily. The role is calibrated for someone technically deep on AI agents who can also face enterprise customers.

**Sell plan:**
- Lead with AgentProbe as proof of the exact technical stack: *"I've built the architecture this role deploys: LangGraph agents, RAG end-to-end, function calling, production FastAPI serving, multi-provider LLM routing. I'm not learning this on the job — I've shipped it."*
- Reframe the customer-facing gap: *"I built AgentProbe as a public open-source tool. Writing documentation, designing APIs for external consumption, and getting user feedback is the same discipline as customer-facing deployment."*
- Comp target: $185K floor, push toward $210K+ given AI depth exceeds the 3yr requirement.
- **Flag Go early** — in recruiter screen: *"Python is my primary language. I see Go in the JD — is that required for the agent development layer, or is it primarily for platform/backend team?"* If it's platform-only, Python suffices for FDE agent work.

**H-1B:** Cresta is a $1.6B Series C company — well-funded AI startup with global hiring. Likely sponsors but verify in first call.

---

## D) Comp and Demand

| Source | Range | Notes |
|--------|-------|-------|
| Job posting | $185K–$235K base | Disclosed — strong transparency |
| Equity + bonus | Not quantified | Series C startup — meaningful upside |
| Market | $180K–$250K for Sr FDE at AI-focused Series C | Competitive |

**Assessment:** $185-235K is strong. Top of range ($220-235K) is achievable given Python/agents depth exceeds the baseline requirement. Contact center is a domain ramp but the AI/agent skills are the hard part — those transfer.

---

## E) Customization Plan

| # | Section | Current | Proposed change | Why |
|---|---------|---------|-----------------|-----|
| 1 | Summary | Fraud ML (Signifyd) | Lead: *"Forward deployed AI engineer — built production LangGraph agents, RAG pipelines, and multi-provider LLM systems; deployed AgentProbe as a public tool with external API, documentation, and user adoption"* | JD: build agents + deploy at customer sites |
| 2 | AgentProbe | General | Emphasize: agent architecture (plan-execute-react), function calling, multi-provider routing, public API + documentation, external adoption | FDE pillars: agent development + customer-facing technical delivery |
| 3 | Competencies | Fraud ML | Replace with: AI Agent Architecture, LangChain/LangGraph, RAG End-to-End, Function Calling, Enterprise API Integration, Customer-Facing Technical Delivery | JD vocabulary |
| 4 | Entrata | General | Add: API/webhook integration, cross-functional with Product + Engineering, 100K+ user production systems | JD: integration expertise + cross-functional |

---

## F) Interview Plan

| # | JD Requirement | Story | Key Points |
|---|----------------|-------|------------|
| 1 | Build AI agents with function calling + RAG | AgentProbe: Orchestrator + RAG Tracer + Auto Fix | LangGraph architecture, tool call routing, retrieval evaluation, failure attribution |
| 2 | Integrate with external systems (APIs, databases, CRMs) | AgentProbe: FastAPI + ChromaDB + multi-provider; Entrata: 20+ integrations | API design, webhook patterns, async pipelines |
| 3 | Gather technical requirements + implementation plans | GMU TA + AgentProbe open-source user feedback | Translate business need → technical spec → delivery plan |
| 4 | Customer demos + technical advising | AgentProbe: documented public tool with README, API docs, React dashboard | "I've built tools for external users — the discipline is the same" |
| 5 | Influence product roadmap from deployment insights | AgentProbe: automated eval detects failure patterns → informed architecture decisions | Closed feedback loop: deployment signal → product direction |

**Red flag questions:**
- *"No Go in your CV"* → *"Python is my primary language for agent work — all of AgentProbe's agent layer is Python. Is Go required for the agent development layer or primarily for platform/infra? Happy to ramp on Go — it's a syntax ramp, not a systems programming gap."*
- *"No contact center experience"* → *"The AI agent architecture — planning, tool calling, RAG, failure recovery — is domain-agnostic. I've built it for LLM testing; applying it to contact center workflows is a domain ramp, not a skills gap."*
- *"No enterprise customer-facing experience"* → *"AgentProbe is a public tool: external API, documentation, community. That's the same discipline — designing for users outside your team, handling feedback, iterating on real usage."*

---

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|--------|---------|--------|
| Salary disclosed | $185K–$235K — rare and positive | Positive |
| JD specificity | Named tech stack (Go, Python, LLM, RAG, function calling), real responsibilities | Positive |
| Company health | Series C ~$1.6B valuation; active enterprise product | Positive |
| Remote US | Confirmed | Positive |
| H-1B | Well-funded Series C — likely sponsors; verify | ⚠️ Confirm |

---

## Keywords Extracted

forward deployed engineer, AI agent, LangChain, LangGraph, RAG, function calling, python, golang, enterprise AI, contact center AI, cresta, llm, cloud, aws, ci/cd, remote us

---

## Machine Summary

```yaml
report_num: 044
company: Cresta
role: Senior Forward Deployed Engineer (AI Agent)
date: 2026-06-11
score: 3.6
archetype: AI Platform / LLMOps
legitimacy: High Confidence
location: Remote US
comp_range: "$185K–$235K base + bonus + equity"
visa_risk: medium (well-funded Series C, likely sponsors H-1B — verify)
key_gaps:
  - Golang (required alongside Python — clarify scope in recruiter call)
  - Customer-facing / FDE enterprise experience (real gap — mitigatable)
  - Contact center domain (domain ramp, not skills gap)
key_strengths:
  - AgentProbe = direct proof of LangGraph, RAG, function calling, multi-provider LLM
  - Python 8+ years production
  - API/webhook/pipeline integration (Entrata + AgentProbe)
  - Comp is excellent ($185-235K)
  - Remote US
location_risk: low — remote US
recommend: apply — AI agent stack is a near-perfect match; clarify Go scope + H-1B in recruiter screen
```
