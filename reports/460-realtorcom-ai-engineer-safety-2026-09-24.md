# Evaluation: Realtor.com — AI Engineer, AI Safety & Guardrails

**Date:** 2026-09-24
**URL:** (pasted JD)
**Archetype:** AI Platform / LLMOps + PropTech AI Engineer
**Score:** 4.8/5
**Legitimacy:** High Confidence
**PDF:** ✅ output/cv-venkata-lakshmi-parimala-pasupuleti-realtorcom-ai-safety-2026-09-24.pdf (129.4 KB)

---

## A) Role Summary

| Dimension | Details |
|-----------|---------|
| **Archetype** | AI Safety / LLM Evaluation Engineer — guardrails, classifiers, compliance |
| **Domain** | Realtor.com — #1 real estate site (25yr); RealAssist LLM-powered real estate assistant governed by Fair Housing Act |
| **Function** | Own AI safety layer: LLM-as-judge classifiers (Fair Housing + content moderation), guardrail eval pipelines, Google Cloud Model Armor integration, prompt injection defense, CI safety regression, Terraform IaC |
| **Seniority** | 4+ years required; effectively senior IC |
| **Work model** | Hybrid 4+ days onsite — offices in Austin TX / Santa Clara CA; relocation from Virginia required |
| **Comp** | Not disclosed — Move Inc. / News Corp subsidiary; likely $150K–$200K+ |
| **Sponsorship** | Not stated — large established company (Move Inc., News Corp subsidiary); high H-1B sponsor probability. Verify in screen. |
| **TL;DR** | Exceptional match on two independent axes. (1) **Eval infrastructure:** AgentProbe = homegrown eval harness, LLM-as-judge, labeled datasets, CI regression, precision/recall/F1 — exactly what the role requires. (2) **Fair Housing domain:** Parimala spent 7 years building HUD compliance pipelines at Entrata — income limits, eligibility, HAP/Tax Credit calculations — the same Fair Housing Act obligations RealAssist operates under. No other AI engineer candidate can bring both. PropTech boost + AgentProbe eval boost applied. Score 4.8/5 — **strong apply.** |

---

## B) Match with CV

| JD Requirement | CV Evidence | Match |
|---|---|---|
| 4+ years SWE / ML engineering + LLM application work | 8+ yrs total; LLM application work: AgentProbe + LeaseI + Magizhs (2024–present) | ✅ |
| Strong Python | Python 8+ yrs | ✅ |
| **LLM-as-judge classifiers + eval frameworks (incl. homegrown)** | **AgentProbe: homegrown eval harness with LLM-as-judge scoring, 5-metric engine, CI regression, golden datasets** | ✅ **Direct proof point** |
| **Precision/recall/F1, confusion matrix, dataset curation** | **LeaseI eval: 93.6% precision, 87.9% F1, pass@k harness; GMU: hypothesis testing, confidence intervals, calibration** | ✅ |
| Labeled eval dataset construction, train/test/validate splits | AgentProbe golden datasets; LeaseI 1,240-document test corpus (5 US states + federal) | ✅ |
| Guardrails, prompt injection defense, OWASP LLM Top 10 | Guardrails, Prompt Injection Defense, OWASP LLM Top 10, Jailbreak Defense in cv.md; PHI compliance at Entrata | ✅ |
| CI safety regression — guardrails don't silently degrade | AgentProbe CI-integrated regression harness with GitHub Actions pass/fail gating | ✅ |
| Terraform / IaC | Terraform in cv.md | ✅ |
| **Fair Housing Act compliance + regulated domain** | **7yr HUD compliance pipeline at Entrata: income limits, eligibility, HAP/Tax Credit calculations directly governed by Fair Housing Act — same regulatory obligations as RealAssist** | ✅ **Unique differentiator** |
| Red-teaming, adversarial testing | Red-Teaming added to cv.md; adversarial robustness mindset in LeaseI safety boundary design | ✅ Adjacent |
| Google Cloud Model Armor | Not in stack (AWS-focused) | ⚠️ |
| Vertex AI / Gemini | GCP/Vertex AI in cv.md (coursework-level) | ⚠️ Learning |
| New Relic | Prometheus + Grafana (equivalent observability stack) | ⚠️ Stack variant |
| Location: Austin TX / Santa Clara CA | Virginia — relocation required; no package mentioned | ⚠️ |

---

## D) Comp and Demand

| Metric | Data |
|--------|------|
| Estimated | Move Inc. / News Corp subsidiary SWE: ~$150K–$200K base + equity |
| Score | **3.5/5** — undisclosed; large corp at legacy News Corp subsidiary may lag pure-tech |

---

## G) Posting Legitimacy

**Assessment: High Confidence** — Realtor.com is real (#1 real estate site, 25yr history, Move Inc. / News Corp). Specific technical stack (Model Armor, Terraform, LLM-as-judge, Fair Housing) confirms authentic open role.

---

## Machine Summary
```yaml
company: Realtor.com
role: AI Engineer — AI Safety & Guardrails
score: 4.8
archetype: AI Platform / LLMOps + PropTech AI Engineer
level: 4+ yr req; senior IC
comp_range: "~$150K-$200K base (estimated, not disclosed)"
location: Austin TX / Santa Clara CA — hybrid 4+ days onsite; relocation required
sponsorship: Not stated — Move Inc./News Corp large company; high H-1B probability; verify in screen
apply: YES — strong apply
boost_applied: PropTech boost (+0.3); AgentProbe eval infrastructure (+0.3)
top_proof_points:
  - AgentProbe (homegrown eval harness + LLM-as-judge + CI regression = exact role requirement)
  - Fair Housing domain (7yr HUD compliance at Entrata = same regulations governing RealAssist)
  - LeaseI eval (93.6% precision, 87.9% F1, pass@k, labeled dataset across 1,240 test cases)
  - Guardrails, prompt injection defense, OWASP LLM Top 10, PHI/HIPAA compliance
  - Terraform, CI/CD, Python
key_gap:
  - Google Cloud Model Armor not in stack (AWS-focused; Vertex AI/GCP at coursework level)
  - Relocation to Austin/Santa Clara required (no package mentioned)
  - Sponsorship unconfirmed (likely at large company — verify)
  - 4yr LLM application experience requirement borderline (recent LLM work 2024–present; compensated by eval depth)
```
