# ==========================================
# File: api/routes.py
# ==========================================


import shutil
from pathlib import Path
from fastapi import (APIRouter,UploadFile,File,Form)
from api.models import (AskRequest,DeleteResponse,UploadResponse)
from document_ai import (DocumentAI)
from config import Config

router = APIRouter()
document_ai = DocumentAI()

Config.UPLOAD_DIR.mkdir(
    parents=True,
    exist_ok=True
)

@router.post("/upload",response_model=UploadResponse)
async def upload_document(user_id: str = Form(...),file: UploadFile = File(...)):
    file_path = (Config.UPLOAD_DIR /file.filename)

    with open(file_path,"wb") as buffer:

        shutil.copyfileobj(file.file,buffer)

    document_id = (
        document_ai.upload(
            pdf_path=str(file_path),user_id=user_id))
    return {"document_id":document_id}


@router.post("/ask")
def ask_question(request: AskRequest):
    return (
        document_ai.ask(
            question=request.question,
            user_id=request.user_id,
            document_id=request.document_id))

@router.get("/documents/{user_id}")
def list_documents(user_id: str):
    return (document_ai.list_documents(user_id))


@router.delete("/documents/{document_id}",response_model=DeleteResponse)
def delete_document(document_id: str):
    return {"deleted":document_ai.delete_document(document_id)}