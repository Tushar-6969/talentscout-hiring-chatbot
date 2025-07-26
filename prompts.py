# prompts.py

def greeting_prompt():
    return (
        "👋 Hello! I’m your AI Hiring Assistant at TalentScout.\n"
        "I'll help with your initial interview screening.\n"
        "Let’s get started by collecting a few basic details!"
    )


def info_collection_prompt():
    return (
        "Please provide the following candidate details:\n"
        "- Full Name\n"
        "- Email Address\n"
        "- Phone Number\n"
        "- Years of Experience\n"
        "- Desired Position(s)\n"
        "- Current Location\n"
    )


def tech_stack_prompt():
    return (
        "Now, please list the technologies you are skilled in — such as programming languages, "
        "frameworks, databases, tools, etc. (Example: Python, React, MongoDB, Docker)"
    )


def generate_tech_question_prompt(tech_stack: str):
    """
    Generate a prompt to instruct LLM to create interview questions based on a candidate's tech stack.
    
    Args:
        tech_stack (str): A comma-separated string like "Python, React, MySQL"

    Returns:
        str: A prompt for the LLM to generate technical questions
    """
    return f"""
You are acting as a senior technical interviewer.

Generate 3 to 5 technical interview questions for a candidate who is skilled in the following technologies: {tech_stack}.

Guidelines:
- Ask 1 question per tech if possible.
- Keep the questions relevant to real-world job applications.
- Make them short, clear, and suitable for 1–3 years of experience.
- Do not include answers or explanations.
- Output only the questions.
"""


def fallback_prompt(user_input: str):
    return (
        f"Sorry, I didn’t understand that input: '{user_input}'.\n"
        "Please provide the requested information or type 'exit' to end the chat."
    )


def end_conversation_prompt():
    return (
        "✅ Thank you for providing your details!\n"
        "Our team will review your responses and get in touch soon.\n"
        "You may now close the chat or type 'exit'."
    )
