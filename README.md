# 🎓 PrepPilot AI – Intelligent Academic Assistant

<p align="center">

**An AI-powered student learning platform that combines Retrieval-Augmented Generation (RAG), Natural Language to SQL, Learning Analytics, and Generative AI to provide personalized academic assistance.**

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?logo=streamlit)
![LangChain](https://img.shields.io/badge/LangChain-LLM-green)
![Groq](https://img.shields.io/badge/Groq-LLM-orange)
![ChromaDB](https://img.shields.io/badge/Vector%20DB-ChromaDB-blueviolet)
![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?logo=sqlite)
![Status](https://img.shields.io/badge/Status-Completed-success)

</p>

---

# 📖 Overview

PrepPilot AI is an intelligent student assistant designed to enhance academic performance through AI-powered learning support.

Instead of simply displaying grades or static dashboards, PrepPilot allows students to:

- 💬 Ask questions about their academic performance using natural language
- 📊 Analyze performance through interactive dashboards
- 🤖 Chat with an AI College Assistant using Retrieval-Augmented Generation (RAG)
- 📝 Generate practice tests automatically using LLMs
- 🧠 Query academic records using Natural Language to SQL
- 📈 Receive personalized insights and recommendations

---

# 🚀 Features

| Feature | Description |
|---------|-------------|
| 🔐 Student Login | Secure authentication using Student ID and Password |
| 📊 Learning Analytics | Interactive academic dashboard with performance metrics |
| 📈 Subject Performance Charts | Visualize marks using Plotly charts |
| 🏫 AI College Assistant | RAG-powered chatbot answering college-related questions |
| 📝 AI Test Generator | Automatically generates subject-wise practice tests |
| 💬 Natural Language to SQL | Ask questions like "What are my weakest subjects?" |
| 🤖 AI Explanations | Converts SQL results into human-friendly insights |
| 📚 Source Citation | Displays retrieved RAG documents with confidence scores |
| 🎨 Modern UI | Professional Streamlit interface with custom sidebar and branding |

---

# 🧠 AI Modules

## 1️⃣ Learning Analytics

PrepPilot analyzes student performance and displays:

- Overall Average
- Class Average
- Student Rank
- Weak Subjects
- Top Student
- Subject-wise Performance Charts

---

## 2️⃣ AI College Assistant (RAG)

Students can ask questions such as:

- Admission Process
- Attendance Rules
- Examination Policies
- College Facilities
- Placements
- Academic Regulations

The assistant retrieves relevant documents using ChromaDB and generates accurate answers with source citations.

---

## 3️⃣ AI Test Generator

Students can generate customized practice tests by selecting:

- Subject
- Difficulty Level
- Number of Questions

The questions are generated dynamically using Groq LLM.

---

## 4️⃣ Natural Language to SQL

Students can ask:

> "What are my weakest subjects?"

> "Show my highest scoring subject."

> "What is my average score?"

PrepPilot automatically:

Natural Language

⬇

SQL Query

⬇

SQLite Database

⬇

Results Table

⬇

AI Explanation

---

# 🏗 System Architecture

```text
                     Student
                        │
                        ▼
               Streamlit Frontend
                        │
        ┌───────────────┼────────────────┐
        │               │                │
        ▼               ▼                ▼
 Learning Analytics   RAG Assistant   SQL Assistant
        │               │                │
        ▼               ▼                ▼
 SQLite Database    ChromaDB       SQLite Database
        │               │                │
        └───────────────┼────────────────┘
                        ▼
                 Groq LLM (Llama 3)
                        │
                        ▼
                AI Generated Response
