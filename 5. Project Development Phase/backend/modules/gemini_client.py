"""
Central Gemini API client shared by every module.
Requires GOOGLE_API_KEY to be set in a .env file (see .env.example).

Uses the current `google-genai` SDK (the older `google-generativeai`
package is deprecated).
"""

import os
from google import genai

_API_KEY = os.getenv("GOOGLE_API_KEY")
_MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

_client = genai.Client(api_key=_API_KEY) if _API_KEY else None


def generate(prompt: str) -> str:
    """Send a prompt to Gemini and return the text response."""
    if not _client:
        raise RuntimeError(
            "GOOGLE_API_KEY is not set. Copy .env.example to .env and add your key."
        )
    response = _client.models.generate_content(model=_MODEL_NAME, contents=prompt)
    return response.text.strip()
