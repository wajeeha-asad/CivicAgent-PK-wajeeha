from rag.rag_service import retrieve_context


def main():
    complaint = "Meri gali ki street lights do hafton se band hain."

    result = retrieve_context(
        complaint,
        top_k=3,
    )

    print("=" * 60)
    print("CivicAgent PK — RAG Retrieval Service")
    print("=" * 60)

    print(f"Complaint: {result['complaint']}")
    print(f"Policies retrieved: {result['count']}")
    print()

    for index, policy in enumerate(
        result["retrieved_policies"],
        start=1,
    ):
        print(f"--- Policy {index} ---")
        print(f"Title: {policy['title']}")
        print(f"Category: {policy['category']}")
        print(f"Authority: {policy['authority']}")
        print(f"Source type: {policy['source_type']}")
        print(f"Distance: {policy['distance']}")
        print()

    print("=" * 60)
    print("SUCCESS: RAG retrieval service is working.")
    print("=" * 60)


if __name__ == "__main__":
    main()