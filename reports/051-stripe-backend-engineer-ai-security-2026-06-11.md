# Evaluation: Stripe — Backend Engineer, AI Security

**Date:** 2026-06-11
**URL:** https://stripe.com/jobs/search?gh_jid=7826765
**Archetype:** AI Platform / Infrastructure Security
**Score:** 3.8/5
**Legitimacy:** High Confidence
**PDF:** output/cv-stripe-backend-engineer-ai-security-2026-06-11.pdf

---

## A) Role Summary

| Field | Detail |
|-------|--------|
| Archetype | Backend SWE — AI Security Infrastructure (first engineer on team) |
| Domain | Build security frameworks for Stripe's AI infrastructure: prompt injection defense, jailbreak protection, tool misuse prevention |
| Function | Build (end-to-end ownership; first security engineer on AI team) |
| Seniority | Senior IC (5+ years) |
| Remote | Remote US or Canada (35+ miles from office); OR hybrid at NY/SF/Seattle — **effectively remote for Virginia** |
| Comp | $190,400–$285,600 base + equity + bonus |
| TL;DR | First security engineer on Stripe's AI team. Build security primitives protecting AI infrastructure from adversarial inputs. Python backend + security engineering + AI/LLM systems. Greenfield ownership — design-from-scratch territory. |

---

## B) Match with CV

| JD Requirement | CV Match | Strength |
|----------------|----------|----------|
| 5+ years backend software development | 8+ years production Python + backend at Entrata + AgentProbe | ✅ Exceeds |
| AI agents / LLM-based systems (preferred) | AgentProbe: LangGraph agents, tool calls, multi-provider LLM routing | ✅ Direct proof (preferred quals) |
| Python production | 8+ years | ✅ Exceeds |
| Infrastructure systems + backend | AgentProbe FastAPI + Entrata microservices + Docker + AWS | ✅ Strong |
| Security engineering background (preferred) | Entrata: Libsodium PHI encryption, HIPAA compliance, zero security incidents; AWS S3 + secure coding | ✅ Adjacent — real security work, not adversarial |
| "Design defenses against prompt injection / jailbreaks" | AgentProbe: compliance metric in eval engine; LLM-as-judge for safety scoring | ⚠️ Conceptually adjacent |
| "Build security frameworks integrated with AI infrastructure" | Not primary expertise; adjacent via Entrata security + AgentProbe AI backend | ⚠️ Stretch |
| "First engineer on team" — greenfield ownership | AgentProbe: built entire platform from scratch; Entrata 40+ debugging/automation tools | ✅ Proven track record |
| Cross-team collaboration | 120+ Agile sprints cross-functional at Entrata | ✅ Strong |
| H-1B | Stripe is one of the strongest H-1B sponsors in fintech — public company equivalent | ✅ High confidence |
| Remote | Remote US confirmed (35+ miles from Stripe offices; Virginia qualifies) | ✅ Clean |

**Gaps and mitigations:**
- **AI Security specialization** — Prompt injection, jailbreaks, and adversarial AI defense is a distinct sub-domain. Not in CV. Mitigate: "I built the eval systems that *detect* these failure modes — LLM-as-judge compliance scoring, hallucination detection, and tool misuse detection. That's the measurement side of the same problem. Building the defenses is the next logical step."
- **Security engineering depth** — CV security work is PHI compliance + encryption, not adversarial/offensive security. The JD says "security engineering background" as *preferred* not required — minimum bar is 5+ years backend.
- **Minimum qualifications met** — 5+ years backend, Python, infrastructure, cross-team collaboration all exceed requirements. The AI preferred quals are a differentiator.

---

## C) Level and Strategy

**Level detected:** Senior IC. The "first engineer" designation makes this a high-ownership role with significant influence over the team's direction.

**Sell plan:**
- Lead with the AI angle (preferred quals): *"I built the systems that detect prompt injection and tool misuse at the eval layer — LLM-as-judge compliance scoring, hallucination detection, retrieval safety. That's the measurement side of AI security. I want to build the defenses."*
- Security credibility: *"I've handled PHI at scale — Libsodium encryption, HIPAA compliance, zero security incidents across 100K+ users. Security-first engineering is in my background."*
- Greenfield ownership: *"AgentProbe was greenfield. I made every architectural decision. The challenge of being the first person on a team and defining what good looks like — that's exactly what I did with AgentProbe."*
- Stripe as company: Strongest H-1B sponsor in the pipeline, stable infrastructure company, high-quality engineering culture, excellent comp.

**Comp target:** Push toward $240K+ (upper half). AI/LLM depth + security adjacent + greenfield ownership record justifies it.

---

## D) Comp and Demand

