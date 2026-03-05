from fastapi import FastAPI, File, UploadFile, Form, HTTPException
import os
import uuid
import asyncio
import traceback
from dotenv import load_dotenv

# ===============================
# Load Environment Variables FIRST
# ===============================
load_dotenv()

# Debug check (remove later if you want)
print("GEMINI_API_KEY Loaded:", os.getenv("GEMINI_API_KEY"))

if not os.getenv("GEMINI_API_KEY"):
    raise ValueError("GEMINI_API_KEY is not set. Check your .env file.")

from crewai import Crew, Process
from agents import financial_analyst
from task import analyze_financial_document

app = FastAPI(title="Financial Document Analyzer")


# ===============================
# Crew Runner
# ===============================
def run_crew(query: str, file_path: str):
    """Run the CrewAI workflow"""
    try:
        financial_crew = Crew(
            agents=[financial_analyst],
            tasks=[analyze_financial_document],
            process=Process.sequential,
            verbose=True
        )

        result = financial_crew.kickoff(
            inputs={
                "query": query,
                "file_path": file_path
            }
        )

        return result

    except Exception as e:
        print("\n========== FULL CREW ERROR ==========")
        traceback.print_exc()
        print("=====================================\n")
        raise e


# ===============================
# Health Check
# ===============================
@app.get("/")
async def root():
    return {"message": "Financial Document Analyzer API is running"}


# ===============================
# Analyze Endpoint
# ===============================
@app.post("/analyze")
async def analyze_financial_document_endpoint(
    file: UploadFile = File(...),
    query: str = Form(default="Analyze this financial document for investment insights")
):
    file_id = str(uuid.uuid4())
    file_path = f"data/financial_document_{file_id}.pdf"

    try:
        os.makedirs("data", exist_ok=True)

        # Save uploaded file
        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)

        if not query:
            query = "Analyze this financial document for investment insights"

        # Run Crew in separate thread
        response = await asyncio.to_thread(
            run_crew,
            query.strip(),
            file_path
        )

        return {
            "status": "success",
            "analysis": str(response),
            "file_processed": file.filename
        }

    except Exception as e:
        print("\n========== API ERROR ==========")
        traceback.print_exc()
        print("================================\n")

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

    finally:
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
            except Exception:
                pass


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)