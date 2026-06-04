from dotenv import load_dotenv

load_dotenv()

from storage.vector_store import (
    VectorStore
)

store = VectorStore()

docs = store.db.get()

counts = {}

for metadata in docs["metadatas"]:

    filename = metadata.get(
        "filename"
    )

    counts[filename] = (
        counts.get(
            filename,
            0
        ) + 1
    )

print()

print(
    "Chunk Counts"
)

print(
    "=" * 40
)

for filename, count in counts.items():

    print(
        f"{filename}: {count}"
    )