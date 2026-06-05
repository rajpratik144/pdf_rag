# ==========================================
# File: ingestion/table_extractor.py
# ==========================================


import pdfplumber
from langchain_core.documents import (Document)

class TableExtractor:

    @staticmethod
    def extract(pdf_path):
        documents = []
        with pdfplumber.open(pdf_path) as pdf:

            for page_num, page in enumerate(pdf.pages,start=1):
                tables = (page.extract_tables())

                for table in tables:
                    rows = []
                    for row in table:
                        cleaned = [str(cell) if cell else "" for cell in row]

                        rows.append(" | ".join(cleaned))

                    table_text = ("\n".join(rows))

                    documents.append(
                        Document(page_content=f"TABLE:\n"f"{table_text}",
                            metadata={
                                "page":page_num,
                                "type":"table"}
                        )
                    )

        return documents