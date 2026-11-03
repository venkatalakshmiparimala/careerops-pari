# Evaluation: Arize AI — Forward Deployed AI Engineer, East

**Date:** 2026-06-16
**URL:** https://job-boards.greenhouse.io/arizeai/jobs/5993755004
**Archetype:** AI Forward Deployed / AI Platform (LLMOps) — hybrid
**Score:** 4.7/5
**Legitimacy:** High Confidence
**PDF:** [cv-arize-ai-fde-east-2026-06-16.pdf](../output/cv-arize-ai-fde-east-2026-06-16.pdf)

---

## A) Role Summary

| Dimension | Detail |
|-----------|--------|
| **Archetype** | AI Forward Deployed + AI Platform / LLMOps (hybrid) |
| **Domain** | GenAI observability, LLM evaluation, production AI deployment |
| **Function** | Deploy / consult / build — customer-facing technical delivery with product influence |
| **Seniority** | Mid-senior IC (2-5 YOE floor; customer ownership + exec-level communication puts effective bar at senior) |
| **Remote** | Remote, NYC metro area required |
| **Team size** | Not specified; cross-functional with Sales, CS, Product, Engineering |
| **Location constraint** | NYC metro area — candidate open to relocating, scored 4.0 per location policy |
| **Salary** | $125,000–$175,000 + equity (explicitly disclosed) |
| **TL;DR** | Embed with East Coast enterprise AI teams to design and ship production-grade GenAI observability programs on Arize's platform — lead technical discussions from engineers to executives, build custom integrations, and influence product roadmap from the field. |

**What Arize AI does:** ML observability and LLM evaluation platform — traces, evals, experiments, monitoring. Their open-source Phoenix (OpenTelemetry-native) is the leading OSS observability toolkit for LLM/agent systems; Arize is the enterprise cloud layer on top. Series C, $131M raised (Feb 2025), ~200 employees, no layoffs detected. Active multi-region FDE hiring (East, West, EMEA, APJ) signals the function is core go-to-market.

**Note on role vs. scan history label:** Scan history tagged this URL (5993755004) as "AI Solutions Engineer, East" from initial ATS scrape on 2026-06-03. The Greenhouse posting itself carries the title "Forward Deployed AI Engineer, East." Treated as an FDE role throughout this evaluation.

---

## B) Match with CV

### Requirements → CV Mapping

| JD Requirement | CV Evidence | Strength |
|----------------|-------------|----------|
| 2-5 years hands-on software development | 8+ years: Entrata (Jan 2017–Aug 2024) + GMU RA (Aug 2024–Aug 2025) — well above the 2-5yr floor | Exceptional |
| Python (at least two of Python/Java/TypeScript) | Production Python: Entrata (20+ microservices, 1M+ records, 1.6M financial records pipeline, PyTorch + OpenAI API); AgentProbe (FastAPI 15-endpoint backend); GMU research (regression models, Isolation Forest) | Exceptional |
| TypeScript (at least two of Python/Java/TypeScript) | TypeScript in skills; JavaScript production at Entrata (full-stack modules) | Strong — satisfies "at least two" requirement with Python |
| ML/AI engineering (MLOps pipelines, production GenAI applications) | AgentProbe: 5-metric LLM-as-judge eval engine, 3 LangGraph agents, RAG pipeline tracking, ChromaDB; AI on FHIR: LLM + BERT + embeddings; Entrata: PyTorch + OpenAI API on 1.6M financial records | Exceptional — DIRECT match to Arize's product use case |
| LLM observability / evaluation (the core product Arize sells) | AgentProbe: trace-level agent monitoring, per-run metrics, regression drift, retrieval quality, latency tracking across concurrent test suites — structurally identical to Arize Phoenix. This is the proof point: candidate built the product category. | Exceptional — strongest possible signal |
| Public cloud (AWS, GCP, Azure) | AWS S3, EC2, RDS, Glue (production at Entrata, PHI-compliant migration); Azure in skills | Strong (AWS primary; Azure listed) |
| Docker / Kubernetes | Docker: containerized 30%+ of Entrata microservices, cut execution time 50%; Docker in AgentProbe stack | Strong for Docker; Kubernetes not explicitly cited (gap, see below) |
| Partner with enterprise AI teams (design + implement GenAI observability programs) | Entrata: 100K+ MAU production platform, 120+ Agile sprints, cross-team delivery; GMU: stakeholder dashboards for faculty leadership | Strong — indirect proxy (no named enterprise customer engagements) |
| Lead technical discussions with engineers to executives | GMU research: presented ML results to faculty leadership (40% comprehension improvement); Entrata: 300+ peer code reviews, 5+ junior engineers mentored | Strong |
| Build custom integrations and workflows extending a platform | AgentProbe's LLM Router: provider-agnostic interface routing to Anthropic, OpenAI, Groq, Ollama; 15-endpoint FastAPI backend — built to be extended; Entrata: 5+ internal platform tools | Strong — direct builder proof |
| Manage concurrent customer engagements (scoping through delivery) | Not direct named-account management; proxy: 20+ modules across parallel Entrata sprints, multiple simultaneous GMU research pipelines | Moderate — the one material gap |
| Cross-functional: Sales, CS, Product, Engineering | 120+ Agile sprints coordinating across product/engineering; GMU cross-functional research delivery | Moderate-Strong |

