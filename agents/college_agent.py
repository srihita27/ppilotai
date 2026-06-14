import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    groq_api_key=os.getenv("GROQ_API_KEY")
)

def ask_college_question(context, question):
    prompt = f"""
Answer ONLY from the provided context.

Context:
{context}

Question:
{question}

If answer is not in context, say:
'I could not find this information in the college FAQ.'
"""

    response = llm.invoke(prompt)
    return response.content