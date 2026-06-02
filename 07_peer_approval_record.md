# SilverTrust — Project 4 | Deliverable 7
## Peer Approval Record
**ContractOS for Oracle Game Studio | Daria Bystrova & Julian Granados**

---

## 1. Pitch Details

| Field | Detail |
|---|---|
| **Date** | Week 7 — Tuesday afternoon |
| **Presenting team** | SilverTrust — Daria Bystrova & Julian Granados |
| **Client scenario** | Oracle Game Studio (assigned by paired team) |
| **Review board** | Paired team acting as Oracle Game Studio |
| **Pitch duration** | ~15 minutes + Q&A |

---

## 2. What Was Presented

**Solution pitched:** ContractOS — AI-powered contract and payroll intelligence layer with five agents:

| Agent | Capability |
|---|---|
| Agent 1 — Contract Intelligence Agent | Reads and extracts structured data from contracts |
| Agent 2 — Invoice Validation Agent | Validates invoices against contract terms |
| Agent 3 — Overlap Detection Agent | Detects duplicate contractor/employee scope |
| Agent 4 — Compliance Flagging Agent | Red/Amber/Green per contract, 5 jurisdictions |
| Agent 5 — Cost Categorisation Agent | Live burn dashboard by country/type/team |

**Key points made during pitch:**
- Revenue side is structurally fixed — only cost can be addressed
- Human-in-the-loop enforced before any payment or reclassification
- EU AI Act: Minimal/Limited risk — justified through human review gate
- GDPR: 3 lawful bases, 3 LIAs completed, data stays EU-side
- LangSmith live: 6 runs traced, all 5 agents visible, PII redacted

---

## 3. Review Board Decision

**Decision:** ✅ Approved with change requests

The review board approved the ContractOS concept and architecture. Approval was conditional on addressing the change requests listed in section 4 below, to be incorporated into the Wednesday revised proposal.

---

## 4. Change Requests from Review Board (Client Feedback)

The following requests were raised during the Q&A session by Eugen (CEO/CTO):

### CR-01 — Employer of Record (EOR) Coverage
**Request:** Oracle operates in Russia, India, Pakistan, Bangladesh, and Philippines with no legal entity set up in those countries. Client needs ContractOS to flag and handle the complexity of employing workers as an Employer of Record, including government onboarding fees and compliance obligations per country.

**Client quote:** *"Where are the borders or the difficulties actually to employ someone in a country where we don't have companies set up?"*

**Status:** Partially answered during pitch. Full response to be documented in revised proposal.

---

### CR-02 — Social Security / Insurance Registration Automation
**Request:** Automate country-specific social security and insurance registration triggered by a new contract event, per jurisdiction. Client confirmed they researched feasibility and believe it is possible.

**Client quote:** *"The entire social registration for every single country needs to be automated. It's just footwork which creates a lot of manual effort."*

**Status:** Agreed to research compliance framework and scope feasibility. Will be addressed as a Phase 2 capability in the revised proposal.

---

### CR-03 — Contract Generation Workflow
**Request:** Build a workflow that automatically generates contract templates per country from employee data, minimising manual steps up to (but not including) the final signature. Human review of first-use templates per country is mandatory.

**Client quote:** *"The entire process needs to be automated until the point where a human interaction is needed."*

**Status:** Team agreed to scope this. Compliance research required before full commitment. To be included as a proposed extension in the revised proposal.

---

### CR-04 — PO Matching for Agent 2 (Invoice Validation)
**Request:** Expand Agent 2 to compare invoices not only against contract terms but also against Purchase Orders (POs).

**Status:** Confirmed feasible. Scope extension to be documented in revised proposal.

---

### CR-05 — Local Accounting Rules in Agent 2
**Request:** Add jurisdiction-specific accounting principles to Agent 2 — including local thresholds, cutback classifications, and accounting law compliance per country where invoices are processed.

**Status:** Confirmed implementable. Slightly more advanced than current build. To be scoped as Agent 2 enhancement in revised proposal.

---

### CR-06 — Intermediary Cost Tracking
**Request:** Intermediary fees (agencies, EOR providers, government bodies) to be tracked as adjacent costs linked to each contract — visible in both Agent 2 (Invoice Validation) and Agent 5 (Cost Categorisation).

**Status:** Agreed immediately during pitch. To be included in revised proposal as a named enhancement.

---

### CR-07 — Multilingual Ingestion Quality Assurance
**Request:** Formal quality assurance plan for Agent 1 across all operating languages — Russian, Hindi, Urdu, Filipino, Bengali. Client asked for consistency guarantees.

**Status:** Addressed during pitch (iterative quality process, LLM training data availability confirmed for target languages). Testing stage to be formalised in the implementation plan.

---

## 5. What Was Not Changed

The following aspects of ContractOS were accepted without challenge:

- Five-agent architecture and individual agent responsibilities
- Human-in-the-loop gate before any payment or reclassification
- EU AI Act classification (Minimal/Limited risk)
- GDPR lawful basis approach including legitimate interest LIAs
- LangSmith observability setup
- Tech stack: n8n · LangChain · LangGraph · LangSmith
- EU-hosted infrastructure

---

## 6. Concerns Noted During Q&A

| Concern | Raised by | Response given |
|---|---|---|
| Intermediary question only partially answered | Eugen | Agreed to document fully in revised proposal |
| Contract signing automation risk | Eugen | Team correctly pushed back — human review mandatory for first templates |
| AI cost vs current solutions | Eugen (implicit) | LangSmith cost data shown — costs comparatively very low |
| Translation quality consistency | Eugen | Iterative process + LLM training data confirmed adequate for target languages |
| PO matching gap | Eugen | Confirmed implementable, to be scoped |

---

*Daria Bystrova & Julian Granados — SilverTrust Project 4 — Deliverable 7: Peer Approval Record*
