# Story Bank — Master STAR+R Stories

This file accumulates your best interview stories over time. Each evaluation (Block F) adds new stories here. Instead of memorizing 100 answers, maintain 5-10 deep stories that you can bend to answer almost any behavioral question.

## How it works

1. Every time `/career-ops oferta` generates Block F (Interview Plan), new STAR+R stories get appended here
2. Before your next interview, review this file — your stories are already organized by theme
3. The "Big Three" questions can be answered with stories from this bank:
   - "Tell me about yourself" → combine 2-3 stories into a narrative
   - "Tell me about your most impactful project" → pick your highest-impact story
   - "Tell me about a conflict you resolved" → find a story with a Reflection

## Stories

<!-- Stories will be added here as you evaluate offers -->
<!-- Format:
### [Theme] Story Title
**Source:** Report #NNN — Company — Role
**S (Situation):** ...
**T (Task):** ...
**A (Action):** ...
**R (Result):** ...
**Reflection:** What I learned / what I'd do differently
**Best for questions about:** [list of question types this story answers]
-->

---

### [Agentic AI] AgentProbe: Shipping a 3-Agent LangGraph Runtime
**Source:** Report #089 — Anthropic — Forward Deployed Engineer, Applied AI
**S (Situation):** Building an open-source LLM evaluation toolkit in 2024 — needed a real multi-agent system with tool calls, not just a chatbot wrapper.
**T (Task):** Ship a production-grade agentic system with inter-agent coordination, multi-provider LLM routing, and automated quality gates.
**A (Action):** Built Orchestrator, RAG Tracer, and Auto Fix agents with inter-agent state handoffs via LangGraph; added LLM Router for dynamic provider selection (Anthropic, OpenAI, Groq, Ollama); deployed as 15-endpoint FastAPI backend; added 5-metric LLM-as-judge eval engine integrated into CI/CD.
**R (Result):** Live GitHub repo with CI/CD that blocks failing agent runs automatically before production. End-to-end observability via React dashboard with per-run regression drift detection.
**Reflection:** Agents fail in non-obvious ways — observability needs to be designed first, not bolted on. The LLM-as-judge prompt engineering was harder than the application prompts; calibration of the eval judge is its own discipline.
**Best for questions about:** Agent development, LLM applications, production AI, quality gates, observability, what you've built, favorite project

---

