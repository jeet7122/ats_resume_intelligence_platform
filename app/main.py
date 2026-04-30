from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.parser import extract_text_from_pdf
from app.scorer import scan_resume
from app.agent import optimize_resume
import uuid
import json
import os


app = FastAPI(title="ATS AI Resume Analyzer")


@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/scan")
async def scan(
    resume: UploadFile = File(...),
    jd: str = Form(...)
    ): 
    text = await resume.read()
    with open("temp.pdf", "wb") as f:
        f.write(text)
    
    resume_text = extract_text_from_pdf("temp.pdf")
    result = scan_resume(resume_text, jd)
    return result

@app.post("/optimize")
async def optimize(
    resume: str = Form(...),
    jd: str = Form(...)
):
    result = optimize_resume(resume, jd)
    return {"result" : result}


@app.post("/analyze")
async def analyze(
    resume: UploadFile = File(...),
    jd: str = Form(...)
):
    temp_filename = f"temp_{uuid.uuid4()}.pdf"
    
    try:
        contents = await resume.read()
        
        with open(temp_filename, "wb") as f:
            f.write(contents)
        
        resume_text = extract_text_from_pdf(temp_filename)
        score_result = scan_resume(resume_text, jd)
        
        ai_result = optimize_resume(resume_text, jd)
        try:
            ai_result = json.loads(ai_result)
        except:
            ai_result = {"raw_response": ai_result}
        return{
            "success": True,
            "resume_filename": resume.filename,
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

    