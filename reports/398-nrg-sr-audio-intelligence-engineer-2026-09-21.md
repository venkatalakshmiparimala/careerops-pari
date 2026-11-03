# Evaluation: NRG Energy -- Sr Audio Intelligence Engineer

**Date:** 2026-09-21
**URL:** (pasted directly, no URL provided)
**Archetype:** Audio / Speech AI Engineer (Smart Home)
**Score:** 2.5/5
**Legitimacy:** High Confidence
**PDF:** N/A (below 4.0 threshold -- SKIP)
**Location:** Seattle, WA -- Hybrid (Mon–Thu in office, Fri WFH)
**Comp:** $150,000 -- $185,000 + bonus + incentives

---

## A) Role Summary

| Dimension | Detail |
|-----------|--------|
| Archetype | Audio / Speech AI Engineer -- STT/TTS, wake word, streaming audio, real-time inference, smart home voice experiences |
| Domain | NRG smart home division -- building conversational + audio AI for smart home panels, cameras, mobile, agentic future experiences |
| Function | Design + build conversational and audio AI (STT/TTS/LLMs/multimodal); optimize latency/privacy/UX for real-time voice; build eval frameworks for conversational quality + safety; integrate with smart home context and agentic tool use |
| Seniority | "Sr Audio Intelligence Engineer" -- Senior title at NRG (~10K employees); large company, some leveling concern |
| Location | Seattle WA -- hybrid Mon–Thu in office (4 days/wk); starts remote then transitions |
| Company | NRG Energy -- large US energy + smart home company (~10K employees); H-1B infrastructure exists |
| TL;DR | The LLM/evaluation/agentic stack matches. Everything audio/speech does not: STT, TTS, wake word, streaming audio, ASR/NLU frameworks, real-time inference, smart home IoT/edge — all ZERO. "Experience with speech-to-text, text-to-speech, audio understanding, or conversational AI systems" is a Required qualification (not preferred), and it's completely absent from her background. Hard SKIP at 2.5. |

---

## B) Match with CV

| JD Requirement | CV Match | Strength |
|----------------|----------|----------|
| Master's + 2+ years OR Bachelor's + 5+ years | M.S. Data Analytics Engineering (GPA 3.87) + 9yr | ✅ Exceeds |
| Strong Python | Python 9yr primary | ✅ Strong |
| LLM integration into production applications | LeaseI (8-agent LangGraph, FastAPI); AgentProbe (multi-provider routing) | ✅ Strong |
| Prompt engineering, evaluation frameworks | AgentProbe: 5-metric eval engine, CI-integrated regression gate, LLM-as-judge | ✅ Strong |
| Latency optimization | AgentProbe latency metric; FastAPI async endpoints | ✅ Present |
| Git, CI/CD, production monitoring | GitHub Actions; 300+ code reviews; Entrata production ops | ✅ Present |
| Docker, K8s, AWS | All present (Entrata production) | ✅ Present (preferred) |
| Agentic tool use, memory, personalization | LangGraph stateful agents; ChromaDB vector memory; HITL escalation | ✅ Present |
| **STT / TTS / audio understanding (required)** | **Zero audio/speech experience -- not in stack** | ❌ Required gap |
| **Conversational AI systems (required)** | Text-based agents (LangGraph) -- NOT voice/audio conversational AI | ❌ Domain mismatch |
| **Wake word / streaming audio / real-time inference (preferred)** | **Zero -- not in stack** | ❌ Absent |
| **ASR / NLU frameworks (preferred)** | **Zero -- not in stack** | ❌ Absent |
| **Smart home / IoT / edge devices / embedded Linux (preferred)** | **Zero -- not in stack** | ❌ Absent |
| **Consumer-facing voice or assistant products (preferred)** | Zero -- never shipped voice/audio consumer products | ❌ Absent |
| Privacy-aware systems | HIPAA-compliant AI on FHIR; PHI compliance on AWS migration | ⚠️ Adjacent (compliance, not audio-specific privacy) |
| H-1B sponsorship | NRG 10K+ employees -- H-1B infrastructure exists | ✅ Likely safe |

