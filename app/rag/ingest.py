from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    JSONLoader,
    WebBaseLoader
)
 
from langchain_text_splitters import RecursiveCharacterTextSplitter


def load_documents(path: str, file_type: str):
    if file_type == "pdf":
        loader = PyPDFLoader(path)

    elif file_type == "json":
        loader = JSONLoader(
            file_path=path,
            jq_schema=".[]",
            text_content=False
        )

    elif file_type == "web":
        loader = WebBaseLoader(path)

    elif file_type == "txt":
        loader = TextLoader(path)

    else:
        raise ValueError("Unsupported file type!")

    return loader.load()


def get_parent_splitter(
    chunk_size: int = 2000,
    chunk_overlap: int = 200
):
    return RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )


def get_child_splitter(
    chunk_size: int = 400,
    chunk_overlap: int = 60
):
    return RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )