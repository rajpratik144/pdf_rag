# ==========================================
# File: test_system.py
# ==========================================

from dotenv import load_dotenv

load_dotenv()

from document_ai import DocumentAI


def main():

    print("=" * 60)
    print("INITIALIZING DOCUMENT AI")
    print("=" * 60)

    doc_ai = DocumentAI()

    print("✓ Initialization successful\n")

    # --------------------------------------
    # Upload
    # --------------------------------------

    pdf_path = input("PDF Path: ").strip()

    pdf_path = pdf_path.strip("'\"")

    user_id = input("User ID: ").strip()

    print("\nUploading document...\n")

    document_id = doc_ai.upload(
        pdf_path=pdf_path,
        user_id=user_id
    )

    print(f"✓ Upload Complete")
    print(f"Document ID : {document_id}")
    print("\nVector Count:")
    print(doc_ai.processor.vector_store.count())

    # --------------------------------------
    # List Documents
    # --------------------------------------

    print("\nListing documents...\n")

    docs = doc_ai.list_documents(user_id)

    print(f"Found {len(docs)} document(s)\n")

    for i, doc in enumerate(docs, start=1):

        print(f"{i}.")
        print(f"Filename    : {doc['filename']}")
        print(f"Document ID : {doc['document_id']}")
        print(f"Pages       : {doc['page_count']}")
        print()

    # --------------------------------------
    # Metadata Query
    # --------------------------------------

    print("\nTesting metadata routing...\n")

    result = doc_ai.ask(
        question="How many pages are there?",
        user_id=user_id
    )

    print(result["answer"])
    print(result["sources"])

    # --------------------------------------
    # Normal RAG
    # --------------------------------------

    print("\nTesting RAG...\n")

    question = input(
        "\nAsk a question about the PDF:\n> "
    )

    result = doc_ai.ask(
        question=question,
        user_id=user_id
    )

    print("\nANSWER\n")
    print(result["answer"])

    print("\nSOURCES\n")
    for source in result["sources"]:
        print(source)

    # --------------------------------------
    # Get Document
    # --------------------------------------

    print("\nFetching document metadata...\n")

    doc = doc_ai.get_document(document_id)

    print(doc)

    # --------------------------------------
    # Delete
    # --------------------------------------

    delete = input(
        "\nDelete this document? (y/n): "
    )

    if delete.lower() == "y":

        doc_ai.delete_document(
            document_id
        )

        print("✓ Document deleted.")

    print("\nTEST COMPLETE")


if __name__ == "__main__":
    main()