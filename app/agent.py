from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from app.prompts import resume_optimizer_prompt
from app.rag.retriever import retrieve_context
import json

load_dotenv()

LLM = ChatGoogleGenerativeAI(
    model = "gemini-3-flash-preview",
    temperature=0.2
)

def optimize_resume(resume: str, jd: str):
    query = f"{jd}\n{resume}"
    context = retrieve_context(query)
    prompt = resume_optimizer_prompt.format(
        resume=resume,
        jd=jd,
        context=context
    )
    
    response = LLM.invoke(prompt)
    
    content = response.content
    
    if isinstance(content, list):
        text = "".join(
            block["text"]
            for block in content
            if isinstance(block, dict) and block.get("type") == "text"
        )
    else:
        text = str(content)
        
    return json.loads(text)