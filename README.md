# Document AI

A multimodal PDF RAG system built with Python, FastAPI, ChromaDB, Gemini, and Groq.

## Features

- PDF ingestion
- Text extraction
- Table extraction
- Image understanding
- Metadata querying
- Multi-document support
- Duplicate detection
- User-level document isolation
- FastAPI endpoints

## API Endpoints

| Method | Endpoint | Description |
|----------|-------------|----------------|
| POST | /upload | Upload a PDF |
| POST | /ask | Ask questions |
| GET | /documents/{user_id} | List documents |
| DELETE | /documents/{document_id} | Delete a document |

## Tech Stack

- Python
- FastAPI
- ChromaDB
- LangChain
- Google Gemini
- Groq
- pdfplumber
- PyMuPDF

## Run Locally

```bash
pip install -r requirements.txt
uvicorn api.main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

to access the API documentation.

## Current Capabilities

- Text RAG
- Table RAG
- Image RAG
- Metadata Routing
- Multi-user document management
- REST API interface