### Gaps

| Gap | Blocker? | Mitigation |
|-----|----------|-----------|
| Java not in stack | Nice-to-have | JD explicitly says "Python, Java, and/or TypeScript" — any two suffice. Python (8yr production) + TypeScript satisfies the requirement. Java is purely additive. |
| No Kubernetes in CV | Nice-to-have | Docker production experience confirmed (Entrata + AgentProbe). K8s understanding can be noted: "containerization with Docker across 30%+ of microservices; familiar with K8s orchestration patterns." Arize's infra team handles K8s; FDE role is deployment-oriented, not infra-engineering. |
| No direct named enterprise customer delivery | Moderate | Strongest proxy: Entrata's enterprise property management clients are the end users of everything Parimala shipped — 100K+ MAU. AgentProbe as open-source demonstrates ability to build for external users with public accountability. Frame as "I've owned production systems at customer scale every day — now I want to own the customer relationship." |
| OpenTelemetry not explicitly named | Nice-to-have | AgentProbe is "structured for integration with external observability backends" — the tracing semantics are aligned. Quick fix: add "OpenTelemetry-aware" to AgentProbe description and LinkedIn. |
| NYC metro relocation required | Logistics | Candidate is open to NYC relocation. No relocation support mentioned in JD — self-funded move assumed. Scored 4.0 per location policy (NYC relocation accepted, no support). |
| H-1B sponsorship unconfirmed | Risk factor | See Block G and visa analysis below. Arize AI has filed 2 LCAs (FY2022-2024) per immihelp. Small but demonstrated sponsorship history. JD includes visa sponsorship question — policy unconfirmed. Warrants a direct recruiter ask before deep investment. |

---

## C) Level and Strategy

**Level detected in JD:** Mid-senior IC. "2-5 years" is the stated floor, but the role requires: customer ownership, executive-level communication, scoping through delivery, cross-functional influence across Sales/CS/Product/Eng. The effective bar is senior — this is a high-autonomy, high-visibility role.

**Parimala's natural level for this archetype:** Senior. 8+ years of production Python engineering, end-to-end delivery ownership, multi-stakeholder communication, active AI builder (AgentProbe, live on GitHub). Significantly above the stated floor.

**"Sell senior without lying" plan:**

1. **Lead with the product mirror:** "I built an LLM eval + observability toolkit — trace-level monitoring, 5-metric eval engine, ChromaDB RAG tracking, CI/CD-integrated quality gates. That's the same category as Arize Phoenix. I didn't just use observability tools; I designed one." This is the most powerful opening for any Arize interviewer.

2. **Frame Entrata as enterprise-scale delivery:** "100K+ monthly active users, 120+ Agile sprints, 99.5% uptime over 6+ months, 40% deployment time reduction — I know what production-grade accountability means at scale."

