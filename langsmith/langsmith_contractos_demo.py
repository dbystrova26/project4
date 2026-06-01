"""
ContractOS — LangSmith Demo
SilverTrust Project 4 | Daria Bystrova & Julian Grandaos

Runs all five ContractOS agents against realistic sample data.
Every call is automatically traced in LangSmith under the project
'contractos-oracle-prod'.

Usage:
    1. Copy .env.example to .env and fill in your API keys
    2. pip install -r requirements.txt
    3. python contractos_demo.py

After running, go to https://smith.langchain.com to see all five traces.
"""

import os
import json
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langsmith import traceable

# ── Load environment variables from .env ───────────────────────────────────
load_dotenv()

# ── Verify required env vars are set ───────────────────────────────────────
required = [
    "LANGCHAIN_TRACING_V2",
    "LANGCHAIN_API_KEY",
    "LANGCHAIN_PROJECT",
    "ANTHROPIC_API_KEY",
]
missing = [k for k in required if not os.getenv(k)]
if missing:
    raise EnvironmentError(
        f"Missing environment variables: {missing}\n"
        "Copy .env.example to .env and fill in your keys."
    )

# ── Initialise the LLM ─────────────────────────────────────────────────────
llm = ChatAnthropic(model="claude-sonnet-4-5")


# ══════════════════════════════════════════════════════════════════════════════
# AGENT 1 — Contract Intelligence Agent
# Extracts structured fields from raw contract text
# ══════════════════════════════════════════════════════════════════════════════
@traceable(name="contract-intelligence-agent")
def contract_intelligence(contract_text: str) -> dict:
    """
    Reads a contractor or employee agreement and extracts key fields as JSON.
    Maps to Capability 1: Contract Intelligence.
    """
    response = llm.invoke(f"""
You are the Contract Intelligence Agent for ContractOS, an AI-powered contract
and payroll intelligence system used by Oracle Game Studio.

Extract the following fields from the contract below and return as valid JSON only.
Do not include any explanation or markdown — return raw JSON only.

Fields to extract:
- name (string)
- role (string)
- rate (number)
- currency (string, e.g. EUR)
- jurisdiction (string, country or region)
- notice_period_days (number)
- ip_clause_present (boolean)
- gdpr_clause_present (boolean)
- contract_type (string: FTE / part-time / contractor / consultant / intern)
- working_arrangement_description (string, one sentence describing the work)

Contract:
{contract_text}
""")
    try:
        return json.loads(response.content)
    except json.JSONDecodeError:
        return {"raw_output": response.content, "parse_error": True}


# ══════════════════════════════════════════════════════════════════════════════
# AGENT 2 — Invoice Validation Agent
# Checks whether an invoice matches the agreed contract terms
# ══════════════════════════════════════════════════════════════════════════════
@traceable(name="invoice-validation-agent")
def invoice_validation(invoice_text: str, contract_rate: str, contract_currency: str) -> dict:
    """
    Validates an incoming invoice against the contract rate and terms.
    Maps to Capability 2: Invoice Validation.
    """
    response = llm.invoke(f"""
You are the Invoice Validation Agent for ContractOS.

Compare this invoice against the agreed contract terms and identify any mismatches.
Return valid JSON only — no explanation, no markdown.

Agreed contract rate: {contract_rate} {contract_currency} per day
Invoice to validate:
{invoice_text}

Return JSON with:
- status (string: "valid" or "flagged")
- invoice_amount (number)
- invoice_currency (string)
- expected_amount (number, based on rate and days worked)
- mismatch_detected (boolean)
- mismatch_detail (string, null if no mismatch)
- recommended_action (string: "approve" / "hold for review" / "reject")
- confidence (number 0-100)
""")
    try:
        return json.loads(response.content)
    except json.JSONDecodeError:
        return {"raw_output": response.content, "parse_error": True}


