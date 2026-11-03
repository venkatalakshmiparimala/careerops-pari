# Evaluation: American Express — AI Engineer (Agentic AI)

**Date:** 2026-08-04
**URL:** via paste (no public URL provided)
**Archetype:** Agentic AI Engineer / AI Platform — LLM-powered features + RAG + eval in financial services
**Score:** 3.8/5
**Legitimacy:** High Confidence
**PDF:** ❌

---

## A) Role Summary

| Dimension | Detail |
|-----------|--------|
| **Archetype** | Agentic AI Engineer — build LLM-powered features, RAG pipelines over financial data, eval/monitoring tooling, production AI ops |
| **Domain** | Financial services — enterprise agentic AI at scale, compliance-grade correctness and safety required |
| **Function** | Build — contribute to agentic workflows, RAG infrastructure, shared LLM services, production monitoring |
| **Seniority** | Mid-level (4+ years; JD language: "contribute to", "help implement", "participate in" — explicit contributor framing) |
| **Location** | Not stated — Amex Tech hubs in NYC and Phoenix AZ; hybrid policy varies by team; must confirm at screen |
| **H-1B** | High confidence — American Express is a top-20 US H-1B sponsor; consistently files 500–1,000+ H-1B petitions annually; one of the safest sponsors available |
| **Comp** | Not disclosed — Amex AI Engineer market range ~$120–155K (NYC), $115–145K (Phoenix); bonus + deferred comp |
| **Stage** | Public (NYSE: AXP) — 175-year-old enterprise, ~70K employees |
| **Interview** | Likely 4–5 rounds (recruiter screen, coding, system design, AI-specific, behavioral) — large enterprise process |
| **TL;DR** | Strong agentic AI + regulated domain match; Python primary; real infra gaps (Go, Kubernetes, Kafka, gRPC); large company = multi-round loop conflicts with 2-round preference. Score 3.8 — below 4.5 non-PropTech threshold. H-1B certainty is the decisive strategic argument for applying anyway. |

---

## B) Match with CV

| JD Requirement | CV Evidence | Strength |
|----------------|-------------|----------|
| LLM-powered agentic features | LeaseI 8-agent LangGraph; AgentProbe 3-agent LangGraph runtime | Strong |
| Agentic workflows: reason over context, call tools, perform actions | LeaseI conditional routing + tool use; AgentProbe Orchestrator + Auto Fix agents | Strong |
| RAG over financial/regulated data — correctness + safety | LeaseI TF-IDF RAG over lease/compliance docs; 100% citation correctness, 0 safety violations | **Direct proof point** |
| LLM eval + monitoring tooling | AgentProbe CI-integrated 5-metric LLM-as-judge eval; per-run metrics, drift tracking | **Direct proof point** |
| Production AI systems: monitor, debug, improve reliability | Entrata first AI pipeline 1.6M records with quality gates; AgentProbe GitHub Actions CI | Strong |
| Regulated/compliance environment | 8yr Entrata — LIHTC, HUD, HAP, AMI, Section 8/HCV — federal housing compliance, zero violations | Strong |
| Python | Primary language, 8+ years production | Strong |
| AI-assisted development tools | Claude Code daily use | Strong |
| Fintech/regulated environment (preferred) | Entrata is PropTech with federal compliance depth (not banking, but close regulatory analogue) | Partial |
| Open-source contributions (preferred) | AgentProbe live on GitHub | Direct proof point |
| 4+ years engineering | 8+ years | Exceeds |
| TypeScript | AgentProbe + projects | Medium |
| AWS | Entrata production (S3, EC2, RDS, Glue) | Strong |
| **Go** | Not in stack | **Gap** |
| **Kubernetes** | Not in stack | **Gap** |
| **Kafka / event-driven architectures** | RabbitMQ at Entrata (adjacent); no Kafka directly | **Gap** |
| **gRPC** | Not in stack | **Gap** |
| GCP | Not in stack | Gap |

