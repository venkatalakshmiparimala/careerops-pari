# Evaluation: GitHub — Machine Learning Engineer (Safety & Integrity)

**Date:** 2026-08-11
**URL:** https://www.github.careers/careers-home/jobs/5507?jr_id=6a762ef57b3417772ade726a
**Archetype:** Applied AI Engineer + ML Engineer (Trust & Safety)
**Score:** 4.0/5
**Legitimacy:** High Confidence
**PDF:** ❌

---

## A) Role Summary

| Dimension | Details |
|-----------|---------|
| **Archetype** | Applied AI Engineer + ML Engineer (Trust & Safety) |
| **Team** | Safety & Integrity — fighting malware, spam, fraud, fake accounts, inauthentic content |
| **Domain** | Online platform trust & safety via ML/AI — classification, detection, LLM-assisted moderation |
| **Function** | Build production-grade ML classification and detection systems; evaluate and deploy agentic safety pipelines |
| **Seniority** | Mid (IC2/IC3 equivalent — no "Senior" in title; broad salary band spans multiple levels) |
| **Work model** | Remote — United States |
| **Comp** | $107,700–$285,900 base (broad band); mid-level likely $150–$180K base + RSUs |
| **Sponsorship** | YES — Microsoft/GitHub is a top-5 H-1B sponsor |
| **TL;DR** | Build ML systems that fight fraud, spam, and malware on GitHub's platform — classification at scale + LLM-as-judge evals for AI safety. Remote US, top H-1B sponsor, exceptional comp ceiling. Core gap: online platform T&S is not in background, but fraud/anomaly detection framing bridges it. |

---

## B) Match with CV

| JD Requirement | CV Evidence | Match |
|----------------|-------------|-------|
| Strong software engineering + AI coding assistants | 8yr Entrata production code (PHP, Python, JS/TS, PostgreSQL, RabbitMQ); 120+ Agile sprints | ✅ Strong |
| Designing/evaluating **agentic systems** (tool-use loops, multi-step workflows, LLM-as-judge) | AgentProbe: 3-agent LangGraph runtime (Orchestrator, RAG Tracer, Auto Fix); CI-integrated LLM-as-judge eval pipeline (5-metric: factual accuracy, hallucination, retrieval, completeness, compliance) | ✅ Direct |
| Classification/detection systems at scale — imbalanced data, precision/recall tradeoffs | LeaseI: 93.6% precision, 87.9% F1 on 1,240 lease PDFs; CrashClarity: 85%+ accuracy (Random Forest + Logistic Regression on 104K accident records) | ✅ |
| **Fraud / spam / malware / threat actor activity** experience | 8yr income fraud detection at Entrata: fake paystubs, income misrepresentation, household-composition fraud in LIHTC/HCV/HUD portfolios; Isolation Forest on 3 GMU research pipelines (anomaly detection surfacing anomalies manual review missed) | ⚠️ Adjacent — property management fraud ≠ online platform abuse, but anomaly detection framing is shared |
| ML algorithms: supervised + unsupervised, anomaly detection | Isolation Forest (GMU), Random Forest, Logistic Regression, XGBoost (CrashClarity), LeaseI classification | ✅ |
| LLM foundation, working knowledge of LLMs | LeaseI (8-agent LangGraph + LLM reasoning pipeline); AgentProbe (multi-provider LLM routing: Anthropic, OpenAI, Groq, Ollama) | ✅ Strong |
| Production ML systems running against high-volume event streams | Entrata: 1.6M records processed (batch, not real-time stream) | ⚠️ Partial — batch vs stream |
| Responsible AI / Safety-by-Design | LeaseI core design rule: LLM reasons, human or deterministic logic makes every final regulated call; HITL escalation; guardrails; citation enforcement; zero auto-resolved eligibility decisions | ✅ Direct |
| Collaboration with AI/Copilot teams | TA workshops on AI applications (600+ students); cross-functional delivery at Entrata | ✅ Soft |

### Gaps

| Gap | Severity | Mitigation |
|-----|----------|------------|
| Online platform T&S (spam, malware, fake accounts, bot detection) — not in background | Medium — preferred specialty, not a 10-yr hard req | Frame Entrata fraud detection as the same paradigm (pattern classification on structured behavioral signals); Isolation Forest = anomaly detection; income fraud detection = financial signal abuse. Same ML problem space, different domain. |
| Real-time stream classification at scale (Kafka-style) | Soft | RabbitMQ at Entrata shows event-driven architecture; batch pipelines on 1.6M records are adjacent; note as ramp area |
| Security research / threat intelligence background | Soft — preferred, not stated as required | No mitigation needed if T&S is framed as fraud/anomaly, which it explicitly lists |

---

## C) Level and Strategy

**Level:** Mid-level MLE (IC2/IC3 at GitHub/Microsoft). The broad salary band ($107K–$285K) spans junior-to-senior; no "Senior" in title. This is the right level for Parimala — avoids the Staff/Principal block, competes in a mid-level pool where her 8yr depth is an asset.

