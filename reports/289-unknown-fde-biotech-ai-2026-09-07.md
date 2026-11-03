# 289 — Unknown Company — Forward Deployed AI Engineer (Biotech/Pharma AI)

**Date:** 2026-09-07
**Score:** 3.3/5 — Borderline (FDE archetype = primary target ✓; Python, AWS, Docker, APIs, AI model integration all covered; Kubernetes required but not in background; pharma/biotech domain desirable not required; no company name disclosed)
**URL:** Unknown — not provided
**PDF:** ✅ `output/289-unknown-fde-biotech-ai-2026-09-07.pdf`
**Legitimacy:** Medium Confidence — Company not named, but JD is highly specific (generative biology platform, protein engineering, drug discovery, pharma/biotech customers); far more credible than #288; likely a stealth-mode biotech AI startup or a company cautiously recruiting

---

## Block A — CV Match

**FDE-specific skills are strong across the board. Kubernetes is the one required gap. Pharma/biotech domain is desirable only — not required. Python, AWS, Docker, CI/CD, API integration, customer-facing deployment, and open-source AI systems all map directly.**

| JD Requirement | CV Proof Point |
|---------------|----------------|
| "Strong academic background in CS, ML, AI or quantitative discipline" | B.Tech CS + M.S. Data Analytics Engineering (GPA 3.87, GMU) ✓ |
| "Experience building systems that interact with large AI models through APIs" | AgentProbe: multi-provider LLM routing (Anthropic, OpenAI, Ollama) via standardized API layer — built to interact with LLMs at scale ✓✓ |
| "Hands-on experience designing, deploying, maintaining infrastructure for large-scale model serving" | AgentProbe: 15-endpoint FastAPI service, CI-integrated regression gate, multi-provider cost optimization; LeaseI: 8-agent LangGraph production deployment ✓/⚠️ (model user, not model server at petabyte scale) |
| "Experience deploying AI solutions for external customers" | Magizhs: agentic AI system concept-to-production, delivered to paying client; Entrata: customer-facing production software for 100K+ housing units ✓ |
| "Translating complex technical concepts for technical and non-technical stakeholders" | 120+ Agile sprints at Entrata with product/compliance/operations; Magizhs: stakeholder scoping → delivery; GMU: mentored 600+ students ✓ |
| "Strong knowledge of AWS; exposure to Azure or GCP" | AWS S3, EC2, RDS, Glue (production at Entrata) ✓✓ |
| "Docker, Kubernetes, CI/CD pipelines, cloud-native architectures" | Docker microservices (50% scalability improvement); GitHub Actions CI/CD; cloud-native AWS deployments ✓ / Kubernetes ✗ |
| "Communication and collaboration across technical and business teams" | Cross-functional delivery at Entrata, Magizhs, GMU — multi-stakeholder environments ✓ |
| "Proactive, adaptable mindset — manage multiple customer engagements" | Solo builds under ambiguity; Magizhs: ambiguous requirements → production in weeks ✓ |
| Computational biology, protein design, generative AI research (desirable) | NLP/BERT/spaCy in background; no computational biology or protein engineering ✗ (desirable only) |
| "Contributions to open-source software or production AI systems" (desirable) | AgentProbe: open-source LLM evaluation platform (GitHub); LeaseI: production AI platform ✓✓ |
| "Secure, reliable enterprise software meeting production requirements" (desirable) | Entrata: 99.5% uptime, PHI compliance, Libsodium encryption, zero security incidents 7yr ✓✓ |
| "Pharmaceutical or biotechnology environments, data governance, regulatory" (desirable) | Not in background; no pharma/biotech or drug discovery experience ✗ |

**Gaps:**
- **Kubernetes** — explicitly required; Docker is present and K8s concepts are adjacent (container orchestration), but K8s is a distinct system with its own operations model; will be probed in technical screening
- **Computational biology / protein design / pharma domain** — desirable but not required; none of the background is in life sciences; this will come up in customer conversations if hired
- **Large-scale model serving infrastructure** — AgentProbe is multi-provider routing + eval; the JD implies GPU cluster / inference serving at pharma scale; different magnitude

**ATS baseline:** ~15/20. Python ✓, AWS ✓, Docker ✓, CI/CD ✓, APIs ✓, AI model integration ✓, customer deployment ✓, open-source ✓. Kubernetes and computational biology missing.

---

## Block B — North Star Alignment

**FDE = primary target archetype per strategy.** "Forward Deployed Engineer" is literally the job title. This is the closest match to the target archetype in this session's pipeline.

The role combines everything that defines the FDE target: customer-facing technical deployment, bridging engineering and product, full lifecycle ownership from discovery to production, and translating complex AI capabilities into working customer environments. The "voice of the customer → internal product feedback" loop is exactly the high-leverage position that makes FDE roles valuable.

The pharma/biotech domain is a learning curve, but it's desirable not required — the JD makes this explicit. Python, AWS, Docker, CI/CD, and production AI systems are the core technical bar, and those are all covered.

