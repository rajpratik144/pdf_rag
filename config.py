import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()


class Config:

    # ==========================
    # API Keys
    # ==========================

    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

    # ==========================
    # Base Paths
    # ==========================

    BASE_DIR = Path(__file__).resolve().parent

    UPLOAD_DIR = Path(
        os.getenv(
            "UPLOAD_DIR",
            str(BASE_DIR / "uploads")
        )
    )

    TEMP_DIR = Path(
        os.getenv(
            "TEMP_DIR",
            str(BASE_DIR / "temp")
        )
    )

    DB_DIR = Path(
        os.getenv(
            "DB_DIR",
            str(BASE_DIR / "db")
        )
    )

    CHROMA_DIR = Path(
        os.getenv(
            "CHROMA_DIR",
            str(DB_DIR / "chroma")
        )
    )

    METADATA_FILE = Path(
        os.getenv(
            "METADATA_FILE",
            str(DB_DIR / "metadata.json")
        )
    )

    LOG_DIR = Path(
        os.getenv(
            "LOG_DIR",
            str(BASE_DIR / "logs")
        )
    )

    # ==========================
    # Models
    # ==========================

    EMBEDDING_MODEL = os.getenv(
        "EMBEDDING_MODEL",
        "gemini-embedding-2-preview"
    )

    IMAGE_MODEL = os.getenv(
        "IMAGE_MODEL",
        "gemini-2.5-flash"
    )

    QA_MODEL = os.getenv(
        "QA_MODEL",
        "llama-3.3-70b-versatile"
    )

    # ==========================
    # Chunking
    # ==========================

    CHUNK_SIZE = int(
        os.getenv("CHUNK_SIZE", 1000)
    )

    CHUNK_OVERLAP = int(
        os.getenv("CHUNK_OVERLAP", 150)
    )

    @classmethod
    def validate(cls):

        required = {
            "GOOGLE_API_KEY": cls.GOOGLE_API_KEY,
            "GROQ_API_KEY": cls.GROQ_API_KEY,
        }

        missing = [
            key
            for key, value in required.items()
            if not value
        ]

        if missing:
            raise ValueError(
                f"Missing environment variables: {missing}"
            )