import os
import sqlite3
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatGroq(
    model_name="llama-3.3-70b-versatile",
    groq_api_key=os.getenv("GROQ_API_KEY")
)

conn = sqlite3.connect(
    "database/students.db",
    check_same_thread=False
)


def ask_database(question, student_id):

    schema = """
Table: students

student_id INTEGER
name TEXT
avg_score REAL

----------------------------------

Table: performance

student_id INTEGER
subject TEXT
score REAL
"""

    prompt = ChatPromptTemplate.from_template(
"""
You are an expert SQLite assistant.

Database Schema

{schema}

Rules:

1. Generate ONLY SQLite SELECT queries.

2. Never generate:
- INSERT
- UPDATE
- DELETE
- DROP
- ALTER
- CREATE
- PRAGMA
- ATTACH

3. Unless the user explicitly asks about the whole class,
always restrict queries using

student_id = {student_id}

4. "Weak subjects" means subjects with the LOWEST average score,
NOT subjects below overall average.

Example:

SELECT subject,
AVG(score) AS average_score
FROM performance
WHERE student_id={student_id}
GROUP BY subject
ORDER BY average_score ASC;

5. "Strong subjects" means highest average score.

6. "Average score" means AVG(score).

7. "Top subjects" means ORDER BY AVG(score) DESC.

8. Return ONLY SQL.

Question:

{question}
"""
    )

    sql = llm.invoke(
        prompt.format(
            schema=schema,
            question=question,
            student_id=student_id
        )
    ).content.strip()

    sql = sql.replace("```sql", "")
    sql = sql.replace("```", "")
    sql = sql.strip()

    if not sql.upper().startswith("SELECT"):

        return None, None, "Unsafe SQL rejected."

    blocked = [
        "INSERT",
        "UPDATE",
        "DELETE",
        "DROP",
        "ALTER",
        "CREATE",
        "PRAGMA",
        "ATTACH"
    ]

    if any(word in sql.upper() for word in blocked):

        return None, None, "Unsafe SQL rejected."

    try:

        cursor = conn.execute(sql)

        columns = [i[0] for i in cursor.description]

        rows = cursor.fetchall()

        return sql, columns, rows

    except Exception as e:

        return sql, None, str(e)


def explain_result(question, sql, rows):

    prompt = f"""
You are an academic advisor.

Student Question:

{question}

SQL Query:

{sql}

Query Result:

{rows}

Explain the result in simple English.

If the result is about weak subjects,
recommend which subject the student
should prioritize.

Keep the response under 120 words.
"""

    return llm.invoke(prompt).content