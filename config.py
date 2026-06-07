# ==========================================
# File: config.py
# ==========================================


import os
from pathlib import Path


class Config:

    # ==========================
    # API Keys
    # ==========================

    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

    # ==========================
    # Storage Paths
    # ==========================

    BASE_DIR = Path(__file__).resolve().parent

    UPLOAD_DIR = BASE_DIR / "uploads"

    TEMP_DIR = BASE_DIR / "temp"

    DB_DIR = BASE_DIR / "db"

    CHROMA_DIR = DB_DIR / "chroma"

    METADATA_FILE = DB_DIR / "metadata.json"

    LOG_DIR = BASE_DIR / "logs"

    # ==========================
    # Embedding Model
    # ==========================

    EMBEDDING_MODEL = "gemini-embedding-2-preview"

    # ==========================
    # LLM Models
    # ==========================

    IMAGE_MODEL = "gemini-2.5-flash"

    QA_MODEL = "llama-3.3-70b-versatile"

    # ==========================
    # Chunking
    # ==========================

    CHUNK_SIZE = 1000

    CHUNK_OVERLAP = 150