# SilverTrust — Project 4 | Deliverable 8
## Revised Proposal — ContractOS v1.1
**Oracle Game Studio | Daria Bystrova & Julian Granados**

---

## What Changed and Why

This revised proposal incorporates seven change requests raised by Oracle Game Studio during the Tuesday pitch Q&A. The core ContractOS architecture — five agents, human-in-the-loop, EU AI Act compliance, LangSmith monitoring — is unchanged and was approved without objection.

| CR | Change request | Response in this proposal |
|---|---|---|
| CR-01 | EOR coverage per country | New section 3.1 — EOR flag in Agent 4 |
| CR-02 | Social registration automation | New section 3.2 — Phase 2 scope |
| CR-03 | Contract generation workflow | New section 3.3 — Agent 6 proposal |
| CR-04 | PO matching for Agent 2 | Section 4 — Agent 2 enhancement |
| CR-05 | Local accounting rules in Agent 2 | Section 4 — Agent 2 enhancement |
| CR-06 | Intermediary cost tracking | Section 4 — Agent 2 + Agent 5 enhancement |
| CR-07 | Multilingual QA plan | Section 5 — implementation plan |

---

## 1. Original Solution — Unchanged and Approved

ContractOS v1.0 with five agents remains the approved foundation:

| Agent | Capability | Status |
|---|---|---|
| Agent 1 — Contract Intelligence Agent | Reads contracts, extracts structured JSON fields | ✅ Approved |
| Agent 2 — Invoice Validation Agent | Validates invoices vs contract terms | ✅ Approved — enhanced in this proposal |
| Agent 3 — Overlap Detection Agent | Detects duplicate contractor/employee scope | ✅ Approved |
| Agent 4 — Compliance Flagging Agent | Red/Amber/Green per contract, 5 jurisdictions | ✅ Approved — enhanced in this proposal |
| Agent 5 — Cost Categorisation Agent | Live burn dashboard by country/type/team | ✅ Approved — enhanced in this proposal |

**Critical constraint unchanged:** Human approves every flag before any payment is sent or any contractor is reclassified. This is technically enforced, not just policy.

---

## 2. What the Client Confirmed They Want First

When asked *"if we give you this tool next week, what would you implement first?"* the client identified:

1. Invoice processing visibility per country — who is paying what, through what intermediary
2. Social registration automation per country
3. Contract generation to minimise paperwork
4. Full process automation up to the human signature step

This confirms that **cost visibility and payment compliance** are the immediate priority, and **contract lifecycle automation** is the medium-term goal.

---

## 3. New Capabilities — Proposed Extensions

### 3.1 EOR Coverage in Agent 4 (Phase 1 — immediate)

**What the client asked:** Oracle operates in Russia, India, Pakistan, Bangladesh, and Philippines with no legal entity. They need visibility over what it means to employ workers there — government onboarding fees, EOR provider costs, and compliance obligations per country.

**What we propose:** Extend Agent 4 (Compliance Flagging) to include an Employer of Record flag:

- For each contractor in a country where Oracle has no legal entity, Agent 4 flags: *"No Oracle entity in [country] — EOR arrangement required"*
- The flag includes: estimated EOR provider cost range, key government registration requirements, and a recommended action (engage EOR provider / engage local counsel)
- Agent 5 (Cost Categorisation) tracks EOR fees as a named cost category alongside direct and intermediary costs

**Why this stays within scope:** EOR flag = information surfacing, not legal advice. The flag tells Oracle *where to look*, not *what to decide*. Human + legal review mandatory before any action.

**Jurisdictions covered in v1.1:** India (DPDP Act 2023), Philippines (DPA 2012), Pakistan (partial), Bangladesh (partial). Russia remains out of scope v1 due to sanctions and data localisation complexity.

---

### 3.2 Social Registration Automation (Phase 2 — post go-live)

**What the client asked:** When Oracle onboards a new worker in a country, the social security and insurance registration process should be automated — triggered by the contract event, executed without manual intervention up to the point where a signature or official filing is required.

**What we propose:** Research and scope a Phase 2 capability:

- Trigger: new contract created for a worker in a target country
- Agent (new — Agent 6 candidate): pulls country-specific social registration requirements, pre-fills registration forms, routes to HR for review and submission
- Scope boundary: agent prepares and routes; a named human submits to government bodies
- Compliance constraint: each country's social registration process must be individually validated by local counsel before automation

**Pre-conditions before Phase 2 can begin:**
- [ ] Legal review of automation feasibility per jurisdiction (India, Philippines, Pakistan, Bangladesh)
- [ ] Identification of official registration APIs or portals per country
- [ ] SilverTrust compliance framework research — to be completed offline

**Timeline:** Phase 2 scoping to begin after Phase 1 (v1.1) go-live and stabilisation.

---

### 3.3 Contract Generation Workflow (Phase 2 — post go-live)

**What the client asked:** Automate all steps in the contract creation process up to the point of human signature. No manual paperwork, no language barriers, no need to hire external firms for translation or legal drafting.

**What we propose:**

**Phase 2a — Contract template generation:**
- New workflow triggered by HR when a new worker is being onboarded
- Agent collects: worker name, role, country, contract type, rate, start date
- LLM generates a contract draft using a jurisdiction-specific template
- Output: draft contract in the local language + English, routed to HR for review

**Phase 2b — Template approval and reuse:**
- First contract for each country/role combination is reviewed by a lawyer
- Approved templates stored in a template register
- Subsequent contracts of the same type auto-generated from the approved template with variable fields substituted
- Human review still required before signature — not negotiable

