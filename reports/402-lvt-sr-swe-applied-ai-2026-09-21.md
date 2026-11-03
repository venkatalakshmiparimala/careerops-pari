# Evaluation: LVT -- Senior Software Engineer, Applied AI

**Date:** 2026-09-21
**URL:** (pasted directly, no URL provided)
**Archetype:** Applied AI / Agentic Systems Engineer (Physical Security / IoT)
**Score:** 4.1/5
**Legitimacy:** High Confidence
**PDF:** output/cv-venkata-lakshmi-parimala-pasupuleti-lvt-2026-09-21.pdf
**Location:** Unknown (LVT HQ: American Fork, UT -- remote policy unconfirmed)
**Comp:** $185,400 -- $232,050 + bonus + equity

---

## A) Role Summary

| Dimension | Detail |
|-----------|--------|
| Archetype | Applied AI / Senior IC -- owns GenAI-powered security deterrence product end-to-end; detection → LLM orchestration → voice response; evaluation harness for real-world-actuating system |
| Domain | LVT -- intelligent site security (AI-driven physical security cameras, solar-powered units, detection models); product acts on the physical world |
| Function | Build detection-to-response harness (LLM orchestration + prompting + voice/TTS); own evaluation + regression suite; precision/safety bar; application APIs; cross-team with ML scientists; build-vs-buy decisions |
| Seniority | Senior IC at LVT (growth startup, ~200-500 employees, Inc. 5000 #10 Rocky Mountain 2025) -- NOT formal-leveling tech company; Senior concern does not apply |
| Location | Unknown -- LVT HQ in Utah; remote policy not stated; confirm at screen |
| Company | LVT -- AI-driven physical security; FT Fastest Growing 2025; Series-stage growth company; H-1B unconfirmed |
| TL;DR | AgentProbe is the most direct proof point in the entire pipeline for this role -- the JD describes "a product-level evaluation and regression suite that catches false or mistimed talkdowns before they reach the field" which is exactly what AgentProbe does. LangGraph + MCP + vector databases are all in preferred and all present. Voice/TTS is a gap (preferred; API-integration level, not audio engineering). H-1B unconfirmed at growth startup. Score 4.1 -- Apply. |

---

## B) Match with CV

| JD Requirement | CV Match | Strength |
|----------------|----------|----------|
| 6+ years backend/full-stack production SWE | 9yr (Entrata 7.5yr + GMU + Magizhs) | ✅ Exceeds |
| Python + TypeScript/Node | Python 9yr primary; TypeScript (AgentProbe); Node.js familiarity | ✅ Strong |
| **LLM orchestration, prompting, retrieval, tool-calling** | LeaseI (8-agent LangGraph, RAG, tool calls, HITL); AgentProbe (multi-provider routing) | ✅ Strong |
| **Evaluation harness for non-deterministic systems** | **AgentProbe: 5-metric eval engine, CI-integrated regression gate, LLM-as-judge, multi-trial pass@k -- built exactly for this purpose** | ✅ Exceptional -- direct proof point |
| Real-world consequences for wrong output | 7yr Entrata: compliance-critical income eligibility (wrong import = wrong housing decision for thousands of residents); HIPAA/PHI pipelines | ✅ Strong -- exact transferable discipline |
| End-to-end product ownership | LeaseI (0→1, design through production); AgentProbe (0→1 open-source toolkit) | ✅ Present |
| Build-vs-buy judgment | AgentProbe: self-hosted vs managed LLM decisions explicit; Magizhs: build vs framework tradeoffs | ✅ Present |
| APIs + production backend | FastAPI (15-endpoint REST); Entrata production backend; RabbitMQ | ✅ Strong |
| Cross-functional collaboration with ML scientists | Cross-team at Entrata; Magizhs external delivery | ✅ Present |
| **LangGraph (preferred)** | LeaseI 8-agent LangGraph StateGraph; AgentProbe; Magizhs | ✅ Strong |
| **MCP frameworks (preferred)** | Claude Code MCP daily; MCP architecture awareness | ✅ Present |
| **Vector databases (preferred)** | ChromaDB (AgentProbe); TF-IDF retrieval (LeaseI) | ✅ Present |
| **Evaluation/regression frameworks for non-deterministic systems (preferred)** | AgentProbe: CI gate, regression suite, pass@k harness | ✅ Exceptional |
| **Voice / TTS generation (preferred)** | **Zero -- no TTS/voice API production experience** | ❌ Preferred gap |
| **Computer vision / detection (preferred)** | Zero -- no CV/detection background | ❌ Absent (preferred) |
| **IoT / edge-to-cloud (preferred)** | Zero -- not in stack | ❌ Absent (preferred) |
| H-1B sponsorship | LVT ~200-500 employees -- uncertain; confirm at screen | ⚠️ Unconfirmed |

---

## C) Level and Strategy

**AgentProbe is the most direct proof point in the entire pipeline for this role.** The JD asks for "a product-level evaluation and regression suite that catches false or mistimed talkdowns before they reach the field." That is exactly what AgentProbe is -- a CI-integrated regression gate with LLM-as-judge scoring that blocks quality degradation on every commit. Built on a real production system (LeaseI), evaluated across 1,240 test cases. No other role in this session has a proof point this direct.

**The real-world consequences discipline is genuinely transferable.** The JD explicitly calls out "systems where a wrong output has real consequences -- real-time, event-driven, or actuating systems." Her citation: "a wrong import means thousands of residents get the wrong eligibility decision and trigger regulatory corrections." LeaseI's core rule: "LLM reasons, deterministic logic makes every final regulated call." This is the same discipline LVT needs -- a system that acts in the physical world must get it right the same way a compliance system must get it right.

**Voice/TTS is a gap but at the API-integration level, not audio engineering.** This is not NRG (#398) where the core domain was raw audio signal processing, wake word, and ASR. LVT's voice component is: detection event → LLM orchestration → TTS API call (ElevenLabs, OpenAI TTS, Azure TTS) → speaker output. The orchestration, evaluation, and guardrails are entirely her strength. The TTS piece is an API integration layer. She has the harder parts; TTS is learnable quickly on the job.

**Senior IC at a growth startup -- no formal leveling concern.** LVT is Inc. 5000 growth-stage company, not Amazon/Stripe/AppFolio. The interview bar is: "Can you own this AI system end-to-end, build the eval harness, and operate with precision in a safety-critical context?" That's a direct match.

**H-1B is the key unknown.** LVT is ~200-500 employees. Growth-stage tech companies at this size sometimes sponsor, sometimes don't. Must confirm before deep investment. The JD says "Must be authorized to work in the U.S." (standard language, compatible with F-1 STEM OPT) but doesn't mention sponsorship.

**Comp is the highest confirmed in the pipeline at $185K–$232K.** With equity from day one.

---

## D) Comp and Demand

| Source | Range | Notes |
|--------|-------|-------|
| Disclosed | $185,400 -- $232,050 base + bonus + equity | Highest confirmed comp in pipeline; equity from day one |
| H-1B | ~200-500 employee growth startup -- unconfirmed | ⚠️ Confirm before applying |
| Location | Unknown -- LVT HQ Utah; remote policy unconfirmed | ⚠️ Confirm at screen |

---

## E) CV Plan

Frame: "I've built the exact evaluation harness your JD describes, and I bring the precision discipline of systems where wrong outputs have regulated consequences."

- Summary: Lead with AgentProbe (CI regression gate, LLM-as-judge, 5-metric eval) + LeaseI (LLM orchestration + HITL + guardrails for regulated decisions) + Entrata compliance-critical systems
- Skills: Python, LangGraph, MCP, FastAPI, ChromaDB/vector databases, LLM evaluation, CI/CD, Docker/K8s, TypeScript
- Entrata: "wrong data has real consequences" framing -- compliance, zero violations, regulatory precision
- Magizhs: agentic delivery + build-vs-buy decisions
- Projects: AgentProbe (eval harness proof point) + LeaseI (orchestration + guardrails)
- Do NOT lead with voice/TTS -- don't have it; let them raise it

---

## G) Posting Legitimacy

**High Confidence.** LVT is a verifiable company (Inc. 5000, FT Fastest Growing 2025, EY CEO award 2025). Detailed role description with specific technical requirements. Comp range disclosed. No ghost signals.

---

## Recommendation: Apply (4.1/5 -- clears 4.0 agentic AI threshold)

**Strongest AgentProbe proof point in the pipeline. Exceptional comp. Real-world consequences discipline is directly transferable.**

Confirm H-1B and location/remote policy before submitting.

Arguments for:
- AgentProbe = eval regression suite they explicitly require (direct proof point)
- LangGraph + MCP + vector databases: all in preferred, all present
- "Wrong output has real consequences" = Entrata compliance-critical discipline
- Senior IC at growth startup (no formal leveling concern)
- $185K–$232K + equity: exceptional
- End-to-end ownership track record: LeaseI + AgentProbe

Arguments against:
- Voice/TTS: zero (preferred, but it IS a major feature of this specific product)
- Computer vision / detection: zero (preferred)
- H-1B: unconfirmed
- Location/remote: unknown

---

## Machine Summary

```yaml
report: 402
company: LVT
role: Senior Software Engineer -- Applied AI
date: 2026-09-21
score: 4.1
archetype: Applied AI / Agentic Systems Engineer (Physical Security / IoT)
legitimacy: High Confidence
url: null
status: Evaluated
recommendation: Apply
threshold: 4.0 (agentic AI growth startup) -- clears
boosts_applied:
  - AgentProbe = exact eval regression suite required by JD (direct proof point)
  - LangGraph + MCP + vector databases: all in preferred, all present
  - "Wrong output has real consequences" = compliance-critical discipline match
  - Growth startup Senior IC = no formal leveling concern
penalties:
  - Voice/TTS gap (preferred but major product feature) (-0.2)
  - CV/detection/IoT zero (preferred) (-0.1)
  - H-1B unconfirmed (-0.1)
  - Location unknown (-0.1, not penalized per profile -- noted only)
gaps:
  - Voice / TTS (preferred; API-integration level, not audio engineering)
  - Computer vision / video detection (preferred)
  - IoT / edge-to-cloud (preferred)
  - H-1B: unconfirmed at ~200-500 employee startup
h1b: UNCONFIRMED -- confirm before deep investment
comp_range: $185,400--$232,050 + bonus + equity from day one
location: Unknown (LVT HQ: American Fork, UT) -- remote policy unconfirmed
```
