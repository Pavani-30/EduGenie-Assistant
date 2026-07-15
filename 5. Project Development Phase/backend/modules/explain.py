from . import gemini_client


def get_explanation(topic: str, level: str = "beginner") -> str:
    prompt = (
        f"Explain the concept '{topic}' to a {level} student in simple, clear language. "
        "Use short paragraphs and, where useful, a small example. "
        "Keep it educational and accurate."
    )
    return gemini_client.generate(prompt)
