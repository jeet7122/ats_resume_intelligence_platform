# ATS Resume Intelligence Platform

AI-powered Resume Optimization Platform that analyzes resumes against job descriptions, calculates ATS match scores, identifies missing skills, and generates recruiter-optimized resume improvements using LLMs and RAG pipelines.

## Overview

Hiring systems often reject strong candidates because resumes are not optimized for Applicant Tracking Systems (ATS).

This platform helps candidates improve resume-job fit through:

- Resume vs Job Description scoring
- Missing keyword detection
- Skill gap analysis
- AI-powered bullet point rewriting
- Resume summary optimization
- RAG-based job intelligence retrieval
- Structured recruiter-ready recommendations

---

## Key Features

### Resume Scanner
Upload a resume PDF + Job Description to receive:

- ATS Match Score
- Matched Skills
- Missing Keywords
- Improvement Suggestions

### AI Resume Optimizer

Uses Gemini AI + LangChain workflows to:

- Rewrite weak bullet points
- Improve action verbs
- Optimize summaries
- Add relevant technical keywords
- Improve ATS readability

### RAG Job Intelligence Engine

Retrieves relevant:

- Similar job descriptions
- Industry skill trends
- Resume best practices
- Role-specific keyword patterns

### Structured Outputs

Returns JSON responses for frontend dashboards and analytics systems.

---

## Tech Stack

### Backend

- Java
- Spring Boot
- Spring AI
- Python
- FastAPI

### AI / GenAI

- Gemini API
- LangChain
- Prompt Engineering
- RAG Pipelines
- ChromaDB
- Embeddings

### Database

- PostgreSQL

### DevOps / Tools

- Docker
- Postman
- Git

---

## System Architecture

```text
Frontend / Dashboard
        |
        v
Spring Boot API Gateway
        |
 -------------------------
 |                       |
FastAPI Scanner Service   AI Optimization Service
 |                       |
Keyword Engine        Gemini + LangChain
 |
ChromaDB RAG Layer
 |
PostgreSQL
```

## API Endpoints
### Resume Scan
```http
POST /scan
```

### Body
```json
Form Data:

resume (PDF)
jd (Job Description)
```

### AI Optimization

```http
POST /optimize
```

### Body
```json
{
  "resume_text": "...",
  "jd": "..."
}
```

### Example Output

```json
{
  "score": 87,
  "matched_keywords": ["Java", "Spring Boot", "SQL"],
  "missing_keywords": ["Docker", "AWS"],
  "suggestions": [
    "Add Docker experience",
    "Mention AWS deployment work"
  ]
}
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