**Sell the match:**
- "I've built the two things this role requires: (1) agentic evaluation systems — AgentProbe's LLM-as-judge pipeline scores every agent run on factual accuracy, hallucination, retrieval quality, completeness, and compliance; (2) classification/detection at scale — LeaseI achieves 93.6% precision classifying compliance decisions across 1,240 lease documents."
- "My fraud detection background at Entrata is directly relevant — 8 years detecting income misrepresentation, fake paystubs, and household-composition fraud in regulated housing portfolios. The ML problem is identical: build a classifier that catches adversarial behavior in structured signals."
- Lead with AgentProbe's LLM-as-judge eval — this maps exactly to the "evaluating agentic systems" requirement.

**T&S domain gap:**
> "I haven't worked on online platform trust & safety specifically, but the ML problem is the same: build classifiers over behavioral signals to catch adversarial patterns. At Entrata I did this on financial signals (fake income documentation). I'd ramp on the platform-specific signal types quickly because the anomaly detection tooling is identical."

---

## D) Comp and Demand

| Metric | Value |
|--------|-------|
| Base range (posted) | $107,700–$285,900 (US remote) |
| Expected mid-level base | ~$150K–$180K (IC3 equivalent) |
| Estimated TC (base + RSU + bonus) | ~$180K–$250K at mid-level |
| Market context | MLE median TC (levels.fyi 2026): $264K across all levels |
| Parimala target | $80K–$140K base |
| Score vs target | 5/5 — far exceeds target even at low end |

**Demand:** GitHub Safety & Integrity is actively hiring despite Microsoft's 2026 restructuring. AI/Copilot teams are explicitly exempt from the March 2026 hiring freeze. Safety ML is a growth area (regulatory pressure on platforms + GenAI content moderation). This team has real exec visibility and budget.

**Microsoft restructuring context:** Microsoft cut 25K+ jobs since May 2025, but those are generalist infrastructure/enterprise/sales roles. AI-adjacent engineering (Copilot, Safety, Azure OpenAI) is protected and growing. GitHub India Engineering was cut; US teams are continuing.

---

## E) Customization Plan

| # | Section | Change | Why |
|---|---------|--------|-----|
| 1 | **Summary** | Lead with: fraud/anomaly detection framing + agentic evaluation systems + classification at scale | Mirrors the two primary JD requirements |
| 2 | **AgentProbe bullets** | Lead with LLM-as-judge eval pipeline: "Designed and evaluated agentic systems — CI-integrated LLM-as-judge pipeline scoring every run on factual accuracy, hallucination, retrieval, completeness, compliance" | Direct match to "evaluating agentic systems (tool-use loops, LLM-as-judge)" requirement |
| 3 | **Research Associate bullet** | Lead with Isolation Forest: "Applied Isolation Forest to automate anomaly detection across 3 research pipelines — surfaced anomalies manual review missed, improved downstream model reliability" | Maps to anomaly detection + unsupervised ML requirement |
| 4 | **Entrata bullets** | Surface income fraud detection explicitly: "Automated income eligibility verification and fraud detection across 8yr of LIHTC/HCV/HUD portfolios — detecting fake paystubs, income misrepresentation, household-composition fraud" | Establishes fraud domain credibility |
| 5 | **LeaseI bullets** | Lead with classification: "Built classification pipeline (93.6% precision, 87.9% F1) over 1,240 lease documents — precision/recall tradeoffs enforced in eval harness with multi-trial sampling and regression gate" | Maps to "precision/recall tradeoffs" requirement |
| 6 | **Skills** | Add: "Anomaly Detection, Isolation Forest, Classification Systems, Trust & Safety" explicitly | Keyword match |

---

## F) Interview Plan

