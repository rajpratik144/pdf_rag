from pathlib import Path        
from ingestion.metadata_extractor import (MetadataExtractor)
from ingestion.text_extractor import (TextExtractor)
from chunking.chunker import (DocumentChunker)
from storage.metadata_store import (MetadataStore)
from storage.vector_store import (VectorStore)
from core.logger import get_logger
from core.hash_utils import (get_file_hash)
from ingestion.table_extractor import (TableExtractor)
from ingestion.image_description_extractor import (ImageDescriptionExtractor)

logger = get_logger(__name__)

class DocumentProcessor:

    def __init__(self):
        self.metadata_store = (MetadataStore())
        self.vector_store = (VectorStore())
        self.chunker = (DocumentChunker())

    def ingest_pdf(self,pdf_path,user_id):
        file_hash = get_file_hash(pdf_path)
        existing_document = (self.metadata_store.find_by_hash(file_hash=file_hash,user_id=user_id))

        if existing_document:
            document_id = (existing_document["document_id"])

            if (self.vector_store.document_exists(document_id)):
                logger.info("Document already exists.")
                return document_id

            logger.warning("Metadata exists but vectors missing. Re-indexing document.")

        metadata = (MetadataExtractor.extract(pdf_path,user_id))
        self.metadata_store.add_document(metadata)
        text_documents = (
            TextExtractor.extract(
                pdf_path
            )
        )

        table_documents = (
            TableExtractor.extract(
                pdf_path
            )
        )

        image_documents = (
            ImageDescriptionExtractor.extract(
                pdf_path
            )
        )

        chunks = (
            self.chunker.chunk_documents(
                text_documents
            )
        )

        chunks.extend(
            table_documents
        )

        chunks.extend(
            image_documents
        )

        
        for chunk_id, chunk in enumerate(chunks):
            chunk.metadata.update(
                {"user_id":user_id,"document_id":metadata.document_id,
                    "filename":metadata.filename,"chunk_id":chunk_id})
        
        self.vector_store.add_documents(chunks)
        
        logger.info(f"{metadata.filename} ingested successfully.")

        return metadata.document_id
    
    def ingest_directory(self,directory,user_id):

        document_ids = []

        directory = Path(directory)

        pdf_files = (directory.glob("*.pdf"))

        for pdf_file in pdf_files:

            try:

                logger.info(f"Ingesting: "f"{pdf_file.name}")
                document_id = (self.ingest_pdf(pdf_path=str(pdf_file),user_id=user_id))

                document_ids.append(document_id)

            except Exception as e:

                logger.error(f"Failed to ingest "f"{pdf_file.name}: {e}")

        logger.info(f"Ingested {len(document_ids)} documents.")

        return document_ids