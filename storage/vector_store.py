from chromadb.config import Settings
from langchain_chroma import Chroma
from embeddings.embedding_service import (EmbeddingService)
from core.logger import get_logger
from core.exceptions import (StorageError)

logger = get_logger(__name__)

class VectorStore:
    def __init__(self,persist_directory="db/chroma"):
        try:
            embedding_service = (EmbeddingService())
            self.embeddings = (embedding_service.get_embedding_model())

            self.db = Chroma(
                collection_name="pdf_documents",
                embedding_function=self.embeddings,
                persist_directory=persist_directory
            )

        except Exception as e:
            logger.error(f"Vector store initialization "f"failed: {e}")

            raise StorageError(str(e)) from e

    def add_documents(self,documents):
        try:
            self.db.add_documents(documents)
            logger.info(f"Added "f"{len(documents)} "f"documents to vector store.")

        except Exception as e:

            logger.error(f"Failed to store documents: "f"{e}")
            raise StorageError(str(e)) from e

    def similarity_search(self,query,user_id,document_id=None,k=5):

        try:
            if document_id:
                filters = {"$and": [{"user_id":user_id},{"document_id":document_id}]}

            else:
                filters = {"user_id":user_id}

            results = self.db.similarity_search_with_score(query=query,k=k,filter=filters)
            logger.info(f"Retrieved {len(results)} chunks.")
            return [doc for doc, score in results
]
            # return results

        except Exception as e:

            logger.error(f"Similarity search failed: {e}")

            raise StorageError(str(e)) from e

    def delete_document(self,document_id):

        try:
            self.db.delete(where={"document_id":document_id})
            
            logger.info(f"Deleted document "f"{document_id}")

        except Exception as e:

            logger.error(f"Delete failed: {e}")

            raise StorageError(str(e)) from e

    def count(self):
        try:
            return (self.db._collection.count())
        except Exception as e:
            logger.error(f"Count failed: {e}")

            raise StorageError(str(e)) from e
    
    def document_exists(self,document_id):

        try:
            results = self.db.get(where={"document_id":document_id})
            return (len(results["ids"]) > 0)

        except Exception as e:
            logger.error(f"Document existence check failed: {e}")

            raise StorageError(str(e)) from e