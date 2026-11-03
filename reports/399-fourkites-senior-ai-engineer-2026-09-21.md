# Evaluation: FourKites -- Senior AI Engineer

**Date:** 2026-09-21
**URL:** (pasted directly, no URL provided)
**Archetype:** Agentic AI / Backend SWE (Supply Chain SaaS)
**Score:** 4.2/5
**Legitimacy:** High Confidence
**PDF:** output/cv-venkata-lakshmi-parimala-pasupuleti-fourkites-2026-09-21.pdf
**Location:** Remote / Chicago (hybrid for in-office employees -- commuter benefit listed, not required)
**Comp:** $140,000 -- $180,000 + bonus + stock options

---

## A) Role Summary

| Dimension | Detail |
|-----------|--------|
| Archetype | Agentic AI / Backend SWE -- Python + LangGraph primary; Java or GoLang secondary; 75-80% backend; builds and productionizes AI agents in production supply chain platform |
| Domain | FourKites supply chain visibility SaaS -- real-time shipment tracking, AI agents for carrier onboarding, support automation, voice (LLM + telephony) |
| Function | Design + build + productionize AI agents (support automation, voice, onboarding) in LangGraph; backend Python + Java; data models; K8s deployment; code reviews |
| Seniority | "Senior AI Engineer" at FourKites (~500-800 employees) -- supply chain SaaS, not a pure formal-leveling tech company; interview bar is agentic/backend-focused, not algorithmic |
| Location | Remote-friendly (no explicit requirement); Chicago commuter benefits for in-office; no location penalty |
| Company | FourKites -- Series E supply chain AI company; 1,600+ global enterprise customers (Walmart, Cardinal Health); ~500-800 employees |
| TL;DR | Stack match is direct: Python/LangGraph/PostgreSQL/Docker/K8s/React all present. LeaseI support investigation agent mirrors FourKites' support automation agent exactly. AgentProbe = their evaluation needs. Java present (early career). Mild concerns: Senior title at 500-800 employee company (below hard-block tier), Java dated (2017-2018), no supply chain domain, no voice/telephony agent experience. Score 4.2 -- Apply. |

---

## B) Match with CV

| JD Requirement | CV Match | Strength |
|----------------|----------|----------|
| 5+ years backend/SWE + AI/agentic exposure | 9yr (Entrata 7.5yr + GMU + Magizhs); LangGraph in production projects | ✅ Exceeds |
| **Python -- mandatory** | Python 9yr primary | ✅ Strong |
| **LangGraph (2+ years hands-on)** | LeaseI: 8-agent LangGraph StateGraph (HITL, conditional routing, tool calls); AgentProbe: LangGraph agents + eval; Magizhs: LangGraph mission-planning stateful graph | ✅ Strong (note: 2yr LangGraph caveat -- LangGraph itself is ~2yr old; she has genuine end-to-end production-grade work) |
| **Java or GoLang (proficiency in at least one)** | Java: Entrata India (property management modules, 2017-2018, 1.5yr) | ✅ Present; ⚠️ 8yr since primary Java use -- recency concern |
| OOP principles | Python OOP; Java/Spring Boot; PHP/Laravel | ✅ Strong |
| PostgreSQL / MySQL / MongoDB | PostgreSQL 9yr; MySQL present | ✅ Strong (no MongoDB) |
| React + JavaScript/HTML/CSS | React.js (AgentProbe, AI on FHIR); TypeScript; Angular; JavaScript | ✅ Present |
| RESTful APIs + microservices | FastAPI 15-endpoint REST; RabbitMQ; Docker microservices redesign at Entrata | ✅ Strong |
| Kubernetes | K8s present (Entrata production) | ✅ Present |
| Full Agile SDLC | 120+ Agile sprints at Entrata; JIRA/Confluence implied | ✅ Strong |
| Git proficiency | Git; 300+ code reviews; GitHub Actions CI/CD | ✅ Strong |
| AWS | AWS S3/EC2/RDS/Glue present | ✅ Present (preferred) |
| **GoLang** | Zero (Java covers "at least one" requirement) | ⚠️ Zero GoLang; Java is the cover |
| **Voice agent / LLM + telephony** | No Twilio/VAPI/telephony API experience; voice AI is one of three agent types in the JD | ⚠️ Gap on voice specifically |
| Supply chain domain | Zero supply chain knowledge; role is AI engineering first, domain second | ⚠️ No domain match; manageable |
| H-1B sponsorship | FourKites is a Series E company (~500-800 employees) -- H-1B infrastructure likely; confirm at screen | ✅ Likely safe |

---

## C) Level and Strategy

**LeaseI is the exact same archetype as FourKites' support automation agent.** The JD describes "a support automation agent handling 60-70% of customer tickets." LeaseI is an 8-agent LangGraph support investigation platform that classifies tickets, retrieves business rules and historical incidents, produces evidence-backed root-cause hypotheses, and escalates to humans when confidence is too low. The architecture is identical to what FourKites is building. This is the strongest single proof point in the pipeline for this role.

