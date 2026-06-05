# ==========================================
# File: storage/metadata_store.py
# ==========================================


import json
from pathlib import Path
from core.logger import get_logger
from core.exceptions import (StorageError)
logger = get_logger(__name__)

class MetadataStore:
    def __init__(self,storage_path="db/metadata.json"):

        self.storage_path = Path(storage_path)
        self.storage_path.parent.mkdir(parents=True,exist_ok=True)

        if not self.storage_path.exists():
            self.storage_path.write_text("[]")

    def _load(self):

        try:
            with open(self.storage_path,"r",encoding="utf-8") as file:
                return json.load(file)

        except Exception as e:
            logger.error(f"Failed to load metadata: {e}")
            raise StorageError(str(e)) from e
        
    def _save(self, data):

        try:
            with open(self.storage_path,"w",encoding="utf-8") as file:
                json.dump(data,file,indent=4,ensure_ascii=False,default=str)

        except Exception as e:
            logger.error(f"Failed to save metadata: {e}")
            raise StorageError(str(e)) from e
        
    def add_document(self,metadata):

        data = self._load()
        data.append(metadata.to_dict())
        self._save(data)
        logger.info(f"Stored metadata for "f"{metadata.filename}")

    def get_user_documents(self,user_id):

        data = self._load()
        return [doc for doc in data if doc["user_id"] == user_id]

    def get_document(self,document_id):

        data = self._load()
        for doc in data:
            if (doc["document_id"]== document_id):
                return doc
            
    def find_by_hash(self,file_hash,user_id):
        
        data = self._load()
        for document in data:
            if(document.get("file_hash")==file_hash and document.get("user_id")==user_id):
                return document
        return None
    
    def delete_document(self,document_id):

        data = self._load()
        updated_data = [doc for doc in data if doc["document_id"] != document_id]
        self._save(updated_data)
        logger.info(f"Deleted metadata for {document_id}")

    def document_exists(self,document_id):

        data = self._load()
        return any(doc["document_id"]== document_id for doc in data )