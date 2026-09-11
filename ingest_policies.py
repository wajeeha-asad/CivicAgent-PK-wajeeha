import json
from pathlib import Path

from rag.chroma_service import get_policy_collection


DATA_FILE = Path("data/civic_policies.json")


def load_policies():
    """
    Load civic policy records from the JSON file.
    """
    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"Policy file not found: {DATA_FILE}"
        )

    with DATA_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


def ingest_policies():
    """
    Store civic policies inside ChromaDB.
    """
    policies = load_policies()
    collection = get_policy_collection()

    ids = []
    documents = []
    metadatas = []

    for policy in policies:
        ids.append(policy["id"])
        documents.append(policy["text"])

        metadatas.append(
            {
                "title": policy["title"],
                "category": policy["category"],
                "authority": policy["authority"],
                "source_type": policy["source_type"],
                "source": policy["source"],
                "language": policy["language"],
            }
        )

    collection.upsert(
        ids=ids,
        documents=documents,
        metadatas=metadatas,
    )

    print("=" * 60)
    print("CivicAgent PK — Policy Ingestion")
    print("=" * 60)
    print(f"Policies loaded: {len(policies)}")
    print(f"Collection: {collection.name}")
    print(f"Total records in ChromaDB: {collection.count()}")
    print()
    print("SUCCESS: Policies stored in ChromaDB.")


if __name__ == "__main__":
    ingest_policies()