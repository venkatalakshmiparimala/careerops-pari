# Venkata Lakshmi Parimala Pasupuleti

venkatalakshmiparimala@gmail.com | +1-703-261-5410 | Fairfax, Virginia 22030
[LinkedIn](https://www.linkedin.com/in/venkata-lakshmi-parimala) | [GitHub](https://github.com/venkatalakshmiparimala) | [Portfolio](https://venkatalakshmiparimala.github.io/Portfolio/about.html)

---

## Professional Summary

Software Engineer with 8+ years shipping production systems at Entrata, a multi-tenant Affordable Housing SaaS platform serving 100K+ monthly active users and processing 1M+ property records. Backend and data depth first — PHP/OOP, SQL, stored procedures, ETL pipelines, asynchronous processing, AWS — with Python/FastAPI and agentic AI built on top of that foundation: LeaseI, a multi-agent LangGraph platform for lease compliance and support investigation, and AgentProbe, an open-source LLM evaluation toolkit. Core design rule across all AI work: the model retrieves, reasons, and explains; deterministic application logic and accountable humans make every regulated decision. Currently a Software Engineer at Intuit, integrating Anthropic Claude into financial applications. M.S. Data Analytics Engineering, George Mason University (GPA 3.87, May 2026).

---

## Technical Skills

**AI & LLMs:** LLM APIs (Anthropic Claude, OpenAI, Azure OpenAI, Groq, Ollama), AI Agents, Multi-Agent Orchestration, LangGraph, LangChain, RAG Pipelines, Hybrid Search, Embeddings, Prompt Engineering, Structured Output Schemas, Human-in-the-Loop Escalation, LLM-as-Judge Evaluation, Golden Dataset Regression Testing, LLM Routing, MCP, Guardrails and Safety Boundaries

**Vector Search & NLP:** ChromaDB, Pinecone, Weaviate, Elasticsearch, Semantic Search, TF-IDF Retrieval, BERT, spaCy, HuggingFace, OCR Ingestion, NLP-to-API Query Translation

**Python & ML:** Python, FastAPI, Flask, Django, Pandas, NumPy, scikit-learn, XGBoost, PyTorch, PySpark

**Other Languages & Web:** TypeScript, JavaScript, Node.js, React, Redux, PHP, Laravel, GraphQL, R, SQL, PL/SQL, Bash

**Databases & Data:** PostgreSQL, MySQL, Oracle, Redis, MongoDB, SQLite, ETL Pipelines, Data Modeling, Schema Design, Query Optimization, Execution-Plan Analysis, Stored Procedures, Data Migration, Effective Dating

**Cloud & DevOps:** AWS (S3, EC2, RDS, Lambda, Glue, SQS, API Gateway, IAM), Azure (OpenAI, Data Factory), GCP (Vertex AI), Docker, Docker Compose, GitHub Actions CI/CD

**Messaging & Monitoring:** RabbitMQ, Celery, Prometheus, Grafana, Grafana Loki, OpenTelemetry

**Practices:** REST APIs, API design and versioning, Microservices, OAuth, Agile/Scrum, TDD, Code Review, Data Structures & Algorithms, HIPAA/PHI Compliance, Observability

---

## Experience

### Software Engineer — Intuit
*Jun 2026 – Present · Virginia, USA*

- Integrate Anthropic Claude into Python/FastAPI services for financial data summaries, natural-language queries, and reporting.
- Design prompts and structured-output schemas for Claude so financial summaries and query answers stay consistent and easy to validate in downstream services.
- Ground Claude responses in customer financial data using retrieval, so answers trace back to their source records.
- Build evaluation and regression tests for LLM outputs (LLM-as-judge and golden datasets) to catch hallucinations and quality drops before release.
- Add guardrails around LLM calls — input validation, sensitive-data handling, and fallbacks when model output fails checks.
- Build ML pipelines in Python with scikit-learn and XGBoost, from data ingestion and feature engineering to model evaluation and prediction APIs.
- Develop backend APIs and data pipelines with validation and error handling, plus React/TypeScript front ends on AWS.
- Containerize services with Docker and ship them through GitHub Actions CI/CD to AWS, with logging and monitoring for production visibility.

### Senior Software Engineer — Entrata (Apartment & Affordable Housing SaaS)
*Nov 2020 – Jul 2024 · India · Multi-tenant platform with 100K+ monthly active users*

- Primary owner of high-risk Affordable Housing modules — HUD income-limit imports, eligibility calculations, gross-rent processing, document generation — including release planning, validation, rollback preparation, and production support.
- Maintained the annual HUD income-limit import for 6 years, transforming a few thousand federal source records into approximately 180,000 domain records per cycle with staging validation for malformed, duplicated, or unmapped input.
- Delivered 20+ features end-to-end (PHP, JavaScript, React, PostgreSQL) across 120+ Agile sprints.
- Built a RabbitMQ-based asynchronous processing system for annual gross-rent updates across thousands of tenant records — acknowledgment only after the database transaction succeeds, retry handling, and idempotent worker design to prevent double processing.
- Optimized 200+ SQL queries by 30% using execution-plan analysis and indexing — baselining elapsed time, row counts, reads, and writes, changing one variable at a time, and validating performance and business results.
- Cut manual operational work by 80% with Bash automation and PL/SQL pipelines, and cut triage time by 40% with internal debugging tools.
- Owned the Affordable Housing module integration for the AWS S3 document migration inside a shared framework built by another team — document inventory and classification, mapping and adapter logic preserving document type, metadata, and business ownership, read-back validation through the application path, and rollout in bounded batches with defined stop conditions; migration included Libsodium encryption for resident PHI.
- Owned the Affordable Housing document-module integration for a merge-field schema migration — field inventory, legacy-to-target mapping validation, and five-layer validation (metadata, mapping, data resolution, template behavior, rendered output) — on a platform generating hundreds of customer documents daily.
- Owned the application side of a production database migration in a Version 2 rollout, structured across release orchestration, database transformation, application deployment, and validation; cleared a suspected failed migration by comparing database dumps, timestamps, and execution records with the database team, avoiding a destructive rollback.
- Spent 8 years as the human check against income fraud in Affordable Housing portfolios — fake paystubs, income misrepresentation, and household-composition fraud across LIHTC, HCV, and HUD programs — including manual document verification of applicant income documents, checking paystubs and supporting records for forgery and falsification.
- Worked on a Docker microservices redesign that delivered 50% better scalability and 30% faster deployments.
- Reviewed 300+ pull requests, mentored junior engineers, ran Git knowledge-transfer sessions, and helped normalize peer review.

### Software Engineer — Entrata (Apartment & Affordable Housing SaaS)
*Sep 2018 – Oct 2020 · India*

- Built full-stack features across Affordable Housing modules (PHP, JavaScript, React, PostgreSQL), growing from user-interface-to-database feature work toward backend systems, databases, and business logic.
- Implemented, maintained, and debugged complex SQL and stored procedures used by production modules for eligibility, rent calculations, and document merge data.
- Applied effective dating and historical correctness across annual limits, certifications, and historical documents.
- Supported annual income-limit processing, schema and data migrations, and production releases with validation checkpoints and rollback readiness.
- Learned Git independently ahead of team adoption and supported the product's SVN-to-Git migration, helping engineers move from hesitation to practical daily usage.

---

## Projects

### LeaseI — Multi-Agent AI Platform for Lease Compliance and Support Investigation
*Python, LangGraph (8-agent), FastAPI, hybrid retrieval (TF-IDF + semantic), OCR, SQLite, CI/CD*
[github.com/venkatalakshmiparimala/Lease_complaince_rag](https://github.com/venkatalakshmiparimala/Lease_complaince_rag)

- Built a lease-compliance platform in Python where an 8-agent LangGraph StateGraph (triage, retrieval, reasoning, validation) investigates issues across three surfaces — Document Intelligence & Review, Support Ticket Investigation, and Tenant Self-Service — on one shared knowledge repository, escalating to a human when confidence is low.
- Built the RAG pipeline: OCR ingestion, section-aware chunking, hybrid search (TF-IDF + semantic reranking), and answers cited to the exact source clause.
- Added guardrails in code so eligibility and financial decisions always route to staff instead of the LLM.
- Measured 93.6% precision and 87.9% F1 across 1,240 test cases with an LLM-as-judge CI harness; Phase 1 evaluation recorded 100% citation correctness, 100% grounding, and 0% unsupported claims on the evaluation set.

### AgentProbe — Open-Source LLM Evaluation Toolkit
*Python, FastAPI, LangGraph, LangChain, ChromaDB, Ollama, Anthropic, OpenAI, Azure OpenAI, Groq*
[github.com/venkatalakshmiparimala/AgentProbe](https://github.com/venkatalakshmiparimala/AgentProbe)

- Built a 15-endpoint FastAPI backend that routes prompts across five LLM providers: Anthropic, OpenAI, Azure OpenAI, Groq, and Ollama.
- Scores LLM and RAG outputs on factual accuracy, hallucination rate, retrieval quality, completeness, and compliance using LLM-as-judge.
- Added CI regression tests with golden datasets; used it to evaluate LeaseI across 1,240+ test cases.
- Built three specialized LangGraph agents: an Orchestrator running an adaptive three-phase stress-test cycle (explore, target weak spots, verify failures), a RAG Tracer that localizes faults across a seven-stage retrieval pipeline (Query, Rewrite, Retrieve, Filter, Rerank, Context, Generate), and an Auto-Fix agent that proposes prompt rewrites, chunking adjustments, and query rewrites as candidate fixes for human review — never silently applied.
- Runs 100% locally at zero cost through Ollama, with no paid model APIs required.

### AI on FHIR — Clinical NLP & LLM API Integration
*Python, Flask, React, TypeScript, Docker, BERT, spaCy, LLMs, FHIR REST APIs*
[github.com/venkatalakshmiparimala/AI_on_FHIR](https://github.com/venkatalakshmiparimala/AI_on_FHIR)

- Built an app that turns English/Spanish questions into FHIR API calls using LLMs, BERT, and embeddings, cutting manual clinical lookup time by ~60%.
- Added role-based access control for HIPAA-style data isolation and containerized with Docker.

### CrashClarity — Road Accident Analysis (104K Records)
*Python, R, scikit-learn, GitHub Pages*

- Built an ML pipeline on 104K+ UK accident records using Random Forest and Logistic Regression (85%+ accuracy), with an interactive dashboard.

---

## Education

**M.S. Data Analytics Engineering** — George Mason University, Virginia | GPA 3.87 | May 2026

**B.Tech Computer Science & Engineering** — JNTU Anantapur | 2013–2017
