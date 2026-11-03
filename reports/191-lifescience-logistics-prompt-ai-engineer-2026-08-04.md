# Evaluation: LifeScience Logistics — Prompt / AI Engineer

**Date:** 2026-08-04
**URL:** via paste (no public URL provided)
**Archetype:** Applied AI Engineer — Prompt Engineering + RAG in pharmaceutical 3PL logistics
**Score:** 2.5/5
**Legitimacy:** High Confidence
**PDF:** ❌

---

## A) Role Summary

| Dimension | Detail |
|-----------|--------|
| **Archetype** | Prompt Engineer / Applied AI — prompt library, RAG pipelines, LLM eval harnesses for a pharmaceutical 3PL company |
| **Domain** | Supply chain / pharmaceutical logistics — WMS, EDI (850/810/856), DSCSA, SOP repositories |
| **Function** | Build + champion — prompt infrastructure, RAG pipelines over internal data, eval harnesses, cross-team enablement |
| **Seniority** | Mid (3+ years SWE/applied AI, 1+ year LLM focus) |
| **Location** | Full on-site ("work is performed in office") — LifeScience Logistics HQ is Coppell TX (Dallas area); relocation required from Virginia |
| **H-1B** | Not stated — LifeScience Logistics is a specialty 3PL, not a known tech H-1B sponsor; must verify; elevated risk |
| **Comp** | Not disclosed — logistics company AI role, likely $80K–$120K (below tech market for prompt/AI engineers) |
| **Physical** | Unusual for an AI role: "frequent walking," "occasional lifting of 25 lbs" — signals operational warehouse-adjacent environment |
| **TL;DR** | Prompt engineering and RAG skills are a genuine match. Three blockers stack up: supply chain/3PL/WMS/EDI/DSCSA domain is completely outside Parimala's background; H-1B sponsorship uncertain at a logistics company; full on-site Coppell TX with physical requirements. Score 2.5 — SKIP. |

---

## B) Match with CV

| JD Requirement | CV Evidence | Strength |
|----------------|-------------|----------|
| Advanced prompting: chain-of-thought, few-shot, XML-structured inputs | LeaseI prompt design + safety boundaries; AgentProbe multi-provider prompt evaluation; Magizhs natural-language → structured output | Strong |
| RAG pipelines | LeaseI TF-IDF RAG (section-aware chunking, citation correctness); AgentProbe ChromaDB RAG | Strong |
| LLM eval harnesses — quality, consistency, regression | AgentProbe 5-metric CI-integrated eval; regression gate on every commit | **Direct proof point** |
| PII handling rules, guardrails, refusal behavior | Entrata 100% PHI compliance (Libsodium); LeaseI safety boundary — never auto-resolves regulated calls for tenants | Strong |
| Regulated industry experience (pharma/healthcare/financial services) | Entrata = federal housing compliance (LIHTC, HUD, AMI) — regulated-domain mindset, not pharma | Partial analogue |
| OCR pipelines / IDP | LeaseI OCR-fallback ingestion for lease PDFs | Partial |
| Python | Primary language, 8+ years | Strong |
| Vector databases (Pinecone, Weaviate, pgvector) | ChromaDB (different product; same paradigm) | Partial |
| Claude Desktop + MCP server configuration | Uses Claude Code (different product; both Claude ecosystem) | Partial — Claude Code ≠ Claude Desktop MCP |
| Prompt injection testing / adversarial red teaming | LeaseI malicious input edge case testing (tenant-facing safety); not formalized red teaming | Weak |
| A/B testing prompt variants + performance benchmarks | AgentProbe per-run metrics, drift detection; not classical A/B framework | Partial |
| **Supply chain / 3PL domain: WMS, EDI 850/810/856, DSCSA** | No experience — completely outside background | **Major gap** |
| **Logistics / pharmaceutical operations knowledge** | No experience | **Major gap** |
| Cross-functional champion (Operations, Control Tower, General Counsel) | Entrata cross-functional delivery (compliance, operations, product, finance across 120+ sprints) | Partial analogue |
| 3+ years SWE + 1 year LLM | 8+ years SWE, 1+ year LLM — exceeds | Exceeds |

