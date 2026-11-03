# 294 — Deloitte — Forward Deployed Engineer, AWS AI&Data

**Date:** 2026-09-08
**Score:** 3.1/5 — Borderline (FDE = primary target archetype ✓✓; agentic platforms/HITL/GenAI production = direct match; AWS certifications required (3 of 6) — none held; Bedrock/AgentCore/Neptune/OpenSearch required — not in background; $155K–$307K disclosed; "limited immigration sponsorship may be available")
**URL:** Deloitte careers (via job posting)
**PDF:** ✅ `output/294-deloitte-fde-aws-ai-data-2026-09-08.pdf`
**Legitimacy:** High Confidence — Deloitte needs no introduction; one of the Big Four; salary range $155,600–$306,800 disclosed; FDE role is a real, active Deloitte practice; no ghost indicators

---

## Block A — CV Match

**The FDE archetype and agentic AI delivery pattern map directly — LeaseI and AgentProbe cover the core of what this role builds. AWS certifications (3 of 6 required) are the hardest gap; Bedrock/AgentCore/Neptune/OpenSearch are required product gaps with conceptual analogues in the background.**

| JD Requirement | CV Proof Point |
|---------------|----------------|
| "5+ years software engineering, data engineering, data science, or analytics engineering" | 9yr 8mo professional SWE (Jan 2017 → present) ✓✓ |
| "Bachelor's or equivalent in CS, Data Science, or Engineering" | B.Tech CS + M.S. Data Analytics Engineering, GMU (GPA 3.87) ✓✓ |
| "1+ years building and deploying GenAI/LLM solutions in client or production environments" | AgentProbe: multi-provider LLM platform (Anthropic/OpenAI/Ollama), production; LeaseI: 8-agent LangGraph production platform; Magizhs: customer-facing agentic AI deployed to external client ✓✓✓ |
| "Build AI-enabled solutions, agentic platforms, and workflows across enterprise AI platforms" | LeaseI: 8-agent LangGraph with HITL, guardrails, conditional routing; AgentProbe: multi-provider evaluation platform ✓✓ |
| "Human-in-the-loop controls" | LeaseI: HITL escalation when confidence below threshold; deterministic guardrails; safety boundary tested ✓✓✓ |
| "Prototype and deliver working AI solutions — speed and precision" | Magizhs: ambiguous requirements → production in weeks, solo; AgentProbe: concept to open-source production end-to-end ✓✓ |
| "Embed with clients — translate high-value GenAI use cases into solutions" | Magizhs: direct customer engagement, requirements scoping, architecture, delivery ✓✓ |
| "Lead working sessions with senior stakeholders" | 120+ Agile sprints (Entrata); Magizhs COO-level scoping; GMU faculty stakeholder delivery ✓ |
| "MLOps/LLMOps: evaluation frameworks, model monitoring, prompt management" (preferred) | AgentProbe: 5-metric eval engine, CI regression gate, multi-provider routing ✓✓ |
| "APIs, microservices, event-driven architectures" (preferred) | Entrata: RabbitMQ async (event-driven); FastAPI microservices; 15-endpoint AgentProbe API ✓✓ |
| "Security, privacy, compliance considerations" (preferred) | Entrata: PHI/HIPAA, Libsodium encryption, zero security incidents 7yr; AI on FHIR: HIPAA RBAC ✓✓ |
| "Testing, CI/CD, logging, versioning, documentation" | AgentProbe: CI-integrated regression gate (GitHub Actions); LeaseI: full test suite, versioning ✓✓ |
| "1+ years with AWS AI&Data: Amazon Bedrock, Bedrock AgentCore, Strands Agents SDK, Knowledge Bases, Guardrails" | AWS S3/EC2/RDS/Glue (production) ✓; Anthropic API directly (not through Bedrock) ✗; AgentCore/Strands Agents SDK ✗; Knowledge Bases ✗; Bedrock Guardrails ✗ — conceptual transfer from Anthropic API patterns is credible but not the same product |
| "1+ years with AWS Neptune and OpenSearch" | ChromaDB for vector search ✓/⚠️ (different product); Neptune (graph DB) ✗; OpenSearch ✗ |
| "At least 3 of 6 AWS certifications" | No AWS certifications held ✗✗ — listed under Required Qualifications |
| "50% travel on average" | User open to any US location ✓; travel-heavy FDE model ⚠️ |
| "Mentoring newer team members" | Entrata: 5+ engineers mentored; GMU: 600+ students ✓ |

