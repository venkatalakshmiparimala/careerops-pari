# Evaluation: Stord — Senior Software Engineer (AI Platform)

**Date:** 2026-09-23
**URL:** (pasted JD)
**Archetype:** Agentic / Automation + AI Platform / LLMOps (both primary)
**Score:** 3.8/5
**Legitimacy:** High Confidence
**PDF:** ✅ output/cv-venkata-lakshmi-parimala-pasupuleti-stord-2026-09-23.pdf

---

## A) Role Summary

| Dimension | Details |
|-----------|---------|
| **Archetype** | Agentic / Automation + AI Platform / LLMOps (both primary) |
| **Domain** | Logistics / supply chain SaaS — fulfillment, OMS, WMS, post-purchase platform |
| **Function** | Build AI platform: agent tool systems, prompt pipelines, edge-deployed services, LLM-powered features across Stord's product suite |
| **Seniority** | Senior Software Engineer |
| **Work model** | HQ Atlanta — not explicitly stated as remote; flag for confirmation |
| **Comp** | Not disclosed |
| **Sponsorship** | Not stated — VC-backed Series C-stage company |
| **TL;DR** | Agentic AI side is a strong match (LeaseI, AgentProbe, MCP, Anthropic Claude). Hard gap: **TypeScript is the primary language (2+ years production required)** — Parimala is Python-primary with TypeScript as secondary. Cloudflare Workers / Durable Objects / Hono / D1 are all unfamiliar. No logistics domain experience. Score 3.8/5 — **below 4.5 threshold for non-PropTech roles. SKIP.** |

---

## B) Match with CV

| JD Requirement | CV Evidence | Match |
|---|---|---|
| **TypeScript (2+ years production — PRIMARY language)** | TypeScript in cv.md skills — but Python-primary; TypeScript used as secondary in full-stack work | ⚠️ **Gap — production TypeScript depth unproven** |
| **Cloudflare Workers + Durable Objects + Hono** | Not in cv.md — no edge computing experience | ✗ Not in stack |
| D1 / Drizzle ORM | Not in cv.md | ✗ Not in stack |
| Elixir / Phoenix (downstream integration) | Not in cv.md | ✗ Not in stack |
| LLM application development — tool calling, context management, multi-step workflows | LeaseI: 8-agent LangGraph, tool-calling agents, durable state, HITL; AgentProbe: model routing, eval engine | ✅ Strong |
| Anthropic Claude + AI SDK | Anthropic API in cv.md; AgentProbe routes across OpenAI/Anthropic/Groq/Ollama | ✅ Direct match |
| MCP (Model Context Protocol) | MCP in cv.md skills | ✅ Nice-to-have met |
| Prompt engineering, eval frameworks, observability for LLM systems | AgentProbe: 5-metric eval engine, LLM-as-judge, trace-level observability, CI regression harness | ✅ Direct match |
| Agent orchestration, skill registries, HITL patterns | LeaseI: LangGraph StateGraph, conditional routing, HITL escalation | ✅ |
| OpenTelemetry / Datadog observability | OpenTelemetry, Prometheus, Grafana in cv.md | ✅ |
| Multi-tenant SaaS | Entrata 7yr multi-tenant PostgreSQL | ✅ |
| Event-driven architecture | RabbitMQ 7yr with retry + idempotency | ✅ |
| PostgreSQL / SQL fundamentals | 7yr multi-tenant PostgreSQL, 200+ query optimizations | ✅ |
| Serverless / edge deployment | Serverless Architecture in cv.md; no Cloudflare-specific | ⚠️ Adjacent |
| **Logistics / supply chain / e-commerce domain** | No logistics or e-commerce experience | ✗ Domain gap |
| Remote policy | HQ Atlanta — not stated explicitly | ⚠️ Unclear |
| Sponsorship | Not stated — VC-backed established company | Likely positive |

---

## C) Level and Strategy

