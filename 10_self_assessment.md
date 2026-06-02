# SilverTrust — Project 4 Self-Assessment
**Daria Bystrova & Julian Granados | Week 7**

---

## Self-Reflection

**What do you like most about your project?**

The thing we are most proud of is that ContractOS is grounded in real pain — every capability maps directly to something Eugen or Thibaud said in the interview, and we can point to the exact quote. The LangSmith demo made the pitch concrete rather than theoretical: we opened a live dashboard and showed Arjun Sharma's contract flagged RED in real time. That moment landed visibly with the review board. We also liked that the compliance package was not theatre — three completed LIAs, not just a statement that legitimate interest applies.

---

**What would you change if you started from scratch?**

We would include EOR coverage, PO matching, and intermediary cost tracking in v1.0 — not as change requests. All three were visible from the discovery interview and from the first Agent 5 run (47% of Oracle's burn goes through intermediaries). We had the data and still missed the capability. A real engagement would not have gotten away with that gap.

We would also formalise the multilingual QA plan before the pitch, not after being challenged on it. Stating confidence informally is not the same as showing a plan.

---

**What would you like to add when you have more time?**

The two Phase 2 capabilities: social registration automation per country (triggered by new contract events) and the contract generation workflow that takes HR onboarding data and produces a draft contract in the local language. Eugen's reaction when we described the contract generation idea was the most animated moment of the entire meeting — that is the feature he actually wants. We would also add a real web dashboard for Thibaud rather than a Python matplotlib output file.

---

**What was the biggest challenge you faced, and how did you overcome it?**

Getting LangSmith to run correctly was the hardest technical moment. The model name `claude-sonnet-4-20250514` returned a 404, the environment variable names had changed between LangSmith versions (`LANGCHAIN_API_KEY` vs `LANGSMITH_API_KEY`), and the agent outputs came back wrapped in markdown backticks that broke JSON parsing. Each of these was a small problem but they compounded under time pressure. We overcame them by isolating each error one at a time — fixing the model name first, then the env vars, then adding a `clean_json()` helper to strip the backticks. The lesson: never leave the technical demo to the day of the pitch.

---

**How did you handle the review board's change requests? What did you learn about change management?**

We accepted five of seven change requests as immediate Phase 1 enhancements, scoped two as Phase 2 pending legal research, and pushed back on two requests — auto-signing and full lawyer replacement. The push-backs were the most important part. Saying "we won't do that and here is why" is harder than saying yes to everything, but it is what a real consultant does. The client accepted both push-backs once we explained the reasoning clearly.

What we learned: change requests are not a failure — they are information. The review board identified three gaps (EOR, intermediary tracking, multilingual QA) that we should have caught ourselves. A good change log does not just say what changed; it says why we missed it the first time.

---

**What did your EU AI Act / GDPR analysis get wrong at first, and how did you fix it?**

Two things. First, we did not address EOR in the compliance position at all, even though operating in five countries without legal entities is a direct compliance risk. The review board surfaced this through CR-01. We fixed it by adding EOR flagging to Agent 4 and documenting that the same legitimate interest basis covers EOR data processing.

Second, the multilingual processing was described as confident but not documented. GDPR Article 5(1)(f) requires appropriate technical and organisational measures — a vague confidence statement is not a measure. We fixed this with a formal three-phase QA plan with acceptance criteria per language.

What we got right from the start: the three LIAs were completed properly, not just mentioned. The balancing tests for LLM processing, overlap detection, and LangSmith monitoring are documented in full in section 5.2a of the Tuesday deliverables.

---

**How did LangSmith monitoring help you reassure the client about the AI? What was still hard to explain?**

What worked: opening the live dashboard and showing the compliance-flagging-agent trace for Arjun Sharma. The client could see — not just be told — that the system flagged a RED status, logged the input contract, logged the output flags, logged the latency, and attributed a cost of $0.0068 to the call. The cost number was unexpectedly effective: Eugen's concern about AI being expensive was answered by showing him the actual per-call cost in the dashboard.

What was still hard to explain: why PII redaction is configured as a technical control rather than a policy promise. The concept that "we have set up automatic redaction before traces are stored" requires the client to trust that the technical control actually works — they cannot see it working in the dashboard the way they can see the agent outputs. This required more verbal explanation than we wanted.

---

**How did the secret stakeholder interviews change your understanding of the real problem?**

Significantly. Going in, we assumed the problem was compliance — Oracle operates across five jurisdictions with complex employment law. The interview revealed that compliance was actually a secondary concern that neither Eugen nor Thibaud had properly thought through. The primary problem was simpler and more urgent: they literally did not know what they were paying, to whom, or whether the amounts were correct. Thibaud's phrase "the stack is absolutely a mess" was said with genuine distress, not corporate understatement.

This changed the solution. Our first instinct was to lead with compliance flagging. After the interview we led with cost visibility and invoice validation — the things that save money this month — and put compliance as supporting evidence, not the headline. The pitch was sharper for it.

The indirect questioning technique also surfaced something we would not have asked directly: when we asked "what is your one wish," Thibaud answered immediately with "break even." That confirmed that cost is the only lever and gave us the framing for the entire pitch — "revenue side is structurally fixed, only cost can move."

---

**What would you do differently in a real AI consulting engagement?**

Three things.

First, validate the EOR and intermediary situation in discovery, not after the pitch. These are not edge cases for a company with 900 people across five countries — they are core operational realities.

Second, run the technical demo before the pitch day, not on it. LangSmith works now, but it took three rounds of debugging to get there. In a paid engagement that debugging happens on the client's time and damages credibility.

Third, define the human review process more concretely in the initial design. "Human approves before action" is the right principle but it is not a product. A real deployment needs a named person, a named interface, and a named maximum review time for each flag type. We described the principle correctly but not the implementation.

---

## Goal Setting for Next Project

**Goal 1:** In the discovery phase, map every capability directly to a specific pain point quote from the interview before writing a single line of solution design. If a capability cannot be traced to a quote, it does not go in the proposal. This would have prevented the EOR and intermediary tracking gaps.

**Goal 2:** Run the technical demo end-to-end at least 48 hours before the pitch. Document any errors encountered and the fixes applied. Keep a "demo runbook" — the exact commands to run, in order, with expected outputs — so that a second team member can reproduce the demo independently without debugging on the day.

---

*Daria Bystrova & Julian Granados — SilverTrust Project 4 — Self-Assessment*
