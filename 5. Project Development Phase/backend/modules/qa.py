from . import gemini_client


def get_answer(question: str) -> str:
    prompt = (
        f"Answer this student's question accurately and concisely, then add one or two "
        f"sentences of useful educational context.\n\nQuestion: {question}"
    )
    return gemini_client.generate(prompt)
