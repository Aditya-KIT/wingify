## Importing libraries
import os
from dotenv import load_dotenv
from typing import Type
from pydantic import BaseModel
from crewai.tools import BaseTool
import PyPDF2

load_dotenv()


# ==============================
# PDF INPUT SCHEMA
# ==============================

class FinancialDocumentInput(BaseModel):
    file_path: str


# ==============================
# PDF READER TOOL
# ==============================

class FinancialDocumentTool(BaseTool):
    name: str = "Financial Document Reader"
    description: str = "Reads and extracts cleaned text from a financial PDF document."
    args_schema: Type[BaseModel] = FinancialDocumentInput

    def _run(self, file_path: str) -> str:
        """Reads and cleans data from a PDF file"""

        # Get absolute project path
        base_dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.join(base_dir, file_path)

        if not os.path.exists(full_path):
            return f"Error: File not found at {full_path}"

        full_report = ""

        try:
            with open(full_path, "rb") as file:
                reader = PyPDF2.PdfReader(file)

                for page in reader.pages:
                    content = page.extract_text()
                    if content:
                        content = content.replace("\n\n", "\n").strip()
                        full_report += content + "\n"

        except Exception as e:
            return f"Error reading PDF: {str(e)}"

        return full_report


# ==============================
# INVESTMENT ANALYSIS TOOL
# ==============================

class InvestmentToolInput(BaseModel):
    financial_document_data: str


class InvestmentTool(BaseTool):
    name: str = "Investment Analysis Tool"
    description: str = "Analyzes financial document data for investment insights."
    args_schema: Type[BaseModel] = InvestmentToolInput

    def _run(self, financial_document_data: str) -> str:
        if not financial_document_data:
            return "No financial data provided."

        processed_data = " ".join(financial_document_data.split())

        return "Investment analysis functionality to be implemented."


# ==============================
# RISK ASSESSMENT TOOL
# ==============================

class RiskToolInput(BaseModel):
    financial_document_data: str


class RiskTool(BaseTool):
    name: str = "Risk Assessment Tool"
    description: str = "Performs risk assessment on financial data."
    args_schema: Type[BaseModel] = RiskToolInput

    def _run(self, financial_document_data: str) -> str:
        if not financial_document_data:
            return "No financial data provided."

        return "Risk assessment functionality to be implemented."