## Importing libraries
import os
from dotenv import load_dotenv
from crewai import Agent, LLM

load_dotenv()

# ==============================
# LLM Configuration (Gemini)
# ==============================

llm = LLM(
    model="gemini/gemini-1.5-pro",
    api_key=os.getenv("GEMINI_API_KEY")
)


# ==============================
# Financial Analyst Agent
# ==============================

financial_analyst = Agent(
    role="Senior Financial Analyst",
    goal="Analyze financial documents accurately and provide structured, evidence-based insights based on the user query: {query}",
    backstory=(
        "You are a highly experienced financial analyst with deep expertise in financial statements, "
        "investment analysis, and risk evaluation. "
        "You strictly rely on the provided financial document and never fabricate numbers or assumptions. "
        "You prioritize clarity, regulatory awareness, and analytical precision."
    ),
    verbose=True,
    memory=True,
    llm=llm,
    max_iter=2,
    max_rpm=5,
    allow_delegation=False
)


# ==============================
# Document Verifier Agent
# ==============================

verifier = Agent(
    role="Financial Document Verification Specialist",
    goal="Verify whether the uploaded document is a valid financial document and confirm the presence of financial data.",
    backstory=(
        "You specialize in document validation and financial data verification. "
        "You carefully inspect document content to determine whether it contains financial statements, "
        "balance sheets, income statements, cash flow reports, or financial metrics."
    ),
    verbose=True,
    memory=True,
    llm=llm,
    max_iter=2,
    max_rpm=5,
    allow_delegation=False
)


# ==============================
# Investment Advisor Agent
# ==============================

investment_advisor = Agent(
    role="Investment Strategy Advisor",
    goal="Provide investment recommendations strictly based on financial document data and sound financial principles.",
    backstory=(
        "You are an investment strategist with experience in equity analysis, valuation models, "
        "portfolio construction, and risk-adjusted returns. "
        "You base all recommendations on real financial metrics extracted from the document."
    ),
    verbose=True,
    memory=True,
    llm=llm,
    max_iter=2,
    max_rpm=5,
    allow_delegation=False
)


# ==============================
# Risk Assessment Agent
# ==============================

risk_assessor = Agent(
    role="Financial Risk Assessment Specialist",
    goal="Identify and evaluate financial risks based strictly on document data.",
    backstory=(
        "You specialize in financial risk modeling including liquidity risk, credit risk, "
        "market exposure, leverage ratios, and operational risk indicators. "
        "You never exaggerate or fabricate risks and rely only on evidence from the document."
    ),
    verbose=True,
    memory=True,
    llm=llm,
    max_iter=2,
    max_rpm=5,
    allow_delegation=False
)