| # | JD Requirement | Story | S | T | A | R | Reflection |
|---|---------------|-------|---|---|---|---|------------|
| 1 | Evaluating agentic systems (LLM-as-judge) | **AgentProbe 5-metric eval engine** | Production LLM agents fail silently — bad outputs with no error signal are the hardest problem | Build automatic quality gates scoring every agent run before merge | LLM-as-judge: factual accuracy, hallucination, retrieval, completeness, compliance; CI-integrated; regressions block merge | Zero manual QA per run; failing agents caught before production | LLM evaluation is an engineering discipline: consistent rubrics, multi-trial sampling, regression gates — not vibes-based review |
| 2 | Classification/detection + precision/recall tradeoffs | **LeaseI classification pipeline** | Compliance decisions in regulated housing have zero tolerance for false negatives — must distinguish "answer is known" from "answer is uncertain" | Build classifier that distinguishes confident from uncertain outputs with controlled precision/recall | TF-IDF retrieval + LLM reasoning; confidence scoring; pass@k harness with multi-trial sampling; HITL escalation when confidence below threshold | 93.6% precision, 87.9% F1, pass@1 81.7%; zero unsupported answers served to end users | Precision/recall tradeoffs in high-stakes domains must be decided at design time, not tuned after deployment |
| 3 | Fraud / anomaly detection | **Entrata 8yr income fraud detection + GMU Isolation Forest** | LIHTC/HCV/HUD portfolios are targets for income misrepresentation — fake paystubs, household-composition fraud, AMI threshold gaming | Build automated detection replacing manual review workflows | Section 8/HCV, LIHTC, HUD compliance modules with automated AMI threshold validation + Isolation Forest at GMU surfacing anomalies manual review missed | Zero compliance violations; anomalies surfaced that manual review missed across 3 pipelines | Fraud detection in structured domains is a classification problem — the signal types differ between financial records and platform events, but the anomaly detection approach (Isolation Forest, supervised classifiers on labeled abuse patterns) is identical |
| 4 | Production ML systems at scale | **Entrata AI pipeline on 1.6M records** | Manual Excel-based income limit processing — 1.6M records, no audit trail, error-prone | Replace with production AI pipeline | Python + PyTorch + OpenAI API; output validation gates; quality controls at launch | 100% production delivery, zero compliance incidents | The hardest part of productionizing ML is the validation layer, not the model — same principle applies to safety classifiers |
| 5 | Responsible AI / Safety-by-Design | **LeaseI core design rule** | Regulated housing decisions (eligibility, income, rent) cannot be auto-resolved by AI — legal and compliance exposure is real | Build system where AI reasons but human or deterministic logic makes every final call | Core rule enforced in code everywhere: HITL escalation for low-confidence; every answer cited to source clause or explicitly downgraded; Tenant agent never auto-resolves eligibility questions | 100% citation correctness on Phase 1 eval set; zero auto-resolved regulated decisions | Safety-by-Design is an architecture decision, not a prompt engineering trick — constraints must be enforced in code, not system message |

**Case study to present:** AgentProbe's LLM-as-judge evaluation pipeline. Show the 5-metric eval running on an agent — score, per-metric breakdown, regression detection. This is exactly "evaluating agentic systems" in the JD.

**Red-flag questions:**
- *"You don't have T&S platform experience — why apply?"* → "The ML problem is identical: build classifiers over behavioral signals to detect adversarial patterns. At Entrata I did this on financial signals for 8 years — detecting fake income documentation in regulated housing portfolios. The domain differs; the anomaly detection approach (Isolation Forest, precision/recall tradeoffs, confidence scoring) is the same. I'd ramp on platform signal types quickly."
- *"Have you worked with high-volume event streams?"* → "My production systems processed 1.6M records — batch, not real-time streams. I've designed event-driven architectures with RabbitMQ. Real-time stream classification at Kafka scale is a gap I'm actively addressing, but the ML classification logic doesn't change at higher throughput."

---

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|--------|---------|--------|
| Source | Official github.careers domain, specific job ID 5507 | Positive |
| Apply button | Active at time of submission | Positive |
| Team | Safety & Integrity — active GitHub division with growing AI investment | Positive |
| JD specificity | Named paradigms (LLM-as-judge, tool-use loops, imbalanced data, precision/recall tradeoffs) — not boilerplate | Positive |
| Comp disclosed | $107,700–$285,900 explicitly | Positive |
| Microsoft restructuring | 2026 layoffs affecting generalist/enterprise roles; AI/Safety teams explicitly exempt from hiring freeze | Neutral (favorable for this team) |
| GitHub India cut | US teams continuing; Safety & Integrity appears to be US-based role | Neutral |
| Sponsorship | Microsoft top-5 H-1B sponsor; role open to US candidates on OPT | Positive |

---

## Keywords Extracted

machine learning engineer, trust and safety, fraud detection, spam, malware, classification systems, detection systems at scale, agentic systems, tool-use loops, LLM-as-judge evaluation, anomaly detection, imbalanced data, precision/recall, supervised learning, unsupervised learning, responsible AI, safety by design, LLM, production ML, GitHub, Safety and Integrity, content moderation

---

## Machine Summary

```yaml
report: 199
company: GitHub
role: Machine Learning Engineer (Safety & Integrity)
score: 4.0
archetype: Applied AI Engineer + ML Engineer (Trust & Safety)
location: Remote USA
comp_base: "$107,700–$285,900 (mid-level ~$150-180K)"
sponsorship: confirmed (Microsoft/GitHub top-5 H-1B sponsor)
legitimacy: High Confidence
recommend: strategic apply — below 4.5 general threshold but fraud/anomaly+sponsorship+remote+comp make it worth pursuing
threshold_used: "4.5+ (non-PropTech general threshold); 4.0 score = just below"
key_gap: Online platform T&S (spam/malware/fake accounts) — not in background; batch vs stream at scale
key_strength: AgentProbe LLM-as-judge eval = direct match to "evaluating agentic systems"; 8yr Entrata fraud detection; LeaseI 93.6% precision
action_before_apply: Tailor CV with fraud/anomaly framing + AgentProbe eval lead story; add Isolation Forest + anomaly detection explicitly
```
