# Interview Intel: Juniper Square — Senior Software Engineer, Data (AI)

**URL:** https://jobs.ashbyhq.com/junipersquare/520b5d66-6520-4604-9b3c-bbb71fd935ba
**Legitimacy:** High Confidence
**Report:** [135](../reports/135-juniper-square-senior-swe-data-ai-2026-06-29.md)
**Researched:** 2026-07-09
**Sources:** Glassdoor (SWE + Senior SWE interview pages), Blind (interview discussions), company blog, LinkedIn
**Audiences covered:** recruiter-screen, hiring-manager, peer-tech

---

## Process Overview

- **Rounds:** ~4 rounds (recruiter screen → technical EM call → coding challenge / take-home → full panel)
- **Format:** Recruiter/HR call → Technical call with Engineering Manager → Coding challenge (90 min, build an API) or take-home (30 min, 2 questions) → Onsite loop (~6 interviews, ~5 hours)
- **Difficulty:** 2.8/5 (Glassdoor avg)
- **Positive experience rate:** 48% (Glassdoor)
- **Known quirks:**
  - Heavy emphasis on **product understanding and business context** — they want to know you've studied JunieAI, not just the stack
  - **No pure LeetCode** — coding is practical: "build an API" style, database modeling, algorithm questions
  - **Database modeling** appears consistently across multiple reviews
  - Final onsite is intense (~6 interviews, 5 hours) — pace yourself
