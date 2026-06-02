# SilverTrust — Project 4 | Deliverable 9
## Change Log — ContractOS v1.0 → v1.1
**Oracle Game Studio | Daria Bystrova & Julian Granados**

---

## How to Read This Log

Each row maps one review board change request to the action taken, the reasoning, and where in the revised solution it is visible. Where we pushed back, we explain why.

| Column | What it means |
|---|---|
| CR # | Change request number from the peer approval record |
| Requested | What the review board (acting as Oracle) asked for |
| Action taken | What we did — accepted, scoped, or pushed back |
| Reasoning | Why we responded this way |
| Where to find it | File or slide that shows the change |

---

## Change Log Table

| CR # | Requested by review board | Action taken | Reasoning | Where to find it |
|---|---|---|---|---|
| **CR-01** | EOR coverage — flag contracts in countries where Oracle has no legal entity (Russia, India, Pakistan, Bangladesh, Philippines). Include government onboarding fees and compliance obligations. | ✅ **Accepted — implemented in Agent 4** | Legitimate and immediate risk. Oracle is already paying workers in 5 countries without entities. Without this flag, ContractOS is incomplete. Added EOR flag output to Agent 4: flag triggered when no Oracle entity found in contractor's country. Agent 5 tracks EOR fees as a named cost subcategory. Russia remains out of scope v1 due to sanctions. | `08_revised_proposal.md` §3.1 · Deck slide 15 |
| **CR-02** | Social security and insurance registration automation per country — triggered by new contract event. | ✅ **Accepted — scoped as Phase 2** | The request is valid and technically feasible. However, per-jurisdiction legal validation is required before any automation — we cannot responsibly automate government filings without confirming the legal framework per country. Scoped as Phase 2 with pre-conditions: legal review per jurisdiction, identification of official APIs or portals, SilverTrust compliance research. | `08_revised_proposal.md` §3.2 · Deck slide 16 |
| **CR-03** | Contract generation workflow — automate all steps in contract creation up to (but not including) human signature. Remove language barriers, paperwork, and need for external translation firms. | ✅ **Accepted — scoped as Phase 2, with one push-back** | Full process automation to the signature step is valid and feasible. Pushed back on one element: auto-signing. We advised strongly against automated signatures on legal contracts, particularly across multi-jurisdictional employment law. Client accepted this. Phase 2a: contract draft generation from HR data using jurisdiction templates. Phase 2b: approved template reuse. Human review required for all first-use templates per country. | `08_revised_proposal.md` §3.3 · Deck slide 16 |
| **CR-04** | PO matching for Agent 2 — compare invoices against Purchase Orders in addition to contracts. | ✅ **Accepted — implemented in Agent 2** | Straightforward extension. Oracle likely issues POs for contractor work; comparing invoice against both contract and PO is standard three-way match in procurement. If no PO exists for an invoice, Agent 2 raises an additional flag recommending Oracle establish a PO process. Covered: Germany, India, Philippines in v1.1. | `08_revised_proposal.md` §4 · Deck slide 15 |
| **CR-05** | Local accounting rules in Agent 2 — jurisdiction-specific thresholds, cutback classifications, and accounting law compliance per country. | ✅ **Accepted — implemented in Agent 2** | Valid request. Different countries have different capitalisation thresholds — an invoice that is an operational cost in Germany may be a capital expenditure in India. Agent 2 now flags where an invoice amount crosses local accounting thresholds and outputs the relevant accounting treatment. Iterative: v1.1 covers Germany, India, Philippines. Other jurisdictions added per-sprint. | `08_revised_proposal.md` §4 · Deck slide 15 |
| **CR-06** | Intermediary cost tracking — track agency fees, EOR provider costs, and government onboarding fees as adjacent costs per contract in Agent 2 and Agent 5. | ✅ **Accepted — implemented in Agent 2 + Agent 5** | This was the most immediately actionable request. Oracle is already paying 47% of monthly burn through intermediaries with no visibility. Agent 2 now identifies and tags intermediary line items in invoices. Agent 5 has a new cost category `intermediary` with four subcategories: `staffing_agency`, `eor_provider`, `government_fee`, `legal_counsel`. Alert triggered if intermediary costs exceed 30% of country spend. | `08_revised_proposal.md` §4 · Deck slide 15 · `agent5_spend_visualiser.py` |
| **CR-07** | Multilingual quality assurance — formal confirmation that Agent 1 can process documents in all operating languages at consistent quality. | ✅ **Accepted — formalised as 3-phase QA plan** | Client challenged this directly during the pitch. We had given an informal confidence statement ("LLM training data is adequate"). That was not enough. Replaced with a formal 3-phase QA plan: Phase 0 baseline testing per language (≥90% accuracy), Phase 1 prompt refinement (≥95% accuracy), Phase 2 production monitoring via LangSmith confidence alerts. 7 languages covered. One honest caveat retained: heavily degraded scans and handwritten documents require OCR pre-processing — we do not promise 100% accuracy on these. | `08_revised_proposal.md` §5 · Deck slide 17 |

