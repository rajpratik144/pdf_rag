from typing import Optional


class ContentValidator:

    ERROR_PATTERNS = [
        "429",
        "RESOURCE_EXHAUSTED",
        "quota exceeded",
        "rate limit",
        "traceback",
        "exception",
        "internal server error",
        "service unavailable",
        "permission denied",
        "authentication failed",
    ]

    @classmethod
    def is_valid_text(
        cls,
        text: Optional[str]
    ) -> bool:

        if text is None:
            return False

        if not isinstance(text, str):
            return False

        text = text.strip()

        if len(text) == 0:
            return False

        lower_text = text.lower()

        for pattern in cls.ERROR_PATTERNS:

            if pattern.lower() in lower_text:
                return False

        return True

    @classmethod
    def is_valid_metadata(
        cls,
        metadata
    ) -> bool:

        if metadata is None:
            return False

        if not hasattr(
            metadata,
            "document_id"
        ):
            return False

        return True