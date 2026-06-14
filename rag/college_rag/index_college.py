from langchain_community.document_loaders import (
    PyPDFLoader
)

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

from vector_store import (
    create_college_vector_store
)

loader = PyPDFLoader(
    "rag/college_rag/gitam_faq.pdf"
)

docs = loader.load()

splitter = (
    RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
)

chunks = splitter.split_documents(
    docs
)

create_college_vector_store(
    chunks
)

print(
    "College RAG Indexed!"
)