from core.logger import get_logger
logger = get_logger(__name__)

class Retriever:
    def __init__(self,vector_store):
        self.vector_store = vector_store

    def retrieve(self,query,user_id,document_id=None,k=5):
        try:
            filters = {"user_id": user_id}

            if document_id: 
                filters["document_id"] = document_id

            results = (self.vector_store.similarity_search(query=query,user_id=user_id,document_id=document_id,k=k))

            logger.info(f"Retrieved "f"{len(results)} chunks.")

            return results

        except Exception as e:
            logger.error(f"Retrieval failed: {e}")
            raise