---

## C) Level and Strategy

**Score: 2.5/5 — SKIP**

No viable path for three stacked reasons:

**1. Supply chain domain gap — not bridgeable at screen**
WMS (Warehouse Management Systems), EDI 850/810/856 (purchase orders, invoices, advance ship notices), and DSCSA (Drug Supply Chain Security Act) are listed under "Technical Expertise" — they're not soft preferences. A prompt engineer building RAG pipelines over WMS and EDI logs needs to understand what those systems contain, how the data is structured, and what the business logic looks like. Parimala has zero exposure to pharmaceutical 3PL operations. At a first screen, this becomes apparent fast.

**2. H-1B uncertain at a logistics company**
LifeScience Logistics is a specialty pharmaceutical 3PL. This type of company rarely has the legal infrastructure to sponsor H-1B cap petitions. Not a known sponsor. If they can't sponsor, the entire conversation ends at the visa question.

**3. Full on-site with physical requirements + Coppell TX relocation**
"Work performed in office" + "frequent walking" + "occasional lifting of 25 lbs" — this is a warehouse-adjacent operational environment, not a tech office. Full relocation to the Dallas suburbs for a logistics company AI role that likely pays $80K–$120K is not a strong trade.

**What's genuine:** Prompt engineering, RAG, eval harnesses, guardrails, and PII handling are all real strengths. If this were a tech company with a domain Parimala knows, it would score higher.

---

## D) Comp and Demand

| Item | Data |
|------|------|
| Disclosed salary | Not disclosed |
| Market estimate | $80K–$120K (logistics company AI role, not tech-company comp) |
| Bonus / equity | Likely modest; 3PL companies are not equity-generous |
| H-1B | Uncertain — not a known sponsor |
| Location | Full on-site, Coppell TX — relocation from Virginia required |
| Interview | Likely 2–3 rounds (non-tech company) |
| Comp score | 2/5 — undisclosed at logistics company, likely below target |

---

## E) Customization Plan

Not applicable — SKIP.

---

## F) Interview Plan

Not applicable — SKIP.

---

## G) Posting Legitimacy

| Signal | Finding | Weight |
|--------|---------|--------|
| Company | LifeScience Logistics — real pharmaceutical 3PL operating company | Positive |
| Role coherence | Prompt engineer building RAG over WMS/EDI/SOP data = coherent and real need | Positive |
| Physical requirements | "Lifting 25 lbs / frequent walking" in an AI role — operational environment, not pure tech | Neutral |
| H-1B | Not stated — logistics company, not a typical H-1B sponsor | Concern |
| No URL | Came via paste — verify posting is active | Neutral |
| Comp | Undisclosed — logistics company AI comp typically below tech market | Neutral |

**Assessment: High Confidence** — Real company, real need. Fit issues are about candidate match, not posting legitimacy.

---

## Machine Summary

```yaml
company: LifeScience Logistics
role: Prompt / AI Engineer
date: 2026-08-04
score: 2.5
archetype: Applied AI Engineer — Prompt Engineering + RAG (pharmaceutical 3PL)
legitimacy: High Confidence
compensation: not disclosed (~$80K-$120K estimated)
h1b: uncertain (3PL logistics company, not a known H-1B sponsor)
location: Full on-site, Coppell TX (relocation required from Virginia)
verdict: skip
key_gap: supply chain / 3PL domain (WMS, EDI 850/810/856, DSCSA) completely outside background; H-1B uncertain; full on-site relocation + physical requirements for logistics environment
key_strength: prompt engineering (chain-of-thought, few-shot, XML), RAG pipelines, LLM eval harnesses, PII/guardrails — all genuine; regulated-industry analogue from Entrata
```

---

## Keywords extracted

Prompt Engineering, Chain-of-Thought, Few-Shot, RAG, WMS, EDI, DSCSA, Claude Desktop, MCP, LLM Evaluation, Guardrails, PII Handling, Prompt Injection, Red Teaming, Vector Database, OCR, IDP, Supply Chain, Pharmaceutical Logistics, 3PL, Python
