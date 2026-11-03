# Evaluation: Parakeet Health -- Software Engineer (AI Products)

**Date:** 2026-09-22
**URL:** (pasted directly, no URL provided)
**Archetype:** Applied AI Engineer / Forward Deployed Engineer (Healthcare AI)
**Score:** 4.4/5
**Legitimacy:** High Confidence
**PDF:** ✅
**Location:** San Francisco, CA (In-person, Downtown SF -- Montgomery BART) · Relocation stipend offered
**Comp:** Not disclosed · Series A-level SF startup ($13M raised, 10x ARR) · est. $140–175K base + meaningful equity

---

## A) Role Summary

| Dimension | Detail |
|-----------|--------|
| Archetype | Applied AI Engineer / FDE -- build production AI agents for healthcare practices; HITL ownership; customer-facing; fast-shipping culture |
| Domain | Parakeet Health -- AI voice agent platform for medical practices; 2yr old; 400+ practices, 27 specialties; One Medical CEO (Tom Lee) as investor; $13M+ raised; 10x ARR growth; SOC 2 + HIPAA compliant |
| Function | Build end-to-end AI agent use cases (voice, fax, referrals, scheduling, billing); own HITL guardrails + conversation design; eval infrastructure; close to customers |
| Seniority | "3-7 years relevant engineering experience" -- startup leveling; no formal ladder; founding engineer territory; Parimala is above YOE cap but fit is strong (9yr SWE + 2yr AI = exactly what they need) |
| Location | **Full onsite, Downtown SF** · Relocation stipend provided · User is open to SF |
| Company | Parakeet Health (parakeethealth.com) · Founded 2023 · CTO: Aaron Lee (ex-Rippling, Twitter) · CEO: Jung Park (One Medical, PhD ops research) · CPO: Eric Mao (ML/NLP pre-ChatGPT) · ~10-15 engineers |
| TL;DR | Best role fit of the pipeline on paper. LeaseI HITL architecture maps directly to their core engineering problem. AI on FHIR + Entrata PHI = verified HIPAA credentials. AgentProbe = their eval infrastructure goal. Django is missing (Flask/FastAPI instead) -- only real gap. SF onsite requires relocation. Score 4.4 -- APPLY. Include 🦜 in the application. |

---

## B) Match with CV

| JD Requirement | CV Match | Strength |
|----------------|----------|----------|
| Python | Python 9yr; FastAPI, Flask, production scale | ✅ Strong |
| **Django** | **Not in stack -- Flask/FastAPI instead** | ❌ Gap |
| React | React.js at Entrata (20+ modules); AI on FHIR | ✅ Present |
| HIPAA compliance | AI on FHIR (HIPAA, RBAC, PHI); Entrata S3 migration (100% PHI compliance, zero incidents) | ✅✅ Exact |
| HITL + knowing when the agent should stop | LeaseI: HITL escalation on regulated decisions; confidence scoring; safety boundary for tenant eligibility questions (never auto-resolved by AI) | ✅✅ Exact |
| Eval systems: "tell good fix from confident wrong answer" | AgentProbe: CI-integrated regression gate, LLM-as-judge scoring, hallucination detection, pass@k harness | ✅✅ Exact |
| Document intelligence / fax processing | LeaseI: OCR-fallback ingestion, section-aware chunking, structured data extraction from PDFs | ✅ Direct |
| Agentic AI / LLM systems in production | LeaseI (8-agent LangGraph, 1,240 test cases, 93.6% precision); AgentProbe; Magizhs (client delivery) | ✅ Strong |
| Fast shipping, customer-facing delivery | Magizhs: production LangGraph system for external client, architecture → deployment; Entrata: 20+ modules, 120+ sprints | ✅ Present |
| Voice/conversation design | Not in portfolio -- HITL and guardrails principles transfer; no direct voice AI experience | ⚠️ Gap |
| Early-stage startup experience | Magizhs is closest (small consulting shop, client delivery); no prior startup employment | ⚠️ Partial |
| Scalable backend systems | Entrata: 100K+ MAU, RabbitMQ async, microservices, 200+ SQL optimizations | ✅ Strong |
| Ownership + product judgment | 7yr HUD pipeline (zero violations); Magizhs end-to-end; LeaseI product design decisions (eligibility → human only) | ✅ Strong |

---

## C) Scoring

**Why this is the best role fit in the current pipeline.** Parakeet Health's hardest engineering problem -- building systems that know when to hand off to a human, with low margin for error on real patient data -- is exactly what LeaseI is designed to solve. The JD says: *"Building systems that know not just what to say but when -- and that route edge cases to a human without grinding everything to a halt -- is some of the most consequential work we're doing."* LeaseI's core design rule, enforced in code: the LLM extracts and reasons; a human or deterministic logic makes every final regulated call. That is the same principle. Eligibility questions always route to staff, never resolved by AI. That's the same safety boundary they're building for patient diagnoses and compliance-sensitive disclosures.

**Eval infrastructure match.** The JD: *"evaluation systems that can tell the difference between a good fix and a confident wrong answer."* AgentProbe is exactly that -- 5-metric eval engine, LLM-as-judge, hallucination detection, CI-integrated regression gate. This is the proof point for their "agents crawling Datadog logs and fixing bugs autonomously" vision. They want to know if agent fixes are trustworthy before they hit production. So does AgentProbe.

