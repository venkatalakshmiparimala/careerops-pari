# Interview Intel: Capital One — Principal Data Analyst, BCP Field Strategy

**URL:** https://www.capitalonecareers.com (BCP Field Strategy — Principal DA)
**Legitimacy:** High Confidence
**Report:** [118](reports/118-capital-one-sr-da-retail-bank-2026-06-23.md) (nearest match — same DA track)
**Researched:** 2026-08-17
**Sources:** Glassdoor (Principal DA + BA interview reviews), Levels.fyi, InterviewQuery, IGotAnOffer, ResumeAdapter, Capital One Careers
**Audiences covered:** recruiter-screen, hiring-manager, peer-tech, panel-mixed (Power Day)

---

## Process Overview

- **Rounds:** 5 stages, ~3–6 weeks end-to-end
- **Format:** Application → Virtual Job Tryout (automated) → Recruiter Screen (30 min) → Mini Case Interview (30–45 min, 1 interviewer) → **Power Day** (4–6 hrs, 3–5 back-to-back rounds)
- **Power Day breakdown (DA track):** 2 case interviews + 1 take-home project defense/presentation + 1 behavioral round
- **Difficulty:** High — case rounds use larger/messier numbers than consulting cases; calculator allowed
- **Key context:** Capital One acquired Discover ($35.3B) in May 2025 → now largest US credit card issuer; commercial card economics and competitive positioning come up more frequently in cases
- **Sources:** [Glassdoor Principal DA](https://www.glassdoor.com/Interview/Capital-One-Principal-Data-Analyst-Interview-Questions-EI_IE3736.0,11_KO12,34.htm), [ResumeAdapter](https://www.resumeadapter.com/companies/capital-one/interview-process), [OphyAI](https://ophyai.com/blog/company-guides/capital-one-interview-guide)

---

## Audience Map

- **Stage 1** (Virtual Job Tryout, async, 20 min) → automated behavioral screen — not a real interview, just complete it
- **Stage 2** (Recruiter Screen, 30 min, phone) → `recruiter-screen`
- **Stage 3** (Mini Case, 30–45 min, 1 interviewer) → `peer-tech` — quantitative case, data analysis thinking
- **Stage 4** (Power Day, 4–6 hrs) → `panel-mixed`
  - Slot A: Case 1 — `peer-tech`
  - Slot B: Case 2 — `peer-tech`
  - Slot C: Take-home defense / presentation — `peer-tech` + `hiring-manager`
  - Slot D: Behavioral — `hiring-manager` or `panel-mixed`

---

## Round-by-Round Breakdown

### Stage 2: Recruiter Screen — audience: `recruiter-screen`
- **Duration:** 30 min
- **Conducted by:** Recruiter / Talent Acquisition
- **What they evaluate:** Fit gate — motivation, location/visa, comp range, timeline, why Capital One
- **Reported questions:**
  - "Walk me through your background." [Glassdoor]
  - "Why Capital One / why BCP?" [Glassdoor]
  - "What are your compensation expectations?" [Glassdoor]
  - "Are you authorized to work in the US? Will you require sponsorship?" [inferred from JD]
  - "Are you open to McLean, VA hybrid?" [inferred from JD]
- **What to prep:** Your 90-second narrative, comp anchor, visa script (see below)

---

### Stage 3: Mini Case Interview — audience: `peer-tech`
- **Duration:** 30–45 min
- **Conducted by:** Senior analyst or data scientist
- **What they evaluate:** Quantitative reasoning, structured problem-solving, business judgment
- **Format:** Interviewer-led; you're asked to walk through a data scenario or profitability question; calculator allowed
- **Reported question types:**
  - Commercial card profitability: "If we add 1,000 new SMB accounts, what's the expected P&L?" [Glassdoor — Capital One DA track]
  - "Given a dataset with X issues, what do you do first?" [inferred from JD / take-home]
  - Breakeven analysis on a field rep outreach campaign [inferred from BCP domain]
- **How to prep:** Practice the MECE structure below; quantify every assumption

---

### Stage 4: Power Day — audience: `panel-mixed`

#### Slot A/B: Case Interviews (×2)
- **Duration:** 30–45 min each
- **Format:** Quantitative business cases; large/messy numbers; calculator provided
- **Typical case types for BCP DA:**
  - Customer profitability / CLV analysis
  - A/B test interpretation ("lift was 26% — should we scale it?")
  - Fraud exposure quantification ("top 20 accounts at risk, $X total")
  - Rep performance diagnosis ("REP07 underperforms — is it luck or skill?")
- **Key pressure test:** They'll introduce a wrinkle mid-case — an imbalance, a missing variable, a conflicting signal. Your job is to catch it and adjust, not just barrel through.

#### Slot C: Take-Home Defense + Presentation (15–20 min)
- **Format:** Present your Jupyter notebook findings as a 12-slide executive deck to VP + 2 Principal DAs
- **They will pick 2 of the 8 questions and drill deep** — per the README:
  - "Walk me through your fraud score weighting — why 40/35/25?"
  - "Your A/B test lift was 26% — why don't I trust that number?"
  - "If the churn model has 78% recall, what does that mean for the 22% we miss?"
  - "Your regression shows REP07 is underperforming even after controlling for mix — what do you tell their manager?"
- **What they're really testing:** Whether you govern the analysis or just run it. Every decision needs a "why", not just a "what."

#### Slot D: Behavioral
- **Duration:** 30–45 min
- **Format:** STAR stories; may include a leadership case ("how would you prioritize if VP and CRO both want conflicting findings?")
- **Typical questions:**
  - "Tell me about a time you presented analysis that a stakeholder disagreed with." [Glassdoor]
  - "Describe your most complex data analysis project." [Glassdoor]
  - "Tell me about a time you found an error in someone else's analysis." [inferred — BCP domain = data quality governance]
  - "How do you handle conflicting priorities from two executives?" [inferred from VP + CRO dual-audience setup]

---

## Comp Reference

| Level | Capital One Title | Base | Total |
|-------|------------------|------|-------|
| Associate | Data Analyst | $109K–$121K | ~$121K |
| Senior Associate | Sr. Data Analyst | $117K–$133K | ~$124K |
| **Principal Associate** | **Principal Data Analyst** | **$131K–$150K** | **~$143K** |

**Your anchor:** "I'm targeting Principal Associate compensation — the $130K–$145K range based on Levels.fyi data for this level at Capital One. I'm flexible depending on total comp structure including RSUs."

**Sources:** [Levels.fyi Capital One](https://www.levels.fyi/companies/capital-one/salaries), [6figr Sr. DA](https://6figr.com/us/salary/capital-one--sr.-data-analyst)

---

## Audience Pack: `recruiter-screen`

### "Walk me through your background" (90 seconds)
> "I'm a software engineer and data analyst with 8 years of experience building production data systems — most of that at Entrata, a PropTech company serving 100K+ monthly active businesses, where I built the financial data infrastructure for affordable housing: income eligibility pipelines, compliance workflows, fraud detection, and the SQL layer that processed 1.6M+ HUD and Tax Credit records. I also earned my MS in Data Analytics Engineering at GMU last May — GPA 3.87 — where I did quantitative research across WHO and UK road safety datasets. The Capital One BCP role is a direct translation of what I've been building: field-rep performance analytics, spend trends across commercial accounts, campaign attribution. The domain shifts from apartments to commercial cards, but the underlying questions — who's at risk, where's the spend moving, which reps are outperforming their portfolio mix — are the same ones I've been answering for 8 years."

### "Why Capital One / why BCP?"
> "Capital One treats data as a competitive advantage in a sector where most institutions still treat it as compliance overhead. The Discover acquisition in particular means BCP is now operating at a scale where the field strategy analytics decisions have outsized impact — which rep gets which accounts, which campaigns scale, which customers need outreach before they churn. That's exactly the intersection of data governance, quantitative analysis, and business strategy I want to be in."

### Visa script
> "I'm on F-1 STEM OPT — 3 years of work authorization. Capital One has an established H-1B sponsorship track, which is why it's a priority for me. I'd be happy to walk through the timeline: my OPT runs through [check exact date], and H-1B cap registration would happen in spring 2027 for an October 2027 start — well within the OPT window."

### Location
- Role is McLean, VA hybrid → zero relocation cost (Virginia resident)
- Lead with: "I'm in Virginia — McLean is my backyard. Hybrid works perfectly."

### Timeline
- "Available immediately / [notice period if any]"

---

## Audience Pack: `hiring-manager`

### "Why this role, why now?"
> "The BCP Field Strategy team is solving a prioritization problem that every rep-based sales org struggles with: after the data shows REP07 is underperforming, is that luck of the draw on account mix or genuine underperformance? Most teams answer that with gut feel. I want to be the analyst who answers it with a regression that controls for territory, account size, and tenure — and then hands the manager a specific action: reassign these 5 accounts, coach on these 3 behaviors. That's the level of analysis I've been building for 8 years at Entrata, and the BCP role is where I can do it at Capital One scale."

### "What would your first 90 days look like?"
> "First 30 days: understand the data model — how accounts, reps, transactions, and campaigns are structured in the warehouse; what the existing dashboards track and where the known gaps are. First 60 days: audit the existing segmentation methodology — whether it's RFM-based or spend-tiered — and identify where it's losing signal. First 90 days: deliver one analysis that the VP of Field Strategy can act on for Q3 planning, with a specific recommendation and a projected dollar impact."

### Sharp questions to ask back
1. "The Discover acquisition makes Capital One the largest commercial card issuer — how is BCP Field Strategy thinking about the integration of Discover's small business card portfolio into the field rep allocation model?"
2. "The take-home project uses 18 months of data and 20 reps — what does the real production data environment look like, and what's the biggest gap between what the team can see today vs. what they wish they could see?"
3. "The dual-audience structure in the take-home — VP of Field Strategy + CRO — is that the actual stakeholder dynamic on the team, and how do those two priorities usually compete in practice?"

---

## Audience Pack: `peer-tech` (Power Day Slots A/B — Case Rounds)

### Capital One Case Framework

Every Capital One case follows this structure — practice until it's automatic:

```
1. CLARIFY — "Before I jump in, a few questions:"
   → What's the time frame? What's the decision this analysis informs?
   → What data do we have access to?

2. STRUCTURE — "Here's how I'd approach this:"
   → Lead with the business question, not the methodology
   → MECE: split the problem into 2-3 non-overlapping dimensions

3. HYPOTHESIS — "My working hypothesis is..."
   → State a directional view before looking at data
   → Shows you're a business analyst, not just a data runner

4. ANALYZE — Walk through the numbers clearly
   → Narrate every calculation: "so that's 26% lift on a $50K baseline, which is $13K per treated account"
   → Flag assumptions explicitly: "I'm assuming gross margin of 8% here — is that reasonable?"

5. FLAG THE WRINKLE — This is where you win or lose
   → Capital One always embeds a trap: pre-period imbalance, biased sample, confounding variable
   → If you don't catch it, you fail; if you catch and quantify it, you ace it

6. RECOMMEND — One decision, not "it depends"
   → "Given the pre-period imbalance, I'd adjust the lift estimate from 26% to approximately 15-18%, which still justifies Q3 scale-up — but I'd recommend a stratified re-run to confirm before committing the full budget."
```

### Likely case topics (BCP DA specific)

| Case type | What they're testing | Your best angle |
|-----------|---------------------|-----------------|
| CLV / profitability | Can you model long-term revenue, not just current spend? | Entrata CLV for housing portfolios; RFM × gross margin formula |
| A/B test lift | Do you catch the pre-period imbalance without prompting? | You caught it in the notebook — lead with this |
| Fraud exposure | Can you quantify a risk to a CFO? | Income fraud detection at Entrata; composite risk score from notebook |
| Rep attribution | Can you separate signal from noise in rep performance? | "Luck vs. skill" regression: controlling for account mix to find true alpha |
| Churn intervention | Which 30 accounts do you pick with a budget constraint? | Churn model from notebook; CLV-weighted prioritization |

### SQL questions (Capital One DA track tests SQL under time pressure)

Prepare these patterns — they may ask you to write live or pseudo-code:

```sql
-- 1. Velocity burst detection (production-ready, asked directly in take-home)
WITH hourly AS (
  SELECT account_id,
         DATE_TRUNC('hour', transaction_date) AS txn_hour,
         COUNT(*) AS txn_count
  FROM transactions
  WHERE transaction_date >= CURRENT_DATE - INTERVAL '90 days'
  GROUP BY account_id, DATE_TRUNC('hour', transaction_date)
)
SELECT account_id, txn_hour, txn_count
FROM hourly
WHERE txn_count >= 10
ORDER BY txn_count DESC;

-- 2. Rep quota attainment with account mix context
SELECT r.rep_id, r.rep_name, r.territory,
       r.quota_attainment_pct,
       r.pct_large_accounts,
       r.avg_account_tenure_months,
       r.quota_attainment_pct - AVG(r.quota_attainment_pct) OVER (PARTITION BY r.territory) AS vs_territory_avg
FROM field_reps r
ORDER BY quota_attainment_pct DESC;

-- 3. 30-day spend lift by channel
SELECT c.channel,
       COUNT(*) AS outreach_count,
       AVG(c.spend_lift_pct) AS avg_lift_pct,
       SUM(CASE WHEN c.converted = 1 THEN 1 ELSE 0 END)::FLOAT / COUNT(*) AS conversion_rate
FROM campaigns c
GROUP BY c.channel
ORDER BY avg_lift_pct DESC;

-- 4. Cohort retention (month 0 = acquisition month)
WITH cohort_base AS (
  SELECT account_id,
         DATE_TRUNC('month', acquisition_date) AS cohort_month,
         COUNT(DISTINCT account_id) OVER (PARTITION BY DATE_TRUNC('month', acquisition_date)) AS cohort_size
  FROM accounts
),
activity AS (
  SELECT a.account_id, cb.cohort_month,
         DATEDIFF('month', cb.cohort_month, DATE_TRUNC('month', t.transaction_date)) AS months_since_acq
  FROM transactions t
  JOIN cohort_base cb ON t.account_id = cb.account_id
  GROUP BY a.account_id, cb.cohort_month, months_since_acq
)
SELECT cohort_month, months_since_acq,
       COUNT(DISTINCT account_id)::FLOAT / MAX(cohort_size) AS retention_rate
FROM activity
GROUP BY cohort_month, months_since_acq
ORDER BY cohort_month, months_since_acq;
```

---

## Power Day Defense — What They'll Drill You On

These are the four questions listed in the README. Have tight answers rehearsed for all four.

### "Walk me through your fraud score weighting — why 40/35/25?"

> "The 40/35/25 weighting reflects signal reliability in the context of commercial card fraud. Velocity is weighted highest at 40% because it's the most operationally urgent — 10+ transactions in 60 minutes is a real-time signal that something's actively happening, not historical. Amount anomaly at 35% is high-reliability but slightly lower because z-score comparison depends on account history depth — new accounts with thin history can generate spurious anomalies. New merchant risk at 25% is the weakest signal in isolation — a first-time merchant might just be a new vendor — but it's meaningful when combined with the high-risk merchant flag. The composite is designed so no single signal alone breaches the review threshold; it takes multiple signals firing together. I'd want to validate this weighting against labeled fraud outcomes before putting it in production — but for a simulation, it reflects a reasonable prior on signal reliability."

### "Your A/B test lift was 26% — why don't I trust that number?"

> "You shouldn't — and I caught this in my analysis. The pre-period balance check showed Treatment accounts had a baseline spend of ~$49K vs. ~$32K for Control — statistically significant (t-test p=0.004). That's a 55% baseline difference. The groups weren't equivalent before the campaign ran. The headline 26% lift partially captures the fact that higher-spending accounts tend to spend more regardless of outreach — not just campaign effect. My adjusted estimate — controlling for the pre-period spend imbalance — brings the true lift closer to 15–18%. That still supports scaling In-Person outreach for Q3, but the investment case should be built on the adjusted number, not the raw one."

### "If the churn model has 78% recall, what does that mean for the 22% we miss?"

> "It means 22% of churned accounts won't appear on the outreach list — we call them false negatives. In the context of the budget constraint (top 30 accounts), I'd prioritize recall over precision because the cost of missing a high-CLV churning account is higher than the cost of reaching out to an account that would have stayed anyway. The 22% we miss are most likely accounts with less pronounced early warning signals — recent acquisition, thin transaction history, or accounts that churned abruptly without the gradual spend decline pattern the model learned. My recommendation: supplement the model's output with a rule-based flag for accounts that missed the model threshold but have had zero transactions in the last 30 days — that catches the 'sudden stop' pattern the model may underweight."

### "Your regression shows REP07 is underperforming even after controlling for mix — what do you tell their manager?"

> "I'd frame it carefully, because the regression tells you magnitude and direction, not cause. After controlling for territory, account size mix, and tenure, REP07's residual is negative — meaning they're underperforming compared to what their account portfolio would predict. That's the evidence. What I'd tell the manager: here's the controlled performance gap, here's how it compares to the bottom quartile, and here are the two hypotheses worth investigating — skill gap (which shows up as low campaigns_run combined with low conversion rate per campaign) vs. engagement gap (fewer touchpoints, lower activity on manageable accounts). The data narrows the question. The manager needs to have the conversation to find the answer."

---

## Story Bank Mapping

| # | Audience | Question / topic | Best story | Fit |
|---|----------|-----------------|------------|-----|
| 1 | recruiter-screen | "Tell me about your background" | Entrata: 40% deployment, 1.6M records, 100K+ MAU | Strong |
| 2 | recruiter-screen | "Why data analytics?" | GMU MS + Research Associate (R²=0.977) + Isolation Forest | Strong |
| 3 | hiring-manager | "Most complex analysis you've done" | LeaseI: 225-query eval harness, LLM-as-judge, regression gating | Partial — reframe as data infrastructure, not AI |
| 4 | hiring-manager | "How do you handle conflicting stakeholder priorities?" | Entrata: VP of Field vs CRO dual audience — use the take-home framing | **Gap — need new story** |
| 5 | hiring-manager | "Tell me about a time you found an error in analysis" | Entrata: PHI pipeline — 50%+ codebase had insecure data paths; I found and fixed them | Strong |
| 6 | peer-tech | "Describe a data quality audit you led" | Entrata: income limits import — 1.6M records, 8 issues found programmatically | Strong — maps directly to Q0 |
| 7 | peer-tech | "Tell me about a time you used statistics to make a business recommendation" | GMU Research Associate: regression on 190+ countries, R²=0.977, drove faculty strategy | Strong |
| 8 | peer-tech | "Fraud detection / anomaly" | Entrata: Isolation Forest across 3 research pipelines; income fraud detection in LIHTC | Strong |
| 9 | panel-mixed | "Tell me about a time you presented to executives" | Entrata/GMU: faculty leadership dashboards; 40% comprehension improvement | Partial — limited executive seniority |
| 10 | panel-mixed | "Tell me about a time your recommendation was rejected" | **Gap — need story** | |

### Gap stories to build

**Story needed #1: Conflicting stakeholder priorities**
> Basis from CV: "Collaborated cross-functionally with compliance, operations, and product stakeholders" at Entrata. Build a STAR+R story about a sprint where compliance needed a change that conflicted with a product manager's timeline — what you decided, how you communicated, what happened.

**Story needed #2: Recommendation that was rejected / overruled**
> Every analyst has this — likely from Entrata. Think: a time you recommended a technical approach, the team went a different direction, and what you learned. Build this before Power Day behavioral round.

---

## Technical Prep Checklist

- [ ] **RFM scoring formula** — practice recoding Q1 to match the README spec exactly: `rfm_score = R_score*100 + F_score*10 + M_score`, 5-tier system (Champions/Loyal/Promising/At Risk/Hibernating). Your current notebook uses a 3-tier simplified version — they may check if it matches the spec.
- [ ] **CLV formula** — `CLV = avg_monthly_spend × avg_remaining_tenure_months × 0.08` — know the 8% gross margin assumption and be ready to defend it or adjust it
- [ ] **A/B test statistics** — two-sample t-test, Mann-Whitney U, Cohen's d, 95% CI, power analysis — know when to use each; be able to explain p-value in plain English to a VP
- [ ] **Pre-period balance check** — you found it; rehearse the explanation (treatment mean $49K vs control $31K, p=0.004, what that means for the headline lift)
- [ ] **Fraud composite score** — know the 40/35/25 weighting rationale cold; have the adjusted normalization formula for each signal
- [ ] **Churn model ROC-AUC** — know what AUC means, what 78% recall implies, how to select the probability threshold for the top-30 shortlist
- [ ] **Regression residuals (rep attribution)** — explain in plain English: "a positive residual means this rep outperformed what their account mix would predict"
- [ ] **SQL: velocity burst detection** — write this from memory; they ask for a production-ready query in Q4 of the hard project
- [ ] **Cohort retention heatmap** — know how to interpret it: which cohort has the steepest drop at Month 3? that's when intervention timing matters
- [ ] **Executive deck structure** — every slide needs a single declarative headline with a number. "In-Person visits drive 18% adjusted lift vs. 5% for email — scale this in Q3" beats "Channel Comparison"

---

## Notebook Completion Checklist

Based on current notebook state (Q0 done, Q1 RFM in progress):

| Question | Status | Critical gap |
|----------|--------|-------------|
| Q0 — Data Quality | ✅ Done | Add dollar impact table for the deck (slide 2) |
| Q1 — RFM + CLV | In progress | Fix scoring to match README spec (R*100+F*10+M); add CLV; add 5-tier; profile by industry; compute total CLV at risk by tier |
| Q2 — Cohort Retention | Not started | Retention matrix + heatmap; answer: which cohort best/worst 12-month retention; when to intervene |
| Q3 — (not in hard project — merged into Q7) | — | — |
| Q4 — Fraud Detection | Not started | 3 signals; composite score 0-100; top 20 accounts; production SQL query |
| Q5 — Churn Prediction | Not started | Feature engineering from README; RF + LR; ROC curve; top 50 churn-risk; top 30 for budget constraint |
| Q6 — A/B Test | Not started | Balance check first (you have the code for this in the data quality section); both tests; effect size; power analysis; adjusted lift |
| Q7 — Field Rep Attribution | Not started | Raw league table; regression controlling for mix; residuals; coaching vs reassignment recommendation |
| Q8 — Executive Synthesis | Not started | One-page Q3 action plan; 4 initiatives, fully quantified; north-star metric |
| **Slide deck** | Not started | 12 slides; every slide = declarative headline + number; no charts without a business implication statement |

**Priority order to complete:** Q1 fix → Q6 (A/B test, you already have the balance check code) → Q4 (fraud) → Q2 (cohort) → Q5 (churn) → Q7 (reps) → Q8 (synthesis) → deck

---

## Company Signals

### What to say to the recruiter
- Lead with: Virginia resident (no relocation), hybrid works, H-1B timeline is clean
- Use: "Business Cards and Payments" (not just "BCP") — shows you know the division
- Avoid: mentioning you applied to multiple Capital One roles (DA, DS, BA) — just focus on this one
- Defer comp: "I'm targeting Principal Associate level — can you confirm the band before I give a number?"

### What to say to the hiring manager
- Use Capital One language: "data governance," "field strategy," "managed spend," "quota attainment"
- Reference: Discover acquisition — "the field rep network just got significantly larger"
- Avoid: over-indexing on AI/ML; this role is applied analytics for a business team, not research
- Sharp question: Ask about the Q3 planning timeline and where the team is right now — shows you understand the urgency behind the take-home

### What to say to peer-tech interviewers
- Lead with data quality story from Q0 — you found all 8 issues programmatically before touching any analysis. This is exactly what Principal-level data governance looks like.
- Show your reasoning, not just your code: "I chose to keep velocity burst flags and not delete them because they represent legitimate fraud signals — removing them would lose the investigability the CRO needs"
- Ask: "What's the biggest data quality challenge the team deals with in production?" — shows you think beyond the take-home

### What NOT to repeat verbatim across slots
- The A/B test pre-period imbalance story — lead with it in Slot C (defense), don't repeat it identically in behavioral; give it a different angle (e.g., "a time I pushed back on a headline number")
- The Entrata scale numbers ($1.6M records, 100K+ MAU) — vary the emphasis: recruiter hears the scope, HM hears the governance, peer-tech hears the technical architecture

---

*Sources:*
- [Capital One Principal DA Interview — Glassdoor](https://www.glassdoor.com/Interview/Capital-One-Principal-Data-Analyst-Interview-Questions-EI_IE3736.0,11_KO12,34.htm)
- [Capital One Interview Process 2026 — ResumeAdapter](https://www.resumeadapter.com/companies/capital-one/interview-process)
- [Capital One Case Interview Guide — IGotAnOffer](https://igotanoffer.com/blogs/mckinsey-case-interview-blog/capital-one-case-interview)
- [Capital One DA Interview Guide — InterviewQuery](https://www.interviewquery.com/guides/capital-one-data-analyst)
- [Capital One Salaries — Levels.fyi](https://www.levels.fyi/companies/capital-one/salaries)
- [Capital One Sr. DA Salary — 6figr](https://6figr.com/us/salary/capital-one--sr.-data-analyst)
