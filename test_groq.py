"""Task 1 smoke test for CivicAgent PK."""

from rag.groq_service import generate_response


def main() -> None:
    complaint = "Meri gali ki street lights do hafton se band hain."

    print("=" * 60)
    print("CivicAgent PK — Groq API Test")
    print("=" * 60)
    print(f"Complaint: {complaint}")
    print()
    print("Llama response:")
    print("-" * 60)

    response = generate_response(complaint)

    print(response)
    print("-" * 60)
    print("SUCCESS: Groq API connection is working.")


if __name__ == "__main__":
    main()
