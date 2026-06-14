def build_prompt(
    context,
    difficulty,
    weak_topics,
    difficulty_config
):

    return f"""
You are an expert university exam setter.

Context:
{context}

Weak Topics:
{weak_topics}

Generate EXACTLY 10 MCQs.

Difficulty:
{difficulty}

Difficulty Rules:
{difficulty_config["description"]}

Bloom's Level:
{difficulty_config["blooms"]}

Concepts Per Question:
{difficulty_config["concepts_per_question"]}

Distractor Strength:
{difficulty_config["distractor_strength"]}

Requirements:

1. Use only the provided context.
2. Prioritize weak topics.
3. 4 options per question.
4. One correct answer.
5. Include explanation.
6. Return ONLY valid JSON.

Example:

[
 {{
   "question":"What is a compiler?",
   "options": {{
      "A":"Option A",
      "B":"Option B",
      "C":"Option C",
      "D":"Option D"
   }},
   "correct":"B",
   "explanation":"Explanation"
 }}
]
"""