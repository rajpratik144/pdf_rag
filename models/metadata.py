from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
import uuid


@dataclass
class PDFMetadata:
    """
    Metadata representation of a PDF document.
    """

    document_id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )

    filename: str = ""
    file_hash : str = ""
    title: Optional[str] = None
    author: Optional[str] = None
    subject: Optional[str] = None
    creator: Optional[str] = None
    producer: Optional[str] = None

    creation_date: Optional[datetime] = None
    modification_date: Optional[datetime] = None

    page_count: int = 0

    user_id: str = ""

    ingestion_timestamp: str = field(
        default_factory=lambda: datetime.utcnow().isoformat()
    )

    def _safe_datetime(self, value):
        """
        Convert datetime objects to ISO strings.
        """

        if value is None:
            return None

        if isinstance(value, datetime):
            return value.isoformat()

        return str(value)

    def to_dict(self) -> dict:
        """
        Convert metadata object into a JSON-safe dictionary.
        """

        return {
            "document_id": self.document_id,
            "filename": self.filename,
            "file_hash":self.file_hash,
            "title": self.title,
            "author": self.author,
            "subject": self.subject,
            "creator": self.creator,
            "producer": self.producer,
            "creation_date": self._safe_datetime(self.creation_date),
            "modification_date": self._safe_datetime(self.modification_date),
            "page_count": self.page_count,
            "user_id": self.user_id,
            "ingestion_timestamp": self.ingestion_timestamp,
        }