# ContractOS — LangSmith Monitoring Demo
## SilverTrust Project 4 | Daria Bystrova & Julian Grandaos

This folder contains the LangSmith observability setup for ContractOS — the AI-powered contract and payroll intelligence system built for Oracle Game Studio.

Running this demo populates the LangSmith dashboard with real traces from all five ContractOS agents, providing a live audit trail that demonstrates EU AI Act compliance and gives Oracle's leadership visibility into every AI decision.

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

# Edit .env and fill in your keys
# LANGCHAIN_API_KEY=your_langsmith_key
# ANTHROPIC_API_KEY=your_anthropic_key
```

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
- Agent 2a: Jana's invoice validated (matches)
- Agent 2b: Raj Consulting invoice flagged (mismatch — rate discrepancy)
- Agent 3: Overlap detected between Jana and internal backend engineer
- Agent 4: Arjun Sharma flagged RED — misclassification risk (works exclusively for Oracle, 40hrs/week, Oracle equipment)
- Agent 5: TechStaff Philippines payment categorised via intermediary

In LangSmith at [smith.langchain.com](https://smith.langchain.com):
- Project `contractos-oracle-prod` shows all six runs
- Each run shows input prompt, output JSON, latency, and model used
- Click any run to see the full trace

---

## Screenshots to Take for Deliverable

Take these four screenshots and add them to this folder:

| File | What to capture |
|---|---|
| `screenshot_01_project_overview.png` | Project dashboard showing all six runs listed |
| `screenshot_02_contract_intelligence_trace.png` | contract-intelligence-agent run opened, showing input and JSON output |
| `screenshot_03_compliance_red_flag.png` | compliance-flagging-agent run for Arjun Sharma showing RED status |
| `screenshot_04_all_agent_names.png` | All five agent names visible in the runs list |

---

## Share the Project Link

In LangSmith:
- Go to project settings
- Enable **Share project**
- Copy the public link
- Paste it into the main `README.md` under LangSmith Monitoring

---

## Files in This Folder

```
langsmith/
├── README.md               ← this file
├── contractos_demo.py      ← runs all five agents
├── requirements.txt        ← Python dependencies
├── .env.example            ← copy to .env and fill in keys
├── .gitignore              ← prevents .env being committed
└── screenshots/            ← add your screenshots here
    ├── screenshot_01_project_overview.png
    ├── screenshot_02_contract_intelligence_trace.png
    ├── screenshot_03_compliance_red_flag.png
    └── screenshot_04_all_agent_names.png
```

---

## Why This Matters — The Client Pitch

When Oracle's leadership asks *"can you actually see what the AI does?"*:

> *"Yes. Here is the LangSmith dashboard. Every time ContractOS read a contract, we logged exactly what it extracted and how confident it was. Here is Agent 4 flagging Arjun's contract red — it detected misclassification risk because he works exclusively for Oracle, 40 hours a week, using Oracle's equipment. That flag went to your legal team for review before any action was taken. Nothing happened automatically. And if a regulator asks what the AI did with that contract — we can show them the complete chain in under five minutes."*

---

## Connection to EU AI Act

The LangSmith traces are technical proof that:
- Human oversight is **actually enforced** (every flag logged, every human decision recorded)
- The system is **auditable** (complete chain from input to approved action)
- ContractOS stays at **limited/minimal risk** (no automated decisions visible in traces)

---

*SilverTrust Project 4 — ContractOS LangSmith Monitoring*
*Daria Bystrova & Julian Grandaos*
