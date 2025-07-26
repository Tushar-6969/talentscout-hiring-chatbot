
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize Gemini model
model = genai.GenerativeModel("gemini-2.0-flash")

def generate_questions(tech_stack):
    """
    Generates 3–5 technical questions based on the candidate's declared tech stack using Gemini.

    Args:
        tech_stack (str): Comma-separated tech stack string (e.g. "Python, React, MongoDB")

    Returns:
        List[str]: A list of up to 5 technical questions
    """

    if not tech_stack:
        return []

    techs = [tech.strip() for tech in tech_stack.split(",") if tech.strip()]
    formatted_tech = ", ".join(techs)

    prompt = f"""
You are acting as a technical recruiter for a software engineering position.

Generate 3 to 5 technical interview questions tailored to assess a candidate's skills in the following tech stack: {formatted_tech}.

- Keep questions clear, short, and relevant to real-world job scenarios.
- Ensure one question per technology is included, where possible.
- Do not include answers.
"""

    try:
        response = model.generate_content(prompt)
        raw_text = response.text.strip()

        # Split into lines, remove empty ones, and clean formatting
        questions = [
    line.lstrip("0123456789.-) ").strip()
    for line in raw_text.split("\n")
    if line.strip() and not line.lower().startswith("q1: okay")
]


        # Limit to max 5 questions
        return questions[:5]

    except Exception as e:
        print(f"[ERROR] Gemini API failed: {e}")
        return []
