# Evaluation: Expedia Group -- Forward Deployed AI Engineer III

**Date:** 2026-09-21
**URL:** (pasted directly, no URL provided)
**Archetype:** AI Platform / Infrastructure Engineering (FDE label, infra core)
**Score:** 3.2/5
**Legitimacy:** High Confidence
**PDF:** N/A (below 4.0 FDE threshold -- SKIP)
**Location:** Austin, TX
**Comp:** $116,500 -- $163,000 (top $186,500)

---

## A) Role Summary

| Dimension | Detail |
|-----------|--------|
| Archetype | "FDE" title but actually AI Platform / Infrastructure Engineer -- owns cloud IaaS, IaC automation, SLOs, observability, enterprise SaaS integrations for internal AI platforms |
| Domain | Expedia Group AI & Automation Team -- deploying AI tools and productivity platforms to internal employees worldwide |
| Function | IaC module design; policy-as-code; cloud architecture (compute/networking/storage/IAM); SLO + observability engineering; enterprise SaaS integrations; incident resolution / RCA; ADRs; mentor junior engineers |
| Seniority | "Engineer III" at Expedia (~17,000 employees) -- formal-leveling company; Engineer III = Senior-equivalent on their IC ladder |
| Location | Austin TX; comp range disclosed |
| Company | Expedia Group -- global travel platform, 17K+ employees, major H-1B sponsor |
| TL;DR | Despite "FDE" in the title, this is an AI Platform / Infrastructure Engineering role. The required qualifications are dominated by: IaC/Terraform (required), design-level cloud IaaS including networking and IAM (required), SLO definition and observability engineering (required), enterprise SaaS administration (Glean/ServiceNow). Her background is application development + AI application engineering -- not platform/infra engineering. IaC gap is the same hard blocker as Capgemini (#395). Score 3.2 -- SKIP. |

---

## B) Match with CV

| JD Requirement | CV Match | Strength |
|----------------|----------|----------|
| Python proficiency + automation | Python 9yr primary; 80% manual workload automation at Entrata | ✅ Strong |
| AI/ML literacy -- LLMs, RAG, agentic, AI-assisted ops | LeaseI (8-agent LangGraph, RAG, HITL); AgentProbe (LLM eval, multi-provider routing) | ✅ Strong |
| AI guardrails, governance, monitoring in production | LeaseI: HITL on regulated decisions, deterministic compliance, output validation, LLM-as-judge | ✅ Present |
| Enterprise AI copilot / knowledge-assistant integration | Uses Claude Code + GitHub Copilot personally; AgentProbe multi-provider routing; not enterprise administration at scale | ⚠️ Partial |
| AWS cloud IaaS | S3, EC2, RDS, Glue (usage-level) | ⚠️ Usage-level, not design-level (IAM, networking, VPC) |
| Docker, Kubernetes | Both present (Entrata production) | ✅ Present |
| SaaS integration architectures | Entrata third-party integrations; FastAPI REST integrations | ⚠️ App-level, not enterprise SaaS lifecycle management |
| Observability / SLOs / telemetry pipelines | AgentProbe CI gate + tracing; observability listed in skills; no production observability platform (Datadog/Grafana/PagerDuty) | ⚠️ Partial |
| Mentorship | 5+ junior engineers; 300+ code reviews | ✅ Present |
| ADRs / technical documentation | Implied from senior engineering ownership | ✅ Plausible |
| **IaC automation -- Terraform, Pulumi (required)** | **Not in stack -- zero IaC experience** | ❌ Required gap |
| **Policy-as-code frameworks (required)** | **Not in stack** | ❌ Required gap |
| **Design-level cloud IaaS -- compute, networking, storage, IAM (required)** | Usage-level AWS only; no VPC/IAM/networking design | ❌ Gap |
| **Enterprise SaaS administration -- Glean, ServiceNow, Salesforce (preferred)** | Not in background | ❌ Absent (preferred only) |
| FinOps / cost attribution (preferred) | Not present | ❌ Absent (preferred only) |
| H-1B sponsorship | Expedia Group 17K+ employees -- major H-1B sponsor | ✅ Safe |

---

## C) Why This Doesn't Clear 4.0

**The "FDE" label is misleading -- this is a platform/infra role.** The Expedia AI & Automation Team deploys AI tools to internal employees. "Forward Deployed" here means "pushing AI capability into the business" -- not customer-facing consulting delivery or the FDE archetype in the product/solutions engineering sense. The actual job is owning cloud infrastructure, IaC, SLOs, and enterprise SaaS integrations for internal AI platforms. This maps to Platform Engineer / AI Infrastructure Engineer, not to the FDE roles where Parimala is strongest (rapid prototyping, domain deployment, cross-functional delivery).

**IaC/Terraform is a required hard gap.** "Hands-on, design-level experience... with ownership of IaC automation (Terraform, Pulumi, or equivalent), including building reusable modules and policy-as-code frameworks" -- listed under minimum qualifications. Not adjacent to Docker/K8s experience. Same blocker that sank Capgemini (#395).

**Design-level cloud IaaS is required.** The JD specifies "compute, networking, storage, IAM" at design level. Her AWS experience is S3/EC2/RDS/Glue -- services used in application code, not VPC design, security group architecture, or IAM policy authoring.

**The AI piece is secondary, not primary.** AI literacy is one of 11 minimum qualifications. The role is primarily building cloud infrastructure that AI tools run on -- not building the AI applications themselves. Her proof points (LeaseI, AgentProbe) are AI application engineering, not AI infrastructure/platform engineering.

**Engineer III at 17K-employee formal company.** This is Senior-equivalent. The strategy penalty applies -- confirmed pattern of rejection at Senior level at formal-leveling companies.

**What's genuinely strong.** Python/AI/LLM literacy, agentic AI proof points (LeaseI + AgentProbe), mentorship, and documentation ownership. If the role had been "Applied AI Engineer building AI features for Expedia employees" with AWS/Docker as standard infrastructure context, this would score 4.0+. The hard requirement for IaC and design-level IaaS is what blocks it.

---

## D) Comp and Demand

| Source | Range | Notes |
|--------|-------|-------|
| Disclosed | $116,500 -- $163,000 base (top $186,500) | Austin TX; solid range for platform engineer |
| H-1B | Expedia Group 17K+ employees -- major H-1B sponsor | ✅ Safe |
| Location | Austin TX | Not penalized per profile |

---

## G) Posting Legitimacy

**High Confidence.** Expedia Group is a verifiable global travel company (17K+ employees, public). Specific location (Austin TX), comp range disclosed with stated top-of-range, ADA accommodation link. No ghost signals.

---

## Recommendation: SKIP (3.2/5 -- below 4.0 FDE threshold)

**IaC/Terraform gap is the hard blocker.** Listed as minimum required; not bridgeable with Docker/K8s proximity. This role's core function (platform/infra engineering, IaC, cloud IaaS design) is outside her application engineering background. Same skip rationale as Capgemini (#395) -- required infra gaps, wrong core archetype despite the "FDE" label.

---

## Machine Summary

```yaml
report: 397
company: Expedia Group
role: Forward Deployed AI Engineer III
date: 2026-09-21
score: 3.2
archetype: AI Platform / Infrastructure Engineering (FDE label, infra core)
legitimacy: High Confidence
url: null
status: SKIP
gaps:
  - IaC / Terraform / Pulumi (required -- not in stack; same blocker as Capgemini #395)
  - Policy-as-code (required -- not in stack)
  - Design-level cloud IaaS (compute, networking, storage, IAM -- required; she has usage-level AWS only)
  - Enterprise SaaS administration (Glean, ServiceNow -- preferred; absent)
strengths:
  - Python/AI/LLM/RAG/agentic: strong proof points (LeaseI + AgentProbe)
  - AI guardrails + governance: LeaseI HITL/deterministic compliance
  - Mentorship + documentation ownership
  - H-1B safe (Expedia 17K+ employees)
note: "FDE" label misleading -- actual role is platform/infra engineering for internal AI tools, not customer-facing FDE or AI application engineering. Engineer III = Senior-equivalent at formal-leveling company.
comp_range: $116,500--$163,000 (top $186,500)
location: Austin TX (not penalized)
```
