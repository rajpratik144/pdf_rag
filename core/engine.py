import os

from retrieval.retriever import Retriever
from qa.qa_service import QAService
from storage.vector_store import VectorStore
from storage.metadata_store import MetadataStore
from core.metadata_router import MetadataRouter

from core.logger import get_logger

logger = get_logger(__name__)

# this is the main engine that handles all the non llm tasks before the query/question is sent to llm.
class RAGEngine:
    def __init__(self):
        # these are all the variables made using the objects of the classes imported foem different files.
        self.vector_store = (VectorStore())
        self.retriver = (Retriever(self.vector_store))
        self.qa_service = (QAService(api_key=os.getenv("GROQ_API_KEY")))
        self.metadata_store = (MetadataStore())

# this function metadata from the metadata_store file
    def _answer_metadata(self,field,user_id,document_id=None):
        if document_id:
            document = (self.metadata_store.get_document(document_id))

            if not document:
                return ("Document not found.")

            documents = [document]

        else:

            documents = (self.metadata_store.get_user_documents(user_id))
        
        return "\n".join(f"{doc['filename']}: {doc.get(field) or 'Not Available'}"for doc in documents)

    def ask(self,question,user_id,document_id=None,k=5):
        field = (MetadataRouter.get_field(question))

        if field:
            return {
                "answer":self._answer_metadata(field=field,user_id=user_id,document_id=document_id),
                "sources": []}
        
        documents = (
            self.retriver.retrieve(query=question,user_id=user_id,document_id=document_id,k=k))

        documents = (documents[:2])

        answer = (self.qa_service.ask(question=question,documents=documents))

        sources = []

        seen = set()

        for doc in documents:
            source = (doc.metadata.get("filename"),doc.metadata.get("page"))

            if source in seen:
                continue
            seen.add(source)
            sources.append({"filename":source[0],"page":source[1]})

        return {"answer":answer,"sources":sources}

    def list_documents(self,user_id):

        return (self.metadata_store.get_user_documents(user_id))

    def get_document(self,document_id):

        return (self.metadata_store.get_document(document_id))

    def delete_document(self,document_id):

        document = (self.metadata_store.get_document(document_id))

        if not document:
            return False

        self.vector_store.delete_document(document_id)
        self.metadata_store.delete_document(document_id)

        return True