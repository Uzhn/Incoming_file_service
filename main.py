from fastapi import FastAPI
from src.api.api import api_router
from src.core.config import settings

app = FastAPI(title="Incoming-file-service")

app.include_router(api_router, prefix=settings.API_STR)
