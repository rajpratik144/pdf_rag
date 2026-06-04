from pathlib import Path
from pypdf import PdfReader

from langchain_core.documents import Document

from core.logger import get_logger
from core.validators import ContentValidator

from core.exceptions import (
    TextExtractionError
)

logger = get_logger(__name__)


class TextExtractor:

    @staticmethod
    def extract(pdf_path: str):

        try:

            pdf_path = Path(pdf_path)

            if not pdf_path.exists():
                raise FileNotFoundError(
                    f"{pdf_path} does not exist."
                )

            reader = PdfReader(
                str(pdf_path)
            )

            documents = []

            for page_num, page in enumerate(
                reader.pages,
                start=1
            ):

                text = page.extract_text()

                if not ContentValidator.is_valid_text(
                    text
                ):
                    continue

                documents.append(
                    Document(
                        page_content=text,
                        metadata={
                            "page": page_num,
                            "source":
                                pdf_path.name
                        }
                    )
                )

            if not documents:

                raise TextExtractionError(
                    "No valid text found."
                )

            logger.info(
                f"Extracted "
                f"{len(documents)} pages"
            )

            return documents

        except Exception as e:

            logger.error(
                f"Text extraction failed: {e}"
            )

            raise TextExtractionError(
                str(e)
            ) from e