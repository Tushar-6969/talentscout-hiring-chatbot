# utils.py
import re

def is_exit_keyword(user_input: str) -> bool:
    """
    Checks if the user input contains any exit keywords to end the conversation.

    Args:
        user_input (str): The user-entered string.

    Returns:
        bool: True if an exit keyword is detected, False otherwise.
    """
    if not user_input:
        return False

    exit_keywords = ["exit", "quit", "bye", "end", "stop"]
    return user_input.strip().lower() in exit_keywords


def validate_input(field_key: str, response: str) -> tuple[bool, str]:
    """
    Validates user input based on the current question type.

    Args:
        field_key (str): One of the keys like 'name', 'email', etc.
        response (str): User's input text.

    Returns:
        Tuple[bool, str]: (is_valid, error_message_if_any)
    """
    if not response.strip():
        return False, "❗This field cannot be empty."

    if field_key == "name":
        if any(char.isdigit() for char in response):
            return False, "❗Name should not contain numbers."
    
    elif field_key == "email":
        if not re.match(r"[^@]+@[^@]+\.[^@]+", response):
            return False, "❗Invalid email format."

    elif field_key == "phone":
        if not response.isdigit() or len(response) < 7:
            return False, "❗Phone number should be numeric and at least 7 digits."

    elif field_key == "experience":
        if not response.isdigit() or int(response) < 0:
            return False, "❗Please enter a valid non-negative number."

    elif field_key == "tech_stack":
        if len(response.split(",")) < 1:
            return False, "❗Please enter at least one technology."

    return True, ""
