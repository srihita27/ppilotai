import sqlite3
import pandas as pd
import os

DB_PATH = "database/students.db"

# ALWAYS rebuild DB on startup (important for Streamlit Cloud)
conn = sqlite3.connect(DB_PATH)

students = pd.read_csv("database/students.csv")
performance = pd.read_csv("database/performance.csv")

students.to_sql("students", conn, if_exists="replace", index=False)
performance.to_sql("performance", conn, if_exists="replace", index=False)

conn.commit()
conn.close()

class SQLAgent:

    def __init__(self):

        self.conn = sqlite3.connect(
            DB_PATH,
            check_same_thread=False
        )

    def get_rank(
        self,
        student_id
    ):

        rows = self.conn.execute("""
                                 SELECT student_id,
           AVG(score) as avg_score
    FROM performance
    GROUP BY student_id
    ORDER BY avg_score DESC
""").fetchall()

        rank = 1

        for row in rows:

            if row[0] == student_id:

                return rank

            rank += 1

        return None

    def get_average_score(self, student_id):
        result = self.conn.execute(
        """
        SELECT AVG(score)
        FROM performance
        WHERE student_id=?
        """,
        (student_id,)
    ).fetchone()
        return round(result[0], 2)  # raw avg marks out of 100

    def get_top_student(self):
        return self.conn.execute("""
                                 SELECT s.name,
           AVG(p.score) as avg_score
    FROM students s
    JOIN performance p
    ON s.student_id = p.student_id
    GROUP BY s.student_id
    ORDER BY avg_score DESC
    LIMIT 1
""").fetchone()

    def get_weak_subjects(
    self,
    student_id
):
        query = """
    SELECT
        subject,
        ROUND(
            AVG(score),
            2
        )
    FROM performance
    WHERE student_id = ?
    GROUP BY subject
    HAVING AVG(score) < 65
    """
        return self.conn.execute(
        query,
        (student_id,)
    ).fetchall()

    def get_class_average(self):

        return self.conn.execute("""
    SELECT AVG(score)
    FROM performance
""").fetchone()[0]
    
    def get_subject_scores(self, student_id):
        query = """
        SELECT subject,
               AVG(score)
        FROM performance
        WHERE student_id=?
        GROUP BY subject
    """
        return self.conn.execute(query, (student_id,)).fetchall()