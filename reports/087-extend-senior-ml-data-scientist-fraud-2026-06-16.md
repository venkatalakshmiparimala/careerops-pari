# Evaluation: Extend — Senior Machine Learning Data Scientist (Fraud & ML)

**Date:** 2026-06-16
**URL:** https://job-boards.greenhouse.io/extend/jobs/5997157004
**Archetype:** ML Engineer / Fraud ML
**Score:** 4.5/5
**Legitimacy:** High Confidence
**PDF:** /Users/Parimala/career-ops/output/cv-extend-senior-ml-fraud-2026-06-16.pdf

---

## A) Role Summary

- **Archetype:** Senior ML Data Scientist — Fraud Detection & ML
- **Domain:** Fraud ML models: full lifecycle (requirements → experimentation → production → monitoring)
- **Seniority:** Senior (3+ years in production ML)
- **Location:** Remote, US (continental US required)
- **TL;DR:** Extend needs a Senior ML Data Scientist to own the full model lifecycle for fraud detection. Build and deploy production ML models, design feature engineering pipelines, monitor for data drift, partner with fraud ops. Stack: Python, SQL, PyTorch, scikit-learn, XGBoost, AWS SageMaker (preferred). Fraud detection preferred but not required. $135K–$165K remote. This is the closest structural match to Parimala's ML skill set across all 7 roles.

---

## B) Match with CV

| JD Requirement | CV Evidence | Strength |
|---|---|---|
| 3+ years building and deploying production ML systems | 8+ years total; 1 year GMU ML research + 8 years production engineering at scale; CrashClarity, Real Estate, Isolation Forest projects | Strong |
| Strong proficiency in Python and SQL | 8+ years Python production; 200+ SQL queries tuned; PostgreSQL/MySQL expert | Strong |
| PyTorch, scikit-learn, XGBoost (hands-on) | PyTorch, scikit-learn, XGBoost all listed in cv.md technical skills; used in projects | Strong |
| ML fundamentals: model selection, evaluation, feature engineering | CrashClarity (RF + LR, feature engineering, 85%+ accuracy), Real Estate (XGBoost, 20+ variables), GMU regression (R²=0.977) | Strong |
| Own model lifecycle: requirements → experimentation → model cards | AgentProbe 5-metric eval engine + CI/CD gates; GMU research pipelines with full lifecycle | Strong |
| Design and maintain feature engineering pipelines | CrashClarity feature engineering; Real Estate XGBoost features; Entrata data transformation pipelines | Strong |
| Monitor production model quality, data drift, retraining | AgentProbe regression drift tracking; CI/CD eval gates blocking failing runs | Strong |
| Fraud detection or risk assessment (preferred) | Isolation Forest fraud-signal detection at GMU; CrashClarity multi-factor pattern detection | Strong (preferred met) |
| AWS SageMaker (preferred) | AWS S3, EC2, RDS, Glue experience; no SageMaker specifically | Partial |
| Graph-based models PyTorch Geometric (preferred) | No graph ML experience | Gap |
| Model monitoring tools Arize (preferred) | No Arize experience | Gap |
| Attention to detail, user behavior/fraud pattern understanding | Isolation Forest caught anomalies manual review missed; CrashClarity behavioral pattern detection | Strong |
| Collaborative team player | 300+ code reviews, 120+ Agile sprints, cross-functional delivery | Strong |

**Key Gaps:**
- AWS SageMaker (knows AWS broadly, not SageMaker specifically)
- Graph-based ML (PyTorch Geometric) — preferred, not required
- Arize or similar model monitoring tools — preferred, not required
- All gaps are "preferred" not "required" — not disqualifying

**Strengths are exceptional:**
- All 4 required skills have direct, metric-backed evidence
- Fraud detection preferred requirement is met by Isolation Forest
- MS Data Analytics Engineering = exact academic background
- 8+ years production systems engineering = operational rigor for ML deployment

---

## C) Level and Strategy

**Seniority match:** Strong. 3+ years required; Parimala has 8+ years of production engineering and 1+ year of applied ML research. The ML models she's built (Isolation Forest, Random Forest, XGBoost, Logistic Regression, regression at R²=0.977) directly demonstrate the required fundamentals.

