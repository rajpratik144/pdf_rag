# ==========================================
# File: core/exceptions.py
# ==========================================


"""
Custom exceptions used throughout the
Document Intelligence Engine.
"""


class DocumentIntelligenceError(Exception):
    """
    Base exception for the project.
    """
    pass


class PDFProcessingError(
    DocumentIntelligenceError
):
    """
    Raised when PDF processing fails.
    """
    pass


class MetadataExtractionError(
    DocumentIntelligenceError
):
    """
    Raised when metadata extraction fails.
    """
    pass


class TextExtractionError(
    DocumentIntelligenceError
):
    """
    Raised when text extraction fails.
    """
    pass


class EmbeddingError(
    DocumentIntelligenceError
):
    """
    Raised when embedding generation fails.
    """
    pass


class StorageError(
    DocumentIntelligenceError
):
    """
    Raised when storage operations fail.
    """
    pass


class ValidationError(
    DocumentIntelligenceError
):
    """
    Raised when content validation fails.
    """
    pass


class RetrievalError(
    DocumentIntelligenceError
):
    """
    Raised when retrieval fails.
    """
    pass