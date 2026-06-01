# SilverTrust — Project 4 | Day 1 Deliverable #3
## Discovery Findings — Oracle Game Studio
**Interview Notes | Indirect Questions Used | Pain-Point Table | Problem Statement | Solution Concept**

*Daria Bystrova & Julian Granados*

---

## 1. Interview Notes

> Selected observations only — not a full transcript. Key moments, deflections, and signals that shaped our solution design.

### Setup

- Two personas present: Eugen (CEO/CTO, co-founder) and Thibaud (CFO)
- Thibaud opened by stating he is new to AI — asked us to speak in plain language throughout
- Eugen led most answers; Thibaud deferred on product and operations, stepped in on financials
- Tone: friendly and open — Eugen visibly uncomfortable when cost questions sharpened

### Key Observations

| # | What happened | What we noted | Signal |
|---|---|---|---|
| 1 | Eugen: "money is a little bit just the secondary thing here" | Classic founder deflection — money IS the problem but he reframes it as a mission company | Financial pain is real but leadership is in partial denial |
| 2 | "I cannot really tell you what kind of tools we're using" | CEO does not know his own tool stack — confirms zero cost visibility | No central oversight of spend |
| 3 | Thibaud: payroll stack is "absolutely a mess" | Strongest language of the interview — CFO is genuinely distressed | Core pain confirmed — not exaggerated |
| 4 | Eugen redirected the "one wish" question to Thibaud | Eugen knows the financial problem is Thibaud's domain — he does not want to own it | Thibaud is the economic buyer |
| 5 | Thibaud: "we kind of lost track of all the subcontractors" | Specific operational failure — contractors active with no oversight, duplicate payments likely | Immediate cost leak |
| 6 | Both said "are we actually compliant?" unprompted | Compliance anxiety is real — they know they don't know, and it worries them | Compliance story is a trust builder in the pitch |
| 7 | Eugen: "not a new contract management system... needs to elevate" | High bar — they have been disappointed by tools before or fear being sold something basic | Pitch must lead with AI intelligence, not software features |
| 8 | Churn question deflected: "it is more or less a one time purchase" | Revenue model confirmed — no subscriber base, no churn lever | Only cost side is actionable — ruled out customer AI |

---

## 2. Indirect Questions Used

> No direct pain-point questions were asked. All questions were indirect — process-led, role-led, or hypothetical. Quoted as closely as possible from the interview transcript.

| # | Block | Question asked | Why indirect / what we were listening for |
|---|---|---|---|
| 1 | Warm up | "Could you give us a brief about the company — walk me through the organisation day by day, what is your core service, who are your customers" | Orient without assumptions — discover sub-sector, business model, customer type before forming any hypothesis |
| 2 | Warm up | "Maybe you'll be the right person to explain how the organisation makes money — like to the baby" | Disarming framing — invites simple answer, surfaces whether revenue model is healthy or stressed without asking directly |
| 3 | Business model | "So who are your clients? Do you develop games for B2B or do you also sell to individuals?" | Confirm B2B vs B2C — changes data flows, GDPR surface, and AI use case landscape entirely |
| 4 | Workflow | "Could you walk us through what happens from the moment the user signs up until they are fully active on the platform?" | Map end-to-end process — find where data is collected, where decisions are made, where friction exists |
| 5 | Cost | "Which is your highest costing cost column — where are you paying the most?" | Indirect cost probe — gets them to rank costs without asking what is broken |
| 6 | Bottleneck | "Which bottlenecks have you identified in the last months — where is the workflow stopping or where is money being spent that is not leading to the expected result?" | Process complaint question — invites frustration without asking what is wrong directly |
| 7 | One wish | "If you had one wish that you could make and make things better in your company — what would it be?" | Classic closing probe — surfaces the priority pain without naming it. Thibaud answered immediately: break even |
| 8 | Current state | "How are you currently doing it and what is not working?" | Forces description of current process before criticising it — reveals legacy tools and workarounds |
| 9 | Workforce | "Are all of your developers on payroll or do you also use contractors?" | Surfaces workforce complexity — different contract types mean different compliance and payment rules |
| 10 | Compliance | "From the angle of GDPR and compliance, is there any data-related process in place — for instance data stored in US-based tools?" | Compliance probe — surfaces whether they have thought about cross-border data at all. Answer confirmed they had not |

---

## 3. Pain-Point Table by Persona

