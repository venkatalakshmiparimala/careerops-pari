# Leadership Screen Prep: Juniper Square
## Daniel Lipkin — VP, Engineering
**Date:** Tuesday, July 14, 2026 | 12:15–1:00 PM EDT
**Format:** Zoom (45 min)
**4 Focus Areas:** Technical Depth · AI Fluency · Career Trajectory · Scope & Influence

---

## What This Interview Is

This is NOT a technical screen. Daniel Lipkin is a VP deciding whether you think at the right level — whether you can own a problem end-to-end, influence without authority, and grow into a senior contributor. He wants to see judgment, not just code.

**Your job in this call:**
- Sound like someone who has shipped real AI at scale, not someone learning AI
- Connect your background directly to what JunieAI needs
- Show you've thought about the *business* of what you're building, not just the tech
- Ask questions that make him think "this person has already started doing the job"

---

## Opening Narrative (First 90 Seconds)

> "I'm a software engineer and ML engineer with 8 years of production experience at Entrata — a PropTech SaaS platform serving 100K+ monthly active users. I owned 20+ modules end-to-end: data pipelines on 1.6M financial records, microservices, compliance automation, AWS infrastructure. I shipped Entrata's first production AI pipeline — Python, PyTorch, OpenAI API — on regulated financial data with full compliance controls.
>
> After 8 years I completed my MS in Data Analytics Engineering at George Mason (GPA 3.87, May 2026) and built two AI projects: LeaseI — a RAG compliance pipeline achieving 93.6% precision on 1,240 lease PDFs with a deterministic rules engine — and AgentProbe — a multi-agent testing toolkit with a 5-metric LLM evaluation engine, CI/CD integration, and full observability dashboard.
>
> The reason Juniper Square makes sense: JunieAI needs LLM pipelines that are auditable on high-stakes financial documents. That's exactly the constraint I designed for in LeaseI. And the domain — Juniper Square serves the fund managers who invest in real estate portfolios; Entrata served the property managers who operate them. I spent 8 years on the operational data side of that same transaction. I understand the schemas, the compliance requirements, and the reporting workflows that institutional real estate finance depends on."

---

## Focus Area 1: Technical Depth

**What Daniel is probing:** Can you go deep on AI systems, data pipelines, and architecture — or do you just talk about them?

---

### "What's the most technically complex thing you've built?"

> "LeaseI. It's a RAG pipeline over 1,240 residential lease PDFs across 5 US states. The complexity wasn't the retrieval — it was making the compliance determinations auditable.
>
> The problem: LLMs give you probabilistic outputs on legal documents that need to be defensible. You can't tell a tenant 'the model thought your lease violated habitability standards with 73% confidence.' So I built a deterministic rules engine underneath the LLM layer — 10 structured compliance rules that map retrieved context to a binary pass/fail with cited sources. The LLM handles language understanding; the rules engine handles the compliance determination.
>
> Result: 93.6% precision, 87.9% F1, pass@1 of 81.7% and pass@3 of 88.3% — measured with a pass@k harness and LLM-as-judge scoring. Every output is fully traceable. That's the architecture JunieAI needs for fund documents — the LLM reads, the rules decide, the audit trail is always there."

---

### "Walk me through how AgentProbe works under the hood."

> "Three LangGraph agents with typed state handoffs: Orchestrator receives the test request and breaks it into subtasks; RAG Tracer monitors retrieval quality independently from generation quality — that's an important architectural choice; Auto Fix agent catches failing runs and attempts correction before surfacing to the user.
>
> The eval engine scores every output on 5 metrics: factual accuracy, hallucination rate, retrieval quality, completeness, and compliance. It's LLM-as-judge, but the judge prompt is itself calibrated — meta-evaluation was harder than the application. The whole thing is integrated into CI/CD so failing runs block production automatically.
>
> The observability dashboard tracks per-run regression drift — so you can see if retrieval quality is degrading over time, not just whether a single run passed."

---

### "How do you handle LLM hallucination in production?"

> "Three layers. First, deterministic checks before any LLM output reaches the user — schema validation, boundary checks, required field presence. Second, LLM-as-judge evaluation that scores outputs on factual accuracy and hallucination rate — automated, not manual review. Third, a CI/CD gate that blocks the failing run so it never hits production.
>
> The key insight is that hallucination is most dangerous in the cases you don't catch — the outputs that look right but are wrong. That's why retrieval quality is monitored separately. A hallucination on regulated financial data isn't a UX problem, it's a compliance problem. The architecture has to treat it that way."

