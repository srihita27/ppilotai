import os
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


PDF_PATH = "rag/college_rag/gitam_faq.pdf"
DB_PATH = "rag/college_rag/chroma_db"


def build_vector_db():
    print("Loading PDF...")

    loader = PyPDFLoader(PDF_PATH)
    docs = loader.load()

    print(f"Total pages loaded: {len(docs)}")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(docs)

    print(f"Total chunks: {len(chunks)}")

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    print("Creating vector DB...")

    db = Chroma.from_documents(
        chunks,
        embeddings,
        persist_directory=DB_PATH
    )

    db.persist()

    print("Vector DB built successfully!")
    print("Vector count:", db._collection.count())


if __name__ == "__main__":
    build_vector_db()