**Domain note:** The JD emphasis on "correctness and safety" for RAG over financial data maps exactly to LeaseI's core design rule — LLM reasons, deterministic logic makes every regulated call, 0% unsupported-claim rate, 100% citation correctness. This is the strongest angle for this application.

---

## C) Level and Strategy

**Score: 3.8/5 — Below threshold (4.5+ for non-PropTech)**

**Strategic case for applying anyway:**

American Express is one of the most reliable H-1B sponsors in the US — 500–1,000+ petitions per year, strong legal infrastructure, track record of cap-subject lottery wins. For a candidate on STEM OPT with the H-1B transition as the primary constraint, this matters more than the score.

**Lead with the regulated domain + RAG safety angle:**
> "I spent 8 years building federal compliance systems at Entrata — LIHTC, HUD, HAP, AMI — where correctness wasn't a goal, it was a legal requirement. LeaseI is an RAG platform I built from scratch for exactly this constraint: LLM reasons over lease documents, deterministic logic or a human makes every regulated eligibility call, and every answer is cited to an exact source clause. When Amex says 'RAG over financial data with an emphasis on correctness and safety,' I understand that design pattern from the inside."

**Lead the eval angle second:**
> "AgentProbe is my CI-integrated eval platform — 5-metric LLM-as-judge scoring on every commit, regressions blocked before merge. I've owned the eval suite end-to-end."

**Address infra gaps honestly:**
> "My enterprise infra stack is AWS + Docker + RabbitMQ. I haven't run Kubernetes or Kafka at production scale, but I've built distributed, event-driven systems — RabbitMQ at Entrata, async pipelines across services. I'd ramp on K8s and Kafka fast in a team context."

**Interview loop warning:** Amex is a large enterprise — expect 4–5 rounds. This conflicts with the 2-round preference from strategy. Apply with awareness that the process will be long.

---

## D) Comp and Demand

| Item | Data |
|------|------|
| Disclosed salary | Not disclosed |
| Market range | ~$120–155K (NYC) / $115–145K (Phoenix) for AI Engineer |
| Bonus | Corporate performance bonus (Amex standard) |
| Equity | No traditional equity — deferred cash comp programs |
| H-1B | High confidence — top-20 US sponsor, 500–1,000+ petitions/year |
| Location | Unconfirmed — NYC or Phoenix likely; must verify at screen |
| Interview | ~4–5 rounds (large enterprise) |
| Comp score | 3.5/5 — undisclosed at large company; likely competitive but no equity upside |

---

## E) Customization Plan

| # | Section | Current | Proposed | Why |
|---|---------|---------|---------|-----|
| 1 | Summary | General agentic AI | Lead: "8 years in federal compliance systems (LIHTC, HUD, AMI) where correctness is a legal requirement; LeaseI RAG with 100% citation correctness and 0 safety violations = direct parallel to RAG over financial data" | Correctness + safety framing is the decisive differentiator |
| 2 | LeaseI | Leasing compliance | Add: "core design rule enforced in code: LLM reasons, deterministic logic makes every regulated call — same pattern required for financial AI" | Maps directly to Amex's safety emphasis |
| 3 | AgentProbe | Eval engine | Lead: "owned full eval suite — CI-integrated, every commit scored, regressions blocked before merge" | Direct match to "evaluation or monitoring tooling" requirement |
| 4 | Entrata | General compliance | Add: "8 years in federal housing compliance (HUD, LIHTC, HAP, AMI) — regulated-domain mindset is built in, not learned" | Financial services = regulated-domain analogue |
| 5 | Skills | Current stack | De-emphasize Go/K8s/Kafka; lead Python + AWS + TypeScript + LangGraph + RAG | Honest framing of production stack |

---

## F) Interview Plan

