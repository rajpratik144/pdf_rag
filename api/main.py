from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI
from api.routes import router
from config import Config

Config.validate()

# Create required folders

Path(
    Config.UPLOAD_DIR
).mkdir(
    parents=True,
    exist_ok=True
)

Path(
    Config.TEMP_DIR
).mkdir(
    parents=True,
    exist_ok=True
)

Path(
    Config.CHROMA_DIR
).mkdir(
    parents=True,
    exist_ok=True
)

Path(
    Config.METADATA_FILE
).parent.mkdir(
    parents=True,
    exist_ok=True
)

Path(Config.LOG_DIR).mkdir(
    parents=True,
    exist_ok=True
)

app = FastAPI(
    title="Document AI API",
    version="1.0.0"
)

app.include_router(router)