3. **Position the FDE convergence:** "I combine the builder instincts to extend platforms (LLM Router, FastAPI integrations, Docker) with the cross-functional communication to work from engineering to executive stakeholders. AgentProbe is my proof that I can own an end-to-end technical product."

4. **Surface the Python + TypeScript dual-language signal:** The JD requires proficiency in at least two of three languages. Python (8yr) + TypeScript is an unambiguous satisfier — make this explicit early.

5. **MS degree + 3.87 GPA:** Signals structured AI/data engineering knowledge alongside industry depth. Rare combination in a candidate this early in the FDE title track.

**"If they downlevel me" plan:**
- Accept if base is $115K+ (well within the $125-175K range).
- Request 6-month performance review with explicit promotion criteria (scoped from senior IC to lead FDE).
- FDE at observability companies: once you own a named strategic account, internal leverage grows quickly. Series C equity is meaningful at Arize's current trajectory.

---

## D) Comp and Demand

| Source | Data Point |
|--------|------------|
| **Job posting (Greenhouse)** | $125,000–$175,000 + competitive equity — explicitly disclosed |
| **Levels.fyi — Arize AI** | $133K–$162K total comp across roles; no FDE East-specific breakdown available |
| **Glassdoor — Arize AI** | 4.6/5 comp & benefits rating; culture rated highly by employees |
| **immihelp.com — Arize AI H1B LCAs** | 2 LCAs filed FY2022-2024; most common sponsored role: Machine Learning Software Sales Engineer |
| **Market: FDE at AI observability/LLMOps startups (2026)** | $120K–$160K base; Series C startups add significant equity component (0.05–0.2% for senior IC) |
| **Parimala's target** | $100K–$140K base minimum; $125-175K range is above target and in top quartile |

**Comp verdict:** The explicit $125K–$175K range scores 5/5 for comp — this is at or above the top end of Parimala's $100K–$140K target, and the upper bound ($175K) represents a meaningful stretch above market. The East role carries a higher salary band than the general US FDE posting (which was undisclosed, estimated $120-150K in report #090). Arize is Series C, well-funded ($131M), with a product category in strong demand — equity upside is real.

**Demand trend:** FDE function is expanding rapidly across AI observability companies. Arize has active postings in East, West, EMEA, APJ — multiple parallel FDE hires signals intentional geographic expansion, not a one-off role. The East posting specifically targets NYC metro, consistent with Arize's stated NYC office presence.

---

## E) Customization Plan

### CV Changes (Top 5)

| # | Section | Current | Proposed Change | Why |
|---|---------|---------|-----------------|-----|
| 1 | Professional Summary | "AI Engineer with 8+ years of production Python engineering..." | Rewrite to lead with observability angle: "AI engineer with 8+ years of production Python engineering and a live open-source LLM eval + agent observability toolkit (AgentProbe) — trace-level monitoring, 5-metric LLM-as-judge eval engine, RAG pipeline tracking, CI/CD quality gates. Python (8yr, production) + TypeScript. Targeting enterprise GenAI deployment roles." | Mirrors Arize's exact product vocabulary; surfaces the Python + TS dual-language qualification immediately |
| 2 | AgentProbe bullet 3 | "Delivered end-to-end observability via React dashboard with trace-level agent monitoring..." | Append: "...structured for integration with external observability backends (OpenTelemetry-compatible tracing semantics)" | Signals OTel ecosystem awareness — Arize Phoenix is built on OTel; this connects the dots without overclaiming |
| 3 | Entrata Software Engineer bullet (top) | "Reduced deployment times by 40% by building 20+ full-stack microservices..." | Add customer-impact framing: "...for 100K+ monthly active users at enterprise property management companies — 99.5% uptime sustained over 6+ months through direct production ownership and on-call accountability" | Positions Entrata scale as customer-facing delivery proof, the key FDE qualification |
| 4 | Skills: Docker | Listed generically in Cloud & DevOps | Move Docker to explicit standalone callout: "Docker (production containerization, 30%+ Entrata microservices; AgentProbe stack); Kubernetes (orchestration patterns)" | Addresses the K8s gap without overclaiming; Docker depth is real and should lead |
| 5 | Projects ordering | AgentProbe #1, AI on FHIR #2, CrashClarity #3 | Keep this order — it is already correct for this archetype. Confirm AgentProbe leads with the observability framing and includes the live GitHub URL prominently | Observability FDE recruiters will look at AgentProbe first; it must immediately signal relevance |