**Positioning strategy:**
- This is the highest-confidence role in the batch — position as a full-stack ML engineer who owns the end-to-end model lifecycle
- Lead with the CrashClarity + GMU ML credentials as production-grade ML proof
- Emphasize the model monitoring and drift detection angle via AgentProbe (regression drift tracking, CI/CD eval gates)
- Fraud detection preferred: lead with Isolation Forest anomaly detection → direct fraud signal detection methodology
- The role is "fraud & ML" — not requiring prior fraud ops experience, just ML applied to fraud patterns

---

## D) Comp and Demand

- **Posted salary:** $135,000–$165,000/year salaried + stock options + medical/dental/vision + flexible PTO
- **Assessment vs. comp target:** Above Parimala's $100K–$140K target range — top of range at $165K is excellent. Floor at $135K is already above target.
- **Market validation:** Senior ML Data Scientist (fraud, remote, fintech startup) runs $130K–$175K (Levels.fyi, Glassdoor 2025–2026) — Extend's range is consistent.
- **H-1B sponsorship:** Same as Extend Lead role — funded fintech startup, likely sponsors but unconfirmed. Same company = one ask covers both applications.

---

## E) Customization Plan

1. **Professional Summary:** "ML engineer and data scientist with 8+ years building production systems and ML pipelines. Built Isolation Forest anomaly detection at GMU (cut manual QA 70%); Random Forest + Logistic Regression on 104K records (85%+ accuracy); XGBoost risk factor segmentation. Expert in Python, SQL, PyTorch, and scikit-learn. M.S. Data Analytics Engineering, GMU (GPA 3.87). Ready to own the full ML model lifecycle in fraud detection."
2. **GMU Research bullet:** Lead with "built and deployed Isolation Forest anomaly detection across 3 pipelines — fraud-signal detection methodology"
3. **AgentProbe:** Emphasize the model lifecycle: requirements → eval engine design → CI/CD integration → regression drift monitoring — maps directly to the JD's model lifecycle ownership requirement
4. **Projects:** CrashClarity (production-ready ML pipeline, 85%+ accuracy, feature engineering), GMU anomaly detection, Real Estate XGBoost — all 3 projects demonstrate model lifecycle ownership
5. **Skills:** Lead with PyTorch, scikit-learn, XGBoost, Python, SQL — mention SageMaker familiarity via AWS experience

---

## F) Interview Plan

**STAR+R Stories:**

1. **GMU Isolation Forest → Fraud pattern detection pipeline**
   - S: 3 research pipelines with manual QA bottleneck; unknown anomaly distribution
   - T: Build unsupervised detection system from scratch with no labeled training data
   - A: Implemented Isolation Forest, tuned contamination hyperparameter, integrated with data pipeline
   - R: Cut manual QA 70%; surfaced anomalies missed by domain experts
   - **Reframe:** "Unsupervised anomaly detection from scratch is the same core challenge as fraud detection in cold-start scenarios."

2. **CrashClarity model lifecycle → End-to-end ML ownership**
   - S: 104K+ multi-source records; no pre-existing model; multiple interacting factors
   - T: Full model lifecycle: problem framing → feature engineering → model selection → evaluation → deployment
   - A: Feature engineering across weather/road/time, Random Forest vs. LR comparison, hyperparameter tuning, GitHub Pages deployment
   - R: 85%+ accuracy; interactive stakeholder dashboard; reproducible codebase

3. **AgentProbe eval engine → Model monitoring and drift detection**
   - S: Agent AI test runs producing inconsistent outputs; no automated quality gates
   - T: Build monitoring system that catches regression drift before production
   - A: 5-metric LLM-as-judge eval engine; CI/CD integration; per-run metrics and regression drift tracking via ChromaDB
   - R: Failing runs blocked automatically; regression drift surfaced per test run
   - **Reframe:** "Same infrastructure pattern as production ML monitoring — track model quality, detect drift, block degraded versions."

4. **Real Estate XGBoost → Feature engineering for risk models**
   - S: 20+ socioeconomic variables with complex interactions; risk prediction for property pricing
   - T: Identify and engineer the most predictive feature set
   - A: Feature importance analysis with XGBoost; correlation analysis; polynomial features; model comparison vs. Random Forest baseline
   - R: Key risk predictors identified; model ready for segmentation use

5. **Entrata Python/AI pipelines → Production ML deployment on regulated data**
   - S: 1.6M financial records requiring AI-powered transformation with correctness guarantees
   - T: Build reliable, auditable ML pipeline on regulated financial data
   - A: Python pipeline with output validation, quality gates, error escalation; PHI compliance throughout
   - R: Zero compliance incidents; production AI on regulated data

