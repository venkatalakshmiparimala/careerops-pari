# Evaluation: Google — Software Engineer, Research Infrastructure (Health AI / Platforms & Devices)

**Date:** 2026-08-31
**URL:** (pasted as JD text — verify on careers.google.com)
**Archetype:** Data Infrastructure / Platform Engineering (research-grade, health domain)
**Score:** 2.0/5
**Legitimacy:** High Confidence
**PDF:** —

---

## A) Role Summary

| Dimension | Detail |
|-----------|--------|
| Archetype | Research Infrastructure SWE — builds and maintains the data processing platform that powers cutting-edge health research at Google |
| Team | Platforms & Devices — Research Infrastructure (health research, multi-site: London, LA, Seattle, Bengaluru) |
| Function | Design scalable research data infrastructure; Apache Beam pipelines; ML tools + agent platform integration; API design for research tooling; compliance-grade data processing |
| Seniority | "Software Engineer" — salary $207K–$300K = Google L6/L7 (Staff/Senior Staff), same band as YACO (#230) |
| Location | Multi-site — not remote; some travel implied |
| Comp | $207,000–$300,000 + 20% bonus target + equity |
| H-1B | Tier-1 — Google filed 4,000+ LCA petitions FY2025 |
| TL;DR | Two hard blocks: (1) Google L6/L7 salary band (Staff equivalent); (2) Apache Beam is a listed minimum qualification — not in stack. Health research infrastructure domain adds a third gap. Score: 2.0/5. |

---

## B) Match with CV

### Minimum Qualifications

| Requirement | CV Match | Quality |
|-------------|----------|---------|
| Bachelor's or equivalent | B.Tech CS (JNTU) + M.S. Data Analytics Engineering (GMU, GPA 3.87) | STRONG |
| 8 years Python (or C++/Java/Kotlin/Go) | 8+ years Python | STRONG |
| 5 years testing and launching software products | AgentProbe CI regression gate, 120+ Agile sprints at Entrata, deployment automation | PARTIAL |
| 3 years software design and architecture | LeaseI 8-agent LangGraph architecture; AgentProbe FastAPI; Entrata 20+ module schema design | MODERATE |
| **Experience with Apache Beam** | **Not in stack. PySpark is listed in cv.md but Apache Beam is a distinct framework (Google Dataflow / Apache-native batch+streaming).** | **GAP — minimum qual** |

### Preferred Qualifications

| Requirement | CV Match | Quality |
|-------------|----------|---------|
| Master's in CS or related | M.S. Data Analytics Engineering (GPA 3.87) | STRONG |
| 8 years data structures/algorithms | CS background; no competitive algorithmic track record | PARTIAL |
| 3 years technical leadership | Led projects + mentored 5+ at Entrata; no formal TL title | PARTIAL |
| 3 years complex matrixed organization | Entrata cross-functional delivery across 120+ sprints | MODERATE |
| **Experience with Healthcare AI** | **AI on FHIR (FHIR API application) — application layer, not health research infrastructure at Google scale** | **PARTIAL — different scope** |

### Responsibilities

| Responsibility | CV Proof Point | Quality |
|----------------|----------------|---------|
| Design infrastructure for scalable research data usage | GMU multi-source pipelines (190+ countries, R²=0.977); Entrata HUD pipelines (1.6M records) — but not research data infrastructure at Google scale | PARTIAL |
| Investigate ML tools and agent platforms; design APIs or standard processing | AgentProbe (ML eval platform, 15-endpoint FastAPI); LeaseI (agentic orchestration); investigation ethos in both projects | MODERATE |
| Build state-of-the-art data processing pipelines for research | Python data pipelines at Entrata + GMU; no Apache Beam or Google-scale research pipelines | PARTIAL |
| Identify researcher friction points and remove red tape | Internal tooling at Entrata (debug dashboards, bug tracking, 40% debugging time reduction) — adjacent pattern | PARTIAL |
| Improve and maintain infrastructure for smooth operation | 99.5% uptime SLA at Entrata; production incident RCA; corrective maintenance | MODERATE |

---

## C) Level and Strategy

**Hard Block #1 — Google L6/L7 (Staff equivalent)**

Salary $207K–$300K is identical to the YACO role (#230, also flagged as L6/L7 and a hard block). At Google, the L5 ceiling is roughly $147K–$210K (per #229 Launch Team), and L6 starts around $200K+. The $207K–$300K band is L6/L7. The preferred qualification "3 years in a technical leadership role" confirms that Google is targeting a senior principal contributor — someone who has already been at the tech lead / Staff Engineer level.

Same hard block as #230: Google's L6 interview bar requires demonstrated Staff-level impact and typically a prior Senior/Staff title at a peer company.

**Hard Block #2 — Apache Beam minimum qualification**

Apache Beam is listed as a minimum qualification ("Experience with Apache Beam"). It is not in Parimala's stack. Apache Beam is Google's open-source unified batch + streaming data processing framework (used via Google Dataflow on GCP). PySpark (listed in cv.md) is conceptually adjacent but not the same — candidates with only Spark experience regularly get screened out when Beam is a hard requirement. This would surface at the résumé review step.

**Domain — Health Research Infrastructure**

The team builds the data platform for health research that feeds into health products used by millions (Google Health, Fitbit data, etc.). The domain requires:
- Compliance-grade data handling (health data: HIPAA-adjacent, IRB-governed research data)
- Research data pipeline design (not product data pipelines)
- Collaboration with research scientists on tooling

AI on FHIR is an application layer over FHIR APIs — it's a clinical NLP system, not health research infrastructure. The spirit is adjacent but the scope is completely different.

**What is a genuine signal:**

The JD mentions "Investigate new ML tools and agent platforms to be supported by the infrastructure team" — this is where AgentProbe and LeaseI are genuinely relevant. The team needs to evaluate new AI tools (LLMs, agent frameworks) and build APIs or standard processing for them. That's an AgentProbe-shaped problem. However, this is one bullet among five — the core of the role is Apache Beam pipelines and research data infrastructure.

**Score: 2.0/5** — Apache Beam min qual gap + L6/L7 hard block are disqualifying. The adjacent signals (pipeline work, health data affinity from AI on FHIR, agentic tooling investigation) prevent it from dropping to 1.5.

---

## D) Comp

| Metric | Value |
|--------|-------|
| Base | $207,000–$300,000 |
| Bonus | 20% target (~$41K–$60K) |
| Equity | Google RSUs |
| TC estimate | $400K–$600K |
| vs. target ($80K–$140K) | Massively above target |
| Comp score | 5.0/5 (moot given hard blocks) |

---

## E) Recommendation

**SKIP — two hard blocks.**

1. Google L6/L7 salary band (Staff equivalent) — same pattern as #230 YACO
2. Apache Beam minimum qualification — not in stack, will fail résumé screen

**If you want Google research infrastructure:** Look for the same team at L4/L5 salary range ($147K–$210K), where the Beam requirement may still apply but the level filter is removed. Or target roles where Python + FastAPI + data pipelines are the stack (no Beam hard requirement).

---

## G) Posting Legitimacy

**High Confidence**

| Signal | Finding | Weight |
|--------|---------|--------|
| Company | Google / Alphabet | Positive |
| Team specificity | Named team (Research Infrastructure / Platforms & Devices), multi-site details | Positive |
| Salary | $207K–$300K — real market comp, consistent with Google L6/L7 | Positive |
| Apache Beam requirement | Specific framework requirement — JD-writer has domain knowledge | Positive |
| No PERM signals | No LI-DNI, no DOL boilerplate | Positive |

---

## Machine Summary

```yaml
company: Google (Alphabet)
role: Software Engineer, Research Infrastructure (Health AI / Platforms & Devices)
date: 2026-08-31
score: 2.0
archetype: Data Infrastructure / Platform Engineering (research-grade)
legitimacy: High Confidence
recommend: SKIP — hard block #1: Google L6/L7 salary ($207K-$300K, Staff equivalent); hard block #2: Apache Beam is a minimum qualification, not in stack; health research infrastructure domain gap
comp_low: 207000
comp_high: 300000
comp_bonus: 20% target
comp_tc_est: 400000-600000
location: multi-site (London, LA, Seattle, Bengaluru) — not remote
h1b_sponsor: tier-1 (4000+ LCA FY2025, ~99% approval)
hard_block: YES — (1) Google L6/L7 Staff level; (2) Apache Beam minimum qualification not met
key_gap: Apache Beam (min qual); Google L6/L7 level; health research infrastructure domain; no distributed data processing at research scale
key_strength: 8+ years Python; M.S. Analytics; ML tools investigation (AgentProbe); health data affinity (AI on FHIR — different scope); data pipeline experience (Entrata, GMU)
priority: skip — 2.0/5, two simultaneous hard blocks
```
