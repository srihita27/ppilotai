from rag.college_rag.retriever import (
    get_college_retriever
)

retriever = get_college_retriever()

docs = retriever.invoke(
    "attendance"
)

print(
    "\nRETRIEVED:",
    len(docs)
)

for i, doc in enumerate(docs):

    print(
        f"\n===== DOC {i+1} ====="
    )

    print(
        doc.page_content[:500]
    )