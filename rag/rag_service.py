from typing import Any

from .retriever import retrieve_policies


def retrieve_context(
    complaint: str,
    top_k: int = 3,
) -> dict[str, Any]:
    """
    Retrieve relevant civic policies and prepare them
    for the next RAG stage.
    """

    results = retrieve_policies(
        complaint=complaint,
        top_k=top_k,
    )

    policies = []

    for result in results:
        policies.append(
            {
                "id": result["id"],
                "title": result["metadata"]["title"],
                "category": result["metadata"]["category"],
                "authority": result["metadata"]["authority"],
                "source_type": result["metadata"]["source_type"],
                "source": result["metadata"]["source"],
                "text": result["document"],
                "distance": result["distance"],
            }
        )

    return {
        "complaint": complaint,
        "retrieved_policies": policies,
        "count": len(policies),
    }