---

## Push-Backs — What We Did Not Accept and Why

| What was suggested | Our response | Reasoning |
|---|---|---|
| Auto-signing of contracts | ❌ **Rejected** | Automated signing of employment contracts across 5+ jurisdictions without human review creates unacceptable legal risk. A signed contract that was never reviewed by a qualified person could be challenged as invalid. We advised the client to always have human sign-off, at minimum for first-use templates per country. Client accepted this position. |
| Full replacement of lawyers | ❌ **Not in scope** | Client pushed for agents that could give legally binding advice per jurisdiction. We clarified clearly: ContractOS gives Oracle a lantern to illuminate where to look, not a legal opinion. The compliance flagging agent tells Oracle which contracts have red flags and where the risk is — a lawyer decides what to do about it. This boundary protects both Oracle and SilverTrust from liability. |

---

## What Changed in the Compliance Position

The revised proposal introduced one material change to the compliance position:

| Area | v1.0 position | v1.1 position | Why it changed |
|---|---|---|---|
| EOR flagging | Not addressed | Agent 4 flags EOR requirement per jurisdiction | CR-01 — Oracle has no entities in 5 operating countries; ignoring this was a gap |
| Intermediary cost GDPR | Not explicitly addressed | EOR and agency fees tracked as adjacent data — same lawful basis as contract data (Art. 6(1)(b)) | CR-06 — new data category introduced |
| Multilingual processing | Stated informally | Formalised with 3-phase QA plan and explicit caveat on OCR | CR-07 — quality assurance is a compliance requirement, not just a technical nicety |
| Social registration (Phase 2) | Not in scope | Scoped as Phase 2 — pre-condition: legal review per jurisdiction | CR-02 — automation of government filings requires jurisdiction-specific legal validation before deployment |

**Nothing in the EU AI Act classification changed.** The addition of EOR flagging and multilingual processing does not move ContractOS above Limited Risk because all outputs still go to a named human before any action is taken.

---

## What We Would Do Differently in a Real Engagement

1. **EOR coverage should have been in v1.0.** Oracle told us in the discovery interview they operate in countries without entities. We identified the pain but did not connect it to an EOR requirement in our initial solution design. A real engagement would have caught this.

2. **Multilingual QA needs a formal plan from day one.** We stated confidence informally during the pitch. A review board (or a real client) will always ask for evidence. The 3-phase plan should have been in the original proposal.

3. **Intermediary cost tracking should have been in the original Agent 5 scope.** The LangSmith demo showed 47% of Oracle's burn going through intermediaries. That number was available from day one — it should have been a named capability, not a change request.

---

*Daria Bystrova & Julian Granados — SilverTrust Project 4 — Deliverable 9: Change Log*