**Hard Gaps:**
- **AWS certifications (3 of 6 required)** — AWS Certified Cloud Practitioner, Solutions Architect, AI Practitioner, Generative AI Developer, ML Engineer Associate, or Data Engineer Associate; none held; listed as Required not Preferred; ATS likely filters on certification keywords
- **AWS Bedrock / AgentCore / Strands Agents SDK** — the specific AWS AI product layer; uses Anthropic API directly (not through Bedrock); conceptual transfer is real (both are LLM API abstractions) but the product-specific interview questions will expose the gap
- **AWS Neptune** — graph database; no graph DB experience in background
- **AWS OpenSearch** — managed search/vector index; ChromaDB is the vector DB used; conceptual overlap but different product
- **50% travel** — consulting model; user is open to relocation but ongoing 50% travel is a lifestyle consideration

**ATS baseline:** ~13/20. Python ✓, AWS ✓, GenAI ✓, LLM ✓, agentic ✓, HITL ✓, LLMOps ✓, CI/CD ✓, client engagement ✓. Bedrock/AgentCore/Neptune/OpenSearch/certifications all absent.

---

## Block B — North Star Alignment

**FDE = the #1 primary target archetype.** "Forward Deployed Engineer" is literally the title. Deloitte's FDE model — embed with clients, rapidly prototype GenAI solutions, translate business problems into working software, deliver with speed and precision — is exactly the target profile.

LeaseI and AgentProbe cover the technical depth: agentic platforms (8-agent LangGraph), HITL controls, LLMOps evaluation (AgentProbe 5-metric engine), production AI deployment (Magizhs), and client-facing delivery. The "contribute reusable assets — code, prompt libraries, runbooks, reference implementations" requirement maps to AgentProbe (open-source, reusable) and LeaseI (documented, reference implementation).

The AWS-specific product requirement (Bedrock vs Anthropic API directly) is conceptually similar but will come up in interviews. The certification requirement is the harder blocker — Deloitte compliance culture takes required credentials seriously, and ATS systems at Big Four firms often filter on certification keywords.

"Limited immigration sponsorship may be available" — this is the most positive H-1B language in the session outside of confirmed sponsors. Deloitte is one of the largest H-1B sponsors in the US (Big Four firms dominate the H-1B filing list annually).

