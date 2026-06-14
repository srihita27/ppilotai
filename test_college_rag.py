from agents.college_agent import CollegeAgent

from rag.college_rag.retriever import (
    get_college_retriever
)


def main():

    print("\n========== GITAM COLLEGE ASSISTANT ==========\n")

    question = input(
        "Ask a question about GITAM: "
    )

    retriever = (
        get_college_retriever()
    )

    docs = retriever.invoke(
        question
    )

    print(
        f"\nRetrieved {len(docs)} document chunks.\n"
    )

    if len(docs) == 0:

        print(
            "No relevant information found in the vector database."
        )

        return

    print(
        "\n========== RETRIEVED CONTEXT ==========\n"
    )

    context = "\n\n".join(
        [
            doc.page_content
            for doc in docs
        ]
    )

    print(
        context[:2000]
    )

    print(
        "\n=======================================\n"
    )

    agent = CollegeAgent()

    answer = agent.answer(
        context,
        question
    )

    print(
        "\n========== ANSWER ==========\n"
    )

    print(answer)


if __name__ == "__main__":
    main()