---

## C) Why This Doesn't Clear 4.0

**The audio/speech domain is completely absent.** "Experience with speech-to-text, text-to-speech, audio understanding, or conversational AI systems" is a Required qualification -- not preferred. She has never worked with STT/TTS frameworks (Whisper, Azure Speech, Google Cloud Speech, Amazon Transcribe), wake word systems, streaming audio pipelines, ASR/NLU frameworks (Rasa, Wit.ai, Dialogflow), or real-time audio inference. This isn't a depth gap -- it's a complete zero.

**Conversational AI here means voice, not text agents.** Her LangGraph/LLM agent experience is genuinely strong, but this role's "conversational AI" context is voice interfaces for smart home devices (think Alexa/Google Home architecture). Text-based document agents are a different paradigm from real-time streaming speech with latency constraints, wake word detection, and audio signal processing.

**Smart home / IoT / edge is a secondary domain zero.** The preferred qualifications include edge AI, embedded devices, IoT, Linux-based systems, hybrid edge/cloud. None of this appears in her background.

**What's genuinely strong and wasted here.** Python, LLM integration, evaluation frameworks (AgentProbe is a direct proof point for "build evaluation frameworks for conversational quality"), agentic tool use, CI/CD, Docker/K8s. These would score this 4.0+ if the role were "AI Application Engineer" without the audio specialization. The eval framework piece is the strongest overlap -- but the job is 70% audio/speech domain and 30% LLM/eval, not the reverse.

**Senior title at 10K-employee company.** Mild concern; NRG is energy-first, not a pure tech IC-ladder company, so the formal leveling concern is lower than at Stripe/Amazon. But still a note.

**Comp is the highest in this session at $150K–$185K.** The mismatch is unfortunate. This is a skip regardless of compensation.

---

## D) Comp and Demand

| Source | Range | Notes |
|--------|-------|-------|
| Disclosed | $150,000 -- $185,000 base + annual bonus + STI/LTI | Highest comp in session (#394–#398) |
| H-1B | NRG ~10K employees -- H-1B infrastructure exists | ✅ Likely safe |
| Location | Seattle WA -- 4 days/wk in office | Heavy hybrid schedule; starts remote |

---

## G) Posting Legitimacy

**High Confidence.** NRG Energy is a verifiable public energy company. Specific location (Seattle WA), comp range disclosed, standard EEO language, drug testing policy disclosed. No ghost signals.

---

## Recommendation: SKIP (2.5/5 -- far below threshold)

**Required qualification missing entirely: STT/TTS/audio understanding.** No audio/speech domain experience in her background -- not a gap to bridge, a complete absence. High comp doesn't change the call.

---

## Machine Summary

```yaml
report: 398
company: NRG Energy
role: Sr Audio Intelligence Engineer
date: 2026-09-21
score: 2.5
archetype: Audio / Speech AI Engineer (Smart Home)
legitimacy: High Confidence
url: null
status: SKIP
gaps:
  - STT / TTS / audio understanding (required -- zero in stack)
  - Conversational AI (required -- text agents present, voice/audio absent)
  - Wake word / streaming audio / real-time inference (preferred -- zero)
  - ASR / NLU frameworks (preferred -- zero)
  - Smart home / IoT / edge / embedded Linux (preferred -- zero)
strengths:
  - Python/LLM integration: strong
  - AgentProbe eval framework: direct proof point for conversational quality eval
  - Agentic tool use / HITL / memory: present
  - Docker/K8s/AWS: present (preferred)
note: Highest comp in session ($150K-$185K) but wrong domain entirely. Audio/speech = hard zero.
comp_range: $150,000--$185,000 + bonus + incentives
location: Seattle WA hybrid (Mon-Thu in office, Fri WFH; starts remote)
```
