from fastapi import APIRouter

from src.api.routers import flights_router

api_router = APIRouter()

api_router.include_router(flights_router)
