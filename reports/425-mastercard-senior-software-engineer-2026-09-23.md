# Evaluation: Mastercard -- Senior Software Engineer, Identity Solutions

**Date:** 2026-09-23
**URL:** (pasted directly, no URL provided)
**Archetype:** Enterprise Java Platform Engineering -- Authentication / Identity / Fraud Prevention
**Score:** 3.6/5
**Legitimacy:** High Confidence
**PDF:** ✅ (score corrected from initial 2.5 -- Java/Spring Boot confirmed strong; income fraud verification is domain overlap)
**Location:** O'Fallon, MO (near St. Louis)
**Comp:** $115,000–$184,000 (O'Fallon, MO) + bonus + equity + benefits

---

## A) Role Summary

| Dimension | Detail |
|-----------|--------|
| Archetype | Enterprise Java Platform Engineer -- authentication, identity verification, fraud prevention; Java + Spring Boot primary; cloud-native; security engineering |
| Domain | Mastercard (~25,000 employees); Identity Solutions platform; payments, 200+ countries; authentication + fraud prevention |
| Function | Java/Spring Boot REST APIs; cloud-native microservices (AWS/Docker/K8s); secure coding + CVE remediation; performance engineering; code reviews + mentoring |
| Seniority | Senior Software Engineer at Mastercard (~25K employees) -- formal leveling; rejection pattern risk; identity platform context may evaluate differently from pure SWE |
| H-1B | **Likely yes** -- Mastercard is a major H-1B filer (large multinational); no explicit exclusion in JD |
| Location | O'Fallon, MO (near St. Louis) · $115K-$184K -- confirmed user open to any US location |
| TL;DR | Java + Spring Boot confirmed strong (in cv.md, in production at Entrata India). Income fraud verification at affordable housing (fake paystub detection, HUD eligibility manipulation) = direct domain overlap with Mastercard's fraud prevention platform. Authentication/identity protocols specifically are a gap. Senior at 25K formal-leveling company is a risk. Score corrected to 3.6 -- Evaluated. CV generated. |

---

## B) Match with CV

| JD Requirement | CV Match | Strength |
|----------------|----------|----------|
| **Java + Spring Boot REST APIs** | **Java + Spring Boot in cv.md skills; Java used at Entrata India for property management modules; user confirmed strong Java/Spring Boot** | ✅ Strong |
| Cloud (AWS/Azure/GCP) + Docker + K8s | AWS (S3/EC2/RDS/IAM), Docker, K8s | ✅ Strong |
| CI/CD pipelines | GitHub Actions | ✅ Present |
| Performance engineering | 200+ SQL optimizations (30% gain), microservices redesign (50% scalability gain) | ✅ Strong |
| Secure coding + CVE remediation | HIPAA PHI compliance at Entrata (7yr, zero incidents), Libsodium encryption, AWS IAM, RBAC | ✅ Present |
| **Fraud prevention domain** | **Entrata: income fraud verification at affordable housing -- HUD eligibility fraud detection, fake paystub patterns, 1.6M income verification records over 5 years** | ✅ Direct overlap |
| Identity verification | HUD eligibility verification (who qualifies for housing) -- document + income fraud detection | ✅ Adjacent |
| Authentication / SSO / OAuth / identity protocols | Not in portfolio (HIPAA RBAC is access control, not authentication protocols) | ❌ Gap |
| Kafka / event-driven (preferred) | RabbitMQ async processing (designed retry logic, idempotency guarantees at Entrata) | ⚠️ Adjacent |
| Unit / integration tests | Mentioned in AgentProbe CI regression gate; expected at Entrata scale | ✅ Present |
| Senior at Mastercard (25K employees) | Senior IC at Entrata; no prior Senior at formal-leveling company -- rejection pattern | ❌ Risk |
| Payments / fintech (preferred) | No direct payments experience | ❌ Gap |
| AI/automation tools in dev workflows (preferred) | Claude Code daily ✅ | ✅ Nice-to-have hit |
| Mentoring + code reviews | 5+ engineers mentored; 300+ peer code reviews at Entrata | ✅ Strong |

---

## C) Scoring

**Java + Spring Boot confirmed strong -- initial score was incorrect.** Spring Boot is listed in cv.md skills. Java was used in production at Entrata India for property management and affordable housing modules. User explicitly confirmed strong Java/Spring Boot proficiency. The initial stack mismatch assessment was wrong -- this removes the primary gap from the earlier 2.5/5 SKIP evaluation.

**Income fraud verification = meaningful domain overlap.** Entrata work included detecting fraudulent income claims, fake paystub patterns, and HUD eligibility manipulation at affordable housing (1.6M income records across 5 years, compliance-critical with zero violations). This is not identical to payment fraud at Mastercard's scale, but it is the same discipline: pattern detection on financial/income records, regulatory compliance, data integrity. The 180,000-record HUD pipeline and income eligibility enforcement demonstrate exactly the kind of fraud-domain judgment Mastercard's team values.

**Authentication/identity protocols are a real gap.** The team works on authentication solutions -- OAuth, OIDC, SSO, digital identity verification. Parimala's security work is compliance-centric (HIPAA, PHI, RBAC, encryption at rest) not protocol-centric. This gap is visible at technical screen.

**Senior at Mastercard (25K employees).** Same rejection pattern risk as AppFolio/Amazon/Juniper Square. However: the identity solutions platform evaluates fraud domain knowledge and Java/Spring Boot depth alongside general SWE leveling. The domain overlap reduces the bar relative to a generic Senior SWE screen.

**O'Fallon MO.** Near St. Louis. User memory confirms open to any US location. Not a concern.

---

## D) Comp and Demand

| Source | Range | Notes |
|--------|-------|-------|
| Disclosed | **$115,000–$184,000** (O'Fallon, MO) + bonus + equity | Competitive for Midwest; Mastercard benefits are strong |
| H-1B | **Likely yes** -- Mastercard is a major H-1B filer, global operations | Confirm at first contact |
| Location | O'Fallon, MO | User open to any US location |

---

## E) Red Flags

- **Authentication/identity protocols** -- OAuth, OIDC, SSO not in portfolio; RBAC/compliance present but different
- **Senior at Mastercard (25K employees)** -- same rejection pattern; fraud domain context may differentiate
- **Kafka absent** -- RabbitMQ async design present; similar patterns, different tool
- **Payments domain** -- income fraud adjacent but not payments-specific

---

## F) Recommendation: Evaluated (3.6/5)

Java/Spring Boot confirmed strong + income fraud verification domain overlap + security compliance depth (HIPAA/PHI/Libsodium/AWS IAM) + AWS/Docker/K8s/CI/CD all present. Authentication protocol gap is real but addressable. Lead with income fraud detection at HUD housing + Java/Spring Boot production depth. Apply if H-1B confirmed and O'Fallon MO is acceptable.

---

## Machine Summary

```yaml
report: 425
company: Mastercard
role: Senior Software Engineer, Identity Solutions
date: 2026-09-23
score: 3.6
archetype: Enterprise Java Platform Engineering -- Authentication / Fraud Prevention
legitimacy: High Confidence
url: null
status: Evaluated
gaps:
  - Authentication protocols (OAuth/OIDC/SSO) -- not in portfolio
  - Senior at 25K formal-leveling company -- rejection pattern risk
  - Kafka absent (RabbitMQ adjacent)
  - Payments domain -- income fraud adjacent, not payments-specific
strengths:
  - Java + Spring Boot confirmed strong (cv.md + user confirmed)
  - Income fraud verification at Entrata (HUD eligibility fraud, fake paystubs, 1.6M records 5yr)
  - Security/compliance depth: HIPAA, Libsodium, AWS IAM, RBAC, zero violations 7yr
  - AWS (S3/EC2/RDS/IAM) + Docker + K8s + CI/CD
  - Performance engineering: 200+ SQL optimizations, microservices at scale
  - 300+ code reviews + 5+ engineers mentored
  - Claude Code (AI tools preferred nice-to-have) ✅
note: Score corrected from initial 2.5/5 SKIP -- Java/Spring Boot was incorrectly flagged as absent
h1b: Likely yes -- Mastercard major H-1B filer; confirm at screening
comp_range: $115,000-$184,000 + bonus + equity (O'Fallon, MO)
location: O'Fallon, MO (near St. Louis) -- user open to any US location
```
