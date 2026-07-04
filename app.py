import pandas as pd
import plotly.express as px
import os

from rag.college_rag.vector_store import build_vector_db
import os
from agents.sql_chat_agent import ask_database, explain_result
if not os.path.exists("rag/college_rag/chroma_db"):
    build_vector_db()

from rag.syllabus_rag.pdf_loader import (
    load_pdf
)

from orchestration.graph import (
    graph
)

import streamlit as st

from agents.student_agent import StudentAgent

from analytics.sql_agent import (
    SQLAgent
)

from agents.college_agent import ask_college_question

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "student_id" not in st.session_state:
    st.session_state.student_id = None

if "student_name" not in st.session_state:
    st.session_state.student_name = None

# PAGE CONFIG

st.set_page_config(
    page_title="PrepPilot AI",
    page_icon="assets/favicon.png",
    layout="wide"
)

st.markdown(
    """
    <style>

    .main {
        background-color: #0f172a;
    }

    [data-testid="stMetric"] {
        background: white;
        border-radius: 15px;
        padding: 20px;
        border: 1px solid #e2e8f0;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
    }

    [data-testid="stMetricLabel"] {
        font-size: 15px;
        font-weight: 600;
    }

    [data-testid="stMetricValue"] {
        font-size: 28px;
        font-weight: bold;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    </style>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns([2, 8])

with col1:
    st.image(
        "assets/favicon.png",
        use_container_width=True
    )

with col2:
    st.title(
        "PrepPilot AI"
    )

    st.caption(
        "AI-Powered Learning, Assessment & Analytics Platform"
    )
# st.image(
#     "assets/banner.png",
#     use_container_width=True
# )
# st.image(
#     "assets/mainlogo.png",
#     width=100
# )

# LOAD AGENTS

student_agent = StudentAgent()

sql_agent = SQLAgent()

# STUDENT SELECTION

# students = student_agent.get_all_students()

# student_options = {
#     f"{s['name']} (ID: {s['student_id']})":
#     s["student_id"]
#     for s in students
# }

# selected_student = st.selectbox(
#     "Select Student",
#     list(student_options.keys())
# )

# student_id = student_options[
#     selected_student
# ]

with st.sidebar:

    st.image(
        "assets/mainlogo.png",
        width=120
    )

    st.markdown(
        """
        <h2 style='margin-top:-10px;'>
        PrepPilot AI
        </h2>
        """,
        unsafe_allow_html=True
    )

    st.success(
        f"👋 {st.session_state.student_name}"
    )

    # st.info(
    #     f"Student ID: {student_id}"
    # )

    st.divider()

    st.markdown(
        "### 🚀 Navigation"
    )

    st.markdown(
        """
        - 🏫 College Assistant
        - 📚 Test Preparation
        - 📊 Student Analytics
        - 💬 SQL Assistant
        """
    )

    st.divider()

    if st.button(
        "🚪 Logout"
    ):

        st.session_state.clear()

        st.rerun()

# LOGIN

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:

    st.title("🎓 PrepPilot Login")

    login_id = st.number_input(
        "Student ID",
        min_value=1,
        step=1
    )

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        student = student_agent.login(
            login_id,
            password
        )

        if student:

            st.session_state.logged_in = True

            st.session_state.student_id = (
                student["student_id"]
            )

            st.session_state.student_name = (
                student["name"]
            )

            st.rerun()

        else:

            st.error(
                "Invalid Credentials"
            )

    st.stop()

# USER IS LOGGED IN
student_id = st.session_state.student_id

st.success(
    f"👋 Welcome back, {st.session_state.student_name}"
)
st.divider()


# TABS

tab1, tab2, tab3, tab4 = st.tabs(
[
    "🏫 College Assistant",
    "📚 Test Preparation",
    "📊 Student Analytics",
    "💬 SQL Assistant"
]
)


# COLLEGE ASSISTANT

from rag.college_rag.retriever import get_college_retriever

# Initialize once (outside tab, at top of file with other agents)
college_retriever = get_college_retriever()

with tab1:
    st.header("🏫 GITAM College Assistant")
    question = st.chat_input("Ask anything about GITAM...")

    if question:

        with st.chat_message("user"):
            st.write(question)

        with st.spinner("Searching..."):

            docs = college_retriever.invoke(
                question
            )

            context = "\n\n".join(
                [
                    doc.page_content
                    for doc in docs
                ]
            )

            answer = ask_college_question(
                context,
                question
            )

        with st.chat_message("assistant"):

            st.write(answer)

            st.divider()

            st.subheader("📚 Sources")

            for i, doc in enumerate(docs, start=1):

                source = doc.metadata.get(
                    "source",
                    "Unknown Source"
                )

                page = doc.metadata.get(
                    "page",
                    None
                )

                title = (
                    f"📄 {source}"
                    if page is None
                    else f"📄 {source} (Page {page + 1})"
                )

                with st.expander(title):

                    st.write(
                        doc.page_content
                    )
# TEST PREPARATION

with tab2:

    st.header(
        "📚 AI Test Preparation"
    )

    difficulty = st.selectbox(
        "Difficulty",
        [
            "Easy",
            "Medium",
            "Hard"
        ]
    )

    pdf = st.file_uploader(
        "Upload Syllabus PDF",
        type=["pdf"]
    )

    if st.button(
        "Generate Test"
    ):

        if pdf is None:

            st.error(
                "Please upload a syllabus PDF."
            )

        else:

            os.makedirs(
                "uploads",
                exist_ok=True
            )

            file_path = os.path.join(
                "uploads",
                pdf.name
            )

            with open(
                file_path,
                "wb"
            ) as f:

                f.write(
                    pdf.getbuffer()
                )

            with st.spinner(
                "Processing syllabus..."
            ):

                docs = load_pdf(
                    file_path
                )

                context = "\n".join(
                    [
                        doc.page_content
                        for doc in docs[:10]
                    ]
                )

                result = graph.invoke(
                    {
                        "student_id":
                        student_id,

                        "subject":
                        pdf.name,

                        "difficulty":
                        difficulty,

                        "context":
                        context
                    }
                )

            st.session_state[
                "questions"
            ] = result["mcqs"]

            st.session_state[
                "results"
            ] = {}

            st.success(
                "Test Generated Successfully!"
            )


# STUDENT ANALYTICS

with tab3:

    st.header(
        "📊 Student Analytics Dashboard"
    )

    st.info(
    """
🚀 Personalized insights generated from student performance data.

View rankings, identify weak subjects,
track progress, and receive AI-powered recommendations.
"""
)

    # KPI Cards
    rank = sql_agent.get_rank(
        student_id
    )

    avg_score = (
        sql_agent.get_average_score(
            student_id
        )
    )

    class_avg = (
        sql_agent.get_class_average()
    )

    top_name, top_score = (
        sql_agent.get_top_student()
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "🏆 Rank",
        rank
    )

    col2.metric(
        "🎯 Average",
        f"{round(avg_score,2)}/100"
    )

    col3.metric(
        "📚 Class Average",
        f"{round(class_avg,2)}/100"
    )

    col4.metric(
        "⭐ Top Score",
        f"{top_score}%"
    )

    st.divider()

    st.subheader(
        "🤖 Recommended Difficulty"
    )

    recommendation = (
        student_agent
        .suggest_difficulty(
            student_id
        )
    )

    if recommendation == "Easy":

        st.info(
            "🟢 Easy"
        )

    elif recommendation == "Medium":

        st.warning(
            "🟡 Medium"
        )

    else:

        st.error(
            "🔴 Hard"
        )

    st.divider()

    st.subheader(
        "📉 Weak Subjects"
    )

    weak_subjects = (
        sql_agent.get_weak_subjects(
            student_id
        )
    )

    if weak_subjects:

        df = pd.DataFrame(
            weak_subjects,
            columns=[
                "Subject",
                "Score"
            ]
        )

        df["Score"] = pd.to_numeric(df["Score"],errors="coerce")
        df["Performance"] = df["Score"]

        df["Status"] = df[
            "Score"
            ].apply(
                lambda x:
                "🔴 Critical"
                if x < 50
                else "🟠 Improve"
            )

        st.dataframe(
            df,
            column_config={
                "Performance":
                st.column_config.ProgressColumn(
                    "Performance",
                    min_value=0,
                    max_value=100,
                    format="%d"
                )
            },
            use_container_width=True
        )

    else:

        st.success(
            "🎉 No weak subjects found"
        )

    st.divider()

with tab4:

    st.markdown("## 🤖 PrepPilot AI")
    st.caption("Ask questions about your academic performance in natural language.")

    question = st.chat_input(
        "Ask about your academic performance..."
    )

    if question:

        with st.chat_message("user"):
            st.write(question)

        with st.spinner("🤖 Thinking..."):

            sql, columns, rows = ask_database(
                question,
                student_id
            )

            if columns:

                import pandas as pd
                import plotly.express as px

                df = pd.DataFrame(
                    rows,
                    columns=columns
                )

                explanation = explain_result(
                    question,
                    sql,
                    rows
                )

        if columns:

            with st.chat_message("assistant"):

                st.markdown("## 🤖 PrepPilot AI")

                st.markdown(explanation)

                st.divider()

                col1, col2 = st.columns(2)

                with col1:
                    st.metric(
                        "Results Found",
                        len(df)
                    )

                with col2:

                    if len(df.columns) == 2:

                        try:

                            st.metric(
                                "Highest Value",
                                round(df.iloc[:, 1].max(), 2)
                            )

                        except Exception:

                            st.metric(
                                "Columns",
                                len(df.columns)
                            )

                st.divider()

                st.subheader("📊 Results")

                st.dataframe(
                    df,
                    use_container_width=True,
                    hide_index=True
                )

                # Automatic chart
                if len(df.columns) == 2:

                    fig = px.bar(
                        df,
                        x=df.columns[0],
                        y=df.columns[1],
                        text=df.columns[1],
                        title="Result Visualization"
                    )

                    fig.update_layout(
                        template="plotly_white",
                        height=420,
                        showlegend=False,
                        margin=dict(
                            l=20,
                            r=20,
                            t=50,
                            b=20
                        )
                    )

                    fig.update_traces(
                        textposition="outside"
                    )

                    st.plotly_chart(
                        fig,
                        use_container_width=True
                    )

                st.divider()

                with st.expander("🧠 How did I answer this?"):

                    st.markdown("#### Generated SQL")

                    st.code(
                        sql,
                        language="sql"
                    )

        else:

            with st.chat_message("assistant"):
                st.error(rows)

st.subheader(
    "📈 Subject Performance"
)

subject_scores = (
    sql_agent.get_subject_scores(
        student_id
    )
)

chart_df = pd.DataFrame(
    subject_scores,
    columns=[
        "Subject",
        "Score"
    ]
)

fig = px.bar(
    chart_df,
    x="Subject",
    y="Score",
    title="Performance by Subject"
)

fig.update_layout(
    height=500
)

st.plotly_chart(
    fig,
    use_container_width=True
)


# DISPLAY GENERATED TEST

if "questions" in st.session_state:

    questions = st.session_state["questions"]

    st.divider()

    st.header(
        "📝 Generated Test"
    )

    if "results" not in st.session_state:

        st.session_state["results"] = {}

    score = 0

    for i, q in enumerate(questions):

        st.subheader(
            f"Question {i + 1}"
        )

        answer = st.radio(
            q["question"],
            list(q["options"].keys()),
            format_func=lambda x:
            f"{x}. {q['options'][x]}",
            key=f"q{i}",
            index=None
        )

        if st.button(
            f"Check Answer {i + 1}",
            key=f"check{i}"
        ):

            if answer is None:

                st.session_state["results"][i] = {
                    "status": "unanswered"
                }

            elif answer == q["correct"]:

                st.session_state["results"][i] = {
                    "status": "correct",
                    "selected": answer
                }

            else:

                st.session_state["results"][i] = {
                    "status": "wrong",
                    "selected": answer
                }

        if i in st.session_state["results"]:

            result = st.session_state["results"][i]

            if result["status"] == "correct":

                score += 1

                st.success(
                    "✅ Correct Answer"
                )

                st.write(
                    f"Your Answer: "
                    f"{result['selected']}. "
                    f"{q['options'][result['selected']]}"
                )

                st.info(
                    q["explanation"]
                )

            elif result["status"] == "wrong":

                st.error(
                    "❌ Wrong Answer"
                )

                st.write(
                    f"Your Answer: "
                    f"{result['selected']}. "
                    f"{q['options'][result['selected']]}"
                )

                st.write(
                    f"Correct Answer: "
                    f"{q['correct']}. "
                    f"{q['options'][q['correct']]}"
                )

                st.info(
                    q["explanation"]
                )

            else:

                st.warning(
                    "⚠️ Please select an option first."
                )

        st.divider()

    percentage = round(
        (
            score / len(questions)
        ) * 100,
        2
    )

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "🎯 Score",
            f"{score}/{len(questions)}"
        )

    with col2:

        st.metric(
            "📈 Percentage",
            f"{percentage}%"
        )

st.divider()

st.caption(
    "PrepPilot AI • College Assistant • Analytics • Test Preparation"
)