# ==========================================
# File: api/main.py
# ==========================================


from dotenv import load_dotenv
load_dotenv()
from fastapi import (FastAPI)
from api.routes import (router)


app = FastAPI(title="Document AI API",version="1.0.0")

app.include_router(router)