**Compared to recent pipeline:** Higher FDE archetype alignment than EliseAI (#281-283, which are product engineering) or Airbnb (#284-286, which are platform engineering). Closest FDE match since the strategy pivot.

**Score: 3.5/5** (FDE archetype ✓; K8s gap and no company name drag from higher)

---

## Block C — Compensation

**Undisclosed.** "Competitive compensation and benefits package." San Francisco hybrid context — for a Forward Deployed AI Engineer at a biotech AI startup in SF, estimated $150K–$220K base + equity. Private health insurance and retirement mentioned but not quantified. No salary range given.

**Score: 2.5/5**

---

## Block D — Cultural Signals

- FDE culture: "bridge between AI models and customers" — customer-focused, high-ownership ✓
- "Curious, mission-driven individuals excited by ambitious technical challenges" ✓
- Computational biology / life sciences mission — drug discovery is high-impact domain ✓
- Hybrid SF — relocation required; user open to any US location ✓
- "Opportunities for travel and international collaboration" — aligns with FDE customer-travel model ✓
- Multi-location team — distributed engineering culture ✓
- H-1B: biotech AI startup in SF, likely VC-backed — typically sponsors; unconfirmed
- Company anonymous — stealth mode or cautious recruiting; adds uncertainty ⚠️

**Score: 3.5/5**

---

## Block E — Red Flags

1. **Kubernetes required** — explicitly listed; Docker is present but K8s is a distinct operational system; will be a concrete technical screening question with no strong answer from current background
2. **No company name** — second anonymous posting today; more credible than #288 but still a concern; cannot verify funding, H-1B history, or team legitimacy
3. **Pharma/biotech domain** — desirable but zero background; customer conversations will involve drug discovery, protein engineering, scientific workflows; harder to fake domain fluency in customer-facing FDE role than in an internal engineering role
4. **Comp undisclosed** — SF cost of living + FDE role = should be strong; no signal to confirm
5. **H-1B unconfirmed** — anonymous company; cannot verify sponsorship history

**Adjustment: −0.4**

---

## Block F — Global Score

| Factor | Signal |
|--------|--------|
| CV match | 3.5 — FDE deployment skills ✓✓; Python ✓✓; AWS ✓✓; Docker ✓✓; AI model APIs ✓✓; CI/CD ✓✓; open-source (AgentProbe) ✓✓; customer deployment ✓; K8s gap; pharma domain absent |
| North Star | 3.5 — FDE = primary target archetype; Python-primary ✓; customer-facing ✓; no formal leveling hard block; K8s gap and domain drag |
| Comp | 2.5 — undisclosed; SF FDE estimated $150K–$220K; no range signal |
| Culture | 3.5 — FDE mission ✓; life sciences impact ✓; hybrid SF ✓; travel ✓; anonymous company ⚠️ |
| Red flags | −0.4 — K8s gap; no company; pharma domain; H-1B unconfirmed |

**Global: 3.3/5 — Borderline**

> This is the best FDE archetype match in this session's pipeline. The role title, responsibilities, and customer-facing technical deployment model all map directly to the primary target archetype. Python, AWS, Docker, CI/CD, AI model integration, and open-source production AI systems are all covered. The two blockers: (1) Kubernetes is listed as a required skill and will come up in technical screening — it's the most learnable gap in the role, but "I have Docker experience and am learning K8s" is a weaker answer than "here are the K8s clusters I've managed"; (2) the pharma/biotech customer domain means every customer conversation will involve drug discovery workflows you haven't touched. If you want to push this, the CV should lean hard on AgentProbe (open-source AI platform, multi-provider, CI regression gate) and Magizhs (customer-facing agentic deployment) as the FDE proof points, with Entrata's enterprise production standards as the reliability angle.

---

## Block G — Posting Legitimacy

**Medium Confidence.** Company anonymous, but the JD is detailed, domain-specific, and internally consistent (generative biology platform, pharma/biotech customers, protein engineering). Not a template. Likely a stealth-mode biotech AI startup or a company that omits its name to manage inbound volume. If you can identify the source (job board URL, recruiter name, LinkedIn post), bring it back for legitimacy verification.

---

## Machine Summary

```yaml
company: Unknown (Biotech AI / Generative Biology Platform)
role: Forward Deployed AI Engineer
score: 3.3
status: Evaluated
date: 2026-09-07
salary_low: null
salary_high: null
location: San Francisco, CA (hybrid; relocation required)
remote: false
visa: unconfirmed (SF biotech AI startup, likely VC-backed — probably sponsors)
proptech_boost: false
h1b_status: unconfirmed
top_match: FDE primary target archetype; Python; AWS; Docker; AI model API integration; CI/CD; AgentProbe open-source; customer-facing deployment (Magizhs)
gaps: Kubernetes required (Docker present but K8s distinct); pharma/biotech domain absent; no company disclosed; comp undisclosed
```
