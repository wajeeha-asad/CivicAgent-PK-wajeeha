"""Small Groq client wrapper for CivicAgent PK."""

import os

from dotenv import load_dotenv
from groq import Groq

from .prompts import SYSTEM_PROMPT


load_dotenv()


def get_client() -> Groq:
    """Create and return an authenticated Groq client."""
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key or api_key == "your_groq_api_key_here":
        raise RuntimeError(
            "GROQ_API_KEY is missing. Create a .env file and add your Groq API key."
        )

    return Groq(api_key=api_key)


def generate_response(
    complaint: str,
    system_prompt: str = SYSTEM_PROMPT,
) -> str:
    """Send a complaint to Llama through Groq and return its text response."""

    if not complaint.strip():
        raise ValueError("Complaint cannot be empty.")

    model = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")
    client = get_client()

    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": complaint.strip()},
        ],
        temperature=0.2,
    )

    return completion.choices[0].message.content.strip()
