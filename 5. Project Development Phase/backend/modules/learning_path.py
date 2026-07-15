from . import gemini_client


def get_learning_path(topic: str) -> str:
    prompt = (
        f"Create a structured learning roadmap for '{topic}' with three sections: "
        "Beginner, Intermediate, and Advanced. Under each section list the key subtopics "
        "to study in order, plus one short study recommendation per section."
    )
    return gemini_client.generate(prompt)