6. **AgentProbe multi-provider routing → Model selection and evaluation**
   - S: Different tasks required different LLM providers (Anthropic vs. OpenAI vs. Groq vs. Ollama) with different accuracy/cost tradeoffs
   - T: Build intelligent model routing that selects optimal model per task type
   - A: Built LLM Router with dynamic routing based on task complexity, latency, and quality metrics
   - R: 100% local at zero cost; same evaluation discipline applies to ML model selection for fraud detection

---

## G) Posting Legitimacy

- **Company:** Extend — same as Job 5 analysis. YC-backed insurance-as-a-service, Series C. Legitimate employer, real product.
- **Posting freshness:** Greenhouse URL live (confirmed). Active posting.
- **H-1B sponsorship:** Unconfirmed. Same company as Job 5. One verification covers both.
- **Concerns:** No disqualifying concerns. This is a strong-fit role with clean requirements.
- **Verdict:** High Confidence — strongest technical fit in this batch. Apply. Score: 4.5/5 (approaching 4.5 threshold for draft application answers below).

---

## Keywords Extracted

ML model lifecycle, fraud detection, feature engineering, model monitoring, data drift, production ML, Python, SQL, PyTorch, scikit-learn, XGBoost, AWS SageMaker, model cards, experimentation, fraud pattern detection, risk assessment, retraining, model evaluation, model quality, graph ML, PyTorch Geometric, Arize, fraud operations partnership

---

## H) Draft Application Answers

*(Score >= 4.5 — draft answers included)*

**Q: Why are you interested in this role at Extend?**
> "Extend is at the intersection of two things I find genuinely interesting: production ML systems and financial risk. This role is one of the few that asks for the full model lifecycle — not just building models, but owning requirements, experimentation, monitoring, and retraining. That matches exactly how I've worked. At GMU, I built an Isolation Forest anomaly detection system from scratch across 3 research pipelines — designed the contamination threshold, integrated it into the data workflow, and tracked its outputs. At Entrata, I applied Python ML pipelines to 1.6M financial records with quality gates and zero compliance incidents. I want to bring that production-grade ML discipline to fraud detection at Extend."

**Q: Describe your experience with the ML model lifecycle.**
> "I own the complete lifecycle across my projects. For CrashClarity: framed the prediction problem, engineered features across weather/road/time variables, ran Random Forest vs. Logistic Regression with cross-validation, evaluated with precision/recall/F1, and deployed an interactive GitHub Pages dashboard. For AgentProbe: designed the evaluation criteria (5 metrics), built an LLM-as-judge evaluation engine, integrated CI/CD gates that block failing runs automatically, and track per-run drift via ChromaDB. For GMU research: built Isolation Forest from scratch, tuned hyperparameters, validated outputs against manual review ground truth, and cut QA time by 70%. I treat every project as production — documented, reproducible, monitored."

**Q: What's your experience with fraud or risk detection?**
> "Directly: I built Isolation Forest anomaly detection at GMU — an unsupervised system that flags behavioral deviations from expected patterns, which is mechanistically identical to fraud signal detection. It surfaced anomalies that expert manual review missed. For CrashClarity, I built a multi-factor classifier (85%+ accuracy on 104K records) distinguishing incident patterns across correlated variables — the same multi-signal fusion challenge that appears in fraud detection. I haven't yet held a formal 'fraud analyst' title, but I've built the core technical systems: unsupervised anomaly detection, supervised classification at scale, and production pipelines with quality gates on regulated financial data."

---

## Machine Summary

```yaml
company: Extend
role: Senior Machine Learning Data Scientist (Fraud & ML)
score: 4.5
archetype: ML Engineer / Fraud ML
location: Remote, US
remote: true
salary_range: "$135K–$165K"
h1b_sponsor: unconfirmed (verify required — same company as Job 5)
visa_risk: medium
gap_flags:
  - AWS SageMaker (knows AWS broadly, not SageMaker specifically)
  - no PyTorch Geometric graph ML experience
  - no Arize model monitoring tool experience
strengths:
  - full ML model lifecycle ownership (CrashClarity, GMU, AgentProbe)
  - Isolation Forest fraud-signal detection (preferred requirement met)
  - PyTorch + scikit-learn + XGBoost all hands-on
  - 8+ years production engineering adds deployment credibility
  - MS Data Analytics Engineering exact degree match
  - remote role ideal
  - salary above target
recommendation: apply — highest-fit role in batch
```