# ══════════════════════════════════════════════════════════════════════════════
# AGENT 3 — Overlap Detection Agent
# Detects where contractor scope duplicates an internal employee role
# ══════════════════════════════════════════════════════════════════════════════
@traceable(name="overlap-detection-agent")
def overlap_detection(contractor_name: str, contractor_scope: str, internal_role: str) -> dict:
    """
    Compares contractor scope against internal job role descriptions.
    Maps to Capability 3: Overlap Detection.
    """
    response = llm.invoke(f"""
You are the Overlap Detection Agent for ContractOS.

Compare these two role descriptions and assess whether they overlap significantly,
which would indicate Oracle may be paying twice for the same work.
Return valid JSON only — no explanation, no markdown.

Contractor name: {contractor_name}
Contractor scope of work: {contractor_scope}
Internal employee role description: {internal_role}

Return JSON with:
- overlap_detected (boolean)
- overlap_score (number 0-100, where 100 = complete duplication)
- overlap_description (string, one sentence)
- estimated_monthly_duplicate_cost_eur (number, estimate if overlap detected, else 0)
- recommended_action (string: "no action" / "flag for HR review" / "escalate immediately")
- confidence (number 0-100)
""")
    try:
        return json.loads(response.content)
    except json.JSONDecodeError:
        return {"raw_output": response.content, "parse_error": True}


# ══════════════════════════════════════════════════════════════════════════════
# AGENT 4 — Compliance Flagging Agent
# Checks contracts against jurisdiction-specific rules
# ══════════════════════════════════════════════════════════════════════════════
@traceable(name="compliance-flagging-agent")
def compliance_flagging(contractor_name: str, contract_text: str, jurisdiction: str) -> dict:
    """
    Checks a contract against employment and data protection rules
    for the relevant jurisdiction. Maps to Capability 4: Compliance Flagging.
    """
    response = llm.invoke(f"""
You are the Compliance Flagging Agent for ContractOS.

Check this contractor agreement against employment and data protection rules
applicable in: {jurisdiction}.

Check for:
1. Misclassification risk — does this contractor look like an employee under local law?
   (Indicators: exclusivity, fixed hours, equipment provided by client, 
   integration into client's organisation)
2. Missing GDPR data processing clause
3. Ambiguous or absent IP assignment clause
4. Notice period below local legal minimum

Return valid JSON only — no explanation, no markdown.

Contractor: {contractor_name}
Contract:
{contract_text}

Return JSON with:
- status (string: "green" / "amber" / "red")
- flags (array of strings, each flag in one sentence)
- misclassification_risk (string: "low" / "medium" / "high")
- misclassification_reasoning (string, one sentence)
- gdpr_clause_present (boolean)
- ip_clause_clear (boolean)
- recommended_actions (array of strings)
- requires_legal_review (boolean)
""")
    try:
        return json.loads(response.content)
    except json.JSONDecodeError:
        return {"raw_output": response.content, "parse_error": True}


# ══════════════════════════════════════════════════════════════════════════════
# AGENT 5 — Cost Categorisation Agent
# Categorises payments by country, type, team, and intermediary
# ══════════════════════════════════════════════════════════════════════════════
@traceable(name="cost-categorisation-agent")
def cost_categorisation(payment_description: str) -> dict:
    """
    Categorises a payment entry for the cost dashboard.
    Maps to Capability 5: Cost Categorisation.
    """
    response = llm.invoke(f"""
You are the Cost Categorisation Agent for ContractOS.

Categorise this payment entry for Oracle Game Studio's cost dashboard.
Return valid JSON only — no explanation, no markdown.

Payment entry:
{payment_description}

Return JSON with:
- country (string)
- contract_type (string: "FTE" / "part-time" / "contractor" / "consultant" / 
  "intern" / "intermediary")
- team (string, infer from description)
- via_intermediary (boolean)
- intermediary_name (string or null)
- amount_eur (number, convert if needed — use approximate rates)
- currency_original (string)
- category (string: "engineering" / "design" / "QA" / "management" / 
  "legal" / "finance" / "unknown")
- confidence (number 0-100)
""")
    try:
        return json.loads(response.content)
    except json.JSONDecodeError:
        return {"raw_output": response.content, "parse_error": True}


# ══════════════════════════════════════════════════════════════════════════════
# SAMPLE DATA — realistic Oracle Game Studio scenarios
# ══════════════════════════════════════════════════════════════════════════════

SAMPLE_CONTRACT_1 = """
This freelance agreement is between Oracle GmbH (Munich) and Jana Novak, 
a backend engineer based in Prague, Czech Republic.
Rate: EUR 600 per day. Contract duration: 6 months, renewable.
Notice period: 14 days. Jana works exclusively for Oracle and follows 
Oracle's internal development processes. Equipment provided by Oracle.
All IP created under this contract is assigned to Oracle GmbH.
No data processing clause included.
"""

