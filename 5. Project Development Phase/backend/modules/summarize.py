from . import gemini_client


def summarize_text(text: str) -> str:
    prompt = (
        "Summarize the following study material into clear, concise bullet points "
        f"that a student can review quickly:\n\n{text}"
    )
    return gemini_client.generate(prompt)
