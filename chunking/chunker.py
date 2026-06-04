from langchain_core.documents import Document
from core.logger import get_logger
logger = get_logger(__name__)

class DocumentChunker:

    def __init__(self,chunk_size=1000,chunk_overlap=150):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def chunk_documents(self,documents):
        chunked_docs = []
        for doc in documents:
            text = doc.page_content
            start = 0
            while start < len(text):
                end = start + self.chunk_size
                chunk_text = text[start:end]
                metadata = doc.metadata.copy()
                chunked_docs.append(
                    Document(
                        page_content=chunk_text,
                        metadata=metadata
                    )
                )
                start += (
                    self.chunk_size
                    - self.chunk_overlap
                )

        logger.info(f"Created {len(chunked_docs)} chunks.")
        return chunked_docs
    

                                # WORKING AND THE REASON
# ------------------------------------------------------------------------------ #

# This code defines the Document Chunker. In the world of AI and "Chat with PDF"
# systems, you cannot feed a whole 100-page book into the AI all at once. You have
# to break it into smaller, bite-sized pieces.

# Think of this code as a "Smart Paper Shredder" that cuts a long document into
# overlapping strips so the AI can process them easily.

# 1. Key Concepts (The Settings)

# The chunker uses two main settings to control how it cuts the text:

#   - chunk_size (1000): This is the maximum length of each piece (measured in
#     characters). It’s like saying, "Each strip of paper can only be 1000 letters
#     long."
#   - chunk_overlap (150): This is the most important part. To make sure we don't
#     cut a sentence in half and lose its meaning, we repeat the last 150
#     characters of one chunk at the beginning of the next. This provides context.

# 2. How the Code Works (Step-by-Step)

# The Setup (__init__)

# It simply remembers the sizes you want for your chunks and overlap. It also sets
# up a Logger (a digital diary) to record how many pieces were created.

# The Action (chunk_documents)

# This function takes your list of documents and performs the following "Sliding
# Window" logic:

# 1.  Looping: It looks at every document in the list (Metadata, Raw Text, and
#     Vision Analysis).
# 2.  Slicing: It starts at the beginning of the text (Position 0). It takes a
#     slice of text from start to start + 1000.
# 3.  Preserving Metadata: It makes a copy of the original tags (like Page Number
#     or Type). This is vital because every small chunk needs to remember which
#     page it originally came from.
# 4.  Creating the New Document: it creates a brand new, smaller Document object
#     with that slice of text and the copied tags.
# 5.  The "Slide": Instead of jumping 1000 characters forward, it only jumps 850
#     characters (size - overlap).
#       - Example: Chunk 1 ends at character 1000. Chunk 2 starts at
#         character 850. The text between 850 and 1000 exists in both chunks.
# 6.  Reporting: Once it finishes all documents, it logs a message: "Created 45
#     chunks," so you know how much data you have.

# 3. Why do we need the "Overlap"?

# Imagine a PDF says: "The total profit for the year was $5 million."

#   - Without Overlap: Chunk 1 might end at "The total profit for the year" and
#     Chunk 2 starts with "was $5 million." Neither chunk makes sense on its own.
#   - With Overlap: Chunk 1 says "The total profit for the year was $5" and
#     Chunk 2 says "the year was $5 million." Now, no matter which chunk the AI
#     looks at, it has enough clues to understand the meaning.

# 4. Summary for Documentation

# | Component    | Simple Description                                                                     |
# | :----------- | :------------------------------------------------------------------------------------- |
# | **Input**    | A list of long `Document` objects.                                                     |
# | **Process**  | Uses a sliding window to cut text into 1000-character pieces.                          |
# | **Metadata** | Every chunk keeps the page number and source information of the original.              |
# | **Logging**  | Tracks the total number of pieces generated for system monitoring.                     |
# | **Output**   | A much longer list of small, overlapping `Document` objects ready for the AI database. |

# Technical Summary

# "The DocumentChunker implements a sliding-window strategy to segment text into
# manageable units. By utilizing a specific chunk_size and chunk_overlap, it
# ensures that semantic context is preserved across boundaries. This is a critical
# pre-processing step for Vector Database indexing, ensuring that retrieved
# segments contain complete information for the LLM to process."