**"Senior AI Engineer" at FourKites ≠ Senior SWE at Amazon/Stripe.** The hard block applies to "formal-leveling companies" like AppFolio, Amazon, Juniper Square, Stripe, Anthropic, Google. FourKites is a supply chain SaaS company with ~500-800 employees. The interview for this role centers on: "Can you build LangGraph agents? Can you write Python? Can you ship backend features?" -- not algorithmic hard or distributed systems design at hyperscale. The rejection pattern (confirmed: 2026-08-17) is specifically about formal tech IC bars. This is different. Mild concern noted, not a hard block.

**Java recency is the real concern.** Java appears in the CV (Entrata India, 2017-2018). That's 8 years ago. If interviewers test Java proficiency directly, she'll struggle. Mitigation: the role says "Java or GoLang -- proficiency in at least one" and Python + LangGraph is the primary work. If asked about Java in screening: acknowledge it's early-career experience and pivot to Python as the primary language where she has 9 years of depth.

**Voice agent gap is manageable.** The JD lists three agent types: support automation, voice (calls carriers), and onboarding. Her gap is only on the voice/telephony piece. Telephony AI (VAPI/Twilio + LLM) is different from raw audio/speech processing (NRG's hard gap). It's LLM orchestration + a telephony API -- conceptually within her reach. This is a feature gap, not a domain zero.

**Supply chain domain is a non-factor.** The JD focuses on engineering, not domain knowledge. The role's value prop is the AI/backend engineering skills applied to supply chain data -- same as how her Entrata work (property management) didn't require prior real estate background.

**$140K-$180K with stock options + remote-friendly.** One of the strongest comp packages in the pipeline for a role that genuinely fits.

---

## D) Comp and Demand

| Source | Range | Notes |
|--------|-------|-------|
| Disclosed | $140,000 -- $180,000 base + bonus + stock options | Strong; stock options are Series E (IPO-adjacent exit potential) |
| H-1B | ~500-800 employee company -- likely sponsors; confirm at screen | ✅ Probable; not guaranteed until confirmed |
| Location | Remote-friendly (Chicago in-office benefit mentioned, not required) | ✅ No penalty |

---

## E) CV Plan

Frame: "I've built the exact agents your team is working on -- LangGraph support investigation, multi-agent orchestration, HITL escalation -- at production quality with full eval harness."

- Summary: Lead with LeaseI (8-agent LangGraph support investigation → mirrors their support automation agent directly) + AgentProbe (eval framework for agent quality)
- Skills: Python, LangGraph, FastAPI, PostgreSQL/MySQL, React/TypeScript, Docker/K8s, AWS, CI/CD, Java (listed, early career)
- Entrata: production backend ownership (microservices, RabbitMQ, 120+ sprints, 300+ code reviews, 80% automation)
- Magizhs: LangGraph stateful graph production delivery
- Projects: LeaseI + AgentProbe front-loaded; AI on FHIR (React + REST)
- Do NOT lead with audio/voice experience (don't have it) -- lead with support automation agent match

---

## G) Posting Legitimacy

**High Confidence.** FourKites is a verifiable, well-funded Series E supply chain AI company (1,600+ enterprise customers including Walmart, Cardinal Health). Comp range disclosed, specific role scope described, benefits detailed. No ghost signals.

---

## Recommendation: Apply (4.2/5 -- clears 4.0 agentic AI threshold)

**The support investigation agent match is direct and rare.** Most candidates applying for this role will have LLM experience but not a production 8-agent LangGraph system with HITL, eval framework, and 1,240-case test suite. That combination is the exact profile FourKites is describing.

Arguments for:
- LeaseI support investigation agent = mirrors their support automation agent exactly
- AgentProbe = built-in evaluation framework for agent quality
- Python/LangGraph/PostgreSQL/Docker/K8s/React: full stack match
- $140K-$180K + stock options: strong comp
- FourKites "Senior" ≠ Amazon/Stripe formal bar
- Remote-friendly, H-1B likely safe

Arguments against:
- Java is dated (2017-2018, 8yr gap)
- No GoLang (covered by Java but both are weak)
- No voice/telephony agent experience
- No supply chain domain
- "Senior" at 500-800 employee company (mild concern)

---

## Machine Summary

```yaml
report: 399
company: FourKites
role: Senior AI Engineer
date: 2026-09-21
score: 4.2
archetype: Agentic AI / Backend SWE (Supply Chain SaaS)
legitimacy: High Confidence
url: null
status: Evaluated
recommendation: Apply
threshold: 4.0 (agentic AI) -- clears
boosts_applied:
  - LangGraph explicitly required + direct match (LeaseI 8-agent + AgentProbe)
  - LeaseI support investigation = mirrors FourKites support automation agent directly
  - Python/PostgreSQL/Docker/K8s/React: full stack match
  - AgentProbe eval framework = their agent quality evaluation need
penalties:
  - Senior title at ~500-800 employee company (-0.2, mild; below hard-block tier)
  - Java dated 2017-2018 (-0.1)
  - No voice/telephony agent experience (-0.1)
  - No supply chain domain (-0.1, minor -- role is AI engineering first)
gaps:
  - Java recency (8yr ago; covered by Python as primary)
  - GoLang (zero; Java covers "at least one" requirement)
  - Voice/telephony agent (one of three agent types; LLM+telephony, not raw speech)
  - Supply chain domain
h1b: Series E company (~500-800 employees) -- likely sponsors; confirm at screen
comp_range: $140,000--$180,000 + bonus + stock options
location: Remote-friendly (Chicago in-office commuter benefit optional)
```
