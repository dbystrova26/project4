# SilverTrust — Project 4
## AI Consulting Engagement: Oracle Game Studio

**Team:** Daria Bystrova & Julian Granados
**Industry:** Financial Services (Payroll & Contract Intelligence)
**Client:** Oracle Game Studio (Tech industry — assigned by paired team)
**Date:** Week 7

---

## The Engagement in One Sentence

Oracle is a funded indie game studio with 800–900 people across five countries, burning cash faster than it earns — we designed ContractOS, an AI-powered contract and payroll intelligence layer that reads every contract, detects duplicate payments, validates invoices, and gives leadership a live view of where their money is going.

---

## Repository Structure

### Day 1 — Scenario Design & Discovery

| # | Deliverable | File | Status |
|---|---|---|---|
| 1 | Industry + rationale + scenario designed for paired team (PulseWork) | [`01_scenario_design.docx`](./01_scenario_design.docx) | ✅ |
| 3 | Discovery findings — interview notes, indirect questions, pain-point table, problem statement, solution concept | [`03_discovery_findings.md`](./03_discovery_findings.md) | ✅ |
| 3 | Discovery findings (Word version) | [`03_discovery_findings_FINAL.docx`](./03_discovery_findings_FINAL.docx) | ✅ |

### Day 2 — Compliant Design, Monitoring & Peer Approval

| # | Deliverable | File | Status |
|---|---|---|---|
| 4+5+6 | Solution design + compliance package + LangSmith monitoring | [`04_05_06_tuesday_deliverables.md`](./04_05_06_tuesday_deliverables.md) | ✅ |
| 4+5+6 | Same — Word version | [`04_05_06_tuesday_deliverables.docx`](./04_05_06_tuesday_deliverables.docx) | ✅ |
| 7 | Peer approval record — pitch, review board decision, change requests | [`07_peer_approval_record.md`](./07_peer_approval_record.md) | ⬜ |

### Day 3 — Revised Proposal & Final Delivery

| # | Deliverable | File | Status |
|---|---|---|---|
| 8 | Revised solution & final proposal | [`08_revised_proposal.md`](./08_revised_proposal.md) | ⬜ |
| 9 | Change log — request → action → why | [`09_change_log.md`](./09_change_log.md) | ⬜ |

---

## The Client

**Company:** Oracle Game Studio
**CEO/CTO:** Eugen (co-founder)
**CFO:** Thibaud
**Size:** ~900 people
**Locations:** Russia, India, Pakistan, Bangladesh, Philippines
**Business model:** B2C indie games, one-time purchase via Steam — no subscriptions, no recurring revenue
**Financial status:** Funded, at break even — high burn rate, needs to cut costs to return to profitability

---

## The Problem

> Oracle has no visibility over who is engaged, on what terms, and at what cost across 900 people in five jurisdictions. Contracts are unread, invoices go unchecked, subcontractors have been lost track of, and internal work is being duplicated externally. The only lever available is cost — AI cannot fix the revenue side of a one-time purchase model.

---

## The Solution — ContractOS

An AI-powered contract and payroll intelligence layer with four capabilities delivered by three AI agents:

| Capability | AI Agent | What it does | Pain point solved |
|---|---|---|---|
| Contract Intelligence | Agent 1 — Contract Reader | Reads all contracts, extracts key terms, flags misclassification and IP risk | Lost contractor visibility, compliance unknown |
| Overlap Detection | Agent 2 — Cost Analyst | Compares contractor scope against internal roles — flags duplicate payments | Paying twice for same work |
| Cost Dashboard | Agent 2 — Cost Analyst | Categorises spend by country, type, team, intermediary — live burn view | No cost visibility |
| Payment Tracking | Agent 2 — Cost Analyst | Validates invoices against contracts, tracks payment status | Wrong invoicing, payroll bottlenecks |
| Compliance Checking | Agent 3 — Compliance Checker | Red/Amber/Green status per contract across five jurisdictions | Compliance unknown, misclassification risk |

> ⚠️ **Critical design constraint:** The AI flags and surfaces — a human approves before any payment is sent or any contractor is reclassified.

---

## Compliance Summary

| Area | Classification | Key obligation |
|---|---|---|
| EU AI Act | Minimal risk (extraction, dashboard) / Limited risk (misclassification flagging) | Human-in-the-loop mandatory before any employment-affecting action |
| GDPR — contracts | Lawful basis: contract performance (Art. 6(1)(b)) + legal obligation (Art. 6(1)(c)) | DPA + SCCs required for LLM provider; EU-based infrastructure only |
| GDPR — LLM processing | Legitimate interest (Art. 6(1)(f)) | LIA must be documented before go-live |
| Third countries | India (DPDP Act), Philippines (DPA 2012), Russia (sanctions + data localisation) | Data stays EU-side; local counsel required per jurisdiction |
| German BetrVG | Works council consultation required before go-live | SilverTrust provides technical documentation |
| NL DBA Act (2025) | Contractor misclassification flags | Human + legal review before any reclassification |

