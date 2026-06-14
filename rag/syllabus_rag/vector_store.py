import os

from langchain_community.vectorstores import (
    Chroma
)

from langchain_community.embeddings import (
    HuggingFaceEmbeddings
)

from langchain.text_splitter import (
    RecursiveCharacterTextSplitter
)


def create_vector_store(
    docs,
    pdf_name
):

    splitter = (
        RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
    )

    chunks = splitter.split_documents(
        docs
    )

    embeddings = (
        HuggingFaceEmbeddings(
            model_name=
            "sentence-transformers/all-MiniLM-L6-v2"
        )
    )

    persist_dir = os.path.join(
        "rag",
        "syllabus_rag",
        "chroma_db",
        pdf_name
    )

    Chroma.from_documents(
        chunks,
        embeddings,
        persist_directory=
        persist_dir
    )

    return persist_dir