### [Production AI on Regulated Data] Entrata: 1.6M Financial Records AI Pipeline
**Source:** Report #089 — Anthropic — Forward Deployed Engineer, Applied AI
**S (Situation):** Entrata had 1.6M financial records needing automated transformation — no AI tooling yet; data was regulated and required compliance guardrails.
**T (Task):** Design and deploy a Python + LLM pipeline on regulated financial data without introducing compliance risk.
**A (Action):** Used Python, PyTorch, and OpenAI API; added output validation gates to catch silent failures before production; maintained PHI compliance throughout the pipeline.
**R (Result):** 100% production output with quality gates; zero compliance incidents across all client environments.
**Reflection:** On regulated data, AI output validation is non-negotiable. Silent failures (wrong outputs that don't throw errors) are the hardest to catch — eval gates saved the project.
**Best for questions about:** Production AI, regulated data, compliance, enterprise deployment, what makes AI reliable

---

### [Healthcare AI / Enterprise Deployment] AI on FHIR: HIPAA-Compliant Clinical NLP
**Source:** Report #089 — Anthropic — Forward Deployed Engineer, Applied AI
**S (Situation):** Needed a proof-of-concept NLP system over structured medical records — healthcare domain with strict compliance requirements.
**T (Task):** Reduce manual clinical retrieval time while maintaining HIPAA compliance and supporting bilingual queries.
**A (Action):** Built Flask + React platform; used LLMs, BERT, and spaCy to translate natural language (EN/ES) to FHIR API queries; implemented HIPAA-compliant RBAC across structured medical records.
**R (Result):** ~60% reduction in manual retrieval time; HIPAA-compliant RBAC in place; bilingual support working in production.
**Reflection:** FHIR is highly structured — the NLP layer needs exact parameter mapping, not fuzzy extraction. Most demos fail at the query translation step; that is the hard part, not the NLP itself.
**Best for questions about:** Healthcare AI, compliance, customer deployment, NLP, domain-specific AI

---

### [Enterprise Delivery / Speed] Entrata: 40% Deployment Time Reduction Across 120+ Sprints
**Source:** Report #089 — Anthropic — Forward Deployed Engineer, Applied AI
**S (Situation):** 120+ Agile sprints at Entrata; deployment pipeline was slow and blocking releases for 100K+ MAU enterprise product.
**T (Task):** Lead containerization initiative to cut deployment overhead across 20+ modules.
**A (Action):** Docker-containerized 30%+ of modules; tuned 200+ SQL queries (30% performance gain); enforced TDD/BDD standards across all major releases.
**R (Result):** 40% faster deployments; 99.5% uptime sustained over 6+ consecutive months.
**Reflection:** Speed is a function of discipline, not heroics. The gains came from automation and standards, not working harder. TDD paid off most on the 30% of modules that looked simple but had hidden edge cases.
**Best for questions about:** Delivery speed, enterprise systems, production reliability, process improvement, scale

---

### [LLM Evaluation / Systematic Quality] AgentProbe: 5-Metric LLM-as-Judge Eval Engine
**Source:** Report #091 — Cohere — Applied AI Engineer - Agentic Workflows
**S (Situation):** Production LLM outputs vary unpredictably — needed reliable quality gates that catch hallucinations and compliance failures before they reach users, not after.
**T (Task):** Build a systematic, repeatable eval system that blocks bad agent runs automatically.
**A (Action):** Implemented LLM-as-judge with 5 metrics (factual accuracy, hallucination, retrieval, completeness, compliance); integrated into CI/CD so failing runs block production; added regression drift tracking in the observability dashboard.
**R (Result):** Zero manual QA needed per test run; eval pipeline runs automatically; dashboard surfaces regression drift over time.
**Reflection:** LLM-as-judge works best when the judge prompt is itself tested. Meta-evaluation matters -- the judge has to be calibrated before you trust it to gate production.
**Best for questions about:** LLM evaluation, quality gates, systematic testing, AI reliability, production AI systems

---

### [RAG Pipeline Design] AgentProbe: ChromaDB RAG Evaluation Layer
**Source:** Report #091 — Cohere — Applied AI Engineer - Agentic Workflows
**S (Situation):** RAG outputs were inconsistent -- retrieval quality was degrading silently across test suites without surfacing in final output metrics.
**T (Task):** Build a RAG evaluation layer that tracks retrieval quality per run independently from generation quality.
**A (Action):** Integrated ChromaDB with per-run metric capture; built RAG Tracer agent to monitor retrieval quality, latency, and regression drift separately from Orchestrator agent outputs.
**R (Result):** Real-time retrieval quality visible in dashboard; regressions caught before they compound into generation failures.
**Reflection:** Retrieval quality and generation quality are independent failure modes. Treating them together hides the root cause. Isolating retrieval as its own traced metric was the architectural decision that made debugging tractable.
**Best for questions about:** RAG systems, vector databases, retrieval design, agent debugging, system architecture

---

### [Reproducible Analysis / Provenance] LeaseI: HITL Compliance Pipeline with Auditable Rule Chain
**Source:** Report #147 — Apple — SWE, AI Platform (Algorithms)
**S (Situation):** Building an AI compliance platform where legal/compliance officers need to trust every determination — "the AI said so" is not acceptable in a regulated context.
**T (Task):** Design a RAG + agentic pipeline where every answer is either cited to a specific source clause or explicitly flagged as unsupported — with no silent failures.
**A (Action):** Built Phase 1 (Document Q&A) with OCR-fallback ingestion, section-aware chunking, TF-IDF retrieval, confidence-scored answers, and a human-review gate; built Phase 3 (Support Investigation) as an 8-agent LangGraph system (Triage → Retrieval → Configuration → Historical Incident → Structured Data → Reasoning → Validation → Human Escalation) with conditional escalation when confidence is too low. Core design rule: LLM extracts and reasons; a human or deterministic logic makes the final call. Validated end-to-end: income-eligible resident wrongly flagged ineligible correctly traced to a misconfigured global setting.
**R (Result):** 100% citation correctness on the Phase 1 eval set; deterministic rules engine keeps all compliance determinations replayable and auditable; 93.6% precision / 87.9% F1 on compliance rule classification.
**Reflection:** Reproducibility in AI is a day-zero architecture decision. Retrofitting auditability into a system that was "just LLM output" is nearly impossible. The citation gate and the escalation edge must be designed first — they can't be bolted on.
**Best for questions about:** HITL design, AI reliability, provenance tracking, reproducible analysis, compliance AI, regulated data

---

### [Access-Controlled Data Infrastructure] Entrata: PHI Pipeline on 1M+ Records
**Source:** Report #147 — Apple — SWE, AI Platform (Algorithms)
**S (Situation):** 1M+ property records across all client environments; resident data (SSNs, phone numbers) subject to PHI regulations; existing storage had no encryption.
**T (Task):** Encrypt all sensitive resident data in-flight and at rest; maintain compliance across 50%+ of the production codebase without disrupting running services.
**A (Action):** Implemented Libsodium encryption pipeline on AWS S3; updated all data insertion and retrieval paths across 50%+ of the codebase; enforced access controls at the pipeline level so only authorized paths could decrypt.
**R (Result):** 100% PHI compliance; zero security incidents; 50%+ codebase updated; zero downtime during rollout.
**Reflection:** Access control is an infrastructure design decision made at schema time. It cannot be retrofitted without touching every read/write path — starting from "secure by default" saves months of remediation.
**Best for questions about:** Data infrastructure, access controls, policy-aware systems, security, compliance engineering

---

### [Mentorship / Engineering Standards] Entrata: 300+ Code Reviews, 5+ Engineers Mentored
**Source:** Report #089 — Cohere — Applied AI Engineer - Agentic Workflows
**S (Situation):** Junior engineers on the Entrata team were inconsistently applying secure coding standards, creating accumulating review debt across releases.
**T (Task):** Establish coding standards and build junior engineer capability without slowing sprint velocity.
**A (Action):** Ran 300+ peer code reviews with structured reasoning feedback (not just corrections); created coding standards reference documentation; pair-programmed on complex modules to demonstrate patterns in context.
**R (Result):** Junior engineer output quality improved measurably across the next sprint cycle; zero security incidents across all major releases.
**Reflection:** The most effective code review teaches reasoning, not just corrections. "Here's the security risk and here's how to think about it" scales better than "change this line." Engineers who understand why make better decisions autonomously.
**Best for questions about:** Mentorship, team leadership, code quality, scaling standards, technical leadership

---

### [Retrieval Design / RAG Architecture] LeaseI: Choosing the Right Retrieval Method
**Source:** Report #151 — Apple — SWE, Agentic AI (AI & Data Platforms)
**S (Situation):** Building retrieval for two different content types in LeaseI: structured lease PDFs (fixed sections, rule-based clauses) and support incident tickets (unstructured, conversational).
**T (Task):** Pick the retrieval strategy that maximizes answer correctness on each content type -- dense embeddings (ChromaDB/semantic) vs. sparse retrieval (TF-IDF).
**A (Action):** Evaluated both approaches on the Document Intelligence module: TF-IDF with section-aware chunking for structured lease PDFs; considered ChromaDB embeddings as the alternative. Ran precision/F1 comparisons -- TF-IDF outperformed dense retrieval on clause-boundary-sensitive questions because lease sections have explicit structure that embeddings blur.
**R (Result):** Chose TF-IDF for Phase 1 (Document Intelligence) and designed the retriever interface to be backend-agnostic -- ChromaDB upgrade path documented for future unstructured content. 93.6% precision and 87.9% F1 on compliance rules.
**Reflection:** Retrieval method selection is a domain decision, not a tech trend decision. Dense embeddings excel at fuzzy semantic recall; sparse retrieval excels at keyword-critical structured documents. Starting with the content type, not the framework, is the correct order of reasoning.
**Best for questions about:** RAG system design, retrieval architecture, technical decision-making, applied AI, choosing tools, domain-specific AI

---

### [Workflow Automation / Adoption] Entrata: 80% Manual Workload Elimination
**Source:** Report #474 — Google — AI Solution Builder
**S (Situation):** Multiple operational teams at Entrata were manually running gross-rent updates, income-limit imports, and document-validation workflows — each cycle took hours and introduced human error on regulated financial data.
**T (Task):** Automate without breaking compliance guarantees or downstream eligibility logic for 100K+ housing units.
**A (Action):** Built Python/Bash pipelines for gross-rent bulk updates; wrote stored-procedure automation for annual income-limit imports with pre/post reconciliation; designed RabbitMQ async processing with retry/idempotency guarantees for gross-rent workflows; built internal debugging tools adopted by the team.
**R (Result):** 80% of manual operational workload eliminated; zero compliance violations across all cycles; team debugging time cut by 40%.
**Reflection:** Automation on regulated data needs a validation gate, not just a scheduler. Silent failures (wrong outputs that don't throw errors) are the hardest problem; the gate that catches them is more valuable than the automation itself.
**Best for questions about:** Workflow automation, 0-to-1 builds, operational efficiency, regulated data, enterprise automation, embedding with teams

---

### [Income Verification Domain] Entrata: Income Limits Import at Scale
**Source:** Report #172 — Checkr (Truework) — Sr SWE (Python), Mortgage
**S (Situation):** Entrata needed to process 1.6M HUD and Tax Credit income limit records across 5 years — inconsistent formats, regulatory schema changes, and family-size/AMI-percentage tier logic making generic import impossible.
**T (Task):** Design scripts that work across all format variations without manual intervention per file.
**A (Action):** Built parameterized SQL import scripts; automated AMI threshold calculation and eligibility tier logic; validated records before insertion to surface schema violations before they entered eligibility calculations.
**R (Result):** Zero import failures in production; eligibility modules stable across 100K+ unit portfolios; framework reused for subsequent HUD data updates.
**Reflection:** Income data is never clean at the edges. Building validation as a first-class concern — not a QA step — is the difference between a pipeline that works once and one that's maintainable.
**Best for questions about:** Data pipelines, financial data at scale, income verification, production reliability, domain-specific engineering, mortgage data

---

### [Income Fraud Domain] Entrata: 8 Years Catching Income Fraud in Rental Applications
**Source:** Report #174 — Snappt — Software Engineer
**S (Situation):** Entrata's affordable housing platform (LIHTC, Section 8/HCV, HUD) required rigorous income eligibility screening — property managers were routinely receiving fraudulent paystubs and inflated income claims from rental applicants trying to pass AMI thresholds they didn't meet.
**T (Task):** Build and maintain automated income eligibility verification, AMI threshold enforcement, and recertification workflows that catch income misrepresentation before leases are signed.
**A (Action):** Built AMI calculation engine, income eligibility automation, and recertification workflows for LIHTC/HCV/HUD portfolios; flagged household-composition fraud and income misrepresentation via deterministic rules; processed 1.6M HUD and Tax Credit income limit records with validation gates before insertion into eligibility calculations.
**R (Result):** Zero compliance violations across 100K+ unit portfolios across 7+ years; fraud flagging built into the eligibility pipeline; framework reused across all subsequent HUD data updates.
**Reflection:** Income fraud patterns are consistent: paystubs with round-number incomes, mismatched employer EINs, income amounts that land exactly at AMI percentage cutoffs. The human fraud detector notices these patterns over years; the AI fraud detector needs them encoded as features. Having been the human, I know what the features should be.
**Best for questions about:** Income fraud domain, rental fraud detection, income verification, LIHTC/HCV/HUD compliance, domain expertise, fraud pattern recognition

---

### [Eval Harnesses / Simulation Testing] LeaseI: Reproducible Eval Harness with Regression Gating
**Source:** Report #208 — Cisco (Splunk) — Agentic Solutions Architect
**S (Situation):** Compliance AI for affordable housing — needed to validate 8-agent pipeline before every release without knowing which edge cases would emerge in production.
**T (Task):** Build an evaluation harness that catches regressions in simulation before they reach production users.
**A (Action):** 225-query benchmark dataset across 5 US states + federal regulations; pass@k multi-trial sampling (multi-trial per query to detect non-deterministic variance); LLM-as-judge scoring on factual accuracy, grounding rate, citation correctness, and hallucination; regression gate blocks deploys when score drops below threshold. Validated three agentic surfaces independently before each release.
**R (Result):** 93.6% precision across 1,240 residential lease PDFs; 0% unsupported-claim rate on eval set; every release shipped with documented simulation validation. Regressions caught and fixed before production 3+ times.
**Reflection:** Calibrating the LLM-as-judge prompt is harder than the application prompts — the eval is only as reliable as your judge. Run the judge against known-good and known-bad outputs first; only deploy it as a gate when you've verified it catches the failure modes you actually care about.
**Best for questions about:** Eval harnesses, simulation testing, regression gating, LLM evaluation, production AI quality, offline evals, agentic system validation

---

### [Guardrails / Governance / Audit Trails] LeaseI: Code-Enforced Safety Boundaries
**Source:** Report #208 — Cisco (Splunk) — Agentic Solutions Architect
**S (Situation):** Compliance AI where LLM reasoning errors on eligibility calculations could result in wrongful tenant actions — regulators can audit every decision made by the system.
**T (Task):** Enforce guardrails that guarantee no regulated decision is made by the LLM without deterministic verification or human sign-off.
**A (Action):** Core design rule enforced in code everywhere: LLM extracts and reasons; human or deterministic logic makes every final eligibility/compliance/financial call. Confidence scoring triggers HITL escalation when agent certainty is below threshold. Every answer cites the exact source clause it draws from, or is flagged as unsupported and downgraded. Tenant self-service agent safety boundary tested: never auto-resolves eligibility, configuration, or calculation for a tenant — always routes to staff.
**R (Result):** 100% citation correctness on eval set; 0% unsupported-claim rate; HITL escalation verified by test suite. System is auditable end-to-end — every decision trace is reproducible.
**Reflection:** Guardrails in prompts are suggestions. Guardrails in code are guarantees. If your safety boundary relies on the LLM deciding not to cross it, you don't have a safety boundary. Build the hard limits in deterministic logic and use prompts only for reasoning within those limits.
**Best for questions about:** Guardrails, HITL, governance, audit trails, policy enforcement, compliance AI, production safety, autonomous system boundaries

---

### [Consulting-Flavored Enterprise Delivery] Entrata: 20+ Production Modules for Housing Authority Clients
**Source:** Report #351 — Consulting Organization (anon) — AI Engineer
**S (Situation):** Housing authority clients (public agencies administering HUD/LIHTC programs) relied on Entrata software for annual eligibility decisions affecting thousands of residents.
**T (Task):** Deliver production features on HUD regulatory release cycles — missed deadlines meant regulatory violations for clients, not just late features.
**A (Action):** Shipped 20+ full-stack modules over 120+ Agile sprints; owned the annual HUD income-limit import pipeline for 7 years (few thousand federal rows → 180K domain records); coordinated with compliance, support, and client-facing PMs on every major release.
**R (Result):** Zero compliance violations across 7 years; 99.5% uptime; 80% manual workload eliminated through Python/PL-SQL automation.
**Reflection:** Client delivery in regulated software mirrors consulting delivery — the client doesn't care about your internal sprint structure, they care that their regulatory deadline is met. Build the accountability culture first; everything else follows.
**Best for questions about:** Consulting experience objections, enterprise delivery, stakeholder management, regulated domain work, client-facing delivery
