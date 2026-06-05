# ==========================================
# File: api/models.py
# ==========================================

from pydantic import BaseModel
class AskRequest(BaseModel):
    question: str
    user_id: str
    document_id: str | None = None

class AskResponse(BaseModel):
    answer: str
    sources: list

class UploadResponse(BaseModel):
    document_id: str


class DeleteResponse(BaseModel):
    deleted: bool