**Score: 3.5/5** (FDE = #1 archetype; strong agentic AI alignment; AWS cert gap; Bedrock/Neptune/OpenSearch product gaps)

---

## Block C — Compensation

**Disclosed: $155,600–$306,800.** One of the widest and highest ranges in the pipeline. Deloitte's FDE compensation reflects both the consulting premium and the AI premium layered on top. Discretionary annual incentive (bonus) on top of base. Big Four benefits (healthcare, 401K, PTO). The range is broad because it covers multiple experience bands — a 5yr candidate lands near the bottom, a 9yr candidate with deep AI delivery experience lands higher.

**Score: 5.0/5**

---

## Block D — Cultural Signals

- "Move with speed and precision, building working software" — delivery-first culture ✓
- "Measurable business impact from day one" — results-accountable ✓
- FDE pod model — small embedded team, high ownership ✓
- "50% travel on average" — consulting travel model; significant lifestyle commitment ⚠️
- Deloitte = large firm (100K+ US employees) but FDE practice operates more like a startup pod within the firm ✓
- "Contribute independently within FDE pod while mentoring newer members" — IC + light leadership ✓
- "Limited immigration sponsorship may be available" — positive; Deloitte files thousands of H-1B petitions annually ✓
- Hybrid/client-site model; Virginia/DC area client base likely (Deloitte's DC Government practice is large) — proximity advantage ✓

**Score: 4.0/5**

---

## Block E — Red Flags

1. **AWS certifications (3 of 6) required** — listed under Required Qualifications; ATS at Big Four firms filters on certification keywords; applying without any of the 6 certifications puts the application at high ATS-filter risk before a human sees it
2. **AWS Bedrock / AgentCore / Strands Agents SDK** — the specific AWS AI products the role requires; Anthropic API experience is the conceptual equivalent but a Deloitte technical screen will ask Bedrock-specific questions; the gap is real even if the patterns are similar
3. **AWS Neptune + OpenSearch** — graph database and managed search index; no direct experience; ChromaDB is a different product in a different category (Neptune is graph, not vector)
4. **50% travel** — ongoing consulting travel; not a hard blocker for user preferences but a real lifestyle commitment over time
5. **Big Four compliance culture** — Deloitte is a formal organization (certifications, engagement management, documentation standards, client relationship hierarchy); different from startup SaaS culture at Entrata

**Adjustment: −0.5** (certifications required/not held; Bedrock/Neptune/OpenSearch product gaps; travel; consulting culture)

---

## Block F — Global Score

| Factor | Signal |
|--------|--------|
| CV match | 3.0 — FDE delivery ✓✓; Python ✓✓; GenAI/LLM production ✓✓; agentic platforms ✓✓; HITL ✓✓; LLMOps ✓✓; AWS general ✓; Bedrock/AgentCore/Neptune/OpenSearch ✗; certifications (3 required) ✗✗ |
| North Star | 3.5 — FDE = #1 target archetype; strong agentic AI alignment; AWS product gaps; certification requirement; Deloitte H-1B sponsorship likely |
| Comp | 5.0 — $155K–$307K disclosed; discretionary bonus; Big Four benefits; exceptional ceiling |
| Culture | 4.0 — FDE delivery culture ✓; pod model ✓; H-1B likely ✓; 50% travel ⚠️; Big Four compliance ⚠️ |
| Red flags | −0.5 — certifications required (none held); Bedrock/AgentCore/Neptune/OpenSearch gaps; travel; consulting culture |

**Global: 3.1/5 — Borderline**

> This is the FDE role you've been targeting all session. Deloitte's FDE practice embeds engineers with enterprise clients to prototype and ship GenAI solutions — LeaseI and AgentProbe are built for exactly this. The problem is two-layered: (1) AWS certifications are listed as Required (3 of 6) and ATS at Big Four firms filters on these; applying without any cert is high-risk for ATS filtering before a human reads the application; (2) Bedrock/AgentCore/Neptune/OpenSearch are specific product requirements where Anthropic API + ChromaDB experience is conceptually similar but not the same thing. If you can get even the AWS Cloud Practitioner cert in the next 2 weeks (online exam, $100, ~1-2 weeks of prep), reapply immediately — it would change this application meaningfully. If you want to push now without the cert, lead very hard on Magizhs (customer-facing agentic AI deployment), LeaseI (8-agent HITL platform), and AgentProbe (LLMOps) as the proof points, and frame Anthropic API → Bedrock as a platform transfer you can close in days.

---

## Block G — Posting Legitimacy

**High Confidence.** Deloitte is one of the Big Four professional services firms. Salary range explicitly disclosed ($155,600–$306,800). FDE is an established Deloitte practice (they have published FDE program materials). JD is specific (AWS AI&Data product list, certification requirements, travel model, pod structure). No ghost indicators.

---

## Machine Summary

```yaml
company: Deloitte
role: Forward Deployed Engineer, AWS AI&Data
score: 3.1
status: Applied
date: 2026-09-08
salary_low: 155600
salary_high: 306800
location: US (client-embedded; 50% travel; DC/Virginia proximity advantage)
remote: false (client-site travel model)
visa: likely (Deloitte files thousands of H-1B petitions annually; "limited sponsorship may be available")
proptech_boost: false
h1b_status: likely (Big Four firm; "limited immigration sponsorship may be available")
top_match: FDE primary target archetype; agentic platforms (LeaseI 8-agent HITL); LLMOps (AgentProbe); GenAI production (Magizhs); Python; client-facing delivery; $155K-$307K; Deloitte H-1B likely
gaps: AWS certifications required (3 of 6; none held); Amazon Bedrock/AgentCore/Strands Agents SDK required (not in background); AWS Neptune + OpenSearch required; 50% travel; Big Four compliance culture
```
