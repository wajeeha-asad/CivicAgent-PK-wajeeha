import json

from rag.rag_service import process_complaint


def main():
    complaint = "There has been a problem with the water supply in our area."

    print("=" * 70)
    print("CivicAgent PK — COMPLETE RAG TEST")
    print("=" * 70)

    print()
    print("Citizen complaint:")
    print(complaint)

    print()
    print("Running ChromaDB retrieval + Groq generation...")
    print()

    result = process_complaint(
        complaint=complaint,
        top_k=3,
    )

    print("=" * 70)
    print("RETRIEVED POLICIES")
    print("=" * 70)

    for index, policy in enumerate(
        result["retrieved_policies"],
        start=1,
    ):
        print()
        print(f"Policy {index}")
        print(f"Title: {policy['title']}")
        print(f"Category: {policy['category']}")
        print(f"Authority: {policy['authority']}")
        print(f"Distance: {policy['distance']}")

    print()
    print("=" * 70)
    print("GROUNDED AI RESPONSE")
    print("=" * 70)

    print(
        json.dumps(
            result["analysis"],
            indent=2,
            ensure_ascii=False,
        )
    )

    print()
    print("=" * 70)
    print("SUCCESS: Complete RAG pipeline is working.")
    print("=" * 70)


if __name__ == "__main__":
    main()