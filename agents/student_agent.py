import pandas as pd
from analytics.sql_agent import SQLAgent


class StudentAgent:

    def __init__(self):

        # Only used for names / metadata
        self.students = pd.read_csv("database/students.csv")

        # Single source of truth for marks
        self.sql_agent = SQLAgent()

    def get_all_students(self):

        return self.students[
            ["student_id", "name"]
        ].to_dict("records")

    def get_student(self, student_id):

        row = self.students[
            self.students.student_id == student_id
        ]

        return row.iloc[0].to_dict()

    def get_weak_topics(self, student_id, subject):

        try:

            perf = pd.read_csv("database/performance.csv")

            filtered = perf[
                (perf.student_id == student_id) &
                (perf.subject == subject)
            ]

            weak = filtered[filtered.score < 50]

            return weak.topic.tolist()

        except:

            return []

    def suggest_difficulty(self, student_id):

        # ✅ Get REAL average from SQL (source of truth)
        avg = self.sql_agent.get_average_score(student_id)

        # 🔒 safety guard against accidental scaling bugs
        if avg > 1000:
            avg = avg / 100
        elif avg > 100:
            avg = avg  # already raw mistake case, keep but safe

        # normalize if needed (optional safety)
        avg = float(avg)

        # ✅ correct logic
        if avg < 50:
            return "Easy"
        elif avg < 75:
            return "Medium"
        else:
            return "Hard"
        
    def login(
    self,
    student_id,
    password):
        row = self.students[
        (
            self.students.student_id
            == student_id
        )
        &
        (
            self.students.password
            == password
        )
    ]
        if len(row) == 0:
            return None
        return row.iloc[0].to_dict()