---

### "pgvector vs ChromaDB — what's your view?"

> "I've used ChromaDB in production — it's fast to set up, great for development and isolated workloads. For a Postgres-native stack like Juniper Square's, pgvector is the natural production choice: co-located with your source data, one fewer moving part, ACID guarantees, existing connection pooling and backup infrastructure. The query patterns are similar. Migration from ChromaDB to pgvector is straightforward once you've already abstracted the retriever interface — which I do by design."

---

## Focus Area 2: AI Fluency

**What Daniel is probing:** Do you understand AI deeply enough to make good product decisions, or just implement what you're told?

---

### "Where do you think AI in private markets/fintech is going in the next 2-3 years?"

> "Three shifts I see coming. First, the move from document extraction to document reasoning — not just 'pull the carried interest rate from this LP agreement' but 'is this LP agreement's fee structure consistent with market standard for this vintage and strategy?' That requires structured financial knowledge, not just retrieval.
>
> Second, structured output reliability will become the table stakes differentiator. Right now most RAG products produce unstructured summaries. The next generation will produce structured, field-level extractions that plug directly into financial models and reporting systems. Juniper Square is well-positioned here because the data model already exists in the platform.
>
> Third, evaluation infrastructure becomes a competitive moat. Companies that have built systematic eval pipelines — not one-off human review — will iterate 10x faster on model improvements. That's why I built AgentProbe: the eval problem is harder and more durable than the application problem."

---

### "What's your approach to prompt engineering vs fine-tuning?"

> "Prompt engineering first, always. It's faster to iterate, easier to debug, and you keep the benefit of the foundation model's generalization. Fine-tuning makes sense when you have a very specific, high-volume task with consistent input/output format and enough labeled data — typically 1,000+ examples minimum.
>
> For JunieAI's use case — fund document extraction with high accuracy requirements — I'd start with structured prompting plus a deterministic validation layer. Fine-tune only if prompt engineering plateaus on specific document types that have unique vocabulary or schema patterns the base model consistently misses."

---

### "How do you evaluate AI output quality on financial documents?"

> "You need two layers that you evaluate independently. Layer 1: retrieval quality — is the right context being surfaced from the document? Measure precision/recall at the chunk level against a ground truth set. Layer 2: generation quality — given correct context, is the output accurate and complete? Measure with LLM-as-judge on a rubric calibrated to the financial domain.
>
> For high-stakes outputs — fund terms, distributions, capital call amounts — add a third deterministic layer: numeric validation, schema enforcement, and cross-reference checks against structured data you already have. LeaseI uses all three. AgentProbe's eval engine implements the second and third."

---

## Focus Area 3: Career Trajectory

**What Daniel is probing:** Is this role the right next step for you, or are you using us as a stepping stone?

---

### "Why now, after 8 years at one company?"

> "Entrata gave me production depth I couldn't have gotten anywhere faster — 20+ modules, real scale, regulated data, every layer of the stack. I left when I had completed what I set out to do there and when the AI engineering opportunity shifted.
>
> The MS was intentional: I wanted to formalize the statistical and ML foundations I'd been applying in production without always being able to explain why. GPA 3.87 in Data Analytics Engineering — that's not incidental. And the two AI projects aren't portfolio pieces — they're systems I built to solve problems I actually had as an engineer.
>
> I'm at the right point in my career to take what I've built and apply it in a company where the AI work is the product, not a feature. That's Juniper Square."

---

### "Where do you want to be in 3 years?"

> "Owning a significant piece of AI infrastructure at a company that's winning in its space. That means: technical scope that includes data pipeline ownership, LLM system design, and eval infrastructure — not just implementing features someone else specced. I want to be the person who sets the standard for how AI outputs are validated and trusted in the product.
>
> At Juniper Square specifically, that looks like being the engineer who built the eval and validation layer that lets JunieAI move faster and with more confidence. That's a 3-year problem worth solving."

---

### "What does success look like for you in this role at 6 months?"

