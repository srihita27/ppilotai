import sqlite3


class AnalyticsAgent:

    def __init__(self):

        self.conn = sqlite3.connect(
            "database/students.db",
            check_same_thread=False
        )

    def get_rank(
        self,
        student_id
    ):

        cur = self.conn.cursor()

        cur.execute(
            """
            SELECT rank
            FROM(
                SELECT
                student_id,
                RANK() OVER(
                    ORDER BY avg_score DESC
                ) rank
                FROM students
            )
            WHERE student_id=?
            """,
            (student_id,)
        )

        row = cur.fetchone()

        if row:
            return row[0]

        return "N/A"

    def get_average_score(
        self,
        student_id
    ):

        cur = self.conn.cursor()

        cur.execute(
            """
            SELECT avg_score
            FROM students
            WHERE student_id=?
            """,
            (student_id,)
        )

        row = cur.fetchone()

        if row:
            return row[0]

        return 0

    def get_recommended_difficulty(
        self,
        student_id
    ):

        score = self.get_average_score(
            student_id
        )

        if score < 50:
            return "Easy"

        elif score < 75:
            return "Medium"

        return "Hard"