- **Sources:** [Glassdoor SWE Interviews](https://www.glassdoor.com/Interview/Juniper-Square-Software-Engineer-Interview-Questions-EI_IE1545781.0,14_KO15,32.htm) | [Glassdoor Senior SWE](https://www.glassdoor.com/Interview/Juniper-Square-Senior-Software-Engineer-Interview-Questions-EI_IE1545781.0,14_KO15,39.htm) | [Blind](https://www.teamblind.com/company/Juniper-Square/posts/juniper-square-interview)

---

## Audience Map

- **Tomorrow's call** (recruiter screen, ~30 min) → `recruiter-screen`
- **Round 2** (likely technical with EM, ~60 min) → `hiring-manager` or `peer-tech` [inferred]
- **Round 3** (coding challenge: 90 min build-an-API OR take-home 30 min / 2 questions) → `peer-tech`
- **Round 4** (onsite loop, ~5 hours, 6 interviews) → `panel-mixed`

---

## Company Context — Know Before You Call

**JunieAI** is Juniper Square's AI product — embedded directly into their private markets platform (not bolted on the side). It automates IR workflows for fund managers: drafting LP emails, compiling quarterly reports, extracting key terms from fund documents, summarizing meeting notes.

- **Valuation:** $1.1B (unicorn) — crossed in 2025
- **Clients:** 2,000+ institutional real estate clients managing $300B+ in private market assets
- **Funding:** Series D, $75M raised (originally), total $350M+
- **2026 recognition:** Fast Company Most Innovative Companies list
- **Why they're hiring AI engineers:** Building out JunieAI's data layer — normalization, schema mapping, validation, enrichment pipelines + LLM-powered features

**Domain bridge to use:** "Juniper Square serves the fund managers and LPs who invest in real estate portfolios. Entrata served the property managers who operate them. I spent 8 years on the operational side of the same real estate transaction — I know owner financial reporting, distribution workflows, and the compliance schemas that institutional real estate finance runs on."

---

## Round 1 — Recruiter Screen (Tomorrow)

### audience: `recruiter-screen`

This is a fit gate. The recruiter wants: right motivation, no logistics surprises (comp, visa, location), clean narrative. Shine here → move to EM call.

---

### "Walk me through your background"

**60-second version (use this):**
> "I'm a software engineer and AI builder with 8 years of production experience at Entrata — a PropTech platform serving 100K+ monthly active users. At Entrata I owned 20+ production modules end-to-end: data pipelines on 1M+ financial records, AWS infrastructure, schema design, compliance automation. After 8 years I completed my MS in Data Analytics Engineering at George Mason (GPA 3.87, May 2026) and built two open-source AI projects: LeaseI — a RAG compliance pipeline achieving 93.6% precision on lease documents — and AgentProbe — a multi-agent testing toolkit with a 5-metric LLM evaluation engine. I'm targeting roles that combine data engineering depth with production AI — the Senior Data (AI) SWE role at Juniper Square maps directly to both."

---

### "Why Juniper Square?"

> "Two reasons. First, the JunieAI product is genuinely interesting — you're building AI that needs to be auditable on high-stakes fund documents, not just useful. That's the same problem I solved with LeaseI: RAG over complex financial/legal documents with a deterministic rules engine so every output is traceable. Second, the domain. Juniper Square serves the investors and fund managers who own real estate portfolios. Entrata serves the property managers who operate them. I spent 8 years building the financial data systems on the operational side — I already understand the data those investors want to analyze."

---

### Comp question

The JD lists **$185K–$225K**. This is well above your $100-140K target. Do NOT anchor to your target — anchor to the band.

> "The posted range of $185K–$225K is in line with what I'm targeting for this level. I'm flexible on the structure between base and equity — what matters most is the scope of the work."

If they push for a number: "Within that band, I'm targeting the $185–$200K range as a starting point, open to discussing equity and total comp."

---

### Visa / Work Authorization

> "I'm on F-1 STEM OPT, which gives me 3 years of work authorization through [your OPT end date]. I'm a strong H-1B candidate — MS from George Mason (GPA 3.87), 8+ years of specialized AI engineering experience. Does Juniper Square sponsor H-1B? I saw your LCA history suggests yes, but wanted to confirm directly."

**Note:** Report #124 (Staff SWE AI) confirmed 14 LCAs filed 2022–2024, all certified. Mention this context if they hesitate — it's public record.

---

### "Why are you leaving / what are you looking for?"

> "I spent 8 years building production systems at Entrata — great engineering foundation, shipped 20+ modules at scale. After completing my MS, I've been focusing on AI engineering: LeaseI and AgentProbe are both live projects. I'm looking for a role where both sides of my background matter — production data engineering depth and hands-on AI/LLM work. The Senior Data AI role is exactly that."

---

### Location / Remote

> "Remote works well for me — I'm in Virginia. No logistics friction."

---

### Timeline / Notice

> "I'm actively interviewing and available to start within [X weeks]. No notice period."

---

### Other processes

If asked: "I'm in a few processes at similar-stage companies. Juniper Square is one of my top choices because of the JunieAI product and the domain alignment." Don't name companies unless pressed.

---

### Red flag: "8 years at one company — can you adapt?"

> "Entrata grew from a regional player to a national PropTech platform while I was there. I shipped across 20+ modules — data pipelines, microservices, AI, compliance, Salesforce integrations, Docker rollout across the entire stack. The breadth is the point. I wasn't doing the same thing for 8 years — I was doing everything, in a company that kept getting more complex. The pace at a Series D startup is something I'm actively looking for."

---

## Round 2 — Technical / Hiring Manager Call

### audience: `hiring-manager` / `peer-tech` [inferred]

---

### "Why this specific role?"

> "The JD lists three areas I've built end-to-end: data normalization and schema mapping pipelines, production LLM features, and AI output evaluation. At Entrata I built 20+ production data modules on 1M+ financial records with schema design, ETL, and AWS pipelines. The AI output evaluation piece — AgentProbe's 5-metric eval engine with deterministic checks and cross-model comparison — is directly what the preferred skills list is asking for. Not 'I've read about it' — I've built the production version."

---

### "What would your first 90 days look like?"

> "First 30 days: understand the data model. JunieAI ingests fund documents, LP statements, K-1s — every schema has quirks. I'd spend time with the data layer, trace the normalization pipeline end to end, and map where validation gaps exist. Days 30–60: ship something small but real. A validation rule, a schema fix, an eval test case — something that shows I understand the production system, not just the architecture. Days 60–90: propose an improvement. Either to the eval pipeline, the RAG retrieval quality, or the data normalization coverage. Something specific to a gap I found in the first 60 days."

---

### Sharp questions to ask them

1. "JunieAI extracts structured data from fund documents — K-1s, LP reports, capital call notices. What's the biggest source of extraction error right now — document variety, schema inconsistency, or LLM hallucination?"
2. "You mentioned AI output evaluation as a preferred skill. What does the current eval pipeline look like? Is it mostly manual review, automated metrics, or a mix?"
3. "Fast Company recognized you in 2026 — what specifically drove that, and where does the engineering team feel most pressure to deliver next?"

---

## Round 3 — Coding / Technical Challenge

### audience: `peer-tech`

Based on Glassdoor/Blind intel:

**Likely formats (not fabricated — both were reported):**
- 90-minute challenge: build an API [source: Blind]
- 30-minute take-home: 2 questions [source: Blind]
- Database modeling question [source: Glassdoor, multiple reports]
- Algorithm question [source: Glassdoor]
- JavaScript question [source: Glassdoor — but your stack is Python; flag this if it comes up]

---

### Technical Prep Checklist

- [ ] **Design a REST API from scratch** — practice FastAPI: endpoint design, request validation, error handling, auth headers. You've built a 15-endpoint FastAPI (AgentProbe) — use that as mental scaffolding.
- [ ] **Database schema design / normalization** — practice: given a domain (e.g., "fund manager with LPs, investments, capital calls"), design normalized tables with foreign keys, indexes. This appears in multiple reviews.
- [ ] **SQL query optimization** — you've tuned 200+ queries; be ready to walk through execution plan thinking out loud.
- [ ] **ETL pipeline design** — given a data source with inconsistent schemas, how do you normalize, validate, and enrich? Walk through your Entrata approach.
- [ ] **RAG system design** — how would you build a RAG pipeline over fund documents? Chunking strategy, embedding model choice, retrieval method, reranking, eval. LeaseI is your proof point.
- [ ] **AI output evaluation** — how do you evaluate LLM outputs on financial documents? Deterministic checks + LLM-as-judge. AgentProbe is the proof point.
- [ ] **pgvector vs ChromaDB** — know the tradeoffs. You use ChromaDB; pgvector lives inside Postgres. Be ready to say "I've used ChromaDB in production and pgvector is the natural next step for a Postgres-native stack."

---

### Technical Questions — Likely from JD

| Topic | Source | Your Angle |
|-------|--------|-----------|
| Design a data normalization pipeline | [inferred from JD] | Entrata: 20+ modules, income eligibility schemas, AMI threshold data |
| Build an API for document ingestion | [inferred from JD] + Blind | AgentProbe FastAPI backend, 15 endpoints, LangGraph integration |
| Schema design for financial data | Glassdoor (multiple) | Entrata: distribution reporting, financial account workflows, 200+ SQL queries |
| RAG pipeline architecture | [inferred from JD] | LeaseI: 1,240 PDFs, chunking, embedding, retrieval, deterministic rules engine |
| LLM evaluation approach | [inferred from JD] | AgentProbe: 5-metric LLM-as-judge, deterministic checks, pass@k harness |
| How do you handle LLM hallucination in production? | [inferred from JD] | Output validation gates, CI/CD blocking, deterministic fallback rules |
| AWS data infrastructure | [inferred from JD] | Entrata: S3, RDS, EC2, Glue — PHI migration, zero incidents |

---

## Story Bank Mapping

| # | Audience | Topic | Best Story | Fit |
|---|----------|-------|-----------|-----|
| 1 | recruiter-screen | Walk me through your background | Exit narrative (above) | Strong |
| 2 | recruiter-screen | One company for 8 years | Adaptability framing (above) | Strong |
| 3 | hiring-manager | Production data pipelines | Entrata 1M+ records, 20+ modules, ETL/schema | Strong |
| 4 | hiring-manager | Why Juniper Square | Domain bridge (above) | Strong |
| 5 | peer-tech | RAG system | LeaseI: 93.6% precision, 1,240 PDFs, deterministic rules | Strong |
| 6 | peer-tech | LLM evaluation | AgentProbe: 5-metric eval, CI/CD gates, pass@k harness | Strong |
| 7 | peer-tech | Production AI at scale | Entrata: 1.6M records, quality gates, zero compliance violations | Strong |
| 8 | peer-tech | Database schema design | Entrata: 20+ production modules, 200+ SQL queries optimized | Strong |
| 9 | peer-tech | AWS infrastructure | Entrata: PHI S3 migration, 100% compliance, zero incidents | Strong |
| 10 | panel-mixed | Domain knowledge | Entrata financial data → JunieAI investor data bridge | Partial → reframe |

**Gap identified:** No story specifically about *cross-team alignment on data schema changes* (common in growing startups). Use the Docker microservices rollout story as a proxy — cross-team coordination + technical change management.

---

## Key Vocab to Use

These terms appear in the JD and should come out naturally:

- **Data normalization, schema mapping, enrichment** (not just "ETL")
- **AI output evaluation** (not just "testing")
- **Deterministic checks** (not just "validation")
- **Agentic workflows** (not just "agents")
- **Production LLMs** (not just "using LLMs")
- **JunieAI** — show you know the product name
- **Private markets** — show you know the domain (fund managers, LPs, capital calls, K-1s)

---

## What NOT to Say

- Don't lead with your $100-140K comp target — the JD band is $185-225K, anchor to that.
- Don't say "I used ChromaDB but not pgvector" as a gap — frame it as "ChromaDB in production, pgvector is the natural extension in a Postgres-native stack."
- Don't volunteer that the Staff SWE role (#124) had a hiring freeze concern — that was a different posting; this one is clean.
- Don't say "affordable housing" when you mean "real estate finance compliance" — the JunieAI audience is fund managers, not property managers.
- Don't say "I'm looking for my first AI role" — you shipped production AI at 1.6M records at Entrata.

---

## Logistics Checklist for Tomorrow

- [ ] Confirm exact time and video link (Zoom / Google Meet / Teams?)
- [ ] Review report #135 one more time — especially Block B (match table) and Block C (framing)
- [ ] Have AgentProbe GitHub link ready to paste if they ask for portfolio
- [ ] Know your OPT authorization end date (for visa question)
- [ ] Have 2-3 questions ready (use the "sharp questions" section above)
- [ ] Block 15 min after the call to write down what they asked