**Constraint accepted by client:** Auto-signing is out of scope. Human signature is always required. Team correctly pushed back on this during the pitch and the client accepted.

**Language coverage:** English, Russian, Hindi, Urdu, Filipino, Bengali — iterative quality validation required (see section 5).

---

## 4. Agent Enhancements — v1.1 Scope

### Agent 2 — Invoice Validation Agent (Enhanced)

**Current capability:** Compares invoice against contract terms — amount, currency, scope, billing period.

**CR-04 addition — PO matching:**
- Agent 2 now also compares incoming invoice against the associated Purchase Order (PO) if one exists
- Flags three-way mismatches: invoice vs contract vs PO
- If no PO exists, flag is raised: *"No PO found for this invoice — recommend PO process be established"*

**CR-05 addition — Local accounting rules:**
- Agent 2 checks invoice against jurisdiction-specific accounting thresholds
- Flags if invoice amount exceeds local capitalisation threshold or triggers a different accounting treatment (e.g. investment vs operational cost classification)
- Covers Germany, India, Philippines in v1.1 — other jurisdictions added iteratively

**CR-06 addition — Intermediary cost tracking:**
- Agent 2 identifies and flags intermediary fees (staffing agencies, EOR providers, government onboarding fees) within invoice line items
- Tags them as *adjacent costs* linked to the primary contract
- Output includes: direct cost, intermediary cost, total cost — all three visible in the approval queue

---

### Agent 5 — Cost Categorisation Agent (Enhanced)

**CR-06 addition:**
- New cost category: `intermediary` — distinct from `contractor` and `FTE`
- Subcategories: `staffing_agency`, `eor_provider`, `government_fee`, `legal_counsel`
- Dashboard updated: burn view now shows direct vs intermediary split per country
- Alert threshold: if intermediary costs exceed 30% of total country spend, flag for Thibaud's review

---

## 5. Multilingual Quality Assurance Plan (CR-07)

**What the client asked:** Formal confirmation that Agent 1 can reliably process documents in all operating languages at consistent quality.

**Target languages:** Russian, Hindi, Urdu, Filipino (Tagalog), Bengali, English, German

**Our approach:**

| Phase | What happens | Acceptance criterion |
|---|---|---|
| Phase 0 — Baseline | Run Agent 1 on 5 test contracts per language, manually verify extraction | ≥90% field accuracy per language |
| Phase 1 — Iteration | Refine extraction prompts per language based on errors | ≥95% field accuracy |
| Phase 2 — Production | Monitor extraction confidence scores in LangSmith | Alert if confidence < 0.80 on any critical field |
| Ongoing | Quarterly prompt review per language as LLM models update | Maintain ≥95% accuracy |

**Confidence:** LLM training data coverage is strong for all target languages — particularly English, Russian, and Hindi. Filipino and Bengali may require additional prompt tuning in Phase 1.

**What we will not promise:** Perfect extraction on heavily degraded scans, handwritten documents, or highly non-standard contract formats. These require a separate OCR pre-processing step.

---

## 6. What Does Not Change

The following elements of ContractOS v1.0 are confirmed unchanged in v1.1:

- Five-agent core architecture
- Human-in-the-loop gate — technically enforced, not policy
- EU AI Act classification: Minimal/Limited risk
- GDPR lawful basis: 3 bases documented, 3 LIAs completed
- LangSmith observability: `contractos-oracle-prod` live
- Tech stack: n8n · LangChain · LangGraph · LangSmith
- EU-hosted infrastructure — all personal data stays EU-side
- Auto-signing out of scope — human signature always required

---

## 7. Revised Scope Summary

| Capability | Phase | Priority |
|---|---|---|
| Five-agent core (Agents 1–5) | v1.0 — delivered | ✅ Done |
| EOR flagging in Agent 4 | v1.1 — immediate | 🔴 High |
| Intermediary cost tracking in Agent 2 + Agent 5 | v1.1 — immediate | 🔴 High |
| PO matching in Agent 2 | v1.1 — immediate | 🔴 High |
| Local accounting rules in Agent 2 | v1.1 | 🟡 Medium |
| Multilingual QA plan | v1.1 — implementation | 🟡 Medium |
| Social registration automation | Phase 2 — post go-live | 🟢 Future |
| Contract generation workflow | Phase 2 — post go-live | 🟢 Future |
| Full document signing automation | Out of scope | ❌ Rejected |

---

## 8. Change Log

| # | What changed | Why | From | To |
|---|---|---|---|---|
| 1 | Agent 4 extended with EOR flag | CR-01 — client has no entities in 5 countries | Compliance flagging only | Compliance + EOR coverage |
| 2 | Agent 2 extended with PO matching | CR-04 — client uses POs alongside contracts | Contract-only validation | Contract + PO validation |
| 3 | Agent 2 extended with local accounting rules | CR-05 — jurisdiction-specific thresholds | No accounting rules | Germany + India + Philippines in v1.1 |
| 4 | Agent 2 + Agent 5 — intermediary cost tracking | CR-06 — client paying agencies + EOR fees | Not tracked separately | Named cost category with subcategories |
| 5 | Social registration automation scoped | CR-02 — reduces manual footwork | Not in scope | Phase 2 — pending legal research |
| 6 | Contract generation workflow scoped | CR-03 — client wants full pre-signature automation | Not in scope | Phase 2 — pending compliance research |
| 7 | Multilingual QA plan formalised | CR-07 — client challenged translation quality | Informal confidence | Formal 3-phase QA plan with acceptance criteria |

---

*Daria Bystrova & Julian Granados — SilverTrust Project 4 — Deliverable 8: Revised Proposal*
