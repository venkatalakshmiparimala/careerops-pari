# Venkata Lakshmi Parimala Pasupuleti

venkatalakshmiparimala@gmail.com | +1-703-261-5410 | Fairfax, Virginia 22030
[LinkedIn](https://www.linkedin.com/in/venkata-lakshmi-parimala) | [GitHub](https://github.com/venkatalakshmiparimala) | [Portfolio](https://venkatalakshmiparimala.github.io/Portfolio/about.html)

---

## Professional Summary

Python software engineer with 7+ years of experience, now focused on building LLM, RAG, and AI agent applications on top of strong backend, API, and data pipeline experience. Built two AI projects: LeaseI, an 8-agent LangGraph app with hybrid-search RAG, cited answers, and human escalation, and AgentProbe, an open-source LLM evaluation toolkit that works with five LLM providers. Currently integrating Anthropic Claude into financial applications at Intuit. Spent 7+ years at Entrata, a multi-tenant SaaS platform with 100K+ monthly active users, building Python/SQL data pipelines, async processing, and AWS integrations. M.S. in Data Analytics Engineering from George Mason University (GPA 3.87, May 2026).

---

## Technical Skills

**AI & LLMs:** LLM APIs (Anthropic Claude, OpenAI, Azure OpenAI, Groq, Ollama), RAG Pipelines, Hybrid Search, Embeddings, Prompt Engineering, AI Agents, LangGraph, LangChain, Human-in-the-Loop, LLM-as-Judge Evaluation, MCP

**Vector Search & NLP:** ChromaDB, Pinecone, Weaviate, Elasticsearch, Semantic Search, BERT, spaCy, HuggingFace

**Python & ML:** Python (9+ yrs), FastAPI, Flask, Django, Pandas, NumPy, scikit-learn, XGBoost, PyTorch, PySpark

**Other Languages & Web:** Java, Spring Boot, TypeScript, JavaScript, Node.js, React, Redux, PHP, Laravel, C#, .NET, Kotlin, Scala, GraphQL, SQL, PL/SQL, Bash

**Databases & Data:** PostgreSQL, MySQL, Oracle, Redis, MongoDB, SQLite, Snowflake, ETL Pipelines, Data Modeling, Query Optimization, Stored Procedures

**Cloud & DevOps:** AWS (S3, EC2, RDS, Lambda, Glue, SQS, API Gateway, IAM), Azure (OpenAI, Data Factory, Databricks, AKS), GCP (Vertex AI), Docker, Kubernetes, Terraform, GitHub Actions CI/CD

**Messaging & Monitoring:** RabbitMQ, Kafka, Celery, Prometheus, Grafana, OpenTelemetry

**Practices:** REST APIs, Microservices, OAuth, Agile/Scrum, TDD, Code Review, HIPAA/PHI Compliance, Observability

---

## Experience

### Software Engineer — Intuit
*Jun 2026 – Present · Virginia, USA*

- Serve as **technical point of contact for AI tool vendors and business stakeholders**: scope integration requirements, evaluate third-party APIs, align on data contracts and implementation approach, and drive each initiative from technical discovery through go-live.
- Partner with TPMs and product managers to translate ambiguous business requirements into concrete technical solutions; own the delivery timeline and keep stakeholders aligned on tradeoffs and progress.
- Integrate Anthropic Claude into Python/FastAPI services for financial data summaries, natural-language queries, and reporting.
- Build evaluation and regression tests for LLM outputs (LLM-as-judge and golden datasets) to catch hallucinations and quality drops before release; set expectations with business stakeholders on AI accuracy and edge cases.
- Build ML pipelines in Python with scikit-learn and XGBoost, from data ingestion and feature engineering to model evaluation and prediction APIs.
- Add guardrails around LLM calls, including input validation, sensitive-data handling, and fallbacks when model output fails checks.
- Containerize services with Docker and ship them through GitHub Actions CI/CD to AWS, with logging and monitoring for production visibility.

### Senior Software Engineer — Entrata (Apartment & Affordable Housing SaaS)
*Oct 2020 – Jul 2024 · Multi-tenant platform with 100K+ monthly active users*

- **Served as the primary technical contact for external vendor integrations**: worked directly with HUD and Tax Credit federal data source teams to scope data requirements, debug API and data issues, coordinate go-live timelines, and resolve production incidents — end to end, without a handoff.
- Collaborated with product managers and TPMs across 120+ Agile sprints to translate client-reported issues and business requirements into scoped technical solutions; led triage calls, wrote root cause summaries for non-technical stakeholders, and drove fixes to closure.
- Delivered 20+ features end-to-end (Python, PHP, Java, JavaScript, React, PostgreSQL); built internal debugging tools that reduced customer issue triage time by 40%.
- Built a RabbitMQ-based async processing system for rent updates across thousands of tenant records, with retry logic to prevent double processing.
- Wrote Python/Bash automation that cut manual operational work by 80%; optimized 200+ SQL queries (30% performance gain).
- Worked on a Docker microservices redesign (50% better scalability, 30% faster deployments) and the AWS S3 document migration, including Libsodium encryption for resident PHI.
- Reviewed 300+ pull requests, mentored junior engineers.

### Junior Software Engineer — Entrata India
*Sep 2018 – Oct 2020 · Pune, India*

- Built property management modules (Python, PHP, Java, PostgreSQL) for affordable housing and rental management.
- Delivered large-scale data import and reconciliation workflows (1.6M HUD/Tax Credit records).
- Led AWS S3 cloud migration from legacy server storage; created 56 state-specific housing certification documents.

---

## Projects

### LeaseI — Multi-Agent AI Platform with RAG
*Python, LangGraph (8-agent), FastAPI, hybrid retrieval (TF-IDF + semantic), OCR, SQLite, CI/CD*
[github.com/venkatalakshmiparimala/Lease_complaince_rag](https://github.com/venkatalakshmiparimala/Lease_complaince_rag)

- Built a lease-compliance app in Python where an 8-agent LangGraph workflow (triage, retrieval, reasoning, validation) investigates issues and escalates to a human when confidence is low.
- Built the RAG pipeline: OCR ingestion, section-aware chunking, hybrid search (TF-IDF + semantic reranking), and answers cited to the exact source clause.
- Added guardrails in code so eligibility and financial decisions always route to staff instead of the LLM.
- Tested with an LLM-as-judge CI harness: 93.6% precision and 87.9% F1 across 1,240 test cases.

### AgentProbe — Open-Source LLM Evaluation Toolkit
*Python, FastAPI, LangGraph, ChromaDB, GitHub Actions, Anthropic, OpenAI, Azure OpenAI, Groq, Ollama*
[github.com/venkatalakshmiparimala/AgentProbe](https://github.com/venkatalakshmiparimala/AgentProbe)

- Built a 15-endpoint FastAPI backend that routes prompts across five LLM providers: Anthropic, OpenAI, Azure OpenAI, Groq, and Ollama.
- Scores LLM and RAG outputs on factual accuracy, hallucination rate, retrieval quality, completeness, and compliance using LLM-as-judge.
- Added CI regression tests with golden datasets; used it to evaluate LeaseI across 1,240+ test cases.

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
