from dotenv import load_dotenv

load_dotenv()

from core.engine import (
    RAGEngine
)

engine = RAGEngine()

ANNUAL_REPORT_ID = (
    "dbfd9145-5d59-40a2-9106-5db6ba206de4"
)

result = engine.ask(

    question=
    "What does the revenue chart show?",

    user_id=
    "user_1",

    document_id=
    ANNUAL_REPORT_ID

)

print(
    result["answer"]
)

print()

for source in result["sources"]:

    print(source)