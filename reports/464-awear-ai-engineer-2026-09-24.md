# Evaluation: Awear — AI Engineer (First Hire)

**Date:** 2026-09-24
**URL:** (pasted JD)
**Archetype:** AI Platform / LLMOps + Agentic Runtime Engineer
**Score:** 4.8/5
**Legitimacy:** High Confidence
**PDF:** ✅ output/cv-venkata-lakshmi-parimala-pasupuleti-awear-ai-engineer-2026-09-24.pdf

---

## A) Role Summary

| Dimension | Details |
|-----------|---------|
| **Archetype** | First AI Engineer — agentic runtime, orchestration, RAG/memory, LLM routing, eval/observability, on-device inference |
| **Domain** | Awear — stealth-mode startup; "operating system for next-generation computing" where AI agents replace apps on a wearable platform; founders from consumer AI, XR, and wearable hardware; backed by silicon/manufacturing partnerships |
| **Function** | Own the entire agent layer: orchestration runtime, multi-provider LLM routing, RAG + memory retrieval, tool/skill integrations, eval + observability, on-device inference optimization, prompt architecture |
| **Seniority** | 4+ years SWE, 2+ years LLM production; first AI engineer = de-facto AI lead |
| **Work model** | **Fully remote** — occasional in-person at Silicon Valley or Paris for key milestones |
| **Comp** | Competitive (undisclosed) + **meaningful early-stage equity** + full medical/dental/vision |
| **Sponsorship** | Not stated — stealth startup; uncertain; verify early |
| **TL;DR** | Exceptional alignment across every required axis. "The backend engineers build the infrastructure. The mobile engineers build the user facing surfaces. You build what runs between them — the agents themselves." — that is precisely what AgentProbe and LeaseI are. AgentProbe = homegrown agent evaluation and observability framework (exact JD bullet). LeaseI = 8-agent LangGraph with multi-step reasoning, RAG, memory retrieval, tool orchestration, HITL, and a pass@k eval harness. LLM routing across OpenAI/Anthropic/Groq/Ollama with cost/latency controls. Fully remote. Early-stage equity. First-hire leverage. Score 4.8/5 — **strong apply.** |

---

## B) Match with CV

| JD Requirement | CV Evidence | Match |
|---|---|---|
| 4+ years SWE, 2+ years LLM production | 8+ yrs SWE; LLM production: AgentProbe + LeaseI + Magizhs (2024–present) | ✅ |
| **Deep LLM integration — production pipelines** | **LeaseI: full LangGraph agentic pipeline, OpenAI API, LangSmith; Magizhs: LangGraph + RAG + guardrails; AgentProbe: multi-provider routing** | ✅ **Direct proof** |
| **RAG architectures — vector DBs, embedding pipelines, retrieval optimization** | **LeaseI: ChromaDB, TF-IDF + semantic reranking, hybrid search, section-aware chunking, citation grounding; AgentProbe: ChromaDB + Qdrant** | ✅ **Direct proof** |
| **Agent frameworks — LangChain, LangGraph, point of view** | **LangGraph (primary — 8-agent LeaseI); LangChain; LangSmith; clear point of view from production use** | ✅ **Primary stack** |
| **Python production code** | **Python 8+ yrs; FastAPI backends; production systems at scale** | ✅ |
| **LLM evaluation at scale — evals, regressions, quality** | **AgentProbe: homegrown eval harness, 5-metric engine, LLM-as-judge, CI regression harness, golden datasets, pass@k, precision/recall/F1 across 1,240+ test cases** | ✅ **Exact match** |
| **LLM routing — capability, latency, cost, privacy** | **AgentProbe: model routing across OpenAI/Anthropic/Groq/Ollama with cost controls and latency metric** | ✅ **Direct proof** |
| AI-assisted dev tools (Cursor, Claude, Copilot) | Claude Code + Cursor daily | ✅ |
| Multi-agent system design | LeaseI 8-agent LangGraph (Triage → Retrieval → Config → Historical → Reasoning → Validation → Escalation); Magizhs agentic graph | ✅ |
| Memory retrieval systems | LeaseI: durable state management, ChromaDB knowledge store, contextual retrieval; AgentProbe: memory module | ✅ |
| Tool and skill integrations | LangGraph tool calling; Function calling; external API integrations in LeaseI | ✅ |
| Privacy-preserving AI | PHI compliance, HIPAA, Libsodium-encrypted pipelines, SOC 2, zero security incidents at Entrata | ✅ |
| Fully remote | Virginia-based; remote ✅ | ✅ |
| **On-device inference (Core ML, ONNX, TFLite)** | **Not in stack — strong plus, not required** | ⚠️ Gap |
| Wearable / mobile AI platform | Not in stack — product is under NDA; first hire builds this | ⚠️ Novel domain |
| Streaming / always-on inference | Ambient AI in cv.md; async distributed systems at Entrata; real-time pipelines ✅ Adjacent | ⚠️ |
| LlamaIndex / AutoGen familiarity | LlamaIndex-adjacent (built the same stack it powers); AutoGen not in stack | ⚠️ Adjacent |
| Comp: competitive + early equity | Undisclosed; early-stage equity is meaningful at stealth pre-launch | ✅ |
| Sponsorship | Not stated — stealth startup; uncertain; verify early | ⚠️ |

---

## D) Comp and Demand

| Metric | Data |
|--------|------|
| Comp | Undisclosed — "competitive depending on experience" + meaningful early-stage equity |
| Score | **4.5/5** — equity at pre-launch stealth startup with silicon partnerships could be significant; base undisclosed |

---

## G) Posting Legitimacy

**Assessment: High Confidence** — Company name "Awear" is disclosed in JD. Founding team claims ("founders of some of the most recognizable hardware and software platforms") + silicon/manufacturing backing + remote + Paris/SV milestones are internally consistent for a stealth wearable AI startup. The technical specificity of the JD (Core ML, ONNX, LangGraph, pass@k framing) confirms genuine technical founders. NDA on product details is standard for stealth mode.

---

## Machine Summary
```yaml
company: Awear
role: AI Engineer (First Hire)
score: 4.8
archetype: AI Platform / LLMOps + Agentic Runtime Engineer
level: 4+ yr SWE, 2+ yr LLM; de-facto AI lead as first hire
comp_range: "Competitive (undisclosed) + meaningful early-stage equity"
location: Fully remote — occasional SV/Paris for milestones; no relocation
sponsorship: Not stated — stealth startup; uncertain; verify early
apply: YES — strong apply; 4.8/5
boost_applied: Startup boost (stealth, early-stage equity); AgentProbe eval boost (+0.3)
top_proof_points:
  - AgentProbe = homegrown eval harness with LLM-as-judge + CI regression + golden datasets = exact "agent evaluation and observability" bullet in JD
  - LeaseI 8-agent LangGraph = multi-agent orchestration + RAG + memory retrieval + tool integrations = exact agent layer JD describes
  - LLM routing across OpenAI/Anthropic/Groq/Ollama with cost/latency controls = exact "multi-provider LLM routing" requirement
  - Privacy-preserving AI: PHI/HIPAA/Libsodium + zero security incidents
  - Fully remote — no relocation friction
key_gap:
  - On-device inference (Core ML/ONNX/TFLite): not in stack (strong plus, not required)
  - Wearable/mobile AI platform: novel domain (product under NDA; first hire builds this)
  - Sponsorship unconfirmed (stealth startup — verify early)
  - LlamaIndex direct experience: adjacent (built same infrastructure it powers); AutoGen not in stack
```
