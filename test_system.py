from dotenv import load_dotenv

load_dotenv()

from core.engine import (
    RAGEngine
)

engine = RAGEngine()

questions = [

    # Annual Report

    # "Who is the author of the annual report?",

    "What does the revenue chart show?",

    # "What does page 4 discuss?",

    # "What is shown in the financial table?",

    # # Resume

    # "What is the name of the candidate?",

    # "What skills are mentioned in the resume?",

    # "What internships has the candidate completed?",

    # # Electricity Bill

    # "What is the consumer number?",

    # "What is the bill amount?",

    # "What is the GSTIN number?"
]

for question in questions:

    print("\n")
    print("=" * 100)

    print(
        f"QUESTION: {question}"
    )

    print("=" * 100)

    try:

        result = engine.ask(
            question=question,
            user_id="user_1"
        )

        print("\nANSWER:\n")

        print(
            result["answer"]
        )

        print("\nSOURCES:\n")

        for source in result["sources"]:

            print(source)

    except Exception as e:

        print(
            f"ERROR: {e}"
        )

    print("\n")