**HIPAA depth is rare and verified.** Two independent proof points: AI on FHIR (PHI + RBAC + FHIR APIs) and Entrata PHI compliance (AWS S3 migration, Libsodium encryption, zero incidents across 7yr). Most AI candidates have neither. Healthcare AI requires both the technical capability and the instinct for what data can flow where -- that instinct comes from actually owning it, which she has.

**Fax / document AI use case is live in her portfolio.** Parakeet's breakout product: turn 50,000 faxes/month into automated scheduling, cutting 5-7 days to 1 minute. LeaseI does the same thing with residential lease PDFs: OCR ingestion, structured data extraction, document intelligence. The domain is different; the technical architecture is identical.

**Django is a real gap.** They list "Expertise in Python, Django, and React" as a hard requirement. Parimala has Python (9yr) and React but not Django. Django is a Python web framework -- the transition from Flask/FastAPI is a few days for an experienced Python dev, not months. But it should be addressed directly in the cover letter rather than papered over. Aaron Lee (ex-Rippling, ex-Twitter) will know the difference between framework expertise and Python depth.

**Voice AI is absent from the portfolio.** The JD spends significant time on voice/conversation design ("cadence and intonation matter"). Nothing in Parimala's work involves voice. This is a genuine gap. However, the underlying judgment problems -- when to escalate, how to fail safely, how to evaluate edge cases -- are exactly what she has built. Voice is a new medium for the same principles.

**SF onsite.** Full in-person required. Relocation stipend provided. User memory confirms she is open to SF. Not a score penalty.

**H-1B.** $13M raised, Series A-level, 10-15 engineers -- can afford H-1B sponsorship (~$5-15K legal cost). CTO Aaron Lee was at Rippling (one of the largest H-1B filers in tech). This is a much stronger sponsorship signal than a seed startup. Confirm at first call, but not a blocking concern here.

**Boosts applied:**
- Healthcare AI + HIPAA domain (AI on FHIR direct proof point) → +0.3
- HITL + eval infrastructure = exact match to their core engineering problems
- Applied AI / FDE archetype = profile priority #1

**🦜 Note for application:** The JD ends with *"Include a 🦜 in your application for extra credit."* Include it. This is a read-the-whole-thing test and signals product judgment and attention to detail.

---

## D) Comp and Demand

| Source | Range | Notes |
|--------|-------|-------|
| Disclosed | **Not disclosed** | Series A-level SF startup with 10x ARR growth |
| Estimated | **$140,000–$175,000 base** + 0.1–0.3% equity | Standard for Series A SF engineering; meaningful equity at this growth stage |
| H-1B | **Likely yes** -- $13M raised, CTO from Rippling (major H-1B filer) | Confirm at screening |
| Location | SF onsite (Montgomery BART) · relocation stipend | User open to SF |
| Benefits | Health/dental/vision, fitness stipend, commuter benefits, free dinner, unlimited PTO, 401k, relocation stipend | Solid for startup stage |

---

## E) Red Flags

- **Django absent** -- Flask/FastAPI instead; address directly in cover letter
- **No voice AI experience** -- HITL and eval principles transfer; direct voice work does not
- **SF onsite** -- requires relocation from Virginia; relocation stipend provided
- **3-7yr YOE cap** -- Parimala has 9yr total; not a hard block at startup but she's above it
- **No prior startup employment** -- Magizhs is the closest; Entrata was 1,000+ employee SaaS

---

## F) Recommendation: APPLY (4.4/5)

This is the strongest technical + cultural fit in the current pipeline. LeaseI HITL architecture, AgentProbe eval infrastructure, AI on FHIR healthcare compliance, and Entrata PHI depth all map directly to Parakeet Health's hardest engineering problems. Django is a learnable gap; voice AI is a genuine new domain that the underlying judgment skills do transfer to. The comp and equity upside at 10x ARR growth is meaningful. Apply immediately. Include 🦜.

**Cover letter hook:** Open with the LeaseI design rule -- "the LLM reasons; a human makes every final regulated call" -- and show that their patient-diagnosis safety boundary is the same problem already solved in code.

---

## Machine Summary

```yaml
report: 416
company: Parakeet Health
role: Software Engineer (AI Products)
date: 2026-09-22
score: 4.4
archetype: Applied AI Engineer / Forward Deployed Engineer (Healthcare AI)
legitimacy: High Confidence
url: null
status: Apply
gaps:
  - Django not in stack (Flask/FastAPI instead) -- address in cover letter
  - No voice AI experience -- HITL/eval principles transfer, direct voice does not
  - SF onsite requires relocation (relocation stipend provided)
  - Above 3-7yr YOE cap (9yr total) -- not a hard block at startup
  - No prior startup employment
strengths:
  - LeaseI HITL architecture = exact match to core Parakeet engineering problem
  - AgentProbe eval infrastructure = exact match to "good fix vs confident wrong answer"
  - AI on FHIR + Entrata PHI = verified HIPAA depth (rare, two independent proof points)
  - LeaseI document/OCR ingestion = direct analogue to fax processing product
  - 9yr Python production + React + FastAPI
  - Healthcare domain knowledge (AI on FHIR)
  - Fast shipping culture fit (Magizhs client delivery)
h1b: Likely yes -- $13M funded; CTO ex-Rippling (major H-1B filer); confirm at screening
comp_range: est. $140,000-$175,000 base + 0.1-0.3% equity (Series A SF)
location: Full onsite, Downtown SF (Montgomery BART) · relocation stipend offered
easter_egg: Include 🦜 in application
```