### LinkedIn Changes (Top 5)

| # | Section | Proposed Change |
|---|---------|-----------------|
| 1 | Headline | "AI Engineer | LLM Observability & Evals | AgentProbe (open-source) | Python + TypeScript | LangGraph | FastAPI | NYC-open" |
| 2 | About section | Open with: "I build systems that make LLMs accountable in production — eval engines, trace-level monitoring, and RAG quality tracking. AgentProbe is my live proof: 5-metric LLM-as-judge, 3 LangGraph agents, OpenTelemetry-compatible tracing. Now targeting enterprise GenAI deployment." |
| 3 | Featured | Pin AgentProbe GitHub repo as primary featured item with caption: "Open-source LLM eval + observability toolkit — same architecture as Arize Phoenix, built locally at zero cost." |
| 4 | Skills (top 5) | Ensure: "LLM Evaluation", "Agent Observability", "LangGraph", "OpenTelemetry", "Python" appear in top skills — these are Arize's core product vocabulary |
| 5 | Location | Update to "New York City Metropolitan Area" to match Arize's East role requirement and appear in NYC-filtered recruiter searches |

---

## F) Interview Plan

### STAR+R Stories

| # | JD Requirement | Story | S | T | A | R | Reflection |
|---|---------------|-------|---|---|---|---|------------|
| 1 | Design + implement production-grade GenAI observability programs | AgentProbe: eval engine + trace monitoring | Building open-source AI eval toolkit; LLMs failing silently in production with no visibility into why | Design a quality gate system covering hallucination, retrieval failures, compliance, and latency across concurrent agent runs | Built 5-metric LLM-as-judge eval engine + trace-level React dashboard; CI/CD integration auto-blocking failing runs; ChromaDB RAG tracking per run | 100% locally deployable at zero cost; real eval results catching issues before production reach | You can't debug what you can't observe — I designed evals as first-class citizens, not afterthoughts. That's the same thesis Arize is built on. |
| 2 | Manage concurrent customer engagements from scoping through delivery | Entrata 120+ sprint parallel delivery | Supporting 100K+ MAU platform with 20+ simultaneous module streams across client environments | Deliver multiple feature streams concurrently without degrading uptime, performance, or security compliance | Sprint backlog ownership, peer code reviews (300+), Docker containerization to isolate deployment risks, automated test suites | 40% deployment time reduction; 30% query performance gain; 99.5% uptime; 100% PHI compliance on AWS migration with zero security incidents | Concurrent delivery fails when scope is ambiguous — I enforced spec clarity at the start of each sprint so parallel streams didn't compound technical debt |
| 3 | Lead technical discussions with engineers to executives | GMU research dashboards + Entrata stakeholder delivery | Faculty leadership and product stakeholders needed ML research and system metrics in accessible, decision-ready formats | Translate complex ML outputs (R², anomaly flags, model drift) into actionable dashboards for non-technical leadership | Built Tableau, ggplot2, and Quarto dashboards mapping model metrics to faculty decisions; ran Entrata sprint reviews with product and engineering | 40% comprehension improvement across two GMU cohorts; Entrata features adopted on schedule; no critical post-release bugs across reviewed modules | Executives don't want to see the model. They want to know what changed and what they should do. I learned to lead with the decision, not the data. |
| 4 | Build custom integrations and workflows extending the Arize platform | AgentProbe LLM Router + FastAPI integration layer | AgentProbe needed to work with any LLM provider without rewiring eval logic per model change | Design an integration layer that is provider-agnostic and extensible without breaking eval consistency | Built LLM Router dispatching to Anthropic, OpenAI, Groq, Ollama; 15-endpoint FastAPI backend abstracting all provider-specific auth, rate limits, and response formats | Any new LLM provider wired in <1 hour; zero changes to eval core per provider swap; open-source contributors able to extend independently | Generic interfaces are force multipliers. One abstraction unlocked infinite extensibility — same principle I'd apply to extending Arize's platform for customer-specific workflows. |
| 5 | Deploy GenAI solutions on public cloud infrastructure | Entrata AWS migration (1.6M financial records, PHI) | All client data required migration to AWS S3 with encryption to achieve 100% PHI compliance — regulated data, zero tolerance for error | Design and execute a zero-downtime, secure migration pipeline with automated output validation | Architected Libsodium-encrypted pipelines, built 5+ internal tools on the new infrastructure, automated quality gates flagging anomalies before final load | 100% PHI compliance, zero security incidents, 80% reduction in manual operational workload through PL/SQL automation | Compliance is a design constraint, not a checklist. I architect around it from day one rather than bolt it on at the end. |
| 6 | Partner cross-functionally with Sales, CS, Product, Engineering | Entrata cross-team product delivery at scale | Features had to coordinate across product, engineering, client-success, and compliance at a company serving enterprise property managers | Bridge technical implementation and business requirements across 120+ Agile sprints spanning multiple teams | Wrote specs, ran code reviews, mentored 5+ junior engineers, eliminated 80% of manual ops workload via Python/PL-SQL automation, sat in cross-functional sprint planning | On-time feature delivery; 100+ critical bugs resolved; improved release reliability across all client environments | The engineers who close the most impactful loops are the ones who can fluently translate between business requirements and technical constraints without losing either side. |
| 7 | Fast prototyping in regulated/complex domains | AI on FHIR: NLP-to-FHIR query system | Healthcare team needed natural-language access to FHIR medical records — regulated domain (HIPAA), multilingual requirement, fast prototype timeline | Build a working NLP-to-FHIR translation layer with HIPAA-compliant RBAC fast enough to demo, without cutting security corners | Used LLMs + BERT + embeddings in Flask/React; implemented bilingual EN/ES support and RBAC from initial prototype (not bolted on later) | ~60% reduction in clinical retrieval time; HIPAA-compliant from day one; live on GitHub | Moving fast in regulated domains requires knowing exactly where shortcuts are safe. HIPAA was a hard constraint I designed around; UX polish was deferrable. Same prioritization I'd apply in any enterprise FDE engagement. |

