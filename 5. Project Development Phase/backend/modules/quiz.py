from . import gemini_client


def generate_quiz(topic: str, num_questions: int = 5) -> str:
    prompt = (
        f"Create a {num_questions}-question multiple-choice quiz on '{topic}' for self-assessment. "
        "For each question give 4 options labeled A-D, then on a new line write "
        "'Answer: <letter>'. Number the questions."
    )
    return gemini_client.generate(prompt)
