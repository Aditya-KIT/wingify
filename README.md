# Financial Document Analyzer - Debug Assignment

## Project Overview
A comprehensive financial document analysis system that processes corporate reports, financial statements, and investment documents using AI-powered analysis agents.

## Getting Started

### Install Required Libraries
```sh
pip install -r requirement.txt
```

### Sample Document
The system analyzes financial documents like Tesla's Q2 2025 financial update.

**To add Tesla's financial document:**
1. Download the Tesla Q2 2025 update from: https://www.tesla.com/sites/default/files/downloads/TSLA-Q2-2025-Update.pdf
2. Save it as `data/sample.pdf` in the project directory
3. Or upload any financial PDF through the API endpoint

**Note:** Current `data/sample.pdf` is a placeholder - replace with actual Tesla financial document for proper testing.

# You're All Not Set!
🐛 **Debug Mode Activated!** The project has bugs waiting to be squashed - your mission is to fix them and bring it to life.

## Debugging Instructions

1. **Identify the Bug**: Carefully read the code in each file and understand the expected behavior. There is a bug in each line of code. So be careful.
2. **Fix the Bug**: Implement the necessary changes to fix the bug.
3. **Test the Fix**: Run the project and verify that the bug is resolved.
4. **Repeat**: Continue this process until all bugs are fixed.

## Expected Features
- Upload financial documents (PDF format)
- AI-powered financial analysis
- Investment recommendations
- Risk assessment
- Market insights

## Changes & Bug Fixes Implemented
## 1️⃣ Dependency & Environment Fixes
Changed requirement.txt → requirements.txt

## 2️⃣ agents.py Bug Fixes
llm = LLM(
    model="gemini/gemini-1.5-pro",
    api_key=os.getenv("GEMINI_API_KEY")
)
FinancialDocumentTool.read_data_tool

## 3️⃣ tools.py Bug Fixes
imported PyPDF dependencies & added Pypdf using import
Fixed incorrect crewai_tools import usage.

## 4️⃣ main.py Bug Fixes

## 5️⃣ task.py Improvements
Removed misleading instructions encouraging fake financial data.

## 6️⃣ Code Improvements

These all error are changed 

Incorrect tool registration in agents

Missing PDF reader dependency

API function naming conflicts

Improper dependency installation command

Incomplete file cleanup logic

Invalid imports in tools module

## .env file
.env file is added with api key of google generative API

## Update dependicies
Updated dependicies like pip, creaw ai
