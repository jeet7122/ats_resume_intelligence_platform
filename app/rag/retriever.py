from app.rag.vectorstore import get_retriever


def retrieve_context(query: str, k: int = 4):
    retriever = get_retriever()
    docs = retriever.invoke(query)
    if not docs:
        return ""
    top_docs = docs[:k]
    ctx = "\n\n".join(doc.page_content for doc in top_docs)
    return ctx