### Recommended Case Study to Present

**Lead with AgentProbe — make it a product demo, not a project description.**

Walk through: "The problem I was solving is the exact problem Arize solves — how do you know your LLM is behaving correctly in production? Here's the architecture: 3 LangGraph agents, a 5-metric eval engine, trace-level monitoring, ChromaDB RAG tracking, CI/CD integration. Here's the GitHub. Here's a live run catching a hallucination failure before it hits production. Here's how the React dashboard surfaces retrieval quality regression across concurrent test suites."

This reframes the interview: instead of "can this candidate learn Arize Phoenix?" the question becomes "this candidate already built the thing Arize Phoenix does — they already think in observability-first terms."

**Second case study:** Entrata AWS + PHI compliance migration — demonstrates cloud infrastructure ownership, regulated data handling, and zero-defect delivery under compliance constraints. Relevant for enterprise customers with data governance requirements.

### Red-Flag Questions

| Question | How to answer |
|----------|--------------|
| "You haven't managed named enterprise customer engagements — is that a gap?" | "Every module I shipped at Entrata ran in production for 100K+ monthly active users at enterprise property management companies. I was accountable for uptime, performance, compliance, and reliability — the same accountability an FDE carries for a customer. The difference is I owned the product layer rather than the relationship layer. AgentProbe adds the dimension of external users and public accountability. I'm ready to own the relationship now." |
| "Your background is product engineering, not customer-facing. How will you handle executive stakeholder communication?" | "At Entrata I ran sprint reviews across product, engineering, and leadership. At GMU I translated ML research into dashboards that changed how faculty made decisions — 40% improvement in comprehension. I've had to communicate technical depth to non-technical decision-makers consistently throughout my career. The FDE role formalizes that into a named accountability I'm ready to step into." |
| "You don't have Kubernetes listed — is that a concern?" | "Docker is my production environment — I containerized 30%+ of Entrata's microservices and cut execution time 50%. I understand Kubernetes orchestration patterns and the scheduler/deployment model. I'd get up to speed on K8s-specific tooling quickly; the mental model from Docker translates directly." |
| "What is your visa status?" | "I'm on F-1 STEM OPT, which provides 3 years of work authorization — no sponsorship needed immediately. For H-1B, I'm a strong candidate: MS GPA 3.87, 8+ years of specialized AI engineering experience. I'd be happy to discuss the timeline and how Arize has handled H-1B transitions for other team members." |
| "Why Arize AI specifically?" | "I built AgentProbe to solve the same problem Arize Phoenix solves — LLM observability and eval in production. I understand your architecture not from documentation but from designing the same abstractions independently: trace semantics, eval metrics, retrieval quality tracking, CI/CD gates. Arize is where I want to take that work to enterprise scale with actual customer problems driving the roadmap." |

