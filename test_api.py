import json

from rag.api import process_complaint


def main():
    complaint = "There has been a problem with the water supply in our area."

    result = process_complaint(
        complaint=complaint,
        top_k=3,
    )

    print(
        json.dumps(
            result,
            indent=2,
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()