<p align="center">
  <img src="./assets/favicon.png" alt="PrepPilot AI Logo" width="220"/>
</p>

<h1 align="center">PrepPilot AI</h1>

<p align="center">
<b>Intelligent Student Learning & Analytics Platform</b>
<br>
AI-powered academic assistance using Retrieval-Augmented Generation (RAG), Natural Language to SQL, Learning Analytics, Adaptive Test Generation, and Large Language Models.
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?logo=streamlit)
![LangChain](https://img.shields.io/badge/LangChain-LLM%20Framework-green)
![LangGraph](https://img.shields.io/badge/LangGraph-Agent%20Workflow-6A5ACD)
![Groq](https://img.shields.io/badge/Groq-Llama%203.3-orange)
![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector%20Database-purple)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?logo=sqlite)
![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Charts-3F4F75?logo=plotly)
![Status](https://img.shields.io/badge/Status-Completed-success)

</p>

---

# 📖 Overview

PrepPilot AI is an AI-powered academic assistant that transforms traditional student portals into an intelligent learning platform.

Rather than simply displaying marks and attendance, PrepPilot leverages Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), Natural Language to SQL, and learning analytics to deliver personalized academic support.

Students can interact with their academic data conversationally, generate customized assessments, receive AI-powered explanations, and gain actionable insights into their performance—all from a single intuitive dashboard.

The platform enables students to:

- 🔐 Securely log in using Student ID & Password
- 🏫 Chat with an AI-powered College Assistant using RAG
- 📝 Generate personalized MCQ practice tests
- 💬 Query academic records using Natural Language
- 📊 Explore interactive learning analytics dashboards
- 📈 Visualize subject-wise performance
- 🎯 Identify weak subjects automatically
- 🤖 Receive AI-generated explanations and recommendations
- 📚 View confidence scores and document sources for AI responses

---

# 🚀 Features

| Feature | Description |
|---------|-------------|
| 🔐 Student Authentication | Secure login system using Student ID & Password |
| 🏫 AI College Assistant | Retrieval-Augmented chatbot answering university-related questions |
| 📝 AI Test Generator | Generates customized MCQ tests based on subject and difficulty |
| 💬 Natural Language to SQL | Ask academic questions in plain English |
| 📊 Student Analytics Dashboard | Displays rankings, averages, weak subjects and insights |
| 📈 Interactive Charts | Plotly-based performance visualizations |
| 📚 Source Attribution | Shows retrieved documents used for AI responses |
| 🎯 Confidence Score | Displays retrieval confidence for every AI answer |
| 🤖 AI Explanations | Explains SQL query results in natural language |
| 🎨 Modern UI | Custom Streamlit interface with responsive dashboard |

---

# 📌 System Architecture

```text
                      Student Login
                            │
                            ▼
                  Authentication System
                            │
        ┌───────────────────┼───────────────────┐
        ▼                   ▼                   ▼
 Learning Analytics   AI College Assistant   AI SQL Assistant
        │                   │                   │
        ▼                   ▼                   ▼
 SQLite Database     Chroma Vector DB     SQLite Database
        │                   │                   │
        ▼                   ▼                   ▼
 Performance Data   Similarity Retrieval   SQL Generation
        │                   │                   │
        └───────────────┬───┴───────────────────┘
                        ▼
               Groq Large Language Model
                        │
        ┌───────────────┼───────────────────┐
        ▼               ▼                   ▼
 AI Responses     Test Generation     SQL Explanations
                        │
                        ▼
              Interactive Streamlit UI
```
---

# 🛠 Tech Stack

| Category | Stack |
|:---------|:------|
| 🖥 **Frontend** | Streamlit, Custom CSS |
| ⚙️ **Backend** | Python |
| 🤖 **AI** | Groq (Llama 3.3), LangChain, LangGraph |
| 📚 **RAG Pipeline** | ChromaDB, Sentence Transformers |
| 🗄 **Database** | SQLite |
| 📊 **Analytics** | Pandas, Plotly |
| 📄 **Document Processing** | PyPDF |
| ☁️ **Deployment** | Streamlit Community Cloud |
| 🔧 **Version Control** | Git & GitHub |

---

# 📂 Project Structure

```text
PrepPilot-AI/
│
├── agents/
│   ├── college_agent.py
│   ├── sql_chat_agent.py
│   ├── student_agent.py
│   └── test_generator.py
│
├── analytics/
│   └── sql_agent.py
│
├── database/
│   ├── students.db
│   ├── students.csv
│   └── performance.csv
│
├── rag/
│   └── college_rag/
│       ├── documents/
│       ├── retriever.py
│       ├── ingest.py
│       └── chroma_db/
│
├── assets/
│   ├── banner.png
│   ├── favicon.png
│   └── mainlogo.png
│
├── app.py
├── requirements.txt
├── .env
├── README.md
└── .gitignore
```

---

# 📊 Application Workflow

```text
                     Student Login
                           │
                           ▼
                  Authentication System
                           │
      ┌────────────────────┼────────────────────┐
      ▼                    ▼                    ▼
Learning Analytics   AI College Assistant   AI SQL Assistant
      │                    │                    │
      ▼                    ▼                    ▼
 SQLite Database     Chroma Vector DB     SQLite Database
      │                    │                    │
      ▼                    ▼                    ▼
Performance Data   Similarity Retrieval   SQL Generation
      │                    │                    │
      └────────────────────┼────────────────────┘
                           ▼
                  Groq Large Language Model
                           │
        ┌──────────────────┼──────────────────┐
        ▼                  ▼                  ▼
 AI Responses      AI Test Generation    SQL Explanations
                           │
                           ▼
               Interactive Streamlit Dashboard
```
---

# 🤖 Core AI Modules

| Module | Description |
|--------|-------------|
| 🏫 **College Assistant (RAG)** | Answers university-related queries using Retrieval-Augmented Generation (RAG) over institutional documents with source attribution and confidence scores. |
| 💬 **AI SQL Assistant** | Converts natural language into SQL, executes queries on the academic database, visualizes results, and generates AI-powered explanations. |
| 📝 **Test Generator** | Dynamically generates personalized MCQ assessments based on subject and selected difficulty using LLMs. |
| 📊 **Learning Analytics** | Provides performance insights including student rank, averages, weak subjects, trends, and interactive visualizations. |

---

# ⚡ Key Capabilities

- 🔐 Secure Student Authentication
- 🤖 Retrieval-Augmented Generation (RAG)
- 💬 Natural Language to SQL
- 📝 AI-Powered Test Generation
- 📊 Interactive Learning Analytics
- 📈 Plotly Performance Visualizations
- 📚 Source Attribution & Confidence Scores
- ⚡ Groq Llama 3.3 Integration 
- 🎨 Modern Streamlit Dashboard
- ☁️ Cloud Deployment Ready
---

# 🌍 Use Cases

PrepPilot AI is designed for modern educational environments including:

- 🎓 Universities & Colleges
- 💻 Learning Management Systems (LMS)
- 📚 Coaching Institutes
- 👩‍🎓 Students
- 👨‍🏫 Faculty & Academic Advisors

---

# 🛣️ Roadmap

- [ ] Voice-enabled AI Assistant 
- [ ] Personalized Study Planner
- [ ] AI-based Grade Prediction
- [ ] PDF Performance Reports
- [ ] Smart Notifications & Reminders
- [ ] Persistent Chat History
- [ ] Multi-Agent Collaboration
- [ ] Multi-University Support
- [ ] Mobile-Optimized Interface

---

# 🚀 Deployment

PrepPilot AI can be deployed on:

- ☁️ Streamlit Community Cloud
- 🚂 Railway
- 🎨 Render
- 🤗 Hugging Face Spaces
- 🐳 Docker


---

# 👩‍💻 Author

**Srihita Kotagiri**

- GitHub: https://github.com/srihita27
- LinkedIn: https://www.linkedin.com/in/srihita-kotagiri/

---

<p align="center">

- If you found this project useful, consider giving it a ⭐ on GitHub!

</p>