> Each pain point is mapped to the persona who revealed it, with transcript evidence and the direct implication for our solution design.

### Persona 1 — Eugen, CEO / CTO

| Discovered pain point | Evidence from interview | How it affects the solution |
|---|---|---|
| **No visibility over tool stack and costs** | "I cannot really tell you what kind of tools we're using... people just want a tool and then we give it to them" | Solution must aggregate all cost data into one view — CEO dashboard requiring no finance expertise → **Agent 5: Cost Categorisation** |
| **Internal and external work overlapping** | "We are externalising tasks which we are already doing internally" | AI compares contractor scope against internal roles and flags duplicates → **Agent 3: Overlap Detection** |
| **Compliance unknown and unmanaged** | "Are we actually compliant by doing what we are doing?" — asked unprompted | Compliance flagging per contract and jurisdiction must be built in as a core feature → **Agent 4: Compliance Flagging** |
| **Existing tools have failed or disappointed** | "This thing needs to kind of elevate what we're doing... not a new contract management system" | Product must be framed as AI intelligence layer, not software. Demo must show reasoning and automation, not forms |

### Persona 2 — Thibaud, CFO

| Discovered pain point | Evidence from interview | How it affects the solution |
|---|---|---|
| **Cannot return to break even — burn exceeding revenue** | "To go back to break even... I'm pretty sure we could reduce some of our costs" | Solution must produce measurable cost reduction as primary outcome. ROI story essential → **Agent 5: Cost Categorisation** |
| **Lost track of subcontractors** | "We kind of lost track of all the subcontractors we have and we're working with" | Live contractor register is a core feature: who is active, what they are paid, when last invoiced → **Agent 1: Contract Intelligence** |
| **Wrong invoicing — amounts not matching contracts** | "Wrong invoicing, pay cycles" — stack is "absolutely a mess" | Invoice validation against contract terms must be automated — flag before payment → **Agent 2: Invoice Validation** |
| **Multi-country payroll bottleneck** | "Solutions only work as good as the availability is in certain countries... we have to include accounting firms or payroll firms" | Payment tracking: confirm sent, confirm arrived, flag failures. Works alongside Wise → **Agent 2: Invoice Validation** |
| **Possibly paying twice for the same work** | "See if we are maybe paying twice for the same" | Cross-reference contractor invoices against internal payroll. Highest quick-win for cost reduction → **Agent 3: Overlap Detection** |

### Combined Summary — Persona → Pain Point → Agent → Capability

| Persona | Discovered pain point | Agent | Capability | Priority |
|---|---|---|---|---|
| Eugen | No tool/cost visibility | Agent 5 | Cost Categorisation | **High** |
| Eugen | Internal vs external overlap | Agent 3 | Overlap Detection | **High** |
| Eugen | Compliance unknown | Agent 4 | Compliance Flagging | **High** |
| Eugen | Tools have failed before | — | AI-first UX, not a form | Medium |
| Thibaud | Burn exceeding revenue | Agent 5 | Cost Categorisation | **Critical** |
| Thibaud | Lost track of contractors | Agent 1 | Contract Intelligence | **Critical** |
| Thibaud | Wrong invoicing | Agent 2 | Invoice Validation | **Critical** |
| Thibaud | Multi-country payroll bottleneck | Agent 2 | Invoice Validation | **High** |
| Thibaud | Paying twice for same work | Agent 3 | Overlap Detection | **Critical** |

---

## 4. Problem Statement

> *"Oracle is a funded indie game studio burning cash at an unsustainable rate across 800–900 people in five high-complexity jurisdictions. The core problem is not revenue — one-time purchases are structurally fixed and no customer data is collected post-sale. The problem is entirely on the cost side: nobody has a clear picture of who is engaged, on what terms, and at what cost. Contracts are unread, invoices go unchecked, subcontractors have been lost track of, and internal work is being duplicated externally. Regulatory compliance across five countries is unverified. The result is money leaving the company through errors, duplicate payments, intermediary costs, and potential regulatory fines. AI can help by reading every contract automatically, identifying overlaps and duplicates, catching invoice errors before payment, categorising costs by type and jurisdiction, and flagging compliance risks — giving Thibaud the visibility to cut costs intelligently and Eugen the operational clarity to protect his engineering team."*

---

## 5. Initial AI Solution Concept — ContractOS

### The One-Line Pitch