> "At 6 months I want to have shipped something that measurably improved JunieAI's output reliability — either a new eval metric that catches a class of failures we were missing, a data normalization improvement that reduces extraction errors on a specific document type, or a validation layer that lets the team ship new features faster with confidence. One real, measurable improvement — not a long list of tasks completed."

---

## Focus Area 4: Scope & Influence

**What Daniel is probing:** Have you operated beyond your job title? Can you drive change, align teams, and make things better beyond your immediate scope?

---

### "Tell me about a time you influenced a technical decision you didn't own."

> "At Entrata, the microservices migration. We had a monolithic PHP codebase — 20+ modules tightly coupled. I wasn't the architect, but I could see that deployment speed was the bottleneck preventing us from shipping faster.
>
> I built a proof of concept on one non-critical module — containerized it with Docker, documented the migration pattern, showed the deployment time improvement in numbers. Then I presented it to the architecture team not as 'here's what we should do' but as 'here's what I've already done and here are the results.' That changed the conversation from theoretical to practical.
>
> Result: 20% of product modules converted to service-based architecture, 30% reduction in deployment time, 50% improvement in scalability. The decision was made by people above me, but the work that made it happen was mine."

---

### "How have you raised the bar for a team beyond your own work?"

> "Two things at Entrata. First, 300+ peer code reviews with structured reasoning feedback — not just 'change this line' but 'here's the security risk and here's how to think about it.' The goal was engineers who make better decisions autonomously, not engineers who wait for review. Second, I developed internal debugging tools that reduced debugging time by 40% — tools the whole team used, not just me. Impact beyond your own output is the difference between a senior engineer and a lead."

---

### "Tell me about a time you pushed back on a product decision."

> "At Entrata, we were under pressure to ship income eligibility automation quickly for a major client. The initial approach was to automate the threshold calculations without validation gates — fast to ship, but if AMI calculations were wrong, we'd have compliance violations across client portfolios.
>
> I pushed back with specific data: showed the distribution of edge cases in the existing data that the simple approach would mishandle. Proposed adding a validation layer that added 2 sprints but would catch every error class I'd identified. The product team pushed back on the timeline.
>
> I presented it as a risk tradeoff with real numbers — estimated probability of a compliance violation × cost of remediation vs 2 sprints of delay. The validation layer got approved. Zero compliance violations at launch or after."

---

## Sharp Questions to Ask Daniel Lipkin

Ask 2-3 of these — pick based on how the conversation flows:

1. **On JunieAI's current state:**
   > "JunieAI is ingesting fund documents — K-1s, LP reports, capital call notices. What's the biggest source of extraction error right now — document variety, schema inconsistency, or LLM hallucination on financial numerics?"

2. **On where the engineering team is focusing:**
   > "When you think about what's blocking JunieAI from moving faster, is it on the data pipeline side — normalization and schema coverage — or on the LLM reliability side — eval and validation?"

3. **On team culture:**
   > "What does a senior engineer at Juniper Square own that a mid-level engineer doesn't? I want to understand where the scope boundary is."

4. **On the role's impact:**
   > "If the person you hire for this role executes really well in year one, what changes about JunieAI that wouldn't have changed otherwise?"

---

## What NOT to Say

- Don't say "I'm new to private markets" — you're not new to financial data or real estate schemas
- Don't downplay the 8 years at one company — reframe it as depth and breadth, not stagnation
- Don't say "I'm looking for my first AI role" — you shipped production AI on 1.6M records
- Don't anchor to your old comp — the band is $185K–$225K, anchor there
- Don't give vague answers on career trajectory — be specific about what you want to own

---

## Logistics Checklist

- [ ] Zoom link is in the calendar invite from Linda Huard — test audio/video Monday evening
- [ ] Have browser tab open with: AgentProbe GitHub, LeaseI GitHub, your portfolio
- [ ] Know your OPT end date for visa question
- [ ] Block 15 min after the call to write down every question they asked
- [ ] Eat before — 12:15 PM start, don't interview hungry
- [ ] Have water on the desk

---

## The One Thing to Remember

Daniel Lipkin is a VP. He's not verifying that you can code — the recruiter and technical rounds do that. He's deciding whether you think at the right level to be a force multiplier on his team. Every answer should show **judgment**, not just execution.

Lead with the *why* behind your decisions, not the *what*.