| # | JD Requirement | Story | S | T | A | R | Reflection |
|---|----------------|-------|---|---|---|---|------------|
| 1 | RAG over regulated data — correctness + safety | LeaseI compliance RAG | Affordable housing compliance AI needs 100% citation accuracy | Build TF-IDF RAG with deterministic compliance gates | Section-aware chunking, LLM reasons, hard gate blocks unsupported claims | 100% citation correctness, 0 unsupported-claim rate | Guardrails must be architecture, not prompts — prompts drift |
| 2 | Eval/monitoring tooling | AgentProbe eval engine | No CI-integrated eval for LLM agent commits | 5-metric evaluation pipeline running on every commit | LLM-as-judge + GitHub Actions; regressions blocked before merge | Every commit scored; drift tracked per-run | Cache reference answers early — LLM-as-judge is slow |
| 3 | Production AI in regulated environment | Entrata first AI pipeline | 1.6M financial records, manual process, compliance risk | Build automated pipeline with quality gates from day one | Python + PyTorch + OpenAI API; output validation, compliance controls at launch | Zero violations at launch | Quality gates in the architecture, not added after |
| 4 | Agentic workflows: reason + act | LeaseI 8-agent StateGraph | Support tickets needed root-cause investigation across multiple data sources | 8-agent pipeline with conditional routing and HITL escalation | Triage → Retrieval → Config → Historical → Reasoning → Validation → Human Escalation | Correctly traces false-ineligibility to misconfigured setting end-to-end | Agent knows when to stop — confidence gate is the most important design decision |
| 5 | Collaborate with product/design | Entrata cross-functional | Compliance, operations, product, finance with conflicting requirements across 120+ sprints | Translate federal housing requirements into modular service design | Sprint planning, requirement decomposition, stakeholder communication | 120+ sprints, zero compliance violations | Stakeholders remember the reasoning, not the implementation |

---

## G) Posting Legitimacy

| Signal | Finding | Weight |
|--------|---------|--------|
| Company | American Express — NYSE: AXP, ~70K employees, S&P 500 | Positive |
| Role coherence | Agentic AI Engineer building LLM products for commercial customers = real active need | Positive |
| JD specificity | Detailed stack (Python/Go/TypeScript, K8s, Kafka, gRPC), specific agent patterns — not generic | Positive |
| H-1B | Top-20 US sponsor, extensive legal infrastructure | Positive |
| No URL | Came via paste — verify posting is active before applying | Neutral |
| Comp | Not disclosed — large company, likely internal band-constrained | Neutral |

**Assessment: High Confidence** — Real Amex posting, coherent engineering requirements, active AI investment at enterprise scale.

---

## Machine Summary

```yaml
company: American Express
role: AI Engineer (Agentic AI)
date: 2026-08-04
score: 3.8
archetype: Agentic AI Engineer / AI Platform (financial services)
legitimacy: High Confidence
compensation: not disclosed (~$120-155K market range + bonus)
h1b: High Confidence (top-20 US sponsor, 500-1000+ petitions/year)
location: unconfirmed (NYC or Phoenix likely; must verify)
verdict: below 4.5 threshold — strategic apply given H-1B certainty
key_gap: Go/Kubernetes/Kafka/gRPC not in stack; large company = 4-5 round interview loop
key_strength: RAG correctness + safety (LeaseI = direct parallel to "RAG over financial data with correctness and safety"); eval ownership (AgentProbe CI-integrated); 8yr regulated domain (federal housing compliance = regulated mindset analogous to financial services); H-1B sponsor certainty
```

---

## Keywords extracted

Agentic AI, LLM Orchestration, RAG Pipelines, Financial Data, Correctness, Safety, LLM Evaluation, Monitoring Tooling, Production AI, Python, Go, TypeScript, AWS, GCP, Kubernetes, Kafka, gRPC, Distributed Systems, Event-Driven, REST APIs, Schema Validation, Structured Data, AI-Assisted Development, Claude Code, Open Source, Financial Services, Regulated Environment, American Express
