from ingestion.processor import (DocumentProcessor)
from core.engine import (RAGEngine)

class DocumentAI:
    def __init__(self):
        self.processor = (DocumentProcessor())
        self.engine = (RAGEngine())

    def upload(self,pdf_path,user_id):
        return (self.processor.ingest_pdf(pdf_path=pdf_path,user_id=user_id))

    def upload_directory(self,directory,user_id):
        return (self.processor.ingest_directory(directory=directory,user_id=user_id))

    def ask(self,question,user_id,document_id=None):
        return (self.engine.ask(question=question,user_id=user_id,document_id=document_id))

    def list_documents(self,user_id):
        return (self.engine.list_documents(user_id))

    def get_document(self,document_id):
        return (self.engine.get_document(document_id))
    
    def delete_document(self,document_id):
        return (self.engine.delete_document(document_id))