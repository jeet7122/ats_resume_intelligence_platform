from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.parser import extract_text_from_pdf
from app.scorer import scan_resume
from app.agent import optimize_resume

import uuid
import os


app = FastAPI(title="ATS AI Resume Analyzer")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/analyze")
async def analyze(
    resume: UploadFile = File(...),
    jd: str = Form(...)
):
    temp_filename = f"temp_{uuid.uuid4()}.pdf"

    try:
        # Save uploaded PDF
        contents = await resume.read()

        with open(temp_filename, "wb") as f:
            f.write(contents)

        # Extract text
        resume_text = extract_text_from_pdf(temp_filename)

        # Deterministic ATS Scan
        score_result = scan_resume(resume_text, jd)

        # AI Optimization
        ai_result = optimize_resume(resume_text, jd)

        # Merge missing keywords
        scan_missing = score_result.get("missing_keywords", [])
        ai_missing = ai_result.get("missing_keywords", [])

        merged_missing = list({
            item.lower(): item
            for item in scan_missing + ai_missing
        }.values())

        score_result["missing_keywords"] = merged_missing

        # Better suggestions merge
        score_result["suggestions"] = (
            score_result.get("suggestions", []) +
            ai_result.get("suggestions", [])[:3]
        )

        return {
            "success": True,
            "resume_filename": resume.filename,
            "resume_text": resume_text,
            "scan_result": score_result,
            "optimization_result": ai_result
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

    finally:
        if os.path.exists(temp_filename):
            os.remove(temp_filename)