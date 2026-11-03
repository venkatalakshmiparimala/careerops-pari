# Evaluation: Grafana Labs — Senior Software Engineer, GenAI & ML Evaluation Frameworks

**Date:** 2026-06-11
**URL:** https://job-boards.greenhouse.io/grafanalabs/jobs/5559973004
**Archetype:** AI Platform / LLMOps
**Score:** 4.2/5
**Legitimacy:** High Confidence
**PDF:** output/cv-grafana-labs-genai-ml-eval-2026-06-11.pdf

---

## A) Role Summary

| Field | Detail |
|-------|--------|
| Archetype | AI Platform / LLMOps — GenAI Eval Infrastructure |
| Domain | LLM evaluation frameworks, automated eval pipelines, regression tracking, CI/CD integration |
| Function | Build (eval infrastructure + cross-team enablement) |
| Seniority | Senior IC |
| Remote | Remote US |
| Comp | $154,445–$185,334 base (US) |
| TL;DR | Design and scale automated evaluation pipelines for Grafana's GenAI/LLM systems. Build golden test sets, regression tracking, LLM-as-judge methods, integrate into CI/CD, define quality metrics, and guide teams across Grafana in GenAI eval best practices. |

---

## B) Match with CV

| JD Requirement | CV Match | Strength |
|----------------|----------|----------|
| Design + implement eval frameworks for AI/ML systems | AgentProbe: 5-metric LLM-as-judge eval engine, per-run scoring, regression detection | ✅ Direct proof |
| LLM-as-judge methods | AgentProbe: LLM-as-judge is the core eval mechanism across all 5 metrics | ✅ Direct proof |
| Automated evaluation pipelines | AgentProbe: fully automated eval runs — no manual intervention per cycle | ✅ Direct proof |
| Regression tracking | AgentProbe: anomaly flags surface regressions before they compound; trend tracking across runs | ✅ Direct proof |
| CI/CD integration of eval | AgentProbe: GitHub Actions CI/CD integrates eval into every build | ✅ Direct proof |
| Prompt engineering + structured output evaluation | AgentProbe: prompt engineering + 5-metric structured scoring per run | ✅ Direct proof |
| Context-window management in LLM systems | AgentProbe: multi-provider routing; manages context across Anthropic, OpenAI, Groq, Ollama | ✅ Strong |
| Golden test sets + dataset management | AgentProbe: eval benchmark runs across fixed prompt/retrieval sets | ✅ Adjacent |
| Python production | 8+ years Python at Entrata + AgentProbe FastAPI | ✅ Exceeds |
| Open-source orientation | AgentProbe is fully open-source with public GitHub | ✅ Cultural fit |
| Guide teams in GenAI eval best practices | Not directly demonstrated; TA at GMU + AgentProbe documentation | ⚠️ Soft gap |
| Grafana/observability tooling | No Grafana, Prometheus, Loki, or Tempo experience | ⚠️ Tool gap |
| Go language | Grafana's codebase is heavily Go — not in CV | ⚠️ Possible gap |
| H-1B | Grafana Labs is a global remote-first company; likely sponsors — verify | ⚠️ Confirm |

**Gaps and mitigations:**
- **Grafana tooling** — Grafana is an observability company; knowing Grafana dashboards/Prometheus is relevant. This role is on the AI/ML team and focused on eval frameworks — Python/LLM tooling is the core. Observability concepts transfer from AgentProbe's dashboard + trace enrichment.
- **Go** — Grafana's platform is Go-heavy but the AI/ML eval layer is likely Python-first. Frame as: *"My eval framework work is Python. Is Go required for this specific AI/ML eval role, or primarily for the platform layer?"*
- **Cross-team enablement** — "Guide teams across Grafana" suggests staff-level influence beyond just building. Mitigate with AgentProbe open-source (tooling others adopt) + Entrata cross-functional delivery.

---

## C) Level and Strategy

**Level detected:** Senior IC on the Grafana Ops / AI/ML team. The role is about building eval infrastructure used by other teams — influence beyond your immediate squad is expected at this level.

**Sell plan:**
- AgentProbe is the pitch, not background context: *"I built the exact system this role describes — automated LLM-as-judge eval engine, regression tracking across runs, CI/CD integration, structured output scoring. AgentProbe is a production version of what Grafana's AI/ML team needs to build internally."*
- Grafana's open-source DNA = AgentProbe is open-source. Cultural fit is real.
- Observability angle: Grafana is the observability company. AgentProbe is an observability tool for LLM systems. The framing is natural: *"I built LLM observability before joining — AgentProbe does for AI agents what Grafana does for infrastructure."*
- Comp target: Push toward $175K+ (upper half); Python/LLM eval depth clearly exceeds the baseline.

