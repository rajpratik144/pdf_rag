from pathlib import Path

from pypdf import PdfReader

from models.metadata import PDFMetadata

from core.validators import ContentValidator
from core.logger import get_logger

from core.exceptions import (
    MetadataExtractionError
)
from core.hash_utils import (get_file_hash)

logger = get_logger(__name__)


class MetadataExtractor:

    @staticmethod
    def extract(
        pdf_path: str,
        user_id: str
    ) -> PDFMetadata:

        try:

            pdf_path = Path(pdf_path)

            if not pdf_path.exists():

                raise FileNotFoundError(
                    f"{pdf_path} does not exist."
                )

            reader = PdfReader(
                str(pdf_path)
            )

            meta = reader.metadata
            file_hash = get_file_hash(pdf_path)
            metadata = PDFMetadata(
                
                filename=pdf_path.name,
                
                file_hash=file_hash,
                
                title=getattr(
                    meta,
                    "title",
                    None
                ),
                author=getattr(
                    meta,
                    "author",
                    None
                ),
                subject=getattr(
                    meta,
                    "subject",
                    None
                ),
                creator=getattr(
                    meta,
                    "creator",
                    None
                ),
                producer=getattr(
                    meta,
                    "producer",
                    None
                ),
                creation_date=getattr(
                    meta,
                    "creation_date",
                    None
                ),
                modification_date=getattr(
                    meta,
                    "modification_date",
                    None
                ),
                page_count=len(
                    reader.pages
                ),
                user_id=user_id,
            )

            if not ContentValidator.is_valid_metadata(
                metadata
            ):
                raise MetadataExtractionError(
                    "Metadata validation failed."
                )

            logger.info(
                f"Metadata extracted "
                f"successfully from "
                f"{pdf_path.name}"
            )

            return metadata

        except Exception as e:

            logger.error(
                f"Metadata extraction failed "
                f"for {pdf_path}: {e}"
            )

            raise MetadataExtractionError(
                str(e)
            ) from e