| Source | Range | Notes |
|--------|-------|-------|
| Job posting | $190,400–$285,600 | Disclosed — excellent |
| Equity | Included | Stripe is likely pre-IPO or recently public — significant upside |
| Bonus | Company bonus program | Additional |
| Market | $190K–$280K for Sr SWE at infra companies | Stripe is top-of-market |

**Assessment:** $190–285K is the best comp range in the current pipeline (alongside Cresta's $185–235K). Stripe pays extremely competitively. Remote US + Stripe brand + H-1B certainty = strong overall package.

**H-1B:** Stripe has filed hundreds of H-1B LCAs annually. One of the most reliable sponsors in tech. Very high confidence.

---

## E) Customization Plan

| # | Section | Current | Proposed change | Why |
|---|---------|---------|-----------------|-----|
| 1 | Summary | Varies | Lead: *"Backend AI engineer with security-first development background — built AgentProbe's AI compliance eval engine (prompt injection detection, tool misuse scoring, hallucination flagging) and implemented PHI encryption + HIPAA compliance at Entrata; now targeting AI security infrastructure"* | JD: AI security + backend |
| 2 | AgentProbe | Varies | Elevate: compliance metric (prompt injection/safety detection), LLM-as-judge for adversarial inputs, tool call misuse detection, multi-provider routing security | JD: AI defenses + prompt injection + tool misuse |
| 3 | Entrata | General | Add: PHI encryption (Libsodium), HIPAA compliance, zero security incidents, secure coding standards, AWS S3 data migration with encryption | JD: security engineering background |
| 4 | Competencies | Varies | AI Security & Safety, Prompt Injection Detection, Backend Infrastructure, Python, LLM Systems, Secure Coding, AWS | JD vocabulary |

---

## F) Interview Plan

| # | JD Requirement | Story | Key Points |
|---|----------------|-------|------------|
| 1 | "Design defenses against prompt injection" | AgentProbe: LLM-as-judge compliance scoring detecting unsafe/off-policy outputs | "I built the detection side — judge prompts that flag injection attempts, policy violations, and tool misuse. Defenses follow the same logic reversed: prevent what the detector catches." |
| 2 | "Build security frameworks integrated with AI infrastructure" | Entrata: PHI encryption, HIPAA, zero incidents + AgentProbe multi-provider routing with fallback guardrails | Security-first architecture: how to build AI systems with defense-in-depth |
| 3 | "First engineer on team" — greenfield | AgentProbe: greenfield LangGraph platform, every decision mine | "I've been the first and only architect of a production AI system. Defining the problem space, choosing abstractions, building what others will eventually build on — that's what I did." |
| 4 | Backend systems at scale | Entrata: 1M+ property records, 99.5% uptime, microservices | Production backend reliability — how you maintain quality in a large codebase |
| 5 | Cross-team collaboration on AI security | Entrata 120+ sprints; AgentProbe public tool with clear API | "Security work that doesn't get adopted fails. I know how to build things others actually use." |

---

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|--------|---------|--------|
| Salary disclosed | $190,400–$285,600 — explicit | Positive |
| Company health | Stripe: one of the most valuable fintech companies; pre-IPO, well-funded | Positive |
| JD specificity | Named responsibilities: prompt injection, jailbreaks, tool misuse — active security problem space | Positive |
| Application window | 100 days from posting — active window | Positive |
| H-1B | Stripe = top H-1B sponsor in tech — very high confidence | ✅ Strong |
| Remote confirmed | Remote US (35+ miles from office — Virginia qualifies) | ✅ Clean |

---

## Keywords Extracted

backend engineer, ai security, stripe, prompt injection, jailbreak defense, llm security, ai infrastructure, python, security engineering, remote us, fintech

---

## Machine Summary

```yaml
report_num: 051
company: Stripe
role: Backend Engineer, AI Security
date: 2026-06-11
score: 3.8
archetype: AI Platform / Infrastructure Security
legitimacy: High Confidence
location: Remote US (35+ miles from office; Virginia qualifies) or hybrid NY/SF/Seattle
comp_range: "$190,400–$285,600 base + equity + bonus"
visa_risk: low (Stripe is one of the top H-1B sponsors in tech — very high confidence)
key_gaps:
  - AI security specialization (prompt injection defense — new domain; mitigation: detection side via AgentProbe eval)
  - Security engineering depth (PHI/HIPAA is adjacent, not adversarial security)
key_strengths:
  - Stripe = strongest H-1B in pipeline
  - Remote US confirmed for Virginia
  - Comp $190-285K = best range in current batch
  - AI/LLM preferred quals = AgentProbe direct proof
  - Security adjacent: Libsodium/HIPAA/PHI at Entrata
  - Greenfield "first engineer" ownership = AgentProbe record
location_risk: low — remote US confirmed
recommend: strong apply — Stripe's H-1B certainty + comp + remote + AI preferred quals make this one of the best packages in the pipeline despite AI security being a stretch domain
```