| Dimension | Finding |
|-----------|---------|
| Hard gap | TypeScript 2+ years production is the #1 technical requirement. Parimala is Python-primary. Even if she can write TypeScript, the role expects someone who *thinks* in TypeScript — the entire AI platform is TypeScript-native. |
| Stack mismatch | Cloudflare Workers, Durable Objects, Hono, D1 are all Cloudflare-specific and not in her background. This is not a ramp-up gap — it's the core operating environment of the role. |
| AI match | The agentic AI side is genuinely strong: LeaseI + AgentProbe + MCP + Anthropic Claude cover every AI/LLM requirement. If the stack were Python/FastAPI this would score 4.5+. |
| Domain | Logistics is not PropTech. No domain boost applies. No natural "I've built these systems" story. |

---

## D) Comp and Demand

| Metric | Data |
|--------|------|
| JD range | Not disclosed |
| Estimated | $130K–$175K (Kleiner/Founders Fund-backed, AI platform role, Atlanta HQ) |
| Score | **3.0/5** — not disclosed; VC backing suggests competitive but unknown |

---

## E) Customization Plan

Not applicable — below apply threshold. If user wants to apply anyway, reframe around:
- TypeScript: position as "active transition" — she has TypeScript in skills + has shipped JS/TS modules at Entrata
- Cloudflare: frame distributed systems + serverless architecture background as ramp signal
- AI/agentic: lead hard — this is the strongest part of the match

---

## F) Interview Plan

Not applicable — below apply threshold.

---

## G) Posting Legitimacy

| Signal | Finding | Weight |
|--------|---------|--------|
| Company | Stord — backed by Kleiner Perkins, Franklin Templeton, Founders Fund, Strike Capital, Baillie Gifford, Salesforce Ventures. $10B+ commerce managed annually. Real established company. | Positive |
| Tech specificity | TypeScript, Hono, Cloudflare Workers, Durable Objects, D1, Drizzle, Anthropic Claude, AI SDK, MCP — specific and real | Positive |
| Comp | Not disclosed | Neutral |
| Remote policy | Not explicitly stated — HQ Atlanta; verify before applying | Unknown |
| Sponsorship | Not stated — VC-backed mid-stage company; likely sponsors; verify | Likely positive |

**Assessment: High Confidence** — Real product, real investors, real stack.

---

## Verdict

**3.8/5 — SKIP.**

The AI/agentic match is genuinely strong — LeaseI, AgentProbe, MCP, Anthropic Claude, tool calling, HITL, observability all line up. But:

1. **TypeScript is the primary required language (2+ years production)** — Parimala is Python-primary. This is the core job.
2. **Cloudflare-specific stack** (Workers, Durable Objects, Hono, D1) is entirely unfamiliar — not a ramp-up gap, it's the daily environment.
3. **No logistics/supply chain domain experience** — no PropTech-style "I've already built this" story.

Below 4.5 threshold for non-PropTech roles. Below 4.0 threshold entirely. Not recommended.

**If you want to apply anyway:** the AI side is strong enough to justify a conversation. Lead hard with LeaseI + AgentProbe + MCP + Anthropic Claude. Be transparent about the TypeScript ramp. It's a stretch but not unreasonable if they're flexible on the stack.

---

## Keywords extracted

TypeScript, Cloudflare Workers, Durable Objects, Hono, D1, Drizzle, Anthropic Claude, AI SDK, MCP, agentic AI, tool calling, context management, multi-step workflows, HITL, prompt engineering, LLM evaluation, observability, OpenTelemetry, serverless, edge computing, multi-tenant SaaS, event-driven, logistics, supply chain, OMS, WMS, fulfillment

## Machine Summary
```yaml
company: Stord
role: Senior Software Engineer (AI Platform)
score: 3.8
archetype: Agentic/Automation + AI Platform/LLMOps (both primary)
level: Senior
comp_range: "Not disclosed (estimated $130K-$175K)"
location: Atlanta HQ — remote policy unconfirmed
sponsorship: Not stated — VC-backed, likely; verify
apply: SKIP — below 4.5 threshold for non-PropTech; below 4.0 hard floor
top_proof_points:
  - LeaseI (8-agent LangGraph + HITL + tool calling + durable state)
  - AgentProbe (LLM eval + observability + Anthropic routing)
  - MCP in cv.md skills
  - OpenTelemetry in cv.md
key_gap:
  - TypeScript primary (2+ yr production required) — Python-primary candidate
  - Cloudflare Workers / Durable Objects / Hono / D1 — not in stack
  - No logistics/e-commerce domain experience
  - Remote policy unconfirmed
```
