from app.rag.ingest import load_documents
from app.rag.retriever import get_retriever

def seed():
    retriever = get_retriever()

    docs = []

    docs.extend(load_documents("knowledge/jobs.txt", "txt"))
    docs.extend(load_documents("knowledge/resume_samples.txt", "txt"))
    docs.extend(load_documents("knowledge/ats_keywords.txt", "txt"))

    retriever.add_documents(docs)

    print("Knowledge base indexed successfully.")


if __name__ == "__main__":
    seed()