# ==========================================
# File: embeddings/embedding_service.py
# ==========================================


import os
from langchain_google_genai import (GoogleGenerativeAIEmbeddings)
from core.logger import get_logger
from core.exceptions import (EmbeddingError)

logger = get_logger(__name__)

class EmbeddingService:
    def __init__(self):
        api_key = os.getenv("GOOGLE_API_KEY")
        
        if not api_key:
            raise EmbeddingError("GOOGLE_API_KEY not found.")
        
        try:
            self.embeddings = (GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001",google_api_key=api_key))

        except Exception as e:
            logger.error(f"Embedding initialization failed: {e}")
            raise EmbeddingError(str(e)) from e

    def get_embedding_model(self):
        return self.embeddings
    
    def test_connection(self):

        try:
            vector = self.embeddings.embed_query("hello world")
            logger.info(f"Embedding service working. "f"Dimension={len(vector)}")
            return True
        
        except Exception as e:
            logger.error(f"Embedding service failed: {e}")
            raise EmbeddingError(str(e)) from e