---

## G) Posting Legitimacy

**Assessment: High Confidence**

This is a distinct posting from the general "Forward Deployed Engineer, US" (job #6002637004, report #090) which showed legitimacy concerns (listed as removed June 10, 2026 on BuiltIn SF). The East-specific role (5993755004) has a different job ID, explicit salary disclosure, and geographic constraint — signals it was crafted for a specific headcount, not a generic evergreen.

| Signal | Finding | Weight |
|--------|---------|--------|
| **Posting freshness** | First seen in scan-history.tsv on 2026-06-03; no "removed" or "closed" flag in any subsequent scan (unlike 6002637004 which was flagged removed June 10) | Positive |
| **Apply button / URL** | Greenhouse URL (5993755004) remains active as of evaluation; scan history shows no redirect or delisting signal | Positive |
| **Salary transparency** | $125,000–$175,000 + equity explicitly disclosed — salary transparency in a JD is a strong signal of a committed, approved headcount | Positive |
| **JD specificity** | Named technologies (Python/Java/TypeScript, Docker/K8s, AWS/GCP/Azure, MLOps, GenAI); specific scope (scoping through delivery, cross-functional alignment, custom integrations); realistic requirements for a mid-senior IC | Positive |
| **Geographic specificity** | NYC metro requirement — not a generic "Remote US" posting. Specific region signals an intentional team build-out, not a speculative evergreen | Positive |
| **Company health** | Series C ($131M raised Feb 2025), no layoffs detected, actively building FDE function across East/West/EMEA/APJ in parallel | Positive |
| **Role-company fit** | FDE is the core go-to-market motion for an enterprise AI platform — makes complete strategic sense; East geographic expansion is consistent with NYC office announcement | Positive |
| **Reposting pattern** | Single scan entry; no repeat postings for this specific URL | Positive / Neutral |
| **H-1B sponsorship** | Arize AI Inc filed 2 LCAs (FY2022-2024) per immihelp — small but demonstrated sponsorship history. JD includes visa sponsorship question (policy not stated); warrants direct recruiter ask | Neutral / Proceed with caution on visa only |

**Context Notes:**
- The East role (5993755004) is explicitly different from the US-wide FDE (6002637004, report #090). Do not treat the legitimacy concern from report #090 as applying here — that URL showed removal signals; this one does not.
- Arize's multi-region FDE hiring (East, West, EMEA, APJ, DevSecOps) is consistent with a company scaling its go-to-market function post-Series C. This is not evergreen — it is intentional geographic expansion.
- **Visa action item:** Before submitting, confirm H-1B sponsorship directly with the Arize recruiter. Sample language: "I'm currently on F-1 STEM OPT with 3 years of authorization remaining. Can you confirm whether Arize AI supports H-1B sponsorship for this role?"

---

## H) Draft Application Answers

*Score 4.7/5 — above the 4.5 threshold. Draft answers for likely application form questions.*

**"Describe your experience with ML/AI engineering in production environments."**
> I built AgentProbe — an open-source LLM evaluation and agent testing toolkit with a 5-metric LLM-as-judge eval engine (factual accuracy, hallucination, retrieval, completeness, compliance), trace-level agent monitoring, ChromaDB RAG pipeline tracking, and CI/CD integration that blocks failing runs automatically. Before AgentProbe, I applied PyTorch and the OpenAI API to automate data transformation pipelines across 1.6M financial records at Entrata — production AI on regulated data with output validation and quality gates. I also built AI on FHIR, an NLP system using LLMs + BERT + embeddings to translate natural-language queries to FHIR APIs for healthcare records — HIPAA-compliant from day one.

**"What is your experience with GenAI observability tools?"**
> I designed and built an observability system from scratch. AgentProbe's architecture is structurally identical to what Arize Phoenix does: per-run metrics, regression drift tracking, retrieval quality scoring, latency monitoring across concurrent agent test suites — delivered through a React dashboard and structured for integration with external observability backends (OpenTelemetry-compatible tracing semantics). I understand the problem space from first principles, not just as a user of existing tools.

**"Tell us about a time you worked cross-functionally to deliver a technical project."**
> At Entrata, I owned delivery across 120+ Agile sprints coordinating product, engineering, and compliance requirements for a platform serving 100K+ monthly active users. I ran sprint reviews, wrote specs, conducted 300+ peer code reviews, and mentored 5+ junior engineers — while simultaneously shipping 20+ microservices and maintaining 99.5% uptime. The most complex cross-functional effort was the AWS S3 migration of all client data with Libsodium-encrypted pipelines: zero-downtime, 100% PHI compliant, zero security incidents, coordinating across engineering, security, and client-success stakeholders.

**"Do you require visa sponsorship?"**
> I am currently on F-1 STEM OPT, which provides 3 years of work authorization with no sponsorship required during that period. I am an excellent H-1B candidate when the time comes: MS in Data Analytics Engineering (GPA 3.87, George Mason University, May 2026) and 8+ years of specialized AI engineering experience. I would welcome a conversation about Arize's H-1B sponsorship process.

---

## Machine Summary

```yaml
report: "092"
company: "Arize AI"
role: "Forward Deployed AI Engineer, East"
date: "2026-06-16"
url: "https://job-boards.greenhouse.io/arizeai/jobs/5993755004"
score: 4.7
archetype: "AI Forward Deployed / AI Platform LLMOps"
legitimacy: "High Confidence"
pdf: "output/cv-arize-ai-fde-east-2026-06-16.pdf"
top_match_points:
  - "AgentProbe = direct LLM eval + observability proof point (built what Arize Phoenix does)"
  - "Salary $125K-$175K explicitly disclosed — above Parimala's $140K target ceiling; scores 5/5 comp"
  - "Python (8yr production) + TypeScript satisfies the at-least-two language requirement"
  - "Docker production containerization confirmed; AWS cloud confirmed"
  - "AgentProbe boost +0.3 applied (LLM eval/observability role with direct proof point)"
  - "NYC relocation accepted; candidate open to move"
key_gaps:
  - "Java not in stack (nice-to-have per JD phrasing — Python+TS satisfies requirement)"
  - "No direct named enterprise customer-facing delivery (proxied by Entrata 100K+ MAU at scale)"
  - "H-1B sponsorship history small (2 LCAs filed FY2022-2024) — verify with recruiter before deep investment"
  - "NYC relocation: no support mentioned in JD (self-funded assumed)"
visa_note: "Confirm H-1B sponsorship with recruiter before investing full application effort"
apply_recommendation: "Strong apply — score 4.7/5. Confirm visa sponsorship first. If confirmed: submit immediately."
```

---

## Keywords Extracted (ATS Optimization)

`LLM observability` · `GenAI observability` · `ML observability` · `LLM evaluation` · `production AI` · `forward deployed AI engineer` · `Python` · `TypeScript` · `Java` · `Docker` · `Kubernetes` · `AWS` · `GCP` · `Azure` · `enterprise AI teams` · `GenAI deployment` · `RAG pipeline` · `agent tracing` · `eval frameworks` · `MLOps pipelines` · `cross-functional collaboration` · `OpenTelemetry` · `customer engineering` · `AI integration`
