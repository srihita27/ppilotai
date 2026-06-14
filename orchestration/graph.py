from langgraph.graph import (
    StateGraph,
    END
)

from agents.mcq_agent import (
    MCQAgent
)

from agents.student_agent import (
    StudentAgent
)

from typing import TypedDict


class GraphState(TypedDict):

    student_id: int

    subject: str

    difficulty: str

    context: str

    mcqs: list


student_agent = StudentAgent()

mcq_agent = MCQAgent()


def generate_node(state):

    weak_topics = (
        student_agent.get_weak_topics(
            state["student_id"],
            state["subject"]
        )
    )

    questions = (
        mcq_agent.generate(
            context=state["context"],
            difficulty=state["difficulty"],
            weak_topics=weak_topics
        )
    )

    state["mcqs"] = questions

    return state


builder = StateGraph(
    GraphState
)

builder.add_node(
    "generate",
    generate_node
)

builder.set_entry_point(
    "generate"
)

builder.add_edge(
    "generate",
    END
)

graph = builder.compile()