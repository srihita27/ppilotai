import sqlite3
import pandas as pd

conn = sqlite3.connect(
    "database/students.db"
)

students = pd.read_csv(
    "database/students.csv"
)

performance = pd.read_csv(
    "database/performance.csv"
)

students.to_sql(
    "students",
    conn,
    if_exists="replace",
    index=False
)

performance.to_sql(
    "performance",
    conn,
    if_exists="replace",
    index=False
)

conn.commit()

conn.close()

print(
    "Database created successfully."
)