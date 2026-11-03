# Interview Intel: Amazon (AWS) — Senior Applied AI Solutions Architect, Amazon Connect

**URL:** https://amazon.jobs/en/jobs/10390088/senior-applied-ai-solutions-architect-amazon-connect-applied-ai-sa-aivt
**Legitimacy:** Proceed with Caution (recruiter-initiated; Amazon #1 H-1B sponsor)
**Report:** [#144](../reports/144-amazon-aws-sr-applied-ai-sa-amazon-connect-2026-07-14.md)
**Researched:** 2026-08-06
**Sources:** Glassdoor, Exponent, Interview Kickstart, Amazon.jobs, Teamblind, mybusinessfuture.com
**Audiences covered:** recruiter-screen, hiring-manager, peer-tech, panel-mixed

---

## Process Overview

- **Rounds:** 5–6 total (recruiter screen → technical phone screen → virtual loop of 4–5 rounds)
- **Format:** Recruiter call (30 min) → Technical phone screen (60 min) → Virtual onsite loop: 4–5 back-to-back 1-hour rounds (Technical, System Design, LP × 2–3, Bar Raiser)
- **Difficulty:** 4/5 — Amazon bar is consistently high; LP questions are as rigorous as technical
- **LP weight:** Every single round includes LP questions. Each interviewer is assigned 2–3 specific LPs to evaluate.
- **Bar Raiser:** One round is conducted by a Bar Raiser (senior Amazon employee from another team) — they only pass candidates who raise the bar for Amazon overall, not just for this team
- **Known quirks:** No LeetCode-style algorithmic coding; replaced by architecture discussion + system design. Every technical answer should include a failure/trade-off angle — Amazon interviewers dig into "what went wrong"
- **Timeline:** Recruiter screen → ~1 week → technical screen → ~1–2 weeks → loop. Total: 3–6 weeks from Round 1
- **Sources:** [Glassdoor AWS SA Reviews](https://www.glassdoor.com/Interview/Amazon-Web-Services-Solution-Architect-Interview-Questions-EI_IE7470741.0,19_KO20,38.htm), [Exponent Guide](https://www.tryexponent.com/guides/amazon-solutions-architect-interview), [Interview Kickstart](https://interviewkickstart.com/blogs/companies/aws-solutions-architect-interview-process)

---

## Audience Map

- **Round 1 (Monday)** — Recruiter screen, ~30 min → `recruiter-screen`
- **Round 2** — Technical phone screen, ~60 min → `peer-tech`
- **Round 3–6** — Virtual onsite loop (4–5 rounds, 1 hour each) → `panel-mixed` (Technical + System Design + LP rounds + Bar Raiser)

---

## Round 1: Recruiter Screen — audience: `recruiter-screen`

**Duration:** 30 min
**Conducted by:** Recruiter / HR
**What they evaluate:** Motivation, comp alignment, visa/location fit, basic background, timeline, very light LP check

### What to lead with

> "I've spent 8 years building production systems at enterprise scale — 100K+ active users, regulated financial data, complex federal compliance workflows. For the last 2 years I've been building agentic AI on top of that foundation: LeaseI is an 8-agent LangGraph system deployed on real housing compliance workflows with 93.6% precision. The Amazon Connect SA role is exactly where I want to take that work — deploying agentic AI for enterprise customers, not just building demos."

Keep it to 60–90 seconds. Land on "agentic AI at enterprise scale" + "I want to help customers deploy, not just configure."

### Prepared answers

**"Walk me through your background"** (60–90 sec)
> "I'm a production AI engineer based in Virginia. I spent 8 years at Entrata building production software for enterprise property management — 100K+ monthly active users, federal housing compliance (LIHTC, HUD, Section 8), real financial data at scale. While completing my MS in Data Analytics Engineering at GMU, I built LeaseI — an 8-agent agentic AI system that does compliance document analysis, root-cause investigation, and tenant self-service with HITL escalation baked in. 93.6% precision on 1,240 real lease PDFs. I'm now looking for a role where I can take that agentic AI depth and apply it customer-facing — helping enterprise customers get from POC to production. That's exactly what the Amazon Connect Applied AI SA role is."

**"Why Amazon Connect specifically?"**
> "Amazon Connect is the place where agentic AI is most urgently needed right now — contact centers have the highest volume of repetitive, high-stakes customer interactions, and AI is genuinely transforming that. The AIVT team structure — dedicated advisory directly with customers to go production-ready in weeks — is the model I want to operate in. I've been following what Amazon Connect launched in April 2026 with the four agentic AI standalone solutions. I want to be on the team building that customer motion."

**Comp**
The posted band is $153,600–$207,800 base + RSUs + sign-on. If asked:
> "I'm targeting the $160K–$190K base range for an L6 Senior SA, which I understand is consistent with Amazon's band for this role. Total comp with RSUs is more important than base alone — I'm looking for a strong total package."

If they push for a number first, defer: *"Can you share the band you have for this role? I want to make sure we're aligned before going further."*

**Visa / location**
> "I'm currently on STEM OPT in Virginia — zero relocation needed for Herndon VA. I'll need H-1B sponsorship — I understand Amazon is the #1 H-1B sponsor in the US and files under Amazon Web Services, Inc. Is this role eligible for H-1B sponsorship?"

Ask this early — don't wait. If they say yes, confirm timeline (H-1B cap lottery is April, with October 1 start — verify where you are in OPT to understand your window).

**Travel (25–40%)**
> "I'm comfortable with the 25–40% travel requirement — customer-facing deployment work requires being onsite. That's part of the SA role I'm signing up for."

**Timeline**
> "I'm available immediately — no notice period."

**"Are you interviewing elsewhere?"**
> "I'm in active conversations with a few companies — mostly AI/ML engineering and solutions architect roles. Amazon is my top choice in this category given the H-1B certainty and the Amazon Connect AI roadmap."

### What NOT to volunteer
- Don't mention the Amazon Connect domain gap unprompted — the recruiter isn't there to evaluate technical depth
- Don't share competing offer specifics
- Don't say you're "open to any range"

---

## Round 2: Technical Phone Screen — audience: `peer-tech`

**Duration:** 60 min
**Conducted by:** Senior SA or technical hiring panel member
**What they evaluate:** Technical depth on AI/cloud architecture, LP check (2–3 principles), ability to discuss trade-offs without code

### Likely questions

**Technical — Architecture**
- *"Walk me through how you'd design an agentic AI system for a contact center customer that needs to resolve billing inquiries without human agents."* `[inferred from JD]`
  - **Your angle:** LeaseI Triage → Retrieval → Reasoning → Validation → Escalation pattern. Map directly. "I built exactly this pattern in LeaseI — the AI handles the retrieval and reasoning; deterministic rules make the compliance call; HITL triggers when confidence is below threshold. For a billing contact center: same architecture — LLM resolves standard queries, deterministic rules handle refund thresholds, escalation when ambiguous."

- *"How would you integrate Amazon Bedrock into an existing customer workflow that already uses a different LLM provider?"* `[inferred from JD]`
  - **Your angle:** AgentProbe multi-provider routing (Anthropic, OpenAI, Groq, Ollama). "I've built provider-agnostic LLM routing — the routing contract abstracts over providers so swap-in is a config change, not a re-architecture. For Bedrock: same pattern, different provider wrapper. The customer's evaluation criteria for switching are latency, cost per token, and task-specific quality — I'd run A/B comparisons on their actual prompts."

- *"What's your approach to prompt engineering for production agentic systems?"* `[inferred from JD]`
  - **Your angle:** LeaseI prompt engineering discipline. "Chain-of-thought for reasoning chains, few-shot for domain-specific output formats, role specification to bound the agent's scope, XML-structured outputs for parsing reliability, output validation gates to catch malformed responses. The most important discipline: test your eval prompt as rigorously as your application prompt — the judge has to be calibrated."

- *"Explain RAG and when you'd use it vs. fine-tuning."* `[inferred from JD]`
  - **Your angle:** LeaseI TF-IDF (structured) vs ChromaDB (semantic) decision + production precision numbers. "RAG when you need fresh, auditable, domain-specific knowledge with source citation. Fine-tuning when you need behavioral style changes across all outputs. For compliance use cases I always choose RAG — the answer has to be cited to a specific clause or flagged as unsupported. You can't cite a fine-tuned weight. For LeaseI I also chose TF-IDF over dense embeddings for structured PDF clauses — semantic search blurs clause boundaries; sparse retrieval respects them."

**LP questions (expect 2)**
See LP section below.

---

## Round 3–6: Virtual Onsite Loop — audience: `panel-mixed`

**Format:** 4–5 × 1-hour back-to-back. Expect: System Design, Technical Deep-Dive, LP × 2, Bar Raiser (LP-heavy).

### System Design Round

**Likely prompt:** *"Design an agentic AI system for Amazon Connect that handles customer service calls and escalates to human agents when needed."* `[inferred from JD]`

**Strong answer structure:**
1. **Clarify requirements** (2 min): "How many concurrent calls? What's the escalation threshold? What's the latency requirement per turn? What data sources does the agent access?"
2. **High-level architecture**: Amazon Connect → Contact Flows → Amazon Lex → Bedrock (LLM) → Knowledge Base (RAG over KB articles) → Escalation Logic → Human Agent Queue
3. **Agentic layer**: Multi-turn memory via session context; tool calling for CRM lookup, order history, policy retrieval; confidence-gated escalation (not just "I don't know" — a scored threshold)
4. **HITL design**: When confidence < threshold OR sentiment = hostile OR query type = refund > $X → route to human with full context summary pre-populated
5. **Eval layer**: LLM-as-judge scoring on sample calls; regression tracking on resolution rate, CSAT, escalation rate
6. **Trade-offs to mention**: Latency vs accuracy (streaming vs complete generation); Bedrock model selection (Nova Lite for simple, Nova Pro for complex); cost optimization via routing

**Your differentiator**: "The architecture I'm describing maps directly to what I built in LeaseI — except the delivery channel is a phone call instead of a web interface. The agent orchestration pattern, confidence-gated escalation, and HITL logic are identical. I've already validated this approach on regulated data."

### Technical Deep-Dive Round

*"Tell me about the most technically complex AI system you've built."*
→ **Use LeaseI HITL story** from story bank. Add: "The hardest part wasn't the retrieval or the LLM integration — it was designing the escalation logic so that borderline cases always route to a human rather than generating a confident-sounding wrong answer. That's the architecture decision that matters in production."

### Bar Raiser Round

Bar Raisers are LP-heavy. They push harder on your weakest stories and look for inconsistencies. Expect:
- "Tell me about a time you disagreed with a technical decision and what happened." (Have Backbone; Disagree and Commit)
- "Tell me about your biggest failure." (Learn and Be Curious, Ownership)
- "Why should Amazon hire you over someone who has 3 years of Amazon Connect experience?" (Be direct — don't deflect)

**For the last question:**
> "Someone with Amazon Connect domain experience knows the product. I know how to build agentic AI systems that work in production on regulated enterprise data — and I can ramp on any domain quickly. LeaseI is evidence of that: I had no prior LegalTech background; I built a production-grade system with 93.6% precision. The Amazon Connect customer who's struggling isn't struggling because their vendor doesn't know the product — they're struggling because nobody knows how to get an agentic AI workflow to production reliably. That's where I add value."

---

## Amazon's 16 Leadership Principles — Story Mapping

Each interviewer is assigned 2–3 LPs. Prepare one strong story per principle. Below are the most likely for this SA role + your best story for each.

| LP | Most likely question | Your story | Fit |
|----|---------------------|------------|-----|
| **Customer Obsession** | "Tell me about a time you went beyond what was asked to deliver for a customer." | Entrata: Redesigning income limits module for 100K+ MAU with zero compliance violations — stakeholder sessions across Compliance, Legal, Ops, Product before writing a line of code | Strong |
| **Ownership** | "Tell me about a time you took responsibility for a failure." | Entrata: PHI migration — owned end-to-end design, implementation, and compliance verification; zero incidents | Strong |
| **Invent and Simplify** | "Tell me about a time you found a simpler solution to a complex problem." | LeaseI: Chose TF-IDF over ChromaDB for structured PDFs — simpler approach outperformed the more complex one; or AgentProbe multi-provider routing via a single abstraction layer | Strong |
| **Are Right A Lot** | "Tell me about a time you made a decision with incomplete information." | LeaseI retrieval method decision — evaluated TF-IDF vs dense embeddings on structured vs unstructured content types; made data-driven call; proved correct at 93.6% precision | Strong |
| **Learn and Be Curious** | "Tell me about a time you learned something outside your comfort zone quickly." | Built LeaseI with zero prior LegalTech experience — ramped on LIHTC compliance law, OCR pipeline design, and LangGraph agentic architecture simultaneously | Strong |
| **Hire and Develop the Best** | "Tell me about a time you helped someone else grow." | Entrata: 300+ code reviews, 5+ engineers mentored — feedback that teaches reasoning, not just corrections | Strong |
| **Insist on the Highest Standards** | "Tell me about a time you raised the bar for quality." | AgentProbe: CI-integrated LLM-as-judge eval — "no manual QA" was the bar; blocking failing runs before production was the implementation | Strong |
| **Think Big** | "Tell me about a visionary idea you pursued." | LeaseI: Designed as a 3-surface platform from day one (Document Intelligence + Support Investigation + Tenant Self-Service) sharing one knowledge repo — bigger than the initial compliance checker requirement | Strong |
| **Bias for Action** | "Tell me about a time you moved fast with limited information." | Entrata: Microservices architecture redesign — made call to containerize with Docker under deadline; 50% scalability gain; 30% deployment reduction | Strong |
| **Frugality** | "Tell me about a time you accomplished more with fewer resources." | AgentProbe: 100% local deployment at zero cost using Ollama for low-stakes LLM tasks; multi-provider routing that picks cheapest capable provider | Strong |
| **Earn Trust** | "Tell me about a time you had to rebuild trust with a stakeholder." | Entrata: Compliance/Legal stakeholders initially skeptical of AI pipeline on financial records — earned trust through transparent audit logs, validation gates, and staged rollout | Partial — build this out |
| **Dive Deep** | "Tell me about a time you had to go unusually deep to solve a problem." | Entrata: 200+ SQL query optimization — execution plan analysis, index strategy, partitioning, not surface-level fixes | Strong |
| **Have Backbone; Disagree and Commit** | "Tell me about a time you disagreed with your manager or team." | **GAP** — build this story (see below) | None in bank |
| **Deliver Results** | "Tell me about a time you delivered a complex project under pressure." | Entrata: 120+ Agile sprints, 99.5% uptime, 20+ modules shipped for 100K+ MAU | Strong |
| **Strive to be Earth's Best Employer** | Less common in technical interviews — skip unless asked | — | — |
| **Success and Scale Bring Broad Responsibility** | "Tell me about a time you considered the broader impact of your work." | LeaseI HITL design: "I explicitly designed the tenant-facing surface so the AI can never resolve eligibility or configuration questions — not because it can't, but because those decisions affect housing security. The AI stays in the lane where it belongs." | Strong |

### GAP: Have Backbone; Disagree and Commit

You need a story here. Think about:
- **At Entrata:** Did you ever push back on a technical direction, sprint scope, or architectural decision? Even a smaller disagreement where you advocated for a different approach and either won the argument or committed after losing it.
- **At GMU:** Research methodology disagreement with faculty?
- **LeaseI:** Any design decision where you considered the simpler path and chose the harder right one?

**Draft prompt:** Think of a time someone (manager, peer, client) wanted to do X, you thought Y was better, you stated your case clearly, and then either: (a) they came around, or (b) they didn't but you committed fully anyway and it still went well. That's the story.

---

## Technical Prep Checklist

- [ ] **Amazon Bedrock basics** — why: role's primary delivery platform; interviewers will ask "how would you use Bedrock for this?" Study: model selection (Nova Lite vs Nova Pro vs Claude on Bedrock), Knowledge Bases, Agents for Bedrock, Guardrails
- [ ] **MCP (Model Context Protocol)** — why: JD calls out "MCP servers"; your LeaseI tool calling is adjacent but you should be able to say "I've studied the MCP spec; my AgentProbe tool-calling layer implements the same pattern"
- [ ] **Amazon Connect basics** — why: customer context; you'll be asked about the domain. Know: what Amazon Connect is (cloud contact center), Contact Flows, Amazon Lex integration, Connect's Unlimited AI tier, the 4 agentic AI solutions launched April 2026 (Connect Talent, etc.)
- [ ] **AWS Lambda / Step Functions** — why: JD lists serverless as preferred; study the basics so you can discuss the pattern even without hands-on experience
- [ ] **Amazon's 16 LP stories** — why: every round has LP questions; rehearse your "Disagree and Commit" story specifically — it's the one most interviewers probe hardest
- [ ] **LeaseI architecture walkthrough (5 min)** — why: will be asked "tell me your most complex AI system"; practice the 5-min version: problem → architecture decision → key trade-offs → results
- [ ] **RAG trade-offs (dense vs sparse, chunking strategies)** — why: core technical topic for AI SA roles; your TF-IDF vs ChromaDB decision is the story
- [ ] **Agentic AI failure modes** — why: Amazon interviewers always ask "what went wrong"; prepare 2–3 failure modes you've seen (hallucination, confidence miscalibration, inter-agent state corruption) with how you addressed them
- [ ] **System design: contact center AI end-to-end** — why: almost certain in the loop; practice the architecture from Connect → Bedrock → RAG KB → agent → escalation → human queue
- [ ] **Comp anchoring** — why: recruiter will ask; know the band ($153K–$207K base), know the Levels.fyi L6 SA total comp (~$280K), know your walk-away number

---

## Company Signals

### To the recruiter (Round 1 — Monday)
- **Volunteer**: Virginia-based (zero relocation), STEM OPT status + H-1B needed, immediate availability, why Amazon Connect specifically
- **Don't volunteer**: Amazon Connect domain gap, competing offers without leverage
- **Vocabulary**: "AIVT team", "production-ready", "Amazon Connect Unlimited AI", "Applied AI Velocity Team"
- **Red flags they screen for**: visa surprise, comp mismatch, "I don't know much about Amazon Connect"

### To hiring manager / technical panel
- **Lead with**: "agentic AI in production on regulated data" — that's your differentiator, not your AWS knowledge
- **Vocabulary Amazon uses**: "Customer Obsession", "Bias for Action", "working backwards", "two-pizza team", "bar raiser", "Tenets", "PRFAQ"
- **Sharp question to ask back**: *"Amazon Connect launched four agentic AI standalone solutions in April 2026 — what's the customer motion for adoption looking like in the first quarter? Where's the friction?"*
- **Second question**: *"How does the AIVT team measure success with a customer — is it time-to-production, adoption rate, or something else?"*

### To the Bar Raiser
- **Expect**: Deeper LP probes, edge-case pushback, "why Amazon over X competitor" — they're testing whether you can defend your reasoning under pressure
- **Don't**: Deflect or soften disagreements in your LP stories — the Bar Raiser wants to see you actually had conviction and held it
- **Do**: End every story with a concrete result + a specific reflection ("here's what I'd do differently")

### What NOT to repeat across rounds
- Don't tell the LeaseI story identically to every interviewer — vary the angle:
  - Recruiter: headline number (93.6% precision, 8 agents, production-grade)
  - HM: why you designed HITL the way you did (housing security impact)
  - Peer-tech: TF-IDF vs ChromaDB trade-off decision, eval pipeline design
  - Bar Raiser: what failed during development and what you changed

---

## Amazon Connect Domain Gap — How to Handle It

You will be asked this. Don't avoid it — own it and redirect:

> "I don't have Amazon Connect product experience — that's true. What I have is 8 years of building enterprise SaaS for complex regulated customer workflows at 100K+ MAU scale, and 2 years of building agentic AI that works in production. The customer problem Amazon Connect SA is solving — getting enterprise customers from POC to production with agentic AI — is exactly what I've been doing, just in a different domain. LeaseI is evidence of how fast I can ramp: I had zero LegalTech background and built a production-grade compliance AI system. Amazon Connect's features and APIs are learnable in weeks; the agentic AI architecture judgment that makes customers successful is what I bring from day one."

---

## Interview on Monday — Day-of Checklist

- [ ] Know the recruiter's name (from original outreach — Prarthana Kakkattukoiloth YogeshKumar)
- [ ] 60–90 sec intro ready: "production AI engineer, 8 years Entrata, LeaseI, want to go customer-facing"
- [ ] Comp range ready: "$160–190K base, L6 band"
- [ ] Visa question ready: ask early, confidently
- [ ] "Why Amazon Connect" answer ready (reference April 2026 agentic AI launch)
- [ ] One LP story on deck in case recruiter asks: **Deliver Results** (Entrata 120+ sprints, 99.5% uptime) — most common recruiter LP probe
- [ ] Ask at the end: "What does the rest of the process look like from here?"
