## Importing libraries and files
from crewai import Task
from agents import financial_analyst
from tools import FinancialDocumentTool


# Create ONE instance of the tool
financial_document_tool = FinancialDocumentTool()


# -----------------------------
# Financial Document Analysis
# -----------------------------
analyze_financial_document = Task(
    description="""
You are provided with a financial document located at: {file_path}

First, use the FinancialDocumentTool to read the document.

Then analyze the document based on the following user query:

User Query:
{query}

Your analysis must:
- Be strictly based on the document content
- Avoid making up data or assumptions
- Clearly reference financial metrics found in the document
- Provide structured insights
""",

    expected_output="""
Provide a structured financial analysis including:

1. Executive Summary
2. Key Financial Highlights
3. Profitability Analysis
4. Liquidity & Solvency Overview
5. Investment Insights
6. Identified Risks (based only on document data)

Do not fabricate numbers, URLs, or financial products.
""",

    agent=financial_analyst,
    tools=[financial_document_tool],
    async_execution=False,
)


# -----------------------------
# Investment Analysis Task
# -----------------------------
investment_analysis = Task(
    description="""
Using the financial document located at: {file_path},

Perform an investment-focused evaluation based on:

User Query:
{query}

Your response must:
- Use real financial figures from the document
- Interpret ratios correctly
- Avoid speculation beyond provided data
""",

    expected_output="""
Provide:

- Investment Strengths
- Potential Weaknesses
- Growth Indicators
- Valuation Considerations
- Final Investment Recommendation (Buy/Hold/Sell with reasoning)

Base all reasoning strictly on the financial document.
""",

    agent=financial_analyst,
    tools=[financial_document_tool],
    async_execution=False,
)


# -----------------------------
# Risk Assessment Task
# -----------------------------
risk_assessment = Task(
    description="""
Read the financial document located at: {file_path}.

Based on the document and the user's query:

{query}

Identify real financial risks including:
- Market risk
- Credit risk
- Liquidity risk
- Operational risk (if applicable)

Do not exaggerate or fabricate risks.
""",

    expected_output="""
Provide a structured risk assessment:

1. Key Risk Areas
2. Risk Severity Level (Low/Moderate/High)
3. Supporting Financial Indicators
4. Risk Mitigation Suggestions (realistic and practical)

Only use document-supported information.
""",

    agent=financial_analyst,
    tools=[financial_document_tool],
    async_execution=False,
)