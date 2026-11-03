# Evaluation: SiriusXM -- Senior Software Engineer, Platform Engineering

**Date:** 2026-09-21
**URL:** (pasted directly, no URL provided)
**Archetype:** Platform Engineering / DevOps / Developer Experience
**Score:** 2.5/5
**Legitimacy:** High Confidence
**PDF:** N/A (below threshold)
**Location:** Unspecified (SiriusXM US; likely NYC)
**Comp:** $100,800 -- $170,000

---

## A) Role Summary

| Dimension | Detail |
|-----------|--------|
| Archetype | Platform Engineering / DevEx / SRE-adjacent (CDK libraries, IaC, developer tooling, AI integration) |
| Domain | SiriusXM audio platform -- internal developer experience, cloud infrastructure, shared component libraries |
| Function | Build CDK/IaC libraries; improve developer productivity tooling; integrate AI into platform operations; provide architectural guidance to internal teams |
| Seniority | Senior IC -- 5+ yr required |
| Location | Unspecified US (likely NYC or DC) |
| Company | SiriusXM -- ~10,000 employees, large formal company |
| TL;DR | Platform/DevOps role at a large media company. Two hard problems: (1) CDK/CloudFormation/IaC is the core required skill -- absent from her stack; (2) Platform Engineering / Developer Experience is not her domain. Python/TypeScript/AWS/GitHub Actions all present, but the domain and primary toolchain don't fit. "Must have legal right to work in the US" = likely no sponsorship -- flag at recruiter screen. Score 2.5 -- SKIP. |

---

## B) Match with CV

| JD Requirement | CV Match | Strength |
|----------------|----------|----------|
| 5+ years SWE experience | 9yr (Entrata 7.5yr + GMU + Magizhs) | ✅ Exceeds |
| Python | Python 9yr primary | ✅ Strong |
| TypeScript | AgentProbe (React/TypeScript) | ✅ Present |
| AWS (large cloud role) | AWS S3, EC2, RDS, Glue -- 7yr production | ✅ Present |
| GitHub Actions / CI-CD | GitHub Actions in AgentProbe, LeaseI | ✅ Present |
| Building reusable libraries/APIs | FastAPI REST APIs, shared pipeline components | ✅ Present |
| Code reviews / technical docs | 300+ peer code reviews; documentation standards | ✅ Present |
| AI-driven tooling integration | LangGraph, agentic AI, RAG pipelines | ✅ Present |
| **CDK / CloudFormation / IaC** | Not in stack -- AWS services used but not IaC tooling | ❌ Core gap |
| **Platform Engineering / DevEx domain** | Backend/data engineer -- never in a platform team | ❌ Domain gap |
| Datadog / observability platforms | Not present | ⚠️ Gap (extra credit) |
| AWS certifications | None | ⚠️ Gap (extra credit) |
| **Legal right to work in US** | F-1 STEM OPT -- current right to work; H-1B sponsorship needed long-term | ⚠️ Sponsorship risk |

---

## C) Level and Strategy

**Domain mismatch is the primary issue.** SiriusXM wants a platform engineer -- someone who builds CDK libraries, standardizes IaC patterns, and owns developer experience tooling. This is a DevOps/SRE-adjacent role, not a backend application engineer role. Her 9yr career is in application-layer backend services and data pipelines. The work she's done is *on top of* cloud infrastructure, not *building and standardizing* the infrastructure layer itself.

**CDK gap is concrete and required.** "Developing CDK libraries and Infrastructure-as-Code patterns" is the first substantive description of what this person will actually do. CDK (AWS Cloud Development Kit) with CloudFormation is explicitly required. She has AWS production experience but has never worked in IaC or platform engineering.

**Senior at SiriusXM (~10,000 employees).** Same formal-leveling concern that applies to large companies. -0.5 penalty.

**Sponsorship flag.** "Must have the legal right to work in the U.S." is not an explicit no-sponsorship statement, but it strongly implies no H-1B sponsorship. She is on F-1 STEM OPT and currently has the legal right to work -- but this language typically signals they won't sponsor future visa status. Flag at recruiter screen before investing time.

**AI integration piece is interesting but insufficient.** "Integrate AI-driven tooling into the platform" is one bullet of many. AgentProbe + LangGraph are directly relevant -- but this is a small fraction of the role. It doesn't outweigh the domain and IaC gaps.

---

## D) Comp and Demand

| Source | Range | Notes |
|--------|-------|-------|
| Disclosed | $100,800 -- $170,000 | + short/long-term incentives |
| Assessment | Good range, but role is a poor fit | Irrelevant given gaps |
| H-1B | "Must have legal right to work" -- likely no sponsorship | Confirm at screen before applying |

---

## G) Posting Legitimacy

**High Confidence.** SiriusXM is a real, verifiable large company. Detailed JD with specific technical requirements. No ghost posting signals.

---

## Recommendation: SKIP (2.5/5 -- below 3.5 threshold)

**Two hard problems:**
1. CDK/CloudFormation/IaC = required, not in stack
2. Platform Engineering / DevEx = wrong domain entirely

Additional concerns: sponsorship unclear ("legal right to work" language), Senior at 10,000+ employee formal company.

The AI integration piece and Python/AWS/TypeScript overlap aren't enough to overcome a domain mismatch this significant.

---

## Machine Summary

```yaml
report: 384
company: SiriusXM
role: Senior Software Engineer -- Platform Engineering
date: 2026-09-21
score: 2.5
archetype: Platform Engineering / DevOps / DevEx
legitimacy: High Confidence
url: null
status: SKIP
hard_blocks:
  - CDK/CloudFormation/IaC (core required skill -- absent from stack)
  - Platform Engineering / Developer Experience domain (not her domain)
  - Senior at SiriusXM (~10,000 employees -- formal leveling concern)
  - Sponsorship risk ("must have legal right to work in US" language)
gaps:
  - IaC tooling (CDK, CloudFormation)
  - Datadog / observability platforms
  - AWS certifications
comp_range: $100,800--$170,000 (+ incentives)
```
