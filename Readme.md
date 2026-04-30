# ATS Resume Intelligence Platform

AI-powered Resume Optimization Platform that analyzes resumes against job descriptions, calculates ATS match scores, identifies missing skills, and generates recruiter-optimized resume improvements using LLMs and Retrieval-Augmented Generation (RAG).

---

## 🚀 Overview

Many strong candidates get filtered out by Applicant Tracking Systems (ATS) because resumes are poorly optimized for keyword relevance, formatting, or role alignment.

This platform helps candidates improve resume-job fit using AI + search systems.

## Core Capabilities

- Resume vs Job Description ATS scoring
- Missing keyword detection
- Skill gap analysis
- AI-powered bullet point rewriting
- Professional summary optimization
- RAG-based hiring intelligence retrieval
- Structured JSON outputs for frontend dashboards

---

#$ ✨ Features

##$ 📄 Resume Scanner

Upload a resume PDF + job description to receive:

- ATS Match Score
- Matched Keywords
- Missing Skills
- Improvement Suggestions

---

### 🤖 AI Resume Optimizer

Uses Gemini + LangChain workflows to:

- Rewrite weak bullet points
- Improve action verbs
- Optimize professional summaries
- Inject relevant technical keywords
- Improve recruiter readability

---

### 🧠 RAG Hiring Intelligence Engine

Retrieves relevant context such as:

- Similar job descriptions
- Industry skill trends
- Resume best practices
- Role-specific keyword patterns

---

### 📊 Structured Outputs

Returns clean JSON responses for:

- React dashboards
- Analytics systems
- Resume builder UIs
- Career coaching tools

---

## 🛠 Tech Stack

### Backend

- Python
- FastAPI

### AI / GenAI

- Gemini API
- LangChain
- Prompt Engineering
- RAG Pipelines
- ChromaDB
- Vector Embeddings

### Data Layer

- Chroma Vector Database
- LocalFileStore (Parent Document Storage)

### Tools / DevOps

- Git
- Postman
- Docker (planned)

---

## 🏗 System Architecture

```text
User Uploads Resume + JD
          |
          v
      FastAPI Backend
          |
  ---------------------
  |                   |
  v                   v
ATS Scanner      AI Optimizer
(Keyword Engine) (Gemini LLM)
  |                   |
  -----------|---------
             v
      RAG Retriever
   (Chroma + Parent Docs)
            |
            v
    Hiring Intelligence Data
```
## API Endpoints

### Analyze Resume (Main Endpoint)
```http
POST /analyze
```

### Body
```json
Form Data
  resume: PDF_File,
  jd: Text
```

### Example Output

```json
{
  "success": true,
  "resume_filename": "resume.pdf",
  "scan_result": {
    "score": 92,
    "matched_keywords": [
      "java",
      "spring boot",
      "python"
    ],
    "missing_keywords": [
      "react"
    ],
    "suggestions": [
      "Add React experience"
    ]
  },
  "optimization_result": {
    "summary": "Backend engineer specializing in scalable Java systems...",
    "missing_keywords": [
      "React",
      "PostgreSQL"
    ],
    "improved_bullets": [
      "...",
      "..."
    ],
    "suggestions": [
      "...",
      "..."
    ]
  }
}
```

## 🧠 How It Works
Resume PDF
→ Text Extraction
→ ATS Keyword Scoring
→ Semantic Retrieval (RAG)
→ Gemini Resume Optimization
→ Structured Output

## 📁 Project Structure
```
app/
├── main.py
├── parser.py
├── scorer.py
├── skills.py
├── agent.py
├── prompts.py
└── rag/
    ├── ingest.py
    ├── vectorstore.py
    └── retriever.py
```

## Future Roadmap
* Resume PDF export
* LinkedIn profile scoring
* Real recruiter feedback simulation
* Multi-language resume support
* Live job scraping
* Vector recommendation engine
* Dashboard analytics

---

## Author

#### Jeet Thakkar

GitHub: https://github.com/jeet7122

Portfolio: https://jeet7122.github.io


