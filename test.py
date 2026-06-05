# # # from dotenv import load_dotenv

# # # load_dotenv()

# # # from ingestion.processor import (
# # #     DocumentProcessor
# # # )

# # # processor = (
# # #     DocumentProcessor()
# # # )

# # # processor.ingest_directory(
# # #     "documents",
# # #     "user_1"
# # # )

# # from dotenv import load_dotenv

# # load_dotenv()

# # # from storage.vector_store import (
# # #     VectorStore
# # # )

# # # store = VectorStore()

# # # results = store.db.similarity_search(
# # #     query="Budget Actual Q4 2024",
# # #     k=3
# # # )

# # # for doc in results:

# # #     print("\n")
# # #     print(doc.metadata)

# # #     print(
# # #         doc.page_content
# # #     )

# # from core.engine import RAGEngine

# # engine = RAGEngine()

# # result = engine.ask(
# #     question="what are the Profile Summary?",
# #     user_id="user_1"
# # )

# # print(result["answer"])
# # print(result["sources"])

# from dotenv import load_dotenv

# load_dotenv()

# from core.engine import RAGEngine

# engine = RAGEngine()

# tests = [

#     # ---------------------------
#     # Metadata Routing
#     # ---------------------------

#     "How many pages are there in all the files?",

#     "Who is the author of all the files?",

#     "What is the title of all the files?",

#     # ---------------------------
#     # Text RAG
#     # ---------------------------

#     "What does the revenue chart show?",

#     "What does page 4 discuss?",

#     "Who is the candidate in the resume?",

#     "What skills are mentioned in the resume?",

#     # ---------------------------
#     # Table RAG
#     # ---------------------------

#     "What was the Actual value for Q4 2024?",

#     "What was the Budget for Q2 2024?",

#     "Show the financial table summary.",

# ]

# for question in tests:

#     print("\n")
#     print("=" * 100)
#     print(f"QUESTION: {question}")
#     print("=" * 100)

#     result = engine.ask(
#         question=question,
#         user_id="user_1"
#     )

#     print("\nANSWER:\n")
#     print(result["answer"])

#     print("\nSOURCES:\n")

#     if result["sources"]:

#         for source in result["sources"]:

#             print(source)

#     else:

#         print("Metadata Query (No Sources)")



# from dotenv import load_dotenv

# load_dotenv()

# from core.engine import RAGEngine

# engine = RAGEngine()

# resume_id = engine.list_documents(
#     "user_1"
# )[1]["document_id"]

# result = engine.ask(
#     question="How many pages are there?",
#     user_id="user_1",
#     document_id=resume_id
# )

# print(result["answer"])

# from ingestion.image_extractor import (
#     ImageExtractor
# )

# images = (
#     ImageExtractor.extract(
#         "documents/annual_report.pdf"
#     )
# )

# print(images)

# from dotenv import load_dotenv

# load_dotenv()

# from ingestion.image_description_extractor import (ImageDescriptionService)

# extractor = (ImageDescriptionService())

# description = (extractor.describe_image("pratik raj singh_GJIMT_FSPBOOTCAMP_002072.jpg"))

# print(description)

# from ingestion.page_renderer import (
#     PageRenderer
# )

# image_path = (
#     PageRenderer.render_page(
#         pdf_path="documents/annual_report.pdf",
#         page_number=5
#     )
# )

# print(image_path)

from dotenv import load_dotenv

load_dotenv()

# from ingestion.image_description_extractor import (
#     ImageDescriptionExtractor
# )

# documents = (
#     ImageDescriptionExtractor.extract(
#         "documents/annual_report.pdf"
#     )
# )

# for doc in documents:

#     print()
#     print(doc.metadata)
#     print()
#     print(doc.page_content)

# from ingestion.processor import (
#     DocumentProcessor
# )

# processor = (
#     DocumentProcessor()
# )

# processor.ingest_directory(
#     "documents",
#     "user_1"
# )

# from core.engine import (
#     RAGEngine
# )

# engine = (
#     RAGEngine()
# )

# result = (
#     engine.ask(
#     question=
#     "Which business segment has the largest market share?",
#     user_id=
#     "user_1"
# )
# )

# print(
#     result["answer"]
# )

# print(
#     result["sources"]
# )

# from ingestion.image_extractor import ImageExtractor

# print(
#     ImageExtractor.extract(
#         "documents/pratik-resume(2310264).pdf"
#     )
# )

# from dotenv import load_dotenv

# load_dotenv()

# from ingestion.image_description_extractor import (
#     ImageDescriptionExtractor
# )

# docs = (
#     ImageDescriptionExtractor.extract(
#         "documents/pratik-resume(2310264).pdf"
#     )
# )

# for doc in docs:

#     print(doc.metadata)
#     print()
#     print(doc.page_content)

# from dotenv import load_dotenv

# load_dotenv()

# from document_ai import (
#     DocumentAI
# )

# ai = (
#     DocumentAI()
# )

# result = (
#     ai.ask(
#         question=
#         "Describe the pie chart.",

#         user_id=
#         "user_1"
#     )
# )

# print(
#     result["answer"]
# )

# print(
#     result["sources"]
# )
from dotenv import load_dotenv

load_dotenv()

from document_ai import (
    DocumentAI
)

ai = (
    DocumentAI()
)

document_id = (
    ai.upload(
        "documents/pratik-resume(2310264).pdf",
        "user_2"
    )
)

print(
    document_id
)

print()

print(

    ai.ask(

        question=
        "What skills are mentioned?",

        user_id=
        "user_2",

        document_id=
        document_id

    )

)