---

## D) Comp and Demand

| Source | Range | Notes |
|--------|-------|-------|
| Job posting (US) | $154,445–$185,334 | Disclosed |
| Job posting (Canada) | CAD 153,729–184,475 | Remote Canada option |
| Market | $160K–$220K for Sr SWE at observability-focused company | Grafana is well-funded |

**Assessment:** $154-185K is solid for remote. Lower than Cresta/Anthropic but Grafana is a well-established company (not a seed-stage bet). Strong equity and remote stability.

**H-1B:** Grafana Labs hires globally and has US entities — likely sponsors. Verify in recruiter screen.

---

## E) Customization Plan

| # | Section | Current | Proposed change | Why |
|---|---------|---------|-----------------|-----|
| 1 | Summary | General AI engineer | Lead: *"LLM evaluation engineer — built AgentProbe's automated eval pipeline: LLM-as-judge, regression tracking, CI/CD integration, 5-metric structured scoring. Open-source. Built for teams to adopt."* | JD is entirely about this |
| 2 | AgentProbe | Varies | Lead with eval architecture: LLM-as-judge, golden test sets, regression tracking, structured output scoring, CI/CD integration | Every JD bullet maps to AgentProbe |
| 3 | Competencies | Varies | LLM Evaluation Frameworks, LLM-as-Judge, Regression Tracking, Automated Eval Pipelines, CI/CD Integration, Structured Output Scoring, Observability | Direct JD vocabulary |
| 4 | Entrata | General | Add: internal tooling for teams — debugging tools adopted across squads, cross-functional enablement | JD: guide teams in best practices |

---

## F) Interview Plan

| # | JD Requirement | Story | Key Points |
|---|----------------|-------|------------|
| 1 | Design eval frameworks for LLM systems | AgentProbe: 5-metric eval engine architecture | Problem definition → metric selection → LLM-as-judge calibration → regression threshold → CI integration |
| 2 | LLM-as-judge implementation | AgentProbe: judge prompt engineering, metric scoring, calibration | Why LLM-as-judge beats rule-based; how to calibrate judge against ground truth; hallucination vs completeness tradeoff |
| 3 | Regression tracking + automated pipelines | AgentProbe: per-run anomaly detection, trend tracking across runs | What counts as a regression; how to set thresholds; surfacing signal vs noise |
| 4 | CI/CD integration of eval | AgentProbe: GitHub Actions gate on eval score | Where eval fits in the pipeline; blocking vs warning; cost/latency tradeoffs |
| 5 | Guide teams in best practices | Entrata internal debugging tools adopted by 2+ squads; AgentProbe open-source documentation | "I've shipped tooling that others adopted — documentation, API design, and clear interfaces are how you enable teams" |

---

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|--------|---------|--------|
| Salary disclosed | $154K–$185K — transparent | Positive |
| Company health | Grafana Labs: well-funded, ~1,200 employees, enterprise observability leader | Positive |
| JD specificity | Named techniques: LLM-as-judge, golden test sets, regression tracking, CI/CD | Positive |
| Open-source culture | Grafana is open-source-first — matches AgentProbe | Positive |
| Remote US confirmed | Yes | Positive |
| H-1B | Global company with US entities — likely sponsors; verify | ⚠️ Confirm |

---

## Keywords Extracted

genai evaluation, ml evaluation frameworks, llm-as-judge, automated eval pipelines, regression tracking, ci/cd, grafana, observability, python, llm evaluation, structured output, prompt engineering, golden test sets, dataset management

---

## Machine Summary

```yaml
report_num: 045
company: Grafana Labs
role: Senior Software Engineer, GenAI & ML Evaluation Frameworks
date: 2026-06-11
score: 4.2
archetype: AI Platform / LLMOps
legitimacy: High Confidence
location: Remote US
comp_range: "$154,445–$185,334 base (US)"
visa_risk: low-medium (global company, likely H-1B sponsor — verify)
key_gaps:
  - Grafana/Prometheus/Loki tooling (platform layer — likely not required for AI/ML eval role)
  - Go (Grafana platform language — clarify if required for this team)
  - Cross-team enablement at scale (mitigatable via AgentProbe open-source + Entrata tooling)
key_strengths:
  - AgentProbe = direct proof of LLM-as-judge, automated eval pipelines, regression tracking, CI/CD integration
  - Open-source AgentProbe = cultural fit with Grafana's DNA
  - Observability framing: "LLM observability" = what Grafana does for infrastructure
  - Python 8+ years production
  - $154-185K solid comp for remote
location_risk: low — remote US
recommend: strong apply — this is the closest JD-to-AgentProbe match in the pipeline; lead with AgentProbe as the product demo
```
