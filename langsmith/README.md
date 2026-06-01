# ContractOS — LangSmith Monitoring Demo
## SilverTrust Project 4 | Daria Bystrova & Julian Grandaos

This folder contains the LangSmith observability setup for ContractOS — the AI-powered contract and payroll intelligence system built for Oracle Game Studio.

Running this demo populates the LangSmith dashboard with real traces from all five ContractOS agents, providing a live audit trail that demonstrates EU AI Act compliance and gives Oracle's leadership visibility into every AI decision.

🔗 **Live LangSmith project:** https://eu.smith.langchain.com/o/453c43c0-ddb5-408a-a509-630402964189/projects/p/bff005c1-351b-4293-92ca-623f47b8ba5b

---

## What This Does

Runs five AI agents against realistic Oracle Game Studio sample data and traces every call in LangSmith:

| Agent | What it traces |
|---|---|
| `contract-intelligence-agent` | Extracts structured fields from contractor agreements |
| `invoice-validation-agent` | Validates invoices against contract terms, flags mismatches |
| `overlap-detection-agent` | Detects where contractor scope duplicates internal roles |
| `compliance-flagging-agent` | Checks contracts against jurisdiction rules, outputs Red/Amber/Green |
| `cost-categorisation-agent` | Categorises payments by country, type, team, intermediary |

---

## Setup — Step by Step

### 1. Create a LangSmith account
Go to [smith.langchain.com](https://smith.langchain.com) and sign up (free tier is fine).

### 2. Create the project
- Click **New Project**
- Name it exactly: `contractos-oracle-prod`
- Click Create

### 3. Get your LangSmith API key
- Go to **Settings → API Keys**
- Click **Create API Key**
- Copy it — you only see it once

### 4. Get your Anthropic API key
- Go to [console.anthropic.com](https://console.anthropic.com) → API Keys
- Create a new key and copy it

### 5. Set up your environment

```bash
# Copy the example env file
cp .env.example .env
# Then open .env and fill in your real keys
```

Your `.env` must contain all of these:

```bash
# Anthropic
ANTHROPIC_API_KEY=sk-ant-your-key-here

# LangSmith — new variable names
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT=https://eu.api.smith.langchain.com
LANGSMITH_API_KEY=lsv2_pt_your-key-here
LANGSMITH_PROJECT=contractos-oracle-prod

# LangSmith — old variable names (kept for compatibility)
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=lsv2_pt_your-key-here
LANGCHAIN_PROJECT=contractos-oracle-prod
```

> ⚠️ Use the EU endpoint if your LangSmith account is on `eu.smith.langchain.com`. Same key under both `LANGSMITH_API_KEY` and `LANGCHAIN_API_KEY` — different packages look for different names.

### 6. Install dependencies

```bash
pip install -r requirements.txt
```

### 7. Run the demo

```bash
python contractos_demo.py
```

---

## What You Should See

In your terminal — six agent runs printing JSON output:
- Agent 1: Jana Novak contract extracted cleanly
- Agent 2a: Jana invoice validated (matches contract rate)
- Agent 2b: Raj Consulting invoice flagged (mismatch — rate discrepancy + verbal agreement claim)
- Agent 3: Overlap detected between Jana and internal backend engineer — score 95/100, €8,500/month duplicate cost
- Agent 4: Arjun Sharma flagged **RED** — misclassification risk (works exclusively for Oracle, 40hrs/week, Oracle equipment, daily standups)
- Agent 5: TechStaff Philippines payment categorised via intermediary

In LangSmith:
- Project `contractos-oracle-prod` shows all six runs
- Each run shows input prompt, output JSON, latency, model used, and cost
- Click any run to see the full trace

---

## Screenshots

Screenshots are in the `screenshots/` subfolder.

| File | What it shows |
|---|---|
| `screenshot_01_overview.png` | Project dashboard — all 6 runs with latency and cost |
| `screenshot_02_contract_intelligence.png` | `contract-intelligence-agent` trace — Jana Novak extracted to JSON |
| `screenshot_03_compliance_red.png` | `compliance-flagging-agent` trace — Arjun Sharma flagged RED |
| `screenshot_04_overlap_detection.png` | `overlap-detection-agent` trace — 95/100 overlap, €8,500/month duplicate cost |

**Screenshot 1 — Project overview: all 6 runs**
![Project overview](./screenshots/screenshot_01_overview.png)

**Screenshot 2 — Contract Intelligence Agent: Jana Novak extracted**
![Contract Intelligence trace](./screenshots/screenshot_02_contract_intelligence.png)

**Screenshot 3 — Compliance Flagging Agent: Arjun Sharma RED**
![Compliance RED flag](./screenshots/screenshot_03_compliance_red.png)

**Screenshot 4 — Overlap Detection Agent: 95/100 overlap score**
![Overlap detection](./screenshots/screenshot_04_overlap_detection.png)

---

## Files in This Folder

```
langsmith/
├── README.md               ← this file
├── contractos_demo.py      ← runs all five agents
├── requirements.txt        ← Python dependencies
├── .env.example            ← copy to .env and fill in keys
├── .gitignore              ← prevents .env being committed
└── screenshots/
    ├── screenshot_01_overview.png
    ├── screenshot_02_contract_intelligence.png
    ├── screenshot_03_compliance_red.png
    └── screenshot_04_overlap_detection.png
```

---

## Why This Matters — The Client Pitch

When Oracle's leadership asks *"can you actually see what the AI does?"*:

> *"Yes. Here is the LangSmith dashboard. Every time ContractOS read a contract, we logged exactly what it extracted and how confident it was. Here is Agent 4 flagging Arjun's contract RED — it detected misclassification risk because he works exclusively for Oracle, 40 hours a week, using Oracle's equipment. That flag went to your legal team for review before any action was taken. Nothing happened automatically. And if a regulator asks what the AI did with that contract — we can show them the complete chain in under five minutes."*

---

## Connection to EU AI Act

The LangSmith traces are technical proof that:
- Human oversight is **actually enforced** — every flag logged, every human decision recorded
- The system is **auditable** — complete chain from input to approved action
- ContractOS stays at **limited/minimal risk** — no automated decisions visible in traces

---

*SilverTrust Project 4 — ContractOS LangSmith Monitoring*
*Daria Bystrova & Julian Grandaos*
