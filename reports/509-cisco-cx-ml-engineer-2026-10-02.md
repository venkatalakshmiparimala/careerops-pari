# Evaluation: Cisco — CX Machine Learning Engineer

**Date:** 2026-10-02
**URL:** https://jobs.cisco.com
**Archetype:** Agentic / Automation + AI Platform / LLMOps
**Score:** 4.3/5
**Legitimacy:** High Confidence
**PDF:** output/509-cisco-cx-ml-engineer-2026-10-02.pdf

---

## A) Role Summary

| Attribute | Detail |
|---|---|
| **Archetype** | GenAI / Agentic AI + LLMOps |
| **Domain** | Enterprise CX Platform — Cisco IQ |
| **Function** | Build RAG architectures, agentic workflows, LLMOps infrastructure, automated evaluation frameworks |
| **Seniority** | Experienced (7+ yr BS / 4+ yr MS) |
| **Location** | San Jose, CA — Hybrid (3 days/wk) |
| **Comp** | $203K–$258.6K base (San Jose) |
| **Sponsorship** | Not stated in JD; Cisco H-1B confirmed from prior eval |

---

## B) Match Analysis

### Strong Fits
- **GenAI/LLM/Agentic (preferred quals):** LeaseI = RAG architecture, agentic workflows, multi-agent orchestration, tool-use, context management, HITL — direct stack match
- **LLMOps / automated evaluation:** AgentProbe = model monitoring, automated evaluation frameworks, LLM-as-judge, CI regression harness — exact scope
- **LangChain/LangGraph explicitly named** ✅ (production LangGraph in LeaseI)
- **Claude/Claude Code explicitly named** as preferred qual ✅ — daily use
- **LangSmith** — in skills profile; AgentProbe covers the same observability scope
- **Python + Java** ✅ (both production)
- **AWS + Docker + Kubernetes + CI/CD** ✅
- **Cross-functional collaboration + mentoring** ✅ (Entrata: 5+ engineers, 300+ code reviews)

### Gaps
- **Model training at scale (PyTorch/TensorFlow production)** — GMU fine-tuned HuggingFace model + CrashClarity (Random Forest/scikit-learn/XGBoost) cover the minimum qual; not production-scale training
- **Kafka** — event-driven experience is RabbitMQ; Kafka listed in minimum data pipeline qual
- **Spark production** — in skills, not production-heavy
- **Relocation** — San Jose CA hybrid

---

## C) ATS Patches Applied

| Term | Added To |
|---|---|
| `LLMOps` | Summary, AgentProbe bullet |
| `context management` | LeaseI bullet |
| `model monitoring` | AgentProbe bullet |
| `automated evaluation frameworks` | AgentProbe bullet |
| `predictive models` | Skills tags + Entrata bullet |
| `responsible AI governance` | Summary + LeaseI |
| `low-latency model serving` | FastAPI/Magizhs bullet |

Post-patch ATS: ~95%

---

## D) Score Breakdown

| Dimension | Score | Notes |
|---|---|---|
| Role fit | 4.4 | GenAI/agentic/LLMOps = strong; ML training at scale is light |
| Domain | 3.8 | CX/enterprise platform, no Cisco domain exp |
| Location | 3.5 | San Jose CA hybrid, relocation needed |
| Comp | 5.0 | $203–258K base is exceptional |
| Sponsorship | 4.5 | Cisco H-1B confirmed from prior eval |
| **Weighted** | **4.3** | Apply |

---

## E) Recommendation

**Apply — 4.3/5.** Exceptional comp + confirmed Cisco H-1B tips this over the threshold. GenAI/agentic/LLMOps preferred quals are all strong matches. Model training gap is manageable given the role's heavy GenAI emphasis and the scikit-learn/XGBoost/GMU fine-tuning coverage.

---

## G) Posting Legitimacy

**Tier: High Confidence** — Cisco active careers page, application window 12/30/2026, specific team and comp range disclosed.

---

## Machine Summary

```yaml
company: Cisco
role: CX Machine Learning Engineer
archetype: agentic_ai_llmops
score: 4.3
apply: true
location: San Jose CA hybrid
sponsorship: cisco_h1b_confirmed
comp_range: 203k-258k
key_match: leaseI_agentic_rag + agentprobe_llmops + claude_code_preferred + langgraph_named
gaps: [ml_training_scale, kafka, spark_production, relocation_sj]
ats_coverage: 95pct
report: 509-cisco-cx-ml-engineer-2026-10-02.md
```
