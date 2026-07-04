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

---

# 🛠️ Technology Stack

| Category | Technology |
|----------|------------|
| **Programming Language** | Python |
| **Frontend** | Streamlit |
| **Database** | SQLite |
| **Data Processing** | Pandas |
| **Data Visualization** | Plotly |
| **Large Language Model (LLM)** | Llama 3.3 70B Versatile |
| **LLM Provider** | Groq |
| **LLM Framework** | LangChain |
| **AI Workflow Orchestration** | LangGraph |
| **Vector Database** | ChromaDB |
| **Embedding Model** | Sentence Transformers |
| **Retrieval Technique** | Retrieval-Augmented Generation (RAG) |
| **Natural Language Processing** | Natural Language to SQL |
| **PDF Processing** | PyPDF |
| **Environment Management** | Python Dotenv |
| **UI Styling** | Custom CSS + Streamlit Components |
| **Charts & Analytics** | Plotly Express |
| **Version Control** | Git & GitHub |
| **Deployment** | Streamlit Community Cloud |

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

# 🤖 AI Modules

## 🏫 AI College Assistant (RAG)

PrepPilot AI uses Retrieval-Augmented Generation (RAG) to answer college-related questions accurately.

Students can ask about:

- 🎓 Admissions
- 🏫 Campus Facilities
- 📚 Academic Regulations
- 📝 Examination Policies
- 💼 Placements
- 🛏 Hostel Facilities
- 💳 Fee Structure
- 📅 Academic Calendar

The assistant retrieves the most relevant document chunks from ChromaDB before generating responses using the Groq LLM. Every response includes source attribution and a confidence score.

---

## 💬 AI SQL Assistant

Students can interact with their academic database using natural language.

Example queries include:

- What are my weak subjects?
- Which subject has my highest score?
- Show my average marks.
- Which subjects are above the class average?
- How many tests have I completed?

PrepPilot automatically:

- Converts natural language into SQL
- Executes the query on the SQLite database
- Displays the results in a table
- Generates interactive charts when applicable
- Explains the results in simple language using AI

---

## 📝 AI Test Generator

Students can generate personalized practice tests by selecting:

- Subject
- Difficulty Level (Easy / Medium / Hard)
- Number of Questions

The AI dynamically creates multiple-choice questions with answers and explanations, helping students prepare effectively.

---

## 📊 Learning Analytics

The analytics dashboard provides valuable insights into student performance, including:

- 🏆 Student Rank
- 📈 Average Score
- 🎓 Class Average
- ⭐ Top Performer
- 📉 Weak Subject Detection
- 📚 Subject-wise Performance
- 📊 Interactive Plotly Charts
- 🎯 Personalized Learning Recommendations

---

# 📸 Screenshots

Add screenshots of your application after deployment.

Example:

```text
assets/
├── login.png
├── dashboard.png
├── analytics.png
├── college_assistant.png
├── sql_assistant.png
└── test_generator.png
```

---

# 🌟 Key Highlights

- 🔐 Secure Student Authentication
- 🤖 AI-Powered College Assistant
- 📚 Retrieval-Augmented Generation (RAG)
- 💬 Natural Language to SQL
- 📝 AI-Based Test Generation
- 📊 Interactive Analytics Dashboard
- 📈 Dynamic Plotly Visualizations
- 🎯 Personalized Learning Insights
- 📚 Confidence Scores & Source Attribution
- ⚡ Powered by Groq Llama 3.3
- ☁ Streamlit Cloud Deployment Ready

---

# 🌍 Applications

PrepPilot AI can be adopted by:

- 🎓 Universities
- 🏫 Colleges
- 📚 Coaching Institutes
- 💻 E-learning Platforms
- 👨‍🏫 Faculty Members
- 👩‍🎓 Students
- 📖 Academic Advisors

---

# 🔮 Future Improvements

- 🎙 Voice-Based AI Assistant
- 📄 PDF Performance Reports
- 📅 AI Study Planner
- 📱 Mobile Responsive Design
- 🔔 Smart Notifications
- 📈 Grade Prediction using Machine Learning
- 🧠 Multi-Agent AI Collaboration
- 🌐 Multi-University Support
- 💬 Persistent Chat History

---

# 🚀 Deployment

PrepPilot AI can be deployed using:

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

⭐ If you found this project useful, consider giving it a ⭐ on GitHub!

</p>
