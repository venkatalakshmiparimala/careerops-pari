# 287 — Leaf Health — Software Engineer, LeafEnterprise

**Date:** 2026-09-07
**Score:** 2.5/5 — SKIP (Comp $80K–$100K is far below market for 9+ years; role is positioned 1–3 years preferred = overqualification; Next.js/Tailwind required gaps; H-1B unknown at small company; healthcare compliance domain match is the strongest signal)
**URL:** https://leafhealth.com (inferred — not provided)
**PDF:** ❌
**Legitimacy:** High Confidence — Leaf Health is a real, established healthcare consulting firm (30+ years); specific platform name (LeafEnterprise), comp range disclosed, Austin TX hybrid; JD is detailed and credible

---

## Block A — CV Match

**Healthcare compliance domain is a genuine match via AI on FHIR (FHIR = healthcare data standard) and Entrata's regulated compliance work. Python, SQL, data pipelines all map directly. Next.js and Tailwind CSS are required but not in background. Overqualification is the structural concern.**

| JD Requirement | CV Proof Point |
|---------------|----------------|
| "Proficiency with Python, experience building CLI applications" | Python 9yr primary; LeaseI, AgentProbe, Magizhs: command-line operable, modular, local-first architecture ✓✓ |
| "TypeScript, React, Next.js, Tailwind CSS — responsive, accessible interfaces" | AI on FHIR: React.js/TypeScript frontend; TypeScript listed in skills — but NO Next.js or Tailwind CSS ✓/✗ |
| "Back-end services, APIs, SQL, data pipelines, integrations" | FastAPI (LeaseI, AgentProbe, 15-endpoint service); Entrata REST APIs; 200+ SQL optimizations; RabbitMQ pipelines ✓✓ |
| "Experience in healthcare, pharmacy benefits, regulated, contract-driven, data-intensive environment" (PREFERRED) | AI on FHIR: FHIR REST API integration, HIPAA-compliant RBAC, healthcare data; Entrata: 7yr HUD federal compliance pipeline (contract → data model → production) ✓✓ |
| "Use coding agents and MCP-based tools with appropriate human review and authorization controls" | Claude Code daily; AgentProbe (LLM evaluation + regression gate = quality control for AI outputs); MCP explicitly in background ✓✓ |
| "End-to-end ownership: requirements through operation, incident response, continued improvement" | LeaseI: 3-surface AI platform concept-to-production solo; AgentProbe: open-source eval platform end-to-end; Entrata: 7yr HUD pipeline full ownership ✓✓ |
| "Translate authoritative documents into traceable software" | Entrata: federal HUD income-limit spec → 180,000 domain records powering eligibility decisions — exactly this ✓✓ |
| "Modular design, domain logic portable and testable, isolate providers behind small interfaces" | AgentProbe: multi-provider routing with clean provider interfaces; LeaseI: deterministic guardrails separating domain logic ✓ |
| "Git, code review, automated testing, CI/CD" | GitHub Actions CI/CD; sub-10 bug count 6+ months; 300+ code reviews; CI-integrated regression gate ✓✓ |
| "Linux, SSH, Windows/PowerShell" | Linux production environments at Entrata; AWS EC2/Linux deployments; SSH workflows ✓/⚠️ |
| "OSI-informed layered-systems thinking" | Distributed systems design (RabbitMQ, Docker microservices, REST APIs, Redis, DB layers) ✓ |
| "Azure, AWS, containers, GPU deployments when requirements justify" | AWS S3/EC2/RDS/Glue; Docker containerization (50% scalability gain); CI/CD ✓ |
| Slurm, GPU/HPC workload profiling (preferred) | Not in background ✗ |
| C/C++, systems programming (preferred) | Not in background ✗ |

**Gaps:**
- **Next.js and Tailwind CSS** — both are explicitly required for the React frontend work; React/TypeScript is present (AI on FHIR) but Next.js (SSR framework) and Tailwind (utility CSS) are distinct enough to be interview gaps
- **Slurm/GPU/HPC** — preferred; not in background; not a primary concern
- **C/C++** — preferred; not in background

**ATS baseline:** ~16/20. Python ✓, healthcare domain ✓, API ✓, SQL ✓, CI/CD ✓, coding agents/MCP ✓, HIPAA/regulated ✓. Next.js and Tailwind missing.

---

## Block B — North Star Alignment

**Healthcare compliance is the strongest domain match outside PropTech — but the role is positioned at 1–3 years preferred experience and the comp ceiling reflects it.** "Exceptional recent graduates are encouraged to apply" is the tell: this is a mid-level role priced for early-career engineers. At 9+ years, the background is significantly beyond the target level.

Positives: ownership model (no ticket-driven, end-to-end accountability), local-first engineering philosophy, product-minded framing, and the explicit mention of coding agents + MCP all align with the working style. The healthcare compliance domain via AI on FHIR + Entrata federal compliance is a genuine differentiator for this specific role.