---

## LangSmith Monitoring

**Project name:** `contractos-oracle-prod`
🔗 **Live link:** https://eu.smith.langchain.com/o/453c43c0-ddb5-408a-a509-630402964189/projects/p/bff005c1-351b-4293-92ca-623f47b8ba5b
**Agents traced:** `contract-intelligence-agent`, `invoice-validation-agent`, `overlap-detection-agent`, `compliance-flagging-agent`, `cost-categorisation-agent`

**What we monitor:**
- Extraction confidence score per field (alert if < 0.80 on critical fields)
- Human override rate (alert if > 20% in 7-day window)
- Latency per agent call (alert if p95 > 30 seconds)
- Failed extractions (zero tolerance alert)
- Compliance flag distribution (alert if Red > 10% of new contracts)
- PII redaction verification (weekly audit, zero tolerance)

**Client reassurance:**
> *"Every time the AI reads a contract, we log exactly what it extracted and how confident it was. If it flags a risk, a human reviews it before anything happens. You have a complete audit trail at all times."*

### Screenshots

**Screenshot 1 — Project overview: all 6 agent runs**
![LangSmith project overview showing all agent runs](./screenshot_01_overview.png)

**Screenshot 2 — Contract Intelligence Agent: Jana Novak contract extracted**
![Contract Intelligence Agent trace showing input contract and extracted JSON](./screenshot_02_contract_intelligence.png)

**Screenshot 3 — Compliance Flagging Agent: Arjun Sharma RED flag**
![Compliance Flagging Agent showing RED status and misclassification flags for Arjun Sharma](./screenshot_03_compliance_red.png)

**Screenshot 4 — Overlap Detection Agent: 95/100 overlap score**
![Overlap Detection Agent showing 95 overlap score between Jana Novak and internal engineer](./screenshot_04_overlap_detection.png)


---

---

## Scenario Designed for Paired Team

**Company:** PulseWork — Munich-based AI workforce analytics scaleup (~150 staff)
**Industry:** Tech
**Core problem:** AI productivity scoring used in firing decisions, no GDPR lawful basis, Dutch works council legal challenge hidden from investors
**Full scenario:** [`01_scenario_design.docx`](./01_scenario_design.docx)

---

## Submission Checklist

- [x] Monday: industry chosen; scenario designed and sent to teacher; discovery findings captured
- [x] Tuesday: solution design, compliance package, LangSmith monitoring documented
- [ ] Tuesday: peer-approval record (after afternoon pitch)
- [ ] Wednesday: revised proposal, final deck, change log, repository delivered
- [x] LangSmith project live — link: https://eu.smith.langchain.com/o/453c43c0-ddb5-408a-a509-630402964189/projects/p/bff005c1-351b-4293-92ca-623f47b8ba5b
- [ ] Repository accessible to instructors; all links working
- [ ] All team members can explain the whole solution

---

## Quick Navigation

| What you need | Where to find it |
|---|---|
| Who is the client and what is the problem | This README — sections above |
| How we discovered the problem | [`03_discovery_findings.md`](./03_discovery_findings.md) |
| What ContractOS does and how it works | [`04_05_06_tuesday_deliverables.md`](./04_05_06_tuesday_deliverables.md) — Deliverable 4 |
| EU AI Act classification and justification | [`04_05_06_tuesday_deliverables.md`](./04_05_06_tuesday_deliverables.md) — Section 5.1 |
| GDPR data map and lawful basis | [`04_05_06_tuesday_deliverables.md`](./04_05_06_tuesday_deliverables.md) — Section 5.2 |
| Compliance memo (plain English) | [`04_05_06_tuesday_deliverables.md`](./04_05_06_tuesday_deliverables.md) — Section 5.5 |
| LangSmith monitoring setup | [`04_05_06_tuesday_deliverables.md`](./04_05_06_tuesday_deliverables.md) — Deliverable 6 |
| Scenario we designed for paired team | [`01_scenario_design.docx`](./01_scenario_design.docx) |
| Peer review record | [`07_peer_approval_record.md`](./07_peer_approval_record.md) *(after Tuesday pitch)* |
| Change log | [`09_change_log.md`](./09_change_log.md) *(Wednesday)* |

---

*SilverTrust Project 4 — Daria Bystrova & Julian Grandaos — Week 7*
