# Evaluation: Sage Care -- AI Evaluation & Feedback Platform Engineer

**Date:** 2026-09-22
**URL:** (pasted directly, no URL provided)
**Archetype:** AI Evaluation / LLMOps Platform Engineer (Healthcare)
**Score:** 4.5/5
**Legitimacy:** High Confidence
**PDF:** output/cv-venkata-lakshmi-parimala-pasupuleti-sage-care-2026-09-22.pdf
**Location:** Unknown (US-based; MENA expansion mentioned; remote policy unconfirmed)
**Comp:** Not disclosed

---

## A) Role Summary

| Dimension | Detail |
|-----------|--------|
| Archetype | AI Evaluation / LLMOps Platform Engineer -- build evaluation pipelines, feedback systems, and ML infrastructure that turn production agent conversations into continuous improvement; own the intelligence layer of the agent platform |
| Domain | Sage Care -- early-stage healthcare startup (General Catalyst / Chelsea Clinton backing); AI agents handling real patient conversations for hospital systems in US + MENA |
| Function | Build eval + feedback platform (analyze production conversations, cluster quality issues, measure agent performance); make failures diagnosable (root cause across transcription/reasoning/retrieval/orchestration); automate learning loop (ML pipelines reducing manual improvement effort); HITL workflows |
| Seniority | No formal title in JD -- mid to senior AI engineering; early-stage startup = no formal leveling concern |
| Location | Unknown -- confirm at screen |
| Company | Sage Care -- early-stage; General Catalyst-backed (top-tier VC); Apple/Uber/Carbon Health founding team; H-1B unconfirmed at this stage |
| TL;DR | AgentProbe is what this role is building. The "What Success Looks Like" section ("failures detected by systems, not discovered by people") is the exact problem statement AgentProbe solves. HITL workflows = LeaseI's HITL escalation layer. Healthcare regulated domain = AI on FHIR (HIPAA-compliant) + PHI compliance (Entrata). Score 4.5 -- Apply. H-1B must be verified at early-stage startup. |

---

## B) Match with CV

| JD Requirement | CV Match | Strength |
|----------------|----------|----------|
| 5+ years SWE + production systems | 9yr | ✅ Exceeds |
| LLMs, AI agents, or conversational AI | LeaseI + AgentProbe + Magizhs | ✅ Strong |
| **Building AI evaluation platforms or frameworks** | **AgentProbe: 5-metric eval engine, CI regression gate, LLM-as-judge, pass@k harness, agent tracing -- exactly this** | ✅ Exceptional -- direct match |
| **Feedback systems for ML/LLM applications** | AgentProbe: regression suite blocks degradation; multi-trial scoring tracks improvement over time | ✅ Strong |
| **Observability, reliability, quality tooling for AI** | AgentProbe: agent tracing, scoring rationale, production monitoring framework | ✅ Strong |
| **ML pipelines improving model/agent performance** | AgentProbe eval harness used to iterate LeaseI across 1,240 test cases | ✅ Present |
| Strong backend engineering + systems thinking | FastAPI, Python, PostgreSQL, RabbitMQ, Docker/K8s; 120+ sprints | ✅ Strong |
| Ambiguous problems, first principles | LeaseI + AgentProbe = 0→1 with no existing codebase or spec | ✅ Strong |
| **HITL workflows (nice-to-have)** | **LeaseI: HITL escalation on low-confidence and regulated decisions -- designed into the agent architecture** | ✅ Direct match |
| **Healthcare / regulated, safety-critical domain (nice-to-have)** | AI on FHIR (HIPAA-compliant, PHI data, RBAC); Entrata PHI compliance (zero incidents); LeaseI regulated-decision discipline | ✅ Strong |
| **Internal platform for engineering teams (nice-to-have)** | AgentProbe: built as a platform used to evaluate LeaseI; open-source for engineering teams | ✅ Present |
| **Voice AI systems (nice-to-have)** | Zero -- agents are text-based; voice is a gap | ❌ Absent (nice-to-have only) |
| H-1B sponsorship | Early-stage startup (General Catalyst-backed) -- unconfirmed; VC-backed startups often have legal support but early stage = uncertain | ⚠️ Unconfirmed |

---

## C) Why This Scores 4.5

**The "What Success Looks Like" section describes AgentProbe.** Word for word: "Failures are detected by systems, not discovered by people. Every production issue has a diagnosable root cause and a clear owner. Human feedback measurably changes agent behavior, with the lag between the two shrinking over time." AgentProbe's CI regression gate catches degradation before deployment (failures detected by systems). Its LLM-as-judge scoring with traced rationale makes every eval decision inspectable (diagnosable root cause). Its multi-trial pass@k harness measures whether changes actually move the quality needle (feedback measurably changes behavior). This isn't a loose analogy -- it is the same problem statement.