Negatives: comp ceiling is $100K for 9+ years — well below the market rate for any engineer at this experience level regardless of market. Growth ceiling at a 30-year-old healthcare consulting firm is different from startup equity upside. No PropTech boost applies.

**Score: 2.5/5**

---

## Block C — Compensation

**$80,000–$100,000 disclosed — significantly below market for 9+ years of production engineering experience.** Austin, TX is a lower cost-of-living market than NYC or SF, but $80K–$100K for a senior engineer in Austin tech is still early-to-mid career compensation (1–3yr range, matching the preferred experience stated). Performance incentives mentioned but unquantified. No equity component stated. Benefits package not detailed.

For context: EliseAI (same session, #281) estimated $160K–$230K for a similar ownership-model role. Google (#280) offered $147K–$210K base with bonus and equity. The comp ceiling here is ~50% of comparable opportunities.

**Score: 1.0/5**

---

## Block D — Cultural Signals

- "Not ticket-driven — anticipate risks, investigate defects, strengthen tests" — ownership culture aligns ✓
- "Local-first engineering model" — thoughtful, pragmatic engineering philosophy ✓
- "Coding agents and MCP-based tools with appropriate human review" — explicitly in the JD; matches working style ✓✓
- "Translate authoritative documents into correct, traceable software" — regulated compliance work, matches Entrata/HUD background ✓
- 30+ years in business — stable, not startup volatility; different risk profile ✓/⚠️
- Hybrid Austin, TX — relocation required; user open to any US location ✓
- H-1B: no sponsorship mention; small healthcare consulting firm — uncertain; a real concern

**Score: 3.5/5**

---

## Block E — Red Flags

1. **Comp $80K–$100K for 9+ years** — the single largest concern; this is early-career compensation applied to a senior background; even after removing the hard salary floor, this represents a significant trade-off
2. **Overqualification risk** — role targets 1–3 years preferred; "exceptional recent graduates encouraged"; 9+ years may be read as overqualified → flight risk
3. **Next.js + Tailwind required** — genuine technical gaps for the frontend half of this full-stack role
4. **H-1B sponsorship unknown** — no mention; small healthcare consulting firm; unconfirmed is a real risk
5. **Austin, TX hybrid** — relocation from Virginia required; not a scoring penalty but a logistical reality
6. **Growth ceiling** — 30-year-old consulting firm with no equity component; different career trajectory than Series A-E startup

**Adjustment: −0.5**

---

## Block F — Global Score

| Factor | Signal |
|--------|--------|
| CV match | 3.5 — Python ✓✓; healthcare/FHIR domain ✓✓; regulated compliance ✓✓; coding agents/MCP ✓✓; SQL/APIs/CI ✓; Next.js/Tailwind gaps |
| North Star | 2.5 — ownership model ✓; healthcare compliance domain ✓; but 1–3yr target = overqualification; no PropTech boost |
| Comp | 1.0 — $80K–$100K for 9+ years is far below market; no equity; performance incentives unquantified |
| Culture | 3.5 — local-first engineering ✓; no ticket-driven ✓; coding agents explicitly ✓; stable company |
| Red flags | −0.5 — comp far below market; overqualification; Next.js/Tailwind gaps; H-1B unknown |

**Global: 2.5/5 — SKIP**

> The healthcare compliance domain match is real — AI on FHIR (FHIR standard, HIPAA, RBAC) + Entrata's 7yr federal compliance pipeline ("translate authoritative documents into traceable software") is exactly what this role values. The engineering culture (local-first, ownership, coding agents) aligns well too. But $80K–$100K for 9+ years is the insurmountable number: it's approximately half of comparable roles in the pipeline, there's no equity component, and the role itself is sized for 1–3 years of experience. If Leaf Health had a senior or principal tier with appropriate compensation, this domain/culture match would score significantly higher. As written, passing is the right call.

---

## Block G — Posting Legitimacy

**High Confidence.** Leaf Health is a real, established healthcare consulting firm (3+ decades, specific platform name LeafEnterprise, real product domains — PBM consulting, claims auditing, rebate operations). Comp range is disclosed. Role is specific and detailed. No ghost indicators.

---

## Machine Summary

```yaml
company: Leaf Health
role: Software Engineer, LeafEnterprise
score: 2.5
status: SKIP
date: 2026-09-07
salary_low: 80000
salary_high: 100000
location: Austin, TX (hybrid; relocation required)
remote: false
visa: unconfirmed (small company — no mention of H-1B sponsorship)
proptech_boost: false
h1b_status: unconfirmed
top_match: Healthcare/FHIR domain; regulated compliance pipeline work; Python; coding agents/MCP; ownership model; local-first engineering culture
gaps: Comp far below market ($80K-$100K for 9yr+); overqualification (1-3yr target); Next.js + Tailwind required; H-1B unknown; no equity; Austin relocation
```