> *"A single AI-powered interface that reads every contract, finds the overlaps, catches the errors, tracks the payments, and shows exactly where the money is going — so Oracle gets back to black numbers."*

### Five Capabilities

| Capability | Agent that powers it | What the AI does | Pain points solved |
|---|---|---|---|
| **1. Contract Intelligence** | Agent 1 — Contract Intelligence Agent | Reads all contracts across formats and languages. Extracts: person, role, rate, currency, contract type, jurisdiction, notice period, IP clauses, renewal date, GDPR clause presence. | Lost contractor visibility, no single contract view |
| **2. Invoice Validation** | Agent 2 — Invoice Validation Agent | Validates every incoming invoice against contract terms before payment. Flags amount mismatches, currency errors, and scope discrepancies. | Wrong invoicing, payments not matching contracts |
| **3. Overlap Detection** | Agent 3 — Overlap Detection Agent | Compares contractor scope descriptions against internal job roles using semantic similarity. Flags where the same work is being paid twice inside and outside the company. | Paying twice for same work, internal vs external overlap |
| **4. Compliance Flagging** | Agent 4 — Compliance Flagging Agent | Checks each contract against jurisdiction-specific rule sets. Outputs Red / Amber / Green status with specific flags for misclassification risk, missing GDPR clauses, and ambiguous IP assignment. | Compliance unknown, misclassification risk across five countries |
| **5. Cost Categorisation** | Agent 5 — Cost Categorisation Agent | Categorises all workforce spend by country, contract type, team, and intermediary. Real-time burn visibility in one view for Thibaud and Eugen. | No cost visibility, burn exceeding revenue, intermediary opacity |

### Five AI Agents — One Capability Each

> Five dedicated AI agents, each with a single responsibility, all orchestrated by LangGraph. Every agent produces structured outputs and confidence scores — none executes final decisions.

| Agent | Capability | Technical description |
|---|---|---|
| **Agent 1 — Contract Intelligence Agent** | Contract Intelligence | LLM ingests contract documents. Structured extraction prompt returns JSON: name, role, rate, currency, jurisdiction, notice period, IP clause status, GDPR clause status, working arrangement description. Output stored in Contract Register DB. |
| **Agent 2 — Invoice Validation Agent** | Invoice Validation | LLM reads incoming invoice text and compares it against extracted contract terms. Flags discrepancies in amount, currency, scope, and billing period. Output: validated / flagged + specific mismatch detail. |
| **Agent 3 — Overlap Detection Agent** | Overlap Detection | LLM compares contractor working arrangement descriptions against internal job role descriptions using semantic similarity. Flags pairs where scope overlap exceeds threshold. Output: overlap alert with contractor name, internal role, estimated duplicate cost. |
| **Agent 4 — Compliance Flagging Agent** | Compliance Flagging | LLM checks extracted contract data against jurisdiction-specific rule sets: GDPR clause presence, IP assignment clarity, misclassification indicators (NL DBA, German Scheinselbstständigkeit, French rules), notice period minimums. Output: Red / Amber / Green + specific flags per contract. |
| **Agent 5 — Cost Categorisation Agent** | Cost Categorisation | LLM normalises ambiguous spend descriptions and categorises all payments by country, contract type, team, and intermediary. Plain software aggregates and renders the dashboard. Output: categorised cost register + burn trend. |

### Where AI Is Genuinely Needed vs Plain Software

| AI / LLM reasoning genuinely needed | Plain software sufficient |
|---|---|
| Extracting data from unstructured, multilingual, varied contract templates | Storing extracted data in a structured database |
| Identifying misclassification risk from natural language descriptions of working arrangements | Sending payment alerts and notifications |
| Detecting overlap between contractor scope and internal roles across free-text descriptions | Generating the cost dashboard and charts |
| Flagging missing jurisdiction-specific clauses from contract text | Access control — who can see salary data |
| Compliance checking across five jurisdictions simultaneously | Payment processing — handled by existing rails such as Wise |
| Invoice anomaly detection — normalising messy multilingual invoice formats | Audit trail and notification alerts |

> ⚠️ **Critical design constraint:** The AI flags and surfaces — a human approves before any payment is sent or any contractor is reclassified. This keeps the system at limited/minimal risk under the EU AI Act and satisfies GDPR Article 22.

---

*Daria Bystrova & Julian Granados — SilverTrust Project 4 — Deliverable #3: Discovery Findings*