**AgentProbe hits all four required "experience in at least one of" bullets simultaneously.** The JD asks for at least one: evaluation platforms (✅), feedback systems for LLM applications (✅), observability/reliability/quality tooling (✅), ML pipelines improving agent performance (✅). She has all four in one project.

**HITL is a direct proof point, not a checkbox.** LeaseI's HITL escalation was designed as a structural constraint: when agent confidence drops below threshold or the decision involves a regulated outcome, the system routes to human review. That is exactly the "workflows that transform human feedback into actionable improvements" the JD describes. It's not "familiarity with HITL" -- it's an architectural decision enforced in code.

**Healthcare regulated domain is covered.** AI on FHIR is an HIPAA-compliant medical records system -- built on actual FHIR APIs, structured PHI data, RBAC access controls. Entrata's PHI compliance (zero incidents across the AWS migration) demonstrates disciplined handling of regulated patient-adjacent data. Sage Care's AI handles patient conversations -- the same trust and compliance discipline required.

**Early-stage startup is a positive per strategy.** General Catalyst backing is credible (top-tier VC, Airbnb/Stripe/Warby Parker portfolio). Apple/Uber/Carbon Health founding team signals execution credibility. Early-stage = high ownership, fast iteration, direct impact -- exactly the profile.

**Voice AI gap is a nice-to-have, not a blocker.** Patient conversations may be voice-transcribed, but the role is evaluation infrastructure -- not voice engineering. The transcription layer is upstream; her work is analyzing the outputs and building feedback systems.

---

## D) Comp and Demand

| Source | Range | Notes |
|--------|-------|-------|
| Disclosed | **Not disclosed** | Early-stage startup; expect equity component; clarify at screen |
| H-1B | Early-stage (General Catalyst-backed) -- uncertain; top VC backing suggests legal infrastructure | ⚠️ Confirm at screen |
| Location | Unknown | Remote? US-based? MENA role? Confirm at screen |

---

## E) CV Plan

Frame: "I built the system this role describes. AgentProbe is an evaluation and feedback platform for production AI agents -- CI regression gate, LLM-as-judge, agent tracing, feedback loop. That's your job description."

- Summary: Lead with AgentProbe (eval platform = exact role function) + LeaseI HITL (feedback loop into agent behavior) + AI on FHIR (healthcare/HIPAA domain)
- Skills: Python, LLM evaluation, CI/CD regression gate, LLM-as-judge, HITL, agent observability, RAG, FastAPI, Docker/K8s, HIPAA
- Entrata: regulated domain, PHI compliance, production reliability
- Projects: AgentProbe (eval platform proof point) + LeaseI (HITL + regulated decisions) + AI on FHIR (healthcare domain)
- Frame LeaseI's "wrong data = wrong housing eligibility" as safety-critical domain experience

---

## G) Posting Legitimacy

**High Confidence.** Sage Care is a verifiable startup (General Catalyst + Chelsea Clinton backing, named health system partnerships, MENA expansion). Detailed and specific JD. No ghost signals. Company stage (early) is the only caveat -- not a legitimacy concern.

---

## Recommendation: Apply (4.5/5 -- clears threshold)

**AgentProbe is the product this role is hiring someone to build. Apply.**

Must confirm at first contact: H-1B sponsorship capability + location/remote policy + compensation structure.

---

## Machine Summary

```yaml
report: 407
company: Sage Care
role: AI Evaluation & Feedback Platform Engineer
date: 2026-09-22
score: 4.5
archetype: AI Evaluation / LLMOps Platform Engineer (Healthcare)
legitimacy: High Confidence
url: null
status: Evaluated
recommendation: Apply
threshold: 4.5 (non-PropTech) -- exactly clears; 4.0 (startup boost) -- clears
boosts_applied:
  - AgentProbe = exact eval platform the JD describes (all 4 required bullets covered)
  - "Success looks like" section = AgentProbe value proposition word for word
  - HITL workflows = LeaseI architectural constraint (direct proof point)
  - Healthcare / regulated domain = AI on FHIR (HIPAA) + Entrata PHI compliance
  - Early-stage startup = strategy boost (General Catalyst backing)
penalties:
  - Voice AI absent (nice-to-have; minimal) (-0.1)
  - Comp not disclosed (-0.1)
  - H-1B unconfirmed at early-stage (-0.2)
  - Location unknown (-0.1)
gaps:
  - Voice AI (nice-to-have; transcription layer is upstream of role scope)
  - H-1B: unconfirmed; must verify at first contact
  - Comp: not disclosed
h1b: UNCONFIRMED -- early-stage startup; General Catalyst backing suggests legal infrastructure; confirm at screen
comp_range: not disclosed
location: unknown -- confirm at screen
```
