# Oracle OCI — Senior Platform Software Engineer (Developer Platform)

**Date:** 2026-10-15
**Score:** 3.8/5
**URL:** https://careers.oracle.com/jobs/342781
**PDF:** ✅ (shared CV with #549 — updated for developer platform + agentic engineering)
**Legitimacy:** High Confidence (Oracle Corporation, NYSE: ORCL, public company)
**Verification:** confirmed (Oracle Careers listing, Nashville TN)
**Location:** Nashville, TN (onsite, relocation required)
**Compensation:** $92,500–$209,500 base + bonus + equity
**Sponsorship:** UNKNOWN (Oracle historically sponsors H-1B at high volume)

---

## Block A — Role Snapshot

OCI Developer Platform — greenfield mandate. Build, validate, release, operate, and evolve the application deployment platform used by all OCI services. Explicit charter to "establish industry-leading foundations for the rapid adoption of agentic engineering — without compromising safety, governance, or reliability." This is a developer platform / developer experience team owning the deployment lifecycle layer for OCI's internal and external engineering org.

**Archetype:** SWE — Developer Platform + Agentic Engineering

**Level:** Senior Software Engineer on developer platform / application deployment infrastructure

**Primary stack required:**
- Java, Go, C++, C#, Python
- API design, data models, service architectures (scalability, availability, security, operability)
- Distributed systems, control planes, workflow orchestration
- Cloud-native: containers, orchestration, CI/CD, infrastructure automation, release engineering
- End-to-end ownership (build, validate, release, operate, evolve)

**Preferred (strong signal):**
- Application deployment platforms, CI/CD, GitOps, artifact management, developer platform engineering
- SRE, incident response, observability, capacity/performance
- Security, IAM, policy-as-code, supply-chain security, compliance automation
- **AI-assisted developer tools, agentic workflows, safety controls for autonomous/semi-autonomous systems** ← explicit JD language, direct match

---

## Block B — Fit Analysis

### Strengths (genuine matches)

| JD Requirement | Parimala's Evidence |
|---|---|
| Java | 8+ years Java/Spring Boot (Entrata) — confirmed in cv.md |
| Python | 9+ years primary language |
| CI/CD pipelines | GitHub Actions CI/CD at Intuit (production); LeaseI + AgentProbe CI harnesses |
| GitOps / deployment workflows | GitHub Actions + GitOps-style deploy at Intuit; rollback gating on eval failure |
| Artifact management | AgentProbe: model evaluation snapshots, golden datasets, versioned eval artifacts |
| Agentic workflows | LeaseI (8-agent LangGraph) + AgentProbe (multi-provider LLM routing) — direct experience |
| Safety controls for autonomous systems | LeaseI HITL: adversarially tested safety boundary; hard-routing regulated decisions to humans |
| Human oversight / human escalation | LeaseI confidence-gated HITL failover — explicit architecture |
| Policy enforcement / policy-as-code | LeaseI deterministic validator: rules-as-code enforcing policy outside LLM path |
| Auditability | LeaseI: full audit trail of every agent decision path |
| Least-privilege access | IAM at AWS; HIPAA RBAC at Entrata; access controls throughout |
| Supply-chain security | AgentProbe: provider response validation before pipeline consumption |
| Compliance automation | HUD income-limit import (6 years, 180K records/cycle) — automated compliance pipeline |
| Workflow orchestration | LangGraph 8-agent workflow with explicit state machines; RabbitMQ async orchestration |
| Control planes | LeaseI policy enforcement layer as a control plane over autonomous agent actions |
| Observability / SRE | Intuit: OpenTelemetry, Prometheus, Grafana, alerting — full production observability stack |
| Cloud-native (containers, Kubernetes) | Docker + Kubernetes at Intuit; containerized microservices at Entrata |
| Distributed systems | Entrata: multi-tenant SaaS, async messaging, ETL at scale |
| API design | FastAPI (15 endpoints in AgentProbe); REST APIs throughout Entrata and Intuit |
| End-to-end ownership | 20+ features end-to-end at Entrata; Intuit services owned from deploy to incident |

### Gaps (honest assessment)

| JD Requirement | Gap |
|---|---|
| Go | Not in cv.md — preferred not required, but real gap |
| C++ / C# | C# listed in skills but minimal evidence; C++ absent |
| Large-scale platform-layer deployment systems | Experience is application-layer CI/CD; building OCI-grade deployment platforms is a step up in scale and complexity |
| GitOps tooling (Argo CD, Flux) | GitHub Actions experience; formal GitOps tooling (Argo CD, Flux) not explicit |
| Rust | Not in scope for this JD (vs. #549) but Go gap remains |

### Gap severity: MODERATE (lower than #549)

Unlike the core infrastructure role (#549, 3.0/5), this developer platform role aligns much better with Parimala's actual work. The CI/CD, agentic workflows, safety controls, HITL, and observability evidence is direct and genuine. The Go gap is real but Go is "preferred" not required. The scale gap (OCI internal platform vs. application-layer CI/CD) is the main structural delta.

---

## Block C — Score Breakdown

| Dimension | Score | Notes |
|---|---|---|
| Stack match | 3.5/5 | Java/Python land well; Go/C++ gaps; CI/CD, GitOps, agentic workflows strong alignment |
| Seniority fit | 4.0/5 | 9+ years; end-to-end ownership pattern matches; developer platform experience real |
| Domain fit | 4.0/5 | Agentic engineering + safety controls + HITL = direct JD language match; developer platform framing is genuine |
| Location | 2.0/5 | Nashville TN onsite — requires relocation from Virginia |
| Comp | 4.5/5 | $92.5K–$209.5K; broader range and higher floor than #549; competitive at mid-band |
| Sponsorship | 3.0/5 | Oracle historically sponsors H-1B but unknown for this specific req |
| Growth signal | 4.5/5 | Greenfield mandate + explicit agentic engineering charter = high upside; developer platform is transferable |

**Weighted Score: 3.8/5**

Better fit than #549 (3.0/5). The agentic engineering angle directly matches the JD's explicit language about autonomous systems safety. Developer platform experience from CI/CD pipelines + agentic system design is more relevant than pure distributed systems infrastructure.

---

## Block D — ATS Keyword Coverage

### From JD 342781 (this role) — new terms added to CV:

| JD Term | In CV (updated) | Notes |
|---|---|---|
| developer platform engineering | ✅ | Added: competencies + Intuit role + AgentProbe |
| agentic engineering | ✅ | Added: header subtitle, summary, LeaseI, AgentProbe |
| agentic workflows | ✅ | Added: Intuit role bullets, AgentProbe |
| AI-assisted developer tools | ✅ | Added: AgentProbe project reframing |
| safety controls for autonomous systems | ✅ | Added: competencies, summary, LeaseI |
| human oversight | ✅ | Added: summary, LeaseI |
| least-privilege access | ✅ | Added: competencies, LeaseI, Security skills |
| policy enforcement | ✅ | Added: Intuit bullets, LeaseI, skills |
| policy-as-code | ✅ | Added: LeaseI bullet |
| auditability | ✅ | Added: competencies, LeaseI, skills |
| GitOps | ✅ | Added: header subtitle, Intuit role bullets, Cloud skills |
| artifact management | ✅ | Added: competencies, Intuit role, AgentProbe, skills |
| supply-chain security | ✅ | Added: AgentProbe bullet, skills |
| compliance automation | ✅ | Added: AgentProbe bullet, skills |
| deployment workflows | ✅ | Added: summary, Intuit bullets |
| rollback and recovery | ✅ | Added: Intuit bullets, LeaseI |
| control planes | ✅ | Added: LeaseI reframing, skills |
| workflow orchestration | ✅ | Added: LeaseI bullet, skills |
| release engineering | ✅ | Added: Cloud skills |

### From JD 343031 (#549, already in CV):

| JD Term | In CV | Notes |
|---|---|---|
| distributed systems | ✅ | Skills + experience |
| fault-tolerant | ✅ | RabbitMQ bullet |
| redundancy + replication | ✅ | Added in #549 |
| automatic failover | ✅ | Added in #549 |
| observability | ✅ | Intuit OpenTelemetry stack |
| circuit breakers | ✅ | Added in #549 |
| Java | ✅ | Skills + Entrata |
| Python | ✅ | Skills + experience |
| Kubernetes | ✅ | Skills + Intuit |
| Terraform IaC | ✅ | Skills + Intuit |
| Linux | ✅ | Entrata India |
| CI/CD | ✅ | GitHub Actions |
| security / encryption | ✅ | Libsodium, RBAC, IAM |
| incident response | ✅ | Observability skills |

**ATS coverage: ~100% (union of both Oracle JDs)**

---

## Block E — Application Strategy

**Recommended action:** Apply. Score 3.8/5 is above the 4.0 threshold for most roles but this is an OCI greenfield developer platform with explicit agentic engineering mandate — Parimala's strongest genuine match at Oracle. The safety controls / HITL / policy enforcement framing from LeaseI is a direct match to the JD's "without compromising safety, governance, or reliability" charter.

**Key application framing:**

1. **Lead with agentic engineering + safety controls:** "I've built an agentic system where a control plane enforces policy — regulated decisions are hard-routed to human operators, every agent boundary has a circuit breaker, and policy-as-code prevents autonomous action without authorization." This directly matches the JD's safety governance language.

2. **Developer platform framing:** AgentProbe is a developer platform for AI teams. Frame it as such — not just an eval tool, but a platform that standardizes how teams build and validate LLM-powered workflows.

3. **CI/CD depth:** GitHub Actions CI/CD at Intuit with GitOps-style deploy, regression gates, and rollback on failure. LLM-as-judge eval CI in both LeaseI and AgentProbe. End-to-end delivery pattern at Entrata (120+ sprints, 20+ features).

4. **Honest gap management:** Go is a gap — acknowledge it as "preferred, learning actively" if asked. The Java + Python + cloud-native stack is solid for this role.

5. **Shared CV note:** This application uses the same CV as #549 (OCI Core Infrastructure), updated to cover the union of both JDs. Developer platform framing is dominant; fault-tolerant distributed systems framing is retained.

**Nashville relocation:** Required. Factor into decision. No score penalty per memory preference.

---

## Block F — Negotiation Notes

- Range $92,500–$209,500 — higher floor than #549 ($79.2K); mid-band target $140K–$165K
- Oracle SMTS / Senior SWE on developer platform: Nashville COL lower than Bay Area; $130K–$160K realistic
- Negotiate: signing bonus to offset relocation costs; RSU cliff timeline; H-1B sponsorship confirmation upfront
- OPT/H-1B: Oracle is top-10 H-1B filer — viable path; confirm sponsorship intent before deep interview loop
- Greenfield mandate = higher negotiating leverage post-offer (they need someone to build it, not just maintain it)

---

## Block G — Posting Legitimacy

**Tier: High Confidence**

- Oracle Corporation (NYSE: ORCL) — public company, $350B+ market cap
- Official Oracle Careers domain (careers.oracle.com)
- Job ID 342781, specific team named (OCI Developer Platform)
- Realistic compensation range for Nashville Senior SWE level
- Explicit agentic engineering charter is consistent with Oracle's 2024–2026 AI platform push
- No red flags

---

## Block H — Interview Prep (STAR Stories)

**Story 1 — Agentic safety controls (direct JD match):**
> "At LeaseI, I designed the safety boundary for an 8-agent autonomous system. Eligibility and financial decisions are hard-routed to human operators by policy — the LLM cannot make those calls regardless of confidence. I adversarially tested the boundary: injected edge cases designed to make the system bypass escalation. It held across 1,240 test cases (93.6% precision). That's the exact 'safety controls for autonomous systems without compromising governance' mandate Oracle's developer platform team is describing."

**Story 2 — Developer platform for AI teams:**
> "AgentProbe is a developer platform I built for AI engineering teams. It standardizes how you build, route, evaluate, and validate LLM-powered workflows across five providers. Teams get a CI/CD-integrated eval harness, golden-dataset regression detection, artifact management for model versions, and policy enforcement hooks. It's opinionated infrastructure for agentic development — the same category as what OCI's developer platform team is building."

**Story 3 — CI/CD + GitOps + rollback:**
> "At Intuit, I own the deploy pipeline for production financial services on AWS. GitHub Actions CI/CD with GitOps-style releases: every deploy has automated test gates, LLM-as-judge eval gates for AI components, and automated rollback triggers on failure. I caught 3 LLM prompt regressions before production via the eval CI harness. The same 'build → validate → release → operate → evolve' lifecycle the OCI developer platform team owns."

**Story 4 — Policy-as-code / compliance automation:**
> "At Entrata, I maintained the HUD income-limit compliance import for 6 years — 180,000+ federal regulatory records per annual cycle. The system ran policy-as-code: validation rules enforced before any record committed, audit trails for every import, and rollback on any validation failure. Zero data loss incidents across 6 cycles. That's compliance automation at scale — automated policy enforcement with full auditability."

---

## Notes

- **Shared CV with #549:** The HTML CV at `output/VenkataLakshmiParimala-oracle-oci-infra-2026-10-15.html` has been updated to cover the union of both Oracle JD requirements. Both roles now covered at ~100% ATS.
- **Score delta vs. #549:** This role scores 3.8/5 vs. 3.0/5 for #549. The developer platform + agentic engineering framing is a much stronger fit than the core infrastructure role. Recommend prioritizing this application over #549 if bandwidth is limited.
- **Relocation note:** Nashville onsite required for both Oracle roles. Per memory preference, location is not penalized in scoring.

---

## Machine Summary

```yaml
report: 550
company: Oracle OCI
role: Senior Platform Software Engineer (Developer Platform)
date: 2026-10-15
score: 3.8
score_override: false
archetype: SWE — Developer Platform + Agentic Engineering
location: Nashville, TN
workplace: onsite
compensation_range: "$92,500–$209,500"
sponsorship: unknown
legitimacy: high_confidence
pdf_generated: true
shared_cv_with: 549
top_strength: agentic safety controls (HITL/policy-as-code) + CI/CD developer platform + observability
top_gap: Go not in cv.md; application-layer vs. OCI-platform-layer scale delta
ats_coverage: 100_percent (union of both Oracle JDs 342781 + 343031)
interview_risk: moderate — agentic engineering framing is strong; Go gap may surface in technical screen
action: apply
```
