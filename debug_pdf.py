from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(
    "rag/college_rag/gitam_faq.pdf"
)

docs = loader.load()

print("Total Pages:", len(docs))

print("\n========== PAGE 1 ==========\n")

print(docs[0].page_content[:3000])