from rag.retriever import retrieve_policies


def main():
    complaint = "Gali mein drain block hai aur pani jama ho raha hai."

    print("=" * 60)
    print("CivicAgent PK — ChromaDB Retrieval Test")
    print("=" * 60)

    print(f"Complaint: {complaint}")
    print()

    results = retrieve_policies(
        complaint,
        top_k=3,
    )

    print(f"Retrieved policies: {len(results)}")
    print()

    for index, result in enumerate(results, start=1):
        metadata = result["metadata"]

        print(f"--- Result {index} ---")
        print(f"Title: {metadata['title']}")
        print(f"Category: {metadata['category']}")
        print(f"Authority: {metadata['authority']}")
        print(f"Source type: {metadata['source_type']}")
        print(f"Distance: {result['distance']}")
        print()
        print(result["document"])
        print()

    print("=" * 60)
    print("SUCCESS: ChromaDB retrieval is working.")
    print("=" * 60)


if __name__ == "__main__":
    main()