SAMPLE_CONTRACT_2 = """
Contractor agreement between Oracle Game Studio and Arjun Sharma, 
full-stack developer, Bangalore, India.
Rate: USD 45 per hour. Works 40 hours per week, Monday to Friday.
Integrated into Oracle's engineering Slack, attends daily standups.
Notice: 7 days. No IP assignment clause. No GDPR clause.
Uses Oracle's development tools and cloud infrastructure.
"""

SAMPLE_INVOICE_1 = """
Invoice #204
From: Jana Novak (Prague)
To: Oracle GmbH
Description: Backend API development, March 2025 — 18 working days
Amount: EUR 12,600
Payment due: 30 days
"""

SAMPLE_INVOICE_MISMATCH = """
Invoice #311
From: Raj Consulting Ltd (Mumbai)
To: Oracle Game Studio
Description: Mobile game QA testing, February 2025 — 22 days
Amount: USD 9,900
Note: rate adjustment applied per verbal agreement
Payment due: 15 days
"""

SAMPLE_INTERNAL_ROLE = """
Senior Backend Engineer — Payment Systems.
Responsibilities: design and maintain payment APIs, database optimisation,
code review for backend services, integration with third-party payment providers.
"""

SAMPLE_CONTRACTOR_SCOPE = """
Backend API development and database optimisation for payment module.
Code review for backend pull requests. Integration work with payment APIs.
"""

SAMPLE_PAYMENT = """
Wire transfer to TechStaff Philippines Inc — March 2025 monthly retainer.
Amount: PHP 480,000 (approx EUR 8,200).
Services: 3 x frontend developers, Manila office, game UI work.
Payment processed via local staffing agency.
"""


# ══════════════════════════════════════════════════════════════════════════════
# MAIN — run all five agents and print results
# ══════════════════════════════════════════════════════════════════════════════

def print_result(agent_name: str, result: dict) -> None:
    print(f"\n{'='*60}")
    print(f"  {agent_name}")
    print(f"{'='*60}")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    print("\nContractOS — LangSmith Demo")
    print("All traces will appear at: https://smith.langchain.com")
    print(f"Project: {os.getenv('LANGCHAIN_PROJECT')}\n")

    # Agent 1 — Contract Intelligence (clean contract)
    print("Running Agent 1 — Contract Intelligence (Jana Novak)...")
    r1 = contract_intelligence(SAMPLE_CONTRACT_1)
    print_result("Agent 1: Contract Intelligence — Jana Novak", r1)

    # Agent 2 — Invoice Validation (matching invoice)
    print("\nRunning Agent 2 — Invoice Validation (matching)...")
    r2 = invoice_validation(SAMPLE_INVOICE_1, "600", "EUR")
    print_result("Agent 2: Invoice Validation — Jana Invoice #204", r2)

    # Agent 2 — Invoice Validation (mismatched invoice)
    print("\nRunning Agent 2 — Invoice Validation (mismatch)...")
    r2b = invoice_validation(SAMPLE_INVOICE_MISMATCH, "400", "USD")
    print_result("Agent 2: Invoice Validation — Raj Consulting MISMATCH", r2b)

    # Agent 3 — Overlap Detection
    print("\nRunning Agent 3 — Overlap Detection...")
    r3 = overlap_detection(
        contractor_name="Jana Novak",
        contractor_scope=SAMPLE_CONTRACTOR_SCOPE,
        internal_role=SAMPLE_INTERNAL_ROLE
    )
    print_result("Agent 3: Overlap Detection — Jana vs Internal Engineer", r3)

    # Agent 4 — Compliance Flagging (high risk — Arjun)
    print("\nRunning Agent 4 — Compliance Flagging (Arjun Sharma — India/NL)...")
    r4 = compliance_flagging(
        contractor_name="Arjun Sharma",
        contract_text=SAMPLE_CONTRACT_2,
        jurisdiction="Netherlands / India"
    )
    print_result("Agent 4: Compliance Flagging — Arjun Sharma", r4)

    # Agent 5 — Cost Categorisation
    print("\nRunning Agent 5 — Cost Categorisation...")
    r5 = cost_categorisation(SAMPLE_PAYMENT)
    print_result("Agent 5: Cost Categorisation — TechStaff Philippines", r5)

    print("\n" + "="*60)
    print("  All agents complete.")
    print("  Go to https://smith.langchain.com to see all traces.")
    print("  Project: contractos-oracle-prod")
    print("="*60)
