from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain_classic.storage import LocalFileStore
from langchain_classic.storage._lc_store import create_kv_docstore
from langchain_classic.retrievers import ParentDocumentRetriever
import os
from app.rag.ingest import (
    get_parent_splitter,
    get_child_splitter
)


load_dotenv()

DB_PATH = "chroma_db"
DOCSTORE_PATH = "parent_docs"

os.makedirs(DB_PATH, exist_ok=True)
os.makedirs(DOCSTORE_PATH, exist_ok=True)

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2"
)

def get_vectorstore():
    return Chroma(
        collection_name="ats_docs",
        persist_directory=DB_PATH,
        embedding_function=embeddings
    )

def get_docstore():
    fs = LocalFileStore(DOCSTORE_PATH)
    return create_kv_docstore(fs)


def get_retriever():
    retriever = ParentDocumentRetriever(
        vectorstore=get_vectorstore(),
        docstore=get_docstore(),
        parent_splitter=get_parent_splitter(),
        child_splitter=get_child_splitter()
    )
    
    return retriever

    



