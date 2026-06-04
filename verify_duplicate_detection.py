from dotenv import load_dotenv

load_dotenv()

from ingestion.processor import (
    DocumentProcessor
)

processor = (
    DocumentProcessor()
)

document_id = (
    processor.ingest_pdf(
        pdf_path=
        "documents/annual_report.pdf",

        user_id=
        "user_1"
    )
)

print(document_id)